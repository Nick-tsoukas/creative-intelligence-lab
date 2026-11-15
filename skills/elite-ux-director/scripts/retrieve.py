#!/usr/bin/env python3
"""Return only the named UX decision card, interaction pattern or homepage card.

Usage:
    python scripts/retrieve.py list [cards|patterns|homepages]
    python scripts/retrieve.py card C04
    python scripts/retrieve.py pattern P5
    python scripts/retrieve.py homepage H01

This script is read-only, uses stdlib, has no network, and prints only one
selected knowledge chunk to minimize Claude context. It is NOT retrieval AI.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {
    "card": (ROOT / "references/DECISION_CARDS.md", r"C\d{2}"),
    "pattern": (ROOT / "references/INTERACTION_PATTERNS.md", r"P\d+"),
    "homepage": (ROOT / "references/HOMEPAGE_INTELLIGENCE.md", r"H\d{2}"),
}


def sections(kind: str) -> dict[str, str]:
    file, id_pattern = SOURCES[kind]
    text = file.read_text(encoding="utf-8")
    headings = list(re.finditer(r"(?m)^## (" + id_pattern + r")\b[^\n]*", text))
    result = {}
    for i, match in enumerate(headings):
        start = match.start()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        part = text[start:end]
        # Stop before appendix notes not part of the numbered card.
        next_heading = re.search(r"(?m)^## (?!"+id_pattern+r"\b)", part[3:])
        if next_heading:
            part = part[:3 + next_heading.start()]
        result[match.group(1).upper()] = part.strip()
    return result


def main(argv: list[str]) -> int:
    if len(argv) == 1 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) > 1 else 2
    action = argv[1].lower()
    if action == "list":
        kinds = ["card", "pattern", "homepage"] if len(argv) < 3 else [
            {"cards": "card", "patterns": "pattern", "homepages": "homepage"}.get(argv[2], argv[2])
        ]
        if not all(k in SOURCES for k in kinds):
            print("Expected list cards, list patterns, or list homepages", file=sys.stderr)
            return 2
        for kind in kinds:
            for key, section in sections(kind).items():
                print(section.splitlines()[0])
        return 0
    if action not in SOURCES or len(argv) != 3:
        print("Expected card Cxx, pattern Px, or homepage Hxx (or list)", file=sys.stderr)
        return 2
    key = argv[2].upper()
    found = sections(action)
    if key not in found:
        print(f"Unknown {action} {key}. Available: {', '.join(found)}", file=sys.stderr)
        return 1
    print(found[key])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
