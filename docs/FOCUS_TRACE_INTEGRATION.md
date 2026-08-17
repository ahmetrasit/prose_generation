# Hermetic Focus Trace Integration

Hermetic Focus Trace is an upstream workflow in
`../latent_activation/focus_trace/`. Production run directories are zero-padded:
`runs/s012`, not `runs/s12`. It recovers the useful part of the retired
per-ayah focus runs: an ayah read first on its own, then read again as later
ayat activate surprising latent possibilities.

It is cheaper than strict staged focus runs. The reader receives one sealed
packet and writes one JSON response. That means it is a reconstructed trace, not
a blind reveal transcript. Layer 2 must label and use it accordingly.

## Bundle Opt-In

The default commentary bundle does not read `../latent_activation`. To add
Hermetic Focus Trace, build the ayah bundles explicitly:

```sh
python3 scripts/build_bundle.py --surah 100 --include-focus-trace
python3 scripts/build_bundle.py --surah 100 --require-focus-trace
python3 scripts/build_bundle.py --surah 100 --ayah 1 --require-focus-trace --focus-trace-variant 5.6-sol-high
```

Use `--include-focus-trace` while packets exist but reader JSON may still be
missing. Use `--require-focus-trace` for the final focused Layer-2 run; it fails
preflight unless every target ayah has a reader response.

Use `--focus-trace-variant` to select one labelled response for a comparison
run. The unlabelled file is variant `default`; for example
`100_1.5.6-sol-high.focus_trace.json` is variant `5.6-sol-high`.

The full bundle from `build_bundle.py` is an auditable source artifact, not the
production Layer-2 input. After a required-focus build, create the separate
tiered bundle and instantiate from that directory:

```sh
mkdir -p bundles-layer2/s100
python3 scripts/tier_branch_payloads.py bundles/s100/100_1.ayah.json \
  --output bundles-layer2/s100/100_1.ayah.json --compact-output
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah \
  --bundles-dir bundles-layer2
```

The tierer reads the inlined HFT activation traces as one of its explicit branch
interest sources and fails if required HFT or any required source field is
missing or malformed. It retains all root/branch identities and all non-branch
evidence; only dictionary/gloss branch payload detail is tiered.

The bundle field is:

```text
v12_focus_trace_hermetic
```

This field is distinct from:

- `v12_reader_responses`: retired strict staged per-ayah focus runs;
- `v12_reader_walks`: regular whole-surah reader walks;
- `v12_reader_walks_wide`: plus/minus-5 / 11-ayah reader walks;
- `v12_cross_run_publication`: compact reconciled publication findings.

## How Layer 2 Uses It

Use `baseline_models` to understand what the ayah yields on its own.

Use `context_deltas` for changed readings: what later ayat activate, sharpen,
weaken, or revise in the focus ayah.

Use `surprising_valid_outliers` aggressively. This is where odd but anchored
activations belong when they produce a changed reading.

Use `discarded_or_unchanged` only as review context. It is not prose fuel unless
a rejection itself explains why a tempting reading should stay contained.

Do not call Hermetic Focus Trace `stage_00` / `stage_01`. If old staged
`v12_reader_responses` exist too, those remain the truer staged reveal. Preserve
the tension in evidence when both remain anchored.

## Workflow Boundary

This does not need a separate ayah-commentary writer workflow. Focus Trace is an
optional Layer-2 evidence source, so the same active
`_ayah_commentary/v2/PROMPT.md` task should write from it. Normal comparator labels
such as `v2.5.5-high`, `v2.5.6-sol-high`, and `v2.5.6-sol-max` are filename and
manifest labels only; they all use the canonical `v2.5.6-sol-high` instruction
profile.

Use a separate bundle/output directory only for controlled comparisons, such as
HFT versus no-HFT or no-reader ablations.

## Current Production Regeneration

For the focused ayah-commentary workflow, the active path is:

```text
build_bundle.py --require-focus-trace
  -> tier_branch_payloads.py --compact-output
  -> instantiate.py --bundles-dir bundles-layer2 --require-focus-trace
```

All three gates are intentional. `build_bundle.py --require-focus-trace` fails
when any target ayah lacks a usable HFT reader. `tier_branch_payloads.py` fails
when HFT, required coverage, branch inventories, or branch citations are absent
or malformed. `instantiate.py --require-focus-trace` fails if the tiered bundle
being inlined no longer has HFT readers. Optional sources may be absent only as
explicit coverage notes; they should not disappear silently.

S12, S18, and S5 use explicit pericope source directories:
`bundles/s012-pericopes/`, `bundles/s018-pericopes/`, and
`bundles/s005-pericopes/`. The tiered production prompt input remains the single
zero-padded directory for each surah under `bundles-layer2/`. Do not create
duplicate `s5`/`s005`, `s18`/`s018`, or `s12`/`s012` workflows.

The current pericope intervals are:

- S12: 1-18, 19-35, 36-57, 58-76, 77-93, 94-111.
- S18: 1-26, 27-44, 45-59, 60-82, 83-98, 99-110.
- S5: 1-11, 12-26, 27-40, 41-56, 57-71, 72-86, 87-108, 109-120.

The production task source is `_ayah_commentary/v2/PROMPT.md`.
`scripts/instantiate.py` appends the canonical `v2.5.6-sol-high` rendering
profile for every normal comparator label; the label changes only the prompt
filename and manifest `profile` value.

## S100 Handoff

The live continuation runbook is:

```text
../latent_activation/focus_trace/runs/s100/COLD_HANDOFF.md
```

After upstream reader JSON validates, rebuild S100 with:

```sh
python3 scripts/build_bundle.py --surah 100 --require-focus-trace
jq '.coverage.v12_focus_trace_hermetic' bundles/s100/100_1.ayah.json
```

Then rerun `scripts/tier_branch_payloads.py` for every target ayah before
instantiating Layer 2. An older tiered bundle must never be reused after its full
source bundle or HFT response changes.

An older instantiated prompt must also never be reused after any bundle changes.
Prompt files inline a snapshot of the JSON; the path in the manifest is
provenance, not a live link. For focused pilots, verify the instantiated prompt
itself before sending it to a model:

```sh
rg -n '"v12_focus_trace_hermetic"|reader_hft_|baseline_models|context_deltas|surprising_valid_outliers' \
  _commentary/inputs/s100/100_1.ayah.*.prompt.md
```
