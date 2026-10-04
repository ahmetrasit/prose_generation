# v16 production runbook (r13 + augment8)

For an agent starting cold. It covers one surah end to end:

**surah map → surah image prose (the surah commentary) → ayah readings → ayah augment.**

The history and the reasons behind each choice are in `DESIGN.md`. This file holds only what is needed to run.

## Rules from the user (never break them)

1. **Each step needs its own go.**
   - Before a step starts, tell the user what it will run, how many calls, and the expected cost (the scripts print an estimate).
   - Then wait for an explicit go. A go for one step or one surah does not cover the next.
2. **No agents, and no background runs, without an explicit go.** That includes subagents, Workflow and `run_in_background`.
3. **Never rerun a call.**
   - A run dir with `started.json` or `run.log.json` is blocked, and the scripts refuse it.
   - If a call failed (for example it hit the session limit at $0), ask the user first. Then rename the dir to `<dir>.<reason>-<cost>usd`, as in `augment.augment3.session-limit-0usd`, and run it again.
4. **No silent failures.**
   - Report every `WARNING:` and `NOTE:` line the scripts print.
   - Report every ledger row whose `status` is not `ok` or whose `check` is not `ok`.
   - Do not summarize them away.
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
- **Ledger.** Every paid call appends a row to `_commentary/v16/out/ledger.jsonl`, with its cost and `check`.
- **Status at any time** (no calls):

```bash
python3 -B _commentary/v16/status.py 87 100 103
```

It shows the map, the image prose, readings n/N, augment8 n/N, and the ayat still to run. "Spent" is the ledger total for that surah, including every earlier trial.

## Step 1: surah map (1 call)

```bash
python3 -B _commentary/v16/packets.py map --surah N --no-hft --tool          # prints the estimate; add --go to run
```

- Output: `out/sNNN/surah.map3.nohft.tool/map.md`.
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

- Output: `out/sNNN/images.r13.map3.nohft.tool.tool/images.md`, plus `check.json`.
- This is the surah commentary. It is final as written: no augment.

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
- At most 5 calls at a time, as for S87.
- Run the builds without `--go` first. Sum the estimates and give the total to the user.

## Step 4: ayah augment (one call per ayah)

Production since 2026-10-04: brief `augment8` with Opus 5.5 high. These are the script defaults.

```bash
python3 -B _commentary/v16/augment.py out/N_A/DM.r13.images.r13.map3.nohft.tool.tool.tool   # estimate; --go to run
```

- **Output** goes to `…/augment.augment8.opus/`:
  - `N_A.reading.tr.md`: the reading with the additions;
  - `additions.md`;
  - `verdicts.md`;
  - `verdict_report.json`;
  - `insertions.json`;
  - `check.json`.
- **Additions** are marked blocks after their paragraph: `<!-- v16:augment brief=augment8 model=opus para=n kind=prose|refs … -->`. `augment.strip_augment()` removes them and gives back the reading byte for byte (asserted).
- **Run it only after the ayah's reading has finished.** At most 5 calls at a time.
- **Every warning goes to the user.** The ones to expect:
  - listed passages without a verdict;
  - verdict mismatches;
  - additions with no verdict;
  - lookups with no verdict;
  - consecutive ayat split into separate references;
  - refused commands, which never ran.
- The ledger has two rows per call: `augment` (the cost) and `augment-applied` (the counts).

## Running several calls

Build first, then report the estimates and wait for the go. Only then launch, at most 5 at a time, keeping every line of output:

```bash
mkdir -p _commentary/v16/work/logs
printf '%s\n' 87:1 87:2 87:3 | xargs -P 5 -I{} sh -c \
  'python3 -B _commentary/v16/augment.py out/$(echo {} | tr : _)/DM.r13.images.r13.map3.nohft.tool.tool.tool --go \
   > _commentary/v16/work/logs/$(echo {} | tr : _).augment8.log 2>&1'
grep -h "WARNING\|NOTE\|error" _commentary/v16/work/logs/*.augment8.log
```

Running this in the background is itself a background run, so it needs the user's go (rule 2).

## After each step

1. Check that the ledger rows are `status: ok` and `check: ok`.
2. Run `status.py` again.
3. Report the actual cost against the estimate, and every warning, to the user.
4. Commit the new `out/` dirs (never `work/`) with a short message, then push.

## Cost reference (Opus 5.5 high, actual)

| Step | S87 (19 ayat) | S100 (11 ayat) | Per call |
|---|---|---|---|
| Map | $4.19 | $1.64 | $1.6–4.3 |
| Image prose | $4.27 | $2.73 | $2.0–4.3 |
| Readings | $21.65 | $12.06 | ~$1.1 (0.7–1.4 × estimate) |
| Augment8 | – | – | ~$1.6–2.5 (87:8: $1.64) |

## Where things stand (2026-10-04)

| Surah | Map | Image prose | Readings | Augment8 |
|---|---|---|---|---|
| S1 | ✓ | ✓ | 7/7 | 0/7 |
| S87 | ✓ | ✓ | 19/19 | 1/19 (87:8) |
| S100 | ✓ | ✓ | 11/11 | 0/11 |
| S103 | – | – | 0/3 | – |
| S107 | ✓ | ✓ | 7/7 | 0/7 |
| S88–S95 | ✓ | ✓ | 0 | – |
| S96–S114, apart from S100, S103, S107 | – | – | – | – |

- Older augments (augment2 and augment3) on S1, S87, S100 and S107 are superseded. They stay on disk under their own dir names.
- `status.py` is the live view; this table is a snapshot.

## Downstream

Enrichment v2 (`enrichment/v2/pack.py`, another session's code) reads `augment.augment3` for ayah readings. Before it consumes production output, it must switch to `augment.augment8.opus`. Tell the user; do not edit that code from here.
