#!/usr/bin/env python3
"""Integration tests using synthetic files and disposable local roots."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import build_screen_handoff as handoff
import judgment_ledger as ledger
import visual_audit as visual


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.repo = self.root / "synthetic-app"
        self.repo.mkdir()
        (self.repo / "pages").mkdir()
        (self.repo / "pages" / "example.vue").write_text(
            "<script setup>const model = await useFetch('/api/demo')</script>"
            "<template><button @click='save'>Save</button></template>",
            encoding="utf-8")
        self.workspace = self.root / "private-workspace"
        self.project = self.workspace / "projects" / "example"
        (self.project / "screens").mkdir(parents=True)
        (self.project / "captures").mkdir()
        (self.project / "project.json").write_text('{"schema":1}')
        self.image = self.project / "screens" / "mobile.png"
        self.image.write_bytes(b"SYNTHETIC_IMAGE_BYTES_ONLY")
        sha = hashlib.sha256(self.image.read_bytes()).hexdigest()
        (self.project / "captures" / "mobile.json").write_text(json.dumps({
            "schema": 1, "id": "mobile", "image": "screens/mobile.png",
            "sha256": sha, "redaction_review": "MANUAL_REVIEW_CONFIRMED",
            "viewport_css": [390, 844], "state": "artist",
        }))

    def tearDown(self):
        self.tmp.cleanup()

    def test_full_handoff_preserves_separate_provenance(self):
        visual.start(self.workspace, "example", "audit-01", "mobile")
        args = argparse.Namespace(id="issue-01", category="HIERARCHY", severity="MAJOR",
                                  observation="The hero visually obscures the primary action",
                                  because="The first task becomes difficult to identify",
                                  recommendation="Give the action a legible region",
                                  evidence="IMAGE_OBSERVED", pixels_inspected=True)
        visual.observe(self.workspace, "example", "audit-01", args)
        recorded = argparse.Namespace(
            project="example", id="owner-01", candidate="concept-a", decision="REJECT",
            axis="COMPOSITION", observation="Visual density is excessive",
            because="The page needs breathing space", next_move="Simplify",
            evidence="OWNER_FEEDBACK", source="Synthetic test only", context="Test viewport",
            supersedes=None,
        )
        ledger.record_feedback(self.workspace / "creative-judgment", recorded)
        output = handoff.build(self.workspace, self.repo, "pages/example.vue", "example", "audit-01")
        self.assertIn("Visual density is excessive", output)
        self.assertIn("hero visually obscures", output)
        self.assertIn("STATIC_HINT_NOT_VERIFIED", output)
        self.assertIn("/api/demo", output)
        self.assertIn("No production authorization", output)

    def test_no_private_artifacts_created_by_default(self):
        output = handoff.build(self.workspace, self.repo, "pages/example.vue", "example")
        self.assertIn("No reviewed screenshot audit attached", output)
        self.assertFalse((self.workspace / "design-hand-offs").exists())

    def test_atlas_packet_is_read_only_and_restricted(self):
        folder = self.project / "research-packets"
        folder.mkdir()
        source = folder / "case-01.md"
        source.write_text("Preview-observed research, not a working app test.")
        out = handoff.build(self.workspace, self.repo, "pages/example.vue", "example",
                            atlas_packet="case-01")
        self.assertIn("Preview-observed research", out)
        with self.assertRaises(ValueError):
            handoff.build(self.workspace, self.repo, "pages/example.vue", "example",
                          atlas_packet="../bad")
        self.assertEqual(source.read_text(), "Preview-observed research, not a working app test.")

    def test_unknown_source_is_not_guessed(self):
        with self.assertRaises(ValueError):
            handoff.build(self.workspace, self.repo, "pages/not-here.vue", "example")


if __name__ == "__main__":
    unittest.main()
