# Commentary v2 Cold Orchestration

This is the run contract for a cold agent. It assumes no prior conversation and
no knowledge beyond this repository.

The workflow instantiates hermetic prompts. It does not invoke a model. The
orchestrating agent is responsible for launching one writing agent per prompt,
waiting for its declared outputs, and running the validation gate before
continuing.

## 1. Governing rules

Read, in order:

1. this file;
2. `README.md`;
3. `shared/EDITORIAL_CONTRACT.md`;
4. the selected run configuration.

Do not edit generated prompts. Change the source contract or run configuration
and instantiate again.

Do not let editorial organization become Layer 2 selection. There is no
surprise budget, finding quota, paragraph quota, or preferred finding count.
Every discovery finding marked `carry` must remain represented.

## 2. Inputs

One run configuration is required. Validate it before doing anything else:

```sh
python3 _commentary/v2/scripts/validate.py config path/to/run.json
```

The configuration defines:

- the surah;
- the target language;
- one or more non-overlapping editorial pericopes;
- the generated output root;
- one or more source files for each ayah, directly or through a filename
  pattern;
- optional governing documents to inline.

Layer 1 is not implemented here. `ayahSources` is deliberately source-agnostic.
It may point to current commentary bundles, future Layer 1 packets, or an
explicit set of precompiled files.

Every configured source must exist and be non-empty. A present but empty file is
a hard failure.

## 3. State machine

Run the stages in this order. Never continue past a failed check.

### Required transition order

The orchestration loop is always:

```text
validate run configuration
  -> instantiate discovery prompts
  -> spawn discovery agents and wait for their files
  -> check discovery
  -> instantiate compiler prompts for eligible pericopes
  -> spawn compiler agents and wait for their files
  -> check each compiler result
  -> instantiate final Layer 2 prompts for eligible pericopes
  -> spawn Layer 2 agents and wait for their files
  -> check each pericope's Layer 2 results
  -> if multi-pericope: instantiate, spawn, and check reconciliation
  -> instantiate the intended Layer 3 prompt
  -> spawn the Layer 3 agent and wait for its files
  -> check Layer 3
```

Instantiation prepares one or more agent packets. It does not complete the
stage. A stage is complete only after its agents have written every declared
artifact and the corresponding `check` command passes.

For multiple pericopes, a pericope may advance as soon as all of its own
dependencies pass. For example, its compiler does not need to wait for
discovery in an unrelated pericope. Whole-surah reconciliation and Layer 3 must
wait for every contributing pericope.

### Stage A: Layer 2 discovery

Instantiate all ayah discovery prompts:

```sh
python3 _commentary/v2/scripts/workflow.py discovery \
  --config path/to/run.json \
  --date YYYY-MM-DD
```

This writes one prompt and manifest per ayah beneath:

```text
layer_2/discovery/inputs/
```

Launch one agent per prompt. These agents are independent and may run in
parallel. Each agent writes exactly:

```text
{S}_{A}.ledger.json
{S}_{A}.memo.md
{S}_{A}.friction.md
```

The ledger is canonical. The memo is optional reasoning support for the compiler
and is not the field boundary.

Gate:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage discovery
```

For a partial rerun, add `--ayah A`. For one editorial scope, add
`--pericope ID`.

### Stage B: Pericope compilation

For every configured pericope:

```sh
python3 _commentary/v2/scripts/workflow.py compile \
  --config path/to/run.json \
  --pericope PERICOPE_ID \
  --date YYYY-MM-DD
```

The token-efficient default inlines ledgers only. Add `--include-memos` only
when the ledgers do not preserve enough reasoning for editorial planning.

Launch one compiler agent per pericope. Different pericopes may compile in
parallel after all of their discovery ledgers pass. Each compiler writes:

```text
{PERICOPE}.editorial-plan.json
{PERICOPE}.channel-registry.json
{PERICOPE}.friction.md
```

The compiler must copy source ledger hashes from its input descriptor. It may
merge presentation, create traceable syntheses, and nominate channels. It may
not change a discovery `carry` finding to blocked.

Gate each pericope:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage compiler \
  --pericope PERICOPE_ID
```

### Stage C: Final Layer 2 ayah prose

For every compiled pericope:

```sh
python3 _commentary/v2/scripts/workflow.py author-layer2 \
  --config path/to/run.json \
  --pericope PERICOPE_ID \
  --date YYYY-MM-DD
```

This writes one prompt per ayah. Each prompt contains only:

- the shared rules;
- that ayah's discovery ledger;
- that ayah's editorial plan slice.

It does not expose the complete channel registry or a surah thesis.

Launch one agent per prompt. Ayahs in the same pericope may run in parallel after
the pericope plan passes. Each agent writes:

```text
{S}_{A}.prose.md
{S}_{A}.evidence.md
{S}_{A}.index.md
{S}_{A}.result.json
{S}_{A}.friction.md
```

Gate:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage layer2 \
  --pericope PERICOPE_ID
```

The gate verifies exact ledger and plan hashes, all output files, all planned
findings, all planned syntheses, and the standalone checks. One omitted carried
finding fails the entire ayah.

### Stage D: Registry reconciliation

Skip this stage when one pericope intentionally covers the whole surah.

For a multi-pericope surah:

```sh
python3 _commentary/v2/scripts/workflow.py reconcile \
  --config path/to/run.json \
  --date YYYY-MM-DD
```

Launch one reconciliation agent. It writes:

```text
whole-surah.channel-registry.json
whole-surah.registry-coverage.json
whole-surah.registry-friction.md
```

The reconciler may merge identities and split a compound candidate. It may not
reject a source candidate. Every pericope candidate must map to at least one
surah candidate.

Gate:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage reconciliation
```

### Stage E: Layer 3 channel commentary

For a single whole-surah pericope:

```sh
python3 _commentary/v2/scripts/workflow.py author-layer3 \
  --config path/to/run.json \
  --pericope PERICOPE_ID \
  --date YYYY-MM-DD
```

For a reconciled multi-pericope surah:

```sh
python3 _commentary/v2/scripts/workflow.py author-layer3 \
  --config path/to/run.json \
  --surah-scope \
  --date YYYY-MM-DD
```

The registry-only prompt is the default. Add `--include-layer2-prose` only when
the Layer 3 writer needs exact reader-facing wording rather than the registry's
anchors, contributions, and evidence references.

Launch one Layer 3 agent. It writes:

```text
{SCOPE}.channels.prose.md
{SCOPE}.channels.evidence.md
{SCOPE}.channels.result.json
{SCOPE}.channels.friction.md
```

Layer 3 may accept, revise, merge, or reject channel candidates. It must account
for every candidate. Its decision never removes the underlying Layer 2 finding.

Gate a pericope result:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage layer3 \
  --pericope PERICOPE_ID
```

Gate a whole-surah result:

```sh
python3 _commentary/v2/scripts/workflow.py check \
  --config path/to/run.json \
  --stage layer3 \
  --surah-scope
```

## 4. Agent launch contract

### Single-file worker packet

Every generated `*.prompt.md` is the complete read packet for one writing
agent. Depending on the stage, it inlines the task prompt, editorial contract,
required schemas, governing documents, input bundles, descriptors, discovery
ledgers, editorial-plan slices, or channel registries. The paths printed inside
the packet are provenance identities and declared write targets; they are not
instructions to open additional source files.

The adjacent `*.manifest.json` belongs to the orchestrator. It records source
hashes and expected outputs for auditing and invalidation. Do not give it to the
writing agent, and do not ask the writing agent to read schemas or input bundles
separately. Their contents are already in the generated prompt.

Spawn each writing agent with an instruction equivalent to:

```text
Read only <absolute-path-to-generated.prompt.md>.
Use only the material inlined in that file.
Write exactly the output files declared in its header.
Do not return the artifacts only in chat.
```

The writing agent needs filesystem permission to read that one prompt and write
the declared outputs. It does not need read access to the original source
bundle, source schemas, source task prompt, or manifest.

For every instantiated prompt:

1. Give the writing agent only that generated `*.prompt.md` as readable input.
2. Tell it to use only inlined sources.
3. Tell it to write exactly the expected files listed in the prompt header.
4. Do not ask it to summarize its work in chat instead of writing the files.
5. Wait for all required files.
6. Treat a missing, empty, malformed, or extra-contract artifact as failure.
7. Run the stage gate before launching dependent work.

`workflow.py` instantiates packets and validates results; it does not spawn
agents. The transport is intentionally unspecified. A cold orchestrator may use
the available native worker/agent runner, but must preserve one generated prompt
per isolated writing context.

## 5. Parallelism

Safe parallel units:

- all Stage A ayahs;
- Stage B pericopes whose discovery ledgers passed;
- all Stage C ayahs inside a passed pericope.

Serial dependencies:

```text
discovery
  -> pericope compiler
    -> final Layer 2 ayah prose
      -> optional registry reconciliation
        -> Layer 3
```

Do not run the compiler while any ledger in its pericope is missing or invalid.
Do not run Layer 2 authoring against a changed ledger without recompiling the
pericope.

## 6. Invalidation and reruns

All downstream artifacts are hash-bound.

- Changed ayah source: rerun that discovery unit, then recompile its pericope,
  regenerate affected Layer 2 ayahs, reconcile registries if used, and rerun
  Layer 3.
- Changed discovery ledger: same downstream invalidation.
- Changed editorial plan: regenerate Layer 2 for that pericope.
- Changed channel registry only: Layer 2 remains valid; rerun reconciliation and
  Layer 3 as applicable.
- Changed reconciled registry: rerun surah-scope Layer 3.

Never edit a hash in an authored JSON file to make validation pass. Reinstantiate
or regenerate the dependent artifact.

## 7. Long ayahs

The semantic field remains uncapped. Model context limits are operational limits,
not editorial permission to select.

The current v2 scripts expect one final discovery ledger per ayah. If a very
long ayah must be discovered in shards, the orchestrator must merge and validate
those shards into one complete `{S}_{A}.ledger.json` before Stage B. Do not feed
partial shard ledgers directly to the pericope compiler.

Shard merging is not yet automated by v2. Until it is, use one discovery packet
when feasible or perform an explicit coverage-preserving merge with all source
obligations accounted for.

## 8. Completion

A run is complete when:

- every configured ayah passes discovery validation;
- every pericope compiler output passes;
- every final Layer 2 result passes;
- multi-pericope registry reconciliation passes when applicable;
- the intended Layer 3 scope passes;
- every expected prose, evidence, index/result, and friction artifact is
  present and non-empty.

Use the status view for orientation, not validation:

```sh
python3 _commentary/v2/scripts/workflow.py status \
  --config path/to/run.json
```
