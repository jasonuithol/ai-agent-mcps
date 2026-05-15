#!/usr/bin/env bash
# clean.sh — undo setup.sh. Removes both containers, both images, AND the
# named volumes so a fresh clean → setup → start cycle returns the repo
# to a verifiable bare state.
#
# Does NOT touch host-mounted state (knowledge/knowledge/ ChromaDB index)
# — that's data, not setup. Delete it manually for a totally fresh KB.
#
# WARNING: removing mcp-dotnet-sdks wipes any SDKs installed via install_sdk.
# Removing mcp-dotnet-nuget wipes the NuGet package cache + feed config.
set -euo pipefail

# Containers first (must be removed before their image can be deleted).
for name in dotnet-mcp-build dotnet-mcp-knowledge; do
    if docker container inspect "$name" >/dev/null 2>&1; then
        echo "Removing container $name..."
        docker rm -f "$name" >/dev/null
    fi
done

for image in dotnet-mcp-build dotnet-mcp-knowledge; do
    if docker image inspect "$image" >/dev/null 2>&1; then
        echo "Removing image $image..."
        docker rmi -f "$image" >/dev/null
    fi
done

for vol in mcp-dotnet-sdks mcp-dotnet-nuget; do
    if docker volume inspect "$vol" >/dev/null 2>&1; then
        echo "Removing volume $vol..."
        docker volume rm "$vol" >/dev/null
    fi
done

echo "Done."
