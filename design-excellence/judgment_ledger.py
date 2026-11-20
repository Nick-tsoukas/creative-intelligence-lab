#!/usr/bin/env python3
"""Private, append-only design feedback ledger (stdlib only, zero model/API calls).

This is a record-keeping tool, NOT an aesthetic evaluator or a trained taste model.
All records are explicit user/agent-entered statements with evidence labels.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
DECISIONS = ("APPROVE", "REVISE", "REJECT")
AXES = ("COMPOSITION", "SPACE", "TYPOGRAPHY", "IMAGERY", "MOTION", "IDENTITY", "TASK_CLARITY", "CRAFT", "OTHER")
EVIDENCE = ("OWNER_FEEDBACK", "IMAGE_OBSERVED", "FLOW_TESTED", "RESEARCH_HYPOTHESIS")
MAX_TEXT = 1000
REQUIRED = {"schema", "id", "project", "candidate", "decision", "axis", "observation", "because", "next_move", "evidence", "created_at", "source", "context", "supersedes"}
DEFAULT_ROOT = Path(__file__).resolve().parent.parent / ".cil-private" / "creative-judgment"


def slug(value: str, name: str = "identifier") -> str:
    if not SLUG.fullmatch(value):
        raise ValueError(f"Invalid {name}: use 1-64 lowercase letters, digits, _ or -")
    return value


def bounded(value: str, name: str, required: bool = False) -> str:
    value = value.strip()
    if (required and not value) or len(value) > MAX_TEXT or "\x00" in value:
        raise ValueError(f"Invalid {name}: {'nonempty, ' if required else ''}at most {MAX_TEXT} characters")
    return value


def record_directory(root: Path, project: str) -> Path:
    return root / slug(project, "project") / "records"


def read_records(root: Path, project: str) -> list[dict]:
    directory = record_directory(root, project)
    if not directory.exists():
        return []
    if directory.is_symlink():
        raise ValueError("Refusing symlinked records directory")
    result = []
    for path in sorted(directory.glob("*.json")):
        if path.is_symlink() or path.stat().st_size > 65536:
            raise ValueError(f"Unsafe record: {path.name}")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"Unreadable record: {path.name}: {exc}") from exc
        validate_record(data, project, path.stem)
        result.append(data)
    ids = {r["id"] for r in result}
    for r in result:
        if r["supersedes"] and (r["supersedes"] not in ids or r["supersedes"] == r["id"]):
            raise ValueError(f"Unresolvable supersedes in {r['id']}")
    # Detect cycles as well as direct self-supersession.
    parents = {r["id"]: r["supersedes"] for r in result}
    for starting in ids:
        visited = set()
        node = starting
        while node:
            if node in visited:
                raise ValueError(f"Supersession cycle involving {starting}")
            visited.add(node)
            node = parents.get(node)
    return sorted(result, key=lambda r: (r["created_at"], r["id"]))


def validate_record(record: object, project: str, file_id: str) -> None:
    if not isinstance(record, dict) or set(record) != REQUIRED or record.get("schema") != 1:
        raise ValueError(f"Invalid schema in {file_id}")
    if record["project"] != project or record["id"] != file_id:
        raise ValueError(f"Record ID/project mismatch in {file_id}")
    slug(record["id"], "record id")
    if record["decision"] not in DECISIONS or record["axis"] not in AXES or record["evidence"] not in EVIDENCE:
        raise ValueError(f"Invalid decision, axis or evidence in {file_id}")
    for key in ("candidate", "observation", "because", "next_move", "source", "context"):
        if not isinstance(record[key], str):
            raise ValueError(f"Invalid {key} type in {file_id}")
        if bounded(record[key], key, required=key in ("candidate", "observation", "because")) != record[key]:
            raise ValueError(f"Non-canonical {key} in {file_id}")
    if record["supersedes"] is not None:
        if not isinstance(record["supersedes"], str):
            raise ValueError(f"Invalid supersedes in {file_id}")
        slug(record["supersedes"], "supersedes")
    try:
        timestamp = datetime.fromisoformat(record["created_at"])
        if timestamp.tzinfo is None:
            raise ValueError("missing timezone")
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid created_at in {file_id}") from exc


def active_records(records: list[dict]) -> list[dict]:
    replaced = {r["supersedes"] for r in records if r["supersedes"]}
    return [r for r in records if r["id"] not in replaced]


def record_feedback(root: Path, args: argparse.Namespace) -> dict:
    project = slug(args.project, "project")
    entry_id = slug(args.id, "record id")
    existing = read_records(root, project)
    ids = {r["id"] for r in existing}
    if entry_id in ids:
        raise ValueError("Record already exists; append a new record with --supersedes to correct it")
    if args.supersedes and args.supersedes not in ids:
        raise ValueError("--supersedes must name an existing record")
    record = {
        "schema": 1,
        "id": entry_id,
        "project": project,
        "candidate": bounded(args.candidate, "candidate", required=True),
        "decision": args.decision,
        "axis": args.axis,
        "observation": bounded(args.observation, "observation", required=True),
        "because": bounded(args.because, "because", required=True),
        "next_move": bounded(args.next_move or "", "next_move"),
        "evidence": args.evidence,
        "source": bounded(args.source or "", "source"),
        "context": bounded(args.context or "", "context"),
        "supersedes": args.supersedes,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    directory = record_directory(root, project)
    directory.mkdir(parents=True, exist_ok=True)
    if directory.is_symlink():
        raise ValueError("Refusing symlinked records directory")
    dest = directory / f"{entry_id}.json"
    # x mode prevents accidental overwriting, including from competing sessions.
    with dest.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2, sort_keys=True)
        stream.write("\n")
    return record


def make_brief(root: Path, project: str, limit: int, include_nonowner: bool = False) -> dict:
    if limit < 1 or limit > 30:
        raise ValueError("limit must be 1-30")
    all_active = active_records(read_records(root, project))
    pool = all_active if include_nonowner else [r for r in all_active if r["evidence"] == "OWNER_FEEDBACK"]
    selected = list(reversed(pool))[:limit]
    return {
        "project": project,
        "status": "HUMAN_RECORDED_EXAMPLES_NOT_MODEL_TRAINING",
        "evidence_filter": "ALL_LABELED" if include_nonowner else "OWNER_FEEDBACK_ONLY",
        "total_active_matching": len(pool),
        "records": selected,
    }


def render_brief(data: dict) -> str:
    lines = [f"# Creative judgment handoff — {data['project']}", "",
             "These are **explicit recorded judgments**, not general rules, verified user-study findings, or model training.",
             f"Included: {data['evidence_filter']} ({len(data['records'])} of {data['total_active_matching']} active matching records).", ""]
    if not data["records"]:
        lines.append("No matching design decisions recorded yet.")
    for r in data["records"]:
        lines.extend([
            f"## {r['decision']} — {r['axis']} — {r['candidate']}",
            f"- Observation: {r['observation']}",
            f"- Why: {r['because']}",
            f"- Next move: {r['next_move'] or 'Not specified'}",
            f"- Evidence: {r['evidence']}; source: {r['source'] or 'Not supplied'}; context: {r['context'] or 'Not supplied'}",
            f"- Record: {r['id']}", "",
        ])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Private local data root; defaults to git-ignored .cil-private")
    subs = p.add_subparsers(dest="command", required=True)

    a = subs.add_parser("record", help="Append an immutable design judgment")
    a.add_argument("--project", required=True)
    a.add_argument("--id", required=True)
    a.add_argument("--candidate", required=True, help="Specific design option or screenshot ID")
    a.add_argument("--decision", required=True, choices=DECISIONS)
    a.add_argument("--axis", required=True, choices=AXES)
    a.add_argument("--observation", required=True)
    a.add_argument("--because", required=True)
    a.add_argument("--next-move", default="")
    a.add_argument("--evidence", required=True, choices=EVIDENCE)
    a.add_argument("--source", default="", help="Who/where the judgment came from; no secrets")
    a.add_argument("--context", default="", help="Device/user task or comparison context")
    a.add_argument("--supersedes", default=None, help="Existing record ID superseded by this correction")

    for name in ("list", "audit", "brief"):
        b = subs.add_parser(name)
        b.add_argument("--project", required=True)
        if name == "brief":
            b.add_argument("--limit", type=int, default=8)
            b.add_argument("--format", choices=("markdown", "json"), default="markdown")
            b.add_argument("--include-nonowner", action="store_true")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "record":
            data = record_feedback(args.root, args)
            print(json.dumps({"saved": data["id"], "project": data["project"], "evidence": data["evidence"]}))
        elif args.command == "list":
            print(json.dumps(read_records(args.root, args.project), indent=2, ensure_ascii=False))
        elif args.command == "audit":
            records = read_records(args.root, args.project)
            print(json.dumps({"valid": True, "project": args.project, "records": len(records), "active": len(active_records(records))}))
        elif args.command == "brief":
            result = make_brief(args.root, args.project, args.limit, args.include_nonowner)
            print(json.dumps(result, indent=2, ensure_ascii=False) if args.format == "json" else render_brief(result))
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
