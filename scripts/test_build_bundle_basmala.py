#!/usr/bin/env python3

from __future__ import annotations

import sys
import unittest
from contextlib import redirect_stderr
from io import StringIO
from unittest.mock import patch

import build_bundle as builder


class BasmalaBundleTests(unittest.TestCase):
    def test_numbered_and_bundle_unit_discovery_are_separate(self) -> None:
        s1 = {f"1:{ayah}": "text" for ayah in range(1, 8)}
        s9 = {f"9:{ayah}": "text" for ayah in range(1, 4)}
        s100 = {"100:0": "basmala", **{
            f"100:{ayah}": "text" for ayah in range(1, 12)
        }}

        self.assertEqual(builder.discover_ayah_numbers(100, s100), list(range(1, 12)))
        self.assertEqual(builder.discover_bundle_unit_numbers(1, s1), list(range(1, 8)))
        self.assertEqual(builder.discover_bundle_unit_numbers(9, s9), [1, 2, 3])
        self.assertEqual(
            builder.discover_bundle_unit_numbers(100, s100),
            [0, *range(1, 12)],
        )

    def test_normalized_surface_equivalence_ignores_quranic_marks(self) -> None:
        self.assertEqual(
            builder.normalize_basmala_surface(
                "\ufeffبِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"
            ),
            builder.normalize_basmala_surface(
                "بسم الله الرحمن الرحيم"
            ),
        )

    def test_dedicated_builder_preserves_alias_and_target_context(self) -> None:
        qac_rows = [{
            "qac_ref": "1:1:1:1",
            "qac_word_ref": "1:1:1",
            "root_ar": "",
        }]
        target_line = {"ayahRef": "100:0", "reading_text_tr": "target"}
        with (
            patch.object(
                builder,
                "build_ayah_bundle",
                side_effect=AssertionError("normal ayah builder must not run"),
            ),
            patch.object(
                builder,
                "load_morphemes_tsv",
                return_value=({}, {"present": False, "source_file": None}, None),
            ),
            patch.object(
                builder,
                "build_word_qac_alignment",
                return_value=([], {"present": True, "unresolved": [], "linguistic_source_ref": "1:1"}),
            ),
            patch.object(
                builder,
                "load_v12_branch_inventories",
                return_value=({"full_context_packet": {}}, {"present": True}),
            ),
            patch.object(
                builder,
                "build_root_lexicon",
                return_value=({}, {"present": True}),
            ),
            patch.object(
                builder,
                "load_v12_reader_responses",
                return_value=({"reader": {"target": True}}, {"present": True}),
            ),
            patch.object(
                builder,
                "load_v12_reader_walks",
                side_effect=[
                    ({"reader_a": {"target": True}}, {"present": True}),
                    ({"reader_wide": {"target": True}}, {"present": True}),
                ],
            ),
            patch.object(
                builder,
                "load_v12_cross_run_publication",
                return_value=({"ayah_ref": "100:0"}, {"present": True}),
            ),
            patch.object(
                builder,
                "load_butuncul_okuma",
                return_value=({"100:0": target_line}, {"present": True}, None),
            ),
            patch.object(
                builder,
                "load_channel_review",
                return_value=({}, {"present": False}, None),
            ),
            patch.object(
                builder,
                "channel_blocks_for_ayah",
                return_value=[{"target": "100:0"}],
            ),
            patch.object(
                builder,
                "load_channel_generated_outputs",
                return_value=({"files": []}, {"present": True}),
            ),
        ):
            bundle = builder.build_basmala_bundle(
                100,
                target_quran_text={
                    "100:0": "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"
                },
                source_quran_text={
                    "1:1": "\ufeffبِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"
                },
                source_word_analysis={"1:1": {"ref": "1:1", "words": []}},
                source_qac_by_ayah={1: qac_rows},
                source_root_id_map={},
                source_alignment={"detail": {}},
            )

        self.assertEqual(bundle["unit_kind"], "prefatory_basmala")
        self.assertEqual(bundle["ayahRef"], "100:0")
        self.assertEqual(bundle["surface_ref"], "100:0")
        self.assertEqual(bundle["linguistic_source_ref"], "1:1")
        self.assertEqual(bundle["qac_morphemes"], qac_rows)
        self.assertEqual(bundle["word_analysis"]["ref"], "1:1")
        self.assertTrue(
            bundle["coverage"]["basmala_alias"][
                "normalized_surface_equivalent"
            ]
        )
        self.assertEqual(
            bundle["coverage"]["v12_focus_trace_hermetic"]["status"],
            "not_applicable",
        )
        self.assertEqual(bundle["coverage"]["inter_ayah"]["status"], "not_applicable")
        self.assertEqual(bundle["v12_reader_walks"]["reader_a"]["target"], True)
        self.assertEqual(bundle["v12_reader_walks_wide"]["reader_wide"]["target"], True)
        self.assertEqual(bundle["v12_cross_run_publication"]["ayah_ref"], "100:0")
        self.assertEqual(bundle["butuncul_okuma_line"], target_line)
        self.assertFalse(any("100:0:" in str(row) for row in bundle["qac_morphemes"]))

    def test_surface_mismatch_is_rejected_before_evidence_loading(self) -> None:
        with self.assertRaisesRegex(builder.RequiredSourceMissing, "surface mismatch"):
            builder.build_basmala_bundle(
                100,
                target_quran_text={"100:0": "different"},
                source_quran_text={"1:1": "basmala"},
                source_word_analysis={},
                source_qac_by_ayah={},
                source_root_id_map={},
            )

    def test_cli_rejects_spans_starting_at_zero(self) -> None:
        argv = [
            "build_bundle.py",
            "--surah",
            "100",
            "--ayah-from",
            "0",
            "--ayah-to",
            "11",
        ]
        with patch.object(sys, "argv", argv):
            with redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit):
                    builder.main()


if __name__ == "__main__":
    unittest.main()
