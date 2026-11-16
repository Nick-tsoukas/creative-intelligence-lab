/* Static-first: all core content, anchors and semantic information work without JS. */
(() => {
  "use strict";
  const allowed = new Set(["editorial", "cinema", "signal"]);
  const buttons = Array.from(document.querySelectorAll("[data-select-mode]"));
  const body = document.body;
  if (!body || buttons.length !== 3) return;

  const status = document.createElement("span");
  status.className = "sr-only";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  const group = document.querySelector(".mode-buttons");
  if (group) group.appendChild(status);

  function setMode(next, announce = true) {
    if (!allowed.has(next)) return;
    body.dataset.mode = next;
    buttons.forEach((button) => {
      const active = button.dataset.selectMode === next;
      button.setAttribute("aria-pressed", String(active));
    });
    if (announce) status.textContent = next + " art direction selected. The product information and links are unchanged.";
  }
  body.dataset.enhanced = "true";

  const fromQuery = new URLSearchParams(window.location.search).get("mode");
  if (allowed.has(fromQuery)) setMode(fromQuery, false);
  else setMode("editorial", false);

  buttons.forEach((button) => {
    button.addEventListener("click", () => setMode(button.dataset.selectMode));
  });
})();
