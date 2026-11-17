# Render and verify the decision

Use the core's mode, work type and existing acceptance list. A prototype needs representative evidence of its stated decision, not a duplicate production certification. Research needs sources and applicability unless a claim depends on an actual rendered interface. Record unsupported boundaries once and reference them thereafter.

## Select states, not a Cartesian matrix

Derive the few important states from actual data/transitions: entry/empty/loaded; editing; pending/failure/recovery; permissions/consequences; completion/return; narrow/short/long-content presentation. Combine equivalent cases. The focused repair uses affected states; a changed journey or concept usually needs representative mobile and desktop. Follow project widths; absent a contract, 390 and 1440 CSS px are useful starting points, not mandatory repair recaptures.

Reuse valid evidence of unchanged states. An existing record can hold `state/setup | viewport/scroll scope | expected truth | capture/check | result/gap`. Labels alone do not prove a state was reached.

## Make captures trustworthy

Use existing browsers/servers, one context and sequential viewports initially on constrained hardware. No new screenshot service or dependency is implied.

1. Confirm route, role, content and target state. Wait for relevant fonts, image decoding and layout with a bounded timeout. For full-content evidence, bring needed below-fold lazy media into view or trigger its loading in the harness; record that preparation. Do not claim complete media evidence while critical images remain pending.
2. Identify the actual scroller. Record viewport, DPR, document/scroller dimensions, capture scope and state when needed to interpret the result. Full-page capture may miss an internal pane; use overlapping scroller/viewport segments instead.
3. Inspect actual pixels, including relevant lower content. Judge fixed/sticky controls and occlusion with **viewport captures**; their position in a full-page composite is not a realistic scrolling experience. Never remove visible UI simply to flatter a capture.
4. If a capture/check fails, separate product behavior from harness timing, missing assets, wrong route/role or incorrect scroll scope. Await a meaningful state/event; asynchronous editor caret focus can finish after the click that initiated it. Reproduce the user consequence before changing application code. A longer timeout alone does not establish the cause.
5. Optional: `python scripts/check_capture.py shot.png --expected-width 390 --expected-height 2400` from the skill root. Dimensions are physical pixels for the chosen scope. Exit 1 = invalid/mismatched; exit 2 = suspicious, inspect/document; exit 0 = no heuristic concern, not beauty or completeness. Preserve originals; re-export unsupported encodings with existing capture tools when needed.

Test-only eager loading or focus synchronization belongs in the evidence notes; it must not conceal production latency or alter the user behavior being evaluated. A missing environment is a limitation, not automatically a product bug.

## Repair once, verify the affected surface

| Repair | Relevant rerun |
|---|---|
| Dialog naming | Accessible name and affected focus behavior; recapture if visible layout changes |
| Mobile crop/focal control | Control changes the real image; affected mobile hero pixels |
| Save/storage behavior | Failure, buffer retention, retry and promised reload/recovery |
| Shared layout | Impacted consumers, widths and difficult content states |

Expand only for shared code, a new failure, unresolved uncertainty or engineering/project requirements. Engineering owns full-suite mechanics; the UX skill adds no second full-suite gate. Valid unchanged captures stay valid.

Review reliability and creative quality separately. Backend/read-model checks apply to the production claims being changed, not every isolated concept. Screenshots do not prove keyboard/assistive-technology or user-task outcomes. Disclose their actual coverage separately.

Done when the agreed decision is possible, critical evidence is valid, material defects are resolved and limits disclosed. Reopen only for a new material defect, changed requirements or invalid/insufficient critical evidence. Keep optional refinements in the existing short deferred list.
