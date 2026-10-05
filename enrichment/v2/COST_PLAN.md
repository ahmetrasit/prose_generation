# Enrichment cost: findings and fix plan (2026-10-04 night)

Targets (user): under $10 per ayah page on average for the Fātiḥa now; **under $5 per ayah page on average** for the
production-grade workflow. Opus 5.5 high writes the pages (chosen for quality after the S107/S100 trials). Never
Haiku. Dollars are the CLI's nominal figure at published rates (the account is a Max subscription; nominal $ tracks
the allowance used).

## 1. Measurements

### The 1:1 page (one Opus subagent, `enrich.py spawn`, brief zengin.md + common.md)
Transcript: 88 assistant messages, context 28k → 512k tokens (mean ~281k per turn).

| item | tokens | $ at published rates |
|---|---|---|
| cache reads (whole context re-read every turn) | 24.75M | 4.95 |
| cache writes, 5-minute TTL | 973k | 4.86 |
| ↳ one cache expiry: the whole 465k context rewritten | 465k | 2.32 |
| visible output (floor; thinking is not in the transcript) | 29.4k | 0.59 |
| hidden thinking (estimate from claude -p trials: ~1.7k output per turn) | ~120k | ~2.4 |
| **total** | | **~12.5–13** |

Tool output that entered the context (532k characters in all; Arabic ≈ 1.45 characters per token):
- spilled outputs re-read in full (Claude Code saves a large Bash output to a file, shows a 2 KB preview; the agent
  then Reads the file): 7 calls, 126k chars;
- corpus search results: 23 calls, 106k;
- whole sources dumped to scratch files and sliced with ad-hoc python, one turn per slice: 15 calls, 89k;
- corpus get / ayah: 20 calls, 74k; prompt, pack, schema: 6 calls, 70k;
- records built by a 26.5k-token generator program `build.py`, then patched six times with python string
  replacement, each patch a turn at ~470k context: 10 calls, 40k;
- self-orientation late in the run (validate.py, render.py, S100's annotations, `ls work`): 5 calls, 18k.

### Root cause of the cache expiry (found and fixed tonight)
The 7.2-minute gap was not thinking or writing: a tool call (the agent re-ran its build.py, which validated the 53
records) took 7 min 12 s. `tools/blocks.py Corpus.resolve` and `corpus.py get` looked locators up with
`seg=? OR seg LIKE ?`, which defeats the UNIQUE index and scans the whole `seg` table: 0.2 s per locator warm,
minutes on a cold external disk. Fixed (commit a38d50c81): exact lookup plus a `seg>=loc# AND seg<loc$` range.
validate.py on 1:1: 32 s → 0.2 s, same result. The agent's earlier `corpus.py get` calls needed `timeout 300`
and one `sleep 30` on a backgrounded get for the same reason.

### Accounting bug (fixed tonight)
`_commentary/v16/agentrun.py` RATES had Opus input $8 and 5m write $10 (double), reads $0.17; Sonnet likewise.
Published: Opus $4 in / $5 5m write / $8 1h write / $0.20 read / $20 out. These reproduce the CLI's own cost_usd to
the cent on three enrichment trials. Ledger figures before the fix overstate writes and understate output.

### v1 (for comparison, from the Codex session logs)
v1 made surah pages only (its ayah pages are 194-byte placeholders), with gpt-6.1-sol max through Codex (no $ shown):
S1 surah page 14.8M input tokens (14.2M cached), 86k output; S100 and S107 9.9M and 10.6M; plus an orchestrator
session (20.7M) and two Astra audit sessions (7.6M, 6.6M). Priced at Opus rates the S1 page alone is ~$7.8. v1 had
the same token pattern; it did not show dollars and did not make ayah pages.

### The staged pilot (okuma.py), dropped
Sonnet planner ($0.61) + Sonnet readers of every segment tied to 1:1 (478 segments, 1.38M characters, 17 readers).
Batch 1 (7 readers, 616k characters): estimate $3.11, actual $6.03; 1,002 evidence cards ≈ 209k tokens (compression
only ~1.6:1); recall 53/53 of the page's citations within those segments. Projected 1:1: ~$19–20 including a judge
reading ~500k tokens of cards. Dropped; the code stays as a record.

## 2. Corpus size per Fātiḥa ayah (characters of segments tied to the ayah, ranges included)
1:1 1,094k · 1:2 561k · 1:3 227k · 1:4 354k · 1:5 397k · 1:6 308k · 1:7 672k. Base pages (numbered) ~36k characters.

## 3. Fix plan for the single-call design (one Opus agent per page)
Done: RATES; index lookups (validator 0.2 s, get instant).

Proposed (code):
1. `corpus.py get` and `search`: hard output caps so nothing ever spills: `get` default --chars 3000 per segment
   and a total cap (~20k characters per call) with a printed note naming what was cut and how to fetch the rest
   (`get LOC --from N`); `search` default --n 10 --chars 300. A paging option `--from N --chars M` to read a long
   segment in pieces instead of dumping it to a file.
2. A `check` subcommand the agent may run on its annotations.jsonl (fast validator, prints only failures) so it never
   writes or runs its own builder/validator scripts.

Proposed (briefs, to be shown to the user first):
3. common.md "Reading economy": never redirect corpus output to files; never read a spilled tool-result file; use
   `get --from` to page; batch locators in one `get`.
4. zengin.md output: write annotations.jsonl directly as JSON lines (in parts if long: Write the first part, then
   append with Edit or a second file merged by the finish step), never through a generator program; run `check`
   once at the end and fix only the failures it names.
5. SCHEMA_CARD.md: one complete example record per common tur, so the agent never reads validate.py, render.py or
   other pages.

Replay of the 1:1 transcript with 1–5 applied (spill re-reads, slow-tool turns, orientation and patch turns removed;
slicing turns halved; no cache expiry): visible-output cost $10.40 → $5.26, 88 → 71 turns, peak context 512k →
~315k. With hidden thinking (~$2–3): **1:1 ≈ $7.5–8**. The lighter Fātiḥa ayat should be lower, so the Fātiḥa
average is expected under $10 but **not under $5**.

## 4. Open questions for the review
- What else, in the single-call design, cuts toward $5/ayah on average without losing what the user values in
  Opus pages (verifiable Arabic quotes, tafsir depth, sharp meal judgement, no false positives)?
- The cache-read share (24.75M tokens, $4.95) is the structural cost of an agent loop: turns × context. Levers:
  fewer turns (batching), smaller context (caps), and what else?
- 5-minute vs 1-hour cache: the subagent used 5m writes; the claude -p trials used 1h on S107 and 5m on S100.
- An alternative design that could reach under $5 per ayah average with Opus quality, and its risks.

## 5. Trials built (2026-10-05), waiting for a session that has the agent types
Opus review (2026-10-05): gaps — turns are the main lever (88 messages, 89 serial calls; common.md said "one file
per call"); thinking stays in the context; the ledger undercounted output (1:1 is ~$14 with thinking, not $10.40);
the brief demands more than one context holds, so sources were skipped silently (25 tied sources never opened on
1:1). Improvement (mode `tur`) and alternative (mode `dosya2`) built; each runs at high and medium.

Prepared (never spawned yet; `--trial`, so nothing is accepted):
- work/s001/zengin-tur.1_1.opus.high      → agent type enrich-page-high
- work/s001/zengin-tur.1_1.opus.medium    → agent type enrich-page-medium
- work/s001/zengin-dosya2.1_1.opus.high   → agent type enrich-page-high
- work/s001/zengin-dosya2.1_1.opus.medium → agent type enrich-page-medium

Spawn: Agent tool, subagent_type as above (the definitions in .claude/agents/ set model opus and the effort; they
load when a Claude Code session starts), prompt = the exact text of the dir's spawn.md. The four run in parallel.
Finish each: `python3 -B enrichment/v2/enrich.py finish --surah 1 --target 1:1 --mode tur|dosya2 --model opus:high|opus:medium --trial`.
Report per trial: cost_usd (recorded) and cost_usd_est (with thinking), turns, kept/dropped, unread_sources, and
compare the records with the reference page work/s001/zengin.1_1.opus.high (53 records, ~$14 estimated).
