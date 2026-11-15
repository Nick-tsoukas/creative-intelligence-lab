# UX Decision / Journey Review — [human job, not feature label]

**Scope / authority:** [research, prototype, local app, approved production change]
**App / version / branch / date:**
**Actors and environment:** [roles, novice/expert, device, venue/desk, interruptions]
**Human job:** When [situation], [actor] wants to [verb/outcome], without [risk].
**Evidence inspected:** [links to screenshots, code/routes, logs, first-person reports, standards]
**Missing evidence:** [not accessed / unknown / user study not performed]
**Source cards used:** [at most 2, precise book/chapter/standard and whether read]
**Decision owner:** [proposed / approved / unclear — never invent approval]

## Quick diagnosis (for a small task, use ONLY this section)
| Finding / classification | Evidence label and exact location | Severity & consequence | Minimal safe repair | Verification |
|---|---|---|---|---|
| ... | REPORTED / OBSERVED / INFERRED / HYPOTHESIS / TESTED / UNKNOWN | P0–P3 with uncertainty | ... | ... |

## Cross-entry journey (only for complex tasks)
| Step / entry | Human purpose & visible action | Context inherited | Actor permission / server truth | Failure / resume | Evidence |
|---|---|---|---|---|---|

## Domain vocabulary & trust boundary
| Object or state | What user thinks it means | What backend currently means | Who may change or see it | Unresolved decision |
|---|---|---|---|---|

Especially distinguish stored vs published, audience vs visibility, queued vs sent/delivered, scan vs follow/check-in, preview vs actual QR payload.

## Decision alternatives
- **A — smallest coherent repair:** [what changes, what remains invariant]
- **B — more structural redesign:** [specific simplification, justified only by evidence]
- **Tradeoffs:** discoverability, task continuity, recipient/privacy, safety, accessibility, performance and engineering cost.
- **Rejected tempting shortcut:** [unsafe or unhelpful option and why]
- **Owner/implementer authorization status:** [never assume a proposed design is approved]

## Behavior contract (critical transitions, not every trivial click)
| Actor / state | Trigger & input | Server-authoritative check | Visible truthful outcome | Keyboard/focus | Error/retry/interruption | Test needed |
|---|---|---|---|---|---|---|

Use only states the real product supports. For public edits, broadcasts, permissions or QR changes specify consequence before action, duplicate prevention and no unauthorized audience.

## Context and persona evidence
- **Role/task differences:** [who has authority, whose interest may conflict]
- **Observed field conditions:** [only with evidence]
- **Provisional scenario assumptions:** [clearly labeled]
- **Who was not represented / what would falsify it:** [if relevant]

## Actual verification (only if work was authorized and executed)
- **Environment / commit / account:** 
- **Tasks and state variations actually run:**
- **Mobile/desktop, keyboard, focus, zoom/reflow, reduced motion, assistive tech:**
- **Actual observed outcomes / defects:**
- **Not executed and why:**
- **Regression / rollback concern:**

## Handoff — concise
1. **What the engineer should change** [bounded to authorized scope].
2. **What MUST NOT change** [permissions, data model, background sending, already printed QR semantics].
3. **Most important product uncertainty** [decision required].
4. **Acceptance check** [real behavior, not “looks good”].
5. **Next observation** [only if evidence gap matters].

**Evidence rule:** don't claim a book was read because listed, a user was interviewed because a persona exists, or a design was tested because a code review passed. Don't generate multiple reports where a project ticket suffices.
