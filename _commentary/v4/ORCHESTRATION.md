# Commentary v4 orchestration

This is the end-to-end runbook for a cold orchestrator. Run commands from the
repository root. Do not invoke the v2 or v3 state machines and do not use old
commentary as evidence or as a gap checklist.

The fixed sequence is:

```text
prepare
  -> 3 fresh one-pass scope authors in parallel
  -> 1 fresh canonical merge writer
  -> same canonical writer for editorial
  -> verify
```

There are no repair, reconciliation, retry, or session-recovery stages.

## 1. Preflight

Choose the package source before starting agents.

For a native numbered focus, require:

```text
bundles/sNNN/S_A.ayah.json
```

Build a missing numbered bundle with:

```bash
python3 scripts/build_bundle.py --surah S --ayah A --out bundles/sNNN
```

For every numbered focus in S2-S8 and S10-S114, also require the host prefatory
bundle:

```text
bundles/sNNN/S_0.ayah.json
```

Build it with:

```bash
python3 scripts/build_bundle.py --surah S --ayah 0 --out bundles/sNNN
```

S1 uses numbered `1:1`; S9 has no prefatory basmala. Never create `1:0` or
`9:0`.

Bundle generation requires the sibling `../quran-data/data/` tree. The default
Hermetic Focus Trace policy also requires
`../latent_activation/focus_trace/`. Use `--exclude-focus-trace` only for an
intentional build whose manifest records that choice.

The active unit manifest is `commentary-v4-unit-manifest-v5`. If the selected
unit already has an older manifest or old `.review.json` output, preserve its
Git history and relocate the legacy raw/editorial files before starting. Then
regenerate the input with `advance --force-input`; V4 will not adopt legacy
output into the one-pass workflow.

For a pericope package, inspect the canonical index and run the dedicated
wrapper:

```bash
rg '"surah":\s*29' \
  ../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

If no index row exists, declare the span and label explicitly:

```bash
python3 scripts/build_pericope_bundles.py \
  --surah 29 --pericope 3 --ayah-from 28 --ayah-to 44 \
  --pericope-label "Declared operator span"
```

Use the emitted `bundles/sNNN-pericopes/pPP_AAA-BBB/` directory as
`--context-bundles-dir`. Keep `scripts/build_bundle.py` as the lower-level ayah
builder; do not patch it to add pericope package orchestration.

Use `--member-bundles-dir bundles` for the mandatory host `S:0` and explicit
external ayat. Build a missing external member as an ordinary single-ayah
bundle. Every external ayah must be enumerated through `--add-ayat`; adding all
of S1 means `1:1,1:2,1:3,1:4,1:5,1:6,1:7`.

## 2. Start one unit

For a native focus:

```bash
python3 _commentary/v4/workflow.py advance --ayah S:A
```

For a pericope focus with external Fatiha context:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

The first call prepares the input and returns `stage: scope_authoring` with
three handoffs:

```text
micro_scope_author
macro_scope_author
global_scope_author
```

Start them as fresh, independent agents in parallel. Use model
`gpt-5.6-luna`, reasoning effort `max`, and no priority or service-tier option.
Give each agent only its declared prompt and expected response path. Each writes
one exact JSON object to:

```text
raw/<analysis-id>/sNNN/S_A/<lane>.contribution.json
```

Do not edit, normalize, or supplement a contribution. Do not run an agent a
second time automatically. A malformed, stale, incomplete, or unknown-evidence
response is a unit error that requires explicit operator inspection and
replacement.

## 3. Canonical first pass

After all three scope agents have finished writing, run the same `advance`
command again. Later calls for a custom analysis need only its stable ID and
focus ref because `analysis.json` is already snapshotted:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id s029-p03-with-fatiha --ayah 29:38
```

V4 mechanically validates each contribution and returns
`stage: canonical_write`. Start one fresh canonical writer with model
`gpt-5.6-luna`, reasoning effort `max`, and no priority or service-tier option.

The canonical prompt contains the three validated prose-ready contributions,
focus-surface evidence, and governing texts. It does not expose lane packets or
authorize new evidence decisions. The writer merges all supplied findings and
writes exactly four first-pass files under the declared raw paths:

```text
S_A.prose.tr.md
S_A.evidence.tr.md
S_A.index.tr.md
S_A.friction.tr.md
```

Keep this canonical writer live for the editorial turn.

## 4. Editorial pass

After all four first-pass files exist, run `advance` again. V4 binds their exact
hashes and returns `stage: canonical_editorial`.

Send that editorial prompt to the same live canonical writer. It embeds the
unchanged v3 editorial instructions and names four separate destination files:

```text
S_A.prose.editorial.tr.md
S_A.evidence.editorial.tr.md
S_A.index.editorial.tr.md
S_A.friction.editorial.tr.md
```

If the canonical conversation is lost, use the returned
`restart_if_agent_unavailable` canonical prompt and regenerate the complete
first-pass set before producing editorial output. Do not invent a repair stage.

## 5. Complete and verify

After the editorial writer has finished, run `advance` once to obtain complete
status, then run:

```bash
python3 _commentary/v4/workflow.py verify --ayah S:A
```

For a custom analysis:

```bash
python3 _commentary/v4/workflow.py verify \
  --analysis-id s029-p03-with-fatiha --ayah 29:38
```

`verify` rechecks source and prompt provenance, Quran and inter-ayah source
hashes, implementation hashes, path safety, composition membership, context
projections, contribution structure, editorial input hashes, exact output
filenames, and nonempty output files. It does not assess prose quality or revise
agent work. Inspect `git diff` and commit the unit's input, raw, and editorial
artifacts together when accepted.

## Context rules

- Native `micro` evidence is focus-local.
- Same-surah context in the focus segment goes to `macro`.
- Cross-segment or cross-surah ordinary selected context goes to `global`.
- Every `--add-ayat` ref is inserted once as an ordinary, context-only `macro`
  member of `--member-surah`. It retains its original Quran identity, receives
  focus-conditioned root cues, and never becomes a focus implicitly.
- The automatic host basmala is also one ordinary lean `macro` member. It is not
  copied into micro or global and does not import standalone-focus payloads. An
  explicitly segmented host `S:0` is normalized to this same route.
- If the same explicit member exists in package and member roots, both
  canonical hashes must agree. A flat package root must have a valid
  `pericope.bundle-manifest.json`.

For a numbered 29:38 pericope run, 29:0, 29:28-37, 29:39-44, and any explicit
`--add-ayat` refs therefore meet as non-focus macro context. The focus remains
29:38. Cross-segment context declared as an ordinary segment remains global.

For a dedicated basmala analysis, invoke it directly:

```bash
python3 _commentary/v4/workflow.py advance --ayah 29:0
```

The CLI derives `s029-basmala-full` and places `29:0,29:1-69` in one host
segment. Every numbered host ayah becomes ordinary lean macro context. An
explicit `S:0` focus composition must carry the complete canonical host surah.

## Batch orchestration

Use ranges or explicit sets:

```bash
python3 _commentary/v4/workflow.py advance --ayah 100:1-11
python3 _commentary/v4/workflow.py advance --ayah 1:1-7 2:1-5
```

Launch every item in `parallel_handoffs` concurrently. Each item carries its
`ayah_ref` and `stage`; never infer either from list order. Do not call
`advance` for a unit while one of its agents is still writing. Either wait for
the full wave or advance only refs whose agents have completed.

For canonical waves, retain an in-memory map from ayah ref to live writer so
the matching editorial handoff returns to that writer. V4 persists no agent
handle or session ID. Different ayahs and different analysis IDs have disjoint
paths and may run concurrently. Do not run two orchestrators for the same
analysis ID and ayah at once.

A failed unit does not suppress ready handoffs for other batch units. A
`partial_error` response exits nonzero so automation cannot overlook it.

## Operational rules

- Run `advance` without `--force-input` first. If input is stale, inspect the
  source change and `git diff` before replacing generated input.
- `--force-input` changes generated input only. It never adopts, deletes, or
  rewrites raw or editorial work.
- Do not create session IDs, attempt counters, repair prompts, reconciliation
  ledgers, or hidden worktrees.
- Do not drive an errored unit with an automatic retry loop.
- Do not modify agent outputs in place. Preserve, remove, or relocate a failed
  artifact explicitly, then rerun the fixed stage.
- Treat partial work as ordinary Git-visible state. V4 does not create a second
  history mechanism.
