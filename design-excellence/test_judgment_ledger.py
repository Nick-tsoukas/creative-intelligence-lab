#!/usr/bin/env python3
"""No external test dependencies. Run python -m unittest discover -s design-excellence."""
import argparse
import json
from pathlib import Path
import tempfile
import unittest

import judgment_ledger as ledger


def feedback(**overrides):
    data = dict(
        project="night-recap", id="owner-001", candidate="prototype-b",
        decision="REVISE", axis="SPACE",
        observation="The hero and gallery feel cramped",
        because="The featured photograph has insufficient room to dominate",
        next_move="Reduce repeated cards and widen the hero margins",
        evidence="OWNER_FEEDBACK", source="Owner design review, 2026-11-16",
        context="390px mobile prototype", supersedes=None,
    )
    data.update(overrides)
    return argparse.Namespace(**data)


class JudgmentLedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_record_and_owner_brief(self):
        ledger.record_feedback(self.root, feedback())
        result = ledger.make_brief(self.root, "night-recap", 8)
        self.assertEqual(result["total_active_matching"], 1)
        self.assertEqual(result["records"][0]["axis"], "SPACE")
        self.assertIn("cramped", ledger.render_brief(result))

    def test_reject_accidental_overwrite(self):
        ledger.record_feedback(self.root, feedback())
        with self.assertRaises(ValueError):
            ledger.record_feedback(self.root, feedback(observation="Replacement"))

    def test_owner_brief_excludes_ai_assumptions_by_default(self):
        ledger.record_feedback(self.root, feedback(evidence="RESEARCH_HYPOTHESIS"))
        self.assertEqual(ledger.make_brief(self.root, "night-recap", 8)["records"], [])
        self.assertEqual(len(ledger.make_brief(self.root, "night-recap", 8, True)["records"]), 1)

    def test_supersede_retains_history_without_duplicating_active_taste(self):
        ledger.record_feedback(self.root, feedback())
        ledger.record_feedback(self.root, feedback(
            id="owner-002", supersedes="owner-001",
            decision="APPROVE", observation="New spacing is balanced"))
        records = ledger.read_records(self.root, "night-recap")
        self.assertEqual(len(records), 2)
        selected = ledger.make_brief(self.root, "night-recap", 8)["records"]
        self.assertEqual([r["id"] for r in selected], ["owner-002"])

    def test_invalid_ids_rejected(self):
        with self.assertRaises(ValueError):
            ledger.record_feedback(self.root, feedback(project="../unsafe"))
        with self.assertRaises(ValueError):
            ledger.record_feedback(self.root, feedback(id="../../token"))

    def test_invalid_revision_target_rejected(self):
        with self.assertRaises(ValueError):
            ledger.record_feedback(self.root, feedback(supersedes="missing"))

    def test_corrupt_records_fail_audit(self):
        directory = ledger.record_directory(self.root, "night-recap")
        directory.mkdir(parents=True)
        (directory / "bad.json").write_text('{"oops":true}', encoding="utf-8")
        with self.assertRaises(ValueError):
            ledger.read_records(self.root, "night-recap")

    def test_text_is_bounded(self):
        with self.assertRaises(ValueError):
            ledger.record_feedback(self.root, feedback(because="x"*1001))

    def test_no_data_created_by_read(self):
        self.assertEqual(ledger.read_records(self.root, "absent"), [])
        self.assertFalse((self.root / "absent").exists())


if __name__ == "__main__":
    unittest.main()
