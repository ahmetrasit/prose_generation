# Ayah reading

You are reading ayah 1:7 with every branch of every one of its words open, inside its neighbourhood and its surah. You produce the record from which its commentary will be written: everything you hear, each finding anchored and contained, each with what it makes perceptible. You do not write the commentary; you output JSON.

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

- ref: 1:7.
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

# Ayah 1:7

## The ayah in its neighbourhood (1:1–7)

1:1| بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:2| ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1:3| ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:4| مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5| إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6| ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7| صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ  ◀ focus

## Its words (ref surface | root | lemma | pos)

1:7:1 صِرَٰطَ | ص ر ط | صِرَٰط | N
1:7:3 أَنْعَمْتَ | ن ع م | أَنْعَمَ | V
1:7:5 غَيْرِ | غ ي ر | غَيْر | N
1:7:6 ٱلْمَغْضُوبِ | غ ض ب | مَغْضُوب | N
1:7:9 ٱلضَّآلِّينَ | ض ل ل | ضَآلّ | N

## Dictionary for its roots (branch | image | definition | tr: Turkish gloss)

### ص ر ط — 45 uses; here: 1:7:1 صِرَٰطَ
B001 | الطريق المستقيم | الصراط والسراط والزراط بمعنى الطريق، وخاصة الطريق المستقيم
B002 | الغيبة في المرور والبلع | سرط الطعام بمعنى بلعه وغيبته في المرور، وما يتصل بسهولة الابتلاع وسعة الحلق
B003 | السيف القاطع الماضي في الضربة | إطلاق السراط على السيف القاطع النافذ الماضي في الضريبة

### س ر ط ~alt (reading sirāṭa (ibdāl)) — 0 uses; here: 1:7:1 صِرَٰطَ
B001 | ابتلاع يغيب في الحلق | سرط الطعام واسترطه وسرعة الابتلاع بلا مضغ ووصف الآكل السريع
B002 | طريق يسترط سالكه | السراط بمعنى الطريق الواضح أو المستسهل والمنهاج الواضح، ولغة السين في الصراط
B003 | حلوى تسترط | السرطراط والسرطراط للفالوذج، وما سمي بذلك لاستلذاذ أكله وإساغته
B004 | قطع يمضي في الضريبة | السراط أو السراطي للسيف القاطع والقطع
B005 | أخذ يبتلع وقضاء يدفع | مثل الأخذ سريطى أو سريط والقضاء ضريطى أو ضريط، في حب الأخذ وكراهة الإعطاء
B006 | حيوان ماء يسمى السرطان | السرطان من خلق الماء
B007 | برج السماء المسمى السرطان | السرطان برج في السماء أو من بروج السماء
B008 | داء يسمى السرطان | داء السرطان في قائمة الدابة أو رسغها، وما ذكر للإنسان في حلقه

### ن ع م — 140 uses; here: 1:7:3 أَنْعَمْتَ
B001 | حسن الحال والنعمة | النعمة والنعمى والنعماء والنعيم والإنعام، بمعنى حسن الحال وطيب العيش والمن والعطاء والإحسان الموصل …
B002 | اللين والنعومة ورفاه العيش | نعم الشيء إذا لان، والناعم والمنعم والمناعم، والتنعم وطيب العيش والترف، والطعام أو الشخص الموصوف …
B003 | مدح الشيء بنعم | نعم المقابلة لبئس، ونعم الشيء، ونعما، وفبها ونعمت، حيث تكون اللفظة فعلا أو صيغة مدح واستحسان.
B004 | الجواب بنعم والتصديق | نعم حرفا أو كلمة جواب، للتصديق والإيجاب والعدة، وما اتصل بذلك مثل أنعم له أي قال له نعم.
B005 | مال الأنعام والإبل | النعم والأنعام، خصوصا الإبل، وبالتوسيع الإبل والبقر والغنم والبهائم الراعية حيث نصت المصادر على ذلك.
B006 | النعام والنعامة الطائر | النعامة والنعام للطائر المعروف، ذكرا أو أنثى، وما يذكر من جنسه وصفاته المباشرة.
B007 | ما سمي نعامة تشبيها بالهيئة | المسميات المشبهة بالنعامة في الهيئة أو البعد أو السرعة، مثل خشبة البئر والظلة على رأس الجبل وباطن …
B008 | طيران النعامة وتفرق القوم | شالت نعامتهم وخفت نعامتهم وأضحوا نعاما ونحوها، حيث يدل التعبير على الارتحال أو التفرق أو ذهاب العز …
B009 | النعامى ريح لينة | النعامى، وهي ريح الجنوب اللينة أو الأرطب والأبل في الهبوب.
B010 | زاد وأنعم في الفعل | فعل كذا وأنعم بمعنى زاد، وأنعم في الدق أو الإحسان بمعنى بالغ وزاد، وأنعما في الخبر بمعنى زادا على …
B011 | موافقة المكان وطيب المقام | أتيت أرضا فتنعمتني أو فنعمتني، إذا وافقت الشخص وأقام بها أو طاب له النزول.
B012 | المشي على القدم وابتذالها | تنعمت فلانا إذا أتيته على غير دابة أو طلبته ماشيا، وتنعم القدمين أي ابتذلهما، وما قرب منه من المشي …
B013 | نعم الله بك عينا وقرة العين | نعم الله بك عينا، ونعمك عينا، ونعمى عين، ونعمة عين، ونعم عين، ونعام عين، بمعنى قرة العين والإكرام …

### غ ي ر — 154 uses; here: 1:7:5 غَيْرِ
B001 | الصلاح والمنفعة بالميرة والسقي والإصلاح | ميرة الأهل ونفعهم، وسقي الأرض أو القوم بالغيث، وإصلاح الرحال أو شأن الراحلة.
B002 | الغَيْر في الدية | اسم الغَيْر أو الغِيرة للدية، وأخذ الدية بدل القود.
B003 | تغيير الصورة أو إبدال الشيء بغيره | تغيير الشيء فتغيره، وتغير الحال، وتبديل الشيء بغيره، ودفع المنكر بغيره من الحق، والمبادلة والبدل.
B004 | الغَيْرة على الأهل | الغَيْرة المفتوحة على الأهل، ووصف الرجل أو المرأة بالغيور وغيران وغيرى، ولغة الغار في الغيرة.
B005 | السوى والخلاف والاستثناء والنفي | كون الشيء سوى غيره وخلافه، واستعمال غير صفة أو اسما أو أداة استثناء، ومعنى لا، ونفي صورة أو ذات، …

### غ ض ب — 24 uses; here: 1:7:6 ٱلْمَغْضُوبِ
B001 | اشتداد السخط وثورانه للانتقام | الغضب ضد الرضا، وغضب عليه، وأوصاف غضبان وغضوب وغضبة بمعنى كثير الغضب أو سريع الغضب، ووصف الغضب …
B002 | الغضب لشخص حي أو به بعد موته | التعبير غضبت لفلان إذا كان حيا وغضبت به إذا كان ميتا.
B003 | المراغمة والمخالفة | غاضبه ومغاضبا بمعنى راغمه ومراغما لقومه.
B004 | صلابة الصخرة وتماسكها | الغضبة بمعنى الصخرة الصلبة أو المتراكمة أو المستديرة في الجبل.
B005 | غلظ الجسم وشدة الحمرة | رجل غضاب أي غليظ الجلد، ورجل غضب أو أحمر غضب بمعنى أحمر غليظ أو شديد الحمرة.
B006 | تورم العين وما حولها | الغضب أو غضبت عين الرجل بمعنى بخصة في الجفن الأعلى أو ورم ما حول العين أو تحتها.
B007 | العبوس والضجر والعظم في وصف الحيوان أو الشخص | غضوب صفة للعبوس أو الضجر، كناقة غضوب أو امرأة غضوب، ويدخل فيه الغضوب للحية العظيمة كما في Maqayis.
B008 | جلد صلب أو مطوي كدرقة | الغضبة أو الغضب للجلد الصلب: جلد المسن من الوعول، جلد السلحفاة، وقطعة من جلد البعير تطوى كدرقة.

### ض ل ل — 191 uses; here: 1:7:9 ٱلضَّآلِّينَ
B001 | الضلال عن الهدى والقصد | الجور عن القصد وترك الهدى والرشد والوقوع في الغواية والباطل والتيه عن الطريق
B002 | الغيبوبة والخفاء | خفاء الشيء وغيبوبته واندثاره في غيره أو في الأرض ودفن الميت حتى يغيب
B003 | فقدان الشيء | ذهاب الشيء من صاحبه أو عدم الاهتداء إلى موضعه في المتحرك والثابت والمكان وذهاب الدم بلا ثأر
B004 | ضياع الحفظ | نسيان الشيء وغياب الحفظ عن صاحبه أو غياب الشيء عن الحفظ
B005 | الضالّة في المضيعة | البهيمة ولا سيما الإبل إذا بقيت في مضيعة لا يعرف ربها والذكر والأنثى فيها سواء

## Scene lines touching its words, in the neighbourhood

- travel.route [9 words, 9 roles] here: صِرَٰطَ 1:7:1: ص ر ط B001 road, س ر ط~alt B002 road · أَنْعَمْتَ 1:7:3: ن ع م B007 road, ن ع م B012 traveller · ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 stray, ض ل ل B003 stray | with: ٱلْعَٰلَمِينَ 1:2:4 waymark · مَٰلِكِ 1:4:1 main course · نَعْبُدُ 1:5:2 road surface, fork · ٱهْدِنَا 1:6:1 guide, direction · ٱلصِّرَٰطَ 1:6:2 road · ٱلْمُسْتَقِيمَ 1:6:3 road
- trade.sale [6 words, 6 roles] here: غَيْرِ 1:7:5: غ ي ر B003 exchange | with: ٱللَّهِ 1:1:2 sale separation · ٱلدِّينِ 1:4:3 bargain · نَعْبُدُ 1:5:2 goods · ٱلْمُسْتَقِيمَ 1:6:3 price, market · +1 more (all: data/scenes/s001/trade.sale.md)
- body.limbs [7 words, 5 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B008 joint · أَنْعَمْتَ 1:7:3: ن ع م B007 foot, ن ع م B012 foot | with: بِسْمِ 1:1:1 back · مَٰلِكِ 1:4:1 leg · ٱهْدِنَا 1:6:1 neck · ٱلصِّرَٰطَ 1:6:2 joint · ٱلْمُسْتَقِيمَ 1:6:3 leg, back
- wealth.property [8 words, 4 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B005 stinginess · أَنْعَمْتَ 1:7:3: ن ع م B001 provision · غَيْرِ 1:7:5: غ ي ر B001 provision | with: رَبِّ 1:2:3 need · مَٰلِكِ 1:4:1 wealth, provision · ٱهْدِنَا 1:6:1 wealth · ٱلصِّرَٰطَ 1:6:2 stinginess · ٱلْمُسْتَقِيمَ 1:6:3 provision
- war.battle [7 words, 4 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B008 rout | with: ٱللَّهِ 1:1:2 captive · نَعْبُدُ 1:5:2 captive · نَسْتَعِينُ 1:5:4 battle · ٱهْدِنَا 1:6:1 captive · ٱلْمُسْتَقِيمَ 1:6:3 confrontation · +1 more (all: data/scenes/s001/war.battle.md)
- body.strength [6 words, 4 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B005 firmness | with: مَٰلِكِ 1:4:1 firmness · نَعْبُدُ 1:5:2 strength · نَسْتَعِينُ 1:5:4 strength · ٱهْدِنَا 1:6:1 frailty · ٱلْمُسْتَقِيمَ 1:6:3 build, strength
- pastoral.herding [6 words, 4 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B005 herd · ٱلضَّآلِّينَ 1:7:9: ض ل ل B005 stray | with: رَبِّ 1:2:3 fold, herd · مَٰلِكِ 1:4:1 lead animal · نَسْتَعِينُ 1:5:4 herd · ٱهْدِنَا 1:6:1 lead animal
- know.perceiving [5 words, 4 roles] here: ٱلضَّآلِّينَ 1:7:9: ض ل ل B004 forgetting | with: بِسْمِ 1:1:1 perceiving · رَبِّ 1:2:3 knowing · ٱلْعَٰلَمِينَ 1:2:4 knowing · ٱهْدِنَا 1:6:1 ignorance
- war.arms [5 words, 4 roles] here: صِرَٰطَ 1:7:1: ص ر ط B003 sword, س ر ط~alt B004 sword · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B008 shield | with: مَٰلِكِ 1:4:1 shaft · ٱهْدِنَا 1:6:1 arrow · ٱلصِّرَٰطَ 1:6:2 sword
- animal.wild [4 words, 4 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B006 ostrich | with: رَبِّ 1:2:3 wild cattle · ٱلْعَٰلَمِينَ 1:2:4 hyena · نَسْتَعِينُ 1:5:4 wild ass
- speech.praise_blame [4 words, 4 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B003 praise | with: بِسْمِ 1:1:1 boasting · ٱلْحَمْدُ 1:2:1 praise, boasting, thanks · ٱهْدِنَا 1:6:1 blame
- water.well [4 words, 4 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B007 beam | with: رَبِّ 1:2:3 abundant water · ٱلْعَٰلَمِينَ 1:2:4 well · ٱلْمُسْتَقِيمَ 1:6:3 pulley
- dwelling.settlement [5 words, 3 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B011 dwelling place | with: بِسْمِ 1:1:1 market · ٱلدِّينِ 1:4:3 town · نَسْتَعِينُ 1:5:4 town · ٱلْمُسْتَقِيمَ 1:6:3 dwelling place, market
- motion.gather_scatter [5 words, 3 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B008 dispersal | with: بِسْمِ 1:1:1 gathering · رَبِّ 1:2:3 crowd · نَعْبُدُ 1:5:2 dispersal · ٱلْمُسْتَقِيمَ 1:6:3 crowd
- motion.passage [5 words, 3 roles] here: صِرَٰطَ 1:7:1: ص ر ط B002 being swallowed, ص ر ط B003 penetrating, س ر ط~alt B004 penetrating · ٱلضَّآلِّينَ 1:7:9: ض ل ل B002 vanishing | with: ٱللَّهِ 1:1:2 vanishing · ٱلصِّرَٰطَ 1:6:2 being swallowed, penetrating · +1 more (all: data/scenes/s001/motion.passage.md)
- sky.bodies [5 words, 3 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B007 constellation · أَنْعَمْتَ 1:7:3: ن ع م B007 constellation | with: بِسْمِ 1:1:1 moon · ٱلصِّرَٰطَ 1:6:2 constellation · ٱلْمُسْتَقِيمَ 1:6:3 zenith
- speech.calling [5 words, 3 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B004 answer, ن ع م B013 call | with: بِسْمِ 1:1:1 naming · ٱللَّهِ 1:1:2 call · ٱلْحَمْدُ 1:2:1 naming · +1 more (all: data/scenes/s001/speech.calling.md)
- war.protection [4 words, 3 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B002 ally | with: رَبِّ 1:2:3 protection pact · نَسْتَعِينُ 1:5:4 ally · ٱهْدِنَا 1:6:1 protected client
- animal.reptile_fish [3 words, 3 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B006 crab · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B007 snake, غ ض ب B008 turtle | with: ٱلصِّرَٰطَ 1:6:2 crab
- body.mouth_throat [3 words, 3 roles] here: صِرَٰطَ 1:7:1: ص ر ط B002 throat, س ر ط~alt B001 swallowing, س ر ط~alt B008 throat | with: ٱلْعَٰلَمِينَ 1:2:4 lip · ٱلصِّرَٰطَ 1:6:2 throat, swallowing
- kin.household [3 words, 3 roles] here: غَيْرِ 1:7:5: غ ي ر B004 protection | with: رَبِّ 1:2:3 provision, dependant · ٱلْمُسْتَقِيمَ 1:6:3 provision
- rule.obedience [3 words, 3 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B003 defiance | with: ٱلدِّينِ 1:4:3 obedience · نَعْبُدُ 1:5:2 submission
- travel.open_land [3 words, 3 roles] here: ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 getting lost, ض ل ل B005 waste | with: بِسْمِ 1:1:1 waste · مَٰلِكِ 1:4:1 water source
- war.vengeance [3 words, 3 roles] here: غَيْرِ 1:7:5: غ ي ر B002 blood money · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 vengeance, غ ض ب B002 vengeance · ٱلضَّآلِّينَ 1:7:9: ض ل ل B003 unavenged blood
- body.illness [7 words, 2 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B008 disease | with: ٱلرَّحْمَٰنِ 1:1:3 pain · ٱلصِّرَٰطَ 1:6:2 disease · ٱلْمُسْتَقِيمَ 1:6:3 pain, disease · +3 more (all: data/scenes/s001/body.illness.md)
- pastoral.livestock_wealth [7 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B005 livestock · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B007 livestock · ٱلضَّآلِّينَ 1:7:9: ض ل ل B003 lost animal, ض ل ل B005 lost animal | with: رَبِّ 1:2:3 livestock · نَعْبُدُ 1:5:2 livestock · ٱهْدِنَا 1:6:1 livestock · ٱلْمُسْتَقِيمَ 1:6:3 livestock
- motion.pace [5 words, 2 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B001 haste · أَنْعَمْتَ 1:7:3: ن ع م B012 slowness | with: نَعْبُدُ 1:5:2 haste · ٱهْدِنَا 1:6:1 slowness · ٱلصِّرَٰطَ 1:6:2 haste
- trade.gift [5 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B001 gift | with: ٱلْحَمْدُ 1:2:1 favour · رَبِّ 1:2:3 favour · نَسْتَعِينُ 1:5:4 favour · ٱهْدِنَا 1:6:1 gift
- emotion.grief_joy [4 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B013 gladness | with: ٱللَّهِ 1:1:2 grief · نَعْبُدُ 1:5:2 grief · +1 more (all: data/scenes/s001/emotion.grief_joy.md)
- emotion.pride [3 words, 2 roles] here: غَيْرِ 1:7:5: غ ي ر B004 honour | with: بِسْمِ 1:1:1 honour, pride · نَعْبُدُ 1:5:2 honour, pride
- quantity.more_less [3 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B010 increase | with: ٱلْحَمْدُ 1:2:1 completion · رَبِّ 1:2:3 completion
- trade.debt [3 words, 2 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B005 repayment | with: ٱلدِّينِ 1:4:3 debt · ٱلصِّرَٰطَ 1:6:2 repayment
- travel.departure_return [3 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B008 departure, ن ع م B011 lodging | with: رَبِّ 1:2:3 lodging · ٱلْمُسْتَقِيمَ 1:6:3 lodging
- travel.mount [3 words, 2 roles] here: غَيْرِ 1:7:5: غ ي ر B001 saddle | with: نَعْبُدُ 1:5:2 exhaustion · ٱلْمُسْتَقِيمَ 1:6:3 exhaustion
- water.rain_cloud [3 words, 2 roles] here: غَيْرِ 1:7:5: غ ي ر B001 rain | with: بِسْمِ 1:1:1 cloud, rain · رَبِّ 1:2:3 cloud
- animal.birds [2 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B006 bird | with: ٱلْعَٰلَمِينَ 1:2:4 bird of prey
- body.eye [2 words, 3 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B006 eyelid | with: ٱلْمُسْتَقِيمَ 1:6:3 eye, blindness
- emotion.anger [2 words, 3 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 anger, غ ض ب B002 anger, غ ض ب B003 enmity, غ ض ب B007 irritability | with: نَعْبُدُ 1:5:2 anger
- food.eating [2 words, 2 roles] here: صِرَٰطَ 1:7:1: ص ر ط B002 swallowing, س ر ط~alt B001 gulp, س ر ط~alt B003 swallowing | with: ٱلصِّرَٰطَ 1:6:2 swallowing, gulp
- land.mountain [2 words, 2 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B004 rock | with: ٱلْعَٰلَمِينَ 1:2:4 mountain
- food.sweet_fat [3 words, 1 roles] here: صِرَٰطَ 1:7:1: س ر ط~alt B003 sweet dish | with: رَبِّ 1:2:3 sweet dish · ٱلصِّرَٰطَ 1:6:2 sweet dish
- weather.wind [2 words, 1 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B009 wind | with: رَبِّ 1:2:3 wind
- divine.lordship [13 words, 5 roles] here: ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 judgment | with: ٱللَّهِ 1:1:2 worship · ٱلرَّحْمَٰنِ 1:1:3 mercy · رَبِّ 1:2:3 lord · مَٰلِكِ 1:4:1 lord · يَوْمِ 1:4:2 mercy judgment · ٱلدِّينِ 1:4:3 worship · نَعْبُدُ 1:5:2 worship · ٱلْمُسْتَقِيمَ 1:6:3 judgment · +4 more (all: data/scenes/s001/divine.lordship.md)
- moral.guidance_error [5 words, 3 roles] here: صِرَٰطَ 1:7:1: ص ر ط B001 right guidance, س ر ط~alt B002 right guidance · ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 straying | with: ٱهْدِنَا 1:6:1 right guidance · ٱلصِّرَٰطَ 1:6:2 right guidance · ٱلْمُسْتَقِيمَ 1:6:3 rectitude
- moral.good_evil [3 words, 2 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B001 good, ن ع م B003 good | with: ٱلْحَمْدُ 1:2:1 good · ٱلْمُسْتَقِيمَ 1:6:3 righteousness
- moral.truth_falsehood [2 words, 1 roles] here: أَنْعَمْتَ 1:7:3: ن ع م B004 confirmation | with: ٱلدِّينِ 1:4:3 confirmation

## Scenes of its words that reach beyond the neighbourhood (at most 10 far words each, new roles first; every member in the file named)

(none)

## Plan from the window reading

- completes: I1 The trodden, marked road that takes its walker in — A desert route with waymarks standing along it and a clear middle course. Many feet have trodden its surface smooth. A guide gently shows the way and keeps the heading. The road is straight and takes its walker in as easily as a throat takes a morsel. Someone who leaves it wanders off the course and disappears into the waste.. Members: ٱلْعَٰلَمِينَ 1:2:4 B002 waymarks (maʿālim al-ṭarīq, ʿalam as mountain or marker) standing along the route; creatures as marks that point the way; مَٰلِكِ 1:4:1 B006 malak al-ṭarīq: the middle and main course of the road (minor); نَعْبُدُ 1:5:2 B005 the road surface: ṭarīq muʿabbad, a road made smooth and level by being walked; ٱهْدِنَا 1:6:1 B001 the guide who shows the road gently (bi-luṭf); ٱهْدِنَا 1:6:1 B002 the heading and set direction of travel (hady as jiha, sīra, ṭarīqa); ٱلصِّرَٰطَ 1:6:2 B001 the road itself; ٱلصِّرَٰطَ 1:6:2 B002 the road that takes its walker in (yastariṭu sālikahu), audible through the canonical sirāṭ reading; ٱلصِّرَٰطَ 1:6:2 B002 swallowing: the walker passes into the road with ease; ٱلْمُسْتَقِيمَ 1:6:3 B008 the road's straightness and evenness; صِرَٰطَ 1:7:1 B001 the road named after the people who walked it; ٱلضَّآلِّينَ 1:7:9 B001 the wanderer who leaves the course and loses the way; ٱلضَّآلِّينَ 1:7:9 B002 the one who goes missing, absorbed into the waste. Perceptible: It makes the path spatial and historical. The road already exists and has been walked: the verb of worship, naʿbudu, shares its root with the road made smooth by feet (muʿabbad). In 1:7 the road is identified by the people who walked it ('the road of those…'), not by a description. The sirāṭ reading hears a road that takes its walker in. Ḍalla also means to vanish into something. So the surah shows two ways of disappearing: into the road, carried along, or into the waste, lost.
- completes: I7 Gift gently sent, favor received, praise returned — A giver gently sends gifts to someone they hold dear and puts the recipient in a good, easy state. The recipient answers with praise and thanks.. Members: ٱلْحَمْدُ 1:2:1 B001 praise and thanks answering a favor; رَبِّ 1:2:3 B016 rubā: favor and kindness (minor); ٱهْدِنَا 1:6:1 B004 the hadiyya: a gentle gift sent to someone held in affection; ٱهْدِنَا 1:6:1 B001 guidance given gently (bi-luṭf); أَنْعَمْتَ 1:7:3 B001 the favor bestowed: good state and good life (niʿma); أَنْعَمْتَ 1:7:3 B002 softness and ease of life (minor). Perceptible: A Turkish reader already has hidayet and hediye without knowing they are one root. Heard together, guidance becomes something sent gently to someone loved. The surah opens with the thanks (ḥamd) and closes by naming the favor (anʿamta), so praise comes first and the favor is named only at the end.
- completes: I2 The branded herd, its owner, its lead animal and the stray — A herd of camels carries its owner's brand. It goes out from and returns to its owner's resting-place, following a lead animal at the front. One beast has strayed. It is left in a wasteland, and no one can tell who its owner is.. Members: بِسْمِ 1:1:1 B001 the brand (wasm, sima) by which an animal is known as someone's; documented alternative derivation of ism; رَبِّ 1:2:3 B001 the owner: rabb al-dābba, master of the beast; رَبِّ 1:2:3 B007 marabb al-ibil: the place where the camels stay; مَٰلِكِ 1:4:1 B008 the animal that goes in front and the rest follow (minor); ٱهْدِنَا 1:6:1 B003 the hādī: the front of the herd, the lead animal; أَنْعَمْتَ 1:7:3 B005 the herd itself (naʿam, camels), heard beside ḍāllīn (minor); ٱلضَّآلِّينَ 1:7:9 B005 the ḍālla: a beast left in a wasteland 'whose owner (rabb) is not known'; ٱلضَّآلِّينَ 1:7:9 B003 the thing gone from its owner, whose place cannot be found. Perceptible: The dictionary defines the ḍālla as the beast 'whose rabb is not known'. The word the surah uses for God in 1:2 is built into the definition of what it asks to be kept from in 1:7. So straying is relational, not only a wrong turn: it is losing one's tie to an owner who knows you. The surah is framed between the mark of belonging (bismi heard through wasm) and the unmarked stray.
- note: The road is named by those who walked it and were favored, and the niʿma finally answers the ḥamd of 1:2. Ḍāllīn is the one who wanders off and vanishes into the waste, the stray beast 'whose rabb is not known', which closes the arc begun by the mark of 1:1.

Opened by earlier ayat:
- 1:1 opened I2 The branded herd, its owner, its lead animal and the stray
- 1:1 opened I3 The womb and the one who raises stage by stage
- 1:2 opened I4 The master's household: owner, king and the owned one
- 1:2 opened I7 Gift gently sent, favor received, praise returned
- 1:4 opened I5 The day when what is owed is settled
- 1:5 opened I6 The weak walker held up between supporters
- 1:6 opened I1 The trodden, marked road that takes its walker in

Window movement: The surah moves from being named and marked (1:1, bismi, which can also be heard as wasm, the owner's brand) to an owner who raises (rabb) wrapped on both sides in womb-mercy (1:1–3). It then reaches the owner and king of a Day on which what is owed is settled (1:4). At 1:5 the owned ones stop speaking about the master and speak to him, declaring service and leaning on him for help. From that posture they ask to be led, held up and gifted onto a road already trodden smooth by the favored. That road takes its walker in (1:6–7). Their thanks were given at the start, and they ask not to become the stray beast in the waste whose owner no one knows. The surah's arc runs from the mark of belonging to the danger of being an unmarked stray, with praise answering a favor it only names at the end.

## Concordance for its lemmas

### صِرَٰط — ص ر ط — 45 uses in the Quran
use profile: {"root": "ص ر ط", "lemma": "صِرَٰط", "total": 45, "groups": [{"label": "A route described as a destination for guidance or invitation", "count": 24, "refs": ["1:6:2", "2:142:20", "2:213:48", "3:101:16", "4:68:2", "4:175:14", "5:16:17", "6:39:16", "6:87:8", "6:161:6", "10:25:10", "14:1:14", "16:121:6", "19:43:12", "22:24:8", "22:54:20", "23:73:4", "24:46:10", "34:6:14", "37:118:2", "38:22:23", "42:52:26", "48:2:14", "48:20:17"]}, {"label": "A route described as a course to follow, hold to, or be on", "count": 16, "refs": ["1:7:1", "3:51:7", "6:126:2", "6:153:3", "11:56:17", "15:41:3", "16:76:28", "19:36:7", "20:135:8", "36:4:2", "36:61:4", "42:53:1", "43:43:7", "43:61:9", "43:64:8", "67:22:11"]}, {"label": "A route someone says they will sit on to intercept others", "count": 1, "refs": ["7:16:6"]}, {"label": "Paths named as places where people are told not to sit and obstruct others", "count": 1, "refs": ["7:86:4"]}, {"label": "A route people are described as turning away from", "count": 1, "refs": ["23:74:7"]}, {"label": "A route raced along in a sight-related hypothetical", "count": 1, "refs": ["36:66:7"]}, {"label": "A route leading to al-Jaḥīm", "count": 1, "refs": ["37:23:6"]}], "dominant": "A route presented for guidance or invitation, or as a course to follow or be on, in 40 of 45 uses", "outside": [{"ref": "7:16:6", "how": "The speaker says he will sit on the route to intercept others."}, {"ref": "7:86:4", "how": "Paths are named as places where people are told not to sit and obstruct others."}, {"ref": "23:74:7", "how": "People are described as turning away from the route."}, {"ref": "36:66:7", "how": "The route is raced along in a hypothetical about sight."}, {"ref": "37:23:6", "how": "The route leads to al-Jaḥīm."}], "collocates": ["ٱلْمُسْتَقِيم — straight", "هَدَى — guide (various forms)", "ٱللَّه — God", "رَبّ — Lord", "ٱتَّبَعَ — follow (various forms)", "ٱلْحَمِيد — praiseworthy", "سَوِيّ — even", "سَبِيل — way"]}
every use: data/kwic/صرط_صرط_b935a3.md

### أَنْعَمَ — ن ع م — 17 uses in the Quran
- 1:7:3 صِرَٰطَ ٱلَّذِينَ ⟦أَنْعَمْتَ⟧ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ …
- 2:40:6 … ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ ⟦أَنْعَمْتُ⟧ عَلَيْكُمْ وَأَوْفُوا۟ بِعَهْدِىٓ …
- 2:47:6 … ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ ⟦أَنْعَمْتُ⟧ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ …
- 2:122:6 … ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ ⟦أَنْعَمْتُ⟧ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ …
- 4:69:8 … فَأُو۟لَٰٓئِكَ مَعَ ٱلَّذِينَ ⟦أَنْعَمَ⟧ ٱللَّهُ عَلَيْهِم مِّنَ …
- 4:72:10 … مُّصِيبَةٌۭ قَالَ قَدْ ⟦أَنْعَمَ⟧ ٱللَّهُ عَلَىَّ إِذْ …
- 5:23:6 … مِنَ ٱلَّذِينَ يَخَافُونَ ⟦أَنْعَمَ⟧ ٱللَّهُ عَلَيْهِمَا ٱدْخُلُوا۟ …
- 8:53:8 … يَكُ مُغَيِّرًۭا نِّعْمَةً ⟦أَنْعَمَهَا⟧ عَلَىٰ قَوْمٍ حَتَّىٰ …
- 17:83:2 وَإِذَآ ⟦أَنْعَمْنَا⟧ عَلَى ٱلْإِنسَٰنِ أَعْرَضَ …
- 19:58:3 أُو۟لَٰٓئِكَ ٱلَّذِينَ ⟦أَنْعَمَ⟧ ٱللَّهُ عَلَيْهِم مِّنَ …
- 27:19:12 … أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ ⟦أَنْعَمْتَ⟧ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ …
- 28:17:4 قَالَ رَبِّ بِمَآ ⟦أَنْعَمْتَ⟧ عَلَىَّ فَلَنْ أَكُونَ …
- 33:37:4 وَإِذْ تَقُولُ لِلَّذِىٓ ⟦أَنْعَمَ⟧ ٱللَّهُ عَلَيْهِ وَأَنْعَمْتَ …
- 33:37:7 … أَنْعَمَ ٱللَّهُ عَلَيْهِ ⟦وَأَنْعَمْتَ⟧ عَلَيْهِ أَمْسِكْ عَلَيْكَ …
- 41:51:2 وَإِذَآ ⟦أَنْعَمْنَا⟧ عَلَى ٱلْإِنسَٰنِ أَعْرَضَ …
- 43:59:5 … هُوَ إِلَّا عَبْدٌ ⟦أَنْعَمْنَا⟧ عَلَيْهِ وَجَعَلْنَٰهُ مَثَلًۭا …
- 46:15:28 … أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ ⟦أَنْعَمْتَ⟧ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ …

### غَيْر — غ ي ر — 147 uses in the Quran
use profile: {"root": "غ ي ر", "lemma": "غَيْر", "total": 147, "groups": [{"label": "Identifies an alternative entity, item, or group", "count": 52, "refs": ["1:7", "2:59", "2:173", "2:230", "3:83", "4:56", "6:14", "7:59", "10:15", "14:48"]}, {"label": "Marks an action or circumstance as lacking a stated basis, right, knowledge, measure, or authority", "count": 44, "refs": ["2:61", "2:212", "3:154", "5:32", "6:100", "13:2", "22:8", "28:50", "40:35", "48:25"]}, {"label": "Restricts a person, agent, or action by excluding a stated condition or conduct", "count": 20, "refs": ["2:173", "2:240", "4:12", "4:24", "4:25", "4:46", "5:1", "5:3", "5:5", "6:145", "9:2", "9:3", "16:115", "22:31", "23:6", "24:31", "24:60", "33:53", "56:86", "70:30"]}, {"label": "Describes or contrasts a feature, state, or extent", "count": 31, "refs": ["6:99", "6:141", "6:141", "11:46", "11:63", "11:65", "11:76", "11:101", "11:108", "11:109", "13:4", "14:37", "16:21", "20:22", "22:5", "24:29", "27:12", "27:22", "28:32", "30:55", "39:28", "41:8", "43:18", "47:15", "50:31", "52:35", "68:3", "70:28", "74:10", "84:25", "95:6"]}], "dominant": "Identifies an alternative entity, item, or group: 52 of 147 uses", "outside": [{"ref": "2:61", "how": "Qualifies killing the prophets as without right."}, {"ref": "2:212", "how": "Marks provision as given without reckoning."}, {"ref": "4:12", "how": "Qualifies a bequest as not causing harm."}, {"ref": "5:32", "how": "Qualifies killing as without another life taken or corruption."}, {"ref": "6:99", "how": "Contrasts produce as similar and unlike."}, {"ref": "6:100", "how": "Qualifies an attribution as made without knowledge."}, {"ref": "9:2", "how": "Describes the addressees as not beyond God's reach."}, {"ref": "11:46", "how": "Classifies a deed as not righteous."}, {"ref": "13:2", "how": "Describes the heavens as raised without pillars."}, {"ref": "14:37", "how": "Describes a valley as lacking cultivation."}, {"ref": "16:21", "how": "Contrasts the dead with the living."}, {"ref": "18:74", "how": "Qualifies a killing as without a life taken in return."}, {"ref": "20:22", "how": "Describes a hand as emerging without defect."}, {"ref": "22:8", "how": "Qualifies argument as without knowledge, guidance, or scripture."}, {"ref": "22:31", "how": "Describes people as not associating partners."}, {"ref": "24:60", "how": "Describes women as not displaying adornment."}, {"ref": "30:55", "how": "Qualifies the reported duration as just an hour."}, {"ref": "33:53", "how": "Describes guests as not waiting for the food to be ready."}, {"ref": "40:35", "how": "Describes debate about the signs as lacking authority."}, {"ref": "47:15", "how": "Describes water as not stale."}], "collocates": ["ٱللَّه — Allah", "ٱلْحَقّ — right, truth", "عِلْم — knowledge", "حِسَاب — reckoning", "إِلَٰه — deity", "ٱلَّذِي — that, which", "بَاغٍ — transgressing, seeking beyond limits", "مُسَٰفِحِينَ / مُسَٰفِحَٰت — sexually promiscuous"]}
every use: data/kwic/غير_غير_521ad2.md

### مَغْضُوب — غ ض ب — 1 uses in the Quran
- 1:7:6 … أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ⟦ٱلْمَغْضُوبِ⟧ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

### ضَآلّ — ض ل ل — 14 uses in the Quran
- 1:7:9 … ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ⟦ٱلضَّآلِّينَ⟧
- 2:198:26 … مِّن قَبْلِهِۦ لَمِنَ ⟦ٱلضَّآلِّينَ⟧
- 3:90:14 … تَوْبَتُهُمْ وَأُو۟لَٰٓئِكَ هُمُ ⟦ٱلضَّآلُّونَ⟧
- 6:77:18 … لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ⟦ٱلضَّآلِّينَ⟧
- 15:56:8 … رَّحْمَةِ رَبِّهِۦٓ إِلَّا ⟦ٱلضَّآلُّونَ⟧
- 23:106:8 … شِقْوَتُنَا وَكُنَّا قَوْمًۭا ⟦ضَآلِّينَ⟧
- 26:20:6 … إِذًۭا وَأَنَا۠ مِنَ ⟦ٱلضَّآلِّينَ⟧
- 26:86:6 … إِنَّهُۥ كَانَ مِنَ ⟦ٱلضَّآلِّينَ⟧
- 37:69:4 إِنَّهُمْ أَلْفَوْا۟ ءَابَآءَهُمْ ⟦ضَآلِّينَ⟧
- 56:51:4 ثُمَّ إِنَّكُمْ أَيُّهَا ⟦ٱلضَّآلُّونَ⟧ ٱلْمُكَذِّبُونَ
- 56:92:6 … كَانَ مِنَ ٱلْمُكَذِّبِينَ ⟦ٱلضَّآلِّينَ⟧
- 68:26:5 … رَأَوْهَا قَالُوٓا۟ إِنَّا ⟦لَضَآلُّونَ⟧
- 83:32:6 … قَالُوٓا۟ إِنَّ هَٰٓؤُلَآءِ ⟦لَضَآلُّونَ⟧
- 93:7:2 وَوَجَدَكَ ⟦ضَآلًّۭا⟧ فَهَدَىٰ

## Variant readings

1:7:1 صِرَٰطَ → سِرَاطَ (sirāṭa; ibdāl; mutawatir) ṣād→sīn substitution; same surface meaning but phonetically closer to sabīl cognate
1:7:1 صِرَٰطَ → صِؗرَاطَ (ṣᶻirāṭa; ibdāl; mutawatir) ishmām (ṣ with z-color); transitional articulation between ṣ and s
1:7:4 عَلَيْهِمْ → عَلَيْهِمُۥ (ʿalayhimū; vhr|madd; mutawatir) lengthened pronoun vowel (silat al-mīm); phonetic variant
1:7:4 عَلَيْهِمْ → عَلَيْهُمْ (ʿalayhum; vhr; mutawatir) short ḍamma pronoun vowel instead of kasra
1:7:7 عَلَيْهِمْ → عَلَيْهُمْ (ʿalayhum; vhr; mutawatir) ḍamma pronoun-vowel variant; canonical

## Turkish loanword cards

- صِرَٰط (ص ر ط) → sırat: today İslamî inanışta ahirette cehennem üzerindeki köprü / Doğru yol; özellikle sırat-ı müstakim sözünde. Reader hears: Bağlama göre ahiret köprüsü veya doğru yol. Drift: Türkçede en belirgin çağrışımı ahiretteki köprüdür; düz veya doğru yol anlamı daha çok dinî kalıplarda yaşar. Arabic keeps: B001 Arapçada sırat özellikle düz yol olmak üzere genel olarak yol anlamına gelir.; B002 Kök açıklamasında yiyeceği yutma anlamı da bulunur.; B003 Arapçada sırat sözcüğü kesip ilerleyen kılıç için de kullanılmıştır. False friend: Türkçede sırat çoğu kez ahiret köprüsünü düşündürür; Arapçada temel anlamı yoldur.
- أَنْعَمَ (ن ع م) → nimet: today İyilik, lütuf veya bağış / Yiyecek, geçim imkânı veya sahip olunan değerli şey. Reader hears: Lütuf, nimet veya iyi bir imkân. Drift: Türkçede hem lütuf ve iyilik hem de kişinin sahip olduğu güzel şeyler için kullanılır; gündelik konuşmada yiyecek için de söylenebilir. Arabic keeps: B001 Arapçada nimet; iyi hal, rahat yaşam ve başkasına ulaştırılan iyilik anlamlarını kapsar.; B002 Arapça kök ailesi yumuşaklık ve rahat yaşam anlamlarını da içerir.
- أَنْعَمَ (ن ع م) → en'am: today Otlayan evcil hayvanlar; özellikle dinî metinlerde davar ve büyükbaş hayvanlar / En'âm suresinin adında geçen sözcük. Reader hears: Otlayan evcil hayvanlar veya sure adı. Drift: Türkçede çoğunlukla Kur’an dili ve En'âm suresi adıyla karşılaşılır; günlük dilde hayvan topluluğu anlamında yaygın değildir. Arabic keeps: B005 Arapçada enʿām başta develer olmak üzere otlayan evcil hayvanları kapsar.
- غَيْر (غ ي ر) → gayri: today Başka, dışında; birleşiklerde olumsuzluk veya dışta bırakma bildiren unsur / Bazı kullanımlarda artık, bundan böyle. Reader hears: Başka, dışında veya birleşiklerde olumsuzluk. Drift: Türkçede en çok birleşiklerde 'olmayan' anlamı verir; kimi konuşma ve kalıplaşmış kullanımlarda 'artık' anlamına da gelir. Arabic keeps: B005 Arapçada gayr, başka olmayı ve istisnayı daha geniş biçimde ifade eder.; B003 Arapça kök değiştirme ve başka bir şeyle değiştirme anlamlarını da kapsar.; B004 Arapçada eşe veya aileye yönelik kıskançlık anlamı da vardır.
- غَيْر (غ ي ر) → gayret: today Çaba, emek ve çalışma azmi / Bir işi başarmak için gösterilen istek. Reader hears: Çaba veya azim. Drift: Türkçede çaba ve azim anlamına yerleşmiştir; Arapçadaki koruyucu kıskançlık anlamı güncel kullanımda belirgin değildir. Arabic keeps: B004 Arapça kök ailesinde eşini veya ailesini kıskanarak koruma duygusu da bulunur. False friend: Türkçede gayret 'çaba' demektir; Arapçadaki kıskançlık anlamı yaygın Türkçe kullanımda yoktur.
- مَغْضُوب (غ ض ب) → gazap: today Şiddetli öfke / Dinî kullanımda ilahî öfke veya ceza. Reader hears: Şiddetli öfke veya Allah’ın gazabı. Drift: Türkçede güçlü, çoğunlukla resmî ya da dinî tonda bir öfkeyi anlatır. Arapçada öfkenin yanı sıra öç alma yönelimi de vurgulanabilir. Arabic keeps: B001 Arapça kök, öfkenin yanı sıra intikam yönelimi ve razı olmamanın karşıtlığını da içerir.; B002 Arapçada biri için veya biri uğruna öfkelenmek ayrı kullanımlarla ifade edilir.; B003 Kök, karşı koyup muhalefet etme anlamını da taşır.
- ضَآلّ (ض ل ل) → dalalet: today Doğru yoldan sapma veya sapkınlık / Yanılgı ya da yanlış inanç. Reader hears: Özellikle dinî anlamda doğru yoldan sapma. Drift: Türkçede daha çok dinî sapma ve doğru yoldan ayrılma anlamında kullanılır; Arapça kök kaybolma, yitirme ve unutmayı da kapsar. Arabic keeps: B002 Arapçada bir şeyin gizlenip gözden kaybolması da kökün anlamlarındandır.; B003 Bir şeyi yitirme veya yerini bulamama anlamları vardır.; B004 Arapçada unutma ve bellekte tutamama da bu köktendir.; B005 Sahibi bilinmeyen kayıp hayvan için de kullanılır. False friend: Delalet 'gösterme, işaret etme' demektir ve dalaletle aynı sözcük değildir.

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
