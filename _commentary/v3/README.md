# Commentary v3

This directory is a standalone ayah-commentary workflow. It ingests an existing
hermetic ayah bundle, retains its exact bytes under `inputs/source/`, and does
not import or execute legacy commentary scripts. Every retained input,
intermediate artifact, response, and final output remains under this directory.

A cold agent asked to orchestrate this workflow for an ayah set or surah must
be given the absolute path to `ORCHESTRATION.md` and follow that document as its
single orchestration entrypoint. This README explains the implementation and
artifact contracts; it is not the cold-agent runbook.

## Evidence lanes

- **micro**: source-bound QAC morphology, word-analysis topics, and a complete record of
  every branch for every root mapped to the focus ayah;
- **macro**: pericope-anchored channel nominations and HFT only when its window
  exactly equals the declared pericope and each reader echoes the packet
  identity;
- **global**: reader walks and cross-run findings, each carrying an explicit
  trust label.

In the legacy structured path below, the lanes are evidence scopes inside one
adjudication call. The prose-first path now gives each lane its own fresh review
conversation before reconciliation and prose preparation.

## Prose-first authoring workflow

The prose-first path is advanced by one idempotent command:

```bash
python3 _commentary/v3/workflow.py authoring-advance \
  --ayah 29:38
```

`--ayah` deterministically selects two canonical, repository-tracked trees:

- hermetic packets, prompts, and prompt manifests under
  `inputs/authoring/sNNN/S_A/`;
- responses, drafts, session/turn receipts, and prose outputs under
  `outputs/authoring/sNNN/S_A/`.

Each scope and downstream stage has a content-addressed request directory. A
semantic source/evidence, governing-document, or prompt change therefore creates
a new stage path instead of overwriting or silently reusing an older artifact. The
production command accepts no arbitrary run directory, and it never emits a
bundle under `/tmp` or `/private`. Every generated artifact is visible to Git
and can be staged and committed.

The command stops whenever an agent handoff is required and returns the
absolute prompt path, prompt hash, expected response or output paths, workspace
access, stable conversation key, and a separate `start`/`resume` action. Prompt
contents are never piped or copied into the initial agent message. The operator
gives the agent the absolute prompt path, and, when using the approved native
multi-agent adapter, the returned expected response/output path that the worker
must write itself. On a new conversation, record the returned persistent
session ID with the returned `authoring-record-session` command before
accepting its output. Scope prose and repair follow-ups resume their
corresponding scope sessions, while the verbatim canonical editorial follow-up
resumes the canonical merge writer. A final invitation summary starts a fresh
read-only conversation that receives only the editorial prose and findings
index. Ephemeral sessions are forbidden.

Structured responses prefer read-only workers and the executor's native atomic
final-response capture. The approved native multi-agent adapter is an explicit
transport exception: persistent spawned workers write their own
`expected_response` files in the contracted JSON or Markdown format, and the
orchestrator only spawns, monitors, records sessions, reruns the state machine,
and closes agents when the ayah no longer needs them. The orchestrator must not
copy, repair, reserialize, pretty-print, wrap, or otherwise edit a worker
response. Canonical writers use the exact declared outputs plus a
content-addressed pre-turn workspace guard.
Turn notarization rejects Git-visible changes outside those paths. Each handoff
also returns hashes for outputs already present before a resumed turn so the
external orchestrator can require them to remain unchanged.

New canonical turn recording always requires this guard. A guardless receipt
can be loaded only when it was already sealed, together with both phase
receipts and all eight unchanged outputs, by a valid content-addressed v2
completion created before guard enforcement existed. Status reports that case
as `legacy_pre_guard_completed_lineage` and sets
`production_workspace_guard_enforced: false`; it is an explicit historical
benchmark compatibility state, never an inferred guard or an end-to-end
production-guard pass. A successor completion binds every admitting v2
completion into its own hashed lineage. The first new authoring run must report
`enforced` before the guarded workflow is called production-ready.

The stage order is:

1. three fresh micro, macro, and global reviews in parallel;
2. deterministic conservation checks, with content-addressed same-scope repair
   follow-ups when a review has a loss/accounting gap;
3. one cross-scope reconciliation, with same-reconciler accounting repair turns
   and repeated same-scope repairs when a concrete evidentiary gap is found;
4. three prose-preparation follow-ups in the original scope conversations,
   followed only when needed by bounded same-agent accounting repairs that
   preserve prose, movement order, and friction exactly, or by a genuine
   same-agent prose rewrite when lossless relabeling is impossible;
5. one fresh canonical merge writer producing the four first-pass files;
6. the canonical editorial follow-up, verbatim, in that same writer
   conversation, producing four editorial counterparts;
7. explicit merge and editorial turn receipts binding the persistent writer
   session, request, prompt, ordered phase, and exact output hashes;
8. one fresh invitation writer receiving only editorial prose and index and
   producing a short reader-facing invitation with no finding-coverage duty;
9. a deterministic completion manifest binding every artifact in the active
   lineage and every final file by path, byte count, and SHA-256. Superseded
   content-addressed generations remain immutable and stageable but are not
   asserted as active lineage.

Embedded JSON and agent-facing v3 input payloads are canonical and minified
(`ensure_ascii=false`, sorted keys, no indentation or separator whitespace).
Agent-facing authoring packets also omit recoverable source/projection
provenance coordinates such as JSON pointers, source files, source lines, row
hashes, and projection pointers; those coordinates remain recoverable from the
committed source snapshots and data repositories, while semantic fields and
exact evidence payloads remain present.
Downstream reconciliation also stores cross-lane branch semantics once while
retaining every lane-specific link. This is transport deduplication only:
evidence and findings are never summarized, sampled, truncated, or semantically
compressed for token savings. Non-payload manifests and reports may remain
pretty-printed for inspection.

The v2 scope-review contract normalizes every reviewable branch meaning under
`review_facets` with a stable `facet_id`. Tested-facet rows and accepted branch
contributions cite that same identity, so a generic branch citation cannot
stand in for the facet actually claimed. Macro and global packets likewise give
every authored and reciprocal connection source row a stable
`connection_evidence_ref`; each direction receives an independent nested result
before the parent connection result is derived. `contact_opportunities` contains
only complete semantic contacts. Failed attempted edges remain visible in their
candidate, branch/facet, support, or connection coverage ledgers without being
assigned synthetic contact identities.

Each scope-prose context contains only records cited by its locked findings or
resolved referrals. A referral also pulls in origin-only candidate, raw support
(including HFT payload and qualification), branch/facet, connection, contact,
and decision records even when those refs cannot appear in the receiving
finding's top-level evidence union. Repeated branch semantics are carried once;
lane availability and only the selected candidate/support/HFT links remain.
Missing cited or origin records stop the workflow rather than yielding thinner
prose.

Scope prose accounting uses the reconciler's exact `locked_finding_ref` values;
member finding refs remain provenance and are never converted by a presumed
prefix rule. A repair follow-up carries only the prior minified draft, the
validation issue, and a compact explicit locked-to-member map. It does not
repeat the much larger original hermetic prose prompt because it resumes the
original scope session. Runtime checks reject any repair that changes prose,
movement keys or order, friction, or other non-accounting content. A missing or
empty response capture, or malformed JSON, stops loudly. A valid scope draft
with empty prose or movements, stale identity, or another genuine
prose/structure defect is routed to a bounded follow-up in the same scope
session instead of being disguised as an accounting repair. That follow-up
remains high-recall and may rewrite prose only as needed while preserving every
assigned locked finding. Ref repair is
allowed only when every assigned locked finding already has one unambiguous
prior locked/member-ref occurrence. The workflow derives the exact normalized
movement and landing map in code; a missing, unknown, or multiply attached
finding cannot be made to look covered by relabeling unrelated prose.

The workflow checks identity, lineage, exact candidate/connection/support and
surface accounting, accepted-to-locked finding conservation, reconciliation-
repair semantic preservation, path confinement, symlinks, persistent-session
continuity, canonical-writer Git-visible workspace guards, ordered turn
receipts, exact locked-ref coverage in both canonical indexes and evidence
files, explicit-apparatus exclusion in the invitation, and exact output hashes.
The invitation is a reader derivative, not a new semantic authority: it neither
adds a locked-finding coverage requirement nor changes editorial artifacts.
These are loss-prevention checks, not prose gates. The workflow deliberately
does not impose prose length, paragraph, finding-density, thesis, or stylistic
schema requirements. Missing, stale, malformed, escaped, partial, or
hash-inconsistent artifacts stop the workflow loudly; no fallback may silently
omit a scope or an accepted finding.

## Legacy structured workflow

`advance` is the normal entry point. It runs every deterministic stage that is
currently possible and returns JSON describing either the next model handoff or
a verified completion:

```bash
python3 _commentary/v3/workflow.py advance \
  --bundle bundles/s029/29_38.ayah.json \
  --hft-policy quarantine
```

The first invocation writes the source snapshot, prepared audit, docket, and
adjudication prompt, then reports `stage=adjudication` and an exact
`expected_response` path. Submit the prompt together with the adjacent
`prompt_manifest`; the response must echo its exact `prompt_sha256`. Place only
the contracted JSON response at that path. Rerun the same command; it validates
the response, writes the selected-evidence packet and synthesis prompt, and
reports `stage=synthesis`. Repeat the prompt-plus-manifest handoff. A third
invocation validates and renders all four outputs, rederives the full lineage
from the retained source snapshot, and byte-verifies the results.

`advance` deliberately does not hide model execution inside the pipeline. The
two response files are explicit, inspectable trust boundaries, while rerunning
the same command supplies the orchestration and status behavior. Existing
artifacts are immutable by default; use `--force` only when deliberately
regenerating a changed run.

Related write sets are conflict-checked before publication. Their prepared or
validated manifest is written last and serves as the completion marker; a crash
can leave identical partial files, but cannot produce a verified completion.
Rerunning the same command repairs that partial set, while `verify` rejects any
incomplete or inconsistent lineage.

The lower-level `prepare`, `render-adjudication`, `validate-adjudication`,
`render-synthesis`, `validate-synthesis`, and `verify` commands remain available
for debugging or custom budget limits. Every lower-level handoff command must
repeat the exact preparation policy and limits; omitted options mean strict
defaults. For example, a docket prepared with `--hft-policy quarantine` must use
that flag again at rendering, validation, synthesis, and verification. All
synthesis limits are bound into the packet, prompt manifest, and validated
artifact; `advance` accepts the same limit flags, and `verify` requires those
same flags so packet-declared limits are checked against trusted caller policy.
Library callers must likewise pass an explicit `SynthesisOptions`; omitted
policy is rejected rather than recovered from an artifact. Response bytes,
model-authored annotation lengths, and aggregate rendered-output bytes have
high caller-bound safety ceilings. Overflow fails before publication; the
workflow never truncates text or reduces candidate coverage to fit them.
Adjudication has no
caller-controlled discovery quota: after existing decisions are made, its
new-candidate capacity is exactly `512 - selected_existing_count`. Rejecting a
properly evidenced optional candidate therefore releases capacity; no slot is
reserved merely because a candidate was eligible for review.

## Prepare trust boundary

`prepare` validates ayah/pericope identity, computes raw and canonical source
hashes, checks HFT packet and reader identity, records every discovered seed,
and builds a deterministic candidate docket. The default HFT policy is strict.
The pericope is bounded before ref expansion by caller policy
(`--max-pericope-ayahs`, default 512), and that limit is persisted in the docket.
Each ledger seed carries its exact source pointer, so repeated labels at distinct
locations remain separate while duplicate source identities fail validation.
An explicit quarantine run preserves malformed HFT in the prepared diagnostic
artifact while making it invisible to adjudication. This includes malformed
top-level packet, summary, reader, and seed shapes: they produce explicit
`parse_failed` ledger entries but do not become mandatory blockers after the
entire HFT source fails trust admission and is excluded.

Packet-bound HFT readers must include this response field:

```json
{
  "packet_identity": {
    "focus_ref": "29:38",
    "protocol": "focus-trace-pericope-lean-v1",
    "window_sha256": "canonical-json-sha256"
  }
}
```

Older scope-valid responses can be admitted only with
`--allow-legacy-hft-response`; their support remains labeled
`legacy_unbound`. A quarantine run can have all mandatory docket candidates
ready without HFT, but its prepared artifact says
`readiness.mode=quarantine_without_hft` and carries an explicit warning. The
compatibility-prone `adjudication_ready` boolean is deliberately not emitted;
consumers use `readiness` and `mandatory_candidates_ready`.

An explicitly null focus-root dictionary blocks model handoff by default. A
deliberate degraded run requires `--allow-incomplete-branch-coverage`; that
authorization is persisted for audit but is not trusted from the artifacts. The
caller must repeat it at every downstream handoff, which rederives the docket
from the source using caller-supplied policy. The gate also exposes
`branch_coverage_complete`,
`incomplete_branch_coverage_authorized`, and `degraded_reasons`, so downstream
tools do not infer capability from warning prose.

An explicitly global HFT packet uses `focus-trace-surah-lean-v1` together with
`window_scope=surah`, a contiguous window beginning at ayah 1, and the same
packet-identity binding. Its candidates enter the global lane, never macro.
Every HFT activation-trace row must also carry a canonical ASCII
`mapped_root_id`, canonical ASCII `branch_id`, and canonical in-window
`source_ref`. The resulting branch must exist in the retained focus or
pericope branch registry. A bad trace blocks strict preparation; quarantine
retains and accounts the seed diagnostically while exposing none of it to the
model.

```bash
python3 _commentary/v3/workflow.py prepare \
  --bundle bundles/s029/29_38.ayah.json
```

For the currently mixed-scope S29 bundle, an exploratory non-HFT docket can be
prepared explicitly:

```bash
python3 _commentary/v3/workflow.py prepare \
  --bundle bundles/s029/29_38.ayah.json \
  --hft-policy quarantine
```

No source is silently trimmed or reclassified. Hard candidate/support/packet
budgets fail with a sizing diagnostic instead of dropping evidence.
Existing artifacts are idempotent only when their bytes match. A different
source, policy, or implementation result at the same ayah path fails with an
artifact conflict unless `--force` is supplied deliberately.

The docket keeps complete focus-root branches in `branch_registry` and
source-bound evidence for non-focus branches explicitly cited by valid nominations in
`nominated_branch_registry`. Arabic-root citations in legacy reader walks are
resolved against those registries; unresolved branch evidence makes a mandatory
candidate fail preparation. Present-but-empty source slots are recorded in the
prepared `source_inventory`. Empty candidate collections contribute no seeds;
an explicitly present null or empty HFT packet is instead malformed
trust-bearing input, so strict mode fails and quarantine mode records one
`hft-structure` `parse_failed` seed. Only a missing HFT key is classified as
absent.
Canonical `root_.../B...` citations use the same closed registry lookup: unknown
refs are retained as unresolved diagnostics, never as trusted support metadata.
Every trusted candidate is likewise bound only to trusted, citable supports.
Cross-run publication anchors are accepted only as exact
`[focus_word_ref, root_id, nonempty_branch_ids]` tuples; malformed anchor
objects or partial tuples are recorded as parse failures instead of being
silently downgraded to branchless findings. The word ref must exist in the
focus QAC inventory, the root ID must be carried by that exact QAC word, and
every branch must belong to that registered root.
Word-analysis rows likewise require a canonical focus-ayah word ref whose
index is bounded by the retained word array. Their obligations are a closed
contract: `must_integrate` and `candidate` are mandatory docket seeds, while
`ledger_only` remains optional apparatus; missing or unknown values are parse
failures. The original orthographic word numbering is retained even where the
bundle explicitly reports that it cannot be joined one-to-one to QAC words.
An explicitly null focus-root `dictionary_entry` is retained as a zero-branch
root record and reported through `scope.branch_coverage`, prepared diagnostics,
and readiness warnings. A missing key, an empty branch array, or a malformed
non-null dictionary fails preparation. Arabic hamza-seat variants are
canonicalized for QAC-to-lexicon joins and word-analysis root matching while the
original evidence spelling remains preserved.
Legacy inter-ayah rows, whole-reading prose, and generated channel prose are
also inventoried with explicit exclusion reasons instead of disappearing from
coverage.

Every support record receives a canonical role derived from an allowlisted
`source_type` plus exact JSON-pointer shape: `focus_occurrence`,
`candidate_evidence`, `branch_nomination`, or `context_only`. The role is not
model-authored and is rederived during docket validation. Unknown, aliased, and
nested provenance shapes fail closed. The adjudication docket retains no
unowned support records: every visible support must belong to at least one
candidate. Each support also carries its own source-derived `branch_refs`.
Candidate-level branch membership cannot make an unrelated support nominate or
contact that branch; channel nominations come only from the exact
`active_motifs` support and HFT nominations only from the exact activation
trace. Support and candidate IDs cover every semantic field, so recomputing only
an enclosing payload hash cannot conceal field mutation.
Only deterministic `qac_morpheme` carriers establish focus-root occurrence.
Editable word-analysis root prose is interpretive evidence and cannot mint root
ownership, even when its word ref is otherwise valid.

Adjudication must return an ordered `branch_review` that covers every focus
branch followed by every nominated external branch exactly once. An `activated`
entry must resolve to a selected docket candidate or `new:<proposal_key>`
carrying that branch; an `unactivated` entry carries a bounded reason and no
activation. Its structured basis cites either only the exact occurrence or
nomination grounding, or that grounding plus specific candidate evidence that
was tested and rejected. Focus entries require trusted focus-occurrence grounding, while
nominated entries require trusted, citable `branch_nomination` support owned by
a candidate that nominated the branch and whose support-level `branch_refs`
contains that exact branch. Every reason quotes the registered focus
gloss or nominated image.
Preparation proves these requirements are satisfiable before setting
`readiness.ready`; missing focus occurrence or nomination support blocks handoff
with structured diagnostics. A legacy-only citation remains in the candidate
ledger as unresolved audit material and cannot enlarge the nominated review
registry. Nominated branches must also have a nonempty image descriptor and a
trusted nomination owner.
Activated entries additionally provide one exact support excerpt per selected
activation. That contact support must be candidate-owned, trusted, citable, and
role-labeled `candidate_evidence`; registry definitions, channel
`active_motifs`, and generic context cannot establish contact by
themselves. Runtime validation checks registry order, full coverage, exact
quotes, support ownership, and selected branch lineage.
Existing docket candidates can activate a branch only when a structured
cross-run publication anchor explicitly binds it. Inferred contact must be a
bounded new candidate whose mechanism contains an exact branch-specific contact
clause. Each recovered activation needs a different evidence support, preventing
one generic quote from activating many branches or many proposals. A focus-root
contact must use either evidence that explicitly cites the branch or word/topic
evidence whose analytic row maps to the root through the bundle's lossless
`word_morpheme_spans`. The span table, not the preserved upstream word number or
the prose `root_display`, is the authoritative QAC join. It is shape- and
lineage-validated before use; packages that genuinely omit it retain word
evidence but cannot use that evidence to ground root-branch contact, while a
present malformed or `null` table fails preparation. Evidence co-owned with an exact branch-specific nomination from
its source record is also eligible for bounded review. A nominated external
contact must use explicitly branch-bound evidence or evidence owned by the same
candidate as its exact branch-specific nomination. New proposals may cite every
needed item in the closed support and branch registries; there is no smaller
support or branch quota. Only trusted, citable occurrence, nomination, and
evidence roles are admissible.

The synthesis model receives every selected candidate with its complete support
and branch sets. It must emit exactly one finding per selection in packet order;
findings cannot be merged, sampled, or capped by caller-supplied density limits.
Every candidate's exact adjudicated claim must land in a unique, non-overlapping
prose substring. Its reader payoff and containment must be rendered naturally,
while their exact adjudicated forms remain in deterministic evidence alongside
the complete mechanism, deletion loss, direct support quote, support set, and
branch set. The complete branch
review ledger remains outside the synthesis model packet and is joined back to
the docket only by deterministic friction rendering. Branch descriptors,
boundaries, reasons, exact contact excerpts, source identities, support roles,
and support texts are rendered there in full, so a silent miss cannot
masquerade as an inspected rejection and the audit remains independently
expandable.
Every rejected or deferred decision is also rendered as its complete normalized
record with its candidate and cited support records. Every selection-ineligible
candidate and each of its support records is rendered in docket order; the
deterministic friction output does not summarize these ledgers away.
Each validated finding receives one deterministic candidate-contribution record;
these records are included in the semantic hash and rendered in evidence output.
The prose lower bound grows from all exact required landings, while the fixed
512 finding, paragraph, and friction ceilings are fail-loud infrastructure guards,
not pruning targets. Candidate branch
refs are nominations, not automatic activations. Generic existing candidates
retain none; an explicit publication may retain its anchored subset, while an
inferred relation must use a bounded new candidate. `legacy_unbound` material
is audit-only and cannot enter synthesis.

Adjudication is exhaustive across every trusted, citable, selection-eligible
candidate. Grammar, lexical range, sound, ambiguity, neighboring activation,
and bounded exploratory resonance remain admissible even when their conclusions
overlap. Exclusion is closed to unsupported, unsafe, out-of-scope, or exact
semantic-duplicate cases and requires a substantive rationale plus an exact
candidate-owned evidence quote; duplicates must identify selected targets and
preserve their full branch union. Similarity never triggers rejection.
Every nonselected rationale must contain that exact candidate-owned quote, so a
generic rejection cannot pass merely by carrying a valid citation.
Every selected or newly recovered contribution retains a concrete deletion loss
and cannot subsume another selected record. The model must attest that discovery
is complete; overflow fails loudly. The fixed ceiling is 512 total selections,
not a pruning target.

The JSON schemas document the wire format. The standard-library Python
validators are authoritative at runtime and additionally verify semantic hashes,
ID uniqueness, support references, branch partitioning, quarantine isolation,
source-snapshot identity, prepared/docket rebinding at every model handoff,
exact prompt and response lineage, and exact final output bytes.
Public adjudication and synthesis rendering and raw-response validation always
reload and rederive their persisted inputs from the retained source snapshot.
Public synthesis artifact validation applies the same binding. The private
unbound packet constructors and validators use leading-underscore names, exist
only for deterministic unit tests and internal orchestration, and are not model
handoff APIs.

## Tests

```bash
python3 -m unittest discover -s _commentary/v3/tests -v
```
