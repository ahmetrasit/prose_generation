The reconciled finding set for your macro lane is now locked. Continue as the
same macro agent. Do not reopen acceptance decisions, add findings, or drop a
locked finding.

Prepare prose-ready Turkish movements for the final writer. For every locked
finding, enter through its focus-ayah word or relation, establish the isolated
reading, then show exactly what the declared pericope changes. Preserve the
boundary between a contextual pressure and a lexical meaning. Different or
countervailing changes remain visible together. Do not rewrite the micro
grammar inventory and do not produce a complete final commentary.

Treat the locked finding's `scope_movements` as lossless before/after source
work. Preserve its `local_before` and `context_after`; do not reconstruct a
weaker generic movement from the claim alone.

Use fluent, contemporary Turkish for a regular reader. Render before/after as a
reading experience, not an evidence report. Suppress candidate IDs and workflow
language inside `draft_prose`; retain them only in the accompanying maps.

When you use Arabic or transliteration, preserve the supplied values but render
them in the canonical single-span syntax with a natural local Turkish gloss.
Never copy raw upstream wrappers or internal analysis/QAC coordinates into
reader prose.

Do not reduce a contextual image to a generic theme. Preserve the concrete
scene, the exact focus-to-context contact, and the changed reading. Exploratory
or noncanonical findings remain reader-visible with proportionate boundaries;
their status is not permission to bury them in friction. Do not compress away a
distinct mechanism merely because another finding reaches a related conclusion.

Return one JSON object with `schema_version:
"commentary-v3-scope-prose-draft-v1"`; `identity` containing
`ayah_ref: "@@AYAH_REF@@"`, `lane: "macro"`,
`reconciled_sha256: "@@RECONCILED_SHA256@@"`, and
`authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`; the same top-level
ayah reference and lane; `coverage_complete`; `movements[]` (`movement_key`,
`draft_prose`, and `finding_refs`); `finding_landings[]` (one per locked
finding, with `finding_ref` and `movement_key`); and `friction_notes[]`. Several findings may share a movement only
when their contextual mechanisms and reader payoffs genuinely belong together.

The prose-context packet repeats the locked set together with connection/facet
coverage, relevant friction, exact focus surface, and only the evidence records
cited by those findings. Use it to preserve the concrete before/after mechanism
even if this follow-up is delivered in a fresh invocation. It does not authorize
new findings or reopened decisions.

<macro_prose_context_json>
@@LANE_PROSE_CONTEXT_JSON@@
</macro_prose_context_json>
