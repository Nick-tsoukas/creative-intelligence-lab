# Independent UX Skill Evaluation — Evidence Protocol

**State:** Prepared for later, **NOT EXECUTED**. Founder explicitly deferred standalone formal benchmarks and extra test sessions. Run normal project QA when an app feature actually changes, but do not run unrelated evals now.

## Two separate questions
**Activation:** Did Claude decide to use this skill for the right task, and abstain for wrong tasks? Measure positive/negative triggers independently of output. A direct `/elite-ux-director` invocation proves manual availability, not automatic activation.

**Quality:** When the skill is available, did the response **correctly** identify the real issue and propose a safer, more useful resolution than baseline? Measure independently of length, tone, number of cards loaded and visual polish. Structure isn't causal evidence.

## Evidence types and independent review
- **Ground-truth defect:** confirmed from current product code, observed UI or executed real task; attach route/commit/test/state.
- **Seeded fixture:** synthetic scenario with a known failure and hidden expected invariants; NEVER present as a verified live bug.
- **Founder report:** first-person frustration is valid but not measured across a user population.
- **Generated persona:** hypothesis only. Real role/venue field data must have method/sample provenance.
- **Reviewer independence:** the generating agent does not grade its own output as a final source of truth. Use a separate reviewer or verifiable deterministic outcome; hide “baseline vs skill” label where practical. Record disagreements instead of averaging them away.

## Minimum matched comparison (when authorized later)
1. Choose **actual current tasks** first; include a couple of negative non-UX prompts to detect over-triggering.
2. Freeze model/version, task brief, project checkout, access to screenshots, tools, source material and time/context budget. Each condition starts in a fresh context.
3. Compare baseline without skill and with skill **at similar access/time**, without secretly giving one condition extra product facts.
4. Record activation events, tool/reference reads, final response and actual code changes if authorized. Two to three repeated trials may help for stochastic behavior, but do not fabricate a win rate from one.
5. Score separately: (a) high-severity true defects found, (b) serious misses, (c) unsafe suggestions (recipient, auth, privacy, irreversible actions), (d) false facts, (e) bounded repair and verification, (f) excessive work / context cost, (g) independent aesthetics if the task actually requires visual direction.
6. Use a non-compensatory safety check: a good paragraph about visual design cannot offset an unsafe privacy recommendation.
7. Compare real outcomes after the authorized implementation, noting confounds and missing user observations; don't claim statistical significance without appropriate sampling.

## Activation fixtures
The canonical machine-readable table is `quality/ux_skill_eval_cases.json` **in the Lab repository**, outside the installed skill. Cases deliberately cover positive and negative triggers across domains, without depending on Faneqo product knowledge. They are design fixtures for a future evaluation, not results.

## Quality fixture guide
Eight existing scenarios in `EVALUATION.md` focus on high-stakes messaging/privacy. Do not modify their seeded assumptions to fit a skill answer. Add QR, forms and cross-industry scenarios in the repository quality set; include at least:
- wrong-artist QR fallback, draft loss, public/private exposure, and status-as-delivered misrepresentation
- a clearly backend-only task where UX skill should not activate
- an interface art-direction task where Concept Exploration applies, and a standalone poster/brand research request outside this skill's scope
- a multi-actor permissions case with evidence-based rather than synthetic-persona reasoning
- accessibility keyboard/focus case tied to actual interaction not bogus ARIA labels

## No false progress claims
Package checks prove file structure and parsing, not skill effectiveness. A model that lists the correct source names without applying the mechanisms is not successful. A model that suggests a radical new UI without correct authority/lifecycle behavior is unsafe.

## Natural feedback loop
For **existing** authorized work, a developer can log:
```
case_id / date / task / source_version
observed user issue / route & code evidence
did skill activate? / what references were actually used
critical correct findings / unsafe or unsupported proposals
implementation and normal QA result / user feedback if actually received
decision: retain / revise / drop card and reason
```
Review these after work, not as interruption to the founder or current development. This record is not an extra required manual testing project.
