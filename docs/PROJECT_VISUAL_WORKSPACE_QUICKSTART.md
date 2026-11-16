# Project Visual Memory — Fast Start (Private and Offline)

**Scope:** this tool **organizes and displays evidence**. It does not automatically capture live sites, inspect pixels with an AI vision model, redraw an interface, test user tasks, or establish copyright permission. Creative Intelligence Lab remains a source-grounded design research and critique system.

## Requirements
- Python **3.12+** (stdlib only). On the user's 8 GB Windows machine, WSL Python is fine.
- Run in `creative-intelligence-lab` repo; no NPM install, browser server, database, Node process, external API or credentials.
- Use real screenshots **only after creating a manually redacted local copy**. The `--redacted-confirmed` switch is your assertion, **not** automatic redaction. Keep customer names, email addresses, private fan media, account details, access tokens, analytics secrets and connected logins out of captures.

## Step 1 — Project context
```bash
python scripts/visual_workspace.py init-project \
  --project faneqo-night --title "Faneqo — Night Recap" \
  --goal "A deeply emotional, visually outstanding Night with clear safe editing"
```
This creates `.cil-private/projects/faneqo-night/project.json`. The entire `.cil-private/` directory is git-ignored.

## Step 2 — Import existing screenshot
Create a **sanitized copy** yourself first; the tool does not modify the image to hide sensitive information.
```bash
python scripts/visual_workspace.py add-screen \
  --project faneqo-night --id night-baseline-mobile \
  --file /path/to/sanitized-night.png --label "Current Night, mobile" \
  --role baseline --state "artist-view" \
  --viewport-width 390 --viewport-height 844 \
  --redacted-confirmed
```
The tool saves a copy, records pixel dimensions, SHA-256, import date, and the optional actual screenshot capture date you explicitly supply via `--captured-at YYYY-MM-DD`. It **does not** call it a visually studied image.

For before/after comparison, import another distinct image with `--role candidate`, using an independent ID. Never overwrite the baseline.

## Step 3 — Record a real problem
```bash
python scripts/visual_workspace.py add-finding \
  --project faneqo-night --id weak-media-choices \
  --screen night-baseline-mobile \
  --statement "Media source actions lack clear recognizable iconography" \
  --severity major --evidence USER_REPORTED \
  --outcome "One readable, direct route to audio/video/photo/links"
```
If an agent actually opens the screenshot and sees the problem, use `--evidence IMAGE_OBSERVED --pixels-inspected` only for a genuine pixel observation. Screenshots never prove that back-end behavior works.

## Step 4 — Discover relevant inspiration
```bash
python scripts/visual_workspace.py find --query "mobile upload"
python scripts/visual_workspace.py find --query "editor gallery"
python scripts/visual_workspace.py find --query "creative editorial"
```
Results are **LINK_ONLY** source directories or official documentation, not automatically visually inspected references. Inspect the exact source screens and compare actual interaction patterns before asserting lessons.

Save a source relevant to this project:
```bash
python scripts/visual_workspace.py add-reference \
  --project faneqo-night --id photo-editorial-source \
  --title "SiteInspire visual gallery" --url https://www.siteinspire.com/ \
  --kind web --tags "editorial,photography" \
  --why "Find a composition mechanism that gives one photo meaning"
```

## Step 5 — Create distinct visual premises
```bash
python scripts/visual_workspace.py add-direction \
  --project faneqo-night --id documentary-night \
  --name "The concert documentary" \
  --thesis "The audience enters a real recorded performance and its aftermath" \
  --difference "Immersive photograph followed by spare editorial chapters, not a card grid" \
  --references "photo-editorial-source" \
  --preserve "Existing artist page, permission rules, and QR behavior" \
  --risk "Heavy media cannot hide the primary edit and share actions"
```
The record remains `UNAPPROVED_CONCEPT`. It cannot auto-publish or overwrite any existing project.

## Step 6 — View the project visually
```bash
python scripts/visual_workspace.py board --project faneqo-night
python scripts/visual_workspace.py report --project faneqo-night
python scripts/visual_workspace.py audit --project faneqo-night
```
Open `.cil-private/projects/faneqo-night/board.html` locally in a browser. No network scripts; the board links screenshots to original local files. For true side-by-side screenshots use:
```bash
python scripts/visual_workspace.py board --project faneqo-night \
  --before night-baseline-mobile --after candidate-mobile
```

## How the AI makes use of it
1. Load the **bounded** report from `report`, then actually open the relevant images with image-capable tools. A text metadata listing is not visual evidence.
2. Search two or three sources and inspect only relevant full screen/flow examples. Do not copy pixels or proprietary design.
3. Write a three-premise direction packet using `templates/PROJECT_VISUAL_REVIEW.md`. Align with actual product routes, data rights, authentic imagery, contrast, mobile reflow and user intent.
4. If code changes are separately authorized, let the implementing agent work in an isolated worktree. Record snapshots from real browser screens afterward, test tasks, and produce a transparent critique.
5. Preserve original baseline and rejected directions. Reviewer/owner approvals and real user outcomes require **separate explicit evidence**; the CLI does not manufacture them.

## Upgrades deliberately deferred
Automated authenticated production captures, screenshot annotations, browser instrumentation, OCR/embeddings/vector search, database UI, live Figma synchronization, and paid Mobbin/Refero MCP accounts. They are unnecessary for the initial quality loop and would add memory, privacy and maintenance burden. Playwright's official screenshot documentation is at https://playwright.dev/python/docs/screenshots.

## Version / safe integration
The source GitHub repository currently contains older skill entrypoints than the separately reported advanced v5.0 installation. **Do not copy those older entrypoints over v5.0**. The workspace and Atlas are optional independent tools; a future integrator may add one pointer from the verified active v5.0 source to this quickstart and Atlas.

## Faster research-to-design handoff (2026-11-16)

Once a project contains manually redacted screen captures and user-reported/observed findings, the Lab can build one **bounded source-grounded art-direction packet** for Claude or ChatGPT:

    python scripts/prepare_design_packet.py --project faneqo-night --task "create a breathtaking, usable Night Recap media gallery"
    python scripts/prepare_design_packet.py --project faneqo-night --task "simplify audio upload" --screen night-baseline-mobile --save audio-brief-001

The packet contains private screenshot paths (you still must **actually open the pixels**), up to eight screen-specific findings, and up to four concrete preview-observed external studies with their original URLs, detailed visual analysis, counterexamples and non-copying directions. It does not run an AI model, invent source visuals, approve a design or edit Faneqo. File stays under `.cil-private/projects/<project>/research-packets/` with no overwrite. See `docs/PROJECT_DESIGN_PACKET_ROUTER.md`.
