from __future__ import annotations

import argparse
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
            "candidate_id": "focus-only",
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
    def test_only_prepare_is_exposed(self) -> None:
        parser = workflow._parser()
        subparsers = next(
            action
            for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)
        )
        self.assertEqual(set(subparsers.choices), {"prepare"})

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
            "candidate_id": "focus-only",
            "ayah_ref": "29:38",
        }])
        self.assertEqual(packet["selected_context_units"], [context])
        self.assertNotIn("source_coverage", packet)
        self.assertNotIn("contract", packet)
        self.assertNotIn("source_canonical_sha256", json.dumps(packet))


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
        self.assertTrue(candidate["adjudicable"])
        self.assertEqual(candidate["unresolved_branch_citations"], [])
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


if __name__ == "__main__":
    unittest.main()
