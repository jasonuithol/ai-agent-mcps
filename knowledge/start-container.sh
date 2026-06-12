#!/usr/bin/env bash
set -euo pipefail

CONTAINER_NAME="ue4ss-mcp-knowledge"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KNOWLEDGE_DIR="$SCRIPT_DIR/knowledge"

mkdir -p "$KNOWLEDGE_DIR"

# Embedding model is baked into the image — no model mount needed.
# Revive a leftover container from a prior run if one exists; otherwise
# create a fresh one. ChromaDB state lives in the $KNOWLEDGE_DIR volume
# either way, so reviving preserves the seeded index without re-embedding.
#
# $HOME/Projects is mounted read-only so seed.sh can reference UE4SS docs
# wherever they're cloned (Advanced-SCUM-Modding/third_party/UE4SS, or a
# standalone clone) without baking absolute host paths into the image.
if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker run -d \
        --name "$CONTAINER_NAME" \
        --network host \
        --device nvidia.com/gpu=all \
        -e ONNX_PROVIDERS=CUDAExecutionProvider \
        -v "$KNOWLEDGE_DIR:/opt/knowledge" \
        -v "$HOME/Projects:/opt/projects:ro" \
        ue4ss-mcp-knowledge
fi
