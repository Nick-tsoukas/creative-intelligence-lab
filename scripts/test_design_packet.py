#!/usr/bin/env python3
"""Offline integration tests of the source-grounded project brief generator."""
from __future__ import annotations
import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("design_packet", ROOT / "scripts/prepare_design_packet.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class DesignPacketTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.project = self.base / "projects" / "example"
        self.project.mkdir(parents=True)
        (self.project / "project.json").write_text(json.dumps({
            "schema":1, "title":"Fictional Artist Page", "slug":"example",
            "goal":"Create an original art-directed media recap and excellent editor",
            "visibility":"PRIVATE_LOCAL_ONLY"}), encoding="utf-8")

    def add_screen(self, id, observation="NOT_VISUALLY_INSPECTED_BY_TOOL"):
        folder = self.project / "captures"
        folder.mkdir(exist_ok=True)
        (folder / (id + ".json")).write_text(json.dumps({
            "id":id,"label":"Synthetic screenshot","role":"baseline",
            "state":"artist-view","image":"screens/" + id + ".png",
            "pixel_dimensions":[390,844],"viewport_css":[390,844],
            "original_capture_date":None,"visual_status":observation}), encoding="utf-8")

    def test_source_cases_are_relevant_and_bounded(self):
        self.add_screen("baseline")
        packet = tool.generate(self.project, "rich text editor", 3)
        self.assertIn("EI-007", packet)
        self.assertIn("PREVIEW_OBSERVED", packet)
        self.assertIn("MUST OPEN IMAGE PIXELS", packet)
        self.assertIn("NOT RUN", packet)
        self.assertIn("THREE materially different", packet)
        self.assertLess(len(packet), 16000)
        self.assertLessEqual(packet.count("Actual external screenshot:"), 3)

    def test_unknown_screen_and_context_budget(self):
        self.add_screen("baseline")
        with self.assertRaises(ValueError):
            tool.generate(self.project, "gallery", 3, "missing")
        with self.assertRaises(ValueError):
            tool.generate(self.project, "gallery", 50)
        with self.assertRaises(ValueError):
            tool.generate(self.project, "x" * 1001)

    def test_missing_screenshot_does_not_imply_evidence(self):
        text = tool.generate(self.project, "an extremely rare unmatchable topology")
        self.assertIn("No imported screenshots", text)
        self.assertIn("NOT an approved design", text)
        self.assertIn("without Atlas: NOT RUN", text)

    def test_findings_remain_screen_scoped_and_evidence_labeled(self):
        self.add_screen("baseline")
        self.add_screen("second")
        folder = self.project / "findings"
        folder.mkdir(exist_ok=True)
        for name,screen in [("reported","baseline"),("offtopic","second")]:
            (folder / (name + ".json")).write_text(json.dumps({
                "id":name,"screen_id":screen,
                "statement": "Media selection seems confusing" if name=="reported" else "Different screen concern",
                "severity":"major","evidence":"USER_REPORTED",
                "desired_outcome":"Clear safe media flow","test_status":"NOT_TESTED"}))
        text = tool.generate(self.project,"media upload", 2, "baseline")
        self.assertIn("Media selection seems confusing",text)
        self.assertNotIn("Different screen concern",text)

    def test_packet_stays_private_and_never_overwrites(self):
        self.add_screen("baseline")
        out,err = StringIO(),StringIO()
        with redirect_stdout(out),redirect_stderr(err):
            status = tool.main(["--workspace", str(self.base),
                                "--project","example","--task","music gallery",
                                "--save","first-brief"])
        self.assertEqual(status,0,err.getvalue())
        saved=self.project / "research-packets/first-brief.md"
        self.assertTrue(saved.exists())
        self.assertIn("PRIVATE",out.getvalue())
        with redirect_stdout(StringIO()),redirect_stderr(err):
            status=tool.main(["--workspace",str(self.base),"--project","example",
                              "--task","music gallery","--save","first-brief"])
        self.assertEqual(status,1,"No overwriting the saved founder/agent research packet")
        with redirect_stdout(StringIO()),redirect_stderr(err):
            status=tool.main(["--workspace",str(self.base),"--project","example",
                              "--task","music gallery","--save","../unsafe"])
        self.assertEqual(status,1)

    def test_no_image_api_or_web_dependency(self):
        source=(ROOT / "scripts/prepare_design_packet.py").read_text()
        self.assertNotIn("requests.",source)
        self.assertNotIn("httpx.",source)
        self.assertNotIn("openai.",source)
        self.assertNotIn("anthropic.",source)
        self.assertIn("NOT an approved design",source)


if __name__=="__main__":
    unittest.main(verbosity=2)
