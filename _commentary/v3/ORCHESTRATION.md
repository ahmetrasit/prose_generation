# Commentary v3 cold-agent orchestration

This is the canonical entrypoint for a cold agent asked to orchestrate the v3
commentary workflow for an ayah set or a complete surah. Read this file fully
before doing anything. It is an orchestration contract, not a prose prompt.

The workflow is a linguistic-analysis and prose-generation workflow that uses
software for loss prevention and reproducible handoffs. Prose and interpretive
yield are primary. Validation protects identity, evidence conservation,
session continuity, hashes, and declared paths; it must never become a style,
length, paragraph, thesis, or prose-density gate.

## 1. Non-negotiable operating rules

1. Work from the repository root that contains `_commentary/v3/`.
2. Never place a production prompt, bundle, response, or prose artifact in
   `/tmp`, `/private`, or another ad hoc run directory. The workflow selects
   canonical Git-stageable paths beneath:
   - `_commentary/v3/inputs/authoring/sNNN/S_A/`
   - `_commentary/v3/outputs/authoring/sNNN/S_A/`
3. Never pipe, shell-expand, paste, summarize, or inline a hermetic prompt into
   an agent message. Give the worker the absolute `prompt_path` returned by the
   workflow and only a short instruction to read that file completely and
   follow it exactly.
4. Use persistent agent sessions. An ephemeral agent is forbidden. Follow the
   returned `conversation_action` exactly:
   - `start` means a genuinely fresh session;
   - `resume` means the exact returned `session_id`, never a replacement agent.
5. Record a new session as soon as the executor returns its session ID, using
   the exact `session_record_command` returned by the workflow. Do this before
   accepting the worker's response as a workflow artifact.
6. Do not intervene while a prose or analysis agent is working. Wait patiently.
   Do not use process inspection as a substitute for waiting. A transient
   capacity failure does not authorize model substitution: retry or resume the
   same session, profile, and prompt path.
7. Never hand-edit, overwrite, delete, rename, or relocate a generated response
   to make validation pass. Rerun the orchestrator and use only the repair or
   follow-up handoff it returns. Generated artifacts are immutable and
   content-addressed.
8. Do not invent an unrequested global repair or combine scopes manually. If a
   repair is required, the state machine names its owner and resumes the proper
   existing session.
9. Run only the ayahs the user placed in scope. Within an ayah, the three scope
   reviews may run in parallel. Complete and verify one ayah before advancing
   to the next unless the user explicitly authorizes cross-ayah concurrency.
10. The user judges prose quality. Do not declare prose production-ready, alter
    an approved rendering, or proceed through an explicit approval gate on the
    basis of schema success alone.
11. Commit or push only when the user explicitly authorizes that external Git
    action. When authorized, do it once at the very end, after all requested
    ayahs, reviews, comparisons, and approvals are complete. This document
    itself is not authorization to commit or push.

## 2. Worker profiles and ownership

Use the executor profile required by the user or project configuration. For the
current v3 production design, linguistic scope agents, the reconciler, and the
canonical writer use **GPT-5.6 Luna, maximum reasoning effort**. Do not silently
downgrade or substitute a model when capacity is limited.

Conversation ownership is fixed:

| Conversation | First turn | Later turns |
| --- | --- | --- |
| `scope-micro` | fresh micro review | micro validation repair, reconciler-requested micro repair, and micro prose preparation/repair |
| `scope-macro` | fresh macro review | macro validation repair, reconciler-requested macro repair, and macro prose preparation/repair |
| `scope-global` | fresh global review | global validation repair, reconciler-requested global repair, and global prose preparation/repair |
| `scope-reconciler` | fresh cross-scope reconciliation | reconciliation validation repairs |
| `canonical-writer` | fresh canonical merge | the exact canonical editorial follow-up |

The micro, macro, and global first turns must be independent. They must not see
one another's responses or an existing commentary. Their later prose turns
resume the same scope sessions because those sessions retain the scope-specific
analysis that produced the accepted findings.

The reconciler owns acceptance accounting across scopes. It may identify a
specific evidentiary gap and request a repair from the owning scope, but it does
not rank readings or optimize the finding set for elegant prose.

The canonical writer is fresh. It receives the reconciled locked ledger and all
three prose-ready scope drafts, writes the four first-pass files, then receives
the canonical editorial prompt verbatim in the same session.

GPT-5.5 code-review agents are not routine linguistic workers. Use them only
when implementation, schema, validation, prompt-template, orchestration, or
operational README files change. Keep the same reviewer sessions for the
initial review and every revised patch.

## 3. Establish the exact ayah queue

Normalize every requested unit to `S:A`, for example `29:38`, and preserve
Quranic reading order.

- If the user supplies an explicit list or range, run exactly that set.
- If the user asks for a complete surah without naming a subset, derive its
  complete numbered ayah list from the configured Quran text. Include only
  `S:A` rows with `A >= 1`; an `S:0` basmala metadata row is not an authoring
  ayah and must never enter the queue. Verify that both of the following
  canonical inputs exist for every numbered ayah:
  - `_commentary/v3/inputs/adjudication/sNNN/S_A.docket.json`
  - `_commentary/v3/inputs/source/sNNN/S_A.bundle.json`
- If any requested ayah lacks either input, stop and report the complete missing
  set. Do not silently run a partial surah and do not fabricate source material.
- Respect any maturity gate set by the user. When one benchmark ayah must be
  approved before the remaining ayahs, finish the benchmark, present the
  requested comparison, and wait for approval.

The reciprocal inter-ayah projection and Quran text are loaded from the
workflow's configured canonical data paths. A complete, explicitly reported
lossless parent reconstruction may be used when the typed projection fails.
If both routes fail, the workflow must stop loudly. Never suppress an integrity
warning or replace reciprocal evidence with a thinner local substitute.

## 4. The only orchestration command

For the current ayah, run:

```bash
python3 _commentary/v3/workflow.py authoring-advance --ayah S:A
```

Do not add arbitrary run-directory arguments. Normally do not override the
docket, source bundle, reciprocal inter-ayah directory, its parent corpus, or
Quran text. An override is allowed only when the user explicitly supplied an
equivalent canonical source and its identity can be verified.

The command is idempotent. It performs every deterministic step currently
possible and returns either a verified completion, a required receipt command,
or one or more agent handoffs. After satisfying the returned action, run the
same command again. Continue until `status` and `stage` are both `complete`.

At every invocation, verify the status envelope says:

- `canonical_paths.artifacts_are_git_stageable: true`;
- `canonical_paths.temporary_paths_allowed: false`;
- `transport.prompt_delivery: "absolute_path_only"`;
- `transport.pipe_or_inline_prompt_contents: false`;
- `transport.embedded_json: "canonical-minified-utf8"`.

If any invariant is absent or false, stop. Do not compensate manually.

Also inspect `inter_ayah_evidence`. Report any integrity warning and whether the
lossless fallback was used. A warning is never permission to omit the evidence.

Inspect `canonical_workspace_policy` on every status. Every newly recorded
canonical turn must require a guard. A previously sealed completion may report
`canonical_workspace_guard_status: legacy_pre_guard_completed_lineage`; this is
an explicit historical compatibility state, not evidence that the old writer
turn was guarded. It is admissible only because both old receipts and all eight
outputs were already bound by an immutable content-addressed completion before
the guard feature existed. Preserve and report it as a historical benchmark
when the user has already approved preserving that prose. Never create, infer,
or silently upgrade such a status, and never use it to claim that the current
workflow's workspace guard has passed end to end. The first newly authored ayah
must report `canonical_workspace_guard_status: enforced` before that production
claim is made.

## 5. How to execute a returned handoff

Each item in `handoffs[]` is authoritative. Check these fields before launch:

- `role` and `conversation_key`;
- `conversation_action`;
- absolute `prompt_path`, plus its hash and byte count;
- `prompt_manifest`;
- `expected_response` or the complete `expected_outputs` map;
- `working_directory` and `workspace_access`;
- `session_persistence_required: true`;
- `ephemeral_session_forbidden: true`.

### Starting a conversation

1. Launch one fresh persistent worker with the required model and reasoning
   profile, the returned working directory, and the returned access mode.
2. Its initial message must contain no hermetic prompt content. Use only:

   ```text
   Read this file completely and follow it exactly:
   /absolute/path/from/prompt_path
   ```

3. As soon as a session ID is available, execute the returned
   `session_record_command`, replacing only `<returned-session-id>`.
4. Wait patiently for completion.

### Resuming a conversation

1. Resume exactly the returned `session_id` using the same model profile.
2. Send the same two-line path-only instruction with the newly returned
   absolute prompt path.
3. Do not create or record a new session receipt.
4. Wait patiently for completion.

### Capturing structured responses

Scope reviews, repairs, reconciliation turns, and scope-prose drafts return one
JSON object. Keep their workspace read-only and use the executor's native
final-response capture to write the response directly and atomically to
`expected_response`. Do not use a shell pipe and do not manually reserialize,
pretty-print, repair, or wrap the JSON. The response file must contain only the
worker's contracted JSON object. Empty, truncated, malformed, or non-object
capture is a loud stop unless `authoring-advance` itself returns an explicit
same-session follow-up; never improvise recovery.

The executor adapter must implement the following operations. Names vary by
host, but the semantics do not:

```text
start_persistent(
  model=LUNA_5_6, reasoning=MAX,
  cwd=handoff.working_directory,
  access=handoff.workspace_access,
  message="Read this file completely and follow it exactly:\n" +
          handoff.prompt_path,
  capture_final_response=handoff.expected_response
) -> session_id

resume_persistent(
  session_id=handoff.session_id,
  model=LUNA_5_6, reasoning=MAX,
  message="Read this file completely and follow it exactly:\n" +
          handoff.prompt_path,
  capture_final_response=handoff.expected_response
)
```

Pass arguments as an argument vector or native API fields, not through shell
interpolation. On `start`, persist `session_id` with the returned
`session_record_command` immediately. On `resume`, reject a runner result whose
session identity differs. The Codex CLI equivalent uses persistent `codex exec`
and `codex exec resume SESSION_ID`, plus native `--output-last-message` for
structured response capture; do not add `--ephemeral`, `-`, or stdin prompt
input. The installed executor/profile supplies the exact production model name
and maximum-reasoning configuration—do not guess or silently substitute them.

### Canonical writer outputs

The canonical merge and editorial workers receive the executor's real
`workspace_access: workspace_write`, the exact four `expected_outputs`, and a
content-addressed `workspace_guard` plus its returned byte hash. Retain that
path/hash pair in the orchestrator's own handoff state; never let the worker
select or replace it. They write the four output paths themselves.
The workflow snapshots Git-visible state before the handoff and verifies it at
turn receipt time. Any undeclared change is a loud failure. The guard's semantic
hash must equal its filename; there must be exactly one guard; and only that
exact file—not its containing directory—is excluded from the pre/post
comparison, so an added guard is itself a failure. Before recording the turn,
confirm the retained handoff path and `workspace_guard_bytes_sha256` still
match. On a partial-output resume, also retain `preexisting_output_states` from
that latest handoff and independently confirm those already-present files did
not change. Retain `preexisting_auxiliary_states` as well; a session or turn
receipt that was already present at guard time must remain byte-identical. Do
not describe this as a filesystem allowlist: the guard plus the
external handoff anchor is the concrete enforcement available with the
executor's workspace-wide mode.

If one or more declared files are missing and `authoring-advance` returns a
same-session canonical handoff, resume that exact writer and create only the
missing files; present outputs remain immutable. An empty, malformed, or
truncated file is not “missing” and stops loudly. It never authorizes a fresh
writer, manual completion, or overwriting an existing artifact.

If the executor cannot provide persistent start/resume semantics, native final
response capture, or the requested workspace access, stop and report that the
execution environment cannot satisfy the workflow contract.

## 6. State-machine stages

Never guess the next step. Dispatch exactly what `authoring-advance` returns.

| Returned stage/status | Required action |
| --- | --- |
| `scope_review` / `waiting_for_agents` | Start the fresh micro, macro, and global workers in parallel. Record all three sessions immediately. |
| `scope_validation_repair` / `waiting_for_agents` | Resume only the named scope sessions with their generated validation-repair prompts. Do not rewrite their JSON yourself. |
| `reconciliation` / `waiting_for_agent` | Start one fresh reconciler and record its session immediately. |
| `reconciliation_validation_repair` / `waiting_for_agent` | Resume the same reconciler with the generated accounting-repair prompt. |
| `scope_repair` / `waiting_for_agents` | Resume only the scope sessions named by the reconciler. These are genuine analysis repairs, not global editorial intervention. |
| `scope_prose` / `waiting_for_agents` | Resume the original three scope sessions with their lane-specific prose-preparation prompts. They may run in parallel. |
| `scope_prose_validation_repair` / `waiting_for_agents` | Resume the named original scope sessions. This path repairs only safe accounting defects and must preserve prose and semantic content exactly. |
| `scope_prose_rewrite` / `waiting_for_agents` | Resume the named original scope sessions for a genuine prose correction when lossless accounting repair is impossible or unsafe. Preserve every locked finding; this is not permission to become conservative. |
| `canonical_merge` / `waiting_for_agent` | Follow the returned `conversation_action`: start one fresh canonical writer only when none of the four first-pass outputs exists; if any exists, resume the exact persisted canonical-writer session. In either case use workspace write access, exactly the declared outputs, and the returned pre-turn guard, then record the session immediately when the action is `start`. |
| `canonical_merge` / `execution_receipt_required` | Run the exact returned `record_command`; do not construct a receipt manually. |
| `canonical_editorial_followup` / `waiting_for_agent` | Resume the same canonical writer. The prompt file must be the byte-exact canonical editorial follow-up. |
| `canonical_editorial_followup` / `execution_receipt_required` | Run the exact returned `record_command`, including its prior merge receipt. |
| `complete` / `complete` | Continue with the verification and prose-review gates below. |

Several validation or reconciliation turns may be required. This is expected.
Repairs must remain in their named conversations. The orchestrator does not
coach an agent during a turn or replace its generated prompt with advice.

## 7. Failure and retry rules

- A nonzero orchestration exit is a loud stop. Preserve the exact error and all
  immutable artifacts. Do not delete the offending content-addressed directory
  or edit its response in place.
- A transient executor/capacity failure before a session exists may retry the
  same start request with the same profile and prompt path. Once a session
  exists, every retry must resume it.
- A response or output without the required persisted session is untrusted.
  Stop rather than attaching it to another session.
- Never accept partial candidate, support, connection, HFT, surface-word,
  branch, facet, referral, locked-finding, or output accounting. A valid JSON
  response with a genuine scope-prose defect may receive the explicit
  `scope_prose_rewrite` turn; malformed transport still stops loudly.
- Never treat HFT provenance, legacy identity, novelty, low confidence,
  canonical absence, conflict, or difficulty of explanation as a reason to
  hide a grounded finding. Qualification controls containment and epistemic
  labeling, not visibility.
- Never loosen or add prose-style validation to get a run through. A genuine
  prose defect needs a genuine same-agent prose turn; it must not be disguised
  as a schema repair.
- If source, prompt, response, receipt, or output hashes disagree, stop loudly.
  Do not fall back to unhashed or incomplete material.

## 8. Per-ayah completion audit

After the first `complete` result, immediately run the same command once more.
It must return the same completion manifest and output hashes without producing
a new request. This is the idempotence check.

Then confirm:

1. The completion manifest is under the ayah's canonical output tree.
2. It binds every artifact in the active lineage—prompt packets, manifests,
   scope responses and active repairs, scope drafts, session receipts,
   canonical workspace guards when the run is guarded, canonical turn receipts,
   and all eight first-pass and editorial files—by byte count and SHA-256.
   A reported historical pre-guard completion has no invented guard and is not
   a production guard test. Superseded content-addressed
   generations remain immutable and Git-stageable in their canonical trees but
   are intentionally not asserted as active by the completion manifest.
3. Micro, macro, and global each have complete locked-finding landings in their
   scope drafts; the first-pass and editorial indexes name every active locked
   ref exactly once, and both evidence files account for every active locked
   ref without invented refs.
4. Reconciliation has no unresolved referral or requested repair when
   `ready_for_prose` is true.
5. The merge and editorial receipts name the same canonical-writer session, and
   the editorial receipt is bound to the exact merge receipt.
6. The generated editorial prompt is byte-for-byte identical to
   `_commentary/v3/prompts/editorial-followup.md`.
7. No production artifact is a symlink, ignored by Git, outside the canonical
   authoring trees, or dependent on `/tmp` or `/private`.
8. The final reader prose contains no candidate IDs, support IDs, branch IDs,
   scope names, workflow language, HFT/QAC labels, or internal coordinates.

These are completeness checks, not a judgment that the prose is good.

## 9. Prose review and approval

Present the editorial prose to the user at any requested approval gate. If a
canonical or previously approved output exists, compare them semantically:

- what the new prose genuinely reveals or explains more fully;
- whether any previous finding, mechanism, image, ambiguity, or reader payoff
  disappeared;
- whether a finding is merely listed in the index or actually disclosed in
  prose;
- whether editorial revision selectively overcompressed a distinctive facet;
- whether primary meaning remains clear while exploratory readings remain
  visible and naturally bounded.

Finding-ID coverage is not semantic disclosure. Do not claim that prose is
production-ready merely because every ID has a landing. The user makes the
final quality decision. If the user approves the prose, preserve it; do not
rewrite it to satisfy an internal preference.

## 10. Moving through a surah

After one ayah passes completion and any required user gate, repeat sections
4–9 for the next queued ayah. Each ayah gets independent content-addressed
trees and fresh first-turn sessions. Never reuse a scope, reconciler, or
canonical-writer session across ayahs.

Maintain a concise run ledger containing, for each ayah:

- completion manifest path;
- micro, macro, global, reconciler, and canonical-writer session IDs;
- locked counts by scope;
- first-pass and editorial prose paths and hashes;
- inter-ayah fallback/warning status;
- user approval status when an approval gate exists.

Do not create the ledger outside the repository. If it must be persisted, put
it in the canonical task documentation or requested surah output tree so it is
Git-stageable.

## 11. Implementation-change protocol

Do not change scripts, schemas, validators, or prompt templates merely because
an agent needs time or returned an inconvenient interpretation. Change them
only for a real reusable workflow or missing-data defect.

If such a change is necessary:

1. Explain the concrete defect and why agent work alone cannot fix it.
2. Make the smallest general change; do not overfit a prompt to the current
   ayah.
3. Keep validation limited to identity, completeness, provenance, lineage,
   paths, hashes, and safe repair preservation.
4. Send the exact implementation and prompt diff to persistent GPT-5.5 code
   reviewers covering orchestration, prompts, and validation.
5. Address their findings, then send the revised exact patch back to those same
   reviewer sessions. Require an explicit GO before continuing production.
6. Rerun proportional deterministic checks such as Python compilation,
   `git diff --check`, the completed-ayah idempotence command, and exact prompt
   or receipt comparisons. Tests support the review; they do not replace it.
7. Expect changed semantic inputs or prompt templates to create new
   content-addressed stage paths. Do not overwrite or delete older generations.

## 12. Final commit and push, only when explicitly authorized

Skip this section entirely unless the user explicitly authorized commit and/or
push. When that authorization exists, act only after the complete authorized
ayah queue is finished and all required user approvals and code-review GOs are
in hand:

1. Inspect the working tree and preserve unrelated user changes.
2. Confirm every new hermetic prompt, packet, response, receipt, completion
   manifest, and prose file is visible to Git and lies in its canonical tree.
3. Run `git diff --check` and the proportional final integrity checks.
4. Stage only the reviewed in-scope paths with an explicit pathspec such as
   `git add -- _commentary/v3/...`; never use a broad staging command that can
   absorb unrelated user work. Review the staged diff and artifact inventory
   before committing.
5. Create one clear final commit for the completed workflow work, unless the
   user explicitly requested a different commit structure.
6. Push the current branch once only if push itself was authorized. Report the
   branch and commit hash.

Do not commit or push at an intermediate ayah, repair, benchmark comparison, or
approval checkpoint.
