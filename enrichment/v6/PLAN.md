# Enrichment v6: corpus index first, script routing, grouped writers

Status 2026-10-06: **plan only; nothing built, nothing spawned.** Each step needs the user's go.
Read first: `enrichment/v5/REPORT_2026-10-06.md` (findings, review of v3/v4/v5, measurements).

## Goal and constraint

- Under **$5 per ayah** (API-equivalent at the saved rates), with the 19 source families.
- **The index must never become a silent failure source.** Every loss is recorded and measured (see the no-silent-failures rule).

## Why v6

**Root cause of the cost:** v3–v5 multiply the number of model calls per ayah by the context each call carries.
- 19 or more family calls per ayah each pay an output and thinking floor (about 76k tokens for the Opus poetry writer).
- Agentic search re-reads its own growing context: v4 accumulated 64–104M input tokens on 1:6 to cite about 565k tokens.
- Nothing reduces the material before an expensive model reads it: packets of every cited verse, extraction quoting 59–92% of each chunk, and 81 near-duplicate meal renderings per verse.

**The content itself fits.** The cited source of the heaviest page, read once, plus about 20–35k words of prose come to roughly $2–4 per ayah on Sonnet. Everything above that is call-structure overhead.

**v6 moves the reading out of the per-ayah path.** The corpus is read once into a structured index. Per ayah, scripts route; a few grouped writers read only what was routed, plus the full text of what they cite.

## Design

### 1. Corpus index: one-time, incremental

- **One row per segment,** keyed by `seg` plus a hash of its text; rebuilt only when the text changes. Fields:
  - verses discussed: explicit, and implicit with the reason;
  - Arabic key terms and roots;
  - named authorities, each position held (one line each), disagreements (who against whom), the author's preference;
  - grading statements as stated;
  - for poetry: the word witnessed, poet, collection and gloss;
  - edition or translation flags;
  - every claim carries a short verbatim anchor from the segment.
- **The index routes; it is never evidence.** Writers cite only full text they opened.
- **Model:** decided by step A below. Opus only if it is clearly more reliable than Sonnet on the measured comparison; Luna is the cheap baseline.
- **How it runs:** Claude Code subagents (nominal cost, but against subscription usage limits) or the Batch API (real money, about half price, needs an API key). Open decision for the user.

### 2. Per-ayah routing: scripts only, never a model search loop

- **Verse route (deterministic):** segments indexed to the target ayah and to the cross-referenced verses the page argues from. Cross-references are **capped at about 15 per page**, chosen by script from the paragraphs; without the cap, S1 and S87–114 pages cite 3,131 verses (about 100M tokens).
- **Range overlay:** `v5/index/range_overlay.jsonl`, 81 WAHIDI-ASBAB segments.
- **Index route:** rows matching the page's verses, terms, roots and named authorities. This is essential for sources not tied to verses: hadith, poetry, rhetoric, wujuh, academic, modern-coherence.
- **Keyword fallback, on every page:** full-text search with the page's Arabic terms. Whatever it finds that the index missed is logged as an **index miss**, so the miss rate is measured continuously.
- **Meal:** a script-built table of distinct renderings per verse, with the translators listed. No index needed.
- **Optional memory leads:** one cheap call for all non-indexed families together, verified by script (`v5/leads.py`).

### 3. Writers: about 5 per ayah, not 19

| Group | Families |
|---|---|
| Transmitted | rivayet, hadith, historical |
| Classical exegesis | kessaf, analytical, imami-mutazili, ishari |
| Language | grammar, qiraat, wujuh, rhetoric, poetry |
| Coherence and modern | classical-coherence, modern-coherence, bayani, modern-tafsir, academic, turkish-tafsir |
| Meal | meal |

- **Page:** each writer reads it once (cached prefix).
- **Material:** the routed index rows, within a fixed budget.
- **Source text:** each segment it cites must be opened in full (`get`). This is proven from the agent's command log, and anchors are verified against the full text.
- **Output:** blocks per family, as in v4/v5.
- **Model:** Sonnet 5.5 at medium effort by default; Opus for groups where depth decides quality (meal judgement, coherence), if measured worth it.
- **Prose volume target per ayah:** to be set by the user (output is the irreducible floor).

### 4. Protections against silent failure

1. **Coverage:** every segment in scope has a row, or an explicit "nothing indexable" with a reason. Gaps are reported by script.
2. **Row validity:** every anchor is verbatim in its segment, and every claimed verse is quoted or cited in it (script).
3. **Suspicious rows:** long segments with few or no positions are flagged for a second pass.
4. **Second-model spot checks:** a sample of rows per batch is re-indexed by another model, and disagreements are listed.
5. **Index-miss log:** the keyword fallback on every page records what the index missed.
6. **Nothing dropped silently:** every refusal or truncated output is recorded. Codex output clipping is avoided with 10k-character deliveries read at 12,000 output tokens; `unreadable` only means broken source text.

## Steps

**A. Model comparison for the index.**
- Index the same 300–500 segments with Opus 5.5, Sonnet 5.5 and Luna max: rivayet and hadith from the 1:6 and 100:1 reference scopes, plus the full poetry roster.
- Measure each against `v5/eval/reference.json` and hand checks:
  - finding-level coverage: does the row hold the point the v4 writer drew from that segment?
  - the known witnesses (Thawbān IBNMAJAH:277, *kenūd* MUFADDALIYYAT:v1p149, ḍ-b-ḥ MUALLAQAT:v1p119#4 and MUFADDALIYYAT:v1p418, Imruʾ al-Qays MUALLAQAT:v1p71#2, Wāḥidī v1p55#2);
  - attribution errors;
  - anchor failures;
  - implicit verse references.
- Estimate: about $5–8 Opus, about $3 Sonnet, under $1 Luna.

**B. Index S1 and S87–114 own-surah material** with the chosen model, about 12M tokens (Opus about $50–60 via the Batch API, $100–120 via single calls). Add the small non-verse rosters (poetry, rhetoric, wujuh, about 5M characters) and each page's capped cross-references.

**C. Grouped-writer pilot on 100:1:** routing by script plus index, five writers. Compare against v4 Sol, v3 Astra and v5 Opus/Sonnet on the same families with the v5 review sheets; measure the full ayah's cost against $5.

**D. Hadith and academic in full** (about 30M tokens; Opus about $150–300), once A–C show the index routes them reliably.

**E. The rest of the corpus,** as other surahs come into production. Amortized over all 6,236 ayat, whole-corpus Opus indexing is about $0.15–0.35 per ayah.

## Estimated cost per ayah after the index exists

| Step | Cost |
|---|---|
| Routing (scripts) | $0 |
| Optional leads | ~$0.2–0.3 |
| 5 Sonnet medium writers | ~$2–2.5 |
| Amortized index | ~$0.05–0.35 |
| **Total, Sonnet writers** | **~$2.5–3.5** |
| Total with Opus on two groups | ~$4–5 |

## Carried over from v5

Keep:
- `ranges.py` (overlay);
- `common.TRANSLATION_OK` (Islāḥī);
- `read.py` deliveries and `selfcheck`;
- `run_codex.py` (Codex pattern, per-request context check);
- `account.py`, `check.py`, `evaluate.py`;
- `leads.py`;
- structured briefs: exact command table, numbered steps, self-check before stopping.

Drop:
- per-family writers;
- writer-side search loops;
- extraction by quoting.

## Open at the time of writing

- The v5 pilot's Luna extractors (68, quoting design) were still running in batches when this plan was written; they test a step v6 drops. Keep them as a recall comparison or stop them: the user's call.
- How Opus indexing runs (subagents or the Batch API).
- The prose volume target per ayah.
