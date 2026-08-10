#!/usr/bin/env python3
"""
mcp-service.py — dotnet-build

Runs inside a Docker container. Exposes generic .NET build / test /
analyze / package / NuGet / SDK-management tools to Claude Code.

Register with Claude Code:
    claude mcp add dotnet --transport http http://localhost:5202/mcp
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from fastmcp import FastMCP
from mcp_knowledge_base import KnowledgeReporter

# ── Config ────────────────────────────────────────────────────────────────────

PROJECTS_DIR = Path(os.environ.get("PROJECTS_DIR", "/opt/projects"))
DOTNET_ROOT  = Path(os.environ.get("DOTNET_ROOT",  "/opt/dotnet"))
NUGET_ROOT   = Path("/opt/nuget")
NUGET_CONFIG = NUGET_ROOT / "NuGet.Config"

# ── Knowledge reporter ────────────────────────────────────────────────────────

_reporter = KnowledgeReporter(service="dotnet-build")
_report = _reporter.report


# ── Helpers ───────────────────────────────────────────────────────────────────

def _project_dir(project: str) -> Path:
    if not project or "/" in project or ".." in project:
        raise ValueError(f"Invalid project name: {project!r}")
    d = PROJECTS_DIR / project
    if not d.is_dir():
        raise FileNotFoundError(f"Project directory not found: {d}")
    return d


def _run(
    cmd: list[str],
    cwd: str | None = None,
    env: dict | None = None,
    timeout: float | None = None,
) -> tuple[bool, str]:
    """Run synchronously, capture combined stdout+stderr."""
    full_env = os.environ.copy()
    if env:
        full_env.update(env)
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            env=full_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        partial = e.output or ""
        return False, f"{partial}\n--- TIMEOUT after {timeout}s ---"
    return proc.returncode == 0, proc.stdout


async def _run_async(
    cmd: list[str],
    cwd: str | None = None,
    env: dict | None = None,
    timeout: float | None = None,
) -> tuple[bool, str]:
    return await asyncio.to_thread(_run, cmd, cwd, env, timeout)


def _dotnet_args_for_project(project: str) -> tuple[Path, list[str]]:
    """
    Resolve the project path. Returns (cwd, extra_args).
    `dotnet` auto-discovers .sln / .csproj in the cwd, so we just return
    the project dir and let the CLI figure it out. If multiple solutions
    are present, the user must pick — surfacing dotnet's own error is
    clearer than us guessing.
    """
    pd = _project_dir(project)
    return pd, []


def _verdict(success: bool, action: str) -> str:
    return f"{action} {'SUCCEEDED ✓' if success else 'FAILED ✗'}"


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="dotnet",
    instructions=(
        "Generic .NET build / test / package / analyze tools. All tools return "
        "full output so failures can be diagnosed without reading a log file. "
        "Projects live under /opt/projects (mounted from ~/Projects on the host). "
        "Pass the project folder name (no path separators) to most tools. "
        "SDK and NuGet state is persisted across container restarts via named "
        "volumes — install_sdk / add_feed are durable."
    ),
)


# ── build / restore / clean ───────────────────────────────────────────────────

@mcp.tool()
async def build(project: str, configuration: str = "Release", target: str | None = None) -> str:
    """
    Build a .NET project or solution with `dotnet build`.

    Auto-discovers .sln / .csproj in the project directory. Respects
    global.json SDK pinning (use ensure_sdk to install a missing pinned SDK).

    Args:
        project: Project folder name under ~/Projects (no path separators).
        configuration: 'Release' (default) or 'Debug'.
        target: Optional .sln / .csproj path relative to the project dir,
                if you need to disambiguate when multiple are present.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "build", "-c", configuration]
    if target:
        cmd.append(target)
    success, log = await _run_async(cmd, cwd=str(pd), timeout=600)
    result = f"{_verdict(success, 'BUILD')}\n\n{log}"
    _report("build", {"project": project, "configuration": configuration, "target": target}, result, success)
    return result


@mcp.tool()
async def restore(project: str, target: str | None = None) -> str:
    """
    Restore NuGet packages with `dotnet restore`.

    Respects per-project nuget.config files and the global container
    feeds (see list_feeds).

    Args:
        project: Project folder name under ~/Projects.
        target: Optional .sln / .csproj path relative to the project dir.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "restore"]
    if target:
        cmd.append(target)
    success, log = await _run_async(cmd, cwd=str(pd), timeout=600)
    result = f"{_verdict(success, 'RESTORE')}\n\n{log}"
    _report("restore", {"project": project, "target": target}, result, success)
    return result


@mcp.tool()
async def clean(project: str, configuration: str = "Release") -> str:
    """
    Clean build outputs with `dotnet clean`.

    Args:
        project: Project folder name under ~/Projects.
        configuration: 'Release' (default) or 'Debug'.
    """
    pd, _ = _dotnet_args_for_project(project)
    success, log = await _run_async(["dotnet", "clean", "-c", configuration], cwd=str(pd), timeout=120)
    result = f"{_verdict(success, 'CLEAN')}\n\n{log}"
    _report("clean", {"project": project, "configuration": configuration}, result, success)
    return result


# ── test ──────────────────────────────────────────────────────────────────────

@mcp.tool()
async def run_tests(
    project: str,
    configuration: str = "Release",
    filter: str | None = None,
    target: str | None = None,
) -> str:
    """
    Run tests with `dotnet test`. Picks up xUnit / NUnit / MSTest
    automatically based on the project's test framework reference.

    Args:
        project: Project folder name under ~/Projects.
        configuration: 'Release' (default) or 'Debug'.
        filter: Optional --filter expression (e.g. 'Category=Unit',
                'FullyQualifiedName~MyNamespace.MyClass').
        target: Optional .sln / .csproj path relative to the project dir.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "test", "-c", configuration, "--logger", "console;verbosity=normal"]
    if filter:
        cmd += ["--filter", filter]
    if target:
        cmd.append(target)
    success, log = await _run_async(cmd, cwd=str(pd), timeout=900)
    result = f"{_verdict(success, 'TESTS')}\n\n{log}"
    _report("run_tests", {"project": project, "configuration": configuration, "filter": filter}, result, success)
    return result


# ── format / analyze ──────────────────────────────────────────────────────────

@mcp.tool()
async def format(project: str, write: bool = False) -> str:
    """
    Run `dotnet format` over the project.

    Args:
        project: Project folder name under ~/Projects.
        write: If False (default), only verify formatting — fail if changes
               would be made (--verify-no-changes). If True, apply the
               formatting changes in-place.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "format"]
    if not write:
        cmd.append("--verify-no-changes")
    success, log = await _run_async(cmd, cwd=str(pd), timeout=300)
    action = "FORMAT (write)" if write else "FORMAT (verify)"
    result = f"{_verdict(success, action)}\n\n{log}"
    _report("format", {"project": project, "write": write}, result, success)
    return result


@mcp.tool()
async def analyze(project: str, configuration: str = "Release") -> str:
    """
    Run Roslyn analyzers via `dotnet build -warnaserror`.

    Treats every warning as an error so analyzer output is surfaced
    cleanly. Respects the project's .editorconfig / analyzer config.

    Args:
        project: Project folder name under ~/Projects.
        configuration: 'Release' (default) or 'Debug'.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "build", "-c", configuration, "-warnaserror"]
    success, log = await _run_async(cmd, cwd=str(pd), timeout=600)
    result = f"{_verdict(success, 'ANALYZE')}\n\n{log}"
    _report("analyze", {"project": project, "configuration": configuration}, result, success)
    return result


# ── pack / publish ────────────────────────────────────────────────────────────

@mcp.tool()
async def pack(project: str, configuration: str = "Release", output: str | None = None) -> str:
    """
    Produce a NuGet package with `dotnet pack`.

    Use this for distributing libraries or dotnet tools — NOT to be confused
    with Thunderstore packaging (which lives in mcp-valheim/mod).

    Args:
        project: Project folder name under ~/Projects.
        configuration: 'Release' (default) or 'Debug'.
        output: Optional output dir relative to the project root
                (defaults to bin/<configuration>/).
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "pack", "-c", configuration]
    if output:
        cmd += ["-o", output]
    success, log = await _run_async(cmd, cwd=str(pd), timeout=600)
    result = f"{_verdict(success, 'PACK')}\n\n{log}"
    _report("pack", {"project": project, "configuration": configuration, "output": output}, result, success)
    return result


@mcp.tool()
async def publish(
    project: str,
    configuration: str = "Release",
    runtime: str | None = None,
    self_contained: bool = False,
    output: str | None = None,
) -> str:
    """
    Publish a .NET app with `dotnet publish` (NOT Thunderstore — that's
    in mcp-valheim/mod).

    Args:
        project: Project folder name under ~/Projects.
        configuration: 'Release' (default) or 'Debug'.
        runtime: Optional RID (e.g. 'linux-x64', 'win-x64'). Required if
                 self_contained=True.
        self_contained: If True, bundle the .NET runtime with the output.
        output: Optional output dir relative to the project root.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "publish", "-c", configuration]
    if runtime:
        cmd += ["-r", runtime]
    cmd.append(f"--self-contained={'true' if self_contained else 'false'}")
    if output:
        cmd += ["-o", output]
    success, log = await _run_async(cmd, cwd=str(pd), timeout=600)
    result = f"{_verdict(success, 'PUBLISH')}\n\n{log}"
    _report(
        "publish",
        {"project": project, "configuration": configuration, "runtime": runtime, "self_contained": self_contained, "output": output},
        result, success,
    )
    return result


# ── NuGet package management ──────────────────────────────────────────────────

@mcp.tool()
async def add_package(project: str, package: str, version: str | None = None, target: str | None = None) -> str:
    """
    Add a NuGet package reference with `dotnet add package`.

    Args:
        project: Project folder name under ~/Projects.
        package: Package id (e.g. 'Newtonsoft.Json').
        version: Optional version. Omit for latest.
        target: Optional .csproj relative path if multiple projects are
                present in the directory.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "add"]
    if target:
        cmd.append(target)
    cmd += ["package", package]
    if version:
        cmd += ["--version", version]
    success, log = await _run_async(cmd, cwd=str(pd), timeout=300)
    result = f"{_verdict(success, 'ADD_PACKAGE')}\n\n{log}"
    _report("add_package", {"project": project, "package": package, "version": version}, result, success)
    return result


@mcp.tool()
async def remove_package(project: str, package: str, target: str | None = None) -> str:
    """
    Remove a NuGet package reference with `dotnet remove package`.

    Args:
        project: Project folder name under ~/Projects.
        package: Package id to remove.
        target: Optional .csproj relative path.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "remove"]
    if target:
        cmd.append(target)
    cmd += ["package", package]
    success, log = await _run_async(cmd, cwd=str(pd), timeout=120)
    result = f"{_verdict(success, 'REMOVE_PACKAGE')}\n\n{log}"
    _report("remove_package", {"project": project, "package": package}, result, success)
    return result


@mcp.tool()
async def list_packages(project: str, outdated: bool = False, target: str | None = None) -> str:
    """
    List NuGet package references via `dotnet list package`.

    Args:
        project: Project folder name under ~/Projects.
        outdated: If True, show packages with newer versions available.
        target: Optional .csproj / .sln relative path.
    """
    pd, _ = _dotnet_args_for_project(project)
    cmd = ["dotnet", "list"]
    if target:
        cmd.append(target)
    cmd += ["package"]
    if outdated:
        cmd.append("--outdated")
    success, log = await _run_async(cmd, cwd=str(pd), timeout=300)
    result = f"{_verdict(success, 'LIST_PACKAGES')}\n\n{log}"
    _report("list_packages", {"project": project, "outdated": outdated}, result, success)
    return result


# ── NuGet feed management ─────────────────────────────────────────────────────
#
# Operates on the container-global /opt/nuget/NuGet.Config (persisted in
# the mcp-dotnet-nuget volume). Per-project nuget.config files in the user's
# source tree are picked up automatically by dotnet restore.

def _nuget_cmd(*args: str) -> list[str]:
    """Build a `dotnet nuget` command targeting the global config."""
    return ["dotnet", "nuget", *args, "--configfile", str(NUGET_CONFIG)]


@mcp.tool()
async def list_feeds() -> str:
    """
    List configured NuGet feeds in the container-global config.
    """
    success, log = await _run_async(_nuget_cmd("list", "source"), timeout=30)
    result = f"{_verdict(success, 'LIST_FEEDS')}\n\n{log}"
    _report("list_feeds", {}, result, success)
    return result


@mcp.tool()
async def add_feed(name: str, url: str, username: str | None = None, password_env: str | None = None) -> str:
    """
    Add a NuGet feed to the container-global config.

    Args:
        name: Short feed name (e.g. 'github').
        url:  Feed v3 index URL.
        username: Optional username for authenticated feeds.
        password_env: Optional environment variable name holding the password
                      / token. The value (not the name) is stored in the
                      config via --store-password-in-clear-text — keep it
                      short-lived if sensitive.
    """
    cmd = _nuget_cmd("add", "source", url, "--name", name)
    if username:
        cmd += ["--username", username]
    if password_env:
        pwd = os.environ.get(password_env, "")
        if not pwd:
            return f"ADD_FEED FAILED ✗\n\nEnvironment variable {password_env!r} is empty or unset."
        cmd += ["--password", pwd, "--store-password-in-clear-text"]
    success, log = await _run_async(cmd, timeout=30)
    result = f"{_verdict(success, 'ADD_FEED')}\n\n{log}"
    _report("add_feed", {"name": name, "url": url, "username": username}, result, success)
    return result


@mcp.tool()
async def remove_feed(name: str) -> str:
    """
    Remove a NuGet feed from the container-global config.

    Args:
        name: Feed name (as reported by list_feeds).
    """
    success, log = await _run_async(_nuget_cmd("remove", "source", name), timeout=30)
    result = f"{_verdict(success, 'REMOVE_FEED')}\n\n{log}"
    _report("remove_feed", {"name": name}, result, success)
    return result


# ── SDK management ────────────────────────────────────────────────────────────

@mcp.tool()
async def list_sdks() -> str:
    """
    List installed .NET SDKs (`dotnet --list-sdks`).
    """
    success, log = await _run_async(["dotnet", "--list-sdks"], timeout=30)
    result = f"{_verdict(success, 'LIST_SDKS')}\n\n{log}"
    _report("list_sdks", {}, result, success)
    return result


@mcp.tool()
async def install_sdk(version: str | None = None, channel: str | None = None) -> str:
    """
    Install an additional .NET SDK into the persistent /opt/dotnet volume
    via Microsoft's dotnet-install.sh. Survives container restart.

    Pass exactly one of `version` (e.g. '8.0.404') or `channel`
    (e.g. '8.0', '9.0', 'LTS', 'STS').

    Args:
        version: Exact SDK version, e.g. '8.0.404'.
        channel: Channel name, e.g. '8.0', '9.0', 'LTS', 'STS'.
    """
    if bool(version) == bool(channel):
        return "INSTALL_SDK FAILED ✗\n\nPass exactly one of `version` or `channel`."
    cmd = ["dotnet-install.sh", "--install-dir", str(DOTNET_ROOT), "--no-path"]
    if version:
        cmd += ["--version", version]
    else:
        cmd += ["--channel", channel]
    success, log = await _run_async(cmd, timeout=900)
    result = f"{_verdict(success, 'INSTALL_SDK')}\n\n{log}"
    _report("install_sdk", {"version": version, "channel": channel}, result, success)
    return result


@mcp.tool()
async def remove_sdk(version: str) -> str:
    """
    Remove an installed .NET SDK from /opt/dotnet.

    Args:
        version: Exact SDK version directory name under sdk/, e.g. '8.0.404'.
                 Use list_sdks to see what's installed.
    """
    sdk_dir = DOTNET_ROOT / "sdk" / version
    if not sdk_dir.is_dir():
        result = f"REMOVE_SDK FAILED ✗\n\nNo SDK directory at {sdk_dir}. Check list_sdks output."
        _report("remove_sdk", {"version": version}, result, False)
        return result
    try:
        await asyncio.to_thread(shutil.rmtree, sdk_dir)
        result = f"REMOVE_SDK SUCCEEDED ✓\n\nRemoved {sdk_dir}."
        _report("remove_sdk", {"version": version}, result, True)
        return result
    except Exception as e:
        result = f"REMOVE_SDK FAILED ✗\n\n{e}"
        _report("remove_sdk", {"version": version}, result, False)
        return result


@mcp.tool()
async def ensure_sdk(project: str) -> str:
    """
    Read the project's global.json and install the pinned SDK if missing.

    No-op if the project has no global.json or if the pinned SDK is
    already installed.

    Args:
        project: Project folder name under ~/Projects.
    """
    pd = _project_dir(project)
    gjson = pd / "global.json"
    if not gjson.exists():
        result = f"ENSURE_SDK NOOP ✓\n\nNo global.json in {pd} — nothing to ensure."
        _report("ensure_sdk", {"project": project}, result, True)
        return result

    try:
        data = json.loads(gjson.read_text())
        pinned = data.get("sdk", {}).get("version")
    except Exception as e:
        result = f"ENSURE_SDK FAILED ✗\n\nCould not parse {gjson}: {e}"
        _report("ensure_sdk", {"project": project}, result, False)
        return result

    if not pinned:
        result = f"ENSURE_SDK NOOP ✓\n\n{gjson} has no sdk.version pin."
        _report("ensure_sdk", {"project": project}, result, True)
        return result

    # Check installed SDKs.
    ok, listing = await _run_async(["dotnet", "--list-sdks"], timeout=30)
    if ok and any(line.split(" ", 1)[0] == pinned for line in listing.splitlines() if line.strip()):
        result = f"ENSURE_SDK NOOP ✓\n\nSDK {pinned} already installed."
        _report("ensure_sdk", {"project": project, "version": pinned}, result, True)
        return result

    # Install it.
    cmd = ["dotnet-install.sh", "--install-dir", str(DOTNET_ROOT), "--no-path", "--version", pinned]
    success, log = await _run_async(cmd, timeout=900)
    result = f"{_verdict(success, 'ENSURE_SDK')}\n\nInstalled SDK {pinned}.\n\n{log}"
    _report("ensure_sdk", {"project": project, "version": pinned}, result, success)
    return result


# ── decompile ─────────────────────────────────────────────────────────────────

@mcp.tool()
async def decompile_dll(container_path: str, type_name: str | None = None) -> str:
    """
    Decompile a DLL with ilspycmd and return the source output.

    Args:
        container_path: Path to the DLL as seen from inside this container.
                        Paths under /opt/projects/<project>/ map to the
                        user's ~/Projects/<project>/ tree.
        type_name:      Optional type name to decompile a single class,
                        e.g. 'Player'. Omit to decompile the entire DLL.
    """
    p = Path(container_path)
    if not p.is_file():
        result = f"DECOMPILE FAILED ✗\n\nNo such file: {container_path}"
        _report("decompile_dll", {"container_path": container_path, "type_name": type_name}, result, False)
        return result

    cmd = ["ilspycmd"]
    if type_name:
        cmd += ["-t", type_name]
    cmd.append(str(p))

    success, log = await _run_async(cmd, timeout=300)
    result = f"{_verdict(success, 'DECOMPILE')}\n\n{log}"
    _report("decompile_dll", {"container_path": container_path, "type_name": type_name}, result, success)
    return result


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"DOTNET_ROOT = {DOTNET_ROOT}")
    print(f"NUGET_CONFIG = {NUGET_CONFIG}")
    print(f"PROJECTS_DIR = {PROJECTS_DIR}")
    print("Starting dotnet MCP on http://0.0.0.0:5202")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add dotnet --transport http http://localhost:5202/mcp")
    print()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5202)
