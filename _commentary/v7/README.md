# Commentary v7

V7 starts from V5's deterministic preparation and inline hermetic evidence.
V6 is a reference for observed failures; none of its delivery or checkpoint
implementation is used here. Source evidence remains complete. Discovery v3
uses one self-contained explanation and source references per finding, instead
of repeating the reasoning across several semantic fields.

The purpose is to reveal secondary readings that expand, complicate, or shift
the main reading. Each reading must show its particular evidence, its connection
to the passage, and the resulting interpretation, with a brief boundary where
needed. Coherence comes from arranging those explanations, not compressing them
into generalized prose. Discovery stays open and encouraged in every stage.
Novelty, uncertainty, earlier exclusion, and absence from a candidate list are
not automatic vetoes; source facts and interpretive inferences stay distinct.

The code validates inputs, assembles the evidence, and renders ready-to-use
prompts for all stages. There are no semantic acceptance gates, checkpoints, or
finding ledgers. The initial 29:38 pilot exposed generic discovery fields and
lost explanations in later prose. The revised handoffs preserve complete inputs
and source records.

The second 29:38 Luna max pilot, `pilot-29-38-p03-fatiha-r2-202609070227`, used
the same pericope plus Fatiha evidence. All five later handoffs reproduced their
authored inputs verbatim, and editorial format validation passed. Semantic
review was mixed: some explanations recovered, but the first pilot's five
additional global readings were missing from discovery, lexical connections
still disappeared in prose, and consolidation introduced a verse attribution
error that editorial retained (household rescue assigned to 29:31, rather than
29:32). This revision remains experimental; successful evidence transport and
format checks do not establish adequate discovery or preservation.

```text
prepare
  -> micro, macro, global scope agents in parallel
  -> same three agents write scope prose after nomination
  -> one consolidator connects the scope readings and develops further findings
  -> same consolidator clarifies every reading and remains open to discovery
  -> same consolidator validates only editorial prose and repairs up to 2 times
```

There is no V7 state machine after `prepare`: no `advance`, no `verify`, no
manifest audit, and no hidden session registry. After preparation,
orchestration is normal agent management and Git-visible files. Launch V7
agents with the multiagent spawn tool, not `codex exec`.

## Basic Command

Native focus:

```bash
python3 _commentary/v7/workflow.py prepare --ayah 29:38
```

Batch focus selectors are accepted:

```bash
python3 _commentary/v7/workflow.py prepare --ayah 100:1-11
python3 _commentary/v7/workflow.py prepare --ayah 1:1-7 2:1-5
```

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
length. They remain source identities, never array positions. V7 also compares
the delivered word-topic inventory with the source and refuses incomplete delivery.

```bash
python3 scripts/migrate_bundle_spans.py --report /tmp/v7-span-audit.json
python3 _commentary/v7/audit_preparation.py --whole-surah --workers 4 --report /tmp/v7-preparation.jsonl
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

For a batch, run the complete workflow for all selected ayat in parallel. Each
ayah gets its own three `gpt-5.6-luna` max scope agents and its own fresh
`gpt-5.6-luna` max consolidator/editorial session.

Preparation writes three evidence-bearing discovery prompts. Later handoffs
are rendered after their required agent outputs exist:

```text
_commentary/v7/input/<analysis-id>/sNNN/S_A/micro.discovery.prompt.md
_commentary/v7/input/<analysis-id>/sNNN/S_A/macro.discovery.prompt.md
_commentary/v7/input/<analysis-id>/sNNN/S_A/global.discovery.prompt.md
_commentary/v7/input/<analysis-id>/sNNN/S_A/<lane>.composition.prompt.md
_commentary/v7/input/<analysis-id>/sNNN/S_A/canonical.prompt.md
_commentary/v7/input/<analysis-id>/sNNN/S_A/editorial.prompt.md
```

The first scope-agent turn writes the matching discovery files under `raw/`:

```text
_commentary/v7/raw/<analysis-id>/sNNN/S_A/micro.discovery.json
_commentary/v7/raw/<analysis-id>/sNNN/S_A/macro.discovery.json
_commentary/v7/raw/<analysis-id>/sNNN/S_A/global.discovery.json
```

It also creates the matching raw and editorial output directories for agent
work:

```text
_commentary/v7/raw/<analysis-id>/sNNN/S_A/
_commentary/v7/editorial/<analysis-id>/sNNN/S_A/
```

The JSON printed by `prepare` contains the generated prompt paths, the
matching discovery and scope-prose output paths, `composition_prompt` for each
lane, `consolidation_handoff`, `editorial_handoff`, the focus/context brief, and
short orchestration notes. Each scope has a `render_composition` command;
consolidation and editorial each have a `render` command. This result is
advisory, not a completion manifest.

Scope packet v4 includes exact Arabic and typed QAC morphology for required
context references. `--qac-morphology` overrides the local `qac.sqlite.gz`
source; unavailable Arabic or morphology is listed in
`context_evidence_coverage`. Morpheme arrays use the explicitly supplied
`context_morpheme_columns`. These records establish forms and roots, not
activation of a dictionary branch.

QAC is streamed once into a local SQLite cache and queried read-only. The cache
defaults to the Git-ignored `_commentary/v7/.cache/qac`; `--qac-cache-dir`
overrides it. Each use hashes the compressed source, so even a same-size source
replacement cannot reuse stale data. Concurrent preparations share an atomic,
validated cache. Packets identify the source by its stable logical name and
SHA-256 of the compressed bytes; local corpus/cache paths stay out of that
provenance. The cache is preparation infrastructure, not agent input.

Production preparation requires a readable QAC source and all required context
morphology. The CLI checks the source once before starting a batch, and each
focus checks coverage before writing prompts or returning handoffs. For an
explicitly exploratory run, `--allow-missing-qac-morphology` preserves Arabic
with missing-evidence qualifications and reports `context_morphology_status:
degraded` in the preparation result. Do not use this override in production.

Prompts supply complete evidence records with their wording and qualifications
together. Existing candidate, support, branch, and ayah IDs connect records;
new prompts contain no `$v7_ref` string lookups or shared-value table. Some
wording is deliberately repeated to keep records readable, without summarizing
or omitting source details. Agents use the stateless `authoring.py read` command
for complete records or exact text windows, without custom parsers or filtered
tool responses. It saves no reading state and certifies no semantic coverage.
No external evidence file is needed. `packet_evidence.expand_packet` remains a
decoder for historical v3 packets only.

After discovery, run the lane's `render_composition` command and send the
resulting `<lane>.composition.prompt.md` to the same scope agent. After all
three scope prose files exist, run `consolidation_handoff.render` and send
`canonical.prompt.md` to one fresh agent. After its first pass exists, run
`editorial_handoff.render` and send `editorial.prompt.md` to that same agent.
For example:

```bash
python3 _commentary/v7/authoring.py handoff --analysis-id native --ayah 29:38 --stage composition --lane micro
python3 _commentary/v7/authoring.py handoff --analysis-id native --ayah 29:38 --stage canonical
python3 _commentary/v7/authoring.py handoff --analysis-id native --ayah 29:38 --stage editorial
```

Each handoff embeds its complete authored inputs verbatim and copies the cited
source records with all their fields. Discovery validation checks identities,
references, and candidate accounting only; it cannot approve or reject a
semantic reading. Missing inputs fail before writing a handoff. Agent outputs
are never rewritten by this command. Agents read the complete authoring inputs
and consult the source appendix as needed; it requires no repeated exhaustive
source survey. Unit-specific editorial instructions may accompany the follow-up.

The compact [reading standard](prompts/reading-standard.md) is rendered into
every stage. Later agents can consult the original `<lane_packet_json>` blocks;
those blocks are source data, while the current stage prompt governs the task.
Initial discovery JSON remains a historical snapshot. New findings are written
explicitly into the current prose output and carried forward through prose;
there is no requirement to revise old outputs or maintain another registry.
The original evidence controls source facts. Correct factual errors without
suppressing supported secondary readings. Briefly explain a correction that
defeats an earlier claim in the completion reply rather than silently losing it.

V7 uses the inherited operations monitor documented in
[ORCHESTRATION.md](ORCHESTRATION.md). Its Git-ignored runtime state is operational
only, not an analytical gate. The existing `v5-monitor` Firebase project remains
the configured backend; V7 uses its own run IDs and artifact directories.

Every contextual interpretation must cite its source ayah beside the claim.
List individual references such as `(1:6, 1:7)`, not intervals. Cite host
prefatory basmala context as `(S:0)`. Arabic interpretive anchors use the full
paragraph-local `{ar:..., tr:..., gloss:...}` display tags in every prose stage.

When `--add-ayat` is present, only the macro prompt gets an external-ayat
overlay procedure. The macro agent first nominates native/pericope and mandatory
host-basmala findings, then separately checks the explicit external ayat for
genuine delta activations before it writes macro prose.

After editorial prose is written, the same consolidator runs the mechanical
downstream-safety validator on the editorial prose file only:

```bash
python3 _commentary/v7/validate_prose.py \
  _commentary/v7/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
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
python3 _commentary/v7/workflow.py prepare \
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
python3 _commentary/v7/workflow.py prepare --ayah 29:0
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
python3 _commentary/v7/workflow.py prepare \
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
