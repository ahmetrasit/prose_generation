# v14 source/accounting repeat — 1:6

The same Sol max model can produce exact tagged sources and substantially smaller accounting under the revised
handover. It also restores two passages missing from the first Sol. It still omits an earlier explanatory connection
while claiming the larger source record is connected. This is evidence for specific prompt/input fixes, not evidence
that the remaining synthesis problem is solved or that a model ceiling has been identified.

One `gpt-6-sol` / `max` agent generated once, with no inherited conversation, interruption, restart or repair.
The v2 activations, QeQ, network and complete v2 1:5 preceding prose were held fixed. Changes were exact-source
normalization, selective Quran lookup and schema-2 evidence anchors. Pre-run commit: `7ade57587`. The claim was
observed at 21:33:23 UTC and completion at 22:03:40 UTC on 2026-09-27, approximately 30 minutes later. These are
observed wall-clock boundaries, not a provider latency measurement. Tokens and billed dollars were not supplied.
The user explicitly said max effort and this experiment's cost are acceptable; neither is a rejection criterion here.

## Measured changes

| Measure | First Sol | Repeat |
|---|---:|---:|
| Prose bytes | 42,307 | 42,579 |
| Raw whitespace words | 4,971 | 4,802 |
| Words with Arabic tags replaced by Turkish gloss | 4,617 | 4,605 |
| Paragraphs | 44 | 41 |
| Median / longest paragraph, raw words | 113 / 151 | 119 / 168 |
| Arabic tags | 27 | 23 |
| Exact / fixable tagged quotations | 23 / 4 | 23 / 0 |
| Accounting bytes | 44,781 | 20,173 |
| Accounting share of raw response | 51.4% | 32.1% |
| Raw response bytes | 87,110 | 62,774 |
| QeQ candidate passages cited | 118 / 155 | 124 / 155 |

Accounting fell 55.0%; prose size barely changed. The accounting remains substantial. The response-size reduction
is not a measured dollar saving. All 23 new tags pass exact-source verification and prose-format validation without
repair. The verifier checks quotation text and declared sources; it does not validate every Turkish paraphrase,
interpretation or source-to-claim relationship. Fewer tags still leave many lexical claims without a local anchor.

The 203,821-byte initial packet was followed by 15 lookup responses totalling 97,910 bytes: 126 distinct requested
ayat and 349 distinct returned ayat including neighbours. All 147 explicitly cited ayat were returned by lookup;
118 requested ayat appear in the citation diagnostic. Known initial-plus-retrieval payload was 301,731 bytes,
against the first run's 201,665-byte initial packet. Wrappers, rereads and other context are not included.
Uncited neighbouring context is not proof of waste: the repeat uses the test following 72:16 and the continuing
covenant at 9:7 to qualify its explanations. Conversely, source availability does not guarantee use: 18:1–2 was
retrieved and its earlier explanatory connection was omitted.

## Passage review

The primary agent read the complete repeat and first Sol prose, revisited the frozen original/v2 comparison
passages, and inspected the accounting against its source records. No comparison agent was used.

The eight frozen preservation criteria pass, and the two improvement criteria still improve over v2. The water
frame holds the load while the bucket raises water for the traveller; P21 adds the Rabb's water and the traveller's
water. P24–28 develops the judge's middle into just measure, exact value, replacement and reckoning. P14–22 joins
upright walking, failed support, living growth, burial/rising, water and sight. The result remains a long sequence
of explanations without headings, with repeated returns to reckoning and arrival.

There are material findings beyond the ten grouped criteria:

- P3 restores Moses hoping to find guidance at the fire (20:10), alongside his road petition (28:22).
- P15 restores 17:97 and 25:34 as the bodily counter-scene to upright walking in 67:22.
- The first Sol's explanation of the unbent, upright Book at 18:1–2 disappears. The new P6's reference to the book
  given to Moses does not reproduce that lexical connection. This is a lost explanation, not just a missing citation.
- The 70:43 marker-directed rush and the 93:7 → 93:11 guidance/favour narrative disappear as supporting
  illustrations; the broader Hour/sign and gift/thanks explanations survive. Do not equate every omitted parallel
  with disappearance of its explanatory job.
- 16:76 is absent from the new target prose but is already developed in P10 of the unchanged preceding 1:5.
  A future previous-context reduction must preserve that reader knowledge or supply it locally.
- The full rain–well–beam–watering system is not explained in this 1:6. Local improvement is not full assembly.
  The inherited network still assigns 1:6 a touch role and 1:4 assembly. The newer v13 review reports a roll-call
  assembly in v2's 1:4; the old claim that it was assembled nowhere in v2 was too broad.

The narrower review command returns `eligible: true`. **Acceptance is withheld** and no `accepted.json` exists:
that gate cannot represent the lost Book connection or certify all components of the bundled records. Exact
candidate excerpts and reasoning are in [review.json](out-sol-stable/s001/1_6/review.json) and
[supplemental.review.json](out-sol-stable/s001/1_6/supplemental.review.json). The latter is explicitly supplemental,
not a rewritten predeclared test or writer input. No new 30-anchor score is claimed.

## Accounting and the next decision

All 192 item IDs have a structurally valid disposition: the writer claims 181 connected, eight explained and
three deferred. The short anchors identify full paragraphs unambiguously. B18/B19 now point to both water failure
and the working frame, correcting the first account's mismatched water evidence.

Structural validity still overstates semantic completeness. B2 marks E_F1 connected although that record includes
the omitted Book explanation. B35 marks F29 connected while its city-of-obedience component is absent. A catch-all
deferral cannot identify missing components inside records already marked connected. Keep provenance and explicit
deferrals, but do not ask the writer to produce a coverage essay or treat its labels as proof.

Before another generation, make the regression record precise enough to identify retained, partly used and
deferred explanatory components; require local evidence for the lexical surprise being made. Then test the next
single change. Compact previous context remains a separate ablation, not a change made in this repeat. A newly
planned network can address where images develop, but is a different intervention from changing the writer model.
No extra generation was started after this result.

Twenty offline tests passed before the run. Post-run checks confirm both Sol arms' frozen inputs, exact sources,
account structure and unchanged copied historical data. The baseline audit flags six live v13 source files changed
by the concurrent v13 workstream; it reports no changes to the archived v14 data. This report does not overwrite or
restore that work. See [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md) for the assessment of the user's quoted review.
