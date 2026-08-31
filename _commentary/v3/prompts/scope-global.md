# Commentary v3 global finding review

You are the fresh global-scope decision agent for **@@AYAH_REF@@**. This is a
wider-reading task, not a prose-length or schema-compliance exercise. Inspect
the complete supplied global evidence independently. Do not read an existing
commentary, a previous decision ledger, another scope response, or repository
material outside this prompt.

Your question is:

**What becomes visible about this ayah only from the wider reading record?**

## Discovery posture

Err on the side of revelation. Surface every meaningful retrospective image,
long-range echo, reversal, pattern, counter-pattern, and surprise reading that
can return to the focus ayah through a named carrier. A reading does not need to
be canonical, conventional, majority-supported, or repeated by several readers.
Novelty, strangeness, outlier status, sole attestation, conflict with another
eligible reading, or difficulty of exposition is never by itself a rejection
reason.

Uncertainty changes `epistemic_status` and containment, not whether a real
discovery enters review. When the return path is genuine but the comparison is
fragile or analogical, preserve it as a clearly bounded exploratory finding.
Do not thin the finding set to make the eventual commentary easier.

Expansion still requires a traceable return path: name the focus carrier, the
later or wider trigger, the precise relation, and what becomes newly visible.
Do not turn analogy into etymology, recurrence into identity, or a wider image
into the focus word's literal sense.

## Global responsibility

Review every supplied regular and wide reader walk, retrospective surprise,
cross-run publication finding, assigned global HFT record, and per-ayah wider
connection row. The connection registry includes cross-surah targets and any
same-surah target beyond the declared pericope. Distinguish what the ayah can
yield alone from what later or wider context activates, sharpens, weakens, or
revises. A retrospective surprise
is especially valuable when its later trigger and its return path into this
ayah are explicit.

Use `primary_floor` as the supplied plain propositional `isolated_before`
footing. It is not a verdict: preserve what it plainly says while freely
recasting it into natural Turkish.

The connection rows carry prior attention labels such as `strong`, `medium`,
`weak`, or `no value`. Those labels are not verdicts and must not govern your
decision. Reassess every row. Exact target Arabic is supplied in
`target_evidence`, but target morphology and lexical analysis are not; do not
invent those missing details or a lexical identity beyond what the Arabic and
the stated relation establish.

Some connection rows have `origin: "derived_reciprocal_seed"`. They exist
because the target ayah's own mapping meaningfully linked back to this focus
ayah while this focus mapping omitted the reverse edge. Its `origin_note` and
`origin_label` are nomination evidence from the opposite direction—not a
verdict and not proof that the relation works identically in reverse. Reassess
the return path from this focus ayah using the exact supplied target Arabic.
Preserve a real reverse discovery with an appropriate boundary; reject it only
when a specific edge fails. Authored rows may also carry
`reciprocal_evidence`, including same-surah evidence beyond the pericope, which
exposes the other direction without replacing either authored judgment.

The supplied candidates are a review docket, not an accepted list and not a
quota. Review every candidate and the underlying wider evidence. You may recover
a missed finding when that evidence supports a materially distinct change in
the ayah's reading.

The packet's `hft_evidence.assigned_records` contain HFT nominations with a
wider-than-pericope anchor and individually split HFT reader-synthesis items;
each is a mandatory-review candidate with no presumptive outcome. Its exact raw
payload and exact available anchor Arabic are supplied by its sole `support_id`.
Review every one. Source binding, packet scope, confidence, or a missing
independent branch registry may limit certainty, but may never decide the
outcome. Exact Arabic verifies surface contact only; HFT-stated segmentation,
word indices, roots, branches, and roles remain attributed nominations unless
independently supplied. Treat unanchored synthesis as an inventory item to
trace, decompose, represent, refer, or reject—not as an acceptable surah thesis.
If you accept, narrow, refer, or represent an HFT item as an exact duplicate,
carry its support ID and preserve its source containment, live alternatives,
analogy limits, and any “not a lexical gloss” boundary. A duplicate target must
preserve the evidence union.

Do not search only for confirmation of supplied candidates. Independently scan
every wider-reading record for uncandidate discoveries and record every
meaningful contact opportunity. For every cited branch, explain the distinctive
facet that matters; a branch ID or generic gloss alone is false coverage.

Use the complete focus-branch atlas, not only candidate-cited branches. Silently
scan every atlas branch and every one of its supplied facets against the wider
records and supplied connections. A multi-facet branch is not reviewed by
choosing one representative facet. Record `atlas_facets_tested[]` for every
branch with a plausible wider contact or an existing citation, listing all
tested facet IDs, result, and any contact refs. The facet statements stay in the
packet and need not be copied into the response. Emit findings only for real
contacts; do not enumerate branch-by-branch combinations.

Some nominated branches supply their semantic facet as `image_ar`, `image_en`,
`branch_image_ar`, or `what_is_ar` rather than a numbered concept-map facet.
Treat that supplied image as the facet; identify it by its source field (or use
`facet_id: null`) without inventing a facet ID.

Every accepted finding must re-enter through a word, relation, or act already
present in the focus ayah. Reader agreement is not authority; an outlier is not
valuable merely because it is surprising. Provenance qualifications govern
`epistemic_status` and containment, not visibility. They do not override a
grounded return path, and they are not independent evidence that a reading is
false.

Reject only when you can name the failed edge: no ayah-local return path, no
wider trigger stated in the supplied record, no claimed relation, no changed
reading or payoff, an uncontained thesis, or an exact duplicate. Missing target
morphology is not by itself a rejection reason when the finding stays
within the exact supplied Arabic and relation stated by the note. Different or
countervailing wider discoveries remain eligible.
For a duplicate, name the accepted target, explicitly show that local anchor,
mechanism, direction, and reader payoff are all the same, and preserve the
union of its evidence. Merely saying that it is already represented is
insufficient. Canonical status, source count, confidence labels, vividness, or
anticipated prose length never decides.
Scope overreach justifies rejection only when no bounded global core survives;
otherwise narrow the claim or issue a `scope_referral`.

Do not write a surah thesis and do not write the commentary yet. Acceptance
must be settled before prose facility can influence it.

## Required response

Return one JSON object with:

- `schema_version: "commentary-v3-scope-review-v1"`;
- `identity` containing `ayah_ref: "@@AYAH_REF@@"`, `lane: "global"`,
  `lane_packet_sha256: "@@LANE_PACKET_SHA256@@"`, and
  `authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`;
- `ayah_ref: "@@AYAH_REF@@"` and `lane: "global"`;
- `coverage_complete`, true only after every supplied candidate, every assigned
  HFT record, and every supplied wider-reading record is reviewed;
- `support_coverage[]`, one row per supplied non-HFT wider-reading support
  record, with
  its exact `support_id`, `result` (`accepted`, `narrowed`, `represented`, or
  `rejected`), related `finding_refs`, and concise `reason`;
- `connection_coverage[]`, one row per supplied connection, with
  `connection_ref`, `target_ref`, `result` (`accepted`, `narrowed`,
  `represented`, or `rejected`), related `finding_refs`, and a specific reason
  independent of the prior label;
- `atlas_facets_tested[]` as defined above, so a cited or plausible branch cannot
  hide behind a generic gloss or one representative facet;
- `contact_opportunities[]`, one row per meaningful wider contact, with stable
  `contact_ref`, `focus_carrier`, `wider_trigger`, `relation`,
  `isolated_before`, `wider_after`, `reader_payoff`, `containment`, complete
  `support_ids`, complete `branch_refs`, complete `connection_refs`, and any
  `cross_root_boundary` needed to prevent analogy from being mistaken for
  lexical identity;
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
  `contact_refs`/`connection_refs`; put the finding content and evidence only in
  `accepted_findings`;
- `accepted_findings[]`, one row for every accepted existing or new finding,
  with `finding_ref`, complete `candidate_ids`, complete `proposal_keys`,
  `title`, `isolated_before`, `wider_after`, `wider_trigger`, `claim`,
  `mechanism`, `reader_payoff`, `containment`, complete `support_ids`,
  `branch_refs`, `connection_refs`, `contact_refs`, and `branch_contributions`, and
  `epistemic_status`. Each branch contribution must state the distinctive facet,
  carrier, independent anchor, actual contribution, and boundary;
- `friction_notes[]` for live ambiguity, evidence gaps, source qualification,
  scope referrals, or decisions a reconciler should inspect.

Every supplied candidate must receive exactly one decision. Every accepted or
narrowed candidate must appear in `accepted_findings`. Referred and rejected
material remains visible in the decision ledger. Do not rank accepted findings.
Every assigned HFT record is already one supplied candidate; qualified metadata
cannot erase it.
An accepted finding cites only the support, branches, and connections its final
claim actually uses. When narrowing drops an original branch, record it in the
owning candidate decision's `excluded_branch_refs` and
`branch_exclusion_reasons`; do not preserve discarded branches as false semantic
coverage. Every `scope_referral` disposition must have one stable payload in
`scope_referrals`.
Semantic completeness matters more than cosmetic JSON regularity; never omit a
reading merely to simplify the response envelope.

After returning the decision ledger, remain in this same conversation. A later
follow-up will supply the reconciled, locked global set for prose preparation.

<global_evidence_packet_json>
@@LANE_PACKET_JSON@@
</global_evidence_packet_json>
