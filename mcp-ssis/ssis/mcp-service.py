#!/usr/bin/env python3
"""
mcp-service.py — db-ssis

Runs inside a container with the SSIS-on-Linux runtime (mssql-server-is).
Wraps dtexec as a subprocess so .dtsx packages can be validated, run, and
benchmarked over MCP. Talks to a peer SQL Server container
(db-mcp-mssql) over the host network for state resets between benchmark
iterations.

This is a dev/benchmark rig — Microsoft does not support SSIS on Linux
in containers. Don't point it at anything important.

Register with Claude Code:
    claude mcp add db-ssis --transport http http://localhost:5190/mcp
"""

from __future__ import annotations

import asyncio
import os
import statistics
import subprocess
import tempfile
import time as time_mod
from pathlib import Path
from typing import Any, Optional

import pymssql
from fastmcp import FastMCP

# ── Config ────────────────────────────────────────────────────────────────────

PACKAGES_DIR = Path(os.environ.get("PACKAGES_DIR", "/packages")).resolve()
LOGS_DIR = PACKAGES_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

DTEXEC = os.environ.get("DTEXEC", "/opt/ssis/bin/dtexec")
GNU_TIME = "/usr/bin/time"

# Peer SQL Server for reset_sql between benchmark iterations.
MSSQL_HOST = os.environ.get("MSSQL_HOST", "host.containers.internal")
MSSQL_PORT = int(os.environ.get("MSSQL_PORT", "1433"))
MSSQL_USER = os.environ.get("MSSQL_USER", "sa")
MSSQL_PASSWORD = os.environ.get("MSSQL_SA_PASSWORD", "DevP@ssw0rd!42")

DEFAULT_RUNS = int(os.environ.get("DEFAULT_RUNS", "5"))
DEFAULT_WARMUP = int(os.environ.get("DEFAULT_WARMUP", "1"))
MAX_RUNS = 100
TAIL_BYTES = 8192


# ── Helpers ──────────────────────────────────────────────────────────────────

def _resolve_package(rel_path: str) -> Path:
    """Resolve a user-supplied relative path to an absolute path under
    PACKAGES_DIR. Rejects absolute paths and traversal attempts."""
    if not rel_path or rel_path.startswith("/"):
        raise ValueError("path must be relative to /packages")
    candidate = (PACKAGES_DIR / rel_path).resolve()
    try:
        candidate.relative_to(PACKAGES_DIR)
    except ValueError:
        raise ValueError(f"path {rel_path!r} escapes /packages")
    if not candidate.is_file():
        raise ValueError(f"file not found: {rel_path}")
    return candidate


def _tail(buf: str, n: int = TAIL_BYTES) -> str:
    if len(buf) <= n:
        return buf
    return f"... [{len(buf) - n} bytes truncated] ...\n" + buf[-n:]


def _dtexec_args(
    pkg: Path,
    validate: bool,
    params: Optional[dict],
    config: Optional[str],
) -> list[str]:
    """Build the dtexec argv. /Set entries are joined as 'propertypath;value'.
    /ConfigFile is resolved through the same packages-dir safety check."""
    args = [DTEXEC, "/File", str(pkg)]
    if validate:
        args += ["/Validate"]
    args += ["/Reporting", "V"]
    if config:
        cfg = _resolve_package(config)
        args += ["/ConfigFile", str(cfg)]
    if params:
        for k, v in params.items():
            args += ["/Set", f"{k};{v}"]
    return args


def _run_one(args: list[str], log_basename: str) -> dict[str, Any]:
    """Run dtexec under GNU time. Writes the full stdout+stderr+metrics to
    /packages/logs/<basename>-<timestamp>.log and returns a structured
    result. GNU time format: '%e %U %S %M %x' → wall, user, sys, RSS_kb, exit."""
    ts = time_mod.strftime("%Y%m%d-%H%M%S")
    log_path = LOGS_DIR / f"{log_basename}-{ts}.log"
    with tempfile.NamedTemporaryFile(
        mode="r", dir="/tmp", suffix=".time", delete=False
    ) as tf:
        timefile = tf.name
    try:
        timed_args = [GNU_TIME, "-o", timefile, "-f", "%e %U %S %M %x"] + args
        t0 = time_mod.monotonic_ns()
        proc = subprocess.run(timed_args, capture_output=True, text=True)
        wall_ns = time_mod.monotonic_ns() - t0

        # Parse GNU time output. If dtexec failed to exec, the file may be
        # empty or incomplete — fall back to wall_ns from monotonic and zeros.
        wall_s = user_s = sys_s = 0.0
        rss_kb = 0
        try:
            with open(timefile) as f:
                parts = f.read().strip().split()
            if len(parts) >= 5:
                wall_s = float(parts[0])
                user_s = float(parts[1])
                sys_s = float(parts[2])
                rss_kb = int(parts[3])
        except (OSError, ValueError):
            pass

        with open(log_path, "w") as f:
            f.write(f"# dtexec args: {args}\n")
            f.write(f"# exit_code: {proc.returncode}\n")
            f.write(
                f"# wall_s: {wall_s}  user_s: {user_s}  "
                f"sys_s: {sys_s}  peak_rss_kb: {rss_kb}\n"
            )
            f.write("\n# ── stdout ─────────────────────────────────\n")
            f.write(proc.stdout)
            f.write("\n# ── stderr ─────────────────────────────────\n")
            f.write(proc.stderr)

        return {
            "exit_code": proc.returncode,
            "wall_ms": round(wall_ns / 1e6, 2),
            "user_cpu_s": user_s,
            "sys_cpu_s": sys_s,
            "peak_rss_kb": rss_kb,
            "stdout_tail": _tail(proc.stdout),
            "stderr_tail": _tail(proc.stderr),
            "log_path": str(log_path.relative_to(PACKAGES_DIR)),
        }
    finally:
        try:
            os.unlink(timefile)
        except OSError:
            pass


def _reset(reset_sql: str, reset_database: str) -> None:
    """Execute reset SQL against the peer mssql container, autocommit."""
    with pymssql.connect(
        server=MSSQL_HOST,
        port=MSSQL_PORT,
        user=MSSQL_USER,
        password=MSSQL_PASSWORD,
        database=reset_database,
        autocommit=True,
        login_timeout=10,
        timeout=60,
    ) as c, c.cursor() as cur:
        cur.execute(reset_sql)


async def _to_thread(fn, *args, **kwargs):
    return await asyncio.to_thread(fn, *args, **kwargs)


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="db-ssis",
    instructions=(
        "SSIS-on-Linux workbench. Drop .dtsx files into the host packages/ "
        "directory; this service runs and benchmarks them via dtexec.\n\n"
        "Tools:\n"
        "  list_packages()        — enumerate .dtsx files\n"
        "  validate_package(path) — dtexec /Validate; use this to diagnose "
        "broken packages\n"
        "  run_package(path, params?, config?) — execute the package once\n"
        "  benchmark_package(path, runs, warmup, reset_sql?, reset_database?, "
        "params?, config?) — execute repeatedly and report timing stats\n\n"
        "Full per-run logs land under /packages/logs/<basename>-<timestamp>.log "
        "(visible from the host). dtexec exit codes: 0=success, 1=failure, "
        "3=cancel, 4=unable to find, 5=unable to load, 6=syntax error.\n\n"
        "NOTE: SSIS on Linux supports only a subset of components — packages "
        "that run on Windows may fail here. See the mcp-ssis README for the "
        "limit list."
    ),
)


@mcp.tool()
async def list_packages() -> str:
    """List all .dtsx files under /packages with size and mtime."""
    def _do() -> list[tuple[str, int, str]]:
        out: list[tuple[str, int, str]] = []
        for p in sorted(PACKAGES_DIR.rglob("*.dtsx")):
            try:
                rel = p.relative_to(PACKAGES_DIR)
                st = p.stat()
                out.append(
                    (
                        str(rel),
                        st.st_size,
                        time_mod.strftime(
                            "%Y-%m-%d %H:%M", time_mod.localtime(st.st_mtime)
                        ),
                    )
                )
            except OSError:
                continue
        return out

    pkgs = await _to_thread(_do)
    if not pkgs:
        return (
            f"No .dtsx packages found under {PACKAGES_DIR}.\n"
            "Drop files into the host packages/ directory and try again."
        )
    width = max(len(p[0]) for p in pkgs)
    lines = [f"{len(pkgs)} package(s) in {PACKAGES_DIR}:", ""]
    for path, size, mtime in pkgs:
        lines.append(f"  {path.ljust(width)}  {size:>10} bytes  {mtime}")
    return "\n".join(lines)


@mcp.tool()
async def validate_package(path: str) -> str:
    """
    Validate a .dtsx package via dtexec /Validate. The SSIS engine reports
    whether the package is well-formed and runnable on this Linux-SSIS host.
    Useful for diagnosing packages that fail to run.

    Args:
        path: Relative path under /packages (e.g. 'simple/copy.dtsx').
    """
    try:
        pkg = await _to_thread(_resolve_package, path)
    except ValueError as e:
        return f"VALIDATE FAILED ✗\n{e}"

    args = _dtexec_args(pkg, validate=True, params=None, config=None)
    basename = "validate-" + Path(path).stem
    result = await _to_thread(_run_one, args, basename)

    verdict = (
        "VALID ✓"
        if result["exit_code"] == 0
        else f"INVALID ✗  exit={result['exit_code']}"
    )
    return (
        f"VALIDATE {verdict}  ({result['wall_ms']} ms)\n"
        f"package:  {path}\n"
        f"log:      {result['log_path']}\n"
        f"\n── stdout (tail) ──\n{result['stdout_tail']}"
        f"\n── stderr (tail) ──\n{result['stderr_tail']}"
    )


@mcp.tool()
async def run_package(
    path: str,
    params: dict[str, str] = None,
    config: str = None,
) -> str:
    """
    Run a .dtsx package once. Returns exit code, timing, and tails of
    stdout/stderr. Full log is written under /packages/logs.

    Args:
        path: Relative .dtsx path under /packages.
        params: Optional /Set arguments. Keys are SSIS property paths
                (e.g. '\\Package.Variables[FilePath].Value'); values are
                passed through to dtexec as-is.
        config: Optional relative path to a .dtsConfig file (/ConfigFile).
    """
    try:
        pkg = await _to_thread(_resolve_package, path)
    except ValueError as e:
        return f"RUN FAILED ✗\n{e}"

    args = _dtexec_args(pkg, validate=False, params=params, config=config)
    basename = "run-" + Path(path).stem
    result = await _to_thread(_run_one, args, basename)

    status = (
        "OK ✓" if result["exit_code"] == 0 else f"FAIL ✗  exit={result['exit_code']}"
    )
    cpu = result["user_cpu_s"] + result["sys_cpu_s"]
    return (
        f"RUN {status}  wall={result['wall_ms']} ms  "
        f"cpu={cpu:.2f}s  peak_rss={result['peak_rss_kb']} KB\n"
        f"package:  {path}\n"
        f"log:      {result['log_path']}\n"
        f"\n── stdout (tail) ──\n{result['stdout_tail']}"
        f"\n── stderr (tail) ──\n{result['stderr_tail']}"
    )


@mcp.tool()
async def benchmark_package(
    path: str,
    runs: int = None,
    warmup: int = None,
    reset_sql: str = None,
    reset_database: str = "master",
    params: dict[str, str] = None,
    config: str = None,
) -> str:
    """
    Run a package N times and report timing statistics over the measured
    runs. The first `warmup` runs are discarded from the stats.

    Before each iteration (including warmups), if reset_sql is provided, it
    is executed against the peer SQL Server with autocommit. Use this for
    e.g. TRUNCATE+reload of input tables, or
    'DBCC DROPCLEANBUFFERS; CHECKPOINT;' for cold-cache runs.

    Args:
        path: Relative .dtsx path under /packages.
        runs: Total iterations including warmups (default 5, max 100).
        warmup: Iterations to discard from stats (default 1).
        reset_sql: Optional T-SQL run before each iteration.
        reset_database: Database for reset_sql (default 'master').
        params: /Set parameters applied to every iteration.
        config: Optional .dtsConfig path applied to every iteration.
    """
    runs = runs if runs is not None else DEFAULT_RUNS
    warmup = warmup if warmup is not None else DEFAULT_WARMUP
    if runs < 1 or runs > MAX_RUNS:
        return f"BENCHMARK FAILED ✗\nruns must be between 1 and {MAX_RUNS}"
    if warmup < 0 or warmup >= runs:
        return f"BENCHMARK FAILED ✗\nwarmup must be in [0, runs)"

    try:
        pkg = await _to_thread(_resolve_package, path)
    except ValueError as e:
        return f"BENCHMARK FAILED ✗\n{e}"

    args = _dtexec_args(pkg, validate=False, params=params, config=config)
    basename = "bench-" + Path(path).stem

    per_run: list[dict[str, Any]] = []

    for i in range(runs):
        if reset_sql:
            try:
                await _to_thread(_reset, reset_sql, reset_database)
            except pymssql.Error as e:
                return (
                    f"BENCHMARK ABORTED ✗  iteration {i + 1}/{runs}\n"
                    f"reset_sql failed against {MSSQL_HOST}:{MSSQL_PORT}/"
                    f"{reset_database}\n{e}"
                )
        r = await _to_thread(_run_one, args, f"{basename}-iter{i + 1:02d}")
        per_run.append(r)

    measured = per_run[warmup:]
    wall_ms = [r["wall_ms"] for r in measured]
    cpu_s = [r["user_cpu_s"] + r["sys_cpu_s"] for r in measured]
    rss_kb = [r["peak_rss_kb"] for r in measured]

    def _stats(xs: list[float]) -> dict[str, float]:
        if not xs:
            return {"min": 0, "p50": 0, "max": 0, "mean": 0, "stdev": 0}
        s = sorted(xs)
        return {
            "min": s[0],
            "p50": s[len(s) // 2],
            "max": s[-1],
            "mean": round(statistics.mean(xs), 2),
            "stdev": round(statistics.stdev(xs), 2) if len(xs) > 1 else 0,
        }

    wall_stats = _stats(wall_ms)
    cpu_stats = _stats(cpu_s)
    rss_stats = _stats(rss_kb)
    failures = [(i + 1, r) for i, r in enumerate(per_run) if r["exit_code"] != 0]

    lines = [
        f"BENCHMARK  runs={runs}  warmup={warmup}  measured={len(measured)}",
        f"package:    {path}",
        f"reset_sql:  {'yes (' + reset_database + ')' if reset_sql else 'no'}",
        f"params:     {params if params else '(none)'}",
        f"config:     {config if config else '(none)'}",
        "",
        f"wall_ms     min={wall_stats['min']}  p50={wall_stats['p50']}  "
        f"max={wall_stats['max']}  mean={wall_stats['mean']}  "
        f"stdev={wall_stats['stdev']}",
        f"cpu_s       min={cpu_stats['min']:.2f}  p50={cpu_stats['p50']:.2f}  "
        f"max={cpu_stats['max']:.2f}  mean={cpu_stats['mean']:.2f}  "
        f"stdev={cpu_stats['stdev']:.2f}",
        f"peak_rss_kb min={rss_stats['min']}  p50={rss_stats['p50']}  "
        f"max={rss_stats['max']}  mean={rss_stats['mean']}  "
        f"stdev={rss_stats['stdev']}",
        "",
        "per-iteration (* = warmup, discarded from stats):",
    ]
    for i, r in enumerate(per_run, start=1):
        tag = "*" if i <= warmup else " "
        verdict = "ok" if r["exit_code"] == 0 else f"FAIL exit={r['exit_code']}"
        cpu = r["user_cpu_s"] + r["sys_cpu_s"]
        lines.append(
            f"  {tag} #{i:02d}  wall={r['wall_ms']:>8} ms  "
            f"cpu={cpu:>5.2f}s  rss={r['peak_rss_kb']:>8} KB  "
            f"{verdict}  log={r['log_path']}"
        )
    if failures:
        lines += ["", f"⚠ {len(failures)} iteration(s) failed — see log files."]
    return "\n".join(lines)


@mcp.tool()
async def connection_info() -> str:
    """Diagnostic info: packages/logs paths, dtexec location, and the peer
    SQL Server used for reset_sql in benchmarks."""
    return (
        "ssis service:\n"
        f"  mcp url:        http://localhost:5190/mcp\n"
        f"  packages dir:   {PACKAGES_DIR}  (host-mounted)\n"
        f"  logs dir:       {LOGS_DIR}\n"
        f"  dtexec:         {DTEXEC}\n"
        "\n"
        "peer mssql (for reset_sql):\n"
        f"  host:           {MSSQL_HOST}\n"
        f"  port:           {MSSQL_PORT}\n"
        f"  user:           {MSSQL_USER}\n"
        f"  conn str:       Server={MSSQL_HOST},{MSSQL_PORT};"
        f"User Id={MSSQL_USER};Password=<MSSQL_SA_PASSWORD>;"
        f"TrustServerCertificate=yes\n"
    )


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"PACKAGES_DIR={PACKAGES_DIR}")
    print(f"DTEXEC={DTEXEC}")
    print(f"peer mssql: {MSSQL_HOST}:{MSSQL_PORT} as {MSSQL_USER}")
    print(f"defaults: runs={DEFAULT_RUNS}, warmup={DEFAULT_WARMUP}")
    print("Starting db-ssis MCP on http://0.0.0.0:5190")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add db-ssis --transport http http://localhost:5190/mcp")
    print()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5190)
