# Dialogs, Alerts and Interruptions — A Comparative Study

**Access:** 2026-11-11, official platform guidance and W3C APG read. **Not** a screen-reader or live browser test.

## Original sources
- W3C WAI-ARIA APG modal dialog: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- W3C native HTML dialog technique: https://www.w3.org/WAI/WCAG22/Techniques/html/H102
- Fluent 2 dialog usage: https://fluent2.microsoft.design/components/web/react/core/dialog/usage
- Apple HIG alerts: https://developer.apple.com/design/human-interface-guidelines/alerts

## Source-grounded findings
**W3C APG:** A modal traps Tab/Shift+Tab within itself, moves focus inside when opened, supports Escape to close, and normally returns focus to the invoker when closed. Initial focus location depends on content and consequences; for hard-to-reverse actions, focus may appropriately start on the least destructive option. APG requires an accessible label; marking a non-modal implementation with aria-modal='true' is harmful.

**W3C H102:** The native HTML dialog element, when used with showModal(), provides built-in modal focus/inertness behavior, though actual labeling and usage still require care.

**Fluent 2:** Modal for necessary focused work, non-modal helper for continuing a workflow, alert dialog for urgent decisions. It advises against nested dialogs and unnecessary actions. Uses a clear title, focused content, simple actionable labels and appropriate dismissal mechanisms. In its guidance, an alert dialog requires choosing one of its available action buttons, while many other dialogs have more flexible dismissal.

**Apple:** Alerts interrupt and should be reserved for critical, actionable information. Undoable common deletion need not always produce an alert; uncommon irreversible destruction generally warrants stronger confirmation. Avoid generic titles; provide a clear Cancel option for destructive actions. Native platform-specific conventions differ.

## Pattern selection decision
| User need | Prefer | Why |
|---|---|---|
| Brief confirmation after reversible action | Toast/status | Avoid interruption |
| Help while continuing work | Popover/non-modal helper | Background still usable |
| Short task that temporarily requires focus | Modal dialog | One focused interaction |
| Irreversible destructive choice | Alert/confirmation tailored to consequence | Clear intentional decision |
| Long complex form/workflow | Dedicated page or step flow | Space, recovery and context |

This table is **our synthesis** of cited guidance, not a universal rule.

## Design anatomy
Accessible title, concise content, action hierarchy, safe dismiss action, focus entry and return, background inertness for modal, responsive sizing/scroll behavior.

## Failure modes
- Modal UI visually dims the background but allows keyboard focus behind it.
- Focus disappears after closing because trigger is gone.
- Destructive default action bound to Enter unintentionally.
- Long form nested in small modal with hidden controls.
- Dismiss on backdrop click loses unsaved data.
- ARIA roles present but behavior absent.

## Hypothesis
A well-designed dialog should make the consequence and escape route clearer than the interruption itself. Its quality is measurable through task success and recovery, not shadow radius.

## Next test
Use the same warning task in Fluent and native HTML dialog demos; log keyboard tab order, Escape, focus return, zoom, screen reader label, and no-JavaScript alternatives. No claim those tests were performed here.