# Commentary V8 Batch orchestration

This is the cold-agent runbook for V8 Batch. This file is authoritative;
`_commentary/v8_batch/README.md` is a quick reference only. Run commands from the
repository root. Do not invoke V2/V3/V4 state machines, and do not use old prose
as evidence or as a checklist.

## Fixed Sequence

```text
prepare
  -> exact discovery prompts enter OpenAI Batch
  -> collector validates and freezes discovery JSON
  -> 3 fresh regular Luna max agents write their scope prose
  -> close composition agents
  -> 1 fresh consolidator merges the three prose drafts
  -> same consolidator writes the editorial version
  -> same consolidator validates the editorial prose only
  -> same consolidator repairs mechanical validator failures, up to 2 cycles
  -> same consolidator revises qualification/image presentation
  -> same consolidator validates the editorial prose again
  -> same consolidator repairs mechanical validator failures, up to 2 cycles
  -> close consolidator
  -> script renders one hermetic prose-only middle-layer prompt
  -> send only the script-produced workspace-path launch message
  -> 1 fresh Luna max agent writes and validates middle prose
  -> same agent receives only the fixed workspace-path audit message
  -> same agent re-inventories, challenges synthesis, repairs, and validates again
  -> close the agent without orchestrator output inspection
  -> render the invitation prompt from final editorial prose
  -> 1 fresh invitation agent writes and validates the reading invitation
  -> close invitation agent
```

V8 has no orchestrator-run post-launch analytical gates. After `prepare`, do
not run `advance` or `verify`; they are not V8 commands. The only manifest is
the minimal script-produced Batch transport manifest; do not create hidden
state directories or ad hoc analytical audit files.
New middle-layer runs persist only their reader prose; inventories, audit
checklists, metrics, and span maps remain transient agent work. Historical V2
claim ledgers remain untouched legacy artifacts. The sole state exception is
`_commentary/v8_batch/operations/runtime/`, which is monitor-owned operational state,
ignored by Git, and never commentary evidence.

All agent launches in this runbook must use the multiagent spawn tool. Do not
launch V5 agents with `codex exec`, shell scripts, or ad hoc terminal sessions.

## Run-Scoped Model Overrides

The standing V5 model assignments are `gpt-5.6-luna` at `max` reasoning effort
for scope, post-editorial middle-layer, and invitation agents, and `gpt-5.6-sol`
at `max` reasoning effort for the CE consolidator/editorial session. Every
middle-layer run uses one fresh Luna max agent for both its authoring turn and
its fixed follow-up audit turn.

An operator may explicitly supply a model override for a particular run. Treat
that override as scoped to the named run only; do not rewrite the standing model
defaults for later V5 work. For the next fresh S1 run requested after
2026-09-11, use `gpt-6-astra` at `high` reasoning effort for every agent stage:
scope discovery/composition, CE consolidation/editorial/qualification follow-up,
and invitation.

The post-editorial middle-layer agent is fixed to fresh `gpt-5.6-luna` at `max`
and is not changed by the historical S1 Astra override above. Change that
assignment only when an operator explicitly overrides the middle-layer stage.

## Operations Monitor

Before preflight, start one operations monitor for this orchestrator and wait
for a JSON result with `"status": "started"`:

```bash
V5_MONITOR_PASSCODE='<operator-supplied-passcode>' \
python3 _commentary/v8_batch/operations/monitor.py start \
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
existing `_commentary/v8_batch/operations/monitor.py` script.

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
_commentary/v8_batch/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/registration.json
_commentary/v8_batch/operations/runtime/runs/<run-id>/orchestrators/<orchestrator-id>/events/sNNN/S_A/<task>.<attempt>.jsonl
_commentary/v8_batch/operations/runtime/monitors/<run-id>/<orchestrator-id>.log
_commentary/v8_batch/operations/runtime/monitors/<run-id>/<orchestrator-id>.pid
_commentary/v8_batch/operations/runtime/snapshot.json
```

For regular composition agents, `<task>` is `micro`, `macro`, or `global`; for the
consolidator, `<task>` is `canonical`; for the reading-invitation writer it is
`invitation`. These files are logs and dashboard state only. Do not read them
as commentary evidence, do not use them as analytical state, and do not create
any other analytical tracking files. The Batch manifest and submission record
are script-owned transport metadata, not commentary evidence. Do not ignore
`_commentary/v8_batch/operations/` or its subfolders in general: `monitor.py` and the
operations docs are part of the orchestration tooling. Only `operations/runtime/`
is disposable monitor runtime state.

Immediately before beginning a new ayah, including a single-ayah run, the
orchestrator checks the daemon-maintained local pause marker without blocking:

```bash
python3 _commentary/v8_batch/operations/monitor.py check \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

The command returns immediately with `running` or `paused`. On `running`, begin
the ayah. On `paused`, do not submit that ayah's discovery prompts; report the paused
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
python3 _commentary/v8_batch/workflow.py prepare --ayah S:A
```

Pericope with external Fatiha:

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

The command writes three hermetic prompt files under:

```text
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/
```

It prints three handoffs:

```text
micro
macro
global
```

Each handoff gives the exact prompt path. The prompts contain all evidence the
Batch discovery request and later replacement composition agent should use.

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

## 3. Batch Discovery, Then Regular Composition

Discovery has no correction or reviewer follow-up. In V5, composition itself is
the planned second turn of the same scope session. Only discovery moves to the
OpenAI Batch API in V8; composition and every later prose step remain regular
agent turns.

Build the Batch request files from the exact prompts written by `prepare`:

```bash
python3 _commentary/v8_batch/batch_discovery.py build \
  --analysis-id <analysis-id> \
  --ayah S:A-S:B \
  --name <run-name>
```

The builder does not rewrite, summarize, concatenate, or cache the discovery
prompts. Each JSONL request contains the exact saved prompt, `gpt-5.6-luna`, and
`max` reasoning. It forces one `write_discovery_json` function call because a
Batch response cannot write into the local repository itself. Request files are
automatically split below the API's 200 MB per-file limit. The manifest stores
only identities, paths, and hashes; it never duplicates evidence packets.
File sharding does not bypass the model's account-tier Batch queue-token limit.
If the selected discovery prompts exceed that limit, build smaller uniquely
named ayah groups and submit the next group only after the preceding group has
left the queue. Never split one lane prompt or alter its contents.

Submit the generated manifest. This is the only paid Batch stage:

```bash
python3 _commentary/v8_batch/batch_discovery.py submit \
  --manifest _commentary/v8_batch/batches/<run-name>.manifest.json
```

Check asynchronously when desired:

```bash
python3 _commentary/v8_batch/batch_discovery.py status \
  --submission _commentary/v8_batch/batches/<run-name>.submission.json
```

There is no automatic rerun or retry. A failed, expired, incomplete, malformed,
or identity-mismatched Batch response stops collection without writing any
discovery file. Once every shard is complete, collect the whole set:

```bash
python3 _commentary/v8_batch/batch_discovery.py collect \
  --manifest _commentary/v8_batch/batches/<run-name>.manifest.json \
  --submission _commentary/v8_batch/batches/<run-name>.submission.json
```

Collection validates all results before atomically materializing any discovery
JSON. It then fills the unchanged `prompts/composition.md` template and creates
one path-only `*.composition-from-batch.prompt.md` handoff per lane. The printed
handoff list is the complete regular-composition launch plan.

Batch cannot preserve the original live scope session. The unchanged discovery
prompt already requires its JSON to be self-contained so a replacement agent
can continue. V8 uses that explicit fallback, without pretending the session
survived: launch one fresh `gpt-5.6-luna` agent at `max` reasoning for each
printed handoff. Send only its printed `launch_message`. The generated handoff
requires the agent to read, in order, the exact discovery prompt as prior-turn
evidence context, the frozen discovery JSON as the finding boundary, and the
unchanged filled composition prompt. It must not redo discovery or reopen
selection.

Composition has no orchestrator follow-up. Its existing ledger validator and
any validator-required repair run inside that single regular agent turn. Do not
inspect and amend the output, inject extra instructions, or retry the stage.

Write each scope prose and non-prose landing-ledger pair under:

```text
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/
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
the composition agent to run `validate_scope_ledger.py` against its discovery,
prose, and ledger. Do not edit the composition agents' files yourself. Once a
composition agent has written both requested files and reports that the ledger
validator returned `ok`, the orchestrator records one final lifecycle status
without sending another message to the agent. Record `started` with the same
command immediately before launching the path-only handoff:

```bash
python3 _commentary/v8_batch/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role scope \
  --lane <micro|macro|global> \
  --agent-id <spawn-task-name> \
  --status <started|completed|failed|interrupted|attention>
```

Use `completed` only after the requested scope prose and ledger files exist and
the ledger validator reports `ok`. Use `failed` when required output could not
be produced, `interrupted` when the lifecycle was interrupted, and `attention`
when operator attention is needed. Treat that final event as the composition
agent's lifecycle close. Continue with the files the composition agents produced.

## 4. Consolidation

After all three scope prose files exist, close the composition agents. Start one
fresh `gpt-5.6-sol` agent at `max` reasoning effort as the consolidator. This
model and reasoning setting are mandatory for the consolidation and editorial
agent unless the operator explicitly supplies a run-scoped model override: do
not substitute another model, do not lower reasoning effort, and do not reuse a
composition-agent session. Use `_commentary/v8_batch/prompts/canonical.md` as the
consolidation instruction template. Do not pass the monitor passcode or
Firebase details to the consolidator. Use the spawn task name as `--agent-id`;
do not pass `--attempt`.

Fill that template manually before launching the agent:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@PROSE_OUTPUT_PATH@@` with the exact output path below;
- replace `@@FOCUS_CONTEXT_BRIEF@@` with the `focus_context_brief` object
  printed by `prepare`;
- replace `@@PRINCIPLES_MD@@`, `@@COMMENTARY_SPEC_MD@@`, `@@CHANNELS_MD@@`, and
  `@@CANONICAL_PROMPT_V2@@` with the complete contents of
  `_commentary/v8_batch/guidance/PRINCIPLES.md`,
  `_commentary/v8_batch/guidance/COMMENTARY_SPEC.md`,
  `_commentary/v8_batch/guidance/CHANNELS.md`, and
  `_commentary/v8_batch/guidance/PROMPT_V2.md`, respectively;
- replace `@@MICRO_SCOPE_PROSE@@`, `@@MACRO_SCOPE_PROSE@@`, and
  `@@GLOBAL_SCOPE_PROSE@@` with the complete contents of the three scope prose
  files.
- replace `@@MICRO_SCOPE_LEDGER@@`, `@@MACRO_SCOPE_LEDGER@@`, and
  `@@GLOBAL_SCOPE_LEDGER@@` with the complete contents of the three validated
  scope landing-ledger files.

Write the filled consolidation handoff under the same repo input directory as
the scope prompts:

```text
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/canonical.prompt.md
```

Do not place filled handoff prompts under `/tmp`, `/private/tmp`, a home
directory scratch path, or any location outside the repository. Every agent
handoff path used in orchestration must be a repository path.

The consolidation package contains the three scope prose texts, their validated
landing ledgers, full pinned guidance, and the focus/context brief. Discovery
JSON stays with the composition agents and is not appended to this package. Scope
prose and ledgers form the consolidator's complete evidence boundary. They
control intended coverage; a demonstrable inconsistency may be corrected from
those supplied inputs without adding evidence or silently dropping a finding.
The governing documents' historical multi-file output instructions are
subordinate to the V5 prose-only handoff.

The consolidator writes:

```text
_commentary/v8_batch/raw/<analysis-id>/sNNN/S_A/S_A.prose.tr.md
```

Before consolidation, the consolidator runs:

```bash
python3 _commentary/v8_batch/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role canonical \
  --agent-id <spawn-task-name> \
  --status started
```

Launch message:

```text
You are the V5 consolidator for <S:A>. You are running as a fresh gpt-5.6-sol
max agent.

Before consolidation, run this lifecycle command:
python3 _commentary/v8_batch/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role canonical --agent-id <spawn-task-name> --status started

Read and follow this filled consolidation prompt exactly:
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/canonical.prompt.md

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

Keep the same `gpt-5.6-sol` max consolidator live for editorial. The editorial
agent is not a new role or model; it is the same mandatory `gpt-5.6-sol` max
session that wrote the consolidated first-pass prose. Send one follow-up asking
for the editorial version. The editorial pass may rewrite sentences for
cadence, clarity, Turkish fluency, removal of English leakage, and better
reader-facing explanation. It must not add new evidence or erase a substantive
finding.

Use `_commentary/v8_batch/prompts/editorial.md` as the editorial follow-up template.
Fill it manually:

- replace `@@AYAH_REF@@` with the focus ref;
- replace `@@PROSE_INPUT_PATH@@` with the exact first-pass prose path;
- replace `@@PROSE_OUTPUT_PATH@@` with the exact editorial prose path below;
- replace `@@EDITORIAL_INSTRUCTIONS@@` with any unit-specific editorial request,
  or `No additional unit-specific instructions.`.

Write the filled editorial handoff under:

```text
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/editorial.prompt.md
```

Do not place this filled handoff under `/tmp`, `/private/tmp`, a home directory
scratch path, or any location outside the repository.

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
_commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

Follow-up message:

```text
Continue as the same V5 consolidator for <S:A>.

Read and follow this filled editorial prompt exactly:
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/editorial.prompt.md

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
python3 _commentary/v8_batch/validate_prose.py @@PROSE_OUTPUT_PATH@@
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

Keep the same `gpt-5.6-sol` max consolidator live after the editorial validator
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
_commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

It is not a new evidence-selection stage and must not inspect upstream evidence,
add findings, drop findings, strengthen claims, or create any extra artifacts.
The validation and terminal lifecycle instructions must have been supplied in
the earlier editorial follow-up message so this final CE writing follow-up can
remain exactly the quoted text. After writing the revised editorial prose, the
same consolidator must run:

```text
python3 _commentary/v8_batch/validate_prose.py _commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/S_A.prose.editorial.tr.md
```

If validation returns nonzero, the same consolidator repairs only the reported
mechanical file-contract issues in the editorial prose file, reruns the
validator, and may do this at most two times. After the validator passes, or
after two repair/rerun cycles with remaining findings reported, the same
consolidator runs exactly one terminal lifecycle command:

```bash
python3 _commentary/v8_batch/operations/monitor.py event \
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

## 7. Post-Editorial Middle-Layer Consolidation

After the CE consolidator completes the qualification/image presentation
follow-up and final editorial validation, close it and create the required
middle-layer derivative. This stage makes the complete editorial commentary
materially easier to read while preserving every distinct finding. It does not
replace or modify the editorial source and is not a new evidence-selection
stage. The only durable output of a new run is the cited middle prose; source
inventories and audits are private working procedures, not files.

Render the hermetic prompt from the final editorial prose:

```bash
python3 _commentary/v8_batch/workflow.py prepare-middle \
  --ayah <S:A> \
  --analysis-id <analysis-id>
```

The command atomically writes:

```text
_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/middle-layer.prompt.md
```

The agent may write only this target:

```text
_commentary/v8_batch/middle/<analysis-id>/sNNN/S_A/S_A.prose.middle.tr.md
```

Start one fresh `gpt-5.6-luna` agent at `max` reasoning effort with no inherited
conversation history. Its first message must be exactly the short
`handoff.launch_message` emitted by `prepare-middle`. That message tells
the agent to read and execute `middle-layer.prompt.md` at its workspace path.
Never open, copy, paste, quote, embed, summarize, or otherwise inject the prompt
contents into the orchestrator conversation or the agent message. Do not
prepend an explanation, append instructions, supply upstream material, reuse
the CE session, or provide ayah-specific advice. The agent performs its own
transient inventory and semantic audit, writes only the prose, and runs
`validate_prose.py` plus `validate_middle_prose.py` within that single turn.

When the first turn completes, do not open, read, search, summarize, diff,
count, validate, or otherwise inspect the prose. Do not use the author's report
to compose a correction. Send exactly the short
`handoff.follow_up_message` emitted by `prepare-middle`, with no prefix or
suffix, to the same agent. That path message directs it to the fixed canonical
`middle-layer-audit-followup.md`. Never inline or customize that file.

The same agent re-reads the complete filled prompt, editorial source, and
current prose; rebuilds its transient atomic inventory and synthesis clusters;
computes the structural warning metrics; performs the mandatory adversarial
synthesis challenge when triggered; repairs only the prose; and runs both
validators again. This fixed second turn is part of the normal workflow, not a
retry and not an output-derived intervention.

After the second turn, close the agent. There is no third message, bespoke
repair turn, reviewer, ledger, span map, orchestrator-run validator, or
orchestrator semantic gate. The orchestrator may record only whether the agent
reports both validators as `ok` and whether both turns completed; it does not
independently verify those claims or inspect prose, citations, metrics, or
diffs. If the agent reports an unresolved failure, report the stage as needing
attention and stop. There is no retry, rerun, relaunch, resend, replacement
agent, or failure-specific repair path. A launch failure likewise ends the
stage.

Historical `*.middle.claims.json` files and `validate_middle_layer.py` remain
available for completed V2 outputs only. The new agent does not read, edit, or
recreate them.

This stage has no separate monitor lifecycle role. Existing canonical and
invitation events remain operational status only and do not certify
middle-layer semantic quality. Invitation generation continues to use the
final editorial prose as its sole semantic source; changing that source is a
separate workflow decision.

## 8. Reading Invitation

After CE has written, revised, and validated the final editorial prose and the
required two-turn middle-layer stage has closed, generate the separate reading
invitation as the final required stage for that ayah. The invitation still uses
the final editorial prose, not the middle-layer derivative. It follows one or
two main channels of resonance in two to four Turkish paragraphs. A channel is
a connected background of meanings, images, actions, or relations that the
editorial develops through several details.
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
python3 _commentary/v8_batch/workflow.py prepare-invitation \
  --ayah <S:A> \
  --analysis-id <analysis-id>
```

The command writes
`_commentary/v8_batch/input/<analysis-id>/sNNN/S_A/invitation.prompt.md` and returns a
fresh-agent handoff whose output is
`_commentary/v8_batch/editorial/<analysis-id>/sNNN/S_A/S_A.invitation.tr.md`.

Start one fresh `gpt-5.6-luna` max agent with no inherited conversation history.
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
gpt-5.6-luna max agent.

Before writing, run this lifecycle command:
python3 _commentary/v8_batch/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role invitation --agent-id <spawn-task-name> --status started

Read and follow this invitation prompt exactly:
<complete contents of the generated invitation.prompt.md>

After validation, run exactly one terminal lifecycle command:
python3 _commentary/v8_batch/operations/monitor.py event --run-id <shared-run-id> --orchestrator-id <unique-orchestrator-id> --ayah-ref <S:A> --role invitation --agent-id <spawn-task-name> --status <completed|failed|interrupted|attention>

Report the final validator result and lifecycle status in this conversation.
```

Inspect and report the invitation separately from the completed commentary.
Check that the reader can follow the selected channel from its opening
expression through its connected background to an expanded or shifted reading
of the ayah. Check fidelity of the connections and qualifications, not coverage
of omitted findings or channels. Mechanical validation does not establish this
semantic quality. Regenerate it whenever its editorial source changes.
The monitor considers a newly registered ayah operationally complete only after
both CE validation and invitation validation have completed. Because the
monitor has no middle-layer role, the orchestrator must also have completed the
fixed same-agent two-turn middle-layer protocol before treating the runbook sequence as
complete; it does so without inspecting the outputs.

## Completed Surah Continuation

Once every numbered ayah in one analysis has completed its final editorial
follow-ups and fixed middle-layer protocol, the surah reading can run under
`_surah_commentary/v2/ORCHESTRATION.md`. It consumes only those final editorial
texts. Discovery, scope prose/ledgers, invitations, separate translations, and
middle-layer prose, and network evidence are not surah inputs.
Invitations may finish independently. The responsible orchestrator must confirm
editorial completion, completion of the no-inspection middle-layer protocol,
and the full numbered ayah count before creating the immutable surah snapshot.
This optional continuation does not change any ayah discovery or
editorial-generation step.

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
python3 _commentary/v8_batch/workflow.py prepare --ayah 29:0
```

The derived `s029-basmala-full` analysis puts all numbered S29 ayat in ordinary
lean macro context so they can activate basmala-focused resonances.

## Batch Rules

Use ranges or explicit sets during preparation, build all exact discovery
prompts into the script-managed Batch shards, and submit every shard. Do not
launch discovery with the multiagent spawn tool.

The nonblocking Operations Monitor pause check applies before the first
discovery submission for each ayah in the batch. Do not omit it for single-ayah
or batch runs. A `paused` result means exclude that ayah's three prompts before
building the request shards; it does not cancel an already submitted API batch.

When multiple ayat are selected, Batch discovery together. After successful
all-or-nothing collection, launch every returned regular-composition handoff
concurrently with the multiagent spawn tool. Each handoff carries its own
`ayah_ref`, lane, and prompt path; do not infer them from list order. As each
ayah's three scope prose files are ready, start its normal fresh consolidator
and carry the unchanged workflow forward. Each ayah remains independent after
discovery collection, with its own composition agents, consolidator, fresh
middle-layer agent, invitation agent, paths, and Git-visible outputs.

Different ayat and analysis IDs have disjoint paths and may run concurrently.
Do not run two orchestrators for the same analysis ID and ayah at once.

## Monitor Shutdown

After all ayat assigned to this orchestrator are complete and no spawned V5
agents remain live, stop the monitor:

```bash
python3 _commentary/v8_batch/operations/monitor.py stop \
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
- After composition agents are launched, do not introduce orchestrator-run validation
  gates. The CE consolidator runs its editorial prose validator, and the
  post-editorial Luna agent runs the two validators embedded in its filled
  prompt during both turns.
- Do not modify agent outputs yourself.
- Treat partial work as ordinary Git-visible state.
- Inspect canonical and invitation prose under their existing rules before
  committing the unit. The middle-layer exception is strict: do not inspect its
  prose, citations, validator output, or diff. Stage only its exact prose target
  and rely on the fixed two-turn protocol and agent-reported completion status.
- Never send a middle-layer agent an ayah-specific hint, output-derived
  correction, third message, inlined prompt, inlined follow-up, or anything
  other than the two exact path-only messages returned by `prepare-middle`.
- Never retry, rerun, relaunch, or replace a failed middle-layer agent. Report
  the stage as needing attention and stop its sequence.
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
- For stages where this runbook explicitly permits a rerun, it starts a new
  lifecycle with a new `started` event and receives the next attempt number
  automatically. This rule never authorizes a middle-layer rerun. Do not close
  or overwrite the earlier attempt to make the dashboard look successful.
