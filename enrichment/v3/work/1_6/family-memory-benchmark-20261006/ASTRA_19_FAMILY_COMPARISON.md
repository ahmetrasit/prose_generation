# Astra high versus max: all 19 source families on 1:6

All 38 Astra tasks are complete. This report combines the full original four-family review with full reads of every block and open ledger entry in the remaining 15 pairs. No audit subagents were used. Agents used training memory only; no source verification was performed. Recommendations assess useful recalled material, attribution discipline, relevance and redundancy, not established historical accuracy.

## Recommendation

Use **max for 10 families**: rivayet, Keşşâf, beyânî, işârî, İmâmî–Muʿtezilî, vücûh, meal, historical, academic and poetry. Use **high for nine**: analytical, classical coherence, modern coherence, grammar, kıraat, rhetoric, modern tafsir, Turkish tafsir and hadith. Grammar, kıraat, analytical and hadith are suitable for targeted max reruns when a particular paragraph needs a wider variant inventory.

For this observed page, choosing those ten max runs and the other nine high runs costs **$26.6142 API-equivalent**, compared with **$18.8095 all-high** and **$34.4415 all-max**. The selected mix saves **$7.8273 (22.7%)** against all-max. This is a sum of observed runs, not a measured new hybrid execution or a projection for every verse.

| Family | High USD | Max USD | Max premium | Default | Reason |
|---|---:|---:|---:|---|---|
| academic | $0.8875 | $2.0125 | 126.8% | Max | Max broadens actual scholarly voices: Nöldeke/Schwally, Donner, Lange, Sinai; high is narrower. |
| analytical | $1.1751 | $2.3241 | 97.8% | High | High already has substantial treatment by all six authors. Max adds alternatives and the closing knowledge/action contrast; reserve it for exhaustive coverage. |
| bayani | $1.0702 | $2.0313 | 89.8% | Max | Max adds passage-specific Bint al-Shati readings and additional Samarrai examples, beyond method applications. |
| classical-coherence | $1.0378 | $1.3186 | 27.1% | High | Different useful examples in each; no consistent max advantage in specific author analysis. |
| grammar | $1.0169 | $2.2708 | 123.3% | High | High already technically detailed; max adds morphology, syntax and wider source voices, useful for selected difficult paragraphs. |
| hadith | $1.0009 | $1.9475 | 94.6% | High | High covers the core reports well. Max adds secondary variants, wealth trial and literal hedy; high also has unique reports. |
| historical | $0.7795 | $1.6193 | 107.7% | Max | Max adds distinct contextual narratives and variants: idols, Hums, Zamzam, Hilf al-fudul and Hudaybiya. |
| imami-mutazili | $0.8134 | $1.6145 | 98.5% | Max | Max adds specific Qadi Abd al-Jabbar analyses, improving balance beyond the strong Imami treatment already in high. |
| ishari | $1.3170 | $1.5057 | 14.3% | Max | Max adds source-specific Sulami, Herewi, Tustari and Kashani contributions at a comparatively small premium. |
| kessaf | $1.0417 | $1.7751 | 70.4% | Max | Max adds specific verse explanations and distinctions, including the rain parable, qiyam and closing knowledge/action failures. |
| meal | $1.3448 | $2.8068 | 108.7% | Max | Max supplies additional translator patterns and narrowing examples, matching the stated aim of this family. Wording still needs verification. |
| modern-coherence | $0.8586 | $1.7262 | 101.0% | High | Most extra coverage is method application or relocation. High already handles the core structure and has a unique Cuypers comparison. |
| modern-tafsir | $0.9457 | $1.9527 | 106.5% | High | High is already strong and retains specific Abduh/Ibn Ashur material that max does not recall. |
| poetry | $1.0495 | $0.9849 | -6.2% | Max | Max adds actual lexical witnesses for h-d-y, leading animals and a straightened spear, plus a Mufaddaliyyat passage. |
| qiraat | $0.8654 | $1.5834 | 83.0% | High | Core readings shared; max adds reader distributions and secondary passages. Prefer targeted max for difficult apparatus. |
| rhetoric | $0.7868 | $1.8233 | 131.7% | High | Most additional max material is general theory or overlaps Keşşâf. High retains useful unique examples. |
| rivayet | $1.0332 | $2.0986 | 103.1% | Max | Max broadens early-source voices and variant reception: Abdurrazzaq, Muqatil, Wajiz, Rad hadi reports and Baghawi continuation analogy. |
| turkish-tafsir | $0.9880 | $1.5559 | 57.5% | High | High already covers both works throughout the page, including useful interpretations missing from max. |
| wujuh | $0.7973 | $1.4902 | 86.9% | Max | Max adds several cross-verse semantic categories and contrasts, rather than only expanding wording. |

## What inflates max cost?

| Metric | High | Max |
|---|---:|---:|
| Input, including cached reads | 4,738,193 | 5,112,321 |
| Cached input | 4,132,736 | 4,215,936 |
| Uncached input | 605,457 | 896,385 |
| Output, including reasoning | 172,443 | 425,234 |
| Reasoning output | 41,654 | 273,383 |
| Visible output | 130,789 | 151,851 |
| Blocks | 291 | 325 |
| Prose words | 34,351 | 40,392 |

Max uses **6.56 times** the reasoning tokens, while visible output rises **16.1%** and prose words rise **17.6%**. Extra reasoning alone contributes **$11.5864**, or **74.1%** of the $15.6320 price difference. The remaining difference comes from visible output and input. Input figures accumulate repeated contexts across calls; they are not the size of the frozen page.

Rates are the [official Standard API pricing](https://developers.openai.com/api/docs/pricing) used by the benchmark: Astra $10/M uncached input, $1/M cached input and $50/M output. Reasoning is included in output, not billed a second time. No cache-write tokens were reported. Parent orchestration and review are excluded. These are API-equivalent estimates, not an account billing statement.

## What high can miss, and what max can lose

Max is most useful when it retrieves different source voices, concrete verse analyses, lexical witnesses or competing interpretations. A longer block, more written ledger rows or a more specific attribution does not by itself establish an improvement. Several families gain method applications or repeat material supplied by another family; those gains receive less weight in the default choices.

Max is not a superset. High remembers Ibn Arabi on the ontological path where max has no recall; Abduh on Ala and Bayyina where max cannot recall the details; and several unique hadiths and poetry witnesses. This benchmark is one run per family per effort on one verse, so model variation is mixed with the effect of reasoning effort. Confidence in the default allocation is moderate; repeat on another page before treating it as universal.

Concrete unresolved disagreements include the Diyanet wording for 5:16 in the meal outputs and the analysis of the ha in the kıraat material at p7. These require source checking; this comparison does not decide that max is right because it is more precise. The selected outputs remain drafts for later verification.

## Detailed new-family observations

### academic

Recommendation: max for a diverse academic literature layer.

**Useful max additions**

- p1 Nold eke/Schwally prayer speaker genre interpretation.
- p6 Watt Medina qibla community identity and Abdel Haleem face/person chapter.
- p7/11 Donner Believers inclusive early monotheist model.
- p9 Christian Lange eschatological bridge reception history.
- p20 Sinai Hanif Quran semantic context.
- p18 qawam; p21 hady/Izutsu eschatological return; p22 diplomatic gift.

**Useful material retained only in high**

- p1 Robinson Fatiha structure.
- p2 construction-aware Badawi Haleem account, max no_recall.
- p16 Izutsu rab/servant and ethico-religious network, max no_recall.

Donner model is a comparison to findings, not his specific singular/plural path interpretation. Sinai discussion relatively broad, not a newly recovered phonological argument. EQ/Zammit and qistas still not recovered. Additional named works/positions remain unverified.

### analytical

Recommendation: high default; max for exhaustive alternative interpretations.

**Useful max additions**

- p4 Ibn Jawzi two breasts alternative for the two najd.
- p5 Razi Rad13:7 hadi Allah vs prophet interpretations.
- p10 Ibn Jawzi Taha world/afterlife distinction.
- p16 named Abu Bakr and Umar interpretations instead of unnamed themes.
- p19 Razi knowledge/action failures and Qurtubi historical group reports directly address the Fatiha closing contrast.
- p20 Ibn Atiyya fitra as preparedness rather than innate detailed knowledge.

**Useful material retained only in high**

- p4 Alusi degrees and Ibn Jawzi Taha82 continued guidance.
- p10 Razi Duha ignorance vs unbelief.
- p13 Ibn Atiyya different kinds of losing or appearing to lose the way.
- p20 Alusi language nuances.

Both have 21 substantial blocks and all six author voices. Max adds real variants, especially p19, but much is shared or overlaps other families. Additional named positions remain unverified.

### grammar

Recommendation: high default; max selectively for dense morphology/complex multi-clause secondary findings.

**Useful max additions**

- p4 Abu Ubayda sawa al-sabil and Ibn Qutayba two najd explanations, high no_recall.
- p6 in lightened inne and distinguishing lam qibla emphasis.
- p17 Zeccac akabba vs kabba intransitive/causative morphology nuance.
- p20 Zeccac akwam implied feminine path and hal hanifan; Abu Ubayda/Ibn Qutayba Kahf word-order explanation.
- p21 Nisa175 siratan second object/ilayhi goal and participle construct indefiniteness.
- broader named works rather than mostly Samin.

**Useful material retained only in high**

- p6 Samin aata object-order alternatives.
- p11 Enam enne/inna syntactic attachment.
- p15 Cin lightened an/conditional/aim syntax instead of max semantic alternatives.
- p18 qawam/qi wam vowel explanation.

High already provides detailed technical i rab across20 blocks. Max gains are targeted rather than uniformly deeper. Both grammar outputs use ha al-sakt interpretation atp7; this does not resolve separate qiraat max pronoun alternative.

### historical

Recommendation: max.

**Useful max additions**

- p1 Ibn Hisham Abbas whisper vs Prophet not hearing variant in Abu Talib death.
- p5 Kalbi Sad idol startled camels and Ibn Hisham Amr ibn Jamuh helpless idol two specific histories.
- p6 distinct Bera afternoon vs Quba Ibn Umar morning transmission scenes.
- p10 Hums privileged exclusion of Arafat rite beyond trade background.
- p12 Wahidi/Suyuti Badr duel framing of Hajj22:19, high no_recall; alternative Ehlkitab tentative.
- p15 Zamzam rediscovery and Qusay rifada specific institutional histories.
- p19 Hilf al-fudul justice across tribal membership, high no_recall.
- p21 named Huleys mediator with hedy.

**Useful material retained only in high**

- p1 Itqan Fatiha Meccan/Medinan/twice-revealed opinions and Burhan distinction of sabab vs application.

Max p4 relocation of Ibn Urayqit story from high p5 is not a new discovery. Exact narrative variants remain memory-based; avoid treating greater specificity as verified history.

### imami-mutazili

Recommendation: max for balanced Imami and Mutazili source-family research.

**Useful max additions**

- p4 Qadi Tenzih specific Thamud verse analysis rather than generic justice/taklif framework.
- p8 Qadi Mughni tamkin vs lutf aid/agency distinction, high no_recall.
- p10 Mizan Duha pre-revelation ignorance vs kufr, high no_recall.
- p12 Qadi Tenzih Nisa hell-path interpretation and penal guidance.
- p15 Mizan mal/Kaaba as qiyam complements reward/trial.
- p9 jary framework distinguishes imam application from lexical definition.
- p22 separates initial benefaction, lutf obligation and deserved reward.

**Useful material retained only in high**

- p17 explicit Zamakhshari vs Mizan contrast in satanic authority.
- p18 Tabarsi ethical expenditure beyond amount, max replaces with tentative Mizan hand report.
- p19 explicit material/spiritual balance of wasat.
- p20 Kahf qayyim book explanation.

High already strong on Mizan levels, paths, imamate and technical lutf necessity. Additional Qadi source attributions unverified, not established correctness. Max tentative hand report should not be counted as certain recall.

### ishari

Recommendation: max if substantive tradition coverage is the aim; high remains viable for economical broad treatment.

**Useful max additions**

- p7 Sulami Adab al-suhba with age/peer duties instead of only general suhba.
- p9 Ghazali worldly moral path linked to eschatological sirat, high no_recall.
- p14 Herewi Manazil degrees/measure and divine sustaining, distinct source absent high.
- p15 Ibn Ataillah istidraj plus Ghazali gratitude/use of gifts, high no_recall.
- p19 Kashani zahir/batin two-sided veiling, more directly matches Fatiha closing balance.
- p20 Tustari Quran layers; p22 Kashani special gifts/knowledge/love.

**Useful material retained only in high**

- p12 Ibn Arabi Fusus Hud ontological path vs moral obligation; max no_recall.
- p4 Ghazali inner/outer travel.
- p8 talwin/tamkin.
- p18 Ghazali therapeutic counter-habit distinction.

Source expansion is useful but memory-based; extra named positions are not independently verified. Max is not a superset.

### kessaf

Recommendation: max.

**Useful max additions**

- p1 collective prayer/wasila Baydawi and guidance distinction.
- p2 Kashshaf Sad judicial-guidance explanation.
- p7 repetition of path as balagha and different companionship degrees.
- p8 actual Zamakhshari hawn modest walking explanation.
- p14 Kashshaf rain-parable stopped walking vs Hud perseverance, high no_recall.
- p15 mal and Kaaba qiyam source explanations.
- p17 Baydawi afterlife alternative for walking and Kashshaf Hijr guarantee interpretation.
- p19 Baydawi knowledge/action failure types directly address closing Fatiha groups.
- p21 Baydawi hedy Harem destination law.

**Useful material retained only in high**

- p2 tentative specific Abu Hayyan objection where max leaves preference unknown.
- p19 wasat justice/excellence.
- p22 direct hidaya-hediyya Baydawi connection.

Core hidaya/sebat/theology and destination contrasts already strong in high. Added passages are memory-based; differing strength of Abu Hayyan recall is not independently resolved.

### modern-coherence

Recommendation: high.

**Useful max additions**

- p11 actual Islahi Enam closing commands/authority analysis.
- p19 adds Bakara/Al Imran pair framing and more differentiated knowledge/will account.
- p22 actual remembered Hucurat ending vs high comparison from Fatiha.
- p16/20/21 expanded method applications.

**Useful material retained only in high**

- p11 Cuypers The Banquet/5:48 actual general scholarly reading absent max.

Written coverage gain 9 to13 partly comes from shared block relocation and general method applications. Max does not recover a specific Cuypers Fatiha or 5:16 scheme; high already preserves main prayer-response and qibla structure.

### modern-tafsir

Recommendation: high.

**Useful max additions**

- p4 Abduh Manar senses/reason/religion levels in addition to roster work.
- p5 Qutb Secde leadership patience and certainty.
- p12 Qutb Saffat scene and Asad Hajj, high no_recall.
- p13 Qutb Muminun truth versus desires, high no_recall.
- p19 Study Quran historical/general Fatiha closing groups.

**Useful material retained only in high**

- p3 Ibn Ashur continuation and increase.
- p4 Asad moral agency/two paths.
- p6 Abduh Amma Ala, max explicitly cannot recall this.
- p7 Ibn Ashur prior prophetic guidance versus legal details.
- p10 Asad Duha pre-revelation searching and general closing groups, max no_recall.
- p15 Ibn Ashur Kaaba qiyam.
- p19 Ibn Ashur wasat.
- p20 Abduh Amma Bayyina, max cannot recall this.

Max p14 repeats Qutb Hud perseverance largely already in high p16; written status gain is not a distinct new lexical explanation. Both strong on Qutb and Asad; high has useful roster-specific Abduh and Ibn Ashur details that max loses.

### poetry

Recommendation: max when lexical witnesses are central.

**Useful max additions**

- p1/3 Ibn Rawaha recez direct h-d-y plus plural help/sebat prayer.
- p2 Zuhayr actual h-d-y with ila rather than high thematic mediation parallel.
- p5 Imru al-Qays al-hadiyat actual leading animals lexical witness.
- p13 Antara muqawwam spear q-w-m witness instead of only shared Jarir road comparison.
- p14 Muthaqqib speaking exhausted camel from Mufaddaliyyat, high had no remembered item from collection.
- p19 Labid judgment not leaning with desire vs Amr intensified retaliation.
- p22 Labid divine apportionment vs Zuhayr reciprocal good.

**Useful material retained only in high**

- p3 Kab Banat Suad direct hidaya prayer.
- p5 Afwah actual h-d-y leadership phrase, max uses structural parallel only.
- p14 Shanfara aqimu opening direct q-w-m witness.
- p15 Antara well ropes and spears image.
- p4 Tarafa physical journey.

Both separate lexical evidence from literary parallels. Max correctly identifies Jarir as an Islamic-period witness; exact poetry wording, collection placement and source attribution remain unverified. Max gains match the lexical task but do not contain every high witness.

### qiraat

Recommendation: high default; max for complex syntax/apparatus or secondary passage discovery.

**Useful max additions**

- p7 preserved/dropped/vowelled ha plus ha al-sakt vs pronoun interpretation.
- p15 explicit reader distributions for 4:5/5:97.
- p20 explicit reader distribution qiyaman/qayyiman.
- p21 47:4 killed/fought changes subject/time of next guidance promise; 7:43 waw omission changes hamd clause, high no_recall.

**Useful material retained only in high**

- p9 Ruways/Yaqoub sin example.
- p17 Muhtasab aliyyun uncertainty preserved.
- p5 more alternative explanation of ungeminated yahdi.

p7 high dismisses new pronoun reading whereas max discusses pronoun analysis: a concrete disagreement requiring source checking, not proof that max is correct. Extra exact reader mappings are unverified. Core inventory and effects largely shared.

### rhetoric

Recommendation: high.

**Useful max additions**

- Kazwini Idah emir-as-prayer/iltifat p1, repetition/itnab p9, general tehakkum p12.
- p3/7/10/22 actual Kashshaf sebat, bedel, swallowed path and Hucurat inversion.
- more general methods p4/5/16 and sensory darkness-light contrast p11.

**Useful material retained only in high**

- p8 composite supporting-walker representation, max no_recall.
- p20 transfer/istiare of book/din/uprightness, max no_recall.
- p11 Rummani tasrif and Jurjani definiteness comparison.

Most added direct exegetical material overlaps max Kashshaf family. Actual Jurjani Yunus composite-representation example retained by both. Additional coverage of generic theory applications is not equivalent to newly recalled author-specific passage analysis.

### rivayet

Recommendation: max for wider early-source and variant coverage.

**Useful max additions**

- p4 Abdurrazzaq via Mamar/Qatada Beled plus Tabari two breasts alternative.
- p5 Rad hadi variant set including Ali report and Ibn Kathir reception of it.
- p6 prior qibla prayers not lost, more than direction-change story.
- p7 Muqatil specific Fatiha reading and Baghawi Thawban companionship anxiety.
- p9 Ibn Kathir Nuwwas road/walls/curtained doors parable.
- p12-13 Wajiz specific readings absent high.
- p14 Baghawi standing-person continuation analogy, high no_recall.
- p16 angel descent timing and Hud aging report.
- p21 literal hedy/Hudaybiya and paradise residents recognizing homes.

**Useful material retained only in high**

- p5 Ibrahim paternal call and received knowledge.
- p9 Baghawi readings of sirat.
- p20 explicit Mujahid and complementary Islam/Quran/right definitions.
- p22 Duha gratitude.

High already excellent on Tabari and Ibn Kathir; max improves breadth of the actual roster, not just length. Additional exact chains and judgments are recollected attributions, not independent authentication.

### turkish-tafsir

Recommendation: high.

**Useful max additions**

- p3/p10 Kuranyolu Duha pre-revelation knowledge distinction.
- p5 Elmalili Hud divine rule/justice and Kuranyolu Secde leaders patience.
- p16 Hud aged Prophet report and angel descent timing options.
- p20 fıtrat is not innate detailed doctrinal knowledge and Kahf qayyim book corrective function.

**Useful material retained only in high**

- p3 Fetih prophetic mission/community opening context.
- p15 explicit alternative disbelief/istidraj reading, max ledger leaves attribution uncertain without prose treatment.
- p19 wasat witness nuance.

Most full22-anchor content already strong in high. High p14 repeats broad perseverance instead of specific lexical finding; max rightly leaves no_recall. Max gains do not justify default premium for just two well-known works.

### wujuh

Recommendation: max for this cross-verse semantic-taxonomy task.

**Useful max additions**

- p3 huda as faith and its increase, high no_recall.
- p6 ilham/creation guidance, high no_recall.
- p7 huda as sunna/prophetic conduct rather than high discussion of nima.
- p10 dalal forgetting/loss examples.
- p16 tentative istiqama faithfulness taxonomy, high no_recall.
- p17 sultan proof/power taxonomy, high no_recall.
- p20 hanif Islam/hajj distinction.
- p22 mann benefaction vs claiming credit, high no_recall.

**Useful material retained only in high**

- p2 explanation vs grammatical construction; max no_recall.
- p7 nima Islam/prophethood category.

Several taxonomy verse/source mappings remain uncertain in both. p16 max explicitly tentative. Many blocks apply broad taxonomies rather than remembering a source treatment of the whole synthesis.

## Artifacts

- [Original four-family full paragraph comparison](ASTRA_DEEP_COMPARISON.md).
- [Machine-readable notes for the remaining 15 family pairs](ASTRA_FAMILY_REVIEW_NOTES.json).
- [Per-agent native usage](usage.csv), including input, cached input, output, reasoning and estimated cost.
- [Astra high assembled prose](../family-memory-astra-high-20261006/1_6.enriched.tr.md).
- [Astra max assembled prose](../family-memory-astra-max-20261006/1_6.enriched.tr.md).
- [87:6 Astra high benchmark](../../87_6/family-memory-benchmark-20261006/README.md).
- [S87 paragraph counts](S87_PARAGRAPH_COUNTS.md).

All three assemblies contain all 19 families and passed ledger/link checks. Removing enrichment blocks recovers the frozen prose byte for byte. Agents wrote to isolated lane directories. The observational search/cross-lane tool-input scan has no flags; it is not a filesystem access-control guarantee.
