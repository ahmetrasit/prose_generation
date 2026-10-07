Surah: 103. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (103:1 to 103:3), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/r13/surah_images.md =====
Write the Turkish commentary on the images of this surah for a curious reader
who knows neither Arabic nor how lexical families work, and who already has the
plain meaning. The map is an earlier reader's proposal: its chains, members,
passages and interactions are your material, not your verdicts. Correct a
member that does not hold, merge chains that are one image, and add what the
map missed from your own knowledge of Arabic and the Quran.

For each image:

- Show the scene through its operation: what the objects are, how they work,
  what the act does. Never flatten a mechanism into a label.
- Say what it makes perceptible in the surah that a plain paraphrase could not.
- Go through the surah in order and show what each ayah's words add to it.
- Bring in the Quran passages that stage it, with the speaker, the situation
  as the Quran itself tells it there and in the neighbouring ayat, and the
  wording the connection needs.

Then show where the images meet: a scene that holds two of them, and how
together they carry the surah's movement.

Develop every chain of the map, unless its members fail; a chain you leave out
goes in the ledger with its reason. A family image is heard beside the word's
meaning in its ayah, never in place of it; say so once. Keep root identity,
family images and your own connections distinct; an echo root does not
establish identity. Never invent a sense, source, citation or chronology. Use
no hadith, no exegetes' views and no report from outside the Quran (no occasion
of revelation, no name the Quran does not give, no date): the Quran, the map's
dictionary phrases and Arabic usage carry the commentary. Name
no dictionary or lexicographer in the prose, never mention the dictionary
("sözlük"), the map, its chains or your own process, and do not hedge in the
first person.

Write continuous prose: one `##` section per image, then a `## Buluşmalar`
section for the meetings; explain, do not dramatize; no lists and no closing
recap. Every Arabic quotation goes in the reader tag, and every tag ends with
its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the map's dictionary phrases:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Outside the `Kaynaklar:` lines, never write a Quran reference
outside a tag; quote the surah's own words in tags too, and name its ayat in
words ("dördüncü ayet"). End each image section with one line, `Kaynaklar:`, giving its
members as ayah, word, root and branch (e.g. 1:6 ٱلْمُسْتَقِيمَ ق و م B012).

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- not developed: <chain> - <why>
- memory: <a claim about Arabic that neither the map nor the Quran text can check>

===== _commentary/v16/work/s103/surah.r2/text.md =====
# Surah 103

- 103:1 وَٱلْعَصْرِ
- 103:2 إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ
- 103:3 إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ


===== _commentary/v16/out/s103/surah.map3.nohft.tool/map.md (without ## Not carried) =====
# Surah 103: map of image chains

Surah words: 103:1 وَٱلْعَصْرِ · 103:2 ٱلْإِنسَٰنَ، خُسْرٍ · 103:3 ءَامَنُوا۟، وَعَمِلُوا۟، ٱلصَّٰلِحَٰتِ، وَتَوَاصَوْا۟ (twice)، بِٱلْحَقِّ، بِٱلصَّبْرِ.

In the member lines below, every Arabic phrase in «» is quoted from dictionary.md, followed by its source tag. Quran passages are quoted from the text tool unless marked (recalled). Material that comes from memory and not from the dictionary or the text is marked (from memory).

## Chains

### 1. The trader's capital and the scale

A merchant puts up capital in a deal. The deal either brings a profit or eats into the principal, and goods are measured or weighed out to the buyer. The surah opens with a time-word whose first sense is "the age, a stretch of time" (العصر الدهر). It then puts the human being *in* khusr, and khusr's own branches say what kind of loss that is: losing from the principal, a deal that brings no profit, a scale left short. In 103:3 the exception is made of things a buyer can count: faith, deeds that are sound, and a right (ḥaqq, also "one's due share") passed between the parties. Time is the stock being spent, and each human is a trader losing it, except for those whose dealing yields a return.

- 103:1 وَٱلْعَصْرِ — ع ص ر B001 — «العصر الدهر» (ayn;sihah;tahdhib) — the span of time: the stock that runs down while the deal is open.
- 103:1 وَٱلْعَصْرِ — ع ص ر B007 — «المعتصر الذي يصيب من الشيء ويأخذ منه» (sihah); «العصارة الغلة» (tahdhib) — the one who draws gain out of a thing; yield or revenue. This is the return a deal should bring.
- 103:1 وَٱلْعَصْرِ — ع ص ر B006 — «اعتصرت ماله إذا استخرجته من يده» (sihah) — property drawn out of someone's hand. This is the loss seen from the other side.
- 103:2 خُسْرٍ — خ س ر B002 — «الخاسر الذي وضع في تجارته» (ayn;tahdhib); «خسر التاجر إذا وضع من رأس ماله» (jamhara); «صفقة خاسرة أي غير مربحة» (ayn;tahdhib); «انتقاص رأس المال» (mufradat) — the merchant who loses from his principal; a deal with no profit.
- 103:2 خُسْرٍ — خ س ر B003 — «خسرت الميزان وأخسرته إذا نقصته» (maqayis); «كلته ووزنته فأخسرته أي نقصته» (ayn;tahdhib); «ولا تخسروا الميزان» (mufradat) — the scale or measure left short.
- 103:2 خُسْرٍ — خ س ر B001 — «الخسر النقصان والخسران كذلك» (ayn;tahdhib) — plain decrease: the stock gets smaller.
- 103:2 خُسْرٍ — خ س ر B004 — «المقتنيات النفسية كالصحة والسلامة والعقل والإيمان والثواب» (mufradat) — the goods that can be lost include inner possessions: health, soundness of mind, faith, reward. The dictionary phrase itself names الإيمان as stock that can be lost, which links it to ءَامَنُوا۟ in 103:3.
- 103:3 وَعَمِلُوا۟ — ع م ل B005 — «عاملت الرجل أعامله معاملة في المبايعة وغيرها» (tahdhib) — dealing with a counterpart in buying and selling.
- 103:3 ءَامَنُوا۟ — ء م ن B001 — «الأمانة ضد الخيانة ومعناها سكون القلب» (maqayis) — the trustworthiness that a deal depends on.
- 103:3 بِٱلْحَقِّ — ح ق ق B003 — «الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي» (sihah;tahdhib) — the due share owed to its owner, the thing the partners hand to each other.
- 103:3 بِٱلصَّبْرِ — ص ب ر B011 — «اشتريت الشيء صبرة أي بلا وزن ولا كيل» (sihah) — buying in a heap, without weighing or measuring. It stands opposite the short scale of خُسْرٍ: here the goods change hands unmeasured.

Quran:
- 2:16 — God, of those who bought error for guidance: فَمَا رَبِحَت تِّجَٰرَتُهُمْ — the trade that brought no profit.
- 2:175 — the same people: ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ … فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ — the bad bargain ends in the reversed ṣabr (see chain 5).
- 35:29 — God, of those who recite, pray and spend: يَرْجُونَ تِجَٰرَةًۭ لَّن تَبُورَ.
- 61:10–11 — God to the believers: تِجَٰرَةٍۢ تُنجِيكُم … تُؤْمِنُونَ بِٱللَّهِ — a trade whose goods are faith and striving.
- 9:111 — God: ٱشْتَرَىٰ مِنَ ٱلْمُؤْمِنِينَ أَنفُسَهُمْ … وَعْدًا عَلَيْهِ حَقًّۭا … فَٱسْتَبْشِرُوا۟ بِبَيْعِكُمُ — the believers as sellers, with a due (ḥaqq) promise.
- 39:15 — the Prophet is told to say: إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ — the principal lost is the self.
- 83:1–3 — God, of the short-measurers: وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ (83:3).
- 55:9 — God, on the balance set up with the heavens: وَلَا تُخْسِرُوا۟ ٱلْمِيزَانَ.
- 104:2–3 — the next surah, of the hoarder: جَمَعَ مَالًۭا وَعَدَّدَهُۥ يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ — he takes his capital for something that outlasts time.
- (from memory) Fakhr al-Dīn al-Rāzī reports a man who said he understood this surah from an ice-seller calling out, "have mercy on one whose capital is melting." The image is time as melting capital.

### 2. The working day and its wage

A labourer is hired for the day and works with his hands, digging and building. At the late part of the day the work stops and the wage falls due. The first word of the surah names the afternoon and its prayer, the end of the working day. ʿamal names both the deed and the hired work with its pay, and ḥaqq names what has become binding, the earned due. The exception in 103:3 is the crew whose work was sound. Everyone else ends the day with a deal that earned nothing.

- 103:1 وَٱلْعَصْرِ — ع ص ر B001 — «العصر العشي» (ayn;tahdhib); «صلاة العصر» (sihah;tahdhib;maqayis); «جاءني فلان عصرا أي بطيئا» (sihah) — the late afternoon, its prayer, and coming late: the day is almost over.
- 103:2 خُسْرٍ — خ س ر B002 — «صفقة خاسرة أي غير مربحة» (ayn;tahdhib) — the day's work brought in nothing.
- 103:3 وَعَمِلُوا۟ — ع م ل B001 — «أصل واحد صحيح وهو عام في كل فعل يفعل» (maqayis); «كل فعل يكون من الحيوان بقصد» (mufradat) — work done on purpose.
- 103:3 وَعَمِلُوا۟ — ع م ل B006 — «العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه» (maqayis) — the crew of hand-workers who dig and line wells.
- 103:3 وَعَمِلُوا۟ — ع م ل B004 — «العمالة أجر ما عمل» (maqayis); «العمالة رزق العامل» (tahdhib) — the worker's wage.
- 103:3 وَعَمِلُوا۟ — ع م ل B003 — «العاملين عليها هم السعاة الذين يأخذون الصدقات» (tahdhib) — the appointed collectors: work given as an office.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B001 — «الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال» (mufradat) — soundness is said mostly of deeds, so this is the quality of the work.
- 103:3 بِٱلْحَقِّ — ح ق ق B002 — «حق الشيء وجب» (maqayis;sihah;tahdhib); «أحققت الشيء أي أوجبته واستحققته أي استوجبته» (sihah) — the wage becomes due and is earned.
- 103:3 بِٱلصَّبْرِ — ص ب ر B003 — «الصبير هو الكفيل» (maqayis;sihah) — the guarantor who stands behind what is owed.

Quran:
- 95:4–6 — God's oath-surah in the same shape: the human created in the best stature, returned to the lowest, إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ — the same exception, with the wage named.
- 84:6 — God addressing the human: إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ — the labourer meeting the one he worked for.
- 18:103–104 — the Prophet is told to say: بِٱلْأَخْسَرِينَ أَعْمَٰلًا ٱلَّذِينَ ضَلَّ سَعْيُهُمْ — khusr said of works themselves.
- (from memory) A hadith in Bukhārī tells of labourers hired for one day. Earlier communities worked until midday and until ʿaṣr. The last group worked from ʿaṣr to sunset and was paid double. It joins ʿaṣr, hired work and wage in one scene.

### 3. Night joined to day: the turning of time

Time here is made of joined parts: night joined to day, morning to evening (the two ʿaṣrs), the heart of winter, the spring that fattens the herd, the yearly time a camel is mated. The time-word and the joining-word of the surah meet in the dictionary. al-ʿaṣrān are "night and day", and waṣṣā is "to join the night to the day". A human life has the same structure: a girl "reaches the ʿaṣr of her youth", and the late afternoon is the late part of a life.

- 103:1 وَٱلْعَصْرِ — ع ص ر B001 — «العصران الليل والنهار» (ayn;sihah;tahdhib;maqayis); «العصران الغداة والعشي» (sihah;tahdhib;maqayis); «العصر الدهر» (ayn;sihah;tahdhib); «العصار الحين» (tahdhib); «نام وما نام لعصر» (tahdhib) — the pairs of times that make up the day, the long age, a while, and the short span of a broken sleep.
- 103:1 وَٱلْعَصْرِ — ع ص ر B009 — «بلغت عصر شبابها وإدراكها» (tahdhib) — ʿaṣr as a stage of life that someone reaches.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B001 — «وصيت الليلة باليوم وصلتها» (maqayis); «أصل يدل على وصل شيء بشيء» (maqayis) — joining night to day: the act of the surah's verb, done to time.
- 103:3 بِٱلْحَقِّ — ح ق ق B011 — «سقط على حاق رأسه وجئته في حاق الشتاء» (sihah) — the very middle of winter.
- 103:3 بِٱلْحَقِّ — ح ق ق B008 — «أتت الناقة على حقها أي الوقت الذي ضربت فيه» (sihah;tahdhib;mufradat) — a year's turn marked by the camel's mating time.
- 103:3 بِٱلْحَقِّ — ح ق ق B013 — «أحقت الناقة من الربيع أي سمنت» (maqayis) — spring, the season that fattens.
- 103:3 بِٱلصَّبْرِ — ص ب ر B007 — «صبارة الشتاء شدة برده» (sihah) — the bitter cold of winter.
- 103:3 بِٱلصَّبْرِ — ص ب ر B014 — «يعبر عن الانتظار بالصبر لما كان حق الانتظار أن لا ينفك عن الصبر» (mufradat) — waiting through time. This dictionary phrase joins ṣabr and ḥaqq.

Quran:
- 18:28 — God to the Prophet: وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ — ṣabr laid along «العصران الغداة والعشي».
- 40:55 — God to the Prophet: فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ … وَسَبِّحْ بِحَمْدِ رَبِّكَ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ — ṣabr, ḥaqq and the two ends of the day in one ayah.
- 20:130 — God to the Prophet: فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ … قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا … وَأَطْرَافَ ٱلنَّهَارِ — the time "before sunset" is the ʿaṣr.
- 45:24 — the deniers speak: وَمَا يُهْلِكُنَآ إِلَّا ٱلدَّهْرُ — they treat time (الدهر, the first gloss of العصر) as the thing that ruins them.
- 10:45 — God, of the gathering: كَأَن لَّمْ يَلْبَثُوٓا۟ إِلَّا سَاعَةًۭ مِّنَ ٱلنَّهَارِ … قَدْ خَسِرَ ٱلَّذِينَ كَذَّبُوا۟ — a life shrunk to one hour of a day, then khusr.
- 46:15 — God: وَوَصَّيْنَا ٱلْإِنسَٰنَ بِوَٰلِدَيْهِ … حَتَّىٰٓ إِذَا بَلَغَ أَشُدَّهُۥ وَبَلَغَ أَرْبَعِينَ سَنَةًۭ قَالَ … وَأَنْ أَعْمَلَ صَٰلِحًۭا … وَأَصْلِحْ لِى فِى ذُرِّيَّتِىٓ — a life's stages, with waṣṣā, insān, ʿamal and ṣāliḥ all in one ayah.
- 102:1–2 — God to the rivals in increase: حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ — time used up without noticing.
- 2:238 (recalled) حَافِظُوا عَلَى الصَّلَوَاتِ وَالصَّلَاةِ الْوُسْطَىٰ — (from memory) a hadith identifies the middle prayer as ṣalāt al-ʿaṣr.

### 4. The press: grapes, extract, bitter sap, stoppered vessel

Grapes or olives go into a sack or press and are squeezed until the liquid runs. What runs out is the ʿuṣāra, and the Arabs use it as a figure for good and giving. The surah opens with this pressing word and closes with a word that the dictionary defines as a pressing: ṣabr is «عصارة شجرة», the bitter sap pressed from a tree and taken as medicine. ṣabr also names the stopper of a flask and the sides of a vessel. In this scene ʿaṣr is the squeezing and ṣabr is the bitter extract kept sealed in its flask. The dictionary also places the human (إنسان) in it: a person choking on food who presses water down in small sips.

- 103:1 وَٱلْعَصْرِ — ع ص ر B002 — «ضغط شيء حتى يتحلب» (maqayis); «عصرت العنب وعصرته إذا وليت عصره بنفسك» (tahdhib); «يعصرون الأعناب والزيت» (tahdhib); «المعصار شيء كالمخلاة يجعل فيه العنب ويعصر» (maqayis); «العصارة ما تحلب من شيء تعصره» (tahdhib); «كل شيء عصر ماؤه فهو عصير» (tahdhib) — the squeezing, the sack, the running juice.
- 103:1 وَٱلْعَصْرِ — ع ص ر B007 — «العرب تجعل العصارة والمعتصر مثلا للخير والعطاء» (maqayis) — the pressed yield as a figure for good and giving.
- 103:1 وَٱلْعَصْرِ — ع ص ر B008 — «الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء وهو أن يشربه قليلا قليلا ليسيغه» (sihah); «لو بغير الماء حلقي شرق كنت كالغصان بالماء اعتصاري» (tahdhib) — the choking person freed by small sips. The phrase joins الإنسان and ʿ-ṣ-r. (from memory) The verse is attributed to ʿAdī ibn Zayd, said to have been composed in prison.
- 103:1 وَٱلْعَصْرِ — ع ص ر B014 — «المعصور اللسان اليابس عطشا» (tahdhib) — a tongue wrung dry by thirst.
- 103:2 ٱلْإِنسَٰنَ — ء ن س — present in the B008 phrase above as the one who chokes and sips.
- 103:2 خُسْرٍ — خ س ر B001 — «الخسر النقصان والخسران كذلك» (ayn;tahdhib) — the pressed mass is left reduced.
- 103:3 بِٱلصَّبْرِ — ص ب ر B008 — «الصبر بكسر الباء عصارة شجرة» (ayn;tahdhib); «الصبر هذا الدواء المر» (sihah) — the bitter pressed sap used as medicine. ṣabr is defined here by ʿuṣāra.
- 103:3 بِٱلصَّبْرِ — ص ب ر B018 — «الصبار صمام القارورة» (tahdhib); «أصبر سد رأس الحوجلة بالصبار وهو السداد» (tahdhib) — the stopper that seals the flask's neck.
- 103:3 بِٱلصَّبْرِ — ص ب ر B004 — «أصبار الإناء نواحيه» (maqayis;ayn;sihah) — the sides of the vessel that hold the liquid.

Quran:
- 12:36 — in Joseph's prison, a fellow inmate tells his dream: إِنِّىٓ أَرَىٰنِىٓ أَعْصِرُ خَمْرًۭا — pressing seen from inside confinement. 12:41 — Joseph's answer: فَيَسْقِى رَبَّهُۥ خَمْرًۭا.
- 12:47–49 — Joseph interprets the king's dream: seven years of sowing, seven hard years, then عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ (12:49) — the press as the sign of a relieved year. The dictionary's «يعصرون الأعناب والزيت» glosses this.
- (from memory) A proverbial line: الصبر مثل اسمه مر مذاقته لكن عواقبه أحلى من العسل — ṣabr as bitter as the sap it is named after.

### 5. Holding: the self held, the captive held, the hand that holds back

ʿaṣr and ṣabr are both defined by ḥabs, holding back: «العصر الحبس» and «الصبر حبس النفس عن الجزع». The scene has several forms of holding:
- a person holds their own self back from panic, from food (fasting), and in waiting;
- the reversal: a captive is held and set up to be killed, and a man is made to swear under compulsion;
- a closed hand holds back what it owes, and a father keeps his son's property from him;
- a girl is kept indoors at her first menses;
- the crop is held in its husk.

The surah ends on the self-holding form of ṣabr, and the dictionary puts الإنسان inside the reversed form: «الصبر نصب الإنسان للقتل». The furthest reversal is ṣabr as boldness, glossed as doing the deeds of the people of the Fire.

- 103:1 وَٱلْعَصْرِ — ع ص ر B006 — «العصر الحبس» (tahdhib); «ما عصرك أي ما منعك» (tahdhib); «يعتصر الوالد على ولده في ماله أي يمنعه إياه ويحبسه عنه» (sihah); «فلان عاصر إذا كان ممسكا» (tahdhib); «تعصر أي تعسر» (tahdhib) — holding back and withholding, the tight-fisted man.
- 103:1 وَٱلْعَصْرِ — ع ص ر B009 — «المعصر ساعة تطمث أي تحيض لأنها تحبس في البيت يجعل لها عصرا» (tahdhib) — a girl kept in the house. The phrase joins ʿaṣr and ḥabs.
- 103:1 وَٱلْعَصْرِ — ع ص ر B010 — «مأخوذ من العصر وهو الحرز أي تحرز في غلفه» (tahdhib) [fixed expression] — grain kept safe inside its husk.
- 103:2 ٱلْإِنسَٰنَ — ء ن س B001 — «الإنس البشر والواحد إنسي والجمع أناسي» (sihah) — the human held. It also stands inside the ṣabr B002 phrase below.
- 103:3 بِٱلصَّبْرِ — ص ب ر B001 — «الصبر حبس النفس عن الجزع» (sihah); «صبرت نفسي أي حبستها» (maqayis;tahdhib); «حبس النفس على ما يقتضيه العقل والشرع» (mufradat); «الصبر نقيض الجزع» (ayn;jamhara;tahdhib) — the self holding itself.
- 103:3 بِٱلصَّبْرِ — ص ب ر B002 — «المصبورة المحبوسة على الموت» (maqayis;sihah); «الصبر نصب الإنسان للقتل» (ayn;tahdhib); «صبرت يمينه أي حلفته» (ayn;maqayis;tahdhib); «قتل صبر ويمين صبر» (sihah;tahdhib); «الصبر الإكراه» (tahdhib) — held by another: the captive set up for death, the forced oath.
- 103:3 بِٱلصَّبْرِ — ص ب ر B012 — «أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود» (tahdhib); «فليصطبر معناه فليقتص» (tahdhib) — the held man killed in retaliation.
- 103:3 بِٱلصَّبْرِ — ص ب ر B014 — «فاصبر لحكم ربك أي انتظر حكمه» (mufradat) — holding still to wait for a judgment.
- 103:3 بِٱلصَّبْرِ — ص ب ر B015 — «سمي الصوم صبرا لكونه كالنوع له» (mufradat) — fasting as one kind of holding.
- 103:3 بِٱلصَّبْرِ — ص ب ر B013 — «الصبر الجرأة ومنه فما أصبرهم على النار» (tahdhib); «ما أعملهم بعمل أهل النار» (mufradat) — the reversal: ṣabr as daring. The mufradat gloss joins ṣabr with ʿamal (عمل).
- 103:3 بِٱلصَّبْرِ — ص ب ر B018 — «أصبر سد رأس الحوجلة بالصبار وهو السداد» (tahdhib) — sealing an opening.

Quran:
- 18:28 — God to the Prophet: وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم — holding the self in place beside a company. The verb is used in its physical sense.
- 2:175 — God, of those who conceal the Book and buy error: فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ — the reversal the dictionary cites.
- 68:48 — God to the Prophet: فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تَكُن كَصَاحِبِ ٱلْحُوتِ إِذْ نَادَىٰ وَهُوَ مَكْظُومٌۭ — holding still to wait for the judgment, set against one who was held in the fish.
- 5:106 — God to the believers on a bequest made away from home: تَحْبِسُونَهُمَا مِنۢ بَعْدِ ٱلصَّلَوٰةِ فَيُقْسِمَانِ بِٱللَّهِ — witnesses held and made to swear (see chain 11).
- 12:36 — Joseph's prison, where the pressing dream is told (see chain 4).
- 3:200 — God to the believers: ٱصْبِرُوا۟ وَصَابِرُوا۟ وَرَابِطُوا۟ — holding, out-holding, and staying tied at the post.

### 6. Refuge and deliverance

A threatened person takes hold of something and clings to it, takes refuge with someone, enters someone's protection, and reaches a house where they are safe. ʿaṣr names the refuge itself, and the proverbial «عصرة المنجود» is the refuge of the man in distress. amn is safety against fear, and the maʾman is the house of safety. Against this stand ruin (khusr as halāk) and a calamity that has no way out (umm ṣabūr). Lineage is described as a refuge too, and a guarantor stays with the group in its affairs. ḥaqīqa names what a man is bound to defend: banner, sanctuary, courtyard. The «معاصر» are mail coats one shelters in. In the surah, al-insān stands in ruin, and the excepted ones are the believers (āmanū), whose word is the word of safety.

- 103:1 وَٱلْعَصْرِ — ع ص ر B005 — «تعلق بشيء وامتساك به» (maqayis); «العصر الملجأ» (sihah;maqayis); «العصر المنجاة والعصرة والمعتصر والمعصر» (tahdhib); «اعتصرت بفلان وتعصرت أي التجأت إليه» (sihah); «اعتصر بالمكان إذا التجأ إليه» (maqayis); «عصرة المنجود» (sihah;tahdhib;maqayis) — clinging, refuge, escape.
- 103:1 وَٱلْعَصْرِ — ع ص ر B011 — «العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ» (maqayis) — one's origin as the refuge one turns back to.
- 103:1 وَٱلْعَصْرِ — ع ص ر B016 — «الصحيح من ذلك أن المعاصر الدروع مأخوذ من العصر لأنه يعصر بها» (maqayis) — mail coats one shelters in. Maqayis first records «المعاصر العمائم» and «قالوا هي ثياب سود», then rejects both in favour of «الدروع».
- 103:1 وَٱلْعَصْرِ — ع ص ر B010 — «عصر الزرع صار في أكمامه» (tahdhib) [fixed expression] — the grain sheltered in its husks.
- 103:2 خُسْرٍ — خ س ر B004 — «خسر إذا هلك» (tahdhib); «التخسير الإهلاك» (sihah); «الخسار والخسارة والخيسرى الضلال والهلاك» (sihah) — the ruin that the refuge saves from.
- 103:3 ءَامَنُوا۟ — ء م ن B001 — «الأمن ضد الخوف» (ayn;sihah); «أصل الأمن طمأنينة النفس وزوال الخوف» (mufradat); «الأمان إعطاء الأمنة» (maqayis;ayn); «استأمن إليه دخل في أمانه» (sihah); «مأمنه منزله الذي فيه أمنه» (mufradat) — entering protection; the house of safety.
- 103:3 بِٱلْحَقِّ — ح ق ق B007 — «الحقيقة ما يحق على الرجل أن يحميه» (sihah); «الحقيقة الراية والحرمة والفناء وما يلزمه الدفاع عنه» (tahdhib) — what has to be defended: banner, sanctuary, courtyard.
- 103:3 بِٱلصَّبْرِ — ص ب ر B003 — «صبير القوم الذي يصبر لهم ويكون معهم في أمورهم» (ayn); «صبرت بفلان إذا كفلت به فأنا به صبير» (tahdhib) — the one who stands surety and stays with the group.
- 103:3 بِٱلصَّبْرِ — ص ب ر B006 — «أم صبور أمر لا منفذ له عنه» (tahdhib); «أم صبار الحرب والداهية الشديدة» (ayn) — the calamity with no exit, the opposite of refuge.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B005 — «إن مكة تسمى صلاحا» (maqayis); «وصلاح مثل قطام اسم مكة» (sihah) — the name of the safe city.

Quran:
- 106:4 — God, of Quraysh, in the surah three after this one: ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ.
- 2:125 — God: وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا — the House as the place to return to for safety, in the city the dictionary also names صلاح.
- 3:103 — God to the believers: وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا … وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا — holding onto a rope together and being pulled back from the brink. The verb is from ع ص م, not ع ص ر. It stages the act of «تعلق بشيء وامتساك به».
- 12:49 — Joseph: فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ — rescue and ʿ-ṣ-r side by side. (from memory) Some early philologists (Abū ʿUbayda) glossed يعصرون as "they are saved", taking it from al-ʿuṣra, refuge.
- 61:10 — God: تِجَٰرَةٍۢ تُنجِيكُم مِّنْ عَذَابٍ أَلِيمٍۢ — a bargain that delivers.
- 29:41 — God, of those who take patrons other than Him: كَمَثَلِ ٱلْعَنكَبُوتِ ٱتَّخَذَتْ بَيْتًۭا ۖ وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ — the false refuge (see chain 13).

### 7. Rain-cloud, joined growth, fattened herd and the whirlwind

Clouds are "pressed" with rain and release it on a people. White cloud lies in layers above the dense cloud. Plants then join one another until the land is continuously green, the pasture gives itself to the grazing herd, the camels fatten in spring, the crop sets in its husks, and grain is heaped. The surah's own form تواصى is used in the dictionary for plants joining. The reversal is the iʿṣār, a whirlwind lifting dust like a column, and hard bare stone or gravel ground where nothing holds. Loss (khusr) is the garden that the whirlwind burns.

- 103:1 وَٱلْعَصْرِ — ع ص ر B003 — «المعصرات السحائب تعتصر بالمطر» (sihah); «السحابة المعصر التي تتحلب بالمطر» (tahdhib); «عصر القوم أي مطروا» (sihah); «أعصر القوم إذا أتاهم المطر» (maqayis); «قرئت وفيه يعصرون أي يأتيهم المطر» (maqayis) — the cloud pressed with rain; the people rained on.
- 103:1 وَٱلْعَصْرِ — ع ص ر B010 — «إذا تبينت أكمام السنبل قيل قد عصر الزرع» (tahdhib) [fixed expression] — the crop setting in its husks.
- 103:1 وَٱلْعَصْرِ — ع ص ر B007 — «العصارة الغلة» (tahdhib); «يعصرون قال يستغلون بأرضيهم» (maqayis) — the yield of the land.
- 103:1 وَٱلْعَصْرِ — ع ص ر B004 — «الإعصار ريح تهب تثير الغبار فيرتفع إلى السماء كأنه عمود» (sihah); «الإعصار الغبار الذي يسطع مستديرا والجمع الأعاصير» (maqayis) — the whirlwind: the destroying reversal.
- 103:2 خُسْرٍ — خ س ر B004 — «خسر إذا هلك» (tahdhib) — the destroyed harvest.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B001 — «تواصى النبت إذا اتصل» (jamhara;sihah); «أرض واصية متصلة النبات» (sihah;mufradat); «فلاة واصية يتصل بفلاة أخرى» (tahdhib) — plants joining to plants; land green without a break. The surah's verb form is used here of vegetation.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B004 — «إذا أطاع المرعى للسائمة فأصابته رغدا قيل وصى لها المرتع يصي وصيا» (ayn;tahdhib) — the pasture giving itself to the herd.
- 103:3 بِٱلْحَقِّ — ح ق ق B013 — «أحقت الناقة من الربيع أي سمنت» (maqayis); «أحق القوم إحقاقا إذا سمن مالهم واحتق المال إذا سمن وانتهى سمنه» (tahdhib) — the herd fattened to the full.
- 103:3 بِٱلصَّبْرِ — ص ب ر B010 — «السحاب الأبيض الذي يصبر بعضه فوق بعض درجا» (sihah;tahdhib); «الصبر سحاب مستو فوق السحاب الكثيف» (ayn) — white cloud built up in layers.
- 103:3 بِٱلصَّبْرِ — ص ب ر B011 — «الصبرة من الطعام بعضه فوق بعض» (ayn;tahdhib) — the harvest heap.
- 103:3 بِٱلصَّبْرِ — ص ب ر B005 — «الصبر الأرض التي فيها حصباء» (maqayis;sihah;tahdhib); «أم صبار الحرة أو الصفاة» (maqayis;sihah;tahdhib); «الصبرة من الحجارة ما اشتد وغلظ» (maqayis;ayn;tahdhib) — gravel ground and hard bare rock.

Quran:
- 78:14 — God, listing His gifts: وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا; 78:15–16 (recalled) لِنُخْرِجَ بِهِ حَبًّا وَنَبَاتًا وَجَنَّاتٍ أَلْفَافًا — rain, then joined, entwined gardens.
- 12:47–49 — Joseph's interpretation: grain left in the ear (فَذَرُوهُ فِى سُنۢبُلِهِۦٓ), hard years, then the year of rain and pressing.
- 2:264–266 — God's parables of spending, opening at 2:264: the showy spender is like صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا (bare stone); the sincere one is like a garden on a height, rained on, giving double (2:265); then 2:266: an old man with weak offspring whose garden of palms and vines فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ. This is the whole chain as the loss of a lifetime's yield at the end of life.
- 57:20 — God on the nearer life: كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا.
- 10:24 — God on the nearer life: rain mixes with the earth's plants until أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا.

### 8. The beast of burden and the road

A young camel reaches the age at which it can be loaded. The trusted she-camel does not tire or stumble. A she-camel is built for work. The rider mounts and milks from the animal's near side, the side named insī. The legs do the work. The rider treats the mount well, or drives it past its strength until it is spent and lean. Walkers go on foot along a worn road over gravel and mountain. Every word of 103:2–3 except khusr has a member in this scene: the human on the near side, the trusted mount, the working camel, the camel that has come of age to be loaded, the kindness done to the animal, and the mountain.

- 103:2 ٱلْإِنسَٰنَ — ء ن س B004 — «الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب» (tahdhib); «إنسي الدابة للجانب الذي يلي الراكب» (mufradat) — the side that faces the rider.
- 103:3 ءَامَنُوا۟ — ء م ن B001 — «الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها» (ayn;sihah;mufradat) — the trusted she-camel that does not flag or stumble.
- 103:3 وَعَمِلُوا۟ — ع م ل B008 — «اليعملة الناقة النجيبة المطبوعة على العمل» (sihah); «اليعملة من الإبل اسم لها اشتق من العمل» (maqayis) — the she-camel made for work.
- 103:3 وَعَمِلُوا۟ — ع م ل B010 — «عوامل الدابة قوائمه واحدها عاملة» (tahdhib) [fixed expression] — the legs as the working parts.
- 103:3 وَعَمِلُوا۟ — ع م ل B011 — «طريق معمل أي لحب مسلوك» (sihah) [fixed expression] — the worn road.
- 103:3 وَعَمِلُوا۟ — ع م ل B012 — «المسافرون إذا مشوا على أرجلهم يسمون بني العمل» (tahdhib) [fixed expression] — travellers on foot.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B001 — «أصلحت إلى الدابة أحسنت إليها» (ayn) — treating the mount well.
- 103:3 بِٱلْحَقِّ — ح ق ق B008 — «الحقة من أولاد الإبل ما استحق أن يحمل عليه» (maqayis); «الحق من الإبل ما استحق أن يحمل عليه والأنثى حقة» (mufradat) — the camel that has become fit to be loaded.
- 103:3 بِٱلْحَقِّ — ح ق ق B012 — «الحقحقة عند العرب أن يسار البعير ويحمل على ما يتعبه ولا يطيقه» (tahdhib); «الحقحقة أرفع السير وأتعبه للظهر» (maqayis;sihah) — over-driving: a load and pace beyond the animal's strength.
- 103:3 بِٱلْحَقِّ — ح ق ق B014 — «الأحق الذي يضع رجله في موضع يده» (tahdhib); «احتق الفرس أي ضمر» (sihah) — the horse whose hind foot falls in the track of its forefoot; the horse grown lean.
- 103:3 بِٱلصَّبْرِ — ص ب ر B005 — «الصبر الأرض التي فيها حصباء» (maqayis;sihah;tahdhib) — gravel ground under foot.
- 103:3 بِٱلصَّبْرِ — ص ب ر B017 — «الصبير الجبل» (tahdhib); «الصبير الأقدر وهو الوسط من الجبال» (tahdhib) — the mountain.

Quran:
- 33:72 — God: إِنَّا عَرَضْنَا ٱلْأَمَانَةَ عَلَى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلْجِبَالِ فَأَبَيْنَ أَن يَحْمِلْنَهَا … وَحَمَلَهَا ٱلْإِنسَٰنُ — the mountains refuse the load, and the human takes on the amāna.
- 16:7 — God, of livestock: وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ.
- 22:27 — God to Abraham: يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ — walkers and lean mounts; compare «احتق الفرس أي ضمر».
- 84:6 — the human as one who toils toward his Lord until he meets Him.
- (from memory) The saying of Muṭarrif: خير الأمور أوساطها وشر السير الحقحقة. The hadith: إن المنبت لا أرضا قطع ولا ظهرا أبقى — the rider who exhausts his mount neither arrives nor keeps his mount.

### 9. Seeing, assenting, making sure

Someone notices something, seeing a fire at a distance or hearing a sound, and looks into it. They then accept what they are told as true, and test it until they are certain. In the dictionary, insān names the small image of a person seen in the dark of the eye. īmān is taṣdīq, and ḥaqq is correspondence to what is so. The sequence is the human who perceives (insān / ānasa), then believes (āmanū), then holds what is verified (al-ḥaqq).

- 103:2 ٱلْإِنسَٰنَ — ء ن س B002 — «آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه» (tahdhib); «آنست الشيء إذا رأيته وآنسته إذا سمعته» (maqayis); «آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته» (sihah) — seeing fire, hearing a voice, noticing maturity.
- 103:2 ٱلْإِنسَٰنَ — ء ن س B005 — «إنسان العين المثال الذي يرى في السواد أي سواد العين» (sihah) — the small figure seen in the pupil.
- 103:3 ءَامَنُوا۟ — ء م ن B002 — «الإيمان التصديق» (ayn;sihah); «وما أنت بمؤمن لنا أي مصدق لنا» (maqayis;ayn;mufradat); «إذعان النفس للحق على سبيل التصديق» (mufradat) — accepting a report as true. The last phrase joins īmān with الحق.
- 103:3 وَعَمِلُوا۟ — ع م ل B002 — «أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه» (tahdhib) — putting the mind to work on it.
- 103:3 وَعَمِلُوا۟ — ع م ل B010 — «وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر» (tahdhib) [fixed expression] — the far-seeing eye as a working organ.
- 103:3 بِٱلْحَقِّ — ح ق ق B001 — «أصل الحق المطابقة والموافقة» (mufradat); «حققت الأمر وأحققته إذا تحققته وصرت منه على يقين» (sihah); «الحق نقيض الباطل» (maqayis;sihah;tahdhib) — matching what is so; becoming certain.
- 103:3 بِٱلْحَقِّ — ح ق ق B005 — «حققت قوله وظنه تحقيقا أي صدقت» (sihah); «حقق الرجل إذا قال هذا الشيء هو الحق» (tahdhib) — confirming a word as true.

Quran:
- 20:10 — Moses on the road with his family: إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى. Also 28:29 (recalled): ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًا.
- 4:6 — God to guardians of orphans: فَإِنْ ءَانَسْتُم مِّنْهُمْ رُشْدًۭا فَٱدْفَعُوٓا۟ إِلَيْهِمْ أَمْوَٰلَهُمْ — perceiving maturity, then handing over property (see chain 11).
- 12:17–18 — Joseph's brothers to Jacob: وَمَآ أَنتَ بِمُؤْمِنٍۢ لَّنَا وَلَوْ كُنَّا صَٰدِقِينَ. Jacob, seeing the false blood: بَلْ سَوَّلَتْ لَكُمْ أَنفُسُكُمْ أَمْرًۭا ۖ فَصَبْرٌۭ جَمِيلٌۭ — a report he will not accept, answered with ṣabr.

### 10. From quarrel to company

Two parties face each other, and each claims that the right is on its side (taḥāqqa). Reconciliation (ṣulḥ) takes away the shying-apart (nifār). Familiarity (uns) is the opposite of shying away and of desolation; the familiar dog is the opposite of the biting one. Then people join one another: the dictionary glosses تواصى القوم as «تواصلوا». In the surah, al-insān stands alone in loss, and in 103:3 the excepted ones turn toward one another in a reciprocal form. Each hands the other the ḥaqq instead of contesting it. ʿaṣr also names the bond of affection or kinship, and ṣabr the companion who stays with the group.

- 103:1 وَٱلْعَصْرِ — ع ص ر B005 — «ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة» (tahdhib) — the tie of affection or kinship (named by its absence).
- 103:2 ٱلْإِنسَٰنَ — ء ن س B003 — «الأنس خلاف النفور ولكل ما يؤنس به» (mufradat); «الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به» (sihah); «الأنس أنس الإنسان بالشيء إذا لم يستوحش منه» (maqayis); «كلب أنوس نقيض العقور» (tahdhib) — ease with another, against desolation and shying away.
- 103:2 ٱلْإِنسَٰنَ — ء ن س B006 — «فلان ابن إنس فلان أي صفيه وخاصته» (sihah) — the chosen intimate.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B002 — «الصلح يختص بإزالة النفار بين الناس، يقال اصطلحوا وتصالحوا» (mufradat); «والصلح تصالح القوم بينهم» (ayn) — reconciliation removes the nifār. The same nifār / nufūr appears in ء ن س B003.
- 103:3 بِٱلْحَقِّ — ح ق ق B004 — «حاقه أي خاصمه، والتحاق التخاصم والاحتقاق الاختصام» (sihah); «تحاق القوم واحتقوا إذا تخاصموا» (tahdhib); «حاققته فحققته أي خاصمته في الحق فغلبته» (mufradat) — the quarrel over who is right, the reversal of passing the ḥaqq to each other.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B003 — «تواصى القوم إذا تواصلوا» (jamhara); «تواصى القوم أي أوصى بعضهم بعضا» (sihah); «تواصى القوم إذا أوصى بعضهم إلى بعض» (mufradat) — joining one another; each counselling the other.
- 103:3 بِٱلصَّبْرِ — ص ب ر B003 — «صبير القوم الذي يصبر لهم ويكون معهم في أمورهم» (ayn) — the companion who stays with the group in its affairs.

Quran:
- 90:17 — God, in the surah of the steep road (opening at 90:11): ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ — the only other تواصوا of the believers.
- 51:53 — God, of the deniers across generations: أَتَوَاصَوْا۟ بِهِۦ ۚ بَلْ هُمْ قَوْمٌۭ طَاغُونَ — the same reciprocal counsel used in the wrong direction.
- 49:9–10 — God to the believers: two factions fight, فَأَصْلِحُوا۟ بَيْنَهُمَا … إِنَّمَا ٱلْمُؤْمِنُونَ إِخْوَةٌۭ فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ.
- 4:128 — God, on a wife who fears her husband's aversion: أَن يُصْلِحَا بَيْنَهُمَا صُلْحًۭا ۚ وَٱلصُّلْحُ خَيْرٌۭ.
- 41:34–35 — God to the Prophet: ٱدْفَعْ بِٱلَّتِى هِىَ أَحْسَنُ فَإِذَا ٱلَّذِى بَيْنَكَ وَبَيْنَهُۥ عَدَٰوَةٌۭ كَأَنَّهُۥ وَلِىٌّ حَمِيمٌۭ وَمَا يُلَقَّىٰهَآ إِلَّا ٱلَّذِينَ صَبَرُوا۟ — enmity turned into intimacy, given only to those with ṣabr.
- 8:46 — God to the believers: وَلَا تَنَٰزَعُوا۟ فَتَفْشَلُوا۟ وَتَذْهَبَ رِيحُكُمْ ۖ وَٱصْبِرُوٓا۟.
- 3:103 — enemies made brothers: إِذْ كُنتُمْ أَعْدَآءًۭ فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًۭا.

### 11. The charge left behind: testament, witnesses, guarantor

A dying person gives instructions to those who will carry them out. The waṣiyya is "speech that is joined" to the living. The heirs' due shares are rights (ḥuqūq), and a father may withhold or take back what he gave. Witnesses to the bequest are held after the prayer and sworn, a guarantor stands surety, and a trust (amāna) is handed over. The surah's تواصوا, its time-word (which also names the ʿaṣr prayer and the long stretch of a life), al-ḥaqq and al-ṣabr all have members in this scene. The mufradat defines waṣiyya as giving another person something to act on (يعمل به), with admonition.

- 103:1 وَٱلْعَصْرِ — ع ص ر B001 — «صلاة العصر» (sihah;tahdhib;maqayis) — the prayer after which, by the commentators' reading of 5:106 (from memory), the witnesses are held.
- 103:1 وَٱلْعَصْرِ — ع ص ر B006 — «يعتصر الوالد على ولده في ماله أي يمنعه إياه ويحبسه عنه» (sihah); «أعطيت فلانا عطية فاعتصرتها أي رجعت فيها» (tahdhib) — the father keeping back his child's property; a gift taken back.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B002 — «الوصية بعد الموت» (ayn); «الوصية من هذا القياس كأنه كلام يوصى أي يوصل» (maqayis); «أوصيت له بشئ وأوصيت إليه إذا جعلته وصيك» (sihah); «الوصي الموصي والموصى إليه جميعا» (jamhara); «التقدم إلى الغير بما يعمل به مقترنا بوعظ» (mufradat) — the testament, the executor, the charge joined to the living. The last phrase joins waṣiyya with ʿamal.
- 103:3 ءَامَنُوا۟ — ء م ن B001 — «الأمانة ضد الخيانة ومعناها سكون القلب» (maqayis) — the trust that is handed over.
- 103:3 بِٱلْحَقِّ — ح ق ق B003 — «الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي» (sihah;tahdhib); «استحقها على المشتري أي ملكها عليه» (tahdhib) — each heir's due share.
- 103:3 بِٱلْحَقِّ — ح ق ق B002 — «حق الشيء وجب» (maqayis;sihah;tahdhib) — the bequest made binding.
- 103:3 بِٱلصَّبْرِ — ص ب ر B002 — «صبرت يمينه أي حلفته» (ayn;maqayis;tahdhib); «قتل صبر ويمين صبر» (sihah;tahdhib) — the oath imposed by authority on the witnesses.
- 103:3 بِٱلصَّبْرِ — ص ب ر B003 — «الصبير هو الكفيل» (maqayis;sihah) — the guarantor.

Quran:
- 2:180 — God legislating: إِذَا حَضَرَ أَحَدَكُمُ ٱلْمَوْتُ إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ … حَقًّا عَلَى ٱلْمُتَّقِينَ — waṣiyya and ḥaqq in one ayah.
- 5:106–107 — God to the believers, on a bequest made while travelling: شَهَٰدَةُ بَيْنِكُمْ إِذَا حَضَرَ أَحَدَكُمُ ٱلْمَوْتُ حِينَ ٱلْوَصِيَّةِ … تَحْبِسُونَهُمَا مِنۢ بَعْدِ ٱلصَّلَوٰةِ فَيُقْسِمَانِ بِٱللَّهِ … فَإِنْ عُثِرَ عَلَىٰٓ أَنَّهُمَا ٱسْتَحَقَّآ إِثْمًۭا … لَشَهَٰدَتُنَآ أَحَقُّ مِن شَهَٰدَتِهِمَا — testament, holding, oath and ḥaqq together. (from memory) Many commentators take "the prayer" here to be the ʿaṣr prayer.
- 2:132–133 — Abraham and Jacob at death: وَوَصَّىٰ بِهَآ إِبْرَٰهِۦمُ بَنِيهِ وَيَعْقُوبُ … إِذْ حَضَرَ يَعْقُوبَ ٱلْمَوْتُ إِذْ قَالَ لِبَنِيهِ مَا تَعْبُدُونَ مِنۢ بَعْدِى — the faith handed on as a bequest across generations.
- 31:13, 31:17 — Luqman counselling his son (the scene opens at 31:13 وَإِذْ قَالَ لُقْمَٰنُ لِٱبْنِهِۦ وَهُوَ يَعِظُهُۥ, recalled): يَٰبُنَىَّ أَقِمِ ٱلصَّلَوٰةَ وَأْمُرْ بِٱلْمَعْرُوفِ … وَٱصْبِرْ عَلَىٰ مَآ أَصَابَكَ — waṣiyya "with admonition", ending in ṣabr.
- 4:6 — the orphans' property handed over once maturity is perceived (فَأَشْهِدُوا۟ عَلَيْهِمْ).
- 46:15 — وَوَصَّيْنَا ٱلْإِنسَٰنَ بِوَٰلِدَيْهِ — God's own charge to the human.
- 12:72 — Joseph's crier: وَلِمَن جَآءَ بِهِۦ حِمْلُ بَعِيرٍۢ وَأَنَا۠ بِهِۦ زَعِيمٌۭ — a guarantor (zaʿīm, like ṣabīr / kafīl) standing behind a reward.

### 12. The thrust that does not swerve

A spear is held so that its forepart, just behind the head, carries the thrust. The thrust goes straight, with no swerve, and reaches the body's inner cavity. ʿamal names that part of the spear, and also the use of the spear (يعمل … رمحه). ḥaqq names the thrust that goes straight in. ṣabr names the man set up as a target to be killed. Its reversal is khusr as ḍalāl, straying off the line.

- 103:3 وَعَمِلُوا۟ — ع م ل B009 — «عامل الرمح صدره دون السنان ويجمع عوامل» (tahdhib); «عامل الرمح ما يلي السنان وهو دون الثعلب» (sihah) — the spear's forepart behind the head.
- 103:3 وَعَمِلُوا۟ — ع م ل B002 — «يستعمل غيره ويعمل رأيه أو كلامه أو رمحه» (maqayis) — putting the spear to work.
- 103:3 بِٱلْحَقِّ — ح ق ق B009 — «طعنة محتقة أي لا زيغ فيها وقد نفذت» (sihah); «المحتق من الطعن النافذ إلى الجوف» (tahdhib); «طعنة محتقة إذا وصلت إلى الجوف» (maqayis) — the thrust with no swerve that reaches the inside.
- 103:3 بِٱلصَّبْرِ — ص ب ر B002 — «الصبر نصب الإنسان للقتل» (ayn;tahdhib) — the man set up as a target.
- 103:2 ٱلْإِنسَٰنَ — ء ن س — the إنسان named in that ṣabr phrase.
- 103:2 خُسْرٍ — خ س ر B004 — «الخسر والخسار والخسران واحد وهو الضلال» (jamhara) — straying off the line, the opposite of «لا زيغ فيها».

### 13. Tight weave, seated door, and the spider's house

Thread is woven tight, speech is put together firmly, bricks are used in a building, and a door's foot sits in its socket. All of these are things made sound and joined part to part. Against them stand the spider's house, which ḥaqq also names, and, if khusr's Maqāyīs root-phrase is read as printed (النقض), the undoing of what was made. ṣalāḥ is the repair of what was spoiled, and waṣy is joining one thing to another.

- 103:2 خُسْرٍ — خ س ر B001 — «أصل واحد يدل على النقض» (maqayis) — as printed, "undoing, unravelling". The Turkish gloss reads it as decrease (النقص). The unravelling reading rests on this one letter.
- 103:3 وَعَمِلُوا۟ — ع م ل B002 — «والبناء يستعمل اللبن» (maqayis) — bricks put to use in a building.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B001 — «الصلاح ضد الفساد والاصلاح نقيض الإفساد» (sihah); «أصل واحد يدل على خلاف الفساد» (maqayis) — making sound what was spoiled.
- 103:3 وَتَوَاصَوْا۟ — و ص ي B001 — «ووصيت الشيء وصلته» (maqayis) — joining part to part.
- 103:3 بِٱلْحَقِّ — ح ق ق B010 — «ثوب محقق إذا كان محكم النسج» (maqayis;sihah); «كلام محقق أي رصين» (sihah); «أحققت الأمر إحقاقا إذا أحكمته وصححته» (tahdhib) [fixed expression] — tight weave, firmly made speech, a thing made firm.
- 103:3 بِٱلْحَقِّ — ح ق ق B011 — «مطابقة رجل الباب في حقه» (mufradat); «الحق ملتقى كل عظمين» (maqayis) — the door's foot seated in its socket; the meeting of two bones.
- 103:3 بِٱلْحَقِّ — ح ق ق B011 — «حق الكهول بيت العنكبوت» (tahdhib) — the spider's house, named by the same word.

Quran:
- 29:41 — God, of those who take patrons other than Him: كَمَثَلِ ٱلْعَنكَبُوتِ ٱتَّخَذَتْ بَيْتًۭا ۖ وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ.
- 16:92 — God, on oaths broken: وَلَا تَكُونُوا۟ كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًۭا — the spun yarn undone. This belongs to the chain only on the printed النقض.

### 14. The day that makes each one's work come due

al-Ḥāqqa is the day that "makes every human due with his work". The dictionary joins the surah's ḥaqq, insān and ʿamal in that one phrase. On that day deeds are sorted into sound and bad, scales are weighed and some come up short, and khusr is glossed as "punishment for his sins" and "being put far from the good". The surah places al-insān inside khusr and names, as the exception, those whose works are sound. The whole surah can be heard as an account that has come due.

- 103:2 ٱلْإِنسَٰنَ / 103:3 وَعَمِلُوا۟ / 103:3 بِٱلْحَقِّ — ح ق ق B006 — «سميت حاقة لأنها تحق كل إنسان بعمله» (tahdhib); «الحاقة القيامة لأنها تحق بكل شيء» (maqayis); «الحاقة إشارة إلى القيامة لأنه يحق فيه الجزاء» (mufradat) — the day that makes each human's work come due.
- 103:2 خُسْرٍ — خ س ر B004 — «لفي عقوبة بذنوبه» (tahdhib); «غير إبعاد من الخير» (tahdhib) — the tahdhib gloss of la-fī khusr: in punishment for his sins.
- 103:2 خُسْرٍ — خ س ر B003 — «خسرت الميزان وأخسرته إذا نقصته» (maqayis) — the scale.
- 103:3 وَعَمِلُوا۟ — ع م ل B001 — «الأعمال الصالحة والسيئة» (mufradat) — deeds sorted into sound and bad. This phrase joins ʿamal and ṣāliḥ.
- 103:3 ٱلصَّٰلِحَٰتِ — ص ل ح B001 — «الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال» (mufradat) — the soundness of the deeds that are weighed.
- 103:3 بِٱلْحَقِّ — ح ق ق B002 — «حق الشيء وجب» (maqayis;sihah;tahdhib) — the recompense made binding.
- 103:3 بِٱلصَّبْرِ — ص ب ر B013 — «ما أعملهم بعمل أهل النار» (mufradat) — the reversed ṣabr as the deeds that lead to the Fire.

Quran:
- 69:1–3 — the surah's opening: ٱلْحَآقَّةُ مَا ٱلْحَآقَّةُ وَمَآ أَدْرَىٰكَ مَا ٱلْحَآقَّةُ.
- 23:101–103 — God, of the blast: فَلَآ أَنسَابَ بَيْنَهُمْ … وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ.
- 7:8–9 — God, of the weighing: وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم.
- 101:6–9 — the scales heavy or light (101:6, 101:8).
- 18:103–104 — the greatest losers in works, who think they do well.
- 99:7–8 (recalled) — فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُ وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ شَرًّا يَرَهُ.

### 15. Origin, rank and the lowly

People trace themselves back to a root stock, noble or base. ʿaṣr names that origin, and also the lowly clients who rank below everyone else. khusr's extended forms name the weak and the vile among people. The surah says al-insān, the whole species, is in loss, so neither noble descent nor low rank decides the outcome. The exception is drawn by faith and deeds.

- 103:1 وَٱلْعَصْرِ — ع ص ر B011 — «العنصر والعنصر الأصل والحسب» (sihah); «فلان كريم العصير أي كريم النسب» (tahdhib); «كلا يئل في الانتساب إلى أصله الذي هو منه» (maqayis) — root stock and noble descent; each returns to his origin.
- 103:1 وَٱلْعَصْرِ — ع ص ر B012 — «هؤلاء موالينا عصرة أي دنية دون من سواهم» (sihah) — the lowest of the clients.
- 103:2 ٱلْإِنسَٰنَ — ء ن س B001 — «الإنس البشر والواحد إنسي والجمع أناسي» (sihah); «الإنس خلاف الجن وسموا لظهورهم» (maqayis;mufradat) — humankind as a whole.
- 103:2 خُسْرٍ — خ س ر B005 — «الخناسر جمع خنسر وهو نحو الخنسرى وفي معناه وهم لئام الناس ورذالهم» (jamhara); «الخناسر الضعاف من الناس» (jamhara) — the vile and weak among people.

Quran:
- 23:101 — فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ, followed in 23:103 by خَسِرُوٓا۟ أَنفُسَهُمْ.
- (recalled) 26:111 — Noah's people: أَنُؤْمِنُ لَكَ وَاتَّبَعَكَ الْأَرْذَلُونَ; 11:27 — مَا نَرَاكَ اتَّبَعَكَ إِلَّا الَّذِينَ هُمْ أَرَاذِلُنَا. The chiefs measure faith by rank.

## Interactions

- Trade (1) × Time (3): العصر الدهر is the capital, and خسر التاجر إذا وضع من رأس ماله is its depletion. (from memory) Rāzī's ice-seller.
- Trade (1) × Labor (2): shared member خ س ر B002 «صفقة خاسرة أي غير مربحة». ع م ل B004 (wage) and B005 (dealing) are the two ways of earning. 95:6 أَجْرٌ غَيْرُ مَمْنُونٍۢ.
- Trade (1) × Holding (5) × Reckoning (14): 2:175 puts the bargain (ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ) and the reversed ṣabr (فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ) together. mufradat's «ما أعملهم بعمل أهل النار» joins ṣabr and ʿamal.
- Trade (1) × Refuge (6): 61:10 تِجَٰرَةٍۢ تُنجِيكُم.
- Trade (1) × Reckoning (14): shared member خ س ر B003, the scale. 23:102–103, 7:9, 101:6–8, 55:9, 83:3.
- Trade (1) × Seeing (9): «المقتنيات النفسية كالصحة والسلامة والعقل والإيمان والثواب» names īmān as stock that can be lost.
- Labor (2) × Time (3): «العصر العشي» and «صلاة العصر» mark the end of the working day. (from memory) The hadith of the hired workers.
- Labor (2) × Reckoning (14): «سميت حاقة لأنها تحق كل إنسان بعمله» — the wage that comes due. 18:103–104.
- Time (3) × Company (10) / Testament (11): «وصيت الليلة باليوم وصلتها» set beside «العصران الليل والنهار». Counsel passed person to person is a joining of the same kind as night to day. «كأنه كلام يوصى أي يوصل».
- Time (3) × Holding (5): 18:28 وَٱصْبِرْ نَفْسَكَ … بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ and 40:55 فَٱصْبِرْ … بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ lay ṣabr along «العصران الغداة والعشي». «حق الانتظار» joins ḥaqq and ṣabr in waiting.
- Time (3) × Rain (7) × Beast (8): ح ق ق B013 «أحقت الناقة من الربيع» is at once a season, a pasture effect and the camel's condition. و ص ي B004, the pasture that gives itself, feeds it.
- Press (4) × Rain (7): the same verb in «ضغط شيء حتى يتحلب» and «السحابة المعصر التي تتحلب بالمطر». 12:49 holds rain-relief and pressing in one clause.
- Press (4) × Holding (5): ص ب ر B008 «الصبر بكسر الباء عصارة شجرة» defines ṣabr by ʿuṣāra. ص ب ر B018, the stopper, both seals the extract and is a holding. 12:36: pressing dreamt in prison. (from memory) ʿAdī ibn Zayd's choking verse composed in prison.
- Press (4) × Origin and the human (15): «الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء» joins الإنسان and ʿ-ṣ-r.
- Holding (5) × Refuge (6): ع ص ر B005 «تعلق بشيء وامتساك به» (holding on) against ع ص ر B006 «العصر الحبس» (being held back). ص ب ر B006 «أمر لا منفذ له عنه» is the holding that refuge escapes.
- Holding (5) × Testament (11): 5:106 تَحْبِسُونَهُمَا مِنۢ بَعْدِ ٱلصَّلَوٰةِ فَيُقْسِمَانِ — ḥabs, the imposed oath (يمين صبر), waṣiyya and ḥaqq (5:107) in one scene.
- Holding (5) × Spear (12): shared member «الصبر نصب الإنسان للقتل».
- Rain (7) × Company (10): «تواصى النبت إذا اتصل» and «تواصى القوم إذا تواصلوا» use the same form, once for plants and once for people.
- Rain (7) × Trade (1): «العصارة الغلة» is the return. 2:264–266 stages spending as gardens rained on or burned by the iʿṣār.
- Beast (8) × Testament (11) / Trade (1): 33:72 ٱلْأَمَانَةَ … فَأَبَيْنَ أَن يَحْمِلْنَهَا … وَحَمَلَهَا ٱلْإِنسَٰنُ joins «ما استحق أن يحمل عليه», «الأمون الناقة الأمينة» and «الصبير الجبل».
- Seeing (9) × Holding (5): 12:17–18 بِمُؤْمِنٍۢ لَّنَا … فَصَبْرٌۭ جَمِيلٌۭ.
- Seeing (9) × Refuge (6): 20:10 ءَانَسْتُ نَارًۭا … أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى — fire seen at a distance as the hope of warmth and guidance for a family on the road.
- Seeing (9) × Testament (11): 4:6 فَإِنْ ءَانَسْتُم مِّنْهُمْ رُشْدًۭا فَٱدْفَعُوٓا۟ إِلَيْهِمْ أَمْوَٰلَهُمْ.
- Seeing (9): «إذعان النفس للحق على سبيل التصديق» joins āmana and ḥaqq.
- Company (10) × Refuge (6): shared member ص ب ر B003 «صبير القوم الذي يصبر لهم ويكون معهم في أمورهم». 3:103: holding the rope together, enemies made brothers, pulled back from the brink.
- Company (10): «الصلح يختص بإزالة النفار» and «الأنس خلاف النفور» use the same nifār / nufūr, joining ṣalaḥ and ins.
- Company (10) × Testament (11): و ص ي B002 and B003. Mutual counsel is the waṣiyya given in both directions. 90:17, 31:17.
- Spear (12) × Seeing (9): «لا زيغ فيها» and «أصل الحق المطابقة» set against khusr «وهو الضلال».
- Weave (13) × Refuge (6): 29:41, the spider's house (named by ح ق ق B011) as the false refuge of those who take other patrons.
- Reckoning (14) × Origin (15): 23:101–103, lineage cut off, then the scale, then خَسِرُوٓا۟ أَنفُسَهُمْ.
- Reckoning (14) × Labor (2) × Soundness: «الأعمال الصالحة والسيئة» joins ʿamal and ṣāliḥ.
- Wuṣy (11) × Labor (2): «التقدم إلى الغير بما يعمل به مقترنا بوعظ» joins waṣiyya and ʿamal.

## Ayat

### 103:1 وَٱلْعَصْرِ

- Chain 1, trade: العصر الدهر — the time spent as capital, plus the yield drawn out (المعتصر) and property drawn from the hand. Scene: time is a trader's stock; each human deal loses principal or is short-weighed, except a bargain of faith and sound deeds in which partners pass the due between them.
- Chain 2, labor: العصر العشي، صلاة العصر — the late afternoon when the day's work ends and the wage falls due. Scene: labourers hired for the day work until ʿaṣr; those whose work was sound are paid, the rest find the day earned nothing.
- Chain 3, time: العصران الليل والنهار / الغداة والعشي، العصر الدهر، بلغت عصر شبابها — day, night, the long age, a stage of life. Scene: night joined to day, morning to evening, winter to spring; the counsellors of 103:3 join each other as waṣṣā joins night to day.
- Chain 4, press: ضغط شيء حتى يتحلب، العصارة، المعصار، the choking person's small sips, the tongue wrung by thirst. Scene: grapes squeezed in a sack until juice runs; the surah ends on ṣabr, the bitter pressed sap stoppered in its flask.
- Chain 5, holding: العصر الحبس، فلان عاصر إذا كان ممسكا، the girl kept indoors, grain kept in its husk. Scene: the self holds itself from panic (ṣabr); a captive is held for death; a closed hand holds back what it owes.
- Chain 6, refuge: العصر الملجأ، المنجاة، عصرة المنجود، تعلق بشيء وامتساك به، origin as refuge, المعاصر الدروع. Scene: one under threat clings to a refuge and enters protection (amn), set against ruin with no exit.
- Chain 7, rain: المعصرات، عصر القوم أي مطروا، العصارة الغلة، the crop in its husks; and the reversal الإعصار. Scene: layered cloud pressed with rain, plants joining plants, pasture yielding, camels fattening, grain heaped, or a fiery whirlwind burning the garden and rain leaving bare rock.
- Chain 10, company: ما بينهما عصر … أي ما بينهما مودة ولا قرابة — the bond. Scene: contenders reconciled, desolation replaced by familiarity, people joined by counsel.
- Chain 11, testament: صلاة العصر (the hour of the sworn witnesses, from memory), the father withholding or taking back a gift. Scene: a dying person's charge joined to the living, witnesses held after prayer and sworn, a guarantor, the heirs' due.
- Chain 15, origin: العنصر الأصل والحسب، كريم العصير، موالينا عصرة. Scene: everyone traces back to a stock, noble or low, and the loss covers all.

### 103:2 إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ

- Chain 1, trade: خُسْرٍ — loss of principal, the bargain without profit, the short scale, decrease, inner goods (faith among them) lost. Scene: as above; al-insān is the trader whose capital, time, is running down.
- Chain 2, labor: خُسْرٍ — صفقة خاسرة. Scene: the day's work ends at ʿaṣr with nothing earned unless the work was sound.
- Chain 4, press: ٱلْإِنسَٰنَ is the one choking who sips; خُسْرٍ is the mass reduced. Scene: the squeeze, the running juice, the bitter stoppered sap at the surah's end.
- Chain 5, holding: ٱلْإِنسَٰنَ stands in «الصبر نصب الإنسان للقتل», the human held by another. Scene: self-holding (103:3) against being held.
- Chain 6, refuge: خُسْرٍ — هلاك, the ruin to be escaped. Scene: refuge, protection, house of safety against ruin.
- Chain 7, rain: خُسْرٍ — the harvest destroyed. Scene: rain, joined growth, the fattened herd, against whirlwind and bare rock.
- Chain 8, beast: ٱلْإِنسَٰنَ — the insī side, from which the rider mounts and milks. Scene: a camel come of age to be loaded, trusted, made for work, cared for or over-driven, on gravel and mountain roads, the human at its near side (33:72: the human carries the trust).
- Chain 9, seeing: ٱلْإِنسَٰنَ — the one who perceives (آنس), and the image in the pupil. Scene: seeing fire at a distance, inspecting, accepting the report, verifying until certain.
- Chain 10, company: ٱلْإِنسَٰنَ — uns against desolation, the chosen intimate. Scene: alone in loss here, joined to others in 103:3.
- Chain 12, spear: ٱلْإِنسَٰنَ set up as a target; خُسْرٍ = ḍalāl, straying off the line. Scene: the spear's forepart carries a thrust straight to the inner cavity, with no swerve.
- Chain 13, weave: خُسْرٍ — «يدل على النقض» as printed, undoing. Scene: tight weave, bricks, the door seated in its socket, against the spider's house and the yarn undone.
- Chain 14, reckoning: ٱلْإِنسَٰنَ and the tahdhib gloss «لفي عقوبة بذنوبه»; the short scale. Scene: the Ḥāqqa makes each human due with his work; the light scale loses the self.
- Chain 15, origin: ٱلْإِنسَٰنَ — the whole species; خُسْرٍ — khanāsir, the weak and vile. Scene: stock and rank do not decide who is in loss.

### 103:3 إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ

- Chain 1, trade: ءَامَنُوا۟ (trustworthiness), وَعَمِلُوا۟ (dealing), بِٱلْحَقِّ (the due share), بِٱلصَّبْرِ (buying by the heap, unmeasured). Scene: the one deal that does not lose principal.
- Chain 2, labor: وَعَمِلُوا۟ (purposeful work, the hand-crew, the wage, the office), ٱلصَّٰلِحَٰتِ (sound work), بِٱلْحَقِّ (the wage made due), بِٱلصَّبْرِ (the guarantor). Scene: the crew paid at the end of the day.
- Chain 3, time: وَتَوَاصَوْا۟ (joining night to day), بِٱلْحَقِّ (the heart of winter, the camel's mating time, spring), بِٱلصَّبْرِ (winter cold, waiting). Scene: time made of joined parts; people joining one another through it.
- Chain 4, press: بِٱلصَّبْرِ — «عصارة شجرة», «الدواء المر», the stopper, the vessel's sides. Scene: what ʿaṣr squeezed out at the start is kept, bitter, in its flask at the end.
- Chain 5, holding: بِٱلصَّبْرِ — the self held from panic, fasting, waiting; the reversals (captive, forced oath, retaliation, daring toward the Fire). Scene: the believers hand each other the self-holding form of ṣabr, not the form in which one is held.
- Chain 6, refuge: ءَامَنُوا۟ (amn, entering protection, the house of safety), بِٱلْحَقِّ (the ḥaqīqa one must defend), بِٱلصَّبْرِ (the surety who stays with the group; umm ṣabūr, the calamity without exit), ٱلصَّٰلِحَٰتِ (Ṣalāḥ, a name of Mecca). Scene: the excepted ones are those who reached safety.
- Chain 7, rain: وَتَوَاصَوْا۟ (تواصى النبت; the pasture giving itself), بِٱلْحَقِّ (the herd fattened), بِٱلصَّبْرِ (layered white cloud, the food heap; gravel and hard rock). Scene: rain to growth to herd to heap, against the whirlwind and bare rock.
- Chain 8, beast: ءَامَنُوا۟ (the trusted she-camel), وَعَمِلُوا۟ (the work-camel, its legs, the worn road, walkers), ٱلصَّٰلِحَٰتِ (treating the mount well), بِٱلْحَقِّ (the camel fit to be loaded, over-driving, the lean horse), بِٱلصَّبْرِ (gravel, mountain). Scene: the mount and its load on the road.
- Chain 9, seeing: ءَامَنُوا۟ (taṣdīq, yielding to the ḥaqq), وَعَمِلُوا۟ (putting the mind to work; the far-seeing eye), بِٱلْحَقِّ (correspondence, certainty, confirming). Scene: perceive, assent, make sure.
- Chain 10, company: ٱلصَّٰلِحَٰتِ (ṣulḥ removing nifār), بِٱلْحَقِّ (taḥāqqa, the quarrel over who is right, reversed), وَتَوَاصَوْا۟ (تواصلوا, each counselling the other), بِٱلصَّبْرِ (the companion who stays). Scene: contenders turned into a company joined by counsel.
- Chain 11, testament: وَتَوَاصَوْا۟ (waṣiyya, executor, speech joined to the living), ءَامَنُوا۟ (amāna), بِٱلْحَقِّ (the heirs' shares, the binding bequest), بِٱلصَّبْرِ (the imposed oath, the guarantor). Scene: the dying person's charge carried on by witnesses held after prayer and sworn.
- Chain 12, spear: وَعَمِلُوا۟ (the spear's forepart; wielding the spear), بِٱلْحَقِّ (the thrust with no swerve that reaches the inside), بِٱلصَّبْرِ (the man set up as target). Scene: a straight thrust, against khusr's swerve.
- Chain 13, weave: وَعَمِلُوا۟ (bricks in a building), ٱلصَّٰلِحَٰتِ (repair), وَتَوَاصَوْا۟ (joining part to part), بِٱلْحَقِّ (tight weave [fixed expression], firm speech, the door's foot in its socket; the spider's house). Scene: things made firm against the flimsy house and undone yarn.
- Chain 14, reckoning: وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ (الأعمال الصالحة والسيئة), بِٱلْحَقِّ (al-Ḥāqqa, the binding recompense), بِٱلصَّبْرِ (the reversal: the deeds of the people of the Fire). Scene: the day that makes each human due with his work, scales weighed.

