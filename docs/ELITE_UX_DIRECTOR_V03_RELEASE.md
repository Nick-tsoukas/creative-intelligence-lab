# Elite UX Director v0.3 — Research-integrated Upgrade and Installation

**Date:** 2026-11-15. **Stage:** research-integrated release candidate intended for real-world Faneqo work. This document records a substantial architecture/content change, **not** measured improvement from controlled skill tests, which the founder has explicitly deferred.

## What changed (vs v0.1)
1. **Specific skill activation:** discovery metadata now covers confusing flows, QR operations, gallery/messaging/permissions, complex mobile tasks, forms and accessibility; avoids basic CSS and backend-only fixes.
2. **Process compression:** diagnose by human job, first-class task context, evidence source, five failure classes, authority boundaries, minimal repair vs consolidation. Format scales from quick issue to multi-state audit.
3. **Selective retrieval:** source router (task-to-card matrix); 9 conditional design cards and 9 interaction patterns. Only 2 cards + 1 pattern should normally load, not a full research library.
4. **Real-world method:** provisional behavioral archetypes vs participant evidence; situational UX, multi-actor agency/team roles, interruptions, phone and venue conditions. **Does not duplicate parallel Faneqo field/persona research**.
5. **Trustworthy state contracts:** audience vs visibility, client display vs backend authority, queued vs delivered, safe retry/recovery, gallery publishing and interrupted drafts.
6. **QR lifecycle coverage:** newly supported Faneqo QR create/download/print/edit/scan/unknown-target and metrics distinctions; includes negative cases and regression concerns.
7. **Worked examples:** founder-reported messaging/gallery and QR failures translated into safe, concise research-to-repair alternatives; explicitly not claims of an executed audit.
8. **Evidence updates:** source ledger now reflects section-scoped reading of HCI (2025), Frost, Vignelli, Costanza-Chock and William James; unread sources remain unread.
9. **Sharper review template:** compact triage option, permission matrix, falsifiable transition contract, affected-person context and verification results.

## Files to install **together**
The entire folder `skills/elite-ux-director/`, **not just `SKILL.md`**:
- `SKILL.md`
- `references/TASK_SOURCE_ROUTER.md`
- `references/DECISION_CARDS.md`
- `references/INTERACTION_PATTERNS.md`
- `references/PERSONA_AND_CONTEXT_METHOD.md`
- `references/FANEQO_QR_ADAPTER.md`
- `references/FANEQO_MESSAGING_ADAPTER.md`
- `references/WORKED_DECISIONS.md`
- `references/ISSUE_RUBRIC.md`
- `references/SOURCE_LEDGER.md`
- `templates/UX_REVIEW_TEMPLATE.md`
- `EVALUATION.md` (retained unexecuted test fixture, not required to invoke)

**Avoid:** overwriting a live working checkout or reinstalling mid-task. The user reports that Claude already uses a version; this repo cannot identify that installed path without inspecting the user's actual machine. **This upgrade is not installed by GitHub merges.**

## Which copy does Claude use?
Current [Claude Code skill docs](https://code.claude.com/docs/en/skills) define:
- **Personal:** `~/.claude/skills/elite-ux-director/SKILL.md` (every project in *that* OS/home environment).
- **Project:** `<your-faneqo-workspace>/.claude/skills/elite-ux-director/SKILL.md` (only there).
- **WSL and Windows are separate homes.** Installing in `/home/<user>/.claude/` does not necessarily update Windows `C:\Users\<user>\.claude\`, and vice versa.
- Same-name/project/added-directory entries can coexist. Inspect actual skill paths and choose **one authoritative copy** for Faneqo; remove or rename an obsolete duplicate only with deliberate backup. A plugin-provided skill may not be replaced by writing a personal copy with the same name.

### Safe method — Windows PowerShell (manual, personal install)
Run after the Lab repo checkout is updated and you're at its root. Prefer the **Windows** personal copy if Claude Code is launched as `claude.exe` from Windows; if it runs from WSL, use the WSL method below.

```powershell
git pull --ff-only
$source = (Resolve-Path ".\skills\elite-ux-director").Path
$target = Join-Path $HOME ".claude\skills\elite-ux-director"
New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
if (Test-Path $target) { Rename-Item $target ("elite-ux-director.backup-" + (Get-Date -Format "yyyyMMdd-HHmmss")) }
Copy-Item -Path $source -Destination $target -Recurse
Test-Path (Join-Path $target "references\TASK_SOURCE_ROUTER.md")
```

That `Rename-Item` backs up an existing folder in the same parent directory. If `$target` is a project-local installation or a plugin, **do not run this personal script expecting to replace it**. Replace the chosen actual target instead, with an equivalent backup.

### Safe method — WSL Bash (manual, personal install)
From an updated Lab repo root inside the **same WSL distribution/home where Claude runs**:

```bash
git pull --ff-only
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/elite-ux-director" ]; then
  mv "$HOME/.claude/skills/elite-ux-director" "$HOME/.claude/skills/elite-ux-director.backup-$(date +%Y%m%d-%H%M%S)"
fi
cp -a skills/elite-ux-director "$HOME/.claude/skills/"
test -f "$HOME/.claude/skills/elite-ux-director/references/TASK_SOURCE_ROUTER.md"
```

If a **project-level** Faneqo skill is currently authoritative, install that folder there instead, preferably through the project's existing skills installer; changing a project-level version may become a repository diff, so use a separate authorized change. Do not silently overwrite other agents' in-progress files or installed skills.

### After copying
1. Finish the current Claude task first. Start a new Claude Code session (or follow the version's documented live reload behavior) so the skill metadata is discovered reliably.
2. Invoke `/elite-ux-director` on a **normal, authorized Faneqo issue**; confirm it reads the new version, performs a task-first diagnosis and selectively loads reference cards.
3. The very first use should be a real task already in the backlog, **not a formal benchmark**. Record friction honestly in the Lab issue/decision history.
4. If the skill is too long, too generic, or suggests unsafe behavior, restore the timestamped backup. The Lab source remains available to fix and republish.
5. Do not infer installation success from the GitHub PR status alone; check the actual path and Claude skill discovery.

## Release acceptance gate (without formal benchmarking)
- [ ] New version merged to `main`, all expected files present on the branch/main.
- [ ] YAML name/description and local reference paths checked against current Claude Code docs.
- [ ] Scope, permission and evidence labels verified; no contradictory “not installed anywhere” claim.
- [ ] Source records correspond to actually inspected original sections; no “full book read” inflation.
- [ ] One worked QR and one messaging example with recovery/trust boundaries in package.
- [ ] Manual installation and rollback documented.
- [ ] No Faneqo production code, data, deployment, or active Claude installed copy changed.
- [ ] **Effectiveness not claimed as empirically proven** until observed in actual authorized use.

## Further improvement — high-value next work, not a blocker to v0.3
- Audit real Faneqo journeys through the refreshed skill during naturally authorized product work, track high-impact misses and false positives.
- Integrate the parallel music-industry field/persona research **after evidence and ownership reconcile**, without double-bookkeeping.
- Deepen HCI reading in Chapters 5, 18, 27, 37, 42 and add more concrete examples only as they change design decisions.
- Review age of external standards before each implementation; the catalog is not automatically current.
- Consider short reference cards for multi-artist switching, notification permissions, empty/long-data dashboards and responsive accessibility based on observed actual product friction.
- Do not run formal skill benchmarks or demand extra founder testing at this stage.

**Owner-facing truth:** v0.3 is a meaningful functional upgrade *on paper and in source*, and may be safely installed when the package is verified, but **“dramatically more effective” requires eventual practical evidence**. Current Claude installations remain unchanged until a person explicitly copies the package.
