#!/usr/bin/env python3
"""Focused tests for word-analysis to morpheme-span resolution."""

from __future__ import annotations

import unittest

import build_bundle as bb


class WordMorphemeSpanTests(unittest.TestCase):
    def test_alef_maqsura_matches_ya_surface(self) -> None:
        self.assertEqual(
            bb.normalize_arabic_surface("إِلَيَّ"),
            bb.normalize_arabic_surface("إِلَىَّ"),
        )

    def test_skip_does_not_start_inside_qac_word(self) -> None:
        morphemes = [
            {
                "qac_ref": "29:8:16:1",
                "word_id": "w-s029-a008-w016",
                "morpheme_id": "m-w-s029-a008-w016-01",
                "surface_ar": "إِلَىَّ",
            },
            {
                "qac_ref": "29:8:16:2",
                "word_id": "w-s029-a008-w016",
                "morpheme_id": "m-w-s029-a008-w016-02",
                "surface_ar": "",
            },
            {
                "qac_ref": "29:8:17:1",
                "word_id": "w-s029-a008-w017",
                "morpheme_id": "m-w-s029-a008-w017-01",
                "surface_ar": "مَرْجِعُ",
            },
            {
                "qac_ref": "29:8:17:2",
                "word_id": "w-s029-a008-w017",
                "morpheme_id": "m-w-s029-a008-w017-02",
                "surface_ar": "كُمْ",
            },
        ]

        matched, span_start, span_end, skipped = bb._find_word_span_from_position(
            morphemes,
            0,
            bb.normalize_arabic_surface("مَرْجِعُكُمْ"),
        )

        self.assertTrue(matched)
        self.assertEqual((span_start, span_end, skipped), (2, 4, 2))

    def test_resolves_29_8_ilayya_then_marjikum_without_crossing_words(self) -> None:
        record = {
            "words": [
                {
                    "surface_display": "{{ar:إِلَيَّ}} ({{tr:ilayya}})",
                    "aligned_qac_word_ref": "29:8:21",
                },
                {
                    "surface_display": "{{ar:مَرْجِعُكُمْ}} ({{tr:marjiʿukum}})",
                    "aligned_qac_word_ref": "29:8:22",
                },
            ]
        }
        morphemes = [
            {
                "qac_ref": "29:8:16:1",
                "word_id": "w-s029-a008-w016",
                "morpheme_id": "m-w-s029-a008-w016-01",
                "surface_ar": "إِلَىَّ",
            },
            {
                "qac_ref": "29:8:16:2",
                "word_id": "w-s029-a008-w016",
                "morpheme_id": "m-w-s029-a008-w016-02",
                "surface_ar": "",
            },
            {
                "qac_ref": "29:8:17:1",
                "word_id": "w-s029-a008-w017",
                "morpheme_id": "m-w-s029-a008-w017-01",
                "surface_ar": "مَرْجِعُ",
            },
            {
                "qac_ref": "29:8:17:2",
                "word_id": "w-s029-a008-w017",
                "morpheme_id": "m-w-s029-a008-w017-02",
                "surface_ar": "كُمْ",
            },
        ]

        spans, unresolved = bb.resolve_word_morpheme_spans(record, morphemes)

        self.assertEqual(unresolved, [])
        self.assertEqual(spans[0]["qac_refs"], ["29:8:16:1", "29:8:16:2"])
        self.assertEqual(spans[1]["qac_refs"], ["29:8:17:1", "29:8:17:2"])


if __name__ == "__main__":
    unittest.main()
