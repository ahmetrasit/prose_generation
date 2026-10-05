# Enrichment v2 runbook (for the orchestrator)

For an agent or operator starting cold. It covers running the enrichment of a surah: the **surah page** (now) and
the **ayah pages** (later, once v16 augment9 has run). The page-writing agents never read this file; their brief
is `prompts/common.md` + `prompts/zengin.md`.

Why things are as they are: `DESIGN.md`. The v16 base itself: `_commentary/v16/RUNBOOK.md` (another session's
work; do not run v16 from here).

Run every command from the workspace root `/Volumes/aro/projects/prose_generation`.

> **From 2026-10-04 evening no page call goes through a script** (user: every model here is Claude). `enrich.py
> spawn` builds a page's call (prompt.md, started.json, spawn.md) and the orchestrator spawns the agent itself with
> the Agent tool (type `enrich-page`, the text of spawn.md as the prompt); `enrich.py finish` checks, renders and
> accepts what the agent wrote, with the cost from the agent's transcript. `enrich.py run` is the old CLI way, kept
> for history. Spawning needs nothing installed (`subagent_type` `general-purpose`, `model` `opus`); the finish
> step reports every tool use outside the call directory's rule. Optional hardening files: `_commentary/v16/RUNBOOK.md`.

## Rules from the user (never break them)

1. **Each run needs its own go.**
   - Before anything that costs money, tell the user which pages, how many calls, and the expected cost (`enrich.py
     build` prints it).
   - Then wait for an explicit go. A go for one surah or one step does not cover the next.
2. **No agents and no background runs without an explicit go.** That includes subagents, Workflow and
   `run_in_background`. Say in the request whether a run will be in the foreground or the background; a go for
   a run covers the background only when the request said so.
3. **Never rerun a call.** A call directory with `started.json` or `run.log.json` is blocked; the script refuses it.
   A deliberate new try is `--attempt 2` (its own directory), and only after the user agrees.
4. **Never overwrite an accepted page.** `enrich.py` writes `out/sNNN/` exclusively. Replacing an accepted page
   is the user's decision; never delete or rename anything in `out/` on your own.
5. **No silent failures.**
   - Report every `WARNING:` line the scripts print, every result line whose `status` is not `ok`, and every
     dropped record and validator warning in `check.json`.
   - Do not summarize them away.
6. **The base is frozen.** Never edit v16 outputs or the pack. Errors in the base go to `errata.jsonl`.
7. **Instruction files** (`prompts/*.md`, `schema.json`, `SCHEMA_CARD.md`): tell the user what you would change
   and wait for an answer before changing them.
8. **Commit and push after every completed step** (user, 2026-10-04). `.gitignore` already decides what is versioned;
   `work/` is never committed.
9. **Spawn only with the go, with the text of spawn.md**, `model` `opus`; the finish step reports every read of
   `out/` or another call directory and every write outside the call directory.

## What a page is

- **One agent call per page.** No retries, no multi-stage pipeline, no repair calls. Model: Opus 5.5 high (the
  user's choice after the S107/S100 trials; the script default).
- **The call writes** `annotations.jsonl` in its call directory `work/sNNN/zengin.<page>.opus.high/`.
- **The script then:**
  - checks every record (a failing record is dropped, never sent back);
  - renders the rest into the frozen base, each block right after the paragraph it names;
  - checks the page against the base byte for byte;
  - copies the page to `out/sNNN/` with a `.json` record;
  - appends `duzeltme` records to `errata.jsonl`.
- **Bases.**
  - Surah page: the v16 surah image prose, `_commentary/v16/out/sNNN/images.r13.*/images.md`. It is final and
    never augmented.
  - Ayah page: the v16 reading after augment9, `_commentary/v16/out/N_A/DM.r13.*/augment.augment9.opus/N_A.reading.tr.md`.
    Its v16 additions (blocks opening with `<!-- v16:augment … para=n … -->`) are part of the base: they are
    unnumbered, belong to ¶n, and enrichment blocks go after them. An ayah without augment9 has no base, so no ayah
    page.

## Where things stand (2026-10-04)

| Surah | v16 surah base | v16 augment9 | Pack | Surah page | Ayah pages |
|---|---|---|---|---|---|
| S1 | ✓ | 7/7 (2026-10-04) | ✓ | – | 1:1 accepted (53 blocks, $13.97); 1:2–1:7 wait for the user's word |
| S87 | ✓ | 19/19 (2026-10-04) | – | – | ready when the user says so |
| S100 | ✓ | 0/11 | ✓ (built before augment9; ayah bases are augment3) | **accepted** (Opus high, 63 blocks) | rebuild the pack first |
| S103 | **missing** (v16 map and image prose never ran) | – | – | blocked | blocked |
| S107 | ✓ | 0/7 | ✓ (no turkish.md) | accepted (Astra max, old brief) | rebuild the pack first |

`enrich.py status --surah N` is the live view; this table is a snapshot.

## Surah page, step by step

For surah N. Steps 1–3 make no model calls.

**1. Check the inputs.**
```bash
python3 -B enrichment/v2/enrich.py status --surah N
```
- "no pack" is expected for a new surah.
- No v16 surah base: stop and tell the user. pack.py says "expected one r13 surah images.md". The base comes from
  the v16 chain, which this runbook does not run.

**2. Build the pack.**
```bash
python3 -B enrichment/v2/pack.py --surah N
```
- It prints a summary line (ayat, words, roots, unbound words, errata candidates, ayat without an augment9 base)
  and a WARNING line if v16's tag checker failed on a base file. Report both.
- Every guard runs before the old pack is touched; if a rebuild fails midway, the previous pack is restored (a
  WARNING says so). A leftover `pack.prev/` means a rebuild was interrupted: tell the user.
- It refuses when `../dictionary` is ahead of the quran-data transfer. Tell the user; syncing quran-data is not
  done from here.
- Read `work/sNNN/pack/pack.json`:
  - `missing_ayah_bases`: ayat without augment9. This is normal before augment9 has run; it only matters for
    ayah pages.
  - `errata_candidates`: problems v16's own tag checker found in the base (details in `errata_candidates.json`).
    The page call reads them too.
  - `turkish.fetch_candidates`: see step 3.

**3. Fetch Turkish word history.**
- `turkish.fetch_candidates` lists stems from the panel meals that have no Nişanyan/TDK/Kubbealtı entry yet. Most
  are noise: pronouns, function words, verb stems (*bizi, sana, ancak, ederiz*).
- Pick only the content words that carry the meaning of an ayah and that a meal might render poorly: theological
  terms, Arabic loanwords, key nouns and adjectives (for S1, for example: nimet, gazap, rahman, rahim, kulluk,
  hidayet).
- Fetch them in their dictionary form, not as the truncated stem:
  ```bash
  python3 -B enrichment/v2/fetch/ref_loanword.py nimet gazap rahman rahim kulluk hidayet
  ```
- Then rebuild the index and the pack. Both refuse while an enrichment call is running (corpus.py takes
  `--force` only with the user's agreement):
  ```bash
  python3 -B enrichment/v2/tools/corpus.py build
  python3 -B enrichment/v2/pack.py --surah N --force
  ```
- Tell the user which words you fetched and which the dictionaries did not have.

**4. Estimate.**
```bash
python3 -B enrichment/v2/enrich.py build --surah N --target surah
```
- It prints the prompt size, a cost estimate from the ledger scaled by the base's word count, and the call
  directory.
- Give the user the estimate and wait for the go (rule 1).

**5. Spawn (after the go).**
```bash
python3 -B enrichment/v2/enrich.py spawn --surah N --target surah
```
- It writes the call directory (`work/sNNN/zengin.surah.opus.high/`: `prompt.md`, `started.json` with the base
  and pack hashes, `spawn.md`) and prints one JSON line per page with `"status": "prepared"`, the dir and the
  agent type. A page already started or accepted is skipped with a NOTE.
- Then one Agent tool call per prepared page: `subagent_type` `enrich-page`, `prompt` = the exact text of that
  page's `spawn.md` (read it, pass it verbatim), `model` `opus`, a short description such as `S1 surah page`. The
  agent runs in the background; wait for its completion notice. A surah page takes about 25–30 minutes.
- **`--target` is required**: `surah`, `S:A`, `ayat` (every ayah page that has a base) or `all`. Never use `all`
  or `ayat` when the user asked for surah pages. Several pages at once: at most two agents at a time unless the
  user says otherwise (a page call reads a lot of corpus).

**6. Finish (after the agent replied).**
```bash
python3 -B enrichment/v2/enrich.py finish --surah N --target surah
```
- It reads the agent's `annotations.jsonl`, finds the agent's transcript for the cost, the commands and the stop
  reason, then checks every record, renders, checks the page byte for byte, copies it to `out/sNNN/`, logs the
  errata, writes `run.log.json` and the ledger row, and prints the result line. `finish` exits 1 when a page
  fails and prints a `WARNING:` line for it; nothing is accepted then.
- `WARNING: no subagent transcript names …`: the page is finished but its cost is `None` in the ledger; report it.
- The agent's chat reply is not the deliverable; the file is. An agent that wrote no `annotations.jsonl` gives
  `call did not complete`; the call directory stays blocked; a new try is `--attempt 2` with the go.
- `enrich.py status --surah N` shows the call as started until `finish` has run; it cannot watch a spawned agent.

**7. Check and report.**
- The result line has `status`, `check`, `kept`, `dropped`, `warnings`, `errata` and `cost_usd`. Report it with the
  actual cost against the estimate.
- Read `check.json` in the call directory:
  - `dropped`: each id with its errors. List them.
  - `warnings`: show the counts and anything unusual.
  - `page_errors`: should be empty, since a page error fails the call.
- Read the page `out/sNNN/surah.md` and judge it as the user does: is each block **appropriate, to the point,
  useful, and does it flow naturally** after its paragraph? Do not audit whether the base is faithful to its
  sources.
- Report to the user:
  - blocks per type;
  - paragraphs that make a claim but got no block;
  - Arabic quotations present or missing;
  - the meal verdict;
  - errata added;
  - anything weak or repeated.

## Ayah pages (later)

- **Prerequisite:** augment9 has run on the ayah (v16 status: `python3 -B _commentary/v16/status.py N`).
- **Rebuild the pack** after augment9 has run: `pack.py --surah N --force`. It refuses while a call of the surah
  is running.
  - Pages already accepted are unaffected. Each call records the sha256 of its page's base and of pack.json; a
    finished but not yet accepted page (a trial) whose pack was rebuilt since its call is never accepted.
  - The surah base does not change, so an accepted surah page stays valid. A surah *trial* not yet accepted cannot
    be accepted after the rebuild (pack.json changes with every build): accept it before rebuilding.
  - `build`, `run` and `status` name the ayat that still have no augment9 base; they get no page.
- **Run:** `enrich.py build --surah N --target ayat` gives the estimate. There is no ayah-page calibration yet:
  estimate from the surah pages' cost per 1k base words, spawn one ayah page first (`--target N:A`), finish it,
  calibrate, then the rest.
- **Then** `enrich.py spawn --surah N --target ayat` (every ayah page with a base, each its own call directory),
  the Agent tool calls as in step 5 (two at a time), and `enrich.py finish --surah N --target ayat` for the pages
  whose agents replied (a page without a reply yet is reported as not complete; finish it later, never twice).

## Failures

| What you see | What it means | What to do |
|---|---|---|
| `call did not complete (the agent wrote no annotations.jsonl)` | the spawned agent replied without writing the records file | report; `--attempt 2` only with the user's go |
| `no subagent transcript names …` | the agent's transcript is not under `~/.claude/projects/` | the page is unaffected; the cost is None; report |
| `call did not complete (timed out …)` | killed after 8 hours | report; new attempt only with the user's go |
| `call did not complete (result error_…)` | the CLI ended the call with an error, e.g. the $40 cap per call | report it with the subtype; never raise the cap on your own |
| `call did not complete (result marked is_error)` or `(no result …)` | the CLI stopped without a usable result (e.g. a session limit) | read `stderr.log` and the end of `run.stream.jsonl`; report |
| `call did not complete (exit code …)` | CLI crash | read `stderr.log`; report; `--attempt 2` with the go |
| `status: started (running or interrupted)` and no process | the orchestrator died | report. Never rerun that directory. `enrich.py confirm-dead --surah N --dir <dir>` (it checks that no process names the directory) lets pack and index rebuilds go ahead; a new try is `--attempt 2`, with the go |
| `page errors: n` | rendering or byte check failed | read `check.json` `page_errors`; report; nothing was accepted |
| `base changed since the call` / `the pack was rebuilt since the call` | the pack was rebuilt between call and acceptance | new attempt on the new base, with the go |
| `NOTE: … predates base/pack hashing` (accept) | a call from before 2026-10-04 has no recorded hashes | the guard is skipped; say so |
| `exists (never overwrite)` | the page was accepted before | nothing; replacing it is the user's decision |
| many dropped records | the agent broke placement or schema rules | list them; the user decides between accepting as is and a new attempt |
| `gaps.json` in the call directory | the agent needed a source the corpus lacks | report; fetch, rebuild the index, new attempt only with the go |
| `permission_denials` > 0 | the agent tried something the sandbox refused | report the count; harmless if the page is good |
| `stream_unparsable` > 0 | broken lines in the call's stream | report; the tokens and cost may be undercounted |

## Trials and accepting a trial page

- **Several models on one page** (comparisons only): `enrich.py run … --model opus:high,sol61:high --trial
  --parallel 2`. A trial renders in its call directory only: nothing goes to `out/`, and no errata are logged.
- **A trial of opus:high uses the production directory** (`zengin.<page>.opus.high`): the page then counts as run.
  Accept it with `accept`; a fresh production run would need `--attempt 2`.
- **Trials are only partly blind.** A Claude call cannot read `out/` or the call directories that existed when it
  started, but it can read ones created after it (parallel runs). A Codex call has no read limits, and its sandbox
  also lets it write to /tmp.
- **Accepting a finished trial page:**
  ```bash
  enrich.py accept --surah N --target surah --model opus:high
  ```
- **A correction a trial found and the accepted page lacks** goes into `errata.jsonl` by hand: one JSON line with
  `surah`, `target`, `base`, `id` (S<sss>-DZT-<n>), `taban`, `hata`, `metin`, `kaynak`, `found_by` (the trial
  directories) and `confirmed_by` (who checked it, and against what). See the S100 muğîrât line.

## Cost reference (Opus 5.5 high, actual)

| Page | Base words | Cost | Time |
|---|---|---|---|
| S100 surah | 10,099 | $6.74 | 26 min |
| S107 surah (trial, before the cost changes) | 7,585 | $7.46 | 25 min |
| S1 ayah 1:1 (first ayah page; agent-spawned, cost from the transcript) | 6,255 | $13.97 | 45 min, 89 commands, 53 blocks |

- **Rate:** about $0.67–0.98 per 1k base words.
- **Surahs with heavy literature cost more.** S1 has about 3 MB of tafsir text, 7× S100. Expect the top of the
  range or above.
- **Cap:** $40 per call (`--max-budget-usd`).
- **The ledger** (`work/ledger.jsonl`) has one row per call: model, effort, tokens, `cost_usd`, `base_words`,
  `base_sha256`, `pack_sha256`, `seconds`, status. `enrich.py build` reads it for its estimate, and adds what failed
  calls of the same kind cost.
- **Ayah pages:** the first one (1:1) cost $2.23 per 1k base words, about 2.5x the surah rate: an ayah page carries
  the whole literature of one ayah. `build` now estimates ayah pages from it.

## Corpus maintenance

```bash
python3 -B enrichment/v2/tools/corpus.py import-local          # sources already on this machine
python3 -B enrichment/v2/fetch/<fetcher> …                      # new sources (meals, OpenITI, Elmalılı, references)
python3 -B enrichment/v2/tools/corpus.py build                 # one index: enrichment/corpus/corpus.sqlite
python3 -B enrichment/v2/tools/corpus.py sources               # what is local, what is a memory pointer
python3 -B enrichment/v2/tools/schema_doc.py                   # after any schema.json change
```
- Rebuild the index only while no enrichment call is running (`corpus.py build` refuses otherwise).
- `corpus.py build` prints a WARNING for a non-memory source without `segments.jsonl`; fetchers print
  `FETCH FAILED` / `WARNING` lines for whatever they could not get. Report them.
- Hadith: only Bukhārī, Muslim and the graded sunan carry a `sahih` grade in the corpus. Ibn Ḥibbān and Musnad Aḥmad
  are ungraded, so a `tur:hadis` block citing them is dropped.

## The Bible pass (tevrat, incil): built 2026-10-04 evening, not yet run

A separate pass over the same frozen base, after the Islamic page of a target exists or beside it: one call per
page writes blocks of gelenek `tevrat` or `incil` (schema 3.1 types paralel, motif, karsi_anlati, soydas,
yorum_gelenegi, plus the shared types), each with `bag`, `tarihleme` and `nusha`. The passes never read each other's
records; `merge` lays the layers after each paragraph: islami, then tevrat, then incil.

**Corpus (kind `intertext`, its own index, never in the Islamic one):**
- WLC (Hebrew Bible, Masoretic, 23,213 verses, `WLC:Gen.22.2`), SBLGNT (Greek New Testament, 7,939 verses,
  `SBLGNT:Matt.6.5`), KJV (English aid with the Apocrypha, 36,822 verses, `KJV:Ps.1.3`): fetched once by
  `python3 -B enrichment/v2/fetch/bible_text.py all` (cached in raw/; open licences recorded in source.json).
- SEFARIA (Targum, Talmud, midrash, classical Jewish commentary, by reference, on demand):
  `python3 -B enrichment/v2/fetch/bible_sefaria.py related "Genesis 22:2" --n 6` or `text "<ref>" …`.
- CORPUSCORANICUM-INTERTEXT (Corpus Coranicum's intertext entries for the surahs fetched: 1, 22, 87–114).
- The index: `python3 -B enrichment/v2/tools/corpus.py --intertext build` (the flag before every subcommand:
  `--intertext search 'בראשית ברא'`, `--intertext get WLC:Gen.22.2`, `--intertext ayah 1:1`). It holds the
  intertext sources plus the Quran text and the shared reference sources. It refuses to rebuild while a Bible-pass
  call is running (`--force` only with the user's word); Islamic-pass calls do not block it.
- Not in the corpus yet: the Peshitta, the Septuagint, patristic and Syriac texts, a Turkish Bible (no open one
  exists online). The brief tells the agent to mark such material as memory and to list it in gaps.json.

**Step by step, for surah N (each step its own go; no agent without a go):**
1. **Discovery** (GPT through Codex; the only scripted calls): per ayah with a reading and per image section, Luna
   max and Terra max name the texts the commentary activates (brief `_commentary/v16/prompts/discover/bible.md`:
   six-field TSV with tradition, kind, reference), two turns each (the brief, then the fixed missing-texts
   follow-up), merged into `_commentary/v16/out/sNNN/discovery_bible/<S_A | secK>.merged.tsv`:
   ```bash
   python3 -B _commentary/v16/discover_bible.py --surah N                   # packages and prompts, no call
   python3 -B _commentary/v16/discover_bible.py --surah N --go              # S1: 7 ayat + sections, x2 models
   python3 -B _commentary/v16/discover_bible.py --surah N --merge --prefetch  # lists + Sefaria texts for them
   python3 -B enrichment/v2/tools/corpus.py --intertext build
   ```
   `--prefetch` fetches, for every Tanakh verse named, its Targum, midrash, Talmud and commentary links (six per
   type by default), and every named Jewish text; failures are printed (a text Sefaria lacks is a gap). Without a
   discovery run the page agent works from the corpus and its own search; the job header says so.
2. **Pack:** the same pack as the Islamic pass (`pack.py --surah N`); the ayah base is the augment9 reading.
3. **Build, spawn, finish**, exactly as for the Islamic page but with `--pass ehlikitap` before the command:
   ```bash
   python3 -B enrichment/v2/enrich.py --pass ehlikitap build  --surah N --target 1:1
   python3 -B enrichment/v2/enrich.py --pass ehlikitap spawn  --surah N --target 1:1   # then the Agent tool, enrich-page
   python3 -B enrichment/v2/enrich.py --pass ehlikitap finish --surah N --target 1:1
   ```
   Call dirs `work/sNNN/ehlikitap.<page>.opus.high/`; pages `out/sNNN/<page>.ehlikitap.md` (the Islamic page keeps
   `<page>.md`); the validator runs with `--pass ehlikitap` (records must carry tevrat or incil; sources resolve
   in the intertext index; Islamic sources are refused). The brief: `prompts/ehlikitap.md` (new, 2026-10-04;
   common.md holds with its rule 6 reversed, as the brief says). No cost calibration yet: the first page calibrates.
4. **Merge:** `python3 -B enrichment/v2/enrich.py merge --surah N --target 1:1` writes `out/sNNN/<page>.merged.md`
   from the accepted pages of both passes (whichever exist); it never touches the accepted pages.

**Order for a surah:** Islamic pass first or the Bible pass first makes no difference to the records (they never
meet before the merge); run the Bible discovery while the Islamic pages run. Report every WARNING of the
discovery (rows outside the schema, failed fetches) and of the finish step as always.
