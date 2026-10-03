Surah: 88. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (88:1 to 88:26), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s088/surah.r2/text.md =====
# Surah 88

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/out/s088/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. The covering that comes over: الغاشية, the garden's cover, the coverer
The surah opens with an event whose name means a cover laid over something. The covering image comes back three more times. The garden is ground hidden under trees, and its reward is hidden from sight now. The man who refuses (كفر) is "one who covers" the truth, as night covers things and a farmer covers seed with soil. The surah closes on العذاب, and the dictionary calls a غاشية "a punishment that wraps everyone" (عقوبة مجللة تعمهم). So the first and last nouns of the surah are joined by a phrase in the dictionary. Faces stand in the middle as the front that the cover falls on. The root of العذاب also gives the reverse picture: a man with no cover between himself and the sky.
- 88:1 ٱلْغَٰشِيَةِ — غ ش و B001 — "أصل صحيح يدل على تغطية شيء بشيء" (maqayis); "وغاشية السرج غطاؤه" (tahdhib): the basic act of laying one thing over another, and a real object, the saddle-cloth.
- 88:1 ٱلْغَٰشِيَةِ — غ ش و B002 — "الغاشية القيامة لأنها تغشى الخلق بإفزاعها" (maqayis); "غاشية من عذاب الله أي عقوبة مجللة تعمهم" (tahdhib); "الغاشية كل ما يغطي الشيء ونائبة تغشاهم وتجللهم وكناية عن القيامة" (mufradat): the Day as a terror that covers all creation, and a covering punishment. This phrase joins الغاشية with 88:24 العذاب.
- 88:1 ٱلْغَٰشِيَةِ — غ ش و B005 — "غشي على فلان إذا نابه ما غشي فهمه" (mufradat): the cover reaches inside and blacks out the mind (a swoon).
- 88:2/88:8 وُجُوهٌ — و ج ه B001 — "الوجه مستقبل كل شيء" (ayn;tahdhib): the exposed front that the cover comes down on.
- 88:10 جَنَّةٍ — ج ن ن B001 — "أصل الجن ستر الشيء عن الحاسة" (mufradat): the same act of covering, now as a hiding from the senses.
- 88:10 جَنَّةٍ — ج ن ن B003 — "كل بستان ذي شجر يستر بأشجاره الأرض" (mufradat): the garden is trees covering the ground, a cover that gives life.
- 88:10 جَنَّةٍ — ج ن ن B004 — "الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم" (maqayis): the reward is the thing kept covered now.
- 88:10 جَنَّةٍ — ج ن ن B002 — "جنان الليل سواده وستره الأشياء" (maqayis): night as a cover.
- 88:23 وَكَفَرَ — ك ف ر B001 — "كل شيء غطى شيئا فقد كفره" (ayn;sihah;tahdhib): the refuser's verb is itself a verb of covering.
- 88:23 وَكَفَرَ — ك ف ر B003 — "الكفر ضد الإيمان سمى لأنه تغطية الحق" (maqayis): covering the truth.
- 88:23 وَكَفَرَ — ك ف ر B002 — "الليل كافر لأنه ستر بظلمته" (tahdhib): night as the one who covers.
- 88:23 وَكَفَرَ — ك ف ر B008 — "الكافر الزارع لأنه يغطي البذر بالتراب" (sihah): the farmer covering seed. This sets the refuser's cover against the garden's cover of trees.
- 88:24 ٱلْعَذَابَ — ع ذ ب B005 — "العذاب العقوبة وقد عذبته تعذيبا" (sihah): the closing word, which the tahdhib phrase under غ ش و B002 calls a covering punishment.
- 88:24 ٱلْعَذَابَ — ع ذ ب B004 — "العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب" (maqayis;tahdhib): the reverse image, a man left with nothing between him and the sky (88:18).
- Quran 12:107 — God, speaking to the Prophet at the close of Joseph's story, about those who feel safe: "أن تأتيهم غاشية من عذاب الله". In one ayah it has أتى, غاشية and عذاب, the words of 88:1 and 88:24.
- Quran 44:10–11 — God tells the Prophet to wait for the day the sky brings smoke: "يوم تأتي السماء بدخان مبين" (opens the scene), then "يغشى الناس هذا عذاب أليم".
- Quran 29:55 — God, of the deniers: "يوم يغشاهم العذاب من فوقهم ومن تحت أرجلهم".
- Quran 14:49–50 — the criminals on the Day, in chains (14:49 opens the scene): "وتغشى وجوههم النار". Covering, faces and fire together.
- Quran 10:27 — those who earned evil: "كأنما أغشيت وجوههم قطعا من الليل مظلما". Faces covered with night.
- Quran 2:6–7 — God, of those who refuse (كفروا): "وعلى أبصارهم غشاوة ولهم عذاب عظيم". Refusal, a cover over the eyes, and punishment.
- Quran 92:1 — oath: "والليل إذا يغشى". Quran 6:76 — Abraham: "فلما جن عليه الليل". Night as cover, under both roots.
- Quran 57:20 — God's parable of this life: "كمثل غيث أعجب الكفار نباته". Here كفار is read as farmers who cover seed (from memory, a known reading).

### 2. The face as ground: dry, dusty, lowered ground against soft, rain-fed ground
The dictionary uses خاشع of ground: low, dusty, dried out because no rain has fallen. ناعمة means "turned soft and supple", and the earth root describes good soil as "أريضة لينة". Both words rest on the same quality, لين (softness). So the two groups of faces are two kinds of ground: one that has had no rain and is given scalding water, and one that sits in a garden with a running spring. The reminder at the end turns the eye to the earth itself, spread out.
- 88:2 وُجُوهٌ — و ج ه B001 — "الوجه مستقبل كل شيء" (ayn;tahdhib): the surface that faces outward, as ground faces the sky.
- 88:2 خَٰشِعَةٌ — خ ش ع B002 — "بلدة خاشعة مغبرة" (maqayis;sihah); "إذا يبست الأرض ولم تمطر قيل قد خشعت" and "أرض خاشعة هامدة" (tahdhib); "قف خاشع لاطئ بالأرض" (maqayis): ground that is dusty, dried out, rainless and hugging the earth.
- 88:5 تُسْقَىٰ — س ق ي B001 — "السقي والسقيا أن يعطيه ما يشرب" (mufradat): the dry face is watered, but from a scalding spring.
- 88:8 نَّاعِمَةٌ — ن ع م B002 — "نعم الشيء صار ناعما لينا" (sihah); "نعمة العيش حسنه وغضارته" (tahdhib): soft, supple and fresh, the opposite of the dried face.
- 88:8 نَّاعِمَةٌ — ن ع م B009 — "النعامى ريح الجنوب لأنها أبل الرياح وأرطبها" (sihah): the root names the moistest, softest wind.
- 88:12 عَيْنٌ جَارِيَةٌ — ع ي ن B006 — "العين الجارية النابعة من عيون الماء" (maqayis): the soft face's ground has a running spring.
- 88:20 ٱلْأَرْضِ — ء ر ض B002 — "أرض أريضة لينة طيبة" (maqayis;ayn); "تأرض النبت تمكن على الأرض فكثر" (mufradat): soft, good, well-grown ground. It shares لين with ناعمة.
- Quran 41:39 — God naming His signs: "ترى الأرض خاشعة فإذا أنزلنا عليها الماء اهتزت وربت". The ground that is خاشعة is brought back by water.
- Quran 22:5 — God to people in doubt about being raised: "وترى الأرض هامدة فإذا أنزلنا عليها الماء اهتزت وربت". هامدة is the word the dictionary uses for أرض خاشعة.
- Quran 80:40–41 — the Day of the Deafening Blast (80:33 opens): "ووجوه يومئذ عليها غبرة ترهقها قترة". Dust on faces, matching "بلدة خاشعة مغبرة".
- Quran 83:24 — the righteous: "تعرف في وجوههم نضرة النعيم".

### 3. What the face shows: humbled, worn, grieving against soft, content, glad
The faces carry inner states. One group is humbled and worn out by grief. The dictionary links خشوع to ضراعة, the root of their food ضريع, in a single phrase. The other group is soft, content with its effort, and seated on couches that the dictionary names after joy (سرور). The same root also gives the lines of the forehead (أسارير).
- 88:2 خَٰشِعَةٌ — خ ش ع B001 — "الخاشع المستكين" (maqayis;jamhara); "الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح" (mufradat): a humbled bearing, and a dictionary phrase joining خشع (88:2) to ضرع, the root of ضريع (88:6).
- 88:3 نَّاصِبَةٌ — ن ص ب B004 — "النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي" (maqayis); "الحزن إذا أثر فيه" (jamhara): worn out from standing and toiling, and grief showing on the face.
- 88:6 ضَرِيعٍ — ض ر ع B002 — "ضرع الرجل ضراعة إذا ذل" (maqayis;sihah;mufradat); "تخشعوا وتذللوا وخضعوا" (tahdhib): the food's root means humbling. The dictionary explains it with خشوع.
- 88:6 ضَرِيعٍ — ض ر ع B003 — "لضارع الجسم أي نحيف ضعيف" (sihah): the humbled body gone thin.
- 88:8 نَّاعِمَةٌ — ن ع م B001 — "أصل واحد يدل على ترفه وطيب عيش وصلاح" (maqayis): ease and a good life.
- 88:8 نَّاعِمَةٌ — ن ع م B013 — "نعمة العين قرتها" (sihah) [fixed expression]: a sight that cools the eye.
- 88:9 رَاضِيَةٌ — ر ض و B001 — "أصل واحد يدل على خلاف السخط" (maqayis): content, the opposite of resentment.
- 88:13 سُرُرٌ — س ر ر B010 — "السرور أمر خال من الحزن" (maqayis): joy free of grief, the opposite of the النصب of 88:3.
- 88:13 سُرُرٌ — س ر ر B011 — "السرير الذي يجلس عليه من السرور" (mufradat): the dictionary takes the couch's name from joy.
- 88:13 سُرُرٌ — س ر ر B009 — "أسرة الراحة وأسارير الجبهة" (mufradat): the lines of the forehead, the face again.
- Quran 75:22–25 — the Day: "وجوه يومئذ ناضرة إلى ربها ناظرة ووجوه يومئذ باسرة".
- Quran 80:38–41 — the Day of the Blast (80:33 opens): faces "مسفرة ضاحكة مستبشرة" against faces with dust.
- Quran 76:11 — God, of the righteous: "ولقاهم نضرة وسرورا".
- Quran 3:106 — "يوم تبيض وجوه وتسود وجوه".
- Quran 15:47–48 — the godfearing in gardens with springs: "على سرر متقابلين لا يمسهم فيها نصب". The نصب of 88:3 is removed there. Quran 35:35 — the people of the garden: "لا يمسنا فيها نصب ولا يمسنا فيها لغوب".
- Quran 89:27–28 — call to the soul at rest: "ارجعي إلى ربك راضية مرضية".

### 4. The gaze: eyes thrown to the ground, springs that are eyes, the call to look
On that day the humbled face throws its eyes to the ground. Both springs in the surah are named عين, the word for the eye, and running water is "visible to the eyes". The reminder then tells the listener where to look: at the camel, up at the sky, across at the mountains, down at the earth.
- 88:2 خَٰشِعَةٌ — خ ش ع B001 — "الخشوع رميك ببصرك إلى الأرض" (ayn); "خشع ببصره إذا غضه" (jamhara): eyes lowered, thrown to the ground.
- 88:5/88:12 عَيْنٍ — ع ي ن B001 — "العين الناظرة لكل ذي بصر" (maqayis;ayn): the spring's name is the seeing eye.
- 88:12 عَيْنٌ — ع ي ن B006 — "ماء معين أي ظاهر للعيون" (mufradat): water that lies open to sight.
- 88:17 يَنظُرُونَ — ن ظ ر B001 — "تأمل الشيء ومعاينته" (maqayis); "تقليب البصر والبصيرة لإدراك الشيء ورؤيته" (mufradat): the look asked for, by eye and by mind.
- 88:17 يَنظُرُونَ — ن ظ ر B012 — "ينظرون إليك وهم لا يبصرون" (mufradat) [fixed expression]: looking without seeing, the failure the question warns against.
- 88:18 ٱلسَّمَآءِ — س م و B004 — "السماء كل ما علاك فأظلك" (sihah): the object of the upward look, all that is above and shades you.
- 88:20 ٱلْأَرْضِ — ء ر ض B001 — "كل شيء يسفل ويقابل السماء" (maqayis): the object of the downward look, the opposite of the sky.
- Quran 42:45 — God, of wrongdoers brought before the fire: "خاشعين من الذل ينظرون من طرف خفي". خشع and نظر together.
- Quran 70:44; 68:43 — the Day: "خاشعة أبصارهم ترهقهم ذلة". Quran 79:9 — "أبصارها خاشعة".
- Quran 50:6 — God, of the deniers: "أفلم ينظروا إلى السماء فوقهم كيف بنيناها". The same question as 88:17–18.
- Quran 7:185 — "أولم ينظروا في ملكوت السماوات والأرض".
- Quran 30:50 — God to the Prophet: "فانظر إلى آثار رحمت الله كيف يحيي الأرض بعد موتها".
- Quran 83:23 — the righteous: "على الأرائك ينظرون". Looking, in the garden. Quran 75:23 — "إلى ربها ناظرة".

### 5. What reaches the ear: the report, hushed voices, the word not heard, the reminder
The surah begins with a report that reaches the listener (هل أتاك حديث). Under the word حديث the dictionary says a report is "every speech that reaches a person through hearing". On that day voices go quiet (خشع). In the garden no ugly word is heard. At the end the Prophet's task is to make the hearer remember.
- 88:1 أَتَىٰكَ — ء ت ي B001 — "الإتيان مجيء بسهولة" (mufradat): the report arrives.
- 88:1 حَدِيثُ — ح د ث B003 — "كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث" (mufradat): the report is defined by the ear.
- 88:1 حَدِيثُ — ح د ث B004 — "فجعلناهم أحاديث أي أخبارا يتمثل بهم" (mufradat): people who become a story told about others.
- 88:2 خَٰشِعَةٌ — خ ش ع B001 — "خشعت الأصوات أي سكنت" (ayn): on that day voices hush.
- 88:11 تَسْمَعُ — س م ع B001 — "إيناس الشيء بالأذن" (maqayis): catching sound with the ear.
- 88:11 تَسْمَعُ — س م ع B003 — "تارة عن الفهم وتارة عن الطاعة" (mufradat): hearing as understanding and obeying.
- 88:11 لَٰغِيَةً — ل غ و B002 — "لاغية كلمة قبيحة أو فاحشة" (ayn;tahdhib): the dictionary glosses the very word لاغية.
- 88:11 لَٰغِيَةً — ل غ و B003 — "اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا" (sihah): raw noise and barking, also absent from the garden.
- 88:21 فَذَكِّرْ — ذ ك ر B004 — "الذكر جري الشيء على لسانك" (ayn;tahdhib) [fixed expression]: speaking a thing out.
- 88:21 مُذَكِّرٌ — ذ ك ر B003 — "ذكرت الشيء خلاف نسيته" (maqayis;sihah): the hearer's remembering, the opposite of forgetting.
- Quran 20:108 — the Day of the Trumpet (20:102 opens): "وخشعت الأصوات للرحمن فلا تسمع إلا همسا". خشع and لا تسمع together, as in 88:2 and 88:11.
- Quran 19:62; 56:25–26; 78:35; 52:23 — the garden: "لا يسمعون فيها لغوا", "لا لغو فيها ولا تأثيم".
- Quran 20:9; 51:24; 79:15; 85:17 — the same opening, "هل أتاك حديث", each before a story.

### 6. Work, wage, effort and the count
Work done with intent earns a wage (عمالة) and a share (نصيب). The face in 88:3 works and wears itself out, and its only gain is fatigue. The face in 88:9 is content with its effort. Under the word لغو the dictionary speaks of "what is struck out of the count" (ما يلغى من الحساب), which joins 88:11 to 88:26. Whatever is void gets no place in the count, and the count belongs to God.
- 88:3 عَامِلَةٌ — ع م ل B001 — "كل فعل يكون من الحيوان بقصد" (mufradat): work done on purpose.
- 88:3 عَامِلَةٌ — ع م ل B004 — "العمالة أجر ما عمل" (maqayis): the wage that work is owed.
- 88:3 نَّاصِبَةٌ — ن ص ب B004 — "النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي" (maqayis): toil carried on until the body gives out.
- 88:3 نَّاصِبَةٌ — ن ص ب B005 — "النصيب الحظ من الشيء" (maqayis;sihah): the root also names a fixed share, which this face does not receive.
- 88:7 يُغْنِى — غ ن ي B002 — "الغناء بالفتح الكفاية ولا يغني أي لا يكفي" (maqayis): the return that does not suffice.
- 88:9 لِّسَعْيِهَا — س ع ي B002 — "كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب" (ayn): effort as earning.
- 88:9 رَاضِيَةٌ — ر ض و B001 — "ورضا العبد عن الله ورضا الله عن العبد" (mufradat): contentment between the one who strives and God.
- 88:11 لَٰغِيَةً — ل غ و B001 — "ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب" (ayn;tahdhib): what is void is struck from the count. This joins 88:11 with 88:26.
- 88:26 حِسَابَهُم — ح س ب B001 — "الحساب عدك الأشياء": counting things one by one.
- 88:26 حِسَابَهُم — ح س ب B003 — "عطاء حسابا أي كافيا": a gift given in full measure, the reverse of لا يغني.
- Quran 53:39–41 — scripture of Abraham and Moses: "وأن ليس للإنسان إلا ما سعى وأن سعيه سوف يرى ثم يجزاه الجزاء الأوفى".
- Quran 17:19 — "ومن أراد الآخرة وسعى لها سعيها ... كان سعيهم مشكورا". Quran 76:22 — "وكان سعيكم مشكورا".
- Quran 79:34–35 — "فإذا جاءت الطامة الكبرى يوم يتذكر الإنسان ما سعى". Quran 92:4 — "إن سعيكم لشتى".
- Quran 25:23 — God of the deniers' works: "وقدمنا إلى ما عملوا من عمل فجعلناه هباء منثورا". Quran 18:103–104 — "الذين ضل سعيهم في الحياة الدنيا".
- Quran 101:6–7 — the Striking Blow (101:1 opens): "فأما من ثقلت موازينه فهو في عيشة راضية".
- Quran 78:36 — "جزاء من ربك عطاء حسابا".
- Quran 31:23 — "إلينا مرجعهم فننبئهم بما عملوا".

### 7. Fire and the scalding drink
The face enters a fire heated to its full and drinks from a spring whose heat has peaked. One phrase in the dictionary under صلى names the one who suffers this as the كافر, joining 88:4 to 88:23. Under ح م ي the dictionary has "عين حمئة". The sun sets into such a spring in 18:86, and some readers there read "عين حامية", which joins 88:4 and 88:5. The root of نار, read the other way, gives the blossom of trees.
- 88:4 تَصْلَىٰ — ص ل ي B003 — "صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها" (ayn); "صلي الرجل نارا إذا أدخلته النار" (sihah) [fixed expression]: entering the fire and suffering its heat. The ayn phrase names the كافر of 88:23.
- 88:4 نَارًا — ن و ر B002 — "النار مؤنثة وهي من الواو؛ الجمع نور ونيران" (sihah): the burning fire.
- 88:4 نَارًا — ن و ر B004 — "النور نور الشجر؛ تنوير الشجرة إزهارها" (ayn): the root reversed, trees in blossom.
- 88:4 حَامِيَةً — ح م ي B001 — "الحامية الحارة" (ayn); "أحميت الحديد في النار فهو محمى" (sihah): heat like iron heated in fire.
- 88:5 تُسْقَىٰ — س ق ي B001 — "السقي والسقيا أن يعطيه ما يشرب" (mufradat): drink given to them.
- 88:5 عَيْنٍ — ح م ي B006 — "عين حمئة أي ذات حمأة" (ayn;mufradat): the dictionary itself pairs عين with this root.
- 88:5 ءَانِيَةٍ — ء ن ي B003 — "حميم آن قد انتهى حره وعين آنية" (maqayis;ayn); "بلغ إناه من شدة الحر" (mufradat): the dictionary gives the surah's own phrase عين آنية, water at the top of its heat.
- 88:23 كَفَرَ / 88:24 ٱلْعَذَابَ — joined to this scene by the ayn phrase under ص ل ي B003.
- Quran 101:11 — the Striking Blow (101:1 opens): "نار حامية". The same words as 88:4.
- Quran 87:12 — previous surah, the reminder (87:9 opens): "الذي يصلى النار الكبرى". Quran 111:3 — "سيصلى نارا ذات لهب". Quran 92:14–16 — "نارا تلظى لا يصلاها إلا الأشقى الذي كذب وتولى".
- Quran 55:43–44 — "هذه جهنم ... يطوفون بينها وبين حميم آن". The word آن again.
- Quran 47:15 — "وسقوا ماء حميما فقطع أمعاءهم". Quran 14:16–17 — "ويسقى من ماء صديد يتجرعه ولا يكاد يسيغه". Quran 6:70 — "لهم شراب من حميم وعذاب أليم بما كانوا يكفرون".
- Quran 18:29 — "وإن يستغيثوا يغاثوا بماء كالمهل يشوي الوجوه". Scalding water on faces.
- Quran 22:19–20 — "يصب من فوق رءوسهم الحميم". Quran 37:66–67; 78:24–25; 56:42.
- Quran 18:86 — Dhu'l-Qarnayn finds the sun setting "في عين حمئة". The reading "حامية" in this ayah comes from memory (Ibn ʿĀmir, Ḥamza, al-Kisāʾī, Shuʿba).

### 8. Two springs and the vessels
Each side has a spring. One is آنية (at its boiling point) and one is جارية (running), and the dictionary gives both pairings: "عين آنية" and "العين الجارية". The word آنية is also the plural of إناء, a vessel. In 76:15 it stands beside أكواب, the cups placed in 88:14. Under طعام the dictionary notes that "feeding reaches even water", which joins drink to the food of 88:6. The root of العذاب also names sweet water.
- 88:5 تُسْقَىٰ — س ق ي B001 — "السقي والسقيا أن يعطيه ما يشرب" (mufradat): drink handed to them.
- 88:5 عَيْنٍ ءَانِيَةٍ — ء ن ي B003 — "حميم آن قد انتهى حره وعين آنية" (maqayis;ayn): the scalding spring.
- 88:5 ءَانِيَةٍ — ء ن ي B004 — "الإناء معروف وجمعه آنية والأواني" (sihah): the same letters mean vessels.
- 88:12 عَيْنٌ جَارِيَةٌ — ع ي ن B006 — "العين الجارية النابعة من عيون الماء" (maqayis): the running spring, named in the surah's own words.
- 88:12 جَارِيَةٌ — ج ر ي B001 — "جرى الماء يجري جرية وجريا وجريانا" (maqayis;sihah;mufradat): water on the move.
- 88:14 أَكْوَابٌ — ك و ب B001 — "الكوب القدح لا عروة له" (maqayis;mufradat); B005 — "كاب يكوب إذا شرب بالكوب" (tahdhib): a cup without a handle, and drinking from it.
- 88:14 مَّوْضُوعَةٌ — و ض ع B001 — "وضعت الشيء أضعه وضعا وهو ضد رفعته" (tahdhib): cups set down, ready to hand.
- 88:4 حَامِيَةً — ح م ي B008 — "حميا الكأس سورتها وحرارتها" (mufradat): the heat and kick of a cup, the drink's other edge.
- 88:6 طَعَامٌ — ط ع م B001 — "أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء" (maqayis): drink counts under "feeding".
- 88:24 ٱلْعَذَابَ — ع ذ ب B001 — "عذب الماء عذوبة فهو عذب طيب" (maqayis;ayn;tahdhib): the closing root reversed, as sweet water.
- Quran 76:15 — the righteous rewarded (76:12 opens): "ويطاف عليهم بآنية من فضة وأكواب". آنية and أكواب together.
- Quran 55:44 against 55:50 — "حميم آن" against "فيهما عينان تجريان". The two springs of 88:5 and 88:12 in one surah.
- Quran 56:18 — "بأكواب وأباريق وكأس من معين". Quran 43:71 — "بصحاف من ذهب وأكواب". Quran 83:25 — "يسقون من رحيق مختوم".
- Quran 76:17–18 — "ويسقون فيها كأسا ... عينا فيها تسمى سلسبيلا".
- Quran 47:15 — a garden with rivers of water and milk, set against "وسقوا ماء حميما".

### 9. A pot over the fire: oven, roasting, the point of doneness
Read for their cooking senses, the surah's words describe a kitchen: an oven fired hot, meat roasted, a pot on its stand, the food reaching its point of doneness (إنى), and someone waiting for it. The dictionary joins آنية to طعام in one phrase ("انتظرنا إنى الطعام"). Quran 33:53 joins نظر, إنى and طعام.
- 88:3 نَّاصِبَةٌ — ن ص ب B001 — "نصبت للقطاة شركا ونصبت للقدر نصبا" (tahdhib): the iron stand set up for the pot.
- 88:4 تَصْلَىٰ — ص ل ي B004 — "صليت اللحم صليا شويته" (ayn;sihah;tahdhib); "الصلاء يقال للوقود وللشواء" (mufradat): fuel, and meat roasted.
- 88:4 حَامِيَةً — ح م ي B001 — "حمى النهار وحمي التنور أي اشتد حره" (sihah): the oven at full heat.
- 88:5 ءَانِيَةٍ — ء ن ي B003 — "انتظرنا إنى الطعام أي إدراكه" (maqayis;ayn): the food's point of doneness. This joins آنية to 88:6 طعام.
- 88:6 طَعَامٌ — ط ع م B001 — "الطعم ذوقه والطعام اسم جامع لكل ما يؤكل" (ayn): the food itself.
- 88:6 ضَرِيعٍ — ض ر ع B007 — "ضرعت القدر أي حان أن تدرك" (sihah) [fixed expression]: the pot about to be done.
- 88:6 طَعَامٌ — ط ع م B005 — "أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم" (sihah) [fixed expression]: ripening until it takes on flavour.
- 88:17 يَنظُرُونَ — ن ظ ر B002 — "النظر الانتظار" (sihah): waiting.
- Quran 33:53 — God telling the believers how to behave in the Prophet's houses: "إلى طعام غير ناظرين إناه". نظر, إنى and طعام together.
- Quran 44:43–46 — the tree of zaqqum is the food of the sinner: "كالمهل يغلي في البطون كغلي الحميم".
- Quran 4:56 — "كلما نضجت جلودهم بدلناهم جلودا غيرها" (text from memory): skin cooked through.

### 10. Food that does not fatten: dry thorn, leanness, want, hunger
The only food on offer is ضريع: dry shibriq, or a red plant with a bad smell. It neither fattens nor fills. Every word of 88:6–7 has its opposite inside the surah's roots. The same letters ضريع name a ewe with a big udder. The root's other senses are a thin body and poverty (ضراعة). يسمن means fat, the opposite of leanness. يغني means wealth and sufficiency. Hunger is defined as the pain of an empty stomach. Against all this, حساب carries the sense of "enough".
- 88:6 لَّيْسَ — ل ي س B001 — "ليس: كلمة نفي، وهو فعل ماض" (sihah): the flat denial that opens the ayah.
- 88:6 طَعَامٌ — ط ع م B004 — "رجل طاعم حسن الحال" (maqayis): a man well fed is a man doing well, and they are denied this.
- 88:6 ضَرِيعٍ — ض ر ع B005 — "الضريع يبيس الشبرق وهو نبت" (sihah); "الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس" (tahdhib); "قيل هو يبيس الشبرق وقيل نبات أحمر منتن الريح" (mufradat): the dried plant.
- 88:6 ضَرِيعٍ — ض ر ع B011 — "الضريع الشراب الرقيق" (tahdhib): the same word as a thin drink.
- 88:6 ضَرِيعٍ — ض ر ع B001 — "شاة ضريع وضريعة عظيمة الضرع" (maqayis;sihah;mufradat;tahdhib): the same word as a ewe with a big udder, the plenty this food lacks.
- 88:6 ضَرِيعٍ — ض ر ع B003 — "لضارع الجسم أي نحيف ضعيف" (sihah): the thin body this food produces.
- 88:6 ضَرِيعٍ — ض ر ع B002 — "مظهرين الضراعة وهي شدة الفقر إلى الشيء والحاجة إليه" (tahdhib): bitter want.
- 88:7 يُسْمِنُ — س م ن B001 — "السمن نقيض الهزال" (ayn;tahdhib;mufradat): fat, the opposite of leanness.
- 88:7 يُغْنِى — غ ن ي B001 — "عدم الحاجات وقلة الحاجات وكثرة القنيات" (mufradat); B002 — "الغناء بالفتح الكفاية ولا يغني أي لا يكفي" (maqayis): wealth, and enough.
- 88:7 جُوعٍ — ج و ع B001 — "الألم الذي ينال الحيوان من خلو المعدة من الطعام" (mufradat): hunger defined by طعام, the word of 88:6.
- 88:26 حِسَابَهُم — ح س ب B003 — "حسبك هذا أي كفاك": "enough" at the close.
- Quran 69:35–36 — the man given his book in his left hand (69:25 opens): "فليس له اليوم ها هنا حميم ولا طعام إلا من غسلين". The same structure as 88:6.
- Quran 44:43–46 and 37:62–67 — zaqqum, the food that fills bellies and is washed down with boiling water.
- Quran 73:13 — "وطعاما ذا غصة وعذابا أليما". Quran 77:31 — "لا ظليل ولا يغني من اللهب".
- Quran 106:4 — Quraysh reminded: "الذي أطعمهم من جوع". Quran 20:118–119 — God to Adam in the garden: "إن لك ألا تجوع فيها ولا تعرى". Quran 26:79 — Abraham: "والذي هو يطعمني ويسقين".
- From memory: camels graze shibriq while it is green and leave it alone once it is dry (ضريع).

### 11. The herd camel's body: fodder, fat, hump, work
The camel is named outright in 88:17, but its body runs through the surah's roots. The dictionary joins ناعمة to الإبل: the herd is called نعم "for the good and the ease in it". One phrase joins طعم, إبل and سمن at once. خشع names a camel's hump that has lost its fat and sunk. The root of تصلى names a plant called "camels' bread". عاملة's root names a hardy working she-camel. موضوعة's root names camels grazing salt-bush, and صف names sacrificial camels set in a line.
- 88:17 ٱلْإِبِلِ — ء ب ل B001 — "الإبل معروفة ورجل آبل ومال مؤبل" (maqayis): the herd as wealth.
- 88:17 ٱلْإِبِلِ — ء ب ل B002 — "أبلت الإبل والوحش اجتزأت بالرطب عن الماء" (sihah): the camel that gets by on green fodder in place of water.
- 88:8 نَّاعِمَةٌ — ن ع م B005 — "النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم" (maqayis): the dictionary joins ناعمة's root to الإبل.
- 88:2 خَٰشِعَةٌ — خ ش ع B004 — "خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه" (tahdhib) [fixed expression]: a worn-out camel's hump losing its fat and sinking.
- 88:3 عَامِلَةٌ — ع م ل B008 — "اليعملة الناقة النجيبة المطبوعة على العمل" (sihah): the she-camel bred for work.
- 88:3 عَامِلَةٌ — ع م ل B010 — "عوامل الدابة قوائمه" (tahdhib) [fixed expression]: an animal's legs as its "workers".
- 88:4 تَصْلَىٰ — ص ل ي B010 — "تسميها العرب خبزة الإبل" (ayn;tahdhib): the صليان plant, camels' bread.
- 88:6 ضَرِيعٍ — ض ر ع B005 — "الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس" (tahdhib): fodder gone dry.
- 88:6 طَعَامٌ / 88:7 يُسْمِنُ — ط ع م B007 — "المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن" (maqayis): one phrase joining طعم, إبل and سمن, a camel with fat in its marrow.
- 88:7 يُسْمِنُ — س م ن B001 — "السمن نقيض الهزال" (ayn;tahdhib;mufradat): a fat animal against a lean one.
- 88:14 مَّوْضُوعَةٌ — و ض ع B007 — "الواضعات الإبل تأكل الخلة" (maqayis); "إبل واضعة أي مقيمة في الحمض" (tahdhib): camels grazing and settled on salt-bush.
- 88:15 مَصْفُوفَةٌ — ص ف ف B001 — "البدن الصواف التي تصفف ثم تنحر" (ayn;tahdhib): sacrificial camels lined up.
- 88:17 خُلِقَتْ — خ ل ق B003 — "رجل خليق ومختلق أي تام الخلق معتدل" (sihah): a frame that is complete and balanced, which is what the look at the camel is asked to see.
- Quran 36:71–72 — "أولم يروا أنا خلقنا لهم مما عملت أيدينا أنعاما ... وذللناها لهم فمنها ركوبهم ومنها يأكلون". خلق, عمل and أنعام together.
- Quran 16:5–7 — "والأنعام خلقها لكم فيها دفء ومنافع ومنها تأكلون ... وتحمل أثقالكم".
- Quran 80:24–32 — "فلينظر الإنسان إلى طعامه ... متاعا لكم ولأنعامكم". Looking, food and the herd.
- Quran 22:36 — God on sacrificial camels: "فاذكروا اسم الله عليها صواف". صف and ذكر together.
- Quran 22:27 — God to Abraham: "يأتوك رجالا وعلى كل ضامر". The lean camel.
- Quran 16:80 — "ومن أصوافها وأوبارها وأشعارها أثاثا ومتاعا". Camel hair becomes furnishings.

### 12. Milk: udder, milk held back, a row of cups at one milking, ghee
Under these senses the camel's yield runs from 88:5 to 88:17. The dictionary joins ضرع and رفع in one phrase: a she-camel that holds her first milk back in her udder. صفوف is the she-camel that lines up cups (أقداح) of her milk, and the كوب of 88:14 is defined as a قدح. Milk ends as ghee, and the waterskin (سقاء) holds water and milk alike.
- 88:6 ضَرِيعٍ — ض ر ع B001 — "الضرع لكل ذات خف أو ظلف" (sihah); "أضرعت الشاة نزل لبنها قبيل النتاج" (sihah;mufradat): the udder, and milk let down before birth.
- 88:13 مَّرْفُوعَةٌ — ر ف ع B007 — "ناقة رافع إذا رفعت اللبأ في ضرعها" (maqayis;sihah) [fixed expression]: milk held back. This joins رفع to ضرع.
- 88:15 مَصْفُوفَةٌ — ص ف ف B002 — "ناقة صفوف للتي تصف أقداحا من لبنها" (sihah); "الصفوف الناقة التي تجمع بين محلبين في حلبة" (maqayis;tahdhib): a she-camel that fills a row of cups at one milking.
- 88:14 أَكْوَابٌ — ك و ب B001 — "الكوب القدح لا عروة له" (maqayis;mufradat): the cup is a قدح, the vessel in the صفوف phrase.
- 88:7 يُسْمِنُ — س م ن B002 — "السمن سلاء اللبن" (ayn;tahdhib): ghee rendered from milk.
- 88:5 تُسْقَىٰ — س ق ي B004 — "السقاء القربة للماء واللبن" (ayn;sihah;tahdhib): the skin for water and milk.
- 88:8 نَّاعِمَةٌ — ن ع م B005 — "النعم الإبل لما فيه من الخير والنعمة" (maqayis): the herd that gives this good.
- 88:17 ٱلْإِبِلِ — ء ب ل B001: the animal the milk comes from.
- Quran 16:66 — God: "وإن لكم في الأنعام لعبرة نسقيكم مما في بطونه ... لبنا خالصا سائغا للشاربين". An object lesson, drink and milk.
- Quran 23:21 — "وإن لكم في الأنعام لعبرة نسقيكم مما في بطونها" (text from memory).
- Quran 47:15 — "وأنهار من لبن لم يتغير طعمه", set against "وسقوا ماء حميما".

### 13. The camel's march and homecoming
The first and last ayat carry the camel's moving forelegs. أتو is the swing back of a she-camel's forelegs as she walks. أوب is the swing back of hands and legs in the march, and also travelling all day and stopping at night. In between come the day's easy pace with riders' song (نصب), an easy run (سعي), running (جري), and quick and easy gaits. The dictionary joins مرفوعة and موضوعة as opposite gaits. The camel lowers its neck to be mounted, and whoever comes back at nightfall is آئب.
- 88:1 أَتَىٰكَ — ء ت ي B009 — "ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير" (sihah) [fixed expression]: the swing back of the forelegs.
- 88:3 نَّاصِبَةٌ — ن ص ب B010 — "نصب القوم ساروا يومهم وهو سير لين" (sihah): a day's easy march.
- 88:3 نَّاصِبَةٌ — ن ص ب B009 — "غناء لهم يشبه الحداء إلا أنه أرق منه" (sihah): the riders' song, softer than the drivers' chant.
- 88:9 لِّسَعْيِهَا — س ع ي B001 — "السعي عدو ليس بشديد" (ayn): an easy run.
- 88:12 جَارِيَةٌ — ج ر ي B001 — "الخيل تجري والرياح تجري والشمس تجري جريا" (ayn;tahdhib): running.
- 88:13 مَّرْفُوعَةٌ — ر ف ع B003 — "مرفوع الناقة في سيرها خلاف الموضوع" (maqayis): a raised gait. This joins 88:13 and 88:14 as opposite paces.
- 88:14 مَّوْضُوعَةٌ — و ض ع B003 — "وضع البعير وغيره أي أسرع في سيره" (sihah); B013 — "اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه" (tahdhib): another pace, and the neck lowered for mounting.
- 88:17 ٱلْإِبِلِ: the animal on the march.
- 88:25 إِيَابَهُمْ — ء و ب B003 — "الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل" (sihah): the swinging legs and the full day's march.
- 88:25 إِيَابَهُمْ — ء و ب B006 — "كل راجع مع الليل فهو آئب" (jamhara); B001 — "آب الرجل يؤوب إيابا إذا رجع إلى مستقره والمآب المرجع" (jamhara): coming home at nightfall to where one belongs.
- Quran 22:27 — God to Abraham: "وأذن في الناس بالحج يأتوك رجالا وعلى كل ضامر يأتين من كل فج عميق". Coming, on lean camels.
- Quran 16:7 — "وتحمل أثقالكم إلى بلد لم تكونوا بالغيه إلا بشق الأنفس" (cattle).
- From memory (al-Zamakhsharī and others): 88:17–20 traces what a rider sees around him, the camel under him, the sky above, the mountains around and the earth below.

### 14. Coming, turning away, coming back
The report comes. The Overwhelmer comes, and the dictionary defines غشيت with أتيت, joining two words of 88:1. The man who refuses turns his back. التولية can mean turning toward as well as turning away. Everyone comes back to Us (إياب, "back to where one belongs"), and the account follows.
- 88:1 أَتَىٰكَ — ء ت ي B001 — "الإتيان مجيء بسهولة" (mufradat); B011 — "الإتيان يقال في الخير وفي الشر" (mufradat); "أتى على فلان أتو أي موت أو بلاء أصابه" (tahdhib) [fixed expression]: a coming, sometimes a coming of disaster.
- 88:1 ٱلْغَٰشِيَةِ — غ ش و B003 — "غشيت موضع كذا أتيته" (mufradat); "غشيه غشيانا أي جاءه" (sihah): غشي defined by أتى, both words of 88:1.
- 88:2 وُجُوهٌ — و ج ه B002 — "الوجهة كل موضع استقبلته" (maqayis): the direction a face is turned.
- 88:23 تَوَلَّىٰ — و ل ي B007 — "ولى الرجل أي أدبر" (ayn); "إذا عدي بعن اقتضى معنى الإعراض وترك قربه" (mufradat) [fixed expression]: turning one's back.
- 88:23 تَوَلَّىٰ — و ل ي B006 — "التولية تكون إقبالا" (tahdhib): the root reversed, turning toward.
- 88:25 إِيَابَهُمْ — ء و ب B001 — "آب الغائب يؤوب أوبا أي رجع والمآب المرجع" (ayn): the absent one coming back.
- 88:25 إِيَابَهُمْ — ء و ب B002 — "الأواب كالتواب وهو الراجع إلى الله تعالى" (mufradat): turning back to God.
- 88:25 إِيَابَهُمْ — ء و ب B005 — "التأويب التسبيح في قوله يا جبال أوبي معه والطير" (maqayis): a dictionary phrase joining أوب with جبال (88:19).
- 88:26 حِسَابَهُم: what waits at the point of return.
- Quran 12:107 — "أن تأتيهم غاشية من عذاب الله أو تأتيهم الساعة بغتة".
- Quran 20:48 — Moses and Aaron to Pharaoh: "إنا قد أوحي إلينا أن العذاب على من كذب وتولى". إلينا, العذاب and تولى together.
- Quran 92:15–16 — "لا يصلاها إلا الأشقى الذي كذب وتولى".
- Quran 96:8 — "إن إلى ربك الرجعى". Quran 50:43 — "وإلينا المصير". Quran 31:23–24 — "إلينا مرجعهم ... ثم نضطرهم إلى عذاب غليظ".
- Quran 78:21–22 — "إن جهنم كانت مرصادا للطاغين مآبا". Quran 78:39 — "فمن شاء اتخذ إلى ربه مآبا". Quran 38:25 — "وحسن مآب".
- Quran 89:28 — "ارجعي إلى ربك راضية مرضية".
- Quran 34:10 — God to the mountains with David: "يا جبال أوبي معه والطير".
- Quran 13:40 — "فإنما عليك البلاغ وعلينا الحساب".

### 15. The furnished chamber and the furnished world
88:13–16 furnish a room: couches raised, cups set down, cushions in a row, carpets spread. 88:18–20 furnish the world with the same actions. The sky is raised, with the same verb as the couches, and the dictionary calls it a house's roof. The mountains are set up, and the dictionary defines نصب through وضع, the verb of the cups; it also calls mountains the earth's pegs. The earth is spread flat, and the dictionary calls a flat stretch of land "as if in a single row" (صف, the cushions' word). Its root also names a thick carpet (إراض), and بث is used of spread rugs and of creatures spread over the earth. The world becomes a tent: raised roof, pegs, a spread floor, and a tent pole (مسطح).
- 88:13 سُرُرٌ — س ر ر B011 — "السرير وجمعه سرر وأسرة" (maqayis); "سرير الرأس مستقره" (maqayis): the couch as a place of rest.
- 88:13 مَّرْفُوعَةٌ — ر ف ع B001 — "الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها" (mufradat): raising what was set down. One phrase holds both رفع and موضوع.
- 88:13 مَّرْفُوعَةٌ — ر ف ع B004 — "الرفع تقريب الشيء" (maqayis;sihah): brought within reach.
- 88:14 مَّوْضُوعَةٌ — و ض ع B001 — "وضعت الشيء أضعه وضعا وهو ضد رفعته" (tahdhib): set down, the opposite of raised.
- 88:15 مَصْفُوفَةٌ — ص ف ف B001 — "الصف أن تجعل الشيء على خط مستو" (mufradat): set along a straight line.
- 88:15/88:20 — ص ف ف B005 — "الصفصف المستوي من الأرض كأنه على صف واحد" (mufradat): the row-word used of level ground. This joins 88:15 to 88:20.
- 88:16 مَبْثُوثَةٌ — ب ث ث B001 — "بثت البسط" (tahdhib); "خلق الخلق وبثهم في الأرض" (maqayis): rugs spread out, and one phrase joining بث, خلق (88:17) and الأرض (88:20).
- 88:18 ٱلسَّمَآءِ — س م و B004 — "السماء سقف البيت وكل عال مطل سماء" (maqayis): the sky as a house's roof.
- 88:18 رُفِعَتْ — ر ف ع B001 — "في البناء إذا طولته" (mufradat): building upward.
- 88:19 نُصِبَتْ — ن ص ب B001 — "نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر" (mufradat): setting up defined as setting down so that it stands out. This joins 88:19 to 88:14.
- 88:19 ٱلْجِبَالِ — ج ب ل B001 — "اسم لكل وتد من أوتاد الأرض إذا عظم وطال" (ayn;tahdhib): mountains as the earth's tent-pegs.
- 88:20 سُطِحَتْ — س ط ح B001 — "سطح الله الأرض سطحا بسطها" (sihah); "السطح ظهر البيت إذا كان مستويا" (tahdhib): the earth spread as a flat floor or roof.
- 88:20 سُطِحَتْ — س ط ح B003 — "المسطح عمود الخيمة الذي يجعل به لها سطحا" (mufradat): the tent pole that gives the tent its flat surface.
- 88:20 ٱلْأَرْضِ — ء ر ض B005 — "الإراض بساط ضخم من وبر أو صوف" (maqayis): the earth root as a thick carpet, beside the زرابي of 88:16.
- Quran 55:7 and 55:10 — God listing His gifts: "والسماء رفعها ووضع الميزان ... والأرض وضعها للأنام". رفع and وضع side by side, as in 88:13–14 and 88:18–20.
- Quran 52:20 — "متكئين على سرر مصفوفة". Couches and the row-word together. Quran 56:34 — "وفرش مرفوعة".
- Quran 78:6–7 — "ألم نجعل الأرض مهادا والجبال أوتادا". Quran 21:32 — "وجعلنا السماء سقفا محفوظا". Quran 52:5 — "والسقف المرفوع".
- Quran 79:27–32 — "أم السماء بناها رفع سمكها فسواها ... والأرض بعد ذلك دحاها ... والجبال أرساها".
- Quran 71:19 — "والله جعل لكم الأرض بساطا". Quran 51:48; 2:22; 43:10; 50:7.
- Quran 31:10 — "وألقى في الأرض رواسي أن تميد بكم وبث فيها من كل دابة".
- Quran 101:4 — "يوم يكون الناس كالفراش المبثوث". The reverse picture: on the Day people, not rugs, are scattered.

### 16. Four acts of making: measuring, raising, setting upright, levelling
The four passive verbs of 88:17–20 are a craftsman's moves. خلق is measuring a hide before cutting it for a waterskin, which joins it to س ق ي, the root of 88:5. Its other senses are smoothing and levelling. رفع is building upward. نصب is setting something upright and even. سطح is spreading a place level. Three of the four definitions turn on evenness (استواء / تسوية).
- 88:17 خُلِقَتْ — خ ل ق B001 — "خلقت الأديم للسقاء إذا قدرته" (maqayis); "الخلق أصله: التقدير المستقيم" (mufradat): measuring the hide for a waterskin, and right measure.
- 88:17 خُلِقَتْ — خ ل ق B008 — "اخلولق الرسم أي استوى بالأرض" (sihah); "صخرة خلقاء ملساء" (jamhara): made smooth and even with the ground.
- 88:18 رُفِعَتْ — ر ف ع B001 — "الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها" (mufradat): lifting from its resting place.
- 88:19 نُصِبَتْ — ن ص ب B001 — "أصل صحيح يدل على إقامة شيء وإهداف في استواء" (maqayis): setting upright, standing even.
- 88:20 سُطِحَتْ — س ط ح B001 — "سطحت المكان جعلته في التسوية كسطح" (mufradat): making a place as level as a flat roof.
- Quran 87:2 — previous surah: "الذي خلق فسوى". Quran 82:7 — "الذي خلقك فسواك فعدلك".
- Quran 79:28 — "رفع سمكها فسواها".
- Quran 36:38 — "ذلك تقدير العزيز العليم". Measure.
- Quran 13:2 — "الله الذي رفع السماوات بغير عمد ترونها" (text from memory).

### 17. Pressed low and raised high
On that day one group of faces is pressed down like low ground. The other sits in a garden that is high, on couches that are raised. The dictionary sets رفعة (being raised) against ذلة (abasement), and شريف (honoured) against وضيع (lowly). The sky is high and the earth is defined as whatever is low and faces it. The surah ends on "the greatest" punishment. The root of عالية also names arrogant self-exaltation, and that of الأكبر self-importance.
- 88:2 خَٰشِعَةٌ — خ ش ع B001 — "أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه" (maqayis); B002 — "قف خاشع لاطئ بالأرض" (maqayis): head bowed, pressed to the ground.
- 88:6 ضَرِيعٍ — ض ر ع B002 — "ضرع الرجل ضراعة إذا ذل" (maqayis;sihah;mufradat): abasement.
- 88:10 عَالِيَةٍ — ع ل و B001 — "أصل واحد يدل على السمو والارتفاع" (maqayis); B002 — "العلاء فالرفعة" (maqayis;ayn): height and high standing.
- 88:10 عَالِيَةٍ — ع ل و B003 — "العلو فالعظمة والتجبر" (maqayis;ayn): the root reversed, haughtiness.
- 88:13 مَّرْفُوعَةٌ — ر ف ع B002 — "الرفعة نقيض الذلة" (tahdhib): raised, the opposite of abasement.
- 88:14 مَّوْضُوعَةٌ — و ض ع B005 — "رجل وضيع ضد الشريف والتواضع التذلل" (tahdhib): low standing, sitting beside the raised couches.
- 88:18 ٱلسَّمَآءِ — س م و B001 — "أصل يدل على العلو؛ سموت إذا علوت" (maqayis): height.
- 88:20 ٱلْأَرْضِ — ء ر ض B001 — "كل شيء يسفل ويقابل السماء" (maqayis): whatever lies low.
- 88:24 ٱلْأَكْبَرَ — ك ب ر B001 — "أصل صحيح يدل على خلاف الصغر" (maqayis); B006 — "الكبر العظمة وكذلك الكبرياء" (maqayis): the greatest, and the root reversed as self-importance.
- Quran 56:1–3 — "إذا وقعت الواقعة ليس لوقعتها كاذبة خافضة رافعة". The Day as the one that lowers and raises.
- Quran 69:21–22 — the man given his book in his right hand (69:19 opens): "فهو في عيشة راضية في جنة عالية". The same words as 88:9–10.
- Quran 83:18 — "إن كتاب الأبرار لفي عليين". Quran 58:11 — "يرفع الله الذين آمنوا منكم".
- Quran 42:45 — "خاشعين من الذل". Quran 70:44 — "ترهقهم ذلة".

### 18. The sun's day: from the face of the day to the return at sunset
Read as time words, the surah's roots run through one whole day. "The face of the day" is its start. The sun's disk is an عين, and the sun is "the runner" (الجارية). The day grows hot (حمى) and rises to its height (أكبر النهار). Stars sink (خشع), the sun nears setting and shadows shrink (ضرع). The sun "returns" (آبت) into its setting place. Then come the night hours (آناء), night's cover (جنان), and night as the coverer (كافر). The surah's own word إيابهم ends the course. The dictionary defines إياب as going "back to where one belongs", and Quran 36:38 has the sun running "to a place where it belongs" (مستقر).
- 88:2 وُجُوهٌ — و ج ه B007 — "وجه النهار أوله" (jamhara) [fixed expression]: daybreak.
- 88:5/88:12 عَيْنٍ — ع ي ن B008 — "طلعت العين وغابت العين، أي الشمس" (tahdhib): the sun's disk rising and setting.
- 88:12 جَارِيَةٌ — ج ر ي B001 — "الجارية السفينة والجارية الشمس" (maqayis;sihah): the sun as runner.
- 88:4 حَامِيَةً — ح م ي B001 — "حمى النهار وحمي التنور أي اشتد حره" (sihah): the heat of the day.
- 88:24 ٱلْأَكْبَرَ — ك ب ر B013 — "أكبر النهار وشباب النهار أي حين ارتفع النهار" (tahdhib) [fixed expression]: the day at its height.
- 88:2 خَٰشِعَةٌ — خ ش ع B003 — "خشوع الكواكب إذا غارت فكادت تغيب في مغيبها" (tahdhib) [fixed expression]: stars sinking toward setting.
- 88:6 ضَرِيعٍ — ض ر ع B006 — "تضريع الشمس دنوها للمغيب" (sihah) [fixed expression]; B008 — "تضرع الظل قل وقلص" (tahdhib) [fixed expression]: the sun nearing its setting, shade shrinking.
- 88:25 إِيَابَهُمْ — ء و ب B007 — "آبت الشمس إيابا إذا غابت في مآبها أي مغيبها" (ayn): the sun's return into its setting place.
- 88:5 ءَانِيَةٍ — ء ن ي B002 — "آناء الليل ساعاته" (sihah;tahdhib;mufradat): the hours of night.
- 88:10 جَنَّةٍ — ج ن ن B002 — "جنان الليل سواده وستره الأشياء" (maqayis): night's covering dark.
- 88:23 كَفَرَ — ك ف ر B002 — "الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر" (maqayis); "الليل كافر لأنه ستر بظلمته" (tahdhib): sunset and night as coverers.
- 88:18 ٱلسَّمَآءِ: where the whole course takes place.
- Quran 36:38 — God's signs: "والشمس تجري لمستقر لها". Running toward a place it belongs, the word in jamhara's definition of إياب.
- Quran 18:86 — the sun setting "في عين حمئة" (a reading حامية, from memory).
- Quran 91:1–4 — oaths by the sun and its morning light and "والليل إذا يغشاها" (from memory). Quran 92:1.

### 19. Rain from sky to ground
The sky's root also means cloud, rain and plants. The spring's root names rain that does not stop. سقي names a cloud of heavy drops. أتي names a flood that comes from rain fallen elsewhere. ولي names the rain that follows the first rain. خاشع is ground with no rain. Rain makes plants take hold (تأرض النبت) and grow tall and tangled (جن النبت). The farmer covers seed (كافر). 41:39 stages this outright: ground that is خاشعة comes alive under water.
- 88:18 ٱلسَّمَآءِ — س م و B004 — "العرب تسمى السحاب سماء والمطر سماء" (maqayis); "سمي النبات سماء" (mufradat): sky as cloud, rain and plants.
- 88:5 عَيْنٍ — ع ي ن B010 — "العين: مطر أيام لا يقلع" (sihah;tahdhib): rain that goes on for days.
- 88:5 تُسْقَىٰ — س ق ي B007 — "السقي على فعيل السحابة العظيمة القطر الشديدة الوقع" (sihah); B006 — "سقاه الله الغيث وأسقاه" (sihah) [fixed expression]: a heavy-drop cloud, and the prayer for rain.
- 88:1 أَتَىٰكَ — ء ت ي B005 — "سيل أتي وأتاوي إذا جاءك ولم يصبك مطره" (sihah) [fixed expression]: a flood from rain that fell elsewhere.
- 88:12 جَارِيَةٌ — ج ر ي B001 — "جرى الماء يجري جرية وجريا وجريانا" (maqayis;sihah;mufradat): water running.
- 88:23 تَوَلَّىٰ — و ل ي B010 — "الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي" (maqayis): the following rain.
- 88:2 خَٰشِعَةٌ — خ ش ع B002 — "إذا يبست الأرض ولم تمطر قيل قد خشعت" (tahdhib): ground with no rain.
- 88:20 ٱلْأَرْضِ — ء ر ض B002 — "تأرض النبت إذا أمكن أن يجز" (maqayis;sihah): plants grown tall enough to cut.
- 88:10 جَنَّةٍ — ج ن ن B011 — "جن النبت جنونا أي طال والتف وخرج زهره" (sihah); B003: plants grown tall, tangled and in flower, and the garden.
- 88:23 كَفَرَ — ك ف ر B008 — "الكافر الزارع لأنه يغطي البذر بالتراب" (sihah): seed covered under the soil.
- Quran 41:39 — God's signs: "ترى الأرض خاشعة فإذا أنزلنا عليها الماء اهتزت وربت".
- Quran 22:5 — "وترى الأرض هامدة فإذا أنزلنا عليها الماء اهتزت وربت".
- Quran 50:9–11 — "ونزلنا من السماء ماء مباركا فأنبتنا به جنات".
- Quran 80:24–31 — "فلينظر الإنسان إلى طعامه أنا صببنا الماء صبا ثم شققنا الأرض شقا".
- Quran 32:27 — "أولم يروا أنا نسوق الماء إلى الأرض الجرز فنخرج به زرعا تأكل منه أنعامهم".
- Quran 57:20 — "كمثل غيث أعجب الكفار نباته". Quran 30:50.

### 20. Well and cistern: dug, lined, ringed, gathering
Many of the surah's roots name a part of a desert water works. ج ب ل names digging down until you hit rock. حامية names the heavy stones that line a well. نصب names stones set round a well's rim or built into a basin. عين names a well's spring-point. خليقة names a rock hollow that catches rainwater, which joins خلق to السماء. مسطح names a flat rock walled round so water gathers on it. مآبة names the spot in a well where the water collects. أتي is the channel a man leads to his land. استقاء is drawing water.
- 88:19 ٱلْجِبَالِ — ج ب ل B005 — "أجبل القوم إذا حفروا فبلغوا المكان الصلب" (sihah) [fixed expression]: digging down to rock.
- 88:4 حَامِيَةً — ح م ي B011 — "الحامية الحجارة يطوى بها البئر" (ayn;tahdhib): stones lining the shaft.
- 88:19 نُصِبَتْ — ن ص ب B003 — "النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد" (maqayis); "النصيب الحوض ينصب من الحجارة" (maqayis): stones set round the rim, and a stone basin.
- 88:5/88:12 عَيْنٍ — ع ي ن B009 — "عين الركية وهما عينان كأنهما نقرتان في مقدمها" (maqayis); B006 — "العين الينبوع الذي ينبع من الأرض ويجري" (tahdhib): the well's eyes, and the spring rising from the ground.
- 88:17 خُلِقَتْ — خ ل ق B011 — "الخليقة نقر في صخرة يجتمع فيه ماء السماء" (jamhara); "الخليقة البئر ساعة تحفر" (tahdhib): a rock hollow holding sky water, and a newly dug well. This joins 88:17 to 88:18.
- 88:20 سُطِحَتْ — س ط ح B005 — "المسطح الصفاة يحاط عليها بالحجارة فيجتمع فيها الماء" (sihah); "صفيحة عريضة من الصخر يحوط عليه لماء السماء" (tahdhib): a flat rock walled round for rainwater.
- 88:25 إِيَابَهُمْ — ء و ب B001 — "مآبة البئر حيث يجتمع إليه الماء في وسطها" (ayn): the point where water gathers in the well.
- 88:1 أَتَىٰكَ — ء ت ي B004 — "الأتي الجدول يؤتيه الرجل إلى أرضه" (sihah); "أت لهذا الماء أي سهل جريه" (maqayis): a channel led to the land, which joins أتى to الأرض and to جري.
- 88:5 تُسْقَىٰ — س ق ي B001 — "الاستقاء الأخذ من النهر والبئر" (ayn): drawing from the well.
- Quran 67:30 — God to the Prophet: "قل أرأيتم إن أصبح ماؤكم غورا فمن يأتيكم بماء معين". أتى and معين together.
- Quran 23:18 — "وأنزلنا من السماء ماء بقدر فأسكناه في الأرض".
- Quran 39:21 — "ألم تر أن الله أنزل من السماء ماء فسلكه ينابيع في الأرض" (text from memory).
- Quran 28:23 — Moses at the water of Midian, people watering their flocks (يسقون) (from memory).

### 21. Shield and guarded ground
The garden is a shield and a fenced, protected place: "whatever guards you is your جنة". The fire's word حامية has a root that elsewhere means protecting and the guarded pasture, a fenced pasture where grazing is kept off. The spring's root gives the guarding eye. The overseer's root gives the guard who keeps watch.
- 88:10 جَنَّةٍ — ج ن ن B008 — "المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك" (ayn): shield, armour, whatever protects.
- 88:10 عَالِيَةٍ — ع ل و B001 — "أصل واحد يدل على السمو والارتفاع" (maqayis): set high, out of reach.
- 88:4 حَامِيَةً — ح م ي B002 — "الحمى موضع فيه كلأ يحمى من الناس أن يرعى" (ayn;tahdhib); "حميته حماية إذا دفعت عنه" (sihah): the fire's root reversed, a guarded pasture full of grass.
- 88:12 عَيْنٌ — ع ي ن B003 — "فلان بعيني أي أحفظه وأراعيه" (mufradat): kept under a watching eye.
- 88:22 بِمُصَيْطِرٍ — س ط ر B003 — "السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء" (ayn;tahdhib): the watcher and keeper.
- Quran 52:27 — the people of the garden: "فمن الله علينا ووقانا عذاب السموم" (from memory). Quran 44:56 — "ووقاهم عذاب الجحيم" (from memory).

### 22. Rows: cushions in line, lines of writing, the record
The cushions of 88:15 are set "on a straight line". The root of مصيطر (88:22) is defined by the dictionary as things set in a row (اصطفاف), the same word as مصفوفة: rows of writing and rows of planted trees. The overseer is the one who "writes his deeds". ذكر also names a written deed of right. Counting fills the account, and what is void is struck out of it.
- 88:15 مَصْفُوفَةٌ — ص ف ف B001 — "الصف أن تجعل الشيء على خط مستو" (mufradat): set along a straight line.
- 88:22 بِمُصَيْطِرٍ — س ط ر B001 — "أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر" (maqayis); "السطر الصف من الشيء والخط والكتابة" (sihah): the root is defined by rows, the word behind مصفوفة.
- 88:22 بِمُصَيْطِرٍ — س ط ر B001 — "السطر سطر من كتب وسطر من شجر مغروس" (ayn;tahdhib): rows of writing and rows of planted trees, the garden of 88:10.
- 88:22 بِمُصَيْطِرٍ — س ط ر B003 — "المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله" (sihah): the overseer who writes down deeds.
- 88:21 فَذَكِّرْ — ذ ك ر B008 — "ذكر الحق الصك وجمعه ذكور حقوق" (ayn;tahdhib) [fixed expression]: a written deed.
- 88:11 لَٰغِيَةً — ل غ و B001 — "وما يلغى من الحساب" (ayn;tahdhib): struck out of the count.
- 88:26 حِسَابَهُم — ح س ب B001 — "الحساب عدك الأشياء": counting.
- Quran 52:20 — "متكئين على سرر مصفوفة".
- Quran 54:52–53 — "وكل شيء فعلوه في الزبر وكل صغير وكبير مستطر". Deeds written in lines.
- Quran 52:1–2 — oath: "والطور وكتاب مسطور" (52:2 from memory). Quran 68:1 — "ن والقلم وما يسطرون".
- Quran 17:13–14 — "اقرأ كتابك كفى بنفسك اليوم عليك حسيبا".
- Quran 52:37 — "أم عندهم خزائن ربك أم هم المصيطرون".

### 23. Reminder, not overseer
The Prophet's work is reminding: making people remember and repeating the reminder. He is not the overseer set over them. Whoever turns his back and refuses is punished by God. The return is to Us and the account is on Us. ولي can mean taking charge of an office as well as turning away, so the same word holds both the role the Prophet does not have and the refusal of the man who turns.
- 88:21 فَذَكِّرْ / مُذَكِّرٌ — ذ ك ر B009 — "التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر" (mufradat); B003 — "ذكرت الشيء خلاف نسيته" (maqayis;sihah): the reminder, and the remembering it seeks.
- 88:22 لَّسْتَ — ل ي س B001 — "ليس: كلمة نفي، وهو فعل ماض" (sihah): the denial of a role.
- 88:22 بِمُصَيْطِرٍ — س ط ر B003 — "المسيطر المتعهد للشيء المتسلط عليه" (maqayis); "المسيطرون الأرباب المسلطون" (tahdhib): the overseer with power over others, a role reserved for lords.
- 88:23 تَوَلَّىٰ — و ل ي B003 — "تولى العمل أي تقلد" (sihah); B007 [fixed expression]: taking up a charge, set against turning one's back.
- 88:23 وَكَفَرَ — ك ف ر B003 — "الكفر ضد الإيمان سمى لأنه تغطية الحق" (maqayis): the refusal.
- 88:24 ٱللَّهُ — ء ل ه B001 — "فالإله الله تعالى لأنه معبود" (maqayis): the one who punishes is the one worshipped.
- 88:24 فَيُعَذِّبُهُ — ع ذ ب B005 — "أصل العذاب الضرب ثم استعير ذلك في كل شدة" (maqayis): the punishment, a beating at root. Some sources give this as an opinion ("ناس يقولون").
- 88:25–26 إِلَيْنَا ... عَلَيْنَا حِسَابَهُم: return and account belong to God.
- Quran 50:45 — God to the Prophet: "وما أنت عليهم بجبار فذكر بالقرآن من يخاف وعيد".
- Quran 87:9 — previous surah: "فذكر إن نفعت الذكرى". Quran 51:55; 52:29; 6:70 ("وذكر به").
- Quran 13:40 — "فإنما عليك البلاغ وعلينا الحساب". The same split as 88:21–26.
- Quran 42:48 — "فإن أعرضوا فما أرسلناك عليهم حفيظا إن عليك إلا البلاغ" (from memory). Quran 6:107.
- Quran 52:37 — "أم هم المصيطرون".
- Quran 80:1–12 — "عبس وتولى ... أو يذكر فتنفعه الذكرى ... كلا إنها تذكرة".

### 24. The snare: set up, and walked into
The two words that stand together in 88:3–4 (ناصبة, تصلى) are joined in one dictionary phrase. نصب is setting a snare, and مصلاة is "to set a snare so something falls into it". Around them are the hunters (سماة) and the bow that "feeds" its owner game. The toiling face is like a bird walking into a trap.
- 88:3 نَّاصِبَةٌ — ن ص ب B001 — "نصبت للقطاة شركا" (tahdhib): a snare set for the sandgrouse.
- 88:4 تَصْلَىٰ — ص ل ي B005 — "المصلاة أن تنصب شركا ونحوه" (ayn); "المصالي شبيهة بالشرك تنصب للطير وغيرها" (tahdhib): the trap, defined with the verb نصب.
- 88:6 طَعَامٌ — ط ع م B006 — "قوس مطعمة تطعم صاحبها الصيد" (maqayis): the bow that brings game to its owner.
- 88:18 ٱلسَّمَآءِ — س م و B006 — "السماة الصيادون" (sihah): hunters.

### 25. Bowing and burning: the two faces of صلى
خاشع is also the one who bows in prayer (راكع). نصب is the toil of worship. The verb of 88:4, صلى, means burning in a fire and also the prescribed prayer of bowing and prostration. The previous surah sets the two meanings next to each other. The root of الإبل also names a Christian monk. From memory: Ibn ʿAbbās is reported to have said that عاملة ناصبة refers to the Christians, meaning ascetics who toiled at worship without reward.
- 88:2 خَٰشِعَةٌ — خ ش ع B001 — "الخاشع المستكين والراكع" (maqayis); "الخاشع الراكع" (jamhara): the bowing posture of worship.
- 88:3 عَامِلَةٌ نَّاصِبَةٌ — ع م ل B001; ن ص ب B004 — "النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي" (maqayis): standing at toil until exhausted.
- 88:4 تَصْلَىٰ — ص ل ي B001 — "الصلاة التي جاء بها الشرع من الركوع والسجود" (maqayis); B003 [fixed expression]: prayer and burning in one root.
- 88:4 تَصْلَىٰ — ص ل ي B008 — "يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات" (mufradat): houses of worship.
- 88:17 ٱلْإِبِلِ — ء ب ل B006 — "الأبيل راهب النصارى" (sihah): the monk.
- 88:21 فَذَكِّرْ — ذ ك ر B005 — "الذكر الصلاة والدعاء والثناء" (ayn;tahdhib): remembrance as prayer.
- 88:24 ٱللَّهُ — ء ل ه B001 — "فالإله الله تعالى لأنه معبود" (maqayis): the one worshipped.
- Quran 87:12 and 87:14–15 — previous surah: "الذي يصلى النار الكبرى" set against "قد أفلح من تزكى وذكر اسم ربه فصلى".
- Quran 75:31–32 — the dying denier: "فلا صدق ولا صلى ولكن كذب وتولى". صلى and تولى together. Quran 92:15–16.
- Quran 23:1–2 — "الذين هم في صلاتهم خاشعون". Quran 94:7 — "فإذا فرغت فانصب".
- Quran 57:27 — "ورهبانية ابتدعوها". Quran 18:103–104.

### 26. The grave: laid flat, covered over, sent back
Under burial senses, سطح is a man stretched on his back and unmoving, a body laid out, and a grave smoothed flat rather than heaped. ج ن ن is covering the dead and the grave. ك ف ر also means grave. The return of 88:25 comes after.
- 88:20 سُطِحَتْ — س ط ح B002 — "انسطح الرجل إذا امتد على قفاه فلم يتحرك" (jamhara;maqayis); "السطيح المسطوح وهو القتيل" (ayn;tahdhib): the body laid flat.
- 88:20 سُطِحَتْ — س ط ح B001 — "تسطيح القبر خلاف تسنيمه" (sihah): a grave smoothed flat.
- 88:10 جَنَّةٍ — ج ن ن B009 — "جننت الميت وأجننته أي واريته والجنن القبر" (sihah): covering the dead.
- 88:23 كَفَرَ — ك ف ر B012 — "الكفر أيضا القرية والكفر أيضا القبر" (sihah): the grave.
- 88:20 ٱلْأَرْضِ: the ground the body is laid in.
- 88:25 إِيَابَهُمْ — ء و ب B001 — "آب الغائب يؤوب أوبا أي رجع" (ayn): the absent one returns.
- Quran 20:55 — "منها خلقناكم وفيها نعيدكم ومنها نخرجكم تارة أخرى" (from memory).
- Quran 80:21–22 — "ثم أماته فأقبره ثم إذا شاء أنشره" (from memory).

### 27. Generation: union, the hidden fetus, delivery
Read for their birth senses, the surah's words follow a pregnancy. The dictionary glosses غشيان as "إتيان الرجل المرأة", joining both words of 88:1. A fetus lies hidden (جنين) in the fluid of the afterbirth sac (سقي). The navel cord is cut (سر), the hindquarters open at birth (صلا), the child is delivered (وضعت), the embryo is fully formed (مخلقة), and the afterbirth follows (عذب).
- 88:1 ٱلْغَٰشِيَةِ — غ ش و B004 — "الغشيان كناية عن إتيان الرجل المرأة" (tahdhib); "غشيها غشيانا جامعها" (sihah): union. This joins غشي and أتى.
- 88:10 جَنَّةٍ — ج ن ن B007 — "الجنين الولد في بطن أمه" (maqayis): the hidden fetus.
- 88:5 تُسْقَىٰ — س ق ي B005 — "السقي الماء الذي يكون في المشيمة" (tahdhib): the fluid in the sac.
- 88:13 سُرُرٌ — س ر ر B006 — "السر ما تقطعه القابلة من سرة الصبي" (sihah): the cord the midwife cuts.
- 88:4 تَصْلَىٰ — ص ل ي B006 — "انفرج صلاها" (ayn): the hindquarters opening at birth.
- 88:14 مَّوْضُوعَةٌ — و ض ع B002 — "وضعت المرأة ولدها" (maqayis): the delivery.
- 88:17 خُلِقَتْ — خ ل ق B003 — "مضغة مخلقة أي تامة الخلق" (sihah): a fully formed embryo.
- 88:24 ٱلْعَذَابَ — ع ذ ب B009 — "العذب ما يخرج على أثر الولد من الرحم" (tahdhib): the afterbirth.
- Quran 7:189 — "فلما تغشاها حملت حملا خفيفا". Quran 53:32 — "وإذ أنتم أجنة في بطون أمهاتكم".
- Quran 22:5 — "ثم من مضغة مخلقة وغير مخلقة ... ونقر في الأرحام ما نشاء". The same ayah goes on to "وترى الأرض هامدة".
- Quran 22:1–2 — the quake of the Hour: "وتضع كل ذات حمل حملها" (from memory).

## Interactions
- Covering (1) and Reminder (23): الغاشية in 88:1 and العذاب in 88:24 are joined by "غاشية من عذاب الله أي عقوبة مجللة تعمهم" (tahdhib). Quran 12:107 joins أتى, غاشية and عذاب.
- Covering (1) and Fire (7): one cover falls on faces, and Quran 14:50 makes that cover the fire itself ("وتغشى وجوههم النار"). The كافر of 88:23 is the one who covers, and the ayn phrase "صلى الكافر نارا" names him as the one who burns.
- Covering (1) and Furnished world (15): ع ذ ب B004, "العذوب الذي ليس بينه وبين السماء ستر", leaves a man with no cover under the raised sky (السماء سقف البيت).
- Covering (1) and Rain (19): the farmer كافر covers seed, and the garden is trees covering ground. Quran 57:20 sets "الكفار" admiring plants.
- Covering (1) and Sun's day (18): جنان الليل and "الليل كافر" share members. Quran 92:1 ("والليل إذا يغشى") puts night under the root of الغاشية.
- Face as ground (2) and Rain (19): خاشعة is a shared member, ground with no rain. Quran 41:39 and 22:5 stage water reviving that ground.
- Face as ground (2) and Fire (7): the dry face is watered, but from a boiling spring. Quran 18:29 has scalding water on faces.
- Face's look (3) and Food (10): "إذا ضرع القلب خشعت الجوارح" (mufradat under خ ش ع) joins the humbled face of 88:2 to the root of ضريع in 88:6. The face is humbled by what it eats.
- Face's look (3) and Work (6): نصب is a shared member. Quran 15:48 and 35:35 remove نصب in the garden, and راضية answers it.
- Face's look (3) and Furnished (15): سرر is a shared member. The couch is named from joy ("السرير الذي يجلس عليه من السرور").
- Gaze (4) and Hearing (5): خاشعة is in both, as lowered eyes and hushed voices. Quran 20:108 and 42:45 stage each.
- Gaze (4) and Furnished world / Making (15, 16): the four objects of ينظرون are the four objects of رفع, نصب, سطح and خلق. Quran 50:6 joins ينظروا, السماء and "كيف بنيناها".
- Gaze (4) and Pot (9): ينظرون also means waiting. Quran 33:53 ("غير ناظرين إناه") joins نظر to the آنية of 88:5.
- Hearing (5) and Work (6) and Rows (22): لاغية is a shared member. It is the word not heard in the garden, and "ما يلغى من الحساب" makes it the item struck from the account of 88:26.
- Work (6) and Food (10): يغني (sufficiency) is set against حساب ("عطاء حسابا أي كافيا"). The toiler's wage is food that does not suffice. Quran 78:36.
- Fire (7) and Two springs (8): عين آنية is a shared member ("حميم آن قد انتهى حره وعين آنية"). Quran 55:44 and 55:50 set the two springs side by side.
- Fire (7) and Pot (9): تصلى, حامية and آنية are shared members, burning and cooking from one set of words. Quran 4:56 has skins "cooked through".
- Fire (7) and Sun's day (18) and Well (20): the dictionary pairs عين with this root ("عين حمئة"). Quran 18:86 sets the sun into it, and the reading حامية there is from memory.
- Two springs (8) and Milk (12): أكواب is the قدح that a صفوف camel fills. سقاء holds water and milk. Quran 47:15 has rivers of water and milk set against حميم.
- Two springs (8) and Food (10): "الإطعام يقع حتى الماء" puts drink under feeding, so 88:5 and 88:6 are one meal.
- Pot (9) and Snare (24): ن ص ب B001 "نصبت للقطاة شركا ونصبت للقدر نصبا" holds the snare and the pot-stand in one sentence.
- Food (10) and Camel body (11) and Milk (12): ضريع is fodder in one sense and an udder in another, and "المطعم من الإبل ... بعض السمن" joins طعم, إبل and سمن. The food that "does not fatten" is set against the herd that does.
- Camel body (11) and Face's look (3): خشع is also a camel's hump losing its fat. Quran 22:27 has lean camels (ضامر) coming in.
- Camel's march (13) and Coming/return (14): أتو in 88:1 and أوب in 88:25 are both the forelegs' swing. The full day's march ends in "كل راجع مع الليل فهو آئب".
- Camel's march (13) and Furnished (15): مرفوع and موضوع are opposite gaits in one phrase ("مرفوع الناقة في سيرها خلاف الموضوع") and opposite placings ("الرفع يقال في الأجسام الموضوعة").
- Coming/return (14) and Sun's day (18): إياب is "رجع إلى مستقره" (jamhara) and "آبت الشمس". Quran 36:38: "والشمس تجري لمستقر لها".
- Coming/return (14) and Furnished world (15): "التأويب التسبيح في قوله يا جبال أوبي معه" (maqayis) joins أوب and جبال. Quran 34:10.
- Furnished world (15) and Lowered/raised (17): رفع and وضع name places and also rank ("الرفعة نقيض الذلة", "رجل وضيع ضد الشريف"). Quran 55:7 and 55:10, and 56:3 ("خافضة رافعة").
- Furnished world (15) and Rows (22): صف means a row of cushions, level ground ("الصفصف ... كأنه على صف واحد"), and lines of writing (سطر "اصطفاف"). Quran 52:20.
- Making (16) and Two springs / Milk (8, 12): "خلقت الأديم للسقاء إذا قدرته" joins the camel's creation to the waterskin.
- Making (16) and Well (20): خلق also names a rock hollow catching "ماء السماء", and سطح a walled flat rock "لماء السماء". Both join 88:17 and 88:20 to 88:18.
- Rain (19) and Well (20): rain from the sky is stored in the ground. Quran 23:18 ("فأسكناه في الأرض") and 67:30.
- Shield (21) and Fire (7): حامية is heat and also a guarded pasture. Shield (21) and Reminder (23): the watcher (رقيب حافظ) is a role denied to the Prophet in 88:22.
- Rows (22) and Reminder (23): the مصيطر "يكتب عمله". The Prophet is not that writer, and the count is God's (13:40, 54:53).
- Bowing/burning (25) and Coming/return (14): Quran 75:31–32 and 92:15–16 join صلى and تولى. Quran 87:12–15 sets يصلى النار against فصلى.
- Grave (26) and Covering (1): جنن and كفر (grave) are covering senses. Grave (26) and Making (16): "تسطيح القبر خلاف تسنيمه" levels the grave as the earth is levelled.
- Generation (27) and Covering (1) and Coming (14): "الغشيان كناية عن إتيان الرجل المرأة" joins both words of 88:1. Quran 22:5 joins the embryo (مخلقة) with the dried ground revived.

## Ayat

**88:1** هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- Covering (1): الغاشية is the cover itself, the Day that covers creation with terror, a saddle-cloth, a swoon. Across the surah the Overwhelmer covers faces, the garden is a hidden cover of trees, the refuser covers truth, and the closing العذاب is "غاشية من عذاب الله".
- Hearing (5): أتاك and حديث are speech reaching the ear. Across the surah the report arrives, voices hush, the ugly word goes unheard, and the reminder makes people remember.
- Coming/return (14): أتاك and غاشية ("غشيت موضع كذا أتيته") are the arrival. Across the surah the Day comes, the refuser turns his back, all return to Us, and the account follows.
- Camel's march (13): أتو is the forelegs' swing [fixed expression]. Across the surah forelegs swing, the day's easy march has its song, gaits rise and fall, the neck kneels for mounting, and the rider comes home at nightfall.
- Rain (19): أتي is a flood from far rain [fixed expression]. Across the surah cloud and rain come from the sky, rainless ground stands against soft grown ground, and the garden grows thick.
- Well (20): أتي is a channel led to the land. Across the surah the well is dug to rock, lined with stones, ringed at the rim, water gathers in rock hollows and at the well's gathering point, and is drawn.
- Generation (27): غشيان / إتيان is union. Across the surah union is followed by the hidden fetus in its fluid, the cut cord, delivery, the formed embryo and the afterbirth.

**88:2** وُجُوهٌ يَوْمَئِذٍ خَٰشِعَةٌ
- Face as ground (2): خاشعة is ground dried, dusty and low. Across the surah one set of faces is rainless ground given scalding water, the other is soft ground with a running spring, and the earth is shown spread.
- Face's look (3): humbled, and tied by the dictionary to the ضراعة of its food. Across the surah humbled, worn, grieving faces stand against soft, content faces on couches named from joy.
- Gaze (4): eyes thrown to the ground. Across the surah lowered eyes, springs named "eye", and the call to look at camel, sky, mountains and earth.
- Hearing (5): "خشعت الأصوات". The scene runs as in 88:1.
- Lowered/raised (17): pressed down. Across the surah faces sit low against a high garden and raised couches, the sky is raised over low earth, and the punishment is the greatest.
- Covering (1): faces as the front the cover falls on.
- Camel body (11): a sinking hump [fixed expression]. Across the surah the herd's fodder (camels' bread, shibriq, salt-bush), fat and sunken humps, working camels, and the herd named نعم.
- Sun's day (18): وجه النهار is daybreak, and stars sinking [fixed expression]. Across the surah daybreak, the sun's disk running, noon heat and the day's height, the sun sinking, the return into setting, night's hours and cover.
- Rain (19): ground that has had no rain.
- Bowing/burning (25): الخاشع الراكع. Across the surah the bowing, toiling posture of worship meets صلى, which is both prayer and burning.
- Coming/return (14): وجهة, the way the face is turned.

**88:3** عَامِلَةٌ نَّاصِبَةٌ
- Work (6): work done with intent, a wage owed, exhaustion, no share. Across the surah one face toils for fatigue, another is content with its effort, the void is struck out, and the count is God's.
- Face's look (3): grief worn into the face.
- Camel body (11): يعملة, the working she-camel. Camel's march (13): a day's easy march and the riders' song.
- Pot (9): the pot-stand ("نصبت للقدر نصبا"). Across the surah an oven at full heat, meat roasting, a pot on its stand reaching its point of doneness, and the food awaited.
- Snare (24): "نصبت للقطاة شركا". Across the surah a snare is set and a trap walked into, with hunters and the bow that brings game.
- Bowing/burning (25): standing at toil in worship. The tafsir reading about Christians is from memory.

**88:4** تَصْلَىٰ نَارًا حَامِيَةً
- Fire (7): entering a fire heated to the full. Across the surah fire at full heat, a spring at boiling point, all named in "صلى الكافر نارا", with blossom as the fire root's reverse.
- Pot (9): fuel, roasting, the oven heated. Two springs (8): حميا الكأس, the cup's heat.
- Camel body (11): صليان, camels' bread. Sun's day (18): the heat of the day.
- Well (20): well-lining stones. Shield (21): the guarded pasture, the reverse of fire. Across the surah the garden is shield and fenced ground, under a guarding eye and a watcher.
- Snare (24): مصلاة, the trap. Bowing/burning (25): صلاة. Generation (27): the hindquarters opening at birth.

**88:5** تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍ
- Two springs (8): a boiling spring, and آنية as vessels. Across the surah a boiling spring stands against a running spring, with cups set down beside vessels (76:15) and sweet water as العذاب's reverse.
- Fire (7): "عين آنية" and "عين حمئة". Pot (9): "إنى الطعام".
- Gaze (4): عين is the eye. Face as ground (2): the dry face is watered.
- Milk (12): سقاء, the skin for water and milk. Across the surah the udder, milk held back, a row of cups filled at one milking, ghee.
- Sun's day (18): the sun's disk, and the hours of night. Rain (19): a heavy-drop cloud and rain that does not stop. Well (20): drawing water and the well's eye. Generation (27): the fluid of the sac.

**88:6** لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍ
- Food (10): a flat denial, and dry shibriq or red stinking plant, thin drink, a big-uddered ewe as reverse, a lean body, want. Across the surah food that neither fattens nor fills, set against fat, sufficiency and "enough".
- Face's look (3) and Lowered/raised (17): ضراعة, abasement.
- Pot (9): a pot about to be done [fixed expression]. Two springs (8): "الإطعام يقع حتى الماء".
- Camel body (11): dry fodder, and "المطعم من الإبل". Milk (12): the udder.
- Sun's day (18): the sun near setting, shade shrinking [fixed expressions]. Snare (24): the bow that "feeds" game.

**88:7** لَا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍ
- Food (10): fat as the opposite of leanness, sufficiency, hunger defined by an empty stomach. The scene runs as in 88:6.
- Work (6): a return that does not suffice. Camel body (11): the fat animal. Milk (12): ghee.

**88:8** وُجُوهٌ يَوْمَئِذٍ نَّاعِمَةٌ
- Face as ground (2): soft, fresh, the moist wind. Face's look (3): ease, a sight that cools the eye.
- Camel body (11) and Milk (12): النعم, the herd named for its good.
- Covering (1): faces as the front.

**88:9** لِّسَعْيِهَا رَاضِيَةٌ
- Work (6): effort as earning, contentment between the striver and God. Face's look (3): content.
- Camel's march (13): an easy run.
- Coming/return (14): راضية returning (89:28).

**88:10** فِى جَنَّةٍ عَالِيَةٍ
- Covering (1): a cover of trees over ground, the reward hidden now, night's cover.
- Lowered/raised (17): high, with haughtiness as the reverse. Shield (21): a shield, set high.
- Rain (19): thick, tall growth. Rows (22): rows of planted trees (سطر). Across the surah cushions in line, lines of writing and planted rows, the overseer who writes, the deed, the count.
- Sun's day (18): night's cover. Grave (26): covering the dead. Across the surah a body laid flat, a grave smoothed level and covered, then the return.
- Generation (27): the hidden fetus.

**88:11** لَّا تَسْمَعُ فِيهَا لَٰغِيَةً
- Hearing (5): hearing as understanding, the ugly word and barking absent.
- Work (6) and Rows (22): "ما يلغى من الحساب", the void struck from the count.

**88:12** فِيهَا عَيْنٌ جَارِيَةٌ
- Two springs (8): "العين الجارية". Face as ground (2): the soft ground's spring.
- Gaze (4): water open to the eyes. Shield (21): the guarding eye.
- Camel's march (13): running. Sun's day (18): the sun as runner and as disk.
- Rain (19): water running. Well (20): the spring rising from the ground.

**88:13** فِيهَا سُرُرٌ مَّرْفُوعَةٌ
- Furnished (15): couches raised, brought near, a resting place, set against the raised sky. Across the surah couches raised, cups set, cushions in row, carpets spread, and the world as tent: sky-roof, mountain-pegs, a spread floor and carpet, a tent pole.
- Face's look (3): couch named from joy, the forehead's lines. Lowered/raised (17): "الرفعة نقيض الذلة".
- Milk (12): milk held back [fixed expression]. Camel's march (13): the raised gait.
- Making (16): lifting from its place. Across the surah measuring, raising, setting upright and levelling, all turning on evenness.
- Generation (27): the cut cord.

**88:14** وَأَكْوَابٌ مَّوْضُوعَةٌ
- Two springs (8): cups without handles, set down to hand. Furnished (15): the opposite of raised.
- Milk (12): the كوب as قدح. Camel body (11): camels on salt-bush.
- Camel's march (13): the quick gait and the neck lowered for mounting.
- Lowered/raised (17): وضيع, lowly. Generation (27): delivery.

**88:15** وَنَمَارِقُ مَصْفُوفَةٌ
- Furnished (15): a straight row, the same word as level ground. Rows (22): the row matching سطر.
- Milk (12): the camel that lines up cups. Camel body (11): sacrificial camels in line.

**88:16** وَزَرَابِىُّ مَبْثُوثَةٌ
- Furnished (15): rugs spread, and "خلق الخلق وبثهم في الأرض". The reverse is people scattered like moths (101:4).

**88:17** أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- Gaze (4): the look of eye and mind, with looking without seeing as the danger.
- Pot (9): waiting.
- Camel body (11), Milk (12), Camel's march (13): the camel itself.
- Making (16): the hide measured for a waterskin, smoothing and levelling.
- Well (20): a rock hollow catching sky water, a new well.
- Bowing/burning (25): الأبيل, the monk. Generation (27): the fully formed embryo.

**88:18** وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- Furnished (15): the sky as roof, built upward. Making (16): lifting.
- Gaze (4): the upward look. Lowered/raised (17): height.
- Sun's day (18): where the day runs its course. Rain (19): cloud, rain and plants.
- Covering (1): the open sky above the man left uncovered. Snare (24): hunters (سماة).

**88:19** وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- Furnished (15): the earth's pegs, set up by "setting down so it stands out". Making (16): upright and even.
- Well (20): digging down to rock [fixed expression], stones set round the rim, a stone basin.
- Coming/return (14): "يا جبال أوبي معه". Pot (9) and Snare (24): نصب as pot-stand and snare.

**88:20** وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- Furnished (15): spread as floor, carpet (إراض), level ground "on a single row", a tent pole. Making (16): levelled.
- Face as ground (2): soft, good soil. Gaze (4) and Lowered/raised (17): what lies low.
- Rain (19): plants grown tall. Well (20): a flat rock walled round for rainwater.
- Grave (26): a body laid flat, a grave levelled.

**88:21** فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌ
- Reminder (23): reminding, and the remembering it aims at. Across the surah the Prophet reminds, is not set over them, God punishes the one who turns and refuses, and the return and account are God's.
- Hearing (5): speaking out, remembering as against forgetting.
- Rows (22): a written deed [fixed expression]. Bowing/burning (25): remembrance as prayer.

**88:22** لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- Reminder (23): the overseer's role is denied. Rows (22): the root of rows, the one who writes deeds.
- Shield (21): the watcher.

**88:23** إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- Coming/return (14): turning one's back [fixed expression], with turning toward as the reverse. Reminder (23): taking a charge, set against turning away, and refusal.
- Covering (1): covering truth, night, the farmer. Fire (7): "صلى الكافر نارا".
- Sun's day (18): sunset and night. Rain (19): the following rain, the farmer covering seed. Grave (26): الكفر, the grave.
- Bowing/burning (25): "ولا صلى ... وتولى" (75:31–32).

**88:24** فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- Covering (1): the covering punishment, and the man with no cover under the sky. Fire (7): the punishment the fire scene ends in.
- Reminder (23): God, the one worshipped, as the punisher, and a beating as the root sense.
- Lowered/raised (17): the greatest, and self-importance. Sun's day (18): the day at its height [fixed expression].
- Two springs (8): sweet water as the reverse. Generation (27): the afterbirth.

**88:25** إِنَّ إِلَيْنَآ إِيَابَهُمْ
- Coming/return (14): coming back to where one belongs, and turning back to God.
- Camel's march (13): the legs' swing and the homecoming at nightfall. Sun's day (18): the sun's return into its setting.
- Well (20): the point where water gathers in the well. Grave (26): the absent one returns.
- Reminder (23): the return is to God.

**88:26** ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم
- Work (6): the count, and a gift in full measure. Rows (22): counting.
- Food (10): "enough". Reminder (23) and Coming/return (14): the account is on God (13:40).

