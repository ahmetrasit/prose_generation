"""Bounded delivery and failure handling for the five approved source items."""

import copy
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

from _commentary.v5 import reviewed_supplements as supplements


def packets(ref="29:38"):
    return {
        "micro": {
            "identity": {"ayah_ref": ref},
            "candidate_inventory": [{
                "source_type": "word_analysis", "source_local_id": topic,
            } for topic in supplements.MICRO_REFERENCES["29:38"]],
        },
        "macro": {"candidate_inventory": [{
            "branch_refs": list(supplements.MACRO_LEXICAL_SOURCES["29:38"]),
        }]},
        "global": {"candidate_inventory": []},
    }


class ReviewedSupplementTests(unittest.TestCase):
    def test_other_focus_and_absent_candidates_do_not_load_or_add_evidence(self):
        other = packets("29:39")
        absent = packets()
        absent["micro"]["candidate_inventory"] = []
        absent["macro"]["candidate_inventory"] = []
        for case in (other, absent):
            with self.subTest(case=case):
                before = copy.deepcopy(case)
                loader = Mock(side_effect=AssertionError("unrequested lexical source"))
                with patch.object(supplements.packet_evidence, "_morphology",
                                  side_effect=AssertionError("unrequested morphology")):
                    result = supplements.attach(case, {}, Path("unused"), Path("cache"), loader)
                self.assertEqual(case, before)
                self.assertEqual(result["micro_reference_refs"], [])
                self.assertEqual(result["macro_lexical_sources"], {})
                loader.assert_not_called()

    def test_missing_arabic_or_morphology_cannot_publish_a_partial_supplement(self):
        quran = {ref: {"arabic_uthmani": "نص"} for ref in ("7:201", "29:39")}
        for sources, morphology, expected in (
            ({"7:201": quran["7:201"]}, ({}, None, None), "Arabic is missing"),
            (quran, ({"7:201": [["7:201:1:1"]]}, None, "hash"), "QAC morphology"),
        ):
            with self.subTest(expected=expected):
                case = packets()
                before = copy.deepcopy(case)
                loader = Mock()
                with patch.object(supplements.packet_evidence, "_morphology", return_value=morphology):
                    with self.assertRaisesRegex(supplements.SupplementError, expected):
                        supplements.attach(case, sources, Path("unused"), Path("cache"), loader)
                self.assertEqual(case, before)
                loader.assert_not_called()

    def test_missing_lexical_boundary_cannot_publish_either_lane(self):
        case = packets()
        before = copy.deepcopy(case)
        refs = ("7:201", "29:39")
        quran = {ref: {"arabic_uthmani": "نص"} for ref in refs}
        morphology = {ref: [[ref + ":1:1"]] for ref in refs}
        row = {field: "source text" for field in supplements.LEXICAL_FIELDS}
        row["branch_ref"] = "root_000347/B011"
        row.pop("what_is_not_ar")
        loader = Mock(return_value={"root_lexicon": {"root_000347": {
            "dictionary_entry": {"branches": [row]}}}})
        with patch.object(supplements.packet_evidence, "_morphology",
                          return_value=(morphology, None, "hash")):
            with self.assertRaisesRegex(supplements.SupplementError, "incomplete source fields"):
                supplements.attach(case, quran, Path("unused"), Path("cache"), loader)
        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
