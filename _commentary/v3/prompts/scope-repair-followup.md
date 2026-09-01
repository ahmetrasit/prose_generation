# Commentary v3 scope review repair

Continue in the same **@@LANE@@** scope conversation for **@@AYAH_REF@@**.
The reconciliation pass found explicit accounting or analysis gaps. Repair all
listed gaps without becoming more conservative: preserve every prior meaningful
image, tension, ambiguity, and surprise reading unless the repair evidence
shows a specific failed edge. Do not remove a finding merely to simplify the
ledger or satisfy a shape requirement.

Return one complete replacement scope-review JSON object, not a patch. Its
`identity.authoring_request_sha256` must be
`@@AUTHORING_REQUEST_SHA256@@`. Recheck the complete evidence packet and the
complete scope contract below; the word “fresh” in that embedded original
contract describes the scope's independence, not this invocation. This is a
same-agent follow-up.

For a `scope_validation` repair, treat the baseline review embedded in the
repair record as immutable linguistic content. Reconstruct from that semantic
baseline even if the immediately prior review differs from it. Preserve every
pre-existing semantic value verbatim across the whole review: accepted
findings, each branch contribution, contact opportunities, candidate reasons,
coverage and connection explanations, referral content, and friction notes.
Never paraphrase, shorten, translate, genericize, delete, or reassign those
values while repairing structure. Keep each value attached to its original
valid finding, candidate, contact, branch, connection, support, or surface-row
identity, and preserve duplicate rows when they are distinct ledger entries.

Change only the exact structural/accounting paths implicated by the reported
validation class. These may include identity hashes; row IDs and reference
mappings such as `finding_refs` or `accepted_finding_refs`; finding evidence
lists such as `candidate_ids`, `proposal_keys`, `support_ids`, `branch_refs`,
`connection_refs`, and `contact_refs`; a missing structural key such as a
contribution's `branch_ref`; or the coverage-ledger shape described below.
Existing semantic fields inside those rows—including every contribution,
boundary, reason, and existing facet result—remain verbatim. A genuinely
missing row or new per-facet result may be added only when the reported defect
requires it; do not invent unrelated analysis during a validation repair.
The repair record's `scope_validation_exception_paths`, when nonempty, names
only exact identity/reference fields already proven malformed against the
baseline packet, or exact control fields (`decision`, `disposition`, `result`,
and analogous fields) whose repaired direction is mandated by retained
evidence. No other identity or valid control value may change. These exceptions
are not permission to alter the row's explanations or any unrelated occurrence.
Intrinsically malformed aliases, enum values, and ledger shapes may be
normalized while all valid linguistic values remain attached and verbatim.

When a malformed duplicate-ID ledger forces several rows to become one or to
receive corrected IDs, keep one supported primary value and copy every other
distinct supplied linguistic value verbatim into a
`preserved_validation_alternatives` list on the repaired row. The same rule
applies when conflicting facet-result aliases or contribution-field aliases
must choose one primary value. These alternatives remain evidence for
reconciliation and prose; never discard them merely because the accounting
schema permits only one primary value.

Audit the complete response for every instance of the reported error class;
the named row may only be the first fail-fast example. In particular:

- an accepted, narrowed, or represented contact's complete support, branch,
  and connection evidence must survive across its accepted `finding_refs`, and
  each receiving finding must retain the contact ref. A failed attempted edge
  belongs in candidate, branch/facet, or connection coverage, not in
  `contact_opportunities`;
- facet coverage uses `tested_facets` (or its `facets_tested` alias) as a list
  of objects. Each object carries a packet-supplied `facet_id` and exactly one
  result: `contact`, `no_independent_trigger`, or `scope_referral`. Every branch
  contribution carries one packet-supplied `facet_id`, and an accepted
  contribution's corresponding tested result is `contact`. A bare
  `facet_ids_tested` string list does not satisfy this ledger;
- macro and global connection coverage contains exactly one
  `evidence_row_results` row per packet-supplied `connection_evidence_ref`.
  Preserve each row's independent reason and finding refs; the parent result
  and finding refs must be the deterministic aggregate required by the scope
  contract.

<requested_repairs_json>
@@REPAIR_REQUESTS_JSON@@
</requested_repairs_json>

<prior_scope_review_json>
@@PRIOR_REVIEW_JSON@@
</prior_scope_review_json>

<reconciliation_response_json>
@@RECONCILED_JSON@@
</reconciliation_response_json>

<complete_scope_contract>
@@COMPLETE_SCOPE_CONTRACT_MD@@
</complete_scope_contract>
