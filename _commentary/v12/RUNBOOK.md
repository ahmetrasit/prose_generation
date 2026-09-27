# RUNBOOK — v12 commentary (for a cold orchestrator)

You start and watch runs; you do not edit inputs or outputs by hand. Every step checks, repairs or reduces its own
output and records what happened in `out/sNNN/S_A/status.json` (surah pass: `out/sNNN/surah/<window>/check.txt`).
Work in the repo root (`/Volumes/OZTURK/_projects/prose_generation`).

## Rules

- **Get the user's go before any Opus run they have not asked for**, and tell them the estimate first (step 1).
- **Cost rule.** A call starts only when its estimate is below `--max-cost` (default $5); once started it is never
  stopped and never retried, whatever it costs. An ayah over the limit is not started (`over-cost`); an unusable answer
  marks the ayah `failed` (no retry). Only the small tag-repair calls (medium effort, a few paragraphs) follow a writer
  call; their cost is recorded (`repair_cost`, `total_cost`).
- Never restart or kill a running write (the lock skips it).
- **Never twice** (user rule): an ayah whose writer call started (`writing`, `checking`, `done`, `failed`) is never
  called again, and a surah window whose pass started is never run again; the commands skip them and say so. Running
  the same command again is therefore safe. There is no `--force`; only the user clears an output.
- Never put `NOTES.md` or anything in `eval/` into a model's input (known answers).
- Commit and push after each run (work on main).

## 0. Once: prerequisites

```
claude --version                                        # Claude Code CLI, logged in (the writer runs `claude -p`)
python3 _commentary/v12/inputs.py 29:45                 # evidence only, no model: prints input sizes
```

The root dossiers come from `/Volumes/OZTURK/_projects/root-dossier` (the user runs Luna there; its RUNBOOK). Without
them `usage.md` is simply absent. `DOSSIER_OUT=/Volumes/OZTURK/_projects/root-dossier/out-wa` reads another arm.

## 1. Estimate (no model)

```
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --estimate
python3 _commentary/v12/run.py surah 1 --estimate
```

Per ayah: input bytes and the estimated cost (input tokens at $8/M as a one-hour cache write, expected output at
$20/M). Tokens per byte and expected output are calibrated from finished calls (≥ 3), else 1.0 token/byte and 60k
output tokens at effort high. Report the estimates to the user with the request for a go.

## 2. Run

```
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3                  # the S29 probe
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3 --no-usage --tag nousage   # arm without usage.md
python3 _commentary/v12/run.py surah 1 --parallel 7                                  # every ayah, then the surah pass
python3 _commentary/v12/run.py chains 1                                              # the surah pass alone
```

Run arms one after another, never at the same time: they share the evidence folder `work/sNNN/S_A/`.

Per ayah: prep (scripts) → estimate → one Opus call (ledger + reading) → check (commas, sources, validator; at most one
small repair call; then unverifiable tags become plain Turkish) → render. Long surahs: the surah pass runs once per
passage window. Options: `--effort high|xhigh|max` (default high), `--max-cost N`, `--tag NAME` (outputs in `out-NAME/`).

## 3. Watch and finish

```
python3 _commentary/v12/run.py status 1            # one line per ayah: state, cost (estimate), tokens, verify, stripped
```

States: `prep`, `writing`, `checking`, `done`, `failed` (the error is in status.json), `over-cost` (not started).
- `failed`: report it with the error; `run.py` never calls it again (a redo needs the user to clear it).
- `over-cost`: report the estimate; the user decides (e.g. `--max-cost`, a smaller input, or not at all).
- `stripped n` in status: n tags could not be verified and became plain Turkish. Report counts above 3 per ayah.
- `dossier_corrections` in check.txt: the writer's `usage.md:` ledger lines (a root dossier it found wrong). Collect
  them for the root-dossier repo; they never reach the reader's page.
- `usage_error` in status: deliver.py failed; usage.md is missing from that ayah's evidence. Report it.

Outputs: `out/sNNN/S_A/S_A.md` (reading + Kur'an'ı Kur'an'la + Kur'an'da bu kelimeler + Kelimeler ve okuyuşlar +
Surenin bütününde), `S_A.ledger.md`, `S_A.reading.tr.md`, `check.txt`, `status.json`, `run.log.jsonl`;
`out/sNNN/surah/<window>/` (`chains.md`, `S.surah.tr.md`, `ayat.md`, `check.txt`). Evidence: `work/sNNN/S_A/`.

Commit and push: `git add -A && git commit -m "v12: <what ran>" && git push origin main`.

## When to stop and report to the user

- Two ayat in a row `failed`, or any `over-cost`.
- A real cost above $5 for an ayah (possible by rule, since a started call is never stopped): report it with the
  estimate so the calibration can be checked.
- The Claude CLI is unavailable.
