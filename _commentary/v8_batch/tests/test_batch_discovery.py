from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from _commentary.v8_batch import batch_discovery
from _commentary.v8_batch import workflow


class BatchDiscoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=batch_discovery.V8_ROOT)
        self.root = Path(self.temporary.name)
        self.analysis_id = "batch-test"
        self.patches = [
            mock.patch.object(workflow, "INPUT_ROOT", self.root / "input"),
            mock.patch.object(workflow, "RAW_ROOT", self.root / "raw"),
            mock.patch.object(workflow, "EDITORIAL_ROOT", self.root / "editorial"),
            mock.patch.object(workflow, "MIDDLE_ROOT", self.root / "middle"),
        ]
        for patcher in self.patches:
            patcher.start()
        self.layout = workflow.layout_for("12:1", self.analysis_id)
        self.layout.input.mkdir(parents=True)
        for lane in batch_discovery.LANES:
            self.layout.scope_prompt(lane).write_text(
                f"exact prompt for {lane}\n", encoding="utf-8"
            )

    def tearDown(self) -> None:
        for patcher in reversed(self.patches):
            patcher.stop()
        self.temporary.cleanup()

    def _build(self) -> tuple[dict, Path, dict]:
        result = batch_discovery.build(
            argparse.Namespace(
                analysis_id=self.analysis_id,
                ayah=["12:1"],
                name="test",
                batch_dir=self.root / "batches",
                max_file_bytes=batch_discovery.MAX_BATCH_FILE_BYTES,
            )
        )
        manifest_path = batch_discovery._resolve_repo_path(result["manifest"])
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        return result, manifest_path, manifest

    def test_copied_behavioral_prompts_match_v5_except_runtime_paths(self) -> None:
        v5_prompts = batch_discovery.V8_ROOT.parent / "v5" / "prompts"
        for name in (
            "canonical.md",
            "composition.md",
            "discovery-policy.md",
            "discovery.md",
            "editorial.md",
            "invitation.md",
            "middle-layer-audit-followup.md",
            "middle-layer.md",
        ):
            original = (v5_prompts / name).read_text(encoding="utf-8")
            copied = (batch_discovery.V8_ROOT / "prompts" / name).read_text(
                encoding="utf-8"
            )
            self.assertEqual(
                copied.replace("_commentary/v8_batch", "_commentary/v5"), original
            )

    def test_build_preserves_exact_prompt_and_forces_luna_max_tool_call(self) -> None:
        result, _manifest_path, manifest = self._build()
        self.assertEqual(result["requests"], 3)
        self.assertEqual(manifest["model"], "gpt-5.6-luna")
        part = batch_discovery._resolve_repo_path(manifest["parts"][0]["path"])
        rows = [json.loads(line) for line in part.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(rows[0]["body"]["input"], "exact prompt for micro\n")
        self.assertEqual(rows[0]["body"]["reasoning"], {"effort": "max"})
        self.assertEqual(
            rows[0]["body"]["tool_choice"],
            {"type": "function", "name": "write_discovery_json"},
        )
        self.assertFalse(rows[0]["body"]["store"])

    def test_collect_writes_only_validated_discovery_and_prepares_handoffs(self) -> None:
        _result, manifest_path, manifest = self._build()
        submission_path = self.root / "batches" / "test.submission.json"
        submission_path.write_text(
            json.dumps(
                {
                    "schema_version": batch_discovery.SUBMISSION_SCHEMA_VERSION,
                    "manifest": batch_discovery._repo_path(manifest_path),
                    "jobs": [
                        {
                            "part": manifest["parts"][0]["path"],
                            "input_file_id": "file_test",
                            "batch_id": "batch_test",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        rows = []
        for request in manifest["requests"]:
            document = {
                "schema_version": batch_discovery.DISCOVERY_SCHEMA_VERSION,
                "ayah_ref": request["ayah_ref"],
                "lane": request["lane"],
                "coverage_complete": True,
                "candidate_decisions": [],
                "findings": [],
                "friction_notes": [],
            }
            arguments = {
                "path": request["discovery_output_path"],
                "document": document,
            }
            rows.append(
                {
                    "custom_id": request["custom_id"],
                    "response": {
                        "status_code": 200,
                        "body": {
                            "output": [
                                {
                                    "type": "function_call",
                                    "name": "write_discovery_json",
                                    "arguments": json.dumps(arguments),
                                }
                            ],
                            "usage": {
                                "input_tokens": 300_000,
                                "input_tokens_details": {"cached_tokens": 0},
                                "output_tokens": 10_000,
                            },
                        },
                    },
                    "error": None,
                }
            )
        output = "\n".join(json.dumps(row) for row in rows).encode("utf-8")

        class FakeClient:
            def json_request(self, method: str, path: str, body=None):
                return {"id": "batch_test", "status": "completed", "output_file_id": "file_out"}

            def bytes_request(self, path: str) -> bytes:
                return output

        with mock.patch.object(batch_discovery, "OpenAIClient", FakeClient):
            result = batch_discovery.collect(
                argparse.Namespace(manifest=manifest_path, submission=submission_path)
            )

        self.assertEqual(result["discoveries"], 3)
        self.assertEqual(len(result["composition_handoffs"]), 3)
        self.assertFalse(result["automatic_retry"])
        self.assertAlmostEqual(result["discovery_cost"]["standard_usd"], 0.414)
        self.assertAlmostEqual(result["discovery_cost"]["batch_usd"], 0.207)
        for lane in batch_discovery.LANES:
            self.assertTrue(self.layout.scope_discovery(lane).is_file())
            composition = self.layout.input / f"{lane}.composition.prompt.md"
            handoff = self.layout.input / f"{lane}.composition-from-batch.prompt.md"
            self.assertTrue(composition.is_file())
            self.assertTrue(handoff.is_file())
            handoff_text = handoff.read_text(encoding="utf-8")
            self.assertIn(batch_discovery._repo_path(self.layout.scope_prompt(lane)), handoff_text)
            self.assertIn(batch_discovery._repo_path(self.layout.scope_discovery(lane)), handoff_text)

    def test_document_rejects_wrong_identity(self) -> None:
        document = {
            "schema_version": batch_discovery.DISCOVERY_SCHEMA_VERSION,
            "ayah_ref": "12:2",
            "lane": "micro",
            "coverage_complete": True,
            "candidate_decisions": [],
            "findings": [],
            "friction_notes": [],
        }
        with self.assertRaises(batch_discovery.BatchError):
            batch_discovery._validate_document(document, ayah_ref="12:1", lane="micro")


if __name__ == "__main__":
    unittest.main()
