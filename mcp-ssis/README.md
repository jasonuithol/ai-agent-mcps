# mcp-ssis

MCP service for SSIS-on-Linux: validate, run, and benchmark `.dtsx`
packages via `dtexec`. Designed as a peer to
[`mcp-db`](../mcp-db) — the SSIS container runs in its own image, and
state-reset SQL between benchmark iterations is issued against the
`mcp-db` mssql container over `host.containers.internal:1433`.

This is a **dev / benchmark rig**, intended for developing a replacement
for SSIS. Microsoft does not support SSIS on Linux in containers; this
image works in practice but should not be pointed at anything you care
about.

| Subdir | Container | MCP port | Engine port | Role |
|--------|-----------|----------|-------------|------|
| `ssis/` | `db-mcp-ssis` | 5190 | — | SSIS runtime (`dtexec`) wrapped by MCP |

`.dtsx` and `.dtsConfig` files live in the host directory
`packages/`, which is bind-mounted at `/packages` inside the container.
Per-run logs land under `packages/logs/`.

## Tools

- `list_packages()` — enumerate `.dtsx` under `/packages` (recursive),
  with size + mtime.
- `validate_package(path)` — `dtexec /Validate /Reporting V`. Returns
  the SSIS engine's verdict on whether the package is well-formed and
  runnable on this Linux-SSIS host. **Use this first when a package is
  suspected of being invalid** — it's faster and more diagnostic than a
  failed run.
- `run_package(path, params?, config?)` — `dtexec /File`. `params` is a
  dict where keys are full SSIS property paths (e.g.
  `\Package.Variables[FilePath].Value`) and values are stringified into
  `/Set` arguments. `config` is an optional `/ConfigFile` path under
  `/packages`.
- `benchmark_package(path, runs=5, warmup=1, reset_sql?, reset_database?, params?, config?)`
  — run the package `runs` times under GNU `time -v` and report
  min / p50 / max / mean / stdev for wall, CPU, and peak RSS. The first
  `warmup` runs are discarded from stats. If `reset_sql` is provided, it
  is executed against the peer mssql container with autocommit before
  *every* iteration (warmups included).
- `connection_info()` — diagnostic surface: packages dir, logs dir,
  dtexec path, peer mssql DSN.

## Usage

```bash
./setup.sh                # one-time, idempotent (builds the image)
./start.sh                # bring up the container
./stop.sh                 # shut it down (packages dir preserved)
./clean.sh                # remove container + image (packages dir preserved)
./info.sh                 # print MCP URL + paths
```

The packages directory (`./packages` by default) is **never** touched by
`clean.sh` — it holds user-authored work. Delete it by hand if you
really want a bare slate.

Register the MCP endpoint:

```bash
claude mcp add db-ssis --transport http http://localhost:5190/mcp
```

## Benchmark methodology

Comparing this rig's `dtexec` against a replacement engine is only
meaningful if both are measured on the same axes. Things this harness
controls or surfaces:

- **Warmup discard.** First `warmup` iterations excluded from stats.
  Default 1. JIT / cold-cache effects are real.
- **Cold-cache toggle.** `reset_sql` can be
  `DBCC DROPCLEANBUFFERS; CHECKPOINT;` to force cold-cache reads each
  iteration (requires sysadmin — the default `sa` login has it).
- **State reset.** `reset_sql` can also `TRUNCATE` + reload from a flat
  file or backup, so destination tables start each iteration in the
  same state.
- **Resource accounting.** Every run captures wall time, user CPU,
  system CPU, and peak RSS via GNU `time`. dtexec's .NET startup tax is
  visible in CPU vs. wall divergence on tiny packages.

Things this harness does **not** control automatically — surface them
in your test setup if they matter:

- **Buffer settings.** SSIS data-flow throughput is dominated by
  `DefaultBufferMaxRows` and `DefaultBufferSize`. Override per-package
  via `params` (the property paths are
  `\Package.Properties[DefaultBufferMaxRows]` and
  `\Package.Properties[DefaultBufferSize]`) and record what you used.
- **Parallelism.** `\Package.Properties[MaxConcurrentExecutables]` for
  control flow; `EngineThreads` on each data-flow task. Match these
  against the parallelism budget you give your replacement.
- **Inputs.** The package's own connection managers point at databases
  you control. Reset them via `reset_sql`.

## SSIS-on-Linux supported-component subset

The Linux SSIS runtime supports a narrow slice of the full SSIS feature
set. Packages that validate on Windows can still fail here. Known
limitations:

- No SSIS Catalog (SSISDB). Packages must come from the filesystem
  (which is what `/packages` is for).
- No third-party components, no CDC, no Scale Out, no Azure Feature
  Pack, no SAP BW connector, no Excel source/destination.
- OLE DB source/destination: SQL Server only.
- ADO.NET source/destination: SQLClient only.
- Windows-style paths in connection strings (`D:\home\x\file.csv`)
  are remapped to Linux paths (`/home/x/file.csv`).
- No Windows Authentication. SQL Auth only.
- Script tasks: standard .NET Framework APIs only.
- SSIS is not available for SQL Server 2025 (17.x) on Linux — this
  feature has a finite shelf life.

For the authoritative list, see
[Feature Support and Limitations for SSIS on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-ssis-known-issues?view=sql-server-ver16).

## Authoring `.dtsx` packages

No Linux-native authoring tool exists. Use either:

- Windows + SQL Server Data Tools (SSDT) or Visual Studio with the SSIS
  extension. Author there, copy the `.dtsx` into this repo's
  `packages/`.
- Hand-edit the XML for small / test cases.

## Configuration

`ssis/start-container.sh` reads:

- `MSSQL_HOST` — peer SQL Server hostname (default
  `host.containers.internal`).
- `MSSQL_PORT` — peer SQL Server port (default `1433`).
- `MSSQL_USER` — peer SQL Server login (default `sa`).
- `MSSQL_SA_PASSWORD` — peer SQL Server password (default
  `DevP@ssw0rd!42`, matching `mcp-db`'s default).
- `PACKAGES_DIR` — host directory to bind-mount as `/packages`
  (default `./packages` relative to the repo root).

`ssis/mcp-service.py` additionally reads:

- `DTEXEC` — path to dtexec (default `/opt/ssis/bin/dtexec`).
- `DEFAULT_RUNS`, `DEFAULT_WARMUP` — benchmark defaults.

## Safety notes

- The MCP service connects to the peer mssql as `sa` for `reset_sql`.
  Anything a caller can pass through `reset_sql` runs with full
  privileges on that instance.
- Package paths and `config` paths are validated against the
  `/packages` boundary (no traversal, no absolute paths).
- The `params` and `reset_sql` arguments to MCP tools are passed
  through to dtexec and SQL Server verbatim — no sanitisation. Local
  dev only.
