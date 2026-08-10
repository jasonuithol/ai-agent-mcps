#!/usr/bin/env bash
# start-foreground.sh — run the mcp-steam server directly on the host
# in the foreground (blocks until killed). For backgrounded use, see
# start.sh which wraps this.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ ! -f "$VENV/bin/activate" ]; then
    echo "Error: virtualenv not found at $VENV"
    echo "  Run: $SCRIPT_DIR/setup.sh"
    exit 1
fi

source "$VENV/bin/activate"
exec python "$SCRIPT_DIR/mcp-service.py"
