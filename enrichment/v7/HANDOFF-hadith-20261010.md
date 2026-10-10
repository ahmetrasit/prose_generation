# Handoff 2026-10-10: hadith missing from tier 1

## Issue

The other computer's agent found that the tier-1 source-kind filter left out hadith segments that are tied to a verse.
For example, Riyāḍ al-Ṣāliḥīn chapters open with `قال الله تعالى: {…} [البينة: 5]`. Ten of those segments fall in the
production range (S59, S90, S92, S97, S98), and neither tier-1 input path reached them.

## Cause

Two design decisions, both made on 2026-10-07, left a gap between them. Nothing was excluded on purpose.

1. **The v7 plan** kept tier 1 to commentary-type kinds. Hadith, together with poetry, lexicon, wujūh and grammar, was
   left to a later "word stage" keyed by term or matn, which was never built. `KINDS` in `digest.py` therefore had no
   `'hadith'`, and `gather()` skipped every verse-indexed hadith segment as "kind hadith: meal table or a later
   stage". The skip was recorded, not silent.
2. **The quotation packet** (`quote_packet()`) brought hadith into tier 1 when a passage quotes the verse's words. It
   searches only segments with no verse key (`seg.s IS NULL`), on the assumption that `gather()` handles every
   indexed segment.

The 165 RIYAD segments that have a verse key were caught by neither path.

## Fixes (`enrichment/v7/digest.py`; fix 6 in `enrichment/v9/q.py`)

| # | Fix | Commit |
|---|---|---|
| 1 | `'hadith'` added to `KINDS`, so `gather()` digests the 165 verse-indexed hadith segments | 7ece8a7e1 |
| 2 | `GUIDE['hadith']` now says "a chapter heading that opens with the verse, or a report" and asks for the theme the compiler files the verse under | d54815a9d |
| 3 | `quote_packet()` also searches indexed hadith/sīra/poetry segments, for the ayat **outside** their key (a chapter quotes several verses but is indexed to one); the ayat inside the key stay with `gather()`. `verses` reads `S:A (quoted; indexed S:A-E)`. In `build()`, a quote hit already gathered for another ayah of the same run has its scope merged, and `verses` adds `(also quoted: S:A)` | d54815a9d |
| 4 | Older bug found while testing: a 3-word window was skipped when a shorter window inside it had already matched. Hadith, sīra and poetry match only on 3-word windows, so they almost never got a chance. Such a window is now still searched, for those kinds only | d54815a9d |
| 5 | Older bug found while testing: `normalize_map()` turned Uthmani ىٰ into "يا" (عَلَىٰ → عليا, إِلَىٰ → اليا), which plain-text على never matched. It also made some windows look unique when they were not. The dagger alif after ى is now dropped | d54815a9d |
| 6 | `q.py` `plain()` (the writer's search tool) drops the dagger alif after ى the same way, so it agrees with `normalize_map()` | d54815a9d |

Sonnet code review: fix 1 OK; fixes 2–6 OK after three rounds (two small follow-ups: the `also quoted` note and fix 6).

## Effect on S1, S59, S87–114 (319 ayat)

- **`gather()`:** +10 verse-indexed RIYAD segments.
- **Quotation packet:** 2,320 → 3,123 segments; 3.78M → 4.47M characters.
  - **Added: 838 segments.** 632 are hadith (19 of them indexed RIYAD chapters reached through another verse), plus
    36 sīra, 14 poetry, and 156 commentary-type segments that were reached only through ىٰ words.
  - **Gone: 35 segments.** All 35 were false matches from four windows that looked unique only because of the ىٰ
    bug:
    - 104:7 «تطلع علي», shared with 5:13 تَطَّلِعُ عَلَىٰ;
    - 96:8 «ان اليا», which matched "إلياس";
    - 88:5 «انيه», shared with 33:53 إِنَىٰهُ;
    - 87:5 «احويا».

  Their existing digests stay in the old runs, but these segments are no longer counted as material for those ayat.

## One digest serves every verse it names (2026-10-10, decided with the user)

A segment is digested once. The brief already asks for the whole segment ("Cover the whole segment, not only the
verses in scope"), and each row names the verses it is about. A segment is therefore never digested again for another
verse. Instead its digest is linked to every verse it names. Measured over S1, S59 and S87–114, before this change:

- **Range rows were invisible.** 6,676 rows name a range (`105:3-5`) and about 1,000 more use other forms (`92:7,10,12`,
  a bare number). `merge.tier1_rows` matched only exact `S:A`, so no map saw these rows. Now
  `digest.verse_list` expands them: +7,627 notes over the 319 ayat (105:4 +193, from 246).
- **Mentions were ignored.** A row about another verse that quotes or names this one (its `mentions`) is now filed
  under this verse too, marked `(about X; names this verse)`: +8,452 notes (96:1 +170).
- **Segments tied to a verse whose notes are about other verses** (by index range or quotation) are not put into the
  map. `q.py linked V` lists them with their notes, from a per-verse index that `enrichment/v9/linked.py build`
  writes (a quotation search takes ~40 s, so the index is built once per range). Most are pages indexed to a wide
  range (`96:1-19`) whose text discusses other verses. A spot check measures how often such a segment does discuss
  the verse after all.

Files: `enrichment/v7/digest.py` (`verse_list`), `enrichment/v7/merge.py` (`tier1_rows`, `tier1_segments`,
`segment_rows`, `row_line`), `enrichment/v9/map.py` (`ROW_FIELDS` + `via`, `about`), `enrichment/v9/q.py` (`linked`),
`enrichment/v9/linked.py`. Note IDs are unchanged and no existing note is lost.

**Existing maps:** they gain these notes through `map.py update-all`. That is a Sol run, so its cost is reported and
approved before it runs.
- `q.stale` does not change, so meals are not blocked meanwhile.
- `tools/ready_pages.py` lists such verses as "tier-1 notes not in the map yet" until the update runs.
- `map.py refresh_rows` refreshes the notes a map has and reports the new ones instead of refusing.
- v7 tier 2 (`merge.py build/update`) takes range rows but not mention rows (`mentions=False`).

**Verse values:** `digest.verse_list` also handles en dashes and annotated values ("Qur'an 2:255", "Surah Yusuf
12:5"). It does not read a Bible reference ("Luke 1:5", "Ps 23:1") or anything after it in the same value, a number
after free text ("2:5, p. 12"), a reversed or cross-sūra range, or an ayah number above 286.
`linked.py build` prints how many tier-1 verse values it could not read and logs each distinct one under
`enrichment/v9/linked/logs/`. On the first build there were 793 values, 97 distinct, mostly `*`, empty strings or
names.

## To do on the tier-1 computer

1. `git pull`, then `python3 -B enrichment/v2/tools/corpus.py fresh`. The index must be "current"; this change
   does not touch the index.
2. Build tier 1 for the whole range once, with the quotation packet:
   `digest.py build <RUN> --surahs 1 59 87 88 … 114 --models gpt-6-luna:max --skip-done luna-max --quotes`.
   Only segments never digested are picked: the new hadith and quotation material, sources imported after the
   earlier runs (96:1 has 30 undigested segments, Turkish tafsirs and hadith among them), and S59, which has no
   run of its own. Already-digested segments are skipped on purpose: their digests are linked, not redone. Check the
   printed totals and the forecast before running.
3. Run it, push `out/` and `runs/*/run.json` as usual, then run `digest.py check/report`.
4. `python3 -B enrichment/v9/linked.py build --surahs 1 59 87 88 … 114` (about 3 minutes, no model), so
   `q.py linked` works for the range. Rebuild it after any corpus rebuild.
