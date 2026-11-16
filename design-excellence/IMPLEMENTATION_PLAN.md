# Creative Intelligence Lab — Design Excellence Implementation Program

**Created:** 2026-11-16  
**Purpose:** Increase the quality of *actual* visually rendered, useful, culturally meaningful digital products—not just produce more research pages or screenshots.  
**Status:** Phase 1 isolated tool started on `feature/creative-judgment-ledger-20261116`. No skill installed and no production files modified.

## Nonnegotiable coexistence rules

1. The other session owns `feature/interface-atlas-observed-studies-v02-20261116` and its `interface-atlas/`, `scripts/query_interface_atlas.py`, gallery, and Faneqo Night research. **Do not edit those files or branches here.**
2. This program owns only the new `design-excellence/` directory on its dedicated branch. Do not modify existing skill entrypoints, `README.md`, `docs/STATUS.md`, `CHANGELOG.md`, project visual memory scripts or Faneqo repositories.
3. The separately reported advanced v5.0 skill is **not verified locally** by this branch; do not install older alpha versions over it.
4. No user screenshots, private artist media, user identifiers, secrets or external copyrighted images committed. Design-feedback records default to the already git-ignored `.cil-private/` path. Never equate any `OWNER_FEEDBACK` label with verified identity; the label is entered by the record author.
5. No merge, deployment or changes to Faneqo without separate authorization. Review and reconcile this branch **after** the Atlas work settles.

## Why these upgrades (priority by leverage, not feature count)

The Lab already has source literacy, initial interface images, UX and art-direction skills, a private screenshot workspace and isolated browser experiments. Weaknesses lie in contextual selection, stable human taste capture, rendered critique depth and transfer from research to actual decisions. This plan improves those with small, inspectable mechanisms before introducing costly models, vector databases, browser daemons, or new frameworks.

### Phase 0 — Protect concurrent work (complete)

- Review branch names and differences against main; confirm Atlas v02 active and separate visual-memory work.
- Create independent `feature/creative-judgment-ledger-20261116` branch based on main; restrict writes to `design-excellence/`.
- No changes to `interface-atlas/`, project screenshot import/board, existing skills or domain adapters.

### Phase 1 — Creative Judgment / Taste Memory (started)

**Deliverable:** `design-excellence/judgment_ledger.py`, tests, and this runbook.

Each **explicit** judgment records candidate/screen ID, decision (APPROVE/REVISE/REJECT), axis, observable concern, reason, next design move, evidence level, provenance, context and optional superseded record. Records are immutable local JSON documents; a correction appends a new record. Export a bounded owner-feedback-only design brief, with separate opt-in inclusion of agent observations/hypotheses. Never train models, infer hidden preferences, or use an average score as aesthetic authority.

**Quality gate:** standard-library-only unit tests; IDs/path traversal rejected, duplicates rejected, supersession recoverable, no mixing AI hypothesis into owner taste, no file created by read, corrupt files detected. Run using `python -m unittest discover -s design-excellence -p "test_*.py" -v`. Validate after checkout in a compatible Python environment.

**Do not:** automatically transfer private data between projects, fabricate owner feedback or alter Atlas schema. Integration will use the optional Markdown/JSON `brief` output after explicit user review.

### Phase 2 — Deep Visual Inspection (depends on Atlas v02 completion)

Upgrade a small sample (8–12) of named reference screens from `PREVIEW_OBSERVED` to full annotated study **only when actual pixels and permissions are available**. Measure: hierarchy, photographic focal point/crop, type roles, spatial rhythm, interaction states, responsive recomposition, motion purpose and source specificity.

- Store observation separate from interpretation and from imitation risk.
- Include one *failure or counterexample* per admired design.
- Source real state sequences rather than believing a polished screenshot reveals interaction quality.
- Output actionable art-direction mechanisms keyed to task and audience.

**Gate:** each case has named screen, dated provenance and viewport, direct visible evidence, accessibility/interaction limits, and a credible application hypothesis. Rights checked. Do not claim live interaction testing for screenshots.

### Phase 3 — Contrasting Creative Exploration

On one approved isolated prototype, hold real task/copy/content/permissions constant. Produce three **different premises** (e.g. editorial story, immersive media, collectible artifact), not three colored copies. For each capture image hierarchy, typography, photography, pacing, motion and small-screen composition. Always preserve useful primary actions.

**Gate:** independent owner selection, documented rejected concepts with reasons, no fabricated metrics. Faneqo production code untouched.

### Phase 4 — Visual Finishing Studio

Build a critique protocol around *rendered* desktop (1440), tablet (768), mobile (390) and narrow mobile (320). Inspect content-specific photo crops, image licensing, whitespace, type wraps, focal order, reading pace, interaction/motion purpose, keyboard/focus, empty/slow/error states, reduced motion and low-end performance. Keep art direction, task effectiveness and engineering quality as separate axes.

**Gate:** side-by-side screenshots plus a small ranked defect list with precise next corrections and repeat captures. Zero-overflow/JS-error checks alone are not proof of aesthetics.

### Phase 5 — Experience and Ritual Design

Study what makes high-quality products emotionally memorable *and* usable: concert archives, fan memory practices, interactive photo essays, personal year-in-review formats and artist-controlled identity. Research with real creators/fans where feasible.

**Gate:** one prioritized feature thesis for Night Recap or another user-approved surface, including actor, emotional job, affordance, recovery, trust/rights implications and measurable observation. Do not build speculative Faneqo features without a product brief.

### Phase 6 — Design Learning Loop

Link decisions to candidate screenshots, optional Atlas reference IDs, approval/rejection history, design defects and observed results; select the smallest relevant research set for a new brief. Periodically review and retire unhelpful rules.

**Gate:** can a fresh session explain *why* a previous design was rejected and produce a materially better revision without replaying old mistakes? If not, simplify rather than adding prompts or more tools.

## Evaluation and exit criteria

No model-generated quality score certifies originality. Compare ordinary agent workflow with Lab-assisted workflow on the **same real content, scope and implementation budget** when explicitly authorized. Look at: independent visual/art judgment, owner preference and reasons, first-glance comprehension, task success, accessibility, privacy/rights and maintainability. Keep independent tests distinct from personal taste.

**Near-term finish line:** an operational and testable private feedback ledger, one real owner-approved design review example, and a bounded design handoff. No need to run expensive models or store proprietary screen content in GitHub.

## Integration only after concurrent feature stabilizes

1. Review current latest Atlas feature branch, verify merged state and resolve duplicate schema fields.
2. Confirm canonical v5.0 file paths with the other session before changing any skill.
3. Add one *optional on-demand* instruction to query project-specific owner feedback from the private ledger; do not paste all records into the system prompt.
4. Keep the Atlas's source images and screenshot evidence distinct from this ledger's authored judgments.
5. Test actual end-to-end use with a single real owner-approved screenshot review and revise the tool from feedback.
6. Merge this branch only after owner review and CI/local tests; there is no auto-merge or deployment in this program.

## First review scenario

Faneqo Night Recap: only when the owner supplies or authorizes a sanitized current screenshot, record the specific reason they accept/reject a candidate, e.g. spatial breathing room, artist photo dominance, legibility of audio actions. Use an actual candidate ID and faithful quoted/paraphrased reason; do not claim a synthetic example was witnessed feedback.
