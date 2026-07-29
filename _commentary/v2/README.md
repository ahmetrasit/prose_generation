# Commentary Workflow v2

This directory implements a ledger-first commentary workflow for Layers 2 and 3.
Layer 1 is intentionally outside this tree.

The workflow separates four operations:

1. Layer 2 discovery records every admitted ayah finding in a structured ledger.
2. The shared pericope compiler sees all ledgers in one editorial scope and
   assigns findings to coherent ayah-local movements.
3. Layer 2 authoring writes each ayah again from its local ledger and its slice
   of the pericope plan.
4. Multi-pericope surahs reconcile compact channel registries without rereading
   Layer 2 prose.
5. Layer 3 consumes a pericope or reconciled surah registry and writes
   cross-ayah image and meaning chains.

There is no surprise budget, finding quota, paragraph quota, or per-ayah cap.
A dense ayah may carry many findings. The validators check complete coverage,
not a target count.

## Directory layout

```text
_commentary/v2/
  layer_2/
    discovery/PROMPT.md
    editorial/PROMPT.md
  layer_3/
    PROMPT.md
  shared/
    EDITORIAL_CONTRACT.md
    compiler/PROMPT.md
    schemas/
  scripts/
    workflow.py
    validate.py
  examples/
    s100.json
  tests/
```

Generated run artifacts are kept beneath the run's configured `outputRoot`:

```text
layer_2/
  discovery/inputs/
  discovery/outputs/
  editorial/inputs/
  editorial/outputs/
shared/
  compiler/inputs/
  compiler/outputs/
  reconciler/inputs/
  reconciler/outputs/
layer_3/
  inputs/
  outputs/
```

## Quick start

Instantiate one discovery prompt per ayah:

```sh
python3 _commentary/v2/scripts/workflow.py discovery \
  --config _commentary/v2/examples/s100.json
```

After the discovery agents have written their ledgers, instantiate the shared
pericope compiler:

```sh
python3 _commentary/v2/scripts/workflow.py compile \
  --config _commentary/v2/examples/s100.json \
  --pericope whole-surah
```

After the compiler has written the editorial plan and channel registry,
instantiate one final Layer 2 prompt per ayah:

```sh
python3 _commentary/v2/scripts/workflow.py author-layer2 \
  --config _commentary/v2/examples/s100.json \
  --pericope whole-surah
```

Instantiate Layer 3 after the channel registry exists:

```sh
python3 _commentary/v2/scripts/workflow.py author-layer3 \
  --config _commentary/v2/examples/s100.json \
  --pericope whole-surah
```

For a multi-pericope surah, reconcile the pericope registries first:

```sh
python3 _commentary/v2/scripts/workflow.py reconcile \
  --config path/to/run.json

python3 _commentary/v2/scripts/workflow.py author-layer3 \
  --config path/to/run.json \
  --surah-scope
```

Validate authored JSON artifacts:

```sh
python3 _commentary/v2/scripts/validate.py ledger path/to/100_1.ledger.json
python3 _commentary/v2/scripts/validate.py plan path/to/whole-surah.editorial-plan.json \
  --ledger-dir path/to/layer_2/discovery/outputs
python3 _commentary/v2/scripts/validate.py registry path/to/whole-surah.channel-registry.json \
  --ledger-dir path/to/layer_2/discovery/outputs

python3 _commentary/v2/scripts/validate.py reconciliation \
  path/to/whole-surah.registry-coverage.json \
  --registry path/to/whole-surah.channel-registry.json \
  --source-registry path/to/first.channel-registry.json \
  --source-registry path/to/second.channel-registry.json

python3 _commentary/v2/scripts/validate.py layer2-result \
  path/to/100_1.result.json \
  --ledger path/to/100_1.ledger.json \
  --plan path/to/pericope.editorial-plan.json

python3 _commentary/v2/scripts/validate.py layer3-result \
  path/to/whole-surah.channels.result.json \
  --registry path/to/whole-surah.channel-registry.json
```

The scripts only instantiate hermetic prompts and validate outputs. They do not
invoke a model.

## Long ayahs and long surahs

Operational sharding is allowed when an input exceeds a model context window.
Sharding is not selection: all shard findings must be merged into one ayah ledger
before the pericope compiler runs.

For long surahs, define editorial pericopes in the run configuration. The
reconciliation stage merges only their compact channel registries and emits
complete candidate coverage. It does not reread all Layer 2 prose or silently
claim that pericope boundaries are surah boundaries.

## Non-destructive rule

Discovery ledgers are immutable inputs to later stages. Editorial prose may
merge repetition and reorganize presentation, but every `carry` finding must
remain represented in the final Layer 2 result. Only a finding already marked
`blocked` in discovery may be absent.
