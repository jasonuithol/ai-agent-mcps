#!/usr/bin/env bash
# start.sh — bring up mcp-steam as a backgrounded host process.
# Idempotent: setup.sh skips if venv exists. Re-running start.sh while
# the service is already up will fail to bind port 5174 — use ./stop.sh
# first if you want a clean restart.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure venv is provisioned. Cheap if already set up.
"$SCRIPT_DIR/setup.sh"

echo "Starting mcp-steam (host process, port 5174)..."
"$SCRIPT_DIR/start-foreground.sh" >"$SCRIPT_DIR/steam.log" 2>&1 &
echo "  background PID $! (logs: $SCRIPT_DIR/steam.log)"

echo "Done."
