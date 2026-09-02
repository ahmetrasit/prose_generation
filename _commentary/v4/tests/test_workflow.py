from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "workflow.py"
SPEC = importlib.util.spec_from_file_location("commentary_v4_workflow", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)


class LayoutTests(unittest.TestCase):
    def test_layout_has_only_three_artifact_roots(self) -> None:
        layout = workflow.layout_for("29:38")
        self.assertEqual(layout.input, workflow.INPUT_ROOT / "s029" / "29_38")
        self.assertEqual(layout.raw, workflow.RAW_ROOT / "s029" / "29_38")
        self.assertEqual(
            layout.editorial, workflow.EDITORIAL_ROOT / "s029" / "29_38"
        )

    def test_prefatory_basmala_is_explicitly_unsupported(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "versioned"):
            workflow.layout_for("100:0")

    def test_batch_selectors_support_lists_ranges_and_deduplication(self) -> None:
        self.assertEqual(
            workflow._expand_ayah_selectors(
                ["100:1-3", "100:3,100:4", "101:1"]
            ),
            ["100:1", "100:2", "100:3", "100:4", "101:1"],
        )

    def test_batch_range_cannot_start_at_prefatory_zero(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "unit zero"):
            workflow._expand_ayah_selectors(["100:0-3"])


class PromptTests(unittest.TestCase):
    def test_scope_templates_are_the_v3_templates(self) -> None:
        expected_hashes = {
            "micro": "75f233e513b724d90ad1f5c0c8fa461bb7dea2a65c3fd2dc71c14b3c7bf65b72",
            "macro": "65d7ff1fcbaa048e497f51297cc15a16728a5583b74d061c5f10214a63c90c0c",
            "global": "5582ea99648ce111338f28ac033f9a53b51a055c8421162dd1f2b8dc44f566d5",
        }
        for lane, expected_hash in expected_hashes.items():
            path = workflow.V3_PROMPTS_ROOT / f"scope-{lane}.md"
            self.assertTrue(path.is_file())
            self.assertEqual(workflow._sha256(path.read_bytes()), expected_hash)
            self.assertIn(
                "commentary-v3-scope-review-v2",
                path.read_text(encoding="utf-8"),
            )

    def test_editorial_source_is_unchanged_v3_prompt(self) -> None:
        source = workflow.V3_PROMPTS_ROOT / "editorial-followup.md"
        self.assertEqual(
            workflow._sha256(source.read_bytes()),
            "5c26ef4d839e15ce8879a4d1811c5fb5e13b30d7c10d15801da3992541c72fea",
        )

    def test_canonical_adapter_preserves_scope_decision_authority(self) -> None:
        prompt = (workflow.PROMPTS_ROOT / "canonical.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("scope analysts own explicit evidentiary decisions", prompt)
        self.assertIn("partition the complete union", prompt)
        self.assertIn("Resolve a referral only when", prompt)
        self.assertIn("complete union of member candidate", prompt)

    def test_canonical_render_rejects_unbound_markers(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "marker mismatch"):
            workflow._render("@@ONE@@ @@TWO@@", {"@@ONE@@": "one"}, label="test")


class ReviewIdentityTests(unittest.TestCase):
    def test_review_check_is_identity_only_not_semantic_repair(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.raw.mkdir(parents=True)
            packet_hash = "a" * 64
            request_hash = "b" * 64
            manifest = {
                "lanes": {
                    "micro": {
                        "packet": {"sha256": packet_hash},
                        "lane_packet_sha256": packet_hash,
                        "request_sha256": request_hash,
                    }
                }
            }
            response = {
                "identity": {
                    "ayah_ref": "1:1",
                    "lane": "micro",
                    "lane_packet_sha256": packet_hash,
                    "authoring_request_sha256": request_hash,
                },
                "ayah_ref": "1:1",
                "lane": "micro",
                "coverage_complete": False,
            }
            layout.scope_review("micro").write_text(
                json.dumps(response), encoding="utf-8"
            )
            self.assertEqual(
                workflow._load_review(layout, manifest, "micro"), response
            )

    def test_stale_review_identity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.raw.mkdir(parents=True)
            manifest = {
                "lanes": {
                    "micro": {
                        "packet": {"sha256": "a" * 64},
                        "lane_packet_sha256": "a" * 64,
                        "request_sha256": "b" * 64,
                    }
                }
            }
            response = {
                "identity": {
                    "ayah_ref": "1:2",
                    "lane": "micro",
                    "lane_packet_sha256": "a" * 64,
                    "authoring_request_sha256": "b" * 64,
                },
                "ayah_ref": "1:2",
                "lane": "micro",
            }
            layout.scope_review("micro").write_text(
                json.dumps(response), encoding="utf-8"
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "stale or mixed"):
                workflow._load_review(layout, manifest, "micro")


class StateTests(unittest.TestCase):
    def test_scope_handoff_has_no_session_state(self) -> None:
        layout = workflow.layout_for("1:1")
        manifest = {"lanes": {"micro": {"request_sha256": "a" * 64}}}
        handoff = workflow._scope_handoff(layout, manifest, "micro")
        self.assertNotIn("session_receipt_required", handoff)
        self.assertNotIn("session_id", handoff)

    def test_output_presence_is_mechanical(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = {"prose": root / "prose.md", "evidence": root / "evidence.md"}
            paths["prose"].write_text("prose", encoding="utf-8")
            present, missing = workflow._nonempty_outputs(paths)
            self.assertEqual(present, ["prose"])
            self.assertEqual(missing, ["evidence"])

    def test_atomic_generated_write_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "artifact.txt"
            workflow._write_generated(path, b"same")
            workflow._write_generated(path, b"same")
            with self.assertRaisesRegex(workflow.WorkflowError, "changed"):
                workflow._write_generated(path, b"different")
            workflow._write_generated(path, b"different", replace_changed=True)
            self.assertEqual(path.read_bytes(), b"different")

    def test_changed_canonical_inputs_cannot_adopt_existing_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.raw.mkdir(parents=True)
            layout.first_pass("prose").write_text("old prose", encoding="utf-8")
            expected = {
                "request_sha256": "a" * 64,
                "prompt": {
                    "path": "_commentary/v4/input/s001/1_1/canonical.prompt.md",
                    "bytes": 6,
                    "sha256": "b" * 64,
                },
            }
            with patch.object(
                workflow,
                "_build_canonical_prompt",
                return_value=("prompt", expected),
            ):
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "Canonical inputs changed"
                ):
                    workflow._ensure_canonical(
                        layout, {"canonical": None}, reviews={}
                    )

    def test_missing_canonical_prompt_is_regenerated_before_outputs(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                payload = b"prompt"
                expected = {
                    "request_sha256": "a" * 64,
                    "prompt": {
                        "path": workflow._repo_path(layout.canonical_prompt),
                        "bytes": len(payload),
                        "sha256": workflow._sha256(payload),
                    },
                }
                manifest = {"canonical": expected}
                with patch.object(
                    workflow,
                    "_build_canonical_prompt",
                    return_value=(payload.decode(), expected),
                ):
                    workflow._ensure_canonical(layout, manifest, reviews={})
                self.assertEqual(layout.canonical_prompt.read_bytes(), payload)

    def test_canonical_verification_mode_does_not_generate_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            payload = b"prompt"
            expected = {
                "request_sha256": "a" * 64,
                "prompt": {
                    "path": "_commentary/v4/input/s001/1_1/canonical.prompt.md",
                    "bytes": len(payload),
                    "sha256": workflow._sha256(payload),
                },
            }
            manifest = {"canonical": None}
            with patch.object(
                workflow,
                "_build_canonical_prompt",
                return_value=(payload.decode(), expected),
            ):
                with self.assertRaisesRegex(workflow.WorkflowError, "run advance"):
                    workflow._ensure_canonical(
                        layout, manifest, reviews={}, write=False
                    )
            self.assertFalse(layout.canonical_prompt.exists())
            self.assertEqual(manifest, {"canonical": None})


class BatchTests(unittest.TestCase):
    def test_batch_collects_ready_handoffs_by_ayah_and_stage(self) -> None:
        args = type(
            "Args",
            (),
            {
                "command": "advance",
                "source_bundle": None,
                "docket": None,
            },
        )()
        results = {
            "1:1": {
                "status": "waiting_for_agents",
                "stage": "scope_review",
                "handoffs": [
                    {"role": "micro_scope_reviewer"},
                    {"role": "macro_scope_reviewer"},
                ],
            },
            "1:2": {
                "status": "waiting_for_agent",
                "stage": "canonical_write",
                "handoff": {"role": "canonical_writer"},
            },
        }

        def execute(unit_args: object) -> dict[str, object]:
            return results[getattr(unit_args, "ayah")]

        with patch.object(workflow, "_execute_one", side_effect=execute):
            result, has_errors = workflow._batch_result(args, ["1:1", "1:2"])
        self.assertFalse(has_errors)
        self.assertEqual(result["summary"]["ready_handoffs"], 3)
        self.assertEqual(
            [handoff["ayah_ref"] for handoff in result["parallel_handoffs"]],
            ["1:1", "1:1", "1:2"],
        )
        self.assertEqual(
            [handoff["stage"] for handoff in result["parallel_handoffs"]],
            ["scope_review", "scope_review", "canonical_write"],
        )

    def test_batch_preserves_other_handoffs_when_one_unit_errors(self) -> None:
        args = type(
            "Args",
            (),
            {
                "command": "advance",
                "source_bundle": None,
                "docket": None,
            },
        )()

        def execute(unit_args: object) -> dict[str, object]:
            if getattr(unit_args, "ayah") == "1:1":
                raise workflow.WorkflowError("broken unit")
            return {
                "status": "waiting_for_agent",
                "stage": "canonical_write",
                "handoff": {"role": "canonical_writer"},
            }

        with patch.object(workflow, "_execute_one", side_effect=execute):
            result, has_errors = workflow._batch_result(args, ["1:1", "1:2"])
        self.assertTrue(has_errors)
        self.assertEqual(result["status"], "partial_error")
        self.assertEqual(result["summary"]["errors"], 1)
        self.assertEqual(result["parallel_handoffs"][0]["ayah_ref"], "1:2")


class RecoveryTests(unittest.TestCase):
    def test_advance_stops_instead_of_repairing_invalid_regular_review(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                layout.raw.mkdir(parents=True)
                layout.manifest.write_text("{}", encoding="utf-8")
                manifest = {
                    "lanes": {
                        lane: {"request_sha256": lane * 8}
                        for lane in workflow.LANES
                    }
                }

                def load_review(
                    _layout: object, _manifest: object, lane: str
                ) -> None:
                    if lane == "micro":
                        raise workflow.WorkflowError("invalid JSON")
                    return None

                with (
                    patch.object(
                        workflow, "_load_unit_manifest", return_value=manifest
                    ),
                    patch.object(
                        workflow, "_load_review", side_effect=load_review
                    ),
                ):
                    with self.assertRaisesRegex(
                        workflow.WorkflowError,
                        "does not issue automated repair turns",
                    ):
                        workflow.advance(
                            SimpleNamespace(ayah="1:1", force_input=False)
                        )

    def test_semantically_incomplete_reviews_advance_directly_to_canonical(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                layout.raw.mkdir(parents=True)
                layout.manifest.write_text("{}", encoding="utf-8")
                manifest = {
                    "lanes": {
                        lane: {"request_sha256": lane * 8}
                        for lane in workflow.LANES
                    }
                }

                def load_review(
                    _layout: object, _manifest: object, lane: str
                ) -> dict[str, object]:
                    return {
                        "ayah_ref": "1:1",
                        "lane": lane,
                        "coverage_complete": False,
                    }

                with (
                    patch.object(
                        workflow, "_load_unit_manifest", return_value=manifest
                    ),
                    patch.object(
                        workflow, "_load_review", side_effect=load_review
                    ),
                    patch.object(
                        workflow,
                        "_ensure_canonical",
                        return_value={"request_sha256": "c" * 64},
                    ),
                ):
                    result = workflow.advance(
                        SimpleNamespace(ayah="1:1", force_input=False)
                    )
                self.assertEqual(result["stage"], "canonical_write")
                self.assertEqual(result["handoff"]["role"], "canonical_writer")
                self.assertNotIn("repair", json.dumps(result).lower())

    def test_advance_force_input_always_runs_prepare(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                layout.manifest.write_text("{}", encoding="utf-8")
                manifest = {
                    "lanes": {
                        lane: {"request_sha256": lane * 8}
                        for lane in workflow.LANES
                    }
                }
                with (
                    patch.object(workflow, "prepare") as prepare,
                    patch.object(
                        workflow, "_load_unit_manifest", return_value=manifest
                    ),
                    patch.object(workflow, "_load_review", return_value=None),
                ):
                    workflow.advance(SimpleNamespace(ayah="1:1", force_input=True))
                prepare.assert_called_once()


class PathSafetyTests(unittest.TestCase):
    def test_confined_write_rejects_symlinked_parent(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary) / "root"
            outside = Path(temporary) / "outside"
            root.mkdir()
            outside.mkdir()
            link = root / "unit"
            link.symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(workflow.WorkflowError, "symlink"):
                workflow._atomic_write(
                    link / "escaped.txt",
                    b"must not escape",
                    root=root,
                )
            self.assertFalse((outside / "escaped.txt").exists())

    def test_handoff_rejects_symlinked_agent_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            outside = root / "outside"
            outside.mkdir()
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.raw.mkdir(parents=True)
                layout.scope_review("micro").symlink_to(outside / "capture.json")
                manifest = {
                    "lanes": {"micro": {"request_sha256": "a" * 64}}
                }
                with self.assertRaisesRegex(workflow.WorkflowError, "symlink"):
                    workflow._scope_handoff(layout, manifest, "micro")

    def test_handoff_rejects_directory_at_agent_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.scope_review("micro").mkdir(parents=True)
                manifest = {
                    "lanes": {"micro": {"request_sha256": "a" * 64}}
                }
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "not a regular file"
                ):
                    workflow._scope_handoff(layout, manifest, "micro")

    def test_manifest_record_must_name_exact_unit_path(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            actual = root / "actual.txt"
            expected = root / "expected.txt"
            actual.write_text("payload", encoding="utf-8")
            record = workflow._path_record(actual)
            with self.assertRaisesRegex(workflow.WorkflowError, "fixed unit path"):
                workflow._verify_record(
                    record,
                    label="test record",
                    expected=expected,
                )


class EditorialLineageTests(unittest.TestCase):
    def test_editorial_handoff_embeds_v3_instructions_and_input_hashes(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                layout.raw.mkdir(parents=True)
                layout.editorial.mkdir(parents=True)
                for kind in workflow.KINDS:
                    layout.first_pass(kind).write_text(kind, encoding="utf-8")

                prompt, record = workflow._build_editorial_prompt(
                    layout, {"request_sha256": "a" * 64}
                )
                instructions = (
                    workflow.V3_PROMPTS_ROOT / "editorial-followup.md"
                ).read_text(encoding="utf-8")
                self.assertIn(instructions, prompt)
                for kind in workflow.KINDS:
                    self.assertEqual(
                        record["first_pass"][kind]["sha256"],
                        workflow._sha256(
                            layout.first_pass(kind).read_bytes()
                        ),
                    )

    def test_changed_first_pass_invalidates_existing_editorial_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.input.mkdir(parents=True)
                layout.raw.mkdir(parents=True)
                layout.editorial.mkdir(parents=True)
                for kind in workflow.KINDS:
                    layout.first_pass(kind).write_text(kind, encoding="utf-8")
                manifest = {"editorial_turn": None}
                canonical = {"request_sha256": "a" * 64}
                workflow._ensure_editorial(layout, manifest, canonical)

                layout.editorial_output("prose").write_text(
                    "editorial prose", encoding="utf-8"
                )
                layout.first_pass("prose").write_text(
                    "changed prose", encoding="utf-8"
                )
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "First-pass inputs changed"
                ):
                    workflow._ensure_editorial(layout, manifest, canonical)


class ProjectionTests(unittest.TestCase):
    def test_quran_projection_rejects_concurrent_source_change(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "quran.tsv"
            source.write_text("1:1|first\n", encoding="utf-8")

            def raced_projection(path: Path) -> tuple[dict[str, object], dict[str, object]]:
                path.write_text("1:1|second\n", encoding="utf-8")
                return {}, {"source_sha256": workflow._sha256(path.read_bytes())}

            with patch.object(
                workflow.v3,
                "_quran_text_evidence",
                side_effect=raced_projection,
            ):
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "changed during packet projection"
                ):
                    workflow._quran_text_projection(source)


if __name__ == "__main__":
    unittest.main()
