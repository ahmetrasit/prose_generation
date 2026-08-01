import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import prepare_tts_chunks as prepare  # noqa: E402


class PrepareTtsChunksTest(unittest.TestCase):
    def test_turkish_ordinal_generation(self):
        for number, expected in (
            (1, "birinci"),
            (5, "beşinci"),
            (21, "yirmi birinci"),
            (100, "yüzüncü"),
            (105, "yüz beşinci"),
            (286, "iki yüz seksen altıncı"),
        ):
            with self.subTest(number=number):
                self.assertEqual(prepare.turkish_ordinal(number), expected)

    def test_canonical_ayah_text_is_loaded_by_reference(self):
        verses = prepare.load_quran_text()
        self.assertEqual(verses["1:5"], "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ")

    def test_inline_annotation_conversion_discards_transliteration(self):
        text = "Bir {ar:ٱلْحَمْدُ, tr:el-hamdü, gloss:o belirli hamd} duyulur."
        converted, count = prepare.replace_inline_tokens(text)
        self.assertEqual(
            converted,
            "Bir ٱلْحَمْدُ (o belirli hamd) duyulur.",
        )
        self.assertEqual(count, 1)

    def test_legacy_colon_gloss_spelling_is_supported(self):
        converted, count = prepare.replace_inline_tokens(
            "{ar:بِ, tr:bi, :gloss:ile ve bağlı olarak}"
        )
        self.assertEqual(converted, "بِ (ile ve bağlı olarak)")
        self.assertEqual(count, 1)

    def test_malformed_annotation_fails(self):
        with self.assertRaises(ValueError):
            prepare.replace_inline_tokens("{ar:بِ, tr:bi}")

        for malformed in (
            "{ar:بِ, tr:, gloss:ile}",
            "{ar:بِ, tr:bi, gloss:ile, extra:x}",
            "{ar:بِ, tr:bi, gloss:ile, :gloss:again}",
            "{ar:بِ, tr:bi, gloss:ile}}",
            "{ar:بِ, tr:bi, gloss:ile",
        ):
            with self.subTest(malformed=malformed):
                with self.assertRaises(ValueError):
                    prepare.replace_inline_tokens(malformed)

    def test_ayah_markdown_is_flattened_without_wrapper_heading(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "1_1.prose.tr.md"
            source.write_text(
                "Bir {ar:بِ, tr:bi, gloss:ile} başlangıç.\n\n"
                "İkinci paragraf.\n",
                encoding="utf-8",
            )
            paragraphs = prepare.parse_ayah_paragraphs(source)

        self.assertEqual(len(paragraphs), 2)
        self.assertEqual(paragraphs[0]["text"], "Bir بِ (ile) başlangıç.")

    def test_real_ayah_source_builds_without_tokens_in_tts_text(self):
        source = prepare.QURAN_DATA_ROOT / "data/commentary/ayah/detailed/tr/s001"
        files = prepare.collect_source_files(source, "ayah")
        artifacts = prepare.build_artifacts(
            source,
            "ayah",
            files,
            "S001",
            Path("/private/tmp/unused-audio-output"),
            "ayah",
        )

        self.assertGreater(len(files), 0)
        self.assertGreater(artifacts["rawTokenCount"], 0)
        self.assertGreater(len(artifacts["chunks"]), 0)
        for chunk in artifacts["chunks"]:
            self.assertNotIn("{ar:", chunk["ttsText"])
            self.assertNotIn("tr:", chunk["ttsText"])

    def test_single_ayah_cannot_replace_existing_collection_implicitly(self):
        source_dir = prepare.QURAN_DATA_ROOT / "data/commentary/ayah/detailed/tr/s001"
        source_file = source_dir / "1_5.prose.tr.md"
        files = prepare.collect_source_files(source_dir, "ayah")
        single_files = prepare.collect_source_files(source_file, "ayah")

        with tempfile.TemporaryDirectory() as directory:
            full = prepare.build_artifacts(
                source_dir,
                "ayah",
                files,
                "S001",
                Path(directory).resolve(),
                "ayah",
            )
            prepare.write_artifacts(full)

            single = prepare.build_artifacts(
                source_file,
                "ayah",
                single_files,
                "S001",
                Path(directory).resolve(),
                "ayah",
            )
            with self.assertRaisesRegex(ValueError, "--replace-existing --prune"):
                prepare.write_artifacts(single)
            with self.assertRaisesRegex(ValueError, "requires --prune"):
                prepare.write_artifacts(single, replace_existing=True)

    def test_surah_title_is_attached_to_first_audio_unit(self):
        source = prepare.QURAN_DATA_ROOT / "data/commentary/surah/detailed/tr/s001"
        files = prepare.collect_source_files(source, "surah")
        artifacts = prepare.build_artifacts(
            source,
            "surah",
            files,
            "S001",
            Path("/private/tmp/unused-audio-output"),
            "surah",
        )

        self.assertEqual(len(artifacts["chunks"]), 12)
        first = artifacts["chunks"][0]
        self.assertTrue(first["titleAttachedToFirstParagraph"])
        self.assertTrue(first["ttsText"].startswith("Yolda Tutulan “Biz”."))
        self.assertTrue(first["text"].startswith("Fâtiha’nın ortasında"))

    def test_ayah_commentary_has_no_synthetic_reference_unit(self):
        source = prepare.QURAN_DATA_ROOT / "data/commentary/ayah/detailed/tr/s001"
        files = prepare.collect_source_files(source, "ayah")
        artifacts = prepare.build_artifacts(
            source,
            "ayah",
            files,
            "S001",
            Path("/private/tmp/unused-audio-output"),
            "ayah",
        )

        self.assertEqual(len(artifacts["chunks"]), 66)
        self.assertEqual(
            artifacts["manifest"]["arabicTextSource"],
            "data/text/quran-uthmani.tsv",
        )
        for section in artifacts["manifest"]["sections"]:
            first = section["paragraphs"][0]
            self.assertEqual(first["kind"], "paragraph")
            self.assertFalse(first["titleAttachedToFirstParagraph"])
            self.assertEqual(first["ttsText"], first["text"])
            self.assertNotIn("ayah_reference", [paragraph["kind"] for paragraph in section["paragraphs"]])
            self.assertNotIn("section_title", [paragraph["kind"] for paragraph in section["paragraphs"]])

    def test_ayah_recitation_uses_one_joined_canonical_unit_per_ayah(self):
        source = prepare.QURAN_DATA_ROOT / "data/commentary/ayah/detailed/tr/s001"
        files = prepare.collect_source_files(source, "ayah")
        artifacts = prepare.build_artifacts(
            source,
            "ayah",
            files,
            "S001",
            Path("/private/tmp/unused-audio-output"),
            "ayah-recitation",
        )

        self.assertEqual(len(artifacts["chunks"]), 7)
        self.assertEqual(artifacts["manifest"]["collection"], "ayah-recitation")
        self.assertIn("One joined ttsText per ayah", artifacts["manifest"]["titleHandling"])
        self.assertEqual(
            artifacts["chunks"][4]["ttsText"],
            "Fâtiha 5: إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
        )
        self.assertEqual(artifacts["chunks"][4]["kind"], "ayah_recitation")
        self.assertEqual(artifacts["chunks"][4]["text"], "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ")
        self.assertNotIn("{ar:", artifacts["chunks"][4]["ttsText"])
        self.assertNotIn("gloss:", artifacts["chunks"][4]["ttsText"])
        self.assertNotEqual(artifacts["manifest"]["prompt"], prepare.PROMPT)


if __name__ == "__main__":
    unittest.main()
