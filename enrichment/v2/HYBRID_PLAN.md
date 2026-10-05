# Enrichment rebuild: the hybrid plan (2026-10-05) — read this first after a context reset

This file is the single source of truth for the enrichment rebuild agreed with the user on 2026-10-04/05. It records
what the user decided, what is done (with commits), what is measured, what is open, in order, with acceptance
criteria, and the traps already found. Keep it current: update the status lines as work lands, commit and push.

## 0. The user's decisions and rules (binding)

1. **No silent losses, no shortcuts, no text cuts** ("make sure there are no short cuts or text cuts"). Every
   source tied to a page is read IN FULL by some agent; every segment is accounted for (used, nothing new,
   repeats X, not about this ayah) and the script verifies the accounting; every cap (tool limits, our own limits)
   is either avoided by construction or continued, and audited after the run. Nothing is skipped for budget.
2. **Budget is real** ("make sure not to act as if there's no budget limit"): small groups per agent, files under
   the tool limits, few turns, no repeated reading. Targets: under $10 per ayah on average for the Fātiḥa now;
   **under $5 per ayah on average for the production-grade workflow**. Measure at published rates with the
   thinking estimate (agentrun cost_usd_est), never the floor alone.
3. **Hybrid design**: many passes, one per tradition/function group, each small enough for one agent; per-surah
   units for groups whose surah material fits one agent (naẓm/Biqāʿī, bayānī/al-Khūlī, meal), per-ayah units
   otherwise, split by source when even one ayah is too big. Each enrichment block is an independent unit:
   order does not matter as long as it is anchored (paragraf + capa) to the correct frozen v16 prose (ayah base =
   augment9 reading, augment additions included).
4. **Major voices**: Biqāʿī (Naẓm al-durar: maqṣūd, munāsaba, naẓm) and the al-Khūlī (bayānī) school are the
   sources the user most wants to hear. Required on every page: cited, or a recorded reason. Fetch ALL the
   school's texts. **Licences are not a barrier** (local analysis).
5. Models: **Opus 5.5 writes pages; effort high is the default**; medium may be tested in parallel. **Never Haiku.**
   Sonnet only where a step is extraction (if ever used again, measure first: the Sonnet-reader pilot failed).
6. Process: every spawned agent needs the user's go (a go covers the runs named, not more); instruction files
   (briefs) are shown to the user before use; commit and push after every completed step (only our own files: a
   parallel session edits the Bible-pass files — never commit its work); report every WARNING; record actual cost
   against the estimate; tell the user the expected cost before a run.
7. The user is checking/downloading missing sources in parallel (2026-10-05). Ask before duplicating that work.

## 1. Where things stand (2026-10-05)

### Done (commits on main, pushed)
- `agentrun.RATES` corrected to published rates (Opus $4 in / $5 5m write / $8 1h write / $0.20 read / $20 out;
  Sonnet $2/$2.5/$4/$0.20/$10) — reproduces the CLI's cost_usd to the cent on 3 trials (cf9421683).
- Output estimate from context growth (`cost_usd_est`, `output_tokens_est`; transcripts record only stream-start
  output, thinking invisible): the old 1:1 page is ~$13.96, not $10.40 (8a66c6684).
- Corpus lookups by index (`seg=? OR seg LIKE ?` scanned the whole table: validator 32 s → 0.2 s; a 7-minute
  validator run had expired the 5-minute cache, $2.32) (a38d50c81).
- `corpus.py` output caps: ≤ 9,000 characters of segment text per call and the whole output < 24,000 BYTES
  (Claude Code spills a Bash output over ~30,000 BYTES to a file; Arabic is 2 bytes/char), cuts marked
  `[cut: corpus.py get LOC --from N]`, search/ayah snippets marked `[preview …]`, unshown segments listed per
  source (dfe…; latest c-hash in git log "corpus.py: output kept under 24,000 bytes").
- `tools/check.py` (agent's own check: drops with reasons, Arabic stretches not in cited segments, placement map).
- `enrich.py` modes `tur` and `dosya2` (trials), finish joins `annotations.N.jsonl`, records unread tied sources,
  required reads with line ranges (Read cap 25,000 tokens; the 1:2/1:7 bases exceed it), wrapped base copy
  (Read cuts lines > 2,000 chars; 1:7 line 122), transcript **audit** (required files' line coverage, spills and
  whether read, corpus cuts not continued, output-limit stops) (923340633, 8a66c6684, de52be689).
- Agent definitions `.claude/agents/enrich-page-high.md` / `-medium.md` (model opus, effort fixed, tools Read/
  Write/Edit/Bash, omitClaudeMd). The Agent tool cannot set effort; these load only at session start.
  Harness floor with them: 5.3k tokens (general-purpose: ~28k).
- `tools/compare_pages.py` (trial vs reference: cost, turns, kept, shared/new segments, meal blocks, audit).
- COST_PLAN.md (measurements, Opus review, trials), this file.
- Never-spawned dirs marked dead.json (okuma c08–c17); `zengin-dosya.1_3.opus.high` (other session, died 9.5 h
  earlier, no output, ~$3 est) confirmed dead.

### Done, with open ends (A1)
- **Biqāʿī data fix** (`fetch/biqai_intros.py`, applied to enrichment/corpus/BIQAI-FULL/segments.jsonl; original
  kept as segments.orig.jsonl; log intros.json): 75 surah introductions (maqṣūd, names, munāsaba) COPIED to the
  surah they introduce (`<seg>#sNNN`, whole-surah range), 29 lagging pages COPIED (S82 al-Infiṭār and S84
  al-Inshiqāq had NO segment at all; now 6 and 9). Copies only: no existing tie removed (moving pages by quoted
  ayat was wrong 388/414 times: commentary cross-quotes neighbours). 32 surahs' introductions not detected (may be
  in place as a heading segment of their own; check). **Index rebuilt 2026-10-05 (972,532 segments) and verified**:
  `corpus.py ayah 107:1 --src BIQAI-FULL` lists `BIQAI-FULL:v8p541#s107` (S107's maqṣūd); `ayah 82:1` lists
  v8p345#s082 and the S82 pages. The script is committed (the corpus data is gitignored; the script reproduces it
  from segments.orig.jsonl). STILL OPEN: the same fix in the importer (openiti_works/openiti_parse) so a re-import
  keeps it; the 32 undetected introductions (A1).

### Measured (1:1, the heaviest ayah; reference = old page zengin.1_1.opus.high, 53 records, ~$14)
| trial | kept | recorded $ | est $ | turns | ref records sharing a segment | new segments | Biqāʿī cited |
|---|---|---|---|---|---|---|---|
| dosya2 high | 58 | 3.63 | 5.14 | 14 | 41/53 | 44 | 0 |
| dosya2 medium | 45 | 2.67 | 3.88 | 11 | 43/53 | 38 | 0 |
| tur high | 53 | 3.77 | 5.45 | 16 | 31/53 (24 tied sources unopened) | 42 | 0 |
| tur medium | 55 | 3.19 | 4.71 | 16 | 35/53 | 41 | 0 |
Cost split of dosya2 medium: output incl. thinking 53%, cache writes 36%, reads 11%. One agent with a budget drops
sources silently → the hybrid. The staged Sonnet-reader pilot (okuma.py) was dropped: cards barely compressed
(1.6:1), 1.94× its estimate, and its "53/53 recall" was locator-level only (the source audit is right on this).

### Corpus facts that matter (audit REVIEW_source_efficiency_2026-10-05.md, checked)
- Tied text per Fātiḥa ayah: 1:1 1.09M chars; 1:2 561k; 1:3 227k; 1:4 354k; 1:5 397k; 1:6 308k; 1:7 672k. S1 unique
  (no meals) 3.02M; summed over the 7 pages 3.57M (only 213k in multi-ayah segments). Production surahs S87 ≈ 91k
  per ayah, S100 83k, S107 102k (whole Qur'an mean 124k).
- Short vs -FULL editions mostly differ (8% of S1 FULL text ≥80% duplicated): read both.
- **Abū Ḥayyān FULL is tied to whole ranges** (19.97× exposure; S33: 67 chunks on 33:1–73). Elmalılı and Biqāʿī
  have shared passage groups (105:1–5 Elmalılı 86k chars on each of five ayat).
- **Segments with no ayah tie** are invisible to ayah lookups: Jishumī 3,401 segs/4.34M, Ibn ʿĀshūr FULL
  2,178/3.07M, Durr FULL 1,308/2.07M, Bursevī 2,534/3.63M.
- Lexica: 1.5M chars of layout markup (PageV…, ms…, ~~); al-ʿAyn 1.2M of 2.44M duplicated across root routes;
  LISAN:ريا 125k chars in one entry.
- Elmalılı: 137 segments `arabic_reliable:false`, not shown to the reader.
- Memory pointers with NO text: KHULI, BINTSHATI, ABDUH-AMMA, MUQATIL-WUJUH (+ others: 24 in all). JURJANI is named
  in the brief but absent from the corpus.

## 2. The five tasks (agreed order), each with acceptance criteria

### Task A — Data organisation and accessibility
A1. Biqāʿī: finish the fix above (index, verification, commit, importer). Check the 32 undetected introductions.
    Accept: every surah 1–114 has a Biqāʿī segment; every detected introduction is tied to its own surah; no
    original tie lost (segments.orig.jsonl ⊆ new file by locator).
A2. Abū Ḥayyān FULL range narrowing: map each chunk to the ayat it actually discusses (quoted ayat in the chunk,
    headings), keep the old range as a searchable "parent" link (never lose the wide tie: add precise ties, keep
    the parent). Then Elmalılı and Biqāʿī shared passages the same way. Accept: per-ayah exposure drops (audit
    script re-run), sampled chunks verified by hand, old locators still resolve.
A3. Segments with no ayah tie (Jishumī, Ibn ʿĀshūr FULL, Durr FULL, Bursevī …): tie by headings/quoted ayat where
    evidence exists; the rest become surah-level or book-level material that a group reads by surah (not lost).
    Accept: no source's text is unreachable by the group workflow; the count of untied characters per source is
    reported, each with its disposition.
A4. `corpus.py` retrieval fixes (audit table "Retrieval defects"): exact-segment `get` by default (siblings only
    with `--family`), match-centred search previews with offsets, the whole response (notes/translations too)
    inside the byte budget, `--from` not reprinting notes, continuation cursors per field, show quality flags
    (`arabic_reliable`, lexicon `route`), a true phrase search distinct from whole-token. Accept: the audit's
    retrieval_proofs.json reproductions all pass.
A5. Clean lexicon view (strip layout markup into a rendered view, page ids kept as metadata); share exact
    duplicate bodies (al-ʿAyn) with their aliases kept; split oversized entries by headword/sense. Accept: markup
    count ~0 in model-facing text; every alias still resolves.
A6. Pack trimming without loss: usage.md as counts + compact index with batched retrieval; meals.md panel first,
    wider set on demand; dictionary bodies shared. Accept: nothing previously reachable becomes unreachable.

### Task B — Source acquisition (user is also downloading in parallel: coordinate)
B1. al-Khūlī school, ALL: Bint al-Shāṭiʾ al-Tafsīr al-bayānī (2 vols; covers 93, 94, 99, 100, 102, 103, 104, 107,
    89, 90, 92, 96, 68, 73; archive.org items elshandawily0546 / elshandawily0547 / 052Pdf noted in
    corpus/BINTSHATI/source.json), her al-Iʿjāz al-bayānī; Amīn al-Khūlī Manāhij tajdīd; and the rest of the
    school the user counts (ask: Khalafallah al-Fann al-qaṣaṣī? Shukrī ʿAyyād? Abū Zayd?). Licence no barrier.
B2. OCR: scans → text. Test local Tesseract (ara) on a few pages first and show the user the quality; Opus vision
    for the two volumes costs roughly $15 (mostly output tokens) — the user decides. Keep page images, OCR text,
    page ids and provenance; mark low-confidence pages (no silent errors).
B3. Import as corpus sources with ayah ties (her chapters are per surah; tie by quoted ayat), access `yerel`.
B4. Other pointers: ʿAbduh Juzʾ ʿAmma, Muqātil al-Wujūh, al-Jurjānī (Dalāʾil, Asrār), the other 24 hafiza
    pointers: list them for the user with what is known about availability.

### Task C — Workflow rebuild: the hybrid (grup.py)
C1. `groups.json` (written; 17 groups): rivayet, dirayet-kesşaf, dirayet-cami, modern-arap, mezhep, nazm-bikai
    (required, per surah), beyani-huli (required, per surah), isari, meani-nahiv, kiraat, lugat (by root),
    vucuh (search), turkce, ulum-nuzul, hadis (search), meal (per surah), oncul (antecedent search). Check: every
    source the briefs name and every corpus source with tied text belongs to exactly one group; print the rest.
C2. `grup.py plan --surah S`: per group, the material of each unit (segments whole; range/untied segments to the
    surah unit; a group whose surah total ≤ budget_chars runs once per surah), splitting by source when a unit
    exceeds the budget (110k chars ≈ 75k tokens). Prints a table: group, unit, segments, characters, estimated
    cost (model below) and writes work/sNNN/grup/plan.json. Every segment of every source appears in exactly one
    unit (assert; print any orphan).
C3. Unit inputs: per-ayah units read the full ayah base (wrapped copy, line ranges); per-surah units read a
    script-built paragraph digest of every page (each ¶n: first ~40 words … last ~15 words, augment blocks marked)
    so capa can be quoted exactly — the full bases of a surah are too big (S1 ≈ 165k tokens). Material files
    ≤ 24,000 chars each (one Read), listed with line ranges if needed. No cut anywhere: a segment longer than a
    file continues in the next file, marked.
C4. Output per unit: `records.<page>.jsonl` (page = `S_A` or `surah`; schema records, ids per file) and
    `kapsam.jsonl`: one line per material segment {seg, durum: kullanildi|yeni_yok|tekrar|ilgisiz|okunamadi,
    neden, kayit_ids}. Required-voice groups: a page with nothing from the voice gets a kapsam line saying why.
C5. Finish per unit: AR.finish (cost + estimate), the transcript audit (caps), kapsam completeness (every segment
    listed; missing → WARNING + recorded; the unit is "incomplete" and is re-run only with the user's go),
    VAL.check_records per page file (drops listed in check.json), ledger row (stage grup, group, unit).
C6. Merge per page: union of kept records from all groups, ids renumbered per page (S<sss>-<KOD>-<NNN>), validate
    again, render into the frozen base (trial dir first: work/sNNN/grup/pages/), the >5 blocks per paragraph rule
    stays a warning (the user: order and count per paragraph do not matter). Accept to out/ only with the user's go.
C7. Group briefs: one shared `prompts/grup.md` (purpose; read every material file completely; account for every
    segment in kapsam.jsonl; anchoring; schema; common.md's source rules, its "one file per call" reading rule
    overridden by parallel Reads; write records directly in parts ≤ 25 records; run tools/check.py once) + each
    group's `odak` from groups.json. Show the briefs to the user before any run.
C8. Search-based groups (hadis, vucuh, oncul): the script runs the deterministic searches first (ayah phrase,
    each content lemma; sahih only for hadis) and gives the hits as material; the agent may run ≤ 10 more
    searches (recorded); antecedent group searches per imge/sentez claim (taranan, tarama recorded).
C9. Cost model for the plan table (calibrated on the trials; recalibrate after the first S1 run): per unit,
    writes $5/M × (5.3k harness + ~12k brief + base/digest + material tokens + output); reads $0.20/M × turns
    (~5) × mean context; output $20/M × (records + ~15k thinking + ~0.08 × material tokens). Material tokens =
    Arabic chars/1.45 + other chars/2.2. Expected S1 total ≈ $25–35 (≈ $4–5 per ayah, the Fātiḥa being the
    heaviest surah); production surahs (≈ 90–100k chars per ayah) should come well under $5. Report estimate vs
    actual per unit.
C10. Run order for the first test: S1 with the user's go, groups in parallel (batches of 7 agents), finish,
    merge, compare with the reference 1:1 page and the four trials, report.

### Task D — Evaluation before production (gate)
D1. Test set: 1:1, 1:7, 105:1/4, 107:7, 112:1–4 (+ 2:196, 3:7, 33:35 when their packs exist).
D2. Questions derived from passages NOT cited by earlier pages: minority views, rare senses, footnotes,
    counter-evidence, Biqāʿī's maqṣūd/munāsaba, al-Khūlī/Bint al-Shāṭiʾ points.
D3. Metrics: claim-level recall, attribution correctness, quote fidelity (tools/check.py QUOTE), missed
    disagreements, cost per ayah (est), turns, kapsam completeness. No critical evidence loss before adoption.

### Task E — Merge and acceptance for multi-pass pages
E1. Versioned acceptance: an accepted page is never overwritten; a later pass (e.g. al-Khūlī after import) adds a
    new version (out/sNNN/<page>.v2.md + record of which groups/units it contains). Decide the rule with the user.
E2. Duplicate points across groups are allowed (independent units) but the merge reports near-duplicates (same
    locator + same paragraph) for the user's review, never drops them silently.

## 3. Traps already found (do not rediscover)
- Claude Code spills a Bash output over ~30,000 BYTES (not characters) to a file + 2 KB preview; an agent may never
  read it. Two corpus.py calls joined with `;` add up: one call per command.
- Read tool: 25,000 tokens per Read (partial view + banner), lines over 2,000 chars cut. List big files with line
  ranges; wrap long lines in a copy.
- The subagent transcript's output_tokens are stream-start counts; thinking is never recorded → use cost_usd_est.
- New `.claude/agents/*.md` load only when a session starts.
- `corpus.py build` refuses while any call dir has started.json without run.log.json/dead.json; mark never-spawned
  dirs with dead.json only after checking no transcript names them (agentrun.transcripts).
- BIQAI-FULL page ties follow the running header: introductions and short surahs sit on the previous surah.
- Never move ties on quoted-ayat votes alone (commentary cross-quotes neighbouring surahs): copy, keep the original.
- The parallel session edits enrich.py, corpus.py, blocks.py, pack.py, render.py, schema.json, tools/intertext.py
  for the Bible pass (uncommitted at the time of writing): do not commit or revert its changes; pull/merge
  carefully when touching the same files.
- Opus at effort medium is cheaper (dosya2 $3.88 vs $5.14 est) but the user keeps high as default.

## 4. Files
- Plans/records: enrichment/v2/HYBRID_PLAN.md (this), COST_PLAN.md, REVIEW_source_efficiency_2026-10-05.md and
  audits/2026-10-05-source-efficiency/, DESIGN.md, RUNBOOK.md.
- Code: enrich.py (modes agent|dosya|tur|dosya2; spawn/finish; audit; unread_sources; required_reads),
  dossier.py (bounded extract), okuma.py (dropped pilot, kept as record), groups.json (C1), grup.py (to write),
  tools/corpus.py, tools/check.py, tools/compare_pages.py, tools/audit_sources.py (the source audit's script),
  fetch/biqai_intros.py, _commentary/v16/agentrun.py (RATES, parse, finish, spawn kinds).
- Trials: work/s001/zengin-{tur,dosya2}.1_1.opus.{high,medium}/ (finished, run.log.json, coverage audit).

## 5. Source inventory after the user's downloads (checked 2026-10-05, before a context compaction)
All in enrichment/corpus/<ID>/raw/acquired-2026-10-05/; every source.json still `access: hafiza`, no acquisition
manifest, nothing ingested or indexed yet.
- Usable text now (import next): ACADEMIC/NOLDEKE-GDQ (3 vols, OCR good, de), ACADEMIC/JEFFERY-FOREIGN (OCR good),
  ACADEMIC/EQ (6 vols, OCR good), ACADEMIC/STUDYQURAN (OCR good), ASAD-NOTES (1,326 pp, PDF text layer good),
  MEAL-HAMIDULLAH (531 pp, text layer good), MEAL-ATAY 2013 and MEAL-AKDEMIR (OCR good, hyphenation `¬` to
  repair), ACADEMIC/SINAI-KEYTERMS and ACADEMIC/CUYPERS-COMPOSITION (text layer good), ACADEMIC/ZAMMIT-COMPARATIVE
  (text layer, tabular: needs table-aware parsing).
- Arabic scans needing OCR (~1,330 pp): BINTSHATI 2 vols 222 pp (bundled OCR readable but noisy, e.g. «بلا شاك»
  for «بلا شك»: not quotable as is), KHULI Manāhij tajdīd 1961 368 pp (bundled OCR noisier), ABDUH-AMMA 189 pp (no
  text layer), MUQATIL-WUJUH (ed. Ḍāmin) 308 pp (garbled layer), IBNKHALAWAYH-MUKHTASAR 246 pp (no layer),
  ACADEMIC/FARAHI-NIZAM (bundled OCR unusable), ACADEMIC/BADAWI-HALEEM 1,095 pp (text layer is glyph codes).
- No OCR engine installed (no tesseract/pdftotext; pypdf only). Options put to the user: Tesseract (free, likely
  no better than the bundled OCR), Claude reading page images (~$0.035/page with Opus: ~$45 all, ~$20 for Bint
  al-Shāṭiʾ + al-Khūlī), or both with disagreement flags. Proposed: Claude for Bint al-Shāṭiʾ and al-Khūlī first,
  checked against the bundled OCR. AWAITING the user's decision.
- Incomplete/open: TARAMA download unfinished (partial ranges and .part files, last write 09:48: ask the user);
  ACADEMIC/ISLAHI-TADABBUR (19 PDFs, 1.3 GB, Urdu: in scope? ask); MEAL-MOZTURK no files; still missing al-Jurjānī
  (Dalāʾil, Asrār) and the rest of the al-Khūlī school (Khalafallah, Shukrī ʿAyyād, Abū Zayd: ask whom).
- Next after the decisions: import the usable sources (source.json with provenance and OCR quality notes,
  segments.jsonl with ayah ties where the text allows, access yerel), rebuild the index, add them to groups.json.

### §5 update (2026-10-05, later): ingested and indexed (index 1,012,263 segments)
The user's download batch completed (20 sources; Iṣlāḥī in scope, all 9 Urdu + 10 English files; TARAMA 8 vols
complete). The user does the OCR (enrichment/v2/OCR_NEEDED.md: ~7,510 pages, Bint al-Shāṭiʾ + al-Khūlī first; one
text file per PDF page in raw/ocr/<pdf stem>/pNNNN.txt). Imported from text layers / archive OCR (scripts in
enrichment/v2/fetch/, every repair, drop and miss counted in source.json `ingestion`; access now yerel):
- ASAD-NOTES 8,374 (import_asad_notes.py: intros, verse groups, 5,303 notes, 5,143 tied by marker)
- STUDYQURAN 5,967 (import_studyquran.py: intros, 4,665 commentary entries, translations flagged duplicate)
- EQ 3,954 pages EQ:v<vol>p<page> (import_eq.py; refs from text + the Index of Qurʾān citations, 26,892 links)
- NOLDEKE-GDQ 884, JEFFERY-FOREIGN 325, SINAI-KEYTERMS 1,015, CUYPERS-COMPOSITION 216, ZAMMIT-COMPARATIVE 671,
  ISLAHI-TADABBUR 3,688 (English, surahs 6–8, 10–114, tied to section verses) (import_pages.py)
- MEAL-HAMIDULLAH 6,392 (6,233/6,236 ayat), MEAL-AKDEMIR 3,461 (6,207/6,236; OCR letter-spacing caveat),
  MEAL-ATAY 4,784 (6,236 aligned by DP against DIB1961/TDV/KURANYOLU; 96 weak flagged)
corpus.py: grouped dirs (ACADEMIC/<ID>) are indexed; new `ref` table of cited ayat: `corpus.py cites S:A`, and
`ayah` reports "CITED ELSEWHERE: n segments". kuranmeali.com (57 translators, checked live) has none of Hamidullah,
Atay 2013, Akdemir, M. Öztürk: the PDFs are their only text.
Open: the ingested sources' source.json files also carry the download session's staged acquisition records:
committing them needs the user's word (they are not committed yet). Next: groups.json membership of the new
sources (C1), then OCR imports when the user's OCR arrives; Task A items remain.
- BINTSHATI ingested (user: "start with bint"; fetch/import_bintshati.py): the Shamela export (373 records = printed
  pages, 7th ed.) as text, text_status "typed, not yet checked against the scan: quote only after checking
  pdf_page"; PDF page = printed page in both volumes (every record's best 3-gram match against the archive OCR is
  its own page, except two metadata records); the 47 scan pages no record covers imported from the archive
  Tesseract OCR as drafts (do not quote) or marked empty: 420 segments = all 418 scan pages + 2 metadata records.
  Ties: chapter surah, verses quoted on the page (spelling-blind skeleton match), «(البقرة 264)» refs.
  Next for her: check quoted spans against the scan at acceptance (cheap, targeted). Al-Khūlī: digital edition
  (VitalSource/Ktab Inc.) to be checked by the user; else the two-witness test (LLM reading vs Tesseract anchor,
  disputed spans re-read from crops) on the six pilot pages first.
- al-Khūlī school, after the user's decision (2026-10-05, "agreed": Manāhij deferred, cover his method through Bint's
  preface and secondary studies, spend effort on works with ayah reach): RIFAI-KHULI and YKHULI-TAJDID (Hindawi,
  secondary, fetch/hindawi_book.py with headless Chrome: the site blocks plain HTTP/EPUB); BINTSHATI-IJAZ (Bint
  al-Shāṭiʾ, al-Iʿjāz al-bayānī wa-masāʾil Ibn al-Azraq, Shamela HTML export archive.org 0865Htm, 584 pages, 1,531
  ayah refs; fetch/import_shamela_html.py, characters in = out). Searched and NOT usable yet: Khalafallah al-Fann
  al-qaṣaṣī (typed PDF from Muhammadanism.org, text layer scrambles phrase order and uses the آ glyph as a space
  filler; archive OCR noisy), Shukrī ʿAyyād Min waṣf al-Qurʾān yawm al-dīn (scan + OCR only:
  archive.org 20260313_20260313_0237), Bint al-Qurʾān wa-qaḍāyā al-insān and Maqāl fī al-insān (scans + OCR only).
  Candidate to ask the user about: Fāḍil al-Sāmarrāʾī, ʿAlā ṭarīq al-tafsīr al-bayānī (bayānī lineage, includes
  al-Fātiḥa; archive.org 00173_201807, 13 MB zip, format unchecked).
