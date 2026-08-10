#!/usr/bin/env bash
# build-container.sh — build the db MCP postgres container image
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Building db-mcp-postgres image..."
docker build -f "$SCRIPT_DIR/Dockerfile" -t db-mcp-postgres "$SCRIPT_DIR"
echo "Done. Run with: $SCRIPT_DIR/start-container.sh"
