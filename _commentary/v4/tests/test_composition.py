from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "composition.py"
SPEC = importlib.util.spec_from_file_location("commentary_v4_composition", MODULE_PATH)
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


class BundleValidationTests(unittest.TestCase):
    def test_prefatory_bundle_keeps_positive_linguistic_refs(self) -> None:
        identity = composition.validate_unit_bundle(
            basmala_bundle(), expected_ref="100:0"
        )
        self.assertEqual(identity["surface_ref"], "100:0")
        self.assertEqual(identity["linguistic_source_ref"], "1:1")

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


class ProjectionTests(unittest.TestCase):
    def test_projection_preserves_full_raw_hft_packet_and_qualifies_prior_readings(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            projects_root = Path(temporary)
            source_path = projects_root / "prose_generation" / "bundle.json"
            source_path.parent.mkdir()
            raw_hft_path = projects_root / "latent" / "100_1.packet.json"
            raw_hft_path.parent.mkdir()
            raw_hft = {
                "protocol": "focus-trace-hermetic-packet-v2",
                "focus_ref": "100:1",
                "large_evidence": {"must_survive": ["a", "b", "c"]},
            }
            raw_hft_path.write_text(json.dumps(raw_hft), encoding="utf-8")

            bundle = numbered_bundle("100:1")
            bundle["v12_focus_trace_hermetic"] = {
                "packet_summary": {
                    "focus_ref": "100:1",
                    "source_file": "latent/100_1.packet.json",
                },
                "readers": {"reader": {"finding": "prior"}},
            }
            source_path.write_text(json.dumps(bundle), encoding="utf-8")
            analysis = composition.composition_from_cli(
                "s100-plus-s17",
                ["s100=100:1", "external=17:50"],
                ["17:50"],
            )
            identity = composition.validate_unit_bundle(
                bundle, expected_ref="100:1"
            )
            identity.update({
                "canonical_sha256": composition.canonical_sha256(bundle),
                "bytes": source_path.stat().st_size,
            })
            row = analysis.context_rows("17:50")[0]

            candidate, supports, inventory = composition.project_context_unit(
                composition=analysis,
                focus_ref="17:50",
                context_row=row,
                source_path=source_path,
                bundle=bundle,
                identity=identity,
                projects_root=projects_root,
            )

        hft_support = next(
            support
            for support in supports
            if support["source_type"] == "selected_context_prior_hft"
        )
        self.assertEqual(
            hft_support["payload"]["source_packet"]["packet"], raw_hft
        )
        self.assertEqual(candidate["anchor_refs"], ["100:1"])
        self.assertEqual(inventory["lane"], "global")
        prior_walk = next(
            support
            for support in supports
            if support["source_type"] == "selected_context_prior_reading"
        )
        self.assertIn("original focus", prior_walk["payload"]["boundary"])


if __name__ == "__main__":
    unittest.main()
