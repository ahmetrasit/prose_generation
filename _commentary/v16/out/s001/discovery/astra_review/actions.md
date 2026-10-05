# Review dispositions before revision3

Implemented: lossless multiword/source-branch parsing; image-wide recall sweep and secondary-feature grading; bounded append-only follow-up; short remembered quotations or English explanation; explicit native wrapper; durable native start/snapshot/audit/finish; input hashes, session/model/effort, per-turn usage and follow-up delivery evidence; missing-file/blank-note/schema checks; duplicate/partial-run merge rejection; snapshot-based provenance; explicit attempt selection; validated merged TSV; unverified discovery rationales and accuracy flags in the dry handoff; list and source hashes; legacy script calls blocked; corrected runbook.

The discovery runs remain independent: the review's newly identified candidates are not seeded into packages or prompts. Existing prompt examples remain exposed cases. Section1 revision3 is a new prompt-and-packaging attempt, not a controlled prompt-only comparison, because all dictionary branch IDs are now preserved.

Deferred to a separately authorized Opus stage: freeze its execution packet/paragraph metadata and make finish stop on a mismatch instead of merely warning. No Opus execution is authorized in this task. Dry handoff builds validate the explicitly chosen discovery list and its source hash.

Verification: five focused regression tests plus a simulated native two-turn lifecycle (including started guard, first-turn snapshot, valid zero-addition follow-up, delivery proof, and one ledger finish). Historical outputs are untouched.
