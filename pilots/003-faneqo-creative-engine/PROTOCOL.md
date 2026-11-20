# Pilot 003 — Creative Director × Faneqo Creative Engine

**Status:** Prepared, not executed. No Studio code or deployed behavior changed.

## Question

Does a small, research-aware direction adapter produce more distinctive, effective, editable Faneqo campaign concepts than the existing plain-language Codex workflow, without disproportionate time or token cost?

## Existing baseline

- Target: `Nick-tsoukas/musicbizqr`, Creative Engine v0.2, `scripts/creative-engine.mjs`.
- Brief: `design-references/creative-engine/your-music-your-world.md`; its three current directions are the comparison baseline, **not** a blinded generated control.
- Preserve the baseline Markdown, revision, assets and all available original PNGs. If original proof images are unavailable, rerender with the same checked-out revision and declare that substitution.

## Fair trial

1. Pin one Studio revision, template set, assets, campaign objective, output format, agent/model and generation budget. Capture the exact instructions for A (ordinary authoring) and B (this adapter). Do not give either condition the other's solution or critique.
2. Each condition authors exactly three valid concepts. Log actual model calls, token telemetry if available, wall time and implementer clarifications. Unknown metrics stay unknown.
3. Render each set through the **same** unmodified local `compose` command into fresh directories. Record parser failures, unsupported fields, render failures and any manual interventions.
4. Inspect the six full-size portrait exports and both comparison boards at phone scale. Evaluate concept distinctness, organizing idea, hierarchy, music authenticity, product truth, CTA and technical editability; separately note crop, legibility and asset rights. Prefer blind order/random labels for human selection.
5. Nick selects the strongest concept or rejects all. Record his reasons. The reviewer may identify specific defects but must not infer audience conversion from appearance.
6. Give each condition one bounded revision opportunity with equal time/call limits. Re-render and compare again. Preserve all earlier output directories.

## Decision rule

Keep the adapter only if it yields clearly more useful creative decisions or higher founder preference **without** unsafe claims, broken contracts or unacceptable overhead. If tied, simplify the instructions; if worse, revise or retire them. No subjective score alone proves effectiveness. No automatic `select` or `produce` before founder approval.

## Required evidence record

Revision SHAs; model and prompts; baseline/candidate Markdown; PNG locations; parser/render/test outcomes; blind preference and specific reasons; observed flaws and revision results; measured run time/tokens where available; rights status; unresolved limitations. A screenshot review is mandatory before any visual-quality claim.
