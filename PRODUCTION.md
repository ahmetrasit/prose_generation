# Production: how to orchestrate the commentary pipeline (from 2026-10-04)

For an agent or operator starting cold. This page says which runbook to follow for what, in which order, and
what is optional. It holds no commands: the runbooks do.

## The pipeline in one view

For each surah, in this order:

| Step | What it makes | Runbook | Optional? |
|---|---|---|---|
| 1. v16 map | the surah's image chains (working material) | `_commentary/v16/RUNBOOK.md`, Step 1 | no |
| 2. v16 image prose | the **surah commentary** (final as written) | same, Step 2 | no |
| 3. v16 readings | one **ayah commentary** per ayah (frozen baseline, brief r13) | same, Step 3 | no |
| 4. v16 augment (augment9) | Quran-explains-Quran additions under each ayah commentary's paragraphs | same, Step 4 | **yes**, resumable any time |
| 5. enrichment v2 | one page per surah and per ayah for the advanced reader: tafsir, hadith, readings, lexicon, meals, antecedents | `enrichment/v2/RUNBOOK.md` | **yes**, needs step 4 on the ayat |

Steps 1–3 are the reading itself: the surah commentary and the ayah commentaries. They are never rerun and
never edited; everything after them builds around them.

Step 4 adds a hideable layer of cross-references, judged passage by passage. It reads only the frozen reading and
the cross-reference lists, so it can run today or a year later with the same result. An ayah without it has no
enrichment page.

Step 5 is for the NGT (next-generation tafsir) project. It is run surah by surah when that project needs the
surah, never as part of a reading run.

Planned, not built (see `_commentary/v16/REVIEW_production.md`, §3–4 and §7): an augment on the surah commentary,
one call per image section, run between steps 2 and 3; and the enrichment ayah pages before the surah page.
Until it exists, the order above stands.

## Which surahs get what

- **Own-reading surahs:** steps 1–3, and step 4 when the budget allows. Step 4 can be added later per ayah.
- **NGT surahs:** steps 1–5. Step 4 on every ayah first, then one enrichment pack build, then the enrichment pages.
- `python3 -B _commentary/v16/status.py N …` shows the v16 state of a surah; `python3 -B enrichment/v2/enrich.py
  status --surah N` the enrichment state. Both make no model calls.

## Rules that hold in both runbooks

1. **Each step needs its own go.** Tell the user what will run, how many calls and the estimate, then wait. A go
   for one step or surah covers nothing else.
2. **No agents and no background runs without a go.** Say whether a run is foreground or background when asking.
3. **Never rerun a call.** A directory with `started.json` or `run.log.json` is blocked; the scripts refuse it.
4. **No silent failures.** Every WARNING, NOTE, BLOCKED, traceback and non-ok ledger row goes to the user, verbatim.
5. **Commit and push after every completed step.** `out/` yes, `work/` never.
6. **Instruction files** (briefs, schema) are shown to the user before they change.
7. **The base is frozen.** Hand corrections to a reading go in a `corrections.json` beside it; the file stays as
   written and the scripts apply the corrections when they read it.

## Costs and billing

The `claude` CLI runs on a Claude Max subscription. Every dollar in the ledgers is the CLI's nominal
API-equivalent cost, not cash; what binds is the plan's session and weekly allowance. Nominal, Opus 5.5 high, per
ayah: steps 1–3 about $1.65; step 4 about $1.9; step 5 about $0.6 for the surah page plus an unmeasured $3–6 per
ayah page. The runbooks carry the measured numbers.

## Where things are

- `_commentary/v16/RUNBOOK.md`: steps 1–4, commands, statuses, failures, cost reference.
- `_commentary/v16/DESIGN.md`: the history and the reasons; `REVIEW_production.md`: the 2026-10-04 review,
  the four-arm augment test, the agreed work list.
- `enrichment/v2/RUNBOOK.md` and `DESIGN.md`: step 5.
- Older workflows (`_commentary/v5/`, `_ayah_commentary/`, `_surah_commentary/`) are history, not production.
