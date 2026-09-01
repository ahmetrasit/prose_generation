from __future__ import annotations

import argparse
import copy
import io
import json
import math
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


V3_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(V3_ROOT))

import render_authoring  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402


class RenderAuthoringTests(unittest.TestCase):
    @staticmethod
    def _micro_facet_packet() -> dict[str, object]:
        return {
            "schema_version": "commentary-v3-lane-evidence-packet-v2",
            "candidate_inventory": [],
            "support_registry": [],
            "connection_registry": [],
            "focus_surface_evidence": {"word_rows": []},
            "branch_registry": [
                {
                    "branch_ref": "root_test/B001",
                    "registry": "focus",
                    "review_facets": [
                        {
                            "facet_id": "F001",
                            "source_fields": ["distinctive_facets[F001]"],
                            "statements": {"statement": "channels movement"},
                        }
                    ],
                }
            ],
        }

    @staticmethod
    def _micro_facet_review() -> dict[str, object]:
        return {
            "schema_version": "commentary-v3-scope-review-v2",
            "coverage_complete": True,
            "candidate_decisions": [],
            "accepted_findings": [
                {
                    "finding_ref": "micro:finding",
                    "candidate_ids": [],
                    "proposal_keys": ["micro:proposal"],
                    "support_ids": [],
                    "branch_refs": ["root_test/B001"],
                    "connection_refs": [],
                    "contact_refs": [],
                    "branch_contributions": [
                        {
                            "branch_ref": "root_test/B001",
                            "facet_id": "F001",
                            "distinctive_facet": "a boundary channels movement",
                            "surface_carrier": "X",
                            "independent_anchor": "the explicit destination",
                            "contribution": "motion becomes constrained passage",
                            "boundary": "not every motion is constrained",
                        }
                    ],
                }
            ],
            "new_findings": [
                {
                    "proposal_key": "micro:proposal",
                    "accepted_finding_ref": "micro:finding",
                    "contact_refs": [],
                }
            ],
            "contact_opportunities": [],
            "scope_referrals": [],
            "surface_coverage": [],
            "branch_screen": [
                {
                    "branch_ref": "root_test/B001",
                    "result": "nominated",
                    "reason": "The syntax independently activates F001.",
                    "contact_refs": [],
                    "tested_facets": [
                        {"facet_id": "F001", "result": "contact"}
                    ],
                }
            ],
        }

    @staticmethod
    def _macro_connection_packet() -> dict[str, object]:
        return {
            "schema_version": "commentary-v3-lane-evidence-packet-v2",
            "candidate_inventory": [],
            "support_registry": [],
            "branch_registry": [],
            "connection_registry": [
                {
                    "connection_ref": "conn_test",
                    "connection_evidence_ref": "conn_ev_authored",
                    "target_ref": "2:2",
                    "reciprocal_evidence": [
                        {"connection_evidence_ref": "conn_ev_reciprocal"}
                    ],
                }
            ],
        }

    @staticmethod
    def _macro_connection_review() -> dict[str, object]:
        return {
            "schema_version": "commentary-v3-scope-review-v2",
            "coverage_complete": True,
            "candidate_decisions": [],
            "accepted_findings": [],
            "new_findings": [],
            "contact_opportunities": [],
            "scope_referrals": [],
            "atlas_facets_tested": [],
            "connection_coverage": [
                {
                    "connection_ref": "conn_test",
                    "target_ref": "2:2",
                    "result": "rejected",
                    "finding_refs": [],
                    "reason": "Neither direction yields a grounded contact.",
                    "evidence_row_results": [
                        {
                            "connection_evidence_ref": "conn_ev_authored",
                            "result": "rejected",
                            "finding_refs": [],
                            "reason": "The authored direction lacks a return path.",
                        },
                        {
                            "connection_evidence_ref": "conn_ev_reciprocal",
                            "result": "rejected",
                            "finding_refs": [],
                            "reason": "The reverse note does not change the reading.",
                        },
                    ],
                }
            ],
        }

    def test_load_object_rejects_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            path = Path(temp_dir) / "duplicate.json"
            path.write_text('{"status":"first","status":"second"}', encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "duplicate JSON object key"):
                render_authoring._load_object(path)

    def test_canonical_json_rejects_nonfinite_numbers(self) -> None:
        with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
            render_authoring._canonical_json({"value": math.nan})

    def test_cli_reports_workflow_system_exit_as_json_error(self) -> None:
        stderr = io.StringIO()
        stdout = io.StringIO()
        with (
            patch.object(
                sys,
                "argv",
                ["render_authoring.py", "scopes", "--ayah", "not-an-ayah"],
            ),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            code = render_authoring.main()
        self.assertEqual(code, 2)
        self.assertEqual(stdout.getvalue(), "")
        error = json.loads(stderr.getvalue())
        self.assertEqual(error["status"], "error")
        self.assertEqual(error["error_type"], "SystemExit")
        self.assertIn("Invalid ayah reference", error["message"])

    def test_mixed_guard_lineage_is_documented_as_stop_state(self) -> None:
        text = (V3_ROOT / "ORCHESTRATION.md").read_text(encoding="utf-8")
        self.assertIn("canonical_workspace_guard_status: mixed_guard_lineage", text)
        self.assertIn("stop and report it", text)

    def test_branch_review_facets_normalize_unnumbered_source_image(self) -> None:
        facets = render_authoring._branch_review_facets(
            {"image_ar": "صورة", "image_en": "an image"}
        )
        self.assertEqual(
            facets,
            [
                {
                    "facet_id": "SOURCE_IMAGE",
                    "source_fields": ["image_ar", "image_en"],
                    "role": "source_semantic_image",
                    "statements": {
                        "image_ar": "صورة",
                        "image_en": "an image",
                    },
                }
            ],
        )

    def test_scope_review_binds_contribution_to_activated_facet(self) -> None:
        packet = self._micro_facet_packet()
        review = self._micro_facet_review()
        render_authoring._validate_scope_review("micro", packet, review)

        unknown = copy.deepcopy(review)
        unknown["accepted_findings"][0]["branch_contributions"][0][
            "facet_id"
        ] = "F999"
        with self.assertRaisesRegex(SystemExit, "cites unknown facet"):
            render_authoring._validate_scope_review("micro", packet, unknown)

        unactivated = copy.deepcopy(review)
        unactivated["branch_screen"][0]["tested_facets"][0][
            "result"
        ] = "no_independent_trigger"
        with self.assertRaisesRegex(SystemExit, "claims unactivated facet"):
            render_authoring._validate_scope_review("micro", packet, unactivated)

        reassigned = copy.deepcopy(review)
        reassigned["accepted_findings"][0]["branch_contributions"][0][
            "facet_id"
        ] = "F002"
        with self.assertRaisesRegex(SystemExit, "loses or rewrites"):
            render_authoring._validate_scope_validation_repair_preserves_semantics(
                "micro", review, reassigned, set()
            )

    def test_scope_review_preserves_every_connection_evidence_row(self) -> None:
        packet = self._macro_connection_packet()
        review = self._macro_connection_review()
        render_authoring._validate_scope_review("macro", packet, review)

        incomplete = copy.deepcopy(review)
        incomplete["connection_coverage"][0]["evidence_row_results"].pop()
        with self.assertRaisesRegex(SystemExit, "evidence-row coverage is not exact"):
            render_authoring._validate_scope_review("macro", packet, incomplete)

    def test_invitation_prompt_handles_optional_primary_relations(self) -> None:
        template = (V3_ROOT / "prompts" / "invitation-summary.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("fresh invitation writer", template)
        self.assertIn("[supports-primary]", template)
        self.assertIn("[shifts-primary]", template)
        self.assertIn("Do not force or invent a surprise relation", template)
        self.assertIn("Add no claim or\ninterpretation", template)

    def test_invitation_handoff_contains_only_editorial_prose_and_index(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir)
            layout = render_authoring.AuthoringLayout(
                ayah_ref="29:38",
                folder="s029",
                stem="29_38",
                inputs=root / "inputs",
                outputs=root / "outputs",
            )
            editorial_dir = layout.outputs / "editorial" / ("a" * 64)
            editorial_dir.mkdir(parents=True)
            source_texts = {
                "prose": "PROSE_ONLY_SOURCE",
                "index": "INDEX_ONLY_SOURCE",
                "evidence": "EVIDENCE_MUST_NOT_APPEAR",
                "friction": "FRICTION_MUST_NOT_APPEAR",
            }
            editorial_outputs: dict[str, Path] = {}
            receipt_outputs: dict[str, dict[str, object]] = {}
            for key, source_text in source_texts.items():
                path = editorial_dir / f"29_38.{key}.editorial.tr.md"
                path.write_text(source_text, encoding="utf-8")
                editorial_outputs[key] = path
                payload = path.read_bytes()
                receipt_outputs[key] = {
                    "path": render_authoring._manifest_path(path),
                    "bytes": len(payload),
                    "sha256": render_authoring._sha256_bytes(payload),
                }
            receipt_path = editorial_dir / "turn-receipt.json"
            receipt_path.write_text("{}\n", encoding="utf-8")
            editorial_result = {
                "request_sha256": "a" * 64,
                "outputs": {
                    key: str(path) for key, path in editorial_outputs.items()
                },
                "receipt": str(receipt_path),
            }
            editorial_receipt = {"outputs": receipt_outputs}

            with patch.object(
                render_authoring, "_authoring_layout", return_value=layout
            ):
                result = render_authoring._render_invitation(
                    argparse.Namespace(ayah="29:38"),
                    editorial_result,
                    editorial_receipt,
                )

            prompt = Path(result["prompt"]).read_text(encoding="utf-8")
            self.assertIn("PROSE_ONLY_SOURCE", prompt)
            self.assertIn("INDEX_ONLY_SOURCE", prompt)
            self.assertNotIn("EVIDENCE_MUST_NOT_APPEAR", prompt)
            self.assertNotIn("FRICTION_MUST_NOT_APPEAR", prompt)
            manifest = render_authoring._load_object(Path(result["manifest"]))
            self.assertEqual(manifest["stage"], "invitation-summary")
            self.assertEqual(
                manifest["expected_response"],
                render_authoring._manifest_path(Path(result["expected_response"])),
            )

    def test_invitation_summary_rejects_internal_apparatus(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir)
            outputs = root / "outputs"
            outputs.mkdir()
            layout = render_authoring.AuthoringLayout(
                ayah_ref="29:38",
                folder="s029",
                stem="29_38",
                inputs=root / "inputs",
                outputs=outputs,
            )
            response = outputs / "invitation.md"
            response.write_text(
                "Ayetin yalın sözü erişilebilir kalırken yeni bir ilişki görünür.",
                encoding="utf-8",
            )
            render_authoring._validate_invitation_summary(layout, response)

            apparatus_examples = (
                "Bu, locked:micro:finding üzerinden okunur.",
                "Kaynak support_id sup_1234567890abcdef1234 olarak kayıtlıdır.",
                "HFT ve QAC bu sonucu doğrular.",
                "scope-micro satırı /word_analysis/words/7 konumundadır.",
                "hft_ref, qac_morpheme ve scope_micro iç etiketleridir.",
                "invitation_summary canonical_editorial_followup sonrasıdır.",
                "invitation-summary canonical-editorial-followup sonrasıdır.",
                "canonical-writer ve invitation-writer aşamaları kullanıldı.",
                "İç koordinat 29:38:12:2 olarak verilir.",
            )
            for example in apparatus_examples:
                with self.subTest(example=example):
                    response.write_text(example, encoding="utf-8")
                    with self.assertRaisesRegex(
                        SystemExit, "internal editorial apparatus"
                    ):
                        render_authoring._validate_invitation_summary(
                            layout, response
                        )

    def test_guardless_receipt_returns_legacy_completion_for_lineage(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir)
            layout = render_authoring.AuthoringLayout(
                ayah_ref="29:38",
                folder="s029",
                stem="29_38",
                inputs=root / "inputs",
                outputs=root / "outputs",
            )
            layout.inputs.mkdir(parents=True)
            receipts_dir = layout.outputs / "receipts"
            receipts_dir.mkdir(parents=True)
            merge_receipt = receipts_dir / "merge.json"
            editorial_receipt = receipts_dir / "editorial.json"
            merge_receipt.write_text('{"stage":"merge"}\n', encoding="utf-8")
            editorial_receipt.write_text(
                '{"stage":"editorial"}\n', encoding="utf-8"
            )

            def file_record(path: Path) -> dict[str, object]:
                payload = path.read_bytes()
                return {
                    "path": render_authoring._manifest_path(path),
                    "bytes": len(payload),
                    "sha256": render_authoring._sha256_bytes(payload),
                }

            output_records: dict[str, dict[str, object]] = {}
            for index in range(8):
                output = layout.outputs / "legacy" / f"output-{index}.md"
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(f"output-{index}\n", encoding="utf-8")
                output_records[f"output-{index}"] = file_record(output)

            merge_record = file_record(merge_receipt)
            editorial_record = file_record(editorial_receipt)
            legacy_completion = {
                "schema_version": "commentary-v3-authoring-completion-v2",
                "ayah_ref": "29:38",
                "lineage": [merge_record, editorial_record],
                "phase_receipts": {
                    "canonical_merge": merge_record["path"],
                    "canonical_editorial": editorial_record["path"],
                },
                "outputs": output_records,
            }
            extra_lineage = layout.outputs / "legacy" / "extra-lineage.json"
            extra_lineage.write_text("{}\n", encoding="utf-8")
            legacy_completions = [legacy_completion, copy.deepcopy(legacy_completion)]
            legacy_completions[1]["lineage"].append(file_record(extra_lineage))
            completion_paths: list[Path] = []
            for completion in legacy_completions:
                completion_path = (
                    layout.outputs
                    / "completion"
                    / render_authoring._sha256_json(completion)
                    / "COMPLETION.json"
                )
                completion_path.parent.mkdir(parents=True)
                completion_path.write_text(
                    render_authoring._pretty_json(completion), encoding="utf-8"
                )
                completion_paths.append(completion_path.resolve())
            manifest_path = layout.inputs / "manifest.json"
            manifest_path.write_text("{}\n", encoding="utf-8")
            actual_receipt = render_authoring._load_object(merge_receipt)
            legacy_paths: list[Path] = []

            with patch.object(
                render_authoring,
                "_expected_turn_receipt",
                return_value=(actual_receipt, merge_receipt),
            ):
                loaded = render_authoring._load_verified_turn_receipt(
                    layout,
                    manifest_path,
                    merge_receipt,
                    legacy_completion_paths=legacy_paths,
                )

            self.assertEqual(loaded, actual_receipt)
            self.assertEqual(set(legacy_paths), set(completion_paths))

    def test_completion_binds_invitation_as_ninth_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir)
            layout = render_authoring.AuthoringLayout(
                ayah_ref="29:38",
                folder="s029",
                stem="29_38",
                inputs=root / "inputs",
                outputs=root / "outputs",
            )
            first_pass: dict[str, Path] = {}
            editorial: dict[str, Path] = {}
            for phase, target in (
                ("first", first_pass),
                ("editorial", editorial),
            ):
                for key in ("prose", "evidence", "index", "friction"):
                    path = layout.outputs / phase / f"{key}.md"
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(f"{phase}-{key}\n", encoding="utf-8")
                    target[key] = path
            invitation = layout.outputs / "invitation" / "summary.md"
            invitation.parent.mkdir(parents=True)
            invitation.write_text("invitation\n", encoding="utf-8")
            invitation_session = layout.outputs / "sessions" / "invitation.json"
            invitation_session.parent.mkdir(parents=True)
            invitation_session.write_text("{}\n", encoding="utf-8")
            merge_receipt = layout.outputs / "receipts" / "merge.json"
            editorial_receipt = layout.outputs / "receipts" / "editorial.json"
            merge_receipt.parent.mkdir(parents=True)
            merge_receipt.write_text("{}\n", encoding="utf-8")
            editorial_receipt.write_text("{}\n", encoding="utf-8")

            completion, _path = render_authoring._authoring_completion(
                layout,
                "29:38",
                [invitation_session],
                first_pass,
                editorial,
                invitation,
                invitation_session,
                merge_receipt,
                editorial_receipt,
            )
            self.assertEqual(
                completion["schema_version"],
                "commentary-v3-authoring-completion-v3",
            )
            self.assertEqual(len(completion["outputs"]), 9)
            self.assertIn("invitation.summary", completion["outputs"])
            self.assertFalse(
                completion["invitation_summary"][
                    "locked_finding_coverage_required"
                ]
            )


if __name__ == "__main__":
    unittest.main()
