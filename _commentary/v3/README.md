# Commentary v3

This directory is a standalone ayah-commentary workflow. It ingests an existing
hermetic ayah bundle, retains its exact bytes under `inputs/source/`, and does
not import or execute legacy commentary scripts. Every retained input,
intermediate artifact, response, and final output remains under this directory.

## Evidence lanes

- **micro**: source-bound QAC morphology, word-analysis topics, and a compact record of
  every branch for every root mapped to the focus ayah;
- **macro**: pericope-anchored channel nominations and HFT only when its window
  exactly equals the declared pericope and each reader echoes the packet
  identity;
- **global**: reader walks and cross-run findings, each carrying an explicit
  trust label.

The lanes are evidence scopes, not separate model calls. The complete workflow
uses one structured adjudication call and one constrained Turkish synthesis
call.

## Complete workflow

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
that flag again at rendering, validation, synthesis, and verification. The seven
synthesis limits are bound into the packet, prompt manifest, and validated
artifact; `advance` accepts the same limit flags, and `verify` requires those
same flags so packet-declared limits are checked against trusted caller policy.
Library callers must likewise pass an explicit `SynthesisOptions`; omitted
policy is rejected rather than recovered from an artifact.
The adjudication `--max-new-candidates` limit is likewise caller-bound and must
be repeated by `render-synthesis`, `validate-synthesis`, and `verify`; a
validated artifact cannot promote its own downstream policy.

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

The docket keeps complete focus-root branches in `branch_registry` and compact
evidence for non-focus branches explicitly cited by valid nominations in
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
candidate as its exact branch-specific nomination. New proposals also obey the docket
support limit and a six-branch hard limit, and may cite only trusted, citable
occurrence, nomination, and evidence roles.

The synthesis model receives only selected candidates and their own supports
and branches. Every selection also carries its structured deletion loss, every
candidate's exact adjudicated claim must land verbatim in prose, and the union
of its finding citations must retain every selected branch. The complete branch
review ledger remains outside the synthesis model packet and is joined back to
the docket only by deterministic friction rendering. Branch descriptors,
boundaries, reasons, exact contact excerpts, source identities, support roles,
and support texts are rendered there in full, so a silent miss cannot
masquerade as an inspected rejection and the audit remains independently
expandable.
Each validated finding receives deterministic candidate-contribution records
that bind its exact landed claim to the adjudicator's deletion loss; these are
included in the semantic hash and rendered in evidence output. Candidate branch
refs are nominations, not automatic activations. Generic existing candidates
retain none; an explicit publication may retain its anchored subset, while an
inferred relation must use a bounded new candidate. `legacy_unbound` material
is audit-only and cannot enter synthesis.

Optional-candidate adjudication is deliberately selective. Provenance trust and
citable support establish eligibility, not publication value. The model applies
a deletion test and retains an optional candidate only when it contributes an
interpretive consequence not already carried by a stronger selection; all
rejected and deferred material remains recoverable in deterministic friction.
Selected optional and newly recovered candidates must provide a structured
`selection_basis` with a concrete deletion loss and explicit subsumption links.
The validator rejects provenance-only rationales and bases, normalized or
near-duplicate claims and losses across mandatory and optional selections, and
any attempt to subsume another selected candidate. The handoff has a
fixed ceiling of 64 total selections; this is a failure limit, not a target.

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
