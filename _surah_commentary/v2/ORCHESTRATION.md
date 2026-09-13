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

- `scripts/workflow.py`: build, instantiate, validate.
- `prompts/10-editorial-outline.md`: select and ground the main movements.
- `prompts/11-editorial-compose.md`: compose the prelude and postlude.
- `prompts/12-editorial-edit.md`: integrate prose and clarify contributions.
- `schemas/editorial-outline-v1.schema.json`: outline output contract.
- `runs/editorial-v1/sNNN/{language}/{runId}/`: frozen inputs and run outputs.

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

Semantic review remains a separate human/operator gate when the operator wants
one. It is not encoded as a publication ceremony and must not be inferred from
a successful packet build, prompt instantiation, agent completion, or
mechanical validation.

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
three-line handoff. Record its Markdown prose output as `{DRAFT}` and validate:

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
Markdown prose output as `{EDITORIAL}` and validate:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py validate \
  --packet {PACKET} --outline {OUTLINE} --composition {EDITORIAL} --phase editorial
```

The edit already includes affirmative qualification, clarification of each
image's contribution, whole-surah continuity, and prose-first reader flow. Its
ending follows the given surah, not a fixed Fatiha sequence.

Keep the composition agent open through semantic acceptance and any needed
revision. In orchestration-only mode, keep it open until the operator either
accepts the output or requests another pass. Follow the V5 artifact style:
stage prompts and outputs use stable names, not attempt-numbered names. If a
composition fails mechanical validation, ask the same composition agent to
repair the same stage output file in place, limited to the reported mechanical
file-contract issue. Do not advance on an invalid output. An editorial rerun
can repair prose but must not silently alter the accepted outline; outline
changes require new composition and editorial passes.

## 5. Final Readability Pass

After the editorial prose validates mechanically, send this generic follow-up
verbatim to the same composition agent, replacing `{EDITORIAL}` with the exact
Markdown prose path:

```text
Revise the existing surah editorial prose in place at {EDITORIAL}.

Use only the same inline evidence and outline already supplied in this
conversation. Do not read other files.

Goal: make the text easier to read as coherent Turkish reader prose. Preserve
the supported readings, but remove the defensive/legal feel.

Specific revision instructions:
- Do not make the prose easier by omitting supported readings, outline
  movements, member contributions, concrete images, qualifications,
  uncertainty, or attribution. Improve readability by recasting, splitting,
  reordering, and connecting the existing material.
- Prefer affirmative secondary-layer language. Say what a resonance lets the
  reader hear, what it contributes, and how it shifts attention.
- Do not preserve boundary sentences in the form "bu X değildir", "kurmaz",
  "yüklemez", "anlamına gelmez", "sayılmaz", "dönüşmez", "oluşturmaz",
  "belirlenmez", "kapatmaz", "bağlamaz", or similar defensive denials. Rewrite
  them as affirmative scope: what the image contributes, where the layer works,
  what remains open, or what the reader should hear.
- If a source-level negation or boundary is truly necessary for truthfulness,
  express it as positive scope rather than a denial list. Prefer forms like
  "Katkısı şudur...", "Bu katman şu noktada çalışır...", "Bu imge şu hareketi
  duyurur...", "Açık kalan nokta şudur...", or "Burada sınır şu kadardır...".
- Make the postlude feel less like an audit report. Keep paragraphs organized
  around readerly movements, not around proving every constraint.
- Keep paragraph count flexible. Do not compress distinct movements, but let
  each paragraph have one clear object of attention.
- Remove repeated disclaimers and repeated formulations.
- Preserve truth conditions, uncertainty, attribution, and the outline's
  retained movements. Do not add evidence or new interpretations.
- Before finishing, search your revised prose mentally for repeated defensive
  endings and for words like "değildir", "kurmaz", "yüklemez", "anlamına
  gelmez", "sayılmaz", "dönüşmez", "oluşturmaz", "belirlenmez", "kapatmaz",
  and "bağlamaz". Rewrite every avoidable occurrence into affirmative prose.
- Write only the revised Markdown prose file at the same path. Do not write
  JSON, evidence maps, notes, or a separate report.
```

Validate `{EDITORIAL}` again after the pass:

```sh
python3 -B _surah_commentary/v2/scripts/workflow.py validate \
  --packet {PACKET} --outline {OUTLINE} --composition {EDITORIAL} --phase editorial
```

Keep the composition agent open if the operator may request another prose
revision.

## 6. Completion

Mechanical validation checks the file contract only: the prose exists, is
nonempty Markdown, is not JSON, and does not expose workflow metadata. It does
not prove that a reading is coherent or well supported. After editorial
validation and the final readability pass, `{EDITORIAL}` is the final run
artifact for this workflow.

If the operator requests semantic review, check especially that the prelude is
anticipatory; the postlude explains the main surprising readings without
becoming a catalogue; image functions are clear; scope and uncertainty survive;
and the primary reading remains visible. No source missing from the editorials
may be used to repair a gap.

Close the composition agent only when the operator is done with follow-up
revision. In orchestration-only mode, keep it open if requested. Report the
packet, outline, draft prose, and editorial prose paths. Do not claim semantic
success from a packet build, prompt instantiation, agent completion, or
mechanical validation.
