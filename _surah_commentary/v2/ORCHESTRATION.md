# Surah Commentary V2

The active workflow produces a prelude and postlude using **only the completed
editorial prose for every numbered ayah of one surah**. All semantic evidence
must come from those texts. It does not consume discovery, scope prose or
ledgers, invitations, separate translations, Quran datasets, lexical sources,
network/V11 evidence, or previous surah outputs. Intermediate outlines are
derived only from the same editorial snapshot.

This supersedes the channel-first workflow preserved in
`LEGACY_ORCHESTRATION.md`. Do not use its scripts or prompts for a new run.
The old `_channel/layer3` path is only a compatibility symlink.

## Active Files

- `scripts/workflow.py`: build, instantiate, validate, publish.
- `prompts/10-editorial-outline.md`: select and ground the main movements.
- `prompts/11-editorial-compose.md`: compose the prelude and postlude.
- `prompts/12-editorial-edit.md`: integrate prose and clarify contributions.
- `schemas/editorial-outline-v1.schema.json` and
  `schemas/editorial-composition-v1.schema.json`: semantic output contracts.
- `runs/editorial-v1/sNNN/{language}/{runId}/`: frozen inputs and run outputs.
- `outputs/sNNN/`: latest accepted reader surfaces and evidence.
- `publication-history/sNNN/{language}/`: preserved superseded stable files.

Scripts other than `workflow.py` and its `common.py` helper, prompts numbered
01-04, older schemas, `runs/v3/`, `packets/`, and old `inputs/` are historical.
Their richer evidence contract is not available to the active agents.

## Completion Gate

Start after the v5 orchestrator confirms every numbered ayah's final editorial
is complete, including any requested editorial follow-up. Use a single explicit
analysis ID; do not select by latest modification time or mix runs. Invitations
may finish independently and neither gate nor inform this workflow.

The operator supplies the surah number and its complete numbered ayah count as
scope metadata, not interpretation evidence. Confirm the count before building.
The builder requires every corresponding editorial directory and file, rejects
extra numbered directories, validates prose format, and checks for changes
during the snapshot. It cannot infer agent completion from file existence;
`--completed-by` records the responsible orchestrator/operator's attestation.
Do not use that flag while any selected editorial is still being revised.
Prefatory `S:0` units are outside this numbered-ayah contract.

## Orchestration-Only Mode

An operator may run this workflow in orchestration-only mode. In that mode, the
orchestrator builds packets, instantiates prompts, starts the requested fresh
agents, records their output paths, and runs mechanical validation only. The
orchestrator must not read composition outputs for meaning, prose quality,
coherence, anchor support, friction acceptance, or semantic approval.

Semantic review remains a separate human/operator gate. Publication still
requires an explicit `--approved-by` identity and must not be inferred from a
successful packet build, prompt instantiation, agent completion, or mechanical
validation.

## 1. Freeze Editorials

From the repository root:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py build \
  --analysis-id {ANALYSIS_ID} --surah {N} --ayah-count {COUNT} \
  --language tr --completed-by {OPERATOR_ID}
```

The only content files read are:
`_commentary/v5/editorial/{ANALYSIS_ID}/sNNN/S_A/S_A.prose.editorial.tr.md`.
Record the emitted path as `{PACKET}`. It contains the exact editorial texts,
source paths and hashes. Subsequent stages read this immutable snapshot, not
live editorial files. Source revisions require a new build, outline, and run.
No additional evidence handoff or final-editorial retention agent is required.

## 2. Outline

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py instantiate outline \
  --packet {PACKET}
```

Record both emitted paths: the generated prompt and its intended output.
Check that the selected model can accept the entire generated prompt plus
output allowance. Do not truncate editorial texts to fit; use a sufficient
context window or stop and report the limitation.
Use a fresh native semantic-agent conversation. Send only:

```text
Read the generated prompt at {PROMPT}.
Use only its inline evidence and instructions.
Write the requested JSON to its designated output path.
```

Do not supply upstream findings, outside knowledge, or an old surah reading.
Use the operator-selected model; this runbook does not prescribe a costly model.
Record the output as `{OUTLINE}`, then validate:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py validate \
  --packet {PACKET} --outline {OUTLINE}
```

A semantic reviewer should review the outline against the editorials before
composing, unless the operator has explicitly authorized an orchestration-only
run to proceed on mechanical validation alone. Check the genuine cross-ayah
relation, significant image coverage, each image's contribution, source
attribution, uncertainty and boundaries. Every ayah must be accounted for, but
the output is not required to compress every local finding. Do not invent a
whole-surah movement when the editorials do not support one. Close the outline
agent after acceptance; it does not compose the final prose.

## 3. Compose

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py instantiate compose \
  --packet {PACKET} --outline {OUTLINE}
```

Give the emitted prompt to a fresh native composition agent using the same
three-line handoff. Record its output as `{DRAFT}` and validate:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py validate \
  --packet {PACKET} --outline {OUTLINE} --composition {DRAFT} --phase draft
```

Keep this agent open for editorial revision.

## 4. Editorial Integration

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py instantiate edit \
  --packet {PACKET} --outline {OUTLINE} --composition {DRAFT}
```

Send the generated prompt to the same composition agent. Record the new
output as `{EDITORIAL}` and validate:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py validate \
  --packet {PACKET} --outline {OUTLINE} --composition {EDITORIAL} --phase editorial
```

The edit already includes affirmative
qualification, clarification of each image's contribution, and whole-surah
continuity. Its ending follows the given surah, not a fixed Fatiha sequence.

Keep the composition agent open through semantic acceptance and any needed
revision. In orchestration-only mode, keep it open until the operator either
accepts the output or requests another pass. Follow the V5 artifact style:
stage prompts and outputs use stable names, not attempt-numbered names. If a
composition fails mechanical validation, ask the same composition agent to
repair the same stage output file in place, limited to the reported mechanical
file-contract issue. Do not advance on an invalid output. An editorial rerun
can repair prose but must not silently alter the accepted outline; outline
changes require new composition and editorial passes.

## 5. Approval And Publication

Mechanical validation checks identities, hashes, exact source anchors, full
outline movement/member coverage, and unique prose anchors. It does not prove
that an anchor supports a claim or that the prose is coherent. A responsible
reviewer must check both surfaces against the editorials and outline, resolve
or explicitly accept friction, and approve the exact editorial revision.

Check especially that the prelude is anticipatory; the postlude explains the
main surprising readings without becoming a catalogue; image functions are
clear; scope and uncertainty survive; and the primary reading remains visible.
No source missing from the editorials may be used to repair a gap.

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py publish \
  --packet {PACKET} --outline {OUTLINE} --composition {EDITORIAL} \
  --approved-by {REVIEWER_ID} --publish-stable
```

Only `phase: editorial` can be published. Approval is an explicit attestation,
not an automatic consequence of passing validation. The publisher first saves
an immutable, content-addressed revision under the run's `published/` directory.
The exact packet, outline, and composition are archived under `accepted/` with
the same revision ID, so later changes to working outputs cannot erase lineage.
With `--publish-stable`, it preserves any prior managed stable files in
`publication-history/`, then replaces only these four files under `outputs/sNNN/`:

```text
N.surah-reading.prelude.{language}.md
N.surah-reading.postlude.{language}.md
N.surah-reading.evidence.{language}.json
N.surah-reading.friction.{language}.md
```

Without `--publish-stable`, publication is run-local only. Revisions and old
run artifacts remain intact. Concurrent publishers are serialized. Each file
is replaced atomically, with evidence committed last; the four-file set is not
a single filesystem transaction. Readers should verify the evidence surface
hashes and retry on mismatch. Ordinary write failures roll back the changed
files; a process crash can be recovered from the preserved prior set or by
republishing the accepted revision.

Close the composition agent after acceptance and publication. Report the two
reader paths and any accepted friction. Do not claim a successful semantic run
from a packet build or a fixture test alone.
