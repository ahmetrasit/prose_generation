# Enrichment v7 runbook: tier 1 → tier 2 → page writer

For the orchestrator, a Codex session (tiers 1 and 2, Astra writers) or a Claude Code session (Opus writers). Design
and reasons: `PLAN.md`. Run every command from the repo root `/Volumes/aro/projects/prose_generation`.

## Rules

1. **Each stage needs the user's go.** Report the build's numbers first: agents, characters, estimate.
2. **The orchestrator spawns the agents itself.** Scripts only build inputs and spawn files, check and report.
   - Do **not** use `run.sh` / `run_codex.py` for these runs. They are the scripted fallback, seven at a time.
   - **Parallelism:** up to **60 tier-1 agents at a time** (user, 2026-10-07). Keep the cap filled as agents finish;
     do not wait for a wave to finish before spawning more.
3. **Do not start a second session for an agent.** A completed agent releases its active slot. If it reports an
   error, send a repair request to that same agent when a slot is available. Report failures to the user.
   Missing work that cannot be repaired is rebuilt as a **new run** (see "When something fails").
4. **No silent failures.** Pass every `WARNING`, `NOTE` and `SKIPPED` line the scripts print to the user, verbatim.
5. **No interim commits or pushes during tier 1.** The orchestrator monitors active agent count, handles reported
   repairs and keeps the 60-agent cap filled. Commit and push after the stage is complete.

## How to spawn one agent (every stage)

Each spawn file is a complete prompt. Its first line is the header:

```
<!-- agent /root/v7d_s103-1_luna-max_c01 | model gpt-6-luna | effort max -->
```

For each spawn file, spawn one native agent with:

- **Name:** use the header's `agent` value when the native spawn tool accepts it. The native tool used for this run
  allows only lowercase letters, digits and underscores in task names, so replace each hyphen in the name after
  `/root/` with an underscore (here `v7d_s103_1_luna_max_c01`). Keep the spawn file text, including its header,
  unchanged. The report looks up both the header name and this underscore-only native alias for session costs.
- **Model and effort:** exactly as in the header.
- **Context:** fresh, with no inherited turn history.
- **Prompt:** for this run, pass the spawn file path and direct the agent to read it once in full, then follow its
  contents exactly. This is the approved native-tool workaround for the 3.43 million characters of spawn prompts;
  the file itself remains unchanged. If its checker finds errors, the agent may reread only its assigned chunk parts
  and use local commands to read and edit only its own output file for the repair, despite the spawn file's command
  list. Keep the source segment body and its header preview distinct when choosing verbatim anchors.

The agent reads its parts with `cat`, writes one output file, and runs the stage's check command until it prints
`OK`. The orchestrator tracks session completion and immediately tops up under the concurrency cap; it does not
inspect individual output files during the run.

## Stage 1: tier 1, per source segment (Luna max)

```bash
python3 -B enrichment/v7/digest.py build s103-1 --page _commentary/v16/out/103_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/augment.augment9.opus/103_1.reading.tr.md --ayah 103:1 --models gpt-6-luna:max --skip-done luna-max
```

- **What it covers:** every source segment tied to 103:1 and to every verse its page cites.
- **What it skips** (each skip listed in `work/s103-1/manifest.json`):
  - segments already digested in any earlier run;
  - short editions where a FULL edition covers the verse;
  - meal, translations and the Quran text.
- **Spawn files:** `enrichment/v7/work/s103-1/spawn/luna-max_c*.md`. Keep up to 60 running at a time.
- **Outputs:** `work/s103-1/out/luna-max/c*.jsonl`.

After all of them finish:

```bash
python3 -B enrichment/v7/digest.py check s103-1      # every segment answered, every anchor verbatim
python3 -B enrichment/v7/digest.py report s103-1     # cost per run, completion, peak context (cap 120k)
```

## Stage 2: tier 2, per verse (Sol high); only after stage 1 is complete

```bash
python3 -B enrichment/v7/merge.py build s103-1 --from luna-max --page <same page> --ayah 103:1 --models gpt-6-sol:high
```

- **Skips:** verses that already have tier 2 (`SKIPPED`). A verse with no tier-1 notes gets an empty view list and
  no agent (`NOTE`).
- **Spawn files:** `work/s103-1/tier2/spawn/sol-high_*.md`, one per verse. Spawn them the same way.
- **Outputs:** `work/s103-1/tier2/out/sol-high/<s>-<a>.jsonl`.

After all of them finish:

```bash
python3 -B enrichment/v7/merge.py check s103-1       # every tier-1 row in at least one view; writes the readable .md
python3 -B enrichment/v7/merge.py report s103-1
```

## Stage 3: page writer (Opus high and/or Astra high); only after stage 2 is complete

```bash
python3 -B enrichment/v7/write.py build s103-1 --ayah 103:1 --page <same page> --views sol-high --rows luna-max --models claude-opus-5-5:high gpt-6-astra:high
```

- **Missing tier 2:** if any cited verse lacks it, the build stops and lists them.
- **Groups:** it prints the paragraph groups.
- **Astra (Codex session):** spawn `work/s103-1/write/spawn/astra-high_g*.md` the same way.
- **Opus (Claude Code session):** for each group, spawn agent type `enrich-page-high` with the exact text of
  `work/s103-1/write/opus-high/gNN/spawn.md`.

After all of them finish:

```bash
python3 -B enrichment/v7/write.py check s103-1 --model astra-high   # and --model opus-high
python3 -B enrichment/v7/write.py render s103-1 --model astra-high  # page + views/ files; strip check
python3 -B enrichment/v7/write.py report s103-1
```

The rendered page is `work/s103-1/write/render/<tag>/103_1.enriched.tr.md`.

## When something fails

| What happened | What to do |
|---|---|
| An agent did not finish (`report` WARNING), or wrote no file (`check`: no output file) | Report it to the user. Ask the same agent to repair its work if possible; do not create a second session with its name. If still missing, with the user's go build a new run with `--skip-done`: it picks up exactly the segments that have no output line anywhere. |
| `check` lists anchor or field problems in a finished file | Report them and ask that same agent to repair them. |
| Peak context over 120k (`report` WARNING) | Report it. The output is still valid if `check` passes. |
| Two tier-2 files for one verse (`merge.load` error) | Two runs consolidated the same verse. Stop and ask the user which one stays. |

## Run names

One run per scope, for example `s103-1` for the 103:1 page. Earlier runs:

| Run | What it holds |
|---|---|
| `test-20261007` | 100:1 and 87:6 own material; tier 2 for both verses |
| `pilot100-20261007` | 100:1 page's cited verses; built, **not run; do not run it** (superseded: later runs digest those segments with `--skip-done`) |

`--skip-done` makes later runs skip whatever earlier runs digested.
