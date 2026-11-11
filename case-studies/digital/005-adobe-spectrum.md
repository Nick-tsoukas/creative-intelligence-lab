# 005 — Adobe Spectrum: visual language as a scalable system

- **Primary source:** https://spectrum.adobe.com/getting-started/introduction
- **Additional official release:** https://spectrum.adobe.com/page/whats-new/
- **Access:** 2026-11-11, official introduction and dated release documentation.
- **Evidence:** DOCUMENTATION-INSPECTED / EXCERPT-REVIEWED. No hands-on cross-platform evaluation.

## Documented facts
**FACT:** Adobe describes Spectrum as a shared foundation for design and engineering across products and platforms, intended to preserve coherence while allowing variation by context. Spectrum 2 develops foundations in color, typography, layout, icons, states and components. Adobe's September 30, 2026 Spectrum Hub announcement describes consolidated guidance, component resources, implementation examples and interactive playgrounds.

## Design interpretation
**INTERPRETATION:** A design system is not just a component kit or color palette; it is a *set of decisions about variation*. If components share behavioral and aesthetic principles, different products can preserve recognizable coherence while adapting to distinct tasks.

This is a contrasting model to GOV.UK: one system spans a portfolio of sophisticated creative tools with varying interaction demands.

## Risks
- Systemwide consistency can become rigidity if product-specific creative needs are ignored.
- Cross-platform component parity is challenging; do not assume every feature works equally on every OS.
- A design system's marketing promises do not establish real-world accessibility or performance.

## Transferable lessons
1. Define semantic design tokens, not isolated hex values.
2. Treat interaction states, typography and accessibility as system foundations.
3. Document where variation is permitted and where consistency is required.
4. Maintain versioned guidance and migration paths for system changes.

## Verification backlog
Inspect concrete Spectrum components and playgrounds; compare keyboard/focus and responsive behaviors; study real Adobe application use-cases; verify published implementations and licensing independently.