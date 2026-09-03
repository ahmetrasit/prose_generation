from __future__ import annotations

import copy
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


def context_branch_bundle(
    ref: str, branch_ref: str = "root_001054/B001"
) -> dict[str, object]:
    root_id = branch_ref.split("/", 1)[0]
    bundle = numbered_bundle(ref)
    bundle["qac_morphemes"][0].update({
        "qac_word_ref": f"{ref}:1",
        "root_ar": "x y z",
    })
    bundle["root_lexicon"] = {
        root_id: {
            "root_id": root_id,
            "root_ar": "x y z",
            "qac_roots_ar": ["x y z"],
            "dictionary_entry": {
                "branches": [{
                    "branch_ref": branch_ref,
                    "concept_gloss": {"text": "web-weaving context"},
                    "concept_map": {
                        "definition": "A concrete contextual image.",
                        "facets": [{
                            "facet_id": "F001",
                            "role": "core",
                            "statement": "The context supplies a concrete web image.",
                        }],
                    },
                    "identity_judgment": {
                        "status": "accepted",
                        "boundary_note": "It remains a context image.",
                    },
                    "lexicalization_scope": {
                        "branch_kind": "mixed_non_bare"
                    },
                }]
            },
        }
    }
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
        candidates.append({
            "candidate_id": candidate_id,
            "anchor_refs": [ref],
            "support_ids": [support_id],
            "branch_refs": [],
            "branch_context_refs": {},
            "required_context_refs": [],
            "trust": "trusted",
        })
        supports.append({
            "support_id": support_id,
            "trust": "trusted",
            "quran_refs": [ref],
            "context_refs": [],
        })
    return {
        "schema_version": workflow.LANE_PACKET_SCHEMA_VERSION,
        "identity": {
            "ayah_ref": ref,
            "lane": lane,
            "lane_packet_sha256": packet_hash,
        },
        "contract": {
            "candidate_context_refs_are_exact": True,
            "support_quran_refs_are_structured": True,
            "accepted_candidates_require_dedicated_findings": True,
            "independent_discovery_audit_is_required": True,
        },
        "focus_surface_evidence": {
            "arabic_uthmani": "text",
            "word_analysis_refs": [f"{ref}:1"],
            "qac_morphemes": [{
                "qac_ref": f"{ref}:1:1",
                "qac_word_ref": f"{ref}:1",
            }],
        },
        "candidate_inventory": candidates,
        "support_registry": supports,
        "branch_registry": [],
        "connection_registry": [],
        "auxiliary_context_sources": [],
        "review_inventory": {
            "surface_refs": [f"{ref}:1"],
            "context_refs": [],
            "support_ids": [support_id] if candidate_id is not None else [],
            "connection_refs": [],
            "connection_evidence_refs": {},
            "branch_facets": [],
        },
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
    if candidate_id is not None:
        finding_ref = f"{lane}:finding"
        prose_statement = {
            "micro": "Yerel bulgu, ayetin soz diziminde sinanabilir bir hareket kurar.",
            "macro": "Baglamsal bulgu, yakin ayetlerle sinanabilir bir hareket kurar.",
            "global": "Genis bulgu, uzak baglantiyla sinanabilir bir hareket kurar.",
        }[lane]
        decisions.append({
            "candidate_id": candidate_id,
            "decision": "accept",
            "reason": "The packet supplies a bounded mechanism.",
            "finding_refs": [finding_ref],
            "branch_exclusions": [],
            "context_exclusions": [],
        })
        findings.append({
            "finding_ref": finding_ref,
            "origin_candidate_id": candidate_id,
            "represented_candidate_ids": [],
            "title": "Finding",
            "claim": "Bounded claim",
            "mechanism": "Concrete mechanism",
            "reader_payoff": "Concrete payoff",
            "containment": "Bounded to the cited evidence",
            "prose_statement": prose_statement,
            "epistemic": {
                "status": "grounded",
                "source_trust": ["trusted"],
                "reason": "The cited packet evidence is directly bound.",
            },
            "draft_prose": prose_statement,
            "support_ids": [support_id],
            "branch_activations": [],
            "connection_refs": [],
            "context_refs": [],
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
        "discovery_audit": {
            "reviewed_surface_refs": [f"{ref}:1"],
            "reviewed_context_refs": [],
            "reviewed_support_ids": (
                [support_id] if candidate_id is not None else []
            ),
            "discovered_finding_refs": [],
            "branch_dispositions": [],
            "connection_dispositions": [],
        },
        "candidate_decisions": decisions,
        "findings": findings,
        "friction_notes": [],
    }


def add_focus_branch(
    packet: dict[str, object],
    contribution: dict[str, object],
    *,
    branch_ref: str = "root_000001/B001",
) -> None:
    ref = packet["identity"]["ayah_ref"]
    lane = packet["identity"]["lane"]
    finding = contribution["findings"][0]
    candidate = packet["candidate_inventory"][0]
    facet_statement = "Tekrarlanan kullanim yolu islek hale getirir."
    branch_gloss = "islek yol"
    prose_statement = (
        "Eylem anlami acik yol sozuyle bulusunca islek yol anlami etkinlesir."
    )
    branch = {
        "branch_ref": branch_ref,
        "registry": "focus",
        "root_id": branch_ref.split("/", 1)[0],
        "root_ar": "x y z",
        "lexicon_identity_status": "accepted",
        "branch_kind": "mixed_non_bare",
        "gloss": branch_gloss,
        "boundary": "Yol, eylemin sozluk karsiligi degildir.",
        "review_facets": [{
            "facet_id": "F001",
            "role": "core",
            "statements": {"statement": facet_statement},
        }],
        "focus_root_occurrences": [{
            "qac_ref": f"{ref}:1:1",
            "qac_word_ref": f"{ref}:1",
        }],
    }
    packet["branch_registry"] = [branch]
    packet["focus_surface_evidence"]["word_analysis_refs"].append(f"{ref}:2")
    packet["focus_surface_evidence"]["qac_morphemes"].append({
        "qac_ref": f"{ref}:2:1",
        "qac_word_ref": f"{ref}:2",
    })
    packet["review_inventory"]["surface_refs"].append(f"{ref}:2")
    contribution["discovery_audit"]["reviewed_surface_refs"].append(f"{ref}:2")
    packet["review_inventory"]["branch_facets"] = [{
        "branch_ref": branch_ref,
        "facet_id": "F001",
    }]
    candidate["branch_refs"] = [branch_ref]
    candidate["branch_context_refs"] = {branch_ref: []}
    finding["branch_activations"] = [{
        "branch_ref": branch_ref,
        "facet_id": "F001",
        "branch_gloss": branch_gloss,
        "facet_statement": facet_statement,
        "application_mode": "intrinsic_cross_root",
        "carrier_refs": [f"{ref}:1"],
        "trigger_refs": [f"{ref}:2"],
        "focus_return_refs": [f"{ref}:1"],
        "carrier": "eylem sozu",
        "independent_trigger": "acik yol sozu",
        "activation": "Iki anlam ayni cumlede birbirini gorunur kilar.",
        "resulting_reading": "Eylem, tekrar yurunen bir yol gibi belirir.",
        "boundary": "Bu, eylem sozcugunu literal yol diye cevirmek degildir.",
        "prose_statement": prose_statement,
    }]
    finding["draft_prose"] = (
        f"{finding['prose_statement']} {prose_statement} "
        "Bu temas eylemin yon verici etkisini aciklar."
    )
    contribution["discovery_audit"]["branch_dispositions"] = [{
        "branch_ref": branch_ref,
        "facet_id": "F001",
        "decision": "activated",
        "reason": "Odak tasiyicisi bagimsiz yol sozuyle temas eder.",
        "finding_refs": [f"{lane}:finding"],
    }]


def write_canonical_output_set(
    layout: workflow.Layout,
    contributions: dict[str, dict[str, object]],
    *,
    phase: str,
) -> None:
    target = layout.raw if phase == "raw" else layout.editorial
    target.mkdir(parents=True, exist_ok=True)
    findings = [
        finding
        for lane in workflow.LANES
        for finding in contributions[lane]["findings"]
    ]
    prose_lines = []
    evidence_lines = []
    index_lines = []
    map_rows = []
    for ordinal, finding in enumerate(findings, start=1):
        finding_ref = finding["finding_ref"]
        activation_quotes = [
            activation["prose_statement"]
            for activation in finding["branch_activations"]
        ]
        prose_quote = finding["prose_statement"]
        prose_lines.extend([
            prose_quote,
            *(quote for quote in activation_quotes if quote != prose_quote),
        ])
        ledger = workflow.v3._canonical_json(
            workflow._finding_apparatus_ledger(contributions, finding)
        )
        evidence_quote = (
            f"- {finding_ref}: exact evidence landing {ordinal}.\n"
            f"provenance_ledger: {ledger}"
        )
        index_quote = (
            f"- {finding_ref}: exact index landing {ordinal}.\n"
            f"provenance_ledger: {ledger}"
        )
        evidence_lines.append(evidence_quote)
        index_lines.append(index_quote)
        map_rows.append({
            "finding_ref": finding_ref,
            "prose_quote": prose_quote,
            "evidence_quote": evidence_quote,
            "index_quote": index_quote,
            "activation_quotes": activation_quotes,
        })
    landing_map = {
        "schema_version": workflow.CANONICAL_LANDING_MAP_SCHEMA_VERSION,
        "ayah_ref": layout.ayah_ref,
        "phase": phase,
        "findings": map_rows,
    }
    outputs = {
        "prose": "\n".join(prose_lines) or "Bulgu bulunmayan tam okuma.",
        "evidence": "\n".join(evidence_lines) or "Bos bulgu kaniti.",
        "index": (
            ("\n".join(index_lines) + "\n" if index_lines else "")
            + "```commentary-v4-landing-map\n"
            + json.dumps(landing_map, ensure_ascii=False, sort_keys=True)
            + "\n```\n"
        ),
        "friction": "Canli surtunme yok.",
    }
    for kind, content in outputs.items():
        path = (
            layout.first_pass(kind)
            if phase == "raw"
            else layout.editorial_output(kind)
        )
        path.write_text(content, encoding="utf-8")


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
        self.assertIn("prose-ready Turkish", prompt)
        self.assertIn("candidate_decisions", prompt)
        self.assertIn("branch_activations", prompt)
        self.assertIn("entire relevant surface", prompt)
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
    def test_reader_prose_rejects_standalone_internal_ids(self) -> None:
        for internal_id in (
            "root_000001",
            "B001",
            "F001",
            "hft_deadbeef",
            "hft:macro:1",
        ):
            with self.subTest(internal_id=internal_id), self.assertRaisesRegex(
                workflow.WorkflowError, "exposes internal ID"
            ):
                workflow._assert_reader_prose_has_no_internal_ids(
                    f"Okuma {internal_id} uzerinden ilerler.", label="test prose"
                )

    def test_short_semantic_statement_fails_before_canonical_handoff(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash,
            candidate_id="cand_test",
        )
        contribution["findings"][0]["prose_statement"] = "Kisa soz."
        contribution["findings"][0]["draft_prose"] = "Kisa soz."

        with self.assertRaisesRegex(workflow.WorkflowError, "too short"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

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

    def test_accepted_candidate_requires_a_dedicated_origin_finding(self) -> None:
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
        contribution["findings"][0]["origin_candidate_id"] = None
        contribution["discovery_audit"]["discovered_finding_refs"] = [
            "micro:finding"
        ]
        manifest = {
            "lanes": {
                "micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }
            }
        }
        with self.assertRaisesRegex(workflow.WorkflowError, "dedicated origin"):
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

    def test_two_accepted_candidates_cannot_share_one_origin_finding(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_one", support_id="sup_one"
        )
        packet["candidate_inventory"].append({
            "candidate_id": "cand_two",
            "anchor_refs": ["1:1"],
            "support_ids": ["sup_two"],
            "branch_refs": [],
            "branch_context_refs": {},
            "required_context_refs": [],
            "trust": "trusted",
        })
        packet["support_registry"].append({
            "support_id": "sup_two",
            "trust": "trusted",
            "quran_refs": ["1:1"],
            "context_refs": [],
        })
        packet["review_inventory"]["support_ids"].append("sup_two")
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash,
            candidate_id="cand_one", support_id="sup_one"
        )
        contribution["candidate_decisions"].append({
            "candidate_id": "cand_two",
            "decision": "accept",
            "reason": "It appears related to the first candidate.",
            "finding_refs": ["micro:finding"],
            "branch_exclusions": [],
            "context_exclusions": [],
        })
        contribution["findings"][0]["support_ids"].append("sup_two")
        contribution["discovery_audit"]["reviewed_support_ids"].append("sup_two")
        manifest = {"lanes": {"micro": {
            "lane_packet_sha256": packet_hash,
            "request_sha256": request_hash,
        }}}

        with self.assertRaisesRegex(workflow.WorkflowError, "dedicated origin"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest=manifest,
                lane="micro",
                packet=packet,
            )

    def test_candidate_branch_cannot_disappear_without_exclusion(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"] = []
        contribution["discovery_audit"]["branch_dispositions"][0].update({
            "decision": "no_independent_trigger",
            "finding_refs": [],
        })

        with self.assertRaisesRegex(workflow.WorkflowError, "branch accounting"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_must_use_actual_focus_root_carrier(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"][0]["carrier_refs"] = [
            "1:1"
        ]

        with self.assertRaisesRegex(workflow.WorkflowError, "non-carrier"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_carrier_cannot_include_unrelated_refs(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"][0]["carrier_refs"] = [
            "1:1:1",
            "1:1:2",
        ]

        with self.assertRaisesRegex(workflow.WorkflowError, "non-carrier"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_requires_trigger_distinct_from_carrier(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"][0]["trigger_refs"] = [
            "1:1:1:1"
        ]

        with self.assertRaisesRegex(workflow.WorkflowError, "independent trigger"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_return_cannot_be_whole_focus_ayah(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"][0][
            "focus_return_refs"
        ] = ["1:1"]

        with self.assertRaisesRegex(workflow.WorkflowError, "focus surface"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_unregistered_branch_activation_must_remain_attributed(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        branch = packet["branch_registry"][0]
        branch["registry"] = "unresolved"
        branch["focus_root_occurrences"] = []
        branch["hft_citations"] = [{
            "hft_ref": "hft_test",
            "source_ref": "1:1",
            "source_word_indices": ["1"],
        }]

        with self.assertRaisesRegex(workflow.WorkflowError, "must remain attributed"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_context_branch_activation_must_use_context_root_carrier(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        branch = packet["branch_registry"][0]
        branch["registry"] = "context"
        branch["focus_root_occurrences"] = []
        branch["context_root_occurrences"] = [{
            "qac_ref": "2:2:1:1",
            "qac_word_ref": "2:2:1",
        }]
        branch["context_root_occurrence_refs_by_source"] = {
            "2:2": ["2:2:1:1", "2:2:1"]
        }
        packet["candidate_inventory"][0]["branch_context_refs"] = {
            branch["branch_ref"]: ["2:2"]
        }
        packet["candidate_inventory"][0]["required_context_refs"] = ["2:2"]
        packet["review_inventory"]["context_refs"] = ["2:2"]
        contribution["discovery_audit"]["reviewed_context_refs"] = ["2:2"]
        activation = contribution["findings"][0]["branch_activations"][0]
        activation["carrier_refs"] = ["1:1:1"]
        contribution["findings"][0]["context_refs"] = ["2:2"]

        with self.assertRaisesRegex(workflow.WorkflowError, "context-root"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_must_list_its_nonfocus_context(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        packet["support_registry"][0]["quran_refs"].append("2:2")
        packet["support_registry"][0]["context_refs"] = ["2:2"]
        packet["review_inventory"]["context_refs"] = ["2:2"]
        contribution["discovery_audit"]["reviewed_context_refs"] = ["2:2"]
        activation = contribution["findings"][0]["branch_activations"][0]
        activation["trigger_refs"] = ["2:2"]

        with self.assertRaisesRegex(workflow.WorkflowError, "omits.*context"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_prefatory_focus_linguistic_alias_is_not_external_context(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "29:0", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "29:0", "micro", packet_hash, request_hash,
            candidate_id="cand_test",
        )
        add_focus_branch(packet, contribution)
        packet["identity"]["linguistic_source_ref"] = "1:1"
        packet["focus_surface_evidence"]["word_analysis_refs"] = ["1:1:1", "1:1:2"]
        packet["focus_surface_evidence"]["qac_morphemes"] = [
            {"qac_ref": "1:1:1:1", "qac_word_ref": "1:1:1"},
            {"qac_ref": "1:1:2:1", "qac_word_ref": "1:1:2"},
        ]
        packet["review_inventory"]["surface_refs"] = ["1:1:1", "1:1:2"]
        packet["branch_registry"][0]["focus_root_occurrences"] = [{
            "qac_ref": "1:1:1:1",
            "qac_word_ref": "1:1:1",
        }]
        contribution["discovery_audit"]["reviewed_surface_refs"] = [
            "1:1:1", "1:1:2"
        ]
        activation = contribution["findings"][0]["branch_activations"][0]
        activation["carrier_refs"] = ["1:1:1"]
        activation["trigger_refs"] = ["1:1:2"]
        activation["focus_return_refs"] = ["1:1:1"]

        workflow._validate_scope_contribution(
            contribution,
            layout=workflow.layout_for("29:0", "s029-basmala-full"),
            manifest={"lanes": {"micro": {
                "lane_packet_sha256": packet_hash,
                "request_sha256": request_hash,
            }}},
            lane="micro",
            packet=packet,
        )
        self.assertEqual(contribution["findings"][0]["context_refs"], [])

        contribution["findings"][0]["context_refs"] = ["1:1"]
        with self.assertRaisesRegex(
            workflow.WorkflowError, "context_refs cites unknown IDs.*1:1"
        ):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("29:0", "s029-basmala-full"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

        packet["review_inventory"]["context_refs"] = ["1:1"]
        contribution["discovery_audit"]["reviewed_context_refs"] = ["1:1"]
        with self.assertRaisesRegex(
            workflow.WorkflowError, "context review inventory includes its focus"
        ):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("29:0", "s029-basmala-full"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_branch_activation_must_preserve_exact_facet_source(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["findings"][0]["branch_activations"][0][
            "facet_statement"
        ] = "Generic meaning."

        with self.assertRaisesRegex(workflow.WorkflowError, "facet_statement is stale"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_full_branch_facet_audit_is_required(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        add_focus_branch(packet, contribution)
        contribution["discovery_audit"]["branch_dispositions"] = []

        with self.assertRaisesRegex(workflow.WorkflowError, "branch-facet.*incomplete"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
                packet=packet,
            )

    def test_legacy_unbound_evidence_cannot_be_called_grounded(self) -> None:
        packet_hash = "a" * 64
        request_hash = "b" * 64
        packet = lane_packet(
            "1:1", "micro", packet_hash, candidate_id="cand_test"
        )
        packet["candidate_inventory"][0]["trust"] = "legacy_unbound"
        packet["support_registry"][0]["trust"] = "legacy_unbound"
        contribution = valid_contribution(
            "1:1", "micro", packet_hash, request_hash, candidate_id="cand_test"
        )
        contribution["findings"][0]["epistemic"]["source_trust"] = [
            "legacy_unbound"
        ]

        with self.assertRaisesRegex(workflow.WorkflowError, "cannot be grounded"):
            workflow._validate_scope_contribution(
                contribution,
                layout=workflow.layout_for("1:1"),
                manifest={"lanes": {"micro": {
                    "lane_packet_sha256": packet_hash,
                    "request_sha256": request_hash,
                }}},
                lane="micro",
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

                    contributions = {
                        lane: json.loads(
                            layout.scope_contribution(lane).read_text(
                                encoding="utf-8"
                            )
                        )
                        for lane in workflow.LANES
                    }
                    write_canonical_output_set(
                        layout, contributions, phase="raw"
                    )

                    editorial = workflow.advance(args)
                    self.assertEqual(editorial["stage"], "canonical_editorial")
                    self.assertTrue(layout.editorial_prompt.is_file())

                    write_canonical_output_set(
                        layout, contributions, phase="editorial"
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

    def test_manifest_reload_runs_added_ayah_root_agreement_check(self) -> None:
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

                with patch.object(
                    workflow,
                    "_verify_added_ayah_root_agreement",
                    wraps=workflow._verify_added_ayah_root_agreement,
                ) as verify_agreement:
                    workflow._load_unit_manifest(layout)

                verify_agreement.assert_called_once()


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


class CanonicalLandingTests(unittest.TestCase):
    def test_raw_and_editorial_outputs_preserve_exact_finding_landings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {}
            for lane in workflow.LANES:
                packet_hash = f"{workflow.LANE_RANK[lane] + 1}" * 64
                request_hash = f"{workflow.LANE_RANK[lane] + 4}" * 64
                packet = lane_packet(
                    "1:1", lane, packet_hash, candidate_id=f"cand_{lane}"
                )
                contribution = valid_contribution(
                    "1:1", lane, packet_hash, request_hash,
                    candidate_id=f"cand_{lane}"
                )
                if lane == "micro":
                    add_focus_branch(packet, contribution)
                contributions[lane] = contribution

            write_canonical_output_set(layout, contributions, phase="raw")
            write_canonical_output_set(layout, contributions, phase="editorial")
            workflow._validate_canonical_outputs(
                layout, contributions, phase="raw"
            )
            workflow._validate_canonical_outputs(
                layout, contributions, phase="editorial"
            )

    def test_editorial_output_cannot_drop_branch_activation_sentence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            packet = lane_packet(
                "1:1", "micro", "1" * 64, candidate_id="cand_micro"
            )
            add_focus_branch(packet, contributions["micro"])
            write_canonical_output_set(layout, contributions, phase="editorial")
            statement = contributions["micro"]["findings"][0][
                "branch_activations"
            ][0]["prose_statement"]
            path = layout.editorial_output("prose")
            path.write_text(
                path.read_text(encoding="utf-8").replace(statement, ""),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                workflow.WorkflowError, "activation_quotes.*exactly once"
            ):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="editorial"
                )

    def test_landing_map_cannot_substitute_generic_finding_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            write_canonical_output_set(layout, contributions, phase="raw")
            generic = "Bu paragraf baska bir genel yorum daha sunar."
            prose_path = layout.first_pass("prose")
            prose_path.write_text(
                prose_path.read_text(encoding="utf-8") + "\n" + generic,
                encoding="utf-8",
            )
            index_path = layout.first_pass("index")
            index_text = index_path.read_text(encoding="utf-8")
            landing, _ = workflow._parse_landing_map(
                index_text, ayah_ref="1:1", phase="raw"
            )
            landing["findings"][0]["prose_quote"] = generic
            match = workflow.LANDING_MAP_BLOCK_RE.search(index_text)
            assert match is not None
            index_path.write_text(
                index_text[:match.start()]
                + "```commentary-v4-landing-map\n"
                + json.dumps(landing, ensure_ascii=False, sort_keys=True)
                + "\n```\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                workflow.WorkflowError, "does not preserve its finding semantics"
            ):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="raw"
                )

    def test_landing_map_cannot_use_another_findings_semantic_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            write_canonical_output_set(layout, contributions, phase="raw")
            index_path = layout.first_pass("index")
            index_text = index_path.read_text(encoding="utf-8")
            landing, _ = workflow._parse_landing_map(
                index_text, ayah_ref="1:1", phase="raw"
            )
            landing["findings"][1]["prose_quote"] = landing["findings"][0][
                "prose_quote"
            ]
            match = workflow.LANDING_MAP_BLOCK_RE.search(index_text)
            assert match is not None
            index_path.write_text(
                index_text[:match.start()]
                + "```commentary-v4-landing-map\n"
                + json.dumps(landing, ensure_ascii=False, sort_keys=True)
                + "\n```\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                workflow.WorkflowError, "does not preserve its finding semantics"
            ):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="raw"
                )

    def test_apparatus_quote_must_preserve_exact_provenance_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            write_canonical_output_set(layout, contributions, phase="raw")
            index_path = layout.first_pass("index")
            index_text = index_path.read_text(encoding="utf-8")
            landing, _ = workflow._parse_landing_map(
                index_text, ayah_ref="1:1", phase="raw"
            )
            old_quote = landing["findings"][0]["evidence_quote"]
            replacement = "- micro:finding: generic evidence placeholder."
            evidence_path = layout.first_pass("evidence")
            evidence_path.write_text(
                evidence_path.read_text(encoding="utf-8").replace(
                    old_quote, replacement
                ),
                encoding="utf-8",
            )
            landing["findings"][0]["evidence_quote"] = replacement
            match = workflow.LANDING_MAP_BLOCK_RE.search(index_text)
            assert match is not None
            index_path.write_text(
                index_text[:match.start()]
                + "```commentary-v4-landing-map\n"
                + json.dumps(landing, ensure_ascii=False, sort_keys=True)
                + "\n```\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                workflow.WorkflowError, "provenance ledger"
            ):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="raw"
                )

    def test_finding_ledger_preserves_full_branch_and_connection_audit(self) -> None:
        contributions = {
            lane: valid_contribution(
                "1:1",
                lane,
                f"{workflow.LANE_RANK[lane] + 1}" * 64,
                f"{workflow.LANE_RANK[lane] + 4}" * 64,
                candidate_id=f"cand_{lane}",
            )
            for lane in workflow.LANES
        }
        finding = contributions["macro"]["findings"][0]
        finding["connection_refs"] = ["conn_macro"]
        branch_disposition = {
            "branch_ref": "root_000001/B001",
            "facet_id": "F001",
            "decision": "activated",
            "reason": "The branch has an independent trigger.",
            "finding_refs": [finding["finding_ref"]],
        }
        disposition = {
            "connection_ref": "conn_macro",
            "decision": "activated",
            "reason": "The reciprocal row returns to the focus.",
            "finding_refs": [finding["finding_ref"]],
            "evidence_rows": [
                {
                    "connection_evidence_ref": "conn_ev_authored",
                    "decision": "activated",
                    "reason": "The authored row supplies the first path.",
                    "finding_refs": [finding["finding_ref"]],
                },
                {
                    "connection_evidence_ref": "conn_ev_reciprocal",
                    "decision": "no_return_path",
                    "reason": "The reciprocal alternative remains excluded.",
                    "finding_refs": [],
                },
            ],
        }
        contributions["macro"]["discovery_audit"][
            "connection_dispositions"
        ] = [disposition]
        contributions["macro"]["discovery_audit"][
            "branch_dispositions"
        ] = [branch_disposition]

        ledger = workflow._finding_apparatus_ledger(contributions, finding)

        self.assertEqual(ledger["branch_dispositions"], [branch_disposition])
        self.assertEqual(ledger["connection_dispositions"], [disposition])

    def test_provenance_ledger_must_occur_once_per_apparatus_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            write_canonical_output_set(layout, contributions, phase="raw")
            finding = contributions["micro"]["findings"][0]
            ledger = workflow.v3._canonical_json(
                workflow._finding_apparatus_ledger(contributions, finding)
            )
            evidence_path = layout.first_pass("evidence")
            evidence_path.write_text(
                evidence_path.read_text(encoding="utf-8")
                + f"\nDuplicate ledger: {ledger}\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(workflow.WorkflowError, "exactly once"):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="raw"
                )

    def test_provenance_ledger_must_occur_once_in_premap_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            write_canonical_output_set(layout, contributions, phase="raw")
            finding = contributions["micro"]["findings"][0]
            ledger = workflow.v3._canonical_json(
                workflow._finding_apparatus_ledger(contributions, finding)
            )
            index_path = layout.first_pass("index")
            index_text = index_path.read_text(encoding="utf-8")
            match = workflow.LANDING_MAP_BLOCK_RE.search(index_text)
            assert match is not None
            index_path.write_text(
                index_text[:match.start()]
                + f"Duplicate ledger: {ledger}\n"
                + index_text[match.start():],
                encoding="utf-8",
            )

            with self.assertRaisesRegex(workflow.WorkflowError, "exactly once"):
                workflow._validate_canonical_outputs(
                    layout, contributions, phase="raw"
                )

    def test_overlapping_immutable_statements_fail_before_canonical_handoff(
        self,
    ) -> None:
        contributions = {
            lane: valid_contribution(
                "1:1",
                lane,
                f"{workflow.LANE_RANK[lane] + 1}" * 64,
                f"{workflow.LANE_RANK[lane] + 4}" * 64,
                candidate_id=f"cand_{lane}",
            )
            for lane in workflow.LANES
        }
        micro_statement = contributions["micro"]["findings"][0][
            "prose_statement"
        ]
        macro_statement = f"{micro_statement} Bu ek, ikinci bulguyu kurar."
        contributions["macro"]["findings"][0]["prose_statement"] = macro_statement
        contributions["macro"]["findings"][0]["draft_prose"] = macro_statement

        with self.assertRaisesRegex(workflow.WorkflowError, "overlapping"):
            workflow._validate_semantic_statement_set(contributions)

    def test_apparatus_landing_spans_cannot_overlap(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "overlapping span"):
            workflow._assert_disjoint_quote_spans(
                [
                    (0, 40, "micro:one", "apparatus", "long quote"),
                    (10, 30, "macro:two", "apparatus", "nested quote"),
                ],
                label="raw evidence",
            )

    def test_same_finding_statement_can_serve_as_its_activation_landing(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            layout = workflow.Layout(
                ayah_ref="1:1",
                stem="1_1",
                input=root / "input",
                raw=root / "raw",
                editorial=root / "editorial",
            )
            contributions = {
                lane: valid_contribution(
                    "1:1",
                    lane,
                    f"{workflow.LANE_RANK[lane] + 1}" * 64,
                    f"{workflow.LANE_RANK[lane] + 4}" * 64,
                    candidate_id=f"cand_{lane}",
                )
                for lane in workflow.LANES
            }
            finding = contributions["micro"]["findings"][0]
            finding["branch_activations"] = [{
                "prose_statement": finding["prose_statement"]
            }]
            write_canonical_output_set(layout, contributions, phase="raw")

            workflow._validate_canonical_outputs(
                layout, contributions, phase="raw"
            )


class ProjectionTests(unittest.TestCase):
    @staticmethod
    def empty_packets(ref: str) -> dict[str, dict[str, object]]:
        return {
            lane: lane_packet(ref, lane, f"{index + 1}" * 64)
            for index, lane in enumerate(workflow.LANES)
        }

    def test_quran_ref_extraction_reads_coordinates_keys_and_existing_refs(self) -> None:
        value = {
            "trace at 29:41:9:1": {
                "description": "Compare 29:43:2 with the focus.",
                "quran_refs": ["7:201"],
            }
        }
        self.assertEqual(
            workflow._extract_quran_refs(value),
            ["7:201", "29:41", "29:43"],
        )

    def test_prefatory_focus_alias_cannot_create_a_context_probe(self) -> None:
        packets = self.empty_packets("29:0")
        for packet in packets.values():
            packet["identity"]["linguistic_source_ref"] = "1:1"
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "cand_alias",
            "source_type": "word_analysis",
            "source_local_id": "alias",
            "anchor_refs": ["29:0"],
            "support_ids": ["sup_alias"],
            "branch_refs": [],
            "trust": "trusted",
        }]
        packets["micro"]["support_registry"] = [{
            "support_id": "sup_alias",
            "source_local_id": "alias",
            "quran_refs": ["1:1"],
            "context_refs": ["1:1"],
            "trust": "trusted",
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                basmala_bundle("29:0"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            for lane in workflow.LANES:
                workflow._validate_packet_review_inventory(
                    routed[lane], lane=lane
                )

        candidate = routed["micro"]["candidate_inventory"][0]
        support = routed["micro"]["support_registry"][0]
        self.assertEqual(candidate["required_context_refs"], [])
        self.assertEqual(support["context_refs"], [])
        self.assertFalse(any(
            row.get("source_type") == "support_quran_reference_probe"
            for packet in routed.values()
            for row in packet["candidate_inventory"]
        ))
        self.assertTrue(all(
            packet["review_inventory"]["context_refs"] == []
            for packet in routed.values()
        ))

    def test_quran_ref_extraction_bounds_malformed_large_range(self) -> None:
        self.assertEqual(
            workflow._extract_quran_refs("1:1-999999999"),
            [],
        )

    def test_selected_cross_surah_context_stays_global_without_probe(self) -> None:
        packets = self.empty_packets("29:38")
        packets["global"]["candidate_inventory"] = [{
            "candidate_id": "cand_selected",
            "source_type": "selected_context_unit",
            "source_local_id": "1:1",
            "anchor_refs": ["1:1"],
            "support_ids": ["sup_selected"],
            "branch_refs": [],
            "trust": "canonical_bundle_hash_bound",
        }]
        packets["global"]["support_registry"] = [{
            "support_id": "sup_selected",
            "source_local_id": "1:1",
            "context_refs": ["1:1"],
            "quran_refs": ["1:1"],
            "trust": "canonical_bundle_hash_bound",
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )

        self.assertFalse(any(
            row["candidate_id"] == "cand_selected"
            for row in routed["macro"]["candidate_inventory"]
        ))
        global_candidates = routed["global"]["candidate_inventory"]
        self.assertEqual(
            [row["candidate_id"] for row in global_candidates],
            ["cand_selected"],
        )
        self.assertEqual(global_candidates[0]["support_ids"], ["sup_selected"])

    def test_multi_support_candidate_routes_with_all_its_supports(self) -> None:
        packets = self.empty_packets("29:38")
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "cand_multi",
            "source_type": "word_analysis",
            "source_local_id": "shared-source",
            "anchor_refs": ["29:38"],
            "support_ids": ["sup_local", "sup_wide"],
            "branch_refs": [],
            "trust": "trusted",
        }]
        packets["micro"]["support_registry"] = [
            {
                "support_id": "sup_local",
                "source_local_id": "shared-source",
                "quran_refs": ["29:38"],
                "trust": "trusted",
            },
            {
                "support_id": "sup_wide",
                "source_local_id": "different-source",
                "quran_refs": ["7:201"],
                "trust": "trusted",
            },
        ]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )

        candidate = next(
            row
            for row in routed["global"]["candidate_inventory"]
            if row["candidate_id"] == "cand_multi"
        )
        self.assertEqual(candidate["support_ids"], ["sup_local", "sup_wide"])
        self.assertEqual(candidate["required_context_refs"], ["7:201"])
        self.assertFalse(any(
            row["source_type"] == "support_quran_reference_probe"
            for row in routed["global"]["candidate_inventory"]
        ))

    def test_serialized_range_refs_route_candidate_to_global(self) -> None:
        packets = self.empty_packets("29:38")
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "cand_range",
            "source_type": "word_analysis",
            "source_local_id": "range-source",
            "anchor_refs": ["29:38"],
            "support_ids": ["sup_range"],
            "branch_refs": [],
            "trust": "trusted",
        }]
        packets["micro"]["support_registry"] = [{
            "support_id": "sup_range",
            "source_local_id": "range-source",
            "text": '{"target": "7:201-202"}',
            "trust": "trusted",
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )

        self.assertEqual(routed["micro"]["candidate_inventory"], [])
        candidate = next(
            row
            for row in routed["global"]["candidate_inventory"]
            if row["candidate_id"] == "cand_range"
        )
        self.assertEqual(candidate["required_context_refs"], ["7:201", "7:202"])
        support = next(
            row
            for row in routed["global"]["support_registry"]
            if row["support_id"] == "sup_range"
        )
        self.assertEqual(support["context_refs"], ["7:201", "7:202"])

    def test_branch_only_cross_surah_ref_routes_to_global_before_hydration(
        self,
    ) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_001054/B001"
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "cand_branch_only_wide",
            "source_type": "hft",
            "source_local_id": "branch-only-wide",
            "hft_ref": "hft_branch_only_wide",
            "anchor_refs": ["29:38"],
            "support_ids": ["sup_branch_only_wide"],
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
        }]
        packets["micro"]["support_registry"] = [{
            "support_id": "sup_branch_only_wide",
            "source_local_id": "branch-only-wide",
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
        }]
        packets["micro"]["branch_registry"] = [{
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": ["sup_branch_only_wide"],
            "hft_citations": [{
                "hft_ref": "hft_branch_only_wide",
                "source_ref": "7:201",
                "source_word_indices": ["1"],
            }],
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "s007" / "7_201.ayah.json"
            path.parent.mkdir()
            path.write_text(
                json.dumps(context_branch_bundle("7:201")), encoding="utf-8"
            )
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            workflow._validate_packet_review_inventory(
                routed["global"], lane="global"
            )

        self.assertEqual(routed["micro"]["candidate_inventory"], [])
        candidate = next(
            row
            for row in routed["global"]["candidate_inventory"]
            if row["candidate_id"] == "cand_branch_only_wide"
        )
        self.assertEqual(candidate["required_context_refs"], ["7:201"])
        self.assertEqual(
            candidate["branch_context_refs"], {branch_ref: ["7:201"]}
        )
        self.assertIn("7:201", routed["global"]["review_inventory"]["context_refs"])

    def test_same_lane_hydration_keeps_candidate_specific_carriers(self) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_001054/B001"
        candidates = []
        supports = []
        citations = []
        for suffix, context_ref in (("a", "29:40"), ("b", "29:41")):
            candidate_id = f"cand_{suffix}"
            support_id = f"sup_{suffix}"
            hft_ref = f"hft_{suffix}"
            candidates.append({
                "candidate_id": candidate_id,
                "source_type": "hft",
                "source_local_id": candidate_id,
                "hft_ref": hft_ref,
                "anchor_refs": ["29:38"],
                "support_ids": [support_id],
                "branch_refs": [branch_ref],
                "trust": "legacy_unbound",
            })
            supports.append({
                "support_id": support_id,
                "source_local_id": candidate_id,
                "branch_refs": [branch_ref],
                "payload": {"activation_trace": [{
                    "mapped_root_id": "root_001054",
                    "branch_id": "B001",
                    "source_ref": context_ref,
                }]},
                "trust": "legacy_unbound",
            })
            citations.append({
                "hft_ref": hft_ref,
                "source_ref": context_ref,
                "source_word_indices": ["1"],
            })
        packets["macro"]["candidate_inventory"] = candidates
        packets["macro"]["support_registry"] = supports
        packets["macro"]["branch_registry"] = [{
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": ["sup_a", "sup_b"],
            "hft_citations": citations,
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "s029"
            path.mkdir()
            for ref in ("29:40", "29:41"):
                (path / f"{ref.replace(':', '_')}.ayah.json").write_text(
                    json.dumps(context_branch_bundle(ref)), encoding="utf-8"
                )
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            workflow._validate_packet_review_inventory(
                routed["macro"], lane="macro"
            )

            packet = routed["macro"]
            branch = next(
                row for row in packet["branch_registry"]
                if row["branch_ref"] == branch_ref
            )
            packet_hash = packet["identity"]["lane_packet_sha256"]
            request_hash = "b" * 64
            contribution = valid_contribution(
                "29:38",
                "macro",
                packet_hash,
                request_hash,
                candidate_id="cand_a",
                support_id="sup_a",
            )
            contribution["candidate_decisions"].append({
                "candidate_id": "cand_b",
                "decision": "reject",
                "reason": "The second candidate is not used by this finding.",
                "finding_refs": [],
                "branch_exclusions": [{
                    "branch_ref": branch_ref,
                    "reason": "The branch belongs to the rejected candidate here.",
                }],
                "context_exclusions": [{
                    "context_ref": "29:41",
                    "reason": "This context belongs to the rejected candidate.",
                }],
            })
            finding = contribution["findings"][0]
            activation_statement = (
                "Ag imgesi odak sozuyle bulussa da yanlis tasiyici kullanilamaz."
            )
            finding.update({
                "epistemic": {
                    "status": "qualified",
                    "source_trust": ["legacy_unbound"],
                    "reason": "The branch source remains explicitly qualified.",
                },
                "context_refs": ["29:40", "29:41"],
                "branch_activations": [{
                    "branch_ref": branch_ref,
                    "facet_id": "F001",
                    "branch_gloss": branch["gloss"],
                    "facet_statement": branch["review_facets"][0]["statements"][
                        "statement"
                    ],
                    "application_mode": "contextual_resonance",
                    "carrier_refs": ["29:41:1"],
                    "trigger_refs": ["29:38:1"],
                    "focus_return_refs": ["29:38:1"],
                    "carrier": "baglamdaki ag imgesi",
                    "independent_trigger": "odak ayetin sozu",
                    "activation": "Iki unsur baglamda temas eder.",
                    "resulting_reading": "Odak, ag imgesiyle yeniden okunur.",
                    "boundary": "Bu, odak sozcugunun sozluk anlami degildir.",
                    "prose_statement": activation_statement,
                }],
            })
            finding["draft_prose"] = (
                f"{finding['prose_statement']} {activation_statement}"
            )
            contribution["discovery_audit"].update({
                "reviewed_surface_refs": packet["review_inventory"][
                    "surface_refs"
                ],
                "reviewed_context_refs": packet["review_inventory"][
                    "context_refs"
                ],
                "reviewed_support_ids": packet["review_inventory"][
                    "support_ids"
                ],
                "branch_dispositions": [{
                    "branch_ref": branch_ref,
                    "facet_id": "F001",
                    "decision": "activated",
                    "reason": "The finding claims this branch is active.",
                    "finding_refs": ["macro:finding"],
                }],
            })
            with self.assertRaisesRegex(workflow.WorkflowError, "context-root"):
                workflow._validate_scope_contribution(
                    contribution,
                    layout=workflow.layout_for("29:38"),
                    manifest={"lanes": {"macro": {
                        "lane_packet_sha256": packet_hash,
                        "request_sha256": request_hash,
                    }}},
                    lane="macro",
                    packet=packet,
                )

        packet = routed["macro"]
        candidate_map = {
            row["candidate_id"]: row for row in packet["candidate_inventory"]
        }
        branch = next(
            row for row in packet["branch_registry"]
            if row["branch_ref"] == branch_ref
        )
        self.assertEqual(
            candidate_map["cand_a"]["branch_context_refs"],
            {branch_ref: ["29:40"]},
        )
        allowed = workflow._context_branch_carriers_for_finding(
            branch, branch_ref, ["cand_a"], candidate_map
        )
        self.assertEqual(allowed, {"29:40:1", "29:40:1:1"})
        self.assertNotIn("29:41:1", allowed)

    def test_repeated_branch_keeps_only_the_routed_lane_hft_citation(self) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_000672/B010"
        branch = {
            "branch_ref": branch_ref,
            "registry": "focus",
            "root_id": "root_000672",
            "root_ar": "r hamza y",
            "lexicon_identity_status": "accepted",
            "branch_kind": "mixed_non_bare",
            "gloss": "eye condition",
            "boundary": "A branch image, not the lexical translation.",
            "semantic_detail": {},
            "review_facets": [{
                "facet_id": "F001",
                "role": "core",
                "statements": {"statement": "A concrete eye condition."},
            }],
            "focus_root_occurrences": [{
                "qac_ref": "29:38:1:1",
                "qac_word_ref": "29:38:1",
            }],
            "candidate_links": [],
            "support_links": [],
        }
        for lane in workflow.LANES:
            packets[lane]["branch_registry"] = [copy.deepcopy(branch)]
        packets["macro"]["candidate_inventory"] = [{
            "candidate_id": "cand_hft",
            "source_type": "hft",
            "source_local_id": "hft-row",
            "anchor_refs": ["29:38"],
            "support_ids": ["sup_hft"],
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
            "hft_ref": "hft:macro:1",
        }]
        packets["macro"]["support_registry"] = [{
            "support_id": "sup_hft",
            "source_local_id": "hft-row",
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
        }]
        packets["macro"]["branch_registry"][0].update({
            "candidate_links": [{
                "candidate_id": "cand_hft",
                "lane": "macro",
            }],
            "support_links": ["sup_hft"],
            "hft_citations": [{
                "hft_ref": "hft:macro:1",
                "role": "carrier",
            }],
        })
        packets["global"]["branch_registry"][0]["hft_citations"] = [{
            "hft_ref": "hft:global:unrelated",
            "role": "unrelated",
        }]

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )

        macro_branch = routed["macro"]["branch_registry"][0]
        self.assertEqual(macro_branch["support_links"], ["sup_hft"])
        self.assertEqual(
            macro_branch["candidate_links"],
            [{"candidate_id": "cand_hft", "lane": "macro"}],
        )
        self.assertEqual(
            macro_branch["hft_citations"],
            [{"hft_ref": "hft:macro:1", "role": "carrier"}],
        )
        self.assertEqual(routed["micro"]["branch_registry"][0]["hft_citations"], [])
        self.assertEqual(routed["global"]["branch_registry"][0]["hft_citations"], [])

    def test_basmala_linguistic_alias_does_not_force_global_routing(self) -> None:
        packets = self.empty_packets("29:38")
        packets["micro"]["candidate_inventory"] = [{
            "candidate_id": "cand_basmala",
            "source_type": "automatic_prefatory_basmala_surah_member",
            "source_local_id": "29:0",
            "anchor_refs": ["29:0"],
            "support_ids": ["sup_basmala"],
            "branch_refs": [],
            "trust": "canonical_bundle_hash_bound",
        }]
        packets["micro"]["support_registry"] = [{
            "support_id": "sup_basmala",
            "source_local_id": "29:0",
            "context_refs": ["29:0"],
            "payload": {
                "surface_ref": "29:0",
                "linguistic_source_ref": "1:1",
                "qac_ref": "1:1:1:1",
            },
            "qualification": {"automatic_prefatory_basmala_membership": True},
            "trust": "canonical_bundle_hash_bound",
        }]
        source = numbered_bundle("29:38")
        source["linguistic_source_ref"] = "29:38"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                source,
                package_bundle_root=root,
                member_bundle_root=root,
            )

        candidate = next(
            row
            for row in routed["macro"]["candidate_inventory"]
            if row["candidate_id"] == "cand_basmala"
        )
        self.assertEqual(candidate["required_context_refs"], ["29:0"])
        self.assertFalse(any(
            row["candidate_id"] == "cand_basmala"
            for row in routed["global"]["candidate_inventory"]
        ))

    def test_unresolved_context_branch_is_hydrated_and_hash_bound(self) -> None:
        packets = self.empty_packets("29:38")
        packets["macro"]["candidate_inventory"] = [{
            "candidate_id": "cand_context_branch",
            "source_type": "hft",
            "source_local_id": "context-branch",
            "anchor_refs": ["29:38", "29:41"],
            "support_ids": ["sup_context_branch"],
            "branch_refs": ["root_001054/B001"],
            "trust": "legacy_unbound",
        }]
        packets["macro"]["support_registry"] = [{
            "support_id": "sup_context_branch",
            "source_local_id": "context-branch",
            "text": "29:41 supplies the context trigger.",
            "branch_refs": ["root_001054/B001"],
            "trust": "legacy_unbound",
        }]
        packets["macro"]["branch_registry"] = [{
            "branch_ref": "root_001054/B001",
            "registry": "nominated",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": ["sup_context_branch"],
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            context = context_branch_bundle("29:41")
            path = root / "s029" / "29_41.ayah.json"
            path.parent.mkdir()
            path.write_text(json.dumps(context), encoding="utf-8")
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            branch = next(
                row
                for row in routed["macro"]["branch_registry"]
                if row["branch_ref"] == "root_001054/B001"
            )
            self.assertEqual(branch["lexicon_identity_status"], "accepted")
            self.assertEqual(branch["context_source_refs"], ["29:41"])
            self.assertEqual(
                set(branch["context_source_canonical_sha256s"]), {"29:41"}
            )
            self.assertEqual(len(branch["review_facets"]), 1)
            workflow._validate_packet_review_inventory(
                routed["macro"], lane="macro"
            )

            stale = copy.deepcopy(routed["macro"])
            stale_branch = next(
                row
                for row in stale["branch_registry"]
                if row["branch_ref"] == "root_001054/B001"
            )
            stale_branch["registry"] = "focus"
            stale_branch["focus_root_occurrences"] = [{
                "qac_ref": "29:38:1:1",
                "qac_word_ref": "29:38:1",
            }]
            with self.assertRaisesRegex(workflow.WorkflowError, "branch is stale"):
                workflow._validate_packet_review_inventory(stale, lane="macro")

            context["generated_at"] = "changed"
            path.write_text(json.dumps(context), encoding="utf-8")
            with self.assertRaisesRegex(workflow.WorkflowError, "source changed"):
                workflow._validate_packet_review_inventory(
                    routed["macro"], lane="macro"
                )

    def test_context_branch_hydration_uses_exact_trace_source_not_all_anchors(
        self,
    ) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_001054/B001"
        packets["macro"]["candidate_inventory"] = [{
            "candidate_id": "cand_exact_context",
            "source_type": "hft",
            "source_local_id": "exact-context",
            "hft_ref": "hft_exact_context",
            "anchor_refs": ["29:38", "29:40", "29:41"],
            "support_ids": ["sup_exact_context"],
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
        }]
        packets["macro"]["support_registry"] = [{
            "support_id": "sup_exact_context",
            "source_local_id": "exact-context",
            "quran_refs": ["29:40", "29:41"],
            "branch_refs": [branch_ref],
            "payload": {"activation_trace": [{
                "mapped_root_id": "root_001054",
                "branch_id": "B001",
                "source_ref": "29:41",
            }]},
            "trust": "legacy_unbound",
        }]
        packets["macro"]["branch_registry"] = [{
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": ["sup_exact_context"],
            "hft_citations": [{
                "hft_ref": "hft_exact_context",
                "source_ref": "29:41",
                "source_word_indices": ["1"],
            }],
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "s029"
            path.mkdir()
            for ref in ("29:40", "29:41"):
                (path / f"{ref.replace(':', '_')}.ayah.json").write_text(
                    json.dumps(context_branch_bundle(ref)), encoding="utf-8"
                )
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )

        branch = next(
            row
            for row in routed["macro"]["branch_registry"]
            if row["branch_ref"] == branch_ref
        )
        self.assertEqual(branch["context_source_refs"], ["29:41"])
        self.assertEqual(
            {row["ayah_ref"] for row in routed["macro"]["auxiliary_context_sources"]},
            {"29:41"},
        )

    def test_context_branch_hydration_aggregates_all_exact_trace_sources(
        self,
    ) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_001054/B001"
        trace = [
            {
                "mapped_root_id": "root_001054",
                "branch_id": "B001",
                "source_ref": ref,
            }
            for ref in ("29:40", "29:41")
        ]
        packets["macro"]["candidate_inventory"] = [{
            "candidate_id": "cand_multi_context",
            "source_type": "hft",
            "source_local_id": "multi-context",
            "hft_ref": "hft_multi_context",
            "anchor_refs": ["29:38", "29:40", "29:41"],
            "support_ids": ["sup_multi_context"],
            "branch_refs": [branch_ref],
            "trust": "legacy_unbound",
        }]
        packets["macro"]["support_registry"] = [{
            "support_id": "sup_multi_context",
            "source_local_id": "multi-context",
            "quran_refs": ["29:40", "29:41"],
            "branch_refs": [branch_ref],
            "payload": {"activation_trace": trace},
            "trust": "legacy_unbound",
        }]
        packets["macro"]["branch_registry"] = [{
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": ["sup_multi_context"],
            "hft_citations": [
                {
                    "hft_ref": "hft_multi_context",
                    "source_ref": ref,
                    "source_word_indices": ["1"],
                }
                for ref in ("29:40", "29:41")
            ],
        }]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "s029"
            path.mkdir()
            for ref in ("29:40", "29:41"):
                (path / f"{ref.replace(':', '_')}.ayah.json").write_text(
                    json.dumps(context_branch_bundle(ref)), encoding="utf-8"
                )
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            workflow._validate_packet_review_inventory(
                routed["macro"], lane="macro"
            )
            stale = copy.deepcopy(routed["macro"])
            stale_branch = next(
                row
                for row in stale["branch_registry"]
                if row["branch_ref"] == branch_ref
            )
            stale_branch["context_source_canonical_sha256s"]["29:41"] = "0" * 64
            with self.assertRaisesRegex(workflow.WorkflowError, "hashes are stale"):
                workflow._validate_packet_review_inventory(stale, lane="macro")

        branch = next(
            row
            for row in routed["macro"]["branch_registry"]
            if row["branch_ref"] == branch_ref
        )
        self.assertEqual(branch["context_source_refs"], ["29:40", "29:41"])
        self.assertEqual(len(branch["context_root_occurrences"]), 2)
        self.assertEqual(
            set(branch["context_source_canonical_sha256s"]),
            {"29:40", "29:41"},
        )

    def test_context_branch_hydration_is_lane_local(self) -> None:
        packets = self.empty_packets("29:38")
        branch_ref = "root_001054/B001"
        base_branch = {
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "lexicon_identity_status": "unresolved",
            "review_facets": [],
            "candidate_links": [],
            "support_links": [],
        }
        for lane, context_ref in (("macro", "29:40"), ("global", "7:201")):
            candidate_id = f"cand_{lane}_context"
            support_id = f"sup_{lane}_context"
            hft_ref = f"hft_{lane}_context"
            packets[lane]["candidate_inventory"] = [{
                "candidate_id": candidate_id,
                "source_type": "hft",
                "source_local_id": candidate_id,
                "hft_ref": hft_ref,
                "anchor_refs": ["29:38", context_ref],
                "support_ids": [support_id],
                "branch_refs": [branch_ref],
                "trust": "legacy_unbound",
            }]
            packets[lane]["support_registry"] = [{
                "support_id": support_id,
                "source_local_id": candidate_id,
                "quran_refs": [context_ref],
                "branch_refs": [branch_ref],
                "payload": {"activation_trace": [{
                    "mapped_root_id": "root_001054",
                    "branch_id": "B001",
                    "source_ref": context_ref,
                }]},
                "trust": "legacy_unbound",
            }]
            branch = copy.deepcopy(base_branch)
            branch["candidate_links"] = [{
                "candidate_id": candidate_id,
                "lane": lane,
            }]
            branch["support_links"] = [support_id]
            branch["hft_citations"] = [{
                "hft_ref": hft_ref,
                "source_ref": context_ref,
                "source_word_indices": ["1"],
            }]
            packets[lane]["branch_registry"] = [branch]

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for ref in ("29:40", "7:201"):
                path = root / f"s{int(ref.split(':', 1)[0]):03d}"
                path.mkdir()
                (path / f"{ref.replace(':', '_')}.ayah.json").write_text(
                    json.dumps(context_branch_bundle(ref)), encoding="utf-8"
                )
            routed = workflow._normalize_and_route_lane_packets(
                packets,
                numbered_bundle("29:38"),
                package_bundle_root=root,
                member_bundle_root=root,
            )
            for lane in ("macro", "global"):
                workflow._validate_packet_review_inventory(
                    routed[lane], lane=lane
                )

        macro_branch = routed["macro"]["branch_registry"][0]
        global_branch = routed["global"]["branch_registry"][0]
        self.assertEqual(macro_branch["context_source_refs"], ["29:40"])
        self.assertEqual(global_branch["context_source_refs"], ["7:201"])

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

    def test_added_ayah_duplicate_roots_are_rechecked_after_prepare(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package_root = root / "package"
            member_root = root / "members"
            bundle = numbered_bundle("17:50")
            for bundle_root in (package_root, member_root):
                path = bundle_root / "s017" / "17_50.ayah.json"
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps(bundle), encoding="utf-8")
            selected = [{
                "ayah_ref": "17:50",
                "canonical_sha256": workflow.compositions.canonical_sha256(bundle),
                "membership_added_ayah": True,
            }]
            analysis = {
                "context_bundles_dir": str(package_root),
                "member_bundles_dir": str(member_root),
            }
            workflow._verify_added_ayah_root_agreement(analysis, selected)

            changed = copy.deepcopy(bundle)
            changed["text"]["arabic_uthmani"] = "changed"
            (member_root / "s017" / "17_50.ayah.json").write_text(
                json.dumps(changed), encoding="utf-8"
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "differs"):
                workflow._verify_added_ayah_root_agreement(analysis, selected)

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
