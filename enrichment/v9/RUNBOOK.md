# Enrichment v9 runbook: one surah, from tier 1 to the enriched pages

For a cold orchestrator in a **Claude Code** session, at the repo root `/Volumes/aro/projects/prose_generation`.
Design and decisions: `PLAN.md` (read its "Decisions" section first). Test standard: `T0-103_1.md`. Tier-1 details:
`enrichment/v7/RUNBOOK.md` (stage 1 only).

## Rules

1. **Scope and quota come from the user.** Before a surah, report the plan's expected cost (`surah.py plan`) and
   use the quota the user gave: Luna up to 50 agents at a time, Sol and Opus as the user allows (2026-10-09:
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
  `python3 -B enrichment/v9/codex_run.py --parallel N <spawn files>` (N = the user's cap; Luna 50). Run it in the
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
Spawn one `enrich-page-high` agent per block in `agents.md`. Each writer runs its own check and final pass.

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
run check `df -h /` (keep > 3 GB free). The user allowed deleting `~/.codex/sessions`; delete only files not modified
for 10 minutes (a running agent keeps writing its file; a finished one's cost is already in its run.json). A cleanup
loop does this every 5 minutes
(pid in `work/session_cleanup.pid`). Agents that failed at start are moved to `<runs>_enospc/` (evidence kept) and
the same spawn files are run again; never move an agent that ran commands.

**Repairing a Codex agent in its own session** (rule 4):
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

## Production state (update this section at every stage; last: 2026-10-09)

| Surah | Plan | Tier 1 | Maps | Translation | Pages | Rendered |
|---|---|---|---|---|---|---|
| 103 (page 103:1) | test (`w103_1-20261008`, `meal103_1-r2-20261009`) | done | done (`maptest-20261008`, `map-103_1-20261008`) | not yet | done; published privately (https://claude.ai/artifact/TnbnSk6SvZYrQSKWZBaDXs) | done |
| 96 | `work/prod_s096` (19 pages, 475 verses) | `t1_s096_20261009`: done, 133,220 rows, $83.45 + $8.61 same-session repairs (17 chunks) | `map_s096_20261009`: 460 verses, Sol running (relaunched after the disk incident; logs `work/map_s096_20261009.run*.log`) | — | — | — |
| 103 (pages 103:2, 103:3) | `work/prod_s103` (95 verses) | `t1_s103_20261009`: done, 52 chunks, 3,674 rows, $2.34 (c32 repaired in its own session) | `map_s103_20261009`: 80 verses (`verses_now.txt`) done, all OK, $27.66; 15 verses (`verses_wait_s096.txt`) wait for S96's tier 1, then map them and run `update-all` | not yet: run after S96's tier 1 (Luna cap is shared) | — | — |
| 87 | `work/prod_s087` (19 pages, 443 verses) | `t1_s087_20261009`: 993 chunks, **running** (relaunched after the disk incident; logs `work/t1_s087.run*.log`) | — | — | — | — |

The S96 tier-1 run also holds the 103:1 completion (103:3, the short editions now kept, the 37 excerpt-only
segments); after its maps stage, `map.py update-all` brings the 103:1 page's maps up to date. The 103:1 page itself is
not rewritten (no second analysis).

Order (user, 2026-10-09): S103 pages 103:2–3 first (start their maps as soon as the 52 S103 chunks are checked, without
waiting for S96), S96 tier 1 continues in the background, then S96, then S87.

Next, in order: when `codex_run.py` exits (log ends, no `codex exec` processes), run `digest.py check` and `report`
for both tier-1 runs; then stage 2 for S103 (pages 103:2–3) and S96 (`map.py build` per surah, then `update-all`),
Sol at the user's cap; then stage 3, stage 4 (`surah.py pages/agents`), stage 5; commit and push after each stage.

Parallel task (user, 2026-10-09): complete the Bible enrichment workflow (`enrichment/bible/`) and run it on S103,
using Hebrew/Semitic root and cognate evidence, anchored to the frozen paragraphs. It is independent of this pathway.
