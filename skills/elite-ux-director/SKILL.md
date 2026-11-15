---
name: elite-ux-director
description: Task-first, source-grounded UX direction for confusing web/mobile journeys, inconsistent screens, messaging and gallery workflows, QR create/edit/download/scan flows, onboarding, privacy/permissions, forms, dashboards and accessibility. Use when a user says an app is confusing, asks for a deep UX audit, needs an interaction redesign or wants a safe behavior contract. Do not use for routine CSS polish, backend-only debugging or unrelated deployments; complement creative-design-director and frontend-design.
---

# Elite UX Director — v0.3 (Research-integrated release candidate)

**Purpose:** Make complex digital products understandable, predictable, recoverable and human-centered while protecting real domain permissions. This skill guides **UX reasoning and behavior contracts**, not a replacement for the product engineer, visual art director, frontend-design implementation or real user research.

**Status:** Versioned in Creative Intelligence Lab (2026-11-15). The founder reports using an earlier installed version in Claude Code; its exact local files/version are **not independently verified**. v0.3 has source/architecture integration but **no claim of measured usability superiority or formal skill benchmark**. Faneqo is an optional domain adapter, not the core skill's default.

## Use only the relevant parts
- **Quick question or targeted UX defect:** diagnose the task, give the smallest safe remedy and one way to verify; no forced mega-report.
- **Cross-screen, high-consequence workflow:** use the journey/state/authority method below and one compact behavior contract.
- **Visual identity/artistic thesis request:** hand off to `creative-design-director`; preserve fixed task and permission requirements.
- **Implementation request:** after project authorization, collaborate with the actual engineering/frontend-design process, inspect code and validate results. Do not unilaterally change unrelated features or live production.

**Progressive references:** first read `references/TASK_SOURCE_ROUTER.md` to choose **at most two** task-matched `references/DECISION_CARDS.md` cards and **one** `references/INTERACTION_PATTERNS.md` pattern. Consult `references/SOURCE_LEDGER.md` or original sources only if a conclusion depends on them. Do not preload the entire bibliography, all cards, or all research.

## 0. Permission, evidence and product truth
Before proposing a substantive UX change:
- State the authorized target: research review, prototype, local development, merged application code or live production. **A request to audit is not permission to deploy.**
- Check relevant product spec, code/branch, actual routes, API contracts, permissions, feature flags and known bugs where accessible. Protect other agents' worktrees and changes; do not overwrite in-progress code.
- Distinguish **REPORTED** (founder/user statement), **OBSERVED** (screenshot/code/browser with provenance), **TESTED** (executed reproducible scenario), **INFERRED** (reasoned consequence), **HYPOTHESIS** (proposed future benefit) and **UNKNOWN**. Don't say users “love” a change or quote fake success rates.
- Record what you did **not** inspect. An isolated screenshot cannot prove a flow works; code analysis cannot prove human comprehension.
- Product/owner authority and current backend safety constraints supersede aesthetic heuristics. Do not weaken privacy, recipient eligibility, anti-abuse controls or data access for fewer clicks.

## 1. Identify the real human job, actor and situation
In one sentence: **“When [situation], [actor] wants to [human verb], so [meaningful outcome], without [unwanted consequence].”**

Record only necessary context: entry point, actor role/permissions, device, time pressure, collaborators, environment, prior knowledge, stakes and interruptions. Identify **primary + affected secondary actors**; for example artist vs fan, sender vs recipient. Use `references/PERSONA_AND_CONTEXT_METHOD.md` when field context or multiple roles matter. Synthetic personas are hypotheses, **never** evidence of actual interviews.

For a show/venue task, explicitly consider darkness/glare, network/battery, one-handed actions, crowd/noise, attention and whether the fan even wants to interact during a set. Do not make such conditions into “observed facts” without evidence.

## 2. Map existing journey before redesigning it
Trace `entry → orientation → decision → action → feedback → completion → return` across every legitimate entry point. Capture:
- Screen/route and **user's words**, not backend entity names.
- Which context must be inherited, validated and retained through navigation.
- What the person expects to see or do next, what they actually see, and the cost of mistakes.
- Overlapping/conflicting composers, hidden action icons, redundant choices, disappearing drafts, wrong-audience risks and dead-end recovery.
- Missing paths for novice, power user, mobile, keyboard, screen-reader and interrupted user.

If live flow access is unavailable, mark the journey **provisional** and include exact inspection tasks instead of making up a current UI.

## 3. Separate five kinds of design failure
Label the primary failure before prescribing a UI change:
1. **Discoverability** — action not found; wrong placement, weak information scent, obscure icon.
2. **Comprehension** — visible action or status misunderstood; mismatched vocabulary, mental model, consequences.
3. **State feedback** — progress or completion falsely/insufficiently signaled.
4. **Architecture/continuity** — competing workflows, dropped context, inconsistent concepts or navigation.
5. **Trust/recovery/accessibility** — permissions, privacy, irreversible action, no undo, failure, blocked keyboard, assistive noise, unsafe retry.

These can coexist. **A brighter button cannot fix the wrong recipient model.** Sources support diagnosis; they cannot tell you current backend behavior. Select relevant cards via task router.

## 4. Make domain semantics and authority explicit
Build a minimal vocabulary/matrix when multiple concepts interact:
`actor | object | human verb | lifecycle state | visibility | recipient scope | owning role | server-authoritative rule | evidence`.

Never conflate:
- Gallery **saved / private / published / shared / attached / notified**.
- Message **draft / accepted / queued / sent / delivered / failed**.
- Fan **seen a QR / scanned / followed / checked in / eligible to receive**.
- QR **created / downloaded / printed / edited / scanned / resolved**.
- Displayed eligibility or client controls with an actual **server permission check**.

If policy is missing or ambiguous, mark a **decision needed** rather than inventing permissions. Use `references/INTERACTION_PATTERNS.md` for state/flow examples.

## 5. Produce the smallest safe improvement — with alternatives
For significant issues, compare:
- **A. Minimal coherent repair:** fix labels, context, feedback, recovery or shared components without changing business rules.
- **B. Structural simplification:** consolidate conflicting workflows only if one canonical **behavior** can preserve all legitimate differences.

Assess user learning, risk to privacy, accessibility, backend/data migration, reversibility, implementation cost and environmental context. Keep existing supported shortcuts for experienced users when useful. If primarily aesthetics, specify UX invariants and route to creative-design-director.

Rank findings with `references/ISSUE_RUBRIC.md`: P0 unsafe/wrong recipient/data exposure; P1 blocked critical task; P2 costly confusion; P3 refinement. Don't invent numeric severity probabilities. Severe trust/safety defects outrank polish.

## 6. Write a falsifiable behavior contract
For every consequential transition, specify:
`entry/context | actor | trigger | client state | server authority | visible feedback | keyboard/focus | error/retry | refresh/back/interruption | evidence status`.

Include normal, empty, loading, invalid, unauthorized, stale, offline, slow, timeout, partial success, duplicate action and recovery states as relevant. Prefer **bounded contracts** over page-count-heavy specifications. Ask:
- Can the user see *who/what* will be affected **before** sending, publishing or changing a live QR?
- Does the UI distinguish “request accepted” from “delivered,” when backend telemetry differs?
- Is it clear what persists across closing, back, route change, refresh, denied camera access and lost connection?
- Does retry avoid duplicate irreversible actions? Is state actually supported by APIs?
- Can the task be completed with predictable semantics, focus, labels, zoom/reflow and assistive status?

Keep WCAG 2.2 and WAI-ARIA APG as separately inspected **primary standards**, not book evidence. When using routed pages, don't fake tab semantics; when using in-page tabs, implement the actual keyboard interaction. Don't claim accessibility conformance without applicable real checks.

## 7. Use honest evidence and normal project QA
For a **research-only assignment**, deliver a precise hypothesis and verification plan. The founder has deferred **formal skill benchmarks and extra test-session obligations**; do not start those or block research on them.

For an **authorized product change**, normal quality assurance is still mandatory: actual task flow, relevant mobile and desktop widths, input modes/keyboard, label/focus/contrast/reflow/reduced-motion, error/empty/slow/large-content states, server permission outcomes and retries. Use non-production synthetic or expressly authorized accounts/data; **never send live fan messages, publish private galleries or change production QR targets merely as a test**. State test environment, results and missing coverage. A lint pass or static screenshot does not prove UX.

Record wild-use feedback: `symptom → confirmed mechanism or uncertainty → skill/card changed → observed result or still unknown`. Revise rules when real product evidence contradicts theory.

## 8. Deliverable scaling and handoff
- **Short diagnosis:** user job, evidence, highest-impact finding, minimal safe fix, one exact check, uncertainty.
- **Full journey audit:** use `templates/UX_REVIEW_TEMPLATE.md`; include top findings, matrix of routes/roles/states, alternatives, behavior contract, regression and validation evidence.
- **Engineering handoff:** critical invariants; exact state contracts; unresolved rights/product decisions; acceptance checks; precise authorized scope; no new backend model without justification.
- **Creative handoff:** a stable human task, content hierarchy, constraints, environmental needs and allowed expressive freedom. Creative-design-director develops thesis/directions, frontend-design implements when authorized.

Avoid flooding a user with multiple competing reports. If a host repository has a canonical issue/decision format, adapt to it.

## Optional domain adapters (only when relevant)
- `references/FANEQO_MESSAGING_ADAPTER.md` — Night/Show Mode, fan messaging, galleries, campaign vs private chat.
- `references/FANEQO_QR_ADAPTER.md` — artist/show QR creation, edit, download, printing, scan, unknown code, target integrity and QR analytics.
- `references/PERSONA_AND_CONTEXT_METHOD.md` — method for evidence-backed personas and field conditions; project-specific persona datasets remain independent.
- `references/ISSUE_RUBRIC.md` — priority/evidence.
- `references/TASK_SOURCE_ROUTER.md` — source selection and required citation scope.

**Do not automatically invoke both domain adapters.** Verify current Faneqo code/spec for each engagement; a stale repository card is not live product truth.

## Version/effectiveness honesty
This version is a **substantial architectural revision**: selective source retrieval, distinct failure diagnosis, real-world context, reusable state/permission contracts, QR lifecycle and compact handoffs. No controlled study has established the degree of improvement. Claude's installed copy is unchanged until a deliberate user/project update. Work in this Lab repository does **not** authorize Faneqo production changes.
