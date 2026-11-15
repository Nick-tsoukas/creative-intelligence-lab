# Elite UX Director — Architecture and Intelligence Audit

**Date:** 2026-11-15. **Target:** existing Elite UX Director and its v0.3 in-progress refactor. **Scope:** technical architecture, activation, knowledge retrieval, personas, independent evaluation, context efficiency and maintenance. NOT a restart, not a Faneqo production audit, not an executed model-efficacy study.

## Sources reviewed
1. Official [Claude Code skills](https://code.claude.com/docs/en/skills), sections on skill locations, invocation, reference files, live editing, context compaction, trigger troubleshooting and evaluation. Reviewed on 2026-11-15.
2. Official [Agent Skills specification](https://agentskills.io/specification) — frontmatter constraints, portability, three-stage loading, shallow relative links, optional scripts/references.
3. Anthropic [Equipping agents with Agent Skills](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) — metadata/body/resources progressive disclosure, composability.
4. Anthropic [Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (2025-09-29) — high-signal minimal context, context decay/attention budget, targeted just-in-time knowledge.
5. Anthropic [Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents) (2025-09-11) — distinct tool boundaries, meaningful outputs, reduce response/token noise, evaluate tool use.
6. Anthropic [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (2026-01-09) — task/trial/grader/trace/outcome distinction, independent evidence and baseline comparisons.
7. Matt Pocock [Skills for Real Engineers](https://github.com/mattpocock/skills), examined repo adaptations in [research/012](../research/012-AGENT-SKILLS-UX-ARCHITECTURE.md), including domain-modeling, prototype, research and test seam patterns.
8. Current Lab [Master Product Plan](MASTER_PRODUCT_PLAN.md), [UX+Design Master Plan](UX_DESIGN_INTELLIGENCE_MASTER_PLAN.md), existing v0.1 skill, 001–012 reading dossiers, source ledger and Faneqo adapter.

**Evidence classification:** Direct technical documentation and existing repository content. Architecture conclusions and predictions are expert judgment, NOT measured Claude output improvements.

## Audit: high-impact improvements

| Aspect | Baseline gap | Change built | Priority | How correctness is evaluated |
|---|---|---|---|---|
| Activation | Broad skill scope could trigger on low-level coding or be missed on human “confusing screen” reports | Specific natural-language trigger metadata + nontrigger boundaries; keep Claude auto-invocation for real UX work | P0 | Inspect frontmatter; later collect positive/negative invocation traces in fresh sessions |
| Progressive disclosure | Long SKILL plus source ledger and generic procedural repetition | Short 76-line core; task router; conditional cards and pattern library; small references only as needed | P0 | Entrypoint length, references reachable, retrieval outputs bounded, no forced mega-document |
| Relevant expert knowledge | Book catalog not directly usable at decision time | Source-to-task router, nine conditional cards, nine interaction patterns, original citation/reading labels | P0 | Source provenance and source→decision→limitation links; no unread text treated as evidence |
| Domain boundaries | Original Faneqo messaging adapter lived inside universal skill; new QR draft repeated pattern | Rehome Faneqo messaging, QR and worked scenarios to `domain-adapters/faneqo/` | P0 | Generic package has no required product-specific files, project adapter installs separately |
| Evidence-based personas | Generic persona advice risks synthetic demographics masquerading as fieldwork | Strict evidence ladder, role × context job cards, alternatives, falsifiable assumptions | P0 | Audit persona outputs for testimony provenance, access rights, role variety and unknowns |
| Independent evaluation | An unexecuted 8-scenario fixture existed, but no clear activation/quality separation or independent review | Versioned evaluation protocol + activation positive/negative cases + quality invariants; keep unexecuted until ordinary work warrants it | P0 | Independent reviewer and source evidence; guard against self-grading and false claims |
| Context efficiency | All decision cards in one file could waste tokens; full bibliography too large | Deterministic `scripts/retrieve.py` selects one Cxx/Px, without network/dependencies; fallback manual section | P1 | Verify one section/unknown ID handling and script package syntax; measure token/context savings only if instrumentation exists |
| Maintainability | Documentation had inconsistent old “not installed anywhere” statements and no release gate | Clear release doc, independent core, optional domain adapter, checker, version tags and future evidence loop | P1 | Static validation, packaged paths, changelog/upgrade instructions, real-world feedback log |
| Implementation boundary | Prompts can be mistaken for guarantees | Explicit distinction among skill advice, app QA, server auth and deterministic CI/hook protections | P0 | Safety review of outputs; project engineering enforces checks, not just prompts |

## What to preserve
- Existing structured TASK → JOURNEY → STATES → EVIDENCE discipline and P0–P3 issue rubric.
- Existing Keith/Lynch/Horton/Boulton/Heydon/Nielsen research with honest reading scope, as well as new HCI/Frost/Vignelli/Costanza-Chock/James dossiers.
- The distinct Creative Design Director role, approved Faneqo domain vocabulary, incident lessons, 8 historical test fixtures, field-persona workstream and the decision contract with frontend-design.
- Minimal-vs-structural repair comparison; keyboard/accessibility, recoverability, synthetic-data-only safety; no forced formal benchmark now.

## Why architecture improvements can be real without proving UX superiority
A slimmer valid SKILL, selectable source excerpts and separate domain package can be checked structurally. Their existence is a real technical improvement in distribution and reproducibility. But **only product observations or controlled model comparisons** can support the claim Claude performs better. Activation detection and outcome quality are two separate variables: a loaded skill might produce a weak answer, and a model may solve a task without activating the skill. Never infer efficacy from passing a linter.

## Retrieval design contract
1. **Level 1 metadata**: one concise name/description with user trigger and avoid-trigger terms. Do not overload with book names or every Faneqo feature.
2. **Level 2 core**: one brief reusable operating algorithm, scoped authority, evidence labeling, role separation, compact output.
3. **Level 3 references**: `TASK_SOURCE_ROUTER` (look up if unclear), `DECISION_CARDS`, `INTERACTION_PATTERNS`, `PERSONA_AND_CONTEXT_METHOD`, `SOURCE_LEDGER`, `ISSUE_RUBRIC`, template. Load narrow; default 2 cards + 1 pattern maximum.
4. **Optional executable**: `python scripts/retrieve.py card C02` (from the installed skill root), or read only the identified Markdown section if Python unavailable. This is deterministic selection and does not search GitHub or AI embeddings.
5. **Domain binding**: only the current project supplies actual actor names, policy, backend rights, scenes/personas and data; Faneqo material lives in `domain-adapters/faneqo/`, not the installed universal skill.

## Evaluation strategy — deliberately prepared, not executed
- **Activation**: for a balanced sample of real UX + negative unrelated prompts, record skill triggered / not, false positives, false negatives and the version installed.
- **Quality**: matched-input outputs with and without skill; at least one independent reviewer (not the generating agent) checks correct issues, missed P0 trust problems, ungrounded claims, actionable fix, and avoided regressions.
- **Outcome**: for authorized product work, verify actual route behavior, permission checks, user task success and recovery at the public interface/server seam, not just text grading.
- **Evidence:** keep task, model/version, frozen brief, project state, outputs/traces, reviewer, grading disagreements, cost/latency if available. Fresh sessions if formal paired comparison eventually authorized.
- **Owner instruction:** no standalone formal benchmarks now; first gather natural feedback from real authorized Faneqo assignments. A prepared protocol is not evidence of results.

## Important constraints
- README/Claude docs cannot grant permission to send fan messages, publish private content, weaken auth or deploy.
- A book excerpt is not a complete book study. Old source summaries may be useful but must carry access limits.
- Historical research may suggest design mechanisms but cannot be promoted to a universal cognitive law.
- Do not make the source router or new scripts a mandatory dependency for basic reasoning; failures should degrade gracefully to local skill instructions.
- No claim that GitHub changes automatically overwrite a user's active Windows/WSL installed copy.

## Next improvement after architecture release
1. Confirm source evidence and quality via natural Faneqo work, with issue tags from actual traces.
2. Improve underperforming cards and delete unhelpful repetition.
3. Deep-read contemporary HCI chapters on navigation, safety, and cognitive load; update narrow source cards only when a specific decision changes.
4. Integrate independently researched music-industry evidence into Faneqo adapter **without altering** the universal skill.
5. Eventually run the prepared independent model eval only when the current development cycle allows it, and label results with model/version and environment.

**Decision:** proceed with v0.3 as a source-based architecture upgrade. Do not label it empirically better than baseline until measured outcomes exist.
