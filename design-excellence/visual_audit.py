#!/usr/bin/env python3
"""Visual-design audit records for *actually inspected* local project screenshots.

No image interpretation occurs in this program. A vision-capable critic opens
pixels; this tool preserves accountable, prioritized observations and reports.
Integrates read-only with scripts/visual_workspace.py capture metadata.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
CATEGORIES = ("COMPOSITION", "SPACING", "TYPOGRAPHY", "PHOTOGRAPHY", "COLOR", "HIERARCHY", "MOTION", "MICRODETAIL", "RESPONSIVE", "TASK_VISIBILITY", "OTHER")
SEVERITY = ("BLOCKER", "MAJOR", "REFINE")
EVIDENCE = ("IMAGE_OBSERVED", "OWNER_REPORTED", "DESIGN_HYPOTHESIS")
MAX_TEXT = 900
MAX_IMAGE = 24 * 1024 * 1024
DEFAULT_WORKSPACE = Path(__file__).resolve().parents[1] / ".cil-private"
AUDIT_FIELDS = {"schema", "id", "project", "screen_id", "capture_sha256", "source_image", "viewport_css", "capture_state", "created_at", "visual_status"}
OBS_FIELDS = {"schema", "id", "audit_id", "category", "severity", "observation", "because", "recommendation", "evidence", "created_at"}


def safe_id(s: str) -> str:
    if not isinstance(s, str) or not ID.fullmatch(s):
        raise ValueError("ID must be 1–64 lowercase letters/digits/hyphen")
    return s


def short(s: str, required: bool = True) -> str:
    if not isinstance(s, str):
        raise ValueError("Expected text")
    t = s.strip()
    if (required and not t) or len(t) > MAX_TEXT or "\x00" in t:
        raise ValueError("Text must be nonempty when required, at most 900 chars, without NUL")
    return t


def read_json(path: Path, limit: int = 64_000) -> dict:
    if not path.is_file() or path.is_symlink() or path.stat().st_size > limit:
        raise ValueError("Missing, symlinked, or oversized JSON: " + path.name)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as e:
        raise ValueError("Invalid JSON: " + path.name) from e
    if not isinstance(value, dict):
        raise ValueError("Expected JSON object: " + path.name)
    return value


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def project_path(workspace: Path, project: str) -> Path:
    root = workspace / "projects" / safe_id(project)
    if root.is_symlink() or not (root / "project.json").is_file():
        raise ValueError("Project must already exist in private visual workspace")
    return root


def audit_path(workspace: Path, project: str, audit: str) -> Path:
    return workspace / "design-audits" / safe_id(project) / safe_id(audit)


def capture(workspace: Path, project: str, screen: str) -> tuple[dict, Path]:
    p = project_path(workspace, project)
    c = read_json(p / "captures" / (safe_id(screen) + ".json"))
    if c.get("id") != screen or c.get("schema") != 1 or c.get("redaction_review") != "MANUAL_REVIEW_CONFIRMED":
        raise ValueError("Screen capture metadata invalid or not marked manually redacted")
    rel = c.get("image")
    if not isinstance(rel, str) or Path(rel).is_absolute() or ".." in Path(rel).parts:
        raise ValueError("Unsafe capture image path")
    image = p / rel
    if not image.is_file() or image.is_symlink() or not image.resolve().is_relative_to(p.resolve()):
        raise ValueError("Captured image unavailable or unsafe")
    if image.stat().st_size > MAX_IMAGE:
        raise ValueError("Captured image exceeds 24MB")
    with image.open("rb") as stream:
        blob_hash = hashlib.file_digest(stream, "sha256").hexdigest()
    if blob_hash != c.get("sha256"):
        raise ValueError("Captured image hash mismatch; refresh original capture")
    return c, image


def validate_audit(a: dict, audit: str, project: str) -> None:
    if set(a) != AUDIT_FIELDS or a.get("schema") != 1:
        raise ValueError("Audit schema mismatch")
    if a["id"] != audit or a["project"] != project:
        raise ValueError("Audit metadata does not match path")
    safe_id(a["screen_id"])
    if not re.fullmatch(r"[a-f0-9]{64}", a["capture_sha256"]):
        raise ValueError("Invalid source capture hash")
    if not isinstance(a["source_image"], str) or ".." in Path(a["source_image"]).parts:
        raise ValueError("Invalid source image path")
    if not isinstance(a["viewport_css"], (list, type(None))):
        raise ValueError("Invalid viewport")
    if a["visual_status"] != "OBSERVATIONS_RECORDED_SEPARATELY":
        raise ValueError("Invalid visual status")


def load_audit(workspace: Path, project: str, audit: str) -> dict:
    base = audit_path(workspace, project, audit)
    a = read_json(base / "audit.json")
    validate_audit(a, audit, project)
    c, _ = capture(workspace, project, a["screen_id"])
    if c["sha256"] != a["capture_sha256"]:
        raise ValueError("Source capture changed since audit started")
    return a


def observations(workspace: Path, project: str, audit: str) -> list[dict]:
    load_audit(workspace, project, audit)
    base = audit_path(workspace, project, audit) / "observations"
    if not base.exists():
        return []
    if base.is_symlink():
        raise ValueError("Observation directory is symlinked")
    entries = []
    for path in sorted(base.glob("*.json")):
        d = read_json(path)
        if set(d) != OBS_FIELDS or d.get("schema") != 1 or d.get("id") != path.stem or d.get("audit_id") != audit:
            raise ValueError("Invalid observation: " + path.stem)
        safe_id(d["id"])
        if d["category"] not in CATEGORIES or d["severity"] not in SEVERITY or d["evidence"] not in EVIDENCE:
            raise ValueError("Invalid category/severity/evidence: " + path.stem)
        for key in ("observation", "because", "recommendation"):
            if short(d[key]) != d[key]:
                raise ValueError("Invalid observation text: " + path.stem)
        entries.append(d)
    return entries


def start(workspace: Path, project: str, audit: str, screen: str) -> dict:
    c, _ = capture(workspace, project, screen)
    record = {"schema": 1, "id": safe_id(audit), "project": safe_id(project), "screen_id": screen,
              "capture_sha256": c["sha256"], "source_image": c["image"],
              "viewport_css": c.get("viewport_css"), "capture_state": str(c.get("state") or "")[:MAX_TEXT],
              "created_at": now(), "visual_status": "OBSERVATIONS_RECORDED_SEPARATELY"}
    target = audit_path(workspace, project, audit) / "audit.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8") as f:
        json.dump(record, f, indent=2, sort_keys=True)
        f.write("\n")
    return record


def observe(workspace: Path, project: str, audit: str, args: argparse.Namespace) -> dict:
    load_audit(workspace, project, audit)
    if args.evidence == "IMAGE_OBSERVED" and not args.pixels_inspected:
        raise ValueError("IMAGE_OBSERVED requires --pixels-inspected after genuinely viewing the image")
    entry = {"schema": 1, "id": safe_id(args.id), "audit_id": audit,
             "category": args.category, "severity": args.severity,
             "observation": short(args.observation), "because": short(args.because),
             "recommendation": short(args.recommendation),
             "evidence": args.evidence, "created_at": now()}
    dest = audit_path(workspace, project, audit) / "observations" / (entry["id"] + ".json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("x", encoding="utf-8") as f:
        json.dump(entry, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    return entry


def report(workspace: Path, project: str, audit: str) -> str:
    a = load_audit(workspace, project, audit)
    items = observations(workspace, project, audit)
    items.sort(key=lambda x: (SEVERITY.index(x["severity"]), x["category"], x["id"]))
    checked = sorted({x["category"] for x in items if x["evidence"] == "IMAGE_OBSERVED"})
    unreviewed = [x for x in CATEGORIES if x not in checked]
    lines = [f"# Visual Design Audit — {project} / {a['screen_id']}", "",
             "**This is a reviewer-authored audit, not an automatic image interpretation.**",
             f"- Capture SHA-256: {a['capture_sha256']}",
             f"- Viewport: {a['viewport_css'] if a['viewport_css'] is not None else 'UNKNOWN'}",
             f"- State: {a['capture_state'] or 'UNKNOWN'}",
             f"- Observations: {len(items)} ({sum(x['evidence']=='IMAGE_OBSERVED' for x in items)} reported as pixels-inspected)",
             "- Visual categories with no direct observation: " + (", ".join(unreviewed) or "none"),
             "", "## Prioritized findings"]
    if not items:
        lines.append("No findings recorded. The image has **not** been audited by this tool.")
    for i, x in enumerate(items, start=1):
        lines += [f"### {i}. [{x['severity']}] {x['category']} — {x['evidence']}",
                  f"- Observed/reported: {x['observation']}",
                  f"- Why it matters: {x['because']}",
                  f"- Actionable revision: {x['recommendation']}",
                  f"- Finding ID: {x['id']}", ""]
    lines += ["## Verification required before sign-off",
              "- Re-open and inspect actual before/after screenshots at the same viewport and state",
              "- Check primary actions, photo crops, hierarchy, contrast, font scaling, whitespace and mobile reflow",
              "- Test keyboard/focus, 200% zoom, reduced motion, content and state fallbacks independently",
              "- A screenshot cannot prove API behavior, accessibility compliance or user success",
              "- Record the owner's acceptance/rejection separately; never invent approval", ""]
    return "\n".join(lines)


def prompt(workspace: Path, project: str, audit: str) -> str:
    a = load_audit(workspace, project, audit)
    _, image = capture(workspace, project, a["screen_id"])
    return "\n".join([
        "# Visual Art Director — Evidence-Bound Audit Prompt",
        "Actually OPEN the following local image in a vision-capable viewer; do not infer pixels from labels:",
        str(image), "",
        "Review ONLY the visible composition. Record exact focal point, typography scale/weight/line wraps,",
        "negative-space rhythm, portrait crops and visual salience, colors/contrast appearance, spacing,",
        "image authenticity limits, hierarchy, balance, interface affordance visibility and micro-detail.",
        "Prioritize at most five fixes. Explain what to change and WHY it will improve this product-specific",
        "experience. Separate observed defects from subjective preference and unknown function.",
        "Never call an unseen screenshot beautiful/poor. Never claim flows or backend permissions tested.",
        "Examine desktop, narrow mobile and relevant states as separate captures rather than extrapolating.",
        "Use 'observe --pixels-inspected' only after actual pixel inspection and real observations.",
        "Keep inspiration mechanisms original; do not clone layouts or copyrighted art.",
    ]) + "\n"



def compare(workspace: Path, project: str, baseline_id: str, candidate_id: str) -> str:
    """Prepare paired, actual-image references; no automatic 'improvement' claim."""
    if baseline_id == candidate_id:
        raise ValueError("Use two different audit IDs")
    before = load_audit(workspace, project, safe_id(baseline_id))
    after = load_audit(workspace, project, safe_id(candidate_id))
    _, before_image = capture(workspace, project, before["screen_id"])
    _, after_image = capture(workspace, project, after["screen_id"])
    same_view = before["viewport_css"] == after["viewport_css"]
    same_state = before["capture_state"] == after["capture_state"]
    lines = [
        "# Before / After — Independent Visual Comparison",
        "**Neither comparison nor apparent visual polish proves UX or design quality improvement.**",
        f"- BEFORE screenshot: {before_image}",
        f"- AFTER screenshot: {after_image}",
        f"- BEFORE viewport/state: {before['viewport_css']} / {before['capture_state'] or 'UNKNOWN'}",
        f"- AFTER viewport/state: {after['viewport_css']} / {after['capture_state'] or 'UNKNOWN'}",
        f"- Viewport comparable: {'YES' if same_view else 'NO — recapture matched viewport'}",
        f"- Product state comparable: {'YES' if same_state else 'NO — inspect state differences'}",
        "",
        "Open BOTH actual images. Independently judge changes to focal hierarchy, photo crop,",
        "typography, breathing room, visual rhythm, comprehension and the primary action.",
        "Inspect whether a correction introduced a new visual or operational failure.",
        "Record the real owner's judgment separately; do not invent acceptance.",
        "",
        "## BEFORE audit evidence", report(workspace, project, baseline_id),
        "## AFTER audit evidence", report(workspace, project, candidate_id),
        "## Human decision still needed",
        "Winner: NOT SELECTED. No aesthetic or task success is certified by this report.",
    ]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE)
    commands = p.add_subparsers(dest="command", required=True)
    for command in ("start", "observe", "report", "prompt", "audit", "compare"):
        x = commands.add_parser(command)
        x.add_argument("--project", required=True)
        if command != "compare":
            x.add_argument("--audit", required=True)
        else:
            x.add_argument("--before", required=True)
            x.add_argument("--after", required=True)
        if command == "start":
            x.add_argument("--screen", required=True)
        if command == "observe":
            x.add_argument("--id", required=True)
            x.add_argument("--category", required=True, choices=CATEGORIES)
            x.add_argument("--severity", required=True, choices=SEVERITY)
            x.add_argument("--observation", required=True)
            x.add_argument("--because", required=True)
            x.add_argument("--recommendation", required=True)
            x.add_argument("--evidence", required=True, choices=EVIDENCE)
            x.add_argument("--pixels-inspected", action="store_true")
    args = p.parse_args(argv)
    try:
        root = args.workspace.expanduser().resolve()
        if args.command == "start":
            print(json.dumps(start(root, args.project, args.audit, args.screen), indent=2))
        elif args.command == "observe":
            print(json.dumps(observe(root, args.project, args.audit, args), indent=2))
        elif args.command == "report":
            print(report(root, args.project, args.audit))
        elif args.command == "compare":
            print(compare(root, args.project, args.before, args.after))
        elif args.command == "prompt":
            print(prompt(root, args.project, args.audit))
        else:
            records = observations(root, args.project, args.audit)
            print(json.dumps({"valid": True, "observation_count": len(records), "audit": args.audit}))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
