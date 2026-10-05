# S1 Bible discovery pilot — 2026-10-05

All seven ayat and all fourteen surah image sections completed independent Luna max and Terra max discovery: **42 native sessions, 84 completed turns**. Each fixed follow-up ran in its original session. The user explicitly authorized parallel execution of all readers.

The final merge passed for every target, producing seven ayah handoffs and one whole-surah handoff (plus the fourteen section handoffs). No page author or prefetch was started. All implementation and saved audit files are confined to `enrichment/bible/`.

## Results

| Scope | References grouped within each target | Distinct connections |
|---|---:|---:|
| 1:1 | 187 | 226 |
| 1:2 | 183 | 228 |
| 1:3 | 274 | 349 |
| 1:4 | 169 | 208 |
| 1:5 | 169 | 209 |
| 1:6 | 142 | 187 |
| 1:7 | 144 | 173 |
| sec1 | 201 | 262 |
| sec2 | 181 | 221 |
| sec3 | 166 | 223 |
| sec4 | 197 | 247 |
| sec5 | 293 | 354 |
| sec6 | 352 | 433 |
| sec7 | 201 | 259 |
| sec8 | 128 | 165 |
| sec9 | 231 | 291 |
| sec10 | 143 | 175 |
| sec11 | 185 | 232 |
| sec12 | 165 | 204 |
| sec13 | 242 | 296 |
| sec14 | 385 | 455 |

The readers produced 3,604 initial rows and 1,795 follow-up proposals. Consolidation removed only 2 exact repeated connections and retained **5,397 distinct connections**: 1,580 across the seven ayah pages and 3,817 across the fourteen image sections. Different reasons for the same passage remain distinct. References and connections repeated across different targets are intentionally counted in each target.

## Findings and repairs

- 585 unresolved-text findings: named works/citations still need source resolution; this is a row count, not 585 distinct unavailable works.
- 82 original-language wording-review findings: check roots, forms, editions and verse boundaries during verification.
- 36 recorded book-name/abbreviation resolutions; edition and verse numbers were unchanged.
- 13 approved first-pass corrections and 15 separately approved follow-up corrections. Original rows, failures, grades and explanations are preserved. Two follow-up column transpositions and one edition-derived tradition-label correction are explicit.
- 29 recoverable tool diagnostic entries remain in the report. No model, input, retrieval or follow-up protocol violations were found in the inspected calls.
- Every nonblank prompt/package line was found in the first-turn tool outputs, including reread chunks after truncation.
- Grades are unverified reader labels: 4,330 strong, 1,039 medium and 28 weak. Agreement or a strong label does not verify a connection.

## Review files

- [Full report](report.md) and [structured report](report.json): every finding, count, diagnostic, repeat and repair.
- [Reader completion notes](reader-notes.json): all 84 completion notices and the readers' accuracy caveats.
- [First-pass proposal](first-turn-repairs.proposed.md) and [approval records](first-turn-repairs.accepted.json).
- [Follow-up proposal](followup-repairs.proposed.md) and [approval records](followup-repairs.accepted.json).
- [Input coverage](input-coverage.json), [audit attestations](reader-audit.json) and [run scope](run-scope.json).
- `readers/`: preserved native first/follow-up TSVs, consolidated lists, logs and repair records. Some raw TSVs intentionally remain invalid; use the accepted records and consolidated lists for the validated interpretation.
- `merged/`: grouped handoffs preserving every connection and its provenance.

Native event transcripts and tool outputs remain in the ignored runtime attempt. This versioned bundle is a review archive, not a replacement for the complete local native evidence required by the merge verifier. Its manifest verifies the saved copies.

## Validation and next stage

All 65 offline tests passed. All 24 Python files parsed; no shared enrichment/v16 helper imports were found. The live report reverified all 42 completed artifact chains. All seven ayah handoffs and the complete surah handoff passed provenance verification.

Next: prefetch named sources, rebuild the Bible-only index, and then run the single verifier/author for each whole page when authorized. It must open the actual Hebrew WLC or Greek SBLGNT passages, check each proposed connection, and record accepted/rejected/unresolved/unavailable verdicts. Wisdom candidates are named-work pointers with a missing original Greek witness; the KJV finding aid never substitutes for original-language evidence. The remaining coverage gaps for full Septuagint, Peshitta and patristic collections remain explicit.
