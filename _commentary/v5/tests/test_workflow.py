from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "workflow.py"
SPEC = importlib.util.spec_from_file_location("commentary_v5_workflow", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)


def numbered_bundle(ref: str, *, root: str = "ف ع ل") -> dict[str, object]:
    surah, ayah = (int(value) for value in ref.split(":"))
    return {
        "bundle_type": "ayah",
        "schema_version": "input-bundle-v4",
        "unit_kind": "numbered_ayah",
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": ref,
        "text": {"arabic_uthmani": f"text {ref}"},
        "qac_morphemes": [{
            "qac_ref": f"{ref}:1:1",
            "word_index": 1,
            "root_ar": root,
            "surface_ar": "فعل",
        }],
        "word_analysis": {"ref": ref, "words": []},
        "branch_inventories": {"full_context_packet": {"branch_inventories": []}},
        "root_lexicon": {},
        "coverage": {},
    }


def basmala_bundle(ref: str) -> dict[str, object]:
    surah = int(ref.split(":", 1)[0])
    bundle = numbered_bundle("1:1", root="س م و")
    bundle.update({
        "unit_kind": "prefatory_basmala",
        "surah": surah,
        "ayah": 0,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": "1:1",
        "text": {"arabic_uthmani": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"},
        "coverage": {
            "basmala_alias": {
                "normalized_surface_equivalent": True,
                "target_normalized": workflow.compositions.BASMALA_NORMALIZED_SURFACE,
                "source_normalized": workflow.compositions.BASMALA_NORMALIZED_SURFACE,
            }
        },
    })
    return bundle


def write_bundle(root: Path, bundle: dict[str, object]) -> Path:
    surah = int(bundle["surah"])
    path = root / f"s{surah:03d}" / f"{surah}_{bundle['ayah']}.ayah.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(bundle, ensure_ascii=False), encoding="utf-8")
    return path


def base_packet(lane: str) -> dict[str, object]:
    return {
        "schema_version": "commentary-v3-lane-evidence-packet-v2",
        "identity": {
            "ayah_ref": "29:38",
            "lane": lane,
            "source_canonical_sha256": "a" * 64,
            "lane_packet_sha256": "b" * 64,
        },
        "candidate_inventory": [{
            "candidate_id": f"{lane}-focus-only",
            "ayah_ref": "29:38",
        }],
        "support_registry": [],
        "branch_registry": [],
        "connection_registry": [],
        "source_coverage": {"source_sha256": "c" * 64},
        "contract": {"every_candidate_requires_one_decision": True},
    }


def write_tsv(path: Path, columns: tuple[str, ...], row: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\t".join(columns)
        + "\n"
        + "\t".join(row[column] for column in columns)
        + "\n",
        encoding="utf-8",
    )


class CliSurfaceTests(unittest.TestCase):
    def test_only_supported_prepare_commands_are_exposed(self) -> None:
        parser = workflow._parser()
        subparsers = next(
            action
            for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)
        )
        self.assertEqual(
            set(subparsers.choices),
            {"prepare", "prepare-middle", "prepare-invitation"},
        )

    def test_removed_post_launch_commands_are_rejected(self) -> None:
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit):
            workflow._parser().parse_args(["advance", "--ayah", "29:38"])
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit):
            workflow._parser().parse_args(["verify", "--ayah", "29:38"])

    def test_prefatory_policy_excludes_s1_and_s9(self) -> None:
        for ref in ("1:0", "9:0"):
            with self.subTest(ref=ref):
                with self.assertRaises(workflow.WorkflowError):
                    workflow.layout_for(ref)

    def test_batch_rejects_single_focus_input_overrides(self) -> None:
        args = workflow._parser().parse_args([
            "prepare",
            "--ayah",
            "29:38",
            "29:39",
            "--source-bundle",
            "one.ayah.json",
        ])
        with self.assertRaisesRegex(workflow.WorkflowError, "only be used for one"):
            workflow._resolve_request(args)

    def test_failed_batch_exposes_no_handoffs_at_any_level(self) -> None:
        args = argparse.Namespace()

        def fake_prepare(unit_args: argparse.Namespace) -> dict[str, object]:
            if unit_args.ayah == "1:2":
                raise workflow.WorkflowError("preflight failed")
            return {
                "ayah_ref": unit_args.ayah,
                "status": "prepared",
                "handoffs": [{"lane": "micro", "prompt": "prompt.md"}],
                "orchestration": {"scope_launch": "launch"},
                "generated_files": ["prompt.md"],
            }

        with patch.object(workflow, "prepare", side_effect=fake_prepare):
            result, failed = workflow._prepare_batch(
                args, ["1:1", "1:2"], None
            )

        self.assertTrue(failed)
        self.assertEqual(result["parallel_handoffs"], [])
        self.assertEqual(result["units"][0]["status"], "withheld_due_to_batch_error")
        for unit in result["units"]:
            self.assertNotIn("handoffs", unit)
            self.assertNotIn("orchestration", unit)
            self.assertNotIn("generated_files", unit)

    def test_output_root_itself_cannot_be_a_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            target = base / "target"
            target.mkdir()
            root = base / "root"
            root.symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(workflow.WorkflowError, "root is a symlink"):
                workflow._assert_confined(root / "unit" / "prompt.md", root)

    def test_record_line_json_is_valid_and_splits_registry_records(self) -> None:
        value = {"identity": {"lane": "micro"}, "records": [{"id": 1}, {"id": 2}]}
        rendered = workflow._record_line_json(value)
        self.assertEqual(json.loads(rendered), value)
        self.assertIn('\n{"id":1},\n{"id":2}\n', rendered)

    def test_canonical_template_restores_guidance_scope_and_ledger_inputs(self) -> None:
        template = (workflow.PROMPTS_ROOT / "canonical.md").read_text(
            encoding="utf-8"
        )
        markers = set(workflow.MARKER_RE.findall(template))
        self.assertEqual(
            markers,
            {
                "@@AYAH_REF@@",
                "@@PROSE_OUTPUT_PATH@@",
                "@@FOCUS_CONTEXT_BRIEF@@",
                "@@PRINCIPLES_MD@@",
                "@@COMMENTARY_SPEC_MD@@",
                "@@CHANNELS_MD@@",
                "@@CANONICAL_PROMPT_V2@@",
                "@@MICRO_SCOPE_PROSE@@",
                "@@MACRO_SCOPE_PROSE@@",
                "@@GLOBAL_SCOPE_PROSE@@",
                "@@MICRO_SCOPE_LEDGER@@",
                "@@MACRO_SCOPE_LEDGER@@",
                "@@GLOBAL_SCOPE_LEDGER@@",
            },
        )
        self.assertNotIn("_discovery_json>", template)

    def test_invitation_template_uses_editorial_prose_as_sole_source(self) -> None:
        template = (workflow.PROMPTS_ROOT / "invitation.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(
            set(workflow.MARKER_RE.findall(template)),
            {
                "@@AYAH_REF@@",
                "@@EDITORIAL_PROSE@@",
                "@@INVITATION_OUTPUT_PATH@@",
            },
        )
        self.assertIn("sole semantic source", template)
        self.assertIn("where any nonordinary detail comes from", template)
        self.assertIn("reference from the editorial prose", template)
        self.assertNotIn("@@MICRO_SCOPE_LEDGER@@", template)
        self.assertNotIn("@@CANONICAL_PROMPT_V2@@", template)

    def test_prepare_middle_embeds_only_final_editorial_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_root = root / "input"
            editorial_root = root / "editorial"
            middle_root = root / "middle"
            source = (
                editorial_root
                / "trial"
                / "s001"
                / "1_5"
                / "1_5.prose.editorial.tr.md"
            )
            source.parent.mkdir(parents=True)
            source.write_text(
                "Yolun nasıl işlendiğini açıklayan nihai metin.", encoding="utf-8"
            )
            with (
                patch.object(workflow, "INPUT_ROOT", input_root),
                patch.object(workflow, "EDITORIAL_ROOT", editorial_root),
                patch.object(workflow, "MIDDLE_ROOT", middle_root),
            ):
                result = workflow.prepare_middle_layer(
                    argparse.Namespace(ayah="1:5", analysis_id="trial")
                )
                prompt_path = Path(result["handoff"]["prompt"])
                prompt = prompt_path.read_text(encoding="utf-8")

        self.assertIn("Yolun nasıl işlendiğini açıklayan nihai metin.", prompt)
        normalized_prompt = " ".join(prompt.split())
        self.assertIn("mandatory diagnostic pass", normalized_prompt)
        self.assertIn("review triggers, not compression targets", normalized_prompt)
        self.assertNotIn(
            "Yolun nasıl işlendiğini açıklayan nihai metin.",
            result["handoff"]["launch_message"],
        )
        self.assertNotRegex(prompt, workflow.MARKER_RE)
        self.assertEqual(
            result["schema_version"], "commentary-v5-middle-prepared-v2"
        )
        self.assertEqual(result["handoff"]["role"], "middle_layer")
        self.assertEqual(result["handoff"]["model"], "gpt-5.6-luna")
        self.assertEqual(result["handoff"]["reasoning_effort"], "max")
        self.assertFalse(result["handoff"]["orchestrator_output_inspection"])
        self.assertFalse(result["handoff"]["retry"])
        self.assertEqual(result["handoff"]["prompt_delivery"], "workspace_path")
        self.assertEqual(
            result["handoff"]["follow_up_delivery"], "workspace_path"
        )
        self.assertIn(
            str(prompt_path.resolve(strict=False)),
            result["handoff"]["launch_message"],
        )
        self.assertNotIn("<source_prose>", result["handoff"]["launch_message"])
        self.assertLess(len(result["handoff"]["launch_message"]), 500)
        self.assertIn(
            "middle-layer-audit-followup.md",
            result["handoff"]["follow_up_message"],
        )
        self.assertEqual(len(result["generated_files"]), 1)
        self.assertTrue(result["handoff"]["prompt"].endswith(
            "input/trial/s001/1_5/middle-layer.prompt.md"
        ))
        self.assertTrue(result["handoff"]["prose_output"].endswith(
            "middle/trial/s001/1_5/1_5.prose.middle.tr.md"
        ))
        self.assertTrue(result["handoff"]["ledger_output"].endswith(
            "middle/trial/s001/1_5/1_5.middle.claims.json"
        ))

    def test_prepare_middle_requires_completed_editorial_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
                patch.object(workflow, "MIDDLE_ROOT", root / "middle"),
            ):
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "Cannot read final editorial prose"
                ):
                    workflow.prepare_middle_layer(
                        argparse.Namespace(ayah="1:5", analysis_id="trial")
                    )

    def test_middle_audit_followup_is_fixed_and_placeholder_free(self) -> None:
        followup = (
            workflow.PROMPTS_ROOT / "middle-layer-audit-followup.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(followup.split())

        self.assertNotRegex(followup, workflow.MARKER_RE)
        self.assertIn("Do not cap a source paragraph at one unit", normalized)
        self.assertIn("mandatory adversarial compression challenge", normalized)
        self.assertIn("diagnostic triggers only", normalized)
        self.assertIn(
            "Repair only the same reader-prose and claim-ledger outputs", normalized
        )

    def test_middle_orchestration_is_path_only_and_has_no_retry(self) -> None:
        runbook = (workflow.V5_ROOT / "ORCHESTRATION.md").read_text(
            encoding="utf-8"
        )
        section = runbook.split(
            "## 7. Post-Editorial Middle-Layer Consolidation", 1
        )[1].split("## 8. Reading Invitation", 1)[0]

        self.assertIn("handoff.launch_message", section)
        self.assertIn("handoff.follow_up_message", section)
        self.assertIn("Never open, copy, paste, quote, embed", section)
        self.assertIn("There is no retry, rerun, relaunch, resend", section)
        self.assertNotIn(
            "first message must be only the complete contents", section
        )

    def test_prepare_invitation_embeds_only_final_editorial_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_root = root / "input"
            editorial_root = root / "editorial"
            source = (
                editorial_root
                / "trial"
                / "s001"
                / "1_5"
                / "1_5.prose.editorial.tr.md"
            )
            source.parent.mkdir(parents=True)
            source.write_text("Yolun nasıl işlendiğini açıklayan nihai metin.", encoding="utf-8")
            with (
                patch.object(workflow, "INPUT_ROOT", input_root),
                patch.object(workflow, "EDITORIAL_ROOT", editorial_root),
            ):
                result = workflow.prepare_invitation(
                    argparse.Namespace(ayah="1:5", analysis_id="trial")
                )
                prompt = Path(result["handoff"]["prompt"]).read_text(encoding="utf-8")

        self.assertIn("Yolun nasıl işlendiğini açıklayan nihai metin.", prompt)
        self.assertNotIn("@@EDITORIAL_PROSE@@", prompt)
        self.assertEqual(result["handoff"]["role"], "invitation")
        self.assertEqual(result["handoff"]["model"], "gpt-5.6-luna")

    def test_prepare_invitation_requires_completed_editorial_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                with self.assertRaisesRegex(
                    workflow.WorkflowError, "Cannot read final editorial prose"
                ):
                    workflow.prepare_invitation(
                        argparse.Namespace(ayah="1:5", analysis_id="trial")
                    )


class ContextEvidenceTests(unittest.TestCase):
    def test_external_overlay_procedure_is_macro_only(self) -> None:
        packet = {
            "analysis_context": {
                "external_ayat_refs": ["1:2", "1:3", "1:4", "1:5", "1:6", "1:7"]
            }
        }

        macro = workflow._lane_specific_procedure("macro", packet)
        micro = workflow._lane_specific_procedure("micro", packet)
        global_ = workflow._lane_specific_procedure("global", packet)

        self.assertIn("Phase 1", macro)
        self.assertIn("Phase 2", macro)
        self.assertIn("1:6", macro)
        self.assertIn("individually listed ayat", macro)
        self.assertIn("not as an implicit whole-surah reading", macro)
        self.assertEqual(micro, "- No additional lane-specific procedure.")
        self.assertEqual(global_, "- No additional lane-specific procedure.")

    def test_macro_without_external_ayat_has_no_overlay_phase(self) -> None:
        procedure = workflow._lane_specific_procedure(
            "macro",
            {"analysis_context": {"external_ayat_refs": []}},
        )

        self.assertIn("no explicitly added external ayat", procedure)
        self.assertNotIn("Phase 1", procedure)

    def test_ordered_external_and_basmala_members_are_evidence_not_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            focus = numbered_bundle("29:38", root="ر ج ف")
            write_bundle(root, numbered_bundle("29:41", root="ع ي ن"))
            write_bundle(root, numbered_bundle("1:1", root="س م و"))
            write_bundle(root, basmala_bundle("29:0"))
            composition = workflow.compositions.composition_from_cli(
                "s29-context",
                ["host=29:0,29:38,29:41"],
                ["29:38"],
                member_surah=29,
                added_ayat_selectors=["1:1"],
            )

            by_lane = workflow._composition_context(
                composition, "29:38", focus, root, root
            )

        refs = [unit["ayah_ref"] for unit in by_lane["macro"]]
        self.assertEqual(refs, ["29:0", "29:41", "1:1"])
        self.assertEqual(by_lane["global"], [])
        for unit in by_lane["macro"]:
            self.assertFalse(unit["focus_eligible"])
            self.assertNotIn("candidate_id", unit)
            self.assertNotIn("support_ids", unit)
            self.assertEqual(
                set(unit["evidence"]),
                {"protocol", "context_order", "context_ayat", "context_root_cues"},
            )
        external = by_lane["macro"][-1]
        self.assertEqual(external["context_kind"], "external_ayah_member")
        self.assertEqual(external["membership_target_surah"], 29)

    def test_automatic_basmala_uses_ordinary_context_shape(self) -> None:
        focus = numbered_bundle("29:38")
        ordinary = workflow.compositions.project_context_unit(
            context_row={"ref": "29:41", "lane": "macro"},
            bundle=numbered_bundle("29:41"),
            focus_bundle=focus,
        )
        basmala = basmala_bundle("29:0")
        identity = workflow.compositions.validate_unit_bundle(
            basmala, expected_ref="29:0"
        )
        units: list[dict[str, object]] = []

        workflow._append_host_basmala(
            units,
            focus_bundle=focus,
            basmala=(Path("29_0.ayah.json"), basmala, identity),
        )

        self.assertEqual(set(units[0]["evidence"]), set(ordinary["evidence"]))
        self.assertEqual(units[0]["context_kind"], "host_prefatory_basmala")
        self.assertTrue(units[0]["automatic_prefatory_basmala_membership"])
        self.assertNotIn("candidate_id", units[0])

    def test_s1_and_s9_do_not_attempt_to_load_a_prefatory_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.assertIsNone(
                workflow._required_host_basmala(
                    numbered_bundle("1:1"), root, None
                )
            )
            self.assertIsNone(
                workflow._required_host_basmala(
                    numbered_bundle("9:1"), root, None
                )
            )

    def test_added_ayah_disagreement_between_roots_fails_preflight(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "package"
            members = root / "members"
            write_bundle(package, numbered_bundle("1:1", root="س م و"))
            write_bundle(members, numbered_bundle("1:1", root="و س م"))
            with self.assertRaisesRegex(workflow.WorkflowError, "differs"):
                workflow._load_added_ayah_bundle(package, members, "1:1")

    def test_context_does_not_expand_focus_candidate_inventory(self) -> None:
        focus = numbered_bundle("29:38")
        context = workflow.compositions.project_context_unit(
            context_row={"ref": "29:41", "lane": "macro"},
            bundle=numbered_bundle("29:41"),
            focus_bundle=focus,
        )
        with patch.object(workflow.v3, "_lane_packet", return_value=base_packet("macro")):
            packet = workflow._build_lane_packet(
                lane="macro",
                docket={},
                source_bundle=focus,
                hft_projection={},
                inter_rows=[],
                reciprocal={},
                inter_coverage={},
                quran_evidence={},
                quran_coverage={},
                composition=None,
                context_by_lane={"micro": [], "macro": [context], "global": []},
                host_basmala=None,
            )

        self.assertEqual(packet["candidate_inventory"], [{
            "candidate_id": "macro-focus-only",
            "ayah_ref": "29:38",
        }])
        self.assertEqual(packet["selected_context_units"], [context])
        self.assertNotIn("source_coverage", packet)
        self.assertNotIn("contract", packet)
        self.assertNotIn("source_canonical_sha256", json.dumps(packet))


class PacketNormalizationTests(unittest.TestCase):
    def _packets(self) -> dict[str, dict[str, object]]:
        packets: dict[str, dict[str, object]] = {}
        for lane in workflow.LANES:
            packet = base_packet(lane)
            packet["candidate_inventory"] = []
            packet["scope"] = {
                "pericope": {
                    "refs": ["29:38", "29:39", "29:40", "29:41"]
                }
            }
            packet["selected_context_units"] = []
            packets[lane] = packet
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "next-ayah",
            "lane": "micro",
            "source_type": "word_analysis",
            "source_local_id": "29:38:22:next-ayah",
            "anchor_refs": ["29:38:22"],
            "branch_refs": [],
            "root_ids": [],
            "support_ids": ["support-next"],
        }]
        packets["micro"]["support_registry"] = [{
            "support_id": "support-next",
            "source_type": "word_analysis",
            "role": "candidate_evidence",
            "scope": "micro",
            "text": json.dumps({
                "headline": "next-ayah echo",
                "reason": "The same construction appears in 29:39.",
                "prose": "The pattern reaches 29:39.",
                "root_display": "{{ar:ك و ن}} ({{tr:k-w-n}})",
            }, ensure_ascii=False),
        }]
        packets["micro"]["branch_registry"] = [{
            "branch_ref": "root_000001/B001",
            "registry": "focus",
            "root_id": "root_000001",
            "root_ar": "ك و ن",
            "gloss": "being",
            "review_facets": [{"facet_id": "F001", "statements": {"statement": "existence"}}],
            "candidate_links": [],
            "support_links": [],
            "hft_citations": [],
        }]
        packets["macro"]["connection_registry"] = [{
            "connection_ref": "connection-29-41",
            "target_ref": "29:41",
            "source_target_components": ["29:41"],
        }]
        packets["global"]["connection_registry"] = [{
            "connection_ref": "connection-44-32",
            "target_ref": "44:32",
            "source_target_components": ["44:32"],
        }]
        return packets

    def test_packet_contract_fields_and_native_pericope_routing(self) -> None:
        packets = self._packets()

        workflow._normalize_and_route_lane_packets(
            packets, numbered_bundle("29:38"), None
        )

        candidate = packets["macro"]["candidate_inventory"][0]
        self.assertEqual(candidate["candidate_id"], "next-ayah")
        self.assertEqual(candidate["root_ids"], ["root_000001"])
        self.assertEqual(
            candidate["root_branch_options"], ["root_000001/B001"]
        )
        self.assertEqual(candidate["required_context_refs"], ["29:39"])
        self.assertTrue(candidate["semantic_obligations"])
        self.assertEqual(
            packets["macro"]["support_registry"][0]["support_id"],
            "support-next",
        )
        self.assertEqual(packets["micro"]["candidate_inventory"], [])

    def test_declared_composition_routes_all_evidence_with_one_map(self) -> None:
        packets = self._packets()
        composition = workflow.compositions.composition_from_cli(
            "routing-test",
            ["focus=29:38,29:39", "later=29:41"],
            ["29:38"],
            member_surah=29,
            added_ayat_selectors=["44:32"],
        )

        workflow._normalize_and_route_lane_packets(
            packets, numbered_bundle("29:38"), composition
        )

        macro_connections = {
            row["connection_ref"]
            for row in packets["macro"]["connection_registry"]
        }
        global_connections = {
            row["connection_ref"]
            for row in packets["global"]["connection_registry"]
        }
        self.assertEqual(macro_connections, {"connection-44-32"})
        self.assertEqual(global_connections, {"connection-29-41"})
        candidate = packets["macro"]["candidate_inventory"][0]
        self.assertEqual(
            candidate["v5_routing"]["basis"], "declared_composition"
        )

    def test_ambiguous_branches_remain_an_explicit_alternative_group(self) -> None:
        candidate = {
            "unresolved_branch_citations": [{
                "citation": "ش ي ء/B001",
                "reason": (
                    "ambiguous root mapping expanded as alternatives: "
                    "root_000831/B001, root_000832/B001"
                ),
            }]
        }
        branches = {
            ref: {"branch_ref": ref}
            for ref in ("root_000831/B001", "root_000832/B001")
        }

        self.assertEqual(
            workflow._candidate_branch_alternatives(candidate, branches),
            [{
                "citation": "ش ي ء/B001",
                "branch_options": ["root_000831/B001", "root_000832/B001"],
                "status": "alternatives_not_established",
            }],
        )

    def test_packet_finalization_does_not_remove_evidence(self) -> None:
        packet = {
            "branch_registry": [{
                "branch_ref": "root_000001/B001",
                "semantic_detail": {
                    "neighbor_distinctions": [{"gloss": "distinct detail"}],
                },
                "root_occurrence_qualification": "bounded qualification",
            }],
            "connection_registry": [{
                "connection_ref": "connection-1",
                "qualification": {"review_boundary": "full detail"},
                "reciprocal_evidence": [{"source_note": "counter-reading"}],
            }],
            "review_inventory": {"candidate_ids": ["candidate-1"]},
            "hft_evidence": {"assigned_records": [{"hft_ref": "hft-1"}]},
        }
        original = json.loads(json.dumps(packet))

        workflow._finalize_lane_packet_contract(packet)

        for key, value in original.items():
            self.assertEqual(packet[key], value)
        self.assertTrue(
            packet["evidence_contract"]["evidence_records_are_lossless"]
        )


class CompactPacketTests(unittest.TestCase):
    def test_governing_documents_match_the_early_v5_snapshot(self) -> None:
        expected = {
            "principles": "fe4c0397d275a0201b8803782011ab9281392c2f76dc5e7584e1bec827c0c62c",
            "commentary_spec": "ff755d734ed019afe0217c8564538ac26cec8b42941cee78492e7a7a19ab6614",
            "channels": "bdb3a2efbc5e1352e1e995ea1e9ab28f8a4bb81d0cf5a758f4b42bf9bd8f89a6",
            "canonical_prompt_v2": "a6e17213aed8ed538cc1ca2cfa957bfbc4617991df4da6df87bce7f09323468d",
        }
        self.assertEqual({key: hashlib.sha256(text.encode()).hexdigest()
                          for key, text in workflow._canonical_inputs().items()}, expected)

    def test_root_repair_preserves_original_topic_ownership_and_evidence(self) -> None:
        packets = PacketNormalizationTests()._packets()
        before = copy.deepcopy(packets)
        workflow._finalize_compact_lane_packets(packets, numbered_bundle("29:38"))
        before["micro"]["candidate_inventory"][0]["root_ids"] = ["root_000001"]
        self.assertEqual(packets, before)
        self.assertEqual(packets["macro"]["candidate_inventory"], [])

    def test_unresolved_hft_branch_is_qualified_for_attributed_activation(self) -> None:
        packets = PacketNormalizationTests()._packets()
        branch = packets["micro"]["branch_registry"][0]
        branch.update({
            "registry": "unresolved",
            "root_ar": None,
            "gloss": None,
            "branch_kind": None,
            "hft_citations": [{
                "source_ref": "29:39",
                "source_word_indices": ["1"],
                "root": "ك و ن",
                "role": "attributed context role",
                "qualification": "old qualification",
            }],
        })

        workflow._finalize_compact_lane_packets(
            packets, numbered_bundle("29:38")
        )

        self.assertIn("may support an attributed contextual activation", branch["boundary"])
        self.assertIn("returns to the focus", branch["root_occurrence_qualification"])
        self.assertIn("not verified lexicon evidence", branch["hft_citations"][0]["qualification"])

    def test_complete_topic_delivery_is_checked_without_rerouting(self) -> None:
        bundle = numbered_bundle("29:38")
        bundle["coverage"] = {"word_morpheme_spans": {
            "alignment_version": "qac-analysis-bridge-v1"}}
        bundle["word_analysis"]["words"] = [{"topics": [
            {"topic_id": "29:38:22:next-ayah"},
            {"topic_id": "29:38:23:inverse-rare-echo"},
        ]}]
        packets = PacketNormalizationTests()._packets()
        with self.assertRaisesRegex(workflow.WorkflowError, "inverse-rare-echo"):
            workflow._finalize_compact_lane_packets(packets, bundle)

    def test_duplicate_candidate_identity_is_rejected(self) -> None:
        packets = PacketNormalizationTests()._packets()
        packets["macro"]["candidate_inventory"] = copy.deepcopy(
            packets["micro"]["candidate_inventory"])
        with self.assertRaisesRegex(workflow.WorkflowError, "more than one source lane"):
            workflow._finalize_compact_lane_packets(packets, numbered_bundle("29:38"))

    def test_conflicting_shared_source_evidence_is_still_rejected(self) -> None:
        for field, error in (("support_registry", "Support ID differs"),
                             ("branch_registry", "Branch semantics differ")):
            with self.subTest(field=field):
                packets = PacketNormalizationTests()._packets()
                packets["macro"][field] = copy.deepcopy(packets["micro"][field])
                packets["macro"][field][0]["text"] = "contradictory source detail"
                with self.assertRaisesRegex(workflow.WorkflowError, error):
                    workflow._finalize_compact_lane_packets(packets, numbered_bundle("29:38"))


class ReciprocalInputTests(unittest.TestCase):
    def test_only_selected_static_document_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "focus_29_38_cutoff_100.tsv"
            row = {
                "record_type": "directional_review",
                "focus_ref": "29:38",
                "target_ref": "29:41",
                "focus_direction_label": "strong",
                "source_direction_label": "strong",
                "source_focus_ref": "29:38",
                "source_target_ref": "29:41",
                "source_target_component_ref": "29:41",
                "relation_scope": "same_surah",
                "source_column_order": "label_target_note",
                "source_row_role": "ranked_review",
                "source_note": "bounded note",
                "source_file": "focus_29_38_cutoff_100.tsv",
                "source_line": "2",
                "source_row_sha256": "a" * 64,
            }
            write_tsv(path, workflow.INTER_AYAH_NUMBERED_COLUMNS, row)
            quran = {
                ref: {"ayah_ref": ref, "arabic_uthmani": ref}
                for ref in ("29:38", "29:41")
            }

            rows, reciprocal, coverage = workflow._load_inter_ayah_projection(
                "29:38", root, root / "directional", quran
            )

        self.assertEqual([item["ref"] for item in rows], ["29:41"])
        self.assertEqual(reciprocal, {})
        self.assertEqual(coverage["directional_review_row_count"], 1)
        self.assertNotIn("manifest", coverage)

    def test_selected_document_focus_mismatch_fails_preflight(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "focus_29_38_cutoff_100.tsv"
            fields = [""] * len(workflow.INTER_AYAH_NUMBERED_COLUMNS)
            fields[workflow.INTER_AYAH_NUMBERED_COLUMNS.index("focus_ref")] = "29:39"
            path.write_text(
                "\t".join(workflow.INTER_AYAH_NUMBERED_COLUMNS)
                + "\n"
                + "\t".join(fields)
                + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "Malformed"):
                workflow._load_inter_ayah_projection(
                    "29:38", root, root, {"29:38": {}, "29:41": {}}
                )

    def test_selected_document_rejects_incoherent_source_provenance(self) -> None:
        base = {
            "record_type": "directional_review",
            "focus_ref": "29:38",
            "target_ref": "29:41",
            "focus_direction_label": "strong",
            "source_direction_label": "strong",
            "source_focus_ref": "29:38",
            "source_target_ref": "29:41",
            "source_target_component_ref": "29:41",
            "relation_scope": "same_surah",
            "source_column_order": "label_target_note",
            "source_row_role": "ranked_review",
            "source_note": "bounded note",
            "source_file": "focus_29_38_cutoff_100.tsv",
            "source_line": "2",
            "source_row_sha256": "a" * 64,
        }
        quran = {"29:38": {}, "29:41": {}}
        for field, value in (
            ("source_focus_ref", "29:39"),
            ("source_row_sha256", "not-a-hash"),
            ("source_column_order", "unknown"),
            ("source_row_role", "missing_ayah_suggestion"),
            ("relation_scope", "cross_surah"),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                row = {**base, field: value}
                write_tsv(
                    root / "focus_29_38_cutoff_100.tsv",
                    workflow.INTER_AYAH_NUMBERED_COLUMNS,
                    row,
                )
                with self.assertRaises(workflow.WorkflowError):
                    workflow._load_inter_ayah_projection(
                        "29:38", root, root, quran
                    )

    def test_prefatory_directional_alias_must_come_from_1_1(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            row = {
                "record_type": "surface_alias_directional_evidence",
                "focus_ref": "29:0",
                "target_ref": "29:41",
                "focus_direction_label": "",
                "source_direction_label": "strong",
                "source_focus_ref": "29:38",
                "source_target_ref": "29:41",
                "source_target_component_ref": "29:41",
                "relation_scope": "same_surah",
                "source_column_order": "label_target_note",
                "source_row_role": "ranked_review",
                "source_note": "not a basmala source row",
                "source_file": "focus_29_38_cutoff_100.tsv",
                "source_line": "2",
                "source_row_sha256": "a" * 64,
                "source_record_type": "directional_review",
                "linguistic_source_ref": "1:1",
                "projection_basis": workflow.INTER_AYAH_PREFATORY_PROJECTION_BASIS,
                "source_relation_scope": "same_surah",
                "host_authored": "false",
            }
            write_tsv(
                root / "prefatory" / "focus_29_0_cutoff_100.tsv",
                workflow.INTER_AYAH_PREFATORY_COLUMNS,
                row,
            )
            quran = {"1:1": {}, "29:38": {}, "29:41": {}}

            with self.assertRaisesRegex(workflow.WorkflowError, "prefatory"):
                workflow._load_inter_ayah_projection(
                    "29:0", root, root, quran
                )

    def test_prefatory_self_reiteration_is_not_reciprocal_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            row = {
                "record_type": "surface_alias_self_reiteration",
                "focus_ref": "29:0",
                "target_ref": "1:1",
                "focus_direction_label": "",
                "source_direction_label": "strong",
                "source_focus_ref": "1:1",
                "source_target_ref": "1:1",
                "source_target_component_ref": "1:1",
                "relation_scope": "cross_surah",
                "source_column_order": "label_target_note",
                "source_row_role": "ranked_review",
                "source_note": "self emphasis",
                "source_file": "focus_1_1_cutoff_100.tsv",
                "source_line": "2",
                "source_row_sha256": "a" * 64,
                "source_record_type": "self_reiteration",
                "linguistic_source_ref": "1:1",
                "projection_basis": workflow.INTER_AYAH_PREFATORY_PROJECTION_BASIS,
                "source_relation_scope": "same_surah",
                "host_authored": "false",
            }
            write_tsv(
                root / "prefatory" / "focus_29_0_cutoff_100.tsv",
                workflow.INTER_AYAH_PREFATORY_COLUMNS,
                row,
            )

            rows, reciprocal, coverage = workflow._load_inter_ayah_projection(
                "29:0", root, root, {"1:1": {}}
            )

        self.assertEqual(rows, [])
        self.assertEqual(reciprocal, {})
        self.assertEqual(coverage["self_reiteration_row_count"], 1)


class V3PreparationCompatibilityTests(unittest.TestCase):
    def test_v5_budget_accepts_lossless_long_ayah_dockets(self) -> None:
        self.assertGreaterEqual(workflow.PREPARE_OPTIONS.max_docket_bytes, 1_300_000)

    def test_real_s87_1_retains_problematic_channel_evidence(self) -> None:
        path = workflow.REPO_ROOT / "bundles" / "s087" / "87_1.ayah.json"
        bundle = json.loads(path.read_text(encoding="utf-8"))

        prepared, docket = workflow.build_prepared_artifacts(
            bundle,
            source_path=path,
            options=workflow.PREPARE_OPTIONS,
        )

        candidate = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "channel"
            and item["title"] == "Origination and State-Making"
        )
        self.assertTrue(prepared["mandatory_candidates_ready"])
        self.assertFalse(candidate["adjudicable"])
        self.assertFalse(candidate["mandatory"])
        self.assertEqual(
            candidate["unresolved_branch_citations"],
            [
                {
                    "citation": "ش ي ء/B001",
                    "reason": (
                        "ambiguous root mapping expanded as alternatives: "
                        "root_000831/B001, root_000832/B001"
                    ),
                }
            ],
        )
        self.assertTrue(
            {
                "root_000831/B001",
                "root_000832/B001",
            }.issubset(candidate["branch_refs"])
        )
        unresolved = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "channel"
            and item["title"] == "Smooth Surface, Worn Fabric, and Damp Folding"
        )
        self.assertFalse(unresolved["mandatory"])
        self.assertEqual(
            unresolved["unresolved_branch_citations"],
            [
                {
                    "citation": "ب ل ل/B007",
                    "reason": "no registered branch match",
                }
            ],
        )


class PrepareTests(unittest.TestCase):
    def _args(self, root: Path) -> argparse.Namespace:
        return argparse.Namespace(
            ayah="1:1",
            analysis_id="native",
            composition=None,
            source_bundle=None,
            docket=None,
            context_bundles_dir=root,
            member_bundles_dir=root,
            quran_text=root / "quran.tsv",
            inter_ayah_dir=root / "reciprocal",
            inter_ayah_parent_dir=root / "directional",
        )

    def _patch_preflight(self):
        focus = numbered_bundle("1:1")
        docket = {"identity": {"ayah_ref": "1:1"}}
        quran = {"1:1": {"ayah_ref": "1:1", "arabic_uthmani": "text"}}
        return (
            patch.object(workflow, "_load_focus_inputs", return_value=(focus, docket)),
            patch.object(workflow, "_quran_text_projection", return_value=(quran, {})),
            patch.object(
                workflow,
                "_load_inter_ayah_projection",
                return_value=([], {}, {}),
            ),
            patch.object(workflow.v3, "_hft_authoring_projection", return_value={}),
            patch.object(
                workflow.v3,
                "_lane_packet",
                side_effect=lambda _d, lane, *_rest: base_packet(lane),
            ),
        )

    def test_prepare_writes_exactly_three_prompts_and_no_state_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_root = root / "input"
            raw_root = root / "raw"
            editorial_root = root / "editorial"
            patches = self._patch_preflight()
            with (
                patch.object(workflow, "INPUT_ROOT", input_root),
                patch.object(workflow, "RAW_ROOT", raw_root),
                patch.object(workflow, "EDITORIAL_ROOT", editorial_root),
                patch.object(workflow, "_required_host_basmala", return_value=None),
                patches[0], patches[1], patches[2], patches[3], patches[4],
            ):
                result = workflow.prepare(self._args(root))

            generated = sorted(path.name for path in input_root.rglob("*") if path.is_file())

        self.assertEqual(generated, [
            "global.discovery.prompt.md",
            "macro.discovery.prompt.md",
            "micro.discovery.prompt.md",
        ])
        self.assertEqual(len(result["handoffs"]), 3)
        for handoff in result["handoffs"]:
            lane = handoff["lane"]
            self.assertTrue(handoff["prompt"].endswith(f"{lane}.discovery.prompt.md"))
            self.assertTrue(
                handoff["discovery_output"].endswith(f"{lane}.discovery.json")
            )
            self.assertTrue(
                handoff["scope_prose_output"].endswith(f"{lane}.scope.tr.md")
            )
            self.assertTrue(
                handoff["scope_ledger_output"].endswith(
                    f"{lane}.scope.ledger.json"
                )
            )
            self.assertTrue(handoff["composition_template"].endswith("composition.md"))
        self.assertEqual(result["orchestration"]["post_launch_gates"], [])
        self.assertEqual(
            result["focus_context_brief"]["automatic_host_basmala_ref"], None
        )
        for forbidden in (
            "manifest.json",
            "source.bundle.json",
            "docket.json",
            "packet.json",
            "analysis.json",
        ):
            self.assertNotIn(forbidden, "\n".join(result["generated_files"]))

    def test_preflight_error_occurs_before_any_prompt_is_written(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_root = root / "input"
            patches = self._patch_preflight()
            with (
                patch.object(workflow, "INPUT_ROOT", input_root),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
                patches[0], patches[1],
                patch.object(
                    workflow,
                    "_load_inter_ayah_projection",
                    side_effect=workflow.WorkflowError("bad selected TSV"),
                ),
            ):
                with self.assertRaisesRegex(workflow.WorkflowError, "bad selected TSV"):
                    workflow.prepare(self._args(root))

            self.assertFalse(input_root.exists())

    def test_existing_agent_outputs_are_not_read_or_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_root = root / "input"
            raw_root = root / "raw"
            editorial_root = root / "editorial"
            old_raw = raw_root / "native" / "s001" / "1_1" / "agent.prose.md"
            old_editorial = (
                editorial_root / "native" / "s001" / "1_1" / "1_1.prose.editorial.tr.md"
            )
            old_raw.parent.mkdir(parents=True)
            old_editorial.parent.mkdir(parents=True)
            old_raw.write_text("scope prose", encoding="utf-8")
            old_editorial.write_text("editorial prose", encoding="utf-8")
            patches = self._patch_preflight()
            with (
                patch.object(workflow, "INPUT_ROOT", input_root),
                patch.object(workflow, "RAW_ROOT", raw_root),
                patch.object(workflow, "EDITORIAL_ROOT", editorial_root),
                patch.object(workflow, "_required_host_basmala", return_value=None),
                patches[0], patches[1], patches[2], patches[3], patches[4],
            ):
                workflow.prepare(self._args(root))

            self.assertEqual(old_raw.read_text(encoding="utf-8"), "scope prose")
            self.assertEqual(
                old_editorial.read_text(encoding="utf-8"), "editorial prose"
            )

    def test_compact_prepare_never_adds_bulk_context_or_reroutes_candidates(self) -> None:
        for check_only in (False, True):
            with self.subTest(check_only=check_only), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                args = self._args(root)
                args.check_only = check_only
                patches = self._patch_preflight()
                packets = {}
                render = workflow._build_scope_prompt

                def capture(layout, lane, packet):
                    prompt = render(layout, lane, packet)
                    packets[lane] = json.loads(prompt.split(
                        "<lane_packet_json>\n", 1)[1].split("\n</lane_packet_json>", 1)[0])
                    self.assertIn('"commentary-v5-scope-discovery-v1"', prompt)
                    for guidance in workflow._canonical_inputs().values():
                        self.assertIn(guidance, prompt)
                    return prompt

                def lane_packet(**kwargs):
                    lane = kwargs["lane"]
                    return {**base_packet(lane), "connection_registry": [{
                        "connection_ref": lane + "-target", "target_ref": "7:201", "qualification": {},
                    }]}
                with (
                    patch.object(workflow, "INPUT_ROOT", root / "input"),
                    patch.object(workflow, "RAW_ROOT", root / "raw"),
                    patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
                    patch.object(workflow, "_required_host_basmala", return_value=None),
                    patch.object(workflow, "_build_lane_packet", side_effect=lane_packet),
                    patch.object(workflow, "_build_scope_prompt", side_effect=capture),
                    patch.object(workflow, "_normalize_and_route_lane_packets",
                                 side_effect=AssertionError("expanded routing used")),
                    patch.object(workflow.packet_evidence, "attach_context_evidence",
                                 side_effect=AssertionError("bulk context added")),
                    patches[0], patches[1], patches[2], patches[3],
                ):
                    result = workflow.prepare(args)
                self.assertEqual(result["agent_input_contract"], "early-v5-compact")
                self.assertEqual(result["context_morphology_status"], "not_requested")
                self.assertEqual(result["missing_context_morphology_refs"], [])
                self.assertEqual((root / "input").exists(), not check_only)
                for lane, packet in packets.items():
                    self.assertEqual(packet["candidate_inventory"],
                                     base_packet(lane)["candidate_inventory"])
                    self.assertNotIn("context_evidence", packet)
                    self.assertNotIn("review_inventory", packet)


if __name__ == "__main__":
    unittest.main()
