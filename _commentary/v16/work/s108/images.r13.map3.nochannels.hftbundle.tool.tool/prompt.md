Surah: 108. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (108:1 to 108:3), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s108/surah.r2.nochannels/text.md =====
# Surah 108

- 108:1 إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ
- 108:2 فَصَلِّ لِرَبِّكَ وَٱنْحَرْ
- 108:3 إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ


===== _commentary/v16/out/s108/surah.map3.nochannels.hftbundle.tool/map.md (without ## Not carried) =====
# Surah 108: map of image chains

## Chains

### 1. Much good put into the hand, and the one cut off from good

The surah begins with something handed over. أعطى is built on العطو, taking in the hand, so the gift is a thing placed in the addressee's hand. What is handed over is الكوثر, the fawʿal form of كثرة: much good, and growth in number. The surah ends with الأبتر, the thing cut before it is complete, the one whose good leaves no trace. The dictionary itself joins the first two words: "الكوثر الخير الكثير الذي أعطاه النبي" (ayn) and "الكوثر الرجل الكثير العطاء والخير والسيد" (tahdhib). For the last word it uses the same noun, خير: "كل أمر انقطع من الخير أثره فهو أبتر". So the surah moves from الخير الكثير handed to "you", through the one who hates "you", to the one from whom الخير is cut off. The middle ayah turns the recipient back toward the giver, and calls the giver رب, the owner who also completes a favour (رب ... النعمة ... إذا تممها). That completion is the direct opposite of the last word's قطعته قبل الإتمام.

- 108:1 أَعْطَيْنَٰكَ: ع ط و B001, "العطو التناول باليد" (maqayis;ayn;tahdhib). The base image: a thing taken in the hand. The gift is a thing in the hand.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B002, "أعطاه مالا يعطيه إعطاء والاسم العطاء والعطية الشيء المعطى" (sihah). The transfer is complete, from "We" to "you". The thing given is now the recipient's.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B004, "الكوثر الخير الكثير الذي أعطاه النبي" (ayn); "الكوثر فوعل من الكثرة ومعناه الخير الكثير" (tahdhib). The thing handed over is much good. The ayn phrase joins the surah's first two words.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B004, "الكوثر الرجل الكثير العطاء والخير والسيد" (tahdhib). The same word names a man of much giving. The dictionary joins كوثر to عطاء, so the word carries both the gift and the giving.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B001, "الكثرة نماء العدد" (ayn;tahdhib); "الكثرة نقيض القلة" (sihah). Growth in number: plenty that keeps increasing, the opposite of قلة.
- 108:2 فَصَلِّ: ص ل و B002, "الصلاة وهي الدعاء" (maqayis;sihah). The recipient answers by turning to the giver and calling on him.
- 108:2 لِرَبِّكَ: ر ب ب B001, "ورب كل شيء مالكه" (jamhara). The giver still owns what he has given. The answer goes to the owner.
- 108:2 لِرَبِّكَ: ر ب ب B002, "رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها" (jamhara). The one addressed is the one who brings a favour to completion.
- 108:3 شَانِئَكَ: ش ن ء B001, "أصل يدل على البغضة والتجنب للشيء" (maqayis). The one who hates the recipient and keeps away from him.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "كل أمر انقطع من الخير أثره فهو أبتر" (sihah); "المنقطع العقب والمنقطع عنه كل خير" (tahdhib). The exact reversal of الخير الكثير: good whose trace is cut off.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "بترت الشيء بترا قطعته قبل الإتمام" (sihah). Cut before completion, against the رب who completes (تممها).
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "الأبتران العبد والعير لقلة خيرهما" (sihah). قلة خير, set against the opening's كثرة.

Quran passages:
- 93:5 وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰ. God to the Prophet, consoling him (scene opens 93:1 وَٱلضُّحَىٰ; 93:3 مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ). It joins يعطي, ربك and the second-person addressee, as 108:1–2 do.
- 11:108 عَطَآءً غَيْرَ مَجْذُوذٍۢ. God, of the people of the Garden (scene opens 11:105). A gift that is not cut off: giving and cutting joined in one phrase.
- 17:20 مِنْ عَطَآءِ رَبِّكَ ۚ وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا. God, on supplying both seekers of this world and seekers of the next. "Your Lord's gift" is not withheld.
- 78:36 جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا. God, of the reward of the God-fearing (scene opens 78:31).
- 38:39 هَٰذَا عَطَآؤُنَا فَٱمْنُنْ أَوْ أَمْسِكْ بِغَيْرِ حِسَابٍۢ. God to Solomon, answering his prayer (scene opens 38:35). "Our gift", given to dispose of freely.
- 53:34 وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ. God, of the man who turned away (scene opens 53:33 أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ). The gift's counter-image: giving a little, then stopping short.
- 92:5 فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ. God, contrasting the two kinds of people. The human giver.
- 20:50 رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ. Moses to Pharaoh. The Lord as the giver.
- 9:32 وَيَأْبَى ٱللَّهُ إِلَّآ أَن يُتِمَّ نُورَهُۥ; 61:8 وَٱللَّهُ مُتِمُّ نُورِهِۦ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ. God, of opponents who want to put the light out with their mouths. God completes against their attempt to cut short.
- 5:3 وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى. God's completion of his favour, matching ر ب ب B002 "النعمة ... إذا تممها".
- 36:12 وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ. God, on recording deeds and their traces. Traces are what أبتر lacks: "انقطع من الخير أثره".
- 47:9 كَرِهُوا۟ مَآ أَنزَلَ ٱللَّهُ فَأَحْبَطَ أَعْمَٰلَهُمْ; 25:23 فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا. God, of those who hated the revelation, and of the deniers' works on the Day. Their works come to nothing.

### 2. Rivalry in number, the race and the battle

Two of the surah's roots name the same act of outdoing, in the same pattern: "كاثرناهم فكثرناهم أي غلبناهم بالكثرة" and "تعاطينا فعطوته أي غلبته" (both sihah). In each, the mutual form is followed by the simple verb meaning "I beat him at it". So the opening words carry a contest: boasting over numbers of men and wealth, and contending until one side wins. The middle word adds the front line of an army and men at each other's throats. The race image adds the second horse close behind the leader, and كوثر adds the dust of death rising thick. The hater belongs to this contest of counts. By memory, the reports on the occasion of the surah say a Qurayshī (al-ʿĀṣ b. Wāʾil in most; Abū Jahl, ʿUqba b. Abī Muʿayṭ or Kaʿb b. al-Ashraf in others) called the Prophet أبتر when his son died, as a man left with no sons to count. The verdict gives the lost count to the one who boasted.

- 108:1 ٱلْكَوْثَرَ: ك ث ر B002, "كاثرناهم فكثرناهم أي غلبناهم بالكثرة" (sihah); "التفاخر بكثرة العدد والمال" (tahdhib). Contending in numbers and wealth, and winning by number.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B002, "فلان مكثور أي مغلوب في الكثرة" (mufradat). The one beaten in the count: the position the verdict assigns to the hater.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B007, "تعاطينا فعطوته أي غلبته" (sihah). Contending hand against hand, and overcoming.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B004, "التعاطي تناول ما ليس له بحق" (maqayis); "ويتعاطى ظلم فلان" (maqayis). Reaching for what is not one's right: the aggressor's move in the contest.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B005, "ثار نقع الموت حتى تكوثرا" (sihah;mufradat); "الكوثر الغبار سمي بذلك لكثرته وثورانه" (maqayis). The dust of the fight rising thick.
- 108:2 لِرَبِّكَ: ر ب ب B004, "الربيون: الجماعات الكثيرة" (tahdhib); "الربي: واحد الربيين، وهم الألوف من الناس" (sihah). Multitudes in their thousands. The tahdhib phrase joins a ر ب ب word to كثير.
- 108:2 وَٱنْحَرْ: ن ح ر B003 [fixed expression], "أقبل فلان في نحر الجيش أي في أوله" (jamhara). The front of the army.
- 108:2 وَٱنْحَرْ: ن ح ر B004 [fixed expression], "انتحر القوم على الشيء إذا تشاحوا عليه حرصا وتناحروا في القتال" (sihah); "كأن كل واحد منهم يريد نحر صاحبه" (maqayis). Grasping rivalry and fighting, each going for the other's throat.
- 108:2 فَصَلِّ: ص ل و B006, "السابق الأول والمصلي الثاني" (tahdhib); "لأن رأسه يتلو الصلا الذي بين يديه" (ayn). The second horse, its head at the leader's haunch.
- 108:3 شَانِئَكَ: ش ن ء B001, "الشنآن البغض وتشانؤوا أي تباغضوا" (sihah). Mutual hatred, in the same mutual pattern as تكاثر, تعاطى and تناحر.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "الأبتر الذي لا عقب له" (sihah). The one with no line of sons: what the contest of counts measures, assigned to the boaster.

Quran passages:
- 102:1 أَلْهَىٰكُمُ ٱلتَّكَاثُرُ. God to people distracted by rivalry in numbers. It is the surah placed just before 103 and 104.
- 57:20 وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ ... ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا. God's parable of this world: the rivalry in wealth and children withers like plants after rain.
- 34:35 وَقَالُوا۟ نَحْنُ أَكْثَرُ أَمْوَٰلًۭا وَأَوْلَٰدًۭا. The affluent of every town, answering the warners (scene opens 34:34).
- 18:34 أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا. The owner of the two gardens to his companion (scene opens 18:32). The garden is destroyed (18:42).
- 19:77–80 أَفَرَءَيْتَ ٱلَّذِى كَفَرَ بِـَٔايَٰتِنَا وَقَالَ لَأُوتَيَنَّ مَالًۭا وَوَلَدًا ... وَنَرِثُهُۥ مَا يَقُولُ وَيَأْتِينَا فَرْدًۭا. God, of a denier who boasted of wealth and sons. By memory, the occasion report (Khabbāb) names al-ʿĀṣ b. Wāʾil, the man most reports name for 108:3. He comes alone: the count reversed.
- 74:11–15 ذَرْنِى وَمَنْ خَلَقْتُ وَحِيدًۭا ... وَبَنِينَ شُهُودًۭا ... ثُمَّ يَطْمَعُ أَنْ أَزِيدَ. God, of a Meccan opponent given wealth and sons (al-Walīd b. al-Mughīra, by memory).
- 68:14 أَن كَانَ ذَا مَالٍۢ وَبَنِينَ. God, of the slanderer whose wealth and sons make him arrogant (scene opens 68:10).
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ. God, of the slanderer who gathers wealth and counts it.
- 9:25 إِذْ أَعْجَبَتْكُمْ كَثْرَتُكُمْ فَلَمْ تُغْنِ عَنكُمْ شَيْـًۭٔا. God to the believers at Ḥunayn: number alone does not decide.
- 3:146 وَكَأَيِّن مِّن نَّبِىٍّۢ قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ. God, of prophets whose many followers fought beside them. ربيون next to كثير, as in the tahdhib phrase.
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا. Oath by the charging horses raising dust (scene opens 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا). Same نقع as the line under كوثر.

### 3. The camel, from throat-front to tail

The words of the last two ayat map one animal body. Its front is the نحر, where a camel is stabbed at the top of the chest and where a necklace lies. Its back and haunch are the صلا, "وسط الظهر لكل ذي أربع", and the صلوان, the two sides of the tail. Its tail is the part بتر cuts away. The opening word adds a camel that yields to the rider and turns its head, and a man who reaches for what is not his right and hamstrings the she-camel. So the surah sets the commanded نحر of a camel, done for the Lord, against the wrongful killing of a camel. It ends on the dock-tailed one, the beast with its tail cut off at the root.

- 108:2 وَٱنْحَرْ: ن ح ر B001, "النحر ذبحك البعير بطعنة في النحر حيث يبدو الحلقوم من أعلى الصدر" (ayn;tahdhib); "موضع القلادة من الصدر وهو المنحر" (sihah;mufradat). The front of the body: top of the chest, windpipe, the place of the necklace.
- 108:2 وَٱنْحَرْ: ن ح ر B002, "النحر في اللبة مثل الذبح في الحلق" (sihah); "نحرت البعير نحرا" (maqayis). The stab at the base of the throat, which is how a camel is slaughtered.
- 108:2 فَصَلِّ: ص ل و B005, "الصلا وسط الظهر لكل ذي أربع وللناس" (ayn); "الصلوين وهما مكتنفا الذنب من الناقة وغيرها" (tahdhib). The back and the two sides of the tail: the rear of the same body.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "البتر قطع الذنب ونحوه إذا استأصلته" (tahdhib); "يستعمل في قطع الذنب" (mufradat). The tail, which the صلوان flank, cut off at the root.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B006, "أعطى البعير إذا انقاد ولم يستعصب" (sihah); "أعط فيعوج رأسه إلى راكبه" (tahdhib). The camel that yields to its rider and turns its head.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B004, "التعاطي تناول ما لا يجوز تناوله وفتعاطى الشقي عقر الناقة فبلغ ما أراد" (tahdhib); "فتعاطى فعقر" (maqayis;sihah). The wrongful killing of the she-camel: the counter-image of the commanded نحر.
- 108:2 لِرَبِّكَ: ر ب ب B007, "مرب الإبل حيث لزمته" (tahdhib). The place where the camels keep.
- 108:2 فَصَلِّ: ص ل و B009, "تسميها العرب خبزة الإبل" (ayn;tahdhib). The camels' fodder plant, "the camels' bread".

Quran passages:
- 22:36 وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ ... فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا. God, on the sacrificial camels of the pilgrimage: standing in rows, slaughtered, falling on their sides.
- 22:37 لَن يَنَالَ ٱللَّهَ لُحُومُهَا وَلَا دِمَآؤُهَا وَلَٰكِن يَنَالُهُ ٱلتَّقْوَىٰ مِنكُمْ ... كَذَٰلِكَ سَخَّرَهَا لَكُمْ. Same scene: the camels made subject to people (compare أعطى البعير إذا انقاد), and the slaughter's direction is to God.
- 22:34 وَلِكُلِّ أُمَّةٍۢ جَعَلْنَا مَنسَكًۭا لِّيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ. Same scene (opens 22:26).
- 6:162 قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ. The Prophet, instructed: prayer and sacrifice to the Lord, the pairing of 108:2.
- 5:2 وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ ... وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ. God to the believers: garlanded sacrificial animals, and a people's hatred, in one ayah. Compare نحر as "موضع القلادة".
- 5:97 وَٱلْهَدْىَ وَٱلْقَلَٰٓئِدَ. God, on the Kaʿba and its sacrificial offerings.
- 54:29 فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ. God, of Thamūd (scene opens 54:23 كَذَّبَتْ ثَمُودُ بِٱلنُّذُرِ; 54:27 إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ). The very phrase the dictionaries cite under ع ط و B004.
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا. God, of Thamūd and "the most wretched" who rose up (91:12 أَشْقَىٰهَا; scene opens 91:11). Compare tahdhib "فتعاطى الشقي".
- 37:107 وَفَدَيْنَٰهُ بِذِبْحٍ عَظِيمٍۢ. God, of Abraham's son (scene opens 37:102). The commanded sacrifice.

### 4. Slaughter, the fire and the open table

The commanded slaughter belongs to a scene of hospitality, and the surah's words carry each stage of it. The generous man is called منحار because he slaughters camels for guests. The meat is roasted at the fire, and صلى names both the fuel and the roasting. Food is handed round to the household and to those who ask with the palm. The host is كوثر, "السيد الكثير الخير" and "السخي", and he is crowded by those who seek his kindness. The house has its رب. The household tools are there too: the broad pounding-stone and the skin treated with syrup. Against this table stand the two أبتر, "العبد والعير", who are called so for their little good.

- 108:2 وَٱنْحَرْ: ن ح ر B002, "رجل منحار يوصف بالجود" (sihah). The generous host who slaughters for guests.
- 108:2 وَٱنْحَرْ: ن ح ر B002, "يوم النحر يوم الأضحى" (ayn;tahdhib). The feast day of sacrifice.
- 108:2 فَصَلِّ: ص ل و B001, "صليت اللحم شويته" (ayn;sihah;tahdhib); "الصلاء يقال للوقود وللشواء" (mufradat). The meat roasted, the fuel and the roast.
- 108:2 فَصَلِّ: ص ل و B001, "اصطليت بالنار" (maqayis;sihah). Warming oneself at the fire: guests around the fire.
- 108:2 فَصَلِّ: ص ل و B008, "الصلاية كل حجر عريض يدق عليه عطر أو هبيد" (tahdhib). The broad pounding-stone of the household.
- 108:2 لِرَبِّكَ: ر ب ب B006, "سقاء مربوب إذا أصلح بالرب" (jamhara); "المرببات الأنبجات" (sihah). A skin treated with syrup, and preserves made with it.
- 108:2 لِرَبِّكَ: ر ب ب B001, "رب الدار ورب الفرس" (mufradat). The master of the house.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B002, "المعاطاة المناولة" (maqayis;tahdhib). Handing across, from hand to hand.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B003, "عاطى الصبي أهله إذا عمل وناول ما أرادوا" (maqayis); "عطيته وعاطيته أي خدمته وقمت بأمره" (tahdhib). Serving the household and handing them what they want.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B005, "يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم" (tahdhib). The asker holding out his palm.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B004, "الكوثر من الرجال السيد الكثير الخير" (sihah); "يقال للرجل السخي كوثر" (mufradat). The generous chief.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B003 [fixed expression], "رجل مكثور عليه أي كثر من يطلب إليه معروفه" (ayn;tahdhib). The host crowded by seekers of his kindness.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "الأبتران العبد والعير لقلة خيرهما" (sihah). Those of little good, set against the host.

Quran passages:
- 22:36 فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ. God, of the slaughtered camels: eat, and feed the one who asks and the one who does not.
- 22:28 فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ. Same pilgrimage scene (opens 22:26).
- 11:69 فَمَا لَبِثَ أَن جَآءَ بِعِجْلٍ حَنِيذٍۢ. Abraham receiving his guests with a roasted calf (the scene opens on this ayah).
- 51:26–27 فَرَاغَ إِلَىٰٓ أَهْلِهِۦ فَجَآءَ بِعِجْلٍۢ سَمِينٍۢ فَقَرَّبَهُۥٓ إِلَيْهِمْ. Same scene in another surah (opens 51:24): the host hands the meal across.
- 76:8 وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا. God, of the righteous who feed others.
- 107:1–7 ... يَدُعُّ ٱلْيَتِيمَ ... وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ ... عَن صَلَاتِهِمْ سَاهُونَ ... وَيَمْنَعُونَ ٱلْمَاعُونَ. God, of the denier, in the surah placed just before this one: he pushes the orphan away, neglects prayer and withholds small kindnesses. By memory, exegetes (al-Rāzī among them) read 108 as its counterpart: much good against withholding, prayer to the Lord against neglected prayer, the open table against withheld help.
- 42:38 وَأَقَامُوا۟ ٱلصَّلَوٰةَ ... وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ. God, describing believers: prayer and spending side by side.
- 34:39 وَمَآ أَنفَقْتُم مِّن شَىْءٍۢ فَهُوَ يُخْلِفُهُۥ. The Prophet, instructed: what is spent is replaced.

### 5. The worshipper's body: standing upright and facing

The dictionary joins the surah's two commands in one phrase: "إذا انتصب الإنسان في صلاته فنهد قيل قد نحر" (ayn;tahdhib). Standing upright in prayer and pushing the chest forward is itself called نحر. Prayer is "القيام والركوع والسجود". The نحر is the top of the chest. It is held upright, set facing the qibla, and the hand is laid on it. The same root says that one thing "faces" another (تنحر). The body has its other pole in the صلا, the middle of the back. The one faced is the رب, and a place of worship is itself called صلاة. So the second ayah can be heard as one bodily scene: a worshipper standing upright, chest set toward the Lord, hand at the chest. By memory, exegetical reports read وانحر in this way: placing the right hand on the left at the chest (attributed to ʿAlī), raising the hands to the chest at the opening takbīr, or facing the qibla with the chest (al-Farrāʾ). Most read it as the sacrifice.

- 108:2 فَصَلِّ: ص ل و B003, "الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح" (tahdhib). The body's movements in prayer: standing, bowing, prostrating.
- 108:2 وَٱنْحَرْ: ن ح ر B007, "إذا انتصب الإنسان في صلاته فنهد قيل قد نحر" (ayn;tahdhib). Standing upright in prayer with the chest pushed forward. This phrase joins the two imperatives.
- 108:2 وَٱنْحَرْ: ن ح ر B007, "النحرة انتصاب الرجل في الصلاة بإزاء المحراب" (tahdhib); "استقبل القبلة بنحرك" (tahdhib). Standing opposite the prayer-niche, chest set to the qibla.
- 108:2 وَٱنْحَرْ: ن ح ر B007, "ضع يدك على نحرك" (jamhara;mufradat). The hand laid on the chest.
- 108:2 وَٱنْحَرْ: ن ح ر B001, "مجال القلادة من الصدر" (jamhara). The top of the chest, the part of the body set forward.
- 108:2 وَٱنْحَرْ: ن ح ر B003 [fixed expression], "هذه الدار تنحر تلك الدار إذا استقبلتها" (ayn); "نحرت الرجل إذا صرت في نحره" (sihah). Facing, being directly in front of.
- 108:2 فَصَلِّ: ص ل و B005, "الصلا وسط الظهر لكل ذي أربع وللناس" (ayn). The middle of the back, the body's rear pole opposite the chest.
- 108:2 فَصَلِّ: ص ل و B007, "يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات" (mufradat). The place of worship that the body stands in and faces.
- 108:2 لِرَبِّكَ: ر ب ب B001, "ويكون الرب: السيد المطاع" (tahdhib). The obeyed master whom the body faces.

Quran passages:
- 2:144 فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ. God to the Prophet, turning him to the qibla he desired.
- 6:79 إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ. Abraham, turning from his people's objects of worship.
- 3:43 يَٰمَرْيَمُ ٱقْنُتِى لِرَبِّكِ وَٱسْجُدِى وَٱرْكَعِى مَعَ ٱلرَّٰكِعِينَ. The angels to Maryam (scene opens 3:42). The same build as فَصَلِّ لِرَبِّكَ: a command of bodily worship, then لربك.
- 22:26 وَطَهِّرْ بَيْتِىَ لِلطَّآئِفِينَ وَٱلْقَآئِمِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ. God to Abraham: the House and the standing, bowing, prostrating bodies.
- 22:40 لَّهُدِّمَتْ صَوَٰمِعُ وَبِيَعٌۭ وَصَلَوَٰتٌۭ وَمَسَٰجِدُ. God, defending those driven from their homes. صلوات here is places of worship (ص ل و B007).
- 15:97–98 وَلَقَدْ نَعْلَمُ أَنَّكَ يَضِيقُ صَدْرُكَ بِمَا يَقُولُونَ فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ ٱلسَّٰجِدِينَ. God to the Prophet, whose chest is tightened by the mockers' talk (scene opens 15:94 فَٱصْدَعْ بِمَا تُؤْمَرُ; 15:95 إِنَّا كَفَيْنَٰكَ ٱلْمُسْتَهْزِءِينَ; ends 15:99 وَٱعْبُدْ رَبَّكَ). The answer to hostile speech is prayer to "your Lord".

### 6. The front of the day, and the prayer when the sun puts out its rays

نحر also names the first part of the day, and the night that meets the new crescent. يوم النحر is the feast of the Aḍḥā. The last word of the surah has a branch (tahdhib) in which أبتر means to pray the forenoon prayer when the sun's rays come out like rods, and البتيراء is the sun. The dictionary thus joins بتر to صلى. These words make a morning scene: the day's front edge, the sun's rays striking the ground, the forenoon prayer, and on the day of sacrifice the slaughter after it. By memory, several early exegetes (Qatāda, ʿIkrima, ʿAṭāʾ) read فصل لربك وانحر as the feast prayer followed by the sacrifice. A hadith (by memory) orders anyone who slaughters before the prayer to slaughter again.

- 108:2 وَٱنْحَرْ: ن ح ر B006, "نحر النهار أوله" (sihah); "استقبل نحر النهار أي أوله" (jamhara). The front of the day.
- 108:2 وَٱنْحَرْ: ن ح ر B006, "نحيرة لأنها تنحر الهلال أي تستقبله" (tahdhib). The month's last night meeting the new crescent: a boundary of time faced.
- 108:2 وَٱنْحَرْ: ن ح ر B002, "يوم النحر يوم الأضحى" (ayn;tahdhib). The day of sacrifice, named for the forenoon (أضحى).
- 108:2 فَصَلِّ: ص ل و B003, "الصلاة واحدة الصلوات المفروضة" (sihah). The prayer at its time.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B005, "أبتر إذا صلى الضحى حين تقضب الشمس؛ تقضب أي يخرج شعاعها كالقضبان؛ حين تبهر البتيراء الأرض؛ البتيراء الشمس" (tahdhib). Praying at forenoon as the sun shoots out its rays and floods the ground. The dictionary joins بتر and صلى.

Quran passages:
- 93:1–5 وَٱلضُّحَىٰ ... مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ ... وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ. God's oath by the forenoon, then consolation of the Prophet. The forenoon, ربك and يعطيك in one scene.
- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا. Oath by the sun and its forenoon light.
- 20:130 فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ ... وَأَطْرَافَ ٱلنَّهَارِ. God to the Prophet: bear what they say, and praise your Lord at the edges of the day.
- 11:114 وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ. God to the Prophet: prayer at the day's two edges.
- 17:78 أَقِمِ ٱلصَّلَوٰةَ لِدُلُوكِ ٱلشَّمْسِ ... وَقُرْءَانَ ٱلْفَجْرِ. God to the Prophet: prayer timed by the sun.
- 87:14–15 قَدْ أَفْلَحَ مَن تَزَكَّىٰ وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ. God. By memory, some early readers took these as the feast-day alms and the feast prayer. Like 108:2, it joins prayer to ربه.

### 7. Birth, rearing to completion, and the line cut off

The surah's words carry a cycle of offspring. The صلا is where a she-camel's young drops when her delivery is near. The ربى is the ewe that has just given birth, and ربان is the fresh first stage of youth. تربية is raising a thing stage by stage "إلى حد التمام". كثرة is growth in number. Its plant form, الكثر, is the palm's growing heart or first spathe, the point from which the tree grows. Against all this stands أبتر: the thing cut "قبل الإتمام", the man with no descendants. Two definitions share one word: rearing goes "إلى حد التمام", and بتر cuts "قبل الإتمام". The verdict on the hater is a line that does not reach its completion. By memory, the occasion reports say the taunt came at the death of the Prophet's son.

- 108:2 فَصَلِّ: ص ل و B005, "كل أنثى إذا ولدت انفرج صلاها" (ayn); "أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها" (tahdhib). Birth: the young drops into the haunch as delivery comes near.
- 108:2 لِرَبِّكَ: ر ب ب B009, "الربى: الشاة التي وضعت حديثا" (sihah); "الربى: أول الشباب" (tahdhib). The newly delivered ewe, and the first freshness of youth.
- 108:2 لِرَبِّكَ: ر ب ب B002, "التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام" (mufradat); "رب فلان ولده؛ رباه" (sihah). Raising the child stage by stage to its completion.
- 108:2 لِرَبِّكَ: ر ب ب B005, "الراب والرابة بأحد الزوجين إذا تولى تربية الولد" (mufradat). The one who takes on a child's rearing, even beyond descent.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B001, "الكثرة نماء العدد" (ayn;tahdhib). Increase in number: a line that multiplies.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B006, "الكثر جمار النخل ويقال طلعها" (sihah); "الكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا" (ayn). The palm's heart or first spathe, its point of growth: the same cycle in the plant.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "بترت الشيء بترا قطعته قبل الإتمام" (sihah); "أصل واحد وهو القطع قبل أن تتمه" (maqayis). Cut before completion.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "الأبتر الذي لا عقب له" (sihah); "أجري قطع العقب مجراه فقيل فلان أبتر إذا لم يكن له عقب" (mufradat). No descendants: the line cut off.

Quran passages:
- 33:40 مَّا كَانَ مُحَمَّدٌ أَبَآ أَحَدٍۢ مِّن رِّجَالِكُمْ وَلَٰكِن رَّسُولَ ٱللَّهِ وَخَاتَمَ ٱلنَّبِيِّۦنَ. God: no son's line, but a messenger and the last of the prophets.
- 43:28 وَجَعَلَهَا كَلِمَةًۢ بَاقِيَةًۭ فِى عَقِبِهِۦ. God, of Abraham's word lasting in his descendants (scene opens 43:26). عقب, the word أبتر is defined by.
- 37:77 وَجَعَلْنَا ذُرِّيَّتَهُۥ هُمُ ٱلْبَاقِينَ. God, of Noah's descendants surviving (scene opens 37:75).
- 26:84 وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ. Abraham's prayer for a true name among later generations.
- 3:38 رَبِّ هَبْ لِى مِن لَّدُنكَ ذُرِّيَّةًۭ طَيِّبَةً. Zakariyyā praying for offspring.
- 19:5–6 وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا يَرِثُنِى. Zakariyyā fearing that his line will end (scene opens 19:2).
- 21:89 رَبِّ لَا تَذَرْنِى فَرْدًۭا وَأَنتَ خَيْرُ ٱلْوَٰرِثِينَ. Zakariyyā: "do not leave me alone".
- 19:80 وَنَرِثُهُۥ مَا يَقُولُ وَيَأْتِينَا فَرْدًۭا. God, of the boaster of 19:77: in the end, the one left alone.
- 2:266 جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ ... وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ. God's parable: a palm garden, weak children, and the garden burned before it can serve them. Palm, offspring and the cut in one scene.
- 63:9 لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ. God to the believers: children and wealth set against God's remembrance.

### 8. The bond kept and the bond cut

The middle word carries the ties that hold people together. رب is a covenant and the people bound by it. It is staying in a place and not leaving it, and it is the bond of fostering, the step-parent who takes charge of the child. The opening word adds service within the household. The hater's root is "البغضة والتجنب": recoiling as from filth, and in one fixed use driving the king out from among them. The last word names the man who cuts his kinship tie. The verdict puts the one who recoiled and cut on the cut side.

- 108:2 لِرَبِّكَ: ر ب ب B011, "الربابة: العهد والميثاق؛ الأربة أهل الميثاق" (sihah); "العقد في موالاة الغير: الربابة" (mufradat). The covenant, and the people bound by it.
- 108:2 لِرَبِّكَ: ر ب ب B007, "أرب فلان بالمكان إذا أقام به فلم يبرحه" (tahdhib). Staying and not leaving.
- 108:2 لِرَبِّكَ: ر ب ب B005, "ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب" (maqayis). A bond made by care, beyond descent.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B003, "هو يعطيني ويعاطيني إذا كان يخدمك" (sihah). Service inside the household.
- 108:3 شَانِئَكَ: ش ن ء B001, "أصل يدل على البغضة والتجنب للشيء" (maqayis). Hatred and keeping away.
- 108:3 شَانِئَكَ: ش ن ء B002, "الشنوءة التقزز وهو التباعد من الأدناس" (sihah). Recoiling as from filth.
- 108:3 شَانِئَكَ: ش ن ء B003 [fixed expression], "شنئوا الملك أي أخرجوه من عندهم" (tahdhib). Driving someone out from among them.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B004, "رجل أباتر يقطع رحمه يبترها" (maqayis); "رجل أباتر للذي يقطع رحمه" (sihah). The one who cuts his kinship tie.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "الانبتار الانقطاع" (sihah). Being cut off: the result, on the cutter's side.

Quran passages:
- 2:27 ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ ... أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ. God, of the corrupt: covenant broken and ties cut. Both halves of this chain in one ayah.
- 13:25 وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ ... أُو۟لَٰٓئِكَ لَهُمُ ٱللَّعْنَةُ. Same, contrasted with those who join (13:21).
- 47:22 فَهَلْ عَسَيْتُمْ إِن تَوَلَّيْتُمْ أَن تُفْسِدُوا۟ فِى ٱلْأَرْضِ وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ. God to the wavering: turning away goes with cutting kinship.
- 26:214 وَأَنذِرْ عَشِيرَتَكَ ٱلْأَقْرَبِينَ. God to the Prophet: his nearest kin, the people the taunt came from.
- 42:23 قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا إِلَّا ٱلْمَوَدَّةَ فِى ٱلْقُرْبَىٰ. The Prophet, instructed: he asks only for affection within kinship.
- 8:30 لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ. God to the Prophet, on the Meccans' plot: to drive him out (compare شنئوا الملك أي أخرجوه).
- 9:40 إِذْ أَخْرَجَهُ ٱلَّذِينَ كَفَرُوا۟ ثَانِىَ ٱثْنَيْنِ. God, of the Prophet driven out at the Hijra.

### 9. Praise spoken, and speech cut off

صلاة is calling on God. From God, it is mercy and fine praise, and from the angels, asking forgiveness. The last word has a fixed use in which a speech is بتراء when it does not open with praise of God and صلاة on the Prophet. The dictionary thus joins بتر to صلاة: the speech with no صلاة is the cut-off one. Al-Mufradāt glosses 108:3 itself as "المقطوع الذكر", cut off from mention. كوثر adds the talkative one, and the hater's root adds the one people hate. So there are two kinds of speech here. One is praise said for the Prophet and for God, and it lasts. The other is the hater's talk, which has no blessing, and his name ends with it.

- 108:2 فَصَلِّ: ص ل و B002, "الصلاة وهي الدعاء" (maqayis;sihah); "صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم" (ayn); "صلاة الملائكة الاستغفار" (ayn;tahdhib;mufradat). Calling on God; God's praise of people; the angels' asking forgiveness.
- 108:2 فَصَلِّ: ص ل و B002, "صلوات الرسول للمسلمين دعاؤه لهم" (ayn). The messenger's call on behalf of others.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B003 [fixed expression], "خطبته البتراء لأنه لم يفتتحها بحمد الله تعالى والصلاة على النبي" (maqayis); "خطب زياد خطبته البتراء لأنه لم يحمد الله فيها ولم يصل على النبي" (sihah). The speech cut off because it lacks praise and صلاة. The dictionary joins بتر and صلى.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B003 [fixed expression], "كل أمر لا يبدأ فيه بذكر الله فهو أبتر" (mufradat). Anything begun without God's mention is cut off.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B002, "إن شانئك هو الأبتر أي المقطوع الذكر" (mufradat). The hater cut off from mention.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B003 [fixed expression], "رجل مكثار وامرأة مكثار وهما الكثيرا الكلام" (ayn). Much talk.
- 108:3 شَانِئَكَ: ش ن ء B004, "رجل مشناء إذا كان يبغضه الناس" (maqayis); "رجل شناءة وشنائية مبغض سيء الخلق" (ayn). The one people hate, of bad character.
- 108:3 شَانِئَكَ: ش ن ء B003 [fixed expression], "شنئ به أي أقر" (sihah). Acknowledging, saying yes to a thing.

Quran passages:
- 33:56 إِنَّ ٱللَّهَ وَمَلَٰٓئِكَتَهُۥ يُصَلُّونَ عَلَى ٱلنَّبِىِّ ۚ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ صَلُّوا۟ عَلَيْهِ. God: the صلاة on the Prophet from God, angels and believers.
- 33:43 هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ. God's صلاة on the believers.
- 2:157 أُو۟لَٰٓئِكَ عَلَيْهِمْ صَلَوَٰتٌۭ مِّن رَّبِّهِمْ وَرَحْمَةٌۭ. God, of the patient in loss (scene opens 2:155): صلوات from their Lord.
- 94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ. God to the Prophet: his mention raised.
- 20:14 وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ. God to Moses: prayer for God's mention.
- 15:6 وَقَالُوا۟ يَٰٓأَيُّهَا ٱلَّذِى نُزِّلَ عَلَيْهِ ٱلذِّكْرُ إِنَّكَ لَمَجْنُونٌۭ. The deniers to the Prophet: hostile speech about the one given the ذكر.
- 52:30 أَمْ يَقُولُونَ شَاعِرٌۭ نَّتَرَبَّصُ بِهِۦ رَيْبَ ٱلْمَنُونِ. The deniers waiting for the Prophet's death, expecting his name to end with him.
- 37:78–79 وَتَرَكْنَا عَلَيْهِ فِى ٱلْءَاخِرِينَ سَلَٰمٌ عَلَىٰ نُوحٍۢ فِى ٱلْعَٰلَمِينَ. God, of Noah: a blessing kept on his name among later generations.

### 10. Water gathered, branching and pouring

The surah's words also carry water. الكوثر is a river in the Garden from which most of the Garden's rivers branch. رب names abundant water, called so because it gathers. It also names the low, piled cloud, called so because it nurtures plants, and a cloud that stays. نحر, in one fixed use, names a cloud pouring out much water at once, as if slaughtered. Against the river and the downpour stands الانبتار, the flow cut off. By memory, a hadith (Muslim, from Anas) has the Prophet wake smiling after a doze, recite this surah, and say that the Kawthar is a river his Lord promised him, with much good, and a pool his community will come to drink from.

- 108:1 ٱلْكَوْثَرَ: ك ث ر B004, "الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة" (ayn); "الكوثر نهر في الجنة وأراد الخير الكثير" (maqayis). The river from which most rivers of the Garden branch.
- 108:2 لِرَبِّكَ: ر ب ب B013, "الربب وهو الماء الكثير سمي بذلك لاجتماعه" (maqayis); "الربب، بالفتح: الماء الكثير، ويقال العذب" (sihah). Much water, gathered, and fresh. The phrase joins a ر ب ب word to كثير.
- 108:2 لِرَبِّكَ: ر ب ب B008, "الرباب: السحاب، سمي بذلك لأنه يرب النبات" (mufradat); "الربابة: السحابة التي قد ركب بعضها بعضا" (tahdhib). Cloud piled layer on layer, which nurtures plants.
- 108:2 لِرَبِّكَ: ر ب ب B007, "أربت السحابة: دامت" (mufradat). The cloud that stays.
- 108:2 وَٱنْحَرْ: ن ح ر B009 [fixed expression], "السحاب إذا انعق بماء كثير قد انتحر انتحارا" (tahdhib); "كأنه منحور" (tahdhib). The cloud bursting with much water, like a slaughtered animal.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "الانبتار الانقطاع" (sihah). The flow cut off.

Quran passages:
- 47:15 فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ ... وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ. God's likeness of the Garden: its rivers, set against the scalding water that cuts.
- 24:43 يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ. God's sign: cloud gathered and piled, then rain pouring out of it.
- 78:14 وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا. God's provision: water pouring from the rain clouds.
- 2:266 جَنَّةٌۭ ... تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ. God's parable of the palm garden (as in chain 7): rivers, and a cut.

### 11. The hand: reaching, handing, asking and cutting

ع ط و is a root of the hand. It means taking in the hand, as the gazelle rises on its forelegs to reach the leaves. It means passing from hand to hand, as men pass a sword between them and each brandishes it in turn. It means asking with the palm held out, and reaching for what is not one's right. وانحر adds the hand laid on the chest. The hater's root, in a fixed use, names acknowledging another's right and handing it out from oneself. Two hand-cuttings close the chain. Under كثر, the dictionaries cite the ruling "لا قطع في ثمر ولا كثر": no hand is cut for taking fruit or palm heart. Under بتر, the sword that cuts. So the surah's words carry the hand that receives, hands on, rests on the chest, asks and takes, and they carry the blade.

- 108:1 أَعْطَيْنَٰكَ: ع ط و B001, "الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق" (ayn). Raised forelimbs reaching to take.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B002, "المعاطاة أن يستقبل رجل رجلا ومعه سيف فيقول أرني سيفك فيعطيه فيهزه هذا ساعة وهذا ساعة" (tahdhib). A sword passed from hand to hand and brandished in turn.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B005, "يستعطي الناس بكفه وفي كفه استعطاء" (tahdhib). The palm held out to ask.
- 108:1 أَعْطَيْنَٰكَ: ع ط و B004, "التعاطي تناول ما ليس له بحق" (maqayis). The hand reaching for what is not its right.
- 108:2 وَٱنْحَرْ: ن ح ر B007, "ضع يدك على نحرك" (jamhara;mufradat). The hand laid on the chest.
- 108:3 شَانِئَكَ: ش ن ء B003 [fixed expression], "شنئت حقك أي أقررت به وأخرجته من عندي" (tahdhib). Acknowledging another's right and handing it out from one's own keeping.
- 108:1 ٱلْكَوْثَرَ: ك ث ر B006, "لا قطع في ثمر ولا كثر" (jamhara;sihah;tahdhib;mufradat). No cutting of the hand for fruit or palm heart.
- 108:3 ٱلْأَبْتَرُ: ب ت ر B001, "سيف باتر وبتار قطاع" (tahdhib). The sword that cuts.

Quran passages:
- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ. God, of the Prophet's uncle and enemy: his hands perish. By memory, some occasion reports name Abū Lahab among those who rejoiced at the death of the Prophet's son.
- 38:39 هَٰذَا عَطَآؤُنَا فَٱمْنُنْ أَوْ أَمْسِكْ. God to Solomon: give freely, or hold back.
- 9:58 فَإِنْ أُعْطُوا۟ مِنْهَا رَضُوا۟ وَإِن لَّمْ يُعْطَوْا۟ مِنْهَآ إِذَا هُمْ يَسْخَطُونَ. God, of those who carp at the Prophet over alms: hands that only want to receive.

## Interactions

- Chains 1 and 7: completion against cutting short. ر ب ب B002 "إذا تممها" and "إلى حد التمام" against ب ت ر B001 "قطعته قبل الإتمام". The same word تمام sits in both definitions. Staged by 9:32 / 61:8 (أَن يُتِمَّ نُورَهُۥ against opponents) and 5:3.
- Chains 1 and 4: كوثر names both the gift and the generous giver ("الرجل الكثير العطاء", "السخي"). The generous man is also منحار. The two أبتر, "العبد والعير", are named for little good. The dictionary phrase joins كوثر and عطاء.
- Chains 3 and 4: the camel stabbed at the نحر is the meat roasted at the fire (صليت اللحم شويته) and handed round. 22:36 stages the slaughter and the feeding together.
- Chains 3 and 5: the same نحر. The camel is stabbed there, and the worshipper holds it upright and sets it toward the qibla. ن ح ر B007 "إذا انتصب الإنسان في صلاته فنهد قيل قد نحر" joins the surah's two imperatives. 6:162 stages prayer and sacrifice together.
- Chains 3 and 7: the صلا is both the flanks of the tail (ص ل و B005 "مكتنفا الذنب") and the place where the young drops at birth (أصلت الناقة ... وقرب نتاجها). بتر cuts the tail (قطع الذنب) and the line (لا عقب له). Same body part, same cut.
- Chains 2 and 3: the race horse's head follows the leader's صلا (ص ل و B006 "لأن رأسه يتلو الصلا"), the body part of chain 3. 54:29 فَتَعَاطَىٰ فَعَقَرَ joins the wrongful reach of chain 2 to the camel of chain 3.
- Chains 3, 8 and 2: 5:2 puts الهدي and القلائد (the place of the necklace, نحر B001 "موضع القلادة") in the same ayah as شَنَـَٔانُ قَوْمٍ, the only other ش ن ء noun in the Quran. Sacrifice and hatred are staged together.
- Chains 5 and 6: the body upright in prayer, at the day's front edge. ن ح ر B007 (prayer posture) and B006 (نحر النهار أوله) are the same root. ب ت ر B005 "أبتر إذا صلى الضحى" puts the prayer at forenoon.
- Chains 6 and 9, with chain 1: the dictionary joins بتر and صلى twice. The verb أبتر means "prayed the forenoon prayer" (B005), and the بتراء speech is the one lacking الصلاة على النبي (B003). The surah's last word holds the very prayer the hater lacks.
- Chains 2 and 7: the contest of counts is a count of sons. ك ث ر B002 "التفاخر بكثرة العدد والمال" and ب ت ر B002 "الأبتر الذي لا عقب له". Staged by 19:77–80 (مالا وولدا ... فردا), 74:11–13 and 34:35.
- Chains 2 and 4: 57:20 (تَكَاثُرٌۭ ... ثُمَّ يَهِيجُ) sets the rivalry of counts in a withering plant. ر ب ب B012 names a plant "لا تهيج في الصيف" (tahdhib), one that does not wither.
- Chains 2 and 8: hatred, rivalry and fighting are each a mutual form. Compare تشانؤوا (ش ن ء B001), تكاثر, تعاطى and تناحروا (ن ح ر B004). 8:30 stages the hostile plot as driving out (compare ش ن ء B003 "شنئوا الملك أي أخرجوه").
- Chains 5 and 9: 15:97–98 has the chest tightened by hostile speech (يَضِيقُ صَدْرُكَ بِمَا يَقُولُونَ) answered by praise and prostration to "your Lord". That is the shape of 108:2–3, with the body of chain 5 and the speech of chain 9.
- Chains 1 and 10: the river (الكوثر نهر في الجنة) is the much good given. ر ب ب B013 "الماء الكثير" joins a word of the middle ayah to كثير. The cut flow (الانبتار الانقطاع) ends both chains.
- Chains 2 and 10: كوثر is two things that rise in plenty: the battle dust ("الكوثر الغبار سمي بذلك لكثرته وثورانه") and the river. The deniers' works become dust in 25:23 (هَبَآءًۭ مَّنثُورًا).
- Chains 4 and 1, through fire: ص ل و B001 roasts the sacrificial meat ("صليت اللحم شويته"), and the same branch has "الصلا النار وصلى الكافر نارا" (ayn). The Quran uses this verb for two men whom reports (by memory) name among the Prophet's mockers: 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ (Abū Lahab) and 74:26 سَأُصْلِيهِ سَقَرَ (the man of 74:11).
- Chains 4 and 107: the surah before this one stages the opposite of chains 1, 4 and 5 together: withholding (يَمْنَعُونَ ٱلْمَاعُونَ), neglected prayer (عَن صَلَاتِهِمْ سَاهُونَ) and the orphan pushed away (107:2).
- Chains 8 and 7: ر ب ب B005 (fostering: "الراب ... إذا تولى تربية الولد") makes a bond outside descent. ب ت ر B004 cuts the kinship tie. 33:40 stages the Prophet with no son's line and a lasting office.
- Chains 11 and 1: the gift is a thing in the hand (ع ط و B001–B002). The hater's root hands a right out of one's own keeping (ش ن ء B003). بتر is the blade (سيف باتر). In ع ط و B002, the sword passes from hand to hand.

## Ayat

### 108:1 إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ

- Chain 1: أعطينا puts a thing in the hand and completes the transfer. الكوثر is the much good handed over and the man of much giving ("الخير الكثير الذي أعطاه النبي"; "الرجل الكثير العطاء"). Whole scene: much good is placed in the addressee's hand by "We". The response goes back to the owner who completes favours. The one who hates the recipient is the one whose good leaves no trace (كل أمر انقطع من الخير أثره).
- Chain 2: كوثر carries contending in number and winning (كاثرناهم فكثرناهم) and the dust of death rising (تكوثر). أعطى carries the hand-to-hand contest (تعاطينا فعطوته أي غلبته) and the wrongful reach (التعاطي). Whole scene: a contest of counts, with the front of the army, throats and dust, ends with the boaster beaten in the count, left with no line of sons.
- Chain 3: أعطى carries the camel that yields and turns its head to the rider, and the wretch who reached out and hamstrung the she-camel. Whole scene: a camel's body from the نحر where it is stabbed for the Lord, to the صلا of the back and tail-flanks, to the tail cut away (بتر).
- Chain 4: أعطى carries handing across, serving the household, and the asker's open palm. كوثر carries the generous chief crowded by seekers. Whole scene: the generous host slaughters, roasts at the fire and hands food round, while the أبتر, "العبد والعير", have little good.
- Chain 7: كوثر carries growth in number and the palm's growing heart. Whole scene: young born and reared stage by stage "إلى حد التمام", against a line cut "قبل الإتمام" and left without descendants.
- Chain 8: أعطى carries service inside the household (يعاطيني إذا كان يخدمك). Whole scene: covenant, staying and fostering hold people together. The hater recoils, drives out and cuts the kinship tie, and he ends on the cut side.
- Chain 9: كوثر carries much talk (مكثار). Whole scene: praise said for the Prophet and for God lasts, while the hater's speech without blessing (بتراء) leaves him cut off from mention.
- Chain 10: كوثر is the river from which the Garden's rivers branch. Whole scene: river, gathered water and piled cloud pour out their plenty, against a flow cut off.
- Chain 11: أعطى is a root of the hand: reaching up, passing a sword from hand to hand, asking with the palm, reaching wrongly. كثر carries "لا قطع في ثمر ولا كثر". Whole scene: the hand that receives, hands on, rests on the chest and asks, and the blade that cuts.

### 108:2 فَصَلِّ لِرَبِّكَ وَٱنْحَرْ

- Chain 1: صل is the turning back to the giver (الدعاء). لربك names the owner who completes the favour ("النعمة ... إذا تممها"). Whole scene: as at 108:1.
- Chain 2: نحر carries the front of the army and men at each other's throats (تناحروا في القتال). صل carries the second horse close behind the leader. رب carries the thousands (الربيون: الجماعات الكثيرة). Whole scene: as at 108:1.
- Chain 3: نحر is the top of the chest where the camel is stabbed, and the stab itself. صلا is the back and the two sides of the tail. رب is the place where the camels keep, and صليان is their fodder. Whole scene: as at 108:1.
- Chain 4: نحر gives the generous slaughterer (منحار) and the day of sacrifice. صلى gives the roasting fire, the fuel and the warming. رب gives the master of the house and the skin treated with syrup. صلاية gives the pounding-stone. Whole scene: as at 108:1.
- Chain 5: صل is standing, bowing and prostrating. نحر is standing upright in prayer with the chest forward, the hand laid on the chest, the chest set to the qibla, and facing. صلا is the back. صلوات are places of worship. رب is the obeyed one faced. Whole scene: a worshipper standing upright, chest set toward the Lord, hand at the chest, back and front placed in the act.
- Chain 6: نحر is the front of the day and the night facing the new crescent. يوم النحر is the day of the Aḍḥā. صل is the prayer at its time. Whole scene: at the day's front edge, as the sun puts out its rays, the forenoon prayer is prayed, and on the day of sacrifice the slaughter follows.
- Chain 7: صلا is where the young drops at birth. رب is the newly delivered ewe, the first freshness of youth, rearing to completion, and fostering. Whole scene: as at 108:1.
- Chain 8: رب is the covenant, the staying, and the fostering bond. Whole scene: as at 108:1.
- Chain 9: صل is calling on God, God's fine praise, and the angels' asking forgiveness. Whole scene: as at 108:1.
- Chain 10: رب is much gathered water, piled cloud that nurtures plants, and the cloud that stays. انتحر [fixed expression] is the cloud bursting with water. Whole scene: as at 108:1.
- Chain 11: نحر carries the hand laid on the chest. Whole scene: as at 108:1.

### 108:3 إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ

- Chain 1: شانئ is the one who hates and keeps away. الأبتر is the one whose good is cut off, cut before completion, of little good like "العبد والعير". Whole scene: as at 108:1.
- Chain 2: شانئ carries mutual hatred (تشانؤوا). الأبتر is the one without a line of sons, beaten in the count he boasted of. Whole scene: as at 108:1.
- Chain 3: الأبتر is the tail cut off at the root (قطع الذنب). Whole scene: as at 108:1.
- Chain 4: الأبتر, "العبد والعير لقلة خيرهما", stands outside the table. Whole scene: as at 108:1.
- Chain 6: الأبتر also means "prayed the forenoon prayer when the sun shoots out its rays", and البتيراء is the sun. Whole scene: as at 108:2.
- Chain 7: الأبتر is cut "قبل الإتمام", with no عقب. Whole scene: as at 108:1.
- Chain 8: شانئ is hatred and keeping away, recoiling as from filth, and driving out [fixed expression]. الأبتر is the one who cuts his kinship tie, and the cut itself (الانبتار). Whole scene: as at 108:1.
- Chain 9: الأبتر is the speech that opens without praise and صلاة [fixed expression], and the one cut off from mention (المقطوع الذكر). شانئ is the one people hate, and acknowledging [fixed expression]. Whole scene: as at 108:1.
- Chain 10: الانبتار is the flow cut off. Whole scene: as at 108:1.
- Chain 11: شانئ carries handing a right out from oneself [fixed expression]. بتر is the cutting sword. Whole scene: as at 108:1.

