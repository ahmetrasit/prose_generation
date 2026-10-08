Surah: 99. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (99:1 to 99:8), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s099/surah.r2/text.md =====
# Surah 99

- 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/out/s099/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. The ground shaken and casting out its loads

The surah opens on an object and its operation: the ground is shaken "with its shaking", and the same ground brings out what it held. The dictionary's own definition of the quake is built on the surah's two first words ("زلزلت الأرض زلزالا"), and its definition of the loads names the ground as their container ("أثقال الأرض كنوزها وأجساد بني آدم"): treasures and human bodies lie inside the ground as heavy contents. The shaking in 99:1 is the operation, أَخْرَجَتِ is the crossing from inside to outside, and أَثْقَالَهَا names what crosses. The scene ends with the ground emptied and its contents lying on its surface.

- 99:1 زُلْزِلَتِ / زِلْزَالَهَا — ز ل ز ل B001 — «الزلزلة: الاضطراب أخذ من زلزلت الأرض زلزالا» — the operation: violent agitation of the ground. The dictionary phrase joins زلزل and الأرض.
- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B001 — «الأرض التي نحن عليها»؛ «كل شيء يسفل ويقابل السماء» — the object: the lower body that holds things and is shaken.
- 99:2 وَأَخْرَجَتِ — خ ر ج B001 — «الخروج نقيض الدخول»؛ «خرج خروجا برز من مقره أو حاله» — the crossing out of a resting place (مقر), a reversal of the earlier entry.
- 99:2 وَأَخْرَجَتِ — خ ر ج B002 — «الإخراج أكثر ما يقال في الأعيان» — bringing out is said mostly of concrete things, which fits bodies and treasures.
- 99:2 أَثْقَالَهَا — ث ق ل B002 — «أثقال الأرض كنوزها وأجساد بني آدم» — the contents: buried treasures and the bodies of Adam's children. The phrase joins ثقل and الأرض.
- 99:2 أَثْقَالَهَا — ث ق ل B002 — «متاع المسافر وحشمه وجمعه أثقال» — a traveller's baggage. The ground puts down the baggage it carried.
- 99:7 خَيْرًا — خ ي ر B006 [fixed expression] — «يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء» — a hidden animal forced out of its burrow by another opening. A small scene of the same operation: what hides in the ground is made to come out. The phrase joins خير and خرج.

Passages:
- 84:3–4 وَإِذَا ٱلْأَرْضُ مُدَّتْ ۝ وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ — description of the Hour (scene opens 84:1 إِذَا ٱلسَّمَآءُ ٱنشَقَّتْ). The ground throws out what is in it and empties itself.
- 100:9 إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ — warning to ungrateful man (scene opens 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ). What is in the graves is turned out.
- 82:4 وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ — the Hour (scene opens 82:1).
- 22:1 إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌ — God addressing mankind. The quake of the Hour named with the same root.
- 56:4 إِذَا رُجَّتِ ٱلْأَرْضُ رَجًّا; 73:14 يَوْمَ تَرْجُفُ ٱلْأَرْضُ وَٱلْجِبَالُ; 79:6 يَوْمَ تَرْجُفُ ٱلرَّاجِفَةُ; 89:21 إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّا دَكًّا; 69:14 وَحُمِلَتِ ٱلْأَرْضُ وَٱلْجِبَالُ فَدُكَّتَا دَكَّةً وَٰحِدَةً — the shaking or pounding of the ground at the Hour, in other words.
- 50:4 قَدْ عَلِمْنَا مَا تَنقُصُ ٱلْأَرْضُ مِنْهُمْ — God answering deniers of resurrection. The ground holds and consumes the bodies, which are its "loads".
- 50:44 يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا — the gathering. The ground splits open off the bodies it held.
- 18:47 وَتَرَى ٱلْأَرْضَ بَارِزَةً — the Day, with the mountains moved. The ground left bare.
- 22:7 وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ — God addressing people in doubt about resurrection (scene opens 22:5).
- From memory (tafsir): the exegetes read أَثْقَالَهَا as the dead and the buried treasures, which is the dictionary's pair.

### 2. A heavy body delivering what it carried

The same words also give a body heavy with what is inside it, which grows until it gives that load out. ثقل names a pregnant woman's heaviness, خرج names both delivery and a swelling that "comes out of itself", and رأى names a pregnancy that shows so that it is seen. In the surah the earth is heavy (أَثْقَالَهَا), it brings out (أَخْرَجَتِ), and what comes out is then seen (يَرَهُۥ). The ground is a womb or a swollen body that empties.

- 99:2 أَثْقَالَهَا — ث ق ل B007 — «أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها» — the load as something carried inside the body, the heaviness of late pregnancy.
- 99:2 أَثْقَالَهَا — ث ق ل B002 — «أثقال الأرض كنوزها وأجساد بني آدم» — what the earth carries is human bodies, so its delivery is of people.
- 99:2 وَأَخْرَجَتِ — خ ر ج B001 — «خرج خروجا برز من مقره أو حاله» — what was inside leaves its resting place.
- 99:2 وَأَخْرَجَتِ — خ ر ج B004 — «الخراج ورم وقرح يخرج من ذاته» — a swelling that pushes out on its own, the body expelling inner matter.
- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B011 [fixed expression] — «أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة» — the earth word used of a sore swelling with matter.
- 99:6, 99:7, 99:8 لِّيُرَوْا۟ / يَرَهُۥ — ر ء ي B010 — «أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها»؛ «أرأت الشاة إذا عظم ضرعها قبل ولادها» — the carried load becomes visible and is seen to be real.

Passages:
- 7:189 فَلَمَّآ أَثْقَلَت دَّعَوَا ٱللَّهَ رَبَّهُمَا — God describing the first couple's pregnancy. The Quran uses أثقلت itself for late pregnancy.
- 22:1–2 إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌ ۝ … وَتَضَعُ كُلُّ ذَاتِ حَمْلٍ حَمْلَهَا — God addressing mankind. The quake of the Hour and every pregnant female delivering her load are staged together.
- 22:5 وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ … ثُمَّ نُخْرِجُكُمْ طِفْلًا … وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ — God to people in doubt about resurrection. The womb's bringing out (نُخْرِجُكُمْ) and the earth's shaking and swelling are set side by side.
- 16:78 وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ — God listing favours. أخرج used of birth.
- 20:55 مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ — words about the earth that follow Moses' answer to Pharaoh (scene opens 20:49). The earth as the place people come from and come out of again.
- 71:17–18 وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًا ۝ ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًا — Noah addressing his people (his speech opens 71:10).
- 84:4 وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ — the earth empties itself (scene opens 84:1).

### 3. The shaking passing from the ground into bodies and people

The earth word itself names shivering, and the same root names a person who jerks head and body without meaning to. زلزل extends to "the hardships of time", and حدث names a calamity that comes down. The quake in 99:1 therefore runs straight into the human body and mind, and 99:3 shows its effect: man, shaken, asks what is happening to the earth. The scene is one tremor moving from the ground into the one who stands on it.

- 99:1 زُلْزِلَتِ / زِلْزَالَهَا — ز ل ز ل B001 — «الزلزلة: الاضطراب» — agitation that does not settle.
- 99:1 زِلْزَالَهَا — ز ل ز ل B002 [fixed expression] — «زلازل الدهر: شدائده» — the same word for hardships that shake people.
- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B008 — «الأرض الرعدة»؛ «بفلان أرض أي رعدة»؛ «الأرْص النفضة والرعدة» — the earth word as a body's shiver. The last phrase is spelt الأرْص in the source as given, and pairs النفضة, a shaking-out, with the shiver.
- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B012 — «المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد» — involuntary jerking of head and body, the quake as a seizure.
- 99:4 تُحَدِّثُ — ح د ث B005 — «الحادثة النازلة العارضة»؛ «الحدث من أحداث الدهر شبه النازلة» — the event as a calamity that descends.
- 99:3 وَقَالَ ٱلْإِنسَٰنُ — ق و ل B001 — «القول من النطق» — the shaken human's outburst of speech, مَا لَهَا.

Passages:
- 22:1–2 إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ … وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ — God addressing mankind. The quake of the Hour seen in people staggering.
- 2:214 مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ — God to the believers about earlier communities. The quake verb used of people under hardship, ending in their outcry.
- 33:11 هُنَالِكَ ٱبْتُلِىَ ٱلْمُؤْمِنُونَ وَزُلْزِلُوا۟ زِلْزَالًا شَدِيدًا — the siege of the Trench (scene opens 33:9). The surah's exact pair زُلْزِلُوا / زِلْزَالًا applied to people.
- 75:10 يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ — man at the Hour (scene opens 75:7). The same shaken question as 99:3.
- 36:52 قَالُوا۟ يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا — the raised dead (scene opens 36:51). The startled question at rising.

### 4. Question, secret message and spoken report: the earth made to speak

99:3–5 make a dialogue in three steps. Man asks (قَالَ … مَا لَهَا). The earth answers by telling its news (تُحَدِّثُ أَخْبَارَهَا). The news comes from a secret message from her Lord (أَوْحَىٰ لَهَا). The dictionary phrases join these steps: a حديث is "every speech that reaches man by hearing or by وحي"; خبر is the inside of a matter as against its outward look; وحي is knowledge passed on in hiding, by sign, by faint voice or by writing on stone. One branch of قول records a thing "saying" by its state ("the basin filled and said: enough"). The earth is a silent, written-on ground that is given a voice, and man is the one who hears.

- 99:3 وَقَالَ — ق و ل B001 — «القول من النطق»؛ «المركب من الحروف المبرز بالنطق» — man's articulated question.
- 99:3 وَقَالَ — ق و ل B014 — «للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني» — "saying" by one's state. The word used for man's speech also names a thing that speaks without a tongue, which is how the earth "tells".
- 99:3 وَقَالَ — ق و ل B017 — «في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا» — inspiration called "saying". This joins قول to the وحي of 99:5.
- 99:3 وَقَالَ — ق و ل B002 — «المقول اللسان» — the tongue, the organ the earth is given.
- 99:4 أَخْبَارَهَا — خ ب ر B001 — «الاستخبار السؤال عن الخبر» — asking for news: man's مَا لَهَا is a request for exactly what 99:4 supplies.
- 99:4 أَخْبَارَهَا — خ ب ر B001 — «الخبر النبأ»؛ «الخبرة المعرفة ببواطن الأمر»؛ «المخبر خلاف المنظر» — the report is of the inside of things, as against their outward look.
- 99:4 تُحَدِّثُ — ح د ث B003 — «كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث» — speech reaching man by hearing or by وحي. The phrase joins الإنسان (99:3), حديث (99:4) and وحي (99:5).
- 99:4 تُحَدِّثُ — ح د ث B003 — «الحديث الخبر» (sihah) — the dictionary equates the verb's object with أَخْبَارَهَا.
- 99:4 تُحَدِّثُ — ح د ث B004 — «فجعلناهم أحاديث أي أخبارا يتمثل بهم» — people turned into told stories. أحاديث and أخبار are joined in one phrase.
- 99:4 تُحَدِّثُ — ح د ث B006 — «الحدث الإبداء» — telling as bringing into the open.
- 99:4 تُحَدِّثُ — ح د ث B001 — «الحدوث كون الشيء بعد أن لم يكن» — speech that newly comes to be: the ground that never spoke now speaks.
- 99:5 أَوْحَىٰ — و ح ي B001 — «أصل يدل على إلقاء علم في إخفاء إلى غيرك»؛ «إعلام في خفاء» — the hidden first step of the message.
- 99:5 أَوْحَىٰ — و ح ي B002 — «الوحي الإشارة»؛ «رمز أو أشار» — the message given by sign.
- 99:5 أَوْحَىٰ — و ح ي B005 — «وحاة الرعد وهو صوته الممدود الخفي» — a long, faint sound, like thunder's.
- 99:5 أَوْحَىٰ — و ح ي B003 — «وحى في الحجر إذا كتب فيه»؛ «وحى وأوحى أي كتب» — writing in stone: the ground as a surface written on, which then reads out what was inscribed.
- 99:5 أَوْحَىٰ — و ح ي B004 — «أوحى الله إلى أنبيائه»؛ «إما إلهاما وإما رؤيا وإما أن ينزل عليه كتابا» — the divine message. Here its recipient is the earth.
- 99:5 رَبَّكَ — ر ب ب B001 — «رب كل شيء مالكه»؛ «يكون الرب: السيد المطاع» — the owner whose command the earth obeys.

Passages:
- 84:5 وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ — the earth at the Hour (scene opens 84:1). The earth listens to her Lord, after casting out what was in her (84:4).
- 41:11 فَقَالَ لَهَا وَلِلْأَرْضِ ٱئْتِيَا طَوْعًا أَوْ كَرْهًا قَالَتَآ أَتَيْنَا طَآئِعِينَ — creation. God speaks to the earth and the earth answers.
- 41:12 وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا — creation. وحي to a part of creation that is not human.
- 16:68 وَأَوْحَىٰ رَبُّكَ إِلَى ٱلنَّحْلِ — God's signs. The surah's own pair, رَبُّكَ أَوْحَىٰ, addressed to a creature.
- 41:21 وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ — the people of the Fire and their skins (scene opens 41:19). Mute things given speech to testify; the question-and-answer form of 99:3–4.
- 41:20 شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم بِمَا كَانُوا۟ يَعْمَلُونَ — the same scene.
- 36:65 ٱلْيَوْمَ نَخْتِمُ عَلَىٰٓ أَفْوَٰهِهِمْ وَتُكَلِّمُنَآ أَيْدِيهِمْ وَتَشْهَدُ أَرْجُلُهُم — God on the Day (scene opens 36:59).
- 24:24 يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ — about the slanderers.
- 45:29 هَٰذَا كِتَٰبُنَا يَنطِقُ عَلَيْكُم بِٱلْحَقِّ إِنَّا كُنَّا نَسْتَنسِخُ مَا كُنتُمْ تَعْمَلُونَ — God to the kneeling nations (scene opens 45:28). A written record that speaks the deeds.
- 18:49 وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةً وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا — the criminals before the record (scene opens 18:47 with the bare earth). The same question form as مَا لَهَا, asked of a record that holds everything.
- 75:13 يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ — man at the Hour (scene opens 75:7). يَوْمَئِذٍ, ٱلْإِنسَٰنُ and being told his deeds.
- 89:23 يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ — after the earth is pounded (scene opens 89:21).
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌ — closing the scene of the turned-out graves (100:9–10). رَبّ, يَوْمَئِذٍ and the خبر root together.
- 9:105 وَقُلِ ٱعْمَلُوا۟ فَسَيَرَى ٱللَّهُ عَمَلَكُمْ … فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ — the Prophet told to address the believers. Deeds seen and then reported.
- 23:44 وَجَعَلْنَٰهُمْ أَحَادِيثَ — God about destroyed nations. The phrase the dictionary cites for B004.
- From memory (tafsir): the exegetes give two readings of تُحَدِّثُ, actual speech created in the earth and speech by its state. The ق و ل B014 phrase attests the second way of "saying".

### 5. Inside drawn out, laid open and shown

Across the surah, contents move from hidden to seen. The earth's loads are underground; its news is the inside of things (المخبر as against المنظر); the people's deeds are invisible until they "are made to see" them (لِّيُرَوْا۟). Each one finally sees his own speck (يَرَهُۥ). The dictionary supplies the concrete operations: drawing out as one draws up hidden water, spreading things out in the sun, holding up a mirror so someone can look, polishing a blade until it shines. Even شَرًّا has a branch "to bring out and display". The viewer is in the chain too: الإنسان is named for being visible, the pupil holds a small human image, and آنس is seeing and hearing.

- 99:2 أَثْقَالَهَا — ث ق ل B002 — «أثقال الأرض كنوزها» — treasures: things buried out of sight.
- 99:2 وَأَخْرَجَتِ — خ ر ج B002 — «الاستخراج كالاستنباط»؛ «اخترجت الرجل واستخرجته سواء» — drawing out what is hidden, like drawing up buried water.
- 99:4 أَخْبَارَهَا — خ ب ر B001 — «المخبر خلاف المنظر»؛ «الخبرة المعرفة ببواطن الأمر» — the inside as against the outside.
- 99:4 تُحَدِّثُ — ح د ث B006 — «الحدث الإبداء» — bringing into view.
- 99:4 تُحَدِّثُ — ح د ث B007 — «محادثة السيف جلاؤه»؛ «أحدث الرجل سيفه وحادثه إذا جلاه وحادثوا هذه القلوب أي اجلوها بالمواعظ» — polishing off the dull layer so the surface shows.
- 99:8 شَرًّا — ش ر ر B008 — «أشررت الشيء إذا أبرزته وأظهرته»؛ «أشررت الشيء أظهرته» — to bring out and display. The word for evil carries the surah's movement into view.
- 99:8 شَرًّا — ش ر ر B002 — «الشر بسطك الشيء في الشمس»؛ «شررت اللحم والثوب وأشررته إذا بسطته ليجف» — spreading things out in full sun.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B004 — «ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر» — fine light spreading over everything.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B004 — «ذر البقل إذا طلع من الأرض» — a sprout coming up out of the earth. The phrase joins ذرّ and الأرض.
- 99:6 لِّيُرَوْا۟ — ر ء ي B012 — «أريته الشيء فرآه»؛ «رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها» — causing to see, and holding up a mirror so someone can look. This is the causative sense of the passive لِّيُرَوْا۟: the deeds are held up to their doers.
- 99:6 لِّيُرَوْا۟ — ر ء ي B006 — «المرآة ما يرى فيه صورة الأشياء» — the mirror that shows the form of things.
- 99:6, 99:7, 99:8 لِّيُرَوْا۟ / يَرَهُۥ — ر ء ي B001 — «الرؤية إدراك المرئي بالحاسة»؛ «نظر وإبصار بعين أو بصيرة» — seeing with the eye or with inner sight.
- 99:6 لِّيُرَوْا۟ — ر ء ي B005 — «وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس» — doing a deed so that people see it. Its reversal is the surah's: each doer is made to see his own deed.
- 99:3 ٱلْإِنسَٰنُ — ء ن س B001 — «الإنس خلاف الجن وسموا لظهورهم» — humans named for being visible.
- 99:3 ٱلْإِنسَٰنُ — ء ن س B005 — «إنسان العين المثال الذي يرى في السواد» — the small figure seen in the pupil, the viewer's eye.
- 99:3 ٱلْإِنسَٰنُ — ء ن س B002 — «آنست الشيء إذا رأيته وآنسته إذا سمعته» — perceiving by sight and by hearing. Man sees the quake, hears the news and sees the deeds.
- 99:6 يَصْدُرُ — ص د ر B001 — «الصدر للإنسان والجمع صدور» — the chest, the body's container of what is hidden. This is a homonym branch of the verb, heard against 100:10.

Passages:
- 100:9–10 إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ ۝ وَحُصِّلَ مَا فِى ٱلصُّدُورِ — warning to ungrateful man (scene opens 100:6). The ground's contents and the chests' contents brought out together.
- 86:9 يَوْمَ تُبْلَى ٱلسَّرَآئِرُ — the Day when secrets are tested.
- 69:18 يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌ — the Day (scene opens 69:13).
- 17:13 وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًا يَلْقَىٰهُ مَنشُورًا — God on each person's record. أخرج used of bringing the record into the open, spread out.
- 81:10 وَإِذَا ٱلصُّحُفُ نُشِرَتْ — the Hour (scene opens 81:1).
- 18:49 وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًا — the criminals before the record (scene opens 18:47).
- 3:30 يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًا وَمَا عَمِلَتْ مِن سُوٓءٍ — God's warning. Good and evil deeds set before their doer.
- 53:39–40 وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ ۝ وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ — the scriptures of Moses and Abraham (scene opens 53:36). The effort is seen, with the passive of the surah's verb.
- 78:40 يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ — God's warning. Each looks at what his hands sent ahead.
- 50:22 فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌ — address to man at the resurrection (scene opens 50:19). The covering removed, sight sharpened.
- 82:5 عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ — the Hour (scene opens 82:1, with the graves turned out in 82:4).
- 4:142 يُرَآءُونَ ٱلنَّاسَ — the hypocrites. The deed done to be seen, the reversed member above.
- 18:47 وَتَرَى ٱلْأَرْضَ بَارِزَةً — the bare earth in full view.
- 39:69 وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ — the Day. The earth lit by its Lord's light as the record is laid down, the open field of the sun image.

### 6. Leaving the watering place in separate parties

يَصْدُرُ is the herdsman's verb for leaving water after drinking. The dictionary uses the surah's own sentence to explain أَشْتَاتًا ("يصدر الناس أشتاتا أي متفرقين"). The scene is concrete: a crowd that came together to one place, as herds come down to water (ورد), now turns back (صدر) and moves off by separate parties along a worn track, each toward the sight of its deeds. The ayah's two ends are the starting point (the gathering) and the destination (لِّيُرَوْا۟ أَعْمَٰلَهُمْ).

- 99:6 يَصْدُرُ — ص د ر B003 — «الصدر الانصراف عن الورد وعن كل أمر»؛ «صدرت الإبل عن الماء»؛ «صدر عن الماء وصدر عن البلاد» — turning away from the watering place after coming to it.
- 99:6 يَصْدُرُ — ص د ر B003 — «طريق صادر يصدر بأهله عن الماء» — the road that carries its people back from the water.
- 99:6 يَصْدُرُ — ص د ر B003 — «أصدرته فصدر أي رجعته فرجع» — sending back, returning.
- 99:6 يَصْدُرُ — ص د ر B006 — «الصدر الطائفة من الشيء» — a portion or party of something. The crowd leaves as parties.
- 99:6 أَشْتَاتًا — ش ت ت B001 — «يصدر الناس أشتاتا أي متفرقين» — the dictionary quotes the ayah, joining يصدر, الناس and أشتاتا.
- 99:6 أَشْتَاتًا — ش ت ت B001 — «أصل يدل على تفرق وتزيل»؛ «الشت تفريق الشعب» — a tribe or group splitting apart.
- 99:6 ٱلنَّاسُ — ء ن س B001 — «الإنس جماعة الناس» — the crowd as a whole before it divides.
- 99:6 أَعْمَٰلَهُمْ, 99:7–8 يَعْمَلْ — ع م ل B011 [fixed expression] — «طريق معمل أي لحب مسلوك» — a worn, travelled track.
- 99:6 أَعْمَٰلَهُمْ, 99:7–8 يَعْمَلْ — ع م ل B012 [fixed expression] — «المسافرون إذا مشوا على أرجلهم يسمون بني العمل» — travellers on foot.
- 99:2 وَأَخْرَجَتِ — خ ر ج B001 — «الخروج نقيض الدخول» — going out, the first move of the crowd once the ground releases it.

Passages:
- 28:23 وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةً مِّنَ ٱلنَّاسِ يَسْقُونَ … قَالَتَا لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ — Moses at the water of Madyan (scene opens 28:22). ورد and صدر at a well, with "a community of people" watering. This is the verb's home scene.
- 11:98 يَقْدُمُ قَوْمَهُۥ يَوْمَ ٱلْقِيَٰمَةِ فَأَوْرَدَهُمُ ٱلنَّارَ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ — Pharaoh leading his people. The watering image turned to the Fire.
- 19:86 وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًا — God on the Day. The criminals driven like herds to a watering place.
- 54:7 خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ — those called by the caller (scene opens 54:6).
- 70:43 يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ — the Day. A crowd hurrying toward a marked point.
- 36:51 فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ — the blast and rising.
- 6:94 وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ — God to the dead on arrival. Each comes alone.
- 30:14 يَوْمَئِذٍۢ يَتَفَرَّقُونَ; 30:43 يَوْمَئِذٍۢ يَصَّدَّعُونَ — the Hour. يَوْمَئِذٍ with the crowd splitting.
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ — the Striking Hour (scene opens 101:1). ٱلنَّاسُ scattered.
- From memory (tafsir): the exegetes give two directions for يَصْدُرُ, out from the graves to the place of standing, or away from the standing to their final places. On the second reading the standing is the "water" the crowd came down to.

### 7. Sprinkled apart into the smallest units

ذرّ is to sprinkle grain, salt or medicine apart. A ذرة is the smallest ant, one of a scattered swarm. أشتات is a group broken into pieces. Together they make one image: a mass is sprinkled into units, and the unit shrinks from parties of people to the speck that is weighed in 99:7–8.

- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B002 — «ذررت الحب والدواء والملح أذره ذرا فرقته» — sprinkling grains apart, the operation.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B001 — «الذر صغار النمل الواحدة ذرة»؛ «الذر جمع ذرة وهي أصغر النمل» — the smallest ant, one of a swarm.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B003 — «الذريرة معروفة» — a known fine powder.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B004 — «ضوء لطيف منتشر» — light spread fine.
- 99:6 أَشْتَاتًا — ش ت ت B001 — «الشت تفريق الشعب»؛ «شت يشت شتاتا وهو التفرق» — the group broken apart, the scattered units at human scale.

Passages:
- 54:7 كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ — those called out of the graves (scene opens 54:6). People as a spread swarm.
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ — the Striking Hour (scene opens 101:1).
- 56:4–6 إِذَا رُجَّتِ ٱلْأَرْضُ رَجًّا … فَكَانَتْ هَبَآءً مُّنۢبَثًّا — the Event (scene opens 56:1). The shaken ground and mountains turned to scattered dust.
- 27:18 قَالَتْ نَمْلَةٌ يَٰٓأَيُّهَا ٱلنَّمْلُ ٱدْخُلُوا۟ مَسَٰكِنَكُمْ — an ant warning the ants as Solomon's army comes. A swarm of the smallest creatures, one of whom speaks.
- 7:172 وَإِذْ أَخَذَ رَبُّكَ مِنۢ بَنِىٓ ءَادَمَ مِن ظُهُورِهِمْ ذُرِّيَّتَهُمْ وَأَشْهَدَهُمْ عَلَىٰٓ أَنفُسِهِمْ — the covenant of Adam's progeny. From memory: the traditional account of this covenant pictures the progeny drawn out like ذرّ, and the root of ذُرِّيَّة is disputed among ذ ر ر, ذ ر أ and ذ ر و.

### 8. Weight: from the earth's loads to the weight of a speck

The root ث ق ل stands in the surah twice in different forms: أَثْقَالَهَا, the earth's huge loads, and مِثْقَالَ, a known unit of weight. The movement runs from the largest weight to the smallest. al-Mufradat states this transfer in so many words: heaviness "belongs originally to bodies, then to meanings". The loads also mean sins, and a reduplicated ش ر ر form means "weights". The scale is set: a speck's weight of good, a speck's weight of evil, and each is seen.

- 99:2 أَثْقَالَهَا — ث ق ل B001 — «الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني»؛ «ضد الخفة» — heavy against light, first in bodies, then in meanings.
- 99:2 أَثْقَالَهَا — ث ق ل B002 — «أثقال الأرض كنوزها وأجساد بني آدم» — the largest weight, the earth's contents.
- 99:2 أَثْقَالَهَا — ث ق ل B003 — «الأثقال الآثام»؛ «أثقالهم آثامهم التي تثقلهم وتثبطهم» — loads as sins that weigh their bearers down.
- 99:7, 99:8 مِثْقَالَ — ث ق ل B004 — «المثقال وزن معلوم قدره ومثقال الشيء ميزانه من مثله»؛ «المثقال ما يوزن به وهو اسم لكل سنج» — a known weight, a counterweight on the scale.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B001 — «الذر جمع ذرة وهي أصغر النمل» — the smallest thing put in the pan.
- 99:7 خَيْرًا — خ ي ر B001 — «الخير ما يرغب فيه الكل وضده الشر» — one content of the pans.
- 99:8 شَرًّا — ش ر ر B001 — «الشر الذي يرغب عنه الكل»؛ «الشر نقيض الخير» — the opposite content. al-Mufradat defines the pair in mirror wording (يرغب فيه / يرغب عنه).
- 99:8 شَرًّا — ش ر ر B006 — «الشراشر الأثقال الواحدة شرشرة» (sihah) — the reduplicated form of the root of شَرًّا names "weights". The phrase joins ش ر ر and أثقال.
- 99:6 أَعْمَٰلَهُمْ, 99:7–8 يَعْمَلْ — ع م ل B001 — «كل فعل يكون من الحيوان بقصد»؛ «الأعمال الصالحة والسيئة» — what is weighed: intended acts, good and bad.

Passages:
- 4:40 إِنَّ ٱللَّهَ لَا يَظْلِمُ مِثْقَالَ ذَرَّةٍۢ — God on His justice. The surah's exact phrase.
- 10:61 وَلَا تَعْمَلُونَ مِنْ عَمَلٍ إِلَّا كُنَّا عَلَيْكُمْ شُهُودًا … وَمَا يَعْزُبُ عَن رَّبِّكَ مِن مِّثْقَالِ ذَرَّةٍۢ فِى ٱلْأَرْضِ — God to the Prophet. عمل, رَبّ, مِثْقَالِ ذَرَّةٍ and ٱلْأَرْض in one ayah.
- 34:3 لَا يَعْزُبُ عَنْهُ مِثْقَالُ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ — the Prophet answering deniers of the Hour.
- 31:16 يَٰبُنَىَّ إِنَّهَآ إِن تَكُ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ فَتَكُن فِى صَخْرَةٍ أَوْ … فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ — Luqman to his son (scene opens 31:13). A tiny weight hidden in rock or earth and brought out, closing on خَبِير.
- 21:47 وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ … وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا — God on the Day's scales.
- 7:8–9 وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ … وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ — God on the Day. يَوْمَئِذٍ with heavy and light scales.
- 101:6–9 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ … وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ ۝ فَأُمُّهُۥ هَاوِيَةٌ — the Striking Hour (scene opens 101:1), the surah right after this one.
- 29:13 وَلَيَحْمِلُنَّ أَثْقَالَهُمْ وَأَثْقَالًا مَّعَ أَثْقَالِهِمْ — the leaders of disbelief who offered to carry others' sins (scene opens 29:12). أثقال as sins.
- 35:18 وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌ — God's warning. A heavily laden soul.
- 53:38 أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ — the scriptures of Moses and Abraham (scene opens 53:36).
- 16:7 وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ — the cattle as God's favour. أثقال as baggage.

### 9. Settling the account: payment out, coin weighed, wage paid

A second group of senses gives the same weighing a market and treasury setting. خراج is "wealth the giver brings out", the year's fixed payment, the yield; تخارج is partners settling their shares; مثقال is the coin-weight (give him his weight); عمالة is the wage for work; خير is wealth. The earth "brings out" what it owes, each deed is weighed like coin, and the doer receives what his work earned. Nothing short-weighted is left.

- 99:2 وَأَخْرَجَتِ — خ ر ج B003 — «الخراج والخرج الإتاوة لأنه مال يخرجه المعطي»؛ «الخرج والخراج ما يخرج من المال في السنة بقدر معلوم»؛ «الخراج الغلة»؛ «الخرج بإزاء الدخل» — a set payment brought out by the payer; income against outgo.
- 99:2 وَأَخْرَجَتِ — خ ر ج B012 — «يتخارج الشريكان وأهل الميراث»؛ «لا بأس أن يتخارجا يعني العين والدين» — partners or heirs settling their shares, cash and debt.
- 99:7, 99:8 مِثْقَالَ — ث ق ل B004 — «أعطه ثقله أي وزنه»؛ «المثقال وزن معلوم قدره» — giving someone the full weight. In the Turkish gloss of this branch: a dinar not short of weight.
- 99:6 أَعْمَٰلَهُمْ, 99:7–8 يَعْمَلْ — ع م ل B004 — «العمالة أجر ما عمل»؛ «العمالة بالضم رزق العامل» — the wage of work.
- 99:6 أَعْمَٰلَهُمْ, 99:7–8 يَعْمَلْ — ع م ل B005 — «عاملت الرجل أعامله معاملة في المبايعة وغيرها» — dealing with someone in trade.
- 99:7 خَيْرًا — خ ي ر B004 — «إن ترك خيرا أي مالا»؛ «ما كان مجموعا من المال من وجه محمود» — wealth gathered in a praiseworthy way.

Passages:
- 23:72 أَمْ تَسْـَٔلُهُمْ خَرْجًا فَخَرَاجُ رَبِّكَ خَيْرٌ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ — God to the Prophet about the deniers. خرج, خراج, رَبّ and خَيْر in one ayah.
- 18:94 فَهَلْ نَجْعَلُ لَكَ خَرْجًا — a people to Dhu'l-Qarnayn. خرج as payment.
- 3:185 وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ — God's address. Wages paid in full.
- 46:19 وَلِكُلٍّۢ دَرَجَٰتٌۭ مِّمَّا عَمِلُوا۟ وَلِيُوَفِّيَهُمْ أَعْمَٰلَهُمْ وَهُمْ لَا يُظْلَمُونَ — the two kinds of offspring (scene opens 46:15). The deeds themselves paid back in full.
- 3:25 وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ — God about the People of the Book.
- 2:110 وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ — God to the believers. Good sent ahead as a deposit that is found again.
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ — ungrateful man (scene opens 100:6). خير as wealth, just before the graves are turned out.
- 2:180 إِن تَرَكَ خَيْرًا — the bequest law. The phrase al-Mufradat cites.

### 10. Soil, cloud and water bringing out growth

The Quran's standing comparison for resurrection is growth from the ground: rain falls, the soil stirs and swells, the plant is brought out, "so you will be brought out". The surah's words carry that whole sequence in their own branches. أرض is soft, fertile soil where plants root. خرج is the cloud's first rising and land that grows in patches. خبر is low soft ground that collects rain, and the farmer who shares in "what comes out of the earth". رب is the layered cloud named because it "rears the plants", and rearing by stages to completion. ذرّ is the sprout coming up out of the earth. زلزل names clear water that goes down easily. The ground of 99:1–2 is a field, and أَخْرَجَتِ is its yield.

- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B002 — «أرض أريضة لينة طيبة»؛ «تأرض النبت تمكن على الأرض فكثر»؛ «تأرض النبت إذا أمكن أن يجز» — soft, good soil; plants taking hold and becoming ready to cut.
- 99:2 وَأَخْرَجَتِ — خ ر ج B007 — «أرض مخرجة نبتها في مكان دون مكان» — land whose growth comes out in some places and not others. The phrase joins خرج and أرض.
- 99:2 وَأَخْرَجَتِ — خ ر ج B003 — «الخراج الغلة» — the yield.
- 99:2 وَأَخْرَجَتِ — خ ر ج B005 [fixed expression] — «الخروج السحاب أول ما يبدأ»؛ «أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن» — the cloud first forming.
- 99:4 أَخْبَارَهَا — خ ب ر B002 — «الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء»؛ «الخبار أرض رخوة» — low soft ground where rainwater collects.
- 99:4 أَخْبَارَهَا — خ ب ر B003 — «الخبير الأكار»؛ «المزارعة ببعض ما يخرج من الأرض» (sihah) — the ploughman, and sharecropping on part of "what comes out of the earth". The phrase joins خبر, خرج and الأرض.
- 99:4 أَخْبَارَهَا — خ ب ر B005 — «الخبير النبات اللين» — tender growth.
- 99:5 رَبَّكَ — ر ب ب B008 — «الرباب: السحاب، سمي بذلك لأنه يرب النبات»؛ «الربابة: السحابة التي قد ركب بعضها بعضا» — layered cloud named for rearing plants.
- 99:5 رَبَّكَ — ر ب ب B007 — «أربت السحابة: دامت» — the cloud staying in place.
- 99:5 رَبَّكَ — ر ب ب B013 — «الربب وهو الماء الكثير سمي بذلك لاجتماعه» — abundant gathered water.
- 99:5 رَبَّكَ — ر ب ب B002 — «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» — bringing a thing up stage by stage to completion.
- 99:5 رَبَّكَ — ر ب ب B012 — «الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف» — tender plants that stay green in summer.
- 99:7, 99:8 ذَرَّةٍ — ذ ر ر B004 — «ذر البقل إذا طلع من الأرض» — the sprout breaking the surface.
- 99:1 زِلْزَالَهَا — ز ل ز ل B003 [fixed expression] — «ماء زلال وزلازل إذا كان ينساغ بلا كلفة من صفائه» — clear, easily drunk water.

Passages:
- 7:57 حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًا ثِقَالًا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ — God's signs. Heavy (ثِقَال) clouds, bringing out fruit, bringing out the dead: three of the surah's images in one ayah.
- 22:5 وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ — God to people in doubt about resurrection. The ground shakes (ٱهْتَزَّتْ) and swells before it grows.
- 41:39 تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰ — God's signs.
- 35:9 فَتُثِيرُ سَحَابًا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا كَذَٰلِكَ ٱلنُّشُورُ — God's signs.
- 50:9–11 وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا … وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًا كَذَٰلِكَ ٱلْخُرُوجُ — God answering deniers of resurrection (scene opens 50:2–3).
- 43:11 فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًا كَذَٰلِكَ تُخْرَجُونَ — God's signs.
- 30:19 يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ … وَيُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَكَذَٰلِكَ تُخْرَجُونَ — God's praise.
- 6:99 فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًا نُّخْرِجُ مِنْهُ حَبًّا — God's signs. أخرج repeated over growth.
- 79:31 أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا — the spreading of the earth (scene opens 79:27). The earth's own contents brought out.
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ — praise of the Lord (scene opens 87:1 سَبِّحِ ٱسْمَ رَبِّكَ).
- 71:17–18 وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًا ۝ ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًا — Noah to his people (speech opens 71:10). Humans as the earth's growth.

### 11. Spark and speck

شَرًّا in 99:8 belongs to the root that names the spark flying from a fire. ذَرَّةٍ is the tiny scattered particle. Heard together in "مِثْقَالَ ذَرَّةٍ شَرًّا", the speck of evil is a spark: the smallest fragment thrown off from fire.

- 99:8 شَرًّا — ش ر ر B003 — «الشرر ما تطاير من النار الواحدة شررة»؛ «شرار النار ما تطاير منها» — sparks flying from fire.
- 99:8 ذَرَّةٍ — ذ ر ر B001 — «الذر جمع ذرة وهي أصغر النمل» — the smallest unit.
- 99:8 ذَرَّةٍ — ذ ر ر B002 — «ذررت الحب والدواء والملح أذره ذرا فرقته» — scattered particles, as sparks scatter.

Passages:
- 77:32 إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ — the Fire described to the deniers (scene opens 77:29). The spark (شَرَر) as large as a castle, the reverse scale of the speck.

### 12. Clinging heavily to the ground, and being set moving at once

The dictionary uses the earth word for clinging to the ground and lingering, and calls that clinging "heaviness toward the earth". ثقل in turn cites the Quran's "اثاقلتم إلى الأرض". The surah's earth held its loads heavily, and they lie low. A swift command (وحي is speed) reverses this: the ground gives up what clung to it and people go out without lingering. The dictionary's own example of the reversal is "فقام عجلان وما تأرضا".

- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B006 — «تأرض فلان إذا لزم الأرض»؛ «التأرض أيضا التثاقل إلى الأرض» (sihah) — sticking to the ground, heaviness toward it. The phrase joins أرض and ثقل.
- 99:1, 99:2 ٱلْأَرْضُ — ء ر ض B006 — «فقام عجلان وما تأرضا أي ما تلبث» — rising quickly without lingering on the ground, the reversal.
- 99:2, 99:7, 99:8 أَثْقَالَهَا / مِثْقَالَ — ث ق ل B006 — «اثاقلتم إلى الأرض» (mufradat)؛ «المثقل البطيء والتثاقل من التباطؤ» — heaviness as slowness and sinking to the ground. The phrase joins ثقل and الأرض.
- 99:2 وَأَخْرَجَتِ — خ ر ج B001 — «خرج خروجا برز من مقره أو حاله» — leaving the place one stayed in.
- 99:5 أَوْحَىٰ — و ح ي B006 — «الوحي السريع»؛ «أمر وحي»؛ «توح يا هذا أي أسرع» — speed, a swift command.
- 99:6 يَصْدُرُ — ص د ر B003 — «الصدر الانصراف عن الورد وعن كل أمر» — moving off from where one stopped.

Passages:
- 9:38 مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ — God to the believers who held back from marching. The phrase al-Mufradat cites, with the question form مَا لَكُمْ.
- 7:176 وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ — the man given signs who sank to the earth (scene opens 7:175).
- 50:44 يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا — the gathering. The ground splits and they come out fast.
- 70:43 يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا — the Day.
- 54:50 وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌۭ كَلَمْحٍۭ بِٱلْبَصَرِ — God's command, as quick as a glance.

### 13. Two lots as far apart as black from white

أَشْتَاتًا is not only scattering. The same root gives "شتان ما بينهما", the great distance between two. خير and شر are defined as each other's opposites, and خرج names a surface of two colours, black and white, or land growing in some places and not others. The crowd of 99:6 sorts into the two ayat that end the surah: one lot with good, one with evil, each seeing its own.

- 99:6 أَشْتَاتًا — ش ت ت B003 — «شتان ما بينهما»؛ «تباعد ما بينهما»؛ «ارتفاع الالتئام بينهما» — how far apart the two are; their joining undone.
- 99:6 أَشْتَاتًا — ش ت ت B001 — «الشت تفريق الشعب» — the group split.
- 99:7 خَيْرًا / 99:8 شَرًّا — خ ي ر B001 / ش ر ر B001 — «الخير ضد الشر»؛ «الشر نقيض الخير» — the two opposite lots.
- 99:2 وَأَخْرَجَتِ — خ ر ج B007 — «الخرج لونان بين سواد وبياض»؛ «الأخرج لون سواده أكثر من بياضه» — a two-coloured surface.
- 99:2 وَأَخْرَجَتِ — خ ر ج B007 — «أرض مخرجة نبتها في مكان دون مكان» — ground patched with growth and bare places.

Passages:
- 3:106–107 يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌ … وَأَمَّا ٱلَّذِينَ ٱبْيَضَّتْ وُجُوهُهُمْ — God's warning. Black and white faces on the Day.
- 80:38–40 وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌ … وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌ — the Deafening Blast (scene opens 80:33).
- 30:14–16 يَوْمَئِذٍۢ يَتَفَرَّقُونَ ۝ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ … وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ — the Hour (scene opens 30:12). The crowd splits into two, sorted by deeds.
- 42:7 يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ — God to the Prophet.
- 56:7 وَكُنتُمْ أَزْوَٰجًا ثَلَٰثَةً — the Event (scene opens 56:1).
- 92:4 إِنَّ سَعْيَكُمْ لَشَتَّىٰ — oath and answer (scene opens 92:1). The same root for the divergence of deeds.
- 101:6–9 heavy and light scales, two outcomes (scene opens 101:1).
- 69:19, 69:25 فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ … وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ — the Day (scene opens 69:13). Two lots by the record.

## Interactions

- 1 ground casting out × 2 heavy body delivering — shared أَثْقَالَهَا and أَخْرَجَتِ. «أثقال الأرض كنوزها وأجساد بني آدم» and «أثقلت المرأة … ثقل حملها في بطنها». 22:1–2 stages the quake and the delivery together.
- 1 ground casting out × 3 shaking into bodies — shared زُلْزِلَتِ and ٱلْأَرْضُ. The earth word names the shiver («الأرض الرعدة») and the shaking-out («الأرْص النفضة والرعدة»).
- 1 ground casting out × 8 weight — the same root, from أَثْقَالَ to مِثْقَالَ. «الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني».
- 1 ground casting out × 10 growth — shared أَخْرَجَتِ and ٱلْأَرْضُ. 7:57 «سَحَابًا ثِقَالًا … فَأَخْرَجْنَا بِهِۦ … كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ».
- 2 delivering × 10 growth — 22:5 stages womb and earth in one ayah: «ثُمَّ نُخْرِجُكُمْ طِفْلًا … ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ».
- 2 delivering × 5 shown — ر ء ي B010 «أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها». What is carried inside becomes seen.
- 1 ground casting out × 4 earth speaking — 84:4–5 «وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ ۝ وَأَذِنَتْ لِرَبِّهَا». Casting out and listening to the Lord, in the same order as 99:2 and 99:5.
- 3 shaking into bodies × 4 earth speaking — 99:3's question is the shaken human's outburst. 75:10 «يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ»; 36:52 «مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا».
- 4 earth speaking × 5 shown — ح د ث B006 «الحدث الإبداء»; خ ب ر «المخبر خلاف المنظر». 17:13 «وَنُخْرِجُ لَهُۥ … كِتَٰبًا يَلْقَىٰهُ مَنشُورًا» joins bringing out with the record. 18:49 «مَالِ هَٰذَا ٱلْكِتَٰبِ … وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًا» pairs the مَا لَهَا question with deeds found present.
- 4 earth speaking (inside) — ح د ث B003 «كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث» joins الإنسان, حديث and وحي, the three steps of 99:3–5. ح د ث B004 «فجعلناهم أحاديث أي أخبارا» joins تُحَدِّثُ and أَخْبَارَهَا.
- 4 earth speaking × 8 weight — ث ق ل B005 «قولا ثقيلا يعني عظم قدره وجلالة خطره وقول له وزن» joins قول and ثقل. 73:5 «إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًا ثَقِيلًا» (God to the Prophet) is a وحي called a heavy word.
- 4 earth speaking × 12 swift command — و ح ي B006 «أمر وحي». 54:50 «وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌۭ كَلَمْحٍۭ بِٱلْبَصَرِ».
- 1 ground casting out × 5 shown — 100:9–10 «بُعْثِرَ مَا فِى ٱلْقُبُورِ ۝ وَحُصِّلَ مَا فِى ٱلصُّدُورِ». The ground's contents and the chest's contents together; ص د ر B001 is the homonym of يَصْدُرُ. 18:47 «وَتَرَى ٱلْأَرْضَ بَارِزَةً».
- 5 shown × 8 weight — 31:16 «مِثْقَالَ حَبَّةٍ … فِى صَخْرَةٍ أَوْ … فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ … خَبِيرٌ»: a hidden tiny weight in the earth, brought out. 10:61 «مِّثْقَالِ ذَرَّةٍۢ فِى ٱلْأَرْضِ».
- 5 shown × 13 two lots — ش ر ر B008 «أشررت الشيء إذا أبرزته وأظهرته» and B001 «الشر نقيض الخير» are two branches of the one word شَرًّا. 3:30 sets both lots (مِنْ خَيْرٍ … مِن سُوٓءٍ) before their doer.
- 6 leaving the water × 7 sprinkled apart — shared أَشْتَاتًا. 54:7 «يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ»; 101:4 «ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ».
- 6 leaving the water × 12 set moving — shared يَصْدُرُ and أَخْرَجَتِ. «فقام عجلان وما تأرضا»; 50:44 and 70:43 «سِرَاعًا».
- 6 leaving the water × 13 two lots — shared أَشْتَاتًا. 30:14–16 «يَتَفَرَّقُونَ» then «فَأَمَّا … وَأَمَّا»; ش ت ت B003 «شتان ما بينهما».
- 6 leaving the water × 5 shown — the ayah's own purpose clause: يَصْدُرُ … لِّيُرَوْا۟ أَعْمَٰلَهُمْ. The route ends at the mirror (ر ء ي B012 «أمسكت له المرآة لينظر فيها»).
- 7 sprinkled apart × 8 weight — shared ذَرَّةٍ. It is the unit of scattering and the unit on the scale. 4:40 «مِثْقَالَ ذَرَّةٍ».
- 7 sprinkled apart × 11 spark — shared ذَرَّةٍ. Scattered particles and flying sparks («الشرر ما تطاير من النار»).
- 8 weight × 9 account — shared مِثْقَالَ. «المثقال وزن معلوم قدره»; «أعطه ثقله أي وزنه».
- 8 weight × 13 two lots — shared خَيْرًا and شَرًّا. 7:8–9 and 101:6–9 give heavy and light scales with two outcomes.
- 8 weight (inside) — ش ر ر B006 «الشراشر الأثقال الواحدة شرشرة» joins the root of شَرًّا with أثقال.
- 9 account × 1 ground casting out — shared أَخْرَجَتِ. «الخراج والخرج الإتاوة لأنه مال يخرجه المعطي»: the earth as payer bringing out what it owes.
- 9 account × 10 growth — «المزارعة ببعض ما يخرج من الأرض»; «الخراج الغلة».
- 9 account × 4 / 10 (رَبّ) — 23:72 «فَخَرَاجُ رَبِّكَ خَيْرٌ» joins خراج, رَبّ and خَيْر.
- 10 growth × 5 shown — ذ ر ر B004 «ذر البقل إذا طلع من الأرض»: the sprout breaking the surface into view.
- 10 growth × 3 shaking — 22:5 and 41:39 «ٱهْتَزَّتْ وَرَبَتْ»: the ground stirring before it grows.
- 12 set moving × 1 ground casting out — shared ٱلْأَرْضُ and أَثْقَالَهَا. «التأرض أيضا التثاقل إلى الأرض»; 9:38 «ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ».

## Ayat

### 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 1 ground casting out: زُلْزِلَتِ / زِلْزَالَهَا give the operation, ٱلْأَرْضُ the container. The dictionary defines the quake with this very pair («زلزلت الأرض زلزالا»). Scene: the ground is shaken with its own shaking and casts out the loads it held, its treasures and the bodies of Adam's children, so that what lay heavy inside lies outside.
- 2 heavy body delivering: ٱلْأَرْضُ is the heavy body; the quake is the throe before delivery (22:1–2). Scene: the earth, heavy as a woman heavy with child or a body swollen with matter, gives up what it carried, and the load is seen as it comes out.
- 3 shaking into bodies: the earth word itself means a shiver («الأرض الرعدة») and an involuntary jerking (B012); زِلْزَالَهَا also names the hardships of time [fixed expression]. Scene: the tremor passes from the ground into bodies and people, as a shiver, a seizure, the shaking of hardship and man's alarmed question.
- 10 growth: ٱلْأَرْضُ is soft fertile soil (B002); زِلْزَال also names clear water [fixed expression]. Scene: soil, cloud and water bring out growth from the ground; the Lord who rears plants by stages brings out the dead as He brings out the sprout.
- 12 set moving: ٱلْأَرْضُ is the ground things cling to («التأرض … التثاقل إلى الأرض»). Scene: what clung heavily to the ground, the earth's loads and those who sank toward it, is set moving at once by a swift command, and people go out without lingering.

### 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 1 ground casting out: أَخْرَجَتِ is the crossing out of the resting place; أَثْقَالَهَا is «كنوزها وأجساد بني آدم». Scene: the ground is shaken and casts out the loads it held, so what lay heavy inside lies outside.
- 2 heavy body delivering: أَثْقَالَهَا is the weight of pregnancy («أثقلت المرأة»); أَخْرَجَتِ is delivery and the swelling that "comes out of itself" («يخرج من ذاته»). Scene: the earth, heavy as a body with child, gives up what it carried, and the load is seen as it comes out.
- 5 shown: أَثْقَالَهَا are buried treasures; أَخْرَجَتِ is drawing out the hidden («الاستخراج كالاستنباط»). Scene: what was inside (treasures, bodies, news, deeds) is drawn out, laid open as in the sun, held up as to a mirror, and seen by the one who did it.
- 8 weight: أَثْقَالَهَا is the largest weight, and also sins («الأثقال الآثام»). Scene: weight runs from the earth's huge loads to the weight of a speck; good and evil are weighed down to that smallest amount, and each sees it.
- 9 account: أَخْرَجَتِ as «مال يخرجه المعطي», the yield (الغلة), the settling of shares (تخارج). Scene: an account is settled: what is owed comes out, is weighed like coin, and each work receives its wage.
- 10 growth: أَخْرَجَتِ is the yield of the soil («أرض مخرجة»; «الخراج الغلة»); the cloud's first rising [fixed expression]. Scene: soil, cloud and water bring out growth, and the dead are brought out like the sprout.
- 12 set moving: أَثْقَالَهَا is what sank and clung; أَخْرَجَتِ is its release. Scene: what clung heavily to the ground is set moving at once by a swift command, and people go out without lingering.
- 13 two lots: أَخْرَجَتِ names a two-coloured surface and land growing in patches (B007). Scene: the going-out splits people into two lots as far apart as good from evil, like a surface of black and white.
- 6 leaving the water: أَخْرَجَتِ is the first going out of the crowd. Scene: people leave the place they came to, as herds leave water, in separate parties along a worn track, each toward the sight of its deeds.

### 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 3 shaking into bodies: قَالَ … مَا لَهَا is the shaken human's outburst (cf. 2:214, 75:10). Scene: the tremor passes from the ground into bodies and people, ending in man's alarmed question.
- 4 earth speaking: قَالَ is the first step of the dialogue, a seeking of news («الاستخبار السؤال عن الخبر»). The same root names a thing "saying" by its state («امتلأ الحوض وقال قطني») and inspiration called saying (B017). Scene: man asks; the earth, given a message in secret by her Lord, answers by telling its news, the inside of what happened on it, as a record now given voice.
- 5 shown: ٱلْإِنسَٰنُ is the visible being («سموا لظهورهم»), the figure in the pupil («إنسان العين»), the one who sees and hears («آنست الشيء إذا رأيته وآنسته إذا سمعته»). Scene: what was inside is drawn out, laid open, held up as to a mirror, and seen by the one who did it.
- 6 leaving the water: ٱلْإِنسَٰنُ, of the root of ٱلنَّاسُ in 99:6, is the whole crowd before it divides («الإنس جماعة الناس»). Scene: people leave the gathering as herds leave water, in separate parties, toward the sight of their deeds.

### 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 4 earth speaking: تُحَدِّثُ is speech that reaches man "by hearing or by وحي" (B003) and speech newly come to be (B001). أَخْبَارَهَا is the answer to the question, the inside of things («المخبر خلاف المنظر»); «فجعلناهم أحاديث أي أخبارا» joins the two words. Scene: man asks; the earth, given a message in secret by her Lord, answers by telling its news as a record now given voice.
- 5 shown: تُحَدِّثُ is «الحدث الإبداء», bringing into view, and polishing a blade bright (B007). أَخْبَارَهَا is the hidden inside told. Scene: what was inside is drawn out, laid open as in the sun, held up as to a mirror, and seen by its doer.
- 3 shaking into bodies: تُحَدِّثُ belongs to the root of «الحادثة النازلة العارضة», the calamity that descends. Scene: the tremor passes from ground to bodies and people as a shiver, a seizure, a calamity and a cry.
- 10 growth: أَخْبَارَهَا is of the root of low soft ground that gathers rain (B002), the ploughman and sharecropping on «ما يخرج من الأرض» (B003), and tender plants (B005). Scene: soil, cloud and water bring out growth from the ground, and the dead are brought out like the sprout.

### 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 4 earth speaking: أَوْحَىٰ is the hidden message («إلقاء علم في إخفاء»), by sign, by faint long sound, by writing in stone («وحى في الحجر إذا كتب فيه»). رَبَّكَ is the owner obeyed («السيد المطاع»). Scene: man asks; the earth, given a message in secret by her Lord, answers by telling its news (cf. 84:5 «وَأَذِنَتْ لِرَبِّهَا»).
- 10 growth: رَبَّكَ is of the root of the layered cloud «سمي بذلك لأنه يرب النبات», the cloud that stays, abundant water, rearing «حالا فحالا إلى حد التمام», and tender evergreen plants. Scene: soil, cloud and water bring out growth from the ground; the Lord who rears plants by stages brings out the dead as He brings out the sprout.
- 12 set moving: أَوْحَىٰ is speed, «أمر وحي». Scene: what clung heavily to the ground is set moving at once by a swift command, and people go out without lingering.
- 9 account: رَبَّكَ joins 23:72 «فَخَرَاجُ رَبِّكَ خَيْرٌ». Scene: an account is settled: what is owed comes out, is weighed like coin, and each work receives its wage.

### 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 6 leaving the water: يَصْدُرُ is leaving the watering place («الصدر الانصراف عن الورد»; «طريق صادر يصدر بأهله عن الماء»), in parties (B006). أَشْتَاتًا is glossed by this ayah itself in the dictionary. أَعْمَٰلَهُمْ is of the root of a worn track and travellers on foot [fixed expressions]. Scene: people leave the place they came to, as herds leave water, in separate parties along a worn track, each toward the sight of its deeds.
- 7 sprinkled apart: أَشْتَاتًا is the group broken into pieces («الشت تفريق الشعب»). Scene: the gathered mass is sprinkled apart like grain or powder into the smallest units: scattered parties, the smallest ants, the speck.
- 13 two lots: أَشْتَاتًا is also «شتان ما بينهما». Scene: the going-out splits people into two lots as far apart as good from evil, like a surface of black and white.
- 5 shown: لِّيُرَوْا۟ is the causative passive, made to see, as when one holds up a mirror («أمسكت له المرآة لينظر فيها»). It reverses deeds done "so that people see them" («ليراه الناس»). يَصْدُرُ is heard against the chest (الصدر) that holds the hidden (100:10). Scene: what was inside is drawn out, laid open, held up as to a mirror, and seen by the one who did it.
- 8 weight: أَعْمَٰلَهُمْ is what is weighed, «الأعمال الصالحة والسيئة». Scene: weight runs from the earth's huge loads to the weight of a speck; good and evil are weighed down to that, and each sees it.
- 9 account: أَعْمَٰلَهُمْ is of the root of wage («العمالة أجر ما عمل») and trade dealing (معاملة). Scene: an account is settled, and each work receives its wage.
- 12 set moving: يَصْدُرُ is moving off from where one stopped. Scene: what clung to the ground is set moving at once, and people go out without lingering.

### 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 8 weight: مِثْقَالَ is the known weight and counterweight («المثقال ما يوزن به»); ذَرَّةٍ is the smallest ant; خَيْرًا is «ما يرغب فيه الكل». Scene: weight runs from the earth's huge loads to the weight of a speck; good is weighed down to that, and its doer sees it.
- 7 sprinkled apart: ذَرَّةٍ is the sprinkled grain and the smallest ant of a swarm. Scene: the gathered mass is sprinkled apart into the smallest units, down to the speck.
- 5 shown: يَرَهُۥ is seeing with eye or inner sight; ذَرَّةٍ is of the root of fine spreading sunlight and the sprout coming up out of the earth. Scene: what was inside is drawn out, laid open as in the sun, held up as to a mirror, and seen by the one who did it.
- 9 account: مِثْقَالَ is the full coin-weight («أعطه ثقله أي وزنه»); يَعْمَلْ is work that earns a wage; خَيْرًا is wealth gathered in a praiseworthy way. Scene: an account is settled; the deed is weighed like coin and paid its wage.
- 13 two lots: خَيْرًا is the first of the two opposite lots. Scene: the going-out splits people into two lots as far apart as good from evil.
- 10 growth: ذَرَّةٍ is «ذر البقل إذا طلع من الأرض». Scene: soil, cloud and water bring out growth, and what was sown comes up into view.
- 1 ground casting out: خَيْرًا is of the root of a creature forced out of its burrow («فخرج من القاصعاء») [fixed expression]. Scene: the ground is shaken and casts out what it held.
- 2 heavy body delivering: يَرَهُۥ is of the root of a pregnancy showing «حتى يرى صدق حملها». Scene: the earth, heavy as a body with child, gives up what it carried, and the load is seen.

### 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
- 8 weight: شَرًّا is «الشر الذي يرغب عنه الكل», the mirror of خَيْرًا. Its root also gives «الشراشر الأثقال». Scene: weight runs from the earth's huge loads to the weight of a speck; evil is weighed down to that, and its doer sees it.
- 11 spark: شَرًّا is of the root of the spark («الشرر ما تطاير من النار»); ذَرَّةٍ is the tiny scattered particle. Scene: the speck of evil is a spark, a tiny fragment flying from fire, which the Fire throws as sparks like castles (77:32).
- 5 shown: شَرًّا also gives «أشررت الشيء إذا أبرزته وأظهرته» and spreading things in the sun («الشر بسطك الشيء في الشمس»); يَرَهُۥ closes the movement. Scene: what was inside is drawn out, laid open as in the sun, held up as to a mirror, and seen by the one who did it.
- 13 two lots: شَرًّا is «نقيض الخير», the second lot. Scene: the going-out splits people into two lots as far apart as good from evil, like a surface of black and white.
- 7 sprinkled apart: ذَرَّةٍ is the smallest scattered unit. Scene: the gathered mass is sprinkled apart into the smallest units, down to the speck.
- 9 account: مِثْقَالَ is the full weight, and يَعْمَلْ the work paid for. Scene: an account is settled, nothing short-weighted, and each work receives its due.

