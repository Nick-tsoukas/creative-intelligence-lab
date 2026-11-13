# Experiment 003 — Music Art-Direction Contrast: Browser Evidence

**Date:** 2026-11-13. **Status:** isolated fictional-music sandbox actually rendered via headless Chromium. NOT a production Faneqo redesign, a Claude implementation, an independent study, or proof of superiority over a strong baseline.

## Question and design
Compare two treatments with identical fictional AMPLIFY. brand/copy, nav, CTA, feature copy and original CSS-art motif:
- A: neutral system typography, rounded blue CTA, quiet blue abstract illustration.
- B: condensed oversized editorial display, warmer paper, hard red accent, angled stage-poster-like original illustration and sharper composition.

This exploratory pair changes multiple visual properties, so it cannot isolate one effect; both variants were authored in this session, not by independent implementers. It is NOT the official blinded baseline-vs-Lab comparison.

## Actual browser evidence
- Python Playwright + locally available Chromium; HTML injected through set_content because direct local navigation was blocked by administrator policy.
- Captured six full-page PNG screenshots: A/B at 1280×800, 390×844 and 320×640.
- Repeated after correction: all **6/6 viewport x direction observations** had document scrollWidth equal to clientWidth; none had horizontal overflow; JavaScript page errors zero.
- Both directions displayed one primary heading and one Explore CTA; switching direction control correctly updated rendering.
- Basic focus on direction selector and existence of navigation hash targets verified.
- Exact HTML, test script, screenshots, run JSON and log are packaged in user-accessible sandbox ZIP at /mnt/data/creative-lab-comparison-001.zip. The ZIP is NOT in GitHub; the GitHub repo only receives this experiment report. A later contributor must obtain the archive separately rather than assume it is part of the repository.

## Defect found by actual visual inspection
At 390px, the expressive poster caption was hard to read over a red diagonal stripe, despite no overflow or JS errors. Fixed by adding a near-opaque dark label field, padding and higher stacking order. Misleading nav label “Join” (linked only to CTA) was changed to honest “Explore” (links to actual section). Re-ran all checks, pass.

**Inference:** human eyes-on critique detected a meaningful visual defect that an overflow-only test could not. This is a procedural lesson, not an efficacy claim about the overall Lab system.

## Test limits (not done)
- Human participant tasks, screen reader, complete keyboard navigation, 200% zoom, automated contrast evaluation, speed/Core Web Vitals, cross-browser comparison, deployed network/navigation checks, real music photography, real product content.
- No independently rated visual originality or task superiority.
- The original CSS illustration is educational placeholder artwork, not an authentic musician identity.
- This is NOT verification of Experiment 002's GitHub Actions workflow or its authored Playwright suite.

## Next stage gates
1. Improve the paired-artifact setup: genuine licensed artist imagery, stronger neutral baseline, frozen real product facts, isolated creative-direction packet and equal implementation budget.
2. Add a mandatory screenshot review gate to design skill: capture desktop/mobile, list concrete defects, correct then retest.
3. Add keyboard, reduced motion, 200% zoom, contrast and screen reader checks.
4. Execute Pilot 002 comparison after owner authorizes isolated Faneqo mockup implementation and Claude becomes available.
5. Preserve source/provenance and do not imply that this experiment establishes world-class artistic quality.

No Faneqo application code was modified.
