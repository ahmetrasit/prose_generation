# Astra high versus max: what choosing high loses and gains

## Decision from this pilot

Astra high preserves substantive literature content at lower cost, but it loses some valuable research leads. The clearest max advantage is broader discovery and connection of material, particularly in beyânî and meal. High also contains useful source-specific contributions absent from max. Max is not a superset of high, and choosing high does not produce merely a shorter version of the same research.

For a cost-conscious baseline I would use high, with max reserved first for beyânî when breadth of literary precedent matters. Meal is the next strongest candidate for max when translator-specific narrowing and repeated choices are central. Hadith high already retains substantial report and commentary detail. Classical coherence has a mixed result rather than a clear quality winner.

If completeness of remembered leads matters more than cost, max adds material worth having. It still leaves major recall gaps and does not establish accurate attribution. The two runs disagree on some remembered wording.

## Scope and method

This review covers all 53 high blocks and 65 max blocks, both 22-row ledgers for each of the four families, and the complete frozen 22-paragraph prose including augmentations. It compares remembered source contributions, relevance to the actual findings, connections across paragraphs, differences between authors, scope discipline, uncertainty, and practical costs. The earlier report was a spot review; this report evaluates the complete outputs.

No literary, tafsir, hadith, or translation attribution was checked against an external text. The source descriptions below are summaries of what the agents claim to recall, not endorsements of those claims. Official OpenAI documentation was consulted only for model effort and price interpretation, not to verify research findings.

There is one independently generated run per family and effort setting. The prose and source rosters are byte-identical; the common brief differs in effort wording. The separate family launch instructions are paraphrases of the same purpose, not identical strings. Launch times, caching, tool behavior, and other concurrent work also differ. Therefore these are observed output differences, not proof that changing effort alone will reliably cause the same losses or gains on another page.

Raw outputs: [high page](../family-memory-astra-high-20261006/1_6.enriched.tr.md), [max page](../family-memory-astra-max-20261006/1_6.enriched.tr.md). Native accounting: [usage.json](usage.json), [usage.csv](usage.csv).

## Size, coverage, cost, and time

| Family | High blocks | Max blocks | High written paragraphs | Max written paragraphs | High words | Max words | High USD equivalent | Max USD equivalent |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Beyânî | 9 | 13 | 9 | 18 | 1,024 | 1,976 | 1.070228 | 2.031310 |
| Classical coherence | 7 | 9 | 9 | 10 | 723 | 958 | 1.037810 | 1.318620 |
| Hadith | 18 | 21 | 19 | 21 | 2,573 | 3,073 | 1.000888 | 1.947546 |
| Meal | 19 | 22 | 19 | 22 | 2,422 | 2,873 | 1.344820 | 2.806764 |
| Total | 53 | 65 | 56 | 71 | 6,742 | 8,880 | 4.453746 | 8.104240 |

Written-paragraph totals are family–paragraph locations out of 88 possible locations, not distinct paragraphs or findings. Shared blocks count at each linked location. Written status does not establish that all secondary findings in that paragraph were addressed. Prose words are measured from block text, not tool or ledger output. Retaining 76% of max's prose words is not evidence of retaining 76% of its knowledge or useful findings.

High saves $3.650494, about 45.0% of max's price equivalent. Max adds 2,138 prose words, 12 blocks, and 15 written family–paragraph locations. The coverage gain is concentrated in beyânî; five of its additional locations are handled by one shared methodological discussion rather than five separate remembered interpretations.

| Native token measure | High | Max |
|---|---:|---:|
| Input, including cached input | 1,019,238 | 1,142,932 |
| Cached input | 882,176 | 939,520 |
| Uncached input | 137,062 | 203,412 |
| Output, including reasoning | 44,019 | 102,612 |
| Reasoning output | 13,776 | 70,627 |
| Other output, including prose, tools, and ledger | 30,243 | 31,985 |

About 77.9% of the extra max cost is the extra reasoning output: 56,851 tokens at $50 per million, or $2.84255. Input accounts for another $0.720844; other output accounts for $0.08710. High's tool behavior included extra visible output in some families, so non-reasoning token totals are not a clean measure of final prose depth. Both efforts use the same per-token model rates; the observed cost difference comes from usage. These are Standard API equivalents, exclude parent orchestration, and are not account billing figures. [Official Astra pricing](https://developers.openai.com/api/docs/models/gpt-6-astra).

| Family | High recorded task duration | Max recorded task duration |
|---|---:|---:|
| Beyânî | 6m 22s | 15m 36s |
| Classical coherence | 5m 12s | 9m 57s |
| Hadith | 5m 52s | 16m 19s |
| Meal | 7m 58s | 22m 41s |

These are launch-to-final-event durations, including reading, writing, and checking. The slowest task in a parallel four-family run was about eight minutes for high and 23 minutes for max. Different execution conditions mean this is not a controlled latency estimate. Official guidance recommends using max when representative evaluations show that its quality gain justifies the extra time and cost. [OpenAI deployment guidance](https://developers.openai.com/api/docs/guides/deployment-checklist).

## Beyânî: the largest loss of breadth with high

Both efforts retain Sâmerrâî's concrete Fâtiha contributions: the worship–help–guidance sequence, plural prayer, the broad edatless request, continued guidance, the favored people, and singular sırât versus plural sübül. High therefore retains the core relevant reading; it is not merely a generic literary-method summary.

Max contributes several substantial additions. At paragraph 4, it connects Bintü’ş-Şâtı's Beled reading to the distinction between being shown a path and undertaking its difficult moral work. At paragraph 16, her Asr reading supplies belief, action, reciprocal counsel, and patience as a literary whole. These are stronger literary precedents than simply saying to compare Qur'anic usages. At paragraphs 20 and 21 it adds uncertain Sâmerrâî recollections concerning Tekvîr's movement/steadfastness/willing and Yûnus's unrestricted invitation versus qualified guidance. Those are useful leads, with uncertain source locations.

The shared paragraph-5 block is a different kind of gain. It contrasts Bintü’ş-Şâtı's contextual specificity with Sâmerrâî's allowance for multiple compatible meanings in suitable constructions, adding his et-Ta'bîrü'l-Kur'ânî as a remembered work. It connects this distinction to the input's front-leading guide, supported walker, swallowing, stasis versus ongoing movement, supporting implements, and balance imagery. That is useful for understanding how traditions might approach the synthesis. It is not a remembered source interpretation of all those images. The block itself acknowledges this. Its six paragraph anchors should not be treated as six separate discoveries.

High has valuable material absent from max. Its paragraph 10 gives a concrete Bintü’ş-Şâtı Duha reading of dalal as pre-revelation searching or not knowing the revealed way, rather than automatically treating it as polytheism or moral depravity. Max's shared method block at that location does not preserve that reading. High's paragraph 17 attributes a specific Mülk construction comparison to Sâmerrâî: upright walking and a straight road are both specified. Max substitutes an application of Hûlî's general psychological/literary method. High's paragraph 22 adds Sâmerrâî's active blessing/passive anger/participial straying contrast, alongside Bintü’ş-Şâtı on Duha. Max's block there focuses on Duha's consolation and duties.

Choosing high therefore loses Beled and Asr, uncertain Tekvîr/Yûnus leads, and a developed methodological contrast. It gains a more selective output and, in this run, several sharper direct readings. Max is preferable for broad discovery; high can be better in particular blocks. Neither effort recalls the whole lexical-image synthesis as the authors' own interpretation.

### Complete paragraph comparison: beyânî

| P | High contribution | Max contribution | What changes if choosing high |
|---:|---|---|---|
| 1 | Sâmerrâî: sequence, unrestricted help, plural prayer | Same core, fuller direct-address and communal connections | Mostly compression; core retained |
| 2 | Sâmerrâî edatless breadth; Bintü’ş-Şâtı word-choice method | Sâmerrâî breadth and application to Sâd; qualification against fixed rules | Different emphasis; high retains the main contribution |
| 3 | Sâmerrâî: persistence, growth, new situations | Same, linked to compatible meanings, later conduct and ambush | Extra synthesis reduced, core retained |
| 4 | Hûlî research program and Bintü’ş-Şâtı's usage method | Hûlî plus a concrete Bintü’ş-Şâtı Beled reading | Lose an important literary precedent |
| 5 | No recall | Shared method contrast on the root-image synthesis | Lose a framework application, not an actual image-chain source passage |
| 6 | No recall | No recall | No observed loss |
| 7 | Sâmerrâî: repeated sırât and favored persons; recalled Nisâ link | Sâmerrâî: favored people, communal prayer and companionship | Both substantive, emphasis differs |
| 8 | No recall | Shared method block, not a recalled hâdî–nasîr explanation | Lose limited methodological coverage |
| 9 | No recall | Recalled broad/open sırât image; Bintü’ş-Şâtı word-choice application | Lose a partly specific, partly methodological lead |
| 10 | Concrete Duha dalal reading by Bintü’ş-Şâtı | Shared root/association method discussion | Gain a sharper source reading; lose general framework |
| 11 | Sâmerrâî singular/plural and positive plural paths | Same core, expanded belirlilik and plurality distinctions | Modest compression |
| 12 | No recall | No recall | No observed loss |
| 13 | No recall | No recall | No observed loss |
| 14 | No recall | Shared method block on stasis versus ongoing movement | Lose methodological treatment, not direct precedent |
| 15 | No recall | Shared method block on supporting implements and water | Same limitation; no specific Cin interpretation recalled |
| 16 | No recall | Concrete Bintü’ş-Şâtı Asr reading related to sustained conduct | Lose an important comparative reading |
| 17 | Concrete Sâmerrâî Mülk construction reading | Hûlî method applied to emotion, walking, danger, and limitation | High is more source-specific here |
| 18 | No recall | Shared method block on balance imagery | Lose methodological coverage, no distinct recalled kavâm treatment |
| 19 | No recall | No recall | No observed loss |
| 20 | No recall | Uncertain Sâmerrâî Tekvîr reading | Lose a useful tentative lead |
| 21 | No recall | Uncertain Sâmerrâî Yûnus invitation/guidance reading | Lose a useful tentative lead |
| 22 | Sâmerrâî attribution grammar plus Bintü’ş-Şâtı Duha | Bintü’ş-Şâtı Duha, consolation, responsibility | Gain the grammar contribution; retain the Duha core |

Evidence: [high blocks](../family-memory-astra-high-20261006/bayani/blocks.jsonl), [max blocks](../family-memory-astra-max-20261006/bayani/blocks.jsonl).

## Classical coherence: smaller and mixed differences

High retains the substantive heart: Biqai's Fatiha purpose and worship–help–guidance progression, continued guidance, Fatiha/Nisâ's favored people, the Fatiha–Baqara request/response connection, and guidance as favor. Max develops prayer etiquette and the journey-to-return horizon more fully. Its one added written paragraph, 11, applies Biqai's remembered En'âm purpose to the one-path/many-paths relationship; it explicitly does not recall the exact combined comparison as his passage.

The most useful differences are different source leads, rather than uniformly deeper versions of the same lead. High paragraph 19 attributes the Fatiha-ending/Baqara/Al Imran sequence to Suyuti, relating the named groups to subsequent sura content. Max instead develops Biqai's knowledge/action distinction. High paragraph 21 recalls Biqai's local Yûnus transition from fragile worldly life to the abode of peace. Max recalls his A'râf treatment of arrival, guidance, and thanksgiving. Choosing high gains the local Yûnus coherence discussion while losing the A'râf-centered account; these are complementary.

Max more confidently attributes the Fatiha–Baqara link to Gharnati. High records that Gharnati's separate reasons do not clearly distinguish themselves from the general remembered framework. This confidence difference is not evidence that max is right. Both identify BIQAI and BIQAI-FULL as one work; the extra corpus ID is not extra scholarly coverage.

Max is only about $0.28 more expensive here, but this small premium still does not purchase a clearly superior set of leads. If one setting must be chosen, high is a reasonable baseline. Max is useful for additional depth and complementary ideas; neither supplies substantial remembered discussion for many lexical-image paragraphs.

### Complete paragraph comparison: classical coherence

| P | High contribution | Max contribution | What changes if choosing high |
|---:|---|---|---|
| 1 | Biqai purpose/sequence, plus Suyuti request-to-book transition | Biqai purpose/sequence and prayer etiquette; shared with 16 | Core retained; etiquette less developed |
| 2 | No recall | No recall | No observed loss |
| 3 | Biqai continued/increased guidance | Same, fuller realization and further understanding | Modest compression |
| 4 | No recall | No recall | No observed loss |
| 5 | No recall | No recall | No observed loss |
| 6 | No recall | No recall | No observed loss |
| 7 | Biqai Fatiha/Nisâ favored people | Same plus fuller companionship/application | Core retained |
| 8 | No recall | No recall | No observed loss |
| 9 | Suyuti Fatiha as opening into the book; shared with 20 | Biqai religious life/path/return horizon | Different source contribution |
| 10 | No recall | No recall; uncertain unexpanded swallowing lead in ledger | A tentative lead is lost, not written research |
| 11 | No recall | Biqai En'âm purpose applied to singular/plural paths | Lose a useful framework application |
| 12 | No recall | No recall | No observed loss |
| 13 | No recall | No recall | No observed loss |
| 14 | No recall | No recall | No observed loss |
| 15 | No recall | No recall | No observed loss |
| 16 | Shared Biqai worship/help/guidance block | Shared Biqai block, with more cross-verse application | Core retained |
| 17 | No recall | No recall | No observed loss |
| 18 | No recall | No recall | No observed loss |
| 19 | Suyuti Fatiha-ending/Baqara/Al Imran sequence | Biqai knowledge/action distinction | High gains a different specific coherence lead |
| 20 | Suyuti request/book relation; cautious general Gharnati recall | Fuller Suyuti relation, firmer Gharnati attribution | Less elaboration and less attribution confidence |
| 21 | Biqai Yûnus world-life/peace-abode transition | Biqai A'râf arrival/thanksgiving, then applied to Fatiha | Different useful local coherence readings |
| 22 | Biqai guidance and favor | Same, extended to additional ayat | Core retained |

Evidence: [high blocks](../family-memory-astra-high-20261006/classical-coherence/blocks.jsonl), [max blocks](../family-memory-astra-max-20261006/classical-coherence/blocks.jsonl).

## Hadith: high retains much of the detail, max adds real secondary material

High retains report settings, transmitter names, commentary reception, and differences between reports. It keeps the two forms of heart/sebat prayer, supported walking and congregational worship, the path parable and afterlife crossing, the status of the recalled thin/sharp addition, faith followed by upright conduct, house/banquet and Paradise-home imagery, and Nawawi's reconciliation of deeds and mercy. Choosing high does not lose these qualifications or turn the output into a bare list of hadith.

Max has important additional contributions. Paragraph 2 supplies the disputed-truth prayer and human-judgment report, connecting different grammatical requests and Davud's judicial scene. Paragraph 15 adds prayer as a supporting pillar, good wealth, and worldly gifts as a test. These address secondary findings high leaves unfilled. At paragraph 11 max distinguishes versions of the line-drawing teaching instead of treating them as one wording; at paragraph 19 it adds the commercial weighing report and vasat as justice; at paragraph 21 it connects actual hedy procedures to the destination image; at paragraph 22 it adds gentle teaching, directly addressing the input's lutf/incelik component. These are substantive gains, not just extra words.

High also retains independent useful leads that max does not. Paragraph 7 uses Ibn Abbas's David-prostration discussion as a concrete application of following previous prophets, where max uses best hedy and prophetic unity. Paragraph 12 gives Hudhayfa's harmful-guide/fitna account, where max uses truth and lies leading to opposite outcomes. Paragraph 19 adds the favoritism/Makhzumi legal example, which max omits. Paragraph 20 adds the Zayd b. Arqam book/light account and the Iyad b. Himar hanif-creation account, while max uses Jabir's pilgrimage wording and returns to the path parable. High paragraph 3 has the Hasan kunut prayer; max substitutes other continuing-guidance examples.

Thus max often better addresses the input's secondary components, while high retains a substantial and sometimes complementary report inventory. High has about 84% of max's prose words here at about 51% of its price. That is a strong observed tradeoff, not a claim about 84% of factual information. Max's added details also create more attribution checks.

### Complete paragraph comparison: hadith

| P | High contribution | Max contribution | What changes if choosing high |
|---:|---|---|---|
| 1 | Fatiha dialogue plus Nawawi; Abu Dharr guidance; Muadh help prayer | Same core plus Abu Talib/28:56 and more sources | Lose a concrete secondary guidance/agency report; gain stated Nawawi reception |
| 2 | No recall | Disputed-truth prayer with edats; Umm Salama judgment report | Important loss tied to grammar and Davud scene |
| 3 | Heart prayers and Hasan kunut | Heart prayers, Ibn Mas'ud prayer, communal Hendek words | Different continuing-guidance examples; both useful |
| 4 | Ali guidance/arrow prayer plus Nawawi, shared with 13 | Abu Bakr road/good-path double meaning; hired migration guide | Lose direct physical/religious language interplay; retain another concrete image |
| 5 | Warning guide plus caller/follower responsibility | Warning guide plus Haybar guidance through Ali | Different source lead, shared core |
| 6 | Quba and prior qibla prayers plus Nawawi's discussion | Same main reports without that stated commentary layer | Core retained; high adds reception |
| 7 | David prostration/following prior prophets; companionship | Best hedy, prophetic unity; companionship | Gain a specific following-prior-prophets application |
| 8 | Supported walker, Prophet's support, calm approach | Same report components | Little substantive loss |
| 9 | Path parable in fuller detail, crossing, cautious thin/sharp addition, Nawawi | Same two settings and cautious addition; extra attribution | High is detailed; no uniform max depth advantage |
| 10 | No recall | No recall | No observed loss |
| 11 | Main line/side lines and multiple Paradise gates | Also distinguishes Jabir variant; Irbad unity/continuity report | Lose transmission comparison and another unity precedent |
| 12 | Hudhayfa harmful guides plus caller responsibility | Truth/lies leading to Paradise/fire plus caller responsibility | Different concrete contribution, not a simple subtraction |
| 13 | Shared Ali guidance/arrow discussion plus Nawawi | Separate Ali discussion, preserving sedad distinction | Core retained; block count difference partly placement |
| 14 | Continuous deeds and Thawban | Same plus easy religion/paced journey imagery | Lose a useful bodily/pacing connection |
| 15 | No recall | Prayer pillar, good wealth, sweet/green world as trial | Important secondary support/wealth/test loss |
| 16 | Faith–steadfastness, Tirmidhi continuation, Nawawi | Same plus Qadi Iyad reception and grave firm-word account | Core retained; additional reception and afterlife connection lost |
| 17 | Satan on successive paths; face-down gathering | Same main reports | Little substantive loss |
| 18 | Salman rights and Sa'd bequest | Same plus Ka'b retaining some wealth after repentance | Lose another application setting |
| 19 | Just leadership, Makhzumi favoritism, Adi interpretation | Just leadership, commercial weighing, vasat testimony, Adi interpretation | Lose more literal scale/vasat links; gain favoritism example |
| 20 | Zayd book/light, Malik, Ali opening prayer, hanif creation | Jabir pilgrimage wording, Malik distinction, Ali prayer, path parable | Different valuable leads; max sharper on those wording variants |
| 21 | House/banquet and purification/home recognition | Same plus actual hedy procedures | Lose literal sacrifice-destination evidence |
| 22 | Hunayn favor, deeds/mercy, Nawawi | Same plus gentleness and a concrete teaching report | Lose direct attention to incelik/lutf |

Evidence: [high blocks](../family-memory-astra-high-20261006/hadith/blocks.jsonl), [max blocks](../family-memory-astra-max-20261006/hadith/blocks.jsonl).

## Meal: both useful, max better on some of the exact requested distinctions

High is already translator-specific. It compares Arberry's preposition and bodily imagery, Asad's explanatory choices, Turkish hidayet/ilet/sevk wording, witness/martyr language, relief versus peace, perseverance versus uprightness, and adding a destination to Fatiha. Its paragraph 16 supplies a remembered repeated Asad choice across 41:30 and 46:13. It is therefore wrong to say that only max reaches concrete translator patterns.

Max's best additions directly meet the user's purpose. Paragraph 2 compares TDV's showing with DIB's leading, and keeps the wording of Kur'an Yolu separate despite overlapping authorship. Paragraph 21 contrasts Suat Yildirim's divine destination with Mihr's specific soul-arrival doctrine, giving recalled examples at 3:73 and 6:71. Paragraph 15 contrasts preserving water imagery with replacing it by abundance/benefits; paragraph 18 identifies a Turkish middle-way expression even though the source has no road noun; paragraph 20 compares supplied road language with Asad's broader uprightness and adds a repeated hanif interpretation. These additions explain narrowing, shifts, and interpretive supplementation, rather than just commenting on the ayah.

High retains several useful contrasts absent from max. Paragraph 3 supplies Ali Fikri Yavuz's explanatory parenthesis about belief, speech, deeds, and morals. Paragraph 12 compares ezvac as spouses versus like-minded companions or counterparts. Paragraph 18 attributes Asad's spending to spending for others, compared with a broader Turkish wording. Paragraph 20 identifies Elmalili's recalled kıymetli yazılar against Asad's normative uprightness reading. These are source-specific and relevant to semantic shifts.

Some apparent coverage loss is relocation. High marks paragraph 14 no_recall, yet its paragraph 16 already discusses the 41:30/46:13 persistence distinction that max addresses at 14. Max's additional written paragraph is not wholly additional information. Conversely, high's no-recall at paragraph 5 leaves a guide/follow and hâdî discussion absent, though max's block is more about preserving components than demonstrating a distinctive translator contrast.

Neither run establishes a consistent translation-error series. Both distinguish interpretation or narrowing from error. Max uses more named roster entries, but some are edition variants or Turkish/English versions of one interpretive line. High uses 13 source IDs and max 20; this is not 13 versus 20 independent scholarly positions or proof of corpus coverage. Both explicitly leave many roster entries without specific recall.

### Complete paragraph comparison: meal

| P | High contribution | Max contribution | What changes if choosing high |
|---:|---|---|---|
| 1 | Prayer wording; Asad willing-subject example at 2:142 | Old/new Diyanet wording; Asad paired examples 28:56/10:25 | Lose version contrast and paired evidence; retain the interpretive issue |
| 2 | English syntax; Cantay/Ates/Golpinarli verbs; Asad Sâd explanation | TDV/DIB showing versus leading; Bulaç/Kur'an Yolu; English syntax | Lose a strong Turkish translator contrast; gain other verbs and Sâd detail |
| 3 | Ali Fikri Yavuz explanatory scope; guidance-then-protection | Elmalili/Bilmen/Mawdudi exposition; Asad increased guidance | Lose broader explanatory literature; gain a concrete annotated-meal choice |
| 4 | Term versus everyday verb; Asad journey/choice examples | More translators and DIB failure-to-follow examples | Both substantive; max broader roster |
| 5 | No recall | Arberry guide/follow; DIB hâdî | Lose component coverage with limited contrast between translators |
| 6 | Asad creation/purpose versus shorter Arberry | Asad creation/purpose plus DIB qibla limits | Lose fuller treatment of secondary qibla finding |
| 7 | Witness/martyr plus Asad sıddık interpretation | Witness/martyr plus companionship and prophetic guidance | Core retained; different secondary emphasis |
| 8 | Guidance/help, Arberry movement versus DIB humility | Guidance/help, TDV humility versus Asad gentle movement | Similar issue through different sources |
| 9 | Road/bridge, path/way, Y. N. Ozturk moving-road wording | Road/bridge, Y. N. Ozturk, DIB sırât/tarîk merger | Lose a specific lexical distinction flattened by translation |
| 10 | Arberry/Asad/Elmalili Duha; cautious unidentified gloss | DIB Fatiha/Duha contrast and sapıklar connotations | Different translator leads; max directly addresses Turkish connotation risk |
| 11 | English peace versus recalled DIB/TDV salvation; plurality | DIB esenlik versus TDV kurtuluş; plurality | A direct DIB recollection disagreement remains unresolved |
| 12 | Ezvac spouses/companions/counterparts; negative destination | Guide used for bad destination; Hamid expansion | Gain a specific ezvac comparison, lose another repeated guide example |
| 13 | No recall | Arberry straight/go straight versus Asad right course | Lose a concrete translation-family relation |
| 14 | No block, but related repeated Asad evidence at 16 | Asad persistence at 41:30/46:13 | Some apparent loss is placement, not missing content |
| 15 | Asad water/bounty interpretation and wealth support | Arberry water versus Asad benefits; DIB wealth/Kaaba functions | Lose fuller imagery/translation-layer contrast; layer disagreement needs checking |
| 16 | Paired Asad persistence; uprightness; Hûd limits | Elmalili worship versus DIB kulluk; worship/path repetition | Lose a useful worship vocabulary contrast; gain a clear repeated Asad pattern |
| 17 | Arberry imagery; Hicr attribution left unresolved | DIB/TDV arrival versus Arberry for Me at Hicr | Gain caution, lose a precise but unchecked translator attribution |
| 18 | Asad spending for others versus general spending | DIB middle-way addition versus Asad just mean | Gain one narrowing lead, lose another road-language addition |
| 19 | Asad broader balance and middle community | DIB upright/just language; Asad moral-accountability note | Different useful layers |
| 20 | Persistent true faith; Elmalili kıymetli yazılar comparison | Supplied road versus broad uprightness; paired hanif interpretation; DIB rulings | Gain one specific Elmalili lead, lose other precise expansion patterns |
| 21 | Suat Yildirim destination; peace abode and thanks | Also Mihr narrowing with two examples; literal hedy destination | Lose one of max's strongest narrowing patterns |
| 22 | Human favor versus divine favor; Asad mercy gift | Also Arberry surrender/belief distinction and TDV favor | Lose a useful distinction within the supplementary verse |

Evidence: [high blocks](../family-memory-astra-high-20261006/meal/blocks.jsonl), [max blocks](../family-memory-astra-max-20261006/meal/blocks.jsonl).

## Gains from choosing high beyond price

High produces less material to read, edit, and later verify, though the time saving was not measured. Its selective beyânî output avoids assigning a general method discussion to many root-image paragraphs. In several places it keeps a specific source reading where max substitutes broader application. It also makes useful conservative decisions: Hicr 15:41 translator assignments remain open, Gharnati's independent rationale remains unclear, and the ledger explicitly avoids turning remembered tafsir into precise meal wording where that distinction is not recalled.

Those choices reduce unsupported precision; they do not prove that high's actual attributions are more accurate. High also misses useful material that max recalls. Its stricter no-recall boundary sometimes requires memory of the entire synthesis even though component literature would be relevant. The output differences therefore reflect both recall and different thresholds for what merits a block.

## What max does not solve

Max supplies neither external verification nor exhaustive source coverage. Both efforts still lack direct remembered precedent for many distinctive lexical-image chains: swallow/sword/road, frozen water versus continuing movement, pulley/sword grip/water, coin/noonday balance, and the complete bride/sacrifice/protected-arrival synthesis. Max often discusses components or methodological approaches, correctly labelled, instead of recalling a source that combines the whole chain.

The DIB 5:16 disagreement is explicit: high attributes kurtuluş yolları to DIB as well as TDV; max attributes esenlik yolları to DIB and kurtuluş yolları to TDV. The runs also present Asad's Cin 72:16 water image differently: high retains it and discusses explanatory interpretation, while max says the translation replaces it with benefits. Translation versus note or edition may explain the latter, but the correct layer was not checked. More confident details are therefore useful leads and possible errors at the same time.

## Practical choices using the observed complete-family costs

| Choice | Four-family price equivalent | Saving versus all max | Main expected tradeoff from these outputs |
|---|---:|---:|---|
| All high | $4.453746 | 45.0% | Strong core, less discovery breadth, some unique high leads |
| Max beyânî; other three high | $5.414828 | 33.2% | Restores Beled/Asr and broader literary connections; meal-specific max leads still absent |
| Max beyânî and meal; high coherence and hadith | $6.876772 | 15.1% | Restores the two largest discovery advantages; misses some secondary hadith/coherence material |
| All max | $8.104240 | — | Broadest observed coverage, more review work, still not a superset of high |

These are substitutions of existing complete-run prices, not estimates for new supplements. A high-first run followed by a tightly specified max search for missed source contributions is a plausible workflow, but has not been tested here. Its cost and ability to recover these exact omissions are unknown. No new agents or runs were started for this comparison.

My judgment is to distinguish economical production from maximum discovery. High is a strong economical baseline. Max buys worthwhile additional research leads, especially literary precedents and translator-specific patterns, but not guaranteed correctness or uniform depth. If the goal is to discover as much remembered literature as possible, an independent additional pass may also matter: the high-only contributions show that one max run does not exhaust even the material recalled in these eight tasks.
