#!/usr/bin/env bash
# ingest-chessprogramming.sh — host-side wiki crawl.
#
# Bootstraps a venv on first run (requests + markdownify), then invokes
# the Python ingester. All args pass through, e.g.:
#   ./ingest-chessprogramming.sh --limit 20        # smoke test
#   ./ingest-chessprogramming.sh                   # full crawl (~30-60 min)
#   ./ingest-chessprogramming.sh --refresh         # re-fetch cached
#
# After this completes, run ./seed.sh to index the cached docs into chroma.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv-ingest"

if [ ! -d "$VENV" ]; then
    echo "Creating ingest venv at $VENV..."
    python3 -m venv "$VENV"
    "$VENV/bin/pip" install --quiet --upgrade pip
    "$VENV/bin/pip" install --quiet requests markdownify
fi

exec "$VENV/bin/python" "$SCRIPT_DIR/ingest-chessprogramming.py" "$@"
