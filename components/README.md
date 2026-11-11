# Component Anatomy & Interaction Excellence

**Research cycle 005 — 2026-11-11.** First-pass review of official Apple HIG, Microsoft Fluent 2, GOV.UK, and W3C APG.

## Why components need more than pretty screenshots
A component is a visual anatomy *plus* an interaction contract. Distinguish the appearance of a button, dialog, tab, or field from its semantic role, keyboard behavior, states, content rules, feedback and error recovery. A screenshot cannot prove implementation quality.

## New studies
- [Buttons and action hierarchy](buttons.md)
- [Dialogs and interruptions](dialogs.md)
- [Forms, errors and tabs](forms-tabs.md)
- [Illustrated original component anatomy SVG](../visual-library/original-studies/component-anatomy.svg)

## Evidence status
Official guidance reviewed (see exact citations in each file). No independently tested deployment, user test, mobile/browser audit, or screen-reader test. No claim that any one design system is objectively the best.

## Common evaluation record
For every component, document:
1. User job and choice of pattern.
2. Anatomy and label/action semantics.
3. Variants, states, priority and disabled behavior.
4. Keyboard/focus/touch and screen reader expectations.
5. Error/loading/success, cancel/undo and reversibility.
6. Narrow-screen and zoom/reflow behavior.
7. Motion and reduced-motion alternative.
8. Verified source guidance versus interpretation.
9. Counterexamples and failure modes.
10. Tests and screen captures with provenance.

## Next investigations
Compare real interactive examples across Material, Fluent, Apple and at least one Vue library, including recorded keyboard walkthrough, visual focus states, and responsive screenshots. Do not imply that app-native HIG mappings directly equal CSS pixel requirements.