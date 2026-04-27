#!/usr/bin/env bash
# stop.sh — stop the mcp-steam host process by killing whatever holds
# port 5177.
#
# Default: SIGTERM. --kill: SIGKILL.
set -euo pipefail

FORCE=false
[ "${1:-}" = "--kill" ] && FORCE=true

echo "Stopping mcp-steam (port 5177)..."
if $FORCE; then
    fuser -k -KILL 5177/tcp 2>/dev/null && echo "  killed" || echo "  not running"
else
    fuser -k -TERM 5177/tcp 2>/dev/null && echo "  stopped" || echo "  not running"
fi

echo "Done."
