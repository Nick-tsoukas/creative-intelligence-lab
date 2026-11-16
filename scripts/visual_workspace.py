#!/usr/bin/env python3
"""Private, offline project visual-memory CLI for Creative Intelligence Lab.

Python 3.12+, standard library only. No browser, credentials, API or model calls.
Use --help for subcommands. Records are local and never committed by default.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "interface-atlas" / "catalog.json"
CSS = ROOT / "interface-atlas" / "board.css"
DEFAULT_WORKSPACE = ROOT / ".cil-private"
VALID_ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
MAX_IMAGE_BYTES = 24 * 1024 * 1024
MAX_JSON_BYTES = 1024 * 1024
ROLES = ("baseline", "production", "candidate", "approved")
EVIDENCE = ("USER_REPORTED", "IMAGE_OBSERVED", "CODE_OBSERVED",
            "INTERACTION_TESTED", "INFERRED", "UNKNOWN")
KINDS = ("web", "mobile", "component", "motion", "research")


def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def check_id(value, description="ID"):
    if not VALID_ID.fullmatch(value):
        raise ValueError(f"{description}: use 1–64 lowercase a-z, 0-9, hyphen only")
    return value


def clean_url(value):
    if not value:
        return None
    if len(value) > 2048 or any(ch.isspace() for ch in value):
        raise ValueError("URL is too long or includes whitespace")
    u = urlsplit(value)
    if u.username or u.password or u.query or u.fragment:
        raise ValueError("Remove URL credentials, query and fragment; never store tokens")
    if u.scheme == "https" and u.hostname:
        return value
    if u.scheme == "http" and u.hostname in {"localhost", "127.0.0.1"}:
        return value
    raise ValueError("URL must be HTTPS, or localhost HTTP for development")


def read_json(path):
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError(f"Metadata oversized: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def write_new(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def project_path(base, name, initialized=True):
    path = base / "projects" / check_id(name, "project")
    if initialized and not (path / "project.json").is_file():
        raise ValueError(f"Unknown project: {name}. Initialize with init-project")
    return path


def records(project, category):
    directory = project / category
    if not directory.is_dir():
        return []
    return [read_json(p) for p in sorted(directory.glob("*.json"))]


def dimensions(blob):
    if blob.startswith(b"\x89PNG\r\n\x1a\n"):
        if (len(blob) < 45 or blob[12:16] != b"IHDR"
                or blob[-12:] != b"\x00\x00\x00\x00IEND\xaeB\x60\x82"):
            raise ValueError("PNG is truncated or has invalid header")
        width, height = struct.unpack(">II", blob[16:24])
        ext = ".png"
    elif blob.startswith(b"\xff\xd8") and blob.endswith(b"\xff\xd9"):
        width = height = 0
        ext = ".jpg"
        position = 2
        while position < len(blob) - 4:
            if blob[position] != 255:
                raise ValueError("JPEG marker malformed")
            while position < len(blob) and blob[position] == 255:
                position += 1
            if position >= len(blob):
                break
            marker = blob[position]
            position += 1
            if marker in (0xD8, 0xD9, 0x01) or 0xD0 <= marker <= 0xD7:
                continue
            length = struct.unpack(">H", blob[position:position + 2])[0]
            if length < 2 or position + length > len(blob):
                raise ValueError("JPEG segment length invalid")
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                if length < 7:
                    raise ValueError("JPEG frame dimensions missing")
                height, width = struct.unpack(">HH", blob[position + 3:position + 7])
                break
            position += length
        if not width or not height:
            raise ValueError("JPEG image dimensions not located")
    else:
        raise ValueError("Only PNG/JPEG files are supported; a renamed SVG/HTML file is not an image")
    if not width or not height or width > 20000 or height > 50000 or width * height > 60_000_000:
        raise ValueError("Image dimensions exceed limits")
    return width, height, ext


def init_project(a, base):
    p = project_path(base, a.project, False)
    if p.exists():
        raise ValueError("Project already exists; will not overwrite")
    if not a.title.strip():
        raise ValueError("Title required")
    write_new(p / "project.json", {
        "schema": 1, "slug": a.project, "title": a.title.strip(),
        "goal": a.goal.strip(), "created_at_utc": utcnow(),
        "visibility": "PRIVATE_LOCAL_ONLY", "evaluation": "NOT_TESTED",
    })
    print(f"CREATED {p}")


def add_screen(a, base):
    p = project_path(base, a.project)
    check_id(a.id, "screen")
    if not a.redacted_confirmed:
        raise ValueError("Redact/review screenshot first, then supply --redacted-confirmed")
    source = Path(a.file).expanduser()
    if not source.is_file() or source.is_symlink():
        raise ValueError("Image must be an existing regular local file, not symlink")
    size = source.stat().st_size
    if size < 20 or size > MAX_IMAGE_BYTES:
        raise ValueError("Image must be between 20 bytes and 24 MiB")
    blob = source.read_bytes()
    width, height, ext = dimensions(blob)
    digest = hashlib.sha256(blob).hexdigest()
    if any(r["sha256"] == digest for r in records(p, "captures")):
        raise ValueError("Identical image already imported into this project")
    if a.captured_at:
        datetime.strptime(a.captured_at, "%Y-%m-%d")
    if (a.viewport_width is None) != (a.viewport_height is None):
        raise ValueError("Viewport width and height must be supplied together")
    if a.viewport_width and (a.viewport_width < 100 or a.viewport_height < 100):
        raise ValueError("Viewport CSS dimensions too small")
    src = f"screens/{a.id}{ext}"
    img = p / src
    data = p / "captures" / f"{a.id}.json"
    if img.exists() or data.exists():
        raise ValueError("Screenshot ID already exists; old states must not be overwritten")
    img.parent.mkdir(parents=True, exist_ok=True)
    try:
        with img.open("xb") as f:
            f.write(blob)
        write_new(data, {
            "schema": 1, "id": a.id, "label": a.label.strip(), "role": a.role,
            "state": a.state, "image": src, "sha256": digest,
            "pixel_dimensions": [width, height],
            "viewport_css": [a.viewport_width, a.viewport_height]
                if a.viewport_width else None,
            "origin_url": clean_url(a.url), "app_version": a.version or None,
            "original_capture_date": a.captured_at or None,
            "imported_at_utc": utcnow(), "redaction_review": "MANUAL_REVIEW_CONFIRMED",
            "visual_status": "NOT_VISUALLY_INSPECTED_BY_TOOL", "note": a.note or "",
        })
    except Exception:
        if not data.exists() and img.exists():
            img.unlink()
        raise
    print(f"IMPORTED {a.id}: {width}×{height}, {size} bytes; PRIVATE {img}")


def add_finding(a, base):
    p = project_path(base, a.project)
    check_id(a.id, "finding")
    if a.screen not in {x["id"] for x in records(p, "captures")}:
        raise ValueError("Finding must reference an existing screenshot ID")
    if a.evidence == "IMAGE_OBSERVED" and not a.pixels_inspected:
        raise ValueError("Image observations require actually viewing the pixels: --pixels-inspected")
    if not a.statement.strip():
        raise ValueError("Finding statement required")
    write_new(p / "findings" / f"{a.id}.json", {
        "schema": 1, "id": a.id, "screen_id": a.screen,
        "statement": a.statement.strip(), "severity": a.severity,
        "evidence": a.evidence, "desired_outcome": a.outcome or "",
        "counterexample": a.counterexample or "",
        "created_at_utc": utcnow(), "test_status": "NOT_TESTED",
    })
    print(f"RECORDED {a.id} ({a.evidence})")


def add_reference(a, base):
    p = project_path(base, a.project)
    check_id(a.id, "reference")
    if not a.title.strip() or not a.why.strip():
        raise ValueError("Reference title and reason are required")
    write_new(p / "references" / f"{a.id}.json", {
        "schema": 1, "id": a.id, "title": a.title.strip(),
        "url": clean_url(a.url), "kind": a.kind,
        "tags": sorted({x.strip().lower() for x in a.tags.split(",") if x.strip()})[:20],
        "why": a.why.strip(), "status": "LINK_ONLY",
        "visual_evidence": "NOT_INSPECTED", "interaction_evidence": "NOT_TESTED",
        "rights": "LINK_ONLY_NOT_A_REPRODUCTION_GRANT",
        "created_at_utc": utcnow(),
    })
    print(f"RECORDED {a.id} (source link only, not observed)")


def add_direction(a, base):
    p = project_path(base, a.project)
    check_id(a.id, "direction")
    if not a.name.strip() or not a.thesis.strip() or not a.difference.strip():
        raise ValueError("A name, artistic thesis and concrete distinction are required")
    write_new(p / "directions" / f"{a.id}.json", {
        "schema": 1, "id": a.id, "name": a.name.strip(),
        "thesis": a.thesis.strip(), "distinctness": a.difference.strip(),
        "source_ids": [s.strip() for s in a.references.split(",") if s.strip()],
        "preserve": a.preserve or "", "risk": a.risk or "",
        "status": "UNAPPROVED_CONCEPT", "human_critique": "NOT_PERFORMED",
        "browser_qa": "NOT_PERFORMED", "created_at_utc": utcnow(),
    })
    print(f"RECORDED {a.id} (unapproved concept)")


def find(a, base):
    tokens = [x for x in re.findall(r"[a-z0-9]+", a.query.lower()) if len(x) > 2]
    if not tokens:
        raise ValueError("Search requires meaningful words")
    refs = read_json(CATALOG)["entries"]
    # Specific image-observed cases are much more actionable than generic
    # directories. They are still ONLY preview observations, never flow tests.
    cases_path = ROOT / "interface-atlas" / "observed-cases.json"
    if cases_path.is_file():
        for case in read_json(cases_path)["cases"]:
            refs.append({
                "id": case["id"], "name": case["title"],
                "url": case["source_url"], "kind": case["kind"],
                "tags": case["tags"], "why_inspect": case["mechanism"],
                "status": "PREVIEW_OBSERVED",
            })
    if a.project:
        refs += records(project_path(base, a.project), "references")
    scored = []
    for item in refs:
        tags = " ".join(item.get("tags", [])).lower()
        name = (item.get("name") or item.get("title") or "").lower()
        why = (item.get("why_inspect") or item.get("why") or "").lower()
        value = sum(5 if x in tags else 3 if x in name else 1 if x in why else 0 for x in tokens)
        if value and item.get("status") == "PREVIEW_OBSERVED":
            value += 2  # Evidence-weighting applies only to matching cases.
        if value:
            scored.append((value, item))
    for _, r in sorted(scored, key=lambda x: (-x[0], x[1]["id"]))[:a.limit]:
        print(f"{r['id']} | {r.get('name') or r.get('title')} | {r.get('status', 'LINK_ONLY')} | {r['url']}")
    if not scored:
        print("No grounded reference results; do not invent links")


def esc(v):
    return html.escape(str(v or ""), quote=True)


def picture(r):
    path = r["image"]
    if not re.fullmatch(r"screens/[a-z0-9-]+\.(png|jpg)", path):
        raise ValueError("Invalid image record path")
    return f'<a class="shot" href="{esc(path)}" target="_blank" rel="noopener"><img loading="lazy" src="{esc(path)}" alt="{esc(r["label"])} screenshot"></a>'


def board(a, base):
    p = project_path(base, a.project)
    project = read_json(p / "project.json")
    screens, findings = records(p, "captures"), records(p, "findings")
    refs, directions = records(p, "references"), records(p, "directions")
    by_id = {r["id"]: r for r in screens}
    if a.before and a.before not in by_id:
        raise ValueError("Missing --before screenshot")
    if a.after and a.after not in by_id:
        raise ValueError("Missing --after screenshot")
    if a.before and a.after and a.before == a.after:
        raise ValueError("Before and after must differ")
    comparison = ""
    if a.before and a.after:
        pair = ""
        for name, key in (("BEFORE", a.before), ("AFTER", a.after)):
            r = by_id[key]
            pair += f'<article><div class="eyebrow">{name} · {esc(r["role"])}</div>{picture(r)}<h3>{esc(r["label"])}</h3></article>'
        comparison = '<section><h2>Before / after</h2><p class="muted">Recorded images, not proof of success.</p><div class="comparison">' + pair + '</div></section>'
    photos = "".join(
        f'<article class="card">{picture(r)}<div class="details"><p class="eyebrow">{esc(r["role"])} · {esc(r["state"])}</p><h3>{esc(r["label"])}</h3><p class="muted">{esc(r["id"])} · {r["pixel_dimensions"][0]}×{r["pixel_dimensions"][1]} · {esc(r["visual_status"])}</p><p>{esc(r.get("note"))}</p></div></article>'
        for r in screens[-30:]
    ) or '<p class="muted">No screens. Import a manually redacted screenshot first.</p>'
    problems = "".join(
        f'<article class="card details"><p class="eyebrow">{esc(r["severity"])} · {esc(r["evidence"])} · {esc(r["screen_id"])}</p><h3>{esc(r["statement"])}</h3><p>Desired: {esc(r.get("desired_outcome"))}</p><p class="muted">Test: {esc(r["test_status"])}</p></article>'
        for r in findings[-30:]
    ) or '<p class="muted">No grounded findings yet.</p>'
    links = "".join(
        f'<article class="card details"><p class="eyebrow">{esc(r["kind"])} · {esc(r["status"])}</p><h3><a href="{esc(r["url"])}" target="_blank" rel="noopener noreferrer">{esc(r["title"])} ↗</a></h3><p>{esc(r["why"])}</p></article>'
        for r in refs[-30:]
    ) or '<p class="muted">No project-specific inspiration links yet.</p>'
    concepts = "".join(
        f'<article class="card details"><p class="eyebrow">{esc(r["id"])} · {esc(r["status"])}</p><h3>{esc(r["name"])}</h3><p>{esc(r["thesis"])}</p><p class="muted">Distinct because: {esc(r["distinctness"])}</p><p class="muted">Risk: {esc(r["risk"])}</p></article>'
        for r in directions[-12:]
    ) or '<p class="muted">No concepts yet. Develop 3 distinct premises, not 3 palette swaps.</p>'
    css = CSS.read_text(encoding="utf-8")
    head = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(project["title"])} — Visual Memory</title><style>{css}</style></head><body>')
    header = ('<header><span class="brand">CREATIVE INTELLIGENCE · PRIVATE VISUAL MEMORY</span>'
              '<nav aria-label="Workspace navigation"><a href="#screens">Screens</a>'
              '<a href="#findings">Findings</a><a href="#references">References</a>'
              '<a href="#directions">Directions</a></nav></header>'
              f'<div class="hero"><p class="eyebrow">PROJECT {esc(project["slug"])}</p>'
              f'<h1>{esc(project["title"])}</h1><p>{esc(project["goal"])}</p>'
              '<p class="notice">Images are evidence, not user tests. This is a private visual board; no automatic AI image analysis or production approval was performed.</p></div>')
    page = (head + header + comparison +
            '<section id="screens"><h2>Captured states</h2><div class="grid">' + photos + '</div></section>' +
            '<section id="findings"><h2>Problems & evidence</h2><div class="grid">' + problems + '</div></section>' +
            '<section id="references"><h2>Inspiration</h2><div class="grid">' + links + '</div></section>' +
            '<section id="directions"><h2>Original concepts</h2><div class="grid">' + concepts + '</div></section>' +
            '<footer>Generated locally · no analytics or external assets · Keep private.</footer></body></html>')
    tmp = p / "board.html.tmp"
    tmp.write_text(page, encoding="utf-8")
    os.replace(tmp, p / "board.html")
    print(f"BOARD {p / 'board.html'} | screens={len(screens)}, findings={len(findings)}, references={len(refs)}, directions={len(directions)}")


def report(a, base):
    p = project_path(base, a.project)
    project = read_json(p / "project.json")
    print(f"# {project['title']}\nGoal: {project['goal']}\n")
    for label, folder in (("Screens (pixels NOT automatically analyzed)", "captures"),
                          ("Findings and evidence", "findings"),
                          ("Reference links, not reviewed cases", "references"),
                          ("Unapproved directions", "directions")):
        print(f"\n## {label}")
        for r in records(p, folder)[-15:]:
            detail = r.get("label") or r.get("statement") or r.get("title") or r.get("thesis")
            print(f"- {r['id']} [{r.get('evidence') or r.get('status') or 'IMPORTED'}]: {detail}")
            if "image" in r:
                print(f"  - Open actual pixels: {p / r['image']}")
    print("\nNext: open actual images, inspect genuine screen states, research 3–6 references, propose and critique 3 distinct original directions.")


def audit(a, base):
    p = project_path(base, a.project)
    problems = []
    project = read_json(p / "project.json")
    if project.get("slug") != a.project or project.get("visibility") != "PRIVATE_LOCAL_ONLY":
        problems.append("Project metadata inconsistent")
    screens = records(p, "captures")
    seen = set()
    for r in screens:
        rid = r.get("id", "")
        if not VALID_ID.fullmatch(rid):
            problems.append("Malformed screen ID")
            continue
        image = r.get("image", "")
        if not re.fullmatch(r"screens/[a-z0-9-]+\.(png|jpg)", image):
            problems.append(f"{rid}: unsafe path")
            continue
        path = p / image
        if not path.is_file() or path.is_symlink():
            problems.append(f"{rid}: screenshot missing or symlink")
            continue
        if path.stat().st_size > MAX_IMAGE_BYTES:
            problems.append(f"{rid}: file too large")
            continue
        blob = path.read_bytes()
        try:
            w, h, _ = dimensions(blob)
            if [w, h] != r["pixel_dimensions"]:
                problems.append(f"{rid}: dimensions changed")
            digest = hashlib.sha256(blob).hexdigest()
            if digest != r["sha256"]:
                problems.append(f"{rid}: image tampered with")
            if digest in seen:
                problems.append(f"{rid}: duplicate image")
            seen.add(digest)
        except (ValueError, KeyError) as err:
            problems.append(f"{rid}: invalid image ({err})")
    for r in records(p, "findings"):
        if r.get("screen_id") not in {x["id"] for x in screens}:
            problems.append(f"Finding {r.get('id')} has missing screen")
        if r.get("evidence") not in EVIDENCE:
            problems.append(f"Finding {r.get('id')} has invalid evidence")
    for r in records(p, "directions"):
        if r.get("status") != "UNAPPROVED_CONCEPT":
            problems.append(f"Direction {r.get('id')} claims unsupported approval")
    for r in records(p, "references"):
        try:
            clean_url(r.get("url"))
        except ValueError:
            problems.append(f"Reference {r.get('id')} has unsafe URL")
    if problems:
        for issue in problems:
            print("FAIL", issue)
        raise ValueError(f"Audit found {len(problems)} issue(s)")
    print(f"PASS: private project integrity ({len(screens)} screenshots); NO visual or UX efficacy claim")


def parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE,
                   help="private workspace root (default repo/.cil-private)")
    sp = p.add_subparsers(dest="action", required=True)
    init = sp.add_parser("init-project")
    init.add_argument("--project", required=True)
    init.add_argument("--title", required=True)
    init.add_argument("--goal", default="")
    cap = sp.add_parser("add-screen")
    for key in ("project", "id", "file", "label"):
        cap.add_argument("--" + key, required=True)
    cap.add_argument("--redacted-confirmed", action="store_true")
    cap.add_argument("--role", choices=ROLES, default="baseline")
    cap.add_argument("--state", default="default")
    cap.add_argument("--url")
    cap.add_argument("--captured-at")
    cap.add_argument("--version")
    cap.add_argument("--viewport-width", type=int)
    cap.add_argument("--viewport-height", type=int)
    cap.add_argument("--note", default="")
    note = sp.add_parser("add-finding")
    for key in ("project", "id", "screen", "statement"):
        note.add_argument("--" + key, required=True)
    note.add_argument("--severity", choices=("blocking", "major", "minor", "opportunity"), default="major")
    note.add_argument("--evidence", choices=EVIDENCE, default="USER_REPORTED")
    note.add_argument("--pixels-inspected", action="store_true")
    note.add_argument("--outcome", default="")
    note.add_argument("--counterexample", default="")
    ref = sp.add_parser("add-reference")
    for key in ("project", "id", "title", "url", "why"):
        ref.add_argument("--" + key, required=True)
    ref.add_argument("--kind", choices=KINDS, required=True)
    ref.add_argument("--tags", default="")
    direction = sp.add_parser("add-direction")
    for key in ("project", "id", "name", "thesis", "difference"):
        direction.add_argument("--" + key, required=True)
    direction.add_argument("--references", default="")
    direction.add_argument("--preserve", default="")
    direction.add_argument("--risk", default="")
    search = sp.add_parser("find")
    search.add_argument("--query", required=True)
    search.add_argument("--project")
    search.add_argument("--limit", type=int, choices=range(1, 13), default=6)
    bd = sp.add_parser("board")
    bd.add_argument("--project", required=True)
    bd.add_argument("--before")
    bd.add_argument("--after")
    for name in ("report", "audit"):
        sub = sp.add_parser(name)
        sub.add_argument("--project", required=True)
    return p


def main(argv=None):
    a = parser().parse_args(argv)
    commands = {"init-project": init_project, "add-screen": add_screen,
                "add-finding": add_finding, "add-reference": add_reference,
                "add-direction": add_direction, "find": find,
                "board": board, "report": report, "audit": audit}
    try:
        base = a.workspace.expanduser().resolve()
        if a.action != "find":
            base.mkdir(parents=True, exist_ok=True)
        commands[a.action](a, base)
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as err:
        print("ERROR:", err, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
