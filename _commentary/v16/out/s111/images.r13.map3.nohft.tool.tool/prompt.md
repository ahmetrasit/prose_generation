Surah: 111. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (111:1 to 111:5), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s111/surah.r2/text.md =====
# Surah 111

- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/out/s111/surah.map3.nohft.tool/map.md (without ## Not carried) =====
# Surah 111: map of image chains

Note on evidence: the root of ذَاتَ (111:3) has no entry in dictionary.md. Where this map uses ذَاتَ, it relies on the surah text alone. "Memory" marks material that comes from my own knowledge of tafsir, hadith or sira and not from the dictionary or the text.

## Chains

### 1. The hands that earn, the hands that lose

111:1 lays the ruin on the two hands, and then (وَتَبَّ) on the whole man. 111:2 names what those hands held and earned (مَالُهُۥ, كَسَبَ) and denies that any of it covered him (مَآ أَغْنَىٰ عَنْهُ). The dictionary ties the two ayat together in two ways. It joins تب and يد in one phrase, and it joins يد and كسب in one phrase. It also calls the working limbs themselves "the earners" (الكواسب). So the hands of 111:1 are the organs of the earning in 111:2. The man stretched out his hands to gather, and what they gathered does not stand between him and the loss that falls on those same hands. أغنى is a wealth word in its own root (الغنى في المال), so wealth is denied its own action: his wealth did not enrich him. تب also carries "cutting" and the curse-formula. The hands are struck off or cursed, and the second تَبَّ moves from wish to settled fact. Memory: when 26:214 came down, the Prophet called the clans from al-Ṣafā, and Abū Lahab answered "تبا لك سائر اليوم ألهذا جمعتنا" (Bukhārī). In some reports he also shook his hands at him. The surah returns his own word to his own hands. Also memory: Ibn Masʿūd's reading is "وقد تب", and the grammarians read the first تَبَّتْ as imprecation and وَتَبَّ as report.

- 111:1 تَبَّتْ — ت ب ب B001 — "تبت يداه تبا وتبابا أي خسرت" (jamhara). The dictionary's own phrase pairs تب with the hands. Ruin is a loss that settles on the hands.
- 111:1 تَبَّتْ — ت ب ب B001 — "التب الخسار وتبا لفلان على الدعاء" (tahdhib); "تبا للكافر أي هلاكا له" (maqayis). The verb is also a curse-formula. The opening sounds as an invocation of ruin.
- 111:1 وَتَبَّ — ت ب ب B001 — "التب والتباب الاستمرار في الخسران" (mufradat). The second تب makes the loss continuous and carries it from the hands to the person.
- 111:1 تَبَّتْ — ت ب ب B004 — "تب إذا قطع". Cutting: the hands are cut off.
- 111:1 يَدَآ — ي د ي B001 — "يديت الرجل إذا ضربت يده" (jamhara;sihah;tahdhib;mufradat); "رجل ميدي أي مقطوع اليد" (tahdhib). The hand as an organ that can be struck or cut off. This meets the cutting sense of تب.
- 111:1 يَدَآ — ي د ي B002 — "اليد القوة" (sihah); "ما لي به يدان أي قوة" (tahdhib;mufradat). The dual "two hands" means power. What is ruined is his capacity.
- 111:1 يَدَآ — ي د ي B004 [fixed expression] — "هذا الشيء في يدي أي في ملكي" (sihah). What is in the hand is what one owns. This leads straight to مَالُهُۥ.
- 111:1 يَدَآ — ي د ي B009 [fixed expression] — "ذلك بما كسبت يداك" (tahdhib); "هذا ما قدمت يداك أي جنيته أنت" (sihah). The dictionary joins يد and كسب: the hands are the agents of what one earns and answers for.
- 111:2 أَغْنَىٰ — غ ن ي B002 — "ما يغني عنك هذا أي ما يجزئ وما ينفع" (sihah); "أغناني كذا وأغنى عنه كذا إذا كفاه" (mufradat). The cover that wealth was expected to give fails.
- 111:2 أَغْنَىٰ — غ ن ي B001 — "الغنى في المال" (maqayis;tahdhib). The negated verb is itself the wealth word, so wealth denies its own function.
- 111:2 مَالُهُۥ — م و ل B001 — "تمول الرجل اتخذ مالا" (maqayis); "كانت أموال العرب أنعامهم" (ayn). Stored holdings, in the Arab case herds: what the hands took and kept.
- 111:2 كَسَبَ — ك س ب B001 — "الكسب طلب الرزق" (ayn;sihah;tahdhib); "الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال" (mufradat). Earning is the active pursuit and drawing-in of gain.
- 111:2 كَسَبَ — ك س ب B003 — "الكواسب الجوارح" (sihah). The earners are the limbs. The earning of 111:2 returns to the hands of 111:1 and closes the circle.

Quran:
- 2:79 — God, of those who write the book with their own hands and sell it for a small price. "فَوَيْلٌۭ لَّهُم مِّمَّا كَتَبَتْ أَيْدِيهِمْ وَوَيْلٌۭ لَّهُم مِّمَّا يَكْسِبُونَ": hands and earning are cursed together.
- 30:41; 42:30 — "بِمَا كَسَبَتْ أَيْدِى ٱلنَّاسِ" / "فَبِمَا كَسَبَتْ أَيْدِيكُمْ": the dictionary's pairing of hand and earning, as Quranic wording.
- 22:10 (the scene opens at 22:8) — said on the Day to the one who disputes about God without knowledge: "ذَٰلِكَ بِمَا قَدَّمَتْ يَدَاكَ". Also 3:182.
- 78:40 — the warning of the Day: "يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ". The dual hands as what a man sends ahead.
- 69:28 (the scene opens at 69:25, the one given his book in his left hand) — "مَآ أَغْنَىٰ عَنِّى مَالِيَهْ": the same verb and the same noun, spoken by the loser himself.
- 92:11 (the scene opens at 92:8, the one who withheld and thought himself self-sufficient) — "وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ": the exact wording of 111:2.
- 15:84; 39:50; 40:82; 45:10 — destroyed or doomed peoples: "فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ". The pairing أغنى + كسب as a fixed Quranic sequence.
- 26:207 — "مَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يُمَتَّعُونَ".
- 11:101 — God, of destroyed towns: "فَمَآ أَغْنَتْ عَنْهُمْ ءَالِهَتُهُمُ ... وَمَا زَادُوهُمْ غَيْرَ تَتْبِيبٍۢ". أغنى and تب in one ayah. The dictionary (maqayis;tahdhib;mufradat) quotes this phrase: "وما زادوهم غير تتبيب أي تخسير".
- 40:37 (the scene opens at 40:36, Pharaoh ordering the tower) — "وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ": a powerful man's scheme ends in تباب.
- 104:2–3 — the slanderer "ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ": the expectation that 111:2 denies.
- 5:64 — God answering those who said God's hand is fettered: "غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟": an imprecation laid on hands, the same grammar as تَبَّتْ يَدَآ.
- 25:27 — "يَوْمَ يَعَضُّ ٱلظَّالِمُ عَلَىٰ يَدَيْهِ": the wrongdoer's hands at the end, in regret.

### 2. Father of Flame: the name becomes the fire

111:1 names the man by a kunya made of flame, أَبِى لَهَبٍۢ. 111:3 gives the same word back as the property of the fire he will enter: نَارًۭا ذَاتَ لَهَبٍۢ. He is "father of flame" and the fire is "possessor of flame" (the text's own ذَاتَ). The name and the fire's attribute share one word, so his kunya turns out to describe his end. The dictionary gives أب as "cause and originator" and as "the one who feeds". The father of flame is the one who brings flame into being and nourishes it. لهب also names striking beauty and intense brightness. Memory: Ibn Kathīr and others say he was given the kunya for the brightness and ruddiness of his face. The root of نار names light and fire together, so the brightness that named him turns into the burning that receives him. نار also means a brand on a camel, and the proverb "نجارها نارها" reads a beast's stock off its fire-mark. His identity is likewise read off a fire-name.

- 111:1 أَبِى — ء ب و B001 — "الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا" (mufradat). The father of a thing is whatever brings it into being: father of flame, cause of flame.
- 111:1 أَبِى — ء ب و B001 — "أبوت الشيء آبوه أبوا إذا غذوته" (maqayis); "يدل على التربية والغذو" (maqayis). To father is to feed. The father of flame feeds the flame, which meets the fuel of 111:4.
- 111:1 لَهَبٍۢ — ل ه ب B006 — "كني أبو لهب به" (sihah); "تبت يدا أبي لهب" (mufradat). The dictionary quotes the surah's own phrase under the naming sense.
- 111:1 لَهَبٍۢ — ل ه ب B008 — "الملهب الرائع الجمال" (tahdhib). Flame as striking beauty, the sense memory links to the kunya.
- 111:1 / 111:3 لَهَبٍۢ — ل ه ب B003 — "كل شيء ارتفع ضوؤه ولمع لمعانا شديدا" (maqayis). Rising, intense brightness: the bridge between the radiant name and the actual blaze.
- 111:3 لَهَبٍۢ — ل ه ب B001 — "ارتفاع لسان النار" (maqayis). In 111:3 the same word is a literal tongue of fire rising.
- 111:3 نَارًۭا — ن و ر B001 — "النور والنار سميا بذلك من طريقة الإضاءة" (maqayis). Light and fire share one root. The brightness of the name and the fire of the end are one shining.
- 111:3 نَارًۭا — ن و ر B002 — "ما نار هذه الناقة أي ما سمتها؛ نجارها نارها" (sihah). Fire as a brand: stock and identity read off a fire-mark.

Quran:
- 85:5 — the companions of the trench: "ٱلنَّارِ ذَاتِ ٱلْوَقُودِ". The same construction, ذات + the fire's own matter, as نَارًۭا ذَاتَ لَهَبٍۢ.
- 77:30–31 — the deniers sent on the Day to a shadow of three branches: "لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ". The word اللهب and the verb أغنى in one ayah: nothing covers from the flame, as nothing covered him in 111:2.
- 9:35 (the scene opens at 9:34, those who hoard gold and silver) — "يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ": hoarded wealth heated in the fire and pressed on as a brand.

### 3. Fuel, kindling, and the one who is roasted

The fire of 111:3 is staged as a whole working fire: wood gathered and carried on a back (111:4), fuel that kindles, a flame burning clear of smoke, and a man who enters it, clings to it and suffers its heat and thirst. يصلى in its own root names the fuel (الصلاء) and the roast (الشواء). So the verb of 111:3 already contains the firewood of 111:4, and the man is set where meat is set. The dictionary even calls a wasted man حطب, likening a person to dry firewood. People are fuel in the Quranic fire. The wood the wife carries and the man who burns belong to one fire.

- 111:4 ٱلْحَطَبِ — ح ط ب B001 — "ما يعد للإيقاد" (mufradat); "حطبت واحتطبت إذا جمعته" (sihah). Wood readied for kindling, gathered.
- 111:4 حَمَّالَةَ — ح م ل B001 — "حملت الشئ على ظهرى أحمله حملا" (sihah). The load carried on the back. The form حَمَّالَةَ (text) makes it a habitual, heavy carrying.
- 111:4 ٱلْحَطَبِ — ح ط ب B004 — "الحطب الرجل الشديد الهزال والأحطب مثله" (sihah); "كأنه شبه بالحطب اليابس" (maqayis). A person called firewood: a human being as dry fuel.
- 111:3 سَيَصْلَىٰ — ص ل ي B004 — "الصلاء ما يصطلى به وما يذكى به النار ويوقد" (maqayis); "الصلاء يقال للوقود وللشواء" (mufradat). The verb's root is fuel and roast.
- 111:3 سَيَصْلَىٰ — ص ل ي B004 — "صليت اللحم صليا شويته" (ayn;sihah;tahdhib). Roasting meat over fire.
- 111:3 سَيَصْلَىٰ — ص ل ي B003 — "صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها" (ayn). The dictionary phrase is the surah's own construction, صلى + نارا. He undergoes its heat and force.
- 111:3 سَيَصْلَىٰ — ص ل ي B003 — "من يصلى في النار أي يلزم النار" (tahdhib); "صلي الرجل نارا إذا أدخلته النار" (sihah). Entering and staying.
- 111:3 نَارًۭا — ن و ر B002 — "النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة" (maqayis). Fire as restless, fast movement.
- 111:3 لَهَبٍۢ — ل ه ب B001 — "اشتعال النار الذي قد خلص من الدخان" (ayn;tahdhib); "التهبت النار وتلهبت وألهبتها" (sihah). Flame at full kindling, past the smoke.
- 111:3 لَهَبٍۢ — ل ه ب B002 — "يستعمل اللهاب في النار والعطش جميعا" (jamhara); "اللهاب في الحر الذي ينال العطشان" (mufradat). The dictionary names fire and thirst with one word: the one inside the flame thirsts.

Quran:
- 72:15 — the jinn speaking: "وَأَمَّا ٱلْقَٰسِطُونَ فَكَانُوا۟ لِجَهَنَّمَ حَطَبًۭا": people as حطب of Jahannam, the surah's own word.
- 21:98 — to the idolaters and their objects of worship: "حَصَبُ جَهَنَّمَ".
- 2:24; 66:6 — "وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ". 3:10 — "وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ", directly after wealth and children failing to avail.
- 88:4 — "تَصْلَىٰ نَارًا حَامِيَةًۭ"; 87:12 — "ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ"; 92:14–15 — "نَارًۭا تَلَظَّىٰ لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى"; 58:8 — "حَسْبُهُمْ جَهَنَّمُ يَصْلَوْنَهَا": the construction صلى + fire.
- 74:26 (the scene opens at 74:11, God about the man given extended wealth and present sons; memory: al-Walīd b. al-Mughīra) — "سَأُصْلِيهِ سَقَرَ": the same سـ future with صلى, after wealth (74:12) and sons (74:13).
- 69:30–31 (the scene opens at 69:25) — "خُذُوهُ فَغُلُّوهُ ثُمَّ ٱلْجَحِيمَ صَلُّوهُ": a neck-shackle, then the roasting.
- 104:6 — "نَارُ ٱللَّهِ ٱلْمُوقَدَةُ": a fire kindled, for the gatherer of wealth.
- 36:80 — God: "ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ": wood as the source of kindled fire.
- 77:32 — "إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ": the fire's throw.

### 4. The household hearth turned inside out

A household runs on a man who earns for his people, a wife, a feast at marriage or house-building, wood gathered for the house, and a hearth where meat is roasted and people warm themselves. The surah's words carry every piece of that domestic scene. كسب names earning good for one's household, أب names the feeder, امرأة names the wife and the feast, غنى names marriage and the wife whom her husband suffices, حطب names gathering wood for someone, and صلى names roasting and warming at a fire. In the surah all of it is reversed. The earner's earning does not suffice even him, the wife gathers wood for the fire he roasts in, and the hearth becomes the Fire.

- 111:2 كَسَبَ — ك س ب B002 — "فلان يكسب أهله خيرا" (tahdhib); "كسبت الرجل مالا فكسبه" (maqayis;jamhara;sihah). Earning good for one's household.
- 111:1 أَبِى — ء ب و B001 — "فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده" (ayn;tahdhib). The father as the one who feeds.
- 111:4 وَٱمْرَأَتُهُۥ — م ر ء (root_001410) B001 — "يقال : هي امرأته ، وهي مرأته ، وهي مرته" (tahdhib). His wife, the partner in the household.
- 111:4 وَٱمْرَأَتُهُۥ — م ر ء (root_001410) B004 — "والمرء : الإطعام على بناء دار ، أو تزويج" (tahdhib); "ما لك لا تمرأ ؟ أي ما لك لا تطعم ؟" (tahdhib). The feast given at building a house or at a marriage: the founding of a household.
- 111:2 أَغْنَىٰ — غ ن ي B006 — "الغنى التزويج" (tahdhib); "الأغناء إملاكات العرائس" (tahdhib). The same root names marriage.
- 111:2 أَغْنَىٰ — غ ن ي B005 — "الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين" (mufradat). The wife whom her husband suffices. In the surah the husband cannot suffice even himself.
- 111:4 ٱلْحَطَبِ — ح ط ب B001 — "حطبت فلانا إذا احتطبت له" (tahdhib). Gathering wood for someone, here for him.
- 111:3 سَيَصْلَىٰ — ص ل ي B004 — "الصلاء ما يصطلى به وما يذكى به النار ويوقد" (maqayis); "صليت اللحم صليا شويته" (ayn;sihah;tahdhib). The hearth: warming and roasting.

Quran:
- 20:10; 27:7; 28:29 — Mūsā to his family on the road, seeing a fire: "لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ" / "لَّعَلَّكُمْ تَصْطَلُونَ". A husband fetching fire to warm his household, with the hearth sense of صلى. It is the positive counterpart of this couple.
- 66:6 — to the believers: "قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ": a man answerable for his household before a fire whose fuel is people.
- 84:12–13 (the scene opens at 84:10, the one given his book behind his back) — "وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا": roasting set against his former ease among his household.
- 66:10 — God's example for those who disbelieve, the wives of Nūḥ and Lūṭ: "فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ". امرأة, أغنى and the Fire together: there spouses do not avail across the marriage.
- 66:11 — Pharaoh's wife, saved from her husband and his deeds: a reversal of the shared fate of this couple.
- 37:22 — "ٱحْشُرُوا۟ ٱلَّذِينَ ظَلَمُوا۟ وَأَزْوَٰجَهُمْ": wrongdoers gathered with their spouses.
- 70:11–12 — the criminal on the Day would ransom himself "بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ".

### 5. What he earned and what she bears: offspring

حَمَّالَةَ (111:4) and حَبْلٌۭ (111:5) are both, in their roots, words for pregnancy. The dictionary itself defines one by the other. Read with أَبِى (111:1), وَٱمْرَأَتُهُۥ (111:4) and كَسَبَ (111:2), these words make a scene of lineage. The wife who would carry his line carries wood and wears a rope. Memory: Ibn ʿAbbās and others read وَمَا كَسَبَ as his children, citing the hadith "إن أطيب ما أكلتم من كسبكم وإن أولادكم من كسبكم". Also memory: his sons ʿUtba and ʿUtayba divorced the Prophet's daughters Ruqayya and Umm Kulthūm at their parents' command. "His wealth and what he earned", meaning wealth and children, is the Quranic pair that does not avail.

- 111:2 كَسَبَ — ك س ب B001 — "كسبت الشيء واكتسبته" (jamhara;sihah). What one acquires. Memory: in the tafsir, his children.
- 111:4 حَمَّالَةَ — ح م ل B002 — "الحمل ما كان في بطن أو على رأس شجر" (maqayis;sihah); "حملت المرأة حبلت وكذا حملت الشجرة" (mufradat). Bearing as pregnancy. Mufradat glosses حمل with حبل.
- 111:5 حَبْلٌۭ — ح ب ل B006 — "الحبل الحمل وقد حبلت المرأة فهي حبلى" (sihah); "الحبل وهو الحمل وذلك أن الأيام تمتد به" (maqayis). The dictionary joins the two surah words حبل and حمل in one phrase.
- 111:1 أَبِى — ء ب و B001 — "الأب الوالد" (mufradat). Fatherhood.
- 111:4 وَٱمْرَأَتُهُۥ — م ر ء B001 — "وامرأة تأنيث امرىء" (maqayis;ayn). The woman, his wife.

Quran:
- 71:21 — Nūḥ complaining of the chiefs: "مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا". Wealth and child producing only loss, and خسار is the dictionary's gloss of تباب.
- 3:10; 58:17 — "لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا", followed by "وَقُودُ ٱلنَّارِ" / "أَصْحَٰبُ ٱلنَّارِ". This is the sequence of 111:2–3 in one ayah.
- 26:88 — "يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ"; 34:37; 63:9.
- 68:14 — the slanderer of 68:10–11 is followed by "أَن كَانَ ذَا مَالٍۢ وَبَنِينَ".
- 74:12–13 (the scene opens at 74:11) — "مَالًۭا مَّمْدُودًۭا وَبَنِينَ شُهُودًۭا", before "سَأُصْلِيهِ سَقَرَ" (74:26).

### 6. Carrier of firewood, carrier of slander: the fire between people

The dictionary records حَمَّالَةَ ٱلْحَطَبِ itself as a figure for slander. حطب as a verb means to talk against someone. Carrying the message, carrying the load, and carrying tales are one act of bearing. The wood is carried to where it will burn. The slanderous talk is carried between people and kindles enmity, which the dictionary names with the fire root itself (نائرة). In the surah the fire she fed between people meets the fire of 111:3. The night wood-gatherer is a fixed figure for one who mixes and over-talks. Memory: Mujāhid and Qatāda say she walked with namīma. Memory also has her mocking verse "مذمما عصينا".

- 111:4 حَمَّالَةَ ٱلْحَطَبِ — ح ط ب B003 — "حمالة الحطب كناية عن النميمة" (maqayis;tahdhib;mufradat); "الحطب في القرآن النميمة" (ayn). The dictionary's phrase is the surah's phrase.
- 111:4 ٱلْحَطَبِ — ح ط ب B003 — "حطب فلان بفلان سعى به" (maqayis;ayn;tahdhib;mufradat); "يوقد بالحطب الجزل كناية عن ذلك" (mufradat). Telling against someone; feeding the fire with heavy wood.
- 111:4 حَمَّالَةَ — ح م ل B001 — "حملت الثقل والرسالة والوزر حملا" (mufradat). One verb for carrying a load and carrying a message.
- 111:4 ٱلْحَطَبِ — ح ط ب B002 [fixed expression] — "يقال للمخلط في كلامه حاطب ليل" (maqayis;ayn;sihah;tahdhib;mufradat). Speech as wood gathered blind at night.
- 111:3 نَارًۭا — ن و ر B007 — "بينهم نائرة أي عداوة وشحناء" (sihah); "النائرة الكائنة تقع بين القوم" (ayn). Enmity between people named by the fire root.
- 111:3 لَهَبٍۢ — ل ه ب B001 — "التهبت النار وتلهبت وألهبتها" (sihah). Kindling: the carried fuel set alight.

Quran:
- 68:10–11 — God to the Prophet: "وَلَا تُطِعْ كُلَّ حَلَّافٍۢ مَّهِينٍ هَمَّازٍۢ مَّشَّآءٍۭ بِنَمِيمٍۢ". The tale-carrier, followed by "ذَا مَالٍۢ وَبَنِينَ" (68:14).
- 104:1–9 — "وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ": the slanderer who gathered wealth, cast into the crusher, "نَارُ ٱللَّهِ ٱلْمُوقَدَةُ" closed over them "فِى عَمَدٍۢ مُّمَدَّدَةٍۭ". Slander, wealth and kindled fire staged together.
- 5:64 — "وَأَلْقَيْنَا بَيْنَهُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ ... كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ": enmity as a fire kindled between people.
- 4:112 — "وَمَن يَكْسِبْ خَطِيٓـَٔةً أَوْ إِثْمًۭا ثُمَّ يَرْمِ بِهِۦ بَرِيٓـًۭٔا فَقَدِ ٱحْتَمَلَ بُهْتَٰنًۭا": earning a wrong, throwing it on another, and so carrying slander. كسب and حمل meet in one ayah.

### 7. The load on the back: pack-bearer, halter, burden

حَمَّالَةَ is an intensive carrying form. With ٱلْحَطَبِ on her back and a حَبْلٌۭ of مَّسَدٍۭ at her neck, the dictionary's own senses build a pack-beast scene. حمولة is the camels that carry loads. حبل is the halter. مسد is rope of palm fibre or camel hair. A she-camel that browses dry thorn is named from حطب. A donkey or camel with a galled back is named from the ruin root تب. The load is also the sin-load: the dictionary quotes the Quran's "وساء لهم يوم القيامة حملا أي وزرا". The bearer strains under it.

- 111:4 حَمَّالَةَ — ح م ل B001 — "حملت الشئ على ظهرى أحمله حملا" (sihah). The load on the back.
- 111:4 حَمَّالَةَ — ح م ل B006 — "الحمولة الإبل تحمل عليها الأثقال" (maqayis;ayn). The pack camels: the carrier as beast of burden.
- 111:4 حَمَّالَةَ — ح م ل B003 [fixed expression] — "من باء بالإثم يسمى حاملا للإثم" (tahdhib); "وساء لهم يوم القيامة حملا أي وزرا" (sihah). The carried load as sin.
- 111:4 حَمَّالَةَ — ح م ل B007 — "تحاملت إذا تكلفت الشيء على مشقة" (maqayis). Carrying under strain.
- 111:4 ٱلْحَطَبِ — ح ط ب B001 — "ناقة محاطبة تأكل الشوك اليابس" (maqayis;sihah). A she-camel named from حطب, feeding on dry thorn.
- 111:5 حَبْلٌۭ — ح ب ل B001 — "الحبل الرسن" (ayn;tahdhib). The halter: a rope at the neck that leads an animal.
- 111:5 مَّسَدٍۭ — م س د B001 — "المسد حبل يتخذ من أوبار الإبل" (maqayis;tahdhib); "حبل من ليف أو خوص وقد يكون من جلود الإبل أو من أوبارها" (sihah;tahdhib). The dictionary defines مسد as حبل: coarse working rope of palm fibre or camel hair.
- 111:1 تَبَّتْ — ت ب ب B003 — "حمار تاب الظهر إذا دبر وجمل تاب كذلك". The ruin root names a pack animal with a galled back.

Quran:
- 6:31 — the losers at the Hour: "وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ ۚ أَلَا سَآءَ مَا يَزِرُونَ". Also "قَدْ خَسِرَ", the gloss of تب.
- 20:100–101 — "فَإِنَّهُۥ يَحْمِلُ يَوْمَ ٱلْقِيَٰمَةِ وِزْرًا ... وَسَآءَ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ حِمْلًۭا". Sihah cites this.
- 35:18 — "وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ". The burden that kin cannot share; a feminine bearer (مُثْقَلَةٌ).
- 20:87 — the Israelites: "حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ". Loads made of ornaments, which meets the necklace in chain 8.

### 8. The rope at the neck: from necklace to fibre collar to shackle

111:5 sets a rope on the جِيد, the front of the neck, the part praised as long and beautiful and the place of the necklace. The rope root itself names a necklace ornament (حبلة), so the ornament word appears as coarse rope. مسد names well-twisted rope. It also names a woman's firm, well-knit build, so the woman and the rope share the word. It further names an axle "if it is of iron". Memory: Mujāhid and ʿUrwa say the masad in the Fire is "سلسلة من حديد ذرعها سبعون ذراعا" or "طوق من حديد". Also memory: Ibn Kathīr reports from Saʿīd b. al-Musayyab that she had a precious necklace and swore "لأنفقنها في عداوة محمد". The neck that wore it receives a rope instead. غانية is the woman whom husband or beauty spares adornment, and here the adornment is reversed. The bound one cannot flee (حبيل براح), and the rope sits over the neck's own cord, حبل الوريد.

- 111:5 جِيدِهَا — ج ي د B001 — "الجيد مقدم العنق" (ayn); "رجل أجيد وامرأة جيداء حسنة الجيد إذا كانت طويلة العنق" (jamhara); "امرأة جيدانة حسنة الجيد" (ayn). The front of the neck, a word of beauty and display.
- 111:5 حَبْلٌۭ — ح ب ل B008 — "الحبلة حلي يجعل في القلائد ولعله مشبه بثمره" (maqayis); "الحبلة حلي كان يجعل في القلائد في الجاهلية وقلائد من حبلة وسلوس" (tahdhib). The rope root names the necklace ornament.
- 111:5 حَبْلٌۭ — ح ب ل B001 — "الحبل الرسن" (ayn;tahdhib). The rope as halter at the neck.
- 111:5 مَّسَدٍۭ — م س د B001 — "مسدت الحبل أي أجدت فتله" (sihah;tahdhib); "أصل صحيح يدل على جدل شيء وطية" (maqayis). Tightly twisted rope.
- 111:5 مَّسَدٍۭ — م س د B002 — "امرأة ممسودة مجدولة الخلق كالحبل الممسود" (maqayis;mufradat). A woman's firm body called by the rope word: the woman and her rope are one word.
- 111:5 مَّسَدٍۭ — م س د B005 — "المسد المحور إذا كان من حديد" (ayn). مسد as iron, which meets the remembered tafsir of an iron chain.
- 111:2 أَغْنَىٰ — غ ن ي B005 — "الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين" (mufradat); "الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة" (ayn). The woman spared adornment by husband or beauty. Her neck now carries a rope.
- 111:5 حَبْلٌۭ — ح ب ل B012 — "للواقف مكانه لا يفر حبيل براح كأنه محبول" (maqayis); "يقال للموت حبيل براح" (tahdhib). The roped one held in place, unable to flee; also a name for death.
- 111:5 حَبْلٌۭ — ح ب ل B004 — "حبل الوريد عرق في العنق" (sihah). The neck's own cord beneath the rope.

Quran:
- 3:180 — the misers: "سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ": withheld wealth turned into a collar, with the same سـ future as سَيَصْلَىٰ.
- 17:29 — God's instruction: "وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ": hand bound to neck, joining 111:1 and 111:5.
- 13:5; 34:33; 36:8 — "ٱلْأَغْلَٰلُ فِىٓ أَعْنَاقِهِمْ" / "فِىٓ أَعْنَٰقِهِمْ أَغْلَٰلًۭا فَهِىَ إِلَى ٱلْأَذْقَانِ".
- 40:71 — "إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ": collar and chain, the condemned dragged.
- 69:30–32 (the scene opens at 69:25) — "خُذُوهُ فَغُلُّوهُ ثُمَّ ٱلْجَحِيمَ صَلُّوهُ ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ": the seventy-cubit chain of the remembered tafsir, together with صلى.
- 76:4 — "سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا".
- 17:13 — "وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ": one's lot fastened to one's neck.
- 50:16 — "وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ": the neck's own cord, named with حبل.
- 89:26 — "وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ".

### 9. Snare, thorn and night: the trap-setter caught

The rope root names the hunter's snare and the "snares of death". Mufradat says "النساء حبائل الشيطان", joining woman and snare. The verb of 111:3 names, in its root, the trap set for birds and game (مصلاة). The dictionary explains a disaster (حِبل) as being caught in the snare. حطب names a she-camel browsing dry thorn, so thorn belongs to حطب. Memory: Ibn ʿAbbās and others say she strewed thorns at night on the Prophet's path. مسد names travelling hard through the night, and the night wood-gatherer is a fixed figure. One idiom of تب gives the clear, straight road. Together these make a night scene: thorn and snare laid on a path, and the one who laid them ends with a cord round her own neck. (Under the echo root ص ل و, which the dictionary marks as withheld and not an identity of سَيَصْلَىٰ, it records "صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة". I note it here and do not use it as a member.)

- 111:5 حَبْلٌۭ — ح ب ل B005 — "الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه" (ayn); "المحبول الوحشي الذي نشب في الحبالة" (sihah). The snare and the caught animal.
- 111:5 حَبْلٌۭ — ح ب ل B005 — "الحبالة خصت بحبل الصائد والنساء حبائل الشيطان" (mufradat). Woman and snare joined in one phrase.
- 111:5 حَبْلٌۭ — ح ب ل B011 — "الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة" (maqayis). Calamity as being caught in the snare.
- 111:3 سَيَصْلَىٰ — ص ل ي B005 — "المصلاة أن تنصب شركا ونحوه" (ayn); "مصالي هي الأشراك واحدتها مصلاة" (maqayis). A trap is set. The verb of the end belongs to the root of the trap.
- 111:1 تَبَّتْ — ت ب ب B001 — "تببوهم تتبيبا أي أهلكوهم" (sihah). Destruction done to someone.
- 111:4 ٱلْحَطَبِ — ح ط ب B001 — "ناقة محاطبة تأكل الشوك اليابس" (maqayis;sihah). Dry thorn under حطب.
- 111:4 ٱلْحَطَبِ — ح ط ب B002 [fixed expression] — "يقال للمخلط في كلامه حاطب ليل". The night gatherer.
- 111:5 مَّسَدٍۭ — م س د B003 — "المسد إدآب السير في الليل" (ayn;sihah;tahdhib); "يكابد الليل عليها مسدا" (ayn;tahdhib). Hard going through the night.
- 111:1 تَبَّتْ — ت ب ب B002 [fixed expression] — "الطريق المستتب الواضح البين المستقيم" (tahdhib). The clear, straight road.

Quran:
- 35:43 — "وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِۦ": the evil plot closes on its own makers.
- 34:33 — the weak to the arrogant: "بَلْ مَكْرُ ٱلَّيْلِ وَٱلنَّهَارِ", then "وَجَعَلْنَا ٱلْأَغْلَٰلَ فِىٓ أَعْنَاقِ ٱلَّذِينَ كَفَرُوا۟". Night plotting followed by collars on necks.

### 10. Bond, protection and their cutting: hand and rope

حبل is also covenant, safe-conduct and connection, and يد is also patron and protector and the pledged hand. تب also means "to cut". In the surah the first word cuts and ruins the hands, and the last word is a rope. The hand that should protect and the rope that should bind in trust are present only as the ruined hand and the collar. Memory: Abū Lahab was the Prophet's paternal uncle. After Abū Ṭālib's death he briefly gave the Prophet protection (jiwār) and then withdrew it (Ibn Saʿd and Ibn Isḥāq, from memory). Sihah compares the rope-covenant to jiwār. مسد is twisting, which is what gives a cord its strength. The Quran sets the rope of God against the pit of fire in one ayah.

- 111:5 حَبْلٌۭ — ح ب ل B002 — "الحبل العهد والأمان والحبل التواصل" (ayn); "الحبل العهد والأمان وهو مثل الجوار والحبل الوصال" (sihah); "استعير للوصل ولكل ما يتوصل به إلى شيء" (mufradat). Rope as covenant, protection and kinship-connection.
- 111:1 يَدَآ — ي د ي B016 [fixed expression] — "فلان يد فلان أي وليه وناصره" (mufradat); "اليد الغياث واليد منع الظلم" (tahdhib). The hand as protector and patron.
- 111:1 يَدَآ — ي د ي B006 — "هذه يدي لك" (tahdhib); "خلع فلان يده عن الطاعة" (tahdhib). The hand pledged, and the hand withdrawn.
- 111:1 تَبَّتْ — ت ب ب B004 — "تب إذا قطع". Cutting: the bond is severed.
- 111:5 مَّسَدٍۭ — م س د B001 — "مسدت الحبل أي أجدت فتله" (sihah;tahdhib). Twisting gives the cord its strength. Here the strength is put to binding a neck.

Quran:
- 3:103 — "وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا ... وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا": the rope as rescue from the fire. It is the inverse of 111:3–5.
- 3:112 — "إِلَّا بِحَبْلٍۢ مِّنَ ٱللَّهِ وَحَبْلٍۢ مِّنَ ٱلنَّاسِ": rope as protection.
- 16:92 — "وَلَا تَكُونُوا۟ كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًۭا تَتَّخِذُونَ أَيْمَٰنَكُمْ دَخَلًۢا بَيْنَكُمْ": a woman who undoes her twisted yarn, used as a figure for broken oaths.
- 2:27; 13:25 — "وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ": cutting what should be joined. 2:27 ends "أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ", the gloss of تب.
- 47:22 — "وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ": cutting kinship.
- 26:214 — "وَأَنذِرْ عَشِيرَتَكَ ٱلْأَقْرَبِينَ". Memory: the occasion of the surah. The warning to the nearest kin, answered by the uncle's curse.
- 35:18 — "وَلَوْ كَانَ ذَا قُرْبَىٰٓ": kinship does not carry another's load.

## Interactions

- Chains 1 and 2 meet at 111:1 أَبِى لَهَبٍۢ, where the ruined hands belong to the man named by flame. Mufradat files "تبت يدا أبي لهب" under the لهب naming sense.
- Chains 1 and 3 meet at أغنى and the Fire. 77:31 "وَلَا يُغْنِى مِنَ ٱللَّهَبِ" and 3:10 "لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ ... وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ" stage wealth failing to cover and then the fire, the sequence of 111:2–3.
- Chains 1 and 8 meet where hand and wealth become neck-bonds. 17:29 binds the hand to the neck. 3:180 turns withheld wealth into a collar (سَيُطَوَّقُونَ).
- Chains 1 and 5 meet at كَسَبَ. Earned gain is read (memory) as children, and 3:10, 58:17 and 71:21 pair wealth and children.
- Chains 1 and 7 meet at كسب and حمل. 4:112 "يَكْسِبْ ... فَقَدِ ٱحْتَمَلَ" makes what one earns what one carries. Sihah's "وساء لهم يوم القيامة حملا أي وزرا" gives the carried load as sin.
- Chains 1 and 10 meet at تب B004 "تب إذا قطع" (cut hand, cut bond) and at يد B006/B016 (the protecting and pledged hand).
- Chains 2 and 3 meet at لهب. The same word is the name (111:1) and the fire's attribute (111:3). أب "أبوت الشيء آبوه أبوا إذا غذوته" makes the father of flame its feeder, meeting حطب "ما يعد للإيقاد".
- Chains 3 and 4 meet at ص ل ي B004 "الصلاء ما يصطلى به وما يذكى به النار ويوقد". One root gives both hearth and Fire. 28:29 and 27:7 "لَعَلَّكُمْ تَصْطَلُونَ" against 111:3 سَيَصْلَىٰ.
- Chains 3 and 6 meet at حطب: the wood for the fire and the wood of slander. Mufradat "يوقد بالحطب الجزل كناية عن ذلك", and نائرة (enmity) under the fire root. 104:1–6 stages slander, wealth and kindled fire. 5:64 stages enmity as kindled fire.
- Chains 3 and 8 meet in 69:30–31, which stages the shackle and صلى together. مسد "المسد المحور إذا كان من حديد" meets the remembered iron chain of the Fire.
- Chains 4 and 5 meet at وَٱمْرَأَتُهُۥ: the wife as partner in the household and as bearer of his line. حمل and حبل are pregnancy words in both of her ayat.
- Chains 4 and 8 meet at غ ن ي B005 "الغانية المستغنية بزوجها عن الزينة". The husband who should suffice her (and who did not suffice himself, 111:2) and the neck that should need no ornament both appear reversed. 66:10 "فَلَمْ يُغْنِيَا عَنْهُمَا" with امرأة and the Fire.
- Chains 6 and 9 meet at حاطب ليل. The night gatherer is both the mixer of speech and the night worker laying thorn.
- Chains 7 and 8 meet at حَبْلٌۭ. The halter "الحبل الرسن" is the pack-beast's neck-rope, and the dictionary defines مسد as "حبل يتخذ من أوبار الإبل". 20:87 joins carried loads and ornaments.
- Chains 8 and 9 meet at حَبْلٌۭ: the rope at the neck is both collar and snare. 34:33 stages night plotting and then collars on necks. 35:43 has the plot closing on its makers.
- Chains 8 and 10 meet at حَبْلٌۭ: the rope of covenant versus the rope of the collar. 3:103 sets the rope of God against the brink of the fire.
- Chains 9 and 3 meet at ص ل ي. In one root the trap (مصلاة) and the roasting (صلى نارا) belong to the verb of 111:3.

## Ayat

### 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- Chain 1: تَبَّتْ lays loss, a curse and cutting on يَدَآ, the dual hands of power, possession and earning. وَتَبَّ makes the loss lasting and total. Across the surah: the hands that gathered (111:1) hold wealth and earnings that do not cover him (111:2), and the ruin they earned stays.
- Chain 2: أَبِى gives cause and feeder; لَهَبٍۢ gives the kunya, radiance and beauty. Across the surah: the man named "father of flame" (111:1) enters a fire "possessor of flame" (111:3), and his name describes his end.
- Chain 3: لَهَبٍۢ brings the flame in early through the name. Across the surah: wood gathered and carried on a back (111:4) feeds a fire that the flame-named man enters, roasts in and thirsts in (111:3).
- Chain 4: أَبِى as the one who feeds. Across the surah: a household of earner, wife, wood and hearth (111:1–4) turns into the Fire, where he roasts and she brings the wood.
- Chain 5: أَبِى as father. Across the surah: what he earned (memory: his children, 111:2) and the bearing and pregnancy words of his wife's ayat (111:4–5) make a lineage that carries wood and rope.
- Chain 7: تَبَّتْ also names a pack animal with a galled back. Across the surah: the wife bears a load on her back with a halter-rope of palm fibre at her neck (111:4–5), and the load is also the sin-load.
- Chain 9: تَبَّتْ gives destruction done to someone and the idiom of the clear, straight road. Across the surah: thorn and snare laid by night (111:4–5) end in a cord at the setter's own neck (111:5) and a trap-root fire (111:3).
- Chain 10: يَدَآ as protecting and pledged hand; تَبَّتْ as cutting. Across the surah: the uncle's protecting hand is cut and ruined (111:1), and the only rope left is a collar (111:5) beside the fire (111:3).

### 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- Chain 1: أَغْنَىٰ is a wealth word that is negated. مَالُهُۥ is stored holdings and herds. كَسَبَ is earning, and its root names the limbs (الكواسب الجوارح), which brings back the hands of 111:1. Across the surah: the hands that gathered (111:1) hold wealth and earnings that do not cover him (111:2), and the ruin they earned stays.
- Chain 4: كَسَبَ as earning good for one's household; أَغْنَىٰ as marriage (الغنى التزويج) and the wife whom her husband suffices. Across the surah: a household of earner, wife, wood and hearth (111:1–4) turns into the Fire, where he roasts and she brings the wood.
- Chain 5: كَسَبَ as what he acquired (memory: his children). Across the surah: what he earned (111:2) and the bearing and pregnancy words of his wife's ayat (111:4–5) make a lineage that carries wood and rope.
- Chain 7: كَسَبَ as what one comes to carry (4:112). Across the surah: the wife bears a load on her back with a halter-rope of palm fibre at her neck (111:4–5), and the load is also the sin-load.
- Chain 8: أَغْنَىٰ through الغانية, the woman spared adornment. Across the surah: the beautiful neck of the necklace (111:5) carries a twisted fibre rope, which memory makes an iron chain.

### 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- Chain 2: لَهَبٍۢ returns the kunya as the fire's attribute (ذَاتَ, text), and نَارًۭا shares a root with light. Across the surah: the man named "father of flame" (111:1) enters a fire "possessor of flame" (111:3), and his name describes his end.
- Chain 3: سَيَصْلَىٰ means entering, clinging, undergoing heat and being roasted, and its root names fuel. نَارًۭا is restless, quick fire. لَهَبٍۢ is flame clear of smoke and thirst. Across the surah: wood gathered and carried on a back (111:4) feeds a fire that the flame-named man enters, roasts in and thirsts in (111:3).
- Chain 4: سَيَصْلَىٰ as roasting meat and warming at the hearth. Across the surah: a household of earner, wife, wood and hearth (111:1–4) turns into the Fire, where he roasts and she brings the wood.
- Chain 6: نَارًۭا as نائرة, enmity between people; لَهَبٍۢ as kindling. Across the surah: the wife carries the wood of slander between people (111:4), and the enmity it kindles meets the fire of 111:3.
- Chain 9: سَيَصْلَىٰ through مصلاة, the set trap. Across the surah: thorn and snare laid by night (111:4–5) end in a cord at the setter's own neck (111:5) and a trap-root fire (111:3).

### 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- Chain 3: ٱلْحَطَبِ is wood readied for kindling, and also a person likened to dry wood. حَمَّالَةَ is a load carried on the back. Across the surah: wood gathered and carried on a back (111:4) feeds a fire that the flame-named man enters, roasts in and thirsts in (111:3).
- Chain 4: وَٱمْرَأَتُهُۥ as his wife and the marriage or house-building feast; ٱلْحَطَبِ as gathering wood for someone. Across the surah: a household of earner, wife, wood and hearth (111:1–4) turns into the Fire, where he roasts and she brings the wood.
- Chain 5: حَمَّالَةَ as pregnancy ("الحمل ما كان في بطن"); وَٱمْرَأَتُهُۥ as the wife. Across the surah: what he earned (111:2) and the bearing and pregnancy words of his wife's ayat (111:4–5) make a lineage that carries wood and rope.
- Chain 6: حَمَّالَةَ ٱلْحَطَبِ is the dictionary's own figure for slander. حمل also means carrying a message. حاطب ليل [fixed expression]. Across the surah: the wife carries the wood of slander between people (111:4), and the enmity it kindles meets the fire of 111:3.
- Chain 7: حَمَّالَةَ as pack-bearing, sin-bearing and strain; ٱلْحَطَبِ as the thorn-browsing she-camel. Across the surah: the wife bears a load on her back with a halter-rope of palm fibre at her neck (111:4–5), and the load is also the sin-load.
- Chain 9: ٱلْحَطَبِ as dry thorn and the night gatherer. Across the surah: thorn and snare laid by night (111:4–5) end in a cord at the setter's own neck (111:5) and a trap-root fire (111:3).

### 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ
- Chain 5: حَبْلٌۭ as pregnancy ("الحبل الحمل"). Across the surah: what he earned (111:2) and the bearing and pregnancy words of his wife's ayat (111:4–5) make a lineage that carries wood and rope.
- Chain 7: حَبْلٌۭ as halter; مَّسَدٍۭ as coarse rope of palm fibre or camel hair. Across the surah: the wife bears a load on her back with a halter-rope of palm fibre at her neck (111:4–5), and the load is also the sin-load.
- Chain 8: جِيدِهَا is the beautiful long neck. حَبْلٌۭ names the necklace ornament, the halter, the bound one who cannot flee, and the neck's own cord. مَّسَدٍۭ is twisted rope, a woman's firm build, and iron. Across the surah: the beautiful neck of the necklace (111:5) carries a twisted fibre rope, which memory makes an iron chain.
- Chain 9: حَبْلٌۭ as snare, "النساء حبائل الشيطان", and calamity as being snared; مَّسَدٍۭ as hard night travel. Across the surah: thorn and snare laid by night (111:4–5) end in a cord at the setter's own neck (111:5) and a trap-root fire (111:3).
- Chain 10: حَبْلٌۭ as covenant, protection and connection; مَّسَدٍۭ as the twisting that gives a cord strength. Across the surah: the uncle's protecting hand is cut and ruined (111:1), and the only rope left is a collar (111:5) beside the fire (111:3).

