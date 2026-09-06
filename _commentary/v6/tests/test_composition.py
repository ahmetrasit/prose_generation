from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "composition.py"
SPEC = importlib.util.spec_from_file_location("commentary_v6_composition", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
composition = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = composition
SPEC.loader.exec_module(composition)


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
        "word_morpheme_spans": [],
        "branch_inventories": {"full_context_packet": {"branches": []}},
        "root_lexicon": {"root_000001": {"dictionary_entry": {}}},
        "v12_reader_walks": {"reader_a": {"reading": ref}},
        "v12_focus_trace_hermetic": {},
        "coverage": {},
    }


def basmala_bundle(ref: str = "100:0") -> dict[str, object]:
    bundle = numbered_bundle("1:1")
    surah = int(ref.split(":", 1)[0])
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
                "target_normalized": composition.BASMALA_NORMALIZED_SURFACE,
                "source_normalized": composition.BASMALA_NORMALIZED_SURFACE,
            }
        },
    })
    return bundle


class SelectorTests(unittest.TestCase):
    def test_ordered_discontinuous_cross_surah_segments(self) -> None:
        analysis = composition.composition_from_cli(
            "fatiha-lens-s100",
            ["fatiha=1:1-7", "s100=100:1,100:3,100:11"],
            ["100:3"],
        )
        self.assertEqual(
            analysis.ordered_refs,
            (*[f"1:{ayah}" for ayah in range(1, 8)], "100:1", "100:3", "100:11"),
        )
        rows = analysis.context_rows("100:3")
        self.assertEqual([row["ref"] for row in rows[:7]], [f"1:{a}" for a in range(1, 8)])
        self.assertTrue(all(row["lane"] == "global" for row in rows[:7]))
        self.assertEqual(
            [(row["ref"], row["lane"]) for row in rows[7:]],
            [("100:1", "macro"), ("100:11", "macro")],
        )

    def test_duplicate_context_ref_across_segments_is_rejected(self) -> None:
        with self.assertRaisesRegex(composition.CompositionError, "only one"):
            composition.composition_from_cli(
                "duplicate",
                ["first=1:1-2", "second=1:2,100:1"],
                ["100:1"],
            )

    def test_host_basmala_is_macro_even_in_a_separate_segment(self) -> None:
        analysis = composition.composition_from_cli(
            "segmented-host-basmala",
            ["preface=100:0", "host=100:1-2"],
            ["100:1"],
        )

        self.assertEqual(
            [(row["ref"], row["lane"]) for row in analysis.context_rows("100:1")],
            [("100:0", "macro"), ("100:2", "macro")],
        )

    def test_invalid_prefatory_refs_and_zero_range_are_rejected(self) -> None:
        for selector in ("1:0", "9:0", "100:0-2"):
            with self.subTest(selector=selector):
                with self.assertRaises(composition.CompositionError):
                    composition.expand_selectors(selector)

    def test_total_composition_limit_applies_across_segments(self) -> None:
        with self.assertRaisesRegex(composition.CompositionError, "at most 512"):
            composition.composition_from_cli(
                "too-large",
                ["first=1:1-300", "second=2:1-300"],
                ["2:1"],
            )

    def test_external_ayat_project_as_ordinary_macro_context(self) -> None:
        analysis = composition.composition_from_cli(
            "s100-plus-17-50",
            ["target=100:1-3"],
            ["100:2"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )

        rows = analysis.context_rows("100:2")
        added_rows = [row for row in rows if row.get("membership_added_ayah")]

        self.assertEqual(
            [(row["ref"], row["lane"]) for row in added_rows],
            [("17:50", "macro")],
        )
        self.assertEqual(analysis.member_surah, 100)
        self.assertEqual(analysis.added_ayat_refs, ("17:50",))
        self.assertEqual(
            added_rows[0]["source_pointer"],
            "/scope/analysis_composition/surah_membership/added_ayat_refs/0",
        )

    def test_external_ayah_can_be_the_only_context_for_one_host_focus(self) -> None:
        analysis = composition.composition_from_cli(
            "single-focus-with-external",
            ["host=100:1"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["17:50"],
        )

        self.assertEqual(analysis.context_refs("100:1"), ("17:50",))
        self.assertEqual(
            [row["lane"] for row in analysis.context_rows("100:1")],
            ["macro"],
        )

    def test_added_ayat_are_context_only(self) -> None:
        with self.assertRaisesRegex(composition.CompositionError, "context-only"):
            composition.composition_from_cli(
                "s100-plus-17-50",
                ["target=100:1-2", "external=17:50"],
                ["17:50"],
                member_surah=100,
                added_ayat_selectors=["17:50"],
            )

    def test_added_ayat_need_not_be_repeated_in_segments(self) -> None:
        analysis = composition.composition_from_cli(
            "host-with-external",
            ["target=100:1-2"],
            ["100:1"],
            member_surah=100,
            added_ayat_selectors=["1:1,1:2", "17:50"],
        )
        self.assertEqual(analysis.context_refs("100:1"), ("100:2", "1:1", "1:2", "17:50"))

    def test_added_ayat_reject_ranges_duplicates_and_empty_membership(self) -> None:
        for selectors, message in (
            (["1:1-7"], "list each"),
            (["1:1,1:1"], "Duplicate"),
            ([], "cannot be empty"),
        ):
            with self.subTest(selectors=selectors):
                with self.assertRaisesRegex(composition.CompositionError, message):
                    composition.composition_from_cli(
                        "bad-added-ayat",
                        ["target=100:1-2"],
                        ["100:1"],
                        member_surah=100,
                        added_ayat_selectors=selectors,
                    )

    def test_added_ayah_cannot_also_be_a_segment_member(self) -> None:
        with self.assertRaisesRegex(
            composition.CompositionError, "must not also appear"
        ):
            composition.composition_from_cli(
                "overlapping-added-ayah",
                ["target=100:1-2", "external=17:50"],
                ["100:1"],
                member_surah=100,
                added_ayat_selectors=["17:50"],
            )


class BundleValidationTests(unittest.TestCase):
    def test_bundle_lookup_rejects_flat_and_nested_shadowing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            direct = root / "100_1.ayah.json"
            nested = root / "s100" / "100_1.ayah.json"
            nested.parent.mkdir()
            direct.write_text("{}", encoding="utf-8")
            nested.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(composition.CompositionError, "Ambiguous"):
                composition.unit_bundle_path(root, "100:1")

    def test_prefatory_bundle_keeps_positive_linguistic_refs(self) -> None:
        identity = composition.validate_unit_bundle(
            basmala_bundle(), expected_ref="100:0"
        )
        self.assertEqual(identity["surface_ref"], "100:0")
        self.assertEqual(identity["linguistic_source_ref"], "1:1")

    def test_loaded_bundle_records_raw_and_canonical_hashes_separately(self) -> None:
        bundle = numbered_bundle("100:1")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "s100" / "100_1.ayah.json"
            path.parent.mkdir()
            path.write_text(json.dumps(bundle), encoding="utf-8")
            _path, _value, first = composition.load_unit_bundle(root, "100:1")
            path.write_text(
                json.dumps(bundle, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            _path, _value, second = composition.load_unit_bundle(root, "100:1")

        self.assertEqual(first["canonical_sha256"], second["canonical_sha256"])
        self.assertNotEqual(first["source_sha256"], second["source_sha256"])

    def test_numbered_bundle_cannot_alias_an_external_surface(self) -> None:
        bundle = numbered_bundle("17:50")
        bundle["surface_ref"] = "29:38"
        with self.assertRaisesRegex(composition.CompositionError, "surface ref"):
            composition.validate_unit_bundle(bundle, expected_ref="17:50")

    def test_prefatory_bundle_rejects_fabricated_qac_ref(self) -> None:
        bundle = basmala_bundle()
        bundle["qac_morphemes"] = [{"qac_ref": "100:0:1:1"}]
        with self.assertRaisesRegex(composition.CompositionError, "outside linguistic"):
            composition.validate_unit_bundle(bundle, expected_ref="100:0")

    def test_prefatory_bundle_requires_surface_equivalence(self) -> None:
        bundle = basmala_bundle()
        bundle["coverage"]["basmala_alias"]["normalized_surface_equivalent"] = False
        with self.assertRaisesRegex(composition.CompositionError, "surface equivalence"):
            composition.validate_unit_bundle(bundle, expected_ref="100:0")

    def test_prefatory_bundle_rejects_forged_normalization_record(self) -> None:
        bundle = basmala_bundle()
        bundle["coverage"]["basmala_alias"].update({
            "target_normalized": "forged",
            "source_normalized": "forged",
        })
        with self.assertRaisesRegex(composition.CompositionError, "surface equivalence"):
            composition.validate_unit_bundle(bundle, expected_ref="100:0")

    def test_prefatory_bundle_rejects_self_consistent_non_basmala_surface(self) -> None:
        bundle = basmala_bundle()
        bundle["text"]["arabic_uthmani"] = "نَصٌّ آخَرُ"
        forged = composition.normalize_arabic_surface(
            bundle["text"]["arabic_uthmani"]
        )
        bundle["coverage"]["basmala_alias"].update({
            "target_normalized": forged,
            "source_normalized": forged,
        })
        with self.assertRaisesRegex(composition.CompositionError, "surface equivalence"):
            composition.validate_unit_bundle(bundle, expected_ref="100:0")


class ProjectionTests(unittest.TestCase):
    def test_prefatory_basmala_uses_the_same_nonfocus_projection_shape(self) -> None:
        focus = numbered_bundle("100:1")
        focus["qac_morphemes"] = [{
            "qac_ref": "100:1:1:1",
            "root_ar": "ف ع ل",
            "surface_ar": "فعل",
        }]
        ordinary = numbered_bundle("100:2")
        ordinary["text"] = {"arabic_uthmani": "سَطْرٌ"}
        ordinary["qac_morphemes"] = [{
            "qac_ref": "100:2:1:1",
            "root_ar": "س ط ر",
            "surface_ar": "سَطْرٌ",
        }]
        prefatory = basmala_bundle()
        prefatory["qac_morphemes"] = [{
            "qac_ref": "1:1:1:1",
            "root_ar": "س م و",
            "surface_ar": "بِسْمِ",
        }]

        ordinary_payload = composition.context_member_payload(
            ordinary, focus_bundle=focus
        )
        prefatory_payload = composition.context_member_payload(
            prefatory, focus_bundle=focus
        )

        self.assertEqual(set(prefatory_payload), set(ordinary_payload))
        self.assertEqual(
            set(prefatory_payload["context_ayat"][0]),
            set(ordinary_payload["context_ayat"][0]),
        )
        self.assertEqual(
            prefatory_payload["protocol"], composition.CONTEXT_MEMBER_PROTOCOL
        )
        for forbidden in (
            "word_analysis",
            "qac_morphemes",
            "root_lexicon",
            "v12_focus_trace_hermetic",
        ):
            self.assertNotIn(
                forbidden, json.dumps(prefatory_payload, ensure_ascii=False)
            )

    def test_projection_uses_native_context_depth_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            projects_root = Path(temporary)
            source_path = projects_root / "prose_generation" / "bundle.json"
            source_path.parent.mkdir()
            bundle = numbered_bundle("100:1")
            bundle["text"] = {"arabic_uthmani": "سَطْرٌ"}
            bundle["qac_morphemes"] = [{
                "qac_ref": "100:1:1:1",
                "word_index": 1,
                "root_ar": "س ط ر",
                "surface_ar": "سَطْرٌ",
                "lemma_ar": "سَطْر",
                "source_pos": "N",
            }]
            bundle["branch_inventories"] = {
                "full_context_packet": {
                    "branch_inventories": [{
                        "root": "س ط ر",
                        "branches": [{
                            "branch_id": "B001",
                            "image_ar": "نظم السطر",
                            "scope_ar": "must not be projected for context",
                            "variants": [{
                                "root_id": "root_000001",
                                "image_ar": "نظم السطر",
                            }],
                        }],
                    }],
                }
            }
            bundle["coverage"] = {
                "root_lexicon": {
                    "per_root": {
                        "س ط ر": {
                            "root_mapping": {
                                "targets": [{
                                    "target_rank": 1,
                                    "furuq_root_id": "root_000001",
                                    "furuq_root_norm": "س ط ر",
                                }]
                            }
                        }
                    }
                }
            }
            bundle["root_lexicon"] = {
                "root_000001": {
                    "dictionary_entry": {"must_not_survive": "dictionary"},
                    "gloss": {"must_not_survive": "gloss"},
                }
            }
            bundle["v12_focus_trace_hermetic"] = {
                "readers": {"must_not_survive": "prior HFT"}
            }
            bundle["v12_reader_walks"] = {"must_not_survive": "prior walk"}
            bundle["inter_ayah_rows"] = [{"must_not_survive": "inter ayah"}]
            bundle["channel_generated_outputs"] = {
                "must_not_survive": "channel output"
            }
            source_path.write_text(json.dumps(bundle), encoding="utf-8")
            analysis = composition.composition_from_cli(
                "s100-plus-s17",
                ["s100=100:1", "external=17:50"],
                ["17:50"],
            )
            row = analysis.context_rows("17:50")[0]

            projected = composition.project_context_unit(
                context_row=row,
                bundle=bundle,
                focus_bundle=numbered_bundle("17:50"),
            )

        self.assertEqual(projected["context_kind"], "ordered_context_ayah")
        self.assertFalse(projected["focus_eligible"])
        self.assertNotIn("candidate_id", projected)
        self.assertNotIn("support_ids", projected)
        payload = projected["evidence"]
        self.assertEqual(payload["protocol"], composition.CONTEXT_MEMBER_PROTOCOL)
        self.assertEqual(payload["context_order"], ["100:1"])
        self.assertEqual(payload["context_ayat"], [{
            "ref": "100:1",
            "text_ar": "سَطْرٌ",
            "root_sequence": ["س ط ر"],
            "root_occurrences": [{
                "root": "س ط ر",
                "occurrence_count": 1,
                "word_indices": ["1"],
                "surfaces_ar": ["سَطْرٌ"],
                "lemmas_ar": ["سَطْر"],
                "pos_tags": ["N"],
            }],
        }])
        self.assertEqual(payload["context_root_cues"], [{
            "root": "س ط ر",
            "targets": [{
                "mapped_root_id": "root_000001",
                "mapped_root_norm": "س ط ر",
                "branches": [{
                    "branch_id": "B001",
                    "branch_image_ar": "نظم السطر",
                }],
            }],
        }])
        projected_text = json.dumps(payload, ensure_ascii=False)
        for forbidden in (
            "qac_morphemes",
            "word_analysis",
            "word_morpheme_spans",
            "coverage",
            "root_lexicon",
            "branch_inventories",
            "v12_focus_trace_hermetic",
            "v12_reader_walks",
            "inter_ayah_rows",
            "channel_generated_outputs",
            "must_not_survive",
        ):
            self.assertNotIn(forbidden, projected_text)
        self.assertEqual(projected["lane"], "global")
        self.assertNotIn("source_file", projected)
        self.assertNotIn("context_projection_sha256", projected)

    def test_projection_omits_context_cue_for_a_focus_root(self) -> None:
        context = numbered_bundle("100:1")
        context["qac_morphemes"] = [{
            "qac_ref": "100:1:1:1",
            "root_ar": "س ط ر",
            "surface_ar": "سطر",
        }]
        focus = numbered_bundle("17:50")
        focus["qac_morphemes"] = [{
            "qac_ref": "17:50:1:1",
            "root_ar": "س ط ر",
            "surface_ar": "سطر",
        }]

        payload = composition.context_member_payload(context, focus_bundle=focus)

        self.assertEqual(payload["context_ayat"][0]["root_sequence"], ["س ط ر"])
        self.assertEqual(payload["context_root_cues"], [])

    def test_projection_keeps_compact_branches_for_every_split_root_target(self) -> None:
        context = numbered_bundle("100:1")
        context["qac_morphemes"] = [{
            "qac_ref": "100:1:1:1",
            "root_ar": "س م و",
            "surface_ar": "اسم",
        }]
        context["coverage"] = {
            "root_lexicon": {
                "per_root": {
                    "س م و": {
                        "root_mapping": {
                            "targets": [
                                {
                                    "target_rank": 1,
                                    "furuq_root_id": "root_primary",
                                    "furuq_root_norm": "س م و",
                                },
                                {
                                    "target_rank": 2,
                                    "furuq_root_id": "root_secondary",
                                    "furuq_root_norm": "و س م",
                                },
                            ]
                        }
                    }
                }
            }
        }
        context["branch_inventories"] = {
            "full_context_packet": {
                "branch_inventories": [{
                    "root": "س م و",
                    "branches": [{
                        "branch_id": "B001",
                        "image_ar": "علو",
                        "variants": [{"root_id": "root_primary", "image_ar": "علو"}],
                    }],
                }]
            }
        }
        context["root_lexicon"] = {
            "root_secondary": {
                "root_ar": "س م و",
                "qac_roots_ar": ["س م و"],
                "dictionary_entry": {
                    "branches": [{
                        "branch_ref": "root_secondary/B003",
                        "branch_image_ar": "وسم",
                        "large_record": "must not be projected",
                    }]
                },
            }
        }

        payload = composition.context_member_payload(
            context, focus_bundle=numbered_bundle("17:50")
        )

        targets = payload["context_root_cues"][0]["targets"]
        self.assertEqual(
            [(target["mapped_root_id"], target["branches"]) for target in targets],
            [
                ("root_primary", [{"branch_id": "B001", "branch_image_ar": "علو"}]),
                ("root_secondary", [{"branch_id": "B003", "branch_image_ar": "وسم"}]),
            ],
        )
        self.assertNotIn("large_record", json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    unittest.main()
