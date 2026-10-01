Surah: 100. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (100:1 to 100:11), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s100/surah.r2/text.md =====
# Surah 100

- 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/out/s100/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. The running horse: gallop, breath, stride, lean body, the run that proves it
The surah opens on running animals. Their breath is heard (ضبحا), their forelegs reach out, they gather their whole speed (جمعا). The horse's root senses then come back in the ayat about man. شهيد names "the run that testifies to the horse's precedence". شديد is itself a word for the gallop. صدور carries "the horse that comes in first by its chest". So the horse runs through the whole surah. It spends its breath and body for the rider who owns it, while man, set beside it, is كنود to his Lord.
- 100:1 ٱلْعَٰدِيَٰتِ — ع د و B002 — "العَدْو هو الحضر"; "يقال من عدو الفرس عدوان أي جيد العدو وكثيره" — the gallop, and the horse that runs well and much.
- 100:1 ضَبْحًا — ض ب ح B001 — "صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة" — the breath-sound of horses while they run. The dictionary phrase itself joins ضبح with عدو.
- 100:1 ضَبْحًا — ض ب ح B002 [fixed expression] — "ضبح الفرس وضبع إذا حرك ضبعيه في مشيه"; "هو عدو فوق التقريب وأصله ضبع" — the forelegs thrown forward, a pace faster than التقريب.
- 100:2 قَدْحًا — ق د ح B008 [fixed expression] — "قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح" — the horse trained down until it is as lean as an arrow shaft: the body built for the run.
- 100:5 جَمْعًا — ج م ع B010 [fixed expression] — "استجمع الفرس جريا" — the horse gathers all its running into one effort.
- 100:6 ٱلْإِنسَٰنَ — ء ن س B004 — "إنسي الدابة للجانب الذي يلي الراكب" — the side of the mount next to its rider. This places the rider on the animal.
- 100:7 لَشَهِيدٌ — ش ه د B008 — "الشاهد من جريه ما يشهد له على سبقه وجودته" — the part of the horse's run that bears witness to its lead and its quality.
- 100:8 لَشَدِيدٌ — ش د د B003 — "الشد العدو والفعل اشتد"; "الشد الحضر والفعل اشتد" — شدّ is itself the gallop. The phrase joins شد with عدو.
- 100:10 ٱلصُّدُورِ — ص د ر B002 — "صدر الفرس إذا جاء قد سبق بصدره" — the horse that wins by its chest.
- Outside: 38:31–33. Narrator: Solomon's swift horses (الصافنات الجياد) are paraded at evening, and he says إني أحببت حب الخير عن ذكر ربي حتى توارت بالحجاب. Horses, حب الخير and ربي appear together. 3:14: God lists what is made attractive to people: حب الشهوات … والقناطير المقنطرة من الذهب والفضة والخيل المسومة. 8:60: God commands ومن رباط الخيل.

### 2. The dawn raid on a gathered host
This is the event the horses carry out. Raiding horses come at first light. Dust goes up, the people attacked cry out, and the riders cut into the middle of an assembled crowd. شديد comes back as "charging the enemy". Note: the dictionary file gives no raid sense under غ ي ر, the root assigned to ٱلْمُغِيرَٰتِ. From memory, the classical lexicons file أغار under غ و ر. Here the raid is attested through ع د و and ص ب ح.
- 100:1 ٱلْعَٰدِيَٰتِ — ع د و B001 — "العادية الخيل المغيرة (ayn;sihah)" — the dictionary defines the word of 100:1 by the word of 100:3. Also "العدوان الظلم الصراح": the attack as open wrong.
- 100:1 ٱلْعَٰدِيَٰتِ — ع د و B003 — "العَدُوّ ضد الولي والجمع الأعداء" — the enemy who is the target.
- 100:3 فَٱلْمُغِيرَٰتِ — the raiding horses, as the text itself says (see note above).
- 100:3 صُبْحًا — ص ب ح B004 — "يوم الصباح يوم الغارة (maqayis;sihah)"; "في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا" — dawn is the raid's own name. The phrase joins صبح, the raid and horses, and adds the cry for help of those attacked.
- 100:3 صُبْحًا — ص ب ح B002 — "صبحته إذا أتيته صباحا" — coming on someone at morning.
- 100:4 فَأَثَرْنَ — ث و ر B001 — "ثار الغبار يثور ثورا وثورانا أي سطع" — dust rising and spreading.
- 100:4 فَأَثَرْنَ — ث و ر B003 — "ثار به الناس أي وثبوا عليه" — leaping on someone in attack.
- 100:4 نَقْعًا — ن ق ع B004 — "النقع الغبار المرتفع" — the raised dust.
- 100:4 نَقْعًا — ن ق ع B005 — "النقع رفع الصوت"; "نقع بصوته وأنقع صوته إذا تابعه" — the raised, sustained cry, the يا صباحاه of the raided camp.
- 100:4 نَقْعًا — ن ق ع B003 — "النقيعة ما نحر من النهب قبل القسم" — the beast slaughtered from the plunder before it is divided: what comes after the raid.
- 100:5 فَوَسَطْنَ — و س ط B003 — "وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم (ayn)" — the dictionary phrase joins وسط with a جماعة: getting into the middle of a crowd.
- 100:5 جَمْعًا — ج م ع B002 — "الجمع اسم لجماعة الناس"; "الجماع ما تجمع من أشابة الناس وأخلاطهم" — the assembled host, a mixed crowd.
- 100:8 لَشَدِيدٌ — ش د د B003 — "شد على العدو إذا حمل عليه (jamhara;sihah)" — the charge against the enemy. The phrase joins شد with عدو.
- Outside: 37:177. God, answering those who want His punishment hurried (37:176): فإذا نزل بساحتهم فساء صباح المنذرين. The punishment comes like a dawn raid. 11:81: the angels tell Lot إن موعدهم الصبح أليس الصبح بقريب. 15:83: فأخذتهم الصيحة مصبحين. 54:38: ولقد صبحهم بكرة عذاب مستقر. 17:64: God tells Iblis وأجلب عليهم بخيلك ورجلك.

### 3. Striking fire: flint, spark, scorch, ash, light
The hooves strike stone and fire comes out. The fire-making words of 100:2 belong to the same scene as three other words. ضبح (100:1) is the scorching of the striker and the stones. حبّ (100:8) is the spark that horses strike and that is of no use. صبح (100:3) is the lamp and the light of day. Fire then turns toward man. إنسان's root is the word for seeing a fire from far off. "Man strikes the matter" when he thinks it through. And one strikes "the flint of error".
- 100:2 فَٱلْمُورِيَٰتِ — و ر ي B002 — "ورى الزند خرجت ناره"; "أوريت النار إذا كانت خامدة فأججتها" — fire coming out of the firestick, and a smouldering fire stirred up.
- 100:2 قَدْحًا — ق د ح B001 — "المقدحة ما تقدح به النار والقداحة والقداح الحجر الذي يوري النار (sihah)"; "المقدح الحديدة التي يقدح بها والقداح الحجر الذي تورى منه النار (ayn)" — the dictionary joins قدح and ورى in one phrase: the iron striker and the stone that gives fire.
- 100:1 ضَبْحًا — ض ب ح B003 — "حجارة القداحة مضبوحة"; "الضبح إحراق أعالي العود بالنار" — the dictionary joins ضبح with قدح: flints are "scorched", and the tip of the firestick is burnt.
- 100:1 ضَبْحًا — ض ب ح B004 — "ضبحته الشمس وضبته إذا غيرت لونه وكذلك النار" — surface darkened by fire or sun.
- 100:1 ضَبْحًا — ض ب ح B005 — "الضبح الرماد" — ash, what is left after burning.
- 100:8 لِحُبِّ — ح ب ب B011 — "نار الحباحب ما أورت الخيل لا ينتفع به"; "ما اقتدحت من شرار النار في الهواء من تصادم الحجارة" — the dictionary joins حبب, ورى, قدح and horses: the useless sparks that horses strike from stones.
- 100:3 صُبْحًا — ص ب ح B005 — "المصباح السراج وقد استصبحت به إذا أسرجت" — the lamp, fire that lasts.
- 100:3 صُبْحًا — ص ب ح B001 — "الصباح نور النهار" — daylight.
- 100:6 ٱلْإِنسَٰنَ — ء ن س B002 — "آنس من جانب يعني أبصر نارا"; "آنست نارا" — seeing a fire from far off.
- 100:6 / 100:2 — ق د ح B010 [fixed expression] — "الإنسان يقتدح الأمر إذا نظر فيه ودبر" — the phrase joins الإنسان and قدح: man strikes a matter as one strikes fire, by thinking it through.
- 100:2 — و ر ي B003 [fixed expression] — "لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب" — a firestick that catches: an undertaking that succeeds.
- 100:2 — و ر ي B009 [fixed expression] — "فلان يستوري زناد الضلالة" — trying to strike fire from the firestick of error.
- Outside: 56:71–72. God asks those who deny the resurrection: أفرأيتم النار التي تورون أأنتم أنشأتم شجرتها. 36:80: الذي جعل لكم من الشجر الأخضر نارا فإذا أنتم منه توقدون, in the answer to the man who asks who will bring bones back to life (36:78). 20:10, 27:7, 28:29: Moses, travelling with his family, says إني آنست نارا … لعلي آتيكم منها بخبر.

### 4. Turning the earth: hooves, plough, graves
The hooves "stir up" (أثرن) the ground. The dictionary uses this very verb for what happens to graves. بعثر is glossed "أثير وأخرج" and "قلب ترابها وأثير ما فيها". The same root's bull ploughs the soil, and its locusts burst out from hiding. Burial is a covering over (ورى), and the scene runs it backwards: the earth is turned, the bottom comes up, and what lay hidden comes out. حصّل closes the scene. Its root sense is working through mine-earth to take out the gold.
- 100:4 فَأَثَرْنَ — ث و ر B002 — "أثار الثور التراب إذا بحثه بقوائمه"; "أثرت الأرض إثارة" — earth dug and thrown up by feet; ground turned.
- 100:4 فَأَثَرْنَ — ث و ر B004 — "والثور البقر الذي يثار به الأرض" (mufradat) — the ox that ploughs.
- 100:4 فَأَثَرْنَ — ث و ر B001 — "ثارت الحصبة... وثار الجراد... وثار الماء... وثار الغبار وغيره كذلك"; "أصل انبعاث الشيء" — hidden things bursting out and spreading, locusts among them.
- 100:9 بُعْثِرَ — ب ع ث ر B001 — "بعثر ما في القبور أثير وأخرج؛ بعثرت الشيء إذا استخرجته وكشفته" (sihah); "قلب ترابها وأثير ما فيها" (mufradat); "بعثره بعثرة إذا قلب التراب عنه" (ayn) — the dictionary glosses بعثر with the verb of 100:4.
- 100:9 بُعْثِرَ — ب ع ث ر B003 [fixed expression] — "بعثرت حوضي أي هدمته وجعلت أسفله أعلاه" — bottom turned to top.
- 100:9 بُعْثِرَ — ب ع ث ر B002 [fixed expression] — "بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض" — goods scattered and tumbled.
- 100:9 ٱلْقُبُورِ — ق ب ر B001 — "القبر مقر الميت" — the resting place that gets turned over.
- 100:9 ٱلْقُبُورِ — ق ب ر B002 — "أصل صحيح يدل على غموض في شيء وتطامن" — sunken and hidden.
- 100:9 ٱلْقُبُورِ — ق ب ر B005 — "إذا بعثر ما في القبور إشارة إلى حال البعث" — the dictionary quotes this ayah as the raising of the dead.
- 100:2 فَٱلْمُورِيَٰتِ — و ر ي B005 — "واريت الشيء أي أخفيته وتوارى هو أي استتر" — covering over, the burial that بعثر undoes. The root that brings fire out also hides things.
- 100:10 وَحُصِّلَ — ح ص ل B002 — "أصل التحصيل استخراج الذهب أو الفضة من الحجر أو من تراب المعدن"; "المحصلة المرأة التي تحصل تراب المعدن" — going through earth to take out its precious metal.
- 100:1 ضَبْحًا — ض ب ح B001 — "الهام تضبح والبوم والذئب والصدى" — the calls of owls and echoes. From memory: in pre-Islamic belief the هامة/صدى was the owl-spirit of a slain man crying over his grave until he was avenged.
- Outside: 82:4–5. Narrator: وإذا القبور بعثرت علمت نفس ما قدمت وأخرت. 22:7: وأن الله يبعث من في القبور. 99:1–2: the earth shaken, وأخرجت الأرض أثقالها. 84:3–4: وألقت ما فيها وتخلت. 5:31: God sends a raven يبحث في الأرض to show Cain كيف يواري سوأة أخيه (ورى as burial). 30:9: earlier peoples وأثاروا الأرض. 2:71: the cow لا ذلول تثير الأرض. 54:7: يخرجون من الأجداث كأنهم جراد منتشر. 102:1–2: التكاثر … حتى زرتم المقابر (the dictionary cites حتى زرتم المقابر under ق ب ر).

### 5. The kernel taken from the husk: what the chest holds
حصّل is an act of sorting. The core is taken from the husk, the grain from the straw and the gold from the ore. What is left fixed is the total, "once everything else has gone". The chest is the container. حبّ (100:8) gives both the grain left at the threshing floor and "the black clot inside the heart". So the love the surah blames is the very seed that is sorted out at the end. خبير is knowledge of the inside as against the outside.
- 100:10 وَحُصِّلَ — ح ص ل B002 — "التحصيل إخراج اللب من القشور كإخراج الذهب من حجر المعدن والبر من التبن"; "التحصيل تمييز ما يحصل" — kernel from husk, wheat from chaff, and the sorting itself.
- 100:10 وَحُصِّلَ — ح ص ل B001 — "حصل يحصل حصولا أي بقي وثبت وذهب ما سواه من حساب أو عمل"; "أظهر ما فيها وجمع أو إظهار الحاصل من الحساب" — what stays when the rest has gone; the bottom line of an account, brought into view.
- 100:10 وَحُصِّلَ — ح ص ل B003 — "الحصالة ما يبقى في الأندر من الحب بعد ما يرفع الحب وهو الكناسة" — the dictionary joins حصل and حبّ: the sweepings left on the threshing floor once the grain is lifted.
- 100:10 وَحُصِّلَ — ح ص ل B004 — "حوصلة الطائر لأنه يجمع فيها" — the bird's crop, where food collects.
- 100:8 لِحُبِّ — ح ب ب B001 — "الحب والحبة في الحنطة والشعير وبزور الرياحين" — grain.
- 100:8 لِحُبِّ — ح ب ب B004 [fixed expression] — "حبة القلب سويداؤه ويقال ثمرته"; "حبة القلب هي العلقة السوداء التي تكون داخل القلب" — the heart's dark seed or fruit, inside the chest.
- 100:10 ٱلصُّدُورِ — ص د ر B001 — "الصدر للإنسان والجمع صدور" — the chest as container.
- 100:11 لَّخَبِيرٌۢ — خ ب ر B001 — "الخبرة المعرفة ببواطن الأمر"; "المخبر خلاف المنظر" — knowledge of the inside, the inside as against the outer look.
- 100:9 ٱلْقُبُورِ — ق ب ر B005 — "أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة" — the dictionary calls hidden inner states "buried". This joins graves and chests.
- Outside: 3:154. God, after Uhud: وليبتلي الله ما في صدوركم وليمحص ما في قلوبكم. 86:9: يوم تبلى السرائر. 3:29: قل إن تخفوا ما في صدوركم أو تبدوه يعلمه الله. 2:284: إن تبدوا ما في أنفسكم أو تخفوه يحاسبكم به الله. 99:6–8: deeds shown, an atom's weight of good and of evil.

### 6. Care given, thanks cut off
The Lord is owner and the one who raises a thing step by step to completion. He makes His favour complete. مغيرات's root, as the dictionary gives it, is God bringing rain, help and provisions. خير is the gift. كنود "cuts" thanks the way one cuts a rope. He counts his troubles and forgets the favours. The surah ends with the same Lord (ربهم) knowing those who cut Him off.
- 100:6 لِرَبِّهِۦ — ر ب ب B001 — "ورب كل شيء مالكه"; "يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح" — owner, master obeyed, the one who sets things right.
- 100:6 لِرَبِّهِۦ — ر ب ب B002 — "التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام"; "رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها" — raising a thing stage by stage; making a favour complete.
- 100:3 فَٱلْمُغِيرَٰتِ — غ ي ر B001 — "غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم"; "الغِيرة بالكسر: الميرة" — God's rain and provisions that put people's affairs right.
- 100:8 ٱلْخَيْرِ — خ ي ر B005 — "الخير الهبة"; "والخير الكرم" — gift, generosity.
- 100:6 لَكَنُودٌ — ك ن د B001 — "كند الحبل يكنده كندا"; "يكند الشكر أي يقطعه" — cutting a rope; cutting off thanks.
- 100:6 لَكَنُودٌ — ك ن د B002 — "الكنود الكفور للنعمة"; "يعد المصائب وينسى النعم"; "امرأة كند وكنود أي كفور للمواصلة" — denying favour; counting troubles and forgetting favours; not keeping up a bond.
- 100:7 لَشَهِيدٌ — ش ه د B002 — "الشهادة قول صادر عن علم" — testimony to this denial. From memory: the commentators divide over whether the witness is man against himself or his Lord.
- 100:11 رَبَّهُم — the same Lord, now as the one who knows them.
- Outside: 14:34. God: وإن تعدوا نعمت الله لا تحصوها إن الإنسان لظلوم كفار. 17:67: rescued at sea, they turn away, وكان الإنسان كفورا. 80:17: قتل الإنسان ما أكفره. 43:15: إن الإنسان لكفور مبين. 96:6–7: إن الإنسان ليطغى أن رآه استغنى. 7:172: the children of Adam made to witness over themselves, ألست بربكم.

### 7. Rain on the land: soil that yields and soil that yields nothing
The roots give a farming scene. A cloud is named for nursing plants (رباب). God brings rain (غار). Wind raises cloud and the plough raises soil (أثار). Rainwater gathers in soft low ground (خبراء) and stands (نقع). There is good clay (نقاع), a farmer (خبير), and grain (حبّ). And there is land that is كنود, which grows nothing.
- 100:6 لِرَبِّهِۦ — ر ب ب B008 — "الرباب: السحاب، سمي بذلك لأنه يرب النبات" (mufradat) — the cloud named for nursing plants.
- 100:6 لِرَبِّهِۦ — ر ب ب B013 — "الربب وهو الماء الكثير سمي بذلك لاجتماعه" — abundant water, named for its gathering.
- 100:3 فَٱلْمُغِيرَٰتِ — غ ي ر B001 — "غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم"; "سقاهم" — God's rain on them.
- 100:4 فَأَثَرْنَ — ث و ر B002 — "فتثير سحابا... وأثاروا الأرض" (mufradat) — raising cloud; turning the soil.
- 100:4 نَقْعًا — ن ق ع B001 — "نقع الماء في منقعة السيل اجتمع فيها وطال مكثه" — floodwater gathering and staying.
- 100:4 نَقْعًا — ن ق ع B007 — "النقاع واحدها نقع وهي الأرض الحرة الطين الطيبة التي لا حزونة فيها ولا ارتفاع ولا انهباط" — good, level clay land.
- 100:11 لَّخَبِيرٌۢ — خ ب ر B002 — "الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء" — low soft ground that collects rain.
- 100:11 لَّخَبِيرٌۢ — خ ب ر B003 — "الخبير الأكار" — the ploughman.
- 100:8 لِحُبِّ — ح ب ب B001 — "الحب والحبة في الحنطة والشعير" — the grain the land gives.
- 100:6 لَكَنُودٌ — ك ن د B003 [fixed expression] — "أرض كنود لا تنبت شيئا" — land that grows nothing.
- Outside: 7:57–58. God: winds carry heavy cloud to a dead land and rain brings out fruit; والبلد الطيب يخرج نباته بإذن ربه والذي خبث لا يخرج إلا نكدا … لقوم يشكرون. Land, its Lord, gratitude and the barren نكد come together. 30:48: الرياح فتثير سحابا … فترى الودق يخرج من خلاله. 30:9: وأثاروا الأرض وعمروها.

### 8. The hoard and the tied hand
خير in 100:8 is wealth, and the dictionary cites this very ayah for it. حبّ is wanting what one thinks good, and clinging to it the way a camel will not leave its spot. شديد is the miser, and the tight knot. جمع's root gives the clenched fist and the shackle that binds hands to neck. The كنود "refuses help". حصّل's root is "gathering" (جمع), so the man who gathered has what is in his chest gathered from him.
- 100:8 ٱلْخَيْرِ — خ ي ر B004 — "وإنه لحب الخير لشديد أي المال الكثير"; "لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب"; "ما كان مجموعا من المال من وجه محمود" (mufradat) — the dictionary glosses this ayah: much wealth, gathered (مجموعا).
- 100:8 لِحُبِّ — ح ب ب B002 — "المحبة إرادة ما تراه أو تظنه خيرا" (mufradat) — the dictionary joins حبّ and خير; "الحب والمحبة اشتقاقه من أحبه إذا لزمه" — love as clinging; "استحبوا أي آثروه عليه" — preferring.
- 100:8 لِحُبِّ — ح ب ب B005 — "أحب البعير إذا حرن ولزم مكانه"; "المحب البعير الذي يحسر فيلزم مكانه" — the camel that refuses to move from its spot.
- 100:8 لَشَدِيدٌ — ش د د B006 — "لشديد أي لبخيل" (tahdhib); "الشديد والمتشدد البخيل" — the miser, glossed on this ayah.
- 100:8 لَشَدِيدٌ — ش د د B001 — "شده أي أوثقه"; "الشد العقد القوي" — tying tight.
- 100:5 جَمْعًا — ج م ع B005 — "جمع الكف وهو حين تقبضها" — the closed fist.
- 100:5 جَمْعًا — ج م ع B008 — "الجامعة الغل لأنها تجمع اليدين إلى العنق" — the collar-shackle binding the hands to the neck.
- 100:5 جَمْعًا — ج م ع B001 — "الجمع ضم الشيء بتقريب بعضه من بعض" — drawing things together.
- 100:6 لَكَنُودٌ — ك ن د B002 — "يأكل وحده ويضرب عبده ويمنع رفده" — eats alone, refuses help.
- 100:10 وَحُصِّلَ — ح ص ل B001 — "أصل واحد منقاس وهو جمع الشيء" — the dictionary defines حصل as جمع: the gathering turned back on the gatherer.
- Outside: 104:1–3. Narrator: الذي جمع مالا وعدده يحسب أن ماله أخلده. 70:18–21: Hell calls من أدبر وتولى وجمع فأوعى; الإنسان خلق هلوعا … وإذا مسه الخير منوعا. 89:17–20: God to those who say "my Lord has humiliated me": لا تكرمون اليتيم … وتحبون المال حبا جما. 17:29: God: ولا تجعل يدك مغلولة إلى عنقك. 17:100: وكان الإنسان قتورا. 3:180: سيطوقون ما بخلوا به يوم القيامة. 9:34–35: the hoarded gold and silver heated and branded on their bodies. 2:180: إن ترك خيرا (خير as wealth).

### 9. The shared pot and the man who eats alone
The roots also give the scene of a feast where food is shared. There is a great pot, ladling, cups and lot-arrows kept in their case. A camel is slaughtered and its portions divided. A sheep is bought together and its meat shared. A meal greets the returning traveller. Against all this stands the كنود, who "eats alone and refuses help".
- 100:5 جَمْعًا — ج م ع B012 — "قدر جماع وجامعة وهي العظيمة" — the great cooking pot.
- 100:2 قَدْحًا — ق د ح B005 — "قدحت القدر غرفت ما فيها"; "المقدحة المغرفة"; "القديح ما يبقى في أسفل القدر فيغرف بجهد" — ladling from the pot, down to its last scrapings.
- 100:2 قَدْحًا — ق د ح B006 — "القدح واحد الأقداح التي للشرب" — the drinking cup.
- 100:2 قَدْحًا — ق د ح B007 — "القدح الواحد من قداح الميسر" — the lot-arrow.
- 100:6, 100:11 رَبّ — ر ب ب B010 — "لما يجمع فيه القدح ربابة" (mufradat); "الربابة شبيهة بالكنانة تجمع فيها سهام الميسر" — the dictionary joins رب, جمع and قدح: the case holding the lot-arrows.
- 100:4 نَقْعًا — ن ق ع B003 — "النقيعة الجزور تنقع عن عدة إبل"; "النقيعة الطعام يتخذ للقادم من السفر" — the slaughtered camel; the meal for the returning traveller.
- 100:11 لَّخَبِيرٌۢ — خ ب ر B006 — "تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها" — meat bought together and divided.
- 100:8 ٱلْخَيْرِ — خ ي ر B005 — "والخير الكرم" — generosity.
- 100:6 لَكَنُودٌ — ك ن د B002 — "يأكل وحده ويضرب عبده ويمنع رفده" — the opposite: he eats alone.
- From memory: the ميسر was played over a slaughtered camel (جزور). Its portions went out by lot-arrows, and the poets praised it as feeding the poor in hard winters.
- Outside: 76:8. Narrator, of the righteous: ويطعمون الطعام على حبه مسكينا ويتيما وأسيرا. 2:177: وآتى المال على حبه. 3:92: لن تنالوا البر حتى تنفقوا مما تحبون. 89:18: ولا تحاضون على طعام المسكين. 69:34: ولا يحض على طعام المسكين. 107:7: ويمنعون الماعون. 2:219: maysir, فيهما إثم كبير ومنافع للناس, with the question of what to spend.

### 10. Morning watering and leaving the water
Camels are given water at the start of the day (صبح). The water stands and puts out their thirst (نقع). They drink until full (حبب). Then they turn back from the water (صدر). صدور in 100:10 carries this last move. Elsewhere the Quran uses it for people turning back on the last day.
- 100:3 صُبْحًا — ص ب ح B003 — "صبحت الإبل إذا سقيتها في أول النهار"; "الصبوح ما يشرب بالغداة" — the morning watering.
- 100:4 نَقْعًا — ن ق ع B002 — "ماء ناقع كأنه استقر قراره فكسر الغلة"; "نقع الماء غلته إذا أروى عطشه" — water that breaks thirst.
- 100:4 نَقْعًا — ن ق ع B001 — "نقع الماء في منقعه استقر" — standing water.
- 100:8 لِحُبِّ — ح ب ب B006 — "شربت الإبل حتى حببت"; "أول الري التحبب" — drinking until full.
- 100:10 ٱلصُّدُورِ — ص د ر B003 — "الصدر الانصراف عن الورد وعن كل أمر"; "صدرت الإبل عن الماء" — leaving the water.
- 100:4 نَقْعًا — ن ق ع B008 — "إن فلانا لشراب بأنقع يضرب مثلا للرجل الذي قد جرب الأمور وعرفها ومارسها حتى خبرها" — "drinker at many pools": the man who has tried things until he knows them (خبرها).
- Outside: 28:23. Moses at the water of Madyan; the two women say لا نسقي حتى يصدر الرعاء. 99:6: after the earth gives up its burdens, يومئذ يصدر الناس أشتاتا ليروا أعمالهم.

### 11. The gathered host and the day of gathering
The crowd the horses break into (جمعا) is the first gathering. The root also names the place and day where people gather, the Day of Gathering included. شهيد's root names "the place where people gather" (مشهد). حصّل is a gathering. In 100:11 يومئذ fixes the day.
- 100:5 جَمْعًا — ج م ع B002 — "الجمع اسم لجماعة الناس" — the crowd.
- 100:5 جَمْعًا — ج م ع B004 — "يوم الجمع ويوم يجمعكم ليوم الجمع" (mufradat); "المجمع حيث يجمع الناس" — the Day of Gathering; the gathering place.
- 100:5 فَوَسَطْنَ — و س ط B002 — "اسما لما بين طرفي كل شيء" — the middle between the edges of the crowd.
- 100:7 لَشَهِيدٌ — ش ه د B001 — "المشهد مجمع الناس (ayn;tahdhib)"; "شهده شهودا أي حضره" — the dictionary joins شهد and جمع: being present at a gathering.
- 100:6, 100:11 رَبّ — ر ب ب B004 — "الربي: واحد الربيين، وهم الألوف من الناس"; "الربيون: الجماعات الكثيرة" — thousands, great crowds.
- 100:10 وَحُصِّلَ — ح ص ل B001 — "أصل واحد منقاس وهو جمع الشيء" — the final gathering.
- Outside: 11:103. God: ذلك يوم مجموع له الناس وذلك يوم مشهود. Joined there: جمع and شهد. 64:9: يوم يجمعكم ليوم الجمع. 85:3: وشاهد ومشهود. 36:51: من الأجداث إلى ربهم ينسلون. 3:146: a prophet with whom قاتل معه ربيون كثير.

### 12. Seeing, knowing, knowing the inside
The surah moves from the man who is present and sees (شهيد) to the question of whether he knows (يعلم). It ends with the Lord who knows the inside (خبير). The dictionary links the three: testimony is "a decisive report" (خبر), it "brings together presence, knowledge and making known", and الخبير is العالم. إنسان's root also gives seeing and hearing.
- 100:7 لَشَهِيدٌ — ش ه د B002 — "الشهادة يجمع الحضور والعلم والإعلام" (maqayis) — joins شهد and علم; "الشهادة خبر قاطع" (sihah) — joins شهد and خبر.
- 100:7 لَشَهِيدٌ — ش ه د B001 — "الشهود والشهادة الحضور مع المشاهدة" — present and seeing.
- 100:7 لَشَهِيدٌ — ش ه د B005 — "الشاهد اللسان" — the tongue as witness.
- 100:9 يَعْلَمُ — ع ل م B001 — "إدراك الشيء بحقيقته"; "ما علمت بخبرك أي ما شعرت به" — the dictionary joins علم and خبر.
- 100:11 لَّخَبِيرٌۢ — خ ب ر B001 — "الخبير العالم" — joins خبر and علم; "الخبرة الاختبار" — knowledge by testing; "الخبرة المعرفة ببواطن الأمر" — knowledge of the inside.
- 100:6 ٱلْإِنسَٰنَ — ء ن س B002 — "آنست الشيء إذا رأيته وآنسته إذا سمعته"; "آنست منه رشدا علمته" — seeing, hearing, coming to know.
- 100:4 نَقْعًا — ن ق ع B008 — "... حتى خبرها" — knowledge reached by experience.
- Outside: 67:13–14. God: إنه عليم بذات الصدور ألا يعلم من خلق وهو اللطيف الخبير. The same ألا يعلم … خبير pattern as 100:9–11. 75:14–15: بل الإنسان على نفسه بصيرة ولو ألقى معاذيره. 24:24: يوم تشهد عليهم ألسنتهم. 41:20–21: skins witness, لم شهدتم علينا. 36:65: تشهد أرجلهم. 50:16: ونعلم ما توسوس به نفسه. 82:5: علمت نفس ما قدمت وأخرت. 99:4: يومئذ تحدث أخبارها.

## Interactions
- 1 × 2: "العادية الخيل المغيرة"; "صبحناهم أي غاديناهم بالخيل" — the running horse is the raiding horse.
- 1 × 3: "نار الحباحب ما أورت الخيل لا ينتفع به"; "صوت أنفاس الخيل إذا عدون" — the same horses breathe and strike sparks; ضبح is both their breath and the scorched flint ("حجارة القداحة مضبوحة").
- 1 × 12: ش ه د B008 "الشاهد من جريه ما يشهد له على سبقه وجودته" — the horse's run is its witness; man in 100:7 is the witness over his own case.
- 1 × 5 × 10: ص د ر — the horse that wins "بصدره"; camels leaving the water (صدرت الإبل عن الماء); the chests whose contents are gathered.
- 1 × 8: 38:31–33 (Solomon's horses, أحببت حب الخير عن ذكر ربي حتى توارت) and 3:14 (الخيل المسومة among things loved) put horses and the love of wealth in one scene. ش د د gives both the gallop (B003) and the miser (B006).
- 1 × 4: 70:43 يخرجون من الأجداث سراعا كأنهم إلى نصب يوفضون and 50:44 سراعا — the dead racing out of graves; ث و ر B001 "وثار الجراد" with 54:7 كأنهم جراد منتشر.
- 2 × 4: أثرن — dust "ثار الغبار" and the soil turned "أثرت الأرض"; بعثر glossed "أثير وأخرج". The hooves' stirring and the graves' turning are one verb.
- 2 × 11: جمعا — the crowd broken into at dawn; "يوم الجمع". 37:177 (صباح المنذرين) and 11:103 (يوم مجموع له الناس … مشهود).
- 2 × 9: "النقيعة ما نحر من النهب قبل القسم" — the raid's plunder becomes slaughtered meat for division.
- 2 × 8 × 6: 68:17–24. Garden owners swear to cut its fruit مصبحين, set out at dawn (فتنادوا مصبحين), and whisper that no poor man shall enter. A visitant من ربك ruins the garden overnight (فأصبحت كالصريم). The scene joins a dawn expedition, withholding from the poor, and the Lord's answer.
- 3 × 12: 27:7 and 28:29 — Moses آنست نارا … لعلي آتيكم منها بخبر: ء ن س perception, fire and خبر in one scene.
- 3 × 4: و ر ي — bringing fire out of the firestick (B002) and covering the dead (B005; 5:31 يواري سوأة أخيه). One root both brings out and hides, and the graves' turning undoes the hiding.
- 4 × 5: ح ص ل B002 "استخراج الذهب أو الفضة من الحجر أو من تراب المعدن" — turned earth worked for its gold; ق ب ر B005 "أحوال الإنسان … مستورة كأنها مقبورة" joins graves and chests; 82:4–5, 99:2–6, 84:4.
- 5 × 8: ح ب ب — the love of 100:8 (B002), the heart's dark seed (B004 [fixed expression]) and the grain on the threshing floor ("الحصالة ما يبقى في الأندر من الحب"). The loved thing is what gets sorted out.
- 8 × 11: ج م ع — the hoarder's gathering (104:2 جمع مالا, 70:18 وجمع فأوعى) and "يوم الجمع"; ح ص ل "جمع الشيء".
- 6 × 7: ك ن د — cutting off thanks (B001) and "أرض كنود لا تنبت شيئا" (B003 [fixed expression]); the cloud that "يرب النبات" and the rain of غار. 7:58 (بإذن ربه … نكدا … يشكرون) stages both.
- 6 × 8 × 9: ك ن د B002 "يأكل وحده ويضرب عبده ويمنع رفده" — denied favour, the refused hand, the lone meal; خ ي ر as gift (B005) against خ ي ر as wealth (B004); 76:8 and 2:177 على حبه.
- 10 × 12: "شراب بأنقع … حتى خبرها" — the drinker at many pools as the man who knows.
- 10 × 4 × 5: 99:6 يصدر الناس أشتاتا ليروا أعمالهم — leaving the water becomes the return from the turned-over earth (99:2) to have deeds shown.
- 12 × 6: 7:172 — made to witness over themselves about their Lord (ألست بربكم).
- 11 × 12: "المشهد مجمع الناس"; 11:103 مجموع … مشهود.

## Ayat
- **100:1** وَٱلْعَٰدِيَٰتِ ضَبْحًا
  - 1: the gallop (العدو هو الحضر) and its breath-sound. Scene: horses run with stretched forelegs and loud breath, lean as arrow shafts, gather their whole run, and prove their lead by the chest, on the rider's side.
  - 2: "العادية الخيل المغيرة". Scene: raiding horses at dawn raise dust and the cry of the raided and charge into the middle of a gathered host.
  - 3: "حجارة القداحة مضبوحة", scorching, darkening, ash. Scene: hooves strike sparks; flint and striker scorch; ash and darkened surface remain; dawn light and lamp follow; man sees fire.
  - 4: ضبح as the calls of owls and echoes (هام/صدى; their lore from memory). Scene: hooves stir the soil; graves are turned bottom up; the hidden comes out like gold from ore.
- **100:2** فَٱلْمُورِيَٰتِ قَدْحًا
  - 3: firestick and striking iron (القداح الحجر الذي يوري النار); success and the "flint of error" [fixed expression]. Scene: struck flint gives sparks, scorch, ash, then light; man "strikes" a matter by thinking it through.
  - 1: horse trained lean like a قدح [fixed expression]. Scene: the running, breathing horse, built for the run that testifies for it.
  - 4: ورى as covering over (5:31). Scene: what was covered in burial is turned up from the graves.
  - 9: ladle, cup, lot-arrow. Scene: great pot, ladled food, lot-arrows in their case, divided meat, against the man who eats alone.
- **100:3** فَٱلْمُغِيرَٰتِ صُبْحًا
  - 2: "يوم الصباح يوم الغارة", "يا صباحاه". Scene: dawn raid, dust and cry, the charge into the crowd's middle.
  - 3: الصباح نور النهار, المصباح السراج. Scene: spark to lasting light.
  - 6: غ ي ر — God's rain and provisions. Scene: the Lord raises and provides; man cuts the bond of thanks.
  - 7: غارهم الله بالغيث. Scene: cloud, rain, low ground and good clay that yield grain, against land that grows nothing.
  - 10: صبحت الإبل. Scene: morning watering, thirst broken, drinking until full, leaving the water.
- **100:4** فَأَثَرْنَ بِهِۦ نَقْعًا
  - 2: rising dust, the sustained cry, the plunder beast. Scene: dawn raid on a gathered host.
  - 4: "أثار الثور التراب", "أثرت الأرض", "وثار الجراد"; the verb that glosses بعثر. Scene: hooves to plough to graves turned, the hidden brought out.
  - 7: "فتثير سحابا... وأثاروا الأرض"; standing floodwater; good clay. Scene: land that answers rain or grows nothing.
  - 9: النقيعة — slaughtered camel, traveller's meal. Scene: shared feast against eating alone.
  - 10: ماء ناقع that breaks thirst. Scene: morning watering and leaving.
  - 12: "شراب بأنقع … حتى خبرها". Scene: presence, knowledge, knowledge of the inside.
- **100:5** فَوَسَطْنَ بِهِۦ جَمْعًا
  - 2: "وسط فلان جماعة … إذا صار في وسطهم"; the mixed host. Scene: the charge ends in the crowd's middle.
  - 1: "استجمع الفرس جريا" [fixed expression]. Scene: the horse's gathered run.
  - 8: fist, collar-shackle, drawing together. Scene: love of wealth, tied hand, hoard, and the gathering turned back on the gatherer.
  - 9: the great pot. Scene: shared feast.
  - 11: "يوم الجمع", "المجمع". Scene: the raided crowd foreshadows the Day of Gathering, the day witnessed.
- **100:6** إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ
  - 6: the owner who raises a thing to completion; thanks cut like a rope; forgetting favours. Scene: favour raised and made complete, its return cut off.
  - 7: الرباب that nurses plants; "أرض كنود لا تنبت شيئا" [fixed expression]. Scene: rain on land that answers or yields nothing (7:58).
  - 8: "يمنع رفده". Scene: the clinging love and the closed hand.
  - 9: "يأكل وحده". Scene: shared pot against the lone eater.
  - 3: آنس نارا; "الإنسان يقتدح الأمر" [fixed expression]. Scene: fire struck, seen and used as thought.
  - 1: إنسي الدابة. Scene: the horse spends itself for its rider.
  - 11, 12: الربيون; آنست علمته. Scenes: the gathering; knowledge.
- **100:7** وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ
  - 12: presence with seeing; testimony that holds together presence, knowledge and declaring; "خبر قاطع"; the tongue. Scene: seeing, then knowing, then the Lord's knowledge of the inside.
  - 1: "الشاهد من جريه". Scene: the horse's run testifies to it.
  - 11: "المشهد مجمع الناس". Scene: the gathering, the day witnessed.
  - 6: testimony to the denial (man or his Lord; the division among commentators is from memory). Scene: thanks cut off.
- **100:8** وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
  - 8: "وإنه لحب الخير لشديد أي المال الكثير"; "لشديد أي لبخيل"; love as clinging. Scene: hoard and tied hand, gathered back at the end.
  - 1: الشد العدو. Scene: the gallop.
  - 2: شد على العدو. Scene: the charge.
  - 3: نار الحباحب. Scene: useless sparks the horses strike.
  - 5: grain; حبة القلب [fixed expression]. Scene: kernel taken from husk in the chest.
  - 6, 9: الخير الهبة / الكرم. Scenes: favour denied; shared pot.
  - 7: grain. Scene: land yielding.
  - 10: شربت الإبل حتى حببت. Scene: watering.
- **100:9** ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
  - 4: "بعثر ما في القبور أثير وأخرج"; bottom made top [fixed expression]; the sunken, hidden grave. Scene: hooves' stirring becomes the graves' turning; buried things come out.
  - 12: إدراك الشيء بحقيقته. Scene: from witnessing to knowing to the Lord's inner knowledge.
  - 5: buried inner states (ق ب ر B005). Scene: what chests hold is sorted out.
- **100:10** وَحُصِّلَ مَا فِى ٱلصُّدُورِ
  - 5: kernel from husk, gold from ore, the bottom line, threshing-floor sweepings, the crop. Scene: the chest's seed sorted and brought out.
  - 4: the woman who works mine-earth. Scene: turned earth gives up its treasure.
  - 8, 11: حصل as جمع. Scenes: the gatherer gathered; the Day of Gathering.
  - 1: the horse winning بصدره. Scene: the run.
  - 10: الصدر الانصراف عن الورد. Scene: leaving the water (99:6).
- **100:11** إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ
  - 12: الخبير العالم; knowledge of the inside; testing. Scene: present, knowing, knowing the inside.
  - 6: the same Lord. Scene: favour cut off, now known.
  - 7: low ground gathering rain; the ploughman. Scene: land under rain.
  - 9: meat bought together and divided. Scene: shared pot against the lone eater.
  - 11: يومئذ; الربيون. Scene: the day of the gathered crowd.

