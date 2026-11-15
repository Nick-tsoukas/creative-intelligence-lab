# Elite UX Director v0.4 — Homepage Intelligence Upgrade

**Date:** 2026-11-15. **Source repo:** `Nick-tsoukas/creative-intelligence-lab`. **Release state:** verified on target PR/CI when reported in GitHub, not assumed by this document. **Installed Windows version before this release:** founder-provided Claude Code report confirms v0.3 personal skill at `C:\Users\happy\.claude\skills\elite-ux-director\`. The GitHub v0.4 update **does not update that local copy**.

## Why update before the homepage assignment
- v0.3 excels at task journeys, state, permission and recovery. v0.4 adds a **separate homepage reading mode** without turning the UX skill into the Creative Design Director or a generic marketing copywriting template.
- Eight selected `H01–H08` cards: first-view purpose, real target audiences, credible product demonstration, nonlinear/skippable cinematic narrative, real CTA/signup destinations, reduced-motion + Core Web Vitals, independent evaluation and lock-preserving design iteration.
- New homepage-specific UX handoff template; just-in-time `python scripts/retrieve.py homepage H01` (works with Windows/WSL Python if available) and manual Markdown fallback.
- Actual Faneqo homepage architecture and approved language captured separately at `domain-adapters/faneqo/HOMEPAGE_EXPERIENCE.md`; these facts must be verified against the live working branch at redesign time.
- Structural CI checks and prepared activation/quality fixtures are **not** an efficacy benchmark. No product code was changed.

## Safest installation — let Claude do it after current Faneqo work is finished
Ask Claude to:
1. Inspect its current personal `elite-ux-director` installation (reported: `C:\Users\happy\.claude\skills\elite-ux-director\`) and existing old project-level v0.1 copy under `C:\code\musicbizqr\.claude\skills\elite-ux-director\`. Preserve project copy and clearly identify precedence. Do not delete either without need.
2. Fetch **current main** of `Nick-tsoukas/creative-intelligence-lab` in a temporary or independent checkout (not an active Faneqo worktree). Verify the exact v0.4 source and GitHub CI status.
3. Run `python3 scripts/check-elite-ux-director.py` through WSL if native Windows Python is unavailable, ensuring paths point to the Lab checkout. This checks packaging and H01–H08 extraction, not Claude UX outcomes.
4. Back up `C:\Users\happy\.claude\skills\elite-ux-director\` with a timestamp, then replace the **entire** personal skill folder from `skills/elite-ux-director/`, copying only source-controlled files (SKILL.md, references, template files, scripts and EVALUATION.md). No partial copy into old contents.
5. Copy the updated *separate* `domain-adapters/faneqo/` to the previously established project-only path `C:\code\musicbizqr\.claude\domain-adapters\faneqo\` after backing up the current adapter folder; ensure `HOMEPAGE_EXPERIENCE.md` is present. This is a project reference, NOT another skill. If the folder is git-ignored, keep it so; do not commit private/local scaffolding without permission.
6. Verify `/skills`, `/elite-ux-director`, new `HOMEPAGE_INTELLIGENCE.md`, selector `homepage H01` and that no stale older copy is shadowing personal v0.4. If skill reload fails, restart in a new session.
7. Leave Faneqo frontend/backend code and production unchanged. Do not run synthetic formal benchmark sessions or make new app code changes merely because the skill upgraded.

**Rollback:** restore timestamped personal skill backup and separate adapter backup if the new version behaves badly. Project-local v0.1 stays untouched unless deliberately retired in a separately scoped action.

## Homepage kickoff — use skill roles deliberately
- **UX Director v0.4**: inspect real homepage, user jobs, first-glance comprehension, CTA actual route/sign-up consequences, proof claims, navigation, focus, motion/performance. Load **up to two H-cards**; create `HOMEPAGE_UX_PACKET.md` only for major redesign.
- **Faneqo domain adapter**: actual product culture/brand, known local route, supported fan-show loop and explicit unknowns, not an automatically trusted requirement.
- **Creative Design Director** (if installed/available): develop three genuinely different art-direction concepts only within the approved/open visual scope; preserve existing first two sections unless evidence demonstrates a defect and owner authorizes the relevant alteration.
- **Frontend-design + Nuxt 3 engineering**: code only when authorized on non-deploying branch/sandbox; inspect actual responsive behavior (320,390,430,768,1440), screenshots, accessibility, SSR/hydration, media failure, browser interaction and CWV.
- **Independent critic**: review actual rendered evidence, compare UX comprehension and creative expression separately; no imaginary conversion outcomes. Founder review remains required for final visual direction and production merge/deploy.

## Release checklist
- [ ] Current main has `v0.4` and all newly referenced files; no Faneqo adapter bundled into universal skill.
- [ ] Package GitHub Action passed on exact PR head/merge if required.
- [ ] `homepage H01` extracts only H01; C01–C09 and P1–P9 unchanged.
- [ ] New H-card sources have precise URLs and status; Baymard retail evidence not generalized to Faneqo.
- [ ] Windows install and rollback recorded separately; don't claim local update from merge.
- [ ] Homepage UX effectiveness not claimed from package CI.

## Next learning loop
Use the upgraded skill on the real authorized Faneqo homepage assignment, record where it made a concrete correct/incorrect decision, note route/screenshot/QA evidence and revise or remove underperforming H-cards. Avoid collecting books without affecting actual decisions.
