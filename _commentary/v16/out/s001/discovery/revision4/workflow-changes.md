# Revision4 workflow changes

User authorization: rerun image 5 and all unfinished S1 images after required workflow/runbook fixes. Images 1–3 retain completed revision3 results. Images 4–14 get fresh Luna/Terra sessions; all earlier artifacts remain intact. No earlier partial output or proposed repair is promoted.

Follow-up proposals now go to a separate file, with no file reads, retrieval, scripts or other-agent consultation. The finish step validates every raw row and appends each new reference once. The first occurrence wins without changing any grade or explanation. Repeated proposals and their provenance remain in consolidation.json; raw followup.tsv remains intact. This is a declared protocol change, not a retrospective repair of revision3.

Snapshot now rejects invalid or duplicate initial rows. Finish rejects malformed/missing follow-up proposals or a changed initial list. Merge checks finished-list and raw-proposal hashes, and checks source agreement before writing merged output. Plaintext follow-up delivery mismatches fail. Failed tool operations are included in diagnostic review.

Runbook now distinguishes structural/provenance failure from reported accuracy findings, recognizes existing rerun authorization, and documents fresh-attempt selection and deterministic proposal consolidation.

Seven regression checks pass, including duplicate follow-up proposals, preservation of original rows/grades/raw proposals, missing/malformed output and empty follow-ups. Accuracy and relevance still require review; repeated-reference handling does not validate meaning. No Opus run is authorized.
