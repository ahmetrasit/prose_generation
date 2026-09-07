# Handoff: V7 operations contract

## Status

The operations integration is implemented. The authoritative cold-agent
instructions are in `_commentary/v7/ORCHESTRATION.md`; this file records the
boundary that future orchestration changes must preserve. It is not an
outstanding documentation task.

## Orchestrator Boundary

An orchestrator starts one existing monitor process before preflight:

```bash
V7_MONITOR_PASSCODE='<operator-supplied-passcode>' \
python3 _commentary/v7/operations/monitor.py start \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --agent-id <orchestrator-agent-id> \
  --analysis-id <analysis-id> \
  --scope <scope-selector>
```

- Use `commentary-v7` as the shared run ID unless the operator supplies another.
- The passcode is at least 12 characters and exists only in the startup process
  environment. It is never written to files, logs, prompts, agent messages,
  commits, or final responses.
- Firebase project details are configured defaults. Ordinary orchestrators do
  not administer passcodes, provision Firebase, or deploy the dashboard.
- A second start for the same live run/orchestrator identity is refused.
- `_commentary/v7/operations/runtime/` is the sole operational-state exception
  to V7's no-ledger rule. It is not commentary evidence or an analytical gate.

Immediately before launching the first scope agents for every new ayah, use the
nonblocking local check:

```bash
python3 _commentary/v7/operations/monitor.py check \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

`paused` defers that not-yet-started ayah. It does not interrupt active ayat or
hold a terminal open. The daemon mirrors Firebase control state to the local
marker; agents never poll Firebase directly.

## Agent Lifecycle

Every scope agent writes one `started` event before analysis and one terminal
event only after its second-turn prose work:

```bash
python3 _commentary/v7/operations/monitor.py event \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id> \
  --ayah-ref <S:A> \
  --role scope \
  --lane <micro|macro|global> \
  --agent-id <spawn-task-name> \
  --status <started|completed|failed|interrupted|attention>
```

The consolidator uses the same two-event lifecycle with `--role canonical` and
no lane. Its terminal event comes only after consolidated prose, editorial
prose, and the validator/repair cycle. `canonical completed` attests that the
editorial validator passed.

- Do not pass the passcode or Firebase details to spawned agents.
- Do not pass `--attempt`; every new `started` event allocates the next attempt.
- A failed spawn is recorded by the orchestrator as a new `attention` attempt.
- If an agent disappears, leave its start-only attempt open so the dashboard can
  show it as potentially stalled.
- Events contain only short operational descriptions, never prose, evidence,
  prompts, or reasoning.
- Never infer completion from an artifact or response alone.

## Shutdown

After all assigned ayat and spawned agents are finished:

```bash
python3 _commentary/v7/operations/monitor.py stop \
  --run-id <shared-run-id> \
  --orchestrator-id <unique-orchestrator-id>
```

The daemon performs at most two final sync attempts. A `stopped` response means
it has exited. A successful `stop_requested` response means that bounded final
sync continues in the detached process; the command does not fail or block the
orchestrator indefinitely.

## Deliberate Omissions

The monitor does not spawn agents, manage a queue, auto-commit Git changes,
recover work after machine restart, or run as a permanent supervisor. Its
registration format remains compatible with a future always-running launcher,
but that launcher is not implemented.
