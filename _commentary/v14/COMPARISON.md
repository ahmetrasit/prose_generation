# v14 Sol max trial — 1:6

The primary agent read the complete candidate and compared the frozen v13 original/v2 passages and preceding
1:5 prose. The eight predeclared preservation criteria survive; the two improvement criteria show progress.
The candidate remains **unaccepted**: four Arabic quotations differ from the verifier's spelling conventions.
This is a useful controlled experiment, not proof of zero regressions or a production-ready pipeline.

One `gpt-6-sol` agent at `max`, with no inherited conversation, read only the frozen writer packet. It generated
once, with no repair. Activations, QeQ and network came unchanged from v13 v2; the preceding prose was v2 1:5.
Target commentary, regression criteria and gold material were excluded. The pre-run commit is `83a00ca52`.
Both the writer model and the handover changed, so this cannot isolate a prompt effect or establish Opus economics.

## What the prose does

| Predeclared criterion | Finding |
|---|---|
| Plain sense and neighbours | Preserved: the help request becomes a plural road petition; 1:7 supplies its people. |
| Turkish losses | Preserved: hidayet, bodily dogru/istikamet and the added bridge association all receive explanations. |
| Consequential grammar | Preserved: both articles, the unmediated object construction and continuing guidance. |
| Road as connected parts | Preserved: marks, trodden surface and middle line work together. |
| Assisted living motion | Preserved: support, seeing, balanced walking, prayer, halted walkers and the dead supported body. |
| Straight balance | Preserved: judgment becomes measure, value, substitute and reckoning; same-word passages remain useful. |
| Traveller-guidance scene | Preserved: Moses' 28:22 petition develops into arrival, relationship and sustained service. |
| Coexistence and counter-evidence | Preserved: road of Hell, wrong ancestral tracks and the rejected gift bound interpretations without suppressing latent readings. |
| Water system's local contribution | Improved: the upright apparatus lifts water, sustaining the traveller's stop and resumed journey. Full surah assembly remains absent. |
| Reader development | Improved over v2: more inferential bridges and readable units; considerable serial touring remains. |

For example, v2 already mentions the well-frame. Its absence was overstated in the v13 handoff. The candidate
adds the working relationship: “Yapı dik durarak suyun yukarı taşınmasını sağlar” and “Yolda durmak, yeniden
yürümeyi besleyebilir.” The next paragraph contrasts frozen water with water lost through uncontrolled flow.
This earns a modest local improvement, not credit for explaining the complete rain–well–beam–watering chain.

The strongest continuity is paragraphs 12–14: the already explained assisted traveller becomes upright seeing
and walking, then a growing plant and standing prayer, against the dead body held upright by a staff. In paragraphs
19–22, the road's middle becomes just judgment, straight measure and a fitting equivalent before the reckoning.
These are explanatory developments beyond simply listing the root's senses.

The ten verdicts and exact candidate excerpts are in [review.json](out-sol-max/s001/1_6/review.json).
They protect selected explanations; they do not certify every sentence or every omission across all prior runs.

## Measured size and evidence

| 1:6 output | Raw whitespace words | Words after tags become their Turkish gloss | Arabic tags | Prose bytes |
|---|---:|---:|---:|---:|
| v13 original | 3,231 | 2,510 | 71 | 28,726 |
| v13 v2 | 7,451 | 5,672 | 150 | 65,405 |
| v14 Sol max | 4,971 | 4,617 | 27 | 42,307 |

Raw words include tag fields; the second measure better exposes how much of the reduction is quotation machinery.
Relative to v2, raw words fall 33.3%, but the gloss-substituted measure falls only 18.6%. This is not a length target.
The candidate cites 118 of 155 QeQ passage candidates, including expanded same-surah ranges. Citation presence
does not prove an explanation is adequate; omitted parallels are not automatically regressions.

The account structurally covers all 192 items, claiming 180 connected, seven explained and five deferred.
Those are writer claims. Some evidence spans do not prove every associated item: B2 quotes the introductory
definition for E_F1, while Moses occurs much later and 20:10 is unused; B26 quotes flowing water while the well
apparatus is in the preceding paragraph. Exact-string matching alone cannot validate those claims.

The raw response is 87,110 bytes, of which **44,781 bytes (51.4%) are accounting JSON**. Entire paragraphs are copied
into that account. This is a substantial output-cost problem; bookkeeping is not free merely because it uses no
separate model call. Future accounting should use compact, sufficient evidence anchors and modest claims.

Source verification finds 23 exact quotations and four fixable written-mark differences (11:56, 67:22, 6:161,
48:2); no missing, elsewhere or bad-source quotations. All four flagged forms match the supplied concordance once
its highlight markers are removed. The packet and verifier therefore disagree about the exact Quranic spelling.
Prose-format validation passes. No text was repaired; the source gate correctly blocks acceptance.

## What the input spend bought, and what remains

The 201,665-byte packet is 32.8% larger than v13 v2's recorded 151,835 bytes. The 49,245-byte preceding prose explains
almost all the growth. The candidate explicitly builds on it, but no ablation establishes that the entire preceding
essay was necessary. It sometimes retells material too, especially the gift circuit and sanctuary.

The concordance is visibly useful: the 33 road/adjective pairings check against its clauses, and the candidate
distinguishes seven offering-noun uses from two gift-noun uses. It avoids the conflicting legacy root totals.
The phonetic variants remain out of the prose with an explicit reason; that small input did not justify a tour.
The local Quran window supports correct transitions, although the same context also exists in other records, so
this run cannot attribute that benefit to the added 613 bytes alone.

Next priorities are targeted: align source spelling across retrieval and validation; retrieve actual QeQ passages
when developing them; reduce accounting output and overclaiming; test compact prior-reader context against the full
preceding essay. The rare-lemma concordance gap, reciprocal check and surah writer still need implementation.
Do not remove discovery dictionaries or channels based on this one writer trial. See [INPUT_AUDIT.md](INPUT_AUDIT.md).

Thirteen offline tests pass. Original v13 and copied historical data remain unchanged. Sol token billing and dollar
cost were not exposed by the agent facility. No additional generation or repair is authorized by this result.
