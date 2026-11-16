#!/usr/bin/env python3
"""Real integration tests for private project visual memory (stdlib, offline).

Tests metadata, binary screenshot import, privacy gate, search, evidence,
generated HTML escaping, comparison, duplicate protection and integrity.
Synthetic pixels only; never user or production assets.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import tempfile
import unittest
import zlib
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "visual_workspace.py"
spec = importlib.util.spec_from_file_location("visual_workspace", SCRIPT)
assert spec and spec.loader
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


def png(width=390, height=844, color=(14, 17, 20, 255)):
    def chunk(name, payload):
        body = name + payload
        return struct.pack(">I", len(payload)) + body + struct.pack(">I", zlib.crc32(body))
    rows = b"".join(b"\x00" + bytes(color) * width for _ in range(height))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows, level=7))
            + chunk(b"IEND", b""))


class ProjectVisualWorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.private = self.folder / "private"
        self.first = self.folder / "first.png"
        self.second = self.folder / "second.png"
        self.first.write_bytes(png())
        self.second.write_bytes(png(color=(76, 30, 40, 255)))

    def run_cli(self, *argv, good=True):
        buf = StringIO()
        err = StringIO()
        with redirect_stdout(buf), redirect_stderr(err):
            code = tool.main(["--workspace", str(self.private), *argv])
        if good:
            self.assertEqual(code, 0, err.getvalue())
        else:
            self.assertNotEqual(code, 0, buf.getvalue())
        return buf.getvalue() + err.getvalue()

    def init(self):
        self.run_cli("init-project", "--project", "stage-memory",
                     "--title", "Artist <Night> & memory",
                     "--goal", "Improve editing and gallery without leaking customer data")

    def add(self, screen, file, role):
        return self.run_cli(
            "add-screen", "--project", "stage-memory", "--id", screen, "--file", str(file),
            "--label", "The Night <script>alert(1)</script>" if screen == "before" else "Improved concept",
            "--role", role, "--state", "initial", "--viewport-width", "390",
            "--viewport-height", "844", "--captured-at", "2026-11-16",
            "--url", "https://faneqo.com/night-example",
            "--redacted-confirmed")

    def test_complete_private_workflow(self):
        self.init()
        self.add("before", self.first, "baseline")
        self.add("after", self.second, "candidate")
        self.run_cli("add-finding", "--project", "stage-memory", "--id", "weak-media-actions",
                     "--screen", "before", "--severity", "major",
                     "--statement", "Controls feel bland & ambiguous",
                     "--evidence", "USER_REPORTED", "--outcome", "Clear media upload")
        self.run_cli("add-reference", "--project", "stage-memory", "--id", "awwwards",
                     "--title", "Awwwards creative examples",
                     "--url", "https://www.awwwards.com/", "--kind", "web",
                     "--tags", "cinematic,editorial", "--why", "Research original visual hierarchy")
        self.run_cli("add-direction", "--project", "stage-memory", "--id", "concert-editorial",
                     "--name", "A richer Night", "--thesis", "Concert documentary",
                     "--difference", "Photo dominates, edit in place, less administrative UI",
                     "--references", "awwwards", "--risk", "Decorative visuals may conceal controls")
        self.run_cli("audit", "--project", "stage-memory")
        self.run_cli("board", "--project", "stage-memory", "--before", "before", "--after", "after")
        self.run_cli("report", "--project", "stage-memory")
        project = self.private / "projects" / "stage-memory"
        board = (project / "board.html").read_text()
        self.assertIn("Before / after", board)
        self.assertIn("screens/before.png", board)
        self.assertIn("screens/after.png", board)
        self.assertIn("artist", board.lower())
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", board)
        self.assertNotIn("<script>alert(1)</script>", board)
        self.assertIn("NOT_VISUALLY_INSPECTED_BY_TOOL", board)
        self.assertNotIn("<iframe", board)
        capture = tool.read_json(project / "captures" / "before.json")
        self.assertEqual(capture["pixel_dimensions"], [390, 844])
        self.assertEqual(capture["viewport_css"], [390, 844])
        self.assertEqual(capture["redaction_review"], "MANUAL_REVIEW_CONFIRMED")
        self.assertEqual(hashlib.sha256(self.first.read_bytes()).hexdigest(), capture["sha256"])

    def test_privacy_requires_manual_review_and_no_duplicates(self):
        self.init()
        self.run_cli("add-screen", "--project", "stage-memory", "--id", "before",
                     "--label", "Unredacted", "--file", str(self.first), good=False)
        self.assertFalse((self.private / "projects" / "stage-memory" / "screens").exists())
        self.add("before", self.first, "baseline")
        self.run_cli("add-screen", "--project", "stage-memory", "--id", "other",
                     "--label", "Duplicate bytes", "--file", str(self.first),
                     "--redacted-confirmed", good=False)
        self.run_cli("add-screen", "--project", "stage-memory", "--id", "before",
                     "--label", "Overwritten", "--file", str(self.second),
                     "--redacted-confirmed", good=False)
        self.run_cli("audit", "--project", "stage-memory")

    def test_provenance_claims_and_unsafe_links_are_rejected(self):
        self.init()
        self.add("before", self.first, "baseline")
        self.run_cli("add-finding", "--project", "stage-memory", "--id", "fiction",
                     "--screen", "before", "--statement", "Claimed visual observation",
                     "--evidence", "IMAGE_OBSERVED", good=False)
        self.run_cli("add-finding", "--project", "stage-memory", "--id", "reported",
                     "--screen", "before", "--statement", "Artist reports confusing screen",
                     good=True)
        self.run_cli("add-reference", "--project", "stage-memory", "--id", "bad-ref",
                     "--title", "Unsafe URL", "--url", "javascript:alert(1)",
                     "--kind", "web", "--why", "test", good=False)
        self.run_cli("add-reference", "--project", "stage-memory", "--id", "token",
                     "--title", "Tokenized URL", "--url", "https://example.com/?token=secret",
                     "--kind", "web", "--why", "test", good=False)
        self.run_cli("add-finding", "--project", "stage-memory", "--id", "nonexistent",
                     "--screen", "none", "--statement", "Should fail", good=False)
        (self.folder / "fake.jpg").write_text("<html>not actually an image</html>")
        self.run_cli("add-screen", "--project", "stage-memory", "--id", "fake",
                     "--file", str(self.folder / "fake.jpg"), "--label", "Fake",
                     "--redacted-confirmed", good=False)
        self.run_cli("audit", "--project", "stage-memory")

    def test_audit_catches_tampered_pixels(self):
        self.init()
        self.add("before", self.first, "baseline")
        project = self.private / "projects" / "stage-memory"
        with (project / "screens" / "before.png").open("ab") as f:
            f.write(b"tamper")
        self.run_cli("audit", "--project", "stage-memory", good=False)

    def test_search_is_bounded_and_source_labeled(self):
        text = self.run_cli("find", "--query", "mobile editor gallery")
        self.assertLessEqual(len(text.strip().splitlines()), 6)
        self.assertIn("LINK_ONLY", text)
        text = self.run_cli("find", "--query", "Awwwards")
        self.assertIn("https://www.awwwards.com/", text)
        self.run_cli("find", "--query", "a", good=False)

    def test_project_names_and_github_ignore(self):
        self.run_cli("init-project", "--project", "../unsafe",
                     "--title", "Unsafe", good=False)
        self.assertIn(".cil-private/", (ROOT / ".gitignore").read_text())
        self.assertFalse((ROOT / ".cil-private").exists(),
                         "Static unit tests must never create a public or persistent workspace")


if __name__ == "__main__":
    unittest.main(verbosity=2)
