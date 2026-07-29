# S100:1-2 Default Writer Model Comparison

## Findings and verdict

**Headline verdict:** among these three conditions, `gpt-5.6-sol max` is the best reader-facing Layer 2 writer. It gives the clearest hierarchy of movements, keeps returning lexical detail to the ayah's surface, and compresses most successfully without turning the prose into a list. The `gpt-5.6-sol xhigh` baseline is the best editorial/depth source: it preserves the widest range of lexical, contextual, and friction-bearing material, but its reader prose repeatedly asks the reader to rank many secondary lines for themselves.

The result is not simply "shorter wins." On 100:1, `5.6-sol-max` remains substantial at 915 words because the ayah has several coherent movements worth developing. On 100:2, it contracts to 517 words because hidden fire, impact, trace, witness, and successful ignition can be gathered into a much tighter argument. That ayah-sensitive difference is a strength. By contrast, `5.5-high` reaches brevity partly by moving less-integrated material into catch-all closing paragraphs.

`5.5-high` is the shortest and easiest to enter on 100:1, but it is not the best condition overall. Its 100:1 ending becomes a compact inventory of remote pressures, its 100:2 prose is written in ASCII Turkish and loses publication-level readability, and its own 100:1 friction report says the session could not verify that the executing model had actually been switched to `gpt-5.5 high`. Its artifacts can be compared as a labelled condition, but they do not establish a clean causal model comparison.

The canonical Layer 2 requirement still matters: prose must be readable with evidence closed, even if a shorter downstream surface is added later. A future summary must not become a remedy for canonical prose that remains catalogued or disorienting.

### Reliability caveats

- All three conditions encountered the same contract conflict: the inner specification requires separate prose, evidence, findings-index, and friction artifacts, while the run allowed only three files. Both `5.5-high` outputs and both `5.6-sol-max` outputs embed the findings index in `evidence.md`; the xhigh baseline does so for 100:2 but omits the index for 100:1. Evidence-file lengths therefore are not directly comparable, and baseline 100:1 lacks the mechanical full-field audit available in the other five units.
- The embedded indexes preserve auditability but blur the required separation between evidence surface and findings index. Reader prose remains clean; editorial apparatus does not.
- Every run reports the same upstream word-analysis/QAC mismatch: three analytic units versus two QAC words, with a dangling analytic word reference. All conditions say they used `word_morpheme_spans`, so this is a shared source caveat rather than a differentiator.
- The HFT signal is a reconstructed focus trace, not a strict blind staged reveal. Claims about what appears "before" and "after" should be read as retrospective reconstruction.
- The exact activation threshold for HFT models, context deltas, and outliers is underspecified. Xhigh and `5.5-high` carry more of them; `5.6-sol-max` rejects or merges more. Some observed depth differences therefore reflect editorial admission thresholds as well as prose skill.
- External channel files were not read, channel review was first-pass rather than an adjudicated ledger, and the retired `v12_reader_responses` were absent. None of these outputs can support a final surah-channel or maturity claim.

## Compact matrix

| Condition | 100:1 prose | 100:2 prose | Argument and reader surface | Editorial/depth value |
| --- | ---: | ---: | --- | --- |
| `gpt-5.6-sol xhigh` baseline | 1,222 words | 1,148 words | Rich, polished, and repeatedly grounded in the Arabic surface, but secondary arcs accumulate as near-equal movements; slowest and most catalog-like | **Best overall source field**; strongest reservoir of remote branches, counter-pressure, and possible later cuts; 100:1 index is missing |
| `gpt-5.5 high` | 585 words | 686 words | Strong initial compression; later catch-all passages catalogue what earlier paragraphs did not synthesize; 100:2 ASCII Turkish materially harms ease and finish | Broad indexes and useful compression evidence, especially for 100:1; model identity is unverified by its own friction |
| `gpt-5.6-sol max` | 915 words | 517 words | **Best overall reader prose**; adapts length by ayah, gives movements a clear hierarchy, and closes by gathering them back into the surface | More selective; omissions are usually declared and defended, but it is not the richest source for remote editorial possibilities |

The baseline is 2.09 times the length of `5.5-high` on 100:1 and 1.67 times on 100:2. `5.6-sol-max` is 75% of baseline length on 100:1 but only 45% on 100:2. This is the key length result: max does not apply a uniform compression ratio.

## Ayah-specific notes

### 100:1

**Xhigh baseline.** The opening establishes the oath, delayed answer, participial class, and unresolved referent with excellent footing. Its best synthesis is the body-to-world sequence: breath, spark, and dust become records of expended force. It also repeatedly reintroduces full word spans, so the reader can recover the ayah surface even late in the piece. The problem is macro-shape. Boundary crossing, redress, transmission, counted pulses, habituated return, seasonal route, desire, service, and embodied witness each receive substantial new movement. The final third reads as a succession of valid editorial dossiers rather than one governed commentary. It is the richest source for an editor, but the reader has to decide which arc matters most.

**`5.5-high`.** The first five paragraphs are the most efficient opening in the set: oath, eponymous action-class, threshold pressure, manner/breath, and warm breath moving toward spark. It gives the reader a stable primary floor and explicitly distinguishes what the ayah yields alone from what later context sharpens. Its compression fails at the end, where redress, transmission, counting, old road, dry terrain, service, and ash are collected in one paragraph. Those readings are retained, but their relation is asserted through proximity rather than demonstrated. Raw Arabic is also used without the structured reading spans required by the specification. The evidence/index is valuable and broad, but the prose is a shortened field more than a fully synthesized one.

**`5.6-sol-max`.** This is the best reader-facing 100:1 of the three. It organizes the ayah around a stable sequence: oath and suspension; action-defined agents; threshold-directed running; breath as bodily geometry; heat opening toward spark; sound; breath/toz as witness; then repeated service and inward desire. Each later movement returns to `el-âdiyât` or `dabhan`, and the conclusion gathers the whole into "what the loading costs inside." It is longer than `5.5-high` because it actually explains the trace/witness and service/desire arcs that `5.5-high` compresses into an inventory. Its cost is editorial selectivity: several HFT outliers are left in the coverage note, so xhigh remains the better reservoir for reconsideration.

### 100:2

**Xhigh baseline.** The first half is strong: `fe` turns oath beats into causation, the participle names agents by action, `kadhan` supplies impact, and hidden fire makes the primary spark more concrete. The trace-and-concealment turn is also clear and properly marked as a frame shift. After that, the prose gives separate space to dust and boundary transition, witness and exhumation, enablement and value, lot selection, inner corrosion, and tender emergence. Full word spans keep the way back open, but repeated grounding cannot by itself create hierarchy. The final gathering sentence names eight added possibilities, confirming that the piece has become a well-supported catalogue. The evidence surface is the strongest apparatus of this ayah and handles the rejected planning claim explicitly.

**`5.5-high`.** This version compresses the central chain well: running becomes contact, contact becomes spark, and spark becomes visible evidence. The disclosure/trace/witness paragraph is a good synthesis. The final two paragraphs then retain success/planning, lot, plant, disease, and corrosion as successive analogies. They are shorter than the baseline treatments but remain separate nominations rather than one movement. The all-ASCII Turkish is a major reader-facing defect, especially in a text whose audience depends on careful distinctions and readable transliteration. Its evidence is broad and candid about the rejected stronger planning formulation, but the prose still lets that area occupy more space than its reliability warrants.

**`5.6-sol-max`.** This is the clearest win in the comparison. It moves through six controlled steps: sequential oath; action-defined agents; manner and impact; hidden fire made visible; spark and score as witness/interior assay; successful ignition; final gathering. The primary spark remains explicit in every secondary turn. Remote lot, corrosion, plant, iterative-pulse, rejected planning, and variant-sound material are left in apparatus rather than appended as reader-facing miniatures. This is genuine compression into movements, not merely fewer words. The evidence still records omissions and counter-pressure, making the prose easier without pretending the larger field did not exist.

## Recommendation for canonical model choice

For these active S100:1-2 conditions, use `gpt-5.6-sol max` as the canonical reader-facing Layer 2 writer and retain the xhigh baseline as the editorial/depth comparator.

This recommendation is provisional to the two sampled ayahs. Promotion should require the same checks across the remaining S100 units: every `must_integrate` topic represented exactly once in an actual findings index, every omitted candidate or HFT outlier named with a reason, no new thesis/channel claims, and human review of evidence-closed prose. The xhigh run should remain available during review because it exposes candidate connections that max may compress away too early. `5.5-high` should not drive a model decision until its execution identity is verifiably controlled.

The reason to choose max is not raw brevity. It is that its paragraphs more consistently have one governing movement, lexical detail returns to the ayah's act, secondary lines explicitly support or shift the primary, and conclusions gather rather than enumerate.

## Recommendation for the separate follow-up summary/arcs workflow

A two-tier downstream reading surface is well supported, provided it is explicitly derived and does not alter canonical Layer 2:

1. Complete normal Layer 2 first, one cold writer per ayah, with no surah thesis or channel knowledge. Freeze its prose, evidence, findings index, and friction.
2. Complete all ayahs, then run the reviewed whole-surah argument/main-arcs and channel-maturity work. Only this later stage is allowed to select the arcs that matter to the assembly.
3. After that review, run a new cold summary agent per ayah. Give it the frozen canonical Layer 2 output plus only the approved main-arc membership and maturity-bounded surah relation for that ayah. Give it no authority to revise Layer 2 or introduce a new reading.
4. Validate every summary claim against either the canonical ayah field or the reviewed surah plan. Require an explicit primary floor, one or two governing movements, and a return to the ayah surface.

Yes, the summary should be produced only after complete surah analysis/main-arcs discovery. The present comparison shows why: before that stage, remote but vivid material such as seasonal routes, lot selection, corrosion, or tender emergence can look as summary-worthy as the actual governing arc. Waiting lets the summary focus on the ayah's main local work in relation to the completed assembly without making the canonical Layer 2 writer thesis-aware.

Gradual disclosure remains binding. Although the summary is produced after the full surah is known, the text shown at 100:1 or 100:2 should use only the arc maturity available at that reading position. It must not reveal the finished channel merely because the downstream agent knows it. Full channel recognition still belongs to the reviewed overlay/`Kanallar` surface.

The prior surface names provide a clean separation:

- `Dinle`: the new 30-60 second downstream orientation, generated after arc review.
- `Derinleş`: the unchanged canonical Layer 2 prose, still required to read well with evidence closed.
- `Kanallar`: reviewed surah/pericope channels and their gradual overlays.
- `İzini Sür`: evidence, findings, counter-evidence, and coverage.

This is compatible with the repository's layered-disclosure design because selection occurs only in a derived orientation after the full field is preserved. It is not compatible with weakening canonical Layer 2 on the assumption that `Dinle` will make it readable later.
