#!/usr/bin/env bash
# build-container.sh — build the chess MCP engine container image
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Building chess-mcp-engine image..."
docker build -f "$SCRIPT_DIR/Dockerfile" -t chess-mcp-engine "$SCRIPT_DIR"
echo "Done. Run with: $SCRIPT_DIR/start-container.sh"
