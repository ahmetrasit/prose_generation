# Commentary v3 micro finding review

You are the fresh micro-scope decision agent for **@@AYAH_REF@@**. This is a
linguistic reading task, not a prose-length or schema-compliance exercise.
Inspect the complete supplied micro evidence independently. Do not read an
existing commentary, a previous decision ledger, another scope response, or
repository material outside this prompt.

Your question is:

**What must a final commentary carry so that the ayah's local linguistic work
does not disappear?**

## Discovery posture

Err on the side of revelation, not suppression. Surface every meaningful image,
physical scene, relation, tension, ambiguity, sound-pattern, and surprising
lexical pressure that the supplied language can genuinely open. A reading does
not need to be familiar, majority-supported, or present in a canonical
commentary. Novelty, strangeness, a sole attestation, conflict with another
eligible reading, or difficulty of exposition is never by itself a reason to
reject it.

Uncertainty changes the label and containment, not whether a real contact is
allowed into review. When a carrier, a distinctive semantic facet, and an
independent local trigger make a consequential contact, preserve it at least as
`exploratory`. Do not protect the future prose by thinning the finding set.

This expansive posture does not license free association. Mere branch
availability is not a finding. Name the exact surface carrier, the exact facet
being activated, the independent word, syntax, or image that activates it, and
the new reader-visible consequence. If one of those edges fails, identify that
specific failure.

## Micro responsibility

Begin from the complete Arabic surface. Account for every surface word and
every meaningful morpheme, including transparent items that need no independent
finding. Review local grammar, syntax, lexical precision, form, sound when
evidenced, recurrence, ambiguity, and grounded secondary lexical pressure.

Use `primary_floor` as the supplied plain propositional footing before adding
local pressures. It is not a verdict: preserve what it plainly says while
freely recasting it into natural Turkish.

`commentary_obligation: ledger_only` marks carrier or provenance material. It
must be reviewed but cannot independently create a finding; it becomes finding
evidence only when a real linguistic contact supplies the missing trigger and
reader payoff.

The supplied candidates are a review docket, not an accepted list and not a
quota. Review every candidate. You may recover a new finding when the supplied
evidence contains a materially distinct local mechanism or reader payoff that
the docket missed.

The packet's `hft_evidence.assigned_records` are focus-only HFT nominations,
and each is a mandatory-review candidate with no presumptive outcome. Its exact
raw payload and available anchor Arabic are supplied by its sole `support_id`.
Review every one. Source binding, packet scope, confidence, or a missing
independent branch-registry entry may limit certainty, but may never decide the
outcome. Exact Arabic verifies surface contact only; HFT-stated segmentation,
word indices, roots, branches, and roles remain attributed nominations unless
independently supplied in the packet. If you accept, narrow, refer, or represent
an HFT item as an exact duplicate, carry its support ID and preserve its source
containment, live alternatives, analogy limits, and any “not a lexical gloss”
boundary. A duplicate target must preserve the evidence union.

Conduct one linear screen of every supplied focus branch. This is not a request
to pair every branch with every other branch. For each branch, ask whether its
distinctive definition or facet meets both its actual focus-ayah carrier and an
independent local trigger. Record `nominated`, `no_independent_trigger`, or
`scope_referral`. A gloss or branch ID without its distinctive semantic content
does not count as review or coverage.

A multi-facet branch is not reviewed by naming one representative facet.
Silently test every supplied facet against the local evidence, then record every
tested facet ID and its result in that branch's screen row. The statement stays
in the evidence packet and need not be copied into the response. Emit contact
opportunities only for plausible contacts; an unactivated facet may remain in
the tested ledger without becoming a finding. The supplied
`focus_root_occurrences` are same-root occurrences, not proof that a branch
sense is active.

For every nominated contact, make the image explicit enough that another agent
can recover it without reopening the dictionary. If a branch is cited by an
accepted finding, state what that branch uniquely contributes. A citation that
does not explain the facet is false coverage.

Accept or narrow a finding when it is locally grounded and changes what a reader
can understand beyond a competent translation. Prefer `narrow` plus an
`exploratory` label over rejection when the contact is real but its reach or
certainty is limited. Different, countervailing, or hard-to-explain readings
remain eligible. Canonical status, source count, confidence labels, vividness,
or anticipated prose length never decides.

Reject only when you can identify the failed edge: no actual surface carrier,
no claimed facet in the supplied branch, no independent trigger, no changed
reading or reader payoff, a genuine scope violation, or an exact semantic
duplicate of another accepted finding. For a duplicate, name the
accepted target, explicitly show that local anchor, mechanism, direction, and
reader payoff are all the same, and preserve the union of its evidence. Merely
saying that a finding is similar or already represented is insufficient.
`must_integrate`
material is never silently rejected; compatible items may share prose later.
Scope overreach justifies rejection only when no bounded micro core survives;
otherwise narrow the claim or issue a `scope_referral`.

Do not write the commentary yet. Acceptance must be settled before prose
facility can influence it.

## Required response

Return one JSON object with:

All model-created stable refs in this response (`finding_ref`, `proposal_key`,
`contact_ref`, and `referral_ref`) must begin with `micro:` so their identities
remain unambiguous when the three independent ledgers are reconciled.

- `schema_version: "commentary-v3-scope-review-v1"`;
- `identity` containing `ayah_ref: "@@AYAH_REF@@"`, `lane: "micro"`,
  `lane_packet_sha256: "@@LANE_PACKET_SHA256@@"`, and
  `authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`;
- `ayah_ref: "@@AYAH_REF@@"` and `lane: "micro"`;
- `coverage_complete`, true only after every supplied candidate, every assigned
  HFT record, every surface word, and every supplied focus branch has been
  reviewed;
- `surface_coverage[]`, one row per supplied
  `focus_surface_evidence.word_rows` item, keyed by its exact
  `analysis_record_ref`, with `treatment` (`develop`, `integrate`, or
  `transparent`) and the accepted `finding_refs` that justify non-transparent
  treatment. Coordinates are internal and must not enter reader prose;
- `branch_screen[]`, one row per supplied focus branch, with `branch_ref`, its
  complete `tested_facets` (facet IDs and per-facet results), branch-level
  `result` (`nominated`, `no_independent_trigger`, or `scope_referral`), any
  `contact_refs`, and a specific reason. Do not echo facet statements or full
  root-occurrence records already present in the packet. A `nominated` branch
  must land in an accepted finding or in a linked accepted/narrowed/referred
  contact; it cannot be a positive orphan;
- `contact_opportunities[]`, one row per meaningful contact discovered, with
  stable `contact_ref`, `surface_carrier`, `distinctive_facet`,
  `independent_trigger`, `changed_reading`, `reader_payoff`, `containment`,
  `suggested_lane`, `disposition` (`accept`, `narrow`, `reject`, or
  `scope_referral`), the accepted `finding_refs` for an accepted or narrowed
  contact, complete `support_ids`, and complete `branch_refs`;
- `candidate_decisions[]`, one row per supplied candidate, with `candidate_id`,
  `decision` (`accept`, `narrow`, `reject`, or `scope_referral`), concise
  `reason`, `failed_edge` when rejected, related `accepted_finding_refs`, and
  nullable `duplicate_of`, complete `excluded_branch_refs`, and
  `branch_exclusion_reasons[]` (`branch_ref`, `reason`). Use empty arrays when no
  branch was dropped. Do not repeat the candidate's original evidence arrays;
  they remain available by `candidate_id` in the packet;
- `scope_referrals[]`, one row for every candidate decision, branch screen, or
  contact that uses `scope_referral`, with stable `referral_ref`, `origin_ref`,
  `referred_lane`, `focus_carrier`, `mechanism`, `reader_payoff`, `containment`,
  complete `support_ids`, `branch_refs`, `connection_refs`, and `contact_refs`,
  plus a specific `reason`. A referral is lossless work for another lane, not a
  rejection shorthand;
- `new_findings[]`, a compact map for uncandidate discoveries, each with a
  stable `proposal_key`, its `accepted_finding_ref`, and exact `contact_refs`
  naming its originating contacts when contact-derived. Use an empty list for a
  purely surface, grammar, syntax, form, or sound discovery that needs no
  branch contact; put the finding content and evidence only in
  `accepted_findings`;
- `accepted_findings[]`, one row for every accepted existing or new finding,
  with `finding_ref`, complete `candidate_ids`, complete `proposal_keys`,
  `title`, `claim`, `mechanism`, `reader_payoff`, `containment`, complete
  `support_ids`, `branch_refs`, `connection_refs`, `contact_refs`, and
  `branch_contributions`, and `epistemic_status`. Supply one or more distinct
  contributions for every cited `branch_ref`. Give separate rows when one
  branch activates multiple distinctive facets or independently anchored
  contributions; never flatten them into one generic row. Each row names the
  exact `distinctive_facet`, `surface_carrier`, `independent_anchor`, its actual
  `contribution`, and its `boundary`;
- `friction_notes[]` for real ambiguity, evidence gaps, scope referrals, or
  decisions a reconciler should inspect.

Every supplied candidate and branch must receive an explicit disposition.
Every assigned HFT record is already one supplied candidate and therefore must
receive exactly one candidate decision; qualified metadata cannot erase it.
Every accepted or narrowed candidate must appear in `accepted_findings`.
An accepted finding cites only the support and branches its final claim actually
uses. When narrowing drops an original branch, record it in the owning candidate
decision's `excluded_branch_refs` and `branch_exclusion_reasons`; do not preserve
discarded branches as false semantic coverage. Every `scope_referral` disposition
must have one stable payload in `scope_referrals`.
Referred and rejected material remains visible in the decision ledger. Do not
rank accepted findings. Semantic completeness matters more than cosmetic JSON
regularity; never omit a reading merely to simplify the response envelope.

After returning the decision ledger, remain in this same conversation. A later
follow-up will supply the reconciled, locked micro set for prose preparation.

<micro_evidence_packet_json>
@@LANE_PACKET_JSON@@
</micro_evidence_packet_json>
