from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "workflow.py"
SPEC = importlib.util.spec_from_file_location("commentary_v5_workflow", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
workflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workflow
SPEC.loader.exec_module(workflow)


def numbered_bundle(ref: str, *, text: str = "text") -> dict[str, object]:
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
        "text": {"arabic_uthmani": text},
        "qac_morphemes": [{"qac_ref": f"{ref}:1:1"}],
        "word_analysis": {"ref": ref, "words": []},
        "coverage": {},
    }


def basmala_bundle(ref: str = "100:0") -> dict[str, object]:
    bundle = numbered_bundle("1:1", text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
    surah = int(ref.split(":", 1)[0])
    bundle.update({
        "unit_kind": "prefatory_basmala",
        "surah": surah,
        "ayah": 0,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": "1:1",
        "coverage": {
            "basmala_alias": {
                "normalized_surface_equivalent": True,
                "target_normalized": workflow.compositions.BASMALA_NORMALIZED_SURFACE,
                "source_normalized": workflow.compositions.BASMALA_NORMALIZED_SURFACE,
            }
        },
    })
    return bundle


def branch(
    branch_ref: str = "root_000001/B001",
    *,
    root_ar: str = "ع و د",
) -> dict[str, object]:
    return {
        "branch_ref": branch_ref,
        "root_id": branch_ref.split("/", 1)[0],
        "root_ar": root_ar,
        "registry": "focus",
        "lexicon_identity_status": "accepted",
        "gloss": "donus yolu",
        "review_facets": [
            {
                "facet_id": "F001",
                "role": "core",
                "statements": {"statement": "Geri donusun temel anlami."},
            },
            {
                "facet_id": "F002",
                "role": "specialization",
                "statements": {"statement": "Yeniden kullanilan eski yol."},
            },
        ],
        "focus_root_occurrences": [
            {
                "qac_ref": "1:1:1:1",
                "qac_word_ref": "1:1:1",
                "surface_ar": "عَادَ",
            }
        ],
    }


def packet(
    *,
    lane: str = "micro",
    candidate: bool = True,
    context_ref: str | None = None,
    hft: bool = False,
    branches: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    branch_rows = branches if branches is not None else [branch()]
    support = {
        "support_id": "sup_test",
        "source_type": "hft" if hft else "word_analysis",
        "source_local_id": "candidate:test",
        "role": "hft_nomination_evidence" if hft else "candidate_evidence",
        "trust": "legacy_unbound" if hft else "trusted",
        "quran_refs": ["1:1", *([context_ref] if context_ref else [])],
        "context_refs": [context_ref] if context_ref else [],
        "text": (
            "A repeated return becomes visible through the separate road image."
            if not hft
            else None
        ),
    }
    if hft:
        support["payload"] = {
            "activation_trace": [
                {
                    "mapped_root_id": branch_rows[0]["root_id"],
                    "branch_id": str(branch_rows[0]["branch_ref"]).split("/", 1)[1],
                    "source_ref": context_ref or "1:1",
                    "source_word_indices": ["1"],
                    "role": "The named branch changes the reading.",
                }
            ],
            "changed_reading": {
                "before": "A plain reading.",
                "after": "A changed reading.",
            },
            "mechanism": "The carrier and trigger alter the reading together.",
            "reader_inference": "The reader infers a bounded secondary image.",
            "structural_cues": ["The two terms occur in one causal sequence."],
            "containment": "This remains a bounded analogy.",
        }
    candidate_row = {
        "candidate_id": "cand_test",
        "source_type": "hft" if hft else "word_analysis",
        "source_local_id": "candidate:test",
        "title": "Repeated return and road",
        "anchor_refs": ["1:1", *([context_ref] if context_ref else [])],
        "support_ids": ["sup_test"],
        "branch_refs": [branch_rows[0]["branch_ref"]],
        "branch_context_refs": {branch_rows[0]["branch_ref"]: []},
        "required_context_refs": [context_ref] if context_ref else [],
        "required_branch_facets": [],
        "semantic_obligations": [],
        "root_ids": [],
        "trust": support["trust"],
    }
    candidate_row["semantic_obligations"] = (
        workflow._candidate_semantic_obligations(
            candidate_row, {"sup_test": support}
        )
    )
    candidates = [candidate_row] if candidate else []
    supports = [support] if candidate else []
    return {
        "schema_version": workflow.LANE_PACKET_SCHEMA_VERSION,
        "identity": {
            "ayah_ref": "1:1",
            "linguistic_source_ref": "1:1",
            "lane": lane,
            "lane_packet_sha256": "a" * 64,
        },
        "contract": {
            "candidate_context_refs_are_exact": True,
            "support_quran_refs_are_structured": True,
            "accepted_candidates_require_dedicated_findings": True,
            "independent_discovery_is_required": True,
            "candidate_semantics_require_explicit_accounting": True,
            "root_branch_options_are_non_nominating": True,
        },
        "focus_surface_evidence": {
            "word_analysis_refs": ["1:1:1", "1:1:2"],
            "qac_morphemes": [
                {"qac_ref": "1:1:1:1", "qac_word_ref": "1:1:1"},
                {"qac_ref": "1:1:2:1", "qac_word_ref": "1:1:2"},
            ],
        },
        "candidate_inventory": candidates,
        "support_registry": supports,
        "branch_registry": branch_rows,
        "connection_registry": [],
        "auxiliary_context_sources": [],
        "review_inventory": {
            "surface_refs": ["1:1:1", "1:1:2"],
            "context_refs": [context_ref] if context_ref else [],
            "support_ids": ["sup_test"] if candidate else [],
            "connection_refs": [],
            "connection_evidence_refs": {},
            "available_branch_facets": workflow._branch_review_pairs(branch_rows),
        },
    }


def manifest_for(lane: str = "micro") -> dict[str, object]:
    return {
        "lanes": {
            lane: {
                "lane_packet_sha256": "a" * 64,
                "discovery": {"request_sha256": "b" * 64},
                "composition": None,
            }
        }
    }


def activation(
    source_branch: dict[str, object],
    *,
    facet_id: str = "F001",
    trigger_ref: str = "1:1:2",
) -> dict[str, object]:
    _, statement = workflow._branch_source_values(source_branch, facet_id)
    return {
        "branch_ref": source_branch["branch_ref"],
        "facet_id": facet_id,
        "branch_gloss": source_branch["gloss"],
        "facet_statement": statement,
        "application_mode": "intrinsic_cross_root",
        "carrier_refs": ["1:1:1"],
        "trigger_refs": [trigger_ref],
        "focus_return_refs": ["1:1:2"],
        "carrier": "Donus kokunun tasidigi anlam.",
        "independent_trigger": "Ayetteki ayri yol imgesi.",
        "activation": "Iki alan birbirini gorunur kilar.",
        "resulting_reading": "Yolun tekrar edilmesi belirginlesir.",
        "boundary": "Bu, ozel adi sozluk anlamina indirgemez.",
    }


def discovery_for(
    source_packet: dict[str, object],
    *,
    lane: str = "micro",
    trigger_ref: str = "1:1:2",
) -> dict[str, object]:
    candidate = source_packet["candidate_inventory"][0]
    obligations = [
        row["obligation_ref"] for row in candidate["semantic_obligations"]
    ]
    context_refs = [
        ref for ref in candidate["required_context_refs"] if ref != "1:1"
    ]
    finding_ref = f"{lane}:finding"
    return {
        "schema_version": workflow.SCOPE_DISCOVERY_SCHEMA_VERSION,
        "identity": {
            "ayah_ref": "1:1",
            "lane": lane,
            "lane_packet_sha256": "a" * 64,
            "authoring_request_sha256": "b" * 64,
        },
        "ayah_ref": "1:1",
        "lane": lane,
        "coverage_complete": True,
        "candidate_decisions": [
            {
                "candidate_id": "cand_test",
                "decision": "accept",
                "reason": "The evidence supplies a bounded contact.",
                "finding_refs": [finding_ref],
                "branch_exclusions": [],
                "facet_exclusions": [],
                "context_exclusions": [],
                "semantic_obligation_exclusions": [],
            }
        ],
        "findings": [
            {
                "finding_ref": finding_ref,
                "origin_candidate_id": "cand_test",
                "represented_candidate_ids": [],
                "title": "Tekrarlanan yol",
                "claim": "Eski yol imgesi yeniden kullanimi duyurur.",
                "mechanism": "Kok alani ayri yol imgesiyle temas eder.",
                "reader_payoff": "Okur tekrar ile sapma arasindaki bagi gorur.",
                "containment": "Ozel ad sozluk anlamina indirgenmez.",
                "epistemic": {
                    "status": (
                        "qualified"
                        if candidate["trust"] == "legacy_unbound"
                        else "grounded"
                    ),
                    "source_trust": [candidate["trust"]],
                    "reason": "Kaynak siniri acikca korunur.",
                },
                "support_ids": ["sup_test"],
                "branch_activations": [
                    activation(
                        source_packet["branch_registry"][0],
                        trigger_ref=trigger_ref,
                    )
                ],
                "connection_refs": [],
                "context_refs": context_refs,
                "semantic_obligation_refs": obligations,
            }
        ],
        "friction_notes": [],
    }


def validate_discovery(
    value: dict[str, object], source_packet: dict[str, object], lane: str = "micro"
) -> None:
    workflow._validate_scope_discovery(
        value,
        layout=workflow.layout_for("1:1"),
        manifest=manifest_for(lane),
        lane=lane,
        packet=source_packet,
    )


def scope_results() -> dict[str, dict[str, object]]:
    common = (
        "Bu ortak Turkce paragraf, iki ayri bulgunun mekanizmasini ve "
        "okuma sonucunu acik bicimde birlikte tasir."
    )
    result: dict[str, dict[str, object]] = {}
    for lane in workflow.LANES:
        findings = []
        if lane in {"micro", "macro"}:
            finding = {
                "finding_ref": f"{lane}:one",
                "claim": "Sinirli bir iddia.",
                "mechanism": "Acik bir mekanizma.",
                "reader_payoff": "Belirgin bir okur kazanci.",
                "containment": "Kaynakla sinirli.",
                "epistemic": {
                    "status": "grounded",
                    "source_trust": ["trusted"],
                    "reason": "Dogrudan kanit.",
                },
                "support_ids": [],
                "branch_activations": [],
                "connection_refs": [],
                "context_refs": [],
                "semantic_obligation_refs": [],
                "origin_candidate_id": None,
                "represented_candidate_ids": [],
                "title": "Bulgu",
                "prose": common,
            }
            inventory = [
                workflow._semantic_inventory_record(
                    f"discovery:{field}",
                    "discovery_field",
                    {"field": field, "value": finding[field]},
                )
                for field in ("claim", "mechanism", "reader_payoff", "containment")
            ]
            finding["semantic_inventory"] = inventory
            finding["composition_semantic_landings"] = [
                {
                    "semantic_refs": [row["semantic_ref"] for row in inventory],
                    "prose_quote": common,
                }
            ]
            findings.append(finding)
        result[lane] = {
            "lane": lane,
            "candidate_decisions": [],
            "findings": findings,
            "friction_notes": [],
        }
    return result


def write_output_set(
    layout: workflow.Layout,
    results: dict[str, dict[str, object]],
    *,
    phase: str,
    prose: str,
) -> None:
    target = layout.raw if phase == "raw" else layout.editorial
    target.mkdir(parents=True, exist_ok=True)
    evidence_lines = []
    index_lines = []
    landing_rows = []
    for finding in workflow._ordered_findings(results):
        finding_ref = finding["finding_ref"]
        ledger_record = workflow._finding_apparatus_ledger(results, finding)
        ledger = workflow.v3._canonical_json(ledger_record)
        evidence_quote = f"Kanita ait {finding_ref} ayrintili kaydi: {ledger}"
        index_quote = (
            f"Dizine ait {finding_ref} kaynak ozeti: "
            f"{ledger_record['source_record_sha256']}"
        )
        evidence_lines.append(evidence_quote)
        index_lines.append(index_quote)
        landing_rows.append(
            {
                "finding_ref": finding_ref,
                "semantic_landings": [
                    {
                        "semantic_refs": [
                            row["semantic_ref"]
                            for row in finding["semantic_inventory"]
                        ],
                        "prose_quote": prose,
                    }
                ],
                "evidence_quote": evidence_quote,
                "index_quote": index_quote,
                "provenance_sha256": workflow._finding_apparatus_ledger(
                    results, finding
                )["source_record_sha256"],
            }
        )
    landing_map = {
        "schema_version": workflow.CANONICAL_LANDING_MAP_SCHEMA_VERSION,
        "ayah_ref": "1:1",
        "phase": phase,
        "findings": landing_rows,
    }
    texts = {
        "prose": prose,
        "evidence": "\n".join(evidence_lines),
        "index": (
            "\n".join(index_lines)
            + "\n```commentary-v5-landing-map\n"
            + json.dumps(landing_map, ensure_ascii=False, sort_keys=True)
            + "\n```\n"
        ),
        "friction": "Cekisme kaydi yoktur.",
    }
    for kind, text in texts.items():
        path = (
            layout.first_pass(kind)
            if phase == "raw"
            else layout.editorial_output(kind)
        )
        path.write_text(text, encoding="utf-8")


class LayoutAndPromptTests(unittest.TestCase):
    def test_v5_has_two_lane_artifacts_and_prompts(self) -> None:
        layout = workflow.layout_for("29:38")
        self.assertEqual(layout.scope_discovery("micro").name, "micro.discovery.json")
        self.assertEqual(
            layout.composition_prompt("micro").name,
            "micro.composition.prompt.md",
        )

    def test_prompts_separate_discovery_from_composition(self) -> None:
        discovery_prompt = (workflow.PROMPTS_ROOT / "discovery.md").read_text()
        composition_prompt = (workflow.PROMPTS_ROOT / "composition.md").read_text()
        editorial_prompt = (workflow.PROMPTS_ROOT / "editorial.md").read_text()
        self.assertIn("Do not write polished commentary prose", discovery_prompt)
        self.assertIn("planned second turn", composition_prompt)
        self.assertIn("No scope sentence is verbatim-immutable", editorial_prompt)
        self.assertNotIn("one-pass scope author", discovery_prompt)

    def test_composition_prompt_does_not_duplicate_the_lane_packet(self) -> None:
        source_packet = packet()
        source_packet["unused_packet_bulk"] = "x" * 250_000
        discovery = discovery_for(source_packet)
        discovery["candidate_decisions"][0]["reason"] = "z" * 250_000

        prompt, record = workflow._build_composition_prompt(
            workflow.layout_for("1:1"), "micro", source_packet, discovery
        )

        self.assertNotIn("unused_packet_bulk", prompt)
        self.assertNotIn("z" * 1_000, prompt)
        self.assertNotIn("<lane_packet_json>", prompt)
        self.assertEqual(
            record["request_inputs"]["lane_packet_sha256"], "a" * 64
        )
        self.assertLess(
            len(prompt.encode("utf-8")),
            len(workflow._canonical_json_bytes(source_packet)),
        )

    def test_discovery_prompt_budget_is_enforced_by_builder(self) -> None:
        with (
            patch.object(workflow, "MAX_DISCOVERY_PROMPT_BYTES", 1),
            self.assertRaisesRegex(
                workflow.WorkflowError, "micro discovery prompt exceeds"
            ),
        ):
            workflow._build_discovery_prompt(
                workflow.layout_for("1:1"), "micro", packet()
            )

    def test_discovery_prompt_rejects_realistically_oversized_packet(self) -> None:
        source_packet = packet()
        source_packet["unexpected_packet_dump"] = (
            "x" * workflow.MAX_DISCOVERY_PROMPT_BYTES
        )
        with self.assertRaisesRegex(
            workflow.WorkflowError, "micro discovery prompt exceeds"
        ):
            workflow._build_discovery_prompt(
                workflow.layout_for("1:1"), "micro", source_packet
            )

    def test_lane_packet_cap_leaves_discovery_prompt_headroom(self) -> None:
        source_packet = packet()
        prompt, _record = workflow._build_discovery_prompt(
            workflow.layout_for("1:1"), "micro", source_packet
        )
        fixed_overhead = len(prompt.encode("utf-8")) - len(
            workflow._canonical_json_bytes(source_packet)
        )
        remaining = (
            workflow.MAX_DISCOVERY_PROMPT_BYTES
            - workflow.MAX_LANE_PACKET_BYTES
            - fixed_overhead
        )

        self.assertGreaterEqual(remaining, 100_000)

    def test_composition_prompt_budget_is_enforced_by_builder(self) -> None:
        source_packet = packet()
        with (
            patch.object(workflow, "MAX_COMPOSITION_PROMPT_BYTES", 1),
            self.assertRaisesRegex(
                workflow.WorkflowError, "micro composition prompt exceeds"
            ),
        ):
            workflow._build_composition_prompt(
                workflow.layout_for("1:1"),
                "micro",
                source_packet,
                discovery_for(source_packet),
            )

    def test_canonical_prompt_budget_is_enforced_by_builder(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            layout.input.mkdir()
            for lane in workflow.LANES:
                layout.packet(lane).write_bytes(
                    workflow._canonical_json_bytes(packet(lane=lane), newline=True)
                )
            manifest = {
                "editorial": {
                    "instructions_sha256": "a" * 64,
                    "handoff_template_sha256": "b" * 64,
                }
            }
            with (
                patch.object(workflow, "MAX_CANONICAL_PROMPT_BYTES", 1),
                self.assertRaisesRegex(
                    workflow.WorkflowError, "canonical prompt exceeds"
                ),
            ):
                workflow._build_canonical_prompt(
                    layout, manifest, scope_results()
                )

    def test_editorial_prompt_budget_is_enforced_by_builder(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            layout.raw.mkdir()
            for kind in workflow.KINDS:
                layout.first_pass(kind).write_text(
                    "Turkce deneme metni.", encoding="utf-8"
                )
            with (
                patch.object(workflow, "MAX_EDITORIAL_PROMPT_BYTES", 1),
                self.assertRaisesRegex(
                    workflow.WorkflowError, "editorial handoff exceeds"
                ),
            ):
                workflow._build_editorial_prompt(
                    layout, {"request_sha256": "c" * 64}
                )

    def test_discovery_and_composition_handoffs_are_recoverable(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            manifest = {
                "lanes": {
                    "micro": {
                        "discovery": {"request_sha256": "b" * 64},
                        "composition": {"request_sha256": "c" * 64},
                    }
                }
            }
            with patch.object(workflow, "RAW_ROOT", root / "raw"):
                first = workflow._discovery_handoff(layout, manifest, "micro")
                second = workflow._composition_handoff(layout, manifest, "micro")
            self.assertTrue(first["fresh_agent"])
            self.assertTrue(second["same_live_agent"])
            self.assertTrue(second["replacement_agent_allowed"])


class DiscoveryValidationTests(unittest.TestCase):
    def test_valid_candidate_discovery_passes(self) -> None:
        source_packet = packet()
        validate_discovery(discovery_for(source_packet), source_packet)

    def test_word_candidate_evidence_becomes_a_semantic_obligation(self) -> None:
        source_packet = packet()
        obligations = source_packet["candidate_inventory"][0][
            "semantic_obligations"
        ]
        self.assertEqual(
            [row["kind"] for row in obligations], ["candidate_evidence"]
        )
        self.assertIn("repeated return", obligations[0]["semantic_claim"])

    def test_reader_walk_candidate_evidence_is_also_an_obligation(self) -> None:
        source_packet = packet()
        candidate = source_packet["candidate_inventory"][0]
        support = source_packet["support_registry"][0]
        candidate["source_type"] = "v12_reader_walks"
        support["source_type"] = "v12_reader_walks"
        candidate["semantic_obligations"] = (
            workflow._candidate_semantic_obligations(
                candidate, {support["support_id"]: support}
            )
        )
        self.assertEqual(
            [row["kind"] for row in candidate["semantic_obligations"]],
            ["candidate_evidence"],
        )

    def test_candidate_text_does_not_depend_on_one_support_role_name(self) -> None:
        source_packet = packet()
        candidate = source_packet["candidate_inventory"][0]
        support = source_packet["support_registry"][0]
        support["role"] = "branch_nomination"

        obligations = workflow._candidate_semantic_obligations(
            candidate, {support["support_id"]: support}
        )

        self.assertEqual([row["kind"] for row in obligations], ["candidate_support_text"])
        self.assertEqual(obligations[0]["support_role"], "branch_nomination")

    def test_prefatory_obligation_order_survives_canonical_json_round_trip(self) -> None:
        candidate = {
            "candidate_id": "cand_prefatory",
            "support_ids": ["sup_prefatory"],
        }
        support = {
            "support_id": "sup_prefatory",
            "source_type": "prefatory_basmala_focus_evidence",
            "role": "surah_conditioned_prefatory_evidence",
            "payload": {
                "z_section": {"reading": "son"},
                "a_section": {"reading": "ilk"},
                "not_applicable_states": {"hft": "not_applicable"},
            },
        }
        before = workflow._candidate_semantic_obligations(
            candidate, {"sup_prefatory": support}
        )
        round_tripped_support = json.loads(
            workflow.v3._canonical_json(support)
        )
        after = workflow._candidate_semantic_obligations(
            candidate, {"sup_prefatory": round_tripped_support}
        )

        self.assertEqual(before, after)
        self.assertEqual(
            [row["section"] for row in before], ["a_section", "z_section"]
        )

    def test_candidate_branch_cannot_disappear(self) -> None:
        source_packet = packet()
        value = discovery_for(source_packet)
        value["findings"][0]["branch_activations"] = []
        with self.assertRaisesRegex(workflow.WorkflowError, "branch accounting"):
            validate_discovery(value, source_packet)

    def test_packet_registry_ids_must_be_unique(self) -> None:
        source_packet = packet()
        source_packet["branch_registry"].append(
            copy.deepcopy(source_packet["branch_registry"][0])
        )
        with self.assertRaisesRegex(workflow.WorkflowError, "duplicate IDs"):
            validate_discovery(discovery_for(source_packet), source_packet)

    def test_context_listing_without_carrier_or_trigger_does_not_land(self) -> None:
        source_packet = packet(context_ref="2:2")
        value = discovery_for(source_packet, trigger_ref="1:1:2")
        with self.assertRaisesRegex(workflow.WorkflowError, "context accounting"):
            validate_discovery(value, source_packet)

    def test_context_trigger_lands_required_context(self) -> None:
        source_packet = packet(context_ref="2:2")
        value = discovery_for(source_packet, trigger_ref="2:2")
        validate_discovery(value, source_packet)

    def test_specialization_cannot_survive_without_core(self) -> None:
        source_packet = packet()
        value = discovery_for(source_packet)
        value["findings"][0]["branch_activations"] = [
            activation(source_packet["branch_registry"][0], facet_id="F002")
        ]
        with self.assertRaisesRegex(workflow.WorkflowError, "without its core facet"):
            validate_discovery(value, source_packet)

    def test_hft_semantic_obligations_are_first_class(self) -> None:
        source_packet = packet(hft=True)
        kinds = [
            row["kind"]
            for row in source_packet["candidate_inventory"][0][
                "semantic_obligations"
            ]
        ]
        self.assertEqual(
            kinds,
            [
                "activation_trace",
                "changed_reading",
                "mechanism",
                "reader_inference",
                "containment",
                "structural_cue",
            ],
        )
        value = discovery_for(source_packet)
        value["findings"][0]["semantic_obligation_refs"].pop()
        with self.assertRaisesRegex(workflow.WorkflowError, "semantic-obligation"):
            validate_discovery(value, source_packet)

    def test_narrow_candidate_must_retain_some_semantic_content(self) -> None:
        source_packet = packet()
        value = discovery_for(source_packet)
        obligation_ref = value["findings"][0]["semantic_obligation_refs"].pop()
        value["candidate_decisions"][0]["decision"] = "narrow"
        value["candidate_decisions"][0]["semantic_obligation_exclusions"] = [
            {
                "obligation_ref": obligation_ref,
                "reason": "The supplied wording is too broad.",
            }
        ]
        with self.assertRaisesRegex(workflow.WorkflowError, "no retained"):
            validate_discovery(value, source_packet)

    def test_represented_candidate_cannot_exclude_semantics(self) -> None:
        source_packet = packet()
        duplicate = copy.deepcopy(source_packet["candidate_inventory"][0])
        duplicate["candidate_id"] = "cand_duplicate"
        duplicate["semantic_obligations"] = (
            workflow._candidate_semantic_obligations(
                duplicate,
                {"sup_test": source_packet["support_registry"][0]},
            )
        )
        source_packet["candidate_inventory"].append(duplicate)
        value = discovery_for(source_packet)
        duplicate_ref = duplicate["semantic_obligations"][0]["obligation_ref"]
        value["findings"][0]["represented_candidate_ids"] = ["cand_duplicate"]
        value["findings"][0]["semantic_obligation_refs"].append(duplicate_ref)
        value["candidate_decisions"].append(
            {
                "candidate_id": "cand_duplicate",
                "decision": "represented",
                "reason": "It is semantically identical to the first candidate.",
                "finding_refs": [value["findings"][0]["finding_ref"]],
                "branch_exclusions": [],
                "facet_exclusions": [],
                "context_exclusions": [],
                "semantic_obligation_exclusions": [],
            }
        )
        validate_discovery(value, source_packet)

        value["findings"][0]["semantic_obligation_refs"].remove(duplicate_ref)
        value["candidate_decisions"][1]["semantic_obligation_exclusions"] = [
            {
                "obligation_ref": duplicate_ref,
                "reason": "The duplicate detail was omitted.",
            }
        ]
        with self.assertRaisesRegex(workflow.WorkflowError, "has exclusions"):
            validate_discovery(value, source_packet)

    def test_trace_obligation_requires_its_named_branch(self) -> None:
        first = branch()
        second = branch("root_000002/B001", root_ar="س ب ل")
        source_packet = packet(hft=True, branches=[first, second])
        candidate = source_packet["candidate_inventory"][0]
        candidate["branch_refs"].append(second["branch_ref"])
        candidate["branch_context_refs"][second["branch_ref"]] = []
        obligation = candidate["semantic_obligations"][0]
        obligation["branch_ref"] = second["branch_ref"]
        source_packet["support_registry"][0]["payload"]["activation_trace"][0].update(
            {"mapped_root_id": second["root_id"], "branch_id": "B001"}
        )
        candidate["semantic_obligations"] = workflow._candidate_semantic_obligations(
            candidate, {"sup_test": source_packet["support_registry"][0]}
        )
        value = discovery_for(source_packet)
        value["candidate_decisions"][0]["decision"] = "narrow"
        value["candidate_decisions"][0]["branch_exclusions"] = [
            {"branch_ref": second["branch_ref"], "reason": "No valid carrier."}
        ]
        with self.assertRaisesRegex(workflow.WorkflowError, "named branch"):
            validate_discovery(value, source_packet)

    def test_word_analysis_root_ids_are_normalized_without_branch_nomination(self) -> None:
        candidate = {
            "source_type": "word_analysis",
            "support_ids": ["sup_root"],
            "root_ids": [],
            "branch_refs": [],
        }
        supports = {
            "sup_root": {
                "support_id": "sup_root",
                "text": json.dumps(
                    {"root_display": "{{ar:ع و د / س ب ل}} (return / road)"}
                ),
            }
        }
        branches = {
            row["branch_ref"]: row
            for row in [
                branch(),
                branch("root_000002/B001"),
                branch("root_000003/B001", root_ar="س ب ل"),
            ]
        }
        workflow._normalize_word_analysis_root_ids(candidate, supports, branches)
        self.assertEqual(
            candidate["root_ids"],
            ["root_000001", "root_000002", "root_000003"],
        )
        self.assertEqual(
            workflow._candidate_root_branch_options(candidate, branches),
            ["root_000001/B001", "root_000002/B001", "root_000003/B001"],
        )
        self.assertEqual(candidate["branch_refs"], [])


class CompositionValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.packet = packet()
        self.discovery = discovery_for(self.packet)
        self.manifest = manifest_for()
        self.manifest["lanes"]["micro"]["composition"] = {
            "request_sha256": "c" * 64
        }

    def contribution(self, prose: str) -> dict[str, object]:
        source = self.discovery["findings"][0]
        inventory = workflow._finding_semantic_inventory(source, self.packet)
        return {
            "schema_version": workflow.SCOPE_COMPOSITION_SCHEMA_VERSION,
            "identity": {
                "ayah_ref": "1:1",
                "lane": "micro",
                "lane_packet_sha256": "a" * 64,
                "discovery_sha256": workflow.v3._sha256_json(self.discovery),
                "authoring_request_sha256": "c" * 64,
            },
            "ayah_ref": "1:1",
            "lane": "micro",
            "findings": [
                {
                    "finding_ref": source["finding_ref"],
                    "prose": prose,
                    "semantic_landings": [
                        {
                            "semantic_refs": [
                                row["semantic_ref"] for row in inventory
                            ],
                            "prose_quote": prose,
                        }
                    ],
                }
            ],
            "friction_notes": [],
        }

    def validate(self, value: dict[str, object]) -> None:
        workflow._validate_scope_composition(
            value,
            layout=workflow.layout_for("1:1"),
            manifest=self.manifest,
            lane="micro",
            discovery=self.discovery,
            packet=self.packet,
        )

    def test_valid_turkish_composition_passes(self) -> None:
        self.validate(
            self.contribution(
                "Kokteki donus anlami, ayetteki yol imgesiyle temas ederek "
                "tekrarlanan yonelisi gorunur kilar."
            )
        )

    def test_obvious_english_term_is_rejected(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "English"):
            self.validate(
                self.contribution(
                    "Bu temas discernment alanini okuyucu icin gorunur kilar."
                )
            )

    def test_english_sentence_is_rejected(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "English"):
            self.validate(
                self.contribution(
                    "This is the reading that was carried into the final prose."
                )
            )

    def test_composition_cannot_drop_semantic_record(self) -> None:
        value = self.contribution(
            "Donus anlami yol imgesiyle temas ederek yeni okumayi aciklar."
        )
        value["findings"][0]["semantic_landings"][0]["semantic_refs"].pop()
        with self.assertRaisesRegex(workflow.WorkflowError, "coverage"):
            self.validate(value)

    def test_composition_cannot_insert_unknown_semantic_ref(self) -> None:
        source_packet = packet(context_ref="1:2")
        self.packet = source_packet
        self.discovery = discovery_for(source_packet, trigger_ref="1:2:1")
        value = self.contribution(
            "Donus anlami komsu ayetin yol imgesiyle temas ederek yeni "
            "okumayi aciklar."
        )
        value["findings"][0]["semantic_landings"][0]["semantic_refs"][-1] = (
            "forged:semantic"
        )
        with self.assertRaisesRegex(workflow.WorkflowError, "unknown semantic"):
            self.validate(value)

    def test_short_english_sentence_is_rejected(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "English"):
            self.validate(
                self.contribution("Knowledge guides action through memory.")
            )


class StateAndLineageTests(unittest.TestCase):
    def test_composition_prompt_binds_persisted_discovery(self) -> None:
        source_packet = packet()
        discovery = discovery_for(source_packet)
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1",
                "1_1",
                root / "input" / "1_1",
                root / "raw" / "1_1",
                root / "editorial" / "1_1",
            )
            layout.input.mkdir(parents=True)
            layout.raw.mkdir(parents=True)
            layout.packet("micro").write_bytes(
                workflow._canonical_json_bytes(source_packet, newline=True)
            )
            layout.scope_discovery("micro").write_text(
                json.dumps(discovery), encoding="utf-8"
            )
            local_manifest = manifest_for()
            layout.manifest.write_bytes(workflow._pretty_json_bytes(local_manifest))
            with patch.object(workflow, "INPUT_ROOT", root / "input"):
                record = workflow._ensure_scope_composition(
                    layout,
                    local_manifest,
                    "micro",
                    source_packet,
                    discovery,
                )
                self.assertTrue(layout.composition_prompt("micro").is_file())
                self.assertEqual(
                    record["discovery"]["sha256"],
                    workflow._sha256(layout.scope_discovery("micro").read_bytes()),
                )
                layout.scope_discovery("micro").write_text("{}", encoding="utf-8")
                with self.assertRaisesRegex(workflow.WorkflowError, "changed"):
                    workflow._ensure_scope_composition(
                        layout,
                        local_manifest,
                        "micro",
                        source_packet,
                        discovery,
                    )

    def test_real_cold_start_returns_three_discovery_handoffs(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            args = workflow._parser().parse_args(["advance", "--ayah", "1:1"])
            args.ayah = "1:1"
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                status = workflow.advance(args)
            self.assertEqual(status["stage"], "scope_discovery")
            self.assertEqual(
                [row["role"] for row in status["handoffs"]],
                [f"{lane}_scope_discoverer" for lane in workflow.LANES],
            )

    def test_real_basmala_cold_start_reloads_with_complete_host_context(self) -> None:
        args = workflow._parser().parse_args(["advance", "--ayah", "100:0"])
        quran_evidence, _coverage = workflow._quran_text_projection(args.quran_text)
        args.analysis_id = "s100-basmala-full"
        args.composition = workflow._automatic_basmala_composition(
            "100:0", quran_evidence
        )
        args.ayah = "100:0"
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                status = workflow.advance(args)
                layout = workflow.layout_for("100:0", "s100-basmala-full")
                manifest = workflow._load_unit_manifest(layout)

        self.assertEqual(status["stage"], "scope_discovery")
        self.assertEqual(
            [
                unit["ayah_ref"]
                for unit in manifest["analysis"]["selected_context_units"]
            ],
            [f"100:{ayah}" for ayah in range(1, 12)],
        )

    def test_complete_discovery_set_advances_to_three_composition_handoffs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1",
                "1_1",
                root / "input" / "1_1",
                root / "raw" / "1_1",
                root / "editorial" / "1_1",
            )
            layout.input.mkdir(parents=True)
            layout.manifest.write_text("{}", encoding="utf-8")
            manifest = {
                "lanes": {
                    lane: {
                        "lane_packet_sha256": "a" * 64,
                        "discovery": {"request_sha256": "b" * 64},
                        "composition": None,
                    }
                    for lane in workflow.LANES
                }
            }
            args = workflow._parser().parse_args(["advance", "--ayah", "1:1"])

            def bind_composition(
                unused_layout: workflow.Layout,
                current_manifest: dict[str, object],
                lane: str,
                unused_packet: dict[str, object],
                unused_discovery: dict[str, object],
            ) -> dict[str, object]:
                record = {"request_sha256": f"{lane}-request"}
                current_manifest["lanes"][lane]["composition"] = record
                return record

            with (
                patch.object(workflow, "_layout_for_args", return_value=layout),
                patch.object(workflow, "_assert_layout"),
                patch.object(workflow, "_load_unit_manifest", return_value=manifest),
                patch.object(workflow, "_assert_fixed_output_names"),
                patch.object(
                    workflow,
                    "_load_discovery",
                    side_effect=lambda unused_layout, unused_manifest, lane: {
                        "lane": lane
                    },
                ),
                patch.object(workflow, "_load_json", return_value={}),
                patch.object(
                    workflow,
                    "_ensure_scope_composition",
                    side_effect=bind_composition,
                ),
                patch.object(workflow, "_load_contribution", return_value=None),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
            ):
                status = workflow.advance(args)

            self.assertEqual(status["stage"], "scope_composition")
            self.assertEqual(
                [row["role"] for row in status["handoffs"]],
                [f"{lane}_scope_composer" for lane in workflow.LANES],
            )
            self.assertTrue(
                all(row["same_live_agent"] for row in status["handoffs"])
            )
            self.assertTrue(
                all(
                    row["replacement_agent_allowed"]
                    for row in status["handoffs"]
                )
            )

    def test_prefatory_snapshot_and_origin_must_be_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "100:1", "100_1", root / "input", root / "raw", root / "editorial"
            )
            layout.input.mkdir()
            origin = root / "100_0.ayah.json"
            payload = workflow._canonical_json_bytes(basmala_bundle(), newline=True)
            origin.write_bytes(payload)
            layout.prefatory_basmala_bundle.write_bytes(payload)
            canonical = workflow.compositions.canonical_sha256(basmala_bundle())
            manifest = {
                "prefatory_basmala": {
                    "snapshot": workflow._path_record(
                        layout.prefatory_basmala_bundle
                    ),
                    "origin": workflow._source_path_record(origin),
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
                        "source_file": str(origin),
                        "lanes": ["macro"],
                    }],
                }
            }

            workflow._verify_prefatory_basmala_record(
                manifest, layout, numbered_bundle("100:1")
            )

            origin.write_text(
                json.dumps(basmala_bundle(), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            manifest["prefatory_basmala"]["origin"] = (
                workflow._source_path_record(origin)
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "no longer matches"):
                workflow._verify_prefatory_basmala_record(
                    manifest, layout, numbered_bundle("100:1")
                )

    def test_provided_docket_origin_is_reverified(self) -> None:
        source = (
            workflow.V3_ROOT
            / "inputs"
            / "adjudication"
            / "s001"
            / "1_1.docket.json"
        )
        docket = json.loads(source.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            origin = Path(tmp) / "docket.json"
            origin.write_bytes(source.read_bytes())
            lineage = {
                "kind": "provided",
                "source": workflow._source_path_record(origin),
            }
            workflow._verify_docket_lineage(
                lineage,
                source_origin={"path": "unused", "bytes": 0, "sha256": "0" * 64},
                source_bundle=numbered_bundle("1:1"),
                docket=docket,
            )

            origin.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(workflow.WorkflowError, "source changed"):
                workflow._verify_docket_lineage(
                    lineage,
                    source_origin={
                        "path": "unused",
                        "bytes": 0,
                        "sha256": "0" * 64,
                    },
                    source_bundle=numbered_bundle("1:1"),
                    docket=docket,
                )

    def test_manifest_reloads_the_original_focus_source(self) -> None:
        with tempfile.TemporaryDirectory(dir=workflow.V5_ROOT) as tmp:
            root = Path(tmp)
            source = root / "1_1.ayah.json"
            source.write_bytes(
                (workflow.REPO_ROOT / "bundles" / "s001" / "1_1.ayah.json").read_bytes()
            )
            args = workflow._parser().parse_args([
                "prepare",
                "--ayah",
                "1:1",
                "--source-bundle",
                str(source),
            ])
            args.ayah = "1:1"
            with (
                patch.object(workflow, "INPUT_ROOT", root / "input"),
                patch.object(workflow, "RAW_ROOT", root / "raw"),
                patch.object(workflow, "EDITORIAL_ROOT", root / "editorial"),
            ):
                workflow.prepare(args)
                layout = workflow.layout_for("1:1")
                workflow._load_unit_manifest(layout)
                source.write_bytes(source.read_bytes() + b"\n")
                with self.assertRaisesRegex(workflow.WorkflowError, "source changed"):
                    workflow._load_unit_manifest(layout)

    def test_added_ayah_duplicate_roots_are_rechecked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
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
            changed = numbered_bundle("17:50", text="changed")
            (member_root / "s017" / "17_50.ayah.json").write_text(
                json.dumps(changed), encoding="utf-8"
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "differs"):
                workflow._verify_added_ayah_root_agreement(analysis, selected)

    def test_host_surah_controls_mandatory_basmala(self) -> None:
        analysis = workflow.compositions.composition_from_cli(
            "s100-with-external",
            ["host=100:1"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )
        loaded = workflow._load_prefatory_basmala_context(
            numbered_bundle("100:1"), workflow.REPO_ROOT / "bundles", analysis
        )
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded[3]["ayah_ref"], "100:0")
        self.assertEqual(
            workflow._expected_context_lanes(analysis, "100:1", "100:0")["100:0"],
            ["macro"],
        )
        for ref in ("1:2", "9:1"):
            self.assertIsNone(
                workflow._load_prefatory_basmala_context(
                    numbered_bundle(ref), workflow.REPO_ROOT / "bundles", None
                )
            )


class CanonicalLandingTests(unittest.TestCase):
    def test_canonical_projection_and_ledger_do_not_reemit_internal_sources(self) -> None:
        results = scope_results()
        finding = results["micro"]["findings"][0]
        finding["semantic_inventory"][0]["source_summary"] = "x" * 200_000
        finding["unused_source_payload"] = "y" * 200_000
        results["micro"]["candidate_decisions"] = [{"reason": "z" * 200_000}]

        projection = workflow._canonical_lane_payload(results["micro"])
        ledger = workflow._finding_apparatus_ledger(results, finding)

        projection_text = workflow.v3._canonical_json(projection)
        ledger_text = workflow.v3._canonical_json(ledger)
        self.assertNotIn("unused_source_payload", projection_text)
        self.assertNotIn("candidate_decisions", projection_text)
        self.assertNotIn("composition_semantic_landings", projection_text)
        self.assertNotIn("source_sha256", projection_text)
        self.assertNotIn("x" * 1_000, ledger_text)
        self.assertNotIn("y" * 1_000, ledger_text)
        self.assertNotIn("z" * 1_000, ledger_text)
        self.assertLess(len(ledger_text), 10_000)

    def test_canonical_requirement_removes_prefatory_provenance_metadata(self) -> None:
        requirement = workflow._agent_semantic_requirement({
            "semantic_ref": "obligation:prefatory",
            "kind": "semantic_obligation",
            "source_sha256": "a" * 64,
            "source_summary": {
                "kind": "prefatory_evidence_section",
                "section": "v12_reader_walks",
                "support_id": "sup_internal",
                "semantic_payload": {
                    "reader_a": {
                        "source_file": "private/path.md",
                        "activated_readings_md": (
                            "Merhamet basligi yuruyusu yonlendirir."
                        ),
                    },
                },
            },
        })
        serialized = workflow.v3._canonical_json(requirement)

        self.assertIn("Merhamet basligi", serialized)
        self.assertNotIn("private/path", serialized)
        self.assertNotIn("sup_internal", serialized)

    def test_prefatory_compaction_preserves_semantic_metadata_named_fields(self) -> None:
        requirement = workflow._agent_semantic_requirement({
            "semantic_ref": "obligation:future",
            "kind": "semantic_obligation",
            "source_sha256": "a" * 64,
            "source_summary": {
                "kind": "prefatory_evidence_section",
                "section": "future_semantic_section",
                "semantic_payload": {
                    "language": "Dilin kendisi semantik tasiyicidir.",
                    "files": ["Katmanli yaprak imgesi."],
                    "protocol": "Rituel duzen okumanin konusudur.",
                    "source_file": "Kaynak dosya imgesi metnin anlamidir.",
                },
            },
        })
        payload = requirement["requirement"]["semantic_payload"]

        self.assertEqual(
            set(payload), {"language", "files", "protocol", "source_file"}
        )

    def test_known_prefatory_metadata_stripping_does_not_recurse(self) -> None:
        requirement = workflow._agent_semantic_requirement({
            "semantic_ref": "obligation:cross-run",
            "kind": "semantic_obligation",
            "source_sha256": "a" * 64,
            "source_summary": {
                "kind": "prefatory_evidence_section",
                "section": "v12_cross_run_publication",
                "semantic_payload": {
                    "language": "tr",
                    "protocol": "publication-v1",
                    "source_file": "internal.json",
                    "findings": [{
                        "language": "Dilin anlam ureten katmani.",
                        "files": "Yapraklar imgesi.",
                    }],
                },
            },
        })
        payload = requirement["requirement"]["semantic_payload"]

        self.assertNotIn("language", payload)
        self.assertNotIn("protocol", payload)
        self.assertNotIn("source_file", payload)
        self.assertEqual(
            payload["findings"][0]["language"],
            "Dilin anlam ureten katmani.",
        )

    def test_channel_manifest_metadata_is_removed_but_usage_is_retained(self) -> None:
        requirement = workflow._agent_semantic_requirement({
            "semantic_ref": "obligation:channel-manifest",
            "kind": "semantic_obligation",
            "source_sha256": "a" * 64,
            "source_summary": {
                "kind": "prefatory_evidence_section",
                "section": "channel_generated_outputs",
                "semantic_payload": {
                    "source_dir": "internal/channels",
                    "files": [{"path": "large.jsonl", "bytes": 99_000_000}],
                    "usage": "Kanal ailesi yalniz baglamsal kanit saglar.",
                },
            },
        })

        self.assertEqual(
            requirement["requirement"]["semantic_payload"],
            {"usage": "Kanal ailesi yalniz baglamsal kanit saglar."},
        )

    def test_oversized_semantic_record_is_rejected_before_handoff(self) -> None:
        with self.assertRaisesRegex(workflow.WorkflowError, "semantic record"):
            workflow._semantic_inventory_record(
                "discovery:claim",
                "discovery_field",
                "x" * workflow.MAX_SEMANTIC_RECORD_BYTES,
            )

    def test_shared_prose_landing_and_editorial_rewrite_are_allowed(self) -> None:
        results = scope_results()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            raw_prose = results["micro"]["findings"][0]["prose"]
            write_output_set(layout, results, phase="raw", prose=raw_prose)
            workflow._validate_canonical_outputs(layout, results, phase="raw")
            editorial_prose = (
                "Iki bulgu, ayni Turkce paragrafta mekanizmalari acik kalacak "
                "bicimde daha akici olarak bir araya gelir."
            )
            write_output_set(
                layout, results, phase="editorial", prose=editorial_prose
            )
            workflow._validate_canonical_outputs(
                layout, results, phase="editorial"
            )

    def test_final_reader_prose_rejects_english_leakage(self) -> None:
        results = scope_results()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            prose = results["micro"]["findings"][0]["prose"]
            write_output_set(layout, results, phase="raw", prose=prose)
            layout.first_pass("prose").write_text(
                prose + "\nThis is the sentence that leaked into the prose.",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "English"):
                workflow._validate_canonical_outputs(layout, results, phase="raw")

    def test_all_human_output_surfaces_reject_english_leakage(self) -> None:
        results = scope_results()
        for kind, sentence in (
            ("evidence", "This is English evidence for the reader."),
            ("index", "This is an English index sentence for the reader."),
            ("friction", "This is an English friction note for the reader."),
        ):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                layout = workflow.Layout(
                    "1:1", "1_1", root / "input", root / "raw", root / "editorial"
                )
                prose = results["micro"]["findings"][0]["prose"]
                write_output_set(layout, results, phase="raw", prose=prose)
                path = layout.first_pass(kind)
                text = path.read_text(encoding="utf-8")
                if kind == "index":
                    text = text.replace(
                        "```commentary-v5-landing-map",
                        sentence + "\n```commentary-v5-landing-map",
                        1,
                    )
                else:
                    text += "\n" + sentence
                path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(workflow.WorkflowError, "English"):
                    workflow._validate_canonical_outputs(
                        layout, results, phase="raw"
                    )

    def test_oversized_apparatus_output_is_rejected(self) -> None:
        results = scope_results()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            prose = results["micro"]["findings"][0]["prose"]
            write_output_set(layout, results, phase="raw", prose=prose)
            layout.first_pass("evidence").write_text(
                "ve " * (workflow.CANONICAL_OUTPUT_BYTE_LIMITS["evidence"] // 2),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "output budget"):
                workflow._validate_canonical_outputs(
                    layout, results, phase="raw"
                )

    def test_landing_map_cannot_change_semantic_ref(self) -> None:
        results = scope_results()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            layout = workflow.Layout(
                "1:1", "1_1", root / "input", root / "raw", root / "editorial"
            )
            prose = results["micro"]["findings"][0]["prose"]
            write_output_set(layout, results, phase="raw", prose=prose)
            index_path = layout.first_pass("index")
            index_text = index_path.read_text(encoding="utf-8")
            index_path.write_text(
                index_text.replace(
                    '"discovery:claim"',
                    '"discovery:forged"',
                    1,
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(workflow.WorkflowError, "unknown semantic"):
                workflow._validate_canonical_outputs(layout, results, phase="raw")


if __name__ == "__main__":
    unittest.main()
