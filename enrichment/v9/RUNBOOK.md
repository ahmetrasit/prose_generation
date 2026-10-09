# Enrichment v9 runbook: one surah, from tier 1 to the enriched pages

For a cold orchestrator in a **Claude Code** session, at the repo root `/Volumes/aro/projects/prose_generation`.
Design and decisions: `PLAN.md` (read its "Decisions" section first). Test standard: `T0-103_1.md`. Tier-1 details:
`enrichment/v7/RUNBOOK.md` (stage 1 only).

## Rules

1. **Scope and quota come from the user.** Before a surah, report the plan's expected cost (`surah.py plan`) and
   use the quota the user gave: Luna up to 60 agents at a time (raised from 50, 2026-10-09), Sol as the user allows, Opus at most 3 agents at a time (user, 2026-10-09) (2026-10-09:
   production go for Sol, Luna and Opus). If no quota is known, ask.
2. **No cuts anywhere.** Never trim, excerpt, sample or drop input or output. Chunking puts whole segments together;
   a segment larger than a chunk goes alone.
3. **No silent failures.** Pass every `WARNING`, `NOTE` and `SKIPPED` line to the user verbatim.
4. **One agent per spawn file, once.** `codex_run.py` never starts an agent whose run directory exists. A failed
   agent is repaired by a message to that same agent while its context is fresh, or rebuilt in a new run with the
   user's go; never start a second session under the same name.
5. **Final passes happen inside the run** (the briefs say so). Do not resume a finished Opus agent later for fixes:
   its whole context is read again (a resumed writer cost $3.27 on the 103:1 test).
6. **Commit and push after every stage and after every ayah page completed** (writer and meal checked, rendered;
   user, 2026-10-09) (only `enrichment/v9`, `enrichment/v7/work/<this surah's runs>`, and the
   scripts you changed). Never commit another session's work.
7. Briefs are generic: never put verse-specific examples into a brief.

## How agents run

- **Luna and Sol (Codex):**
  `python3 -B enrichment/v9/codex_run.py --parallel N <spawn files>` (N = the user's cap; since 2026-10-09 evening: tier-1 Luna 40, Luna translations 20, Sol 20, Opus 3; for the rest of S96 only: 3 Opus writers + 2 Opus meals at once, back to 3 for S87). Run it in the
  background; it prints one line per agent. Each agent's record is `<stage>/runs/<agent>/run.json`.
- **Opus (Claude Code):** agent type `enrich-page-high` (model opus, effort high). For each prompt block in
  `work/prod_sNNN/agents.md`, spawn one agent with exactly that text. Several may run at once.

## Stages for surah S (dates as YYYYMMDD; the plan fixes the run names)

### 0. Plan
```bash
python3 -B enrichment/v9/surah.py plan S
```
Pages are the base r13 readings (`_commentary/v16/out/S_A/*/S_A.reading.tr.md`, never augment); the verses are
every verse those pages cite. Report the counts and expected cost to the user.

### 1. Tier 1 (Luna max), including the quotation packet
```bash
python3 -B enrichment/v7/digest.py build <tier1 run> --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt) --models gpt-6-luna:max --skip-done luna-max --quotes [--skip-planned <tier1 runs built but not finished>]
python3 -B enrichment/v9/codex_run.py --parallel 50 enrichment/v7/work/<tier1 run>/spawn/luna-max_c*.md
python3 -B enrichment/v7/digest.py check <tier1 run>
python3 -B enrichment/v7/digest.py report <tier1 run>
```
The build takes about 25 s plus 0.35 s per verse. If `check` lists a chunk, report it and repair (rule 4).

**Never analyse anything twice.** `--skip-done` skips every segment a finished Luna run digested; while another
surah's tier-1 run is built but not finished, pass it to `--skip-planned` so its segments are not built again
(check: the two manifests share no locator). Map and translation builds skip verses and questions planned in other
runs automatically. The only re-read is a segment an earlier run saw only as an excerpt (37, all in
`q103_1-20261008`): it is read whole once.

**Tier 1 runs on the user's other computer** (user, 2026-10-09: "i'll run tier 1 luna in a separate computer").
This machine builds the run (`digest.py build …`) and commits `manifest.json`, `chunks/`, `spawn/`; the other machine
pulls and runs the spawn files, then commits `out/` and `runs/*/run.json` and pushes; this machine pulls and runs
`check`/`report`. A chunk whose `runs/<agent>/run.json` is committed is never run again (`codex_run.py` skips it).
Before a handoff, move agents that failed at start aside (`tools/rerun_failed_start.py <run>/runs`) so their failed
run.json does not block a rerun, and write records for agents whose runner was stopped
(`tools/recover_run_json.py <run>/runs`). On the other machine:
```bash
git pull
python3 -B enrichment/v9/codex_run.py --parallel 60 enrichment/v7/work/<tier1 run>/spawn/luna-max_c*.md
python3 -B enrichment/v9/tools/rerun_failed_start.py enrichment/v7/work/<tier1 run>/runs   # then run the line above again
git add enrichment/v7/work/<tier1 run>/out enrichment/v7/work/<tier1 run>/runs/*/run.json && git commit -m "…" && git push
```

### 2. Verse maps (Sol high): new verses, then updates of existing maps
```bash
python3 -B enrichment/v9/map.py build <maps run> --from luna-max --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt) --models gpt-6-sol:high
python3 -B enrichment/v9/map.py update-all --model gpt-6-sol:high --ayat $(cat enrichment/v9/work/prod_sNNN/verses.txt)
python3 -B enrichment/v9/codex_run.py --parallel <Sol cap> enrichment/v9/work/<maps run>/map/spawn/sol-high_*.md <every update spawn printed by update-all>
python3 -B enrichment/v9/map.py check <maps run>          # and `check <run>` for every run update-all touched
python3 -B enrichment/v9/map.py report <maps run>
```
`build` skips verses that already have a map (`SKIPPED`); `update-all` builds an update only for mapped verses whose
tier-1 notes grew. `check` without `--ayah` assembles every finished map (`<k>.jsonl`, `<k>.md`).

### 3. Turkish renderings of the maps (Luna max)
```bash
python3 -B enrichment/v9/maptr.py build <maptr run> --ayat-file enrichment/v9/work/prod_sNNN/verses.txt --model gpt-6-luna:max
python3 -B enrichment/v9/codex_run.py --parallel 50 enrichment/v9/work/<maptr run>/maptr/spawn/luna-max_c*.md
python3 -B enrichment/v9/maptr.py check <maptr run>
python3 -B enrichment/v9/maptr.py report <maptr run>
```
Only questions without a current rendering are included; after a map update, run a new maptr build for the changed
questions.

### 4. Pages: writer and meal (Opus high)
```bash
python3 -B enrichment/v9/surah.py pages S        # writer.py and meal.py builds; refuses while a map is missing
python3 -B enrichment/v9/surah.py agents S       # prompts → work/prod_sNNN/agents.md
```
Spawn one `enrich-page-high` agent per block in `agents.md`, **at most 3 Opus agents at a time** (user, 2026-10-09); top up as each finishes. Each writer runs its own check and final pass.

### 5. Finish
```bash
python3 -B enrichment/v9/surah.py status S       # every stage; each page's checks
python3 -B enrichment/v9/surah.py finish S       # renders each page (md + strip check) and an HTML reading view
```
Outputs: `work/<writer run>/render/<page>.enriched.md` (+ `maps/`), and `work/prod_sNNN/<S_A>.html`. Report the
actual cost of every stage against the plan's estimate (`report` commands; Opus costs from `digest.claude_usage`).

## Several surahs at once

Plan each surah; build their tier-1 runs one after the other, each with `--skip-planned` naming the earlier unfinished
runs; run all their spawn files through one `codex_run.py` call (one Luna cap). Maps: build per surah after its tier
1 is checked; a verse planned in another surah's map run is `SKIPPED` and that surah's pages wait for it
(`writer.py build` refuses until every cited verse has a map).

**Tier 1 still running elsewhere.** Map builds read only finished chunk outputs (`NOTE … its agent has not finished;
not read`). A verse whose segments are still queued in another surah's tier-1 run (check the run manifest's chunk
`scope`) is not mapped yet: list it in `work/prod_sNNN/verses_wait_*.txt` and map it after that run finishes, so a map
is never built on a fraction of its notes. Notes of other verses that arrive later go through `update-all`.

**Disk space (2026-10-09 incident).** Codex writes every session to `~/.codex/sessions` on the system disk; on
2026-10-09 the disk filled and 1,089 agents failed at start (`No space left on device`, 0 commands, $0). Before a big
run check `df -h /` (keep > 3 GB free). A loop (pid in `work/session_cleanup.pid`) moves session files idle for 10
minutes to `/Volumes/aro/codex_sessions_archive/` every 5 minutes (a running agent keeps writing its file; a finished
one's cost is already in its run.json). Never delete them: a same-session repair needs the session, and the repair
scripts copy it back from the archive. Agents that failed at start (0 commands) are moved to
`<runs>_enospc/` or `<runs>_failed_start/` (evidence kept) and the same spawn files are run again; never move an agent
that ran commands.

**Disk throttle.** `tools/disk_throttle.sh` (pid in `work/disk_throttle.pid`, log `work/disk_throttle.log`) pauses
every `codex_run.py` runner with SIGSTOP when the system disk has under 1.5 GB free (no new agents; running ones
finish) and resumes them above 2.5 GB. About 100 concurrent Codex agents push swap onto the system disk.

**Repairing a Codex agent in its own session** (rule 4): `tools/repair_t1.sh RUN NN` (a tier-1 chunk) and
`tools/repair_map.sh RUN S:A` (a verse map) send the checker's exact problems to the agent's session and print its
reply; run several with `xargs -P`. If a session is gone, rebuild the verse in a new run:
`map.py build NEWRUN --from luna-max --ayat … --models gpt-6-sol:high --supersede OLDRUN` (recorded in both
manifests; OLDRUN's check then prints `SUPERSEDED`). The command it wraps:
`codex exec resume --ignore-user-config -c model_reasoning_effort="<effort>" -c web_search="disabled" -c sandbox_mode="workspace-write" --skip-git-repo-check --json -o <runs/agent>/repairN.last.txt <thread_id> - < message`
from the repo root (the thread id is in `stream.jsonl`'s `thread.started` event; without the sandbox option the
session is read-only). Name the exact problems and allow reading and editing only its own output file.

## When something fails

| What happened | What to do |
|---|---|
| `codex_run.py` prints `started earlier without run.json` | an agent is running or died; check `ps` for its codex process; rerun with `--retry` only with the user's go |
| a map or translation `check` lists problems | report; repair through the same agent if it is still fresh, else rebuild that verse in a new run |
| `writer.py build` refuses: no verse map | finish stage 2 for the listed verses |
| a writer's `check` fails after its run | report the problems; do not resume it for fixes (rule 5): rebuild that page in a new writer run with the user's go |
| peak context over 120k (tier-1 report) | report; the output is valid if `check` passes |

## Production state (update this section at every stage; last: 2026-10-09 ~09:45, before a machine restart)

| Surah | Tier 1 | Maps | Translation | Pages | Rendered |
|---|---|---|---|---|---|
| 103 | done (`t1_s103_20261009` $2.34; 103:1 completion in S96's run) | done: `map_s103_20261009` (80), `map_s103w_20261009` (12), 100 updates ($8.46) | `tr_s103_20261009` (131 verses, 74 chunks): 51 of 74 chunks done; run the other 23 | 103:1 (test), 103:2, 103:3 done | md done; HTML: `surah.py finish 103` after the translations (103:1's HTML then re-rendered with the Turkish appendix) |
| 96 | done (`t1_s096_20261009`, $83.45 + $8.61 repairs) | done: `map_s096_20261009` (460; 4 superseded by `map_s096r_20261009`), 91 updates ($8.63); maps $162.36 | not built (`tr_s096_…`; build after S103's finishes) | 96:1–96:5 done (writers $18.14, meals $2.29); 96:6, 96:7 done; 96:8 writer done (check OK), its meal not run yet | md for 96:1–96:5 |
| 87 | `t1_s087_20261009`: **771 of 993 chunks done here** (69,582 rows so far); **222 chunks run on the user's other computer** (stage 1 handoff); 8 finished chunks need a same-session repair here (`tools/repair_t1.sh t1_s087_20261009 NN` for c325 c362 c497 c499 c656 c850 c894 c896; their sessions are in the archive) | — | — | — | — |

**Resume after the restart (in this order):**
1. `git pull`; `surah.py agents 96` (lists only agents not yet run).
2. Remaining S96 agents, **at most 3 Opus agents at a time**: meal 96:8 (then render 96:8 and commit it as a page),
   then writer + meal for 96:9–96:19. Check each with `tools/page_status.sh 96 N`, render, commit and push per page.
3. Turkish renderings `tr_s103_20261009`: `tools/rerun_failed_start.py`, then
   `tools/run_until_done.sh 20 enrichment/v9/work/tr_s103_20261009/maptr/runs <log> enrichment/v9/work/tr_s103_20261009/maptr/spawn/luna-max_c*.md`;
   `maptr.py check/report`; then `surah.py finish 103`.
4. Start the helpers again: `tools/session_archive.sh` (pid in `work/session_cleanup.pid`) and `tools/disk_throttle.sh` (see "Disk space" and "Disk throttle").
5. S87: repair the 8 chunks listed in the table here; when the other computer pushes the other 222,
   `digest.py check/report t1_s087_20261009`, repair any new problems, then maps etc.
6. 103:1 page (user, 2026-10-09): its maps gained notes after the page was written; if the new notes are significant
   (`map.py update` reports per verse), rebuild the 103:1 writer in a new run.
7. Bible (user, 2026-10-09): liked; some blocks share only keywords with the commentary. Before S96/S87 Bible runs
   (after their enrichment is complete), tighten the briefs so a block needs a substantive link beyond shared words.
