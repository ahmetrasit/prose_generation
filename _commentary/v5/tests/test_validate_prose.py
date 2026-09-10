from pathlib import Path
import contextlib
import io
import tempfile
import unittest

from _commentary.v5 import validate_prose


def codes(text: str) -> list[str]:
    findings = validate_prose.validate_text(text, path=Path("sample.md"))
    return [finding.code for finding in findings]


class ValidateProseTests(unittest.TestCase):
    def test_accepts_valid_paragraph_local_tags(self) -> None:
        text = (
            "{ar:ٱلسَّبِيلِ, tr:es-Sebîl, gloss:tanınan yol} burada açılır.\n\n"
            "{ar:ٱلسَّبِيلِ, tr:es-Sebîl, gloss:tanınan yol} yeni paragrafta yine çalışır.\n"
        )

        self.assertEqual(codes(text), [])

    def test_rejects_double_curly_tags_and_arabic_outside_valid_tag(self) -> None:
        text = "{{ar:ٱلسَّبِيلِ, tr:es-Sebîl, gloss:tanınan yol}}"

        self.assertIn("double_curly_tag", codes(text))
        self.assertIn("malformed_or_nested_braces", codes(text))

    def test_rejects_unknown_qac_field(self) -> None:
        text = "{ar:ٱلسَّبِيلِ, tr:es-Sebîl, gloss:tanınan yol, qac:29:38:20:1}"

        result = codes(text)

        self.assertIn("unknown_tag_field", result)
        self.assertIn("malformed_tag", result)

    def test_rejects_interposed_duplicate_and_colon_prefixed_fields(self) -> None:
        cases = (
            ("{ar:بِ, qac:1:1:1, tr:bi, gloss:ile}", "unknown_tag_field"),
            ("{ar:بِ, tr:bi, tr:bee, gloss:ile}", "duplicate_tag_field"),
            ("{ar:بِ, tr:bi, :gloss:ile}", "malformed_tag"),
            ("{,ar:ب, tr:bi, gloss:ile}", "malformed_tag"),
            ("{ar:ب, tr:bi, gloss:ile,}", "malformed_tag"),
            ("{ar:ب,, tr:bi, gloss:ile}", "malformed_tag"),
            ("{ar:ب, tr:bi qac:1:1:1, gloss:ile}", "unknown_tag_field"),
        )

        for text, expected in cases:
            with self.subTest(text=text):
                result = codes(text)
                self.assertIn(expected, result)
                self.assertIn("malformed_tag", result)

    def test_rejects_missing_and_empty_fields(self) -> None:
        self.assertIn("missing_tag_field", codes("{ar:بِ, tr:bi}"))
        self.assertIn("empty_transliteration", codes("{ar:بِ, tr:, gloss:ile}"))

    def test_rejects_non_letter_arabic_field(self) -> None:
        self.assertIn("ar_field_not_arabic", codes("{ar:،, tr:x, gloss:x}"))

    def test_accepts_arabic_presentation_forms_in_valid_tags(self) -> None:
        self.assertEqual(codes("{ar:ﷲ, tr:Allah, gloss:Allah}\n"), [])
        self.assertEqual(codes("{ar:﷽, tr:bismillah, gloss:besmele}\n"), [])

    def test_rejects_unresolved_placeholder_and_wrapper_label(self) -> None:
        text = "=== PROSE ===\n@@prose_output_path@@\n"

        self.assertEqual(codes(text), ["wrapper_label", "unresolved_placeholder"])

    def test_accepts_reader_subtitles_but_rejects_generic_wrappers(self) -> None:
        self.assertEqual(codes("## Taşın Hafızası\n\nGeçerli Türkçe düzyazı.\n"), [])
        self.assertEqual(codes("# PROSE\n\nGeçerli Türkçe düzyazı.\n"), ["wrapper_label"])
        self.assertIn("no_renderable_prose", codes("## Taşın Hafızası\n"))

    def test_rejects_heading_without_blank_line_separation(self) -> None:
        self.assertEqual(
            codes("Önceki paragraf.\n## Yeni Bakış\nSonraki paragraf.\n"),
            ["heading_spacing", "heading_spacing"],
        )

    def test_rejects_mixed_transliteration_for_identical_arabic_surface(self) -> None:
        text = (
            "{ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:yol} burada açılır.\n\n"
            "{ar:ٱلسَّبِيلِ, tr:as-sabīl, gloss:yol} burada kapanır.\n"
        )

        self.assertEqual(codes(text), ["inconsistent_transliteration"])

    def test_rejects_arabic_outside_tag(self) -> None:
        self.assertEqual(codes("Bu ٱلسَّبِيلِ etiketsizdir.\n"), ["arabic_outside_tag"])
        self.assertEqual(codes("Bu ﷲ etiketsizdir.\n"), ["arabic_outside_tag"])

        findings = validate_prose.validate_text(
            "Bu ٱلسَّبِيلِ ve ﷲ etiketsizdir.\n",
            path=Path("sample.md"),
        )
        self.assertEqual(
            [finding.code for finding in findings],
            ["arabic_outside_tag", "arabic_outside_tag"],
        )

    def test_malformed_annotations_do_not_hide_arabic_outside(self) -> None:
        self.assertIn("arabic_outside_tag", codes("{ar:ب, tr:bi}\n"))
        self.assertIn("arabic_outside_tag", codes("{{ar:ب, tr:bi, gloss:ile}}\n"))

    def test_malformed_annotations_report_parseable_field_issues(self) -> None:
        result = codes("{ar:, tr:, gloss:, qac:x}\n")

        self.assertIn("unknown_tag_field", result)
        self.assertIn("malformed_tag", result)
        self.assertIn("empty_arabic", result)
        self.assertIn("empty_transliteration", result)
        self.assertIn("empty_gloss", result)
        self.assertIn("ar_field_not_arabic", result)

    def test_rejects_effectively_empty_markdown(self) -> None:
        cases = (
            "```markdown\nGeçerli Türkçe düzyazı.\n```\n",
            "~~~markdown\nGeçerli Türkçe düzyazı.\n~~~\n",
            "    Geçerli Türkçe düzyazı.\n",
            "# PROSE\n",
            "<prose>\n</prose>\n",
            "<!-- yalnız yorum -->\n",
            "---\ntitle: prose\n---\n",
            "***\n",
            "* * *\n",
            "```markdown\n~~~\nyalnız kod\n~~~\n```\n",
            "````markdown\n```\nyalnız kod\n````\n",
            "```markdown\n```not-a-close\nyalnız kod\n```\n",
        )

        for text in cases:
            with self.subTest(text=repr(text)):
                self.assertIn("no_renderable_prose", codes(text))

        self.assertEqual(codes("\ufeff"), ["empty_file"])

    def test_accepts_bom_prefixed_prose(self) -> None:
        self.assertEqual(codes("\ufeffGeçerli Türkçe düzyazı.\n"), [])

    def test_rejects_invalid_utf8_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "invalid.md"
            path.write_bytes(b"\xff")

            self.assertEqual(validate_prose.validate_path(path)[0].code, "invalid_utf8")

    def test_cli_returns_nonzero_for_missing_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "missing.md"

            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(validate_prose.main([str(missing)]), 1)

    def test_cli_json_returns_zero_for_valid_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "valid.md"
            path.write_text(
                "{ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:gören ve kavrayanlar}\n",
                encoding="utf-8",
            )

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(validate_prose.main(["--json", str(path)]), 0)


if __name__ == "__main__":
    unittest.main()
