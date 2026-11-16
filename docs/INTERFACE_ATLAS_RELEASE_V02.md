# Exceptional Interface Atlas — Source-Observed Visual Research Release 002

**Date:** 2026-11-16. **Change boundary:** research, source metadata, original HTML/CSS schematic gallery, scripts/tests, and the Faneqo-independent pilot brief only. The separate advanced v5.0 skill is NOT installed or modified. No production Faneqo repo touched.

## New, actually implemented
- **Ten specific externally source-linked screenshots** were visually inspected through public previews. Each observed case records exact image URL and original product/project, what was actually seen, why the design might be useful, its failure conditions, one original composition exercise, and copyright/interaction limits. See \`interface-atlas/observed-cases.json\` (EI-001..EI-010).
- **60 research targets**, exactly 10 web / 10 mobile / 10 music / 15 components / 10 motion / 5 experimental, in \`interface-atlas/research-targets.json\`. **50 QUEUED** uninspected targets; **10 PREVIEW_OBSERVED** entries linked to cases. These targets are leads, not 60 observed works or verified deep links to app screenshots.
- New offline visual browser \`interface-atlas/gallery.html\`: curated original interpretive visual **schematics**, grouped/sorted by web/mobile/component/music with instant local filtering and details. Links open actual screenshot pixels at **the source host** or the creator's page. There are **no external image assets loaded or copied into GitHub**; illustrations are original CSS, not screenshot reproductions. Responsive design expected at 320/390/768/1440 after CI.
- \`scripts/query_interface_atlas.py\`: \`search\`, \`show EI-###\`, \`compare EI-### EI-###\`, \`targets\`. Standard library only; returns bounded, source-verified notes, no semantic model calls or hidden purchase.
- \`scripts/build_interface_gallery.py\`: rebuilds a deterministic, safe data-embedded standalone HTML page without a network call. Use \`--check\` in CI to prevent stale gallery source.
- Structural/source integrity tests and actual Chromium visual browser checks using self-drawn schematics. They do NOT prove user research, art direction quality or original apps' usability.
- Pilot plan \`pilots/002-faneqo-night-art-research/README.md\`: applies specific source mechanisms to three genuinely different Night Recap directions without changing actual app or publishing mock statistics.

## Correct interpretation of the first studies
EI-001 RCA Records Awwwards design; EI-002 Wax Poetics editorial; EI-003 Polish Electronic Music composition; EI-004 Dine HEM Records visual/player; EI-005 Yung Studio Lady Gaga; EI-006 Mobbin source search UI; EI-007 Tiptap editor illustration; EI-008 older Apple Photos Memories; EI-009 Uppy **2016 v0.8** uploader; EI-010 older/unknown-date third-party Spotify player screenshot.

**Important time-bound examples:** HEM relaunch on **August 20, 2025** means EI-004 original studio design is *not necessarily current*; see https://dinehq.com/news/relaunching-hem/. The uploaded Apple Photos 2021 UI and old Uppy release represent older versions, not current app behavior. The Lady Gaga studio discusses an evolving site/visual system; self-reported reach is not independently validated UX gain.

## Research-to-original-design workflow
1. Private workspace: \`python scripts/visual_workspace.py init-project ...\` and \`add-screen --redacted-confirmed\`.
2. Open the image pixels (not just file name) and note exact issues, confidence, unknown interactions.
3. \`python scripts/query_interface_atlas.py search "gallery media"\` and \`show EI-002\` / \`compare EI-002 EI-008\`.
4. From original work observation + human needs, develop 3 distinct artistic *premises*. Avoid replicating signature layout, brand art, music or copyrighted images.
5. Prototype only on authorized isolated branch/worktree; capture actual render and focus/disabled states; compare visual, task, accessibility and implementation separately. Record contradictory evidence and retire poor ideas.
6. Real person success and artistic excellence must be judged by human participants/reviewers, not fabricated from the screenshot library.

## To use locally
\`\`\`bash
python scripts/query_interface_atlas.py list
python scripts/query_interface_atlas.py search "music editor"
python scripts/query_interface_atlas.py compare EI-002 EI-008
python scripts/query_interface_atlas.py targets "upload"
python scripts/build_interface_gallery.py --check
\`\`\`
Open \`interface-atlas/gallery.html\` as a file in Edge/Chrome. This browser requires JavaScript for interactive cards/search but uses no external packages or network resources; a noscript note or static source-link fallback may be improved later.

## Non-goals and unanswered engineering questions
- No automatic remote website scraping, mass screenshot downloads, paywall bypass, privileged account access, authenticated production capture or Figma sync.
- No original copyrighted images served or embedded.
- No v5.0 installation, source modification or production product edits.
- Visual study ≠ keyboard/mobile/gesture flow testing; those require authorized live access.
- Quality advantage over unskilled AI **NOT TESTED**; future blinded before/after and independent art/UX critiques needed.
- 60 targets need independent source URL freshness checks and deeper actual work-level research, beginning with highest relevance and creator rights.

## Next short mission
Pick 2–3 high-value queued actual UI flows (e.g. editor on mobile, uploader under network error, media gallery with one hero). When authorized use direct product or connector access, create evidence of a state sequence rather than another beautiful still. The next substantive skill upgrade is **per-project reference selection tied to observed failures**, not collecting more random aesthetic examples.
