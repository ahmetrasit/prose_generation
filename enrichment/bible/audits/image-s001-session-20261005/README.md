# S1 Sol image authors — completed pilot

All 14 original r13 image sections were accepted and assembled on 2026-10-05:

- 340 annotations across 73 base paragraphs; the original commentary is preserved.
- 4,030 judgments cover all 3,817 discovery connections and 213 additional research/context decisions.
- Judgment counts: 1,084 accepted, 2,552 rejected, 390 unavailable and 4 unresolved.
- Every image passed native model/effort, tool-use, frozen-input, paragraph-scope,
  candidate/gap-coverage and actual opened-source checks before assembly.
- The source snapshot supplied 1,916 distinct candidate references locally;
  313 distinct candidate references were unavailable. This pilot did not fetch
  sources over the network. Unavailable and unresolved judgments remain visible.
- The final quotation review covered 286 tagged Hebrew/Greek quotations. Three
  text-match differences were reviewed as omitted apparatus/cantillation marks.
  One operator spelling correction in section 9 removed an extra yod; the exact
  before/after record and original author file are preserved.

Read [the accepted page](accepted/surah.ehlikitap.md), [result counts](result.json)
and [quotation review](quotation-review.json). The accepted directory includes
the annotation, verdict and gap snapshots, ID map, validation and page provenance.
`evidence.tar.gz` retains each image's frozen inputs, native events, tool calls,
outputs and immutable run log, plus the assembly inputs and evidence. It also
preserves all eight authorized resume records and the section 9 correction.
[The manifest](evidence-manifest.json) lists raw member and accepted-file hashes;
every member was reread and checked after compression. Extract into a new review
directory to inspect it; do not overwrite the original runtime files.

Validation: both Bible test modules passed (77 distinct tests; the inherited
shared workflow tests also ran twice in the combined 142-test invocation).

## Earlier decision checkpoint

This is an in-progress checkpoint, not an accepted Bible page.

- 14 Sol max sessions were launched in parallel for the original r13 images.
- Sections 1–6 were interrupted by the operator after an unnecessary concern about using augmented images.
- The user confirmed that original images are the intended scope and explicitly authorized same-session resumption.
- Sections 7 and 14 encountered model-capacity errors; retry the same requested model.
- Other sections are still running or have returned drafts. Final native evidence and output checks are pending.
- `checkpoint.json` records counts, draft hashes and outstanding tool-audit findings at this checkpoint. It does not certify unfinished results.
- S87 has 74 prepared discovery sessions and is now authorized to start on the same original-image basis. None had started when this checkpoint was made.

See [the decision](../../DECISIONS.md). Preserve all native sessions and earlier work; do not silently replace inputs or discard interruptions.
