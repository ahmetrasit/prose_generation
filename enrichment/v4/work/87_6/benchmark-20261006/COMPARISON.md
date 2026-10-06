# 87:6: corpus Sol max versus memory Astra high

Both runs use the same frozen v16 r13 page with augment9: 17 paragraphs, identical input bytes, 19 source families. Sol max reads local corpus passages and permits local keyword discovery; Astra high uses learned knowledge without retrieval. The comparison changes model, effort and evidence mode together. It cannot isolate any one of them. There is one run per configuration.

## Cost and size

| Measure | Astra high memory | Sol max corpus |
|---|---:|---:|
| Completed families | 19 | 19 |
| Standard API-equivalent USD | 19.118502 | 30.442718 |
| Input tokens, cumulative | 4,875,803 | 97,776,485 |
| Cached input tokens | 4,289,792 | 94,531,584 |
| Output tokens, reasoning included | 179,372 | 504,660 |
| Reasoning output | 36,461 | 233,593 |
| Literature blocks | 256 | 290 |
| Prose words | 35,097 | 25,712 |

Corpus Sol costs $11.324216 more (59.2%). It produces more, shorter blocks with source locators. The accumulated input is the sum of repeated contexts across retrieval and writing calls, not a 97.8M-token initial prompt. Parent preparation, review, repairs and assembly are excluded; no measured parent cost is available. No corpus request triggered long-context pricing. Figures are API equivalents from native usage, not billing statements.

## Concrete gains and misses in tafsir

This is a targeted comparison of grammar, hadith, meal, historical and modern-coherence paragraphs, alongside the full source/paragraph inventories. It is not a semantic audit of every block in all 19 families. Source anchors were checked across all corpus blocks.

### 87:6: promise or prohibition (paragraph 9)

Both grammar runs retain the competing readings: a promise of not forgetting, versus a prohibition explained through verse-ending elongation and avoiding neglect. Astra is already substantive here; Sol does not discover the existence of this disagreement anew.

Corpus Sol supplies Nahhas's explicit objection that forgetting is not voluntary, plus Samin's defense of the alternative as avoidance of causes of forgetting. This makes the arguments and attribution checkable.

Meal is a clearer retrieval gain. Astra says it cannot confidently name a translator turning the promise into a prohibition. Corpus Sol reads Atalay's imperative, the old interlinear text's command to strive and not forget, and Tekin's obligation plus added acts. It contrasts these with the actual reminder command at 87:9. These are concrete translator choices. Two different translators' examples do not establish a repeated error by one translator, and the underlying prohibition reading is a known tafsir alternative; the comparison should not automatically declare it an error.

### 87:7: exception, forgetting and abrogation (paragraph 13)

Astra grammar recalls Farra, cautiously recalls Zajjaj, and distinguishes forgetting from postponement in 2:106. Corpus Sol adds Nahhas's multiple alternatives and Samin's explicit rejection of attaching the exception to 87:5. Its source-based Zajjaj discussion qualifies identifying the forgetting form with simple abandonment. Thus choosing Astra high retains the main problem but loses several precise argument/attribution details in this sample.

Astra meal offers Asad's interpretation of 2:106 in terms of prior revelations rather than intra-Quran abrogation. Corpus meal instead makes the translation layer especially concrete: Asad's bracketed forgetting gloss in English and Turkish, old/new Suleymaniye versions, ayah versus message, and the note's prior-book interpretation. Both useful contributions should remain distinguished.

Hadith illustrates complementary scope. Astra supplies remembered Abu Musa material with Nawawi's abrogation reception and an Ibn Maja/Hudhayfa eschatological removal report. Corpus Sol's paragraph focuses on the Umar/Ubayy report's actual cited form, another Nasai record linking naskh to qibla, named corpus grading assessments, and Aisha's temporary forgetting/remembering variants. Choosing corpus Sol alone loses those broader remembered leads from this paragraph; choosing Astra alone loses the checked wordings, local variant distinctions and available grading metadata. This review does not independently authenticate any report.

### Surah composition: actual Cuypers versus method application (paragraphs 1,13,15)

Astra recalls Islahi's prophetic-task and aid framework, his 87–88 pairing, and uncertain exception interpretation. It labels its Cuypers observations as applications of his general method rather than a recalled published scheme.

Corpus Sol recovers Cuypers's actual ABB-prime opening division, displacement of creation/reminder themes across 87–88, and the framing of 87:10–15 by remembrance. It also recovers his contextual argument that 2:106 concerns replacement of prior Torah provisions rather than Quran verses cancelling one another. Astra explicitly cannot confidently supply Islahi's exact naskh formula there.

This is strong evidence for retrieval's value in the observed workflow. It is not proof that Sol is a better model: corpus Sol cannot use the unavailable Farahi text or Urdu Islahi original, so their remembered tradition coverage is absent by design. It also correctly distinguishes its application of the published division to the page's person shift from Cuypers's own explicit analysis of that shift.

### Preservation and historical context (paragraph 9)

Both connect preservation with collection after the Prophet's death. Corpus Sol anchors Zarkashi's distinction between the prophetic assurance and later collection due to fear of losing reciters, and adds Emin Isik's explicit extension to later memorizers. Astra provides a broader remembered summary of prophetic writing, Abu Bakr's collection and Uthman's codex work. Retrieval strengthens attribution and exact linkage; it does not make all historical material newly discovered.

The corpus historical ledger also retains Suyuti's very-weak judgment on the directly indexed 87:6 occasion narrative, separating it from 75:16 material. A corpus grading statement remains a statement of that source, not independent authentication by the agent.

### Reading as worship and earlier scripture (paragraph 17)

Astra hadith supplies rich ethical leads: Aisha's Quran-as-character account, the learning-and-practice teaching tradition, reading that does not pass the throat, and Quran as proof for or against the reader. Its specific author/report attributions remain memory-based here.

Corpus Sol supplies checkable Friday/Eid and witr recitation reception, the Waraqa/Moses connection, and the Ibn Hibban scroll report with an explicit absence of grading in that corpus record. It does not retain the full range of Astra's ethical leads in this block. More blocks and max effort have not made the corpus output a superset.

## Decision from this sample

Use corpus Sol max when actual source passages, translator wording and author-specific composition are required. Choosing Astra high memory saves $11.32 and supplies broader interpretive and outside-corpus leads, but leaves attributions unverified and misses several recoverable precise passages. A cheaper corpus Sol high 87:6 run has not been performed, so its price or omissions must not be inferred from this pair.

For production, the 1:6 corpus high/max comparison supports selective effort rather than automatically using max for every family. This 87:6 run tests a second page; it does not establish the optimum allocation or a reliability score.

## Validation

All 19 corpus ledgers contain exactly 17 decisions. All 290 blocks assembled after frozen paragraphs, with shared-block links where present. Source/ledger checks passed and removing insertions recovers the frozen bytes. All **1,204** source anchors were checked; parent review repaired **29** raw mismatches, including missing footnote markers, short quotes and paraphrased connectors. Original anchors and replacements are preserved in `PARENT_ANCHOR_REVIEW.json`; passing final checks are not described as flawless raw agent output. No corpus block prose was changed in this review.

Per-family native tokens and prices are in `usage.csv` and `usage.json`. `AGENT_COSTS.md` and `agent_cost_matrix.csv` compare both runs family by family.
