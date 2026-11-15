#!/usr/bin/env python3
"""Read exactly one selected UX knowledge card/pattern from a bounded local corpus.

Usage (from the installed elite-ux-director directory):
    python scripts/retrieve.py list [cards|patterns|homepages|knowledge]
    python scripts/retrieve.py card C04
    python scripts/retrieve.py pattern P5
    python scripts/retrieve.py homepage H01
    python scripts/retrieve.py knowledge K03
    python scripts/retrieve.py search "visual hierarchy"

Read-only. Python standard library, no network, embedding or model calls.
Search only suggests IDs; it does NOT read or output a whole book.
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
    "knowledge": (ROOT / "references/KNOWLEDGE_CARDS.md", r"K\d{2}"),
}
ALIASES = {
    "cards": "card", "patterns": "pattern",
    "homepages": "homepage", "knowledge": "knowledge"
}


def sections(kind: str) -> dict[str, str]:
    """Return ordered, self-contained ## ID sections; fail for missing files."""
    path, id_pattern = SOURCES[kind]
    source = path.read_text(encoding="utf-8")
    headers = list(re.finditer(r"(?m)^## (" + id_pattern + r")\b[^\n]*", source))
    result = {}
    for i, match in enumerate(headers):
        end = headers[i + 1].start() if i + 1 < len(headers) else len(source)
        chunk = source[match.start():end]
        # The final numbered card may be followed by a non-card appendix.
        appendix = re.search(r"(?m)^## (?!"+id_pattern+r"\b)[^\n]+", chunk[3:])
        if appendix:
            chunk = chunk[:3 + appendix.start()]
        key = match.group(1).upper()
        if key in result:
            raise ValueError("Duplicate knowledge/card ID: " + key)
        result[key] = chunk.strip()
    return result


def search_words(query: str, limit: int = 6) -> list[tuple[int, str, str, str]]:
    """Deterministically rank a few IDs by title/tags plus body match, never full text."""
    tokens = [t for t in re.findall(r"[a-z0-9]+", query.lower()) if len(t) > 2]
    if not tokens:
        return []
    out = []
    for kind in SOURCES:
        for key, part in sections(kind).items():
            head = "\n".join(part.splitlines()[:3]).lower()
            body = part.lower()
            score = sum(4 if word in head else 1 if word in body else 0 for word in tokens)
            if score:
                title = part.splitlines()[0].removeprefix("## ")
                out.append((score, kind, key, title))
    return sorted(out, key=lambda v: (-v[0], v[1], v[2]))[:limit]


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) > 1 else 2
    action = ALIASES.get(argv[1].lower(), argv[1].lower())
    if action == "list":
        if len(argv) > 3:
            print("Expected list [cards|patterns|homepages|knowledge]", file=sys.stderr)
            return 2
        kinds = [ALIASES.get(argv[2].lower(), argv[2].lower())] if len(argv) == 3 else list(SOURCES)
        if any(kind not in SOURCES for kind in kinds):
            print("Unknown list category", file=sys.stderr)
            return 2
        for kind in kinds:
            for value in sections(kind).values():
                print(value.splitlines()[0])
        return 0
    if action == "search":
        if len(argv) < 3:
            print("Expected a quoted search phrase", file=sys.stderr)
            return 2
        for score, kind, key, title in search_words(" ".join(argv[2:])):
            print(f"{kind} {key} | {title} | rank={score}")
        return 0
    if action not in SOURCES or len(argv) != 3:
        print("Expected card Cxx, pattern Px, homepage Hxx or knowledge Kxx", file=sys.stderr)
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
