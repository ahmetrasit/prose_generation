# Commentary V5 Operations

A small local monitor plus a static Firebase dashboard for V5 commentary runs. The
monitor scans every 10 seconds; agents only append a start event and one terminal
event. Runtime state is ignored by Git.

The deployed dashboard version is `web/firebase-config.js` `appVersion`. Increment
it before every Hosting deployment.

## Orchestrator contract

Start one monitor when an orchestrator starts. For cloud operation, set the
passcode copied from the dashboard before starting the monitor:

```bash
export V5_MONITOR_PASSCODE='the-passcode-from-the-dashboard'

python3 _commentary/v5/operations/monitor.py start \
  --run-id commentary-v5 \
  --orchestrator-id orch-s029 \
  --agent-id CODEX_AGENT_ID \
  --analysis-id native \
  --scope 29
```

Use `--scope 29:38-45`, repeat `--scope`, or use `--scope 1-114`. Use
`--local-only` while testing without Firebase. For cloud operation, `start`
verifies the passcode-backed Firebase registration before it launches the
background monitor.

The Firebase project and public Web API key already default to `v5-monitor`.
They can be overridden with `--firebase-project` and `--firebase-api-key`.

Before starting each new ayah, the orchestrator runs:

```bash
python3 _commentary/v5/operations/monitor.py wait \
  --run-id commentary-v5 --orchestrator-id orch-s029
```

Each scope or canonical agent makes exactly two event writes:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id commentary-v5 --orchestrator-id orch-s029 \
  --ayah-ref 29:38 --role scope --lane micro \
  --agent-id AGENT_ID --status started

python3 _commentary/v5/operations/monitor.py event \
  --run-id commentary-v5 --orchestrator-id orch-s029 \
  --ayah-ref 29:38 --role scope --lane micro \
  --agent-id AGENT_ID --status completed
```

Use `--role canonical` without `--lane`. Terminal states are `completed`,
`failed`, `interrupted`, and `attention`; `attention` records operator attention
needed for an otherwise finished attempt. New starts allocate attempt numbers
automatically, so an unplanned rerun remains visible. `--attempt` is only an
override. Event lines are tiny JSON objects and the daemon does the filesystem
and Firebase work, so prose does not pass through agent logs.

Stop the monitor when the orchestrator has no live spawned agents and all
assigned ayat are complete:

```bash
python3 _commentary/v5/operations/monitor.py stop \
  --run-id commentary-v5 --orchestrator-id orch-s029
```

Shutdown is cooperative. `stop` writes a local `STOP` marker; the daemon scans
once more, retries any pending Firebase prose uploads, marks itself offline, and
then exits. A second `start` for the same run and orchestrator is refused while
the existing monitor process is live.

Pause is cooperative: Firebase sets `desired_state` to `paused`, the monitor
creates its local `runtime/control/.../PAUSE` marker, and `wait` blocks before the
next ayah. Work already in progress may finish. Remote control changes normally
reach the local marker within the monitor's 10-second polling interval.

## Firebase setup

The deployed dashboard is `https://v5-monitor.web.app`. Sign in with the
configured operator account, open `Passcodes`, and either enter or generate a
passcode. Copy it to each machine as `V5_MONITOR_PASSCODE`. The dashboard stores
only its SHA-256 fingerprint and can revoke or re-enable it later.

The monitor uses Python's standard library to call the Firestore REST API. It
does not use Firebase Admin, a service account, Application Default Credentials,
or an extra Python package. The Firebase Web API key identifies the project and
is not an administrator credential. Firestore rules accept daemon writes only
when their passcode fingerprint is currently allowed.

Google Authentication must have the Google provider enabled for dashboard
administration. To deploy from this folder:

```bash
firebase use v5-monitor
firebase deploy
```

The rules allow only `ozturk.ahmetr@gmail.com` to read monitor data, administer
passcodes, or request pause/resume. The passcode scheme is intentionally a basic
bearer credential; use a different passcode per machine or account when useful.

## Local dashboard

Create a snapshot once, then serve the operations folder:

```bash
python3 _commentary/v5/operations/monitor.py start \
  --run-id commentary-v5 --orchestrator-id local-preview \
  --analysis-id native --scope 29:38 --local-only

python3 -m http.server 4173 --bind 127.0.0.1
```

Open
`http://127.0.0.1:4173/_commentary/v5/operations/web/?local=1&run=commentary-v5`.
The web view polls `runtime/snapshot.json` every 10 seconds and fetches only the
selected prose file. If no snapshot exists, it shows a labeled 180-ayah preview
so sorting, filtering, pagination, stalled work, reruns, and the markup reader can
be tested at bulk-session scale.

The daemon is intentionally restart-neutral for now. Its registration format is
separate from process launch, so a later always-running supervisor can create the
same registration and spawn orchestrators without changing logs or dashboard data.

Automatic Git commits are deliberately outside this first version: a monitor must
not commit unrelated files from a dirty checkout. Generated prose remains in the
existing V5 output paths and can use the repository's current review/commit flow.
