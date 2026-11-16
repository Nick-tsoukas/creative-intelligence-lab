#!/usr/bin/env python3
"""Real browser smoke/reflow QA for the original Visual Grammar Studio.

Optional dev tool: python -m pip install playwright; python -m playwright install chromium
Then: python scripts/test_visual_grammar_studio.py

Creates non-repository screenshots under /tmp (or $ART_STUDIO_SCREENSHOTS).
This is NOT a usability study, design-quality score or model benchmark.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
STUDIO = ROOT / "experiments/004-visual-grammar-studio/index.html"
TARGET = STUDIO.as_uri()
SHOTS = Path(os.environ.get("ART_STUDIO_SCREENSHOTS", str(Path(tempfile.gettempdir()) / "cil-art-studio-screenshots")))
MODES = ("editorial", "cinema", "signal")
WIDTHS = (320, 390, 768, 1440)


def inspect(page, mode: str, width: int) -> None:
    page.goto(TARGET + f"?mode={mode}", wait_until="load")
    assert page.locator("body").get_attribute("data-mode") == mode, (mode, width, "query mode")
    assert page.locator("#main-headline").is_visible(), (mode, width, "headline hidden")
    assert page.locator(".hero-cta").is_visible(), (mode, width, "CTA hidden")
    assert page.locator(".hero-cta").get_attribute("href") == "#concept", (mode, width, "CTA destination")
    assert page.locator("#concept").count() == 1, (mode, width, "missing real CTA target")
    assert page.locator('button[data-select-mode="' + mode + '"]').get_attribute("aria-pressed") == "true"
    dims = page.evaluate("""() => ({
       viewport: window.innerWidth,
       document: document.documentElement.scrollWidth,
       headline: document.querySelector('#main-headline').getBoundingClientRect().width,
       cta: document.querySelector('.hero-cta').getBoundingClientRect().width
    })""")
    assert dims["document"] <= dims["viewport"] + 1, (mode, width, "horizontal overflow", dims)
    assert dims["headline"] > 0 and dims["cta"] > 0, (mode, width, "missing geometry", dims)

    # Query-mode screenshots make source changes visible to reviewers. A saved
    # PNG does NOT mean anyone inspected its pixels or approved the visual.
    SHOTS.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(SHOTS / f"{mode}-{width}.png"), full_page=True, animations="disabled")
    # Support navigation and switchable presentations without changing copy.
    page.locator(".hero-cta").click()
    assert page.evaluate("location.hash") == "#concept", (mode, width, "real anchor click")
    page.locator('button[data-select-mode="editorial"]').click()
    assert page.locator("body").get_attribute("data-mode") == "editorial"
    page.locator('button[data-select-mode="signal"]').click()
    assert page.locator("body").get_attribute("data-mode") == "signal"
    assert page.locator("#main-headline").inner_text().strip() == "The night stays with you."


def stress(page) -> None:
    page.goto(TARGET + "?mode=signal")
    page.evaluate("""() => {
       document.documentElement.style.fontSize='200%';
       for (const e of document.querySelectorAll('p, h1, h2, h3, a, button, span')) {
           e.style.lineHeight = '1.5';
           e.style.letterSpacing = '0.12em';
           e.style.wordSpacing = '0.16em';
       }
    }""")
    # WCAG text spacing requires no LOSS OF CONTENT; a geometry smoke check
    # can flag overflow but does not certify screen reader/comprehension.
    dims = page.evaluate("() => ({vp:innerWidth,sw:document.documentElement.scrollWidth})")
    assert dims["sw"] <= dims["vp"] + 1, ("text size/spacing horizontal overflow", dims)
    assert page.locator(".hero-cta").is_visible()
    page.screenshot(path=str(SHOTS / "signal-text-stress-320.png"), full_page=True, animations="disabled")


def main() -> int:
    assert STUDIO.exists(), "Missing Studio HTML"
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox"])
        try:
            for width in WIDTHS:
                page = browser.new_page(viewport={"width": width, "height": 920}, device_scale_factor=1)
                for mode in MODES:
                    inspect(page, mode, width)
                page.close()
            page = browser.new_page(viewport={"width": 320, "height": 900})
            stress(page)
            page.close()

            reduced = browser.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
            reduced.goto(TARGET + "?mode=cinema")
            assert reduced.locator(".hero-cta").is_visible()
            assert reduced.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
            reduced.close()

            static = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
            page = static.new_page()
            page.goto(TARGET)
            assert page.locator(".hero-cta").is_visible()
            assert not page.locator(".mode-buttons").is_visible(), "Inert controls visible with JS disabled"
            page.locator(".hero-cta").click()
            assert page.url.endswith("#concept")
            static.close()
        finally:
            browser.close()
    print("PASS: 12 real Chromium mode/viewport renders, CTA, responsive geometry, 200% text stress, reduced motion and no-JS fallback.")
    print("SCREENSHOTS:", SHOTS)
    print("NOT TESTED: human comprehension, visual taste, actual accessibility conformance, real product behavior.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
