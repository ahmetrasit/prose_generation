# Layer 3 v3 Implementation Status

Status as of 2026-08-17: **paused mid-implementation; not ready to run**.

## Completed before this Layer 3 change

- Layer 2 now uses `_ayah_commentary/v2/PROMPT.md` through
  `scripts/instantiate.py`.
- The Layer 2 v2 prompt, rewrite prompt, runbook, and related references were
  aligned around explicit local resonances, no disambiguation, selective word
  analysis, four artifacts, and no prose quota.
- Those Layer 2 changes were committed as `c605d60f` and pushed to
  `origin/main`.

## Adversarial review completed

A read-only `gpt-5.6-sol` agent at maximum reasoning reviewed the proposed
Layer 3 migration. Its main required corrections were:

1. use a separately authored, typed primary floor rather than Layer 2 prose;
2. hand off the complete Layer 2 findings index, not only `surprise:` rows;
3. account for hypotheses and local resonances many-to-many, without ranking or
   treating merged material as discarded;
4. preserve every admitted channel and hinge in reader-visible prose;
5. emit and validate prose, evidence, and friction with immutable source
   lineage;
6. fail closed when a Layer 2 artifact set or typed floor is incomplete.

## Drafted in the current worktree

- `_channel/layer3/scripts/common.py`
  - canonical hashing and SHA-256 helpers;
  - normalized language tags;
  - immutable/idempotent generated-file writes;
  - portable source-path resolution.
- `_channel/layer3/scripts/build_packet.py`
  - replaced with a draft v3 packet builder;
  - requires a typed Layer 1 primary floor;
  - selects one complete prose/evidence/index/friction set per ayah;
  - parses every findings-index row and typed local resonance;
  - hashes all four Layer 2 artifacts while withholding prose and friction from
    semantic passes;
  - preserves explicit evidence boundaries;
  - projects Network V3 activation cards and bounded V11 material;
  - derives source-set/packet hashes and an immutable run identity.
- `_channel/layer3/scripts/validate.py`
  - newly drafted functional validators for packets, hypotheses, briefs,
    composition envelopes, and final evidence lineage.

The three drafted Python files pass AST syntax parsing. They have not passed
functional tests or a real packet build.

## Important intermediate-state warning

The active Layer 3 workflow is currently inconsistent and must not be run:

- `build_packet.py` now emits `layer3-source-packet-v3`;
- `instantiate.py`, the active prompts, and active schemas still expect the old
  v2 packet and v1 briefs.

Historical packets, prompts, briefs, and readings under
`_channel/layer3/{packets,inputs,outputs}/` have not been modified.

## Remaining work

1. Add new immutable schemas:
   - `layer2-handoff-v1.schema.json`;
   - `source-packet-v3.schema.json`;
   - `discovery-hypotheses-v2.schema.json`;
   - `channel-briefs-v2.schema.json`;
   - `surah-composition-v1.schema.json`;
   - `surah-reading-evidence-v1.schema.json`.
2. Rewrite `_channel/layer3/scripts/instantiate.py` for v3 run directories,
   per-attempt immutable paths, stage validation, and language-aware filenames.
3. Update all three Layer 3 prompts:
   - discovery remains blind to Layer 2;
   - review receives typed primary ground, complete findings, local resonances,
     boundaries, and complete non-channel accounting;
   - composition makes every admitted channel/hinge explicit in ordinary reader
     language, permits incompatible channels to coexist, and imposes no word,
     paragraph, channel-count, or length quota.
4. Add a deterministic finalizer that validates one composition envelope and
   emits:
   - `N.surah-reading.{language}.md`;
   - `N.surah-reading.evidence.{language}.json`;
   - `N.surah-reading.friction.{language}.md`.
5. Reconcile the packet/validator drafts against the schemas and review all
   referential checks. Syntax success is not sufficient.
6. Update `_channel/layer3/ORCHESTRATION.md`, `COMMENTARY_SPEC.md`,
   `docs/CHANNELS.md`, root/channel README references, and the retired combined
   workflow notice in `scripts/README.md`.
7. Replace the stale `tests/test_layer3_channel_workflow.py` with runnable
   standard-library tests covering strict handoff selection, malformed indexes,
   many-to-many channel use, complete dispositions, bounded claim policies,
   immutable paths, and final prose landings/hashes.
8. Run syntax checks, unit tests, `git diff --check`, synthetic multi-channel
   tests, and a real S87 smoke build in a temporary directory. Confirm all
   historical generated artifacts remain byte-identical.

## Concurrent focus-trace work

Separate focus-trace work arrived concurrently in:

- `_commentary/ORCHESTRATION.md`;
- `docs/FOCUS_TRACE_INTEGRATION.md`;
- `docs/SOURCES.md`;
- `scripts/README.md`;
- `scripts/build_bundle.py`;
- `scripts/test_build_bundle_focus_trace.py`.

Those changes were committed and pushed separately as `ccb04ee7` while this
Layer 3 implementation was in progress. They are no longer dirty worktree
changes. Do not revert or broadly rewrite them; patch only the Layer 3-specific
portions of overlapping documentation.

## Plan position

- Migration invariants: complete.
- Adversarial review: complete.
- Packet/schema/prompt/validation implementation: in progress.
- Runbook/spec alignment: pending.
- Tests: pending.
- Real-surah smoke validation: pending.
