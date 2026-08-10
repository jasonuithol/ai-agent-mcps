#!/usr/bin/env python3
"""
mcp-service.py — chess-engine

Runs inside a Docker container. Exposes UCI engine control, position
analysis, perft, engine-vs-engine matches (fastchess), SPRT, and EPD
tactics-suite scoring to Claude Code.

Stockfish (apt) is auto-registered as `stockfish` on startup. Additional
engines are added at runtime via `register_engine`.

Register with Claude Code (run this inside the claude-sandbox-core container):
    claude mcp add chess-engine --transport http http://localhost:5180/mcp
"""

from __future__ import annotations

import asyncio
import atexit
import io
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import chess
import chess.engine
import chess.pgn
from fastmcp import FastMCP
from mcp_knowledge_base import KnowledgeReporter

# ── Config ────────────────────────────────────────────────────────────────────

PROJECTS_DIR = Path(os.environ.get("PROJECTS_DIR", "/opt/projects"))
STOCKFISH_PATH = os.environ.get("STOCKFISH_PATH", shutil.which("stockfish") or "/usr/games/stockfish")
FASTCHESS_PATH = os.environ.get("FASTCHESS_PATH", shutil.which("fastchess") or "/usr/local/bin/fastchess")

# ── Knowledge reporter ────────────────────────────────────────────────────────

_reporter = KnowledgeReporter(service="chess-engine")
_report = _reporter.report


# ── Engine registry ───────────────────────────────────────────────────────────

class EngineEntry:
    """A registered UCI engine with its persistent subprocess."""
    def __init__(self, name: str, path: str, engine: chess.engine.SimpleEngine, options: dict[str, Any]):
        self.name = name
        self.path = path
        self.engine = engine
        self.options = options or {}

    def close(self) -> None:
        try:
            self.engine.quit()
        except Exception:
            pass


_engines: dict[str, EngineEntry] = {}


def _close_all_engines() -> None:
    for entry in list(_engines.values()):
        entry.close()
    _engines.clear()


atexit.register(_close_all_engines)


def _open_engine(name: str, path: str, options: dict[str, Any] | None) -> EngineEntry:
    if not Path(path).exists():
        raise FileNotFoundError(f"Engine binary not found: {path}")
    engine = chess.engine.SimpleEngine.popen_uci(path)
    if options:
        # Filter to options the engine actually advertises; UCI rejects unknown ones.
        valid = {k: v for k, v in options.items() if k in engine.options}
        if valid:
            engine.configure(valid)
    return EngineEntry(name=name, path=path, engine=engine, options=options or {})


def _get_engine(name: str) -> chess.engine.SimpleEngine:
    if name not in _engines:
        raise KeyError(
            f"Engine {name!r} not registered. Use list_engines() to see what's available, "
            f"or register_engine() to add one."
        )
    return _engines[name].engine


def _build_limit(depth: int | None, movetime_ms: int | None, nodes: int | None = None) -> chess.engine.Limit:
    if depth is None and movetime_ms is None and nodes is None:
        # Default to a modest depth so unbounded calls don't run forever.
        return chess.engine.Limit(depth=15)
    return chess.engine.Limit(
        depth=depth,
        time=(movetime_ms / 1000.0) if movetime_ms is not None else None,
        nodes=nodes,
    )


def _parse_board(fen: str) -> chess.Board:
    try:
        return chess.Board(fen)
    except ValueError as e:
        raise ValueError(f"Invalid FEN: {e}") from e


# ── Async wrappers ────────────────────────────────────────────────────────────

async def _to_thread(fn, *args, **kwargs):
    return await asyncio.to_thread(fn, *args, **kwargs)


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="chess-engine",
    instructions=(
        "Tools for chess engine development: UCI engine registry, position analysis, "
        "perft (move-generation correctness), engine-vs-engine matches via fastchess, "
        "SPRT (Sequential Probability Ratio Test) for patch testing, and EPD tactics-suite "
        "scoring. Stockfish is autoregistered as 'stockfish'. Register additional engines "
        "with register_engine(name, path); engine binaries live at /opt/projects/<repo>/..."
    ),
)


# ── Engine management ─────────────────────────────────────────────────────────

@mcp.tool()
async def register_engine(name: str, path: str, options: dict[str, Any] = None) -> str:
    """
    Register a UCI engine with the service, opening its subprocess and
    keeping it alive across calls.

    Args:
        name: Short identifier used in subsequent tool calls.
        path: Absolute path to the engine binary inside the container
              (typically under /opt/projects/<repo>/...).
        options: UCI options to set, e.g. {"Hash": 64, "Threads": 1}.
                 Unknown options (not advertised by the engine) are ignored.
    """
    if name in _engines:
        return f"Engine {name!r} already registered (path={_engines[name].path}). Unregister first to replace."
    try:
        entry = await _to_thread(_open_engine, name, path, options)
    except Exception as e:
        return f"REGISTER FAILED ✗\n\n{e}"
    _engines[name] = entry
    advertised = sorted(entry.engine.options.keys())[:10]
    return (
        f"Registered {name!r} → {path}\n"
        f"Options applied: {entry.options or '(none)'}\n"
        f"Engine advertises {len(entry.engine.options)} options "
        f"(first 10: {advertised})"
    )


@mcp.tool()
async def unregister_engine(name: str) -> str:
    """Close and remove a registered engine."""
    entry = _engines.pop(name, None)
    if entry is None:
        return f"No engine named {name!r} is registered."
    await _to_thread(entry.close)
    return f"Unregistered {name!r}."


@mcp.tool()
async def list_engines() -> str:
    """Show registered engines."""
    if not _engines:
        return "No engines registered."
    lines = []
    for entry in _engines.values():
        lines.append(f"  {entry.name}: {entry.path}  options={entry.options or '(default)'}")
    return f"{len(_engines)} engine(s) registered:\n" + "\n".join(lines)


# ── Position handling (no engine required) ───────────────────────────────────

@mcp.tool()
async def parse_fen(fen: str) -> str:
    """
    Parse a FEN and return a human-readable summary: ASCII board, side to
    move, castling rights, en-passant square, halfmove/fullmove counters,
    and a legality check.
    """
    try:
        board = _parse_board(fen)
    except ValueError as e:
        return str(e)
    status = board.status()
    return (
        f"FEN: {board.fen()}\n\n"
        f"{board.unicode(borders=True)}\n\n"
        f"Side to move: {'white' if board.turn else 'black'}\n"
        f"Castling: {board.castling_xfen() or '-'}\n"
        f"En passant: {chess.square_name(board.ep_square) if board.ep_square else '-'}\n"
        f"Halfmove clock: {board.halfmove_clock}   Fullmove: {board.fullmove_number}\n"
        f"Status: {status.name if status == chess.STATUS_VALID else status!r}\n"
        f"Check? {board.is_check()}    Checkmate? {board.is_checkmate()}    "
        f"Stalemate? {board.is_stalemate()}"
    )


@mcp.tool()
async def legal_moves(fen: str) -> str:
    """List all legal moves from the given position, in UCI and SAN."""
    try:
        board = _parse_board(fen)
    except ValueError as e:
        return str(e)
    moves = list(board.legal_moves)
    if not moves:
        return f"No legal moves ({'mate' if board.is_checkmate() else 'stalemate'})."
    lines = [f"{len(moves)} legal moves:"]
    for m in moves:
        lines.append(f"  {m.uci():6}  {board.san(m)}")
    return "\n".join(lines)


@mcp.tool()
async def apply_moves(fen: str, moves: list[str]) -> str:
    """
    Apply a sequence of moves (UCI or SAN) to a position and return the
    resulting FEN. Errors out with the offending move if any is illegal.
    """
    try:
        board = _parse_board(fen)
    except ValueError as e:
        return str(e)
    for i, mv in enumerate(moves):
        try:
            move = board.parse_uci(mv)
        except ValueError:
            try:
                move = board.parse_san(mv)
            except ValueError as e:
                return f"Illegal/unparseable move at index {i}: {mv!r} ({e})"
        board.push(move)
    return f"Final FEN: {board.fen()}\nMoves applied: {len(moves)}\n\n{board.unicode(borders=True)}"


@mcp.tool()
async def pgn_to_fens(pgn: str) -> str:
    """
    Parse a PGN game string and return the FEN at every ply, plus headers
    and result.
    """
    game = chess.pgn.read_game(io.StringIO(pgn))
    if game is None:
        return "Could not parse PGN."
    board = game.board()
    fens = [board.fen()]
    moves_uci = []
    for move in game.mainline_moves():
        board.push(move)
        fens.append(board.fen())
        moves_uci.append(move.uci())
    headers = "\n".join(f"  {k}: {v}" for k, v in game.headers.items())
    return (
        f"Headers:\n{headers}\n\n"
        f"Result: {game.headers.get('Result', '*')}\n"
        f"Plies: {len(moves_uci)}\n\n"
        f"Move sequence (UCI):\n{' '.join(moves_uci)}\n\n"
        f"Final FEN: {fens[-1]}"
    )


# ── Perft ─────────────────────────────────────────────────────────────────────

def _perft(board: chess.Board, depth: int) -> int:
    if depth == 0:
        return 1
    nodes = 0
    for move in board.legal_moves:
        board.push(move)
        nodes += _perft(board, depth - 1)
        board.pop()
    return nodes


@mcp.tool()
async def perft(fen: str, depth: int) -> str:
    """
    Count leaf nodes at the given depth (move-generation correctness).

    Standard known values from the chessprogramming wiki — useful as
    test vectors for an engine under development:
        startpos depth 1: 20
        startpos depth 2: 400
        startpos depth 3: 8902
        startpos depth 4: 197281
        startpos depth 5: 4865609
        startpos depth 6: 119060324

    Args:
        fen: Position to count from.
        depth: Plies to search (start with 1-5; 6+ is slow in pure Python).
    """
    try:
        board = _parse_board(fen)
    except ValueError as e:
        return str(e)
    if depth < 0 or depth > 7:
        return f"depth must be 0–7 (pure-Python perft; was {depth})."
    # Per-move breakdown for small depths is the conventional 'divide' output.
    if depth >= 1:
        divides: list[tuple[str, int]] = []
        total = 0
        for move in board.legal_moves:
            board.push(move)
            n = await _to_thread(_perft, board, depth - 1)
            board.pop()
            divides.append((move.uci(), n))
            total += n
        lines = [f"perft({depth}) = {total}", "", "divide:"]
        for mv, n in sorted(divides):
            lines.append(f"  {mv}: {n}")
        return "\n".join(lines)
    return "perft(0) = 1"


# ── Analysis ──────────────────────────────────────────────────────────────────

def _format_score(score: chess.engine.PovScore, board: chess.Board) -> str:
    rel = score.white()
    if rel.is_mate():
        return f"#{rel.mate()}"
    return f"{rel.score() / 100.0:+.2f}"


@mcp.tool()
async def bestmove(
    engine: str,
    fen: str,
    depth: int = None,
    movetime_ms: int = None,
) -> str:
    """
    Ask an engine for its best move from the given position.

    Args:
        engine: Registered engine name.
        fen: Position FEN.
        depth: Search depth in plies (mutually exclusive with movetime_ms).
        movetime_ms: Search time budget in milliseconds.
    """
    try:
        board = _parse_board(fen)
        eng = _get_engine(engine)
    except (ValueError, KeyError, FileNotFoundError) as e:
        return str(e)
    limit = _build_limit(depth, movetime_ms)
    result = await _to_thread(eng.play, board, limit)
    move = result.move
    san = board.san(move) if move else "(none)"
    ponder = result.ponder.uci() if result.ponder else "-"
    return (
        f"engine={engine}  fen={fen}\n"
        f"limit: depth={depth} movetime_ms={movetime_ms}\n"
        f"bestmove: {move.uci() if move else '(none)'}  ({san})\n"
        f"ponder: {ponder}"
    )


@mcp.tool()
async def analyze(
    engine: str,
    fen: str,
    depth: int = None,
    movetime_ms: int = None,
    multipv: int = 1,
) -> str:
    """
    Run analysis on a position. Returns score, depth reached, and PV.
    Supports multipv for top-N lines.

    Args:
        engine: Registered engine name.
        fen: Position FEN.
        depth: Search depth in plies.
        movetime_ms: Search time budget in milliseconds.
        multipv: Number of principal variations to return (1 = best line only).
    """
    try:
        board = _parse_board(fen)
        eng = _get_engine(engine)
    except (ValueError, KeyError, FileNotFoundError) as e:
        return str(e)
    limit = _build_limit(depth, movetime_ms)
    info = await _to_thread(eng.analyse, board, limit, multipv=multipv if multipv > 1 else None)
    if multipv > 1 and isinstance(info, list):
        infos = info
    else:
        infos = [info if isinstance(info, dict) else info[0]]

    lines = [f"engine={engine}  fen={fen}", f"limit: depth={depth} movetime_ms={movetime_ms}  multipv={multipv}", ""]
    for i, inf in enumerate(infos, 1):
        score = inf.get("score")
        score_s = _format_score(score, board) if score else "?"
        d = inf.get("depth", "?")
        nodes = inf.get("nodes", "?")
        nps = inf.get("nps", "?")
        pv = inf.get("pv", [])
        pv_san: list[str] = []
        b = board.copy()
        for mv in pv:
            try:
                pv_san.append(b.san(mv))
                b.push(mv)
            except Exception:
                pv_san.append(mv.uci())
                break
        lines.append(
            f"  pv{i}: score={score_s}  depth={d}  nodes={nodes}  nps={nps}\n"
            f"        {' '.join(pv_san[:20])}"
        )
    return "\n".join(lines)


@mcp.tool()
async def compare_eval(
    fen: str,
    engines: list[str],
    depth: int = None,
    movetime_ms: int = None,
) -> str:
    """
    Run analyze() across multiple registered engines on the same position
    and present results side-by-side. Useful for spotting eval disagreements
    between an engine under test and a reference (Stockfish).
    """
    try:
        board = _parse_board(fen)
    except ValueError as e:
        return str(e)
    limit = _build_limit(depth, movetime_ms)
    rows = []
    for name in engines:
        try:
            eng = _get_engine(name)
        except KeyError as e:
            rows.append((name, f"<not registered>"))
            continue
        info = await _to_thread(eng.analyse, board, limit)
        score_s = _format_score(info["score"], board) if "score" in info else "?"
        d = info.get("depth", "?")
        pv = info.get("pv", [])
        pv0 = board.san(pv[0]) if pv else "(none)"
        rows.append((name, f"score={score_s}  depth={d}  bestmove={pv0}"))
    width = max(len(name) for name, _ in rows)
    out = [f"fen={fen}", f"limit: depth={depth} movetime_ms={movetime_ms}", ""]
    for name, info in rows:
        out.append(f"  {name.ljust(width)}  {info}")
    return "\n".join(out)


# ── fastchess: match + SPRT ───────────────────────────────────────────────────

_FASTCHESS_ELO = re.compile(
    r"Elo difference:\s*(?P<elo>[-+]?\d+\.\d+)\s*\+/-\s*(?P<err>\d+\.\d+)"
)
_FASTCHESS_SCORE = re.compile(
    r"Score of\s+\S+\s+vs\s+\S+:\s*(?P<w>\d+)\s*-\s*(?P<l>\d+)\s*-\s*(?P<d>\d+)"
)
_FASTCHESS_SPRT = re.compile(
    r"SPRT.*?(LLR|llr).*?(?P<llr>[-+]?\d+\.\d+).*?(?P<verdict>(H0 was accepted|H1 was accepted|continue))",
    re.IGNORECASE,
)


def _engine_path(name: str) -> str:
    if name not in _engines:
        raise KeyError(f"Engine {name!r} not registered.")
    return _engines[name].path


def _fastchess_cmd(
    engine_a: str, engine_b: str,
    n_games: int, time_control: str,
    opening_book: str | None,
    sprt: dict | None,
    concurrency: int,
) -> list[str]:
    path_a = _engine_path(engine_a)
    path_b = _engine_path(engine_b)
    cmd = [
        FASTCHESS_PATH,
        "-engine", f"cmd={path_a}", f"name={engine_a}",
        "-engine", f"cmd={path_b}", f"name={engine_b}",
        "-each", f"tc={time_control}",
        "-rounds", str(n_games),
        "-repeat",
        "-concurrency", str(concurrency),
        "-ratinginterval", "10",
    ]
    if opening_book:
        cmd += ["-openings", f"file={opening_book}", "format=pgn", "order=random"]
    if sprt:
        cmd += [
            "-sprt",
            f"elo0={sprt['elo0']}", f"elo1={sprt['elo1']}",
            f"alpha={sprt['alpha']}", f"beta={sprt['beta']}",
        ]
    return cmd


def _run_fastchess(cmd: list[str], timeout: int) -> tuple[bool, str]:
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=timeout,
    )
    return proc.returncode == 0, proc.stdout


def _summarise_fastchess(out: str) -> str:
    elo = _FASTCHESS_ELO.search(out)
    score = _FASTCHESS_SCORE.search(out)
    sprt = _FASTCHESS_SPRT.search(out)
    parts = []
    if score:
        parts.append(f"score: {score.group('w')}W - {score.group('l')}L - {score.group('d')}D")
    if elo:
        parts.append(f"Elo: {elo.group('elo')} +/- {elo.group('err')}")
    if sprt:
        parts.append(f"SPRT: LLR={sprt.group('llr')} verdict={sprt.group('verdict')}")
    return "  ".join(parts) if parts else "(no summary lines matched)"


@mcp.tool()
async def match(
    engine_a: str,
    engine_b: str,
    n_games: int = 100,
    time_control: str = "10+0.1",
    opening_book: str = None,
    concurrency: int = 4,
    timeout_s: int = 3600,
) -> str:
    """
    Run a fastchess head-to-head match between two registered engines.

    Args:
        engine_a, engine_b: Registered engine names.
        n_games: Number of games (use even numbers; -repeat alternates colours).
        time_control: fastchess TC string, e.g. '10+0.1' for 10s + 0.1s/move.
        opening_book: Absolute container path to a PGN opening book (optional).
                      Without one, all games start from the standard position
                      and noise dominates — recommended for any real test.
        concurrency: Parallel games. Match your CPU core count.
        timeout_s: Hard timeout for the entire match.
    """
    try:
        cmd = _fastchess_cmd(engine_a, engine_b, n_games, time_control, opening_book, None, concurrency)
    except KeyError as e:
        return str(e)
    try:
        ok, out = await _to_thread(_run_fastchess, cmd, timeout_s)
    except subprocess.TimeoutExpired:
        return f"MATCH TIMEOUT ✗ (>{timeout_s}s)"
    summary = _summarise_fastchess(out)
    header = "MATCH OK ✓" if ok else "MATCH ENDED WITH ERROR ✗"
    tail = out[-3000:]
    result = f"{header}\n{summary}\n\n--- fastchess output (tail) ---\n{tail}"
    _report("match", {"a": engine_a, "b": engine_b, "n": n_games, "tc": time_control}, result, ok)
    return result


@mcp.tool()
async def sprt(
    engine_a: str,
    engine_b: str,
    elo0: float = 0.0,
    elo1: float = 5.0,
    alpha: float = 0.05,
    beta: float = 0.05,
    time_control: str = "10+0.1",
    opening_book: str = None,
    concurrency: int = 4,
    max_games: int = 40000,
    timeout_s: int = 14400,
) -> str:
    """
    Run a Sequential Probability Ratio Test (SPRT) between two engines.

    The patch-acceptance methodology used upstream by Stockfish: keep
    playing until LLR crosses log(beta/(1-alpha)) (H0: <=elo0) or
    log((1-beta)/alpha) (H1: >=elo1). Defaults [0,5] alpha=beta=0.05 are
    the standard 'is this patch worth at least 5 Elo?' test.

    Args:
        elo0, elo1: Null and alternative Elo bounds.
        alpha, beta: Type-I and type-II error rates.
        max_games: Cap so the test cannot run forever if LLR oscillates.
    """
    try:
        cmd = _fastchess_cmd(
            engine_a, engine_b, max_games, time_control, opening_book,
            sprt={"elo0": elo0, "elo1": elo1, "alpha": alpha, "beta": beta},
            concurrency=concurrency,
        )
    except KeyError as e:
        return str(e)
    try:
        ok, out = await _to_thread(_run_fastchess, cmd, timeout_s)
    except subprocess.TimeoutExpired:
        return f"SPRT TIMEOUT ✗ (>{timeout_s}s)"
    summary = _summarise_fastchess(out)
    header = "SPRT OK ✓" if ok else "SPRT ENDED WITH ERROR ✗"
    tail = out[-3000:]
    result = (
        f"{header}\nelo bounds: [{elo0}, {elo1}]  alpha={alpha}  beta={beta}\n"
        f"{summary}\n\n--- fastchess output (tail) ---\n{tail}"
    )
    _report("sprt", {"a": engine_a, "b": engine_b, "elo0": elo0, "elo1": elo1}, result, ok)
    return result


# ── EPD tactics suite ─────────────────────────────────────────────────────────

@mcp.tool()
async def epd_test(
    engine: str,
    suite_path: str,
    time_per_pos_ms: int = 1000,
    max_positions: int = None,
) -> str:
    """
    Score an engine on an EPD tactics suite (WAC, STS, ERET, Arasan, etc.).

    Reads positions with `bm` (best move) operations; the engine 'passes'
    a position if its chosen move equals one of the bm moves.

    Args:
        suite_path: Container path to .epd file (typically under /opt/projects/...).
        time_per_pos_ms: Search time budget per position.
        max_positions: Optional cap for quick smoke-test runs.
    """
    try:
        eng = _get_engine(engine)
    except KeyError as e:
        return str(e)
    p = Path(suite_path)
    if not p.exists():
        return f"EPD file not found: {suite_path}"

    positions: list[tuple[chess.Board, list[chess.Move], dict]] = []
    with p.open() as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                board = chess.Board()
                ops = board.set_epd(line)
            except Exception:
                continue
            bm = ops.get("bm")
            if not bm:
                continue
            positions.append((board, bm, ops))

    if not positions:
        return f"No positions with bm operations found in {suite_path}"
    if max_positions:
        positions = positions[:max_positions]

    passed = 0
    failures: list[str] = []
    for i, (board, bm, ops) in enumerate(positions, 1):
        result = await _to_thread(
            eng.play, board, chess.engine.Limit(time=time_per_pos_ms / 1000.0)
        )
        chosen = result.move
        if chosen in bm:
            passed += 1
        else:
            ident = ops.get("id", f"pos{i}")
            wanted = ", ".join(board.san(m) for m in bm)
            got = board.san(chosen) if chosen else "(none)"
            failures.append(f"  {ident}: wanted [{wanted}], got {got}")

    pct = 100.0 * passed / len(positions)
    summary = (
        f"engine={engine}  suite={p.name}  "
        f"passed={passed}/{len(positions)} ({pct:.1f}%)  "
        f"time/pos={time_per_pos_ms}ms"
    )
    body = summary
    if failures and len(failures) <= 50:
        body += "\n\nFailures:\n" + "\n".join(failures)
    elif failures:
        body += f"\n\nFailures (first 50 of {len(failures)}):\n" + "\n".join(failures[:50])
    _report("epd_test", {"engine": engine, "suite": str(p)}, body, True)
    return body


# ── Auto-register Stockfish ───────────────────────────────────────────────────

def _autoregister_stockfish() -> None:
    if not STOCKFISH_PATH or not Path(STOCKFISH_PATH).exists():
        print(f"WARNING: Stockfish not found at {STOCKFISH_PATH}; skipping auto-register.", file=sys.stderr)
        return
    try:
        entry = _open_engine("stockfish", STOCKFISH_PATH, options=None)
        _engines["stockfish"] = entry
        print(f"Auto-registered stockfish → {STOCKFISH_PATH}")
    except Exception as e:
        print(f"WARNING: failed to auto-register Stockfish: {e}", file=sys.stderr)


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"PROJECTS_DIR={PROJECTS_DIR}")
    print(f"STOCKFISH_PATH={STOCKFISH_PATH}")
    print(f"FASTCHESS_PATH={FASTCHESS_PATH}")
    print(f"KNOWLEDGE_URL={_reporter.url}")
    _autoregister_stockfish()
    print("Starting chess-engine MCP on http://0.0.0.0:5180")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add chess-engine --transport http http://localhost:5180/mcp")
    print()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5180)
