# Research Note 003 — Two Kinds of Digital Excellence

**Date:** 2026-11-11  
**Status:** Comparative synthesis / preliminary; five official published case studies and design-system documents inspected; no independent interactive accessibility or performance audit.

## The five cases
| Case | Strongest stated design problem | Evidence type | Read |
|---|---|---|---|
| [FinalFinal](../case-studies/digital/001-finalfinal.md) | Music collaboration: structured workflow vs creative energy | Studio case study | Official text |
| [David Whyte](../case-studies/digital/002-david-whyte.md) | Literary emotion through watercolor, sound and 3D | Studio case study | Official text |
| [Linear 2026](../case-studies/digital/003-linear-2026.md) | Reduce visual noise in information-dense product | Designer-authored change explanation | Official text |
| [GOV.UK](../case-studies/digital/004-govuk-components.md) | Reliable reusable task-completion components | Official component documentation | Catalog |
| [Adobe Spectrum](../case-studies/digital/005-adobe-spectrum.md) | Coherent product families without erasing context | Official system introduction | Foundation |

## Original comparative interpretation
### 1. Attention is a budget
The creator-oriented experiences compete for *emotional attention*; Linear is explicitly reducing competing visual emphasis in repeated work. Both use hierarchy, but the objective varies by task. An expressive homepage may need a memorable gesture; an editor may need quiet controls and predictable feedback.

### 2. Art direction can demonstrate a subject
FinalFinal describes using storytelling and interaction to represent collaboration. David Whyte's studio associates fluid watercolor imagery and sound with poetry. In both, distinctive media is justified **in relation to content**, not because it happens to be trendy.

### 3. Components are promises
A dialog, file upload, navigation control or form promises a predictable behavior. GOV.UK and W3C APG foreground functionality and keyboard semantics. Spectrum addresses the larger problem of preserving such coherence across multiple products and contexts.

### 4. Design-system craft requires both restraint and permission
Linear demonstrates subtraction; Spectrum describes shared foundations with contextual flexibility. A brand system must say *what stays consistent* and *where creative variation is allowed*. Excessive consistency can become blandness; arbitrary variation becomes fragmented.

## Proposed two-axis evaluation
For each case study, assess independently:
- **Expressive quality**: identity, emotional coherence, visual originality, narrative, craft.
- **Operational quality**: clarity, task success, component affordances, accessibility, resilience, performance.

Do not convert these into a single score without explaining weights and task context.

## Unverified
No actual mobile/keyboard/screen-reader/user testing was performed for these five cases. No Lighthouse scores or conversion data were collected. Treat any such claim as **UNKNOWN**.

## Next experiments
1. Compare FinalFinal's narrative product explanation with a plain text/task-oriented alternative in a small comprehension study.
2. Compare older vs updated Linear navigation in first-time and experienced-user task trials.
3. Build a cross-system dialog component matrix against W3C APG, then keyboard test real examples.
4. Record actual device, viewport and accessibility checks for each case before upgrading evidence status.

## Original primary references
- https://locomotive.ca/en/work/finalfinal
- https://immersive-g.com/projects/david-whyte-experience/
- https://linear.app/now/behind-the-latest-design-refresh
- https://design-system.service.gov.uk/components/
- https://spectrum.adobe.com/getting-started/introduction
- https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
