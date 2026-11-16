#!/usr/bin/env python3
"""Actual Chromium layout smoke of generated local board, SYNTHETIC pixels only.

Not a human visual critique, accessibility certification or real project user test.
"""
import importlib.util
import os
import struct
import tempfile
import zlib
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("workspace", ROOT / "scripts/visual_workspace.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


def make_png(color):
    w, h = 390, 844
    def chunk(tag, value):
        body = tag + value
        return struct.pack(">I", len(value)) + body + struct.pack(">I", zlib.crc32(body))
    body = b"".join(b"\0" + color * w for _ in range(h))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(body))
            + chunk(b"IEND", b""))


def cli(workspace, *argv):
    exit_code = tool.main(["--workspace", str(workspace), *argv])
    if exit_code:
        raise RuntimeError(f"CLI failed {argv}")


def main():
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp)
        workspace = path / "private"
        old = path / "old.png"
        new = path / "new.png"
        old.write_bytes(make_png(bytes([45, 53, 62, 255])))
        new.write_bytes(make_png(bytes([112, 72, 44, 255])))
        cli(workspace, "init-project", "--project", "visual-qa",
            "--title", "Visual Studio — an & original design review",
            "--goal", "Beautiful, accessible private evidence board")
        cli(workspace, "add-screen", "--project", "visual-qa",
            "--id", "before", "--file", str(old), "--label", "Before • mobile",
            "--role", "baseline", "--redacted-confirmed")
        cli(workspace, "add-screen", "--project", "visual-qa",
            "--id", "after", "--file", str(new), "--label", "Concept • mobile",
            "--role", "candidate", "--redacted-confirmed")
        cli(workspace, "add-finding", "--project", "visual-qa",
            "--id", "hierarchy", "--screen", "before",
            "--statement", "User reports low hierarchy", "--evidence", "USER_REPORTED")
        cli(workspace, "add-reference", "--project", "visual-qa",
            "--id", "inspiration", "--title", "Awwwards", "--url", "https://www.awwwards.com/",
            "--kind", "web", "--why", "Art direction research lead")
        cli(workspace, "add-direction", "--project", "visual-qa",
            "--id", "editorial", "--name", "Editorial Night",
            "--thesis", "The Night as a beautiful music documentary",
            "--difference", "Photography-led chapters rather than repeated cards")
        cli(workspace, "board", "--project", "visual-qa",
            "--before", "before", "--after", "after")
        uri = (workspace / "projects/visual-qa/board.html").as_uri()
        screenshots = Path(os.environ.get("VISUAL_BOARD_SCREENSHOTS",
                                          str(path / "screenshots")))
        screenshots.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True, args=["--no-sandbox"])
            try:
                for width in (320, 390, 1440):
                    page = browser.new_page(viewport={"width": width, "height": 900})
                    page.goto(uri)
                    assert page.locator("h1").is_visible()
                    assert page.locator("text=Before / after").is_visible()
                    assert page.locator("#screens img").count() == 2
                    natural = page.locator("#screens img").first.evaluate("(el)=>el.naturalWidth")
                    assert natural == 390, ("Private image failed to render", width)
                    body = page.evaluate("() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})")
                    assert body["scrollWidth"] <= body["width"] + 1, ("Horizontal overflow", width, body)
                    assert page.locator("text=Artist private data").count() == 0
                    page.screenshot(path=str(screenshots / f"visual-board-{width}.png"),
                                    full_page=True, animations="disabled")
                    page.close()
                page = browser.new_page(viewport={"width": 390, "height": 844},
                                        reduced_motion="reduce")
                page.goto(uri)
                assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
                assert page.locator("a[href='screens/before.png']").first.is_visible()
                page.close()
            finally:
                browser.close()
        print("PASS: real Chromium local board 320/390/1440, local images, comparison, no x-overflow, reduced motion")
        print("Screenshots (synthetic only):", screenshots)
        print("NOT CLAIMED: aesthetic superiority, real person usability, imported production screenshots")


if __name__ == "__main__":
    main()
