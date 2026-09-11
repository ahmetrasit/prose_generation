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
  -> same consolidator revises qualification/image presentation
  -> same consolidator validates the editorial prose again
  -> same consolidator repairs mechanical validator failures, up to 2 cycles
  -> close consolidator
  -> render the invitation prompt from final editorial prose
  -> 1 fresh invitation agent writes and validates the reading invitation
  -> close invitation agent
```

V5 has no post-launch analytical gates. After `prepare`, do not run `advance`
or `verify`; they are not V5 commands. Do not create ledgers, manifests, hidden
state directories, or audit files for V5 orchestration. The only exception is
`_commentary/v5/operations/runtime/`, which is monitor-owned operational state,
ignored by Git, and never commentary evidence.

All agent launches in this runbook must use the multiagent spawn tool. Do not
launch V5 agents with `codex exec`, shell scripts, or ad hoc terminal sessions.

## Operations Monitor

Before preflight, start one operations monitor for this orchestrator and wait
for a JSON result with `"status": "started"`:

```bash
V5_MONITOR_PASSCODE='<operator-supplied-passcode>' \
python3 _commentary/v5/operations/monitor.py start \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --agent-id <orchestrator-agent-id> \
  --analysis-id <analysis-id> \
  --scope <scope-selector>
```

Use `commentary-v5` as the shared `run-id` unless the operator supplies a
different shared run ID. All machines participating in the same run must use
the same `run-id`.

The passcode must be at least 12 characters. If the operator did not provide
one in the orchestration request, ask for it before starting the monitor or
launching agents. Use the passcode only in the environment of this `monitor.py
start` command. Never write the plaintext passcode to a repository file,
runtime event, agent launch message, final response, or commit. Scope agents and
consolidators do not need the passcode.

The Firebase project and Web API key are already configured as monitor defaults.
Do not request, set, pass, or document Firebase credentials during ordinary V5
orchestration. Do not deploy Firebase, create a daemon script, copy a monitor
script, or add supervisor/queue/restart automation. The orchestrator runs the
existing `_commentary/v5/operations/monitor.py` script.

For cloud operation, `"status": "started"` means the passcode-backed Firebase
registration succeeded and the background monitor process was launched. If
monitor startup fails or does not return `"status": "started"`, do not launch
analysis agents. Report the startup error to the operator.

Each orchestrator uses an `orchestrator-id` that is unique across all
participating machines and accounts. One monitor registration covers one
`analysis-id`; repeat `--scope` when needed. Valid scope selectors are `S`,
`S-T`, `S:A`, and `S:A-B`.

The monitor writes local operational files under:

```text
_commentary/v5/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/registration.json
_commentary/v5/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/events/sNNN/S_A/<task>.<attempt>.jsonl
_commentary/v5/operations/runtime/monitors/<run-id>/<orchestrator-id>.log
_commentary/v5/operations/runtime/monitors/<run-id>/<orchestrator-id>.pid
_commentary/v5/operations/runtime/snapshot.json
```

For scope agents, `<task>` is `micro`, `macro`, or `global`; for the
consolidator, `<task>` is `canonical`; for the reading-invitation writer it is
`invitation`. These files are logs and dashboard state only. Do not read them
as commentary evidence, do not use them as analytical state, and do not create
any other tracking files. Do not ignore
`_commentary/v5/operations/` or its subfolders in general: `monitor.py` and the
operations docs are part of the orchestration tooling. Only `operations/runtime/`
is disposable monitor runtime state.

Immediately before beginning a new ayah, including a single-ayah run, the
orchestrator checks the daemon-maintained local pause marker without blocking:

```bash
python3 _commentary/v5/operations/monitor.py check \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

The command returns immediately with `running` or `paused`. On `running`, begin
the ayah. On `paused`, do not launch that ayah's scope agents; report the paused
state and leave already-running ayat alone. The daemon will remove the marker
after a remote resume. Do not check between steps of an active ayah, poll
Firebase directly, or introduce direct remote messaging to agents.

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
invalid. For non-S1/S9 host analyses, the default external Fatiha complement is
S1 after the basmala, because the host prefatory basmala is already present as
`S:0`. Use:

```text
1:2,1:3,1:4,1:5,1:6,1:7
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
  --add-ayat 1:2,1:3,1:4,1:5,1:6,1:7 \
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

Production preparation checks QAC source availability before a batch and
validates the focus's accepted analysis/QAC bridge and complete word-topic
delivery. Stop on a preparation error; do not launch from files left by an
earlier run. Confirm `agent_input_contract: early-v5-compact` for each prepared
unit. `context_morphology_status` is `targeted` when the individually reviewed
29:38 reference additions are included, otherwise `not_requested`. The
`reviewed_supplements` handoff identifies the supplied sources. Preparation
requires those selected sources to be present; neither status claims a bulk
context morphology registry. The `--allow-missing-qac-morphology` source-preflight
override is for explicitly exploratory runs, not this production procedure.

## 3. Scope Agents

Launch three fresh, independent agents in parallel with the multiagent spawn
tool, one for each prompt. Every scope agent must be `gpt-6-astra` at `high`
reasoning effort. Do not substitute another model, lower reasoning effort, or
launch with `codex exec`.

The scope-agent launch message may contain only the prompt path, the instruction
to follow it, and the start/terminal lifecycle command templates below. Do not
pass the monitor passcode or Firebase details to a scope agent. Use the spawn
task name as `--agent-id`; do not pass `--attempt`.

Before analysis, each scope agent runs:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role scope \
  --lane <micro|macro|global> \
  --agent-id <spawn-task-name> \
  --status started
```

Keep the session open after its first response. The same scope agent must not
append a terminal event after its first-turn nomination response.

First turn: each scope agent nominates the findings/candidates that matter for
its lane. It should decide supplied candidates and independently notice
uncandidate findings. It should not write final polished prose in this turn.
Macro prompts include a lane-specific external-ayat overlay procedure when
`--add-ayat` is present: the macro agent first assesses native/pericope context
and mandatory host basmala while quarantining explicitly added external ayat,
then separately reviews those external ayat for genuine deltas before finalizing
macro findings. This is part of the original macro discovery prompt, not a
separate agent or later follow-up.

Second turn: keep the same live scope agent and use
`_commentary/v5/prompts/composition.md` as the follow-up template. Fill it before
sending:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@LANE@@` with `micro`, `macro`, or `global`;
- replace `@@DISCOVERY_OUTPUT_PATH@@` with that lane's exact
  `*.discovery.json` path from the prepare handoff;
- replace `@@SCOPE_PROSE_OUTPUT_PATH@@` with that lane's exact
  `*.scope.tr.md` output path from the prepare handoff.
- replace `@@SCOPE_LEDGER_OUTPUT_PATH@@` with that lane's exact
  `*.scope.ledger.json` output path from the prepare handoff.

Ask the same agent to turn its nominated findings into fluent Turkish scope
prose. The prose should make activation explicit in normal language: which root
or ordinary meaning is activated, what in the focus carries it, what in the
context triggers it, and how the focus reading changes. It should not expose
internal root IDs or branch IDs to the reader.

Write each scope prose and non-prose landing-ledger pair under:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/
```

Use clear lane-specific filenames, for example:

```text
micro.scope.tr.md
micro.scope.ledger.json
macro.scope.tr.md
macro.scope.ledger.json
global.scope.tr.md
global.scope.ledger.json
```

The landing ledger is compact accountability metadata. It must not be appended
to reader prose or expose internal IDs there. The composition template requires
the scope agent to run `validate_scope_ledger.py` against its discovery, prose,
and ledger. Do not edit the scope agents' files yourself. Once a scope agent has
written both requested files and the ledger validator reports `ok`, it runs the
same lifecycle command with one final session status:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role scope \
  --lane <micro|macro|global> \
  --agent-id <spawn-task-name> \
  --status <completed|failed|interrupted|attention>
```

Use `completed` only after the requested scope prose and ledger files exist and
the ledger validator reports `ok`. Use `failed` when required output could not
be produced, `interrupted` when the lifecycle was interrupted, and `attention`
when operator attention is needed. Treat that final event as the scope agent's
lifecycle close. Continue the workflow with the files the scope agents produced.

## 4. Consolidation

After all three scope prose files exist, close the scope agents. Start one
fresh `gpt-6-astra` agent at `high` reasoning effort as the consolidator. This
model and reasoning setting are mandatory for the consolidation and editorial
agent: do not substitute another model, do not lower reasoning effort, and do
not reuse a scope-agent session. Use `_commentary/v5/prompts/canonical.md` as
the consolidation instruction template. Do not pass the monitor passcode or
Firebase details to the consolidator. Use the spawn task name as `--agent-id`;
do not pass `--attempt`.

Fill that template manually before launching the agent:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@PROSE_OUTPUT_PATH@@` with the exact output path below;
- replace `@@FOCUS_CONTEXT_BRIEF@@` with the `focus_context_brief` object
  printed by `prepare`;
- replace `@@PRINCIPLES_MD@@`, `@@COMMENTARY_SPEC_MD@@`, `@@CHANNELS_MD@@`, and
  `@@CANONICAL_PROMPT_V2@@` with the complete contents of
  `_commentary/v5/guidance/PRINCIPLES.md`,
  `_commentary/v5/guidance/COMMENTARY_SPEC.md`,
  `_commentary/v5/guidance/CHANNELS.md`, and
  `_commentary/v5/guidance/PROMPT_V2.md`, respectively;
- replace `@@MICRO_SCOPE_PROSE@@`, `@@MACRO_SCOPE_PROSE@@`, and
  `@@GLOBAL_SCOPE_PROSE@@` with the complete contents of the three scope prose
  files.
- replace `@@MICRO_SCOPE_LEDGER@@`, `@@MACRO_SCOPE_LEDGER@@`, and
  `@@GLOBAL_SCOPE_LEDGER@@` with the complete contents of the three validated
  scope landing-ledger files.

The consolidation package contains the three scope prose texts, their validated
landing ledgers, full pinned guidance, and the focus/context brief. Discovery
JSON stays with the scope agents and is not appended to this package. Scope
prose and ledgers form the consolidator's complete evidence boundary. They
control intended coverage; a demonstrable inconsistency may be corrected from
those supplied inputs without adding evidence or silently dropping a finding.
The governing documents' historical multi-file output instructions are
subordinate to the V5 prose-only handoff.

The consolidator writes:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/S_A.prose.tr.md
```

Before consolidation, the consolidator runs:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role canonical \
  --agent-id <spawn-task-name> \
  --status started
```

Launch message:

```text
You are the V5 consolidator for <S:A>. You are running as a fresh gpt-6-astra
high agent.

Before consolidation, run this lifecycle command:
python3 _commentary/v5/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role canonical --agent-id <spawn-task-name> --status started

Read and follow this consolidation prompt exactly:
<filled contents of _commentary/v5/prompts/canonical.md>

Write only the requested first-pass prose file. Keep this conversation open for
the editorial follow-up. Do not append a terminal lifecycle event yet.
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

Keep the same `gpt-6-astra` high consolidator live for editorial. The editorial
agent is not a new role or model; it is the same mandatory `gpt-6-astra` high
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
Keep this conversation open for the final qualification/image presentation
follow-up. When that final follow-up arrives, apply it to the same editorial
prose file, then run the editorial prose validator again on that same file and
repair only mechanical validator failures, up to two cycles. After the
post-follow-up validator passes or the two repair cycles are exhausted, run
exactly one terminal canonical lifecycle event and report the final validator
result and lifecycle status. Do not append a terminal lifecycle event before
that final follow-up is complete.
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

Do not add a separate validator agent, validator event, or per-step progress
event. The consolidator has one `canonical started` event and one final
`canonical completed`, `canonical failed`, `canonical interrupted`, or
`canonical attention` event covering consolidation, editorial work, the
qualification/image presentation follow-up, and validator/repair cycles.

The orchestrating agent does not run this validator as a workflow gate. It
should only confirm that the consolidator reported either a passing validator
result or completion of the two permitted repair/rerun cycles with remaining
findings reported, then close the consolidator and inspect the prose quality
directly.

## 6. Qualification/Image Presentation Follow-Up

Keep the same `gpt-6-astra` high consolidator live after the editorial validator
has passed or completed its permitted repair/rerun cycles. Send this exact
message verbatim as the final CE writing follow-up:

```text
Revise only the presentation of qualifications and the clarity of image
  contributions in the editorial prose. Lead with what each resonance
  contributes and describe its scope affirmatively where possible.

  Avoid repeatedly listing unused images merely to exclude them. When such a
  list expresses a substantive restriction, preserve that restriction in a
  concise sentence attached to the relevant reading. Retain explicit exclusions
  wherever affirmative wording would leave the boundary ambiguous.

  Where several images or details accumulate, clarify what each contributes to
  the reading and how their contributions relate. Make the existing connections
  easier to follow without inventing new connections or removing concrete
  details.

  Make clear that a restriction concerns this particular connection, rather than
  declaring other readings invalid. Preserve every retained finding, concrete
  image, evidence attribution, uncertainty level, and substantive qualification.
  Do not strengthen claims or add interpretations.
```

This follow-up rewrites the same editorial prose file in place:

```text
_commentary/v5/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

It is not a new evidence-selection stage and must not inspect upstream evidence,
add findings, drop findings, strengthen claims, or create any extra artifacts.
The validation and terminal lifecycle instructions must have been supplied in
the earlier editorial follow-up message so this final CE writing follow-up can
remain exactly the quoted text. After writing the revised editorial prose, the
same consolidator must run:

```text
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

If validation returns nonzero, the same consolidator repairs only the reported
mechanical file-contract issues in the editorial prose file, reruns the
validator, and may do this at most two times. After the validator passes, or
after two repair/rerun cycles with remaining findings reported, the same
consolidator runs exactly one terminal lifecycle command:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role canonical \
  --agent-id <spawn-task-name> \
  --status <completed|failed|interrupted|attention>
```

Use canonical `completed` only when the final editorial prose exists and the
post-follow-up validator passed. Use `attention` when the final editorial prose
exists but validation remains nonzero after the two permitted repair/rerun
cycles. Use `failed` when required output could not be produced and
`interrupted` when the lifecycle was interrupted. Report the final validator
result and lifecycle status in this conversation.

## 7. Reading Invitation

After CE has written, revised, and validated the final editorial prose, generate the
separate reading invitation as the final required stage for that ayah. This
derivative follows one or two main channels of resonance in two to four
Turkish paragraphs. A channel is a connected background of meanings, images,
actions, or relations that the editorial develops through several details.
Select across the complete editorial prose for interpretive consequence and
clear grounding. Start with the expression that opens a channel, unfold its
connected background, and show how the ayah sounds or reads against it, making
an expansion or shift of its main meaning intelligible. Reveal a distinctive
reading in the first paragraph and preserve its force and qualifications.

One developed channel is sufficient. The invitation does not compress findings
individually, and no finding, channel, or major shift is mandatory coverage.
Other channels may remain entirely in the commentary. A modest explanation
of the main meaning or a collection of unusual details is insufficient when
the source develops a more revealing channel. Use only connections developed
in the editorial; if it supplies none, explain its strongest grounded reading.

Render its hermetic prompt from the completed editorial prose:

```bash
python3 _commentary/v5/workflow.py prepare-invitation \
  --ayah <S:A> \
  --analysis-id <analysis-id>
```

The command writes
`_commentary/v5/input/<analysis-id>/sNNN/S_A/invitation.prompt.md` and returns a
fresh-agent handoff whose output is
`_commentary/v5/editorial/<analysis-id>/sNNN/S_A/S_A.invitation.tr.md`.

Start one fresh `gpt-6-astra` high agent with no inherited conversation history.
Give it only the filled invitation prompt. Do not reuse the consolidator session
or supply scope prose, scope ledgers, discovery outputs, first-pass prose,
evidence packets, or project-governance documents. The finished editorial prose
is the invitation's sole semantic source: this keeps its promise aligned with
what the reader will encounter. The summary is selective; it does not repeat
every reading or introduce discoveries absent from the editorial prose.

The invitation agent writes only the separate invitation artifact and runs the
mechanical prose validator named in the prompt. It does not modify the editorial
commentary. It must append one `invitation started` lifecycle event before
writing and exactly one terminal `invitation completed`, `invitation failed`,
`invitation interrupted`, or `invitation attention` event after validation.
Use `completed` only when the invitation exists and its validator passed. Use
`attention` when it exists but validation remains nonzero after the permitted
repair cycles.

Launch message:

```text
You are the V5 reading-invitation writer for <S:A>. You are running as a fresh
gpt-6-astra high agent.

Before writing, run this lifecycle command:
python3 _commentary/v5/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role invitation --agent-id <spawn-task-name> --status started

Read and follow this invitation prompt exactly:
<complete contents of the generated invitation.prompt.md>

After validation, run exactly one terminal lifecycle command:
python3 _commentary/v5/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role invitation --agent-id <spawn-task-name> --status <completed|failed|interrupted|attention>

Report the final validator result and lifecycle status in this conversation.
```

Inspect and report the invitation separately from the completed commentary.
Check that the reader can follow the selected channel from its opening
expression through its connected background to an expanded or shifted reading
of the ayah. Check fidelity of the connections and qualifications, not coverage
of omitted findings or channels. Mechanical validation does not establish this
semantic quality. Regenerate it whenever its editorial source changes.
The monitor considers a
newly registered ayah complete only after both CE validation and invitation
validation have completed.

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

The nonblocking Operations Monitor pause check applies before the first
scope-agent launch for each ayah in the batch. Do not omit it for single-ayah
runs or batch runs. A `paused` result defers only ayat that have not started;
it does not interrupt or hold the terminal for active ayat.

When multiple ayat are selected, run the whole V5 workflow for those ayat in
parallel. Do not finish one ayah end to end before starting the next. Spawn the
three `gpt-6-astra` high scope agents for each ayah as soon as its prompts
exist; as each ayah's three scope prose files are ready, spawn that ayah's fresh
`gpt-6-astra` high consolidator and carry that same consolidator through the
editorial follow-up and qualification/image presentation follow-up. Each ayah
remains an independent workflow with its own scope agents, consolidator,
invitation agent, paths, and Git-visible outputs. As soon as an ayah's CE stage
completes, render and launch its invitation; do not wait for CE to finish on the
other ayat.

Different ayat and analysis IDs have disjoint paths and may run concurrently.
Do not run two orchestrators for the same analysis ID and ayah at once.

## Monitor Shutdown

After all ayat assigned to this orchestrator are complete and no spawned V5
agents remain live, stop the monitor:

```bash
python3 _commentary/v5/operations/monitor.py stop \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

Shutdown performs at most two final sync attempts, then exits even if Firebase
is unavailable. `status: stop_requested` is a successful bounded response: the
detached monitor is finishing those attempts in the background. Unsynced local
runtime state remains local rather than keeping the orchestrator blocked
indefinitely.

## Operational Rules

- Preflight checks happen before agent orchestration starts.
- After scope agents are launched, do not introduce validation gates outside the
  consolidator's editorial-only mechanical validator.
- Do not modify agent outputs yourself.
- Treat partial work as ordinary Git-visible state.
- Inspect the final prose before committing the unit.
- If a launched agent terminates before appending its final lifecycle event,
  leave its start event incomplete. That is how the dashboard identifies a
  possible stall.
- Monitor or lifecycle logging mismatches are operational only. Do not rerun
  content, relaunch agents, or change the workflow solely to fix monitor state.
  Hand-record the operational issue if useful; if it cannot be repaired, leave
  it and continue from the content files that were produced and validated.
- If spawning fails before the new agent can write `started`, the orchestrator
  writes an `attention` event for the intended ayah, role, agent ID, and scope
  lane when applicable.
- Never fabricate `completed` from the presence of a response alone.
- Event messages must be short operational descriptions. Never put prose,
  evidence, prompts, or model reasoning in event logs.
- A rerun starts a new lifecycle with a new `started` event and receives the
  next attempt number automatically. Do not close or overwrite the earlier
  attempt to make the dashboard look successful.
