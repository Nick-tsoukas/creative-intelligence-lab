# Masterpiece Atlas — Art-to-Interface Research (Increment 001)

**Date:** 2026-11-15. **Status:** Eight artwork/architecture/identity source-grounded first-pass studies with image-preview inspection; **not** eight exhaustive art-historical monographs, complete digital-website audits, or claims of observed user eye-tracking. All images remain at institutional/creator sources and are **not copied into this repo**.

## Purpose
Turn exact works into **original, conditional mechanisms** for digital experience art direction. Do not use famous artists as endorsements, copy identifiable styles, or conflate museum scholarship with UX evidence.

**Source of truth:** the artist/institution object record + the particular representation visibly inspected + contextual primary commentary, with each kept distinct. A visually inspected low-resolution thumbnail counts as *preview-observed*, NOT full-resolution figure studied. A written curator description does not make unseen visual details personally observed.

## Selection / retrieval
From this repository root:
```bash
python3 scripts/query_masterpiece_atlas.py list
python3 scripts/query_masterpiece_atlas.py search "rhythm"
python3 scripts/query_masterpiece_atlas.py show MA-002
```
Commands are local, read-only, standard-library-only, return bounded text, and never auto-fetch remote images.

For an ordinary design task, choose **one** artwork mechanism, optionally compare a second one; stop reading when a meaningful direction is possible. For deeper research, open its linked original object record and images, verify edition and rights, and create a deeper dossier. Avoid growing SKILL.md to contain an atlas.

## Studies in Increment 001
| ID | Work / exact provider | Type | Source / image status | Proposed conditional mechanism |
|---|---|---|---|---|
| [MA-001](studies/MA-001-VERMEER-BALANCE.md) | Vermeer, *Woman Holding a Balance*, NGA | Painting | institution curatorial text + low-res external preview inspected | quiet axis, localized light and restrained emphasis |
| [MA-002](studies/MA-002-HOKUSAI-WAVE.md) | Hokusai, *Under the Wave off Kanagawa*, Met JP10 | Woodblock print | official Met image preview inspected | scale tension, restrained distant anchor and serial rhythm |
| [MA-003](studies/MA-003-HOPPER-NIGHTHAWKS.md) | Hopper, *Nighthawks*, Art Institute | Painting / spatial light | museum curatorial text + external thumbnail inspected | luminous threshold, visual separation and spatial storytelling |
| [MA-004](studies/MA-004-SCHER-SIMPATICO.md) | Scher, *Simpatico*, Public Theater | Graphic design / typography | museum store poster preview + Pentagram project context inspected | typographic personality with differentiated information hierarchy |
| [MA-005](studies/MA-005-ALBERS-LIGHT-RISING.md) | Albers, *Study for Homage to the Square: Light Rising*, NGA | Color painting | NGA record + cropped image preview inspected | relative color/context and nesting; no standalone color formulas |
| [MA-006](studies/MA-006-ANDO-CHURCH-OF-LIGHT.md) | Ando, *Church of the Light*, Ibaraki | Architecture / light / sequence | architect-authored primary account + editorial photo preview | arrival, contrast and controlled reveal; no forced scrolling |
| [MA-007](studies/MA-007-PARKS-AMERICAN-GOTHIC.md) | Parks, *American Gothic*, Washington, D.C. | Photography / identity / ethics | foundation/LOC context and museum print preview | real human context before symbolic visual treatment |
| [MA-008](studies/MA-008-REID-MILES-OUT-TO-LUNCH.md) | Reid Miles, *Out to Lunch!* sleeve | Music / typography / photography | Blue Note label history + original-cover collector preview | content-specific imagery with typographic truth; no copied record-label aesthetic |

## Status taxonomy
- `OBJECT_IDENTIFIED`: correct institutional title/author/accession.
- `PREVIEW_OBSERVED`: specific accessible image/crop seen, but full original detail or edition not verified.
- `PRIMARY_CONTEXT_READ`: original institution/creator account read, with conflicting interpretations kept.
- `DEEP_VISUAL_STUDY`: high-quality complete work inspected and detailed visual mechanics documented.
- `MULTI_WORK_COMPARISON`: source-verified relation among multiple works.
- `DIGITAL_TRANSFER_PROPOSED`: original UI exercise/hypothesis (not proof).
- `BROWSER_EXERCISE_RUN` / `HUMAN_OUTCOME_OBSERVED`: evidence captured, not currently achieved.

All eight initial cards are **object identified + preview-observed + primary context read where noted + digital transfer proposed**. None is promoted to full complete visual study or measured UX result.

## Required critique separation
1. What image pixels can actually be seen (avoid inventing missing edges).
2. What author, curator, or museum says.
3. What we interpret, with credible alternative.
4. Mechanism in original medium.
5. **Conditional** transfer to digital expression.
6. Counterexample, harm, rights, responsive/mobile constraints.
7. Original exercise and measurable acceptance question—not made-up success.

## Expressive versus utility
The same identity may use expressive image/narrative composition for public storytelling and restrained, unmistakable controls for operational use. They must share recognizable design grammar (typographic family, content voice, color semantics, geometry), not become unrelated brands. A poster's typographic bravado is **not** permission to obscure form labels or critical message statuses.

## Integration safeguard — v5.0 compatibility
The user's separate handoff refers to a **v5.0 UX/Design system** but does not identify an accessible branch/path in this repository. At this GitHub snapshot, `skills/creative-design-director/SKILL.md` is **alpha v0.3** and `skills/elite-ux-director/SKILL.md` is **v0.5**, not v5.0. The Atlas therefore lives as **additive, independently retrievable research**. Do not replace an unknown newer skill with either older entrypoint. An existing v5.0 integration can read this index as an optional research source when its actual path is confirmed.

## Rights
Links and original commentary only. Museum image permissions vary; the Met explicitly marks its Hokusai JP10 image public domain, but this does not grant unrestricted reuse of third-party website screenshots or the actual creative identity. No unlicensed image assets are committed. Check individual rights before reproducing photographs, posters or branding.


## Increment 002 — From referenced masterpieces to tested compositions (2026-11-15)
- Deepened the *textual/institutional source reading* of Vermeer MA-001 and Hokusai MA-002, while keeping the original images at **preview-observed**, not full-resolution examined: `../../research/015-SOURCE_CRITICAL_COMPOSITION-VERMEER-HOKUSAI.md`.
- Added a method for relative color, expressive-versus-utility typography and **actual WCAG 2.2 technical constraints**: `../../research/016-COLOR-TYPE-CRAFT-AND-ACCESSIBILITY.md`. It does **not** claim full reading of Yale's paid Albers digital edition.
- Produced an original *same copy, 3 compositions* studio at `../../experiments/004-visual-grammar-studio/`, with separate browser QA; no external artwork/copyrighted asset copies.
- Task-first reading and counterexample guide: `../../handbook/VISUAL_DIRECTION_TASK_ROUTER.md`.
