# Hermetic Focus Trace Integration

## Summary

Hermetic Focus Trace is a new upstream workflow in
`../latent_activation/focus_trace/`. It is designed to recover the most useful
part of the retired per-ayah focus runs: an ayah first read on its own, then
read again as neighboring ayat activate surprising latent possibilities.

It is intentionally cheaper than strict staged focus runs. The reader receives
one sealed packet and writes one JSON response. That means it is a reconstructed
trace, not a blind reveal transcript. The commentary workflow must label and use
it accordingly.

## Why It Matters For S100

S100 exposed the gap. `reader_m_ayah_walk.md` is a whole-surah reader walk, but
it preserved exactly the qualities the commentary needs:

- surprise;
- latent activation;
- changed reading;
- abductive moves;
- multiple coexisting readings;
- late-arriving retrospective insight.

The regular v12 and plus/minus-5 reader walks are useful, but their prose can
collapse the most surprising material into a coherent surah-wide account.
Hermetic Focus Trace gives Layer 2 a more inspectable ayah-level signal:
baseline readings, context deltas, and surprising outliers that remain anchored
in the focus ayah.

The goal is not to beat `reader_m` as prose. The goal is to be good enough as a
production substrate for whole-Quran ayah commentary: structured, local,
surprise-preserving, and cost-effective.

The S100 run package records the current comparison baseline at
`../latent_activation/focus_trace/runs/s100/READER_M_BASELINE.md`. That document
identifies the `reader_m`, regular v12, and 11-ayah source files and lists the
specific latent motifs Hermetic Focus Trace should try to recover.

The concrete continuation runbook for the live S100 test is
`../latent_activation/focus_trace/runs/s100/COLD_HANDOFF.md`. A cold agent should
start there, not by re-auditing manifests.

## Bundle Field

The latest ayah commentary bundle consumes this source as:

```text
v12_focus_trace_hermetic
```

This field is distinct from:

- `v12_reader_responses`: retired strict staged per-ayah focus runs;
- `v12_reader_walks`: regular whole-surah reader walks;
- `v12_reader_walks_wide`: plus/minus-5 / 11-ayah reader walks;
- `v12_cross_run_publication`: compact reconciled publication findings.

Hermetic Focus Trace is a one-call reconstructed focus trace. It can support the
"Before and after" section of Layer 2, but the writer must not call it a staged
`stage_00` / `stage_01` run.

Root identity is already resolved upstream through
`../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`. That bridge is
root-level, not the older form-level `qac-v4` bridge. When a QAC root splits
across multiple Furuq roots, the focus trace packet includes all mapped
`root_id` values and all their accepted, non-contaminated branch inventories.
Downstream prose code must preserve the pair `mapped_root_id` + `branch_id`;
using only the dominant root or only `branch_id` can erase precisely the
secondary latent activations this workflow is meant to recover.

Layer 2 does not inline full dictionary/gloss payloads for every secondary
split-root target in `root_lexicon`; that made S100:1 prompts jump into an
unnecessary high-token range before any focus reader output existed. Instead,
`root_lexicon.coverage` lists every mapped `root_id`, while Hermetic Focus Trace
packets and responses carry the secondary branch images and reader activations.
That keeps the commentary prompt cost tied to actual discovered readings rather
than to every possible split-root lexical envelope.

## How Layer 2 Should Use It

Use `baseline_models` to understand what the ayah yields on its own.

Use `context_deltas` for changed readings: what later ayat activate, sharpen,
weaken, or revise in the focus ayah.

Use `surprising_valid_outliers` aggressively. This is the field added to prevent
GPT readers from becoming conservative auditors. It is where odd but anchored
activations belong when they produce a changed reading.

Use `discarded_or_unchanged` only as review context. It is not a source of prose
unless a rejection itself explains why a tempting reading should stay contained.

If old `v12_reader_responses` exist too, treat them as the truer staged reveal.
If both old staged and hermetic traces disagree, preserve the tension in the
evidence surface and let the prose carry both readings when both remain
anchored.

## Production Readiness Question

The production question is lexical and reader-facing, not administrative:

Does Hermetic Focus Trace make the commentary more surprising, more locally
anchored, and more capable of changed reading than the current reader-walk-only
bundle?

If the answer for S100 is yes, even if it remains slightly behind `reader_m` in
natural prose force, it is a good candidate for whole-Quran generation.
