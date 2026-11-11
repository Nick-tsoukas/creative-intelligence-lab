# Creative Direction Protocol — ChatGPT ↔ Claude Code ↔ Owner

**Status:** Working operating contract, 2026-11-11. Human oversight required. No external autonomous agent is running.

## Roles
**ChatGPT (research/art director):** chooses relevant research, writes narrative design direction, supplies source links and evidence grades, insists on distinct conceptual alternatives, critiques screenshots and live behavior where access permits, and signs off on research completeness (not production deployment).

**Claude Code (implementation/design engineering):** inspects real repository and app constraints, proposes implementation plans, builds authorized sandbox prototypes, reports files changed and test evidence, and identifies engineering/accessibility tradeoffs. Claude does not unilaterally choose a visual direction or deploy.

**Owner:** selects strategy, resolves taste conflicts, authorizes production work/deployment, can veto any direction.

## Exchange artifacts (versioned Markdown)
1. **CREATIVE_BRIEF.md:** audience, task, intended emotion, content, functional constraints, references + explicit *not to imitate*, success/anti-goals.
2. **CONCEPTS.md:** 3 meaningfully different visual theses (one restrained, one expressive, one surprising but justified), each with conceptual mechanism, layout plan, visual principles, motion and UX risks.
3. **DESIGN_DECISION.md:** selected approach, tradeoffs, who approved, date.
4. **IMPLEMENTATION_PLAN.md:** current code reality, reusable components, CSS/motion/performance strategy, implementation boundaries, manual and automated checks.
5. **DESIGN_REVIEW.md:** observations versus hypotheses, screenshots with source/provenance, UX defects, artistic critique, priorities, discrepancies between implemented and intended work.
6. **HANDOFF.md:** final tested facts, changed files, passing and missing tests, live links and next instructions.

Examples live in [templates](../templates/).

## Closed-loop working cycle
**Research → Brief → 3 Concepts → Critique → Owner direction → Prototype → Evidence → Independent critique → Revision → Owner approval.**
ChatGPT and Claude should *disagree constructively*. A design decision must mention alternatives and why rejected. No imitation of proprietary style.

## Minimum acceptance checks
- **Creative:** subject-specific concept, explainable hierarchy, original visual relationships, consistent craft, documented reference mechanisms.
- **UX:** primary task findable; navigation and controls understandable; appropriate feedback, empty/error and success states.
- **Accessibility:** semantic headings/labels, keyboard, focus indicator, text contrast and reflow, reduced motion; consult WCAG 2.2 criteria. Don't claim compliance without testing.
- **Performance:** image budgeting, animation jank and Core Web Vitals consideration; never invent benchmark scores.
- **Engineering:** Nuxt/Vue SSR/hydration correctness when relevant; code maintainable, state semantics sound, no unrequested dependency additions.
- **Traceability:** evidence for decisions and screenshots clearly labelled original/reference/captured.

## Conflict resolution
If research favors unusual expression but usability tests reveal confusion, treat usability defects as real evidence. Revisit the expression rather than ignore either goal. If Claude reports constraints, ChatGPT revises directions while preserving the core concept. Owner makes final tradeoff decision.

## Separation of contexts
The Creative Intelligence Lab research repo is independent of Faneqo. Use this contract on invented exercises first. Production repos should not be changed merely because a future chat reads these instructions.

## Resumption in new chats
Read `START_HERE.md`, `docs/STATUS.md`, `docs/FINISH_LINE.md`, this contract, latest decision log, handbook and skill status. State present stage, blockers and next smallest deliverable. Don't treat a planned skill or prototype as already installed or tested.

## 2026-11-11 skill complementarity amendment
Anthropic's `frontend-design` skill is the specialist for actually constructing attractive usable frontend interfaces; do not duplicate it in the Creative Intelligence skill. Our `creative-design-director` skill supplies research-grounded art direction before build, and evidence-based independent critique afterwards. During implementation, Claude may use frontend-design with that direction packet. Read `research/009-FRONTEND-SKILL-COMPARISON.md` and `handbook/DIRECTION-TO-BUILD-CONTRACT.md`. The final isolated Faneqo homepage test must assess whether the extra research layer improves results, not assume success.
