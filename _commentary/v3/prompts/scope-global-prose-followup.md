The reconciled finding set for your global lane is now locked. Continue as the
same global agent. Do not reopen acceptance decisions, add findings, or drop a
locked finding.

Prepare prose-ready Turkish movements for the final writer. Render each wider
discovery as reading experience: what the ayah yielded before, what later or
wider context made visible, and how the discovery returns through an existing word,
relation, or act in this ayah. Preserve retrospective triggers and source
qualification without mentioning reader IDs, run labels, confidence counts, or
workflow instruments. Do not turn a wider recurrence into a surah thesis and do
not produce a complete final commentary.

Treat the locked finding's `scope_movements` as lossless discovery source work.
Preserve its `isolated_before`, `wider_after`, and `wider_trigger`; do not
reconstruct a weaker generic movement from the claim alone.

Use fluent, contemporary Turkish for a regular reader. Keep the local meaning
reachable and state the changed understanding. Suppress candidate IDs and
workflow language inside `draft_prose`; retain them only in the accompanying
maps.

When you use Arabic or transliteration, preserve the supplied values but render
them in the canonical single-span syntax with a natural local Turkish gloss.
Never copy raw upstream wrappers or internal analysis/QAC coordinates into
reader prose.

Do not flatten a surprising image or analogy into a general moral. Preserve the
wider trigger, return path, concrete image, and reader payoff. If two roots or
structures are only analogous, say so naturally while still letting the analogy
do its full interpretive work. Exploratory or noncanonical status requires
containment, not omission.

For every cited HFT support, preserve the raw payload's containment, live
alternative, analogy or cross-root limit, and any warning that the image is not
a lexical gloss. The attached anchor Arabic verifies surface contact; it does
not independently verify HFT-attributed morphology, roots, branches, word
indices, or roles. Render these boundaries naturally in Turkish, but do not
drop them during prose preparation.

Return one JSON object with `schema_version:
"commentary-v3-scope-prose-draft-v1"`; `identity` containing
`ayah_ref: "@@AYAH_REF@@"`, `lane: "global"`,
`reconciled_sha256: "@@RECONCILED_SHA256@@"`, and
`authoring_request_sha256: "@@AUTHORING_REQUEST_SHA256@@"`; the same top-level
ayah reference and lane; `coverage_complete`; `movements[]` (`movement_key`,
`draft_prose`, and `finding_refs`); `finding_landings[]` (one per locked
finding, with `finding_ref` and `movement_key`); and `friction_notes[]`. Several findings may share a movement only
when their wider mechanisms and reader payoffs genuinely belong together.

In both `movements[].finding_refs` and
`finding_landings[].finding_ref`, copy only the exact
`locked_findings[].locked_finding_ref` values from the prose-context packet.
`member_finding_records[].finding_ref` values are provenance only. Never use a
member ref in those accounting fields, and never derive a locked ref by adding
a prefix.

The prose-context packet repeats the locked set together with wider-source,
connection, and facet coverage, relevant friction, exact focus surface, and only
the evidence records cited by those findings. Use it to preserve the wider
trigger and return path even if this follow-up is delivered in a fresh
invocation. It does not authorize new findings or reopened decisions.

`member_finding_records` preserves each originating accepted finding verbatim;
the consolidated locked wording organizes those records but never replaces or
genericizes their carrier, mechanism, payoff, containment, or epistemic status.
`resolved_referrals` and `originating_referral_records` may carry evidence that
exists only in another lane. Its complete originating candidate, raw support,
branch/facets, connection, and contact records are included in the corresponding
`cited_*_records`; use them as first-class evidence even when their refs are
absent from the locked finding's top-level unions.

<global_prose_context_json>
@@LANE_PROSE_CONTEXT_JSON@@
</global_prose_context_json>
