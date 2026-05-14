#!/usr/bin/env bash
# setup.sh — one-time setup for mcp-ssis: build the container image.
# Idempotent: skips the image if already built. Use clean.sh to undo.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if docker image inspect db-mcp-ssis >/dev/null 2>&1; then
    echo "Image db-mcp-ssis already built — skipping."
else
    echo "Building image db-mcp-ssis..."
    "$SCRIPT_DIR/ssis/build-container.sh"
fi

echo "Done."
