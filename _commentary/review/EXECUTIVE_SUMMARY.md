# Executive summary: Phase 1 of the v3–v15 review

2026-09-28. The full evidence is in `PHASE1_REPORT.md` and `phase1/agents/*.json`.

## Method

- Eleven read-only agents covered the thirteen versions, the quran-slm distance, the sister repos and the dilution
  numbers. Each read `NORTH_STAR.md` first and scored against the same thirteen criteria.
- I compared the prose myself: 1:6 in four configurations, 18:86, 18:96, and 29:38 in every run that has it.
- No model runs were made.

## Bottom line

**We are not at the limit of what the data and models allow. We are at the limit of one method:** one pipeline,
tuned by trial on a few named cases, where each fix moves along the same trade-off between keeping everything (a
catalogue) and choosing (losing a surprise).

**Three findings reframe the problem:**

1. **Finding readings is not the bottleneck; losing them afterwards is.**
   - v5's Luna lanes held the ingredients of nearly all 26 Fatiha gold items.
   - v13's discovery step found nearly every anchor.
   - v9 found the eye film and kohl.
   - Readings died between stages:
     - labels used as filters;
     - chains judged from one member ("1:4'te tutmaz");
     - upstream "no value" verdicts repeated;
     - set-asides never handed forward;
     - a cheap selector dropping the eye film;
     - and every records-to-prose contract v13/v14 tried traded recall against form.
2. **The "bulk input dilutes synthesis" lesson is much weaker than recorded.**
   - The context-only arm was the only one allowed to use "your own knowledge of the Quran". Every fed arm was told
     "work only from the supplied evidence". The dictionary-fed arms cite 0–3 passages outside the surah (zero in 10
     of 14 runs), against 3–28 for the context-only arm.
   - Dictionary-fed runs that *were* allowed memory (the v11 brief) cite a median of 30 outside passages (12–47).
     Input size does not predict that reach (ρ −0.03).
   - Two identical context-only runs share only about 60% of their citations, so the famous 8-against-5 anchor gap
     is within noise.
   - Reasoning volume really does collapse, but only for very large packages (≈150–400k tokens: 45k → 9k thinking
     tokens).
   - Below that, what hurts is stance: verdict-carrying inputs, audit instructions, must-land lists.
3. **The model already knows a lot; data is needed in a few specific places.**
   - Context-only Opus recalls Quran references, famous lexical images with real early phrases (12 of 14 attested
     in the six early entries), grammar, Turkish drift and cross-surah parallels.
   - Its latent-sense recall collapses outside the famous core:
     - 35% for branch positions B001–B003, but 3% for B004+;
     - 0 of 60 branches no earlier reader ever activated;
     - 1 of 56 collocation-bound branches.
   - Only data supplies:
     - rare branches (the sabal eye film, ʿayn as the sun disk, ʿalam as a waymark mountain);
     - counts and dominant roles (nafakha as animating appears only when concordance counts are pushed);
     - partners that sit in other ayat;
     - construction scope;
     - marking, which memory never does unprompted.
   - **Correction (Phase 2).** "Every run recalls the ḥamaʾ creation passages" is withdrawn. The shared brief's
     citation example was literally "(15:26, 15:28, 15:33)".

## Answers so far (Phase 2 tests them)

| question | answer from Phase 1 |
|---|---|
| Q1: most we can do? | **No.** See the untouched opportunities below. Several were built or designed and never run. |
| Q2a: can the model's knowledge replace pushed data? | **Partly.** Push only rare branches with classical phrases, counts and dominant roles, and a parallels list. Allow memory, mark it, and verify it by script. |
| Q2b: enough labelled data to train? | **For a reranker, yes:** ~30k independent v12 branch pairs; 623k graded inter-ayah pairs; a held-out protocol with 19 sealed surahs. **For the aha layer, no:** complementary roles, loaded words and contrasts have only S1/29:38-sized gold. An S1-only metric failed to generalize. The inter-ayah labels are canonical-biased: 18:86 → 15:26/28/33 marked "no value". |
| Q3: a step on top of v5? | **Plausible,** if it reads v5's discovery JSON (909 ayat, 96k anchored activations, rejects with reasons) through a ~16 KB digest, integrates with Opus, adds cross-ayah partners, and never lets a selector hide what it left out. v14's composition trial is the counter-example. |
| Q4: a non-iterative alternative? | Candidates the evidence supports: "synthesize free, anchor afterward" with targeted supply (the July quran-roots lineage recorded this: free dialogue ≈10/10, schema pipelines 2–4/10); several complementary cheap readings integrated once (on 1:6, four configurations each returned a different slice); surah-first coalitions with per-ayah disclosure. Phase 2 designs and attacks them. |
| Q5: a better distance? | **The current one finds near-synonyms, not scenes.** Top-10 neighbours are 45× enriched for the same role, only 6.7× for another role in the same scene. It cannot relate same-root branches, contrasts or alternative roots. **But it is the best tool measured for choosing which branches of two context-linked words cohere** (MRR 0.54 vs 0.15 random). Replace it with a typed, context-conditioned graph: candidates from Quranic context, similarity for branch choice, plus scene-role, shared-component, contrast, sound-echo and loaded-word edges, each carrying its path as explanation. |

## The largest untouched opportunities

1. **Stop losing readings between stages.**
   - No verdict inputs.
   - No per-member chain verdicts.
   - Set-asides and record-level fragments handed forward.
   - A visible index of anything unselected.
2. **Targeted supply instead of packages or nothing,** plus permission to use memory, verified by script.
3. **Use complementary readings together.** For example: a Quran-memory reading, a rare-branch reading and a chain
   reading, integrated once.
4. **Re-synthesize the v5 harvest with Opus.** Nobody has; about $0.5–1 per ayah is my estimate.
5. **Run the coalition-first surah step and the progressive-disclosure overlays.** Both were designed and never run
   end to end.
6. **Script discovery:**
   - a definitional cross-reference detector ("the highest-yield cue class… a weekend of code", never built; a
     prototype finds the stray whose rabb is unknown in S1);
   - a loaded-word detector (collocation profiles: ḥamaʾ with ṣalṣāl 3 of 3);
   - a parallels list;
   - typed contrasts.
7. **Unused guards and sources.**
   - **The dictionary's own `branch_kind`.** Every branch is marked bare (3,326), mixed (5,653), non-bare (749) or
     collocation-bound (1,803). For example, ض ر ب B002 "travel" belongs only to ḍaraba fī l-arḍ: "yalın köke
     yolculuk anlamı yüklenmez". v9–v15, quran-slm and the scene index never used it.
   - **Early-source citation files.** Per-ayah citations in the early lexicons (Mufradāt 8,056, Tahdhīb 3,239, ʿAyn
     530) and Majāz al-Qurʾān (1,308 ayah-keyed glosses).
   - **Other unused material:** Maqāyīs "one aṣl" statements (473 roots); grammar translation-support rows; Turkish
     gloss error profiles.

   **User correction.** Late compilations (Lisān, Lane, Qāmūs) are *not* sense evidence: they fold collocation-bound
   senses into the root (ḍaraba = travel), the very drift the project's earliest-sources dictionary prevents. Model
   memory carries the same risk, so memory checks must use `branch_kind`. No classical tafsir or munāsabāt text
   exists locally.
8. **Batch API and no 2× cache writes.** They were designed three times and never built, and they would halve Opus
   cost. One or two Opus calls per ayah would then land at about $0.3–1.0.
9. **A fixed blind scorecard with two replicates per decision.** Every version since v11 was replaced before its
   planned measurement ran.

## Next: Phase 2 (approved)

Four independent proposals, attacked by critics on cost, North Star fit, and dilution/pruning, plus a completeness
critic:

- (A) a step on top of v5;
- (B) a non-iterative method;
- (C) a new distance, tested by free scripts;
- (D) using the model's own knowledge to shrink input.

Every design is scored on the watch cases: 29:38's neighbour-activated eye film, ḥamaʾ at 18:86 and nafakha at
18:96 as Quran-loaded words, and the Fatiha chains. No Luna or Opus pipeline runs without a separate approval.
