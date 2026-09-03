# Commentary v5 orchestration

This is the end-to-end runbook for a cold orchestrator. Run every command from
the repository root. Do not invoke V2/V3/V4 state machines and do not use old
prose as evidence or as a gap checklist.

## Fixed Sequence

```text
prepare
  -> 3 fresh scope-discovery agents in parallel
  -> planned composition follow-up to the same 3 live agents in parallel
  -> 1 fresh canonical writer
  -> editorial follow-up to the same live canonical writer
  -> verify
```

Discovery and composition are two planned turns, not a repair cycle. There are
no reconciliation, repair, or automated retry stages. The first-turn discovery
is persisted and hash-bound before the composition prompt is created, so a cold
replacement may perform the second turn when the original lane agent is no
longer available.

## 1. Preflight

For a native numbered focus, require:

```text
bundles/sNNN/S_A.ayah.json
```

Build a missing numbered bundle with:

```bash
python3 scripts/build_bundle.py --surah S --ayah A --out bundles/sNNN
```

For numbered focuses in S2-S8 and S10-S114, also require
`bundles/sNNN/S_0.ayah.json`. S1 uses `1:1`; S9 has no prefatory basmala. Never
create `1:0` or `9:0`.

For a large-surah pericope, use the wrapper:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

If the canonical pericope index has no row, declare the interval and label:

```bash
python3 scripts/build_pericope_bundles.py \
  --surah 29 --pericope 3 --ayah-from 28 --ayah-to 44 \
  --pericope-label "Declared operator span"
```

Use its emitted `bundles/sNNN-pericopes/pPP_AAA-BBB/` directory as
`--context-bundles-dir`. Keep `bundles/` as `--member-bundles-dir` for the
mandatory host basmala and external ayat. Do not patch `scripts/build_bundle.py`
to orchestrate pericopes.

Every external ayah must be listed individually with `--add-ayat`; ranges are
invalid. Adding all of S1 requires
`1:1,1:2,1:3,1:4,1:5,1:6,1:7`.

## 2. Start The Unit

Native:

```bash
python3 _commentary/v5/workflow.py advance --ayah S:A
```

Pericope with external Fatiha:

```bash
python3 _commentary/v5/workflow.py advance \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

The first call prepares all hermetic inputs and returns
`stage: scope_discovery` with three roles:

```text
micro_scope_discoverer
macro_scope_discoverer
global_scope_discoverer
```

Launch three fresh, independent agents in parallel. Use the configured
maximum-capability authoring model at maximum reasoning effort; the established
repository default is `gpt-5.6-luna` with `max`. Do not add a priority or
service-tier override. This is operator policy, not a model/runtime identity
attested by the manifest or checked by `verify`.

Give each agent only its returned prompt and destination. Each writes exactly
one JSON object to:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/<lane>.discovery.json
```

Do not edit, normalize, repair, supplement, or semantically judge these files.
Wait until all three agents have finished before advancing the unit.

### Discovery Duties

Each agent decides every supplied candidate and independently searches its lane
for uncandidate findings. It does not write polished prose and does not emit an
exhaustive negative audit of every dictionary branch or connection.

For each supplied candidate it must preserve or explicitly exclude:

- every nominated branch;
- every explicitly nominated branch facet;
- every required context ref;
- every named semantic obligation, including candidate-specific word/channel
  evidence, HFT trace roles, before/after readings, and containment.

A context ref survives only through an actual activation carrier or trigger.
Every branch activation names an exact facet, actual carrier, independent
trigger, focus return, resulting reading, and boundary. A specialization cannot
stand without that branch's core facet. `root_ids` on word-analysis candidates
are orientation/provenance only. Their `root_branch_options` index makes the
relevant choices explicit, but the agent still decides whether any branch is
activated from an independent trigger.

## 3. Scope Composition Follow-Up

After all three discovery files exist, run the same `advance` command. For a
prepared custom analysis, the stable ID and focus are sufficient:

```bash
python3 _commentary/v5/workflow.py advance \
  --analysis-id s029-p03-with-fatiha --ayah 29:38
```

The workflow validates each discovery, records its raw bytes and SHA-256 in the
unit manifest, and writes a self-contained composition prompt. It returns
`stage: scope_composition` with three roles:

```text
micro_scope_composer
macro_scope_composer
global_scope_composer
```

Send each prompt as the planned follow-up to the same live lane agent. These
three follow-ups may run in parallel. If a lane conversation was lost, start one
cold replacement with that lane's returned composition prompt; it embeds the
validated finding set and compact semantic requirements, not another copy of the
candidate-decision ledger or full packet.

Each lane writes exactly one JSON object to:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/<lane>.contribution.json
```

The agent renders every discovery finding as fluent Turkish without changing
the finding set. It may group compatible activation explanations within a
finding, but it must explicitly preserve the carrier, trigger, contact,
resulting reading, boundary, and concrete semantic details. English source
phrases must be translated, not copied. The response maps every ordered
semantic ref to an exact prose passage. The request hash binds the source
inventory without requiring the agent to echo its hashes or payloads. This is
mechanical traceability; the workflow does not claim to prove semantic
entailment.

Do not turn a malformed response into a repair conversation. The workflow stops
the unit. Preserve or relocate the invalid artifact, diagnose the contract
failure, and deliberately replace it before continuing.

## 4. Canonical First Pass

After all three lane contributions exist, run `advance` again. It returns
`stage: canonical_write`.

Start one fresh canonical writer with the same maximum-capability model policy.
The prompt contains compact findings projections, Turkish lane renderings,
focus-surface evidence, compact provenance ledgers, and governing texts. Full
packets and candidate audits remain separately persisted and hash-bound. The
writer is not authorized to make new evidence decisions.

The writer creates exactly:

```text
S_A.prose.tr.md
S_A.evidence.tr.md
S_A.index.tr.md
S_A.friction.tr.md
```

The prose must be coherent Turkish, not a lane report or ledger dump. Wording
from lane contributions is editable. Every validated mechanism and specific
image remains explicit, including which ordinary/root meaning meets which
trigger and how that contact changes the focus reading.

The findings index ends with one `commentary-v5-landing-map` block. For every
finding it gives exact prose/evidence/index quotes and lists every ordered
semantic ref exactly once. Compatible findings may share one substantive prose
quote. Evidence and index quotes must remain unique. Evidence contains the
finding ref and exact compact provenance ledger once; the index contains the
finding ref and only the ledger's source-record hash.

Keep this canonical writer live.

## 5. Editorial Follow-Up

After all four first-pass files exist, run `advance` again. It validates the raw
landing map, binds all four input hashes, and returns
`stage: canonical_editorial`.

Send the returned prompt to the same live canonical writer. The writer creates:

```text
S_A.prose.editorial.tr.md
S_A.evidence.editorial.tr.md
S_A.index.editorial.tr.md
S_A.friction.editorial.tr.md
```

Editorial prose may rewrite every prior sentence to improve cadence, remove
technical shorthand, and translate English leakage. The immutable layer is the
structured discovery semantics and exact apparatus provenance, not a sentence.
The editorial landing map keeps the same finding order and semantic refs while
updating its quotes and phase.

If the canonical conversation is lost, use the returned
`restart_if_agent_unavailable` canonical prompt and regenerate the complete
first-pass set before editorial work. Do not invent an editorial repair stage.

## 6. Complete And Verify

Run `advance` after editorial output, then verify explicitly:

```bash
python3 _commentary/v5/workflow.py verify --ayah S:A
```

Custom analysis:

```bash
python3 _commentary/v5/workflow.py verify \
  --analysis-id s029-p03-with-fatiha --ayah 29:38
```

Verification is mechanical. It rechecks fixed paths, source and package hashes,
context membership/projections, implementation and prompt hashes, discovery and
composition identities, first-pass lineage, all final files, landing coverage,
compact provenance placement, byte budgets, internal-ID leakage in reader
prose, and obvious English in all human-authored Turkish output text. It checks
the declared source-to-passage mapping mechanically; it does not adjudicate
semantic entailment or interpretive quality.

Inspect the complete Git diff before committing the unit.

## Context Rules

- Micro is focus-local.
- Same-surah context in the focus segment is macro.
- Ordinary cross-segment or cross-surah context is global.
- Automatic host basmala and `--add-ayat` members are macro regardless of their
  source aliases.
- Added ayat are context-only and never become focus ayat implicitly.
- Every non-focus member uses the same lean native-context projection. A
  basmala does not import its standalone-focus payload into another focus.
- Candidate-bound unresolved context branches may be hydrated only from the
  exact cited context sources. Their paths, bytes, hashes, identities, and
  projections are revalidated.
- If an explicit member exists in package and member roots, canonical hashes
  must agree.

For pericope focus 29:38, `29:0`, `29:28-37`, `29:39-44`, and explicit
`--add-ayat` refs are non-focus macro context. The focus remains `29:38`.

For a dedicated basmala analysis:

```bash
python3 _commentary/v5/workflow.py advance --ayah 29:0
```

The derived `s029-basmala-full` analysis puts all numbered S29 ayat in ordinary
lean macro context so they can activate basmala-focused resonances.

## Batch Rules

Use ranges or explicit sets and launch every returned `parallel_handoffs` item
concurrently. Each item carries its own `ayah_ref` and `stage`; do not infer
either from list order. Do not advance a unit while one of its agents is still
writing.

Retain an in-memory map from ayah ref to live lane agents through the composition
wave, and from ayah ref to canonical writer through editorial. Agent sessions
are conveniences, not persisted workflow state. Different ayat and analysis IDs
have disjoint paths and may run concurrently; never run two orchestrators for
the same analysis ID and ayah at once.

A failed unit does not suppress ready handoffs for other batch units. A
`partial_error` response exits nonzero.

## Operational Rules

- Run without `--force-input` first. Inspect any stale-input error before
  replacing generated inputs.
- `--force-input` changes generated input only. It never edits raw/editorial
  agent artifacts.
- Do not create attempt counters, repair prompts, reconciliation ledgers,
  session registries, or hidden worktrees.
- Do not modify agent outputs in place.
- Treat partial work as ordinary Git-visible state; V5 has no second history
  mechanism.
