FROM docker.io/library/postgres:16-bookworm

LABEL maintainer="mcp-db"
LABEL description="PostgreSQL database workbench: list/create/drop databases, run DDL and SQL via MCP"

# Python + psycopg for the MCP service. The base image provides postgres,
# initdb, pg_ctl, and the postgres user.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv \
        gosu \
    && rm -rf /var/lib/apt/lists/*

# Use a venv so pip install isn't blocked by PEP 668 on bookworm.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir \
        fastmcp \
        psycopg[binary]

WORKDIR /app
COPY mcp-service.py entrypoint.sh ./
RUN chmod +x entrypoint.sh

# MCP transport port and PostgreSQL itself, for direct DB access from host.
EXPOSE 5188
EXPOSE 5432

# entrypoint.sh boots PostgreSQL then exec's the MCP service.
CMD ["./entrypoint.sh"]
