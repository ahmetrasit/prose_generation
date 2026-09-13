from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tests.test_layer3_channel_workflow import layer3_common


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "_surah_commentary" / "v2"
spec = importlib.util.spec_from_file_location("surah_editorial_workflow", WORKFLOW / "scripts" / "workflow.py")
workflow = importlib.util.module_from_spec(spec)
with patch.dict(sys.modules, {"common": layer3_common}):
    spec.loader.exec_module(workflow)


class SurahEditorialWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="surah-editorial-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.editorial_root = self.root / "editorial"
        self.texts = [
            "The first image shows a path sustained by received assistance.",
            "The second image makes each step depend on continuing support.",
        ]
        self.paths = []
        for ayah, text in enumerate(self.texts, 1):
            path = self.editorial_root / "chosen" / "s042" / f"42_{ayah}" / f"42_{ayah}.prose.editorial.tr.md"
            path.parent.mkdir(parents=True)
            path.write_text(text, encoding="utf-8")
            self.paths.append(path)
        self.packet = self.build()
        self.outline = {
            "schemaVersion": workflow.OUTLINE_SCHEMA,
            "packetHash": self.packet["packetHash"],
            "primaryArc": {"text": "Assistance accompanies the path.",
                           "evidence": [{"ayahRef": "42:1", "anchor": self.texts[0]}]},
            "movements": [{"id": "supported-path", "title": "The supported path",
                           "contribution": "Walking depends on assistance.",
                           "members": [{"ayahRef": f"42:{i}", "image": "Path and support",
                                        "contribution": text, "qualification": "An image of support.",
                                        "anchors": [text]} for i, text in enumerate(self.texts, 1)]}],
            "ayahCoverage": [{"ayahRef": f"42:{i}", "movementIds": ["supported-path"],
                              "note": "Contributes a supported walking image."} for i in (1, 2)],
            "friction": [],
        }
        self.composition = {
            "schemaVersion": workflow.COMPOSITION_SCHEMA,
            "packetHash": self.packet["packetHash"], "outlineHash": workflow.content_hash(self.outline),
            "phase": "editorial",
            "prelude": "A path begins to appear through the help that sustains it.",
            "postlude": "The path and assistance form one developing reader movement.\n\n" + "\n\n".join(self.texts),
            "primaryLanding": "The path and assistance form one developing reader movement.",
            "landings": [{"movementId": "supported-path",
                          "preludeAnchor": "A path begins to appear through the help that sustains it.",
                          "postludeAnchor": "The path and assistance form one developing reader movement.",
                          "members": [{"ayahRef": f"42:{i}", "anchor": text} for i, text in enumerate(self.texts, 1)]}],
            "friction": [],
        }

    def build(self):
        return workflow.build_packet(editorial_root=self.editorial_root, analysis_id="chosen",
                                     surah=42, ayah_count=2, language="tr", completed_by="fixture")

    def test_editorials_are_sufficient_and_frozen(self):
        self.assertFalse((self.root / "raw").exists())
        self.assertFalse((self.root / "quran-data").exists())
        workflow.validate_packet(self.packet)
        self.paths[0].write_text("A revised editorial has a genuinely different complete opening.", encoding="utf-8")
        workflow.validate_packet(self.packet)
        self.assertNotEqual(self.build()["packetHash"], self.packet["packetHash"])
        self.assertEqual(self.packet["editorials"][0]["text"], self.texts[0])

    def test_completion_missing_and_extra_ayahs_fail(self):
        with self.assertRaises(SystemExit):
            workflow.build_packet(editorial_root=self.editorial_root, analysis_id="chosen",
                                  surah=42, ayah_count=2, language="tr", completed_by="")
        self.paths[1].unlink()
        with self.assertRaisesRegex(SystemExit, "editorial missing"):
            self.build()
        self.paths[1].write_text(self.texts[1], encoding="utf-8")
        (self.paths[1].parent.parent / "42_3").mkdir()
        with self.assertRaisesRegex(SystemExit, "declared complete surah"):
            self.build()

    def test_tampered_or_mixed_packet_fails(self):
        broken = copy.deepcopy(self.packet)
        broken["editorials"][0]["text"] += " Silent edit."
        with self.assertRaisesRegex(SystemExit, "changed editorial"):
            workflow.validate_packet(broken)
        broken = copy.deepcopy(self.packet)
        broken["editorials"][1]["ayahRef"] = "43:2"
        with self.assertRaisesRegex(SystemExit, "every numbered ayah"):
            workflow.validate_packet(broken)

    def test_outline_requires_exact_sources_and_complete_coverage(self):
        workflow.validate_outline(self.outline, self.packet)
        broken = copy.deepcopy(self.outline)
        broken["movements"][0]["members"][0]["anchors"] = ["An upstream image absent from this final editorial prose."]
        with self.assertRaisesRegex(SystemExit, "exactly once"):
            workflow.validate_outline(broken, self.packet)
        broken = copy.deepcopy(self.outline)
        broken["ayahCoverage"].pop()
        with self.assertRaisesRegex(SystemExit, "every ayah"):
            workflow.validate_outline(broken, self.packet)
        broken = copy.deepcopy(self.outline)
        broken["movements"][0]["members"].pop()
        with self.assertRaisesRegex(SystemExit, "two distinct"):
            workflow.validate_outline(broken, self.packet)

    def test_all_stage_prompts_contain_only_editorial_derived_content(self):
        draft = copy.deepcopy(self.composition)
        draft["phase"] = "draft"
        for stage in workflow.STAGES:
            prompt = workflow.assemble(stage, self.packet, outline=self.outline, draft=draft,
                                       output=self.root / f"{stage}.json")
            for text in self.texts:
                self.assertIn(text, prompt)
            self.assertNotIn("sourcePath", prompt)
            self.assertNotIn("activationCards", prompt)
            self.assertNotIn("layer2Handoff", prompt)
            self.assertNotIn("support_registry", prompt)
        with self.assertRaises(SystemExit):
            workflow.assemble("edit", self.packet, outline=self.outline, output=self.root / "edit.json")

    def test_composition_requires_coverage_unique_anchors_and_lineage(self):
        workflow.validate_composition(self.composition, self.packet, self.outline)
        for field, value in (("outlineHash", "0" * 64), ("landings", []),
                             ("postlude", self.composition["postlude"] + "\n" + self.texts[0])):
            broken = copy.deepcopy(self.composition)
            broken[field] = value
            with self.subTest(field=field), self.assertRaises(SystemExit):
                workflow.validate_composition(broken, self.packet, self.outline)

    def test_no_secondary_movement_is_allowed_without_invention(self):
        outline = copy.deepcopy(self.outline)
        outline["movements"] = []
        for row in outline["ayahCoverage"]:
            row["movementIds"] = []
        outline["friction"] = ["Only the primary progression is supported by these editorials."]
        workflow.validate_outline(outline, self.packet)

    def test_publication_requires_editorial_and_approval(self):
        with self.assertRaises(SystemExit):
            workflow.publication_files(self.packet, self.outline, self.composition, "")
        draft = copy.deepcopy(self.composition)
        draft["phase"] = "draft"
        with self.assertRaisesRegex(SystemExit, "expected editorial"):
            workflow.publication_files(self.packet, self.outline, draft, "reviewer")

    def test_publication_revision_replaces_stable_preserves_history(self):
        with patch.object(workflow, "WORKFLOW_ROOT", self.root / "workflow"):
            original = workflow.publish(self.packet, self.outline, self.composition,
                                        approved_by="reviewer", stable=True)
            original_files = {p.name: p.read_text(encoding="utf-8") for p in original.iterdir()}
            accepted = workflow.run_dir(self.packet) / "accepted" / original.name
            self.assertEqual(json.loads((accepted / "composition.json").read_text(encoding="utf-8")), self.composition)
            stable = workflow.WORKFLOW_ROOT / "outputs" / "s042"
            unrelated = stable / "old-reader.md"
            unrelated.write_text("Preserve me.", encoding="utf-8")
            revised = copy.deepcopy(self.composition)
            revised["postlude"] += "\n\nA final transition returns to the same supported reading."
            second = workflow.publish(self.packet, self.outline, revised, approved_by="reviewer", stable=True)
            self.assertNotEqual(original, second)
            self.assertEqual(original_files, {p.name: p.read_text(encoding="utf-8") for p in original.iterdir()})
            history = workflow.WORKFLOW_ROOT / "publication-history" / "s042" / "tr" / workflow.content_hash(original_files)
            self.assertEqual(original_files, {p.name: p.read_text(encoding="utf-8") for p in history.iterdir()})
            self.assertEqual(unrelated.read_text(encoding="utf-8"), "Preserve me.")
            evidence = json.loads((stable / "42.surah-reading.evidence.tr.json").read_text(encoding="utf-8"))
            postlude = (stable / "42.surah-reading.postlude.tr.md").read_text(encoding="utf-8")
            self.assertEqual(evidence["surfaceHashes"]["postlude"], workflow.sha256_text(postlude))
            self.assertEqual(second, workflow.publish(self.packet, self.outline, revised, approved_by="reviewer", stable=True))

    def test_cli_validates_packet_and_rejects_wrong_phase(self):
        import subprocess

        paths = {}
        for name, value in (("packet", self.packet), ("outline", self.outline), ("composition", self.composition)):
            paths[name] = self.root / f"{name}.json"
            paths[name].write_text(json.dumps(value), encoding="utf-8")
        command = [sys.executable, "-B", str(WORKFLOW / "scripts" / "workflow.py"), "validate",
                   "--packet", str(paths["packet"]), "--outline", str(paths["outline"]),
                   "--composition", str(paths["composition"]), "--phase"]
        passed = subprocess.run(command + ["editorial"], text=True, capture_output=True)
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertEqual(passed.stdout.strip(), "ok")
        failed = subprocess.run(command + ["draft"], text=True, capture_output=True)
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("expected draft", failed.stderr)

    def test_immutable_set_preflight_and_stable_rollback(self):
        stable, history = self.root / "stable", self.root / "history"
        stable.mkdir()
        (stable / "first.md").write_text("Original first.", encoding="utf-8")
        (stable / "last.json").write_text("Original last.", encoding="utf-8")
        with self.assertRaises(SystemExit):
            workflow.write_immutable_set(stable, {"new.md": "New.", "last.json": "Different."})
        self.assertFalse((stable / "new.md").exists())
        original_replace = workflow.os.replace
        calls = 0

        def fail_second(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated failure")
            return original_replace(source, target)

        with patch.object(workflow.os, "replace", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "simulated"):
                workflow.replace_stable(stable, {"first.md": "Changed first.", "last.json": "Changed last."}, history)
        self.assertEqual((stable / "first.md").read_text(encoding="utf-8"), "Original first.")
        self.assertEqual((stable / "last.json").read_text(encoding="utf-8"), "Original last.")
        self.assertEqual({p.name for p in stable.iterdir()}, {"first.md", "last.json"})


if __name__ == "__main__":
    unittest.main()
