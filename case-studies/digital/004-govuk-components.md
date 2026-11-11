# 004 — GOV.UK Design System: reusable UI as public infrastructure

- **Primary artifact:** https://design-system.service.gov.uk/components/
- **Complementary authoritative reference:** https://www.w3.org/WAI/ARIA/apg/patterns/
- **Access:** 2026-11-11, official component catalog and W3C APG documentation.
- **Evidence:** DOCUMENTATION-INSPECTED; not an independent live screen reader or user test.

## What is verifiable
**FACT:** GOV.UK defines components as reusable interface elements, provides usage guidance and examples for forms, navigation, status, and more, and publishes implementation code. The catalog includes text inputs, error messages and summaries, confirmation panels, notification banners, pagination, radios, tabs, checkboxes, date input, and other patterns. The code is published under an MIT license as stated by the GOV.UK site.

**FACT:** W3C APG's dialog pattern specifies focus entering the modal, tab navigation remaining inside, Escape closing the dialog, and focus usually returning to the invoking control. APG examples are illustrative rather than an independent accessibility guarantee.

## Analysis
**INTERPRETATION:** GOV.UK's visual restraint is intentional functional infrastructure: predictable elements are more valuable for completing important tasks than novelty at each step. Designers focus on *the contract of the component*: instructions, states, focus, error recovery and completion.

Unlike cinematic marketing sites, the unit of quality here is often the reliability of a single user action under varied conditions.

## Component lesson: error summary + field error
For multi-field forms, consider a top-level error summary that links to relevant controls, in addition to clear local error text. Compare semantics, focus management, where errors appear, and whether user input remains intact. This is a research pattern and should be evaluated against the precise task and GOV.UK guidance, not universally mandated.

## Limitations
Documentation does not tell us whether a particular service implemented the components correctly. No hands-on keyboard/screen reader audit was conducted; none is claimed.

## Transferable lessons
1. Maintain usage **guidance and code examples together**.
2. Test components across disabled, validation, loading, error, success and responsive states.
3. Accessibility is a behavioral contract, not just the presence of ARIA attributes.
4. Keep brand expression mostly compatible with learned interaction conventions.

## Next test
Select three patterns (dialog, error summary, file upload) and evaluate a real implementation against its authoritative guidance, with keyboard and assistive technology checks.