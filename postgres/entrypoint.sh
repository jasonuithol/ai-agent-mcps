#!/usr/bin/env bash
# entrypoint.sh — boot PostgreSQL (Unix socket only), then exec the MCP service.
#
# Data lives under /var/lib/postgresql/data, which is mounted as a named
# volume by start-container.sh so databases survive container restarts.
# initdb only runs on first boot (empty data dir).
set -euo pipefail

PGDATA=/var/lib/postgresql/data
SOCKET_DIR=/var/run/postgresql

mkdir -p "$SOCKET_DIR"
chown postgres:postgres "$SOCKET_DIR"

# First-boot init. The official postgres image normally handles this via
# its own entrypoint, but we're overriding CMD so we do it ourselves.
if [ ! -s "$PGDATA/PG_VERSION" ]; then
    echo "Initialising fresh PostgreSQL cluster at $PGDATA..."
    mkdir -p "$PGDATA"
    chown -R postgres:postgres "$PGDATA"
    chmod 700 "$PGDATA"
    gosu postgres initdb -D "$PGDATA" --username=postgres --auth=trust --encoding=UTF8
fi

# Disable TCP listening — MCP service connects via Unix socket only.
# listen_addresses='' means no TCP at all; trust auth on the socket is
# fine because nothing outside the container can reach it.
gosu postgres pg_ctl -D "$PGDATA" -o "-c listen_addresses='' -c unix_socket_directories='$SOCKET_DIR'" -w start

echo "PostgreSQL up. Starting MCP service on :5188..."
exec python /app/mcp-service.py
