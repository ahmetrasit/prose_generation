# Commentary v4 orchestration

This is the end-to-end runbook for a cold orchestrator. Run commands from the
repository root. Do not invoke the v2 or v3 state machines and do not use old
commentary as evidence or as a gap checklist.

The fixed sequence is:

```text
prepare
  -> 3 fresh one-pass scope authors in parallel
  -> same scope author for one repair turn if its contribution is invalid
  -> 1 fresh canonical merge writer
  -> same canonical writer for editorial
  -> verify
```

There are no reconciliation, retry-loop, or session-recovery stages. The only
repair path is a single same-agent scope repair described below.

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

The active unit manifest is `commentary-v4-unit-manifest-v6`, lane packets use
`commentary-v4-lane-evidence-packet-v1`, active scope responses use
`commentary-v4-scope-contribution-v2`, and apparatus ledgers use
`commentary-v4-finding-provenance-v1`. If the selected unit
already has a manifest-v5 or older input, a contribution-v1 response, or old
`.review.json` output, preserve its Git history and relocate the legacy
raw/editorial files before starting. Then regenerate the input with
`advance --force-input`; V4 will not adopt legacy output into the current
one-pass workflow.

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

Do not edit, normalize, or supplement a contribution. If a malformed, stale,
incomplete, or unknown-evidence response fails workflow validation, preserve the
bad artifact outside the active raw path and send exactly one repair request to
the same live scope agent. The repair request must give the same prompt and
expected response path, must instruct the agent not to read the failed artifact
or any existing output data, and must require overwriting the expected response
directly. When that same agent returns the second artifact for the lane, accept
it as the lane contribution and continue the fixed workflow; do not run another
repair, do not spawn a replacement, and do not create a retry loop.

Each contribution must decide every candidate and audit every supplied branch
facet, connection, and nested connection-evidence row. Every accepted or
narrowed candidate owns its own finding; only exact semantic duplicates may be
represented by another finding. Every activated branch records its exact
facet, a nonempty subset of its actual carrier occurrences, a distinct
independent trigger, an exact focus-word return path, and a fluent Turkish
activation sentence. Every finding also supplies one exact semantic sentence
that carries its distinctive mechanism and payoff. Internal IDs remain in the
apparatus and must not appear in either sentence or reader prose.

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
focus-surface evidence, workflow-derived per-finding provenance ledgers, and
governing texts. It does not expose lane packets or
authorize new evidence decisions. The writer merges all supplied findings and
writes exactly four first-pass files under the declared raw paths:

```text
S_A.prose.tr.md
S_A.evidence.tr.md
S_A.index.tr.md
S_A.friction.tr.md
```

The findings index ends with a `commentary-v4-landing-map` JSON block. It binds
each finding's exact top-level semantic sentence to its unique prose occurrence,
binds the finding to unique evidence and index quotes, and lists every
branch-activation sentence verbatim. The canonical writer may compose freely
around those sentences but may not weaken, generalize, combine away, or omit
them. Each evidence and index quote must also encompass the only copy in that
apparatus file of the finding's exact single-line provenance-ledger JSON object.
The ledger includes linked candidate, branch, connection, and
connection-evidence decisions. Apparatus quotes and immutable semantic
sentences for different findings may not overlap or contain one another.

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

The editorial index replaces the raw landing map with an editorial map carrying
the same findings, exact finding-level semantic sentences, and exact activation
sentences. Editorial revision may change their surrounding prose and apparatus
quotes, but not either semantic sentence class or the exact provenance ledger
carried in both apparatus files.

If the canonical conversation is lost, use the returned
`restart_if_agent_unavailable` canonical prompt and regenerate the complete
first-pass set before producing editorial output. Do not invent any repair stage
outside the single same-agent scope repair.

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
and auxiliary-branch projections, contribution identity and semantic
obligations, editorial input hashes, exact output filenames, and all eight
outputs. It validates complete candidate/branch/connection accounting, unique
raw and editorial finding landings, exact activation-sentence survival, and the
exactly one copy of each per-finding provenance ledger in both apparatus files.
It rejects
overlapping landings and internal IDs in reader prose. It does not decide whether an
interpretation is substantively good or revise agent work. Inspect `git diff`
and commit the unit's input, raw, and editorial artifacts together when
accepted.

## Context rules

- Native `micro` evidence is focus-local.
- Same-surah context in the focus segment goes to `macro`.
- Cross-segment or cross-surah ordinary selected context goes to `global`.
- Candidate and support refs are parsed from structured fields, serialized JSON,
  Quran coordinates, and same-surah ranges before prompt generation. Evidence
  is moved to the widest lane required by those refs. Host basmala and explicit
  `--add-ayat` membership remain macro even when their linguistic source or
  source evidence names another surah.
- Every `--add-ayat` ref is inserted once as an ordinary, context-only `macro`
  member of `--member-surah`. It retains its original Quran identity, receives
  focus-conditioned root cues, and never becomes a focus implicitly.
- The automatic host basmala is also one ordinary lean `macro` member. It is not
  copied into micro or global and does not import standalone-focus payloads. An
  explicitly segmented host `S:0` is normalized to this same route.
- If the same explicit member exists in package and member roots, both
  canonical hashes must agree during preparation and every later manifest load.
  A flat package root must have a valid
  `pericope.bundle-manifest.json`.
- Lean context normally excludes full root dictionaries. When a supplied
  candidate's branch-specific trace cites exact context refs whose bundles
  contain that unresolved branch, V4 adds only that branch's semantic descriptor
  and aggregates its matching root occurrences. Branch-only refs take part in
  lane routing before hydration, and each candidate retains a separate source-to-
  carrier binding so one finding cannot borrow another candidate's occurrence.
  Every auxiliary bundle's path,
  bytes, raw and canonical hashes, unit identity, source pointer, and complete
  projected descriptor are revalidated before every stage.

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
The focus's canonical `1:1` linguistic coordinates remain focus surface and
must never be routed or cited as external context.

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
- Do not create session IDs, attempt counters, separate repair prompts,
  reconciliation ledgers, or hidden worktrees.
- Do not drive an errored unit with an automatic retry loop.
- Do not modify agent outputs in place. Preserve, remove, or relocate a failed
  scope artifact explicitly, then send one same-agent repair request. Accept the
  second returned artifact for that lane and continue; do not spawn a replacement
  for the same lane unless the original live agent is unavailable.
- Treat partial work as ordinary Git-visible state. V4 does not create a second
  history mechanism.
