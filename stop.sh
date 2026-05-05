#!/usr/bin/env bash
# stop.sh — shut down both db-mcp containers.
#
# Default: SIGTERM with grace period (docker stop) — gives the engines
# time to checkpoint and shut down cleanly.
# --kill: SIGKILL immediately (docker kill). Containers are left in place
#         either way so the next start.sh can revive them. For full removal
#         (including data volumes), use ./clean.sh.
set -euo pipefail

FORCE=false
if [ "${1:-}" = "--kill" ]; then
    FORCE=true
fi

for name in db-mcp-postgres db-mcp-mssql; do
    echo "Stopping $name..."
    if [ "$FORCE" = true ]; then
        docker kill "$name" 2>/dev/null && echo "  killed" || echo "  not running"
    else
        docker stop "$name" 2>/dev/null && echo "  stopped" || echo "  not running"
    fi
done

echo "Done."
