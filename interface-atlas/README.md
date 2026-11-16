# Exceptional Interface Atlas — Curated References & Patterns

**Increment 001:** source-linked, searchable *research leads* and original design-analysis patterns. This is not yet a visual capture service, a clone engine, 60 visually audited case studies, or proof of design outcomes.

**Architecture:** `catalog.json` holds URL, reference type, tags, the design problem it may illuminate, why it warrants **future inspection**, evidence status and rights caution. Screenshots and author-specific project evidence are stored ONLY in the ignored `.cil-private/` project workspace and remain distinct from public library records.

Source types: `web` (editorial/visual web), `mobile` (real app/flow libraries), `component` (official component/code docs), `motion` (interaction examples), `research` (standards/method). A source hub is not an individual checked product case study.

See the task-oriented patterns:
- `patterns/inline-editor.md` — writing, selection, autosave, explicit publishing
- `patterns/media-upload.md` — adding video/audio/photo with progress/visibility constraints
- `patterns/photography-gallery.md` — curated image storytelling + mobile navigation
- `patterns/share-and-qr.md` — URL, QR, sharing, destination integrity

These are original reasoning patterns, not copyrighted third-party example collections.

## From source lead to genuine case study
A source reaches `VISUALLY_INSPECTED` only after a named work/screen is actually opened and observed, with dated viewport/provenance and limitations. `FLOW_TESTED` requires real interactions and states, not just pictures. `USER_EVALUATED` requires real user outcomes, not self-scored aesthetics. Increment 001 intentionally uses `LINK_ONLY`.

## Retrieval
```bash
python scripts/visual_workspace.py find --query "editor gallery"
python scripts/visual_workspace.py find --query "mobile upload"
```
The search returns brief, bounded, evidence-labeled source links. A research agent opens chosen sources, actually examines pixels/flows with an authorized browser or visual tool, and records a limited case study. Link-only results **must not be described as observed examples**.

## Related existing knowledge
- `visual-library/masterpiece-atlas` — primary artwork and architecture, preview-observed image studies
- `web-design/experience-atlas.md` — earlier digital research leads and partial studies
- `handbook/VISUAL_DIRECTION_TASK_ROUTER.md` — selective art-direction methods
- `docs/V5_ART_DIRECTION_INTEGRATION_AUDIT.md` — preserve the separate advanced v5.0 system

## Rights & credentials
Awwwards, Mobbin and Refero each have their own terms and entitlements. No bypass, mass scraping, exporting screenshots or credential harvesting. A URL is a locator, not a reuse grant. Official Nuxt UI, Reka UI and W3C design patterns may provide implementation-friendly analogues, still subject to the source's license and semantic requirements.

## Increment 002 — Actual preview-observed cases + original visual browser (2026-11-16)

The source-hub catalog (`catalog.json`, 20 general library/doc sources) remains separate from **60 individual research targets** in `research-targets.json`. Exactly ten specific digital works/screens have been visually inspected *at accessible preview resolution*: `observed-cases.json` EI-001..EI-010, with exact source image URL, direct observation, cited work source, transfer hypothesis, counterexample, rights and time/interaction limits. The other 50 targets are `QUEUED_FOR_RESEARCH`—not audited examples, nor verified as current.

**Visual browsing:** open `gallery.html` directly in your browser. Its ten original CSS diagrams convey different visual *ideas* and link to the actual reference preview and original work. The gallery does not hotlink, embed or host copyrighted screenshot pixels; links are outbound. Click "Actual observation, limitations & application" to read evidence. Filter by web, mobile, component or music; local search requires no server/API. JavaScript-disabled readers still get ten source links.

**Claude/ChatGPT research retrieval:**
```bash
python scripts/query_interface_atlas.py search "music gallery"
python scripts/query_interface_atlas.py show EI-002
python scripts/query_interface_atlas.py compare EI-002 EI-008
python scripts/query_interface_atlas.py targets "audio"
python scripts/build_interface_gallery.py --check
```
Retrieve 2–4 relevant specific studies for a substantial design task, not the whole 60. Never convert `PREVIEW_OBSERVED` into "flow tested"; choose a real app browser session for actual behavior. Contribute specific observations and failures to the current project workspace, not a fictional global user-study score.

**Pilot:** `../pilots/002-faneqo-night-art-research/README.md` uses actual observed source mechanisms to develop three original Night Recap art directions; no Faneqo application code modified. **Fair comparison protocol:** `../quality/BLIND_ART_DIRECTION_COMPARISON_PROTOCOL.md`, not yet run.
