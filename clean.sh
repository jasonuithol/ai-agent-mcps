#!/usr/bin/env bash
# clean.sh — undo setup.sh. Removes the .venv/ directory entirely so a
# fresh setup.sh run is guaranteed to start from bare state.
#
# Use this to validate that setup.sh works for someone with nothing
# installed yet (clean → setup → smoke test).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ -d "$VENV" ]; then
    echo "Removing $VENV..."
    rm -rf "$VENV"
    echo "Done."
else
    echo "Nothing to clean ($VENV does not exist)."
fi
