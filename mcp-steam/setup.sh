#!/usr/bin/env bash
# setup.sh — one-time setup for mcp-steam (host-runner, no container).
# Idempotent: safe to re-run. Creates a venv at .venv/ and installs deps.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV" ]; then
    echo "Creating virtualenv at $VENV..."
    python3 -m venv "$VENV"
fi

echo "Installing/upgrading dependencies..."
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$SCRIPT_DIR/requirements.txt"

echo "Done. Run with: $SCRIPT_DIR/start-mcp-service.sh"
