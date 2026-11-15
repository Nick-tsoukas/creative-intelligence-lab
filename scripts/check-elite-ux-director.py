#!/usr/bin/env python3
"""Static Elite UX Director package validation. No LLM calls or product UX tests.

Run: python scripts/check-elite-ux-director.py
Standard library only. Failure exits nonzero. Separates structural proof from
claiming any model performance, user research, or accessibility conformance.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "elite-ux-director"
MAIN = SKILL / "SKILL.md"
REQUIRED = (
    "references/TASK_SOURCE_ROUTER.md",
    "references/DECISION_CARDS.md",
    "references/INTERACTION_PATTERNS.md",
    "references/PERSONA_AND_CONTEXT_METHOD.md",
    "references/INDEPENDENT_EVALUATION.md",
    "references/ISSUE_RUBRIC.md",
    "references/SOURCE_LEDGER.md",
    "templates/UX_REVIEW_TEMPLATE.md",
    "scripts/retrieve.py",
    "EVALUATION.md",
)


def check() -> list[str]:
    errors: list[str] = []
    if not MAIN.is_file():
        return [f"Missing SKILL.md: {MAIN}"]
    body = MAIN.read_text(encoding="utf-8")
    lines = body.splitlines()
    if not lines or lines[0] != "---":
        return ["Missing YAML frontmatter delimiter"]
    try:
        stop = lines.index("---", 1)
    except ValueError:
        return ["Missing closing YAML frontmatter delimiter"]
    fields: dict[str, str] = {}
    for line in lines[1:stop]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            errors.append("Unparseable frontmatter line (simple scalar parser)")
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        if k in fields:
            errors.append(f"Duplicate frontmatter key: {k}")
        fields[k] = v.strip().strip('"').strip("'")
    if fields.get("name") != SKILL.name:
        errors.append("name must match skill directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")):
        errors.append("name violates agentskills.io naming")
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append("description must be 1–1024 characters")
    if "when" not in fields.get("description", "").lower() and "use for" not in fields.get("description", "").lower():
        errors.append("description should mention activation circumstance")
    if len(lines) > 500:
        errors.append("SKILL.md over 500 lines (progressive disclosure)")
    if len(body) > 20000:
        errors.append("SKILL.md over conservative 20k character budget")
    for rel in REQUIRED:
        if not (SKILL / rel).is_file():
            errors.append(f"Missing bundled resource: {rel}")
    for match in re.finditer(r"\]\(((?:references|templates)/[^)#]+\.md)\)", body):
        rel = match.group(1)
        if not (SKILL / rel).is_file():
            errors.append(f"Broken linked reference: {rel}")
    for match in re.finditer(r"`((?:scripts|references|templates)/[a-zA-Z0-9_.-]+\.(?:md|py))`", body):
        rel = match.group(1)
        if not (SKILL / rel).is_file():
            errors.append(f"Broken code reference: {rel}")
    if any((SKILL / p).exists() for p in ["references/FANEQO_QR_ADAPTER.md", "references/FANEQO_MESSAGING_ADAPTER.md"]):
        errors.append("Product-specific adapters must not ship inside reusable skill")
    for doc in SKILL.rglob("*.md"):
        if not doc.read_text(encoding="utf-8").strip():
            errors.append(f"Empty document: {doc.relative_to(SKILL)}")
    for key in ("P0", "P1", "P2", "P3"):
        if key not in (SKILL / "references/ISSUE_RUBRIC.md").read_text(encoding="utf-8"):
            errors.append(f"Missing severity: {key}")
    # Exercise deterministic retrieval, not the LLM skill.
    selector = SKILL / "scripts/retrieve.py"
    if selector.exists():
        spec = importlib.util.spec_from_file_location("ux_retrieve", selector)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            cards = module.sections("card")
            patterns = module.sections("pattern")
            if list(cards) != [f"C{x:02d}" for x in range(1, 10)]:
                errors.append("Expected decision cards C01–C09 exactly")
            if list(patterns) != [f"P{x}" for x in range(1, 10)]:
                errors.append("Expected patterns P1–P9 exactly")
            if any("## C" in text[5:] for text in cards.values()):
                errors.append("Retrieved decision card includes another card")
            if any("## P" in text[5:] for text in patterns.values()):
                errors.append("Retrieved pattern includes another pattern")
        else:
            errors.append("Cannot load retrieval module")
    fixtures = ROOT / "quality/ux_skill_eval_cases.json"
    if fixtures.is_file():
        data = json.loads(fixtures.read_text(encoding="utf-8"))
        if data.get("status") != "NOT_RUN":
            errors.append("Prepared quality fixtures must not imply run results")
        cases = data["activation_cases"]
        if not any(c["expected"] == "activate" for c in cases) or not any(c["expected"] == "do_not_activate" for c in cases):
            errors.append("Activation set requires positive and negative fixtures")
    return sorted(set(errors))


if __name__ == "__main__":
    problems = check()
    for issue in problems:
        print("FAIL:", issue)
    if problems:
        sys.exit(1)
    print("PASS: metadata, bundled references, product separation, retrieval and fixture structure.")
    print("NOT TESTED: model invocation, skill effectiveness, user task outcomes, browser accessibility.")
