#!/usr/bin/env python3
"""Read-only, lightweight, source-aware Exceptional Interface Atlas search.

Usage:
 python scripts/query_interface_atlas.py list
 python scripts/query_interface_atlas.py search "media gallery"
 python scripts/query_interface_atlas.py show EI-002
 python scripts/query_interface_atlas.py compare EI-002 EI-008
 python scripts/query_interface_atlas.py targets "upload"

Only displays what was actually supported by observed preview images.
No remote calls, paid APIs, browser, or external dependencies.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "interface-atlas"
ALLOWED = re.compile(r"^EI-\d{3}$")
TERMS = re.compile(r"[a-z0-9]+")


def load(name: str, key: str):
    p = BASE / name
    data = json.loads(p.read_text(encoding="utf-8"))
    return data[key]


def cases():
    return load("observed-cases.json", "cases")


def targets():
    return load("research-targets.json", "targets")


def text_blob(r):
    fields = ["title", "creator", "kind", "observed", "mechanism", "risks",
              "original_exercise", "source_claim", "not_copy", "category"]
    return " ".join(str(r.get(k) or "") for k in fields).lower()


def rank(query, rows):
    tokens = [x for x in TERMS.findall(query.lower()) if len(x) > 2]
    if not tokens:
        return []
    result = []
    for row in rows:
        tags = " ".join(row.get("tags", [])).lower()
        title = row.get("title", "").lower()
        body = text_blob(row)
        score = sum(6 if t in tags else 4 if t in title else 1 if t in body else 0 for t in tokens)
        if score:
            result.append((score, row))
    return sorted(result, key=lambda pair: (-pair[0], pair[1]["id"]))


def short(row):
    return f'{row["id"]} | {row["title"]} | {row["status"]} | {row["source_url"]}'


def detail(row):
    return "\n".join([
        f'# {row["id"]} — {row["title"]}',
        f'**Evidence:** {row["status"]} · **Interactions:** {row["interaction_status"]}'
        f' · **Responsive live test:** {row["mobile_browser_status"]}',
        f'**Original work / owner:** {row["creator"]}',
        f'**Source:** {row["source_url"]}',
        f'**Image preview (external, source-linked only):** {row["preview_url"]}',
        f'**Image representation:** {row["preview_source"]}; {row["observation_limits"]}',
        f'\n## What the accessible pixels actually showed\n{row["observed"]}',
        f'\n## Transfer hypothesis\n{row["mechanism"]}',
        f'\n## Counterexamples and limitations\n{row["risks"]}',
        f'\n## Original design exercise\n{row["original_exercise"]}',
        f'\n## Do not copy\n{row["not_copy"]}',
        '\n**Reminder:** screenshot preview observation is not an interactive product'
        ' audit, accessibility test, current-app version check or evidence of improved conversions.'
    ])


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    query = sub.add_parser("search")
    query.add_argument("query", nargs="+")
    query.add_argument("--limit", type=int, default=6, choices=range(1, 13))
    show = sub.add_parser("show")
    show.add_argument("id")
    compare = sub.add_parser("compare")
    compare.add_argument("ids", nargs="+")
    queue = sub.add_parser("targets")
    queue.add_argument("query", nargs="*")
    args = p.parse_args(argv)

    if args.cmd == "list":
        for case in cases():
            print(short(case))
    elif args.cmd == "search":
        rows = rank(" ".join(args.query), cases())
        for _, c in rows[:args.limit]:
            print(f'{short(c)}\n  PRINCIPLE: {c["mechanism"]}\n  CAUTION: {c["risks"]}')
        if not rows:
            print("No inspected reference matches. Search queued targets, then inspect source before claiming a study.")
    elif args.cmd == "show":
        if not ALLOWED.fullmatch(args.id):
            p.error("Use a valid EI-### id")
        found = next((c for c in cases() if c["id"] == args.id), None)
        if not found:
            p.error("Unknown case ID")
        print(detail(found))
    elif args.cmd == "compare":
        if len(args.ids) < 2 or len(args.ids) > 3 or len(set(args.ids)) != len(args.ids):
            p.error("Compare 2 or 3 distinct case IDs")
        index = {r["id"]: r for r in cases()}
        if any(rid not in index for rid in args.ids):
            p.error("Unknown case ID")
        for case_id in args.ids:
            r = index[case_id]
            print(f'\n## {case_id} — {r["title"]}\nMECHANISM: {r["mechanism"]}\n'
                  f'RISK: {r["risks"]}\nORIGINAL EXERCISE: {r["original_exercise"]}')
        print("\nSYNTHESIS REQUIRED: What *different* problems do these works solve?"
              " Which mechanisms conflict? Do not imitate recognizable artwork or assume one wins.")
    else:
        selection = rank(" ".join(args.query), targets()) if args.query else [(0,r) for r in targets()]
        for _, t in selection[:15 if args.query else 60]:
            print(f'{t["id"]} | {t["category"]} | {t["title"]} | {t["status"]} | '
                  f'{t["url"]} | {t["case_id"] or "NO VISUAL STUDY"}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
