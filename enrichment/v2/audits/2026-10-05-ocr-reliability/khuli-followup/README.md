# Al-Khūlī: digital editions, two-witness OCR and section priorities

Audit date: **2026-10-05**. This checks the user's three-step proposal against the actual source listings, local scan and prior six-page experiment.

**Prioritizing the tafsīr section is justified. The digital edition remains an unverified lead. Sol/Tesseract disagreement finds many errors, but fresh Sol crop readings did not reliably correct them.** No candidate was accepted into the production corpus.

## 1. Digital editions and supplementary studies

The [VitalSource listing](https://www.vitalsource.com/products/v14048ktab) identifies the exact title and author, Ktab Inc., a first-edition label, **Fixed Layout**, product identifier `14048KTAB`, and a US price of $29.99. The listing was available through search; direct retrieval failed. Neither fixed layout nor generic search/read-aloud features establish a clean Arabic text layer. Fixed layout also does not prove the book is image-only. No body sample or edition correspondence was verified.

VitalSource's [official FAQ](https://www.vitalsource.com/faqs) distinguishes offline access inside Bookshelf from downloading an ordinary ebook file, and says copying/printing restrictions vary by title. Therefore this is **not yet an equivalent to the downloadable Shamela export**. Before acquiring it for corpus ingestion, establish both text fidelity and an available full-text export. A useful sample should include the opening, a tafsīr passage, quotations and footnotes; compare it with the 1961 scan and retain edition-specific locators.

An additional [Ktab Google Play listing](https://play.google.com/store/books/details?id=2NlPEQAAQBAJ) offers a free sample and lists 274 pages, March 2025 and $15.99. The [Google Books catalog](https://books.google.com/books?id=2NlPEQAAQBAJ) has a contents list and indexed Arabic terms. Its preview did not load here. The different page count requires investigation; neither identity with the VitalSource master nor completeness against our 368-page scan is established. No purchase was made.

Both suggested Hindawi books are useful **secondary studies**, with different authors:

| Study | Author | Verified access | Corpus role |
|---|---|---|---|
| [الهِرْمِنيوطيقا: بوصفها منهجًا للتفسير عند أمين الخولي](https://www.hindawi.org/books/28184726/) | ʿAbd al-Jabbār al-Rifāʿī | Readable HTML; EPUB/PDF/KFX offered | Hermeneutics and literary interpretation; separate secondary source |
| [أمين الخولي والأبعاد الفلسفية للتجديد](https://www.hindawi.org/books/86174619/) | Yumnā Ṭarīf al-Khūlī | Readable HTML; EPUB/PDF/KFX offered | Renewal and philosophical context; separate secondary source |

The publisher links currently resolve to Hindawi-branded `safahat.org` pages. The relevant HTML chapters are [literary interpretation](https://www.safahat.org/books/28184726/4/) and [philosophical horizons of interpretation](https://www.safahat.org/books/86174619/2/). Prefer EPUB/HTML extraction over OCR when acquiring these. Preserve headings, footnotes, links and the original package; cite their own chapter/paragraph anchors. Do not label their prose as Amīn al-Khūlī's primary text or use it to reconstruct missing *Manāhij* wording.

**Download status:** EPUB fetches returned HTTP 403, including escalated retries; no EPUB package was acquired or inspected. The first publisher page also displays a download login prompt. Public HTML readability is verified, full local acquisition is pending. [source_checks.json](source_checks.json) separates confirmed metadata, failures and remaining questions.

## 2. What the two-witness test actually shows

“Tesseract never invents a word” is too strong. It is not a generative prose model, but it can substitute, insert, merge, split or omit recognized text. Its [official quality guidance](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) describes dictionary and segmentation effects. Use it as another fallible witness, not as the authority when it differs from Sol.

We compared the **final prior Sol outputs** with existing same-scan Internet Archive Tesseract XML, preserving word boxes and separate flags for missing-word gaps. No new Tesseract run occurred. These six pages are **four Bint pages and two Khūlī rhetoric pages (PDF 92 and 100)**, not six Khūlī pages and not a tafsīr quality sample.

| Diagnostic | Bint al-Shāṭiʾ | Al-Khūlī |
|---|---:|---:|
| Frozen reference words | 234 | 206 |
| Known Sol word-edit errors | 8 | 19 |
| Errors directly flagged by disagreement | 6/8 | **18/19** |
| Errors flagged when adjacent context is included | 8/8 | **19/19** |
| Correct reference-aligned Sol tokens also directly flagged | 64/226 | **68/188** |

For Khūlī's two whole-page outputs, disagreement flags **246/542 Sol tokens (45.4%)**, plus 22 gaps. With adjacent-line fallback for words missing from Tesseract, **49/49 XML lines** receive an alert. This helps locate trouble, but it does not yet produce a small review queue. Strict word alignment is sensitive to joins/splits; a future character/span alignment can reduce noise, while keeping numbers, names and negations explicit.

The one Khūlī error missed by a direct flag is an omitted `كما` in the frozen reference; adjacent context catches it. The two Bint misses are an omitted verse number and an omitted lexical form. Matching errors or joint omissions can still escape. The measured detection rates come from eight purposive supervisor-transcribed passages, **not independent human gold or a whole-page accuracy estimate**. Normalization excludes harakāt, punctuation and some spelling distinctions. [witness_results.json](witness_results.json) records exact alignments, hashes and limits.

### Fresh crop readings: tested, but not a reliable repair

Six fresh `gpt-6-sol` agents at verified medium reasoning reread eight crops covering those same reference windows, with surrounding context. They saw neither prior OCR nor reference text and inherited no conversation. The crops retain the original raster pixels: no enhancement, enlargement or additional scan detail. The [manifest](crop_manifest.json) freezes all coordinates, hashes and assignments; native logs confirm original-detail image forwarding.

| Frozen excerpt comparison | Prior whole-page Sol | Fresh crop Sol |
|---|---:|---:|
| Bint normalized word error | 8/234 = 3.4% | **12/234 = 5.1%** |
| Khūlī normalized word error | 19/206 = 9.2% | **39/206 = 18.9%** |
| Khūlī normalized character error | 35/1,104 = 3.2% | **86/1,104 = 7.8%** |

Some readings improve while new ones fail. The Bint crop recovers `الثرى` and verse 135 but loses verse 130. Khūlī p100's crop changes the clearly printed `ولعلى بن أبى طالب` into `ولعل من أن طالب`, and changes the following wording as well. Its opening has several new substitutions and unreadable markers. Image review confirms that crop rereading can damage previously readable text.

This is a **single blind reread configuration**, not proof that all cropping or guided correction fails. Crops were deliberately selected around the old diagnostic windows; automatic selection of every disagreement span was not implemented. Some contain partial neighboring lines, whose markers are not corpus text. No adjudicator was given both witnesses, and no automatic replacement or majority vote was applied. A genuinely checked repair still needs image-based span adjudication, explicit omission checks and a record of every accepted change. An unchanged or agreeing reading is not sufficient evidence of correctness.

Final crop-agent counters: **894,574 input tokens**, including 837,120 cached; **16,470 output**, including 9,655 reasoning. They exclude the supervising agent's research/review. These are native agent-session costs, not just image/transcription tokens. The poor result gives no basis for scaling this wrapper. See [crop_results.json](crop_results.json).

## 3. Tafsīr first, retaining the full book

The local scan's title/imprint identifies **Dār al-Maʿrifa, first edition, September 1961**. Contents, section boundaries and selected headings were checked against rendered images. Canonical locators remain one-based **PDF page numbers**.

| Priority | PDF pages | Printed pages | Pages | Purpose |
|---|---|---|---:|---|
| First section | **271–320** | Body 271–318 | **50** | Tafsīr title and its footnote, blank reverse, complete text and references |
| Start within that section | **304–320** | 302–318 | **17** | `التفسير اليوم`, literary method, references |
| Complete its earlier portion | 271–303 | Main body begins at printed 271 / PDF 273 | 33 | Title, reverse and historical context |
| Next related cluster | **201–217** | 199–215 | **17** | Psychological iʿjāz and Quran interpretation within rhetoric |
| Remaining scope | All other PDF pages | Edition-specific | **301** | Finish the whole book, including other relevant passages |

The first two subranges partition the 50-page section; they are not additional pages. PDF 272 is visually blank. The main text plus references is **48 pages, PDF 273–320**. PDF 309 begins the literary-method subsection mid-page; preserve its earlier text too. PDF 320 contains the references, and PDF 321 starts literary psychology. The rhetoric cluster continues after its psychological-tafsīr heading at PDF 213; it ends on PDF 217 before a blank reverse and the next section title at PDF 219.

Thus the first batch is **13.6% of the book**, deferring 86.4% of initial recognition work without deleting any source material. This is a page-count saving, not a measured token saving. The 17-page rhetoric cluster is not an exhaustive list of Quran-related material elsewhere: the later literary-psychology contents also include artistic iʿjāz. [priority_pages.json](priority_pages.json) records all 368 pages in nonoverlapping batches, visual anchors and image hashes. It is a plan, not an executed OCR queue.

## Recommendation and implementation status

1. Pursue a sample and usable export from Ktab before spending on full-book OCR. Neither store listing currently supplies verified replacement text. Acquire the Hindawi studies separately when available; their own text can be extracted directly.
2. Work on the 50-page tafsīr block first. Use a few actual tafsīr pages for independent, spelling/diacritic-sensitive references before extrapolating quality from rhetoric samples.
3. Retain Sol and Tesseract as immutable candidates. Use disagreement and omission flags to assist a reviewer, then adjudicate against the scan. Do not replace an entire paragraph with a fresh crop result. A candidate-guided model adjudicator remains a possible next experiment, with acceptance contingent on measured improvement; it was not tested here.
4. Keep accepted diplomatic text separate from normalized search text, and retain PDF/region locators and correction provenance. Summaries should route retrieval to exact passages, not replace evidence. For immediate use, verify quotations directly against the image while corpus text remains unaccepted.

This remains **both a workflow and data fix**: source/edition acquisition and page mapping on the data side; candidate comparison, bounded review, acceptance and retrieval on the workflow side. This follow-up creates audit evidence and a priority manifest only. It does not register the supplemental sources, import unverified text or reduce the full 12,026-page objective.

## Reproduce and validate

From the repository root:

```sh
python3 -B enrichment/v2/audits/2026-10-05-ocr-reliability/khuli-followup/test_witnesses.py
python3 -B enrichment/v2/audits/2026-10-05-ocr-reliability/khuli-followup/compare_witnesses.py
python3 -B enrichment/v2/audits/2026-10-05-ocr-reliability/khuli-followup/measure_crops.py
```

`prepare_crops.py` records the fixed crop recipe and refuses to overwrite its frozen manifest. It makes no model calls. `measure_crops.py` requires six completed native sessions, checks frozen inputs and reads final candidate hashes. The alignment checks cover 450 short-sequence/global-or-substring cases plus an explicit missing-word gap. Full OCR witnesses, crop images and candidates remain in ignored `raw/ocr-candidates/`; only instructions, scripts and compact evidence are versioned. No production `raw/ocr/` file was written.
