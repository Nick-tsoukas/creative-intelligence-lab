# Perception Workbench — Study Protocol and QA

**Instrument:** [standalone workbench](index.html). **Created:** 2026-11-13. **Status:** GitHub code committed and static checks run; NO independent browser session, screenshots, human participants, screen-reader evaluation, or performance measurement have been completed.

## Purpose and research boundaries

Explore three separable perceptual questions raised in [Research 011](../../research/011-PERCEPTUAL-ORGANIZATION.md):
1. How does changing visual emphasis move attention among unchanged pieces of text?
2. Does spatial grouping help viewers identify which label belongs to which category?
3. Do identical sRGB patches appear different on different backgrounds?

Do not confuse the teaching interface's interactive controls with a valid controlled user study. The interface currently presents variants sequentially selected by the observer, not randomized and not blinded. Thus order/expectancy, demand and observer effects are uncontrolled. The single answer after each variant is a subjective report, not an accuracy or response-time measurement.

## Exact content and conditions

**Study A: visual weight**
- Unchanged text: “Find the signal.” / “A curated archive of remarkable sounds.” / “Explore recordings”.
- Conditions: single focal point, asymmetric balance, competing emphasis.
- Outcome: self-reported first-noticed element, no timed measure.
- Confound: layout, type size and color change together. It tests a *composite art direction*, not a causal effect of any one property.

**Study B: grouping**
- Identical six labels arranged into Discover (Field recordings, Collections, Curator picks) and Your archive (Saved sounds, Recent listens, Playlists).
- Conditions: explicit containers, loose boundaries, mixed alignment.
- Outcome: selected category of “Recent listens”, or “unclear”.
- Confound: headers are hidden in loose condition and layout DOM order shifts visually, so the conditions change both semantics and positioning. No claim that proximity alone caused any difference.

**Study C: contextual color**
- Identical center-patch CSS background: `#a69a74` on A and B, with identical border.
- Surrounds: dark vs warm light; identical; inverted.
- Outcome: chosen apparent lighter patch, or equal.
- Confound: perception differs by display settings, brightness, adaptation and color vision; no calibrated monitor, no randomized assignment.

## How to run locally

Open `index.html` in a modern browser (it uses no dependencies). For clipboard export, use localhost or HTTPS because Clipboard API may be unavailable under `file://`.

Example:

```bash
cd experiments/002-perception-workbench
python3 -m http.server 8765
```

Then open `http://localhost:8765/`. Responses exist only in current tab memory; refresh destroys them. The JSON export is manual and contains no names or location by design, but does contain client timestamps.

**Do not deploy to a public participant collection service** without a privacy notice, informed consent plan and appropriate review. This prototype does not collect remote data.

## Required engineering QA (PENDING manual/browser execution)

| QA | Steps | Pass criteria | Status |
|---|---|---|---|
| Desktop | Visit at 1280×800 and switch all three tabs | no overflow, all stage panels visible | NOT TESTED |
| Mobile | Visit at 390×844 and 320×640 | no sideways document scroll, legible stimuli | NOT TESTED |
| Keyboard | Tab across tabs; ArrowLeft/Right/Home/End | selected tab and focused panel correspond | NOT TESTED |
| Form | choose radio on each study, record, reset | count increments, data resets, status announces | NOT TESTED |
| Clipboard | run from localhost secure context and Copy | valid JSON, correct variant/answer | NOT TESTED |
| Reduced motion | emulate media feature | no unintended transitions | NOT TESTED |
| Screen reader | VoiceOver/NVDA read tablist and radio questions | usable labels and announcements | NOT TESTED |
| Browser compatibility | Chromium, Firefox, Safari | no functional regressions | NOT TESTED |
| Visual QC | inspect variants manually | intended contrasts, no clipping or overlap | NOT TESTED |

## Static checks performed on GitHub source (2026-11-13)

A small structural inspection (NOT runtime QA) found all 12 conditions true:
- HTML document has closing tag; three `tabpanel`s; three selectors; three experiment stages.
- Tabs handle arrows plus Home/End.
- Two inactive tabs initially hidden.
- Three form fieldsets.
- Reduced-motion media query present.
- No `innerHTML` insertion, network requests, local/session storage or external images.
- GitHub file length 13,018 characters.

**Known limitations found before visual execution:**
- The grouping conditions intentionally change multiple dimensions, so inference must be described as broad compositional comparison.
- The tablist follows common ARIA patterns, but accessibility cannot be declared compliant without actual keyboard/AT checks.
- Responses have no randomized condition assignment or per-condition participant ID, so this is *not* suitable for formal statistical inference.
- The optional clipboard feature depends on secure contexts.

## If proceeding to a real comparative research test

1. Freeze stimuli and isolate one variable at a time. Do not change header availability and proximity simultaneously.
2. Randomize condition order (or counterbalance), and assign coded participant IDs without identifying personal data.
3. Define primary outcomes before testing: task-completion correctness for grouping, first fixation **only if eye-tracking exists**, otherwise timed first click / self-reported first noticed.
4. Establish recruitment/consent and minimum readable sample targets, plus accessible alternatives.
5. Separate qualitative observations from quantitative measurements, and archive the exact stimulus version/hash.
6. Compare desktop and mobile and keep a neutral baseline.

## References
- NN/g Proximity Principle: https://www.nngroup.com/articles/gestalt-proximity/
- W3C Understanding Focus Visible: https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
- W3C Understanding Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- MDN Reduced Motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion
- [Perceptual Composition Card](../../handbook/PERCEPTUAL-COMPOSITION-CARD.md)

No artwork reproductions are embedded; all stimuli and text are original to the Lab.

## Browser automation scaffold (committed, NOT executed)

A Playwright Test spec is available at [workbench.spec.mjs](workbench.spec.mjs), with 9 automated test cases including 3 viewport sizes. It is **not evidence of a passing test run**.

Run inside this directory once Node and Playwright Test are available:

```bash
npm install --no-save @playwright/test
npx playwright install chromium
npx playwright test workbench.spec.mjs --browser=chromium
```

This creates or updates only local experiment dependencies. Keep this environment isolated from the Faneqo application repositories and do not modify the Faneqo application repositories. Record exact browser, OS, viewport, errors and screenshots. Any test failure must be investigated before claiming the study's layout is correct.

This automation checks only testable DOM/behavior claims; it does not replace manual visual perception, keyboard, screen reader or participant studies.
