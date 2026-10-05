**Enrichment reference efficiency audit — 2026-10-05**

The best next step is to improve passage addressing and retrieval while retaining the complete source archive. Summaries can help choose what to open; replacing the archive, or treating summaries as sufficient evidence for every claim, would work against the requested near-zero loss. Most format conversion has already happened.

**This requires both workflow and data fixes.** Workflow changes control what the reader receives and how often it reads it. Data changes correct the reference units, verse associations and extraction that the workflow relies on. A smaller prompt alone cannot correct a misassigned passage; better segmentation alone does not stop the reader from fetching it repeatedly. These recommendations are proposed work, not a record of completed fixes.

| Priority | Track | Concrete work | Acceptance evidence |
|---|---|---|---|
| 1 | Workflow: retrieval | Exact-segment reads; explicit sibling/neighbor reads; matching excerpts; complete output budgets; resumable notes and translations; visible extraction/routing flags | A locator returns only its requested unit; every omitted span has a continuation; repeated pages do not repeat notes; relevant matches and quality flags are visible |
| 2 | Data: mapping and extraction | Narrow Abū Ḥayyān's inherited ranges; distinguish shared Elmalılı/Biqāʿī discussion from local comments; repair surah boundaries and flagged Arabic | Original text remains recoverable; corrected mappings are checked against source passages; footnotes, page identity and old citation aliases survive; uncertain assignments remain searchable |
| 3 | Both: corpus and packet reuse | Share exact repeated bodies with separate provenance; align editions; clean layout markup; reduce duplicate dictionary, meal and occurrence material in packets | All 16 default tafsir authors and all edition-specific evidence remain accessible; packet content is deduplicated without merging distinct testimony |
| 4 | Workflow with derived data | Optional reusable work profiles and passage indexes, followed by retrieval of exact supporting and contrary evidence | Reduced actual input and repeat exposure, with no critical evidence loss on the evaluation set below; summaries alone never establish source coverage |

Fix extraction and mapping in the importers as well as the derived corpus, so a rebuild preserves the correction. Rebuild the affected index and packs against versioned inputs once corrected; preserve existing accepted pages and their citation provenance. Keep source preservation, retrieval recall and final page quality as separate acceptance criteria.

This is an audit of `enrichment/v2`, the enrichment pass after v16/augment9, plus its separate Bible/intertext index. No production code, corpus, pack, prompt, or accepted page was changed. No enrichment or summarization models were run. The measured snapshot and supporting reproductions are versioned in [audits/2026-10-05-source-efficiency](audits/2026-10-05-source-efficiency/README.md); the read-only inventory script is [tools/audit_sources.py](tools/audit_sources.py). This records the state inspected on 2026-10-05; later corpus changes require a new scan.

**Scope and measurement.** The Islamic index contains 220 source records: 196 local sources and 24 memory-only pointers; 972,428 segments; 478,162,345 primary-text characters; and 48,370,162 additional characters in translations/notes that the retrieval tool can display. The physical corpus has 201 `segments.jsonl` files, including the five intertext collections. The intertext index also includes shared Quran, reference and modern sources, so its totals must not be added to the Islamic index as unique holdings.

The rankings below count Unicode characters, not model tokens or billed input. They reproduce `pack.sources_md`: every segment whose inclusive `s/a/a_end` range contains the ayah. Each segment is counted once per matching ayah. They exclude headings, wrappers, notes, the frozen base, root lexica and other references found only through search. All 6,236 ayat and 114 surahs were measured. Coverage differs: the 16 original per-ayah tafsir collections cover Fātiḥa and late surahs; the whole-book collections cover much more. These are rankings of the available corpus, not an intrinsic complexity ranking of the Quran. A large attached set does not mean a worker actually read all of it.

Independent SQL checks reproduce the totals for 1:1, 1:7, 2:196, 112:1 and 105:1. Ayah, surah and source aggregates reconcile. The main database's modification time did not change during the audit.

**What the documents are, and what to do with their formats.**

| Reference material | Current holdings and form | Useful change | Summary suitability |
|---|---|---|---|
| Arabic tafsir | 44 local source records + 3 pointers; per-ayah web extracts and whole-book OpenITI text, already in JSONL/SQLite | Align commentary paragraphs to actual ayat; distinguish general introductions, passage discussions and cross-references. Reconcile alternative editions at paragraph level. | Passage/topic navigation summaries are useful; retain each attribution, alternative, objection, preference and exact evidence span. |
| Turkish tafsir | Elmalılı and Kur'an Yolu; Elmalılı's six PDFs are already converted into page text and 2,796 indexed segments | Repair flagged Arabic extraction; preserve page and footnote links; improve narrow retrieval within long passage groups | Useful for long excursuses; direct quotation and textual variants require the original passage and its relevant notes. |
| Lexica and grammar | 20 local lexicon sources + 6 pointers, and Sībawayh; imported SQLite/root records and OpenITI-derived entries | Clean leftover layout markup into a rendered view; store page anchors separately; split oversized entries by actual headword/sense; display root-routing caveats | A generic root summary is unsafe for this project's lexical-image work. Keep sense inventory, rare concrete senses, collocations, poetry and contrasts accessible verbatim. |
| Maʿānī/gharīb, wujūh, readings | 8 maʿānī sources; 2 local wujūh works + 1 pointer; 6 local qirāʾāt sources + 1 pointer | Preserve structural headings, verse/word mapping, reading forms and named readers; retrieve complete arguments with adjacent context | Useful as an index. Do not replace exact alternative readings, grammatical constructions or sense distinctions. |
| Hadith and occasion/chronology literature | 9 hadith sources; 9 `ulum` sources; Arabic records with optional translations and grading fields; OpenITI text | Retrieve the Arabic and requested translation, with collection/number and all relevant grading/attribution metadata; separate the report from extended commentary | Summary only for discovery. Citation needs the report and attribution; a summary must not manufacture a grade or turn a Companion statement into a Prophetic report. |
| Meals and English controls | 76 local Turkish meal records + 3 pointers; 16-meal panel; Asad and Arberry; JSON, HTML and text imports | Read the panel and controls as a compact comparison; retrieve wider alternatives when needed; share identical display text while retaining every translator, edition and lineage | Do not summarize wording used for translation comparison. Possessives, particles, brackets, additions and omissions are the evidence. |
| Ishārī, naẓm, poetry, sīra | 5 local ishārī sources; 2 local naẓm works + 4 pointers; 4 poetry and 3 sīra sources | Preserve poem/hemistich structure and narrative boundaries; use topic indexes and exact passage retrieval | Good candidates for orientation summaries, with full text retained for relevant interpretation and quotation. |
| TDV İA, Corpus Coranicum, Turkish word history | HTML/JSON converted to articles/entries; Turkish dictionaries count under lexicon | Split long articles by section; keep bibliography and dated attestations attached to the passages they support | Summarize background. Preserve dating qualifications, competing views and the exact earliest attestations. |
| Bible/intertext pass | WLC XML, SBLGNT and KJV verse text, Sefaria JSON, Corpus Coranicum intertext records; separate index | Keep book/chapter/verse, witness, language and dating; share each intertext body across its Quran-reference links | Discovery summaries are useful. Comparison requires the actual relevant passages and witness information. |
| Frozen base and reference pack | Markdown prose; JSON binding/provenance; per-ayah words, dictionary, usage, meals, source lists and Turkish entries; per-root files | Read the numbered base once; share repeated dictionary bodies; retrieve usage examples rather than always printing all occurrences | Do not replace the frozen base or binding with a summary. They define the claims being enriched and their paragraph/word identity. |

The raw-format inventory found **only six PDFs**, all Elmalılı, plus **70 OpenITI book-text files**, 15,370 compressed HTML files, 114 uncompressed HTML files, JSON/text files, 39 WLC XML files, and a KJV ZIP. Original-v1 and upstream dictionary backing stores are separate from this physical count. The workers generally consume the extracted corpus and Markdown pack, not these downloads. ZIP/gzip and compacting the on-disk JSON therefore do not reduce model input after the text is rendered.

Elmalılı already has 6,107 page-text files and glyph-level extraction. There are **137 segments marked `arabic_reliable: false`**. Its build report records 1,096 unmatched Quran quotations and another 263 too short to match. Successfully matched Quran quotations were replaced with canonical Uthmani text, so the searchable view is not always the literal typography/wording of the printed quotation. Keep the PDF, extraction, match provenance and normalized search form distinct. `corpus.py show` currently does not expose the reliability flag to the reader. Conversion should be improved at these flagged passages, not repeated indiscriminately. PDF extraction can lose reading order, footnote relationships or glyph identity even when there is a text layer; the [pypdf extraction documentation](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) explains these limitations.

**Which ayat have the largest attached source sets.** Primary-text characters, before notes and other pack inputs:

| Rank | Ayah | Characters | Main contributors |
|---|---|---:|---|
| 1 | 1:1 | 1,094,387 | Rāzī FULL 222,556; Ālūsī slice 107,206 + FULL 82,830; Ibn Kathīr slice 69,544; Elmalılı 68,663 |
| 2 | 1:7 | 671,564 | Rāzī FULL 65,912; Abū Ḥayyān FULL 53,027; Rāzī slice 37,474; Elmalılı 31,993 |
| 3 | 2:196 | 649,052 | Ṭabarī FULL 93,874; Qurṭubī FULL 62,600; Abū Ḥayyān FULL 57,657 |
| 4 | 2:102 | 596,362 | Ṭabarī FULL 53,112; Ibn Kathīr FULL 52,626; Rāzī FULL 50,657 |
| 5 | 5:3 | 583,778 | Ṭabāṭabāʾī 70,992; Ṭabarī FULL 39,351; Ibn ʿĀshūr FULL 38,462 |
| 6 | 1:2 | 560,976 | Abū Ḥayyān FULL 51,479; Ālūsī slice 46,163; Elmalılı 45,852 |
| 7 | 3:7 | 554,794 | Ṭabāṭabāʾī 111,763; Abū Ḥayyān FULL 52,111; Kur'an Yolu 35,209 |
| 8 | 2:282 | 554,184 | Abū Ḥayyān FULL 61,720; Qurṭubī FULL 47,936; Ṭabarī FULL 45,129 |
| 9 | 5:6 | 509,336 | Rāzī FULL 57,905; Qurṭubī FULL 45,193; Ālūsī FULL 35,549 |
| 10 | 2:187 | 497,631 | Abū Ḥayyān FULL 79,600; Ṭabarī FULL 44,385; Qurṭubī FULL 38,533 |

All of Fātiḥa: **1:1 1,094k; 1:2 561k; 1:3 227k; 1:4 354k; 1:5 397k; 1:6 308k; 1:7 672k**. Across the late surahs, the largest individual lookups are **112:1 423k, 105:1 338k, 112:4 308k, 112:2 284k, 108:1 277k, 110:3 258k, and 112:3 253k**. Fātiḥa 1:1 also has 14,087 displayable notes/translation characters beyond its primary-text total.

**Which surahs are heaviest per ayah.** Mean attached primary-text characters:

| Surah | Mean per ayah |
|---|---:|
| 1 — Fātiḥa | 516,241 |
| 112 — Ikhlāṣ | 317,020 |
| 105 — Fīl | 246,643 |
| 33 — Aḥzāb | 221,438 |
| 110 — Naṣr | 219,318 |
| 108 — Kawthar | 212,047 |
| 2 — Baqara | 208,566 |
| 5 — Māʾida | 198,694 |
| 97 — Qadr | 197,937 |
| 106 — Quraysh | 177,250 |

For comparison, the means for current project examples are S87 **90,991**, S100 **83,385**, and S107 **101,726**. Across the entire Quran the mean is 123,629 and median 111,709 characters. In cumulative ayah lookups, the largest surahs are S2 **59.65M**, S3 **28.58M**, S7 **27.69M**, S4 **26.55M**, and S5 **23.84M**. Those totals include repeated retrieval of shared ranges; they are not the cost of a surah-page call, which has a different scope.

**The largest avoidable inflation is range assignment.** There are 304.60M characters in distinct ayah-attached segments. Counting each at every attached ayah expands this to 770.95M, a 2.53× exposure. Some shared passage material belongs to several ayat, so this is not a promise that all of the difference can be removed.

| Source | Attached text stored once | Across all matching ayat | Expansion |
|---|---:|---:|---:|
| Abū Ḥayyān FULL | 11.27M | 225.21M | 19.97× |
| Ṭabāṭabāʾī | 12.33M | 61.48M | 4.99× |
| Elmalılı | 9.87M | 45.83M | 4.64× |
| Thaʿlabī | 5.53M | 26.52M | 4.79× |
| Biqāʿī FULL | 10.13M | 28.45M | 2.81× |

Abū Ḥayyān alone accounts for **29.2%** of primary text exposed across all ayah lookups. Its own metadata admits broad range-level assignment. In S33, **67 chunks / 113,573 characters** are attached to every ayah **33:1–73**; one inspected middle chunk discusses 33:34–35 while retaining the whole-surah range. Other large shared groups include **40:1–85 (86,805 characters), 28:1–88 (83,204), 26:1–104 (59,153), and 43:1–89 (64,869)**. This is a mapping problem with a clear precision improvement available; it is not proof that the commentary itself should be abbreviated.

For the late-surah work, **Elmalılı 105:1–5 is 85,959 characters retrieved for each of five ayat**, and **112:2–4 is 87,288 characters retrieved for each of three ayat**. Biqāʿī likewise has extensive shared Ikhlāṣ material. Separate genuine passage-wide discussion from paragraph-specific evidence and keep both retrievable. One inspected Biqāʿī segment, `BIQAI-FULL:v8p603`, even opens the next surah, al-Falaq, while still indexed under 112:1–4; boundary checks belong in this work.

At surah level, the largest ratios of cumulative ayah retrieval to distinct attached text are S26 **5.90×**, S80 **5.49×**, S55 **5.06×**, S84 **4.86×**, S68 **4.78×**, and S37 **4.75×**. These provide useful tests for range-aware retrieval beyond the currently prepared packs.

**Other savings, and their limits.**

1. **Two editions of a work need alignment, not automatic deletion.** At 1:1, 14 same-ID/`-FULL` pairs account for 362,533 slice characters plus 481,590 whole-book characters. The bodies are not generally identical. A sample comparison of normalized seven-word sequences finds 95.4% overlap of the Rāzī slice at 107:7 with its FULL counterpart, but only 0.4% at 1:1: the web slice there gives introductory matter while FULL contains the long basmala discussion. This diagnostic is not semantic equivalence. Preserve the 16-author research set; select an appropriate primary edition and retrieve verified shared passages once, retaining all alternative readings and extra material.
2. **Exact whole-segment deduplication is a modest global gain.** Repeated primary bodies total 4.03M characters, only **0.84%** of the Islamic corpus. It helps specific sources: **1.20M of al-ʿAyn's 2.44M characters** repeat under multiple root routes. For example, the same 26,942-character body occurs under eleven locators. Share that body with its aliases, but retain the actual headword and route status so an alias is not mistaken for an independent lexical entry. Different isnāds, translations and editions must retain their distinct evidence identity.
3. **Lexical markup remains in model-facing text.** The inspected lexical/grammar sources contain 1,495,433 characters of `PageV…`, `ms…`, `~~` and paragraph-marker syntax. This measurement excludes surrounding whitespace. A clean display view can remove layout artifacts while keeping page/paragraph identity as metadata. Some Lisān entries are also very large: `LISAN:ريا` is 125,322 characters. Correct entry boundaries and internal sections matter more than changing the filename extension.
4. **The pack repeats material and eagerly expands reference sets.** `dictionary.md` and per-root files repeat the project branches; the older dossier adds classical entries already in the root files, and repeats meals already in `meals.md`. The newer `dosya2` excludes meals, translations and Quran from its extract, which is an improvement. Fātiḥa's current `usage.md` alone is 37,724 characters for 1:1 and 48,113 for 1:2. Keep counts and a compact occurrence index in the initial packet; retrieve actual cross-Quran examples in batches as the comparison requires. Meal files currently include the full wider reference set, not just the panel.
5. **Repeated context can dominate actual cost.** The saved 1:1 run records 88 turns, 89 commands and 24,752,353 cached input tokens, with a historical cost figure of $13.97. These are not 24.75M unique source tokens. Reading the right passages once, batching independent retrieval and avoiding duplicated citation checks can matter as much as shortening the first packet. Citation verification can reopen only the cited span plus sufficient context.
6. **Intertexts have straightforward identity reuse.** Corpus Coranicum's intertext collection has 242 records / 1.43M characters, and repeats the same TUK document under several Quran references. Store one document body per TUK/version and separate its reference links; keep the distinct relationship metadata. This improves storage and prevents duplicate inclusion within a combined packet, but saves no tokens if the same body was already read only once in a call. In the separate intertext index, the biggest directly attached lookups include 1:1 (64.8k) and 88:5–7 (about 54.4k each); WLC/KJV/SBLGNT passages discovered independently are additional.

**Retrieval defects worth fixing before adding summaries.**

| Finding | Evidence and consequence | Recommended behavior |
|---|---|---|
| Search previews are passage prefixes | `cmd_search` sends matched rows to `show`, which prints the first 300 characters. In a ten-result `رحمان` search, four results did not show the matching word in that prefix. | Show the matching span, with paragraph boundaries and offsets into the original text. Keep a headword hit distinct from a body hit. |
| The total cap does not cover all rendered fields | `show` caps the primary text, then prints `en`, `tr`, and `notes` without the remaining-call-budget check. A 100-character reproduction with `ELMALILI:1:1` counted 200 body/note characters; wrapper characters are additional. | Budget the whole response, including metadata; expose continuation cursors for every truncated field. |
| Notes can be cut silently and repeated on each page | Extra fields are independently sliced to `--chars`, without their own cut/continuation notice. `--from` advances the main text but reprints the extras from their beginning. | Page linked notes independently; print those relevant to the selected span and offer the rest explicitly. |
| A locator also selects sibling chunks | `get ELMALILI:105:1-5` selects all sixteen siblings: 85,959 body characters before the output cap, although the exact base segment is only 4,571. Requesting the base and explicit siblings can repeat them. `--from` is also applied separately to every selected sibling. | Exact-segment retrieval by default; explicit family/neighbor retrieval; deduplicate requested segment IDs; resume one specific segment/field. Preserve existing citation aliases. |
| Quality metadata is hidden | Elmalılı's `arabic_reliable` and lexical `route` information live in `extra` but are not printed by `show`. | Always expose extraction quality, headword routing and inferred range status beside the evidence. |
| `--exact` is not an exact phrase option | It suppresses prefix matching for each word, then joins the words as separate FTS terms. The older dossier labels such a lookup “exact search.” | Offer separate whole-token, phrase and root/lemma search modes; retain current normalized search for discovery. |
| Bounded extracts select source openings | `dossier.bounded` takes the first 5,000 characters per source until the global budget is used. Its `chars_shown` accounts for body text, not all rendered extras. | Select by paragraph/topic and coverage, keeping all source IDs and explicit unread spans. Do not equate “source opened” with “source covered.” |

[SQLite FTS5 supports matching snippets](https://www.sqlite.org/fts5.html#the_snippet_function), but the current FTS table is contentless and indexes normalized text. A correct implementation must either provide retrievable indexed content plus mappings to original text or compute original-text windows itself; simply inserting `snippet()` into the existing query is insufficient.

Ayah indexing is also incomplete in places. The current corpus has **3,401 Jishumī segments / 4.34M characters with no ayah**, **2,178 Ibn ʿĀshūr FULL / 3.07M**, **1,308 Durr FULL / 2.07M**, and **2,534 Bursevī / 3.63M**. Some are legitimate introductions and excursuses. A summary/extract pipeline limited to `ayah S:A` will not see them; full-book and surah-level search must remain available.

**When summaries are acceptable.** A short profile of each work is safe as a navigation aid: identity, edition, coverage, genre, strengths, limitations and search vocabulary. For long passages, a compact topic/evidence index can point to exact spans covering each distinct position. Generate and version such indexes once per source passage, reusing them across ayat; generating them afresh inside every ayah run forfeits much of the benefit.

The page writer may start from those indexes instead of reading every complete book/passage. It should fetch the exact source span for every quotation, disputed attribution, reading, lexical sense, grade, date or translation claim it actually uses, including supporting notes and enough surrounding argument to avoid reversing the author's position. Claims of absence or novelty also need searches beyond the summary. Keep disagreements, rejected interpretations, qualifying language and minority views in the index, not just the preferred conclusion.

The existing `okuma` pilot is a warning about economics, not proof that all summaries are useless. Seven completed readers currently contain **1,041 JSON lines: 1,003 non-empty cards and 38 empty markers**, totaling **353,044 characters**, with $6.03 recorded reader cost. The cost plan estimated roughly $19–20 for the complete reading-and-judging design. Its recall checker checks whether a cited **locator** has a card; it does not verify that every proposition, qualification or counterexample from that locator survived. Thus the earlier “53/53” result does not establish lossless summarization. A reusable, much smaller navigational index is a different design, but its benefits remain to be measured.

For the stated objective, the appropriate structure is **immutable original → faithful full text with provenance → searchable passage/claim index → small retrieved evidence packet**. Summary text is one optional search field, alongside exact original text and structural identifiers. This preserves the archive while reducing what each worker sees. It does not guarantee perfect research recall; that requires evaluation.

**Recommended order of work.**

1. Fix exact-segment addressing, match-centered previews, complete response budgeting, continuations and visible quality metadata. This can save reading without discarding evidence or requiring model-generated summaries.
2. Improve verse/paragraph assignment for Abū Ḥayyān; then shared Elmalılı and Biqāʿī passages. Retain parent passage links and uncertain assignments as searchable candidates. Check the next-surah boundary example above.
3. Render cleaner lexical text, share exact repeated bodies/aliases, and align overlapping editions while preserving edition differences and all 16 default tafsir authors. Make occurrence lists and the wider meal set accessible without dumping them all initially.
4. Add cached work profiles and passage indexes where the remaining material is still large. Use selective verbatim evidence, rather than either whole-book dumps or summary-only evidence.
5. Evaluate on 1:1, 1:7, 2:196, 3:7, 33:35, 105:1/4, 107:7 and 112:1–4. Include questions derived from previously unread passages, minority views, rare senses, footnotes and counter-evidence, not just citations in an accepted page. Measure actual model input, unique source spans read, repeat exposure, retrieval recall, attribution correctness, quote fidelity and missed disagreements. Separate archive preservation from research recall and page quality; require no critical evidence loss before adopting a compressed path.

**Audit artifacts and code evidence.**

- [All ayat, ranked](audits/2026-10-05-source-efficiency/islamic_ayah.csv), [all surahs](audits/2026-10-05-source-efficiency/islamic_surah.csv), [source inventory with coverage and quality notes](audits/2026-10-05-source-efficiency/islamic_sources.csv).
- [Corpus scan script](tools/audit_sources.py), [format inventory](audits/2026-10-05-source-efficiency/formats.json), [retrieval reproductions](audits/2026-10-05-source-efficiency/retrieval_proofs.json), [edition-overlap diagnostic](audits/2026-10-05-source-efficiency/edition_overlap_sample.json), [lexical markup counts](audits/2026-10-05-source-efficiency/lexicon_markup.json).
- Current workflow: [design](DESIGN.md), [cost history](COST_PLAN.md), [research scope](prompts/zengin.md#L35).
- Retrieval: [response rendering](tools/corpus.py#L472), [locator expansion](tools/corpus.py#L519), [search](tools/corpus.py#L555), [bounded extraction](dossier.py#L169).
- Mapping/quality: [range assignment](fetch/openiti_parse.py#L290), [source QA notes](fetch/openiti_works.py#L289), [Elmalılı provenance](../corpus/ELMALILI/source.json), [build report](../corpus/ELMALILI/build_report.json).
- Summary pilot: [recall checker](okuma.py#L630), [saved 1:1 usage](work/s001/zengin.1_1.opus.high/run.log.json).
