# Experiment 001 — Anti-Generic Self-Audit: Signal Archive

Date: 2026-11-11. Inspected: source-code text of pilots/001-signal-archive/prototype/index.html. No real browser/participant test performed.

## Our original thesis
"Each sound is a found artifact with its own story."

## Risk signals found
Warm paper/off-white background, dark ink, Georgia serif hero, uppercase specimen metadata, numbered markers, repeated three-column cards, arrows in calls to action. These are adjacent to the default traits identified in Anthropic's official frontend-design skill.

These are not intrinsically bad. The archival context may justify some. The actual critique is whether they uniquely express sound collection or merely occupy familiar visual slots. We have not verified user perception.

## Strengths to retain
Search, visible filters, empty-state reset, session-only favorite state, honest "audio unavailable" wording, reduced-motion CSS and keyboard-focus restoration in source.

## Better alternate direction to test
- Replace repeated cards with a disciplined archival row/index.
- Feature one acoustic artifact while keeping search immediately discoverable.
- Introduce category-specific illustration without inventing analyzed audio.
- Remove unnecessary numbered decoration and generic small uppercase labels.
- Maintain semantics/focus/keyboard/mobile regardless of visual direction.

## Experimental requirement
Implement two visually different alternatives with identical content and behavior. Blind-review subject specificity and comprehension, perform task-based checks, then revise our skill when it fails. Do not claim that the Creative Intelligence method is superior before this is done.

Official source: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
