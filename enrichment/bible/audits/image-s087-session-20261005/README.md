# S87 Sol image authors — accepted pilot

All 18 original r13 image sections were accepted and assembled on 2026-10-05.
One Sol max agent worked on each image, with all 18 launched in parallel. Each
completed one successful native turn; no failed attempts or resumes were needed.
The input was the original completed image commentary, under the
[saved Bible decision](../../DECISIONS.md).

- 346 annotations cover all 73 base paragraphs; the original commentary is preserved.
- 3,703 judgments cover all 3,523 image discovery connections and 180 additional
  research/context decisions.
- Judgment counts: 1,220 accepted, 2,075 rejected, 383 unavailable and 25 unresolved.
- The frozen source snapshot supplied 1,605 distinct candidate references locally;
  282 distinct candidate references were unavailable. No network source expansion
  was attempted. Repeated references across images retain independent judgments.
- Every image passed native model/effort, tool-use, frozen-input, paragraph-scope,
  candidate/gap-coverage and actual opened-source checks before assembly. The
  combined page passed with no warnings and no base-commentary errata.
- The parent read all final annotation explanations and reviewed 278 tagged
  quotations. Ten presentation differences omit only Hebrew cantillation/meteg
  or Greek apparatus marks. Five editorial corrections were made by the original
  authors during their active turns, including an exact WLC spelling correction.
  Their native edits and source checks are retained.

Read [the accepted page](accepted/surah.ehlikitap.md), [result counts](result.json),
[quotation review](quotation-review.json) and [editorial review](editorial-review.json).
The accepted directory also contains annotation, verdict, gap, ID-map, validation
and page-provenance snapshots. Missing sources and unresolved judgments remain
explicit; the result does not claim exhaustive coverage of unavailable works.
Full candidate coverage and opened-source evidence were checked mechanically;
the parent's semantic review of rejected verdicts was sampled.

`evidence.tar.gz` preserves every image's frozen inputs, native events, raw tool
calls, outputs and immutable acceptance log, plus assembly evidence and reviews.
It includes all 38 selected S87 discovery handoffs and their metadata, the launch
record, operator review scripts, workflow snapshots and the successful 79-test
record. The original Luna/Terra sessions and approved locator repairs remain in
the linked [discovery audit](../s087-prepared-20261005/README.md).

The Bible audit now recognizes narrowly scoped print-only preview ranges, text
searches and trailing-line reads of an author's own files. One status acknowledgment
to the parent is retained with an exact native-call hash and operator review;
its encrypted native body remains marked, and it supplies no source evidence.
These operational exceptions do not permit consulting another image author.

[The manifest](evidence-manifest.json) records archive-member and accepted-file
SHA256 hashes. Every accepted image artifact was checked against its immutable
log, and every compressed member was reread and checked. Extract into a new
review directory; preserve the original runtime and archive files.

Validation: `python3 -B -m unittest enrichment.bible.test_image_enrich` passed all
79 distinct tests, including the 65 inherited Bible workflow tests.

S87 ayah discovery is merged, but ayah page authorship is separate. This pilot
has not been published to the reader.
