"""mcp-knowledge: RAG-backed .NET knowledge service.

Built on `mcp-knowledge-base`, which provides FastMCP + ChromaDB +
/ingest scaffolding. This module adds only the .NET-specific pieces:
the chunker, tag taxonomy, and seed tools.

Collection is *domain-scoped*: all .NET projects share `dotnet_knowledge`
so cross-project patterns surface during retrieval. The `project`
metadata field identifies origin when that matters.
"""

from __future__ import annotations

import os
from pathlib import Path

from mcp_knowledge_base import KnowledgeService, ServiceConfig

from ingest.chunker import (
    chunk_dotnet_source,
    chunk_docs,
    upsert_chunks,
)
from ingest.extractors import PATTERN_TAGS, detect_tags
from ingest.router import DotnetIngestRouter

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECTS_DIR = os.environ.get("PROJECTS_DIR", "/opt/projects")

# ---------------------------------------------------------------------------
# Service assembly
# ---------------------------------------------------------------------------

svc = KnowledgeService(ServiceConfig.from_env(
    name="dotnet-knowledge",
    collection_name="dotnet_knowledge",
    port=5204,
    header_keys=["project", "module", "class_name", "func_name"],
))

svc.register_default_tools()
svc.register_retag_all(PATTERN_TAGS, detect_tags)
svc.set_ingest_router(DotnetIngestRouter(svc.collection))

collection = svc.collection
mcp = svc.mcp


# ---- Domain-specific query tools -----------------------------------------

@svc.tool()
def ask_module(module: str) -> str:
    """Find knowledge about a specific module path (e.g. 'src.Foo.Bar')."""
    results = collection.query(
        query_texts=[module],
        n_results=10,
        where={"module": module},
    )
    return svc.format_query(results)


@svc.tool()
def ask_project(question: str, project: str) -> str:
    """Scope a semantic search to one project's chunks."""
    results = collection.query(
        query_texts=[question],
        n_results=5,
        where={"project": project},
    )
    return svc.format_query(results)


# ---- Seed tools -----------------------------------------------------------

@svc.tool()
def seed_docs(docs_path: str) -> str:
    """Index every `.md` file under a directory by `##` section.

    Args:
        docs_path: Absolute path (as seen from inside this container) to a
                   directory of markdown docs, e.g. '/opt/projects/mcp-dotnet/docs'.
    """
    root = Path(docs_path)
    if not root.is_dir():
        return f"ERROR: {docs_path} is not a directory."

    files = sorted(root.rglob("*.md"))
    if not files:
        return f"No markdown files under {docs_path}."

    all_chunks: list[dict] = []
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception as e:
            return f"ERROR reading {f}: {e}"
        rel = str(f.relative_to(root))
        all_chunks.extend(chunk_docs(text, rel))

    upsert_chunks(collection, all_chunks)
    return f"Indexed {len(all_chunks)} chunks from {len(files)} files under {docs_path}."


@svc.tool()
def seed_dotnet_source(
    project: str,
    source_dir: str,
    extra_tags: list[str] | None = None,
) -> str:
    """Index a .NET project's C# source tree.

    Walks `source_dir` for `.cs` files (skipping obj/, bin/, .git/,
    Migrations/) and chunks each by top-level type/method.

    Args:
        project:    Logical project name (used as a tag and in chunk source ids).
        source_dir: Absolute path (as seen from inside this container) to the
                    project root, e.g. '/opt/projects/betl'.
        extra_tags: Optional list of tags to apply to every chunk (e.g.
                    ['successful-example']).
    """
    extra_tags = extra_tags or []
    root = Path(source_dir)
    if not root.is_dir():
        return f"ERROR: {source_dir} is not a directory."

    SKIP_DIRS = {"obj", "bin", ".git", "Migrations", "node_modules", ".vs"}

    cs_files: list[Path] = []
    for p in root.rglob("*.cs"):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts[:-1]):
            continue
        cs_files.append(p)

    if not cs_files:
        return f"No .cs files under {source_dir}."

    all_chunks: list[dict] = []
    for f in cs_files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        all_chunks.extend(
            chunk_dotnet_source(text, str(f), project, str(root), extra_tags=extra_tags)
        )

    upsert_chunks(collection, all_chunks)
    return f"Indexed {len(all_chunks)} chunks from {len(cs_files)} .cs files in project '{project}'."


# ---- Entrypoint -----------------------------------------------------------

if __name__ == "__main__":
    svc.run()
