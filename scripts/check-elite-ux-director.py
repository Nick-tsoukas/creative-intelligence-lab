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
    "references/SCREEN_INTELLIGENCE.md",
    "references/ACTION_TRUTH.md",
    "references/DESIGN_TO_CODE.md",
    "references/RENDER_AND_VERIFY.md",
    "references/VISUAL_CRAFT_AND_MEMORY.md",
    "references/RESEARCH_AND_DISTILLATION.md",
    "scripts/check_capture.py",
    "references/TASK_SOURCE_ROUTER.md",
    "references/DECISION_CARDS.md",
    "references/HOMEPAGE_INTELLIGENCE.md",
    "references/BOOK_STUDY_PROTOCOL.md",
    "references/VISUAL_ANALYSIS_PROTOCOL.md",
    "references/DESIGN_KNOWLEDGE_SCHEMA.md",
    "references/CROSS_BOOK_SYNTHESIS.md",
    "references/KNOWLEDGE_CARDS.md",
    "references/RESEARCH_INDEX.md",
    "references/INTERACTION_PATTERNS.md",
    "references/PERSONA_AND_CONTEXT_METHOD.md",
    "references/INDEPENDENT_EVALUATION.md",
    "references/ISSUE_RUBRIC.md",
    "references/SOURCE_LEDGER.md",
    "templates/UX_REVIEW_TEMPLATE.md",
    "templates/HOMEPAGE_UX_PACKET.md",
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
    core = body.split("---", 2)[-1]
    if len(core.split()) > 800:
        errors.append("Runtime core exceeds 800 words")
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
            homepages = module.sections("homepage")
            knowledge = module.sections("knowledge")
            if list(cards) != [f"C{x:02d}" for x in range(1, 10)]:
                errors.append("Expected decision cards C01–C09 exactly")
            if list(patterns) != [f"P{x}" for x in range(1, 10)]:
                errors.append("Expected patterns P1–P9 exactly")
            if list(homepages) != [f"H{x:02d}" for x in range(1, 9)]:
                errors.append("Expected homepage decision cards H01–H08 exactly")
            if list(knowledge) != [f"K{x:02d}" for x in range(1, 10)]:
                errors.append("Expected research knowledge cards K01–K09 exactly")
            if any("## K" in text[5:] for text in knowledge.values()):
                errors.append("Retrieved research knowledge card includes another knowledge card")
            for key, chunk in knowledge.items():
                if not all(part in chunk for part in ("**Source", "**Trigger", "**Counterexample", "**Actual evaluation")):
                    errors.append(f"Research card {key} missing provenance/condition/evaluation fields")
            if not module.search_words("homepage hierarchy") or len(module.search_words("homepage hierarchy")) > 6:
                errors.append("Knowledge search returned no results or overlong response")
            if any("## H" in text[5:] for text in homepages.values()):
                errors.append("Retrieved homepage card includes another homepage card")
            if any("## C" in text[5:] for text in cards.values()):
                errors.append("Retrieved decision card includes another card")
            if any("## P" in text[5:] for text in patterns.values()):
                errors.append("Retrieved pattern includes another pattern")
        else:
            errors.append("Cannot load retrieval module")
    if "homepage" not in fields.get("description", "").lower():
        errors.append("Homepage activation cue missing from skill description")
    review_template = (SKILL / "templates/UX_REVIEW_TEMPLATE.md").read_text(encoding="utf-8")
    normalized_review = " ".join(review_template.split()).lower()
    for label in (
        "Routes/components:",
        "Locked/open:",
        "Actions/data:",
        "Desktop→mobile:",
        "Accessibility:",
        "Acceptance:",
        "Visual verification:",
    ):
        if label not in review_template:
            errors.append(f"Implementation handoff missing field: {label}")
    for requirement in (
        "composition/hierarchy",
        "typography/spacing",
        "authentic imagery/art direction",
        "interaction clarity",
        "mobile transformation",
        "observed pixels",
        "automated capture/overflow checks validate capture or geometry, not aesthetics or task success",
    ):
        if requirement not in normalized_review:
            errors.append(f"Visual review missing criterion: {requirement}")
    # Read-only catalog check: no automatic edition promotion or ingest claims.
    recon = ROOT / "scripts/reconcile_ux_book_canon.py"
    if not recon.is_file():
        errors.append("Missing canonical catalog reconciliation script")
    else:
        spec = importlib.util.spec_from_file_location("ux_books", recon)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            summary = module.reconcile()
            if summary["incoming_books"] != 82 or summary["incoming_other_resources"] != 40:
                errors.append("Uploaded source manifest count differs from expected 82 + 40")
            if summary["legacy_catalog_book_entries"] != 130:
                errors.append("Legacy catalog count differs from historical 130")
            if summary["incoming_study_statuses"] != {"not-ingested": 122}:
                errors.append("New intake must not be auto-marked read or studied")
        else:
            errors.append("Cannot import catalog reconciler")
    for path in (
        "sources/intake/2026-11-15/BOOK_TO_DESIGN_INTELLIGENCE_PROTOCOL.md",
        "sources/intake/2026-11-15/ELITE_UX_DESIGN_SOURCE_MANIFEST.csv",
        "sources/intake/2026-11-15/ELITE_UX_DESIGN_RESEARCH_CANON.md",
        "sources/BOOK_CANON_RECONCILIATION_2026-11-15.md",
    ):
        if not (ROOT / path).is_file():
            errors.append(f"Missing provenance/intake file: {path}")
    fixtures = ROOT / "quality/ux_skill_eval_cases.json"
    if fixtures.is_file():
        data = json.loads(fixtures.read_text(encoding="utf-8"))
        if data.get("status") != "NOT_RUN":
            errors.append("Prepared quality fixtures must not imply run results")
        cases = data["activation_cases"]
        if not any(c["expected"] == "activate" for c in cases) or not any(c["expected"] == "do_not_activate" for c in cases):
            errors.append("Activation set requires positive and negative fixtures")
        dashboard = next((case for case in data.get("quality_cases", []) if case.get("id") == "Q17"), None)
        if dashboard is None:
            errors.append("Missing dashboard/data UX evaluation fixture Q17")
        else:
            required = ("gross/net", "loading", "empty", "mobile", "chart")
            coverage = " ".join(dashboard.get("must_detect", [])).lower()
            has_failure_state = "error" in coverage or "failure" in coverage
            if not dashboard.get("prompt") or any(term not in coverage for term in required) or not has_failure_state:
                errors.append("Q17 must include a prompt and metric/state/responsive/accessibility criteria")
    return sorted(set(errors))


if __name__ == "__main__":
    problems = check()
    for issue in problems:
        print("FAIL:", issue)
    if problems:
        sys.exit(1)
    print("PASS: skill metadata, source cards, evidence/intake integrity, book reconciliation, bounded retrieval and fixture structure.")
    print("NOT TESTED BY THIS CHECK: activation, overall skill effectiveness, user outcomes, browser accessibility.")
