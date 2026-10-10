# Independent review of the Tier 1 and enrichment workflow — 2026-10-10

Commit reviewed: `9e2fc1939` ("Review and harden Tier 1 and enrichment workflow integration"), against `ab261386e`.
`REVIEW-workflow-20261010.md` was treated as a claim to test, not as an authority. Every number below was measured on
this machine's data (git-synced work, maps and corpus index of 2026-10-09 19:23). No repository code was changed and no
model was called; all checks were local and read-only. No independent Sonnet review has happened yet.

## Verdict: not ready for a production run

The commit fixes real problems: CHECK verses are now enforced by every reader, failing checks exit non-zero, repairs are
tracked, and translations can no longer be replaced by worse output. It also brings regressions. One of them will block
40% of the saved maps the first time a full map check runs. Fix or decide items 1–4 before the recheck launch or any
`map.py check RUN` / `update-all` / `refresh-rows` / `ready_pages.py --fresh`.

| # | Severity | Item | Blocks | Needs |
|---|---|---|---|---|
| 1 | High | 368 of 929 saved maps would be blocked | maps, pages, writer, meal, translation | decision, then code |
| 2 | High | Automatic startup retry no longer works | any scripted run (recheck, maps, translations) | code |
| 3 | Medium–high | `writer.py check` aborts on any stale map of the page's surah | writer agents, render | code |
| 4 | Medium | Recheck now ~$91 / 3,942 agents, not ~$55 / 2,074 | recheck launch | decision |
| 5 | Medium | `map.py check` takes ~45–60 min; `maptr.py build` aborts on an unmapped verse | operations | code |

## 1. 368 of 929 saved maps would be blocked (high)

The new snapshot check (`map.snapshot_problem`, `map.row_changes`) marks a map unusable when any saved note is
unavailable or changed in Tier 1. It runs in `map.py check RUN`, `update`, `update-all`, `refresh-rows` and
`ready_pages.py --fresh`, and records `tier1_problem` in the manifest. `q.stale` then refuses the map, so the
writer, meal, translation and render steps stop for that verse. The only remedy the code offers is a full Sol rebuild
with `--supersede`.

Replay over every saved map (`merge.tier1_rows` vs `rows/<k>.json`, 101 minutes):

- 929 maps checked, **368 flagged**: map_s096 191, map_s087 113, map-103_1 28, map_s103 26, map_s103w 6, map_s096r 2,
  maptest 2.
- 1,525 saved notes unavailable; **0 notes with any changed field**.
- Today `q.stale` reports all 925 assembled maps as current, only because no full check has run since the commit.

Cause: 756 digested segments have no valid luna-max digest in any run, so their notes are missing from maps and from
the recheck. They explain 340 of the 368 flagged maps exactly. The other 28 are in the old map-103_1 test run.

| Source | Segments | Reason |
|---|---|---|
| ISLAHI-TADABBUR | 620 | source text changed in the 2026-10-09 corpus rebuild ("excerpt or source input changed") |
| BURHAN | 54 | invalid row |
| ITQAN | 37 | invalid row |
| IBNQUTAYBA-MUSHKIL, TABATABAI, DAMGHANI, ASAD-NOTES, SAMARRAI-*, others | ~45 | invalid row; 2 ELMALILI stale |

Of the invalid rows, 130 carry `verses: ["*"]` (the whole-verse word tag put in the verses field), 2 are empty and 2
name ayah 0. One bad row drops every note in its segment. Notes lost from maps, by source: ISLAHI-TADABBUR 912,
BURHAN 116, ITQAN 59, DAMGHANI 27, IBNQUTAYBA-MUSHKIL 25, SAMARRAI-ASRAR 24, TABATABAI 15. Rejected segments
indexed to scope surahs include 30 in S59 and 18 in S89.

Re-digesting does not simply restore them. Note ids are `loc/rN` with no run name, so a new digest reuses the old ids
with new content, and the check then reports them as changed.

**Decision needed:** how a map treats notes that become unavailable. Options: keep them visibly marked as withdrawn
(map stays usable, the page shows the mark); drop them from the saved map and run an update; or rebuild the map.
Rebuilding 368 verses with Sol is a large cost and should not be the automatic answer for unchanged content. Separately,
re-digest or repair the 756 segments, and decide whether one bad row should still discard a whole segment.

## 2. Automatic startup retry no longer works (high)

`rerun_failed_start.failed_before_session` now retries only a run with no thread id, no usage and nothing but `error`
events. All 396 recorded real startup failures (in `*_failed_start/` across t1_s087, map_s096, map_s096r, map_s103,
map_s103w, maptest, tr_s103) were network timeouts ("workspace routing discovery timed out") with 0 requests and $0,
but each has `thread.started`, `turn.started` and `turn.failed`. **0 of 396 qualify.** `run_until_done.sh` now stops
after the first pass, and `codex_run.py` refuses to start those agents again ("repair that session"). In a
3,942-agent run, every network outage would need manual repair.

Fix: classify by zero requests, empty usage and no completed item other than `error` (no command, file change or
message), whatever the thread id.

## 3. `writer.py check` aborts on any stale map of the page's surah (medium–high)

`q.load` now exits the program when a map is stale. `writer.check` loads every mapped verse of the page's own surah
before it reaches its new "map not current" problem list, so that list is never reached for a stale map, and an
unrelated update in the same surah aborts the check. This hits the Opus writer agents' own check loop and
`render.py`, which now runs the writer check first.

Fix: call `q.stale` first, record problems, and load only current maps.

## 4. Recheck cost (medium, decision)

`recheck.py plan --mapped --verses-file enrichment/v7/recheck/scope_s1_s59_s87-114.txt` on current data:

| | Handoff (before the fixes) | Now |
|---|---|---|
| Candidate pairs | 24,613 | 24,244 |
| Segments to check | 15,439 | 15,323 |
| Source characters | 25.9M | 25.7M |
| Rendered agent input | ~41M (×1.6 estimate) | **68.9M** |
| Luna agents | ~2,074 | **3,942** |
| Cost estimate | ~$55 | **~$91** |

Pairs by marker only: 3,708; by explicit citation plus full verse (new): 301. Seventy-five segments exceed the chunk
size and stand alone. The growth comes from printing every earlier note in full JSON (about 63% of the input).
Compact notes (claim, verses, mentions, anchor) would recover most of it.

## 5. Other regressions (medium)

- **`map.py check RUN` speed.** It now reads Tier 1 for every verse: measured 874 s for the first verse in a process
  (cold), then about 6 s per verse, so roughly 45–60 minutes for a 300–475-verse run. Before, it took seconds.
- **`maptr.py build` aborts on an unmapped verse.** `q.stale` returns "no assembled map" and the build exits
  ("nothing built") instead of printing a note and skipping the verse. Reproduced with `--ayat 96:1 9:1`; nothing
  written. Current `prod_s*/verses.txt` lists contain no unmapped verse, so this is latent.

## Lower severity

- **Verse markers (net improvement).** Against the old parser on the 43,558 non-Quran segments indexed to S1, S59 and
  S87–114, the new label rule drops 307 false markers from Shamela footnote marks `(¬N)` and 172 citations of other
  surahs. It loses about 38 correct markers: `(سورة الأعلى الآية 1)`, `(الفاتحة آية 7)`, Asad's
  "i.e., verses 2-17", Corpus Coranicum's "V. 3–5".
- **`q.py linked`.** `linked.stamp()` now hashes every segment's full text: about 19 s per call (was about 6 s), and
  writer agents call it repeatedly. Every existing link index shows a "rebuild" note until rebuilt.
- **`repair.py`** fails with `invalid literal for int()` on the legacy unnumbered `repair.stream.jsonl`
  (t1_s103_20261009 c32).
- **Claims in `REVIEW-workflow-20261010.md` that the code does not implement.** The recheck chunk's `input_sha256`
  is recorded but never checked, so earlier notes that change after a build go unnoticed. Segments that keep only
  recheck notes (their digest no longer valid) are not marked as such in `merge.segment_rows` or `q.py linked`.

## Gaps and silent failure points

- **Largest coverage gap:** 53,839 pairs reachable only through too-common 2-word windows are not checked, 2.2 times the
  24,244 pairs that are.
- **The 756 rejected segments** are reported one warning at a time during plan or build. Nothing tracks them in one
  place or queues them for re-digestion; maps lose their notes without a map-level signal until item 1 fires.
- **Native Codex sessions** (no `runs/` folder) count as finished whether or not they completed (`digest.unfinished`).
- **Readers drop lines without a message** when a segment has duplicate lines or is missing from the corpus
  (`digest.valid_output_locs`). There are 0 such cases today.
- **Overlapping recheck runs** are forbidden only in the docs; nothing enforces it.
- **Not verified (needs a live session):** whether a same-session repair can resume a session that failed before its
  first model request, and whether the resumed session's cost lands in the same session file.

## What checked out

- `digest.run_record` gives the same completion result as before on all 4,058 local run folders, including the 31 with
  repairs.
- Recheck notes pass the same CHECK-verse rule in the checker, coverage tracking (`checked_before`) and every reader.
- Check commands exit non-zero and print every problem; unknown chunks and model tags fail.
- `q.translation` keeps a complete current translation over a newer partial or malformed one.
- Map assembly stamps are written on assembly; `q.stale` reports all 925 current maps as OK today.
- No out-of-scope tier-1 output directories; no duplicate-line or missing-corpus locators in 5,043 output files.

## Order of work

1. Decide item 1 (unavailable notes in maps) and item 4 (note rendering in the recheck input).
2. Fix items 2, 3 and 5 and the item-1 policy in code; each changed script gets its own read-only Sonnet reviewer.
3. Re-digest or repair the 756 rejected segments (Luna; cost to be planned and approved).
4. Then run the full map checks, rebuild link indices, and plan and approve the recheck.

## Fixes applied (2026-10-10, same day)

The user agreed with every recommendation: saved notes stay in their maps and are marked, nothing forces a rebuild;
earlier notes are shown compactly to the recheck agent. The user runs the Luna and Sol agents. Every changed script had
its own read-only Sonnet reviewer; every patch went back to the same reviewer until it confirmed (13 scripts, up to 3
rounds). No model job was run; tests used fixtures, a copy of map_s103_20261009 and read-only passes over real data.

| Item | Fix | Verified |
|---|---|---|
| 1. Maps blocked | `map.reconcile`/`sync_tier1`: unavailable notes marked in `rows/<k>.tier1.json`; a changed note keeps its mapped version and its new content is offered to the next update as `<id>~<k>` (older version then marked replaced); author/death/missing anchor refreshed in place, stamp renewed; `tier1_problem` no longer used. `q.py` and pages show the marks | 929 maps: 1,525 notes marked in 368 maps, none blocked; copy: full check 80/80 assembled; simulated changed note → update with `~2`, then replaced |
| 2. Startup retry | proof = failed run, no request/usage/cost, stream of start/error/turn.failed only, every error the known pre-request failure ("workspace routing discovery timed out"); unproven failures listed for review; bad records no longer abort the sweep | 396/396 recorded failures accepted; 0 of 6,014 completed runs; unknown disconnect, reasoning/file/message items rejected |
| 3. Writer check | stale maps are problems (needed verses) or NOTEs (other same-surah verses); no exit. Same for `q.py index/question/notes/find`, `surah.py`, `maptr.py check`; unreadable map files are reported, not crashes | fixtures |
| 4. Recheck cost | earlier notes one compact line each (verses, mentions, speaker, stance, claim, exact words) | plan: 58.4M characters, 3,276 chunks, ~$77 (was 68.9M / 3,942 / ~$91) |
| 5. Speed, translation build | `merge.tier1_rows_by_verse` (one pass for all verses) in map check/update/refresh/build and `ready_pages --fresh`; manifest parse cache in `valid_output_locs`; `maptr.py build` notes and skips unmapped verses | one pass for 925 verses: 182–274 s cold (was ~874 s for the first verse + ~6 s each); rows identical on 6 verses incl. mention rows |
| Markers | label rule: this surah's name or a verse word, also after other words; another surah named anywhere is rejected; `والآية` accepted; capitalised Latin words other than common leads are taken as possible surah names | 28 fixture cases; a bare Latin name of the same surah ("Fatiha, verse 3" in S1) is still rejected (names table is Arabic only) |
| Link stamp | `linked.stamp_cached()` (corpus/wal/overlay mtime, size, inode, ctime + code hash) for `q.py linked` | |
| Repair helper | legacy unnumbered `repair.stream.jsonl` handled (repair 0 in `digest.run_record`) | completion unchanged on all 4,058 run folders |
| Other | `segment_rows` marks recheck-only segments; recheck `build` refuses while earlier recheck chunks are unanswered (`--allow-overlap`) | |

**New finding, fixed: the range overlay pointed at the wrong segments.** `enrichment/v5/index/range_overlay.jsonl`
(81 rows) stores numeric segment ids; the 2026-10-09 corpus rebuild renumbered them, so all 81 rows extended the verse
range of unrelated TAB-FULL pages (it also crashed `gather` on three rows). `digest.overlay_rows()` now resolves each row
by its locator and prints rows it cannot apply; tier-1 gathering, the quotation packet and the recheck use it. No
tier-1 run digested a wrong segment under an overlay verse. 30 of the 81 intended overlay segments have no valid
digest yet. Link indices built before the fix need rebuilding.

**Re-digesting the 756 segments.** `digest.py rejected OUT` lists them (with the verses that reached them);
`digest.py build RUN --ayat <OUT's ayat> --quotes --skip-done luna-max --only-locs OUT --models gpt-6-luna:max`
builds exactly those: 756 of 756 gathered, 129 chunks, 2.34M characters (about $3 at the tier-1 rate; probe build
deleted). Separately, 32,168 segments sit in chunks that were built but never run (s1_r13_augrefs938_20261008 31,317,
pilot100-20261007 1,015); `--include-unanswered` lists them.

**Still open (decisions for the user, not code):** `update-all` will offer 31,694 tier-1 notes that no map has placed
yet (range, mention and supplement rows); the 53,839 pairs reached only through too-common windows stay outside the
recheck; one bad row still discards its whole segment.
