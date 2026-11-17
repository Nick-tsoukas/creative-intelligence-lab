# Findings: consequence, confidence and taste

For a material finding, state the affected person/task, exact location, evidence,
user consequence, smallest appropriate repair and how to verify it. Add regression
risk when it changes the decision. A small repair needs no nine-field dossier.

Classify the claim before assigning priority:

- **Confirmed defect:** reproduced behavior or directly observed visual/semantic failure, with scope. A screenshot can confirm clipping, not failed persistence.
- **Plausible risk:** evidence supports a possible harm; identify the smallest check that could confirm or reject it. High potential impact merits investigation, not invented certainty or automatic redesign.
- **Preference disagreement:** a tradeoff/taste judgment. Explain its effect on the brief and let the proper decision maker choose; it is not automatically a defect.

| Severity | User consequence | Example |
|---|---|---|
| P0 | Serious privacy, financial or irreversible harm | Private media exposed; wrong-audience send |
| P1 | Core task blocked, meaningful work lost or consequential state falsely trusted | Failed save reports success and discards the buffer; keyboard cannot reach Save |
| P2 | Recoverable confusion or repeated friction | Redundant selection; unclear but reachable action |
| P3 | Minor defect with little task impact | Small inconsistency without impaired perception or use |

Grade what happens to the user, even when a narrow specification omits it.
A contrast issue that hides an essential control is not cosmetic. A local-only
prototype can still lose real writing; its declared boundary does not excuse false
local success. Conversely, a deliberately unsupported production integration is
not a prototype defect when it is disclosed and irrelevant to the decision.

Priority considers consequence, reach and confidence without invented arithmetic.
Reviewer labels are advice: verify claims, resolve material defects and explain
any disagreement. Do not turn every review suggestion into implementation work.

Use REPORTED / OBSERVED / TESTED / INFERRED when the distinction changes a
consequential decision. Generated personas remain hypotheses; stakeholder
preferences are reports; tests establish only their actual tested behavior.
No fabricated metrics, interviews or approvals.
