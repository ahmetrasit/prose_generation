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
import build_pericope_bundles as pericope_builder  # noqa: E402


def numbered_bundle(ref: str) -> dict[str, object]:
    surah, ayah = (int(item) for item in ref.split(":"))
    return {
        "bundle_type": "ayah",
        "schema_version": "input-bundle-v4",
        "unit_kind": "numbered_ayah",
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": ref,
        "text": {"arabic_uthmani": "text"},
        "qac_morphemes": [{"qac_ref": f"{ref}:1:1"}],
        "word_analysis": {"ref": ref, "words": []},
        "coverage": {},
    }


def basmala_bundle(ref: str) -> dict[str, object]:
    surah = int(ref.split(":", 1)[0])
    bundle = numbered_bundle("1:1")
    bundle.update({
        "unit_kind": "prefatory_basmala",
        "surah": surah,
        "ayah": 0,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": "1:1",
        "text": {"arabic_uthmani": "basmala"},
        "coverage": {
            "basmala_alias": {
                "normalized_surface_equivalent": True,
                "target_normalized": "basmala",
                "source_normalized": "basmala",
            }
        },
    })
    return bundle


def lane_packet(
    ref: str,
    lane: str,
    packet_hash: str,
    *,
    candidate_id: str | None = None,
    support_id: str = "sup_test",
) -> dict[str, object]:
    candidates = []
    supports = []
    if candidate_id is not None:
        candidates.append({"candidate_id": candidate_id, "anchor_refs": [ref]})
        supports.append({"support_id": support_id})
    return {
        "identity": {
            "ayah_ref": ref,
            "lane": lane,
            "lane_packet_sha256": packet_hash,
        },
        "focus_surface_evidence": {"arabic_uthmani": "text"},
        "candidate_inventory": candidates,
        "support_registry": supports,
        "branch_registry": [],
        "connection_registry": [],
    }


def valid_contribution(
    ref: str,
    lane: str,
    packet_hash: str,
    request_hash: str,
    *,
    candidate_id: str | None = None,
    support_id: str = "sup_test",
) -> dict[str, object]:
    decisions = []
    findings = []
    movements = []
    if candidate_id is not None:
        finding_ref = f"{lane}:finding"
        decisions.append({
            "candidate_id": candidate_id,
            "decision": "accept",
            "reason": "The packet supplies a bounded mechanism.",
            "finding_refs": [finding_ref],
        })
        findings.append({
            "finding_ref": finding_ref,
            "title": "Finding",
            "claim": "Bounded claim",
            "mechanism": "Concrete mechanism",
            "reader_payoff": "Concrete payoff",
            "containment": "Bounded to the cited evidence",
            "epistemic_status": "grounded",
            "candidate_ids": [candidate_id],
            "support_ids": [support_id],
            "branch_refs": [],
            "connection_refs": [],
            "context_refs": [ref],
        })
        movements.append({
            "movement_key": "movement",
            "draft_prose": "Akici Turkce hareket.",
            "finding_refs": [finding_ref],
        })
    return {
        "schema_version": workflow.SCOPE_CONTRIBUTION_SCHEMA_VERSION,
        "identity": {
            "ayah_ref": ref,
            "lane": lane,
            "lane_packet_sha256": packet_hash,
            "authoring_request_sha256": request_hash,
        },
        "ayah_ref": ref,
        "lane": lane,
        "coverage_complete": True,
        "candidate_decisions": decisions,
        "findings": findings,
        "movements": movements,
        "friction_notes": [],
    }


class LayoutTests(unittest.TestCase):
    def test_layout_has_only_three_artifact_roots(self) -> None:
        layout = workflow.layout_for("29:38")
        self.assertEqual(
            layout.input, workflow.INPUT_ROOT / "native" / "s029" / "29_38"
        )
        self.assertEqual(
            layout.raw, workflow.RAW_ROOT / "native" / "s029" / "29_38"
        )
        self.assertEqual(
            layout.editorial,
            workflow.EDITORIAL_ROOT / "native" / "s029" / "29_38",
        )

    def test_analysis_namespaces_have_disjoint_fixed_paths(self) -> None:
        native = workflow.layout_for("100:1")
        custom = workflow.layout_for("100:1", "fatiha-lens-s100")
        self.assertNotEqual(native.input, custom.input)
        self.assertEqual(
            custom.input,
            workflow.INPUT_ROOT / "fatiha-lens-s100" / "s100" / "100_1",
        )

    def test_prefatory_basmala_is_supported_except_s1_and_s9(self) -> None:
        self.assertEqual(workflow.layout_for("100:0").ayah_ref, "100:0")
        for ref in ("1:0", "9:0"):
            with self.subTest(ref=ref):
                with self.assertRaises(workflow.WorkflowError):
                    workflow.layout_for(ref)

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

    def test_add_ayat_cli_accepts_repeatable_comma_lists(self) -> None:
        args = workflow._parser().parse_args([
            "prepare",
            "--ayah", "100:1",
            "--analysis-id", "s100-external",
            "--segment", "host=100:1-2",
            "--member-surah", "100",
            "--add-ayat", "1:1,1:2",
            "--add-ayat", "17:50",
        ])
        self.assertEqual(args.add_ayat, ["1:1,1:2", "17:50"])

    def test_focus_uses_configured_bundle_root_without_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            selected = root / "selected"
            args = SimpleNamespace(ayah="29:38", source_bundle=None)
            self.assertEqual(
                workflow._focus_bundle_origin(args, selected, selected),
                selected / "s029" / "29_38.ayah.json",
            )

    def test_numbered_focus_never_falls_back_to_member_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package_root = root / "package"
            member_root = root / "members"
            args = SimpleNamespace(ayah="29:38", source_bundle=None)
            self.assertEqual(
                workflow._focus_bundle_origin(args, package_root, member_root),
                package_root / "s029" / "29_38.ayah.json",
            )

    def test_prefatory_focus_uses_member_bundle_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package_root = root / "package"
            member_root = root / "members"
            args = SimpleNamespace(ayah="100:0", source_bundle=None)
            composition = workflow.compositions.composition_from_cli(
                "s100-basmala",
                ["target=100:0,100:1"],
                ["100:0"],
            )
            self.assertEqual(
                workflow._focus_bundle_origin(
                    args, package_root, member_root
                ),
                member_root / "s100" / "100_0.ayah.json",
            )

    def test_analysis_handoffs_use_input_raw_and_editorial_roots(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("100:1", "basmala-s100")
                scope = workflow._scope_handoff(
                    layout,
                    {"lanes": {"micro": {"request_sha256": "a" * 64}}},
                    "micro",
                )
                canonical = workflow._canonical_handoff(
                    layout, {"request_sha256": "b" * 64}
                )
                editorial = workflow._editorial_handoff(
                    layout, {"request_sha256": "c" * 64}
                )

                self.assertEqual(Path(scope["prompt"]), layout.scope_prompt("micro"))
                self.assertEqual(
                    Path(scope["expected_response"]),
                    layout.scope_contribution("micro"),
                )
                self.assertTrue(
                    all(
                        Path(path).parent == layout.raw
                        for path in canonical["expected_outputs"].values()
                    )
                )
                self.assertTrue(
                    all(
                        Path(path).parent == layout.editorial
                        for path in editorial["expected_outputs"].values()
                    )
                )
                self.assertIn(
                    "--analysis-id basmala-s100",
                    canonical["after_first_pass"]["command"],
                )


class BasmalaFocusPolicyTests(unittest.TestCase):
    @staticmethod
    def quran_evidence(ayah_count: int = 11) -> dict[str, dict[str, object]]:
        return {
            **{"100:0": {}},
            **{f"100:{ayah}": {} for ayah in range(1, ayah_count + 1)},
        }

    def test_implicit_basmala_analysis_contains_the_complete_host_surah(self) -> None:
        composition = workflow._automatic_basmala_composition(
            "100:0", self.quran_evidence()
        )

        self.assertEqual(composition.analysis_id, "s100-basmala-full")
        self.assertEqual(
            composition.ordered_refs,
            ("100:0", *[f"100:{ayah}" for ayah in range(1, 12)]),
        )
        self.assertEqual(
            [(row["ref"], row["lane"]) for row in composition.context_rows("100:0")],
            [(f"100:{ayah}", "macro") for ayah in range(1, 12)],
        )

    def test_trailing_truncated_quran_source_is_not_a_complete_host_surah(self) -> None:
        with self.assertRaisesRegex(
            workflow.WorkflowError, "complete canonical numbered ayat"
        ):
            workflow._automatic_basmala_composition(
                "100:0", self.quran_evidence(ayah_count=2)
            )

    def test_incomplete_basmala_composition_is_rejected(self) -> None:
        composition = workflow.compositions.composition_from_cli(
            "incomplete-basmala",
            ["host=100:0,100:1-2"],
            ["100:0"],
        )

        with self.assertRaisesRegex(
            workflow.WorkflowError, "complete numbered host surah"
        ):
            workflow._validate_basmala_focus_context(
                composition, self.quran_evidence()
            )

    def test_basmala_host_ayat_must_stay_in_the_focus_segment(self) -> None:
        composition = workflow.compositions.composition_from_cli(
            "split-basmala",
            ["host=100:0,100:1", "remainder=100:2-11"],
            ["100:0"],
        )

        with self.assertRaisesRegex(
            workflow.WorkflowError, "complete numbered host surah"
        ):
            workflow._validate_basmala_focus_context(
                composition, self.quran_evidence()
            )

    def test_native_basmala_prepare_fails_closed_without_cli_derivation(self) -> None:
        layout = workflow.layout_for("100:0")
        with self.assertRaisesRegex(workflow.WorkflowError, "basmala-only native"):
            workflow._composition_for_prepare(
                SimpleNamespace(composition=None), layout
            )

    def test_complete_basmala_context_lane_contract_is_exact(self) -> None:
        composition = workflow._automatic_basmala_composition(
            "100:0", self.quran_evidence()
        )
        expected = workflow._expected_context_lanes(
            composition, "100:0", None
        )

        self.assertEqual(
            expected,
            {f"100:{ayah}": ["macro"] for ayah in range(1, 12)},
        )

    def test_automatic_numbered_focus_basmala_routes_only_to_macro(self) -> None:
        expected = workflow._expected_context_lanes(None, "100:1", "100:0")
        self.assertEqual(expected, {"100:0": ["macro"]})
        self.assertEqual(
            [
                workflow._expected_lane_context_refs(
                    None, "100:1", "100:0", lane
                )
                for lane in workflow.LANES
            ],
            [[], ["100:0"], []],
        )


class PromptTests(unittest.TestCase):
    def test_scope_template_combines_decision_and_prose_in_one_pass(self) -> None:
        prompt = (workflow.PROMPTS_ROOT / "scope.md").read_text(encoding="utf-8")
        self.assertIn("one-pass scope author", prompt)
        self.assertIn("prose-ready Turkish movement", prompt)
        self.assertIn("candidate_decisions", prompt)
        self.assertIn("@@CANONICAL_PROMPT_V2@@", prompt)
        self.assertNotIn("scope-review-v2", prompt)

    def test_governing_spec_matches_active_lane_and_workflow_contract(self) -> None:
        spec = (workflow.REPO_ROOT / "COMMENTARY_SPEC.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("adds the host surah's `S:0` bundle once to macro", spec)
        self.assertIn("one-pass micro, macro, and", spec)
        self.assertNotIn("enter all three lanes", spec)
        self.assertNotIn("prompts and editorial instructions remain the V3 prompts", spec)

    def test_editorial_source_is_unchanged_v3_prompt(self) -> None:
        source = workflow.V3_PROMPTS_ROOT / "editorial-followup.md"
        self.assertEqual(
            workflow._sha256(source.read_bytes()),
            "5c26ef4d839e15ce8879a4d1811c5fb5e13b30d7c10d15801da3992541c72fea",
        )

    def test_canonical_prompt_is_merge_only(self) -> None:
        prompt = (workflow.PROMPTS_ROOT / "canonical.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Your job is composition, not adjudication", prompt)
        self.assertIn("Preserve every supplied finding exactly once", prompt)
        self.assertIn("@@MICRO_CONTRIBUTION_JSON@@", prompt)
        self.assertNotIn("@@MICRO_PACKET_PATH@@", prompt)
        self.assertNotIn("recover accounting", prompt)

    def test_canonical_render_rejects_unbound_markers(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "marker mismatch"):
            workflow._render("@@ONE@@ @@TWO@@", {"@@ONE@@": "one"}, label="test")

    def test_canonical_render_contains_contributions_but_no_packet_paths(self) -> None:
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
                contributions = {}
                for lane in workflow.LANES:
                    packet_hash = workflow._sha256(f"{lane}-packet".encode())
                    request_hash = workflow._sha256(f"{lane}-request".encode())
                    layout.packet(lane).write_text(
                        json.dumps(lane_packet("1:1", lane, packet_hash)),
                        encoding="utf-8",
                    )
                    contribution = valid_contribution(
                        "1:1", lane, packet_hash, request_hash
                    )
                    layout.scope_contribution(lane).write_text(
                        json.dumps(contribution), encoding="utf-8"
                    )
                    contributions[lane] = contribution
                manifest = {
                    "editorial": {
                        "instructions_sha256": "a" * 64,
                        "handoff_template_sha256": "b" * 64,
                    }
                }

                prompt, record = workflow._build_canonical_prompt(
                    layout, manifest, contributions
                )

                self.assertIn("<micro_contribution_json>", prompt)
                self.assertNotIn(str(layout.packet("micro")), prompt)
                self.assertNotIn("micro_packet_sha256", record["inputs"])
                self.assertIn("micro_contribution_sha256", record["inputs"])


class ColdStartSmokeTests(unittest.TestCase):
    def test_real_prepare_returns_three_one_pass_scope_handoffs(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                args = workflow._parser().parse_args(
                    ["advance", "--ayah", "1:1"]
                )
                args.ayah = "1:1"
                args.composition = None

                prepared = workflow.prepare(args)
                status = workflow.advance(args)
                layout = workflow.layout_for("1:1")
                manifest = json.loads(layout.manifest.read_text(encoding="utf-8"))

                self.assertEqual(prepared["status"], "prepared")
                self.assertEqual(status["stage"], "scope_authoring")
                self.assertEqual(
                    [handoff["role"] for handoff in status["handoffs"]],
                    [f"{lane}_scope_author" for lane in workflow.LANES],
                )
                self.assertEqual(
                    manifest["schema_version"],
                    workflow.UNIT_MANIFEST_SCHEMA_VERSION,
                )
                for lane in workflow.LANES:
                    self.assertEqual(
                        manifest["lanes"][lane]["expected_response"],
                        workflow._repo_path(layout.scope_contribution(lane)),
                    )
                    prompt = layout.scope_prompt(lane).read_text(encoding="utf-8")
                    self.assertIn("one-pass scope author", prompt)
                    self.assertIn("<canonical_prompt_v2>", prompt)

    def test_packet_source_coverage_must_match_revalidated_manifest_sources(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                args = workflow._parser().parse_args(
                    ["prepare", "--ayah", "1:1"]
                )
                args.ayah = "1:1"
                args.composition = None
                workflow.prepare(args)
                layout = workflow.layout_for("1:1")

                packet = json.loads(
                    layout.packet("macro").read_text(encoding="utf-8")
                )
                packet["source_coverage"]["quran_text_source"]["ayah_count"] += 1
                packet["identity"]["lane_packet_sha256"] = (
                    workflow.v3._payload_hash_with_identity_field_removed(
                        packet, "lane_packet_sha256"
                    )
                )
                layout.packet("macro").write_bytes(
                    workflow._canonical_json_bytes(packet, newline=True)
                )

                manifest = json.loads(layout.manifest.read_text(encoding="utf-8"))
                manifest["lanes"]["macro"]["packet"] = workflow._path_record(
                    layout.packet("macro")
                )
                manifest["lanes"]["macro"]["lane_packet_sha256"] = packet[
                    "identity"
                ]["lane_packet_sha256"]
                layout.manifest.write_bytes(workflow._pretty_json_bytes(manifest))

                with self.assertRaisesRegex(
                    workflow.WorkflowError, "Quran text provenance is stale"
                ):
                    workflow._load_unit_manifest(layout)


class ContributionValidationTests(unittest.TestCase):
    def test_valid_complete_contribution_is_loaded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.input.mkdir(parents=True)
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
            packet = lane_packet(
                "1:1", "micro", packet_hash, candidate_id="cand_test"
            )
            layout.packet("micro").write_text(json.dumps(packet), encoding="utf-8")
            response = valid_contribution(
                "1:1",
                "micro",
                packet_hash,
                request_hash,
                candidate_id="cand_test",
            )
            layout.scope_contribution("micro").write_text(
                json.dumps(response), encoding="utf-8"
            )
            self.assertEqual(
                workflow._load_contribution(layout, manifest, "micro"), response
            )

    def test_incomplete_candidate_accounting_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.input.mkdir(parents=True)
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
            packet = lane_packet(
                "1:1", "micro", packet_hash, candidate_id="cand_test"
            )
            layout.packet("micro").write_text(json.dumps(packet), encoding="utf-8")
            response = valid_contribution(
                "1:1", "micro", packet_hash, request_hash
            )
            layout.scope_contribution("micro").write_text(
                json.dumps(response), encoding="utf-8"
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "accounting is incomplete"):
                workflow._load_contribution(layout, manifest, "micro")

    def test_each_finding_must_land_once(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        layout = workflow.layout_for("1:1")
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1",
            "micro",
            packet_hash,
            request_hash,
            candidate_id="cand_test",
        )
        contribution["movements"] = []
        manifest = {
            "lanes": {
                "micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }
            }
        }
        with self.assertRaisesRegex(workflow.WorkflowError, "coverage is incomplete"):
            workflow._validate_scope_contribution(
                contribution,
                layout=layout,
                manifest=manifest,
                lane="micro",
                packet=packet,
            )

    def test_unknown_context_ref_is_rejected(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        layout = workflow.layout_for("1:1")
        packet = lane_packet(
            "1:1", "macro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1",
            "macro",
            packet_hash,
            request_hash,
            candidate_id="cand_test",
        )
        contribution["findings"][0]["context_refs"] = ["2:2"]
        manifest = {
            "lanes": {
                "macro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }
            }
        }
        with self.assertRaisesRegex(workflow.WorkflowError, "unknown IDs"):
            workflow._validate_scope_contribution(
                contribution,
                layout=layout,
                manifest=manifest,
                lane="macro",
                packet=packet,
            )


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

    def test_unexpected_output_artifact_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("1:1")
                layout.raw.mkdir(parents=True)
                (layout.raw / "1_1.prose.summary.tr.md").write_text(
                    "stale", encoding="utf-8"
                )
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "Unexpected v4 output artifacts"
                ):
                    workflow._assert_fixed_output_names(layout)

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
                    "path": "_commentary/v4/input/native/s001/1_1/canonical.prompt.md",
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
                        layout, {"canonical": None}, contributions={}
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
                    workflow._ensure_canonical(
                        layout, manifest, contributions={}
                    )
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
                    "path": "_commentary/v4/input/native/s001/1_1/canonical.prompt.md",
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
                        layout, manifest, contributions={}, write=False
                    )
            self.assertFalse(layout.canonical_prompt.exists())
            self.assertEqual(manifest, {"canonical": None})


class OrchestrationAcceptanceTests(unittest.TestCase):
    def test_advance_runs_scope_canonical_editorial_and_complete_sequence(
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
                layout.manifest.write_text("{}", encoding="utf-8")
                manifest = {
                    "lanes": {
                        lane: {
                            "request_sha256": workflow._sha256(
                                f"{lane}-request".encode()
                            ),
                            "lane_packet_sha256": workflow._sha256(
                                f"{lane}-packet".encode()
                            ),
                            "packet": {
                                "sha256": workflow._sha256(
                                    f"{lane}-packet".encode()
                                )
                            },
                        }
                        for lane in workflow.LANES
                    },
                    "editorial": {
                        "instructions_sha256": "d" * 64,
                        "handoff_template_sha256": "e" * 64,
                    },
                    "canonical": None,
                    "editorial_turn": None,
                }
                for lane in workflow.LANES:
                    lane_record = manifest["lanes"][lane]
                    layout.packet(lane).write_text(
                        json.dumps(
                            lane_packet(
                                "1:1",
                                lane,
                                lane_record["lane_packet_sha256"],
                                candidate_id=f"cand_{lane}",
                            )
                        ),
                        encoding="utf-8",
                    )
                args = SimpleNamespace(ayah="1:1", force_input=False)

                with patch.object(
                    workflow, "_load_unit_manifest", return_value=manifest
                ):
                    scope = workflow.advance(args)
                    self.assertEqual(scope["stage"], "scope_authoring")
                    self.assertEqual(scope["missing_lanes"], list(workflow.LANES))

                    layout.raw.mkdir(parents=True)
                    for lane in workflow.LANES:
                        lane_record = manifest["lanes"][lane]
                        layout.scope_contribution(lane).write_text(
                            json.dumps(
                                valid_contribution(
                                    "1:1",
                                    lane,
                                    lane_record["lane_packet_sha256"],
                                    lane_record["request_sha256"],
                                    candidate_id=f"cand_{lane}",
                                )
                            ),
                            encoding="utf-8",
                        )

                    canonical = workflow.advance(args)
                    self.assertEqual(canonical["stage"], "canonical_write")
                    self.assertTrue(layout.canonical_prompt.is_file())

                    for kind in workflow.KINDS:
                        layout.first_pass(kind).write_text(
                            f"first-pass {kind}", encoding="utf-8"
                        )

                    editorial = workflow.advance(args)
                    self.assertEqual(editorial["stage"], "canonical_editorial")
                    self.assertTrue(layout.editorial_prompt.is_file())

                    layout.editorial.mkdir(parents=True)
                    for kind in workflow.KINDS:
                        layout.editorial_output(kind).write_text(
                            f"editorial {kind}", encoding="utf-8"
                        )

                    complete = workflow.advance(args)
                    self.assertEqual(complete["status"], "complete")
                    self.assertEqual(
                        set(complete["outputs"]), {"raw", "editorial"}
                    )


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
                "stage": "scope_authoring",
                "handoffs": [
                    {"role": "micro_scope_author"},
                    {"role": "macro_scope_author"},
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
            ["scope_authoring", "scope_authoring", "canonical_write"],
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
    def test_advance_stops_instead_of_repairing_invalid_contribution(
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

                def load_contribution(
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
                        workflow,
                        "_load_contribution",
                        side_effect=load_contribution,
                    ),
                ):
                    with self.assertRaisesRegex(
                        workflow.WorkflowError,
                        "does not issue automated repair turns",
                    ):
                        workflow.advance(
                            SimpleNamespace(ayah="1:1", force_input=False)
                        )

    def test_incomplete_contribution_fails_before_canonical(
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

                def load_contribution(
                    _layout: object, _manifest: object, lane: str
                ) -> dict[str, object]:
                    raise workflow.WorkflowError(
                        f"{lane} contribution must declare coverage_complete=true"
                    )

                with (
                    patch.object(
                        workflow, "_load_unit_manifest", return_value=manifest
                    ),
                    patch.object(
                        workflow,
                        "_load_contribution",
                        side_effect=load_contribution,
                    ),
                ):
                    with self.assertRaisesRegex(
                        workflow.WorkflowError, "coverage_complete=true"
                    ):
                        workflow.advance(
                            SimpleNamespace(ayah="1:1", force_input=False)
                        )

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
                    patch.object(
                        workflow, "_load_contribution", return_value=None
                    ),
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
                layout.scope_contribution("micro").symlink_to(
                    outside / "capture.json"
                )
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
                layout.scope_contribution("micro").mkdir(parents=True)
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

    def test_prefatory_snapshot_is_reverified_and_canonically_bound(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="100:1",
                stem="100_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            layout.input.mkdir()
            bundle = basmala_bundle("100:0")
            layout.prefatory_basmala_bundle.write_text(
                json.dumps(bundle), encoding="utf-8"
            )
            canonical = workflow.compositions.canonical_sha256(bundle)
            manifest = {
                "prefatory_basmala": {
                    "snapshot": workflow._path_record(
                        layout.prefatory_basmala_bundle
                    ),
                    "canonical_sha256": canonical,
                    "ayah_ref": "100:0",
                    "surface_ref": "100:0",
                    "linguistic_source_ref": "1:1",
                    "mode": "included_as_ordinary_context_member",
                    "selected_context_units": [{
                        "ayah_ref": "100:0",
                        "unit_kind": "prefatory_basmala",
                        "surface_ref": "100:0",
                        "linguistic_source_ref": "1:1",
                        "canonical_sha256": canonical,
                        "source_file": "source.json",
                        "lanes": ["macro"],
                    }],
                }
            }

            identity = workflow._verify_prefatory_basmala_record(
                manifest, layout, numbered_bundle("100:1")
            )
            self.assertEqual(identity["canonical_sha256"], canonical)

            layout.prefatory_basmala_bundle.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(workflow.WorkflowError, "stale"):
                workflow._verify_prefatory_basmala_record(
                    manifest, layout, numbered_bundle("100:1")
                )

    def test_legacy_unit_manifest_schema_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V4_ROOT) as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                layout = workflow.layout_for("100:1")
                layout.input.mkdir(parents=True)
                layout.manifest.write_text(
                    json.dumps({
                        "schema_version": "commentary-v4-unit-manifest-v2",
                        "analysis_id": "native",
                        "ayah_ref": "100:1",
                    }),
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "legacy or stale schema"
                ):
                    workflow._load_unit_manifest(layout)


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
    def test_context_lineage_dedupes_lane_specific_routes(self) -> None:
        units = []
        for lane, segment in zip(workflow.LANES, ("automatic", "explicit", "automatic")):
            units.append({
                "ayah_ref": "100:0",
                "unit_kind": "prefatory_basmala",
                "surface_ref": "100:0",
                "linguistic_source_ref": "1:1",
                "canonical_sha256": "a" * 64,
                "source_file": "bundle.json",
                "lane": lane,
                "segment_id": segment,
                "composition_order": 0,
            })
        deduped = workflow._dedupe_context_units(units)
        self.assertEqual(len(deduped), 1)
        self.assertEqual(deduped[0]["lanes"], list(workflow.LANES))
        self.assertEqual(
            deduped[0]["lane_bindings"]["macro"]["segment_id"], "explicit"
        )

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

    def test_out_of_tree_quran_source_round_trips_through_manifest_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "quran.tsv"
            source.write_text("1:1|first\n", encoding="utf-8")

            evidence, coverage = workflow._quran_text_projection(source)
            verified, current = workflow._verified_quran_text_projection(coverage)

        self.assertEqual(coverage["source_path"], str(source.resolve()))
        self.assertEqual(
            evidence["1:1"]["source_pointer"], f"{source.resolve()}#L1"
        )
        self.assertEqual(verified, evidence)
        self.assertEqual(current, coverage)

    def test_inter_ayah_coverage_is_recomputed_on_manifest_load(self) -> None:
        coverage = {
            "source_id": "quran-data/inter-ayah-row-reciprocal-v2",
            "source_document_sha256": "a" * 64,
        }
        inputs = {
            "projection_dir": "/projection",
            "parent_dir": "/parent",
        }
        with patch.object(
            workflow.v3,
            "_inter_ayah_evidence_with_fallback",
            return_value=([], {}, coverage),
        ) as project:
            workflow._verified_inter_ayah_projection(
                coverage,
                inputs,
                focus_ref="1:1",
                numbered_refs={"1:1"},
                prefatory_focus=False,
            )
        project.assert_called_once_with(
            "1:1", Path("/projection"), Path("/parent"), {"1:1"}
        )

        changed = {**coverage, "source_document_sha256": "b" * 64}
        with patch.object(
            workflow.v3,
            "_inter_ayah_evidence_with_fallback",
            return_value=([], {}, changed),
        ):
            with self.assertRaisesRegex(workflow.WorkflowError, "provenance is stale"):
                workflow._verified_inter_ayah_projection(
                    coverage,
                    inputs,
                    focus_ref="1:1",
                    numbered_refs={"1:1"},
                    prefatory_focus=False,
                )

    def test_host_surah_controls_automatic_basmala_for_external_context(self) -> None:
        analysis = workflow.compositions.composition_from_cli(
            "s100-with-s17",
            ["host=100:1-2"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "s100" / "100_0.ayah.json"
            path.parent.mkdir()
            path.write_text(json.dumps(basmala_bundle("100:0")), encoding="utf-8")
            loaded = workflow._load_prefatory_basmala_context(
                numbered_bundle("100:1"), root, analysis
            )
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded[3]["ayah_ref"], "100:0")

    def test_basmala_context_is_mandatory_except_for_s1_and_s9(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for ref in ("1:2", "9:1"):
                with self.subTest(ref=ref):
                    self.assertIsNone(
                        workflow._load_prefatory_basmala_context(
                            numbered_bundle(ref), root, None
                        )
                    )
            with self.assertRaisesRegex(workflow.WorkflowError, "is required"):
                workflow._load_prefatory_basmala_context(
                    numbered_bundle("2:1"), root, None
                )

    def test_flat_context_root_requires_and_revalidates_package_manifest(self) -> None:
        row = {
            "surah": 29,
            "pericope": 3,
            "ayah_from": 38,
            "ayah_to": 38,
            "label": "One ayah",
        }
        with tempfile.TemporaryDirectory(
            dir=workflow.REPO_ROOT / "bundles"
        ) as temporary:
            root = Path(temporary)
            bundle = numbered_bundle("29:38")
            bundle["pericope"] = {
                key: row[key]
                for key in ("surah", "pericope", "ayah_from", "ayah_to", "label")
            }
            bundle_path = root / "29_38.ayah.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            with self.assertRaisesRegex(workflow.WorkflowError, "must carry"):
                workflow._context_package_record(root, None, "29:38")

            manifest_path = pericope_builder.write_manifest(
                row,
                root,
                command=pericope_builder.build_command(
                    row,
                    root,
                    exclude_focus_trace=False,
                    focus_trace_variant=None,
                ),
                pericope_index=None,
                source="cli-span",
            )
            record = workflow._context_package_record(root, None, "29:38")
            self.assertEqual(record["ayah_refs"], ["29:38"])

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["ayah_refs"] = []
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(workflow.WorkflowError, "stale"):
                workflow._verify_context_package_record(record)


class CompositionIntegrationTests(unittest.TestCase):
    def test_lane_augmentation_keeps_micro_local_and_routes_context(self) -> None:
        analysis = workflow.compositions.composition_from_cli(
            "fatiha-lens-s100",
            ["fatiha=1:1", "s100=100:1-2"],
            ["100:1"],
        )
        projection = {
            "by_lane": {
                "micro": {"candidates": [], "supports": [], "units": []},
                "macro": {
                    "candidates": [{"candidate_id": "cand_ctx_macro"}],
                    "supports": [{
                        "support_id": "sup_ctx_macro",
                        "source_type": "context",
                        "role": "context",
                        "payload": {"ref": "100:2"},
                        "context_refs": ["100:2"],
                    }],
                    "units": [{"ayah_ref": "100:2"}],
                },
                "global": {
                    "candidates": [{"candidate_id": "cand_ctx_global"}],
                    "supports": [{
                        "support_id": "sup_ctx_global",
                        "source_type": "context",
                        "role": "context",
                        "payload": {"ref": "1:1"},
                        "context_refs": ["1:1"],
                    }],
                    "units": [{"ayah_ref": "1:1"}],
                },
            },
            "units": [{"ayah_ref": "1:1"}, {"ayah_ref": "100:2"}],
        }

        def packet(lane: str) -> dict[str, object]:
            return {
                "identity": {"lane": lane, "lane_packet_sha256": "old"},
                "scope": {},
                "candidate_inventory": [],
                "support_registry": [],
            }

        source = {"unit_kind": "numbered_ayah"}
        layout = workflow.layout_for("100:1", analysis.analysis_id)
        micro = workflow._augment_lane_packet(
            packet("micro"),
            layout=layout,
            composition=analysis,
            projection=projection,
            source_bundle=source,
            prefatory_basmala_context=None,
            lane="micro",
        )
        macro = workflow._augment_lane_packet(
            packet("macro"),
            layout=layout,
            composition=analysis,
            projection=projection,
            source_bundle=source,
            prefatory_basmala_context=None,
            lane="macro",
        )
        global_packet = workflow._augment_lane_packet(
            packet("global"),
            layout=layout,
            composition=analysis,
            projection=projection,
            source_bundle=source,
            prefatory_basmala_context=None,
            lane="global",
        )

        self.assertEqual(micro["selected_context_units"], [])
        self.assertEqual(macro["selected_context_units"], [{"ayah_ref": "100:2"}])
        self.assertEqual(global_packet["selected_context_units"], [{"ayah_ref": "1:1"}])
        for value in (micro, macro, global_packet):
            self.assertEqual(value["identity"]["analysis_id"], analysis.analysis_id)
            self.assertNotEqual(value["identity"]["lane_packet_sha256"], "old")

    def test_numbered_ayah_macro_packet_includes_prefatory_basmala_context(self) -> None:
        packet = {
            "identity": {"ayah_ref": "100:1", "lane": "macro", "lane_packet_sha256": "old"},
            "scope": {},
            "candidate_inventory": [],
            "support_registry": [],
        }
        basmala_bundle = {
            "bundle_type": "ayah",
            "schema_version": "input-bundle-v4",
            "surah": 100,
            "ayah": 0,
            "ayahRef": "100:0",
            "unit_kind": "prefatory_basmala",
            "surface_ref": "100:0",
            "linguistic_source_ref": "1:1",
            "text": {"arabic_uthmani": "بسم الله الرحمن الرحيم"},
            "qac_morphemes": [{"qac_ref": "1:1:1:1"}],
            "word_analysis": {"ref": "1:1"},
            "coverage": {
                "basmala_alias": {
                    "normalized_surface_equivalent": True,
                    "target_normalized": "بسماللهالرحمنالرحيم",
                    "source_normalized": "بسماللهالرحمنالرحيم",
                }
            },
            "branch_inventories": {"full_context_packet": {"branches": [{"id": "b"}]}},
        }
        basmala_identity = {
            "unit_kind": "prefatory_basmala",
            "ayah_ref": "100:0",
            "surface_ref": "100:0",
            "linguistic_source_ref": "1:1",
            "schema_version": "input-bundle-v4",
            "canonical_sha256": "b" * 64,
            "bytes": 123,
        }

        augmented = workflow._augment_lane_packet(
            packet,
            layout=workflow.layout_for("100:1"),
            composition=None,
            projection=None,
            source_bundle={"unit_kind": "numbered_ayah"},
            prefatory_basmala_context=(
                workflow.REPO_ROOT / "bundles" / "s100" / "100_0.ayah.json",
                basmala_bundle,
                basmala_identity,
            ),
            lane="macro",
        )

        self.assertEqual(
            augmented["scope"]["prefatory_basmala"]["status"],
            "included_as_surah_preface_context",
        )
        self.assertEqual(
            augmented["selected_context_units"][0]["ayah_ref"], "100:0"
        )
        self.assertEqual(
            augmented["candidate_inventory"][0]["source_type"],
            "automatic_prefatory_basmala_surah_member",
        )
        support_roles = {
            support["role"] for support in augmented["support_registry"]
        }
        self.assertEqual(support_roles, {"context_unit_native_depth_evidence"})
        context_support = augmented["support_registry"][0]
        self.assertEqual(
            context_support["payload"]["protocol"],
            workflow.compositions.CONTEXT_MEMBER_PROTOCOL,
        )
        self.assertNotIn(
            "word_analysis", json.dumps(context_support["payload"], ensure_ascii=False)
        )
        self.assertNotEqual(augmented["identity"]["lane_packet_sha256"], "old")

    def test_explicit_basmala_context_is_not_duplicated_by_auto_membership(self) -> None:
        packet = {
            "identity": {"ayah_ref": "100:1", "lane": "macro", "lane_packet_sha256": "old"},
            "scope": {},
            "candidate_inventory": [],
            "support_registry": [],
        }
        projection = {
            "by_lane": {
                "micro": {"candidates": [], "supports": [], "units": []},
                "macro": {
                    "candidates": [{
                        "candidate_id": "cand_explicit_basmala",
                        "source_local_id": "100:0",
                    }],
                    "supports": [{
                        "support_id": "sup_explicit_basmala",
                        "role": "context_unit_native_depth_evidence",
                        "context_refs": ["100:0"],
                    }],
                    "units": [{
                        "ayah_ref": "100:0",
                        "unit_kind": "prefatory_basmala",
                        "surface_ref": "100:0",
                        "linguistic_source_ref": "1:1",
                        "canonical_sha256": "b" * 64,
                        "lane": "macro",
                        "candidate_id": "cand_explicit_basmala",
                        "source_file": "prose_generation/bundles/s100/100_0.ayah.json",
                    }],
                },
                "global": {"candidates": [], "supports": [], "units": []},
            },
            "units": [],
        }
        analysis = workflow.compositions.composition_from_cli(
            "explicit-basmala",
            ["surah=100:0,100:1"],
            ["100:1"],
        )
        augmented = workflow._augment_lane_packet(
            packet,
            layout=workflow.layout_for("100:1", analysis.analysis_id),
            composition=analysis,
            projection=projection,
            source_bundle={"unit_kind": "numbered_ayah"},
            prefatory_basmala_context=(
                workflow.REPO_ROOT / "bundles" / "s100" / "100_0.ayah.json",
                {"ayahRef": "100:0"},
                {
                    "unit_kind": "prefatory_basmala",
                    "ayah_ref": "100:0",
                    "surface_ref": "100:0",
                    "linguistic_source_ref": "1:1",
                    "schema_version": "input-bundle-v4",
                    "canonical_sha256": "b" * 64,
                    "bytes": 123,
                },
            ),
            lane="macro",
        )

        self.assertEqual(
            [
                unit["ayah_ref"]
                for unit in augmented["selected_context_units"]
                if unit.get("ayah_ref") == "100:0"
            ],
            ["100:0"],
        )
        self.assertEqual(len(augmented["candidate_inventory"]), 1)
        self.assertEqual(
            augmented["scope"]["prefatory_basmala"]["via"],
            "explicit_composition_context",
        )

    def test_explicit_basmala_hash_conflict_is_rejected(self) -> None:
        packet = {
            "identity": {"ayah_ref": "100:1", "lane": "micro"},
            "scope": {},
            "candidate_inventory": [],
            "support_registry": [],
            "selected_context_units": [{
                "ayah_ref": "100:0",
                "surface_ref": "100:0",
                "linguistic_source_ref": "1:1",
                "canonical_sha256": "a" * 64,
            }],
        }
        with self.assertRaisesRegex(workflow.WorkflowError, "conflicts"):
            workflow._append_numbered_ayah_basmala_context(
                packet,
                focus_ref="100:1",
                basmala_path=Path("100_0.ayah.json"),
                basmala_bundle=basmala_bundle("100:0"),
                focus_bundle=numbered_bundle("100:1"),
                basmala_identity={
                    "ayah_ref": "100:0",
                    "surface_ref": "100:0",
                    "linguistic_source_ref": "1:1",
                    "canonical_sha256": "b" * 64,
                },
                lane="micro",
            )

    def test_added_ayat_share_one_load_and_project_as_macro_context(self) -> None:
        analysis = workflow.compositions.composition_from_cli(
            "s100-plus-17-50",
            ["target=100:1-2"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package_root = root / "package"
            member_root = root / "members"
            for bundle_root, surah, ayah in (
                (package_root, 100, 2),
                (member_root, 17, 50),
            ):
                source_path = (
                    bundle_root / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json"
                )
                source_path.parent.mkdir(parents=True)
                source_path.write_text(
                    json.dumps({
                        "bundle_type": "ayah",
                        "schema_version": "input-bundle-v4",
                        "unit_kind": "numbered_ayah",
                        "surah": surah,
                        "ayah": ayah,
                        "ayahRef": f"{surah}:{ayah}",
                        "surface_ref": f"{surah}:{ayah}",
                        "linguistic_source_ref": f"{surah}:{ayah}",
                        "text": {"arabic_uthmani": "text"},
                        "qac_morphemes": [{"qac_ref": f"{surah}:{ayah}:1:1"}],
                        "word_analysis": {"ref": f"{surah}:{ayah}", "words": []},
                        "coverage": {},
                    }),
                    encoding="utf-8",
                )
            with patch.object(
                workflow.compositions,
                "load_unit_bundle",
                wraps=workflow.compositions.load_unit_bundle,
            ) as load_bundle:
                projection = workflow._composition_projection(
                    analysis,
                    "100:1",
                    numbered_bundle("100:1"),
                    package_root,
                    member_root,
                )

        self.assertIsNotNone(projection)
        self.assertEqual(load_bundle.call_count, 2)
        for lane in workflow.LANES:
            packet = {
                "identity": {"ayah_ref": "100:1", "lane": lane, "lane_packet_sha256": "old"},
                "scope": {},
                "candidate_inventory": [],
                "support_registry": [],
            }
            augmented = workflow._augment_lane_packet(
                packet,
                layout=workflow.layout_for("100:1", analysis.analysis_id),
                composition=analysis,
                projection=projection,
                source_bundle={"unit_kind": "numbered_ayah"},
                prefatory_basmala_context=None,
                lane=lane,
            )
            external_refs = [
                unit["ayah_ref"]
                for unit in augmented["selected_context_units"]
                if unit.get("membership_added_ayah") is True
            ]
            self.assertEqual(external_refs, ["17:50"] if lane == "macro" else [])
            membership = augmented["scope"]["surah_membership"]
            self.assertEqual(
                membership["lane_context_refs"],
                ["17:50"] if lane == "macro" else [],
            )
            if lane == "macro":
                external = next(
                    candidate
                    for candidate in augmented["candidate_inventory"]
                    if candidate.get("source_local_id") == "17:50"
                )
                self.assertEqual(external["source_type"], "external_ayah_member")
                self.assertFalse(external["focus_eligible"])

    def test_added_ayah_conflict_between_roots_is_rejected(self) -> None:
        analysis = workflow.compositions.composition_from_cli(
            "s100-pericope-plus-17-50",
            ["target=100:1-2"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package_root = root / "package"
            member_root = root / "members"
            for index, bundle_root in enumerate((package_root, member_root)):
                source_path = bundle_root / "s017" / "17_50.ayah.json"
                source_path.parent.mkdir(parents=True, exist_ok=True)
                source_path.write_text(
                    json.dumps(
                        {
                            "bundle_type": "ayah",
                            "schema_version": "input-bundle-v4",
                            "unit_kind": "numbered_ayah",
                            "surah": 17,
                            "ayah": 50,
                            "ayahRef": "17:50",
                            "surface_ref": "17:50",
                            "linguistic_source_ref": "17:50",
                            "text": {"arabic_uthmani": f"text-{index}"},
                            "qac_morphemes": [{"qac_ref": "17:50:1:1"}],
                            "word_analysis": {"ref": "17:50", "words": []},
                            "coverage": {},
                        }
                    ),
                    encoding="utf-8",
                )
            with self.assertRaisesRegex(workflow.WorkflowError, "differs"):
                workflow._load_added_ayah_bundle(
                    package_root, member_root, "17:50"
                )

    def test_basmala_docket_uses_target_surface_and_1_1_linguistics(self) -> None:
        source_bundle = json.loads(
            (
                workflow.REPO_ROOT
                / "bundles"
                / "s001"
                / "1_1.ayah.json"
            ).read_text(encoding="utf-8")
        )
        source_bundle.update({
            "unit_kind": "prefatory_basmala",
            "surah": 100,
            "ayah": 0,
            "ayahRef": "100:0",
            "surface_ref": "100:0",
            "linguistic_source_ref": "1:1",
        })
        normalized_surface = workflow.compositions.normalize_arabic_surface(
            source_bundle["text"]["arabic_uthmani"]
        )
        source_bundle["coverage"]["basmala_alias"] = {
            "normalized_surface_equivalent": True,
            "target_normalized": normalized_surface,
            "source_normalized": normalized_surface,
        }
        template = json.loads(
            (
                workflow.V3_ROOT
                / "inputs"
                / "adjudication"
                / "s001"
                / "1_1.docket.json"
            ).read_text(encoding="utf-8")
        )

        docket = workflow._adapt_basmala_docket(source_bundle, template)

        self.assertEqual(docket["identity"]["ayah_ref"], "100:0")
        self.assertEqual(docket["focus"]["surface_ref"], "100:0")
        self.assertEqual(docket["focus"]["linguistic_source_ref"], "1:1")
        self.assertEqual(docket["scope"]["hft"]["status"], "not_applicable")
        self.assertTrue(docket["candidates"])
        self.assertTrue(
            all(candidate["ayah_ref"] == "100:0" for candidate in docket["candidates"])
        )
        self.assertTrue(
            all(
                row["qac_ref"].startswith("1:1:")
                for row in docket["focus"]["qac_morphemes"]
            )
        )

    def test_derived_docket_records_fixed_v3_projection_policy(self) -> None:
        docket = {"identity": {"docket_payload_sha256": "a" * 64}}
        with patch.object(
            workflow,
            "build_prepared_artifacts",
            return_value=({}, docket),
        ) as build:
            actual, lineage = workflow._derive_docket(
                workflow.REPO_ROOT / "bundle.json",
                b"{}",
                {},
            )

        self.assertIs(actual, docket)
        self.assertEqual(lineage["kind"], "derived_in_memory")
        self.assertEqual(lineage["prepare_options"]["hft_policy"], "quarantine")
        self.assertEqual(lineage["prepare_options"]["max_support_chars"], 8_000)
        self.assertEqual(
            build.call_args.kwargs["options"], workflow.V4_PREPARE_OPTIONS
        )


if __name__ == "__main__":
    unittest.main()
