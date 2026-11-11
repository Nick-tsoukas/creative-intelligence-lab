# Signal Archive — Validation Plan (Not Yet Executed)

## Execution environment
Use a **separate throwaway sandbox**. Document git repo, commit, runtime, node version, package manager, browser versions and exact viewport sizes.

## Functional scenarios
- Search "rain" matches title and/or location as specified.
- Search with no matches shows count 0, informative empty state, clear reset.
- Category Nature returns the appropriate results.
- Clearing filters restores all six.
- Toggle a favorite via pointer and keyboard; accessible pressed state and visible feedback are correct.
- If no actual licensed original audio exists, preview is clearly labeled as unavailable/demo and is **not** a fake play button.

## Semantics and inclusive interactions
- One logical page heading and headings in hierarchical order.
- Use semantic links/buttons/search input, labels, visible focus.
- Tab order follows reading order; no keyboard trap.
- Status updates announced appropriately (e.g. aria-live for result count, not excessive).
- Text contrast, focus contrast and non-color-only state indicators.
- 320 CSS px reflow, 200% text zoom, 390×844 mobile, 1440×900 desktop.
- Prefers-reduced-motion disables nonessential motion.
- Error/empty/loading states actually rendered and inspected.

## Performance and engineering
- Record Lighthouse/Core Web Vitals only when actually measured; specify hardware and network if possible.
- Verify no client-only hydration mismatch if Nuxt.
- No oversized images or autoplay media.
- Test in actual browser; static screenshot does not prove interaction.
- Check console errors, no external tracker, no credentials.

## Art direction critique
- Does the specific idea arise from *field-recording archival practice*?
- Can an unfamiliar user discover sounds without deciphering the artistic metaphor?
- Do typography and color form a recognizable system rather than a generic card layout?
- Does experience survive no motion, narrow screen and high zoom?
- What is most memorable? Does it support use?

## Evidence artifacts
- IMPLEMENTATION_PLAN.md
- SCREENSHOTS.md with hashes/URL/viewport/date and rights status
- DESIGN_REVIEW.md with issue priorities
- HANDOFF.md, final decision and next iteration
- Automated test logs if any

## Explicit current results
All checks: **NOT RUN**. No passing scores may be recorded until actually executed.
