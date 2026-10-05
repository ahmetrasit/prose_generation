# Bible pathway after v16

This is the independent Bible enrichment implementation. Its helpers, prompts,
schema, source cache, index, packs, ledgers and outputs all live in this directory.
It imports no shared enrichment or v16 Python helpers. The old shared
`enrichment/v2/enrich.py --pass ehlikitap` commands are superseded **for Bible work
only**; the other enrichment workflow is unchanged.

The only upstream reads are completed v16 commentary, the optional frozen input
pack selected by the operator, the initial corpus seed, and accepted Islamic pages
when explicitly assembling a combined page. Combined pages are written here.
The Bible author never reads the Islamic enrichment pages or call directories.

## Texts and evidence

- WLC is the primary Hebrew Bible witness (including Torah). Its main text is the
  written/ketiv stream. Qere and other notes retain their word positions in
  `variant_notes`; they are never extra words inserted into the verse.
- SBLGNT is the primary Greek New Testament witness. These are identified editions,
  not claims to possess lost original manuscripts.
- Search Hebrew with `--src WLC` and Greek with `--src SBLGNT`. Pointing and accents
  are normalized for search; returned text preserves them. Search matches word
  prefixes, not roots or lemmas. Check inflected forms and surrounding verses.
- English KJV is a finding aid. A canonical Bible parallel cannot be accepted with
  KJV as its only textual witness. Match the actual Hebrew/Greek edition's verse
  numbering; English and Hebrew numbering are not assumed identical.
- Jewish interpretation is fetched through the Bible-owned Sefaria importer.
  Corpus Coranicum supplies selected contextual passages and editorial information.
  Tradition is assigned per segment, not per mixed collection. Background material
  is restricted to scholarship, source notes and method notes.
- `nusha` identifies the cited witness. Use `tercume` for an explicitly identified
  translation; `uygulanmaz` is for background/method notes without a scriptural
  witness. An available original witness must support a claimed textual reading.
- Full Peshitta, Septuagint and patristic collections are not currently present.
  Some Syriac excerpts occur in Corpus Coranicum. Explicitly record unavailable
  witnesses and untranslated/unverified candidates in `gaps.json`.

## 1. Prepare the Bible-owned corpus and frozen commentary

Run from the repository root with Python 3.10+ and `requests`; SQLite must support
FTS5. The setup used here was checked with Python 3.14.

```sh
python3 -B enrichment/bible/corpus.py seed
python3 -B enrichment/bible/fetch/bible_text.py wlc
python3 -B enrichment/bible/corpus.py build
python3 -B enrichment/bible/pack.py --surah 1
```

`seed` copies eligible cached sources once from `enrichment/corpus`; existing
Bible-owned sources are retained. The WLC step reparses the cached XML with the
correct variant handling. On a checkout without the bulk originals, run
`python3 -B enrichment/bible/fetch/bible_text.py all` before indexing (downloads).

`pack.py` freezes its own copies directly from completed v16 r13 surah output and
augment9 ayah output. When multiple outputs exist, explicitly select an existing
frozen pack with `--from-pack PATH`. For example, the verified S1 setup used
`--from-pack enrichment/v2/work/s001/pack`; that source pack is read-only.
Missing augment9 ayah bases are recorded and cannot produce ayah pages.

Pack rebuilds are refused while any Bible discovery or page call is active. Source
mutation and index rebuilds are refused while a Bible page call is active. Frozen
input hashes are checked again before acceptance. `--force` on `pack.py` replaces
only the Bible pack and does not bypass the active-call guard.

## 2. Prepare and complete native discovery

```sh
python3 -B enrichment/bible/discovery.py --surah 1 --run-tag pilot1 --targets 1:1,surah
```

This writes packages and prompts, with **no model calls**. `1:1` uses the full frozen
augment9 ayah text; `surah` selects every image section of the frozen surah text.
The configured discovery readers remain Luna max and Terra max. Their exact model
identifiers are in `discovery.py`; the runner must provide them. Do not silently
substitute another model. Use a unique native task name for every session.

For each prepared target and model:

```sh
python3 -B enrichment/bible/discovery_native.py start --surah 1 --run-tag pilot1 --target 1:1 --model luna --task bible_pilot1_1_1_luna
```

An orchestrator launches the native agent with the exact generated `spawn.md`,
using an independent context and the specified model/effort. After its first turn:

```sh
python3 -B enrichment/bible/discovery_native.py snapshot --surah 1 --run-tag pilot1 --target 1:1 --model luna
```

Deliver the generated `followup.txt` to **that same session**. It writes new
proposals to `followup.tsv` without modifying `list.tsv`. After the second turn:

```sh
python3 -B enrichment/bible/discovery_native.py audit --surah 1 --run-tag pilot1 --target 1:1 --model luna
python3 -B enrichment/bible/discovery_native.py finish --surah 1 --run-tag pilot1 --target 1:1 --model luna --reviewed
```

Before passing `--reviewed`, inspect `tool_calls.json` for adherence to the supplied
inputs and the no-retrieval/no-other-agents rules. The flag is an operator audit
attestation. Finish verifies the session model and effort, two completed turns,
follow-up delivery, frozen inputs and first-turn bytes. It consolidates unique
proposals, preserving distinct reasons and link kinds. An empty delivered TSV is
valid; a missing TSV, overwritten first turn or failed session is not.

Raw discovery uses exactly six tab-separated fields: strength, tradition, kind,
reference, basis, explanation. Bible references must name their edition, e.g.
`WLC:Gen.22.2` or `SBLGNT:Matt.6.5`, and resolve in the local index. Named secondary
works may be proposed for prefetch. These are candidates, not verified evidence.

## 3. Merge discovery, prefetch, rebuild the index

After both readers complete all selected targets:

```sh
python3 -B enrichment/bible/discovery.py --surah 1 --run-tag pilot1 --targets 1:1,surah --merge --prefetch
python3 -B enrichment/bible/corpus.py build
```

The merge accepts only successful audited runs. It emits individual handoffs and
a real `surah.merged.tsv` after all surah sections complete. `selected.json`
explicitly selects each page's handoff; there is no implicit legacy fallback.

Prefetch records candidate resolution, fetched locators, missing texts, retrieval
errors, list hashes and source hashes in `prefetch.json`. Errors block page start.
Unavailable secondary works remain explicit coverage gaps; the author must record
them. HTTP failures are retried on a later prefetch instead of becoming permanent
cached failures. Build the Bible index after all prefetch operations and before
starting any page authors. Run the merge/prefetch command for the complete set of
pages you intend to use together, since the report covers the selected set.

## 4. Write, validate and accept a Bible page

```sh
python3 -B enrichment/bible/enrich.py build --surah 1 --target 1:1
python3 -B enrichment/bible/enrich.py spawn --surah 1 --target 1:1
```

`build` reports preflight readiness and a cost estimate based solely on previous
Bible calls. Initially there is no calibration. `spawn` requires a matching
discovery handoff, completed prefetch, current index manifest and unchanged pack;
it writes a native page-agent brief, **without calling a model**.

The page author is the configured native Claude Opus agent at high effort. Use a
general-purpose native agent with the exact `spawn.md`; no shared agent definition
or hook is required. A single completed native transcript is mandatory. Missing
transcripts, mixed models and tool use outside the Bible call rules reject the
result. Accounting uses the Bible-local nominal rate snapshot; it is not a billing
quote. No legacy model CLI fallback is provided.

The agent writes `annotations.jsonl` and `gaps.json`, validates records, and renders
a preview inside its call directory. IDs are `S001-TEV-PRL-001` or
`S001-INC-MTF-001`, using the schema's actual type codes. After completion:

```sh
python3 -B enrichment/bible/enrich.py finish --surah 1 --target 1:1
```

Invalid records are reported and dropped. A result with every record dropped is a
failure. An intentionally empty page requires `gaps.json.no_findings_reason`.
Acceptance writes the page, an immutable copy of kept annotations and provenance
to `enrichment/bible/out/s001/`; accepted pages are never overwritten. Native
transcripts and local checks are retained in the Bible call directory.

Use `--trial` on finish to keep the result only in its call directory. A trial is
not an accepted page; the CLI currently has no trial-promotion command. Do not
start the same call twice. `--attempt 2` is a separate, explicitly chosen attempt.

## 5. Optional combined page

```sh
python3 -B enrichment/bible/enrich.py merge --surah 1 --target 1:1
```

This reads the accepted Islamic page, if present, and the accepted Bible page. It
requires identical frozen bases, verifies page/snapshot hashes and rejects
duplicate IDs. Legacy Islamic annotations are used only if they reproduce the
accepted page exactly. Accepted source descriptions are preserved. The combined
page and its provenance are written only to `enrichment/bible/out/`; the manifest
marks a page containing only one layer as partial. No publication is performed.

## Verification

```sh
python3 -B -m unittest enrichment.bible.test_workflow -v
```

The tests use temporary packs, indexes, annotations and mocked fetches. They do
not call models, fetch online texts or write shared enrichment data. See
`READINESS_2026-10-05.md` for the current verified state and remaining live work.
