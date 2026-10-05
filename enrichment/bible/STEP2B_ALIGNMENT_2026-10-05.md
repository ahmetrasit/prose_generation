# Bible discovery: selective v16 Step 2b alignment

The user approved adopting the updated discovery operations while retaining the
Bible pathway's original-language research and page structure. All implementation
changes are confined to `enrichment/bible/`. The reference workflow is
`_commentary/v16/RUNBOOK.md`, Step 2b; no shared workflow helper is imported or edited.

## Resulting workflow

1. Freeze the completed augment9 commentary in the Bible pack. For one ayah, both
   discovery readers receive the whole ayah commentary, its Arabic, the whole
   surah's Arabic and the word/root/branch labels associated with that ayah in the
   frozen surah commentary. Surah discovery continues to use individual images.
2. Independently run the configured native Luna and Terra readers at max, each in
   a fresh context. Each has exactly one fixed follow-up in the same session.
   The updated brief works through all developed details, including secondary
   senses and contrary readings, and requires concrete, contextual connections.
3. Preserve first-turn bytes and raw follow-up proposals. Consolidate exact
   repeated connections without changing the retained grade or explanation.
   Record each repeat's retained occurrence. Keep different reasons and kinds for
   the same verse visible in the verifier's handoff.
4. Check structural references and locally review Hebrew/Greek wording, WLC
   variant readings and verse boundaries. Surface findings and all diagnostics.
   These checks do not establish relevance, meaning or historical influence.
5. Require both completed, audited readers before merging. Hashes cover input
   packages, raw proposals, native evidence, tool audits and validation. A narrow
   repair process preserves malformed raw proposals and the failed run; explicit
   approval of a displayed reference correction produces a separate accepted
   version. It cannot repair protocol failures or change reader judgements.
6. Explicitly select completed attempts, prefetch the candidate texts, and build
   the independent index. Each handoff groups references while carrying stable
   IDs for every distinct connection, reader evidence and review findings.
7. One page author verifies the candidates in Hebrew WLC / Greek SBLGNT and other
   available witnesses, and does its own research across every paragraph. Every
   connection gets an accepted/rejected/unresolved/unavailable verdict. Additional
   `get` lookups, including neighbours and missing passages, get research verdicts.
8. Acceptance checks that evidence was actually displayed by corpus `get`, every
   discovered connection and lookup was judged, accepted verdicts reference kept
   annotations at valid paragraphs, and unavailable/unresolved material appears
   in gaps. Accepted annotations, verdicts, gaps and the coverage report have
   immutable snapshots. The frozen commentary remains unchanged.

## Operational choices retained

- One author per whole ayah/page; no adoption of v16's separate section writers.
- Hebrew/Greek search, source editions, witness metadata, ketiv/qere separation,
  dating and relationship safeguards remain intact. Search is still normalized
  prefix search, not morphological analysis.
- A reference may have several distinct connections. A first occurrence is a
  consolidation rule, not a judgement of truth or relevance.
- Seven discovery agents at once by default; another workflow's scoped exception
  does not authorize broader Bible concurrency. A discovery run does not launch
  the page author. Scripts prepare, inspect and validate; they never call models.
- Historical runs cannot be silently converted to the new protocol. Prepared
  packages and local outputs remain under Bible-owned ignored runtime directories.

## Verification and remaining work

All **54 offline Bible regression tests pass**, including a mocked complete native
CLI lifecycle, missing readers, raw-artifact changes, explicit mixed-attempt
selection, repeat preservation, Hebrew/Greek wording and qere findings, recorded
repairs, verdict completeness, actual lookup evidence, source gaps, dropped
annotation links and immutable accepted evidence. All 23 Bible Python modules
parse and import no shared workflow helpers. Git whitespace checks pass.

Two fresh ayah 1:1 discovery packages were prepared with the updated prompt and 13
lexical members. Their frozen input hashes match; neither session started. The
report correctly fails readiness for incomplete discovery, and page preflight
correctly reports no selected completed discovery. No model calls, downloads,
source/index rebuilds, production annotations or publication occurred.

The live ayah pilot remains necessary before rollout: confirm the configured
native readers are available, complete both rounds, inspect the full reports,
prefetch and verify evidence, then review one authored page for accuracy,
coverage, Turkish prose and placement. Structural completeness and original-text
access do not by themselves establish the quality of the Bible connections.
