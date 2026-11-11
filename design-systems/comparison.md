# Major Design Systems — Comparative Research Matrix

**Date:** 2026-11-11. **Status:** OFFICIAL-DOCUMENTATION-REVIEWED (catalog pages and guidance, not component-level cross-browser tests).

| System | System priority | Best research questions | Official source |
|---|---|---|---|
| Apple HIG | Platform coherence, purpose, agency, craft | How do control anatomy and behaviors adapt across devices? | https://developer.apple.com/design/human-interface-guidelines/ |
| Google Material 3 / Expressive | Adaptive components; salience, expression, tokens and motion | When does more expressive UI improve task performance? | https://m3.material.io/ |
| Microsoft Fluent 2 | Coherent products across web/iOS/Android, code-aligned kits | How do Figma variables and component variants map to code? | https://fluent2.microsoft.design/get-started/design |
| IBM Carbon | Enterprise UX, data-rich workflows, accessible components | How does hierarchy hold under tables, forms and data visualization? | https://www.carbondesignsystem.com/ |
| Shopify Polaris | Native-feeling merchant-facing embedded tools | How can framework-independent web components constrain styling yet improve platform coherence? | https://shopify.dev/docs/api/polaris |
| Adobe Spectrum | Shared foundations for diverse creative products | Which global tokens and states should remain consistent across different tools? | https://spectrum.adobe.com/ |
| GOV.UK | Public-service task reliability and accessibility | How do field labels, error summary, keyboard and content guidance support completion? | https://design-system.service.gov.uk/ |
| Atlassian Design System | Dense collaboration and task workflows | What are useful patterns for complex navigation and project views? | https://atlassian.design/ |
| Salesforce Lightning Design System | Enterprise application interfaces | How are complex data and form controls governed? | https://www.lightningdesignsystem.com/ |
| GitHub Primer | Developer workflows and scalable visual consistency | How are semantic tokens and components shared across browser and React contexts? | https://primer.style/ |
| USWDS | Federal public service accessibility | How are service patterns, plain language and accessibility documented? | https://designsystem.digital.gov/ |
| W3C WAI APG | Interaction semantics and keyboard patterns | What does a component *promise* when called a dialog, tabs or combobox? | https://www.w3.org/WAI/ARIA/apg/patterns/ |

## Notes from official documents
- **Fluent 2:** Microsoft offers Figma UI kits for web/iOS/Android; system assets are organized as language, core, Copilot and Labs layers. Styling variables include color, stroke, corner radii, spacing and size. These can help bridge design/dev vocabulary.
- **Carbon:** IBM describes an open-source, enterprise-ready system with foundations, components, patterns and data visualization. Its current documentation also advertises an AI-facing Carbon MCP; evaluate compatibility/security independently before adopting.
- **Polaris:** Shopify's current web component documentation describes framework-independent native custom elements used within Shopify apps, with versioned releases; admin-context styling constraints differ from freeform product websites.
- **Spectrum:** Research notes already exist in `case-studies/digital/005-adobe-spectrum.md`; avoid duplicating unverified performance claims.
- **GOV.UK:** See `case-studies/digital/004-govuk-components.md`.

## Comparative lessons (hypotheses)
- A system's excellence depends on its **environment of use**: market, device, frequency, risk, complexity, authoring tools.
- A premium-feeling system may achieve polish with restraint (Apple) or with deliberate expressive salience (Google); neither is universal.
- A design system is governance of permissible variation, not simply a component gallery.

## Next research depth
Choose the same component (button, dialog, navigation, form errors, tabs) in at least four systems and compare anatomy, states, keyboard/focus, accessible name, motion, dark mode, breakpoint behavior and API. Cite the exact component page and version. Avoid declaring a winner without a task/context.