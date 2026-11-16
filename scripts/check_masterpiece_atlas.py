#!/usr/bin/env python3
"""Static provenance, retrieval and integration safety validation.

Validates source-linked Atlas integrity only. No external URLs are fetched.
Not a browser/UX evaluation, model benchmark or proof of art-historical depth.
"""
from __future__ import annotations
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "visual-library/masterpiece-atlas"
ALLOWED = {"OBJECT_IDENTIFIED", "PREVIEW_OBSERVED", "PRIMARY_CONTEXT_READ",
           "DEEP_VISUAL_STUDY", "MULTI_WORK_COMPARISON",
           "DIGITAL_TRANSFER_PROPOSED", "BROWSER_EXERCISE_RUN", "HUMAN_OUTCOME_OBSERVED"}


def check() -> list[str]:
    errors = []
    data = json.loads((ATLAS / "index.json").read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    if len(entries) != 8:
        errors.append("Expected eight first-pass studies; count changes require explicit review")
    if data.get("image_assets_embedded") is not False:
        errors.append("No third-party imagery may be embedded in Atlas")
    ids = set()
    for e in entries:
        key = e.get("id")
        if key in ids or not re.fullmatch(r"MA-\d{3}", key or ""):
            errors.append(f"Duplicate/invalid work ID {key}")
        ids.add(key)
        file = (ATLAS / e.get("study", "")).resolve()
        if ATLAS.resolve() not in file.parents or not file.is_file():
            errors.append(f"Missing or unsafe study {key}")
            continue
        content = file.read_text(encoding="utf-8")
        if (len(content) < 1000 or not all(s in content.lower() for s in ["source", "observed", "hypothesis"]) or not ("not done" in content.lower() or "not run" in content.lower())):
            errors.append(f"Study {key} lacks original evidence/counterexample coverage")
        if not e.get("source", "").startswith("https://"):
            errors.append(f"Unverified source URL format for {key}")
        if not set(e.get("evidence", [])).issubset(ALLOWED):
            errors.append(f"Unexpected evidence status for {key}")
        if any(x in e.get("evidence", []) for x in ["BROWSER_EXERCISE_RUN", "HUMAN_OUTCOME_OBSERVED", "DEEP_VISUAL_STUDY"]):
            errors.append(f"First pass {key} must not claim deep visual or empirical task testing")
        for field in ("creator", "title", "year", "rights", "mechanism"):
            if not e.get(field):
                errors.append(f"Missing {field} in {key}")
    spec = importlib.util.spec_from_file_location("atlas_query", ROOT / "scripts/query_masterpiece_atlas.py")
    if spec is None or spec.loader is None:
        return errors + ["Cannot load Atlas selector"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for e in entries:
        selected = module.find(e["id"])
        if selected is None or selected["id"] != e["id"]:
            errors.append(f"Selector cannot resolve {e['id']}")
    if not module.search("light") or len(module.search("light")) > 6:
        errors.append("Bounded search broken")
    if any((ATLAS / "studies").glob("*.png")) or any((ATLAS / "studies").glob("*.jpg")):
        errors.append("Third-party raster assets must remain off-repo")
    return errors


if __name__ == "__main__":
    failures = check()
    for problem in failures:
        print("FAIL:", problem)
    if failures:
        raise SystemExit(1)
    print("PASS: eight Atlas records, provenance fields, linked studies, safe paths, bounded lookup.")
    print("NOT TESTED: visual images beyond described previews, user behavior, browser access, effect on v5.0 skill.")
