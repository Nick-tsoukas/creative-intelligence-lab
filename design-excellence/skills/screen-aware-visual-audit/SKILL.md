---
name: screen-aware-visual-audit
description: Visually audit an existing web/mobile screenshot and produce implementation-ready Nuxt/Vue direction grounded in the screen's real code, data fields, actions, and server permissions. Use for major visual redesigns or when asked whether a screen looks excellent. This skill is an isolated CANDIDATE and must not be auto-installed over other design skills.
---

# Screen-Aware Visual Audit — Candidate skill (NOT installed)

**Scope:** diagnostic review and a *reviewable* handoff. No UI code edits, production deployment, backend permission changes, screenshots uploaded to Git, or model training. Works as a focused add-on to the existing UX Director, Creative Design Director and Anthropic frontend-design expertise. Do not duplicate their full methods.

## Entry conditions

For a real audit require an existing screen/capture that can be OPENED visually, its intended audience and task, and authorized access to the relevant code if implementation feasibility is requested. If screenshot pixels are unavailable, provide a **limited source-code/requirements critique** and clearly state no visual audit occurred.

Avoid invoking for pure backend/CI/auth bugs or trivial CSS changes.

## Step 1 — Establish truth, without hallucinating product functionality

- Identify route, actor, user job, environment and current feature/state.
- Read the actual selected Vue SFC plus only task-relevant composables, components and stores. Keep source reads bounded.
- Run `design-excellence/screen_intelligence.py` when available to generate a **static hint** inventory.
- When available, examine selected Strapi content-type `schema.json` files, controllers, policies and permission tests. A schema reveals possible fields, **not** their API availability or access rights.
- For important fields/actions, independently confirm actual names/shapes, state lifecycle and server ownership from code or authorized dev tests. Use `examples/screen-contract.example.json` only as a shape guide; never repeat its invented fields as real app facts.
- Record missing permissions and data as `UNKNOWN`, not allowed by default. Do not invent functioning media players, share links, statistics, uploads or publications.

## Step 2 — Visual-only critique of ACTUAL pixels

- Locate the privacy-reviewed existing screenshot from Visual Memory; open it with the agent's image-capable viewer. Screen labels/source code do not count as observed pixels.
- Use `design-excellence/visual_audit.py prompt` for a scoped visual brief. Examine precise composition, focal weight, negative-space rhythm, typography/line breaks, image crop/light/identity, palette, affordance visibility and finishing detail.
- Compare the exact viewport and content state. An attractive desktop screenshot cannot establish good mobile design; inspect separate small-screen captures.
- Prioritize at most five **concrete** visual defects with exact visible evidence and a better compositional treatment. Distinguish aesthetic preference, observed defect and unknown interaction.
- Use `visual_audit.py observe --pixels-inspected` only after actual pixel inspection. For owner-only reports, use `OWNER_REPORTED`; for an unverified proposal, use `DESIGN_HYPOTHESIS`. Do not fake any observation.
- Remain critical of generic AI compositions, weak type hierarchy, crammed cards, fake media, meaningless gradients, gratuitous motion and decorative CTA clutter. But challenge clichés based on context, not blanket prohibitions.
- Do not reduce quality to a single aesthetic score; photography, composition, originality, accessibility and task success are separate.

## Step 3 — Convert critique into constrained creative direction

When a redesign is requested, produce **three substantially different artistic premises** using the SAME real data/actions/permissions. Distinguish narrative, focal system, typography, image treatments, spatial sequence, motion purpose and small-screen composition. Do not copy recognizable designs or unlicensed artist imagery from external examples. Keep at least one calm conventional task-first option.

Use the independent existing Atlas router for a few source-observed examples if the current task merits research; do **not** duplicate or edit that router's files.

## Step 4 — Compact implementation-ready handoff

Use `design-excellence/build_screen_handoff.py` if a local checkout exists. The handoff should carry:

- Observed screenshot ID, viewport and the *actual* five most consequential visual issues.
- Verified technical sources; data field and relationship matrix; read/write actions; editing/publication/visibility state; server permissions; unknowns.
- Approved brand/product invariants, rights constraints, selected artistic thesis and detailed responsive transformation.
- Which UI needs entirely new backend capability versus what can be built with existing fields.
- Image/media fallbacks, loading/error/retry, keyboard/zoom/reduced motion, low-end device tests.
- Original design examples as **mechanisms**, not tracing/copyrighted assets.
- Owner decision required before implementation. When owner feedback actually arrives, record it through the private `judgment_ledger.py`.

## Step 5 — Independent refinement after an authorized build

Only after an implementer has produced screenshots/actual interactions in an **explicitly authorized isolated worktree**:
1. Inspect 320/390/768/1440 and relevant editing/empty/error states.
2. Diagnose art direction and UX separately from browser/code correctness.
3. Request the few changes most likely to meaningfully increase craft.
4. Retake images, compare genuinely observed before/after, and get explicit owner approval.

Never claim world-class quality from passing syntax, no overflow, a high AI self-rating, or an impressive external reference. A design gets better through real judgment and repeatable revision.

## Referenced tools (load only when relevant)

- `design-excellence/VISUAL_AUDIT_PLAYBOOK.md`
- `design-excellence/SCREEN_INTELLIGENCE_PLAYBOOK.md`
- `design-excellence/INDEPENDENT_VISUAL_REVIEW.md`
- `design-excellence/IMPLEMENTATION_PLAN.md`
- Existing Lab `docs/PROJECT_DESIGN_PACKET_ROUTER.md`, `quality/BLIND_ART_DIRECTION_COMPARISON_PROTOCOL.md`, and the established live UX/Creative Director skill (do not replace it)

**Installation boundary:** This candidate is stored only in the isolated Git branch. Confirm the canonical active v5.0 installation and avoid introducing a second always-active art director without owner-reviewed role boundaries.
