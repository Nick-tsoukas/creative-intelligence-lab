# One compact design decision record

Reuse the existing brief, ticket, project log or visual workspace. This is an
optional shape, not another required document. Link detailed logs and captures.

- **Decision:** user job; interface mode (skip for source-only research); prototype / production / research; what must be real; owner choice/authority status.
- **Evidence:** only sources, current code, observed pixels and behavior that change the decision. Label REPORTED / OBSERVED / TESTED / INFERRED where material. Record unsupported boundaries once.
- **Material findings:** confirmed defect / plausible risk / preference; affected person and consequence; bounded repair or next check. Optional refinements stay deferred.
- **Verification:** affected behaviors/states and valid captures actually inspected, with result/location. Reuse unchanged evidence; engineering owns full-suite requirements.
- **Limitations:** specific unverified claims, unavailable evidence and what they prevent deciding. A disclosed irrelevant production boundary does not block a prototype choice.
- **Next action:** fix, choose, implement under existing authority, or stop. Reopen only for a material defect, changed requirements or invalid/insufficient critical evidence.

For visual exploration/review, add two short independent judgments:

**UX reliability:** what is understandable, completable, recoverable and truthful;
behavior evidence and remaining uncertainty.

**Creative quality:** strongest content-specific relationship; weakest decision
and its effect on composition/hierarchy, typography/spacing, authentic imagery/art
direction, interaction clarity and mobile transformation; concrete next correction.
Name the captures actually opened (route/state/role/viewport) and separate
OBSERVED pixels from INFERRED intent. Automated capture/overflow checks validate
capture or geometry, not aesthetics or task success. A behavior-test count is not
an aesthetic verdict.

Each concept: `organizing idea → intended impression → task benefit → sacrifice`.
Name self-review versus independent critique and who actually selected/approved.

## Optional implementation handoff

Use only when another agent will build. Fill every key once; summarize rather
than repeat the review. Mark unknowns with a source check, and reserve reviewer/
owner questions for choices the codebase cannot resolve:

`Routes/components: [names or UNKNOWN + lookup] | Locked/open: [decisions] | Actions/data: [contracts and distinct state truth] | Desktop→mobile: [transformation] | Accessibility: [requirements] | Acceptance: [observable outcomes, including applicable loading/empty/error/retry states] | Visual verification: [states/viewports/screenshots to render and inspect]`

After a meaningful task, optional field note: skill/version; decision changed or
defect found; unnecessary work caused/prevented; actual owner/user response;
quality outcome (including unknown); confounds; retain/revise/drop guidance.
