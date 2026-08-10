#!/usr/bin/env bash
set -euo pipefail

CONTAINER_NAME="valheim-mcp-knowledge"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KNOWLEDGE_DIR="$SCRIPT_DIR/knowledge"

mkdir -p "$KNOWLEDGE_DIR"

# Embedding model is baked into the image — no model mount needed.
# Always recreate the container so mount/env changes take effect. ChromaDB
# state lives in the $KNOWLEDGE_DIR volume, so the seeded index survives.
docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
docker run -d \
    --name "$CONTAINER_NAME" \
    --network host \
    --device nvidia.com/gpu=all \
    -e ONNX_PROVIDERS=CUDAExecutionProvider \
    -e PORT=5184 \
    -v "$KNOWLEDGE_DIR:/opt/knowledge" \
    -v "$HOME/Projects:/opt/projects:ro" \
    valheim-mcp-knowledge
