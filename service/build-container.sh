#!/usr/bin/env bash
# build-container.sh — build the dotnet-mcp-build container image
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Building dotnet-mcp-build image..."
docker build -f "$SCRIPT_DIR/Dockerfile" -t dotnet-mcp-build "$SCRIPT_DIR"
echo "Done. Run with: $SCRIPT_DIR/start-container.sh"
