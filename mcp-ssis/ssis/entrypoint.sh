#!/usr/bin/env bash
# entrypoint.sh — probe the peer SQL Server, then exec the MCP service.
#
# Unlike mcp-db/mssql, there is no engine to babysit here — dtexec is
# spawned per-request from inside the MCP service. We only need to make
# sure the peer mssql container is reachable so the first benchmark run
# doesn't surprise the caller.
set -euo pipefail

MSSQL_HOST="${MSSQL_HOST:-host.containers.internal}"
MSSQL_PORT="${MSSQL_PORT:-1433}"

# Warn (not fail) if the peer isn't up: tools that don't need state-reset
# can still run packages against in-package connections, and the peer may
# come up after us in a docker-compose-style start.
echo "Probing peer SQL Server at ${MSSQL_HOST}:${MSSQL_PORT}..."
ok=false
for i in $(seq 1 10); do
    if (exec 3<>/dev/tcp/"$MSSQL_HOST"/"$MSSQL_PORT") 2>/dev/null; then
        exec 3<&-; exec 3>&-
        echo "  reachable after ${i}s"
        ok=true
        break
    fi
    sleep 1
done
if [ "$ok" = false ]; then
    echo "  WARNING: peer not reachable yet — benchmark reset_sql will fail until it is" >&2
fi

mkdir -p /packages/logs

echo "Starting MCP service on :5190..."
exec python /app/mcp-service.py
