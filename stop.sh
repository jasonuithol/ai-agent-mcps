#!/usr/bin/env bash
# stop.sh — shut down the mcp-ssis container.
#
# Default: SIGTERM via docker stop. --kill: SIGKILL via docker kill.
# Container is left in place either way so next start.sh can revive it.
# For full removal (image, container), use ./clean.sh. Host packages/
# directory is never touched.
set -euo pipefail

FORCE=false
if [ "${1:-}" = "--kill" ]; then
    FORCE=true
fi

name=db-mcp-ssis
echo "Stopping $name..."
if [ "$FORCE" = true ]; then
    docker kill "$name" 2>/dev/null && echo "  killed" || echo "  not running"
else
    docker stop "$name" 2>/dev/null && echo "  stopped" || echo "  not running"
fi

echo "Done."
