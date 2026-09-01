# Commentary v3 scope prose accounting repair

Continue in the same **@@LANE@@** scope conversation for **@@AYAH_REF@@**. A
deterministic check found the accounting or prompt-binding defect below. Return
one complete replacement scope-prose JSON object, not a patch.

This is an accounting-only repair. Preserve, byte for byte, every prior
`draft_prose`, every `movement_key`, their order, all other non-reference
movement fields, and the complete `friction_notes` value. Do not shorten,
paraphrase, merge, delete, reorder, or add prose movements. Do not reopen
finding decisions. Correct only schema/identity binding, `finding_refs`,
`finding_landings`, or other accounting named by the defect. Code will reject
the response if semantic content changes.

Use `schema_version: "commentary-v3-scope-prose-draft-v1"`. Its identity must
contain `ayah_ref: "@@AYAH_REF@@"`, `lane: "@@LANE@@"`,
`reconciled_sha256: "@@RECONCILED_SHA256@@"`, and
`authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`. The repair request
hash supersedes the prior request hash.

For `movements[].finding_refs` and `finding_landings[].finding_ref`, use only
the exact `locked_finding_ref` strings in the explicit map below. Member refs
are provenance only. Never derive, normalize, or manufacture a locked ref by
prefixing a member ref. Preserve the prior movement-to-finding relationship
while replacing mistaken member refs with their explicitly mapped locked refs.
Every assigned locked finding must land exactly once, and that landing must
point to a movement citing it.

<validation_issue_json>
@@VALIDATION_ISSUE_JSON@@
</validation_issue_json>

<locked_ref_map_json>
@@LOCKED_REF_MAP_JSON@@
</locked_ref_map_json>

<prior_scope_prose_draft_json>
@@PRIOR_PROSE_DRAFT_JSON@@
</prior_scope_prose_draft_json>
