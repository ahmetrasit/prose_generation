# Production: how to orchestrate the commentary pipeline (from 2026-10-04)

For an agent or operator starting cold. This page says which workflows are current, in which order, what is
optional, and how a run happens. It holds no commands: the runbooks do.

## The two current workflows

- **Commentaries: v16 r13 with augment9** (`_commentary/v16/RUNBOOK.md`): the surah commentary and one ayah
  commentary per ayah, frozen as written, plus the hideable augment layer of Quran-explains-Quran additions.
- **Enrichment v2** (`enrichment/v2/RUNBOOK.md`), the follow-up workflow on the v16 outputs: one page per surah and
  per ayah for the advanced reader (tafsir, hadith, readings, lexicon, meals, antecedents) for the NGT project
  (next-generation tafsir). It never edits the v16 base.

Older workflows (`_commentary/v5/`, `_ayah_commentary/`, `_surah_commentary/`) are history, not production.

## The pipeline in one view

For each surah, in this order:

| Step | What it makes | Runbook | Optional? |
|---|---|---|---|
| 1. v16 map | the surah's image chains (working material) | `_commentary/v16/RUNBOOK.md`, Step 1 | no |
| 2. v16 image prose | the **surah commentary** (final as written) | same, Step 2 | no |
| 2b. surah-commentary augment | image-based discovery (Luna, Terra) then augment9 per image section | same, Step 2b | built, **waits for the user's confirmation to start** |
| 3. v16 readings | one **ayah commentary** per ayah (frozen baseline, brief r13) | same, Step 3 | no |
| 4. v16 augment (augment9) | Quran-explains-Quran additions under each ayah commentary's paragraphs | same, Step 4 | **yes**, resumable any time |
| 5. enrichment v2 | the advanced-reader pages (ayah pages need step 4) | `enrichment/v2/RUNBOOK.md` | **yes**, run surah by surah when NGT needs it |

Steps 1–3 are the reading itself and are never rerun or edited; everything after them builds around them.

## How a run happens (from 2026-10-04 evening)

No model call goes through a script. For every Claude call the scripts **build** the run (its `prompt.md`, a
`started.json` guard so it is never run twice, and a `spawn.md`), the orchestrating Claude session **spawns** the
agent itself with the Agent tool (type `v16-call` or `enrich-page`, the text of `spawn.md` as the prompt, seven at a
time for v16, two for enrichment), and the scripts **finish** it (status, check, ledger with the cost computed from
the agent's transcript, apply). The only script-run calls left are the GPT discovery agents of step 2b, through the
Codex subscription.

**Install once** (the user, not the orchestrator): the run guard hook in `.claude/settings.json` and the two agent
definitions in `.claude/agents/`; their exact contents are in `_commentary/v16/RUNBOOK.md`, "Install once". The
orchestrator checks they exist before its first spawn and stops if they do not.

## Which surahs get what

- **Own-reading surahs:** steps 1–3, then step 4 as intended; step 4 can also be added later per ayah.
- **NGT surahs:** steps 1–5. Step 4 on every ayah first, then one enrichment pack build, one ayah page to calibrate,
  then the rest, then the surah page.
- `python3 -B _commentary/v16/status.py N …` shows the v16 state of a surah; `python3 -B enrichment/v2/enrich.py
  status --surah N` the enrichment state. Both make no model calls.

## Rules that hold in both runbooks

1. **Each step needs its own go.** Tell the user what will run, how many calls and the estimate, then wait. A go
   for one step or surah covers nothing else.
2. **No agents and no background runs without a go.** Spawned agents run in the background; the request says so.
3. **Never rerun a call.** A directory with `started.json` or `run.log.json` is blocked; the scripts refuse it and
   no second agent is spawned for it. A failed call is renamed with the user's word and built anew.
4. **No silent failures.** Every WARNING, NOTE, BLOCKED, traceback and non-ok ledger row goes to the user, verbatim.
5. **Actual costs are always recorded** beside the estimate; seven agents at a time; commit and push after every
   completed step and every batch.
6. **Instruction files** (briefs, schema) are shown to the user before they change.
7. **The base is frozen.** Hand corrections to a reading go in a `corrections.json` beside it.

## Costs and billing

The calls run on a Claude Max subscription. Every dollar in the ledgers is nominal (the CLI's API-equivalent
figure, or, for a spawned agent, its transcript's tokens at the same rates), not cash; what binds is the plan's
session and weekly allowance (session limits were hit on 2026-10-01 and 2026-10-04). Nominal, Opus 5.5 high, per
ayah: steps 1–3 about $1.65; step 4 about $2.5 (measured on 20 ayat, $1.8–4.4 by list size); step 5 about $0.6
for the surah page plus an unmeasured $3–6 per ayah page. The runbooks carry the measured numbers.

## Where things are

- `_commentary/v16/RUNBOOK.md`: steps 1–4 and 2b, the install-once files, commands, statuses, failures, costs.
- `_commentary/v16/agentrun.py` (spawn and finish of agent runs), `hooks/guard.py` (the run guard),
  `discover.py` and `augment_surah.py` (step 2b), `batch.py` (dry estimates for a whole surah).
- `_commentary/v16/DESIGN.md`: the history and the reasons; `REVIEW_production.md`: the 2026-10-04 review, the
  four-arm augment test, the work list.
- `enrichment/v2/RUNBOOK.md` and `DESIGN.md`: step 5.
