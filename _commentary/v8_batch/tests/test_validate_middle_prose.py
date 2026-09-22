from __future__ import annotations

import unittest

from _commentary.v8_batch import validate_middle_prose


SOURCE = (
    "Birinci taşıyıcının anlamı burada olumsuz değildir; sınırı ayrıca "
    "açıklanır.\n\n"
    "İkinci ayrıntının bağlamsal katkısı yalnızca bir ihtimal olarak korunur."
)
PROSE = (
    "Taşıyıcının anlamı olumsuz değildir (1:5 ¶1); bağlamsal katkı ise "
    "ihtimal olarak kalır (1:5 ¶2)."
)


class ValidateMiddleProseTests(unittest.TestCase):
    def codes(self, prose: str, *, max_paragraph_words: int = 180) -> set[str]:
        return {
            finding.code
            for finding in validate_middle_prose.validate(
                SOURCE,
                prose,
                ayah_ref="1:5",
                max_paragraph_words=max_paragraph_words,
            )
        }

    def test_accepts_ledger_free_traceable_prose(self) -> None:
        self.assertEqual(self.codes(PROSE), set())

    def test_reports_transient_structural_metrics_without_a_ledger(self) -> None:
        metrics = validate_middle_prose.structural_metrics(
            SOURCE, PROSE, ayah_ref="1:5"
        )
        self.assertEqual(metrics["source_paragraph_count"], 2)
        self.assertEqual(metrics["output_paragraph_count"], 1)
        self.assertEqual(metrics["multi_source_output_paragraphs"], 1)
        self.assertEqual(metrics["single_source_output_paragraphs"], 0)
        self.assertEqual(metrics["same_position_singleton_paragraphs"], 0)
        self.assertEqual(metrics["output_to_source_paragraph_ratio"], 0.5)
        self.assertEqual(metrics["multi_source_output_paragraph_ratio"], 1.0)

    def test_requires_every_source_paragraph_citation(self) -> None:
        self.assertIn(
            "source_coverage",
            self.codes("Taşıyıcının anlamı olumsuz değildir (1:5 ¶1)."),
        )

    def test_rejects_malformed_citation_even_beside_a_valid_one(self) -> None:
        prose = PROSE + " Bozuk iz (1:5 ¶1–2)."
        self.assertIn("malformed_citation", self.codes(prose))

    def test_rejects_duplicate_number_in_one_citation(self) -> None:
        prose = (
            "Taşıyıcının anlamı olumsuz değildir (1:5 ¶1, ¶1); bağlamsal "
            "katkı ihtimal olarak kalır (1:5 ¶2)."
        )
        self.assertIn("duplicate_paragraph_citation", self.codes(prose))

    def test_density_limit_is_readability_only(self) -> None:
        self.assertIn(
            "overdense_output_paragraph",
            self.codes(PROSE, max_paragraph_words=5),
        )

    def test_rejects_quran_interval_shorthand(self) -> None:
        prose = PROSE + " Bağlam ayrıca (1:1–3) içinde gelişir."
        self.assertIn("quran_interval_shorthand", self.codes(prose))

    def test_requires_level_two_headings(self) -> None:
        self.assertIn("heading_level", self.codes("# Başlık\n\n" + PROSE))


if __name__ == "__main__":
    unittest.main()
