FROM debian:bookworm-slim

LABEL maintainer="mcp-c"
LABEL description="C build + test + analyze tools MCP server"

# Toolchain: gcc 12 (default in bookworm), clang 14, clang-tidy, clang-format,
# cmake, meson, ninja, make, valgrind, cppcheck. Plus python3 for the MCP
# service itself, curl/ca-certs for fetching the mcp-knowledge-base tarball
# and the llvm-mingw release tarball.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc g++ \
        clang clang-tidy clang-format libclang-rt-14-dev \
        cmake meson ninja-build make \
        valgrind cppcheck \
        gdb \
        pkg-config \
        python3 python3-pip \
        curl ca-certificates xz-utils \
    && rm -rf /var/lib/apt/lists/*

# llvm-mingw — clang-based mingw-w64 toolchain for cross-compiling to
# Windows x86_64 (PE/COFF DLLs). Used by the build()/lint()/analyze()
# tools when target="win64". Bumping the tag: pick a recent release from
# https://github.com/mstorsjo/llvm-mingw/releases and update LLVM_MINGW_VER.
ARG LLVM_MINGW_VER=20250528
ARG LLVM_MINGW_DIST=ubuntu-22.04-x86_64
RUN curl -fsSL -o /tmp/llvm-mingw.tar.xz \
        "https://github.com/mstorsjo/llvm-mingw/releases/download/${LLVM_MINGW_VER}/llvm-mingw-${LLVM_MINGW_VER}-ucrt-${LLVM_MINGW_DIST}.tar.xz" \
    && mkdir -p /opt/llvm-mingw \
    && tar -xJf /tmp/llvm-mingw.tar.xz -C /opt/llvm-mingw --strip-components=1 \
    && rm /tmp/llvm-mingw.tar.xz
ENV PATH="/opt/llvm-mingw/bin:${PATH}"

# Python deps for the MCP service. The service is small; pin only what we need.
RUN pip install --no-cache-dir --break-system-packages \
        "mcp>=2,<3" \
        "mcp-knowledge-base @ https://github.com/jasonuithol/ai-agent-mcps/archive/refs/tags/kb-v0.3.0.tar.gz#subdirectory=mcp-knowledge-base"

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5192

CMD ["python3", "mcp-service.py"]
