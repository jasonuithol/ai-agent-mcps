#!/usr/bin/env python3
"""
Cache chessprogramming.org wiki pages as markdown under
~/Projects/mcp-chess/docs/chessprogramming/.

MediaWiki API workflow:
  1. ?action=query&list=allpages&apnamespace=0  — enumerate content pages
  2. ?action=parse&page=<title>&prop=text       — render HTML
  3. markdownify(HTML)                          — to markdown
  4. write to disk with the page URL in a header

Idempotent: skips pages that already have a cached file. Pass --refresh
to force re-download. Pass --limit N to stop after N fetches (useful for
smoke-testing the pipeline). Crawl rate is throttled to ~1 req/s out of
politeness; full crawl is multi-thousand pages and takes ~30-60 min.

After this completes, run knowledge/seed.sh to index the cache into the
mcp-chess knowledge base.
"""
import argparse
import re
import sys
import time
from pathlib import Path

import requests
from markdownify import markdownify

API = "https://www.chessprogramming.org/api.php"
SITE = "https://www.chessprogramming.org"
USER_AGENT = (
    "mcp-chess-ingest/0.1 "
    "(https://github.com/jasonuithol/mcp-chess; "
    "chess knowledge base for personal MCP RAG)"
)
THROTTLE_SEC = 1.0
NAMESPACE_MAIN = 0
APLIMIT = 500


def sanitize_filename(title: str) -> str:
    s = title.replace(" ", "_")
    s = re.sub(r"[^\w.\-_]", "_", s, flags=re.UNICODE)
    return s[:200]


def list_all_pages(session, limit):
    apcontinue = None
    yielded = 0
    while True:
        params = {
            "action": "query",
            "list": "allpages",
            "apnamespace": NAMESPACE_MAIN,
            "aplimit": APLIMIT,
            "format": "json",
            "maxlag": 5,
        }
        if apcontinue:
            params["apcontinue"] = apcontinue
        r = session.get(API, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        for p in data.get("query", {}).get("allpages", []):
            yield p["title"]
            yielded += 1
            if limit and yielded >= limit:
                return
        cont = data.get("continue", {})
        if "apcontinue" in cont:
            apcontinue = cont["apcontinue"]
            time.sleep(THROTTLE_SEC)
        else:
            return


def fetch_page_html(session, title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",
        "format": "json",
        "maxlag": 5,
        "disableeditsection": 1,
        "disabletoc": 1,
    }
    r = session.get(API, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()
    if "error" in data:
        return None
    return data.get("parse", {}).get("text", {}).get("*")


def html_to_markdown(html):
    md = markdownify(html, heading_style="ATX", bullets="-")
    md = re.sub(r"\[\s*edit\s*\]", "", md, flags=re.IGNORECASE)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=Path.home() / "Projects/mcp-chess/docs/chessprogramming")
    ap.add_argument("--limit", type=int, help="Stop after N fetches (smoke test)")
    ap.add_argument("--refresh", action="store_true", help="Re-fetch cached pages")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    fetched = skipped = errors = 0
    print(f"Caching to {args.out}")
    for title in list_all_pages(session, limit=args.limit):
        fname = sanitize_filename(title) + ".md"
        path = args.out / fname
        if path.exists() and not args.refresh:
            skipped += 1
            continue
        try:
            html = fetch_page_html(session, title)
            if not html:
                print(f"  empty: {title}", file=sys.stderr)
                errors += 1
                time.sleep(THROTTLE_SEC)
                continue
            md = html_to_markdown(html)
            url = f"{SITE}/{title.replace(' ', '_')}"
            header = f"# {title}\n\nSource: {url}\n\n"
            path.write_text(header + md, encoding="utf-8")
            fetched += 1
            if fetched % 10 == 0:
                print(f"  fetched {fetched} (skipped {skipped}, errors {errors})", flush=True)
        except requests.exceptions.RequestException as e:
            print(f"  ERROR fetching {title}: {e}", file=sys.stderr)
            errors += 1
        time.sleep(THROTTLE_SEC)

    print(f"\nDone. fetched={fetched} skipped={skipped} errors={errors} dest={args.out}")


if __name__ == "__main__":
    main()
