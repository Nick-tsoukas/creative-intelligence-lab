# Elite UX Director v0.3 — Release and Safe Claude Upgrade

**Date:** 2026-11-15. **State:** research-integrated, source-architecture upgrade candidate; not yet proven superior by real user/model comparisons. **Goal:** let Claude use more accurate expert methods with *less* irrelevant context; no production change.

## Delivered technical improvements
- **Progressive disclosure:** activation description → compact, general 76-line entrypoint → only selected references. Main procedure no longer repeats detailed book summaries.
- **Precise activation:** triggers on confusing flows, forms, navigation, gallery/media messaging, permissions, QR journeys, mobile interruptions and accessibility; explicitly defers styling/backend/deployment.
- **On-demand expertise:** 9 decision cards + 9 stateful interaction patterns + task/source router + deterministic single-card `scripts/retrieve.py`. External book corpus remains in Lab, not loaded on each skill call.
- **Evidence-backed personas:** affected actors, current authority and device/venue context without synthetic biographies pretending to be interviews.
- **Independent UX evaluation:** activation fixtures distinct from output quality, ground-truth/independent review protocol, honest missing coverage; **formal benchmark not run** by owner direction.
- **Long-term maintenance:** read-status/provenance ledger, static checks, GitHub Actions integrity gate, separate project adapter, release instructions and rollback.
- **Faneqo split:** `domain-adapters/faneqo/` contains the messaging/QR/real-case notes. Those are **not** required or shipped in the universal skill folder.

Sources: [architecture audit](UX_SKILL_ARCHITECTURE_AUDIT_2026-11-15.md), [master UX plan](UX_DESIGN_INTELLIGENCE_MASTER_PLAN.md), [Anthropic skills](https://code.claude.com/docs/en/skills), [Agent Skills spec](https://agentskills.io/specification).

## Actual package to install
Copy the **entire folder** `skills/elite-ux-director/` including `SKILL.md`, `references/`, `templates/`, `scripts/` and `EVALUATION.md`. Do not copy just the entrypoint.

**DO NOT copy `domain-adapters/faneqo/` into the universal skill.** In Faneqo work, make that adapter separately accessible to Claude (read through the Lab checkout or copy to a project-specific docs/reference directory when authorized).

## Before replacing active Claude skill
The founder reports that Claude is **already using** an earlier version. This repo cannot inspect the actual copy in Windows, WSL, plugin, or Faneqo project:
- Personal skill: `~/.claude/skills/elite-ux-director/`.
- Project skill: `<faneqo>/.claude/skills/elite-ux-director/`.
- Plugins have namespaced skill discovery; a plugin-provided skill isn't necessarily overridden by a personal folder.
- Windows home and WSL home are different. Updating one won't update the other.
- Claude Code currently detects many skill edits without restart; still prefer a new session after updating a busy long-running project, or `/reload-skills` if a new top-level skills directory was added.

**Avoid updating an active session mid-implementation.** Choose the actual skill source and back it up. The following examples install a **personal** copy, only if that is the intended authoritative source.

### Windows PowerShell (run from updated Lab checkout root)
```powershell
git pull --ff-only
python scripts/check-elite-ux-director.py
$source = (Resolve-Path ".\skills\elite-ux-director").Path
$parent = Join-Path $HOME ".claude\skills"
$target = Join-Path $parent "elite-ux-director"
New-Item -ItemType Directory -Force -Path $parent | Out-Null
if (Test-Path $target) { Rename-Item -Path $target -NewName ("elite-ux-director.backup-" + (Get-Date -Format "yyyyMMdd-HHmmss")) }
Copy-Item -Path $source -Destination $target -Recurse
Test-Path (Join-Path $target "scripts\retrieve.py")
```

### WSL Bash (in same Linux environment where Claude runs)
```bash
git pull --ff-only
python3 scripts/check-elite-ux-director.py
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/elite-ux-director" ]; then
  mv "$HOME/.claude/skills/elite-ux-director" "$HOME/.claude/skills/elite-ux-director.backup-$(date +%Y%m%d-%H%M%S)"
fi
cp -a skills/elite-ux-director "$HOME/.claude/skills/"
test -f "$HOME/.claude/skills/elite-ux-director/scripts/retrieve.py"
```

If your active skill is **project-local**, instead back up and install into that exact Faneqo project path through its existing approved installation workflow. Do not overwrite any agent's active worktree.

## Verify installation without a formal skill benchmark
- Confirm Claude's available skills list includes `elite-ux-director`, and invoke `/elite-ux-director` on an **already authorized ordinary UX task** (do not generate a synthetic user test).
- Check the entered instructions identify **v0.3**, do not demand a large report for a simple problem, and retrieve at most 2 evidence cards + 1 pattern.
- Ensure the project-specific Faneqo docs are available only when the task is Faneqo-related.
- If the new skill produces unsafe behavior or worsens performance, restore the timestamped backup and report the case to the Lab repo.

## Release gates
- [ ] Main skill/references syntactically valid, local paths resolve, product adapter separate.
- [ ] CI package checker actually passed on the released commit.
- [ ] Research reading claims constrained to actually examined sections and primary links.
- [ ] Future independent-eval cases prepared but not represented as run or successful.
- [ ] Release merged and exact main commit recorded; user copy not changed automatically.
- [ ] Documented backup/rollback works in target OS/project environment.
- [ ] First **real-world** usage quality observed later; never infer effectiveness from static lint.

## Boundaries and roadmap
v0.3 is a **substantial structural and knowledge-design upgrade**, not a scientifically demonstrated UX efficacy improvement. The project still needs actual Faneqo outcomes. Prioritize learning from live authorized bug fixes, developer feedback and actual user interactions; defer formal model benchmarks until project capacity permits. Always preserve production authorization boundaries.
