# Design-to-code: prevent demonstrated failure modes

These are conditional checks derived from field feedback, not bans on useful CSS techniques.

| Risk | Check the rendered behavior and semantics |
|---|---|
| Visual reorder | DOM/reading/focus order must preserve task meaning across widths. CSS order and display:contents can create a visual/semantic mismatch; test the actual accessibility tree and keyboard sequence. Prefer meaningful source order. |
| Sticky controls | Measure available height on short viewports, zoom and mobile keyboard. Keep primary actions reachable through normal scrolling; fall back to nonsticky or bounded internal scrolling when needed. |
| Editable fields | Make editability and current value recognizable without hover; explicit labels, focus and invalid states. If a boundary is necessary to identify a control, assess its non-text contrast against adjacent colors. Not every decorative border requires 3:1. |
| Label/name mismatch | Accessible names should include the visible label; icon-only actions need meaningful names. Verify disabled explanations and status announcements; do not encode state only in color. |
| Font-dependent sizing | Await document.fonts.ready before measuring text; remeasure when font/content/container changes. Prefer intrinsic CSS sizing where practical. Check long/localized strings, text zoom, fallback fonts and late loads. |
| Overlays and fixed nav | Check open dialogs, failed-upload notices, toasts and sticky footers with keyboard/focus. Ensure content and controls are not hidden; do not hide the nav merely to obtain a flattering screenshot. |
| Responsive data | Exercise empty, busy, failure, resumed and long-content variants; check crop/focal point and intrinsic min-width. No placeholder success for unsupported operations. |
| Shared components | Reuse existing contracts. Prefer an optional scoped variant when a change is surface-specific; check other consumers before altering global behavior. |
| Framework boundary | Preserve the actual stack/version and JS/TS conventions. With Nuxt 3/Vue, avoid SSR/client divergence, stale route state and watchers that outlive their owners. Do not migrate frameworks as visual cleanup. |

## Legacy tests: behavior versus taste

Read the assertion and its reason. Authorization, persistence, reading order, keyboard reachability and state truth are behavior contracts. A gradient/class/old composition assertion may encode a superseded taste decision, but can also encode meaningful contrast or state; inspect before classifying.

If current authorized design intent supersedes a taste assertion, replace it with a positive check of that intent and retain underlying behavior/accessibility coverage. Explain the changed expectation. Never delete a failing test just to obtain green results, infer approval from a newer timestamp, or silently weaken a behavioral requirement. Report unresolved product-authority conflicts.
