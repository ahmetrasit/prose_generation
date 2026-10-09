# Enrichment v9 runbook: one surah, from tier 1 to the enriched pages

For a cold orchestrator in a **Claude Code** session, at the repo root `/Volumes/aro/projects/prose_generation`.
Read this whole file, then `## Production state` at the end, before doing anything. Design and decisions:
`PLAN.md` ("Decisions" first). Test standard: `T0-103_1.md`. Tier-1 details: `enrichment/v7/RUNBOOK.md` (stage 1).
The Bible (Ehl-i Kitap) layer has its own runbook: `enrichment/bible/RUNBOOK.md` (stage 6 below).
Memory notes for this project (`~/.claude/projects/-Volumes-aro-projects-prose-generation/memory/`) hold the user's
standing rules; the ones this runbook relies on are restated here.

## Rules

1. **Scope and quota come from the user.** Report a stage's expected cost before it and the actual cost after it.
   Current caps (user, 2026-10-09): tier-1 Luna 40 agents, Luna map translations 20, Sol 40, Opus page agents
   (writers + meals) **3 at a time from S87 on** (S96 had 5), **Bible Opus authors 2 at a time** (a separate cap).
   If a cap is not known, ask. Never Haiku.
2. **No cuts anywhere.** Never trim, excerpt, sample or drop input or output. Chunking puts whole segments together;
   a segment larger than a chunk goes alone. Word counts in briefs are soft ceilings, never a reason to drop material.
3. **No silent failures.** Pass every `WARNING`, `NOTE` and `SKIPPED` line to the user; record every gap in the
   source's or run's record.
4. **One agent per spawn file, once.** `codex_run.py` claims a run directory atomically and never starts an agent
   twice. A failed or incomplete agent is repaired by a message to **that same agent** with the exact problems
   (Codex: `tools/repair_t1.sh`, `repair_map.sh`, `repair_maptr.sh`; Opus: SendMessage to its agent id). Never start a
   second session under the same name.
5. **Final passes happen inside the run.** A targeted same-session repair of an Opus writer (named question ids, a
   failed check) costs about $0.3–1 and is fine; do not resume a finished writer for broad rewrites.
6. **Commit and push after every stage and after every ayah page completed**, committing only your own paths
   (`git add <paths>`, `git commit -m … -- <paths>`): `enrichment/v9`, `enrichment/v7/work/<this surah's runs>`, the
   scripts you changed. Never commit another session's work.
7. **Never `git stash`, `git pull --rebase`, `--autostash`, `git reset`, or check out other paths** while anything
   runs (2026-10-09: an importer agent's autostash reverted map rows mid-run). Every agent prompt that commits says so;
   an agent whose push is rejected stops and reports. After agents commit, check that no `.git/rebase-apply` or
   `.git/rebase-merge` is left behind.
8. Briefs are generic: never put verse-specific examples into a brief.
9. **Scripts you write or change get a read-only Sonnet review**, one reviewer per script; a fix goes back to the same
   reviewer (SendMessage) until it says OK.

## How agents run

- **Luna and Sol (Codex):** `enrichment/v9/tools/run_until_done.sh CAP RUNS_DIR LOG <spawn files>` with `nohup … &`.
  It runs `codex_run.py` (atomic claim, one line per agent, `WARNING` for any failure), sets agents that failed at
  start aside (`rerun_failed_start.py`), retries up to 8 passes, and ends the log with `== done` (preceded by
  `== WARNING n agent(s)…` when the last pass had warnings). Each agent's record is `<stage>/runs/<agent>/run.json`.
  Beware `A && B &` in bash: it backgrounds the whole chain.
- **Opus (Claude Code):** agent type `enrich-page-high` (model opus, effort high), one agent per spawn text, at the
  cap; top up as each finishes.
- **Helpers (once per machine boot, before any Codex run):**
  `nohup enrichment/v9/tools/session_archive.sh > /dev/null 2>&1 & echo $! > enrichment/v9/work/session_cleanup.pid`
  (moves Codex session files idle 30+ min and not open by any process to `/Volumes/aro/codex_sessions_archive/`;
  never deletes: repairs copy sessions back) and
  `nohup enrichment/v9/tools/disk_throttle.sh > /dev/null 2>&1 & echo $! > enrichment/v9/work/disk_throttle.pid`
  (SIGSTOPs `codex_run.py` runners under 1.5 GB free on `/`, resumes above 2.5 GB). Keep > 3 GB free (`df -h /`).

## Stages for surah S (dates as YYYYMMDD; the plan fixes the run names)

### 0. Plan
```bash
python3 -B enrichment/v9/surah.py plan S
```
Pages are the base r13 readings (`_commentary/v16/out/S_A/*/S_A.reading.tr.md`, never augment); the verses are every
verse those pages cite. Report the counts and the expected cost to the user.

### 1. Tier 1 (Luna max), including the quotation packet
```bash
python3 -B enrichment/v7/digest.py build <tier1 run> --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt) --models gpt-6-luna:max --skip-done luna-max --quotes [--skip-planned <tier1 runs built but not finished>]
nohup enrichment/v9/tools/run_until_done.sh 40 enrichment/v7/work/<tier1 run>/runs <log> enrichment/v7/work/<tier1 run>/spawn/luna-max_c*.md &
python3 -B enrichment/v7/digest.py check <tier1 run> --model luna-max      # prints every problem (do not tail -1 it)
python3 -B enrichment/v7/digest.py report <tier1 run>
```
Repair each listed chunk in its session: `tools/repair_t1.sh <tier1 run> NN` (several with `xargs -P`). If its
session is gone, set the chunk's output and run dir aside (`out_superseded/`, `runs_superseded/` + README line) and run
its spawn file again. The build takes about 25 s plus 0.35 s per verse. **Never analyse anything twice**
(`--skip-done`, `--skip-planned`). Tier 1 may also run on the user's other computer (handoff via git: this machine
builds and commits `manifest.json`, `chunks/` (force-added; they are git-ignored), `spawn/`; the other runs and pushes
`out/` and `runs/*/run.json`).

### 2. Verse maps (Sol high): new verses, then updates of existing maps
```bash
python3 -B enrichment/v9/map.py build <maps run> --from luna-max --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt) --models gpt-6-sol:high > work/prod_sNNN/map_build.log 2>&1   # ~20 min for 450 verses: background it
python3 -B -u enrichment/v9/map.py update-all --model gpt-6-sol:high --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt) > work/prod_sNNN/update_all.log 2>&1
# order: the plan's focus verses first, then each page's cited verses in page order (example: work/prod_s087/map_order.txt)
nohup enrichment/v9/tools/run_until_done.sh 32 enrichment/v9/work/<maps run>/map/runs <log> $(cat work/prod_sNNN/map_order.txt) &
nohup enrichment/v9/tools/run_until_done.sh 8 <a runs dir> <log> $(grep -o 'spawn enrichment[^ ]*' work/prod_sNNN/update_all.log | cut -d' ' -f2) &
```
**After every map AND update agent has finished — mandatory, this assembles the maps the pages read:**
```bash
python3 -B enrichment/v9/map.py check <maps run>
python3 -B enrichment/v9/map.py check <run>       # for EVERY run whose "== <run>" block in update_all.log built > 0 updates
python3 -B enrichment/v9/map.py report <maps run>
```
`build` skips verses that already have a map (`SKIPPED`); `update-all` builds an update only for mapped verses whose
tier-1 notes grew. Until `check` runs, an updated verse's assembled map is the old one; `writer.py`/`meal.py build`
refuse such a verse (`q.stale`: "assembled map older than its outputs" / "no output yet") — if they refuse, run the
check, do not work around it. A check's `note X is in no position` on an update → `tools/repair_map.sh RUN S:A N`
(N = the update number). A base map that fails → `tools/repair_map.sh RUN S:A`; if its session is gone, rebuild the
verse with `map.py build NEWRUN … --supersede OLDRUN`.

**Pages while maps run** (user, 2026-10-09): `tools/ready_pages.py S` (dry; writes nothing) lists READY/WAIT per writer
and meal; `--build` assembles the ready verses and builds those pages. Spawn their Opus agents at the cap.

### 3. Turkish renderings of the maps (Luna max)
```bash
python3 -B enrichment/v9/maptr.py build <maptr run> --ayat-file enrichment/v9/work/prod_sNNN/verses.txt --model gpt-6-luna:max   # after stage 2's checks
nohup enrichment/v9/tools/run_until_done.sh 20 enrichment/v9/work/<maptr run>/maptr/runs <log> enrichment/v9/work/<maptr run>/maptr/spawn/luna-max_c*.md &
python3 -B enrichment/v9/maptr.py check <maptr run>      # NOTE lines (questions changed after the build) are not failures
python3 -B enrichment/v9/maptr.py report <maptr run>
```
Repair a failing chunk in its session: `tools/repair_maptr.sh <maptr run> NNN`. Only questions without a current,
complete rendering are built; after a map update, a new maptr build picks up the changed questions.

### 4. Pages: writer and meal (Opus high)
```bash
python3 -B enrichment/v9/surah.py pages S        # or tools/ready_pages.py S --build while maps still run
python3 -B enrichment/v9/surah.py agents S       # prompts → work/prod_sNNN/agents.md (a page with a transcript is never re-listed)
enrichment/v9/tools/page_status.sh S A            # writer and meal check + Opus cost of one page
```
Spawn one `enrich-page-high` agent per block, at the Opus cap. Each writer runs its own check and final pass; a page
may cover any mapped verse of its own surah (full coverage). **Meals read `enrichment/corpus/corpus.sqlite` at build
time:** build them only when the corpus is current (meal imports and OCR corrections done, then
`python3 -B enrichment/v2/tools/corpus.py build`). The meal table lists all 93+ meal/translation sources; the ones
with `panel: true` in their `enrichment/corpus/<ID>/source.json` come first (22 since 2026-10-09).
When a page's writer AND meal pass: `python3 -B enrichment/v9/render.py <writer run> --meal <meal run>`, commit, push.

### 5. Finish
```bash
python3 -B enrichment/v9/surah.py status S       # every stage; each page's checks; stale translations counted
python3 -B enrichment/v9/surah.py finish S       # renders each page (md + strip check) and its HTML; warns for English-only questions
```
Outputs: `work/<writer run>/render/<page>.enriched.md` (+ `maps/`), `work/prod_sNNN/<S_A>.html`. Report the actual
cost of every stage against the estimate (`report` commands; Opus from `page_status.sh`).

### 6. Bible layer (after the surah's Islamic enrichment is complete)
Follow `enrichment/bible/RUNBOOK.md` ("Production route from a Claude Code session"). Models: discovery readers Luna
max + Sol high, surah-page image authors Sol max, ayah-page authors Opus high (**2 at a time**). The author prompts
carry the relevance rule (user, 2026-10-09: accept only a shared scene, claim, image, argument or formula, or its
reversal; keyword-only candidates are rejected with that reason). An accepted page is never rewritten in place: a
revision is `enrich.py spawn --surah S --target S:A --attempt N --revise`, then `finish … --attempt N --trial`,
compare, and `enrich.py supersede … --attempt N` (the old page moves to `out/sNNN/superseded/`).

## Meal corpus (enrichment/corpus)

- One directory per source (`source.json` versioned; `segments.jsonl` and `raw/` local, git-ignored). Importers:
  `enrichment/v2/fetch/import_meal_*.py` (`--dry`, ingestion record with issues, counts and `missing`).
- Importers write source files only; **rebuild the index once afterwards**: `python3 -B enrichment/v2/tools/corpus.py build`.
- OCR corrections: `enrichment/v2/fetch/ocr_fix.py SOURCE_ID [--dry]` (confident fixes only; originals kept in
  `text_ocr`, each fix in `ocr_fixes`, summary in the ingestion record).
- Every missing verse of a meal source is recorded in its `source.json` (`ingestion.missing` + notes); a meal
  coverage review fixes what the source allows and records the rest.
- New works: look on archive.org first (`advancedsearch.php`; the uploader "Lami Aydın" has ~126 Turkish editions).

## When something fails

| What happened | What to do |
|---|---|
| `codex_run.py` prints `started earlier without run.json` | running or died: check `ps` for its codex process; died → `tools/recover_run_json.py <runs>` records its cost; rerun with `--retry` only with the user's go |
| a tier-1, map or translation `check` lists problems | repair through the same agent (`tools/repair_*.sh`); if its session is gone, rebuild that unit in a new run |
| `writer.py`/`meal.py build` refuses: no map / map not current | finish stage 2 for those verses / run `map.py check RUN` |
| a writer's `check` fails after its run | SendMessage the exact problems to that writer |
| a usage limit stops agents | after the reset, SendMessage each stopped agent "continue from where you left off" |
| peak context over 120k (tier-1 report) | report; the output is valid if `check` passes |
| git shows a rebase in progress / a stash | an agent broke rule 7: inspect `.git/rebase-apply/autostash` (`git show --stat <hash>`), restore anything it holds that is newer than the tree, then remove the leftover state |

## Production state (update at every stage; last: 2026-10-09 ~15:30)

| Surah | Tier 1 | Maps | Translation | Pages | Rendered | Bible |
|---|---|---|---|---|---|---|
| 103 | done | done (+ updates) | done (74/74, $2.19) | 103:1 (test page `w103_1-20261008`), 103:2, 103:3 done | md + HTML done | done 2026-10-09 (old prompt); **re-author all 3 ayat after the relevance test** |
| 96 | done ($92.06) | done ($162.36 + updates) | done (265/265, $7.87) | 96:1–19 done ($86.42 Opus) and repaired | md + HTML done (`prod_s096/*.html`) | not started (cap 2, after the test) |
| 87 | done (993/993, $55.65) | done: 334 new ($121.49) + 57 updates; all reassembled 2026-10-09 15:20 | `tr_s087_20261009` running (167 chunks) | writers done: 87:1, 2, 5, 6, 7, 8; running: 87:9, 10, 11; built, queued: 87:3, 4, 12–19; **meals: 19 READY, not built** (wait for OCR fix + corpus rebuild) | — | not started |

**Resume (in this order):**
1. `git pull` (only if nothing runs); start the helpers (see "How agents run"); `df -h /`.
2. S87 writers: keep 3 Opus running from the queue (87:3, 87:4, 87:12–87:19; their spawn files are
   `work/w_87_A_20261009/write/spawn/opus-high.md`). `tools/page_status.sh 87 A` after each; commit outputs.
3. OCR correction agent (sources: Akdemir, Öztürk, Eliaçık, Duman, Çelik, Doğrul, Vehbi, Riyad-TR): when it
   reports, `python3 -B enrichment/v2/tools/corpus.py build`; then build the 19 S87 meals
   (`tools/ready_pages.py 87 --build` builds the missing meals) and run them inside the Opus cap; render each page
   when writer + meal pass; commit.
4. Then spawn the meal coverage review agent (every meal source: missing ayat; fix from the source if possible,
   otherwise record in source.json; no git stash).
5. S87 translations: when `tr_s087` is done, `maptr.py check/report`; `surah.py finish 87`.
6. Bible: test re-author of 103:1 is running (`enrichment/bible/work/s103/ehlikitap.103_1.opus.high.a2`). When it
   replies: `enrich.py finish --surah 103 --target 103:1 --attempt 2 --trial`, compare with the accepted page
   (blocks, kinds, keyword-only links gone). If better and the user agrees: supersede 103:1, re-author 103:2/103:3 the
   same way, **prepare for compaction (update this section, commit)**, then S96 and S87 Bible production at 2 Opus.
7. Pending user decisions: import the Lami Aydın priorities (Mâtürîdî Te'vîlât, Tahâvî Ahkâm, Molla Câmî, Çantay
   tefsirli, Kattân, Çetin, Cerrahoğlu); 103:1 writer rerun for notes its maps gained after it was written.
