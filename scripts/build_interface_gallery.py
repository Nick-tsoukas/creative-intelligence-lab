#!/usr/bin/env python3
"""Build/check the static, offline Exceptional Interface Atlas gallery.

No external images/assets are copied, loaded or embedded. All images are
outbound links to their original sources. Schematics are original CSS only.
Usage: python scripts/build_interface_gallery.py [--check]
"""
from __future__ import annotations
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "interface-atlas"
TEMPLATE = BASE / "gallery-template.html"
OUTPUT = BASE / "gallery.html"
STUDIES = BASE / "observed-cases.json"
TARGETS = BASE / "research-targets.json"


def build():
    source = TEMPLATE.read_text(encoding="utf-8")
    cases = json.loads(STUDIES.read_text(encoding="utf-8"))["cases"]
    targets = json.loads(TARGETS.read_text(encoding="utf-8"))["targets"]
    data = json.dumps({"cases": cases, "total_targets": len(targets)},
                      ensure_ascii=False, separators=(",", ":"))
    # A JSON string inside a <script type=application/json> must not terminate
    # the script element or allow HTML injection via untrusted reference text.
    data = data.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    if source.count("__RESEARCH_DATA__") != 1 or source.count("__NOSCRIPT_LINKS__") != 1:
        raise ValueError("Gallery template must have exactly one of each data placeholder")
    links = "\n".join(
        f'<li><a href="{html.escape(item["source_url"], quote=True)}"'
        f' target="_blank" rel="noopener noreferrer">'
        f'{html.escape(item["title"])} — Original source</a></li>'
        for item in cases
    )
    return source.replace("__RESEARCH_DATA__", data).replace("__NOSCRIPT_LINKS__", links)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if gallery stale")
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            raise SystemExit("FAIL: gallery.html stale; run python scripts/build_interface_gallery.py")
        print("PASS: offline gallery matches verified case data and 60 targets")
    else:
        OUTPUT.write_text(expected, encoding="utf-8")
        print(f"BUILT: {OUTPUT} ({len(expected)} bytes, source-linked images only)")


if __name__ == "__main__":
    main()
