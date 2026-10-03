Surah: 89. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (89:1 to 89:30), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s089/surah.r2/text.md =====
# Surah 89

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/out/s089/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. Night covering, dawn splitting it
Night lies over everything. Movement goes on inside it, and dawn breaks through it at a single point. The surah opens on the first light (89:1), counts nights (89:2), sets the closing odd prayer of the night beside the paired prayer of the morning (89:3) and watches the night move off (89:4). Under the surah's later words the dictionary supplies the rest of the scene. Dawn stands up as a column (العماد), and morning "breathes" (النفس). Night's covering is الجنان, the word whose root gives the closing جنتي. The first half of the scene, the night covering things, comes back at the end as the garden that covers its ground (chain 16).
- 89:1 وَٱلْفَجْرِ: ف ج ر B002, "الفجر انفجار الظلمة عن الصبح" (maqayis); "قيل للصبح فجر لكونه فجر الليل" (mufradat); "الفجر في آخر الليل كالشفق في أوله" (sihah). Dawn is the dark split open, and it marks the night's far edge.
- 89:2 وَلَيَالٍ: ل ي ل B001, "ظلام الليل" (tahdhib); "ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه" (jamhara). The covering darkness that is counted.
- 89:2 عَشْرٍۢ: ع ش ر B016, "يقال أيضا لثلاث ليال من ليالى الشهر عشر وهي بعد التسع" (sihah). عشر is also a name for a group of the month's nights, so the nights are counted toward the month's end.
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ: و ت ر B001, "الوتر في العدد خلاف الشفع وأوتر في الصلاة" (mufradat). ش ف ع B001, "شفعة الضحى ركعتا الضحى" (tahdhib). The night's prayer is closed with an odd number and the forenoon's prayer is a pair, so the night and the day are each framed. From memory, the commentators also read the ten as the nights of Dhū l-Ḥijja, the odd as ʿArafa and the even as the day of sacrifice.
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ: س ر ي B001, "السرى سير الليل" (maqayis;ayn;sihah;mufradat). Night moves on as a night traveller does. س ر ي B004, "السرو كشف الشيء عن الشيء" (maqayis); "انسرى عني الهم انكشف" (sihah). The same root names lifting a cover off something, which is the night going away.
- 89:7 ٱلْعِمَادِ: ع م د B007, "عمود الصبح ابتداء ضوئه" (sihah;mufradat) [fixed expression]. The first shaft of dawn standing upright. Compare ف ج ر B002, "الفجر حمرة الشمس في سواد الليل وهما فجران" (jamhara): there are two dawns.
- 89:23 وَأَنَّىٰ: ء ن ي B002, "آناء الليل ساعاته" (sihah;tahdhib;mufradat). The night's hours.
- 89:27 ٱلنَّفْسُ: ن ف س B009, "تنفس الصبح أي تبلج" (sihah); "إذا انشق الفجر وانفلق" (tahdhib) [fixed expression]. The dictionary explains the root of النفس with الفجر: morning breathes out when dawn splits.
- 89:30 جَنَّتِى: ج ن ن B002, "جنان الليل سواده وستره الأشياء" (maqayis); "أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته" (ayn). The root of the garden also names night's covering.
- Quran: 81:17–18, وَٱللَّيْلِ إِذَا عَسْعَسَ وَٱلصُّبْحِ إِذَا تَنَفَّسَ. An oath series in at-Takwīr: night moving and morning breathing are joined.
- Quran: 6:76, فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ. Abraham, as night comes over him, watching the stars set.
- Quran: 92:1, وَٱلَّيْلِ إِذَا يَغْشَىٰ. An oath on the night as it covers.
- Quran: 74:33–34. An oath on the night as it turns back and the morning as it brightens.
- Quran: 6:96, فَالِقُ ٱلْإِصْبَاحِ وَجَعَلَ ٱلَّيْلَ سَكَنًا. God described as the one who splits the dawn and makes the night a rest.
- Quran: 2:187. The fasting rule: the white thread is told from the black مِنَ ٱلْفَجْرِ.
- Quran: 17:78 (وَقُرْءَانَ ٱلْفَجْرِ, the dawn recitation in the prayer times) and 97:5 (حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ, the Night of Decree lasting until dawn).

### 2. Water bursting out, running down the wadi, overflowing its measure
Water breaks out of rock or ground, finds the wadi that drains it and runs down the slope. It collects in hollows, can be dammed with stone, and in flood rises above its bounds and sweeps things away. The dictionary describes moral breach with the same words it uses for the water: انبعاث and تفتح for sin, خروج for corruption and for water leaving its measure. So 89:11–12 (طغوا… الفساد) is heard as a flood, and Thamud's wadi (89:9) is the channel. The opening الفجر already holds the bursting of water.
- 89:1 وَٱلْفَجْرِ: ف ج ر B001, "انفجر الماء انفجارا تفتح" (maqayis); "وانفجر الماء وغيره انفجارا إذا انبعث سائلا" (jamhara); "شق الشيء شقا واسعا" (mufradat). Water splitting out. "مفاجر الوادي مرافضه" (maqayis;sihah): here the dictionary joins the root of الفجر to the wadi, whose outlets are its مفاجر.
- 89:1 وَٱلْفَجْرِ: ف ج ر B004, "الانبعاث والتفتح في المعاصي فجورا" (maqayis); "انبعاثه في المعاصي" (jamhara). The same bursting, now into sin.
- 89:9 بِٱلْوَادِ: و د ي B005, "والوادي كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل أو منفذا" (tahdhib); "وأحسبه راجعا إلى هذا لسيلان الماء فيه" (jamhara). و د ي B001, "ودى أي سال" (tahdhib). The flood's channel, named for flowing.
- 89:9 جَابُوا۟: ج و ب B004, "الجوبة كالغائط وهو من الباب لأنه كالخرق في الأرض" (maqayis). A hollow torn into the ground.
- 89:8 يُخْلَقْ: خ ل ق B011, "الخليقة نقر في صخرة يجتمع فيه ماء السماء" (jamhara); "قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق" (tahdhib). A hollow in rock that holds rainwater, the same rock as 89:9 الصخر.
- 89:7 ٱلْعِمَادِ: ع م د B013, "عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة" (tahdhib). The flood stopped with stones until it pools.
- 89:11 طَغَوْا۟: ط غ ي B002 [fixed expression], "طغى السيل إذا جاء بماء كثير" (maqayis;sihah); "طغى الماء خروجه عن المقدار" (maqayis); "طغا البحر والماء إذا علا كل شيء فاجترفه" (tahdhib). The flood rising over everything and sweeping it off.
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ: ك ث ر B001, "الكثرة نماء العدد" (ayn;tahdhib). ف س د B001, "الفساد خروج الشيء عن الاعتدال" (mufradat). The volume grows and things leave their balance; the خروج matches water leaving its measure.
- 89:13 فَصَبَّ: ص ب ب B002, "صب في الوادي إذا انحدر فيه" (jamhara); "الصبب تصوب نهر أو طريق يكون في حدور" (ayn;tahdhib). The dictionary joins صبّ with the wadi: running down into it.
- 89:16 فَقَدَرَ: ق د ر B001, "المقدار هو الهنداز؛ ينزل المطر بمقدار" (tahdhib). The measure that the flood breaks.
- 89:20 جَمًّۭا: ج م م B001, "جمة الماء معظمه ومجتمعه" (mufradat); "كثرة الشيء واجتماعه" (maqayis). The bulk of gathered water.
- 89:22 وَجَآءَ: ج ي ء (root_000282) B002, "الجيأة الحفرة العظيمة يجتمع فيها ماء المطر" (tahdhib). A pit where rain gathers.
- Quran: 2:74, وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ. God to the Israelites: their hearts are harder than stones that let rivers burst out.
- Quran: 13:17, فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا. The parable of water filling wadis by their measure.
- Quran: 54:11–12, وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا. Noah's flood.
- Quran: 69:11, إِنَّا لَمَّا طَغَا ٱلْمَآءُ. God recalls the flood (cited under ط غ ي by mufradat).
- Quran: 46:21–25. Hud warns ʿĀd. They see a cloud facing their wadis (مُّسْتَقْبِلَ أَوْدِيَتِهِمْ), call it rain, and it is punishment.
- Quran: 30:41, ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ. Corruption spreading over land and sea.
- Quran: 26:151–152, ٱلَّذِينَ يُفْسِدُونَ فِى ٱلْأَرْضِ. Ṣāliḥ to Thamud about the extravagant.
- Quran: 17:90–91. Quraysh demand that the Prophet make a spring and rivers burst out (تَفْجُرَ… فَتُفَجِّرَ).

### 3. Rain poured from above, returning life to the soil
Water comes down from above, and the dictionary names rain from several of the surah's words: provision, life, return, generosity and the first rain. The rain falls on soft soil and grows the garden that covers the ground. The same pouring verb carries the punishment of 89:13 (فصبّ… عذاب), and ع ذ ب names sweet water as well as punishment. So the downpour can be heard either way: as mercy, or as what ʿĀd took for rain.
- 89:13 فَصَبَّ: ص ب ب B001, "صب الماء إراقته من أعلى" (mufradat). ص ب ب B006, "الصبيب المصبوب من المطر" (mufradat). Pouring from above.
- 89:28 ٱرْجِعِىٓ: ر ج ع B006, "الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث" (maqayis). The dictionary joins the root of ارجعي with صبّ: rain is named for pouring and then coming back.
- 89:16 رِزْقَهُۥ: ر ز ق B003, "في السماء رزقكم قال المطر" (tahdhib); "وقد يسمى المطر رزقا" (sihah). Provision that falls from the sky.
- 89:24 لِحَيَاتِى: ح ي ي B002, "يسمى المطر حيا لأن به حياة الأرض" (maqayis); "الحيا المطر لأنه يحيي الأرض بعد موتها" (mufradat). Rain as the earth's life.
- 89:15 فَأَكْرَمَهُۥ: ك ر م B002 [fixed expression], "كرم السحاب أتى بالغيث" (maqayis;sihah); "أرض مكرمة للنبات إذا كانت جيدة النبات" (maqayis;sihah). The cloud that gives generously, and the soil that answers it.
- رَبُّكَ (89:6, 13, 14, 22, 28; رَبُّهُۥ / رَبِّىٓ in 89:15–16): ر ب ب B008, "الرباب: السحاب، سمي بذلك لأنه يرب النبات" (mufradat). ر ب ب B013, "الربب وهو الماء الكثير سمي بذلك لاجتماعه" (maqayis). Cloud that nurses the plants, and gathered water.
- 89:14 لَبِٱلْمِرْصَادِ: ر ص د B004, "الرصد أول المطر"; "أرض مرصدة وهي التي مطرت وهي ترجى لأن تنبت". The first rain, and ground that has been rained on and is waiting to sprout.
- 89:21 ٱلْأَرْضُ: ء ر ض B002, "أرض أريضة لينة طيبة" (maqayis;ayn). Soft, fertile soil.
- 89:30 جَنَّتِى: ج ن ن B003, "كل بستان ذي شجر يستر بأشجاره الأرض" (mufradat). ج ن ن B011, "جن النبت جنونا إذا اشتد وخرج زهره" (maqayis). The garden that covers its ground, and plants thickening and flowering.
- 89:13 / 89:25 عَذَابٍ / يُعَذِّبُ: ع ذ ب B001, "العذب ضد الملح وكل مستسيغ من طعام أو شراب" (jamhara). The root of punishment also names sweet, drinkable water. This is the reversal inside the downpour.
- Quran: 80:24–26, فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا. Man told to look at his food: water poured, then the earth split.
- Quran: 86:11–12, وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ وَٱلْأَرْضِ ذَاتِ ٱلصَّدْعِ. An oath on returning rain and splitting earth.
- Quran: 51:22, وَفِى ٱلسَّمَآءِ رِزْقُكُمْ. Provision in the sky.
- Quran: 46:24, قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا. ʿĀd take the punishment for a rain cloud (scene opens at 46:21).

### 4. Lash and bond: the instruments of punishment
The punishment is staged with two tools: a lash poured down on the tyrants of the past (89:13), and on the Day a punishment and a binding that no one else can match (89:25–26). The dictionary joins the lash and the punishment through the whip's tip, says the whip "mixes" with the skin, and names the mark left on the body. Pharaoh's pegs (89:10) give a third tool, the stake that pins a body down.
- 89:13 سَوْطَ: س و ط B002, "السوط الجلد المضفور الذي يضرب به" (mufradat); "سطته بالسوط ضربته" (maqayis). The plaited leather lash. س و ط B001, "السوط لأنه يخالط الجلدة" (maqayis): it is named for mixing into the skin. س و ط B003 [fixed expression], "تشبيها بما يكون في الدنيا من العذاب بالسوط"; "إشارة إلى ما خلط لهم من أنواع العذاب" (mufradat). The kinds of punishment mixed together for them.
- 89:13 عَذَابٍ: ع ذ ب B006, "عذبة السوط طرفه" (maqayis;tahdhib). The dictionary joins سوط and the root of عذاب: the whip's tip. ع ذ ب B005, "ناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة" (maqayis). Punishment at root is a striking.
- 89:13 فَصَبَّ: ص ب ب B009, "صب رجل فلان في القيد إذا قيد" (tahdhib). The same verb for putting a foot in a fetter.
- 89:8, 89:11 ٱلْبِلَٰدِ: ب ل د B006, "البلد الأثر بالجسد وجمعه أبلاد" (tahdhib); "بجلده بلد أي أثر" (mufradat). The mark left on the skin.
- 89:10 ذِى ٱلْأَوْتَادِ: و ت د B001, "تد وتدك بالميتدة" (sihah). و ت د B003, "وتد فلان رجله في الأرض إذا ثبتها" (tahdhib). The stake driven in and the foot pinned to the ground. From memory, commentators say Pharaoh pegged people out on four stakes to torture them.
- 89:25 يُعَذِّبُ عَذَابَهُۥٓ: ع ذ ب B005, "العذاب هو الإيجاع الشديد" (mufradat). Severe pain.
- 89:26 يُوثِقُ وَثَاقَهُۥٓ: و ث ق B003, "الوثاق: كل ما أوثقت به شيئا" (jamhara); "أوثقه في الوثاق، أي شده؛ فشدوا الوثاق" (sihah). The rope and the tying.
- 89:25–26 أَحَدٌۭ: ء ح د B002, "أحد في النفي لاستغراق جنس الناطقين" (mufradat). No one at all can strike or bind like this.
- Quran: 69:25–34. On the Day, about the one handed his book in his left hand: يَٰلَيْتَنِى… خُذُوهُ فَغُلُّوهُ… فِى سِلْسِلَةٍۢ… إِنَّهُۥ… لَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ. Binding, regret and failing to urge food on the poor in one scene.
- Quran: 38:12, وَفِرْعَوْنُ ذُو ٱلْأَوْتَادِ. A list of nations that denied.
- Quran: 47:4, فَشُدُّوا۟ ٱلْوَثَاقَ. A battle order: bind the captives.
- Quran: 14:49 (مُّقَرَّنِينَ فِى ٱلْأَصْفَادِ, the guilty chained together on the Day) and 76:4 (chains and collars prepared).
- Quran: 20:71. Pharaoh threatens the sorcerers with crucifixion on palm trunks.

### 5. The road and the one lying in wait
Travellers cross the land by night and by day. On the road a watcher waits at its post, the way a snake lies across a road and then rears and drops onto whoever passes. The surah tells how the nations "cut through" lands and overstepped in them (89:9, 11). The strike is "poured down on them" (89:13), and only then is the Lord named as being at the lookout (89:14). The image of the ambush is complete: travellers, the road, the watcher, and the strike from above.
- 89:14 لَبِٱلْمِرْصَادِ: ر ص د B003, "المرصاد الطريق"; "المرصاد المكان الذي يرصد به الراصد"; "الرصائد الوصائد مصايد تعد للسباع". The road, the lookout post and the traps. ر ص د B001, "الراصد للشئ المراقب له"; "يقال للحية التي ترصد المارة على الطريق رصيد". The watcher, and the snake waiting on the road for passers-by.
- 89:13 فَصَبَّ: ص ب ب B008, "الحية السوداء إذا أرادت أن تنهش ارتفعت ثم صبت" (sihah); "صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق" (tahdhib). The snake rears and then drops on its victim from above.
- 89:9 جَابُوا۟: ج و ب B002, "جبت الأرض جوبا فأنا جائب وجواب" (maqayis); "جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها" (sihah). The dictionary joins جابوا with البلاد (89:8, 11): people crossing the lands.
- 89:11 طَغَوْا۟ فِى ٱلْبِلَٰدِ: ط غ ي B001, "مجاوزة الحد في العصيان" (maqayis;mufradat). Going past the limit as they cross.
- 89:4 يَسْرِ: س ر ي B001, "السارية للقوم الذين يسرون بالليل" (mufradat). Travellers who go by night.
- 89:6 أَلَمْ تَرَ: ر ء ي B001, "نظر وإبصار بعين أو بصيرة" (maqayis). The listener is told to look at what the watcher did.
- Quran: 78:21, إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا. An-Nabaʾ, the Day: Hell is a lookout.
- Quran: 9:5, وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ. A command against those who broke their treaties.
- Quran: 7:16–17, لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ. Iblis tells God he will lie in wait on the straight path.
- Quran: 7:86, وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ. Shuʿayb to his people, who lay in wait on the roads.
- Quran: 72:9, شِهَابًۭا رَّصَدًۭا. The jinn find a flame lying in wait in the sky.

### 6. Stone, column and peg: the builders' works and their leveling
Three peoples are named by what they built: ʿĀd by columns (or tent poles) and a city with no equal, Thamud by rock cut out in the valley, Pharaoh by pegs. The dictionary adds the stone column (سارية), the stone-walled dwellings of Thamud (الحجر), and diggers who work in clay and pits. It also names the opposite: a trace leveled with the ground, an effaced ruin, and the wall and the mountain crushed flat. That leveling arrives at 89:21. The upright and the flattened are both inside مثل.
- 89:7 إِرَمَ: this root is not in the dictionary. From memory, the lexicons give the أَرَام / إِرَم as stones set up as way-markers in the desert.
- 89:7 ذَاتِ ٱلْعِمَادِ: ع م د B003, "الشيء الذي يسند إليه عماد وجمع العماد عمد والعمود من خشب أو حديد" (maqayis); "العمد أساطين الرخام" (tahdhib). The load-bearing column. ع م د B005 [fixed expression], "ذات العماد أي ذات الطول وقيل ذات البناء الرفيع" (tahdhib): the dictionary glosses the ayah itself as height or tall building. ع م د B004, "أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها" (maqayis;ayn). The other reading: tent poles of people who live only in tents.
- 89:4 يَسْرِ: س ر ي B005, "السارية أسطوانة من حجارة أو آجر" (ayn). The root of يسر also names a stone or brick pillar.
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا: خ ل ق B002, "الخلق ابتداع الشيء على مثال لم يسبق إليه" (tahdhib). The dictionary joins يخلق and مثلها: making something on a model nothing preceded. خ ل ق B008, "رسم مخلولق إذا استوى بالأرض" (maqayis). The same root names a ruin's trace leveled with the ground.
- 89:8 مِثْلُهَا: م ث ل B005, "مثل الرجل قائما انتصب" (maqayis). Standing upright. م ث ل B006, "مثل أي لطأ بالأرض وهو من الأضداد" (sihah); "الماثل الدارس" (tahdhib). Pressed flat to the ground, or effaced. The upright structure and its flattened ruin are opposite senses of one root.
- 89:8, 89:11 ٱلْبِلَٰدِ: ب ل د B001, "البلد كل موضع مستحيز من الأرض عامر أو غير عامر أو خال أو مسكون" (tahdhib). Bounded settled land, lived in or empty.
- 89:9 جَابُوا۟ ٱلصَّخْرَ: ج و ب B001, "اجتاب احتفر" (tahdhib); "خرق الشيء" (maqayis). The dictionary quotes the ayah: "وثمود الذين جابوا الصخر بالواد" (mufradat). ص خ ر B001, "الصخر عظام الحجارة وصلابها" (ayn;tahdhib). Boring into hard, massive rock.
- 89:5 حِجْرٍ: ح ج ر B004, "الحجر منازل ثمود" (sihah); "سمي ما أحيط به الحجارة حجرا وبه سمي حجر الكعبة وديار ثمود" (mufradat). The dictionary names Thamud's stone-walled region with this word four ayat before Thamud appears. ح ج ر B003, "الحجر الجوهر الصلب المعروف" (mufradat). Stone.
- 89:6 فَعَلَ: ف ع ل B003, "الفعلة قوم يعملون عمل الطين والحفر وما أشبه ذلك من العمل" (tahdhib). The root of "how your Lord dealt" also names workers in clay and digging. The diggers are answered by the Lord's own doing.
- 89:10 ٱلْأَوْتَادِ: و ت د B001, "يجمع الوتد أوتادا؛ الجبال أوتادا" (tahdhib). Pegs, which the dictionary already compares to mountains.
- 89:9 بِٱلْوَادِ: و د ي B004, "أودى فلان أي هلك" (sihah); "أودى به المنون أي أهلكه" (tahdhib). The root of the valley where they built also names perishing.
- 89:21 دُكَّتِ… دَكًّۭا دَكًّۭا: د ك ك B001, "الدك كسر الحائط والجبل" (ayn;tahdhib); "الدك الدق وضربته وكسرته حتى سويته بالأرض" (sihah). Wall and mountain broken until level with the ground.
- Quran: 15:80–82, وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ. The people of al-Ḥijr deny the messengers.
- Quran: 7:74. Ṣāliḥ to Thamud: you carve the mountains into houses; do not spread corruption.
- Quran: 26:128–129, أَتَبْنُونَ بِكُلِّ رِيعٍ ءَايَةًۭ… مَصَانِعَ لَعَلَّكُمْ تَخْلُدُونَ. Hud to ʿĀd about their buildings on every height.
- Quran: 69:6–7, كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍۢ. ʿĀd laid flat like hollow palm trunks.
- Quran: 78:6–7, وَٱلْجِبَالَ أَوْتَادًۭا. God's own pegs.
- Quran: 69:13–14, فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ. The Day: earth and mountains crushed.
- Quran: 7:143, جَعَلَهُۥ دَكًّۭا. The mountain before Moses.
- Quran: 38:12. Pharaoh of the pegs, among the nations that denied.

### 7. Raised up and brought low
Some things rise above their limit: the tyrants who "rose over", tall columns, the high places. Then everything is brought down: the earth crushed flat, mountains made into a level plain. People are lowered in two ways. The man calls his low state humiliation (أهانن), while the soul at the end is lowered and settled (المطمئنة) and joins those who have made themselves low (عبادي). The dictionary gives each word a concrete form: a mountain top, flattened ground, a bent back, a low-lying hollow, a road trodden smooth, and a mortar where things are pounded.
- 89:11 طَغَوْا۟: ط غ ي B005, "الطغية أعلى الجبل" (sihah); "كل مكان مرتفع طغوة" (sihah). A summit, any raised place. ط غ ي B001, "مجاوزة الحد في العصيان". Rising past the limit.
- 89:7 ٱلْعِمَادِ: ع م د B005, "ذات العماد أي ذات الطول" (tahdhib) [fixed expression]. Height.
- 89:21 دُكَّتِ ٱلْأَرْضُ: د ك ك B002, "أرض دكاء مسواة وناقة دكاء لا سنام لها" (mufradat); "الأرض الدكاء الأرض العريضة المستوية" (maqayis). Ground made level, like a camel with no hump.
- 89:22 صَفًّۭا: ص ف ف B005, "الصفصف المستوي من الأرض كأنه على صف واحد" (mufradat). The dictionary derives the level plain from صفّ.
- 89:16 أَهَٰنَنِ: ه و ن B003, "الهون هوان الشيء الحقير" (ayn). Being made worthless. ه و ن B001, "يمشي على الأرض هونا" (sihah). The same root names a gentle, low walk. ه و ن B004, "الهاون: الذي يدق فيه" (sihah). A mortar. Set it beside د ك ك B001, "دككت الشيء مثل دققته" (maqayis): both are defined through دقّ, pounding.
- 89:18 ٱلْمِسْكِينِ: س ك ن B006, "تمسكن إذا خضع لله وهي المسكنة للذلة". Lowered and humbled.
- 89:27 ٱلْمُطْمَئِنَّةُ: ط م ء ن B002, "المطمئن من الأرض أرض منخفضة وهي المتطأمنة" (ayn); "طامن ظهره إذا حناه" (tahdhib). Low-lying ground, a bent back. ط م ء ن B001, "الطمأنينة والاطمئنان السكون بعد الانزعاج" (mufradat). Settling after agitation.
- 89:29 عِبَٰدِى: ع ب د B003, "العبودية إظهار التذلل والعبادة غاية التذلل" (mufradat). ع ب د B005, "الطريق المعبد وهو المسلوك المذلل" (maqayis). A road trodden smooth.
- Quran: 96:6–7, كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ أَن رَّءَاهُ ٱسْتَغْنَىٰٓ. Man rises past the limit when he sees himself as needing nothing.
- Quran: 28:4, إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ. Pharaoh rose high in the land.
- Quran: 79:24, أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ. Pharaoh's claim.
- Quran: 20:105–107, فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا. The answer to a question about the mountains: they are scattered and left as a level plain.
- Quran: 25:63, وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا. Servants, earth and the low walk in one ayah.
- Quran: 22:18, وَمَن يُهِنِ ٱللَّهُ فَمَا لَهُۥ مِن مُّكْرِمٍ. Abasement against honor.

### 8. Paired, odd and the unmatched one
Things are joined to their like or stand alone. The oath sets the pair against the odd (89:3). Iram has nothing like it, no partner (89:8). The orphan is the single one with nobody beside him (89:17). No one (أحد) punishes or binds as He does (89:25–26). Against these single things the surah doubles words: دكا دكا, صفا صفا, the paired راضية مرضية, and the soul joined to a company (في عبادي).
- 89:3 ٱلشَّفْعِ: ش ف ع B001, "ضم الشيء إلى مثله" (mufradat). The dictionary defines the pair with the word مثل of 89:8. "الشفع خلاف الوتر" (maqayis;sihah). ش ف ع B002, "الانضمام إلى آخر ناصرا له وسائلا عنه" (mufradat). Standing beside another to support him.
- 89:3 ٱلْوَتْرِ: و ت ر B001, "الوتر الفرد ضد الشفع" (jamhara). The single one.
- 89:8 لَمْ يُخْلَقْ مِثْلُهَا: م ث ل B001, "المثل النظير" (jamhara). There is no counterpart: the city is an odd one.
- 89:17 ٱلْيَتِيمَ: ي ت م B002, "كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة" (sihah); "لكل منفرد يتيم" (maqayis). The orphan is the one left alone, like the pearl with no match.
- 89:25–26 أَحَدٌۭ: ء ح د B002, "أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا" (mufradat). Not one, not two, none. ء ح د B005, "استأحد الرجل انفرد" (sihah). Being alone.
- 89:21–22 دَكًّۭا دَكًّۭا / صَفًّۭا صَفًّۭا: the surah's own doublings, where each unit has a second like it.
- 89:28 رَاضِيَةًۭ مَّرْضِيَّةًۭ: ر ض و B003, "المراضاة من اثنين" (ayn); "إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه" (mufradat). Contentment between two, one pleased and one pleasing.
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى: ع ب د B002, "فادخلي في عبادي أي في حزبي" (sihah). The single soul joined to a company.
- 89:2 عَشْرٍۢ: ع ش ر B002, "كانوا تسعة فتموا بي عشرة" (maqayis;ayn). The one who completes a group. ع ش ر B012, "عاشرته صرت له كعشرة في المصاهرة" (mufradat). Close companionship.
- Quran: 51:49, وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ. Everything created in pairs.
- Quran: 112:1, 4, قُلْ هُوَ ٱللَّهُ أَحَدٌ… وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ. The One with no equal.
- Quran: 42:11, لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ.
- Quran: 19:95 (وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا) and 6:94 (وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ). Each one comes alone on the Day.
- Quran: 74:48, فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ. Nobody standing beside them helps.
- Quran: 98:8, رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ. Contentment on both sides.

### 9. Arrival in ranks
After the pounding, a host comes. The Lord comes, the angels row upon row, and Hell is brought. The dictionary gives the distributive "they came ten by ten" with the same verb جاء, and it names the one-after-another arrival through the root of الوتر. It also has a fixed phrase for disasters "bursting in" on people in numbers, using the root of الفجر and جاء.
- 89:22 وَجَآءَ: ج ي ء B001, "المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا" (mufradat). Coming.
- 89:23 وَجِا۟ىٓءَ… بِجَهَنَّمَ: ج ي ء B004, "جاءه بكذا وأجاءه، وجاء بكذا: استحضره" (mufradat). Something brought and made present. ج ي ء B005 [fixed expression], "أجأته إلى كذا بمعنى ألجأته واضطررته إليه" (sihah). Driven to it. From memory, a hadith (Muslim): Hell is brought that day with seventy thousand reins, each pulled by seventy thousand angels.
- 89:22 وَٱلْمَلَكُ: م ل ك B009, "الملك من الملائكة واحد وجمع؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة" (sihah). The singular stands for the whole rank.
- 89:22 صَفًّۭا صَفًّۭا: ص ف ف B001, "الصف أن تجعل الشيء على خط مستو" (mufradat); "الصافات صفا يعني الملائكة" (mufradat;tahdhib); "المصف الموقف" (ayn;sihah;tahdhib). Straight lines of angels taking their stand.
- 89:2 عَشْرٍۢ: ع ش ر B005, "جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة" (maqayis;ayn;tahdhib). The dictionary uses جاء with a repeated distributive, the same build as صفا صفا.
- 89:3 ٱلْوَتْرِ: و ت ر B004, "تترى من الوتر أي واحدا بعد واحد" (sihah); "جاءوا تترى" (mufradat). Coming one after another.
- 89:1 ٱلْفَجْرِ: ف ج ر B003 [fixed expression], "انفجر عليهم القوم وانفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة" (ayn). A crowd or disasters bursting on people suddenly and in numbers.
- 89:21 دَكًّۭا: د ك ك B008 [fixed expression], "تداك عليه القوم إذا ازدحموا عليه" (tahdhib). A crowd pressing in.
- Quran: 78:38, يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا. The Day.
- Quran: 2:210, هَلْ يَنظُرُونَ إِلَّآ أَن يَأْتِيَهُمُ ٱللَّهُ فِى ظُلَلٍۢ مِّنَ ٱلْغَمَامِ وَٱلْمَلَٰٓئِكَةُ. A warning about what the deniers are waiting for.
- Quran: 18:48, وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا. People lined up before the Lord.
- Quran: 25:25–26. The sky splits and the angels are sent down.
- Quran: 39:68–69, وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ. The same passive verb, after the trumpet.
- Quran: 50:21, وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ. Every soul brought with a driver and a witness.
- Quran: 79:34–36, فَإِذَا جَآءَتِ ٱلطَّآمَّةُ… وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ. Hell made visible. See also 26:91.
- Quran: 69:13–17, وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا. The singular ٱلْمَلَكُ for the angels after the crushing.
- Quran: 23:44, ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا. Messengers one after another. Also 37:1.

### 10. Honor and abasement: the trial's two readings
A man is tested in two ways: given plenty, or kept short. He reads the plenty as honor and the shortage as humiliation (89:15–16). The surah's answer كلّا moves honor to what he fails to give: honoring the orphan (89:17). The dictionary defines the generous one as the one who gives favor (منعم), and defines the abased one as the one with no كرامة. It also names generosity with the root of الفجر, generosity that overflows. The test itself is also a wearing-out (chains 17 and 22).
- 89:15–16 ٱبْتَلَىٰهُ: ب ل و B002, "بلوته بلوا جربته واختبرته" (sihah). Testing. ب ل و B003, "اختبار الله للعباد تارة بالمسار وتارة بالمضار" (mufradat). Tested sometimes with what pleases and sometimes with what harms.
- 89:15 فَأَكْرَمَهُۥ: ك ر م B001, "الكثير الخير الجواد المنعم المفضل" (tahdhib). The dictionary joins أكرمه and نعّمه. "الكرم ضد اللؤم" (sihah).
- 89:15 وَنَعَّمَهُۥ: ن ع م B002, "نعم فلان أولاده ترفهم" (maqayis); "نعمة العيش حسنه وغضارته" (tahdhib). Given an easy, comfortable life.
- 89:16 فَقَدَرَ عَلَيْهِ رِزْقَهُۥ: ق د ر B004 [fixed expression], "قدر على عياله مثل قتر" (sihah); "ومن قدر عليه رزقه أي ضيق عليه" (mufradat). Provision kept narrow.
- 89:16 أَهَٰنَنِ: ه و ن B003, "الهين الذي لا كرامة له" (ayn). The dictionary defines abasement as the lack of كرامة. "الهوان من جهة متسلط مستخف به" (mufradat).
- 89:17 لَّا تُكْرِمُونَ ٱلْيَتِيمَ: ك ر م B001. Honor is something you do to someone, not something you hold. ك ر م B006, "كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه" (sihah). A contest in generosity, which the man never enters.
- 89:1 ٱلْفَجْرِ: ف ج ر B005, "الفجر وهو الكرم والتفجر بالخير" (maqayis); "رجل ذو فجر إذا كان يتفجر بالخير" (jamhara). The dictionary joins the root of الفجر with كرم: generosity that overflows. Its reversal is فجور (chain 2).
- Quran: 21:35, وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ.
- Quran: 7:168, وَبَلَوْنَٰهُم بِٱلْحَسَنَٰتِ وَٱلسَّيِّـَٔاتِ. The test of the Israelites.
- Quran: 39:49. When man is given a favor he says إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍۭ; the answer: بَلْ هِىَ فِتْنَةٌۭ.
- Quran: 28:82, ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ… وَيَقْدِرُ. Those who had envied Qārūn, after he is swallowed.
- Quran: 22:18 (whom God abases has none to honor him) and 49:13 (إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ).
- Quran: 44:43–49, ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ. Said in mockery to the sinner in Hell.
- Quran: 2:155, وَلَنَبْلُوَنَّكُم… وَنَقْصٍۢ مِّنَ ٱلْأَمْوَٰلِ. Testing by loss of wealth.

### 11. Shares measured out and seized
Provision is measured and handed out as shares. Each person gets a portion of food, a portion of the good, a tenth. An inheritance passes from one set of people to the next. The man swallows the inheritance whole, his own share and others' (89:19). The tyrants receive their share too: سوط عذاب, which the dictionary glosses as "a share of punishment". The dictionary joins dividing with the inheritance and its rightful owners, and joins the share with measure.
- 89:16 فَقَدَرَ: ق د ر B001, "القدر مبلغ الشيء؛ لكل شيء مقدار وأجل" (ayn). ق د ر B002, "قضاء الله تعالى الأشياء على مبالغها ونهاياتها" (maqayis). Everything given in its measure.
- 89:16 رِزْقَهُۥ: ر ز ق B001, "الرزق يقال للعطاء الجاري وللنصيب" (mufradat); "أصيل واحد يدل على عطاء لوقت" (maqayis). A running grant, and a share.
- 89:5 قَسَمٌۭ: ق س م B003, "القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما" (mufradat). The dictionary joins the root of قسم with the inheritance (التراث, 89:19) and its rightful owners (أرباب, the root of رب).
- 89:8 يُخْلَقْ: خ ل ق B006, "الخلاق النصيب لأنه قد قدر لكل أحد نصيبه" (maqayis). The dictionary joins the root of يخلق with قدر and أحد: the share measured out for each one.
- 89:13 سَوْطَ عَذَابٍ: س و ط B003 [fixed expression], "فصب عليهم ربك سوط عذاب أي نصيبا من العذاب" (maqayis); "سوط عذاب أي نصيب عذاب ويقال شدته" (sihah). The punished get their share.
- 89:19 وَتَأْكُلُونَ: ء ك ل B003, "الأكل حظ الرجل وما يعطاه من الدنيا"; "المأكلة ما جعل للإنسان لا يحاسب عليه". Eating as one's lot.
- 89:19 ٱلتُّرَاثَ: و ر ث B001, "أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب" (maqayis). Property passing to others. و ر ث B004, "يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه" (tahdhib). The dictionary joins inheritance with رجع and عباد: what servants owned goes back to the One who remains.
- 89:19 لَّمًّۭا: ل م م B001, "لممته أجمع حتى أتيت على آخره" (sihah). Taking all of it, to the last. From memory, the commentators gloss أكلا لمّا as eating one's own share together with others'.
- 89:2 عَشْرٍۢ: ع ش ر B003, "العشر جزء من عشرة أجزاء" (ayn). ع ش ر B004, "عشرت القوم إذا أخذت عشر أموالهم" (maqayis). A tenth part, and taking a tenth of people's property.
- 89:3 ٱلشَّفْعِ: ش ف ع B003, "الشفعة الزيادة حتى تضمه إلى ما عندك" (tahdhib). Adding a neighbor's share to what you already hold.
- Quran: 43:32, نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ. God answers the objection about who should receive revelation.
- Quran: 13:26 and 34:36, ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ.
- Quran: 65:7, وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ. A ruling on support after divorce.
- Quran: 4:7–8, وَإِذَا حَضَرَ ٱلْقِسْمَةَ أُو۟لُوا۟ ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينُ فَٱرْزُقُوهُم مِّنْهُ. Inheritance rules: division, orphans, the poor and provision in one ayah.
- Quran: 19:40, إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا وَإِلَيْنَا يُرْجَعُونَ. Also 57:10, وَلِلَّهِ مِيرَٰثُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ.

### 12. Feeding the needy, devouring the inheritance
People are meant to urge one another toward food for the poor. Instead they eat: the inheritance, the property of the weak, everything. The orphan is the one to whom kindness comes slowly. The dictionary says food is named the thing that lets a person stay where he lives, and it gives the eating of the weak's goods. Its root for eating also names fire eating wood. Hell arrives at 89:23.
- 89:18 تَحَٰٓضُّونَ: ح ض ض B001, "حضه على القتال حضا أي حثه… والتحاض التحاث والمحاضة أن يحث كل واحد منهما صاحبه" (sihah). Urging one another.
- 89:18 طَعَامِ: ط ع م B001, "الطعام هو المأكول والإطعام يقع حتى الماء" (maqayis). ط ع م B002, "استطعمه سأله أن يطعمه وأطعمته الطعام" (sihah). Food, and someone asking to be fed.
- 89:18 ٱلْمِسْكِينِ: س ك ن B006, "المسكين الفقير وقد يكون بمعنى الذلة والضعف". The poor, weak one. س ك ن B010, "الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن". Food named as what lets one stay. From memory, the classical gloss: المسكين is the one whom poverty has made still.
- 89:17 ٱلْيَتِيمَ: ي ت م B004, "اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه" (tahdhib). Kindness is slow to reach him. ي ت م B003, "أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره" (tahdhib). He is overlooked.
- 89:19 وَتَأْكُلُونَ: ء ك ل B004, "فلان يستأكل الضعفاء أي يأخذ أموالهم"; "أكل المال بالباطل صرفه إلى ما ينافيه الحق". Eating up the weak's goods. ء ك ل B007, "أكيلة الأسد فريسته". Prey.
- 89:19 أَكْلًۭا لَّمًّۭا: ل م م B001, "لممته أجمع حتى أتيت على آخره" (sihah). Eating everything.
- 89:20 حُبًّۭا: ح ب ب B001, "الحب والحبة في الحنطة والشعير وبزور الرياحين". The same letters as حبّ (love) name grain, food itself.
- 89:16 رِزْقَهُۥ: ر ز ق B002, "لما يصل إلى الجوف ويتغذى به" (mufradat). Provision as what reaches the belly.
- 89:19 تَأْكُلُونَ (and 89:23 جَهَنَّمَ): ء ك ل B005, "أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها". Fire eats wood. The eater is answered by the fire brought in 89:23.
- Quran: 107:1–3, فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ. The one who denies the Judgment.
- Quran: 69:25–34. The book given in the left hand; bound in chains because لَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ.
- Quran: 90:11–16, إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ يَتِيمًۭا… أَوْ مِسْكِينًۭا. The steep road.
- Quran: 4:2, وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ. Orphans' property.
- Quran: 4:10, إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا. Eating orphans' property is eating fire.
- Quran: 9:34–35. Scholars and monks eating people's goods and hoarding them; the hoard is heated in the fire of Hell.
- Quran: 76:8, وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا. Food, love, the poor and the orphan in one ayah. Also 80:24.

### 13. Gathering to the brim
Things are scraped together until the vessel is full: wealth gathered, love filling up like a measure to its rim or water in a large jar. The surah sets this beside 89:12, where corruption is made many. The dictionary gives a measure brought almost to overflowing, a large jar, filling a waterskin, and a troop massed tight.
- 89:20 جَمًّۭا: ج م م B001, "أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ" (jamhara); "كثرة الشيء واجتماعه" (maqayis). The measure filled almost to the brim.
- 89:20 وَتُحِبُّونَ / حُبًّۭا: ح ب ب B006, "أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره" (tahdhib). Filling up a waterskin. ح ب ب B007, "الحب الجرة الضخمة" (ayn;tahdhib). A large jar.
- 89:20 ٱلْمَالَ: م و ل B001, "تمول الرجل اتخذ مالا؛ مال يمال كثر ماله" (maqayis). Wealth acquired and multiplying.
- 89:19 لَّمًّۭا: ل م م B001, "لممت شعثه إذا ضممت ما كان متشعثا منتشرا" (maqayis); "كتيبة ململمة وملمومة أي مجتمعة مضموم بعضها إلى بعض" (sihah). Scattered things pulled into one mass.
- 89:12 فَأَكْثَرُوا۟: ك ث ر B002, "المكاثرة والتكاثر التباري في كثرة المال والعز" (mufradat). Competing in quantity.
- 89:23 وَأَنَّىٰ: ء ن ي B004, "الإناء ما يوضع فيه الشيء" (mufradat). The root names the vessel.
- Quran: 104:1–3, ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ. The slanderer counting his money.
- Quran: 102:1–2, أَلْهَىٰكُمُ ٱلتَّكَاثُرُ. Competing in more until the graves.
- Quran: 70:15–18, وَجَمَعَ فَأَوْعَىٰ. The Fire calls the one who gathered and stored.
- Quran: 3:14 (حُبُّ ٱلشَّهَوَٰتِ… وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ) and 100:8 (وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ).
- Quran: 50:30, يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ. Hell's own filling.

### 14. Stuck to the ground, called away
Love clings. The dictionary derives المحبة from "keeping to" something and names the camel that sinks down and will not leave its spot. The surah's land words name staying put, pressing to the ground and growing heavy toward the earth. The pegs pin the foot down. Against this weight the end of the surah calls the soul to go: ارجعي, ادخلي.
- 89:20 وَتُحِبُّونَ: ح ب ب B002, "الحب والمحبة اشتقاقه من أحبه إذا لزمه" (maqayis). Love as clinging. ح ب ب B005, "المحب البعير الذي يحسر فيلزم مكانه" (maqayis); "أحب البعير إذا حرن ولزم مكانه" (mufradat). The camel that stops and will not move.
- 89:8, 89:11 ٱلْبِلَٰدِ: ب ل د B009, "بلد بالمكان أقام به فهو بالد" (sihah). Staying in a place. ب ل د B010, "بلد الرجل بالأرض إذا لزق بها" (maqayis). Sticking to the ground. ب ل د B002, "وضعت الناقة بلدتها بالأرض إذا بركت" (maqayis). The camel kneeling with its chest on the ground.
- 89:21 ٱلْأَرْضُ: ء ر ض B006, "تأرض فلان إذا لزم الأرض" (maqayis); "التأرض أيضا التثاقل إلى الأرض" (sihah). Keeping to the earth, growing heavy toward it.
- 89:10 ٱلْأَوْتَادِ: و ت د B003, "وتد فلان رجله في الأرض إذا ثبتها" (tahdhib). The foot planted fast.
- 89:26 وَثَاقَهُۥٓ: و ث ق B003. Being bound.
- 89:28 ٱرْجِعِىٓ: ر ج ع B001, "الرجوع العود إلى ما كان منه البدء" (mufradat). Going back to where it began.
- 89:29–30 فَٱدْخُلِى: د خ ل B001. Moving inside.
- Quran: 9:38, ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا. Believers rebuked for holding back from the call: earth, being content (رضي) and life in one ayah.
- Quran: 7:176, وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ. The man who clung to the earth.
- Quran: 38:31–32, إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى. Solomon and the horses: love, remembrance and Lord.
- Quran: 87:16, بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا.

### 15. The lap and the rearing: the orphan with no one to hold him
A child is held in a lap and raised in stages under someone's care. The surah calls God رب six times; the dictionary gives that root the sense of raising, the foster parent and the stepchild. The man's Lord "pampered" him (نعّمه) as a father pampers his children, yet the orphan, the child without a father, gets no honor (89:17). حجر in 89:5 also names the lap.
- 89:5 حِجْرٍ: ح ج ر B005, "حجر المرأة وحجرها حضنها وفلان حجر فلان أي في كنفه ومنعته" (tahdhib). The lap, a protecting embrace.
- رَبُّكَ / رَبُّهُۥ / رَبِّىٓ / رَبِّكِ (89:6–28): ر ب ب B002, "التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام" (mufradat); "رب فلان ولده؛ رباه" (sihah). Raising stage by stage until complete. ر ب ب B005, "ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب" (maqayis). The foster child and the one who cares for him.
- 89:15 وَنَعَّمَهُۥ: ن ع م B002, "نعم فلان أولاده ترفهم" (maqayis). He raised his children in comfort.
- 89:17 ٱلْيَتِيمَ: ي ت م B001, "اليتيم الذي مات أبوه حتى يبلغ" (tahdhib); "انقطاع الصبي عن أبيه قبل بلوغه" (mufradat). A child cut off from his father. ي ت م B003, "أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره" (tahdhib). Neglected.
- 89:17 لَّا تُكْرِمُونَ: ك ر م B001. The honor that is withheld.
- 89:18 تَحَٰٓضُّونَ عَلَىٰ طَعَامِ: ح ض ض B001; ط ع م B002. Prompting one another to feed.
- Quran: 4:23, وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم. The marriage prohibitions: the root of رب and حجر joined in "stepdaughters in your laps".
- Quran: 93:6–9, أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ… فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ. God to the Prophet.
- Quran: 17:24, رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا. Prayer for parents.
- Quran: 26:18, أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا. Pharaoh to Moses, the tyrant claiming to have reared him.
- Quran: 4:2, 4:6. Orphans' property handed back when they mature.

### 16. Wall, cover and the interior entered
A boundary keeps things out and holds things in: a walled room, a forbidden zone, the mind that holds a person back. A cover hides what is under it: the garden's trees over the ground, night over things, earth over the dead. To enter (ادخلي) is to cross that boundary into the hidden inside. The dictionary describes فجور as tearing a cover. The surah ends with entry into a company and into a covered garden. Its other land words, البلاد and the crushed earth of 89:21, also name the grave and the earth heaped over a body.
- 89:5 حِجْرٍ: ح ج ر B001, "أصل واحد مطرد وهو المنع والإحاطة" (maqayis). Holding back and enclosing. ح ج ر B004, "الحجرة التي ينزلها الناس وهو ما حوطوا عليه" (tahdhib). A walled room. ح ج ر B002, "العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي" (maqayis). The mind as the inner wall.
- 89:1 ٱلْفَجْرِ: ف ج ر B004, "الفجور شق ستر الديانة" (mufradat). Tearing the cover of faith.
- 89:29–30 فَٱدْخُلِى: د خ ل B001, "أصل مطرد منقاس وهو الولوج" (maqayis); "الدخول نقيض الخروج" (mufradat). Going in. د خ ل B003, "الدخلة باطن أمر الرجل" (maqayis). The inside.
- 89:30 جَنَّتِى: ج ن ن B001, "أصل الجن ستر الشيء عن الحاسة" (mufradat). Hidden from the senses. ج ن ن B003, "كل بستان ذي شجر يستر بأشجاره الأرض" (mufradat). The garden covering its ground. ج ن ن B004, "الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم" (maqayis). A reward hidden from them today. ج ن ن B009, "جننت الميت وأجننته أي واريته والجنن القبر" (sihah). The grave cover is the reversal.
- 89:29 عِبَٰدِى: ع ب د B002, "فادخلي في عبادي أي في حزبي" (sihah). The company one enters.
- 89:18 ٱلْمِسْكِينِ: س ك ن B002, "المنزل وهو المسكن". The root of dwelling.
- 89:8, 89:11 ٱلْبِلَٰدِ: ب ل د B001, "البلد المكان المحيط المحدود" (mufradat); "البلد المقبرة ويقال هو نفس القبر" (tahdhib). A bounded place, and the grave.
- 89:21 دُكَّتِ: د ك ك B003 [fixed expression], "دككت التراب على الميت إذا هلته عليه" (maqayis;tahdhib). Earth heaped over the dead.
- Quran: 25:21–22, يَوْمَ يَرَوْنَ ٱلْمَلَٰٓئِكَةَ… وَيَقُولُونَ حِجْرًۭا مَّحْجُورًۭا. On the Day the angels set up a barrier for the guilty.
- Quran: 50:31–34, وَأُزْلِفَتِ ٱلْجَنَّةُ… ٱدْخُلُوهَا بِسَلَٰمٍۢ. The Garden brought near and the entry; also 15:45–46.
- Quran: 39:73, وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا. Driven to the Garden in groups.
- Quran: 27:19, وَأَدْخِلْنِى بِرَحْمَتِكَ فِى عِبَادِكَ ٱلصَّٰلِحِينَ. Solomon's prayer, with نعمتك and ترضاه in the same ayah.

### 17. The journey: night travel, crossing, wear, return, arrival, rest
The surah reads as a journey. People travel by night, cut across lands and wear out their mounts. They come back, arrive and settle. ʿĀd's name shares its root with المعاد, the place of return. The dictionary words for arriving from a journey (القدوم) and for the worn-out beast (ناقة بلو سفر, الرجيع) appear under the surah's own words. The journey ends with ارجعي إلى ربك and entry, and the soul settles after its agitation.
- 89:4 يَسْرِ: س ر ي B001, "السرى سير الليل"; "سريت سرى ومسرى وأسريت بمعنى" (sihah). Travelling by night.
- 89:9 جَابُوا۟: ج و ب B002, "جبت المفازة أي قطعتها" (ayn); "رجل جواب إذا كان قطاعا للبلاد" (tahdhib). Crossing the waste, a man always cutting across lands.
- 89:15–16 ٱبْتَلَىٰهُ: ب ل و B001, "ناقة بلو سفر أبلاها السفر" (ayn;sihah;tahdhib;mufradat). The mount worn out by travel.
- 89:28 ٱرْجِعِىٓ: ر ج ع B014, "الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال" (sihah). The beast sent out journey after journey. ر ج ع B002, "إلى الله مرجعكم وإن إلى ربك الرجعى" (mufradat). The final return.
- 89:6 بِعَادٍ: ع و د B012, "عاد قبيلة وهم قوم هود" (sihah), under the same root as B002, "المعاد المصير والمرجع" (sihah); "الآخرة معاد الخلق" (sihah). The dictionary joins عود with مرجع: the people named ʿĀd carry the root of the place one returns to. ع و د B009, "العود الطريق القديم الذي يعود إليه السفر" (mufradat). The old road travellers come back to.
- 89:24 قَدَّمْتُ: ق د م B005, "القدوم الرجوع من السفر" (ayn); "القدوم الإياب من السفر" (tahdhib). Arriving home from a journey.
- 89:22 وَجَآءَ: ج ي ء B001. Arrival.
- 89:27 ٱلْمُطْمَئِنَّةُ: ط م ء ن B001, "الطمأنينة والاطمئنان السكون بعد الانزعاج" (mufradat). Stillness after disturbance.
- 89:29–30 فَٱدْخُلِى… جَنَّتِى: د خ ل B001. Going in at the end.
- Quran: 17:1, سُبْحَٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًۭا. The Night Journey: the root of سري, servant and night joined.
- Quran: 2:155–156, إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ. Said by the patient when they are tested.
- Quran: 96:6–8, إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ. After "man rises past the limit".
- Quran: 28:85, لَرَآدُّكَ إِلَىٰ مَعَادٍۢ. A promise to the Prophet.
- Quran: 88:25, إِنَّ إِلَيْنَآ إِيَابَهُمْ.
- Quran: 23:99–100, رَبِّ ٱرْجِعُونِ… كَلَّآ. A dying denier asks to be sent back and is refused. This reverses ارجعي.
- Quran: 13:28, أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ.

### 18. Too late: sending ahead, seeking what has gone by
On the Day the man finally remembers. But in the dictionary remembering is "seeking what has passed", and أنّى asks "from where, how", while its root says the time has come or gone. His one wish is that he had sent something ahead, before its time, for his "life", which the dictionary takes to include the lasting life to come. The surah gives him three sayings: two misreadings of his trial (89:15–16) and this regret (89:24).
- 89:23 يَتَذَكَّرُ: ذ ك ر B003, "ذكر بالقلب والتذكر طلب ما فات" (ayn;tahdhib;mufradat). Remembering as reaching after what is gone.
- 89:23 ٱلذِّكْرَىٰ: ذ ك ر B009, "الذكرى اسم للتذكير" (ayn); "التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر" (mufradat). The reminder.
- 89:23 وَأَنَّىٰ: ء ن ي B005, "أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف" (sihah). From where, how. ء ن ي B003, "ما أنى لك ولم يأن لك أي لم يحن" (maqayis;ayn). Whether the time has come. ء ن ي B001, "آنيت يعني أخرت المجيء وأبطأت" (maqayis). Holding back, being slow.
- 89:24 قَدَّمْتُ: ق د م B004, "لا تقدموا معناه لا تتقدموا قبل الوقت" (tahdhib); "قدم فلان قومه أي يكون أمامهم" (ayn). Going ahead, ahead of time. ق د م B002, "القدم السابقة وكل ما قدمت من خير والعمل الصالح" (tahdhib). The good work sent ahead.
- 89:24 لِحَيَاتِى: ح ي ي B003, "الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي" (mufradat). ح ي ي B001, "الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية" (mufradat). Life, including the life after death.
- 89:15–16, 89:24 فَيَقُولُ / يَقُولُ: ق و ل B001, "القول من النطق" (maqayis). The man's three sayings.
- 89:22–23 وَجَآءَ… يَوْمَئِذٍۢ: the arrival that makes remembering come too late.
- Quran: 78:40, يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ وَيَقُولُ ٱلْكَافِرُ يَٰلَيْتَنِى كُنتُ تُرَٰبًۢا. Sending ahead, saying and يا ليتني in one ayah.
- Quran: 59:18, وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ. A command to the believers.
- Quran: 75:13 (يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ) and 82:5.
- Quran: 79:34–36, يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ. The same phrase يتذكر الإنسان, with Hell shown.
- Quran: 44:13, أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ. Also 47:18 (فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ) and 34:52.
- Quran: 29:64, وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ. Cited under ح ي ي B003.
- Quran: 23:99–100. The request to go back and do good, refused.
- Quran: 57:16, أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟. The verb of أنى's root: "has the time not come?"
- Quran: 25:27 (يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا, the wrongdoer biting his hands) and 69:25.

### 19. Blood-claim and requital
Someone has been killed. The blood stays unavenged, and the dead man's kin swear oaths shared out among themselves. Blood-money is paid or refused. Then comes requital that makes an example. The dictionary roots the oath of 89:5 in these divided oaths, names unavenged blood with the root of الوتر, and gives blood-money under الواد. مثل names exemplary punishment, and المرصاد names repayment kept ready. In the surah's order: the oath, the nations punished, the Lord at the lookout.
- 89:5 قَسَمٌۭ: ق س م B004, "اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول" (maqayis). The oath, divided among the kin of a slain man.
- 89:3 ٱلْوَتْرِ: و ت ر B002, "الوتر الذحل" (maqayis); "الوتر الترة… قتلت له ولدا أو قريبا" (jamhara); "الموتور الذي قتل له قتيل" (sihah). Blood still owed. و ت ر B003 [fixed expression], "وتره حقه أي نقصه" (sihah). Cutting someone's due short.
- 89:9 بِٱلْوَادِ: و د ي B002, "وديت القتيل أديه دية إذا أعطيت ديته" (jamhara). Blood-money.
- 89:8 مِثْلُهَا: م ث ل B002, "مثل به إذا نكل" (maqayis); "نقمة تنزل بالإنسان فيجعل مثالا يرتدع به غيره" (mufradat). Punishment that makes an example.
- 89:14 لَبِٱلْمِرْصَادِ: ر ص د B002, "أنا لك مرصد بإحسانك حتى أكافئك به"; "وإرصاد الانسان في المكافأة والخير". Requital kept ready.
- 89:24 لِحَيَاتِى: ح ي ي B013, "ولكم في القصاص حياة أي يرتدع بالقصاص" (mufradat). Life secured through retaliation.
- 89:25 لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ: the one requiter whom no one matches.
- Quran: 2:178–179, كُتِبَ عَلَيْكُمُ ٱلْقِصَاصُ… وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ. The law of retaliation.
- Quran: 17:33, فَقَدْ جَعَلْنَا لِوَلِيِّهِۦ سُلْطَٰنًۭا. Authority given to the kin of the wrongfully killed.
- Quran: 4:92, وَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦ. Accidental killing.
- Quran: 13:6, وَقَدْ خَلَتْ مِن قَبْلِهِمُ ٱلْمَثُلَٰتُ. The deniers demand punishment though exemplary punishments have already passed.
- Quran: 47:35, وَلَن يَتِرَكُمْ أَعْمَٰلَكُمْ. Cited under و ت ر B003.

### 20. The eye and the image in it
"Have you not seen?" (89:6) turns the listener's eye to what happened. The dictionary gives the eye's parts from the surah's own words: the socket (محجر), the little figure seen in the pupil (إنسان العين), the image (تمثال), the eye that sees one thing as two, the watcher. It defines the pupil's figure using the roots of both مثل and يرى. Man is called إنسان, yet he "sees" his trial wrongly.
- 89:6 أَلَمْ تَرَ: ر ء ي B001, "نظر وإبصار بعين أو بصيرة" (maqayis). Seeing with the eye or the mind. ر ء ي B013, "يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه" (mufradat). "Have you seen?" as a call to attention.
- 89:15, 89:23 ٱلْإِنسَٰنُ: ء ن س B005, "إنسان العين المثال الذي يرى في السواد أي سواد العين" (sihah). The dictionary joins الإنسان with مثال and يرى: the little image seen in the dark of the eye. ء ن س B002, "آنست الشيء إذا رأيته" (maqayis). Catching sight of something.
- 89:8 مِثْلُهَا: م ث ل B008, "التمثال الصورة" (jamhara;sihah). The image. م ث ل B011, "يكون المثل بمعنى العبرة" (tahdhib). A lesson to be seen.
- 89:5 حِجْرٍ: ح ج ر B006, "ومحجر العين ما يدور بها" (maqayis). The rim around the eye.
- 89:3 ٱلشَّفْعِ: ش ف ع B006, "عين شافعة تنظر نظرين" (tahdhib). An eye that sees double.
- 89:14 ٱلْمِرْصَادِ: ر ص د B001, "رصدته أرصده أي ترقبته". Keeping watch.
- Quran: 105:1, أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ. The same formula about another destroyed people.
- Quran: 96:7, أَن رَّءَاهُ ٱسْتَغْنَىٰٓ. Man's self-seeing.
- Quran: 50:21–22, فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ. The cover taken off the eye on the Day.
- Quran: 20:10, إِنِّىٓ ءَانَسْتُ نَارًۭا. Moses catching sight of the fire (cited under ء ن س B002).
- Quran: 46:26. ʿĀd had eyes and they did them no good.

### 21. Breath and life
Breath goes in and out of the body. The dictionary calls the self that has breath the soul and the blood, and it says morning breathes. Under the root of تر it names the lung as "the place of breath". The man wishes he had prepared for his "life" (89:24). The soul is addressed and called back (89:27–28).
- 89:27 ٱلنَّفْسُ: ن ف س B001, "التنفس خروج النسيم من الجوف" (maqayis;ayn). Breath leaving the body. ن ف س B011, "النفس الروح الذي به حياة الجسد" (ayn). The spirit by which the body lives. ن ف س B004, "النفس الدم وإذا فقد الدم فقد نفسه" (maqayis). Blood as life. ن ف س B009 [fixed expression], "تنفس الصبح" (sihah). Morning breathing.
- 89:24 لِحَيَاتِى: ح ي ي B001, "الحياة ضد الموت والحي ضد الميت" (jamhara;sihah). Life against death.
- 89:6 تَرَ: ر ء ي B009, "الرئة موضع الريح والنفس" (ayn). The dictionary joins the root of تر with النفس: the lung, where breath sits.
- 89:28 ٱرْجِعِىٓ: the breath-soul called back. From memory, the hadith of al-Barāʾ: at death the good soul is told اخرجي أيتها النفس المطمئنة.
- Quran: 81:18, وَٱلصُّبْحِ إِذَا تَنَفَّسَ.
- Quran: 6:93, أَخْرِجُوٓا۟ أَنفُسَكُمُ. The angels to wrongdoers at death (cited under ن ف س B011).
- Quran: 75:26–30, كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ… إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ. The last breath and the drive to the Lord.
- Quran: 39:42, ٱللَّهُ يَتَوَفَّى ٱلْأَنفُسَ حِينَ مَوْتِهَا. Souls taken at death and in sleep.

### 22. Measuring the hide, cutting through, wearing out
This is craftwork. A hide is measured before it is cut. Material is cut through the way a shirt's neck opening is cut. A plait is made firm. Cloth is folded, worn and worn out. The dictionary joins the root of يخلق to قدر through measuring the hide before cutting. Thamud's cutting of rock uses the shirt-opening verb. The man's trial is the root of a garment wearing out.
- 89:8 يُخْلَقْ: خ ل ق B001, "خلقت الأديم إذا قدرته قبل القطع" (sihah); "الخلق أصله: التقدير المستقيم" (mufradat). The dictionary joins خلق with قدر (89:16). خ ل ق B009, "خلق الثوب يخلق خلوقة أي بلي" (ayn). Cloth wearing out.
- 89:16 فَقَدَرَ: ق د ر B005, "قدر في السرد أي أحكمه" (tahdhib;mufradat). Making the links of mail fit. ق د ر B001, "قدر الشيء مبلغه" (sihah). Measure.
- 89:9 جَابُوا۟: ج و ب B001, "قطعك الشيء كما يجاب الجيب" (ayn); "خرق الشيء" (maqayis). Cutting as one cuts a neck opening. ج و ب B005, "اجتبت القميص إذا لبسته" (sihah). Putting the shirt on.
- 89:13 سَوْطَ: س و ط B002, "السوط الجلد المضفور" (mufradat). Plaited leather.
- 89:15–16 ٱبْتَلَىٰهُ: ب ل و B001, "بلي الثوب يبلى بلى وبلاء" (sihah;tahdhib;mufradat). The garment wearing out.
- 89:5 قَسَمٌۭ: ق س م B007, "القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه" (sihah). The one who first folds cloth into its creases.
- 89:1 ٱلْفَجْرِ: ف ج ر B001, "شق الشيء شقا واسعا" (mufradat). A wide slit.
- 89:26 وَثَاقَهُۥٓ: و ث ق B002, "وثقت الشيء: أحكمته" (maqayis). Made fast.
- Quran: 25:2, وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا. Also 54:49 and 87:2–3.
- Quran: 34:10–11, أَنِ ٱعْمَلْ سَٰبِغَٰتٍۢ وَقَدِّرْ فِى ٱلسَّرْدِ. God to David, the armorer (cited under ق د ر B005).
- Quran: 74:18–20, إِنَّهُۥ فَكَّرَ وَقَدَّرَ. The reverse: a man's own scheming measure, cursed.

## Interactions
- 1 × 2: the root of الفجر. Dawn as the dark split open (B002) and water bursting out (B001); "قيل للصبح فجر لكونه فجر الليل" (mufradat).
- 1 × 21: ن ف س B009, "إذا انشق الفجر وانفلق" (tahdhib). The dictionary explains النفس with الفجر; Quran 81:18.
- 1 × 6: ع م د B007, "عمود الصبح ابتداء ضوئه". The column of 89:7 is also dawn's first upright shaft.
- 1 × 16: ج ن ن B002 night's cover and B003 the garden's cover; ف ج ر B004 "الفجور شق ستر الديانة". The opening word splits a cover and the last word is a cover.
- 1 × 17: س ر ي B001. The night that "travels" (89:4) is the first stage of the journey; Quran 17:1 joins night, night travel and servant.
- 2 × 3: صبّ in both. "صب في الوادي إذا انحدر فيه" for the wadi and "صب الماء إراقته من أعلى" for rain. Quran 46:24: ʿĀd see the punishment coming over their wadis and call it rain.
- 2 × 7: ط غ ي B002 water rising over everything, B005 summit. The flood's rise and the tyrant's height are one root; Quran 69:11.
- 2 × 6: ع م د B013 flood dammed with stones; خ ل ق B011 rock hollow holding rain. The builders' stone and the water's hollows sit in the same wadi.
- 2 × 10: ف ج ر B004 bursting into sin, B005 overflowing generosity. One root, two directions of overflow.
- 3 × 4: ع ذ ب B001 sweet water and B005/B006 punishment and whip-tip. The downpour is life or lash.
- 4 × 5: صبّ for the lash poured (89:13) and for the snake rearing and dropping (ص ب ب B008), followed by المرصاد (89:14). The strike comes before the lookout is named.
- 4 × 14: و ت د and و ث ق. Pinned and bound to the ground; ارجعي calls the soul away from it.
- 4 × 12: Quran 69:25–34 puts binding and the failure to urge food on the poor in one scene.
- 4 × 8: أحد at 89:25–26. The punishment and the binding have no match.
- 6 × 7: د ك ك B001 "حتى سويته بالأرض", م ث ل B005/B006 (upright / flattened), خ ل ق B008 "رسم مخلولق إذا استوى بالأرض". Columns, pegs and cut rock leveled; Quran 69:14, 20:106–107.
- 6 × 8: خ ل ق B002 "ابتداع الشيء على مثال لم يسبق إليه" and ش ف ع B001 "ضم الشيء إلى مثله". The city that was never paired.
- 6 × 19: م ث ل B002 exemplary punishment and Quran 13:6 (ٱلْمَثُلَٰتُ). The ruined builders are the example.
- 7 × 10: ه و ن B003 humiliation against B001 the low, gentle walk; Quran 25:63 (servants walking on the earth هونا). The man's أهانن and the lowered servants of 89:29.
- 7 × 17: ط م ء ن B001 "السكون بعد الانزعاج" and B002 low-lying ground. The journey ends low and still.
- 7 × 14: low ground is good (المطمئنة) and heaviness toward the ground is bad (تأرض, Quran 9:38).
- 8 × 9: repetition. دكا دكا, صفا صفا and ع ش ر B005 "جاء القوم عشار عشار"; و ت ر B004 "تترى… واحدا بعد واحد". Doubled words as ranks arriving.
- 8 × 15: ي ت م B002 the single unmatched one and B001 the fatherless child.
- 9 × 16: Quran 25:21–22. The angels come and declare حِجْرًۭا مَّحْجُورًۭا.
- 9 × 18: Quran 79:34–36, جاءت + يتذكر الإنسان + Hell shown. Arrival brings the late remembering.
- 10 × 15: ك ر م and ن ع م B002 "نعم فلان أولاده ترفهم". The pampered child of a Lord who does not honor the orphan.
- 11 × 12 × 13: لمّا in all three: taking every share (11), eating everything (12), gathering into one mass (13). ء ك ل B003 eating as one's lot, B004 eating the weak's goods.
- 11 × 17: و ر ث B004 "فيرجع ما كان ملك العباد إليه" joins التراث with ارجعي and عبادي; Quran 19:40.
- 11 × 19: ق س م B003 shares of inheritance and B004 oaths divided among the kin of the slain.
- 11 × 22: ق د ر and خ ل ق B001/B006, "الخلاق النصيب لأنه قد قدر لكل أحد نصيبه". Measuring the hide and measuring the share.
- 12 × 16: س ك ن B010 "قيل للقوت سكن لأن المكان به يسكن". Food is what lets the poor stay in his dwelling.
- 13 × 2: ج م م B001. Water massing and love filling to the brim are one word.
- 13 × 14: ح ب ب B006/B007 filling a skin and a big jar, B002/B005 clinging and the camel that will not rise. Love that fills and love that sticks.
- 14 × 17: love keeps the self down (أحب البعير); the call ارجعي sets it moving. Quran 23:99–100 reverses it: the one who asks to go back is refused.
- 15 × 6: Quran 26:18. Pharaoh, a man of pegs, claims to have reared Moses.
- 16 × 17: entry (د خ ل) is where the journey (ر ج ع, ق د م B005) ends; Quran 27:19 joins entry, servants and being pleased.
- 17 × 18: ق د م B005 arriving from travel and B004/B002 going or sending ahead. One root for the arrival and for the provision sent ahead.
- 18 × 21: لحياتي and النفس. The life he did not prepare for, the soul called back; Quran 29:64.
- 20 × 8: ش ف ع B006 the eye that sees double, م ث ل the image. The eye that sees a pair where there is one.
- 20 × 10: the man is إنسان, the "figure in the eye" (ء ن س B005), yet he misreads his trial. Quran 96:7 أن رآه استغنى.

## Ayat
- **89:1 وَٱلْفَجْرِ**
  - Chain 1, Night and dawn: dawn as the dark split open. Scene: night covers, travels and is uncovered by dawn's upright shaft and breath.
  - Chain 2, Water bursting: water breaking out, the outlets of a wadi (مفاجر الوادي), bursting into sin. Scene: water bursts from rock, runs the wadi, gathers and floods past its measure, like transgression.
  - Chain 9, Arrival in ranks: disasters "bursting in" on people [fixed expression]. Scene: after the pounding the Lord and the angels come rank on rank and Hell is brought.
  - Chain 10, Honor and abasement: generosity overflowing. Scene: tested with plenty and with want, the man misreads both; honor belongs to giving.
  - Chain 16, Wall, cover and entry: فجور as tearing the cover. Scene: the mind's wall and covered places, entered by the soul at the end.
  - Chain 22, Craft: a wide slit. Scene: measure, cut, plait, fold, wear out.
- **89:2 وَلَيَالٍ عَشْرٍۢ**
  - Chain 1: the nights counted, عشر as a group of the month's nights. Scene: as in 89:1.
  - Chain 9: "جاء القوم عشار عشار". Scene: rank after rank arriving.
  - Chain 8: ten completed by one, close companionship. Scene: pair against single, with the unmatched One.
  - Chain 11: a tenth part, a tithe. Scene: provision measured out as shares and swallowed by the greedy.
- **89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ**
  - Chain 8: pair and single; ش ف ع defined as "joining a thing to its like". Scene as above.
  - Chain 1: the night's odd prayer, the forenoon's pair.
  - Chain 9: تترى, one after another.
  - Chain 19: الوتر as unavenged blood. Scene: a killing, oaths, blood-money, exemplary requital.
  - Chain 11: the neighbor's share added to one's own.
  - Chain 20: the double-seeing eye. Scene: the eye, its socket, the image in the pupil, the watcher.
- **89:4 وَٱلَّيْلِ إِذَا يَسْرِ**
  - Chain 1: night moving off, a cover lifted.
  - Chain 17, Journey: night travel. Scene: travel by night, cross the land, wear out, come back, arrive, settle, enter.
  - Chain 5, Road and ambush: night travellers on the road. Scene: travellers cross, the watcher waits, the strike drops from above.
  - Chain 6, Stone and column: سارية, the stone pillar. Scene: columns, cut rock and pegs, then leveled.
- **89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ**
  - Chain 19: the oath rooted in القسامة.
  - Chain 11: قسم as share and the dividing of inheritance.
  - Chain 22: the first folder of cloth.
  - Chain 16: حجر as enclosure and as the mind that holds back.
  - Chain 6: حجر as stone and Thamud's stone-walled land.
  - Chain 15, Lap and rearing: حجر as lap. Scene: a child raised in someone's lap; the orphan has no one to hold him.
  - Chain 20: محجر العين, the rim of the eye.
- **89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ**
  - Chain 20: seeing, and "have you seen?" as a call to attention.
  - Chain 5: the listener looks at what the watcher did.
  - Chain 21, Breath and life: the lung as "the place of breath". Scene: breath, soul, blood and life; the soul called back.
  - Chain 6: الفعلة, diggers in clay. Scene as above.
  - Chain 17: عاد, the people whose root names the place of return.
  - Chain 3, Rain: the Lord's root names nursing cloud and gathered water. Scene: rain pours, comes back, revives soil and grows the covering garden, or falls as punishment.
  - Chain 15: the Lord as the one who rears.
- **89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ**
  - Chain 6: column, tall building, tent pole; إرم as stone markers (from memory).
  - Chain 7, Raised and lowered: height. Scene: what rose past its limit is crushed flat; the soul is lowered and settled.
  - Chain 1: عمود الصبح.
  - Chain 2: the flood dammed with stones.
- **89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ**
  - Chain 6: made on no earlier model; standing upright against pressed flat or effaced; leveled trace.
  - Chain 8: no counterpart.
  - Chain 11: الخلاق, the share measured for each one.
  - Chain 22: measuring the hide before cutting, cloth wearing out.
  - Chain 2: the rock hollow that holds rain.
  - Chain 19 and chain 20: exemplary punishment, and the image (تمثال).
  - Chain 4, Lash and bond: البلد as the mark on the skin. Scene: lash poured, mark left, peg driven, rope tied, matched by no one.
  - Chain 14, Stuck to the ground: staying, pressing to the ground. Scene: love clings like a kneeling camel and the call ارجعي pulls the soul away.
  - Chain 16: البلد as bounded place and as grave.
  - Chain 5: the lands that are crossed (جابوا with البلاد).
- **89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ**
  - Chain 6: boring into hard rock in the valley; the valley's root names perishing.
  - Chain 2: the wadi as the flood's channel, the hollow torn in the ground.
  - Chain 5 and chain 17: crossing lands.
  - Chain 22: cutting like a shirt opening.
  - Chain 19: blood-money.
- **89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ**
  - Chain 6: pegs, compared to mountains.
  - Chain 4: the stake and the pinned body.
  - Chain 14: the foot planted fast.
- **89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ**
  - Chain 2: the flood rising over everything.
  - Chain 7: the summit, rising past the limit.
  - Chain 5: overstepping while crossing.
  - Chain 4 and chain 14: as in 89:8.
- **89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ**
  - Chain 2: volume growing, things leaving their balance as water leaves its measure.
  - Chain 13, Gathering to the brim: competing in quantity. Scene: wealth gathered and love filled to the rim like a jar.
- **89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ**
  - Chain 4: the plaited lash mixed into the skin; the whip's tip as the root of punishment; foot put in the fetter.
  - Chain 3: pouring from above; عذب as sweet water.
  - Chain 2: running down into the wadi.
  - Chain 5: the snake dropping from above.
  - Chain 11: سوط عذاب as a share of punishment.
  - Chain 22: plaited leather.
- **89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ**
  - Chain 5: the road, the lookout post, the waiting snake.
  - Chain 19: requital kept ready.
  - Chain 20: keeping watch.
  - Chain 3: the first rain, ground waiting to sprout.
- **89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ**
  - Chain 10: testing; the generous one defined as the one who gives favor.
  - Chain 15: the Lord pampering him as a father pampers his children.
  - Chain 3: the cloud that gives rain generously.
  - Chain 17: the mount worn out by travel.
  - Chain 22: the garment wearing out.
  - Chain 18, Too late: his first saying. Scene: he misreads his trial, then on the Day remembers too late and wishes he had sent something ahead.
  - Chain 20: إنسان, the figure in the pupil.
- **89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ**
  - Chain 10: provision kept narrow; abasement as the lack of كرامة.
  - Chain 11: measure, provision as a share.
  - Chain 7: humiliation against the low walk; the mortar for pounding.
  - Chain 3: rain as provision.
  - Chain 2: the measure the flood breaks.
  - Chain 22: making the mail fit.
  - Chain 12, Feeding and devouring: provision as what reaches the belly. Scene: urge each other to feed the poor, or eat the inheritance whole, then face the fire that eats.
  - Chain 18: his second saying.
- **89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ**
  - Chain 10: honor moved to giving.
  - Chain 15: the fatherless child, overlooked.
  - Chain 8: the unmatched one.
  - Chain 12: the one kindness is slow to reach.
- **89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ**
  - Chain 12: urging one another; food; asking to be fed; food as what lets one stay.
  - Chain 7: the poor man brought low.
  - Chain 16: the root of dwelling.
  - Chain 15: prompting one another to feed.
- **89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا**
  - Chain 12: eating up the weak's goods; fire eating wood.
  - Chain 11: eating as one's lot; inheritance passing on and going back to the One who remains; taking every share.
  - Chain 13: scattered things pulled into one mass.
- **89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا**
  - Chain 13: a measure filled almost to the brim, a skin filled, a big jar, wealth piling up.
  - Chain 14: love as clinging, the camel that will not move.
  - Chain 2: the bulk of gathered water.
  - Chain 12: حبّ as grain.
- **89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا**
  - Chain 6: wall and mountain broken level with the ground.
  - Chain 7: level ground like a humpless camel.
  - Chain 8: the doubled word.
  - Chain 9: a crowd pressing in [fixed expression].
  - Chain 16: earth heaped over the dead [fixed expression].
  - Chain 3: soft fertile soil.
  - Chain 14: keeping to the earth, growing heavy toward it.
- **89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا**
  - Chain 9: coming; the angel standing for the rank; straight lines taking their stand.
  - Chain 7: the level plain (صفصف).
  - Chain 8: the doubled word.
  - Chain 17: arrival.
  - Chain 2: the pit where rain gathers.
- **89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ**
  - Chain 9: Hell brought and made present; driven [fixed expression].
  - Chain 18: remembering as seeking what has passed; from where, how; the time come or gone.
  - Chain 12: the fire that answers the eater.
  - Chain 1: the night's hours.
  - Chain 13: the vessel.
  - Chain 20: the figure in the pupil.
- **89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى**
  - Chain 18: going ahead of time, the good work sent ahead; life including the life to come; his third saying.
  - Chain 17: arriving home from a journey.
  - Chain 21: life against death.
  - Chain 3: rain as the earth's life.
  - Chain 19: life through retaliation.
- **89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ**
  - Chain 4: severe pain that no one can match.
  - Chain 8: not one, not two.
  - Chain 19: the unmatched requiter.
  - Chain 3: punishment's root as sweet water.
- **89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ**
  - Chain 4: the rope and the tying.
  - Chain 14: being bound.
  - Chain 22: made fast.
  - Chain 8: no one matches.
- **89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ**
  - Chain 21: breath, spirit, blood.
  - Chain 1: morning breathing [fixed expression].
  - Chain 7: low-lying ground, a bent back.
  - Chain 17: stillness after disturbance.
- **89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ**
  - Chain 17: going back to where it began; the final return; the worn-out beast sent journey after journey.
  - Chain 3: rain pours and comes back.
  - Chain 14: the call that pulls away from the ground.
  - Chain 8: contentment between two.
  - Chain 21: the soul called back.
- **89:29 فَٱدْخُلِى فِى عِبَٰدِى**
  - Chain 16: going in; the company one enters.
  - Chain 8: the single soul joined to a company.
  - Chain 7: servants who make themselves low; a road trodden smooth.
  - Chain 17: entry at the journey's end.
  - Chain 14: moving inside.
- **89:30 وَٱدْخُلِى جَنَّتِى**
  - Chain 16: hidden from the senses; a reward hidden for now; the grave cover as reversal.
  - Chain 3: the garden covering its ground, plants thickening.
  - Chain 1: night's covering.
  - Chain 17: entry at the journey's end.

