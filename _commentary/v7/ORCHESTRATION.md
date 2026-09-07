# Commentary v7 orchestration

This is the cold-agent runbook for V7. This file is authoritative;
`_commentary/v7/README.md` is a quick reference only. Run commands from the
repository root. Do not invoke V2/V3/V4 state machines, and do not use old prose
as evidence or as a checklist.

Use V5-style inline evidence and the generated V7 handoffs. Discovery is
encouraged at every stage. Preserve explicit evidence-to-interpretation chains;
earlier findings and exclusions are revisable judgments. Source facts come
from the original packets, not from earlier prose. Do not hand edit agent
outputs; corrections belong to the producing agent under the prompts.

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

V7 has no post-launch analytical gates. After `prepare`, do not run `advance`
or `verify`; they are not V7 commands. Do not create ledgers, manifests, hidden
state directories, or audit files for V7 orchestration. The only exception is
`_commentary/v7/operations/runtime/`, which is monitor-owned operational state,
ignored by Git, and never commentary evidence.

All agent launches in this runbook must use the multiagent spawn tool. Do not
launch V7 agents with `codex exec`, shell scripts, or ad hoc terminal sessions.

## Operations Monitor

Before preflight, start one operations monitor for this orchestrator and wait
for a JSON result with `"status": "started"`:

```bash
V7_MONITOR_PASSCODE='<operator-supplied-passcode>' \
python3 _commentary/v7/operations/monitor.py start \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --agent-id <orchestrator-agent-id> \
  --analysis-id <analysis-id> \
  --scope <scope-selector>
```

Use `commentary-v7` as the shared `run-id` unless the operator supplies a
different shared run ID. All machines participating in the same run must use
the same `run-id`.

The passcode must be at least 12 characters. If the operator did not provide
one in the orchestration request, ask for it before starting the monitor or
launching agents. Use the passcode only in the environment of this `monitor.py
start` command. Never write the plaintext passcode to a repository file,
runtime event, agent launch message, final response, or commit. Scope agents and
consolidators do not need the passcode.

The Firebase project and Web API key are already configured as monitor defaults.
Do not request, set, pass, or document Firebase credentials during ordinary V7
orchestration. Do not deploy Firebase, create a daemon script, copy a monitor
script, or add supervisor/queue/restart automation. The orchestrator runs the
existing `_commentary/v7/operations/monitor.py` script.

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
_commentary/v7/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/registration.json
_commentary/v7/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/events/sNNN/S_A/<task>.<attempt>.jsonl
_commentary/v7/operations/runtime/monitors/<run-id>/<orchestrator-id>.log
_commentary/v7/operations/runtime/monitors/<run-id>/<orchestrator-id>.pid
_commentary/v7/operations/runtime/snapshot.json
```

For scope agents, `<task>` is `micro`, `macro`, or `global`; for the
consolidator, `<task>` is `canonical`. These files are logs and dashboard state
only. Do not read them as commentary evidence, do not use them as analytical
state, and do not create any other tracking files. Do not ignore
`_commentary/v7/operations/` or its subfolders in general: `monitor.py` and the
operations docs are part of the orchestration tooling. Only `operations/runtime/`
is disposable monitor runtime state.

Immediately before beginning a new ayah, including a single-ayah run, the
orchestrator checks the daemon-maintained local pause marker without blocking:

```bash
python3 _commentary/v7/operations/monitor.py check \
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
python3 _commentary/v7/workflow.py prepare --ayah S:A
```

Pericope with external Fatiha:

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

The command writes three hermetic discovery prompts and five small follow-up
prompts under:

```text
_commentary/v7/input/<analysis-id>/sNNN/S_A/
```

It prints three handoffs:

```text
micro
macro
global
```

Each scope handoff gives its discovery prompt and `composition_prompt` path.
The result also includes `consolidation_handoff` and `editorial_handoff`.
Preparation renders all eight prompts before writing any of them. Later-stage
input paths refer to outputs that their preceding agents will produce; their
existence is required before those handoffs are sent. Discovery prompts contain
the sealed evidence, and follow-up prompts reference those same packets.

Production preparation checks QAC source availability before a batch and
required morphology coverage before returning handoffs. Stop on a preparation
error; do not launch from files left by an earlier run. Confirm
`context_morphology_status: complete` for each prepared unit. The
`--allow-missing-qac-morphology` override is for explicitly exploratory runs,
not this production procedure. Source checksums are recorded in the packets.

## 3. Scope Agents

Launch three fresh, independent agents in parallel with the multiagent spawn
tool, one for each prompt. Every scope agent must be `gpt-5.6-luna` at `max`
reasoning effort. Do not substitute another model, lower reasoning effort, or
launch with `codex exec`.

The scope-agent launch message may contain only the prompt path, the instruction
to follow it, and the start/terminal lifecycle command templates below. Do not
pass the monitor passcode or Firebase details to a scope agent. Use the spawn
task name as `--agent-id`; do not pass `--attempt`.

Before analysis, each scope agent runs:

```bash
python3 _commentary/v7/operations/monitor.py event \
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

Second turn: send the generated `composition_prompt` path from the lane's
prepare handoff to that same live agent and tell it to follow the prompt.
No template filling is needed. The prompt names the initial discovery JSON,
original evidence, and prose output. The agent develops all supported initial
findings and actively looks for further readings while writing. New findings
are fully explained in prose; the discovery JSON remains the initial snapshot.

Write each scope prose file under:

```text
_commentary/v7/raw/<analysis-id>/sNNN/S_A/
```

Use clear lane-specific filenames, for example:

```text
micro.scope.tr.md
macro.scope.tr.md
global.scope.tr.md
```

Do not edit the scope agents' files yourself. Once a scope agent has written its
requested scope prose file, it runs the same lifecycle command with one final
session status:

```bash
python3 _commentary/v7/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role scope \
  --lane <micro|macro|global> \
  --agent-id <spawn-task-name> \
  --status <completed|failed|interrupted|attention>
```

Use `completed` only after the requested scope prose file exists. Use `failed`
when required output could not be produced, `interrupted` when the lifecycle was
interrupted, and `attention` when operator attention is needed. Treat that final
event as the scope agent's lifecycle close. Continue the workflow with the files
the scope agents produced.

## 4. Consolidation

After all three scope prose files exist, close the scope agents. Start one
fresh `gpt-5.6-luna` agent at `max` reasoning effort as the consolidator. This
model and reasoning setting are mandatory for the consolidation and editorial
agent: do not substitute another model, do not lower reasoning effort, and do
not reuse a scope-agent session. Send the generated
`consolidation_handoff.prompt` path and lifecycle commands. Do not pass the
monitor passcode or Firebase details. Use the spawn task name as `--agent-id`;
do not pass `--attempt`.

The prompt names all three discovery JSON files, all three scope prose files,
and their original sealed evidence, and includes the focus/context brief.
No manual copying or template filling is required. The consolidator reads all
six authored inputs, preserves their supported readings, and investigates new
contacts across scopes. It can check source facts and reopen exclusions using
the original packet data. Current-stage instructions govern; the discovery
instructions surrounding those data blocks do not apply to consolidation.

The consolidator writes:

```text
_commentary/v7/raw/<analysis-id>/sNNN/S_A/S_A.prose.tr.md
```

Before consolidation, the consolidator runs:

```bash
python3 _commentary/v7/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role canonical \
  --agent-id <spawn-task-name> \
  --status started
```

Launch message:

```text
You are the V7 consolidator for <S:A>. You are running as a fresh gpt-5.6-luna
max agent.

Before consolidation, run this lifecycle command:
python3 _commentary/v7/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role canonical --agent-id <spawn-task-name> --status started

Read and follow this consolidation prompt exactly:
<consolidation_handoff.prompt path returned by prepare>

Write only the requested first-pass prose file. Keep this conversation open for
the editorial follow-up. Do not append a terminal lifecycle event yet.
```

The prose should be coherent Turkish, not a lane report or word-by-word
catalogue. The prompt already contains the mandatory non-compression rule:
every retained finding, and every distinct claim, image, branch activation, or
interpretive movement inside a scope paragraph, must land explicitly in prose.
Explicit landings may be woven into coherent composed prose; they do not require
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
reader-facing explanation. It also remains open to new readings and recovery
of missed explanations from the supplied original evidence.

Send the generated `editorial_handoff.prompt` path to the same consolidator.
Append any unit-specific editorial request to the follow-up message. The prompt
already names the first-pass input, original evidence, earlier authored inputs,
and exact editorial output. New findings belong in the editorial prose, fully
explained; do not require rewriting earlier artifacts or updating a ledger.

The editorial version must preserve all supported readings of the raw version
and explicitly explain newly discovered ones. Source-backed corrections may
repair factual errors; a defeated prior claim requires a brief explanation in
the completion reply, not silent deletion. It may change wording, cadence, clarity, and fluency; it may not remove
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
_commentary/v7/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

Follow-up message:

```text
Continue as the same V7 consolidator for <S:A>.

Read and follow this editorial prompt exactly:
<filled contents of _commentary/v7/prompts/editorial.md>

Write only the requested editorial prose file. Then run the validator command
specified in the prompt yourself on that editorial prose file only. If it fails,
repair only the reported mechanical prose-file issues and rerun it. Stop after
the validator passes or after two repair/rerun cycles, whichever comes first.
Then run exactly one terminal lifecycle command:
python3 _commentary/v7/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role canonical --agent-id <spawn-task-name> --status <completed|failed|interrupted|attention>

Use canonical completed only when the editorial validator passed. Use attention
when the editorial prose exists but the validator is still nonzero after the two
permitted repair/rerun cycles. Use failed when required output could not be
produced and interrupted when the lifecycle was interrupted. Report the final
validator result and lifecycle status in this conversation.
```

After writing the editorial file, the same consolidator must run the mechanical
downstream-safety validator itself. This validation applies only to the
editorial prose file, not to scope prose or first-pass prose:

```text
python3 _commentary/v7/validate_prose.py @@PROSE_OUTPUT_PATH@@
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
`canonical attention` event covering consolidation, editorial work, and the
validator/repair cycle.

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
python3 _commentary/v7/workflow.py prepare --ayah 29:0
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

When multiple ayat are selected, run the whole V7 workflow for those ayat in
parallel. Do not finish one ayah end to end before starting the next. Spawn the
three `gpt-5.6-luna` max scope agents for each ayah as soon as its prompts
exist; as each ayah's three scope prose files are ready, spawn that ayah's fresh
`gpt-5.6-luna` max consolidator and carry that same consolidator through the
editorial follow-up. Each ayah remains an independent workflow with its own
scope agents, consolidator, paths, and Git-visible outputs.

Different ayat and analysis IDs have disjoint paths and may run concurrently.
Do not run two orchestrators for the same analysis ID and ayah at once.

## Monitor Shutdown

After all ayat assigned to this orchestrator are complete and no spawned V7
agents remain live, stop the monitor:

```bash
python3 _commentary/v7/operations/monitor.py stop \
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
- If spawning fails before the new agent can write `started`, the orchestrator
  writes an `attention` event for the intended ayah, role, agent ID, and scope
  lane when applicable.
- Never fabricate `completed` from the presence of a response alone.
- Event messages must be short operational descriptions. Never put prose,
  evidence, prompts, or model reasoning in event logs.
- A rerun starts a new lifecycle with a new `started` event and receives the
  next attempt number automatically. Do not close or overwrite the earlier
  attempt to make the dashboard look successful.
