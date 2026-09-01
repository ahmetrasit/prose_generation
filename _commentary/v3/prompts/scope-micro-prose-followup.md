The reconciled finding set for your micro lane is now locked. Continue as the
same micro agent. Do not reopen acceptance decisions, add findings, or drop a
locked finding.

Prepare prose-ready Turkish movements for the final writer. Begin from what the
ayah plainly says and show how its words, meaningful morphemes, syntax, form,
sound when evidenced, and local lexical pressures build that act. Account for
every locked micro finding and the reconciled surface-word coverage, but group
supportive details when they perform the same work. Do not produce a serial
word catalogue or a complete final commentary.

Use fluent, contemporary Turkish for a regular reader. Give a concrete effect
before a linguistic term. Teach a secondary meaning from the local translated
sense into the grounded added pressure and its reader payoff. Keep the primary
reading reachable. Suppress candidate IDs and workflow language inside
`draft_prose`; retain them only in the accompanying maps.

When you use Arabic or transliteration, preserve the supplied values but render
them in the canonical single-span syntax with a natural local Turkish gloss.
Never copy raw upstream wrappers or internal analysis/QAC coordinates into
reader prose.

Do not replace a vivid branch image with a generic abstraction. Render its
distinctive facet—what is physically, spatially, socially, or perceptually
happening—and then state the changed reading. Exploratory status requires a
natural boundary, not silence or vague wording. Do not compress away a small but
distinct surprise because a larger finding is easier to explain.

For every cited HFT support, preserve the raw payload's containment, live
alternative, analogy or cross-root limit, and any warning that the image is not
a lexical gloss. The attached anchor Arabic verifies surface contact; it does
not independently verify HFT-attributed morphology, roots, branches, word
indices, or roles. Render these boundaries naturally in Turkish, but do not
drop them during prose preparation.

Return one JSON object with `schema_version:
"commentary-v3-scope-prose-draft-v1"`; `identity` containing
`ayah_ref: "@@AYAH_REF@@"`, `lane: "micro"`,
`reconciled_sha256: "@@RECONCILED_SHA256@@"`, and
`authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`; the same top-level
ayah reference and lane; `coverage_complete`; `movements[]` (`movement_key`,
`draft_prose`, and `finding_refs`); `finding_landings[]` (one per locked
finding, with `finding_ref` and `movement_key`); and `friction_notes[]`. Several findings may share a movement when
their mechanisms and reader payoffs genuinely belong together.

In both `movements[].finding_refs` and
`finding_landings[].finding_ref`, copy only the exact
`locked_findings[].locked_finding_ref` values from the prose-context packet.
`member_finding_records[].finding_ref` values are provenance only. Never use a
member ref in those accounting fields, and never derive a locked ref by adding
a prefix.

The prose-context packet repeats the locked set together with the reconciled
surface/branch coverage, relevant friction, exact focus surface, and only the
evidence records cited by those findings. Use it to preserve small linguistic
details even if this follow-up is delivered in a fresh invocation. It does not
authorize new findings or reopened decisions.

`member_finding_records` preserves each originating accepted finding verbatim;
the consolidated locked wording organizes those records but never replaces or
genericizes their carrier, mechanism, payoff, containment, or epistemic status.
`resolved_referrals` and `originating_referral_records` may carry evidence that
exists only in another lane. Its complete originating candidate, raw support,
branch/facets, connection, and contact records are included in the corresponding
`cited_*_records`; use them as first-class evidence even when their refs are
absent from the locked finding's top-level unions.

<micro_prose_context_json>
@@LANE_PROSE_CONTEXT_JSON@@
</micro_prose_context_json>
