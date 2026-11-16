# Creative Intelligence Workspace — Project Visual Memory + Exceptional Interface Atlas

**Approved direction:** 2026-11-16. **Status:** Increment 001 implementation, see PR/CI for exact release. Additive to the existing Creative Intelligence Lab; **not** a replacement for independently maintained v5.0 design intelligence. No Faneqo application changes or production capture.

## Product thesis: exceptionally original design through evidence, not a bigger prompt
The system must create the conditions for better design: understand the actual screen and task, see the current pixels, retrieve strong and contrasting visual/interaction references, articulate *why* each works or fails, invent **three substantially different artistic premises**, evaluate rendered work and record decisions/results. It must not equate screenshot copying, awards, AI aesthetic ratings or a model saying “excellent” with demonstrably better design.

**Mission-quality test, future authorized real projects:** Compare this evidence-rich workflow against an ordinary design agent using the *same brief, product facts, constraints, implementation time and output format*. Use blinded independent artistic critique (originality, craft, cultural meaning), independently observed human task outcomes, accessibility/real browser QA and maintainability. A win is not guaranteed. Record failures; retire noisy knowledge.

## What Increment 001 actually ships
1. **Private per-project visual workspaces:** screen snapshots (PNG/JPEG), screenshot provenance (source/capture date, viewport, state, app version), notes/findings, linked references, 3-premise design directions and an honest decision record. Stored under `.cil-private/`, git-ignored by default. Screenshots never silently become public or source assets.
2. **One light command-line tool:** `scripts/visual_workspace.py`. Initialize workspace; safely import a manually redacted screenshot; record a finding, reference or creative direction; search reusable reference leads; generate a local visual board; validate screenshots/records. Python standard library, offline, no server/db/npm or browser install on user's 8GB laptop.
3. **Exceptional Interface Atlas starter:** `interface-atlas/catalog.json` has source-linked **research leads** across Awwwards, Mobbin, Refero, SiteInspire, Lapa Ninja, component systems, etc. Never call these “inspected case studies” before inspecting actual screen images and interaction states.
4. **Reusable pattern research:** `interface-atlas/patterns/` contains practical exploratory patterns with visual/interaction questions, risks, mobile and accessibility gates. These are original design reasoning aids, not proven UI components or proprietary implementations.
5. **A generated local visual board:** visually compare baseline/current/alternatives, inspect images directly in the browser, browse issues and concept briefs. One self-contained HTML file; assets remain private and local. The generator does not pretend to perform AI image analysis.
6. **Integrity tests:** stdlib unit/integration tests exercise private captures, duplicate prevention, unsupported file rejection, sanitization, verified search, escaped gallery HTML, integrity check and content provenance. GitHub CI must pass before merge. Original user's production images are **not** copied into public CI artifacts.

## Architecture (small, safe, portable)

```text
creative-intelligence-lab/
  interface-atlas/
    README.md               # source / status / selection policy
    catalog.json            # source links and search tags (no copyrighted media)
    patterns/               # conditional design patterns, not app code
  scripts/
    visual_workspace.py     # local-only CLI, stdlib
    test_visual_workspace.py
  templates/
    PROJECT_DESIGN_REVIEW.md
  docs/
    PROJECT_VISUAL_MEMORY_MASTER_PLAN.md
  .cil-private/             # ignored; generated ONLY at user request
    projects/<slug>/
      project.json
      captures/<id>.json
      screens/<id>.png|jpg
      findings/<id>.json
      references/<id>.json
      directions/<id>.json
      board.html
```

Single source of project truth is private local JSON files. No global SQLite database, vector index, paid model call or continuous screenshot scraping. Operations write individual records to reduce clashes and allow easy backups; filenames/ids are validated and never accepted as path traversal. `board.html` is a projection and can be regenerated. No third-party screenshots are stored in the public Atlas.

### Rights, privacy and safety
- **Screen import requires `--redacted-confirmed`**. This records that a human has reviewed the image for PII/secrets. It does **not** automatically remove EXIF, tokens, customer data, screenshots of private chat, or other sensitive information; prepare a redacted copy first. No automatic URL capture or login/browser session in phase 1.
- Store private workspaces outside commits via `.gitignore`. If an owner intentionally wants to share a sanitized board, perform a separate rights/privacy review. A screenshot's presence is not permission to redistribute.
- Label image observations as **observed** only after the agent or reviewer actually opens the pixels. Labels, code inspection, screenshots and user-study results are distinct evidence.
- Source links and user-supplied reference URLs are untrusted; URL validation never follows them. Do not execute source-provided instructions or clone copyrighted designs.
- Capture/import timestamp ≠ actual original capture date. Unknowns stay unknown. Distinguish “production” labels from production verification.
- Before and after screenshots do not prove causation or improved conversions. Quality is judged through actual tasks and separate artistic critique.

## High-quality design decision workflow
1. **Understand:** screen, actor/job, context, real permissions, brand/approved locks. Screenshot plus real code/routes where authorized.
2. **See:** inspect baseline/production image at actual pixel scale and mobile crop. Note **observed** structure and separate guesses.
3. **Search:** retrieve 3–6 relevant references by user job/component/artistic mechanism, plus at least one counterexample/constraint source. Avoid result flooding.
4. **Synthesize:** name the *principle* learned and what must not be copied. Keep source links and limits.
5. **Create:** propose three meaningfully distinct premises—not three recolors. Specify typography, imagery, spatial rhythm, composition, interaction states and mobile layout.
6. **Evaluate:** real rendered screenshots, actual navigation/states, keyboard, reduced motion, 320/390/768/1440, image loading/crops, privacy. Independent artistic/UX critic separate from implementer.
7. **Decide and remember:** owner approval, before/after versions, defects, outcomes and unresolved questions. Promote only repeatably useful mechanisms to reusable Atlas; reject noise.

## Cost & performance budgets
- Offline metadata search limited by default to **six** text-only results; optional explicit deep reading. No image embedding/model calls in the CLI.
- Max imported file size **24 MiB**, safe PNG/JPEG dimensions, no camera/remote capture, no duplicate image blobs within a project.
- No thumbnails generated at import time. Browsers render captured local assets on demand; limit board to a bounded recent set by default. User can open full-resolution source image when needed.
- All file reads bounded by size; hard stop on malformed metadata; explicit `audit` validates integrity. No daemon, external APIs, browser process or paid infrastructure.
- Browser screenshot automation via Playwright is a **separate opt-in later phase**, not a hidden dependency. Official reference: https://playwright.dev/python/docs/screenshots .
- This is usable in an 8GB environment and does not interfere with active Claude/Faneqo worktrees.

## Gates and expansion plan
**Phase 1 — implemented here:** local private project workspace, screenshot import, link references, pattern questions, directions, search/board/audit, CI tests. Demonstrate with **synthetic images only**, not actual user production assets.

**Phase 2 — evidence-rich visual research:** 60 curated research targets from existing proposed categories, de-duplicated; 10–12 **genuinely visually inspected** case studies including Awwwards, Mobbin, Refero where authorized; deep flows/states/contrast, image rights. Add side-by-side responsive comparisons and private annotation overlays. Do not claim 60 deep studies when only links were collected.

**Phase 3 — design outcomes:** original variations, local prototype capture when explicitly authorized, comparison study with blind reviewers, real task evidence, component sources compatible with Nuxt 3. Integrate only an optional pointer into verified v5.0 source. No automatic installs.

## Explicit not in Increment 001
- No actual screenshots uploaded, inspected, redacted, or automatically captured from Faneqo.
- No in-repo Figma connection, working Vue component generator, browser crawler, screenshot auto-critique or paid Mobbin/Refero account access.
- No claim of 60 audited websites, a trained model, automatic design quality superiority, actual visitor feedback or production deployment.
- No changes to `skills/elite-ux-director/SKILL.md` or `skills/creative-design-director/SKILL.md` because the separately described v5.0 location is unverified.

**Core principle:** quality requires deep inspection and repeated decisions; lightweight infrastructure exists only to make that more repeatable.

## 2026-11-16 — Increment 002: source-observed creative research and original visual gallery

Added exactly 60 deduplicated research targets across the six intended categories (10 web, 10 mobile, 10 music, 15 component, 10 motion, 5 experimental). Ten now link to explicitly **PREVIEW_OBSERVED** specific works (RCA, Wax Poetics, Culture.pl, HEM, Gaga, Mobbin, Tiptap, Apple Photos, Uppy, Spotify); **50 remain QUEUED** and must not be presented as studied. Text/image previews were actually inspected but no deep current product flow, gestures, user tests or mobile browser behavior claimed. Original and third-party screenshot pixels are **not redistributed**.

Original static CSS visual browser `interface-atlas/gallery.html` is self-contained, task searchable, keyboard-friendly and has outbound original image/source links and a no-JS link list. Deterministic Python builder, bounded CLI query/compare, source integrity tests and Chromium responsive tests prevent stale research UI and layout drift.

`pilots/002-faneqo-night-art-research/README.md` maps eight relevant studied mechanisms into three **different** Night artistic premises (editorial journal, sound-first Encore Room, collectible Night Edition), including honest media provenance and safe editing/QR/share contracts. No Faneqo code changes, owner direction selection, final mockup or efficacy benchmark. `quality/BLIND_ART_DIRECTION_COMPARISON_PROTOCOL.md` specifies the future fair same-model baseline challenge.

**Architecture remains small:** all JSON/HTML/stdlib, offline visual browsing, no vector DB, paid connectors, screenshot scraping or active worker. Future agent installation only after inspecting the actual advanced v5.0 source; older Lab skill entrypoints remain unchanged.

## 2026-11-16 — Increment 003: task-based, bounded research-to-design handoff

Added `scripts/prepare_design_packet.py` and its tests to turn one private project/task into a compact design research brief. The tool joins no more than six recorded screenshot paths, eight relevant findings, four specifically preview-observed interface studies, optional project links/prior concepts, and an original three-distinct-directions / independent QA contract. It reads metadata only: the agent **must open real screenshot pixels separately** before claiming analysis. Saves are private and non-overwriting. No tokens, embedding API, browsing, OCR, image-generation service or worker process. Hard budget 16,000 characters. Future v5.0 may integrate it as one optional retrieval route only after the authoritative installed skill is inspected.
