# Commentary V8 Batch

V8 Batch is an executable-source copy of V5 with one bounded transport change:
the three discovery turns run through the OpenAI Batch API. Composition and all
later prose turns remain regular agents. Generated V5 inputs, outputs, runtime
state, and caches were deliberately not copied into this source tree.

```text
prepare
  -> exact micro, macro, global discovery prompts enter Batch
  -> collector validates and freezes all discovery JSON
  -> three fresh regular Luna max agents compose scope prose
  -> one consolidator merges the three prose drafts without dropping findings
  -> same consolidator writes the editorial version without reducing coverage
  -> same consolidator validates only editorial prose and repairs up to 2 times
  -> script writes one hermetic prose-only middle-layer prompt per ayah
  -> one fresh Luna max agent writes and validates the middle prose
  -> the same agent receives the fixed generic audit through its workspace path
  -> orchestrator closes it without inspecting the middle-layer output
  -> one fresh invitation agent writes the separate reading invitation
```

The default agent input contract is the compact early V5 workflow from
`41763703` (September 3, before the later expansion). Discovery keeps the
original candidate ownership, support/branch organization, lean selected
context, and discovery v1 response schema. All word-analysis topics remain in
micro, including topics whose source explanations mention another ayah.
The four governing documents in `guidance/` are pinned to that revision and
embedded in full. Later shared project-document edits cannot silently change
this V5 contract.

Exact QAC/analysis links, sparse topic preservation, source validation, root-ID
corrections, unresolved-branch handling, basmala/external-context support, the
QAC cache, monitor lifecycle, and prose formatting/validation fixes remain.
The later candidate rerouting, generated semantic/review inventories, and bulk
context-morphology registry are not part of newly prepared agent inputs. Source
data and historical expanded packets remain available in the repository.

There is no analytical state machine after `prepare`: no `advance`, no `verify`,
and no hidden session registry. V8 adds only a small Batch transport manifest of
paths, identities, and hashes; it contains no evidence duplication. New post-editorial middle-layer
runs persist only their reader prose; inventories, semantic audits, and metrics
remain transient agent work. Historical V2 claim ledgers and their validator
remain available as legacy artifacts but are not inputs to new runs. After
discovery collection, orchestration returns to normal agent management and
Git-visible files. Launch regular V8 agents with the multiagent spawn tool, not
`codex exec`.

## Basic Command

Native focus:

```bash
python3 _commentary/v8_batch/workflow.py prepare --ayah 29:38
```

Batch focus selectors are accepted:

```bash
python3 _commentary/v8_batch/workflow.py prepare --ayah 100:1-11
python3 _commentary/v8_batch/workflow.py prepare --ayah 1:1-7 2:1-5
```

After preparation, Batch only the discovery turns:

```bash
python3 _commentary/v8_batch/batch_discovery.py build \
  --analysis-id <analysis-id> --ayah 12:1-111 --name s012-discovery
python3 _commentary/v8_batch/batch_discovery.py submit \
  --manifest _commentary/v8_batch/batches/s012-discovery.manifest.json
python3 _commentary/v8_batch/batch_discovery.py status \
  --submission _commentary/v8_batch/batches/s012-discovery.submission.json
python3 _commentary/v8_batch/batch_discovery.py collect \
  --manifest _commentary/v8_batch/batches/s012-discovery.manifest.json \
  --submission _commentary/v8_batch/batches/s012-discovery.submission.json
```

`collect` prints the path-only handoffs for the fresh regular composition
agents and the actual standard-equivalent, Batch, and saved discovery dollars.
It never retries a failed request. See `COSTS.md` for the S12 projection.

Before bulk operation, check the actual saved inventory. The first command
checks whether deterministic word-to-morpheme joins need migration; add
`--apply` to regenerate only those joins and their coverage. It also updates
surah coverage summaries and existing package manifests. Source analysis and
agent outputs are preserved. Reviewed source exclusions remain explicit.

New generation and migration use the accepted `analysis_qac_edges` in
`quran-data/data/bridges/qac-masaq.sqlite.gz`. Analysis identities are separate
from QAC identities: a whole expression and its component can share morphemes.
The loader verifies release checksums, bridge version and source metadata,
the released analysis, and the bundled QAC rows. Missing, changed or incompatible
sources fail preparation; source exclusions are retained with their reasons.
The compressed databases are streamed into the existing disk cache, and one
verified connection per process serves subsequent ayat. Local paths never enter
the recorded bridge provenance.

Legacy ordered spans retain their strict contract. Bridge-backed spans carry
`analysis_ref` and verified QAC links instead of an exclusive traversal's
`morpheme_skip_count`. Preparation verifies the complete mapping and its
provenance against the release before allowing overlaps. This migration applies
to canonical, prefatory and pericope copies through the same generation path.
Bridge-verified analysis IDs may be sparse and larger than the analysis array's
length. They remain source identities, never array positions. V5 also compares
the delivered word-topic inventory with the source and refuses incomplete delivery.

```bash
python3 scripts/migrate_bundle_spans.py --report /tmp/v5-span-audit.json
python3 _commentary/v8_batch/audit_preparation.py --whole-surah --workers 4 --report /tmp/v5-preparation.jsonl
```

The preparation audit renders and validates all three real prompts for every
saved focus, including each pericope package's declared context. `--whole-surah`
also checks every numbered canonical focus against its full host surah. It
records every failure and prompt byte size and exits unsuccessfully if any
preparation fails. It creates no agent artifacts or handoffs. Large byte sizes
still require a separate reading-efficiency review; the 16 MB guard is a file
limit, not a model-context or semantic-quality guarantee.

For an S:0 focus, its complete numbered host must be available in one context
root. A basmala bundle can already serve as package context while those numbered
inputs still live in separate pericope collections. Generate the whole-surah
root with `scripts/build_bundle.py --surah S` before using its native S:0 focus;
the audit reports any missing host files explicitly.

For a selected production command, append `--check-only` to perform its full
preparation without writing prompts. A successful result has `status: checked`.
The QAC cache may be populated. `focus_word_alignment` in every new lane packet
identifies the bridge provenance, shared morphemes and excluded source units.
Each word candidate also carries `word_alignment` with its analysis identity,
exact QAC refs and status. Shared morphology does not make distinct semantic
claims duplicates; excluded entries retain their source readings and qualification.

For a batch, prepare all selected ayat, Batch all discovery requests, then run
each ayah's three fresh regular `gpt-5.6-luna` max composition agents and its
normal downstream sessions.

The command writes one prompt per lane:

```text
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/micro.discovery.prompt.md
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/macro.discovery.prompt.md
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/global.discovery.prompt.md
```

The collector materializes the matching validated discovery files under `raw/`:

```text
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/micro.discovery.json
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/macro.discovery.json
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/global.discovery.json
```

It also creates the matching raw and editorial output directories for agent
work:

```text
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/
_commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/
```

The JSON printed by `prepare` contains the generated prompt paths, the
matching discovery and scope-prose output paths, the focus/context brief, and
short orchestration notes. It is advisory; it is not a completion manifest.

The scope packet uses the original v1 organization, with the additive
`focus_word_alignment` and candidate `word_alignment` correctness fields.
Source supports retain their full text and qualifications. Selected context,
connection evidence, and existing source projections are supplied as before;
the later `context_evidence`, `context_morpheme_columns`, and generated
`review_inventory` sections are not inserted. Their absence does not establish
that a nominated interpretation is false. Agents stay within the evidence
actually supplied by the lane packet.

For 29:38, five individually reviewed source items supplement that contract
when their owning candidates are present. Micro's `reference_evidence` supplies
the complete Arabic and typed QAC rows for 7:201 and 29:39, supporting the
already-nominated participle comparisons. Macro's `lexical_evidence` supplies
dictionary quotations, source names, form restrictions, and sense boundaries
for `root_000347/B011`, `root_001222/B008`, and `root_001273/B012` (socket/join,
tent frame, and upright support). These are selected branch fields, not whole
root dictionaries. `_commentary/v8_batch/reviewed_supplements.py` fixes the reviewed
references and source locations; it does not expand other context automatically.
The raw evidence adds 4,306 / 4,527 bytes to micro / macro, respectively.

Preparation reports `agent_input_contract: early-v5-compact` and
`context_morphology_status: targeted` when those reviewed QAC references are
included, otherwise `not_requested`. Neither status claims a complete context
morphology registry. The `reviewed_supplements` handoff records the included
references, QAC source hash, and lexical source pointers. Missing required
Arabic, QAC rows, or dictionary fields stop preparation before prompts are
written. Production CLI preflight still checks a readable QAC source;
`--qac-morphology` and `--qac-cache-dir` configure that check. The cache and
historical packet utilities remain available, including the decoder for saved
v3 `$v5_ref` transport. The exploratory `--allow-missing-qac-morphology` flag
skips the source preflight; it does not bypass focus bridge validation or the
required reviewed-source checks.

Collection fills the unchanged
`_commentary/v8_batch/prompts/composition.md` and generates a path-only
`*.composition-from-batch.prompt.md` for a fresh regular Luna max agent. That
handoff reads the exact discovery prompt, frozen JSON, and filled composition
prompt in order. The scope prose remains publishable Markdown. The sidecar
ledger maps every retained discovery movement to a paragraph-local exact anchor
without duplicating the prose or governing documents. The composition agent
runs `validate_scope_ledger.py` and any required repair inside its one turn;
there is no later orchestrator follow-up or retry.

V8 orchestration uses the operations monitor documented in
`_commentary/v8_batch/ORCHESTRATION.md`. The monitor writes only operational runtime
state under `_commentary/v8_batch/operations/runtime/`; that directory is not
commentary evidence and is not an analytical gate.

Consolidation receives the three scope prose files, a focus/context brief, and
the four full pinned guidance documents. Discovery JSON is not appended.
Composition agents carry their frozen findings and necessary explanations into
prose. The consolidator can correct a demonstrable inconsistency from
the supplied texts, while retaining uncertainty where those texts do not
establish a correction.
Consolidation is prose work, not evidence selection. Every retained scope
finding must keep its carrier, independent trigger, contact, changed reading,
concrete semantic detail, and boundary visible in the reader-facing result.
When one scope paragraph contains multiple claims, images, branches, or
movements, each distinct one is a separate mandatory landing.
Editorial rewriting may improve Turkish and cadence, but it must not reduce
that coverage. In editorial prose, every inter-ayah or contextual comment must
show the source ayah reference near the comment itself, normally in compact
parentheses like `(29:41)`. If several ayat carry one comment, every ayah must
be listed explicitly, such as `(1:6, 1:7)`; interval shorthand such as `(1:6-7)`
is not allowed in reader prose. Use the workflow/context reference visible to
the reader, so a host prefatory basmala acting as context is cited as `(S:0)`.

When `--add-ayat` is present, only the macro prompt gets an external-ayat
overlay procedure. The macro agent first nominates native/pericope and mandatory
host-basmala findings, then separately checks the explicit external ayat for
genuine delta activations before it writes macro prose.

After editorial prose is written, the same consolidator runs the mechanical
downstream-safety validator on the editorial prose file only:

```bash
python3 _commentary/v8_batch/validate_prose.py \
  _commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

This checks format safety only, including downstream-renderable prose, malformed
tags, double-curly tags, unsupported or duplicate tag fields, unresolved
placeholders, wrapper labels, and Arabic script outside valid paragraph-local
`{ar:..., tr:..., gloss:...}` tags. It lists every detected issue, including
every Arabic-outside span, in compact line-oriented output. A nonzero result
stays with the same consolidator: it fixes only the reported mechanical
editorial-prose issue and reruns the validator, with at most two repair/rerun
cycles. After that, the editorial prose is accepted as-is and any remaining
validator findings are reported. It does not reopen evidence selection or launch
another agent.

After the final editorial follow-up, render the required middle-layer prompt:

```bash
python3 _commentary/v8_batch/workflow.py prepare-middle \
  --ayah <S:A> \
  --analysis-id <analysis-id>
```

The command atomically writes one complete hermetic prompt and returns two
short path-only messages. Spawn one fresh `gpt-5.6-luna` max agent and send
exactly `handoff.launch_message`. After its first turn, keep the same agent and
send exactly `handoff.follow_up_message`, which points to the fixed canonical
audit file. Never inline, copy, quote, summarize, or load either file into the
orchestrator conversation.

The same agent re-inventories the source, rebuilds its synthesis clusters,
performs the structural warning challenge, repairs only the prose, and runs
both prose validators again. The orchestrator does not inspect, diff, validate,
summarize, or customize the output and never sends an output-derived message.
It does not retry, rerun, relaunch, or replace the agent if the stage fails.
The only new durable middle-layer output is:

```text
_commentary/v8_batch/middle/<analysis-id>/sNNN/S_A/S_A.prose.middle.tr.md
```

Existing `*.middle.claims.json` files and
`validate_middle_layer.py` belong to the legacy V2 workflow. New prompts do not
read, modify, or recreate them; new prose uses `validate_middle_prose.py`.

The invitation remains derived from final editorial prose, not middle prose.

Reader-facing section subtitles are allowed in consolidated and editorial
prose when they improve readability. They must be marked as level-2 Markdown
headings, for example `## Taşın Hafızası`, so downstream renderers can style
them separately. They are not wrappers; generic labels such as `# PROSE`,
`=== PROSE ===`, and XML-style prose wrappers remain invalid.

## Context And External Ayat

An ordered analysis uses named segments. Same-surah context in the focus
segment is macro; ordinary cross-segment or cross-surah context is global.

Explicit external ayat use `--add-ayat`. They are first-class, context-only
members of `--member-surah`, enter macro once, retain their original Quran
identity, and receive root cues conditioned by the host-surah focus. They never
become focus ayat implicitly. The option accepts comma-separated individual refs
and rejects ranges. For non-S1/S9 host analyses, the default external Fatiha
complement starts at `1:2` because `1:1` is already represented by the mandatory
host prefatory basmala `S:0`:

```bash
python3 _commentary/v8_batch/workflow.py prepare \
  --analysis-id s100-with-fatiha \
  --segment host=100:1-11 \
  --member-surah 100 \
  --add-ayat 1:2,1:3,1:4,1:5,1:6,1:7 \
  --ayah 100:1-11
```

## Basmala Policy

For every numbered focus in S2-S8 and S10-S114, the host `S:0` prefatory
basmala is mandatory. It enters macro exactly once as the same lean, ordinary
non-focus context projection used for any other context ayah. It does not carry
its standalone-focus payload into another ayah's prompt.

S1 already contains its basmala as `1:1`; S9 has no prefatory basmala. `1:0`
and `9:0` are invalid.

A prefatory basmala can itself be the focus:

```bash
python3 _commentary/v8_batch/workflow.py prepare --ayah 29:0
```

That derives analysis `s029-basmala-full` with `29:0,29:1-69` in one host
segment. All numbered host ayat become ordinary lean macro context. The focus
surface remains `29:0`; its canonical linguistic source `1:1` is an alias, not
external context.

## Pericope Packages

Use the dedicated wrapper instead of adding pericope behavior to
`scripts/build_bundle.py`:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

For a pericope plus external Fatiha context:

```bash
python3 _commentary/v8_batch/workflow.py prepare \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

Focus and ordinary pericope members come from the package root. Automatic
basmala and explicit external members may come from the member root. If an
external member exists in both roots, the canonical bundle content must agree.

See [ORCHESTRATION.md](ORCHESTRATION.md) for the cold-agent runbook.
