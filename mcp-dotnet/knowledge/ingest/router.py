"""Ingest router for dotnet-knowledge.

Routes payloads from the sibling build service's KnowledgeReporter
calls. Successful tool runs are skipped; failures get indexed.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

from mcp_knowledge_base import IngestRouter

from .chunker import (
    chunk_analyze_error,
    chunk_build_error,
    chunk_test_failure,
    chunk_test_fix,
    upsert_chunks,
)

if TYPE_CHECKING:
    import chromadb

logger = logging.getLogger("dotnet-knowledge.router")

BUFFER_PATH = Path("/opt/knowledge/test_failure_buffer.json")
MAX_BUFFER_ENTRIES = 500

# `dotnet test --logger console;verbosity=normal` prints failing tests as:
#   Failed Namespace.Class.Method [...]
# Extract the qualified name so each failure becomes its own chunk.
_FAILED_TEST_RE = re.compile(r"^\s*(?:Failed|X)\s+([A-Za-z_][\w\.]*)", re.MULTILINE)
_PASSED_TEST_RE = re.compile(r"^\s*(?:Passed|✓)\s+([A-Za-z_][\w\.]*)", re.MULTILINE)


class DotnetIngestRouter(IngestRouter):
    """Routes incoming tool payloads to chunking/indexing logic."""

    def __init__(self, collection: "chromadb.Collection"):
        self.collection = collection
        self._pending_failures: dict[str, dict] = self._load_buffer()

    # ── buffer persistence ────────────────────────────────────────────

    def _load_buffer(self) -> dict[str, dict]:
        try:
            if BUFFER_PATH.exists():
                data = json.loads(BUFFER_PATH.read_text())
                if isinstance(data, dict):
                    return data
        except Exception:
            logger.warning("Failed to load test failure buffer, starting fresh")
        return {}

    def _save_buffer(self) -> None:
        try:
            BUFFER_PATH.parent.mkdir(parents=True, exist_ok=True)
            if len(self._pending_failures) > MAX_BUFFER_ENTRIES:
                items = sorted(
                    self._pending_failures.items(),
                    key=lambda kv: kv[1].get("timestamp", ""),
                    reverse=True,
                )[:MAX_BUFFER_ENTRIES]
                self._pending_failures = dict(items)
            BUFFER_PATH.write_text(json.dumps(self._pending_failures))
        except Exception:
            logger.warning("Failed to persist test failure buffer")

    def _index_chunks(self, chunks: list[dict]) -> None:
        if not chunks:
            return
        upsert_chunks(self.collection, chunks)
        logger.info("Indexed %d chunks", len(chunks))

    # ── route ──────────────────────────────────────────────────────────

    def route(self, payload: dict) -> dict:
        tool = payload.get("tool", "")
        success = payload.get("success", True)
        result = payload.get("result", "")
        args = payload.get("args", {})
        timestamp = payload.get("timestamp", "")
        project = args.get("project", "unknown")

        if tool == "build":
            if success:
                return {"action": "skipped_build_success", "chunks": 0}
            self._index_chunks([chunk_build_error(result, project)])
            return {"action": "indexed_build_error", "chunks": 1}

        if tool == "run_tests":
            return self._handle_run_tests(result, project, timestamp)

        if tool == "analyze":
            if success:
                return {"action": "skipped_analyze_clean", "chunks": 0}
            self._index_chunks([chunk_analyze_error(result, project)])
            return {"action": "indexed_analyze_error", "chunks": 1}

        if tool == "format":
            if success:
                return {"action": "skipped_format_clean", "chunks": 0}
            # Treat format violations as a build-error-shaped chunk.
            self._index_chunks([chunk_build_error(result, project)])
            return {"action": "indexed_format_error", "chunks": 1}

        logger.debug("Unhandled tool: %s", tool)
        return {"action": "skipped_unknown", "chunks": 0}

    # ── run_tests ──────────────────────────────────────────────────────

    def _handle_run_tests(self, result: str, project: str, timestamp: str) -> dict:
        failed = set(_FAILED_TEST_RE.findall(result))
        passed = set(_PASSED_TEST_RE.findall(result))

        new_chunks: list[dict] = []
        fix_count = 0

        for node_id in failed:
            longrepr = _extract_failure_section(result, node_id) or result[-4000:]
            new_chunks.append(chunk_test_failure(node_id, longrepr, project))
            self._pending_failures[node_id] = {
                "project": project,
                "longrepr": longrepr,
                "timestamp": timestamp,
            }

        for node_id in passed:
            pending = self._pending_failures.pop(node_id, None)
            if pending:
                new_chunks.append(chunk_test_fix(
                    node_id=node_id,
                    failure_longrepr=pending.get("longrepr", ""),
                    project=pending.get("project", project),
                ))
                fix_count += 1

        self._save_buffer()
        self._index_chunks(new_chunks)

        action = (
            "indexed_test_failures_and_fixes" if failed and fix_count
            else "indexed_test_failures" if failed
            else "indexed_test_fixes" if fix_count
            else "skipped_routine_success"
        )
        return {"action": action, "chunks": len(new_chunks)}


def _extract_failure_section(output: str, node_id: str) -> str:
    """
    Pull the section of `dotnet test` output that pertains to `node_id`.
    `dotnet test` typically prints a Failed line then an indented stack
    trace ending before the next test header — grab from the Failed line
    to either the next Passed/Failed line or end of output.
    """
    pat = re.compile(rf"^\s*Failed\s+{re.escape(node_id)}\b.*?$", re.MULTILINE)
    m = pat.search(output)
    if not m:
        return ""
    start = m.start()
    next_test = re.search(r"^\s*(?:Failed|Passed|✓|X)\s+\S", output[m.end():], re.MULTILINE)
    end = m.end() + next_test.start() if next_test else len(output)
    return output[start:end]
