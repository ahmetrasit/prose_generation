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
2. `../dictionary` HEAD equals the transfer commit in `quran-data/data/dictionary/tr/MANIFEST.json` (pack.py
   checks; if not, sync quran-data first).
3. Tell the user the expected cost before the surah starts. Codex subscription runs report no USD: give the call
   count (one per page: the surah page plus one per ayah page) and prompt sizes from `enrich.py build`.

## 2. Run
```
python3 enrichment/v2/enrich.py build  --surah 107                      # builds the pack if needed; sizes the prompts
python3 enrichment/v2/enrich.py run    --surah 107                      # every page of the surah not yet started
python3 enrichment/v2/enrich.py run    --surah 107 --target 107:3       # one page
python3 enrichment/v2/enrich.py run    --surahs 87-114 --parallel 3
python3 enrichment/v2/enrich.py status --surah 107
```
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
