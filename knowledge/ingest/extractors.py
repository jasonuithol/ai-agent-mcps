"""Lightweight C# / .NET text extractors.

No Roslyn — heuristic regex. Good enough for retrieval; the embedding
model forgives noise. Mirrors the shape of mcp-c/knowledge/ingest/extractors.py
so router/chunker code reads identically across siblings.
"""

from __future__ import annotations

import re
from pathlib import Path

# ── Pattern tags ──────────────────────────────────────────────────────────────
#
# (regex, tag). Tags are auto-detected by scanning chunk bodies; provenance
# tags (project name, source type) are added separately by the chunker.

PATTERN_TAGS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\busing\s+System\.Threading\.Tasks\b"),       "async"),
    (re.compile(r"\basync\s+Task\b"),                            "async"),
    (re.compile(r"\bawait\s+"),                                  "async"),
    (re.compile(r"\bIDisposable\b"),                             "disposable"),
    (re.compile(r"\bIEnumerable<"),                              "linq"),
    (re.compile(r"\busing\s+System\.Linq\b"),                    "linq"),
    (re.compile(r"\bSystem\.IO\b"),                              "io"),
    (re.compile(r"\bSystem\.Net\."),                             "net"),
    (re.compile(r"\bSystem\.Reflection\b"),                      "reflection"),
    (re.compile(r"\bxunit\b", re.IGNORECASE),                    "xunit"),
    (re.compile(r"\[Fact\]|\[Theory\]"),                         "xunit"),
    (re.compile(r"\bNUnit\b"),                                   "nunit"),
    (re.compile(r"\[TestMethod\]|MSTest"),                       "mstest"),
    (re.compile(r"\bBepInEx\b"),                                 "bepinex"),
    (re.compile(r"\bHarmonyLib\b|\[HarmonyPatch"),               "harmony"),
    (re.compile(r"\bUnityEngine\b"),                             "unity"),
    (re.compile(r"\bMicrosoft\.Extensions\.DependencyInjection"), "di"),
    (re.compile(r"\bMicrosoft\.AspNetCore\b"),                   "aspnet"),
]


def detect_tags(text: str) -> list[str]:
    """Return content-derived tags for the given chunk body."""
    out: list[str] = []
    seen: set[str] = set()
    for pat, tag in PATTERN_TAGS:
        if tag in seen:
            continue
        if pat.search(text):
            out.append(tag)
            seen.add(tag)
    return out


# ── Top-level node extraction ─────────────────────────────────────────────────
#
# We grab top-level type declarations (class / struct / interface / record /
# enum) and method-like members within them. Braces are walked naïvely — this
# can over-extend a chunk if a string literal contains a stray `{`, which is
# rare and the embedding query is robust to it.

_TYPE_DECL_RE = re.compile(
    r"""
    ^\s*
    (?:\[[^\]]*\]\s*)*                              # attributes
    (?:public|internal|private|protected|static|sealed|abstract|partial|readonly|ref|\s)*
    \b(?P<kind>class|struct|interface|record|enum)\b
    \s+
    (?P<name>[A-Za-z_][A-Za-z0-9_]*)
    """,
    re.MULTILINE | re.VERBOSE,
)

_METHOD_DECL_RE = re.compile(
    r"""
    ^\s*
    (?:\[[^\]]*\]\s*)*
    (?:public|internal|private|protected|static|virtual|override|async|sealed|abstract|extern|partial|new|\s)+
    [A-Za-z_][\w<>?,\s\[\]\.]*?\s+                  # return type (loose)
    (?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*
    \([^;{}]*\)\s*                                  # parameter list (one line)
    (?:where[^{;]*)?                                # optional generic constraint
    \{                                              # opening brace = method body
    """,
    re.MULTILINE | re.VERBOSE,
)


def _find_balanced_brace_end(src: str, start: int) -> int:
    """Given the index of an opening '{', return index of its matching '}'.

    Naïve walk — does not respect strings or comments. Returns len(src)
    if unbalanced (over-extends rather than missing the node entirely).
    """
    depth = 0
    i = start
    while i < len(src):
        c = src[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return len(src)


def extract_top_level_nodes(src: str) -> list[dict]:
    """Extract type and method declarations as {kind, name, text} dicts.

    Each method node carries its enclosing type's name (best-effort) in
    a `class_name` field. Type nodes have empty `class_name`.
    """
    nodes: list[dict] = []

    # Types first — find each declaration's opening brace and its body span.
    type_spans: list[tuple[int, int, str]] = []   # (start, end, name)
    for m in _TYPE_DECL_RE.finditer(src):
        brace = src.find("{", m.end())
        if brace < 0:
            continue
        end = _find_balanced_brace_end(src, brace)
        nodes.append({
            "kind": m.group("kind"),
            "name": m.group("name"),
            "class_name": "",
            "func_name": "",
            "text": src[m.start():end],
        })
        type_spans.append((m.start(), end, m.group("name")))

    # Methods — pin each to its enclosing type by span.
    for m in _METHOD_DECL_RE.finditer(src):
        brace = m.end() - 1   # the '{' is included in the pattern
        end = _find_balanced_brace_end(src, brace)
        enclosing = ""
        for ts, te, tn in type_spans:
            if ts <= m.start() <= te:
                enclosing = tn
                break
        nodes.append({
            "kind": "method",
            "name": m.group("name"),
            "class_name": enclosing,
            "func_name": m.group("name"),
            "text": src[m.start():end],
        })

    return nodes


def extract_module_name(file_path: str, project_root: str) -> str:
    """Module name from path: 'src/Foo/Bar.cs' → 'src.Foo.Bar'."""
    p = Path(file_path)
    root = Path(project_root)
    try:
        rel = p.relative_to(root)
    except ValueError:
        rel = p
    parts = list(rel.with_suffix("").parts)
    return ".".join(parts)
