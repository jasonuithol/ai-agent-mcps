#!/usr/bin/env bash
# setup.sh — one-time setup for mcp-dotnet: create persistent volumes
# and build the two container images.
# Idempotent: skips images and volumes that already exist. Use clean.sh to undo.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Persistent volumes ────────────────────────────────────────────────────────
# mcp-dotnet-sdks  : holds dotnet SDKs installed at runtime (so install_sdk
#                    survives container restart and image rebuild).
# mcp-dotnet-nuget : holds NuGet.Config + global package cache (so add_feed
#                    survives, and `dotnet restore` doesn't re-download
#                    everything after a container rebuild).
for vol in mcp-dotnet-sdks mcp-dotnet-nuget; do
    if docker volume inspect "$vol" >/dev/null 2>&1; then
        echo "Volume $vol already exists — skipping."
    else
        echo "Creating volume $vol..."
        docker volume create "$vol" >/dev/null
    fi
done

# ── Container images ──────────────────────────────────────────────────────────

declare -A SUBDIR=( [dotnet-mcp-build]=service [dotnet-mcp-knowledge]=knowledge )

for image in dotnet-mcp-build dotnet-mcp-knowledge; do
    if docker image inspect "$image" >/dev/null 2>&1; then
        echo "Image $image already built — skipping."
    else
        echo "Building image $image..."
        "$SCRIPT_DIR/${SUBDIR[$image]}/build-container.sh"
    fi
done

echo "Done."
