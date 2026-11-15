#!/usr/bin/env python3
"""Low-memory, read-only source reconciliation for Elite UX book research.

Compares the 2026-11-15 user manifest with the historical Lab book catalog.
Never claims a candidate was acquired, studied or licensed; never auto-merges
different editions. Standard-library only; no network, APIs or model calls.

Usage: python scripts/reconcile_ux_book_canon.py [--json]
"""
from __future__ import annotations

import csv
import difflib
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources/intake/2026-11-15/ELITE_UX_DESIGN_SOURCE_MANIFEST.csv"
LEGACY = ROOT / "sources/UX_DESIGN_BOOK_CATALOG_2026-11-15.md"


def title_key(title: str) -> str:
    value = unicodedata.normalize("NFKD", title)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = value.casefold().replace("&", "and")
    value = re.sub(r"\([^)]*(?:edition|ed\.|\d{4})[^)]*\)", " ", value)
    value = re.sub(r"\b(?:first|second|third|fourth|fifth|sixth|2nd|3rd|4th|5th|6th)\s+ed(?:ition)?\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def title_variants(title: str) -> set[str]:
    raw = title.strip()
    variants = {title_key(raw)}
    # Subtitle may contain useful bibliographic disambiguation; matches on
    # the short title remain proposals, not authority to collapse editions.
    if ":" in raw:
        variants.add(title_key(raw.split(":", 1)[0]))
    return {x for x in variants if x}


def legacy_books(text: str) -> list[dict[str, str]]:
    result = []
    for line in text.splitlines():
        match = re.match(r"^\|\s*((?:V\d{2})|(?:C\d{3}))\s*\|\s*([^|]+)\s*\|\s*([^|]+)\|", line)
        if match:
            result.append({"id": match.group(1), "title": match.group(2).strip(), "author": match.group(3).strip()})
    return result


def reconcile() -> dict:
    legacy = legacy_books(LEGACY.read_text(encoding="utf-8"))
    with MANIFEST.open(encoding="utf-8-sig", newline="") as stream:
        incoming = list(csv.DictReader(stream))
    books = [row for row in incoming if row.get("type", "").strip().lower() == "book"]
    other = [row for row in incoming if row.get("type", "").strip().lower() != "book"]
    matches = {"title_match_review_edition": [], "possible_match_manual_review": [], "no_title_match_manual_review": []}
    for item in books:
        title = item.get("title", "").strip()
        variations = title_variants(title)
        exact = [x for x in legacy if variations & title_variants(x["title"])]
        # Similarity never establishes a match. Require a strong title match
        # and keep all uncertain results for human review.
        near = sorted(
            ((difflib.SequenceMatcher(None, title_key(title), title_key(x["title"])).ratio(), x)
             for x in legacy if x not in exact),
            key=lambda pair: -pair[0],
        )
        if exact:
            key = "title_match_review_edition"
            options = exact[:5]
        elif near and near[0][0] >= .76:
            key = "possible_match_manual_review"
            options = [x for similarity, x in near[:3] if similarity >= .76]
        else:
            key = "no_title_match_manual_review"
            options = []
        matches[key].append({
            "incoming_id": item.get("id", ""), "title": title,
            "source_access_label": item.get("access", ""),
            "study_status": item.get("study_status", ""),
            "legacy_candidates": options,
        })
    return {
        "legacy_catalog_book_entries": len(legacy),
        "incoming_manifest_rows": len(incoming),
        "incoming_books": len(books),
        "incoming_other_resources": len(other),
        "incoming_study_statuses": dict(sorted({x.get("study_status", ""): sum(v.get("study_status", "") == x.get("study_status", "") for v in incoming) for x in incoming}.items())),
        "groups": matches,
        "warning": "Title/author candidate matching only. No edition merged, no acquisition verified, no book reading implied. Ambiguous matches need manual review.",
    }


def main(argv: list[str]) -> int:
    data = reconcile()
    if "--json" in argv:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    print(f"Legacy catalog entries: {data['legacy_catalog_book_entries']}")
    print(f"Incoming: {data['incoming_books']} books + {data['incoming_other_resources']} other sources")
    for group, entries in data["groups"].items():
        print(f"{group}: {len(entries)}")
        for item in entries:
            ids = ",".join(x["id"] for x in item["legacy_candidates"])
            print(f"  {item['incoming_id']}: {item['title']} (candidate matches: {ids or 'none'})")
    print(data["warning"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
