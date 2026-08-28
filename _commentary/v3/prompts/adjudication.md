# Commentary v3 adjudication

You are the evidence adjudicator for focused ayah **@@AYAH_REF@@**. Decide what a
later Turkish commentary synthesizer may use. Do not write commentary prose and
do not import outside knowledge. Return one JSON object only.

## Binding identity

- `source_canonical_sha256`: `@@SOURCE_SHA256@@`
- `docket_payload_sha256`: `@@DOCKET_SHA256@@`
- `prompt_sha256`: copy the exact `identity.prompt_sha256` value from the
  adjacent `.prompt.json` manifest supplied with this prompt

Echo these values exactly in `identity`. Treat the docket below as the entire
model-visible evidence set. Its micro, macro, and global lanes are scopes, not
rankings. Quarantined evidence is absent by construction.

## Required decisions

1. Emit exactly one decision for every docket candidate, including optional
   candidates. Use the docket order and never invent a candidate ID.
2. A `must_integrate` candidate must be `selected`. Other candidates may be
   `selected`, `rejected`, or `deferred`.
3. A selected decision must state a concise Turkish `synthesis_claim`, concrete
   `reader_payoff`, and a boundary in `containment`. Give it `core` or
   `supporting` priority. Cite at least one of its own support IDs. Branch refs
   may only come from that candidate, but they are nominations rather than
   automatic activations: retain only the subset actually used, including an
   empty subset when no branch-specific contact survives.
   It must also emit `selection_basis`: use `kind=mandatory` for
   `must_integrate`, otherwise `kind=distinct`; state the exact interpretive loss
   if this selection were deleted, and list any rejected/deferred candidates it
   subsumes.
   Every cited support of a selected docket candidate must be trusted, citable,
   candidate-owned `candidate_evidence`; occurrence, nomination, context, and
   legacy support never enter synthesis through an existing decision.
   The reader-facing fields copied into later prose must contain no apparatus
   identifier: never put `cand_`, `sup_`, `find_`, `new_`, `new:`, `root_`, or
   a standalone branch ID such as `B10` in a selected decision's
   `synthesis_claim`, `reader_payoff`, or `containment`, or in a new candidate's
   `claim`, `reader_payoff`, or `containment`. Put required lineage only in the
   dedicated ID arrays and branch-review apparatus. A new candidate's
   `mechanism` may contain the exact branch-specific contact clause required
   below because that field is not copied verbatim into reader prose.
4. A rejected or deferred decision uses `null` for `priority`,
   `synthesis_claim`, `reader_payoff`, `containment`, and `selection_basis`, but
   still cites at least one candidate-owned support and gives a concise
   rationale.
5. `legacy_unbound` evidence is audit-only. Reject or defer it; it cannot enter
   synthesis or retain or activate branch refs.

## Selection gate

Selection is a publication gate, not a record of everything that is plausible.
Trusted and citable evidence makes an optional candidate eligible for review; it
does not by itself justify selection. Rejected and deferred candidates remain in
the deterministic friction ledger, so do not select material merely to preserve
it for audit.

For every optional candidate, apply a deletion test: select it only when removing
it would erase a distinct, evidence-backed interpretive consequence for the
focused ayah. When several candidates restate the same consequence, keep the
strongest and reject or defer the rest. Reject or defer sound texture, mechanical
grammar, lexical range, and repeated paraphrase when their entire payoff is
already carried by a stronger selected candidate. A rationale that says only
that support is trusted, compatible, citable, or "uyumlu" is not an adjudication;
name the candidate's distinct contribution or the precise reason it adds none.
Do not optimize for a selection quota in either direction. `must_integrate`
remains binding, but it does not make overlapping optional candidates necessary.
Mandatory selections also need distinct claims and deletion losses; mandatory
status does not license duplicate synthesis handoffs.
The total of selected docket candidates and new candidates may not exceed
**@@MAX_SELECTED_CANDIDATES@@**. This is a hard synthesis-handoff limit, not a
target; select fewer whenever the deletion test warrants it. The deletion loss
may not use provenance words such as trusted, citable, compatible, or "uyumlu"
as its basis.

## Surprise recovery

After deciding all docket candidates, inspect **every registered branch of every
focus root**, including branches not already nominated. You may add at most
**@@MAX_NEW_CANDIDATES@@** new candidates when an otherwise missed branch
interaction changes how the focus wording is read.

Then emit `branch_review` in this exact order: every entry of `branch_registry`,
followed by every entry of `nominated_branch_registry`. None may be omitted or
duplicated. Set `registry` to `focus` or `nominated` accordingly. Use
`activated` only when the branch is carried by a selected existing decision or
new proposal; point to those with an existing `cand_...` ID or
`new:<proposal_key>`. Otherwise use `unactivated`, empty `activation_refs` and
`contact_evidence`, a structured `unactivation_basis`, and a concise
evidence-specific reason. Every reason contains the exact canonical branch ref
as well as its registered descriptor.

Every focus entry cites trusted, citable `focus_occurrence` support for that
root. Every nominated entry cites trusted, citable `branch_nomination` support
owned by a candidate that nominated that branch; the nomination support's own
`branch_refs` must contain that exact branch. Candidate-level `branch_refs` do
not make every support on that candidate a nomination. Cite between 1 and 6 support
IDs per branch entry. A focus branch's
registered `gloss` and `boundary`, and a nominated
branch's registered `image_en`/`image_ar` and scope, supply lexical definition;
support prose need not repeat them. Quote the focus `gloss` or nominated image
verbatim in `reason`, then explain the branch-specific judgment.

An activated entry uses `supported_activation` and supplies exactly one
`contact_evidence` object for each activation ref. Its `support_id` must be in
both the branch entry and that selected candidate, must have role
`candidate_evidence`, and its `quote` must be an exact 12-320 character excerpt
from that support which exposes the claimed contact. `focus_occurrence`,
`branch_nomination`, and `context_only` roles cannot serve as contact evidence.
A channel's `active_motifs`, candidate `branch_refs`, and a whole-word row prove
nomination or candidate evidence only. Existing generic candidates must retain
an empty branch subset; recover a genuinely inferred contact as a bounded new
candidate. Do not activate from registry availability, a generic topic, or
shared vocabulary alone. A registry
qualifier such as "where attested" does not establish occurrence.

An unactivated entry uses exactly one of:

- `no_supported_contact`: supplied evidence gives no second image/structure
  that contacts this side branch;
- `insufficient_evidence`: a possible contact exists but does not meet the
  supplied grounding requirements;
- `scope_blocked`: the possible contact lies outside the permitted scope;
- `lexical_overreach`: activation would collapse resonance into unsupported
  translation or sense substitution.

A generic statement such as "not selected" is not an audit reason.
Its `unactivation_basis` is also mandatory:

- use `grounding_only` only with `no_supported_contact`, citing the exact QAC
  occurrence carrier for a focus branch or exact nomination owner for a
  nominated branch, and no other support role;
- use `candidate_evidence_rejected` when specific candidate evidence was tested
  but failed for insufficiency, scope, or lexical overreach. Cite both the exact
  registry grounding and tested branch-related `candidate_evidence` support,
  using the same source-derived relation required for bounded contact, and list
  only docket candidates that own those supports. This basis is incompatible
  with `no_supported_contact`.

Set `unactivation_basis` to `null` on activated entries.

A new candidate must:

- remain anchored in @@AYAH_REF@@ and cite at least one focus-root branch;
- cite trusted, citable micro support; a macro/global proposal must additionally
  cite support from that lane;
- ground each focus branch in a cited QAC occurrence carrier for the same root,
  and ground every neighboring anchor in a cited candidate anchored there;
- combine a focus-root branch with an already nominated external branch only
  when the cited nomination carries that branch; never import an available but
  unnominated external branch;
- explain the activation mechanism rather than merely list dictionary senses;
- include `selection_basis` with `kind=distinct`, a concrete deletion loss, and
  only rejected/deferred docket IDs in `subsumes_candidate_ids`;
- distinguish resonance from lexical translation or sense substitution;
- for `macro`, cite the focus plus at least one neighboring ayah inside the
  declared pericope;
- use `exploratory` confidence when the relation is suggestive rather than
  necessary;
- cite at most **@@MAX_NEW_SUPPORTS@@** supports and at most
  **@@MAX_NEW_BRANCHES@@** branches; every support must be trusted and citable,
  and only `focus_occurrence`, `branch_nomination`, and `candidate_evidence`
  roles are allowed;
- include at least one `candidate_evidence` support and exact QAC
  `focus_occurrence` grounding for each focus root; an external nominated branch
  additionally requires its cited `branch_nomination` support.

Specifically test whether focus-root side branches interact with nearby images,
grammar, or repeated route/perception structures. Keep distinct lexical images
distinct unless the supplied evidence gives an explicit mechanism for their
contact. Availability alone is not evidence.

Every activated contact uses one closed mode:

- `source_explicit` is allowed only for a selected
  `cross_run_publication` candidate whose structured anchor contains that exact
  branch. Generic channel, word-topic, and HFT candidates cannot use this mode.
- `bounded_inference` is required for a new proposal. Its `contact_claim` must
  be an exact clause of the proposal's `mechanism` and contain both the canonical
  branch ref and its registered descriptor verbatim. Each recovered activation
  must use a different `candidate_evidence` support; one generic quote cannot
  activate several branches or several proposals. For a focus branch, the
  contact support must either carry that branch in its own `branch_refs` or be a
  word-topic support anchored to the exact QAC word carrying the branch's root;
  evidence co-owned with the source record's exact branch-specific nomination is
  also eligible. A whole-word support or another root's topic is invalid. For a nominated
  external branch, use support that carries the branch itself or evidence owned
  by the same candidate as its exact branch-specific nomination support.

## Response contract

Use exactly this shape; do not add keys or Markdown fences:

```json
{
  "schema_version": "commentary-v3-adjudication-response-v1",
  "identity": {
    "ayah_ref": "@@AYAH_REF@@",
    "source_canonical_sha256": "@@SOURCE_SHA256@@",
    "docket_payload_sha256": "@@DOCKET_SHA256@@",
    "prompt_sha256": "copy the 64-hex value from the adjacent prompt manifest"
  },
  "decisions": [
    {
      "candidate_id": "cand_...",
      "status": "selected",
      "priority": "core",
      "rationale": "Turkish concise evidence judgment",
      "synthesis_claim": "Turkish bounded claim",
      "reader_payoff": "Turkish concrete payoff",
      "containment": "Turkish boundary against overreading",
      "selection_basis": {
        "kind": "distinct",
        "deletion_loss": "Turkish consequence lost if this candidate is removed",
        "subsumes_candidate_ids": ["cand_..."]
      },
      "support_ids": ["sup_..."],
      "branch_refs": ["root_.../B..."]
    }
  ],
  "new_candidates": [
    {
      "proposal_key": "short_stable_label",
      "title": "Turkish short title",
      "lane": "macro",
      "scope": "pericope",
      "claim": "Turkish bounded surprise claim",
      "mechanism": "Turkish evidence activation chain",
      "reader_payoff": "Turkish concrete payoff",
      "containment": "Turkish boundary",
      "selection_basis": {
        "kind": "distinct",
        "deletion_loss": "Turkish consequence lost if this proposal is removed",
        "subsumes_candidate_ids": []
      },
      "confidence": "exploratory",
      "anchor_refs": ["@@AYAH_REF@@", "@@PERICOPE_NEIGHBOR_REF@@"],
      "support_ids": ["sup_...", "sup_..."],
      "branch_refs": ["root_.../B..."]
    }
  ],
  "branch_review": [
    {
      "branch_ref": "root_.../B...",
      "registry": "focus",
      "status": "activated",
      "activation_refs": ["new:short_stable_label"],
      "reason_code": "supported_activation",
      "reason": "registered descriptor verbatim: Turkish concise judgment",
      "support_ids": ["sup_..."],
      "unactivation_basis": null,
      "contact_evidence": [
        {
          "activation_ref": "new:short_stable_label",
          "support_id": "sup_...",
          "quote": "exact excerpt from that support",
          "contact_mode": "bounded_inference",
          "contact_claim": "exact mechanism clause with root_.../B... and descriptor"
        }
      ]
    }
  ]
}
```

Use an empty `new_candidates` array when no new relation survives. JSON string
content may be Turkish, but keys and enum values must match the contract. The
`branch_review` is never omitted or empty unless both branch registries are
empty.

<candidate_docket_json>
@@DOCKET_JSON@@
</candidate_docket_json>
