# Commentary v5 orchestration

This is the cold-agent runbook for V5. This file is authoritative;
`_commentary/v5/README.md` is a quick reference only. Run commands from the
repository root. Do not invoke V2/V3/V4 state machines, and do not use old prose
as evidence or as a checklist.

## Fixed Sequence

```text
prepare
  -> 3 fresh scope agents in parallel
  -> same 3 agents write their scope prose
  -> close scope agents
  -> 1 fresh consolidator merges the three prose drafts
  -> same consolidator writes the editorial version
  -> same consolidator validates the editorial prose only
  -> same consolidator repairs mechanical validator failures, up to 2 cycles
  -> close consolidator
```

V5 has no post-launch orchestration gates. After `prepare`, do not run `advance`
or `verify`; they are not V5 commands. Do not create ledgers, manifests, hidden
state directories, or audit files for V5 orchestration.

All agent launches in this runbook must use the multiagent spawn tool. Do not
launch V5 agents with `codex exec`, shell scripts, or ad hoc terminal sessions.

## 1. Preflight

For a native numbered focus, require:

```text
bundles/sNNN/S_A.ayah.json
```

Build a missing numbered bundle with:

```bash
python3 scripts/build_bundle.py --surah S --ayah A --out bundles/sNNN
```

For numbered focuses in S2-S8 and S10-S114, also require the host prefatory
basmala bundle:

```text
bundles/sNNN/S_0.ayah.json
```

S1 uses `1:1`; S9 has no prefatory basmala. Never create `1:0` or `9:0`.

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

Use the emitted `bundles/sNNN-pericopes/pPP_AAA-BBB/` directory as
`--context-bundles-dir`. Keep `bundles/` as `--member-bundles-dir` for the
mandatory host basmala and external ayat. Do not patch `scripts/build_bundle.py`
to orchestrate pericopes.

Every external ayah must be listed individually with `--add-ayat`; ranges are
invalid. Adding all of S1 requires:

```text
1:1,1:2,1:3,1:4,1:5,1:6,1:7
```

## 2. Prepare Prompts

Native:

```bash
python3 _commentary/v5/workflow.py prepare --ayah S:A
```

Pericope with external Fatiha:

```bash
python3 _commentary/v5/workflow.py prepare \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

The command writes three hermetic prompt files under:

```text
_commentary/v5/input/<analysis-id>/sNNN/S_A/
```

It prints three handoffs:

```text
micro
macro
global
```

Each handoff gives the exact prompt path. The prompts contain all evidence the
scope agents should use.

## 3. Scope Agents

Launch three fresh, independent agents in parallel with the multiagent spawn
tool, one for each prompt. Every scope agent must be `gpt-5.6-luna` at `max`
reasoning effort. Do not substitute another model, lower reasoning effort, or
launch with `codex exec`.

Give each agent only its prompt path and the instruction to follow that prompt.
Keep the session open after its first response.

First turn: each scope agent nominates the findings/candidates that matter for
its lane. It should decide supplied candidates and independently notice
uncandidate findings. It should not write final polished prose in this turn.
Macro prompts include a lane-specific external-ayat overlay procedure when
`--add-ayat` is present: the macro agent first assesses native/pericope context
and mandatory host basmala while quarantining explicitly added external ayat,
then separately reviews those external ayat for genuine deltas before finalizing
macro findings. This is part of the original macro discovery prompt, not a
separate agent or later follow-up.

Second turn: ask the same live scope agent to turn its nominated findings into
fluent Turkish scope prose. The prose should make activation explicit in normal
language: which root or ordinary meaning is activated, what in the focus carries
it, what in the context triggers it, and how the focus reading changes. It
should not expose internal root IDs or branch IDs to the reader.

Write each scope prose file under:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/
```

Use clear lane-specific filenames, for example:

```text
micro.scope.tr.md
macro.scope.tr.md
global.scope.tr.md
```

Do not edit the scope agents' files yourself. Once a scope agent has written its
requested files, continue the workflow with the files it produced.

## 4. Consolidation

After all three scope prose files exist, close the scope agents. Start one
fresh `gpt-5.6-luna` agent at `max` reasoning effort as the consolidator. This
model and reasoning setting are mandatory for the consolidation and editorial
agent: do not substitute another model, do not lower reasoning effort, and do
not reuse a scope-agent session. Use `_commentary/v5/prompts/canonical.md` as
the consolidation instruction template.

Fill that template manually before launching the agent:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@PROSE_OUTPUT_PATH@@` with the exact output path below;
- replace `@@FOCUS_CONTEXT_BRIEF@@` with the `focus_context_brief` object
  printed by `prepare`;
- replace `@@MICRO_SCOPE_PROSE@@`, `@@MACRO_SCOPE_PROSE@@`, and
  `@@GLOBAL_SCOPE_PROSE@@` with the complete contents of the three scope prose
  files;
- replace the governing-document placeholders with the current contents of the
  named local documents, or include those documents by path if the consolidator
  can read the workspace.

The consolidator writes:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/S_A.prose.tr.md
```

Launch message:

```text
You are the V5 consolidator for <S:A>. You are running as a fresh gpt-5.6-luna
max agent.

Read and follow this consolidation prompt exactly:
<filled contents of _commentary/v5/prompts/canonical.md>

Write only the requested first-pass prose file. Keep this conversation open for
the editorial follow-up.
```

The prose should be coherent Turkish, not a lane report or word-by-word
catalogue. The template already contains the mandatory non-compression rule:
every retained finding, and every distinct claim, image, branch activation, or
interpretive movement inside a scope paragraph, must land explicitly in prose.
Explicit landings may be woven into v2-style composed prose; they do not require
one paragraph per finding. If any retained landing is missing, the consolidator
should revise before treating the unit as complete.

Real Turkish section subtitles are allowed and encouraged when they make the
commentary easier to read. They must be marked as level-2 Markdown headings, for
example `## Taşın Hafızası`, so downstream renderers can style them separately.
They are reader prose, not wrapper labels. Do not use generic wrappers such as
`# PROSE`, `=== PROSE ===`, or XML-style prose wrappers.

When an Arabic word is doing interpretive work, tell the consolidator to use
the project display tag syntax:

```text
{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}
```

Tags are paragraph-local. A tag in an earlier paragraph does not cover a later
paragraph. If the same Arabic word, phrase, carrier, or anchor does
interpretive work again in a new paragraph, repeat the full tag in that
paragraph. This is required for downstream TTS and reader masking. Do not
deduplicate tags, reduce later paragraph tags, convert tagged anchors to plain
Arabic/transliteration, add QAC IDs, or invent another tag shape.

## 5. Editorial Follow-Up

Keep the same `gpt-5.6-luna` max consolidator live for editorial. The editorial
agent is not a new role or model; it is the same mandatory `gpt-5.6-luna` max
session that wrote the consolidated first-pass prose. Send one follow-up asking
for the editorial version. The editorial pass may rewrite sentences for
cadence, clarity, Turkish fluency, removal of English leakage, and better
reader-facing explanation. It must not add new evidence or erase a substantive
finding.

Use `_commentary/v5/prompts/editorial.md` as the editorial follow-up template.
Fill it manually:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@PROSE_INPUT_PATH@@` with the exact first-pass prose path;
- replace `@@PROSE_OUTPUT_PATH@@` with the exact editorial prose path below;
- replace `@@EDITORIAL_INSTRUCTIONS@@` with any unit-specific editorial request,
  or `No additional unit-specific instructions.`.

The editorial version must preserve the complete semantic coverage of the raw
version. It may change wording, cadence, clarity, and fluency; it may not remove
the carrier, independent trigger, contact, changed reading, concrete detail, or
boundary of any retained finding or distinct retained landing. It must also
preserve valid `{ar:..., tr:..., gloss:...}` display tags at every
paragraph-local Arabic anchor point.

Every inter-ayah or contextual comment in the editorial prose must show the
source ayah reference near the comment itself, normally in compact parentheses
like `(29:41)`. If several ayat jointly carry one movement, list every ayah
explicitly, such as `(29:17, 29:25)` or `(1:6, 1:7)`. Do not use ayah interval
shorthand such as `(1:6-1:7)`, `(1:6-7)`, or `(29:45-46)`. Do not leave context sources
as vague phrases such as "sûrenin ilerleyen yerinde", "bir yerde", "başka
yerde", or "sonlara doğru". Use the workflow/context reference visible to the
reader: a host prefatory basmala acting as context is cited as `(S:0)`, while
`(1:1)` is used only when Al-Fatiha 1:1 itself is being discussed as a separate
source or alias.

The consolidator writes:

```text
_commentary/v5/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

Follow-up message:

```text
Continue as the same V5 consolidator for <S:A>.

Read and follow this editorial prompt exactly:
<filled contents of _commentary/v5/prompts/editorial.md>

Write only the requested editorial prose file. Then run the validator command
specified in the prompt yourself on that editorial prose file only. If it fails,
repair only the reported mechanical prose-file issues and rerun it. Stop after
the validator passes or after two repair/rerun cycles, whichever comes first.
Report the final validator result in this conversation.
```

After writing the editorial file, the same consolidator must run the mechanical
downstream-safety validator itself. This validation applies only to the
editorial prose file, not to scope prose or first-pass prose:

```text
python3 _commentary/v5/validate_prose.py @@PROSE_OUTPUT_PATH@@
```

This check is limited to file-contract safety: existence, nonempty UTF-8 text,
downstream-renderable prose, unresolved placeholders, wrapper labels, malformed
braces, double-curly tags, unsupported or duplicate tag fields, and Arabic
script outside valid paragraph-local `{ar:..., tr:..., gloss:...}` tags. The
validator reports every detected issue, including every Arabic-outside span, but
keeps each finding line compact for repair. It does not judge semantic quality,
does not validate evidence, and does not create ledgers or hashes.

If validation returns nonzero, the same consolidator repairs only the reported
mechanical file-contract issues in the editorial prose file, reruns the
validator, and may do this at most two times. After two repair/rerun cycles,
accept the editorial prose as it stands and report the remaining validator
findings. Do not use validator failures to reopen evidence selection, add new
findings, drop findings, or launch a separate repair agent.

The orchestrating agent does not run this validator as a workflow gate. It
should only confirm that the consolidator reported either a passing validator
result or completion of the two permitted repair/rerun cycles with remaining
findings reported, then close the consolidator and inspect the prose quality
directly.

## Context Rules

- Micro is focus-local.
- Same-surah context in the focus segment is macro.
- Ordinary cross-segment or cross-surah context is global.
- Automatic host basmala and `--add-ayat` members are macro regardless of their
  source aliases.
- Added ayat are context-only and never become focus ayat implicitly.
- Every non-focus member uses the same lean native-context projection. A
  basmala does not import its standalone-focus payload into another focus.

For pericope focus `29:38`, `29:0`, `29:28-37`, `29:39-44`, and explicit
`--add-ayat` refs are non-focus macro context. The focus remains `29:38`.

For a dedicated basmala analysis:

```bash
python3 _commentary/v5/workflow.py prepare --ayah 29:0
```

The derived `s029-basmala-full` analysis puts all numbered S29 ayat in ordinary
lean macro context so they can activate basmala-focused resonances.

## Batch Rules

Use ranges or explicit sets and launch every returned handoff concurrently with
the multiagent spawn tool. Each item carries its own `ayah_ref`, `analysis_id`,
lane, and prompt path; do not infer them from list order.

When multiple ayat are selected, run the whole V5 workflow for those ayat in
parallel. Do not finish one ayah end to end before starting the next. Spawn the
three `gpt-5.6-luna` max scope agents for each ayah as soon as its prompts
exist; as each ayah's three scope prose files are ready, spawn that ayah's fresh
`gpt-5.6-luna` max consolidator and carry that same consolidator through the
editorial follow-up. Each ayah remains an independent workflow with its own
scope agents, consolidator, paths, and Git-visible outputs.

Different ayat and analysis IDs have disjoint paths and may run concurrently.
Do not run two orchestrators for the same analysis ID and ayah at once.

## Operational Rules

- Preflight checks happen before agent orchestration starts.
- After scope agents are launched, do not introduce validation gates outside the
  consolidator's editorial-only mechanical validator.
- Do not modify agent outputs yourself.
- Treat partial work as ordinary Git-visible state.
- Inspect the final prose before committing the unit.
