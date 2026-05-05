#!/usr/bin/env bash
# setup.sh — one-time setup for mcp-db: build both engine container images.
# Idempotent: skips images that are already built. Use clean.sh to undo.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# image_name → subdir holding its build-container.sh
declare -A SUBDIR=( [db-mcp-postgres]=postgres [db-mcp-mssql]=mssql )

for image in db-mcp-postgres db-mcp-mssql; do
    if docker image inspect "$image" >/dev/null 2>&1; then
        echo "Image $image already built — skipping."
    else
        echo "Building image $image..."
        "$SCRIPT_DIR/${SUBDIR[$image]}/build-container.sh"
    fi
done

echo "Done."
