# Enrichment v7: verse digests first, page writers after

Status 2026-10-07: **plan only; nothing built, nothing spawned.** Each step needs the user's go.
Supersedes `enrichment/v6/PLAN.md` (index for routing only, cross-references capped at 15) and the v5 per-family
pipeline. Measurements below were taken from run records and `corpus.sqlite` on 2026-10-07; the saved reports were
not used as evidence.

## 1. Why v7

### 1.1 What drove the cost (measured)

- **Agent loops, not reading.** v4 1:6 Sol high, $19.80:
  - re-reading cached context on every turn: $12.40 (62%);
  - new input: $4.60 (23%);
  - output: $2.85 (14%).

  The v5 Opus poetry writer spent $3.19, of which $1.53 was output: 76k output tokens for about 3,200 words.
- **The page's cross-references, not the ayah.** Of the segments the v4 runs cited:
  - only 11–12% of the characters are on the page's own ayah;
  - 14–20% if segments that quote the ayah are added.

  Pages cite a median of **171 verses** (S1/S87–114, 44 existing pages; maximum 337).
- **The ayah's own material is small.** All verse-tied sources on one ayah:
  - S100: median 103k characters;
  - S87: median 119k characters;
  - Fatiha: 264k–1.12M characters.
- **Pages share cross-references.** The 44 pages cite 3,073 distinct verses; 1,575 of them only once. Every
  verse is eventually some page's own ayah, so reading it once and reusing that reading is never wasted.
- **Rates.** At the saved rates Opus is 2× Sonnet, and Sol is 20× Luna. The "Sonnet four times cheaper" in the
  v5 report came from how Opus behaved, not from its price.

### 1.2 Decisions (user, 2026-10-07)

1. **Two stages:**
   - **Verse digests**, built once per verse and reused by every page that cites the verse.
   - **Page writers**, run only after the digests they need exist. No placeholders, no incremental fills.
2. **No cross-reference cap.** Every verse a page cites is covered: a block, or a recorded `no_match` with a
   reason. Nothing is dropped silently.
3. **Source types are staged.** Tafsir-type sources and meal first. Poetry, lexicon, wujuh and hadith later, each in
   its own unit (§3.4).
4. **Digest models:** Luna or Sol via Codex. A head-to-head test decides (§5, step 1).
5. **Writers make the connections.** A digest records what a source says. Comparing sources and connecting verses
   is the writer's job.

## 2. Pipeline overview

```
corpus.sqlite
  ├─ stage 1a  meal table (script, $0): distinct renderings per verse, translators listed
  ├─ stage 1b  verse digests (Luna/Sol): tafsir-type segments → claim rows with verbatim anchors
  │            └─ script checks: coverage, verbatim, attribution, verse claims, density
  ├─ stage 1c  (later) root digests: poetry, lexicon, wujuh;  term digests: hadith
  └─ cores     script-built one-line index of every digest row (no model)
page writer (per ayah, after its digests exist)
  request 1: page + own-ayah full text + own digest + cores of every cited verse → picks rows, drafts
  request 2: script serves the full rows picked (and up to N full segments) → blocks per paragraph
  └─ script checks: every (paragraph, cited verse) has a block or a no_match with reason; anchors re-verified
```

## 3. Stage 1: digests

### 3.1 Unit and scope

- **Reading unit: one source at a time, segments in text order, chunked at ≤ 40k characters**
  (`v5/common.CHUNK_CHARS`; the measured Luna peak is 67–84k tokens, cap 120k).
  - A segment covering a passage (2:1–5) is read **once**. Its rows are tagged with the verses they concern.
  - Keeping a chunk to one author keeps that author's argument together.
- **Kinds in stage 1:** tafsir, tafsir_tr, maani, nazm, isari, modern, qiraat, translation, ulum and reference,
  where the segment is tied to a verse.
  - Whole Quran: **266M characters, about 6,650 chunks.** Of that, 16.7M is surah-level (introductions, maqṣūd);
    its rows go to a surah digest and are tagged with any verses they name.
- **Edition rule** (from `v5/packet.py`): X is skipped where X-FULL covers the verse. Each skip is logged per verse.
  Whole Quran: 6.8M characters.
- **Range overlay** (`v5/index/range_overlay.jsonl`) is applied; 81 WAHIDI-ASBAB segments.
- **Translations are allowed and labelled** (`v5/common.TRANSLATION_OK`, Islāḥī).

### 3.2 Row schema (`digest.jsonl`, one row per claim)

| Field | Content |
|---|---|
| `row` | `<loc>/rNN`, stable |
| `loc` | segment locator |
| `verses` | verses the claim is about. From the segment index, or from the text (with `verse_basis`: index / quoted / named / implicit+reason) |
| `mentions` | other verses the claim quotes or names |
| `kind` | position · report · lexical · grammatical · qiraat · rhetorical · legal · narrative · coherence · disagreement · grading · other |
| `speaker` | who holds the view, as named in the text. `speaker_ar` is verbatim; empty means the author |
| `via` | for reports: the transmitter(s) named, short |
| `stance` | the author's stance: holds · reports · prefers · rejects · neutral |
| `against` | speakers or row ids it is contrasted with in the same source |
| `claim` | one English line, ≤ 30 words |
| `anchor` | verbatim span from the segment, ≤ 25 words. When `speaker` is not the author, it includes or directly follows the attribution phrase |
| `terms` | Arabic words or roots discussed |

**Coverage file (`coverage.jsonl`), one row per segment in the chunk:**
- `digested` (n rows);
- `nothing_substantive` (reason: e.g. verse text only, list of cross-references, apparatus);
- `unreadable` (broken source text only; never "not read").

**Rows, not quotes.** In v5, extractors told to quote kept 59–92% of each chunk. The brief asks for claims
with short anchors and gives a target ratio. The ratio of digest size to source size is measured.

### 3.3 Script checks (no model; every failure printed and recorded)

1. **Coverage:** every segment in the chunk has exactly one coverage row.
2. **Verbatim:** every anchor is found in its segment (`v5/common.contains`, normalized).
3. **Attribution:** when `speaker_ar` is set, it occurs inside the anchor or within 200 characters before it.
   Failures are listed for review, not dropped.
4. **Verse claims:** every verse in `verses`/`mentions` is either in the segment's index range or overlay, or
   quoted (Quran-text match, Uthmani and standard spellings), or named in the segment. Otherwise the row is
   flagged `verse_unverified`.
5. **Density:** a segment over 3k characters with 0–1 rows is flagged `thin` for a second pass.
6. **Run health:** returncode, turn completed, requests, peak request tokens (≤ 120k), cost. Truncated or
   refused output is recorded per agent (`run_codex.py` already does this).
7. **Spot check:** a sample of chunks per batch is digested again by the other model. Differences are listed
   (row matched / missing / conflicting).

### 3.4 Later stages (not in the first run)

| Stage | Sources | Unit | Attached to verses by |
|---|---|---|---|
| 1c-root | poetry, lexicon, wujuh, grammar | Arabic root or word | the ayah's words (roots) and the page's terms |
| 1c-term | hadith | matn or key term | term and quotation search; Quran-text match in matn |
| 1c-academic | EQ, Sinai, Jeffery, Nöldeke, etc. | entry or page | term and verse search |

When a later stage lands after pages are written, it adds blocks only. The frozen bytes and earlier blocks are not
touched.

### 3.5 Meal table (stage 1a, script)

- Per verse: distinct renderings after normalization (case, punctuation, diacritics), each with its translators.
- The Arberry, Asad and the other translations are labelled by language.
- No model. All verses at once.

### 3.6 Cores (script)

- One line per row: `row | speaker | stance | kind | claim`, grouped by source.
- Expected size is about 1–2k tokens per verse. To be measured.

## 4. Stage 2: page writers (after the digests a page needs exist)

- **Inputs:**
  - the frozen page (v16 r13 plus augment9);
  - the own ayah's full verse-tied text (S87–114 ≈ 35k tokens);
  - the own digest;
  - the meal table;
  - **the cores of every verse the page cites**, at a median of 171 verses, about 170–340k tokens split
    across 2–3 requests that share the cached page;
  - script flags: rows in cross-referenced digests that mention the target ayah, or another verse the page cites.
- **Request 2:** a script serves the full rows picked, plus up to N full segments where a row is not enough.
  There is no search loop.
- **Output:**
  - blocks attached to paragraphs, citing row ids;
  - the script resolves locators and anchors from the rows, then re-verifies them against the segments;
  - the ledger has one row per (paragraph, cited verse): `written` / `no_match` + reason.
- **Model, prose volume per block, and families per writer:** open (§7).

## 5. Steps

1. **Luna vs Sol digest test** (next; needs a go). §6.
2. **Closed-set pilot on 100:1:** the chosen model digests 100:1 and all 32 verses it cites (≈ 3.8M characters,
   ≈ 95 chunks), plus the meal table. Then one page writer. The output is compared with the v4 and v5 outputs on the
   same paragraphs.
3. **Scope digests for S1 and S87–114:** the 295 own ayat, then the verses their pages cite, in order of citation
   count.
   - The 44 existing pages cite 3,073 verses; the full scope will likely cite most of the Quran.
   - Runs go seven at a time; commit and push after each batch.
4. **Page writers for S1 and S87–114.**
5. **Stage 1c** (root, term, academic) when the user schedules it.

## 6. Step 1 in detail: Luna vs Sol

**Question:** does Luna max produce digests as complete and as correctly attributed as Sol, at 1/20 of the
API-equivalent cost?

**Chunks:** about 16, identical for both models, drawn from the 100:1 and 87:6 scopes, where v4 has references
(87:6: 19 families; 100:1: rivayet, historical, meal, poetry). Stratified so that each kind of source is tested:

| Kind of source | Candidate sources |
|---|---|
| transmitted reports | TAB-FULL, DURR-FULL, IBNABIHATIM |
| analytical / grammar | RAZI-FULL, ABUHAYYAN-FULL, KASHSHAF-FULL |
| Imami / Muʿtazilī | TABATABAI, TABRISI, JISHUMI |
| Sufi | BURSEVI, QUSHAYRI |
| maʿānī | SAMIN-DURR, ZAJJAJ, FARRA |
| naẓm / coherence | BIQAI-FULL, ISLAHI-TADABBUR (English) |
| bayānī / modern | BINTSHATI, ASAD-NOTES |
| Turkish | ELMALILI |
| qirāʾāt | FARISI-HUJJA |

**Settings:**
- Luna `gpt-6-luna` at max effort, Sol `gpt-6-sol` at high effort (v4 found high and max differ mostly by run
  variance).
- Same brief, same chunk files, fresh context per chunk, `run_codex.py`, at most 7 in parallel.

**Measures:**

| Measure | How |
|---|---|
| Finding recall | for each v4 reference block drawn from a segment in the chunk: does the digest hold a row carrying that point? Judged per block, recorded with the row id or "missing" |
| Attribution accuracy | hand check of 40 rows per model (speaker, stance, claim faithful to the anchor), plus script check 3 failures |
| Agreement | rows matched between the models per segment; every conflict adjudicated against the text |
| Anchor and coverage failures | script checks 1–2 |
| Compression | digest characters ÷ source characters |
| Cost and context | API-equivalent per chunk, requests, peak request tokens |

**Decision rule** (proposed; the user confirms before the test):
- Luna is adopted if its finding recall is within 5 points of Sol's, and its attribution error rate is no more
  than 1.5× Sol's and under 5% in absolute terms.
- Otherwise, Sol is used for the kinds where Luna failed.

**Estimated cost** (API-equivalent; actual $0 via Codex):
- Luna: 16 × ~$0.04–0.05 ≈ **$1**.
- Sol: 16 × ~$0.8–1.0 ≈ **$13–16**.

Parent preparation and review are reported separately.

## 7. Open decisions

- The decision rule in §6 (confirm or change).
- The writer model (Opus for the own ayah, Sonnet for cross-references, or one model).
- Prose volume per cross-reference block, and per page.
- Whether writers wait for stage 1c, or 1c adds blocks later.
- N, the number of full segments a writer may request.

## 8. Estimated cost (to be replaced by measurements)

| Item | Luna digests | Sol digests |
|---|---|---|
| Stage 1b, whole Quran (≈ 6,650 chunks) | ≈ $270–330 | ≈ $5,500–6,500 |
| Per ayah, spread over 6,236 | ≈ $0.05 | ≈ $0.9–1.0 |

**Page writer, per page:**
- Sonnet: ≈ $1.5–2.5.
- Opus: ≈ $3–5.

Output dominates, so the prose-volume decision moves this figure most.

## 9. Reused from v5 (no copies; imported or called)

- `common.py`: rates, chunk size, `contains`, translation rule.
- `ranges.py` and the range overlay.
- `read.py`: 10k-character deliveries and `selfcheck`.
- `run_codex.py`: the Codex runner, with per-request context and cost accounting.
- `account.py`.
- `evaluate.py reference`: the v4 reference set.

**New in v7:**
- `digest/prepare.py`: chunks, spawn files and the run manifest;
- `digest/check.py`: §3.3 checks 1–6;
- `digest/compare.py`: the Luna vs Sol measures;
- `briefs/digest.md`.
