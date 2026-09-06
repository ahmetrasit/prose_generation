# Commentary v6

V6 copies V5's evidence preparation and prose workflow, adding bounded discovery
for large packets. V5 remains independent. Each lane receives short instructions,
a full evidence snapshot, and a deterministic reading plan. One scope agent
reviews successive batches, checkpoints useful observations, then revisits the
branch and connection catalogs before finalizing its discoveries.

```text
prepare
  -> micro, macro, global scope agents in parallel
  -> bounded discovery, checkpoints, cross-batch review, checked final discovery
  -> same three agents write scope prose
  -> one consolidator merges the three prose drafts without dropping findings
  -> same consolidator writes the editorial version without reducing coverage
  -> same consolidator validates only editorial prose and repairs up to 2 times
```

The only new execution helper is `discovery.py`: it reads the frozen packet,
records page delivery and batch completion in one visible work file per lane,
and checks source accounting before publishing final discovery. There is no
scheduler or extra agent tier. Launch V6 agents with the multiagent spawn tool,
not `codex exec`.

## Basic Command

Native focus:

```bash
python3 _commentary/v6/workflow.py prepare --ayah 29:38
```

Batch focus selectors are accepted:

```bash
python3 _commentary/v6/workflow.py prepare --ayah 100:1-11
python3 _commentary/v6/workflow.py prepare --ayah 1:1-7 2:1-5
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
length. They remain source identities, never array positions. V6 also compares
the delivered word-topic inventory with the source and refuses incomplete delivery.

```bash
python3 scripts/migrate_bundle_spans.py --report /tmp/v6-span-audit.json
python3 _commentary/v6/audit_preparation.py --whole-surah --workers 4 --report /tmp/v6-preparation.jsonl
```

The preparation audit renders and validates all three real packages for every
saved focus, including each pericope package's declared context. `--whole-surah`
also checks every numbered canonical focus against its full host surah. It
records failures, instruction and packet sizes, and batch counts, and exits
unsuccessfully if any preparation fails. It creates no agent artifacts or
handoffs. The 16 MB packet guard is a file limit, not a model-context or
semantic-quality guarantee.

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

The command writes three files per lane (shown for micro):

```text
_commentary/v6/input/<analysis-id>/sNNN/S_A/micro.discovery.prompt.md
_commentary/v6/input/<analysis-id>/sNNN/S_A/micro.packet.json
_commentary/v6/input/<analysis-id>/sNNN/S_A/micro.reading.json
```

Discovery uses `micro.work.json`, `macro.work.json`, and `global.work.json` in
the raw directory. These checkpoints preserve decisions, findings, useful
observations, and unfinished leads across compaction. The reader records
progress; the agent writes every analytical statement. `discovery.py finish`
writes the matching final files only after the completion checks pass:

```text
_commentary/v6/raw/<analysis-id>/sNNN/S_A/micro.discovery.json
_commentary/v6/raw/<analysis-id>/sNNN/S_A/macro.discovery.json
_commentary/v6/raw/<analysis-id>/sNNN/S_A/global.discovery.json
```

It also creates the matching raw and editorial output directories for agent
work:

```text
_commentary/v6/raw/<analysis-id>/sNNN/S_A/
_commentary/v6/editorial/<analysis-id>/sNNN/S_A/
```

The JSON printed by `prepare` contains the generated prompt paths, the
matching discovery and scope-prose output paths, the focus/context brief, and
short orchestration notes. It is advisory; it is not a completion manifest.

Scope packet v4 includes exact Arabic and typed QAC morphology for required
context references. `--qac-morphology` overrides the local `qac.sqlite.gz`
source; unavailable Arabic or morphology is listed in
`context_evidence_coverage`. Morpheme arrays use the explicitly supplied
`context_morpheme_columns`. These records establish forms and roots, not
activation of a dictionary branch.

QAC is streamed once into a local SQLite cache and queried read-only. The cache
defaults to the Git-ignored `_commentary/v6/.cache/qac`; `--qac-cache-dir`
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

The snapshot preserves every source record, wording, qualification, and original
identity. Nothing is filtered by retrieval strength or by candidate nomination.
The reader returns at most 24,000 UTF-8 bytes per page, with exact source
pointers. Branches of a root, candidate supports, and connection context are
grouped where they fit.
The default batch budget is 120,000 UTF-8 bytes (`--reading-budget` overrides
it). Byte budgets are conservative sizing, not measured model tokens. This
changes how evidence is consumed; it does not claim a 50% token reduction.

The reader opens the current batch and completed batches. Before advancing,
the agent saves a short `notes` entry with that `batch_id` and a source pointer
from the batch, plus any useful unfinished leads. Completion validates those
pointers immediately. Targeted `lookup` remains available across batches.
Evidence and catalog pages must reach the agent intact; analytical choices
cannot be supplied by default facets, fallback carriers, or generic templates.

After all batches, the same agent reviews all branch facets and connections
again using compact catalogs, follows cross-batch leads, and reopens full source
records as needed. Unresolved leads remain explicit in final friction notes.
The completion check verifies page/batch accounting and cited source identities;
it cannot prove attention, semantic adequacy, or exhaustive discovery. Resume
requires reloading the checkpoint and relevant source evidence, not trusting a
conversation summary for exact facts. Packet, instruction, and reader/helper
hashes prevent resuming against changed inputs or paging rules; use a fresh
analysis ID when they change.

The composition phase for each scope agent uses
`_commentary/v6/prompts/composition.md`. Fill it with the focus ref, lane,
that lane's `*.discovery.json` path, and that lane's `*.scope.tr.md` output
path from the prepare handoff.

V6 orchestration uses the operations monitor documented in
`_commentary/v6/ORCHESTRATION.md`. The monitor writes only operational runtime
state under `_commentary/v6/operations/runtime/`; that directory is not
commentary evidence and is not an analytical gate.

Consolidation receives all three discovery JSON objects as well as all three
scope prose files. Discovery evidence facts and exact branch fields control
source facts; scope prose controls intended coverage but may be corrected when
it demonstrably misstates grammar, morphology, or lexical identity.
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
python3 _commentary/v6/validate_prose.py \
  _commentary/v6/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
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
python3 _commentary/v6/workflow.py prepare \
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
python3 _commentary/v6/workflow.py prepare --ayah 29:0
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
python3 _commentary/v6/workflow.py prepare \
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

## Initial Verification

Independent review compared 33 real lane packets with V5, covering 29:38 native,
pericope, whole-surah and added-context preparations; large 22:5 and 73:20
packets; 87:0; sparse word identities in 5:3, 12:31 and 24:31; and 100:1 with
whole-surah context. Evidence was identical apart from version metadata.
Reconstructing the final reader's 4,059 pages recovered all 1,937,529 source
values exactly, including empty containers. No page exceeded 24,000 bytes.

| Global packet | Snapshot bytes | Batches | Reading pages |
| --- | ---: | ---: | ---: |
| 29:38, whole surah | 1,864,362 | 19 | 101 |
| 22:5, pericope | 7,442,993 | 72 | 404 |
| 73:20, native | 7,223,688 | 69 | 391 |

These counts exclude the final catalog review and any source lookups. Root
families stay together where the budget permits, so batches are not uniformly
full. They bound work between checkpoints, not the total work per lane.

Actual 29:38 preparation/resume checks preserved existing work, refused a changed
plan before writes, and confirmed that the monitor ignores partial checkpoints.
Synthetic checks covered oversized records and string fragments, interrupted
reading, cross-batch completion, source accounting, and refusal to overwrite a
final discovery. The 101 workflow/reader checks and 35 monitor checks passed.
The [first Luna semantic pilot](reviews/29-38-global-pilot-2026-09-06.md) completed
but exposed delayed checkpoints, filtered tool responses, and a wrong facet
choice that passed mechanical validation. Batch progression now requires a
source-grounded checkpoint, and the prompt explicitly requires intact page
reads and individual semantic judgments. The
[fresh rerun](reviews/29-38-global-rerun-2026-09-06.md) preserved batch reviews
through four compactions and removed the original facet error and boilerplate.
It still made false source-availability exclusions, and the inherited
core/extension rule induced an unsupported grammatical activation. These
semantic failures remain unresolved; the run does not establish large-packet
readiness.
