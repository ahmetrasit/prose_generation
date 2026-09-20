from __future__ import annotations

import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from _commentary.v5 import validate_concise


class ValidateConciseTests(unittest.TestCase):
    def test_headings_do_not_consume_source_paragraph_numbers(self) -> None:
        text = "İlk paragraf.\n\n## Başlık\n\nİkinci paragraf.\n"

        self.assertEqual(
            validate_concise.prose_paragraphs(text),
            ["İlk paragraf.", "İkinci paragraf."],
        )

    def test_accepts_complete_explicit_coverage(self) -> None:
        source = (
            "Birinci bulgunun ayrıntılı açıklaması ve sınırı burada verilir.\n\n"
            "## Ara Başlık\n\n"
            "İkinci bulgunun taşıyıcısı ile mekanizması ayrıca açıklanır.\n\n"
            "Üçüncü bulgunun farklı okur katkısı burada korunur."
        )
        concise = (
            "İlk iki bulgu birleşir (1:2 ¶1, ¶2).\n\n"
            "Üçüncü bulgu ayrı kalır (1:2 ¶3)."
        )

        self.assertEqual(
            validate_concise.validate_pair(source, concise, ayah_ref="1:2"), []
        )

    def test_rejects_missing_wrong_and_out_of_range_citations(self) -> None:
        source = "Birinci bulgu.\n\nİkinci bulgu."
        concise = "Yanlış kaynak (1:3 ¶1); taşan kaynak (1:2 ¶4)."

        codes = {
            item.code
            for item in validate_concise.validate_pair(
                source, concise, ayah_ref="1:2"
            )
        }

        self.assertIn("wrong_ayah_citation", codes)
        self.assertIn("paragraph_out_of_range", codes)
        self.assertIn("source_coverage", codes)

    def test_rejects_uncited_and_malformed_output_paragraphs(self) -> None:
        source = "Birinci bulgu."
        concise = "Atıfsız paragraf.\n\nBozuk atıf (1:2 ¶1-2)."

        codes = [
            item.code
            for item in validate_concise.validate_pair(
                source, concise, ayah_ref="1:2"
            )
        ]

        self.assertIn("uncited_output_paragraph", codes)
        self.assertIn("malformed_citation", codes)

    def test_cli_fails_when_a_pair_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(
                    validate_concise.main(
                        [
                            "--analysis-id",
                            "missing",
                            "--surah",
                            "1",
                            "--ayah-count",
                            "1",
                            "--repo-root",
                            str(Path(temporary)),
                        ]
                    ),
                    1,
                )


if __name__ == "__main__":
    unittest.main()
