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
A pack records the index mtime; rebuild packs (`pack.py --surah N --force`) only for surahs with no agent stage
started, or start a new attempt.

## 1. Before a surah starts
1. The v16 base is final: one `out/sNNN/images.r13.*/images.md` and, per ayah, `augment.augment3/S_A.reading.tr.md`.
   pack.py refuses an ambiguous surah base (pass `--surah-base`).
2. `../dictionary` HEAD equals the transfer commit in `quran-data/data/dictionary/tr/MANIFEST.json` (pack.py
   checks; if not, sync quran-data first).
3. Tell the user the expected cost before the surah starts. Codex subscription runs report no USD: give the stage
   count (5 agent calls + up to 4 repair/audit calls) and prompt sizes from `enrich.py build`.

## 2. Run
```
python3 enrichment/v2/enrich.py next --surah 107            # shows the next stage(s)
python3 enrichment/v2/enrich.py next --surah 107 --run      # runs stages until done or a failure
python3 enrichment/v2/enrich.py next --surahs 87-114 --run --parallel 3
python3 enrichment/v2/enrich.py status --surah 107
```
Order: paket → harita ‖ meal → yaz → dizgi1 → denetim1 → (onarim1 → dizgi2 → denetim2 → (onarim2 → dizgi3 →
denetim3)) → kabul. A surah stops at the first failed stage; nothing retries automatically.

## 3. Gates
- After every agent stage: required outputs exist; records pass `validate.py` (meal, yaz, onarim).
- dizgi: render + validate pages (base paragraphs byte-exact and in order, blocks round-trip, sources resolve).
- denetim: `review.json.accepted`; otherwise a repair round. After two rounds the surah is accepted with its open
  fixes counted in `accepted.json` — read them before publishing.
- kabul: pages copied to `enrichment/v2/out/sNNN/` (never overwritten), hashes in `accepted.json`, the audit's
  errata appended to `enrichment/v2/errata.jsonl` (input for a later v16 revision; v16 itself is not touched).

## 4. Failures
- `status` shows `started (running or interrupted)`: the call died (session limit, crash). Never rerun that
  directory. Read its `run.stream.jsonl`/`stderr.log`, then `enrich.py run --surah N --stage X --attempt 2`
  (directory `X.a2`). The pipeline uses the latest successful attempt.
- Validator errors in an agent stage: the stage is `error`; look at `validation.json`; decide between a new attempt
  and a manual fix of the records (record the manual fix in DESIGN.md).
- A missing source the workers needed: `gaps.json` of harita/meal; fetch it, rebuild the index, and run a new
  attempt of the affected stage.

## 5. Ledger
`enrichment/v2/work/ledger.jsonl`: one line per stage call (prompt hash, model, effort, tokens, seconds, status).

## 6. Later: the intertext pass
Bible and other non-Islamic scripture are a separate pass with its own sources (kind `intertext`), its own brief
and its own page or layer, so it never mixes into the Islamic-literature page. Not built yet.
