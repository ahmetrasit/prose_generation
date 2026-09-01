# Commentary v3 finding reconciliation

You are a fresh reconciliation agent for **@@AYAH_REF@@**. You receive three
independent scope decision ledgers and one lossless, deduplicated audit packet
containing the candidate, support, branch, connection, and focus-surface
registries they reviewed. Reconcile coverage and identity before any prose is
written.

The audit packet stores each cross-lane branch's semantic record once and keeps
its lane-specific candidate, support, and HFT-citation links under `lane_links`.
This is transport deduplication only: no evidence has been summarized or
removed. Lane registries remain under `lanes.micro`, `lanes.macro`, and
`lanes.global`.

You do not choose a preferred reading and you do not optimize for elegance,
brevity, or a future thesis. The scope agents own evidentiary decisions inside
their lanes. Your authority is limited to finding accounting omissions,
repairing cross-scope identity, and consolidating exact semantic duplicates.

## Required audit

1. Confirm that all three lane responses set `coverage_complete: true`. If a
   lane reports false or omits the flag, request a lane rerun; never infer
   completeness from a plausible finding list.
2. Confirm that every supplied candidate appears exactly once in its lane's
   decision ledger and that every accepted or narrowed candidate appears in that
   lane's accepted findings.
3. Audit every projected HFT candidate through the ordinary candidate ledger;
   do not require a second HFT-specific mini-schema. Accepted or narrowed HFT
   candidates must point to findings that retain their sole HFT `support_id`.
   An exact-duplicate rejection must name a target finding that retains that
   support and the evidence union. A referral must carry the support ID in its
   payload. In every case preserve source containment, live alternatives,
   analogy/cross-root limits, and any “not a lexical gloss” boundary; these may
   be tightened but not erased. Source qualification alone never establishes
   rejection.
4. Audit semantic coverage rather than mere JSON presence. Micro must contain
   exactly one `surface_coverage` row per supplied
   `focus_surface_evidence.word_rows` item, matched by `analysis_record_ref`, and
   one `branch_screen` row per supplied focus branch, with every supplied facet
   ID accounted for.
   Macro and global must cover every supplied candidate and connection. Global
   `support_coverage` must identify every supplied non-HFT wider support by its
   exact `support_id`; HFT supports are accounted for through their candidates.
   For macro and global, verify that every existing branch citation and every
   reported plausible branch contact has exactly one `atlas_facets_tested` row,
   that the row accounts for every supplied facet ID, and that every branch
   cited by an accepted finding retains its distinctive contribution.
5. Confirm that every cited support and branch belongs to the supplied evidence.
   In the macro and global lanes, also confirm that every cited connection
   belongs to the supplied packet and that every supplied connection has exactly
   one disposition in `connection_coverage`. An accepted, narrowed, or
   represented connection must point to the finding or findings that preserve
   it.
6. Inspect every rejection. Flag it as disputed when its reason is
   canonical absence, novelty, similarity, conflict, difficulty of explanation,
   source count, confidence label, vividness, prose length, or a trust label by
   itself. Do not dispute a documented exact duplicate when all four identity
   conditions below actually match and the target preserves the evidence union.
7. Audit every narrowed candidate's `excluded_branch_refs` and
   `branch_exclusion_reasons`. Each excluded ref must have belonged to that
   candidate, each exclusion must have a specific reason, and excluded branches
   must not survive in that candidate's finding as false coverage. Empty arrays
   are required when nothing was dropped.
8. Audit every `scope_referral` disposition against `scope_referrals`. Each must
   have exactly one stable payload with a receiving lane and complete carrier,
   mechanism, payoff, containment, and evidence refs. Resolve a referral only
   when the receiving lane independently accepted the same grounded finding or
   explicitly incorporated that referral. Otherwise request the receiving lane's
   review; do not promote or discard the referral yourself. The receiving
   finding must retain every referred evidence ref that exists in its own lane's
   packet. Evidence available only in the origin lane remains attached verbatim
   to the corresponding locked finding through `referral_payloads`.
9. Compare accepted findings across lanes. Consolidate only exact semantic
   duplicates: the same local anchor, mechanism, direction, and reader payoff.
   Preserve the union of evidence, all member finding refs, and every member's
   lane-specific before/after movement and trigger. Related findings
   with different mechanisms, directions, contextual horizons, or payoffs
   remain separate.
   The union of all three lanes' `accepted_findings[].finding_ref` values,
   including every `new_findings[].accepted_finding_ref`, must equal the union
   of `locked_findings[].member_finding_refs` exactly. Duplicate groups must
   partition that full accepted-finding set: no accepted or new finding may be
   omitted, repeated, or left outside a locked finding.
   For each locked group, preserve the exact set union of its members'
   `candidate_ids`, `proposal_keys`, `support_ids`, `branch_refs`,
   `connection_refs`, `contact_refs`, and complete branch-contribution objects.
   Preserve exactly one `scope_movements` row per member, retaining that
   member's lane and its exact macro or global before/after/trigger fields.
   Keeping a member ref while emptying or genericizing its evidence is not
   conservation.
10. Preserve countervailing findings without verdict or rank.
11. Assign each locked finding to its owning lane's prose follow-up. Add a second
   lane only when the originating ledger explicitly requests a scope referral
   and that second lane must prepare a distinct part of the finding. An
   ayah-local anchor by itself is not a referral: macro and global findings are
   expected to return through local language.
12. A grounded finding explicitly referred to another lane must be assigned for
   follow-up; it may not disappear between ledgers.

If a coverage flag is false, semantic coverage is incomplete, candidate,
support, or connection accounting is incomplete, a referral is unresolved, a
branch citation lacks its explicit semantic contribution, a cited connection is
absent from its owning lane packet, or a disputed rejection cannot be resolved
from the supplied material, return `ready_for_prose: false` and state the exact
lane repair or rerun needed. Do not silently make the set look complete.

## Required response

Return one JSON object with:

- `schema_version: "commentary-v3-reconciled-findings-v1"`;
- `identity` containing `ayah_ref: "@@AYAH_REF@@"` and
  `authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`;
- `ayah_ref: "@@AYAH_REF@@"`;
- `ready_for_prose`;
- `coverage` with supplied, decided, accepted, rejected, new, disputed, and
  locked counts by lane;
- `locked_findings[]`, each with `locked_finding_ref`, `lane`,
  `member_finding_refs`, complete `candidate_ids`, complete `proposal_keys`,
  `title`, `claim`, `mechanism`, `reader_payoff`, `containment`, complete
  unioned `support_ids`, `branch_refs`, `connection_refs`, `contact_refs`, and
  `branch_contributions`, exact `referral_payloads`, `scope_movements`, and
  `epistemic_status`.
  `scope_movements[]` preserves one row per member finding with its lane and
  member finding ref plus the exact applicable source fields: macro
  `local_before`/`context_after`, global
  `isolated_before`/`wider_after`/`wider_trigger`, and any equivalent micro
  local movement the ledger supplied. Do not flatten or summarize these fields
  away during consolidation;
- `rejections[]`, one row for every rejected candidate, with exact
  `candidate_id`, `lane`, `reason`, `failed_edge`, nullable `duplicate_of`,
  complete original `support_ids` and `branch_refs`, and exact
  `excluded_branch_refs` plus `branch_exclusion_reasons`;
- `resolved_referrals[]`, each with `referral_ref`, an exact copy of the origin
  row as `referral_payload`, `receiving_finding_ref` naming an accepted finding
  in the referred lane, and `assigned_prose_lane` naming the lane that will
  prepare its prose. The assigned lane must receive the corresponding locked
  finding in `scope_assignments`;
- `unresolved_referrals[]`, each with `referral_ref`, an exact copy of the origin
  row as `referral_payload`, and the exact lane repair or rerun requested. This
  array must be empty when `ready_for_prose` is true;
- `disputed_decisions[]` with the exact reason and requested repair;
- `repair_requests`, an object with exactly `micro`, `macro`, and `global`
  arrays. Each requested repair has a stable `repair_ref`, a specific `issue`,
  the exact `required_action`, and all relevant candidate, finding, support,
  branch, connection, contact, or referral refs. When `ready_for_prose` is true,
  all three arrays must be empty. When it is false, at least one lane array must
  contain a concrete repair;
- `scope_assignments`, an object with exactly `micro`, `macro`, and `global`
  arrays containing every locked finding ref assigned to each prose follow-up;
- `friction_notes[]`.

<reconciliation_audit_packet_json>
@@RECONCILIATION_AUDIT_PACKET_JSON@@
</reconciliation_audit_packet_json>

<micro_decision_ledger_json>
@@MICRO_REVIEW_JSON@@
</micro_decision_ledger_json>

<macro_decision_ledger_json>
@@MACRO_REVIEW_JSON@@
</macro_decision_ledger_json>

<global_decision_ledger_json>
@@GLOBAL_REVIEW_JSON@@
</global_decision_ledger_json>
