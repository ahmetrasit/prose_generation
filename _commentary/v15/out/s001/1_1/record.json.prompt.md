# Ayah reading

You are reading ayah 1:1 with every branch of every one of its words open, inside its neighbourhood and its surah. You produce the record from which its commentary will be written: everything you hear, each finding anchored and contained, each with what it makes perceptible. You do not write the commentary; you output JSON.

## Who this is for

One reader: a curious Turkish speaker with almost no Arabic grammar. Their Arabic arrives through loanwords, and those loanwords, theological ones above all, have shifted, narrowed or lost their meaning in Turkish. Canonical meanings are easy for them to find elsewhere; they are only the anchor. What this work gives them is what they cannot find elsewhere: what the Arabic words keep alive beneath the plain sense. Success: after reading, they understand the ayah and the surah better than before, and they are never disoriented.

## How a sense becomes heard

- Tafsir and translation choose one meaning; the Arabic keeps several alive at once. Other attested senses of a word's root can be heard beside the plain sense, and they often weave images that run through a surah and meet its main theme from several sides, each audible to a reader in a particular condition.
- Every attested branch of every root is open. Branches have no order. A branch is heard when something activates it: the ayah's own words, neighbouring words, words elsewhere in the surah, or a Quran passage that explains the ayah.
- The dictionary is both guard and supplier. Use the branches given (and the full entries you may read). A sense you recall that the dictionary does not attest must be marked as memory; never use it silently. No invented senses, sources, etymologies or chronology.
- Do not prune early. Keep partial, strange and minor activations. Combine fragments across words, branches and roles. Let a completed image strengthen its weak members. Only then ask what it shows about the plain reading. No plausibility filter, no confidence scores, no verdict on an image from one of its members.
- Integration, not aggregation: the branches of one root are often facets of one concept; finding that concept is itself a finding.
- Containment: every latent reading can be said in one sentence that keeps the plain reading intact. Never "not X but Y".
- The test that matters: what does this make perceptible in the plain reading that a paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)? Space in the commentary will follow that payoff; it is a matter of function, not of certainty.
- Readings coexist. Never declare one correct.

## What you have (below the line)

1. The ayah in its neighbourhood (±7 ayat; the focus is marked).
2. Its words with roots, lemmas and parts of speech.
3. The dictionary for its roots, one line per branch (branch | Arabic image | Arabic definition, trimmed). Alternative roots are marked ~alt with the reason.
4. Scene lines touching its words: first in the neighbourhood, then scenes that reach elsewhere in the surah (each with at most a few far words, those adding roles the neighbourhood lacks first, and a file listing every member). Members of one scene activate one another: several words supplying different parts of one scene are themselves an activation. Mechanical and generous: an ordering aid, not a worklist.
5. The plan from the window reading: the images this ayah should open, advance or complete, the images earlier ayat opened, and the window's movement. Use it; you are not bound by it. If the ayah opens an image the plan missed, record it.
6. The concordance for its lemmas: every use (lemmas used up to 30 times) or a use profile (frequent lemmas).
7. Variant readings.
8. Turkish loanword cards for its lemmas: what the Turkish reader hears, what the Arabic keeps.

You may read more from the paths listed at the end. Read only what a specific question needs; do not read in bulk.

## The record

- ref: 1:1.
- ground: the plain sense in two to four sentences, as a careful translator would give it.
- findings: every latent reading, local resonance, image member, root concept, Quran-loaded word, variant and grammar point you hear. For each:
  - id (F1, F2, …); kind: latent | image | local_resonance | concept | loaded_word | variant | grammar;
  - anchor: the word (ref S:A:W, surface) and the dictionary branch (root with spaces, branch Bnnn) the finding stands on (branch may be empty for grammar);
  - triggers: the words (ref, surface) that activate it and how (shared scene, sound, shared root, syntax, a neighbouring or explaining passage);
  - statement: one containment sentence (plain reading kept);
  - perceptible: what it makes perceptible in the plain reading;
  - image: the plan's image id, a new id you give, or "";
  - memory: true if any part rests on a sense the dictionary does not attest;
  - for_prose: lead | support | record. Lead: this ayah's commentary should make it perceptible; support: it can serve a lead finding; record: kept here, not needed in this ayah's prose. Decide by payoff for this reader in this ayah, respecting the plan.
- loaded_words: words the Quran uses with one recurring role (read it from the concordance: the role, and how many uses keep it), and where a usual translation departs from that role here.
- losses: for the key Turkish words the reader will meet for this ayah (from the loanword cards and your knowledge of Turkish; memory true for what the cards do not give): what the Turkish word loses or adds against the Arabic here.
- grammar: only grammar the Turkish reader cannot hear and that matters to a reading here, one line each; else empty.
- variants: variant readings that open or support a reading, one line each; else empty.
- reread: the plain reading read anew with the findings heard together, three to six sentences.
- disclosed: the image ids this ayah's commentary will make audible (so later ayat can build on them).
- set_aside: activations you considered and did not keep, each with why. Nothing is lost silently.

Do not audit your own findings for plausibility; the payoff test is the only test here. Evidence from the rest of the Quran will be gathered separately after this reading. Analysis in English; Arabic as in the text. Output only the JSON object required by the schema.

---

# Ayah 1:1

## The ayah in its neighbourhood (1:1–7)

1:1| بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ  ◀ focus
1:2| ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1:3| ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:4| مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5| إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6| ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7| صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

## Its words (ref surface | root | lemma | pos)

1:1:1 بِسْمِ | س م و | ٱسْم | N
1:1:2 ٱللَّهِ | ء ل ه | ٱللَّه | PN
1:1:3 ٱلرَّحْمَٰنِ | ر ح م | رَّحْمَٰن | ADJ
1:1:4 ٱلرَّحِيمِ | ر ح م | رَّحِيم | ADJ

## Dictionary for its roots (branch | image | definition | tr: Turkish gloss)

### س م و — 381 uses; here: 1:1:1 بِسْمِ
B001 | العلو والارتفاع | سمو الشيء وعلوه، وارتفاع البصر، وعلو الحسيب والشريف، ورفعة الذكر.
B002 | الشخص المرتفع الظاهر | الشيء أو الشخص الذي يرتفع فيلوح من بعيد، وسماوة الهلال أو كل شيء بمعنى شخصه العالي الظاهر.
B003 | تطاول الفحل على الشول | سما الفحل إذا تطاول أو سطا على شوله، أي علاها وتخللها.
B004 | السماء وما علا فأظل | السماء لما علا وأظل، والسقف، والسحاب، والمطر، والنبات المنسوب إلى المطر، وظهر الفرس أو أعلى الشيء.
B005 | الاسم تنويه ودلالة | الاسم والتسمية والتسمي والأسامي، والسمي بمعنى الموافق في الاسم أو النظير المستحق للاسم.
B006 | الخروج للصيد | سما القوم أو استموا إذا خرجوا للصيد، والسماة الصيادون، وما لحق بذلك من طلب الوحش وآلة الصياد.
B007 | المساماة والمباراة | تسامى القوم إذا تباروا، والمساماة بمعنى المفاخرة والمباراة والمعارضة، ومن لا يسامى إذا لا يقدر على …
B008 | الصيت الحسن المنتشر | سماه بمعنى صوته أو صيته في الخير لا في الشر.

### و س م ~alt (documented alternative analysis) — 2 uses; here: 1:1:1 بِسْمِ
B001 | أثر وسم ظاهر يجعل الشيء معروفا | وسم الشيء أو الدابة بسمة أو كي أو قطع أذن، والميسم أو المكواة، وكل علامة حسية للتعريف أو التمييز.
B002 | سمة يرى بها الناظر دلالة الحال | التوسم والتفرس، ورؤية أثر الخير أو الشر في الشخص، والآيات للمتوسمين بوصفهم ناظرين في السمة الدالة.
B003 | مطر أول يسم الأرض بالنبات | الوسمي، وهو المطر الأول أو مطر أول السنة أو الربيع الأول، وتسميته لأنه يسم الأرض بالنبات، والأرض …
B004 | موسم معلم يجتمع إليه الناس | موسم الحج ومواسم أسواق العرب، والمجمع أو الوقت المعلم الذي يجتمع إليه الناس، ووسم الناس بمعنى شهدوا …
B005 | حسن عليه أثر الجمال | الوسامة، والوسيم والوسيمة، وذات ميسم، أي الحسن أو أثر الجمال والعتق الظاهر على الشخص.
B006 | وسمة يخضب بورقها | الوسم أو الوسمة اسم شجرة أو نبات ورقه خضاب، والعظلم الذي يختضب به.

### ء ل ه — 2851 uses; here: 1:1:2 ٱللَّهِ
B001 | التعبد والمعبود | أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
B002 | اسم الله في القسم والنداء | اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه …

### و ل ه ~alt (documented alternative analysis) — 0 uses; here: 1:1:2 ٱللَّهِ
B001 | الوَلَه والحيرة | ذهاب العقل أو اضطرابه من شدة الوجد، والحيرة، والحنين إلى المفقود أو المحبوب في الرجل والمرأة …
B002 | تَوْلِيه الوالدة عن ولدها | التوليه المتعدي: التفريق بين المرأة أو الوالدة وولدها حتى تصير والهة، وخاصة في البيع أو السبي
B003 | ماء مُولَه ذاهب | الماء أو العين إذا أرسل ماؤها في الصحراء فذهب
B004 | المُولَه العنكبوت | اسم المُولَه للعنكبوت كما في رواية الصحاح

### ر ح م — 339 uses; here: 1:1:3 ٱلرَّحْمَٰنِ; 1:1:4 ٱلرَّحِيمِ
B001 | الرَّحْمَة والرقة | الرقة والعطف والرأفة والإحسان إلى المرحوم والمرحمة والتراحم والترحم وأسماء الرحمن والرحيم من جهة …
B002 | الرَّحِم والقرابة | الرَّحِم بمعنى القرابة القريبة وأسباب النسب وصلة الرحم وقطعها والأرحام.
B003 | رَحِم الأنثى | رَحِم المرأة أو الأنثى بوصفه بيت منبت الولد ووعاءه في البطن.
B004 | وجع الرَّحِم بعد الولادة | الرحوم والراحم والرواحم وما قيل في الناقة أو الشاة أو المرأة إذا اشتكت رحمها أو أصابه داء أو ورم أو …

## Scene lines touching its words, in the neighbourhood

- trade.sale [6 words, 6 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B002 sale separation | with: لِلَّهِ 1:2:2 sale separation · ٱلدِّينِ 1:4:3 bargain · نَعْبُدُ 1:5:2 goods · ٱلْمُسْتَقِيمَ 1:6:3 price, market · غَيْرِ 1:7:5 exchange
- body.limbs [7 words, 5 roles] here: بِسْمِ 1:1:1: س م و B004 back | with: مَٰلِكِ 1:4:1 leg · ٱهْدِنَا 1:6:1 neck · ٱلصِّرَٰطَ 1:6:2 joint · ٱلْمُسْتَقِيمَ 1:6:3 leg, back · أَنْعَمْتَ 1:7:3 foot · +1 more (all: data/scenes/s001/body.limbs.md)
- time.age [5 words, 6 roles] here: بِسْمِ 1:1:1: و س م~alt B004 appointed time | with: يَوْمِ 1:4:2 duration, epoch, appointed time · نَعْبُدُ 1:5:2 delay · نَسْتَعِينُ 1:5:4 age, old age · ٱلْمُسْتَقِيمَ 1:6:3 appointed time
- kin.birth_nursing [7 words, 4 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B002 mother child separation · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B003 womb, ر ح م B004 birth · ٱلرَّحِيمِ 1:1:4: ر ح م B003 womb, ر ح م B004 birth | with: لِلَّهِ 1:2:2 mother child separation · رَبِّ 1:2:3 foster child · ٱلرَّحْمَٰنِ 1:3:1 womb, birth · +1 more (all: data/scenes/s001/kin.birth_nursing.md)
- war.battle [7 words, 4 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B002 captive | with: لِلَّهِ 1:2:2 captive · نَعْبُدُ 1:5:2 captive · نَسْتَعِينُ 1:5:4 battle · ٱهْدِنَا 1:6:1 captive · ٱلْمُسْتَقِيمَ 1:6:3 confrontation · أَنْعَمْتَ 1:7:3 rout
- know.perceiving [5 words, 4 roles] here: بِسْمِ 1:1:1: و س م~alt B002 perceiving | with: رَبِّ 1:2:3 knowing · ٱلْعَٰلَمِينَ 1:2:4 knowing · ٱهْدِنَا 1:6:1 ignorance · ٱلضَّآلِّينَ 1:7:9 forgetting
- ritual.prayer [4 words, 4 roles] here: ٱللَّهِ 1:1:2: ء ل ه B001 worship, ء ل ه B002 call | with: لِلَّهِ 1:2:2 worship, call · ٱلدِّينِ 1:4:3 worship · ٱلْمُسْتَقِيمَ 1:6:3 standing, prayer performance
- speech.praise_blame [4 words, 4 roles] here: بِسْمِ 1:1:1: س م و B007 boasting | with: ٱلْحَمْدُ 1:2:1 praise, boasting, thanks · ٱهْدِنَا 1:6:1 blame · أَنْعَمْتَ 1:7:3 praise
- emotion.love [7 words, 3 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B001 longing · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B001 mercy · ٱلرَّحِيمِ 1:1:4: ر ح م B001 mercy | with: لِلَّهِ 1:2:2 longing · ٱلرَّحْمَٰنِ 1:3:1 mercy · ٱهْدِنَا 1:6:1 affection · +1 more (all: data/scenes/s001/emotion.love.md)
- kin.lineage [6 words, 3 roles] here: ٱلرَّحْمَٰنِ 1:1:3: ر ح م B002 kin tie · ٱلرَّحِيمِ 1:1:4: ر ح م B002 kin tie | with: رَبِّ 1:2:3 tribe · ٱلرَّحْمَٰنِ 1:3:1 kin tie · ٱلْمُسْتَقِيمَ 1:6:3 clan · +1 more (all: data/scenes/s001/kin.lineage.md)
- dwelling.settlement [5 words, 3 roles] here: بِسْمِ 1:1:1: و س م~alt B004 market | with: ٱلدِّينِ 1:4:3 town · نَسْتَعِينُ 1:5:4 town · ٱلْمُسْتَقِيمَ 1:6:3 dwelling place, market · أَنْعَمْتَ 1:7:3 dwelling place
- motion.gather_scatter [5 words, 3 roles] here: بِسْمِ 1:1:1: و س م~alt B004 gathering | with: رَبِّ 1:2:3 crowd · نَعْبُدُ 1:5:2 dispersal · ٱلْمُسْتَقِيمَ 1:6:3 crowd · أَنْعَمْتَ 1:7:3 dispersal
- motion.passage [5 words, 3 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B003 vanishing | with: لِلَّهِ 1:2:2 vanishing · ٱلصِّرَٰطَ 1:6:2 being swallowed, penetrating · ٱلضَّآلِّينَ 1:7:9 vanishing · +1 more (all: data/scenes/s001/motion.passage.md)
- sky.bodies [5 words, 3 roles] here: بِسْمِ 1:1:1: س م و B002 moon | with: ٱلصِّرَٰطَ 1:6:2 constellation · ٱلْمُسْتَقِيمَ 1:6:3 zenith · أَنْعَمْتَ 1:7:3 constellation · +1 more (all: data/scenes/s001/sky.bodies.md)
- speech.calling [5 words, 3 roles] here: بِسْمِ 1:1:1: س م و B005 naming · ٱللَّهِ 1:1:2: ء ل ه B002 call | with: ٱلْحَمْدُ 1:2:1 naming · لِلَّهِ 1:2:2 call · أَنْعَمْتَ 1:7:3 answer, call
- rule.covenant [4 words, 3 roles] here: ٱللَّهِ 1:1:2: ء ل ه B002 oath | with: لِلَّهِ 1:2:2 oath · رَبِّ 1:2:3 covenant · ٱلدِّينِ 1:4:3 witness
- dwelling.building [3 words, 3 roles] here: بِسْمِ 1:1:1: س م و B004 roof | with: مَٰلِكِ 1:4:1 wall · ٱلْمُسْتَقِيمَ 1:6:3 pillar
- plant.growth_decay [3 words, 4 roles] here: بِسْمِ 1:1:1: س م و B004 growth, و س م~alt B003 growth, و س م~alt B006 leaf | with: رَبِّ 1:2:3 growth, greenness · ٱلْمُسْتَقِيمَ 1:6:3 root
- speech.news [3 words, 3 roles] here: بِسْمِ 1:1:1: س م و B008 report | with: ٱلْعَٰلَمِينَ 1:2:4 message · مَٰلِكِ 1:4:1 messenger
- travel.open_land [3 words, 3 roles] here: بِسْمِ 1:1:1: س م و B006 waste | with: مَٰلِكِ 1:4:1 water source · ٱلضَّآلِّينَ 1:7:9 getting lost, waste
- body.illness [7 words, 2 roles] here: ٱلرَّحْمَٰنِ 1:1:3: ر ح م B004 pain · ٱلرَّحِيمِ 1:1:4: ر ح م B004 pain | with: ٱلرَّحْمَٰنِ 1:3:1 pain · ٱلصِّرَٰطَ 1:6:2 disease · ٱلْمُسْتَقِيمَ 1:6:3 pain, disease · +2 more (all: data/scenes/s001/body.illness.md)
- body.innards [5 words, 2 roles] here: ٱلرَّحْمَٰنِ 1:1:3: ر ح م B003 belly · ٱلرَّحِيمِ 1:1:4: ر ح م B003 belly | with: ٱلرَّحْمَٰنِ 1:3:1 belly · مَٰلِكِ 1:4:1 heart · +1 more (all: data/scenes/s001/body.innards.md)
- emotion.grief_joy [4 words, 2 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B001 grief | with: لِلَّهِ 1:2:2 grief · نَعْبُدُ 1:5:2 grief · أَنْعَمْتَ 1:7:3 gladness
- animal.small [3 words, 2 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B004 spider | with: لِلَّهِ 1:2:2 spider · مَٰلِكِ 1:4:1 bee
- emotion.pride [3 words, 2 roles] here: بِسْمِ 1:1:1: س م و B001 honour, س م و B007 pride, س م و B008 honour | with: نَعْبُدُ 1:5:2 honour, pride · غَيْرِ 1:7:5 honour
- ritual.idols_lots [3 words, 2 roles] here: ٱللَّهِ 1:1:2: ء ل ه B001 cult | with: لِلَّهِ 1:2:2 cult · رَبِّ 1:2:3 lot
- water.rain_cloud [3 words, 2 roles] here: بِسْمِ 1:1:1: س م و B004 cloud, و س م~alt B003 rain | with: رَبِّ 1:2:3 cloud · غَيْرِ 1:7:5 rain
- craft.dyeing [2 words, 2 roles] here: بِسْمِ 1:1:1: و س م~alt B006 dye | with: ٱلْعَٰلَمِينَ 1:2:4 marking
- hunt.chase [2 words, 2 roles] here: بِسْمِ 1:1:1: س م و B006 hunter | with: ٱلْعَٰلَمِينَ 1:2:4 falcon
- pastoral.animal_care [2 words, 3 roles] here: بِسْمِ 1:1:1: و س م~alt B001 brand | with: نَعْبُدُ 1:5:2 tar coating, taming
- pastoral.breeding [2 words, 2 roles] here: بِسْمِ 1:1:1: س م و B003 mating | with: رَبِّ 1:2:3 newborn
- ritual.sanctuary [2 words, 2 roles] here: بِسْمِ 1:1:1: و س م~alt B004 pilgrim | with: ٱهْدِنَا 1:6:1 sanctuary
- sign.marking [2 words, 2 roles] here: بِسْمِ 1:1:1: س م و B005 sign, و س م~alt B001 mark, و س م~alt B002 sign | with: ٱلْعَٰلَمِينَ 1:2:4 mark, sign
- tool.implement [3 words, 1 roles] here: بِسْمِ 1:1:1: و س م~alt B001 device | with: نَعْبُدُ 1:5:2 device · ٱلْمُسْتَقِيمَ 1:6:3 device
- land.desert_sand [2 words, 1 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B003 desert | with: لِلَّهِ 1:2:2 desert
- motion.up_down [2 words, 1 roles] here: بِسْمِ 1:1:1: س م و B001 height, س م و B002 height | with: ٱلْمُسْتَقِيمَ 1:6:3 height
- water.spring_stream [2 words, 1 roles] here: ٱللَّهِ 1:1:2: و ل ه~alt B003 flow | with: لِلَّهِ 1:2:2 flow
- divine.lordship [13 words, 5 roles] here: ٱللَّهِ 1:1:2: ء ل ه B001 worship · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B001 mercy · ٱلرَّحِيمِ 1:1:4: ر ح م B001 mercy | with: لِلَّهِ 1:2:2 worship · رَبِّ 1:2:3 lord · ٱلرَّحْمَٰنِ 1:3:1 mercy · مَٰلِكِ 1:4:1 lord · يَوْمِ 1:4:2 mercy judgment · ٱلدِّينِ 1:4:3 worship · نَعْبُدُ 1:5:2 worship · ٱلْمُسْتَقِيمَ 1:6:3 judgment · ٱلْمَغْضُوبِ 1:7:6 judgment · +1 more (all: data/scenes/s001/divine.lordship.md)

## Scenes of its words that reach beyond the neighbourhood (at most 10 far words each, new roles first; every member in the file named)

(none)

## Plan from the window reading

- opens: I2 The branded herd, its owner, its lead animal and the stray — A herd of camels carries its owner's brand. It goes out from and returns to its owner's resting-place, following a lead animal at the front. One beast has strayed. It is left in a wasteland, and no one can tell who its owner is.. Members: بِسْمِ 1:1:1 B001 the brand (wasm, sima) by which an animal is known as someone's; documented alternative derivation of ism; رَبِّ 1:2:3 B001 the owner: rabb al-dābba, master of the beast; رَبِّ 1:2:3 B007 marabb al-ibil: the place where the camels stay; مَٰلِكِ 1:4:1 B008 the animal that goes in front and the rest follow (minor); ٱهْدِنَا 1:6:1 B003 the hādī: the front of the herd, the lead animal; أَنْعَمْتَ 1:7:3 B005 the herd itself (naʿam, camels), heard beside ḍāllīn (minor); ٱلضَّآلِّينَ 1:7:9 B005 the ḍālla: a beast left in a wasteland 'whose owner (rabb) is not known'; ٱلضَّآلِّينَ 1:7:9 B003 the thing gone from its owner, whose place cannot be found. Perceptible: The dictionary defines the ḍālla as the beast 'whose rabb is not known'. The word the surah uses for God in 1:2 is built into the definition of what it asks to be kept from in 1:7. So straying is relational, not only a wrong turn: it is losing one's tie to an owner who knows you. The surah is framed between the mark of belonging (bismi heard through wasm) and the unmarked stray.
- opens: I3 The womb and the one who raises stage by stage — A womb holds growing young. Kin are bound by the tie of the womb. A newly delivered mother stays home to nurse, and a caregiver takes charge of a child and raises it stage by stage until it is complete.. Members: ٱلرَّحْمَٰنِ 1:1:3 B001 tenderness and kindness toward the one shown mercy; ٱلرَّحِيمِ 1:1:4 B003 the womb as the house where offspring grows; ٱلرَّحِيمِ 1:1:4 B002 the kinship tie that comes from the womb; رَبِّ 1:2:3 B002 the one who puts a thing right and completes it, raising it 'stage by stage' (tarbiya ḥālan fa-ḥālan); رَبِّ 1:2:3 B005 the fosterer (rābb, rābba) who takes charge of the rabīb, the child in their care; رَبِّ 1:2:3 B009 the ewe that has just given birth and stays home for its milk (minor); ٱلرَّحْمَٰنِ 1:3:1 B001 mercy named again, after the rabb; ٱلرَّحِيمِ 1:3:2 B003 the womb heard again around the rabb. Perceptible: In Turkish, rahmet has become an abstract pity or rain. Here mercy becomes bodily and connected to kin: the tenderness of a womb toward what grows inside it. Rabb is placed between two mentions of the mercy names (1:1, 1:3), so lordship is heard wrapped in womb-tenderness: an owner who also raises, stage by stage, over time.
- note: Ism can also be heard from wasm, the mark by which an owner's animal is known. Raḥmān and raḥīm keep raḥim, the womb, audible under the flattened Turkish 'rahmet'.

Opened by earlier ayat:
(none)

Window movement: The surah moves from being named and marked (1:1, bismi, which can also be heard as wasm, the owner's brand) to an owner who raises (rabb) wrapped on both sides in womb-mercy (1:1–3). It then reaches the owner and king of a Day on which what is owed is settled (1:4). At 1:5 the owned ones stop speaking about the master and speak to him, declaring service and leaning on him for help. From that posture they ask to be led, held up and gifted onto a road already trodden smooth by the favored. That road takes its walker in (1:6–7). Their thanks were given at the start, and they ask not to become the stray beast in the waste whose owner no one knows. The surah's arc runs from the mark of belonging to the danger of being an unmarked stray, with praise answering a favor it only names at the end.

## Concordance for its lemmas

### ٱسْم — س م و — 39 uses in the Quran
use profile: {"root": "س م و", "lemma": "ٱسْم", "total": 39, "groups": [{"label": "Name as the object of mention or remembrance", "count": 14, "refs": ["2:114:10", "5:4:23", "6:118:4", "6:119:7", "6:121:6", "6:138:18", "22:28:5", "22:34:6", "22:36:11", "22:40:25", "24:36:9", "73:8:2", "76:25:2", "87:15:2"]}, {"label": "Names taught, reported, or assigned as designations", "count": 7, "refs": ["2:31:3", "2:31:11", "2:33:4", "2:33:7", "7:71:11", "12:40:6", "53:23:4"]}, {"label": "Names described as belonging to God", "count": 5, "refs": ["7:180:2", "7:180:10", "17:110:11", "20:8:7", "59:24:7"]}, {"label": "Name in a بِسْمِ phrase accompanying an act or text", "count": 4, "refs": ["1:1:1", "11:41:4", "27:30:5", "96:1:2"]}, {"label": "A person's name given as identifying information", "count": 3, "refs": ["3:45:10", "19:7:5", "61:6:23"]}, {"label": "Name in glorifying or blessing the Lord", "count": 5, "refs": ["55:78:2", "56:74:2", "56:96:2", "69:52:2", "87:1:2"]}, {"label": "Name used as a label for conduct", "count": 1, "refs": ["49:11:30"]}], "dominant": "Name as the object of mention or remembrance in 14 of 39 uses", "outside": [{"ref": "2:31:3", "how": "Names are the content of what Adam is taught."}, {"ref": "2:31:11", "how": "Names are requested as information about those being pointed out."}, {"ref": "2:33:4", "how": "Adam is told to inform them of the names."}, {"ref": "2:33:7", "how": "The names are the content of Adam's informing them."}, {"ref": "7:71:11", "how": "Names are described as ones people and their forebears assigned."}, {"ref": "12:40:6", "how": "Names are described as assigned by the addressees and their forebears."}, {"ref": "53:23:4", "how": "Names are described as assigned by people and their forebears."}, {"ref": "7:180:2", "how": "Names are described as belonging to God and as al-ḥusnā."}, {"ref": "7:180:10", "how": "Names follow فِى in a clause that includes يُلْحِدُونَ."}, {"ref": "17:110:11", "how": "Names are described as al-ḥusnā."}, {"ref": "20:8:7", "how": "Names are described as belonging to Him and as al-ḥusnā."}, {"ref": "59:24:7", "how": "Names are described as belonging to Him and as al-ḥusnā."}, {"ref": "1:1:1", "how": "The phrase opens a text before God's other descriptions."}, {"ref": "11:41:4", "how": "The بِسْمِ phrase accompanies a command to board."}, {"ref": "27:30:5", "how": "The بِسْمِ phrase appears at the opening of a letter."}, {"ref": "96:1:2", "how": "The بِسْمِ phrase accompanies a command to read."}, {"ref": "3:45:10", "how": "A person's name is followed by identifying names."}, {"ref": "19:7:5", "how": "A person's name is stated as Yaḥyā."}, {"ref": "61:6:23", "how": "A person's name is stated as Aḥmad."}, {"ref": "49:11:30", "how": "The name is equated with al-fusūq in a clause following mention of belief."}], "collocates": ["ٱللَّه (Allah/God)", "رَبّ (Lord)", "ذَكَرَ (remember/mention)", "سَمَّى (name/designate)", "ٱلْحُسْنَىٰ (best/most beautiful)", "عَلَىٰ (on/upon)", "فِى (in)"]}
every use: data/kwic/سمو_اسم_b9a97f.md

### ٱللَّه — ء ل ه — 2699 uses in the Quran
use profile: {"root": "ء ل ه", "lemma": "ٱللَّه", "total": 400, "groups": [{"label": "Clause subject or topic: acts, knows, wills, gives, or is described", "count": 212, "refs": ["2:15:1", "2:26:2", "2:77:4", "2:88:6", "2:113:23", "2:164:19", "2:187:15", "2:235:45", "3:156:30", "4:27:1"]}, {"label": "Object or selected complement of an action or attitude", "count": 73, "refs": ["2:200:5", "2:223:11", "3:32:8", "3:179:29", "4:64:21", "5:28:14", "7:65:8", "9:18:7", "10:22:31", "26:227:7"]}, {"label": "Noun-phrase relation or clause adjunct: possession, source, destination, route, or other link", "count": 115, "refs": ["1:1:2", "2:61:44", "2:120:13", "2:246:38", "3:73:11", "4:83:24", "5:15:20", "6:62:4", "9:20:13", "35:18:33"]}], "dominant": "In the 400-use sample, Allah is the clause subject or topic in 212 of 400 uses.", "outside": [{"ref": "2:200:5", "how": "Direct object of remembering."}, {"ref": "2:223:11", "how": "Object of an instruction to be mindful of Allah."}, {"ref": "3:32:8", "how": "Object of the command to obey."}, {"ref": "3:179:29", "how": "Complement of believing in Allah."}, {"ref": "4:64:21", "how": "Object of seeking forgiveness."}, {"ref": "5:28:14", "how": "Object of fearing."}, {"ref": "7:65:8", "how": "Object of worship."}, {"ref": "9:18:7", "how": "Complement of believing in Allah."}, {"ref": "10:22:31", "how": "Object of calling upon."}, {"ref": "26:227:7", "how": "Object of remembering."}, {"ref": "1:1:2", "how": "Part of the noun phrase “in the name of Allah.”"}, {"ref": "2:61:44", "how": "Source phrase specifying the source of anger."}, {"ref": "2:120:13", "how": "Possessor in “guidance of Allah.”"}, {"ref": "2:246:38", "how": "Route phrase in “in the way of Allah.”"}, {"ref": "3:73:11", "how": "Possessor in “guidance of Allah.”"}, {"ref": "4:83:24", "how": "Source in “favor of Allah.”"}, {"ref": "5:15:20", "how": "Source phrase, “from Allah.”"}, {"ref": "6:62:4", "how": "Destination in “to Allah.”"}, {"ref": "9:20:13", "how": "Locative phrase, “with/near Allah.”"}, {"ref": "35:18:33", "how": "Destination in “to Allah.”"}], "collocates": ["ٱلرَّسُول — the messenger", "سَبِيل — way, path", "ءَايَٰت — signs, verses", "رَبّ — lord", "ٱلْيَوْم ٱلْءَاخِر — the Last Day", "عَلِيم — knowing", "غَفُور — forgiving", "رَحِيم — merciful", "يَعْلَم — knows", "يَشَآء — wills"]}
every use: data/kwic/ءله_الله_803a5b.md

### رَّحْمَٰن — ر ح م — 57 uses in the Quran
use profile: {"root": "ر ح م", "lemma": "رَّحْمَٰن", "total": 57, "groups": [{"label": "Named in an identification, title, or formula", "count": 11, "refs": ["1:1:3", "1:3:1", "2:163:8", "20:90:13", "21:112:6", "25:60:8", "27:30:7", "55:1:1", "59:22:12", "67:29:3", "78:37:6"]}, {"label": "Grammatical subject or actor in an action, statement, or condition", "count": 16, "refs": ["19:61:5", "19:75:8", "19:88:3", "19:92:3", "19:96:8", "20:5:1", "20:109:9", "21:26:3", "25:59:14", "36:15:9", "36:23:7", "36:52:10", "43:20:4", "43:81:4", "67:19:11", "78:38:12"]}, {"label": "Target, recipient, or reference point of an act or attitude", "count": 20, "refs": ["13:30:17", "17:110:6", "19:18:4", "19:26:13", "19:44:8", "19:69:9", "19:78:6", "19:85:5", "19:87:8", "19:91:3", "19:93:9", "20:108:9", "21:42:7", "25:60:5", "36:11:7", "43:17:6", "43:33:10", "43:45:11", "50:33:3", "67:20:10"]}, {"label": "Source, possessor, or object within a linked noun phrase", "count": 10, "refs": ["19:45:8", "19:58:26", "21:36:15", "25:26:4", "25:63:2", "26:5:6", "41:2:3", "43:19:6", "43:36:5", "67:3:10"]}], "dominant": "no dominant role", "outside": [], "collocates": ["ٱلرَّحِيم — the Merciful", "وَلَد — child", "عَبْد — servant", "ذِكْر — remembrance", "عَهْد — covenant", "رَبّ — Lord", "ٱسْتَوَىٰ — be established", "ٱلْعَرْش — the Throne", "خَشِيَ — fear", "بِٱلْغَيْبِ — unseen", "وَعَدَ — promise", "ٱللَّه — Allah", "سَجَدَ — prostrate", "شَفَاعَة — intercession", "إِلَٰه — god or deity", "اِتَّخَذَ — take or claim as"]}
every use: data/kwic/رحم_رحمن_1ab85f.md

### رَّحِيم — ر ح م — 116 uses in the Quran
use profile: {"root": "ر ح م", "lemma": "رَّحِيم", "total": 116, "groups": [{"label": "Describes Allah or the Lord", "count": 114, "refs": ["1:1:4", "2:37:11", "2:143:45", "2:173:25", "4:29:23", "26:9:5", "33:43:13", "34:2:17", "36:58:5", "41:32:4"]}, {"label": "Describes the messenger toward the believers", "count": 1, "refs": ["9:128:14"]}, {"label": "Describes believers' relation to one another", "count": 1, "refs": ["48:29:9"]}], "dominant": "Describes Allah or the Lord in 114 of 116 uses", "outside": [{"ref": "9:128:14", "how": "Applied to the messenger; بِٱلْمُؤْمِنِينَ names the group toward whom the quality is directed."}, {"ref": "48:29:9", "how": "Plural description of the believers, followed by بَيْنَهُمْ to describe their relation within the group."}], "collocates": ["ٱللَّه (Allah)", "رَبّ (Lord)", "غَفُور (forgiving)", "ٱلتَّوَّاب (accepting repentance)", "رَءُوف (compassionate)", "ٱلْعَزِيز (mighty)", "ٱلرَّحْمَٰن (merciful)", "ٱلْمُؤْمِنِينَ (believers)"]}
every use: data/kwic/رحم_رحيم_2436e2.md

## Variant readings

(none)

## Turkish loanword cards

- ٱسْم (س م و) → isim: today Bir kişiyi veya şeyi tanıtan ad / Dil bilgisinde ad türündeki sözcük. Reader hears: Ad veya dil bilgisinde isim. Drift: Türkçede yaygın günlük anlamı ad, dil bilgisindeki anlamı da isim sözcük türüdür. Arapça kökün yükselme ve gök anlamları Türkçe isimde bulunmaz. Arabic keeps: B001 Arapça kök yükselme ve şöhret anlamlarını da içerir.; B004 Arapça kök ailesinde gök ve üstte bulunan şeyler de vardır.; B008 Arapçada iyi ün anlamı da bulunur.
- ٱللَّه (ء ل ه) → Allah: today İslam’da tek Tanrı’nın özel adı / Seslenme, şaşma ve yemin kalıplarında kullanılan ad. Reader hears: Tanrı’nın adı; dinî dilde doğrudan Allah. Drift: Türkçede çoğunlukla özel ad olarak kullanılır. Arapça kök ailesinde genel olarak tapınılan varlığı anlatan ilah da bulunur. Arabic keeps: B001 İlah, Allah’a özgü addan ayrı olarak genel anlamda tapınılan varlığı da anlatır.; B002 Arapçada Allah’la seslenme ve ant biçimleri de kök ailesinde yer alır.
- ٱللَّه (ء ل ه) → ilah: today Tanrı, tapınılan varlık / Dinî veya teolojik dilde tanrısal varlık. Reader hears: Genel anlamda Tanrı ya da tapınılan varlık. Drift: Türkçede Allah’a özgü addan farklı olarak genel bir tanrı veya tapınılan varlık anlamındadır. Arabic keeps: B001 Arapçada bu sözcük tapınma ve tapınılan varlıkla ilgili kullanımları kapsar.
- ٱللَّه (ء ل ه) → ilahi: today Tanrı’yla ilgili, kutsal / Dinî ezgi, özellikle tasavvuf veya halk dinî müziğinde söylenen eser. Reader hears: Bağlama göre Tanrı’yla ilgili olan ya da bir dinî ezgi. Drift: Sıfat olan biçim, Türkçede dinî ezgi adı olarak da yerleşmiştir. Arabic keeps: B001 Arapça kök ailesi tapınma ve tapınılan varlık anlamlarını da taşır. False friend: Türkçede ilahi, yalnızca 'Tanrı’yla ilgili' değil, bir dinî ezgi de demektir.
- رَّحْمَٰن (ر ح م) → Rahman: today Allah’a verilen, çok merhametli oluşunu bildiren ad / Erkek adı. Reader hears: Allah’ın çok merhametli oluşunu bildiren ad. Drift: Türkçede çoğunlukla Allah’ın adı ve kişi adı olarak kullanılır; genel bir sıfat kullanımı sınırlıdır. Arabic keeps: B001 Arapçada kök, merhamet ve şefkat bildiren başka biçimleri de kapsar.; B002 Arapça kök ailesinde yakın akrabalık anlamı da bulunur.; B003 Arapça kök ailesi döl yatağı anlamını da içerir.
- رَّحِيم (ر ح م) → Rahîm: today Allah’ın çok merhametli oluşunu bildiren adı / Erkek adı. Reader hears: Allah’ın merhametli oluşunu bildiren ad. Drift: Türkçede başlıca ilahî ad ve kişi adı olarak kullanılır; gündelik sıfat kullanımı sınırlıdır. Arabic keeps: B001 Arapça kök ailesi merhamet, şefkat ve iyilik etmeyi de kapsar.; B002 Türkçedeki ilahî ad, Arapçanın yakın akrabalık anlamını taşımaz.
- رَّحِيم (ر ح م) → rahim: today Kadın üreme organı; döl yatağı. Reader hears: Döl yatağı. Drift: Türkçede anatomik anlamla yerleşmiştir; Arapça kök ailesindeki yakın akrabalık anlamı Türkçe rahim sözcüğünde yaygın değildir. Arabic keeps: B002 Arapçada rahim, yakın soy bağı ve akrabalık ilişkisini de anlatır. False friend: Rahim döl yatağıdır; Rahîm ise dinî kullanımda 'çok merhametli' anlamlı addır.
- رَّحِيم (ر ح م) → rahmet: today Merhamet, acıma ve esirgeme / İyilik, nimet veya bereket. Reader hears: Merhamet, lütuf veya nimet. Drift: Türkçede merhamet ve iyilik anlamlarında kullanılır; çoğu zaman dinî dilde Allah’ın lütfunu anlatır. Arabic keeps: B002 Arapçada aynı kök yakın akrabalık ve soy bağını da anlatır.; B003 Arapçada kök ailesi döl yatağı anlamını da içerir.
- رَّحِيم (ر ح م) → merhamet: today Acıma, şefkat ve iyilik etme duygusu. Reader hears: Şefkat veya acıma duygusu. Drift: Türkçede çoğunlukla bir kişiye karşı duyulan şefkat ve acımayı anlatır; dinî bağlam dışında da yaygındır. Arabic keeps: B002 Arapça kök ailesi yakın akrabalık anlamını da taşır.; B003 Arapça kök ailesinde döl yatağına ilişkin anlamlar da bulunur.

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
