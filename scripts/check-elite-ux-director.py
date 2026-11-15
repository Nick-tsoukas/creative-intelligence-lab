#!/usr/bin/env python3
"""Static packaging checks for the Elite UX Director Claude skill.

This is NOT a skill-efficacy benchmark, product UX test, accessibility audit,
or verification that any book has been read. It checks only local distribution
structure and obvious reference packaging errors. Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "elite-ux-director"
MAIN = SKILL / "SKILL.md"
REQUIRED = [
    "references/TASK_SOURCE_ROUTER.md",
    "references/DECISION_CARDS.md",
    "references/INTERACTION_PATTERNS.md",
    "references/PERSONA_AND_CONTEXT_METHOD.md",
    "references/ISSUE_RUBRIC.md",
    "references/SOURCE_LEDGER.md",
    "templates/UX_REVIEW_TEMPLATE.md",
]


def check() -> list[str]:
    errors: list[str] = []
    if not MAIN.is_file():
        return [f"Missing entrypoint: {MAIN}"]
    text = MAIN.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append("SKILL.md frontmatter must start with ---")
        return errors
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append("SKILL.md has no closing YAML delimiter")
        return errors
    fm = "\n".join(lines[1:end])
    fields = {}
    for line in lines[1:end]:
        if ":" in line:
            key, value = line.split(":", 1)
            if key.strip() in fields:
                errors.append(f"Duplicate frontmatter key: {key.strip()}")
            fields[key.strip()] = value.strip()
    if fields.get("name") != SKILL.name:
        errors.append("Frontmatter name does not match folder")
    if not fields.get("description"):
        errors.append("Frontmatter description is missing")
    if len(fields.get("description", "")) > 1024:
        errors.append("Frontmatter description exceeds 1024 characters")
    if len(text) > 20000:
        errors.append("SKILL.md exceeds 20k characters; consider progressive disclosure")
    for rel in REQUIRED:
        if not (SKILL / rel).is_file():
            errors.append(f"Missing required local reference: {rel}")
    for rel in re.findall(r"`((?:references|templates)/[A-Za-z0-9_.-]+\.md)`", text):
        if not (SKILL / rel).is_file():
            errors.append(f"Broken SKILL.md reference: {rel}")
    for rel in re.findall(r"(?<![A-Za-z])(?:references|templates)/[A-Za-z0-9_.-]+\.md", text):
        if not (SKILL / rel).is_file():
            errors.append(f"Broken unquoted SKILL.md reference: {rel}")
    for p in SKILL.rglob("*.md"):
        if not p.read_text(encoding="utf-8").strip():
            errors.append(f"Empty skill file: {p.relative_to(SKILL)}")
    for phrase in ["not", "permissions", "hypothesis", "TASK_SOURCE_ROUTER.md"]:
        if phrase.lower() not in text.lower():
            errors.append(f"Missing guard/discovery phrase from SKILL: {phrase}")
    return sorted(set(errors))


if __name__ == "__main__":
    issues = check()
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        sys.exit(1)
    print("PASS: Elite UX Director local package structure and frontmatter checked.")
    print("Not tested: Claude invocation, UX outcomes, accessibility, link reachability, source rights.")
