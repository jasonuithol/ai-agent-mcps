"""mcp-knowledge: RAG-backed chess engine knowledge service.

Built on `mcp-knowledge-base`, which provides the FastMCP + ChromaDB +
/ingest scaffolding. This module adds chess-specific seeding tools.

Collection is *domain-scoped*: all chess engine projects share
`chess_knowledge` so cross-project patterns (eval ideas, search
techniques, NNUE recipes) surface during retrieval. The `project`
metadata field identifies origin when that matters.

Seeding sources (intended):
  - chessprogramming.org wiki (CC-BY-SA, MediaWiki API)
  - Stockfish docs (https://official-stockfish.github.io/docs/, GPL)
  - python-chess docs (Sphinx, GPL)

Phase-1 ships seed_docs() for local markdown/text content; the wiki
ingester is queued for phase 2 (see CLAUDE.md).
"""

from __future__ import annotations

import os
import re
from pathlib import Path

from mcp_knowledge_base import KnowledgeService, ServiceConfig

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECTS_DIR = os.environ.get("PROJECTS_DIR", "/opt/projects")

# ---------------------------------------------------------------------------
# Service assembly
# ---------------------------------------------------------------------------

svc = KnowledgeService(ServiceConfig.from_env(
    name="chess-knowledge",
    collection_name="chess_knowledge",
    port=5186,
    header_keys=["project", "topic", "page_title"],
))

svc.register_default_tools(exclude={"stats"})

collection = svc.collection
mcp = svc.mcp


# ---- stats() override (adds project + topic breakdown) -------------------


@svc.tool()
def stats() -> str:
    """Collection size, source/type/tag/project/topic distributions."""
    count = collection.count()
    if count == 0:
        return "Knowledge base is empty."

    all_meta = collection.get(include=["metadatas"])

    sources: dict[str, int] = {}
    tags_count: dict[str, int] = {}
    types: dict[str, int] = {}
    projects: dict[str, int] = {}
    topics: dict[str, int] = {}

    for meta in all_meta["metadatas"]:
        src = meta.get("source", "unknown")
        sources[src] = sources.get(src, 0) + 1

        chunk_type = meta.get("type", "unknown")
        types[chunk_type] = types.get(chunk_type, 0) + 1

        proj = meta.get("project", "") or "(none)"
        projects[proj] = projects.get(proj, 0) + 1

        topic = meta.get("topic", "") or "(none)"
        topics[topic] = topics.get(topic, 0) + 1

        for tag in meta.get("tags", "").split(","):
            tag = tag.strip()
            if tag:
                tags_count[tag] = tags_count.get(tag, 0) + 1

    lines = [f"Total chunks: {count}", ""]

    lines.append(f"Projects ({len(projects)}):")
    for p, c in sorted(projects.items(), key=lambda x: -x[1]):
        lines.append(f"  {p}: {c}")

    lines.append(f"\nTop sources ({len(sources)}):")
    for src, c in sorted(sources.items(), key=lambda x: -x[1])[:20]:
        lines.append(f"  {src}: {c}")

    lines.append("\nTopics:")
    for t, c in sorted(topics.items(), key=lambda x: -x[1])[:20]:
        lines.append(f"  {t}: {c}")

    lines.append("\nTypes:")
    for t, c in sorted(types.items(), key=lambda x: -x[1]):
        lines.append(f"  {t}: {c}")

    lines.append("\nTop tags:")
    for tag, c in sorted(tags_count.items(), key=lambda x: -x[1])[:20]:
        lines.append(f"  {tag}: {c}")

    return "\n".join(lines)


# ---- Domain-specific seeding tools ---------------------------------------


_HEADER_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def _chunk_markdown(text: str, source_name: str, topic: str | None) -> list[dict]:
    """Split a markdown doc into chunks at `## ` headers."""
    chunks: list[dict] = []
    parts = _HEADER_RE.split(text)
    # Pattern: [preamble, h1, body1, h2, body2, ...]
    if parts and parts[0].strip():
        chunks.append({
            "text": parts[0].strip(),
            "metadata": {
                "source": source_name,
                "type": "doc",
                "section": "(intro)",
                "topic": topic or "",
                "tags": "doc",
            },
        })
    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if not body:
            continue
        chunks.append({
            "text": f"## {header}\n\n{body}",
            "metadata": {
                "source": source_name,
                "type": "doc",
                "section": header,
                "topic": topic or "",
                "tags": "doc",
            },
        })
    return chunks


def _upsert(chunks: list[dict]) -> None:
    """Insert chunks into the collection with deterministic ids."""
    if not chunks:
        return
    ids: list[str] = []
    docs: list[str] = []
    metas: list[dict] = []
    for i, ch in enumerate(chunks):
        # Hash-free id: source + section + index. Stable enough across reseeds.
        src = ch["metadata"].get("source", "x")
        sect = ch["metadata"].get("section", "x")
        ids.append(f"{src}::{sect}::{i}".replace(" ", "_"))
        docs.append(ch["text"])
        metas.append(ch["metadata"])
    collection.upsert(ids=ids, documents=docs, metadatas=metas)


@svc.tool()
def seed_docs(docs_path: str, topic: str = None) -> str:
    """Index every *.md under a directory as curated docs.

    Chunks by `## ` header. Adds an optional `topic` tag (e.g.
    'chessprogramming-wiki', 'stockfish', 'python-chess').

    Args:
        docs_path: Directory to walk recursively.
        topic: Optional topic label stored in metadata.topic.
    """
    docs_dir = Path(docs_path)
    if not docs_dir.is_dir():
        return f"Directory not found: {docs_path}"

    total_chunks = 0
    files_indexed: list[str] = []

    for md_file in sorted(docs_dir.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        chunks = _chunk_markdown(text, md_file.name, topic)
        if chunks:
            _upsert(chunks)
            total_chunks += len(chunks)
            files_indexed.append(f"  {md_file.relative_to(docs_dir)}: {len(chunks)} chunks")

    if not files_indexed:
        return f"No .md files found under {docs_path}"

    return (
        f"Indexed {total_chunks} chunks from {len(files_indexed)} files"
        + (f" (topic={topic})" if topic else "")
        + ":\n"
        + "\n".join(files_indexed)
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    svc.run()
