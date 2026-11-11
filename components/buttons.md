# Buttons — A Component's Visual Priority and Behavioral Promise

**Access:** 2026-11-11; official guidance viewed; **not** live accessibility testing.

## Original primary sources
- Apple HIG buttons: https://developer.apple.com/design/human-interface-guidelines/buttons
- Microsoft Fluent 2 button usage: https://fluent2.microsoft.design/components/web/react/core/button/usage/
- GOV.UK button: https://design-system.service.gov.uk/components/button/
- W3C WCAG 2.2 target size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

## Verified guidance
**Apple (official HIG):** Defines a button by style, content, and semantic role (normal, primary, cancel, destructive). Recommends recognizable and sufficiently separated touch/click targets; gives a general 44×44-point hit-region rule (and 60×60-point for visionOS) *in Apple's native platform contexts*. Advises limiting prominent buttons to one or two per view, using different *styles* rather than arbitrary size differences to indicate preferred actions, and providing a press state for custom buttons. Warns against making destructive actions the default primary.

**Fluent 2 (official guidance):** A button initiates an action; a link is appropriate for navigating elsewhere. Documents standard, split, menu, compound and toggle buttons. Advises a single primary action in the layout, with neutral appearances when priorities are equal. For toggle actions, communicate both status and effect; visual color alone is inadequate. Fluent's text and icon contrast advice is stated within its own component guidance, not a substitute for a complete WCAG audit.

**Comparison:** Both explicitly connect visual hierarchy to action priority. Apple permits one or two prominent actions and emphasizes native roles/context; Fluent usually specifies one primary per layout. These are platform guidelines rather than contradictory universal physical laws.

## Invented teaching example (NOT an Apple/Microsoft screenshot)
Imagine a publish screen:
- Primary: **Publish project** (high contrast).
- Secondary: **Save draft** (neutral).
- Destructive: **Delete project** (separated and appropriately labeled).
A row of three equally bright filled buttons makes all three appear primary and weakens the decision hierarchy.

## State machine to document
- Rest: label and affordance visible.
- Hover: optional for pointer devices, not the sole feedback.
- Focus-visible: discernible keyboard focus.
- Pressed: immediate response.
- Loading: show progress and prevent accidental duplicate submission while preserving context.
- Success: clearly announce completion, or navigate to a meaningful result.
- Error: specific recovery instructions; do not silently fail.
- Disabled: explain unavailability when useful; consider discoverability and focus behavior.
- Destructive: clarify consequence, provide undo/confirmation proportionate to risk.

## Research hypotheses
1. Strong prominence works best when task intent is clear and priority unambiguous.
2. More than one visual 'primary' can increase choice uncertainty.
3. Action hierarchy should survive monochrome viewing and keyboard focus.

These are proposed design hypotheses, **not measured findings** in this study.

## Risks
- Copying Apple point values as CSS pixels is incorrect without considering platform/context.
- Giant bright buttons do not automatically improve conversion or comprehension.
- A visually convincing disabled button may be undiscoverable to assistive technology.
- Icon-only labels can become ambiguous and require accessible names.

## Future verification
Capture documented side-by-side button variants from official design-system examples; test task comprehension, contrast, keyboard access and loading states at desktop/mobile viewport sizes. Record version, URL and date.