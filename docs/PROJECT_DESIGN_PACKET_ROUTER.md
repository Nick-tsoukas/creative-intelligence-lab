# Research-to-Design Packet Router — Creative Intelligence Lab

**2026-11-16.** A compact, optional orchestrator for design tasks. This is **not** a new Claude skill, a replacement for the separately maintained v5.0 design system, an AI vision model, an app deployment, or a browser capture service.

## What this solves
Our Lab now has:
- Project-specific **private** imported screenshots and first-hand notes (screenshots must be opened by a vision-capable agent; the CLI does not read pixels).
- Ten source-grounded **PREVIEW_OBSERVED** reference studies and 50 queued targets, plus the art-history Masterpiece Atlas.
- Art-direction methods and contrastive design research.

Without a small task router, Claude can still drown in research or forget source evidence. The new script chooses a maximum of **1–4 relevant inspected preview cases**, combines them with a bounded slice of one project's actual screen state and problems, and outputs one practical *research packet*. It intentionally does **not** pick a winning design.

## No dependencies, not even a server
Run from the Creative Intelligence Lab checkout, Python 3.12+ (WSL works):

    python scripts/visual_workspace.py init-project --project faneqo-night --title "Faneqo Night Recap" --goal "Beautiful, safe artist Night storytelling"

Once sanitized screenshots and evidence findings have been imported with the prior workspace tool:

    python scripts/prepare_design_packet.py --project faneqo-night --task "redesign the Night gallery with refined photographic storytelling"
    python scripts/prepare_design_packet.py --project faneqo-night --task "simplify adding audio and video" --screen night-baseline-mobile --max-cases 3
    python scripts/prepare_design_packet.py --project faneqo-night --task "editorial story writing flow" --save story-brief-001

The last command creates a file at:

    .cil-private/projects/faneqo-night/research-packets/story-brief-001.md

This stays **git-ignored and local**. Existing packet IDs cannot be overwritten. There is no paid model call, screenshot download, server, index daemon or package install.

## What it prints
1. Project name, goal, exact user task and explicitly unapproved research status.
2. No more than six imported screenshot paths, their recorded role/state, pixel dimensions, capture-date truth and visual-study status. The receiving agent must actually open the pixels to analyze them.
3. Up to eight findings tied specifically to the selected screen(s), with user-reported vs image-observed vs tested evidence labels.
4. Up to four task-matched image-preview case studies: original work and image URLs, visually observed details, transferable mechanisms, counterexamples, copyright limits and original creative exercises.
5. Optional project-specific source URLs and prior unapproved concepts; none automatically becomes an owner choice.
6. A strong contract for three genuinely distinct original artistic directions, accessible mobile/desktop handling, truthful product behavior, independent rendered critique and a record of unresolved gaps.

**Source truth:** A visual preview does not prove a real app flow; our old Apple Photos/Uppy/HEM examples are historic, not current production UX. If a source image can't be opened by the receiving agent, disclose that limit instead of inventing detailed pixels.

## When to use
Use this for substantial homepage, gallery, editor, messaging composer, upload/player, event recap, or product design work where firsthand image and source research could meaningfully change the result.

**Do not use** for an isolated auth bug, missing API permission, crash/500 error, deployment configuration or pure backend route fix. Art history and beautiful screenshots are not prerequisites for all engineering tasks.

## Performance/quality gates
- At most four selected studies and six imported screen paths in a packet; current length hard cap **16,000 characters**.
- Only Python standard library; no image manipulation, OCR, metadata copying to cloud, background processes, vectors or API charges.
- Original case selection uses a deterministic keyword/task-based scorer, with modest source-type diversity when relevant. This is **not a semantic vision model** and does not guarantee the best reference; the agent must critique source relevance.
- Authoritative app facts are validated in the current project repository at implementation time; the Lab's Faneqo adapters are not dynamic production snapshots.
- Session must maintain the owner-approved boundaries, true image rights, distinct editing vs publishing and share permissions.
- Refuse invented user studies, purchased reference access, automatic production edits and status promotion merely because a packet was generated.
- Independent visual/UX review and controlled same-model baseline comparisons are still **NOT RUN**; quality superiority cannot be claimed yet.

## v5.0 integration seam
The owner reports an advanced separate v5.0 skill; its precise installation location remains unverified. This new router is a **standalone optional tool**. The safe next integration is to discover the active v5.0 entrypoint and add at most one just-in-time route: "For major visual design assignments with project screenshots, run Creative Intelligence Lab's prepare_design_packet.py; use 2–4 relevant references and open actual images before proposing a direction." Preserve all existing methods and never overwrite older skill files on top of v5.0.

## Next actionable applied experiment
Choose one Faneqo Night Recap screen with a sanitized original screenshot and a real implementation-state brief. Generate a packet, let the current AI produce three original *comparable* directions, build only an authorized isolated prototype and obtain actual screenshot/interaction criticism. Compare against the same model without the packet under identical time/tokens/briefs; see quality/BLIND_ART_DIRECTION_COMPARISON_PROTOCOL.md. This remains future work, not an experiment that has already shown better outcomes.
