# Review of the proposed packet / extractor / writer workflow

The architecture is worth testing: deterministic corpus discovery, a cheap source extractor, and a fresh family writer remove expensive conversational discovery from the writing stage. The benchmark supports the motivation, but does not yet support the stated cost or quality conclusion. No new agents or workflow were launched for this review.

## Independently checked claims

- The frozen 1:6 page contains 171 distinct expanded source verses, including 1:6, and 211 reference occurrences.
- The two corpus runs cite 933 distinct segment locators in total. They are a useful reference set, not an exhaustive or semantically verified gold standard.
- Cumulative input is 64,138,019 tokens for Sol high and 104,481,366 for Sol max. Cached input is 61,844,096 and 101,100,928 respectively, about 96.4% and 96.8%. Actual API-equivalent costs are $19.802453 and $32.016642. Reducing repeated context saves money, but the cumulative totals are mostly discounted cache reads.
- Ten families reproduce 90–100% of previously cited segments through the exact target/reference verse index: analytical, classical coherence, grammar, imami-mutazili, ishari, kessaf, meal, modern tafsir, rivayet and Turkish tafsir.
- Three other families need explicit treatment: qiraat reaches 59.5% (22/37), bayani 77.5% (31/40), and historical 32.1% (9/28). Ten indexed plus six fallback families accounts for only sixteen of nineteen.
- Among the proposed six fallback families, academic has 80.6% index coverage and modern coherence 42.9%; hadith, poetry, rhetoric and wujuh have zero in this reference set. Mixed index-plus-discovery treatment is more accurate than a binary taxonomy.
- Luna's $0.286248 benchmark consumed 5,414,467 cumulative input tokens, including 4,518,656 cached and 895,811 uncached. It was memory-only. It did not demonstrate full reading or extraction of 5.4M tokens of new source text. At the saved Luna input rate, 5.4M fresh input tokens alone would cost about $0.54, before outputs and retries.

The 565k source-text token estimate and 0.2–1.4M packet estimates were not independently tokenized in this review. The exact citation and coverage audit is in [PIPELINE_REVIEW.json](PIPELINE_REVIEW.json).

## Changes needed before a pilot

1. **Bounded complete source chunks.** Split large packets under the model's actual input/output limits. Preserve full segment text, headings, notes, flags, grading attribution and necessary adjacent context. A ledger can prove what was delivered; it cannot prove that a model understood every segment.
2. **Structured finding extracts.** Keep exact quotes, source/edition/locator, linked paragraphs, claim type and disagreement. Separate the author's preference from reports the author merely transmits. An extractor omission is invisible to the writer if only extracts are supplied; this is the main quality risk.
3. **Fallback for all nineteen families.** Use indexed packets where useful and bounded local discovery for the gaps, including qiraat, bayani and history. Memory-led verification is a useful additional route, but a memory-only candidate generator inherits memory's missing rare witnesses. Both Astra efforts missed the available madbuh and Muthaqqab kenud poetry examples on 100:1.
4. **Script validation plus semantic review.** A matched matn and locator establish occurrence, not the intended inference or hadith strength. Attach existing attributed gradings and variants; do not infer a grade automatically from a text match. Human/model review is needed where context or identification remains uncertain. On 100:1 both Astra efforts misassigned TDV's 38:32 reading, despite plausible prose.
5. **Label translations accurately.** Islāḥī translation can be useful evidence, with translator/language/edition and access limitations retained. Do not treat original and translated wording as interchangeable. This changes the previous original-only eligibility rule and should be versioned explicitly when implemented.
6. **Test the writer effort.** A Sol high writer supplied with good extracts may be sufficient, but that was not isolated in the existing end-to-end runs. The claim that repeated high runs gain more than max needs a matched-budget experiment including union/merge costs. In 100:1, Sol max added useful source-specific findings in all four families, and two high runs would cost more than one max run overall.

## Cost assessment and first experiment

At the stated 60k uncached input and 15k total output per family, nineteen Sol writers alone cost **$5.13** at saved rates. Extraction, memory leads, verification, retries and reconciliation add to that. If 15k means visible prose, reasoning output also needs costing. $4–6 is therefore an optimistic unbenchmarked end-to-end estimate, although a substantial reduction from the current corpus-loop cost is plausible.

Start with rivayet, grammar and meal: indexed Arabic tafsir, more variable grammatical material, and exact Turkish/version wording. Give the extractor the actual frozen prose and deterministic packets, while withholding the 933-locator reference set. Measure finding-level recall, preservation of disagreements and gradings, false positives, paragraph fit, new useful findings and actual stage costs. Compare against the reference afterward and manually review a sample of uncited packet passages to detect shared blind spots. Then test a non-indexed family such as poetry and the final fresh writer. No end-to-end quality or cost claim is established by a retrieval-only test.
