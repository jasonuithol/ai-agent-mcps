#!/usr/bin/env bash
# setup.sh — one-time setup for mcp-ue4ss: build the knowledge container image.
# Idempotent: skips images that are already built. Use clean.sh to undo.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for image in ue4ss-mcp-knowledge; do
    if docker image inspect "$image" >/dev/null 2>&1; then
        echo "Image $image already built — skipping."
    else
        echo "Building image $image..."
        "$SCRIPT_DIR/knowledge/build-container.sh"
    fi
done

echo "Done."
