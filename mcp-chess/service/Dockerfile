FROM python:3.12-slim-bookworm

LABEL maintainer="mcp-chess"
LABEL description="Chess engine development workbench: Stockfish + fastchess + python-chess MCP server"

# System deps:
#   stockfish      -> reference engine, autoregistered at startup
#   build-essential, git -> needed to compile fastchess from source
#   curl, ca-certs -> mcp-knowledge-base tarball fetch + general fetches
RUN apt-get update && apt-get install -y --no-install-recommends \
        stockfish \
        build-essential \
        git \
        curl \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Build fastchess from source. The repo's top-level Makefile produces a
# `fastchess` binary; we install it onto PATH. Pinned to main for now —
# bump to a tagged release once one suits.
RUN git clone --depth 1 https://github.com/Disservin/fastchess.git /tmp/fastchess \
    && cd /tmp/fastchess \
    && make -j"$(nproc)" \
    && cp fastchess /usr/local/bin/fastchess \
    && rm -rf /tmp/fastchess

# Strip the build toolchain after fastchess is built — the runtime image
# only needs the binary, not the compiler. Keeps the layer reasonable.
RUN apt-get purge -y --auto-remove build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Python deps for the MCP service. python-chess gives us UCI subprocess
# management, FEN/PGN/SAN, perft, Polyglot books, Syzygy tablebases.
RUN pip install --no-cache-dir \
        fastmcp \
        chess \
        "mcp-knowledge-base @ https://github.com/jasonuithol/mcp-knowledge-base/archive/refs/tags/v0.2.1.tar.gz"

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5180

CMD ["python", "mcp-service.py"]
