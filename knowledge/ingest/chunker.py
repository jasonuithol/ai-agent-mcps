"""Chunking logic for dotnet-knowledge sources.

Cross-domain primitives live in `mcp_knowledge_base.chunks` and are
re-exported here for the convenience of router.py / mcp-service.py.
"""

from __future__ import annotations

import re

from mcp_knowledge_base import (
    now_iso,
    sanitize_for_id,
    tag_flags,
    tag_key,
    upsert_chunks,
)

from .extractors import (
    detect_tags,
    extract_module_name,
    extract_top_level_nodes,
)

__all__ = [
    "chunk_dotnet_source",
    "chunk_docs",
    "chunk_test_failure",
    "chunk_test_fix",
    "chunk_build_error",
    "chunk_analyze_error",
    "tag_key",
    "tag_flags",
    "upsert_chunks",
]


# ── .NET source ───────────────────────────────────────────────────────────────

def chunk_dotnet_source(
    source: str,
    file_path: str,
    project: str,
    project_root: str,
    extra_tags: list[str] | None = None,
) -> list[dict]:
    """Chunk a .cs file by top-level type / method.

    Files with no extracted nodes become a single whole-file chunk.
    """
    extra_tags = extra_tags or []
    module = extract_module_name(file_path, project_root)
    nodes = extract_top_level_nodes(source)
    now = now_iso()
    chunks: list[dict] = []

    if not nodes:
        tags = [*extra_tags, project.lower(), *detect_tags(source)]
        chunks.append({
            "id": f"dotnet-source/{project}/{sanitize_for_id(module)}",
            "document": source,
            "metadata": {
                "source": f"dotnet-source/{project}/{module}",
                "type": "module",
                "module": module,
                "class_name": "",
                "func_name": "",
                "tags": ",".join(tags),
                "indexed_at": now,
                "project": project,
                **tag_flags(tags),
            },
        })
        return chunks

    seen_ids: set[str] = set()
    for node in nodes:
        kind = node["kind"]
        name = node["name"]
        class_name = node["class_name"]
        text = node["text"]
        ident = f"{class_name}.{name}" if class_name else name
        cid = f"dotnet-source/{project}/{sanitize_for_id(module)}/{kind}/{sanitize_for_id(ident)}"
        if cid in seen_ids:
            # Overloaded method or duplicate name — disambiguate by hash
            # suffix of the body so each chunk survives.
            cid = f"{cid}-{abs(hash(text)) & 0xFFFF:04x}"
        seen_ids.add(cid)

        tags = [*extra_tags, project.lower(), *detect_tags(text)]
        chunks.append({
            "id": cid,
            "document": text,
            "metadata": {
                "source": f"dotnet-source/{project}/{module}",
                "type": kind,
                "module": module,
                "class_name": class_name,
                "func_name": node["func_name"],
                "tags": ",".join(tags),
                "indexed_at": now,
                "project": project,
                **tag_flags(tags),
            },
        })

    return chunks


# ── Markdown docs ─────────────────────────────────────────────────────────────

_H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def chunk_docs(text: str, source_path: str, extra_tags: list[str] | None = None) -> list[dict]:
    """One chunk per ##-section in a markdown file."""
    extra_tags = extra_tags or []
    matches = list(_H2_RE.finditer(text))
    now = now_iso()
    chunks: list[dict] = []

    if not matches:
        tags = [*extra_tags, "docs", *detect_tags(text)]
        chunks.append({
            "id": f"docs/{sanitize_for_id(source_path)}",
            "document": text,
            "metadata": {
                "source": f"docs/{source_path}",
                "type": "section",
                "module": "",
                "class_name": "",
                "func_name": "",
                "tags": ",".join(tags),
                "indexed_at": now,
                "project": "",
                **tag_flags(tags),
            },
        })
        return chunks

    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        tags = [*extra_tags, "docs", *detect_tags(body)]
        chunks.append({
            "id": f"docs/{sanitize_for_id(source_path)}/{sanitize_for_id(title)}",
            "document": body,
            "metadata": {
                "source": f"docs/{source_path}",
                "type": "section",
                "module": title,
                "class_name": "",
                "func_name": "",
                "tags": ",".join(tags),
                "indexed_at": now,
                "project": "",
                **tag_flags(tags),
            },
        })
    return chunks


# ── Build / test / analyze signal chunks ──────────────────────────────────────

def chunk_build_error(output: str, project: str) -> dict:
    tags = [project.lower(), "build-error", *detect_tags(output)]
    return {
        "id": f"build-error/{project}/{abs(hash(output)) & 0xFFFFFFFF:08x}",
        "document": output[-8000:],
        "metadata": {
            "source": f"build-error/{project}",
            "type": "error",
            "module": "",
            "class_name": "",
            "func_name": "",
            "tags": ",".join(tags),
            "indexed_at": now_iso(),
            "project": project,
            **tag_flags(tags),
        },
    }


def chunk_test_failure(node_id: str, longrepr: str, project: str) -> dict:
    tags = [project.lower(), "test-failure", *detect_tags(longrepr)]
    return {
        "id": f"test-failure/{project}/{sanitize_for_id(node_id)}",
        "document": f"FAILING: {node_id}\n\n{longrepr[-6000:]}",
        "metadata": {
            "source": f"test-failure/{project}",
            "type": "test-failure",
            "module": node_id,
            "class_name": "",
            "func_name": "",
            "tags": ",".join(tags),
            "indexed_at": now_iso(),
            "project": project,
            **tag_flags(tags),
        },
    }


def chunk_test_fix(node_id: str, failure_longrepr: str, project: str) -> dict:
    tags = [project.lower(), "test-fix"]
    return {
        "id": f"test-fix/{project}/{sanitize_for_id(node_id)}-{now_iso()}",
        "document": f"FIXED: {node_id}\n\nPrior failure:\n{failure_longrepr[-3000:]}",
        "metadata": {
            "source": f"test-fix/{project}",
            "type": "test-fix",
            "module": node_id,
            "class_name": "",
            "func_name": "",
            "tags": ",".join(tags),
            "indexed_at": now_iso(),
            "project": project,
            **tag_flags(tags),
        },
    }


def chunk_analyze_error(output: str, project: str) -> dict:
    tags = [project.lower(), "analyzer", *detect_tags(output)]
    return {
        "id": f"analyze-error/{project}/{abs(hash(output)) & 0xFFFFFFFF:08x}",
        "document": output[-8000:],
        "metadata": {
            "source": f"analyze-error/{project}",
            "type": "error",
            "module": "",
            "class_name": "",
            "func_name": "",
            "tags": ",".join(tags),
            "indexed_at": now_iso(),
            "project": project,
            **tag_flags(tags),
        },
    }
