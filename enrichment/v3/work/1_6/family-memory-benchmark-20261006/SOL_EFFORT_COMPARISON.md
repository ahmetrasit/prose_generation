# Sol high versus max: four-family pilot

This is a qualitative spot comparison of one fresh run per family per effort setting, on the same frozen 1:6 prose and byte-identical source rosters. It is not a source-verified accuracy evaluation or a repeated experiment. The substantive research instructions are shared; launch count/model wording and the later lanes' explicit isolation sentence differ. Neither output was revised after review.

## Native usage and output size

| Measure | Sol high | Sol max |
|---|---:|---:|
| Cumulative input, including cached input | 1,190,503 | 1,176,767 |
| Output, including reasoning | 31,007 | 66,168 |
| Reasoning output | 11,432 | 44,432 |
| Visible output, including tools and ledger | 19,575 | 21,736 |
| Prose blocks | 64 | 68 |
| Turkish prose words | 4,734 | 5,524 |
| Standard API-equivalent cost | $0.778987 | $1.199432 |

Max spent 3.89 times as many reasoning tokens, generated 16.7% more prose words, and cost 54.0% more. Its cumulative input was slightly lower, showing that tool calls and repeated contexts vary between runs. These are native token counts and pricing equivalents, not account billing figures; the full breakdown is in usage.json and usage.csv.

| Family | High blocks / words | Max blocks / words | High USD | Max USD |
|---|---:|---:|---:|---:|
| Beyânî | 22 / 1,804 | 22 / 1,864 | 0.197542 | 0.308995 |
| Classical coherence | 5 / 389 | 5 / 341 | 0.171862 | 0.240776 |
| Hadith | 21 / 1,312 | 19 / 1,488 | 0.221341 | 0.341459 |
| Meal | 16 / 1,229 | 22 / 1,831 | 0.188242 | 0.308202 |

## Findings from matched samples

The samples reviewed were paragraphs 3, 9, 16, 21, and 22 for beyânî, meal, and hadith, plus the complete five-block classical-coherence outputs. The review assessed concrete remembered contributions, differences between authors, connection to the supplied findings, and adherence to the instruction not to grade the frozen prose.

**Beyânî:** Max's paragraph 3 adds more cross-verse examples for continuing guidance; paragraph 16 better distinguishes the speaking situations of Jesus, the Fâtiha reader, and the command in Hûd. Coverage and length barely change. Both runs largely apply Bint al-Shati's general method rather than recall her specific treatment of the findings. Max's paragraphs 9, 21, and 22 also drift into judgments about where the supplied lexical interpretation obtains its strength. Phrases such as “esas gücünü ... Kur'an sahnelerinden alır” and “kök akrabalığını ... sınama” go beyond a remembered literature position. Higher effort did not resolve this scope problem.

**Classical coherence:** There is no convincing depth gain. Both runs produce five short blocks centered on the 1:5–7 sequence and the Fâtiha–Baqara guidance connection. Max is shorter and substitutes paragraph 3 coverage for high's paragraph 16 coverage. It attributes the Fâtiha–Baqara connection to Gharnati more confidently, whereas high records uncertainty. Without source checking, that confidence change cannot be counted as better accuracy.

**Hadith:** Max supplies useful additional, concrete remembered reports. Paragraph 3 distinguishes guidance through disputed truth from preservation of the heart's direction. Paragraph 21 connects the path of seeking knowledge to Paradise and adds the report of believers recognizing their homes there. Paragraph 22 relates deeds, mercy, and the request for guidance more fully. High already has relevant concrete reports, especially the confession-then-steadfastness report in paragraph 16. Max has fewer blocks overall but somewhat more prose. This family shows the clearest useful change in the samples, with all report attributions still unverified.

**Meal:** Max expands to all 22 paragraphs and introduces more translators and cross-verse comparisons. Paragraph 16 makes the repeated worship/straight-path sequence clearer; paragraph 22 distinguishes English translation vocabulary while relating guidance to favor. Some additions describe tafsir layers or the input's theological argument rather than a specific translator choice. Max still does not demonstrate a consistent translation error through recalled repeated examples, and the source list sometimes includes both Asad's English and Turkish IDs without explaining a difference between them. More coverage is not equivalent to a larger inventory of concrete translation choices.

## Working conclusion

The samples show some useful changes, especially in hadith, but no uniform gain from max. Classical coherence remains thin; beyânî remains largely methodological and retains scope drift. Meal grows substantially without fully meeting the request for concrete translator patterns. One run cannot isolate a stable causal effect of effort from ordinary generation variation. This pilot supports selective use of max for a difficult, specific subtask rather than claiming that max consistently produces a better whole-family literature review.

No web search, repository search, corpus retrieval, or external attribution verification was performed by this review. The benchmark's tool-input scan found no forbidden-search or cross-lane-path flags; this is observational evidence, not filesystem enforcement.
