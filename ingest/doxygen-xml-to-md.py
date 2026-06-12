#!/usr/bin/env python3
"""
Convert Doxygen XML output into one markdown file per class / namespace / file,
sized for ChromaDB chunking. Reads from ../knowledge/.doxygen-out/xml/, writes
to ../docs/ue4ss-cpp-api/.

The XML schema we care about:

  index.xml                lists every compound (class/struct/namespace/file)
  <refid>.xml              one file per compound with its members + brief docs

For each compound we emit:

    # <Compound::Name>
    Source: <path>
    Kind: class | struct | namespace | file
    <brief description, if any>
    <detailed description, if any>

    ## Members
    ### <return-type> <name>(<params>) <const?> <override?>
    <brief if any>
    <detail if any>
    ...

This is intentionally minimal — we're optimising for RAG retrieval, not for
human browsing. The embedding model picks up symbol names + nearby comments;
we don't need styled tables or cross-links.
"""

from __future__ import annotations

import sys
import re
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable


def text_of(element: ET.Element | None) -> str:
    """Recursively flatten an element's text content."""
    if element is None:
        return ""
    parts: list[str] = []
    if element.text:
        parts.append(element.text)
    for child in element:
        parts.append(text_of(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def collapse(s: str) -> str:
    """Collapse runs of whitespace to single spaces, strip."""
    return re.sub(r"\s+", " ", s).strip()


def sanitize_filename(name: str) -> str:
    """Turn a Doxygen compound name into a safe filename."""
    safe = re.sub(r"[^\w\-]", "_", name)
    return safe[:200] or "_"


def describe(element: ET.Element) -> tuple[str, str]:
    """Return (brief, detailed) text for a Doxygen-described element."""
    brief = collapse(text_of(element.find("briefdescription")))
    detail = collapse(text_of(element.find("detaileddescription")))
    return brief, detail


def render_member(member: ET.Element) -> str:
    """Render one member (function/variable/enum/typedef) as a markdown block."""
    kind = member.get("kind", "")
    name = collapse(text_of(member.find("name")))
    rtype = collapse(text_of(member.find("type")))
    argstring = collapse(text_of(member.find("argsstring")))

    # Header line: `### returnType Name(args)` for functions, `### kind Name` otherwise.
    if kind == "function":
        sig_parts = [p for p in (rtype, name + argstring) if p]
        header = " ".join(sig_parts)
    elif kind in ("variable", "typedef"):
        header = f"{kind} {rtype} {name}".strip()
    elif kind == "enum":
        header = f"enum {name}"
    elif kind == "define":
        header = f"#define {name}"
    elif kind in ("friend",):
        return ""  # noise
    else:
        header = f"{kind} {name}".strip()

    brief, detail = describe(member)

    lines: list[str] = [f"### {header}"]
    if brief:
        lines.append(brief)
    if detail and detail != brief:
        lines.append(detail)

    # Enum values inline.
    if kind == "enum":
        values: list[str] = []
        for ev in member.findall("enumvalue"):
            ev_name = collapse(text_of(ev.find("name")))
            ev_init = collapse(text_of(ev.find("initializer")))
            ev_brief = collapse(text_of(ev.find("briefdescription")))
            line = f"- `{ev_name}`"
            if ev_init:
                line += f" {ev_init}"
            if ev_brief:
                line += f" — {ev_brief}"
            values.append(line)
        if values:
            lines.append("")
            lines.extend(values)

    return "\n".join(lines)


def render_compound(compound_xml: Path) -> tuple[str, str] | None:
    """Read one compound XML file, return (filename, markdown) or None to skip."""
    try:
        tree = ET.parse(compound_xml)
    except ET.ParseError:
        return None

    root = tree.getroot()
    compound = root.find("compounddef")
    if compound is None:
        return None

    kind = compound.get("kind", "")
    # Skip noise compound kinds: dir entries, pages.
    if kind not in ("class", "struct", "namespace", "file"):
        return None

    name = collapse(text_of(compound.find("compoundname")))
    if not name:
        return None

    location = compound.find("location")
    source_path = location.get("file") if location is not None else ""
    brief, detail = describe(compound)

    lines: list[str] = [f"# {name}", ""]
    if source_path:
        lines.append(f"Source: `{source_path}`")
    lines.append(f"Kind: {kind}")
    lines.append("")
    if brief:
        lines.append(brief)
        lines.append("")
    if detail and detail != brief:
        lines.append(detail)
        lines.append("")

    # Members are grouped by sectiondef (public-func, public-attrib, ...).
    rendered_members: list[str] = []
    for section in compound.findall("sectiondef"):
        section_kind = section.get("kind", "")
        # Skip private/protected sections — public API only.
        if "private" in section_kind or "protected" in section_kind:
            continue
        for member in section.findall("memberdef"):
            block = render_member(member)
            if block:
                rendered_members.append(block)

    if rendered_members:
        lines.append("## Members")
        lines.append("")
        lines.extend(rendered_members)

    filename = f"{kind}_{sanitize_filename(name)}.md"
    return filename, "\n".join(lines).rstrip() + "\n"


def iter_compound_xmls(xml_dir: Path) -> Iterable[Path]:
    """Yield every compound XML file (skipping index.xml and Doxygen-internal files)."""
    for path in sorted(xml_dir.glob("*.xml")):
        if path.name in ("index.xml", "Doxyfile.xml"):
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--xml-dir",
        required=True,
        type=Path,
        help="Doxygen XML output dir (contains index.xml + per-compound .xml files)",
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        type=Path,
        help="Where to write the generated .md files (will be cleared first)",
    )
    args = parser.parse_args()

    if not args.xml_dir.is_dir():
        print(f"ERROR: xml-dir does not exist: {args.xml_dir}", file=sys.stderr)
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for stale in args.out_dir.glob("*.md"):
        stale.unlink()

    n_written = 0
    n_skipped = 0
    for compound_xml in iter_compound_xmls(args.xml_dir):
        result = render_compound(compound_xml)
        if result is None:
            n_skipped += 1
            continue
        filename, content = result
        (args.out_dir / filename).write_text(content, encoding="utf-8")
        n_written += 1

    print(f"Wrote {n_written} markdown files to {args.out_dir} ({n_skipped} skipped).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
