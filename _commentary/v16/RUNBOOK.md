# v16 production runbook (r13 + augment9)

For an agent starting cold. It covers one surah end to end:

**surah map → surah image prose (the surah commentary) → ayah readings → ayah augment**, then, only if the user
says so, **enrichment** (Step 5, its own runbook).

The history and the reasons behind each choice are in `DESIGN.md`. This file holds only what is needed to run.

## Rules from the user (never break them)

1. **Each step needs its own go.**
   - Before a step starts, tell the user what it will run, how many calls, and the expected cost (the scripts print an estimate).
   - Then wait for an explicit go. A go for one step or one surah does not cover the next.
2. **No agents, and no background runs, without an explicit go.** That includes subagents, Workflow and `run_in_background`. Say in the request whether a run will be in the foreground or the background; a go for a run covers the background only when the request said so.
3. **Never rerun a call.**
   - A run dir with `started.json` or `run.log.json` is blocked, and the scripts refuse it.
   - If a call failed (for example it hit the session limit at $0), ask the user first. Then rename the dir to `<dir>.<reason>-<cost>usd`, as in `augment.augment3.session-limit-0usd`, and run it again.
   - A safeguard stop (`status safety-stop`: the model's safeguards stopped the first attempt and the CLI continued once)
     leaves its output in `augment.raw.partial.md`, unapplied. Show the user whether it is whole: every paragraph served,
     every listed passage with a verdict, `stop_reason end_turn`. With their go, `python3 -B _commentary/v16/augment.py
     <run dir> --accept "<reason>"` applies it without a call and records the reason in `accepted.json` and in a ledger
     row with `status accepted` (cost 0; the call's cost was recorded when it ran). Otherwise rename and rerun as above.
     (1:4, 2026-10-04: $4.31, 27/27 paragraphs, 319/319 listed, accepted.)
4. **No silent failures.**
   - Report every `WARNING:`, `NOTE:` and `BLOCKED:` line the scripts print, and every traceback.
   - Report every ledger row whose `status` is not `ok`, whose `check` is not `ok`, or that has a `post_error`.
   - Do not summarize them away. When a step's output is not clean, stop that surah and let the user decide.
5. **Augment runs on ayah readings only, never on the surah commentary.** `augment.py` refuses a surah commentary.

## Setup

- **Paths.**
  - Repo root: `/Volumes/aro/projects/prose_generation`. Run every command below from there.
  - The scripts resolve `out/…` paths against `_commentary/v16/`.
- **Outside the repo.** These sibling repos sit in `/Volumes/aro/projects/`:
  - `latent_activation/`, the channel reviews;
  - `dictionary/` and `root-dossier/`;
  - `quran/`, for qiraat;
  - `quran-data/`;
  - `quran-slm/`.
- **Claude CLI.** Opus 5.5 at high effort through the `claude` CLI (`v16.call_opus`).
- **Ledger.** Every paid call appends a row to `_commentary/v16/out/ledger.jsonl`, with its cost, `status` and
  `check`. The row is written even if anything after the call fails; the failure is then in `post_error`.
- **Call status** (`status` in the row):

  | Status | Meaning |
  |---|---|
  | `ok` | a clean output |
  | `truncated` | the CLI exited non-zero, or the model stopped for a reason other than the end of its turn |
  | `suspect` | the text before the last tool call is longer than the text after it, so the output may be the earlier text (see `run.stream.jsonl`) |
  | `partial` | the stream ended without a result |
  | `safety-stop` | the model's safeguards stopped it |
  | `error` | no result, or an API error such as the session limit |

  - A map, image prose or reading that is not clean is written as `*.partial.md`, never under the finished name, so nothing downstream uses it. The same goes for an output with no `=== LEDGER ===` line, and for an incomplete map or image prose.
  - An augment that is not ok applies nothing; its text is in `augment.raw.partial.md`.
  - Not yet seen in a real run: the CLI's exit code when a command was refused. If a run whose output looks complete comes back `truncated` only because "the CLI exited with 1", stop and tell the user before anything else runs.
- **Check** (`check` in the row):

  | Value | Meaning |
  |---|---|
  | `ok` | check.py ran and found nothing |
  | `findings` | the counts are in `check_findings` and were printed: unverified sources, Arabic outside tags, unsourced quotes, process words |
  | `failed` | check.py itself failed |

  - Findings do not stop the pipeline; report them.
  - For an augment, `check` covers only the additions (`WARNING: in an addition, …`). The reading's own findings, already reported with the reading, are kept in `check_baseline`.
- **Status at any time** (no calls):

```bash
python3 -B _commentary/v16/status.py 87 100 103
```

It shows:
- whether the map and the image prose are `done`, `incomplete`, `partial`, `BLOCKED` or `-` (not started);
- readings n/N and augment9 n/N, counting only finished, complete files;
- what is still to run;
- every partial or blocked run, for the user to decide;
- check findings per reading, per augment and for the image prose;
- production ledger rows whose latest status is not ok.

"Spent" is every ledger cost for the surah, including errors and earlier trials.

## Step 1: surah map (1 call)

```bash
python3 -B _commentary/v16/packets.py map --surah N --no-hft --tool          # prints the estimate; add --go to run
```

- Output: `out/sNNN/surah.map3.nohft.tool/map.md`. `--surah` is required.
- The map3 brief forbids tools, and the `--tool` header asks for the check. From 2026-10-04 the packet adapts that one line (`packets.TOOL_BRIEF`). Maps built before (S1, S87–S95, S100, S107) had both lines, and their models ran the check.
- Surahs without a channel review (S108, S110, S113, S114) use HFT from the ayah bundles instead (user decision, 2026-10-03):

```bash
python3 -B _commentary/v16/packets.py map --surah N --no-channels --hft-bundle --tool
```

  Their output goes to `out/sNNN/surah.map3.nochannels.hftbundle.tool/`. In the steps below, use that dir name in place of `surah.map3.nohft.tool` / `map3.nohft.tool`.

## Step 2: surah image prose (1 call)

```bash
python3 -B _commentary/v16/packets.py images --surah N --brief r13 --tool \
    --map out/sNNN/surah.map3.nohft.tool/map.md                              # add --go to run
```

- Output: `out/sNNN/images.r13.map3.nohft.tool.tool/images.md`, plus `ledger.md` and `check.json`.
- This is the surah commentary. It is final as written: no augment.
- Complete means at least one `## ` image section, `## Buluşmalar` and a ledger. Anything else is written as `images.partial.md`, the call exits non-zero, and no reading can be built on it. Report it; the user decides.
- An image section without a `Kaynaklar:` line is printed as a WARNING by `slices` and by the writer build.

## Step 3: ayah readings (one call per ayah)

First, check that every ayah has image sections to read. This makes no call:

```bash
python3 -B _commentary/v16/packets.py slices --surah N --images out/sNNN/images.r13.map3.nohft.tool.tool/images.md
```

- An ayah without sections stops its writer build. Report it to the user; never work around it.
- Choices for such an ayah: an explicit alias in `packets.SLICE_ALIAS` (as for `94:6 → 94:5`), the full images, or no reading.

Then one writer per ayah:

```bash
python3 -B _commentary/v16/packets.py writer --ayah N:A --brief r13 --tool \
    --map out/sNNN/surah.map3.nohft.tool/map.md \
    --images out/sNNN/images.r13.map3.nohft.tool.tool/images.md              # add --go to run
```

- Output: `out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool/N_A.reading.tr.md`, plus `check.json` and `ledger.md`.
- Seven calls at a time (`batch.py --parallel 7`; user, 2026-10-04).
- Run the builds without `--go` first. Sum the estimates and give the total to the user. Leave out any build that prints `BLOCKED:`; that call has already run and is never repeated.

## Step 4: ayah augment (one call per ayah)

Production since 2026-10-04: brief `augment9` with Opus 5.5 high. These are the script defaults. augment9 is augment8 plus an exhaustive own-knowledge pass (the four-arm test on 87:8, `REVIEW_production.md` §9); the 87:8 augment8 run and the test arms (`augment.augment8.*`, `augment.augment8m.*`) are superseded and stay on disk.

```bash
python3 -B _commentary/v16/augment.py out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool   # estimate; --go to run
```

- **Output** goes to `…/augment.augment9.opus/`:
  - `N_A.reading.tr.md`: the reading with the additions;
  - `additions.md`;
  - `verdicts.md`;
  - `verdict_report.json`;
  - `insertions.json`;
  - `check.json`.
- **Additions** are marked blocks after their paragraph: `<!-- v16:augment brief=augment9 model=opus para=n kind=prose|refs … -->`. `augment.strip_augment()` removes them and gives back the reading byte for byte (asserted).
- **Run it only after the ayah's reading has finished.** Seven calls at a time, through `batch.py`.
- **Hand corrections to a reading** go in `corrections.json` beside the reading (`file`, `old`, `new`, `why`; `old` must occur exactly once). The reading file stays as written; augment.py applies the corrections before it reads and merges, prints a NOTE for each, and records the count in `packet.json`. 87:6 has one (19:22 → 19:23).
- **The estimate** scales with the list: about 15k + 330 output tokens per listed passage, and twice the prompt for input because of the lookups. 87:8 (123 passages) estimates $1.63 against $1.64 actual; 256 passages comes to about $2.8.
- **Every warning goes to the user.** The ones to expect:
  - listed passages without a verdict;
  - verdict lines the parser could not read (each printed);
  - a missing `=== VERDICTS ===` line;
  - blocks after the verdicts;
  - a ref that is not a verse;
  - verdict mismatches;
  - additions with no verdict;
  - lookups with no verdict;
  - consecutive ayat split into separate references;
  - a missing list file or ledger;
  - check findings inside the additions;
  - refused commands, which never ran.
- The ledger has two rows per call: `augment` (the cost) and `augment-applied` (the counts).

## Running several calls

Build first, then report the estimates and wait for the go. Then launch with `batch.py`: **seven calls at a time**
(user, 2026-10-04), one log per call, the queue stopped on a session limit or an API error, every WARNING, NOTE and
BLOCKED line printed again at the end, and **every call's actual cost against its estimate** (user: always record
actual costs), with a summary file in `work/logs/batch.<brief>.<model>.<time>.json`:

```bash
python3 -B _commentary/v16/batch.py --surah 87 --parallel 7            # dry: estimates, skips, BLOCKED; no call
python3 -B _commentary/v16/batch.py --surah 87 --parallel 7 --go \
    > _commentary/v16/work/logs/batch.s87.augment9.log 2>&1            # the go covers this background run
python3 -B _commentary/v16/batch.py 1:1 1:2 1:3 --parallel 7 --go     # or named ayat; several --surah may be given
```

- `--surah N` queues every ayah whose reading is finished and whose `augment.augment9.opus` does not exist, and
  prints a NOTE for each one it skips.
- A call that fails stops nothing else that is already running; a session limit or an API error stops the queue
  (the not-started ayat are listed; the failed dir is blocked and needs a rename before a new try).
- Read the batch log in full at the end; the ledger (`out/ledger.jsonl`) holds each call's rows.
- **Commit and push after each batch** (user, 2026-10-04): the new `augment.*` dirs and the ledger, never `work/`.
- Do not use `xargs -I{}` with a long command: it refuses it ("command line cannot be assembled, too long") and
  nothing runs (2026-10-04).

## After each step

1. Check the ledger rows: `status`, `check` (`ok`, `findings` or `failed`), and any `post_error`.
2. Run `status.py` again.
3. Report the actual cost against the estimate, per call and in total, and every warning, to the user. Actual costs are always recorded: the ledger has every call, `batch.py` writes a summary per batch, and the cost reference below is updated from them.
4. Commit the new `out/` dirs (never `work/`) with a short message, then push. The user wants a commit after every completed step (2026-10-04).
5. After a surah's augments, ask the user whether to run the enrichment for it (Step 5).

## Cost reference (Opus 5.5 high, actual)

| Step | S87 (19 ayat) | S100 (11 ayat) | Per call |
|---|---|---|---|
| Map | $4.19 | $1.64 | $1.6–4.3; a large surah is estimated up to $6.3 (S96) |
| Image prose | $4.27 | $2.73 | $2.0–4.3 |
| Readings | $21.65 | $12.06 | ~$1.1 (0.7–1.4 × estimate) |
| Augment9 (2026-10-04 batch) | $15.15 for 6 ok | S1: $17.65 for 6 ok | $1.8–4.4 by list size, mean $2.5 for 13 ok calls, 0.73–1.28 × estimate (123–347 passages); 1:4 at 319 passages hit a safeguard stop after $4.31; five 429s cost $3.96 for nothing |

## Where things stand (2026-10-04)

| Surah | Map | Image prose | Readings | Augment9 |
|---|---|---|---|---|
| S1 | ✓ | ✓ | 7/7 | 7/7 (1:4 accepted after a safeguard stop) |
| S87 | ✓ | ✓ | 19/19 | 6/19 (87:7–87:11 429 session limit, 87:12–87:19 not started) |
| S100 | ✓ | ✓ | 11/11 | 0/11 |
| S103 | – | – | 0/3 | – |
| S107 | ✓ | ✓ | 7/7 | 0/7 |
| S88–S95 | ✓ | ✓ | 0 | – |
| S96–S114, apart from S100, S103, S107 | – | – | – | – |

- Older augments (augment2, augment3, and augment8 on 87:8) are superseded. They stay on disk under their own dir names.
- Existing readings with check findings (most often Arabic outside tags, and process words) are listed by `status.py`. They were never printed when they ran, before 2026-10-04. Fixing them is the user's call.
- `status.py` is the live view; this table is a snapshot.

## Step 5 (optional): enrichment

After a surah's ayat are read and augmented, there is an optional enrichment step: a page of extra notes for the advanced reader, on the surah commentary and on each ayah reading. It is a separate pipeline with its own rules and costs.

- **Ask the user.** When a surah's ayah readings and augments have finished and been reported, ask whether the user also wants the enrichment run for that surah. Never start it without that go; the go for v16 does not cover it.
- **Runbook:** `enrichment/v2/RUNBOOK.md`. Follow it for everything about enrichment: its rules, its pack step, the surah page, the ayah pages, costs and failures. Do not run it from this runbook.
- **What it reads from v16:**
  - the surah image prose (`images.r13…/images.md`), never augmented;
  - each ayah's reading after augment9 (`…/augment.augment9.opus/N_A.reading.tr.md`). An ayah without augment9 gets no ayah page.
  - The v16 outputs are frozen for it: enrichment never edits them, and reports errors in the base to its own `errata.jsonl`.
- **Order:**
  - The surah page can run once the image prose exists.
  - The ayah pages need augment9 on their ayat.
  - Its pack must be rebuilt after augment9 has run (`enrichment/v2/RUNBOOK.md`, "Ayah pages").
- The enrichment code is another session's work; do not edit it from here.

**The order for each surah is: map → image prose → readings → augment9 on the ayat → (ask) enrichment.**

- The ayah augment (augment9) runs as part of a surah's v16 run; enrichment is the optional step.
- A **surah-commentary augment** is a dedicated step still to be designed (user, 2026-10-04 evening): image-based discovery from the commentary's own prose, since the per-ayah lists encode ayah-level links and inflate five-fold when given per image section (`REVIEW_production.md` §10). When it exists it goes between the image prose and the readings; readings written before it predate it, which the DESIGN records. Until then the order above stands and readings are not held back.
