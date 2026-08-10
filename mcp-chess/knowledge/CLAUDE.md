# chess-mcp-knowledge — design notes

## What this service is

Domain-scoped RAG over chess-engine-development knowledge. Single
ChromaDB collection `chess_knowledge`. All projects share it so
cross-project patterns surface during retrieval. `project` metadata
identifies origin when callers care.

## Built on

[`mcp-knowledge-base`](https://github.com/jasonuithol/mcp-knowledge-base)
v0.2.1 supplies the FastMCP + ChromaDB + `/ingest` scaffolding.
This service adds chess-specific tooling:

- `seed_docs(docs_path, topic)` — markdown ingester, chunks at `## `.
- `stats()` — overrides default to add project + topic breakdowns.

## Embedding model

`all-MiniLM-L6-v2`, baked into the image (Dockerfile pre-fetches the
ONNX bundle). No first-run download. Container needs an NVIDIA GPU
(CUDA 12.8) for accelerated embeddings via ONNX Runtime.

## Phase 2 — sources still to ingest

Three primary external sources, all with clean ingestion paths:

### 1. chessprogramming.org wiki (CC-BY-SA)

MediaWiki-backed. Use the API, not HTML scraping:

```
https://www.chessprogramming.org/api.php?action=query&list=allpages&aplimit=500&format=json
https://www.chessprogramming.org/api.php?action=parse&page=<title>&prop=wikitext&format=json
```

Plan:
- `seed_chessprogramming_wiki(category=None, max_pages=None)` tool.
- Fetch page list (optionally filter by category, e.g. "Search",
  "Evaluation").
- For each page, parse wikitext → markdown via mwparserfromhell or strip
  tags directly. Chunk at `==` headings (MediaWiki section markers).
- Metadata: `source="chessprogramming.org"`, `topic="<category>"`,
  `page_title=<title>`, `tags="wiki,cc-by-sa"`.
- Be polite: 1 request/sec, User-Agent string identifying the project.

### 2. Stockfish documentation (GPL)

Lives at https://official-stockfish.github.io/docs/ and in the source
repo's `docs/` directory. Small, ingest the whole thing once.
`topic="stockfish"`, `tags="reference-engine"`.

### 3. python-chess documentation (GPL)

Sphinx-built, hosted on Read the Docs. Has a proper `objects.inv` for
precise symbol → URL mapping. Use Sphinx's intersphinx-format inventory
rather than scraping rendered HTML — cleaner section boundaries and
canonical anchors.

`topic="python-chess"`, `tags="library,api-reference"`.

## Attribution requirement

CPW content is CC-BY-SA. If this image is ever distributed (it isn't,
per the repo's local-rebuild model), seeded chunks need attribution
alongside their content. Currently a non-issue.

## What to NOT seed

- Engine source code from arbitrary GPL engines. Code chunks belong in
  the engine's own knowledge sub-collection (or in mcp-c if the engine
  is C/C++) — chess_knowledge is for *concepts*, not specific engines'
  implementations.
- Game databases / PGN dumps. Wrong tool — use a real PGN store.
