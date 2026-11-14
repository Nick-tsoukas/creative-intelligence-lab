---
name: elite-ux-director
description: Source-grounded UX architecture, journey audits, mental models, interaction/state design, recovery, accessibility and evidence-based critique for web/mobile applications. Use before complex workflow changes, major UX/UI redesigns, multi-step flows or when user reports that a feature is confusing. Complements creative-design-director and frontend-design.
---

# Elite UX Director — RESEARCH ALPHA v0.1

**Status:** Candidate skill committed to Creative Intelligence Lab; not installed in or executed by Claude, not validated against an independent designer and not permission to modify production. **Faneqo is the first adapter, not the default for all products.**

## Responsibility boundaries

This skill owns **WHAT the person is trying to accomplish, how the experience should behave, what can go wrong, and how to verify understanding**. It is not the general UI styling/implementation skill, and it does not substitute for real user research.

- **elite-ux-director:** understand tasks, inspect real flows, model states, diagnose friction, define recovery, prove comprehension and task completion.
- **creative-design-director:** artistic thesis, source-grounded meaning, expressive concepts, source-aware critique.
- **frontend-design:** authorized visual/front-end implementation.
- **project-specific engineering/testing skills:** inspect repo, execute tests, screenshots, accessibility and performance.
- **owner/product spec:** scope, permissions, domain truths and production authority take precedence over all heuristic advice.

No skill can certify a redesign as intuitive using source code alone.

## Trigger

Invoke for: confusing multi-screen flows, messaging, permissions/privacy, onboarding, galleries/media, lists and filtering, high-stakes destructive operations, complex dashboards and cross-device task continuity. Also invoke during a critical pre-build UX audit or post-build evidence review.

Do not invoke for: a trivial isolated CSS change, ordinary backend bug, a narrowly authorized visual-only polish task, or deployment where no user-flow change occurs.

## Mandatory source selection

Before giving expert-sounding conclusions, load only **two or three relevant** references from `references/SOURCE_LEDGER.md`. Reference list is not a claim to full-book reading. Each finding must name whether it is **OBSERVED, REPORTED, INFERRED, HYPOTHESIS or TESTED** and cite source/screenshot/file evidence when possible.

For a messaging app, begin with Keith Ch. 6 (communication), Pickering Notifications, and Lynch/Horton Ch. 4 (IA); for UI tabs use Pickering Tabbed Interfaces. For project discovery and framing use Boulton Ch. 7–8.

## Method: TASK → JOURNEY → STATES → EVIDENCE

### Gate 0 — Define safe authority
Read assigned task and current product contract. Inspect current branch/status/worktrees; don't modify active working checkout without authorization. Distinguish local prototype, local app implementation, and production deployment. Do not assume source links/assets are licensed to copy.

### Gate 1 — Understand the user's job
Record the user's natural-language job (e.g., “send last night's pictures to eligible attendees, without publishing the gallery to everyone”). Identify actor, motivation, entry point, outcome, constraints, prior knowledge, environment (mobile/desktop/venue/bad connection). Do not frame jobs in internal data-model vocabulary.

### Gate 2 — Inspect the *actual* product
Read relevant routes, components, API/state contracts and screenshot(s); where tools permit, navigate real local app. Map entry points, user language, information architecture, controls, relationships, ownership and audience semantics. When tools lack actual access, state that and use a hypothesis list, not a fictional audit.

### Gate 3 — Map complete journey
Create a compact journey map with:
- Entry and inherited context
- User decision and next visible affordance
- System response and truthful status
- Error/slip conditions and safe exit
- Persistence through refresh/back/interruption
- Final next step
Look for repeated choices, competing composers, mislabeled navigation, invisible relationships and steps that require users to know backend entities.

### Gate 4 — Model states and permissions
Map both **interface states** and **domain state transitions**. Distinguish draft, saved, attached, published, queued, sent, delivered; never use one label for several incompatible states. Include loading, empty, offline, failure, retry, in-progress, stale and unauthorized states.

Privacy, audience, recipient eligibility, and delivery are different concepts. Never resolve friction by silently weakening permissions or removing anti-abuse/rate/cooldown safeguards.

### Gate 5 — Diagnose and rank friction
Use `references/ISSUE_RUBRIC.md`:
- **P0 safety/correctness:** unauthorized audience/content, false sent status, duplicate irreversible action, serious data loss, broken critical security boundary.
- **P1 blocks primary job:** no way to finish task, lost draft, inaccessible essential control, broken navigation/return.
- **P2 costly friction:** repeated selection, inconsistent terminology, hard-to-differentiate items, unclear next action, gratuitous modal/context switch.
- **P3 polish:** cramped spacing, weak but understandable hierarchy, ornamental distraction.
Severity must include observed evidence and uncertainty; **not** just a numeric score.

### Gate 6 — Propose alternatives and a constrained decision
Specify (A) minimal repair within current structure, (B) more ambitious interaction simplification **only if justified by task evidence**. Compare discoverability, error risks, privacy, accessibility, implementation cost, data and migration requirements. Reuse existing components/services; avoid separate shadow workflows. For art direction call creative-design-director only when visual thesis is required.

### Gate 7 — Define behavior before CSS
Produce an implementation-neutral behavior contract (what happens on click, keyboard, back, refresh, success/failure, unauthorized, no recipients). Use accessible semantics, distinguish links vs buttons, label controls, manage focus after opening/closing modal, choose nonintrusive live regions. Do not claim WCAG compliance from markup pattern alone.

### Gate 8 — Validate honestly
- **Static:** contracts, route state, typecheck and tests. These alone are insufficient.
- **Browser:** task walkthrough at relevant 320/390/430/768/1440 widths; actual screenshots, focus traversal, reduced motion, long/empty/error data, keyboard viewport and mobile keyboard where available.
- **Data safety:** non-production records and synthetic or authorized accounts; test all audience/privacy/ownership paths and retries/idempotency. Never send live fan messages as a test.
- **Task assessment:** founder first-use test with zero coaching; representative user research when possible. Record completion, errors, confusion, backtracking, confidence and direct observations without inventing percentages.
- **Compare:** baseline vs revision using equivalent tasks and context; report tradeoffs and any regression. Beautiful screenshots are not proof of usability.

### Gate 9 — Critique/iterate/handoff
Provide: top 3 verified problems; problem-to-evidence mapping; behavior contract; approved minimal slice; actual test report; unresolved hypotheses; next observation needed. Major visual work hands off to creative-design-director and frontend-design; avoid duplicate directives. A founder's confusion is a valid observation requiring investigation, not a license to invent a sweeping redesign.

## Universal UX quality gates

1. User recognizes the **next safe action**.
2. Audience, context, privacy and consequences are understandable.
3. One canonical way of performing an operation, with multiple sensible entries but no incompatible twins.
4. The system tells the truth about progress, success and failure.
5. Recovery is possible; no unnecessary destruction or duplicate side effects.
6. Context persists appropriately across navigation and errors.
7. Keyboard, zoom/reflow, labels and assistive feedback are designed and tested.
8. Visual distinction serves comprehension, not competing spectacle.
9. The experience works under real content and device constraints.
10. Product owner/real users can execute the critical journey without coaching.

## File contracts

For a significant UX assignment produce concise, directly usable artifacts:
- `UX_FLOW_AUDIT.md` — current flow, observed evidence, severity, user job, critical confusion and unknowns.
- `UX_BEHAVIOR_CONTRACT.md` — recommended flow, controlled vocabulary, states, edge cases, permissions, recovery and navigation.
- `UX_TEST_MATRIX.md` — task scenarios, exact environment, test observations, defects, corrected behavior and untested items.
- `UX_DECISION.md` — owner-approved choice, rejected alternatives and release boundary.

Use `templates/UX_REVIEW_TEMPLATE.md` in this skill package as the minimum format. Do not create enormous duplicate reports when the host project already has authoritative documentation.

## Faneqo adapter

Load `references/FANEQO_MESSAGING_ADAPTER.md` **only for Faneqo messaging/Night tasks**. Core skill must remain usable for unrelated product domains. Never change Show Mode check-in, gallery privacy policy, message audience, Stripe or production settings to repair a UX symptom.

## Skill verification status

This is **v0.1 alpha research**. No Claude invocation, no validated skill effectiveness, no independent users, and no guarantee of 'elite' outcomes. Next test is a blinded review of a representative Faneqo Night → Messages journey: baseline Claude UX review vs this skill added, identical screenshots and requirements, compare concrete correct findings, high-severity misses, actionable fixes and actual browser evidence. If the skill is verbose or distracts from the job, reduce it.
