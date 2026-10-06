# Astra high versus max: four-family pilot

One independent run per family per effort setting, on the same frozen 1:6 prose and byte-identical source rosters. The shared brief differs only in model effort wording; family launch purposes are expressed separately, so this is a practical comparison of the same task, not an identical-prompt repeated experiment. No attributions were externally checked and no baseline outputs were revised after review.

## Family comparisons

| Family | High blocks / words | Max blocks / words | High reasoning tokens | Max reasoning tokens | High API-equivalent USD | Max API-equivalent USD |
|---|---:|---:|---:|---:|---:|---:|
| Beyânî | 9 / 1,024 | 13 / 1,976 | 5,036 | 16,903 | 1.070228 | 2.031310 |
| Classical coherence | 7 / 723 | 9 / 958 | 2,824 | 11,197 | 1.037810 | 1.318620 |
| Hadith | 18 / 2,573 | 21 / 3,073 | 1,602 | 16,325 | 1.000888 | 1.947546 |
| Meal | 19 / 2,422 | 22 / 2,873 | 4,314 | 26,202 | 1.344820 | 2.806764 |

**Classical coherence:** High preserves concrete remembered source contributions: Biqai's Fatiha purpose and help-to-guidance sequence, continued guidance, the favored people's identity, and Suyuti's Fatiha-to-Baqara relationship. It adds a remembered Fatiha/Baqara/Al Imran sequence and a local Yunus world-life-to-abode connection. Max has wider coverage and fuller development, but high is substantive, unlike the much thinner Sol coherence runs. The two outputs offer different useful leads; source fidelity has not been checked.

**Hadith:** Matched samples at paragraphs 3, 9, 16, 21, and 22 retain much of max's detail: remembered report settings, the distinct guidance/sebat prayers, the path parable versus the afterlife crossing, confession followed by steadfastness, differing continuations, the house-and-banquet parable, purification before Paradise, and Nawawi's deeds/mercy explanation. Max adds material such as human judgment at paragraph 2, actual hedy practice at paragraph 21, and gentle instruction at paragraph 22. High is only about 16% shorter in prose while using about 90% fewer reasoning tokens in this run. Its no-recall decisions also omit paragraphs 2 and 15, which max addresses.

**Beyânî:** High is much more selective: nine written paragraphs and thirteen no_recall, compared with max's shared-block coverage of eighteen paragraphs. It retains Samarrai's concrete Fatiha discussions, a recalled Mulk construction comparison, and Bint al-Shati's Duha reading, including dalal before revelation and favor followed by duties. Max adds the Beled and Asr readings, the differentiated method discussion, and uncertain Tekvir/Yunus leads. Some extra max coverage consists of applying a general method to the root-image paragraphs. High's omissions therefore reduce breadth, but also avoid many of those broad methodological applications. Both contain useful, unverified recollections.

## Meal

Matched samples at paragraphs 1, 2, 3, 7, 9, 11, 16, 21, and 22 retain concrete translator comparisons: English prepositions, Turkish motion verbs, witness versus martyr language, peace/salvation vocabulary, steadfastness versus uprightness, and adding the divine destination to Fatiha. High gives a remembered two-occurrence Asad pattern at 41:30 and 46:13. Max's paired Asad willingness examples and Mihr's narrowing examples are absent from high. High adds other remembered translators and explanatory choices. Both are useful as literature leads; max has broader coverage and more specific material in some places.

There is also a direct recollection disagreement: high describes DIB's 5:16 wording as kurtuluş yolları, whereas max describes it as esenlik yolları. The sources were not checked, so neither attribution is endorsed by this review. Such disagreement is a concrete reason not to infer factual reliability from fluent specificity, model choice, or reasoning effort.

## Aggregate result

| Measure | Astra high | Astra max |
|---|---:|---:|
| Cumulative input including cached input | 1,019,238 | 1,142,932 |
| Output including reasoning | 44,019 | 102,612 |
| Reasoning tokens | 13,776 | 70,627 |
| Visible output including tools/ledger | 30,243 | 31,985 |
| Blocks | 53 | 65 |
| Prose words | 6,742 | 8,880 |
| Standard API-equivalent USD | 4.453746 | 8.104240 |

High costs about 45% less and retains about 76% of max's prose words in this run. Max uses 5.13 times the reasoning tokens. High retains substantial source content in the samples, especially hadith and meal; max gains breadth, notably beyânî. This suggests a promising depth/cost tradeoff for high in this pilot, rather than a verified accuracy advantage for either effort setting. The remembered sources and details vary between outputs, so the observed differences cannot all be assigned causally to effort.

The benchmark's native usage records include repeated contexts, cached input, visible tool/ledger output, and reasoning. Pricing equivalents are not account billing figures. This single-run pilot cannot establish a stable accuracy ranking or causal effect of effort.
