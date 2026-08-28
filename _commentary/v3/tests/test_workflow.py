from __future__ import annotations

import argparse
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch


V3_ROOT = Path(__file__).resolve().parent.parent

import sys

sys.path.insert(0, str(V3_ROOT))

import workflow  # noqa: E402
from v3lib.common import PathConfinementError, ValidationError  # noqa: E402


class AdvanceWorkflowTests(unittest.TestCase):
    def _adjudication_manifest(self) -> dict:
        return {
            "identity": {
                "ayah_ref": "29:38",
                "source_canonical_sha256": "a" * 64,
                "docket_payload_sha256": "b" * 64,
                "prompt_sha256": "e" * 64,
            },
            "budget": {"prompt_bytes": 123},
        }

    def _synthesis_manifest(self) -> dict:
        return {
            "identity": {
                "ayah_ref": "29:38",
                "source_canonical_sha256": "a" * 64,
                "docket_payload_sha256": "b" * 64,
                "adjudication_payload_sha256": "c" * 64,
                "synthesis_packet_sha256": "d" * 64,
                "prompt_sha256": "f" * 64,
            },
            "budget": {"prompt_bytes": 456},
        }

    def _args(self) -> argparse.Namespace:
        return argparse.Namespace(
            bundle=Path("source.json"),
            hft_policy="quarantine",
            allow_legacy_hft_response=False,
            allow_incomplete_branch_coverage=False,
            max_optional_candidates=40,
            max_support_chars=1_600,
            max_support_per_candidate=5,
            max_branch_bytes_per_root=32_000,
            max_pericope_ayahs=512,
            max_docket_bytes=500_000,
            force=False,
        )

    def _prepare_result(self, source_path: Path) -> tuple[dict, dict, dict]:
        return (
            {
                "identity": {"ayah_ref": "29:38"},
                "readiness": {
                    "mode": "quarantine_without_hft",
                    "warnings": ["HFT quarantined"],
                    "degraded_reasons": ["quarantined_hft"],
                },
            },
            {
                "candidates": [{"candidate_id": "cand_1"}],
                "identity": {
                    "ayah_ref": "29:38",
                    "source_canonical_sha256": "a" * 64,
                    "docket_payload_sha256": "b" * 64,
                },
                "scope": {"branch_coverage": {"complete": True}},
            },
            {"source_bundle": str(source_path)},
        )

    def test_adjudication_discovery_capacity_has_no_cli_pruning_switch(self) -> None:
        parser = workflow._build_parser()
        for command in ("render-synthesis", "validate-synthesis", "verify"):
            args = parser.parse_args([command, "--ayah", "29:38"])
            self.assertEqual(
                workflow._adjudication_options(args), workflow.AdjudicationOptions()
            )
        advance = parser.parse_args(
            [
                "advance",
                "--bundle",
                "fixture.json",
            ]
        )
        self.assertEqual(
            workflow._adjudication_options(advance), workflow.AdjudicationOptions()
        )

    def test_synthesis_density_caps_have_no_cli_switch(self) -> None:
        parser = workflow._build_parser()
        subparsers = next(
            action
            for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)
        )
        forbidden = {
            "--max-paragraphs",
            "--max-findings",
            "--max-friction-notes",
        }
        for command in (
            "advance",
            "render-synthesis",
            "validate-synthesis",
            "verify",
        ):
            option_strings = {
                option
                for action in subparsers.choices[command]._actions
                for option in action.option_strings
            }
            self.assertFalse(forbidden & option_strings)

    def test_advance_stops_at_adjudication_handoff(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            response = temporary / "adjudication.response.json"
            validate_adjudication = Mock()
            with (
                patch.object(
                    workflow,
                    "prepare_bundle_file",
                    return_value=self._prepare_result(temporary / "source.bundle.json"),
                ),
                patch.object(
                    workflow,
                    "render_adjudication_for_ayah",
                    return_value=(
                        "prompt",
                        self._adjudication_manifest(),
                        {
                            "prompt": str(temporary / "adjudication.prompt.md"),
                            "prompt_manifest": str(temporary / "adjudication.prompt.json"),
                            "expected_response": str(response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_adjudication_for_ayah",
                    validate_adjudication,
                ),
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = workflow._run_advance(self._args())
            self.assertEqual(result, 0)
            self.assertEqual(json.loads(output.getvalue())["stage"], "adjudication")
            validate_adjudication.assert_not_called()

    def test_advance_treats_identity_mismatched_response_as_stale(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            response = temporary / "adjudication.response.json"
            response.write_text(
                json.dumps(
                    {
                        "identity": {
                            "ayah_ref": "29:38",
                            "source_canonical_sha256": "a" * 64,
                            "docket_payload_sha256": "c" * 64,
                            "prompt_sha256": "e" * 64,
                        }
                    }
                ),
                encoding="utf-8",
            )
            validate_adjudication = Mock()
            with (
                patch.object(
                    workflow,
                    "prepare_bundle_file",
                    return_value=self._prepare_result(temporary / "source.bundle.json"),
                ),
                patch.object(
                    workflow,
                    "render_adjudication_for_ayah",
                    return_value=(
                        "prompt",
                        self._adjudication_manifest(),
                        {
                            "prompt": str(temporary / "adjudication.prompt.md"),
                            "prompt_manifest": str(temporary / "adjudication.prompt.json"),
                            "expected_response": str(response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_adjudication_for_ayah",
                    validate_adjudication,
                ),
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = workflow._run_advance(self._args())
            payload = json.loads(output.getvalue())
            self.assertEqual(result, 0)
            self.assertEqual(payload["stage"], "adjudication")
            self.assertEqual(payload["response_state"], "stale")
            validate_adjudication.assert_not_called()

    def test_advance_stops_at_synthesis_handoff(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            adjudication_response = temporary / "adjudication.response.json"
            adjudication_response.write_text(
                json.dumps({"identity": self._adjudication_manifest()["identity"]}),
                encoding="utf-8",
            )
            synthesis_response = temporary / "synthesis.response.json"
            validate_synthesis = Mock()
            with (
                patch.object(
                    workflow,
                    "prepare_bundle_file",
                    return_value=self._prepare_result(temporary / "source.bundle.json"),
                ),
                patch.object(
                    workflow,
                    "render_adjudication_for_ayah",
                    return_value=(
                        "prompt",
                        self._adjudication_manifest(),
                        {
                            "prompt": str(temporary / "adjudication.prompt.md"),
                            "prompt_manifest": str(temporary / "adjudication.prompt.json"),
                            "expected_response": str(adjudication_response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_adjudication_for_ayah",
                    return_value=({"coverage": {"selected": 1}}, {"validated": "a.json"}),
                ),
                patch.object(
                    workflow,
                    "render_synthesis_for_ayah",
                    return_value=(
                        {
                            "identity": {
                                "ayah_ref": "29:38",
                                "source_canonical_sha256": "a" * 64,
                                "docket_payload_sha256": "b" * 64,
                                "adjudication_payload_sha256": "c" * 64,
                                "synthesis_packet_sha256": "d" * 64,
                            },
                            "selections": [{"candidate_id": "cand_1"}],
                        },
                        "prompt",
                        self._synthesis_manifest(),
                        {
                            "prompt": str(temporary / "synthesis.prompt.md"),
                            "prompt_manifest": str(temporary / "synthesis.prompt.json"),
                            "expected_response": str(synthesis_response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_synthesis_for_ayah",
                    validate_synthesis,
                ),
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = workflow._run_advance(self._args())
            self.assertEqual(result, 0)
            self.assertEqual(json.loads(output.getvalue())["stage"], "synthesis")
            validate_synthesis.assert_not_called()

    def test_advance_validates_and_verifies_complete_run(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            adjudication_response = temporary / "adjudication.response.json"
            synthesis_response = temporary / "synthesis.response.json"
            adjudication_response.write_text(
                json.dumps({"identity": self._adjudication_manifest()["identity"]}),
                encoding="utf-8",
            )
            synthesis_response.write_text(
                json.dumps({"identity": self._synthesis_manifest()["identity"]}),
                encoding="utf-8",
            )
            verification = {"ayah_ref": "29:38", "outputs": {"prose": {"bytes": 12}}}
            with (
                patch.object(
                    workflow,
                    "prepare_bundle_file",
                    return_value=self._prepare_result(temporary / "source.bundle.json"),
                ),
                patch.object(
                    workflow,
                    "render_adjudication_for_ayah",
                    return_value=(
                        "prompt",
                        self._adjudication_manifest(),
                        {
                            "prompt": "a.md",
                            "prompt_manifest": "a.json",
                            "expected_response": str(adjudication_response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_adjudication_for_ayah",
                    return_value=({"coverage": {"selected": 1}}, {"validated": "a.json"}),
                ),
                patch.object(
                    workflow,
                    "render_synthesis_for_ayah",
                    return_value=(
                        {
                            "identity": {
                                "ayah_ref": "29:38",
                                "source_canonical_sha256": "a" * 64,
                                "docket_payload_sha256": "b" * 64,
                                "adjudication_payload_sha256": "c" * 64,
                                "synthesis_packet_sha256": "d" * 64,
                            },
                            "selections": [{"candidate_id": "cand_1"}],
                        },
                        "prompt",
                        self._synthesis_manifest(),
                        {
                            "prompt": "s.md",
                            "prompt_manifest": "s.json",
                            "expected_response": str(synthesis_response),
                        },
                    ),
                ),
                patch.object(
                    workflow,
                    "validate_synthesis_for_ayah",
                    return_value=({"coverage": {"selected": 1}}, {}, {"validated": "s.json"}),
                ),
                patch.object(
                    workflow,
                    "verify_final_outputs_for_ayah",
                    return_value=verification,
                ),
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = workflow._run_advance(self._args())
            payload = json.loads(output.getvalue())
            self.assertEqual(result, 0)
            self.assertEqual(payload["stage"], "complete")
            self.assertEqual(payload["verification"], verification)

    def test_response_handoff_requires_a_confined_regular_file(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            missing = temporary / "missing.json"
            self.assertFalse(workflow._raw_response_is_present(str(missing)))
            regular = temporary / "response.json"
            regular.write_text("{}", encoding="utf-8")
            self.assertTrue(workflow._raw_response_is_present(str(regular)))
            self.assertEqual(
                workflow._raw_response_state(
                    str(regular), expected_identity={}, max_bytes=1
                ),
                "invalid",
            )
            linked = temporary / "linked.json"
            linked.symlink_to(regular)
            with self.assertRaises(PathConfinementError):
                workflow._raw_response_is_present(str(linked))

    def test_response_state_rejects_malformed_or_incomplete_identity(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.OUTPUTS_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            malformed = temporary / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            self.assertEqual(
                workflow._raw_response_state(
                    str(malformed),
                    expected_identity=self._adjudication_manifest()["identity"],
                ),
                "invalid",
            )
            incomplete = temporary / "incomplete.json"
            identity = dict(self._adjudication_manifest()["identity"])
            identity.pop("prompt_sha256")
            incomplete.write_text(
                json.dumps({"identity": identity}), encoding="utf-8"
            )
            self.assertEqual(
                workflow._raw_response_state(
                    str(incomplete),
                    expected_identity=self._adjudication_manifest()["identity"],
                ),
                "invalid",
            )

    def test_advance_accepts_lossless_synthesis_capacity_configuration(self) -> None:
        args = workflow._build_parser().parse_args(
            [
                "advance",
                "--bundle",
                "source.json",
                "--max-packet-bytes",
                "301000",
                "--max-prompt-bytes",
                "376000",
                "--max-response-bytes",
                "501000",
                "--max-annotation-chars",
                "12000",
                "--min-prose-chars",
                "400",
                "--max-prose-chars",
                "23000",
                "--max-rendered-output-bytes",
                "902000",
            ]
        )
        self.assertEqual(
            workflow._synthesis_options(args),
            workflow.SynthesisOptions(
                max_packet_bytes=301_000,
                max_prompt_bytes=376_000,
                max_response_bytes=501_000,
                max_annotation_chars=12_000,
                min_prose_chars=400,
                max_prose_chars=23_000,
                max_rendered_output_bytes=902_000,
            ),
        )

    def test_verify_accepts_lossless_synthesis_capacity_configuration(self) -> None:
        args = workflow._build_parser().parse_args(
            [
                "verify",
                "--ayah",
                "29:38",
                "--max-packet-bytes",
                "301000",
                "--max-prompt-bytes",
                "376000",
                "--max-response-bytes",
                "501000",
                "--max-annotation-chars",
                "12000",
                "--min-prose-chars",
                "400",
                "--max-prose-chars",
                "23000",
                "--max-rendered-output-bytes",
                "902000",
            ]
        )
        self.assertEqual(
            workflow._synthesis_options(args),
            workflow.SynthesisOptions(
                max_packet_bytes=301_000,
                max_prompt_bytes=376_000,
                max_response_bytes=501_000,
                max_annotation_chars=12_000,
                min_prose_chars=400,
                max_prose_chars=23_000,
                max_rendered_output_bytes=902_000,
            ),
        )

    def test_cli_reports_persisted_artifact_validation_errors_as_exit_2(self) -> None:
        error = "Validated findings[0] fields disagree with contract"
        stderr = io.StringIO()
        with (
            patch.object(workflow, "_run_verify", side_effect=ValidationError(error)),
            redirect_stderr(stderr),
        ):
            result = workflow.main(["verify", "--ayah", "29:38"])
        payload = json.loads(stderr.getvalue())
        self.assertEqual(result, 2)
        self.assertEqual(payload["error_type"], "ValidationError")
        self.assertEqual(payload["message"], error)


if __name__ == "__main__":
    unittest.main()
