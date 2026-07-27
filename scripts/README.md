# scripts/

Shared tooling for the two commentary levels. Layer 1 has its own builder under
`_translation/v1/tools/`.

## build_bundle.py

Assembles the input bundle consumed by `_ayah_commentary/PROMPT.md` (layer 2) and
`_surah_commentary/PROMPT.md` (layer 3). Governed by `COMMENTARY_SPEC.md` §6;
sources, formats, and gotchas in `docs/SOURCES.md`; output shape in
`bundles/schema.json`.

### Run it

```sh
# One ayah bundle
python3 scripts/build_bundle.py --surah 103 --ayah 1

# Every ayah bundle for the surah, plus the surah-level bundle
python3 scripts/build_bundle.py --surah 103

# Custom output directory (default is bundles/s{NNN}/)
python3 scripts/build_bundle.py --surah 103 --out /tmp/some_dir
```

Requires Python 3 standard library, plus either the `zstandard` pip package or a
`zstd` binary on `PATH` (falls back to `/opt/homebrew/bin/zstd`). Nothing else is
shelled out to: `.gz` is read with stdlib `gzip`, QAC morphology is queried with
stdlib `sqlite3` against a decompressed temp file.

### What it emits

For each numbered ayah of the surah — basmalah `S:0` rows get no ayah bundle,
matching the v12 run layout, which has no `focus_{S}_0`:

`{surah}_{ayah}.ayah.json`, containing

- the Arabic text of the ayah;
- full `qac_morphemes` rows, ordered by word_index/morpheme_index;
- the complete word-analysis record — every `words[]` entry, every `prose`
  string, every `topics[]` entry;
- `branch_inventories`, verbatim, from each variant's v12 **stage_00** input
  packet (scoped to the focus ayah's own roots, before any neighbour is
  revealed);
- v12 reader responses — all readers, all stages, complete objects — when
  present;
- the per-ayah excerpt of each `reader_s{NNN}_{a,b}_ayah_walk.md` (Activated
  readings + Retrospective surprises, plus the separate Turkish Prose Synthesis
  block where the reader's file has one);
- the per-ayah line of the whole-surah `{NNN}-0-{N}-butuncul-okuma.md`;
- every row of `focus_{S}_{A}_cutoff_100.tsv` — **unfiltered**, all four labels;
- `channel_subchannels_anchored_here` — the subchannels from the surah's
  `network/v3` review whose ayah anchors include this ayah, each carrying its
  parent channel's invariant so the block reads on its own;
- a mandatory `coverage` block: per source, present/missing, with counts or a
  note explaining absence.

Run without `--ayah`, it also emits `{surah}.surah.json`, which references the
ayah bundle filenames rather than duplicating them and carries surah-scope
material with no single-ayah home: every Quran-text row for the surah including
the `S:0` basmalah, the full whole-surah reading, and a coverage rollup.

### Branch inventories: focus run, else surah packet

Per-ayah `focus_{S}_{A}/stage_00_*.json` packets exist for six ayahs in the whole
corpus. When none exists, the builder falls back to the surah's
`full_context_packet.json`, which exists for all 114 surahs and carries the same
`branch_inventories` structure.

The scope differs and coverage says so: `scope: "surah"`, a variant keyed
`full_context_packet`, and a note that it covers every root in the surah rather
than only this ayah's roots and carries no staged reveal order.

Before this fallback existed the builder emitted a bundle with
`branch_inventories: {}` and exited 0 — a healthy-looking bundle with none of the
latent material the commentary exists to render. If **no** branch source resolves,
the run now aborts.

### Channel review

Each surah's `network/v3/reviews/s{NNN}/reader_a_pilot.md` is parsed into parent
channels and subchannels. The surah bundle carries the whole parsed review; each
ayah bundle carries the subchannels anchored to that ayah.

Coverage records `review_status: "first-pass-single-reader"`. This is not an
adjudicated ledger — no accept/reject, no second reader, no per-ayah maturity —
so it is evidence for a writer, not authority to state a channel as established.
See `docs/CHANNELS.md` §5.1. Absent for S108, S110, S113, S114.

### Why unfiltered

The inter-ayah label axis measures marginal contribution, not reality. Filtering
at `strong` silently deletes distributed findings. The bundle carries all four
labels and the writer orders with the axis rather than filtering on it —
`PRINCIPLES.md` §9.

### v12 reveal-order variants

If a focus dir contains `left_first/`/`right_first/` subdirectories, both are kept
and labelled separately under `branch_inventories` / `v12_reader_responses`
(keyed `"left_first"` / `"right_first"`). A flat focus dir is keyed `"default"`.
`pilot_invalid_prompt_leak/` directories are excluded unconditionally, wherever
they appear.

### Fail loud vs. degrade gracefully

Missing **required** sources — Quran text, word-analysis record, QAC morphemes,
or branch inventories from *either* a focus packet or the surah packet — raise
`RequiredSourceMissing` and abort with a non-zero exit code. These are
structurally expected to exist for every canonical numbered ayah.

Missing **optional** sources — v12 reader responses, a reader's ayah-walk entry,
the whole-surah reading line, the inter-ayah TSV, the channel review — are
recorded in `coverage` with `present: false` and a note; the run continues. A
missing v12 response set is a first-class fact the writer must be able to state,
not a silent gap.

The distinction matters: an optional source that goes missing should degrade the
bundle *visibly*. Two sources were failing silently before 2026-07-27 — branch
inventories (110 surahs) and the whole-surah reading (15 of the 30 that exist,
via a zero-padding mismatch in the filename glob).

### Verified output

Measured counts for S103 are recorded in `STATUS.md`.

## Not in the bundle by design

The Furuq/V4 lexicon, the QAC↔V4 bridge, and grammar attachments/contextual
profiles are documented in `docs/SOURCES.md` but not carried: branch data comes
from the v12 packets (themselves built from furuq's `branch_images` filtered to
`status='accepted'`), and grammar attachments are already folded into
word-analysis `prose`/`topics[]` via `evidence_checked` tags.

Revisit if a writer needs branch `status` or bridge `match_status` directly, or
if channel work needs review-status branches. `docs/SOURCES.md` §7 names the
tables to start from.
