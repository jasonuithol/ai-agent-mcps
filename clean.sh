#!/usr/bin/env bash
# clean.sh — undo setup.sh. Removes both containers, both images, AND
# both data volumes so a fresh clean → setup → start cycle returns the
# repo to a verifiable bare state.
#
# WARNING: this destroys all databases stored in the data volumes.
# If you only want to stop the services, use ./stop.sh.
set -euo pipefail

# Containers first (must be removed before their image can be deleted).
for name in db-mcp-postgres db-mcp-mssql; do
    if docker container inspect "$name" >/dev/null 2>&1; then
        echo "Removing container $name..."
        docker rm -f "$name" >/dev/null
    fi
done

for image in db-mcp-postgres db-mcp-mssql; do
    if docker image inspect "$image" >/dev/null 2>&1; then
        echo "Removing image $image..."
        docker rmi -f "$image" >/dev/null
    fi
done

for volume in db-mcp-postgres-data db-mcp-mssql-data; do
    if docker volume inspect "$volume" >/dev/null 2>&1; then
        echo "Removing volume $volume (databases will be destroyed)..."
        docker volume rm "$volume" >/dev/null
    fi
done

echo "Done."
