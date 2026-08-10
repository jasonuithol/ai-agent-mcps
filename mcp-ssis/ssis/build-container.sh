#!/usr/bin/env bash
# build-container.sh — build the mcp-ssis container image
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Building db-mcp-ssis image..."
docker build -f "$SCRIPT_DIR/Dockerfile" -t db-mcp-ssis "$SCRIPT_DIR"
echo "Done. Run with: $SCRIPT_DIR/start-container.sh"
