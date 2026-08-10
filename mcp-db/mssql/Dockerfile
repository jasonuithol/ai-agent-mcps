FROM mcr.microsoft.com/mssql/server:2022-latest

LABEL maintainer="mcp-db"
LABEL description="MSSQL database workbench: list/create/drop databases, run DDL and SQL via MCP"

# The base image is Ubuntu 22.04. Layering Python + pymssql on top so the
# MCP service can run inside the same container as sqlservr — keeps the
# wire path short (localhost:1433 → in-process driver) and the orchestration
# simple (one container per engine, mirrors the postgres side).
USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Use a venv so pip install isn't blocked by PEP 668. pymssql 2.3+ ships
# manylinux wheels with vendored FreeTDS — no extra system libs needed.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir \
        "mcp>=2,<3" \
        pymssql

WORKDIR /app
COPY mcp-service.py entrypoint.sh ./
RUN chmod +x entrypoint.sh && chown -R mssql:root /app

# MCP transport port and SQL Server itself, for direct DB access from host.
EXPOSE 5189
EXPOSE 1433

# entrypoint.sh boots SQL Server in the background, waits for it, then
# exec's the MCP service. Run as the 'mssql' user the base image expects.
USER mssql
CMD ["./entrypoint.sh"]
