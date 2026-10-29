#!/usr/bin/env python3
"""Muse Global Research — RSS health check (stdlib only, no API key needed).

Usage:
    python3 scripts/check_feeds.py --config skills/muse-global-research/sources.yaml
    python3 scripts/check_feeds.py --config skills/muse-global-research/sources.yaml --format json
    python3 scripts/check_feeds.py --url https://news.ycombinator.com/rss --url https://techcrunch.com/feed/

What it checks, per feed, with ONE attempt (no retry loop):
  - HTTP status (429 / 403 / 404 are failures, not "try harder" signals)
  - Body is really XML/RSS/Atom, not an HTML security-check or error page
  - Item count and the newest item date, when present
  - A short sample of the newest titles (for a human to eyeball relevance)

Exit codes:
  0 = check completed (the report itself may list failures — read it)
  1 = script / argument error
  2 = every Tier A feed failed (the routine list is not usable this round)

Design note: this script proves a feed *can* be read. It does not prove a
claim in a report. Titles are signals; key numbers still need the source
article or official page, per SKILL.md.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

UA = "Muse-Global-Research-FeedCheck/1.0 (+https://github.com/CCD-AIGC/muse-global-research-skill)"


def parse_config(path):
    """Minimal parser for our sources.yaml shape: name/tier/url triples.

    It intentionally does not require PyYAML. Parameterised RSSHub routes
    (containing ':') and url_pattern entries are skipped: they need a real
    id substituted before they can be tested.
    """
    feeds = []
    name = tier = None
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read config: {exc}", file=sys.stderr)
        sys.exit(1)
    for line in text.splitlines():
        # Platform pages are not feeds; stop before that section.
        if line.startswith("platform_pages_not_rss:"):
            break
        m = re.search(r'^\s*-?\s*name:\s*"?(.*?)"?\s*$', line)
        if m:
            name = m.group(1).strip()
            continue
        m = re.search(r'^\s*tier:\s*([A-D])\s*$', line)
        if m:
            tier = m.group(1)
            continue
        m = re.search(r'^\s*url:\s*"?(https?://[^"\s]+)"?\s*$', line)
        if m and name:
            url = m.group(1)
            if ":" in url.split("://", 1)[1].split("/")[0]:
                continue
            feeds.append({"name": name, "tier": tier or "?", "url": url})
            name = None
    return feeds


def check_one(feed):
    req = urllib.request.Request(feed["url"], headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            body = resp.read(2_000_000)
    except urllib.error.HTTPError as exc:
        return {**feed, "ok": False, "status": exc.code,
                "reason": f"HTTP {exc.code} — stop at this source, use its fallback in sources.yaml"}
    except Exception as exc:  # timeout, DNS, TLS, connection reset, etc.
        return {**feed, "ok": False, "status": None,
                "reason": f"{type(exc).__name__}: {exc}"}
    stripped = body.lstrip()
    if not (stripped.startswith(b"<?xml") or stripped.startswith(b"<rss")
            or stripped.startswith(b"<feed") or stripped.startswith(b"<rdf")):
        snippet = stripped[:120].decode("utf-8", "replace")
        return {**feed, "ok": False, "status": status,
                "reason": f"Not XML (likely HTML / security-check / error page). Starts with: {snippet!r}"}
    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        return {**feed, "ok": False, "status": status, "reason": f"XML parse failed: {exc}"}
    items = []
    for el in root.iter():
        tag = el.tag.rsplit("}", 1)[-1]
        if tag in ("item", "entry"):
            title = ""
            date = ""
            for child in el:
                ctag = child.tag.rsplit("}", 1)[-1]
                if ctag == "title" and child.text:
                    title = " ".join(child.text.split())
                if ctag in ("pubDate", "published", "updated") and child.text:
                    date = child.text.strip()
            items.append({"title": title, "date": date})
    newest = ""
    for it in items:
        if not it["date"]:
            continue
        try:
            dt = parsedate_to_datetime(it["date"])
            if dt and (not newest or dt > parsedate_to_datetime(newest)):
                newest = it["date"]
        except Exception:
            if not newest:
                newest = it["date"]
    return {**feed, "ok": True, "status": status, "items": len(items),
            "newest": newest, "sample_titles": [i["title"] for i in items[:3]]}


def main():
    ap = argparse.ArgumentParser(description="Check RSS feeds from sources.yaml or --url list.")
    ap.add_argument("--config", default=None)
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--format", choices=["md", "json"], default="md")
    args = ap.parse_args()
    feeds = []
    if args.config:
        feeds = parse_config(args.config)
    for url in args.url:
        feeds.append({"name": url, "tier": "?", "url": url})
    if not feeds:
        ap.error("no feeds: pass --config or --url")
    results = [check_one(f) for f in feeds]
    if args.format == "json":
        print(json.dumps({"checked_at_utc": datetime.now(timezone.utc).isoformat(),
                          "results": results}, ensure_ascii=False, indent=2))
    else:
        print(f"# Feed check — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
        print("| Feed | Tier | Status | Items | Newest item | Result |")
        print("|---|---|---|---|---|---|")
        for r in results:
            if r["ok"]:
                print(f"| {r['name']} | {r['tier']} | {r['status']} | {r.get('items', 0)} | {r.get('newest','')} | OK |")
            else:
                print(f"| {r['name']} | {r['tier']} | {r.get('status','-')} | - | - | FAIL: {r['reason']} |")
        print("\n## Sample titles (OK feeds only)\n")
        for r in results:
            if r["ok"]:
                for t in r.get("sample_titles", []):
                    print(f"- [{r['name']}] {t}")
    tier_a = [r for r in results if r["tier"] == "A"]
    if tier_a and not any(r["ok"] for r in tier_a):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
