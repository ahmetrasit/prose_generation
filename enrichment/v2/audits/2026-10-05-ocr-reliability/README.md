# Extraction and OCR reliability — 2026-10-05

**Reliable preservation and page accounting are achievable. The tested local OCR does not meet the requested diplomatic-transcription standard.** Do not publish its Arabic/Urdu output as finished source text. A stronger OCR service must pass an image-based pilot before bulk processing, and even then difficult pages need review. No measured whole-corpus accuracy or near-zero transcription loss is claimed.

**Follow-up completed:** the user authorized a 24-page Luna low/medium pilot. [Measured results](luna-pilot/README.md) show both settings fail the priority Bint al-Shāṭiʾ/al-Khūlī preservation checks. [Machine-readable alternatives](luna-pilot/SOURCE_ALTERNATIVES.md) record the newly acquired structured Bint al-Shāṭiʾ text and checks of Internet Archive, OpenITI and Doha. [LUNA.md](LUNA.md) retains the pre-run estimate. The Mistral option below remains an untested alternative, not a selected provider.

**Sol follow-up completed:** [six isolated-page Sol medium agents](sol-pilot/README.md) improved the same diagnostic excerpts to 3.4% normalized word error for Bint and 9.2% for al-Khūlī. Substitutions, omissions and lost harakāt remain, so no pages were accepted. The report records actual usage and recommends structured-text reconciliation for Bint and a measured region/correction experiment for al-Khūlī.

**Al-Khūlī follow-up completed:** the [digital-edition, disagreement and crop audit](khuli-followup/README.md) checks VitalSource/Ktab and both Hindawi studies, and maps a 50-page tafsīr-first batch. Sol/Tesseract disagreement directly flags 18 of 19 known Khūlī excerpt errors but alerts every sampled line. Six fresh crop agents worsen Khūlī's normalized excerpt word error to 18.9%; blind crop replacement is therefore not accepted. The report preserves measured limits, pending source acquisition and the full-book objective.

## Scope and importer contract

The user's final scope is **26 PDFs / 12,026 PDF pages**: the primary 7,510-page list **plus all 4,516 pages of Iṣlāḥī's Urdu volumes 3–9**. English translations do not replace the Urdu originals. [scope.json](scope.json) records every original path, SHA-256, page count, output path and priority. Bint al-Shāṭiʾ and al-Khūlī come first. **Accepted OCR pages from this pilot: zero; the 12,026-page production batch is pending.**

Required output: `<source>/raw/ocr/<pdf stem>/p0001.txt`, one UTF-8 file for every **one-based PDF page**, including verified blank pages as empty files. Printed-page numbers are separate metadata; Tarama can contain two printed pages on one PDF page. Preserve original spelling, logical-order Arabic and printed harakāt; put footnotes after the body. Use `[?]` for genuinely unreadable stretches after review. Never fill missing text from memory or silently substitute a modern Qur'an text for the printed quotation. Every source also needs `raw/ocr/README.md` with the engine/model, settings and date.

Use scripts for deterministic extraction, OCR requests, checkpointing, naming and completeness checks. Autonomous agents are not required for these steps. Model-assisted transcription or review can be called from a script; it still needs a demonstrated quality level and a cost budget. No agents or paid OCR services were launched in the initial local Tesseract pilot described below; the separately authorized Luna and Sol follow-ups have now completed.

## What was actually tested

- **399 page samples across all 49 downloaded PDFs**, using pypdf 5.9.0 and PDFium through pypdfium2 5.2.0. Sampling includes beginning/end and distributed body positions. Both engines returned no text on 153 samples. No extraction exceptions occurred; that does not make nonempty output correct.
- **12 rendered pages / 13 OCR regions**, using Tesseract.js 7.0.0 with official floating-point `tessdata_best` models for Arabic, Urdu, Turkish, English and German. Settings: 300-dpi PDF rendering, LSTM mode, automatic page segmentation (PSM 3); Tarama's spread was split into left/right regions. Mixed-script pages used multiple language models. Model commit and hashes are retained.
- Visual comparison of Bint al-Shāṭiʾ, Iṣlāḥī Urdu, Tarama, Badawi–Haleem, Akdemir and Sinai against their page images. These are purposive diagnostic examples, **not a statistically representative accuracy benchmark**. No independently transcribed gold set or character/word error rate has yet been established.
- [samples.json](samples.json) and [ocr_results.json](ocr_results.json) contain metrics and paths. Full sample text, OCR layouts/word confidence and images are under each source's git-ignored `raw/ocr-pilot-2026-10-05/`. Original PDFs remain untouched.

| Evidence | Finding | Consequence |
|---|---|---|
| Bint al-Shāṭiʾ v1, PDF p100 | Image reads `والجزاء`; OCR reads `والخزاء`. More words and quotation marks/diacritics are corrupted. | Local Arabic OCR fails the quotation standard even on this short page. |
| Iṣlāḥī Urdu v1, PDF p100 | Numerous broken words; the heading and running prose are substantially corrupted. Engine confidence was 36/100. | This configuration is unsuitable for diplomatic Urdu. Confidence is **not** an accuracy percentage. |
| Tarama v1, PDF p100 (printed pp104–105) | Existing text layer is gibberish. Fresh split-page OCR improves readability but changes the clearly printed `400` to `100`, and damages Ottoman Arabic-script forms and citations. | Needs layout/curvature handling, mixed-script verification and number checks. Turkish-only OCR would lose evidence. |
| Badawi–Haleem, PDF p100 | pypdf returns 21,600 characters of glyph codes; PDFium returns control-code garbage. OCR recovers English prose but damages Arabic and scholarly transliteration. | First investigate deterministic font decoding; otherwise use stronger mixed-script OCR. A nonempty-text test is inadequate. |
| Akdemir, PDF p100 (outside the requested OCR batch) | Existing layer has broken word spacing and reads verse `151` as `15i`; fresh OCR improves Turkish but corrupts the Arabic panel. | Even sources omitted from the OCR list need extraction QA; checking Turkish alone misses lost Arabic. |
| Sinai, PDF p100 | Native extraction is readable; OCR adds an unnecessary recognition step. | Prefer validated native text wherever possible; inspect transliteration and footnotes separately. |
| Other diagnostics | EQ contains private-use characters; many English Iṣlāḥī samples contain unexpected control characters. | Audit embedded quotations and glyph mappings before calling these texts reliable. |

Two extractors reading the same embedded OCR layer are **not independent recognition checks**. Agreement can simply reproduce the same mistake. Likewise, a high OCR confidence score does not establish fidelity. Tesseract's own documentation describes the importance of resolution, skew and segmentation, and limitations with tables. [Tesseract quality guidance](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)

## English Iṣlāḥī volume 6

The acquired `tadabbur-e-quran-vol-6-2.pdf` has 580 pages. PDF p3 identifies **volume 6, surahs 29–39**; p5 lists all eleven surahs, and pp8–9 begin al-ʿAnkabūt. The filename suffix `-2` does **not** establish a missing part 1. This resolves the suspected missing opening at the title/contents/start level; it is not a verse-by-verse completeness certification. Urdu volume 6 remains in scope because the user requested all Urdu volumes.

## Recommended production method

1. Keep originals, raw OCR responses, page coordinates, settings and hashes. Draft recognition goes under `raw/ocr-candidates/`; only accepted transcription goes to `raw/ocr/<stem>/pNNNN.txt`.
2. Establish image-checked reference passages across languages, volumes, layouts, headings, numbers, harakāt, notes and poor scans. Compare actual errors and omissions, not only confidence. Review disagreement with the archive OCR where available, recognizing that neither output is ground truth.
3. Pilot a stronger OCR engine on those pages. **Mistral OCR 4.1 is a candidate, not yet a validated solution for this collection.** Its API offers page output, structural blocks and confidence information. Preserve all returned fields and explicitly resolve image/table placeholders; do not retain only the Markdown body and silently drop other content. [OCR API documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
4. If the pilot passes, process all 26 PDFs in priority order with resumable scripts. Account for every PDF page exactly once. An empty OCR response is an error/review case until the image is confirmed blank. Preserve both printed sides of Tarama spreads in the single PDF-page output, in reading order.
5. Check every page for missing regions, corrupt glyphs, script mismatch, broken order and anomalous numbers; route exceptions for image-based correction. Sample apparently good pages too: confidence can miss substantive mistakes. Verify quoted passages against the original image at use time until sufficiently reviewed. Do not claim every character is correct from sampling alone.
6. Keep diplomatic text separate from a normalized search view. Search may ignore diacritics and normalize variants; the stored transcription and image must preserve them. Summaries are navigation aids, not replacements.

At the checked standard price of **$4 per 1,000 pages**, one OCR 4.1 pass over 12,026 PDF pages is approximately **$48.10**, or **$24.05 at the advertised half-price batch rate**. These figures exclude retries, splitting spreads into extra requests, independent verification and correction. A pilot capped at $1 would make the quality decision concrete before a full run. No OCR API credential was present in this process's environment, and no paid requests or document uploads were made. [Current provider pricing](https://mistral.ai/pricing/api/)

## Reproduce the local pilot

Run from the repository root with pypdf, pypdfium2 and Pillow available:

```sh
python3 -B enrichment/v2/audits/2026-10-05-ocr-reliability/sample_pdfs.py
npm install --prefix .scratch/ocr-reliability-20261005 --cache .scratch/ocr-reliability-20261005/npm-cache --ignore-scripts --no-audit --no-fund tesseract.js@7.0.0
```

Download `ara`, `urd`, `tur`, `eng` and `deu` `.traineddata` files from the official [`tessdata_best` commit e12c65a](https://github.com/tesseract-ocr/tessdata_best/tree/e12c65a915945e4c28e237a9b52bc4a8f39a0cec) into `.scratch/ocr-reliability-20261005/tessdata/`, then run:

```sh
node enrichment/v2/audits/2026-10-05-ocr-reliability/ocr_samples.cjs
```

Warning encountered and resolved: the v7 relaxed-SIMD core crashed with these floating-point models. `ocr_worker.cjs` scopes a feature-detection workaround to this pilot so the working SIMD core is selected, without modifying installed packages. This matches the reported [upstream issue 1080](https://github.com/naptha/tesseract.js/issues/1080). The successful outputs use the workaround, recorded in `ocr_results.json`. This pilot code is not the production importer.
