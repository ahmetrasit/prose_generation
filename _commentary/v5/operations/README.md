# Commentary V5 Operations

A small local monitor plus a static Firebase dashboard for V5 commentary runs. The
monitor scans every 10 seconds; agents only append a start event and one terminal
event. Runtime state is ignored by Git.

## Orchestrator contract

Start one monitor when an orchestrator starts:

```bash
python3 _commentary/v5/operations/monitor.py start \
  --run-id commentary-v5 \
  --orchestrator-id orch-s029 \
  --agent-id CODEX_AGENT_ID \
  --analysis-id native \
  --scope 29 \
  --firebase-project YOUR_PROJECT_ID
```

Use `--scope 29:38-45`, repeat `--scope`, or use `--scope 1-114`. Use
`--local-only` instead of `--firebase-project` while testing without Firebase.

Before starting each new ayah, the orchestrator runs:

```bash
python3 _commentary/v5/operations/monitor.py wait \
  --run-id commentary-v5 --orchestrator-id orch-s029
```

Each scope or canonical agent makes exactly two event writes:

```bash
python3 _commentary/v5/operations/monitor.py event \
  --run-id commentary-v5 --orchestrator-id orch-s029 \
  --ayah-ref 29:38 --role scope --lane micro --attempt 1 \
  --agent-id AGENT_ID --status started

python3 _commentary/v5/operations/monitor.py event \
  --run-id commentary-v5 --orchestrator-id orch-s029 \
  --ayah-ref 29:38 --role scope --lane micro --attempt 1 \
  --agent-id AGENT_ID --status completed
```

Use `--role canonical` without `--lane`. Terminal states are `completed`,
`failed`, and `interrupted`; `attention` records a user decision that is needed.
Increment `--attempt` on a rerun. Event lines are tiny JSON objects and the daemon
does the filesystem and Firebase work, so prose does not pass through agent logs.

Pause is cooperative: Firebase sets `desired_state` to `paused`, the monitor
creates its local `runtime/control/.../PAUSE` marker, and `wait` blocks before the
next ayah. Work already in progress may finish.

## Firebase setup

1. Create a Firebase project with Firestore, Hosting, and Google Authentication.
2. Install the one optional monitor dependency:

   ```bash
   python3 -m pip install -r _commentary/v5/operations/requirements.txt
   ```

3. Register a Web app and place its config object in `web/firebase-config.js`.
   Firebase web config is public identification, not an Admin credential.
4. Give each machine Application Default Credentials:

   ```bash
   gcloud auth application-default login
   ```

5. From this folder, select the project and deploy:

   ```bash
   firebase use YOUR_PROJECT_ID
   firebase deploy
   ```

The included rules require sign-in to read and a verified email to request
pause/resume. For a shared Firebase project, tighten `verifiedOperator()` to an
email allowlist or organization domain before deployment. Admin SDK writes from
the monitor bypass these client rules.

## Local dashboard

Create a snapshot once, then serve the operations folder:

```bash
python3 _commentary/v5/operations/monitor.py start \
  --run-id commentary-v5 --orchestrator-id local-preview \
  --analysis-id native --scope 29:38 --local-only

python3 -m http.server 4173 --directory _commentary/v5/operations
```

Open `http://127.0.0.1:4173/web/?local=1&run=commentary-v5`. The web view polls
`runtime/snapshot.json` every 10 seconds. If no snapshot exists, it shows labeled
preview data so the layout remains testable.

The daemon is intentionally restart-neutral for now. Its registration format is
separate from process launch, so a later always-running supervisor can create the
same registration and spawn orchestrators without changing logs or dashboard data.

Automatic Git commits are deliberately outside this first version: a monitor must
not commit unrelated files from a dirty checkout. Generated prose remains in the
existing V5 output paths and can use the repository's current review/commit flow.

