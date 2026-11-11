# Forms, Error Recovery and Tab Navigation

**Access:** 2026-11-11, GOV.UK and W3C official docs reviewed.

## Primary sources
- GOV.UK error summary: https://design-system.service.gov.uk/components/error-summary/
- GOV.UK error message: https://design-system.service.gov.uk/components/error-message/
- GOV.UK text input: https://design-system.service.gov.uk/components/text-input/
- W3C APG tabs: https://www.w3.org/WAI/ARIA/apg/patterns/tabs/

## Forms: verified GOV.UK approach
GOV.UK recommends a page-level error summary **and** a local field error message. Its error summary must link to problem inputs, use matching wording, and (with govuk-frontend JS) receive keyboard focus when validation fails. It specifically advises preserving user-entered values, including invalid values, when presenting errors. Error wording should describe the concrete issue and recovery, not a generic 'an error occurred.'

**Practical synthesis:** error recovery is not merely a red border. It is a navigation and comprehension problem: detect → announce → locate → understand → correct → confirm.

### Original hypothetical example
Wrong: **Invalid input** below a field after submission, with all fields cleared.
Better: An error summary linked to Email; local message **Enter an email address** or **Enter an email address in the correct format** as appropriate, original values preserved, focus moved to the summary for long forms.
This example is our illustration, not a claim of testing a specific public service.

## Tabs: W3C APG verified behavior
A `tablist` contains `tab` elements; each corresponds to a `tabpanel`. Arrow keys move among tabs; Enter/Space activate tabs when manual activation is used. Automatic activation is advised when panels can display without noticeable delay; otherwise moving focus could trigger expensive loading. Active tab state is communicated via `aria-selected`; labels and panels are associated.

**Critical distinction:** a site navigation set of links styled like tabs is **not** automatically an ARIA tabs widget. Use actual links for destination changes; tabs are appropriate for related panels within a view. This is a synthesis of semantic expectations, not a rigid ban on all alternate designs.

## Comparative questions
- Is error context clear at the top and beside fields?
- Does the interface retain valid responses while fixing invalid ones?
- Can users recover using keyboard only?
- Are focus and aria-describedby relationships correct?
- Is tab selection visually distinct *without color alone*?
- Are panels loaded so keyboard focus movement remains responsive?

## Failure modes
- Error tooltip shown only on hover.
- Focus moved to a hidden field.
- Form data cleared after validation.
- Tabs that only respond to mouse clicks.
- Automatic activation with a slow remote API on every arrow key.
- Different labeling for field and summary errors.

## Next step
Create real test fixtures in a separate experimental environment; log desktop/mobile screenshots, keyboard traces, focus states and accessibility checks. Do not claim a full usability study from documentation alone.