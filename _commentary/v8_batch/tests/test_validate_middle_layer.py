from __future__ import annotations

import copy
import unittest

from _commentary.v8_batch import validate_middle_layer


SOURCE = (
    "Birinci taşıyıcının anlamı burada olumsuz değildir ve bunun sınırı "
    "ayrıntılı biçimde açıklanır.\n\n"
    "İkinci ayrıntının bağlamsal katkısı mümkündür ve başka yorumlar ayrıca "
    "sınırlandırılır."
)
PROSE = (
    "Birinci taşıyıcının anlamı korunur (1:5 ¶1); "
    "ikinci ayrıntı ihtimal olarak kalır (1:5 ¶2)."
)


def valid_ledger() -> dict[str, object]:
    source_words = len(SOURCE.split())
    prose_words = len(PROSE.split())
    return {
        "schema_version": "commentary-v5-middle-claim-ledger-v2",
        "ayah_ref": "1:5",
        "source_paragraph_count": 2,
        "output_paragraph_count": 1,
        "metrics": {
            "source_word_count": source_words,
            "output_word_count": prose_words,
            "retained_word_ratio": prose_words / source_words,
            "multi_source_output_paragraphs": 1,
            "single_source_output_paragraphs": 0,
            "same_position_singleton_paragraphs": 0,
            "output_to_source_paragraph_ratio": 0.5,
        },
        "source_paragraphs": [
            {
                "paragraph": 1,
                "disposition": "substantive",
                "unit_refs": ["p001.u01"],
                "restates_unit_refs": [],
                "note": None,
            },
            {
                "paragraph": 2,
                "disposition": "substantive",
                "unit_refs": ["p002.u01"],
                "restates_unit_refs": [],
                "note": None,
            },
        ],
        "synthesis_clusters": [
            {
                "cluster_ref": "c001",
                "movement_tr": "İki katkı birlikte açıklanır.",
                "unit_refs": ["p001.u01", "p002.u01"],
                "source_paragraphs": [1, 2],
                "output_paragraphs": [1],
                "kind": "synthesis",
                "why_together_or_apart_tr": "İkinci ayrıntı ilk anlamı sınırlar.",
            }
        ],
        "semantic_units": [
            {
                "unit_ref": "p001.u01",
                "source_paragraph": 1,
                "unit_order_in_paragraph": 1,
                "source_anchor": "anlamı burada olumsuz değildir",
                "assertion_tr": "Birinci anlam olumsuz değildir.",
                "truth_status": "negated",
                "role": "foreground",
                "relation": {
                    "classification": "unique",
                    "canonical_unit_ref": "p001.u01",
                    "related_unit_refs": [],
                    "rationale": "Ayrı önermedir.",
                },
                "landing": {
                    "output_paragraph": 1,
                    "anchor": "Birinci taşıyıcının anlamı korunur",
                    "citation": "(1:5 ¶1)",
                },
            },
            {
                "unit_ref": "p002.u01",
                "source_paragraph": 2,
                "unit_order_in_paragraph": 1,
                "source_anchor": "bağlamsal katkısı mümkündür",
                "assertion_tr": "İkinci katkı ihtimaldir.",
                "truth_status": "possible",
                "role": "qualification",
                "relation": {
                    "classification": "related_distinct",
                    "canonical_unit_ref": "p002.u01",
                    "related_unit_refs": ["p001.u01"],
                    "rationale": "İlk önermeyi sınırlar.",
                },
                "landing": {
                    "output_paragraph": 1,
                    "anchor": "ikinci ayrıntı ihtimal olarak kalır",
                    "citation": "(1:5 ¶2)",
                },
            },
        ],
        "audit": {
            "unassessed_source_paragraphs": [],
            "uncited_source_paragraphs": [],
            "unlanded_unit_refs": [],
            "unclustered_unit_refs": [],
            "units_with_nonunique_anchors": [],
            "unresolved_deduplication_questions": [],
            "unmerged_overlap_groups": [],
            "source_mirroring_findings": [],
            "polarity_or_modality_mismatches": [],
            "reader_paragraphs_without_detail_clues": [],
            "overdense_output_paragraphs": [],
            "notes": [],
        },
    }


class ValidateMiddleLayerTests(unittest.TestCase):
    def test_accepts_consistent_v2_pair(self) -> None:
        self.assertEqual(
            validate_middle_layer.validate(
                SOURCE, PROSE, valid_ledger(), ayah_ref="1:5"
            ),
            [],
        )

    def test_rejects_paraphrased_source_anchor(self) -> None:
        ledger = copy.deepcopy(valid_ledger())
        ledger["semantic_units"][0]["source_anchor"] = "anlam olumsuz değildir"

        codes = {
            finding.code
            for finding in validate_middle_layer.validate(
                SOURCE, PROSE, ledger, ayah_ref="1:5"
            )
        }

        self.assertIn("source_anchor_not_exact", codes)

    def test_rejects_landing_citation_that_omits_its_source(self) -> None:
        ledger = copy.deepcopy(valid_ledger())
        ledger["semantic_units"][1]["landing"]["citation"] = "(1:5 ¶1)"

        codes = {
            finding.code
            for finding in validate_middle_layer.validate(
                SOURCE, PROSE, ledger, ayah_ref="1:5"
            )
        }

        self.assertIn("landing_citation_omits_source", codes)

    def test_density_limit_is_a_readability_gate(self) -> None:
        codes = {
            finding.code
            for finding in validate_middle_layer.validate(
                SOURCE,
                PROSE,
                valid_ledger(),
                ayah_ref="1:5",
                max_paragraph_words=5,
            )
        }

        self.assertIn("overdense_output_paragraph", codes)

    def test_rejects_quran_interval_shorthand(self) -> None:
        prose = PROSE + " Fâtiha'nın 1:1–3 bağlamı da anılır."
        codes = {
            finding.code
            for finding in validate_middle_layer.validate(
                SOURCE, prose, valid_ledger(), ayah_ref="1:5"
            )
        }

        self.assertIn("quran_interval_shorthand", codes)


if __name__ == "__main__":
    unittest.main()
