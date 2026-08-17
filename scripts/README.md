# scripts/

Shared tooling for the two commentary levels. Layer 1 has its own builder under
`_translation/v1/tools/`.

## build_bundle.py

Assembles the full, auditable base bundle. Layer 2 does not instantiate this
bundle directly: `tier_branch_payloads.py` creates the production Layer-2
projection first. Governed by `COMMENTARY_SPEC.md` §6; sources, formats, and
gotchas in `docs/SOURCES.md`; output shape in `bundles/schema.json`.

### Run it

```sh
# One ayah bundle
python3 scripts/build_bundle.py --surah 103 --ayah 1

# Every ayah bundle for the surah, plus the surah-level bundle
python3 scripts/build_bundle.py --surah 103

# Default build includes and requires Hermetic Focus Trace
python3 scripts/build_bundle.py --surah 100

# Explicit no-HFT build; coverage records the intentional exclusion
python3 scripts/build_bundle.py --surah 100 --exclude-focus-trace

# Use one labelled HFT response for a comparison run
python3 scripts/build_bundle.py --surah 100 --ayah 1 --focus-trace-variant 5.5-high

# Custom output directory (default is bundles/s{NNN}/)
python3 scripts/build_bundle.py --surah 103 --out _commentary/work/some_dir
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
- `v12_focus_trace_hermetic`, required by default unless
  `--exclude-focus-trace` is passed, carrying Hermetic Focus Trace packet
  summaries and reader JSONs from `../latent_activation`;
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
- `root_lexicon` — Turkish dictionary/gloss entries for roots in the ayah.
  QAC roots are mapped to Furuq `root_XXXXXX` IDs through
  `data/bridges/qac-furuq-v4-root-map.sqlite.gz` when present, with
  `full_context_packet.json` as fallback. Dictionary/gloss branch arrays are
  kept in full. If a QAC root has split Furuq targets, the non-dominant targets
  are included as additional root entries and recorded in coverage. If multiple
  QAC roots map to the same Furuq target, the shared root entry records all
  source roots in `qac_roots_ar` / `qac_root_mappings`;
- a mandatory `coverage` block: per source, present/missing, with counts or a
  note explaining absence.

Run without `--ayah`, it also emits `{surah}.surah.json`, which references the
ayah bundle filenames rather than duplicating them and carries surah-scope
material with no single-ayah home: every Quran-text row for the surah including
the `S:0` basmalah, the full whole-surah reading, and a coverage rollup.

`build_bundle.py` deliberately leaves the base ayah bundle pretty-printed and
its `root_lexicon` branch arrays full. Run `tier_branch_payloads.py` before
`instantiate.py`; the instantiator then compacts the tiered JSON while inlining
it and records both `source_bytes` and `inlined_bytes` in the manifest.

### Branch inventories: focus run, else surah packet

The default commentary lane does not consume per-ayah `focus_{S}_{A}/` packets.
It uses the surah's `full_context_packet.json`, which exists for all 114 surahs,
then scopes that inventory to roots this ayah can justify. Roots occurring in
the ayah keep all branches; roots cited by channel material anchored here keep
only the cited branches. Coverage records `scope:
"surah-fallback-scoped-to-ayah"` and the scoping report.

This is separate from `root_lexicon`. Branch inventories remain the compact
branch map and are ayah-scoped here. The base bundle keeps every Turkish
dictionary/gloss branch for every included Furuq root target, including
non-dominant targets of split QAC roots. The required pre-L2 tierer does not
change `branch_inventories` and does not remove any root or dictionary branch
identity.

Before this fallback/scoping path existed the builder emitted a bundle with
`branch_inventories: {}` for most surahs and exited 0 — a healthy-looking bundle
with none of the latent material the commentary exists to render. If **no**
branch source resolves, the run now aborts.

### Hermetic Focus Trace

Hermetic Focus Trace is required by default even though it reads a sibling
generation workspace, `../latent_activation/focus_trace`, instead of the frozen
`quran-data` source root. The builder probes both run directory spellings
(`runs/s012` and `runs/s12`) and fails if both contain material for the same
target ayah. Use `--exclude-focus-trace` only for an intentional no-HFT build;
coverage records that exclusion.

If multiple HFT responses exist for the same ayah, `--focus-trace-variant`
selects one filename variant. The unlabelled file is `default`; a file named
`100_1.5.5-high.focus_trace.json` is variant `5.5-high`.

Layer 2 treats this as reconstructed before/after evidence:
`baseline_models`, `context_deltas`, and `surprising_valid_outliers`. It is not
labelled as a staged `stage_00` / `stage_01` transcript.

### Reviewed channels

Each surah's reviewed `network/v3` report is parsed into parent channels and
subchannels. The ordinary surah bundle carries that parsed source; the compact
channel bundle preserves its synthesis and compiles root/branch citations to
typed Quran anchors. Maturity is absent upstream because it belongs to reader
order and is derived by the combined Layer 3 + 2.5 pass. Reviewed channel reports
are absent for S108, S110, S113, and S114.

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

## tier_branch_payloads.py

This is the required pre-Layer-2 step for new production prompts. It reads one
full ayah bundle, collects explicit branch interest from HFT activation traces,
cross-run anchors, regular/wide reader walks, channel review blocks,
`word_analysis`, inter-ayah rows, and whole-surah reading text, then writes a
separate bundle. It never overwrites its input.

```sh
# One ayah: validate and inspect projected compact size
python3 scripts/tier_branch_payloads.py bundles/s100/100_1.ayah.json --check

# One production Layer-2 bundle
python3 scripts/tier_branch_payloads.py bundles/s100/100_1.ayah.json \
  --output bundles-layer2/s100/100_1.ayah.json --compact-output

# Whole surah
mkdir -p bundles-layer2/s100
for bundle in bundles/s100/*.ayah.json; do
  python3 scripts/tier_branch_payloads.py "$bundle" \
    --output "bundles-layer2/s100/$(basename "$bundle")" --compact-output
done
```

Payload tiers are recorded in `coverage.root_lexicon.branch_policy` and on each
projected branch:

- `explicit_interest`: full branch payload except `what_is_not_ar` and
  `identity_judgment.boundary_note`;
- `local_low_branch_safety`: B001/B002 branches not already explicit, retaining
  identity, Arabic image/definition, status, branch kind, and reviewed or
  dictionary concept/context gloss text;
- `compact_rest`: identity, Arabic image/definition, and status, with a semantic
  fallback only when both Arabic semantic fields are empty.

Every dominant and non-dominant root target remains. Every dictionary branch
reference remains. Compact reviewed-gloss records remain as branch-reference
stubs. `branch_inventories`, `word_analysis`, reader evidence, inter-ayah data,
and all other non-branch fields are unchanged.

Tier names are storage contracts, not finding ranks or prose budgets. A compact
branch may support a significant finding, and an explicit branch creates no
automatic prose obligation. Prose length and selection remain governed by the
single canonical ayah-commentary prompt profile; Layer 2 retains every distinct
anchored surprise with reader payoff and rejects only repetition, fluff, or
material that does not change understanding. The admission threshold is
identical for sparse and dense ayat; root count never reduces the explanatory
space available to a qualifying finding.

The transform fails non-zero on a missing input, invalid JSON, missing required
field, coverage/payload contradiction, missing HFT, malformed or unresolved
branch citation, duplicate/gloss-only branch reference, missing status, or a
branch with no usable semantic payload. Source-path strings inside a hermetic
bundle are provenance, not files this step rereads; the inlined payload is the
source of truth.

## instantiate.py

Assembles hermetic prompt files from the tiered Layer-2 bundles plus the
commentary task and governing documents. New Layer-2 runs must pass the tiered
directory with `--bundles-dir`; do not point this command at the full base
bundle directory.

The active ayah-commentary task source is `_ayah_commentary/v2/PROMPT.md`.

Prompt files are immutable snapshots. Regenerate them after every base-bundle,
tiered-bundle, or HFT response change; do not rely on an existing prompt
filename to imply freshness. For focused pilots, verify the prompt itself
contains `v12_focus_trace_hermetic`, `baseline_models`, `context_deltas`,
`surprising_valid_outliers`, and at least one reader before sending it to a
model.

### Run it

```sh
# Base ayah prompts for a whole surah
python3 scripts/instantiate.py --surah 100 --layer ayah --bundles-dir bundles-layer2 --language tr --date 2026-07-27

# One focus-aware canonical prompt
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir bundles-layer2 --profile v2.5.6-sol-high --language tr --date 2026-07-27

# Comparator output labels, when needed. These labels use the same prompt
# contract; they only create separate filenames/manifests for model runs.
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir bundles-layer2 --profile v2.5.5-high --language tr --date 2026-07-27
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir bundles-layer2 --profile v2.5.6-sol-max --language tr --date 2026-07-27
```

Without `--profile`, outputs are named like `{S}_{A}.ayah.prompt.md` and
`{S}_{A}.ayah.manifest.json`. With `--profile`, the comparator label is
appended: `{S}_{A}.ayah.v2.5.6-sol-high.prompt.md` and matching manifest.

The normal comparator labels (`v2.5.5-high`, `v2.5.6-sol-high`, and
`v2.5.6-sol-max`) all use the active task from
`_ayah_commentary/v2/PROMPT.md` plus the canonical `v2.5.6-sol-high` rendering
profile. Do not tailor prompt instructions to a model name
or reasoning level; vary only the runtime model/reasoning configuration outside
the prompt.

For S12/S18/S5 focused production refreshes, rebuild each pericope span with
`build_bundle.py`, project each ayah through
`tier_branch_payloads.py --compact-output`, then instantiate from
`bundles-layer2` with `--require-focus-trace`. Source spans live under
`bundles/s012-pericopes/`, `bundles/s018-pericopes/`, and
`bundles/s005-pericopes/`; the production prompt inputs live under
`bundles-layer2/s012`, `bundles-layer2/s018`, and `bundles-layer2/s005`.
The repeated HFT checks are part of the contract: build fails on missing focus
trace readers, tiering fails on missing HFT or malformed required evidence, and
instantiation fails if a tiered bundle has lost HFT readers. Optional source
absence must appear in coverage; it should not be silently erased.

### Combined Layer 3 + Layer 2.5

```sh
python3 scripts/build_channel_bundle.py --surah 87
python3 scripts/check_channel_bundle.py bundles/s087/87.channel.json --surah 87
python3 scripts/instantiate_channel.py --surah 87 \
  --layer2-label default.v2.5.6-sol-high --date 2026-07-28
```

The bundle begins with the reviewed network channel material, retains its
synthesis, and deterministically joins every cited root/branch/motif to typed QAC
anchors. The instantiator then adds only each ayah's unchanged Layer-2 prose.
It does not reload Layer-2 evidence/index files, raw ayah bundles, per-ayah
coverage, or the whole-surah `butuncul_okuma`.

The single authored pass writes the primary-grounded surah argument, completed
surprising channel reading, reviewed channel plan with maturity, and Layer-2.5
overlays. There is no second channel-admission pass. The cold Layer-2 prose
remains canonical; overlay JSON records additions and exact insertion points.

`--layer2-dir` defaults to `_commentary/outputs/s{NNN}-default`, then `s{NNN}`.
`--layer2-label` disambiguates comparative runs. Missing, empty, or ambiguous
prose aborts before prompt creation.

Validate the authored structures:

```sh
python3 scripts/check_channel_plan.py \
  _commentary/outputs/s087-default/87.surah.channels.reviewed.json \
  --state reviewed --bundle bundles/s087/87.channel.json
python3 scripts/check_channel_overlays.py _commentary/outputs/s087-default/87.ayah-channel-overlays.json \
  --plan _commentary/outputs/s087-default/87.surah.channels.reviewed.json
```

The older `instantiate.py --layer surah` and
`instantiate_channel_workflow.py --stage review|integrate|finalize` commands
remain only for reproducing legacy draft-plan runs.
