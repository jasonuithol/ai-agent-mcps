#!/usr/bin/env bash
# entrypoint.sh — boot SQL Server, wait for it, then exec the MCP service.
#
# SQL Server requires:
#   ACCEPT_EULA=Y
#   MSSQL_SA_PASSWORD set to a strong password (>=8 chars, mixed classes)
# Both are provided by start-container.sh as -e flags. Data lives under
# /var/opt/mssql, mounted as a named volume so databases persist.
set -euo pipefail

if [ -z "${ACCEPT_EULA:-}" ] || [ -z "${MSSQL_SA_PASSWORD:-}" ]; then
    echo "entrypoint: ACCEPT_EULA and MSSQL_SA_PASSWORD must both be set." >&2
    exit 1
fi

# Start sqlservr in the background. The MCP service connects to it via
# localhost:1433 once it's up.
/opt/mssql/bin/sqlservr &
SQL_PID=$!

# Forward signals so docker stop shuts SQL Server down cleanly.
trap 'kill -TERM "$SQL_PID" 2>/dev/null; wait "$SQL_PID"; exit 0' TERM INT

# Wait for SQL Server to accept TCP connections. /dev/tcp is bash-builtin —
# avoids needing nc or sqlcmd in the image. Cap at ~60s; first-boot does
# template DB extraction which can be slow on cold I/O.
echo "Waiting for SQL Server to accept connections on localhost:1433..."
for i in $(seq 1 60); do
    if (exec 3<>/dev/tcp/127.0.0.1/1433) 2>/dev/null; then
        exec 3<&-; exec 3>&-
        echo "  up after ${i}s"
        break
    fi
    sleep 1
    if [ "$i" = "60" ]; then
        echo "entrypoint: SQL Server did not come up within 60s." >&2
        kill "$SQL_PID" 2>/dev/null || true
        exit 1
    fi
done

echo "Starting MCP service on :5189..."
exec python /app/mcp-service.py
