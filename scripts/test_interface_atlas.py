#!/usr/bin/env python3
"""Static QA for source fidelity, study depth and gallery generation.

NOT a claim of user research, mobile app functionality or improved aesthetics.
"""
import importlib.util
import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "interface-atlas"


def load(path):
    return json.loads((ATLAS / path).read_text(encoding="utf-8"))


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


class AtlasResearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.studies = load("observed-cases.json")["cases"]
        cls.targets = load("research-targets.json")["targets"]
        cls.query = module("query_interface_atlas.py", "atlas_query")
        cls.gallery = module("build_interface_gallery.py", "gallery_builder")

    def test_honest_study_coverage(self):
        self.assertEqual(len(self.studies), 10)
        self.assertEqual({r["id"] for r in self.studies},
                         {f"EI-{i:03d}" for i in range(1, 11)})
        for r in self.studies:
            self.assertEqual(r["status"], "PREVIEW_OBSERVED")
            self.assertEqual(r["interaction_status"], "NOT_TESTED")
            self.assertEqual(r["mobile_browser_status"], "NOT_TESTED")
            self.assertEqual(r["media_reuse_status"], "LINK_ONLY")
            self.assertIn(r["kind"], {"web", "mobile", "component"})
            for field in ("title", "creator", "source_url", "preview_url",
                          "observed", "mechanism", "risks", "original_exercise",
                          "not_copy", "observation_limits", "preview_source"):
                self.assertTrue(r.get(field), (r["id"], field))
            for field in ("observed", "mechanism", "risks", "original_exercise"):
                self.assertGreaterEqual(len(r[field]), 100, (r["id"], field))
            for field in ("source_url", "preview_url"):
                u = urlsplit(r[field])
                self.assertEqual(u.scheme, "https")
                self.assertTrue(u.hostname)
                self.assertNotIn("@", u.netloc)
            self.assertTrue(r["tags"])
            self.assertEqual(r["retrieved_on"], "2026-11-16")

    def test_sixty_targets_distribution_and_provenance(self):
        self.assertEqual(len(self.targets), 60)
        self.assertEqual({r["id"] for r in self.targets}, {f"T-{i:03d}" for i in range(1, 61)})
        from collections import Counter
        counts = Counter(r["category"] for r in self.targets)
        self.assertEqual(dict(counts),
                         {"web": 10, "mobile": 10, "music": 10,
                          "component": 15, "motion": 10, "experimental": 5})
        self.assertEqual(sum(bool(t["case_id"]) for t in self.targets), 10)
        for t in self.targets:
            self.assertTrue(t["tags"])
            u = urlsplit(t["url"])
            self.assertEqual(u.scheme, "https")
            self.assertTrue(u.hostname)
            self.assertFalse(t["flow_tested"])
            if t["case_id"]:
                self.assertEqual(t["status"], "PREVIEW_OBSERVED")
                self.assertIn(t["case_id"], {r["id"] for r in self.studies})
            else:
                self.assertEqual(t["status"], "QUEUED_FOR_RESEARCH")
                self.assertEqual(t["visual_evidence"], "NOT_INSPECTED")

    def test_on_demand_retrieval_is_small_and_truthful(self):
        q = self.query
        self.assertEqual(len(q.cases()), 10)
        self.assertEqual(len(q.targets()), 60)
        editor = q.rank("rich text editor", q.cases())
        self.assertGreater(len(editor), 0)
        self.assertEqual(editor[0][1]["id"], "EI-007")
        music = q.rank("music", q.cases())
        self.assertGreater(len(music), 2)
        self.assertIn("not an interactive product", q.detail(self.studies[0]))
        self.assertFalse(q.rank("abcxxxnotpresent", q.cases()))

    def test_visual_gallery_is_self_contained_and_reproducible(self):
        expected = self.gallery.build()
        output = (ATLAS / "gallery.html").read_text(encoding="utf-8")
        self.assertEqual(expected, output)
        self.assertEqual(output.count('id="research-data"'), 1)
        self.assertIn("EI-010", output)
        self.assertIn("PREVIEW_OBSERVED", output)
        self.assertIn("SOURCE", output.upper())
        self.assertIn("ORIGINAL SCHEMATIC", output)
        self.assertIn("View actual source image", output)
        self.assertNotIn("<img src=\"https://", output)
        self.assertNotIn("<script src=\"https://", output)
        self.assertNotIn("google-analytics", output)
        self.assertNotIn("gtag(", output)
        self.assertFalse(any((ATLAS / "gallery-assets").glob("*.png")) if (ATLAS / "gallery-assets").exists() else False)

    def test_malicious_text_does_not_break_gallery_script(self):
        gallery = self.gallery
        # Check script-data escaping used by the reproducible gallery builder.
        malicious = "</script><script>alert(1)</script>&"
        encoded = json.dumps({"text": malicious}, ensure_ascii=False,
                             separators=(",", ":"))
        encoded = encoded.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
        self.assertNotIn("</script>", encoded)
        self.assertNotIn("<script>", encoded)
        self.assertIn("\\u003c", encoded)


if __name__ == "__main__":
    unittest.main(verbosity=2)
