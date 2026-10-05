# Luna OCR pilot: results and priority recommendation

**Do not use this Luna configuration for production transcription. Neither low nor medium meets the requested preservation standard for Bint al-Shāṭiʾ or al-Khūlī.** Use the newly acquired structured Bint al-Shāṭiʾ text as a candidate base, reconcile it with the scans, and reserve recognition for gaps and corrections. Al-Khūlī still needs a better recognition/review method. See [machine-readable alternatives](SOURCE_ALTERNATIVES.md).

**Subsequent comparison:** the user then requested Sol. The [completed six-page Sol diagnostic](../sol-pilot/README.md) materially improves recognition but still fails diplomatic preservation. Its results are separate from the original Luna measurements below.

## Executed experiment

On 2026-10-05, twelve fresh native agents ran `gpt-6-luna`: six at low and six at medium, four pages each, without inherited conversation history. They used the same frozen 24 page images and [brief](BRIEF.md), with no competing transcription or source-text lookup. Rendering used PDFium, 300 dpi capped at 3,500 pixels on the longest side. Agent tool records confirm original-detail image forwarding for the priority batches. [Manifest](manifest.json) records input hashes, dimensions and exact output paths; [results](results.json) retain native session IDs, verified model/effort, tool-call metadata, usage and artifact hashes.

All **48 text drafts** were produced. All are under each source's ignored `raw/ocr-candidates/luna-pilot-2026-10-05/`; **none was promoted to `raw/ocr/`**. Forty-seven review files parse as JSON; the low Urdu volume 9 review is malformed and remains preserved as returned. Both efforts correctly returned an empty file for Urdu volume 6 PDF p114, which the supervisor also inspected as blank. Some Urdu drafts explicitly report incomplete transcription. File existence and an agent's `complete: true` are not quality gates.

The user subsequently prioritized Bint al-Shāṭiʾ and al-Khūlī. Detailed image comparison and excerpt measurement therefore focus on **four Bint al-Shāṭiʾ pages and two al-Khūlī pages**. The other 18 paired outputs have structural checks and agent notes, not a completed independent linguistic evaluation. Do not extrapolate their quality from the priority results.

## Priority quality

The supervisor transcribed eight diagnostic passages from the six images: **234 words for Bint al-Shāṭiʾ and 206 for al-Khūlī**. These are purposive examples, not a random sample or independently human-verified gold. The metric removes vowel marks and punctuation, normalizes yeh variants and digit shapes, and aligns excerpts to the closest text span. It is a deliberately forgiving diagnostic; it does not measure diplomatic fidelity or whole-book accuracy. References and normalization are in [priority_references.json](priority_references.json); alignments are inspectable in `results.json`.

| Work | Luna low: word edits / reference words | Luna medium | Existing Archive OCR | Newly found structured text |
|---|---:|---:|---:|---:|
| Bint al-Shāṭiʾ, both volumes | 25/234 — **10.7%** | 22/234 — **9.4%** | 88/234 — **37.6%** | 8/234 — **3.4%** |
| Al-Khūlī | 59/206 — **28.6%** | 86/206 — **41.7%** | 91/206 — **44.2%** | No verified complete structured text found |

Archive and structured-text comparisons use the same references with best-substring alignment; the short Bint p100 Luna comparison uses its complete body text. Rates also count word splits/joins: Archive al-Khūlī's character edit rate is 11.1%, versus Luna low 14.2%, despite its higher word rate. These rates are **not percentages of factual correctness**. Medium's omitted final al-Khūlī passage aligns poorly to unrelated surviving text; its number is a conservative diagnostic, not an exact count of all lost text. No confidence intervals or whole-book accuracy claim are justified.

All six priority page pairs contain material errors. Examples checked against the images:

| Scan locator | Printed evidence | Low output | Medium output |
|---|---|---|---|
| Bint v1 PDF p50 | `الحاقة ٢٨` | Changes the surah name to `الطاقة` | Changes the reference to `الضحى ٨` and alters its quotation |
| Bint v1 PDF p50 | `وليس من أسمائه تعالى (الثرى)`; later `بل لا نعرف` | Replaces `الثرى` with `الغني`; drops the later negation | Also replaces `الثرى` with `الغني` |
| Bint v1 PDF p100 | `يغفر لمن يشاء` | Inserts `لا`, reversing the statement | Keeps this phrase, but drops `أو شرا` earlier and changes `يجز` to `يجزأ` |
| Bint v2 PDF p49 | `النهى أو النفى`; attribution to `الزمخشرى` | Rewrites the interpretation and loses the attribution | Rewrites the interpretation and changes the attribution to `الخثري` |
| Bint v2 PDF p98 | `استغشاء الثياب`; `المعطلة للحس` | Reads `الغياب` and `المغطية` | Also reads `الغياب`; changes the latter to `المغطلة` |
| Al-Khūlī PDF p92, printed p90 | `بديع ابن المعتز`; printed page `٩٠` | Substitutes Ibn Ḥazm, and later another name; prints `١٠٢` | Also substitutes names; prints `٩٢` |
| Al-Khūlī PDF p100, printed p98 | Final paragraphs on ʿUmar and ʿAlī; legible footnote | Numerous substitutions, wrong printed page and footnote numbers | Omits both final paragraphs; labels the legible footnote clipped/unreadable |

All four low Bint outputs contain **zero Unicode combining marks**. Medium retains only 3–4 per page. The scans have abundant printed harakāt. Neither effort follows the diplomatic-text requirement. Several uncertainty notes describe readable words as degraded without marking the invented substitutes in the text.

## Is this a model problem?

It is a demonstrated failure of **this model-and-workflow combination**, not evidence that the underlying books are unreadable. The affected scan words are often clear. Raising reasoning from low to medium does not solve the problem and sometimes increases omissions. Multi-image batching may also contribute: the medium Bint p49 review refers to the *ghashiya* discussion on its other assigned page, p98. Its transcript was corrected within the agent run after a cross-page insertion. This is a reason to test isolated pages or small regions if Luna is reconsidered.

The Luna experiment did not vary model family, one-page versus four-page inputs, crops, rendering resolution or prompting independently. It therefore cannot attribute all errors to model capacity alone. A stronger recognizer with isolated pages was proposed at the end of this pilot and subsequently tested in the linked Sol diagnostic. No bulk production OCR run was started.

## Actual tokens and the 786-page priority scenario

The following usage is from the final native-session counters. Input includes harness/history/tool replay; cached tokens are a **subset** of input. Output includes tool syntax, review notes and messages as well as transcription. Reasoning is a **subset** of output, not an additional charge. Supervisor review/research tokens are excluded.

| Completed run | Input tokens | Cached input | Output tokens | Of which reasoning |
|---|---:|---:|---:|---:|
| Low, 24 pages | 1,406,478 | 1,143,296 | 28,453 | 492 |
| Medium, 24 pages | 1,713,293 | 1,429,376 | 34,287 | 4,013 |
| Both | **3,119,771** | **2,572,672** | **62,740** | **4,505** |

The previous 1.2–1.4M-input pilot estimate understated native-agent overhead. Measured non-reasoning output totals 58,235 tokens, but this includes incomplete/incorrect drafts and must not become a budget for a correct edition.

**Bint al-Shāṭiʾ: 418 pages. Al-Khūlī: 368 pages. Total: 786.** Scaling the observed batches gives this counterfactual one-pass scenario:

| Work | Low input / output | Medium input / output |
|---|---:|---:|
| Bint al-Shāṭiʾ | 15.15M / 0.282M | 20.86M / 0.411M |
| Al-Khūlī | 12.59M / 0.301M | 21.86M / 0.443M |
| Total | **27.74M / 0.583M** | **42.72M / 0.854M** |

Bint's basis is its own four-page batch, including one unusually short page. Al-Khūlī's basis is a mixed batch containing two al-Khūlī and two ʿAbduh pages; per-page allocation is a proxy, not isolated al-Khūlī telemetry. Native tool-round variability is material. Output includes roughly 0.012M reasoning at low or 0.123M at medium. The scenario excludes correction, reruns and review and **is not a recommendation to spend these tokens on failed output**. Native subscription usage is not an API invoice.

## Recommended action

1. **Bint al-Shāṭiʾ:** use the acquired Shamela database/HTML as a searchable candidate. It contains both volumes, structured printed locators and mostly intact wording, but still has typos, quotation changes and omissions. Reconcile all PDF pages, add missing front/end matter, and verify passages against images. Keep raw exports and scans; do not silently call the export a diplomatic transcription.
2. **Al-Khūlī:** retain Archive page XML as a rough alignment/search aid. Existing OCR and both Luna efforts fail. Test improved recognition on a few isolated pages/regions before processing the 368-page book. Doha's 1995 catalogue entry is useful for edition discovery, not a verified downloadable replacement.
3. **Workflow:** prefer validated existing digital text; then deterministic extraction; then recognition only where needed. Preserve page/region identity, raw candidates, hashes and review status. Build normalized search text separately from diplomatic text. Summaries may route retrieval but must not replace evidence.

This remains **both a data and workflow fix**: acquire better textual witnesses and repair coverage/locators, while changing the recognition and acceptance process. The 12,026-page preservation scope remains intact; this pilot has accepted zero production pages.

## Reproduce and inspect

- `prepare.py`: renders the frozen selection and writes the twelve assignments; refuses to overwrite an existing manifest.
- `measure.py`: reads the native session counters and draft files, validates artifacts and computes priority excerpt diagnostics. Requires the local Codex session logs for usage; the captured counters are retained in `results.json`.
- `compare_archives.py`: verifies the downloads in `archive_inputs.json`, reads the acquired SQLite database without mutation, extracts page candidates and compares the same references. Requires the downloaded raw files retained locally.
- `source_checks.json` and `archive_results.json`: provider queries, catalogue checks, downloaded file hashes and bounded coverage findings.

Model drafts and imported full text remain ignored raw data. Only the audit, instructions, reproducibility scripts, manifests and compact evidence are staged.
