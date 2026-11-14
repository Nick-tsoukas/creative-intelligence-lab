# UX Issue Triage and Evidence Contract

A finding must specify **who**, **task**, **where**, **observation**, **impact**, **evidence type**, **proposed minimal repair**, **regression risk**, **verification test**.

| Severity | Condition | Faneqo illustrative example |
|---|---|---|
| P0 correctness/privacy | Irreversible wrong-audience send, public exposure of private photo, false delivery certainty, duplicate send with real fan impact | A gallery unexpectedly becomes public when attached |
| P1 critical task block | Can't send eligible message, draft lost, keyboard user cannot reach composer, trapped workflow | Returning from new gallery erases composed text |
| P2 friction/ambiguity | Repeat recipient selection, confusing navigation, unlabelled ambiguous icon | Artist must reselect same Night after clicking Message attendees |
| P3 refinement | Contrast and spacing polish that doesn't prevent task, minor inconsistent affordance | Underdeveloped welcome composition |

**Severity is contextual:** a P3-looking visual issue can become P1 if an essential control is not perceivable.

Priority = consequence × frequency/reach × confidence, with uncertainty named. Do not multiply invented numerical scores.

### Audit output example
```
Issue UX-001 | P1 | INFERRED FROM SCREEN / needs browser test
Task: create an attendee announcement with show gallery
Observed: two visible entry buttons appear to lead to distinct composers
Risk: artist may not understand where draft and gallery attachments live
Minimal proposal: route both entries into one composer, keep their preselected audience separate
Verification: full local flow, refresh, keyboard, privacy check and founder first-use test
```

### Evidence labels
- OBSERVED — direct screenshot/browser/code observation with scope
- REPORTED — founder or participant account, not independently reproduced
- INFERRED — consequence grounded in evidence but not tested
- HYPOTHESIS — new proposed improvement or behavioral prediction
- TESTED — reproducible completed task/browser observation with date/device
- NOT TESTED — explicit missing coverage

Never turn heuristics or founder frustration into invented metrics.
