Surah: 87. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (87:1 to 87:19), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s087/surah.r2/text.md =====
# Surah 87

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/out/s087/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. The rain sky: cloud, lightning watched, first rain
This is the weather that comes before 87:4. The surah only says أَخْرَجَ ٱلْمَرْعَىٰ, but the dictionary entries for its other words lay out what happens first. Cloud forms and hangs low. It is called "rabāb" because it rears plants, and it lingers. Faint lightning flickers at its edges while someone stays awake all night watching where it will flash. The first rain of the year marks the ground with green. Rain is "ḥayā" because it brings the land to life, and it drives creatures out of their burrows. The image runs from the sky (اسم, رب), through the night watch (يخفى, أبقى), to the living ground (يحيى) and to what is brought out (أخرج).
- 87:1/87:15 ٱسْمَ · س م و B004 · «العرب تسمى السحاب سماء والمطر سماء» and «يسموا النبات سماء» (maqayis); «السماء كل ما علاك فأظلك» (sihah) · one word covers the whole column: overhead cover, cloud, rain and the plant the rain raises.
- 87:1/87:15 ٱسْمَ · و س م B003 (the dictionary's documented alternative derivation of اسم, from the Kufans and Thaʿlab) · «سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة» (tahdhib) · the first rain marks the earth with plants. The phrase itself contains أثر (the root of 87:16) and أول (87:18).
- 87:1/87:15 رَبِّ · ر ب ب B008 · «الرباب: السحاب، سمي بذلك لأنه يرب النبات» (mufradat); «السحاب المتعلق دون السحاب يكون أبيض ويكون أسود» (maqayis) · the low hanging cloud that rears the plants.
- 87:1/87:15 رَبِّ · ر ب ب B007 · «أربت الجنوب والسحابة أي دامت» (sihah); «أربت السحابة: دامت» (mufradat) · the cloud stays put. The sihah phrase joins this root with ج ن ب (the south wind) and so with 87:11.
- 87:11 يَتَجَنَّبُهَا · ج ن ب B006 · «الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح» (ayn) · the south wind that drives the cloud.
- 87:4 أَخْرَجَ · خ ر ج B005 [fixed expression] · «الخروج السحاب أول ما يبدأ» (ayn); «أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن» (tahdhib) · the cloud first appearing.
- 87:7 يَخْفَىٰ · خ ف ي B004 · «خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم» (sihah) · weak lightning running sideways along the cloud's edges.
- 87:17 أَبْقَىٰٓ · ب ق ي B005 · «بات فلان يبقي البرق أي ينظر إليه من أين يلمع» (maqayis;ayn) · the watcher who spends the night tracking that lightning.
- 87:13 يَحْيَىٰ / 87:16 ٱلْحَيَوٰةَ · ح ي ي B002 · «يسمى المطر حيا لأن به حياة الأرض» (maqayis); «الحيا المطر لأنه يحيي الأرض بعد موتها» (mufradat) · rain is named for the life it gives the land.
- 87:7 يَخْفَىٰ · خ ف ي B003 · «خفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن» (maqayis) · rain brings mice out of their holes. The dictionary glosses this خفي with أخرج, the verb of 87:4.
- Quran: 7:57 (God describes winds lifting heavy clouds and driving them to a dead land; water sent down, fruits brought out; «كذلك نخرج الموتى لعلكم تذكرون»). 50:9–11 (God's speech: blessed water from the sky, gardens, a dead land revived, «كذلك الخروج»). 20:53 (Moses answering Pharaoh about his Lord: water sent down from the sky, «فأخرجنا به أزواجا من نبات شتى»; the scene opens at 20:49).

### 2. The pasture's course: brought out, darkened, dried, gathered as wrack
87:4–5 squeeze a pasture's whole life into two clauses. It is brought out of the soil in patches, in a dark colour. It is turned (جعل) into غثاء. The dictionary's غثاء is grass that has dried "after its green", lost its sweetness, been heaped together by a flood and carried along. أحوى is "black from green": a green mixed with black and yellow. It can name the deep dark of lush growth or the blackening of decay. Al-Farrāʾ (from memory) read أحوى as describing the pasture when it is brought out, dark green, before it is made غثاء. The Quran uses this same process as its parable of «ٱلْحَيَوٰةَ ٱلدُّنْيَا» (87:16).
- 87:4 أَخْرَجَ · خ ر ج B002 · «الإخراج أكثر ما يقال في الأعيان» (mufradat) · solid things brought out: the plants out of the ground.
- 87:4 أَخْرَجَ · خ ر ج B007 · «أرض مخرجة نبتها في مكان دون مكان» (ayn;sihah;tahdhib;mufradat); «الأخرج لون سواده أكثر من بياضه» (ayn;tahdhib) · patchy first growth, and a colour in which dark outweighs light. This anticipates أحوى.
- 87:4 ٱلْمَرْعَىٰ · ر ع ي B001 · «المرعى الرعي والموضع والمصدر» (sihah) · the grass, the place where it grows, and the grazing itself.
- 87:5 أَحْوَىٰ · ح و ي B006 · «الأحوى الأسود من الخضرة» (tahdhib); «بعير أحوى إذا خالط خضرته سواد وصفرة» (sihah) · green turning black; green mixed with black and yellow.
- 87:5 فَجَعَلَهُۥ · ج ع ل B002 · «جعل صير» (tahdhib) · the turn from one state to the next.
- 87:5 غُثَآءً · غ ث و B002 · «غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته» (sihah;tahdhib); «يابسا بعد خضرته» (tahdhib) · the flood heaps the grazing ground together and takes its sweetness away; dry after green.
- 87:5 غُثَآءً · غ ث و B001 · «الغثاء ما جاء به السيل من نبات قد يبس» (ayn) · the dried plants the flood brings down.
- 87:5 أَحْوَىٰ · ح و ي B001 · «حواه يحويه حيا أي جمعه واحتواه مثله» (sihah) · gathering, which matches the flood's «جمع بعضه إلى بعض».
- 87:13 يَحْيَىٰ · ح ي ي B002 · «الحي من النبات ما كان طريا يهتز» (tahdhib) · living grass is fresh and quivering, the state before غثاء.
- 87:13 يَمُوتُ · م و ت B003 · «الموتان الأرض لم تحي بعد بزرع ولا إصلاح» (maqayis) · dead land: the ground before it is brought to life and after the pasture has gone.
- 87:10 يَخْشَىٰ · خ ش ي B004 · «الخشي وهو اليابس» (sihah); «الخشو الحشف من التمر» (sihah) · dried and shrivelled. Maqayis lists this «مما شذ عن الباب وقد يمكن الجمع بينهما على بعد».
- 87:1/87:15 رَبِّ · ر ب ب B012 · «اسم لعدة من النبات لا تهيج في الصيف» (tahdhib) · plants that do not dry out in summer: the opposite of the pasture's fate.
- Quran: 18:45 (God tells the Prophet to strike the likeness of «ٱلْحَيَوٰةِ ٱلدُّنْيَا»: water from the sky, plants mingling, then «هشيما تذروه الرياح»). 57:20 (the near life as rain whose plants «يهيج فتراه مصفرا ثم يكون حطاما»). 39:21 (God's sign: water from the sky, «يخرج به زرعا مختلفا ألوانه ثم يهيج فتراه مصفرا ثم يجعله حطاما», with «لذكرى»). 10:24 (the near life as rain-fed plants made «حصيدا»). 79:31–33 («أخرج منها ماءها ومرعاها ... متاعا لكم ولأنعامكم»; the scene opens at 79:27). 56:63–65 (God on the sown field: «لو نشاء لجعلناه حطاما»). 23:41 (a destroyed people: «فجعلناهم غثاء»; the scene opens at 23:31). 55:64 (from memory as a visual parallel: «مدهامتان», gardens dark with green).

### 3. The flood: the wrack goes, the water stays
In the same flood the dictionary tells two things apart. One is what floats and scatters, the غثاء that "goes off and is not counted". The other is the water, which collects in rock hollows the Arabs call «الخلائق», in twisting pits the flood fills, and in wells cleaned until the water shows. The surah's words نفع (87:9) and أبقى (87:17) name what the collected water does: it serves, and it stays.
- 87:5 غُثَآءً · غ ث و B001 · «الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر» (mufradat) · what rises to the surface and scatters, in a flood or in a cooking pot.
- 87:5 غُثَآءً · غ ث و B004 · «يضرب به المثل فيما يضيع ويذهب غير معتد به» (mufradat) · the proverbial thing that is lost and gone, of no account.
- 87:9 نَّفَعَتِ · ن ف ع B001 · «ما يستعان به في الوصول إلى الخيرات» (mufradat) · what helps one reach good things. The phrase carries خير, the word of 87:17.
- 87:17 أَبْقَىٰٓ · ب ق ي B001 · «البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء» (mufradat) · staying fixed in its state, the opposite of perishing. The phrase also carries «الأولى» (87:18).
- 87:2 خَلَقَ · خ ل ق B011 · «الخليقة نقر في صخرة يجتمع فيه ماء السماء» (jamhara); «قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق» (tahdhib) · rock basins that hold rainwater. The tahdhib phrase joins خلق with س م و (السماء, تسميها).
- 87:5 أَحْوَىٰ · ح و ي B008 · «الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل» (tahdhib) · twisting pits that the flood fills.
- 87:1/87:15 رَبِّ · ر ب ب B013 · «الربب وهو الماء الكثير سمي بذلك لاجتماعه» (maqayis) · plentiful water, named for its gathering.
- 87:7 ٱلْجَهْرَ · ج ه ر B008 [fixed expression] · «جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو» (sihah) · a well cleaned until its water shows and runs clear.
- 87:7 يَعْلَمُ · ع ل م B005 · «العيلم البئر الكثيرة الماء» (tahdhib) · a well full of water.
- Quran: 13:17 (God's likeness: valleys flow «بقدرها», the flood carries a swelling scum, metal in the fire throws up a scum like it; «فأما الزبد فيذهب جفاء وأما ما ينفع الناس فيمكث في الأرض»).

### 4. The tilled field: split, grown, yielding, its due given
87:14 «قَدْ أَفْلَحَ مَن تَزَكَّىٰ» sits on a farming scene that the dictionary spells out. فلح is to split the earth; the فلّاح is the ploughman. زكا is the crop growing and increasing, and also the portion paid out of wealth. خراج is the field's yield, taken out each year by a known measure. The ربّ of an estate is the one who keeps it in good order and brings it to completion, and «الباقي» is what is left of the yield. The dictionary also defines فلاح as «البقاء في الخير», which carries the field into 87:17 «خَيْرٌۭ وَأَبْقَىٰٓ». From memory: some early authorities read 87:14–15 as paying the alms of the fast-breaking and then praying the feast prayer.
- 87:14 أَفْلَحَ · ف ل ح B001 · «فلحت الأرض شققتها» (maqayis;sihah;tahdhib) · splitting the ground.
- 87:14 أَفْلَحَ · ف ل ح B003 · «سمي الأكار فلاحا لأنه يشق الأرض» (maqayis;jamhara;sihah;tahdhib;mufradat) · the ploughman.
- 87:14 أَفْلَحَ · ف ل ح B005 · «الفلاح والفلح البقاء في الخير» (ayn;tahdhib); «الفلاح الفوز والنجاة والبقاء» (sihah) · success is remaining in good. The phrase joins فلح with بقي and خير (87:17).
- 87:14 تَزَكَّىٰ · ز ك و B001 · «زكا الزرع يزكو زكاء ازداد ونما» (ayn); «أصل الزكاة النمو الحاصل عن بركة الله تعالى» (mufradat) · the crop's growth.
- 87:14 تَزَكَّىٰ · ز ك و B003 · «زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق» (sihah) · the share given out.
- 87:14 تَزَكَّىٰ · ز ك و B002 · «الطهارة زكاة المال؛ زكاة لأنها طهارة» (maqayis) · the share given out cleanses what is left.
- 87:4 أَخْرَجَ · خ ر ج B003 · «الخراج الغلة» (tahdhib); «الخرج والخراج ما يخرج من المال في السنة بقدر معلوم» (ayn;tahdhib) · the yield, by a known measure. The phrase joins خرج with قدر (87:3).
- 87:1/87:15 رَبِّ · ر ب ب B002 · «رب الضيعة أي أصلحها وأتمها» (sihah); «رب فلان ضيعته إذا قام على إصلاحها» (maqayis) · the owner who tends the farm to completion.
- 87:17 أَبْقَىٰٓ · ب ق ي B002 · «الباقي حاصل الخراج ونحوه» (tahdhib) · what is left of the yield. This joins بقي with خراج.
- Quran: 80:24–32 (God tells man to look at his food: water poured, «ثم شققنا الأرض شقا», grain and pasture «متاعا لكم ولأنعامكم»). 56:63–65 («أفرأيتم ما تحرثون»). 42:20 (God's speech: whoever wants «حرث الآخرة» has it increased; whoever wants «حرث الدنيا» is given some, «وما له في الآخرة من نصيب»). 91:7–10 (the oath sequence that opens at 91:1: «ونفس وما سواها ... قد أفلح من زكاها»). 92:18 («الذي يؤتي ماله يتزكى»). 6:141 («وآتوا حقه يوم حصاده»). 48:29 («كزرع أخرج شطأه»). 23:1–4 («قد أفلح المؤمنون ... والذين هم للزكاة فاعلون»).

### 5. The herd at pasture: owned, led, grazed, watched
87:1–4 run ربّ, then هدى, then المرعى. The dictionary sets this up as a herding scene. The ربّ owns, governs and sets things right. The «هوادي» are the lead animals at the front of a herd. The راعي guards the grazing animals and watches where things are heading. The camels have a haunt they keep to. From memory, Mujāhid explained 87:3 in part as guiding the cattle to their pastures.
- 87:1/87:15 رَبِّ · ر ب ب B001 · «رب كل شئ: مالكه» and «رببت القوم: سستهم» (sihah); «ويكون الرب: المصلح» (tahdhib) · owner, manager, the one who sets things right.
- 87:1/87:15 رَبِّ · ر ب ب B007 · «مرب الإبل حيث لزمته» (sihah) · the place the camels keep to.
- 87:1/87:15 رَبِّ · ر ب ب B014 · «الربرب: القطيع من بقر الوحش» (sihah) · a herd of wild cattle.
- 87:3 فَهَدَىٰ · ه د ي B003 · «الهاديات أوائل الوحش» (sihah); «هوادي الوحش متقدماتها الهادية لغيرها» (mufradat) · the front animals that lead the rest.
- 87:4 ٱلْمَرْعَىٰ · ر ع ي B002 · «الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته» (tahdhib) · the herder guards the flock, and the governor his people.
- 87:4 ٱلْمَرْعَىٰ · ر ع ي B003 · «راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها» (maqayis) · watching where a thing ends up; watching the stars.
- 87:4 ٱلْمَرْعَىٰ · ر ع ي B007 · «الإبل التي ترعى حوالي القوم وديارهم» (sihah) · the working camels that graze around the camp.
- Quran: 20:53–54 (Moses to Pharaoh: plants brought out, «كلوا وارعوا أنعامكم»; the scene opens at 20:49 «فمن ربكما يا موسى», with 20:50 «ربنا الذي أعطى كل شيء خلقه ثم هدى»). 79:31–33. 80:31–32.

### 6. The shaft: measured, smoothed, straightened, headed
87:2–3 run خلق, فسوّى, قدّر, فهدى. In the dictionary these are the steps of shaping a shaft. خلق is first measuring and then smoothing: an arrow that has been finished is «مخلق أملس مستو». سوّى is straightening out a bend. قدّر is measuring, and thinking out how to make something even. A staff is straightened by turning it over a fire. The «هادي» of an arrow is its head, and a staff is «هاديا» because it goes in front of the man holding it. The ربّ is the one who sets a thing right and brings it to completion stage by stage.
- 87:2 خَلَقَ · خ ل ق B001 · «الخلق أصله: التقدير المستقيم» (mufradat) · straight measuring. The phrase joins خلق with قدر and with straightness.
- 87:2 خَلَقَ · خ ل ق B008 · «السهم المصلح مخلق لأنه يصير أملس» (maqayis); «سهم مخلق أملس مستو» (tahdhib) · the finished arrow, smooth and even. The tahdhib phrase joins خلق and سوي.
- 87:2 فَسَوَّىٰ · س و ي B002 · «سويت الشيء فاستوى» (ayn;sihah); «استوى من اعوجاج» (sihah;tahdhib) · made straight out of a bend.
- 87:3 قَدَّرَ · ق د ر B005 · «التروية والتفكير في تسوية أمر وتهيئته» (tahdhib) · thinking out how to even a thing and get it ready. The phrase joins قدر and سوي.
- 87:3 قَدَّرَ · ق د ر B001 · «مبلغ الشيء وكنهه ونهايته» (maqayis) · the measure a thing reaches.
- 87:12 يَصْلَى · ص ل ي B004 · «صلى عصاه إذا أدارها على النار يثقفها» (ayn;tahdhib); ص ل و B001 «صليت العود بالنار» (maqayis) · fire used to straighten wood.
- 87:3 فَهَدَىٰ · ه د ي B003 · «هادي السهم نصله» (sihah); «العصا هاديا لأنها تتقدمه» (ayn) · the head that goes first.
- 87:1/87:15 رَبِّ · ر ب ب B002 · «رب الشيء أي أصلحه» (tahdhib); «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» (mufradat) · the maker who brings it to completion step by step.
- Quran: 80:19–20 (God on man: «من نطفة خلقه فقدره ثم السبيل يسره»; the scene opens at 80:17). 25:2 («وخلق كل شيء فقدره تقديرا»). 54:49 («إنا كل شيء خلقناه بقدر»). 20:50.

### 7. The hide cut for a waterskin
The dictionary's first example for خلق is a leatherworker sizing up a hide for a waterskin before he cuts it. The tahdhib entry for نفع then describes the finished vessel: the hide is split and a piece called نفعة is set into each of its two sides (جانب). The skin is seasoned with رُبّ (thick syrup or ghee), churned (جهر), and in the end worn smooth. Five of the surah's roots (خلق, قدر, نفع, جنب, رب) meet on this one object.
- 87:2 خَلَقَ · خ ل ق B001 · «خلقت الأديم للسقاء إذا قدرته» (maqayis); «خلقت الأديم إذا قدرته قبل القطع» (sihah) · sizing the hide before the cut. The dictionary joins خلق with قدّر (87:3).
- 87:9 نَّفَعَتِ · ن ف ع B002 · «النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة» (tahdhib) · side pieces set into a split hide. The phrase joins نفع with ج ن ب (جانب), and its «الأديم» is the same hide as in خلق.
- 87:11 يَتَجَنَّبُهَا · ج ن ب B001 · «الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء» (ayn) · the vessel's two sides.
- 87:1/87:15 رَبِّ · ر ب ب B006 · «رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب» (mufradat); «الرب للعنب وغيره لأنه يرب به الشيء» (maqayis) · the hide treated so the skin holds well.
- 87:7 ٱلْجَهْرَ · ج ه ر B010 [fixed expression] · «جهرت السقاء مخضته» (sihah) · churning the skin.
- 87:2 خَلَقَ · خ ل ق B009 · «أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره» (maqayis) · the leather worn smooth with use.
- Quran: no passage stages this object.

### 8. The body formed: gathered in the womb, made even, raised to completion
The forming verbs of 87:2–3 also have bodily senses in the dictionary. قرأ, the root of 87:6, is the womb closing round its young. خلق is the embryo that has taken full form. سوّى is a body made even, without flaw or illness, and استوى is youth reaching its full strength. قدّر sets each thing to its own measure. ربّ is rearing a child step by step. أدنت (the root of الدنيا) is the birth drawing near, and كبر is growing old. 75:38 has the surah's exact pair «فخلق فسوى» for the embryo. From memory: one early reading of 87:3 is that God guided the newborn to the breast and each creature to what suits it.
- 87:6 سَنُقْرِئُكَ · ق ر ء B004 · «لم تضم رحمها على ولد» (sihah); «ما قرأت الناقة سلى قط وما قرأت ملقوحا قط» (tahdhib) · the womb that gathers, or never gathered, a young one.
- 87:2 خَلَقَ · خ ل ق B003 · «مضغة مخلقة أي تامة الخلق» (sihah); «مخلقة قد بدا خلقها وغير مخلقة لم تصور» (tahdhib) · the embryo whose form has appeared.
- 87:2 فَسَوَّىٰ · س و ي B002 · «السوي الذي سوى الله خلقه لا دمامة فيه ولا داء» (ayn) · a body made even, without flaw.
- 87:2 فَسَوَّىٰ · س و ي B005 · «استوى الرجل إذا انتهى شبابه» (sihah) · reaching full growth.
- 87:3 قَدَّرَ · ق د ر B002 · «يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة» (mufradat) · each thing set to its own measure.
- 87:1/87:15 رَبِّ · ر ب ب B002 · «رببت الصبي أربه» (maqayis); «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» (mufradat) · rearing in stages.
- 87:16 ٱلدُّنْيَا · د ن و B004 [fixed expression] · «أدنت الناقة إذا دنا نتاجها» (sihah) · the birth coming close.
- 87:12 ٱلْكُبْرَىٰ · ك ب ر B004 · «الكبر في السن وقد كبر الرجل أي أسن» (sihah) · old age at the end.
- Quran: 75:37–39 (God's speech: drop, clot, «فخلق فسوى», then the pair; the scene opens at 75:36). 82:6–8 («الذي خلقك فسواك فعدلك»). 22:5 («مخلقة وغير مخلقة»). 32:7–9 («ثم سواه ونفخ فيه من روحه»). 80:18–20. 91:7. 20:50.

### 9. Lot arrows and the measured share
Three of the surah's words name parts of the maysir, the pre-Islamic draw with arrows over a slaughtered camel. The ربابة is the bag the arrows are kept in. المعلى is the seventh arrow, which takes the largest share. الميسر is the game itself, in which the players divide the camel's parts. A shaft made smooth is «مخلق». خلاق is a person's share "because each one's share was measured", and the dictionary uses it in «لا خلاق له في الآخرة». The scene ends on the surah's own contrast: a share in the near life against a share in the later one (87:16–17).
- 87:1/87:15 رَبِّ · ر ب ب B010 · «الربابة شبيهة بالكنانة تجمع فيها سهام الميسر» (sihah) · the arrow bag. The phrase joins رب and ي س ر (87:8).
- 87:1 ٱلْأَعْلَى · ع ل و B009 · «المعلى السابع من القداح» (maqayis;sihah;mufradat) · the highest arrow, which takes the largest share.
- 87:8 لِلْيُسْرَىٰ · ي س ر B007 · «الميسر: قمار العرب بالأزلام» and «يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها» (sihah) · the game and the dividing of the camel.
- 87:2 خَلَقَ · خ ل ق B008 · «المخلق القدح إذا لين» (sihah) · the arrow shaft made smooth.
- 87:2 خَلَقَ · خ ل ق B006 · «الخلاق النصيب لأنه قد قدر لكل أحد نصيبه» (maqayis); «لا خلاق له في الآخرة» (sihah) · the measured share. The phrases join خلق with قدر (87:3) and with الآخرة (87:17).
- 87:3 قَدَّرَ · ق د ر B001 · «لكل شيء مقدار وأجل» (ayn) · every share has its amount.
- Quran: 2:200 (in the Hajj passage: some ask only for this world, «وما له في الآخرة من خلاق»). 9:69 (earlier peoples «فاستمتعوا بخلاقهم ... حبطت أعمالهم في الدنيا والآخرة»). 42:20 («وما له في الآخرة من نصيب»). 5:90 and 2:219 (the maysir and the divining arrows forbidden). 5:3 («وأن تستقسموا بالأزلام»).

### 10. The brand: a mark burned into the hide
The dictionary records a second derivation of اسم, from وسم: the brand burned into a camel's hide so that it can be known. The surah's other words carry the same scene. نار also means the brand itself; «نجارها نارها» says an animal's lineage shows in its brand. أثر includes the mark scored into a camel's foot so its tracks can be followed. علم is "a mark on a thing that sets it apart". توسّم is reading good or evil off someone's face. The ربّ is the owner whose mark it is.
- 87:1/87:15 ٱسْمَ · و س م B001 (documented alternative derivation) · «الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي» (ayn); «الميسم المكواة أو الشيء الذي يوسم به الدواب» (ayn;sihah;tahdhib) · the brand and the branding iron. «أثر كي» joins وسم with أثر (87:16).
- 87:12 ٱلنَّارَ · ن و ر B002 · «ما نار هذه الناقة أي ما سمتها؛ نجارها نارها» (sihah) · fire as brand. The phrase joins نار with سمة, the root of وسم.
- 87:16 تُؤْثِرُونَ · ء ث ر B008 · «المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض» (tahdhib) · the foot-mark that makes tracks readable.
- 87:16 تُؤْثِرُونَ · ء ث ر B003 · «الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة» (maqayis) · the trace that remains. The phrase joins أثر with بقي (87:17).
- 87:7 يَعْلَمُ · ع ل م B002 · «أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره» (maqayis) · the mark that sets a thing apart. Again joined with أثر.
- 87:1/87:15 ٱسْمَ · و س م B002 · «توسمت فيه الخير والشر أي رأيت فيه أثرا» (ayn) · reading the mark of good or evil on someone. The phrase joins وسم, خير (87:17) and أثر.
- 87:1/87:15 رَبِّ · ر ب ب B001 · «رب كل شئ: مالكه» (sihah) · the owner the mark identifies.
- Quran: 68:16 (God's threat to the slanderer: «سنسمه على الخرطوم»; the scene opens at 68:10). 15:75 («إن في ذلك لآيات للمتوسمين», after the ruin of Lot's people).

### 11. Fire seen from afar: beacon, warming, roasting
The النار of 87:12 shares its root with light: «النور والنار سميا بذلك من طريقة الإضاءة». The dictionary sets out the ways one can come to a fire. One sees it in the distance and heads for it (تنوّر). One follows it as a beacon «ليهتدى». One warms oneself at it (اصطلى). Or one is thrust into it and suffers its heat (صلي النار), as meat is roasted. Moses, whose sheets close the surah (87:19), saw a fire, hoped for a brand from it or for «هدى» at it, went to warm himself, and was told «أقم الصلاة لذكري». His story moves from the fire to prayer and remembrance. The wretched of 87:12 enters the great fire instead. From memory: early commentators set «النار الكبرى» against «النار الصغرى», the fire of this world.
- 87:12 ٱلنَّارَ · ن و ر B003 [fixed expression] · «تنورت نارا قصدت إليها» (ayn); «تنورت النار من بعيد: تبصرتها» (sihah) · making for a fire seen in the distance.
- 87:12 ٱلنَّارَ · ن و ر B005 · «كانوا ينورون في الجاهلية ليهتدى ويقتدى بها» (ayn); «المنار: علم الطريق» (sihah) · the fire as beacon. The ayn phrase joins نور with هدى (87:3); the sihah phrase joins it with علم (87:7).
- 87:12 ٱلنَّارَ · ن و ر B001 · «النور والنار سميا بذلك من طريقة الإضاءة» (maqayis) · fire and light are one root.
- 87:12 يَصْلَى · ص ل ي B004 · «الصلاء ما يصطلى به وما يذكى به النار ويوقد» (maqayis); ص ل و B001 «اصطليت بالنار» (maqayis;sihah) · warming at the fire.
- 87:12 يَصْلَى · ص ل ي B003 · «صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها» (ayn); «صلي الرجل نارا إذا أدخلته النار» (sihah) · being put into the fire and enduring its heat.
- 87:12 يَصْلَى · ص ل ي B004 · «صليت اللحم صليا شويته» (ayn;sihah;tahdhib) · roasting.
- 87:12 ٱلْكُبْرَىٰ · ك ب ر B001 · «كبر كل شيء عظمه» (ayn) · the greatest fire.
- 87:3 فَهَدَىٰ · ه د ي B001 · «دله على الطريق» (tahdhib) · the guidance hoped for at the fire.
- 87:15 فَصَلَّىٰ · ص ل و B003 · «الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة» (maqayis) · where Moses' approach to the fire ends.
- Quran: 20:9–14 (Moses tells his family «إني آنست نارا لعلي آتيكم منها بقبس أو أجد على النار هدى»; then «فاعبدني وأقم الصلاة لذكري»). 27:7 («لعلكم تصطلون»). 28:29 (the fire seen «من جانب الطور ... لعلكم تصطلون»). 56:71–73 (the fire people kindle: «نحن جعلناها تذكرة»). 4:56 («سوف نصليهم نارا كلما نضجت جلودهم بدلناهم جلودا غيرها»). 74:26–28 («سأصليه سقر ... لا تبقي ولا تذر»). 74:42–43 (the people of Saqar: «لم نك من المصلين»). 92:14–16 («نارا تلظى لا يصلاها إلا الأشقى»).

### 12. Neither dead nor alive; the life that remains
87:13 says of the wretched man in the fire that he neither dies nor lives. 87:16 then names the near life and 87:17 what remains. The dictionary fills in the states between. Death is "strength leaving a thing". There is a swoon one wakes from, and sleep. "No life in him" means no benefit and no good in him. "Sparing alive" is glossed as "keeping remaining". The true life (الحيوان) is defined as "the seat of life ... and what has lasting permanence".
- 87:13 يَمُوتُ · م و ت B001 · «أصل صحيح يدل على ذهاب القوة من الشيء» (maqayis) · strength leaving.
- 87:13 يَمُوتُ · م و ت B009 · «الموتة الذي يصرع من الجنون أو غيره ثم يفيق» (tahdhib) · a death-like fit one comes back from.
- 87:13 يَمُوتُ · م و ت B012 [fixed expression] · «مات الرجل وهمد وهوم إذا نام» (tahdhib) · sleep as stillness.
- 87:13 يَحْيَىٰ · ح ي ي B013 · «ليس بفلان حياة أي ليس عنده نفع ولا خير» (tahdhib); «ومن أحياها أي من نجاها من الهلاك» (mufradat) · life as benefit and good. The tahdhib phrase joins حياة with نفع (87:9) and خير (87:17).
- 87:13 يَحْيَىٰ · ح ي ي B006 · «ويستحيون نساءكم أي يستبقونهن» (mufradat) · sparing alive. The phrase joins حيي and بقي (87:17).
- 87:16 ٱلْحَيَوٰةَ · ح ي ي B003 · «الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي» (mufradat) · true life, which lasts.
- 87:16 ٱلْحَيَوٰةَ · ح ي و B003 (documented alternative) · «والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله» (ayn) · the water of life in the Garden.
- 87:17 أَبْقَىٰٓ · ب ق ي B001 · «بقى الشيء يبقى بقاء وبقي الرجل زمانا طويلا أي عاش» (sihah) · remaining as living on.
- 87:17 أَبْقَىٰٓ · ب ق ي B003 · «العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا» (tahdhib) · sparing from destruction.
- 87:16 ٱلدُّنْيَا · د ن و B002 · «سميت الدنيا لدنوها» (maqayis;sihah) · the near life.
- Quran: 20:74 (Pharaoh's magicians: the guilty get Hell, «لا يموت فيها ولا يحيى»; the scene opens at 20:70). 14:16–17 («ويأتيه الموت من كل مكان وما هو بميت»). 35:36. 4:56. 74:28 («لا تبقي ولا تذر»). 29:64 («وإن الدار الآخرة لهي الحيوان»). 89:23–24 («يا ليتني قدمت لحياتي»).

### 13. Height: the name that raises, the Most High, the low near life
The surah opens on height. In the dictionary اسم comes from سموّ, "rising": a name is what raises the mention of the thing named. علو is defined through سموّ, and ذكر includes «العلاء والشرف». So in 87:1 the name, the Most High and (in 87:15) the mention all point upward. The root also gives the picture of a figure rising into view and the new moon lifting off the horizon. تسبيح clears God of every flaw, and the «سبحات» of His face are His majesty and light. Height can also be the arrogant kind (علا في الأرض), Pharaoh's «أنا ربكم الأعلى». At the other end, 87:16's الدنيا is the nearer and lower life, and the dictionary also explains أدنى as "the smaller" and "the meaner".
- 87:1/87:15 ٱسْمَ · س م و B005 · «أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى» (maqayis); «الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى» (mufradat) · the name raises the mention. The phrases join اسم with علو and ذكر.
- 87:1/87:15 ٱسْمَ · س م و B002 · «سما لي شخص ارتفع حتى استثبته» (maqayis); «سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا» (ayn) · a figure rising until it is clearly seen; the crescent lifting off the horizon.
- 87:1 ٱلْأَعْلَى · ع ل و B001 · «أصل واحد يدل على السمو والارتفاع» (maqayis) · height. The dictionary defines علو by سمو.
- 87:1 ٱلْأَعْلَى · ع ل و B006 · «تعال أصله أن يدعى الإنسان إلى مكان مرتفع» (mufradat) · the call to come up.
- 87:1 ٱلْأَعْلَى · ع ل و B003 · «علا ملك في الأرض أي طغى وتعظم» (ayn) · height turned to tyranny: the reversal.
- 87:15 وَذَكَرَ · ذ ك ر B007 · «الذكر العلاء والشرف» (maqayis) · mention as height and honour.
- 87:1 سَبِّحِ · س ب ح B002 · «التسبيح وهو تنزيه الله من كل سوء» (maqayis) · clearing God of every flaw.
- 87:1 سَبِّحِ · س ب ح B003 · «سبحات وجه ربنا يعني جلاله وعظمته ونوره» (ayn) · majesty and light. The phrase joins سبح, رب and نور (the root of النار).
- 87:12 ٱلْكُبْرَىٰ · ك ب ر B009 · «التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر» (mufradat) · the word of the great fire is also the word of magnifying God.
- 87:12 ٱلْكُبْرَىٰ · ك ب ر B006 · «الكبر العظمة وكذلك الكبرياء» (maqayis) · greatness, and greatness claimed.
- 87:16 ٱلدُّنْيَا · د ن و B002/B003 · «يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب» (mufradat); «الدني من الرجال الضعيف الدون» (maqayis) · the lower, smaller, nearer pole.
- Quran: 79:24 (Pharaoh to his people: «أنا ربكم الأعلى»; the scene opens at 79:15 «هل أتاك حديث موسى»). 20:68 (God to Moses before the magicians: «إنك أنت الأعلى»). 20:4 («والسماوات العلى»). 20:114 («فتعالى الله»). 92:19–20 («ابتغاء وجه ربه الأعلى»; the scene opens at 92:17). 24:36 («في بيوت أذن الله أن ترفع ويذكر فيها اسمه يسبح له فيها»). 94:4 («ورفعنا لك ذكرك»). 96:1. 56:74. 55:78.

### 14. Glorify, remember, pray: the act that opens and closes the surah
The command of 87:1 («سَبِّحِ ٱسْمَ رَبِّكَ») comes back in 87:15 («وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ»). The dictionary treats the three verbs as one practice. A single phrase joins تسبيح, ذكر and صلاة. Another defines ذكر as reciting, glorifying and supplicating. A third breaks the prayer into standing, bowing, prostrating, supplication and glorifying. One more has a person voicing his words, his prayer and his recitation aloud. The prayer's body is concrete: the «سبحات» are the places of prostration, and the صلا is the middle of the back. From memory: some derived صلاة from moving the صَلَوان (the two sides of the tail-bone) in bowing. The mufradat also defines God's صلاة on believers as His تزكية of them, which joins 87:15 to 87:14.
- 87:1 سَبِّحِ · س ب ح B001 · «السبحة التطوع من الذكر والصلاة» (sihah); «السبحة وهي الصلاة» (maqayis); «التسبيح عاما في العبادات قولا كان أو فعلا أو نية» (mufradat) · glorifying as voluntary remembrance and prayer. The sihah phrase joins سبح with ذكر and صلاة (87:15).
- 87:1 سَبِّحِ · س ب ح B003 · «السبحات مواضع السجود» (tahdhib) · the places where the forehead touches the ground.
- 87:15 وَذَكَرَ · ذ ك ر B005 · «الذكر الصلاة والدعاء والثناء» (ayn;tahdhib); «الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة» (tahdhib) · remembrance as prayer, recitation and glorifying. The phrase joins ذكر with قرأ (87:6), سبح (87:1) and صلاة.
- 87:15 وَذَكَرَ · ذ ك ر B004 · «الذكر جري الشيء على لسانك» (ayn;tahdhib) · the name on the tongue.
- 87:15 فَصَلَّىٰ · ص ل و B003 · «الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح» (tahdhib) · the parts of the prayer. The phrase joins صلاة and تسبيح.
- 87:15 فَصَلَّىٰ · ص ل و B002 · «الصلاة وهي الدعاء» (maqayis;sihah); «صلاة الله للمسلمين تزكيته إياهم» (mufradat) · prayer as supplication; God's صلاة as تزكية (87:14).
- 87:15 فَصَلَّىٰ · ص ل و B005 · «الصلا وسط الظهر لكل ذي أربع وللناس» (ayn) · the middle of the back that bends.
- 87:7 ٱلْجَهْرَ · ج ه ر B001 · «جهر بكلامه وصلاته وقراءته» (ayn) · the prayer and recitation voiced. The phrase joins جهر, صلاة and قراءة.
- Quran: 24:36–37 (the raised houses: name remembered, glorifying, men not distracted «عن ذكر الله وإقام الصلاة وإيتاء الزكاة»). 20:14 («وأقم الصلاة لذكري»). 20:130 («وسبح بحمد ربك»). 62:9–10 (the Friday call: «إلى ذكر الله ... واذكروا الله كثيرا لعلكم تفلحون»). 23:1–4. 96:1 («اقرأ باسم ربك»). 7:205.

### 15. Gathered, kept, dropped: recitation, memory and the sheets
87:6–10 and 87:18–19 picture memory as a set of containers. قرأ is to gather a thing and put its parts together. Recitation is putting letters and words together. To be made to recite (أقرأ) is to be given that gathering. نسي is losing hold of what was entrusted, or leaving it. النِّسي is the worthless scraps that fall behind at an abandoned camp. ذكر is the opposite of forgetting: it means keeping, and seeking what has slipped away. ذكر is also the book of a prophet. The صحف are pieces of white leather or parchment, and the مصحف is what gathers the written sheets together. أثر is a report passed on from someone else.
- 87:6 سَنُقْرِئُكَ · ق ر ء B001 · «قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض» (sihah); «القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل» (mufradat) · gathering and joining.
- 87:6 سَنُقْرِئُكَ · ق ر ء B002 · «أقرأت غيري أقرئه إقراء» (tahdhib) · making another person recite.
- 87:6 تَنسَىٰٓ · ن س ي B001 · «ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد» (mufradat); «النسيان خلاف الذكر والحفظ» (sihah) · losing hold of a trust.
- 87:6 تَنسَىٰٓ · ن س ي B002 · «النسيان الترك، نسوا الله فنسيهم» (sihah) · leaving behind.
- 87:6 تَنسَىٰٓ · ن س ي B003 · «النسي ما سقط من منازل المرتحلين من رذال أمتعتهم» (maqayis) · the dropped scraps at an abandoned camp.
- 87:9/87:10/87:15 ذَكِّرْ, ٱلذِّكْرَىٰ, يَذَّكَّرُ, ذَكَرَ · ذ ك ر B003 · «ذكرت الشيء خلاف نسيته» (maqayis;sihah); «الذكر الحفظ للشيء وهو مني على ذكر» (ayn;tahdhib); «ذكر بالقلب والتذكر طلب ما فات» (ayn;tahdhib;mufradat) · keeping, and seeking what has slipped. The dictionary joins ذكر and نسي in one phrase.
- 87:9 ٱلذِّكْرَىٰ · ذ ك ر B009 · «التذكرة ما تستذكر به الحاجة» (sihah) · the thing that brings the need back to mind.
- 87:9 ٱلذِّكْرَىٰ · ذ ك ر B006 · «الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر» (ayn;tahdhib); «القرآن والكتب المتقدمة والزبور من بعد الذكر» (mufradat) · the reminder as a prophet's book. This joins 87:9 with the sheets of 87:18–19.
- 87:18/87:19 ٱلصُّحُفِ · ص ح ف B002 · «الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها» (jamhara) · leather writing sheets.
- 87:18/87:19 ٱلصُّحُفِ · ص ح ف B003 · «المصحف ما جعل جامعا للصحف المكتوبة» (mufradat) · the sheets gathered into one.
- 87:18 ٱلْأُولَىٰ · ء و ل B001 · «الأول وهو مبتدأ الشيء» (maqayis) · the first sheets.
- 87:16 تُؤْثِرُونَ · ء ث ر B002 · «أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور» (sihah) · a report handed down. The phrase joins أثر and ذكر.
- Quran: 75:16–19 (God to the Prophet: «لا تحرك به لسانك لتعجل به إن علينا جمعه وقرآنه فإذا قرأناه فاتبع قرآنه»). From memory: reports say the Prophet hurried to repeat revelation for fear of forgetting it. 20:114 («ولا تعجل بالقرآن»). 20:115 (Adam «فنسي»). 20:52 (Moses: «في كتاب لا يضل ربي ولا ينسى»). 20:126 («أتتك آياتنا فنسيتها وكذلك اليوم تنسى»). 2:106. 18:24. 59:19. 9:67. 53:36–37 («صحف موسى وإبراهيم الذي وفى»; their contents run to 53:54). 20:133 («ما في الصحف الأولى»). 80:11–16 («في صحف مكرمة مرفوعة مطهرة»). 26:196. 21:105.

### 16. Aloud and hidden: the voice
87:7 sets الجهر (what is said aloud) against what stays hidden. In the dictionary the scene is one of speaking. جهر is raising the voice in speech, prayer and recitation. خفي is keeping the voice low, and is the opposite of open declaration. ذكر is remembrance on the tongue and in the heart. The two ends of the voice match the two places remembrance lives.
- 87:7 ٱلْجَهْرَ · ج ه ر B001 · «جهر بالقول رفع به صوته» (sihah); «جهر بكلامه وصلاته وقراءته» (ayn); «الجهر ضد السر» (jamhara) · the raised voice.
- 87:7 ٱلْجَهْرَ · ج ه ر B011 [fixed expression] · «سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه» (sihah) · the voiced letter, down to the scale of a single sound.
- 87:7 يَخْفَىٰ · خ ف ي B001 · «أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا» (ayn) · the lowered voice; secrecy.
- 87:15 وَذَكَرَ · ذ ك ر B004 · «ذكرته بلساني وبقلبي» (sihah) · tongue and heart.
- 87:6 سَنُقْرِئُكَ · ق ر ء B002 · «قرأت القرآن عن ظهر قلب أو نظرت فيه» (ayn) · reciting from memory.
- 87:7 يَعْلَمُ · ع ل م B001 · «ما علمت بخبرك أي ما شعرت به» (ayn;tahdhib) · knowing as being aware of what is said.
- Quran: 20:7 (God to the Prophet at the opening of Ṭā Hā: «وإن تجهر بالقول فإنه يعلم السر وأخفى»). 17:110 («ولا تجهر بصلاتك ولا تخافت بها»). 7:205 («واذكر ربك في نفسك تضرعا وخيفة ودون الجهر من القول»). 7:55 («تضرعا وخفية»). 21:110 («إنه يعلم الجهر من القول»). 6:3.

### 17. Brought out from cover
Read with 87:4, 87:7's pair becomes a scene of things coming out of hiding. In the dictionary خفي is one of the words that carry opposite senses: «خفيته» can mean "I brought it out". Its example is rain driving mice from their holes, and the dictionary explains it with أخرج. Other members are the inner fronds at a palm's heart, the inner feathers under a wing, a well cleared until its water shows, and «كل شيء بدا فقد جهر». The reversal is the eye that cannot see in sunlight, hidden from by too much light.
- 87:4 أَخْرَجَ · خ ر ج B001 · «خرج خروجا برز من مقره أو حاله» (mufradat) · coming out of its place.
- 87:7 يَخْفَىٰ · خ ف ي B003 · «خفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن» (maqayis); «استخفيت الشئ أي استخرجته» (sihah) · bringing out of cover. Both phrases join خفي with خرج.
- 87:7 يَخْفَىٰ · خ ف ي B002 · «الخوافي سعفات يلين قلب النخلة» (maqayis); «الخوافي جمع خافية وهي ما دون القوادم من الريش» (mufradat) · the covered parts of a palm and a wing.
- 87:7 ٱلْجَهْرَ · ج ه ر B002 · «كل شيء بدا فقد جهر» (ayn); «إعلان الشيء وكشفه» (maqayis) · whatever shows.
- 87:7 ٱلْجَهْرَ · ج ه ر B008 [fixed expression] · «جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو» (sihah) · water uncovered.
- 87:7 ٱلْجَهْرَ · ج ه ر B004 · «العين الجهراء التي لا تبصر في الشمس» (maqayis) · the reversal: sight lost in too much light.
- Quran: 27:25 (the hoopoe to Solomon, from memory: «ألا يسجدوا لله الذي يخرج الخبء في السماوات والأرض ويعلم ما تخفون وما تعلنون»). 20:7.

### 18. The road and the mount: led in front, made easy, climbed, steered aside
87:3, 87:8 and 87:11 trace a journey. هدى is going ahead to show the way: the guide, or the staff carried in front. يسر is the mount that is easy to lead, quick to follow, light-legged. شقو is hardship, but the dictionary also gives الشاقي, a long mountain ridge that is "easier to climb, and better to sit on" for its length. That one ayn phrase holds شقي, يسر and قدر together. The rider settles on the animal's back (استوى ... علا), on a padded saddle cloth that jamhara compares to the حوية: a phrase holding سوّى (87:2) and أحوى (87:5). One kind of leading is جنب, leading an animal at your side. Another is the تجنّب of 87:11, keeping the thing off to one side. سواء is the middle ground, and also «سواء الجحيم», the middle of Hell. The weak walk propped between two people (يهادى), and a calm unhurried pace is «هدي حسن».
- 87:3 فَهَدَىٰ · ه د ي B001 · «هديته الطريق والبيت هداية أي عرفته» (sihah); «التقدم للإرشاد» (maqayis) · showing the road by going ahead.
- 87:3 فَهَدَىٰ · ه د ي B003 · «العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه» (ayn) · staff and guide go in front.
- 87:3 فَهَدَىٰ · ه د ي B008 · «يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله» (sihah) · the weak walking propped up.
- 87:3 فَهَدَىٰ · ه د ي B010 · «لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن» (ayn) · a calm, unhurried pace.
- 87:8 نُيَسِّرُكَ لِلْيُسْرَىٰ · ي س ر B001 · «الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ» (sihah) · the way made easy and ready.
- 87:8 نُيَسِّرُكَ لِلْيُسْرَىٰ · ي س ر B005 · «ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس» (ayn); «اليسرات: القوائم الخفاف» (sihah) · the easy-led, light-legged mount.
- 87:8 لِلْيُسْرَىٰ · ي س ر B004 · «اليسار لليد، تياسروا إذ أخذوا ذات اليسار» (maqayis) · taking the left-hand way: a turn of direction on the same road.
- 87:11 ٱلْأَشْقَى · ش ق و B004 · «الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان» (ayn) · the long ridge, easier to climb. The phrase joins شقو, يسر (87:8) and قدر (87:3).
- 87:11 ٱلْأَشْقَى · ش ق و B002 · «أصل يدل على المعاناة وخلاف السهولة» (maqayis) · toil, the opposite of ease.
- 87:11 يَتَجَنَّبُهَا · ج ن ب B005 · «جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير» (maqayis;jamhara); «من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك» (mufradat) · leading at the side. The mufradat applies it to Abraham's prayer.
- 87:11 يَتَجَنَّبُهَا · ج ن ب B003 · «جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه» (sihah) · keeping something off to one side.
- 87:2 فَسَوَّىٰ · س و ي B003 [fixed expression] · «استوى على ظهر دابته أي علا واستقر» (sihah) · the rider settles on top. The phrase joins سوي and علو (87:1).
- 87:2 فَسَوَّىٰ · س و ي B010 · «السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير» (jamhara) · the saddle pad. The phrase joins سوّى (87:2) and أحوى (87:5).
- 87:5 أَحْوَىٰ · ح و ي B004 · «الحوية كساء يحوي حول سنام البعير ثم يركب» (maqayis;tahdhib) · the cloth wrapped round the hump for riding.
- 87:2 فَسَوَّىٰ · س و ي B006 · «مكان سوى أي عدل ووسط» (sihah); «في سواء الجحيم» (maqayis;mufradat) · the middle of the road, and the middle of Hell.
- Quran: 92:5–10 (after the oaths that open at 92:1: «فسنيسره لليسرى ... فسنيسره للعسرى»). 92:12 («إن علينا للهدى»). 80:20 («ثم السبيل يسره»). 90:10–11 («وهديناه النجدين فلا اقتحم العقبة»). 74:17 («سأرهقه صعودا»). 20:123 («فمن اتبع هداي فلا يضل ولا يشقى»). 20:2. 76:3. 14:35 (Abraham's prayer, «واجنبني وبني أن نعبد الأصنام», which the mufradat's phrase points to). 37:55 («فرآه في سواء الجحيم»).

### 19. The moving file: front, follower, rear, and the horse that holds back
The time words of 87:16–18 also name places in a moving line of horses or camels. The سابح is the horse that stretches its forelegs as it runs. The «هوادي» are the leaders. The مصلّي is the second horse, whose head is at the leader's croup. آثر is putting first, and also following in someone's tracks. The دنيا is the nearer bank. «أخرى القوم» are those at the back, and «آخرة الرحل» is the rear post of the saddle. The ناقة أولة is the she-camel at the front. The «مبقيات» are horses that hold back part of their running for later. Read through this scene, 87:16–17 says that what you put first is the nearer thing, while the later one is better and holds out longer.
- 87:1 سَبِّحِ · س ب ح B004 · «السابح من الخيل يمد يديه في الجري؛ النجوم تسبح في الفلك» (tahdhib) · the running horse; the stars sailing along their courses.
- 87:3 فَهَدَىٰ · ه د ي B003 · «هوادي الخيل أعناقها أو أول رعيل» (sihah) · the leading band.
- 87:15 فَصَلَّىٰ · ص ل و B006 · «قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه» (ayn); «السابق الأول والمصلي الثاني» (tahdhib) · the second horse, its head at the leader's croup.
- 87:8 لِلْيُسْرَىٰ · ي س ر B005 · «دابة حسن التيسور أي حسن نقل القوائم» (sihah) · a good, even stride.
- 87:16 تُؤْثِرُونَ · ء ث ر B001 · «له أصل تقديم الشيء» (maqayis) · putting first.
- 87:16 تُؤْثِرُونَ · ء ث ر B004 · «جاء فلان على إثري وأثري وجاء في أثره وإثره» (tahdhib) · coming behind, in the tracks.
- 87:16 ٱلدُّنْيَا · د ن و B002 · «العدوة الدنيا والعدوة القصوى» (mufradat) · the nearer bank and the farther one.
- 87:17 وَٱلْءَاخِرَةُ · ء خ ر B001 · «أخرى القوم أي من كان في آخرهم» (sihah) · the rear of the company.
- 87:17 وَٱلْءَاخِرَةُ · ء خ ر B003 · «آخرة الرحل وقادمته ومؤخر الرحل ومقدمه» (maqayis) · the rear post of the saddle.
- 87:17 أَبْقَىٰٓ · ب ق ي B004 · «المبقيات من الخيل التي تبقي بعض جريها تدخره» (tahdhib) · horses that save part of their run.
- 87:18 ٱلْأُولَىٰ · ء و ل B001 · «ناقة أولة وجمل أول إذا تقدما الإبل» (maqayis) · the camel at the front.
- Quran: 79:1–5 (oaths: «والسابحات سبحا فالسابقات سبقا»). 56:10–11 («والسابقون السابقون»). 57:21 («سابقوا إلى مغفرة من ربكم»). 8:42 (Badr: «إذ أنتم بالعدوة الدنيا وهم بالعدوة القصوى»).

### 20. Choosing: the picked and the refuse
تؤثرون in 87:16 is choosing what to favour and what to keep for oneself. The dictionary sets two kinds of thing against each other. On one side is the favoured one (الأثير), the best picked out «لا رذل فيهن», and wealth worth calling خير only if it is plentiful and cleanly earned. On the other is الدنيء, "the mean in worth", الأدنى as "the meanest", the غثاء as the lowest of people, and النِّسي as the scraps left behind. The dictionary uses one phrase for both choosing and remaining: «استأثر الله بالبقاء», God keeps lasting for Himself alone. It also defines «أولو بقية» as people who still have some hold and some good in them.
- 87:16 تُؤْثِرُونَ · ء ث ر B005 · «الأثير الكريم عليك الذي تؤثره بفضلك وصلتك» (maqayis); «آثرت فلانا على نفسي من الإيثار» (sihah) · the one you favour.
- 87:16 تُؤْثِرُونَ · ء ث ر B006 · «استأثر الله بالبقاء أي انفرد بالبقاء» (tahdhib) · keeping something for oneself alone. The phrase joins أثر and بقي (87:17).
- 87:17 خَيْرٌۭ · خ ي ر B003 · «الاختيار طلب ما هو خير وفعله» (mufradat) · choosing as seeking the better.
- 87:17 خَيْرٌۭ · خ ي ر B002 · «فيهن مختارات لا رذل فيهن» (mufradat) · the picked, with no refuse among them.
- 87:17 خَيْرٌۭ · خ ي ر B004 · «لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب» (mufradat) · wealth that deserves the name.
- 87:16 ٱلدُّنْيَا · د ن و B003 · «خص الدنيء بالحقير القدر» and «الأدنى عن الأرذل» (mufradat) · the mean and the meanest. The phrase joins دنو and قدر (87:3).
- 87:5 غُثَآءً · غ ث و B004 · «يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه» (maqayis) · the dregs of people.
- 87:6 تَنسَىٰٓ · ن س ي B003 · «النسي ما سقط من منازل المرتحلين من رذال أمتعتهم» (maqayis) · refuse left behind.
- 87:17 أَبْقَىٰٓ · ب ق ي B002 · «أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير» (tahdhib) · what remains still holds good. The phrase joins بقية and خير.
- Quran: 79:37–41 («فأما من طغى وآثر الحياة الدنيا فإن الجحيم هي المأوى», against the one who feared his Lord's standing). 20:72–73 (Pharaoh's magicians: «لن نؤثرك على ما جاءنا من البينات ... والله خير وأبقى»; the scene opens at 20:70). 20:131 («زهرة الحياة الدنيا ... ورزق ربك خير وأبقى»). 28:60. 42:36. 12:91 (Joseph's brothers: «لقد آثرك الله علينا»). 11:116 («أولو بقية»). 59:9 («ويؤثرون على أنفسهم»).

### 21. The reminder offered: taken by the one who fears, steered round by the most wretched
87:9–11 show the reminder being offered, taken by one person and avoided by another. The reminder is a means of recalling a need. نفع is benefit, the opposite of harm. خشية is a fear mixed with reverence, which "mostly comes from knowledge", and the dictionary even uses خشيت to mean "I knew", in a phrase about following guidance. The most wretched one does not refuse the reminder outright; he keeps it at a distance (جنب, distance, the opposite of closeness). The dictionary derives the state of جنابة from the same root «لأنه يبعد عن الصلاة والمسجد». Avoiding the reminder thus shades into being kept from the prayer of 87:15.
- 87:9 فَذَكِّرْ / ٱلذِّكْرَىٰ · ذ ك ر B009 · «الذكرى اسم للتذكير والتذكير مجاوز» (ayn); «التذكرة ما تستذكر به الحاجة» (sihah) · the reminder as an offered means.
- 87:9 نَّفَعَتِ · ن ف ع B001 · «النفع ضد الضر» (ayn;sihah;tahdhib) · benefit, against harm.
- 87:10 يَخْشَىٰ · خ ش ي B001 · «الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم» (mufradat) · fear born of knowledge. The phrase joins خشية with علم (87:7).
- 87:10 يَخْشَىٰ · خ ش ي B002 · «خشيت بأن من تبع الهدى معناه علمت» (sihah) · fearing as knowing. The phrase joins خشي and هدى (87:3).
- 87:11 يَتَجَنَّبُهَا · ج ن ب B003 · «الأصل الآخر البعد والجنابة» (maqayis) · distance.
- 87:11 يَتَجَنَّبُهَا · ج ن ب B004 · «الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد» (maqayis) · the one kept away from prayer. The phrase joins جنب and صلاة (87:15).
- 87:11 ٱلْأَشْقَى · ش ق و B001 · «الشقوة خلاف السعادة» (maqayis) · wretchedness, the opposite of happiness.
- Quran: 80:1–10 (the Prophet and the blind man: «لعله يزكى أو يذكر فتنفعه الذكرى ... وهو يخشى»). 51:55 («وذكر فإن الذكرى تنفع المؤمنين»). 20:2–3 («ما أنزلنا عليك القرآن لتشقى إلا تذكرة لمن يخشى»). 79:18–19 (Moses sent to Pharaoh: «هل لك إلى أن تزكى وأهديك إلى ربك فتخشى»). 79:26. 35:18 («إنما تنذر الذين يخشون ربهم بالغيب وأقاموا الصلاة ومن تزكى»). 35:28 («إنما يخشى الله من عباده العلماء»). 50:45. 88:21. 20:124 («ومن أعرض عن ذكري»). 92:15–17 (the reversal: «لا يصلاها إلا الأشقى ... وسيجنبها الأتقى»).

## Interactions

- 2 Pasture × 3 Flood: they share غثاء. 13:17 stages the flood carrying scum away while «ما ينفع الناس فيمكث في الأرض».
- 3 Flood × 11 Fire: the mufradat's «غثاء السيل والقدر ... وزبد القدر» puts scum in the flood and on the pot. 13:17 puts one scum in the torrent and another «مما يوقدون عليه في النار».
- 1 Rain × 2 Pasture: they meet at أخرج المرعى. 7:57, 20:53 and 39:21 run from the sky's water to the plant brought out.
- 1 Rain × 17 Out of cover: خفي carries both faint lightning (B004) and rain bringing mice out (B003, glossed with أخرجهن).
- 1 Rain × 10 Brand: «الوسمي ... يسم الأرض بالنبات فيصير فيها أثرا». Rain brands the land the way an iron brands a hide.
- 2 Pasture × 20 Choosing × 12 Life: الحياة الدنيا is likened to pasture that dries (18:45, 57:20, 10:24); غثاء is also «سفلة الناس»; the living plant «طريا يهتز» against land not yet brought to life.
- 4 Field × 12 Life × 19 File × 20 Choosing: «الفلاح والفلح البقاء في الخير» joins أفلح (87:14) with أبقى and خير (87:17).
- 4 Field × 14 Worship: «صلاة الله للمسلمين تزكيته إياهم» joins فصلّى with تزكّى. 24:37 and 23:1–4 stage ذكر, صلاة and زكاة together.
- 4 Field × 2 Pasture: the land is the same, but cultivated ground grows and yields (زكا, خراج) while wild pasture dries to غثاء. 42:20 sets «حرث الآخرة» against «حرث الدنيا».
- 5 Herd × 18 Road × 19 File: «هوادي» are the leaders of the wild herd, of the road and of the running horses (هدي B003).
- 6 Shaft × 8 Body: «خلق فسوى» is both the finished arrow («سهم مخلق أملس مستو») and the embryo (75:38 «فخلق فسوى»). 80:19–20 runs خلق, قدر, then the way made easy.
- 6 Shaft × 11 Fire: «صلى عصاه إذا أدارها على النار يثقفها». The same verb as 87:12 names fire used to straighten wood.
- 6 Shaft × 7 Waterskin × 9 Lots: خلق is measuring before cutting, for a hide («خلقت الأديم للسقاء إذا قدرته»), for an arrow, and for a share («قدر لكل أحد نصيبه»).
- 7 Waterskin × 21 Reminder: the tahdhib phrase sets نفعة pieces «في كل جانب», so نفع (87:9) and the root of يتجنبها (87:11) name the same vessel.
- 7 Waterskin × 15 Memory: the صحف are «القطعة من أدم أبيض أو رق», the same leather the craftsman measures.
- 9 Lots × 13 Height: المعلى, the top arrow, comes from the root of الأعلى.
- 9 Lots × 20 Choosing: «لا خلاق له في الآخرة» (2:200), and 9:69's worldly خلاق enjoyed and lost.
- 10 Brand × 11 Fire: «ما نار هذه الناقة أي ما سمتها». The fire of 87:12 is also the mark of وسم.
- 10 Brand × 20 Choosing: «توسمت فيه الخير والشر أي رأيت فيه أثرا» joins وسم, خير and أثر.
- 11 Fire × 14 Worship: one consonantal frame, ص ل ى, gives يصلى النار (87:12) and فصلّى (87:15). 20:10–14 runs from the fire Moses saw to «أقم الصلاة لذكري». 74:42–43 places «لم نك من المصلين» inside Saqar.
- 11 Fire × 18 Road: «كانوا ينورون ... ليهتدى». 20:10 has «أجد على النار هدى», and «سواء الجحيم» is the middle of the road gone wrong.
- 11 Fire × 21 Reminder: 56:73 calls the fire people kindle a «تذكرة». 92:15–17 has the most wretched entering the fire and the most pious kept away from it.
- 12 Life × 20 Choosing: «ويستحيون نساءكم أي يستبقونهن» and «استأثر الله بالبقاء» both tie life and choosing to remaining.
- 13 Height × 14 Worship: they share اسم. 24:36 stages raised houses, the name remembered, and glorifying.
- 13 Height × 16 Voice: «جهر بالقول رفع به صوته»; speaking aloud is raising the voice.
- 13 Height × 18 Road: «استوى على ظهر دابته أي علا واستقر».
- 13 Height × 20 Choosing: الأعلى (87:1) against الدنيا (87:16). In surah 79, Pharaoh says «أنا ربكم الأعلى» (79:24) and the transgressor «آثر الحياة الدنيا» (79:38).
- 14 Worship × 15 Memory × 16 Voice: «الذكر قراءة القرآن والتسبيح والدعاء» and «جهر بكلامه وصلاته وقراءته».
- 15 Memory × 3 Flood × 20 Choosing: قرأ as gathering, against غثاء that «يتفرق» and النِّسي dropped at the camp.
- 15 Memory × 8 Body: ق ر ء is both the gathering of recitation and the womb closing on its young.
- 16 Voice × 17 Out of cover: the pair in 87:7. 20:7 and 27:25 stage sound and hidden things together.
- 18 Road × 21 Reminder: يتجنبها and الأشقى. 20:123 («فلا يضل ولا يشقى») and 92:5–17 stage the easy way, the hard way, and the one kept away.
- 18 Road × 6 Shaft × 4 Field: the ayn phrase «أيسر صعودا وأقدر مقعدا» holds شقو, يسر and قدر together.
- 19 File × 20 Choosing: آثر is both "put in front" and "prefer". 87:16–17 then has the later one outlasting the first.
- Ṭā Hā as a whole stages many of these chains together: 20:2–7 (لتشقى, تذكرة, يخشى, العلى, الجهر وأخفى); 20:9–14 (fire, guidance, prayer, remembrance); 20:50–54 (خلق, هدى, أخرج, ارعوا); 20:68–76 (الأعلى, نؤثرك, الحياة الدنيا, خير وأبقى, لا يموت فيها ولا يحيى, من تزكى); 20:114–133 (forgetting, يشقى, ذكري, sabbih, خير وأبقى, الصحف الأولى).
- Surah 92 stages 18, 21, 11 and 4 together: يسرى/عسرى, هدى, يصلاها الأشقى, سيجنبها, يتزكى, ربه الأعلى.
- Surah 80 stages 21, 4, 6/8 and 15 together: يزكى, يذكر, تنفعه الذكرى, يخشى, صحف, خلقه فقدره, السبيل يسره, شققنا الأرض.
- Surah 79 stages 13, 20, 2, 5, 19 and 21 together: السابحات, تزكى, أهديك, تخشى, ربكم الأعلى, أخرج مرعاها, آثر الحياة الدنيا.

## Ayat

**87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى**
- 13 Height: اسم (from سموّ), الأعلى and سبّح (clearing of flaw; majesty and light). Scene: a name that raises what it names, a figure rising into view, the Most High exalted above every flaw, mention as height, against the low near life.
- 14 Worship: سبّح opens the act that 87:15 closes. Scene: glorifying, remembering the name, praying (standing, bowing, prostrating, voicing), one act seen at the surah's start and end.
- 1 Rain: اسم as sky, cloud, rain and plant; اسم read through وسم as the first rain; ربّ as the low cloud that rears plants and lingers. Scene: cloud forms, hangs low and stays; faint lightning flickers at its edges while a watcher keeps vigil; first rain marks the ground green, brings the land to life and drives creatures out, ahead of the pasture.
- 10 Brand: اسم read through وسم as a brand; ربّ as owner. Scene: a mark burned into the hide by an iron, by which owner and lineage are known; a foot-mark that makes tracks readable; signs read on a face.
- 5 Herd: ربّ as owner and manager; the herd; the haunt. Scene: the owner who governs, the lead animals in front, the pasture grazed and guarded under a watching herder, the camels' haunt.
- 6 Shaft: ربّ as the one who sets right and completes in stages. Scene: the maker measures the shaft, smooths it, straightens it (even over fire), fixes the head that goes first.
- 4 Field: ربّ of the estate. Scene: ground split by the ploughman, crop growing, the owner tending it to completion, yield brought out, its due given; flourishing as "remaining in good".
- 7 Waterskin: ربّ as the seasoning of the skin. Scene: hide measured before cutting, gusseted on both sides, seasoned, churned, in time worn smooth.
- 8 Body: ربّ as rearing in stages. Scene: gathered in the womb, formed, made even without flaw, raised to full growth, guided to its way, then aging.
- 9 Lots: ربابة (the arrow bag) and المعلى (the top arrow). Scene: smoothed shafts kept in a bag and drawn to divide a camel, the highest arrow taking most; each share measured; some have no share in the later life.
- 3 Flood: ربّ as gathered plentiful water. Scene: the torrent carries the dry wrack off while the water is caught in rock basins, twisting pits and cleaned wells, where it stays and serves.
- 2 Pasture: ربّة, plants that do not dry in summer, as the counter-image. Scene: pasture brought out in patches, dark green-black, then dried, its sweetness gone, heaped by the flood and carried as wrack.
- 19 File: سبّح as the running horse. Scene: a line of runners: the swift horse, the leaders, the second at the leader's croup, the near bank and the rear, and the horse that holds back part of its run.

**87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ**
- 6 Shaft: خلق as straight measuring and smoothing; سوّى as straightening a bend. Scene as at 87:1.
- 8 Body: the embryo whose form has appeared; the body made even; full growth. Scene as at 87:1.
- 7 Waterskin: خلق as sizing the hide; wear. Scene as at 87:1.
- 9 Lots: the smoothed arrow; خلاق, the measured share. Scene as at 87:1.
- 3 Flood: الخلائق, the rock basins of rainwater. Scene as at 87:1.
- 18 Road: سوّى as mounting a back, the saddle pad (joined with أحوى), the middle ground and the middle of Hell. Scene: a guide ahead, a staff in front, an easy-led light-legged mount, a long ridge easy to climb, the middle ground, a rider settled on a padded saddle, and one who steers aside.

**87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ**
- 6 Shaft: قدّر as thinking out how to even a thing; هدى as the arrowhead and staff that go first. Scene as at 87:1.
- 8 Body: each thing set to its measure; (from memory) the newborn guided. Scene as at 87:1.
- 18 Road: هدى as the guide ahead, the propped walk, the calm pace. Scene as at 87:2.
- 5 Herd: the lead animals. Scene as at 87:1.
- 19 File: هوادي الخيل. Scene as at 87:1.
- 11 Fire: هدى sought at the beacon. Scene: a fire seen afar and made for, a beacon «ليهتدى», a fire to warm at, and the fire one is thrust into and roasted in.
- 4 Field: the yield «بقدر معلوم». Scene as at 87:1.
- 9 Lots: each share measured. Scene as at 87:1.
- 7 Waterskin: «إذا قدرته». Scene as at 87:1.
- 21 Reminder: «خشيت بأن من تبع الهدى». Scene: a reminder offered that may help; the one who fears from knowledge takes it; the most wretched keeps it at a distance, as one kept from prayer.

**87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ**
- 2 Pasture: brought out in patches, dark outweighing light; the grass, the place and the grazing. Scene as at 87:1.
- 1 Rain: the cloud first appearing. Scene as at 87:1.
- 17 Out of cover: coming out of its place. Scene: plants out of soil, mice out of burrows after rain, a well cleared until its water shows, inner fronds and hidden feathers; and an eye blinded by too much light.
- 5 Herd: the pasture guarded and watched. Scene as at 87:1.
- 4 Field: خراج, the yield. Scene as at 87:1.

**87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ**
- 2 Pasture: the turn (جعل), dry after green, heaped by the flood, black from green. Scene as at 87:1.
- 3 Flood: what floats and scatters; pits the flood fills. Scene as at 87:1.
- 20 Choosing: غثاء as the dregs of people. Scene: the favoured put first, the best picked with no refuse among it, against the near and mean kept instead, dregs and dropped scraps, and what remains with good in it.
- 18 Road: الحوية saddle pad. Scene as at 87:2.

**87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ**
- 15 Memory: gathering and joining; being made to recite; losing hold of a trust; dropped scraps. Scene: recitation gathered and joined, held in memory, kept from slipping, recalled by reminder, set down in sheets gathered together; what is forgotten is dropped like scraps at an old camp.
- 16 Voice: reciting from memory. Scene: speech raised aloud in reading and prayer, or kept low and hidden in the heart; both known.
- 8 Body: the womb gathering its young. Scene as at 87:1.
- 20 Choosing: النِّسي, refuse. Scene as at 87:5.

**87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ**
- 16 Voice: the raised voice against the lowered one. Scene as at 87:6.
- 17 Out of cover: خفي as bringing out; «كل شيء بدا فقد جهر»; the dazzled eye. Scene as at 87:4.
- 1 Rain: faint lightning; mice brought out by rain. Scene as at 87:1.
- 3 Flood: the cleared well; the well full of water. Scene as at 87:1.
- 7 Waterskin: churning. Scene as at 87:1.
- 10 Brand: علم as a mark that sets apart. Scene as at 87:1.
- 14 Worship: «جهر بكلامه وصلاته وقراءته». Scene as at 87:1.
- 21 Reminder: knowledge as the source of fear. Scene as at 87:3.
- 15 Memory: the exception «إلا ما شاء الله» stands within the keeping. Scene asat 87:6.

**87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ**
- 18 Road: the way made easy and ready; the easy-led, light-legged mount; taking the left-hand way. Scene as at 87:2.
- 19 File: a good, even stride. Scene as at 87:1.
- 9 Lots: الميسر and the dividing of the camel. Scene as at 87:1.
- 6 Shaft: «تهيأ» is shared with قدّر (B005); ready to be released. Scene as at 87:1.

**87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ**
- 21 Reminder: the reminder as an offered means; benefit as the opposite of harm. Scene as at 87:3.
- 15 Memory: ذكرى as recall of what slipped, and as a prophet's book. Scene as at 87:6.
- 3 Flood: نفع as what serves and stays. Scene as at 87:1.
- 7 Waterskin: نفعة pieces on the skin's two sides. Scene as at 87:1.
- 12 Life: «ليس بفلان حياة أي ليس عنده نفع ولا خير». Scene: strength leaving, the swoon one wakes from, life as benefit and good, sparing alive, the near life and the life that lasts; in the fire, a state that is neither.

**87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ**
- 21 Reminder: fear born of knowledge; fearing as knowing. Scene as at 87:3.
- 15 Memory: تذكّر as seeking what slipped. Scene as at 87:6.
- 2 Pasture: الخشي as dried and shrivelled (maqayis calls it anomalous to the root). Scene as at 87:1.

**87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى**
- 21 Reminder: keeping at a distance; the one kept from prayer; wretchedness. Scene as at 87:3.
- 18 Road: leading at the side and steering aside; toil; the long ridge «أيسر صعودا». Scene as at 87:2.
- 7 Waterskin: the two sides (جانب). Scene as at 87:1.
- 1 Rain: the south wind that drives the cloud. Scene as at 87:1.

**87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ**
- 11 Fire: making for a fire seen afar, the beacon, warming, being thrust in, roasting; the greatest fire (from memory: set against the small fire of this world). Scene as at 87:3.
- 6 Shaft: the staff straightened over fire. Scene as at 87:1.
- 10 Brand: النار as the brand. Scene as at 87:1.
- 13 Height: الكبرى shares a root with التكبير and with الكبرياء. Scene as at 87:1.
- 12 Life: the fire is where the state of 87:13 is held. Scene as at 87:9.
- 8 Body: كبر as old age. Scene as at 87:1.
- 14 Worship: يصلى shares the consonantal frame of فصلّى (87:15). Scene as at 87:1.

**87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ**
- 12 Life: strength leaving; the swoon; sleep; life as benefit; sparing alive; both negated. Scene as at 87:9.
- 2 Pasture: living grass «طريا يهتز» and dead land not yet revived; neither describes the man in the fire. Scene as at 87:1.
- 1 Rain: الحيا, the rain that brings the land to life. Scene as at 87:1.

**87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ**
- 4 Field: splitting the ground; the ploughman; success as «البقاء في الخير»; the crop growing; the share given out. Scene as at 87:1.
- 14 Worship: God's صلاة as تزكية joins 87:14 to 87:15. Scene as at 87:1.
- 21 Reminder: 80:3–4 has تزكّى and the reminder that benefits together. Scene as at 87:3.

**87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ**
- 14 Worship: remembrance as prayer, recitation and glorifying; the parts of the prayer; the bent back. Scene as at 87:1.
- 13 Height: اسم that raises; ذكر as «العلاء والشرف». Scene as at 87:1.
- 15 Memory and 16 Voice: ذكر on the tongue and in the heart. Scenes as at 87:6.
- 11 Fire: the prayer is where Moses' approach to the fire ends (20:14); the frame is shared with يصلى. Scene as at 87:3.
- 19 File: المصلّي, the second horse. Scene as at 87:1.
- 1 Rain, 5 Herd, 4 Field, 10 Brand: ربّه and اسم carry the same senses as at 87:1.

**87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا**
- 20 Choosing: the favoured; keeping something for oneself; the mean and the meanest. Scene as at 87:5.
- 19 File: putting first; following in tracks; the nearer bank. Scene as at 87:1.
- 12 Life: the near life against the true life that lasts. Scene as at 87:9.
- 13 Height: الدنيا as the low pole against الأعلى. Scene as at 87:1.
- 10 Brand: أثر as foot-mark and lasting trace. Scene as at 87:1.
- 15 Memory: «أثرت الحديث». Scene as at 87:6.
- 2 Pasture: the near life is the Quran's pasture parable (18:45, 57:20). Scene as at 87:1.
- 8 Body: أدنت, birth drawing near. Scene as at 87:1.

**87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ**
- 20 Choosing: choosing as seeking the better; the picked; «أولو بقية». Scene as at 87:5.
- 19 File: the rear of the company; the rear post of the saddle; horses that save part of their run. Scene as at 87:1.
- 12 Life: remaining as living on; sparing from destruction. Scene as at 87:9.
- 4 Field: «البقاء في الخير»; «الباقي حاصل الخراج». Scene as at 87:1.
- 3 Flood: staying fixed in its state; what benefits stays. Scene as at 87:1.
- 1 Rain: the watcher tracking the lightning. Scene as at 87:1.
- 9 Lots: «لا خلاق له في الآخرة». Scene as at 87:1.
- 10 Brand: «توسمت فيه الخير والشر». Scene as at 87:1.

**87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ**
- 15 Memory: leather sheets; sheets gathered into one; the first. Scene as at 87:6.
- 19 File: الأولى as the camel at the front. Scene as at 87:1.
- 1 Rain: the first rain «في أول السنة». Scene as at 87:1.

**87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ**
- 15 Memory: the gathered sheets of two prophets (53:36–54 gives their contents). Scene as at 87:6.
- 11 Fire: Moses who saw a fire and found guidance and prayer at it (20:9–14, 27:7, 28:29). Scene as at 87:3.
- 18 Road: Abraham's prayer «واجنبني», to which the mufradat points for جنب. Scene as at 87:2.
- 13 Height and 20 Choosing: Moses against Pharaoh's «أنا ربكم الأعلى» (79:24), and the magicians' «لن نؤثرك ... والله خير وأبقى» (20:72–73). Scenes as at 87:1 and 87:5.

