# Check what the action really does

For each primary action and any visibility, money, deletion, publication or transmission action, verify the chain:
visible sentence → input/handler → request → validation/authorization → stored state → downstream effects → visible result.

Record `action | stores/links | publishes where/to whom | sends/notifies | third parties | defaults | eligibility | failure/retry | evidence`. Unknown effects stay UNKNOWN. Distinguish stored/published/notified and queued/sent/delivered. Attaching content must not silently broaden its audience. Product wording must not promise telemetry the system lacks.

Treat visible explanatory sentences as factual claims: disabled reasons, cover selection, counts, saved indicators, audience summaries, and what happens next. Verify material claims against actual code and, when authorized, runtime outcomes. This is targeted verification, not an instruction to prove every adjective through code.

Before a risky action, explain who and what it affects with enough context to choose. Defaults involving another public surface require explicit product reasoning; a reported surprising default is evidence to investigate, not an automatic directive to change policy.

After submission, verify the relevant readback or server state and exactly-once intent where applicable. A network acceptance response may prove acceptance, not delivery. Test interruption and uncertain confirmation before offering a retry that could duplicate effects. Use synthetic or authorized data. Do not send messages, publish private content or weaken authorization solely to test the design.
