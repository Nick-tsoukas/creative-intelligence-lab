# Apple Human Interface Guidelines — An Art Direction & UX Reading

**Date reviewed:** 2026-11-11  
**Evidence:** OFFICIAL-GUIDANCE-REVIEWED (text-based official HIG, WWDC documents and Apple's public guidance). **Not** a device interaction test or a full HIG reading.

## Primary references
1. Design principles — https://developer.apple.com/design/human-interface-guidelines/design-principles/
2. Human Interface Guidelines — https://developer.apple.com/design/human-interface-guidelines/
3. Layout (updated September 9, 2026) — https://developer.apple.com/design/human-interface-guidelines/layout
4. 2026 Apple design guidance — https://developer.apple.com/wwdc26/guides/design/
5. WWDC25 design system presentation — https://developer.apple.com/videos/play/wwdc2025/356/
6. Apple Design Resources / official UI kits — https://developer.apple.com/design/resources/

## What Apple actually says (attributed, not independent UX proof)
Apple's HIG identifies eight principles: **purpose, agency, responsibility, familiarity, flexibility, simplicity, craft and delight**. Apple's guidance explicitly says there is no one right way to apply the principles.

### Purpose / agency / responsibility
- Make the primary user benefit meaningful.
- Let people explore, back out, recover and understand consequences.
- Prioritize privacy, transparency and users' interests.
**Interpretation:** Good visual hierarchy starts with *what deserves attention* and what control the user retains, not with how striking the screen looks.

### Familiarity / flexibility
- Keep learned patterns consistent, account for different inputs and platforms, preserve context when adapting.
- Apple's 2025 design presentation describes continuity through shared component anatomy even as platform-specific structures differ.
**Interpretation:** Consistency can be behavioral rather than pixel-identical. A sidebar, tab bar and menu may look different but communicate selection and location coherently.

### Simplicity / craft / delight
- Apple distinguishes simplicity from minimalism: include what is necessary.
- Craft includes careful animation, wording, visuals and iteration.
- Delight should not obstruct the task.
**Interpretation:** The most powerful lesson isn't rounded corners or translucency; it's *editing* to give content space and interactions clarity.

## Current design specifics to investigate
- Apple 2026 HIG layout discussion mentions progressive disclosure, grouping, adaptable layouts, differentiated controls vs content, Liquid Glass and scroll-edge behaviors.
- Liquid Glass is a platform material concept, not a universally appropriate CSS trend. The web has different accessibility, GPU and browser constraints.
- Apple Design Resources includes official platform UI kits and device templates; inspect their terms and platform scope before reusing them.
- Apple's older standalone design tips mention minimum 44 × 44 pt touch targets for that context. Do not generalize pt = CSS px or assume a single number guarantees accessible hit targets.

## Visual examination guide
Study actual layout images and demos via official pages. For each:
- Identify content region, chrome, toolbar and gesture focus.
- Compare narrow vs wide and text size changes.
- Inspect where content appears beneath material; record perceived contrast.
- Check focus visibility, labels, discoverability and reduced-transparency behavior if available.

**Screenshots:** [visual library capture queue](../visual-library/README.md). No independently captured 2026 Apple screenshot is in the repo yet.

## Critique and limitations
Familiarity can become platform convention and may not suit a cross-platform branded web experience. Beautiful translucent materials can reduce text/edge distinction if poorly implemented. HIG is guidance from Apple, not independent evidence that every Apple product has excellent UX.

## Research question
Can an experience feel premium by giving people *agency and confidence* rather than by increasing decorative detail?

## Transfer
Carry forward purpose, coherent structure, agency, polish and responsive context. Do not replicate trademarked Apple UI or imply Apple endorsement.