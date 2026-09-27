# Matched Sol 6 max / Astra 6 max — 1:6

Astra is the stronger candidate in this matched run. It preserves the upright Book, fire/guide, bodily resurrection
and working well frame that the new Sol candidate omits. Its sections also carry more of an argument. Neither
candidate is accepted: both lose the explicit connection between the trodden road surface, the signs and the centre
line. All generated responses remain unchanged. This result supports continuing with the existing pipeline and
targeted fixes to preservation and input completeness; it does not establish that either model is regression-free.

The prompt and the writer both matter. The revised brief gets Sol to supply exact local Arabic evidence and headings;
its 23 tags in the previous repeat become 110 here. But Sol also compresses distinct explanations away, including
passages it actually retrieved. Astra responds to the same task with stronger retention, source caution and functional
development. One pair demonstrates this difference in outcomes, not a universal model ranking or a measured model
ceiling. There is no reason to reject this experiment on cost: the user expressly accepts max effort and its cost.

The candidates are [Sol](out-sol-argument/s001/1_6/1_6.reading.tr.md) and
[Astra](out-astra-argument/s001/1_6/1_6.reading.tr.md). The primary agent read both complete candidates, checked the
frozen baseline passages and preceding 1:5, and wrote the reviews. No comparison agents were used.

Both writers ran in parallel, once each, without interruption, retry or repair. They had the same v2 activation,
QeQ, network, full previous 1:5, revised brief, schema-3 trace contract and exact-text lookup capability. The packets
are byte-identical after normalizing the lookup routing tag. The 15 criteria were frozen separately before generation
and excluded from the writer packet. The pre-run commit is `f15e74b4a`. The writers chose different lookups; the
comparison controls available evidence and instructions, not the returned tool text, output length or hidden compute.

| Measure | Sol argument | Astra argument |
|---|---:|---:|
| Raw whitespace words | 4,055 | 6,442 |
| Words with tags replaced by Turkish gloss | 2,920 | 5,119 |
| Headings / prose paragraphs | 6 / 25 | 5 / 49 |
| Median / longest paragraph, raw words | 164 / 280 | 128 / 184 |
| Arabic tags, all exact | 110 | 140 |
| Quran / dictionary tags | 68 / 42 | 81 / 59 |
| Accounting bytes | 15,112 | 16,180 |
| Accounting share of raw response | 28.6% | 21.2% |
| Initial packet bytes | 206,599 | 206,601 |
| Lookup calls / returned bytes | 15 / 94,287 | 11 / 112,390 |
| Candidate passages cited, of 155 | 91 | 135 |

Paragraph counts exclude heading-only blocks. The raw-word measure counts Arabic, transliteration and metadata;
the gloss measure better approximates the Turkish reading. Source checks verify exact quoted text against its
declared Quran or dictionary source, not the truth of the translation or inference. Citation counts neither prove
integration nor prescribe using every passage. Actual tokens and billing are unavailable. Both claims were observed
at 22:23:50 UTC; completion was observed at 22:49:12 for Sol and 22:52:18 for Astra. These are observation intervals,
not provider generation timings. Per-arm provenance, lookup logs and `comparison.metrics.json` retain the details.

The frozen criteria give the following results. “Mixed” blocks acceptance; gains cannot cancel a lost explanation.
The reader-development criterion includes retention, so its failure is partly consequent on the road loss, not a
second independent missing explanation. These are the 15 predeclared criteria, not a rescore of the separate historic
30-anchor sheet.

| Criterion | Sol | Astra |
|---|---|---|
| Help → plural petition → 1:7 | Preserved | Preserved |
| Turkish losses and added bridge association | Preserved | Preserved |
| Articles and direct-object construction | Preserved, less careful | Preserved |
| Signs + centre + trodden surface | **Mixed: surface connection lost** | **Mixed: surface connection lost** |
| Assisted, halted and living upright motion | Preserved | Preserved |
| Straight balance and exact measure | Preserved | Preserved |
| Concrete traveller-guidance scene | Preserved through Medyen | Preserved |
| Latent/plain coexistence and counter-evidence | Preserved | Preserved |
| Well frame working with water and traveller | **Regressed** | Improved |
| Reader development with protected explanations retained | **Mixed** | **Mixed** |
| Upright/unbent Book, 18:1–2 | **Regressed** | Preserved |
| Fire/guide, 20:10 | **Regressed** | Preserved |
| Face-down resurrection, 17:97 / 25:34 | **Regressed** | Preserved |
| Paragraph-local lexical source hinges | Improved | Improved |
| Orientation and sustained argument | **Mixed** | Improved |

Exact candidate evidence and reasoning are in each arm's `review.json`; `review.check.json` records rejection.
`supplemental.review.json` reports additional losses and incomplete multi-part records. No `accepted.json` exists.
Block numbers below count blank-line blocks, including headings, in the unchanged prose; they are not trace bundle IDs.

Astra's strongest change is functional development. In blocks 12 and 18 the intact blind eye and the dead body held
upright share a question: does the visible form still do its work? Support then becomes a means of growing a body
capable of carrying itself. The fixed frame in block 23 bears the load so the bucket can move: “Durmak, burada
hareketin koşuludur.” Standing still is now a condition of useful motion. The traveller's halt and provisions carry
that motion onward. The well story also includes the child's concealment and sale, distinguishing being moved from
being brought into a good relationship. The Medyen marriage later gives arrival a new responsibility. These are
explanatory consequences, not merely names gathered under a heading.

Astra is also more careful with evidence. Its direct-object discussion uses 90:10 to prevent a mechanical claim that
edat-free guidance guarantees arrival. At 7:16 it distinguishes a road made definite by “your” from the two articles
in 1:6. It restores the Book explanation inside the discussion of a life made straight (block 7), the actual fire/guide
scene (8), and the face-down reckoning consequence (49). The previously missing city-of-obedience component appears
in block 52. Secondary illustrations from the first Sol, such as 70:43 and 93:7 → 93:11, return too.

Sol's source revision is real: signs, the intact blind eye, assisted gait, bride, coin and valuation now have exact
local Arabic phrases. Its clear opening, gift/benefaction circuit, companions, Medyen marriage and balance/reckoning
remain useful. But the six sections often collect independent scenes. The collective-walking section moves through
ancestors, animal parts, swallowing and weapons; the arrival section moves from gift to bride to pilgrimage and back
to gift. Shorter total prose does not ensure tighter argument. The new Sol is only 2,920 gloss-substituted words,
down from 4,605 in the repeat, and loses distinct explanations despite having no word cap.

The Book, fire and face-down passages were all explicitly requested and returned to Sol. Their absence is therefore
not a missing Quran-source problem. The well is different: Sol deferred F47/E_F47 because it judged the frame and
water-drawing scene to add no direction to this ayah's explanation. The two previous Sol outputs, and Astra here,
demonstrate the contribution it discarded. Sol also explicitly defers the substitution/blood-price explanation.
That is more honest accounting, but still a content loss against the prior output. It mislocates “âlemler” and
“sahip” in the previous ayah, when those words belong to 1:2 and 1:4; discussing them in 1:5's commentary does not
make them words of 1:5.

The shared road loss needs a narrow description. Both writers explain signs and the middle line. Both have the full
previous 1:5, where the trodden surface is already explained. A brief return connecting that surface to the requested
path would be enough; retelling 1:5 is unnecessary. Neither makes that connection. The earlier Sol outputs did:
first Sol block 18 and stable block 25 explicitly join usable ground, readable signs and measured direction.
Thus this is a regression in the developing explanation, not a claim that the reader has never encountered the surface.

The new trace helps, but has not solved partial use. Sol records 173 linked, nine partial and ten deferred IDs;
Astra records 188 linked, three partial and one deferred. “Linked” deliberately means only a location, not “connected”
or fully explained. Nevertheless the brief also asks for distinct omissions within linked records to be named. Sol
links E_F1 without the Book/fire components, E_F25 without the resurrection consequence, F29 without the city, and
F23 without the surface. Astra also links F23 without naming its missing component. Renaming the grade removes an
overclaim; the independent omission audit still has work to do.

The input audit found both available-but-unused evidence and real gaps:

- The road branch is present in `branches.md`, the inventory and previous prose. Its omission cannot be blamed on
  unavailable input. Full previous prose also supported the staff, growth, herd and ship continuity; this run does
  not justify deleting it wholesale. A compact reader-state ablation remains separate work.
- F12 mentions a rock member, gh-d-b B004, but its branch line is missing from `branches.md`. Astra correctly reports
  that source gap rather than inventing a quotation. Recovering branch references embedded in finding descriptions,
  as well as their formal branch field, needs checking in a future preparation step.
- F30 asserts an alternative reading at 43:61; the variant packet contains only the focus ayah's phonetic variants,
  and the lookup returns canonical text. Astra explicitly defers that alternative. Exact Quran access alone does
  not supply variant evidence. Both writers also defer F54's unattested near-sound material.
- Astra returned 409 distinct ayat and cites 155; Sol returned 311 and cites 100. All Astra citations occurred in
  returned text. Sol's only cited ayah absent from lookup returns is 1:4, already in the frozen local window.
  Much retrieval is surrounding context. Unquoted material is not automatically wasted: it can support selection
  or counter-evidence. The measured initial-plus-lookup payloads are 300,886 and 318,991 bytes, not token bills.

Against previous runs, both new candidates fix the first Sol's exact-text rejection and improve local anchoring over
the stable repeat. The raw accounting tail is now about 15–16 KB, versus 44,781 initially and 20,173 in the repeat;
Astra's lower percentage also reflects its longer prose. Astra's 5,119 gloss words are fewer than v2's 5,672, with a
longest raw paragraph of 184 rather than 897. That is a useful preservation/readability result, despite the road loss.
Sol's shorter response should not be promoted as an efficiency gain when the missing explanations were requested.
Both still have serial lexical touring; Astra's headings and carried consequences reduce it, rather than eliminate it.

The next change should protect distinct explanatory components inside multi-part records, with an explicit location
or reason for each consequential omission. It should also distinguish prior reader knowledge from the new connection
this ayah owes, and close the two source gaps above. It should not require all 155 passages, impose a word quota or
expand the bookkeeping back into essays. Preserve these outputs as evidence; a further run needs a new frozen arm.

Validation: both schema-3 accounts are structurally valid; all 250 tags are exact with no repair; both prose validators
pass; packet hashes and all four experimental arms' frozen inputs verify. The 23 offline tests passed before the
writers started and no implementation changed after that run. The source-copy audit reports the six expected files
changed by the concurrent v13 workstream, with **no copied historical-data changes**. The generated prose and raw
responses were not edited. The concurrent v13 work was not staged or restored.
