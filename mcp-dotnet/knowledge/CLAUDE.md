# mcp-knowledge — .NET Knowledge Service

A RAG-backed MCP service that accumulates knowledge from indexing
project source, curated docs, and the build / test / analyze signals
fired by the sibling `service/` (`dotnet-mcp-build`).

Sibling to the pygame / Valheim / C variants of this service. All share
the `mcp-knowledge-base` scaffolding but stay isolated — one sandbox
runs at a time per host.

---

## Design principle: domain-scoped collection

All .NET projects share a single ChromaDB collection: `dotnet_knowledge`.
Retrieval crosses project boundaries deliberately — a pattern learned
in project A is discoverable while working in project B. Each chunk
carries a `project` metadata field, so scoped queries are still
possible via `ask_project(question, project)`.

---

## Passive ingest, active query

Tool executions in `dotnet-mcp-build` fire fire-and-forget POSTs to
`/ingest`. The router (`ingest/router.py`) decides what to index:

- **Build failures** (`build`) — one chunk per failed invocation.
- **Test failures** (`run_tests`) — one chunk per failing
  `Namespace.Class.Method` extracted from `dotnet test` output.
- **Test fixes** — when a previously-failing test now passes, a
  `test-fix` chunk pairs the old failure with the resolution timestamp.
  Buffer persists across container restarts at
  `/opt/knowledge/test_failure_buffer.json`.
- **Analyzer / format failures** (`analyze`, `format`) — one chunk per
  failing run.

Successful builds, clean analyses, and clean format checks are skipped.

---

## MCP tools

### Query
| Tool | Purpose |
|------|---------|
| `ask(question)` | Semantic search across the whole collection |
| `ask_tagged(question, tags)` | Filter by one or more tags |
| `ask_module(module)` | Filter by module path (e.g. `src.Foo.Bar`) |
| `ask_project(question, project)` | Scope to one project |

### Maintenance
| Tool | Purpose |
|------|---------|
| `list_sources()` | Every indexed source with chunk count |
| `stats()` | Totals by source, type, tag |
| `forget(source)` | Delete chunks matching a source (supports prefix) |
| `retag_all()` | Re-run tag auto-detection across every chunk |

### Seed
| Tool | Purpose |
|------|---------|
| `seed_docs(docs_path)` | Index every `.md` under a directory by `##` section |
| `seed_dotnet_source(project, source_dir, extra_tags=[])` | Index a C# source tree |

---

## Chunking strategy

Roslyn is heavyweight — for retrieval we use regex extractors. Good enough;
the embedding model forgives noise.

| Source | Boundary | Typical size |
|--------|----------|--------------|
| .cs file | One chunk per top-level type / method | 5-200 lines |
| .cs file (no nodes extracted) | One whole-file chunk | variable |
| Markdown doc | One chunk per `## ` section | 10-100 lines |
| Build error | One chunk per failed `build` | medium |
| Test failure | One chunk per failing test node | small |
| Test fix | One chunk per fail→pass transition | small |
| Analyze error | One chunk per failed `analyze` | medium |

The regex chunker walks brace pairs naïvely — an unbalanced `{` inside
a string literal could over-extend a chunk. Embedding query is robust.

---

## Metadata schema

```python
{
    "source":      "dotnet-source/MyProj/src.Foo.Bar",
    "type":        "method",         # class | struct | interface | record | enum | method | module | section | error | test-failure | test-fix
    "module":      "src.Foo.Bar",
    "class_name":  "Bar",            # enclosing type for methods
    "func_name":   "DoThing",        # method name, "" otherwise
    "tags":        "myproj,async,xunit",
    "indexed_at":  "2026-05-15T08:00:00Z",
    "project":     "MyProj",
    # Plus per-tag boolean keys for filtering:
    "tag_myproj":   True,
    "tag_async":    True,
    "tag_xunit":    True,
}
```

---

## Container layout

```
mcp-dotnet/knowledge/
├── CLAUDE.md              ← this file
├── Dockerfile             ← CUDA base for GPU-accelerated embeddings
├── requirements.txt       ← mcp (SDK v2), chromadb, mcp-knowledge-base, onnxruntime-gpu
├── build-container.sh
├── start-container.sh     ← runs with --device nvidia.com/gpu=all
├── seed.sh                ← edit to add your projects
├── mcp-service.py         ← MCP server + /ingest endpoint
├── ingest/
│   ├── chunker.py         ← C# source + markdown chunking
│   ├── extractors.py      ← PATTERN_TAGS, regex node walker
│   └── router.py          ← build / run_tests / analyze / format routing
└── knowledge/             ← ChromaDB persistent storage (gitignored)
```

---

## Seeding workflow

First-time setup after `start-container.sh`:

```bash
./seed.sh
```

Edit `seed.sh` to add blocks for your projects. After seeding, the
knowledge base grows automatically from `build` / `run_tests` /
`analyze` / `format` invocations on the sibling build service.

External docs (MS Learn .NET, xUnit, MSBuild reference) aren't seeded
automatically — they don't ship as tarballs. Mirror them locally:

```bash
wget --mirror --no-parent --convert-links \
     -P ~/dotnet-docs/ms-learn-fundamentals \
     https://learn.microsoft.com/en-us/dotnet/fundamentals/
```

then call `seed_docs("/opt/projects/<path-to-mirrored-dir>")`.

---

## Known concerns

### 1. Regex chunking is approximate

Lambdas at class scope, multi-line method signatures, and `{` inside
string literals can throw off boundaries. Output is still indexable.
For accurate parsing, Roslyn — out of scope for v1.

### 2. Test failure extraction depends on `dotnet test` output shape

We grep for `^Failed Namespace.Class.Method`. If a custom logger is
configured that emits a different shape, failures may not be captured.
The console logger is the default; if you set `--logger trx` only,
failures land as one coarse chunk instead of one-per-test.

### 3. No deduplication on re-seed

`seed_dotnet_source` uses deterministic ids
(`dotnet-source/{project}/{module}/{kind}/{name}`), so re-seeding
upserts rather than duplicating. But if a method is renamed or
deleted, the old chunk lingers — run
`forget("dotnet-source/<project>")` before re-seeding a refactored
project.

---

## Non-goals

- Not a replacement for curated docs.
- Not general-purpose — scoped to .NET work.
- No fine-tuning or model training — pure retrieval.
