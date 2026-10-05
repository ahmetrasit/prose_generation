# v16 production runbook (r13 + augment9): agent-spawned runs

For an agent, a Claude Code session, orchestrating one surah end to end:

**surah map → surah image prose (the surah commentary) → ayah readings → ayah augment**, then, only if the user
says so, **enrichment** (Step 5, its own runbook).

From 2026-10-04 evening **no model call goes through a script** (user: every model here is Claude, so the
orchestrator spawns the agents itself). The scripts **build** a run (its `prompt.md`, the `started.json` guard and a
`spawn.md`) and **finish** it (status, check, ledger, apply). The orchestrator spawns the model call with the Agent
tool and runs the finish step when the agent replies. The history and the reasons are in `DESIGN.md`; the review
that led here is `REVIEW_production.md`. This file holds only what is needed to run.

## Rules from the user (never break them)

1. **Each step needs its own go.** Before a step, tell the user what will run, how many calls and the estimate
   (the build prints it), then wait. A go for one step or one surah covers nothing else.
2. **No agents, and no background runs, without an explicit go.** The go names the step and the ayat; the spawned
   agents run in the background, and the request must have said so.
3. **Never rerun a call.** A run dir with `started.json` or `run.log.json` is blocked and the scripts refuse it; a
   dir with `started.json` is never given a second agent. A failed call: ask the user, then rename the dir to
   `<dir>.<reason>-<cost>usd` (as `augment.augment9.opus.session-limit-0usd`) and build a new run.
   - A safeguard stop whose output is whole (every paragraph served, every listed passage judged, `end_turn`) can
     be accepted with the user's go: `augment.py <run dir> --accept "<reason>"` (no call; `accepted.json` and a ledger
     row with `status accepted`). 1:4, 2026-10-04: accepted.
4. **No silent failures.** Report every `WARNING:`, `NOTE:` and `BLOCKED:` line the scripts print, every traceback,
   and every ledger row whose `status` is not `ok`/`accepted`, whose `check` is not `ok`, or that has a `post_error`.
   When a step's output is not clean, stop that surah and let the user decide.
5. **Augment runs on ayah readings only** (`augment.py` refuses a surah commentary); the surah commentary has its
   own step (2b below), not started without the user's confirmation.
6. **Seven agents at a time** (user, 2026-10-04): spawn at most seven runs in one message, finish them, report,
   commit, then the next seven.
7. **Actual costs are always recorded.** The finish step computes each run's cost from the agent's transcript
   (tokens × the CLI's rates, `agentrun.RATES`) and the ledger keeps it beside the estimate; report both.
8. **Commit and push after every completed step and every batch of seven:** `out/` yes, `work/` never.
9. **Instruction files** (briefs, schema) are shown to the user before they change.

## Setup

- **Paths.** Repo root `/Volumes/aro/projects/prose_generation`; run every command from there. The scripts
  resolve `out/…` against `_commentary/v16/`.
- **Sibling repos** in `/Volumes/aro/projects/`: `latent_activation/` (channel reviews), `dictionary/`,
  `root-dossier/`, `quran/` (qiraat), `quran-data/` (text, inter-ayah lists), `quran-slm/`.
- **Models.** Opus 5.5 at effort high for every v16 call; pinned by the agent definition below.
- **Ledger.** Every call appends a row to `out/ledger.jsonl` with its cost, `status` and `check`; the row is
  written even if anything after the call fails (`post_error`).
- **Call status** (`status` in the row): `ok` a clean output; `truncated` the model stopped for a reason other
  than the end of its turn; `suspect` more text before the last tool call than after it; `partial` no result;
  `safety-stop` the model's safeguards stopped it; `error` no output (the agent wrote nothing, or a session limit);
  `accepted` a non-ok output the user accepted (rule 3). A map, image prose or reading that is not clean is written
  as `*.partial.md`, never under the finished name; an augment that is not ok applies nothing (`augment.raw.partial.md`).
- **Check** (`check` in the row): `ok`, `findings` (counts in `check_findings`, printed: unverified sources, Arabic
  outside tags, unsourced quotes, process words) or `failed`. Findings do not stop the pipeline; report them. For an
  augment the check covers only the additions; the reading's own findings stay in `check_baseline`.
- **Status at any time** (no calls): `python3 -B _commentary/v16/status.py 87 100 103`: map and image prose state,
  readings n/N and augment9 n/N (finished files only), what is still to run, every partial or blocked run, check
  findings, and production ledger rows whose latest status is not ok. "Spent" is every ledger cost for the surah.

### Install once (the user does this; the orchestrator only checks)

Agent-spawned runs need two things in the repo's `.claude/` that the orchestrator must not create itself:

1. **The run guard**, a PreToolUse hook in `.claude/settings.json`. It runs `_commentary/v16/hooks/guard.py` on
   every tool call; inside a spawned run (a subagent whose first message starts with `v16-agent-run: <dir>`) it
   refuses anything but reading the run's `prompt.md`, running the lookup `python3 missing.py …` exactly as written,
   and writing the run's `response.md`; for enrichment runs it refuses reads of `enrichment/v2/out/` and other call
   directories, writes outside the call directory, and git. Outside such runs it does nothing.

   ```json
   {
     "hooks": {
       "PreToolUse": [
         {
           "matcher": "Bash|Read|Write|Edit|MultiEdit|NotebookEdit|Glob|Grep",
           "hooks": [
             { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/_commentary/v16/hooks/guard.py" }
           ]
         }
       ]
     }
   }
   ```

2. **Two agent definitions**, which pin the model and the effort and limit the tools.

   `.claude/agents/v16-call.md`:

   ```markdown
   ---
   name: v16-call
   description: One v16 production model call (surah map, surah image prose, ayah reading, ayah augment) spawned by the orchestrator from a built prompt.md; reads the prompt, runs only the lookup, writes response.md. Spawn it only with the text of a run's spawn.md.
   model: opus
   effort: high
   tools: Read, Bash, Write
   ---

   You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the user message
   exactly and return only the requested output.

   The user message names a run directory and its prompt.md: read that file once, do the work it describes, and
   write the complete output to the file the message names, in one write at the end. The only command you may run
   is the lookup the brief describes, exactly as written, as the whole command. Anything else is refused by a guard
   and spoils the run. Your reply in chat is one line.
   ```

   `.claude/agents/enrich-page.md`:

   ```markdown
   ---
   name: enrich-page
   description: One enrichment v2 page call (surah page or ayah page) spawned by the orchestrator from a built prompt.md; works inside its call directory and writes annotations.jsonl there. Spawn it only with the text of a call's spawn.md.
   model: opus
   effort: high
   tools: Read, Bash, Write, Edit, Glob, Grep
   ---

   The user message names a call directory and its prompt.md: read that file once and follow it exactly. Write only
   inside the call directory; never read enrichment/v2/out/ or another call directory, and never use git. A guard
   refuses such calls. Your reply in chat is one line when the records file is complete.
   ```

   Agent definitions are read when a session starts: after creating them, start a new session.

**Check before the first spawn of a session**, no calls:

```bash
ls .claude/agents/v16-call.md .claude/agents/enrich-page.md
python3 -c 'import json; print(json.load(open(".claude/settings.json"))["hooks"]["PreToolUse"][0]["hooks"][0]["command"])'
```

If either is missing, stop and tell the user: without the hook the guard is off, without the definitions the
model and the effort are not pinned. Do not spawn.

## How one run goes (the pattern for every step)

1. **Build** (no files under `out/`, no call): the step's command without `--spawn` prints the run dir, the prompt
   size and the estimate, and `BLOCKED:` for a dir that already ran.
2. **Report** the estimates and **wait for the go** (rules 1 and 2).
3. **Spawn.** The same command with `--spawn` writes `out/<run dir>/prompt.md`, `started.json` (the guard: the
   dir is blocked from now on) and `spawn.md`, and prints the agent type. Then, for each run, one Agent tool call:
   `subagent_type` as printed (`v16-call`), `prompt` = the exact text of that run's `spawn.md` (read it with the
   Read tool and pass it verbatim; its first line is the marker the guard and the finish step key on), `model`
   `opus`, a short `description` such as `87:12 augment9`. Up to seven Agent calls in one message. The agents run in
   the background; wait for their completion notices; do nothing in their dirs meanwhile.
4. **Finish** each run with the step's finish command. It reads the agent's `response.md`, finds the agent's
   transcript (`~/.claude/projects/*/*/subagents/`) for the cost, the commands and the stop reason, writes
   `run.log.json` and `tool_calls.json`, and then does exactly what the CLI path did after a call: status, partial
   naming, check, ledger, apply. Read everything it prints.
5. **Report** (rule 4 and 7), `status.py`, commit and push (rule 8).

- The agent's one-line reply ("written") is not the output; the file is. An agent that replies without writing
  the file, or writes a partial one, gives `status error`/`partial`: nothing is applied, the dir stays blocked, the
  user decides (rename, new build, new spawn).
- `WARNING: no subagent transcript names <dir>`: the output is finished, but the cost is `None` in the ledger.
  Report it; it happens when the transcript is not under `~/.claude/projects/` (another machine or account).
- A tool call the guard refused shows in `tool_calls.json` with `is_error`; the finish step prints it as a
  refused command. A run that ran a command outside the rule is reported as contaminated: the user decides.

## Step 1: surah map (1 call)

```bash
python3 -B _commentary/v16/packets.py map --surah N --no-hft --tool             # build: the estimate
python3 -B _commentary/v16/packets.py map --surah N --no-hft --tool --spawn     # after the go; then spawn the agent
python3 -B _commentary/v16/packets.py finish --run out/sNNN/surah.map3.nohft.tool   # after the agent replied
```

- Output: `out/sNNN/surah.map3.nohft.tool/map.md`. `--surah` is required.
- Surahs without a channel review (S108, S110, S113, S114) use HFT from the ayah bundles (user, 2026-10-03):
  `map --surah N --no-channels --hft-bundle --tool`; their dir is `surah.map3.nochannels.hftbundle.tool`, and that
  name replaces `map3.nohft.tool` in the steps below.

## Step 2: surah image prose (1 call)

```bash
python3 -B _commentary/v16/packets.py images --surah N --brief r13 --tool --map out/sNNN/surah.map3.nohft.tool/map.md
python3 -B _commentary/v16/packets.py images --surah N --brief r13 --tool --map out/sNNN/surah.map3.nohft.tool/map.md --spawn
python3 -B _commentary/v16/packets.py finish --run out/sNNN/images.r13.map3.nohft.tool.tool
```

- Output: `out/sNNN/images.r13.map3.nohft.tool.tool/images.md`, plus `ledger.md` and `check.json`. This is the
  surah commentary; it is final as written. Complete means at least one `## ` image section, `## Buluşmalar` and a
  ledger; anything else is `images.partial.md`, the finish exits non-zero, and no reading is built on it.
- An image section without a `Kaynaklar:` line is printed as a WARNING by `slices` and by the writer build.

## Step 2b (built, not started): the surah-commentary augment

Deferred on 2026-10-04 until a dedicated image-based step existed; it exists now and **waits for the user's
confirmation to start**. Two parts:

**Discovery** (`discover.py`): per image section of `images.md`, GPT agents find the ayat the image activates, as
the focus-ayah-100-card-review-v2 protocol did for every ayah in 2026-07 (quran-slm `inter-ayah/`: Terra reviewed a
package, then the fixed follow-up asked for the missing ayat). The package is the section's prose, its ayat, its
roots and the whole surah in Arabic; the brief is `prompts/discover/brief.md` (scene, root, theme, speaker,
contrast, neighbour; four-field TSV). Two models per section, Luna max and Terra max, two turns each in one Codex
session. These are the only script-run calls left: GPT is not Claude, so `codex exec` runs them.

```bash
python3 -B _commentary/v16/discover.py --surah N                    # packages and prompts, no call (S87: 18 sections)
python3 -B _commentary/v16/discover.py --surah N --go               # every section x luna, terra; --parallel 2
python3 -B _commentary/v16/discover.py --surah N --merge            # sec<k>.merged.tsv: one tiered list per section
python3 -B _commentary/v16/discover.py --surah N --status
```

- Output: `out/sNNN/discovery/sec<k>/<model>/` (`package.md`, `prompt.md`, `list.tsv` as the agent wrote it,
  streams, `run.log.json`; blocked by `started.json`) and `out/sNNN/discovery/sec<k>.merged.tsv` (tier = the best
  label either model gave; the follow-up turn's rows marked). Rows outside the schema are kept in `list.tsv`,
  printed, and left out of the merge. Codex runs are on the subscription: the ledger row carries tokens, cost 0.
- `gpt-6-terra` is the assumed id for Terra (by analogy with `gpt-6-luna`); the first run shows whether it exists.

**Augment** (`augment_surah.py`): augment9's verdict pass over one section at a time, seeded by the section's merged
list (brief `prompts/augment9s/augment.md`: same output, paragraph numbers as in the whole commentary, only the
section's paragraphs may be served), agent-spawned like every Claude call; then one merge into `images.md`.

```bash
python3 -B _commentary/v16/augment_surah.py --surah N --status
python3 -B _commentary/v16/augment_surah.py --surah N --section k            # build: the estimate
python3 -B _commentary/v16/augment_surah.py --surah N --section k --spawn    # then spawn v16-call with spawn.md
python3 -B _commentary/v16/augment_surah.py --surah N --section k --finish
python3 -B _commentary/v16/augment_surah.py --surah N --merge                # images.md with every finished section
```

- Output: `out/sNNN/augment.augment9s.opus/sec<k>/` and `out/sNNN/augment.augment9s.opus/images.md` (marked
  blocks as in the ayah augment; `strip_augment` gives the original back). Ledger arms `augment-surah` and
  `augment-surah-applied`, ref `S<N>`.
- Order once it runs: after Step 2, before Step 3, so the ayah writers read the augmented surah commentary
  (the writer's `--images` then points at `augment.augment9s.opus/images.md`; not wired until the first merge has
  been judged). Readings written before it predate it; `DESIGN.md` records which.

## Step 3: ayah readings (one call per ayah)

First, no call: every ayah must have image sections to read.

```bash
python3 -B _commentary/v16/packets.py slices --surah N --images out/sNNN/images.r13.map3.nohft.tool.tool/images.md
```

- An ayah without sections stops its writer build. Report it; never work around it. The choices are an explicit
  alias in `packets.SLICE_ALIAS` (as `94:6 → 94:5`), the full images, or no reading.

Then one run per ayah, seven at a time:

```bash
python3 -B _commentary/v16/batch.py --surah N --step writer                 # dry: one build per ayah without a reading, the estimates
python3 -B _commentary/v16/packets.py writer --ayah N:A --brief r13 --tool \
    --map out/sNNN/surah.map3.nohft.tool/map.md \
    --images out/sNNN/images.r13.map3.nohft.tool.tool/images.md --spawn       # after the go, per ayah; then spawn
python3 -B _commentary/v16/packets.py finish --run out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool
```

- Output: `out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool/N_A.reading.tr.md`, plus `check.json` and
  `ledger.md`. A build that prints `BLOCKED:` has already run and is never repeated.

## Step 4: ayah augment (one call per ayah)

Production since 2026-10-04: brief `augment9`, Opus 5.5 high (the script defaults): augment8 plus the exhaustive
own-knowledge pass (`REVIEW_production.md` §9). Only after the ayah's reading has finished.

```bash
python3 -B _commentary/v16/batch.py --surah N                               # dry: every ayah with a reading and no augment9, the estimates
python3 -B _commentary/v16/augment.py out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool --spawn    # after the go; then spawn
python3 -B _commentary/v16/augment.py out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool --finish
```

- Output in `…/augment.augment9.opus/`: `N_A.reading.tr.md` (the reading with the additions as marked blocks
  `<!-- v16:augment brief=augment9 model=opus para=n kind=prose|refs … -->`; `augment.strip_augment()` gives the
  reading back byte for byte), `additions.md`, `verdicts.md`, `verdict_report.json`, `insertions.json`, `check.json`.
- **Hand corrections to a reading** go in `corrections.json` beside it (`file`, `old`, `new`, `why`; `old` occurs
  exactly once); the reading stays as written, the build applies them and prints a NOTE each. 87:6 has one.
- **The estimate** scales with the list: about 15k + 330 output tokens per listed passage, twice the prompt for
  input because of the lookups. Actual: $1.8–4.4 by list size, mean $2.5 (20 ayat, 2026-10-04).
- **Every warning goes to the user:** listed passages without a verdict; verdict lines not understood; a missing
  `=== VERDICTS ===` line; blocks after the verdicts; a ref that is not a verse; verdict mismatches; additions with
  no verdict; lookups with no verdict; consecutive ayat split into separate references; a missing list file or
  ledger; check findings inside the additions; refused commands.
- The ledger has two rows per call: `augment` (the cost) and `augment-applied` (the counts).

## The old way (not for new runs)

`--go` on `packets.py` and `augment.py`, and `batch.py --go`, run the call through the `claude` CLI in a
script. They stay for history and for reading old runs; the S87 augment9 batch of 2026-10-04 evening was the last
run through them. `batch.py` without `--go` is still the dry estimate for a whole surah (`--step writer` or the
default augment).

## After each step

1. Read every line the finish steps printed; check the ledger rows (`status`, `check`, `post_error`).
2. `python3 -B _commentary/v16/status.py N`.
3. Report the actual cost against the estimate, per run and in total, and every warning.
4. Commit the new `out/` dirs (never `work/`), push.
5. After a surah's augments, ask the user whether to run the enrichment for it (Step 5).

## Cost reference (Opus 5.5 high, actual; nominal dollars on the Max subscription)

| Step | S87 (19 ayat) | S100 (11 ayat) | Per call |
|---|---|---|---|
| Map | $4.19 | $1.64 | $1.6–4.3; a large surah is estimated up to $6.3 (S96) |
| Image prose | $4.27 | $2.73 | $2.0–4.3 |
| Readings | $21.65 | $12.06 | ~$1.1 (0.7–1.4 × estimate) |
| Augment9 (2026-10-04) | $15.15 for 87:1–6, the rest in the second batch | S1: $21.96 for 7 (1:4 $4.31 accepted) | $1.8–4.4 by list size, mean $2.5 for 20 ok calls, 0.73–1.28 × estimate; five 429s cost $3.96 for nothing |
| Surah-commentary augment (2b) | not run | – | build estimate ~$0.9 per section at 54 passages; discovery on the Codex subscription |

For an agent-spawned run the cost is computed from the transcript's tokens at `agentrun.RATES` (Opus input $8,
1h cache write $8.15 and cache read $0.17 fitted from 122 CLI runs, output $20 per MTok); it is comparable with the
CLI's figure to within about $0.7 per run, never cash.

## Where things stand (2026-10-04 evening)

| Surah | Map | Image prose | Readings | Augment9 |
|---|---|---|---|---|
| S1 | ✓ | ✓ | 7/7 | 7/7 (1:4 accepted after a safeguard stop) |
| S87 | ✓ | ✓ | 19/19 | 19 in progress: 87:1–14 done, 87:15–19 running in the last CLI batch |
| S100 | ✓ | ✓ | 11/11 | 0/11 |
| S103 | – | – | 0/3 | – |
| S107 | ✓ | ✓ | 7/7 | 0/7 |
| S88–S95 | ✓ | ✓ | 0 | – |
| S96–S114, apart from S100, S103, S107 | – | – | – | – |

- Older augments (augment2, augment3, augment8 and the 87:8 test arms) are superseded and stay on disk.
- Readings with check findings (Arabic outside tags, process words) are listed by `status.py`; fixing them is the
  user's call. `status.py` is the live view; this table is a snapshot.

## Step 5 (optional): enrichment

After a surah's ayat are read and augmented: one page per surah and per ayah for the advanced reader, a separate
pipeline with its own runbook, `enrichment/v2/RUNBOOK.md`. Ask the user; the go for v16 does not cover it. It reads
the surah image prose (never augmented, until Step 2b exists) and each ayah's reading after augment9
(`…/augment.augment9.opus/N_A.reading.tr.md`); an ayah without augment9 gets no ayah page; the v16 outputs are
frozen for it. Its pack is rebuilt after augment9 has run.

**The order for each surah: map → image prose → (2b, once confirmed) → readings → augment9 on the ayat → (ask) enrichment.**
