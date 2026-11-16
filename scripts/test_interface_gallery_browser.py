#!/usr/bin/env python3
"""Real Chromium checks of our ORIGINAL static Atlas gallery. No external images.

Tests visual board structure, responsive layout, search, filters and source links.
Does not prove aesthetics, live app flows, accessibility conformance or outcomes.
"""
from __future__ import annotations
import os
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "interface-atlas/gallery.html").resolve().as_uri()
SHOTS = Path(os.environ.get("ATLAS_GALLERY_SHOTS",
                            str(Path(tempfile.gettempdir()) / "cil-atlas-screenshots")))


def run():
    SHOTS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox"])
        try:
            for width in (320, 390, 768, 1440):
                page = browser.new_page(viewport={"width": width, "height": 930},
                                        device_scale_factor=1)
                page.goto(PAGE, wait_until="load")
                page.wait_for_selector(".case")
                assert page.locator(".case").count() == 10, ("missing observed cases", width)
                assert page.locator("h1").is_visible()
                assert page.locator('a[href^="https://"][target="_blank"]').count() == 20
                assert page.locator(".art-label").count() == 10
                assert "10 of 10" in page.locator("#result-count").inner_text()
                width_state = page.evaluate(
                    "() => ({vw:window.innerWidth, sw:document.documentElement.scrollWidth})")
                assert width_state["sw"] <= width_state["vw"] + 1, (
                    "gallery horizontal overflow", width, width_state)
                page.screenshot(path=str(SHOTS / f"atlas-{width}.png"),
                                full_page=True, animations="disabled")
                # On all sizes search stays functional and updates result count.
                page.locator("#query").fill("editor")
                assert page.locator(".case").count() >= 1
                assert page.locator(".case").count() < 10
                page.locator("#query").fill("no-match-super-random")
                assert page.locator(".case").count() == 0
                assert page.locator("#empty").is_visible()
                page.locator("#query").fill("")
                page.locator('button[data-filter="component"]').click()
                assert page.locator(".case").count() == 2, ("component count", width)
                assert page.locator('button[data-filter="component"]').get_attribute(
                    "aria-pressed") == "true"
                page.locator('button[data-filter="all"]').click()
                detail = page.locator(".case").first.locator("details")
                detail.locator("summary").click()
                assert detail.evaluate("(el)=>el.open")
                assert detail.inner_text().find("What was visible") >= 0
                page.close()

            reduced = browser.new_page(viewport={"width": 390, "height": 844},
                                       reduced_motion="reduce")
            reduced.goto(PAGE)
            assert reduced.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
            assert reduced.locator(".case").count() == 10
            reduced.close()

            static = browser.new_context(java_script_enabled=False,
                                         viewport={"width": 390, "height": 844})
            page = static.new_page()
            page.goto(PAGE)
            # A dedicated accessible noscript link index will be required if
            # the research gallery itself becomes a core no-JS application.
            assert page.locator("h1").is_visible()
            page.close()
            static.close()
        finally:
            browser.close()

    print("PASS: original Atlas gallery 320/390/768/1440; 10 cases, source links, filters, search, details, reduced motion.")
    print("Original-schematic screenshots:", SHOTS)
    print("NOT TESTED: external app flows, source screenshot pixel rights, human creativity judgment, production integration.")


if __name__ == "__main__":
    run()
