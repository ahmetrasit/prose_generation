# Independent assessment of ayah enrichment — 2026-10-06

Historical workflow assessment. The current [v3 plan](../../../v3/PLAN.md) and its worker briefs govern the pilot: collect external literature awareness without confirming or criticizing the frozen prose. The one-time local probes mentioned below are not additional v3 stages or tracking requirements.

**Decision: the current workflow does not establish the coverage needed for a tafsir writer to rely on it.** There are useful annotations and useful infrastructure, but both the existing output and executable checks demonstrate omissions that can be reported as success. Novelty decisions need stronger evidence than this workflow currently requires.

The target used here is **v16 r13, with augment9 where available**. The assessment standard comes from the user's current instructions: every substantive claim in every paragraph, including additions, needs concise awareness of relevant earlier positions, differences, and unresolved antecedents. Existing documentation, earlier reviews, source summaries, and the frozen prose itself were not treated as proof that this standard is met.

## What was examined and run

- Read the executable input selection, source grouping/retrieval, prompts, placement, validation, rendering and acceptance paths in `pack.py`, `grup.py`, `enrich.py`, `render.py`, `validate.py`, and `tools/blocks.py`.
- Inventoried the available r13 ayah readings and existing enrichment packs; checked recorded hashes against upstream files and pack copies.
- Rechecked the accepted **1:1** output and compared paragraph coverage in four other 1:1 trials. Read selected frozen paragraphs together with their augment9 additions and actual annotations; this is a substantive sample, not a full scholarly review of every annotation.
- Reconstructed live grouped retrieval for hadith and representative tafsir groups from the corpus database. Checked specific omitted sources directly.
- Exercised validators and completion functions with isolated synthetic cases. Model execution and production logging were mocked only in the two completion-accounting probes; their content validators ran normally. Other probes use the actual functions directly.
- Cross-checked two hadith examples and one tafsir example against public primary-text presentations.

The grouped workflow currently has plans for S1 and S87, with **zero prepared and zero completed grouped calls** in each. Its deficiencies below are demonstrated in planning/retrieval and controlled execution. The 1:1 output examples come from the earlier single-page workflow; they are not represented as outputs of the unrun grouped workflow.

The earlier local probes used read-only corpus access and temporary synthetic files; they did not launch models, rebuild packs or accept pages. Their scripts and raw diagnostic outputs remain local, outside the v3 workflow. The observations below describe those probes, not an enrichment acceptance result.

## 1. There is no complete, enforceable inventory of paragraph claims

**Critical.** `grup.py` gives extraction agents source material without the frozen commentary. `prompts/grup.md` explicitly tells them they do not see the commentary. A later placement call reads the page and puts claims that no line “touches” into `bos.jsonl`. There is no prior inventory against which that gap list is reconciled.

This lets three different omissions escape:

1. A claim is never recognized.
2. A line shares a word or theme with a claim but does not address the actual inference.
3. One tradition addresses a claim, so other relevant traditions and contrary readings are not sought for it.

`check_place()` (`grup.py:1148`) checks paragraph numbers, line dispositions and cluster representatives. It does not check that all claims were identified or assessed. Missing `input_lines.jsonl` and `bos.jsonl` are read as empty lists. A placement containing one source line at paragraph 1, with no gap inventory for the remaining page, passes. An isolated `finish_place()` with an empty placement file and missing input/gap files receives `status: ok`.

The older accepted 1:1 page has **53 valid annotations across 27 numbered prose paragraphs**, with **no annotation at paragraphs 10, 14, 16 or 23**. All 53 records still pass the current record validator. Paragraph 23 is unannotated in every one of the five inspected 1:1 versions:

| 1:1 version | Records | Paragraphs without annotations |
| --- | ---: | --- |
| Accepted `zengin`, Opus high | 53 | 10, 14, 16, 23 |
| `dosya2`, Opus high | 58 | 10, 17, 23 |
| `dosya2`, Opus medium | 45 | 17, 23, 27 |
| `tur`, Opus high | 53 | 23 |
| `tur`, Opus medium | 55 | 23 |

These counts are a lower bound on missing coverage, not an assertion that every other paragraph is adequately covered. A repeated claim could be handled by a clear cross-reference; the workflow has no claim mapping that establishes such coverage here.

**Concrete example inside an annotated paragraph:** paragraph 4 has three annotations about invocation, eating and the legal effect of naming God at slaughter. They do not account for its further connection between the sacrificial animal's journey and *ihdinā*, or its augment9 discussion of 22:37: meat and blood do not reach God, while taqwā does. “Paragraph has annotations” would miss these separate questions.

**Required change:** establish stable claim IDs from the frozen paragraph and all additions before source passes. Each pass must account for those IDs. Review the claim inventory against the prose itself; a machine can enforce reconciliation only after the claims have actually been identified.

## 2. Retrieval misses relevant material already present locally

**Critical.** `search_items()` (`grup.py:275`) searches the target ayah's exact normalized three-word phrases for the hadith group. It does not derive searches from the paragraph's propositions, the augment9 additions, or most cross-referenced ayahs. The search retains at most six hits per query/source and can skip frequent queries entirely.

The live S1 reconstruction selected 54 distinct hadith segments. None was assigned to 1:4 or 1:6. Three locally present reports, marked sahih in the database and pertinent to the existing 1:1 discussion, were absent from the selection:

- `BUKHARI:5376`: naming Allah when beginning to eat. The report is independently visible in [Sahih al-Bukhari 5376](https://sunnah.com/bukhari:5376).
- `ABUDAWUD:1694`: the relation between the divine name and the bond of kinship. The Arabic passage and al-Albani's sahih grading are independently visible in [Sunan Abi Dawud 1694](https://sunnah.com/abudawud:1694).
- `BUKHARI:5988`: another locally stored report connecting raḥim and Raḥmān.

All three were actually used in the earlier accepted 1:1 annotations. Thus the new retrieval path can omit connections that the earlier research already located. Other passes might rediscover them, but that possibility is not a coverage mechanism. A page absent from the hadith unit's allowed pages cannot receive a hadith line from that unit at all.

There is also a demonstrated orthographic mismatch. Searching the local Muslim collection with the same exact-phrase mechanism gives:

| Query | Hits |
| --- | ---: |
| `اهدنا الصرط المستقيم` | 0 |
| `اهدنا الصراط المستقيم` | 1 |
| `لله رب العلمين` | 0 |
| `لله رب العالمين` | 5 |
| `ملك يوم الدين` | 0 |
| `مالك يوم الدين` | 1 |

Removing vocalization does not fully reconcile Qur'anic orthography with the ordinary spelling used in reports. Variant readings must also be distinguished rather than indiscriminately conflated.

**Required change:** use claim concepts, cited ayahs, spelling variants, known related reports, and agent recollection to guide retrieval. Preserve search caps as unresolved retrieval work when relevant material remains unexamined. A zero lexical match must not imply no relevant tradition.

## 3. Multi-ayah passages can disappear from the relevant ayah's input

**Critical.** `ayah_items()` (`grup.py:170`) assigns a segment spanning up to three ayahs to its first ayah. Wider segments normally go to `surah`, with limited extra routing based on explicit citations. The source's full ayah range is not propagated to every covered ayah.

Reconstructed examples:

| Segment | Assigned pages |
| --- | --- |
| `MUQATIL:1:1-4` | `surah` |
| `MUQATIL:1:5-7` | `1:5` |
| `TABATABAI:1:1-5#5` | `surah` |

The last segment is a source for the existing 1:1 paragraph 13 annotation about naming and belonging. The grouped pipeline's `page_lines()` selects only lines with the matching page. No automatic redistribution brings a surah-only line back into 1:1. The global pointer ledger can consider a source preserved somewhere even though it is missing from the ayah where the reader needs it.

**Required change:** allow positions to address every relevant page and claim. Store a shared source passage once, but associate its positions with all affected ayahs. Coverage must be tested at the claim/page level.

## 4. Novelty can be inferred from inadequate or incomplete searches

**Critical.** The antecedent pass receives only the placement agent's short descriptions in `bos.jsonl` (`oncul_input()`, `grup.py:926`). It does not receive the original paragraph text, its augmentations, the evidence already assigned to it, or stable claim IDs. It is told to search at most 15 corpus calls for the whole unit, currently the entire surah's remaining claims.

This is particularly weak for a paragraph containing several claims where one is traditional, another a new combination, and another unresolved. A source that “touches” one feature can prevent an important remainder from reaching this pass.

The schema has useful distinctions such as partial precedent and bounded search. However, `tarama:tam` and `taranan` are declarations, not validated evidence of search completeness. The checker neither proves that the listed sources were searched adequately nor ties search results to each claim. A second `yenilik` record after the same paragraph is dropped (`validate.py:106`), although two distinct claims can need different novelty assessments. Combining them in one reader note would be reasonable only with separate claim-level accounting underneath it.

**Required change:** assess prior attestation separately for each claim, including the exact relationship or synthesis it proposes. Distinguish direct antecedent, partial antecedent, familiar components with an unlocated combination, no match within a stated search, and unresolved coverage. Treat a claim of complete novelty as a conclusion requiring broader justification; no finite negative search here establishes that nobody has said it.

## 5. Agent memory is permitted but is not systematically used for discovery

**High.** The prompt allows explicitly unverified memory pointers and correctly restricts memory-based hadith and grading assertions. But there is no required memory/discovery assessment for each claim. Sources available only as memory pointers are excluded from `held_sources()` and generally just listed as unavailable. The accepted 1:1 page has no memory records; absence of such records alone is not a defect, but the workflow provides no evidence that the memory route was considered.

Source-first extraction also asks for every position in the selected material, which can spend attention on unrelated debates while never prompting the agent about a distinctive inference in the frozen paragraph. The meal pass reads verse words and translations without the prose; this can produce useful translation criticism while missing how translations bear on a particular prose claim or its cross-references.

**Required change:** give each specialized pass the relevant paragraph context and the same claims. Use memory to propose further sources and counterexamples, verify those where possible, and retain clearly marked unresolved leads when useful to the reader. Do not make unchecked recollection into a validated source or confuse its absence with novelty.

## 6. Mechanical success does not mean a complete or faithfully delivered enrichment

**Critical.** The executable probes reproduce these failures:

| Probe | Current result |
| --- | --- |
| Validate an empty annotation list | `passed: true` |
| Finish an empty single-page trial | `ok: true`, 0 kept |
| Check a rendered page after deleting every annotation block | No errors, despite 53 expected records |
| Check placement with input and gap files absent | No errors |
| Finish extraction after dropping its only line, with its segment labelled irrelevant | `status: ok`, 1 dropped |
| Submit two novelty records at one paragraph | Second record dropped |
| Submit a synthetic sahih hadith assertion citing only a tafsir segment | Record passes |

`check_page()` checks blocks that are present but never compares the complete expected and actual ID sets. `enrich.finish()` can accept the remaining records after dropping invalid ones; missing claim coverage does not prevent acceptance. `grup.merge()` renders incomplete results with warnings into `work/`, not `out/`; this distinction matters, but there is still no complete-readiness result that a batch caller can rely on.

Source resolution and quote matching are useful checks, but cannot establish that a Turkish paraphrase faithfully represents the cited author's position. The synthetic hadith test also shows that a claimed grade can pass without a resolved hadith record: the grade checks run conditionally when such a source is present.

**Required change:** missing artifacts, unexplained claim gaps, relevant unread material, lost positions and dropped records must keep a page incomplete until repaired or explicitly resolved. Compare every expected annotation with the rendered output exactly once. Add semantic source/attribution review; do not present schema validation as that review.

## 7. Some optimizations discard precisely the differences the reader needs

**High.** `ayah_items()` suppresses a full-edition segment when at least 80% of its normalized character five-grams occur in the shorter edition's accumulated text. This does not establish that all its positions are duplicates. A controlled test appending a distinct contrary position to a repeated passage causes the entire longer segment, including the new position, to be discarded.

Extraction coverage marks a segment used if any surviving line carries its locator. It does not show that every relevant position in a long segment was captured. Likewise, the final pointer ledger can pass while a distinct argument or qualification from the same source has vanished. Clustering unions pointers and holders onto an unchanged representative sentence; equivalence of reasoning and scope is instructed but not independently checked.

Budgeting also has exceptions: the planned S87 meal unit contains **247,609 material characters** against a nominal **110,000-character** budget. The Fatiha bayani unit has 164,915. Entire-surah units bypass the normal splitting mechanism. These are sizing observations, not proof of context overflow, but they contradict treating the budget as a reliable upper bound.

**Required change:** deduplicate exact passages or preserve unmatched content explicitly; merge positions only after checking their substantive equivalence. Split material independently of the need for a later common verdict. Spend tokens on claim coverage and differing positions before translation rankings or peripheral source summaries.

## 8. Baseline selection does not implement “augment9 if available”

**High.** Of the local ayah output directories examined, 26 contain augment9 readings and 18 have r13 readings without augment9. One additional directory has neither target version. These are counts of currently available local artifacts, not the whole Qur'an.

`pack.ayah_base()` (`pack.py:78`) returns only augment9 and returns no base otherwise. `render.target_page()` also requires an augment9 path. S100's pack therefore has no ayah bases. S107's old pack contains augment3 readings; the renderer correctly refuses those stale ayah inputs, so I did not treat them as valid current outputs.

The S1 and S87 pack copies and upstream augment9 readings matched their recorded hashes during this audit. Frozen-paragraph preservation and stale augment3 rejection are useful existing safeguards.

**Required change:** select r13+augment9 when available and bare r13 otherwise, with explicit provenance and hashes for both cases. When an augmentation later becomes available, treat it as a new baseline that requires coverage review. Do not use augment3 as a fallback.

## Substantive sample: what the missing awareness would contain

These are short examples supported by checked local passages, not a completed replacement enrichment or judgments that the remaining claims are novel.

For **1:1 paragraph 14**, the accepted output supplies no annotation, although the paragraph and augmentation discuss trace-reading, branding and the facial sign in 48:29:

- **15:75:** Taberî, Mücâhid'in “mütevessimîn”i feraset sahipleri, İbn Abbas'ın dikkatle bakanlar, Katâde'nin ise ibret alanlar diye açıkladığını aktarır; izden anlam çıkarma okumasının bu yorumlarda öncülleri vardır. Pointer: `TAB-FULL:v14p94#2`.
- **68:16:** Taberî, damgayı kişinin kusurlarının herkesçe tanınır hâle gelmesi diye yorumlar; kalıcı ayıp ve kılıç yarası açıklamalarını da aktarır. Pointer: `TAB-FULL:v23p170`.
- **Augment9 / 48:29:** İbn Kesîr, yüzlerdeki nişan için güzel hâl, huşû ve tevazu açıklamalarını aktarır; Mücâhid'in bunu yalnız alındaki fiziksel iz saymaya karşı çıkışını da kaydeder. Pointer: `IBNKATHIR-FULL:v7p361`; independently checked against [Ibn Kathir on 48:29](https://quran.ksu.edu.sa/tafseer/katheer/sura48-aya29.html).

The frozen augmentation does not explicitly insist on a physical forehead mark. The last pointer supplies an interpretive distinction the reader should know; it is not presented as a refutation of a claim the paragraph never made.

For **1:1 paragraph 23**, a whole paragraph missed by all five inspected versions:

> Taberî, 21:112'de Rahmân'ı kullarına merhamet edip nimetini yayan, inkârcıların sözleri karşısında yardımına başvurulan Rab diye açıklar. (`TAB-FULL:v16p444`.)

That is an antecedent for part of the mercy/help connection. It does not by itself establish a prior author making the paragraph's exact connection to Fatiha 1:5 or its specific fullness analysis. `claim-sample.json` separates nine claims/comparisons in this paragraph and its augment9 references so that the supported part cannot conceal the unresolved parts.

This is the distinction the workflow needs to preserve: **the relevant earlier thought, its precise relationship to the prose, and the limits of what has actually been established.**

## Recommended workflow before a production ayah run

1. **Freeze and identify the claims.** Produce the correct baseline manifest, stable paragraph/addition IDs, and a checked inventory of all substantive claims. Keep shared claims linked when repeated.
2. **Run the specialized passes against that inventory and its prose context.** Reuse cached source extraction, but require each relevant tradition, hadith, meal and memory search to address the claims. Read cross-referenced passages when the prose's argument depends on them. Record why a pass is inapplicable or incomplete.
3. **Keep an internal coverage table.** For each claim/pass, record the actual finding: antecedent, partial antecedent, different interpretation, objection, relevant background, bounded negative result, unresolved source access, or justified inapplicability. Attach evidence and source-search scope. Distinguish source support for a premise from precedent for the final synthesis.
4. **Review omissions and novelty independently of composition.** Re-read the full frozen prose and additions against the coverage table. Search for contrary positions and missed sources. A claim does not leave this review merely because an annotation shares its topic.
5. **Compose concise reader pointers from established findings.** Combine genuinely equivalent positions without losing differing reasons or attribution. Show useful unresolved leads. Put the claim-to-note accounting in the internal artifact; the reader gets short summaries and usable source locations, not the whole audit table.
6. **Require complete delivery before acceptance.** All mandatory artifacts present; every claim accounted for; every relevant extracted position retained or explained; every rendered record present exactly once; the frozen text preserved; all unresolved coverage reflected honestly. Bounded, unresolved research must not appear as a finding of complete novelty.
7. **Then run a pilot and reassess the actual output.** Fatiha 1:1 is a strong first test because it has multiple meanings per paragraph, cross-ayah arguments and augment9 additions, known precedents, different schools, and already demonstrated omissions. Add an S87 ayah to exercise multi-ayah source routing, then expand the batch only after the outputs meet the claim-level standard.

The source catalog, immutable prose, paragraph anchors, group separation, source locators and script rendering can be retained. The necessary change is to make **claims and their evidence the unit of completeness**, so retrieval and compression cannot quietly turn a partial awareness summary into apparent exhaustive coverage.
