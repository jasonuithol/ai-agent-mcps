#!/usr/bin/env bash
# build-container.sh — build the db MCP mssql container image
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Building db-mcp-mssql image..."
docker build -f "$SCRIPT_DIR/Dockerfile" -t db-mcp-mssql "$SCRIPT_DIR"
echo "Done. Run with: $SCRIPT_DIR/start-container.sh"
