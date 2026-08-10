# ai-agent-mcps

Monorepo of MCP services, consolidated from the individual `mcp-*` repositories.
Each subdirectory retains the full commit history of its original repo.

All services implement the stateless **MCP 2026-07-28** specification via the
official Python SDK (`mcp>=2,<3`): no `initialize` handshake, no `Mcp-Session-Id`,
one POST per request. Legacy handshake-era clients are still answered by the SDK.
The pre-migration state is preserved under the `stateful` tag.

| Service | Description |
|---------|-------------|
| `mcp-c` | MCP service pair for C development (workbench + knowledge containers). |
| `mcp-chess` | MCP service pair for chess engine development. |
| `mcp-db` | MCP services for relational databases (Postgres + MSSQL). |
| `mcp-dosre` | DOS reverse-engineering tools (incl. decompile via rizin + rz-ghidra). |
| `mcp-dotnet` | MCP service pair for .NET development. |
| `mcp-knowledge-base` | Shared MCP + ChromaDB scaffolding for RAG-backed knowledge MCP services. |
| `mcp-pygame` | MCP service pair for Python / pygame development. |
| `mcp-ssis` | SSIS-on-Linux: validate, run, and benchmark `.dtsx` packages. |
| `mcp-steam` | Steam client process control (status, start, stop, ...). |
| `mcp-ue4ss` | UE4SS domain knowledge base — RAG over RE-UE4SS docs and C++ API. |
| `mcp-valheim` | MCP service trio for Valheim mod development. |
