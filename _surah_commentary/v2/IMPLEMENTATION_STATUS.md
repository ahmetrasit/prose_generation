# Editorial-Only Workflow Status

Updated 2026-09-11. The active entry point is `scripts/workflow.py` and its
contract is `ORCHESTRATION.md`.

The sole semantic source is the completed final editorial prose for every
numbered ayah in one selected v5 analysis. The workflow freezes those texts,
derives an anchored outline, composes and edits the prelude/postlude, validates
coverage, and publishes an explicitly approved revision. No upstream discovery,
scope ledgers, invitations, independent primary floor, or network sources enter
the active prompts.

The old channel-first workflow and its implementation status are preserved as
legacy material. Its tests establish historical compatibility, not acceptance
of the new prose workflow. The new workflow has separate regression tests in
`tests/test_surah_editorial_workflow.py`.

## Verification

- 45 tests pass across the new editorial workflow, legacy channel workflow,
  and reused v5 prose validator. Eleven tests cover the new workflow.
- Coverage includes editorial-only inputs, missing/extra ayahs, immutable
  snapshots, source and prose anchors, phase/approval gates, preserved accepted
  inputs, stable replacement, revision history, idempotence, and rollback.
- A read-only S1 preflight loaded and validated all seven saved editorials from
  `s001-fresh-20260910` and assembled the outline prompt. The editorial snapshot
  contained 616,901 UTF-8 bytes; the generated prompt contained 623,715 bytes.
  These are byte counts, not token estimates. Nothing was published or sent to
  a semantic agent, and the preflight does not attest that live agents finished.
- All JSON schemas parse, and `git diff --check` passes.
- Legacy semantic prompts and scripts are unchanged; only their workflow-root
  path had been updated for the earlier directory move.

A full semantic run remains a separate operation: fresh outline and composition
agents must execute the generated prompts, and a reviewer must approve the
actual prose. Mechanical tests and S1 source-snapshot checks do not substitute
for that acceptance.
