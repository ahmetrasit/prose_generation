# Ayah reading

You are reading ayah 1:2 with every branch of every one of its words open, inside its neighbourhood and its surah. You produce the record from which its commentary will be written: everything you hear, each finding anchored and contained, each with what it makes perceptible. You do not write the commentary; you output JSON.

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

- ref: 1:2.
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

# Ayah 1:2

## The ayah in its neighbourhood (1:1–7)

1:1| بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:2| ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ  ◀ focus
1:3| ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:4| مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5| إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6| ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7| صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

## Its words (ref surface | root | lemma | pos)

1:2:1 ٱلْحَمْدُ | ح م د | حَمْد | N
1:2:2 لِلَّهِ | ء ل ه | ٱللَّه | PN
1:2:3 رَبِّ | ر ب ب | رَبّ | N
1:2:4 ٱلْعَٰلَمِينَ | ع ل م | عَٰلَمِين | N

## Dictionary for its roots (branch | image | definition | tr: Turkish gloss)

### ح م د — 63 uses; here: 1:2:1 ٱلْحَمْدُ
B001 | الحمد خلاف الذم | الحمد والثناء على الفعل المحمود والشكر على النعمة وكثرة حمد الله
B002 | وجود الشيء محمودا | إيجاد الشخص أو الموضع محمودا مرضيا بعد تجربة وسؤال الرضا للأمر
B003 | المحمود كثير الخصال | الوصف أو الاسم لمن حمد أو كثرت خصاله المحمودة مثل محمود ومحمد وأحمد وحميد
B004 | حماداك الغاية المحمودة | صيغة حماداك وحماديات في معنى الغاية والقصارى وما يحمد بلوغه
B005 | يتحمد بالمنة | التحمد على الناس بمعنى المن وطلب الحمد على الإحسان أو الإنفاق
B006 | أحمد إليك الله | صيغة أحمد إليك الله ونحوها في حمد الله مع المخاطب أو شكر أياديه

### ء ل ه — 2851 uses; here: 1:2:2 لِلَّهِ
B001 | التعبد والمعبود | أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
B002 | اسم الله في القسم والنداء | اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه …

### و ل ه ~alt (documented alternative analysis) — 0 uses; here: 1:2:2 لِلَّهِ
B001 | الوَلَه والحيرة | ذهاب العقل أو اضطرابه من شدة الوجد، والحيرة، والحنين إلى المفقود أو المحبوب في الرجل والمرأة …
B002 | تَوْلِيه الوالدة عن ولدها | التوليه المتعدي: التفريق بين المرأة أو الوالدة وولدها حتى تصير والهة، وخاصة في البيع أو السبي
B003 | ماء مُولَه ذاهب | الماء أو العين إذا أرسل ماؤها في الصحراء فذهب
B004 | المُولَه العنكبوت | اسم المُولَه للعنكبوت كما في رواية الصحاح

### ر ب ب — 980 uses; here: 1:2:3 رَبِّ
B001 | ربوبية وملك وسيادة | الرب بمعنى الله تعالى، ومالك الشيء، وسيده المطاع، وصاحبه، ورب الدار والدابة والملك
B002 | إصلاح وتربية وإتمام | رب الشيء إذا أصلحه وأتمه وقام عليه، ورب النعمة والصنيعة والضيعة والولد والصبي، والتربية حالا فحالا
B003 | علم رباني | الرباني والربانيون بمعنى العلماء والحكماء وأهل العلم بالرب أو من يرب العلم ونفسه به
B004 | ربة وجماعات كثيرة | الربة والجماعات الكثيرة، والربيون إذا فسروا بالألوف أو الجماعات، ورباب القبائل لاجتماعهم
B005 | ربيب وربيبة ورابة | الربيب والربيبة للولد المربوب من زوج سابق، والراب والرابة لمن يقوم على أمره، والحاضنة
B006 | رُبّ خاثر وإصلاح به | الرُّبّ الطلاء الخاثر أو ثفل السمن والزيت، والسقاء والنحي والأديم والدواء والطعام إذا جعل فيه …
B007 | لزوم وإقامة ودوام | رب أو أرب بالمكان إذا أقام، ومرب الإبل ومرابها، وأربت السحابة أو الجنوب إذا دامت، والإرباب بمعنى …
B008 | رباب السحاب | الرباب والربابة للسحاب، والسحاب المتعلق أو المركب بعضه على بعض، وما سمي بذلك لتربية النبات أو دوام …
B009 | شاة رُبّى وحداثة | الشاة الرُّبّى والرباب لقرب العهد بالولادة أو لزوم البيت للبن، وربان الشيء بمعنى حدثانه وطراءته، …
B010 | ربابة تجمع القداح | الربابة للجلدة أو الوعاء الذي تجمع فيه القداح أو سهام الميسر، وجماعة السهام نفسها
B011 | ربابة عهد وميثاق | الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد
B012 | ربة نبات | الربة والربب لضرب من الشجر أو النبت أو البقلة التي تبقى خضراء
B013 | ماء رَبَب كثير | الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء
B014 | رَبْرَب قطيع | الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل
B015 | حرف رب وربما | رب وربما وربت وربه كحرف خافض أو حرف معنى للتقليل، ودخول ما أو التاء أو الهاء عليه
B016 | رُبَى حاجة وعقدة ونعمة | الربى بمعنى الحاجة، والرابة، والعقدة المحكمة، والنعمة والإحسان
B017 | رباني الملاحين | الرباني لرئيس الملاحين

### ع ل م — 854 uses; here: 1:2:4 ٱلْعَٰلَمِينَ
B001 | انكشاف الشيء للعارف | العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم
B002 | أثر يميز الشيء ويهدي إليه | العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب …
B003 | الخلق عالم يدل على صانعه | العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال
B004 | شق ظاهر في الشفة العليا | العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى
B005 | ماء كثير مجتمع في عيلم | العيلم بمعنى البحر أو البئر الكثيرة الماء
B006 | طائر جارح يسمى العلام | العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي
B007 | ذكر الضباع يسمى العيلام | العيلام بمعنى ذكر الضباع

## Scene lines touching its words, in the neighbourhood

- travel.route [9 words, 9 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 waymark | with: مَٰلِكِ 1:4:1 main course · نَعْبُدُ 1:5:2 road surface, fork · ٱهْدِنَا 1:6:1 guide, direction · ٱلصِّرَٰطَ 1:6:2 road · ٱلْمُسْتَقِيمَ 1:6:3 road · أَنْعَمْتَ 1:7:3 road, traveller · ٱلضَّآلِّينَ 1:7:9 stray · +1 more (all: data/scenes/s001/travel.route.md)
- trade.sale [6 words, 6 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B002 sale separation | with: ٱللَّهِ 1:1:2 sale separation · ٱلدِّينِ 1:4:3 bargain · نَعْبُدُ 1:5:2 goods · ٱلْمُسْتَقِيمَ 1:6:3 price, market · غَيْرِ 1:7:5 exchange
- wealth.property [8 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B016 need | with: مَٰلِكِ 1:4:1 wealth, provision · ٱهْدِنَا 1:6:1 wealth · ٱلصِّرَٰطَ 1:6:2 stinginess · ٱلْمُسْتَقِيمَ 1:6:3 provision · أَنْعَمْتَ 1:7:3 provision · غَيْرِ 1:7:5 provision · +1 more (all: data/scenes/s001/wealth.property.md)
- kin.birth_nursing [7 words, 4 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B002 mother child separation · رَبِّ 1:2:3: ر ب ب B005 foster child | with: ٱللَّهِ 1:1:2 mother child separation · ٱلرَّحْمَٰنِ 1:1:3 womb, birth · +3 more (all: data/scenes/s001/kin.birth_nursing.md)
- war.battle [7 words, 4 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B002 captive | with: ٱللَّهِ 1:1:2 captive · نَعْبُدُ 1:5:2 captive · نَسْتَعِينُ 1:5:4 battle · ٱهْدِنَا 1:6:1 captive · ٱلْمُسْتَقِيمَ 1:6:3 confrontation · أَنْعَمْتَ 1:7:3 rout
- pastoral.herding [6 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B007 fold, ر ب ب B014 herd | with: مَٰلِكِ 1:4:1 lead animal · نَسْتَعِينُ 1:5:4 herd · ٱهْدِنَا 1:6:1 lead animal · أَنْعَمْتَ 1:7:3 herd · ٱلضَّآلِّينَ 1:7:9 stray
- know.perceiving [5 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B003 knowing · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B001 knowing | with: بِسْمِ 1:1:1 perceiving · ٱهْدِنَا 1:6:1 ignorance · ٱلضَّآلِّينَ 1:7:9 forgetting
- animal.wild [4 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B014 wild cattle · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B007 hyena | with: نَسْتَعِينُ 1:5:4 wild ass · أَنْعَمْتَ 1:7:3 ostrich
- ritual.prayer [4 words, 4 roles] here: لِلَّهِ 1:2:2: ء ل ه B001 worship, ء ل ه B002 call | with: ٱللَّهِ 1:1:2 worship, call · ٱلدِّينِ 1:4:3 worship · ٱلْمُسْتَقِيمَ 1:6:3 standing, prayer performance
- rule.ownership [4 words, 6 roles] here: رَبِّ 1:2:3: ر ب ب B001 owner | with: مَٰلِكِ 1:4:1 possession · ٱلدِّينِ 1:4:3 master · نَعْبُدُ 1:5:2 servant, servitude, service
- speech.praise_blame [4 words, 4 roles] here: ٱلْحَمْدُ 1:2:1: ح م د B001 praise, ح م د B003 praise, ح م د B005 boasting, ح م د B006 thanks | with: بِسْمِ 1:1:1 boasting · ٱهْدِنَا 1:6:1 blame · أَنْعَمْتَ 1:7:3 praise
- water.well [4 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B013 abundant water · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B005 well | with: ٱلْمُسْتَقِيمَ 1:6:3 pulley · أَنْعَمْتَ 1:7:3 beam
- emotion.love [7 words, 3 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B001 longing | with: ٱللَّهِ 1:1:2 longing · ٱلرَّحْمَٰنِ 1:1:3 mercy · ٱهْدِنَا 1:6:1 affection · +3 more (all: data/scenes/s001/emotion.love.md)
- kin.lineage [6 words, 3 roles] here: رَبِّ 1:2:3: ر ب ب B004 tribe | with: ٱلرَّحْمَٰنِ 1:1:3 kin tie · ٱلْمُسْتَقِيمَ 1:6:3 clan · +3 more (all: data/scenes/s001/kin.lineage.md)
- motion.gather_scatter [5 words, 3 roles] here: رَبِّ 1:2:3: ر ب ب B004 crowd | with: بِسْمِ 1:1:1 gathering · نَعْبُدُ 1:5:2 dispersal · ٱلْمُسْتَقِيمَ 1:6:3 crowd · أَنْعَمْتَ 1:7:3 dispersal
- motion.passage [5 words, 3 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B003 vanishing | with: ٱللَّهِ 1:1:2 vanishing · ٱلصِّرَٰطَ 1:6:2 being swallowed, penetrating · ٱلضَّآلِّينَ 1:7:9 vanishing · +1 more (all: data/scenes/s001/motion.passage.md)
- speech.calling [5 words, 3 roles] here: ٱلْحَمْدُ 1:2:1: ح م د B003 naming · لِلَّهِ 1:2:2: ء ل ه B002 call | with: بِسْمِ 1:1:1 naming · ٱللَّهِ 1:1:2 call · أَنْعَمْتَ 1:7:3 answer, call
- rule.covenant [4 words, 3 roles] here: لِلَّهِ 1:2:2: ء ل ه B002 oath · رَبِّ 1:2:3: ر ب ب B011 covenant | with: ٱللَّهِ 1:1:2 oath · ٱلدِّينِ 1:4:3 witness
- war.protection [4 words, 3 roles] here: رَبِّ 1:2:3: ر ب ب B011 protection pact | with: نَسْتَعِينُ 1:5:4 ally · ٱهْدِنَا 1:6:1 protected client · ٱلْمَغْضُوبِ 1:7:6 ally
- body.mouth_throat [3 words, 3 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B004 lip | with: ٱلصِّرَٰطَ 1:6:2 throat, swallowing · +1 more (all: data/scenes/s001/body.mouth_throat.md)
- kin.household [3 words, 3 roles] here: رَبِّ 1:2:3: ر ب ب B002 provision, ر ب ب B005 dependant | with: ٱلْمُسْتَقِيمَ 1:6:3 provision · غَيْرِ 1:7:5 protection
- plant.growth_decay [3 words, 4 roles] here: رَبِّ 1:2:3: ر ب ب B002 growth, ر ب ب B012 greenness | with: بِسْمِ 1:1:1 growth, leaf · ٱلْمُسْتَقِيمَ 1:6:3 root
- speech.news [3 words, 3 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B001 message | with: بِسْمِ 1:1:1 report · مَٰلِكِ 1:4:1 messenger
- pastoral.livestock_wealth [7 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B014 livestock | with: نَعْبُدُ 1:5:2 livestock · ٱهْدِنَا 1:6:1 livestock · ٱلْمُسْتَقِيمَ 1:6:3 livestock · أَنْعَمْتَ 1:7:3 livestock · ٱلْمَغْضُوبِ 1:7:6 livestock · ٱلضَّآلِّينَ 1:7:9 lost animal
- trade.gift [5 words, 2 roles] here: ٱلْحَمْدُ 1:2:1: ح م د B005 favour · رَبِّ 1:2:3: ر ب ب B016 favour | with: نَسْتَعِينُ 1:5:4 favour · ٱهْدِنَا 1:6:1 gift · أَنْعَمْتَ 1:7:3 gift
- emotion.grief_joy [4 words, 2 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B001 grief | with: ٱللَّهِ 1:1:2 grief · نَعْبُدُ 1:5:2 grief · أَنْعَمْتَ 1:7:3 gladness
- animal.small [3 words, 2 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B004 spider | with: ٱللَّهِ 1:1:2 spider · مَٰلِكِ 1:4:1 bee
- quantity.more_less [3 words, 2 roles] here: ٱلْحَمْدُ 1:2:1: ح م د B004 completion · رَبِّ 1:2:3: ر ب ب B002 completion | with: أَنْعَمْتَ 1:7:3 increase
- ritual.idols_lots [3 words, 2 roles] here: لِلَّهِ 1:2:2: ء ل ه B001 cult · رَبِّ 1:2:3: ر ب ب B010 lot | with: ٱللَّهِ 1:1:2 cult
- rule.kingship [3 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B001 king | with: مَٰلِكِ 1:4:1 king · ٱلدِّينِ 1:4:3 dominion
- travel.departure_return [3 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B007 lodging | with: ٱلْمُسْتَقِيمَ 1:6:3 lodging · أَنْعَمْتَ 1:7:3 departure, lodging
- water.rain_cloud [3 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B007 cloud, ر ب ب B008 cloud | with: بِسْمِ 1:1:1 cloud, rain · غَيْرِ 1:7:5 rain
- animal.birds [2 words, 2 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B006 bird of prey | with: أَنْعَمْتَ 1:7:3 bird
- craft.dyeing [2 words, 2 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 marking | with: بِسْمِ 1:1:1 dye
- hunt.chase [2 words, 2 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B006 falcon | with: بِسْمِ 1:1:1 hunter
- land.mountain [2 words, 2 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 mountain | with: ٱلْمَغْضُوبِ 1:7:6 rock
- life.growing_up [2 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B009 youth | with: نَسْتَعِينُ 1:5:4 maturity
- pastoral.breeding [2 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B009 newborn | with: بِسْمِ 1:1:1 mating
- rule.leadership [2 words, 3 roles] here: رَبِّ 1:2:3: ر ب ب B017 chief | with: ٱلْمُسْتَقِيمَ 1:6:3 chief, council, deputy
- sign.marking [2 words, 2 roles] here: ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 mark, ع ل م B003 sign, ع ل م B004 mark | with: بِسْمِ 1:1:1 sign, mark
- tool.vessel [2 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B010 basket | with: ٱهْدِنَا 1:6:1 vessel
- travel.sea [2 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B017 steering | with: نَعْبُدُ 1:5:2 ship
- water.gathered [2 words, 2 roles] here: رَبِّ 1:2:3: ر ب ب B013 pool | with: ٱلْمُسْتَقِيمَ 1:6:3 stagnant water
- food.sweet_fat [3 words, 1 roles] here: رَبِّ 1:2:3: ر ب ب B006 sweet dish | with: ٱلصِّرَٰطَ 1:6:2 sweet dish · +1 more (all: data/scenes/s001/food.sweet_fat.md)
- craft.coating [2 words, 1 roles] here: رَبِّ 1:2:3: ر ب ب B006 coating | with: نَعْبُدُ 1:5:2 coating
- land.desert_sand [2 words, 1 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B003 desert | with: ٱللَّهِ 1:1:2 desert
- water.spring_stream [2 words, 1 roles] here: لِلَّهِ 1:2:2: و ل ه~alt B003 flow | with: ٱللَّهِ 1:1:2 flow
- weather.wind [2 words, 1 roles] here: رَبِّ 1:2:3: ر ب ب B007 wind | with: أَنْعَمْتَ 1:7:3 wind
- divine.lordship [13 words, 5 roles] here: لِلَّهِ 1:2:2: ء ل ه B001 worship · رَبِّ 1:2:3: ر ب ب B001 lord | with: ٱللَّهِ 1:1:2 worship · ٱلرَّحْمَٰنِ 1:1:3 mercy · مَٰلِكِ 1:4:1 lord · يَوْمِ 1:4:2 mercy judgment · ٱلدِّينِ 1:4:3 worship · نَعْبُدُ 1:5:2 worship · ٱلْمُسْتَقِيمَ 1:6:3 judgment · ٱلْمَغْضُوبِ 1:7:6 judgment · +3 more (all: data/scenes/s001/divine.lordship.md)
- moral.good_evil [3 words, 2 roles] here: ٱلْحَمْدُ 1:2:1: ح م د B002 good, ح م د B003 good | with: ٱلْمُسْتَقِيمَ 1:6:3 righteousness · أَنْعَمْتَ 1:7:3 good

## Scenes of its words that reach beyond the neighbourhood (at most 10 far words each, new roles first; every member in the file named)

(none)

## Plan from the window reading

- opens: I4 The master's household: owner, king and the owned one — A household under a master who owns and a king who rules. Dominion is exercised and obedience given. The owned one steps forward and speaks in the first person: you alone we serve.. Members: رَبِّ 1:2:3 B001 the owner and obeyed master (rabb al-dār); مَٰلِكِ 1:4:1 B002 the owner and possessor (mālik, canonical reading); مَٰلِكِ 1:4:1 B003 the king who rules (malik, mutawatir reading); ٱلدِّينِ 1:4:3 B004 dominion and subjugation, the one held in service; ٱلدِّينِ 1:4:3 B001 obedience and submission; نَعْبُدُ 1:5:2 B001 the ʿabd: the owned one, the opposite of free; نَعْبُدُ 1:5:2 B003 worship as humble, submissive obedience. Perceptible: In Turkish, ibadet has narrowed to ritual acts. Naʿbudu keeps the ʿabd, the whole person as someone's own. The two canonical readings keep owner (mālik) and king (malik) both alive in 1:4. The switch from third person (1:2–4) to 'You' (1:5) is the moment the owned ones stop speaking about the master and turn to face him.
- opens: I7 Gift gently sent, favor received, praise returned — A giver gently sends gifts to someone they hold dear and puts the recipient in a good, easy state. The recipient answers with praise and thanks.. Members: ٱلْحَمْدُ 1:2:1 B001 praise and thanks answering a favor; رَبِّ 1:2:3 B016 rubā: favor and kindness (minor); ٱهْدِنَا 1:6:1 B004 the hadiyya: a gentle gift sent to someone held in affection; ٱهْدِنَا 1:6:1 B001 guidance given gently (bi-luṭf); أَنْعَمْتَ 1:7:3 B001 the favor bestowed: good state and good life (niʿma); أَنْعَمْتَ 1:7:3 B002 softness and ease of life (minor). Perceptible: A Turkish reader already has hidayet and hediye without knowing they are one root. Heard together, guidance becomes something sent gently to someone loved. The surah opens with the thanks (ḥamd) and closes by naming the favor (anʿamta), so praise comes first and the favor is named only at the end.
- advances: I2 The branded herd, its owner, its lead animal and the stray — A herd of camels carries its owner's brand. It goes out from and returns to its owner's resting-place, following a lead animal at the front. One beast has strayed. It is left in a wasteland, and no one can tell who its owner is.. Members: بِسْمِ 1:1:1 B001 the brand (wasm, sima) by which an animal is known as someone's; documented alternative derivation of ism; رَبِّ 1:2:3 B001 the owner: rabb al-dābba, master of the beast; رَبِّ 1:2:3 B007 marabb al-ibil: the place where the camels stay; مَٰلِكِ 1:4:1 B008 the animal that goes in front and the rest follow (minor); ٱهْدِنَا 1:6:1 B003 the hādī: the front of the herd, the lead animal; أَنْعَمْتَ 1:7:3 B005 the herd itself (naʿam, camels), heard beside ḍāllīn (minor); ٱلضَّآلِّينَ 1:7:9 B005 the ḍālla: a beast left in a wasteland 'whose owner (rabb) is not known'; ٱلضَّآلِّينَ 1:7:9 B003 the thing gone from its owner, whose place cannot be found. Perceptible: The dictionary defines the ḍālla as the beast 'whose rabb is not known'. The word the surah uses for God in 1:2 is built into the definition of what it asks to be kept from in 1:7. So straying is relational, not only a wrong turn: it is losing one's tie to an owner who knows you. The surah is framed between the mark of belonging (bismi heard through wasm) and the unmarked stray.
- note: Ḥamd is thanks for favors not yet named. Rabb is the owner and master (rabb al-dābba) and also the one who raises stage by stage. ʿĀlamīn are creatures as marks and waymarks pointing to their maker.

Opened by earlier ayat:
- 1:1 opened I2 The branded herd, its owner, its lead animal and the stray
- 1:1 opened I3 The womb and the one who raises stage by stage

Window movement: The surah moves from being named and marked (1:1, bismi, which can also be heard as wasm, the owner's brand) to an owner who raises (rabb) wrapped on both sides in womb-mercy (1:1–3). It then reaches the owner and king of a Day on which what is owed is settled (1:4). At 1:5 the owned ones stop speaking about the master and speak to him, declaring service and leaning on him for help. From that posture they ask to be led, held up and gifted onto a road already trodden smooth by the favored. That road takes its walker in (1:6–7). Their thanks were given at the start, and they ask not to become the stray beast in the waste whose owner no one knows. The surah's arc runs from the mark of belonging to the danger of being an unmarked stray, with praise answering a favor it only names at the end.

## Concordance for its lemmas

### حَمْد — ح م د — 43 uses in the Quran
use profile: {"root": "ح م د", "lemma": "حَمْد", "total": 43, "groups": [{"label": "Hamd in al-ḥamdu li-llāh / lahu al-ḥamd attribution statements", "count": 28, "refs": ["1:2:1", "6:1:1", "6:45:6", "7:43:12", "10:10:11", "14:39:1", "16:75:22", "17:111:2", "18:1:1", "23:28:9", "27:15:7", "27:59:2", "27:93:2", "28:70:8", "29:63:17", "30:18:2", "31:25:10", "34:1:1", "34:1:12", "35:1:1", "35:34:2", "37:182:1", "39:29:14", "39:74:2", "39:75:14", "40:65:11", "45:36:2", "64:1:12"]}, {"label": "Hamd with a tasbīḥ verb", "count": 14, "refs": ["2:30:20", "13:13:3", "15:98:2", "17:44:13", "20:130:6", "25:58:8", "32:15:11", "39:75:8", "40:7:7", "40:55:9", "42:5:8", "50:39:6", "52:48:7", "110:3:2"]}, {"label": "Hamd with responding to a call", "count": 1, "refs": ["17:52:4"]}], "dominant": "Hamd in al-ḥamdu li-llāh / lahu al-ḥamd attribution statements, in 28 of 43 uses.", "outside": [{"ref": "2:30:20", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "13:13:3", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "15:98:2", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "17:44:13", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "17:52:4", "how": "Hamd follows بِـ in a clause about responding to a call."}, {"ref": "20:130:6", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "25:58:8", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "32:15:11", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "39:75:8", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "40:7:7", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "40:55:9", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "42:5:8", "how": "Hamd follows بِـ with a tasbīḥ verb."}, {"ref": "50:39:6", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "52:48:7", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}, {"ref": "110:3:2", "how": "Hamd follows بِـ with an imperative tasbīḥ verb."}], "collocates": ["ٱللَّه — Allah", "رَبّ — Lord", "سَبِّحْ / يُسَبِّحُ — glorify", "قَالَ / قُلْ — say", "ٱلْعَٰلَمِينَ — worlds"]}
every use: data/kwic/حمد_حمد_64aa03.md

### ٱللَّه — ء ل ه — 2699 uses in the Quran
use profile: {"root": "ء ل ه", "lemma": "ٱللَّه", "total": 400, "groups": [{"label": "Clause subject or topic: acts, knows, wills, gives, or is described", "count": 212, "refs": ["2:15:1", "2:26:2", "2:77:4", "2:88:6", "2:113:23", "2:164:19", "2:187:15", "2:235:45", "3:156:30", "4:27:1"]}, {"label": "Object or selected complement of an action or attitude", "count": 73, "refs": ["2:200:5", "2:223:11", "3:32:8", "3:179:29", "4:64:21", "5:28:14", "7:65:8", "9:18:7", "10:22:31", "26:227:7"]}, {"label": "Noun-phrase relation or clause adjunct: possession, source, destination, route, or other link", "count": 115, "refs": ["1:1:2", "2:61:44", "2:120:13", "2:246:38", "3:73:11", "4:83:24", "5:15:20", "6:62:4", "9:20:13", "35:18:33"]}], "dominant": "In the 400-use sample, Allah is the clause subject or topic in 212 of 400 uses.", "outside": [{"ref": "2:200:5", "how": "Direct object of remembering."}, {"ref": "2:223:11", "how": "Object of an instruction to be mindful of Allah."}, {"ref": "3:32:8", "how": "Object of the command to obey."}, {"ref": "3:179:29", "how": "Complement of believing in Allah."}, {"ref": "4:64:21", "how": "Object of seeking forgiveness."}, {"ref": "5:28:14", "how": "Object of fearing."}, {"ref": "7:65:8", "how": "Object of worship."}, {"ref": "9:18:7", "how": "Complement of believing in Allah."}, {"ref": "10:22:31", "how": "Object of calling upon."}, {"ref": "26:227:7", "how": "Object of remembering."}, {"ref": "1:1:2", "how": "Part of the noun phrase “in the name of Allah.”"}, {"ref": "2:61:44", "how": "Source phrase specifying the source of anger."}, {"ref": "2:120:13", "how": "Possessor in “guidance of Allah.”"}, {"ref": "2:246:38", "how": "Route phrase in “in the way of Allah.”"}, {"ref": "3:73:11", "how": "Possessor in “guidance of Allah.”"}, {"ref": "4:83:24", "how": "Source in “favor of Allah.”"}, {"ref": "5:15:20", "how": "Source phrase, “from Allah.”"}, {"ref": "6:62:4", "how": "Destination in “to Allah.”"}, {"ref": "9:20:13", "how": "Locative phrase, “with/near Allah.”"}, {"ref": "35:18:33", "how": "Destination in “to Allah.”"}], "collocates": ["ٱلرَّسُول — the messenger", "سَبِيل — way, path", "ءَايَٰت — signs, verses", "رَبّ — lord", "ٱلْيَوْم ٱلْءَاخِر — the Last Day", "عَلِيم — knowing", "غَفُور — forgiving", "رَحِيم — merciful", "يَعْلَم — knows", "يَشَآء — wills"]}
every use: data/kwic/ءله_الله_803a5b.md

### رَبّ — ر ب ب — 975 uses in the Quran
use profile: {"root": "ر ب ب", "lemma": "رَبّ", "total": 400, "groups": [{"label": "Directly addressed in petitions or requests", "count": 56, "refs": ["2:126:4", "2:128:1", "2:285:25", "3:8:1", "3:36:4", "4:75:15", "10:85:5", "14:41:1", "20:25:2", "66:8:35"]}, {"label": "Source or possessor in genitive and attribution phrases", "count": 112, "refs": ["2:105:16", "2:144:29", "3:49:10", "4:174:7", "5:67:8", "6:4:7", "7:137:14", "17:85:8", "32:3:8", "47:15:34"]}, {"label": "Subject or agent, or part of a defining statement", "count": 95, "refs": ["2:30:3", "3:195:3", "6:131:5", "7:22:16", "10:9:7", "11:107:12", "12:100:17", "16:125:13", "18:49:26", "19:21:4"]}, {"label": "Object or target of worship, trust, fear, remembrance, or belief", "count": 83, "refs": ["2:21:4", "3:43:3", "6:52:5", "7:55:2", "8:2:16", "13:21:10", "16:50:2", "18:28:6", "25:64:3", "35:18:23"]}, {"label": "Point of location, return, standing, or outcome", "count": 54, "refs": ["2:62:18", "2:262:18", "3:169:12", "6:38:21", "6:108:20", "7:125:4", "18:87:10", "32:11:10", "57:19:10", "75:30:2"]}], "dominant": "No dominant role; these counts describe the evenly spaced sample of 400 from the 975 uses.", "outside": [], "collocates": ["ءَايَٰت — signs", "رَحْمَة — mercy", "مَغْفِرَة — forgiveness", "عَذَاب — punishment", "رَسُول — messenger", "ٱلْعَٰلَمِينَ — the worlds", "غَفُور — forgiving", "رَحِيم — merciful", "مِن — from", "عِند — at, with"]}
every use: data/kwic/ربب_رب_7754a4.md

### عَٰلَمِين — ع ل م — 73 uses in the Quran
use profile: {"root": "ع ل م", "lemma": "عَٰلَمِين", "total": 73, "groups": [{"label": "As the complement of رَبّ (Lord)", "count": 42, "refs": ["1:2:4", "2:131:9", "5:28:16", "6:45:9", "6:71:39", "6:162:9", "7:54:32", "7:61:10", "7:67:10", "7:104:8", "7:121:4", "10:10:14", "10:37:22", "26:16:7", "26:23:5", "26:47:4", "26:77:6", "26:98:4", "26:109:11", "26:127:11", "26:145:11", "26:164:11", "26:180:11", "26:192:4", "27:8:14", "27:44:28", "28:30:19", "32:2:8", "37:87:4", "37:182:4", "39:75:17", "40:64:21", "40:65:14", "40:66:20", "41:9:14", "43:46:12", "45:36:8", "56:80:4", "59:16:17", "69:43:4", "81:29:8", "83:6:5"]}, {"label": "Population used for comparison, distinction, or a subgroup reference", "count": 14, "refs": ["2:47:11", "2:122:11", "2:251:27", "3:33:11", "3:42:12", "5:20:22", "5:115:17", "6:86:8", "7:80:13", "7:140:9", "26:165:4", "29:28:14", "44:32:6", "45:16:13"]}, {"label": "Recipients or audience of something", "count": 11, "refs": ["3:96:10", "6:90:16", "12:104:10", "21:71:8", "21:91:11", "21:107:5", "25:1:8", "29:15:6", "38:87:5", "68:52:5", "81:27:5"]}, {"label": "Group from whom independence is expressed", "count": 2, "refs": ["3:97:25", "29:6:10"]}, {"label": "People for whom injustice is negated", "count": 1, "refs": ["3:108:11"]}, {"label": "People from whom the addressees are said to be forbidden", "count": 1, "refs": ["15:70:5"]}, {"label": "People whose inner thoughts are known", "count": 1, "refs": ["29:10:31"]}, {"label": "Setting in which Noah is greeted", "count": 1, "refs": ["37:79:5"]}], "dominant": "The complement of رَبّ (Lord), in the phrase “Lord of the worlds,” in 42 of 73 uses.", "outside": [{"ref": "3:42:12", "how": "Names the population against which a subgroup, women, is compared."}, {"ref": "3:96:10", "how": "Names the recipients of guidance."}, {"ref": "3:97:25", "how": "Names the group from whom independence is expressed."}, {"ref": "3:108:11", "how": "Names those for whom injustice is negated."}, {"ref": "5:20:22", "how": "Names the population from which a recipient is singled out."}, {"ref": "6:90:16", "how": "Names the audience for a reminder."}, {"ref": "12:104:10", "how": "Names the audience for a reminder."}, {"ref": "15:70:5", "how": "Names the people from whom the addressees are said to be forbidden."}, {"ref": "21:71:8", "how": "Names the beneficiaries of a blessed land."}, {"ref": "21:91:11", "how": "Names the audience for a sign."}, {"ref": "21:107:5", "how": "Names the recipients of mercy."}, {"ref": "25:1:8", "how": "Names the audience for a warning."}, {"ref": "26:165:4", "how": "Names the population from whom male partners are selected."}, {"ref": "29:6:10", "how": "Names the group from whom independence is expressed."}, {"ref": "29:10:31", "how": "Names the people whose inner thoughts are known."}, {"ref": "29:15:6", "how": "Names the audience for a sign."}, {"ref": "37:79:5", "how": "Places Noah’s greeting among the worlds."}, {"ref": "38:87:5", "how": "Names the audience for a reminder."}, {"ref": "68:52:5", "how": "Names the audience for a reminder."}, {"ref": "81:27:5", "how": "Names the audience for a reminder."}], "collocates": ["رَبّ — Lord", "عَلَىٰ — over, above", "لِـ — for, to", "مِنْ — from, among", "ذِكْر / ذِكْرَىٰ — reminder, mention", "رَسُول — messenger", "ٱلْحَمْد — praise", "فَضْل / فَضَّلَ — favor, prefer", "آيَة — sign", "تَنزِيل — sending down, revelation", "أَجْر — payment, reward"]}
every use: data/kwic/علم_علمين_04884c.md

## Variant readings

(none)

## Turkish loanword cards

- حَمْد (ح م د) → hamd: today Övgü ve şükür; özellikle Allah’a yönelik övgü ve şükür / Hamdolsun kalıbında şükür bildirme. Reader hears: Dinî övgü ve şükür. Drift: Türkçede daha çok dinî övgü ve şükür için, özellikle Allah’ı anarken kullanılır. Arapçada kökün övme ve övülmeye dair başka kullanımları da vardır. Arabic keeps: B001 Arapça hamd, iyilik için teşekkürün yanı sıra övgü ve övgüyle anmayı kapsar.; B005 Arapçada kökün bir kullanımı, iyiliğini başa kakıp övgü beklemektir.
- حَمْد (ح م د) → Ahmet: today Erkek adı. Reader hears: Bir erkek adı. Drift: Arapçadaki övme anlamlı ad Türkçede yaygın bir özel ada dönüşmüştür; adı taşıyan kişi bu anlamı ayrıca ifade etmiş olmaz. Arabic keeps: B003 Arapçada Ahmed, övülen veya övülesi niteliklerle anılan kimseyi anlatan biçimlerden biridir. False friend: Türkçede Ahmet bir addır; tek başına 'övülen' anlamında kullanılmaz.
- حَمْد (ح م د) → Mehmet: today Erkek adı. Reader hears: Çok yaygın bir erkek adı. Drift: Muhammed biçiminin Türkçede yerleşmiş adı olarak kullanılır; övgü anlamı bugünkü ad kullanımında şeffaf değildir. Arabic keeps: B003 Arapçada Muhammed, çokça övülen kimseyi anlatan ad biçimidir. False friend: Türkçede Mehmet, çoğunlukla özel ad olarak algılanır; 'övülen' anlamını taşımaz.
- حَمْد (ح م د) → Mahmut: today Erkek adı. Reader hears: Bir erkek adı. Drift: Arapçadaki övülmüş anlamlı ad Türkçede özel ada dönüşmüştür. Arabic keeps: B003 Arapçada Mahmûd, övülmüş kimseyi anlatan addır. False friend: Türkçede Mahmut adı gündelik kullanımda 'övülmüş' anlamına gelmez.
- ٱللَّه (ء ل ه) → Allah: today İslam’da tek Tanrı’nın özel adı / Seslenme, şaşma ve yemin kalıplarında kullanılan ad. Reader hears: Tanrı’nın adı; dinî dilde doğrudan Allah. Drift: Türkçede çoğunlukla özel ad olarak kullanılır. Arapça kök ailesinde genel olarak tapınılan varlığı anlatan ilah da bulunur. Arabic keeps: B001 İlah, Allah’a özgü addan ayrı olarak genel anlamda tapınılan varlığı da anlatır.; B002 Arapçada Allah’la seslenme ve ant biçimleri de kök ailesinde yer alır.
- ٱللَّه (ء ل ه) → ilah: today Tanrı, tapınılan varlık / Dinî veya teolojik dilde tanrısal varlık. Reader hears: Genel anlamda Tanrı ya da tapınılan varlık. Drift: Türkçede Allah’a özgü addan farklı olarak genel bir tanrı veya tapınılan varlık anlamındadır. Arabic keeps: B001 Arapçada bu sözcük tapınma ve tapınılan varlıkla ilgili kullanımları kapsar.
- ٱللَّه (ء ل ه) → ilahi: today Tanrı’yla ilgili, kutsal / Dinî ezgi, özellikle tasavvuf veya halk dinî müziğinde söylenen eser. Reader hears: Bağlama göre Tanrı’yla ilgili olan ya da bir dinî ezgi. Drift: Sıfat olan biçim, Türkçede dinî ezgi adı olarak da yerleşmiştir. Arabic keeps: B001 Arapça kök ailesi tapınma ve tapınılan varlık anlamlarını da taşır. False friend: Türkçede ilahi, yalnızca 'Tanrı’yla ilgili' değil, bir dinî ezgi de demektir.
- رَبّ (ر ب ب) → Rab: today Tanrı, Allah; özellikle dua ve dinî dilde kullanılan ad. Reader hears: Tanrı veya Allah. Drift: Türkçede büyük ölçüde Tanrı’ya verilen bir ad olarak özelleşmiştir. Arapçada aynı sözcük bir şeyin sahibi veya yöneticisi için de kullanılabilir. Arabic keeps: B001 Arapçada evin, hayvanın veya başka bir şeyin sahibi ve yöneticisi anlamları da vardır.
- رَبّ (ر ب ب) → terbiye: today Yetiştirme, eğitim ve görgü kazandırma / Davranışları düzeltme veya disipline etme. Reader hears: Eğitim, görgü veya disiplin. Drift: Türkçede insan yetiştirme, eğitim ve davranış disiplini anlamlarına yerleşmiştir; bakım ve aşama aşama tamamlama anlamı daha az belirgindir. Arabic keeps: B002 Arapçada bir şeyi gözetme, onarma ve aşama aşama yetiştirip tamamlama anlamları bulunur.
- عَٰلَمِين (ع ل م) → âlem: today Dünya, evren; yaratılmışların bütünü / Bir çevre, topluluk veya ortam. Reader hears: Evren, dünya veya bütün yaratılmışlar. Drift: Türkçede hem evren hem de çevre ya da topluluk anlamlarıyla kullanılır. Dinî çevirilerde âlemler yaratılmışların tümünü çağrıştırabilir. Arabic keeps: B003 Arapçada âlem ve âlemin, yaratılmışların bütünü veya yaratık sınıfları anlamına gelir.; B002 Arapça kök ailesinde işaret, bayrak ve yol gösteren belirti anlamları da vardır.
- عَٰلَمِين (ع ل م) → ilim: today Bilgi, bilme / Bilim veya bir bilgi alanı; özellikle dinî ilimler. Reader hears: Bilgi, bilim ya da dinî bilgi. Drift: Türkçede bilgi ve bilim alanı anlamlarında, kimi zaman daha resmî veya dinî bir tonda kullanılır. Arabic keeps: B001 Arapçada kök, bilme, kavrama, öğrenme ve öğretmeyi kapsar.
- عَٰلَمِين (ع ل م) → âlim: today Bilgin; özellikle dinî bilgisi olan kişi. Reader hears: Bilgin veya din bilgini. Drift: Türkçede daha çok saygın bir bilgin veya din bilgini için kullanılır; Arapça kökün bilme ve öğretme anlamları Türkçedeki adın dışında kalır. Arabic keeps: B001 Arapçada kök bilme, öğrenme ve öğretmeyi de kapsar.; B002 Arapçada kök ailesi işaret ve alamet anlamlarını da içerir.
- عَٰلَمِين (ع ل م) → alâmet: today Belirti, işaret / Bir durumu veya niteliği gösteren iz. Reader hears: Belirti veya ayırt edici işaret. Drift: Türkçede çoğunlukla bir şeyin belirtisi veya işareti olarak kullanılır. Arabic keeps: B002 Arapçada alamet, bayrak, sınır işareti ve yol gösteren belirti anlamlarını da kapsar.

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
