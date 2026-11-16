#!/usr/bin/env python3
"""Synthetic, private-only tests for visual audits and Nuxt screen inspection."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import screen_intelligence as si
import visual_audit as va


class ScreenIntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "pages").mkdir()
        (self.root / "pages" / "night.vue").write_text("""<script setup lang="ts">
const route = useRoute()
const record = await useFetch('/api/show-recaps')
const unknown = await $fetch('/api/' + route.params.id)
const artist = useState('selected-band', () => null)
import useComposer from '~/composables/useComposer'
</script>
<template><button @click="saveDraft" :disabled="busy">Save</button></template>
""", encoding="utf-8")
        (self.root / ".env").write_text("SECRET=don't-leak", encoding="utf-8")
        (self.root / "pages" / "secret.vue").write_text("const token = 'supersecret'", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_scan_reports_only_static_hints(self):
        result = si.inventory(self.root, "pages/night.vue", [])
        self.assertTrue(result["no_code_executed"])
        self.assertEqual(result["files_scanned"], 1)
        hints = result["static_hints"][0]
        self.assertIn("useRoute", hints["composables"])
        self.assertIn("click", hints["ui_events"])
        self.assertIn("useFetch", [a["function"] for a in hints["api_calls"]])
        self.assertIn("$fetch", [a["function"] for a in hints["api_calls"]])
        self.assertIn("/api/show-recaps", [a["static_path"] for a in hints["api_calls"]])
        self.assertIn(None, [a["static_path"] for a in hints["api_calls"]])
        self.assertNotIn("don't-leak", si.render_markdown(result))
        self.assertEqual(result["confirmed_or_observed_facts"], [])

    def test_only_explicit_sources_scanned(self):
        with self.assertRaises(ValueError):
            si.inventory(self.root, ".env", [])
        with self.assertRaises(ValueError):
            si.inventory(self.root, "../outside.vue", [])
        with self.assertRaises(ValueError):
            si.inventory(self.root, "pages/night.vue", ["pages/missing.vue"])
        with self.assertRaises(ValueError):
            si.inventory(self.root, "pages/night.vue", ["pages/secret.vue"])
        with self.assertRaises(ValueError):
            si.inventory(self.root, "pages/night.vue", ["pages/night.vue"] * 13)

    def test_manifest_preserves_authority_and_unknowns(self):
        contract = {
            "schema": 1, "route": "pages/night.vue",
            "facts": [
                {"id": "recap", "kind": "API_DATA", "name": "recap",
                 "source": "confirmed Strapi /api/show-recaps response in dev",
                 "used_for": "Night heading", "shape": "title:string, date:string",
                 "permissions": "Artist owner only (test this)", "states": "loading, error, data",
                 "evidence": "CODE_OBSERVED", "verified_on": "2026-11-16"}
            ], "unknowns": ["Production authorization unknown"],
            "constraints": ["Never imply draft is published"]
        }
        path = self.root / "manifest.json"
        path.write_text(json.dumps(contract), encoding="utf-8")
        result = si.inventory(self.root, "pages/night.vue", [], str(path))
        self.assertEqual(result["confirmed_or_observed_facts"][0]["name"], "recap")
        self.assertIn("Production authorization unknown", result["unknowns"])
        self.assertIn("Never imply", si.render_markdown(result))

    def test_explicit_strapi_schema_has_field_shapes_not_permission_claims(self):
        backend = self.root / "backend"
        schema = backend / "src" / "api" / "night" / "content-types" / "night" / "schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_text(json.dumps({
            "info": {"displayName": "Show Recap"},
            "attributes": {
                "title": {"type": "string", "required": True},
                "photos": {"type": "media", "multiple": True},
                "band": {"type": "relation", "relation": "manyToOne", "target": "api::band.band"}
            }
        }), encoding="utf-8")
        data = si.inventory(self.root, "pages/night.vue", [], backend_root=backend,
                            schema_paths=["src/api/night/content-types/night/schema.json"])
        self.assertEqual(data["backend_schema_hints"][0]["display_name"], "Show Recap")
        self.assertEqual([x["name"] for x in data["backend_schema_hints"][0]["fields"]],
                         ["band", "photos", "title"])
        self.assertEqual(data["backend_schema_hints"][0]["fields"][1]["type"], "media")
        self.assertIn("NOT evidence of API responses", si.render_markdown(data).replace(
            "No verified API response/permission from schema alone.",
            "NOT evidence of API responses"))
        with self.assertRaises(ValueError):
            si.inventory(self.root, "pages/night.vue", [],
                         schema_paths=["src/api/night/content-types/night/schema.json"])

    def test_reject_mismatched_manifest(self):
        path = self.root / "wrong.json"
        path.write_text(json.dumps({"schema": 1, "route": "other.vue", "facts": [], "unknowns": [], "constraints": []}))
        with self.assertRaises(ValueError):
            si.inventory(self.root, "pages/night.vue", [], str(path))


class VisualAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp.name)
        self.project = self.workspace / "projects" / "example"
        (self.project / "captures").mkdir(parents=True)
        (self.project / "screens").mkdir()
        (self.project / "project.json").write_text('{"schema":1}')
        # Synthetic bytes only. Audit trusts hash-verified captures made by the existing
        # visual_workspace importer, which checks actual PNG/JPEG integrity.
        self.image = self.project / "screens" / "screen1.png"
        self.image.write_bytes(b"synthetic-capture-for-test")
        self.sha = hashlib.sha256(self.image.read_bytes()).hexdigest()
        capture = {
            "schema": 1, "id": "screen1", "image": "screens/screen1.png",
            "sha256": self.sha, "redaction_review": "MANUAL_REVIEW_CONFIRMED",
            "viewport_css": [390, 844], "state": "prototype"
        }
        (self.project / "captures" / "screen1.json").write_text(json.dumps(capture))

    def tearDown(self):
        self.temp.cleanup()

    def args(self, **changes):
        values = dict(id="issue1", category="SPACING", severity="MAJOR",
                      observation="Heading and hero are visually crowded",
                      because="The photograph loses its intended focal priority",
                      recommendation="Add breathing room between title and image",
                      evidence="IMAGE_OBSERVED", pixels_inspected=True)
        values.update(changes)
        return argparse.Namespace(**values)

    def test_start_observe_report_and_integrity(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        va.observe(self.workspace, "example", "audit1", self.args())
        text = va.report(self.workspace, "example", "audit1")
        self.assertIn("Heading and hero", text)
        self.assertIn("IMAGE_OBSERVED", text)
        self.assertIn("TYPOGRAPHY", text)  # Listed as not reviewed, not a passing check
        self.assertIn(str(self.image), va.prompt(self.workspace, "example", "audit1"))
        self.assertEqual(len(va.observations(self.workspace, "example", "audit1")), 1)

    def test_unseen_image_cannot_be_claimed_observed(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        with self.assertRaises(ValueError):
            va.observe(self.workspace, "example", "audit1", self.args(pixels_inspected=False))
        self.assertEqual(len(va.observations(self.workspace, "example", "audit1")), 0)

    def test_immutable_findings(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        va.observe(self.workspace, "example", "audit1", self.args())
        with self.assertRaises(FileExistsError):
            va.observe(self.workspace, "example", "audit1", self.args())

    def test_tamper_detected_before_observation(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        self.image.write_bytes(b"changed-file")
        with self.assertRaises(ValueError):
            va.observations(self.workspace, "example", "audit1")

    def test_missing_redaction_check(self):
        path = self.project / "captures" / "screen1.json"
        capture = json.loads(path.read_text())
        capture["redaction_review"] = "UNKNOWN"
        path.write_text(json.dumps(capture))
        with self.assertRaises(ValueError):
            va.start(self.workspace, "example", "audit1", "screen1")

    def test_comparison_requires_two_audits_and_does_not_choose_winner(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        va.start(self.workspace, "example", "audit2", "screen1")
        comparison = va.compare(self.workspace, "example", "audit1", "audit2")
        self.assertIn("Viewport comparable: YES", comparison)
        self.assertIn("Winner: NOT SELECTED", comparison)
        self.assertIn("Open BOTH actual images", comparison)
        with self.assertRaises(ValueError):
            va.compare(self.workspace, "example", "audit1", "audit1")

    def test_empty_report_has_honest_limit(self):
        va.start(self.workspace, "example", "audit1", "screen1")
        self.assertIn("not** been audited", va.report(self.workspace, "example", "audit1"))


if __name__ == "__main__":
    unittest.main()
