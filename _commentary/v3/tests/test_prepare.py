from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


V3_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = V3_ROOT / "workflow.py"
REAL_S29_BUNDLE = V3_ROOT.parents[1] / "bundles/s029/29_38.ayah.json"
REAL_S29_39_BUNDLE = V3_ROOT.parents[1] / "bundles/s029/29_39.ayah.json"

import sys

sys.path.insert(0, str(V3_ROOT))

from v3lib.common import (  # noqa: E402
    ArtifactConflictError,
    PathConfinementError,
    ScopeError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    confined_destination,
    load_json_object,
    pretty_json_bytes,
    sha256_bytes,
    write_json_confined,
)
from v3lib.prepare import (  # noqa: E402
    BranchResolver,
    PrepareOptions,
    _branch_registry,
    _branch_review_grounding_gaps,
    _extract_branch_refs,
    _stable_id,
    build_prepared_artifacts,
    prepare_bundle_file,
    support_role_for,
    validate_docket,
    validate_prepared,
)


def branch(root_id: str, branch_id: str, gloss: str) -> dict:
    return {
        "branch_ref": f"{root_id}/{branch_id}",
        "identity_judgment": {
            "status": "accepted",
            "boundary_note": f"boundary for {gloss}",
        },
        "lexicalization_scope": {"branch_kind": "bare"},
        "concept_gloss": {"text": gloss},
    }


def root_record(root_id: str, root_ar: str, branches: list[dict]) -> dict:
    return {
        "root_id": root_id,
        "root_ar": root_ar,
        "qac_roots_ar": [root_ar],
        "root_mapping_role": "dominant",
        "dictionary_entry": {"branches": branches},
    }


def fixture_bundle(
    *,
    valid_hft: bool = False,
    bind_hft: bool = False,
    surah_hft: bool = False,
) -> dict:
    pericope_refs = [f"29:{ayah}" for ayah in range(28, 45)]
    hft_window = (
        [f"29:{ayah}" for ayah in range(1, 70)]
        if surah_hft or not valid_hft
        else pericope_refs
    )
    hft_protocol = (
        "focus-trace-surah-lean-v1"
        if surah_hft
        else "focus-trace-pericope-lean-v1"
    )
    return {
        "schema_version": "input-bundle-v3",
        "bundle_type": "ayah",
        "ayahRef": "29:38",
        "surah": 29,
        "ayah": 38,
        "text": {"arabic_uthmani": "TEST"},
        "pericope": {
            "surah": 29,
            "pericope": 3,
            "ayah_from": 28,
            "ayah_to": 44,
            "label": "test pericope",
        },
        "qac_morphemes": [
            {
                "qac_ref": "29:38:1:1",
                "qac_word_ref": "29:38:1",
                "surface_ar": "أَعْمَالَهُمْ",
                "lemma_ar": "عَمَل",
                "root_ar": "ع م ل",
                "pos": "N",
                "morpheme_role": "STEM",
                "morph_features": "N",
            },
            {
                "qac_ref": "29:38:2:1",
                "qac_word_ref": "29:38:2",
                "surface_ar": "السَّبِيلِ",
                "lemma_ar": "سَبِيل",
                "root_ar": "س ب ل",
                "pos": "N",
                "morpheme_role": "STEM",
                "morph_features": "N",
            },
            {
                "qac_ref": "29:38:3:1",
                "qac_word_ref": "29:38:3",
                "surface_ar": "مُسْتَبْصِرِينَ",
                "lemma_ar": "مُسْتَبْصِر",
                "root_ar": "ب ص ر",
                "pos": "N",
                "morpheme_role": "STEM",
                "morph_features": "N",
            },
        ],
        "root_lexicon": {
            "root_001046": root_record(
                "root_001046",
                "ع م ل",
                [
                    branch("root_001046", "B001", "intentional work"),
                    branch("root_001046", "B011", "worked road"),
                ],
            ),
            "root_000672": root_record(
                "root_000672",
                "س ب ل",
                [
                    branch("root_000672", "B001", "road"),
                    branch("root_000672", "B010", "web-like eye film"),
                ],
            ),
            "root_000121": root_record(
                "root_000121",
                "ب ص ر",
                [branch("root_000121", "B001", "ocular sight")],
            ),
        },
        "word_analysis": {
            "words": [
                {
                    "aligned_qac_word_ref": "29:38:1",
                    "surface_display": "works",
                    "root_display": "ع م ل",
                    "gloss_range": "works",
                    "root_gloss_range": "intentional work",
                    "prose": "The word names their works.",
                    "topics": [
                        {
                            "topic_id": "29:38:1:work",
                            "headline": "works are evaluated",
                            "status": "used",
                            "reader_payoff": "The reader sees evaluated work.",
                            "reason": "Local grammar supports it.",
                            "commentary_obligation": "must_integrate",
                            "representative_source_ids": ["Q1"],
                        }
                    ],
                },
                {
                    "aligned_qac_word_ref": "29:38:2",
                    "surface_display": "yol",
                    "root_display": "س ب ل",
                    "gloss_range": "yol",
                    "root_gloss_range": "س ب ل",
                    "prose": "Yol kokune bagli odak delili.",
                    "topics": [
                        {
                            "topic_id": "29:38:2:ground-root_000672",
                            "headline": "Yol kokunun yerel kullanimi",
                            "status": "used",
                            "reader_payoff": "Kok dali odak kelimeye baglanir.",
                            "reason": "Odak morfolojisi kok eslemesini destekler.",
                            "commentary_obligation": "ledger_only",
                            "representative_source_ids": ["Q1"],
                        }
                    ],
                },
                {
                    "aligned_qac_word_ref": "29:38:3",
                    "surface_display": "gorenler",
                    "root_display": "ب ص ر",
                    "gloss_range": "gorenler",
                    "root_gloss_range": "ب ص ر",
                    "prose": "Gorme kokune bagli odak delili.",
                    "topics": [
                        {
                            "topic_id": "29:38:3:ground-root_000121",
                            "headline": "Gorme kokunun yerel kullanimi",
                            "status": "used",
                            "reader_payoff": "Kok dali odak kelimeye baglanir.",
                            "reason": "Odak morfolojisi kok eslemesini destekler.",
                            "commentary_obligation": "ledger_only",
                            "representative_source_ids": ["Q1"],
                        }
                    ],
                },
            ]
        },
        "channel_subchannels_anchored_here": [
            {
                "key": "A",
                "name": "Cutting the Worked Road",
                "reading_type": "mixed",
                "scene_or_process": "A worked road is obstructed.",
                "synthesis": "Their own work meets the road that is blocked.",
                "active_motifs": (
                    "a worked road `quranic:root_001046:B011/m01`; "
                    "a route `quranic:root_000672:B001/m01`"
                ),
                "ayah_refs": ["29:29", "29:38"],
                "ayah_anchors": "ع م ل 29:38; س ب ل 29:38",
                "parent_semantic_invariant": "Public movement is obstructed.",
            }
        ],
        "v12_focus_trace_hermetic": {
            "packet_summary": {
                "source_file": "focus.packet.json",
                "protocol": hft_protocol,
                "window_scope": "surah" if surah_hft else None,
                "focus_ref": "29:38",
                "window": hft_window,
                "ayah_count": len(hft_window),
            },
            "readers": {
                "reader_hft_a": {
                    "protocol": "focus-trace-hermetic-response-v4",
                    "focus_ref": "29:38",
                    "packet_identity": (
                        {
                            "focus_ref": "29:38",
                            "protocol": hft_protocol,
                            "window_sha256": canonical_sha256(hft_window),
                        }
                        if bind_hft
                        else None
                    ),
                    "baseline_models": [],
                    "context_deltas": [],
                    "surprising_valid_outliers": [
                        {
                            "outlier_id": "outlier_webbed_path",
                            "confidence": "exploratory",
                            "focus_anchor": "path and sight",
                            "containment": "Not a lexical translation.",
                            "activation_trace": [
                                {
                                    "source_ref": "29:38",
                                    "mapped_root_id": "root_000672",
                                    "branch_id": "B010",
                                    "role": "web-like eye film",
                                },
                                {
                                    "source_ref": "29:38",
                                    "mapped_root_id": "root_000121",
                                    "branch_id": "B001",
                                    "role": "ocular sight",
                                },
                            ],
                            "changed_reading": {
                                "before": "road block",
                                "after": "web-like visual obstruction",
                            },
                        }
                    ],
                }
            },
        },
        "v12_reader_walks": {},
        "v12_reader_walks_wide": {},
        "v12_cross_run_publication": {},
        "v12_reader_responses": {},
    }


class PrepareTests(unittest.TestCase):
    def test_authoring_retains_unresolved_word_topic_without_changing_obligation(self) -> None:
        bundle = fixture_bundle()
        topic = bundle["word_analysis"]["words"][0]["topics"][0]
        topic["reason"] = "Check the unregistered root_001046/B999 citation."
        original = copy.deepcopy(bundle)
        with self.assertRaisesRegex(ValidationError, "unresolved branch evidence"):
            build_prepared_artifacts(bundle, source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"))
        _prepared, docket = build_prepared_artifacts(
            bundle, source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine",
                demote_unresolved_mandatory_candidates=True))
        candidate = next(item for item in docket["candidates"]
                         if item["source_local_id"] == topic["topic_id"])
        self.assertEqual(candidate["obligation"], "must_integrate")
        self.assertFalse(candidate["mandatory"])
        self.assertFalse(candidate["adjudicable"])
        self.assertFalse(candidate["selection_eligible"])
        self.assertTrue(candidate["unresolved_branch_citations"])
        self.assertEqual(bundle, original)

    def test_missing_word_morpheme_spans_cannot_fall_back_to_upstream_refs(self) -> None:
        bundle = fixture_bundle()
        bundle.pop("word_morpheme_spans", None)
        bundle["word_analysis"]["words"][1]["aligned_qac_word_ref"] = "29:38:1"
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(
            docket["focus"]["word_analysis_qac_refs"],
            [[], [], []],
        )

    def test_present_null_word_morpheme_spans_is_not_legacy_absence(self) -> None:
        bundle = fixture_bundle()
        bundle["word_morpheme_spans"] = None
        with self.assertRaisesRegex(ValidationError, "one-for-one"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_source_ayah_ref_must_be_canonical(self) -> None:
        bundle = fixture_bundle()
        bundle["ayahRef"] = "029:038"
        with self.assertRaisesRegex(ValidationError, "canonical unpadded"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_model_visible_qac_rows_fail_closed_before_docket_build(self) -> None:
        for root_value in (None, 123):
            with self.subTest(root_value=root_value):
                bundle = fixture_bundle()
                bundle["qac_morphemes"][0]["root_ar"] = root_value
                with self.assertRaisesRegex(
                    ValidationError, "linguistic fields must all be strings"
                ):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="quarantine"),
                    )
        missing = fixture_bundle()
        del missing["qac_morphemes"][0]["root_ar"]
        with self.assertRaisesRegex(
            ValidationError, "linguistic fields must all be strings"
        ):
            build_prepared_artifacts(
                missing,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_qac_docket_schema_matches_runtime_projection(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        schema = json.loads(
            (V3_ROOT / "schemas/docket.schema.json").read_text(encoding="utf-8")
        )
        qac_schema = schema["$defs"]["qacMorpheme"]
        expected_fields = {
            "qac_ref",
            "qac_word_ref",
            "surface_ar",
            "lemma_ar",
            "root_ar",
            "pos",
            "morpheme_role",
            "morph_features",
        }
        self.assertEqual(set(qac_schema["required"]), expected_fields)
        self.assertEqual(set(qac_schema["properties"]), expected_fields)
        self.assertFalse(qac_schema["additionalProperties"])
        self.assertEqual(
            set(docket["focus"]["qac_morphemes"][0]), expected_fields
        )
        qac_array = schema["properties"]["focus"]["properties"]["qac_morphemes"]
        self.assertEqual(qac_array["items"]["$ref"], "#/$defs/qacMorpheme")
        self.assertEqual(qac_array["minItems"], 1)

    def test_qac_refs_are_ascii_only_and_runtime_requires_a_carrier(self) -> None:
        for field, value in (
            ("qac_word_ref", "29:38:1١"),
            ("qac_ref", "29:38:1:1١"),
        ):
            with self.subTest(field=field):
                bundle = fixture_bundle()
                bundle["qac_morphemes"][0][field] = value
                if field == "qac_word_ref":
                    bundle["qac_morphemes"][0]["qac_ref"] = "29:38:1١:1"
                with self.assertRaisesRegex(
                    ValidationError, "invalid or duplicate canonical refs"
                ):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="quarantine"),
                    )

        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        empty = copy.deepcopy(docket)
        empty["focus"]["qac_morphemes"] = []
        payload = copy.deepcopy(empty)
        payload["identity"].pop("docket_payload_sha256")
        empty["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "must not be empty"):
            validate_docket(empty)

    def test_pericope_number_requires_a_positive_json_integer(self) -> None:
        for value in (None, [], {}, "", "17", 17.5, True, 0, -1):
            with self.subTest(value=value):
                bundle = fixture_bundle()
                bundle["pericope"]["pericope"] = value
                with self.assertRaisesRegex(
                    ValidationError, "pericope number must be a positive integer"
                ):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="quarantine"),
                    )

    def test_pericope_width_is_bounded_before_ref_materialization(self) -> None:
        bundle = fixture_bundle()
        bundle["pericope"]["ayah_from"] = 1
        bundle["pericope"]["ayah_to"] = 10_000_000
        with self.assertRaisesRegex(ScopeError, "10000000 ayahs; limit is 512"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        forged = copy.deepcopy(docket)
        forged["scope"]["pericope"]["ayah_to"] = 10_000_000
        forged["scope"]["pericope"]["refs"] = []
        forged["limits"]["max_pericope_ayahs"] = 10_000_000
        payload = copy.deepcopy(forged)
        payload["identity"].pop("docket_payload_sha256")
        forged["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with patch(
            "v3lib.prepare.range",
            side_effect=AssertionError("range must not be called"),
            create=True,
        ):
            with self.assertRaisesRegex(ValidationError, "hard safety cap"):
                validate_docket(forged)

    def test_branch_registry_normalizes_qac_root_aliases(self) -> None:
        bundle = {
            "qac_morphemes": [{"root_ar": "ج ي أ"}],
            "root_lexicon": {
                "root_000282": root_record(
                    "root_000282",
                    "ج ي ء",
                    [branch("root_000282", "B001", "coming")],
                )
            },
        }
        roots, refs, mappings, gaps = _branch_registry(
            bundle, max_bytes_per_root=32_000
        )
        self.assertEqual(mappings, {"ج ي أ": ["root_000282"]})
        self.assertEqual(refs, {"root_000282/B001"})
        self.assertEqual(roots[0]["qac_roots_ar"], ["ج ي ء"])
        self.assertEqual(gaps, [])

        full_bundle = fixture_bundle()
        next(
            row
            for row in full_bundle["qac_morphemes"]
            if row.get("root_ar") == "ب ص ر"
        )["root_ar"] = "ب ص أ"
        root = full_bundle["root_lexicon"]["root_000121"]
        root["root_ar"] = "ب ص ء"
        root["qac_roots_ar"] = ["ب ص ء"]
        full_bundle["word_analysis"]["words"].append(
            {
                "aligned_qac_word_ref": "29:38:3",
                "surface_display": "gorenler",
                "root_display": "ب ص أ",
                "gloss_range": "gorenler",
                "root_gloss_range": "gorme",
                "prose": "Gorme kokune bagli odak delili.",
                "topics": [
                    {
                        "topic_id": "29:38:3:alias-grounding",
                        "headline": "Alias kok eslemesi",
                        "status": "used",
                        "reader_payoff": "Kok dali odak kelimeye baglanir.",
                        "reason": "QAC ve sozluk yazimlari kanonik olarak eslesir.",
                        "commentary_obligation": "ledger_only",
                        "representative_source_ids": ["Q1"],
                    }
                ],
            }
        )
        _prepared, docket = build_prepared_artifacts(
            full_bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(docket["focus_root_mappings"]["ب ص أ"], ["root_000121"])
        grounded = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_type"] == "qac_morpheme"
            and "root_000121" in candidate["root_ids"]
        )
        self.assertEqual(grounded["root_ids"], ["root_000121"])

        root["dictionary_entry"] = None
        prepared, gap_docket = build_prepared_artifacts(
            full_bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="quarantine",
                allow_incomplete_branch_coverage=True,
            ),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        self.assertEqual(
            gap_docket["scope"]["branch_coverage"]["missing_dictionary_roots"][0][
                "qac_roots_ar"
            ],
            ["ب ص أ"],
        )

    def test_branch_ref_extraction_requires_token_boundaries(self) -> None:
        self.assertEqual(
            _extract_branch_refs(
                "root_1/B001 xroot_2/B002 root_3/B003x root_4:B004"
            ),
            ["root_1/B001", "root_4/B004"],
        )
        self.assertEqual(
            _extract_branch_refs(
                "قroot_000672/B010 root_000672/B010س root_000672/B010"
            ),
            ["root_000672/B010"],
        )
        self.assertEqual(
            _extract_branch_refs(
                "root_1/B001\u0301 root_2/B002\u200d root_3/B003\ufe0f "
                "root_4/B004\u203f \u0301root_5/B005 \u200droot_6/B006"
            ),
            [],
        )

    def test_arabic_root_branch_scan_requires_grapheme_boundaries(self) -> None:
        resolver = BranchResolver(
            root_ids_by_arabic={"ب ص ر": ["root_000672"]},
            available_branch_refs={"root_000672/B001"},
        )
        self.assertEqual(
            resolver.resolve_text("ب ص ر B001")[0],
            ["root_000672/B001"],
        )
        for text in (
            "كب ص ر B001",
            "ب ص ر\u0301 B001",
            "ب ص ر bad\u0301and B001",
            "ب ص ر bad\u200dand B001",
            "ب ص ر bad\ufe0fand B001",
            "ب ص ر bad\u203fand B001",
        ):
            with self.subTest(text=text):
                self.assertEqual(resolver.resolve_text(text)[0], [])
        self.assertEqual(resolver.root_ids_in_text("كب ص ر"), [])

    def test_explicit_empty_grounding_map_does_not_fall_back_to_inventory(self) -> None:
        resolver = BranchResolver(
            root_ids_by_arabic={"ج ي ء": ["root_000282"]},
            grounding_root_ids_by_arabic={},
            available_branch_refs={"root_000282/B001"},
        )
        self.assertEqual(resolver.root_ids_in_text("ج ي أ"), [])
        self.assertEqual(
            resolver.resolve_text("ج ي أ B001")[0],
            ["root_000282/B001"],
        )

    def test_native_furuq_root_precedes_qac_split_targets(self) -> None:
        split_targets = ["root_000743", "root_000745", "root_001650"]
        resolver = BranchResolver(
            root_ids_by_arabic={"س م و": split_targets},
            native_branch_refs_by_arabic={
                "س م م": {"B004": ["root_000743/B004"]},
                "س م و": {"B004": ["root_000745/B004"]},
                "و س م": {"B004": ["root_001650/B004"]},
            },
            available_branch_refs={
                f"{root_id}/B004" for root_id in split_targets
            },
        )

        self.assertEqual(
            resolver.resolve_text("the overhead sky `س م و:B004/m01`"),
            (["root_000745/B004"], []),
        )
        self.assertEqual(
            resolver.root_ids_in_text("س م و"),
            split_targets,
        )

        ambiguous = BranchResolver(
            root_ids_by_arabic={"س م و": split_targets},
            native_branch_refs_by_arabic={
                "س م و": {
                    "B004": ["root_000745/B004", "root_009999/B004"]
                },
            },
            available_branch_refs={"root_000745/B004", "root_009999/B004"},
        )
        resolved, unresolved = ambiguous.resolve_text("س م و:B004")
        self.assertEqual(resolved, [])
        self.assertEqual(
            unresolved,
            [
                {
                    "citation": "س م و/B004",
                    "reason": (
                        "ambiguous root mapping: "
                        "root_000745/B004, root_009999/B004"
                    ),
                }
            ],
        )
        expanded = BranchResolver(
            root_ids_by_arabic={"س م و": split_targets},
            native_branch_refs_by_arabic={
                "س م و": {
                    "B004": ["root_000745/B004", "root_009999/B004"]
                },
            },
            available_branch_refs={"root_000745/B004", "root_009999/B004"},
            expand_ambiguous_native_branches=True,
        )
        self.assertEqual(
            expanded.resolve_text("س م و:B004"),
            (
                ["root_000745/B004", "root_009999/B004"],
                [
                    {
                        "citation": "س م و/B004",
                        "reason": (
                            "ambiguous root mapping expanded as alternatives: "
                            "root_000745/B004, root_009999/B004"
                        ),
                    }
                ],
            ),
        )

    def test_unknown_explicit_branch_is_diagnostic_not_support_metadata(self) -> None:
        bundle = fixture_bundle()
        topic = bundle["word_analysis"]["words"][1]["topics"][0]
        topic["reason"] += " Explicit root_999999/B999 citation."
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        candidate = next(
            item
            for item in docket["candidates"]
            if item["source_local_id"] == topic["topic_id"]
        )
        self.assertFalse(candidate["adjudicable"])
        self.assertEqual(
            candidate["unresolved_branch_citations"],
            [
                {
                    "citation": "root_999999/B999",
                    "reason": "no registered branch match",
                }
            ],
        )
        self.assertFalse(
            any(
                "root_999999/B999" in support["branch_refs"]
                for support in docket["support_registry"]
            )
        )
        self.assertTrue(prepared["readiness"]["ready"])

        for source_kind in ("word_prose", "channel_evidence"):
            with self.subTest(source_kind=source_kind):
                malformed = fixture_bundle()
                if source_kind == "word_prose":
                    malformed["word_analysis"]["words"][0][
                        "prose"
                    ] += " Explicit root_999999/B999 citation."
                else:
                    malformed["channel_subchannels_anchored_here"][0][
                        "scene_or_process"
                    ] += " Explicit root_999999/B999 citation."
                with self.assertRaisesRegex(
                    ValidationError, "unresolved branch evidence"
                ):
                    build_prepared_artifacts(
                        malformed,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="quarantine"),
                    )

    def test_strict_rejects_hft_scope_mismatch(self) -> None:
        bundle = fixture_bundle()
        with self.assertRaises(ScopeError) as caught:
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        self.assertIn("does not exactly match", str(caught.exception))
        self.assertEqual(caught.exception.report["status"], "invalid")

    def test_quarantine_is_diagnostic_only_and_worked_route_survives(self) -> None:
        prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertTrue(prepared["mandatory_candidates_ready"])
        quarantine = prepared["diagnostics"]["quarantined_hft"]
        self.assertFalse(quarantine["visible_to_adjudication"])
        self.assertEqual(
            quarantine["seeds"][0]["source_local_id"],
            "reader_hft_a:outlier_webbed_path",
        )
        self.assertFalse(
            any(candidate["source_type"] == "hft" for candidate in docket["candidates"])
        )
        worked = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["title"] == "Cutting the Worked Road"
        )
        self.assertIn("root_001046/B011", worked["branch_refs"])
        self.assertFalse(
            any(
                candidate["source_local_id"].endswith("outlier_webbed_path")
                for candidate in docket["candidates"]
            )
        )

    def test_every_focus_root_branch_is_registered(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        refs = {
            branch_item["branch_ref"]
            for root in docket["branch_registry"]
            for branch_item in root["branches"]
        }
        self.assertEqual(
            refs,
            {
                "root_001046/B001",
                "root_001046/B011",
                "root_000672/B001",
                "root_000672/B010",
                "root_000121/B001",
            },
        )

    def test_support_roles_are_canonical_and_provenance_closed(self) -> None:
        bundle = fixture_bundle()
        bundle["v12_reader_responses"] = {
            "legacy-a": "Legacy whole-reading context without a branch claim."
        }
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        roles = {
            (item["source_type"], item["json_pointer"]): item["role"]
            for item in docket["support_registry"]
        }
        self.assertEqual(
            roles[("word_analysis", "/word_analysis/words/0")],
            "candidate_evidence",
        )
        self.assertEqual(
            roles[("qac_morpheme", "/qac_morphemes/0")],
            "focus_occurrence",
        )
        self.assertEqual(
            roles[("word_analysis", "/word_analysis/words/0/topics/0")],
            "candidate_evidence",
        )
        self.assertEqual(
            roles[("channel", "/channel_subchannels_anchored_here/0/active_motifs")],
            "branch_nomination",
        )
        self.assertEqual(
            roles[("channel", "/channel_subchannels_anchored_here/0/synthesis")],
            "candidate_evidence",
        )
        self.assertEqual(
            roles[("channel", "/channel_subchannels_anchored_here/0/ayah_anchors")],
            "context_only",
        )
        self.assertEqual(
            roles[("legacy_reader_response", "/v12_reader_responses/legacy-a")],
            "context_only",
        )

        malformed = copy.deepcopy(docket)
        malformed["support_registry"][0]["role"] = "context_only"
        payload = copy.deepcopy(malformed)
        payload["identity"].pop("docket_payload_sha256")
        malformed["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "canonical provenance"):
            validate_docket(malformed)

        for source_type, pointer in (
            (
                "channel",
                "/channel_subchannels_anchored_here/0/active_motifs/forged",
            ),
            (
                "channel_alias",
                "/channel_subchannels_anchored_here/0/active_motifs",
            ),
        ):
            with self.assertRaisesRegex(ValidationError, "Unsupported support provenance"):
                support_role_for(source_type, pointer)

    def test_candidate_and_support_identity_cover_all_semantic_fields(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        candidate_mutation = copy.deepcopy(docket)
        candidate_mutation["candidates"][0]["title"] = "forged title"
        payload = copy.deepcopy(candidate_mutation)
        payload["identity"].pop("docket_payload_sha256")
        candidate_mutation["identity"]["docket_payload_sha256"] = canonical_sha256(
            payload
        )
        with self.assertRaisesRegex(ValidationError, "Candidate .* identity hash"):
            validate_docket(candidate_mutation)

        support_mutation = copy.deepcopy(docket)
        support_mutation["support_registry"][0]["citable"] = False
        payload = copy.deepcopy(support_mutation)
        payload["identity"].pop("docket_payload_sha256")
        support_mutation["identity"]["docket_payload_sha256"] = canonical_sha256(
            payload
        )
        with self.assertRaisesRegex(ValidationError, "Support identity hash"):
            validate_docket(support_mutation)

    def test_candidate_set_like_arrays_require_canonical_order(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        malformed = copy.deepcopy(docket)
        candidate = next(
            item for item in malformed["candidates"] if len(item["support_ids"]) > 1
        )
        candidate["support_ids"].reverse()
        candidate["candidate_id"] = _stable_id(
            "cand",
            {
                "ayah_ref": malformed["identity"]["ayah_ref"],
                "lane": candidate["lane"],
                "source_type": candidate["source_type"],
                "source_local_id": candidate["source_local_id"],
                "source_pointer": candidate["source_pointer"],
                "kind": candidate["kind"],
                "title": candidate["title"],
                "mandatory": candidate["mandatory"],
                "obligation": candidate["obligation"],
                "scope": candidate["scope"],
                "trust": candidate["trust"],
                "branch_refs": candidate["branch_refs"],
                "root_ids": candidate["root_ids"],
                "unresolved_branch_citations": candidate[
                    "unresolved_branch_citations"
                ],
                "anchor_refs": candidate["anchor_refs"],
                "support_ids": candidate["support_ids"],
            },
        )
        payload = copy.deepcopy(malformed)
        payload["identity"].pop("docket_payload_sha256")
        malformed["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "noncanonical"):
            validate_docket(malformed)

    def test_malformed_source_discriminators_raise_validation_errors(self) -> None:
        bundle = fixture_bundle()
        bundle["surah"] = []
        with self.assertRaises(ValidationError):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

        bundle = fixture_bundle()
        bundle["word_analysis"]["words"][0]["topics"][0][
            "commentary_obligation"
        ] = []
        prepared, _docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertGreaterEqual(
            prepared["coverage"]["by_disposition"]["parse_failed"], 1
        )

    def test_missing_focus_dictionary_is_explicit_degraded_coverage(self) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000121"]["dictionary_entry"] = None
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        coverage = docket["scope"]["branch_coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(
            coverage["missing_dictionary_roots"][0]["root_id"], "root_000121"
        )
        missing_root = next(
            item for item in docket["branch_registry"] if item["root_id"] == "root_000121"
        )
        self.assertEqual(missing_root["branches"], [])
        self.assertIn(
            "branch surprise coverage is incomplete",
            " ".join(prepared["readiness"]["warnings"]),
        )
        self.assertEqual(
            prepared["diagnostics"]["focus_root_dictionary_gaps"],
            coverage["missing_dictionary_roots"],
        )
        self.assertFalse(prepared["readiness"]["ready"])
        self.assertIn(
            "branch_coverage/incomplete",
            prepared["readiness"]["blocker_counts"],
        )

        authorized, authorized_docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="quarantine",
                allow_incomplete_branch_coverage=True,
            ),
        )
        self.assertTrue(authorized["readiness"]["ready"])
        self.assertTrue(
            authorized_docket["adjudication_gate"][
                "incomplete_branch_coverage_authorized"
            ]
        )

    def test_missing_or_empty_focus_dictionary_is_not_degraded_silently(self) -> None:
        missing = fixture_bundle()
        del missing["root_lexicon"]["root_000121"]["dictionary_entry"]
        with self.assertRaisesRegex(ValidationError, "lacks dictionary_entry"):
            build_prepared_artifacts(
                missing,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

        empty = fixture_bundle()
        empty["root_lexicon"]["root_000121"]["dictionary_entry"] = {
            "branches": []
        }
        with self.assertRaisesRegex(ValidationError, "branches must not be empty"):
            build_prepared_artifacts(
                empty,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_unmapped_focus_root_is_explicit_degraded_coverage(self) -> None:
        bundle = fixture_bundle()
        del bundle["root_lexicon"]["root_000121"]
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        coverage = docket["scope"]["branch_coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(
            coverage["missing_dictionary_roots"][0],
            {
                "root_id": None,
                "root_ar": "ب ص ر",
                "qac_roots_ar": ["ب ص ر"],
                "reason": "no root_lexicon mapping for this QAC focus root",
            },
        )
        self.assertFalse(prepared["readiness"]["ready"])
        self.assertIn(
            "branch_coverage/incomplete",
            prepared["readiness"]["blocker_counts"],
        )

        authorized, authorized_docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="quarantine",
                allow_incomplete_branch_coverage=True,
            ),
        )
        self.assertTrue(authorized["readiness"]["ready"])
        self.assertTrue(
            authorized_docket["adjudication_gate"][
                "incomplete_branch_coverage_authorized"
            ]
        )

    def test_mandatory_candidate_cannot_cite_branch_from_null_dictionary(self) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000121"]["dictionary_entry"] = None
        bundle["word_analysis"]["words"].append(
            {
                "aligned_qac_word_ref": "29:38:3",
                "surface_display": "sight",
                "root_display": "ب ص ر",
                "gloss_range": "sight",
                "root_gloss_range": "ب ص ر",
                "prose": "Sight evidence.",
                "topics": [
                    {
                        "topic_id": "29:38:3:unavailable-branch",
                        "headline": "Unavailable branch claim",
                        "status": "used",
                        "reader_payoff": "Tests branch grounding.",
                        "reason": "ب ص ر B001 is required.",
                        "commentary_obligation": "must_integrate",
                        "representative_source_ids": ["Q2"],
                    }
                ],
            }
        )
        with self.assertRaisesRegex(ValidationError, "unresolved branch evidence"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(
                    hft_policy="quarantine",
                    allow_incomplete_branch_coverage=True,
                ),
            )

    def test_nomination_only_mandatory_channel_blocks_preparation(self) -> None:
        bundle = fixture_bundle()
        channel = bundle["channel_subchannels_anchored_here"][0]
        channel["scene_or_process"] = None
        channel["synthesis"] = None
        with self.assertRaisesRegex(
            ValidationError, "not selection eligible.*no_candidate_evidence"
        ):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_malformed_nonnull_focus_dictionary_still_fails(self) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000121"]["dictionary_entry"] = "invalid"
        with self.assertRaisesRegex(ValidationError, "dictionary_entry must be an object"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

    def test_branch_coverage_accounting_cannot_be_recomputed_inconsistently(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        malformed = copy.deepcopy(docket)
        malformed["scope"]["branch_coverage"]["registered_branch_count"] += 1
        payload = copy.deepcopy(malformed)
        payload["identity"].pop("docket_payload_sha256")
        malformed["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "coverage accounting"):
            validate_docket(malformed)

    def test_docket_coverage_maps_reject_forged_keys_and_counts(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        mutations = (
            lambda value: value["coverage"]["by_disposition"].update(
                forged="not-a-count"
            ),
            lambda value: value["coverage"]["by_disposition"].update(
                quarantined=True
            ),
            lambda value: value["coverage"]["by_source_type"].update(
                forged=-1
            ),
        )
        for mutation in mutations:
            malformed = copy.deepcopy(docket)
            mutation(malformed)
            payload = copy.deepcopy(malformed)
            payload["identity"].pop("docket_payload_sha256")
            malformed["identity"]["docket_payload_sha256"] = canonical_sha256(
                payload
            )
            with self.assertRaisesRegex(ValidationError, "counts are invalid"):
                validate_docket(malformed)

    def test_runtime_rejects_schema_invalid_branch_records_with_recomputed_hash(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        for mutate, message in (
            (
                lambda value: value["branch_registry"][0]["branches"][0].update(
                    branch_ref="root_001046/BAD"
                ),
                "canonical branch ref",
            ),
            (
                lambda value: value["nominated_branch_registry"].append(
                    {"branch_ref": "evil"}
                ),
                "fields disagree with contract",
            ),
        ):
            malformed = copy.deepcopy(docket)
            mutate(malformed)
            payload = copy.deepcopy(malformed)
            payload["identity"].pop("docket_payload_sha256")
            malformed["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
            with self.assertRaisesRegex(ValidationError, message):
                validate_docket(malformed)

    def test_focus_branch_gloss_is_required_for_branch_review(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        malformed = copy.deepcopy(docket)
        malformed["branch_registry"][0]["branches"][0]["gloss"] = None
        payload = copy.deepcopy(malformed)
        payload["identity"].pop("docket_payload_sha256")
        malformed["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "gloss is missing"):
            validate_docket(malformed)

    def test_valid_pericope_hft_enters_macro_docket(self) -> None:
        prepared, docket = build_prepared_artifacts(
            fixture_bundle(valid_hft=True, bind_hft=True),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="strict"),
        )
        self.assertEqual(
            prepared["scope_audit"]["hft"]["status"], "valid_pericope_bound"
        )
        hft = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_type"] == "hft"
        )
        self.assertEqual(hft["lane"], "macro")
        self.assertEqual(hft["trust"], "trusted")
        self.assertIn("root_000672/B010", hft["branch_refs"])

    def test_unbound_local_hft_requires_explicit_escape_hatch(self) -> None:
        bundle = fixture_bundle(valid_hft=True)
        with self.assertRaises(ScopeError):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="strict", allow_legacy_hft_response=True
            ),
        )
        self.assertEqual(prepared["readiness"]["mode"], "legacy_hft_allowed")
        self.assertTrue(any(item["source_type"] == "hft" for item in docket["candidates"]))

    def test_bound_surah_hft_enters_global_lane(self) -> None:
        prepared, docket = build_prepared_artifacts(
            fixture_bundle(valid_hft=True, bind_hft=True, surah_hft=True),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="strict"),
        )
        self.assertEqual(
            prepared["scope_audit"]["hft"]["status"], "valid_surah_bound"
        )
        hft = next(item for item in docket["candidates"] if item["source_type"] == "hft")
        self.assertEqual(hft["lane"], "global")
        self.assertEqual(hft["scope"], "surah")

    def test_hft_seed_trace_must_stay_inside_packet_window(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        outlier = bundle["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"][
            "surprising_valid_outliers"
        ][0]
        outlier["activation_trace"][0]["source_ref"] = "29:45"
        with self.assertRaisesRegex(ScopeError, "seed scope violation"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(prepared["readiness"]["mode"], "quarantine_without_hft")
        self.assertTrue(prepared["mandatory_candidates_ready"])
        self.assertFalse(any(item["source_type"] == "hft" for item in docket["candidates"]))
        self.assertEqual(prepared["coverage"]["by_disposition"]["out_of_scope"], 1)
        self.assertEqual(prepared["scope_audit"]["hft"]["status"], "invalid")
        quarantined = prepared["diagnostics"]["quarantined_hft"]
        self.assertFalse(quarantined["visible_to_adjudication"])
        self.assertIn(
            "outside packet window", quarantined["seeds"][0]["quarantine_reason"]
        )

    def test_malformed_hft_window_scope_is_controlled_by_policy(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        bundle["v12_focus_trace_hermetic"]["packet_summary"]["window_scope"] = []
        with self.assertRaisesRegex(ScopeError, "packet window_scope"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(prepared["scope_audit"]["hft"]["status"], "invalid")
        self.assertTrue(prepared["diagnostics"]["quarantined_hft"]["seeds"])
        self.assertFalse(
            any(item["source_type"] == "hft" for item in docket["candidates"])
        )

    def test_hft_trace_branch_must_be_canonical_and_registered(self) -> None:
        unknown = fixture_bundle(valid_hft=True, bind_hft=True)
        trace = unknown["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"][
            "surprising_valid_outliers"
        ][0]["activation_trace"]
        trace[0]["branch_id"] = "B999"
        with self.assertRaisesRegex(ScopeError, "seed branch violation"):
            build_prepared_artifacts(
                unknown,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            unknown,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(prepared["readiness"]["mode"], "quarantine_without_hft")
        self.assertFalse(any(item["source_type"] == "hft" for item in docket["candidates"]))
        self.assertEqual(prepared["coverage"]["by_disposition"]["parse_failed"], 1)
        seed = prepared["diagnostics"]["quarantined_hft"]["seeds"][0]
        self.assertIn("root_000672/B999", seed["branch_refs"])
        self.assertIn("outside the retained", seed["quarantine_reason"])

        for missing_field in ("mapped_root_id", "branch_id"):
            with self.subTest(missing_field=missing_field):
                malformed = fixture_bundle(valid_hft=True, bind_hft=True)
                malformed_trace = malformed["v12_focus_trace_hermetic"]["readers"][
                    "reader_hft_a"
                ]["surprising_valid_outliers"][0]["activation_trace"]
                malformed_trace[0].pop(missing_field)
                with self.assertRaisesRegex(ScopeError, "malformed HFT structure"):
                    build_prepared_artifacts(
                        malformed,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="strict"),
                    )
                quarantined, quarantine_docket = build_prepared_artifacts(
                    malformed,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertEqual(
                    quarantined["readiness"]["mode"], "quarantine_without_hft"
                )
                self.assertFalse(
                    any(
                        item["source_type"] == "hft"
                        for item in quarantine_docket["candidates"]
                    )
                )
                self.assertGreaterEqual(
                    quarantined["coverage"]["by_disposition"]["parse_failed"], 1
                )
                diagnostic_seeds = quarantined["diagnostics"]["quarantined_hft"][
                    "seeds"
                ]
                self.assertEqual(len(diagnostic_seeds), 1)
                self.assertIn(
                    "/surprising_valid_outliers/0",
                    diagnostic_seeds[0]["source_pointer"],
                )
                self.assertIn(
                    missing_field, diagnostic_seeds[0]["quarantine_reason"]
                )

    def test_empty_hft_seed_id_is_retained_as_failed_diagnostic(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        bundle["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"][
            "surprising_valid_outliers"
        ][0]["outlier_id"] = ""
        with self.assertRaisesRegex(ScopeError, "missing or empty outlier_id"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        seed = prepared["diagnostics"]["quarantined_hft"]["seeds"][0]
        self.assertEqual(
            seed["source_local_id"], "reader_hft_a:surprising_valid_outliers:0"
        )
        self.assertIn("missing or empty outlier_id", seed["quarantine_reason"])
        self.assertFalse(
            any(item["source_type"] == "hft" for item in docket["candidates"])
        )

    def test_invalid_empty_hft_readers_are_structurally_accounted(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        bundle["v12_focus_trace_hermetic"]["readers"] = {}
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        hft_rows = [
            item
            for item in prepared["candidate_ledger"]
            if item["source_type"] == "hft"
        ]
        self.assertEqual(len(hft_rows), 1)
        self.assertEqual(hft_rows[0]["source_local_id"], "hft-structure")
        self.assertEqual(hft_rows[0]["disposition"], "parse_failed")
        self.assertIn("no reader", hft_rows[0]["reason"])
        self.assertEqual(prepared["coverage"]["by_source_type"]["hft"], 1)
        self.assertFalse(
            any(item["source_type"] == "hft" for item in docket["candidates"])
        )

    def test_empty_hft_reader_id_quarantines_without_losing_its_seeds(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        readers = bundle["v12_focus_trace_hermetic"]["readers"]
        readers[""] = readers.pop("reader_hft_a")
        with self.assertRaisesRegex(ScopeError, "reader ID must be nonempty"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        diagnostics = prepared["diagnostics"]["quarantined_hft"]
        self.assertEqual(len(diagnostics["seeds"]), 1)
        self.assertEqual(
            diagnostics["seeds"][0]["source_local_id"], ":outlier_webbed_path"
        )
        self.assertIn("/readers//surprising_valid_outliers/0", diagnostics["seeds"][0]["source_pointer"])
        self.assertFalse(
            any(item["source_type"] == "hft" for item in docket["candidates"])
        )

    def test_hft_identity_refs_and_echo_fields_fail_closed(self) -> None:
        padded = fixture_bundle(valid_hft=True, bind_hft=True, surah_hft=True)
        summary = padded["v12_focus_trace_hermetic"]["packet_summary"]
        summary["window"][0] = "029:1"
        reader = padded["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"]
        reader["packet_identity"]["window_sha256"] = canonical_sha256(
            summary["window"]
        )

        extra_echo = fixture_bundle(valid_hft=True, bind_hft=True)
        extra_echo["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"][
            "packet_identity"
        ]["extra"] = "uncontracted"

        for label, bundle in (("padded", padded), ("extra", extra_echo)):
            with self.subTest(label=label):
                with self.assertRaises(ScopeError):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="strict"),
                    )
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertTrue(prepared["readiness"]["ready"])
                self.assertEqual(prepared["scope_audit"]["hft"]["status"], "invalid")
                self.assertFalse(
                    any(c["source_type"] == "hft" for c in docket["candidates"])
                )

    def test_docket_is_byte_deterministic(self) -> None:
        bundle = fixture_bundle()
        first = build_prepared_artifacts(
            copy.deepcopy(bundle),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        second = build_prepared_artifacts(
            copy.deepcopy(bundle),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(canonical_json_bytes(first[0]), canonical_json_bytes(second[0]))
        self.assertEqual(canonical_json_bytes(first[1]), canonical_json_bytes(second[1]))
        validate_docket(first[1])

    def test_candidate_accounting_has_no_silent_loss(self) -> None:
        bundle = fixture_bundle()
        bundle["word_analysis"]["words"][0]["topics"].append({"headline": "bad"})
        bundle["channel_subchannels_anchored_here"].append(
            {
                "key": "Z",
                "name": "Other ayah only",
                "ayah_refs": ["29:39"],
                "active_motifs": "",
            }
        )
        prepared, _docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        coverage = prepared["coverage"]
        self.assertEqual(
            coverage["discovered_seed_count"], coverage["accounted_seed_count"]
        )
        self.assertEqual(coverage["by_disposition"]["parse_failed"], 1)
        self.assertEqual(coverage["by_disposition"]["out_of_scope"], 1)
        self.assertEqual(coverage["by_disposition"]["quarantined"], 1)

    def test_malformed_or_empty_topics_do_not_leave_unowned_supports(self) -> None:
        for topics in ([], "not-an-array"):
            with self.subTest(topics=topics):
                bundle = fixture_bundle()
                bundle["word_analysis"]["words"][0]["topics"] = topics
                _prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                owned = {
                    support_id
                    for candidate in docket["candidates"]
                    for support_id in candidate["support_ids"]
                }
                registered = {
                    support["support_id"] for support in docket["support_registry"]
                }
                self.assertEqual(registered, owned)
                self.assertFalse(
                    any(
                        support["json_pointer"] == "/word_analysis/words/0"
                        for support in docket["support_registry"]
                    )
                )

    def test_channel_fallback_anchor_requires_exact_ref(self) -> None:
        bundle = fixture_bundle()
        channel = bundle["channel_subchannels_anchored_here"][0]
        channel["ayah_refs"] = []
        channel["ayah_anchors"] = "not the focus: 129:380"
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(any(item["source_type"] == "channel" for item in docket["candidates"]))
        self.assertEqual(prepared["coverage"]["by_disposition"]["parse_failed"], 1)

    def test_channel_structured_refs_must_stay_in_pericope(self) -> None:
        bundle = fixture_bundle()
        bundle["channel_subchannels_anchored_here"][0]["ayah_refs"].append("29:45")
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(any(item["source_type"] == "channel" for item in docket["candidates"]))
        self.assertEqual(prepared["readiness"]["mode"], "blocked")
        self.assertEqual(prepared["coverage"]["by_disposition"]["parse_failed"], 1)

    def test_channel_non_string_anchor_is_accounted_parse_failure(self) -> None:
        bundle = fixture_bundle()
        bundle["channel_subchannels_anchored_here"][0]["ayah_anchors"] = {
            "ref": "29:38"
        }
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(any(item["source_type"] == "channel" for item in docket["candidates"]))
        self.assertEqual(prepared["coverage"]["by_disposition"]["parse_failed"], 1)

    def test_duplicate_local_ids_at_distinct_pointers_do_not_collapse(self) -> None:
        bundle = fixture_bundle()
        duplicate_word = copy.deepcopy(bundle["word_analysis"]["words"][0])
        duplicate_word["aligned_qac_word_ref"] = "29:38:2"
        bundle["word_analysis"]["words"].append(duplicate_word)
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        topics = [
            candidate
            for candidate in docket["candidates"]
            if candidate["source_local_id"] == "29:38:1:work"
        ]
        self.assertEqual(len(topics), 2)
        self.assertEqual(len({item["candidate_id"] for item in topics}), 2)
        self.assertEqual(len({item["source_pointer"] for item in topics}), 2)

    def test_source_inventory_distinguishes_present_empty_from_absent(self) -> None:
        bundle = fixture_bundle()
        del bundle["v12_reader_walks_wide"]
        prepared, _docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        inventory = prepared["source_inventory"]
        self.assertEqual(inventory["v12_reader_responses"]["state"], "present_empty")
        self.assertEqual(inventory["v12_reader_walks_wide"]["state"], "absent")

    def test_falsey_malformed_optional_sources_cannot_disappear(self) -> None:
        for source_key in (
            "branch_inventories",
            "v12_reader_walks",
            "v12_reader_walks_wide",
            "v12_cross_run_publication",
            "v12_reader_responses",
        ):
            with self.subTest(source_key=source_key):
                bundle = fixture_bundle()
                bundle[source_key] = False
                with self.assertRaisesRegex(ValidationError, "must be an object"):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="quarantine"),
                    )

    def test_validator_rejects_candidate_contract_drift(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        malformed = copy.deepcopy(docket)
        del malformed["candidates"][0]["source_pointer"]
        with self.assertRaisesRegex(Exception, "fields disagree with contract"):
            validate_docket(malformed)

        unknown_source = copy.deepcopy(docket)
        unknown_source["candidates"][0]["source_type"] = "future_source"
        with self.assertRaisesRegex(ValidationError, "invalid source type"):
            validate_docket(unknown_source)

        bundle = fixture_bundle()
        policy = PrepareOptions(hft_policy="quarantine")
        prepared, clean_docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=policy,
        )
        malformed_prepared = copy.deepcopy(prepared)
        malformed_prepared["coverage"]["docket_candidate_count"] += 1
        with self.assertRaisesRegex(Exception, "coverage"):
            validate_prepared(
                malformed_prepared,
                clean_docket,
                source_bundle=bundle,
                source_raw=canonical_json_bytes(bundle),
                options=policy,
            )

    def test_prepared_validator_controls_malformed_candidate_ledger_rows(self) -> None:
        bundle = fixture_bundle()
        policy = PrepareOptions(hft_policy="quarantine")
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=policy,
        )
        source_raw = canonical_json_bytes(bundle)
        mutations = [("row", value) for value in (None, [], False, 0, "")]
        mutations.extend(
            (
                ("source_type", []),
                ("source_local_id", {}),
                ("source_pointer", []),
                ("disposition", []),
                ("candidate_id", []),
                ("reason", {}),
            )
        )
        for field, value in mutations:
            with self.subTest(field=field, value=value):
                malformed = copy.deepcopy(prepared)
                if field == "row":
                    malformed["candidate_ledger"][0] = value
                else:
                    malformed["candidate_ledger"][0][field] = value
                with self.assertRaises(ValidationError):
                    validate_prepared(
                        malformed,
                        docket,
                        source_bundle=bundle,
                        source_raw=source_raw,
                        options=policy,
                    )

        duplicate = copy.deepcopy(prepared)
        quarantined_index = next(
            index
            for index, entry in enumerate(duplicate["candidate_ledger"])
            if entry["disposition"] == "quarantined"
        )
        replacement_index = next(
            index
            for index in range(len(duplicate["candidate_ledger"]))
            if index != quarantined_index
        )
        duplicate["candidate_ledger"][replacement_index] = copy.deepcopy(
            duplicate["candidate_ledger"][quarantined_index]
        )
        with self.assertRaisesRegex(ValidationError, "source identities must be unique"):
            validate_prepared(
                duplicate,
                docket,
                source_bundle=bundle,
                source_raw=source_raw,
                options=policy,
            )

        forged_local_id = copy.deepcopy(prepared)
        forged_entry = next(
            item
            for item in forged_local_id["candidate_ledger"]
            if not item["disposition"].startswith("docket_")
        )
        forged_entry["source_local_id"] += ":forged"
        with self.assertRaisesRegex(ValidationError, "exactly rederive"):
            validate_prepared(
                forged_local_id,
                docket,
                source_bundle=bundle,
                source_raw=source_raw,
                options=policy,
            )

        rebucketed = copy.deepcopy(prepared)
        rebucketed["source_inventory"]["qac_morphemes"]["seed_count"] -= 1
        rebucketed["source_inventory"]["word_analysis"]["seed_count"] += 1
        with self.assertRaisesRegex(ValidationError, "exactly rederive"):
            validate_prepared(
                rebucketed,
                docket,
                source_bundle=bundle,
                source_raw=source_raw,
                options=policy,
            )

        forged_dispositions = copy.deepcopy(prepared)
        forged_dispositions["source_inventory"]["qac_morphemes"][
            "dispositions"
        ] = {"quarantined": 999}
        with self.assertRaisesRegex(ValidationError, "exactly rederive"):
            validate_prepared(
                forged_dispositions,
                docket,
                source_bundle=bundle,
                source_raw=source_raw,
                options=policy,
            )

    def test_prepared_schema_readiness_keys_match_runtime_artifact(self) -> None:
        prepared, _docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        schema = json.loads(
            (V3_ROOT / "schemas/prepared.schema.json").read_text(encoding="utf-8")
        )
        readiness_schema = schema["properties"]["readiness"]
        self.assertEqual(set(readiness_schema["required"]), set(prepared["readiness"]))
        self.assertEqual(
            set(readiness_schema["properties"]), set(prepared["readiness"])
        )

    def test_branch_review_readiness_requires_focus_occurrence_grounding(self) -> None:
        prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        target_candidate = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_type"] == "qac_morpheme"
            and "root_000672" in candidate["root_ids"]
        )
        pruned_candidates = [
            candidate
            for candidate in docket["candidates"]
            if candidate["candidate_id"] != target_candidate["candidate_id"]
        ]
        gaps = _branch_review_grounding_gaps(
            ayah_ref=docket["identity"]["ayah_ref"],
            branch_registry=docket["branch_registry"],
            nominated_branch_registry=docket["nominated_branch_registry"],
            candidates=pruned_candidates,
            support_registry=docket["support_registry"],
        )
        self.assertEqual(
            sum(gap["kind"] == "focus_occurrence_missing" for gap in gaps),
            1,
        )
        self.assertEqual(
            next(
                gap["root_id"]
                for gap in gaps
                if gap["kind"] == "focus_occurrence_missing"
            ),
            "root_000672",
        )

    def test_legacy_only_branch_is_audited_without_entering_review_registry(self) -> None:
        bundle = fixture_bundle()
        bundle["branch_inventories"] = {
            "full_context_packet": {
                "source_file": "fixture-branches.json",
                "branch_inventories": [
                    {
                        "root": "ب ي ت",
                        "branches": [
                            {
                                "branch_id": "B007",
                                "image_en": "woven shelter",
                                "scope_en": "shelter imagery where attested",
                                "variants": [{"root_id": "root_009999"}],
                            }
                        ],
                    }
                ],
            }
        }
        bundle["v12_reader_responses"] = {
            "legacy": "ب ي ت B007 is a possible woven shelter relation."
        }
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(docket["nominated_branch_registry"], [])
        legacy_candidate = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "legacy_reader_response"
        )
        self.assertEqual(legacy_candidate["unresolved_branch_refs"], ["root_009999/B007"])
        self.assertFalse(legacy_candidate["adjudicable"])
        self.assertTrue(prepared["readiness"]["ready"])

    def test_malformed_hft_shapes_are_quarantined_without_handoff_leakage(self) -> None:
        malformed_values = [
            [],
            {"packet_summary": [], "readers": {}},
            {"packet_summary": {}, "readers": []},
            {
                "packet_summary": {
                    "protocol": "focus-trace-pericope-lean-v1",
                    "focus_ref": "29:38",
                    "window": [f"29:{ayah}" for ayah in range(28, 45)],
                    "ayah_count": 17,
                },
                "readers": {
                    "reader": {
                        "protocol": "focus-trace-hermetic-response-v4",
                        "focus_ref": "29:38",
                        "baseline_models": {},
                        "context_deltas": [],
                        "surprising_valid_outliers": [],
                    }
                },
            },
        ]
        for malformed in malformed_values:
            with self.subTest(shape=type(malformed).__name__, value=malformed):
                bundle = fixture_bundle()
                bundle["v12_focus_trace_hermetic"] = malformed
                with self.assertRaises(ScopeError):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="strict"),
                    )
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertTrue(prepared["readiness"]["ready"])
                self.assertFalse(
                    any(item["source_type"] == "hft" for item in docket["candidates"])
                )
                quarantine = prepared["diagnostics"]["quarantined_hft"]
                self.assertFalse(quarantine["visible_to_adjudication"])
                self.assertIsNotNone(quarantine["structural_error"])
                self.assertTrue(
                    any(
                        item["source_type"] == "hft"
                        and item["disposition"] == "parse_failed"
                        for item in prepared["candidate_ledger"]
                    )
                )

    def test_malformed_bound_hft_seed_obeys_strict_or_quarantine_policy(self) -> None:
        bundle = fixture_bundle(valid_hft=True, bind_hft=True)
        bundle["v12_focus_trace_hermetic"]["readers"]["reader_hft_a"][
            "surprising_valid_outliers"
        ][0]["activation_trace"][0]["branch_id"] = "BAD"

        with self.assertRaises(ScopeError):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="strict"),
            )

        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        self.assertEqual(prepared["scope_audit"]["hft"]["status"], "invalid")
        self.assertFalse(
            any(candidate["source_type"] == "hft" for candidate in docket["candidates"])
        )
        quarantine = prepared["diagnostics"]["quarantined_hft"]
        self.assertIsNotNone(quarantine["structural_error"])
        self.assertIsNotNone(quarantine["malformed_payload"])
        self.assertTrue(
            any(
                entry["source_type"] == "hft"
                and entry["disposition"] == "parse_failed"
                and "outlier_webbed_path" in entry["source_local_id"]
                for entry in prepared["candidate_ledger"]
            )
        )

    def test_word_refs_and_obligations_fail_closed(self) -> None:
        invalid_refs = [None, "1:1:1", "29:38:0", "29:38:999"]
        for invalid_ref in invalid_refs:
            with self.subTest(aligned_qac_word_ref=invalid_ref):
                bundle = fixture_bundle()
                bundle["word_analysis"]["words"][0][
                    "aligned_qac_word_ref"
                ] = invalid_ref
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertFalse(prepared["readiness"]["ready"])
                self.assertEqual(
                    prepared["readiness"]["blocker_counts"][
                        "word_analysis/parse_failed"
                    ],
                    1,
                )
                self.assertFalse(
                    any(
                        candidate["source_local_id"] == "29:38:1:work"
                        for candidate in docket["candidates"]
                    )
                )

        bundle = fixture_bundle()
        bundle["word_analysis"]["words"][0]["topics"][0][
            "commentary_obligation"
        ] = "must-integrate"
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(prepared["readiness"]["ready"])
        self.assertEqual(
            prepared["readiness"]["blocker_counts"]["word_analysis/parse_failed"],
            1,
        )
        self.assertFalse(
            any(
                candidate["source_local_id"] == "29:38:1:work"
                for candidate in docket["candidates"]
            )
        )

    def test_docket_validator_rebinds_word_candidate_to_source_row(self) -> None:
        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        mutated = copy.deepcopy(docket)
        word_candidate = next(
            candidate
            for candidate in mutated["candidates"]
            if candidate["source_type"] == "word_analysis"
        )
        word_candidate["anchor_refs"] = ["29:38:999"]
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("docket_payload_sha256")
        mutated["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "word-analysis anchor"):
            validate_docket(mutated)

    def test_word_root_prose_cannot_mint_focus_root_ownership(self) -> None:
        bundle = fixture_bundle()
        bundle["word_analysis"]["words"][1]["root_display"] = "ب ص ر"
        bundle["word_analysis"]["words"][1]["root_gloss_range"] = "ب ص ر"
        spoof = copy.deepcopy(bundle["word_analysis"]["words"][2])
        spoof["aligned_qac_word_ref"] = "29:38:4"
        spoof["root_display"] = "س ب ل"
        spoof["root_gloss_range"] = "س ب ل"
        spoof["topics"][0]["topic_id"] = "29:38:4:spoofed-root"
        bundle["word_analysis"]["words"].append(spoof)

        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        self.assertTrue(
            all(
                not candidate["root_ids"]
                for candidate in docket["candidates"]
                if candidate["source_type"] == "word_analysis"
            )
        )
        self.assertEqual(
            [
                candidate["source_type"]
                for candidate in docket["candidates"]
                if "root_000672" in candidate["root_ids"]
            ],
            ["qac_morpheme"],
        )

    def test_publication_anchor_shape_is_strict_and_lossless(self) -> None:
        valid_bundle = fixture_bundle()
        valid_bundle["v12_cross_run_publication"] = {
            "ayah_ref": "29:38",
            "findings": [
                {
                    "text": "Published finding",
                    "grade": "strong",
                    "anchors": [["29:38:1", "root_001046", ["B011"]]],
                }
            ],
        }
        _prepared, valid_docket = build_prepared_artifacts(
            valid_bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        published = next(
            item
            for item in valid_docket["candidates"]
            if item["source_type"] == "cross_run_publication"
        )
        self.assertEqual(published["anchor_refs"], ["29:38:1"])
        self.assertEqual(published["branch_refs"], ["root_001046/B011"])

        malformed_anchors = [
            None,
            [],
            {},
            [["bad"]],
            [["29:38:1", "root_001046", ["BAD"]]],
            [["29:38:1", "root_000672", ["B001"]]],
        ]
        for anchors in malformed_anchors:
            with self.subTest(anchors=anchors):
                bundle = fixture_bundle()
                bundle["v12_cross_run_publication"] = {
                    "ayah_ref": "29:38",
                    "findings": [{"text": "Published finding", "anchors": anchors}],
                }
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertFalse(
                    any(
                        item["source_type"] == "cross_run_publication"
                        for item in docket["candidates"]
                    )
                )
                entry = next(
                    item
                    for item in prepared["candidate_ledger"]
                    if item["source_type"] == "cross_run_publication"
                )
                self.assertEqual(entry["disposition"], "parse_failed")

        missing_bundle = fixture_bundle()
        missing_bundle["v12_cross_run_publication"] = {
            "ayah_ref": "29:38",
            "findings": [{"text": "Published finding"}],
        }
        prepared, docket = build_prepared_artifacts(
            missing_bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(
            any(
                item["source_type"] == "cross_run_publication"
                for item in docket["candidates"]
            )
        )
        self.assertEqual(
            next(
                item["disposition"]
                for item in prepared["candidate_ledger"]
                if item["source_type"] == "cross_run_publication"
            ),
            "parse_failed",
        )

        conflicting_identities = [
            {"ayah_ref": "29:38", "canonical_ayah_ref": "29:39"},
            {"ayah_ref": "029:038"},
            {"ayah_ref": "29:38", "surah": 30},
        ]
        for identity_fields in conflicting_identities:
            with self.subTest(identity_fields=identity_fields):
                bundle = fixture_bundle()
                bundle["v12_cross_run_publication"] = {
                    **identity_fields,
                    "findings": [
                        {
                            "text": "Conflicting publication",
                            "anchors": [
                                ["29:38:1", "root_001046", ["B011"]]
                            ],
                        }
                    ],
                }
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=PrepareOptions(hft_policy="quarantine"),
                )
                self.assertFalse(
                    any(
                        item["source_type"] == "cross_run_publication"
                        for item in docket["candidates"]
                    )
                )
                publication_entry = next(
                    item
                    for item in prepared["candidate_ledger"]
                    if item["source_type"] == "cross_run_publication"
                )
                self.assertEqual(publication_entry["disposition"], "parse_failed")

    def test_channel_nomination_is_bound_to_its_exact_support_field(self) -> None:
        bundle = fixture_bundle()
        bundle["branch_inventories"] = {
            "full_context_packet": {
                "source_file": "fixture-branches.json",
                "branch_inventories": [
                    {
                        "root": "ب ي ت",
                        "branches": [
                            {
                                "branch_id": branch_id,
                                "image_en": image,
                                "scope_en": "where attested",
                                "variants": [{"root_id": "root_009999"}],
                            }
                            for branch_id, image in (
                                ("B007", "woven shelter"),
                                ("B008", "sealed chamber"),
                            )
                        ],
                    }
                ],
            }
        }
        channel = bundle["channel_subchannels_anchored_here"][0]
        channel["active_motifs"] = "root_009999/B007 woven shelter"
        channel["scene_or_process"] = "root_009999/B008 sealed chamber"
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        candidate = next(
            item for item in docket["candidates"] if item["source_type"] == "channel"
        )
        self.assertEqual(candidate["branch_refs"], ["root_009999/B007"])
        supports = {
            item["json_pointer"]: item for item in docket["support_registry"]
        }
        self.assertEqual(
            supports[
                "/channel_subchannels_anchored_here/0/active_motifs"
            ]["branch_refs"],
            ["root_009999/B007"],
        )
        self.assertEqual(
            supports[
                "/channel_subchannels_anchored_here/0/scene_or_process"
            ]["branch_refs"],
            [],
        )
        self.assertEqual(
            [item["branch_ref"] for item in docket["nominated_branch_registry"]],
            ["root_009999/B007"],
        )

    def test_channel_nomination_uses_native_inventory_before_qac_split_map(
        self,
    ) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000672"]["dictionary_entry"][
            "branches"
        ].append(branch("root_000672", "B002", "QAC bridge collision"))
        for root_id, gloss in (
            ("root_009998", "unrelated split target one"),
            ("root_009999", "unrelated split target two"),
        ):
            bundle["root_lexicon"][root_id] = root_record(
                root_id,
                "س ب ل",
                [branch(root_id, "B002", gloss)],
            )
        bundle["branch_inventories"] = {
            "full_context_packet": {
                "source_file": "fixture-branches.json",
                "branch_inventories": [
                    {
                        "root": "س ب ل",
                        "branches": [
                            {
                                "branch_id": "B001",
                                "image_en": "route",
                                "scope_en": "a traversable way",
                                "variants": [{"root_id": "root_000672"}],
                            },
                            {
                                "branch_id": "B002",
                                "image_en": "branch-specific route",
                                "scope_en": "the nominated route variant",
                                "variants": [{"root_id": "root_009999"}],
                            },
                        ],
                    }
                ],
            }
        }
        channel = bundle["channel_subchannels_anchored_here"][0]
        channel["active_motifs"] = "a route `س ب ل:B002/m01`"

        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )

        self.assertTrue(prepared["readiness"]["ready"])
        candidate = next(
            item for item in docket["candidates"] if item["source_type"] == "channel"
        )
        self.assertEqual(candidate["branch_refs"], ["root_009999/B002"])
        self.assertEqual(candidate["unresolved_branch_citations"], [])

    def test_nominated_branch_requires_descriptor_and_candidate_owner(self) -> None:
        bundle = fixture_bundle()
        bundle["branch_inventories"] = {
            "full_context_packet": {
                "branch_inventories": [
                    {
                        "root": "ب ي ت",
                        "branches": [
                            {
                                "branch_id": "B007",
                                "variants": [{"root_id": "root_009999"}],
                            }
                        ],
                    }
                ]
            }
        }
        with self.assertRaisesRegex(ValidationError, "image descriptor"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("fixture.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

        _prepared, docket = build_prepared_artifacts(
            fixture_bundle(),
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        mutated = copy.deepcopy(docket)
        mutated["nominated_branch_registry"].append(
            {
                "branch_ref": "root_009999/B007",
                "root_ar": "ب ي ت",
                "image_ar": None,
                "image_en": "woven shelter",
                "scope_ar": None,
                "scope_en": "where attested",
                "source_file": "fixture.json",
                "source_pointer": "/branch_inventories/0",
            }
        )
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("docket_payload_sha256")
        mutated["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "exact nomination support"):
            validate_docket(mutated)

    @unittest.skipUnless(REAL_S29_BUNDLE.exists(), "real S29 bundle not present")
    def test_real_s29_prepare_regression(self) -> None:
        raw = REAL_S29_BUNDLE.read_bytes()
        bundle = json.loads(raw)
        with self.assertRaises(ScopeError):
            build_prepared_artifacts(
                bundle,
                source_path=REAL_S29_BUNDLE,
                source_raw=raw,
                options=PrepareOptions(hft_policy="strict"),
            )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=REAL_S29_BUNDLE,
            source_raw=raw,
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(prepared["readiness"]["mode"], "quarantine_without_hft")
        self.assertFalse(any(item["source_type"] == "hft" for item in docket["candidates"]))

        worked = next(
            item for item in docket["candidates"]
            if item["title"] == "Cutting the Worked Road"
        )
        self.assertIn("root_001046/B011", worked["focus_branch_refs"])
        self.assertIn("root_001240/B023", worked["nominated_branch_refs"])
        self.assertTrue(worked["adjudicable"])
        wide = [
            item for item in docket["candidates"]
            if item["source_type"] == "v12_reader_walks_wide"
        ]
        resolved = {ref for item in wide for ref in item["branch_refs"]}
        self.assertTrue(
            {
                "root_000121/B002",
                "root_000672/B001",
                "root_000848/B001",
                "root_001046/B001",
            }
            <= resolved
        )
        focus_refs = {
            branch_item["branch_ref"]
            for root in docket["branch_registry"]
            for branch_item in root["branches"]
        }
        self.assertIn("root_000672/B010", focus_refs)
        self.assertFalse(
            any(item["mandatory"] and not item["adjudicable"] for item in docket["candidates"])
        )

    def test_present_empty_hft_is_invalid_not_absent(self) -> None:
        policy = PrepareOptions(hft_policy="quarantine")
        for empty_value in (None, {}):
            with self.subTest(empty_value=empty_value):
                bundle = fixture_bundle()
                bundle["v12_focus_trace_hermetic"] = empty_value
                prepared, docket = build_prepared_artifacts(
                    bundle,
                    source_path=Path("fixture.json"),
                    options=policy,
                )
                self.assertEqual(prepared["scope_audit"]["hft"]["status"], "invalid")
                self.assertEqual(
                    prepared["readiness"]["mode"], "quarantine_without_hft"
                )
                hft_rows = [
                    item
                    for item in prepared["candidate_ledger"]
                    if item["source_type"] == "hft"
                ]
                self.assertEqual(len(hft_rows), 1)
                self.assertEqual(hft_rows[0]["source_local_id"], "hft-structure")
                self.assertEqual(hft_rows[0]["disposition"], "parse_failed")
                self.assertEqual(
                    prepared["source_inventory"]["v12_focus_trace_hermetic"]["state"],
                    "present_empty",
                )
                self.assertFalse(
                    any(item["source_type"] == "hft" for item in docket["candidates"])
                )
                with self.assertRaises(ScopeError):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        options=PrepareOptions(hft_policy="strict"),
                    )

        missing = fixture_bundle()
        del missing["v12_focus_trace_hermetic"]
        prepared, _docket = build_prepared_artifacts(
            missing,
            source_path=Path("fixture.json"),
            options=policy,
        )
        self.assertEqual(prepared["scope_audit"]["hft"]["status"], "absent")
        self.assertEqual(prepared["readiness"]["mode"], "without_hft")
        self.assertFalse(
            any(
                item["source_type"] == "hft"
                for item in prepared["candidate_ledger"]
            )
        )

    @unittest.skipUnless(REAL_S29_39_BUNDLE.exists(), "real S29:39 bundle not present")
    def test_real_s29_39_missing_dictionary_is_visible_but_runnable(self) -> None:
        raw = REAL_S29_39_BUNDLE.read_bytes()
        bundle = json.loads(raw)
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=REAL_S29_39_BUNDLE,
            source_raw=raw,
            options=PrepareOptions(
                hft_policy="quarantine",
                allow_incomplete_branch_coverage=True,
            ),
        )
        self.assertTrue(prepared["readiness"]["ready"])
        self.assertEqual(
            docket["scope"]["branch_coverage"]["missing_dictionary_roots"][0][
                "root_id"
            ],
            "root_000281",
        )
        self.assertIn(
            "branch surprise coverage is incomplete",
            " ".join(prepared["readiness"]["warnings"]),
        )
        self.assertEqual(
            {
                item["source_local_id"]: item["root_ids"]
                for item in docket["candidates"]
                if item["source_type"] == "qac_morpheme"
                and set(item["root_ids"]) & {"root_000281", "root_000025"}
            },
            {
                next(
                    item["source_local_id"]
                    for item in docket["candidates"]
                    if item["source_type"] == "qac_morpheme"
                    and "root_000281" in item["root_ids"]
                ): ["root_000281"],
                next(
                    item["source_local_id"]
                    for item in docket["candidates"]
                    if item["source_type"] == "qac_morpheme"
                    and "root_000025" in item["root_ids"]
                ): ["root_000025"],
            },
        )

    def test_confined_destination_rejects_traversal_and_symlink_escape(self) -> None:
        with self.assertRaises(PathConfinementError):
            confined_destination(
                Path("/tmp/commentary-v3-outside-root"), Path("artifact.json")
            )
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            escaped_creation = V3_ROOT.parent / (
                f"{Path(temp_dir).name}-must-not-exist"
            )
            unsafe_root = (
                V3_ROOT
                / "inputs"
                / ".."
                / ".."
                / escaped_creation.name
            )
            with self.assertRaisesRegex(PathConfinementError, "Unsafe artifact root"):
                confined_destination(unsafe_root, Path("artifact.json"))
            self.assertFalse(escaped_creation.exists())
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir) / "root"
            with self.assertRaises(PathConfinementError):
                confined_destination(root, Path("../escape.json"))
            outside = Path(temp_dir) / "outside"
            outside.mkdir()
            root.mkdir()
            (root / "linked").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(PathConfinementError):
                confined_destination(root, Path("linked/escape.json"))

        with (
            tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir,
            tempfile.TemporaryDirectory() as outside_dir,
        ):
            base = Path(temp_dir)
            outside = Path(outside_dir)
            (base / "linked").symlink_to(outside, target_is_directory=True)
            escaped_creation = outside / "must-not-exist"
            root = base / "linked" / escaped_creation.name / "root"
            with self.assertRaisesRegex(
                PathConfinementError, "ancestor may not be a symlink"
            ):
                confined_destination(root, Path("artifact.json"))
            self.assertFalse(escaped_creation.exists())

    def test_artifact_write_is_idempotent_but_conflicts_by_default(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            root = Path(temp_dir) / "root"
            relative = Path("stage/artifact.json")
            first = write_json_confined(root, relative, {"value": 1})
            self.assertEqual(first.read_text(encoding="utf-8"), '{\n  "value": 1\n}\n')
            write_json_confined(root, relative, {"value": 1})
            with self.assertRaises(ArtifactConflictError):
                write_json_confined(root, relative, {"value": 2})
            write_json_confined(root, relative, {"value": 2}, replace=True)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8")), {"value": 2})

    def test_nonfinite_numbers_fail_strict_json_boundary(self) -> None:
        with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
            canonical_json_bytes({"value": float("nan")})
        for value in ({"nested": {1: "ambiguous"}}, {"tuple": (1, 2)}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
                    canonical_json_bytes(value)
                with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
                    pretty_json_bytes(value)
        circular: list[object] = []
        circular.append(circular)
        with self.assertRaisesRegex(ValidationError, "circular JSON container"):
            canonical_json_bytes(circular)
        with self.assertRaisesRegex(ValidationError, "circular JSON container"):
            pretty_json_bytes(circular)
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            path = Path(temp_dir) / "nonfinite.json"
            path.write_text('{"value": NaN}', encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "non-finite JSON number"):
                load_json_object(path)

            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text(
                '{"outer":{"same":1,"same":2}}', encoding="utf-8"
            )
            with self.assertRaisesRegex(ValidationError, "duplicate JSON object key"):
                load_json_object(duplicate)

    def test_source_raw_must_encode_the_exact_supplied_bundle(self) -> None:
        bundle = fixture_bundle()
        policy = PrepareOptions(hft_policy="quarantine")
        for raw in (
            b"not-json",
            b"[]",
            canonical_json_bytes({"different": True}),
        ):
            with self.subTest(raw=raw):
                with self.assertRaises(ValidationError):
                    build_prepared_artifacts(
                        bundle,
                        source_path=Path("fixture.json"),
                        source_raw=raw,
                        options=policy,
                    )

        for bundle_value, raw_value in ((True, 1), (1, 1.0)):
            with self.subTest(bundle_value=bundle_value, raw_value=raw_value):
                typed_bundle = copy.deepcopy(bundle)
                typed_bundle["__type_probe__"] = bundle_value
                raw_bundle = copy.deepcopy(typed_bundle)
                raw_bundle["__type_probe__"] = raw_value
                with self.assertRaisesRegex(
                    ValidationError, "does not encode the supplied bundle"
                ):
                    build_prepared_artifacts(
                        typed_bundle,
                        source_path=Path("fixture.json"),
                        source_raw=canonical_json_bytes(raw_bundle),
                        options=policy,
                    )

        source_raw = canonical_json_bytes(bundle)
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            source_raw=source_raw,
            options=policy,
        )
        with self.assertRaisesRegex(ValidationError, "does not encode source_bundle"):
            validate_prepared(
                prepared,
                docket,
                source_bundle=bundle,
                source_raw=canonical_json_bytes({"different": True}),
                options=policy,
            )

        circular: list[object] = []
        circular.append(circular)
        for malformed_value in ({1: "ambiguous"}, (1, 2), circular):
            with self.subTest(malformed_value=malformed_value):
                malformed_bundle = copy.deepcopy(bundle)
                malformed_bundle["__json_type_probe__"] = malformed_value
                with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
                    build_prepared_artifacts(
                        malformed_bundle,
                        source_path=Path("fixture.json"),
                        options=policy,
                    )
                with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
                    validate_prepared(
                        prepared,
                        docket,
                        source_bundle=malformed_bundle,
                        source_raw=source_raw,
                        options=policy,
                    )

    def test_prepare_retains_minified_source_snapshot_under_v3_inputs(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            source_path = temporary / "source.json"
            raw = (
                json.dumps(fixture_bundle(), ensure_ascii=False, indent=1) + "\n"
            ).encode("utf-8")
            source_path.write_bytes(raw)
            inputs_root = temporary / "inputs"
            with patch("v3lib.prepare.INPUTS_ROOT", inputs_root):
                prepared, _docket, paths = prepare_bundle_file(
                    source_path,
                    options=PrepareOptions(hft_policy="quarantine"),
            )
            snapshot = Path(paths["source_bundle"])
            self.assertTrue(snapshot.is_relative_to(inputs_root))
            self.assertEqual(snapshot.read_bytes(), canonical_json_bytes(fixture_bundle()))
            self.assertEqual(
                prepared["artifacts"]["source_bundle"],
                "inputs/source/s029/29_38.bundle.json",
            )
            self.assertEqual(
                prepared["identity"]["source"]["raw_sha256"],
                prepared["identity"]["source"]["canonical_sha256"],
            )
            self.assertEqual(
                prepared["identity"]["source"]["raw_sha256"],
                sha256_bytes(snapshot.read_bytes()),
            )
            legacy_prepared, legacy_docket = build_prepared_artifacts(
                fixture_bundle(),
                source_path=source_path,
                source_raw=raw,
                options=PrepareOptions(hft_policy="quarantine"),
            )
            self.assertNotEqual(
                legacy_prepared["identity"]["source"]["raw_sha256"],
                legacy_prepared["identity"]["source"]["canonical_sha256"],
            )
            validate_prepared(
                legacy_prepared,
                legacy_docket,
                source_bundle=fixture_bundle(),
                source_raw=raw,
                options=PrepareOptions(hft_policy="quarantine"),
            )
            self.assertEqual(
                Path(paths["prepared"]).read_bytes(),
                canonical_json_bytes(prepared),
            )
            self.assertEqual(
                Path(paths["docket"]).read_bytes(),
                canonical_json_bytes(_docket),
            )
            Path(paths["prepared"]).unlink()
            with patch("v3lib.prepare.INPUTS_ROOT", inputs_root):
                prepare_bundle_file(
                    source_path,
                    options=PrepareOptions(hft_policy="quarantine"),
                )
            self.assertTrue(Path(paths["prepared"]).is_file())

    def test_v3_python_has_no_legacy_commentary_imports(self) -> None:
        forbidden = {"build_bundle", "tier_branch_payloads", "scripts"}
        for path in V3_ROOT.rglob("*.py"):
            tree = compile(path.read_text(encoding="utf-8"), str(path), "exec")
            self.assertIsNotNone(tree)
            source = path.read_text(encoding="utf-8")
            for name in forbidden:
                self.assertNotRegex(source, rf"(?:from|import)\s+{name}(?:\b|\.)")
        self.assertIsNotNone(importlib.util.spec_from_file_location("v3_cli", WORKFLOW_PATH))


if __name__ == "__main__":
    unittest.main()
