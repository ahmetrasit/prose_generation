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
| 2 | `GUIDE['hadith']` now says "a chapter heading that opens with the verse, or a report" and asks for the theme the compiler files the verse under | (this commit) |
| 3 | `quote_packet()` also searches indexed hadith/sīra/poetry segments, for the ayat **outside** their key (a chapter quotes several verses but is indexed to one); the ayat inside the key stay with `gather()`. `verses` reads `S:A (quoted; indexed S:A-E)`. In `build()`, a quote hit already gathered for another ayah of the same run has its scope merged, and `verses` adds `(also quoted: S:A)` | (this commit) |
| 4 | Older bug found while testing: a 3-word window was skipped when a shorter window inside it had already matched. Hadith, sīra and poetry match only on 3-word windows, so they almost never got a chance. Such a window is now still searched, for those kinds only | (this commit) |
| 5 | Older bug found while testing: `normalize_map()` turned Uthmani ىٰ into "يا" (عَلَىٰ → عليا, إِلَىٰ → اليا), which plain-text على never matched. It also made some windows look unique when they were not. The dagger alif after ى is now dropped | (this commit) |
| 6 | `q.py` `plain()` (the writer's search tool) drops the dagger alif after ى the same way, so it agrees with `normalize_map()` | (this commit) |

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

## To do on the tier-1 computer

1. `git pull`, then `python3 -B enrichment/v2/tools/corpus.py fresh`. The index must be "current"; the code change
   does not touch the index.
2. **S59 and S88–114** have no tier-1 run yet. The first build with this code (`--quotes`) includes the new material
   automatically.
3. **S1, S87, S96 and S103** already have runs. Build one top-up run over all of them together, so each new segment is
   digested once with its full scope:
   `digest.py build <RUN> --surahs 1 87 96 103 --models gpt-6-luna:max --skip-done luna-max --quotes`.
   Only segments not yet digested are picked. Check the build's printed segment and character totals, and the
   cost forecast, before running.
4. Run it, push `out/` and `runs/*/run.json` as usual, then run `digest.py check/report`.
5. Any focus-ayah map already built for these ayat lacks this material. `enrichment/v9/material.py` lists the new
   segments under "quotes" once they are digested.

## Known limitation (not changed)

`--skip-done` is keyed by locator. A segment digested for one ayah in an earlier run is not digested again for another
verse it quotes in a later run. It is recorded as "already digested", not dropped silently. No RIYAD segment had been
digested before this fix, so building each range in one run (steps 2–3) avoids the problem for them.
