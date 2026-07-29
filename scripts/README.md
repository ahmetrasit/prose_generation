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
- `branch_inventories` from the surah `full_context_packet.json`, scoped by the
  builder to roots this ayah can justify;
- `v12_reader_responses` as an explicit retired/absent coverage field; per-ayah
  focus-run responses are no longer consumed by the default commentary lane;
- `v12_focus_trace_hermetic` from `../latent_activation/focus_trace/runs/` when
  generated for the surah, carrying a reconstructed focus-only baseline,
  context-triggered deltas, and surprise-preserving outliers. If only packets
  exist, coverage records `packet_present: true` while `present` remains false
  until reader responses are generated. Focus Trace preserves split-root
  identity with `mapped_root_id` + `branch_id`;
- the per-ayah excerpt of each `reader_s{NNN}_{a,b}_ayah_walk.md` (Activated
  readings + Retrospective surprises, plus the separate Turkish Prose Synthesis
  block where the reader's file has one);
- the per-ayah excerpt of the plus/minus-5 / 11-ayah reader walk family under
  `v12-tr-11ayah/`, kept separately as `v12_reader_walks_wide`;
- the compact final v12 cross-run publication row for the ayah, under
  `v12_cross_run_publication`, reconciled upstream from the regular and
  plus/minus-5 reader families;
- the per-ayah line of the whole-surah `{NNN}-0-{N}-butuncul-okuma.md`;
- every row of `focus_{S}_{A}_cutoff_100.tsv` — **unfiltered**, all four labels;
- `channel_subchannels_anchored_here` — the subchannels from the surah's
  `network/v3` review whose ayah anchors include this ayah, each carrying its
  parent channel's invariant so the block reads on its own;
- `channel_generated_outputs` — a lightweight manifest of generated network-v3
  channel candidate, family, branch-inventory, and semantic-path files available
  in `quran-data`; contents are not inlined because they can be large, but an
  agent with file access may read only the listed files when channel detail is
  necessary;
- a mandatory `coverage` block: per source, present/missing, with counts or a
  note explaining absence.

Run without `--ayah`, it also emits `{surah}.surah.json`, which references the
ayah bundle filenames rather than duplicating them and carries surah-scope
material with no single-ayah home: every Quran-text row for the surah including
the `S:0` basmalah, the full whole-surah reading, and a coverage rollup.

### Branch inventories: focus run, else surah packet

The default commentary lane does not consume per-ayah `focus_{S}_{A}/` packets.
It uses the surah's `full_context_packet.json`, which exists for all 114 surahs,
then scopes that inventory to roots this ayah can justify. Roots occurring in
the ayah keep all branches; roots cited by channel material anchored here keep
only the cited branches. Coverage records `scope:
"surah-fallback-scoped-to-ayah"` and the scoping report.

Before this fallback/scoping path existed the builder emitted a bundle with
`branch_inventories: {}` for most surahs and exited 0 — a healthy-looking bundle
with none of the latent material the commentary exists to render. If **no**
branch source resolves, the run now aborts.

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

Missing **optional** sources — a retired v12 focus-reader response set, a
reader's ayah-walk entry, a plus/minus-5 reader-walk entry, the cross-run
publication row, the whole-surah reading line, the inter-ayah TSV, the channel
review — are recorded in `coverage` with `present: false` and a note; the run
continues. The retired v12 response set is a first-class fact the writer must be
able to state, not a silent gap.

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

## instantiate.py

Assembles hermetic prompt files from the generated bundles plus the commentary
task and governing documents. A changed bundle does not reach an agent until
this stage is run.

### Run it

```sh
# Base ayah prompts for a whole surah
python3 scripts/instantiate.py --surah 100 --layer ayah --language tr --date 2026-07-27

# One active v2 pilot prompt
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.6-sol-high --language tr --date 2026-07-27

# Comparator profiles, when needed
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.5-high --language tr --date 2026-07-27
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.6-sol-max --language tr --date 2026-07-27
```

Without `--profile`, outputs are named like `{S}_{A}.ayah.prompt.md` and
`{S}_{A}.ayah.manifest.json`. With `--profile`, the profile label is appended:
`{S}_{A}.ayah.v2.5.6-sol-high.prompt.md` and matching manifest.

The current reader-facing S100 pilot default is `v2.5.6-sol-high`. Keep only that
profile prompt in the active `_commentary/inputs/s{NNN}/` path; archive
comparator prompts under `_commentary/inputs/archive/s{NNN}/` after use.
