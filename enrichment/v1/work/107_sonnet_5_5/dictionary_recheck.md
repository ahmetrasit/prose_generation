# S107 enriched commentary: lexical re-check against the project dictionary

Input (read-only): `enrichment/v1/out/107/107_enriched.sonnet-5-5.md`
Dictionary (read-only): `enrichment/v1/corpus/dictionary_agent/agent/` (ladder: START_HERE -> roots.min.json/aliases shards -> card.md -> routes.min.json -> branches.select.min.json + branch/*.source.json -> occurrences.compact.json). `root_packets/<id>.json` was opened only to read the quoted lexicon text of root_000477 (دع), to confirm the "pushing from his right" and Mufradat origin statements.
Also used (not the dictionary): the cached Maqayis pages in `work/107_sonnet_5_5/sources/maqayis_*.txt`, only to cross-check quotations where the dictionary is silent.

Verdict counts (44 rows): SUPPORTED 18, PARTLY 10, NOT FOUND IN DICTIONARY 13, CONTRADICTED 1, DICTIONARY SILENT 2.

## 1. Root resolution (every candidate inspected; matched one in bold)

The agent export has 1679 roots (manifest). Two roots the commentary depends on are not in it.

| Requested | Candidates inspected (root_id, root) | Matched | Notes |
|---|---|---|---|
| كذب | root_001290 ك ذ ب | **root_001290** | QAC 107:1:3:1 يُكَذِّبُ; 9 branches; Maqayis route exact |
| يتم | root_001692 ي ت م | **root_001692** | QAC 107:2:4:2; 5 branches |
| دع / دعع | root_000477 د ع ع; root_000478 د ع و (card only) | **root_000477** | QAC 107:2:3:1 يَدُعُّ lemma/root د ع ع. Maqayis, Ayn, Mufradat, Tahdhib are routed to it as variants (headword دع); Sihah exact. root_000478 (calling/claiming, دعاء) rejected |
| حض / حضض | root_000334 ح ض ض; root_000293 ح ث ث (comparison for hass) | **root_000334** | QAC 107:3:2:1 يَحُضُّ. Maqayis headword حض routed as variant. No root "ح ض" exists separately |
| طعم | root_000934 ط ع م | **root_000934** | QAC 107:3:4:1 طَعَام; 14 branches |
| مسك / سكن (miskin) | root_001424 م س ك; root_000726 س ك ن | **root_000726 س ك ن** | QAC 107:3:5:2 مِسْكِين -> س ك ن. م س ك B013 states "ليس المسكين"; م س ك has no 107 occurrence |
| سهو | alias shards u0633-u0647 (only س ه ر/ل/م), roots.min.json, lookup shards, all 1679 packets | **NONE** | root س ه و does not exist in the dictionary. Candidates by folding: none. Related roots opened for semantics only: root_001097 غ ف ل, root_001382 ل ه و (and ل ه ي root_001383 listed by folding, not opened) |
| صلي / صلو | root_000879 ص ل و; root_000880 ص ل ي | **root_000879 ص ل و** for 107:4 and 107:5 (QAC 107:4:2:3, 107:5:4:1) | ص ل ي (000880) carries the same fire/prayer branches and is the QAC root of Qur'anic fire verbs (69:31, 83:16, 92:15, 4:10) |
| رأي | root_000531 ر ء ي; root_000615 ر و ي | **root_000531** (QAC 107:1:1:2, 107:6:3:1) | ر و ي is a weak-fold candidate; its B009 (الرواء) is only Mufradat's unhamzed analysis. Rejected |
| منع | root_001448 م ن ع | **root_001448** | QAC 107:7:1:2 |
| معن | roots.min.json fold of م ع ن; aliases u0645-u0639 shard (م ع ز root_001433, م ع ع root_001434, م ع ي root_001435 only); string search "ماعون" over all cards and branch files = 0 hits | **NONE** | root م ع ن does not exist. root_001064 ع و ن (a'āna) opened for the derivation claim; root_001458 م و ه (water) opened for the "māʿūn = water" claim |
| دين | root_000504 د ي ن; root_000502 د و ن | **root_000504** (QAC 107:1:4:3) | د و ن is a fold candidate, rejected |
| ويل | root_001689 و ي ل; also fold hits root_000067 ء و ل, root_001616 و ء ل (opened, unrelated) | **root_001689 و ي ل** | exists (2 branches) but QAC links NO Qur'anic form to it (occurrences = {}); no Maqayis route (covered_by: ayn;sihah;tahdhib;mufradat) |
| Other roots touched | root_000637 ز ك و, root_001382 ل ه و, root_001097 غ ف ل, root_001064 ع و ن, root_001458 م و ه | n/a | used as supporting context only |

Occurrence check for the 107 words: ح ض ض, ط ع م, ر ء ي (x2), ص ل و (x2), ك ذ ب, س ك ن, د ي ن, م ن ع, د ع ع, ي ت م are all linked. وَيْل, سَاهُونَ, الْمَاعُونَ have no QAC-linked root in the dictionary.

## 2. Claim-by-claim

Verdict codes: S = SUPPORTED, P = PARTLY, NF = NOT FOUND IN DICTIONARY, C = CONTRADICTED, SIL = DICTIONARY SILENT. Branch ids are from the dictionary; "src" = lexicons recorded on that branch.

| # | Block | Claim | Dictionary evidence | V |
|---|---|---|---|---|
| 1 | NOV-001 | mirror, "er-riyyu/ruwa' = beautiful appearance", lexical material (Maqayis and others) | ر ء ي B006 (src ayn, maqayis, mufradat, sihah, tahdhib): "الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)"; "الري ما أريت القوم من حسن الشارة (ayn)". B012 "رأيت الرجل ترئية إذا أمسكت له المرآة" is Tahdhib only. Note the Maqayis form is الرئي (hamza), الري is Ayn | S |
| 2 | NOV-002 | kezzabe cloth and "interrupted motion" idioms (attack, milk, wild animal) exist as lexical material | ك ذ ب B009 "الكذابة ثوب يكذب بحاله" (ayn, mufradat only, not Maqayis); B004 attack (maqayis, jamhara, sihah, mufradat); B006 milk (maqayis marks it "فيه نظر وقياسه صحيح"); B007 wild animal is single-source jamhara | S |
| 3 | MEAL-002 | "baz metindeki Maqayis tanimi (kezib soz ve fiil icin soylenir)" | ك ذ ب B001: "يقال في المقال والفعال (mufradat)". The Maqayis phrase on that branch is only "الكذب خلاف الصدق (maqayis;jamhara)". The content is supported but the source label is wrong: the "speech and deed" definition is Raghib's Mufradat, not Maqayis | C (label) |
| 4 | SEM-001 | ed-din range: hesap/ceza, din/Islam, itaat (Razi: boyun egis) | د ي ن B002 "يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)", "الدين الجزاء والمكافأة (sihah)"; B001 "الطاعة والانقياد ... الملة والشريعة" (maqayis: "فالدين الطاعة"). Branches the commentary does not use: B004 الإذلال والملك, B005 العادة والشأن, B006 مدينة, B007 التديين | P |
| 5 | SEM-008 | din=itaat (Maqayis) and din=karsilik/odeme are separate classical branches; "borc/defter" is a project image | د ي ن B001 note: Maqayis gives ONE asl for all din branches: "أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل". B003 note: "Maqayis treats debt as within the same asl because debt carries dhull". So Maqayis itself ties obedience, recompense and debt together; the split is the dictionary's analytical one | P |
| 6 | MEAL-001 | Islamoglu's "Allah'a karsi borclulukI" and Esed's reframing are outside the classical range of din | Lexically a debt branch exists: د ي ن B003 الدين المالي (maqayis: "داينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء"; tahdhib "دنت الرجل أقرضته"), and Maqayis unifies it with inqiyad (see row 5). The "not in classical commentaries" part is a tafsir claim (dictionary silent) | P |
| 7 | NOV-009 | first object (ed-din) and last object (maun) meet in "itaat" | din=itaat: د ي ن B001, supported. maun=itaat: م ع ن absent from dictionary, so the second half is unverifiable here | P |
| 8 | NOV-010 | dayentu, dintu, "kezebe aleyke = vacip oldu" are lexical material | د ي ن B003 (dayentu: maqayis; dintu: tahdhib); ك ذ ب B003 "كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis)", "كذب عليكم الحج أي وجب (ayn/sihah)"; B003 note: Maqayis calls the idiom difficult and old speech | S |
| 9 | SEM-002 | sahun: lexical range (gaflet, lahv) | root س ه و NOT in dictionary. Semantic neighbours exist: غ ف ل B001 "الغفلة سهو يعتري الإنسان من قلة التحفظ" (mufradat), "غفلت عن الشيء إذا تركته ساهيا (maqayis)"; ل ه و B001 "كل شيء شغلك عن شيء فقد ألهاك (maqayis)" supports the Tabari "lahun" gloss lexically | NF |
| 10 | TAF-006 / REJ-001 | Maqayis gives "sehavtu fi's-salat" (so fi is lawful in language) | No sahw root. Cached Maqayis page confirms: "السهو: الغفلة، يقال سهوت في الصلاة أسهو سهوا" | NF (cache OK) |
| 11 | MEAL-004 | Maqayis defines "sehv: kalbin ondan gitmesi" | No sahw root. Cached Maqayis sahw entry says only "السهو: الغفلة" and "السهو: السكون". The phrase "وذهاب القلب عنه" is not in the cached Maqayis text; it is the base tag text for س ه و B001 and its lexicon is unknown. Probable mislabel | NF (cache contradicts label) |
| 12 | NOV-004 | Maqayis yatm: "her tek kalan sey yetimdir"; "yetimin asli gaflettir" and "gecikmedir" come from other dictionaries | ي ت م B002 "لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)"; B003 gaflet: src jamhara, tahdhib only; B004 ibta': src sihah, tahdhib only. Exactly as stated. Missed: B001 (Maqayis: orphanhood from father in humans, from mother in animals), B005 (unmarried woman, Tahdhib) | S |
| 13 | NOV-004 | sahv is a separate root; Maqayis gives sahv = gaflet | No sahw root. Cached Maqayis: "السهو: الغفلة" | NF (cache OK) |
| 14 | NOV-005 | Maqayis: Suha "birinci babdan olmasi muhtemel, cunku cok gizli, gorulmesinden gaflet edilir" | No sahw root, so also base tags س ه و B005. Cached Maqayis: "فأما السها فمحتمل أن يكون من الباب الأول لأنه خفي جدا فيسهى عن رؤيته". Quote exact | NF (cache OK) |
| 15 | SEM-003 | yedu''u: pushing from his right and property; not feeding; harsh push; Maqayis defines dec as "ed-def'" and cites 52:13 | د ع ع B001 (maqayis, tahdhib, sihah, ayn, mufradat): "الدَّعّ الدفع (maqayis;tahdhib)", "دفع في جفوة (ayn)", Ayn text "يعنف به ... أي يدفعه حقه وصلته" (hak branch), lu_004 "يوم يدعون إلى نار جهنم دعا (maqayis)"; QAC lists 52:13 under د ع ع | S |
| 16 | MET-004 | Maqayis does not count "da' da'" and the sheep call as asl; core is movement, pushing, agitation; so "kaldiran cagri" is only phonetic association, not the root's true meaning | Maqayis half S: B003 note "Maqayis treats this sound material as non-productive sound imitation rather than a measured root asl"; B002 note "Maqayis groups this under movement, pushing, and disturbance"; cached Maqayis quote exact. Narrowed: B004 (دع دع للعاثر) is an accepted branch (src maqayis, sihah, tahdhib, mufradat) and the dictionary records the opposite view: Mufradat "أصله أن يقال للعاثر دع دع" (origin of severe pushing; B001 and B004 notes, lu_012). The commentary states Maqayis's position as the root's status and omits Raghib | P |
| 17 | REJ-003 | reading yedu''u as "raises/calls the orphan" via da' da' rejected; Maqayis does not treat sounds as asl | same as row 16; the "no sharh gives it" half is tafsir (silent) | P |
| 18 | NOV-006 | di'a' (small dependents) and de'de'a (shaking a measure) sit in the same root | د ع ع B009 الدعاع عيال صغار (tahdhib only, "أدع الرجل إذا كثر دعاعه") and B002 (maqayis, sihah, tahdhib). Both exist; B009 is single-source; B006/B007 are marked review | S |
| 19 | NOV-006 | miskin root is linked with house and household (seken) | QAC puts مِسْكِين under س ك ن (not م س ك). B003 السكن أهل الدار (maqayis, mufradat, sihah, tahdhib, ayn), B010 الأسكان الأقوات "مرعى مسكن" (tahdhib), B006 note: Tahdhib derives المسكين from the sukun asl | S |
| 20 | NOV-006 | sehv root has the "sehve" porch | No sahw root. Cached Maqayis: sehwa is listed under "ما شذ عن هذا الباب" (outlier to the root's measure); not mentioned in the claim | NF (cache adds caveat) |
| 21 | SEM-004 / MEAL-006 / MET-005 | hadd = urging/teshvik; base gloss "surmek" is Turkish association | ح ض ض B001 "الحث والتحريض والحض المتبادل على الخير أو القتال أو طعام المسكين" (src ayn, maqayis, mufradat, sihah, tahdhib); B001 "not": excludes "السير والسوق عند من فرقه عن الحث". ح ث ث B002 shows hass includes speed and driving (maqayis "ولي حثيثا"). So the "surmek" gloss is not lexically carried by hadd | S |
| 22 | SEM-004 | Ibn Kathir: miskin = "hicbir seyi olmayan fakir" (used to test meals) | س ك ن B006 (src ayn, sihah, tahdhib only; not Maqayis, not Mufradat): "المسكين الفقير وقد يكون بمعنى الذلة والضعف"; "تمسكن إذا خضع لله". Dictionary adds an abasement/submission strand; no "owns nothing" sense | P |
| 23 | MET-005 | Maqayis gives hadd as two asls (urging; low ground hadid), so the "push toward the bottom" image is resonance not unity; Halil: hass in walking/driving, hadd not | S for the core: ح ض ض B001 and B002 are separate branches; B002 note "Maqayis makes this a separate asl"; cached Maqayis text "الحاء والضاد أصلان ... وقال الخليل: الحث يكون في السير والسوق ... والحض لا يكون في سير ولا سوق" exact. Narrowed: B002 note adds "Mufradat links urging to الحضيض as an origin story", i.e. a lexicon does connect them; "anlam birligi degildir" is Maqayis's view only. Also missed: B003 الحُضُض (bitter resin), B004 استزادة النفس. Route detail: the Maqayis entry is headword حض (variant route); Sihah is the exact ح ض ض | P |
| 24 | TAF-009 | maun derivations: (1) ma'n, (2) ma'une with alif for ha, (3) a'ane mef'ul, (4) me'vun by qalb | No م ع ن root; no card or branch contains ماعون. ع و ن (root_001064) B001 "الإعانة والمظاهرة" only shows that a'ane/ma'ūna exist as a root; it never lists ماعون. Derivation claims cannot be checked here | NF |
| 25 | MEAL-007 | ma'n = "az ve kolay sey" (Qutrub, Razi) as the basis of "ufacik yardim" | base tag م ع ن B003 المعن الشيء اليسير الهين: root absent | NF |
| 26 | MEAL-007 / MEAL-008 | verb yemne'un: "engel olurlar" (araya girmek) vs "esirgerler" (opposite of giving) | م ن ع B002 "المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)" (src ayn, mufradat, sihah, tahdhib) and B001 "خلاف الإعطاء (maqayis;sihah)". Both images exist. Note Maqayis records only B001, so "araya girmek" is not Maqayis's | S |
| 27 | SEM-006 | maun = water ("suya da maun denir") | No م ع ن root. م و ه (root_001458) B001 water, no ماعون. Only tangential: ط ع م B001 "والإطعام يقع حتى الماء (maqayis)" | NF |
| 28 | NOV-007 / XQ-006 | ma'in = flowing water, mu'nan, mem'un, "mai ma'in" 67:30 | No م ع ن root. QAC 67:30 is linked only to ر ء ي (أرأيتم). Cannot verify | NF |
| 29 | NOV-007 | "mer'an muskin" association with miskin root | س ك ن B010 "مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه" (tahdhib only) | S |
| 30 | SEM-007 | veyl = azap/yikim threat, not mere reproach (valley of Jahannam in Tabari) | و ي ل B001 "الوَيل حلول الشر (ayn;tahdhib)", "كلمة عذاب (sihah)", "أصل الوَيل الهلاك والعذاب (tahdhib)"; B001 "not" explicitly excludes "تفسير الويل بأنه واد في جهنم" (a tafsir gloss, not a lexical sense). Missed: B002 ندبة الفضيحة والبلية ("ويلاه", "يا ويلتاه", "الوَيلة الفضيحة"), a lament/disgrace register. No Maqayis entry for this root; no QAC occurrence is linked | P |
| 31 | MEAL-008 | "Yazıklar olsun" shifts veyl to moral rebuke and softens it; "Lanet olsun" (la'n) is misleading | B001 supports "doom/azab" and nothing lexical for la'n (second part S). But "Yazıklar/ah vah" is close to B002 lament register, so softening is lexically attested, not only an error of tone | P |
| 32 | MEAL-008 | musallin: salat = namaz and dua (Maqayis gives both); "didinip duranlar" is un-Arabic | ص ل و B003 "الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)", B002 "الصلاة وهي الدعاء (maqayis;sihah)". No branch for "toiling" | S |
| 33 | NOV-008 | musallin root carries fire; miskin root carries "seken = ocak"; project joins them | ص ل و B001 fire (maqayis, ayn, sihah, mufradat, tahdhib); س ك ن B004 "السكن النار التي يسكن بها" (maqayis, mufradat, sihah, tahdhib). Caveat: the Qur'anic fire verbs are QAC ص ل ي, and in ص ل و the fire sense reaches Maqayis only by weak-final variant routing (headword صلى) | S |
| 34 | NOV-011 / TAF-014 | salat = dua; seken = huzur (9:103) | ص ل و B002 "صلوات الرسول للمسلمين دعاؤه لهم (ayn)"; س ك ن B004 "إن صلواتك سكن لهم", "كل ما سكنت إليه من محبوب"; QAC places 9:103 under both ص ل و and س ك ن. Note: Mufradat there groups بيت وليل وصلاة under ما يسكن إليه | S |
| 35 | MEAL-010 / NOV-001 | yuraun: mutual seeing (muf'ale), showing, mirror image | ر ء ي B004 تراءى القوم (maqayis), B005 "وراءى فلان يرائي ... ليراه الناس (maqayis)", Tahdhib "يرآءون الناس إذا أبصرهم الناس صلوا", B012 إراءة. QAC 107:6 يُرَآءُ -> ر ء ي | S |
| 36 | XQ-001, 003-007, 009; SEM-003/008 | verse links share the root: 52:13 دع; 69:34 and 89:18 حض/طعم/سكن; 89:17, 93:9 يتم; 36:47 طعم; 4:142 ر ء ي + ص ل و; 9:103; 9:54; 68:12 منع; 74:43-46; 19:59; 29:45; 83:10-11 | QAC occurrence tables of root_000477, 000334, 000934, 000726, 001692, 000531, 000879, 001448, 000504, 001290 contain all of these refs | S |
| 37 | XQ-003, XQ-006, XQ-007, NOV-007 | 51:11 sahun, 67:30 ma'in, 83:1 veyl as same-root links | 51:11 and 67:30 (ma'in) have no root in the dictionary; 83:1 وَيْل has no QAC link; 74:42 also not covered | NF |
| 38 | Base inline tags | 86 tags cite "ROOT,Bnnn" for roots that exist (ر ء ي 11, ك ذ ب 11, ص ل و 11, د ع ع 12, س ك ن 10, م ن ع 9, د ي ن 8, ي ت م 7, ط ع م 4, ح ض ض 3) | Programmatic check: every Arabic phrase sits inside the cited branch's source_phrase_ar or what_is_ar (surface-form tags such as يُكَذِّبُ / بِٱلدِّينِ resolve at root and branch level). No wrong branch ids | S |
| 39 | Base inline tags | 29 tags cite س ه و (10) and م ع ن (19) branches B001-B006 | Neither root exists in the exported dictionary (1679 roots, none with those norms). The citations may come from a newer or different dictionary build; cannot be audited here | NF |
| 40 | Base tag "veyl" | `source:"memory"`, gloss "yikim, vay hali" | و ي ل root_001689 B001/B002 supports both parts of the gloss and could replace the "memory" label | S |
| 41 | TAF-013 / SEM-005 | maun in jahiliyya = every benefit and gift; in Islam = obedience and zakat; "maun = itaat" | No م ع ن. ز ك و B003 (zakat) exists but is independent | NF |
| 42 | MEAL-003 / TAF-006 | 'an vs fi particle contrast | particles are not in the dictionary | SIL |
| 43 | MEAL-010 / NOV-001 | "muf'ale: dual direction of the showing" (Zamakhshari) as a grammar claim | grammar form not recorded in the dictionary (lexical B004 supports reciprocal seeing only) | SIL |
| 44 | QIR-002 / SEM-002 | Ibn Mas'ud "lahun" links sahw to lahw | ل ه و B001 "اللهو ما يشغل الإنسان عما يعنيه (mufradat)" gives the lexical meaning of lahw; the reading attribution itself is qiraat (not in the dictionary) | S |

(Row 44 is counted under SUPPORTED. Row 42 and 43 under DICTIONARY SILENT. The SUPPORTED total of 18 comprises rows 1, 2, 8, 12, 15, 18, 19, 21, 26, 29, 32, 33, 34, 35, 36, 38, 40, 44.)

## 3. Highlights

### 3.1 Claims the dictionary contradicts or narrows

1. MET-004 (da' da'): the Maqayis half is correct (dictionary B003 and cached text agree), but the dictionary also stores the opposite classical view. Mufradat (Raghib) says the stumbler's cry is the origin of severe pushing (B004 note, lu_012, B001 note); the dictionary keeps B004 as an "accepted" branch. The note should say "Maqayis does not treat it as asl; Raghib does", not state Maqayis's position as the root's status.
2. MET-005 (ḥ-ḍ-ḍ two asls): confirmed for Maqayis (cached text and dictionary B002 note "Maqayis makes this a separate asl"). Narrowed: the dictionary also records that Mufradat explicitly links urging to al-ḥaḍīḍ as an origin story, so "harf birliginden dogan rezonans, anlam birligi degildir" is Maqayis's view, not all lexicons'. The Khalil hass/hadd distinction is verified in the cached Maqayis page; the dictionary does not record it as a branch rule.
3. MEAL-002 source label: "Maqayis tanimi (kezib soz ve fiil icin soylenir)" is Mufradat in the dictionary (ك ذ ب B001, src mufradat). Maqayis supplies only "الكذب خلاف الصدق".
4. SEM-008 / MEAL-001: Maqayis puts all of din (obedience, recompense, debt, subjugation) under ONE asl, "انقياد وذل" (د ي ن B001/B003 notes). The enriched file treats "din=itaat (Maqayis)" and "din=karsilik/borc" as separate and calls borçluluk outside the classical range; lexically, debt is inside Maqayis's own asl.
5. wayl and maun derivations:
   - veyl: و ي ل exists (2 branches, no Maqayis, no QAC link). B001 doom/azap supports SEM-007, and its "not" clause excludes "valley in Jahannam" as a lexical sense. B002 (lament, "ويلاه", "الويلة الفضيحة") is missed and gives lexical basis to "Yazıklar olsun" renderings that MEAL-008 calls a softening.
   - maun: no م ع ن root anywhere in the dictionary, so TAF-009 (ma'n / ma'une / a'ane / me'vun), SEM-006 (water), TAF-013 (itaat), NOV-007 (ma'in) cannot be verified. ع و ن B001 (help) exists but never lists ماعون.

### 3.2 Roots with branches the commentary missed

| Root | Used | Dictionary branches not mentioned |
|---|---|---|
| د ع ع 000477 | B001-B004, B009 | B005 slow twisting running, B006/B007 (review), B008 watery plant, B010 wild seed |
| ح ض ض 000334 | B001, B002 | B003 الحُضُض bitter medicinal resin, B004 استزادة النفس |
| ك ذ ب 001290 | B001-B007, B009 | B008 النفس الكذوب (jamhara) |
| ي ت م 001692 | B001-B004 | B005 unmarried woman (Tahdhib); B001 Maqayis animal/mother-side orphanhood |
| د ي ن 000504 | B001-B003, B007 | B004 subjugation, B005 habit/custom, B006 city (المدينة) |
| س ك ن 000726 | B001, B002, B003, B004, B006, B010 | B005 السكينة, B007 knife, B008 rudder, B009 positions; also note miskin B006 (src ayn, sihah, tahdhib) is not in Maqayis |
| ر ء ي 000531 | B001, B004-B006, B010, B012, B013 | B002 opinion (الرأي), B003 dream, B007 menstrual trace, B008 jinn familiar, B009 lung, B011 banner |
| ط ع م 000934 | B001, B002, B004 | B003 prompting speech, B005 ripening, B006-B014 specialised senses |
| م ن ع 001448 | B001-B003 | B004 chaste refusal, B005 imperative "مناع", B006 contending, B007 youthful resilience |
| ص ل و 000879 | B001-B003 | B004 snare, B005 haunch, B006 racing second, B007 places of worship, B008-B009 |
| و ي ل 001689 | B001 | B002 lament |

### 3.3 Source-label differences (commentary vs dictionary)

| Block | Commentary label | Dictionary / cache |
|---|---|---|
| MEAL-002 | Maqayis: "kezib soz ve fiil icin" | Mufradat (ك ذ ب B001) |
| MEAL-004 | Maqayis: "sehv: kalbin ondan gitmesi" | not in cached Maqayis (it has "الغفلة" and "السكون"); sahw root absent from dictionary |
| NOV-001 | "er-riyyu/ruwa'" under "Maqayis and other dictionaries" | Maqayis has الرئي/الرواء/المرآة (hamza form); الري is Ayn (ر ء ي B006) |
| MET-005 | "Halil distinction" via Maqayis | correct per cache; dictionary has no such rule field |
| SEM-004 test of miskin | "Ibn Kathir: owns nothing" | dictionary miskin (س ك ن B006) is Ayn/Sihah/Tahdhib only, with abasement strand |
| NOV-006 | di'a' and de'de'a as one lexical family | de'de'a is Maqayis/Sihah/Tahdhib; di'a' (B009) is Tahdhib-only |
| Inline tag | veyl `source:"memory"` | و ي ل B001/B002 (ayn, sihah, tahdhib, mufradat; no Maqayis) |
| Inline tags (29) | `س ه و,B001-B005` and `م ع ن,B001-B006` | roots absent from the dictionary export |

## 4. Suggested corrections (suggestions only; nothing edited)

1. MET-004: add "Mufradat (Raghib) takes 'da' da' lil-'athir' as the origin of severe pushing (dictionary د ع ع B001/B004 notes); Maqayis denies it asl status". Keep the Maqayis quote.
2. MET-005: add that Mufradat explicitly connects urging with al-hadid (dictionary ح ض ض B002 note); phrase the resonance warning as Maqayis's judgement. Optionally mention B003/B004.
3. MEAL-002: relabel "kezib soz ve fiil icin soylenir" as Mufradat (ك ذ ب B001), or cite the Maqayis wording "خلاف الصدق".
4. MEAL-004: verify the source of "ذهاب القلب عنه" before attributing it to Maqayis; the cached Maqayis sahw entry reads "الغفلة والسكون" only.
5. SEM-008 / MEAL-001: note that Maqayis ties din, debt and recompense under one asl "انقياد وذل" (د ي ن B001/B003); do not call debt-based "borcluluk" lexically foreign.
6. SEM-007 / MEAL-008: mention و ي ل B002 (lament/disgrace register); keep the "valley in Jahannam is a tafsir gloss, not a lexical sense" point. Replace `source:"memory"` for veyl with the و ي ل root_001689 citation.
7. TAF-009 / SEM-006 / NOV-007 / XQ-006 / TAF-013: add "root م ع ن is not in the project dictionary export; derivation and branch ids (م ع ن,B001-B006) unverifiable here", or confirm the dictionary build that contains them. Same for س ه و (10 inline tags).
8. NOV-004 / NOV-006: add ي ت م B001 (animal orphanhood) and B005, and flag that di'a' (د ع ع B009) is Tahdhib-only and "review"-adjacent.
9. NOV-008: add the caveat that Qur'anic fire verbs sit in ص ل ي (root_000880) and that ص ل و reaches Maqayis's fire asl through variant routing; and that س ك ن B004 already pairs "صلاة" and "نار" as "ما يسكن إليه" (Mufradat), so the pairing has a lexical source.
10. SEM-004 miskin discussion: note that miskin (س ك ن B006) is Ayn/Sihah/Tahdhib and includes abasement; Maqayis does not cover it.
