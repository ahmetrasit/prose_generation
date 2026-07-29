# Hermetic Focus Trace Integration

Hermetic Focus Trace is an upstream workflow in
`../latent_activation/focus_trace/`. It recovers the useful part of the retired
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
optional Layer-2 evidence source, so the same `_ayah_commentary/v1/PROMPT.md`
task should write from it.

Use a separate bundle/output directory only for controlled comparisons, such as
HFT versus no-HFT or no-reader ablations.

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
