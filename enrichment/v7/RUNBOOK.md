# Enrichment runbook: tier 1 (v7) — read this first

For the orchestrator, a Codex session running **tier 1** (per source segment, Luna max). Run commands from the
root of the active checkout.

**Status 2026-10-09.** Tier 1 is the only v7 stage still in use. Everything after it is v9: verse maps
(`enrichment/v9/map.py`), the writer and the meal block (`enrichment/v9/PLAN.md`). **Do not run v7 stages 1b, 2 or
3 below** (retag, tier 2, v7 writer); they are kept as the record.

**What changed on 2026-10-09 (user: no input or output dropped anywhere in the workflow):**
- **Always build with `--quotes`.** The quotation packet adds works with no verse index that quote the verses' own
  words (ulūm, grammar, wujūh, modern bayānī works such as Bint al-Shāṭiʾ's *al-Iʿjāz*, hadith matn).
  Indexed hadith segments are now Tier 1 inputs too. The packet uses unique Arabic windows and a cautious
  explicit-citation plus full-verse fallback; `quote_limits` in the manifest records verses that cannot be
  searched by a unique window. Other untied material may still need the later word stage.
  Indexed hadith, sīra and poetry are also searched for verses outside their index range and overlay; when both
  routes reach one segment, its scopes are merged into one full input.
- **Whole segments only.** The quotation packet no longer cuts long segments to excerpts. The old
  `q103_1-20261008` run documented 37 excerpts, but its saved chunk parts are absent in this checkout, so their
  exact locators cannot be recovered. Its outputs stay unresolved for coverage until rebuilt from full current
  text. New manifests record `excerpt_locs`; legacy manifests need a complete saved input snapshot to count as done.
- **No edition rule.** A short edition is digested even when its `-FULL` edition covers the verse; the two mostly
  differ. Earlier runs skipped short editions, so builds over already-digested surahs now pick them up.
- **Row tags** (`words`, `type`) stay in the brief; the v9 maps do not need them, but they are harmless.
- **Chunk size** is unchanged (20,000 rendered characters; the forecast-split policy below still applies). Chunking
  never drops input: a segment larger than a chunk gets its own chunk, whole.
- **Corpus provenance** from selected `seg.extra` fields follows the segment header. Agents use it for source
  status and reference leads; only the body may supply a claim's anchor.

## Rules

1. **Each stage needs the user's go.** Report the build's numbers first: agents, characters, estimate.
2. **The orchestrator spawns the agents itself.** Scripts only build inputs and spawn files, check and report.
   - Do **not** use `run.sh` / `run_codex.py` for these runs. They are the scripted fallback, seven at a time.
   - **Parallelism:** use the user's current cap (60 Luna max agents for the requested two batches). Keep that
     cap filled as agents finish; do not wait for a wave.
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

**Scope and quota come from the user.** Before every build, ask which surahs to run and how much quota to use
(agents at a time, expected cost); do not choose a scope on your own. Typical cost: about $0.25 per verse
API-equivalent (tier 1 about $0.16 plus the quotation packet about $0.09); Codex usage counts toward the budget.

```bash
python3 -B enrichment/v7/digest.py build t1_s002-003_20261009 --surahs 2 3 --models gpt-6-luna:max --skip-done luna-max --quotes
```

- **Never twice:** while another tier-1 run is built but not finished, add `--skip-planned <that run>` (see
  `enrichment/v9/RUNBOOK.md`, "Several surahs at once").
- Scope options: `--surahs 2 3 …` (every ayah of those surahs), `--ayat S:A …`, or `--page PATH --ayah A` (a frozen
  page: its own ayah and every verse it cites). Name runs `t1_<scope>_<date>`.
- The build takes about 25 seconds plus 0.35 seconds per verse for the quotation search; it prints every window it
  searched (`quotes S:A …` lines). Pass the build's `NOTE`, `WARNING` and `SKIPPED` lines to the user verbatim.
- **What it covers:** every eligible source segment tied to the verses (index range and range overlay), including
  indexed hadith, every short and full edition, and the selected quotation packet.
- **What it routes elsewhere** (each listed in `work/RUN/manifest.json`, never silently):
  - segments already digested in any earlier run (`--skip-done`), except excerpt-only ones;
  - meal and translations (the v9 meal step reads them), and the Quran text;
  - surah-level segments (no ayah number): reserved for the surah pages;
  - lexica are not searched (the project dictionary is the only lexical source).
- **Quotation windows too common to mean a quotation** (found in more than 40 segments) are printed as `NOTE … not
  used`; report them, they are a selection rule, not a cut.
- **Quotation limits:** `manifest.json` records each ayah's unique-window counts and explicit-reference fallback.
  If no unique window exists, the fallback requires both a source's explicit verse citation and its full normalized
  Arabic verse in the body. It avoids noisy index-only references but cannot prove all untied material is covered.
- **Already done:** `--skip-done` counts only finished, valid output lines with verified input provenance. New
  manifests hash each source's body, heading and selected metadata. Legacy runs need complete saved chunk parts,
  checked against the current body; if the parts are missing, the output is unresolved even with a valid anchor or
  a `none` reason. Use `--skip-planned` with `--skip-done` for an active run.
- **One verified digest serves every verse it names.** Readers expand ranges and annotated verse lists in
  `verses` and link `mentions` with an explicit "about another verse" label. The checker and word tags use the
  same expansion. Readers apply the same output and provenance checks as `--skip-done`; unresolved inputs stay
  unresolved. `enrichment/v9/linked.py build` creates the index used by `q.py linked` for segments tied to a verse
  whose notes discuss other verses. Existing maps require the separately approved map update to gain new notes.
- **Spawn files:** `enrichment/v7/work/s103-1/spawn/luna-max_c*.md`. Keep up to 60 running at a time.
- **Outputs:** `work/s103-1/out/luna-max/c*.jsonl`.
- **Chunk size for new builds:** v7 now defaults to 20,000 rendered input characters per agent. A single
  source segment can exceed the target; smaller chunks reduce the risk of crossing 120k context tokens but
  do not enforce a hard token ceiling. The recorded `chunk_chars` in each manifest governs that run.
- **S12/S17–19 selective plan:** launch `work/s12_17_19_sel150k/spawn/luna-max_c*.md` when the user gives the
  stage go. It retains the original 391-chunk order, splits the 52 chunks forecast above **150k peak request
  input tokens** into two, then splits two halves that still forecast above 150k. This produces 445 agents for
  the same 12,715 segments and 16,039,136 rendered source characters. The final maximum forecast is 149,752
  tokens. The forecast is not a hard cap: held-out historical error was 18.5k–23.6k tokens on average.
  The 120k figure remains the post-run reporting cap; the user's pre-run split threshold is 150k.
  `forecast.py` records the training runs, coefficients, held-out results and every chunk estimate in the
  `forecast*.json` files. `digest.py build --split-plan` reproduces a selected split, including quotation locators.
  Older manifests lack input hashes; a changed rendered length emits a `NOTE` for review before launch.

After all of them finish:

```bash
python3 -B enrichment/v7/digest.py check s103-1      # every segment answered, every anchor verbatim
python3 -B enrichment/v7/digest.py report s103-1     # cost per run, completion, peak context (cap 120k)
```

**Workflow review fixes (2026-10-10).** Check commands print every problem and return
nonzero on failure; unknown chunk/model selections fail. Coverage/readers track the
latest same-session repair, including a pending repair, and invalidate caches when
completion changes. Portable repair wrappers accept padded or plain chunk numbers,
use the configured live/archive directories, preserve every checker problem and
save `repairN.run.json`; push those records with the original `run.json`. A changed
or missing source requires rebuilding the input, not another model repair.

For the screened missed-verse pass, follow `HANDOFF-hadith-20261010.md` and the
current plan, not its historical agent/cost totals. It checks unnamed verses, uses
whole segments and complete earlier notes, and records its quotation selection
limits. CHECK assignments are enforced by the checker and all supplement readers.
Do not build overlapping recheck runs while one is active.

Existing verse maps must be checked/updated after Tier 1 or supplements change.
An existing note whose content changes, or whose provenance is no longer valid,
requires a fresh verse map with `map.py build NEW_RUN ... --supersede OLD_RUN`.
Saved evidence stays in the old run; additive updates cannot repair its old positions.
The full review is `REVIEW-workflow-20261010.md`.

## Stage 1b: retag (v7 record; superseded by v9 maps, do not run)

Rows digested before row tags (runs without `"row_tags": true`) need `words` and `type` before tier 2 groups them
into cells.

```bash
python3 -B enrichment/v7/retag.py build RUN (--ayat … | --page PATH --ayah A) --models gpt-6-luna:max
python3 -B enrichment/v7/retag.py check RUN          # every row answered once, words in its verses, type listed
python3 -B enrichment/v7/retag.py report RUN
```

Spawn files: `work/RUN/retag/spawn/luna-max_c*.md`, spawned like tier 1. Already-tagged rows are skipped and counted.

## Stage 2: tier 2 (v7 record; superseded by v9 maps, do not run)

```bash
python3 -B enrichment/v7/merge.py build s103-1 --from luna-max --page <same page> --ayah 103:1 --models gpt-6-sol:high
```

- **Skips:** verses that already have tier 2 (`SKIPPED`). A verse with no tier-1 notes gets an empty view list and
  no agent (`NOTE`).
- **Spawn files:** `work/s103-1/tier2/spawn/sol-high_<s>-<a>.<slice>.md`, one per slice (a verse is one slice unless it
  exceeds 90k characters of input). Spawn them the same way. Untagged rows are printed as a WARNING: run stage 1b first.
- **New rows later:** `merge.py update RUN --model TAG` builds slices only for the cells whose rows changed.
- **Outputs:** `work/s103-1/tier2/out/sol-high/<s>-<a>.<slice>.jsonl`; `merge.py check RUN` assembles `<s>-<a>.jsonl` and `.md`.

After all of them finish:

```bash
python3 -B enrichment/v7/merge.py check s103-1       # every tier-1 row in at least one view; writes the readable .md
python3 -B enrichment/v7/merge.py report s103-1
```

## Stage 3: v7 page writer (record; superseded by the v9 writer, do not run)

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
| An agent did not finish (`report` WARNING), or wrote no file (`check`: no output file) | Report it to the user. Ask the same agent to repair its work if possible; do not create a second session with its name. If still missing, with the user's go build a new run with `--skip-done`: it picks up segments without a valid, finished output line against the current corpus. |
| `check` lists anchor or field problems in a finished file | Report them and ask that same agent to repair them. |
| Peak context over 120k (`report` WARNING) | Report it. The output is still valid if `check` passes. |
| Two tier-2 files for one verse (`merge.load` error) | Two runs consolidated the same verse. Stop and ask the user which one stays. |

## Run names

One run per scope, for example `s103-1` for the 103:1 page. Earlier runs:

| Run | What it holds |
|---|---|
| `test-20261007` | 100:1 and 87:6 own material; tier 2 for both verses |
| `pilot100-20261007` | 100:1 page's cited verses; built, **not run; do not run it** (superseded: later runs digest those segments with `--skip-done`) |
| `s103-1` | 103:1 page's own and cited verses; tier 1 complete |
| `s103-23` | 103:2–3 references; tier 1 complete |
| `s1_87_114` | All 295 own ayat of S1 and S87–114; tier 1 complete (264 chunks) |
| `s12_17_19` | All 430 own ayat of S12 and S17–19; original 40k build, **not run** (391 chunks); base for selective forecast |
| `s12_17_19_20k_exact` | Same 430 ayat, 20k rendered-input alternative, **not run** (862 chunks) |
| `s12_17_19_pred150k` | First selective split build, **not run** (443 chunks); planning intermediate |
| `s12_17_19_sel150k` | Final selective forecast build, **not run** (445 chunks); built before 2026-10-09 (no quotation packet, edition rule applied): rebuild with `--surahs 12 17 18 19 … --quotes` instead |
| `q103_1-20261008` | Quotation packet of the 103:1 page (69 chunks); 37 excerpt-only segments documented, exact locators unavailable because its chunk snapshots are absent here; outputs require a new full-input run before reuse |

`--skip-done` makes later runs skip whatever earlier runs digested.
When building while an unrelated run is still rewriting output files, first verify that the two runs have no
source-segment overlap, then pass `--skip-done-exclude-run <active-run>` so the build does not read those transient
files. The excluded run is recorded in the new manifest.
