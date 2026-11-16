#!/usr/bin/env python3
"""Query the source-grounded Masterpiece Atlas without loading the whole library.

Usage:
  python scripts/query_masterpiece_atlas.py list
  python scripts/query_masterpiece_atlas.py search "light"
  python scripts/query_masterpiece_atlas.py show MA-001

No network, embeddings, subprocesses, external packages or file writes.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "visual-library" / "masterpiece-atlas"
INDEX = ATLAS / "index.json"


def load() -> list[dict]:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    return data["entries"]


def find(item_id: str) -> dict | None:
    return next((x for x in load() if x["id"].upper() == item_id.upper()), None)


def search(query: str) -> list[tuple[int, dict]]:
    tokens = [t for t in re.findall(r"[a-z0-9]+", query.lower()) if len(t) > 2]
    if not tokens:
        return []
    ranked = []
    for entry in load():
        fields = " ".join((entry["creator"], entry["title"], entry["discipline"], entry["mechanism"])).lower()
        tags = " ".join(entry["tags"]).lower()
        points = sum((5 if t in tags else 2 if t in fields else 0) for t in tokens)
        if points:
            ranked.append((points, entry))
    return sorted(ranked, key=lambda x: (-x[0], x[1]["id"]))[:6]


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("--help", "-h"):
        print(__doc__)
        return 0 if len(argv) > 1 else 2
    command = argv[1].lower()
    if command == "list" and len(argv) == 2:
        for e in load():
            print(f'{e["id"]} | {e["creator"]} — {e["title"]} | {e["discipline"]}')
        return 0
    if command == "search" and len(argv) >= 3:
        for score, e in search(" ".join(argv[2:])):
            print(f'{e["id"]} | {e["title"]} | {e["mechanism"]}')
        return 0
    if command == "show" and len(argv) == 3:
        e = find(argv[2])
        if e is None:
            print("Unknown Atlas ID; use list", file=sys.stderr)
            return 1
        # Paths are provenance-reviewed and checked by static CI. Enforce
        # containment anyway to reject future unsafe records.
        file = (ATLAS / e["study"]).resolve()
        if ATLAS.resolve() not in file.parents or not file.is_file():
            print("Invalid or missing study path", file=sys.stderr)
            return 1
        print(file.read_text(encoding="utf-8"))
        return 0
    print("Expected list, search <phrase>, or show MA-XXX", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
