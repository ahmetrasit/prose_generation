# Files that need OCR (checked 2026-10-05)

The user is handling OCR. Each file below has no usable text layer: pypdf finds no text, or the text it finds is
garbage. Paths are relative to `enrichment/corpus/<dir>/raw/acquired-2026-10-05/`.

## Needed (no other text exists)

| # | Source (dir) | File | PDF pages | Language | Why |
|---|---|---|---:|---|---|
| 1 | BINTSHATI | bintshati-vol-1.pdf | 222 | Arabic | major voice; no text layer; the bundled .ocr.txt is noisy and has no page breaks |
| 2 | BINTSHATI | bintshati-vol-2.pdf | 196 | Arabic | as above |
| 3 | KHULI | khuli-manahij-tajdid-1961.pdf | 368 | Arabic | major voice; no text layer; the bundled OCR is noisier |
| 4 | ABDUH-AMMA | abduh-tafsir-juz-amma.pdf | 189 | Arabic | no text layer |
| 5 | MUQATIL-WUJUH | muqatil-wujuh-damin.pdf | 308 | Arabic | text layer missing or garbled |
| 6 | IBNKHALAWAYH-MUKHTASAR | ibnkhalawayh-mukhtasar.pdf | 246 | Arabic | no text layer |
| 7 | ACADEMIC/FARAHI-NIZAM | farahi-nizam-book.pdf | 632 | Arabic | no text layer; the bundled OCR is unusable |
| 8 | ACADEMIC/BADAWI-HALEEM | badawi-haleem-2008.pdf | 1,095 | Arabic + English | the text layer is glyph codes (`/g369/g338…`) |
| 9 | ACADEMIC/ISLAHI-TADABBUR | tadabbur-e-quran-vol-3-surah-tawbah-09.pdf | 110 | English (Arabic quotations) | the only English file without a text layer |
| 10 | ACADEMIC/ISLAHI-TADABBUR | tadabbur-e-quran-vol-1.pdf, -vol-2.pdf | 672 + 633 | Urdu | surahs 1–5 exist only in Urdu (the English set starts at vol. 3, surah 6) |
| 11 | TARAMA | tarama-vol-1.pdf … tarama-vol-8.pdf | 2,839 | Turkish (Latin with diacritics) | the text layer is garbage (`Kaygusuz eder,l lleLi sana qiikrnE`) |

**Total needed: about 7,510 pages.** Rows 1–3 (786 pages) come first: they are the major voices.

## Optional (an English text layer already exists; Urdu only as a cross-check or for gaps)

- **Iṣlāḥī Urdu vols 3–9**: tadabbur-e-quran-vol-3.pdf … -vol-9.pdf, 4,516 pages.
  - English files with text layers exist for surahs 6–8 and 10–19, and for vols 5, 6 (part 2), 7, 8 and 9.
  - Check whether English vol. 6 part 1 exists anywhere. If it does not, the surahs it covers are needed from Urdu vol. 6 (459 pages).

## Not needed (usable text already exists)

- **Text layers good:**
  - EQ;
  - Study Quran (its 117 empty pages are surah separators);
  - Asad;
  - Hamidullah;
  - Atay;
  - Akdemir (its Arabic column is garbage, which is fine: only the Turkish is used);
  - Sinai;
  - Cuypers;
  - Zammit;
  - Nöldeke (73 empty pages, front matter and plates; I will check them);
  - Iṣlāḥī English (except row 9).
- **Jeffery:** the pypdf text lost its spaces, but the archive's .ocr.txt is good, and its running headers give the page breaks.

## What the importer needs from the OCR

1. **One file per PDF page**, numbered by the PDF page, not the printed one:
   - path: `raw/ocr/<pdf stem>/p0001.txt`;
   - alternatively, one file per PDF with form feeds (`\f`) between pages.

   Every page needs a file, including blank pages (empty files). Page numbers are the citation locators, and a missing page is a silent loss.
2. **Diplomatic text:**
   - original spelling;
   - Arabic in logical order;
   - harakāt kept where printed;
   - no normalisation;
   - footnotes kept, after the page body.
3. **Unreadable stretches marked** `[?]`, never guessed.
4. **A line in `raw/ocr/README.md`** saying which engine or model was used, with settings and date, so `source.json` can record provenance and quality.
