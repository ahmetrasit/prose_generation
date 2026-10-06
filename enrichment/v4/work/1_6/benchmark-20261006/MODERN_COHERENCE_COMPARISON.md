# Modern coherence: four completed 1:6 runs

Reviewed all blocks and ledgers for corpus Sol high/max and memory Astra high/max. Corpus Sol uses actual local passages; Astra uses remembered findings without retrieval. The frozen input is the same. Cross-model differences also change evidence mode and available works, so this is a workflow comparison, not an isolated model ranking. One run per configuration does not establish repeatable performance.

## Output and cost

| Run | Evidence mode | Blocks | Paragraphs with blocks | Prose words | Input tokens | Cached input | Output tokens (reasoning included) | Standard API equivalent USD |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Sol high | Corpus | 6 | 6 | 375 | 1,545,950 | 1,484,672 | 8,717 | 0.506660 |
| Sol max | Corpus | 6 | 8 | 471 | 1,660,320 | 1,571,328 | 17,561 | 0.667860 |
| Astra high | Memory | 8 | 9 | 1,094 | 247,624 | 219,648 | 7,184 | 0.858608 |
| Astra max | Memory | 10 | 13 | 1,514 | 262,429 | 220,032 | 21,643 | 1.726152 |

Native token counts and existing benchmark prices; API-equivalent estimates, not billing records. Input is accumulated across calls, not a single prompt. Shared blocks increase paragraph coverage without adding distinct findings. Corpus runs have only Cuypers's Composition available for attribution: Farahi's work and the required Urdu original of Islahi are unavailable under this lane's rules. Astra memory draws on those authors and Astra high also recalls The Banquet.

## Tafsir findings and omissions

### Sol high, corpus

Gains:

- Fatiha 1:5–7: retrieves Cuypers's actual three-piece composition. Praise in 1–4 and petition in 6–7 frame verse 5; worship looks backward to praise, assistance forward to guidance. This is a published author analysis rather than a newly applied method (Composition pp47,109).
- Fatiha 1:6–7: retains the closing mirror: guide/astray outside, blessing/anger inside. Also reports that the two negative members are synonymic in Cuypers's analysis. This does not make them two opposite ethical extremes (pp78,173). Sol max omits this explicit account.
- Fatiha and Baqara 2:2: reports Cuypers's own connection between the request for guidance and the Book as guide, and the two-ways parallel with Psalm 1 (p173).
- Fatiha 1:7: reports Cuypers's refusal to fix the negative labels to whole religious communities from this sura's context (pp172–174).

Misses:

- No block on paragraph 11: it does not recover Cuypers's specific explanation of 5:16 inside the covenant sequence 5:12–26.
- Omits Cuypers's pairing of suras 87–88 and his interpretation of the central question in 81:26.
- The high run read p126, which prints 81:26–29, but did not retrieve p125's explanatory discussion. It retrieved pp50 and52 but not p53, where the 5:16 interpretation is explained. These misses involve passage selection and follow-through, not simply shorter prose.

### Sol max, corpus

Gains:

- Recovers the same precise Fatiha center, which neither Astra memory run recalls as Cuypers's published scheme.
- 5:16: recovers Cuypers's covenant sequence 5:12–26, with 5:15–19 at its center. The messenger and explanatory revelation lead out of darkness toward peace and the right path, answering covenant violation and deviation in the surrounding passages (pp50,53). This supplies an actual author interpretation where Sol high had no match and Astra max offered its own methodological application.
- 87:2–3: creation, formation, determination and guidance are placed within Cuypers's 87–88 pairing, which also connects reminder and judgment themes (pp118–119).
- 81:26–29: the question about where the listener is going interrupts and connects the preceding defense of revelation and its messenger with the following reminder and wish to go straight. Cuypers makes this a choice of paths (pp125–126).
- Fatiha 1:7: specifically preserves Cuypers's qualification that the warning can apply to some Jews or Christians, pagan opponents and hypocrites; not all members of a community (pp172–173).

Misses:

- Omits high's explicit closing mirror and synonymic analysis, despite retrieving pp78 and173. Max is not a superset.
- Cannot supply Farahi/Islahi tafsir under the corpus lane's source availability rules.
- Its 5:16 block is a contextual interpretation, not a grammatical theory explaining every singular sirat/plural subul occurrence. Cuypers's English wording on p53 says way of peace; the block's plural comparison also draws on the supplied Quran wording. Do not overstate this as a comprehensive number analysis by Cuypers.

### Astra high, memory

Gains:

- Islahi's Fatiha: develops the movement from praise to worship, assistance and guidance, and continued need for guidance after belief. This broadens the author coverage beyond locally available Cuypers.
- Islahi's Baqara: situates the qibla change in Abrahamic inheritance, religious leadership, the community's witness and obedience. This is a different tafsir contribution from Sol max's 87–88 reading of paragraph 6.
- Islahi's Fatiha–Baqara relation: treats the guidance request as a prayer answered by the Book's opening.
- Paragraph 11 recalls Cuypers's treatment of religious difference around 5:48 in The Banquet. It explicitly does not claim to remember his explanation of 5:16; the connection is a broader interpretive horizon.

Misses:

- Explicitly cannot recall Cuypers's actual Fatiha scheme, replacing it with its own application of his method.
- Does not recover the specific covenant interpretation of 5:16, the 87–88 pairing or the 81:26 center found by corpus Sol max.
- At paragraph 19, distinguishing two negative phrases from two equal-and-opposite extremes is its own methodological observation. Sol high can replace that with Cuypers's explicit mirror/synonymic analysis.
- The remembered Farahi/Islahi attributions have not been independently checked against originals in this comparison. Greater author breadth is not verified greater accuracy.

### Astra max, memory

Gains over Astra high:

- Islahi on Anam's closing commandments: reads the one straight path as unifying divine obligations after disputes over invented prohibitions; divergent paths fragment that allegiance. High instead uses Cuypers/5:48 as its principal broader horizon for this paragraph.
- Islahi on Fatiha 1:7: develops the difference between resistance to known truth and misdirected religious understanding, and connects the historical examples with the paired Baqara/Al Imran reading. This is an author position distinct from Cuypers's contextual reading.
- Islahi on Hujurat 49:17: places the claim that conversion is a favor to the Prophet against the preceding tests of faithful conduct and God's gift of guidance. High marks this cross-verse connection as its own application rather than recalled author tafsir.
- Extends Farahi/Cuypers methods to Hud's command of steadfastness, the end of Anam, and Yunus/Araf's movement toward the final abode. It labels these as its own applications, not remembered detailed author interpretations.

Misses:

- Still cannot recall Cuypers's precise Fatiha composition or his actual 5:16 analysis. Its paragraph 11 comparison applies a general method to the supplied verse; more reasoning has not recovered the missing source passage.
- Omits high's recalled Banquet/5:48 contribution.
- Some extra covered paragraphs reuse shared blocks or extend general methods. Thirteen covered paragraphs are not thirteen new author findings.
- The stronger remembered author attributions remain unverified against originals here, including the more specific Islahi claims at paragraphs 7,19 and22.

## Judgment for this family and workflow

For source-anchored Cuypers tafsir in this observed corpus run, Sol max earns its $0.161200 premium over high (31.8%) through three substantive additional author analyses. Retain high's closing mirror analysis during synthesis. The observed recommendation is max for corpus modern coherence, with moderate confidence because there is only one paired sample.

For the memory workflow, the existing approved high default remains reasonable: Astra max costs $0.867544 more (101.0%), gains some specific Islahi material and useful applications, but still misses the precise Cuypers findings that retrieval supplies. This does not revise the saved global memory allocation. Astra offers richer interpretive prose and broader remembered authors; corpus Sol supplies more checkable Cuypers-specific tafsir. The evidence does not support saying Astra is the only route to reliable findings.

All 36 corpus evidence anchors were checked against local passages (17 high,19 max). The decisive explanatory pages 53,118–119,125–126,78 and173 were read for this review. Anchor matching supports provenance; it is not an independent authentication of editions or exhaustive validation of every remembered attribution.

## Inputs reviewed

- `enrichment/v4/work/1_6/corpus-sol-high-20261006/modern-coherence/{blocks,ledger}.jsonl`
- `enrichment/v4/work/1_6/corpus-sol-max-20261006/modern-coherence/{blocks,ledger}.jsonl`
- `enrichment/v3/work/1_6/family-memory-astra-high-20261006/modern-coherence/{blocks,ledger}.jsonl`
- `enrichment/v3/work/1_6/family-memory-astra-max-20261006/modern-coherence/{blocks,ledger}.jsonl`
- Native usage in this directory's `usage.json` and the v3 memory benchmark's `usage.json`.
