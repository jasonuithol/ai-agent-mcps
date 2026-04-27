#!/usr/bin/env python3
"""
mcp-service.py — mcp-steam

Runs directly on the host (NOT in a container). Exposes Steam process
control: status, start, stop, restart. Cross-domain — useful for any
Steam game, not specific to a single title.

No KnowledgeReporter — runtime status is ephemeral and not worth indexing.

Register with Claude Code:
    claude mcp add steam --transport http http://localhost:5177/mcp
"""

import subprocess

import psutil
from fastmcp import FastMCP


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="steam",
    instructions=(
        "Tools for controlling the Steam client process on the host. "
        "Cross-domain — applies to any Steam game. "
        "Game-specific lifecycle (e.g. Valheim server/client) lives in per-domain "
        "control MCPs (mcp-valheim/control etc.)."
    ),
)


# ── Steam ─────────────────────────────────────────────────────────────────────

@mcp.tool()
def steam_status() -> str:
    """Check whether Steam is currently running on the host."""
    procs = [p for p in psutil.process_iter(["name"])
             if p.info["name"] in ("steam", "steam.exe")]
    if procs:
        pids = ", ".join(str(p.pid) for p in procs)
        return f"Steam is running (PID {pids})."
    return "Steam is not running."


@mcp.tool()
def start_steam() -> str:
    """Start Steam on the host. Non-blocking — use steam_status() to confirm startup."""
    subprocess.Popen(["steam"], start_new_session=True)
    return "Steam launch initiated."


@mcp.tool()
def stop_steam() -> str:
    """Stop Steam gracefully by sending SIGTERM to all Steam processes."""
    procs = [p for p in psutil.process_iter(["name"])
             if p.info["name"] in ("steam", "steam.exe")]
    if not procs:
        return "Steam is not running."
    for p in procs:
        p.terminate()
    gone, alive = psutil.wait_procs(procs, timeout=10)
    if alive:
        return f"Steam did not exit cleanly; {len(alive)} process(es) still alive. Try restart_steam or kill manually."
    return f"Steam stopped ({len(gone)} process(es) terminated)."


@mcp.tool()
def restart_steam() -> str:
    """Stop Steam (if running) and start it again. Non-blocking — use steam_status() to confirm startup."""
    procs = [p for p in psutil.process_iter(["name"])
             if p.info["name"] in ("steam", "steam.exe")]
    if procs:
        for p in procs:
            p.terminate()
        psutil.wait_procs(procs, timeout=10)
    subprocess.Popen(["steam"], start_new_session=True)
    return "Steam restarted."


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Starting steam MCP on http://0.0.0.0:5177")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add steam --transport http http://localhost:5177/mcp")
    print()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5177)
