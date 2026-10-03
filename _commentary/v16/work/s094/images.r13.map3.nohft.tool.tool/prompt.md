Surah: 94. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (94:1 to 94:8), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s094/surah.r2/text.md =====
# Surah 94

- 94:1 أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- 94:2 وَوَضَعْنَا عَنكَ وِزْرَكَ
- 94:3 ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- 94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ
- 94:5 فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- 94:6 إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- 94:7 فَإِذَا فَرَغْتَ فَٱنصَبْ
- 94:8 وَإِلَىٰ رَبِّكَ فَٱرْغَب


===== _commentary/v16/out/s094/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### C1. The load on the back, its creak, and its setting-down
A torso carries a load. The chest is its front and the back takes the weight. The load is a bundle that a man makes by spreading his garment, filling it and lifting it. Its weight makes the back creak. Then someone takes it down and off the bearer. In 94:1–3 the surah names the chest, then the burden set down off "you", then the back that the burden "made creak". The relative clause in 94:3 describes the burden only by what it did to the back. The dictionary joins two of the surah's words in one phrase: "أنقض الحمل ظهره أي أثقله" (sihah). وضع is defined against رفع ("وهو ضد رفعته"), so the lowering in 94:2 already looks ahead to the raising in 94:4.
- 94:1 صَدْرَكَ: ص د ر B001: "الصدر الجارحة" (mufradat); "المصدور الذي يشتكي صدره" (maqayis;sihah). The front of the loaded body, the place where pressure is felt.
- 94:2 وَضَعْنَا: و ض ع B001: "أصل واحد يدل على الخفض للشيء وحطه" (maqayis); "وضعت الشيء أضعه وضعا وهو ضد رفعته" (tahdhib). Lowering the load and putting it down; with عن, taking it off the one who carries it.
- 94:2 وِزْرَكَ: و ز ر B002: "الوزر حمل الرجل إذا بسط ثوبه فجعل فيه المتاع وحمله" (maqayis); "قد وزرت الشيء أي حملته والآثام تسمى أوزارا" (tahdhib); "الوزر الثقل ويعبر بذلك عن الإثم" (mufradat). The bundle, its weight, and guilt named as weight.
- 94:3 أَنقَضَ: ن ق ض B005: "أنقض الحمل ظهره أي أثقله" (sihah); "الظهر إذا أثقله حمله سمع له نقيض" (tahdhib); "أنقض ظهرك" (mufradat); "كل صوت لمفصل أو إصبع أو ضلع فهو نقيض" (tahdhib). The weight presses until the joints and ribs of the back can be heard.
- 94:3 ظَهْرَكَ: ظ ه ر B002: "ظهر الإنسان خلاف بطنه" (maqayis); "رجل ظهر يشتكي ظهره" (maqayis;sihah;tahdhib;mufradat). The surface that bears the load, and a man who complains of his back.
- 94:4 رَفَعْنَا: ر ف ع B009: "رفاعة المقيد خيط يرفع به قيده إليه" (sihah); "الرفاع حبل القيد يأخذه المقيد بيده يرفعه إليه" (tahdhib). A cord that lifts the weight of a fetter off a bound man.
- Quran: 6:31: the deniers, overtaken by the Hour: "وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ" (وزر on the back, the reverse of 94:2–3). 35:18: no burden-bearer carries another's burden, and "إِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌ". 53:38: same rule, in the scrolls of Moses and Abraham. 16:25 and 29:12–13: misleaders carry full burdens, and the deniers' false offer to carry others' sins. 20:100–101 (from memory): whoever turns away from the reminder carries a وزر on the Day, "وساء لهم يوم القيامة حملا". 7:157: the unlettered prophet "يَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ" (وضع عن with a load and fetters, as in 94:2). 73:5: God to the Prophet: "إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًا ثَقِيلًا". 4:28: "يُرِيدُ ٱللَّهُ أَن يُخَفِّفَ عَنكُمْ".

### C2. The pack-camel on the road: mounting, gait, wear, water, halt
"Back" also names the riding and pack animal itself. The surah's words make a whole caravan scene. The camel lowers its neck to be mounted and carries loads. It travels at a lower (وضع) or higher (رفع) gait. It may be ridden before it is trained, or be light and compliant. It is worn thin by journeys while its saddle creaks. The riders keep going all day and chant. The animals come to water at noon and leave the water, then halt and graze. Some phrases join two of the surah's words: "الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع" (maqayis) joins وضع, رفع and an easy pace; "مرفوع الناقة في سيرها خلاف الموضوع" (maqayis); "نصب القوم السير نصبا إذا رفعوه" (jamhara) joins نصب and رفع; "العاسر من النوق إذا عدت رفعت ذنبها" (maqayis) joins عسر and رفع.
- 94:3 ظَهْرَكَ: ظ ه ر B005: "الظهر الركاب تحمل الأثقال في السفر" (ayn;tahdhib); "يعبر عن المركوب بالظهر وظهري معد للركوب" (mufradat). The back as the mount that carries loads.
- 94:3 أَنقَضَ: ن ق ض B002: "البعير المهزول نقض كأن الأسفار نقضته" (maqayis); "البعير الذي أضناه السفر وكذلك الناقة" (sihah). The camel worn down by journeys.
- 94:3 أَنقَضَ: ن ق ض B005: "النقيض صوت المحامل والرحال" (sihah). The creak of litters and saddles under load.
- 94:3 أَنقَضَ: ن ق ض B006: "الإنقاض زجر القعود" (maqayis); "الانقاض أصوات صغار الابل" (sihah). The click that urges a young camel on, and the cries of young camels.
- 94:2 وَضَعْنَا: و ض ع B013: "اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه" (tahdhib). The standing camel's neck lowered for the rider.
- 94:2 وَضَعْنَا: و ض ع B003: "الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع" (maqayis); "وضع البعير وغيره أي أسرع في سيره" (sihah). An easy or quick gait, set against the "raised" gait.
- 94:2 وَضَعْنَا: و ض ع B007: "إبل واضعة أي مقيمة في الحمض" (tahdhib). Camels halted at saltbush pasture.
- 94:4 رَفَعْنَا: ر ف ع B003: "مرفوع الناقة في سيرها خلاف الموضوع" (maqayis); "المرفوع من حضر الفرس والبرذون دون الحضر وفوق الموضوع" (ayn;tahdhib). The higher gait, ranked above the وضع gait.
- 94:4 رَفَعْنَا: ر ف ع B011: "رفع القوم فهم رافعون إذا أصعدوا في البلاد" (tahdhib). A party pushing up-country.
- 94:5–6 ٱلْعُسْرِ: ع س ر B008: "العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض" (sihah). The camel ridden before it is broken in.
- 94:5–6 ٱلْعُسْرِ: ع س ر B009: "العاسر من النوق إذا عدت رفعت ذنبها" (maqayis). The running camel with its tail lifted.
- 94:5–6 يُسْرًا: ي س ر B005: "ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس" (ayn); "دابة حسن التيسور أي حسن نقل القوائم" (sihah). The light, compliant mount that moves its legs well; the opposite of the untrained one.
- 94:7 فَرَغْتَ: ف ر غ B003 [fixed expression]: "فرس فريغ أي واسع المشي" (maqayis;sihah); "طريق فريغ واسع" (maqayis). The wide-striding horse and the broad road.
- 94:7 فَٱنصَبْ: ن ص ب B010: "نصب القوم ساروا يومهم وهو سير لين" (sihah); "نصب القوم السير نصبا إذا رفعوه" (jamhara). A gentle daylong march, or raising the pace.
- 94:7 فَٱنصَبْ: ن ص ب B004: "النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي" (maqayis). Fatigue from staying upright on the road.
- 94:7 فَٱنصَبْ: ن ص ب B009: "النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان" (tahdhib). The riders' chant.
- 94:8 فَٱرْغَب: ر غ ب B002: "فرس رغيب الشحوة كثير الأخذ بقوائمه من الأرض" (jamhara). The horse whose stride takes in much ground.
- 94:3 ظَهْرَكَ: ظ ه ر B004: "الظاهرة أن ترد كل يوم ظهرا" (sihah;tahdhib). Coming to water at noon each day. ظ ه ر B015: "سلكنا الظهر يريدون طريق البر" (maqayis). The overland road.
- 94:1 صَدْرَكَ: ص د ر B003: "صدرت الإبل عن الماء" (mufradat); "طريق صادر يصدر بأهله عن الماء" (ayn;sihah;tahdhib). Camels and travellers leaving the water.
- 94:8 رَبِّكَ: ر ب ب B007: "مرب الإبل حيث لزمته" (sihah); "أرب فلان بالمكان إذا أقام به فلم يبرحه" (tahdhib). The place where camels stay put: the halt.
- Quran: 16:5–7: God's signs in livestock: "وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ ۚ إِنَّ رَبَّكُمْ لَرَءُوفٌ رَّحِيمٌ". 43:12–14: mounts provided "لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ … وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ"; one passage holds the backs of mounts, remembering, the Lord, and the journey "to our Lord". 9:47: the hypocrites "لَأَوْضَعُوا۟ خِلَٰلَكُمْ" (riding fast in among the ranks). 18:62: Moses to his young companion after passing the meeting-point: "لَقَدْ لَقِينَا مِن سَفَرِنَا هَٰذَا نَصَبًا" (scene opens 18:60). 88:17–19: "أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ … كَيْفَ رُفِعَتْ … كَيْفَ نُصِبَتْ".

### C3. Lowered and raised: rank and name
In 94:2 and 94:4 the same speaker ("-نا") and the same addressee set two verbs against each other: وضعنا عنك… رفعنا لك. What is lowered is the weight. What is raised is the name. The dictionary carries this opposition into rank, in "رجل وضيع بين الضعة في مقابلة رفيع" (mufradat). It also joins the surah's two words directly: under رفع, "في الذكر إذا نوهته" (mufradat). The renown that is raised is itself height, in "الذكر العلاء والشرف" (maqayis). The chest gives the place of honour (the top of the assembly) and a win by a chest's length. The back gives a reproach that does not stick.
- 94:2 وَضَعْنَا: و ض ع B005: "الوضيع الدنئ من الناس وفي حسبه ضعة" (sihah); "رجل وضيع ضد الشريف والتواضع التذلل" (tahdhib); "رجل وضيع بين الضعة في مقابلة رفيع" (mufradat). The low station. Here the weight is lowered, not the person.
- 94:4 رَفَعْنَا: ر ف ع B002: "رفع الرجل يرفع رفاعة فهو رفيع إذا شرف" (ayn;tahdhib); "الرفعة نقيض الذلة" (tahdhib); "في الذكر إذا نوهته" (mufradat); "في المنزلة إذا شرفتها" (mufradat). Raising rank, and raising a name by proclaiming it.
- 94:4 ذِكْرَكَ: ذ ك ر B007: "الذكر العلاء والشرف" (maqayis); "الذكر الصيت والثناء وذي الذكر أي ذي الشرف" (sihah); "وإنه لذكر لك ولقومك أي شرف" (mufradat). Renown as height and honour.
- 94:1 صَدْرَكَ: ص د ر B002: "صدر المجلس والكتاب والكلام" (mufradat); "الصدر أعلى مقدم كل شيء" (ayn;tahdhib); "صدر الفرس إذا جاء قد سبق بصدره" (sihah;tahdhib;mufradat). The head of the assembly, the top front of a thing, winning by the chest.
- 94:3 ظَهْرَكَ: ظ ه ر B013 [fixed expression]: "ظهر عني هذا العيب أي نبا عني ولم يعلق بي" (tahdhib); "تلك شكاة ظاهر عنك عارها" (maqayis;sihah;tahdhib). Shame that falls away and does not cling.
- 94:3 ظَهْرَكَ: ظ ه ر B007 [fixed expression]: "ظهرت على الرجل غلبته وظهرت البيت علوته" (sihah). Climbing on top of something; getting the upper hand.
- Quran: 55:7: "وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ" (رفع and وضع in one ayah of the Lord's works, continuing to 55:10 "وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ"). 56:3: the Event "خَافِضَةٌ رَّافِعَةٌ" (from memory). 43:44: to the Prophet about the Revelation: "وَإِنَّهُۥ لَذِكْرٌ لَّكَ وَلِقَوْمِكَ". 21:10 (from memory): "كتابا فيه ذكركم". 19:50: the line of Abraham: "وَجَعَلْنَا لَهُمْ لِسَانَ صِدْقٍ عَلِيًّا". 19:57 (from memory): Idris: "ورفعناه مكانا عليا". 24:36: "فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ" (رفع and ذكر together). 58:11 (from memory): God raises believers and those given knowledge by degrees. The tradition that God's name is not mentioned without the Prophet's being mentioned with it (in the call to prayer and the testimony) is the standard gloss of 94:4 (from memory).

### C4. Placed, raised, erected, undone: building, spear, rope
The surah's four main verbs are also verbs of building. وضع places a thing on its site. رفع raises it high. نصب sets it upright and standing out. نقض takes apart what was made firm. The dictionary links them in its own definitions: "الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها" (mufradat) joins رفع and وضع; "نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر" (mufradat) joins نصب, وضع and building; "كل شيء رفعته فقد نصبته" (jamhara) joins نصب and رفع. Undoing applies to rope and building alike. Under عسر there is a game in which a post is erected and then knocked out.
- 94:2 وَضَعْنَا: و ض ع B001: "الوضع أعم من الحط ومنه الموضع" (mufradat); "الموضع المكان ومصدر وضعت الشيء من يدي" (sihah). Setting a thing on its site.
- 94:3 أَنقَضَ: ن ق ض B001: "نقضت الحبل والبناء؛ نقض العهد" (maqayis); "إفساد ما أبرمت من حبل أو بناء" (ayn;tahdhib); "نقضت البناء والحبل والعقد؛ استعير نقض العهد" (mufradat). Undoing a twisted rope or a building, and by extension a covenant.
- 94:4 رَفَعْنَا: ر ف ع B001: "الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها" (mufradat); "في البناء إذا طولته" (mufradat). Lifting placed bodies off their base; building something tall.
- 94:7 فَٱنصَبْ: ن ص ب B001: "نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر" (mufradat); "النصب رفعك شيئا تنصبه قائما منتصبا" (ayn;tahdhib); "كل شيء رفعته فقد نصبته" (jamhara); "نصبت الشئ إذا أقمته" (sihah). Setting upright a spear, a building or a stone.
- 94:1 صَدْرَكَ: ص د ر B002: "صدر القناة أعلاها" (ayn;sihah;tahdhib;mufradat). The top of the erected spear-shaft.
- 94:5–6 ٱلْعُسْرِ: ع س ر B013: "العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع" (tahdhib). A post set upright, then struck and uprooted. The phrase joins عسر with ينصبون.
- 94:8 رَبِّكَ: ر ب ب B016: "الربى: العقدة المحكمة" (tahdhib). The firmly tied knot, the opposite of the undone rope.
- Quran: 2:127: "وَإِذْ يَرْفَعُ إِبْرَٰهِۦمُ ٱلْقَوَاعِدَ مِنَ ٱلْبَيْتِ وَإِسْمَٰعِيلُ رَبَّنَا تَقَبَّلْ مِنَّآ". 3:96 (from memory): "إن أول بيت وضع للناس للذي ببكة". 88:17–20: camel, sky "رُفِعَتْ", mountains "نُصِبَتْ", earth spread. 55:7–10: sky raised, balance and earth "وضع". 16:92: "كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًا" (undoing yarn after it was spun firm, said of broken oaths).

### C5. The opened chest: spread, widened, explained
شرح is a laying open: flesh cut and spread flat, a hard passage of speech opened out and its hidden sense brought to view, a chest widened to receive what is good. The dictionary joins the surah's two words in "شرح الله صدره فانشرح إذا اتسع لقبول الخير" (jamhara) and "شرح الصدر أي بسطه بنور إلهي وسكينة" (mufradat). The same act of spreading (بسط) defines the burden of 94:2, a garment spread and filled ("إذا بسط ثوبه"). So one spread cloth makes the bundle on the back, and the spreading of the chest takes its place. The opposite is the narrow chest of the Quran's other passages.
- 94:1 نَشْرَحْ: ش ر ح B003: "الشرح السعة وشرح الله صدره للإسلام أي وسعه" (ayn); "شرح الله صدره فانشرح أي وسع صدره لقبول الحق فاتسع" (tahdhib); "شرح الصدر أي بسطه بنور إلهي وسكينة" (mufradat). Widening the chest to take in good.
- 94:1 نَشْرَحْ: ش ر ح B002: "أصل الشرح بسط اللحم ونحوه" (mufradat); "الشرح والتشريح قطع اللحم على العظام والقطعة شرحة" (ayn); "الشريحة من اللحم القطعة المرققة" (jamhara). The physical act: flesh cut and spread thin.
- 94:1 نَشْرَحْ: ش ر ح B001: "شرح المشكل من الكلام بسطه وإظهار ما يخفى من معانيه" (mufradat); "شرحت لك الأمر إذا أوضحته وكشفته" (jamhara). Opening a closed matter so that it lies plain.
- 94:1 صَدْرَكَ: ص د ر B001: "الصدر الجارحة" (mufradat). The organ that is opened.
- 94:2 وِزْرَكَ: و ز ر B002: "الوزر حمل الرجل إذا بسط ثوبه فجعل فيه المتاع وحمله" (maqayis). The other spreading: cloth spread out to make a load.
- 94:8 فَٱرْغَب: ر غ ب B002: "أصل الرغبة السعة في الشيء" (mufradat). The final verb also comes from breadth.
- Quran: 20:25–26: Moses, sent to Pharaoh (scene opens 20:24): "رَبِّ ٱشْرَحْ لِى صَدْرِى وَيَسِّرْ لِىٓ أَمْرِى". 6:125: "يَشْرَحْ صَدْرَهُۥ لِلْإِسْلَٰمِ … يَجْعَلْ صَدْرَهُۥ ضَيِّقًا حَرَجًا كَأَنَّمَا يَصَّعَّدُ فِى ٱلسَّمَآءِ". 39:22: "أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍ مِّن رَّبِّهِۦ". 16:106 (from memory): the reversal, "من شرح بالكفر صدرا". 26:12–13: Moses: "وَيَضِيقُ صَدْرِى وَلَا يَنطَلِقُ لِسَانِى فَأَرْسِلْ إِلَىٰ هَٰرُونَ". 15:97 and 11:12 (from memory): the Prophet's chest straitened by what they say. 7:2: "فَلَا يَكُن فِى صَدْرِكَ حَرَجٌ مِّنْهُ". 9:118: the three left behind, "ضَاقَتْ عَلَيْهِمُ ٱلْأَرْضُ بِمَا رَحُبَتْ وَضَاقَتْ عَلَيْهِمْ أَنفُسُهُمْ", then relieved.

### C6. The vessel: widened, emptied, poured out, wide-bellied
This chain is about how much a vessel holds and what it holds. The chest is widened, so its room grows. A vessel or heart is emptied (فرغ), and a bucket is poured out from its spout. The ayah's final verb comes from رغب, whose root sense is the wide-bellied thing: a wide basin, a wide skin, a big-bellied man with a big appetite, and the large gift that is wanted. There is also water gathered in plenty, and a basin built of upright stones. فرغ and رغب share ر and غ, and the surah closes on the two words one after the other (94:7 and 94:8). The emptied vessel and the wide vessel stand at its last two ayat.
- 94:1 نَشْرَحْ: ش ر ح B003: "الشرح السعة" (ayn). The capacity widened.
- 94:7 فَرَغْتَ: ف ر غ B001: "الفراغ خلاف الشغل" (maqayis;mufradat); "فؤاد أم موسى فارغا أي خاليا من الصبر" (ayn); "كأنما فرغ من لبها" (mufradat); "حتى إذا فرغ عن قلوبهم أي ذهب بالخوف" (ayn). A heart emptied of patience, or emptied of fear. The ayn's last phrase reads 34:23 as فُرِّغ; the standard text has فُزِّعَ.
- 94:7 فَرَغْتَ: ف ر غ B002: "أفرغت الدلو صببت ما فيه ومنه استعير أفرغ علينا صبرا" (mufradat); "تفريغ الظروف إخلاؤها" (sihah); "الفرغ مفرغ الدلو الذي ينصب منه الماء" (maqayis). Pouring out a bucket, emptying containers, the bucket's spout.
- 94:8 فَٱرْغَب: ر غ ب B002: "الشيء الرغيب الواسع الجوف وحوض رغيب وسقاء رغيب" (maqayis); "رجل رغيب واسع الجوف أكول وحوض رغيب أي واسع" (ayn). A wide-bellied basin, skin or man.
- 94:8 فَٱرْغَب: ر غ ب B003: "الرغب بالضم الشره" (sihah). The wide belly's craving.
- 94:8 فَٱرْغَب: ر غ ب B004: "الرغيبة العطاء الكثير الذي يرغب في مثله" (jamhara). The large gift that fills it.
- 94:7 فَٱنصَبْ: ن ص ب B003: "النصيب الحوض ينصب من الحجارة" (maqayis); "النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد" (maqayis). A basin built of upright stones around the well's lip.
- 94:8 رَبِّكَ: ر ب ب B013: "الربب وهو الماء الكثير سمي بذلك لاجتماعه" (maqayis). Water gathered in plenty.
- Quran: 28:10: "وَأَصْبَحَ فُؤَادُ أُمِّ مُوسَىٰ فَٰرِغًا … لَوْلَآ أَن رَّبَطْنَا عَلَىٰ قَلْبِهَا". 2:250: Talut's men facing Goliath: "رَبَّنَآ أَفْرِغْ عَلَيْنَا صَبْرًا". 7:126 (from memory): Pharaoh's converted magicians: "ربنا أفرغ علينا صبرا". 34:23: "حَتَّىٰٓ إِذَا فُزِّعَ عَن قُلُوبِهِمْ" (read فُرِّغ in the reading the ayn cites). 100:10 (from memory): "وحصل ما في الصدور": the chest as a container.

### C7. Hardship paired with ease
عسر and يسر are defined by each other in every source ("العسر نقيض اليسر"). The surah sets them side by side twice, joined by مع: ease comes with hardship, not after it. In the dictionary hardship is a twisting, resisting thing ("الخلاف والالتواء"). Ease is a thing made smooth and ready, and it is also small and light. Both roots also name the left hand, and the dictionary joins them in a single person: "رجل أعسر يسر للذي يعمل بكلتا يديه" (sihah). That is a man whose two hands work together. Read with مع, it gives the pair one body. Hardship is also a day: "أمر عسير ويوم عسير". The repetition in 94:5–6 is read in the tradition (from memory) as "لن يغلب عسر يسرين": the definite العسر is one hardship, the two indefinite يسرا are two eases.
- 94:5–6 ٱلْعُسْرِ: ع س ر B001: "أصل صحيح واحد يدل على صعوبة وشدة" (maqayis); "العسر نقيض اليسر" (maqayis;ayn;sihah;tahdhib;mufradat); "العسرى الأمور التي تعسر ولا تتيسر" (tahdhib); "أمر عسير ويوم عسير" (all). Hardness and severity, always defined against ease.
- 94:5–6 يُسْرًا: ي س ر B001: "اليسر: ضد العسر" (maqayis;mufradat); "تيسر واستيسر أي تسهل وتهيأ" (mufradat); "ياسره أي ساهله" (sihah). Made smooth and ready.
- 94:5–6 ٱلْعُسْرِ: ع س ر B004: "العسر الخلاف والالتواء" (maqayis;ayn); "عسر عليه الأمر أي التاث" (sihah). Hardship as twisting resistance.
- 94:5–6 يُسْرًا: ي س ر B002: "اليسير: القليل، وشيء يسير أي هين" (sihah). Ease as small and light.
- 94:5–6 ٱلْعُسْرِ / يُسْرًا: ع س ر B005; ي س ر B004: "رجل أعسر يسر للذي يعمل بكلتا يديه" (sihah); "العسرى خلاف اليسرى" (maqayis;sihah). Two hands, one worker.
- 94:5–6 ٱلْعُسْرِ: ع س ر B010 [fixed expression]: "يوم أعسر أي مشئوم" (tahdhib). The hard, ill-omened day.
- Quran: 65:7: "سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍ يُسْرًا", after the rule on spending by the wealthy and the straitened (scene opens 65:1). 65:4: "وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًا". 2:185: the fast, eased for the sick and the traveller: "يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ". 92:5–10: "فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ … فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ". 87:8 (from memory): to the Prophet: "ونيسرك لليسرى". 20:26: Moses: "وَيَسِّرْ لِىٓ أَمْرِى". 54:40: "وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ" (يسر with ذكر).

### C8. The debtor's straits and the creditor's remission
A man falls from plenty into want. His creditor presses him. The case may go before the ruler. Part of the capital can be taken off, or the debtor can be given time until he has means again. Read in this scene, "وضعنا عنك" is the remission of part of a debt, and 94:5–6 is the fall from ميسرة to عسرة turned the other way. The dictionary joins the surah's two words: "أعسر الرجل إذا صار من ميسرة إلى عسرة" (maqayis) and "عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته" (maqayis).
- 94:5–6 ٱلْعُسْرِ: ع س ر B002: "العسر قلة ذات اليد" (ayn); "أعسر الرجل إذا صار من ميسرة إلى عسرة" (maqayis); "العسرة تعسر وجود المال" (mufradat). Little in hand; the fall from means.
- 94:5–6 ٱلْعُسْرِ: ع س ر B003: "عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته" (maqayis); "عسرت الغريم أعسره عسرا إذا أخذته على عسرة ولم ترفق به" (tahdhib). The creditor who presses without granting time.
- 94:5–6 يُسْرًا: ي س ر B003: "الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى" (sihah). Means restored.
- 94:2 وَضَعْنَا: و ض ع B004: "الوضيعة الحطيطة وقد استوضع" (tahdhib); "الوضيعة الحطيطة من رأس المال" (mufradat); "وضع في تجارته يوضع خسر" (maqayis). An amount taken off the capital; a loss in trade. With عن it becomes the creditor's reduction of what is owed. That usage is from memory, e.g. the hadith "من أنظر معسرا أو وضع عنه".
- 94:4 رَفَعْنَا: ر ف ع B004: "رفعت فلانا إلى الحاكم أي قدمته إليه" (tahdhib); "رفعته للسلطان" (maqayis). The debtor brought before the authority.
- 94:1 صَدْرَكَ: ص د ر B005: "صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه" (tahdhib). An official bound to pay a sum he has guaranteed.
- 94:4 ذِكْرَكَ: ذ ك ر B008 [fixed expression]: "ذكر الحق الصك" (ayn;tahdhib). The written deed of a claim.
- 94:3 ظَهْرَكَ: ظ ه ر B023 [fixed expression]: "ما كان عن ظهر غنى عن فضل عيال" (tahdhib). Giving from what is left over once dependants are fed.
- Quran: 2:280: on debts after the ban on usury: "وَإِن كَانَ ذُو عُسْرَةٍ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌ لَّكُمْ". 2:282 (from memory): writing down a debt, two women witnesses "فتذكر إحداهما الأخرى". 65:7: the straitened man spends from what he was given, then "بَعْدَ عُسْرٍ يُسْرًا". 93:8: in the preceding surah, to the Prophet: "وَوَجَدَكَ عَآئِلًا فَأَغْنَىٰ".

### C9. Carrying, delivering, rearing: the birth scene
The dictionary builds a birth scene out of four of the surah's words. وضع is a woman laying down what she carried. عسر is a hard delivery. يسر is an easy one, and ذكر is a male child: "أعسرت وآنثت" / "أيسرت وأذكرت" (maqayis;tahdhib). That phrase, a blessing or a curse said over a pregnant woman, joins يسر and ذكر. The رب root names the ewe that has just given birth, "الربى: الشاة التي وضعت حديثا" (sihah), which joins رب and وضع. The same root names rearing and foster care. At the edges of the scene are union and seed (شرح, فرغ), the she-camel that did not conceive, and milk that is plentiful or held back.
- 94:2 وَضَعْنَا: و ض ع B002: "وضعت المرأة الحمل وضعا" (mufradat); "وضعت المرأة ولدها" (maqayis). Delivery: laying down what was carried.
- 94:2 وِزْرَكَ: و ز ر B002: "الوزر الحمل الثقيل من الإثم" (ayn). The heavy load (حِمل). The pregnancy word حَمل has the same consonants; the surah's own word is a load, not a pregnancy.
- 94:5–6 ٱلْعُسْرِ: ع س ر B006: "أعسرت المرأة إذا عسر عليها ولادها" (maqayis;sihah;tahdhib); "أعسرت وآنثت" (maqayis;tahdhib). The hard delivery.
- 94:5–6 يُسْرًا: ي س ر B001: "أيسرت المرأة وتيسرت في كذا أي سهلته وهيأته" (mufradat); with "أيسرت وأذكرت" (maqayis;tahdhib, under ع س ر B006). The easy delivery.
- 94:4 ذِكْرَكَ: ذ ك ر B001: "أذكرت ولدت ذكرا والمذكار تلد الذكور" (maqayis;ayn;sihah;tahdhib;mufradat). Bearing a male.
- 94:8 رَبِّكَ: ر ب ب B009: "الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة" (sihah). The ewe that has just given birth.
- 94:8 رَبِّكَ: ر ب ب B002: "رب فلان ولده؛ رباه" (sihah); "التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام" (mufradat). Rearing the child stage by stage to completion.
- 94:8 رَبِّكَ: ر ب ب B005: "الربيبة: الحاضنة" (sihah); "الراب والرابة بأحد الزوجين إذا تولى تربية الولد" (mufradat). The foster-carer.
- 94:5–6 يُسْرًا: ي س ر B006 [fixed expression]: "يسرت الغنم إذا كثر لبنها ونسلها" (maqayis;sihah). Plenty of milk and young.
- 94:4 رَفَعْنَا: ر ف ع B007 [fixed expression]: "ناقة رافع إذا رفعت اللبأ في ضرعها" (maqayis;sihah). First milk held back in the udder: the reverse.
- 94:5–6 ٱلْعُسْرِ: ع س ر B007: "العسير الناقة التي اعتاطت واعتاصت فلم تحمل عامها" (maqayis). The she-camel that did not conceive that year. The tahdhib records al-Layth's gloss and rejects it: "تفسير الليث للعسير أنها الناقة التي اعتاطت غير صحيح".
- 94:7 فَرَغْتَ: ف ر غ B005: "الفراغة ماء الرجل وهو النطفة" (sihah). The seed.
- 94:1 نَشْرَحْ: ش ر ح B004: "ويشرحون النساء شرحا والشرح افتضاض الأبكار" (tahdhib). Union.
- Quran: 3:35–37: the wife of Imran vows what is in her womb, then "فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ … وَلَيْسَ ٱلذَّكَرُ كَٱلْأُنثَىٰ", and her Lord accepts the child, makes her grow and places her in Zakariyya's care (وضع, ذكر, رب and fosterage in one scene). 65:4–7: "أَن يَضَعْنَ حَمْلَهُنَّ … يُسْرًا"; 65:6 "وَإِن تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُۥٓ أُخْرَىٰ"; 65:7 "بَعْدَ عُسْرٍ يُسْرًا" (delivery, nursing, hardship and ease together). 46:15: "حَمَلَتْهُ أُمُّهُۥ كُرْهًا وَوَضَعَتْهُ كُرْهًا", then the grown son: "رَبِّ أَوْزِعْنِىٓ". 19:23–26 (from memory): Maryam's labour at the palm trunk, then water and dates provided. 22:2 (from memory): every pregnant female sets down her load at the Hour. 26:18 (from memory): Pharaoh to Moses: "ألم نربك فينا وليدا".

### C10. The minister, the backer, the refuge
The وزير is named after the load: he "carries the weight off his master". So the root of 94:2's burden also names the one who takes a burden off another, and the mountain one shelters behind. The back of 94:3 gives the helper who sets his back against yours, and a man's back is his band of supporters. In 94:2 the speaker takes the load off. The Lord of 94:8 is the master who is turned to. The dictionary itself joins the minister, the load and the refuge: "وزير الخليفة الذي يعتمد على رأيه ويلتجئ إليه" (tahdhib).
- 94:2 وِزْرَكَ: و ز ر B004: "الوزير سمي به لأنه يحمل الثقل عن صاحبه" (maqayis); "الوزير الموازر لأنه يحمل عنه وزره" (sihah); "وزير الخليفة الذي يعتمد على رأيه ويلتجئ إليه" (tahdhib); "الوزير المتحمل ثقل أميره والموازرة المعاونة" (mufradat). The one who carries the load off another.
- 94:2 وِزْرَكَ: و ز ر B001: "الوزر الجبل يلجأ إليه" (ayn); "الوزر الملجأ" (maqayis;sihah); "كل ما التجأت إليه وتحصنت به" (tahdhib). The mountain refuge.
- 94:2 وِزْرَكَ: و ز ر B007: "الاتزار فهو من الوزر يقال اتزرت" (tahdhib). Girding on the waist-wrap. The tahdhib derives this from وزر, which links it to the أزر of 20:31.
- 94:3 ظَهْرَكَ: ظ ه ر B006: "الظهير المعين كأنه أسند ظهره إلى ظهرك" (maqayis); "استظهر به استعان به" (sihah). Back set against back: the helper.
- 94:3 ظَهْرَكَ: ظ ه ر B016: "الظهرة ظهر الرجل وأنصاره" (tahdhib); "الظهراء أعوان النبي" (tahdhib). A man's back as his supporters.
- 94:8 رَبِّكَ: ر ب ب B001: "يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح" (tahdhib). The master whose load the minister would carry; here He carries it off.
- Quran: 20:24–32: Moses, sent to Pharaoh, asks: "ٱشْرَحْ لِى صَدْرِى وَيَسِّرْ لِىٓ أَمْرِى … وَٱجْعَل لِّى وَزِيرًا مِّنْ أَهْلِى هَٰرُونَ أَخِى ٱشْدُدْ بِهِۦٓ أَزْرِى" (شرح صدر, يسر and وزير in one prayer). 25:35: "وَجَعَلْنَا مَعَهُۥٓ أَخَاهُ هَٰرُونَ وَزِيرًا". 28:34–35 (from memory): "سنشد عضدك بأخيك". 75:10–12: man on the Day: "أَيْنَ ٱلْمَفَرُّ كَلَّا لَا وَزَرَ إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ" (no refuge, and "إلى ربك", as in 94:8). 9:118: "وَظَنُّوٓا۟ أَن لَّا مَلْجَأَ مِنَ ٱللَّهِ إِلَّآ إِلَيْهِ". 66:4: "وَٱلْمَلَٰٓئِكَةُ بَعْدَ ذَٰلِكَ ظَهِيرٌ".

### C11. War's gear laid down
أوزار also means the gear of war, and "وضع" + "أوزار" is the Quran's phrase for war ending. That lets 94:2 be heard as armour and weapons laid down. The other words fill in a battlefield: overcoming, getting on top, two mail-coats worn one over the other, setting war up against someone (ناصب), a wide wound, and blood left unavenged. The surah ends that scene with "إذا فرغت". An early gloss (from memory, attributed to al-Hasan and Zayd b. Aslam) reads 94:7 as: when you are done with fighting your enemy, stand in worship of your Lord.
- 94:2 وِزْرَكَ: و ز ر B003: "أوزار الحرب آلتها" (ayn;mufradat); "الأوزار ههانا السلاح وآلة الحرب" (tahdhib); "الوزر السلاح والجمع أوزار" (maqayis). Weapons and war gear.
- 94:2 وَضَعْنَا: و ض ع B001: "وضعت الشيء أضعه وضعا وهو ضد رفعته" (tahdhib). Laying them down.
- 94:2 وِزْرَكَ: و ز ر B006: "وزرته غلبته" (maqayis); "وزرت فلانا غلبته" (sihah). Overcoming a man.
- 94:3 ظَهْرَكَ: ظ ه ر B007 [fixed expression]: "الظهور الغلبة" (maqayis); "ظهر عليه غلبه وليظهره على الدين كله" (mufradat). Getting the upper hand.
- 94:3 ظَهْرَكَ: ظ ه ر B020 [fixed expression]: "ظاهر فلان بين ثوبين وبين درعين إذا طابق بينهما" (tahdhib). Two mail-coats worn one over the other.
- 94:7 فَٱنصَبْ: ن ص ب B008: "ناصبته الحرب مناصبة" (sihah); "ناصبت فلانا الشر والحرب والعداوة" (ayn;tahdhib). Setting war up against someone: the opposite of the upright stance of worship.
- 94:7 فَرَغْتَ: ف ر غ B003 [fixed expression]: "فرس فريغ واسع العدو وضربة فريغة واسعة ينصب منها الدم" (mufradat). The wide blow that blood pours from.
- 94:7 فَرَغْتَ: ف ر غ B004 [fixed expression]: "ذهب دمه فرغا أي باطلا لم يطلب به" (maqayis). Blood left unclaimed.
- Quran: 47:4: orders for battle with the deniers: "حَتَّىٰ تَضَعَ ٱلْحَرْبُ أَوْزَارَهَا" (the phrase for war's end). 9:33 (from memory; the mufradat cites it under ظ ه ر B007): "ليظهره على الدين كله". 2:250: in the field against Goliath: "أَفْرِغْ عَلَيْنَا صَبْرًا … وَٱنصُرْنَا". 8:66: "ٱلْـَٰٔنَ خَفَّفَ ٱللَّهُ عَنكُمْ" (load lightened in battle).

### C12. Sound: the creak under the load and the raised voice
The surah's words carry sounds. The back creaks under its weight (نقيض), and so do saddles and joints. A rider clicks his tongue to urge a young camel (إنقاض). Riders sing the نصب chant with raised voices. ذكر itself is "الصوت", fame as a sound that carries. رفع is raising the voice. So 94:3–4 runs from the groan of the loaded back to a raised name that is heard. In the call to prayer (the standard gloss of 94:4, from memory) that name is literally called aloud.
- 94:3 أَنقَضَ: ن ق ض B005: "النقيض صوت الأصابع والمفاصل والأضلاع" (ayn); "النقيض صوت المحامل والرحال" (sihah). The creak of joints, ribs and saddles.
- 94:3 أَنقَضَ: ن ق ض B006: "الإنقاض زجر القعود" (maqayis); "أنقضت العقاب وكذلك الدجاجة" (sihah). The urging click; small animal cries.
- 94:4 ذِكْرَكَ: ذ ك ر B007: "الذكر الشرف والصوت" (ayn;tahdhib); "الذكر الصيت والثناء" (sihah). Renown as sound.
- 94:4 رَفَعْنَا: ر ف ع B010 [fixed expression]: "في صوته رفاعة ورفاعة" (sihah;tahdhib); "إذا كان رفيع الصوت" (tahdhib). The raised voice.
- 94:7 فَٱنصَبْ: ن ص ب B009: "النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت" (maqayis); "غناء لهم يشبه الحداء إلا أنه أرق منه" (sihah). A song sung with a raised voice: the travellers' chant.
- 94:4 ذِكْرَكَ: ذ ك ر B005: "الذكر الصلاة والدعاء والثناء" (ayn;tahdhib). Remembrance spoken in prayer and praise.
- Quran: 49:2: to the believers: "لَا تَرْفَعُوٓا۟ أَصْوَٰتَكُمْ فَوْقَ صَوْتِ ٱلنَّبِىِّ" (the Prophet's voice set above theirs). 7:205 (from memory): "واذكر ربك في نفسك تضرعا وخيفة ودون الجهر من القول".

### C13. Behind the back, kept in mind
ظهر is also the place things are put to be forgotten: "تجعله بظهر أي تنساه". ذكر is the opposite, "خلاف نسيته". So 94:3–4 runs from the back, where things are put away, to the name kept in mind. The back root also turns the other way: "ظهر القلب" is knowing by heart, and a reciter "carries the Quran on the back of his tongue". The phrase joins ظهر to carrying, and so to C1's load. شرح adds keeping and guarding.
- 94:3 ظَهْرَكَ: ظ ه ر B012: "الظهري كل شيء تجعله بظهر أي تنساه" (maqayis); "لا تجعل حاجتي بظهر أي لا تنسها" (sihah); "ظهرت بكذا أي خلفته ولم ألتفت إليه" (mufradat). Put behind and forgotten.
- 94:4 ذِكْرَكَ: ذ ك ر B003: "ذكرت الشيء خلاف نسيته" (maqayis;sihah); "الذكر الحفظ للشيء وهو مني على ذكر" (ayn;tahdhib). Kept in mind.
- 94:3 ظَهْرَكَ: ظ ه ر B019: "ظهر القلب حفظ من غير كتاب" (ayn;tahdhib); "حمل القرآن على ظهر لسانه" (tahdhib); "استظهر الشيء أي حفظه وقرأه ظاهرا" (sihah). Known by heart; the Quran carried on the tongue's back.
- 94:4 ذِكْرَكَ: ذ ك ر B009: "التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر" (mufradat). The reminder.
- 94:4 ذِكْرَكَ: ذ ك ر B006: "الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر" (ayn;tahdhib). The Reminder as scripture.
- 94:1 نَشْرَحْ: ش ر ح B006: "الشارح الحافظ؛ الشرح الحفظ" (tahdhib). Keeping and guarding.
- Quran: 3:187: People of the Book, bound by covenant "لَتُبَيِّنُنَّهُۥ لِلنَّاسِ … فَنَبَذُوهُ وَرَآءَ ظُهُورِهِمْ" (making plain, set against the back). 11:92: Shu'ayb to his people: "وَٱتَّخَذْتُمُوهُ وَرَآءَكُمْ ظِهْرِيًّا". 15:9 (from memory): "إنا نحن نزلنا الذكر وإنا له لحافظون". 87:6 (from memory): "سنقرئك فلا تنسى". 2:152 (from memory): "فاذكروني أذكركم".

### C14. Made plain, made to appear, made known
شرح opens what is hidden. ظهر is a hidden thing coming into view. رفع is making a report public. ذكر is speaking a thing aloud, and it is also the Book. The dictionary joins شرح and ظهر in its definition: "بسطه وإظهار ما يخفى من معانيه" (mufradat). Across 94:1, 94:3 and 94:4 these words move from a thing laid open, to a thing in view, to a name spread abroad.
- 94:1 نَشْرَحْ: ش ر ح B001: "الشرح البيان اشرح أي بين" (ayn); "شرحت الغامض إذا فسرته" (sihah); "شرح المشكل من الكلام بسطه وإظهار ما يخفى من معانيه" (mufradat). Laying open what is obscure.
- 94:3 ظَهْرَكَ: ظ ه ر B001: "الظهور بدو الشيء الخفي" (ayn;tahdhib); "ظهر الشيء إذا انكشف وبرز" (maqayis). A hidden thing coming into view.
- 94:3 ظَهْرَكَ: ظ ه ر B008 [fixed expression]: "فلا يظهر على غيبه أحدا أي لا يطلع عليه" (mufradat). Being let in on what was hidden.
- 94:4 رَفَعْنَا: ر ف ع B005: "الرفع إذاعة الشيء وإظهاره" (maqayis); "أذاع خبر ما احتجبه" (mufradat). Making public what was screened.
- 94:4 ذِكْرَكَ: ذ ك ر B004 [fixed expression]: "الذكر جري الشيء على لسانك" (ayn;tahdhib); "ذكرته بلساني وبقلبي" (sihah). A name running on the tongue.
- Quran: 16:44: "وَأَنزَلْنَآ إِلَيْكَ ٱلذِّكْرَ لِتُبَيِّنَ لِلنَّاسِ مَا نُزِّلَ إِلَيْهِمْ" (the Reminder sent to the Prophet to be made plain). 3:187: the covenant to make it plain, broken. 72:26 (from memory; the mufradat cites it): "فلا يظهر على غيبه أحدا".

### C15. Finished, standing to toil, turning in desire to the Lord
94:7–8 is a work cycle. A task is finished and the worker is empty of it (فرغ). Then he stands upright and works until tired (نصب). Then his wanting is turned to the Lord (إلى ربك فارغب). The dictionary already uses فرغ with إلى in "فرغت إلى أمر كذا أي عمدت له" (maqayis): being done with one thing means turning on purpose to another. رغب can face either way: "رغب فيه وإليه … ورغب عنه". The surah sends it "to your Lord". It is the opposite of the spreading-out toward the world that the dictionary records under شرح: "يشرحون إلى الدنيا … ويرغبون في اقتنائها رغبة واسعة". A worshipper's phrase links the turn to the gift: "إليك الرغباء ومنك النعماء" (ayn).
- 94:7 فَرَغْتَ: ف ر غ B001: "الفراغ خلاف الشغل" (maqayis;mufradat); "فرغت من الشغل" (sihah). Finished with the work.
- 94:7 فَرَغْتَ: ف ر غ B006 [fixed expression]: "فرغت إلى أمر كذا أي عمدت له" (maqayis); "سنفرغ أي نعمد" (maqayis); "تفرغت لكذا" (sihah). Turning on purpose to the next thing.
- 94:7 فَٱنصَبْ: ن ص ب B001: "نصبت الشئ إذا أقمته" (sihah); "النصب رفعك شيئا تنصبه قائما منتصبا" (ayn;tahdhib). Standing upright.
- 94:7 فَٱنصَبْ: ن ص ب B004: "النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي" (maqayis); "النصب الإعياء والتعب" (ayn); "أنصبني كذا أي أتعبني وأزعجني" (mufradat). Standing until worn out.
- 94:8 فَٱرْغَب: ر غ ب B001: "رغب فيه وإليه يقتضي الحرص عليه ورغب عنه اقتضى صرف الرغبة عنه والزهد فيه" (mufradat); "إليك الرغباء ومنك النعماء" (ayn); "رغبت في الشيء إذا ملت إليه ورغبت عنه إذا صددت عنه" (jamhara). Wanting that leans toward, or turns away.
- 94:8 فَٱرْغَب: ر غ ب B004: "الرغيبة العطاء الكثير والجمع الرغائب" (sihah). The large gift the wanting reaches for.
- 94:8 رَبِّكَ: ر ب ب B001: "الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه" (jamhara). The one turned to.
- 94:8 رَبِّكَ: ر ب ب B016: "الربى: النعمة والإحسان" (tahdhib). Favour and kindness.
- 94:1 نَشْرَحْ: ش ر ح B005 [fixed expression]: "أكان الأنبياء يشرحون إلى الدنيا يريد كانوا ينبسطون إليها ويرغبون في اقتنائها رغبة واسعة" (tahdhib). The opposite turn: spreading toward the world with wide wanting.
- Quran: 55:31: God to men and jinn: "سَنَفْرُغُ لَكُمْ أَيُّهَ ٱلثَّقَلَانِ" (the maqayis cites it as "نعمد"; the addressees are "the two weighty ones"). 68:32: owners of the ruined garden, repenting (scene opens 68:17): "إِنَّآ إِلَىٰ رَبِّنَا رَٰغِبُونَ". 9:59: "إِنَّآ إِلَى ٱللَّهِ رَٰغِبُونَ". 21:90: Zakariyya's house: "وَيَدْعُونَنَا رَغَبًا وَرَهَبًا". 2:130 (from memory): "ومن يرغب عن ملة إبراهيم إلا من سفه نفسه" (the turning away). 4:103: "فَإِذَا قَضَيْتُمُ ٱلصَّلَوٰةَ فَٱذْكُرُوا۟ ٱللَّهَ قِيَٰمًا وَقُعُودًا". 2:200: "فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ". 62:10: the reverse order: prayer finished, then "فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ". 73:2–8 (from memory for 73:2, 7, 8): "قم الليل … إن لك في النهار سبحا طويلا واذكر اسم ربك وتبتل إليه تبتيلا". 84:6: "إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ". 53:42: "وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ". 74:7: "وَلِرَبِّكَ فَٱصْبِرْ" (same shape as 94:8). 88:2–3: faces on the Day "عَامِلَةٌ نَّاصِبَةٌ" (toil that gains nothing).

### C16. The slaughtered camel divided by arrows at the standing stones
These words also make the old Arab ميسر scene. A slaughtered camel is cut up (تشريح). Its parts are shared out by arrows kept in a bag (ربابة), and each man gets his portion (نصيب, صدر). Offerings were made at standing stones (أنصاب) whose surfaces took the victims' blood. The dictionary joins two of the surah's roots in "الربابة شبيهة بالكنانة تجمع فيها سهام الميسر" (sihah). The Quran puts الميسر and الأنصاب in one ayah. Against this scene, the surah's ease is given by the Lord, not drawn by lot, and the one who stands (انصب) turns to his Lord, not to the stones.
- 94:5–6 يُسْرًا: ي س ر B007: "الميسر: قمار العرب بالأزلام" (sihah); "يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها" (sihah). Arrow-lots over a slaughtered camel; the parts shared out.
- 94:1 نَشْرَحْ: ش ر ح B002: "الشرح والتشريح قطع اللحم على العظام والقطعة شرحة" (ayn); "الشرح والتشريح قطع اللحم عن العضو" (tahdhib). Flesh cut from the bones, piece by piece.
- 94:8 رَبِّكَ: ر ب ب B010: "الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام" (sihah). The bag that holds the ميسر arrows.
- 94:7 فَٱنصَبْ: ن ص ب B002: "حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب" (ayn); "حجارة تعبدها وتذبح عليها" (mufradat). The standing stone of sacrifice.
- 94:7 فَٱنصَبْ: ن ص ب B005: "النصيب الحظ من الشيء" (maqayis;sihah); "النصيب الحظ المنصوب أي المعين" (mufradat). The fixed portion.
- 94:1 صَدْرَكَ: ص د ر B006: "الصدر الطائفة من الشيء" (sihah). A portion of a thing.
- Quran: 5:90: "إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌ" (ميسر and أنصاب together). 5:3: forbidden "مَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ". 2:219 (from memory): "يسألونك عن الخمر والميسر".

## Interactions

- C1 × C2: they share ظَهْرَكَ and أَنقَضَ. "النقيض صوت المحامل والرحال" (sihah) puts the creak of 94:3 in the camel's saddle, and "الظهر الركاب تحمل الأثقال في السفر" makes the loaded back a mount. 16:7 stages both: loads carried by beasts "إلا بشق الأنفس".
- C1 × C3: 94:2 and 94:4 are paired by "وضعت الشيء أضعه وضعا وهو ضد رفعته" (tahdhib). What is lowered is the weight (C1); what is raised is the name (C3).
- C1 × C10: "الوزير … لأنه يحمل الثقل عن صاحبه" (maqayis) uses عن like "وضعنا عنك". The root of the burden also names the one who takes it off. 20:24–32 stages both, with شرح صدر and يسر.
- C1 × C5: بسط defines both words: "الوزر حمل الرجل إذا بسط ثوبه فجعل فيه المتاع" (maqayis) and "شرح الصدر أي بسطه" (mufradat). The cloth spread to hold a load, and the chest spread open.
- C1 × C13: "حمل القرآن على ظهر لسانه" (tahdhib) puts a carried thing on a "back" that is memory. 6:31 (burdens on backs) and 3:187 (the Book thrown behind backs) are the two ways the back carries.
- C1 × C12: نقيض is both the weight on the back and the sound it makes. 94:3 → 94:4 runs from the creak to the raised voice.
- C2 × C7: "العسير الناقة التي لم ترض" against "يسر أي لين الانقياد سريع المتابعة … والفرس". Hardship and ease are the unbroken and the compliant mount. "الدابة تضع في سيرها وضعا وهو سير سهل" ties وضع's gait to ease.
- C2 × C3 × C4: "مرفوع الناقة في سيرها خلاف الموضوع" (maqayis) and "نصب القوم السير نصبا إذا رفعوه" (jamhara). The وضع/رفع/نصب axis of rank and building is also the axis of gait. 88:17–19 stages camel, رفع and نصب.
- C2 × C15: 43:12–14 stages the mount's back, remembering the Lord's favour, and "إلى ربنا لمنقلبون". 18:62 gives نصب as road-weariness. The camels' halt (مرب الإبل) under رب matches the end-point "إلى ربك".
- C2 × C6: the watering-place: noon watering "الظاهرة أن ترد كل يوم ظهرا", leaving the water "صدر عن الماء", the stone basin "النصيب الحوض ينصب من الحجارة", the wide basin "حوض رغيب", the poured bucket "أفرغت الدلو".
- C3 × C12 × C14: ذكر is both "العلاء والشرف" and "الصوت". رفع is "في الذكر إذا نوهته", "إذاعة الشيء وإظهاره" and "رفيع الصوت". 24:36 stages رفع with ذكر of the name.
- C4 × C16: نصب gives both the upright building or spear and the standing stone of sacrifice. 88:19 (mountains "نصبت") against 5:90 (أنصاب).
- C4 × C7: "العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع" (tahdhib) puts عسر and نصب in one phrase: an upright post knocked out.
- C5 × C6: "الشرح السعة" and "أصل الرغبة السعة في الشيء" (mufradat). The opened chest of 94:1 and the wide-bellied vessel of 94:8 both come from breadth.
- C5 × C15: "يشرحون إلى الدنيا … ويرغبون في اقتنائها رغبة واسعة" (tahdhib) puts شرح, إلى and رغب in one phrase. 94:1 opens the chest, and 94:8 turns the wanting "إلى ربك" instead of to the world.
- C5 × C10 × C7: 20:25–32 stages the opened chest, the eased affair and the وزير in one prayer of Moses. 26:13 gives its reverse ("يضيق صدري").
- C6 × C15: فرغ is both emptying (C6) and "فرغت إلى أمر كذا أي عمدت له" (C15). 94:7's emptiness is the empty vessel and the turn to a new task. 55:31 "سنفرغ لكم أيه الثقلان" puts فرغ against the weighty ones (C1).
- C7 × C8: "أعسر الرجل إذا صار من ميسرة إلى عسرة" and "ولم تنظره إلى ميسرته" (maqayis). 2:280 and 65:7 stage the debtor's hardship and ease.
- C7 × C9: "أعسرت وآنثت / أيسرت وأذكرت" (maqayis;tahdhib). Hardship and ease in labour, with ذكر as the male child. 65:4–7 stages delivery (يضعن حملهن), nursing in hardship (تعاسرتم) and "بعد عسر يسرا".
- C8 × C1: the remission (وضيعة, "وضع عنه") and the load set down (وضع عن) are one verb with عن.
- C9 × C1: "الوزر الحمل الثقيل" and "وضعت المرأة الحمل". One shape, a load carried and laid down, used for burden and for birth. 46:15 "حملته … ووضعته".
- C9 × C15: رب as rearing (رب ولده) and as the Lord turned to. 3:35–37 stages وضع, ذكر and "ربها" who receives the child and makes her grow.
- C10 × C15: 75:11–12 "لا وزر إلى ربك يومئذ المستقر" and 9:118 "لا ملجأ من الله إلا إليه". The refuge-sense of وزر meets "إلى ربك".
- C11 × C1: 47:4 "تضع الحرب أوزارها" and 94:2 "وضعنا عنك وزرك": the same verb with the same noun.
- C11 × C15: "ناصبته الحرب" against "فانصب" as standing to worship. The gloss "إذا فرغت من الجهاد فانصب في العبادة" (from memory) links the end of war to the turn of 94:7–8.
- C13 × C14: 3:187 stages making plain (لتبيننه, the sense of شرح) and throwing behind the back (وراء ظهورهم).
- C16 × C7 × C15: "الربابة … تجمع فيها سهام الميسر" (sihah) puts رب and يسر in one phrase. The ease of 94:5–6 and the Lord of 94:8 stand against the ميسر and the أنصاب of 5:90.

## Ayat

**94:1 أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ**
- C1: the chest, the front of the loaded torso. Scene: a chest and back under a bundle of weight; the back creaks; the speaker takes the load down and off; a fetter's weight is lifted.
- C2: صدر is leaving the water. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C3: صدر is the head of the assembly and winning by a chest's length. Scene: a weight lowered and a name raised high, with honour and no clinging shame.
- C4: صدر is the top of the spear-shaft. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C5: شرح صدر, the chest spread and widened like flesh laid flat, its hidden sense opened. Scene: the chest laid open and widened to receive good, against the straitened chest, and against the bundle-cloth spread to carry a load.
- C6: the widened capacity. Scene: a chest widened, a heart and a bucket emptied and poured, a wide-bellied basin of stones filled with plenty of water and with the wanted gift.
- C8: صادره, an agent bound to pay. Scene: a man fallen from plenty into want, pressed by his creditor and brought to the ruler; part is taken off; he waits for means; giving comes from surplus.
- C9: شرح as union. Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C13: شرح as guarding. Scene: what is thrown behind the back is forgotten; the name is kept in mind, known by heart, carried on the tongue's back.
- C14: شرح as laying open what is obscure. Scene: a hidden matter laid open, brought into view, and made public as a spoken name.
- C15: شرح إلى الدنيا, the wrong spreading-out. Scene: work finished, the worker stands and toils, and his wanting turns to his Lord, not out toward the world.
- C16: تشريح, flesh cut from bones; صدر, a portion. Scene: a camel slaughtered and cut up, shared by arrows from the bag into portions, beside standing stones of sacrifice.

**94:2 وَوَضَعْنَا عَنكَ وِزْرَكَ**
- C1: lowering and taking off; وزر as bundle, weight and guilt. Scene: a chest and back under a bundle of weight; the back creaks; the speaker takes the load down and off; a fetter's weight is lifted.
- C2: the camel's neck lowered to mount; the easy وضع gait; camels halted at pasture. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C3: وضيع, the low station, here applied to the weight. Scene: a weight lowered and a name raised high, with honour and no clinging shame.
- C4: placing on a site. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C5: وزر as cloth spread to hold a load. Scene: the chest laid open and widened to receive good, against the straitened chest, and against the bundle-cloth spread to carry a load.
- C8: وضيعة, an amount taken off capital; "وضع عنه" as remission. Scene: a man fallen from plenty into want, pressed by his creditor and brought to the ruler; part is taken off; he waits for means; giving comes from surplus.
- C9: laying down what was carried. Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C10: وزير, the one who carries the load off his master; وزر, the mountain refuge; girding. Scene: a minister carries his master's load, a helper sets his back against yours, a mountain gives shelter; here the speaker carries the load off, and the Lord is the refuge turned to.
- C11: أوزار, the gear of war, laid down; وزر, overcoming. Scene: war's weapons laid down after victory; then, the fight done, standing to another labour.

**94:3 ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ**
- C1: the weight that made the back creak; the back that bore it. Scene: a chest and back under a bundle of weight; the back creaks; the speaker takes the load down and off; a fetter's weight is lifted.
- C2: the back as mount; the camel worn by journeys; the creaking saddle; the click that urges young camels; noon watering; the land road. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C3: shame that does not cling; climbing on top. Scene: a weight lowered and a name raised high, with honour and no clinging shame.
- C4: نقض, undoing rope and building. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C8: giving "عن ظهر غنى". Scene: a man fallen from plenty into want, pressed by his creditor and brought to the ruler; part is taken off; he waits for means; giving comes from surplus.
- C10: ظهير, back set against back; a man's back as his supporters. Scene: a minister carries his master's load, a helper sets his back against yours, a mountain gives shelter; here the speaker carries the load off, and the Lord is the refuge turned to.
- C11: getting the upper hand; two mail-coats worn one over the other. Scene: war's weapons laid down after victory; then, the fight done, standing to another labour.
- C12: نقيض, the creak of joints, ribs and saddles. Scene: the groan of the loaded back and saddle, the click and chant of riders, rising to a name called aloud.
- C13: the back where things are forgotten; ظهر القلب, knowing by heart. Scene: what is thrown behind the back is forgotten; the name is kept in mind, known by heart, carried on the tongue's back.
- C14: ظهور, a hidden thing coming into view. Scene: a hidden matter laid open, brought into view, and made public as a spoken name.

**94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ**
- C1: the cord that lifts a fetter. Scene: a chest and back under a bundle of weight; the back creaks; the speaker takes the load down and off; a fetter's weight is lifted.
- C2: the higher رفع gait; travelling up-country. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C3: رفع ذكر, "في الذكر إذا نوهته"; ذكر as height and honour. Scene: a weight lowered and a name raised high, with honour and no clinging shame.
- C4: raising placed bodies off their base; building tall. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C8: bringing a man before the ruler; ذكر الحق, the deed. Scene: a man fallen from plenty into want, pressed by his creditor and brought to the ruler; part is taken off; he waits for means; giving comes from surplus.
- C9: أذكرت, bearing a male; milk held back (رافع). Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C12: ذكر as الصوت; the raised voice. Scene: the groan of the loaded back and saddle, the click and chant of riders, rising to a name called aloud.
- C13: ذكر, keeping in mind, the reminder, the Book. Scene: what is thrown behind the back is forgotten; the name is kept in mind, known by heart, carried on the tongue's back.
- C14: رفع, making public; ذكر, a name on the tongue. Scene: a hidden matter laid open, brought into view, and made public as a spoken name.

**94:5 فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا**
- C2: the unbroken camel against the light, compliant mount; the running camel's lifted tail. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C4: عسر, the upright post knocked out. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C7: hardship against ease; twisting resistance against smooth readiness; the two hands of "أعسر يسر"; the hard day. Scene: hardship and ease held together with مع, like a man's two working hands, the hard day carrying its ease inside it.
- C8: want, and the means that return. Scene: a man fallen from plenty into want, pressed by his creditor and brought to the ruler; part is taken off; he waits for means; giving comes from surplus.
- C9: hard and easy delivery; plenty of milk and young; the camel that did not conceive. Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C16: ميسر, the camel divided by arrow-lots. Scene: a camel slaughtered and cut up, shared by arrows from the bag into portions, beside standing stones of sacrifice.

**94:6 إِنَّ مَعَ ٱلْعُسْرِ يُسْرًا**
- C7: the repetition. The definite العسر stays one hardship and the indefinite يسرا is counted again ("لن يغلب عسر يسرين", from memory). Scene: hardship and ease held together with مع, like a man's two working hands, the hard day carrying its ease inside it.
- C2, C4, C8, C9, C16: the same members as 94:5, heard a second time. Scenes as in 94:5.

**94:7 فَإِذَا فَرَغْتَ فَٱنصَبْ**
- C2: فريغ, wide-striding; نصب, daylong march, road-weariness, the riders' chant. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C4: نصب, setting upright spear, building, stone. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C6: فرغ, a heart or bucket emptied and poured; the basin of upright stones. Scene: a chest widened, a heart and a bucket emptied and poured, a wide-bellied basin of stones filled with plenty of water and with the wanted gift.
- C9: فراغة, the seed. Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C11: done with fighting; ناصبه الحرب; the wide wound; blood left unclaimed. Scene: war's weapons laid down after victory; then, the fight done, standing to another labour.
- C12: the نصب chant sung with a raised voice. Scene: the groan of the loaded back and saddle, the click and chant of riders, rising to a name called aloud.
- C15: finished with the task, turning on purpose to the next, standing upright until tired. Scene: work finished, the worker stands and toils, and his wanting turns to his Lord, not out toward the world.
- C16: أنصاب, standing stones of sacrifice; نصيب, the portion. Scene: a camel slaughtered and cut up, shared by arrows from the bag into portions, beside standing stones of sacrifice.

**94:8 وَإِلَىٰ رَبِّكَ فَٱرْغَب**
- C2: مرب الإبل, the halt; رغيب الشحوة, the wide stride. Scene: a camel kneels for its rider and carries loads; it goes at a low or high pace, untrained or compliant; it grows thin on the road while the saddle creaks and the riders chant; it waters at noon, leaves the water, halts at pasture.
- C4: الربى, the firm knot. Scene: things placed, raised, set upright like spear and building, and rope or building undone.
- C5: رغبة as breadth. Scene: the chest laid open and widened to receive good, against the straitened chest, and against the bundle-cloth spread to carry a load.
- C6: رغيب, the wide-bellied basin, skin or man; the craving; the large gift; ربب, plenty of water. Scene: a chest widened, a heart and a bucket emptied and poured, a wide-bellied basin of stones filled with plenty of water and with the wanted gift.
- C9: الربى, the newly delivered ewe; rearing; the foster-carer. Scene: union and seed; a load carried; delivery hard or easy, a male child; the newly delivered mother; rearing and fostering; milk plentiful or held back.
- C10: the master and Lord, turned to as refuge. Scene: a minister carries his master's load, a helper sets his back against yours, a mountain gives shelter; here the speaker carries the load off, and the Lord is the refuge turned to.
- C15: رغب إلى, wanting turned toward; "إليك الرغباء ومنك النعماء"; the Lord as end-point and giver. Scene: work finished, the worker stands and toils, and his wanting turns to his Lord, not out toward the world.
- C16: ربابة, the bag of ميسر arrows. Scene: a camel slaughtered and cut up, shared by arrows from the bag into portions, beside standing stones of sacrifice.

