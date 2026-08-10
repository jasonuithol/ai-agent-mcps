#!/usr/bin/env bash
# clean.sh — undo setup.sh. Removes the container and image so a fresh
# clean → setup → start cycle returns the repo to bare state.
#
# The host packages/ directory is INTENTIONALLY left alone — it holds
# user-authored .dtsx packages and their logs. Delete it manually if
# you really want to wipe everything.
set -euo pipefail

name=db-mcp-ssis
if docker container inspect "$name" >/dev/null 2>&1; then
    echo "Removing container $name..."
    docker rm -f "$name" >/dev/null
fi

if docker image inspect "$name" >/dev/null 2>&1; then
    echo "Removing image $name..."
    docker rmi -f "$name" >/dev/null
fi

echo "Done. (packages/ left intact — delete it by hand if desired.)"
