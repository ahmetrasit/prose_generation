# Commentary v3 macro finding review

You are the fresh macro-scope decision agent for **@@AYAH_REF@@**. This is a
contextual linguistic reading task, not a prose-length or schema-compliance
exercise. Inspect the complete supplied pericope-bound evidence independently.
Do not read an existing commentary, a previous decision ledger, another scope
response, or repository material outside this prompt.

Your question is:

**What does the declared neighboring context genuinely change in the reading
of this ayah?**

## Discovery posture

Err on the side of revelation. Surface every meaningful contextual image,
counter-image, sequence, reversal, spatial relation, social mechanism, and
surprising before/after change supported by the supplied pericope. A reading
does not need canonical precedent or majority support. Novelty, strangeness,
sole attestation, conflict with another eligible reading, low source count, or
difficulty of exposition is never by itself a rejection reason.

Uncertainty controls `epistemic_status` and containment, not admission to
review. If the contact is real but its reach is limited, narrow it and preserve
it as exploratory. Do not thin the finding set for the convenience of the final
writer.

Expansion still requires an edge: identify the focus-ayah carrier, the exact
contextual anchor, the contact between them, and the changed reading. Mere
dictionary resemblance or thematic likeness is not enough.

An anchor reference or contextual statement may support only the relation it
actually states. When neighboring ayah text is not supplied, do not invent its
wording, morphology, or lexical identity; narrow the finding to what the
supplied statement establishes.

## Macro responsibility

For each candidate, identify the exact word, relation, or act in the focus ayah
through which the pericope enters. State the before/after movement: what the
ayah yields locally, what the declared context activates, sharpens, revises, or
places under pressure, and what the reader can consequently see.

Use `primary_floor` as the supplied plain propositional `local_before` footing.
It is not a verdict: preserve what it plainly says while freely recasting it
into natural Turkish.

The supplied candidates are a review docket, not an accepted list and not a
quota. Review every candidate and the supplied contextual evidence. You may
recover a missed finding when that evidence supports a materially distinct,
pericope-bounded change.

The packet's `hft_evidence.assigned_records` are HFT nominations whose explicit
ayah anchors all lie inside the declared pericope, and each is a
mandatory-review candidate with no presumptive outcome. Its exact raw payload
and exact available anchor Arabic are supplied by its sole `support_id`. Review
every one. Source binding, broader packet scope, confidence, or a missing
independent branch registry may limit certainty, but may never decide the
outcome. Exact Arabic verifies surface contact only; HFT-stated segmentation,
word indices, roots, branches, and roles remain attributed nominations unless
independently supplied. If you accept, narrow, refer, or represent an HFT item
as an exact duplicate, carry its support ID and preserve its source containment,
live alternatives, analogy limits, and any “not a lexical gloss” boundary. A
duplicate target must preserve the evidence union.

Review every supplied `connection_registry` row. These are same-surah targets
inside the declared pericope, including derived reciprocal nominations and
counterevidence. Their prior attention labels are not verdicts. Exact target
Arabic is supplied in `target_evidence`, but target morphology and lexical
analysis are not; do not invent those missing details. `reciprocal_evidence`
reports what a source-direction review said while looking back toward the focus
ayah. `reciprocal_nomination` invites fresh focus-side discovery;
`reciprocal_counterevidence` preserves a source-side `no value` or `reject`
assessment so asymmetry and failed edges remain visible. Neither record type nor
its `source_direction_label` is a focus-direction verdict, and negative evidence
must not pre-empt a real relation found by fresh assessment.
The source note is a lead, not the limit of admissible discovery: a different
bounded relation may be recovered when it is freshly grounded in the supplied
Arabic and returns through a named focus-ayah carrier. Do not invent lexical or
morphological details that are not supplied.
A connection may carry both reciprocal types and multiple distinct source
notes. Inspect every nested row, keep disagreements visible, and never collapse
the two directions into one judgment.

Every authored connection and every nested reciprocal row carries
`source_row_role`; a derived connection exposes its roles through its nested
`reciprocal_evidence` rows.
`ranked_review` identifies the first 100 reviewed candidates;
`missing_ayah_suggestion` identifies the source agent's later high-recall
follow-up additions. Both invite fresh analysis. A suggestion is not
pre-accepted, and neither role nor its label may veto a grounded discovery.

An occasional `self_reference_source_row` preserves an original mapping row
that names the focus ayah itself. Keep its stated emphasis visible, but do not
treat the generated self-reiteration as a second direction, independent
corroboration, or a contextual discovery.

When `source_target_is_range` is true, the source note was authored for the
complete range, not independently for every expanded ayah. The packet supplies
exact Arabic for all components in `source_target_range_evidence`. Test what the
named component itself contributes; keep sequence-level images and claims at
range scope, and never project another component's wording or morphology onto
this one.

Do not search only for confirmation of the supplied candidates. Make an
independent pass through the contextual evidence for uncandidate images and
relations. Record every meaningful contact opportunity before deciding which
ones become findings. For every cited branch, explain its distinctive semantic
facet and contribution; a branch ID by itself is not coverage.

Use the complete focus-branch atlas, not only candidate-cited branches. Silently
scan every atlas branch and every one of its supplied facets against the
pericope evidence. A multi-facet branch is not reviewed by choosing one
representative facet. Record `atlas_facets_tested[]` for every branch with a
plausible contextual contact or an existing citation, listing all tested facet
IDs, result, and any contact refs. The facet statements stay in the packet and
need not be copied into the response. Emit findings only for real
contacts; do not enumerate branch-by-branch combinations.

Some nominated branches supply their semantic facet as `image_ar`, `image_en`,
`branch_image_ar`, or `what_is_ar` rather than a numbered concept-map facet.
Treat that supplied image as the facet; identify it by its source field (or use
`facet_id: null`) without inventing a facet ID.

Accept or narrow a change with a visible local anchor, a real contextual
mechanism, and a distinct reader payoff. A neighboring image may sharpen this
ayah without becoming its lexical meaning. Different or countervailing
contextual changes remain eligible together.

Reject only when you can name the failed edge: no ayah-local carrier, no claimed
contextual anchor, no actual contact, no changed reading or reader payoff, an
uncontained scope excess, mere lexical availability, or an exact duplicate.
For a duplicate, name the accepted target, explicitly show that local anchor,
mechanism, direction, and reader payoff are all the same, and preserve the
union of its evidence. Merely saying that it is already represented is
insufficient. Remote dictionary resemblance is not a mechanism. Similarity,
canonical status, source count, confidence labels, vividness, or anticipated
prose length never decides.
Scope overreach justifies rejection only when no bounded macro core survives;
otherwise narrow the claim or issue a `scope_referral`.

Do not rewrite the local grammar inventory and do not write the commentary yet.
Acceptance must be settled before prose facility can influence it.

## Required response

Return one JSON object with:

- `schema_version: "commentary-v3-scope-review-v1"`;
- `identity` containing `ayah_ref: "@@AYAH_REF@@"`, `lane: "macro"`,
  `lane_packet_sha256: "@@LANE_PACKET_SHA256@@"`, and
  `authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`;
- `ayah_ref: "@@AYAH_REF@@"` and `lane: "macro"`;
- `coverage_complete`, true only after every supplied candidate, every assigned
  HFT record, and every supplied contextual evidence group and connection has
  been independently scanned;
- `connection_coverage[]`, one row per supplied connection, with
  `connection_ref`, `target_ref`, `result` (`accepted`, `narrowed`,
  `represented`, or `rejected`), related `finding_refs`, and a specific reason
  independent of the prior label;
- `contact_opportunities[]`, one row per meaningful contextual contact, with a
  stable `contact_ref`, `focus_carrier`, `context_anchor`, `distinctive_facet`,
  `local_before`, `context_after`, `mechanism`, `reader_payoff`, `containment`,
  `suggested_lane`, complete `support_ids`, complete `branch_refs`, and complete
  `connection_refs`;
- `atlas_facets_tested[]` as defined above, so a cited or plausible branch cannot
  hide behind a generic gloss or one representative facet;
- `candidate_decisions[]`, one row per supplied candidate, with `candidate_id`,
  `decision` (`accept`, `narrow`, `reject`, or `scope_referral`), concise
  `reason`, `failed_edge` when rejected, related `accepted_finding_refs`, and
  nullable `duplicate_of`, complete `excluded_branch_refs`, and
  `branch_exclusion_reasons[]` (`branch_ref`, `reason`). Use empty arrays when no
  branch was dropped. Do not repeat the candidate's original evidence arrays;
  they remain available by `candidate_id` in the packet;
- `scope_referrals[]`, one row for every candidate decision, atlas row, or
  contact that uses `scope_referral`, with stable `referral_ref`, `origin_ref`,
  `referred_lane`, `focus_carrier`, `mechanism`, `reader_payoff`, `containment`,
  complete `support_ids`, `branch_refs`, `connection_refs`, and `contact_refs`,
  plus a specific `reason`. A referral is lossless work for another lane, not a
  rejection shorthand;
- `new_findings[]`, a compact map for uncandidate discoveries, each with a
  stable `proposal_key`, its `accepted_finding_ref`, and originating
  `contact_refs`; put the finding content and evidence only in
  `accepted_findings`;
- `accepted_findings[]`, one row for every accepted existing or new finding,
  with `finding_ref`, complete `candidate_ids`, complete `proposal_keys`,
  `title`, `local_before`, `context_after`, `claim`, `mechanism`,
  `reader_payoff`, `containment`, complete `support_ids`, `branch_refs`,
  `connection_refs`, `contact_refs`, and `branch_contributions`, and
  `epistemic_status`. Each branch
  contribution must state the distinctive facet, carrier, independent anchor,
  actual contribution, and boundary;
- `friction_notes[]` for live ambiguity, evidence gaps, scope referrals, or
  decisions a reconciler should inspect.

Every supplied candidate must receive exactly one decision. Every accepted or
narrowed candidate must appear in `accepted_findings`. Referred and rejected
material remains visible in the decision ledger. Do not rank accepted findings.
Every assigned HFT record is already one supplied candidate; qualified metadata
cannot erase it.
An accepted finding cites only the support and branches its final claim actually
uses. When narrowing drops an original branch, record it in the owning candidate
decision's `excluded_branch_refs` and `branch_exclusion_reasons`; do not preserve
discarded branches as false semantic coverage. Every `scope_referral` disposition
must have one stable payload in `scope_referrals`.
Semantic completeness matters more than cosmetic JSON regularity; never omit a
reading merely to simplify the response envelope.

After returning the decision ledger, remain in this same conversation. A later
follow-up will supply the reconciled, locked macro set for prose preparation.

<macro_evidence_packet_json>
@@LANE_PACKET_JSON@@
</macro_evidence_packet_json>
