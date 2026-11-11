# Research 009 — Complementing Anthropic frontend-design

Date: 2026-11-11. Sources:
- https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

## Key finding
Official frontend-design already contains thoughtful anti-template aesthetic direction, typography/palette/layout planning, interface writing, restrained motion, mobile/focus/reduced-motion requirements and self-critique. It flags familiar AI design tells: warm paper/serif/terracotta, acid-on-dark, broadsheet rules, identical cards and unnecessary labels/arrows. Do NOT falsely present these ideas as unique to our skill.

## Differentiated responsibility
**Creative Intelligence Lab (upstream and downstream):** grounded research selection, cultural/artistic context, three conceptually different design theses, precise brief and decisions, evidence/rights provenance, independent critique, and accumulated learning from failures.

**Anthropic frontend-design (implementation):** turn the authorized design brief into responsive, expressive frontend code; self-critique, meaningful microcopy, test and report observable results.

**Owner:** final creative and production authority. Claude's current Faneqo work must not be interrupted.

## Working sequence
Research and context -> creative thesis and three alternatives -> owner-approved or clearly provisional choice -> implementation by Claude with frontend-design -> actual screenshots and UX checks -> independent ChatGPT critique -> revision -> owner review.

## What to remove from our skill
Repeated instructions to be bold, avoid generic gradients/cards, choose type and palettes or simply polish frontend. Anthropic already says these things. Replace them with source-specific references, conditional principles, evidence levels, documented counterexamples and a decision ledger.

## Risk: two contradictory art directors
When both skills are used, our approved brief establishes constraints and specific creative direction. Official skill fills implementation freedom rather than reselecting an unrelated visual style. If the briefs disagree, surface conflict; do not silently override. Priority: owner instruction > approved project brief > actual product requirements > accessibility/interaction essentials > compatible skill heuristics > default aesthetic preferences.

## Honest self-critique
Our own Signal Archive prototype has off-white paper, a large Georgia serif headline, uppercase metadata and repeated cards—the very defaults Anthropic warns about. The archival context may justify some choices, but we have not proven they are original. This is a source-code-based critique, not a browser screenshot audit.

## Proposed discriminating test
Later, with owner permission, compare a baseline generated using the official frontend skill alone against an artifact generated with the same implementation skill plus our research/brief layer. Keep scope and content equal. Compare task clarity, visual distinctiveness, responsive behavior, user understanding, implementation effort and reviewer agreement. Our method must earn its place.

## Evidence limits
This is based on the written official instructions. We have not installed, executed, or compared both skills in Claude Code. Revisit source version before the real test.
