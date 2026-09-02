# Commentary v4 orchestration

This is the complete runbook for a cold orchestrator. Do not invoke v3's
authoring state machine.

## One unit

1. Run:

   ```bash
   python3 _commentary/v4/workflow.py advance --ayah S:A
   ```

2. At `stage: scope_review`, start the returned micro, macro, and global
   handoffs as three fresh independent agents in parallel. Give each agent its
   absolute prompt path and expected response path. The agent writes its exact
   returned JSON object to that path. Do not edit, normalize, or repair it.

3. Run `advance` again. It performs only JSON parsing and identity checks, then
   returns `stage: canonical_write`. It does not score semantic completeness or
   request repairs.

4. Start one fresh canonical writer with the returned canonical prompt and four
   raw output paths. Keep that live agent available. After it writes all four
   first-pass files, run `advance` again. This hashes those exact inputs and
   returns `stage: canonical_editorial`.

5. Send the returned editorial prompt and four declared editorial output paths
   to that same live writer. The handoff embeds the exact v3 editorial
   instructions and adds only the bound input hashes and destination map.

6. Run:

   ```bash
   python3 _commentary/v4/workflow.py verify --ayah S:A
   ```

7. Inspect `git diff` and commit the unit's `input/`, `raw/`, and `editorial/`
   artifacts together when accepted.

## Rules

- Do not create or record session IDs. The workflow issues no agent-close
  operation and stores no lifecycle state.
- Do not run a post-scope repair checker. The canonical writer owns semantic
  reconciliation and can inspect every immutable lane packet.
- Each scope analyst receives one substantive turn. `coverage_complete: false`
  and other semantic limitations go forward to the canonical writer; they never
  create a scope repair turn.
- Do not modify analyst ledgers. Missing files receive their initial fixed
  handoff. Invalid, malformed, stale, or wrong-unit JSON stops that unit with an
  error; v4 does not turn it into an automated replacement or repair cycle. An
  operator may explicitly remove or replace the failed artifact and rerun the
  unit. A symlink or escaped output target is likewise a path-safety error that
  must be resolved explicitly.
- Never drive `advance` in an automatic retry loop. A unit error is terminal for
  that orchestration wave; report it while unrelated batch units continue.
- Do not use an existing commentary as evidence or as a gap checklist.
- If the live canonical conversation is lost before editorial completion,
  restart from `canonical.prompt.md`, regenerate all four first-pass files, run
  `advance` to rebind them, and apply the newly generated
  `editorial.prompt.md`. There is no session-recovery layer.
- A partial or failed run is ordinary Git-visible working state. Preserve it by
  commit or branch when it matters; v4 does not manufacture a second history.

## Parallel ayahs

Request a whole same-surah range or any explicit set in one command:

```bash
python3 _commentary/v4/workflow.py advance --ayah 100:1-11
python3 _commentary/v4/workflow.py advance --ayah 1:1-7 2:1-5
```

The command prepares units deterministically and returns a flat
`parallel_handoffs` array. Launch all returned handoffs concurrently. Each item
contains its `ayah_ref` and `stage`; never infer either from list order.

Do not call `advance` for an ayah while one of its workers is still writing.
Either wait for every handoff in the current batch wave and then rerun the full
batch, or rerun only the explicit ayah refs whose workers have returned. Output
presence is a file boundary, not an agent-liveness signal; v4 intentionally has
no persisted session registry from which to infer liveness.

For a canonical wave, retain an in-memory map from `ayah_ref` to that live
canonical writer. After the selected writer or full wave finishes first-pass
work, run `advance` for those completed refs, then send each
`canonical_editorial` handoff to the matching live writer. This map is temporary
executor state, not a persisted workflow session. If a writer is no longer
available, use that handoff's `restart_if_agent_unavailable` path and regenerate
the unit's complete first-pass set.

Different ayahs have disjoint fixed paths, so their scope, canonical, and
editorial work may run concurrently without a repository-wide guard. Do not run
two orchestrators for the same ayah at the same time. A batch can contain mixed
stages and unit errors; continue every returned handoff and address only the
reported failed units. `partial_error` deliberately exits nonzero so automation
cannot miss the failed unit, but its JSON and `parallel_handoffs` remain valid.

Prefatory basmala units remain unsupported until their versioned authoring
protocol lands.
