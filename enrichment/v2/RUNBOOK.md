# Enrichment v2 runbook (for the operator; agents never read this)

All commands from the workspace root `/Volumes/aro/projects/prose_generation`.

## 0. Once per corpus change
```
python3 enrichment/v2/tools/corpus.py import-local          # sources already on this machine
python3 enrichment/v2/fetch/<fetcher> …                      # new sources (meal, OpenITI, Elmalılı, references)
python3 enrichment/v2/tools/corpus.py build                 # one index: enrichment/corpus/corpus.sqlite
python3 enrichment/v2/tools/corpus.py sources               # what is local, what is a memory pointer
python3 enrichment/v2/tools/schema_doc.py                   # after any schema.json change
```
A pack records the index mtime; rebuild packs (`pack.py --surah N --force`) only for surahs with no call
started, or start a new attempt.

## 1. Before a surah starts
1. The v16 base is final: one `out/sNNN/images.r13.*/images.md` and, per ayah, `augment.augment3/S_A.reading.tr.md`.
   pack.py refuses an ambiguous surah base (pass `--surah-base`).
2. Turkish word history: build the pack, read `pack.json` turkish.fetch_candidates (key words of the panel meals
   with no Nişanyan/TDK/Kubbealtı entry yet), fetch the ones that matter
   (`python3 enrichment/v2/fetch/ref_loanword.py <word> …`), rebuild the index (`tools/corpus.py build`) and the pack
   (`pack.py --surah N --force`, only while no call of the surah has started).
3. `../dictionary` HEAD equals the transfer commit in `quran-data/data/dictionary/tr/MANIFEST.json` (pack.py
   checks; if not, sync quran-data first).
4. Tell the user the expected cost before the surah starts. Codex subscription runs report no USD: give the call
   count (one per page: the surah page plus one per ayah page) and prompt sizes from `enrich.py build`.
   Measured cost per call: `run.log.json` holds `session.tokens` (input, cached, output, reasoning), the weekly-limit
   reading before the call (`weekly_before`, from the latest saved session) and during it (`session.weekly_used_*`);
   `status` shows a running call's tokens and context live. Calibrate the next estimate from these.

## 2. Run
```
python3 enrichment/v2/enrich.py build  --surah 107                      # builds the pack if needed; sizes the prompts
python3 enrichment/v2/enrich.py run    --surah 107                      # every page of the surah not yet started
python3 enrichment/v2/enrich.py run    --surah 107 --target 107:3       # one page
python3 enrichment/v2/enrich.py run    --surahs 87-114 --parallel 3
python3 enrichment/v2/enrich.py status --surah 107
```
Model: Opus 5.5 high is the default (user, 2026-10-04, after the S107 and S100 trials); a finished trial page is
accepted with `enrich.py accept --surah N --target T --model opus:high`. Corrections that a trial model found and the
accepted page lacks are added to errata.jsonl by hand, with found_by and the operator's confirmation.

Model comparison on one page (each model and effort in its own call directory, nothing copied to out/):
```
python3 enrichment/v2/enrich.py build --surah 107 --target surah --model sol:max,sol61:max,opus:high,sonnet:high
python3 enrichment/v2/enrich.py run   --surah 107 --target surah --model sol:max,sol61:max,opus:high,sonnet:high \
        --trial --parallel 4
```
Models: astra (default), sol, sol61 (codex exec); opus, sonnet (claude -p inside Claude Code's own sandbox: every
shell command sandboxed, writes only in the call directory, no network; out/, other call directories and the
session stores hidden, so trials are blind; --max-budget-usd 40; run.log.json records cost_usd and
permission_denials). Every call is killed after 8 hours. Several models on the same pages only with --trial.
Codex runs can still read other call directories (their sandbox has no read limits): run trials before a page is
accepted, or check their command logs for reads of out/ and zengin.* directories.

One call per page, like v16's augment step: the call (prompts/common.md + prompts/zengin.md) does the research,
the meal review and the composition, and writes the page's records to `work/sNNN/zengin.<page>/annotations.jsonl`.
Nothing retries automatically.

## 3. After each call (script)
- Every record is checked (`validate.py`). A failing record is dropped and listed with its errors in
  `check.json`; it is not sent back for repair. Read the dropped list before publishing.
- The kept records are rendered into the frozen base (`page/`); the page is checked: base paragraphs byte-exact and
  in order, blocks round-trip, nothing after the registry. A page error fails the call (status `error`).
- Accepted: the page is copied to `enrichment/v2/out/sNNN/` (never overwritten) with a `.json` record (hashes, base,
  dictionary commit, kept and dropped ids); duzeltme records go to `enrichment/v2/errata.jsonl` (input for a later
  v16 revision; v16 itself is not touched).

## 4. Failures
- `status` shows `started (running or interrupted)`: the call died (session limit, crash). Never rerun that
  directory. Read its `run.stream.jsonl`/`stderr.log`, then `enrich.py run --surah N --target T --attempt 2`
  (directory `zengin.<page>.a2`).
- Many dropped records or a page error: read `check.json`; decide between a new attempt and accepting the page as
  it is.
- A missing source the call needed: `gaps.json`; fetch it, rebuild the index, and run a new attempt of the page.

## 5. Ledger
`enrichment/v2/work/ledger.jsonl`: one line per call (prompt hash, model, effort, tokens, seconds, status).

## 6. Later: the Bible pass (tevrat, incil)
Bible and other Jewish and Christian sources are a separate pass with their own corpus and index (kind `intertext`,
each source.json declaring its `gelenek`), their own brief, one call per page as here, writing blocks with gelenek
tevrat or incil (schema 3.1). It never reads the Islamic records and vice versa. Its pages anchor to the same base
paragraphs, so a script merges the layers: after each paragraph, islami, then tevrat, then incil blocks. Corpus,
brief and merge script not built yet.
