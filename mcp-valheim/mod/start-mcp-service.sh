#!/usr/bin/env bash
# start-mcp-service.sh — launch the Valheim MCP server on the host
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

# Create venv on first run
if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV"
fi

# Install/upgrade the MCP SDK if missing
if ! "$VENV/bin/python" -c "import mcp, psutil" 2>/dev/null; then
    echo "Installing dependencies..."
    "$VENV/bin/pip" install --quiet "mcp>=2,<3" psutil
fi

exec "$VENV/bin/python" "$SCRIPT_DIR/mcp-service.py"
