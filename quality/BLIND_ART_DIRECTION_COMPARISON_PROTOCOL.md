# Quality Gate — Does Reference-Driven Art Direction Actually Improve the Design?

**2026-11-16.** This is a **proposed** evaluation protocol, not a claimed experiment. The end goal is to produce truly exceptional, creative, usable designs more reliably than the same model without this Atlas. Research volume, a passing CI suite or a high model self-rating is *not* evidence of that outcome.

## Fair controlled comparison (future permitted pilot)
1. Choose a real project brief that includes the exact current-state screenshots, honest product data, route requirements, approved brand locks, user tasks, privacy/permissions, deadline and implementation constraints.
2. Assign two independent sessions of the **same AI model**, same prompt, identical token/tool/time budget, identical assets and code snapshot. **Condition A (baseline)** uses normal design capability, without the Atlas or Visual Memory. **Condition B (research)** may selectively retrieve 2–4 directly relevant, actually inspected Atlas sources and the same private project history. Neither gets the other's work.
3. Each produces **three truly distinct directions**, one chosen concept and one responsive interactive prototype from the same locked content. Separate vision and UX specialists can critique independently. Both use same tools/CI.
4. Randomly label the submitted prototypes **X/Y** so reviewers are blinded to which was Atlas-supported. Avoid telling critics which source examples were used before ratings.
5. Reviewers independently judge artistic premise, meaning, originality, typographic/photo craft, cultural relevance, hierarchy and restraint. Record precise observations and disagreement rather than one magic "Mona Lisa score".
6. Test representative real tasks with unfamiliar users and actual devices or browsers, recording task success, time-to-completion and failures. Keep user study **separate** from art-critic votes.
7. Collect implementation evidence: focus/keyboard, color/zoom/reflow, 320/390/768/1440 screenshots, low-end performance or measured LCP/INP/CLS where feasible, state recovery, permission truth, privacy and code maintenance.
8. Compare both complete results and costs (prompt length, API requests, preparation/time, source failures). If research case selection causes noise, complexity or copying, revise/retire the relevant records.

## Evaluation scorecard (no invented ratings)
| Axis | Evidence required | Condition A | Condition B | Independently verified? |
|---|---|---|---|---|
| First-view product comprehension | Uncoached participant answer | NOT RUN | NOT RUN | NO |
| Artistic meaning and originality | Blinded independent critic notes | NOT RUN | NOT RUN | NO |
| Composition and editorial craft | Paired real screenshots at exact sizes | NOT RUN | NOT RUN | NO |
| Mobile/task flow and recoverability | Device/browser interactions & logs | NOT RUN | NOT RUN | NO |
| Accessible controls and states | Real keyboard, focus, reflow, contrast | NOT RUN | NOT RUN | NO |
| Cultural/asset integrity | Owner confirmation, consent/source licenses | NOT RUN | NOT RUN | NO |
| Runtime & maintainability | Measurements and diff/code review | NOT RUN | NOT RUN | NO |
| Time/cost overhead | Tool use, time and scope counts | NOT RUN | NOT RUN | NO |

## Minimum bar before claiming a benefit
- Real evidence of more distinctive and on-brand **original** composition, not simply an aesthetic preference from the researcher who selected the references.
- The human task is at least as usable and reliable as the baseline, with no newly introduced security/privacy/accessibility regressions.
- The improvement is repeatable on more than one product/design context, including a case that is not music/Faneqo.
- If there is no meaningful difference, say so, then improve retrieval and the art-direction method—do not inflate case counts.

## Two immediate pilot challenges
- **Faneqo Night Recap:** authentic concert documentary and media editing, with current screenshots and a demanding artist workflow.
- **Unrelated content tool:** a simple journal/editor/gallery app using fictional test data to challenge genre bias.

Current state: **preparing an experiment**; the Lab has not yet run blind prototype comparisons or measured user outcomes. GitHub browser tests validate our own gallery UI, not an art superiority hypothesis.
