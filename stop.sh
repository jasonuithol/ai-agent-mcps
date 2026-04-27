#!/usr/bin/env bash
# stop.sh — stop the mcp-steam host process by killing whatever holds
# port 5174.
#
# Default: SIGTERM. --kill: SIGKILL.
set -euo pipefail

FORCE=false
[ "${1:-}" = "--kill" ] && FORCE=true

echo "Stopping mcp-steam (port 5174)..."
if $FORCE; then
    fuser -k -KILL 5174/tcp 2>/dev/null && echo "  killed" || echo "  not running"
else
    fuser -k -TERM 5174/tcp 2>/dev/null && echo "  stopped" || echo "  not running"
fi

echo "Done."
