# Handoff: V5 operations integration

## Objective

Update `_commentary/v5/ORCHESTRATION.md` so every V5 orchestrator uses the
existing operations monitor. Keep the analytical workflow unchanged. This is a
documentation-only task.

## Allowed scope

Edit only:

```text
_commentary/v5/ORCHESTRATION.md
```

Do not edit `workflow.py`, analytical prompts, prose outputs, validators, the
operations implementation, or Firebase configuration. Do not deploy Firebase.

## Required changes

### 1. Register the orchestrator once

Add a short `Operations Monitor` section before `1. Preflight`. Require the
orchestrator to launch one monitor before beginning work:

```bash
python3 _commentary/v5/operations/monitor.py start \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --agent-id <orchestrator-agent-id> \
  --analysis-id <analysis-id> \
  --scope <scope-selector> \
  --firebase-project "$FIREBASE_PROJECT_ID"
```

State these rules compactly:

- All machines participating in one run use the same `run-id`.
- Every orchestrator uses a unique `orchestrator-id`.
- One registration covers one `analysis-id`; repeat `--scope` when needed.
- Valid scope selectors are `S`, `S-T`, `S:A`, and `S:A-B`.
- The orchestrator launches the existing script. It does not create or copy a
  daemon script.
- Firebase provisioning and credentials are machine setup, not orchestration
  work. Do not add installation or deployment steps to the cold-agent runbook.

### 2. Preserve the no-ledger rule with one exception

The current runbook prohibits ledgers, manifests, hidden state, and audit files.
Keep that prohibition, but add this explicit exception:

```text
_commentary/v5/operations/runtime/
```

Clarify that this directory is monitor-owned, ignored by Git, operational only,
and must never be read as commentary evidence or used as an analytical gate.
Agents must not create any other tracking files.

### 3. Check pause before each new ayah

In `Batch Rules`, require this command immediately before beginning the next
ayah's analysis or launching its first scope agents:

```bash
python3 _commentary/v5/operations/monitor.py wait \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

Pause is cooperative. An ayah already in progress may finish; no new ayah may
start until `wait` returns `running`. Do not introduce direct remote messaging
to agents.

### 4. Add the scope-agent lifecycle boundary

Amend the instruction that currently gives scope agents "only" the prompt path.
The launch message may contain only the prompt path, the instruction to follow
it, and the two exact lifecycle commands.

The scope agent runs this before analysis:

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

Immediately before its final response, the same agent runs the same command with
one terminal status: `completed`, `failed`, `interrupted`, or `attention`.
`completed` is allowed only after its requested scope prose file exists.

Use the spawn task name as `agent-id`; it is stable and known before launch. Do
not pass `--attempt`. Each new `started` event receives the next attempt number
automatically, including an unplanned rerun.

### 5. Add the consolidator lifecycle boundary

Add the corresponding commands to the consolidator launch and editorial
follow-up contract:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role canonical \
  --agent-id <spawn-task-name> \
  --status started
```

The consolidator emits its canonical terminal event only after it has written
the consolidated prose, written the editorial prose, and finished the required
validator/repair cycle. Therefore `canonical completed` means the entire
consolidator lifecycle, including validation, completed successfully. Use
`failed`, `interrupted`, or `attention` otherwise.

Do not add a separate validator agent or require per-step progress events. Keep
the agreed start/final lifecycle minimal.

### 6. Define the failure fallback

Add one short operational rule:

- If a launched agent terminates before appending its terminal event, leave its
  start event incomplete; that is how the dashboard identifies a possible
  stall.
- If spawning fails before the new agent can write `started`, the orchestrator
  writes an `attention` event for the intended ayah and role.
- Never fabricate `completed` from the presence of a response alone.
- Event messages must remain short operational descriptions. Never put prose,
  evidence, prompts, or model reasoning in event logs.

## Required consistency cleanup

Update the `Fixed Sequence`, `Scope Agents`, `Consolidation`, `Editorial
Follow-Up`, `Batch Rules`, and `Operational Rules` wording only where necessary
to make the additions above non-contradictory. Do not otherwise reorganize or
rewrite those sections.

There is one implementation-contract dependency: the monitor must interpret a
successful final `canonical completed` event as confirmation that the mandatory
validator cycle also finished. Preserve the two-event consolidator lifecycle;
do not work around this dependency by adding separate validator events to the
runbook.

## Acceptance checks

- Exactly one monitor is started per orchestrator registration.
- Pause is checked once before each newly started ayah, not between steps of an
  active ayah.
- Each scope agent has one start and one terminal event.
- Each consolidator has one start and one terminal event covering consolidation,
  editorial work, and validation.
- Reruns require no manual attempt bookkeeping.
- The existing evidence, model, prompt, file-path, validator, and concurrency
  rules remain unchanged.
- No Git automation, supervisor, queue, restart recovery, or agent-spawning
  daemon is introduced.
