#!/usr/bin/env python3
"""Focused tests for word-analysis to morpheme-span resolution."""

from __future__ import annotations

import unittest

import build_bundle as bb
from word_morpheme_alignment import surface_forms


class WordMorphemeSpanTests(unittest.TestCase):
    def test_duplicate_analytic_units_do_not_choose_an_arbitrary_owner(self) -> None:
        record = {"words": [{"surface_display": "{{ar:قُلْ}}"}] * 2}
        rows = [{"surface_ar": "قُلْ", "qac_ref": "1:1:1:1",
                 "word_id": "w1", "morpheme_id": "m1"}]
        spans, unresolved = bb.resolve_word_morpheme_spans(record, rows)
        self.assertEqual(spans, [None, None])
        self.assertEqual(len(unresolved), 2)

    def test_contracted_article_does_not_steal_later_preposition(self) -> None:
        record = {"words": [{"surface_display": "{{ar:" + text + "}}"}
                            for text in ("لِ", "التَّقْوَىٰ", "لَ", "هُمْ")]}
        rows = [dict(surface_ar=text, pos=pos, qac_ref=ref,
                     word_id=ref.rsplit(":", 1)[0], morpheme_id=ref)
                for text, pos, ref in (
                    ("لِ", "P", "49:3:13:1"), ("ل", "DET", "49:3:13:2"),
                    ("تَّقْوَىٰ", "N", "49:3:13:3"),
                    ("لَ", "P", "49:3:14:1"), ("هُمْ", "PRON", "49:3:14:2"))]
        spans, unresolved = bb.resolve_word_morpheme_spans(record, rows)
        self.assertEqual(unresolved, [])
        self.assertEqual(spans[2]["qac_refs"], ["49:3:14:1"])

    def test_spelling_equivalences_preserve_distinct_carriers(self) -> None:
        self.assertFalse(surface_forms("إِلَىٰ") & surface_forms("إِلَّا"))
        self.assertFalse(surface_forms("وَٰحِد") & surface_forms("أَحَد"))
        self.assertTrue(surface_forms("صَلَوٰة") & surface_forms("صَلَاة"))
        self.assertTrue(surface_forms("مَسَٰكِن") & surface_forms("مَسَاكِن"))
        self.assertTrue(surface_forms("هُدَىٰهَا") & surface_forms("هُدَاهَا"))

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
