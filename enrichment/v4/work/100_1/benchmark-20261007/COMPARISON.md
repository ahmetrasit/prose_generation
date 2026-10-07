# 100:1: four-family decision benchmark

All 16 fresh agents completed. For this frozen 100:1 input, the single winner in **each of the four tested families is Sol max with the local corpus**. The selected four outputs cost **$6.648597**; running all four configurations for the comparison cost **$24.991561**. These are Standard API-equivalent agent estimates, excluding parent preparation, review and assembly.

This changes the provisional 1:6/87:6 preference for rivayet, historical and poetry on this test. It reinforces the corpus preference for meal. It does not establish new winners for the other 15 families or replace the approved Astra memory-only allocation. Model and evidence access both change across Sol/Astra: this is a workflow comparison, with reasoning effort isolated only within each model/evidence pair.

## Scope and review

The input is the same augment2 frozen prose in all lanes: 22 paragraphs, 2,909 whitespace-delimited words. Four agents per lane handle rivayet, historical, poetry and meal. Sol high/max use only the assigned local corpus, including bounded keyword discovery. Astra high/max use learned recall, without corpus, repository or web search. No agent sees another lane's output. Native sessions confirm the requested model/effort, fresh contexts and completion; the saved policy checks flag no prohibited tool use.

The parent read all 258 blocks and their ledgers, compared concrete source contributions and important omissions, and checked selected decisive memory claims against available originals. Every agent supplied all 22 paragraph decisions (352 total). All four assembled prose files preserve the original frozen bytes. Block counts, prose length and number of source IDs describe coverage; they do not measure accuracy. Extra memory works outside the corpus remain eligible leads, with availability and uncertainty recorded.

There are 519 corpus evidence anchors. The completed raw outputs had 14 exact-anchor failures: six in Sol high and eight in Sol max. Parent repairs affect quote wording or minimum quote length, leaving prose and ledgers unchanged. Two initially apparent failures are valid quotations in substantive corpus headings exposed by the read helper; validation now accepts either exposed heading or body. A seventeenth preliminary issue was already corrected by the agent before the completed raw snapshot. Original outputs and before/after audits are retained. Passing the anchor check does not establish that every interpretation or attribution is correct.

## Costs and tokens

| Configuration / evidence | Four-agent cost | Cumulative input | Cached input | Output including reasoning | Reasoning output | Blocks |
|---|---:|---:|---:|---:|---:|---:|
| Sol high / corpus | $4.513840 | 14,206,195 | 13,683,584 | 73,190 | 26,157 | 64 |
| Sol max / corpus | $6.648597 | 21,005,142 | 20,293,376 | 116,639 | 60,174 | 72 |
| Astra high / memory | $4.443538 | 1,045,058 | 933,888 | 47,959 | 14,203 | 55 |
| Astra max / memory | $9.385586 | 1,212,525 | 1,015,296 | 127,960 | 80,444 | 67 |
| **All 16 agents** | **$24.991561** | **37,468,920** | **35,926,144** | **365,748** | **180,978** | **258** |

Input is the sum across model requests, including repeatedly cached context. It is not unique text loaded once. The largest individual request was Sol max meal at 245,015 input tokens; no request crossed the 272,000-token pricing boundary. Cache reads account for 96.3% of Sol high input and 96.6% of Sol max input. The corpus agents make substantially more source-reading calls, but cached reads and Sol's lower rates keep the cost moderate.

Astra max's output costs $6.398 of its $9.386 total; 80,444 reasoning tokens are included in output. Max raises Astra cost by 111.2% over high. Sol max raises cost by 47.3% over high, with substantive gains described below. These single-run ratios are observations, not forecasts for all ayat. The observed four-family 1:6 reference was $23.016077; this full comparison is about 8.6% higher.

| Family | Sol high corpus | Sol max corpus | Astra high memory | Astra max memory | Winner |
|---|---:|---:|---:|---:|---|
| Rivayet | $0.981518 | $1.526024 | $1.004874 | $2.345960 | **Sol max corpus** |
| Historical | $0.935139 | $1.140643 | $0.847470 | $2.068456 | **Sol max corpus** |
| Poetry | $0.772462 | $1.737111 | $0.928368 | $2.052214 | **Sol max corpus** |
| Meal | $1.824721 | $2.244819 | $1.662826 | $2.918956 | **Sol max corpus** |

Full per-agent native input, cached/uncached input, output, reasoning, session ID and cost are in [AGENT_COSTS.md](AGENT_COSTS.md), [usage.csv](usage.csv) and [usage.json](usage.json). Saved benchmark rates per million tokens are Sol $2 uncached/$0.20 cached/$10 output and Astra $10/$1/$50. Pricing provenance is retained in usage.json; estimates do not claim actual account billing.

## Rivayet: Sol max corpus

**Sol high's strengths:** it retains the competing horse/pilgrimage-camel readings, Tabari's horse preference, rare sound definitions, the fox explanation, fire-related dabh, and the competing readings of fire-making. It preserves an important horse-count variant: Ali's Badr argument has two horses in one transmission and one in the Durr version. It also gives concrete expedition narratives and flags Ibn Kathir's reservation about the occasion report. These are source-specific findings rather than a generic consensus summary.

**What Sol max gains:** it reads Abd al-Razzaq's full 51-opening sequence; adds Yahya b. Sallam's independent 16:7 explanation and Mujahid's 43:13 horses reading; extracts Tabari's explicit adawtu/jawaza explanation for 18:28; and preserves Thalabi's unusual Ali report in which the returned object in the Solomon scene is the sun. That last report is visible at `THALABI:v8p200`, alongside Tabari's stroking preference and Baghawi's cutting preference. Twelve corpus source IDs contribute, versus ten in high. Max does lose high's one-horse Durr variant; it is not a superset.

**What Astra high contributes:** especially useful author-specific links in the secondary verses. Its Ibn Kathir 16:9 transition from physical travel to spiritual roads is real (`IBNKATHIR-FULL:v4p560`) and is missed by both corpus Sol runs. It also explains Ibn Kathir's resistance to treating the peace verse as unconditionally abrogated and the difference between Tabari's and Ibn Kathir's treatment of the horses. Recall is concentrated in five familiar works, with explicit gaps for rare lexical material and several early witnesses.

**What Astra max gains over high:** a verified Tabari/Ibn Kathir disagreement over 81:17 (night withdrawing versus arriving), clearer named report layers, Ibn Kathir's weakness assessment of the elevated Abu Umama kenud report, and more secondary-verse context. The 81:17 preferences check against `TAB-FULL:v24p161` and `IBNKATHIR-FULL:v8p337#2`. It still cannot recall the direct fire-related dabh material, the dabh/dabʿ relationship or Tabari's lexical bridge used by Sol max. Qualified Thalabi/Abd al-Razzaq leads are left open rather than turned into independent findings. Its more careful prose does not recover the missing source breadth.

**Decision:** Sol max is the best standalone extraction of this family's relevant corpus findings, at $1.526. Choosing Sol high saves $0.545 and retains valuable variants, while giving up several independent witnesses. Choosing Astra max preserves excellent Ibn Kathir connections but loses important lexical/source findings and costs $0.820 more than Sol max. The winner still needs an omission check for Ibn Kathir's 16:9 link and the Durr horse-count variant.

## Historical: Sol max corpus

**Sol high's strengths:** concrete occasion narratives; Suyuti's dating argument; TDV's style/topic dating; Corpus Coranicum's Sinai/Neuwirth treatment of early oaths; the 2 Clement parallel; Ibn Hisham's three named Badr horses; Hubal/lot-arrow and Suraqa material; and camel transport/market evidence. It separates modern TDV applications involving vehicles and firearms from ancient history. The independently different one/two/three horse counts are a useful report/source problem to preserve.

**What Sol max gains:** exact separation of the Mundhir raid narrative from the Bir Mauna episode; the Khaybar dawn example; Azraqi's pilgrimage timing and Quzah beacon; Ghatafan's raid as a counterexample to automatically assigning moral value to horsemen; the explicitly weak Abu Umama report in Itqan; and, most decisively, competing elite-person narratives and Ibn Kathir's chronological objection around 18:28/6:52 (`SUYUTI-LUBAB:v1p101`). These gains cost only $0.206 beyond high. Max misses high's named three-horse witness and some other concrete material, so selection should preserve those in a later curated merge.

**What Astra high contributes:** helpful context beyond the immediate sura—Uhud, Tabuk, Hums pilgrimage rules, the hijra guide, and Hudaybiyya/umrat al-qada. The last is verified in Wahidi's adjacent 2:194 section at `WAHIDI-ASBAB:v1p55#2`, which both corpus agents missed. A verse-index lookup misses that embedded section, while keyword search finds it. Several other leads remain unverified in this targeted review; a failed keyword query is not grounds to call them false. It has no secure sura-specific Corpus Coranicum recall.

**What Astra max gains over high:** more explicit separation of dating from occasion claims, an Imami Ali/Zat al-Salasil account kept distinct from Ibn Hisham's Amr b. al-As campaign, rotating camel use at Badr, and a wider set of qualified contextual works. It also gives a careful Razi/Tabari reception contrast for Solomon. This extends historical and reception context, but leaves the concrete Corpus Coranicum comparisons and several locally available rare details unrecovered. It often contributes applications from familiar general history rather than newly documented paragraph-specific source disputes.

**Decision:** Sol max offers the most useful combination of specific evidence, chronology and qualified disputes at $1.141. Astra high is a useful inexpensive lead generator at $0.847, but loses the concrete comparative scholarship and some decisive source-specific checks. Astra max's $2.068 adds breadth of remembered context without overtaking Sol max's documented details. The Sol winner still misses the available Wahidi 2:194 context and high's Badr details.

## Poetry: Sol max corpus

This family exposes the largest difference between familiar thematic recall and direct lexical witness recovery.

**Both Sol runs find three decisive direct witnesses:** Salama b. Jandal's al-adiyat with explicit horses (`MUFADDALIYYAT:v1p119`); Tarafa's asfar madbuh, with Zawzani's gloss of a heat-treated gaming/lot stick (`MUALLAQAT:v1p119#4`); and al-Muthaqqab al-Abdi's kenuduha in a patron/gratitude context (`MUFADDALIYYAT:v1p149`). Both Astra runs miss these particular witnesses. Honest no-recall entries are appropriate, but the omitted findings materially limit the requested research.

**What Sol max gains over high:** Asmaiyyat's suppressed horse-breath image; distinct foreleg/movement vocabulary; ash as a generosity image; Marzuqi's explicit 2:194 citation distinguishing aggression from recompense (`HAMASA:v1p549#2`); a naqʿ gloss that means noise in a particular context rather than dust; multiple adiya/awadi witnesses; and exact safun/musawwama horse posture/marking material. It preserves uncertain poem attributions where the source does. These are substantive additions, although max misses high's chest-noise example. Its $0.965 increment is the largest Sol effort increment in this pilot.

**What Astra high contributes:** the Imru al-Qays consecutive two catches with Zawzani's gloss, directly verified at `MUALLAQAT:v1p71#2`. Both corpus agents miss it even though the frozen paragraph already points toward this scene. High also brings useful familiar horse/camel images and distinguishes thematic parallels from root attestations. It does not recover the available madbuh, kenud or explicit al-adiyat examples, and has no secure Asmaiyyat recall.

**What Astra max gains over high:** the sabihat movement adjective, a Shanfara hard-ground/fire-striking lead, Zuhayr's record/accountability comparison, and the Hamasa nufus=blood passage at paragraph 17. The last is verified at `HAMASA:v1p87`; both Sol runs leave that paragraph without a finding. The Asha k-n-d witness is explicitly qualified and remains unverified because its named Diwan is outside the assigned available poetry works. Max still says it has no direct recalled dabh witness and does not recover the three decisive corpus witnesses above. It expands to 17 blocks/19 written paragraphs, compared with Sol max's 18 blocks/18 written paragraphs; that numerically wider paragraph coverage does not reverse the lexical result.

**Decision:** Sol max best satisfies direct lexical witnesses plus actual commentator glosses, at $1.737. Sol high at $0.772 is exceptionally good value if fewer secondary findings are acceptable; it retains the three core witnesses. Astra high preserves a valuable hunt gloss. Astra max adds useful nufus and context material, but at $2.052 still misses the central direct witnesses. The winner requires a targeted pass for the Imru al-Qays hunt and Hamasa blood gloss.

## Meal: Sol max corpus

**Sol high's strengths:** 26 cited corpus identities and concrete additions/narrowings: horses, hoof explanations, Hamidullah's mares, Akgul's modern vehicles, Islamoglu's human/anger reading, and Suleymaniye's old/current differences. It preserves source/version distinctions and grouped-verse structure. Its original/simplified Elmalili 38:32 wording comparison is useful, but the claim that the direction changes needs qualification: wording such as “Rabbimi anmaktan ötürü tercih ettim” alone does not conclusively establish a negative moral reversal. That caution is retained separately from anchor validation.

**What Sol max gains:** repeated patterns within a translator: Suleymaniye's human-nefis choices across openings, Shems's chest/heart distinction, and Ozdemir's breath/self expressions and crossing vocabulary. It adds Cahit Yildirim's explicit camel alternative, Kuntman's riders' campfire interpretation, and a precise English-to-Turkish Asad acoustic shift: English 7:176 panting becomes Turkish hirlar (`ASAD-EN:7:176`, `MEAL-ESED:7:176`). It does not promote one lexical shift into a proven recurrent translation error. It cites 29 corpus identities. Its $0.420 increment buys concrete findings directed at the family's stated purpose.

**What Astra high contributes:** readable comparisons among familiar DIB, TDV, Elmalili, Asad and Arberry texts; useful Asad 18:28 causal wording, verified against both English and Turkish originals; and Mawdudi's horse-service/ingratitude reception as a lead. Its recall reaches seven identities and misses several edition-specific and repeated translator patterns recovered by the corpus runs. More seriously, paragraph 21 assigns TDV a preference for forgetting remembrance and striking the horses. All three available TDV witnesses contradict the remembrance attribution; the official grouped text and DUZ copy also explicitly say stroking.

**What Astra max gains over high:** more disciplined original/translation and edition separation, clearer root distributions across verses, and a careful ledger admitting many unknown roster identities and insufficient examples for a recurrent-error claim. It still repeats the wrong TDV motive attribution. Max does not repeat high's striking claim, but the remaining error alone affects the proposed contrast. At paragraph 16 it additionally remembers Turkish Asad 16:8 as future yaratacak; the available Koytak–Erturk text says yaratmaktadir. The English will yet create clause is correct, so the error is precisely in assigning the tense to the named Turkish witness. This is a second concrete memory attribution failure, not a general claim about every edition.

**Decision:** Sol max wins at $2.245 for actual wording, repeated translator patterns and edition coverage. Sol high costs $1.825 and captures much of the major interpretive landscape. Astra high costs $1.663 but loses the rare translator/version findings and introduces a material TDV error. Astra max costs $2.919, still cites seven identities, fails to fix the TDV contrast and adds the Turkish-tense error. Max reasoning did not ensure factual attribution here.

## What this changes in the workflow decision

For these four families on this input, use Sol max corpus as the standalone baseline. Sol high saves $2.134757 overall (32.1%) and is credible when narrower finding coverage is acceptable, particularly in poetry. The cost premium for Sol max is supported by specific source gains in all four families; it also has real omissions.

Memory recall remains useful for finding connections that corpus discovery misses: Ibn Kathir's physical/spiritual roads, Wahidi's embedded 2:194 context, Imru al-Qays's consecutive hunt and the Hamasa nufus gloss. A later targeted memory-lead pass followed by source verification is worth testing, but this run does not measure the cost or quality of that hybrid. No extra agents were run for it.

The lesson is to judge a workflow against the family's research purpose. For direct poetry witnesses and translator/version wording, source access mattered more here than additional memory reasoning. For tafsir connections and wider historical context, memory supplied valuable gaps. Neither high/max pair is a strict superset, and no combination in this pilot recovers every substantial available finding. This single unreplicated case strengthens the four local decisions; it cannot determine all 19 family winners universally.

## Artifacts

- [Decision and limitations](DECISION.json)
- [Per-agent cost ledger](AGENT_COSTS.md), [CSV](usage.csv), [native usage metadata](usage.json)
- [Targeted semantic checks](MEMORY_CLAIM_CHECKS.json)
- [Corpus semantic review notes](CORPUS_SEMANTIC_REVIEW.json)
- [Raw corpus blocks/ledgers](RAW_CORPUS_OUTPUTS.json), [raw anchor audit](RAW_SOURCE_ANCHOR_AUDIT.json), [parent quote corrections](PARENT_ANCHOR_REVIEW.json), [final structure/anchor audit](SOURCE_ANCHOR_AUDIT.json)
- [Sol high enriched prose](../corpus-sol-high-20261007/100_1.enriched.tr.md), [Sol max enriched prose](../corpus-sol-max-20261007/100_1.enriched.tr.md)
- [Astra high enriched prose](../../../../v3/work/100_1/family-memory-astra-high-20261007/100_1.enriched.tr.md), [Astra max enriched prose](../../../../v3/work/100_1/family-memory-astra-max-20261007/100_1.enriched.tr.md)
