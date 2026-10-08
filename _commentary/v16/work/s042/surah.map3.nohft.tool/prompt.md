Surah: 42. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S42 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), an earlier reader's channel review (channels.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not delegate, browse or inspect files; run only the command the header describes.

The channel review is an earlier reader's proposal. Ignore its judgements: grades,
strength or confidence labels, reading types, words such as "surprising", "exploratory" or "latent", and every
statement of what a reading may or may not do. Make your own judgement from the surah's words, the dictionary
phrases and the Quran. Do not rediscover what it already assembled: start from its chains, test each one
against the dictionary phrases and the text, and join, extend, split or correct them. Where its wording
abstracts a member, go back to the dictionary phrase and name what it actually says.

A chain belongs on the map when its members are senses the dictionary attests for words that stand in the surah,
and together they make one image or process that the surah's wording or sequence lets a listener hear. A member
need not be the sense that translates its word in its own ayah; a chain is heard across the surah, not in one
word. A chain may join a sense and its reversal as well as the parts of one scene. Mark a member attested only
inside a fixed expression [fixed expression]; add no other label to a member or a chain, and where a source
records a phrase and rejects it, say so of that phrase alone. When the dictionary itself joins two of the
surah's words in one phrase, quote that phrase: it is the strongest evidence a chain can have. Keep a scene at
the level of its objects, their parts and their operation. When proposals share members, do not fold one into
another's more abstract function unless nothing concrete is lost. Carry every chain that meets this test,
however unusual; leave out proposals that do not.

Write the map in English, with Arabic quoted exactly (surah wording from the text, dictionary phrases from the
dictionary). It is working material for the writer, not commentary prose.

1. `## Chains`. For each chain, a `###` heading naming the image. One paragraph on what the image is and how it
   moves through the surah. Then its members, one line each: the ayah ref, the word as it stands in the text,
   the root and branch id, the dictionary's own phrase quoted exactly, and what this member contributes to the
   image. Add Quran passages outside the surah, with exact refs, where they stage or confirm the chain; for
   each, name the speaker and the situation in a few words, and include the ayah that opens its scene when the
   passage continues one.
2. `## Interactions`. Where chains meet: a shared member, a dictionary phrase that joins members of two chains,
   a Quran passage that stages two chains together, or one chain's scene needing another's. One line each: the
   chains, where they meet, the evidence.
3. `## Ayat`. For each ayah in order: the chains its words take part in, what its words add to each, and in one
   line the whole scene each chain makes across the surah, so that a writer who sees only this ayah sees the
   scene, not a fragment.
4. `## Not carried`. Each channel subchannel you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s042/surah.r2/text.md =====
# Surah 42

- 42:1 حمٓ
- 42:2 عٓسٓقٓ
- 42:3 كَذَٰلِكَ يُوحِىٓ إِلَيْكَ وَإِلَى ٱلَّذِينَ مِن قَبْلِكَ ٱللَّهُ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 42:4 لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- 42:5 تَكَادُ ٱلسَّمَٰوَٰتُ يَتَفَطَّرْنَ مِن فَوْقِهِنَّ ۚ وَٱلْمَلَٰٓئِكَةُ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ وَيَسْتَغْفِرُونَ لِمَن فِى ٱلْأَرْضِ ۗ أَلَآ إِنَّ ٱللَّهَ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- 42:6 وَٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ ٱللَّهُ حَفِيظٌ عَلَيْهِمْ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ
- 42:7 وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ قُرْءَانًا عَرَبِيًّۭا لِّتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا وَتُنذِرَ يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ ۚ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ
- 42:8 وَلَوْ شَآءَ ٱللَّهُ لَجَعَلَهُمْ أُمَّةًۭ وَٰحِدَةًۭ وَلَٰكِن يُدْخِلُ مَن يَشَآءُ فِى رَحْمَتِهِۦ ۚ وَٱلظَّٰلِمُونَ مَا لَهُم مِّن وَلِىٍّۢ وَلَا نَصِيرٍ
- 42:9 أَمِ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ ۖ فَٱللَّهُ هُوَ ٱلْوَلِىُّ وَهُوَ يُحْىِ ٱلْمَوْتَىٰ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- 42:10 وَمَا ٱخْتَلَفْتُمْ فِيهِ مِن شَىْءٍۢ فَحُكْمُهُۥٓ إِلَى ٱللَّهِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبِّى عَلَيْهِ تَوَكَّلْتُ وَإِلَيْهِ أُنِيبُ
- 42:11 فَاطِرُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَمِنَ ٱلْأَنْعَٰمِ أَزْوَٰجًۭا ۖ يَذْرَؤُكُمْ فِيهِ ۚ لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- 42:12 لَهُۥ مَقَالِيدُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- 42:13 ۞ شَرَعَ لَكُم مِّنَ ٱلدِّينِ مَا وَصَّىٰ بِهِۦ نُوحًۭا وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَمَا وَصَّيْنَا بِهِۦٓ إِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَىٰٓ ۖ أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ ۚ ٱللَّهُ يَجْتَبِىٓ إِلَيْهِ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَن يُنِيبُ
- 42:14 وَمَا تَفَرَّقُوٓا۟ إِلَّا مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْعِلْمُ بَغْيًۢا بَيْنَهُمْ ۚ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى لَّقُضِىَ بَيْنَهُمْ ۚ وَإِنَّ ٱلَّذِينَ أُورِثُوا۟ ٱلْكِتَٰبَ مِنۢ بَعْدِهِمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- 42:15 فَلِذَٰلِكَ فَٱدْعُ ۖ وَٱسْتَقِمْ كَمَآ أُمِرْتَ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ ۖ وَقُلْ ءَامَنتُ بِمَآ أَنزَلَ ٱللَّهُ مِن كِتَٰبٍۢ ۖ وَأُمِرْتُ لِأَعْدِلَ بَيْنَكُمُ ۖ ٱللَّهُ رَبُّنَا وَرَبُّكُمْ ۖ لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ ۖ لَا حُجَّةَ بَيْنَنَا وَبَيْنَكُمُ ۖ ٱللَّهُ يَجْمَعُ بَيْنَنَا ۖ وَإِلَيْهِ ٱلْمَصِيرُ
- 42:16 وَٱلَّذِينَ يُحَآجُّونَ فِى ٱللَّهِ مِنۢ بَعْدِ مَا ٱسْتُجِيبَ لَهُۥ حُجَّتُهُمْ دَاحِضَةٌ عِندَ رَبِّهِمْ وَعَلَيْهِمْ غَضَبٌۭ وَلَهُمْ عَذَابٌۭ شَدِيدٌ
- 42:17 ٱللَّهُ ٱلَّذِىٓ أَنزَلَ ٱلْكِتَٰبَ بِٱلْحَقِّ وَٱلْمِيزَانَ ۗ وَمَا يُدْرِيكَ لَعَلَّ ٱلسَّاعَةَ قَرِيبٌۭ
- 42:18 يَسْتَعْجِلُ بِهَا ٱلَّذِينَ لَا يُؤْمِنُونَ بِهَا ۖ وَٱلَّذِينَ ءَامَنُوا۟ مُشْفِقُونَ مِنْهَا وَيَعْلَمُونَ أَنَّهَا ٱلْحَقُّ ۗ أَلَآ إِنَّ ٱلَّذِينَ يُمَارُونَ فِى ٱلسَّاعَةِ لَفِى ضَلَٰلٍۭ بَعِيدٍ
- 42:19 ٱللَّهُ لَطِيفٌۢ بِعِبَادِهِۦ يَرْزُقُ مَن يَشَآءُ ۖ وَهُوَ ٱلْقَوِىُّ ٱلْعَزِيزُ
- 42:20 مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
- 42:21 أَمْ لَهُمْ شُرَكَٰٓؤُا۟ شَرَعُوا۟ لَهُم مِّنَ ٱلدِّينِ مَا لَمْ يَأْذَنۢ بِهِ ٱللَّهُ ۚ وَلَوْلَا كَلِمَةُ ٱلْفَصْلِ لَقُضِىَ بَيْنَهُمْ ۗ وَإِنَّ ٱلظَّٰلِمِينَ لَهُمْ عَذَابٌ أَلِيمٌۭ
- 42:22 تَرَى ٱلظَّٰلِمِينَ مُشْفِقِينَ مِمَّا كَسَبُوا۟ وَهُوَ وَاقِعٌۢ بِهِمْ ۗ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِى رَوْضَاتِ ٱلْجَنَّاتِ ۖ لَهُم مَّا يَشَآءُونَ عِندَ رَبِّهِمْ ۚ ذَٰلِكَ هُوَ ٱلْفَضْلُ ٱلْكَبِيرُ
- 42:23 ذَٰلِكَ ٱلَّذِى يُبَشِّرُ ٱللَّهُ عِبَادَهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا إِلَّا ٱلْمَوَدَّةَ فِى ٱلْقُرْبَىٰ ۗ وَمَن يَقْتَرِفْ حَسَنَةًۭ نَّزِدْ لَهُۥ فِيهَا حُسْنًا ۚ إِنَّ ٱللَّهَ غَفُورٌۭ شَكُورٌ
- 42:24 أَمْ يَقُولُونَ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًۭا ۖ فَإِن يَشَإِ ٱللَّهُ يَخْتِمْ عَلَىٰ قَلْبِكَ ۗ وَيَمْحُ ٱللَّهُ ٱلْبَٰطِلَ وَيُحِقُّ ٱلْحَقَّ بِكَلِمَٰتِهِۦٓ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- 42:25 وَهُوَ ٱلَّذِى يَقْبَلُ ٱلتَّوْبَةَ عَنْ عِبَادِهِۦ وَيَعْفُوا۟ عَنِ ٱلسَّيِّـَٔاتِ وَيَعْلَمُ مَا تَفْعَلُونَ
- 42:26 وَيَسْتَجِيبُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَيَزِيدُهُم مِّن فَضْلِهِۦ ۚ وَٱلْكَٰفِرُونَ لَهُمْ عَذَابٌۭ شَدِيدٌۭ
- 42:27 ۞ وَلَوْ بَسَطَ ٱللَّهُ ٱلرِّزْقَ لِعِبَادِهِۦ لَبَغَوْا۟ فِى ٱلْأَرْضِ وَلَٰكِن يُنَزِّلُ بِقَدَرٍۢ مَّا يَشَآءُ ۚ إِنَّهُۥ بِعِبَادِهِۦ خَبِيرٌۢ بَصِيرٌۭ
- 42:28 وَهُوَ ٱلَّذِى يُنَزِّلُ ٱلْغَيْثَ مِنۢ بَعْدِ مَا قَنَطُوا۟ وَيَنشُرُ رَحْمَتَهُۥ ۚ وَهُوَ ٱلْوَلِىُّ ٱلْحَمِيدُ
- 42:29 وَمِنْ ءَايَٰتِهِۦ خَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَثَّ فِيهِمَا مِن دَآبَّةٍۢ ۚ وَهُوَ عَلَىٰ جَمْعِهِمْ إِذَا يَشَآءُ قَدِيرٌۭ
- 42:30 وَمَآ أَصَٰبَكُم مِّن مُّصِيبَةٍۢ فَبِمَا كَسَبَتْ أَيْدِيكُمْ وَيَعْفُوا۟ عَن كَثِيرٍۢ
- 42:31 وَمَآ أَنتُم بِمُعْجِزِينَ فِى ٱلْأَرْضِ ۖ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- 42:32 وَمِنْ ءَايَٰتِهِ ٱلْجَوَارِ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ
- 42:33 إِن يَشَأْ يُسْكِنِ ٱلرِّيحَ فَيَظْلَلْنَ رَوَاكِدَ عَلَىٰ ظَهْرِهِۦٓ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍ
- 42:34 أَوْ يُوبِقْهُنَّ بِمَا كَسَبُوا۟ وَيَعْفُ عَن كَثِيرٍۢ
- 42:35 وَيَعْلَمَ ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِنَا مَا لَهُم مِّن مَّحِيصٍۢ
- 42:36 فَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- 42:37 وَٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ وَإِذَا مَا غَضِبُوا۟ هُمْ يَغْفِرُونَ
- 42:38 وَٱلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَمْرُهُمْ شُورَىٰ بَيْنَهُمْ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- 42:39 وَٱلَّذِينَ إِذَآ أَصَابَهُمُ ٱلْبَغْىُ هُمْ يَنتَصِرُونَ
- 42:40 وَجَزَٰٓؤُا۟ سَيِّئَةٍۢ سَيِّئَةٌۭ مِّثْلُهَا ۖ فَمَنْ عَفَا وَأَصْلَحَ فَأَجْرُهُۥ عَلَى ٱللَّهِ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلظَّٰلِمِينَ
- 42:41 وَلَمَنِ ٱنتَصَرَ بَعْدَ ظُلْمِهِۦ فَأُو۟لَٰٓئِكَ مَا عَلَيْهِم مِّن سَبِيلٍ
- 42:42 إِنَّمَا ٱلسَّبِيلُ عَلَى ٱلَّذِينَ يَظْلِمُونَ ٱلنَّاسَ وَيَبْغُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌ أَلِيمٌۭ
- 42:43 وَلَمَن صَبَرَ وَغَفَرَ إِنَّ ذَٰلِكَ لَمِنْ عَزْمِ ٱلْأُمُورِ
- 42:44 وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن وَلِىٍّۢ مِّنۢ بَعْدِهِۦ ۗ وَتَرَى ٱلظَّٰلِمِينَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ يَقُولُونَ هَلْ إِلَىٰ مَرَدٍّۢ مِّن سَبِيلٍۢ
- 42:45 وَتَرَىٰهُمْ يُعْرَضُونَ عَلَيْهَا خَٰشِعِينَ مِنَ ٱلذُّلِّ يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ ۗ وَقَالَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَآ إِنَّ ٱلظَّٰلِمِينَ فِى عَذَابٍۢ مُّقِيمٍۢ
- 42:46 وَمَا كَانَ لَهُم مِّنْ أَوْلِيَآءَ يَنصُرُونَهُم مِّن دُونِ ٱللَّهِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن سَبِيلٍ
- 42:47 ٱسْتَجِيبُوا۟ لِرَبِّكُم مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۚ مَا لَكُم مِّن مَّلْجَإٍۢ يَوْمَئِذٍۢ وَمَا لَكُم مِّن نَّكِيرٍۢ
- 42:48 فَإِنْ أَعْرَضُوا۟ فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ ۗ وَإِنَّآ إِذَآ أَذَقْنَا ٱلْإِنسَٰنَ مِنَّا رَحْمَةًۭ فَرِحَ بِهَا ۖ وَإِن تُصِبْهُمْ سَيِّئَةٌۢ بِمَا قَدَّمَتْ أَيْدِيهِمْ فَإِنَّ ٱلْإِنسَٰنَ كَفُورٌۭ
- 42:49 لِّلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ يَخْلُقُ مَا يَشَآءُ ۚ يَهَبُ لِمَن يَشَآءُ إِنَٰثًۭا وَيَهَبُ لِمَن يَشَآءُ ٱلذُّكُورَ
- 42:50 أَوْ يُزَوِّجُهُمْ ذُكْرَانًۭا وَإِنَٰثًۭا ۖ وَيَجْعَلُ مَن يَشَآءُ عَقِيمًا ۚ إِنَّهُۥ عَلِيمٌۭ قَدِيرٌۭ
- 42:51 ۞ وَمَا كَانَ لِبَشَرٍ أَن يُكَلِّمَهُ ٱللَّهُ إِلَّا وَحْيًا أَوْ مِن وَرَآئِ حِجَابٍ أَوْ يُرْسِلَ رَسُولًۭا فَيُوحِىَ بِإِذْنِهِۦ مَا يَشَآءُ ۚ إِنَّهُۥ عَلِىٌّ حَكِيمٌۭ
- 42:52 وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ رُوحًۭا مِّنْ أَمْرِنَا ۚ مَا كُنتَ تَدْرِى مَا ٱلْكِتَٰبُ وَلَا ٱلْإِيمَٰنُ وَلَٰكِن جَعَلْنَٰهُ نُورًۭا نَّهْدِى بِهِۦ مَن نَّشَآءُ مِنْ عِبَادِنَا ۚ وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 42:53 صِرَٰطِ ٱللَّهِ ٱلَّذِى لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ أَلَآ إِلَى ٱللَّهِ تَصِيرُ ٱلْأُمُورُ


===== _commentary/v16/work/s042/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ح ي (root_001633): 42:3 يُوحِىٓ, 42:7 أَوْحَيْنَآ, 42:13 أَوْحَيْنَآ, 42:51 وَحْيًا, 42:51 فَيُوحِىَ, 42:52 أَوْحَيْنَآ

- **B001** bilgiyi ya da sözü gizlice iletme — bilgiyi ya da sözü gizlice iletme · sözü başkalarından gizleyerek ona söylemek · güvenilir bir elçi göndermek ya da aracısız konuşmak
  أصل يدل على إلقاء علم في إخفاء إلى غيرك (maqayis)؛ كل ما ألقيته إلى غيرك (maqayis;sihah)؛ إعلام في خفاء (tahdhib)؛ يكون بالكلام على سبيل الرمز والتعريض (mufradat)
- **B002** işaret veya simgeyle anlatma — işaret veya beden hareketiyle anlatma · ona işaret etmek · bir haberi işaretle anlatmak ya da hafif sesle söylemek
  الوحي الإشارة (maqayis;sihah)؛ من الناس إشارة (jamhara)؛ أومأ إليهم وأشار (jamhara;tahdhib)؛ رمز أو أشار (mufradat)
- **B003** yazma ve yazılı metin — yazı, kitap, ileti veya yazma · yazmak · taşa yazmak · kitabı yazmak
  الوحي الكتاب والرسالة (maqayis)؛ وحي يحي وحيا أي كتب (ayn)؛ وحى في الحجر إذا كتب فيه (jamhara)؛ وحى وأوحى أي كتب (sihah)؛ وحيت الكتاب أي كتبته (tahdhib)؛ بالكتابة (mufradat)
- **B004** Tanrı'nın seçilmiş kuluna bildirimi — Tanrı'nın seçilmiş kuluna bilgi ulaştırması
  أوحى الله تعالى ووحى (maqayis)؛ من الله نبأ وإلهام (jamhara)؛ أوحى الله إلى أنبيائه (sihah)؛ إما إلهاما وإما رؤيا وإما أن ينزل عليه كتابا (tahdhib)؛ الكلمة الإلهية التي تلقى إلى أنبيائه وأوليائه (mufradat)
- **B005** ses, özellikle hafif veya uzayan ses — ses, özellikle hafif veya uzayan ses · haberi işaretle ya da hafif sesle iletmek · ses · gök gürültüsünün uzayan hafif sesi
  الوحي الصوت (maqayis)؛ الوحى مثال الوغى الصوت (sihah)؛ وحاة الرعد وهو صوته الممدود الخفي (sihah)؛ الوحاة الصوت (tahdhib)؛ بصوت مجرد عن التركيب (mufradat)
- **B006** hız, acele ve hızlandırma — hızlı · hız · acele, acele · acele et · onu hızlandırdı · çabuk gelen ölüm · hayvanını hızla kesmek
  الوحي السريع (maqayis)؛ الوحاء السرعة (jamhara;tahdhib)؛ الوحي الوحي يعني البدار البدار (sihah)؛ توح يا هذا أي أسرع (sihah;tahdhib)؛ وحاه توحية أي عجله (sihah)؛ وحى فلان ذبيحته إذا ذبحه ذبحا وحيا (tahdhib)؛ أمر وحي (mufradat)
- **B007** yardım isteme, sorma veya salmak için çağırma — onlardan yardım istemek · ona sorup bilgi istemek · köpeği salmak için çağırmak
  استوحيناهم أي استصرخناهم (sihah)؛ استوحيته أي استفهمته (tahdhib)؛ استوحيت الكلب إذا دعوته لترسله (tahdhib)
- **B008** özel adlandırma kümesi — yoksulluktan sonra hükümdar olmak · yönetiminde zulmetmek · ateş · hükümdar
  أوحى الإنسان إذا صار ملكا بعد فقر؛ أوحى الإنسان ووحى وأحى إذا ظلم في سلطانه؛ الوحى النار؛ يقال للملك وحى؛ الوحى النار فكأنه مثل النار ينفع ويضر
- **B009** ağlama ve ölünün ardından ağıt yakma — ağlama · babasının ardından ağlamak · ölünün ardından ağıt yakmak
  الإيحاء البكاء؛ فلان يوحي أباه أي يبكيه؛ النائحة توحي الميت تنوح عليه
- **B010** taşa kazınmış yazı benzetmeleri [kalıp] — sırrını güvenle saklayan kişi için söylenen söz · taşa kazınmış yazı kadar apaçık
  وحي في حجر يضرب مثلا لمن يكتم سره؛ هو كالوحي في الحجر إذا نقر فيه نقرا

## ق ب ل (root_001198): 42:3 قَبْلِكَ, 42:25 يَقْبَلُ, 42:47 قَبْلِ

- **B001** karşı karşıya olma ve ön yön — ön taraf, karşıya dönük yön · ön taraftaki cinsel bölge · yüz yüze, göz göre göre yapmak · karşısında, tam karşı hizada · dağın karşıdan görünen yamacı veya yükseltisi · yönelecek bir yönü yok; işin yolunu bulamıyor
  مواجهة الشيء للشيء (maqayis)؛ القبل خلاف الدبر (ayn;tahdhib)؛ قبل ضد الدبر (jamhara)؛ المقابلة المواجهة (sihah)؛ الإقبال التوجه نحو القبل (mufradat)
- **B002** önce olma ve sırada yaklaşma — önce; zaman, yer veya sırada önde · gelecek veya yaklaşan yıl, gece ve benzeri dönem · bundan sonraki zamanda · gençliğinin başında, yaşlılık izi belirmemiş
  قبل الذي هو خلاف بعد (maqayis)؛ من قبل ومن بعد غايتان (ayn;tahdhib)؛ قبل ضد بعد (jamhara)؛ القابلة الليلة المقبلة والعام القابل المقبل (sihah;tahdhib)؛ قبل يستعمل في التقدم المتصل والمنفصل (mufradat)
- **B003** birinin tarafından veya nezdinde [kalıp] — o kişiden, onun tarafından veya yanından · o kişide hakkım var; ondan alacağım var
  هذا من قبل فلان أي من عنده (maqayis)؛ أصيب هذا من قبله أي من تلقائه ومن لدنه (ayn;tahdhib)؛ لي قبل فلان حق أي عنده (sihah;mufradat)
- **B004** uygun bulup benimseme — bir şeyi uygun bulup benimsemek · olumlu karşılayıp benimsemek ve karşılığını vermek · göze ve gönle hoş gelmek
  قبلت الشيء قبولا (maqayis)؛ التقبل القبول (ayn)؛ تقبلت الشيء وقبلته قبولا (sihah)؛ قبلت الشيء قبولا إذا رضيته (tahdhib)؛ قبلت عذره وتوبته وغيره وتقبلته (mufradat)
- **B005** namazda yönelinen yön — namazda yönelinen yön veya yer
  القبلة سميت قبلة لإقبال الناس عليها في صلاتهم (maqayis)؛ القبلة قبلة الصلاة (jamhara)؛ القبلة التي يصلى نحوها (sihah)؛ صار اسما للمكان المقابل المتوجه إليه للصلاة (mufradat)
- **B006** öpücük ve öpme — öpücük; dudakla öpmek
  الفعل من القبلة التقبيل (ayn)؛ القبلة من التقبيل معروفة (sihah)؛ القبلة معروفة وجمعها القبل وفعلها التقبيل (tahdhib)؛ ومنه القبلة وجمعها قبل وقبلته تقبيلا (mufradat)
- **B007** çıkanı karşılayıp teslim alma — doğumda bebeği karşılayıp alan kadın · kuyudan çıkan kovayı teslim alan kişi
  القابلة التي تقبل الولد عند الولاد (maqayis)؛ القابلة التي تقبل الولد عند الولاد (ayn)؛ القابلة التي تقبل الصبي (jamhara)؛ القابلة من النساء معروفة (sihah)؛ القابل الذي يستقبل الدلو من البئر (mufradat)
- **B008** güvence ve sorumluluk üstlenme — başkası için güvence veren kişi · güvence üstlenme veya yazılı yüklenim
  القبيل الكفيل يقال قبل به قبالة (maqayis)؛ القبيل الكفيل (jamhara)؛ القبيل الكفيل والعريف (sihah)؛ قبل به يقبل به قبالة إذا كفل به (tahdhib)؛ قيل للكفالة قبالة (mufradat)
- **B009** soy veya kuşak topluluğu — insan topluluğu veya kuşak · aynı atadan gelen soy topluluğu · topluluğun işlerini gözeten temsilci
  قبائل العرب (maqayis)؛ كل جيل من الجن والإنس قبل (ayn)؛ القبيل جيل من الناس (jamhara)؛ القبيل الجماعة تكون من الثلاثة فصاعدا (sihah)؛ القبيلة بنو أب واحد (tahdhib)؛ القبيل جمع قبيلة وهي الجماعة المجتمعة (mufradat)
- **B010** karşılıklı birleşen ve bağlayan parçalar — kafatası bölümleri ve birleşme çizgileri · ayakkabının parmaklar arasındaki bağı · iplik veya ipin ileri ve geri büküm yönleri · gem, giysi ve eyerin bağlı kayış, yama ve kemerleri
  القبال زمام البعير والنعل (maqayis)؛ قبيلة الرأس كل فلقة قوبلت بالأخرى (ayn)؛ قبال النعل معروف (jamhara)؛ قبال النعل الزمام (sihah)؛ قبائلا اللجام سيوره (tahdhib)؛ قبال النعل زمامها (mufradat)
- **B011** beden bölümünün belirli yöne dönüklüğü — göz bebeğinin buruna veya iç yana yönelmesi · bacakların veya ayakların ayrık duruşu · kulağı ön yandan kesik veya boynuzları öne dönük koyun
  القبل في العين إقبال السواد على المحجر (maqayis)؛ القبال شبه فحج (ayn)؛ رجل أقبل والأنثى قبلاء (jamhara)؛ شاة قبلاء بينة القبل (sihah)؛ الأقبل الذي أقبلت حدقتاه على أنفه (tahdhib)؛ وشاة مقابلة قطع من قبل أذنها (mufradat)
- **B012** batı rüzgarının karşıtı olan rüzgar — batı rüzgarının karşıtı olan rüzgar
  القبول من الرياح الصبا لأنها تقابل الدبور (maqayis)؛ القبول الصبا (ayn)؛ الريح القبول الصبا (jamhara)؛ القبول أيضا الصبا (sihah)؛ القبول من الرياح الصبا (tahdhib)؛ القبول ريح الصبا (mufradat)
- **B013** onunla başa çıkacak gücü olmama [kalıp] — onunla başa çıkacak veya ona karşı koyacak gücüm yok
  لا قبل لي به أي لا طاقة (maqayis)؛ القبل الطاقة (ayn)؛ ما لي به قبل أي طاقة (sihah)؛ لا قبل معناه لا طاقة لهم بها (tahdhib)؛ لا قبل لي بكذا أي لا يمكنني أن أقابله (mufradat)
- **B014** develer içerken önlerine su çekip dökme — develer içerken başları veya ağızları üzerinde su çekip dökme
  أقبلنا على الإبل إذا استقينا على رءوسها وهي تشرب (maqayis)؛ القبل أن يورد الرجل إبله ثم يستقي لها (jamhara)؛ القبل أن تشرب الإبل الماء وهو يصب على رؤوسها (sihah)؛ القبل أن يورد الرجل إبله فيستقي على أفواهها (tahdhib)
- **B015** ilk elden veya yeniden başlama — ayı daha önce görülmemişken ilk kez ince haliyle görmek · önceden hazırlamadan konuşmak veya söylemek · işi yeniden ele alıp başlamak
  القبل استئناف الشيء (ayn)؛ رأيت هلال كذا قبلا فكان صغيرا (jamhara)؛ تكلم فلان قبلا فأجاد (sihah)؛ اقتبل أمره إذا استأنفه (tahdhib)
- **B016** asılan boncuk veya makara biçimli takı — asılan boncuk veya makara biçimli takı; yüzü birine çevirdiğine inanılan türü
  القبلة خرزة شبيهة بالفلكة (maqayis)؛ القبلة خرزة من خرز نساء الأعراب (jamhara)؛ القبل جمع قبلة وهي الفلكة (sihah)؛ القبلة حجر أبيض عظيم تجعل في عنق الفرس (tahdhib)؛ القبلة خرزة يزعم الساحر أنه يقبل بالإنسان (mufradat)

## ء ل ه (root_000047): 42:3 ٱللَّهُ, 42:5 ٱللَّهَ, 42:6 ٱللَّهُ, 42:8 ٱللَّهُ, 42:9 فَٱللَّهُ, 42:10 ٱللَّهِ, 42:10 ٱللَّهُ, 42:13 ٱللَّهُ, 42:15 ٱللَّهُ, 42:15 ٱللَّهُ, 42:15 ٱللَّهُ, 42:16 ٱللَّهِ, 42:17 ٱللَّهُ, 42:19 ٱللَّهُ, 42:21 ٱللَّهُ, 42:23 ٱللَّهُ, 42:23 ٱللَّهَ, 42:24 ٱللَّهِ, 42:24 ٱللَّهُ, 42:24 ٱللَّهُ, 42:27 ٱللَّهُ, 42:31 ٱللَّهِ, 42:36 ٱللَّهِ, 42:40 ٱللَّهِ, 42:44 ٱللَّهُ, 42:46 ٱللَّهِ, 42:46 ٱللَّهُ, 42:47 ٱللَّهِ, 42:49 لِّلَّهِ, 42:51 ٱللَّهُ, 42:53 ٱللَّهِ, 42:53 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 42:3 ٱللَّهُ, 42:5 ٱللَّهَ, 42:6 ٱللَّهُ, 42:8 ٱللَّهُ, 42:9 فَٱللَّهُ, 42:10 ٱللَّهِ, 42:10 ٱللَّهُ, 42:13 ٱللَّهُ, 42:15 ٱللَّهُ, 42:15 ٱللَّهُ, 42:15 ٱللَّهُ, 42:16 ٱللَّهِ, 42:17 ٱللَّهُ, 42:19 ٱللَّهُ, 42:21 ٱللَّهُ, 42:23 ٱللَّهُ, 42:23 ٱللَّهَ, 42:24 ٱللَّهِ, 42:24 ٱللَّهُ, 42:24 ٱللَّهُ, 42:27 ٱللَّهُ, 42:31 ٱللَّهِ, 42:36 ٱللَّهِ, 42:40 ٱللَّهِ, 42:44 ٱللَّهُ, 42:46 ٱللَّهِ, 42:46 ٱللَّهُ, 42:47 ٱللَّهِ, 42:49 لِّلَّهِ, 42:51 ٱللَّهُ, 42:53 ٱللَّهِ, 42:53 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ع ز ز (root_001008): 42:3 ٱلْعَزِيزُ, 42:19 ٱلْعَزِيزُ

- **B001** güçlü, yenilmez ve saygın olma — yenilmezlik sağlayan güç ve saygınlık durumu · güçlü, üstün gelen ve yenilmeyen · güçsüzlükten çıkıp güçlü ve saygın duruma gelmek
  العين والزاء أصل صحيح واحد يدل على شدة وقوة (maqayis); العزة لله والله العزيز (ayn); عز يعز عزة وعزا إذا صار عزيزا (jamhara); العز خلاف الذل (sihah); العزيز الممتنع فلا يغلبه شيء (tahdhib); العزة حالة مانعة للإنسان من أن يغلب (mufradat)
- **B002** üstün gelip boyun eğdirme — onu yenip boyun eğdirmek · onunla üstünlük yarışına girmek · sözlü çekişmede beni yenmek · üstün gelen, yenilenin malını alır
  غلبة وقهر (maqayis); عزه على أمره إذا غلبه (maqayis); وعزني في الخطاب أي غلبني (ayn;tahdhib;mufradat); عز يعز عزا إذا قهر (jamhara); عزه يعزه عزا غلبه (sihah); عزه يعزه إذا غلبه وقهره (tahdhib)
- **B003** çok kıt ve güç bulunur olma — neredeyse bulunamayacak kadar azalmak · kıt, güç bulunan ve benzeri olmayan
  عز الشيء حتى يكاد لا يوجد (maqayis); عز الشيء جامع لكل شيء إذا قل حتى يكاد لا يوجد (ayn); عز الشئ إذا قل لا يكاد يوجد (sihah); عز كذا وكذا إذا قل حتى لا يكاد يوجد (tahdhib); يصعب مناله ووجود مثله (mufradat)
- **B004** güçlendirip pekiştirme — onu güçlü ve saygın kılmak · onu güçlendirip sağlamlaştırmak
  أعززته أنا جعلته عزيزا (maqayis); أعززته قويته وعززته أيضا (maqayis); أعزه الله (ayn); فعززنا بثالث أي قوينا وشددنا (sihah); قويناه وشددناه (tahdhib)
- **B005** kişiye ağır ve çetin gelme — bu bana zor, ağır ve çetin geldi · başına gelen bana çok büyük ve ağır geldi
  أعززت بما أصاب فلانا أي عظم علي واشتد (maqayis); أعزز علي بما أصاب فلانا أي أعظم علي (ayn); عز علي أن تفعل كذا (sihah); عز علي ذاك أي حق واشتد (sihah); عز علي كذا صعب (mufradat)
- **B006** dar kanallı ve güç sağılan olma — meme kanalı dar, sütü az veya güç sağılan dişi hayvan · malı çok olduğu halde vermeyen cimri kişi
  ناقة عزوز إذا كانت ضيقة الإحليل لا تدر إلا بجهد (maqayis); العزوز الشاة الضيقة الإحليل (ayn); العزوز من النوق الضيقة الإحليل (sihah); شاة عزوز ضيقة الإحليل لا تدر حتى تحلب بجهد (tahdhib); شاة عزوز قل درها (mufradat)
- **B007** sertleşip sıkıca pekişme — taşsız, sert ve su tutmayan zemin · kum sıkılaşıp dağılmaz hale gelmek · yağmur toprağı bastırıp pekiştirmek
  العزازة أرض صلبة ليست بذات حجارة (maqayis); العزاز أرض صلبة (ayn;sihah;tahdhib); كل شيء صلب فقد استعز (jamhara); تعزز لحم الناقة إذا صلب واشتد (maqayis;tahdhib); استعز الرمل وغيره إذا تماسك فلم ينهل (maqayis;sihah); المطر يعزز الأرض أي يلبدها (sihah;mufradat)
- **B008** çetin ve baskın doğa şiddeti — ağır ve çetin yıl · çok ve şiddetli yağmur · baskın ve güçlü sel
  العزاء السنة الشديدة (maqayis;ayn;sihah); العز من المطر الكثير الشديد (maqayis); مطر عز أي شديد (sihah); العز المطر الشديد الوابل (tahdhib); سيل عز وهو السيل الغالب (maqayis)
- **B009** hastalık veya durumun kişiye üstün gelmesi — hastalık, ölüm veya başka bir durum ona üstün gelmek · iş onun üzerinde inatla sürüp egemen olmak · hastalığı çok ağır olan kişi
  استعز على المريض إذا اشتد مرضه (maqayis); استعز به المرض (maqayis); استعز عليه الشيطان أي غلب عليه (maqayis); استعز عليه الأمر إذا لج فيه (maqayis); استعز بفلان أي غلب في كل شيء مرض أو غيره (sihah;tahdhib); استعز بفلان إذا غلب بمرض أو بموت (mufradat)
- **B010** atın iki kalça ucu arasındaki bölge — atın sağrı ile uyluk yakınındaki iki kalça ucu arası
  العزيزاء من الفرس ما بين عكوته وجاعرته (maqayis); العزيزى من الفرس وهما طرفا الوركين (sihah); العزيزاء وهما عزيزاوا الفرس ما بين جاعرتيه (tahdhib)
- **B011** biçime bağlı adlandırmalar — en güçlü veya en üstün sıfatının dişil biçimi · tapınılan bir putun veya kutsal ağacın adı · ceylan yavrusu; buradan türeyen kadın adı
  العزى تأنيث الأعز (maqayis;tahdhib); العزى صنم (mufradat); العزى سمرة كانت لغطفان يعبدونها (sihah;tahdhib); العزة بالفتح بنت الظبية وبها سميت المرأة عزة (sihah;tahdhib)
- **B012** keçiyi kovma ünlemiyle sürme — keçiyi kovmak için çıkarılan ünlem · keçiyi bu ünlemle azarlayıp sürmek
  يقال للعنز إذا زجرت عز عز (tahdhib); عزعزت بها فلم تعزعز (tahdhib)

## ح ك م (root_000348): 42:3 ٱلْحَكِيمُ, 42:10 فَحُكْمُهُۥٓ, 42:51 حَكِيمٌ

- **B001** alıkoyup geri çevirmek — haksızlıktan veya bozulmadan alıkoyup geri çevirmek · sorumsuz kişinin elini tutup zarar vermesini önlemek · yetimi bozulmadan koruyup durumunu düzeltmek · birini yapmak istediği şeyden alıkoymak
  الحكم وهو المنع من الظلم (maqayis)؛ كل شيء منعته من الفساد فقد حكمته وحكمته وأحكمته (ayn)؛ حكمت السفيه وأحكمته إذا أخذت على يده (sihah)؛ كل من منعته من شيء فقد حكمته وأحكمته (tahdhib)؛ حكم أصله منع منعا لإصلاح (mufradat)
- **B002** uyuşmazlığı bağlayıcı kararla sonuçlandırmak — insanlar arasında doğru ölçüyle karar vermek · biri lehine veya aleyhine karar vermek · karar verme veya işi karara bağlama · insanlar arasında karar veren kişi · karar verme işiyle özellikle görevli kişi · çekişmede verilen karar veya yaralanma karşılığını belirleme · çekişmeyi karar verecek bir mercie götürmek
  الحكم وهو المنع من الظلم (maqayis)؛ حاكمناه إلى الله دعوناه إلى حكم الله (ayn)؛ الحكم مصدر قولك حكم بينهم أي قضى (sihah)؛ الحكم أيضا القضاء بالعدل (tahdhib)؛ الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا (mufradat)
- **B003** bilgi ve usla doğruyu bulma yetkinliği — bilgi ve kavrayış ya da doğru bir önerme · bilgi ve usla doğruyu bulma yetkinliği · bilgili, deneyimli ve doğruyu bulan kişi · deneyimle olgunlaşmış bilge yaşlı
  الحكمة تمنع من الجهل (maqayis)؛ الحكمة مرجعها إلى العدل والعلم والحلم (ayn)؛ الحكمة من العلم والحكيم العالم وصاحب الحكمة (sihah)؛ الحكم العلم والفقه (tahdhib)؛ الحكمة إصابة الحق بالعلم والعقل (mufradat)
- **B004** sağlam ve kusursuz duruma getirmek — bir şeyi sağlamlaştırmak veya sağlam duruma gelmek · kusur ve kuşkuya yer bırakmayacak biçimde sağlamlaştırılmış · işleri sağlam ve kusursuz yapan · övgüye değer niteliğinde doruğa varmak · kendisine zarar verecek şeylerden bütünüyle uzaklaşmak
  استحكم الأمر وثق (ayn)؛ أحكمت الشيء فاستحكم أي صار محكما (sihah)؛ آياته أحكمت وفصلت (tahdhib)؛ المحكم ما لا يعرض فيه شبهة (mufradat)؛ حكم الرجل إذا بلغ النهاية في معناه (tahdhib)
- **B005** karar verme yetkisini başkasına bırakmak — bir işte karar verme yetkisini ona bırakmak · malı üzerinde uygun gördüğü gibi davranabilmek · yetim malını yönetmeye elverişli duruma geldiğinde malı üzerinde tasarruf etmesine izin vermek · birinin elini istediğini yapmakta serbest bırakmak
  حكم فلان في كذا إذا جعل أمره إليه (maqayis)؛ احتكم في ماله إذا جاز فيه حكمه (ayn)؛ حكمته في مالي إذا جعلت إليه الحكم فيه (sihah)؛ حكمنا فلانا بيننا أي أجزنا حكمه بيننا (tahdhib)؛ الحكمين أن يتوليا الحكم عليهم ولهم حسب ما يستصوبانه (mufradat)
- **B006** gemin çene çevresini kuşatan kısıtlayıcı parçası — gemin hayvanın çene çevresini kuşatıp koşmasını sınırlayan parçası · hayvana gem takmak veya onu gemle durdurmak · koyunun çenesi · başında gemin kısıtlayıcı parçası bulunan at
  حكمة الدابة لأنها تمنعها (maqayis)؛ حكمة اللجام ما أحاط بحنكيه (ayn)؛ حكمة اللجام ما أحاط بالحنك (sihah)؛ حكمة اللجام ما أحاط بحنكيه (tahdhib)؛ سميت اللجام حكمة الدابة (mufradat)
- **B007** bir şeyden geri dönmek veya birini döndürmek — bir şeyden geri dönmek · birini bir şeyden geri döndürmek
  حكم فلان عن الشيء أي رجع؛ وأحكمته أنا أي رجعته (tahdhib)

## س م و (root_000745): 42:4 ٱلسَّمَٰوَٰتِ, 42:5 ٱلسَّمَٰوَٰتُ, 42:11 ٱلسَّمَٰوَٰتِ, 42:12 ٱلسَّمَٰوَٰتِ, 42:14 مُّسَمًّى, 42:29 ٱلسَّمَٰوَٰتِ, 42:49 ٱلسَّمَٰوَٰتِ, 42:53 ٱلسَّمَٰوَٰتِ

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ECHO و س م (root_001650): for 42:4 ٱلسَّمَٰوَٰتِ, 42:5 ٱلسَّمَٰوَٰتُ, 42:11 ٱلسَّمَٰوَٰتِ, 42:12 ٱلسَّمَٰوَٰتِ, 42:14 مُّسَمًّى, 42:29 ٱلسَّمَٰوَٰتِ, 42:49 ٱلسَّمَٰوَٰتِ, 42:53 ٱلسَّمَٰوَٰتِ: withheld observed target; not identity

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

## ء ر ض (root_000025): 42:4 ٱلْأَرْضِ, 42:5 ٱلْأَرْضِ, 42:11 وَٱلْأَرْضِ, 42:12 وَٱلْأَرْضِ, 42:27 ٱلْأَرْضِ, 42:29 وَٱلْأَرْضِ, 42:31 ٱلْأَرْضِ, 42:42 ٱلْأَرْضِ, 42:49 وَٱلْأَرْضِ, 42:53 ٱلْأَرْضِ

- **B001** yer ve yere bakan alt bölüm — yer, yeryüzü · yerler, ülkeler · bir şeyin yere bakan altı · hayvanın tırnağı veya ayaklarının altı
  كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)
- **B002** yumuşak ve verimli toprak — yumuşak, verimli ve bol bitkili toprak · yumuşak tabanlı geniş çayırlık · toprak verimlileşti · bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi · toprakta kök salmış fidan · oğlak yer bitkisini yedi veya onunla semirdi
  أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)
- **B003** iyiliğe yatkın ve layık [kalıp] — iyiliğe yatkın, layık ve alçak gönüllü kişi · bunu yapmaya en uygunları
  رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)
- **B004** yabancı kimse — yabancı kimse
  فلان ابن أرض أي غريب (maqayis)
- **B005** kalın yün veya kıl yaygı — kalın yün veya kıl yaygı
  الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)
- **B006** yere çökercesine ağırlaşıp oyalanmak — yere bağlı kalmak, ağırlaşıp oyalanmak
  تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)
- **B007** karşısına çıkıp kendini ortaya koymak — birinin karşısına çıkıp kendini ortaya koymak
  جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)
- **B008** titreme veya ürperme — insanı tutan titreme veya ürperme · titreme ve sarsılma
  الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)
- **B009** soğuk algınlığı — soğuk algınlığı · soğuk algınlığına yakalanmış · soğuk algınlığına uğratmak
  الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)
- **B010** odun yiyen küçük canlı — odun yiyen küçük canlı · odunu bu canlı yedi ve zarar verdi
  الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)
- **B011** yaranın irinlenip bozulması [kalıp] — yara irinlenip kabardı ve bozuldu
  أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)
- **B012** doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu — görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi
  المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)

## ع ل و (root_001042): 42:4 ٱلْعَلِىُّ, 42:51 عَلِىٌّ

- **B001** yukarı yükselme ve yüksekte olma — yukarı olma; aşağı karşıtı yükseklik · bir yerde yükselmek · günün yükselmesi · yükselip uzaklaşmak
  أصل واحد يدل على السمو والارتفاع (maqayis)؛ العلو أصل البناء (ayn)؛ علا في المكان يعلو علوا (sihah)؛ العلو ضد السفل والعلو الارتفاع (mufradat)
- **B002** saygınlıkta yüksek mevki — saygınlık ve yüksek mevki · değeri yüksek kimse veya nitelik · en üstün ve en yüksek değerde olan · saygın ve yüksek mevki sahibi · toplumun seçkinleri · kazanılmış yüksek onur dereceleri
  العلاء فالرفعة (maqayis;ayn)؛ رجل عالي الكعب أي شريف (maqayis;ayn)؛ العلاء والعلاء الرفعة والشرف (sihah)؛ العلي هو الرفيع القدر (mufradat)
- **B003** kibirli üstünlük taslama — kınanan büyüklük taslama · yeryüzünde kibirlenip taşkınlık etmek · kibirli ve kendini üstün görenler
  العلو فالعظمة والتجبر (maqayis;ayn)؛ علا ملك في الأرض أي طغى وتعظم (ayn)؛ علا في الأرض تكبر (sihah)؛ علا يقال في المحمود والمذموم (mufradat)
- **B004** yapı içinde üstün gelip bastırma [kalıp] — onu yenip bastırmak · kişiyi yenmek · kılıçla vurmak · işi üstlenip tek başına yürütmek · ata binmek
  من قهر أمرا فقد اعتلاه واستعلى عليه (maqayis)؛ علوت الرجل غلبته (sihah)؛ استعلى الرجل أي علا واستعلاه أي علاه (sihah)؛ الاستعلاء قد يكون طلب العلو المذموم وقد يكون طلب العلاء (mufradat)
- **B005** üst yan ve yukarıdanlık [kalıp] — evin üst kısmı; altının karşıtı · yukarıdan · üstten veya yukarıdan · yukarıdan · rüzgarın avın üstünde kalan yönü
  أسفل الشيء وأعلاه (maqayis)؛ جئتك من أعلى ومن علا ومن عال ومن عل (maqayis)؛ علو الدار نقيض سفلها (sihah)؛ علاوة الريح وسفالتها (sihah;mufradat)؛ علاوة الشيء أعلاه (mufradat)
- **B006** gel diye çağırma — gel; buraya yönel
  تعال فهو من العلو كأنه قال اصعد إلي (maqayis)؛ لا يستعمل هذا إلا في الأمر خاصة (maqayis)؛ التعالي الارتفاع تقول منه إذا أمرت تعال (sihah)؛ تعال أصله أن يدعى الإنسان إلى مكان مرتفع (mufradat)
- **B007** yüksek yer adları — dağ başı veya yüksek yer · yüksek bölge veya yukarıdaki yerleşim · yüksek yerler veya oraların halkı · üst oda · iyi kimselere ait çok yüksek yer veya kayıt
  العلياء رأس كل جبل أو شرف (maqayis)؛ العالية من محال العرب من الحجاز (maqayis)؛ العلية غرفة (maqayis;sihah)؛ العلياء كل مكان مشرف (sihah)؛ لفي عليين (maqayis;mufradat)؛ العلية اسما للغرفة (mufradat)
- **B008** üstüne eklenen veya üst parça — tam yükten sonra üste konan ek yük · baş ve boyun · bir şeyin üst kısmı · kitabın başlığı; başta ve üstte yer alan ad
  العلاوة ما يحمل على البعير بعد تمام الوقر (maqayis)؛ رأس الرجل وعنقه علاوة (maqayis)؛ علوان الكتاب من العلو لأنه أول الكتاب وأعلاه (maqayis)؛ العلاوة ما عليت به على البعير بعد تمام الوقر (sihah)؛ علاوة الشيء أعلاه (mufradat)
- **B009** belirli araç ve parça adları — örs · kurutulmuş süt ürünü konan taş · mızrağın uç kısmına yakın bölümü · oyun oklarının yedincisi ve en değerlisi · kova ipini makaraya geri alan kişi · sağ yandan süt hayvanına yaklaşan kişi · ipi makaradaki yerine kaldırmak
  العلاة وهي السندان (maqayis)؛ العلاة حجر يجعل عليه الأقط والعلاة السندان (sihah)؛ عالية الرمح ما دخل في السنان إلى ثلثه (sihah)؛ المعلى السابع من القداح (maqayis;sihah;mufradat)؛ المعلي الذي يمد الدلو (maqayis)
- **B010** uzun ve iri yapılı — uzun iri kimse veya iri deve · sağlam yapılı dişi deve · uzun, iri ve sağlam yaratılışlı
  ناقة عليان أي طويلة جسيمة ورجل عليان طويل (maqayis)؛ يقال للناقة علاة تشبه بها في صلابتها (maqayis;sihah)؛ يقال رجل عليان وكذلك المرأة (sihah)؛ العليان البعير الضخم (mufradat)
- **B011** bedensel halden kurtulup esenleşme [kalıp] — lohusalıktan temizlenip esenliğe kavuşmak · hastalıktan kurtulmak
  للمرأة إذا طهرت من نفاسها قد تعلت (maqayis)؛ لا يقال إلا للنفساء (maqayis)؛ تعلت المرأة من نفاسها أي سلمت وتعلى الرجل من علته (sihah)
- **B012** ilgeç ve kalıplaşmış görev sözü — üzerinde, üzerine veya benzeri ilgeç görevi · şunu al · bana şunu ver · onun yanından veya üstünden
  جئت من عليك أي من عندك (maqayis)؛ على لها ثلاثة مواضع (sihah)؛ لفظة مشتركة للاسم والفعل والحرف (sihah)؛ على حرف خافض وقد يكون اسما (sihah)؛ عليك زيدا أي خذه (sihah)

## ع ظ م (root_001029): 42:4 ٱلْعَظِيمُ

- **B001** büyük ve güçlü olma; büyük sayıp yüceltme — büyük ve güçlü olmak; değeri yükselmek · büyük, güçlü veya yüce · büyüklük ve yücelik · büyütmek, yüceltmek ve ululamak · gözünde büyütmek veya görkemli göstermek · büyük saymak · Karnın ne kadar büyük! · büyüklük hali
  أصل واحد صحيح يدل على كبر وقوة (maqayis)؛ عظم الشيء عظما فهو عظيم (ayn;sihah;tahdhib)؛ أعظم الأمر وعظمه أي فخمه والتعظيم التبجيل (sihah)؛ عظم الشيء أصله كبر عظمه ثم استعير لكل كبير (mufradat)
- **B002** bir şeyin çoğu veya büyük bölümü [kalıp] — şeyin çoğu · şeyin büyük bölümü · insanların çoğunluğuna katılmak
  ومعظم الشيء أكثره (maqayis)؛ معظم الشيء أكثره والعظم جل الشيء وأكثره (ayn)؛ عظم الشيء أكثره ومعظمه (sihah)؛ عظم الشيء ومعظمه جله وأكبره ودخل في عظم الناس أي في معظمهم (tahdhib)
- **B003** uzvun belirli kalın kesimi [kalıp] — kolun dirseğe yakın kalın bölümü · dilin köke yakın kalın bölümü
  عظمة الذراع مستغلظها (maqayis;sihah;tahdhib)؛ عظمة اللسان مستغلظه فوق العكدة (tahdhib)؛ العظمة ما يلي المرفق من مستغلظ الذراع (tahdhib)؛ عظمة الذراع لمستغلظها (mufradat)
- **B004** ağır ve içinden çıkılmaz felaket — ağır ve korkunç felaket · büyük felaket · içinden çıkılmaz ağır felaket
  العظيمة النازلة الملمة الشديدة (maqayis)؛ العظيمة الملمة النازلة الفظيعة (ayn)؛ العظيمة والمعظمة النازلة الشديدة (sihah)؛ العظمية الملمة إذا أعضلت (tahdhib)؛ العظيمة النازلة (mufradat)
- **B005** kemik — kemik · kemikler
  العَظْم معروف سمي بذلك لقوته وشدته (maqayis)؛ العظام جمع العَظْم وهو قصب المفاصل (ayn)؛ العَظْم واحد العظام (sihah)؛ العَظْم بتسكين الظاء يجمع عظاما (tahdhib)؛ العَظْم جمعه عظام (mufradat)
- **B006** kibirlenip böbürlenme — kibir ve böbürlenme · kibirlenmek ve kurumlanmak · böbürlenmek
  العظمة من التعظم والزهو والنخوة (ayn)؛ استعظم وتعظم تكبر والعظمة الكبرياء (sihah)؛ العظمة التعظم والنخوة والزهو وأما عظمة العبد فهو كبره المذموم وتجبره (tahdhib)
- **B007** yadırgayıp gözünde büyütmek — yadırgamak veya ürkütücü bulmak · iş gözümde büyüdü ve beni ürküttü · söylediğin beni ürküttü · bunu yapmak gözümü korkutmaz
  استعظمته أنكرته ولا يتعاظمني ذلك أي لا يعظم في عيني (ayn)؛ استعظمت الأمر إذا أنكرته وأعظمني أي هالني وعظم علي وما يعظمني أي ما يهولني (tahdhib)
- **B008** kalçayı büyük gösteren dolgu — kalçayı büyük gösteren yastık · kalça dolgusu · kalçayı büyütme dolgusu
  الإعظامة والعظامة كالوسادة تعظم بها المرأة عجيزتها (sihah)؛ العظمة شيء تعظم به المرأة ردفها من مرفقة وغيرها والعظامة بكسر العين (tahdhib)؛ الإعظامة والعظامة شبه وسادة تعظم بها المرأة عجيزتها (mufradat)
- **B009** eyerin donanımsız ahşap iskelet parçası [kalıp] — eyerin kayışsız ve donanımsız ahşap parçası
  عظم الرحل خشبة بلا أنساع ولا أداة (sihah)؛ عظم الرجل خشبة بلا أنساع ولا أداة (tahdhib)؛ عظم الرحل خشبة بلا أنساع (mufradat)
- **B010** şerefli ve saygın bir mevki edinme — görüş ve şan bakımından yükselmek · insanlar arasında saygınlık · saygınlıklar ve dokunulmaz değerler · topluluğun ileri gelenleri
  عظم الرجل عظامة فهو عظيم في الرأي والمجد (ayn)؛ عظمة عند الناس أي حرمة يعظم لها وله معاظم مثله وعظيم المعاظم أي عظيم الحرمة وعظمات القوم سادتهم وذوو شرفهم (tahdhib)

## ك و د (root_001329): 42:5 تَكَادُ

- **B001** bir şeyi biraz güçlükle aramak — bir şeyi biraz güçlükle aradı
  التماس شيء ببعض العناء؛ كاد يكود كودا ومكادا
- **B002** eyleme ramak kalmak; olumluda yapmamak, olumsuzda güçlükle yapmak — az kalsın yapacaktı, ama yapmadı · güçlükle de olsa yaptı · az kalsın yapacaktı · bir kimse az kalsın yapacaktı
  فأما قولهم في المقاربة كاد فمعناها قارب (maqayis)؛ كاد يفعل كذا يكاد كودا ومكادة أي قارب ولم يفعل (sihah)؛ مجردة فلم يقع ذلك الشيء وقرنت بجحد فقد وقع (maqayis)؛ مجرده ينبئ عن نفي الفعل ومقرونه بالجحد ينبئ عن وقوع الفعل (sihah)
- **B003** vermeyi ya da yapmayı kesin biçimde reddetmek [kalıp] — Hayır, vermeye hiç niyetim yok. · Bunu kesinlikle yapmam. · Bunu ne önemsiyorum ne de yapmaya yanaşıyorum.
  لمن يطلب منك الشيء فلا تريد إعطاءه لا ولا مكادة (maqayis)؛ لا أفعل ذلك ولا كودا (sihah)؛ لا مهمة لي ولا مكادة أي لا أهم ولا أكاد (sihah)
- **B004** istemek, niyet etmek — ondan ne istendiği · onu gizlemek istiyorum
  عرف فلان ما يكاد منه أي ما يراد منه؛ قال بعضهم في قوله أكاد أخفيها أريد أخفيها؛ كادت وكدت وتلك خير إرادة

## ECHO ك ي د (root_001334): for 42:5 تَكَادُ: withheld observed target; not identity

- **B001** bir şeyi yoğun çabayla işleme — bir şeyi yoğun çabayla işleme ve onunla uğraşma · onu yoğun çabayla ele alıp işlemek
  يدل على معالجة لشيء بشدة (maqayis)؛ الكيد المعالجة (maqayis)؛ كل شيء تعالجه فأنت تكيده (maqayis;sihah)
- **B002** dolaylı ve gizli düzen kurma — dolaylı düzen ve tuzak · gizli ve aldatıcı düzen · birine tuzak kurmak · karşılıklı tuzak kurma yarışı · onlara kötülük etmeye kesin karar vermek · cezaya götüren süre tanıma ve erteleme
  يسمون المكر كيدا (maqayis)؛ الكيد من المكيدة وقد كاده يكيده مكيدة (ayn)؛ الكيد المكر وكاده يكيده كيدا ومكيدة وكذلك المكايدة (sihah)؛ الكيد ضرب من الاحتيال وقد يكون مذموما وممدوحا والاستدراج والمكر (mufradat)؛ لأريدن بها سوءا (mufradat)؛ الإملاء والإمهال المؤدي إلى العقاب (mufradat)
- **B003** can çekişerek can verme [kalıp] — can çekişmek ve canını vermek üzere olmak
  هو يكيد بنفسه أي يجود بها (maqayis;sihah;mufradat)؛ رأيته يكيد بنفسه أي يسوق سياقا (ayn)
- **B004** karşılaşılmayan savaş [kalıp] — savaşla karşılaşmamak
  الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا (maqayis)؛ ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا (sihah)
- **B005** karganın var gücüyle bağırması — karganın var gücüyle bağırması
  صياح الغراب بجهد (maqayis)؛ يسمى اجتهاد العرب في صياحه كيدا (sihah)
- **B006** ateşi yavaş ve güçlükle çıkarma [kalıp] — çakmak taşının ateşi yavaşça ve güçlükle çıkarması
  أن يخرج الزند النار ببطء وشدة (maqayis)؛ كاد الزند إذا تباطأ بإخراج ناره (mufradat)
- **B007** kusma ve kusmuk — kusma veya kusmuk
  الكيد القيء (maqayis)؛ وكذلك القيء (sihah)
- **B008** aybaşı görme için seyrek bir ad — kimi zaman aybaşı görme anlamında kullanılan ad
  ربما سموا الحيض كيدا (maqayis)

## ف ط ر (root_001165): 42:5 يَتَفَطَّرْنَ, 42:11 فَاطِرُ

- **B001** yarılıp açılma — yarma ve açma · yarıklar, çatlaklar veya yapı bozuklukları · kumaş yarıldı · çatlaklı ya da kesmeyen kılıç · parmağına vurup kanayacak biçimde yardı · az miktarda gelen ince cinsel sıvı; adlandırmanın hangi benzetmeye dayandığı tartışmalıdır · ne yararı ne zararı olan, anlayışı kıt adam
  أصل صحيح يدل على فتح شيء وإبرازه (maqayis)؛ انفطر الثوب وتفطر أي انشق (ayn)؛ الفطر أيضا الشق وتفطر الشيء تشقق (sihah)؛ أصل الفطر الشق (tahdhib)؛ أصل الفطر الشق طولا (mufradat)
- **B002** ilk kez var edip başlatma — Tanrı canlıları yarattı ve yapımlarını ilk kez başlattı · göklerle yeri ilk kez yaratan · kuyunun kazısını ilk kez başlattı
  الفطرة الخلقة (maqayis)؛ فطر الله الخلق أي خلقهم وابتدأ صنعة الأشياء (ayn)؛ فطره أي خلقه؛ الفطر الابتداء والاختراع (sihah)؛ فاطر السماوات والأرض؛ فطرني أي خلقني؛ أنا فطرتها أي أنا ابتدأت حفرها (tahdhib)؛ فطر الله الخلق وهو إيجاده الشيء وإبداعه (mufradat)
- **B003** doğuştan gelen temel yapı — doğuştan gelen yapı; inanç veya ilk bilgiyle yorumlanan temel yönelim · Tanrı'nın insanları üzerinde yarattığı doğuştan yapı veya yönelttiği inanç yolu
  الفطرة الخلقة (maqayis;sihah)؛ الفطرة التي طبعت عليها الخليقة من الدين (ayn)؛ الفطرة الخلقة التي يخلق عليها المولود؛ فطرة ثانية وهي الكلمة التي يصير بها العبد مسلما (tahdhib)؛ ومنه الفطرة (mufradat)
- **B004** orucu sona erdirme — orucu bırakma ve oruçsuz duruma geçme · oruçlu kişi orucunu bozdu · orucunu bozmuş veya oruç tutmayan kişi · orucun açıldığı yiyecek ya da içecek
  الفطر من الصوم؛ أفطر إفطارا وقوم فطر أي مفطرون (maqayis)؛ فطرت وأفطرت الرجل وفطرته من الفطر بمعنى ترك الصوم (ayn)؛ أفطر الصائم والاسم الفطر؛ الفطور ما يفطر عليه (sihah)؛ فطرت الصائم فأفطر؛ الفطور ما يفطر عنه (tahdhib)
- **B005** iki parmakla sağma — koyunu veya deveyi parmak uçlarıyla sağmak · sağım anında çıkan az miktarda süt · az miktarda gelen ince cinsel sıvı; adlandırmanın sağmaya mı kanlı yarılmaya mı dayandığı tartışmalıdır
  فطرت الشاة فطرا إذا حلبتها؛ الفطر يكون الحلب بإصبعين (maqayis)؛ الفطر شيء قليل من اللبن؛ فطرت الناقة أي حلبتها بأطراف الأصابع (ayn)؛ الفطر حلب الناقة بالسبابة والإبهام (sihah)؛ الفطر شيء قليل من اللبن؛ الحلب بأطراف الأصابع (tahdhib)؛ فطرت الشاة حلبتها بإصبعين (mufradat)
- **B006** olgunlaşmadan aceleye getirme — mayalanmamış veya olgunlaşmadan aceleye getirilmiş şey · hamuru ya da kili hazırlayıp bekletmeden hemen işlemek · yeterince düşünülmeden ileri sürülmüş ham görüş · deriyi yeterince işleyip doyurmadın
  فطرت العجين والطين أي عجنته واختبزته من ساعته (ayn)؛ الفطير خلاف الخمير؛ كل شيء أعجلته عن إدراكه فهو فطير (sihah)؛ فطرت العجين والطين وهو أن تعجنه ثم تخبزه من ساعته؛ أفطرت جلدك إذا لم تروه من الدباغ (tahdhib)؛ فطرت العجين إذا عجنته فخبزته من وقته (mufradat)
- **B007** devenin köpek dişinin sürmesi — devenin köpek dişi sürüp çıktı · köpek dişi çıkmış deve
  فطر ناب البعير طلع (ayn;sihah)؛ فطر ناب البعير إذا طلع؛ فطرنا به إذا بزل (tahdhib)
- **B008** bir yer mantarı türü — bir yer mantarı türü · bu türden tek bir yer mantarı
  الفطر ضرب من الكماة وهو المروزي ونحوه الواحدة بالهاء (ayn)؛ الفطر أيضا ضرب من الكمأة أبيض عظام الواحدة فطرة (sihah)؛ الفطر ضرب من الكمأة والواحدة فطرة (tahdhib)

## ف و ق (root_001188): 42:5 فَوْقِهِنَّ

- **B001** üstte bulunma — üstünde; yukarıda
  الفوق نقيض التحت (ayn;sihah;tahdhib)؛ الأول الفوق وهو العلو (maqayis)؛ فوق يستعمل في المكان والزمان والجسم (mufradat)؛ باعتبار العلو وباعتبار الصعود والحدور (mufradat)؛ يفوق السطح أي يعلوه (ayn)؛ يفوق سطحا أي يعلوه (tahdhib)
- **B002** değer ve mertebe üstünlüğü — derece ve erdem bakımından üstün · saygınlık ve değer bakımından arkadaşlarını aşmak · güzelliğiyle öne çıkan genç kadın · niteliği veya değeri çok yüksek · kısa bir sağım aralığı kadar bekleyerek veya paylaştırmada birini üstün tutarak
  فلان يفوق قومه أي يعلوهم (ayn;tahdhib)؛ جارية فائقة الجمال أي فاقت في الجمال (ayn;tahdhib)؛ فاق الرجل أصحابه يفوقهم أي علاهم بالشرف (sihah)؛ أمر فائق أي مرتفع عال (maqayis)؛ باعتبار الفضيلة الدنيوية أو الأخروية (mufradat)؛ الفوق أعلى الفضائل (tahdhib)
- **B003** baskın ve egemen olma — üzerinde egemen ve baskın
  السادس باعتبار القهر والغلبة؛ وهو القاهر فوق عباده؛ وإنا فوقهم قاهرون
- **B004** bir ölçü sınırını aşma — bir sayıdan, nicelikten veya ölçüden daha ileride
  يقال في العدد نحو فإن كن نساء فوق اثنتين (mufradat)؛ في الكبر والصغر مثلا ما بعوضة فما فوقها (mufradat)؛ فما فوقها قال أبو عبيدة فما دونها أي أعظم منها (sihah)؛ من قال أراد ما دونها فإنما قصد هذا المعنى وتصور بعض أهل اللغة أنه يعني أن فوق يستعمل بمعنى دون وهذا توهم منه (mufradat)
- **B005** bilincin veya gücün geri gelmesi — ayılmak veya yeniden güç kazanmak · hiçbir geri dönüşü, arası, dinlenmesi veya beklemesi olmamak · kuraklıktan sonra yeniden verimli olmak
  فواق ناقة بمعنى الإفاقة كإفاقة المغشي عليه أفاق يفيق إفاقة وفواقا (ayn;tahdhib)؛ كل مغشي عليه أو سكران إذا انجلى عنه ذلك قيل أفاق واستفاق (ayn)؛ استفاق من مرضه ومن سكره وأفاق بمعنى (sihah)؛ الإفاقة رجوع الفهم إلى الإنسان بعد السكر أو الجنون والقوة بعد المرض (mufradat)؛ ما لها من فواق أي ما لها من رجوع ولا مثنوية ولا ارتداد (maqayis)؛ أي ما لها من نظرة وراحة وإفاقة (sihah;tahdhib)؛ أفاق الزمان إذا أخصب بعد جدب (tahdhib)
- **B006** sağım arası süt dönüşü — devenin memesinde sütün yeniden birikmesi veya iki sağım arasındaki süre · iki sağım arasında memede biriken süt · devenin memesi yeniden sütle dolmak ve sağım vakti gelmek · kısa bir sağım aralığı kadar bekleyerek veya paylaştırmada birini üstün tutarak
  فواق الناقة رجوع اللبن في ضرعها بعد حلبها (ayn;tahdhib;maqayis)؛ ما بين الحلبتين من الوقت (sihah;mufradat)؛ كلما اجتمع من الفواق درة فاسمها الفيقة (ayn;tahdhib)؛ الفيقة ما اجتمع من الدرة في الضرع والأصل الواو (maqayis:2694)؛ أفاقت الناقة واستفاقها أهلها إذا نفسوا حلبها حتى تجتمع درتها (ayn;tahdhib)
- **B007** aralıklı küçük paylarla alma — yavruya sütü aralıklı küçük paylarla içirmek · yavrunun sütü ara ara içmesi · bir şeyi tek seferde değil, parça parça ve ara vererek almak veya okumak · azar azar alınan yiyecek veya içecek · içmeye hiç ara vermemek
  فوقت الفصيل أي سقيته اللبن فواقا فواقا وتفوق الفصيل إذا شرب اللبن كذلك (sihah)؛ أتفوقه تفوق اللقوح أي أقرأ منه شيئا بعد شيء (sihah;tahdhib;maqayis)؛ المفوق الذي يؤخذ قليلا قليلا من مأكول أو مشروب (tahdhib)؛ فوق فصيلك أي اسقه ساعة بعد ساعة وظل يتفوق المخض (mufradat)؛ لا يستفيق من الشراب أي لا يجعل لشربه وقتا (tahdhib)؛ خرجنا بعد أفاويق من الليل أي بعدما تمضي عامة الليل (tahdhib)
- **B008** bulut suyunun aralıklı yağış payları — bulutta biriken su veya ara ara yağan yağmur payları
  الأفاويق ما اجتمع من الماء في السحاب (ayn;maqayis)؛ الأفاويق أيضا ما اجتمع في السحاب من ماء فهو يمطر ساعة بعد ساعة (sihah)؛ أفاويق السحابة مطرها مرة بعد مرة (tahdhib)
- **B009** okun kiriş kertiği — okun kirişe oturan arka kertiği · okların kiriş kertikleri · ok kertiği adının sesçe çevrilmiş çoğul biçimi · kiriş kertiği eğri veya kırık ok · oka kiriş kertiği açmak veya kertiği düzeltmek · eksik bir payla veya sonuç alamadan dönmek
  الفوق مشق السهم حيث يقع الوتر (ayn;tahdhib)؛ الفوق موضع الوتر من السهم والجمع أفواق وفوق (sihah)؛ فوق السهم وسمى لأن الوتر يجعل فيه كأنه قد رد فيه والجمع أفواق (maqayis)؛ من فوق يشتق فوق السهم وسهم أفوق انكسر فوقه (mufradat)؛ سهم أفيق وأفوق إذا كان في الفوق ميل أو انكسار (ayn)؛ الأفوق السهم المكسور الفوق (sihah;tahdhib)؛ رجع فلان بأفوق ناصل أي بسهم منكسر لا نصل فيه (sihah;tahdhib)؛ الفقي ملين فجمع فوق وهو مقلوب وليس من هذا الباب (maqayis:2641)
- **B010** göğüsten yükselen kesik soluk — baskın hıçkırık veya göğüsten yükselen kesik soluk · son nefesini vermek üzere olmak
  الفواق ترجيع الشهقة الغالبة (ayn;tahdhib)؛ يفوق فواقا وفؤوقا (ayn;tahdhib)؛ وفاق الرجل فواقا إذا شخصت الريح من صدره (sihah)؛ فلان يفوق بنفسه فؤوقا إذا كانت نفسه على الخروج (sihah)؛ الفواق الذي يأخذ الإنسان عند النزع وكذلك الريح التي تشخص من صدره (sihah)؛ الفوق نفس الموت (tahdhib)؛ مما شذ عن هذين الأصلين قولهم هو يفوق بنفسه وهذا من باب الإبدال وإنما أصله يسوق (maqayis)
- **B011** yoksulluk ve gereksinim içinde olma — yoksulluk ve gereksinim · yoksullaşmak ve gereksinim içine düşmek
  الفاقة الحاجة ولا فعل لها (ayn;tahdhib)؛ الفاقة الفقر والحاجة وافتاق الرجل أي افتقر (sihah)؛ يقال من الفاقة إنه لمفتاق ذو فاقة (tahdhib)
- **B012** özel adlandırma kümesi — yemek dolu büyük kap; ayrıca pişmiş yağ, yağ veren bir ağaç veya çöl ve arazi için aktarılan ad
  الفاق الجفنة المملوءة طعاما (ayn;tahdhib)؛ الفاق الزيت المطبوخ (tahdhib)؛ الفاق البان (tahdhib)؛ الفاق الصحراء وقال مرة هي أرض (tahdhib)
- **B013** özel adlandırma kümesi — baş ile boynun birleşme yeri · erkeklik organının üst bölümü · her dişinde ok gezi gibi iki kertik bulunan çark
  الفائق موصل العنق في الرأس (sihah)؛ فوق الذكر أعلاه (tahdhib)؛ محالة فوقاء إذا كان لكل سن منها فوقان مثل فوقي السهم (tahdhib)

## م ل ك (root_001444): 42:5 وَٱلْمَلَٰٓئِكَةُ, 42:49 مُلْكُ

- **B001** güçlü ve tutarlı biçimde bir arada durma — hamuru sıkıca yoğurup kıvamlandırmak · sürgünü kabuğuyla kurutup sertleştirmek · kendini tutmak; dayanmak · bir şeyi ayakta tutan iç sağlamlık
  أصل صحيح يدل على قوة في الشيء وصحة (maqayis)؛ أملك عجينه قوي عجنه وشده (maqayis)؛ ملكت العجين إذا شددت عجنه (sihah)؛ ملك النبعة صلبها (sihah)؛ العجين إذا كان متماسكا متينا مملوك ومملك (tahdhib)؛ حائط ليس له ملاك أي تماسك (mufradat)
- **B002** sahiplik ve tasarruf yetkisi — bir şeye sahip olup onu tasarrufunda bulundurmak · mülkiyet; sahip olunan mal veya hak · kişinin elinin altında ve sahipliğinde bulunan şey · köleleştirilmiş kişi · köleleştirilmiş kişilere iyi davranma · özgür doğmuşken tutsak edilip köleleştirilen kişi · boşanma kararını eşin tasarrufuna bırakmak
  ملك الإنسان الشيء يملكه ملكا (maqayis)؛ الملك ما ملكت اليد من مال وخول (ayn;tahdhib)؛ ملكت الشيء أملكه ملكا (sihah)؛ وملكه المال والملك فهو مملك (sihah)؛ أملكت فلانة أمرها إذا جعل أمر طلاقها بيدها (tahdhib)؛ المملوك يختص في التعارف بالرقيق من الأملاك (mufradat)
- **B003** hükümdarlık ve kamusal egemenlik — hükümdar · hükümdar; egemen yönetici · hükümranlık; kamusal egemenlik · ilahi mutlak hükümranlık · hükümdarın yönetim alanı ve ülkesi · birini başlarına hükümdar yapmak
  والاسم الملك لأن يده فيه قوية صحيحة (maqayis)؛ الملك لله المالك المليك (ayn)؛ الملكوت ملك الله وملكوت الله سلطانه (ayn)؛ الملكوت من الملك (sihah)؛ المملكة سلطان الملك في رعيته (ayn;tahdhib)؛ له ملكوت العراق وعزه وسلطانه وملكه (tahdhib)؛ الملك هو المتصرف بالأمر والنهي في الجمهور (mufradat)؛ ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا (tahdhib)
- **B004** evlilik akdi kurma — evlilik akdi; evlendirme · kadınla evlenmek
  كنا في إملاك فلان أي أملكناه امرأته (maqayis)؛ الإملاك التزويج قد أملكوه وملكوه أي زوجوه (ayn)؛ ملكت المرأة تزوجتها (sihah)؛ أملكنا فلانا فلانة إذا زوجناه إياها (sihah)؛ شهدنا إملاك فلان وملاكه وملاكه (tahdhib)؛ الملاك التزويج وأملكوه زوجوه (mufradat)
- **B005** işi ayakta tutan temel dayanak [kalıp] — işin dayandığı temel unsur · kalp bedenin temel dayanağıdır
  ملاك الأمر ما يعتمد عليه (ayn)؛ القلب ملاك الجسد (ayn;sihah;mufradat)؛ هذا ملاك الأمر وملاكه أي صلاحه (tahdhib)
- **B006** yolun veya yerin orta ya da ana kesimi — yolun ortası veya ana kesimi · vadinin sınırı veya orta kesimi · yerleşimin ortası veya büyük kesimi
  ملك الطريق أيضا وسطه (sihah)؛ خل عن ملك الطريق وملك الوادي وملكه وملكه أي حده ووسطه (tahdhib)؛ الزم ملك الطريق أي وسطه (tahdhib)؛ أراد بالمملكة وسطها وملك الطريق معظمه ووسطه (tahdhib)
- **B007** işleri ve yaşamı sürdüren su kaynağı [kalıp] — işini yürütmesini sağlayan su · hiç suyu yok · sularımız geçimimizi ayakta tutar
  والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)؛ الماء ملك أمر أي يقوم به الأمر (sihah)؛ الماء ملك أمره (tahdhib)؛ الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر (tahdhib)؛ ماله ملك ولا نقر أي ما له ماء (tahdhib)؛ مياهنا ملوكنا ومات فلان عن ملوك كثيرة (tahdhib)
- **B008** hayvanlarda önden gidip yön veren unsur [kalıp] — arı topluluğunun önderi · bineğin ön ayakları ve yönlendirici kısmı · deve ve koyun sürüsünün öncüsü
  مليك النحل يعسوبها (sihah)؛ ملك الدابة قوائمها وهاديها (sihah;tahdhib)؛ جاءنا تقوده ملكه يعني قوائمه وهاديه (tahdhib)؛ ملك الإبل والشاء ما يتقدم ويتبعه سائره (mufradat)
- **B009** ilahi haberci varlık — 
  الملك واحد الملائكة إنما هو تخفيف الملأك والأصل مألك (ayn)؛ مألك من الألوك وهو الرسالة (ayn)؛ الملك من الملائكة واحد وجمع (sihah)؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة (sihah)؛ الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك (tahdhib)

## س ب ح (root_000666): 42:5 يُسَبِّحُونَ

- **B001** Tanrı'yı yücelterek anma ve kulluk — dua ve anma biçimindeki gönüllü kulluk · Tanrı'yı sözle, eylemle veya niyetle yüceltme ve anma
  السُّبحة وهي الصلاة (maqayis)؛ التسبيح يكون في معنى الصلاة (ayn)؛ سبح الرجل تسبيحا إذا عظم الله ومجده (jamhara)؛ السبحة التطوع من الذكر والصلاة (sihah)؛ السبحة من الصلاة التطوع (tahdhib)؛ التسبيح عاما في العبادات قولا كان أو فعلا أو نية (mufradat)
- **B002** Tanrı'yı her türlü eksiklikten uzak sayma — Tanrı her türlü kötülük ve eksiklikten uzaktır · Tanrı'yı her türlü kötülük ve eksiklikten uzak sayarak yüceltme · şaşma veya söz konusu kişiyi bir iddiadan uzak tutma sözü · her türlü kötülükten ve kendisine yakışmayan nitelikten uzak olan Tanrı
  التسبيح وهو تنزيه الله من كل سوء (maqayis)؛ سبحان الله تنزيه لله (ayn)؛ سبحان تنزيه وتبرئة (jamhara)؛ التسبيح التنزيه (sihah)؛ سبحان في اللغة تنزيه لله عز وجل عن السوء (tahdhib)؛ التسبيح تنزيه الله تعالى (mufradat)
- **B003** Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı — Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı · yere kapanma yerleri
  السبحات جلال الله وعظمته (maqayis)؛ سبحات وجه ربنا يعني جلاله وعظمته ونوره (ayn)؛ سبحات وجهه نور وجهه (jamhara)؛ سبحات وجه ربنا أي جلالته (sihah)؛ سبحات وجهه نور وجهه؛ السبحات مواضع السجود (tahdhib)
- **B004** yüzerek veya akıcı biçimde hızla ilerleme — yüzme ve su ya da havada hızla ilerleme · yıldızların yörüngede akıp ilerlemesi · ön ayaklarını ileri uzatarak koşan at · yörüngede ya da koşuda hızla akıp gidenler
  السَّبح والسباحة العوم في الماء (maqayis)؛ السبح مصدر كالسباحة سبح السابح في الماء (ayn)؛ سبح الرجل وغيره في الماء سبحا وسباحة (jamhara)؛ السباحة العوم (sihah)؛ النجوم تسبح في الفلك؛ السابح من الخيل يمد يديه في الجري (tahdhib)؛ السبح المر السريع في الماء وفي الهواء (mufradat)
- **B005** iş ve geçim için zaman ve hareket imkânı — serbest zaman, geçim için hareket ve gidip gelme imkânı · yeryüzünde uzaklara gitmek · sözü uzatıp çok konuşmak
  أصلان أحدهما جنس من العبادة والآخر جنس من السعي (maqayis)؛ سبحا طويلا أي فراغا للنوم (ayn)؛ السبح الفراغ والتصرف في المعاش والمنقلب والجيئة والذهاب (sihah)؛ فراغا وتصرفا؛ اضطرابا ومعاشا؛ منقلبا طويلا (tahdhib)؛ سرعة الذهاب في العمل (mufradat)
- **B006** anma sözlerini saymaya yarayan boncuk dizisi — Tanrı'yı anma sözlerini saymaya yarayan boncuk dizisi
  السبحة خرزات يسبح بعدها (ayn)؛ السبحة بالضم خرزات يسبح بها (sihah)؛ الخرزات التي يعد بها المسبح تسبيحه السبحة وهي كلمة مولدة (tahdhib)؛ الخرزات التي بها يسبح سبحة (mufradat)
- **B007** çocuk deri giysisi; güçlü ve sıkı örtü — çocuklar için deriden yapılmış gömlek veya giysi · güçlü, sağlam ve sıkı örtü
  السبحة قميص يعمل للصبيان من جلود وسلف رقيق والجمع سباح (jamhara)؛ السبحة بفتح السين وجمعها سباح ثياب من جلود؛ السباح قمص للصبيان من جلود؛ كساء مسبح أي قوي شديد (tahdhib)
- **B008** kutsal kent veya hac bölgesindeki bir vadinin adı — kutsal kent ya da hac sırasında durulan bölgedeki bir vadinin adı
  سَبّوحة البلد الحرام ويقال واد بعرفات (sihah)

## ح م د (root_000355): 42:5 بِحَمْدِ, 42:28 ٱلْحَمِيدُ

- **B001** yermenin karşıtı olan, iyilik için teşekkürü de kapsayan övgü — yermenin karşıtı olan övgü; iyilik için teşekkür de içerebilir · birini, yaptığı övülesi bir işten dolayı övmek · övgü; yerginin karşıtı · Tanrı'yı güzel sözlerle çokça övme · onun için övgü ve teşekkür · övülecek bir iş yapmak ya da sonunda övgü kazanmak · her şeyi çokça, kimi zaman olduğundan fazla öven kimse · çok öven kimse · seni överek başlarım
  الحمد نقيض الذم (maqayis;ayn;jamhara;sihah;tahdhib)؛ الحمد الثناء (ayn;tahdhib;mufradat)؛ الحمد أعم من الشكر (sihah;mufradat)؛ التحميد كثرة حمد الله بحسن المحامد (ayn;tahdhib)
- **B002** deneyip övülesi ya da uygun bulma — birini deneyip övgüye değer bulmak · bir yeri yerleşmeye ya da otlatmaya elverişli bulmak · bu işi benim için uygun buluyor musun? · idrar kanalını yıkamayı sizin için uygun bulmak
  أحمدت فلانا إذا وجدته محمودا (maqayis;ayn;sihah;tahdhib)؛ أحمدت الأرض إذا رضيت سكناها أو مرعاها (jamhara;sihah)؛ هل تحمد لي هذا الأمر أي هل ترضاه لي (tahdhib)
- **B003** övülen veya birçok övülesi niteliği bulunan kimse — övülen, övgüye değer · çokça övülen, birçok övülesi niteliği bulunan · övülmeye daha çok layık olan ya da daha çok öven · övülen; bağlama göre öven
  رجل محمود ومحمد إذا كثرت خصاله المحمودة (maqayis;sihah)؛ محمد كأنه حمد مرة بعد أخرى (jamhara)؛ فلان محمود إذا حمد ومحمد إذا كثرت خصاله المحمودة (mufradat)؛ الحميد بمعنى المحمود (tahdhib;mufradat)
- **B004** övülesi işin varılabilecek en ileri sınırı — yapabileceğinin en ilerisi ve övülecek olanı · aktarılan sözde kadınlarda övülebilecek niteliklerin en ileri derecesi
  حماداك أن تفعل كذا أي غايتك وفعلك المحمود (maqayis)؛ حماداك أن تفعل كذا أي حمدك (ayn;tahdhib)؛ حماداك في معنى قصاراك (jamhara;sihah)؛ حماديات النساء معناه غاية ما يحمد منهن (tahdhib)؛ حماداك أي غايتك المحمودة (mufradat)
- **B005** iyiliğini başa kakıp kendine pay çıkarma [kalıp] — iyiliğini insanların başına kakıp bununla övgü beklemek
  فلان يتحمد علي أي يمن (sihah)؛ من أنفق ماله على نفسه فلا يتحمد به إلى الناس (sihah;tahdhib)
- **B006** muhatabı katarak övme veya iyilikleri teşekkürle anma [kalıp] — seninle birlikte Tanrı'yı övmek veya onun iyiliklerini sana teşekkürle anmak
  أحمد إليك الله أي معك (ayn;tahdhib)؛ أشكر إليك أياديه ونعمه (tahdhib)

## ر ب ب (root_000532): 42:5 رَبِّهِمْ, 42:10 رَبِّى, 42:14 رَّبِّكَ, 42:15 رَبُّنَا, 42:15 وَرَبُّكُمْ, 42:16 رَبِّهِمْ, 42:22 رَبِّهِمْ, 42:36 رَبِّهِمْ, 42:38 لِرَبِّهِمْ, 42:47 لِرَبِّكُم

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## ECHO ر ب و (root_000537): for 42:5 رَبِّهِمْ, 42:10 رَبِّى, 42:14 رَّبِّكَ, 42:15 رَبُّنَا, 42:15 وَرَبُّكُمْ, 42:16 رَبِّهِمْ, 42:22 رَبِّهِمْ, 42:36 رَبِّهِمْ, 42:38 لِرَبِّهِمْ, 42:47 لِرَبِّكُم: withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

## غ ف ر (root_001096): 42:5 وَيَسْتَغْفِرُونَ, 42:5 ٱلْغَفُورُ, 42:23 غَفُورٌ, 42:37 يَغْفِرُونَ, 42:43 وَغَفَرَ

- **B001** koruyucu biçimde örtme — örtme ve koruyucu biçimde kaplama · başı koruyan zincir örgülü zırh başlığı · baş yağı bulaşmasın diye başörtüsünün altına konan bez · yay kirişinin geçtiği çentiği örten yama · alttaki bulutu örten üst bulut · eşyayı bir kaba koymak · boyanın kumaşı kiri daha iyi gizler duruma getirmesi · işi gereken biçimde örtüp düzeltmek · enseden sarkan saçı örtmek
  الغفر الستر (maqayis)؛ أصل الغفر التغطية (ayn)؛ الغفر: التغطية (sihah)؛ الغفر: إلباس ما يصونه عن الدنس (mufradat)؛ المغفر وقاية للرأس (ayn)؛ المغفر: زرد ينسج من الدروع على قدر الرأس (sihah)؛ اغفروا هذا الأمر بغفرته أي استروه بما يجب أن يستر به (mufradat)
- **B002** suçu bağışlayıp cezadan koruma — suçu bağışlama ve ceza sonucundan koruma · suçu bağışlayıp cezasını kaldırma · Tanrı'nın suçu bağışlayıp kulunu cezadan koruması · suçu bağışlama · Tanrı'nın onun suçunu bağışlaması · onu bağışlamak · Tanrı'dan bağışlanma dilemek · suçu bağışlamak · çok bağışlayan · sürekli ve çok bağışlayan · içlerinde kimsenin suçunu bağışlayan yok
  الغفران والغفر بمعنى (maqayis)؛ الله الغفور الغفار يغفر الذنوب مغفرة وغفرانا وغفرا (ayn)؛ استغفر الله لذنبه ومن ذنبه فغفر له ذنبه مغفرة وغفرا وغفرانا (sihah)؛ المغفرة من الله هو أن يصون العبد من أن يمسه العذاب (mufradat)
- **B003** yüzeyi kaplayan ince tüy veya kumaş havı — kumaşın havı kalkıp yüzünü kaplamak · kumaş havı ya da bedendeki ince tüy · ince tüy · enseden aşağı sarkan saç · enseden sarkan saçı örtmek
  غفر الثوب إذا ثار زئبره وهو من الباب لأن الزئبر يغطي وجه الثوب (maqayis)؛ غفر الثوب إذا ثار زئبره غفرا (ayn)؛ الغفر أيضا شعر كالزغب يكون على ساق المرأة والجبهة ونحو ذلك؛ والغفر أيضا زئبر الثوب (sihah)
- **B004** yaranın veya hastanın yeniden kötüleşmesi [kalıp] — yara yeniden kötüleşti · hasta yeniden kötüleşti
  الغفر النكس في المرض (maqayis)؛ غفر الجرح يغفر غفرا: نكس، وكذلك المريض (sihah)
- **B005** dağ keçisi yavrusu ve annesi — dağ keçisi yavrusu · yavrunun annesi olan dişi dağ keçisi · dağ keçisi yavrusunun annesi
  الغفر ولد الأروية وأمه مغفر (maqayis)؛ الغفر ولد الأروية؛ والمغفر الأروية ويقال لها أم غفر (ayn)؛ الغفر بالضم: ولد الأروية، والجمع الأغفار، وأمه مغفرة (sihah)
- **B006** Ay'ın konaklarından olan üç küçük yıldız — Ay'ın konaklarından olan üç küçük yıldız
  الغفر من منازل القمر (ayn)؛ الغفر: ثلاثة أنجم صغار ينزلها القمر، وهي من الميزان (sihah)
- **B007** ağaçtan çıkan veya toplanan ürün — ağaçtan çıkan ürün; reçine benzeri madde veya tatlı kurt · ağaçtan çıkan ve toplanan ürünler · ağaç ürünlerini aramaya çıkmak · ağaç ürünü toplamaya çıkmak
  المغفور فشىء يشبه بالصمغ يخرج من العرفط (maqayis)؛ المغفور دود يخرج من العرفط حلو يضيح بالماء فيشرب؛ وصمغ الإجاصة مغفور (ayn)؛ ما أحسن مغافير هذا الرمث؛ خرجنا نتمغفر؛ خرجنا نتغفر، إذا خرجوا يجتنونه من شجرة (sihah)
- **B008** bütün topluluğun kalabalık ve eksiksiz gelişi [kalıp] — bütün topluluk, kalabalık ve kimse eksik olmadan · bütün toplulukla birlikte · hep birlikte ve kalabalık olarak
  جاء القوم جماء الغفير أي بلفهم ولفيفهم (ayn)؛ جاءوا جماء غفيراء؛ والجماء الغفير، وجم الغفير، وجماء الغفير، أي جاءوا بجماعتهم: الشريف والوضيع، ولم يتخلف أحد، وكانت فيهم كثرة (sihah)

## ر ح م (root_000552): 42:5 ٱلرَّحِيمُ, 42:8 رَحْمَتِهِۦ, 42:28 رَحْمَتَهُۥ, 42:48 رَحْمَةً

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ء خ ذ (root_000018): 42:6 ٱتَّخَذُوا۟, 42:9 ٱتَّخَذُوا۟

- **B001** ele geçirip edinme — nesneyi ele geçirip almak · al · söylediğimi dinle, kuşkuyu ve çekişmeyi bırak · yuları tut · alma eylemini yoğunluk bildiren kalıpla anlatan biçim
  الأصل حوز الشيء وجبيه وجمعه (maqayis)؛ الأخذ التناول (ayn)؛ أخذت الشئ آخذه أخذا تناولته (sihah)؛ خلاف العطاء وهو التناول (tahdhib)
- **B002** suçundan sorumlu tutma [kalıp] — onu suçundan ötürü hesaba çekip cezalandırdı
  آخذه بذنبه مؤاخذة (sihah)
- **B003** yakalayıp tutsak etme — tutsak edilmiş kişi · falanca yakalanıp tutsak edildi · onları tutsak edin
  الأخيذ الأسير والمرأة أخيذة (sihah)؛ ومن هنا قيل للأسير أخيذ وقد أخذ فلان إذا أسر وخذوهم معناه ائسروهم (tahdhib)
- **B004** büyüsel yolla etkileyip engelleme — gözü ve benzeri durumları etkilediğine inanılan sözlü uygulama veya büyüsel nesne · eşi başka kadınlarla birleşmekten büyüsel yollarla alıkoyma · kadınlarla birleşmekten büyüsel yolla alıkonmuş
  الأخذة رقية تأخذ العين ونحوها والمؤخذ الرجل كأنه حبس (maqayis)؛ الأخذة رقية تأخذ العين ورجل مؤخذ عن النساء (ayn)؛ الأخذة رقية كالسحر أو خرزة تؤخذ بها النساء الرجال من التأخيذ (sihah)؛ التأخيذ حيل من السحر تمنع الزوج من جماع غيرها (tahdhib)
- **B005** sahiplenilip işletilen arazi — kişinin kendisi için sahiplenip denetimine aldığı arazi
  الإخاذة الضيعة يتخذها الإنسان لنفسه (ayn)؛ الاخاذة والاخاذ أرض يجوزها الرجل لنفسه أو السلطان (sihah)؛ الإخاذة الأرض يأخذها الرجل فيحوزها لنفسه ويتخذها ويحييها (tahdhib)
- **B006** su tutan çukur veya havuz — suyu günlerce tutan birikme yeri, havuz veya çukur
  الإخاذ مجمع الماء شبيه بالغدير (maqayis)؛ الإخاذة والإخذ ما حفرت لنفسك كهيئة الحوض تمسك الماء أياما (ayn)؛ الاخاذة شئ كالغدير والجمع إخاذ (sihah)؛ الإخذ صنع الماء يجتمع فيه (tahdhib)
- **B007** bedende bir durumun baş gösterip etkisini göstermesi — süt emen yavru fazla sütten rahatsızlandı · deve veya koyunda deliliğe benzer bir hal başladı · gözü yangılandı · hastalık veya göz ağrısı yüzünden başını eğip çökmüş kişi · yağ tutmaya başlamış deve
  الأدواء تسمى بهذا لأخذها الإنسان واستأخذ الرمد فيه (maqayis)؛ الأخذ من الإبل حين يأخذ فيه السمن وأخذ البعير كهيئة الجنون ومريض مستأخذ (ayn)؛ أخذ الفصيل اتخم من اللبن ورجل أخذ أي رمد والمستأخذ لمطأطئ رأسه من رمد أو وجع (sihah)؛ بعينه أخذ وهو الرمد وأخذ البعير كهيئة الجنون والفصيل اتخم من اللبن (tahdhib)
- **B008** ay konaklarının yıldızları [kalıp] — ayın her gece birinde bulunduğu ay konaklarının yıldızları
  نجوم الأخذ منازل القمر لأن القمر يأخذ كل ليلة في منزل (maqayis)؛ نجوم الأخذ منازل القمر لأن القمر يأخذ كل ليلة في منزل منها (sihah)؛ نجوم الأخذ هي نجوم منازل القمر لأخذ القمر في منازلها (tahdhib)
- **B009** bir topluluğun yolunu ve özelliklerini benimseme [kalıp] — bizim yolumuzu, tutumumuzu ve özelliklerimizi benimseyip izledi
  لو كنت منا لأخذت بإخذنا أي بخلائقنا وشكلنا (sihah)؛ لأخذت بإخذنا أي بشكلنا وهدينا ومن أخذ إخذهم أي من سار سيرهم (tahdhib)
- **B010** kendisi için edinip kazanma — bir şeyi kendisi için edinmek veya kazanmak · mal edindim veya kazandım · bunun karşılığında ücret alırdım
  الإتخاذ من تخذ يتخذ تخذا وتخذت مالا أي كسبته (ayn)؛ الاتخاذ افتعال من الأخذ وتخذ يتخذ (sihah)؛ اتخذ فلان مال الله دولا وتخذت مالا أي كسبته ولو شئت لتخذت عليه أجرا (tahdhib)
- **B011** güreşte kavrayıp kilitleme [kalıp] — topluluk karşılıklı kavrayarak dövüştü veya güreşti · güreşçinin rakibini kilitlediği kavrama tutuşu
  ائتخذوا في القتال أي أخذ بعضهم بعضا (sihah)؛ ائتخذ القوم إذا تصارعوا فأخذ كل واحد على مصارعه أخذة يعتقله بها (tahdhib)
- **B012** kancalı aracın tutamağı [kalıp] — kancalı aracın sapı ve tutamağı
  إخاذة الحجنة مقبضها وهي ثقافها (tahdhib)

## د و ن (root_000502): 42:6 دُونِهِۦٓ, 42:9 دُونِهِۦٓ, 42:31 دُونِ, 42:46 دُونِ

- **B001** yakın, aşağı ya da hedefin gerisinde olma — yakın; altında; hedefin gerisinde · bu, ötekinden daha yakındır · yaklaş
  أصل واحد يدل على المداناة والمقاربة (maqayis)؛ دون نقيض فوق وهو تقصير عن الغاية (sihah)؛ أدن دونك أي اقترب (tahdhib)؛ يقال للقاصر عن الشيء دون (mufradat)
- **B002** değersiz, önemsiz veya aşağı olma — değersiz, aşağılık ve önemsiz · küçümseme bildiren küçültülmüş biçim · aşağılık, bayağı · değeri yakın ya da düşük sayılan iş veya kumaş
  إذا أردت تحقيره قلت دوين والشيء الدون أي الهين (maqayis)؛ الدون الحقير الخسيس (sihah)؛ الأدون الدنيء (mufradat)
- **B003** başkası ya da daha aşağıda olan [kalıp] — sizin düzeyinize ulaşmamış olanlar · bundan daha azı veya bunun dışındakiler · Tanrı'dan başkası ya da O'na ulaşmak için aracı sayılan şey · ondan başkası veya onun buyruğu dışında olan
  ممن لم يبلغ منزلته منزلتكم؛ ما كان أقل من ذلك وقيل ما سوى ذلك؛ من دون الله أي غير الله
- **B004** buyur, bunu al — buyur, bunu al
  في الإغراء دونكه أي خذه أقرب منه وقربه منك (maqayis)؛ في الاغراء بالشئ دونكه ودونكموه (sihah)؛ يغرى بلفظ دون فيقال دونك كذا أي تناوله (mufradat)
- **B005** kayıt defteri ve kayıtları düzenleme — kayıt defteri veya kayıtların tutulduğu yer · kayıtları yazıya geçirip düzenledim
  الديوان أصله دوان فعوض من إحدى الواوين لأنه يجمع على دواوين؛ وقد دونت الدواوين
- **B006** zayıflamak (aktarımı tartışmalı) — 
  دان يدون دونا إذا ضعف (maqayis;mufradat)؛ يروى لم يدن وغيره يرويه لم يدن بتشديد النون من دنى يدنى أي ضعف (sihah)

## و ل ي (root_001684): 42:6 أَوْلِيَآءَ, 42:8 وَلِىٍّ, 42:9 أَوْلِيَآءَ, 42:9 ٱلْوَلِىُّ, 42:28 ٱلْوَلِىُّ, 42:31 وَلِىٍّ, 42:44 وَلِىٍّ, 42:46 أَوْلِيَآءَ

- **B001** aralıksız yakınlık — yakınlık ve bitişiklik · sana yakın veya yanında olan şey · bir eve bitişik olan ev
  أصل صحيح يدل على قرب؛ الولي القرب؛ جلس مما يليني أي يقاربني (maqayis)؛ دار فلان ولي دار فلان؛ الدار ولية أي قريبة (jamhara)؛ الولي القرب والدنو؛ كل مما يليك أي مما يقاربك (sihah)؛ الولي القرب (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما؛ يستعار ذلك للقرب (mufradat)
- **B002** kesintisiz ardışıklık — kesintisiz sıra · araya kesinti girmeden peş peşe oluş · şeyleri veya işleri peş peşe getirme · iki şeyi peş peşe getirmek · peş peşe isabet eden üç ok
  يوالي بين رميتين أو فعلين؛ أصبته بثلاثة أسهم ولاء؛ على الولاء أي الشيء بعد الشيء (ayn)؛ واليت بين الشيئين؛ افعل هذا على الولاء أي مرتبا (maqayis)؛ واليت بين الشيئين موالاة وولاء (jamhara)؛ والى بينهما ولاء أي تابع؛ على الولاء أي متتابعة؛ توالى عليه شهران (sihah)؛ الموالاة المتابعة؛ بثلاثة أسهم ولاء أي تباعا؛ توالت إلي كتب فلان (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما (mufradat)
- **B003** bir işi üstlenip yönetme — yönetim ve yetki alanı · bir yeri veya işi yöneten kişi · başkasının işlerinden sorumlu kişi · bir işi üstlenmek
  الولاية مصدر الوالي (ayn)؛ كل من ولى أمر آخر فهو وليه (maqayis)؛ الولاية الإمارة (jamhara)؛ ولي الوالي البلد؛ تولى العمل أي تقلد؛ الولاية بالكسر السلطان (sihah)؛ الولاية التي بمنزلة الإمارة؛ ولي اليتيم الذي يلي أمره؛ ولي المرأة؛ وليت فلانا عمل ناحيته؛ توليت الأمر توليا (tahdhib)؛ الولاية تولي الأمر؛ حقيقته تولي الأمر (mufradat)
- **B004** yakın durup destek olma — dost, seven veya destekleyen kişi · destekçi, anlaşmalı dost veya yakın yoldaş · birini sevip destekleme veya kayırma · birini sevmek, desteklemek veya kayırmak
  المولى الحليف والولي؛ الموالاة اتخاذ المولى (ayn)؛ المولى الصاحب والحليف والناصر؛ كل هؤلاء من الولي وهو القرب (maqayis)؛ الولي خلاف العدو (jamhara)؛ الولى ضد العدو؛ المولى الناصر والحليف؛ الموالاة ضد المعاداة (sihah)؛ الولي التابع المحب؛ الولاية من النصرة والنسب؛ الولاية على الإيمان؛ المولى في الدين؛ الناصر؛ والى فلان فلانا إذا أحبه؛ فيواليه أي يحابيه (tahdhib)؛ يستعار للقرب من حيث الدين والصداقة والنصرة والاعتقاد؛ الولاية النصرة (mufradat)
- **B005** özel yakınlık ve bağlılık bağı — özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi · özgür bırakma ilişkisine bağlı özel hak ve mensubiyet · soy yakınları veya özgür bırakma bağıyla bağlı kişiler · nimet veya özgür bırakma bağı kuran kişi
  الموالي بنو العم؛ المولى المعتق والحليف والولي؛ الولي ولي النعم (ayn)؛ المولى المعتق والمعتق والصاحب والحليف وابن العم والناصر والجار؛ الولاء ولاء المعتق (maqayis)؛ المولى المعتق والمعتق وابن العم والناصر والجار؛ الولي الصهر؛ بينهما ولاء أي قرابة؛ الولاء ولاء المعتق (sihah)؛ المولى العصبة؛ المولى الحليف؛ المولى المعتق؛ ابن العم والعم والأخ والابن والعصبات كلهم؛ مولى النعمة؛ المعتق؛ يجب عليك أن تنصره وترثه (tahdhib)
- **B006** yüzünü veya dikkatini yöneltme — yüzünü bir şeye çevirmek · yüzünü o yöne dönmüş veya ona uyan kişi · kulağını veya dikkatini bir şeye vermek
  موليها أي مستقبلها بوجهه (sihah)؛ التولية تكون إقبالا؛ فول وجهك أي وجه وجهك نحوه؛ هو مستقبلها؛ متوليها أي متبعها وراضيها (tahdhib)؛ وليت سمعي كذا ووليت عيني كذا ووليت وجهي كذا أقبلت به عليه (mufradat)
- **B007** dönüp yüz çevirme [kalıp] — arkasını dönüp kaçarak uzaklaşmak · birinden yüz çevirmek ve ilgiyi kesmek
  ولى الرجل أي أدبر (ayn)؛ تولى عنه أي أعرض؛ ولى هاربا أي أدبر (sihah)؛ التولية تكون انصرافا؛ وليتم مدبرين؛ التولي يكون بمعنى الإعراض (tahdhib)؛ إذا عدي بعن اقتضى معنى الإعراض وترك قربه؛ التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار (mufradat)
- **B008** daha uygun ve hak sahibi olma — bir şeye daha uygun, daha layık veya daha hak sahibi olmak · iki daha haklı veya daha uygun kişi
  فلان أولى بكذا أي أحرى به وأجدر (maqayis)؛ فلان أولى بكذا أي أحرى به وأجدر (sihah)؛ فلان أولى بهذا الأمر أي أحق به؛ الأوليان أي الأحقان (tahdhib)
- **B009** yaklaşan kötü sonuç tehdidi — tehdit ve uyarı sözü; sana kötü şey yaklaştı
  أولى تهدد ووعيد؛ معناه قاربه ما يهلكه؛ أولى تحسير له على ما فاته (maqayis)؛ أولى لك تهدد ووعيد؛ معناه قاربه ما يهلكه؛ قارب أن يزيد (sihah)؛ أولى لك تهدد ووعيد؛ قاربك ما تكره؛ يحسره على ما فاته (tahdhib)
- **B010** önceki yağmuru izleyen yağmur — önceki yağmurdan sonra gelen yağmur · erken mevsim yağmurunu izleyen yağmur adı · toprağa izleyen yağmurun yağması · iyilik ardından gelen yağmur veya iyilik
  الولي المطر الذي يكون بعد الوسمي؛ وليت الأرض وليا فهي مولية (ayn)؛ الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي (maqayis)؛ الولي المطرة بعد الوسمي؛ وليت الأرض فهي مولية (jamhara)؛ الولي المطر بعد الوسمي؛ وليت الأرض وليا (sihah)؛ الولي المطر الذي يأتي بعد المطر؛ وليت الأرض وليا؛ أمطرني ولية منك (tahdhib)
- **B011** deve sırtı alt örtüsü — deve sırtında semer altında kullanılan örtü · semer altı örtüleri
  الولية الحلس والولايا جمعه (ayn)؛ الولية شبيهة بالبرذعة تطرح على ظهر البعير؛ الجمع ولايا (jamhara)؛ الولية البرذعة؛ التي تكون تحت البرذعة؛ الجمع الولايا (sihah)؛ الولية البرذعة وجمعها الولايا؛ البرذعة التي تحت الرحل (tahdhib)
- **B012** ele geçirip hedefe ulaşma [kalıp] — bir şeyi ele geçirmek veya ona üstün gelmek · hedefe varmak veya ona önce ulaşmak
  استولى فلان على شيء إذا صار في يده؛ استولى الفرس على الغاية أي بلغها (ayn)؛ استولى على الأمد أي بلغ الغاية (sihah)؛ استولى أحدهما على الغاية إذا سبق الآخر إليها؛ استيلاؤه على الأمد أن يغلب عليه بسبقه؛ استولى فلان على مالي إذا غلب عليه (tahdhib)
- **B013** birine iyi ya da kötü şey yöneltme [kalıp] — birine iyilik yapmak veya bir şeyi ona ulaştırmak · birine iyilik veya kötülük yöneltmek
  أوليته الشيء فوليه؛ أوليته معروفا (sihah)؛ أوليت فلانا شرا وأوليته خيرا؛ أوليته معروفا أسديته إليه (tahdhib)
- **B014** aldığı fiyatla devretme — satın alınan malı bilinen aynı fiyatla başkasına devretme
  التولية في البيع أن تشتري سلعة بثمن معلوم ثم توليها رجلا آخر بذلك الثمن (tahdhib)
- **B015** küçük sürü hayvanlarını ayırma — küçük sürü hayvanlarını büyüklerinden ayırmak · yavru develeri analarından ayırıp alıştırma
  للموالاة معنى ثالث؛ والوا حواشي نعمكم من الجلة أي اعزلوا صغارها عن كبارها؛ توالي ربعي السقاب؛ تواليه أن يفصل عن أمه (tahdhib)
- **B016** taze hurmanın kurumaya dönmesi — taze hurmanın solup kurumaya başlaması · taze hurmadaki solgun kuruma rengi
  يقال للرطب إذا أخذ في الهيج قد ولى وتولى؛ توليه شهبته (tahdhib)

## ح ف ظ (root_000342): 42:6 حَفِيظٌ, 42:48 حَفِيظًا

- **B001** koruyup gözetme — koruyup gözetme ve bakımını üstlenme · bir şeyi koruyup kolladı · bir şeyi koruyan ya da korumakla görevlendirilen kimse · insanların yaptıklarını sayıp yazan melekler · onu yalnız kendisi için sakladı · onu korumasını istedi ve güvenip kendisine teslim etti · koruma altında, kaybolmadan ve değişmeden saklanmış · gözetip başında durma
  أصل واحد يدل على مراعاة الشيء (maqayis)؛ الحفيظ الموكل بالشيء يحفظه (ayn;tahdhib)؛ حفظت الشيء حفظا (jamhara)؛ حفظت الشئ حفظا أي حرسته (sihah)؛ استحفظته كذا أي سألته أن يحفظه عليك (ayn;sihah;tahdhib)؛ تفقد وتعهد ورعاية (mufradat)
- **B002** bellekte tutma — bir şeyi unutmayacak biçimde bellekte tutma · kitabı bölüm bölüm ezberledi
  الحفظ نقيض النسيان (ayn;tahdhib)؛ حفظته أيضا بمعنى استظهرته (sihah)؛ تحفظت الكتاب أي استظهرته (sihah)؛ رزقوا حفظ ما سمعوا وقلما ينسون (tahdhib)؛ هيئة النفس التي بها يثبت ما يؤدي إليه الفهم وضبط الشيء في النفس (mufradat)
- **B003** düzenli biçimde sürdürme — bir işi düzenli biçimde sürdürme · işi bırakmadan sürdürdü · işlerin üzerinde düzenli biçimde durma
  الحفاظ المحافظة على الأمور (maqayis)؛ المحافظة المواظبة على الأمور من الصلوات والعلم ونحوه (ayn)؛ المحافظة المواظبة على الأمر (tahdhib)؛ حافظ على الأمر والعمل وثابر عليه (tahdhib)
- **B004** uyanık ve dikkatli olma — hata yapmamak için tetikte ve dikkatli olma
  التحفظ قلة الغفلة (maqayis)؛ التحفظ قلة الغفلة حذرا من السقطة في الكلام والأمور (ayn)؛ التحفظ التيقظ وقلة الغفلة (sihah)؛ التحفظ قلة الغفلة في الكلام والتيقظ من السقطة (tahdhib)
- **B005** koruyucu öfke ve onurlu tepki — dokunulmaz saydığı bir şey çiğnendiğinde duyulan koruyucu öfke · içte bekleyen koruyucu öfke · beni öfkelendirdi · yakınına ya da komşusuna zarar geldiğinde kişiyi öfkelendiren şeyler
  الغضب الحفيظة (maqayis)؛ أحفظني أي أغضبني (maqayis)؛ الحفيظة الحمية (jamhara)؛ الحفيظة الغضب والحمية وكذلك الحفظة بالكسر (sihah)؛ إنه لذو حفاظ وذو محافظة إذا كانت له أنفة (sihah)؛ الحفظة اسم من الاحتفاظ عندما يرى من حفيظة الرجل (tahdhib)
- **B006** dokunulmazlıkları, sözleri ve bağlılığı koruma — yakınları, verilen sözü ve bağlılığı koruma · kendi topluluğunu arkadan kollayıp açıklarını örtenler · haksızlığa uğrayan yakını savunmanın eski kini giderdiğini anlatan söz · yokluğunda onu ve hakkını korudu · cinsel davranışta özdenetimini koruyanlar · eşleri yokken evlilik bağını gözeten kadınlar
  الحفاظ المحافظة على المحارم ومنعها عند الحروب (ayn)؛ أهل الحفائظ المحامون من وراء إخوانهم مانعون لعوراتهم (ayn)؛ حافظت على الرجل محافظة وحفاظا إذا حفظته في مغيبه (jamhara)؛ إن الحفائظ تنقض الأحقاد (jamhara;sihah)؛ الحفاظ المحافظة على العهد والمحاماة على الحرم (tahdhib)؛ الوفاء بالعقد والتمسك بالود (tahdhib)؛ فروجهم حافظون كناية عن العفة (mufradat)؛ حافظات للغيب أي يحفظن عهد الأزواج (mufradat)
- **B007** açık, düz ve kesintisiz yol [kalıp] — açık, düz ve kesintisiz süren yol
  الطريق الحافظ هو البين المستقيم الذي لا ينقطع (tahdhib)

## و ك ل (root_001681): 42:6 بِوَكِيلٍ, 42:10 تَوَكَّلْتُ, 42:36 يَتَوَكَّلُونَ

- **B001** bir işi başkasına devredip onu kendi adına yetkilendirme — onu birine bırakıp işini ona devretmek · belirli bir iş için onu yetkili kılmak · bir başkasını kendi adına yetkilendirme · temsil görevi; başkasının işini yürütme · kendisine iş devredilen yetkili temsilci · iş onun kararına bırakılmıştır · beni onlarla baş başa bırak
  وكلته إليك أكله كلة أي فوضته (ayn)؛ سمي الوكيل لأنه يوكل إليه الأمر (maqayis)؛ وكلته بأمر كذا توكيلا والاسم الوكالة (sihah)؛ وكيل الرجل الذي يقوم بأمره (tahdhib)؛ التوكيل أن تعتمد على غيرك وتجعله نائبا عنك (mufradat)
- **B002** kendi yetersizliğini kabul edip başkasına dayanarak güvenme — Tanrı'ya güvenmek ve onun koruyup yeteceğine inanmak · birine dayanıp güvenmek · Tanrı'ya dayanıp onu yeterli görmek · birine dayanıp güvenmek
  التوكل منه وهو إظهار العجز في الأمر والاعتماد على غيرك (maqayis)؛ وكلت بالله وتوكلت على الله (ayn)؛ التوكل إظهار العجز والاعتماد على غيرك (sihah)؛ قد اتكل فلان عليك (tahdhib)؛ توكلت عليه بمعنى اعتمدته (mufradat)
- **B003** güçsüzlüğü yüzünden işini başkasına bırakıp aksatan kişi — güçsüz, etkisiz ve işini başkasına bırakan kişi · işini insanlara bırakıp başkasına dayanan kişi · işinde sürekli başkasına dayanan kişi · başkasına dayanıp işini aksatan veya çevik olmayan kişi · işini başkasına güvenerek savsaklamak
  الوَكَلَة والوَكَل الرجل الضعيف (maqayis)؛ رجل وكل ووكلة وهو المواكل يتكل على غيره فيضيع أمره (ayn)؛ رجل وكل ووكلة وتكلة أي عاجز يكل أمره إلى غيره (sihah)؛ رجل وكل إذا كان ضعيفا ليس بنافذ (tahdhib)؛ رجل وكلة تكلة إذا اعتمد غيره في أمره (mufradat)
- **B004** tarafların işte karşılıklı olarak birbirine dayanması — birine dayanmak, onun da sana dayanması · topluluktaki herkesin işi birbirine bırakması
  واكلت الرجل إذا اتكلت عليه واتكل عليك (maqayis)؛ واكلت فلانا مواكلة إذا اتكلت عليه واتكل هو عليك (sihah)؛ تواكل القوم إذا اتكل كل على الآخر (mufradat)
- **B005** hayvanın geride kalarak veya eşine dayanarak kötü yürümesi — hayvanın geride kalması ya da ancak öteki hayvanlarla yürümesi · hayvanın kötü yürümesi · koşuda eşine dayanıp dürtülmeye ihtiyaç duyan at · koşuda eşine dayanarak giden at · kalkışında ve yürüyüşünde yavaşlamak
  الوكال في الدابة أن يتأخر أبدا خلف الدواب (maqayis)؛ الوكال في الدابة أن تحب التأخر خلف الدواب (ayn)؛ فرس واكل يتكل على صاحبه في العدو (sihah)؛ واكلت الدابة وكالا إذا أساءت السير (tahdhib)؛ الوكال في الدابة أن لا يمشي إلا بمشي غيره (mufradat)
- **B006** kendisine bırakılan işi üstlenip koruyan yeterli görevli — birinin işini üstlenip yürütmek · işi üstlenen, koruyan, yeterli olan ve güvence veren görevli · deve sahibi
  سمي الوكيل لأنه يوكل إليه الأمر (maqayis)؛ الوكيل كافينا والكافي والحافظ والكفيل والذي توكل بالقيام بجميع ما خلق (tahdhib)؛ الوكيل فعيل بمعنى المفعول واكتف به أن يتولى أمرك وحافظ لهم والكفيل (mufradat)

## ق ر ء (root_001210): 42:7 قُرْءَانًا

- **B001** toplamak ve bir araya getirmek — bir şeyi toplayıp parçalarını birleştirmek · insanların toplandığı yerleşim · konukların çevresinde toplandığı veya yiyeceğin toplandığı büyük kap · develerin su içmeye geldiği uzun yalak · sıkma düzeneğine benzeyen araç · kemiklerin birleştiği sırt · içindekileri toplayan kursak
  أصل صحيح يدل على جمع واجتماع (maqayis-v4;maqayis-v5)؛ قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض (sihah)؛ معنى قرآن معنى الجمع (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض (mufradat)؛ الجرية أصلها قرية لأنها تقري الشيء أي تجمعه (maqayis-ibdal)
- **B002** okumak, okutmak ve birlikte okumak — kutsal metni, kitabı, şiiri veya anlatıyı okumak · düzenli ve güzel okuma · Kur'an; ayrıca okuma eylemi · okuyan kişi · ona Kur'an okumayı öğretmek veya okutmak · onunla karşılıklı okuyup çalışmak
  قرأت القرآن عن ظهر قلب أو نظرت فيه (ayn)؛ وقرأ فلان قراءة حسنة فالقرآن مقروء وأنا قارئ (ayn)؛ قرأت الكتاب قراءة وقرآنا ومنه سمي القرآن (sihah)؛ قرأت القرآن لفظت به مجموعا (tahdhib)؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا (tahdhib)؛ أقرأت غيري أقرئه إقراء (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل (mufradat)؛ قارأته دارسته (tahdhib;mufradat)
- **B003** aybaşı ya da arınma dönemi — aybaşı, arınma veya bunların dönemi · bekleme süresini belirleyen aybaşı ya da arınma dönemleri · kadının aybaşı olması, arınması veya döngü dönemine girmesi · kadının kanama görmesi veya aybaşı olması
  قرأت المرأة قرءا إذا رأت دما وأقرأت إذا حاضت (ayn)؛ القرء الحيض والقرء أيضا الطهر وهو من الأضداد (sihah)؛ القرء انقضاء الحيض وما بين الحيضتين (sihah)؛ الأقراء الحيض والأقراء الأطهار (tahdhib)؛ القرء اسم للوقت يصلح للحيض ويصلح للطهر (tahdhib)؛ اسم للدخول في الحيض عن طهر (mufradat)؛ القرء وقت يكون للطهر مرة وللحيض مرة (maqayis-v4;maqayis-v5)
- **B004** rahminde taşıyıp gebe olmak — dişi devenin rahminde yavru veya doğum artığı taşımak · dişi devenin gebe olması · gebe dişi deve
  فأما الناقة فإذا حملت قيل قرؤت قروءة (ayn)؛ القارئ الحامل (ayn)؛ ما قرأت هذه الناقة سلى قط وما قرأت جنينا (sihah)؛ لم تضم رحمها على ولد (sihah)؛ ما قرأت الناقة سلى قط وما قرأت ملقوحا قط (tahdhib)؛ لم تحمل علقة أي دما ولا جنينا (tahdhib)؛ ما قرأت هذه الناقة سلى كأنه يراد أنها ما حملت قط (maqayis-v4;maqayis-v5)
- **B005** vakit, yaklaşma veya gecikme — vakit · rüzgarların esme vakti · rüzgarın vaktine girmesi veya yıldızlara bağlanan yağmurun gecikmesi · ihtiyacın ya da işin yaklaşması veya gecikmesi · yolculuktan dönmek veya aileye yaklaşmak
  القارئ الوقت (sihah)؛ أقرأت الريح إذا دخلت في وقتها (sihah)؛ أقرأت النجوم إذا تأخر مطرها (sihah)؛ أقرأت حاجتك دنت (sihah)؛ هذا قارئ الرياح لوقت هبوبها (tahdhib)؛ أقرأت من سفري أي انصرفت وأقرأت من أهلي أي دنوت (tahdhib)؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر (tahdhib)؛ هبت الرياح لقارئها لوقتها (maqayis-v4;maqayis-v5)
- **B006** dindar okur; öğrenmeye yönelen kişi — dindar ve ibadete bağlı okur · ibadete bağlı okurlar veya çok dindar okur · kendini ibadete vermek, öğrenmek veya anlamak
  رجل قارئ عابد ناسك وفعله التقري والقراءة (ayn)؛ القراء الرجل المتنسك وقد تقرأ أي تنسك (sihah)؛ قرأت أي صرت قارئا ناسكا وتقرأت بهذا المعنى (tahdhib)؛ قال بعضهم تقرأت تفقهت (tahdhib)؛ تقرأت تفهمت (mufradat)
- **B007** esenlik dileğini iletmek [kalıp] — sana selamını iletti · sana selamını iletti; biçimin doğruluğu tartışmalıdır · selamımı alıp ilet
  فلان قرأ عليك السلام وأقراك السلام بمعنى (sihah)؛ اقرأ عليه السلام ولا يقال أقرئه السلام لأنه خطأ (tahdhib)؛ اقترئ مني السلام (tahdhib)
- **B008** yeni gelinen yöreye bağlı salgın etkisi [kalıp] — yeni gelinen yörenin zamanla geçen salgın etkisi
  القرأة بالكسر الوباء (sihah)؛ إذا قدمت بلادا فمكثت بها خمس عشرة فقد ذهبت عنك قرأة البلاد (sihah)؛ قرأة البلاد وأهل الحجاز يقولون قرة البلاد بغير همز (tahdhib)؛ إن مرضت بعد ذلك فليس من وباء البلاد (tahdhib)
- **B009** dişi devenin çiftleşme dönemi [kalıp] — erkek devenin, gebe kalıp kalmadığını anlamak için dişiyi bırakması · dişi devenin çiftleşme isteği veya dönemi
  استقرأ الجمل الناقة إذا تاركها لينظر ألقحت أم لا (sihah)؛ ضرب الفحل الناقة على غير قرء وقرء الناقة ضبعتها (tahdhib)؛ ما دامت الوديق في وداقها فهي في قرئها وإقرائها (tahdhib)
- **B010** biçime bağlı adlandırmalar — kadın köleyi aybaşı görene kadar gözetim altında tutmak · kadın kölenin gebe olmadığını aybaşı bekleyerek anlamak · onu hapsetmek
  دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (sihah)؛ دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (tahdhib)؛ قرأت الجارية استبرأتها بالقرء (mufradat)؛ أعتم فلان قراه وأقرأه أي حبسه (tahdhib)
- **B011** bir yolu veya örneği izlemek — tek bir yol, amaç veya izlenen yön · şiirin başka bir şiirin yöntem ve örneğine göre olması
  القرو كل شيء على طريقة واحدة (maqayis-v4;maqayis-v5)؛ رأيت القوم على قرو واحد (maqayis-v4;maqayis-v5)؛ القرو القصد تقول قروت وقريت إذا سلكت (maqayis-v4;maqayis-v5)؛ أقرأت في الشعر (tahdhib)؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله (tahdhib)
- **B012** bilgiyi toplayıp tanıklık eden kişi — tanık · yeryüzündeki tanıklar; bilgiyi toplayıp tanıklık edenler
  القارئة وهو الشاهد (maqayis-v4;maqayis-v5)؛ الناس قواري الله تعالى في الأرض هم الشهود (maqayis-v4;maqayis-v5)؛ ممكن أن يحمل هذا على ذلك القياس أي إنهم يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها (maqayis-v4;maqayis-v5)
- **B013** hayvan varlığı veya bakmakla yükümlü olunanlar — deve ve küçükbaş hayvan varlığı veya bakmakla yükümlü olunan aile
  القرة المال من الإبل والغنم (maqayis-v4;maqayis-v5)؛ والقرة العيال (maqayis-v4;maqayis-v5)

## ق ر ء (root_001211): 42:7 قُرْءَانًا

- **B001** biçime bağlı adlandırmalar — Kur'an; adı toplama anlamıyla ilişkilendirilmiş, fakat bu köken reddedilmiştir · Kur'an'ı sözlerini birleştirerek okumak · okuma ve sözleri söyleme · başkasına okutmak veya okumayı öğretmek · okuyan kişi · başkasına okutan veya okumayı öğreten kişi · dindar bir okur durumuna gelmek · dindar bir okur olmak veya öğrenmek · onunla karşılıklı okuyup çalışmak · birinden okumasını istemek; aktarımda açıklama verilmemiştir
  ومعنى قرآن معنى الجمع؛ قرأت القرآن لفظت به مجموعا؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا؛ أقرأت غيري إقراء؛ قارأت فلانا مقارأة أي دارسته؛ تقرأت تفقهت
- **B002** özel adlandırma kümesi — aybaşı veya arınmanın gerçekleştiği dönem · aybaşı ve arınma dönemleri · kadının aybaşı veya arınma dönemine girmesi · rüzgarların esme vakti · dişi devenin çiftleşme isteği · yeni gelinen yörenin ilk günlerdeki salgın etkisi
  الأقراء الحيض والأطهار؛ القرء اسم للوقت؛ قارئ الرياح لوقت هبوبها؛ قرء الناقة ضبعتها؛ قرأة البلاد
- **B003** rahimde toplanıp taşınmak — kanın rahimde toplanması · dişi devenin doğum artığı taşımaması veya dışarı atmaması · yavruyu rahminde toplamamak, taşımamak veya dışarı atmamak · rahminde bir aybaşılık kan toplamamış olmak
  لم تجمع جنينا؛ لم تضطم رحمها على الجنين؛ لم تلقه؛ ما قرأت الناقة سلى قط أي ما طرحت وتأويله ما حملت؛ القرء اجتماع الدم في الرحم؛ ما ضمت رحمها على حيضة
- **B004** biçime bağlı adlandırmalar — 
  أقرأت من سفري أي انصرفت؛ أقرأت من أهلي أي دنوت؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر؛ أعتم فلان قراه وأقرأه أي حبسه
- **B005** şiiri başka bir şiirin örneğine göre kurmak — bu şiirin öteki şiirin yöntem ve örneğine göre olması · şiir bağlamında kullanmak; bağımsız anlamı açıklanmamıştır
  أقرأت في الشعر؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله؛ على قري هذا الشعر وغراره
- **B006** belirli kalıpla selam iletmek — ona selam ilet · selamımı alıp ilet · selam iletmek için yanlış sayılan biçim
  اقرأ عليه السلام ولا يقال أقرئه السلام؛ اقترىء مني السلام

## ع ر ب (root_000996): 42:7 عَرَبِيًّا

- **B001** açıkça ortaya koyma — açık ve anlaşılır konuşmak · içindekini açıkça anlatmak · daha önce evlenmiş kadının kendi rızasını açıkça bildirmesi · çocuğun ilk kez kendini anlatabilmesi · sözün çekim sonlarını göstererek anlam ayrımlarını açıklama · sözü karışıklık kalmayacak biçimde açıklamak · topluluk adına konuşup onu savunmak · konuşmasını dil yanlışlarından arındırmak · dili açık ve düzgün
  أعرب الرجل عن نفسه إذا بين وأوضح (maqayis)؛ وأعرب الرجل أفصح القول والكلام (ayn)؛ وأعرب الرجل بحجته إذا أفصح عنها (jamhara)؛ وأعرب بحجته أي أفصح بها (sihah)؛ الإعراب والتعريب معناهما واحد وهو الإبانة (tahdhib)؛ الإعراب البيان يقال أعرب عن نفسه (mufradat)
- **B002** Arap halkı ve çölde yaşayan kesimi — Arap halkı · çölde yaşayan Araplar · soy bakımından katışıksız Araplar · sonradan Arap topluluğuna katılıp onun dilini konuşanlar · Arap topluluğuna katılmak veya onun dilini benimsemek · yerleşik hayattan sonra çöle dönüp göçebe yaşamak · Arapça · Arap halkından olan · Arapları yüceltme amacı taşıyan küçültme biçimi
  الأمة التي تسمى العرب (maqayis)؛ العرب العاربة هم الصريح والأعاريب جماعة الأعراب (ayn)؛ العرب ضد العجم (jamhara)؛ العرب جيل من الناس والأعراب سكان البادية خاصة (sihah)؛ رجل عربي إذا كان نسبه في العرب ثابتا (tahdhib)؛ العرب ولد إسماعيل والأعراب صار اسما لسكان البادية (mufradat)
- **B003** orada hiç kimse yok [kalıp] — evde hiç kimse yok
  ما بها عريب أي ما بها أحد (maqayis)؛ ما بها عريب أي ما بها عربي (ayn)؛ ما بالدار عريب أي ما بها أحد (jamhara)؛ ما بالدار عريب أي ما بها أحد (sihah)؛ وما بالدار عريب أي أحد يعرب عن نفسه (mufradat)
- **B004** katışıksız soylu Arap atı veya devesi — atın soy bakımından katışıksız olması · katışıksız soylu Arap atları ve develeri · katışıksız soylu Arap atı sahibi
  أعرب الفرس خلصت عربيته وفاتته القرفة (maqayis)؛ والإبل العراب هي العربية (ayn)؛ رجل معرب له خيل عراب (jamhara)؛ المعرب من الخيل الذي ليس فيه عرق هجين (sihah)؛ المعرب صاحب الفرس العربي (mufradat)
- **B005** kocasına sevgisini gösteren neşeli kadın — kocasına sevgisini belli eden neşeli kadın · eşlerine sevgi gösteren kadınlar
  المرأة العروب الضحاكة الطيبة النفس (maqayis;ayn)؛ العروب من النساء المحبة لزوجها المظهرة له ذلك (jamhara)؛ العروب من النساء المتحببة إلى زوجها (sihah)؛ امرأة عروبة معربة بحالها عن عفتها ومحبة زوجها (mufradat)
- **B006** canlılık ve istekli atılma — canlılık ve atların dizginlere doğru atılması
  العرب بسكون الراء النشاط؛ والخيل تنزع عربا في أعنتها
- **B007** geride kalan iz — geride kalan iz
  والعرب الأثر بفتح الراء؛ يقال منه عرب يعرب عربا
- **B008** beden veya organda bozulma — midesi bozulmak · mide bozukluğu · yaranın yeniden azması veya kabuk bağlaması · bozulmuş sayılan kadın
  فساد في جسم أو عضو؛ عربت معدته إذا فسدت (maqayis)؛ عربت المعدة إذا فسدت (jamhara)؛ العرب أيضا فساد المعدة؛ عرب أيضا الجرح نكس وغفر (sihah)
- **B009** cuma gününün eski adı [kalıp] — cuma gününün eski adı
  يوم الجمعة يدعى العروبة (maqayis)؛ والعروبة يوم الجمعة (ayn)؛ ويوم عروبة يوم الجمعة (jamhara)؛ ويوم العروبة يوم الجمعة (sihah)
- **B010** başaklı bir mera otunun kurusu — başaklı bir mera otunun kurusu
  والعرب يبيس البهمى (jamhara)؛ والعرب بالكسر يبيس البهمى (sihah)
- **B011** karşı çıkıp kınama [kalıp] — sözüne karşı çıkıp onu reddetmek · yaptığını çirkin bulup kınamak
  عربت على الرجل إذا رددت عليه قوله (jamhara)؛ عرب عليه فعله أي قبح؛ عربوا عليه أي ردوا عليه بالإنكار (sihah)؛ عربت عليه إذا رددت من حيث الإعراب (mufradat)
- **B012** çok hızlı akan ırmak — çok hızlı akan ırmak
  العربة النهر الشديد الجري (jamhara)؛ والعربة بالتحريك النهر الشديد الجرية (sihah)
- **B013** satışta önceden verilen güvence parası — satışta önceden verilen güvence parası
  والعربان والعربون الذي تسميه العامة الربون
- **B014** atı yararak kan alma [kalıp] — atın bir yerini yarıp kan almak
  وعربت الفرس تعريبا إذا بزغته
- **B015** Araplara özgü sayılan ten renginde çocuğu olma — Araplara özgü sayılan renkte bir çocuğu olmak
  وأعرب الرجل أي ولد له ولد عربي اللون
- **B016** ağza alınmayacak sözler söyleme — ağza alınmayacak sözler söylemek
  وأعرب الرجل تكلم بالفحش والاسم العرابة
- **B017** değişken sulamayı tek düzene bağlama [kalıp] — değişken aralıklı sulamayı tek düzene bağlamak
  وأعرب سقي القوم إذا كان مرة غبا ومرة خمسا ثم قام على وجه واحد
- **B018** hurmanın yapraklarını kesip budama — hurmanın yapraklarını kesip budamak
  والتعريب قطع سعف النخل وهو التشذيب
- **B019** yabancı adı Arap söyleyişine uyarlama — yabancı bir adı Arap söyleyiş düzenine uyarlamak
  وتعريب الاسم الأعجمي أن تتفوه به العرب على منهاجها
- **B020** kişinin kendisi ve benliği — kişinin kendisi; benliği
  والعربة أيضا النفس

## ن ذ ر (root_001488): 42:7 لِّتُنذِرَ, 42:7 وَتُنذِرَ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ء م م (root_000053): 42:7 أُمَّ, 42:8 أُمَّةً

- **B001** anne ve annelik işlevi — anne · anneler · anneler; özellikle insan dışı canlılar için kullanılan çoğul · anne yokluğu üzerinden öven ya da yeren kalıp söz
  الأم الواحد والجمع أمهات وربما قالوا أم وأمات وفلانة تؤم فلانا أي تغذوه وتربيه (maqayis)؛ الأم معروفة (jamhara)؛ الأم الوالدة والجمع أمات وأصل الأم أمهة لذلك تجمع على أمهات وأمت المرأة صارت أما (sihah)؛ الأم بإزاء الأب وهي الوالدة القريبة والبعيدة (mufradat)
- **B002** ana kaynak ve toplayıcı odak — bir şeyin kaynağı, başlangıcı veya parçalarının döndüğü odak · Mekke; bağlama göre çevresindeki yerleşimleri toplayan ana kent · kitabın ana kaynağı; bağlama göre başlangıç bölümü veya korunmuş ana kayıt · bir şeyin kaynağını, odağını veya ana bölümünü gösteren adlandırma
  كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما (maqayis)؛ كل شيء يضم إليه سائر ما يليه فإن العرب تسمي ذلك الشيء أما (ayn)؛ كل شيء انضمت إليه أشياء فهو أم (jamhara)؛ أم الشيء أصله ومكة أم القرى (sihah)؛ كل ما كان أصلا لوجود شيء أو تربيته أو إصلاحه أو مبدئه أم (mufradat)
- **B003** beyin bölgesi ve ona ulaşan baş yarası — beyin veya baş içindeki beyin bölgesi · beyne ulaşan baş yarası · başından beyin bölgesine ulaşan darbeyle yaralanmış kişi · ağır baş yaralısı; baş ezmeye yarayan taş
  أم الرأس وهو الدماغ والشجة الآمة التي تبلغ أم الدماغ (maqayis)؛ أم الرأس وهو الدماغ ورجل مأموم والشجة الآمة التي تبلغ أم الدماغ (ayn)؛ أم رأسه بالعصا إذا أصاب أم رأسه وهي أم الدماغ (jamhara)؛ أم الدماع الجلدة التي تجمع الدماغ ويقال أيضا أم الرأس وأمه أي شجه آمة (sihah)؛ أمه شجه فحقيقته أن يصيب أم دماغه (mufradat)
- **B004** ortak bağla birleşen topluluk veya tür — ortak bir bağla birleşen topluluk veya canlı türü
  كل قوم نسبوا إلى شيء وأضيفوا إليه فهم أمة وكل جيل من الناس أمة (maqayis)؛ كل قوم في دينهم من أمتهم وكل جيل من الناس هم أمة وكل جنس من السباع أمة (ayn)؛ الأمة القرن من الناس (jamhara)؛ الأمة الجماعة وكل جنس من الحيوان أمة (sihah)؛ الأمة كل جماعة يجمعهم أمر ما (mufradat)
- **B005** benimsenen inanç ve yaşayış yolu — benimsenen inanç veya yaşayış yolu · inanç veya izlenen yol anlamındaki değişik söyleyiş
  الأمة الدين (maqayis)؛ الأمة كل قوم في دينهم من أمتهم (ayn)؛ الأمة الملة (jamhara)؛ الأمة الطريقة والدين والإمة أيضا لغة في الأمة وهي الطريقة والدين (sihah)؛ إنا وجدنا آباءنا على أمة أي على دين مجتمع (mufradat)
- **B006** boy ve beden görünüşü — insanın boyu, beden yapısı veya görünüşü
  الأمة القامة وطوال الأمم وبدنه ووجهه وما أحسن أمته أي خلقه (maqayis)؛ طوال الأمم يعني القامة والجسم (ayn)؛ الأمة قامة الإنسان والأمة الطول (jamhara)؛ الأمة القامة (sihah)
- **B007** okuma yazma bilmeyen — okuma yazma bilmeyen kişi
  الأمي في اللغة المنسوب إلى ما عليه جبلة الناس لا يكتب (maqayis)؛ الأمي هو الذي لا يكتب ولا يقرأ من كتاب وقيل منسوب إلى الأمة الذين لم يكتبوا وقيل لنسبته إلى أم القرى (mufradat)
- **B008** bir süre, zaman dilimi — bir süre veya zaman dilimi
  الأمة في قوله وادكر بعد أمة أي بعد حين (maqayis)؛ الأمة الحين (sihah)؛ وادكر بعد أمة أي حين وحقيقة ذلك بعد انقضاء أهل عصر أو أهل دين (mufradat)
- **B009** öne konulan ve izlenen kılavuz — önder veya izlenen kılavuz · birlikte kılınan namazda öne geçip önderlik etmek
  الإمام كل من اقتدي به وقدم في الأمور والخيط الذي يقوم عليه البناء إمام (maqayis)؛ كل من اقتدي به وقدم في الأمور فهو إمام والإمام الطريق (ayn)؛ إن إبراهيم كان أمة أي إماما ورئيس القوم أما لهم (jamhara)؛ أممت القوم في الصلاة إمامة والإمام الذي يقتدى به والإمام الطريق (sihah)؛ الإمام المؤتم به إنسانا أو كتابا أو غير ذلك (mufradat)
- **B010** iyilik ve iyi durum — iyilik, bolluk veya iyi durum
  الأمة النعمة (maqayis)؛ الإمة النعمة (ayn)؛ الإمة النعمة (jamhara)؛ الإمة بالكسر النعمة (sihah)
- **B011** ön taraf ve yakın konum — ön, ön taraf veya ilerisi · yakın, erişilebilir veya orta uzaklıkta olan
  الأمام القدام وامض يمامي في معنى امض أمامي والأمم الشيء القريب المتناول (maqayis)؛ الأمام بمنزلة القدام والأمم الشيء القريب (ayn)؛ سرت أمام الرجل وأمامته ويمامته (jamhara)؛ كنت أمامه أي قدامه والأمم بين القريب والبعيد وأخذت ذلك من أمم أي من قرب (sihah)
- **B012** amaçlayıp yönelmek — bir şeyi amaçlayıp ona yönelmek · bir şeyi bilerek seçmek ve hedeflemek · kutsal eve yönelenler
  الأمم القصد وآمين البيت الحرام أي يقصدونه والتيمم يجري مجرى التوخي أي تعمدوا (maqayis)؛ أم يؤم أما إذا قصد للشيء (jamhara)؛ الأم بالفتح القصد أمة وأممه وتأممه إذا قصده (sihah)؛ الأم القصد المستقيم وهو التوجه نحو مقصود (mufradat)
- **B013** az, küçük veya önemsiz şey — az, küçük ya da değersiz şey
  الأمم الشيء اليسير الحقير وأمم أي صغير وعظيم من الأضداد (maqayis)؛ الأمم الشيء اليسر الهين الحقير (ayn)؛ الامم الشئ اليسير يقال ما سألت إلا أمما (sihah)
- **B014** genç kız veya kadın köle — genç kız veya kadın köle
  الأمة الوليدة (jamhara)
- **B015** insandaki kusur — insandaki kusur veya ayıp
  الآمة العيب (ayn)؛ الأمة العيب في الإنسان (jamhara)
- **B016** seçenek veya düzeltme bildiren soru bağlacı — iki soru seçeneğini bağlayan veya düzeltmeli yeni soru açan "yoksa"
  أم مخففة حرف عطف في الاستفهام تقع معادلة لألف الاستفهام بمعنى أي وتكون منقطعة (sihah)؛ أم إذا قوبل به ألف الاستفهام فمعناه أي وإذا جرد عن ذلك يقتضي معنى ألف الاستفهام مع بل (mufradat)

## ق ر ي (root_001222): 42:7 ٱلْقُرَىٰ

- **B001** insanların toplandığı yerleşim ve halkı — insanların toplandığı yerleşim ya da o yerin halkı · köyler ya da yerleşimler · ayet bağlamında sözü edilen iki şehir · yerleşimde oturan ile açık arazide yaşayan
  القرية سميت قرية لاجتماع الناس فيها (maqayis)؛ القرية معروفة والجمع القرى؛ القريتين مكة والطائف؛ جاءني كل قار وباد (sihah)؛ القرية اسم للموضع الذي يجتمع فيه الناس وللناس جميعا (mufradat)
- **B002** havuzda, ağızda, yarada veya kursakta toplama ve birikme — havuzda ya da başka bir yerde birikmiş su · suyu havuzda toplamak · bir şeyi ağzında toplamak · devenin yemi yanağında biriktirmesi · irinin yarada birikmesi · suyun biriktiği yer ya da aktığı yatak · yiyecek biriktiren kursak
  قريت الماء في المقراة جمعته؛ وذلك الماء المجموع قرى (maqayis)؛ القري جبي الماء في الحوض؛ المقرى مجتمع ماء كثير؛ المدة تقري في الجرح أي تجتمع (ayn)؛ قريت الماء في الحوض أي جمعت؛ البعير يقري العلف في شدقه أي يجمعه (sihah)؛ قريت الماء في الحوض؛ قرى الشيء في فمه جمعه؛ قريان الماء مجتمعه (mufradat)؛ الجرية الحوصلة كأن أصلها قرية لأنها تقري الشيء أي تجمعه (maqayis-jry)
- **B003** konuğu yiyecekle ağırlama — konuğu yiyecekle ağırlama · konuğu doyurup iyi ağırlamak · konuğa sunulan yiyecek · konukların çevresinde toplandığı büyük yemek çanağı · konuklara yemek sunulan büyük çanaklar · konuğun ağırlandığı yemek kabı
  المقراة الجفنة سميت لاجتماع الضيف عليها أو لما جمع فيها من طعام (maqayis)؛ القرى الإحسان إلى الضيف؛ قراه يقريه قرى؛ المقاري جفان يقرى فيها الأضياف (ayn)؛ المقرى إناء يقرى فيه الضيف؛ قريت الضيف قرى وقراء أحسنت إليه؛ ما قري به الضيف (sihah)؛ قريت الضيف قرى (mufradat)
- **B004** su ya da yiyecek toplayan kap veya oyuk — su ya da yiyecek toplayan havuz, oluk veya büyük çanak · suyun toplandığı yer ya da onu tutan kap · ahşap kap, yalak, uzun havuz ya da oyulmuş toplama yeri · hayvanın su içtiği yalak
  المقراة الجفنة؛ القرو كالمعصرة؛ القرو حوض معروف ممدود (maqayis)؛ المقراة شبه حوض ضخم؛ المقاري جفان؛ المقرى مجتمع ماء كثير (ayn)؛ القرو قدح من خشب؛ القرو ميلغ الكلب؛ القرو أسفل النخلة ينقر؛ القرو حوض طويل؛ المقراة المسيل؛ المقرى إناء؛ الجفنة مقراة (sihah)
- **B005** bir güzergâhı yer yer izleyerek ilerleme — ülkeleri ya da toprakları birer birer izleyip dolaşmak · ülkeleri yer yer izleyerek baştan başa dolaşmak · su kaynaklarını takip etmek · yolun izlenen yönü ya da yanı
  القرو القصد؛ قروت وقريت إذا سلكت؛ يتبعها قرية قرية (maqayis)؛ قروت البلاد وقريتها واقتريتها واستقريتها إذا تتبعتها؛ تقريت المياه أي تتبعتها (sihah)؛ تنح عن سنن الطريق وقريه وقرقه بمعنى واحد (tahdhib)
- **B006** tek yol ya da tek örtü halinde olma [kalıp] — aynı yol ya da durum üzerinde · yağmurun tek örtü gibi kapladığı toprak
  القرو كل شيء على طريقة واحدة؛ رأيت القوم على قرو واحد (maqayis)؛ تركت الأرض قروا واحدا إذا طبقها المطر؛ رأيت القوم على قرو واحد أي على طريقة واحدة (sihah)
- **B007** sırt ve güçlü sırtlı dişi deve — kemiklerin birleştiği sırt · uzun hörgüçlü ya da güçlü sırtlı dişi deve
  القرى الظهر وسمى قرى لما اجتمع فيه من العظام؛ ناقة قرواء شديدة الظهر (maqayis)؛ القرا الظهر؛ ناقة قرواء طويلة السنام ويقال الشديدة الظهر (sihah)
- **B008** ev direğinin başını taşıyan yuvalı ahşap düzenek — ev direğinin başı için yuvası bulunan ahşap düzenek
  القرية على فعيلة خشبات فيها فرض يجعل فيها رأس عمود البيت (sihah)؛ القرية بلا همز أن تؤخذ عصيتان طولهما ذراع ثم يعرض على أطرافهما عويد؛ يكون فيه رأس العمود (tahdhib)
- **B009** toplama ve belirli döneme girme çevresindeki kullanımlar — içindeki hükümleri ve anlatıları bir araya getiren kutsal kitap · temizlik ya da aybaşı dönemi için belirli vakit · kadının temizlikten aybaşına ya da tersine geçmesi · dişi devenin hiç gebe kalmamış olması
  إذا همز هذا الباب كان هو والأول سواء؛ ما قرأت هذه الناقة سلى؛ ومنه القرآن كأنه سمى بذلك لجمعه ما فيه؛ أقرأت المرأة؛ القرء وقت يكون للطهر مرة وللحيض مرة؛ هبت الرياح لقارئها لوقتها
- **B010** izleyip bilgi toplayan tanık — izleyip bilgi toplayarak tanıklık eden kişi · insanları ve yaptıklarını izleyen tanıklar
  القارئة وهو الشاهد؛ الناس قوارى الله تعالى في الأرض هم الشهود؛ يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها (maqayis)؛ الناس قواري الله في الأرض أي شهداء الله؛ يقرون الناس أي يتبعونهم فينظرون إلى أعمالهم (sihah)
- **B011** sürü malı ya da bakmakla yükümlü olunan ev halkı — deve ve koyunlardan oluşan mal varlığı · bakmakla yükümlü olunan ev halkı
  القرة المال من الإبل والغنم؛ والقرة العيال؛ القرة التي هي المال
- **B012** mızrak ucunun sivri tepesi ve keskin kenar — mızrak ucunun en üstteki sivri ve keskin bölümü · bir şeyin keskin ucu ya da kenarı
  مما شذ عن هذا الباب القارية طرف السنان؛ وحد كل شيء قاريته (maqayis)؛ القارية من السنان أعلاه وحده وكذلك حد السيف ونحوه (sihah)

## ح و ل (root_000373): 42:7 حَوْلَهَا

- **B001** yer ya da durum değiştirme — hareket etmek, değişmek veya başka bir duruma geçmek · bir şeyi değiştirmek veya başka yere taşımak · atın sırtına sıçrayıp binmek · atın sırtına sıçramak · düzgünlüğünü yitirip eğrilmek · eğrilmiş yay · rengi, yeri veya durumu değişmiş şey · hareket edip etmediğine bakmak · kamçıyla vurmak üzere üzerine yönelmek · kovayı çevirip suyu dökmek
  أصل واحد وهو تحرك في دور (maqayis); حال الشخص يحول إذا تحرك وكذلك كل متحول عن حالة (maqayis); حال الرجل في متن فرسه يحول حولا وحؤولا إذا وثب عليه (maqayis;sihah); حال الشيء يحول حؤولا يكون تغييرا ويكون تحويلا (ayn); حال إلى مكان آخر أي تحول وحال الشخص أي تحرك (sihah); أصل الحول تغير الشيء وانفصاله عن غيره (mufradat)
- **B002** bir tam yıl — tam yıl · üzerinden tam bir yıl geçmek · üzerinden bir yıl geçmiş olmak · bir yerde bir yıl kalmak · bir yaşını doldurmak · ilk yılındaki hayvan; yıllık · bir veya birkaç yıl ekilmeden bırakılmış toprak
  الحول العام وذلك أنه يحول أي يدور (maqayis); الحول سنة بأسرها (ayn); الحول السنة وحال عليه الحول أي مر (sihah); الحول السنة اعتبارا بانقلابها ودوران الشمس (mufradat)
- **B003** gizli yoldan amaca ulaşma ve güç yetirme — gizli veya dolaylı yoldan amaca ulaştıran düzen · dolaylı çözüm yolu · istemek ve elde etmeye çalışmak · iş görme gücü ve yetisi · hiçbir güç ve yeti yok · işleri çevirmekte becerikli kişi · kaçınılmaz olarak; başka yolu yok · büyük ve sarsıcı olay
  الحيلة والحويل والمحاولة من طريق واحد لأنه يدور حوالي الشيء ليدركه (maqayis); الحول الحيلة والاحتيال والمحاولة مطالبتك الأمر بالحيل (ayn); الحول الحيلة والقوة أيضا وحاولت الشيء أي أردته (sihah); الحيلة والحويلة ما يتوصل به إلى حالة ما في خفية والحول ما له من القوة (mufradat)
- **B004** çevre, yan veya karşı taraf — bir şeyin çevresi ve yanı · tam karşısında, hizasında · çevresini kuşatmak
  الحول اسم يجمع الحوالي تقول حوالي الدار (ayn); قعدوا حوله وحواله وحوليه وحواليه وقعد حياله وبحياله أي بإزائه (sihah); حول الشيء جانبه الذي يمكنه أن يحول إليه (mufradat)
- **B005** araya girip ayıran engel — iki şeyi ayıran engel · ikimizin arasına girip ayırmak
  الحوال كل شيء حال بين اثنين أي حائل بينهما (ayn); حال الشيء بيني وبينك أي حجز (sihah); حال بيني وبينك كذا وحيل بينهم وبين ما يشتهون (mufradat)
- **B006** göz bebeğinin buruna doğru kayması — göz bebeğinin buruna doğru kayması · gözü içe doğru kaymak
  الحول إقبال الحدقة على الأنف وإذا كان الحول يحدث ويذهب قيل احولت عينه (ayn); رجل أحول بين الحول وقد حولت عينه واحولت أيضا (sihah)
- **B007** gebe kalmayan dişi deve; ürün vermeyen hurma — bir yıl veya daha uzun süre gebe kalmamış dişi deve · gebe kalmayan dişi develer; gebe kalmama · dişi deve yavrusu
  ناقة حائل التي لم تحمل سنة أو أكثر (ayn); حالت الناقة حيالا إذا ضربها الفحل فلم تحمل وكذلك النخل (sihah); الحائل الأنثى من ولد الناقة (sihah); حالت الناقة تحول حيالا إذا لم تحمل وأم حائل (mufradat)
- **B008** doğumla çıkan zar ya da su — yavruyla birlikte çıkan zar, su veya eten benzeri oluşum
  الحولاء ما يخرج من الولد وهو مطيف (maqayis); الحولاء من الناقة كالمشيمة من المرأة (ayn); الحولاء الجلدة التي تخرج مع الولد والماء الذي يخرج على رأس الولد (sihah); الحولاء لما يخرج مع الولد (mufradat)
- **B009** içinde bulunulan durum — kişinin veya şeyin içinde bulunduğu durum, nitelik ve zaman
  الحال تؤنث فيقال حال حسنة وحالات الدهر وأحواله صروفه والحال الوقت الذي أنت فيه (ayn); الحالة واحدة حال الإنسان وأحواله (sihah); الحال لما يختص به الإنسان وغيره من أموره المتغيرة والحال الصفة التي عليها الموصوف (mufradat)
- **B010** borcun başka kişiye aktarılması — borcu veya borçluyu başka bir kişiye aktarma
  الحوالة إحالتك غريما (ayn); أحال عليه بدينه والاسم الحوالة (sihah); أحلت على فلان بالدين (mufradat)
- **B011** çelişkili olduğu için olanaksız söz — anlamı saptırılmış veya karşıtları birleştiren olanaksız söz
  المحال من الكلام ما حول عن وجهه وكلام مستحيل محال (ayn); أحال الرجل أتى بالمحال وتكلم به واستحال الكلام أي صار محالا (sihah); المحال ما جمع فيه بين المتناقضين واستحال الشيء صار محالا (mufradat)
- **B012** sırtta taşınan bohça yükü — kumaşa sarılıp sırtta taşınan bohça yükü
  حولت كسائي إذا جعلت فيه شيئا ثم حملته على ظهرك والاسم الحال (ayn); الحال الكارة التي يحملها الرجل على ظهره وتحول الرجل إذا حمل الكارة (sihah)
- **B013** yumuşak toprak veya kara çamur — yumuşak toprak veya kara çamur
  الحال التراب اللين الذي يقال له السهلة (ayn); الحال الطين الأسود (sihah)
- **B014** çocuk yürüme aracı — çocuğun üzerinde yürüdüğü küçük tekerlekli araç
  الحال الدراجة التي يذرج عليها الصبي وهي كالعجلة الصغيرة (sihah)
- **B015** harman döven demirli araç — ahşabına bağlı demirlerle harman döven araç
  الحيلان الحدائد بخشبها يداس بها الكدس (ayn)
- **B016** su çekme düzeneği — üzerinden su çekilen döner düzenek
  المحالة منجنون يستقى عليه والجميع محاول (ayn)

## ي و م (root_001700): 42:7 يَوْمَ, 42:45 يَوْمَ, 42:47 يَوْمٌ

- **B001** güneşin doğuşundan batışına kadarki gün — güneşin doğuşundan batışına kadarki gün · bu anlamdaki günlerin çoğulu · gün gün veya gündelik esasa göre yapılan işlem
  اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)
- **B002** herhangi bir zaman dilimi; bağlama göre devir — herhangi bir zaman dilimi; bağlama göre devir · iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali
  مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)
- **B003** büyük olayın yaşandığı çetin gün veya olay — büyük olay, olayın gerçekleştiği kritik gün veya çetin gün · çok çetin gün veya savaş günü · bilinen günlerde gerçekleşmiş olaylar · çok çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün
  يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)
- **B004** Tanrı'nın nimet ve ibret verici işleriyle anılan günler [kalıp] — Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri
  وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)
- **B005** bağlamda işaret edilen o gün veya o sırada — o gün; o sırada
  يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)

## ج م ع (root_000259): 42:7 ٱلْجَمْعِ, 42:15 يَجْمَعُ, 42:29 جَمْعِهِمْ

- **B001** dağınık parçaları bir araya toplama — dağınık şeyi bir araya toplamak · mal biriktirmek ve saymak · ayrı yerlerdeki şeyleri bütünüyle bir araya getirmek · çeşitli yerlerden toplanmış şey · çeşitli yerlerden toplanıp götürülen yağma malı
  أصل واحد يدل على تضام الشيء (maqayis)؛ الجمع مصدر جمعت الشيء (ayn)؛ الجمع خلاف التفريق جمعت الشيء إذا ضممت بعضه إلى بعض (jamhara)؛ جمعت الشئ المتفرق فاجتمع (sihah)؛ الجمع أن تجمع شيئا إلى شيء (tahdhib)؛ الجمع ضم الشيء بتقريب بعضه من بعض (mufradat)
- **B002** bir araya gelmiş insan topluluğu — insan topluluğu veya çokluk · farklı boylardan karışık insan topluluğu · toplanmış topluluk veya ordu
  الجماع الأشابة من قبائل شتى (maqayis)؛ الجمع اسم لجماعة الناس والجموع اسم لجماعة الناس (ayn)؛ الجماع ما تجمع من أشابة الناس وأخلاطهم (jamhara)؛ جماع الناس أخلاطهم وهم الأشابة من قبائل شتى (sihah)؛ الجماع يقال في أقوام متفاوتة اجتمعوا (mufradat)
- **B003** düşünüp kesin bir tutuma bağlanma — bir işi yapmaya kesin biçimde karar vermek · hazırlık, kesin karar veya görüş birliği · işi veya düzeni sağlamlaştırıp kesinleştirmek
  أجمعت على الأمر إجماعا وأجمعته (maqayis)؛ أجمعت على الأمر إجماعا إذا عزمت عليه (jamhara)؛ أجمعت الأمر وعلى الأمر إذا عزمت عليه (sihah)؛ الإجماع الإعداد والعزيمة على الأمر (tahdhib)؛ أجمعت كذا فيما يكون جمعا يتوصل إليه بالفكرة (mufradat)
- **B004** toplanmayla belirlenen yer veya gün — insanların toplandığı yer · insanların bir araya geldiği kutsal yer veya günler için kullanılan ad · insanların ibadet veya yeniden diriliş için toplandığı gün · haftalık toplu ibadete katılıp namazı kılmak · halkı toplu ibadet için bir araya getiren ibadet yeri · ibadet için toplanma çağrısı · yolunu yitirme korkusuyla insanların ayrılmadığı ıssız alan
  جمع مكة سمي لاجتماع الناس به وكذلك يوم الجمعة (maqayis)؛ المجمع حيث يجمع الناس (ayn)؛ أيام جمع أيام منى والجمعة مشتقة من اجتماع الناس فيها للصلاة (jamhara)؛ يقال للمزدلفة جمع لاجتماع الناس فيها (sihah)؛ يوم الجمع ويوم يجمعكم ليوم الجمع (mufradat)
- **B005** sıkılmış avuç veya bir avuçluk miktar — sıkılmış avuç veya bu avuçla vurma · bir avuç dolusu
  ضربته بجمع كفي وجمع كفي (maqayis)؛ ضربته بجمع كفي وأعطيته من الدراهم جمع الكف (ayn)؛ ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها (jamhara)؛ جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه (sihah)
- **B006** cinsel birleşme — cinsel birleşme için kullanılan örtülü söz · cinsel ilişkide bulunma
  الجماع كناية عن النكاح (jamhara)؛ المجامعة المباضعة (sihah)
- **B007** çocuğu karnındayken ölen veya el değmemiş kalan kadın — çocuğu karnındayken veya el değmemişken ölmek · kocasıyla cinsel birleşme yaşamamış kadın · ilk kez gebe kalan dişi eşek
  ماتت بجمع أي في بطنها ولد (maqayis)؛ ماتت المرأة بجمع أي مع ما في بطنها وكذلك إذا ماتت عذراء (ayn)؛ ماتت المرأة بجمع إذا ماتت وولدها في بطنها (jamhara)؛ أمر بني فلان بجمع أي لم يقتضها وماتت فلانة بجمع أي ماتت وولدها في بطنها (sihah)
- **B008** elleri boyna bağlayan kelepçe — elleri boyna bağlayan kelepçe veya demir bağ
  الجوامع الأغلال (maqayis)؛ الجوامع الأغلال الواحدة جامعة (jamhara)؛ الجامعة الغل لأنها تجمع اليدين إلى العنق (sihah)
- **B009** eksiksiz bütünlük — bedeni eksiksiz hayvan veya varlık · bedence derli toplu veya gelişimini tamamlamış adam · büyüyüp bütün dış giysileri giyecek çağa gelmek · bütünlük bildiren pekiştirme sözleri · dağılmamış bütün veya hepsi
  الجمعاء من البهائم وغيرها التي لم يذهب من بدنها شيء (maqayis)؛ رجل جميع أي مجتمع في خلقه (ayn)؛ الرجل المجتمع الذي بلغ أشده (sihah)؛ جميع لدينا محضرون (mufradat)
- **B010** parçaları toplanıp tamamlanma [kalıp] — koşusunu ve gücünü bütünüyle toplamak · çeşitli yerlerden birleşip büyümek · işlerin kişi için yoluna girip hazır duruma gelmesi
  استجمع الفرس جريا (maqayis)؛ استجمع للمرء أموره (ayn)؛ استجمع السيل اجتمع من كل موضع واستجمع الفرس جريا (sihah)
- **B011** adı bilinmeyen çekirdekten yetişme hurma ağacı — adı bilinmeyen çekirdekten yetişme hurma ağacı
  الجمع كل لون من النخل لا يعرف اسمه لنخل خرج من النوى (maqayis)؛ الجمع أيضا الدقل لنخل يخرج من النوى ولا يعرف اسمه (sihah)
- **B012** büyük kazan — büyük kazan
  قدر جماع وجامعة وهي العظيمة (maqayis)؛ قدر جامعة وهي العظيمة وقدر جماع أيضا للعظيمة (sihah)
- **B013** bir işte başkasıyla birleşip destek olma [kalıp] — bir işte başkasıyla birleşip ona destek olmak
  جامعت الرجل على الأمر مجامعة وجماعا إذا مالأته عليه (jamhara)؛ جامعه على أمر كذا أي اجتمع معه (sihah)

## ر ي ب (root_000616): 42:7 رَيْبَ, 42:14 مُرِيبٍ

- **B001** kuşku ve güvensizlik — kuşku ve zihinsel kararsızlık · suçlayıcı kuşku ve güven eksikliği · bende kuşku ve korku uyandırdı · bende kuşku uyandırdı · kuşkulu duruma geldi veya kuşku uyandırır oldu · ondan veya o şeyden kuşkulandı · onda kuşku uyandıran bir belirti gördü · kuşku duyan veya kuşku uyandıran
  الريب الشك (maqayis;ayn;jamhara;sihah)؛ الريب التهمة (jamhara)؛ ما رابك من أمر تخوفت عاقبته (ayn)؛ رابني هذا الأمر إذا أدخل عليك شكا وخوفا (maqayis;ayn)؛ الريبة اسم من الريب تدل على دغل وقلة يقين (mufradat)؛ أراب الرجل صار ذا ريبة (maqayis;ayn;sihah)؛ ارتبت به أي ظننت به (ayn)
- **B002** zamanın değişimleri ve olayları [kalıp] — zamanın değişimleri, olayları ve terslikleri · ölümün ne zaman geleceğine ilişkin korkulan olaylar
  ريب الدهر صروفه (maqayis;jamhara;mufradat)؛ الريب صرف الدهر وعرضه وحدثه (ayn)؛ ريب المنون حوادث الدهر (sihah)؛ ريب المنون من جهة وقته لا من جهة كونه (mufradat)
- **B003** karşılanması gereken gereksinim — elden kaçırma kaygısıyla aranan gereksinim
  الريب الحاجة (sihah)؛ فيقال إن الريب الحاجة (maqayis)؛ طالب الحاجة شاك على ما به من خوف الفوت (maqayis)

## ف ر ق (root_001148): 42:7 فَرِيقٌ, 42:7 وَفَرِيقٌ, 42:13 تَتَفَرَّقُوا۟, 42:14 تَفَرَّقُوٓا۟

- **B001** ayırt edip birbirinden ayırma — iki şeyi birbirinden ayırıp ayırt etmek · kişilerin birbirinden ayrılması ve uzaklaşması · konunun açıklığa kavuşması · metni sağlamlaştırıp hükümlerini açıklamak ve bölümlendirmek
  أصيل صحيح يدل على تمييز وتزييل بين شيئين (maqayis)؛ الفرق تفريق بين شيئين حتى يفترقا ويتفرقا (ayn)؛ فرقت بين الشيئين أفرق فرقا وفرقانا (sihah)؛ فرقت أفرق بين الكلام وفرقت بين الأجسام (tahdhib)؛ فرقت بين الشيئين فصلت بينهما سواء كان ذلك بفصل يدركه البصر أو بفصل تدركه البصيرة (mufradat)؛ الفراق والمفارقة تكون بالأبدان أكثر (mufradat)؛ فرق لي هذا الأمر إذا تبين ووضح (tahdhib)
- **B002** parçalara ayırıp dağıtma — parçalara ayırma ve dağıtma · ayrı zamanlarda bölümler halinde ulaştırmak · sürüyü dağıtan kokarca
  أخذت حقي منه بالتفاريق (sihah)؛ قرآنا فرقناه من شدد قال أنزلناه مفرقا في أيام (sihah)؛ نزل متفرقا (tahdhib)؛ والتفريق أصله للتكثير ويقال ذلك في تشتيت الشمل والكلمة (mufradat)؛ يفرقون به بين المرء وزوجه (mufradat)؛ إن الذين فرقوا دينهم وقرئ فارقوا (mufradat)؛ ومفرق النعم هو الظربان لأنه إذا فسا بينها وهي مجتمعة تفرقت (sihah)
- **B003** doğruyu yanlıştan ayıran ölçüt veya araç — doğruyu yanlıştan ayıran kitap, kanıt, aydınlık veya destek · doğru ile yanlışın ayrıldığı belirleyici gün · doğruyu yanlıştan hakça ayıran kişi
  الفرقان كتاب الله تعالى فرق به بين الحق والباطل (maqayis)؛ الفرقان كل كتاب أنزل به فرق الله بين الحق والباطل (ayn)؛ يجعل لكم فرقانا أي حجة ظاهرة وظفرا (ayn)؛ كل ما فرق به بين الحق والباطل فهو فرقان (sihah)؛ سمى الله الكتاب المنزل على محمد فرقانا وسمى الكتاب المنزل على موسى فرقانا (tahdhib)؛ يوم الفرقان هو يوم بدر (tahdhib;mufradat)؛ الفرقان أبلغ من الفرق لأنه يستعمل في الفرق بين الحق والباطل (mufradat)؛ نورا وتوفيقا على قلوبكم يفرق به بين الحق والباطل (mufradat)
- **B004** yarılma ve ayrılan parça — yarılmış şeyden ayrılan parça veya su kütlesi · sabahın sökmesi ve aydınlığın yarılarak belirmesi
  الفرق الفلق من الشيء إذا انفلق (maqayis)؛ فانفلق فكان كل فرق كالطود العظيم (maqayis;sihah;mufradat)؛ كل فرق كالطود العظيم يريد من الماء (ayn)؛ انفرق الصبح أي انفلق والفرق هو الفلق (ayn)؛ فانفرق البحر فصار كالجبال العظام (tahdhib)؛ الفرق الموجة والفرق الجبل والفرق الهضبة (tahdhib)؛ الفرق يقارب الفلق لكن الفلق يقال اعتبارا بالانشقاق والفرق يقال اعتبارا بالانفصال (mufradat)
- **B005** ana bütünden ayrılmış topluluk — ayrı insan topluluğu veya grup · koyun sürüsü veya sürüden ayrılan küçük koyun grubu
  الفرق القطيع من الغنم (maqayis)؛ الفريقة وهو القطيع من الغنم كأنها قطعة فارقت معظم الغنم (maqayis)؛ الفرق طائفة من الناس ومن كل شيء والفريق من الناس أكثر من الفرق (ayn)؛ الفرق بالكسر القطيع من الغنم العظيم (sihah)؛ الفرقة طائفة من الناس والفريق أكثر منهم (sihah)؛ الفريقة فريقة الغنم أن تنفرق منها قطعة أو شاة أو شاتان أو ثلاث شياه (tahdhib;sihah)؛ الفريق الجماعة المتفرقة عن آخرين (mufradat)
- **B006** ayrım çizgisi veya çatallanma noktası — saç ayrımı ve saçın ayrıldığı yer · yol ayrımı veya yolun çatallanma noktası
  من ذلك الفرق فرق الشعر (maqayis)؛ الفرق موضع المفرق من الرأس في الشعر (ayn)؛ المفرق والمفرق وسط الرأس وهو الذي يفرق فيه الشعر وكذلك مفرق الطريق ومفرقه (sihah)؛ فرق له الطريق أي اتجه له طريقان (sihah)؛ الفرق مصدر فرقت الشعر (tahdhib)؛ لا يفرق شعره إلا أن ينفرق هو (tahdhib)
- **B007** beden yapısında doğuştan ayrıklık veya eşitsizlik — beden yapısı doğuştan ayrık, aralıklı veya eşitsiz olan
  الأفرق الديك الذي عرفه مفروق والفرق في الخيل أن يكون أحد وركيه أرفع من الآخر (maqayis)؛ الأفرق كالأفلج والأفرق يكون خلقة (ayn)؛ شاة فرقاء بعيدة ما بين الطبيين والأفرق من ذكورها بعيد ما بين الخصيتين (ayn)؛ تباعد ما بين الثنيتين وما بين المنسمين (sihah)؛ ديك أفرق بين الفرق للذي عرفه مفروق (sihah)؛ الأفرق من الخيل الذي نقصت إحدى فخذيه عن الأخرى (tahdhib)؛ الأفرق من الديك ما عرفه مفروق ومن الخيل ما أحد وركيه أرفع من الآخر (mufradat)
- **B008** doğum sancısıyla sürüden ayrılıp başıboş giden dişi deve — doğum sancısıyla sürüden ayrılıp başıboş giden dişi deve · yavrusu ölerek kendisinden ayrılmış dişi deve · öteki bulutlardan ayrı duran tek bulut
  الفارق الخلفة تذهب في الأرض نادة من وجع المخاض (maqayis)؛ سميت بذلك لأنها فارقت سائر النوق (maqayis)؛ تشبه السحابة تنفرد عن السحاب بهذه الناقة (maqayis)؛ الناقة إذا مخضت تفرق فروقا وهو نفارها وذهابها نادة من الوجع (ayn)؛ فرقت الناقة إذا أخذها المخاض فندت في الأرض (sihah)؛ ناقة مفرق أي فارتها ولدها بموت (sihah)؛ السحابة المنفردة لا تخلف (tahdhib)؛ أفرقنا إبلنا العام إذا حلوها في المرعى (tahdhib)؛ الناقة التي تذهب في الأرض نادة من وجع المخاض فارق وبها شبه السحابة المنفردة (mufradat)
- **B009** yüreği dağıtan korku ve yoğun ürküntü — korku, yoğun ürküntü veya çok korkak olma
  رجل فروقة وامرأة فروقة وقد فرق فرقا فهو فرق من الخوف (ayn)؛ الفرق بالتحريك الخوف وقد فرق بالكسر (sihah)؛ الفرق أيضا الخوف وقد فرق يفرق فرقا (tahdhib)؛ رجل فروقة وفروقة وفاروقة وهو الفزع الشديد الفرق (tahdhib)؛ الفرق تفرق القلب من الخوف (mufradat)
- **B010** hastalıktan kurtulup kendine gelme — hastalıktan kurtulup iyileşmek ve kendine gelmek
  إفراق المحموم من حماه وإنما يكون كذا لأنها فارقته (maqayis)؛ المطعون إذا برأ قيل أفرق إفراقا (ayn)؛ أفرق المريض من مرضه والمحموم من حماه أي أقبل (sihah)؛ ما علامة برء المحموم فقال العرق (sihah)؛ المطعون إذا برأ قيل أفرق يفرق إفراقا (tahdhib)؛ كل عليل أفاق من علته فقد أفرق (tahdhib)
- **B011** kap olarak kullanılan tarihsel hacim ölçüsü — kapasitesi aktarıma göre değişen tarihsel ölçü kabı veya hacim birimi
  مما شذ عن هذا الباب الفرق مكيال من المكاييل (maqayis)؛ الفرق مكيال ضخم لأهل العراق (ayn)؛ الفرق مكيال معروف بالمدينة وهو ستة عشر رطلا (sihah)؛ إناء يقال له الفرق (tahdhib)؛ إناء يأخذ ستة عشر مدا وذلك ثلاثة آصع (tahdhib)
- **B012** hurma ve çemenle pişirilen iyileştirici yiyecek — hurma ve çemenle pişirilen besleyici veya iyileştirici karışım
  الفريقة تمر يطبخ بحلبة يتداوى به (maqayis)؛ الفريقة تمر يطبخ بأشياء يتداوى بها (ayn)؛ الفريقة تمر يطبخ بحلبة للنفساء (sihah)؛ الفريقة التمر والحلبة تجعل للنفساء (tahdhib)؛ لون الفريقة صفيت للمدنف (tahdhib;sihah)؛ الفريقة تمر يطبخ بحلبة (mufradat)
- **B013** böbrek çevresi yağı — böbreğin veya böbreklerin çevresindeki yağ
  الفروقة شحم الكليتين (maqayis;tahdhib;mufradat)؛ الفروقة شحم الكلية (ayn)؛ شحم الفروقة والكلى (maqayis;ayn;tahdhib)
- **B014** seyrek ve kesintili bitki örtülü arazi [kalıp] — bitki örtüsü seyrek ve kesintili arazi
  هذه أرض فرقة وفي نبتها فرق إذا كان متفرقا ولم يكن منصلا (sihah)؛ أرض فرقة في نبتها فرق إذا لم تكن واصية متصلة النبات (tahdhib)
- **B015** ayırt edilen türler ve yönler — bir şeyin ayırt edilen türü veya anlatının ayrı yönü
  الماشطة تمشط كذا فرقا أي ضربا (ayn;tahdhib)؛ وقفت فلانا على مفارق الحديث أي على وجوهه (tahdhib)
- **B016** hareketle kenara çekilip dağılma — hareketle kenara çekilip birbirinden ayrılarak dağılmak
  افرنقعوا إذا تنحوا (maqayis)؛ كلمة منحوتة من فرق وفقع لأنهم يتفرقون فيكون لهم عند ذلك فقعة وحركة (maqayis)

## ج ن ن (root_000266): 42:7 ٱلْجَنَّةِ, 42:22 ٱلْجَنَّاتِ

- **B001** örtme ve duyulardan gizleme — örtmek; gizleyecek bir örtü sağlamak; içinde saklamak · bir şeyin arkasına gizlenmek · insanı örten giysi veya örtü
  الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)
- **B002** gecenin karartıp örtmesi — gecenin kararıp üzerini örtmesi · gecenin koyu karanlığı ve nesneleri örtmesi
  جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)
- **B003** zemini ağaçlarla örtülü bahçe — zemini ağaçlarla örtülü bahçe veya koruluk
  الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)
- **B004** ölüm sonrası gizli nimetler yurdu — ölüm sonrası ödül ve gizli nimetler yurdu
  الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)
- **B005** gözle görülmeyen ruhani varlıklar topluluğu — gözle görülmeyen ruhani varlıklar · görünmeyen varlıkların atası veya bir bireyi · görünmeyen ruhani varlıkların topluluğu · görünmeyen ruhani varlıkların çok bulunduğu yer
  الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)
- **B006** aklı örten akıl yitimi — aklını yitirmek; aklını yitirmiş duruma getirmek · akıl yitimi; benlik ile akıl arasındaki engel · aklını yitirmiş gibi davranmak
  الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)
- **B007** ana rahmindeki doğmamış çocuk — ana rahmindeki doğmamış çocuk · rahminde çocuk taşımak; çocuğun rahimde saklı kalması
  الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)
- **B008** koruyucu siper veya savaş donanımı — koruyucu örtü, siper veya savaş donanımı · kalkan
  المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)
- **B009** ölüyü örtüp gömme — ölüyü örtmek ve gömmek · gömüt; ölü örtüsü; gömülmüş kişi
  الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)
- **B010** duyulardan saklı yürek ve gizli yön — yürek veya yüreğin saklı iç yönü · gizli iş veya görünmeyen yön
  الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)
- **B011** bitkinin güçlenip boylanması ve sıklaşması — bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması · uzun ağaç; bol otlu ve henüz otlanmamış arazi
  جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)
- **B012** yılan, özellikle beyaz bir tür — yılan, beyaz yılan veya belirli bir yılan türü
  الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)
- **B013** halkın büyük kitlesi — insanların çoğunluğu veya halkın büyük kitlesi
  جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)
- **B014** bir şeyin ilk ve yeni dönemi — gençliğin, çocukluğun veya bir dönemin ilk başlangıcı
  كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)
- **B015** uçuş sırasında çoğalan sinek vızıltısı — sineğin vızıltısının veya sesinin çoğalması · böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması
  جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)
- **B016** göğüs kemikleri ve kaburga uçları — göğüs kemikleri veya kaburgaların göğse yakın uçları
  الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)
- **B017** içine girilip saklanılan yer — saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı
  المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)

## س ع ر (root_000708): 42:7 ٱلسَّعِيرِ

- **B001** ateşin tutuşması, yakılıp harlanması; ateş, yakıt, sıcaklık ve harlama aracı — ateşin yanışı, yakıtı ve yanmasını sağlayan şey · ateşi yakmak ve harlamak · ateş tutuşup alevlenmek · alevli ateş · ateş karıştırma ve harlama aracı · ateşin yakıcı sıcaklığı
  أصل واحد يدل على اشتعال الشيء واتقاده (maqayis); السعير نار (maqayis); السعر وقود النار (ayn); سعرت النار هيجتها وألهبتها (sihah); سعرت النار إذا أوقدتها وهي مسعورة (tahdhib); السعر التهاب النار (mufradat); المسعر الخشب الذي يسعر به (maqayis;sihah;mufradat)
- **B002** savaşı ve kötülüğü alevlendirmek; yakıcı saldırı ya da taşkın yayılma yaratmak [kalıp] — savaşı körükleyip kızıştırmak · savaşı sürekli körükleyen kişi ya da etken · üzerlerine kötülük salmak · onları oklarla yakıp acıtmak · hırsızlar taşkınca harekete geçip yayılmak
  السعر وقود النار والحرب (ayn); سعرت النار والحرب هيجتهما وألهبتهما (sihah); سعرناهم بالنبل أي أحرقناهم وأمضضناهم (sihah); رجل مسعر حرب (sihah;tahdhib); سعرت نار الحرب واستعرت النار (tahdhib); استعر الحرب واللصوص نحو اشتعل (mufradat); سعرهم شرا (maqayis;sihah)
- **B003** piyasa fiyatı ve fiyat belirleme — malın ya da yiyeceğin piyasa fiyatı · piyasa esnafı bir fiyatta anlaşmak veya fiyat belirlemek
  السعر سعر السوق الذي تقوم عليه بالثمن (ayn); أسعر أهل السوق إسعارا وسعروا تسعيرا (ayn); السعر واحد أسعار الطعام والتسعير تقدير السعر (sihah); السعر من الأسعار وهو الذي يقوم عليه الثمن (tahdhib); السعر في السوق تشبيها باستعار النار (mufradat); سعر الطعام من هذا لأنه يرتفع ويعلو (maqayis)
- **B004** yakıcı bedensel şiddet, çılgın taşkınlık ve ağır acı; ayrıca ateşin harareti — delilik; çekilen ağır acı ve ceza · keskin ve çılgınca davranan deve · sıcak rüzgârdan, şiddetli açlıktan ya da susuzluktan kavrulmak · açlığın ve susuzluğun yakıcı şiddeti · sapma içinde delilik ya da ağır acı
  السعار حر النار (maqayis;tahdhib;mufradat); سعر الرجل إذا ضربته السموم (maqayis;sihah); السعار شدة الجوع أيضا (sihah); السعر أيضا الجنون (maqayis;sihah); ناقة مسعورة أي مجنونة (maqayis;sihah); العناء والعذاب خاصة (sihah;tahdhib); سعار العطش التهابه وسعار الجوع لهيبه (tahdhib); سعر الرجل فهو مسعور إذا اشتد جوعه أو عطشه (tahdhib); ناقة مسعورة نحو موقدة ومهيجة (mufradat)
- **B005** devede uyuzun başladığı ya da şiddetlendiği koltuk altı, kasık ve benzeri bölgeler — devenin uyuzun başladığı koltuk altı, kasık ve benzeri kıvrım bölgeleri · uyuz devenin kıvrım bölgelerinde başlamak veya şiddetlenmek
  مساعر البعير آباطة وأرفاغه واصل ذنبه حيث رف وبره (maqayis); الجرب يستعر فيها أولا ويستعر فيها أشد (maqayis); مساعر الإبل آباطها وأرفاغها (sihah); استعر الجرب في البعير إذا ابتدأ بمساعره (sihah); مساعر البعير حيث يستعر فيه الجرب من الآباط والأرفاغ وأم القراد والمشافر (tahdhib)
- **B006** güneş ışığı demetinde görülen uçuşan ince toz — güneş ışığında görülen uçuşan ince toz
  السعرارة هي التي تراها في الشمس كالهباء (maqayis); السعرارة الهباء في الشمس (sihah); السعرارة ما تردد في الضوء الساقط في البيت من الشمس وهو الهباء المنبث (tahdhib)
- **B007** iş için dolaşıp yayılmak; hızla koşmak veya ayakları dağınık biçimde ilerlemek — bugün işimin peşinde dolaştım · deve hızla yürümek · ayaklarını dağınık savurarak ilerleyen at · koşunun şiddeti ve hızı
  سعرت اليوم في حاجتي أي طفت (sihah;tahdhib); سعرت الناقة إذا أسرعت في سيرها فهي سعور (tahdhib); فرس مسعر ومساعر وهو الذي تطيح قوائمه متفرقة ولا ضبر له (tahdhib); السعران شدة العدو (tahdhib); استعر الناس في كل وجه (tahdhib)
- **B008** esmerden biraz koyu, siyaha çalan ten rengi — esmerden biraz koyu, siyaha çalan renk
  السعرة لون إلى السواد (sihah); السعرة في الإنسان لون يضرب إلى سواد فويق الأدمة (tahdhib)
- **B009** toprağa kazılmış ekmek fırını — toprağa kazılmış ekmek fırını
  الساعورة كهيئة التنور يحفر في الأرض يختبز فيه (tahdhib)
- **B010** keskin öksürük; bir işin ilk ve en sert evresi — keskin ve şiddetli öksürük · işin ilk ve sert evresi
  السعيرة تصغير السعرة وهي السعال الحاد (tahdhib); هذا سعرة الأمر أي أوله وحدته (tahdhib)
- **B011** uzun; güçlü, sert veya şiddetli — uzun veya güçlü ve sert
  المسعر أيضا الطويل (sihah); المسعر الشديد (tahdhib); المسعر الطويل (tahdhib)

## ش ي ء (root_000831): 42:8 شَآءَ, 42:8 يَشَآءُ, 42:9 شَىْءٍ, 42:10 شَىْءٍ, 42:11 شَىْءٌ, 42:12 يَشَآءُ, 42:12 شَىْءٍ, 42:13 يَشَآءُ, 42:19 يَشَآءُ, 42:22 يَشَآءُونَ, 42:24 يَشَإِ, 42:27 يَشَآءُ, 42:29 يَشَآءُ, 42:33 يَشَأْ, 42:36 شَىْءٍ, 42:49 يَشَآءُ, 42:49 يَشَآءُ, 42:49 يَشَآءُ, 42:50 يَشَآءُ, 42:51 يَشَآءُ, 42:52 نَّشَآءُ

- **B001** varlık, olgu ya da konu — şey; varlık, olgu ya da konu · şeyler; varlıklar, olgular ya da konular · hiçbir şey yok; istenen bir şey yok
  الشيء واحد الأشياء (ayn); الشئ والجمع أشياء (sihah); أشياء جمع شيء (tahdhib); الذي يصح أن يعلم ويخبر عنه (mufradat)
- **B002** isteme ve gerçekleşmesini dileme — isteme; bir şeyin olmasını dileme · istedi, olmasını diledi · Tanrı'nın istemesiyle · Tanrı isterse
  المشيئة مصدر شاء يشاء (ayn); المشيئة الإرادة وقد شئت الشئ أشاؤه (sihah); الشيئة مصدر شاء يشاء مشيئة (tahdhib); المشيئة عند أكثر المتكلمين كالإرادة وفي الأصل إيجاد الشيء وإصابته (mufradat)
- **B003** bir işe ya da hedefe sevk etmek — adamı o işe yöneltti · onu zorlayıp getirdi · seni oraya getirir
  شيأت الرجل على الامر حملته عليه; وأشاءه لغة في أجاءه أي ألجأه; يشيئك إلى مخة عرقوب بمعنى يجيئك
- **B004** yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yaradılışı bozuk, görünüşü çirkin
  شيأ الله وجهه إذا دعا عليه بالقبح (maqayis); رجل مشيأ الخلق قبيح المنظر (jamhara); المشيأ المختلف الخلق القبيح وقد شيأ الله خلقه أي قبحه (tahdhib)
- **B005** özlem duymak; beğenip sevinmek [kalıp] — bu bende özlem uyandırdı · onu beğendim ve sevindim
  شاءني الشيء مثل شاعني إذا شاقني (jamhara); شؤت به أعجبت به وسررت (tahdhib)
- **B006** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت
- **B007** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان البعيد النظر وينعت به الفرس
- **B008** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل واحدها أشاءة
- **B009** yakınma ve şaşma ünlemi — Eyvah, ne haldeyim! · Vay, ne güzel!
  ياشيء مالي معناه الأسف والتلهف والحزن; يتعجب بشيء وهيء وفيء ويقول يا شيما أي ما أحسن هذا

## ش ي ء (root_000832): 42:8 شَآءَ, 42:8 يَشَآءُ, 42:9 شَىْءٍ, 42:10 شَىْءٍ, 42:11 شَىْءٌ, 42:12 يَشَآءُ, 42:12 شَىْءٍ, 42:13 يَشَآءُ, 42:19 يَشَآءُ, 42:22 يَشَآءُونَ, 42:24 يَشَإِ, 42:27 يَشَآءُ, 42:29 يَشَآءُ, 42:33 يَشَأْ, 42:36 شَىْءٍ, 42:49 يَشَآءُ, 42:49 يَشَآءُ, 42:49 يَشَآءُ, 42:50 يَشَآءُ, 42:51 يَشَآءُ, 42:52 نَّشَآءُ

- **B001** isteme ve dileme — isteme; olmasını dileme · isteme, dileme · istedi, olmasını diledi
  للشيئة مصدر شاء يشاء مشيئة (tahdhib)
- **B002** yüzü veya yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yüzü veya yaradılışı bozuk ve çirkin
  شَيَّأ الله وجهه إذا دعا عليه بالقبح؛ وجه مشيأ (maqayis); المشيأ المختلف الخلق، القبيح، وقد شَيَّأ الله خلقه أي قبحه؛ المشيأ مثل المؤبن (tahdhib)
- **B003** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان: البعيد النظر، وينعت به الفرس (tahdhib)
- **B004** beğenip sevinmek [kalıp] — onu beğendim ve sevindim
  شؤت به: أعجبت به وسررت (tahdhib)
- **B005** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت (tahdhib)
- **B006** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل، واحدها أشاءة (tahdhib)
- **B007** yakınma ve şaşma ünlemleri — Eyvah, ne haldeyim! · Eyvah, ne haldeyim! · Vay!; şaşma ünlemi · Vay, ne güzel!
  يافيء مالي، وياشيء مالي، وياهيء مالي، معناه كله الأسف والتلهف والحزن؛ يا شيء مالي ويا شي مالي يهمز ولا يهمز؛ من يتعجب بشيء وهيء وفيء؛ يا شيما أي ما أحسن هذا (tahdhib)

## ج ع ل (root_000248): 42:8 لَجَعَلَهُمْ, 42:11 جَعَلَ, 42:50 وَيَجْعَلُ, 42:52 جَعَلْنَٰهُ

- **B001** bir şeyi yapıp var etme — bir şeyi yapmak, yaratmak veya var etmek
  جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)
- **B002** birini veya şeyi belirli bir duruma getirme — bir şeyi belirli bir duruma, niteliğe veya konuma getirmek · bir şeyi belirli bir duruma getirmek
  جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)
- **B003** öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma — 
  جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)
- **B004** bir eylemi yapmaya başlama — bir şeyi yapmaya başlamak
  تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)
- **B005** iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme — bir iş karşılığında belirlenen ücret, ödeme veya ödül · önemli bir iş için ortaklaşa kararlaştırılan ödemeler · ona bir ödeme veya armağan ayırmak
  الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)
- **B006** kısa veya küçük hurma ağaçları — kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri
  الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)
- **B007** sıcak tencereyi indirme bezi ve onunla indirme — sıcak tencereyi ateşten indirmeye yarayan koruyucu bez · tencereyi koruyucu bezle ateşten indirmek
  الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)
- **B008** kara küçük yer hayvanı ve bunlarla dolu su — kara renkli küçük bir yer hayvanı · bu hayvanların çokça bulunduğu su
  الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)
- **B009** dişinin çiftleşmek için erkeği istemesi — çiftleşmek isteyen dişi köpek · dişinin çiftleşmek için erkeği istemesi
  كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)
- **B010** deve kuşu yavrusu — deve kuşu yavrusu
  الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)
- **B011** belirtilmemiş bir yer adı — kimliği belirtilmemiş bir yer adı
  الجَعْلة اسم مكان (maqayis)
- **B012** kısa, şişman ve inatçı olma — kısa, şişman ve inatçı kişi
  الجعل القصر مع السمن واللجاج (tahdhib)

## و ح د (root_001631): 42:8 وَٰحِدَةً

- **B001** tek başına ve ayrı olma — tek başına ve ayrı olma · tek başına · tek başına olan · kimsesiz ve tek başına olan · ötekilerden ayrı olarak · yalnız, kimsesiz · tek başına kaldı · öteki tepelerden ayrı duran tepecik · bu konuda yalnız değilim · kendi görüşünde tek kaldı
  أصل واحد يدل على الانفراد (maqayis)؛ الوحد المنفرد (ayn)؛ رجل واحد منفرد (jamhara)؛ الوحدة الانفراد ورجل وحد ووحيد أي منفرد (sihah)؛ الوحدة الانفراد والوحد المفرد (mufradat)
- **B002** bir sayısı, birer birerlik ve tek parça — birer birer, tek tek · bir sayısı · bir; ikisinden biri · on birinci · birlerden oluşan topluluk; tekler · teker teker · bir bütünün tek parçası
  الواحد أول عدد من الحساب (ayn)؛ الواحد أول العدد والأحد مثل الواحد وأحاد أحاد واحد واحد (jamhara)؛ الواحد أول العدد وأحاد ووحاد وموحد والميحاد (sihah)؛ لمبدإ العدد كقولك واحد اثنان (mufradat)
- **B003** övgüde ya da yergide eşi benzeri olmama — kabilesinde eşi olmayan · eşi benzeri olmayan · yergide benzeri olmayan · kötülükte eşi olmayan · çağının eşsizi · çağdaşları arasında eşsiz · benzeri olmayan, eşsiz · eşi benzeri olmayan
  واحد قبيلته إذا لم يكن فيهم مثله ونسيج وحده (maqayis)؛ لا يقارعه في الفضل أحد (ayn)؛ فلان واحد دهره أي لا نظير له وأوحد أهل زمانه (sihah)؛ واحد لعدم نظيره ونسيج وحده وعيير وحده وجحيش وحده (mufradat)
- **B004** Tanrı'nın tek, ortaksız ve bölünmez oluşu ve buna inanma — Tanrı'nın tek ve ortaksız olduğuna inanma · parçalanması ve çoğalması düşünülemeyen tek Tanrı · mutlak anlamda yalnız Tanrı için kullanılan tek nitelemesi · Tanrı'nın tek ve ortaksız oluşu
  التوحيد الإيمان بالله وحده لا شريك له والله الواحد الأحد ذو التوحد والوحدانية (ayn)؛ إذا وصف الله تعالى بالواحد فمعناه هو الذي لا يصح عليه التجزي ولا التكثر (mufradat)
- **B005** ortak bir yönden bir ve aynı sayılma — aynı anlamda veya aynı değerde · tür veya bağlantı bakımından bir olan
  الجلوس والقعود واحد وأصحابك وأصحابي واحد (ayn)؛ واحدا في الجنس أو في النوع وواحدا بالاتصال (mufradat)
- **B006** tek yavru doğurma veya çağının eşsizi kılma [kalıp] — tek yavru doğurdu · onu çağının eşsizi yaptı
  أوحدت الشاة فهي موحد أي وضعت واحدا؛ أوحده الله جعله واحد زمانه (sihah)

## د خ ل (root_000464): 42:8 يُدْخِلُ

- **B001** içeri girmek veya içeri sokmak — bir yere, zamana veya işe girmek · içeri girme veya giriş · başkasını ya da bir şeyi içeri sokmak · bir şeyin içine azar azar girmek · girme eylemi veya giriş yeri
  أصل مطرد منقاس وهو الولوج (maqayis)؛ دخل يدخل دخولا (maqayis)؛ ادخل في غار وتدخل فيه (ayn)؛ دخلت الدار وغيرها وأدخلت غيري (jamhara)؛ دخلت البيت وادخل وتدخل الشيء (sihah)؛ الدخول نقيض الخروج ويستعمل في المكان والزمان والأعمال (mufradat)
- **B002** eşiyle cinsel birleşmede bulunmak [kalıp] — eşiyle cinsel birleşmede bulunmak
  دخل بامرأته كناية عن الإفضاء إليها (mufradat)
- **B003** içte kalan yan — bir işin veya kişinin iç yüzü · giysinin bedene bakan iç kenarı · saklı tutulan iş veya açılan gizli iç yüz
  الدخلة باطن أمر الرجل وأنا عالم بدخلته (maqayis)؛ الدخلة بطانة من الأمر وعالم بدخلة أمرهم (ayn)؛ دخلل أمري إذا بثثته مكتومك (jamhara)؛ داخلة الإزار طرفه الذي يلي الجسد وداخلة الرجل باطن أمره (sihah)
- **B004** içten bozan kusur — içteki kusur, bozukluk veya kuşku · antları hile ve aldatma aracı yapmak · içten kusurlu, zayıf veya zihni bozuk · içi çürümüş palmiye · böcekçe yenmiş veya kurtlanmış yiyecek
  الدخل العيب في الحسب وكالدغل (maqayis)؛ دخل فلان وهو مدخول إذا كان في عقله دخل ونخلة مدخولة عفنة الجوف (maqayis)؛ عيب في الحسب وفي هذا الأمر دخل ودغل ودخل حسبه أو عقله (ayn)؛ في أمره دخل أي فساد (jamhara)؛ الدخل العيب والريبة ومكرا وخديعة ومدخول في عقله ونخلة مدخولة (sihah)؛ الدخل كناية عن الفساد والعداوة المستبطنة كالدغل ومدخول كناية عن بله في عقله وفساد في أصله (mufradat)
- **B005** sonradan araya katılan kimse — özel işlere alınan veya bir topluluğa dışarıdan katılan kimse · kişinin özel işlerine aldığı yakın kimse · bilmediği işlere zorla karışan kimse
  دخيلك الذي يداخلك في أمورك وبنو فلان في بني فلان دخيل (maqayis)؛ دخيلك الذي تدخله في أمورك ودخلل والمتدخل في الأمور المتكلف فيها (ayn)؛ فلان دخيل في بني فلان إذا كان من غيرهم (jamhara)؛ هم دخل في بني فلان ودخيل الرجل ودخلله الذي يداخله في أموره (sihah)؛ وعن الدعوة في النسب (mufradat)
- **B006** gelir — gelir veya içeri giren kazanç
  الدخل ما دخل ضيعة الإنسان من المنالة (ayn)؛ الدخل خلاف الخرج (sihah)
- **B007** develeri yeniden ya da araya katarak sulama — develeri ikinci kez suya götürme veya susuz deveyi sürüye katma
  الدخال في الورد أن تشرب الإبل ثم ترد إلى الحوض (maqayis)؛ سقيت الإبل دخالا إذا حملتها على الحوض ثانية والدخال في وجه آخر أن تحملها على الحوض بمرة واحدة عراكا (ayn)؛ أورد الرجل إبله دخالا (jamhara)؛ الدخال في الورد أن يشرب البعير ثم يرد من العطن إلى الحوض (sihah)؛ الدخال في الإبل أن يدخل إبل في أثناء ما لم تشرب لتشرب معها ثانيا (mufradat)
- **B008** iç içe geçme ve arada kalma — eklemlerin birbirine geçmesi · bir sinir üzerinde toplanmış et parçası · bir ana renge karışmış başka renkler · kuşun sırtıyla karnı arasındaki tüyler · ağaç köklerinin arasına girmiş ot
  كل لحمة مجتمعة دخلة والدخل من ريش الطائر ما بين الظهران والبطنان والدخل من الكلأ ما دخل منه في أصول الشجر (maqayis)؛ الدخلة في اللون تحليط من ألوان في لون والدخال مداخلة المفاصل بعضها في بعض (ayn)؛ كل لحمة مجتمعة على عصب فهي دخلة (jamhara)؛ الدخل من الكلأ ما دخل منه في أصول الشجر (sihah)
- **B009** sık ağaçlıkta barınan küçük kuş — oyuklarda ve sık ağaç altında barınan küçük kuş · bu küçük kuş adının bir çoğul biçimi · bu küçük kuş adının öteki çoğul biçimi
  بذلك سمي هذا الطائر دخلا (maqayis)؛ الدخل صغار الطير مأواها الغيران وبطون الأودية تحت شجر ملتف والجميع الدخاخيل (ayn)؛ الدخل طائر صغير وجمع دخل دخاخيل (jamhara)؛ الدخل طائر صغير والجمع الدخاليل (sihah)؛ الدخل طائر سمي بذلك لدخوله فيما بين الأشجار الملتفة (mufradat)
- **B010** taze palmiye meyvesi için küçük örgü sepet — taze palmiye meyvesi konan küçük örgü sepet
  الدوخلة سفيفة من خوص صغيرة يجعل فيها الرطب (ayn)؛ الدوخلة هذا المنسوج من الخوص يجعل فيه الرطب (sihah)؛ الدوخلة معروفة (mufradat)

## ظ ل م (root_000967): 42:8 وَٱلظَّٰلِمُونَ, 42:21 ٱلظَّٰلِمِينَ, 42:22 ٱلظَّٰلِمِينَ, 42:40 ٱلظَّٰلِمِينَ, 42:41 ظُلْمِهِۦ, 42:42 يَظْلِمُونَ, 42:44 ٱلظَّٰلِمِينَ, 42:45 ٱلظَّٰلِمِينَ

- **B001** isik yoklugu ve karanlik benzetmesi — karanlik; isigin yoklugu · karanliklar; bilgisizlik, ortak kosma veya yoldan cikma icin benzetme · karanlik; gecenin baslangici · karanliga girmek veya bir yerin kararmasi · gecenin kararmasi · karanlik; karanlik gece · gormeyi ilk kapatan anda onunla karsilasmak · en yakin anda veya ilk gorus noktasinda onunla karsilasmak · takvim ayindaki belirli uc karanlik gece
  الظلمة والجمع ظلمات؛ الظلمة خلاف النور (maqayis;sihah)؛ الظلمة ذهاب النور والظلام اسم لذلك (tahdhib)؛ الظلمة عدم النور ويعبر بها عن الجهل والشرك والفسق (mufradat)
- **B002** haksiz yerinden etme ve siniri asma — bir seyi yerli yerine koymama; haksizlik ve siniri asma · birine haksizlik etmek veya onun sinirini asmak · kendine haksizlik etmek veya kendi payini eksiltmek · eksiltmek veya payini kismak · yoldan ya da dogru yonden sapmak · Tanri'ya ortak kosmayi en agir haksizlik sayan kullanim · haksiz davranan veya kisilere ait paylari engelleyen kisi · cok haksizlik eden kisi · bir toplulugun birbirine haksizlik etmesi · gercekten; ya da isin yerli yerinde olmamasi
  الأصل وضع الشيء في غير موضعه (maqayis;sihah;tahdhib)؛ الظلم مجاوزة الحق ويقال فيما يكثر وفيما يقل (mufradat)؛ ما نقصونا شيئا ولكن نقصوا أنفسهم (tahdhib)؛ إن الشرك لظلم عظيم (mufradat;tahdhib)
- **B003** haksizliga karsi yakinma ve geri istem — birini haksizlikla suclamak veya ona haksiz davrandigini bildirmek · haksizlikla alinan seyin geri istenen konusu · haksiz alinmis pay veya mal icin geri istem · haksizligi dile getirip duzeltilmesini istemek · haksizliga katlanmak ve bunu kabul etmek · gucunu asan istek yuklendiginde buna katlanmak
  الظلامة ما تطلبه من مظلمتك عند الظالم (maqayis)؛ الظلامة والظليمة والمظلمة ما تطلبه عند الظالم (sihah)؛ تظلم منه أي اشتكى ظلمه (sihah)؛ ظلمته تظليما إذا نبأته أنه ظالم (tahdhib)؛ ظلم فلان فاظلم معناه أنه احتمل الظلم (tahdhib)
- **B004** yersiz veya zamansiz somut islem — tulumdaki sutu olgunlasmadan icmek veya icirmek · olgunlasmadan icilen veya icirilen sut · onceden kazilmamis ya da kazi yeri olmayan topragin kazilmasi · cukurdan veya mezardan cikarilip geri konan toprak · hastalik yokken deveyi kesmek · vadi suyunun daha once ulasmadigi yere varmasi · havuzu uygun olmayan yerde yapmak · erkek esegin gebe disi esege ciftlesmek uzere yanasmasi
  ظلم وطبه إذا سقى منه قبل أن يروب (maqayis;sihah;tahdhib)؛ ظلمت السقاء وظلمت اللبن إذا شربته أو سقيته قبل إدراكه (tahdhib;mufradat)؛ الأرض المظلومة التي لم تحفر قط ثم حفرت (maqayis;sihah)؛ ظلمت الأرض حفرتها ولم تكن موضعا للحفر (mufradat)؛ ظلم الوادي إذا بلغ الماء منه موضعا لم يكن بلغه (sihah;tahdhib)؛ ظلمت البعير إذا نحرته من غير داء (sihah)؛ ظلم الحمار الأتان إذا كامها وقد حملت (tahdhib)
- **B005** dislerde su gibi parilti — dislerin su gibi parlakligi · agzin ince su gibi parildamasi
  الظلم ماء الأسنان وبريقها (sihah)؛ الظلم الماء الذي يجري على الأسنان من اللون لا من الريق (tahdhib)؛ أظلم الثغر إذا تلألأ عليه كالماء الرقيق (tahdhib)؛ الظلم ماء الأسنان (mufradat)
- **B006** erkek devekusu — erkek devekusu
  الظليم الذكر من النعام (sihah)؛ الظليم الذكر من النعام وجمعه الظلمان (tahdhib)؛ الظليم ذكر النعام (mufradat)
- **B007** siniri asan uzun surgunlu bitki — sinirini asan uzun surgunleri olan bitki · o uzun surgunlu bitkinin adi
  ومن غريب الشجر الظلم واحدها ظلمة وهو الظلام والظلام والظالم؛ هو شجر له عساليج طوال وتنبسط حتى تجوز حد أصل شجرها
- **B008** paydan alikoyma — kisileri kendilerine ait paylardan alikoyanlar · seni bundan ne alikoydu
  الظلمة المانعون أهل الحقوق حقوقهم؛ ما ظلمك عن كذا أي ما منعك

## ن ص ر (root_001510): 42:8 نَصِيرٍ, 42:31 نَصِيرٍ, 42:39 يَنتَصِرُونَ, 42:41 ٱنتَصَرَ, 42:46 يَنصُرُونَهُم

- **B001** yardım edip üstün gelmesini sağlama — yardım etti ve düşmana karşı üstün gelmesini sağladı · yardım, destek · iyi ve etkili yardım · yardımcı, destekçi · yardımcı, destekçi · yardımcılar, destekçiler · düşmanına karşı kendisine yardım etmesini istedi · birbirlerine yardım ettiler, dayanıştılar
  النصر والنصرة العون (mufradat)؛ عون المظلوم (ayn;tahdhib)؛ نصره الله على عدوه ينصره نصرا (sihah)؛ آتاهم الظفر على عدوهم (maqayis)؛ النصير الناصر (ayn;sihah;tahdhib)؛ التناصر التعاون (mufradat)
- **B002** zulmedene karşı koyup hakkını alma — zulmeden kişiden hakkını aldı, öcünü aldı
  انتصر انتقم وهو منه (maqayis)؛ انتصر الرجل انتقم من ظالمه (ayn)؛ وانتصر منه انتقم (sihah)؛ انتصر الرجل إذا امتنع من ظالمه (tahdhib)؛ الانتصاف والانتقام منه (tahdhib)؛ إذا أصابهم البغي هم ينتصرون (mufradat)
- **B003** bir ülkeye veya toprağa gelmek [kalıp] — belirtilen ülkeye veya toprağa geldim
  نصرت بلد كذا إذا أتيته (maqayis)؛ نصرت أرض بني فلان أي أتيتها (tahdhib)
- **B004** toprağı sulayıp yeşerten, insanları ferahlatan yağmur — yağmur · eksiksiz ve doyurucu yağmur · yağmur ülkeyi suladı veya yeşertti · toprağa yağmur yağdı · halk yağmura kavuşup rahatladı
  يسمى المطر نصرا (maqayis)؛ نصر الغيث البلاد أرواها (ayn)؛ نصر الغيث الأرض أي غاثها (sihah)؛ النصرة المطرة التامة (tahdhib)؛ نصر الغيث البلاد إذا أنبتها (tahdhib)؛ نصر القوم إذا أغيثوا (tahdhib)
- **B005** iyilik veya armağan verme — armağan, veriş
  النصر العطاء (maqayis;sihah)؛ أصل صحيح يدل على إتيان خير وإيتائه (maqayis)
- **B006** Hristiyanlık ve Hristiyan olma ya da yapma — Hristiyan oldu, Hristiyanlığı benimsedi · onu Hristiyan yaptı · Hristiyan erkek, Hristiyan · Hristiyan kadın · Hristiyanlar
  تنصر دخل في النصرانية (ayn;tahdhib)؛ نصره جعله نصرانيا (sihah)؛ رجل نصراني وامرأة نصرانية (sihah)؛ النصارى قيل سموا بذلك لقوله كونوا أنصار الله (mufradat)؛ انتسابا إلى قرية يقال لها نصرانة (mufradat)
- **B007** uzaktan gelip su toplanma yerine ulaşan su yatağı — uzaktan gelip su toplanma yerine ulaşan su yatakları · bu tür su yatağı için olası tekil ad · bu tür su yatağı için diğer olası tekil ad
  النواصر من الشعاب ما جاء من مكان بعيد إلى الوادي؛ النواصر مسايل المياه واحدها ناصرة؛ تجيء من مكان بعيد حتى تقع في مجتمع الماء

## ح ي ي (root_000383): 42:9 يُحْىِ, 42:36 ٱلْحَيَوٰةِ

- **B001** canlı olma, sürüp gitme ve canlandırma — yaşam · canlı; ölmesi düşünülemeyen varlık · canlı oldu ya da canlı kaldı · canlandırdı ya da yeniden yaşama döndürdü · yaşam · bitmeyen gerçek yaşam · ateşi üfleyerek canlandırdı · çocuğu yaşatan besin
  خلاف الموت (maqayis); الحياة ضد الموت والحي ضد الميت (jamhara;sihah); يقال حيي يحيا فهو حي (ayn;tahdhib); الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية والباري حي (mufradat)
- **B002** yağmurla gelen toprak canlılığı ve bolluk — toprağı canlandıran yağmur ve bolluk · toprağı bitkili ve verimli buldum · topluluk yağmura ve bol ota kavuştu · körpe ve canlı bitki
  يسمى المطر حيا لأن به حياة الأرض (maqayis); الحيا مقصور حيا الربيع وهو ما تحيا به الأرض من الغيث (ayn); أحيا القوم أي صاروا في الحيا وهو الخصب وأتيت الأرض فأحييتها أي وجدتها خصبة (sihah); الحي من النبات ما كان طريا يهتز والحيا الغيث (tahdhib); الحيا المطر لأنه يحيي الأرض بعد موتها (mufradat)
- **B003** canlı varlık veya bitmeyen gerçek yaşam — canlı varlık, özellikle duyup hareket eden varlık · bitmeyen gerçek yaşam
  الحيوان كل ذي روح (ayn); الحيوان خلاف الموتان (sihah); الحيوان اسم يقع على كل شيء حي وكل ذي روح حيوان (tahdhib); الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي (mufradat)
- **B004** yılan ve yılanla ilgili adlandırmalar — yılan · erkek yılan · yılan bakıcısı · yılanlı toprak
  الحية معروف يقال حية ذكر وحية أنثى والحيوت ذكر الحيات (jamhara); الحية اشتقاقها من الحياة (ayn); الحية تكون للذكر والأنثى والحيوت ذكر الحيات (sihah); اشتقاق الحية من الحياة ومن قال حواء قال من حويت لأنها تتحوى (tahdhib)
- **B005** kötü olandan utanarak çekinme — utanma ve kötü davranıştan çekinme · ondan utandı ve çekindi · ondan utandı ya da konuşmasına karşılık vermedi
  الاستحياء الذي هو ضد الوقاحة واستحييت منه (maqayis); حييت عن فلان إذا استحييت عنه (jamhara); حييت منه أحيا استحييت واستحياه واستحيا منه من الحياء (sihah); الحياء من الاستحياء ورجل حيي واستحيا الرجل (tahdhib); الحياء انقباض النفس عن القبائح وتركه (mufradat)
- **B006** öldürmeyip sağ bırakma — kadınları sağ bırakıyor ve öldürmüyorlar
  ويستحيون نساءكم أي لا يستبقي (sihah); استحيوا شرخهم بمعنى استفعلوا من الحياة أي استبقوهم ولا تقتلوهم (tahdhib); ويستحيون نساءكم أي يستبقونهن (mufradat)
- **B007** esenlik, uzun ömür ve kalıcılık dileği — Tanrı sana yaşam, kalıcılık ve esenlik versin · karşılama ve esenlik dileği · yoruma göre bütün esenlik, kalıcılık ya da egemenlik Tanrı'nındır
  حياك الله أي ملكك الله والتحيات لله أي الملك لله (sihah); التحية ما يحيي به بعضهم بعضا وتحية الله السلام عليكم ورحمة الله وحياك الله أي أبقاك (tahdhib); التحية أن يقال حياك الله أي جعل لك حياة ثم يجعل دعاء (mufradat)
- **B008** egemenlik bildiren kalıplaşmış söz — egemenlik ve yönetme gücü · bütün egemenlik Tanrı'nındır
  التحية الملك وحياك الله أي ملكك الله (sihah); التحية الملك وأنشد يعني على ملكه والتحيات لله الألفاظ التي تدل على الملك (tahdhib)
- **B009** bir şeye gelmeye çağırma — haydi ibadete gel · haydi et suyuna ekmek yemeğine gel
  قولهم حي على الصلاة معناه هلم وأقبل والعرب تقول حي على الثريد وهو اسم لفعل الأمر (sihah)
- **B010** ortak soylu topluluk veya boylar birliği — soy topluluğu ya da boy · aynı soydan gelen bir topluluk
  الحي حي من العرب وبنو حي بطن من العرب (jamhara); الحي واحد أحياء العرب (sihah); الحي الواحد من أحياء العرب يقع على بني أب كثروا أم قلوا وعلى شعب يجمع القبائل (tahdhib)
- **B011** dişi canlının üreme organı veya döl yatağı — dişi insan ya da hayvanın üreme organı veya döl yatağı
  حياء الناقة وهو فرجها يمكن أن يكون من هذا (maqayis); الحياء أيضا رحم الناقة والجمع أحيية (sihah); الحي فرج المرأة وحياء الشاة والناقة والمرأة ممدود (tahdhib)
- **B012** yüz — yüz
  المحيا الوجه (sihah)
- **B013** yarar, iyilik ve yok olmaktan koruma — yarar, iyilik ve yok olmaktan koruma · çocuğu yaşatan besin
  في القصاص حياة أي منفعة وليس بفلان حياة أي ليس عنده نفع ولا خير (tahdhib); ولكم في القصاص حياة أي يرتدع بالقصاص ومن أحياها أي من نجاها من الهلاك (mufradat)
- **B014** yaşamla ilişkilendirilen erkek kişi adları — yaşamla ilişkilendirilen erkek kişi adları
  حيي اسم رجل (jamhara); حيوة اسم رجل (sihah); حيوة اسم رجل بسكون الياء (tahdhib); اسمه يحيى نبه أنه سماه بذلك من حيث إنه لم تمته الذنوب (mufradat)

## م و ت (root_001454): 42:9 ٱلْمَوْتَىٰ

- **B001** yaşamın ve canlı gücünün sona ermesi — ölüm; yaşamın sona ermesi · öldü; yaşamdan ayrıldı · öldü; yaşamdan ayrıldı · yakında ölecek kimse · ölmüş veya ölecek kimse · kesin ve gerçek ölüm
  أصل صحيح يدل على ذهاب القوة من الشيء (maqayis)؛ الموت خلاف الحياة (maqayis;sihah)؛ الموت معروف مات يموت موتا (jamhara)؛ الموت خلق من خلق الله (tahdhib)؛ أنواع الموت بحسب أنواع الحياة (mufradat)
- **B002** öldürme veya pişirerek keskinliğini giderme — öldürdü; gücünü giderdi · pişirerek keskinliğini giderin · içki pişirilip keskinliği giderildi
  أميتوها طبخا (maqayis)؛ أميتت الخمر طبخت (maqayis)؛ أماته الله وموته شدد للمبالغة (sihah)
- **B003** cansız şey; işlenmemiş veya sahipsiz arazi — işlenmemiş arazi; canlı olmayan şey · cansız şey; sahipsiz ve kullanılmayan arazi
  الموتان الأرض لم تحي بعد بزرع ولا إصلاح وكذلك الموات (maqayis)؛ الموات ما لا روح فيه (sihah)؛ الموات الأرض التي لا مالك لها ولا ينتفع بها أحد (sihah)؛ الموتان أن يبيع المتاع وكل شيء غير ذي روح (tahdhib)
- **B004** insanlar veya hayvan varlığı içinde ölüm görülmesi — insanlarda veya hayvanlarda görülen ölüm · mal veya hayvan varlığı içindeki ölüm
  وقع في الناس موتان (maqayis)؛ الموتان بالضم موت يقع في الماشية (sihah)؛ وقع في المال موتان وموات وهو الموت (tahdhib)
- **B005** çocuğu ölmüş ebeveyn veya ana hayvan — yavrusu ölmüş ana hayvan veya çocuğu ölmüş kadın · oğlu veya oğulları öldü
  ناقة مميت ومميتة للتي يموت ولدها (maqayis)؛ أماتت الناقة إذا مات ولدها فهي مميت ومميتة (sihah)؛ وكذلك المرأة (sihah)؛ أمات فلان إذا مات له ابن أو بنون (sihah)
- **B006** zekâ ve anlayıştan yoksunluk — zekâsı ve anlayışı kıt kimse · ne kadar anlayışsız!
  رجل موتان الفؤاد وامرأة موتانة (maqayis)؛ رجل موتان الفؤاد وامرأة موتانة الفؤاد (sihah)؛ رجل موتان الفؤاد إذا كان غير ذكي ولا فهم (tahdhib)
- **B007** usulüne uygun kesilmeden ölen yenilebilir hayvan — usulüne uygun kesilmeden ölmüş yenilebilir hayvan
  الميتة ما مات مما يؤكل لحمه إذا ذكي (maqayis)؛ الميتة ما لم تلحقه الذكاة (sihah)
- **B008** bir kez ölme veya ölüm biçimi — ölüm biçimi veya hali · bir kez ölme
  الموتة الواحدة من الموت (maqayis)؛ الميتة حال من الموت حسنة أو قبيحة (maqayis)؛ مات فلان ميتة حسنة (sihah)؛ الميتة الحال من أحوال الموت (tahdhib)
- **B009** ardından ayılınan geçici delilik, nöbet veya baygınlık — ardından ayılınan delilik benzeri hal, nöbet veya baygınlık
  الموتة شبه الجنون يعترى الإنسان (maqayis)؛ الموتة جنس من الجنون والصرع يعتري الإنسان (sihah)؛ الموتة الجنون (tahdhib)؛ الموتة الذي يصرع من الجنون أو غيره ثم يفيق (tahdhib)؛ الموتة شبه الغشية (tahdhib)
- **B010** bir işe kendini bütünüyle verme; savaşta ölümü göze alma [kalıp] — işe kendini bütünüyle veren · savaşta ölümü göze alarak dövüşen · ölümü gönüllü karşıladı
  المستميت للأمر المسترسل له (maqayis;sihah)؛ المستميت المستقتل الذي لا يبالي في الحرب من الموت (sihah)؛ استمات الرجل إذا طاب نفسا بالموت (tahdhib)؛ المستميت الذي يقاتل على الموت (tahdhib)
- **B011** ölmüş, deli veya alçakgönüllüymüş gibi davranma — gösteriş için aşırı alçakgönüllü görünen · canlıyken ölmüş gibi davrandı · deli veya alçakgönüllüymüş gibi davranan
  المتماوت من صفة الناسك المرائي (sihah)؛ المستميت الذي يتجان وليس بمجنون (tahdhib)؛ يتخاشع ويتواضع لهذا حتى يطعمه (tahdhib)؛ ضربته فتماوت إذا أرى أنه ميت وهو حي (tahdhib)؛ المتماوتون المراءون (tahdhib)
- **B012** rüzgârın dinmesi, kumaşın eskimesi veya insanın uyuması [kalıp] — rüzgâr dindi · kumaş eskidi ve yıprandı · adam uyudu ve hareketsizleşti
  الموت السكون (tahdhib)؛ ماتت الريح إذا سكنت (tahdhib)؛ مات الثوب ونام إذا بلي (tahdhib)؛ مات الرجل وهمد وهوم إذا نام (tahdhib)
- **B013** gerçeğe boyun eğme [kalıp] — adam gerçeğe boyun eğdi
  مات الرجل إذا خضع للحق (tahdhib)
- **B014** vurulmuş avın ölüp ölmediğini inceleme [kalıp] — avınızın ölüp ölmediğine bakın
  استميتوا صيدكم أي انظروا مات أم لا (tahdhib)؛ إذا أصيب فشك في موته (tahdhib)

## ك ل ل (root_001315): 42:9 كُلِّ, 42:12 بِكُلِّ, 42:33 لِّكُلِّ

- **B001** körelip güçten düşme — körelmek, yorulup güçten düşmek · körleşmiş, yorgun veya etkisiz · bineğini yorup güçten düşürmek
  خلاف الحدة وكل السيف واللسان والطرف (maqayis)؛ الكليل السيف الذي لا حد له ولسان كليل والكال المعيي (ayn)؛ كللت من المشي وكل السيف والريح والطرف واللسان (sihah)؛ الكليل السيف ولسان كليل والكال المعيي وثقل سمعه وكل بصره (tahdhib)؛ كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام (mufradat)
- **B002** bakımı başkasına yük olan — bakımı ve geçimi sahibine yük olan · yetim veya yakın aile desteği bulunmayan kişi · sahibinin taşıdığı, ona yük olan tapınma nesnesi · bakmakla yükümlü olduğum kişiler · yakınlarının geçim yükünü üstlenir duruma gelmek
  الكُلّ العيال واليتيم (maqayis)؛ الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل (ayn)؛ الكل العيال والثقل والكل اليتيم والكل الذي لا ولد له ولا والد (sihah)؛ الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه (tahdhib)
- **B003** bütün, tüm — bütün, tüm, tamamı
  كل اسم موضوع للإحاطة مضاف أبدا (maqayis)؛ كل لفظه واحد ومعناه جمع (sihah)؛ يقع كل على اسم منكور موحد فيؤدي معنى الجماعة وكلهم للإحاطة (tahdhib)؛ لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام (mufradat)
- **B004** üstsoy ve altsoy dışı mirasçılık — ana baba ve çocuk dışındaki yan kol mirasçılığı · yan koldan değil, doğrudan hakla miras almak · uzak kuzen · soy bakımından daha uzak olmak
  الكلالة هم الرجال الورثة وبنو العم الأباعد ومن مات وليس له ولد ولا والد (maqayis)؛ الكل النسب البعيد (ayn)؛ لم يرثه كلالة أي لم يرثه عن عرض والكلالة بنو العم الأباعد (sihah)؛ الكلالة من القرابة ما خلا الوالد والولد (tahdhib)؛ الكلالة اسم لما عدا الولد والوالد من الورثة (mufradat)
- **B005** çevresini kuşak gibi saran oluşum — taç veya süslü baş kuşağı · Ay'ın konaklarından biri, Akrep takımyıldızının başı · bir yerin çevresini dolaşan örtümsü bulut · çiçeklerle çevrili çayır · çevresi küçük bulut parçalarıyla sarılı bulut · başına taç takmak
  إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان (maqayis)؛ الإكليل شبه عصابة مزينة بالجواهر والإكليل من منازل القمر وروضة مكللة حفت بالنور (ayn)؛ الإكليل شبه عصابة ويسمى التاج إكليلا والإكليل منزل والسحاب كأن غشاء ألبسه وروضة مكللة وسحاب مكلل (sihah)؛ الغمام المكلل السحابة تكون حولها قطع والإكليل شبه عصابة والإكليل منزل (tahdhib)؛ الإكليل سمي بذلك لإطافته بالرأس (mufradat)
- **B006** ev biçimli ince koruyucu örtü — böceklerden koruyan ev biçimli ince örtü, cibinlik · mezar üzerine küçük kule veya kubbe biçimli yapı yükseltmek
  الكلة غشاء من ثوب يتوقى به من البعوض (ayn)؛ الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق (sihah)؛ الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب (tahdhib)
- **B007** göğüs — göğüs · göğüs
  الكلكل الصدر (maqayis)؛ الكلكل الصدر (ayn)؛ الكلكل والكلكال الصدر (sihah)؛ الكلكل فهو الصدر (tahdhib)؛ الكلكل الصدر (mufradat)
- **B008** kısa, kalın ve güçlü yapılı erkek [kalıp] — kısa, kalın, güçlü ve toplu yapılı erkek
  الكلكل القصير (maqayis)؛ الكلكل الرجل الضرب ليس بجد طويل والمربوع المجتمع الخلق (ayn)؛ رجل كلكل قصير غليظ مع شدة (sihah)؛ رجل كلكل وكلاكل وكوألل قصر وغلظ مع شدة (tahdhib)
- **B009** topluluklar, kümeler — topluluklar, kümeler
  الكلاكل من الجماعات كالكراكر من الخيل (ayn)؛ الكلاكل هي الجماعات كالكراكر (tahdhib)
- **B010** saldırıda ilerleme veya korkup geri durma; itaatsizlik — saldırıda durmadan ileri gitmek · savaşta korkup geri durmak · ona itaat etmemek, karşı gelmek
  كلل حمل ولعله أن يكون من المتضادات (maqayis)؛ المكلل الجاد حمل فكلل مضى قدما وقد يكون كلل بمعنى جبن (sihah)؛ المكلل الذي يحمل فلا يرجع حتى يقع بقرنه وكلل فلان فلانا لم يطعه (tahdhib)
- **B011** dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması — dişleri görünerek gülümsemek · bulutun içinden beyaz şimşek çakmak
  انكلت المرأة إذا ضحكت (maqayis)؛ انكل الرجل انكلالا تبسم وتنكل عن غر عذاب وانكلال الغيم بالبرق (sihah)؛ انكلت المرأة إذا تبسمت وانكل السحاب بالبرق إذا تبسم بالبرق (tahdhib)

## ق د ر (root_001205): 42:9 قَدِيرٌ, 42:12 وَيَقْدِرُ, 42:27 بِقَدَرٍ, 42:29 قَدِيرٌ, 42:50 قَدِيرٌ

- **B001** bir şeyin ölçüsü ve eriştiği sınır — bir şeyin ölçüsü, niceliği ve sınırı · belirlenmiş ölçü, sınır veya süre
  مبلغ الشيء وكنهه ونهايته (maqayis)؛ القدر مبلغ الشيء؛ لكل شيء مقدار وأجل (ayn)؛ قدر الشيء مبلغه (sihah)؛ المقدار هو الهنداز؛ ينزل المطر بمقدار (tahdhib)؛ القدر والتقدير تبيين كمية الشيء (mufradat)
- **B002** Tanrı'nın varlıkları ölçülü biçimde hükme bağlaması — Tanrı'nın varlıklar için belirlediği ölçülü hüküm · Tanrısal belirlemeyi reddetmekle anılan topluluk · belirli işlere ayrılmış özel gece
  قضاء الله تعالى الأشياء على مبالغها ونهاياتها (maqayis)؛ القدر القضاء الموفق؛ قدره الله تقديرا (ayn;tahdhib)؛ ما يقدره الله عزوجل من القضاء (sihah)؛ يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة (mufradat)
- **B003** bir şeyi yapmaya veya ona egemen olmaya elveren güç — bir işi yapmaya elveren güç ve yetkinlik · gücü yeten ve yapabilen · dilediğini gerçekleştirecek ölçüde güçlü · gücü olan veya güç edinmiş · varlıklı ve geniş olanaklı
  قدرة الله تعالى على خليقته؛ رجل ذو قدرة وذو مقدرة أي يسار (maqayis)؛ قدر على الشيء قدرة أي ملك فهو قادر (ayn;tahdhib)؛ الاقتدار على الشيء القدرة عليه؛ رجل ذو قدرة أي ذو يسار (sihah)؛ القدرة إذا وصف بها الإنسان فاسم لهيئة له بها يتمكن (mufradat)
- **B004** birinin geçim payını kısmak [kalıp] — onun geçim payını kıstı · onu darlığa sokarız
  من قدر عليه رزقه فمعناه قتر (maqayis)؛ قدر على عياله مثل قتر؛ قدر على الإنسان رزقه مثل قتر (sihah)؛ نضيق عليه؛ ضيق عليه (tahdhib)؛ قدرت عليه الشيء ضيقته؛ ومن قدر عليه رزقه أي ضيق عليه (mufradat)
- **B005** ölçüp biçerek tasarlamak ve hazırlamak — ölçüsünü belirleyip hazırladı · ayın gün sayısını hesaplayıp otuza tamamlayın · örgülü işi düzgün ve sağlam kurdu · o şey onun için hazır duruma geldi
  اقتدرت الشيء جعلته قدرا؛ قدرت الشيء أي هيأته (ayn)؛ فاقدروا له أي أتموا ثلاثين؛ تقدر له الشيء أي تهيأ (sihah)؛ التروية والتفكير في تسوية أمر وتهيئته؛ نظرت فيه ودبرته وقايسته؛ قدر في السرد أي أحكمه (tahdhib)؛ التقدير من الإنسان التفكر في الأمر؛ فكر وقدر؛ قدر في السرد أي أحكمه (mufradat)
- **B006** söz öbeğine göre ölçüye uygun, orta veya yapıca ölçülü olma [kalıp] — ölçüsüne uydu ve tam denk geldi · orta büyüklükte eyer · orta boylu adam · kısa boyunlu veya kısa adam · arka ayaklarını ön ayak izlerine basan at · yol alması kolay gece
  جاء على قدره؛ المقتدر الوسط؛ سرج قدر أي وسط (ayn)؛ بين أرضك وأرض فلان ليلة قادرة؛ الأقدر القصير؛ الأقدار من الخيل (sihah)؛ كل شيء مقتدر فهو الوسط؛ القدر من الرحال والسروج الوسط؛ الأقدر من الرجال القصير العنق؛ الأقدر من الخيل (maqayis;tahdhib)؛ الأقدر القصير العنق؛ فرس أقدر (mufradat)
- **B007** pişirme kabı ve ona bağlı yemek, pişirme işi ve görevli sözleri — et veya yemek pişirme tenceresi · tencerede pişmiş et veya yemek · pişmiş çorba suyu · topluluk tencerede yemek pişirdi · hayvanı kesip etini pişiren kasap veya aşçı
  القدر وهي معروفة؛ القدير اللحم يطبخ في القدر؛ القدار الجزار ويقال الطباخ (maqayis)؛ القدير ما طبخ من اللحم؛ مرق مقدور؛ القدار الطباخ (ayn)؛ القدير المطبوخ في القدر؛ القدار الجزار ويقال الطباخ (sihah)؛ القدر مؤنثة؛ قدرت القدر إذا طبخت قدرا؛ القدار الجزار (tahdhib)؛ القدر اسم لما يطبخ فيه اللحم؛ قدرت اللحم طبخته؛ القدار الذي ينحر ويقدر (mufradat)

## خ ل ف (root_000433): 42:10 ٱخْتَلَفْتُمْ

- **B001** ardından gelip yerini tutma — ardından gelip yerini veya görevini üstlenen kimse ya da durum · birinin ardından onun ailesi veya topluluğu içindeki işini üstlenmek · Tanrı'nın kaybedilen kimsenin yerini tutmasını veya gidene karşılık vermesini dilemek
  أن يجيء شيء بعد شيء يقوم مقامه؛ الخلافة لأن الثاني يجيء بعد الأول قائما مقامه (maqayis)؛ الخلف الخليفة؛ الخليفة من استخلف مكان من قبله (ayn)؛ خلف فلان فلانا في أهله؛ خلف فلان فلانا فهو خليفة له (jamhara)؛ الخلف ما جاء من بعد؛ خليفة؛ خلف فلان فلانا إذا كان خليفته (sihah)؛ خلف فلان فلانا قام بالأمر عنه؛ الخلافة النيابة عن الغير (mufradat)
- **B002** arkasında ya da sonrasında olma — bir şeyin arkasında veya sonrasında, ön tarafında değil · birinin arkasında oturmak veya gerisinde kalmak
  خلف وهو غير قدام؛ هذا خلفي وهذا قدامي (maqayis)؛ الخلاف بمنزلة بعد؛ خلافك أي بعدك (ayn)؛ جاء فلان خلف فلان وخلاف فلان إذا جاء بعده (jamhara)؛ خلف نقيض قدام؛ جلست خلف فلان أي بعده (sihah)؛ خلف ضد القدام؛ لا يلبثون خلفك بعدك (mufradat)
- **B003** geride kalma ve geride kalanlar — erkekler ayrıldığında evlerde kalan kadınlar veya topluluk · eksiklik veya yetersizlik yüzünden geri kalan kimse
  الخوالف هن النساء؛ الحي خلوف إذا كان الرجال غيبا والنساء مقيمات (maqayis)؛ الخوالف يعني النساء؛ حي خلوف أي غيب (ayn)؛ حي خلوف إذا غزا الرجال وبقي النساء (jamhara)؛ الخوالف أي مع النساء؛ حي خلوف أي غيب؛ الحضور المتخلفون (sihah)؛ الخالف المتأخر لنقصان؛ الخالفة المرأة؛ الحي خلوفا (mufradat)
- **B004** ayrı yol tutup karşı çıkma — başka bir yol tutmak, karşı çıkmak veya uyuşmamak · görüş veya durum bakımından ayrışma; çekişmeye dönüşebilen uyuşmazlık · karşılıklı olarak farklı iki yandan
  اختلف الناس في كذا؛ كل واحد منهم ينحي قول صاحبه (maqayis)؛ خلاف رسول الله مخالفته؛ رجل خالف؛ اختلفت (ayn)؛ خالفني الرجل مخالفة وخلافا؛ في فلان خلفة أي مخالف لما أمرته (jamhara)؛ الخلاف المخالفة؛ خلاف رسول الله أي مخالفة رسول الله (sihah)؛ الاختلاف والمخالفة أن يأخذ كل واحد طريقا غير طريق الآخر؛ استعير ذلك للمنازعة والمجادلة (mufradat)
- **B005** verdiği sözü tutmama — verilen sözün veya belirlenen zamanın yerine getirilmemesi · verdiği sözü yerine getirmemek · sözünü çok sık tutmayan kimse
  الخلاف في الوعد؛ وعدني فأخلفته (maqayis)؛ الخلف مصدر قولك أخلفت وعدي (ayn)؛ وعدني فأخلفني إخلافا؛ الخلف الاسم والإخلاف المصدر (jamhara)؛ الإخلاف وهو في المستقبل كالكذب في الماضي؛ أخلفه ما وعده (sihah)؛ الخلف المخالفة في الوعد؛ وعدني فأخلفني (mufradat)
- **B006** sırayla birbirinin ardından gelme — sırayla veya grup grup birbirinin ardından gelme · gece ile gündüzün birbirini izlemesi
  إذا مرت هذه خلفتها هذه؛ يستقيان هذا بعد ذا وذاك بعد هذا (maqayis)؛ الخلفة مصدر الاختلاف؛ جعل الليل والنهار خلفة (ayn)؛ يمشين خلفة؛ فوجا بعد فوج؛ كل شيء كان بدلا من شيء خلفة (jamhara)؛ يمشين خلفة؛ تذهب هذه وتجئ هذه؛ اختلاف الليل والنهار (sihah)؛ الخلفة في أن يخلف كل واحد الآخر؛ إن في اختلاف الليل والنهار أي مجيء كل واحد منهما خلف الآخر (mufradat)
- **B007** bozulup eski durumundan çıkma — ağız kokusunun değişmesi · süt veya yiyeceğin tadı ya da kokusu değişip bozulmak · bozulmak veya önceki düzgün halinden değişmek · ortası yıpranmış bölümü çıkarılıp onarılmış giysi · hastalıktan bir yanına eğik yürüyen deve
  الثالث التغير؛ خلف فوه إذا تغير؛ الخليف الثوب يبلى وسطه؛ البعير الأخلف (maqayis)؛ خلوف فم الصائم نكهته؛ خلف ريح فمه أي تغير (ayn)؛ خلف فوه خلوفة وخلوفا؛ خلف اللبن خلوفا إذا حمض؛ خلفت نفسه عن الشيء (jamhara)؛ خلف فم الصائم خلوفا؛ خلف اللبن والطعام إذا تغير؛ خلفت الثوب (sihah)؛ خلف خلافة فسد؛ لمن فسد كلامه أو كان فاسدا في نفسه (mufradat)
- **B008** kötü ve değersiz olma — kötü söz veya öncekilerin ardından gelen kötü topluluk · iyilik taşımayan, çok ters davranan veya budala kimse
  خلف سوء؛ الجيد خلف وللردي خلف (maqayis)؛ خلف سوء؛ رجل خالفة أي يخالف ذو خلاف (ayn)؛ الخلف الرديء من الكلام؛ فلان خالفة من الخوالف إذا كان لا خير عنده؛ الخلافة الحمق (jamhara)؛ الخلف الردى من القول؛ فلان خالفة أهل بيته إذا كان لا خير فيه (sihah)؛ الخلف الرديء؛ لمن فسد كلامه أو كان فاسدا في نفسه؛ الخالف المتأخر لنقصان (mufradat)
- **B009** arka parça ve araç ağzı adları — baltanın kesici ağzı veya iki başından biri · arka veya içe yakın kaburga ya da devenin meme ucu · evin veya çadırın arka direği · evlerin arkasında hayvanların çevrildiği açık alan
  الخلف الواحد من أخلاف الضرع؛ الخالفة من عمد البيت في مؤخر البيت (maqayis)؛ الخلف حد الفأس؛ الخلف أصغر ضلع يلي البطن؛ الأطباء المؤخر؛ الخلف الضرع نفسه؛ الخالفتان عمودا البيت (ayn)؛ فأس ذات خلفين؛ الخلف المربد وراء بيوت القوم؛ الخالفة العمود المؤخر؛ الخلف الواحد من أخلاف الناقة؛ ضلع الخلف (jamhara)؛ الخلف أقصر أضلاع الجنب؛ فأس ذات خلفين؛ خلف جيد وهو المربد؛ الخالفة عمود من أعمدة الخباء (sihah)؛ الخلف حد الفأس؛ ما تخلف من الأضلاع إلى ما يلي البطن؛ الخالفة عمود الخيمة المتأخر (mufradat)
- **B010** kaybın ardından yenisinin çıkması veya verilmesi — Tanrı'nın kaybedilen kimsenin yerini tutmasını veya gidene karşılık vermesini dilemek · önceki bitki veya meyveden sonra çıkan yeni ürün · bitkinin yeni ürün vermesi veya ağacın yeniden yeşermesi · kuşun eski tüyünü döküp yenisini çıkarması
  الخلفة نبت ينبت بعد الهشيم؛ خلفة الشجر ثمر يخرج بعد الثمر (maqayis)؛ الخلفة ما أنبت الصيف من العشب؛ زرع الحبوب خلفة (ayn)؛ الخلفة نبت ينبت بعد نبت؛ خلفة الشجر ثمر يطلع بعد الثمر (jamhara)؛ الخلفة نبت ينبت بعد النبات؛ أخلف النبات أي أخرج الخلفة (sihah)؛ أخلف الشجر إذا اخضر بعد سقوط ورقه؛ أخلف الله عليك أعطاك خلفا (mufradat)
- **B011** sırayla su çekip topluluğa sağlama — sırayla veya topluluk ve hayvanlar için su çekme · topluluk ya da sürü için su çeken kişi
  الخلف وهو الاستقاء؛ المستقيين يتخالفان؛ أخلف إذا استقى (maqayis)؛ الخلفة والإخلاف الاستقاء؛ بعتنا فلانا يخلف لنا أي يستقي (ayn)؛ أخلفت القوم إذا استقيت لهم؛ المخلف المستقي (jamhara)؛ الخلف الاستقاء؛ من أين خلفتكم أي من أين تستقون؛ الخالف المستقى (sihah)؛ الإخلاف أن يسقي واحد بعد آخر (mufradat)
- **B012** engebeli arazide geçit veya yöresel yönetim bölgesi — dağlar arasında veya engebeli arazide genişliğe açılan geçit · Yemen'e özgü yönetim bölgesi veya ilçe
  الخليف الطريق بين الجبلين (maqayis)؛ المخلاف الكورة بلغة أهل اليمن؛ الخليف فرج بين قنتين؛ مدافع الأودية ومن الطريق أفضلها (ayn)؛ الخليف الطريق في رمل أو في غلظ؛ المخاليف رساتيقها (jamhara)؛ المخلاف لأهل اليمن واحد المخاليف؛ الخليف الطريق بين الجبلين (sihah)
- **B013** özel bitki, hayvan, yaş ve ilişki kullanımları — belirli bir ağaç türünün adı · gebe dişi deve veya gebe dişi develer topluluğu · yetişkin diş evresini bir veya daha çok yıl geçmiş erkek deve · bir kadınla önceki eşinden sonra evlenmek · bir erkeğin yokluğunda onun kadınına gitmek · ergenliğe yaklaşan oğlan
  الناقة الحامل خلفة؛ يجوز أن يكون شاذا (maqayis)؛ الخلاف شجر؛ الخلفة من النوق الحامل؛ إذا تمت للإبل بعد البزول سنة قيل مخلف عام (ayn)؛ خلف فلان على فلانة إذا تزوجها؛ الخلاف شجر معروف؛ الجمل بعد بزوله مخلف (jamhara)؛ الخلف المخاض وهي الحوامل من النوق؛ المخلف من الإبل الذي جاوز البازل؛ شجر الخلاف معروف؛ يخالف إلى امرأة فلان (sihah)؛ الخلاف شجر؛ للجمل بعد بزوله مخلف عام (mufradat)

## ن و ب (root_001562): 42:10 أُنِيبُ, 42:13 يُنِيبُ

- **B001** yinelenen dönüş ve dönüşümlü sıra — tekrar tekrar dönmek · bir topluluğa tekrar tekrar gitmek · sıra; nöbet · bir işi veya payı sırayla üstlenmek
  اعتياد مكان ورجوع إليه (maqayis)؛ انتاب أتاهم مرة بعد أخرى (sihah)؛ النوب رجوع الشيء مرة بعد أخرى (mufradat)؛ جاءت نوبتك ونيابتك وهم يتناوبون النوبة (sihah)
- **B002** başkasının yerine geçip işini yürütme — başkasının yerine geçmek · başkalarının yerine iş görenler
  ناب عني فلان ينوب منابا أي قام مقامي (sihah)؛ النوب جمع نائب (maqayis;jamhara)
- **B003** yanlışından dönüp Tanrı'ya içtenlikle yönelme [kalıp] — yanlışından dönüp Tanrı'ya yönelmek · yanlışından dönerek Tanrı'ya içtenlikle yönelme
  أناب إلى الله أي أقبل وتاب (sihah)؛ الإنابة إلى الله الرجوع إليه بالتوبة وإخلاص العمل (mufradat)
- **B004** başa gelen olay veya sıkıntı — başına bir olay gelmek · başına bir olay gelmek · başına gelen olay · felaket; başa gelen ağır olay · zamanın getirdiği felaketler · her gün yinelenen ateşli hastalık
  النوبة بالضم الاسم من قولك نابه أمر وانتابه أي أصابه (sihah)؛ النائبة المصيبة واحدة نوائب الدهر (sihah)؛ الحمى النائبة التي تأتي كل يوم (sihah)؛ نابته نائبة أي حادثة من شأنها أن تنوب دائبا (mufradat)
- **B005** arılar, özellikle siyah arılar — arılar, özellikle siyah arılar
  النوب النحل (maqayis;ayn)؛ النوب السود من النحل (ayn)؛ سميت به لرعيها ونوبها إلى مكانها (maqayis)؛ لأنها ترعى وتنوب إلى مكانها (sihah)؛ سمي النحل نوبا لرجوعها إلى مقارها (mufradat)
- **B006** Siyah Afrikalı bir halk ve bu halktan kişi — Siyah Afrikalı bir halk · bu halktan bir kişi
  النوبة ضرب من السودان (ayn)؛ النوب والنوبة أيضا جيل من السودان الواحد نوبي (sihah)
- **B007** yakınlık; su yolunda bir gün bir gecelik uzaklık — yakınlık; su yolunda bir gün bir gecelik uzaklık
  النوب القرب خلاف البعد (ayn;sihah)؛ النوب ما كان منك مسيرة يوم وليلة والقرب ما كان منك مسيرة ليلة وأصله في الورد (sihah)

## ECHO ن ي ب (root_001571): for 42:10 أُنِيبُ, 42:13 يُنِيبُ: withheld observed target; not identity

- **B001** tekrar tekrar dönme veya gitme — tekrar tekrar dönmek · birine tekrar tekrar gitmek · yanlışından vazgeçip Tanrı'ya içtenlikle yönelmek · bir işi sırayla üstlenmek · yuvalarına dönen arılar
  كلمة واحدة تدل على اعتياد مكان ورجوع إليه (maqayis)؛ وأناب فلان إلى الله إنابة فهو منيب إذا ناب ورجع إلى الطاعة (ayn)؛ وتناوبنا الخطب والأمر نتناوبه إذا قمتما به نوبة بعد نوبة (ayn)؛ انتاب الرجل القوم إذا أتاهم مرة بعد مرة (ayn)؛ النوب رجوع الشيء مرة بعد أخرى (mufradat)؛ الإنابة إلى الله تعالى الرجوع إليه بالتوبة وإخلاص العمل (mufradat)؛ فلان ينتاب فلانا أي يقصده مرة بعد أخرى (mufradat)؛ سمي النحل نوبا لرجوعها إلى مقارها (mufradat)
- **B002** köpek dişi — köpek dişi · köpek dişleri · köpek dişleri · köpek dişiyle vurmak · ok sapını dişleyip iz bırakmak
  الناب السن الذي خلف الرباعية وهو الناب مذكر وأنياب جمعه (ayn)؛ الناب من السن والجمع أنياب ونيوب أيضا (sihah)؛ نابه ينيبه أي أصاب نابه ونيب سهمه أي عجم عوده وأثر فيه بنابه (sihah)
- **B003** uzun köpek dişli yaşlı dişi deve — uzun köpek dişli yaşlı dişi deve · yaşlı dişi develer · yaşlı dişi develer · dişi devenin yaşlanması
  الناب الناقة المسنة والجميع نيب وأنياب (ayn)؛ الناب المسنة من النوق والجمع النيب (sihah)؛ سميت بذلك لطول نابها (sihah)؛ نيبت الناقة أي صارت هرمة ولا يقال للجمل ناب (sihah)
- **B004** yeniden başa gelebilen olumsuz olay — başa gelen olumsuz olay · başına olumsuz bir olay gelmek
  النائبة النازلة يقال ناب هذا الأمر نوبة أي نزل ونابتهم نوائب الدهر (ayn)؛ نابته نائبة أي حادثة من شأنها أن تنوب دائبا (mufradat)
- **B005** başkasının yerine görev yapmak [kalıp] — bir işte başkasının yerine geçmek
  ناب عني فلان في هذا الأمر نيابة إذا قام مقامك
- **B006** topluluğun önderi [kalıp] — topluluğun önderi
  ناب القوم سيدهم

## ECHO ن ب ء (root_001464): for 42:10 أُنِيبُ, 42:13 يُنِيبُ: withheld observed target; not identity

- **B001** bir yerden başka bir yere geçip belirme — bir yerden başka bir yere çıktı veya gelip belirdi · başka bir yerden gelen ya da çıkan · toprak onu getirip ortaya çıkardı
  الإتيان من مكان إلى مكان (maqayis)؛ ينبأ من أرض إلى أرض وسيل نابئ ورجل نابئ (maqayis;ayn;sihah;tahdhib)؛ نبأت على القوم إذا طلعت عليهم (sihah;tahdhib)؛ نبأت به الأرض جاءت به (sihah)
- **B002** bilgi taşıyan haber — haber · bilgi sağlayan önemli haber · haberler · ona güçlü biçimde haber verdim · ona haber verdim · ona bu konuda haber verdim · ona bunu bildirdim · ondan haber istedim
  النبأ الخبر (maqayis;ayn;sihah;tahdhib)؛ نبأته وأنبأته واستنبأته والجميع الأنباء (ayn;sihah;tahdhib)؛ خبر ذو فائدة عظيمة يحصل به علم أو غلبة ظن (mufradat)؛ نبأته أبلغ من أنبأته (mufradat)
- **B003** Tanrı'dan haber veren elçi — Tanrı'dan haber veren elçi · Tanrı ile insanlar arasındaki kutsal elçilik görevi
  من همز النبي فلأنه أنبأ عن الله تعالى (maqayis)؛ النبي ينبئ الأنباء عن الله عز وجل (ayn)؛ النبئ لانه أنبأ عن الله تعالى (sihah)؛ النبوة سفارة بين الله وبين ذوي العقول من عباده (mufradat)؛ النبي لكونه منبئا بما تسكن إليه العقول الذكية (mufradat)
- **B004** Tanrı elçiliğini yalan yere ileri sürme — Tanrı elçisi olduğunu yalan yere ileri sürdü · haberleri Tanrı'dan gelmeyen yalancı elçi
  تنبأ مسيلمة بالهمز (sihah)؛ العرب كانت نبيئة مسيلمة نبيئة سوء (sihah)؛ تنبأ فلان ادعى النبوة (mufradat)؛ لم يستعمل إلا في المتقول في دعواه (mufradat)
- **B005** okun hedefi çizmeden başka yere düşmesi [kalıp] — attı; oku hedefi çizmeden sapıp başka yere düştü
  رمى الرامي فأنبأ إذا لم يشرم كأن سهمه عدل عن الخدش وسقط مكانا آخر (maqayis)؛ رمى فأنبأ إذا لم يشرم ولم يخدش (sihah)
- **B006** hafif ve belirsiz ses — hafif, gizli ve belirsiz ses
  النبأة الصوت (maqayis)؛ النبأة النغية وهو صوت يشك فيه ولا يتيقن (ayn)؛ النبأة الصوت الخفى (sihah)؛ النبأة الصوت ليس الشديد (tahdhib)؛ النبأة الصوت الخفي (mufradat)
- **B007** istenen yere götüren açık yol — istenen yere götüren açık yol; kolay geçilen düz yer
  النبي يقال الطريق الواضح يأخذك إلى حيث تريد (ayn)؛ مكان النبي من الكاثب هو ما سهل من الأرض (ayn)

## ن ف س (root_001533): 42:11 أَنفُسِكُمْ, 42:45 أَنفُسَهُمْ

- **B001** soluk alıp verme — soluk alıp verme · gövdeye girip çıkan hava; soluk · tek soluk ya da soluklanma arası · soluklar
  التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)
- **B002** sıkıntıyı hafifletip ferahlatma — Tanrı onun sıkıntısını giderdi · beni sıkıntıdan kurtarıp rahatlat · Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı
  نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)
- **B003** kem gözle zarar verme — zarar verdiğine inanılan bakış · ona kem göz değdi · kem gözle zarar veren kişi
  يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)
- **B004** canlıdaki akışkan kan — kaybıyla yaşamın da yitirildiği kan · hayvandaki akışkan kan
  النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)
- **B005** doğum ve doğuma bağlı kadın-çocuk durumu — doğum yapmış ya da doğum sonrası kanaması olan kadın · doğum ve doğum sonrası kanama dönemi · yeni doğan çocuk · doğmadan önce
  الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)
- **B006** soluk aralı içim ve bir içimlik yudum — bir solukta alınan yudum ya da içim · üç soluk arasıyla içme
  كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)
- **B007** bir deri işlemeye yetecek sepi maddesi payı — deriyi bir kez işlemeye yetecek sepi maddesi · bir işlemelik sepi maddesi payı
  في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)
- **B008** yaşamı sürdüren, bol ve doyurucu su — yaşamı ayakta tutan su · bol ve susuzluğu gideren içecek · tadı kötü, bayat ve içimi güç içecek
  يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)
- **B009** kalıba bağlı yarılıp açılma ve genişleme [kalıp] — yay çatladı ya da yarıldı · sabah söktü, aydınlık yayıldı · gündüz uzayıp genişledi · ırmağın suyu artıp yayıldı
  تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)
- **B010** değerli ve uğrunda yarışılan şey — değerli, önemli ve arzulanan · bir şeyi elde etme ya da üstünlere benzeme yarışı · başkasına vermeye kıyamayıp esirgemek · sahip olduğu şey yüzünden onu kıskanmak
  شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)
- **B011** bedene yaşam veren can — bedene yaşam veren can · insan ya da canlı birey
  النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)
- **B012** şeyin kendisi ve bütün öz varlığı [kalıp] — şeyin tam kendisi ve gerçeği · başkası aracılığıyla değil, bizzat kendisi
  كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)
- **B013** iç düşünce, niyet ve ayırt etme gücü — onun içinden geçen düşünce ya da niyet · ayırt etmeyi sağlayan zihinsel güç
  نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)
- **B014** sağlam, cömert ve onurlu yaradılış — sağlam karakterli, dayanıklı ve cömert adam · büyüklük duygusu, onur, yüksek amaç ve kendine saygı
  رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)
- **B015** uzaklık, genişlik ve zaman payı — işinde rahat hareket edecek genişlikte · ek süre ya da hareket alanı · daha uzak, daha uzun ya da daha geniş
  هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)
- **B016** eski bahis oyunundaki beşinci pay oku — eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok
  النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)

## ز و ج (root_000652): 42:11 أَزْوَٰجًا, 42:11 أَزْوَٰجًا, 42:50 يُزَوِّجُهُمْ

- **B001** eş; çift veya çiftin her bir üyesi — eş; çift veya çiftin her bir üyesi · birbirine bağlı iki öğe; bir çift · eşler; çiftler
  أصل يدل على مقارنة شيء لشيء (maqayis)؛ زوجان من الحمام أي ذكر وأنثى (ayn)؛ كل اثنين زوج والزوج ضد الفرد (jamhara)؛ الزوج خلاف الفرد وكل واحد منهما يسمى زوجا (sihah)؛ كل شيء اقترن أحدهما بالآخر فهما زوجان (tahdhib)؛ لكل قرينين زوج ولكل ما يقترن بآخر مماثلا له أو مضادا زوج (mufradat)
- **B002** eş; evlilikteki kadın veya erkek — evlilikteki kadın veya erkek eş · kadın eş · evlilikteki eşler
  الزوج زوج المرأة والمرأة زوج بعلها (maqayis)؛ زوج المرأة والمرأة زوج الرجل (jamhara)؛ زوج المرأة بعلها وزوج الرجل امرأته (sihah)؛ الرجل زوج المرأة والمرأة زوج الرجل وزوجته (tahdhib)؛ وزوجك الجنة وزوجة لغة رديئة (mufradat)
- **B003** eş kılmak, eş edinmek veya eşleştirmek — birine bir kadın eş sağlamak · bir kadınla evlenmek · bir kadınla evlenmek; belirli bir ağızda kullanılan kuruluş · eşleşme ve çift oluşturma · eşleştirme ve birbirine eş kılma · eşleşme ve çift oluşturma · kuşların birbiriyle eşleşmesi · eşleşmiş; bir eşi bulunan · onları eşleriyle bir araya getirmek · onları erkekler ve dişiler olarak eşleştirmek veya sınıflandırmak · kadının erkeği kendine eş edinmesi
  زوجته امرأة وتزوجت امرأة (sihah;tahdhib)؛ زوجناهم بحور عين أي قرناهم بهن (sihah;mufradat)؛ معنى يزوجهم يقرنهم وكل شيء اقترن أحدهما بالآخر فهما زوجان (tahdhib)
- **B004** tür, sınıf veya renk çeşidi — türler ve sınıflar · renk, tür veya sınıf · bir kumaş rengi · güzel bir bitki türü · çeşitli ve benzer bitki türleri · onları erkekler ve dişiler olarak eşleştirmek veya sınıflandırmak
  من كل زوج بهيج أراد به اللون (maqayis)؛ زوج من الثياب أي لون ومنها من كل زوج بهيج أي لون (ayn)؛ من كل ضرب من النبات حسن والزوج اللون وأزواج أي أنواع والزوج الصنف (tahdhib)؛ أزواجا من نبات شتى أي أنواعا متشابهة وثمانية أزواج أي أصناف (mufradat)
- **B005** benzerler ve aynı tutumu izleyen yoldaşlar — benzerler, denkler ve aynı tutumu izleyen yoldaşlar
  أزواجهم أي قرناءهم (sihah)؛ أزواجهم معناه نظراءهم ضرباءهم وعندي من هذا أزواج أي أمثال (tahdhib)؛ أزواجهم أي أقرانهم المقتدين بهم في أفعالهم وأشباها وأقرانا (mufradat)
- **B006** kapalı yolcu oturağına serilen desenli örtü — deve üzerindeki kapalı yolcu oturağına serilen desenli örtü
  النمط الذي يطرح على الهودج زوج لأنه زوج لما يلقى عليه (maqayis)؛ الزوج النمط يطرح على الهودج (jamhara;sihah;tahdhib)

## ن ع م (root_001525): 42:11 ٱلْأَنْعَٰمِ

- **B001** iyi yaşam durumu ve başkasına ulaştırılan iyilik — bağış, iyilik veya elverişli yaşam durumu · iyi durum ve esenlik · bolluk ve rahatlık · bol ve rahat yaşam · iyiliği başkasına ulaştırma
  أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)
- **B002** yumuşamak, rahat yaşamak veya rahat yaşatmak — yumuşamak · yumuşak; rahat yaşayan · rahat ve bolluk içinde yaşayan kadın · çocuklarını bolluk içinde yaşattı · rahat ve bolluk içindeki yaşam
  نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)
- **B003** övgü ve beğeni bildirmek — ne güzel; övgü bildirir · bu ne güzel · öyleyse ne güzel, yerinde olur
  نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)
- **B004** evet diyerek onaylamak veya söz vermek — evet; doğru; olur · ona evet dedi
  نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)
- **B005** develer ve geniş anlamda otlayan evcil hayvanlar — develer; deve varlığı · deve, sığır ve koyun topluluğu
  النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)
- **B006** devekuşu — devekuşu; erkek veya dişi birey · devekuşu türü veya topluluğu
  النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)
- **B007** devekuşuna benzetilerek ad verilen şeyler — devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol · Ay'ın konak yerlerinden biri
  على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)
- **B008** bir topluluğun dağılıp gücünü yitirmesi [kalıp] — dağıldılar, ayrıldılar veya güçlerini yitirdiler · hızla yola koyulup gittiler · yenilip dağıldılar
  شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)
- **B009** yumuşak esen nemli güney rüzgarı — yumuşak esen nemli güney rüzgarı
  النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)
- **B010** daha da artırmak veya ileri dereceye götürmek — artırdı; daha ileri götürdü · onu iyice ince öğüttü
  فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)
- **B011** bir yeri kendine uygun bulup orada kalmak [kalıp] — bir yere geldi, orayı uygun bulup kaldı
  أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)
- **B012** birine yaya gitmek ve ayakları yürüyerek kullanmak [kalıp] — ona yaya gitti veya onu yürüyerek aradı · ayaklarını yürümekle eskitti; hafif yürüdü
  تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)
- **B013** birini göz sevinci saymak veya bunun için dua etmek [kalıp] — Tanrı seni gözlere sevinç kaynağı kılsın · göz sevinci ve hoşnutluğu
  نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)

## ذ ر ء (root_000510): 42:11 يَذْرَؤُكُمْ

- **B001** varlıkları yaratıp bireylerini ortaya çıkarma ve çoğaltma — yaratmak ve bireylerini varlığa çıkarmak · ateş için yaratılmış olanlar · varlıkları yaratan · onun aracılığıyla sizi çoğaltmak ve çiftler halinde sürdürmek
  ذرأ الله الخلق يذرؤهم (maqayis;sihah;tahdhib); خلقهم (sihah;tahdhib); يذرؤكم به أي يكثركم (tahdhib); الذرء إظهار الله تعالى ما أبداه وأوجد أشخاصهم (mufradat)
- **B002** çocuklar ve onların soyundan gelenler — 
  منه الذرية وهي نسل الثقلين (sihah); الذرء عدد الذرية وأنمى الله ذرءك أي ذريتك (tahdhib); الذرية أصلها الصغار من الأولاد (mufradat)
- **B003** toprağa tohum ekme ve ilk ekin — toprağa tohum ekmek · ekimden sonraki ilk ekin
  ذرأنا الأرض أي بذرناها (maqayis); ذرأت الأرض أي بذرتها وزرع ذرئ (sihah); الزرع أول ما تزرعه تسميه الذريء وقد ذرأنا أرضا (tahdhib)
- **B004** kırlaşmadan veya başka bir kaynaktan doğan beyazlık — kırlaşmadan ya da benzeri bir durumdan doğan beyazlık · başın ön kısmındaki kır saç · kır saçlı ya da başında veya kulağında beyaz işaret bulunan · kır saçlı kadın ya da başında beyaz işaret bulunan dişi hayvan · çok beyaz tuz · saçı ağarıp kırlaşmak
  الذرأة البياض من شيب وغيره (maqayis); الذُّرْأ الشيب في مقدم الرأس وملح ذرآني (sihah); ذُرِئ رأس فلان إذا ابيض وجدي أذرأ وملح ذرآني (tahdhib); الذرأة بياض الشيب والملح (mufradat)
- **B005** birini öfkelendirme, bir şeye dadandırma ya da birine karşı kışkırtma [kalıp] — birini bir şeye öfkelendirmek ya da ona dadandırmak · birini arkadaşına karşı kışkırtıp onun üzerine salmak
  أذرأت فلانا بكذا أولعته به (maqayis); أذرأني فلان أي أغضبني وأذرأت الرجل بصاحبه إذا حرشته عليه وأولعته به (tahdhib)
- **B006** iki kişi arasındaki ayırıcı engel — iki kişi arasındaki engel
  ما بيني وبينه ذرء أي حائل (maqayis)
- **B007** sözün küçük ve tamamlanmamış bir parçası [kalıp] — sözün küçük ve tamamlanmamış bir parçası
  بلغني عن فلان ذرء من قول إذا بلغك طرف منه ولم يتكامل؛ الشيء اليسير من القول (tahdhib)

## ل ي س (root_001390): 42:11 لَيْسَ

- **B001** özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi — özneyi yalın, yüklem öğesini belirtme durumunda kullanarak olumsuzluk bildiren geçmiş biçimli eylem · bulunduğu ya da bulunmadığı yerden
  ليس كلمة جحود ... معناه لا أيس (ayn;tahdhib)؛ ليس: كلمة نفي، وهو فعل ماض (sihah)؛ تكون بمنزلة كان، ترفع الاسم وتنصب الخبر (tahdhib)
- **B002** ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı — ardından gelen adı belirtme durumunda kullanarak dışarıda bırakan istisna yapısı · senin dışında
  وقد يستثنى بها، تقول: جاءني القوم ليس زيدا (sihah)؛ يكون استثناء، ينصب به ... بمعنى ما عدا زيدا ... بمعنى إلا زيدا (tahdhib)
- **B003** bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı — bağlanan öğeyi olumsuzlayan ya da bir türün bütünüyle bulunmadığını bildiren söz
  ربما جاءت ليس بمعنى لا التي ينسق بها؛ وربما جاءت ليس بمعنى لا التبرئة (tahdhib)
- **B004** savaşta korkmayan ve rakibini bırakmayan yiğit — savaş karşısında yılmayan yiğitlik · savaştan korkmayan ve rakibini bırakmayan yiğit · övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz
  الأليس وهو الشجاع الذي لا يروعه الحرب (ayn;tahdhib)؛ ورجل أليس، أي شجاع بين الليس (sihah)؛ الأليس الذي لا يبارح قرنه؛ يقال للرجل الشجاع: أهيس أليس (tahdhib)
- **B005** yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan — yerinden ya da evinden ayrılmayan ağır kimse · övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz · su başında kalıp oradan ayrılmayan develer
  الأليس الرجل الثقيل الذي لا يبرح مكانه (ayn)؛ الأليس: الذي لا يبرح بيته؛ إبل ليس على الحوض: إذا أقامت عليه فلم تبرحه؛ وبالأليس الذي لا يبرح بيته، وهذا ذم (tahdhib)
- **B006** yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme — üzerine yüklenen her yükü taşıyan deve · güçlüğe katlanan ve yumuşak huylu olmak · görmezden gelip üzerinde durmamak · yumuşak huylu
  الأليس: البعير يحمل كل ما حمل (sihah)؛ تلايس الرجل: إذا كان حمولا حسن الخلق؛ وتلايست عن كذا وكذا: أي غمضت عنه؛ وفلان أليس دهثم: أي حسن الخلق (tahdhib)
- **B007** görüşü ve yargısı zayıf kişi — görüşü zayıf kimse
  الأليس الضعيف الرأي (ayn)
- **B008** ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi — ailesine karşı koruyucu kıskançlık göstermediği için alay edilen erkek · ailesine karşı koruyucu kıskançlık göstermeyen erkeği alaya alan yergi sözü
  الأليس: الديوثي الذي لا يغار ويتهزأ به؛ فيقال: هو أليس بورك فيه؛ فالليس يدخل في المعنيين: في المدح والذم (tahdhib)

## م ث ل (root_001397): 42:11 كَمِثْلِهِۦ, 42:40 مِّثْلُهَا

- **B001** benzerlik ve denklik — benzeri, dengi · benzer, eşdeğer · bunu başka bir şeye benzettim
  يدل على مناظرة الشيء للشيء (maqayis); المثل النظير (jamhara); كلمة تسوية (sihah); مثل وشبه بمعنى واحد (tahdhib); أعم الألفاظ الموضوعة للمشابهة (mufradat)
- **B002** ibret verici ağır cezalandırma — onu ibret verici biçimde cezalandırdı · öldürülen kişinin bedenini kesip bozdu · ibret verici ağır ceza · caydırıcı ağır cezalar · yönetici onu kısas gereği öldürdü · ondan hakkının karşılığını aldı · suça denk karşılık
  مثل به إذا نكل (maqayis); مثلت بالرجل إذا نكلت به (jamhara); مثل به يمثل مثلا أي نكل به (sihah); المثلة الاسم (tahdhib); نقمة تنزل بالإنسان فيجعل مثالا يرتدع به غيره (mufradat)
- **B003** benzer duruma aktarılan örnek söz — benzer bir duruma aktarılan örnek söz · dilden dile dolaşan özlü söz · örnek bir söz söyledi · bu dizeyi örnek gösterdi
  المثل المضروب (maqayis); المثل السائر (jamhara); ما يضرب به من الأمثال (sihah); يقال تمثل فلان إذا ضرب مثلا (tahdhib); عبارة عن قول في شيء يشبه قولا في شيء آخر (mufradat)
- **B004** nitelik veya hakkında verilen bilgi — niteliği veya hakkında verilen bilgi
  مثل الشيء صفته (sihah); مثلها هو الخبر عنها (tahdhib); مثلها صفتها (tahdhib); يعبر بهما عن وصف الشيء (mufradat)
- **B005** ayağa kalkıp dik durma — adam ayağa kalkıp dikildi · ayakta dik duran
  مثل الرجل قائما انتصب (maqayis); مثل الرجل مثولا إذا انتصب قائما (jamhara); مثل بين يديه مثولا أي انتصب قائما (sihah); الماثل القائم (tahdhib); أصل المثول الانتصاب (mufradat)
- **B006** yerinden ayrılma; yere sinip silinme — bulunduğu yerden ayrılıp gitti · yere sinmiş veya izi silinmiş
  مثل يمثل إذا زال عن موضعه (jamhara); مثل أي لطأ بالأرض وهو من الأضداد (sihah); الماثل اللاطىء بالأرض (tahdhib); ثم مثل أي ذهب (tahdhib); الماثل الدارس (tahdhib)
- **B007** döşek veya yere serilen yaygı — döşek veya yere serilen yaygı
  المثال الفراش والجمع مثل (maqayis); المثال الفراش (jamhara); المثال الفراش والجمع مثل (sihah); ما مثالان قال نمطان (tahdhib); النمط ما يفترش (tahdhib)
- **B008** başkasına benzetilerek yapılmış görüntü — başkasına benzetilerek yapılmış görüntü veya nesne · benzetilerek yapılmış görüntüler veya nesneler · onun görüntüsünü oluşturdu · bir biçim olarak canlandı veya göründü · örnek alınan biçim veya karşılık
  التمثال الصورة (jamhara); التمثال الصورة (sihah); مثلت له كذا تمثيلا إذا صورت له مثاله (sihah); التمثال اسم للشيء المصنوع مشبها (tahdhib); الممثل المصور على مثال غيره (mufradat)
- **B009** iyilik ve erdem bakımından üstün — daha iyi veya erdeme daha yakın · topluluğun en iyileri · en iyi olan veya en iyi yol · adam daha iyi ve seçkin bir duruma geldi
  أمثل بني فلان أدناهم للخير (maqayis); أماثل القوم خيارهم (jamhara); صار فاضلا (sihah); أمثل من فلان أي أفضل (tahdhib); الأشبه بالفضيلة (mufradat)
- **B010** buyruk veya örneğe uygun davranma [kalıp] — buyruğunu yerine getirdi · onun izinden ve yolundan gitti
  امتثل أمره أي احتذاه (sihah); امتثلت مثال فلان أي احتذيت حذوه وسلكت طريقته (tahdhib); وضع شيء ما ليحتذى به فيما يفعل (mufradat)
- **B011** ders çıkarılan olay veya gösterge — ders çıkarılan olay veya gerçeği gösteren belirti
  يكون المثل بمعنى العبرة (tahdhib); يكون المثل بمعنى الآية (tahdhib)
- **B012** hastalıktan sonra toparlanıp iyileşme [kalıp] — hastalığından sonra toparlanmaya başladı · hasta bugün daha iyi durumda
  تماثل من علته أي أقبل (sihah); تماثل المريض من المثول والانتصاب (tahdhib); المريض اليوم أمثل أي أفضل حالا (tahdhib)

## س م ع (root_000741): 42:11 ٱلسَّمِيعُ

- **B001** duymak ve dikkatle dinlemek — sesi kulakla algılamak · işitme gücü veya duyma eylemi · duyma eylemi veya duyulan şey · dikkatle dinlemek · duymaya çalışarak kulak vermek · beni dinle ve söylediklerime kulak ver · dinle · söylenenleri çokça dinleyen kimse · işiten kimse · kendi kulağımla duydum; görmeyle ilgili aktarılmış yorum kaynakta reddedilir
  إيناس الشيء بالأذن (maqayis)؛ سمعت الشيء سمعا (maqayis;sihah;mufradat)؛ الاستماع الإصغاء (sihah;mufradat)؛ سماع أي اسمع (maqayis;sihah)؛ السمع سمع الإنسان وغيره (tahdhib)
- **B002** kulak ve kulak açıklığı — kulak veya işitme yeri · kulak veya kulak açıklığı · kulak açıklığı veya işitme yeri · kulak · iki kulak veya iki işitme yeri
  السمع الأذن وهي المسمعة (ayn;tahdhib)؛ المسمعة خرقها (ayn)؛ المسمع خرق الأذن (tahdhib;mufradat)؛ السامعة الأذن (sihah)؛ المسمعان الأذنان (sihah;tahdhib)
- **B003** anlayıp kabul etmek ve uymak — sözü anlayıp kabul etmek ve ona uymak
  تارة عن الفهم وتارة عن الطاعة (mufradat)؛ فهمنا وارتسمنا (mufradat)؛ فهمنا وهم لا يفهمون (mufradat)؛ لم يستعملوا هذه الحواس استعمالا يجدي عليهم (tahdhib)
- **B004** duyurmak veya kavratmak — duymasını sağlamak veya kavratmak · başkasına duyuran kimse
  سمعه الصوت وأسمعه (sihah)؛ السميع المسمع (sihah;tahdhib)؛ أسمعهم أي أفهمهم (mufradat)؛ فعلت ذلك تسمعتك وتسمعة لك أي لتسمعه (tahdhib)
- **B005** adı yayılıp tanınmak — yaymak, tanınır kılmak veya adını öne çıkarmak · güzel ün ve iyi ad · duyulup yayılan ve konuşulan şey · insanlar duysun diye yapılan gösteriş · insanların haberi birbirinden duyup yayması
  السمع الذكر الجميل (maqayis;sihah)؛ السماع ما سمعت به فشاع (ayn;tahdhib)؛ سمعت بالشيء إذا أشعته (maqayis)؛ فعله رياء وسمعة (ayn;sihah)؛ سمع به أي شهره (sihah)؛ سمعت بفلان في الناس إذا نوهت بذكره (tahdhib)
- **B006** kötü söz işittirip sövmek [kalıp] — sövmek ve hoşlanmayacağı sözleri yüzüne söylemek · sövmek veya duymaz olmasını dilemek
  أسمعه الحديث وسمعه أي شتمه (sihah)؛ أسمعت فلانا إذا سببته (mufradat)؛ أسمعك الله أي جعلك الله أصم (mufradat)؛ سمعت بالرجل تسميعا إذا نددت به وشهرته وفضحته (tahdhib)؛ أسمعته القبيح وشتمته (tahdhib)
- **B007** kulağa hoş gelen ezgili ses — şarkı veya kulağa hoş gelen güzel ses · kadın şarkıcı
  المسمعة المغنية (maqayis;sihah)؛ السماع الغناء (ayn)؛ السماع اسم ما استلذت الأذن من صوت حسن (tahdhib)؛ المسمعة القينة المغنية (ayn)
- **B008** taşıma kabının sap veya denge parçası — kova veya su kabının yükü dengeleyen sapı ya da halkası · büyük su kabının iki yanı veya yük sepetinin iki taşıyıcı tahtası · kovaya sap takmak veya saplarını yükü hafifletecek biçimde bağlamak
  المسمع كالأذن للغرب (maqayis)؛ مسمع الدلو والغرب عروة في وسطه (ayn;sihah)؛ المسمع من المزادة ما جاوز خرت العروة إلى الظرف (ayn)؛ المسمعان جانبا الغرب (tahdhib)؛ المسمع عروة في داخل الدلو (tahdhib)؛ حلقة مسمع الغرب (mufradat)
- **B009** ayak bağı veya hareket kısıtlayıcı bağ — ayak bağı veya bağlama aracı · iki ayak bağı ve bir boyun bağıyla bağlanmış
  من أسماء القيد المسمع؛ ولي مسمعان وزمارة؛ مسمعا مزمرا أي مقيدا مسوجرا
- **B010** kurt ile sırtlan arasında sayılan yırtıcı — kurt ile sırtlan arasında sayılan yırtıcı veya onların yavrusu · o yırtıcıdan bile daha keskin işiten
  السمع ولد الذئب من الضبع (maqayis;tahdhib)؛ السمع سبع بين الذئب والضبع (ayn)؛ السمع سبع مركب (sihah)؛ أسمع من السمع الأزل (sihah)
- **B011** duyulsun ama bana ulaşmasın — duyulsun ama bana ulaşmasın
  اللهم سمعا لا بلغا (sihah)؛ سمع لا بلغ معناه يسمع ولا يبلغ (tahdhib)؛ أسمع بالدواهي ولا تبلغني (tahdhib)
- **B012** küçük başlı, ince uzun veya çevik atılgan kimse — küçük başlı, ince uzun, çevik atılgan veya kötü
  السمعمع الصغير الرأس (sihah;tahdhib)؛ السمعمع من الرجال المنكمش الماضي (tahdhib)؛ الشيطان الخبيث يقال له سمعمع (tahdhib)؛ السمعمع من الرجال الدقيق الطويل (tahdhib)؛ امرأة سمعمعة (tahdhib)
- **B013** bakıp dinlediği hâlde göremeyince tahmin eden kadın — dinleyip baktığı hâlde bir şey göremeyince tahmin eden kadın
  امرأة سمعنة نظرنة (sihah;tahdhib)؛ إذا تسمعت أو تبصرت فلم تر شيئا تظنته تظنيا (sihah)؛ إذا سمعت أو تبصرت فلم تر شيئا تظنت تظنيا (tahdhib)
- **B014** kimsenin görüp duymadığı boş arazide [kalıp] — kimsenin görüp duymadığı boş arazide
  تخرج بين سمع الأرض وبصرها؛ ليس معها أحد يسمع كلامها أو يبصرها إلا الأرض القفر؛ لقيته يمشي بين سمع الأرض وبصرها أي بأرض خلاء ما بها أحد
- **B015** öküz koşumundaki iki uzun çubuk — toprak sürmek için iki öküzün bağlandığı düzenekteki iki uzun çubuk
  السميعان من أدوات الحراثين؛ عودان طويلان في المقرن الذي يقرن به الثوران لحراثة الأرض
- **B016** beyin — beyin
  أم السمع وأم السميع الدماغ؛ نقبن الحرة السوداء عنهم كنقب الرأس عن أم السميع

## ب ص ر (root_000121): 42:11 ٱلْبَصِيرُ, 42:27 بَصِيرٌ

- **B001** gözle görme — görme duyusu; bakan göz · bir şeyi gözle görmek · gören, kör olmayan kişi · dikkatle dikilerek bakış; belirgin ve sert durum · göz ucuyla süzerek incelemek · yavrunun gözünün açılması
  أبصرته إذا رأيته (maqayis)؛ البصر العين (ayn;tahdhib)؛ البصر حاسة الرؤية وأبصرت الشيء رأيته والبصير خلاف الضرير (sihah)؛ والبصر معروف أبصر يبصر إبصارا فهو مبصر وبصير (jamhara)؛ الجارحة الناظرة والباصرة (mufradat)؛ رأيته لمحا باصرا أي نظرا بتحديق شديد (maqayis;sihah;tahdhib;mufradat)؛ بصر الجرو تبصيرا فتح عينه (ayn;tahdhib;mufradat)
- **B002** iç kavrayış — bir şeyi bilip kavramak · bilgi; kalbin kavrayışı · bilgili, kavrayış sahibi kişi · düşünüp tanımak · işinde veya dininde kavrayış sahibi olmak · kalp bilgisi, delil ve ibret · deliller, ibretler ve açıklamalar
  أحدهما العلم بالشيء وبصرت بالشيء إذا صرت به بصيرا عالما والبصيرة البرهان (maqayis)؛ البصر نفاذ في القلب والبصيرة اسم لما اعتقد في القلب من الدين وحقيق الأمر واستبصر في أمره ودينه (ayn;tahdhib)؛ حسن البصيرة إذا كان مستبصرا في دينه (jamhara)؛ البصر العلم وبصرت بالشيء علمته والتبصر التأمل والتعرف والبصيرة الحجة والاستبصار في الشيء (sihah)؛ لقوة القلب المدركة بصيرة وبصر وعلى معرفة وتحقق (mufradat)
- **B003** aydınlatıcı açıklık — aydınlık, açık kılan ve görmeyi sağlayan · açıklama ve belirgin kılma
  المبصرة المضيئة تبصرهم أي تجعلهم بصراء والمبصرة بالفتح الحجة (sihah)؛ مبصرة مضيئة وتبين لهم ومبصرا بها (tahdhib)؛ آياتنا مبصرة أي مضيئة للأبصار وقيل صار أهله بصراء وتبصرة أي تبصيرا وتبيانا (mufradat)
- **B004** kan izi — yerde veya bedende kan lekesi, kan izi · kanlar; kan bedelleri veya öçler
  البصيرة القطعة من الدم إذا وقعت بالأرض استدارت (maqayis;jamhara)؛ بصائر الدماء طرائقها على الجسد (ayn)؛ البصيرة من الدم ما كان على الأرض وشيء من الدم يستدل به على الرمية (sihah)؛ بصيرة من دم والجدية منها على الأرض والبصيرة الدية ومقدار الدرهم من الدم (tahdhib)؛ البصيرة قطعة من الدم تلمع (mufradat)
- **B005** koruyucu savaş gereci — kalkan, zırh veya giyilen savaş koruması
  البصيرة الترس فيما يقال (maqayis)؛ البصيرة الدرع وما لبس من السلاح فهو بصائر السلاح (ayn;tahdhib)؛ البصيرة في هذا البيت الترس أو الدرع (sihah)؛ الترس اللامع (mufradat)
- **B006** kalın kenar ve ek yeri — bir şeyin yanı, kenarı veya kalın dış yüzü · iki deri parçasını birleştirip dikme · çadır, elbise veya kapta iki parça arası · iki parça arasında yamanmış ek
  بصر الشيء غلظه والبصر هو أن يضم أديم إلى أديم يخاطان والبصيرة ما بين شقتي البيت (maqayis)؛ البصر غلظ الشيء نحو بصر الجبل والسماء والحائط (ayn)؛ بصر كل شيء جلده الظاهر وثوب ذو بصر إذا كان غليظا وثيجا (jamhara)؛ البصر أن يضم أديم إلى أديم والبصر بالضم الجانب والحرف من كل شيء وغلظها (sihah)؛ الباصر الملفق بين شقتين والبصيرة الشقة التي تكون على الخباء والبصر أن يضم أديم إلى أديم (tahdhib)؛ البصر الناحية والبصيرة ما بين شقتي الثوب والمزادة وبصرت الثوب والأديم إذا خطت ذلك الموضع (mufradat)
- **B007** yumuşak parlak taş — yumuşak veya parlak taş; böyle taşlı yer · sonundaki ek düşmüş biçimiyle yumuşak taş · adı bu taşlı yer olan yere gitmek
  البصرة الحجارة الرخوة وبصر بكسر الباء من الأصل الثاني (maqayis)؛ البصرة أرض حجارتها جص والبصرة الحجارة التي فيها بعض اللين (ayn)؛ البصرة حجارة رخوة وبه سميت البصرة (jamhara)؛ البصرة حجارة رخوة إلى البياض وبصر بالكسر (sihah)؛ البصر والبصرة الحجارة البراقة وأرض كأنها جبل من جص وبصر الأرض غلظها وبصر فلان تبصيرا إذا أتى البصرة (tahdhib)؛ البصرة حجارة رخوة تلمع ويقال له بصر (mufradat)

## ق ل د (root_001249): 42:12 مَقَالِيدُ

- **B001** burup üst üste dolama — burma ve bir şeyi ötekinin üzerine dolama · ipi burdu · burulmuş ip · burulmuş, iki telli bilezik · dizginin bağlandığı, ucu bükülen halka · otu burmaya yarayan eğri uçlu sopa ya da orak benzeri araç
  أصل القلد الفتل وقلدت الحبل (maqayis;mufradat)؛ القلد إدارتك قلبا على قلب ولي الحديدة (ayn;tahdhib)؛ القلد السوار المفتول من فضة (sihah)؛ المقلد يقلد بها الكلأ كما يقلد القت أي يفتل (maqayis;sihah;tahdhib)؛ القلد لي الشيء على الشيء (tahdhib)
- **B002** boyna takılan süs ya da tanıtma işareti — boyna takılan süs ya da işaret · kurbanlık hayvanın boynuna tanıtıcı işaret asma · öne geçtiği işaretle belirtilen seçkin yarış atı
  تقليد البدنة أن يعلق في عنقها شيء ليعلم أنها هدى (maqayis)؛ هي قلادة الإنسان والبدنة والكلب (ayn)؛ القلادة التي في العنق وتقليد البدنة (sihah)؛ القلادة ما جعل في العنق جامع للإنسان والبدنة والكلب (tahdhib)؛ القلادة المفتولة التي تجعل في العنق (mufradat)؛ المقلد من الخيل السابق وقلائد الخيل أي هن كرام (sihah;tahdhib)
- **B003** kılıcı omuz askısıyla kuşanma — kılıcı kuşandı veya omuzdan astı · kılıç askısının omuza dayandığı yer
  وتقلدت السيف ومقلد الرجل موضع نجاد السيف على منكبه (maqayis;sihah)؛ تقلدت السيف والأمر ونحوه (ayn)؛ وتقلدت السيف وتقلدت الأمر (tahdhib)؛ تقلد سيفه تشبيها بالقلادة وقلدته سيفا إذا وشحته به (mufradat)
- **B004** sorumluluk yükleme veya üstlenme [kalıp] — işi ya da sorumluluğu üstlendi · ona bir iş verdi ve sorumluluğunu yükledi · inanç konusunda bir görüşü benimseyip izleme
  تقلدت السيف والأمر ونحوه الزمته نفسي وقلدنيه فلان أي ألزمنيه وجعله في عنقي (ayn)؛ ومنه التقليد في الدين وتقليد الولاة الأعمال (sihah)؛ تقلدت الأمر وقلد فلان فلانا عملا تقليدا (tahdhib)؛ قلدته عملا ألزمته (mufradat)
- **B005** kalıcı kötü damga yükleyen yergi [kalıp] — kişide kalıcı leke bırakan yergi · ona silinmeyen kötü bir ün yükledi
  يقال قلد فلان قلادة سوء إذا هجاه بما يبقى عليه وسمه (maqayis)؛ قلده طوق الحمامة أي لا يفارقه (maqayis)؛ قلدته هجاء ألزمته (mufradat)
- **B006** açma anahtarı; saklama deposu — anahtar · depo · anahtarlar; başka açıklamalarda depolar veya kuşatıp koruyan araçlar
  المقاليد يقال هي الخزائن ولعلها سميت بذلك لأنها تحصن الأشياء أي تحفظها وتحوزها (maqayis)؛ الإقليد المفتاح والمقلاد الخزانة ويجمع مقاليد (ayn)؛ الإقليد المفتاح والجمع المقاليد (sihah)؛ مقاليد السموات والأرض معناه مفاتيح والمقلاد الخزانة والمقاليد الخزائن (tahdhib)؛ مقاليد السموات والأرض أي ما يحيط بها وقيل خزائنها وقيل مفاتحها (mufradat)
- **B007** su payı ve dönemli sulama sırası — su payı ya da sulama sırası · gökyüzü bize belirli aralıkta yağmur verdi · ateşli hastalık onu her gün tuttu · suyu sırayla kullanıyorlar
  الأصل الآخر القلد الحظ من الماء وسقينا أرضنا قلدها وسقتنا السماء قلدا (maqayis)؛ القلد بالكسر يوم تأتي فيه الربع وسقتنا السماء قلدا أي مطرتنا لوقت (sihah)؛ سقى إبله قلدا وهو السقي كل يوم وقلدته الحمى إذا أخذته كل يوم (tahdhib)؛ قلدك من الماء أراد يوم سقيه ماله وما بين القلدين ظمء (tahdhib)
- **B008** sıvıyı bir kaba döküp biriktirme [kalıp] — suyu havuza döküp biriktirdi · sütü tuluma döküp biriktirdi · içti ve içecek gövdesinde toplandı
  القلد جمع الماء في الشيء يقال قلدت أقلد قلدا أي جمعت ماء إلى ماء (tahdhib)؛ قلدت الماء في الحوض وقلدت اللبن في السقاء إذا قدحت بقدحك ثم صببته (tahdhib)؛ قلد من الشراب في جوفه إذا شرب (tahdhib)
- **B009** denizin insanları içine alıp kapatması [kalıp] — deniz çok sayıda kişiyi içine kapattı ve boğdu
  أقلد البحر على خلق كثير إذا أحصنهم في جوفه (maqayis)؛ أقلد البحر على خلق كثير أي ضم عليهم (ayn)؛ أقلد البحر على خلق كثير أي غرقهم كأنه أغلق عليهم (sihah)؛ أقلد البحر على خلق كثير أي ضم عليه وأحضنه في جوفه (tahdhib)
- **B010** boyna kılıçla vurma [kalıp] — boynuna kılıçla vurdu
  قلدته سيفا يقال تارة إذا وشحته به وتارة إذا ضربت عنقه (mufradat)

## ب س ط (root_000116): 42:12 يَبْسُطُ, 42:27 بَسَطَ

- **B001** yaymak ve uzatmak — bir şeyi yaymak, uzatmak ve genişletmek · toplamanın karşıtı olan yayılma ve açılma · bir şeyin yere yayılıp uzanması · bir şeyi yaymak
  أصل واحد وهو امتداد الشيء في عرض أو غير عرض (maqayis)؛ البسط نقيض القبض (ayn)؛ بسط الشيء نشره وانبسط الشيء على الأرض (sihah)؛ البسط نقيض القبض (tahdhib)؛ بسط الشيء نشره وتوسيعه (mufradat)
- **B002** yaygı; geniş ve düz arazi — yaygı veya geniş, yayılmış arazi · yayılmış, geniş arazi · geniş veya yayılmış yer · çıkıntısız, düz arazi
  البساط ما يبسط والبساط الأرض وهي البسيطة (maqayis)؛ البسيطة من الأرض كالبساط من المتاع (ayn)؛ البساط ما يبسط والبساط الأرض الواسعة ومكان بسيط وبساط (sihah)؛ البساط الأرض العريضة الواسعة وأرض بساط مستوية لا نبك فيها (tahdhib)؛ البساط اسم لكل مبسوط والله جعل لكم الأرض بساطا (mufradat)
- **B003** genişlik, artış ve üstünlük — genişlik, artış ve üstünlük · genişlik veya artış · geçim imkanlarını genişletip çoğaltmak · bilgi ve bedende genişlik ve artış · geniş yapılı veya erişimi uzun · sahibini rahatça alacak geniş yatak
  البسطة في كل شيء السعة وهو بسيط الجسم والباع والعلم (maqayis)؛ البسطة الفضيلة على غيرك (ayn)؛ البسطة السعة وفلان بسيط الجسم والباع وفراش يبسطك إذا كان واسعا (sihah)؛ فالبسطة الزيادة وفراش يبسطني إذا كان سابغا (tahdhib)؛ ولو بسط الله الرزق أي وسعه وزاده بسطة أي سعة (mufradat)
- **B004** eli uzatıp serbestçe kullanmak [kalıp] — eli istemek, almak, saldırmak veya vermek için uzatmak · vermeye açık ve serbest el · iki kolunu uzatmış · istemek için iki avucunu suya doğru uzatan
  يد فلان بسط إذا كان منفاقا (maqayis)؛ بسط إلينا فلان يده بما نحب ونكره (ayn)؛ يد بسط أي مطلقة وبل يداه بسطان (sihah)؛ بسط فلان يده بما يحب ويكره وبسطان مبسوطتان (tahdhib)؛ بسط اليد مدها وبسط الكف للطلب والأخذ والصولة والبذل (mufradat)
- **B005** rahat ve açık ilişki kurmak — rahat ve akıcı konuşan erkek · rahat konuşan veya kolay ilişki kuran kadın · çekingenliği bırakıp rahatça ilişki kurma · insanlara sevimli gelen açık yüz
  البسيط الرجل المنبسط اللسان والمرأة بسيطة (ayn)؛ الانبساط ترك الاحتشام وبسطت من فلان فانبسط (sihah)؛ البسيط الرجل المنبسط اللسان وليكن وجهك بسطا (tahdhib)
- **B006** beni de sevindirir [kalıp] — seni sevindiren şey beni de sevindirir
  إنه ليبسطني ما بسطك ويقبضني ما قبضك أي يسرني ما سرك ويسوءني ما ساءك (ayn)؛ إنه ليبسطني ما بسطك ويقبضني ما قبضك أي يسرني ما سرك ويسوءني ما ساءك (tahdhib)
- **B007** dolaşmak ve gezintiye çıkmak — ülkede enine boyuna dolaşmak · bitkili açık alanda gezintiye çıkmak
  تبسط في البلاد أي سار فيها طولا وعرضا (sihah)؛ التبسط التنزه خرج يتبسط مأخوذ من البساط وهي الأرض ذات الرياحين (tahdhib)
- **B008** yavrusuyla serbest bırakılan dişi deve — yavrusuyla bırakılan ve ondan esirgenmeyen dişi deve · yavrularıyla serbest bırakılmış dişi develer · dişi deveyi yavrusuyla bırakmak
  الناقة التي خليت هي وولدها لا تمنع منه بسط (maqayis)؛ الأبساط من النوق التي معها أولادها والواحد بسط (ayn)؛ البسط الناقة تخلى مع ولدها لا يمنع منها (sihah)؛ البساط جمع بسط وهي الناقة التي تركت وولدها لا يمنع منها (tahdhib)؛ البسط الناقة تترك مع ولدها وقد أبسط ناقته أي تركها مع ولدها (mufradat)
- **B009** belirli bir şiir ölçüsü — belirli bir şiir ölçüsü türü
  البسيط نحو من العروض (ayn)؛ البسيط جنس من العروض (sihah)
- **B010** sunulan gerekçeyi kabul etmek [kalıp] — kusur için sunulan gerekçeyi kabul etmek
  بسط العذر قبوله (sihah)
- **B011** uzak mesafe ve tam uzanma erişimi [kalıp] — uzun ve uzak geçit · ayakta durup eli uzatarak ulaşılan tam boy mesafesi · ulaşılabilir bir millik mesafe
  سرنا عقبة باسطة وهي البعيدة (sihah)؛ عقبة باسطة أي بعيدة طويلة وقامة باسطة إذا حفر مدى قامته وقد مد يده (tahdhib)
- **B012** yapısal olarak bileşiksiz — parçalardan oluşması veya düzenlenmesi düşünülemeyen
  استعار قوم البسط لكل شيء لا يتصور فيه تركيب وتأليف ونظم (mufradat)
- **B013** çatallı olmayan deve semeri — çatallı olmayan deve semeri · çatalsız, yayvan deve semeri
  الباسوط من الأقتاب ضد المفروق ويقال قتب مبسوط ويجمع مباسيط (tahdhib)

## ر ز ق (root_000560): 42:12 ٱلرِّزْقَ, 42:19 يَرْزُقُ, 42:27 ٱلرِّزْقَ, 42:38 رَزَقْنَٰهُمْ

- **B001** yararlanılmak üzere verilen pay — yararlanılan pay veya sağlanan geçimlik · Tanrı ona yararlanacağı bir pay verdi · kendisine bilgi verildi · yararı sağlayan veya ulaşmasına aracılık eden · bütün varlıklara sürekli geçim payı sağlayan Tanrı için özel niteleme
  أصيل واحد يدل على عطاء لوقت ثم يحمل عليه غير الموقوت (maqayis)؛ الرزق عطاء الله (maqayis)؛ رزق الله يرزق العباد رزقا اعتمدوا عليه (ayn)؛ الرزق ما ينتفع به والرزق العطاء (sihah)؛ الرزق معروف (tahdhib)؛ الرزق يقال للعطاء الجاري وللنصيب (mufradat)؛ الرازق يقال لخالق الرزق ومعطيه والمسبب له والرزاق لا يقال إلا لله تعالى (mufradat)
- **B002** yenip beslenilen yiyecek — yenip bedeni besleyen yiyecek
  وجد عندها رزقا عنبا في غير حينه (tahdhib)؛ لما يصل إلى الجوف ويتغذى به (mufradat)؛ فليأتكم برزق منه أي بطعام يتغذى به (mufradat)؛ عني به الأغذية (mufradat)
- **B003** yağmur — yağmur; gökten inerek canlılığı sürdüren su
  وقد يسمى المطر رزقا (sihah)؛ في السماء رزقكم قال المطر (tahdhib)؛ في السماء رزقكم قيل عني به المطر الذي به حياة الحيوان (mufradat)
- **B004** asker ödeneği — yönetici askerlere ödeneklerini verdi · askerlere tek seferde verilen ödeme · askerler ödeneklerini aldı
  إذا أخذ الجند أرزاقهم قيل ارتزقوا رزقة واحدة (ayn)؛ الرزقة بالفتح المرة الواحدة وهي أطماع الجند وارتزق الجند أي أخذوا أرزاقهم (sihah)؛ رزق الأمير جنده فارتزقوا ارتزاقا (tahdhib)؛ رزق الجند رزقة واحدة ورزقوا رزقتين (tahdhib)؛ ارتزق الجند أخذوا أرزاقهم والرزقة ما يعطونه دفعة واحدة (mufradat)
- **B005** iyiliğe gönül borcunu bildirme — size verilen iyiliğe karşılık yalanlamayı seçiyorsunuz · bana yaptığım iyilik için gönül borcunu bildirdin
  الرزق بلغة أزدشنوءة الشكر (maqayis)؛ فعلت ذلك لما رزقتني أي لما شكرتني (maqayis)؛ وتجعلون رزقكم أنكم تكذبون أي شكر رزقكم (sihah)؛ تجعلون شكر رزقكم التكذيب (tahdhib)؛ تجعلون نصيبكم من النعمة تحري الكذب (mufradat)
- **B006** iyi talih sahibi olma — talihli; payına iyi sonuçlar düşen
  رجل مرزوق أي مجدود (sihah)؛ تنبيه أن الحظوظ بالمقادير (mufradat)
- **B007** biçime bağlı adlandırmalar — beyaz keten giysiler · belirli bir üzüm çeşidi
  الرازقية ثياب كتان بيض (sihah)؛ الرازقية ثياب كتان بيض (tahdhib)؛ الرازقي من الأعناب هو الملاحي (tahdhib)

## ع ل م (root_001040): 42:12 عَلِيمٌ, 42:14 ٱلْعِلْمُ, 42:18 وَيَعْلَمُونَ, 42:24 عَلِيمٌۢ, 42:25 وَيَعْلَمُ, 42:32 كَٱلْأَعْلَٰمِ, 42:35 وَيَعْلَمَ, 42:50 عَلِيمٌ

- **B001** bilme ve gerçeğini kavrama — bilgi; bir şeyi gerçeğiyle kavrama · bir şeyi bilmek ve tanımak · haberinden haberdar olmak · bildirmek, haberdar etmek · öğretmek, öğrenmesini sağlamak · öğrenmek, kavramaya yönelmek · bilmek; buyrukta bil ki · bilgi yarışında yenmek · bilen ve bildiğine göre davranan kişi · bilgili, bilgi sahibi · çok bilgili, çok bilen · son derece bilgili kişi
  العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)
- **B002** ayırt edici ve yol gösterici işaret — ayırt edici işaret · bayrak, sancak · yol gösteren belirgin dağ · kumaşın kenar işareti veya deseni · yol gösteren iz veya belirti · savaşta kendine ayırt edici işaret takmak · kumaşı işaretlemek · işaret olarak kullanılan kına · sarığı tanıtıcı bir biçimde sarmak · tanınmış ve öne çıkan kişi · son saatin yaklaştığını gösteren belirti
  أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)
- **B003** evren ve bütün yaratılmışlar — evren veya yaratılmışlar bütünü · bütün yaratıklar veya varlık sınıfları · evrenler, varlık dünyaları
  العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)
- **B004** üst dudak yarığı — üst dudaktaki yarık · üst dudağı yarık kişi veya deve · üst dudağını yarmak
  العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)
- **B005** deniz ya da suyu bol kuyu — deniz · suyu bol kuyu
  العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)
- **B006** doğan veya atmaca türü yırtıcı kuş — doğan veya atmaca · çevik ve zeki adam
  العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)
- **B007** erkek sırtlan — erkek sırtlan
  العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)

## ش ر ع (root_000789): 42:13 شَرَعَ, 42:21 شَرَعُوا۟

- **B001** Tanrı tarafından belirlenmiş dinsel yol ve hükümler — açık ve dosdoğru yol · dinsel yol ve yöntem · Tanrı'nın kulları için belirlediği dinsel düzen · din konusunda hüküm koyup açıkça bildirmek · herkesin kullandığı ana yol · bilgili, bildiğini uygulayan ve öğreten din bilgini
  الشرعة في الدين والشريعة (maqayis)؛ ما شرع الله للعباد من أمر الدين (ayn)؛ ما شرع الله لعباده من الدين؛ سن (sihah)؛ الشرعة في الدين والمنهاج الطريق؛ شرع أي أظهر (tahdhib)؛ نهج الطريق الواضح؛ الطريقة الإلهية (mufradat)
- **B002** açık su alma yeri ve oraya girip içme — hayvanların suya girdiği açık sulama yeri · hayvanların su içmesi için hazırlanmış kıyı yeri · sürülerin suya indiği yerler · su yerine girip ağzıyla su almak · hayvanların suya girip içmesi · suya girmiş ve içmekte olan develer · develeri su çekmeden içebilecekleri açık suya götürme
  الشريعة مورد الشاربة الماء؛ الإبل الشروع التي شرعت ورويت (maqayis)؛ شرع الوارد الماء؛ الشريعة والمشرعة موضع على شاطئ البحر (ayn)؛ مشرعة الماء؛ شرعت الدواب في الماء (sihah)؛ مشارع الماء؛ الشرعة والشريعة المشرعة؛ شرعت الواردة الشريعة (tahdhib)؛ تشبيها بشريعة الماء (mufradat)
- **B003** bir işe girip onu yapmaya başlamak [kalıp] — bu işe girip onunla uğraşmaya başlamak · belirli bir işi ele alıp başlatmak
  شرع الوارد الماء شروعا (ayn)؛ شرعت في هذا الأمر شروعا أي خضت (sihah)؛ شرع فلان في كذا وكذا أي أخذ فيه (tahdhib)؛ يشرعون فيه شروعا واحدا؛ تشرع في أمره (mufradat)
- **B004** hedefe uzatmak veya geçişe açmak [kalıp] — mızrağı hedefe doğrultmak · mızrakları hedefe doğru uzatmak · kapıyı geçiş yoluna açmak · yolu açıp geçilir duruma getirmek
  أشرعت الرمح نحوه إشراعا؛ أشرعت طريقا إذا أنفذته وفتحته (maqayis)؛ أشرعت الرماح نحوهم إشراعا (ayn)؛ أشرعت بابا إلى الطريق؛ أشرعت الرمح قبله (sihah)؛ أشرعنا الرماح نحوهم؛ السيوف شرعن إليه (tahdhib)؛ أشرعت الرمح قبله (mufradat)
- **B005** gerilmiş, yükseltilmiş veya belirgin biçimde uzun — gerilmiş teller · gerilmiş tek tel · gemi yelkeni · gemiye yelken takmak · devenin boynunu yukarı kaldırması · uzun mızrak · uzun boyunlu dişi deve
  الشرع الأوتار؛ شراع السفينة؛ شرع البعير عنقه؛ رمح شراعي (maqayis)؛ الشرعة الوتر؛ الشراع شراع السفينة؛ رفع شراعه؛ رمح شراعي (sihah)؛ الشراع الأوتار؛ شراع السفينة؛ رفع شراعه؛ الشراعية الناقة الطويلة العنق (tahdhib)؛ شرعت السفينة جعلت لها شراعا؛ الشرع خص بما يشرع من الأوتار (mufradat)
- **B006** deriyi bacaklar arasından yarıp yüzmek [kalıp] — deriyi bacakların arasından yarıp yüzmek
  شرعت الإهاب إذا شققت ما بين رجليه (maqayis)؛ شرعت الإهاب إذا سلخته؛ شققت ما بين الرجلين ثم سلخته (sihah)؛ شرعت الإهاب إذا شققت ما بين الرجلين وسلخته؛ الشرع أوسعها وأبينها (tahdhib)
- **B007** birbirine benzer veya eşit olma [kalıp] — bu, onun benzeri · bu, bunun dengi · bu işte eşit durumdalar
  هذه شرعة ذاك أي مثله (ayn)؛ هذه شرعة هذه؛ هذا شرع هذا؛ هما شرعان أي مثلان (sihah)؛ هم في الأمر شرع أي سواء؛ هذا شرعة ذاك أي مثله (tahdhib)؛ هم في هذا الأمر شرع أي سواء (mufradat)
- **B008** yeterli gelmek ve ulaşılanla yetinmek [kalıp] — bu sana yeter · ulaştığın kadarı sana yeter
  شرعك هذا أي حسبك؛ شرعك ما بلغك المحل (sihah)؛ شرعك هذا أي حسبك؛ شرعك ما بلغك المحلا (tahdhib)؛ شرعك من رجل زيد كقولك حسبك (mufradat)
- **B009** yakın durmak veya üzerine uzanıp görünmek — suya yönelmiş, başları görünür balıklar · batışa yaklaşmış yıldızlar · yola bitişik ve insanlara yakın ev · yakın duran veya üzerine uzanan
  حيتان شروع رافعة رأسها؛ الشوارع من النجوم الدانية من المغيب؛ كل دان من شيء فهو شارع؛ الدار الشارعة (tahdhib)؛ حيتانهم يوم سبتهم شرعا جمع شارع؛ شارعة الطريق جمعها شوارع (mufradat)

## د ي ن (root_000504): 42:13 ٱلدِّينِ, 42:13 ٱلدِّينَ, 42:21 ٱلدِّينِ

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)

## و ص ي (root_001656): 42:13 وَصَّىٰ, 42:13 وَصَّيْنَا

- **B001** bir şeyi başka şeyle bağlama veya bitişik sürdürme — bir şeyi başka bir şeye bağlamak veya onunla bitiştirmek · geceyi gündüze ekleyerek işi kesintisiz sürdürmek · bitki örtüsü birbirine bağlı ve kesintisiz olan arazi · bitkinin bir kısmının başka kısmıyla birleşip kesintisiz olması · birbirine bağlı ve kesintisiz bitki · arazinin bitki örtüsünün birbirine bağlanıp kesintisiz olması · başka bir çöl alanına bitişen çöl · soyu, sebebi ve görünüş yolu başka biriyle bağlantılı olan kişi
  أصل يدل على وصل شيء بشيء (maqayis)؛ ووصيت الشيء وصلته (maqayis)؛ وصيت الليلة باليوم وصلتها (maqayis)؛ تواصى النبت إذا اتصل (jamhara;sihah)؛ أرض واصية متصلة النبات (sihah;mufradat)؛ فلاة واصية يتصل بفلاة أخرى (tahdhib)؛ وصى الشيء يصي إذا اتصل ووصاه غيره وصله (tahdhib)
- **B002** başkasına bırakılan iş talimatı — başkasına yapılması için verilen öğütlü iş talimatı · vasiyet; ölümden sonra uygulanması istenen talimat veya bırakılan istek · birine yapılacak işi bildirmek veya öğütlü talimat vermek · talimat veya bırakılan istek anlamındaki ad · bırakılan talimatı yürütme görevi veya bu görevde bulunma · talimatı veya isteği bırakan kişi · vasi; bırakılan talimatı yerine getirmekle görevlendirilen kişi · kendisine söylenen şeyi unutmasından kaygı duyulan kimse için kullanılan söz · birini bırakılan talimatı yürütmekle görevlendirmek
  الوصية من هذا القياس كأنه كلام يوصى أي يوصل (maqayis)؛ وصيته توصية وأوصيته إيصاء (maqayis;sihah;mufradat)؛ الوصاة كالوصية (ayn;jamhara;tahdhib)؛ الوصاية مصدر الوصي (ayn;sihah)؛ الوصية بعد الموت (ayn)؛ الوصية ما أوصيت به (ayn;tahdhib)؛ أوصيت له بشئ وأوصيت إليه إذا جعلته وصيك (sihah)؛ الوصي الموصي والموصى إليه جميعا (jamhara)؛ التقدم إلى الغير بما يعمل به مقترنا بوعظ (mufradat)
- **B003** birbirine öğüt veya talimat iletmek — birbirine öğüt vermek veya yapılacak şeyi karşılıklı bildirmek; bağlamına göre karşılıklı bağlantı kurmak
  تواصى القوم إذا تواصلوا (jamhara)؛ تواصى القوم أي أوصى بعضهم بعضا (sihah)؛ تواصى القوم إذا أوصى بعضهم إلى بعض (mufradat)
- **B004** otlağın sürüye bolca elverişli olması — otlağın otlayan hayvanlara uygun gelip onlara bol ve rahat yem sağlaması
  إذا أطاع المرعى للسائمة فأصابته رغدا قيل وصى لها المرتع يصي وصيا (ayn;tahdhib)

## ق و م (root_001273): 42:13 أَقِيمُوا۟, 42:15 وَٱسْتَقِمْ, 42:38 وَأَقَامُوا۟, 42:45 ٱلْقِيَٰمَةِ, 42:45 مُّقِيمٍ, 42:52 مُّسْتَقِيمٍ

- **B001** erkekler topluluğu ve yakın çevresi — aslen erkeklerden oluşan topluluk · bir erkeğin yandaşları ve yakın soy çevresi · topluluklar; çoğulun çoğulu
  القوم الرجال دون النساء؛ قوم كل رجل شيعته وعشيرته (ayn;tahdhib)؛ القوم الرجال دون النساء؛ ربما دخل النساء فيه على سبيل التبع (sihah)؛ القوم جماعة الرجال في الأصل دون النساء؛ وفي عامة القرآن أريدوا به والنساء جميعا (mufradat)؛ القوم جمع امرئ ولا يكون ذلك إلا للرجال؛ وربما استعير في غيرهم (maqayis)
- **B002** ayağa kalkma ve dik durma — ayağa kalkmak veya dikilmek · bir kez ayağa kalkma; iki bölüm arasındaki ayakta duruş · kökleri üzerinde dikili kalmış
  القومة ما بين الركعتين من القيام؛ قمت قياما؛ منها هامد ومنها قائم (ayn;tahdhib)؛ قام الرجل قياما؛ القومة المرة الواحدة؛ قامت الدابة وقفت (sihah)؛ قيام بالشخص إما بتسخير أو اختيار؛ ساجدا وقائما؛ تركتموها قائمة على أصولها (mufradat)؛ قام قياما والقومة المرة الواحدة إذا انتصب (maqayis)
- **B003** bir işe kararlılıkla girişme [kalıp] — bu işi üstlenip kararlılıkla girişti
  قام بمعنى العزيمة؛ قام بهذا الأمر إذا اعتنقه؛ قيام عزم (maqayis)؛ القيام الذي هو العزم؛ إذا قمتم إلى الصلاة (mufradat)
- **B004** sürekli gözetip yönetme — işi gözeten, koruyan ve yürüten kişi · topluluğun işlerini yöneten kişi · her şeyi sürekli yöneten ve koruyan · onu taşıyamadı veya buna gücü yetmedi
  قيم القوم من يسوس أمرهم ويقومهم؛ القائم في الملك ونحوه الحافظ؛ القيوم (ayn)؛ قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم؛ القيوم اسم من أسماء الله (sihah)؛ قيم القوم الذي يقومهم ويسوس أمرهم؛ القائم بالأمر؛ القيوم القائم على كل شيء (tahdhib)؛ قيام للشيء هو المراعاة للشيء والحفظ له؛ قوامين لله؛ القيوم القائم الحافظ لكل شيء (mufradat)؛ قام بهذا الأمر إذا اعتنقه؛ قوام الدين والحق أي به يقوم (maqayis)
- **B005** sürdürüp gereğini yerine getirme [kalıp] — bir şeyi sürdürmek, işler halde tutmak veya gereğini yerine getirmek · ibadetin ya da kitabın gereklerini eksiksiz uygulamak
  أقام الشيء أي أدامه؛ يقيمون الصلاة (sihah)؛ أقمت الشيء وقومته فقام بمعنى استقام؛ إقام الصلاة (tahdhib)؛ إقامة الشيء توفية حقه؛ تقيموا التوراة والإنجيل؛ أقيموا الصلاة؛ مقيم الصلاة (mufradat)
- **B006** bir yerde kalma ve kalınan yer — bir yerde yerleşip kalmak · ayak basılan veya kalınan yer ya da süre; oturum veya toplanmış topluluk
  أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين؛ المقام والمقامة الموضع الذي تقيم فيه (ayn;tahdhib)؛ المقامة الإقامة؛ المقامة المجلس والجماعة من الناس؛ المقام موضع القيام أو الإقامة (sihah)؛ المقام يكون مصدرا واسم مكان القيام وزمانه؛ المقامة الإقامة؛ لا مقام لكم أي لا مستقر لكم (mufradat)
- **B007** başkasının yerini ve işlevini alma [kalıp] — onun yerine geçti veya adına görev yaptı
  القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)؛ قام فلان مقام فلان إذا ناب عنه؛ يقومان مقامهما (mufradat)؛ أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك (maqayis)
- **B008** düzgünlük, denge ve doğru yoldan sapmama — düzgün ve dengeli olmak; doğru yoldan ayrılmamak · düzgün, dengeli ve doğru
  رمح قويم ورجل قويم؛ القيمة الملة المستقيمة؛ إذا انقاد واستمرت طريقته فقد استقام (ayn)؛ الاستقامة الاعتدال؛ استقام له الأمر؛ قومت الشيء فهو قويم أي مستقيم؛ القوام العدل؛ دينا قيما (sihah)؛ الاستقامة على الطاعة؛ القيم هو المستقيم؛ أقوم كلاما أي أعدل كلاما (tahdhib)؛ الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم؛ دينا قيما أي ثابتا (mufradat)
- **B009** ayakta tutan dayanak ve geçim temeli — bir şeyi ayakta tutan dayanak, düzen ve geçim temeli
  هذا الأمر لا قومية له أي لا قوام له؛ القوام من العيش ما يقيمك ويغنيك؛ القيام العماد؛ قوام كل شيء ما استقام به (ayn)؛ قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه؛ جعل الله لكم قياما (sihah)؛ قوام الأمر وملاكه؛ تقيمكم فتقومون بها؛ قوام الجسم تمامه؛ قوام كل شيء ما استقام به (tahdhib)؛ القيام والقوام اسم لما يقوم به الشيء؛ جعلها مما يمسككم؛ قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم (mufradat)؛ قوام الدين والحق أي به يقوم (maqayis)
- **B010** değer biçme ve belirlenen bedel — değer biçmeyle belirlenen bedel · malın değerini belirlemek veya ulaştığı bedeli bildirmek
  القيمة ثمن الشيء بالتقويم؛ تقاوموا فيما بينهم (ayn)؛ قومت السلعة؛ استقمت السلعة؛ القيمة واحدة القيم (sihah)؛ القيمة ثمن الشيء بالتقويم؛ تقاوموه فيما بينهم؛ استقمت المتاع أي قومته؛ قامت الأمة مائة دينار أي بلغت قيمتها (tahdhib)؛ تقويم السلعة بيان قيمتها (mufradat)؛ قومت الشيء تقويما؛ أصل القيمة الواو (maqayis)
- **B011** insanın boyu ve düzgün beden yapısı — insanın boyu ve beden uzunluğu · düzgün ve güzel boy; beden yapısı
  القامة مقدار قيام الرجل؛ قوام الجسم تمامه وطوله (ayn)؛ قوام الرجل قامته وحسن طوله؛ قامة الإنسان قده (sihah)؛ القامة قامة الرجل؛ حسن القامة والقمة والقومية؛ قوام الجسم تمامه (tahdhib)؛ تقويم الإنسان في أحسن تقويم؛ انتصاب القامة (mufradat)؛ القوام الطول الحسن؛ القومية القوام والقامة (maqayis)
- **B012** düzeneğin dik, taşıyıcı veya tutulan parçası — kuyu makarası veya ona bağlı donanım · kuyu başındaki insan biçimli yapı diye aktarılmış, fakat yanlış sayılmış yorum · kılıç sapı veya yatak, masa ve hayvanın dik duran parçası · çiftçinin elinde tuttuğu ahşap parça
  القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر؛ قائم السيف مقبضه؛ قائمة السرير والخوان والدابة (ayn)؛ القامة البكرة بأداتها؛ قائم السيف وقائمته مقبضه؛ القائمة واحدة قوائم الدواب؛ المقوم الخشبة التي يمسكها الحراث (sihah)؛ القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة؛ قائم السيف مقبضه وما سوى ذلك فهو قائمة (tahdhib)؛ القامة البكرة بأداتها (maqayis)
- **B013** ölülerin diriltildiği ve insanların yargı için kalktığı gün — ölülerin diriltildiği ve insanların yargı için ayağa kalktığı son gün
  القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)؛ يوم القيامة معروف (sihah)؛ القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم (tahdhib)؛ القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين (mufradat)
- **B014** karşılıklı direnip mücadele etme [kalıp] — ona karşı durup mücadele etmek; tarafların birbirine karşı koyması
  قاومته في كذا أي نازلته (ayn)؛ قاومه في المصارعة وغيرها؛ تقاوموا في الحرب أي قام بعضهم لبعض (sihah)؛ ما زلت أقاوم فلانا في هذا الأمر أي أنازله (tahdhib)
- **B015** tam ve denk ağırlıktaki para — ölçün ağırlığa tam denk gelen, ağır basmayan para
  دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)؛ دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح (tahdhib)
- **B016** donup akmama veya yorulup ilerleyememe [kalıp] — su dondu veya akmaz halde kaldı · binek hayvanı durdu veya yorulup yürüyemedi
  قام الماء جمد؛ قامت الدابة وقفت (sihah)؛ قامت لفلان دابته إذا كلت أو عيت فلم تسر (tahdhib)
- **B017** güneşin tam tepede olduğu öğle ortası — güneşin ortada, günün iki yarısının dengede olduğu öğle vakti
  قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn;tahdhib)؛ قام ميزان النهار إذا انتصف؛ قام ميزان النهار فاعتدل (tahdhib)
- **B018** pazarın canlanıp satışların artması [kalıp] — pazar canlandı ve mallar alıcı buldu
  قامت السوق نفقت (sihah)؛ قامت السوق إذا نفقت ونامت إذا كسدت (tahdhib)
- **B019** bir beden bölümünün kişiye ağrı vermesi [kalıp] — sırtım veya gözlerim ağrıdı
  قام بي ظهري أي أوجعني؛ قامت بي عيناي؛ كل ما أوجعك من جسدك فقد قام بك (tahdhib)
- **B020** koyunun bacaklarını tutan hastalık — koyunun bacaklarını tutup onu ayağa kaldıran hastalık
  القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)؛ أخذها قوام وهو داء يأخذها في قوائمها تقوم منه (tahdhib)
- **B021** göz bebeği sağlamken görme yetisinin kaybolması — göz bebeği sağlam kaldığı halde görmeyen göz
  عين قائمة ذهب بصرها والحدقة صحيحة (ayn)؛ العين القائمة أن يذهب بصرها والحدقة صحيحة (tahdhib)

## ك ب ر (root_001281): 42:13 كَبُرَ, 42:22 ٱلْكَبِيرُ, 42:37 كَبَٰٓئِرَ

- **B001** küçüğün karşıtı olan büyüklük — büyük · pek büyük · daha büyük veya en büyük
  أصل صحيح يدل على خلاف الصغر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ الكبر ضد الصغر (jamhara)؛ كبر بالضم يكبر أي عظم فهو كبير وكبار (sihah)؛ الكبير والصغير من الأسماء المتضايفة (mufradat)
- **B002** bir işin ana payı ve başlıca yükü — işin büyük bölümü veya ağır yükü · onun işinin en önemli bölümü
  والكبر معظم الأمر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ كبر الشيء معظمه (jamhara)؛ كبر الشيء أيضا معظمه (sihah)؛ كبر الشيء معظمه بالكسر (tahdhib)؛ والذي تولى كبره إشارة إلى من أوقع حديث الإفك (mufradat)
- **B003** gözünde büyütüp hayrete düşmek — onu gözünde büyüttü ve ona hayret etti · onu gözlerinde büyüttüler
  أكبرت الشيء استعظمته (maqayis)؛ أكبرت الشيء أكبره إكبارا إذا عظم في صدرك وعجبت منه (jamhara)؛ أكبرت الشيء استعظمته (sihah)؛ أكبرنه أعظمنه (tahdhib)؛ أكبرت الشيء رأيته كبيرا (mufradat)
- **B004** yaşlanma ve zamanla eskime — adam yaşlandı · yaşlılık veya eskilik hali
  ومن الباب الكبر وهو الهرم (maqayis)؛ الكبرة السن يقال علته كبرة (ayn)؛ بلغ فلان الكبر في السن (jamhara)؛ الكبر في السن وقد كبر الرجل أي أسن (sihah)؛ الكبر مصدر الكبير في السن من الناس والدواب (tahdhib)؛ يقال فلان كبير أي مسن (mufradat)؛ السهم والنصل العتيق الذي أفسده الوسخ قد علته كبرة (ayn)؛ للسيف والنصل العتيق الذي قدم علته كبرة (tahdhib)
- **B005** saygınlık ve önderlikte yüksek konum — kuşaktan kuşağa soylu ve saygın biçimde · onların başı veya en bilgilisi · sizin öğreticiniz veya başınız · önder veya en büyük ata
  الرفعة في الشرف (ayn)؛ ورثوا المجد كابرا عن كابر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ كبيرهم أعلمهم كأنه كان رئيسهم (tahdhib)؛ إنه لكبيركم أي رئيسكم (mufradat)؛ الكابر السيد والكابر الجد الأكبر (tahdhib)
- **B006** ululuk ve kendini üstün görme — büyüklük taslama ve kendini üstün görme · ululuk ve boyun eğmeme; Tanrı'ya özgü yücelik · büyüklendi ve kendini üstün gösterdi · gerçeği inatla reddedip büyüklük tasladı
  الكبر العظمة وكذلك الكبرياء (maqayis)؛ الكبرياء اسم للتكبر والعظمة (ayn)؛ تكبر إذا تعظم (jamhara)؛ الكبر بالكسر العظمة وكذلك الكبرياء (sihah)؛ يتكبرون أي يرون أنهم أفضل الخلق (tahdhib)؛ الكبر الحالة التي يتخصص بها الإنسان من إعجابه بنفسه (mufradat)
- **B007** ağır cezalık büyük günah — ağır cezalık büyük günah · ağır cezalık büyük günahlar
  الكبر الإثم الكبير من الكبيرة (ayn)؛ الكبيرة من الذنوب والجمع كبائر (jamhara)؛ كبيرة من الكبائر يعني الذنوب (ayn)؛ الكبيرة متعارفة في كل ذنب تعظم عقوبته (mufradat)؛ إثم كبير (mufradat)
- **B008** soy yakınlığı veya aile içi doğum sırası — soyda en yakın olan veya en büyük evlat · babasının son çocuğu; başka aktarımda en büyük çocuğu
  الولاء للكبر يراد به أقعد القوم في النسب (maqayis)؛ الكبر أكبر ولد الرجل (ayn)؛ فلان كبرة ولد أبويه إذا كان آخرهم (sihah)؛ كبرة ولد أبيه بمعنى عجزة أي آخرهم (tahdhib)؛ هو صغرة ولد أبيه وكبرتهم أي أكبرهم (tahdhib)
- **B009** Tanrı'yı en büyük diye yüceltme — Tanrı'yı en büyük diye yüceltme · Tanrı en büyüktür
  التكبير في الصلاة وغيرها تفعيل من قولهم الله أكبر (jamhara)؛ التكبير التعظيم (sihah)؛ قول المصلي الله أكبر وكذلك قول المؤذن (tahdhib)؛ التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر (mufradat)
- **B010** bir işin birine ağır ve güç gelmesi [kalıp] — bize çok ağır ve güç geldi
  إذا أردت الأمر العظيم قلت كبر علينا كبارة (ayn)؛ فإذا أردت الأمر العظيم قلت كبر علينا كبارة (sihah)؛ كبر الأمر يكبر كبارة (tahdhib)؛ تستعمل الكبيرة فيما يشق ويصعب (mufradat)؛ كبر على المشركين ما تدعوهم إليه (mufradat)
- **B011** üstünlük yarışına girip yenmek [kalıp] — benimle üstünlük yarışına girdi, ben de onu yendim
  كابرني فكبرته أي غلبته (ayn)
- **B012** tek yüzlü davul — tek yüzlü davul
  الكبر طبل له وجه (ayn)؛ الكبر الطبل الذي له وجه واحد (tahdhib)؛ الكبر الطبل وجمعه كبار (tahdhib)
- **B013** günün yükseldiği vakit [kalıp] — günün yükseldiği vakit
  أكبر النهار وشباب النهار أي حين ارتفع النهار (tahdhib)

## ش ر ك (root_000791): 42:13 ٱلْمُشْرِكِينَ, 42:21 شُرَكَٰٓؤُا۟

- **B001** ortaklık ve ortak olma — ortaklık ve ortak olma · ortak · ortak olmak veya birini ortak etmek · karşılıklı olarak ortaklaşmak · herkesin ortak olduğu veya eşit yararlandığı şey · ortaklık payı
  الشركة أن يكون الشيء بين اثنين لا ينفرد به أحدهما (maqayis)؛ الشركة مخالطة الشريكين (ayn;tahdhib)؛ شاركت فلانا صرت شريكه (sihah)؛ شركه في الأمر إذا دخل معه فيه (tahdhib)؛ خلط الملكين أو شيء لاثنين فصاعدا (mufradat)
- **B002** Tanrı'ya ortak koşma — Tanrı'ya ortak koşma · Tanrı'ya ortak koşmak · Tanrı'ya ortak koşan kimse · büyük ve küçük ortak koşma türleri
  الشرك ظلم عظيم (ayn)؛ الشرك أيضا الكفر (sihah)؛ أن تجعل لله شريكا في ربوبيته (tahdhib)؛ إثبات شريك لله تعالى (mufradat)
- **B003** eş veya evlilik yoluyla hısım — eş veya evlilik yoluyla hısım · sizinle evlilik yoluyla hısım olmak istedik
  في المصاهرة رغبنا في شرككم وصهركم (ayn;tahdhib)؛ فلان شريك فلان إذا تزوج بابنته أو بأخته (tahdhib)؛ امرأة الرجل شريكته (tahdhib)
- **B004** sandal kayışı ve sandala kayış takma — sandal kayışı · sandala kayış takmak
  شراك النعل مشبه بهذا (maqayis)؛ الشراك سير النعل (ayn;tahdhib)؛ أشركت نعلي جعلت لها شراكا (sihah)؛ شركت النعل وأشركتها إذا جعلت لها شراكا (tahdhib)
- **B005** yolun ana yatağı, izleri ve küçük kolları — yolun ana yatağı, ortası veya izleri · ana yoldan ayrılan küçük yollar · otlağın yollar veya izler halinde uzanması
  الشرك لقم الطريق وهو شراكه (maqayis)؛ الشرك أخاديد الطريق الواضح (ayn)؛ الشركة معظم الطريق ووسطه (sihah)؛ شرك الطريق أنساع الطريق (tahdhib)؛ أم الطريق معظمه وبنياته أشراك صغار (tahdhib)
- **B006** avın dolandığı kapan ve tuzak benzetmesi — avın dolandığı av kapanı · tek bir av kapanı · dünyanın tuzağı
  شرك الصائد سمي بذلك لامتداده (maqayis)؛ الشرك حبالة يرتبك فيها الصيد (ayn)؛ الشرك بالتحريك حبالة الصائد (sihah)؛ شرك الصائد حبالته يرتبك فيها الصيد (tahdhib)؛ شرك الدنيا أي حبالتها (mufradat)
- **B007** özel yapılarda hızlı ve art arda oluş — hızlı ve art arda tokatlar · suya birbiri ardından geliş
  لطمه لطما شركيا أي سريعا متتابعا (sihah)؛ لطمه لطما شركيا أي متتابعا (tahdhib)؛ ورد بعد ورد متتابع (sihah)
- **B008** kaygılı iç konuşma veya bölünmüş görüş — kaygılı biçimde kendi kendine konuşan · görüşü tek olmayan veya bölünmüş
  رأيت فلانا مشتركا إذا كان يحدث نفسه كالمهموم (sihah;tahdhib)؛ رأيه مشترك ليس بواحد (tahdhib)

## د ع و (root_000478): 42:13 تَدْعُوهُمْ, 42:15 فَٱدْعُ

- **B001** seslenerek kendine yöneltme — seslenmek; çağırmak · yemeğe çağırma · belirtilen yeri amaçlayıp oraya gitmek
  أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك؛ دعوت أدعو دعاء؛ الدعوة إلى الطعام بالفتح؛ دعا فلانا مكان كذا إذا قصد ذلك المكان كأن المكان دعاه
- **B002** hak veya aidiyet ileri sürme — soy bağı ileri sürme · kendisi veya başkası adına hak iddia etme · savaşta soyunu söyleyerek kendini tanıtma · öz babasından başkasına bağlanan kişi
  الادعاء أن تدعي حقا لك أو لغيرك (maqayis)؛ الادعاء في الحرب الاعتزاء (maqayis)؛ الدعوة ادعاء الولد الدعي غير أبيه ويدعيه غير أبيه (ayn)؛ الدعوة في النسب بالكسر (maqayis)
- **B003** sütün devamını çekmek için memede bırakılan pay [kalıp] — sonraki sütü çekmek için memede bırakılan süt payı
  داعية اللبن ما يترك في الضرع ليدعو ما بعده
- **B004** Tanrı'nın birine istemediği bir sıkıntıyı vermesi [kalıp] — Tanrı'nın birinin başına hoşlanmadığı bir sıkıntıyı getirmesi
  دعا الله فلانا بما يكره أي أنزل به ذلك
- **B005** birbiri ardından çökme veya yıkma — duvarların birbiri ardından çökmesi · yapıları üzerlerine birbiri ardından yıkmak
  تداعت الحيطان وذلك إذا سقط واحد وآخر بعده؛ داعيناها عليهم إذا هدمناها واحدا بعد آخر
- **B006** dönemin olaylara yön veren değişimleri [kalıp] — dönemin değişimleri ve getirdiği olaylar
  دواعي الدهر صروفه كأنها تميل الحوادث
- **B007** gizli cevabı buldurmaya yönelik bilmeceleşme — gizli cevabı buldurmak için karşılıklı sorulan bilmeceler · sana bir bilmece sorayım
  لبنى فلان أدعية يتداعون بها وهي مثل الأغلوطة كأنه يدعو المسؤول إلى إخراج ما يعميه عليه
- **B008** evde hiç kimsenin bulunmaması — evde hiç kimse yok
  ما بالدار دَعْوِيّ أي ما بها أحد كأنه ليس بها صائح يدعو بصياحه

## ECHO د ع ع (root_000477): for 42:13 تَدْعُوهُمْ, 42:15 فَٱدْعُ: withheld observed target; not identity

- **B001** itme — sert ve kaba itme · sertçe itmek · yetimi itip azarlamak · ateşe doğru zorla sürmek
  الدَّعّ الدفع (maqayis;tahdhib)؛ دَعَعته أدَعُّه دَعًّا أي دفعته (sihah)؛ دفع في جفوة (ayn)؛ الدفع الشديد (mufradat)
- **B002** sallayarak doldurma — kabı sallayarak doldurma · bir şeyi doldurmak veya hareket ettirerek sıkıştırmak · ağzına kadar dolu büyük çanak · selin vadiyi doldurması
  الدعدعة تحريك المكيال ليستوعب الشيء (maqayis)؛ دعدعت الشيء ملأته وجفنة مدعدعة (sihah)؛ دعدع مكيالا أو جوالقا حتى يكتنز (tahdhib)
- **B003** hayvanı seslenerek yönlendirme — küçükbaş hayvanı seslenerek çağırma veya azarlama · keçilere seslenip onları yönlendirmek · çobanın keçileri yönlendirmek için çıkardığı geleneksel çağrı
  الدعدعة زجر الغنم (maqayis)؛ للمعز خاصة دعدعت بها إذا دعوتها (sihah)؛ يقول الراعي للمعزى داع داع وهو زجر لها (tahdhib)
- **B004** tökezleyeni ayağa kalkmaya çağırma — tökezleyene söylenen 'kalk, toparlan' sözü
  قولك للعاثر دع دع (maqayis)؛ أن تقول للعاثر دع دع أي قم فانتعش (sihah;tahdhib)؛ أصله أن يقال للعاثر دع دع (mufradat)
- **B005** kıvrılarak yavaş koşma — kıvrıla kıvrıla yavaş koşma
  الدعدعة عدو في التواء (maqayis)؛ عدا عدوا فيه بطء والتواء (sihah)؛ عدو في التواء وبطء (tahdhib)
- **B006** kısa boylu adam — 
  دعداع فإن صح فهو من الإبدال من دحداح (maqayis)؛ الدعداع والدحداح الرجل القصير (tahdhib)
- **B007** iki hurma arasındaki açıklık veya seyrek hurmalar — 
  الدعاع ما بين النخلتين؛ الدعاع النخل المتفرق؛ رواه بعضهم في ذعاع النخل بالذال
- **B008** yazın su barındıran, sığırların yediği bitki — yazın su tutan ve sığırların yediği bir bitki
  الدعدع نبت يكون فيه ماء في الصيف يأكله البقر
- **B009** küçük çocuklar ve bakmakla yükümlü olunan küçükler — bir erkeğin küçük çocukları ve bakımına bağlı küçükler · bakımına bağlı küçüklerin sayısı çoğalmak
  الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه
- **B010** yabani bitki tohumu — yabani bir bitkinin tohumu · kuraklıkta yenen siyah tohum; ona benzeyen siyah karınca · bu tohumu ve başka bir yabani tohumu yemek için toplayan adam
  الدعاع حب شجرة برية؛ الدعاعة حبة سوداء؛ نملة سوداء تشاكل هذه الحبة؛ رجل دعاع فثاث

## ج ب ي (root_000220): 42:13 يَجْتَبِىٓ (also echo for 42:16 ٱسْتُجِيبَ, 42:26 وَيَسْتَجِيبُ, 42:38 ٱسْتَجَابُوا۟, 42:47 ٱسْتَجِيبُوا۟)

- **B001** bir şeyi toplayıp elde etmek — bir şeyi kendisi için ya da bir yerde toplayıp elde etmek · vergiyi toplayıp almak · suyu su teknesinde toplamak
  جبيت الخراج جباية أي جمعته وحصلته (ayn)؛ جبيت الخراج جباية وجبوته جباوة (sihah)؛ جبيت الشيء إذا حصلته لنفسك؛ جباية الخراج جمعه وتحصيله (tahdhib)؛ جبيت الماء في الحوض جمعته؛ جبيت الخراج جباية؛ يجبى إليه ثمرات كل شيء (mufradat)؛ أصل واحد يدل على جمع الشيء والتجمع؛ جبيت المال أجبيه جباية (maqayis_v4+maqayis_v5)
- **B002** birikmiş su veya büyük su teknesi — su teknesinde ya da başka bir yerde birikmiş su · su teknesinde birikmiş su · hayvanların su içtiği geniş ve büyük su teknesi · büyük su tekneleri · su teknesinde biriken bir miktar su
  الجبى ما جمع في الحوض من الماء؛ الجابية حوض ضخم واسع (ayn)؛ الجبى الماء المجموع في الحوض؛ الجابية الحوض الذي يجبى فيه الماء؛ الجمع الجوابي (sihah)؛ الجبى ما جمع في الحوض من الماء؛ الجبى جمع جبية (tahdhib)؛ الحوض الجامع له جابية وجمعها جواب (mufradat)؛ الحوض نفسه جابية؛ الجبا بكسر الجيم ما جمع من الماء في الحوض أو غيره (maqayis_v4+maqayis_v5)
- **B003** kuyu çukuru veya çevresindeki kazı toprağı — kuyu çukuru, kuyu çevresindeki kazı toprağı veya su teknesinin çevresi
  الجبى محفر البئر؛ نثيلة البئر وهي ترابها الذي حولها (ayn)؛ الجبا بالفتح مقصور نثيلة البئر وهي ترابها الذي حولها (sihah)؛ الجبا مقصور ما حول البئر؛ الجبى ما حول الحوض يكتب بالياء (tahdhib)؛ الجبا مقصور ما حول البئر (maqayis_v4+maqayis_v5)
- **B004** seçip kendine yaklaştırmak — seçmek, özel bir yere ayırmak ve yakına getirmek · Yaratıcının bir kulunu seçip özel iyiliklere ayırması
  اجتبى الرجل الرجل إذا قربه (ayn)؛ اجتباه أي اصطفاه (sihah)؛ اختار لك الشيء واجتباه؛ يجتبيك ربك معناه يختارك ويصطفيك (tahdhib)؛ الاجتباء الجمع على طريق الاصطفاء؛ اجتباء الله العبد تخصيصه إياه (mufradat)
- **B005** onu kendin derleyip uydursaydın ya — Onu kendin derleyip uydursaydın ya!
  لولا اجتبيتها معناه هلا اختلقتها وافتعلتها من قبل نفسك (tahdhib)؛ هلا جمعتها تعريضا منهم بأنك تخترع هذه الآيات وليست من الله (mufradat)
- **B006** öne eğilmek veya diz çöküp yere kapanmak — öne eğilmiş duruş veya diz çöküp yüzüstü kapanma · bedenini toplayarak yere kapanmak
  التجبية ركوع كركوع المصلي؛ التجبية أن يجبي الرجل على وجهه باركا (ayn)؛ التجبية أن يقوم الإنسان قيام الراكع؛ أن يضع يديه على ركبتيه وهو قائم؛ أن ينكب على وجهه باركا (sihah)؛ جبى يجبي إذا سجد وهو تجمع (maqayis_v4+maqayis_v5)
- **B007** ürünü olgunlaşmadan alıp satmak — ekini veya tarla ürününü olgunluğu belli olmadan alıp satma · Ürünü olgunlaşmadan satan, yasak kazanca girmiş olur.
  الإجباء بيع الزرع قبل أن يبدو صلاحه؛ من أجبى فقد أربى؛ أصله الهمز (sihah)؛ الإجباء بيع الحرث قبل صلاحه؛ من أجبى فقد أربى (tahdhib)؛ أجبأت إذا اشتريت زرعا قبل بدو صلاحه؛ بعضهم يقوله بلا همز؛ من أجبى فقد أربى (maqayis_v4)

## ه د ي (root_001583): 42:13 وَيَهْدِىٓ, 42:52 نَّهْدِى, 42:52 لَتَهْدِىٓ

- **B001** doğru yolu gösterme ve doğruya yönelme — doğru yol, doğruyu gösterme ve açıklama · ona yolu gösterip tanıttım · doğru yolu kabul edip buldu · yol gösteren, doğruya çağıran kimse
  الهدى نقيض الضلالة؛ هدي فاهتدى (ayn;tahdhib)؛ الهدى الرشاد والدلالة؛ هداه الله للدين هدى؛ أولم يبين لهم؛ هديته الطريق والبيت هداية أي عرفته (sihah)؛ الهدى البيان وإخراج شيء إلى شيء والطاعة والورع؛ دله على الطريق (tahdhib)؛ الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق (mufradat)؛ التقدم للإرشاد؛ هديته الطريق هداية؛ الهدى خلاف الضلالة (maqayis)
- **B002** yön, izlenen yol ve tutum — işin yönü, doğrultusu ve amacı · bir kimsenin gidişi, tutumu ve yöntemi · onun benzeri veya onu yeniden yapma
  خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه؛ هدية أمره وسيرته؛ هدى هدي فلان أي سار سيرته (sihah)؛ هدية أمره أي جهة أمره؛ هديت به أي قصدت به؛ هديه أي سمته؛ ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة؛ هدياها أي مثلها أو أعاودك (tahdhib)؛ هدية فلان وهديه أي طريقته (mufradat)؛ نظر فلان هدي أمره أي جهته؛ ما أحسن هديته أي هديه؛ رميت بآخر هدياه أي قصده (maqayis)
- **B003** bir şeyin ilk veya öndeki bölümü — bir şeyin ilki veya öndeki bölümü · atların boyunları ya da ilk sırası; yaban hayvanlarının öncüleri · okun ucu ve koyunun boynu
  الهادي من كل شيء أوله؛ هوادي الخيل أعناقها أو أول رعيل؛ العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه (ayn)؛ هادي السهم نصله؛ الهادي العنق؛ هوادي الخيل أعناقها أو أول رعيل؛ الهاديات أوائل الوحش (sihah)؛ الهادية من كل شيء أوله وما تقدم منه؛ هادية الشاة الرقبة؛ هوادي الخيل أعناقها أو أول رعيل؛ هاديات الوحش أوائلها (tahdhib)؛ هوادي الوحش متقدماتها الهادية لغيرها (mufradat)؛ كل متقدم لذلك هاد؛ هوادي الخيل أعناقها؛ هاديها أول رعيل؛ الهادية العصا لأنها تتقدم ممسكها (maqayis)
- **B004** incelik göstergesi armağan verme — yakınlık ve incelik göstergesi armağan · armağan gönderdi veya verdi · karşılıklı armağanlaşma · armağanın sunulduğu tabak · sık sık armağan veren kimse
  الهدية ما أهديت إلى ذي مودة من بر (ayn)؛ الهدية واحدة الهدايا؛ أهديت له وإليه؛ المهدى ما يهدى فيه؛ التهادي أن يهدي بعضهم إلى بعض؛ المهداء الذي من عادته أن يهدي (sihah)؛ أهديت الهدية إهداء؛ امرأة مهداء؛ المهدى الطبق الذي يهدى عليه (tahdhib)؛ الهدية مختصة باللطف؛ المهدى الطبق؛ المهداء من يكثر إهداء الهدية (mufradat)؛ الهدية ما أهديت من لطف إلى ذي مودة؛ المهدي الطبق تهدى عليه (maqayis)
- **B005** kutsal yere adanan hayvan, mal veya eşya — kutsal bölgeye adanan hayvan, mal veya eşya · adanmış sunu adından genişleyen deve adı
  الهدي والهدي ما أهديت إلى مكة؛ كل شيء تهديه من مال أو متاع فهو هدي (ayn)؛ الهدي ما يهدى إلى الحرم من النعم؛ مالى هدي؛ حتى يبلغ الهدى محله (sihah)؛ أهديت الهدي إلى بيت الله؛ الهدي خفيف وعليه هدية أي بدنة؛ ما يهدى إلى مكة من النعم وغيره من مال أو متاع؛ العرب تسمي الإبل هديا (tahdhib)؛ الهدي مختص بما يهدى إلى البيت؛ فما استيسر من الهدي؛ هديا بالغ الكعبة (mufradat)؛ الهدي والهدي ما أهدي من النعم إلى الحرم قربة إلى الله تعالى (maqayis)
- **B006** gelini eşinin yanına götürme — gelini eşinin yanına götürdü · gelinin eşinin yanına götürülmesi · eşine götürülen gelin
  الهداء مصدر قولك هديت المرأة إلى زوجها؛ وهي مهدية وهدي (sihah)؛ هديت العروس فأنا أهديها هداء؛ أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها (tahdhib)؛ الهدي يقال في العروس؛ هديت العروس إلى زوجها (mufradat)؛ الهدى العروس وقد هديت إلى بعلها هداء (maqayis)
- **B007** dokunulmaz sığınmacı; kimi açıklamalarda tutsak — dokunulmaz sığınmacı; kimi açıklamalarda tutsak
  الرجل الذي له حرمة كحرمة هدي البيت؛ يقال للأسير أيضا هدي (sihah)؛ الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا؛ يقال للأسير أيضا الهدي (tahdhib)؛ وقيل الهدي الأسير (maqayis)
- **B008** sallanarak, gerektiğinde başkalarına dayanarak yürüme — güçsüzlükten iki kişiye dayanarak yürümek · yürürken sağa sola sallandı
  التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)؛ يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله؛ المرأة إذا تمايلت في مشيتها قيل تهادى (sihah)؛ يهادى بين اثنين معناه يعتمد عليهما من ضعفه وتمايله؛ هي تهادى إذا تمايلت في مشيها (tahdhib)؛ يهادي بين اثنين إذا مشى بينهما معتمدا عليهما؛ تهادت المرأة إذا مشت مشي الهدي (mufradat)؛ جاء فلان يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما (maqayis)
- **B009** bön, güçsüz ve ağır kimse — bön, güçsüz, ağır ve uyuşuk adam
  الهداء الرجل البليد الضعيف (ayn)؛ رجل هداء وهدان للثقيل الوخم (tahdhib)
- **B010** sakin, ölçülü ve düzgün ilerleyiş — sakinlik ve güzel, telaşsız tutum
  الهدي السكون؛ ما هدى هدي مهزوم؛ لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن (ayn)؛ الهدي السكون؛ لم يسرع إسراع المنهزم ولكن على سكون وحسن هدي (tahdhib)
- **B011** övgü veya yergi şiiri sunma ve şiirle yergileşme — birine övgü veya yergi şiiri sunma · şiirle karşılıklı yergileşme
  الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)؛ هاداني فلان الشعر وهاديته أي هاجاني وهاجيته (tahdhib)

## ECHO ه د د (root_001580): for 42:13 وَيَهْدِىٓ, 42:52 نَّهْدِى, 42:52 لَتَهْدِىٓ: withheld observed target; not identity

- **B001** agir kirip yikma — kirip yikmak, sarsip bozmak · agir yikim ve kirilma · kirilip yikilmak · bir felaketin kisiyi sarsip gucunu kirmasi · yer cokmesi ya da yikima benzer agir olay
  أصل صحيح يدل على كسر وهضم وهدم (maqayis)؛ الهد الهدم الشديد (ayn;tahdhib)؛ هددت الحائط إذا هدمته (jamhara)؛ هد البناء يهده هدا كسره وضعضعه (sihah;tahdhib)؛ انهد الجبل أي انكسر (sihah)؛ الهدة الخسوف والهد الهدم (tahdhib)؛ هد ركني إذا بلغ منه وكسره (tahdhib)
- **B002** zayif ve korkak kisi — zayif veya korkak adam · korkak veya zayif adam · korkak adam · korkak topluluk · birini zayif saymak · zayif olmayan
  الهد من الرجال الضعيف كأنه هد (maqayis)؛ رجل هد جبان (jamhara)؛ رجل هد وأهد بمعنى الجبن والضعف (jamhara)؛ الهد الرجل الضعيف (sihah;tahdhib)؛ الهد بالكسر الجبان الضعيف (sihah;tahdhib)؛ استهددت فلانا أي استضعفته (tahdhib)
- **B003** cömert ve guclu kisi — cömert, degerli veya guclu adam · adam gucu ve dayanikliligiyla ovulmek · adami dayanikli diye ovmek
  الهد من الرجال الجواد الكريم (maqayis;tahdhib)؛ الهد الكريم الهاد لماله (maqayis)؛ فلان يهد إذا أثني عليه بالجلد والقوة (sihah)؛ لهد الرجل إذا أثني عليه بالجلد والشدة (tahdhib)؛ هد الرجل جلد الرجل (tahdhib)
- **B004** siddetli ugultu — duvar, kose veya dag dusmesinin siddetli sesi · deniz tarafindan duyulan siddetli ugultu · gok gurultusu · ses ve ugultu · kumru veya erkek devenin gurleyis ugultusu
  الهدة صوت وقع الحائط (maqayis;sihah)؛ الهدة صوت تسمعه من سقوط ركن أو ناحية جبل (ayn;tahdhib)؛ الهاد صوت شديد يسمعه أهل السواحل (ayn;sihah;tahdhib)؛ ما سمعنا العام هادة أي رعدا (jamhara)؛ هدهد الحمام صوت (maqayis)؛ الفحل يهدهد في هديره (ayn;sihah;tahdhib)؛ الهديد والغديد الصوت (tahdhib)
- **B005** ibibik kusu — ibibik kusu · ibibik veya guvercine benzetilen kus adlari
  الهدهد معروف (maqayis;tahdhib)؛ الهدهد طائر والهداهد مثله (sihah)؛ الهداهد طائر يشبه الحمام (tahdhib)؛ هداهد تصغير هدهد (tahdhib)
- **B006** uyutmak icin sallama [kalıp] — cocugu uyusun diye sallamak
  هدهدت المرأة ابنها حركته لينام (maqayis;sihah)؛ الهدهدة تحريك الأم ولدها لينام (tahdhib)؛ يهدهد الصبي (tahdhib)
- **B007** ovgu yeterlik kalibi — bir erkegi 'ona diyecek yok' anlaminda oven kalip
  مررت برجل هدك من رجل كقولهم حسبك من رجل (maqayis)؛ هدك فلان من رجل أي حسبك به (jamhara)؛ مررت برجل هدك من رجل معناه أثقلك وصف محاسنه (sihah)؛ مررت برجل هدك من رجل فهو بمعنى حسبك وهو مدح (tahdhib)
- **B008** agir basarak yurume [kalıp] — yururken yere cok sert basmak
  فلان يهد الأرض في مشيه إذا جاء يطأ وطأ شديدا (jamhara)
- **B009** sarp inisli gecit — sarp inisli tepe veya zorlu gecit
  أكمة هدود صعبة المنحدر وربما تردت الإبل منها (jamhara)؛ الهدود العقبة الشاقة (tahdhib)
- **B010** gozdagi vererek korkutma — gozdagi verme ve korkutma · korkutma ve gozdagi verme · gozdagi verme · uzaktan savrulan gozdagi
  التهديد التخويف وكذلك التهدد (sihah)؛ التهدد والتهديد والتهداد من الوعيد (tahdhib)؛ يقال للوعيد من وراء وراء الفديد والهديد (tahdhib)
- **B011** kesinlesmemis sani [kalıp] — kisinin icine kesinlesmemis bir sani gibi belirmek
  يقال يهدهد إلي كذا إذا شبه للإنسان في نفسه بالظن ما لم يثبته ولم يعقد عليه التشبيه (tahdhib)
- **B012** uzun boylu adam — uzun boylu adam
  الهديد الرجل الطويل (tahdhib)

## ب ع د (root_000131): 42:14 بَعْدِ, 42:14 بَعْدِهِمْ, 42:16 بَعْدِ, 42:18 بَعِيدٍ, 42:28 بَعْدِ, 42:41 بَعْدَ, 42:44 بَعْدِهِۦ

- **B001** uzak olma — yerde veya anlamda uzaklik · uzak, yakin olmayan · uzak yer veya uzak akrabalik · uzak saymak ya da uzaklasmak
  البعد خلاف القرب (maqayis;sihah;mufradat)؛ بعد يبعد بعدا فهو بعيد (ayn;jamhara;tahdhib)؛ يقال ذلك في المحسوس وفي المعقول (mufradat)؛ بيننا بعدة من الأرض والقرابة (sihah)
- **B002** sonra gelme — sonra, oncekinin ardindan gelen · sonradan, ondan sonra · bundan sonra soz gecisi
  بعد ضد قبل (ayn;jamhara;sihah)؛ من بعد كما تقول في خلافه من قبل (maqayis)؛ بعد كلمة دالة على الشيء الأخير (tahdhib)؛ وما خلف بعقبه فهو من بعده (ayn)؛ يقال في مقابلة قبل (mufradat)
- **B003** uzaklastirma — uzaklastirmak veya arayi acmak · uzaklastirmak, kovmak ya da uzaklara gitmek · uzaklastirma, karsilikli uzak durma
  باعدته مباعدة وأبعده الله نحاه عن الخير وباعد الله بينهما (ayn)؛ والبعاد مصدر باعدته مباعدة وبعادا (jamhara)؛ وأبعده غيره وباعده وبعده تبعيدا (sihah)؛ باعد بين أسفارنا (ayn;tahdhib)؛ أبعد فلان في الأرض إذا أمعن فيها (tahdhib)
- **B004** yikim bedduasi — yok olmak ya da beddua anlamina gelmek · kahrolsun, yok olup gitsin · onu iyilikten uzak kilsin diye beddua etmek · hain veya dislanmis kotu kisi
  البعد والبعد الهلاك (maqayis;sihah)؛ بعدت ثمود أي هلكت (maqayis;mufradat)؛ بعدا وسحقا (ayn;tahdhib)؛ أبعده الله أي لا يرثى له (tahdhib)؛ بعد يبعد بعدا من قولهم أبعده الله (jamhara)
- **B005** uzak yakinlar — uzak akrabalar veya uzak kimseler · uzak kimseler, yakin cevre disindakiler
  الأباعد خلاف الأقارب (maqayis;tahdhib)؛ الأبعد ضد الأقرب والجمع أقربون وأبعدون وأباعد وأقارب (ayn)؛ فلان من قربان الأمير ومن بعدانه (sihah)؛ إذا لم تكن من قربان الأمير فكن من بعدانه (tahdhib)
- **B006** uzak degil kalibi — kucuk dusmus degil · uzak degil, yakin sayilir
  تنح غير باعد أي غير صاغر وتنح غير بعيد أي كن قريبا (maqayis;sihah;tahdhib)؛ فلان غير بعيد وغير بعد (jamhara)؛ هم مني غير بعد أي ليسوا ببعيد (tahdhib)
- **B007** aralikli gorusme — aradan sonra ve araliklarla
  لقيته بعيدات بين (sihah;tahdhib)؛ إذا كان الرجل يمسك عن إتيان صاحب الزمان ثم يأتيه (sihah)؛ بعد حين ثم أمسكت عنه ثم أتيته (tahdhib)
- **B008** derin gorusluluk — derin ve tedbirli gorus sahibi
  إنه لذو بعدة أي ذو رأي وحزم؛ رجل ذو بعدة إذا كان نافذ الرأي ذا غور وذا بعد رأي
- **B009** faydasizlik — faydasi yok, hayir yok
  رجعت بغير أبعد أي بغير منفعة؛ ما عندك أبعد؛ إنك لغير أبعد أي لا خير فيك ليس لك بعد مذهب
- **B010** dusmanlikta ileri gitme — dusmanlikta ileri giden kisi
  ذا البعدة الذي يبعد في المعاداة

## ج ي ء (root_000281): 42:14 جَآءَهُمُ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · geliş; varış · bir kez geliş veya geliş biçimi · sık sık iyilik getiren · iyi ki geldin
  جاء يجيء مجيئا (maqayis;mufradat)؛ جاء فلان يجيء جيئة إذا جاء مرة واحدة وجيئة حسنة (jamhara)؛ المجئ: الاتيان، جاء يجئ جيئة، وجئت مجيئا حسنا (sihah)؛ المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا (mufradat)
- **B002** gelip gitmede üstün gelmek [kalıp] — benimle sık gelme yarışına girdi, ben de onu geçtim
  جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ وجاءانى على فاعلنى فجئته أجيئه، أي غالبني بكثرة المجئ فغلبته (sihah)
- **B003** suyun biriktiği çukur veya yer — suyun biriktiği yer veya büyük çukur · tuzlu ya da idrar karışmış kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره ويقال هي جيئة (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون، والموضع الذي يجتمع فيه الماء، والحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ جية من ماء أي ماء ناقع خبيث (tahdhib)
- **B004** bir şeyi getirmek veya hazır bulundurmak — sık sık iyilik getiren · bir şeyi getirmek veya hazır bulundurmak · onu getirmek
  أجأته، أي جئت به (sihah)؛ جاءه بكذا وأجاءه، وجاء بكذا: استحضره (mufradat)
- **B005** birini bir şeye zorlamak [kalıp] — onu belirli bir şeye zorlamak · seni buna gerek duyar duruma düşürmek
  أجأته إلى كذا بمعنى ألجأته واضطررته إليه (sihah)؛ أجاءها المخاض إلى جذع النخلة، قيل: ألجأها، وإنما هو معدى عن جاء (mufradat)
- **B006** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح، يقال: جاءت جائية الجراح (tahdhib)

## ج ي ء (root_000282): 42:14 جَآءَهُمُ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ب غ ي (root_000138): 42:14 بَغْيًۢا, 42:27 لَبَغَوْا۟, 42:39 ٱلْبَغْىُ, 42:42 وَيَبْغُونَ

- **B001** bir şeyi arayıp istemek; başkası için aramak veya arayışına yardım etmek — bir şeyi aramak ve istemek · bir şeyi çaba göstererek aramak · ihtiyaç; aranan veya istenen şey · bir şeyi birisi için aramak · birinin bir şeyi aramasına yardım etmek veya onu arayan duruma getirmek
  طلب الشيء؛ بغيت الشيء إذا طلبته؛ البغية الحاجة؛ أبغيتك الشيء إذا أعنتك على طلبه (maqayis)؛ البغية مصدر الابتغاء؛ بغيت الشيء وابتغيته طلبته (ayn)؛ بغى ضالته؛ ابتغيت الشيء وتبغيته إذا طلبته (sihah)؛ البغي طلب تجاوز الاقتصاد؛ الابتغاء خص بالاجتهاد في الطلب (mufradat)
- **B002** uygun, mümkün veya hak edilmiş olmak — uygun olmak; mümkün olmak; hak edilmiş olmak
  ما ينبغي لك أن تفعل كذا؛ بغيته فانبغى (maqayis)؛ لا ينبغي لك أن تفعل كذا وما انبغى لك (ayn)؛ ينبغي لك أن تفعل كذا هو من أفعال المطاوعة (sihah)؛ ينبغي مطاوع بغى؛ لا يتسخر ولا يتسهل له؛ على معنى الاستئهال (mufradat)
- **B003** haddi aşarak haksızlık etmek — haddi aşma, haksızlık ve baskı · birine karşı haddini aşıp haksızlık etmek · haddini aşan ve haksızlık eden kişi · birbirine haksızlık etmek
  جنس من الفساد؛ أن يبغي الإنسان على آخر؛ البغي الظلم (maqayis)؛ البغي الظلم والباغي الظالم (ayn)؛ البغي التعدي؛ بغى الرجل على الرجل استطال؛ كل مجاوزة في الحد وإفراط على المقدار فهو بغي؛ تباغوا أي بغى بعضهم على بعض (sihah)؛ البغي على ضربين؛ تجاوز الحق إلى الباطل؛ بغى تكبر (mufradat)
- **B004** yaranın şişip bozulması veya içinde irin kalmış halde kapanması [kalıp] — yaranın şişip ilerleyerek bozulması · yaranın içinde irinli bozukluk kalmış halde kapanması
  بغى الجرح إذا ترامى إلى فساد (maqayis)؛ بغى الجرح ورم وترامى إلى فساد؛ برئ جرحه على بغى وفيه شيء من نغل (sihah)؛ بغى الجرح تجاوز الحد في فساده (mufradat)
- **B005** evlilik dışı cinsel ilişki ve buna bağlı kişi adları — kadının evlilik dışı cinsel ilişkiye girmesi · evlilik dışı cinsel ilişki; cinsel ahlaka aykırı davranış · evlilik dışı cinsel ilişkiye giren kadın; bu adla anılan kadın köle · kadın köleler veya evlilik dışı cinsel ilişkiye giren kadınlar · evlilik dışı cinsel ilişkiden doğan çocuk
  البغي الفاجرة؛ بغت تبغي بغاء وهي بغي (maqayis)؛ بغى بغاء أي فجر؛ البغية من الزنى؛ البغايا الجواري (ayn)؛ بغت المرأة بغاء أي زنت فهي بغي والجمع بغايا؛ خرجت المرأة تباغي أي تزاني؛ الأمة يقال لها بغي (sihah)؛ بغت المرأة بغاء إذا فجرت (mufradat)
- **B006** göğün şiddetli, bol ve gereğinden fazla yağdırması [kalıp] — göğün şiddetli veya gereğinden fazla yağmur yağdırması · göğün en şiddetli ve bol yağmuru
  بغي المطر وهو شدته ومعظمه؛ بغي السماء أي معظم مطرها (maqayis)؛ بغت السماء اشتد مطرها؛ بغي السماء أي معظم مطرها (sihah)؛ بغت السماء تجاوزت في المطر حد المحتاج إليه (mufradat)
- **B007** atın koşarken çalımlı ve neşeli davranması [kalıp] — atın koşarken çalımlı ve neşeli davranması
  اختيال الفرس ومرحه بغي؛ لا يقال فرس باغ (maqayis)؛ البغي في عدو الفرس اختيال ومرح؛ لا يقال فرس باغ (ayn)؛ البغي اختيال ومرح في الفرس؛ لا يقال فرس باغ (sihah)
- **B008** ordudan önce ilerleyen öncüler — ordudan önce ilerleyen öncüler · öncü topluluğun tek bir üyesi
  البغايا الطلائع الواحدة بغية أيضا (ayn)؛ البغايا أيضا الطلائع التي تكون قبل ورود الجيش (sihah)

## ب ي ن (root_000170): 42:14 بَيْنَهُمْ, 42:14 بَيْنَهُمْ, 42:15 بَيْنَكُمُ, 42:15 بَيْنَنَا, 42:15 وَبَيْنَكُمُ, 42:15 بَيْنَنَا, 42:21 بَيْنَهُمْ, 42:38 بَيْنَهُمْ

- **B001** ayrılıp kopma — ayrılık ve kopuş · ayrılmak, kopmak, kesilip ayrılmak · karşılıklı ayrılma ve uzaklaşma
  البين الفراق (maqayis;sihah)؛ البينونة مصدر بأن يبين بينا وبينونة أي قطع (ayn)؛ البين مصدر بان يبين بينا (jamhara)؛ بان كذا أي انفصل (mufradat)
- **B002** arada olma — iki veya daha çok şey arasındaki orta ve aralık · önünde, yanında veya yakınında · topluluğun içinden veya topluluğa dahil
  بين بمعنى وسط (sihah)؛ بين موضوع للخلالة بين الشيئين ووسطهما (mufradat)؛ لا يستعمل بين إلا فيما كان له مسافة أو له عدد ما اثنان فصاعدا (mufradat)
- **B003** arayı bağlayan ilişki — taraflar arasındaki bağ ve bağlantı · aranızdaki akrabalık, yakınlık ve sevgi durumları
  البين الوصل (ayn;sihah)؛ لقد تقطع بينكم أي وصلكم (mufradat)؛ ذات بينكم أي الأحوال التي تجمعكم من القرابة والوصلة والمودة (mufradat)
- **B004** açığa çıkıp belirginleşme — görünmek, açığa çıkmak, belirginleşmek · açık hale getirmek ve ortaya koymak · açık kanıt veya açık tanıklık · açık veya açıklayıcı işaretler
  بان الشيء وأبان إذا اتضح وانكشف (maqayis)؛ البيان معروف وبان الشيء وأبان وتبين وبين واستبان (ayn)؛ بان الشيء بيانا اتضح فهو بين (sihah)؛ البينة الدلالة الواضحة (mufradat)
- **B005** anlamı açıkça ortaya koyma — anlamı söz, yazı veya işaretle açıkça ortaya koyma · açık ve düzgün konuşan adam
  أبين من فلان أي أوضح كلاما منه (maqayis)؛ البين من الرجال الفصيح (ayn)؛ البيان الفصاحة واللسن (sihah)؛ البيان الكشف عن الشيء وهو أعم من النطق (mufradat)
- **B006** geniş uzaklık — ikisi arasında büyük uzaklık · dibi uzak veya geniş kuyu
  أصل واحد وهو بعد الشيء (maqayis)؛ البائنة البئر البعيدة القعر الواسعة (sihah)؛ بيون لبعد ما بين الشفير والقعر (mufradat)
- **B007** göz erimindeki arazi parçası — göz erimindeki arazi parçası, yöre veya kabarık yer
  البين قطعة من الأرض قدر مد البصر (maqayis)؛ البين الغلظ من الأرض (jamhara)؛ البين بالكسر القطعة من الأرض قدر منتهى البصر (sihah)؛ البين أيضا الناحية (sihah)
- **B008** bağlı yerinden ayrılma [kalıp] — devenin ayağının yanından açılması · teli gövdesinden uzak duran yay · başını gövdesinden kesip ayırmak
  بانت يد الناقة عن جنبها (ayn)؛ قوس بائن وهي التي بان وترها عن كبدها (ayn)؛ ضربه فأبان رأسه من جسده وفصله (sihah)؛ البائنة القوس التي بانت عن وترها كثيرا (sihah)
- **B009** sol yandan sağan kişi — sağımda hayvanın sol yanından gelen sağan
  البائن أحد الحالبين والآخر يسمى المستعلي (ayn)؛ البائن الذي يأتي الحلوبة من قبل شمالها والمعلى من قبل يمينها (sihah)
- **B010** o sırada — o sırada, bir şey olurken
  قولك بينا فلان معناه بينما (ayn)؛ بينا نحن نرقبه أتانا أي أتانا بين أوقات رقبتنا إياه (sihah)؛ يزاد في بين ما أو الألف فيجعل بمنزلة حين (mufradat)
- **B011** iki arada kalmış hal — iki uç arasında kalan orta veya zayıf hal
  هذا الشيء بين بين أي بين الجيد والرديء (sihah)؛ الهمزة المخففة تسمى بين بين (sihah)؛ يسقط بين بينا أي يتساقط ضعيفا غير معتد به (sihah)
- **B012** geri dönüşsüz boşanma [kalıp] — geri dönüş hakkını kesen boşanma
  تطليقة بائنة وهي فاعلة بمعنى مفعولة (sihah)
- **B013** ayrılık uğursuzu kuş [kalıp] — ayrılığı uğursuz biçimde haber verdiği sayılan kuş
  غراب البين يقال هو الأبقع (sihah)؛ غراب البين هو الأحمر المنقار والرجلين (sihah)؛ يحتم بالفراق (sihah)

## ك ل م (root_001316): 42:14 كَلِمَةٌ, 42:21 كَلِمَةُ, 42:24 بِكَلِمَٰتِهِۦٓ, 42:51 يُكَلِّمَهُ

- **B001** anlaşılır konuşma, hitap ve söz alışverişi — anlaşılır konuşma · ona hitap etti · birine söz yöneltme · ona sözle karşılık verdi · bir uzaklaşmadan sonra yeniden karşılıklı konuştuk · seninle konuşan ve senin de konuştuğun kişi · konuşulacak yer · sözünü iyi ve akıcı söyleyen kimse · iyi konuşan adam
  أحدهما يدل على نطق مفهم (maqayis)؛ كلمته أكلمه تكليما وهو كليمى إذا كلمك أو كلمته (maqayis)؛ كليمك الذي يكلمك وتكلمه (ayn;tahdhib)؛ الكليم الذي يكلمك وكلمته تكليما وكلاما (sihah)؛ كالمته إذا جاوبته وتكالمنا بعد التهاجر (sihah)؛ ما أجد متكلما أي موضع كلام والكلماني المنطيق (sihah)؛ رجل تكلامة يحسن الكلام (tahdhib)
- **B002** anlam taşıyan tek söz birimi — anlamlı tek söz veya harf · en az üç sözden oluşan sözler topluluğu · sözler · bütün bir anlatı, şiir veya söylev · Tanrı'nın sözü · Tanrı'nın söylediği söz
  يسمون اللفظة الواحدة المفهمة كلمة والقصة كلمة والقصيدة بطولها كلمة ويجمعون الكلمة كلمات وكلما (maqayis)؛ الكلمة لغة حجازية والكلمة تميمية والجميع الكلم (ayn;tahdhib)؛ الكلام اسم جنس يقع على القليل والكثير والكلم لا يكون أقل من ثلاث كلمات والكلمة أيضا القصيدة بطولها (sihah)؛ الكلمة تقع على الحرف الواحد من حروف الهجاء وتقع على لفظة واحدة مؤلفة من جماعة حروف لها معنى وتقع على قصيدة بكمالها وخطبة بأسرها (tahdhib)؛ كلمة الله وكلام الله وكلم الله وكلمات الله (sihah;tahdhib)
- **B003** yaralama ve yara — yara · yaralar · yaralar · onu yaraladı · yaralayan · yaralanmış · yaralı kişi · yaralılar · yaralama · onları yaralayıp damgalaması
  الأصل الآخر الكلم وهو الجرح والكلام الجراحات وجمع الكلم كلوم (maqayis)؛ الكلم الجرح والجميع الكلوم وكلمته أكلمه كلما وأنا كالم وهو مكلوم أي جرحته (ayn)؛ الكلم الجراحة والجمع كلوم وكلام والتكليم التجريح (sihah)؛ الكلم الجرح والجميع كلوم وكلمته وأنا أكلمه كلما وأنا كالم وهو مكلوم (tahdhib)؛ تكلمهم فسر تجرحهم وتسمهم (sihah;tahdhib)

## س ب ق (root_000671): 42:14 سَبَقَتْ

- **B001** harekette ya da işte öne geçme ve yarışarak ön alma — koşuda, işte ya da bir şeyde başkasının önüne geçmek · öne geçme; koşuda ya da işte önce gelme · bir işte önceden kazanılmış öncelik · yarışma; koşuda ve benzeri bir alanda birbirini geçmeye çalışma · yarışmak ya da bir şeye önce davranmak · atış yarışmasına gitmek · kapıya ilk varmak için birbirinden önce davranmak · yolu aşıp geçerek yönünü kaybetmek · yarışta başa geçen at ya da benzeri varlık · iyi işlerle ödüle önden koşanlar · önceden kesinleşip yürürlüğe girmek
  أصل واحد صحيح يدل على التقديم (maqayis)؛ السبق القدمة في الجري وفي الأمر (ayn;tahdhib)؛ وسبق يسبق سبقا (jamhara)؛ سابقته فسبقته سبقا واستبقنا في العدو أي تسابقنا (sihah)؛ أصل السبق التقدم في السير والاستباق التسابق (mufradat)
- **B002** yarışta ortaya konup kazananın aldığı pay — yarışta ya da atışta ortaya konup kazananın aldığı pay · yarış payını almak ya da yarış payını vermek · ortaya konan yarış payını kazandı
  السبق الخطر الذي يأخذه السابق (maqayis)؛ السبق الخطر يوضع بين أهل السباق (ayn;sihah)؛ السبق الرهن (jamhara)؛ الخطر الذي يوضع في النضال والرهان في الخيل فمن سبق أخذه (tahdhib)
- **B003** avcı kuşun ayaklarına takılan iki bağ — avcı kuşun ayaklarına takılan iki bağ · avcı kuşun ayaklarına bu iki bağı takmak
  السباقان قيد أرجل الطائر الجارح بسير أو خيط (ayn)؛ سباقا البازي قيداه من سير أو غيره (sihah)؛ السباقان في رجل الطائر الجارح قيداه من سير أو خيط وسبقت البازي إذا جعلت السباقان في رجليه (tahdhib)
- **B004** yakalanmaktan kurtulacak kadar öne kaçma — takip edenin elinden kaçıp kurtulmak · kaçıp kurtulmuş olmamak; takip edeni aşamamış olmak
  وما نحن بمسبوقين أي لا يفوتوننا؛ ولا يحسبن الذين كفروا سبقوا؛ وما كانوا سابقين (mufradat)

## ء ج ل (root_000016): 42:14 أَجَلٍ

- **B001** belirlenmiş süre, son zaman ve o zamana erteleme — belirlenmiş süre veya son zaman · adı konmuş belirli süre · ölüm zamanı yaklaştı · hemen olmayıp sonraya kaldı · sonraya bırakılmış olan · belirli bir zamana ertelenmiş · öteki dünya · ona belirli bir süre koydu · süre istedi, o da süre verdi
  الأجل غاية الوقت في الموت ومحل الدين ونحوه (ayn;tahdhib)؛ الأجل مدة الشيء (sihah)؛ الأجل المدة المضروبة للشيء (mufradat)؛ الأجيل المرجأ أي المؤخر إلى وقت والآجل نقيض العاجل (maqayis)
- **B002** nedeniyle veya yüzünden — bundan dolayı, bunun yüzünden · senin yüzünden veya senin için · bundan dolayı · sen böyle olduğun için
  فعلت ذاك من أجل كذا ومن جراء كذا أي من أجله (ayn)؛ فعلت ذاك من أجلك ومن إجلك ومن أجلاك أي من جراك (sihah)؛ من أجلاك وإجلاك ومن جلالك بمعنى واحد (tahdhib)؛ من أجل ذلك فعلت كذا محمول على أجلت الشيء أي جنيته (maqayis)
- **B003** evet, doğrudur — evet, doğrudur
  قولهم أجل إنما هو جواب مثل نعم (sihah)؛ قولهم أجل في الجواب هو من هذا الباب كأنه يريد انتهى وبلغ الغاية (maqayis)
- **B004** yaban sığırı sürüsü ve sürüleşme — yaban sığırı sürüsü · yaban sığırı sürüleri · sürü veya sürüler haline geldi
  الإجل القطيع من بقر الوحش والجميع الآجال وتأجل الصوار صار قطيعا قطيعا (ayn)؛ الإجل القطيع من بقر الوحش والجمع الآجال وتأجلت البهام أي صارت آجالا (sihah)؛ الأجل القطيع من بقر الوحش وجمعه الآجال (tahdhib)؛ الإجل القطيع من بقر الوحش والجمع آجال (maqayis)
- **B005** kötülük işleyip hedefe yöneltme — başlarına kötülük getirip körükledi · kötülük işleyip yöneltme
  أجل عليهم شرا أجلا أي جناه وبحثه (ayn)؛ أجل عليهم شرا يأجل ويأجل أجلا أي جناه وهيجه (sihah)؛ أجلت عليهم آجل أجلا أي جررت جريرة (tahdhib)؛ الأجل مصدر أجل عليهم شرا أي جناه وبحثه (maqayis)
- **B006** boyun ağrısı, buna yol açan yatış ve tedavisi — boyun ağrısı · boynu üzerine yatıp ağrı çekti · boyun ağrısını tedavi etme · boynum ağrıyor, beni tedavi edin
  الأجل وجع في العنق (ayn)؛ الإجل وجع في العنق وقد أجل الرجل أي نام على عنقه فاشتكاها والتأجيل المداواة منه (sihah)؛ الإجل وجع في العنق وبي إجل فأجلوني أي داووني (tahdhib)؛ الإجل وجع في العنق وبي إجل فأجلوني أي داووني منه (maqayis)
- **B007** su biriktiren havuz ve suyun toplanması — su biriktiren havuz veya su birikintisi · su biriktiren havuzlar · su birikintisi · su toplandı · toplanmış su · hurma ağacın için havuz yap
  المأجل شبه حوض واسع يؤجل فيه ماء البئر وماء القناة (ayn)؛ المأجل مستنقع الماء وقد تأجل الماء وماء أجيل أي مجتمع (sihah)؛ المأجل شبه حوض واسع يؤجل فيه ماء القناة والمأجل الجبأة التي يجتمع فيها مياه الأمطار (tahdhib)؛ المأجل شبه حوض واسع يؤجل فيه ماء البئر أو القناة (maqayis)؛ الماجل مستنقع الماء وهذا من باب أجل (maqayis)
- **B008** sürü hayvanlarını otlakta tutma — develerini veya sürülerini otlakta tuttular · sürü hayvanlarını otlakta tutma
  الأجل مصدر قولك أجلوا إبلهم أي حبسوها في المرعى (ayn)؛ أجلوا مالهم يأجلونه أجلا أي حبسوه والأصل في ذلك الزاء أزلوه (maqayis)

## ق ض ي (root_001237): 42:14 لَّقُضِىَ, 42:21 لَقُضِىَ

- **B001** kesin hüküm veya buyruk vermek — hükme bağladı veya kesin olarak buyurdu · hüküm verme ve işi kesin sonuca bağlama · hüküm veya karara bağlanmış konu · insanlar arasında hüküm veren ve kararları uygulayan yargıç · yargıç olarak görevlendirildi
  قضى يقضي قضاء وقضية أي حكم (ayn); القضاء الحكم وقضى أي حكم (sihah); قضى ربك أي أمر ربك والقضاء الفصل في الحكم (tahdhib); القضاء فصل الأمر وقضى ربك أي أمر (mufradat); القضاء الحكم وسمي القاضي قاضيا لأنه يحكم الأحكام وينفذها (maqayis)
- **B002** kalıp içinde kesin bildirmek veya ahit ya da talimat iletmek [kalıp] — ona bir ahit veya talimat iletti · onlara kesin biçimde bildirdik
  قضى إليه عهدا معناه الوصية (ayn); قضينا إليه ذلك الأمر أي أنهيناه إليه وأبلغناه (sihah); قضينا إلى بني إسرائيل أي أعلمناهم إعلاما قاطعا وقضى الله عهدا معناه الوصية (tahdhib); أعلمناهم وأوحينا إليهم وحيا جزما (mufradat)
- **B003** ölümün gerçekleşmesi veya gerçekleştirilmesi — ölüm onun yaşamını sona erdirdi · öldü · insanın yaşamını sona erdiren ölüm · öldürücü zehir · insanların arasında gerçekleşen ölümler
  فلما قضينا عليه الموت أي أتى والقاضية المنية (ayn); ضربه فقضى عليه أي قتله وقضى نحبه أي مات (sihah); فلما قضينا عليه الموت أي أتى عليه والقاضية المنية (tahdhib); يعبر عن الموت بالقضاء وقضى نحبه معناه مات (mufradat); سميت المنية قضاء لأنه أمر ينفذ (maqayis)
- **B004** tamamlayıp bitirmek veya sona erip tükenmek — kendine yüklediği adağı yerine getirdi · gereksinimini giderip işini bitirdi · sona erdi, tükenip gitti · ibadetini tamamladı · süreyi tamamlayıp sonuna ulaştı · isteğini giderip işini bitirdi · içindekileri bütünüyle döküp ağlamasını bitirdi · gereksinimini bütünüyle giderdi · iş geri alınamayacak biçimde sonuçlandı
  انقضى الشيء وتقضى أي فني وذهب (ayn); بمعنى الفراغ وقضيت حاجتي وانقضى الشيء وتقضى (sihah); قضي الأمر أتم إهلاكهم وقضى صلاته فرغ منها والانقضاء ذهاب الشيء وفناؤه (tahdhib); فإذا قضيتم مناسككم وليقضوا تفثهم وأيما الأجلين قضيت وفلما قضى زيد منها وطرا (mufradat)
- **B005** yapıp kusursuzca tamamlamak ve yürürlüğe koymak — giysiyi ve evi yapıp işçiliğini kusursuzlaştırdı · onları yedi gök olarak yaratıp kusursuzca tamamladı · yapacağın işi gerçekleştir · tasarlamadan sonra kesinleştirip yürürlüğe koyma · işçiliği tamamlanmış sağlam zırhlar
  قضاه أي صنعه وقدره ومنه فقضاهن سبع سموات (sihah); كل ما أحكم فقد قضي وخلقهن وعملهن وصنعهن وفاقض ما أنت قاض أي فاعمل (tahdhib); فقضاهن سبع سماوات إشارة إلى إيجاده الإبداعي والفراغ منه (mufradat); أصل يدل على إحكام أمر وإتقانه وإنفاذه لجهته (maqayis)
- **B006** borcu ödeyerek veya tahsil ederek kapatmak — borcunu ödeyip aradaki yükümlülüğü kapattı · borcunun ödenmesini istedi veya alacağını tahsil etti · ondan hakkını istedi veya hakkını teslim aldı · kan bedeli veya zorunlu ödemede geçerli sayılan deve
  قضيت ديني واقتضى دينه وتقاضاه (sihah); قضى فلان دينه وقطع ما بينه وبينه وتقاضيته حقي فقضانيه واقتضيت مالي عليه (tahdhib); قضى الدين فصل الأمر فيه برده والاقتضاء المطالبة بقضائه (mufradat)
- **B007** uzun süre bırakılan tulumun bozulup eskimesi — tulum uzun süre bırakıldığı için bozulup eskidi
  قضي السقاء قضا فهو قض إذا طال تركه في مكان ففسد وبلي (ayn)
- **B008** kuru üzüm çekirdeği ve onu yemek — adam kuru üzüm çekirdeğini yedi · kuru üzüm çekirdeği
  قضى الرجل إذا أكل القضى وهو عجم الزبيب (tahdhib)

## و ر ث (root_001639): 42:14 أُورِثُوا۟

- **B001** mirasın mirasçıya geçmesi — miras · miras, miras kalan mal · miras, kalıt · miras; atadan kalan köken veya kalıntı · miras yoluyla geçiş · miras · miras · miras almak, mirasçısı olmak · mirasçıları · kuşaktan kuşağa miras almak
  أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب (maqayis)؛ ورثت أبي وورثت الشيء من أبي (sihah)؛ ورث فلان أباه، ورثت فلانا مالا إذا مات مورثك فصار ميراثه لك (tahdhib)؛ الوراثة والإرث انتقال قنية إليك عن غيرك من غير عقد، وإرث أبيكم أي أصله وبقيته (mufradat)
- **B002** miras bırakmak veya emeksizce kazandırmak — miras bırakmak, miras yoluyla kazandırmak · malına miras payıyla dahil etmek · emeksizce elde etmek
  يصير إلى آخرين بنسب أو سبب (maqayis)؛ أورثه الشيء أبوه، ورثه توريثا أي أدخله في ماله على ورثته (sihah)؛ أورث الرجل ولده مالا، ورثت فلانا من فلان أي جعلت ميراثه له (tahdhib)؛ أورثني الله كذا، لكل من حصل له شيء من غير تعب، خول شيئا مهنئا (mufradat)
- **B003** maddi olmayan mirasın aktarılması — peygamberlik, bilgi veya erdemin maddi olmayan mirası · bilgiyi bir öncekinden edinmek · kitabı veya bilgisini miras yoluyla devralmak · peygamberlerin bilgi mirasçıları
  وراثة النبوة والعلم والفضيلة دون المال؛ العلماء ورثة الأنبياء؛ ورثت علما من فلان أي استفدت منه (mufradat)
- **B004** her şeyden sonra kalıp mülkün kendisine dönmesi — her şeyden sonra kalan ve her şeyin döndüğü varlık · ölümüne dek yanında kalan · göklerin ve yerin sonunda Tanrı'ya kalan mülkiyeti · yer ve üzerindekiler yok olduktan sonra kalıp mülkü geri almak
  الوارث صفة من صفات الله وهو الباقي الدائم (tahdhib)؛ يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه (tahdhib)؛ الأشياء كلها صائرة إلى الله (mufradat)
- **B005** koru karıştırıp ateşi tutuşturmak [kalıp] — ateşin korunu karıştırıp tutuşturmak · ateşin korunu karıştırıp tutuşturmak
  الورثة: لغة في ورثت النار وأرثتها إذا حركت جمرها لتشتعل (jamhara)

## ك ت ب (root_001283): 42:14 ٱلْكِتَٰبَ, 42:15 كِتَٰبٍ, 42:17 ٱلْكِتَٰبَ, 42:52 ٱلْكِتَٰبُ

- **B001** bir şeyi başka bir şeye katıp birleştirme — bir şeyi başka bir şeye katıp birleştirme · su tulumunu dikerek birleştirmek · katırın üreme organının dudaklarını halka veya kayışla birleştirmek · dişi devenin burun deliklerini iplikle dikmek veya bağlamak · dişi devenin memelerini bağlamak · su tulumunun ağzını bağıyla sıkıca kapatmak · kayışın iki yüzünü birleştiren boncuk · bir arada duran atlı veya askerî birlik · atların toplanması · askerleri birlik birlik düzenlemek
  أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)
- **B002** yazma ve yazılı metin — kitabı yazmak veya kopyalamak · yazılı metin veya üzerinde yazı bulunan sayfa · yazma işi ve yazıcılık · kitabı yazmak veya kopyalamak · ona şiiri söyleyerek yazdırmak · birinden kendisi için bir şey yazmasını istemek · çocuğa yazmayı öğretmek · yazı öğretmeni veya yazı öğretilen yer · öğretim yerindeki çocuklar veya onların topluluğu
  الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)
- **B003** bağlayıcı olarak hükme bağlama ve belirleme — yükümlülük, hüküm veya yazgı · size zorunlu kılındı · Tanrı belirledi, karara bağladı veya zorunlu kıldı
  الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)
- **B004** adını sicile yazma veya bir gruba dâhil etme — pay veya geçim tahsisatı için kaydolma · adını pay kaydına veya yönetim siciline yazdırmak · bizi tanıklar topluluğuna kat
  الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)
- **B005** özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi — kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi · özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi · köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak · kölenin özgürlüğünü satın almak için yaptığı sözleşme
  المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)

## ش ك ك (root_000812): 42:14 شَكٍّ

- **B001** karşıt olasılıklar arasında kesinliğe varamama — kesinliğin karşıtı olan kuşku · bir konuda kuşku duymak · kuşkuya düşmek ve duraksamak · birini bir konuda kuşkuya düşürmek · çiftleşip çiftleşmediği bilinmeyen dişi deve
  الشك خلاف اليقين (maqayis;ayn;sihah;tahdhib)؛ اعتدال النقيضين وتساويهما (mufradat)؛ الشكوك الناقة التي يشك فيها (sihah)
- **B002** içine geçirerek delme veya birleştirme — kargıyla delip ucunu gövdeye geçirmek · iki yaprağın arasına çubuk saplayıp birleştirmek · bir şeyi ötekine sokmak ya da eklemek · balta gözünü daraltan geniş tahta kama · deve taşıma kafesinin birbirine geçirilmiş çubukları
  شككته بالرمح إذا طعنته فداخل السنان جسمه (maqayis)؛ شككته بالرمح خرقته (ayn)؛ شككته بالرمح أي خرقته وانتظمته (sihah)؛ كل شيء ضممته إلى شيء فقد شككته (tahdhib)؛ شككت الشيء أي خرقته (mufradat)
- **B003** üstüne giyilen savaş donanımı — kişinin üzerine giydiği savaş donanımı · eksiksiz savaş donanımını kuşanmış · demir savaş donanımı kuşanmış topluluk · süvarinin gemleri ve donanımı
  الشكة ما يلبسه الإنسان من السلاح (maqayis)؛ الشكة ما يلبس من السلاح (ayn;tahdhib)؛ الشكة بالكسر السلاح وشاك في السلاح (sihah)؛ الشكة السلاح الذي به يشك (mufradat)
- **B004** yapışma, bitişme ve yakın temas — devenin hafifçe aksaması · yapışma, bitişme veya üst kolun böğre değmesi · yakın ve bağlı akrabalık · eli öteki ele değmek veya onunla yan yana gelmek
  بعير شاك وقد شك شكا (maqayis;sihah;tahdhib)؛ الشك اللزوم واللصوق (sihah)؛ لصوق العضد بالجنب (maqayis;mufradat)؛ ما قارن ورحم شاكة أي قريبة وقد شكت إذا اتصلت (tahdhib)
- **B005** bölük oluşturma veya ortak düzende sıralama — insan bölüğü · insan bölükleri · bölükler oluşturan asker toplulukları · evleri aynı doğrultuda ve düzende sıralamak · aynı doğrultuda sıralanmış evler
  الشكائك الفرق من الناس الواحدة شكيكة (maqayis;sihah;tahdhib)؛ الشكك الجماعات من العساكر يكونون فرقا (tahdhib)؛ شك القوم بيوتهم إذا جعلوها على طريقة واحدة ونظم واحد (tahdhib)
- **B006** birini gerçek olmayan bir soya bağlama — bir kişiyi gerçek soyundan başka bir soya bağlamak · gerçek soyundan başka bir soya bağlanmış kimseler
  شك إذا ألحق بنسب غيره؛ الشكك الأدعياء

## ء م ر (root_000051): 42:15 أُمِرْتَ, 42:15 وَأُمِرْتُ, 42:38 وَأَمْرُهُمْ, 42:43 ٱلْأُمُورِ, 42:52 أَمْرِنَا, 42:53 ٱلْأُمُورُ

- **B001** konu ve hal — konu, hal veya tekil iş · konular, haller ve işler
  الأمر من الأمور، الواحد من الأمور (maqayis)؛ الأمر واحد من أمور الناس (ayn)؛ الأمر واحد الأمور (sihah;tahdhib)؛ الأمر الشأن وجمعه أمور (mufradat)
- **B002** buyrukla yükümlü kılma — yapma buyruğu ve yükümlü kılma · ona bir şeyi yapmasını buyurdum · buyurma fiilinin söz içindeki biçimi · uyulacak tek bir buyruk hakkı · iyiliği çokça buyuran · onlara uymaları buyruldu, onlar da karşı geldi
  الأمر الذي هو نقيض النهي قولك افعل كذا (maqayis)؛ الأمر نقيض النهي وإذا أمرت من الأمر قلت اؤمر (ayn)؛ أمرته بكذا أمرا والجمع الأوامر (sihah)؛ الأمر معروف نقيض النهي (tahdhib)؛ مصدر أمرته إذا كلفته أن يفعل شيئا، والتقدم بالشيء (mufradat)
- **B003** yönetme yetkisi — yönetme makamı ve yetkisi · yetkili yönetici · yönetici kılınmış kimse · onu yönetici yaptım · topluluğunun yöneticisi oldu · yetki sahipleri · onları yönetici kıldık
  الإمرة والإمارة وصاحبها أمير ومؤمر (maqayis)؛ الإمرة الإمارة وهو أمير مؤمر (ayn)؛ الأمير ذو الأمر والتأمير تولية الامارة (sihah)؛ أمر الرجل إمارة إذا صار عليهم أميرا (tahdhib)؛ أولي الأمر عنى الأمراء، وقرئ أمرنا أي جعلناهم أمراء (mufradat)
- **B004** bereketli çoğalma — artış, verim ve bereket · çoğaldı ve büyüdü · topluluk çoğaldı, malları veya nimetleri arttı · uğurlu, bereket getiren kişi · çok yavrulayan ve bereketli kısrak · Tanrı onun malını çoğalttı · onları veya varlıklılarını çoğalttık
  الأمر النماء والبركة، وقد أمر الشيء أي كثر (maqayis)؛ الأمرة البركة وامرأة أمرة، وأمر الشيء أي كثر (ayn)؛ أمر هو أي كثر، وأمر القوم أي كثروا (sihah)؛ الأمرة الزيادة والنماء والبركة (tahdhib)؛ أمر القوم كثروا، وآمرنا بمعنى أكثرنا (mufradat)
- **B005** belirti veya belirlenmiş vakit — belirti, belirlenmiş zaman veya buluşma vakti · yolun işaretleri · çöl veya yol üzerindeki küçük işaret taşı
  الأمارة الموعد، والأمارة العلامة، والأمار أمار الطريق معالمه (maqayis)؛ الأمار الموعد (ayn)؛ الأمار والأمارة الوقت والعلامة، والأمر بالتحريك جمع أمرة وهي العلم الصغير من أعلام المفاوز من الحجارة (sihah)؛ الأمار الوقت والعلامة، والأمرات الأعلام واحدتها أمرة (tahdhib)
- **B006** ağır ve yadırganan şey — büyük, ağır, yadırganan veya şaşırtıcı iş · büyük ve yadırganan bir şey
  العجب، لقد جئت شيئا إمرا (maqayis)؛ أمر أمره أي اشتد والاسم الإمر، ويقال عجبا (sihah)؛ لقد جئت شيئا إمرا أي جئت شيئا عظيما من المنكر (tahdhib)؛ إمرا أي منكرا، من قولهم أمر الأمر أي كبر وكثر (mufradat)
- **B007** danışıp görüş oluşturma — işimde ona danıştım · karşılıklı danışma veya birbirinin görüşünü kabul etme · kendi içinde düşünüp görüşünü karara bağladı · senin hakkında birbirleriyle danışıyorlar
  فلان يؤامر نفسيه أي نفس تأمره بشيء ونفس تأمره بآخر (maqayis)؛ آمرته في أمري إذا شاورته، والائتمار والاستئمار المشاورة وكذلك التآمر (sihah)؛ ائتمر القوم إذا تشاوروا، أي كيف يرتئي رأيا ويشاور نفسه ويعقد عليه (tahdhib)؛ الائتمار قبول الأمر، ويقال للتشاور ائتمار (mufradat)
- **B008** zayıf görüşlü kişi — görüşü zayıf, her sözü dinleyip uyan akılsız kişi
  الإمر الرجل الضعيف الرأي الأحمق الذي يسمع كلام هذا وكلام هذا (maqayis)؛ الإمر الضعيف من الرجال (ayn)؛ رجل إمر وإمرة أي ضعيف الرأي يأتمر لكل أحد (sihah)؛ رجل إمر وإمرة أي يستأمر كل أحد في أمره، والإمر الأحمق (tahdhib)
- **B009** küçük koyun yavrusu — küçük koyun yavrusu; dişisi dişi kuzu veya genç dişi koyun
  الإمرة الأنثى من الحملان (ayn)؛ الإمر الصغير من ولد الضأن والأنثى إمرة (sihah)؛ الإمر الخروف والإمرة الرخل (tahdhib)
- **B010** Tanrı'ya özgü yaratma — Tanrı'ya özgü yaratma ve var etme
  ويقال للإبداع أمر، ويختص ذلك بالله تعالى دون الخلائق؛ قل الروح من أمر ربي أي من إبداعه؛ إنما قولنا لشيء إذا أردناه أن نقول له كن فيكون
- **B011** mızrağa uç takma — sivriltilmiş veya uç takılmış mızrak ucu · mızrağına keskin uç tak
  سنان مؤمر أي محدد؛ أمر قناتك أي اجعل فيها سنانا

## ت ب ع (root_000175): 42:15 تَتَّبِعْ

- **B001** ardından gitmek ve yolunu benimsemek — birlikte ya da arkasından yürümek · izinden gitmek, örneğini veya buyruğunu benimsemek · ardından giden kimse · ardından giden kimse veya topluluk
  التابع التالي؛ يتبعه يتلوه؛ تبعه يتبعه تبعا؛ هؤلاء تبع وأتباع (ayn)؛ تبعت الرجل إذا مشيت معه (jamhara)؛ تبعت القوم تبعا وتباعة إذا مشيت خلفهم؛ التبع يكون واحدا وجماعة (sihah)؛ التابع التالي؛ اتباع بالمعروف؛ اتبعوا القرآن (tahdhib)؛ تبعه واتبعه قفا أثره تارة بالجسم وتارة بالارتسام والائتمار (mufradat)
- **B002** geriden yetişmek veya peşine takmak — önden gidene yetişmek veya başkasını peşine takmak · uzaklaşan topluluğun izlerini gözle sürdürmek
  وأتبعت القوم بصري إذا أتبعت النظر في آثارهم (jamhara)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعت غيري؛ أتبعه الشيء فتبعه (sihah)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعه يريد به شرا؛ ما زلت أتبعهم حتى أتبعتهم أي حتى أدركتهم (tahdhib)؛ أتبعه إذا لحقه (mufradat)
- **B003** adım adım iz sürüp araştırmak — bir şeyi zaman içinde parça parça aramak · izleri adım adım araştırmak
  التتبع فعلك شيئا بعد شيء؛ تتبعت علمه أي اتبعت آثاره (ayn)؛ تتبعت الشيء تتبعا أي تطلبته متتبعا له (sihah)؛ التتبع أن يتتبع في مهلة شيئا بعد شيء؛ يتتبع مساوىء فلان وأثره؛ أتتبعه من اللخاف والعسب (tahdhib)
- **B004** aralıksız peş peşe gelmek — kesintisiz ardışıklık · iki şeyi ara vermeden peş peşe yapmak · aralıksız olarak peş peşe
  التباع الولاء؛ تابعه على كذا متباعة وتباعا (sihah)؛ تابع بين الصلاة وبين القراءة إذا والى بينهما؛ تباعا أي ولاء؛ يتابع الحديث إذا كان يسرده (tahdhib)؛ فأتبعنا بعضهم بعضا (mufradat)
- **B005** hak istemek ve alacağı ödeyene yöneltmek — hak, öç veya alacak isteyen kimse · alacak için ödeme gücü olan kişiye yönlendirilmek · kan bedelini veya hakkı uygun biçimde istemek
  ليس عليك من هذا الأمر تبيعة وتباعة وتبعة (jamhara)؛ التبيع الذي لك عليه مال (sihah)؛ التبيع تابع بالثأر أو مطالب؛ اتباع بالمعروف أي المطالبة بالدية؛ له عليك مال يتابعك به أي يطالبك به؛ إذا أتبع أحدكم على مليء فليتبع (tahdhib)؛ أتبعت عليه أي أحلت عليه؛ أتبع فلان بمال أي أحيل عليه (mufradat)
- **B006** üzerinde kalan yükümlülük veya olumsuz sonuç — kişinin üzerinde kalan hak, sorumluluk veya istenmeyen sonuç
  ليس عليك من هذا الأمر تبيعة وتباعة وتبعة أي لا يلحقك منه شيء تكرهه (jamhara)؛ التباعة مثل التبعة (sihah)؛ التبعة والتباعة اسم للشيء الذي لك فيه بغية شبه ظلامة (tahdhib)
- **B007** ilk yılındaki sığır yavrusu ve yavrusu ardındaki inek — ilk yaş yılındaki erkek sığır yavrusu · ilk yaş yılındaki dişi sığır yavrusu · yavrusu arkasından gelen inek
  بقرة متبع إذا كان ولدها يتبعها والولد تبيع (jamhara)؛ التبيع ولد البقرة في أول سنة والأنثى تبيعة (sihah)؛ يأخذ من كل ثلاثين من البقر تبيعا؛ ولد البقرة أول سنة تبيع؛ بقرة متبع خلفها تبيع (tahdhib)؛ التبيع خص بولد البقر إذا تبع أمه؛ المتبع من البهائم التي يتبعها ولدها (mufradat)
- **B008** biçime bağlı adlandırmalar — güneşin hareketini izleyen gölge · belirli bir yıldızın adı · belirli bir kuş veya iri kanatlı böcek türü · binek hayvanının ayağı veya bacakları
  القوائم يقال لها تبع (ayn)؛ سمي الظل تبعا لاتباعه الشمس (jamhara)؛ التبع أيضا الظل؛ التبع أيضا ضرب من الطير (sihah)؛ التبع الطل؛ التبع هو الدبران؛ التابع والتويبع؛ التبع ضرب من اليعاسيب؛ التبع سيد النحل (tahdhib)؛ التبع رجل الدابة؛ التبع الظل (mufradat)
- **B009** eski güneybatı Arabistan hükümdar unvanı — eski güneybatı Arabistan krallık geleneğinde hükümdar · aynı gelenekte birbirinin ardından gelen hükümdarlar
  التبابعة سموا بذلك لاتباع بعضهم في الملك بعضا (jamhara)؛ التبابعة ملوك اليمن الواحد تبع (sihah)؛ تبع الملك؛ كان تبع ملكا من الملوك؛ فيهم تبابعة (tahdhib)؛ تبع كانوا رؤساء سموا بذلك لاتباع بعضهم بعضا في الرياسة والسياسة؛ تبع ملك يتبعه قومه (mufradat)
- **B010** insanı her yerde izleyen dişi doğaüstü eşlikçi — bir insanı gittiği her yerde izleyen dişi doğaüstü varlık
  التابعة جنية تكون مع الإنسان تتبعه حيثما ذهب (ayn)؛ معه تابعة أي من الجن (sihah)
- **B011** kadınların peşinden cinsel amaçla gitmek [kalıp] — kadın kölelerle evlilik dışı ilişki kurmak veya bunun için peşlerinden gitmek · kadınların peşinden cinsel amaçla giden erkek
  فلان يتابع الإماء أي يزانيهن (ayn)؛ فلان تبع نساء أي يتبعهن؛ حدث نساء يحادثهن؛ وزير نساء يزورهن (tahdhib)
- **B012** sağlamlaştırmak, uyumlu olmak veya iyi duruma getirmek — işini sağlam ve ustaca yapmak · sözünü sağlam kurmak veya anlatıyı ustaca sürdürmek · beden yapısı düzgün ve orantılı · bilgisi kendi içinde tutarlı · otlak hayvanları besleyip semirtmek ve güzelleştirmek
  تابع الرجل عمله أي أتقنه وأحكمه (sihah)؛ تابعنا الأعمال أي أحكمناها وعرفناها؛ تابع فلان كلامه؛ فرس متتابع الخلق أي مستو؛ متتابع العلم إذا كان علمه يشاكل بعضه بعضا؛ تابع المرتع المال فتتابعت (tahdhib)

## ه و ي (root_001609): 42:15 أَهْوَآءَهُمْ

- **B001** hava ve boşluk; kalpte boşluk ve yüreksizlik — hava; boşluk veya aralık · kalpleri bomboş, kavrayışsız ve kararsızdır · yüreksiz, korkak ya da akılsız kimse
  الهَواء ممدود هو الجو (ayn)؛ قلبه هَواء (ayn)؛ هَواء الجو ممدود (jamhara)؛ الهَواء ما بين السماء والأرض وكل خال هواء (sihah)؛ الهَواء والخواء واحد (tahdhib)؛ الهَواء كل فرجة بين شيئين (tahdhib)؛ هوى صدره أي خلا (tahdhib)؛ الهوهاءة الضعيف الفؤاد الجبان (tahdhib)؛ الهَواء ما بين الأرض والسماء (mufradat)؛ أصل صحيح يدل على خلو وسقوط (maqayis)؛ أصله الهَواء بين الأرض والسماء سمي لخلوه (maqayis)
- **B002** yukarıdan düşme; yönlü gidiş, derin çukur, düşürme, ölüm ve yas bağlantıları — yukarıdan aşağı düştü veya indi · dipsiz uçurum; ateş azabının adı · derin çukur veya düşme yeri · topluluk derin çukura birbiri ardınca düştü
  هوى الطائر يهوي هويا (ayn)؛ هاوية من أسماء جهنم والهاوية كل مهواة لا يدرك قعرها (ayn)؛ هوى فلان أي مات (ayn)؛ هوى الشيء يهوي إذا خر من علو إلى سفل (jamhara)؛ هوى بالفتح يهوي هويا أي سقط إلى أسفل (sihah)؛ الهاوية اسم من أسماء النار والهاوية المهواة (sihah)؛ هوت أمه فهي هاوية أي ثاكلة (sihah)؛ هويت أهوي هويا إذا سقطت من علو إلى أسفل (tahdhib)؛ المؤتفكة أهوى أي أسقطها (tahdhib)؛ الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة (tahdhib)؛ الهوي سقوط من علو إلى سفل (mufradat)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ هوى الشيء يهوي سقط (maqayis)؛ تهاوى القوم في المهواة سقط بعضهم في إثر بعض (maqayis)
- **B003** eli ya da nesneyi hedefe yöneltmek; yukarıdan atmak — almak için elini ona uzattı · nesneyle işaret etti veya kılıçla vurdu · onu yukarıdan aşağı attı
  أهوى إليه فأخذه أي أهوى إليه يده (ayn)؛ أهوى إليه بيده ليأخذه (sihah)؛ أهويت بالشيء إذا أومأت به (sihah)؛ أهويت له بالسيف (sihah)؛ أهويت له بالسيف وغيره (tahdhib)؛ أهويته إذا ألقيته من فوق (tahdhib)؛ هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء (tahdhib)؛ أهوى إليه بيده ليأخذه كأنه رمى إليه بيده إذا أرسلها (maqayis)
- **B004** benliğin sevgi ve isteğe yönelmesi — benliğin sevgiye veya isteğe yönelmesi · sevdi, gönlü ona yöneldi · ötekinden daha çok sevilen · çeşitli kişisel eğilimlerin izleyicileri
  الهَوَى مقصور الحب (ayn)؛ هوى النفس مقصور (jamhara)؛ الهَوَى مقصور هوى النفس والجمع الأهواء (sihah)؛ هوى بالكسر يهوى هوى أي أحب (sihah)؛ هذا الشيء أهوى إلى من كذا أي أحب إلي (sihah)؛ أفئدة من الناس تهوى إليهم يقول تريدهم (tahdhib)؛ وتهوي إليهم تهواهم (tahdhib)؛ الهَوَى مقصور هوى الضمير (tahdhib)؛ أهل الأهواء واحدها هوى (tahdhib)؛ الهَوَى ميل النفس إلى الشهوة (mufradat)؛ الهوى هوى النفس فمن المعنيين جميعا (maqayis)؛ هويت أهوى هوى (maqayis)
- **B005** ayartıp şaşkınlığa ve isteklerinin peşine sürüklemek [kalıp] — ayartıcı güçler onu yoldan çıkarıp şaşkınlığa sürükledi
  استهوته الشياطين فهو حيران هائم (ayn)؛ استهواه الشيطان أي استهامه (sihah)؛ استهوته الشياطين فهو حيران هائم (tahdhib)؛ كالذي زينت له الشياطين هواه حيران (tahdhib)؛ استهوته الشياطين هوت به وأذهبته (tahdhib)؛ استهوته الشياطين أي حملته على اتباع الهوى (mufradat)
- **B006** uzun bir zaman veya gecenin bir bölümü — uzun bir zaman · gecenin bir bölümü veya dilimi
  الهوي الملي الحين الطويل من الزمان (ayn)؛ مر هوي من الليل أي قطعة منه وكذلك تهواء من الليل (jamhara)؛ مضى هوى من الليل أي هزيع منه (sihah)؛ الهوي الملي الحين الطويل من الزمان (tahdhib)
- **B007** yaranın açılması veya gövdenin boşalıp oyuklaşması [kalıp] — saplama yarası açılıp genişledi · böğür bölgesi zayıflıktan oyuklaşıp açıldı
  هوت الطعنة تهوى فتحت فاها (sihah)؛ هوى بين الكلى والكراكر (sihah)؛ هوت الطعنة إذا فتحت فاها (tahdhib)؛ خلا وانفتح من الضمر (tahdhib)؛ هوى صدره يهوي هواء إذا خلا (tahdhib)؛ هوت الطعنة فتحت فاها تهوى وهو من الهواء الخالي (maqayis)
- **B008** hızlı yönlü ilerleme, atılımlı koşu ve sert yol alma — hızlı veya güçlü ilerleme · yırtıcı kuş hızla daldı veya deve güçlü biçimde koştu · sert ve hızlı yol alma · çeşitli yol alış biçimleri
  الهوي في السير إذا مضى (sihah)؛ المهاواة شدة السير (sihah)؛ الهوي في السير إذا مضى (tahdhib)؛ الهوي السريع إلى أسفل والهوي السريع إلى فوق (tahdhib)؛ هوت العقاب إذا انقضت (tahdhib)؛ هوت الناقة تهوي إذا عدت عدوا أرفع العدو (tahdhib)؛ الهواهي ضروب من السير (tahdhib)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ الهوي ذهاب في انحدار والهوى في الارتفاع (maqayis)؛ شدة السير لما في ذلك من الترامي بالأبدان عند السير (maqayis)
- **B009** karşılıklı inatlaşma ve çekişme — karşılıklı inatlaşma ve çekişme
  المهاواة الملاجة (sihah)؛ المهاواة فذكر أبو عمرو أنها الملاجة (maqayis)؛ أما الملاجة فلأن كل واحد منهما يحب هوى صاحبه (maqayis)
- **B010** asılsız ve boş sözler — asılsız ve boş sözler
  الهواهي الباطل واللغو من القول (sihah)؛ الهواهي الأباطيل (tahdhib)

## ق و ل (root_001272): 42:15 وَقُلْ, 42:23 قُل, 42:24 يَقُولُونَ, 42:44 يَقُولُونَ, 42:45 وَقَالَ

- **B001** söze dökme — sözü sesle dile getirmek · söylenmiş söz veya sözlü ifade · söylenmiş söz için kullanılan adlar
  القول من النطق (maqayis)؛ قال يقول قولا وقولة ومقالا ومقالة (sihah)؛ القول والقيل واحد (mufradat)؛ المركب من الحروف المبرز بالنطق (mufradat)؛ القيل من القول اسم (ayn)
- **B002** konuşma organı — konuşma organı olan dil
  المقول اللسان (maqayis;ayn;sihah)
- **B003** çok sözlü kişi — çok konuşan, dili güçlü kişi
  رجل قولة وقوال كثير القول (maqayis)؛ رجل تقوالة أي منطيق وقوال وقوالة أي كثير القول (ayn)؛ رجل مقول ومقوال وقولة وقوال وتقوالة أي لسن كثير القول (sihah)
- **B004** sözü geçen yönetici unvanı — sözü geçen yerel hükümdar unvanı · bu unvanın çoğul adları · bu unvanın kadın için kullanılan biçimi
  المقول بلغة أهل اليمن القيل وهم المقاولة والأقيال والأقوال والواحد القيل (ayn)؛ القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة (sihah)؛ كأنه الذي له قول أي ينفذ قوله (sihah)
- **B005** yalan söyleme veya isnat etme [kalıp] — olmayan bir şeyi söyledi · ona yalan isnat etti · bana söylemediğim şeyi yükledi
  تقول باطلا أي قال ما لم يكن (ayn)؛ قولتني ما لم أقل وأقولتني ما لم أقل أي ادعيته علي (sihah)؛ تقول عليه أي كذب عليه (sihah)
- **B006** sözü üzerine alma [kalıp] — iyi ya da kötü bir sözü kendi üzerine aldı
  اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر (ayn)
- **B007** dolaşımdaki söz — hakkında iyi veya kötü söz yayıldı · insanlar arasında yayılmış söz · dedikodu ve çokça dönen laf
  انتشرت له قالة حسنة أو قبيحة في الناس (ayn)؛ القالة القول الفاشي في الناس (ayn)؛ كثر فيه القيل والقال (ayn)؛ كثرت قالة الناس (sihah)؛ كثر القيل والقال (sihah)
- **B008** oyun sopası — oyunda küçük parçaya vurulan tahta sopa
  القال الخشبة التي تضرب بها القلة (sihah)
- **B009** müzakere etme [kalıp] — bir iş hakkında karşılıklı görüştük
  قاولته في أمره وتقاولنا أي تفاوضنا (sihah)
- **B010** hükmünü dayatma [kalıp] — üzerinde hüküm yürüttü, tahakküm etti
  اقتال عليه تحكم (sihah)
- **B011** sanma işlevli söyleme — söyleme fiilini sanmak gibi kurmak
  العرب تجري تقول وحدها في الاستفهام مجرى تظن في العمل (sihah)؛ بنو سليم يجرون متصرف قلت في غير الاستفهام أيضا مجرى الظن (sihah)
- **B012** içte kalmış söz [kalıp] — içte tasarlanıp henüz söylenmemiş anlam
  المتصور في النفس قبل الإبراز باللفظ قول (mufradat)؛ في نفسي قول لم أظهره (mufradat)
- **B013** görüş benimseme [kalıp] — bir görüş veya mezhebi benimsedi
  للاعتقاد نحو فلان يقول بقول أبي حنيفة (mufradat)
- **B014** durumuyla belli etme [kalıp] — durumuyla yeter olduğunu belli etti
  للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني (mufradat)
- **B015** içten önemseme [kalıp] — bir şeye içten önem verdi
  للعناية الصادقة بالشيء كقولك فلان يقول بكذا (mufradat)
- **B016** teknik tanım [kalıp] — bir şeyin teknik tanımı
  يستعمله المنطقيون في معنى الحد فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما (mufradat)
- **B017** içe doğan anlam — içe doğan anlamın söz diye adlandırılması
  في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا (mufradat)

## ECHO ق ل ل (root_001251): for 42:15 وَقُلْ, 42:23 قُل, 42:24 يَقُولُونَ, 42:44 يَقُولُونَ, 42:45 وَقَالَ: withheld observed target; not identity

- **B001** azlık — az şey; azlık · azlık ve yetersizlik; yoksulluk ve düşüklük · az; az sayıda veya az miktarda · azalmak; az olmak · gözünde az göstermek · yoksullaşmak · az saymak; az görmek · hiç; ne azı ne çoğu · pek seyrek; hemen hemen hiç · yoksulluğa ve aşağılanmaya uğrasın · hiç malı olmamak · kendisi de ailesi de tanınmayan adam
  القل القليل؛ رماه الله بالقل والذل أي بالقلة والذلة (jamhara)؛ شيء قليل وجمعه قلل؛ قل الشيء يقل قلة؛ قلله في عينه؛ أقل افتقر؛ استقله عده قليلا (sihah)؛ قل الشيء يقل قلة فهو قليل وقلال؛ القل من الرجال الخسيس الدنيء؛ قليلة ولا كثيرة؛ قليلا ما يؤمنون؛ قاللت لفلان؛ تقاللت ما أعطاني (tahdhib)؛ القلة والكثرة يستعملان في الأعداد؛ يكنى بالقلة عن الذلة؛ يكنى بها تارة عن العزة؛ قليل يعبر به عن النفي (mufradat)
- **B002** bir şeyin tepesi veya başı — dağın tepesi; doruk · bir şeyin tepesi veya başı · insanın başı · sap ucunda topuzu bulunan kılıç
  القلة قلة الجبل وهي القطعة تستدير في أعلاه وهي القنة (jamhara)؛ القلة أعلى الجبل؛ قلة كل شيء أعلاه؛ رأس الإنسان قلة (sihah)؛ قلة كل شيء رأسه؛ قلة الجبل أعلاه؛ قبيعة السيف قلته؛ سيف مقلل (tahdhib)؛ قلة الجبل شعفه (mufradat)
- **B003** büyük küp — büyük küp; iri kap · belirli bir bölgenin iri küpleri · iki büyük küp veya bunların aldığı miktar
  القلة التي جاءت في الحديث مثل قلال هجر هي جرار عظام (jamhara)؛ القلة إناء للعرب كالجرة الكبيرة؛ قلال هجر شبيهة بالحباب (sihah)؛ قلتين يعني هذه الحباب العظام واحدتها قلة؛ قلال هجر؛ القلة منها تأخذ مزادة من الماء (tahdhib)؛ القلة ما أقله الإنسان من جرة وحب (mufradat)
- **B004** yük kaldırma, yükselme ve yola koyulma — küpü taşıyabilmek · bir şeyi taşımak; yüklenmek · ağır bulutları taşımak · uçuşa kalkmak; havalanmak · yüklenip yola çıkmak · yükselmek
  أقل الجرة أطاق حملها؛ استقلت السماء ارتفعت؛ استقل القوم مضوا وارتحلوا (sihah)؛ أقل الرجل الشيء واستقله إذا احتمله؛ استقل الطائر إذا نهض للطيران؛ استقل النبات أناف؛ استقل القوم إذا احتملوا ظاعنين؛ أقلت سحابا ثقالا أي حملت؛ قل إذا رفع وقل إذا علا (tahdhib)؛ أقلت سحابا ثقالا أي احتملته؛ أقللت كذا وجدته قليل المحمل (mufradat)
- **B005** korku veya öfkeden titreme — korku veya öfkeden doğan titreme · korku veya öfkeden titremeye tutulmak · öfkeden titremek
  القل الرعدة والانتفاض؛ أخذ فلانا القل إذا أخذته رعدة من فزع (jamhara)؛ القل بالكسر شبه الرعدة؛ أخذه قل من الغضب (sihah)؛ القل الرعدة؛ أخذه قل إذا أرعد من الغضب؛ إذا غضب قد استقل (tahdhib)
- **B006** oynatma ve kararsızca sallanma — sallanma, yerinde duramama ve hareket sesi · sallayıp oynatmak · sallanmak; yerinde duramamak · çevik; hızlı
  قلقل أي صوت وهو حكاية؛ قلقله قلقلة وقلقالا فتقلقل أي حركه فتحرك واضطرب (sihah)؛ القلقلة والتقلقل قلة الثبوت في المكان؛ يتقلقل في موضعه؛ القلق ألا يستقر الشيء في مكان واحد (tahdhib)؛ تقلقل الشيء إذا اضطرب؛ تقلقل المسمار؛ القلقلة حكاية صوت الحركة (mufradat)

## ء م ن (root_000054): 42:15 ءَامَنتُ, 42:18 يُؤْمِنُونَ, 42:18 ءَامَنُوا۟, 42:22 ءَامَنُوا۟, 42:23 ءَامَنُوا۟, 42:26 ءَامَنُوا۟, 42:36 ءَامَنُوا۟, 42:45 ءَامَنُوٓا۟, 42:52 ٱلْإِيمَٰنُ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ن ز ل (root_001492): 42:15 أَنزَلَ, 42:17 أَنزَلَ, 42:27 يُنَزِّلُ, 42:28 يُنَزِّلُ

- **B001** aşağı inme veya bir yere konaklama — yüksekten inmek veya bir yerde konaklamak · yağmurun gökten yağması · bir yerde yükünü bırakıp konaklamak · ağır ağır inme
  هبوط شيء ووقوعه؛ نزل عن دابته نزولا؛ نزل المطر من السماء نزولا (maqayis)؛ نزل فلان عن الدابة أو من علو إلى سفل (ayn)؛ المنزل النزول وهو الحلول؛ التنزل النزول في مهلة (sihah)؛ النزول في الأصل هو انحطاط من علو؛ نزل في مكان كذا حط رحله (mufradat)
- **B002** Tanrısal iyilik, ceza veya bildiriyi insanlara ulaştırma — başkasını indirmek veya bir şeyi yerine ulaştırmak · Tanrı'nın iyilikleri ve cezaları insanlara vermesi · bölüm bölüm ve yinelenerek bildirme · Tanrısal esirgemenin onlara erişmesi
  تنزلت الرحمة عليهم (tahdhib)؛ إنزال الله تعالى نعمه ونقمه على الخلق وإعطاؤهم إياها؛ إما بإنزال الشيء نفسه كإنزال القرآن وإما بإنزال أسبابه؛ التنزيل يختص بما أنزل مفرقا ومرة بعد أخرى (mufradat)
- **B003** konaklama yeri veya bulunulan derece — konaklama yeri, ev veya su başı · derece veya konum · birinin derecesini düşürmek · topluluğu konaklama yerlerine yerleştirmek
  مكان نزل ينزل فيه كثيرا؛ وجدت القوم على نزلاتهم أي منازلهم (maqayis)؛ المنزل المنهل والدار؛ المنزلة المرتبة؛ استنزل فلان أي حط عن مرتبته (sihah)؛ نزلت القوم أي أنزلتهم المنازل؛ نزل فلان غيره أي قدر لها المنازل (tahdhib)؛ أنزلني منزلا مباركا؛ نزل في مكان كذا حط رحله (mufradat)
- **B004** bir şeyi uygun yerine veya sırasına koyma — bir şeyi düzenleyip uygun yerine veya sırasına koyma
  التنزيل ترتيب الشيء ووضعه منزله (maqayis)؛ التنزيل أيضا الترتيب (sihah)؛ التنزيل يختص بالموضع الذي يشير إليه إنزاله مفرقا ومرة بعد أخرى (mufradat)
- **B005** konuk için hazırlanan yiyecek ve ağırlama payı — konuğa hazırlanan yiyecek veya yol azığı · ürün geliri, fazlalık veya bağış · konuk · birini konuk etmek · topluluğun geçim payları · bol ve bereketli yemek · bol veren ve eli açık olan · bir araya gelmiş pay
  النزل ما يهيأ للنزيل؛ طعام ذو نزل؛ النزيل الضيف (maqayis)؛ النزل ما يهيأ للقوم والضيف؛ النزل ريع ما يزرع (ayn)؛ النزل ما يهيأ للنزيل؛ النزل أيضا الريع؛ النزيل الضيف (sihah)؛ حسن النزل أي الضيافة؛ أنزال القوم أرزاقهم؛ أقمت لهم غذاءهم وما يصلح معه أن ينزلوا عليه؛ النزل الريع والفضل (tahdhib)؛ النزل ما يعد للنازل من الزاد؛ أنزلت فلانا أضفته؛ ذو نزل له ريع؛ حظ نزل مجتمع تشبيها بالطعام النزل (mufradat)
- **B006** başa gelen ağır sıkıntı — insanların başına gelen ağır sıkıntı veya felaket
  النازلة الشديدة من شدائد الدهر تنزل (maqayis)؛ النازلة الشديدة من شدائد الدهر تنزل بالقوم وجمعها النوازل (ayn)؛ النازلة الشديدة من شدائد الدهر تنزل بالناس (sihah;tahdhib)؛ يعبر بالنازلة عن الشدة وجمعها نوازل (mufradat)
- **B007** savaşmak için karşı karşıya inme — savaşta karşı karşıya gelme · savaşmak üzere inin
  النزال في الحرب أن يتنازل الفريقان؛ نزال كلمة توضع موضع انزل (maqayis)؛ النزال المنازلة في الحرب أن ينزلا معا فيقتتلا؛ نزال أي انزلوا للحرب (ayn)؛ نزال بمعنى انزل؛ النزال في الحرب أن يتنازل الفريقان (sihah)؛ النزال في الحرب المنازلة (mufradat)
- **B008** hac yolculuğunda Mina'ya varma — hac yapmak veya Mina'ya gelmek · topluluğun Mina'ya gelmesi
  يعبرون عن الحج بالنزول؛ نزل إذا حج؛ نزلنا أتينا منى (maqayis)؛ نزل القوم إذا أتوا منى (sihah;tahdhib)؛ نزل فلان إذا أتى منى (mufradat)
- **B009** erkeğin dışarı çıkan üreme sıvısı — erkeğin dışarı çıkan üreme sıvısı · cinsel birleşme sırasında boşalmak · kadının erkeğin boşalmasını istemesi
  النزالة ماء الرجل (maqayis)؛ النزالة بالضم ماء الرجل وقد أنزل (sihah)؛ أنزل الرجل ماءه إذا جامع والمرأة تستنزل ذلك (tahdhib)؛ النزالة والنزل يكنى بهما عن ماء الرجل إذا خرج عنه (mufradat)
- **B010** bir kez inme — bir kez inme · bir kez daha · soğuk algınlığına benzer geçici rahatsızlık
  النزلة المرة الواحدة؛ ولقد رآه نزلة أخرى أي مرة أخرى (ayn)؛ النزلة كالزكام؛ ولقد رآه نزلة أخرى قالوا مرة أخرى (sihah)؛ النزلة المرة الواحدة من النزول (tahdhib)
- **B011** akış, konaklanma veya biçim özelliğiyle nitelenen yer [kalıp] — az yağmurda bile hızla su akıtan sert arazi · sık konaklanan, geniş uzak, otlaklı veya suyu çabuk akan yer · dar vadi
  مكان نزل ينزل فيه كثيرا (maqayis)؛ أرض نزلة ومكان نزل إذا كانت تسيل من أدنى مطر لصلابتها (sihah)؛ طعام نزل وأرض نزلة ومكان نزل سريع السيل؛ مكان نزل ينزل فيه كثيرا؛ مكان نزل واسع بعيد؛ مكان نزل إذا كان محلالا مربا؛ النزل من الأودية الضيق منها (tahdhib)

## ع د ل (root_000991): 42:15 لِأَعْدِلَ

- **B001** hükümde hak gözetme ve güvenilir doğruluk — hükümde hak gözetme ve haksızlığın karşıtı · hakka göre hükmeden kimse · sözüne, hükmüne ve tanıklığına güvenilen kimse · söz ve hükümde doğruluk ve güvenilirlik hali · hak gözeten hüküm ve yönetim düzeni · tanıkların güvenilirliğini onaylama
  العدل نقيض الجور (maqayis;sihah;tahdhib); العدل الحكم بالحق (ayn;tahdhib); رجل عدل مرضي قوله وحكمه (ayn;tahdhib); العدل التقسيط على سواء (mufradat)
- **B002** eşlik ve denklik — eş, denk veya benzer olan şey · birini ötekine denk tutmak · gözümüzde hiçbir şey senin yerini tutmaz
  كل ذلك من المعادلة وهي المساواة (maqayis); عدل الشيء نظيره (ayn); العدل المثل (sihah;tahdhib); لفظ يقتضي معنى المساواة (mufradat)
- **B003** denk kurtulma karşılığı — kurtulma karşılığı veya eşdeğer değer · ondan hiçbir kurtulma karşılığı kabul edilmez · bunun yerine aynı değerde oruç
  العدل قيمة الشيء وفداؤه (maqayis); العدل الفداء (ayn;sihah); العدل الفدية (tahdhib); ما يعادل من الصيام الطعام (mufradat)
- **B004** karşılıklı dengeli yük — hayvanın iki yanındaki denk yüklerden biri · hayvanın iki yanındaki dengeli iki yük · taşıtta veya ağırlıkta denk olan eş · heybeyi hayvanın bir yanına yükleyip öteki yana denklemek
  العدلان حملا الدابة سميا بذلك لتساويهما (maqayis); العدلان الحملان على الدابة من جانبين (ayn); واحد الأعدل عدل (sihah;tahdhib); العديل الذي يعادلك في المحمل (maqayis;ayn;tahdhib); عدلت الجوالق على البعير (tahdhib)
- **B005** düzeltip dengeleme — bir şeyi düzeltip dengeli hale getirmek · düzelip dengelenmek · düzgün, dengeli veya ılımlı · organları uyumlu, güzel yapılı dişi deve
  عدلت الشيء أقمته حتى اعتدل (maqayis;ayn;sihah;tahdhib); يوم معتدل إذا تساوى حره وبرده (maqayis); المعتدلة من النوق الحسنة المتفقة الأعضاء (maqayis;tahdhib); أيام معتدلات طيبات (mufradat)
- **B006** yönünden çevirme ve sapma — yoldan ya da doğrudan sapmak · bir şeyi yönünden çevirip eğmek · kıvrılmak, eğrilmek veya yön değiştirmek · erkek devenin çiftleşmeyi bırakıp sürüden uzaklaşması
  الأصل الآخر في الاعوجاج عدل وانعدل (maqayis); العدل أن تعدل الشيء عن وجهه فتميله (ayn;tahdhib); عدل عن الطريق جار (sihah); عدل عن الحق إذا جار عدولا (mufradat)
- **B007** Tanrı'ya başka bir varlığı eş tutma — Tanrı'ya başka bir varlığı eş tutmak · Tanrı'ya başka bir varlığı eş tutup ona tapan kimse
  المشرك يعدل بربه كأنه يسوي به غيره (maqayis); العادل المشرك الذي يعدل بربه (ayn;sihah); العدل في الإشراك (tahdhib); يجعلون له عديلا (mufradat)
- **B008** iki seçenek arasında kararsız kalıp üstün olanı tartma — iki seçenek arasında tartıp hangisinin üstün olduğuna bakmak · iki seçenek arasında kararsızlık ve kuşku
  يعادل أمره عدالا يميل بين أمرين (sihah); المعادلة الشك في الأمرين (tahdhib); أنا في عدال من هذا الأمر أي في شك منه (tahdhib); عادل بين الأمرين إذا نظر أيهما أرجح (mufradat)

## ع م ل (root_001046): 42:15 أَعْمَٰلُنَا, 42:15 أَعْمَٰلُكُمْ, 42:22 وَعَمِلُوا۟, 42:23 وَعَمِلُوا۟, 42:26 وَعَمِلُوا۟

- **B001** bilerek yapılan iş veya eylem — bilerek yapılan iş veya eylem · iş yapan kimse · kendisi için çalışmak veya işe koyulmak · iş veya uğraş · işte kullanılan sığırlar · iyi ve kötü davranışlar
  أصل واحد صحيح وهو عام في كل فعل يفعل (maqayis); عمل عملا فهو عامل (ayn;sihah;tahdhib); كل فعل يكون من الحيوان بقصد (mufradat); الأعمال الصالحة والسيئة (mufradat)
- **B002** işe koşmak veya kullanmak — onu çalıştırdı · onu kullandı veya çalıştırdı · ondan çalışmasını istedi · görüşünü, sözünü veya mızrağını kullandı · kerpici yapıda kullandı · zihnini işletip düşündü
  يستعمل غيره ويعمل رأيه أو كلامه أو رمحه؛ والبناء يستعمل اللبن (maqayis); أعمله غيره واستعمله بمعنى؛ واستعمله أيضا أي طلب إليه العمل (sihah); أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه (tahdhib)
- **B003** işe görevli kılma veya görev üstlenme — bağışları toplayan görevliler · bağış işi görevlisi · resmi bir işi üstlendi · birine iş görevi verme · bir kimseyi bir şehirde görevli kılmak
  العاملين عليها هم السعاة الذين يأخذون الصدقات (tahdhib); استعمل فلان إذا ولي عملا من أعمال السلطان (tahdhib); التعميل تولية العمل (sihah); العاملين عليها هم المتولون على الصدقة (mufradat)
- **B004** iş ücreti — iş karşılığı ücret veya pay · iş ücreti
  العمالة أجر ما عمل (maqayis); العمالة بالضم رزق العامل (sihah); العمالة رزق العامل (tahdhib); العملة والعمالة أجر العمل (tahdhib); العمالة أجرته (mufradat)
- **B005** karşılıklı işlem — karşılıklı işlem veya alışveriş ilişkisi · bir kimseyle alışveriş veya benzeri işlem yaptı
  المعاملة مصدر من قولك عاملته وأنا أعامله معاملة (maqayis); عاملت الرجل أعامله معاملة في المبايعة وغيرها (tahdhib)
- **B006** el işçileri — elleriyle çalışan işçi topluluğu
  العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه (maqayis); العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره (tahdhib)
- **B007** zahmete girmek [kalıp] — kendini yorma · ihtiyacın için zahmete gireceğim · zahmet etme
  لا تتعمل في أمرك ذا كقولك لا تتعن (tahdhib); سوف أتعمل في حاجتك أي أتعنى (tahdhib); لا تعمل أي لا تتعن (tahdhib)
- **B008** işe yatkın ve dayanıklı — işe yatkın üstün dişi deve · işe nispet edilen dişi deve · işe yatkın adam · işe yatkın çalışkan adam · işe yatkın, güçlü ve üstün dişi deve
  اليعملة من الإبل اسم لها اشتق من العمل (maqayis); رجل عمل بكسر الميم أي مطبوع على العمل؛ ورجل عمول؛ اليعملة الناقة النجيبة المطبوعة على العمل (sihah); ناقة عملة بينة العمالة مثل اليعملة إذا كانت فارهة (tahdhib); اليعملة مشتقة من العمل (mufradat)
- **B009** mızrak ucunun alt bölümü — mızrağın sivri ucuna yakın ön gövde bölümü · mızrağın ucuna yakın gövde bölümü
  عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره (maqayis); عامل الرمح ما يلي السنان وهو دون الثعلب (sihah); عامل الرمح صدره دون السنان ويجمع عوامل (tahdhib); عامل الرمح ما يلي السنان (mufradat)
- **B010** iş gören beden parçası [kalıp] — hayvanın ayakları · uzağı gören göz
  عوامل الدابة قوائمه واحدها عاملة (tahdhib); وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر (tahdhib)
- **B011** işlek yol [kalıp] — işlek ve belirgin yol
  طريق معمل أي لحب مسلوك (sihah)
- **B012** yaya yolcular [kalıp] — yaya giden yolcular
  المسافرون إذا مشوا على أرجلهم يسمون بني العمل (tahdhib)

## ح ج ج (root_000295): 42:15 حُجَّةَ, 42:16 يُحَآجُّونَ, 42:16 حُجَّتُهُمْ

- **B001** bir hedefe yönelme; kimi kullanımda yineleyerek veya dinsel uygulama için gitme — kutsal yapıya dinsel uygulamaları yerine getirmek için yönelme · birini amaçlayarak ona gitme veya onu tekrar tekrar ziyaret etme · birini amaçlayıp sık sık yanına giderek ona saygı gösterme · bize geldi · kutsal yapıya dinsel uygulama için yönelen kişi · kutsal ziyaretçiler topluluğu · kutsal ziyareti çok kez yapan kişi · kutsal ziyaretçiler · birini kutsal ziyarete gönderme
  أصل الحج القصد (maqayis;jamhara)؛ الحج كثرة القصد إلى من يعظم (ayn)؛ حججت البيت أحجه حجا (sihah;tahdhib)؛ أصل الحج القصد للزيارة (mufradat)؛ الحجيج الحاج (maqayis;sihah)؛ الحاج أسمعت (maqayis)
- **B002** ana ve belirgin yol; ayrıca kıvrımlı veya oyuklu yol türleri — ana ve açık yol · yer yer düzleşip yer yer kıvrılan yol · yüzeyinde oyuklar bulunan yollar
  المحجة جادة الطريق (maqayis;sihah)؛ المحجة قارعة الطريق الواضح (ayn)؛ المحجة قارعة الطريق (tahdhib)؛ الحجوج الطريق يستقيم مرة ويعوج أخرى (tahdhib)؛ الحجج الطرق المحفرة (tahdhib)
- **B003** açıklayıcı kanıt ve onunla tartışmada üstün gelme — savın doğruluğunu gösteren kanıt · kanıtlarla tartışma · tartışmada kanıtla alt etme · karşılıklı kanıt ileri sürerek tartışma · çok tartışan ve sürekli kanıt ileri süren kişi · direndi; sonunda ya kanıtla üstün geldi ya da kutsal ziyarete yöneldi
  الحجة مشتقة من هذا لأنها تقصد أو بها يقصد الحق المطلوب (maqayis)؛ الحجة وجه الظفر عند الخصومة (ayn;tahdhib)؛ الحجة من الاحتجاج (jamhara)؛ الحجة البرهان (sihah)؛ حاجه فحجه أي غلبه بالحجة (sihah)؛ الحجة الدلالة المبينة للمحجة (mufradat)
- **B004** baş yarasını sondalayıp ölçme, tedavi etme ve kırık kemiği çıkarma — baş yarasını ince bir araçla sondalayıp ölçme veya tedavi etme · yaradaki kırık kemiği kesip çıkarma · tedavi edilmiş baş yarası veya kanın beyinle karıştığı yara · baş yarasını sondalamaya yarayan ince araç
  حججت الشجة وذلك إذا سبرتها بالميل (maqayis)؛ الحجيج ما قد عولج من الشجة (ayn)؛ حج العظم يحجه حجا إذا قطعه من الجرح فاستخرجه (jamhara)؛ حججته حجا فهو حجيج إذا سبرت شجته (sihah)؛ حججت الشجة إذا سبرتها (tahdhib)؛ سبر الجراحة حجا (mufradat)
- **B005** yıl veya kutsal ziyaret dönemi; ayrıca bu ziyaretin yapıldığı ay — yıl veya kutsal ziyaret dönemi · kutsal ziyaretin yapıldığı ay
  الحجة وهي السنة (maqayis)؛ الحجة ههنا الموسم (ayn)؛ الحجة السنة (jamhara)؛ الحجة السنة والجمع الحجج (sihah)؛ ذو الحجة شهر الحج (sihah;tahdhib)؛ في كل حجة أي في كل سنة (tahdhib)
- **B006** kulak memesi ya da deliği; ayrıca kulağa asılan boncuk veya inci — kulak memesi veya kulak memesindeki delik · kulağa asılan boncuk veya inci
  الحجة شحمة الأذن (ayn;sihah;tahdhib)؛ الحجة خرزة أو لؤلؤة تعلق في الأذن (maqayis;jamhara;tahdhib)؛ ثقبة شحمة الأذن (tahdhib)؛ جاجة بجيمين وهو غلط (jamhara)
- **B007** gözü çevreleyen kemik çerçeve; benzer kenarlar ve bu çerçevenin iriliği veya başın sertliği — gözü çevreleyen yuvarlak kemik · göz çevresi kemiği iri olan veya başı sert olan · güneşin sınırı ve dağın iki yanı · kayanın içe göçük bölümü
  الحجاج العظم المستدير حول العين (maqayis;ayn;sihah;tahdhib)؛ للعظيم الحجاج أحج (maqayis)؛ المكان المتكاهف من الصخرة حجاج (maqayis)؛ حجاج الشمس حاجبها وحجاجا الجبل جانباه (tahdhib)؛ رأس أحج صلب (tahdhib)
- **B008** ilerledikten sonra geri çekilme, güçsüz kalma, olumsuz kalıpta kuşku duymama ve söyleyeceğini tutma — ilerledikten sonra geri çekilme · güçsüz kalan kişi · bu konuda hiç kuşku duymuyorum · içindekini söylemeye niyetlenip susma
  الحجحجة النكوص (maqayis;ayn;sihah)؛ المحجحج العاجز (maqayis)؛ لا أحجحج أي لا أشك (maqayis)؛ حجحج الرجل إذا أراد أن يقول ما في نفسه ثم أمسك (sihah)
- **B009** Tanrı'yı anarak yapmayacağına ant içme — Tanrı'yı anarak bunu yapmayacağına ant içme
  وحجة الله لا أفعل؛ يمين للعرب (sihah)

## ص ي ر (root_000897): 42:15 ٱلْمَصِيرُ, 42:53 تَصِيرُ

- **B001** bir durumdan ötekine geçme, bir sonuca varma veya bir şeyi o duruma getirme — olmak, bir duruma dönüşmek · bir yere ya da sonuca varmak · bir şeyi belirli bir duruma getirmek · varış yeri, son veya sonuç · oluş, bir duruma geçiş · işin sonu, varacağı sonuç · bir işin sonuçlanma eşiğinde
  صار يصير صيرا وصيرورة؛ صير كل شيء مصيره؛ صيور الأمر آخره؛ صار الشيء كذا؛ صرت إلى فلان مصيرا؛ صيرته أنا كذا أي جعلته؛ صار إلى كذا انتهى إليه؛ صار عبارة عن التنقل من حال إلى حال
- **B002** bir işin sonuçlanma eşiği veya dağın başı — bir işin sonuçlanma eşiğinde · dağın başı, zirvesi · tepe başındaki dairesel yapı veya taş yığını
  على صير أمر أي إشراف من قضائه؛ صير الأمر شرفه؛ على صير أمر إذا كان على إشراف من قضائه؛ على صير أمر أي على طرف منه؛ صارة الجبل رأسه؛ الصيرة على رأس القارة
- **B003** sığır veya koyun ağılı — sığır veya koyun ağılı · ağıllar
  الصير كالحظائر يتخذ للبقر والواحدة صيرة؛ صيرة البقر موضع يتخذ من أغصان الشجر والحجارة كالحظيرة؛ الصيرة حظيرة الغنم وجمعها صير؛ الصيرة الحظيرة للغنم
- **B004** yarık açma, kesme, yana eğme veya boyun bükme — yarık, özellikle kapı aralığı · kapıdaki bakma yarığı · kesmek veya yana eğmek · insanların boyunlarını büken kimse
  الصير وهو الشق؛ الصير الشق؛ صير باب؛ صاره يصيره لغة في يصوره أي قطعه وكذلك إذا أماله؛ الصير شق الباب؛ الصائر الملوي أعناق الرجال؛ الصير الشق وهو المصدر
- **B005** niteliği açıklanmamış bir yiyecek türü — niteliği açıklanmamış bir yiyecek türü
  الصير وهو شيء يقال له الصحناة؛ الصير شبه الصحناء؛ الصير أيضا الصحناة؛ الصير فذاق منه؛ تفسيره في الحديث أنه الصحناء
- **B006** babasına çekmek [kalıp] — babasına çekmek
  تصير فلان أباه إذا نزع إليه في الشبه؛ تصير فلان أباه إذا نزع إليه في الشبه؛ تصير فلان أباه وتقيضه إذا نزع إليه في الشبه
- **B007** mezar ya da konak yeri; su başına varma veya konak yerine dönme — mezar, ölünün karar yeri · konak yeri, menzil · su başına varmak · konak yerine dönmüş topluluk veya konak yerine dönüş
  صيره قبره؛ هذا صير فلان أي قبره؛ أين مصيركم أي أين منزلكم؛ صار الرجل يصير إذا حضر الماء؛ الصير رجوع المنتجعين إلى محاضرهم
- **B008** topluluk, grup — topluluk, grup
  الصير الجماعة
- **B009** zilin çınlaması — zil sesi, çınlama
  الصيار صوت الصنج؛ رنات الصيار

## ج و ب (root_000273): 42:16 ٱسْتُجِيبَ, 42:26 وَيَسْتَجِيبُ, 42:38 ٱسْتَجَابُوا۟, 42:47 ٱسْتَجِيبُوا۟

- **B001** delip geçerek kesme — bir şeyi delip geçecek biçimde kesmek · kayayı oyarak kesmek · gömleğin yaka açıklığı · gömleğin yakasını kesip açmak · gömleğe yaka açıklığı açmak · kesme veya yama yapma aleti · bir yeri kazıp oymak · ceylan boynuzunun deriyi delerek çıkması
  خرق الشيء (maqayis)؛ قطعك الشيء كما يجاب الجيب (ayn)؛ جبت الشيء أجوبه إذا قطعته جوبا (jamhara)؛ جاب يجوب جوبا إذا خرق وقطع (sihah)؛ اجتاب احتفر (tahdhib)؛ جاب قرنها الجلد فطلع (tahdhib)؛ وثمود الذين جابوا الصخر بالواد (mufradat)
- **B002** bir yeri baştan başa geçme — yeri ve ülkeleri baştan başa geçmek · bir yeri baştan başa geçmek · ülkeleri sürekli dolaşan kimse · bütün gece yol alan kimse · karanlığı yarıp ilerlemek · ülkeden ülkeye taşınan haber · uzak yerlerden gelen şaşırtıcı haberler
  جبت الأرض جوبا فأنا جائب وجواب؛ خبر يجوب البلاد (maqayis)؛ جبت المفازة أي قطعتها؛ الجوائب الغرائب من الأخبار (ayn)؛ جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها؛ جائبة خبر يجوب الأرض من بلد إلى بلد (sihah)؛ جبت البلد أجوبه جوبا إذا قطعته؛ رجل جواب إذا كان قطاعا للبلاد (tahdhib)؛ يستعمل في قطع كل أرض؛ جائبة خبر (mufradat)
- **B003** söze ya da çağrıya karşılık verme — söze ya da soruya verilen karşılık · karşılık vermek · karşılık verme ve çağrıya uyma · isteyenin dileğini karşılamak · karşılıklı konuşmak · karşılık · yanlış işitip yanlış karşılık vermek
  مراجعة الكلام؛ أجابه جوابا؛ تجاوبا مجاوبة (maqayis)؛ الجواب رديد الكلام (ayn)؛ الجواب معروف؛ الإجابة والاستجابة بمعنى؛ المجاوبة والتجاوب التحاور (sihah)؛ أجوبه من الإجابة أي أسرعه إجابة (tahdhib)؛ جواب الكلام؛ أجيبوا داعي الله؛ أجيب دعوة الداع؛ فليستجيبوا لي (mufradat)
- **B004** açılmış ya da ortası boş geniş aralık — geniş açıklık ya da çukur alan · ortası boş veya oyuk · bulutun açılıp dağılması
  الجوبة كالغائط وهو من الباب لأنه كالخرق في الأرض (maqayis)؛ كل مجوف وسطه فهو مجوب (ayn)؛ الجوبة الفرجة في السحاب وفي الجبال؛ انجابت السحابة انكشفت (sihah)؛ الجوبة من الأرض الدارة؛ كل منفتق يتسع فهو جوبة (tahdhib)؛ الجوب قطع الجوبة وهي كالغائط من الأرض (mufradat)
- **B005** giysi, zırh veya kalkan; giysiyi üstüne geçirme — kadının giydiği zırh ya da giysi · kalkan · kesilmiş bir tür giysi · giysiyi üstüne geçirmek
  الجوب درع تلبسه المرأة وهو مجوب (maqayis)؛ الجوب درع تلبسه المرأة (ayn)؛ الجوب الترس (jamhara)؛ الجوب الترس؛ الجوب كالبقيرة؛ اجتبت القميص إذا لبسته (sihah)؛ الجوب الترس؛ اجتاب فلان ثوبا إذا لبسه (tahdhib)
- **B006** ışık, açığa çıkarma ve belirginleştirme — 
  جوب نور وكشف وجلى (tahdhib)

## ECHO ج ي ب (root_000283): for 42:16 ٱسْتُجِيبَ, 42:26 وَيَسْتَجِيبُ, 42:38 ٱسْتَجَابُوا۟, 42:47 ٱسْتَجِيبُوا۟: withheld observed target; not identity

- **B001** gömlek açıklığı ve onu oyup oluşturma — gömlek açıklığı veya açıklığın yeri · gömleğin açıklığını oyarak açmak · gömleğe açıklık yapmak
  الجيب جيب القميص (maqayis;sihah)؛ جيب القميص معروف (jamhara)؛ جبيت القميص تجبيبا جعلت له جيبا (ayn)؛ جبت القميص قورت جيبه وجيبته جعلت له جيبا (maqayis)؛ جيبت القميص تجييبا إذا جعلت له جيبا (sihah)؛ جمع جيب (mufradat)

## ECHO ج ب ب (root_000214): for 42:16 ٱسْتُجِيبَ, 42:26 وَيَسْتَجِيبُ, 42:38 ٱسْتَجَابُوا۟, 42:47 ٱسْتَجِيبُوا۟: withheld observed target; not identity

- **B001** kokunden kesip ayirma — kokunden kesme ve koparma · onu kesip kokunden ayirdi · horgucu kokunden kesmek · horgucu kesilmis deve · erkeklik organlari kesilerek alinmis kisi
  الجب القطع (maqayis;sihah;mufradat)؛ استئصال السنام من أصله وبعير أجب (ayn;tahdhib)؛ كل شيء قطعته فقد جببته وخصي مجبوب (jamhara)
- **B002** ustun gelip geride birakma — toplulugu yenip asmak · kadinin diger kadinlari guzelligiyle gecmesi
  جبه إذا غلبه بحسنه أو غيره كأنه قطعه عن مساماته (maqayis)؛ والجب الغلبة (ayn)؛ جبت المرأة النساء إذا غلبتهن من حسنها (jamhara;tahdhib;mufradat)؛ فلان جب القوم إذا غلبهم (sihah)
- **B003** bedeni saran giysi — bedeni saran giysi · giyilen giysiler veya zırhlar · zırh adi olarak kullanilan giysi
  الجبة معروفة لأنها تشمل الجسم وتجمعه فيها (maqayis)؛ الجباب جمع الجبة التي تلبس (ayn)؛ الجباب التي تلبس (sihah)؛ الجبة التي تلبس والجبة من أسماء الدروع (tahdhib)؛ الجبة التي هي اللباس منه (mufradat)
- **B004** icine girilen yuva — mızrak ucunun sap giren yuvasi · goz cukuru ve cevresi · evin ortasi ve ici · tomurcugun ic kismi · boynuzdaki ilik yeri
  الجبة ما دخل فيه ثعلب الرمح من السنان (maqayis)؛ جبة السنان أي مدخله (ayn)؛ الجبة ما دخل فيه الرمح من السنان (sihah)؛ جبة العين حجاجها وجبة الدار وسطها وجب طلعة داخلها وجب القرن الذي فيه المشاشة (tahdhib)؛ به شبه ما دخل فيه الرمح من السنان (mufradat)
- **B005** deri veya iskembe kabi — toprak tasiyan deri sepet · et veya yag konan iskembe kabi · bu kaba et parcalari koymak veya ona gore hazirlanmak · bu tur kaplarin ticaretini yapmak
  الجبجبة زبيل من جلود يجمع فيه التراب والجبجبة الكرش يجعل فيه اللحم (maqayis)؛ الجبجبة الكرش يجعل فيها الخلع أو تذاب الإهالة فتحقن فيها والجبجبة أيضا زبيل من جلود ينقل فيه التراب (sihah)؛ الجبجبة زبيل من جلود ينقل فيه التراب والجبجبة الكرش يجعل فيها اللحم ويسمى الخلع (tahdhib)
- **B006** hurma asılama isi ve zamani [kalıp] — insanlarin hurmalari asılamasi · hurma asilama veya hurma isleri zamani
  وجب الناس النخل إذا ألقحوه وذا زمن الجباب (maqayis)؛ الجباب أيضا تلقيح النخل وقد جب الناس النخل (sihah)؛ إذا لقح الناس النخيل قيل قد جبوا وقد أتانا زمن الجباب (tahdhib)؛ كجب النخل وقيل زمن الجباب نحو زمن الصرام (mufradat)
- **B007** sert kalin toprak yuzeyi — sert veya kalin yer yuzeyi · yerden koparilan iri sert toprak kesegi
  الجبوب الأرض الغليظة (maqayis)؛ الجبوب وجه الأرض الصلبة (ayn)؛ الجبوب الأرض الغليظة ويقال وجه الأرض (sihah)؛ الجبوب وجه الأرض والأرض الغليظة والأرض الصلبة والمدر المفتت (tahdhib)؛ جبوب أي أرض غليظة (mufradat)
- **B008** ana yol hatti — ana yol ve yolun toplanma hatti
  المجبة جادة الطريق ومجتمعه (maqayis)؛ المجبة جادة الطريق (sihah)؛ ركب فلان المجبة وهي الجادة (tahdhib)
- **B009** kaplanmamis derin kuyu — kaplanmamis veya derin kuyu · genis icli kuyu veya kuyu ici · belirli bir su yeri adi
  الجب البئر (maqayis)؛ الجب البئر العميقة التي لا طي لها الكثيرة الماء البعيدة القعر (jamhara)؛ الجب البئر التي لم تطو وجمعها جباب وجببة (sihah)؛ الجب البئر التي لم تطو وبئر مجببة الجوف والقليب الواسعة الشحوة وركية تجاب في الصفا (tahdhib)؛ الجب أي بئر لم تطو (mufradat)
- **B010** kacis icin toparlanip savusma — kacip savusmak, kacis icin toparlanmak
  جببت تجبيبا إذا فر وذلك أنه يجمع نفسه للفرار ويتشمر (maqayis)؛ التجبيب أيضا النفار يقال جبب فلان فذهب (sihah)؛ جبب الرجل تجبيبا فهو مجبب إذا فر وعرد (tahdhib)
- **B011** deve sutu kopugu benzeri birikinti — deve sutu ustunde toplanan kopuk benzeri madde
  الجباب شيء يجتمع من ألبان الإبل كالزبد وليس للإبل زبد (maqayis)؛ الجباب كهيئة الزبد من ألبان الإبل (ayn)؛ الجباب بالضم شيء يعلو ألبان الإبل كالزبد ولا زبد لألبانها (sihah)؛ الجباب شبه الزبد يعلو ألبان الإبل ويجتمع عند فم السقاء (tahdhib)؛ الجباب شيء يعلو ألبان الإبل (mufradat)
- **B012** hayvan ayaginda beyaz nişan ve yuva — hayvan ayaginda yukariya uzanan beyazlik · beyazligi dizlerine kadar ulasan at · ayak-bacak birlesimi veya tirnak yuvasi
  الجبة بياض تطأ فيه الدابة بحافرها حتى تبلغ الأشاعر والنعت مجبب (ayn)؛ الجبة موصل الوظيف في الذراع ومغرز الوظيف في الحافر والتجبيب أن يبلغ التحجيل ركبة اليد وعرقوب الرجل (sihah)؛ المجبب الفرس الذي يبلغ تحجيله إلى ركبتيه وجبة الفرس ملتقى الوظيف في أعلى الحوشب والجبب جمع جبة وهو وعاء الحافر (tahdhib)
- **B013** dikilmis su tulumu — parcalari birbirine dikilmis su tulumu
  نهى النبي عن الجب قيل هو المزادة يخيط بعضها إلى بعض (tahdhib)
- **B014** siddetli kuraklik — siddetli kuraklik
  الجباب القحط الشديد (tahdhib)
- **B015** iri yanli ve dolgun bedenli olma — iri yanli veya iri bedenli · zayifliktan sonra bedeni buyumek veya semirmek
  رجل جباجب ومجبجب إذا كان ضخم الجنبين ونوق جباجب وجمل جباجب وبجابج ضخم وقد جبج إذا عظم جسمه بعد ضعف وجبجب إذا سمن (tahdhib)
- **B016** sığ sudaki su kayasi — sığ sudaki su kayasi
  الجبجبة أتان الضحل وهو صخرة الماء (tahdhib)

## د ح ض (root_000461): 42:16 دَاحِضَةٌ

- **B001** ayağın kayıp tutunamaması — ayağı kaymak, ayağının tutuşunu yitirmek · kayma, kayganlık · kaygan yer · ayağın tutunmadığı kaygan yer · basınca ayağın tutmadığı kaygan yer · yeri kayganlaştıran su · kaydırma
  الدحض الزلق (maqayis;ayn;jamhara;tahdhib)؛ دحضت رجله زلقت (maqayis;sihah)؛ دحضت رجل البعير زلقت (ayn;tahdhib)؛ كل موضع لا تطمئن فيه القدم فهو مدحض (jamhara)؛ مكان دحض أي زلق (sihah)؛ أصله من دحض الرجل (mufradat)
- **B002** güneşin göğün ortasından ayrılması [kalıp] — güneş göğün orta noktasından ayrıldı
  دحضت الشمس زالت (maqayis)؛ دحضت الشمس عن بطن السماء أي زالت (ayn;tahdhib)؛ دحضت الشمس عن كبد السماء زالت (sihah)؛ دحضت الشمس مستعار من ذلك (mufradat)
- **B003** bir savın geçersizleşmesi veya geçersiz kılınması — savı geçersiz kaldı, gerekçesi çürük çıktı · savını çürüttü, geçersiz kıldı · geçersiz veya çürük sav · çürütülmüş, geçersiz bırakılmış
  دحضت حجة فلان إذا لم تثبت (maqayis)؛ دحضت حجته أي بطلت (ayn)؛ ودحضت حجته فهي داحضة وأدحضها الله (jamhara)؛ حجتهم داحضة بمعنى مدحوضة (jamhara)؛ دحضت حجته بطلت وأدحضها الله (sihah)؛ دحضت حجته إذا بطلت وأدحض حجته إذا أبطلها (tahdhib)؛ حجتهم داحضة أي باطلة زائلة (mufradat)؛ ليدحضوا به الحق (mufradat)

## ع ن د (root_001052): 42:16 عِندَ, 42:22 عِندَ, 42:36 عِندَ

- **B001** doğruyu bile bile geri çevirerek karşı koyma ve sınırı aşma — azıp sınırı aşmak ve doğruyu bile bile geri çevirmek · bildiği şeyi kabul etmeyi bile bile reddetme · birine karşı durup onunla boy ölçüşmek; kimi zaman onun yaptığının benzerini yapmak · zorbalık eden ve doğruya uymaktan yüz çeviren kimse · doğruyu kabul etmeyip karşı çıkan kimse · devenin yulara yüklenip onu yöneten kişiyi çekmesi
  أصل صحيح واحد يدل على مجاوزة وترك طريق الاستقامة (maqayis)؛ عند الرجل إذا طغى وعتا وجاوز قدره (maqayis;ayn)؛ المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله (maqayis;ayn;tahdhib)؛ خالف ورد الحق وهو يعرفه (sihah)؛ العنيد المعرض عن طاعة الله تعالى (tahdhib)؛ استعند البعير إذا غلب قائده على الزمام (maqayis)؛ عاند البعير خطامه أي عارضه (tahdhib)
- **B002** ortak doğrultudan yana sapıp ayrı durma — yoldan ya da amaçlanan yönden sapıp uzaklaşmak · bir yana çekilip topluluğa karışmayan · tek başına yaşayıp insanlara karışmayan adam · sürünün bir yanında durup öteki develere karışmayan deve · canlılığı ve gücü yüzünden yoldan yana sapan dişi deve · düz doğrultudan yana sapmış yol · yan, taraf · sağa sola yönelen saplama vuruşu · öteki kura oklarından başka bir yönde çıkarak kazanan ok · dirseği göğüsten uzakta duran
  العنود من الإبل الذي لا يخالط الإبل إنما هو في ناحية (maqayis;ayn;tahdhib)؛ رجل عنود لا يخالط الناس (maqayis;ayn)؛ طريق عاند أي مائل (maqayis)؛ العند بالتحريك الجانب (sihah)؛ العاند البعير الذي يجور عن الطريق ويعدل عن القصد (sihah)؛ قدح عنود وهو الذي يخرج فائزا على غير وجهة سائر القداح (tahdhib)
- **B003** sıvının yana yönelerek veya kesilmeden akması [kalıp] — kanı fışkırıp bir türlü dinmeyen damar · kanın yana doğru akması · kanı yaralıdan uzağa doğru akan yara · kusmanın art arda sürüp kesilmemesi · bol yağmur taşıyan bulut
  العرق العاند الذي يتفجر منه الدم فلا يكاد يرقأ (maqayis)؛ عند العرق سال ولم يرقأ وهو عرق عاند (sihah)؛ أعند في قيئه إذا لم ينقطع (maqayis)؛ أعند الرجل في قيئه إذا أتبع بعضه بعضا (sihah;tahdhib)؛ عند الدم إذا سال في جانب (tahdhib)؛ سحابة عنود كثيرة المطر (tahdhib)
- **B004** yakınında veya birinin değerlendirmesinde bulunma — bir şeyin yer veya zaman bakımından yakınında · birinin görüşünde, değerlendirmesinde, gözünde veya katında
  عند فحضور الشيء ودنوه (sihah)؛ عند لفظ موضوع للقرب (mufradat)؛ يستعمل في المكان وفي الاعتقاد وفي الزلفى والمنزلة (mufradat)؛ عند حرف صفة يكون موضعا لغيره ولفظه نصب (tahdhib)؛ في التقريب شبه اللزق (tahdhib)؛ مال عن الناس كلهم إليه حتى قرب منه ولزق به (maqayis)
- **B005** başka seçenek, kaçınma payı veya çıkış yolu — başka bir seçenek, kaçınma payı veya çıkış yolu · bir işe ulaşma yolu ya da başka seçenek
  ما عنه عِنْدَد أي ما عنه ميل ولا حيدودة (maqayis)؛ مالي منه عِنْدَد ومُعْلَنْدَد أي بد (sihah;tahdhib)؛ العندد الحيلة (tahdhib)؛ ما وجدت إلى كذا معلنددا أي سبيلا (sihah)
- **B006** sözü dinleyeni almaya veya tutmaya yönelten buyruk — onu al; ona bağlı kal
  وقد يغرى بها تقول عندك زيدا أي خذه (sihah)؛ العرب تأمر من الصفات بعليك وعندك ودونك وإليك (tahdhib)

## غ ض ب (root_001092): 42:16 غَضَبٌ, 42:37 غَضِبُوا۟

- **B001** şiddetli öfke ve öç alma yönelimi — şiddetli öfke ve öç alma isteği · ona çok öfkelenmek · öfke ve kızgınlık · onu öfkelendirmek · öfkelenmek veya öfkesini göstermek · öfkeli · öfkeli kadın veya öfkeli topluluk · öfkeli kadın · öfkeli topluluklar · çok ve şiddetli öfkelenen · çok veya çabuk öfkelenen adam · çok ve şiddetli öfkelenen adam
  الغضب لأنه اشتداد السخط (maqayis)؛ رجل غضوب وغضب وغضبة وغضب أي كثير الغضب شديده (ayn)؛ الغضب ضد الرضا ورجل غضبة كثير الغضب (jamhara)؛ غضب عليه غضبا ورجل غضبان وغضبة يغضب سريعا (sihah)؛ الغضب ثوران دم القلب إرادة الانتقام وإذا وصف الله تعالى به فالمراد به الانتقام (mufradat)
- **B002** biri için ya da uğruna öfkelenmek [kalıp] — yaşayan biri için öfkelenmek · ölen biri uğruna öfkelenmek · ölen kişi uğruna öfkeli olmak
  غضبت لفلان إذا كان حيا وغضبت به إذا كان ميتا (maqayis;sihah;mufradat)
- **B003** karşı koyup muhalefet etmek — ona karşı koyup muhalefet etmek · topluluğuna karşı çıkan
  غاضبه: راغمه؛ مغاضبا أي مراغما لقومه (sihah)
- **B004** sert, yığılmış veya yuvarlak kaya — sert, yığılmış veya yuvarlak kaya
  الغضبة الصخرة الصلبة (maqayis)؛ الغضبة الصخرة الصلبة المتراكمة في الجبل (ayn)؛ الغضبة صخرة مستديرة (jamhara)؛ الغضبة كالصخرة (mufradat)
- **B005** kalın derili ya da çok kızıl — kalın derili adam · kızıl ve kalın yapılı adam · çok kızıl · çok kızıl olan
  رجل غضاب إذا كان غليظ الجلد؛ رجل غضب إذا كان أحمر غليظا (jamhara)؛ الغضب الأحمر الشديد الحمرة ويقال أحمر غضب (sihah)
- **B006** üst göz kapağı çıkıntısı veya göz çevresi şişliği — üst göz kapağında doğuştan çıkıntı veya göz çevresi şişliği · göz çevresinin şişmesi · göz altı şişmiş adam
  الغضب بخصة في الجفن الأعلى خلقة (ayn)؛ غضبت عين الرجل إذا ورم ما حولها ورجل به غضب إذا ورم ما تحت عينه (jamhara)
- **B007** somurtkan, huysuz; iri yılan — iri yılan; somurtkan veya huysuz olan · somurtkan veya huysuz dişi deve · somurtkan kadın
  الغضوب الحية العظيمة (maqayis)؛ ناقة غضوب عبوس (ayn)؛ امرأة غضوب أي عبوس (sihah)؛ توصف به الحية والناقة الضجور (mufradat)
- **B008** belirli hayvan derileri veya kalkan gibi katlanmış deri — yaşlı dağ keçisinin yüzülmüş derisi veya kalkan gibi katlanmış deve derisi · kaplumbağa derisi
  الغضبة جلد المسن من الوعول حين يسلخ (ayn)؛ يسمى جلد السلحفاة الغضب؛ الغضبة قطعة من جلد البعير يطوى بعضها على بعض ويجعل شبيها بالدرقة (jamhara)

## ع ذ ب (root_000994): 42:16 عَذَابٌ, 42:21 عَذَابٌ, 42:26 عَذَابٌ, 42:42 عَذَابٌ, 42:44 ٱلْعَذَابَ, 42:45 عَذَابٍ

- **B001** tatlı ve kolay tüketilen yiyecek ya da içecek — tatlı, hoş ve kolay tüketilir · tatlılık ve içim hoşluğu · suları tatlılaştı veya tatlı suya kavuştular · tatlı içme suyu aradılar veya sağladılar · onu tatlı saydı · onun için şu kuyudan su çekilir · birlikte anılan tükürük ve şarap
  عذب الماء عذوبة فهو عذب طيب (maqayis;ayn;tahdhib)؛ العذب ضد الملح وكل مستسيغ من طعام أو شراب (jamhara)؛ ماء عذب طيب بارد (mufradat)؛ استعذب القوم ماءهم إذا استقوه عذبا (sihah)
- **B002** yemeden içmeden durma — susuzluktan yemedi · yiyip içmeden duran · yiyip içmeden duran · yemekten kaçınır · geceyi yemeden içmeden geçirdi
  عذب الحمار يعذب عذبا وعذوبا فهو عاذب وعذوب لا يأكل من شدة العطش (maqayis;ayn)؛ العذوب من الدواب وغيرها القائم الذي لا يأكل ولا يشرب (sihah)؛ بات عذوبا إذا لم يأكل شيئا ولم يشرب (tahdhib)
- **B003** vazgeçme veya alıkoyma — o şeyden vazgeçti · kadınlardan söz etmekten kaçının · onu o işten alıkoydu · onu o işten kesti · senden vazgeçtim
  أعذب عن الشيء إذا لها عنه وتركه (maqayis)؛ أعذب عن الشيء إذا امتنع عنه (jamhara;tahdhib)؛ أعذبته عن الأمر إذا منعته عنه (sihah)؛ عذبته تعذيبا كقولك فطمته عن هذا الأمر (ayn;tahdhib)
- **B004** gökyüzüne karşı örtüsüz — gökyüzüne karşı örtüsüz olan · gökyüzüne karşı örtüsüz olan · geceyi gökyüzüne açık geçirdi
  العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب (maqayis;tahdhib)؛ فبات عذوبا للسماء كأنه سهيل (maqayis;tahdhib)
- **B005** ağır acı çektirme ve cezalandırma — ağır acı ve ceza · ona ağır acı çektirdi veya ceza verdi · yok edici ceza
  العذاب يقال منه عذب تعذيبا وناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة (maqayis)؛ عذبت الرجل وغيره تعذيبا والاسم العذاب (jamhara)؛ العذاب العقوبة وقد عذبته تعذيبا (sihah)؛ العذاب هو الإيجاع الشديد (mufradat)
- **B006** ince uç veya sarkan bağlı parça — kamçının ucu veya askısı · mızrak başına bağlanan bez · dilin ince ucu · teraziyi kaldıran ip · ağaç dalı · deve kamışının öndeki sivri ucu · ayakkabı bağının serbest ucu · kayışların uçları · eyerin arkasından sarkan deri parçası · ağıtçı kadının bezi · kamçıya askı yaptı
  عذبة السوط طرفه (maqayis;tahdhib)؛ عذبة الرمح الخرقة التي تشد على رأسه (jamhara)؛ عذبة اللسان طرفه (jamhara;sihah;tahdhib)؛ عذبة الميزان الخيط الذي يرفع به (sihah;tahdhib)؛ عذبة الشجر غصنه (sihah;tahdhib)؛ عذبة شراك النعل المرسلة من الشراك (tahdhib)
- **B007** yalıtık adlandırmalar — sudaki çer çöp veya yüzey tabakası · çer çöpü bol su · havuzundaki çer çöpü çıkar · havuzun yüzey tabakasını kır · çevresinde otlak bulunmayan su başı
  العذبة القذاة وماء ذو عذب أي كثير القذى (sihah)؛ أعذب حوضك أي انزع ما فيه من القذى (sihah)؛ اضرب عذبة الحوض حتى يظهر الماء أي اضرب عرمضه (tahdhib)؛ ماء ما به عذبة أي لا رعي فيه ولا كلأ (tahdhib)
- **B008** iyi ve cömert huylu — iyi ve cömert huylu
  العذبي الكريم الأخلاق (sihah)
- **B009** biçime bağlı adlandırmalar — doğumdan sonra döl yatağından çıkan madde · kadının döl yatağı
  العذب ما يخرج على أثر الولد من الرحم (tahdhib)؛ العذابة رحم المرأة (tahdhib)

## ش د د (root_000782): 42:16 شَدِيدٌ, 42:26 شَدِيدٌ

- **B001** bağlayıp sağlamlaştırma — bir şeyi bağlayıp sağlamlaştırmak · gücüne güç katmak, desteklemek · Tanrı onun yönetimini güçlendirsin
  شددت العقد شدا (maqayis)؛ شد الحبل أو غيره (jamhara)؛ شده أي أوثقه (sihah)؛ شددت الشيء إذا أوثقته (tahdhib)؛ الشد العقد القوي وقويت عقده (mufradat)؛ شد عضده أي قواه (sihah)؛ شد الله ملكه وشدده أي قواه (sihah)؛ اشدد به أزرى (tahdhib)
- **B002** güç, katılık ve çetinlik — güç, katılık, dayanıklılık ve çetinlik · güçlü ve yürekli · ağır sıkıntı, çetin sınanma · büyük sarsıntılar ve ağır sıkıntılar · artırma ve ağırlaştırma · bir konuda çok sıkı davranma · hiçbir şeye gücü yetmemek · şarkı söylerken sesini yükseltmek için var gücünü kullanmak · güçlü bir bineğe sahip olmak · güçlü ve sert
  أصل واحد يدل على قوة في الشيء (maqayis)؛ الشدة الصلابة والنجدة وثبات القلب والمجاعة (ayn;tahdhib)؛ الشدة القوة في الجسم وصعوبة الزمن (jamhara)؛ الشدة القوة والجلادة والشديد الرجل القوي (tahdhib)؛ الشدة تستعمل في العقد وفي البدن وفي قوى النفس وفي العذاب (mufradat)؛ أصابتني شدى أي شدة (maqayis;sihah;tahdhib)؛ التشديد خلاف التخفيف (sihah)؛ ما أملك شدا ولا إرخاء لا أقدر على شيء (tahdhib)؛ تشددت القينة إذا جهدت نفسها (tahdhib)؛ كانت دوابهم شدادا وأشد الرجل إذا كانت معه دابة شديدة (maqayis;sihah)
- **B003** saldırıya atılma ve hızla koşma — düşmanın üzerine saldırmak · koşma, hızlı koşu · koşmak, hızla ilerlemek · tek bir saldırı hamlesi
  في الحرب أيضا يشد شدا (maqayis)؛ الشد الحمل وشد عليه في القتال (ayn;tahdhib)؛ شد على العدو إذا حمل عليه (jamhara;sihah)؛ الشد العدو والفعل اشتد (ayn;sihah)؛ الشد الحضر والفعل اشتد (tahdhib)؛ شد فلان على العدو شدة واحدة وشد شدات كثيرة (tahdhib)
- **B004** güç ve sağduyu bakımından olgunluğa erişme — güç, sağduyu ve deneyimin olgunluk düzeyi
  الأشد العشرون ويقال أربعون سنة (maqayis)؛ الأشد مبلغ الرجل الحنكة والمعرفة (ayn;tahdhib)؛ بلغ الرجل أشده والواحد شد (jamhara)؛ حتى يبلغ أشده أي قوته (sihah)؛ معناه الإدراك والبلوغ وأن يؤنس منه الرشد مع أن يكون بالغا (tahdhib)؛ يجتمع أمره وقوته ويكتهل وينتهي شبابه (tahdhib)
- **B005** günün ilerleyip yükselmesi [kalıp] — günün ilerleyip yükselmesi
  شد النهار ارتفاعه (maqayis;sihah)
- **B006** eli sıkılık — eli sıkı · eli sıkı
  الشديد والمتشدد البخيل (maqayis)؛ المتشدد البخيل (sihah)؛ لشديد أي لبخيل (tahdhib)

## ح ق ق (root_000347): 42:17 بِٱلْحَقِّ, 42:18 ٱلْحَقُّ, 42:24 وَيُحِقُّ, 42:24 ٱلْحَقَّ, 42:42 ٱلْحَقِّ

- **B001** gerçekliğe uygun, kesin doğruluk — gerçekte var olana uygun, doğru ve sağlam olan · işin açığa çıkmış gerçek yüzü · kesinlikle yapmayacağım diye yemin etme sözü · konuyu doğrulayıp kesinliğinden emin oldum · haber doğru çıktı ve kesinleşti · gerçekte var olan şey veya sözün ilk anlamı
  الحق نقيض الباطل (maqayis;sihah;tahdhib)؛ أصل الحق المطابقة والموافقة (mufradat)؛ حققت الأمر وأحققته إذا تحققته وصرت منه على يقين (sihah)؛ الحقيقة خلاف المجاز (sihah)
- **B002** bağlayıcı gereklilik ve hak ediş — gerekli ve bağlayıcı oldu · bildirilen hüküm onun için kesinleşip bağlayıcı oldu · buna layık veya bunu yapmakla yükümlü · bunu yapman sana düşer veya senin yükümlülüğündür · gerekli kıldı veya bir sonucu hak etti · korktuğu şeyi yapıp başına getirdi · doğru bir istem ileri sürdü ve isteği kesinleşti
  حق الشيء وجب (maqayis;sihah;tahdhib)؛ حقيق بكذا ومحقوق به (maqayis;sihah;tahdhib)؛ أحققت الشيء أي أوجبته واستحققته أي استوجبته (sihah)؛ يستعمل استعمال الواجب واللازم والجائز (mufradat)
- **B003** sahibine bağlı pay ve istem yetkisi — sahibine ait ve onun isteyebileceği özel pay · kişinin kendine ait belirli payı · malı, elinde tutana karşı kendisinin saydırıp geri aldı
  إنك لتعرف الحقة عليك (maqayis)؛ الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي (sihah;tahdhib)؛ استحقها على المشتري أي ملكها عليه (tahdhib)؛ وبعولتهن أحق بردهن (mufradat)
- **B004** doğru taraf olma savıyla çekişme — doğrunun kendisinde olduğunu ileri sürerek onunla çekişti · karşılıklı çekişip her biri kendini doğru saydı · küçük konularda bile durmadan çekişen · çekişmede savını kabul ettirip üstün geldi
  حاق فلان فلانا إذا ادعى كل واحد منهما (maqayis)؛ حاقه أي خاصمه، والتحاق التخاصم والاحتقاق الاختصام (sihah)؛ تحاق القوم واحتقوا إذا تخاصموا (tahdhib)؛ حاققته فحققته أي خاصمته في الحق فغلبته (mufradat)
- **B005** doğruluğunu belirleme ve gösterme — konuyu doğrulayıp kesinliğinden emin oldum · sözünün veya sanısının doğru çıktığını gösterdi · savını geçerli kılıp karşısındakine üstün geldi · doğruyu söyledi veya doğru istemi kabul edildi
  حققت الأمر وأحققته أي كنت على يقين منه (maqayis)؛ حققت قوله وظنه تحقيقا أي صدقت (sihah)؛ حقق الرجل إذا قال هذا الشيء هو الحق (tahdhib)؛ أحققت كذا أي أثبته حقا أو حكمت بكونه حقا، ليحق الحق (mufradat)
- **B006** karşılığın kesinleştiği Son Gün — bütün karşılıkların kesinleştiği Son Yargı Günü
  الحاقة القيامة لأنها تحق بكل شيء (maqayis)؛ الحاقة القيامة سميت بذلك لأن فيها حواق الأمور (sihah)؛ سميت حاقة لأنها تحق كل إنسان بعمله (tahdhib)؛ الحاقة إشارة إلى القيامة لأنه يحق فيه الجزاء (mufradat)
- **B007** korunması ve savunulması gereken şey — koruması gereken şeyi savunan kişi · korunacak bayrak, dokunulmaz değer veya çevre
  حامي الحقيقة إذا حمى ما يحق عليه أن يحميه ويقال الحقيقة الراية (maqayis)؛ الحقيقة ما يحق على الرجل أن يحميه (sihah)؛ الحقيقة الراية والحرمة والفناء وما يلزمه الدفاع عنه (tahdhib)؛ فلان يحمي حقيقته أي ما يحق عليه أن يحمى (mufradat)
- **B008** dördüncü yaşındaki yük taşımaya elverişli deve — üç yaşını tamamlamış, yük veya binme için elverişli dişi deve · üç yaşını tamamlamış, yük veya binme için elverişli erkek deve · dişi devenin çiftleştirildiği belirli zaman
  الحقة من أولاد الإبل ما استحق أن يحمل عليه (maqayis)؛ الحق من الإبل ابن ثلاث سنين وقد دخل في الرابعة والأنثى حقة (sihah;tahdhib)؛ الحق من الإبل ما استحق أن يحمل عليه والأنثى حقة (mufradat)؛ أتت الناقة على حقها أي الوقت الذي ضربت فيه (sihah;tahdhib;mufradat)
- **B009** iç boşluğa ulaşan düz saplanış — düz ilerleyip bedenin iç boşluğuna ulaşan saplanış · avın bir bölümünü öldürücü veya delici biçimde vurdu
  طعنة محتقة إذا وصلت إلى الجوف (maqayis)؛ طعنة محتقة أي لا زيغ فيها وقد نفذت (sihah)؛ المحتق من الطعن النافذ إلى الجوف (tahdhib)
- **B010** sıkı dokunmuş veya sağlam kurulmuş [kalıp] — sıkı ve düzgün dokunmuş kumaş · sağlam, tutarlı ve iyi kurulmuş söz
  ثوب محقق إذا كان محكم النسج (maqayis;sihah)؛ كلام محقق أي رصين (sihah)؛ أحققت الأمر إحقاقا إذا أحكمته وصححته (tahdhib)
- **B011** özel adlandırma kümesi — iki kemiğin birleştiği eklem yeri · başın tam ortası veya kışın ortası · ağaçtan veya fildişinden yapılmış küçük kap · kapı ayağının oturup döndüğü yuva · örümcek ağı
  الحق ملتقى كل عظمين والحق من الخشب (maqayis)؛ سقط على حاق رأسه وجئته في حاق الشتاء (sihah)؛ الحقة من خشب وحق العاج وحق الورك وحق الوابلة وحق الكهول بيت العنكبوت (tahdhib)؛ مطابقة رجل الباب في حقه (mufradat)
- **B012** bineği gücünü aşacak biçimde sert sürme — bineğin sırtını yoran, gücünü aşan sert sürüş
  الحقحقة أرفع السير وأتعبه للظهر (maqayis;sihah)؛ الحقحقة عند العرب أن يسار البعير ويحمل على ما يتعبه ولا يطيقه (tahdhib)؛ الحقحقة السير الشديد (tahdhib)
- **B013** devenin veya sürünün iyice semirmesi — dişi deve semirdi veya çiftleşip gebe kaldı · topluluğun sürüsü semirdi veya en semiz durumuna ulaştı
  أحقت الناقة من الربيع أي سمنت (maqayis)؛ استحقت الناقة سمنا وأحقت وحقت إذا سمنت (tahdhib)؛ أحق القوم إحقاقا إذا سمن مالهم واحتق المال إذا سمن وانتهى سمنه (tahdhib)
- **B014** terlemeyen veya art ayağını ön ayak izine basan at — terlemeyen veya art ayağını ön ayağının bastığı yere koyan at · at zayıfladı ve bedeni inceldi
  الأحق من الخيل الذي لا يعرق (maqayis;sihah;tahdhib)؛ الأحق أن يطبق هذا ذاك (maqayis)؛ الأحق الذي يضع رجله في موضع يده (tahdhib)؛ احتق الفرس أي ضمر (sihah)

## و ز ن (root_001645): 42:17 وَٱلْمِيزَانَ

- **B001** tartarak veya yaklaşık ölçüp biçerek niceliği belirleme — bir şeyi tartmak veya ölçüsünü belirlemek · hurma ürününün miktarını yaklaşık kestirmek · bir şeyin ağırlık ölçüsü · bir dirhem ağırlığında gelmek · bir kimse için veya ona karşı bir şeyi tartmak · kendisi için tartılanı teslim almak
  وزنت الشيء وزنا؛ الزنة قدر وزن الشيء (maqayis)؛ الوزن ثقل شيء بشيء مثله؛ وزن الشيء إذا قدره؛ وزن ثمر النخل إذا خرصه (ayn;tahdhib)؛ وزنت الشئ وزنا وزنة؛ هذا يزن درهما (sihah)؛ الوزن معرفة قدر الشيء؛ ما يقدر بالقسط والقبان (mufradat)
- **B002** tartı aracı ve adil değerlendirme ölçütü — terazi · teraziler ve tartı ağırlıkları · hesapta adil ve denk değerlendirme
  بناء يدل على تعديل واستقامة (maqayis)؛ الميزان ما وزنت به (ayn)؛ الميزان معروف (sihah)؛ الموازين واحدها ميزان وهو المثاقيل؛ الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل (tahdhib)؛ مراعاة المعدلة؛ الوزن يومئذ الحق فإشارة إلى العدل في محاسبة الناس (mufradat)
- **B003** iki şeyi denk veya karşılıklı konumda tutma — iki şeyi karşılaştırıp birbirine denklemek · bu, ötekiyle aynı ölçüde veya onun hizasındadır · dağın yanı veya hizası · bu, ötekiyle zihinde denk tutulur
  هذا يوازن ذلك أي هو محاذيه (maqayis)؛ وازنت بين الشيئين؛ هذا يوازن هذا إذا كان على زنته أو كان محاذيه؛ هو وزن الجبل أي ناحية منه؛ هو زنة الجبل أي حذاءه (sihah)؛ هذا في وزن هذا؛ قام في النفس مساويا لغيره (tahdhib)
- **B004** günün tam ortasına gelmesi [kalıp] — gün ortalandı
  قام ميزان النهار إذا انتصف النهار (maqayis;mufradat)؛ قام ميزان النهار أي انتصف (sihah)
- **B005** sağlam yargı ve kararlı yöneliş [kalıp] — sağlam ve ağırbaşlı düşünceli · yargısı güçlü ve aklı sağlam · kendini o işe hazırlayıp kararlılıkla yönelmek
  وزين الرأى معتدله؛ راجح الوزن إذا نسبوه إلى رجاحة الرأي وشدة العقل (maqayis)؛ رجل وزين الرأي وقد وزن وزانة إذا كان متثبتا (ayn;tahdhib)؛ فلان وزين الرأي أي رزينه (sihah)؛ أوزن فلان نفسه على الأمر إذا وطن نفسه عليه (tahdhib)
- **B006** kısa boylu, kimi kullanımda aklı başında kadın — kısa boylu kız · kısa boylu, aklı başında kadın · kısa boylu kadın
  جارية موزونة فيها قصر (ayn;tahdhib)؛ امرأة موزونة قصيرة عاقلة؛ الوزنة المرأة القصيرة (tahdhib)
- **B007** toplumsal değer; eksiksiz ağırlıktaki para [kalıp] — bizim yanımızda hiçbir değeri ve saygınlığı yok · onlara hiçbir değer ve saygınlık tanımayız · tam ağırlıktaki dirhem
  درهم وازن أي تام (sihah)؛ ما لفلان عندنا وزن أي قدر لخسته؛ فلا نقيم لهم يوم القيامة وزنا (tahdhib)؛ فلا نقيم لهم يوم القيامة وزنا (mufradat)
- **B008** ölçülü ve dengeli yaratılmış şey [kalıp] — ölçülü ve dengeli yaratılmış şey
  بناء يدل على تعديل واستقامة (maqayis)؛ وأنبتنا فيها من كل شيء موزون؛ قيل هو المعادن كالفضة والذهب؛ كل ما أوجده الله وأنه خلقه باعتدال (mufradat)

## د ر ي (root_000473): 42:17 يُدْرِيكَ, 42:52 تَدْرِى

- **B001** bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme — bir şeyi bilmek veya ondan haberdar olmak · birine bildirmek, onun bilmesini sağlamak · bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi · bilmiyorum
  دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)
- **B002** saldırı amacıyla bir yer ya da kişiyi seçmek [kalıp] — bir yeri baskın veya saldırı için seçmek
  أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)
- **B003** avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak — avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan · avı gizlenip aldatarak atış menziline getirmek · hileyle kandırmak
  الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)
- **B004** sivri uç ve bundan ad alan saç düzeltme aracı — sivri boynuz; saçı düzeltmeye yarayan sivri araç · saçı ayırıp düzeltmeye yarayan şiş biçimli araç · saçını tarayıp düzeltmek
  الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)
- **B005** saplama ve atış alıştırma hedefi — üzerinde saplama alıştırması yapılan hedef
  الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)
- **B006** insanlarla yumuşak ve incelikli geçinmek [kalıp] — insanlara karşı yumuşak ve uzlaştırıcı davranmak
  مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)

## ECHO د ر ر (root_000469): for 42:17 يُدْرِيكَ, 42:52 تَدْرِى: withheld observed target; not identity

- **B001** bir kaynaktan bolca çıkma veya bol ürün verme — sütün memeden çıkıp akması · süt · bol sütlü dişi deve · bulutun yağmur boşaltması · bol yağmur getiren · gözünden yaş akması · damarların kanla dolması · Ne güzel iş ve iyilik! · İyiliği artmasın! · vergi gelirinin artması · pazarın canlanması · dişi keçilerin teke istemesi · sütün bolluğu veya akışı
  الدر در اللبن (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در السحاب بالمطر ودرت السماء وسحابة مدرار (maqayis;jamhara;sihah;tahdhib;mufradat)؛ لله دره ولا در دره أي خيره أو عمله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در الخراج وحلوبة المسلمين وللسوق درة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ استدرت المعزى إذا أرادت الفحل (maqayis;sihah;tahdhib;mufradat)
- **B002** hızlı, güçlü ve akıcı koşma — çok hızlı koşan binek hayvanı · atın hızlı ve rahat koşması · bacakta güçlü koşma yetisi · atın tırıs sırasında ön ayağını kaldırıp indirdiği yürüyüş biçimi
  الدرير من الدواب الشديد العدو السريعة (maqayis)؛ در الفرس دريرا إذا عدا عدوا شديدا سهلا (jamhara)؛ فرس درير أي سريع (sihah)؛ در الفرس درة فهو درير إذا أسرع في عدوه والإدرار في الخيل (tahdhib)
- **B003** gevşekçe sallanma veya tekrar tekrar gidip gelme — diş yuvaları; kimi kullanımda dil ucu · çocuğun bir şeyi ağzında çevirip çiğnemesi · sallanıp oynamak · dişleri dökülüp diş yuvaları görünmek · gereksiz yere gidip gelen kimse
  الدردر منابت أسنان الصبي ومن تدردرت اللحمة إذا اضطربت ودردر الصبي الشيء إذا لاكه (maqayis)؛ الدردر مغارز أسنان الصبي ودردر الصبي البسرة لاكها (sihah)؛ تدردر أي تمرمر وترجرج والدردر مغرز السن وطرف اللسان والدردرى الذي يذهب ويجيء في غير حاجة (tahdhib)
- **B004** doğrultu, yön veya karşı karşıya hizalanma — yolun doğrultusu veya güzergâhı · rüzgârın esiş yönü · tam karşında veya hizanda
  درر الريح مهبها ودرر الطريق قصده (maqayis)؛ هما على درر واحد ونحن على درر الطريق ودرر الريح مهبها (sihah)؛ فلان دررك أي قبالتك وعلى درر الطريق أي مدرجته وداري بدرر دارك أي بحذائها (tahdhib)
- **B005** iri inci; inci gibi beyaz ve parlak yıldız — iri inciler veya inci topluluğu · iri inci; tek bir inci · inci gibi beyaz ve parlak yıldız
  الدر كبار اللؤلؤ والكوكب الدري الثاقب المضيء (maqayis)؛ الدرة ما عظم من اللؤلؤ (jamhara)؛ الدرة اللؤلؤة والكوكب الدري الثاقب المضيء نسب إلى الدر لبياضه (sihah)؛ الدر العظام من اللؤلؤ والكوكب الدري الثاقب المضيء (tahdhib)
- **B006** özellikle yöneticinin kullandığı vurma değneği — özellikle yöneticinin kullandığı vurma değneği
  الدرة التي يضرب بها عربية معروفة (jamhara)؛ الدرة التي يضرب بها (sihah)؛ الدرة درة السلطان التي يضرب بها (tahdhib)
- **B007** ipliği sıkı bükmek için iği döndürme — ipliği sıkı bükmek için iği veya dönen parçasını çevirmek
  أدرت المرأة المغزل إذا فتلته فتلا شديدا فهي مدر والمغزل مدر (jamhara)؛ أدرت الغزالة درارتها إذا أدارتها لتستحكم قوة ما تغزله (tahdhib)
- **B008** gemiyi tehlikeye atan çalkantılı deniz girdabı — girdap; gemiyi tehlikeye atan çalkantılı deniz yeri
  الدردور الماء الذي يدور ويخاف فيه الغرق (sihah)؛ الدردور موضع من البحر يجيش ماؤه وقلما تسلم السفينة منه (tahdhib)

## س و ع (root_000760): 42:17 ٱلسَّاعَةَ, 42:18 ٱلسَّاعَةِ

- **B001** zamanın sürmesi ve belirli bir zaman kesiti — şimdiki zaman ya da gece ve gündüzden bir bölüm · dünyanın sona erip insanların yeniden dirileceği gün · zaman bölümleri · kısacık bir zaman · gecenin sakinleşmesinden bir süre sonra · gecenin sakinleşmesinden bir süre sonra · zaman dilimi başına işlem yapma · bir çalışanı zaman dilimi başına tutmak · çetin bir zaman kesiti
  استمرار الشيء ومضيه (maqayis)؛ الساعة سميت بذلك (maqayis)؛ الساعة الوقت الحاضر (sihah)؛ الساعة القيامة (ayn;sihah;tahdhib)؛ الساعة جزء من آخر الليل والنهار (tahdhib)؛ جاءنا بعد سوع من الليل وبعد سواع (maqayis;sihah;tahdhib)؛ عاملته مساوعة (maqayis;sihah)؛ ساوعت الأجير إذا استأجرته ساعة بعد ساعة (tahdhib)؛ ساعة سوعاء أي شديدة (sihah)
- **B002** gözetimsiz bırakıp başıboş gitmesine yol açma — develeri kendi yönlerine gidecek biçimde gözetimsiz bırakmak · bir şeyi kaybetmek · gözetimsiz kaldığı için kendi yönüne gitmek · başıboş gitmek veya yavrusunu gözetimsiz bırakmak · kaybolmuş ve gözetimsiz kalmış · otlakta kendi başına uzaklaşan dişi deve · yavrusunu yırtıcıya açık biçimde bırakan dişi deve · malını savuran adam · malı savuran kişi
  أسعت الإبل إساعة إذا أهملتها (maqayis;sihah;tahdhib)؛ ساعت فهي تسوع (maqayis;sihah;tahdhib)؛ ضائع سائع (maqayis;sihah;tahdhib)؛ ناقة مسياع تذهب في المرعى (maqayis;sihah;tahdhib)؛ رجل مسياع مضياع للمال (sihah;tahdhib)؛ ناقة مسياع تدع ولدها حتى يأكله السبع (tahdhib)
- **B003** eski anlatılarda geçen belirli bir putun özel adı — eski anlatılarda tapınılan belirli bir putun özel adı
  سواع اسم صنم في زمن نوح (ayn;tahdhib)؛ سواع اسم صنم كان لقوم نوح ثم صار لهذيل (sihah)
- **B004** saman karıştırılmış çamur — saman karıştırılmış çamur
  السياع الطين فيه التبن (maqayis)
- **B005** boşalma öncesi salgı — boşalma öncesi salgı · boşalmadan önce çıkan salgı · boşalma öncesi salgıyla ilgilenme buyruğu
  السواعي مأخوذ من السواع وهو المذي وهو السوعاء (tahdhib)؛ السوعاء المذي الذي يخرج قبل النطفة (tahdhib)؛ سع سع إذا أمرته أن يتعهد سوعاءه (tahdhib)
- **B006** ölüp yok olanlar — ölüp yok olmuş kimseler
  الساعة الهلكى (tahdhib)

## ق ر ب (root_001212): 42:17 قَرِيبٌ, 42:23 ٱلْقُرْبَىٰ

- **B001** yakın olma, yaklaşma veya yaklaştırma — yakın olmak veya yaklaşmak · yaklaştırmak, yakına getirmek · yaklaşma · ses değişmesiyle yaklaşmak · suyu yakın kuyu · parçaları birbirine yakın, kısa yapılı
  أصل صحيح يدل على خلاف البعد (maqayis)؛ كرب الشيء دنا فليس من الباب وإنما هو من الإبدال من القرب (maqayis-ibdal)؛ قرب الشيء قربا ضد البعد (jamhara)؛ قرب الشيء يقرب قربا أي دنا والقرب ضد البعد (sihah)؛ القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو والقرب البئر القريبة الماء والرجل القصير متقارب (tahdhib)؛ القرب والبعد يتقابلان ويستعمل ذلك في المكان (mufradat)
- **B002** zamanca yaklaşma veya yakın geçmişe ait olma — vaadin veya hesap vaktinin yaklaşması · son saatin yaklaşması · ürünün olgunlaşma vaktinin yaklaşması · güneşin batmaya yaklaşması · henüz taze olan tuzlu balık
  اقترب الوعد أي تقارب (sihah)؛ تقارب الزمان اقتراب الساعة وتقارب الزرع إذا دنا إدراكه والشيء إذا ولى وأدبر قد تقارب والقريب السمك المملح ما دام في طراءته (tahdhib)؛ في الزمان نحو اقترب للناس حسابهم (mufradat)؛ كربت الشمس دنت للمغيب (maqayis-ibdal)
- **B003** akrabalık ve yakın akraba — akrabalık, soy bağı · yakın akraba · yakın akrabalığı olan kimse
  فلان ذو قرابتي وهو من يقرب منك رحما والقربة والقربى القرابة (maqayis)؛ قريب الرجل مدانيه من نسب أم أو أب والجمع قرابة وقرباء وأقرباء (jamhara)؛ القرابة القربى في الرحم وهو قريبي وذو قرابتي وهم أقربائي وأقاربي (sihah)؛ القريب والقريبة ذو القرابة وفلان ذو قرابتي وذو مقربة وذو قربى (tahdhib)؛ في النسبة أولوا القربى والأقربون وذو قربى ولذي القربى والجار ذي القربى ويتيما ذا مقربة (mufradat)
- **B004** ayrıcalıklı yakın çevre — yakın kılınmış, gözde kişiler · hükümdarın özel çevresi, oturum arkadaşları ve yöneticileri · yakın kılınmış melekler
  قربان الملك وقرابينه وزراؤه وجلساؤه (maqayis)؛ قرابين الملك خاصته وقربان الملك قرابته والجمع قرابين (jamhara)؛ القربان واحد قرابين الملك وهم جلساؤه وخاصته (sihah)؛ القرابين جلساء الملوك وخاصته وقرابين الملك وزراؤه (tahdhib)؛ في الحظوة الملائكة المقربون ومن المقربين وقربناه نجيا (mufradat)؛ الملائكة الكروبيون وهم المقربون (maqayis-ibdal)
- **B005** Tanrı'ya yakınlık kazandıran iş veya sunu — Tanrı'ya yakınlık kazandıran iyi iş veya araç · Tanrı'ya yakınlık için sunulan şey veya kesilen hayvan · iyi bir iş veya sunuyla Tanrı'ya yakınlık aramak
  القربان ما قرب إلى الله تعالى من نسيكة أو غيرها (maqayis)؛ ما له عند الله قربة والقربان الأضاحي وكل ما تقرب إلى الله فهو قربان (jamhara)؛ القربان ما تقربت به إلى الله وتقرب إلى الله بشيء طلب به القربة (sihah)؛ القربان ما قربت إلى الله تبتغي بذلك قربة ووسيلة وهي ذبائح كانوا يذبحونها (tahdhib)؛ القربان ما يتقرب به إلى الله وصار اسما للنسيكة التي هي الذبيحة والقربة قربات عند الله (mufradat)
- **B006** gözetme, güç ve ruhsal yöneliş bakımından yakınlık — gözetip karşılık vermek üzere yakın · gücü ve erişimi bakımından insana en yakından hakim · insanın Tanrı'ya ruhsal yakınlığı
  في الرعاية نحو فإني قريب أجيب دعوة الداع وفي القدرة نحو ونحن أقرب إليه من حبل الوريد وقرب الله تعالى من العبد هو بالإفضال عليه والفيض لا بالمكان وقرب العبد من الله قرب روحاني لا بدني (mufradat)
- **B007** temas edip içine girecek ölçüde yaklaşma — bir işe bulaşmak, girişmek veya onu yapmak üzere olmak · yasak şeye yönelmemek ve onunla temas kurmamak · eşiyle cinsel ilişkide bulunmak
  ما قربت هذا الأمر ولا أقربه إذا لم تشامه ولم تلتبس به (maqayis)؛ قرب فلان أهله قربانا إذا غشيها وما قربت هذا الأمر ولا قربته ولا تقربا هذه الشجرة ولا تقربوا الزنى (tahdhib)؛ ولا تقربوهن كناية عن الجماع ولا تقربوا مال اليتيم أبلغ من النهي عن تناوله ولا تقربوا الزنى (mufradat)
- **B008** geceleyin su kaynağına yönelme — suya varıştan önceki gece yolculuğu · su arayıp kaynağa doğru gitmek · geceleyin su arayan kişi veya hayvan · suya doğru giderken acele etmek · suya gidip gelen hiç kimsesi yok
  من الباب القرب وهي ليلة ورود الإبل الماء والقارب الطالب الماء ليلا (maqayis)؛ القرب أن يرعى القوم بينهم وبين المورد حتى إذا كان بينهم وبين الماء عشية أو ليلة عجلوا فقربوا وحمار قارب يطلب الماء (ayn)؛ قربت الإبل الماء إذا طلبته وليلة القرب ليلة طلب الماء (jamhara)؛ القرب سير الليل لورد الغد والقارب طالب الماء ليلا (sihah)؛ ليلة القرب هو السوق الشديد وتقرب أي اعجل وقربت الماء أي طلبته والقرب سير الليل (tahdhib)؛ رجل قارب قرب من الماء وليلة القرب وأقربوا إبلهم (mufradat)
- **B009** su tulumu — su tulumu, deri su kabı
  القربة معروفة (jamhara)؛ القربة ما يستقى فيه الماء والجمع قربات وقربات وقربات وللكثير قرب (sihah)؛ القربة وجمعها قرب من الأساقي (tahdhib)
- **B010** kılıç kını veya deri dış kabı — kılıç kını veya kını saran deri kap · kılıcı kabına koymak veya ona bir kap yapmak
  منه القراب قراب السيف والجمع قرب (maqayis)؛ قراب السيف جلد يكون فيه وليس بالغمد والجمع قرب (jamhara)؛ قراب السيف جفنه وهو وعاء يكون فيه السيف بغمده وحمالته (sihah)؛ القراب للسيف والسكين وقربته جعلته في القراب (tahdhib)؛ القراب وعاء السيف وقيل جلد فوق الغمد لا الغمد نفسه (mufradat)
- **B011** gemiye bağlı küçük hizmet teknesi — gemiye eşlik eden küçük hizmet teknesi
  القارب سفينة صغيرة تكون مع أصحاب السفن البحرية وكأنها سميت بذلك لقربها منهم (maqayis)؛ قارب السفينة وهو الصغير الذي يتبعها (jamhara)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم (sihah)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم والجميع القوارب (tahdhib)
- **B012** doğumu yaklaşmış gebe dişi — koyunun doğumu yaklaşmak · doğumu yaklaşmış gebe dişi
  أقربت الشاة دنا نتاجها (maqayis)؛ شاة مقرب إذا دنا ولادها (jamhara)؛ أقربت المرأة إذا قرب ولادها وكذلك الفرس والشاة فهي مقرب ولا يقال للناقة (sihah)؛ أقربت الشاة والأتان فهي مقرب ولا يقال للناقة إلا إذا أدنت فهي مدن (tahdhib)؛ المقرب الحامل التي قربت ولادتها (mufradat)
- **B013** yakında tutulan ve binmeye hazırlanan hayvan — yakında tutulan, gözetilen ve binmeye hazır at · binmek için bağlanmış veya eyerlenmiş develer
  فرس مقربة وهي التي ترتاد وتقرب ولا تترك أن ترود (maqayis)؛ فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة (jamhara)؛ المقرب من الخيل الذي يدنى ويكرم والأنثى مقربة (sihah)؛ الخيل المقربة التي تكون قريبا معدة والتي تدنى وتقرب وتكرم والإبل المقربة التي حزمت للركوب (tahdhib)
- **B014** atın dörtnaldan yavaş özel koşusu — atın dörtnaldan yavaş özel koşu biçimi
  قرب الفرس تقريبا وهو دون الحضر وله تقريبان أدنى وأعلى (maqayis)؛ قرب الفرس تقريبا وهو تقريبان التقريب الأدنى والتقريب الأعلى وهو دون الحضر (jamhara)؛ التقريب ضرب من العدو وهو دون الحضر (sihah)؛ إذا رفع الفرس يديه معا ووضعهما معا فذلك التقريب (tahdhib)؛ تقريب الفرس سير يقرب من عدوه (mufradat)
- **B015** böğür, bedenin yan bölgesi — böğür, bel ile karnın alt yanı arasındaki bölge · böğürler, bedenin yanları · yürürken elini böğrüne koymuş
  الخاصرة هي القرب سميت لقربها من الجنب (maqayis)؛ قرب الفرس كشحه وهو الخصر والجمع أقراب (jamhara)؛ القرب من الشاكلة إلى مراق البطن والجمع الأقراب (sihah)؛ القرب من لدن الشاكلة إلى مراق البطن ومتقربا أي واضعا يده على قربه (tahdhib)؛ فرس لاحق الأقراب أي الخواصر (mufradat)
- **B016** bir ölçü veya sınıra yaklaşık olma — bir şeyin doluluğuna, sayısına veya miktarına yakın değer · neredeyse dolu kap · ses değişmesiyle neredeyse dolu kap · orta kalitede veya ucuz kumaş · satışta önerileri birbirine yaklaştırmak · akşama veya geceye yakın vakit
  ثوب مقارب إذا لم يكن جيدا وهذا على معنى أنه مقارب في ثمنه (maqayis)؛ الدراهم قراب مائة وإناء قربان إذا قارب أن يمتلىء وقراب كل شيء ما قارب الامتلاء (jamhara)؛ شيء مقارب وسط بين الجيد والردئ أو رخيص وقدح قربان إذا قارب أن يمتلئ وقاربته في البيع مقاربة (sihah)؛ القراب مقاربة الشيء معه ألف درهم أو قرابه وأتيته قراب العشي أو قراب الليل وقدح قربان ماء ولو أن في قراب هذا ذهبا (tahdhib)؛ القراب المقاربة وقدح قربان قريب من الملء (mufradat)؛ إناء كربان كرب أن يمتلىء (maqayis-ibdal)

## ع ج ل (root_000987): 42:18 يَسْتَعْجِلُ

- **B001** tez davranma, çabuklaştırma ve öne alma — bir işte tez davranma ve onu vaktinden önce isteme · tez davranan, ağırdan almayan · çok tez davranan · çabuk davranmaya yöneltmek · çabuklaştırmak veya bir işten uzaklaştırmak · önüne geçmek · geciktirilmemiş, elde bulunan · bu dünya ve eldeki dünya nimetleri · bir şeyi vaktinden önce vermek
  العَجَلة في الأمر (maqayis)؛ العجل خلاف البطء (jamhara;sihah)؛ العجلة طلب الشيء وتحريه قبل أوانه (mufradat)؛ استعجلته أي حثثته (ayn;sihah;tahdhib)؛ أعجلتم أمر ربكم أي سبقتم (maqayis;sihah;tahdhib)؛ العاجل ضد الآجل (maqayis;sihah;tahdhib)
- **B002** evcil sığır yavrusu — evcil sığır yavrusu, buzağı · dişi buzağı · buzağı için kullanılan başka bir ad · yavrulu inek
  العجل ولد البقرة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ العجل عجل الثيران (ayn)؛ الأنثى عجلة والعجول مثله والجمع عجاجيل (maqayis;jamhara;sihah;tahdhib)؛ لا يقال لولد الوحشية عجل (jamhara)
- **B003** su çekme ve yük taşıma düzeneği — su çekme, yük taşıma veya çekme düzeneği · su çekme veya yük taşıma düzenekleri
  العجلة عجلة الثيران (maqayis;ayn;sihah)؛ العجلة المنجنون يستقى عليها (maqayis;ayn;sihah;tahdhib)؛ خشبة معترضة على نعامتي البئر (maqayis;sihah;tahdhib;mufradat)؛ خشب يؤلف شبيه بالمحفة تجعل عليه الأثقال (jamhara)؛ الدولاب (tahdhib)؛ ما يحمل على الثيران (mufradat)
- **B004** hafif, taşınabilir su kabı — hafif su tulumu, kırba veya küçük su kabı
  العجلة الإداوة الصغيرة (maqayis;ayn;mufradat)؛ العجلة المزادة أو السقاء أو القربة (jamhara;sihah;tahdhib)؛ سميت بذلك لأنها خفيفة يعجل بها حاملها (maqayis)
- **B005** çabuk sunulan veya kolay yenilen azık — çabuk elde edilen veya kolay yenilen azık · yolcunun hurma ve kavrulmuş tahıl türü kolay azığı · çobanın ailesine hızla götürdüğü süt kabı veya süt · konuklara hazırlık tamamlanmadan sunulan yemek · kurutulmuş süt ürünü, hurma veya karışımından küçük parçalar
  العجالة ما تعجل من شيء (maqayis;sihah;tahdhib)؛ التمر عجالة الراكب (maqayis;jamhara;sihah;tahdhib)؛ العجل ما استعجل به طعام (maqayis;tahdhib)؛ العجالة ما يعجل أكله (mufradat)؛ الإعجالة اللبن الذي يعجله الراعي (jamhara;tahdhib;sihah)؛ العجيلاء طعام يقرب إلى القوم (jamhara)؛ العجاجيل هنات من الأقط والتمر (tahdhib)
- **B006** yavrusunu yitirip özlem duyan dişi — yavrusunu yitirip özlem duyan dişi deve veya çocuğunu yitirmiş kadın · yavrularını yitirmiş dişi develer
  العجول من الإبل الواله التي فقدت ولدها (maqayis;sihah;tahdhib)؛ المعاجيل من الإبل اللاتي فقدت أولادها (jamhara)؛ المرأة الثكلى عجول (maqayis;tahdhib)
- **B007** yavrusunu vaktinden önce doğuran dişi — erken doğurup yavrusu yaşayan dişi deve · yavrusunu vaktinden önce doğuran gebe dişi
  المعجل والمعجل من النوق التي تنتج قبل أن تستكمل الوقت فيعيش ولدها (maqayis)؛ المعجال من الحوامل التي تضع ولدها قبل إناه (tahdhib)
- **B008** hızlı gidiş, kestirme yol ve erken sıçrama — hızlı bir gidiş biçimi · yakın veya kestirme yollar · binici yerleşmeden devenin sıçraması
  العجيلي ضرب من السير سريع (tahdhib)؛ معاجيل الطرق أقرب (tahdhib)؛ الإعجال في السير أن يثب البعير قبل استواء الراكب عليه (tahdhib)
- **B009** belirli bir bitki veya ağaç adı — belirli bir bitki veya ağaç türünün adı
  العجلة ضرب من النبت (jamhara;sihah;tahdhib)؛ العجلة شجرة (tahdhib)

## ش ف ق (root_000803): 42:18 مُشْفِقُونَ, 42:22 مُشْفِقِينَ

- **B001** incelik, düşük nitelik ya da azlık — ince, düşük nitelikli veya az şey · ince ya da düşük nitelikli giysi veya örtü · dokumayı düşük nitelikli yapmak veya verilecek miktarı azaltmak · azaltılmış veya az miktardaki bağış
  أصل واحد يدل على رقة في الشيء (maqayis)؛ الشفق الرديء من الأشياء (maqayis;ayn;sihah;tahdhib)؛ شفق الثوب أي جعله في النسج شفقا (tahdhib)؛ عطاء مشفق أي مقلل (sihah)
- **B002** gün batımı kızıllığı — gün batımından sonra kalan kızıllık veya gündüz aydınlığı · bazı hukukçulara göre akşam kızıllığından sonra kalan beyazlık
  الشفق الحمرة التي بين غروب الشمس إلى وقت صلاة العشاء الآخرة (maqayis;ayn;sihah)؛ الشفق الحمرة التي في المغرب من الشمس (tahdhib)؛ اختلاط ضوء النهار بسواد الليل عند غروب الشمس (mufradat)
- **B003** kaygılı ilgi ve sakınma — kaygıyla gözetme ve sakınma · bir şeyden çekinip sakınmak · biri için kaygılanıp onu gözetmek · iyiliğini kaygıyla gözeten dikkatli öğütçü · bir şeyden çekinmek; seyrek ve tartışmalı kullanım
  أشفقت من الأمر إذا رققت وحاذرت (maqayis)؛ الشفق الخوف وهو مشفق أي خائف (ayn;tahdhib)؛ أشفقت عليه فأنا مشفق وشفيق وأشفقت منه تعني حذرته (sihah)؛ الإشفاق عناية مختلطة بخوف (mufradat)
- **B004** erzakı esirgemek veya bağışı kısmak [kalıp] — erzakı veya geçimliği cimrice esirgemek · azaltılmış veya az miktardaki bağış
  كما شفقت على الزاد العيال فمعناه بخلت به (maqayis)؛ عطاء مشفق أي مقلل (sihah)؛ إذا شفقت على الرزق العيال (tahdhib)
- **B005** bir işin çeşitli yönleri içinde olmak [kalıp] — bu işin çeşitli yönleri veya tarafları içindeyim
  أنا في أشفاق من هذا الأمر أي نواح منه (tahdhib)؛ ومثله أنا في عروض منه وفي أعراض منه أي في نواح (tahdhib)

## م ر ي (root_001416): 42:18 يُمَارُونَ

- **B001** ovup içteki akışı veya gücü ortaya çıkarma — sütü indirmek için memeyi elle ovma · sütü insin diye devenin memesini ovdu · bol sütlü ya da memesi ovulunca süt veren deve · devenin sütü aktı · ovma yoluyla devenin sütünü indirme · sütle dolup süt veren damarlar · atı kamçıyla veya başka bir yolla bütün koşu gücünü göstermeye zorladı · at ön ayaklarını oyalanır gibi yerde hareket ettirdi · rüzgâr buluttan yağmur çıkardı · rüzgâr buluttan yağmur çıkardı
  مري الناقة وذلك إذا مسحت للحلب؛ المرايا العروق التي تمتلىء وتدر باللبن (maqayis)؛ المري بالتخفيف مسحك ضرع الناقة تمريها بيدك كي تسكن للحلب؛ والريح تمري السحاب مريا (ayn)؛ مريت الناقة مريا إذا مسحت ضرعها ليدر؛ ومريت الفرس إذا استخرجت ما عنده من الجري؛ والريح تمري السحاب وتمتريه (sihah)
- **B002** ateş çıkarabilen beyaz parlak taş — ateş çıkarabilen beyaz parlak taşlar · ateş çıkarabilen beyaz parlak taş
  الأصل الآخر المرو جمع مروة وهي حجارة تبرق (maqayis)؛ المرو حجارة بيض براقة تقدح منها النار، الواحدة مروة (sihah)
- **B003** kuşkulu bir konu üzerinde sertçe tartışma — sert sözler içerebilen karşılıklı tartışma · kuşkulu bir konuda karşılıklı kanıtlaşma · onunla tartıştı ve çekişti · kuşkulu bir konuda karşılıklı kanıtlaşma · iki kişi arasında karşılıklı tartışma
  المراء مما يتمارى فيه الرجلان ... كلام فيه بعض الشدة؛ ماراه مراء ومماراة (maqayis)؛ ماريت الرجل أماريه مراء إذا جادلته (sihah)؛ الامتراء والمماراة المحاجة فيما فيه مرية (mufradat)
- **B004** kuşku veya kararsızlık — kuşku veya bir konuda kararsızlık · bir şeyden kuşku duyma · bir şeyden kuşku duyma
  المرية الشك (maqayis)؛ المرية الشك في الأمر؛ تمارى يتمارى تماريا وامترى امتراء إذا شك (ayn)؛ المرية الشك؛ الامتراء في الشيء الشك فيه وكذلك التمارى (sihah)؛ المرية التردد في الأمر، وهو أخص من الشك (mufradat)
- **B005** bir kimsenin hakkını inkâr etme [kalıp] — onun hakkını inkâr etti
  ومراه حقه، أي جحده؛ وقرئ قوله تعالى أفتمرونه على ما يرى (sihah)

## ECHO م و ر (root_001456): for 42:18 يُمَارُونَ: withheld observed target; not identity

- **B001** enine gidip gelme ve dalgalanma — enine gidip gelmek, salınmak · gidip gelerek salınma · göğün dalgalanıp çalkalanması · dalga, dalgalanma · üst kolları yanları boyunca salınmak · saplamanın sağa veya sola yatması
  أصل صحيح يدل على تردد (maqayis)؛ المور الموج (maqayis;ayn;sihah)؛ مار الشيء يمور مورا أي تحرك وجاء وذهب (sihah)؛ يوم تمور السماء مورا (ayn;sihah;mufradat)؛ الطعنة تمور إذا مالت يمينا أو شمالا (ayn)
- **B002** kanın yüzeyde gidip gelerek yayılması; hızlı akış — kanın yüzeye dökülüp akarak yayılması · kanı akıtmak; alternatif rivayette başka bir köke bağlanan kullanım · akan kanlar · hızlı akış
  مار الدم على وجه الأرض انصب وتردد (maqayis;ayn)؛ مار الدم على وجه الأرض وأماره غيره (sihah)؛ مار الدم على وجهه (mufradat)؛ المور الجريان السريع (mufradat)
- **B003** rüzgârın döndürdüğü toz — rüzgârın savurup döndürdüğü toz veya toprak
  المور تراب تمور به الريح (maqayis)؛ المور تراب وجولان تمور به الريح (ayn)؛ المور بالضم الغبار بالريح (sihah)؛ التراب المتردد به الريح (mufradat)
- **B004** salınarak hızlı gidiş [kalıp] — salınarak hızla giden dişi deve · sırtı yürüyüşte salınan at
  الناقة تمور في سيرها وهي موارة سريعة (maqayis)؛ ناقة موراة سريعة في سيرها (ayn)؛ ناقة موارة اليد أي سريعة (sihah)؛ ناقة تمور في سيرها فهي موارة (mufradat)؛ فرس موارة الظهر (maqayis)
- **B005** ilk tüy örtüsünün dökülmesi — eşek veya sıpanın doğum tüylerinin dökülmesi · eşekten dökülen tüy parçası
  انمارت عقيقة الحمار سقطت عنه (maqayis;sihah)؛ انمارت لبدة الفحل وعقيقة الجحش إذا سقطت عنه (ayn)؛ الموارة نسيل الحمار وقد تمور عليه نسيله (sihah)
- **B006** gidilip gelinen yol — insanların gidip geldiği yol
  المور الطريق لأن الناس يمورون فيه أي يترددون (maqayis)؛ المور الطريق (sihah)
- **B007** aşağıya gitmek mi, dönüp yukarı gelmek mi — Aşağı bölgeye mi gitti, yoksa dönüp yüksek bölgeye mi geldi, bilmiyorum.
  لا أدري أغار أم مار أي أتى غورا أم دار فرجع إلى نجد (maqayis;sihah)
- **B008** darbede ilerleyen keskin kılıç — kesme darbesinde ilerleyen keskin kılıç
  المائر السيف القاطع الذي يمور في الضريبة (maqayis)؛ السائر الشعر المروي (maqayis)

## ض ل ل (root_000913): 42:18 ضَلَٰلٍۭ, 42:44 يُضْلِلِ, 42:46 يُضْلِلِ

- **B001** doğru yoldan ve amaçtan sapma ya da başkasını saptırma — doğru yoldan, amaçtan veya doğruluktan sapmak · doğru yoldan ve doğruluktan sapma · doğru yoldan veya amaçtan sapmış kimse · sapmada direnen, çok sapmış kimse · iyilikten uzak, yanlış ve boş işlere dalmış kimse · asılsız ve yanlış düşünceler · birini doğru yoldan saptırmak · bir kimseyi sapmış saymak · yanlışlığın ve sapmanın içine düşülen yer · yolun bulunamadığı şaşırtıcı arazi · o işi yanlış ve sağduyusuz bir tutumla yapmak
  كل جائر عن القصد ضال؛ الضلال والضلالة بمعنى (maqayis); ضل إذا جار عن القصد؛ لا يوفق لخير صاحب غوايات وبطالات (ayn); الضلال ضد الهدى؛ ضل في الأمر إذا لم يهتد له؛ ضل في الأرض إذا لم يهتد للسبيل (jamhara); الضلال والضلالة ضد الرشاد؛ رجل ضليل ومضلل أي ضال جدا (sihah); الإضلال في كلام العرب ضد الهداية والإرشاد؛ ضل الكافر غاب عن الحجة؛ ضل فلان عن القصد إذا جار (tahdhib)
- **B002** gizlenerek, karışıp eriyerek veya gömülerek gözden yitme — gizlenip gözden kaybolmak · ölüyü gömüp gözden kaldırmak · bir sıvının ötekine karışıp içinde kaybolması · kaya altında güneş görmeyen su
  أضل الميت إذا دفن؛ ضل اللبن في الماء ثم استهلك (maqayis); ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (jamhara); أضل الميت إذا دفن؛ أضل عنه أي أخفى عليه وأغيب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (sihah); أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته (tahdhib)
- **B003** bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması — bir şeyin kaybolması, yitip gitmesi veya yok olması · devesini ya da başka bir hayvanını kaybetmek · evin, ibadet yerinin ya da başka bir yerin konumunu bulamamak · bir işin elinden kaçması ve ona güç yetirememek · kanı yerde kalmak, öcü alınmamak · yitme veya yok olma
  أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تهتد لهما (maqayis); ضللت مكاني إذا لم تهتد له؛ أضل بعيره إذا أفلت فذهب (ayn); ذهب فلان ضلة إذا لم يدر أين ذهب؛ ذهب دمه ضلة إذا لم يثأر به (jamhara); أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تعرف موضعهما (sihah); أضللت الشيء إذا ضاع منك؛ ضللت الشيء أضله إذا جعلته في مكان ولم تدر أين هو (tahdhib)
- **B004** bir şeyi unutmak veya bellekte tutamamak [kalıp] — bir şeyi unutmak ya da belleğinde tutamamak
  ضللت الشيء أنسيته (jamhara); إن تضل أي إن تنس؛ أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها (tahdhib)
- **B005** sahibi bilinmeyen kayıp hayvan, özellikle deve — sahibi bilinmeyen kayıp hayvan, özellikle deve · sahibi bilinmeyen kayıp hayvanlar veya develer
  الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn); الضالة ما ضل من البهيمة للذكر والأنثى (sihah); الضالة من الإبل التي بمضيعة لا يعرف لها مالك؛ الجميع الضوال (tahdhib)

## ل ط ف (root_001356): 42:19 لَطِيفٌۢ

- **B001** incitmeden iyilik ve özenle davranma — bir işi yumuşaklıkla yapma, iyilik ve ikram · kullarına şefkatli ve yumuşak davranan · çocuğuna iyilik eden ve onu gözeten anne · bu işi yumuşaklık ve idareyle yürüten · birine yumuşak davrandı · Tanrı, sevdiğin şeyi sana incitmeden ulaştırdı · Tanrı'nın yardım edip doğru sonuca eriştirmesi ve koruması · karşılıklı iyilik ve yumuşak davranış · işi yumuşaklıkla ele alma · kullarına yumuşak davranan; ince ayrıntıları bilen
  اللطف الرفق في العمل (maqayis;sihah)؛ لطيف بعباده أي رءوف رفيق (maqayis)؛ البر والتكرمة (ayn;tahdhib)؛ أم لطيفة بولدها تلطف إلطافا (ayn;tahdhib)؛ رفيق بمداراته (ayn)؛ التوفيق والعصمة (sihah)؛ يوصل إليك أربك في رفق (tahdhib)؛ لطف الله لك أي أوصل إليك ما تحب برفق (tahdhib)؛ لرفقه با (mufradat)
- **B002** küçüklük, incelik ve güç algılanırlık — kullarına yumuşak davranan; ince ayrıntıları bilen · küçüldü, inceldi ve hafifleşti · küçük, ince, hafif ve kaba olmayan · anlamı ince ya da örtük söz · ince, sert ve kaba olmayan çubuk · karnı çekik, beli ince kadın · incelik, küçüklük ve hafiflik · duyularla algılanamayacak kadar ince şeyler
  صغر في الشيء (maqayis)؛ لطيف الشيء الذي لا يتجافى من الكلام وغيره والعود ونحوه (ayn)؛ كلام لطيف وعود لطيف (ayn)؛ لطافة خلق غير جسيمة (ayn)؛ لطف الشيء يلطف لطافة أي صغر (sihah)؛ جارية لطيفة الخصر ضامرة البطن (tahdhib)؛ اللطيف من الكلام ما غمض معناه وخفي (tahdhib)؛ ضد الجثل وهو الثقيل (mufradat)؛ الحركة الخفيفة (mufradat)؛ تعاطي الأمور الدقيقة (mufradat)؛ اللطائف عما لا تدركه الحاسة (mufradat)؛ معرفته بدقائق الأمور (mufradat)
- **B003** iyiliği gösteren seçkin armağan — iyilik göstergesi olarak verilen seçkin armağan · ona bir şey vererek iyilik etti · falancadan gelen armağan
  اللطف من طرف التحف ما ألطفت به أخاك ليعرف به برك (ayn;tahdhib)؛ ألطفه بكذا أي بره به (sihah)؛ لطفة من فلان أي هدية (sihah)
- **B004** erkek devenin organını çiftleşme yerine yerleştirme — çiftleşme yerini bulamayan erkek devenin cinsel organını dişinin üreme açıklığına yerleştirmek · erkek devenin cinsel organını kendiliğinden dişinin üreme açıklığına sokması
  الإلطاف للبعير إذا لم يهتد لموضع الضراب فألطف له (maqayis)؛ ألطف الرجل البعير أدخل قضيبه في الحياء (sihah)؛ استلطف العبير أي أدخله فيها بنفسه (sihah)؛ إذا لم يسترشد لطروقته فأدخل الراعي قضيبه في حيائها قد أخلطه إخلاطا وألطفه إلطافا (tahdhib)؛ استلطف إذا فعل ذلك من تلقاء نفسه (tahdhib)
- **B005** bir nesneyi yana bitiştirme — nesneyi yanıma yapıştırdım · onu yanıma yapıştırdım · yana yapıştırılmış ya da giysinin altına yaklaştırılmış
  ألطفت الشيء بجنبي واستلطفته إذا ألصقته (tahdhib)؛ ضد جافيته عني (tahdhib)

## ع ب د (root_000973): 42:19 بِعِبَادِهِۦ, 42:23 عِبَادَهُ, 42:25 عِبَادِهِۦ, 42:27 لِعِبَادِهِۦ, 42:27 بِعِبَادِهِۦ, 42:52 عِبَادِنَا

- **B001** özgür olmayan, sahip olunan kişi — özgür olmayan, sahip olunan kişi · köleler · köle doğmuş veya kuşaklar boyunca köle kalmış kişiler
  العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)
- **B002** Tanrı'ya ait sayılan insan veya topluluk — Tanrı'nın kulu · Tanrı'nın kulları veya ona bağlı topluluk · Tanrı'ya ait sayılan bütün kullar
  تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)
- **B003** boyun eğerek itaat ve tapınma — Tanrı'ya boyun eğerek tapındı · boyun eğerek tapınma · kendini tapınmaya verme · sahte tanrısal güce boyun eğip itaat etti · sahte tanrısal güçlere veya putlara tapan topluluk
  عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)
- **B004** köleleştirmek veya köle gibi boyunduruk altına almak — onu köleleştirdi · kişiyi ezip köleleştirdi; topluluğu köle edindi · onu köle durumuna getirdi · özgür olsa da onu köle gibi boyunduruk altına aldı
  استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)
- **B005** düzleşmiş yol, katranlanmış deve veya kaplanmış gemi — çok geçilerek düzleşmiş yol · derisi baştan başa katranlanmış ve uysallaştırılmış deve · katranla kaplanmış gemi
  الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)
- **B006** saygı gösterilip hizmet edilen kişi — saygı gösterilen, yüceltilen ve hizmet edilen kişi
  المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)
- **B007** güç, sağlamlık ve dayanıklılık — güç, sağlamlık ve dayanıklılık · güçlü ve semiz dişi deve · kumaşının hiç dayanıklılığı yok
  العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)
- **B008** incinmiş gurur, öfke veya kederli iç duygulanım — incinmiş gurur, öfke, keder veya iç sıkıntısı · gururu incindiği için sustu
  العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)
- **B009** gecikmeden yapmak veya koşuda biraz hızlanmak [kalıp] — yapmakta gecikmedi · koşarken biraz hızlandı
  ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)
- **B010** her yana dağılmış kümeler, nesneler veya yollar — her yana dağılmış insan kümeleri, nesneler veya yollar
  العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)
- **B011** bineği yüzünden yolda kalma veya güçlükle direnen deve — bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı · insanlara güçlük çıkararak direnen deve
  أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)
- **B012** güzel koku maddesi ezme taşı — güzel koku maddelerini ezme taşı
  العبدة صلاءة الطيب (jamhara)

## ق و ي (root_001274): 42:19 ٱلْقَوِىُّ

- **B001** güç, dayanıklılık ve yeterlik — güç, dayanıklılık ve kudret · bir şeye dönüşmeye hazır gizil yeterlik · güçlü, zayıf olmayan · güçlendi veya güçlü oldu · bükülmüş ipin tek kolu · güçler veya ipin bükümlü kolları · beden yapısı çok sağlam adam · bir işte kararlılık ve sağlam tutum · malı, desteği veya güçlü bineği olan kişi · onu güçlendirdi · güç yarışında onu yendi · ipin bir kolunu gevşetip ötekini değiştirerek örgüsünü bozdu · varlıklı oldu veya bineği güçlüydü
  القوة خلاف الضعف (maqayis;sihah)؛ القوي خلاف الضعيف (maqayis)؛ رجل شديد القوى أي شديد أسر الخلق (maqayis;ayn;sihah;tahdhib)؛ القوة طاقة من طاقات الحبل وجمعها قوى (ayn;sihah;tahdhib)؛ القواية في الحزم دون البدن (ayn;tahdhib)؛ قوة البدن والقلب والمعاون والقدرة الإلهية (mufradat)؛ رجل مقو إذا كان ذا ظهر وذا مال (jamhara)؛ فلان قوي مقو فالقوي في نفسه والمقوي في دابته (sihah;tahdhib)
- **B002** şiirde ölçü veya uyak düzeni kusuru — şiirinde ölçü veya uyak düzeni kusuru yaptı · şiirde ölçü ya da uyak sonu uyumsuzluğu
  أقوى الرجل في شعره أن ينقص من عروضه قوة (maqayis)؛ الإقواء في الشعر مخالفة إعراب الروي (jamhara;sihah;tahdhib)؛ الإقواء نقصان الحرف من الفاصلة أو العروض (sihah;tahdhib)
- **B003** ıssızlık, boşluk ve geçim yoksunluğu — insansız, ıssız kır · düz, çıplak ve ıssız arazi · ev halksız kaldı · topluluk ıssız araziye vardı · geceyi aç geçirdi · azıksız ya da malsız kişi · yoksullaştı veya azığı tükendi · yağmursuz ve otsuz çıplak arazi · yağmur kesildi veya azaldı
  القواء الأرض لا أهل بها (maqayis;ayn;sihah;tahdhib)؛ أقوت الدار خلت من أهلها (maqayis;ayn;sihah;tahdhib)؛ أقوى القوم صاروا بالقواء أو وقعوا في قي من الأرض (maqayis;ayn;tahdhib)؛ بات القواء أي على غير طعم والمقوي لا زاد معه (maqayis;sihah;tahdhib)؛ أقوى افتقر (tahdhib;mufradat)؛ المقوي لا مال له (jamhara)؛ أرض أو بلد مقوية لا مطر ولا كلأ وسنة قاوية قليلة الأمطار (sihah;tahdhib)
- **B004** ortak malı değerleyerek veya fiyat artırarak tek ortağa bırakma — ortaklar malı değerledi veya fiyatını artırdı ve biri ötekinin payını aldı · ortak maldaki payı satın alıp kendine ayırma · ortak mal için karşılıklı değerleme veya fiyat artırma · diğer ortağın payını satın alan kişi · ortaklık işleminde payını satan kişi · payı alan kişi; payını ona ver
  اشترى الشركاء الشيء ثم اقتووه إذا تزايدوه حتى بلغ غاية ثمنه (maqayis;ayn;sihah)؛ التقاوي بين الشركاء إذا قوماها فقامَت على ثمن فأخذها أحدهما (tahdhib)؛ اقتويت منه الغلام أي اشتريت نصيبه (tahdhib)؛ القاوي الآخذ وقاوه أي أعطه نصيبه (tahdhib)
- **B005** dolu kovadaki suyu birlikte eğilip içme [kalıp] — dolu kovaya eğilip içindeki suyu hep birlikte içtik
  سمعت العرب تقول للسقاة إذا كرعوا في دلو ملآن ماء فشربوا ماءه قد تقاووه وقد تقاوينا الدلو تقاويا (tahdhib)
- **B006** boş yumurta kabuğu, çıkan yavru ve kesin ayrılık imgesi — yavrunun terk ettiği boş yumurta kabuğu · yumurtadan çıkmış kuş yavrusu · aralarındaki bağ kesin koptu veya satış geri alınamaz oldu · değersiz görülen kişi için boş kabuktan çıkmış yavru sözü
  انقطع قوي من قاوية إذا انقطع ما بين الرجلين أو وجبت بيعة لا تستقال؛ القاوية هي البيضة؛ فالقوي الفرخ تصغير قاو؛ العرب تقول للدنيء قوي من قاوية (tahdhib)

## ك و ن (root_001332): 42:20 كَانَ, 42:20 كَانَ, 42:46 كَانَ, 42:51 كَانَ, 42:52 كُنتَ

- **B001** gerçekleşme, bulunma ve olma bildirimi — gerçekleşip ortaya çıkmak veya hazır bulunmak · geçmişte bir durumu bildirmek · oluş; gerçekleşme · olma, oluş · sonradan gerçekleşen iş · yüklemi pekiştiren ek söz · birini geliş kapsamı dışında tutan bağlı söz · var edip gerçekleşmesini sağlamak
  الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)
- **B002** bulunma yeri ve konum değeri — bulunulan yer · yerler · konum, düzey veya bulunulan yer · birinin yanında güçlü konumu olan · yerleşmek veya güç kazanmak · birinin yanında şu yer veya düzeyde bulunmak
  المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)
- **B003** birini güvenceyle üstlenme — başkası için güvence üstlenme · birini üstlenmek · birine güvence olmak
  الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)
- **B004** boyun eğme — boyun eğme
  الاستكانة الخضوع (sihah)
- **B005** gençliğini anan yaşlı kişi — gençken şöyleydim diye anlatan yaşlı kişi
  يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)
- **B006** kötü durumda gece geçirme [kalıp] — geceyi kötü durumda geçirmek
  الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

## ر و د (root_000610): 42:20 يُرِيدُ, 42:20 يُرِيدُ

- **B001** dileyip yonelme — dileme, amaclama ve bir seye icten yonelme · bir seyi amaclamak, istemek ya da elde etmeye calismak · Yaraticinin bir seyi oyle diye hukme baglamasi · senden belirli bir seyi yapmani istemek ve buyurmak
  الإرادة: المشيئة (sihah)؛ الإرادة منقولة من راد يرود (mufradat)؛ نزوع النفس إلى الشيء (mufradat)؛ يذكر ويراد به القصد (mufradat)؛ فمعناه حكم فيه (mufradat)؛ قد تذكر الإرادة ويراد بها معنى الأمر (mufradat)؛ قال بعضهم الإرادة أصلها الواو (maqayis)
- **B002** birini istegine karsi razi etmeye calisma — birini belirli bir isi yapmaya razi etmeye calismak · birinin istegiyle cekisip onu gorusunden dondurmeye calismak · ters cevrilmis bicimde yeniden girisip yaklasma
  راودته على كذا مراودة وروادا، أي أردته (sihah)؛ المراودة أن تنازع غيرك في الإرادة (mufradat)؛ تصرفه عن رأيه (mufradat)؛ راودته على أن يفعل كذا إذا أردته على فعله (maqayis)؛ يرادى مقلوب ومعناه يراود (maqayis-crossref)
- **B003** dolasarak arama — bir seyi yumusakca dolasip gozden gecirerek aramak · otlak aramak icin giden ya da onde gonderilen kisi · arayisa cikan oncu adam
  راد الكلأ يروده رودا وريادا وارتاده ارتيادا أي طلبه (sihah)؛ الرائد الذي يرسل في طلب الكلإ (sihah)؛ رجل رأد بمعنى رائد (sihah)؛ الرود التردد في طلب الشيء برفق (mufradat)؛ الرائد لطالب الكلإ (mufradat)؛ بعثنا رائدا يرود الكلأ أي ينظر ويطلب (maqayis)
- **B004** gidip gelme — gidip gelmek ve ileri geri dolasmak · develerin otlakta ileri geri dolasmasi · suru veya bakicinin gidip geldigi yer · kadinin komsu evleri arasinda sik sik dolasmasi · yastiginda yerlesemeyip donup durmak
  يدل على مجيء وذهاب من انطلاق في جهة واحدة (maqayis)؛ راد الشئ يرود أي جاء وذهب (sihah)؛ رياد الإبل اختلافها في المرعى مقبلة ومدبرة (sihah)؛ المراد الموضع الذي ترود فيه الراعية (maqayis)؛ رادت المرأة ترود إذا اختلفت إلى بيوت جاراتها (maqayis)؛ راد وساده إذا لم يستقر (maqayis)
- **B005** yumusak ve yavas ilerleme — yolda yumusak davranip agir agir ilerlemek · agir ve acele etmeden yurume · yavas ol, acele etme ve biraz bekle · sert ve guclu esmeyen yumusak ruzgar
  يمشي على رود أي على مهل (sihah)؛ أرود في السير إروادا ومرودا أي رفق (sihah)؛ رويد: مهلا ورويدك: أمهل (sihah)؛ أرود يرود إذا رفق ومنه بني رويد (mufradat)؛ الإرواد في الفعل أن يكون رويدا (maqayis)؛ الرادة السهلة من الرياح لأنها ترود لا تهب بشدة (maqayis)
- **B006** cevirme kolu ve doner demir parca — el degirmenini cevirmeye yarayan tutamak kolu · ince cubuk, gemde donen demir parca veya demir makara ekseni
  الرائد يد الرحى وهو العود الذي يقبض عليه الطاحن إذا أداره (sihah)؛ الرائد العود الذي تدار به الرحى (maqayis)؛ المرود الميل وحديدة تدور في اللجام ومحور البكرة إذا كان من حديد (sihah)؛ والمرود الميل (maqayis)
- **B007** gozde dolasan bozukluk [kalıp] — gozun icinde dolasan bozukluk
  رائد العين عوارها الذي يرود فيها (sihah)؛ رائد العين عوارها الذي يرود فيها (maqayis)
- **B008** genc kiz veya genc ve guzel kadin — genc kiz · genc ve guzel kadin
  جارية رود شابة (maqayis)؛ الرؤدة والرأدة بالهمز: الشابة الحسنة (sihah)؛ وتكبير رويد رود (maqayis)

## ر د د (root_000555): 42:44 مَرَدٍّ, 42:47 مَرَدَّ (also echo for 42:20 يُرِيدُ, 42:20 يُرِيدُ)

- **B001** geri dönme veya geri döndürme — geri verme, geri gönderme veya eski durumuna döndürme · bir yere, sahibine veya kaynağına geri gönderme · kararı veya değerlendirme yetkisini bir kimseye bırakma · yolda veya durumda geri dönme · sapı içine katlanabilen ustura · görmesi geri gelmek
  أصل واحد مطرد منقاس وهو رجع الشيء (maqayis)؛ رده إلى منزله ورد إليه جوابا أي رجع (sihah)؛ الرد مصدر رددت الشيء (tahdhib)؛ الرد صرف الشيء بذاته أو بحالة من أحواله وفارتد بصيرا أي عاد إليه البصر (mufradat)
- **B002** yönünden çevirip engelleme [kalıp] — bir şeyi yolundan veya bir işten çevirme · geri dönüşü, yararı veya onu engelleyecek bir güç bulunmayan · iyiliğini engelleyebilecek kimse yok · savuşturulamayan ve önlenemeyen azap
  رده عن وجهه يرده ردا ومردا صرفه (sihah)؛ رده عن الأمر ولده أي صرفه عنه برفق (tahdhib)؛ لا راد لفضله أي لا دافع ولا مانع له وعذاب غير مردود (mufradat)
- **B003** kabul etmeyip geçersiz sayarak geri çevirme [kalıp] — sunulan şeyi kabul etmeme veya söyleyeni yanlış sayma · sahte bulunarak denetleyene geri verilen paralar
  رد عليه الشيء إذا لم يقبله وكذلك إذا خطأه (sihah)؛ ردود الدراهم واحدها رد وهو ما زيف فرد على ناقده بعد ما أخذ منه (tahdhib)
- **B004** geri isteme veya karşılıklı geri verme [kalıp] — bir şeyin geri verilmesini isteme veya onu geri alma · satışı bozarken tarafların aldıklarını karşılıklı geri vermesi
  استرده الشيء سأله أن يرده عليه وهما يترادان البيع من الرد والفسخ (sihah)؛ البيعان يترادان أي يرد كل واحد منهما ما أخذ واسترد المتاع استرجعه (mufradat)
- **B005** İslam'dan inkâra dönme — İslam'dan ayrılıp inkâra dönen kişi · Müslüman olduktan sonra inkâra dönme · dinden ayrılıp inkâra dönme · iman ettikten sonra yeniden inkâr durumuna döndürmek
  سمي المرتد لأنه رد نفسه إلى كفره (maqayis)؛ الارتداد الرجوع ومنه المرتد والردة الاسم من الارتداد (sihah)؛ ارتد الرجل عن دينه ردة إذا كفر بعد إسلامه (tahdhib)؛ الردة تختص بالكفر والارتداد يستعمل فيه وفي غيره (mufradat)
- **B006** boşanıp ailesine dönen kadın — boşanıp ailesine geri gönderilen kadın · boşanmış ve ailesine geri dönmüş kadın
  المردودة المرأة المطلقة وابنتك مردودة عليك ليس لها كاسب غيرك (maqayis)؛ المردودة المطلقة (sihah)؛ المردودة من النساء المطلقة وابنتك مردودة عليك لا كاسب لها غيرك (tahdhib)
- **B007** sütün, suyun veya bedensel sıvının birikip çoğalması — memesi sütle dolmuş koyun · memesine süt inmiş veya memesi sütle dolmuş deve · doğumdan önce memenin sütle dolması · suyu ya da dalgası bol ırmak veya deniz · uzun süre eşsiz kaldığı için cinsel isteği yoğunlaşmış erkek
  شاة مرد وناقة مردة إذا أضرعت ونهر مرد كثير الماء ورجل مرد إذا طالت عزبته (maqayis)؛ الردة امتلاء الضرع من اللبن قبل النتاج وبحر مرد كثير الموج (sihah)؛ ناقة مرد إذا أشرق ضرعها ووقع فيه اللبن ورجل مرد إذا طالت عزبته وبحر مرد أي كثير الماء (tahdhib)
- **B008** görünüş, nitelik veya konuşmadaki kusur — çenenin geriye çekikliği · yüzde güzelliğe karışan ve bakışı uzaklaştıran çirkinlik · kötü nitelikli şey · dil tutulması veya konuşma güçlüğü · çirkin kimseler
  الردة تقاعس في الذقن وقبح في الوجه مع شيء من جمال يرد الطرف (maqayis)؛ شيء رد أي رديء وفي لسانه رد أي حبسة وفي وجهه ردة أي قبح مع شيء من الجمال (sihah)؛ الردة تقاعس في الذقن وفي فلان ردة أي يرتد البصر عنه من قبحه (tahdhib)
- **B009** düşmeyi önleyen dayanak, sırt veya yük devesi — bir şeyi düşmekten koruyan dayanak; sırt veya yük taşıyan develer
  الرد عماد الشيء الذي يرده أي يرجعه عن السقوط والضعف (maqayis)؛ الرد ما صار عمادا للشيء يدفعه ويرده والرد الظهر والحمولة من الإبل (tahdhib)
- **B010** yineleme, gidip gelme, kararsızlık veya sıkı yapılı olma — bir şeyi tekrar tekrar yapma · bir eylemi defalarca yineleme · tekrar geri gelme veya iki yön arasında gidip gelme · bedeni sıkı, toplu ve parçaları birbirine geçmiş gibi olan kişi · kararsız ve ne yapacağını bilemeyen adam · develerin suya tekrar tekrar gitmesi · ellerini ağızlarına götürdüler; parmak ısırma, sus işareti yapma veya elçilerin ağızlarını kapatma biçimlerinde yorumlanan ifade
  المتردد الإنسان المجتمع الخلق كأن بعضه رد على بعض (maqayis)؛ ردده ترديدا وتردادا فتردد ورجل مردد حائر بائر (sihah)؛ فعلوا ذلك مرة بعد أخرى وردة الإبل أن تتردد إلى الماء (mufradat)

## ح ر ث (root_000303): 42:20 حَرْثَ, 42:20 حَرْثِهِۦ, 42:20 حَرْثَ

- **B001** çalışarak kazanma ve biriktirme — kazanç, biriktirme ve çalışma · mal edinme ya da kazanç arama · dünya hayatı veya ölüm sonrası için çalışmak · ailesinin geçimi için kazanıp çabalamak · kazanan kimse · ailesinin geçimi için kazanmak; ses değişmeli biçim
  الاحتراث من كسب المال (ayn;tahdhib)؛ الحرث كسب المال وجمعه (sihah)؛ حرث الرجل لدنياه أو آخرته إذا عمل لها (jamhara)؛ الحرث العمل للدنيا والآخرة (tahdhib)؛ يحرث لعياله ويحترث أي يكتسب (tahdhib)؛ الحارث معناه الكاسب (tahdhib;mufradat;maqayis)؛ هو من حرث أي كسب وجمع (maqayis-ibdal)
- **B002** toprağı hazırlayıp tohum ekme — tohumu toprağa atma ve toprağı ekime hazırlama · toprağı işleyip ekmek · ekin, ekilmiş ürün ya da ekili tarla · ekime hazırlanmış yer · çiftçiler
  الحرث قذفك الحب في الأرض (ayn;tahdhib)؛ حرث الزرع (jamhara)؛ الحرث الزرع والحراث الزراع (sihah)؛ إلقاء البذر في الأرض وتهيؤها للزرع ويسمى المحروث حرثا (mufradat)؛ من هذا الباب حرث الزرع (maqayis)
- **B003** evlilik ve cinsel birliktelik için ekim benzetmesi — evlilik ya da cinsel birliktelik için ekim benzetmesi · kadınlar, çocuk ve haz için ürün yetiştirilen yere benzetilir · kadın, kocanın çocuğunun yetiştiği yere benzetilir · karısıyla cinsel ilişkide bulunmak · dört kadınla aynı anda evli olmak · çok sık cinsel ilişkide bulunma
  الحرث النكاح (jamhara)؛ المرأة حرث الزوج مزدرع ولده (maqayis)؛ حرث الرجل امرأته والجماع الكثير (tahdhib)؛ فيهن تحرثون الولد واللذة (tahdhib)؛ بالنساء زرع ما فيه بقاء نوع الإنسان (mufradat)؛ حرث الرجل إذا جمع بين أربع نسوة (tahdhib)
- **B004** hayvanı kullanma veya kullanarak zayıf düşürme — atı kullanarak ya da sürerek zayıf düşürme · dişi devesini sürerek ya da kullanarak zayıf düşürmek · dişi deveyi zayıflayıncaya kadar sürmek veya onu kullanmak
  الإحراث هزل الخيل (ayn)؛ أحرث الرجل ناقته إذا هزلها (jamhara)؛ حرثت الناقة وأحرثتها أي سرت عليها حتى هزلت (sihah;tahdhib)؛ حرث ناقته إذا استعملها (mufradat)؛ حرث ناقته هزلها وأحرثها (maqayis)
- **B005** ateşi karıştırıp canlandırma — ateşi karıştırıp canlandırmak · ateşi karıştırmaya yarayan demir ya da tahta araç · savaşı kışkırtan şey · ateşi canlandırmaya yarayan araç
  المحراث من الحديد كهيئة المسحاة تحرك بها النار (ayn)؛ محراث الحرب ما يهيجها (ayn;tahdhib)؛ المحراث خشبة تحرك بها النار (jamhara)؛ حرثت النار حركتها (sihah)؛ الحرث إشعال النار ومحراث النار مسحاتها (tahdhib)؛ حرثت النار ولما تهيج به النار محرث (mufradat)
- **B006** metni inceleyip üzerinde düşünme — kutsal metni incelemek ya da çokça okumak · kutsal metni uzun süre inceleyip üzerinde düşünmek · bir kitabı araştırıp üzerinde düşünme · bilgi edinip derinlemesine araştırmak
  احرث القرآن أي ادرسه (sihah)؛ حرث إذا تفقه وفتش (tahdhib)؛ الحرث تفتيش الكتاب وتدبره (tahdhib)؛ حرثت القرآن إذا أطلت دراسته وتدبرته (tahdhib)؛ احرث القرآن أي أكثر تلاوته (mufradat)
- **B007** kiriş için kertik ve oluk hazırlama — ok kertiğinde yayın kirişinin geçtiği oluk · ok kertiklerindeki kiriş olukları · yayın ucunda kiriş için açılmış kertik · yayda kiriş halkası için yer hazırlamak · yay ucunda kiriş yerini son delme işleminden önce hazırlamak
  الحراث مجرى الوتر في الفوق والجمع أحرثة (jamhara)؛ الأحرثة مجاري الأوتار في الأفواق لأنها تجمعها (maqayis)؛ الحرثة الفرضة التي في طرف القوس للوتر (tahdhib)؛ حرثت القوس إذا هيأت موضعا لعروة الوتر (tahdhib)؛ الزندة تحرث ثم تكظر بعد الحرث (tahdhib)
- **B008** toprağı çiğneyip bozma veya ekim için çevirme — insanların çiğneyip kabartarak bozduğu toprak · toprağı çiğneyip bozmak veya ekim için çevirmek · toynaklarla dövülmüş yol
  أرض محروثة ومحرثة وطئها الناس حتى أحرثوها وحرثوها (tahdhib)؛ وطئت حتى أثاروها وهو فساد (tahdhib)؛ تقلب للزرع (tahdhib)؛ المحجة المكدودة بالحوافر (tahdhib)
- **B009** insan erkeğinin cinsel organı dibindeki damar ya da erkek eşeğin cinsel organ kökü — erkeğin cinsel organının dibindeki damar · erkek eşeğin cinsel organının kökü
  الحَرْثة عرق في أصل أداف الرجل (tahdhib)؛ الحَرْث أصل جردان الحمار (tahdhib)
- **B010** kişi, topluluk ve yer adları — kazanan anlamıyla verilmiş bir erkek adı · geleneksel bir kişi adı · geleneksel bir kişi adı · geleneksel bir kişi adı · geleneksel bir kişi adı · aslan için kullanılan bir lakap · bir dağ tepesi adı · iki kişi ya da iki topluluk için kullanılan ikili adlandırma · bir soy topluluğunu belirten kısaltılmış ad
  به سمي الرجل حارثا (maqayis)؛ سمت العرب حارثا وحراثا وحريثا ومحرثا وحرثان (jamhara)؛ أبو الحارث كنية الأسد (sihah)؛ الحارث قلة من قلل الجولان (sihah)؛ الحارثان في باهلة (sihah)؛ أصدق الأسماء الحارث (tahdhib;mufradat)

## ء خ ر (root_000019): 42:20 ٱلْءَاخِرَةِ, 42:20 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ز ي د (root_000657): 42:20 نَزِدْ, 42:23 نَّزِدْ, 42:26 وَيَزِيدُهُم

- **B001** artma, büyüme ya da artırma — kendiliğinden arttı ve büyüdü · onu artırdı veya ona daha çok verdi · artış, büyüme veya bir şeye başka bir öğenin katılması · ek artış ya da fazladan şey · artmış veya başkasından fazla · artış · artış · belirtilen sayıyı aşan topluluk · bunu ötekine ek olarak yaparım · anlatılandan da fazlası oldu · fiyat yükseldi
  أصل يدل على الفضل (maqayis)؛ زدته زيدا وزيادة (ayn)؛ الزيادة النمو (sihah)؛ زاد الشيء يزيد وزدته أنا أزيده زيادة (tahdhib)؛ الزيادة أن ينضم إلى ما عليه الشيء في نفسه شيء آخر (mufradat)
- **B002** fazladan bölüm ya da uzantı — fazlalıklar ve ek parçalar · uzuvlardaki fazladan parçalar veya uzantılar · karaciğerin yanında asılı küçük parça · olağandan fazla parmaklar · bedendeki fazladan parçalara dayanarak verilmiş takma ad
  شيء كثير الزيايد أي الزيادات (maqayis)؛ زيادة الكبد قطيعة معلقة منها (ayn)؛ زائدة الكبد هنية منها صغيرة إلى جنبها (sihah)؛ الزوائد في قوائم الدابة (tahdhib)؛ زيادة الأصابع والزوائد في قوائم الدابة وزيادة الكبد (mufradat)
- **B003** ölçüyü zorlayarak aşma [kalıp] — kükremesini, sesini ve saldırısını ölçünün ötesine taşıyan aslan · yürüyüşünde gücünü aşacak ölçüde kendini zorlayan dişi deve · konuşurken gereğinden fazla zorlamaya ve abartıya kaçmak · anlatıda yalan söyleme veya yapmacık abartıya kaçma · orta hızlı yürüyüşten daha hızlı gitme
  الأسد ذو زوائد وهو الذي يتزيد في زئيره وصولته (maqayis)؛ الناقة تتزيد في سيرها أي تتكلف فوق قدرها (ayn)؛ التزيد في الحديث الكذب (sihah)؛ الإنسان يتزيد في حديثه وكلامه إذا تكلف مجاوزة ما ينبغي (tahdhib)
- **B004** daha çoğunu isteme ve açık artırmada yarışma — onu yetersiz buldu veya hoşnut olmadığı bir iş için kınadı · verdiğinden daha çoğunu ondan istedi · sana verilenden daha çoğunu ister misin? · alıcılar malın fiyatını artırarak birbirleriyle yarıştı · daha var mı; bağlama göre daha çoğunu isteme ya da doluluğu bildirme
  استزاده أي استقصره (sihah)؛ إذا أعطى رجل رجلا مالا وطلب زيادة على ما أعطاه قيل قد استزاده (tahdhib)؛ تزايد أهل السوق على السلعة إذا بيعت فيمن يزيد (tahdhib)؛ هل من مزيد يجوز أن يكون ذلك استدعاء للزيادة (mufradat)
- **B005** yol azığı edinme ve azık kapları — o anki gereksinimin ötesinde saklanan yol azığı · yol azığı edinme ve yanına alma · birine yol azığı verdi · yol yiyeceğinin konduğu deri torba · su taşımaya yarayan tulum ya da kap · yol için su konan kap · su tulumları ve taşıma kapları
  المزادة مفعلة من الزيادة والجميع المزايد (ayn)؛ المزادة الرواية (sihah)؛ الزادة مفعلة من الزاد يتزود فيها الماء والمزود شبه جراب من أدم يتزود فيه الطعام للسفر (tahdhib)؛ الزاد المدخر الزائد على ما يحتاج إليه في الوقت والتزود أخذ الزاد (mufradat)

## ECHO ز و د (root_000653): for 42:20 نَزِدْ, 42:23 نَّزِدْ, 42:26 وَيَزِيدُهُم: withheld observed target; not identity

- **B001** geçişte taşınacak birikimi hazırlama, edinme veya verme — yol gereğini hazırlayıp hazır bulundurma · yolculukta veya konaklamada kullanılmak üzere saklanan yiyecek ve gereç · birine yolculukta kullanacağı yiyecek ve gereci verme · yol gereğini edinmek veya bir geçişte taşınacak iş ve kazanç biriktirmek · yanında yol gereği ya da işlerinden doğan birikimi taşıyan kimse
  أصل يدل على انتقال بخير من عمل أو كسب؛ الزاد وهو الطعام يتخذ للسفر (maqayis)؛ الزاد وهو الطعام الذي يتخذ للسفر والحضر؛ كل منتقل بخير أو عمل فهو متزود (ayn)؛ الزاد طعام يتخذ السفر؛ زودت الرجل فتزود (sihah)؛ كل من انتقل معه بخير أو شر من عمل أو كسب فقد تزود (tahdhib)؛ الزاد المدخر الزائد؛ التزود أخذ الزاد (mufradat)
- **B002** yol yiyeceği kabı — yol yiyeceğinin konduğu kap · boyunları yol yiyeceği kaplarına benzetilenler
  المزود الوعاء يجعل للزاد؛ تلقب العجم برقاب المزاود (maqayis)؛ المزود وعاء الزاد (ayn)؛ المزود ما يجعل فيه الزاد؛ العرب تلقب العجم برقاب المزاود (sihah)؛ المزود وعاء يجعل فيه الزاد (tahdhib)؛ المزود ما يجعل فيه الزاد من الطعام (mufradat)
- **B003** binicinin taşıdığı büyük deri su kabı — binicinin taşıdığı büyük deri su kabı · eyer arkasına bağlanan tek büyük su kabı · büyük deri su kapları
  المزادة بمنزلة راوية لا عزلاء لها؛ المزاد بغير ها هي الفردة التي يحتقبها الراكب خلف رحله؛ سميت مزادة لأنها تزيد على السطيحتين (tahdhib)؛ المزادة ما يجعل فيه الزاد من الماء (mufradat)

## د ن و (root_000493): 42:20 ٱلدُّنْيَا, 42:36 ٱلدُّنْيَا

- **B001** yakın olma, yaklaşma veya yaklaştırma — yakın olmak veya yaklaşmak · yakında bulunan · birini veya bir şeyi yaklaştırmak · iki şeyi birbirine yaklaştırmak · yakın akrabalık · adım adım yaklaşmak · birbirlerine yaklaşmak · yakın olan · yakın dereceden amca oğlu · yemekte önündeki yakın kısımdan yemek
  أصل واحد وهو المقاربة (maqayis)؛ دنوت منه دنوا وأدنيت غيري (sihah)؛ الدنو القرب بالذات أو بالحكم (mufradat)؛ دانيت بين الأمرين قاربت بينهما (maqayis;sihah;mufradat)؛ دناوة أي قرابة (sihah)؛ فدنوا أي كلوا مما يليكم (maqayis;sihah;mufradat)
- **B002** bu yaşam veya karşıtına göre yakın, küçük ya da ilk olan — bu yaşam, ilk yaşam · bu yaşama ilişkin · bu yaşama ilişkin · karşıtına göre daha yakın veya daha küçük olan · ilk iş olarak · yakın kıyı veya yakın taraf
  سميت الدنيا لدنوها (maqayis;sihah)؛ يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب (mufradat)؛ الدنيا والآخرة (mufradat)؛ العدوة الدنيا والعدوة القصوى (mufradat)؛ لقيته أدنى دنى أي أول شيء (maqayis;sihah)
- **B003** değersizlik, aşağı konum, güçsüzlük veya eksiklik — değersiz ve aşağı kimse · değersizleşmek veya alçalmak · kusur veya eksiklik · küçük ve değersiz işlerin peşine düşmek · daha kötü ve aşağı olan
  الدني من الرجال الضعيف الدون (maqayis)؛ الدنىء الدون مهموز (maqayis)؛ الدنية النقيصة (maqayis)؛ الدني بمعنى الدون فهو مهموز (sihah)؛ يدني في الأمور تدنية أي يتتبع صغيرها وخسيسها (sihah)؛ خص الدنيء بالحقير القدر (mufradat)؛ الأدنى عن الأرذل (mufradat)
- **B004** dişi hayvanda doğumun yaklaşması [kalıp] — kısrak veya dişi devenin doğumunun yaklaşması
  أدنت الفرس وغيرها إذا دنا نتاجها (maqayis)؛ أدنت الناقة إذا دنا نتاجها (sihah)؛ أدنت الفرس دنا نتاجها (mufradat)
- **B005** üst gövdesi göğsüne doğru kapanmış erkek — üst gövdesi göğsüne doğru kapanmış erkek
  الأدنأ من الرجال الذي فيه انكباب على صدره (maqayis)؛ لأن أعلاه دان من وسطه (maqayis)

## ء ت ي (root_000009): 42:20 نُؤْتِهِۦ, 42:36 أُوتِيتُم, 42:47 يَأْتِىَ

- **B001** gelmek, ulaşmak — gelmek veya ulaşmak · ona gitmek veya yanına varmak · geciktiğini düşünüp gelmesini istemek
  أتى يأتي أتيا (jamhara)؛ الإتيان المجئ (sihah)؛ أتاني فلان إتيانا وأتيا وأتية وأتوة (tahdhib;maqayis)؛ الإتيان مجيء بسهولة (mufradat)
- **B002** vermek; getirip sunmak — vermek; bir şeyi getirip sunmak
  آتى يؤتي إيتاء في معنى أعطى (jamhara)؛ آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به (sihah)؛ الإتياء الإعطاء (tahdhib)؛ الإيتاء الإعطاء (mufradat;maqayis)
- **B003** uygun yoldan ele almak ve elverişli hale gelmek — işin uygun yönü ve tutulacak yolu · uyma ve razı olma · bir şeyin ona elverişli hale gelmesi · ihtiyacını uygun yoldan ve incelikle yürütmek
  أتيت الأمر من مأتاته (sihah;maqayis)؛ آتيته على ذلك الأمر مواتاة إذا وافقته وطاوعته (sihah)؛ آتيت فلانا على أمره مؤاتاة وهو حسن المطاوعة (maqayis)؛ تأتى له الشيء أي تهيأ (sihah)؛ تأتى فلان لحاجته إذا ترفق لها (tahdhib)
- **B004** su kanalı açmak ve akışı yönlendirmek — su kanalı; suyu tutan odun ve yaprak birikintisi · bu suya yol açıp akışını yönlendirmek
  أت لمائك أي سهل له سبيلا وذلك السبيل الأتي (jamhara)؛ الأتي الجدول يؤتيه الرجل إلى أرضه (sihah)؛ كل جدول ماء أتي (tahdhib)؛ أت لهذا الماء أي سهل جريه (maqayis)؛ الأتي ما وقع في النهر من خشب أو ورق مما يحبس الماء (maqayis)
- **B005** başka bölgeden gelen sel [kalıp] — yağmur alan başka bir bölgeden gelen sel
  الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك (jamhara)؛ سيل أتي وأتاوي إذا جاءك ولم يصبك مطره (sihah)؛ المسيل الذي يأتي من بلد قد مطر فيه إلى بلد لم يمطر فيه أتي (tahdhib)؛ السيل المار على وجهه أتي وأتاوي (mufradat)؛ الأتي أيضا السيل الذي يأتي من بلد غير بلدك (maqayis)
- **B006** topluluğa yabancı kimse [kalıp] — içinde bulunduğu topluluğa mensup olmayan yabancı adam
  رجل أتي وأتاوي وهو الغريب (jamhara)؛ الاتي أيضا والاتاوى الغريب (sihah)؛ إنما هو أتي فينا (tahdhib)؛ به شبه الغريب فقيل أتاوي (mufradat)؛ رجل أتي أي غريب في قوم ليس منهم وأتاوي كذلك (maqayis)
- **B007** gelişip bol ürün vermek — ekin ve hurmanın gelişmesi, ürünü ve bol verimi · çalkalanan tulumun yağının ortaya çıkması
  أتاء هذا النخل أي ثمره وكذلك الزرع (jamhara)؛ الاتاء البركة والنماء وحمل النخل (sihah)؛ جاء أتوه (sihah;mufradat)؛ إتاء النخلة ريعها وزكاؤها وكثرة ثمارها (tahdhib)؛ الإتاء نماء الزرع والنخل وأتى الماء إتاء أي كثر (maqayis)
- **B008** ödenen vergi; rüşvet — vergi veya baş vergisi; rüşvet · ona rüşvet vermek
  الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك (jamhara)؛ الاتاوة الخراج والجمع الاتاوي (sihah)؛ الإتاوة الخراج وجمعها الأتاوى والإتاوات (tahdhib)؛ أتوته أتوة إذا رشوته إتاوة وهي الرشوة (tahdhib)
- **B009** devenin ön ayaklarını geri getirişi [kalıp] — devenin yürürken ön ayaklarını geri getirişi
  ما أحسن أتو قوائم الناقة وأتيها في السير (jamhara)؛ ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير (sihah)؛ ما أحسن أتو يديها وأتي يديها يعني رجع يديها (tahdhib)
- **B010** işlek ana yol, son sınır ve karşı hizası — yarışın son sınırı; işlek ana yol veya yol kavşağı · yarışın son sınırı veya yolun ana kesimi · bir evin karşısında veya aynı hizasında
  الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل (sihah)؛ الميتاء الطريق العامر ومجتمع الطريق (sihah)؛ داري بميتاء دار فلان وميداء دار فلان أي تلقاء داره ومحاذية لها (sihah)؛ طريق ميتاء مسلوك وميتاء الطريق وميداؤه محجته (tahdhib)
- **B011** felakete uğramak, kaybetmek veya düşmanca ele geçirilmek [kalıp] — ölüm, ağır hastalık, bela veya kırığa uğramak · malı yok olmak · uğruna öldürülmek, götürülmek veya yenilmek · düşman yaklaşmış olmak
  أتى على فلان أتو أي موت أو بلاء أصابه (tahdhib)؛ الأتو المرض الشديد أو كسر يد أو رجل أو موت (tahdhib)؛ أتي على يد فلان إذا هلك له مال (tahdhib)؛ يؤتى دونه أي يذهب به ويغلب عليه (tahdhib)؛ أتي فلان إذا أطل عليه العدو (tahdhib)؛ الإتيان يقال في الخير وفي الشر (mufradat)
- **B012** dişi devenin çiftleşmek istemesi [kalıp] — dişi devenin çiftleşmek için erkek deve istemesi
  استأتت الناقة استئتاء مهموز أي ضبعت وأرادت الفحل (sihah)
- **B013** etkili ve işini yürüten adam [kalıp] — etkili ve işini yürütebilen adam
  رجل أتي إذا كان نافذا (maqayis)

## ن ص ب (root_001507): 42:20 نَّصِيبٍ (also echo for 42:30 أَصَٰبَكُم, 42:30 مُّصِيبَةٍ, 42:39 أَصَابَهُمُ, 42:48 تُصِبْهُمْ)

- **B001** dikme, dik durma ve yükselme — bir şeyi dikmek veya dik konuma kaldırmak · boynuzları dik olan · boynuzu dik veya göğsü yüksek dişi hayvan · havaya yükselmiş toz · perdeyi kaldırmak · kuş avlamak için tuzak kurmak · kazanın üzerine konduğu demir destek · dikili direk veya sütun
  أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)
- **B002** tapınma veya adak kesme taşı — tapınılan veya üzerinde adak kesilen dikili taş · tapınılan ya da adak kesilen dikili taşlar
  النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)
- **B003** sınır işareti veya kuyu-havuz taşı — dikili işaret veya havuz kenarı taşı · kuyu ya da havuz ağzının çevresine dizilen taşlar · taşlardan kurulmuş havuz · topluluk veya sınır için dikilmiş işaret
  النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)
- **B004** yorgunluk ve yıpratıcı sıkıntı — yorgunluk, bitkinlik, zahmet ve sıkıntı · hastalığın verdiği bitkinlik · beni yordu ve huzursuz etti · yorucu veya yorgunluk içindeki
  النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)
- **B005** belirlenmiş pay — pay veya bir şeyden ayrılan belirli bölüm · pay
  النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)
- **B006** temel veya sabit başvuru noktası — bir şeyin temeli ve dönülen başvuru noktası · bıçağın sapı veya arka bölümü · mal için mali yükümlülük doğuran alt miktar · köken, soy ve aileden gelen saygınlık · güneşin battığı ve döndüğü yer
  نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)
- **B007** dil bilgisinde yükleme konumu [kalıp] — çekimde üst konumun karşıtı olan yükleme konumu · yükleme konumuna getirilmiş sözcük
  في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)
- **B008** birine savaş veya düşmanlıkla karşı çıkma — birine savaş veya düşmanlıkla karşı çıkmak · ona düşman olmak veya düşmanlık yöneltmek
  ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)
- **B009** özel bir şarkı veya ezgi türü — yolcuların söylediği özel ezgi türü · hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi · yolcu ezgisini söyledi
  النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)
- **B010** yolculuğu yumuşak sürdürme veya artırma — gün boyunca yumuşak biçimde ilerlediler · yol alışlarını yükseltip artırdılar
  نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)

## ء ذ ن (root_000022): 42:21 يَأْذَنۢ, 42:51 بِإِذْنِهِۦ

- **B001** kulak ve kulak biçimli tutamak — kulak; işitme organı · kulaklar · kulaklı · kulaklı ya da uzun kulaklı dişi hayvan · büyük kulaklı · kupanın ya da kabın kulak biçimli tutamağı · ayakkabıya kulak biçimli bağ ya da işaret yapmak · kulağına vurmak ya da kulağını ovmak
  الأذن معروفة مؤنثة؛ أذن كل ذي أذن (maqayis)؛ هو أذن؛ الأذن العروة أي عروة الكوز (ayn)؛ الأذن تخفف وتثقل وهي مؤنثة؛ رجل أذاني؛ أذنت النعل إذا جعلت لها أذنا (sihah)؛ آذان الكيزان عراها؛ أذنت فلانا إذا ضربت أذنه (tahdhib)؛ الأذن الجارحة وشبه به أذن القدر وغيرها (mufradat)
- **B002** kulak verip benimseme — her söyleneni dinleyip kabul eden kişi · her şeyi dinleyen kişi · kulak vermek, dikkatle dinlemek · buyruğu dinleyip uymak
  الأذن الاستماع؛ رجل سامع من كل أحد أذن (maqayis)؛ أذن له استمع؛ رجل أذنة يستمع لكل شيء (ayn)؛ أذن له أذنا استمع؛ رجل أذن إذا كان يسمع مقال كل أحد ويقبله (sihah)؛ أذنت للشيء إذا استمعت له؛ هو أذن أي يستمع فيقبل؛ وأذنت لربها أي سمعت سمع طاعة وقبول (tahdhib)؛ أذن استمع؛ ويستعار لمن كثر استماعه (mufradat)
- **B003** bilme ve başkasına bildirme — bu konuyu bilmek · ona bunu bildirmek · duyuru; özellikle namazı ve vaktini bildiren çağrı · bildirme ve duyurma · duyuru ya da sesli çağrı · çağrının her yandan ulaştığı yer · duyurucu ya da çağrıcı · namaz vakitlerini çağrıyla bildiren kişi · namaz çağrısının yapıldığı kule ya da yüksek yer
  الأصل الآخر العلم والإعلام؛ آذنني فلان أعلمني؛ الأذان اسم التأذين؛ الأذين المكان يأتيه الأذان؛ الأذين المؤذن (maqayis)؛ أذنت بهذا الشيء أي علمت؛ آذنني أعلمني؛ الأذان اسم للتأذين؛ هل سمعت الأذان من المئذنة (ayn)؛ أذن بمعنى علم؛ الأذان الإعلام؛ أذان الصلاة معروف؛ المئذنة المنارة؛ آذنتك بالشيء أعلمتكه (sihah)؛ آذنته إذا أعلمته؛ الأذان للصلاة إعلام بها وبوقتها؛ المؤذن المعلم بأوقات الصلاة؛ ثم أذن مؤذن أي نادى مناد (tahdhib)؛ يستعمل ذلك في العلم؛ المؤذن كل من يعلم بشيء نداء (mufradat)
- **B004** onay verme ve yetkilendirme — bir işi yapmasına onay vermek · onay veya yetkilendirme; ayrıca bilgisi ya da buyruğuyla yapılan iş · birinden onay istemek · içeri girişe onay veren kapı görevlisi
  فعله بإذني أي بعلمي ويجوز بأمري؛ أذن لي في كذا (maqayis)؛ فعله بإذني أي بعلمي وهو في معنى بأمري؛ الذي يأذن بالدخول (ayn)؛ أذن له في الشيء؛ ائذن لي على الأمير؛ الآذن الحاجب (sihah)؛ أذنت لفلان في أمر كذا؛ استأذنت فلانا؛ بإذن الله أي بعلمه؛ ويكون بإذنه أي بأمره (tahdhib)؛ ائذن لي؛ الأذن والأذان لما يسمع ويعبر بذلك عن العلم (mufradat)
- **B005** kendini bağlayan kesin bildirim — 
  تأذن ربكم؛ التأذن من قولك لأفعلن كذا تريد به إيجاب الفعل؛ وأوضح منه أعلم ربكم (maqayis)؛ التأذن من قولك تأذنت لأفعلن كذا يراد به إيجاب الفعل (ayn)؛ تأذنت لأفعلن كذا وكذا يراد به إيجاب الفعل (tahdhib)

## ف ص ل (root_001159): 42:21 ٱلْفَصْلِ

- **B001** bir şeyi ötekinden ayırıp arada belirgin sınır açma — ayırma, ayırt etme veya kesip koparma · ayrılma ya da kesilme sonucunda kopma · kasabın koyunu eklem yerlerinden parçalaması
  تدل على تمييز الشيء من الشيء وإبانته عنه (maqayis)؛ الفصل بون ما بين الشيئين (ayn;tahdhib)؛ فصلت الشيء فصلا (maqayis)؛ فصلت الشئ فانفصل أي قطعته فانقطع (sihah)؛ إبانة أحد الشيئين من الآخر حتى يكون بينهما فرجة (mufradat)
- **B002** doğruyla yanlışı ayırıp uyuşmazlığı bitiren kesin karar — doğruyla yanlışı ayıran yargıç ya da karar · kararı kesinleştiren söz
  الفيصل الحاكم (maqayis)؛ الفصل القضاء بين الحق والباطل (ayn;tahdhib)؛ الفيصل الحاكم ويقال القضاء بين الحق والباطل (sihah)؛ يبين الحق من الباطل ويفصل بين الناس بالحكم (mufradat)؛ فصل الخطاب ما فيه قطع الحكم (mufradat)
- **B003** sütten kesme ve annesinden ayrılmış deve yavrusu — annesinden ayrılmış deve yavrusu · sütten kesme, yavruyu emmeden ayırma
  الفصيل ولد الناقة إذا افتصل عن أمه (maqayis)؛ الفصلان جمع الفصيل وهو ولد الإبل (ayn)؛ فصلت الرضيع عن أمه فصالا وافتصلته إذا فطمته (sihah)؛ الفصيل ولد الناقة إذا فصل عن أمه (sihah)؛ الفصال الفطام (tahdhib)؛ فصلت المرأة ولدها أي فطمته (tahdhib)؛ الفصال التفريق بين الصبي والرضاع (mufradat)؛ الفصيل اختص بالحوار (mufradat)
- **B004** konuları ayırıp belirginleştiren dil — konuları ayırıp belirginleştiren dil
  المفصل اللسان لأن به تفصل الأمور وتميز (maqayis)؛ المفصل اللسان (ayn)؛ المفصل بالكسر اللسان (sihah)؛ المفصل بفتح الميم اللسان (tahdhib)؛ لسان مفصل (mufradat)
- **B005** eklem, iki kemik veya beden bölümünün birleşme yeri — eklem, kemiklerin veya beden üyelerinin birleşme yeri
  المفاصل مفاصل العظام (maqayis)؛ الفصل من الجسد موضع المفصل (ayn;tahdhib)؛ المفصل واحد مفاصل الأعضاء (sihah)؛ المفاصل الواحد مفصل (mufradat)
- **B006** dağlık veya kumlu arazideki ayırıcı ara kesit — iki dağ arasında veya dağ içinde bulunan, kimi zaman su geçen ara kesit
  المفصل ما بين الجبلين والجمع مفاصل (maqayis)؛ المفصل كل مكان في الجبل لا تطلع عليه الشمس (ayn;tahdhib)؛ من فصل الحبل من الرملة يكون بينهما رضراض وحصى صغار يصفو ماؤه (sihah)؛ مفرق ما بين الجبل والسهل (tahdhib)؛ صدوع في الجبال يسيل منها الماء (tahdhib)
- **B007** ana çevre duvarından daha kısa duvar — şehir veya korunak çevre duvarından daha kısa duvar
  الفصيل حائط دون سور المدينة (maqayis)؛ الفصيل حائط قصير دون سور المدينة والحصن (ayn;sihah;tahdhib)؛ الفصيل حائط دون سور المدينة (mufradat)
- **B008** inançla inançsızlığı ayırdığı söylenen harcama [kalıp] — inançlılık ile inançsızlığı ayırdığı söylenen harcama
  من أنفق نفقة فاصلة فله من الأجر كذا (maqayis;sihah)؛ التي فصلت بين إيمانه وكفره (maqayis;sihah)؛ نفقة تفصل بين الكفر والإيمان (mufradat)
- **B009** kişinin boyu içindeki en yakın soy kolu — kişinin en yakın soydaşları veya boyu içindeki yakın soy kolu
  الفصيلة فخذ الرجل من قومه الذين هو منهم (ayn;tahdhib)؛ فصيلة الرجل رهطه الأدنون (sihah;tahdhib)؛ فصيلة الرجل عشيرته المنفصلة عنه (mufradat)
- **B010** bir yerden çıkıp ayrılma; yazı için birinden ötekine gönderilme — bulunduğu yerden çıkmak veya ayrılmak · yazının bir kişiden ötekine gönderilmesi
  فصل من الناحية أي خرج (sihah)؛ فصل فلان من عندي فصولا إذا خرج (tahdhib)؛ فصل مني إليه كتاب إذا نفذ (tahdhib)؛ فصل القوم عن مكان كذا وانفصلوا فارقوه (mufradat)
- **B011** ölçü ve kutsal metinde söz parçalarını ayıran sınır birimleri — üç hareketli ses birimini bir duruk birimin izlediği ölçü dizisi · Kur'an'daki sözce sonları · Kur'an'ın kısa bölümlerin anlatıları ayırdığı son yedide birlik kesimi
  الفاصلة في العروض أن يجمع ثلاثة أحرف متحركة والرابع ساكن (ayn;tahdhib)؛ الفاصلة في العروض الصغرى والكبرى (sihah)؛ أواخر الآيات في كتاب الله فواصل (tahdhib)؛ المفصل من القرآن السبع الأخير وذلك للفصل بين القصص بالسور القصار (mufradat)؛ الفواصل أواخر الآي (mufradat)
- **B012** inciler arasına ayırıcı boncuklar yerleştirilmiş süs dizisi [kalıp] — inciler arasına ayırıcı boncuk veya değerli taş konmuş kolye
  عقد مفصل أي جعل بين كل لؤلؤتين خرزة (sihah)؛ فصلت الوشاح إذا كان نظمه مفصلا بأن يجعل بين كل لؤلؤتين مرجانة أو شذرة أو جوهرة (tahdhib)؛ فواصل القلادة شذر يفصل به بينها (mufradat)
- **B013** parçaları ve anlamları ayırarak ayrıntılı biçimde açıklama — parçaları ve anlamları ayırarak ayrıntılı biçimde açıklama
  التفصيل أيضا التبيين (sihah)؛ فصلناه بيناه (tahdhib)؛ مفصلات مبينات (tahdhib)؛ كل شيء فصلناه تفصيلا (mufradat)؛ فصلت إشارة إلى تبيانا لكل شيء (mufradat)
- **B014** ortakla ilişkiyi veya ortak işi ayırıp sonuçlandırma [kalıp] — ortaktan ayrılmak veya ortak işi onunla paylaşıp sonuçlandırmak
  فاصلت شريكي (sihah)
- **B015** ad cümlesindeki iki ögeyi ayıran üçüncü kişi adılı — ad cümlesindeki iki ögeyi ayıran üçüncü kişi adılına verilen dil bilgisi terimi
  الفصل عند البصريين بمنزلة العماد عند الكوفيين (tahdhib)؛ دخلت هو للفصل (tahdhib)
- **B016** başka yere taşınmış palmiye sürgünü — ilk yetişme yerinden başka yere taşınmış palmiye sürgünü
  الفسيلة المحولة تسمى الفصلة وهي الفصلات (tahdhib)؛ افتصلنا فصلات كثيرة أي حولناها (tahdhib)

## ء ل م (root_000046): 42:21 أَلِيمٌ, 42:42 أَلِيمٌ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ر ء ي (root_000531): 42:22 تَرَى, 42:44 وَتَرَى, 42:44 رَأَوُا۟, 42:45 وَتَرَىٰهُمْ

- **B001** gözle ya da içsel kavrayışla görme — gözle ya da içsel kavrayışla görmek · görme, gözle algılama · kendi gözüyle görme · yeni ayı görebilmek için dikkatle bakmaya çalıştık
  نظر وإبصار بعين أو بصيرة (maqayis)؛ رأيت بعيني رؤية ورأيته رأي العين (ayn;tahdhib)؛ الرؤية بالعين (sihah)؛ الرؤية إدراك المرئي بالحاسة (mufradat)
- **B002** düşünüp bir görüşe varma — bilmek, sanmak veya öyle olduğuna inanmak · görüş, kanı veya değerlendirme · düşünüp taşınmak ve bir görüşe varmak · ağır ağır ve dikkatle düşünme · bir görüşe varmak için düşünme · adamın görüşünü sordu · onunla görüş alışverişinde bulundu · gözle gördüğünün gereğince öyle sandı
  الرأي ما يراه الإنسان في الأمر (maqayis)؛ الرأي رأي القلب (ayn;tahdhib)؛ بمعنى العلم تتعدى إلى مفعولين ورأى في الفقه رأيا (sihah)؛ الرأي اعتقاد النفس والروية والتروية التفكر (mufradat)؛ استرأيت الرجل في الرأي أي استشرته (tahdhib)
- **B003** uykuda görülen düş — uykuda görülen düş · uykuda görülen düşler
  الرؤيا معروفة والجمع رؤى (maqayis)؛ رأيت رؤيا حسنة (ayn)؛ رأى في منامه رؤيا وجمع الرؤيا رؤى (sihah)؛ لا تجمع الرؤيا وتجمع الرؤيا رؤى (tahdhib)؛ الرؤيا ما يرى في المنام (mufradat)
- **B004** karşı karşıya gelip görünür olma — topluluk birbirini gördü · görünmek üzere karşıma çıktı · birbirine bakar ve karşılıklı konumda
  تراءى القوم إذا رأى بعضهم بعضا (maqayis)؛ تراءى القوم رأى بعضهم بعضا وتراءى لي فلان (ayn)؛ قوم رئاء وبيوتهم رئاء وتراءى الجمعان (sihah)؛ تراءينا أي تلاقينا فرأيته ورآني وداري ترى دار فلان (tahdhib)؛ تراءا الجمعان أي تقاربا وتقابلا ومنازلهم رئاء (mufradat)
- **B005** başkaları görsün diye yapma — başkaları görsün diye yapma · işini başkalarına gösteriş için yaptı · gösteriş yapmaya zorlandı veya özendi
  وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس (maqayis)؛ فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة (sihah)؛ يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة (tahdhib)؛ فعل ذلك رئاء الناس أي مراءاة (mufradat)
- **B006** görünüş, belirti ve yansıtıcı yüzey — ayna · aynada yüzüne baktı · güzel ve parlak dış görünüş · göze güzel görünen durum veya donanım · yüzde beliren budalalık belirtisi
  الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)؛ المرآة التي ينظر فيها والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر (ayn)؛ المرآة التي ينظر فيها والمرآة المنظر الحسن والرواء حسن المنظر ورأوة الحمق (sihah)؛ الرئي المنظر والرواء حسن المنظر والمرآة التي ينظر فيها ورأوة أي نظرة ودمامة (tahdhib)؛ المرآة ما يرى فيه صورة الأشياء (mufradat)
- **B007** aybaşı sonu izi ve denetleme bezi — aybaşı sonrası hafif sarı, beyaz veya bulanık iz · aybaşı belirtisi olarak görülen iz
  الترئية والترية ما تراه الحائض من صفرة بعد دم حيض أو أمارات الحيض (maqayis)؛ الترية الخرقة التي تعرف بها المرأة حيضها من طهرها والماء الأصفر عند انقطاع الدم (jamhara)؛ الترية الشيء الخفي اليسير من الصفرة والكدرة (sihah)؛ الترية ما تراه المرأة من بقية حيضها من صفرة أو بياض (tahdhib)
- **B008** kişiye görünen görünmez yoldaş — kişiye alışıp onunla ilişki kuran görünmez varlık · görünmez yoldaşı ona göründü
  الرئي جني يتعرض للرجل يريه كهانة وطبا (ayn)؛ به رئي من الجن أي مس (sihah)؛ رئي من الجن وهو الذي يعتاد الإنسان من الجن وأرأى إذا صار له رئي من الجن (tahdhib)؛ مع فلان رئي من الجن (mufradat)
- **B009** akciğer ve ona gelen zarar — akciğer · akciğerine vurdu veya sapladı · akciğerinden yakındı
  الرئة موضع الريح والنفس وجمعها الرئات والرئين (ayn)؛ الرئة مهموزة وتجمع على رئين ورأيته أي أصبت رئته (sihah)؛ أرأى إذا اشتكى رئته (tahdhib)؛ الرئة العضو المنتشر عن القلب ورئته إذا ضربت رئته (mufradat)
- **B010** meme gelişmesiyle gebeliğin belli olması — dişi devenin gebeliği memesi gelişince belli oldu · dişi koyunun gebeliği memesi büyüyünce belli oldu
  أرأت الناقة إذا أرأى ضرعها أنها أقربت وأنزلت (ayn)؛ أرأت الشاة إذا عظم ضرعها قبل ولادها (sihah)؛ إذا استبان حمل الشاة وعظم ضرعها قيل أرأت (tahdhib)؛ أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها (mufradat)
- **B011** görünür yere dikilen bayrak — dikili bayrak veya görünür işaret · bayrağı dikti
  الراية من رايات الأعلام (ayn)؛ الراية العلم لا تهمزها العرب وأصلها الهمز (tahdhib)؛ الراية العلامة المنصوبة للرؤية (mufradat)
- **B012** gösterip görmesini sağlama — bakması için aynayı ona tuttu · ona gösterip görmesini sağladı · ver, uzat · Tanrı onu düşmanını sevindirecek bir duruma düşürdü
  أرني يا فلان ثوبك لأراه وأرنا للمعاطاة (ayn)؛ أريته الشيء فرآه (sihah)؛ رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها وأرى الله الناس بفلان (tahdhib)؛ أرنا وبما أراك الله أي بما علمك (mufradat)
- **B013** söyler misin, bir düşün — söyler misin, bir düşün · söyleyin bakalım, bir düşünün
  أرأيتك وأنت تقول أخبرني (tahdhib)؛ يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه (mufradat)

## ECHO ر و ي (root_000615): for 42:22 تَرَى, 42:44 وَتَرَى, 42:44 رَأَوُا۟, 42:45 وَتَرَىٰهُمْ: withheld observed target; not identity

- **B001** suya kanma ve susuzluğun giderilmesi — susuzluğu sona erinceye kadar su içmek · suya kanmak · suya kanmışlık; susuzluğun sona ermesi · suya kanmış, susuzluğu kalmamış · tatlı ve içeni iyice kandıran bol su · bol sulu pınar
  خلاف العطش (maqayis)؛ رويت من الماء ريا وارتويت وترويت (sihah)؛ روي فلان من الماء يروى ريا فهو ريان (tahdhib)؛ ماء رواء وروى (sihah;tahdhib;mufradat)؛ عين رية (sihah)
- **B002** başkaları için su çekip getirme — ailesine su getirip taşımak · topluluk için su çekmek · su çekmede kullanılan yük hayvanı veya su çeken kişi · su taşımaya yarayan büyük tulum · su taşıma işini meslek edinen kimse · hacıların sonraki günler için su tedarik ettiği gün
  رويت على أهلي أروي ريا (maqayis;sihah;tahdhib)؛ رويت القوم أرويهم إذا استقيت لهم (sihah;tahdhib)؛ الراوية البعير أو البغل أو الحمار الذي يستقى عليه (sihah)؛ الراوية هو البعير الذي يستقى عليه الماء والرجل المستقي أيضا راوية (tahdhib)؛ يوم التروية سمي به لأنهم يرتوون فيه من الماء (sihah;tahdhib)
- **B003** anlatı veya şiir aktarma — anlatıyı veya şiiri aktarmak · anlatı veya şiir aktaran kimse · çok sayıda şiir ya da anlatı aktaran kimse · birine şiiri tekrar ederek ezberletmek
  رويت الحديث والشعر رواية فأنا راو (sihah)؛ روى فلان حديثا وشعرا يرويه رواية فهو راو (tahdhib)؛ روى فلان فلانا شعرا إذا رواه له حتى حفظه للرواية عنه (tahdhib)؛ الذي يأتي القوم بعلم أو خبر فيرويه كأنه أتاهم بريهم من ذلك (maqayis)
- **B004** enine boyuna düşünüp değerlendirme — enine boyuna düşünme; değerlendirme · bir mesele üzerinde düşünüp değerlendirmek
  الرَّوِيَّة التفكر في الأمر (sihah)؛ رويت في الأمر إذا نظرت فيه وفكرت (sihah)؛ روأت في الأمر وريأت فكرت (tahdhib)
- **B005** birinden beklenen ihtiyaç veya talep [kalıp] — birinden beklenen ihtiyaç veya talep
  لنا قبلك روية أي حاجة (sihah)؛ لنا عند فلان روية وأشكلة وهما الحاجة (tahdhib)
- **B006** geriye kalan bölüm veya miktar — borçtan ya da başka bir şeyden kalan miktar
  الرَّوِيَّة البقية من الدين ونحوه (sihah)؛ بقيت منه روية أي بقية مثل التلية (tahdhib)
- **B007** yük bağlama ipi — yükü veya su tulumlarını yük hayvanına bağlayan ip · yükü veya su tulumlarını özel iple hayvana bağlamak · su tulumlarını yük hayvanına bağlayan ip
  الرِّوَاء حبل يشد به المتاع على البعير (sihah)؛ رويته على الرجل إذا شددته على ظهر البعير (sihah)؛ الرِّوَاء الحبل الذي يروى به على الراوية إذا عكمت المزادتان (tahdhib)؛ يقال له المروى وجمعه مراوى (tahdhib)
- **B008** yapıya göre dolgunlaşma veya suya kavuşma [kalıp] — ipin lifleri kalınlaşıp bükümü sıkılaşmak · eklemler dengeli ve dolgun hale gelmek · sırtı semirip dolgunlaşmış at · kurak yere dikildikten sonra kökten sulanmak
  ارتوى الحبل غلظت قواه (sihah)؛ ارتوت مفاصل الرجل اعتدلت وغلظت (sihah)؛ ارتوت مفاصل الدابة إذا اعتدلت وغلظت (tahdhib)؛ فرس ريان الظهر إذا سمن متناه (tahdhib)؛ ارتوت النخلة إذا غرست في قفر ثم سقيت في أصلها (tahdhib)
- **B009** hoş ve güzel dış görünüş — hoş dış görünüş; görünen güzellik · kökeni tartışmalı bir görünüş güzelliği biçimi
  رجل له رُوَاء أي منظر (sihah)؛ من لم يهمز رئيا جعله من روي كأنه ريان من الحسن (mufradat)
- **B010** hoş koku — hoş koku; bir şeyin güzel kokusu
  طيبة الرِّيَا إذا كانت عطرة الجرم (tahdhib)؛ ريا كل شيء طيب رائحته (tahdhib)
- **B011** dişi dağ keçisi — dağ keçisi; özellikle dişisi, bazı kullanımlarda erkeği de · çok sayıda dağ keçisi; dağ keçileri topluluğu · kadın adı
  الإِرْوِيَّة الأنثى من الوعول (sihah)؛ أروى أيضا اسم امرأة (sihah)؛ الأُرْوِيَّة الأنثى من الوعول (tahdhib)؛ يقال للأنثى أروية وللذكر أروية (tahdhib)؛ لا تجمع بين الأروى والنعام (tahdhib)
- **B012** bayrak — bayrak; sancak
  الرَّايَة العلم (sihah)
- **B013** temel uyak harfi — şiir boyunca değişmeyen temel uyak harfi
  الرَّوِيّ حرف القافية (sihah)؛ قصيدتان على روي واحد (sihah)
- **B014** iri damlalı güçlü yağmur bulutu — iri damlalı, sert yağan yağmur bulutu
  الرَّوِيّ سحابة عظيمة القطر شديدة الوقع (sihah)
- **B015** topluluğun ağır yükümlülüklerini üstlenen ileri gelenler — topluluk adına kan bedeli ve ağır yükümlülükleri üstlenen ileri gelenler
  يقال لسادة القوم الروايا (tahdhib)؛ شبه السيد الذي تحمل الديات عن الحي بالبعير الراوية (tahdhib)؛ روايا الثقل حوامل ثقل الديات (tahdhib)

## ك س ب (root_001296): 42:22 كَسَبُوا۟, 42:30 كَسَبَتْ, 42:34 كَسَبُوا۟

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

## و ق ع (root_001675): 42:22 وَاقِعٌۢ

- **B001** düşüp gerçekleşme — düşmek ve yerini bulmak · sözün veya hükmün kesinleşmesi · başlarına gelmek · hemen secdeye kapanmak
  وقع الشيء وقوعا فهو واقع (maqayis)؛ وقع الشيء موقعه (sihah)؛ وقع القول والحكم إذا وجب (tahdhib)؛ الوقوع ثبوت الشيء وسقوطه (mufradat)
- **B002** ağır felaket — büyük hesap günü veya ağır felaket
  الواقعة القيامة لأنها تقع بالخلق فتغشاهم (maqayis)؛ الواقعة القيامة (sihah)؛ الواقعة النازلة من صروف الدهر (tahdhib)؛ الواقعة لا تقال إلا في الشدة والمكروه (mufradat)
- **B003** yağışın düşmesi ve düştüğü yer — yağmurun damla damla düşmesi · sonbaharın ilk yağmurunun toprağa düşmesi · yağışın düştüğü yerler
  وقع الغيث سقط متفرقا ومواقع الغيث مساقطه (maqayis)؛ وقع المطر (ayn)؛ مواقع الغيث مساقطه (sihah)؛ وقع ربيع بالأرض لأول مطر يقع في الخريف (tahdhib)؛ وقع المطر نحو سقط ومواقع الغيث مساقطه (mufradat)
- **B004** çarpma ve çarpma sesi — vuruş veya çarpma sesi
  الوقع وقعة الضرب بالشيء (ayn)؛ سمعت وقع المطر وهو شدة ضربه الأرض (tahdhib)؛ سمعت لحوافر الدواب وقعا ووقوعا (tahdhib)؛ وقع الحديد صوته (mufradat)
- **B005** savaşta çarpışma ve düşmana saldırma — savaş çarpışması · savaşta karşılaşma · bir topluluğa savaşta saldırıp zarar vermek · savaşta karşılıklı çarpışmak
  الوقعة صدمة الحرب (maqayis)؛ الوقعة صدمة الحرب والوقيعة القتال (sihah)؛ وقع بهم وأوقع بهم في الحرب (tahdhib)؛ المواقعة في الحرب والإيقاع في شن الحرب بالوقعة (mufradat)
- **B006** kuşun konması ve konduğu yer — kuşun yere, ağaca veya yuvasına konması · kanatlarını kapatmış kuşa benzetilen yıldız · kuşun alıştığı konma yeri
  من وقع الطائر (maqayis)؛ موقعة الطائر موضعه الذي يقع عليه (maqayis)؛ يقال للطير إذا كان على أرض أو شجر هن وقوع (ayn)؛ ميقعة البازي الموضع الذي يألفه فيقع عليه (sihah)؛ طائر واقع إذا كان على شجر أو موكن (tahdhib)؛ الموضع الذي يستقر فيه الطير موقع (mufradat)
- **B007** hayvanın yere çöküp yatması [kalıp] — devenin çökmesi, hayvanın yere yatması
  وقعت الدواب والإبل أي ربضت تشبيها بوقوع الطير (ayn)؛ يقال للإبل إذا بركت والدواب إذا ربضت قد وقعت (tahdhib)
- **B008** su birikintisi yeri ve su tutan toprak — dağınık su birikme yerleri · kayada su biriken oyuk · suyu emmeyip tutan toprak veya çayır
  الوقائع مناقع الماء المتفرقة (maqayis)؛ الوقيعة نقرة في متن حجر يستنقع فيها الماء (sihah)؛ أرض وقيعة لا تكاد تنشف الماء (tahdhib)؛ أوقعت الروضة إذا أمسكت الماء (tahdhib)؛ المكان الذي يستقر الماء فيه الوقيعة (mufradat)
- **B009** taşla bilemek ve keskinleştirmek — demiri veya bıçağı taşla bilemek · taşla bilenmiş kılıç, bıçak veya toynak · taştan aşınmış ayak veya toynak acısı
  وقعت الحديدة أقعها وقعا إذا حددتها (maqayis)؛ الحافر الوقيع ما شحذ بالحجر (maqayis)؛ الوقيع من السيوف ما شحذ بالحجر (sihah)؛ وقعت الحديدة أقعها وقعا إذا حددتها (tahdhib)؛ وقعته الحجارة توقيعا كما يسن الحديد بالحجارة (tahdhib)؛ وقعت الحديدة إذا حددتها بالميقعة (mufradat)
- **B010** devenin sırtındaki eyer yarası izi — devenin sırtındaki eyer yarası ve sıyrık izi · sırtında yara izleri bulunan veya sıkıntı görmüş
  التوقيع وهو أثر الدبر يظهر البعير (maqayis)؛ التوقيع الدبر (sihah)؛ الموقع البعير الذي به آثار الدبر (tahdhib)؛ التوقيع سحج بأطراف عظام الدابة من الركوب (tahdhib)؛ التوقيع أثر الدبر بظهر البعير (mufradat)
- **B011** belgeye sonradan eklenen not — tamamlanmış belgeye eklenen not veya satır arası yazı
  التوقيع ما يلحق بالكتاب بعد الفراغ منه (maqayis)؛ التوقيع ما يوقع في الكتاب (sihah)؛ توقيع الكاتب في الكتاب المكتوب (tahdhib)؛ التوقيع في الكتاب أن يلحق فيه شيئا بعد الفراغ منه (tahdhib)؛ أثر الكتابة في الكتاب ومنه استعير التوقيع في القصص (mufradat)
- **B012** gerçekleşmesini beklemek veya olası saymak — gerçekleşmesini beklemek · bir şey hakkında kesin olmayan düşünce veya söz ileri sürmek
  توقعت الشيء انتظرته متى يقع (maqayis)؛ توقعت الشيء واستوقعته أي انتظرت كونه (sihah)؛ التوقع تنظر الأمر (tahdhib)؛ التوقيع بالظن والكلام الرمي يعتمده ليقع عليه وهمه (tahdhib)؛ استعمال لفظة الوقوع تأكيد للوجوب (mufradat)
- **B013** arkasından kötülemek ve ayıplamak [kalıp] — insanları çekiştirmek ve ayıplamak · insanların arkasından kötü konuşma
  وقع فلان في فلان وأوقع به (maqayis)؛ الوقيعة في الناس الغيبة (sihah)؛ وقع في الناس وقيعة أي اغتابهم (sihah)؛ وقع فلان في فلان إذا عابه (tahdhib)؛ عنه استعير الوقيعة في الإنسان (mufradat)
- **B014** cinsel birleşme — cinsel birleşme ve eşle birlikte olma
  الوقاع مواقعة الرجل امرأته إذا باضعها وخالطها (tahdhib)؛ يكنى بالمواقعة عن الجماع (mufradat)
- **B015** dairesel yakma damgası — deveye vurulan dairesel yakma damgası veya başın üstüne uygulanan özel yakma
  كويت البعير وقاع دائرة واحدة (maqayis)؛ كويته وقاع هي الدائرة (sihah)؛ كويته وقاع وهي الدائرة (tahdhib)؛ كواه وقاع إذا كوى أم رأسه (tahdhib)
- **B016** özel adlandırma kümesi: yüksek yer ve ince bulut — dağdan alçak yükselti veya dağın yüksek bölümü · ince veya yayvan bulut
  الوقع المكان المرتفع من الجبل (maqayis)؛ الوق الطخاف من السحاب (maqayis)؛ الوقع المكان المرتفع من الجبل (sihah)؛ الوقع السحاب الرقيق (sihah)؛ الوقع المكان المرتفع وهو دون الجبل (tahdhib)

## ECHO ق و ع (root_001270): for 42:22 وَاقِعٌۢ: withheld observed target; not identity

- **B001** düz ve yayvan alan — düz, yayvan ve pürüzsüz arazi · düzlük veya düzlükler topluluğu · düz arazi, düzlük · düzlükler, yayvan araziler · düzlükler anlamındaki çoğul biçimler · küçük düzlük anlamındaki iki küçültme biçimi · evin avlusu veya açık iç alanı · hurmanın üzerine serildiği düz yüzey
  أصل يدل على تبسط في مكان (maqayis)؛ القاع الأرض الملساء (maqayis)؛ القوع المسطح الذي يبسط فيه التمر (maqayis)؛ القاع المستوي من الأرض والقيعة مثل القاع وقاعة الدار ساحتها (sihah)؛ القاع ما انبسط من الأرض والقيعة جمع القاع وما استوى من الأرض لا حصى فيه ولا حجارة (tahdhib)
- **B002** çiftleşmek üzere dişinin üzerine çıkma — erkek devenin dişi deveyle çiftleşmesi · erkek devenin dişi devenin üzerine çıkıp çiftleşmesi · erkek devenin çiftleşme isteğiyle kızışması · bukalemunun ağaca tırmanması
  القوع وهو ضراب الفحل الناقة فليس من هذا الباب لأنه من المقلوب وأصله قعوه (maqayis)؛ قاع الفحل على الناقة يقوع قوعا وقياعا إذا نزا وهو قلب قعا واقتاع الفحل إذا هاج (sihah)؛ تقوع الحرباء الشجرة إذا علاها كما يتقوع الفحل الناقة (tahdhib)
- **B003** erkek ve dişi tavşanı ayrı adlandırma — erkek tavşan · dişi tavşan
  شذ عن هذا الباب قولهم إن القواع الذكر من الأرانب (maqayis)؛ القواع الذكر من الأرانب والقواعة الأرنب الأنثى (tahdhib)
- **B004** çok uluyan kurt — çok uluyan kurt
  القواع الذئب الصياح (tahdhib)

## ECHO  (): for 42:22 وَاقِعٌۢ: non-dominant observed target (1 occ.); not identity

- () no Turkish dictionary entry

## ص ل ح (root_000876): 42:22 ٱلصَّٰلِحَٰتِ, 42:23 ٱلصَّٰلِحَٰتِ, 42:26 ٱلصَّٰلِحَٰتِ, 42:40 وَأَصْلَحَ

- **B001** iyi ve düzgün olma; düzeltme — iyilik, düzgünlük ve bozulmamışlık · iyi ve düzgün duruma gelmek · kendisi iyi ve düzgün olan kişi; iyi ve yararlı iş · işlerini düzelten veya başkasını iyi duruma getiren kimse · bozukluğu giderip iyi ve düzgün duruma getirme · hayvana iyi davranmak · iyilik ya da yarar sağlayan şey · iyi ve yararlı duruma getirmeye çalışma
  أصل واحد يدل على خلاف الفساد (maqayis)؛ الصلاح نقيض الطلاح ورجل صالح ومصلح وأصلحت إلى الدابة أحسنت إليها (ayn)؛ الصلاح ضد الطلاح وصلح الرجل صلاحا وصلوحا (jamhara)؛ الصلاح ضد الفساد والاصلاح نقيض الإفساد والمصلحة والاستصلاح (sihah)؛ الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال وإصلاح الله تعالى الإنسان (mufradat)
- **B002** barışma ve uzlaşma — barışma, uzlaşma ve aradaki soğukluğun giderilmesi · birbiriyle barışıp uzlaşmak
  والصلح تصالح القوم بينهم (ayn)؛ الصلاح بكسر الصاد المصالحة والاسم الصلح وقد اصطلحا وتصالحا واصالحا (sihah)؛ الصلح يختص بإزالة النفار بين الناس، يقال اصطلحوا وتصالحوا (mufradat)
- **B003** sana uygun olma [kalıp] — bu sana uygundur; bu sana uyar
  وهذا الشئ يصلح لك، أي هو من بابتك (sihah)
- **B004** kişi adı olan kök türevleri — bu kökten türemiş kişi adları; bunlardan biri bir peygamber adıdır
  وقد سمت العرب صالحا وصليحا ومصلحا (jamhara)؛ وصالح اسم للنبي عليه السلام (mufradat)
- **B005** bir kent ve bir nehir için özel adlar — belirli bir kentin özel adı · belirli bir nehrin özel adı
  إن مكة تسمى صلاحا (maqayis)؛ والصلح نهر بميسان (ayn)؛ وصلاح في وزن حذام وقطام وهو اسم مكة (jamhara)؛ وصلاح مثل قطام اسم مكة (sihah)

## ر و ض (root_000611): 42:22 رَوْضَاتِ

- **B001** yeşil otluk veya yayvan sığ su birikintisi — otluk ve yeşillik alan; cennet bahçesi · teknenin dibini örten yayvan su birikintisi · su ve yeşillik bulunan çayırlık; yayvan su birikintisi · çıplak araziyi çayırlığa dönüştürmek · bir yerde çayırlıkların çoğalması
  ومن الباب الروضة (maqayis)؛ الروض والروضة والريضان جمع الروض والرياض جمع الروضة (ayn)؛ الروضة من البقل والعشب (sihah)؛ في الحوض روضة من ماء إذا غطى أسفله (sihah)؛ الروض مستنقع الماء والخضرة (mufradat)
- **B002** yaklaşık yarım tulum su — yaklaşık yarım su tulumu kadar su
  والروض نحو من نصف القربة (ayn)؛ والروض نحو من نصف القربة ماء (sihah)
- **B003** bir gruba yetecek suyu verip susuzluğunu giderme — vadide suyun birikmesi veya çoğalması · havuzda suyun birikmesi · belirli sayıda kişiye yetip onları suya kandıran kap · onlara içirip susuzluklarını gidermek · iyice suya kanıncaya kadar içmek
  وقد اراضهم إذا أرواهم (maqayis)؛ أتانا بإناء يريض كذا وكذا رجلا وقد أراضهم إذا أرواهم بعض الري (ayn)؛ شربوا حتى أراضوا أي رووا فنقعوا بالري (sihah)؛ أراضهم أرواهم (mufradat)
- **B004** genişleyip ferahlama; kimi kullanımda eğitilebilirlik — yerin genişlemesi · iç dünyanın ferah ve hoş olması; ayrıca eğitilmeye elverişli olma ihtimali
  استراض المكان اتسع (maqayis)؛ ما دام النفس مستريضا أي متسعا (maqayis)؛ واستراض المكان أي اتسع (sihah)؛ النفس مستريضة أي متسعة طيبة (sihah)؛ مستراضة أي قابلة للرياضة أو معناه متسعة (mufradat)
- **B005** tekrarlı alıştırmayla uysallık ve beceri kazandırma — hayvana yürümeyi öğretip onu uysallaştırmak · tekrarlı alıştırmayla yatkınlık ve ustalık kazanma · yoğun biçimde alıştırıp yumuşatmak ve öğretmek · eğitilmiş ve uysallaştırılmış hayvan · eğitime yeni alınmış ve henüz güçlük çıkaran hayvan ya da genç kişi
  رضت الناقة أروضها رياضة (maqayis)؛ رضت الدابة أروضها رياضة أي علمتها السير (ayn)؛ رضت المهر أروضه رياضا ورياضة فهو مروض (sihah)؛ الرياضة كثرة استعمال النفس ليسلس ويمهر ومنه رضت الدابة (mufradat)
- **B006** incelikle idare ederek bir işe çekme [kalıp] — birini incelikle idare ederek bir işe çekmeye çalışmak
  فلان يراوض فلانا على أمر كذا أي يداريه ليدخله فيه (sihah)

## ف ض ل (root_001163): 42:22 ٱلْفَضْلُ, 42:26 فَضْلِهِۦ

- **B001** gereksinimi aşan veya bir işlemden sonra kalan fazlalık — gereksinimden fazla olan ve geride kalan bölüm · herhangi bir şeyden artakalan kısım · artık, geriye kalan bölüm · bir miktarı geride kaldı · yiyeceğin bir kısmını bıraktı · ondan bir miktar geride bıraktım · ganimet bölüşümünden artanlar · sudan geriye kalanlar · malın gelirleri ve getirileri · içki ve benzerlerinden kalan artıklar
  الفضل الزيادة والخير (maqayis); الفضالة ما فضل من كل شيء والفضلة البقية من كل شيء (ayn;tahdhib); الفضل الزيادة عن الاقتصاد (mufradat); الفضل والفضيلة خلاف النقص والنقيصة (sihah); أفضل من الأرض والطعام إذا ترك منه شيئا (ayn); فضول الغنائم ما فضل من القسم وفضلات الماء بقاياه (tahdhib)
- **B002** nitelikçe üstün olma, yüksek değer taşıma ve karşılaştırmada öne geçme — üstünlük, yüksek değer ve derece · yüksek nitelik ve değer derecesi · topluluktaki kişiler arasındaki üstünlük farkı · birini başkasından üstün sayma · birini üstünlükte geçti · adamı üstünlükte geçtim · onunla üstünlük yarışına girip onu geçtim · yüksek nitelikli, değerli · başkası tarafından üstünlükte geçilmiş · üstünlük karşılaştırması
  الفضيلة الدرجة والرفعة في الفضل (ayn); الفضيلة الدرجة الرفيعة في الفضل (tahdhib); الفضل والفضيلة خلاف النقص والنقيصة (sihah); الفضل إذا استعمل لزيادة أحد الشيئين على الآخر فعلى ثلاثة أضرب (mufradat); التفاضل بين القوم أن يكون بعضهم أفضل من بعض (tahdhib); فاضلته ففضلته إذا غلبته بالفضل (sihah)
- **B003** başkasına gönüllü iyilik etme ve yükümlülük dışı bağış verme — başkasına iyilik etme · birine kendi imkânından verip iyilik etti · başkasına iyilik ve bağışta bulunma · verilmesi zorunlu olmayan bağış · çok iyilik yapan ve eli açık kişi
  الإفضال الإحسان (maqayis;sihah); أفضل فلان على فلان أناله من فضله وأحسن إليه (ayn;tahdhib); التفضل التطول على غيرك (ayn;tahdhib); كل عطية لا تلزم من يعطي يقال لها فضل (mufradat); رجل مفضال كثير الخير والمعروف (tahdhib)
- **B004** akranlarına karşı üstünlük iddia etme ve daha yüksek konum isteme — akranlarına karşı üstünlük iddiasında bulunan kişi · başkalarından daha yüksek konum isteme · size karşı daha yüksek konum istemek
  المتفضل فالمدعي للفضل على أضرابه وأقرانه (maqayis); المتفضل أيضا الذي يدعي الفضل على أقرانه (sihah); يريد أن يكون له الفضل عليكم في القدر والمنزلة وليس من التفضل الذي هو بمعنى الإفضال والتطول (ayn;tahdhib)
- **B005** giysiyi omuzlara dolayarak kuşanma veya evde tek giysiyle bulunma — giysiyi omuzlara dolayarak kuşanma · üstüne tek giysi almış erkek · evde tek giysiyle bulunan kadın · uçları omuzda çaprazlanarak kuşanılan giysi · erkeğin evde giydiği tek giysi · kadının tek başına giydiği giysi · tek giysiyi kuşanışının güzel olması
  التفضل التوشح (maqayis;ayn;tahdhib); رجل فضل ومتفضل وامرأة فضل ومتفضلة (ayn;tahdhib); الفضل الذي عليه قميص ورداء وليس عليه إزار ولا سراويل (maqayis); تفضلت المرأة في بيتها إذا كانت في ثوب واحد (sihah); الفضال الثوب الواحد يتفضل به الرجل (ayn;tahdhib)

## ب ش ر (root_000120): 42:23 يُبَشِّرُ, 42:51 لِبَشَرٍ

- **B001** derinin dış yüzü ve toprağın beliren bitkisi — derinin görünen dış yüzü · toprağın üzerinde beliren bitki örtüsü · toprak bitkisini çıkardı
  البشرة ظاهر جلد الإنسان (maqayis;sihah;mufradat)؛ البشرة أعلى جلد الوجه والجسد (ayn;tahdhib)؛ بشرة الأرض ما ظهر من نباتها وأبشرت الأرض إذا أخرجت نباتها (maqayis;sihah;tahdhib;mufradat)
- **B002** insan ya da insanlık — insan ya da insanlık
  وسمى البشر بشرا لظهورهم (maqayis)؛ البشر الإنسان الواحد رجلا كان أو امرأة (ayn)؛ البشر اسم يقع على الناس (jamhara)؛ البشر الخلق (sihah;tahdhib)؛ عبر عن الإنسان بالبشر اعتبارا بظهور جلده (mufradat)
- **B003** doğrudan temas etme veya işi bizzat yürütme [kalıp] — bir erkeğin bir kadınla ten tene yakınlaşması · kadına doğrudan tenle temas etme · işin başında bizzat bulunup onu yürütme
  باشر الرجل المرأة إفضاؤه ببشرته إلى بشرتها (maqayis)؛ مباشرة الرجل المرأة لتضام أبشارهما (ayn;tahdhib)؛ مباشرة المرأة ملامستها (sihah)؛ باشر الرجل المرأة إذا ألصق بشرته ببشرتها (jamhara)؛ المباشرة الإفضاء بالبشرتين (mufradat)؛ مباشرة الأمر أن تحضره بنفسك (ayn;sihah;tahdhib)
- **B004** dış katmanı soyma, soyulan parça ve yüzeydekini tüketme — işlenmiş derinin dış yüzünü soydu · derinin dış katmanını soyma · işlenmiş deriden soyulup düşen parça · çekirgeler yerin üstündekileri yedi
  بشرت الأديم إذا قشرت وجهه (maqayis)؛ البشر قشرك البشرة عن الجلد (ayn)؛ بشرت الأديم إذا قشرت بشرته وبشارة الأديم ما سقط منه (jamhara)؛ بشرت الأديم إذا أخذت بشرته (sihah;tahdhib)؛ بشرت الأديم أصبت بشرته وبشر الجراد الأرض إذا أكلته (mufradat)؛ بشر الجراد الأرض إذا أكل ما عليها (sihah;tahdhib)
- **B005** sevindirici haber verme; kötü haberde açık nitelemeli alaycı bildirim — adama sevindirici haber verdi · ona sevindirici bir haber verdi · sevindirici haber · sevindirici haber · iyi ya da kötü haberi getiren kişi · onlara acı verici cezayı alaycı biçimde haber verdi · sevindirici haberi alınca sevindi · topluluk üyeleri birbirlerine sevindirici haber verdiler
  بشرت فلانا تبشيرا وذلك يكون بالخير وربما حمل عليه غيره من الشر (maqayis)؛ البشارة ما بشرت به والبشير المبشر بخير أو شر والبشرى الاسم (ayn;tahdhib)؛ بشرت الرجل وبشرته بما يسر به والبشرى والبشارة اسم لما بشرت به (jamhara)؛ البشارة المطلقة لا تكون إلا بالخير وإنما تكون بالشر إذا كانت مقيدة به (sihah)؛ أخبرته بسار بسط بشرة وجهه ويقال للخبر السار البشارة والبشرى (mufradat)
- **B006** güler yüzlülük ve güzel görünüş — güler yüzlülük · güzellik ve hoş görünüş · güzel yüzlü kişi · güzel yüzlü kadın · yaradılışı ve ten rengi güzel genç kadın · güzel ya da orta yapılı, ne zayıf ne semiz deve
  البشير الحسن الوجه والبشارة الجمال (maqayis)؛ البشارة الجمال وامرأة بشيرة (ayn)؛ البشر طلاقة الوجه وفلان حسن البشر والبشارة الجمال وحسن الهيئة (jamhara)؛ حسن البشر أي طلق الوجه والبشير الجميل وناقة بشيرة أي حسنة (sihah)؛ فلان يلقاني ببشر أي بوجه منبسط عند السرور ورجل بشير الوجه وامرأة بشيرة الوجه (tahdhib)؛ تباشير الوجه وبشره ما يبدو من سروره (mufradat)
- **B007** bir şeyin ilk belirtileri ve başlangıç görünümleri — sabahın ilk ışıkları · hurmanın ilk olgunlaşma belirtileri · yağmurun yaklaştığını bildiren rüzgârlar · bir şey tamamlanmadan önce beliren ilk izler
  تباشير الصبح أوائله وكذلك أوائل كل شيء (maqayis;ayn;sihah)؛ تباشير النخل أول ما يرطب ورأى الناس التباشير في النخل إذا رأوا الحمرة والصفرة (jamhara)؛ التباشير طرائق ضوء الصبح في الليل وآثار الرياح وآثار جنب الدابة (tahdhib)؛ المبشرات الرياح التي تبشر بالغيث (maqayis;ayn;sihah;tahdhib;mufradat)؛ تباشير الوجه وبشره ما يبدو من سروره وتباشير الصبح ما يبدو من أوائله وتباشير النخيل ما يبدو من رطبه (mufradat)
- **B008** yumuşaklıkla sağlamlığı ve dışla iç erdemleri birleştiren tam yetkinlik — yumuşaklıkla sağlamlığı ve iç-dış erdemleri birleştiren yetkin kişi · her yönden yetkin, iç ve dış erdemleri birleştiren kadın
  فلان مؤدم مبشر إذا كان كاملا من الرجال كأنه جمع لين الأدمة وخشونة البشرة (maqayis;sihah)؛ رجل مؤدم مبشر وهو الذي قد جمع لينا وشدة مع المعرفة بالأمور (tahdhib)؛ فلان مؤدم مبشر عبر بذلك عن الكامل الذي يجمع بين الفضيلتين الظاهرة والباطنة (mufradat)؛ فلانة مؤدمة مبشرة إذا كانت تامة في كل وجه (tahdhib)

## س ء ل (root_000661): 42:23 أَسْـَٔلُكُمْ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 42:23 أَسْـَٔلُكُمْ: withheld observed target; not identity

- **B001** nazikçe ve fark ettirmeden çekip çıkarma — bir şeyi çekip çıkarmak · kılıcı kınından çekmek · hamurdaki kılı ayıklayıp çıkarmak
  سللت الشيء أسله سلا (maqayis;sihah;tahdhib)؛ إخراجك الشعر من العجين (ayn;tahdhib)؛ سل الشيء من الشيء نزعه (mufradat)
- **B002** gizlice çalma — hırsızlık; gizli hırsızlık · gizli hırsızlık; ayrıca rüşvet · çalmak · hırsız
  السلة والإسلال السرقة (maqayis)؛ الإسلال السرقة الخفية (ayn;tahdhib)؛ الإسلال الرشوة والسرقة (sihah)؛ سل الشيء من البيت على سبيل السرقة (mufradat)
- **B003** kökenden çıkan yavru veya öz — oğul; çocuk · kız evlat · tay ve dişi tay · kökten ayrılan öz; üreme maddesi
  السليل الولد (maqayis;sihah;tahdhib)؛ السلالة ما استل منه والنطفة سلالة الإنسان (sihah;tahdhib;mufradat)؛ السليل والسليلة المهر والمهرة (ayn;tahdhib)
- **B004** aradan sıyrılıp çıkma — dar yerden veya kalabalıktan sıyrılıp çıkma · aralarından çıkmak · topluluktan gizlice ayrılma
  الانسلال المضي والخروج من بين مضيق أو زحام (ayn;tahdhib)؛ انسل من بينهم أي خرج (sihah)؛ يتسللون منكم لواذا (tahdhib;mufradat)
- **B005** birbirine bağlı dizi — zincir; parçaların birbirine bağlanması · birbirine bağlı · bulut boyunca uzanan şimşek · birbirine eklenen kıvrımlı kum
  السلسلة اتصال الشيء بالشيء (maqayis)؛ شيء مسلسل متصل بعضه ببعض (sihah)؛ السلسلة معروفة وبرق ذو سلاسل ورمل ذو سلاسل (tahdhib)؛ ومنه السلسلة (mufradat)
- **B006** tatlı, duru ve kolay akan su — suyun boğazdan veya eğimden kolayca akması · tatlı, duru ve kolay içilen su · boğazdan kolay geçen duru şarap · kolay içilen, lezzetli ve hızlı akan kaynak suyu
  تسلسل الماء في الحلق إذا جرى وماء سلسل وسلسال (maqayis;sihah;tahdhib)؛ السلسل الماء العذب الصافي (ayn;tahdhib)؛ ماء سلسل متردد في مقره حتى صفا (mufradat)
- **B007** vadi içindeki su yolu veya çukur arazi — vadide dar su yolu; su toplayan alçak yer · vadi içindeki dar su yolları veya ağaçlı çukur yerler · geniş ve ağaçlı vadi
  السال مسيل في مضيق الوادي (maqayis;sihah;tahdhib)؛ السليل الوادي الواسع ينبت السلم والسمر (sihah;tahdhib)؛ السلان بطون من الأرض غامضة ذات شجر (tahdhib)
- **B008** tüberküloz — tüberküloz · tüberküloz · tüberküloz hastası
  السلال من المرض كأن لحمه قد سل (maqayis)؛ السل والسلال داء يأخذ الإنسان ويقتل (ayn)؛ السلال بالضم السل (sihah)؛ داء يهزل ويضني ويقتل (tahdhib)؛ مرض ينزع به اللحم والقوة (mufradat)
- **B009** atın yarıştaki güçlü ileri atılımı [kalıp] — atın yarışta ileri atılıp öne çıkması
  فرس شديد السلة وهي دفعته في سباقه (maqayis;sihah;tahdhib)؛ خرجت سلة هذا الفرس على سائر الخيل (ayn;tahdhib)
- **B010** çuvaldız — çuvaldız; iri dikiş iğnesi
  المسلة معروفة لأنها تسل الخيط سلا (maqayis)؛ المسلة المخيط وجمعه مسال (ayn)؛ المسلة واحدة المسال وهي الإبر العظام (sihah)
- **B011** sepet veya kapaklı kap — ekmek sepeti · kapaklı sepet veya kap
  سلة الخبز معروفة (sihah)؛ السلة السبذة المطبقة كالجؤنة (ayn;tahdhib)؛ سبذة الطين السلة (tahdhib)
- **B012** ince uzun şerit, lif veya uç — saçtan veya dokudan ince uzun şerit · hörgüçteki uzun şeritler veya burun içi doku parçaları · dilin ince ucu · uzun ve sivri diken · hurma dalından sıyrılmış ince parça
  السليلة عقبة أو عصبة أو لحمة شبه طرائق (ayn;tahdhib)؛ سليلة من شعر لما استل من ضريبته (sihah)؛ سلائل السنام طرائق طوال (tahdhib)؛ أسلة اللسان الطرف الرقيق (mufradat)؛ السلاءة من الشوك لأن فيها امتدادا (maqayis)
- **B013** biçime bağlı adlandırmalar — kumaşın giyilmekten incelmesi · kılıç yüzeyinin dalgalı parıltısı · çizgili süslü kumaş · eti azalıp bedeni oluklaşmış kişi
  تسلسل الثوب وتخلخل إذا لبس حتى رق؛ التسلسل بريق فرند السيف ودبيبه؛ ثوب ملسلس فيه وشي مخطط؛ المتسلسل الذي تخدد لحمه وقل
- **B014** dişleri düşmüş olma — dişleri düşmüş erkek, kadın veya koyun · yaşlılıktan dişleri düşmüş dişi deve
  السلة الناقة التي سقطت أسنانها؛ رجل سل وامرأة سلة وشاة سلة أي ساقطة الأسنان
- **B015** su teknesi destekleri arasındaki boşluk — su teknesinin dikili parçaları arasındaki boşluk
  السلة الفرجة بين نصائب الحوض

## ء ج ر (root_000015): 42:23 أَجْرًا, 42:40 فَأَجْرُهُۥ

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## و د د (root_001634): 42:23 ٱلْمَوَدَّةَ

- **B001** sevgi ve gönülden yakınlık besleme — bir kişiyi sevmek ve ona gönülden yönelmek · sevgi ve gönülden yakınlık · sevgi ve gönülden yakınlık · birinin sevgi bağı kurduğu kişi · çok seven kişi veya sevenlerden biri · çok seven ve sevgi gösteren · birbirini sevmek ve karşılıklı sevgi beslemek · sevgi ve yakınlık · sevgi ve yakınlık · yazılı ileti ya da sevgiyi doğuran öğüt benzeri bir araç
  كلمة تدل على محبة؛ وددته أحببته؛ الود من الوداد (maqayis;jamhara)؛ الود والود والود: المودة؛ ووددت الرجل إذا أحببته؛ الودود: المحب (sihah)؛ الود مصدر للمودة وكذلك الوداد؛ يقال في الحب الود والود والمودة والموددة؛ المودة: الكتاب (tahdhib)؛ الود: محبة الشيء؛ بأسباب المحبة من النصيحة ونحوها؛ فلان وديد فلان: مواده (mufradat)
- **B002** bir şeyin gerçekleşmesini dilemek — bir şeyin gerçekleşmesini dilemek · dileme ve istek · şöyle olmasını isterim
  ووددت أن ذاك كان إذا تمنيته؛ في التمني الودادة (maqayis)؛ وددت لو تفعل ذاك أي تمنيت (sihah)؛ الودادة مصدر وددت أود وهو من الأمنية؛ يود أحدهم لو يعمر أي يتمنى (tahdhib)؛ وتمني كونه؛ التمني هو تشهي حصول ما توده (mufradat)
- **B003** bölgesel söyleyişte kazık — kazık; bölgesel söyleyişte kaynaşmış biçim
  فأما الود فالوتد (maqayis)؛ الود لغة تميمية وهو الوتد (jamhara)؛ الود بالفتح الوتد في لغة أهل نجد كأنهم سكنوا التاء فأدغموها في الدال (sihah)؛ الود بلغة تميم الوتد (tahdhib)؛ الود: الوتد، وأصله يصح أن يكون وتد فأدغم (mufradat)
- **B004** dağ veya vadi özel adı — bilinen bir dağın özel adı · bilinen bir vadinin özel adı
  الود: جبل معروف؛ وودان: واد معروف (jamhara)؛ هو اسم جبل (sihah)
- **B005** bir putun özel adı — maddede anılan putun özel adı · bu putun adına bağlanan kişi adı
  وود: صنم هكذا فسر في التنزيل؛ وقد قالوا ود أيضا (jamhara)؛ وود: صنم كان لقوم نوح ثم صار لكلاب (sihah)؛ الود صنم كان لقوم نوح، وكان لقريش صنم يدعونه ودا؛ ومنه سمي عبد ود (tahdhib)؛ الود: صنم سمي بذلك (mufradat)

## ق ر ف (root_001220): 42:23 يَقْتَرِفْ

- **B001** kabuk ve soyulan kuru dış katman — dış kabuk · yaranın kurumuş kabuğunu soymak · kabuk bağlayıp soyulmak · kabuk parçası veya kurumuş deri · burun içinde kuruyup yapışmış kalıntı
  القرف وهو كل قشر (maqayis)؛ القرف قشر المقل ونحوه وقشر السدر وكل قرف قشر (ayn)؛ كل قشر قرف بالكسر والقرفة القشرة (sihah)؛ أصل القرف القشر وقرف كل شجرة قشرها وقرفة أنفه (tahdhib)؛ أصل القرف والاقتراف قشر اللحاء عن الشجر والجلدة عن الجرح (mufradat)
- **B002** deri kap, kızıl deri veya kullanılan bitki kabuğu — deriden yapılmış eşya kabı · tabaklamada veya sağaltımda kullanılan bitki kabuğu · kızıl deri veya onun gibi koyu kızıl
  القرف شيء يعمل من جلود يعمل فيه الخلع (maqayis)؛ القروف الأوعية الواحد قرف وهي التي تتخذ من الجلود (ayn)؛ القرف بالفتح وعاء من جلد يدبغ بالقرفة والقرفة من الأدوية (sihah)؛ القرف الأديم الأحمر والقروف الأدم الحمر والقرفة دواء معروف (tahdhib)
- **B003** edinmek, kazanmak ve üstüne almak — edinmek veya kazanmak · suç işlemek · ailesi için geçim kazanmak · yeni satın alınmış deve
  اقترفت الشيء اكتسبته وكأنه لابسه وادرعه (maqayis)؛ واقترف ذنبا أي أتاه وفعله واقترفت أي اكتسبت لأهلي (ayn)؛ فلان يقرف لعياله أي يكسب والاقتراف الاكتساب (sihah)؛ اقتراف أي اكتسب وبعير مقترف (tahdhib)؛ استعير الاقتراف للاكتساب حسنا كان أو سوءا والاقتراف في الإساءة أكثر استعمالا (mufradat)
- **B004** suçlamak, ayıplamak ve kuşkulanmak — birini bir suçla itham etmek · birini ayıplamak ve hakkında kötü konuşmak · kuşkulandığım veya aradığımı onda sandığım kişi
  فلان يقرف بكذا أي يرمى به والذى أتهمه (maqayis)؛ فلان يقرف بالسوء أي يرمى به ويظن به وقرفت فلانا أي وقعت فيه وذكرته بسوء (ayn)؛ قرفت الرجل أي عبته ويقرف بكذا أي يرمى به ويتهم (sihah)؛ قرفت الرجل بالذنب إذا رميته به وقرف فلانا إذا اتهمه بسرقة أو غيرها (tahdhib)؛ قرفت فلانا بكذا إذا عبته به أو اتهمته (mufradat)
- **B005** yaklaşmak, temas etmek ve karışmak — kötü bir işe bulaşmak · eşiyle cinsel birleşmede bulunmak · cinsel birleşme ve yakın temas · yaklaşmak ve temas etmek
  قارف فلان الخطيئة خالطها وقارف امرأته جامعها لأن كل واحد منهما لباس صاحبه (maqayis)؛ ما أقرفت لذلك أي ما دانيته ولا خالطت أهله وقارف الخطيئة خالطها وقارف امرأته جامعها (sihah)؛ ما أقرفت يدي شيئا مما تكره أي ما دانت وما قاربت ومن قراف غير احتلام أي من جماع وخلاط (tahdhib)
- **B006** soyu melezliğe yaklaşmış — soyu melezliğe yaklaşmış
  الفرس المقرف المداني الهجنة (maqayis)؛ فرس مقرف دانى الهجنة (ayn)؛ المقرف الذي دانى الهجنة من الفرس وغيره (sihah)؛ المقرف من الخيل الذي دانى الهجنة من قبل أبيه (tahdhib)؛ رجل مقرف هجين (mufradat)
- **B007** salgın ve hastalığa yakalanma tehlikesi — salgın veya hastalığa yakalanma tehlikesi · hastalığa yakalanmasından korkmak · hastalarla temas edip hastalanmak
  القرف الوباء يكون بالبلد (maqayis)؛ القرف بالتحريك مداناة المرض فإن من القرف التلف (sihah)؛ إني لأخشى على فلان القرف أي مداناة المرض والقرف الوباء (tahdhib)
- **B008** bunu yapması beklenir ve ona uygundur [kalıp] — bunu yapması beklenir ve ona uygundur
  إنه لقرف أن يفعل ذاك مثل قمن وخليق (tahdhib)

## ح س ن (root_000323): 42:23 حَسَنَةً, 42:23 حُسْنًا

- **B001** akla, eğilime veya duyulara göre güzel ve beğenilir olma — güzel ve beğenilir olma; güzellik · güzel olmak · güzel erkek · güzel kadın · güzel kadın · çok güzel kadın · çok güzel · güzel yanlar ve iyi nitelikler · bedenin güzel yeri
  الحسن ضد القبح (maqayis;sihah)؛ حسن الشيء فهو حسن (ayn)؛ الحسن نعت لما حسن (tahdhib)؛ كل مبهج مرغوب فيه (mufradat)؛ مستحسن من جهة العقل ومستحسن من جهة الهوى ومستحسن من جهة الحس (mufradat)؛ رجل حسن وامرأة حسناء وحسانة (maqayis)؛ الحسان الحسن جدا (ayn)؛ المحاسن ضد المساوىء (maqayis;ayn;sihah;tahdhib)
- **B002** bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme — bir şeyi güzelleştirmek · birine iyilik etmek · işini iyi ve ustalıkla yapmak · iyilik etme veya işi iyi yapma · iyilik eden veya işini iyi yapan kimse · sürekli iyilik eden kimse · güzel bulmak; beğenmek
  أحسنت إليه وبه (sihah)؛ وهو يحسن الشيء أي يعمله (sihah)؛ حسنت الشيء تحسينا زينته (sihah)؛ أحسن يا هذا فإنك محسان (tahdhib)؛ الإحسان ضد الإساءة (tahdhib)؛ أحسنت بفلان أي أحسنت إليه (tahdhib)؛ الإحسان يقال على وجهين الإنعام على الغير وإحسان في فعله (mufradat)؛ الإحسان فوق العدل (mufradat)
- **B003** kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç — kişiye ulaşan iyilik, bolluk veya ödül · iyi son veya en güzel karşılık; sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme · iki iyi sonuçtan biri: utkı ya da inancı uğruna ölme · kötü işleri gideren iyi işler, özellikle beş günlük tapınma
  للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى (ayn)؛ الحسنة خلاف السيئة (sihah)؛ الحسنى خلاف السوأى (sihah)؛ الحسنى هي الجنة وضد الحسنى السوءى (tahdhib)؛ إحدى الحسنيين يعني الظفر أو الشهادة (tahdhib)؛ حسنة أي نعمة (tahdhib)؛ أي غنيمة وخصب (tahdhib)؛ الحسنة يعبر عنها عن كل ما يسر من نعمة (mufradat)؛ خصب وسعة وظفر (mufradat)؛ من ثواب وما أصابك من سيئة أي من عقاب (mufradat)
- **B004** yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı — bir dağın, kum sırtının, kumluğun veya kum tepesinin adı · ön kolun bileğe yakın yarısı · ay · yüksek dağ · temiz ve yüksek bir kum tepesine oturmak · iki yerin veya iki kum sırtının birlikte anılışı
  الحسن جبل وحبل من حبال الرمل (maqayis)؛ الحسن من الذراع النصف الذي يلي الكوع (maqayis)؛ حسن اسم رملة لنبي سعد (ayn)؛ الحاسن القمر (sihah)؛ الحسن اسم رملة لبنى سعد (sihah)؛ الحسن نقا في ديار بني تميم (tahdhib)؛ أحسن الرجل إذا جلس على الحسن وهو الكثيب النقي العالي (tahdhib)؛ الحسين الجبل العالي (tahdhib)
- **B005** bir işteki en yüksek çabası ve erişebileceği son sınır — bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır · bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır
  حُسَيْناؤه أن يفعل كذا وحُسَيْناه مثله أي جهده وغايته (tahdhib)

## ش ك ر (root_000810): 42:23 شَكُورٌ, 42:33 شَكُورٍ

- **B001** İyiliği tanıyıp söz ve davranışla karşılık verme — iyiliği tanıma, iyilik yapanı övme ve iyiliği görünür kılma · yaptığı iyilikten ötürü onu övdüm ve iyiliğini kabul ettim · ona karşı duyduğum gönül borcunu göstermeye çabaladım · iyiliği kabul edip karşılık verme; iyiliği yadsımanın karşıtı · iyiliği içten kavrayıp kabul etme · iyilik yapanı sözle övme · iyiliğin değerine uygun davranışla karşılık verme · Tanrı için, kullarının az iyiliğini değerli sayıp onları ödüllendiren · Tanrı'ya bağlı davranarak gördüğü iyiliğe karşılık vermeye çok çabalayan kul
  الشكر الثناء على الإنسان بمعروف يوليكه (maqayis)؛ الشكر عرفان الإحسان ونشره وحمد موليه (ayn;tahdhib)؛ الشكر الثناء على المحسن بما أولاك من المعروف (sihah)؛ الشكر تصور النعمة وإظهارها (mufradat)؛ شكر القلب وشكر اللسان وشكر سائر الجوارح (mufradat)
- **B002** azla yetinip belirgin biçimde gelişme — az yemle yetinip semiren hayvan · çok az yağışla bile geliştiği görülen bitki için söylenen örnek söz
  حقيقة الشكر الرضا باليسير (maqayis)؛ فرس شكور إذا كفاه لسمنه العلف القليل (maqayis)؛ الشكور من الدواب ما يسمن بالعلف اليسير ويكفيه (ayn)؛ الشكور من الدواب ما يكفيه العلف القليل (sihah;tahdhib)؛ دابة شكور مظهرة بسمنها إسداء صاحبها إليها (mufradat)؛ أشكر من بروقة (maqayis;mufradat)
- **B003** dolup bollaşma — otlayınca sütü bollaşan veya memesi sütle dolan sağmal hayvan · sağmalın sütü otlaktan sonra bollaştı veya memesi sütle doldu · topluluğun hayvanları otlayıp süt vermeye başladı · bol sütlü deve veya koyun sürüsü · sütle dolu meme · hayvanın sütünü artıran ot · yazın bol süt veren veya sütü yıl boyunca süren dişi deve · yağlı et parçası
  الأصل الثاني الامتلاء والغزر في الشيء (maqayis)؛ حلوبة شكرة إذا أصابت حظا من مرعى فغزرت (maqayis)؛ الشكرة من الحلوبات التي تصيب حظا من بقل أو مرعى فتغزر عليه بعد قلة اللبن (ayn;tahdhib)؛ اشتكر الضرع املا لبنا (sihah)؛ ناقة شكرة ممتلئة الضرع من اللبن (mufradat)؛ الفدرة من اللحم إذا كانت سمينة شكرى (tahdhib)
- **B004** körpe sürgün ve ona benzetilen yeni oluşum — ağacın gövdesinden veya dibinden çıkan körpe sürgün · örgülerin arasından yeni çıkan saç · yavru kuşun ince tüyü · taze sürgünlere benzetilen küçük çocuklar veya genç kuşak · ağaç körpe sürgün çıkardı veya dalları çoğaldı · ağaçta körpe bir sürgün çıktı · yeni çıkan saçların veya bitki sürgünlerinin bütünü · belirli bir bitki türü
  الأصل الثالث الشكير من النبات (maqayis)؛ الشكير من النبات ما ينبت من ساق الشجر قضبان غضة (ayn)؛ شكرت الشجرة خرج منها الشكير (sihah)؛ الشكير من الشعر والنبات ما ينبت (tahdhib)؛ الشكير من الفرخ الزغب (tahdhib)؛ وشكير كثير أي ذرية صغار (tahdhib)؛ الشيكَران ضرب من النبت (sihah)؛ الشكير نبت في أصل الشجرة غض (mufradat)
- **B005** şiddetlenip etkisini artırma — yağmurun yere düşüşü şiddetlendi · rüzgarın esişi şiddetlendi · sıcak veya soğuk şiddetlendi
  اشتكرت السماء اشتد وقعها (sihah)؛ اشتكرت السماء وحفلت واغبرت كل ذلك من حين يجد وقع مطرها ويشتد (tahdhib)؛ اشتكرت الريح إذا اشتد هبوبها (tahdhib)؛ اشتكر الحر والبرد كذلك (tahdhib)
- **B006** kadın cinsel organı veya birleşme için örtmece — kadın cinsel organı veya cinsel birleşme için örtmece · kadının cinsel organı · kadınların cinsel organları
  الأصل الرابع الشكر وهو النكاح (maqayis)؛ شكر المرأة فرجها (maqayis;sihah;tahdhib)؛ الشكر الفرج (ayn)؛ الشكر يكنى به عن فرج المرأة وعن النكاح (mufradat)؛ الشكار فروج النساء واحدها شكر (tahdhib)
- **B007** iki ayrı boy adı kullanımı — kanıtta belirtilen bir boyun adı · kanıtta belirtilen başka bir boyun adı
  يشكر قبيلة من ربيعة (ayn;tahdhib)؛ شاكر قبيلة من اليمن من همدان (ayn;tahdhib)

## ف ر ي (root_001150): 42:24 ٱفْتَرَىٰ

- **B001** onarmak veya yapmak için kesip biçmek — onarmak veya dikmek için kesip biçmek · deriyi dikiş ve onarım için kesme · su tulumunu kesip biçerek yapmak
  فريت الشيء أفريه فريا وذلك قطعه لإصلاحه (maqayis)؛ فرى إذا خرز (maqayis)؛ فريته أصلحته (ayn)؛ فريت الشئ أفريه قطعته لأصلحه (sihah)؛ فريت المزادة خلقتها وصنعتها (sihah)؛ الفري قطع الجلد للخرز والإصلاح (mufradat)
- **B002** bozarak kesmek veya yarmak — bozacak biçimde kesmek veya yarmak · boyun damarlarını kesmek · yarılıp ayrılmak · yarılmış
  أفريته إذا أنت قطعته للإفساد (maqayis)؛ فريت الشيء بالسيف وبالشفرة قطعته وشققته (ayn)؛ التفري التشقق (ayn)؛ أفريت الأوداج قطعتها (sihah)؛ أفريت الشيء شققته فانفرى وتفرى (sihah)؛ أفرى الذئب بطن الشاة (sihah)؛ الإفراء للإفساد (mufradat)
- **B003** asılsız söz veya suçlama uydurmak — yalan veya ağır bir asılsızlık uydurmak · uydurulmuş yalan veya asılsız suçlama · bir yalanı üretip uydurmak
  فرى فلان كذبا يفريه إذا خلقه (maqayis)؛ فرى يفري فلان الكذب إذا اختلقه والفرية الكذب والقذف (ayn)؛ فرى فلان كذبا إذا خلقه وافتراه اختلقه والاسم الفرية (sihah)؛ الافتراء في الإفساد أكثر وكذلك استعمل في القرآن في الكذب والشرك والظلم (mufradat)
- **B004** şaşırtıcı, büyük ya da düzülmüş şey — şaşırtıcı, büyük veya yapılmış şey · şaşırtıcı, büyük ya da düzülmüş bir şey · işinde hayret verici bir şey yapmak
  فلان يفري الفري إذا كان يأتي بالعجب (maqayis)؛ الفرى أيضا مثل الفري وهو العجب (maqayis)؛ الفري الأمر العظيم في قوله لقد جئت شيئا فريا (ayn)؛ فلان يفري الفري إذا كان يأتي بالعجب في عمله (sihah)؛ لقد جئت شيئا فريا أي مصنوعا مختلقا وقيل عظيما (sihah)؛ لقد جئت شيئا فريا قيل معناه عظيما وقيل عجيبا وقيل مصنوعا (mufradat)
- **B005** yerin yarılıp kaynaklardan su fışkırtması [kalıp] — yerin kaynaklarla yarılıp su fışkırtması
  تفرت الأرض بالعيون انبجست (maqayis)؛ تبجست الأرض بالعيون وتفرت (ayn)؛ غمارا تفرى بالسلاح وبالدم (ayn)؛ تفرت الأرض بالعيون انبجست (sihah)
- **B006** kürk ve kalın örtü; baş derisi, zenginlik veya kuru bitki kümesi — giyilen kürk veya kalın deri örtü · kürkler · kürk giydi · baş derisi · varlık ve zenginlik · kuruyup bir araya kümelenmiş bitki topluluğu
  الفروة التي تلبس (maqayis)؛ فروة الرأس وهي جلدته (maqayis)؛ الفروة وهي الغنى والثروة (maqayis)؛ الفروة كل نبات مجتمع إذا يبس (maqayis)؛ التغطية والستر بشيء ثخين (maqayis)؛ الفرو الذي يلبس والجمع الفراء (sihah)؛ الفروة جلدة الرأس (sihah)؛ الفروة إبدال الثروة وهي الغنى (sihah)؛ الفروة قطعة نبات مجتمعة يابسة (sihah)
- **B007** şaşırıp bocalamak — şaşırıp bocalamak
  الفرى البهت والدهش يقال فري يفرى فرى (maqayis)؛ فري بالكسر يفرى فرى تحير ودهش (sihah)
- **B008** öne atılmaktan korkan kişi — öne atılmaktan korkan kişi
  الفرى الجبان سمي بذلك لأنه فري عن الإقدام أي قطع (maqayis)
- **B009** gürültülü patırtı — gürültülü patırtı
  الفرية الجلبة (ayn)

## ECHO ف ت ر (root_001125): for 42:24 ٱفْتَرَىٰ: withheld observed target; not identity

- **B001** şiddetini yitirerek zayıflama, yumuşama ve durulma — zayıflamak; sertliği ya da şiddeti azalıp durulmak · bir şeyi zayıflatmak ya da şiddetini gidermek · bir şeyi zayıflatmak veya ılık duruma getirmek · şiddetten sonra durulma, sertlikten sonra yumuşama ve güçten sonra zayıflama · bedende ya da iç dünyada kırılma ve güçsüzlük · keskin olmayan, durgun bakış · göz kapakları zayıflayıp bakışı kırılmak · içilince bedeni gevşeten şey · sıcak ile soğuk arasında, ılık su · sıcağın şiddeti kırılıp azalmak · yağmur suyunu boşaltıp kesilmek ve duraksamak · taşkınlıktan sonra benim izlediğim yola yönelip durulmak
  أصل صحيح يدل على ضعف في الشيء (maqayis)؛ الفترة الانكسار والضعف (sihah)؛ الفتور سكون بعد حدة ولين بعد شدة وضعف بعد قوة (mufradat)؛ فتر فلان إذا سكن عن حدته ولان بعد شدته (tahdhib)؛ فتر الإنسان إذا لانت مفاصله وضعفت (jamhara)؛ لا يفتر أي لا يضعف (maqayis)؛ لا يسكنون عن نشاطهم (mufradat)؛ المفتر الذي يفتر الجسد (tahdhib)؛ ماء فاتر بين الحار والبارد (tahdhib)؛ فتر مطر فرغ ماءه وكف وتحير (tahdhib)
- **B002** iki elçinin gelişi arasındaki dönem — iki elçinin gelişi arasındaki, yeni bir elçinin gelmediği dönem
  الفترة ما بين كل نبيين (jamhara)؛ الفترة ما بين الرسولين من رسل الله عزوجل (sihah)؛ على فترة من الرسل أي سكون حال عن مجيء رسول الله (mufradat)
- **B003** başparmak ile işaret parmağı arasındaki açıklık ve bununla ölçme — başparmak ile işaret parmağı açıldığında uçları arasında kalan açıklık · bir şeyi başparmak ile işaret parmağı arasındaki açıklığı kullanarak ölçmek
  الفتر ما بين طرف الإبهام وطرف السبابة إذا فتحتهما (maqayis)؛ الفتر ما بين طرفي السبابة وطرف الإبهام إذا فتحتهما (jamhara)؛ الفتر ما بين طرف السبابة والابهام إذا فتحتهما (sihah)؛ الفتر قدر ما بين طرف الإبهام وطرف المسبحة وقد فترت الشيء إذا قدرته بفترك (tahdhib)؛ الفتر ما بين طرف الإبهام وطرف السبابة يقال فترته بفتري (mufradat)

## ك ذ ب (root_001290): 42:24 كَذِبًا

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## خ ت م (root_000393): 42:24 يَخْتِمْ

- **B001** sonuna ulaşma ve tamamlama — bir şeyin sonuna ulaşıp onu tamamlamak · işi tamamlamak · Kur'an'ı veya bir sureyi okuyup sonuna ulaşmak · bir şeyi sona erdirmek · bir şeyin sonu ve bitiş bölümü · peygamberlerin sonuncusu · içeceğin sonu, son yudumu veya içildikten sonra kalan kısmı · vadinin en uç noktası · sonu iyi olmak · sonunda misk kokusu kalmak
  أصل واحد وهو بلوغ آخر الشيء (maqayis)؛ خاتمة السورة آخرها وخاتم العمل وكل شيء آخره وختام الوادي أقصاه (ayn)؛ ختمت الشيء إذا بلغت آخره وختام كل مشروب آخره (jamhara)؛ ختمت القرآن بلغت آخره وخاتمة الشيء آخره وخاتم الأنبياء (sihah)؛ يعتبر منه بلوغ الآخر وختمت القرآن أي انتهيت إلى آخره وخاتم النبيين لأنه ختم النبوة (mufradat)
- **B002** mühürleme, izi ve aracı — miskle mühürlenmiş olan veya üzerine miskten mühür konan şey · bir şeyi mühürleme veya üzerinde oluşan mühür izi · mühürlenmiş · mühür basma aracı; ayrıca parmağa takılan yüzük · mühür veya yüzük · belgeyi mühürlemekte kullanılan kil veya benzeri madde · yüzük takmak · üzerinde mühürlü bir kil parçası bulunmak
  الختم وهو الطبع على الشيء والخاتم مشتق منه لأن به يختم (maqayis)؛ ختم يختم ختما أي طبع والخاتم ما يوضع على الطينة والختام الطين الذي يختم به (ayn)؛ الخاتم معروف وختام كل شيء ما ختمته به (jamhara)؛ ختمت الشيء فهو مختوم والختام الطين الذي يختم به وتختمت إذا لبسته (sihah)؛ الختم والطبع مصدر وتأثير الشيء كنقش الخاتم والطابع والأثر الحاصل عن النقش (mufradat)
- **B003** mühürleyerek engelleme [kalıp] — kalpleri mühürleyip kavrayışa kapatmak · ağızlarını mühürleyip konuşmalarını engellemek
  يتجوز بذلك تارة في الاستيثاق من الشيء والمنع منه اعتبارا بما يحصل من المنع بالختم على الكتب والأبواب نحو ختم الله على قلوبهم؛ اليوم نختم على أفواههم أي نمنعهم من الكلام
- **B004** ekini sürümden sonra ilk kez sulama [kalıp] — ekini sürümden sonra ilk kez sulamak
  ختمت زرعي إذا سقيته أول سقية فهو الختم والختام اسم لأنه إذا سقي فقد ختم بالرجاء؛ وختموا على زرعهم ختما أي سقوه وهو كراب بعد
- **B005** görmezden gelip susma [kalıp] — bir şeyi görmezden gelip onun hakkında susmak
  تختم الرجل عن الشيء إذا تغافل عنه وسكت
- **B006** kıllarında belli belirsiz beyazlık bulunan at [kalıp] — kıllarında parıltı gibi belli belirsiz beyazlık bulunan at
  فرس مختم إذا كان في أشاعره بياض خفي كاللمع دون التخديم
- **B007** vuruşta kullanılan pürüzsüzleştirilmiş ceviz tanesi — vuruşta kullanılmak üzere pürüzsüzleştirilmiş ceviz tanesi
  المختم الجوزة التي تدلك لتملاس فينقد بها تسمى التير بالفارسية

## ق ل ب (root_001248): 42:24 قَلْبِكَ

- **B001** yürek ve iç merkez — yürek; akıl, kavrayış, ruh, bilgi, cesaret ve duygusal incelik merkezi
  القلب قلب الإنسان وغيره (maqayis;jamhara)؛ القلب مضغة من الفؤاد معلقة بالنياط (ayn;tahdhib)؛ القلب الفؤاد وقد يعبر به عن العقل (sihah)؛ يعبر بالقلب عن الروح والعلم والشجاعة (mufradat)
- **B002** öz ve katışıksız seçkin kısım — bir şeyin özü, en seçkin ve katışıksız kısmı · saf ve katışıksız Arap; soyu karışmamış kişi · Kur'an'ın merkezi sayılan bölüm; kaynakta Yasin ile açıklanan adlandırma
  خالص كل شيء وأشرفه قلبه (maqayis)؛ جئتك بهذا الأمر قلبا أي محضا لا يشوبه شيء (ayn;tahdhib)؛ عربي قلب أي خالص (jamhara;sihah;tahdhib)؛ قلب القرآن ياسين (ayn;tahdhib)
- **B003** hurma ağacının yumuşak iç sürgünü — hurma ağacının beyaz ve yumuşak iç sürgünü · ağaçların veya taze bitkilerin yumuşak iç kısımları
  قلب النخلة شحمتها (ayn)؛ قلوب الشجر ما رخص من عروقه وأجوافه (ayn;tahdhib)؛ قلب النخلة جمارها (tahdhib)؛ قلبت النخلة نزعت قلبها (maqayis;jamhara;sihah)
- **B004** çevirmek ve yönünü değiştirmek — bir şeyi çevirdi, ters yüz etti veya yönünü değiştirdi · birini yöneldiği taraftan çevirdi veya saptırdı · işleri yönetmek için düşünüp evirip çevirmek · gönülleri ve bakışları bir görüşten başka görüşe çevirmek · tehdit veya öfke anında gözünü ya da göz bebeğini çevirmek · ekmeğin diğer yüzünün çevrilme zamanı geldi · toprağı çevirmeye yarayan demir tarım aleti · anasının veya aslının renginden farklı renkte olan · satın almadan önce kusurlarını görmek için kişiyi inceleyip çevirmek
  قلبت الثوب قلبا (maqayis)؛ قلبت الشيء كببته وقلبته بيدي تقليبا (maqayis;jamhara;sihah)؛ القلب تحويلك الشيء عن وجهه (ayn;tahdhib)؛ قلب الشيء تصريفه وصرفه عن وجه إلى وجه (mufradat)؛ تقليب الأمور تدبيرها والنظر فيها (mufradat)
- **B005** dönüş ve akıbet — dönüp ayrılma veya geri dönüş · varış yeri, dönüş yeri, sonuç veya akıbet · öğretmen çocukları evlerine geri gönderdi
  المنقلب مصيرك إلى الآخرة (ayn;tahdhib)؛ المنقلب يكون مكانا ويكون مصدرا (sihah)؛ الانقلاب الانصراف (mufradat)
- **B006** pişmanlıkla avuç çevirmek [kalıp] — pişmanlıkla avuçlarını çevirdi veya ellerini çırpıp durdu
  تقليب اليد عبارة عن الندم؛ فأصبح يقلب كفيه
- **B007** kaplanmamış kuyu — içi henüz örülmemiş kuyu; bazı aktarımda genel kuyu adı
  القليب البئر قبل أن تطوى (maqayis;ayn;sihah;tahdhib;mufradat)؛ القليب الركي مذكر (jamhara)؛ القليب اسم من أسماء الركي مطوية أو غير مطوية (tahdhib)
- **B008** tek parça bilezik veya halka süs — bilezik ya da tek parça halka biçimli süs eşyası
  القلب من الأسورة ما كان قلبا واحدا (maqayis;sihah)؛ القلب من الأسورة ما كان قلدا واحدا (ayn;tahdhib)؛ القلب السوار (jamhara)؛ القلب المقلوب من الأسورة (mufradat)
- **B009** takıya benzetilen beyaz yılan — halka biçimli süse benzetilerek adlandırılan beyaz yılan
  شبه الحية بالقلب من الحلى فسمى قلبا (maqayis)؛ القلب الحية البيضاء شبهت بالقلب (ayn)؛ القلب أيضا حية تشبه به (sihah)
- **B010** Akrep'in Yüreği yıldızı [kalıp] — Akrep'in Yüreği diye bilinen parlak yıldız veya ay konağı
  القلب نجم يقولون إنه قلب العقرب (maqayis)؛ القلب نجم من منازل القمر (jamhara)؛ قلب العقرب منزل من منازل القمر وهو كوكب نير (sihah)
- **B011** yürekle ilişkili hastalık ve hastalık yokluğu kalıbı — deveyi veya yüreği tutan hastalık · onda hastalık, kusur ya da gizli zarar yok
  القلاب داء يصيب البعير فيشتكى قلبه (maqayis)؛ ما به قلبة أي لا داء ولا غائلة (ayn;tahdhib)؛ القلاب داء يأخذ البعير (sihah)؛ ما به قلبة علة يقلب لأجلها (mufradat)
- **B012** dudak dönüklüğü — dudakta dönüklük; dudağı dönük kişi veya dönük dudak
  القلب انقلاب الشفة وهي قلباء وصاحبها أقلب (maqayis)؛ الأقلب من في شفتيه انقلاب وشفة قلباء (ayn)؛ القلب بالتحريك انقلاب الشفة (sihah)؛ القلب انقلاب في الشفة (tahdhib)
- **B013** Yemen kullanımında kurt adı — Yemen'e nispet edilen dilde kurt adı
  القليب والقلوب فيقال إنه الذئب (maqayis)؛ القلوب الذئب يمانية (ayn)؛ القليب الذئب لغة يمانية (jamhara)؛ القليب وكذلك القلوب (sihah)؛ القليب والقلوب الذئب بلغة أهل اليمن (tahdhib)
- **B014** biçim verme kabı — içine dökülerek veya yerleştirilerek bir şeye biçim verilen kap ya da araç
  القالب دخيل (ayn;tahdhib)؛ القالب الذي يصب فيه الشيء من صفر أو غيره (jamhara)؛ القالب قالب الخف وغيره (sihah)
- **B015** kızarmış ham hurma — kızarmış ham hurma · ham hurma kırmızı renge döndü
  القالب بالكسر البسر الأحمر (sihah)؛ القالب البسر الأحمر يقال منه قلبت البسرة إذا احمرت (tahdhib)
- **B016** yüreğinden vurmak — birini yüreğinden vurdu veya yüreğine isabet ettirdi
  قلبته أي أصبت قلبه (sihah)؛ قلبت فلانا إذا أصبت قلبه فهو مقلوب (tahdhib)

## م ح و (root_001404): 42:24 وَيَمْحُ

- **B001** izini silerek ortadan kaldırma — izin silinip ortadan kaldırılması · izi silinip kaybolmak · silinmek, izi kaybolmak · izi silinip kaybolmak · silgi bezi veya iz giderme aracı · Allah'ın onun aracılığıyla inançsızlığı ve izini ortadan kaldırmasına dayanan Peygamber adlarından biri
  أصل صحيح يدل على الذهاب بالشيء (maqayis)؛ المحو لكل شيء يذهب أثره (ayn;tahdhib)؛ محوت الكتاب أمحوه محوا (maqayis)؛ محوت الشيء أمحوه محوا إذا طمسته (jamhara)؛ محا لوحه يمحوه محوا (sihah)؛ المحو إزالة الأثر (mufradat)؛ الممحاة خرقة يزال بها المنى ونحوه (sihah)؛ المحي من أسماء النبي محا الله به الكفر وأثره (tahdhib)
- **B002** bulutları dağıtan kuzey rüzgârı — bulutları veya izleri dağıttığı düşünülen kuzey rüzgârı
  تسمى الشمال محوة لأنها تمحو السحاب (maqayis)؛ سميت الشمال محوة لأنها تمحو السحاب وقال قوم بل تمحو الآثار (jamhara)؛ محوة ريح الشمال لأنها تذهب بالسحاب (sihah)؛ من أسماء الشمال محوة لأنها تمحو السحاب وتقشعها (tahdhib)؛ قيل للشمال محوة لأنها تمحو السحاب والأثر (mufradat)
- **B003** baştan başa yağmur suyuyla kaplanmış arazi [kalıp] — baştan başa yağmur suyuyla kaplanmış arazi
  تركت الأرض محوة واحدة إذا طبقها المطر (sihah)؛ أصبحت الأرض محوة واحدة إذا تغطى وجهها بالماء (tahdhib)؛ تركب السماء الأرض محوة واحدة إذا طبقها المطر (tahdhib)

## ب ط ل (root_000127): 42:24 ٱلْبَٰطِلَ

- **B001** doğru ve gerçek temelden yoksun olup geçerliliğini koruyamama — şey boşa çıktı ve geçerliliğini yitirdi · doğrunun karşıtı olan, asılsız ve geçersiz şey · asılsız ve geçersiz şey · asılsızlıklar ve geçersiz şeyler · geçersiz ve asılsız şeyler · tek bir asılsızlık veya geçersiz şey · eylemleri gerçek temelden yoksun sayılan kötülük ayartıcısı
  بطل الشيء يبطل بطلا وبطولا (maqayis;sihah); الباطل نقيض الحق (ayn;mufradat); لا حقيقة لأفعاله (maqayis); ما لا ثبات له عند الفحص عنه (mufradat); بطل الشيء بطلا فهو باطل (tahdhib)
- **B002** bir şeyi geçersiz kılıp bozma veya ortadan kaldırma — bir şeyi geçersiz kılmak, bozup ortadan kaldırmak · geçersiz kılma, bozma ve ortadan kaldırma
  أبطلته جعلته باطلا (ayn); أبطله غيره (sihah;mufradat); أبطلت الشيء جعلته باطلا (tahdhib); الإبطال يقال في إفساد الشيء وإزالته (mufradat)
- **B003** gerçek dışı söz veya iddia ileri sürme ya da doğruyu geçersizleştirmeye çalışma — yalan söyleyip gerçek dışı iddiada bulunmak · doğruyu geçersizleştirmeye çalışanlar
  أبطلت جئت بكذب وادعيت غير الحق (ayn); أبطل فلان جاء بكذب وادعى باطلا (tahdhib); يقول شيئا لا حقيقة له (mufradat); المبطلون أي الذين يبطلون الحق (mufradat)
- **B004** tehlike ve ölüm karşısında geri durmayan yiğitlik — tehlikeye atılmaktan çekinmeyen yiğit kişi · adam yiğitleşti · yiğitlik · yiğitlik ve yiğit olma durumu · yiğit kadın · Kardeşin savaşa zorla girdi, yiğit olduğu için değil.
  البطل الشجاع (maqayis;sihah); البطل الشجاع الذي يبطل جراحته ولا يكترث لها (ayn); بطل بين البطولة والبطالة (maqayis;tahdhib); صار شجاعا (sihah); الشجاع المتعرض للموت بطل (mufradat); مكره أخوك لا بطل (maqayis)
- **B005** işten veya yararlı uğraştan uzak kalma — işten veya yararlı uğraştan uzak, aylak kimse · işsizlik ve yararlı uğraştan uzak kalma · eğlence ve bilgisizliğin peşine düşerek aylaklaşma · beni işimden alıkoydu · ücretli çalışan işsiz kaldı
  رجل بطال بين البطالة (maqayis); التبطل فعل البطالة وهو اتباع اللهو والجهالة (ayn;tahdhib); بطلني فلان منعني عملي (ayn); بطل الأجير بطالة أي تعطل (sihah;tahdhib); للمستقل عما يعود بنفع دنيوي أو أخروي بطال (mufradat)
- **B006** öldürülenin kanının heder kalması ve öcünün alınmaması [kalıp] — kanı yerde kaldı; ne öcü alındı ne kan bedeli ödendi · öldürüldü, fakat kanının öcü alınmadı ve bedeli ödenmedi · onun yanında dökülen kanların öcü alınmaz
  ذهب دمه بطلا أي هدرا (maqayis;sihah); الدماء تبطل عنده فلا يدرك عنده ثأر (tahdhib); بطل دمه إذا قتل ولم يحصل له ثأر ولا دية (mufradat)
- **B007** belirli kullanımdaki büyücüler topluluğu — belirli kullanımdaki büyücüler
  البطلة السحرة؛ ولا تستطيعه البطلة (tahdhib)

## ص د ر (root_000849): 42:24 ٱلصُّدُورِ

- **B001** göğüs bölgesi — göğüs · göğüsler · göğsün üstte çıkıntılı kesimi · göğsü örten kısa giysi · devenin göğsündeki damga · yükü sabitleyen göğüs bağı · göğsünden rahatsız olan kimse · birinin göğsüne bir şeyle vurmak · göğsü ağrımak · güçlü göğüslü aslan
  الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)
- **B002** ön, üst ya da başlangıç bölümü — ön, üst ya da başlangıç bölümü · mızrağın üst bölümü · işin başlangıcı · toplantının ön kısmı; kitabın veya sözün başlangıcı · okun ortasından ucuna uzanan ön bölümü · ön gövdesi kalın ok · göğsüyle öne çıkıp yarışı geçmek · kitaba giriş bölümü koymak · toplantının başköşesine oturmak
  الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)
- **B003** geldiği yerden ayrılıp dönme — bir yerden ya da durumdan ayrılış · su başından, geldikten sonra ayrılmak · geri döndürmek · su başından dönüşü sağlayan yol
  صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)
- **B004** eylem türetme temeli; çıkış yeri veya zamanı — eylemlerin türediği temel sözcük biçimi · çıkış yeri ya da zamanı
  المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)
- **B005** para ödeme ve güvence yükümlülüğü koyma — birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak · kendisine para ödeme ve güvence yükümlülüğü konmak
  صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)
- **B006** bir şeyin bölümü ya da kümesi — bir şeyin bölümü ya da kümesi
  الصدر الطائفة من الشيء (sihah)

## ت و ب (root_000189): 42:25 ٱلتَّوْبَةَ

- **B001** yanlistan Tanri'ya donus — yanlisindan donup Tanri'ya yoneldi · yanlistan donme, pismanlikla birakma · yanlistan donme eylemi · Tanri'ya tam bir donus · Tanri'ya donen kisi · Rabbine sikca donen kul · yaraticiniza donun
  كلمة واحدة تدل على الرجوع (maqayis)؛ التوب مصدر تاب يتوب توبا (jamhara)؛ التوبة الرجوع من الذنب (sihah)؛ تاب عاد إلى الله ورجع وأناب (tahdhib)؛ التوب ترك الذنب على أجمل الوجوه (mufradat)
- **B002** Tanri'nin donusu kabul etmesi — Tanri onun donusunu kabul etti ve bagisladi · kullarin donusunu cokca kabul eden Tanri · Tanri kulunun donusunu kabul edendir
  وقد تاب الله عليه وفقه لها (sihah)؛ تاب الله عليه أي عاد عليه بالمغفرة (tahdhib)؛ تاب الله عليه أي قبل توبته (mufradat)؛ التواب من صفات الله هو الذي يتوب على عباده (tahdhib)؛ يقال ذلك لله تعالى لكثرة قبوله توبة العباد (mufradat)
- **B003** donuse cagirma — ondan yanlisindan donmesini istedi veya bunu teklif etti
  استتابه سأله أن يتوب (sihah)؛ استتبت فلانا أي عرضت عليه التوبة مما اقترف (tahdhib)
- **B004** hafifletmeye dondurme — sizi hafifletmeye dondurdu veya onceki yasagi serbest kildi
  فتاب عليكم أي رجع بكم إلى التخفيف (tahdhib)؛ أي أباح لكم ما كان حظر عليكم (tahdhib)

## ECHO ت ب ب (root_000172): for 42:25 ٱلتَّوْبَةَ: withheld observed target; not identity

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع

## ع ف و (root_001032): 42:25 وَيَعْفُوا۟, 42:30 وَيَعْفُوا۟, 42:34 وَيَعْفُ, 42:40 عَفَا

- **B001** hak edilmiş cezadan vazgeçip suçu silme — cezadan vazgeçip suçu silme · suçu yüzünden cezalandırmamak · Tanrı'nın kulunu cezalandırmayıp suçunu silmesi
  عفو الله تعالى عن خلقه وذلك تركه إياهم فلا يعاقبهم (maqayis)؛ العفو تركك إنسانا استوجب عقوبة (ayn)؛ عفوت عن ذنبه إذا تركته ولم تعاقبه (sihah)؛ محو الله ذنوب عبده عنه (tahdhib)؛ عفوت عنه قصدت إزالة ذنبه (mufradat)
- **B002** kötülüğü uzaklaştırıp esenlik sağlama — kötülüklerden korunma ve esenlik · Tanrı'nın kişiyi kötülükten koruyup esen kılması · Tanrı'nın kişiyi başkalarının zararından, başkalarını da onun zararından koruması
  العافية دفاع الله تعالى عن العبد (maqayis;ayn)؛ عافاه الله من سقم أو بلية (tahdhib)؛ عافاه الله وأعفاه بمعنى والاسم العافية (sihah)؛ أسألك العفو والعافية أي ترك العقوبة والسلامة (mufradat)
- **B003** zahmetsiz seçkin artığı verme veya alacaktan vazgeçme — kolay elde edilen artan ve seçkin mal · giderden artan veya zahmetsizce gelen mal · istenmeden ve yük oluşturmadan mal vermek · kendisine borçlu olunan hakkı karşılıksız bırakmak · yüklenen bir işten bağışık tutulmayı isteme
  العفو أحل المال وأطيبه (ayn;tahdhib)؛ عفو المال ما يفضل عن النفقة (sihah)؛ العفو الفضل الذي يجيء بغير كلفة (tahdhib)؛ ما يسهل قصده وتناوله (mufradat)؛ أعطيته المال عفوا أي عن غير مسألة (maqayis;tahdhib)؛ عفوت له عما لي عليه إذا تركته له (tahdhib)
- **B004** birine yönelip iyilik veya geçimlik arama — iyilik ve fazlalık isteyenler · birinden iyilik ve fazlalık istemek · yiyecek arayan insanlar, hayvanlar ve kuşlar
  العفاة طلاب المعروف وهم المعتفون (maqayis;ayn)؛ اعتفيت فلانا طلبت معروفه (maqayis;ayn)؛ العافية كل طالب رزق (sihah;tahdhib;mufradat)؛ العفو القصد لتناول الشيء (mufradat)
- **B005** kullanım izi taşımayan yer veya su [kalıp] — ayak basılmamış ve sahiplenilmemiş toprak · uğranıp bulandırılmamış veya çekişmeden alınabilen su · daha önce kimsenin dokunmadığı yemek
  العفو المكان الذي لم يوطأ (maqayis)؛ أرض عفو ليس فيها أثر (maqayis)؛ العفو الأرض الغفل التي لم توطأ (sihah)؛ عفو البلاد ما لا أثر لأحد فيها بملك (tahdhib)؛ عفا الماء أي لم يطأه شيء يكدره (maqayis)
- **B006** aşınıp silinerek iz bırakmama — toprak, harap oluş ve izlerin kaybolması · rüzgârın yapının izlerini silmesi · izi silinsin diye edilen kötü dilek
  العفاء التراب والدروس (ayn;tahdhib)؛ العفاء الدروس والهلاك (sihah)؛ عفت الريح المنزل درسته (sihah)؛ عفت الرياح الآثار إذا درستها ومحتها (tahdhib)؛ عفت الدار كأنها قصدت البلى (mufradat)
- **B007** büyüyüp çoğalma veya bir ölçüde başkasını aşma — saçın bırakıldıkça uzayıp çoğalması · sakalı kesmeyip gürleşmeye bırakma · gür ve sık tüy ya da telek · bitkinin veya ağacın büyüyüp çoğalması ve yeri örtmesi · bilgi veya vermede birini aşmak · devenin sırtını binmeden dinlendirip etlenmesini ve yarasının iyileşmesini sağlamak
  عفا الشعر وغيره إذا كثر (sihah;tahdhib)؛ حتى عفوا أي نموا وكثروا (maqayis;sihah;tahdhib)؛ العفاء ما كثر من الريش والوبر (ayn;sihah;tahdhib;mufradat)؛ عفا النبت والشجر قصد تناول الزيادة (mufradat)؛ عفا فلان على فلان في العلم إذا زاد عليه (tahdhib)
- **B008** biçime bağlı adlandırmalar — genç eşek yavrusu, sıpa · dişi eşek yavrusu veya genç eşek yavruları topluluğu · devenin sırtını binmeden dinlendirip etlenmesini ve yarasının iyileşmesini sağlamak
  العفو ولد الحمار والأنثى عفوة والجمع عفاء (maqayis;ayn)؛ العفو والعفا الجحش والأنثى عفوة (sihah)؛ الأعفاء أولاد الحمير (tahdhib)
- **B009** seçkin yiyecek payı veya tencereye geri konan et suyu — yemekten veya et suyundan ayrılıp değer verilen kişiye sunulan pay · yemeğin veya içeceğin en seçkin bölümü · ödünç tencere geri verilirken içinde bırakılan veya geri konan et suyu
  العفاوة شيء يرفع من الطعام (maqayis)؛ عفوة الطعام والشراب خياره (sihah;tahdhib)؛ العافي ما يرده مستعير القدر من المرق (sihah;tahdhib;mufradat)؛ عافي القدر الذي يرده المستعير للقدر (maqayis)

## س و ء (root_000755): 42:25 ٱلسَّيِّـَٔاتِ, 42:40 سَيِّئَةٍ, 42:40 سَيِّئَةٌ, 42:48 سَيِّئَةٌۢ

- **B001** çirkinlik ve kötülük — çirkinlik, kötülük ve nitelikçe bozukluk · çirkin adam · çirkin kadın · kötü ve çirkin iş · kötü davranış veya günah · kötü davranış veya en kötü sonuç · ceza ateşi veya görünüşü kötü son · kötü veya ayıplanan adam · kötü iş · kötü söz · çirkin durum veya huy · utanç verici iş veya durum · kusurları ve hastalıkları
  من باب القبح (maqayis)؛ السوء نعت لكل شيء رديء وساء الشيء قبح (ayn)؛ السوءى نقيض الحسنى والسيئة أصلها سيوئة (sihah)؛ كل كلمة أو فعلة قبيحة فهي سوء (tahdhib)؛ عبر عن كل ما يقبح بالسوأى والسيئة الفعلة القبيحة (mufradat)
- **B002** birini üzme veya ona kötülük etme — insanı üzen kötülük veya istenmeyen sonuç · onu üzdü veya ona istemediği bir şey yaşattı · birine kötülük etti veya onu üzdü · ona kötü davrandı · üzüldü ve sıkıntı duydu · üzme veya kötülük etme · yenilgi, yıkım veya acı getiren kötü son · başlarına onları üzen bir şey geldi
  سؤت وجه فلان وأنا أسوءه مساءة وأسأت إليه في الصنع (ayn)؛ ساءه يسوءه سوءا ومساءة نقيض سره (sihah)؛ ساء يسوء فعل لازم ومجاوز واستاء فلان من السوء (tahdhib)؛ السوء كل ما يغم الإنسان وساءني كذا وأسأت إلى فلان (mufradat)
- **B003** bedensel kusur veya hastalık — bedensel kusur, bozukluk veya hastalık · beyaz lekeli deri hastalığı veya başka bir bedensel kusur olmadan
  السوء اسم جامع للآفات والداء ويكنى بالسوء عن البرص (ayn)؛ من غير برص (sihah)؛ السوء الاسم الجامع للآفات والداء والسوء كناية عن اسم البرص (tahdhib)؛ من غير آفة بها وفسر بالبرص (mufradat)
- **B004** örtülmesi gereken cinsel bölge — kadın veya erkeğin örtülmesi gereken cinsel bölgesi · örtülmesi gereken özel bölgeler
  السوأة فرج الرجل والمرأة (ayn)؛ السوأة العورة والفاحشة (sihah)؛ السوء فرج الرجل والمرأة والسوءة كل عمل وأمر شائن (tahdhib)؛ كني عن الفرج بالسوأة (mufradat)
- **B005** yaptığını ayıplayıp kötüleme — ayıplama ve kötü yaptığını söyleme · yaptığı işi yüzüne karşı ayıplayıp kötüledi
  سوأت عليه ما صنع تسوئة وتسويئا إذا عبته عليه وقلت له أسأت (sihah)؛ ما صنع تسوئة وتسويئا إذا عبت ما صنع (tahdhib)
- **B006** ne kötü! — ne kötü; pek kötü · yaptıkları ne kötü · ne kötü bir örnek
  فساء هاهنا تجري مجرى بئس (mufradat)

## ف ع ل (root_001167): 42:25 تَفْعَلُونَ

- **B001** bir şeyi yapıp etkileme — bir şeyi yapmak, ortaya çıkarmak veya üzerinde etki bırakmak · yapma işi, eylemin ad eylem biçimi · gerçekleşmiş işin veya eylemin adı · tek bir yapma olayı veya iyi ya da kötü iş · işlerin çoğulu · eylem adı olarak kullanılan biçim · bir etkinin altında değişmek veya ona uymak
  أصل صحيح يدل على إحداث شيء من عمل وغيره (maqayis)؛ فعل يفعل فعلا وفعلا فالفِعل المصدر والفِعل الاسم (ayn)؛ الفِعل بالفتح مصدر فعل يفعل والفِعل بالكسر الاسم (sihah)؛ فعلت الشيء فانفعل كسرته فانكسر (sihah)؛ فعل يفعل فعلا وفعلا فالمصدر مفتوح والاسم مكسور (tahdhib)
- **B002** iyi iş ve kişisel tutum — eli açıklık ve güzel davranış; ayrıca tek kişinin iyi ya da kötü işi
  الفَعال بفتح الفاء الكرم وما يفعل من حسن (maqayis)؛ الفَعال اسم للفعل الحسن مثل الجود والكرم ونحوه (ayn)؛ الفَعال بالفتح الكرم (sihah)؛ الفَعال فعل الواحد خاصة في الخير والشر (tahdhib)؛ الفَعال يكون في المدح والذم (tahdhib)
- **B003** el işçileri — işçiler, özellikle çamur ve kazı işlerinde çalışanlar · marangoz
  الفَعلة العملة وهم قوم يستعملون الطين والحفر وما يشبه ذلك من العمل (ayn)؛ الفَعلة قوم يعملون عمل الطين والحفر وما أشبه ذلك من العمل (tahdhib)؛ النجار يقال له فاعل (tahdhib)
- **B004** uydurup düzme — yalanı, düzme sözü veya anlatıyı uydurmak · sahibince ortaya atılmış veya önceki örneği olmadan yapılmış şey
  افتعل كذبا وزورا أي اختلق (sihah)؛ شعر مفتعل إذا ابتدعه قائله (tahdhib)؛ افتعل فلان حديثا إذا اخترقه (tahdhib)؛ يقال لكل شيء يسوى على غير مثال تقدمه مفتعل (tahdhib)
- **B005** karşılıklı eylem — eylem iki kişi arasında gerçekleştiğinde kullanılan ad
  الفِعال بكسر الفاء إذا كان الفعل بين الاثنين (tahdhib)؛ فإذا كان من فاعلين فهو فِعال (tahdhib)
- **B006** balta ya da keser sapı — balta sapı veya balta gözüne takılan ağaç parça; keser sapı
  يقولون الفَعال خشبة الفأس (maqayis)؛ الفَعال العود الذي يجعل في خرت الفأس يعمل به (tahdhib)؛ في نصاب القدوم سماه فَعالا (tahdhib)
- **B007** dil bilgisi tümleçleri — dil bilgisinde eyleme bağlanan öge türleri · eylemin yöneldiği veya etkilediği şey; nesne · eylemin yapılma amacı veya gerekçesi · yer, zaman veya durum bildirerek eyleme bağlanan öge · eylemin üzerinde gerçekleştiği alanı bildiren öge · doğrudan eylem adı; geçişli veya geçişsiz eylemle kullanılan tür
  المفعولات على وجوه في باب النحو (tahdhib)؛ فمفعول به (tahdhib)؛ ومفعول له (tahdhib)؛ ومفعول فيه (tahdhib)؛ ومفعول عليه (tahdhib)؛ ومفعول بلا صلة وهو المصدر (tahdhib)

## ECHO ء ب و (root_000007): for 42:25 تَفْعَلُونَ: withheld observed target; not identity

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ك ف ر (root_001307): 42:26 وَٱلْكَٰفِرُونَ, 42:48 كَفُورٌ

- **B001** örtmek, kapatmak — bir şeyi örtmek ve kapatmak · zırhının üstüne bir giysi geçirmek · silahlarıyla örtünmek veya silah kuşanmak · rüzgârın savurduğu toprakla örtülmüş kül · güneşin yıldızları görünmez kılması
  الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)
- **B002** örten karanlık veya enginlik — karanlık gece, deniz, büyük ırmak, gün batımı veya bulut
  الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)
- **B003** dinî gerçeği reddetme — dinî gerçeği veya inancı reddetme · kalben bildiği gerçeği diliyle kabul etmeme · gerçeği bildiği hâlde inatla kabul etmemek · kalben reddederken diliyle inanmış görünmek · gerçeği hem kalple hem dille inkâr etmek
  الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)
- **B004** nimeti yadsıma — nimeti yadsımak ve şükrünü yerine getirmemek · nimeti yadsıma ve şükretmeme · nimetleri aşırı biçimde yadsıyan kimse · iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam
  كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)
- **B005** bağını reddedip uzaklaşmak — bir şeyle bağını reddedip ondan uzaklaşmak
  يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)
- **B006** inançsız saymak — birini inançsız saymak veya öyle adlandırmak
  أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)
- **B007** itaatsizliğe zorlamak — itaat eden birini itaatsizliğe zorlamak
  إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)
- **B008** tohumu örten çiftçi — tohumu toprakla örten çiftçi · tohumları toprakla örten çiftçiler
  يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)
- **B009** günah yükünü giderme — günahı veya bozulan yeminin yükünü gideren karşılık · bozulan yeminin gerektirdiği yükümlülüğü yerine getirme · günahları örtüp etkisini silme
  الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)
- **B010** çiçek veya meyve kılıfı — üzüm salkımının veya hurma çiçeğinin kılıfı · hurma çiçeğinin ya da meyvenin kılıfı · hurma ağacından çıkan kapalı çiçek kılıfları
  الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)
- **B011** koku maddesi, su kaynağı veya bitki — güzel kokulu karışımlarda kullanılan madde · cennetteki bir su kaynağı · çiçeği papatyaya benzeyen bir bitki
  الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)
- **B012** uzak arazi; köy, uzak yer halkı veya mezar — insanlardan uzak, pek uğranmayan arazi · köy veya mezar · köyler veya uzak yerlerin halkı
  الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)
- **B013** dağ geçidi; iri dağ veya alçak duvar — dağ geçitleri · dağ geçidi veya iri dağ · alçak duvar
  الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)
- **B014** eğilerek boyun eğme gösterisi — başını eğmek veya elini göğsüne koyup eğilmek
  التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)
- **B015** hükümdara taç giydirme veya taç — hükümdara taç giydirme veya tacın kendisi
  التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)

## خ ب ر (root_000387): 42:27 خَبِيرٌۢ

- **B001** bilgi edinme, bildirme ve deneyerek iç yüzü tanıma — bir olay veya durum hakkında edinilen ve aktarılan bilgi · bilgi vermek; bildirmek · bir konuyu sorup bilgi edinmek · sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma · sınayıp deneyerek bilgi sahibi olmuş kişi · bilgili; bir işin iç yüzüne hakim · dış görünüşün karşısındaki iç yüz ve gerçek nitelik
  الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)
- **B002** gevşek, alçak ve su tutan arazi veya su birikintisi — gevşek, yumuşak veya alçak olup su toplayan arazi · sıcak, ağaçlı ve suyu bol yer · akış yatağında oluşan geçilebilir su birikintisi
  الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)
- **B003** üründen pay karşılığı ortakçılık ve bunu yapan çiftçi — toprağı işleyen çiftçi · ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık
  الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)
- **B004** büyük su tulumu ve bolluğuyla ona benzetilen dişi deve — büyük ve geniş su tulumu · bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve
  الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)
- **B005** yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü — kesilip yenebilen yumuşak bitki · yün veya ince hayvan kılı · devenin ağzında oluşan veya ağzından çıkan köpük
  الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)
- **B006** ortak alınıp kesilen koyun veya bölüşülen et-balık payı — ortaklaşa alınıp kesilen ve eti bölüşülen koyun · et veya balıktan alınan pay
  الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)

## غ ي ث (root_001118): 42:28 ٱلْغَيْثَ

- **B001** gökten inen yağmur — gökten inen yağmur · yağmur toprağa ulaştı · Tanrı ülkeye yağmur yağdırdı · yağmura kavuştuk · yağmur almış toprak · yağmur almış toprak
  أصل صحيح وهو الحيا النازل من السماء (maqayis)؛ الغيث المطر (ayn;sihah)؛ الغيث وهو المطر (jamhara)؛ الغيث في المطر، والغيث المطر (mufradat)
- **B002** yağmurla yetişen ot — yağmurla yetişen ot veya bitki · yağmurla yetişen otlar
  الغيث الكلأ ينبت من المطر (ayn)؛ ربما سمي العشب غيثا (jamhara)؛ ربما سمى السحاب والنبات بذلك (sihah)
- **B003** yağmur adıyla anılan bulut — yağmur adıyla anılan bulut
  ربما سمى السحاب والنبات بذلك (sihah)
- **B004** sıkıntıyı gideren yardım — 
  الغياث ما أغاثك الله به، ويقول المبتلى أغثني أي فرج عني (ayn)؛ استغثته طلبت الغوث أو الغيث، فإنه يصح أن يكون من الغيث ويصح أن يكون من الغوث (mufradat)
- **B005** atın art arda koşu hamleleri — bir koşunun ardından yeniden koşan at · birbirini izleyen koşu hamleleri
  فرس ذو غيث إذا عدا عدوا بعد عدو؛ المترافد الذي بعضه في إثر بعض (jamhara)

## ECHO غ و ث (root_001111): for 42:28 ٱلْغَيْثَ: withheld observed target; not identity

- **B001** sıkıntı anında yardım ve destek — sıkıntı anında yardım ve destek · yardım etme ve destek olma · ona ihtiyaç anında yardım etti ve destek oldu · ondan yardım istedi · ona yardım etti · yardım ve destek
  الغوث من الإغاثة وهي الإعانة والنصرة عند الشدة (maqayis); غاثه يغوثه غوثا وأغاثه يغيثه إغاثة (jamhara); استغاثني فلان فأغثته والاسم الغياث (sihah); الغوث يقال في النصرة واستغثته طلبت الغوث فأغاثني من الغوث وغوثت من الغوث (mufradat)
- **B002** yardım istemek için seslenme — yardım istemek için seslendi · yardım çağrısı · yardım çağrısının sesi
  قال واغوثاه أي من يغيثني والغوث الاسم من ذلك (ayn); غوث الرجل قال واغوثاه والاسم الغوث والغواث وقال الفراء دعاءه وغواثه (sihah)
- **B003** kişi, kabile ve put adları — kişi ve kabile adı · kişi adı · kişi adı · tanınmış bir putun adı
  غوث قبيلة (maqayis); سموا غوثا ومغيثا وغياثا ويغوث اسم صنم معروف (jamhara); غوث قبيلة من اليمن (sihah)
- **B004** yağmur ve yardımla belirsizleşen yağmur isteme — 
  الغيث في المطر; استغثته طلبت الغوث أو الغيث; غاثني من الغيث; يغاثوا يصح فيه المعنيان (mufradat)

## ق ن ط (root_001261): 42:28 قَنَطُوا۟

- **B001** umudu kesmek — bir şeyden, iyilikten ya da Tanrı'nın esirgemesinden umudu kesmek · iyilikten umudu kesme; umutsuzluk · umudunu kesmiş, umutsuz · umudunu kesmiş kimse · umudu kesme, umutsuzluk · insanların Tanrı'nın bağışlayıcılığından umutlarını kesmelerine yol açmak
  تدل على اليأس من الشيء (maqayis)؛ القنوط الإياس (ayn)؛ القنوط اليأس (sihah)؛ القنوط الإياس من الخير (tahdhib)؛ يقنطون الناس من رحمة الله أي يؤيسونهم (tahdhib)؛ القنوط اليأس من الخير (mufradat)

## ن ش ر (root_001503): 42:28 وَيَنشُرُ

- **B001** açıp yayma, dallandırıp dağıtma — bir şeyi açmak, serip yaymak ve görünür hale getirmek · haberi duyurup yaymak · insanların yeryüzüne dağılıp kendi işlerine yönelmesi · sıçrayıp çevreye saçılan su damlacıkları · Tanrı dağılmış işlerini toparlasın · geniş, uzun ve yayvan tüyler · dağınık halde esen veya yağmur bulutlarını yayan rüzgarlar · yağmur getiren ya da bulutları yayan rüzgarlar; ayrıca rüzgarları yayan melekler yorumu
  أصل صحيح يدل على فتح شيء وتشعبه (maqayis)؛ نشرت الثوب والكتاب نشرا بسطته (ayn)؛ نشر المتاع وغيره بسطه وانتشر الخبر ذاع (sihah)؛ جاء الجيش نشرا أي متفرقين وضم الله نشرك ما انتشر من أمرك ونشر الماء ما تطاير منه (tahdhib)؛ نشر الثوب والصحيفة والسحاب والنعمة والحديث بسطها (mufradat)؛ اكتسى البازي ريشا نشرا أي منتشرا واسعا طويلا (maqayis;sihah;mufradat)
- **B002** ölüyü yeniden hayata döndürme ve yeniden dirilme — ölümden sonra yeniden hayat bulma · ölünün yeniden yaşaması · Tanrı'nın ölüyü yeniden hayata döndürmesi · ölü toprağı yağmurla canlandırmak
  نشر الله الموتى فنشروا وأنشر الله الموتى أيضا (maqayis)؛ النشور الحياة بعد الموت ينشرهم الله إنشارا (ayn)؛ نشر الميت نشورا أي عاش بعد الموت وأنشرهم الله أي أحياهم (sihah)؛ أنشر الله الميت ونشره فنشر الميت لا غير ونشرهم الله أي بعثهم (tahdhib)؛ نشر الميت نشورا وأنشر الله الميت فنشر وفأنشرنا به بلدة ميتا (mufradat)
- **B003** hoş koku; uykudan sonraki ağız ve beden kokusu — hoş ve duyulur koku · bir kadının uykudan sonra ağzından, burnundan ve beden kıvrımlarından gelen koku
  النشر الريح الطيبة (maqayis;ayn;tahdhib)؛ النشر الرائحة الطيبة (sihah)؛ نشره أمامه يعني ريح المسك (ayn;tahdhib)؛ النشر ريح فم المرأة وأنفها وأعطافها بعد النوم (tahdhib)
- **B004** kuruduktan veya kaybolduktan sonra yeniden belirme — toprağın bahar veya yağmurla yeniden bitki vermesi · yağmurla yeniden yeşeren ve hayvanlara zarar verebilen kuru ot · uyuzun geri gelmesi veya iyileşen yerde tüyün yeniden çıkması
  نشرت الأرض أصابها الربيع فأنبتت والنشر الكلأ ييبس ثم يصيبه المطر (maqayis)؛ نشرت الأرض تنشر نشورا إذا أصابها الربيع فأنبتت (ayn)؛ النشر الكلأ إذا يبس ثم أصابه مطر فاخضر (sihah)؛ النشر أن يخرج النبت يبطئ عنه المطر فييبس ثم يصيبه مطر بعد اليبس (tahdhib)؛ النشر الكلأ اليابس إذا أصابه مطر فينشر أي يحيا (mufradat)؛ نشر الجرب ينشر نشرا ونشورا إذا حيي بعد ذهابه ونبات الوبر على الجرب بعد ما يبرأ (tahdhib)
- **B005** ahşabı testereyle kesme ve çıkan talaş — ahşabı testereyle kesmek · testereyle keserken dökülen ahşap talaşı
  نشرت الخشبة بالمنشار نشرا (maqayis)؛ نشرت الخشبة أنشرها إذا قطعتها بالمنشار والنشارة ما سقط منه (sihah)؛ نشرت الخشبة بالمنشار أنشرها نشرا (tahdhib)
- **B006** koyunların gece otlamaya dağılması veya dağılmış sürü — koyunların gece otlamak için dağılması veya bu haldeki sürü
  النشر أن تنتشر الغنم بالليل فترعى (maqayis;sihah;tahdhib)؛ النشر الغنم المنتشر (mufradat)
- **B007** ön kol damarları; hayvanda kiriş bozukluğu; cinsel sertleşme — ön kolun iç yüzündeki damarlar · hayvanda yorgunluktan kirişin şişmesi veya yerinden oynaması · erkeğin cinsel organının sertleşmesi
  النواشر عروق باطن الذراع (maqayis;ayn;sihah;tahdhib;mufradat)؛ الانتشار انتفاخ عصب الدابة من تعب (maqayis;sihah;tahdhib)؛ انتشر الرجل أنعظ (sihah)؛ انتشر ذكره إذا قام (tahdhib)
- **B008** sözlü koruma ve tedaviyle sıkıntıyı giderme — akıl sağlığı bozulmuş veya büyüden etkilendiği düşünülen kişiden sıkıntıyı gideren sözlü tedavi · koruyucu sözlerle tedavi uygulama · etkilenmiş kişiyi bu uygulamayla tedavi edip sıkıntısını gidermek
  النشرة رقية علاج للمجنون ينشر بها عنه تنشيرا (ayn)؛ التنشير من النشرة وهي كالتعويذ والرقية ونشره أي رقاه (sihah)؛ النشرة علاج رقية يعالج بها المجنون ينشر بها عنه تنشيرا (tahdhib)
- **B009** çocuk yazısı; açılmış sayfalar; mühürsüz resmi yazı — çocukların deftere yazdığı yazılar · hükümdarın mühürsüz yazılı buyruğu · açılıp serilmiş sayfalar
  التناشير كتابة الغلمان في الكتاب (ayn;tahdhib)؛ صحف منشرة شدد للكثرة (sihah)؛ المنشور من كتب السلطان ما كان غير مختوم (tahdhib)؛ نشر الصحيفة بسطها وإذا الصحف نشرت (mufradat)
- **B010** cömertlik ve onurluluk — cömert ve onurlu kadın · cömertlik ve onurluluk
  امرأة منشورة ومشبورة إذا كانت سخية كريمة؛ نشرا بين يدي رحمته أي سخاء وكرامة (tahdhib)

## ء ي ي (root_000074): 42:29 ءَايَٰتِهِۦ, 42:32 ءَايَٰتِهِ, 42:33 لَءَايَٰتٍ, 42:35 ءَايَٰتِنَا

- **B001** bekleyerek oyalanma — durup oyalanmak · isin imkanini beklemek · kalinacak veya oyalanilacak yer
  تأيا يتأيا تأييا أي تمكث؛ تأييت الأمر انتظرت إمكانه؛ ليست هذه بدار تئية أي مقام (maqayis)؛ تأيا أي توقف وتمكث؛ منزل تئية أي منزل تلبث وتحبس (sihah)
- **B002** kisiyi bilerek hedefleme — onu belirtisiyle bilerek kastetmek
  تآييت وأصله تعمدت آيته وشخصه (maqayis)؛ تآييته وتأييته إذا قصدت آيته وتعمدته (sihah)
- **B003** gorunen belirti — gorunen isaret · belirlenmis isaret · kisinin sahsi · topluca cikmak · kitaptaki harf toplulugu parcasi · gunesin isigi · gunesin isigi
  الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ آية القرآن لأنها جماعة حروف؛ إياة الشمس ضوءها لأنه كالعلامة لها (maqayis)؛ الآية العلامة والآية من آيات الله والجميع الآي (ayn)؛ الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ الآية من كتاب الله جماعة حروف؛ أياة الشمس ضوؤها (sihah)
- **B004** hangi belirleyicisi — soru, sart veya ilgiyle belirleyen ad · hangi olursa veya herhangi bir
  لم يجىء إلا في قولهم أي في الاستفهام (jamhara)؛ أي مثقلة بمنزلة من وما؛ أيهم أخوك؛ أيما الأخوين؛ أيا ما تحب؛ أي لا تنون لأن أي مضاف (ayn)؛ أي اسم معرب يستفهم به ويجازى؛ وقد يكون بمنزلة الذي؛ وقد يكون نعتا للنكرة؛ وأي قد يتعجب بها (sihah)
- **B005** nesne zamiri dayanagi — nesne zamiri icin dayanak unsur
  إياك ضربت فتكون إيا عمادا للكاف؛ ولا تكون إيا مع كاف ولا هاء ولا ياء في موضع الرفع والجر؛ إياك وزيدا (ayn)
- **B006** zaman sorusu — ne zaman anlaminda zaman sorusu
  أيان بمنزلة متى؛ يختلف في نونها فيقال هي أصلية ويقال هي زائدة (ayn)
- **B007** nice cok — ne kadar cok anlaminda nicelik birimi · ne kadar cok anlaminda varyant
  كأين في معنى كم؛ أصل بنائها أي (ayn)؛ تدخل على أي الكاف فينقل إلى تكثير العدد بمعنى كم؛ كائن وكأين (sihah)
- **B008** ey seslenmesi — yakin muhataba seslenme birimi · yakin veya uzak muhataba seslenme birimi · uzatilmis seslenme bicimi
  في النداء أي فلان وقد يمد آي فلان (ayn)؛ أيا من حروف النداء ينادى بها القريب والبعيد؛ أي حرف ينادى به القريب (sihah)
- **B009** yani aciklayicisi — anlami aciklayan yani birimi
  أي تفسيرا للمعاني أي كذا وكذا (ayn)؛ أي كلمة تتقدم التفسير تقول أي كذا بمعنى تريد كذا (sihah)
- **B010** yemin oncesi evet — yemin oncesi evet veya bilakis sozu
  إي تدخل في اليمين كالصلة والافتتاح؛ إي وربي؛ المعنى نعم والله (ayn)؛ إى بالكسر كلمة تتقدم القسم معناها بلى؛ إى ربى وإى والله (sihah)

## خ ل ق (root_000434): 42:29 خَلْقُ, 42:49 يَخْلُقُ

- **B001** ölçüp sınırlarını belirleme — ölçüp sınırlarını belirlemek · ölçüp biçme
  أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)
- **B002** var etme ve ortaya çıkarma — yaratmak, var etmek · yaratan, var eden · yaratan, var eden; özellikle Tanrı için kullanılan ad · yaratılanlar, insanlar · yaratılmış varlık ya da varlıklar topluluğu
  الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)
- **B003** tam ve dengeli dış biçim — dış görünüş ve beden yapısı · beden yapısı tam ve dengeli · yapısı tamamlanmış ve ölçülü · biçimi belirmiş ve oluşumu tamamlanmış
  رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)
- **B004** huy ve iç karakter — huy, iç karakter · doğal huy ve yaradılıştan eğilim · iyi huyluluk ve iyi geçim · insanlarla huyuna göre geçinmek · bir huyu edinmeye veya öyle görünmeye çalışmak
  الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)
- **B005** bir şeye yaraşır ve uygun olma — yaraşır, uygun · bunu yapması ne kadar beklenir · iyiliğe veya o işe çok uygun
  فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)
- **B006** iyilikten düşen pay — pay, özellikle iyilikten düşen pay · iyilikten veya öte dünyadaki karşılıktan payı yok
  الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)
- **B007** uydurup yalan üretme — söz uydurmak ve çarpıtmak · zihninde yalan kurup ortaya atmak · yanlış kişiye bağlanmış, uydurma · uydurma öyküler ve asılsız anlatılar
  الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)
- **B008** engebesiz ve düz olma — yüzeyini düzeltmek ve pürüzsüzleştirmek · engebesiz, düz ve yoğun · düz ve engebesiz kaya · alnın veya gözler arasının düz bölümü · yayılıp düzleşmek · düzeltilmiş ve yüzeyi engebesiz
  الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)
- **B009** kullanımdan yıpranıp eskime — kullanımdan yıpranıp tüyünü yitirmek · eski ve yıpranmış giysi · her yanı yıpranmış veya parçalanmış giysi · birine eski ve yıpranmış bir giysi vermek · istemekten yüzünü eskitmek
  أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)
- **B010** sürülen hoş koku karışımı — sürülen hoş koku karışımı · hoş koku karışımı sürmek veya sürünmek
  الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)
- **B011** su tutan kaya oyuğu veya yeni kuyu — su tutan kaya oyuğu veya yeni kuyu · yeni kazılmış kuyular
  الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)
- **B012** kapalı üreme yolu — üreme yolu kapalı kadın
  امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)

## ب ث ث (root_000083): 42:29 بَثَّ

- **B001** dagitip yaymak — bir seyi dagitip yaymak veya aciga cikarmak · atlari saldiriya yaymak veya av kopeklerini ava salmak · yayilip dagilmak · cok ve daginik; yayilmis veya savrulmus · toplanmamis, etrafa sacilmis hurma · yiyecegi veya hurmayi alt ust edip birbirinin ustune atmak · yaratilmislari veya hayvanlari yeryuzune yayip cogaltmak
  تفريق الشيء وإظهاره؛ بثوا الخيل؛ بث الصياد كلابه؛ خلق الخلق وبثهم في الأرض؛ وزرابي مبثوثة؛ تمر بث؛ بثثت الطعام والتمر (maqayis)؛ بث الخيل؛ كل شيء فرقته؛ انبث الجراد؛ كالفراش المبثوث؛ تمر بث (jamhara)؛ فانبث أي انتشر؛ تمر بث؛ منثورا متفرقا؛ الغبار إذا هيجته (sihah)؛ تفريقك الأشياء؛ بثوا الخيل؛ بث الصياد كلابه؛ بثت البسط؛ مبثوثة كثيرة؛ غبارا منتشرا؛ وبث منهما رجالا كثيرا ونساء أي نشر وكثر (tahdhib)؛ التفريق وإثارة الشيء كبث الريح التراب؛ بثثته فانبث؛ وبث فيها؛ كالفراش المبثوث (mufradat)
- **B002** icindekini acip dile getirmek — haberi veya sozu yaymak, duyurmak · birine sirrini acmak ve onu haberdar etmek · insanin icinde tasidigi keder, gam veya sikinti · yoksullugunu ve duskunlugunu birine sikayet etmek · gizli bir kusur, sevgi veya isin durumunu yoklayip anlamaya calisma
  بثثت الحديث أي نشرته؛ البث من الحزن؛ يشتكى ويبث ويظهر؛ أبث فلان شقوره وفقوره؛ وأبثثتك مكتومي (maqayis)؛ بثثته سري وأبثثته؛ البث ما يجده الرجل في نفسه من كرب أو غم (jamhara)؛ بث الخبر وأبثه؛ نشره؛ أبثثتك سري؛ أظهرته لك؛ البث الحال والحزن؛ أظهرت لك بثي (sihah)؛ البث الحزن الذي تفضي به إلى صاحبك؛ أبثثت فلانا سري؛ أطلعته عليه؛ لا يولج الكف ليعلم البث (tahdhib)؛ بث النفس ما انطوت عليه من الغم والسر؛ غمي الذي أبثه عن كتمان (mufradat)
- **B003** arastirip aciga cikarmak [kalıp] — haberi yaymak veya tozu kaldirip savurmak · bir isi arastirip yoklamak veya aciga cikarmak
  بثبثت الخبر بثبثة نشرته؛ وكذلك الغبار إذا هيجته (sihah)؛ بثبثت الأمر إذا فتشت عنه وتخبرته؛ بثبثوه أي كشفوه؛ الأصل فيه بثثوه فأبدلوا (tahdhib)

## د ب ب (root_000457): 42:29 دَآبَّةٍ

- **B001** yerde hafif ya da yavaş ilerleme — yerde hafifçe veya yavaşça ilerlemek · hafif ya da yavaş yer hareketi · çocuğu emeklemeye yöneltmek · ağırlığından ancak yavaşça yürüyebilen deve
  حركة على الأرض أخف من المشي (maqayis)؛ دب يدب دبا ودبيبا (jamhara)؛ دب على الأرض يدب ودب الشيخ وناقة دبوب (sihah)؛ الدب والدبيب مشي خفيف في الحيوان والحشرات (mufradat)
- **B002** yerde hareket eden canlı — yerde hareket eden canlı · yerden çıkacak kıyamet alameti canlı
  كل ما مشى على الأرض فهو دابة (maqayis)؛ كل ماش على الأرض دابة ودبيب والدابة التي تركب ودابة الأرض (sihah)؛ يستعمل في كل حيوان والدابة جمع لكل شيء يدب (mufradat)
- **B003** duyulmadan içten içe yayılma [kalıp] — kanı içten içe yayılan yara
  طعنة دبوب إذا كانت تدب بالدم (maqayis)؛ يستعمل في الشراب والبلى ونحو ذلك مما لا تدرك حركته الحاسة (mufradat)
- **B004** laf taşıyan kimse — laf taşıyan kimse
  الديبوب النمام الذي يدب بين الناس بالنمائم
- **B005** izlenen yol ve alışılmış tutum — birinin yolunu ve davranışını izlemek · benim yolum ve yaradılışım · gizli bir yoldan ilerleyiş · yol
  ركب فلان دبة فلان وأخذ بدبته إذا فعل مثل فعله (maqayis)؛ الدبة الطريق ودعني ودبتي أي طريقتي وسجيتي ودببت دبة خفية (sihah)
- **B006** orada hiç kimse yok [kalıp] — evde hiç kimse yok
  ما بالدار دبي ودبي أي أحد يدب (maqayis)؛ ما بالدار دبي ودبى أي أحد (sihah)؛ وما بالدار دبي أي من يدب (mufradat)
- **B007** yaşam evrelerini kapsayan kalıplaşmış sözler [kalıp] — gençlikten değnekle yürüyen yaşlılığa kadar · yaşayanı ve ölmüşüyle herkesten daha yalancı
  من شب إلى دب أي من لدن أن شببت إلى أن دببت على العصا (jamhara)؛ أكذب من دب ودرج أي الأحياء والأموات ومن شب إلى دب (sihah)
- **B008** ayı — ayı · dişi ayı · ayıların bulunduğu arazi
  الدب هذه الدابة المعروفة عربية صحيحة (jamhara)؛ الدب من السباع والأنثى دبة وأرض مدبة ذات دببة (sihah)
- **B009** kabak — kabak
  الدباء القرع ويجوز أن يكون شاذا ومحتمل أن يكون سمي بذلك لملاسته كأنه يخف إذا دحرج
- **B010** yağ kabı — yağ kabı
  الدبة التي للدهن
- **B011** kum tepesi — kum tepesi
  الدبة أيضا الكثيب من الرمل
- **B012** akış veya geçiş yatağı [kalıp] — sel yatağı · karınca yolu
  مدب السيل ومدبه موضع جريه ومدب النمل ومدبه
- **B013** yüz tüyü [kalıp] — yüzdeki ince tüyler
  دبب الوجه زغبه
- **B014** bir tür ses — bir tür ses · atların köprü üzerindeki sesi
  الدبدبة ضرب من الصوت دبدبة الخيل على الجسور

## ECHO د ء ب (root_000456): for 42:29 دَآبَّةٍ: withheld observed target; not identity

- **B001** bir işi kararlılıkla ve sürekli sürdürme — bir şey üzerinde yılmadan ve sürekli çalışmak · yolculuğu kesintisiz sürdürme · durmaksızın ve yoğun çabayla yol alma · işini ya da devinimini sürekli sürdüren · sürekli birbirini izleyen gece ile gündüz
  ملازمة ودوام (maqayis)؛ دأب الرجل في عمله إذا جد (maqayis)؛ دأب فلان في عمله أي جد وتعب ودؤوبا فهو دائب (sihah)؛ الدؤوب المبالغة في السير ودأبت الناقة دؤوبا (tahdhib)؛ الدأب إدامة السير ودأب في السير والشمس والقمر دائبين (mufradat)؛ الدائبان الليل والنهار (maqayis;sihah)
- **B002** süregelen alışkanlık ve tutum — süregelen alışkanlık, tutum veya durum · senin alışkanlığın ve süregelen tutumun
  الدأب العادة والشأن (maqayis;sihah)؛ كدأب آل فرعون أي كشأن آل فرعون وكأمر آل فرعون (tahdhib)؛ دأبك وديدنك كله في العادة (tahdhib)؛ العادة المستمرة دائما على حالة (mufradat)
- **B003** bir başkasını yormak — bir başkasını uzun süre yürütüp ya da çalıştırıp yormak · bir başkasını sürekli yürütme veya çalıştırma yoluyla yorma
  أدأبته أنا إدآبا (maqayis)؛ وأدأبته أنا (sihah)؛ أدأب الرجل الدابة إدآبا إذا أتعبها (tahdhib)

## ص و ب (root_000889): 42:30 أَصَٰبَكُم, 42:30 مُّصِيبَةٍ, 42:39 أَصَابَهُمُ, 42:48 تُصِبْهُمْ

- **B001** yukarıdan inip yerleşen yağış — yağmur veya yağmurun yukarıdan inmesi · yağmur taşıyan bulut veya yağmur · yağmurun bir yere inmesi
  الصوب المطر؛ الصيب سحاب ذو صوب؛ صاب الغيث بمكان كذا (ayn)؛ الصوب نزول المطر؛ الصيب السحاب دون الصوب؛ صاب أي نزل (sihah)؛ الصيب في اللغة المطر؛ كل نازل من علو إلى استفال فقد صاب يصوب؛ الصوب المطر؛ الصيب سحاب ذو صوب (tahdhib)؛ جعل الصوب لنزول المطر؛ الصيب السحاب المختص بالصوب؛ قيل هو السحاب وقيل هو المطر (mufradat)؛ أصل صحيح يدل على نزول شيء واستقراره قراره؛ الصوب وهو نزول المطر؛ الصيب السحاب ذو الصوب (maqayis)
- **B002** yanlışa karşı doğru olan — yanlışın karşıtı olan doğru ve uygun şey · ona doğru yaptın demek · bir davranışı doğru saymak · doğru sonuca yönelmek veya onu bulmak · işin tam yerine oturması
  الصواب نقيض الخطأ (ayn)؛ خطئي وصوبي أي صوابي؛ الصواب نقيض الخطأ؛ صوبه أي قال له أصبت؛ استصوب فعله واستصاب فعله (sihah)؛ الصواب نقيض الخطأ؛ أصاب فلان الصواب فأخطأ الجواب (tahdhib)؛ الصواب يقال على وجهين؛ في نفسه محمودا ومرضيا؛ باعتبار القاصد إذا أدرك المقصود؛ الصواب التام (mufradat)؛ الصواب في القول والفعل؛ خلاف الخطأ؛ قد صابت بقر (maqayis)
- **B003** hedefe yönelip varma — okun hedefe yönelmesi veya hedefe varması · hedefe yönelen ok · arananı bulmak veya hedeflenene ulaşmak · yönünü koru · yönünden sapmayan
  صاب السهم نحو الرمية يصوب صيبوبة إذا قصد؛ سهم صائب أي قاصد؛ أقم صوبك أي قصدك؛ مستقيم الصوب إذا لم يزغ عن قصده (ayn)؛ صاب السهم يصوب صيبوبة أي قصد ولم يجر؛ صاب السهم القرطاس؛ أصابه أي وجده (sihah)؛ صاب إذا أصاب؛ صاب السهم نحو الرمية يصوب صيبوبة إذا قصد؛ صاب السهم الرمية يصوبها وأصابها إذا قصدها؛ حيث أراد أنه يصيب (tahdhib)؛ أصاب كذا أي وجد ما طلب؛ أصاب السهم إذا وصل إلى المرمى بالصواب (mufradat)
- **B004** başına gelen kötü olay — kişinin başına gelen kötü olay veya sıkıntı · başına kötü olay gelmek · kötü olaydan etkilenmiş ya da aklı bozulmuş kişi · akılda hafif bozulma
  أصابته مصيبة أي أخذته فهو مصاب؛ في عقله صابة أي فيه طرف من الجنون (sihah)؛ مصيبة كانت في الأصل مصوبة؛ مصائب؛ في عقل فلان صابة؛ يقال للمجنون مصاب (tahdhib)؛ المصيبة أصلها في الرمية ثم اختصت بالنائبة؛ أصاب جاء في الخير والشر؛ الإصابة في الخير اعتبارا بالصوب وفي الشر اعتبارا بإصابة السهم (mufradat)
- **B005** aşağı eğme — aşağı doğru eğimli oluş · kabı veya tahta ucunu aşağı indirmek · başı aşağı eğme · atı koşuya salmak
  التصوب حدب في حدور؛ صوبت الإناء ورأس الخشبة إذا خفضته؛ كره تصويب الرأس في الصلاة (ayn)؛ التصوب مثله؛ صوبت الفرس إذا أرسلته في الجري؛ صوب رأسه أي خفضه (sihah)؛ التصوب حدب في حدور؛ صوبت الإناء ورأس الخشبة تصويبا إذا خفضته؛ كره تصويب الرأس في الصلاة (tahdhib)؛ التصويب حدب في حدور لا يكون إلا كذا (maqayis)
- **B006** saf seçkin öz — her şeyin seçkin kısmı · topluluğun saf soyu ve iç özü
  الصياب الخيار من كل شيء؛ الصياب والصيابة أصل كل قوم؛ من صميم النوب (ayn)؛ قوم صياب أي خيار؛ صيابة قومه وصوابة قومه أي في صميم قومه؛ الصيابة الخيار من كل شيء (sihah)؛ من صيابة قومه أي من مصاصهم وأخلصهم نسبا؛ من صوابة قومه مثله (tahdhib)؛ الصيابة فالخيار من كل شيء؛ كأنه من الصوب وهو خالص ماء السحاب (maqayis)
- **B007** acı bitki özsuyu — acı ağaç veya bitki özsuyu
  الصاب عصارة شجرة مرة؛ يقال هو عصارة الصبر (ayn)؛ الصاب عصارة شجر مر (sihah)؛ الصاب والسلع ضربان من الشجر مران؛ الصاب عصارة شجر مر (tahdhib)
- **B008** dökülüp oluşan yığın — toprak yığını, hurma yeri veya dökülmüş şey
  أهل الفلج يسمون الجرين الصوبة وهو موضع التمر؛ الدنانير صوبة أي مهيلة (sihah)؛ الصوبة الكثبة من تراب أو غيره (tahdhib)
- **B009** yana sapma — yana eğilmek veya sapmak · kötülükten uzaklaşıp ayrılmak
  صاف عن الشر إذا عدل؛ من باب الإبدال؛ يقال صاب إذا مال؛ وقد ذكر في بابه (maqayis)

## ي د ي (root_001693): 42:30 أَيْدِيكُمْ, 42:48 أَيْدِيهِمْ

- **B001** el ve elin uğradığı bedensel durumlar — el · elinden vurmak · eli kökünden kesilmiş kimse · el ağrısı · eli tuzağa yakalanmış olmak
  اليَد الجارحة (mufradat)؛ اليد أصلها يدي وجمعها أيد ويدي (sihah)؛ يديت الرجل إذا ضربت يده (jamhara;sihah;tahdhib;mufradat)؛ رجل ميدي أي مقطوع اليد واليداء وجع اليد (tahdhib)
- **B002** güç, yeterlik ve güçlendirme — güç ve yeterlik · güç · güçlendirmek · buna gücüm yetmez
  اليد القوة وأيده أي قواه (sihah)؛ ما لي به يدان أي قوة (tahdhib;mufradat)؛ أولي الأيدي أي أولي القوة (tahdhib;mufradat)
- **B003** karşılıksız iyilik ve bağış — iyilik ve karşılıksız yarar · iyilikte bulunmak · satış, borç ya da karşılık olmadan vermek
  أيديت إلى الرجل يدا إذا أسديتها إليه (jamhara)؛ اليد النعمة والإحسان (sihah;tahdhib;mufradat)؛ أعطاه مالا عن ظهر يد تفضلا ليس من قرض ولا مكافأة (sihah;tahdhib)؛ يده مطلقة عبارة عن إيتاء النعيم (mufradat)
- **B004** elinde bulunma, sahiplik ve denetim [kalıp] — onun elinde, sahipliğinde ve denetiminde
  هذا الشيء في يدي أي في ملكي (sihah)؛ هذه الضيعة في يد فلان أي ملكه (tahdhib)؛ للحوز والملك يقال هذا في يد فلان (mufradat)
- **B005** egemenlik ve buyurma gücü — egemenlik ve buyurma gücü · rüzgarın yön verme gücü
  اليد السلطان (tahdhib)؛ اليد في هذا لفلان أي الأمر النافذ لفلان (tahdhib)؛ أيديكم فوق أيديهم (mufradat)؛ عن قهر وذل (tahdhib)
- **B006** boyun eğme, bağlılık ve güvence üstlenme — boyun eğme ve uyma · buyruğuna girdim · bunun için sana güvence veriyorum · bağlılıktan çıkmak
  عن يد أي عن ذلة واستسلام (sihah)؛ اليد الطاعة واليد الاستسلام (tahdhib)؛ هذه يدي لك (tahdhib)؛ يدي لك رهن بكذا أي ضمنت وكفلت (tahdhib)؛ خلع فلان يده عن الطاعة (tahdhib)
- **B007** elden ele verme, peşin ödeme ve iki fiyatlı satış — elden ele, doğrudan karşılık vererek · karşılığını elden vermek · elden ele verme · iki ayrı fiyatla
  ياديت فلانا جازيته يدا بيد (sihah)؛ أعطيته مياداة أي من يدي إلى يده (sihah)؛ عن يد نقدا عن ظهر يد ليس بنسيئة (sihah;tahdhib)؛ ابتعت الغنم باليدين أي بثمنين مختلفين (sihah;tahdhib)؛ باع غنمه اليدين أن يسلمها بيد ويأخذ ثمنها بيد (tahdhib)
- **B008** önünde ya da hemen öncesinde [kalıp] — önünde veya hemen öncesinde
  بين يدي الساعة أهوال أي قدامها (sihah)؛ بين يديك كذا لكل شيء أمامك (tahdhib)؛ يثور الرهج بين يدي المطر ويهيج السباب بين يدي القتال (tahdhib)
- **B009** kişinin kendi yaptığı iş ve doğurduğu sorumluluk [kalıp] — senin yaptığın, işlediğin ve kazandığın şey
  هذا ما قدمت يداك أي جنيته أنت (sihah)؛ ذلك بما كسبت يداك (tahdhib)؛ مما كتبت أيديهم فنسبته إلى أيديهم تنبيه على أنهم اختلقوه (mufradat)
- **B010** pişman olup hayıflanma [kalıp] — pişman olup hayıflanmak
  سقط في يديه وأسقط أي ندم (sihah)؛ اليد الندم ويقال سقط في يده إذا ندم (tahdhib)؛ ولما سقط في أيديهم أي ندموا (mufradat)
- **B011** yönlere dağılıp gitme ve izlenen yol [kalıp] — her yana dağılıp gitmek · deniz yolu
  ذهبوا أيدي سبا وأيادي سبا أي متفرقين (sihah)؛ اليد الطريق يقال أخذ فلان يد بحر إذا أخذ طريق البحر (tahdhib)؛ ذهب القوم أيدي سبا أي متفرقين في كل وجه (tahdhib)
- **B012** zaman boyunca, sonsuza dek [kalıp] — zaman boyunca, sonsuza dek
  لا أفعله يد الدهر أي أبدا (sihah)؛ يد الدهر مد زمانه (tahdhib)؛ شبه الدهر فجعل له يد في قولهم يد الدهر (mufradat)
- **B013** bir nesnenin tutacağı, ucu ya da uzantısı [kalıp] — nesnenin tutacağı, ucu, kolu veya uzantısı
  يد الثوب ما فضل منه إذا تعطفت به والتحفت (sihah)؛ يد الفأس مقبضها ويد القوس سيتها (tahdhib)؛ قميص قصير اليدين أي قصير الكمين (tahdhib)؛ يد المسند (mufradat)
- **B014** geniş, bol ve rahat [kalıp] — geniş ve rahat yaşam · bol ve geniş giysi
  عيش يدي واسع (jamhara)؛ ثوب يدي وأدي أي واسع (sihah)؛ ثوب يدي واسع (tahdhib)
- **B015** eli işe yatkın ve becerikli — eli işe yatkın, becerikli
  امرأة يدية أي صناع (sihah;mufradat)؛ رجل يدي (sihah;mufradat)؛ النسبة إلى يد يدي (tahdhib)
- **B016** birlik içinde destek ve koruma [kalıp] — başkalarına karşı tek güç olarak dayanışmak · onun destekçisi ve koruyucusu
  المسلمون يد على من سواهم أي كلمتهم ونصرتهم واحدة (tahdhib)؛ اليد الغياث واليد منع الظلم (tahdhib)؛ فلان يد فلان أي وليه وناصره (mufradat)؛ أنا يدك (mufradat)
- **B017** yemeye başlama buyruğu [kalıp] — ye, yemeğe başla
  اليد الأكل يقال ضع يدك أي كل (tahdhib)

## ECHO ء ي د (root_000071): for 42:30 أَيْدِيكُمْ, 42:48 أَيْدِيهِمْ: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## ك ث ر (root_001286): 42:30 كَثِيرٍ, 42:34 كَثِيرٍ

- **B001** çokluk ve sayıca artma — çokluk; sayının artması ve azlığın karşıtı · bir şey çoğaldı, sayısı arttı · çok, sayıca fazla · bir şeyi çoğaltmak · bir şeyden çokça edinmek veya onu çok saymak · malın ya da durumun azı ve çoğu · pek çok, çok büyük sayıda
  الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)
- **B002** çokluk yarışı ve çoklukla üstün gelme — onlarla çokluk yarışına girdik ve onları sayıca geçtik · mal, sayı veya güç bakımından çokluk yarışı ve övünme · çokluk yarışında yenilmiş
  كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)
- **B003** kişiye bağlı çokluk nitelemeleri [kalıp] — malı çok kişi · çok konuşan kadın veya erkek · iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi · başkasının malıyla kendini varlıklı göstermek
  رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)
- **B004** özel ırmak veya bol iyilik — cennetteki özel ırmak · bol veya büyük iyilik · iyiliği ve bağışı bol, cömert önder
  الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)
- **B005** kabarıp yükselen yoğun toz — kabarıp yükselen yoğun toz · son derece çoğalmak
  الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)
- **B006** hurma ağacının iç göbeği — hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü · meyve veya hurma göbeği için el kesme cezası yoktur · hurma ağacı çiçek sürgünü verdi
  الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)
- **B007** bir araya toplanma — bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir
  الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)

## ع ج ز (root_000985): 42:31 بِمُعْجِزِينَ

- **B001** güç yetirememe ve yetersiz kalma — bir şeyi yapmaya gücü yetmemek · güçsüzlük ve yetersizlik · caydırma veya yetersiz sayma · çiftleşmeye gücü yetmemek
  يدل أحدهما على الضعف (maqayis)؛ عجز عن الشيء يعجز عجزا فهو عاجز أي ضعيف (maqayis;ayn)؛ العجز نقيض الحزم (maqayis;ayn)؛ عجزت تعجز عجزا من التقصير (jamhara)؛ العجز: الضعف (sihah)؛ التعجيز: التثبيط (sihah)؛ من قصر عنه عجز (tahdhib)؛ فحل عجيز وعجيس إذا عجز عن الضراب (jamhara;tahdhib)؛ القصور عن فعل الشيء وهو ضد القدرة (mufradat)
- **B002** takipten sıyrılıp erişilemez olma — takipte ona yetişememek, onu elden kaçırmak · uzaklaşıp erişilemez olmak · yarışarak öne geçenler veya kaçabileceklerini sananlar · güvenilir bir sığınağa yönelmek
  أعجزني فلان إذا عجزت عن طلبه وإدراكه (maqayis;ayn;tahdhib)؛ فلان عاجز فلانا إذا ذهب فلم يوصل إليه (maqayis)؛ عاجز فلان إذا ذهب فلم يقدر عليه (ayn;sihah)؛ معنى الإعجاز الفوت والسبق (tahdhib)؛ معاجزين تفسيره معاندين وقيل مسابقين (tahdhib)؛ معاجزين قيل ظانين ومقدرين أنهم يعجزوننا (mufradat)؛ إنه ليعاجز إلى ثقة إذا مال إليه (sihah;tahdhib)
- **B003** yaşlılık ve eskilikle adlandırma — yaşlı kadın veya yaşlı erkek · kadının yaşlanması · yıllanmış içki · kılıç namlusu ya da kabza çivilerinden biri · geleneksel takvimde özel adla anılan beş günlük dönem
  العجوز المرأة الشيخة (maqayis;ayn;tahdhib)؛ عجزت المرأة إذا صارت عجوزا (jamhara;sihah;tahdhib)؛ العجوز المرأة الكبيرة (sihah)؛ العجوز سميت لعجزها في كثير من الأمور (mufradat)؛ الخمر عجوز لعتقها (maqayis;sihah;tahdhib)؛ العجوز نصل السيف (maqayis;ayn;sihah;tahdhib)؛ يقال للرجل عجوز وللمرأة عجوز (tahdhib)
- **B004** arka kısım, art bölüm ve son — arka bölüm, insanın kalçası · işlerin sonları · develerin arka bölümleri · kadının kalçası · kalçası iri kadın · kadının kalçasının irileşmesi · devenin arka tarafına binmek · kalçayı iri göstermek için bağlanan yastık benzeri dolgu
  العجز مؤخر الشيء والجمع أعجاز (maqayis;ayn;sihah)؛ عجز الإنسان مؤخره وبه شبه مؤخر غيره (mufradat)؛ أعجاز الإبل مآخيرها (tahdhib)؛ عجز الأمر وأعجاز الأمور (maqayis)؛ العجيزة عجيزة المرأة خاصة (maqayis;ayn;sihah;tahdhib)؛ امرأة عجزاء عظيمة العجز (maqayis;ayn;jamhara;sihah;tahdhib)؛ تعجزت البعير ركبت عجزه (sihah;tahdhib)؛ العجازة ما تعظم به المرأة عجيزتها (jamhara;sihah;tahdhib)
- **B005** bitki tutan yüksek kum sırtı [kalıp] — bitki yetişmesine elverişli yüksek kum sırtı · belirli bir çöl bölgesindeki özel adlı kum tepesi
  العجزاء من الرمل رملة مرتفعة كأنها جبل (maqayis)؛ العجزاء من الرمل خاصة رملة مرتفعة كأنها جبل ليس بركام رمل وهي مكرمة المنبت (ayn)؛ العجزاء رملة مرتفعة (sihah)؛ العجوز رملة بالدهناء (sihah)؛ العجزاء من الرمال حبل مرتفع كأنه جلد ليس بركام رمل وهو مكرمة للنبت (tahdhib)
- **B006** arka bölüm hastalığı, kartal niteliği ve kuşun arka parmağı [kalıp] — binek hayvanının arka kısmını tutup ağırlaştıran hastalık · arka bölümü, kuyruğu veya arka pençesiyle nitelenen kartal · kuşun arka parmağı
  العجز داء يأخذ الدابة في عجزها (maqayis;ayn)؛ العجزاء من العقبان الخفيفة العجيزة (maqayis)؛ عقاب عجزاء اختلفوا في تفسيره (jamhara)؛ إذا كان في ذنبها ريشة بيضاء أو ريشتان (jamhara;tahdhib)؛ عقاب عجزاء للقصيرة الذنب (sihah)؛ العجزاء الشديدة الدابرة والشديدة الكف (jamhara)؛ يقال لدابرة الطائر العجازة (tahdhib)
- **B007** ileri yaşta doğan son çocuk — yaşlı anne veya babanın son çocuğu · ileri yaştaki ebeveynlerin son çocuğu
  العجزة وابن العجزة آخر ولد الشيخ (maqayis;ayn;tahdhib)؛ آخر ولد المرأة إذا أسنت وكذلك الرجل (jamhara)؛ العجزة آخر ولد الرجل (sihah)؛ فلان عجزة ولد أبويه إذا كان آخرهم (sihah;tahdhib)؛ ولد لعجزة أي بعدما كبر أبواه (ayn;tahdhib)

## ج ر ي (root_000240): 42:32 ٱلْجَوَارِ

- **B001** bir yol boyunca akıp, koşup ya da ilerleyerek gitme — hızlı ilerleyiş ve kendi yatağında akış · aktı, koştu ya da yol aldı · suyun akışı · at koşusu · akıtmak ya da harekete geçirmek · akış, gidiş yolu ya da koşu yeri · denizde yol alan gemi · gökte yol alan güneş · suyu akan pınar · denizde yol alan gemiler · çeşitli koşu biçimleri olan at · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  أصل واحد وهو انسياح الشيء (maqayis)؛ جرى الماء يجري جرية وجريا وجريانا (maqayis;sihah;mufradat)؛ الخيل تجري والرياح تجري والشمس تجري جريا (ayn;tahdhib)؛ الجارية السفينة والجارية الشمس (maqayis;sihah)
- **B002** alışılmış yol ve davranış düzeni — kişinin alışkanlık edindiği ve sürekli izlediği yol
  للعادة الإجريا (maqayis)؛ الإجريا طريقته التي يجري عليها من عادته (ayn)؛ الإجريا الجري والعادة مما تأخذ فيه (sihah)؛ الإجرياء الوجه الذي نأخذ فيه (tahdhib)؛ الإجريا العادة التي يجري عليها الإنسان (mufradat)
- **B003** başkası adına iş gören, haber götüren ya da güvence veren kimse — başkası adına iş gören, haber götüren ya da güvence veren kimse · başkası adına iş görecek birini tutmak · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  الجري الوكيل (maqayis;tahdhib)؛ الجري الرسول (ayn;tahdhib;mufradat)؛ الجري الضامن (tahdhib)؛ استجريت أي اتخذت وكيلا (maqayis;sihah;tahdhib)؛ لا يستجرينكم الشيطان (maqayis;sihah;tahdhib;mufradat)
- **B004** genç kız ve ona bağlı genç kızlık çağı — genç kız ya da hizmette çalıştırılan genç kadın · genç kızlık çağı · genç kızlık durumu
  الجارية من النساء لأنها تستجرى في الخدمة (maqayis)؛ الجارية مصدرها الجراء (ayn)؛ جارية بينة الجراية والجراء (sihah;tahdhib)؛ أيام جرائها أي صباها (maqayis;ayn;sihah)
- **B005** kuş kursağı — 
  الجرية وهي الحوصلة أصلها قرية (maqayis)؛ الجرية مثل القرية هي الحوصلة (sihah)؛ الجرية والقرية والنوطة لحوصلة الطائر (tahdhib)؛ يقال للحوصلة جرية لأنها مجرى الطعام (mufradat)
- **B006** sürekli verilen geçimlik ya da kalıcı yarar — düzenli görev ödeneği · onun için sürekli verildi ya da sürüp gitti · ona sürekli olarak verdim · yararı süren bağış
  الجراية الجاري من الوظائف (sihah)؛ الأرزاق جارية والأعطيات دارة (tahdhib)؛ جرى عليه ذلك الشيء ودر له بمعنى دام له (tahdhib)؛ أجريت له كذا أي أدمت له (tahdhib)؛ صدقة جارية (tahdhib)
- **B007** birlikte ilerleyip birbirine ayak uydurma — yanında koşmak ya da ona ayak uydurmak · söyleşide ona ayak uydurmak ve karşılık vermek
  جاراه مجاراة وجراء أي جرى معه (sihah)؛ جاراه في الحديث وتجاروا فيه (sihah)
- **B008** senin yüzünden ya da senin için — senin yüzünden ya da senin için
  فعلت ذلك من جراك ومن جرائك أي من أجلك (sihah)

## ب ح ر (root_000086): 42:32 ٱلْبَحْرِ

- **B001** genis büyük su kütlesi — genis ve cok su, büyük su kütlesi veya büyük irimak · kucuk deniz gibi anilan su birikimi ya da büyük gol
  سمي به لاستبحاره وهو انبساطه وسعته (ayn;tahdhib)؛ كل مكان واسع جامع للماء الكثير (mufradat)؛ كل نهر عظيم بحر (sihah;tahdhib)؛ إذا كان البحر صغيرا قيل له بحيرة (ayn;tahdhib)
- **B002** genisleyip derinlesmek — bilgisinde veya herhangi bir alanda genislemis kisi · bir seyi deniz genisligi gibi genisletmek · bilgi, mal veya otlakta genislemek ve derinlesmek · kosusu genis, cok kosan iyi at
  استبحر في العلم (ayn;tahdhib;mufradat)؛ تبحر في العلم وغيره أي تعمق فيه وتوسع (sihah)؛ تبحر الراعي في رعي كثير (ayn;tahdhib)؛ تبحر في المال إذا كثر ماله (tahdhib)؛ فرس بحر باعتبار سعة جريه (sihah;tahdhib;mufradat)؛ استبحر الشاعر إذا اتسع له القول (tahdhib)
- **B003** kulagi genis yarikla kesmek — kulagi genis bir yarikla kesip delmek · kulagi yarilip belli bir adet icin saliverilen deve veya koyun
  الناقة تبحر بحرا وشق أذنها (ayn)؛ بحرت أذن الناقة بحرا شققتها وخرقتها (sihah)؛ بحروا أذنها أي شقوها (tahdhib)؛ بحرت البعير شققت أذنه شقا واسعا ومنه سميت البحيرة (mufradat)
- **B004** suyun tuzlu olmasi — tuzlu su · suyun tuzlu hale gelmesi · tuzlu su
  ماء بحر أي ملح وأبحر الماء ملح (sihah)؛ الماء البحر هو الملح وقد أبحر الماء إذا صار ملحا (tahdhib)؛ ماء بحراني أي ملح وقد أبحر الماء (mufradat)
- **B005** acikta karsilasmak [kalıp] — onu acikta, arada engel olmadan karsiladim
  لقيته صحرة بحرة أي بارزا ليس بينك وبينه شيء (sihah)؛ وهو من قولهم لقيته صحرة بحرة (tahdhib)؛ لقيته صحرة بحرة أي ظاهرا حيث لا بناء يستره (mufradat)
- **B006** yer ve su cukuru adi — belde, toprak veya köy · cayir, alcak yer, su biriktiren cukur veya vadi bitkiligi · arazide su birikintilerinin cogalmasi
  البحرة البلدة هذه بحرتنا أي بلدتنا وأرضنا (sihah;tahdhib)؛ لكل قرية هذه بحرتنا (tahdhib)؛ الروضة بحرة وقد أبحرت الأرض إذا كثر مناقع الماء فيها (tahdhib)؛ البحرة الأوقة يستنقع فيها الماء (tahdhib)؛ البحرة المنخفض من الأرض (tahdhib)؛ البحرة منبت الثمام من الأودية (tahdhib)
- **B007** derinlikten gelen koyu kirmizilik — rahmin dibi veya derinligi · saf ve siddetli kirmizi kan · cok siddetli kirmizi
  البحر عمق الرحم ومنه الدم الخالص الحمرة باحر وبحراني (sihah)؛ أبحر الرجل إذا اشتدت حمرة أنفه (tahdhib)؛ أحمر باحري وبحراني (tahdhib)؛ الدم البحراني منسوب إلى قعر الرحم وعمقها (tahdhib)؛ دم باحري إذا كان شديد الحمرة (tahdhib)
- **B008** saskinliktan donakalmak — konusulunca sersem gibi kalan aptal kimse · korkudan saskinliga düsmek veya denizi görünce ürküp donakalmak
  الباحر الأحمق الذي إذا كلم بحر وبقي كالمبهوت (ayn)؛ الباحر الأحمق (sihah;tahdhib)؛ بحر الرجل إذا تحير من الفزع (sihah)؛ بحر الرجل إذا رأى البحر ففرق حتى دهش (tahdhib)؛ الباحر الفضولي والباحر الكذاب (tahdhib)
- **B009** denize binmek ve denize nispetli olmak — denize veya suya binip yolculuk etmek · Bahreyn'e nispet edilen · denize nispet edilen veya deniz yolculuguna cikan topluluk
  أبحر فلان إذا ركب البحر (sihah)؛ أبحر الرجل إذا ركب البحر والماء (tahdhib)؛ رجل بحراني منسوب إلى البحرين (ayn;tahdhib)؛ النسبة إلى البحرين بحراني (sihah;tahdhib)؛ كل ما نسب إلى البحر فهو بحري (tahdhib)؛ البحرية لأنها ركبت البحر (tahdhib)
- **B010** kastsiz rastlamak — bir insana onu görme niyeti olmadan rastlamak
  أبحر إذا صادف إنسانا على غير اعتماد وقصد لرؤيته (tahdhib)
- **B011** verem gibi zayiflatici hastalik — kisinin vereme tutulmasi · verem doguran hastalik veya bedeni etten düsüren zayiflama
  أبحر الرجل إذا أخذه السل (tahdhib)؛ البحير والبحر الذي به السل (tahdhib)؛ البحر داء في الإبل وقد بحرت (sihah)؛ وأما البحر فهو داء يورث السل (tahdhib)؛ البحير المسلول الجسم الذاهب اللحم (tahdhib)
- **B012** sonradan turemis tibbi kriz terimi — akut hastalikta hastaya birden gelen degisim · tibbi kriz günü · Temmuz sicaginin siddetli günü
  التغير الذي يحدث للعليل دفعة في الأمراض الحادة بحران (sihah)؛ هذا يوم بحران بالإضافة (sihah)؛ يوم باحورى منسوب إلى باحور وباحوراء وهو شدة الحر في تموز؛ وجميع ذلك مولد (sihah)
- **B013** büyük karinli — büyük karinli kimse
  يقال للعظيم البطن بحري (tahdhib)
- **B014** sudan kanmayacak kadar susamak — siddetle susayip sudan kanmamak
  بحر إذا اشتد عطشه فلم يرو من الماء (sihah)؛ الداء الذي يصيب البعير فلا يروى من الماء هو النجر والبجر وكذلك البقر، وأما البحر فهو داء يورث السل (tahdhib)

## س ك ن (root_000726): 42:33 يُسْكِنِ

- **B001** hareketin dinip durulması — hareketin sona erip şeyin durması · hareketi veya çalkantısı dindi ve durdu · rüzgar, yağmur ya da öfke dindi · hareketsiz, yerinde duran veya dingin
  خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك
- **B002** bir yere yerleşip orada yaşama — bir yere yerleşip orada yaşadı · konut, ev veya yaşanan yer · bir evi kira almadan oturması için verme · onu bir evde veya yerde oturttu · konut olarak kullanılan ev veya yer
  يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن
- **B003** ev halkı ve orada yaşayanlar — ev halkı ve aile üyeleri · bir yerde yaşayanlar · evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar
  السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار
- **B004** insanı rahatlatıp içini yatıştıran dayanak — insanın yanında rahatlayıp içinin yatıştığı kişi veya şey · yanında oturulup rahatlık bulunan ateş · senin yakarışların onları rahatlatır · geceyi dinlenme ve dinginleşme zamanı yaptı · eğri sırığı ateş ve yağla doğrultma
  كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها
- **B005** güven veren ağırbaşlı iç dinginlik — ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği · sandıktaki, kalpleri yatıştırıp güven veren şey · inananların kalplerine güven ve dinginlik verdi
  السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين
- **B006** yoksulluk, güçsüzlük ve ezilmişlik — yoksul ya da ezilmiş ve güçsüz kişi · yoksulluk veya ezilmişlik durumu · yoksul duruma geldi ya da boyun eğip kendini alçalttı · boyun eğdi ve alçaldı · Tanrı onu yoksul duruma düşürdü
  المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل
- **B007** kesici bıçak — kesici bıçak · bıçak yapan kimse
  السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح
- **B008** geminin kıçındaki dengeleyici yöneltme aracı — geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç · gemiyi dengede tutup çalkantısını azaltan kıç parçası
  سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به
- **B009** sabit yer ve konum bildiren özel kullanımlar — başın boyuna oturduğu yer · yerlerinizde, konumlarınızda veya alışılmış düzeninizde · belirli bir bölgedeki özel yer adı
  موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم
- **B010** yerinde kalmayı sağlayan geçimlik ve bol otlak — bulunduğu yerde geçinmeyi sağlayan yiyecekler · yerinde kalmayı sağlayan bir geçimlik · sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak
  الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه

## ر و ح (root_000609): 42:33 ٱلرِّيحَ, 42:52 رُوحًا

- **B001** bedene canlılık veren iç varlık — bedene yaşam veren ve ölümde ayrılan iç varlık
  الروح النفس التي يحيا بها البدن؛ خرجت روحه أي نفسه (ayn)؛ روح الإنسان مختلف فيه فقال قوم هي نفسه التي يقوم بها جسمه وقال آخرون الروح خلاف النفس (jamhara)؛ الروح يذكر ويؤنث والجمع الأرواح (sihah)؛ فالروح روح الإنسان وإنما هو مشتق من الريح (maqayis)
- **B002** kutsal bildiri veya göksel varlık adı — vahyi taşıyan göksel elçi veya kutsal bildiri için kullanılan ad · göksel varlıklara ilişkin veya canlılık taşıyan
  الروحاني من الخلق نحو الملائكة؛ الروح جبرئيل وهو روح القدس؛ الروح ملك يقوم وحده (ayn)؛ الروح الأمين جبريل؛ الروحانيون من الملائكة (jamhara)؛ يسمى القرآن روحا وكذلك جبريل وعيسى؛ روحانيون (sihah)؛ والروح جبرئيل عليه السلام (maqayis)
- **B003** hareket eden hava ve esinti — rüzgar · yel esintisi · yeli hoş gün · sert yelli gün · yelpaze · rüzgar geçiren açık yer
  الريح معروفة وأصل هذه الياء واو (jamhara)؛ الريح واحدة الرياح والأرياح؛ الروح نسيم الريح؛ يوم روح وريوح أي طيب؛ راح اليوم إذا اشتدت ريحه؛ المروحة ما يتروح بها والموضع الذي تخترق فيه الرياح (sihah)؛ أصل ذلك كله الريح؛ الروح نسيم الريح؛ ريح الغدير أصابته الريح؛ أراح القوم دخلوا في الريح؛ يوم ريح طيب ويوم راح ذو ريح شديدة؛ المروحة الموضع تخترق فيه الريح (maqayis)؛ فالريح معروفة (maqayis-ريح)
- **B004** koku ve kokudaki değişim — şeyin kokusu · burunla algılanan koku · et koktu · suyun kokusu değişti · kokulandırılmış yağ
  إرواح اللحم تغير ريحه (ayn)؛ مكان ريح أي طيب الروح (jamhara)؛ وجدت ريح الشيء ورائحته؛ الدهن المروح المطيب؛ أراح اللحم أي أنتن؛ أراح الشيء أي وجد ريحه؛ أروح الماء وغيره أي تغيرت ريحه؛ تروح الماء إذا أخذ ريح غيره؛ أروحت من فلان طيبا (sihah)؛ أروح الماء وغيره تغيرت رائحته؛ الدهن المروح المطيب؛ لم يرح رائحة الجنة؛ أروحني الصيد إذا وجد ريحك؛ أروحت من فلان طيبا (maqayis)
- **B005** geç gün vakti ve akşam dönüşü — öğle sonrası vakit ve bu vakitte gidiş · geç gün vaktinde yola çıktı · sürüyü akşam barınağa döndürdü · sürünün geceleme yeri
  الرواح من لدن زوال الشمس إلى الليل؛ السير والعمل بالعشي؛ تروح القوم في معنى راحوا؛ المراح الموضع؛ الإراحة رد الإبل بالعشي (ayn)؛ راح الرجل من رواح العشي؛ أراح ماشيته؛ الرواح الراحة أيضا (jamhara)؛ الرواح نقيض الصباح من زوال الشمس إلى الليل؛ سرحت الماشية بالغداة وراحت بالعشي؛ المراح حيث تأوي إليه الإبل والغنم؛ المراح الموضع الذي يروح منه القوم أو يروحون إليه (sihah)؛ الرواح العشي؛ راحوا في ذلك الوقت من لدن زوال الشمس إلى الليل؛ أرحنا إبلنا رددناها ذلك الوقت؛ المراح حيث تأوي الماشية بالليل (maqayis)
- **B006** hakkını kendisine geri vermek [kalıp] — onun hakkını kendisine geri verdim
  أرحت على الرجل حقه إذا رددته عليه (sihah)؛ أرحت على الرجل حقه إذا رددته إليه (maqayis)
- **B007** dinlenip güç toplama — dinlenme ve yorgunluğu giderme · soluklandı ve yorgunluktan toparlandı · kolaylık ve sıkıntısızlık · gereksinim giderme yeri · ona yaslanıp dinginleşti · gece ibadetinin her dört bölümlük dizisinden sonraki dinlenme
  ما لفلان في كذا من رواح أي من راحة (ayn)؛ الرواح الراحة أيضا؛ أرحت فلانا من كذا إراحة (jamhara)؛ الروح والراحة من الاستراحة؛ أراحه الله فاستراح؛ أراح الرجل رجعت إليه نفسه بعد الإعياء؛ أراح تنفس؛ افعل ذاك في سراح ورواح أي سهولة؛ استراح الرجل من الراحة؛ المستراح المخرج؛ استروح إليه أي استنام (sihah)؛ أراح الإنسان إذا تنفس؛ أراح الرجل إذا رجعت إليه نفسه بعد الإعياء؛ أفعل ذلك في سراح ورواح أي في سهولة؛ سميت الترويحة لاستراحة القوم (maqayis)
- **B008** iki seçenek arasında nöbetleşme — iki iş veya durum arasında nöbetleşme · ağırlığını sırayla iki bacağına verdi
  المراوحة عملان في عمل يعمل ذاك مرة وهذا مرة (ayn)؛ المراوحة في العملين أن يعمل هذا مرة وهذا مرة؛ راوح بين رجليه إذا قام على إحداهما مرة وعلى الأخرى مرة (sihah)؛ المراوحة في العملين أن يعمل هذا مرة وهذا مرة (maqayis)
- **B009** duyusal açıklık ve yayvan genişlik — ayakların ön bölümlerindeki açıklık · ayak uçları birbirinden açık duran · sığ ve geniş çanak
  رجل أروح في صدر قدمه انبساط؛ بعير أروح وقدم أروح وروحاء؛ قصعة روحاء قريبة القعر (ayn)؛ رجل أروح وامرأة روحاء وهو دون الفحج (jamhara)؛ الروح بالتحريك السعة؛ الروح أيضا سعة في الرجلين؛ قصعة روحاء أي قريبة القعر (sihah)؛ أصل كبير يدل على سعة وفسحة؛ الأروح الذي في صدور قدميه انبساط؛ قصعة روحاء قريبة القعر؛ لكل شيء واسع أريح (maqayis)
- **B010** iyiliğe hevesle yönelme — iyilik için gönüllü coşku ve geniş gönüllülük · iyilik yapmaya hevesle yöneldi
  راح فلان للمعروف يراح راحة إذا أخذته له خفة وأريحية؛ راحت يده بكذا؛ الراح الارتياح؛ الارتياح النشاط؛ الأريحي الواسع الخلق؛ أخذته الأريحية إذا ارتاح للندى (sihah)؛ يقال فلان يراح للمعروف إذا أخذته له أريحية؛ أريحي؛ الأريحي مأخوذ من راح يراح (maqayis)
- **B011** güç, üstünlük ve egemenlik — güç, üstünlük ve egemenlik
  قد تكون الريح بمعنى الغلبة والقوة؛ وتذهب ريحكم (sihah)؛ الريح الغلبة والقوة في قوله تعالى فتفشلوا وتذهب ريحكم (maqayis-ريح)
- **B012** kokulu bitki veya ekin yaprağı — kokulu bitki veya ekinin yaprağı
  الريحان نبت معروف؛ والحب ذو العصف والريحان فالعصف ساق الزرع والريحان ورقه (sihah)؛ الريحان معروف (maqayis-ريح)
- **B013** ferahlık ve geçim payı — ferahlık veya esirgeme ile geçim payı · yaratıcıdan gelen veya istenen geçim payı
  روح وريحان؛ الروح الراحة والريحان الرزق (jamhara)؛ روح وريحان أي رحمة ورزق؛ الريحان الرزق؛ خرجت أبتغي ريحان الله؛ سبحان الله وريحانه يريدون استرزاقا (sihah)؛ الريحان الرزق؛ الولد من ريحان الله (maqayis-ريح)
- **B014** avuç içi — avuç içi · avuç içleri
  راحة الإنسان معروفة والجمع راح (jamhara)؛ الراح جمع راحة وهي الكف (sihah)؛ الراح جماعة راحة الكف (maqayis)
- **B015** üzümden yapılan sarhoş edici içki — üzümden yapılan sarhoş edici içki
  الرياح بالفتح الراح وهي الخمر؛ الراح الخمر (sihah)؛ الراح الخمر (maqayis)
- **B016** öldü [kalıp] — adam öldü
  أراح الرجل أي مات (sihah)؛ يقال للميت إذا قضى قد أراح (maqayis)
- **B017** ağacın yapraklanması veya bitkinin uzaması [kalıp] — ağaç yaz sonrasında yeniden yapraklandı · bitki boy attı
  راح الشجر يراح مثل تروح أي تفطر بورق؛ تروح الشجر إذا تفطر بورق بعد إدبار الصيف؛ تروح النبت أي طال (sihah)؛ تروح الشجر وراح يراح معناهما أن يتفطر بالورق (maqayis)
- **B018** erkek atın damızlık olgunluğa erişmesi [kalıp] — erkek at damızlık olgunluğa erişti
  راح الفرس يراح راحة إذا تحصن أي صار فحلا (sihah)؛ وراح الفرس يراح راحة إذا تحصن (maqayis)
- **B019** dağılan veya yuvasına dönen kuşlar — 
  الروح في هذا البيت المتفرقة (ayn)؛ طير روح أي متفرقة؛ وقيل هي الرائحة إلى مواضعها (sihah)؛ قال قوم هي المتفرقة وقال آخرون هي الرائحة إلى أوكارها (maqayis)

## ظ ل ل (root_000966): 42:33 فَيَظْلَلْنَ

- **B001** isik kesen golge — gölge; bir seyin isigi kesmesiyle olusan ortu veya gunes gormeyen yer · gölgeler; cisimlerin ya da yerlerin golgeleri · surekli, yogun ve faydali golge · gunesin ortadan kaldirmadigi uzun veya surekli golge · agac beni golgesi altina aldi · agacin golgesine sigindi ve onu ortu edindi
  أصل واحد يدل على ستر شيء لشيء وهو الذي يسمى الظل (maqayis)؛ الظل معروف والجمع ظلال (sihah)؛ محل ما لم تطلع عليه الشمس فهو ظل (tahdhib)؛ الظل ضد الضح وهو أعم من الفيء (mufradat)
- **B002** gecenin karanlik golgesi [kalıp] — gecenin siyahligi ve karanlik ortusu
  والليل ظل (maqayis)؛ ظل الليل سواده (sihah)؛ وسواد الليل كله ظل (tahdhib)؛ يقال ظل الليل (mufradat)
- **B003** ustten golgeleyen ortu — ustten orten golgelik, bulut veya benzeri ortu · ustteki golgelikler, bulut katlari veya yukselen dalga gorunumleri · guneslik, golgelik veya buyuk cadir · gun golgeli ya da bulutlu oldu
  المظلة معروفة والظلة أول سحابة تظل (maqayis)؛ الظلال أيضا ما أظلك من سحاب ونحوه (sihah)؛ كل شيء أظلك فهو ظلة والظلة ما سترك من فوق (tahdhib)؛ الظلة سحابة تظل والظلل جمع ظلة (mufradat)
- **B004** koruyucu guvence altinda olmak — beni korudu, guvencesi ve gucu altina aldi · birinin korumasinda, guvencesinde ve yakin desteginde · iyi, rahat ve guvenli yasam
  أظللت فلانا كأنه وقاك بظله وهو عزه ومنعته (maqayis)؛ فلان يعيش في ظل فلان أي في كنفه (sihah)؛ فلان في ظل فلان أي في ذراه وفي كنفه (tahdhib)؛ يعبر بالظل عن العزة والمنعة وعن الرفاهة (mufradat)
- **B005** yaklasip uzerine gelmek — sana yaklasti, yakinina geldi · is veya zaman yaklasti, vakti gelmek uzere oldu
  أظلك فلان إذا دنا منك كأنه ألقى عليك ظله (sihah)؛ الإظلال الدنو يقال أظلك فلان وأظل شهر رمضان أي دنا منك (tahdhib)
- **B006** gunduz boyunca yapmak — bir isi gunduz yapti veya gun boyunca surdurdu · gunduz yapma veya gun boyunca surme anlaminda kullanilan bicim
  ظل يفعل كذا وذلك إذا فعله نهارا (maqayis)؛ ظللت أعمل كذا إذا عملته بالنهار دون الليل (sihah)؛ ظل فلان نهاره صائما ولا تقول العرب ظل يظل إلا لكل عمل بالنهار (tahdhib)؛ ظللت يعبر به عما يفعل بالنهار ويجري مجرى صرت (mufradat)
- **B007** deve ayaginin ic tabani — devenin ayak tabaninin ic yuzu, toynak altindaki bolge · devenin toynak altina yapisik ince et
  الأظل وهو باطن خف البعير (maqayis)؛ الأظل ما تحت منسم البعير (sihah)؛ الأظل والمنسم للبعير كالظفر للإنسان (tahdhib)
- **B008** gunes almayan agac alti suyu — agac altinda kalip gunes almayan su · az su birikintisi veya cok calili yesil alan
  الظلل الماء تحت الشجر لا تصيبه الشمس (sihah)؛ الظليلة مستنقع ماء قليل والظليلة الروضة الكثيرة الحرجات (tahdhib)
- **B009** görünen dikili cisim — golge diye adlandirildigi bildirilen gorunen dikili cisim veya kisi
  يقال هو شخوصهم (tahdhib)؛ قال بعض أهل اللغة يقال للشاخص ظل (mufradat)

## ر ك د (root_000590): 42:33 رَوَاكِدَ

- **B001** akmadan ya da devinmeden sakin ve yerinde kalmak — akışı ya da devinimi kesilip durulmak ve yerinde kalmak · akışın ya da devinimin kesilmesiyle oluşan durgunluk · yerinde duran veya sürekli sakin olup akmayan · güneşin öğle noktasında durmuş görünmesi · insanın ya da başka bir varlığın durup kaldığı yerler
  أصل يدل على سكون (maqayis)؛ ركد الماء والريح ركودا أي سكن (ayn;mufradat)؛ ركد الماء ركودا سكن وكذلك الريح والسفينة (sihah)؛ الراكد هو الدائم الساكن الذي لا يجري (tahdhib)؛ ركد القوم ركودا سكنوا وهدءوا (maqayis;ayn;tahdhib)
- **B002** terazinin dengeye gelip yerleşik durması [kalıp] — terazinin dengeye gelip yerleşik durması
  ركد الميزان استوى (maqayis;sihah;tahdhib)؛ والميزان إذا استوى فقد ركد وهو راكد (ayn)
- **B003** dolu büyük yemek çanağı [kalıp] — dolu büyük yemek çanağı
  جفنة ركود مملوءة (maqayis;sihah)؛ الجفنة الركود المملوءة الثقيلة (ayn)؛ الجفنة الركود الثقيلة المملوءة (tahdhib)؛ جفنة ركود عبارة عن الامتلاء (mufradat)

## ظ ه ر (root_000970): 42:33 ظَهْرِهِۦٓ

- **B001** açığa çıkıp belirginleşmek — açığa çıkmak, belirip anlaşılır olmak · görünür ve dışta olan
  ظهر الشيء إذا انكشف وبرز (maqayis)؛ الظهور بدو الشيء الخفي (ayn;tahdhib)؛ ظهر الشيء ظهورا تبين (sihah)؛ أن يحصل شيء على ظهر الأرض فلا يخفى (mufradat)
- **B002** sırt ve arka yüz — sırt; karın ya da ön tarafın karşıtı olan arka yüz · sırtı güçlü kimse · sırtı ağrıyan veya incinmiş kimse · birinin sırtına vurmak veya zarar vermek · kolları arkada bağlayan veya yere düşüren tutuş
  ظهر الإنسان خلاف بطنه (maqayis)؛ الظهر خلاف البطن من كل شيء (ayn;sihah;tahdhib)؛ الظهر الجارحة وجمعه ظهور (mufradat)؛ رجل مظهر شديد الظهر ورجل ظهر يشتكي ظهره (maqayis;sihah;tahdhib;mufradat)
- **B003** yüksek ya da dışta kalan yüz — yerin yüksek veya açıkta kalan yüzü · dış ya da üst yüz; astarın karşıtı
  الظهر من الأرض ما غلط وارتفع (ayn;tahdhib)؛ الظاهرة كل أرض غليظة مشرفة (ayn)؛ الظواهر أشراف الأرض (sihah;tahdhib)؛ ظهر الأرض وبطنها (mufradat)؛ الظهارة خلاف البطانة (ayn;sihah;tahdhib)
- **B004** öğle vakti ve ona bağlı eylemler — öğle vakti ve o vakitte kılınan namaz · gün ortası veya öğle sıcağı · öğle vaktine girmek veya o sırada yol almak · hayvanların her gün öğleyin suya gelmesi
  وقت الظهر والظهيرة أظهر أوقات النهار (maqayis)؛ الظهر ساعة الزوال وصلاة الظهر والظهيرة حد انتصاف النهار (ayn;tahdhib)؛ الظهر بعد الزوال والظهيرة الهاجرة (sihah)؛ صلاة الظهر والظهيرة وقت الظهر وأظهر فلان حصل في ذلك الوقت (mufradat)؛ الظاهرة أن ترد كل يوم ظهرا (sihah;tahdhib)
- **B005** yük bineği ve yedek deve — yük taşıyan binek veya deve topluluğu · gerektiğinde kullanılmak üzere hazır tutulan deve
  الركاب الظهر لأن الذي يحمل منها الشيء ظهورها (maqayis)؛ الظهر الركاب تحمل الأثقال في السفر (ayn;tahdhib)؛ الظهر الركاب وبنو فلان مظهرون (sihah)؛ يعبر عن المركوب بالظهر وظهري معد للركوب (mufradat)؛ البعير الظهري العدة للحاجة (sihah;tahdhib)
- **B006** yardım edip güçlendirmek — yardımcı, destekçi · yardımlaşma ve destek olma · ondan yardım alıp güçlenmek
  الظهير المعين كأنه أسند ظهره إلى ظهرك (maqayis)؛ الظهير العون والمظاهر المعاون وهما يتظاهران أي يتعاونان (ayn)؛ الظهير المعين والمظاهرة المعاونة والتظاهر التعاون واستظهر به استعان به (sihah)؛ ظهير في معنى ظهراء أي أعوان وظاهروا أي عاونوا (tahdhib)؛ ظاهرته عاونته وما له منهم من ظهير أي معين (mufradat)
- **B007** üzerine çıkmak veya üstün gelmek [kalıp] — üstün gelmek veya üzerinde güç kurmak · damın veya yüzeyin üstüne çıkmak
  الظهور الغلبة (maqayis)؛ الظهور الظفر بالشيء (ayn;tahdhib)؛ ظهرت على الرجل غلبته وظهرت البيت علوته (sihah)؛ ظهر على الحائط وعلى السطح وظهر على الشيء إذا غلبه وعلاه (tahdhib)؛ ظهر عليه غلبه وليظهره على الدين كله (mufradat)
- **B008** bilgiye ulaşıp öğrenmek [kalıp] — bir şeyi öğrenmek veya bulup ortaya çıkarmak
  ظهرت على كذا إذا اطلعت عليه (maqayis)؛ والله أظهرنا عليه أي أطلعنا (ayn)؛ أظهرني الله على ما سرق مني أي أعثرني عليه وظهرت على الأمر (tahdhib)؛ فلا يظهر على غيبه أحدا أي لا يطلع عليه (mufradat)
- **B009** çıkık göz — çökük gözün karşıtı olan çıkık göz
  الظاهرة العين الجاحظة (maqayis)؛ الظاهرة العين الجاحظة وهي خلاف الغائرة (ayn)؛ الظاهرة من العيون الجاحظة (sihah)؛ العين الظاهرة التي ملأت نقرة العين وهي خلاف الغائرة (tahdhib)
- **B010** eşe yönelik benzetmeli yasaklama sözü — kocanın eşini kendisine yasak saydığını bildiren geleneksel söz · eşini annesinin sırtına benzeterek kendisine yasak sayma sözü
  الظهار قول الرجل لامرأته أنت علي كظهر أمي (maqayis;sihah;mufradat)؛ مظاهرة الرجل امرأته إذا قال هي علي كظهر أمي أو كظهر ذات رحم محرم (ayn)؛ وأوجبت الكفارة على من ظاهر من امرأته (tahdhib)
- **B011** kanadın dış tüyleri — kanadın dıştan görünen tüyleri veya tüy sapının sırt yönündeki parçası
  الظهار من الريش ما يظهر منه في الجناح (maqayis)؛ الظهار من الريش الذي يظهر من ريش الطائر وهو في الجناح (ayn;tahdhib)؛ الظهار ما جعل من ظهر عسيب الريشة والظهران الجانب القصير من الريش (sihah;tahdhib)
- **B012** geriye atıp önemsememek — arkaya atılıp unutulan şey · bir isteği önemsemeyip geriye atmak
  الظهري كل شيء تجعله بظهر أي تنساه (maqayis)؛ الظهري الشيء تنساه وتغفل عنه (ayn;tahdhib)؛ لا تجعل حاجتي بظهر أي لا تنسها (sihah)؛ ظهرت بكذا أي خلفته ولم ألتفت إليه (mufradat)
- **B013** ayıbı kişiden uzak olmak [kalıp] — ayıbı sana yapışmayan, senden uzak söz veya durum
  أمر ظاهر عنك عاره أي زائل (maqayis;sihah)؛ ظهر عني هذا العيب أي نبا عني ولم يعلق بي (tahdhib)؛ تلك شكاة ظاهر عنك عارها (maqayis;sihah;tahdhib)
- **B014** ev eşyası ve yedek mallar — ev eşyası ve gerektiğinde yararlanılan mallar
  الظهرة متاع البيت وأحسب هذه مستعارة من الظهر أيضا لأن الإنسان يستظهر بها (maqayis)؛ الظهرة بالتحريك متاع البيت (sihah)؛ الظهرة ما في البيت من المتاع والثياب (tahdhib)
- **B015** kara yolu ve dıştaki yüksek kesim — deniz yolunun karşıtı olan kara yolu · Mekke'nin dış veya yüksek kesimlerinde yaşayan Kureyşliler
  طريق الظهر (ayn;sihah;tahdhib)؛ سلكنا الظهر يريدون طريق البر (maqayis)؛ قريش الظواهر سموا بذلك لأنهم ينزلون ظاهر مكة (maqayis;sihah;tahdhib)؛ ظاهرة الجبل أعلاه وظاهرة كل شيء أعلاه (tahdhib)
- **B016** güç alınan destekçi topluluğu — kişinin güç aldığı yardımcıları ve yakın topluluğu
  جاء فلان في ظهرته وناهضته أي قومه (maqayis;sihah)؛ الظهرة ظهر الرجل وأنصاره (tahdhib)؛ الظهراء أعوان النبي (tahdhib)
- **B017** topluluk veya zaman sınırları arasında [kalıp] — aralarında, topluluğun ortasında · iki gün veya iki zaman sınırı arasında
  أنا بين ظهرانيهم وظهريهم (ayn)؛ نازل بين ظهريهم وظهرانيهم (sihah)؛ نزل فلان بين ظهرينا وظهرانينا وأظهرنا (tahdhib)؛ بين الظهرانين معناه في اليومين أو في الأيام (sihah;tahdhib)
- **B018** bir konuyu her yönüyle incelemek [kalıp] — bir konuyu evirip çevirerek her yönüyle incelemek
  قلبت الأمر ظهرا لبطن (ayn;tahdhib)
- **B019** ezberleyip bellekten söylemek — kitaba bakmadan, ezberden · ezberlemek ve kitaba bakmadan okumak
  تكلمت بذلك عن ظهر غيب (ayn;tahdhib)؛ ظهر القلب حفظ من غير كتاب (ayn;tahdhib)؛ استظهر الشيء أي حفظه وقرأه ظاهرا (sihah)؛ حمل القرآن على ظهر لسانه (tahdhib)
- **B020** iki katmanı üst üste getirmek [kalıp] — iki giysiyi veya iki zırhı üst üste getirmek
  ظاهر بين ثوبين أي طارق بينهما وطابق (sihah)؛ ظاهر فلان بين ثوبين وبين درعين إذا طابق بينهما (tahdhib)
- **B021** yedek hazırlayıp güvence sağlamak — gerektiğinde kullanılmak üzere hazır tutulan deve · yedek hazırlayarak önlem almak ve güvence sağlamak
  البعير الظهري العدة للحاجة (sihah;tahdhib)؛ الاستظهار في كلامهم الاحتياط والاستيثاق (tahdhib)؛ استظهر ببعيرين ظهريين محتاطا بهما (tahdhib)
- **B022** birbirine sırt çevirip uzaklaşmak — birbirine sırt çevirip uzaklaşmak
  تظاهر القوم إذا تدابروا (maqayis;sihah)؛ كل واحد منهما أدبر عن صاحبه وجعل ظهره إليه (maqayis)
- **B023** karşılıksız veya artandan vermek [kalıp] — karşılık beklemeden, kendiliğinden vermek · geçim gereklerinden artan bolluktan vermek
  عن ظهر يد معناه ابتداء من غير مكافأة (tahdhib)؛ ما كان عن ظهر غنى عن فضل عيال (tahdhib)
- **B024** bir şeyle övünmek [kalıp] — bir şeyle övünmek ve onu övünç dayanağı yapmak
  ظهرت به أي افتخرت به (tahdhib)؛ واظهر ببزته أي افخر به على غيره (tahdhib)

## ص ب ر (root_000840): 42:33 صَبَّارٍ, 42:43 صَبَرَ

- **B001** kendini tutarak dayanma — kendini tutarak dayanma · kendimi o işte tuttum · kendini zorlayarak dayanma · çaba göstererek dayan · dayanma gücü yüksek kişi · her defasında çabayla dayanan kişi
  الصبر نقيض الجزع (ayn;jamhara;tahdhib)؛ الصبر حبس النفس عن الجزع (sihah)؛ صبرت نفسي أي حبستها (maqayis;tahdhib)؛ حبس النفس على ما يقتضيه العقل والشرع (mufradat)
- **B002** zorla alıkoyma — onu zorla alıkoydu · öldürülmek üzere bağlı tutma · ölümü beklemek üzere alıkonmuş canlı · yetkili önünde zorla ettirilen ant · ona bütün gücüyle ant içirdi
  المصبورة المحبوسة على الموت (maqayis;sihah)؛ الصبر نصب الإنسان للقتل (ayn;tahdhib)؛ صبرت يمينه أي حلفته (ayn;maqayis;tahdhib)؛ قتل صبر ويمين صبر (sihah;tahdhib)؛ الصبر الإكراه (tahdhib)
- **B003** yükümlülüğe güvence veren kişi — yükümlülüğe güvence veren kişi · onun yükümlülüğüne güvence verdim · bana bir güvence veren kişi bul · topluluğun işlerinde yanında duran kişi
  الصبير هو الكفيل (maqayis;sihah)؛ صبرت بفلان إذا كفلت به فأنا به صبير (tahdhib)؛ صبير القوم الذي يصبر لهم ويكون معهم في أمورهم (ayn)
- **B004** üst ya da yan sınır — şeyin üstü ya da yanı · kabın çevre yanları · mezarın çevre yanları · üst ya da yan sınırına kadar · bahçenin en üst bölümü
  صبر كل شيء أعلاه (maqayis;ayn;tahdhib)؛ أصبار الإناء نواحيه (maqayis;ayn;sihah)؛ أصبار القبر نواحيه (ayn;tahdhib)؛ الصبر جانب الشيء (tahdhib)
- **B005** sert taş ve taşlı arazi — sert ve kalın taş · sert ve düz taşlar · taşlar ya da kaba yüksekçe arazi · çok engebeli olmayan çakıllı yer · katı kaya yüzeyi ya da taşlık alan
  الصبرة من الحجارة ما اشتد وغلظ (maqayis;ayn;tahdhib)؛ الصبارة الحجارة (sihah;tahdhib)؛ الصبر الأرض التي فيها حصباء (maqayis;sihah;tahdhib)؛ أم صبار الحرة أو الصفاة (maqayis;sihah;tahdhib)
- **B006** çıkışsız ağır durum — savaş ya da ağır yıkım · çıkış yolu olmayan büyük sıkıntı
  وقع القوم في أم صبور إذا وقعوا في أمر عظيم (maqayis)؛ أم صبار الحرب والداهية الشديدة (ayn)؛ وقع القوم في أم صبور أي في أمر شديد (sihah)؛ أم صبور أمر لا منفذ له عنه (tahdhib)
- **B007** kışın ayazı — kışın şiddetli soğuğu
  صبارة الشتاء شدة برده (sihah)؛ أتيته في صبارة الشتاء أي في شدة البرد (tahdhib)
- **B008** acı ağaç özü — acı ağaç özü ve bundan yapılan ilaç
  الصبر بكسر الباء عصارة شجرة (ayn;tahdhib)؛ الصبر هذا الدواء المر (sihah)
- **B009** demirhindi meyvesi — demirhindi meyvesi
  الصبار حمل شجرة طعمه أشد حموضة من المصل (ayn;tahdhib)؛ الصبار التمر الهندي (tahdhib)
- **B010** katmanlı beyaz bulut — üst üste yığılmış beyaz bulut · yoğun bulutun üstündeki düz bulut · beyaz bulutlar
  الصبر سحاب مستو فوق السحاب الكثيف (ayn)؛ الصبير السحاب الأبيض (sihah;tahdhib)؛ السحاب الأبيض الذي يصبر بعضه فوق بعض درجا (sihah;tahdhib)؛ الاصبار السحائب البيض (sihah)
- **B011** sofra yaygısı ya da yiyecek yığını — yiyeceğin altına serilen geniş ince yaygı · üst üste konmuş yiyecek yığını · malı tartmadan ya da ölçmeden topluca aldım · düğün yemeğinin üstüne konduğu ince yaygı
  صبير الخوان رقاقته العريضة تبسط تحت ما يؤكل من الطعام (ayn;tahdhib)؛ الصبرة من الطعام بعضه فوق بعض (ayn;tahdhib)؛ اشتريت الشيء صبرة أي بلا وزن ولا كيل (sihah)
- **B012** öldürmeye karşılık ölüm cezası — öldürmeye karşılık ölüm cezası istesin · yetkili onu önceki öldürmeye karşılık öldürdü
  فليصطبر معناه فليقتص (tahdhib)؛ أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود (tahdhib)
- **B013** ateşe götüren işlerde pervasızlık — ateşi hak edecek işleri yapmaya ne kadar da gözü pekler
  الصبر الجرأة ومنه فما أصبرهم على النار (tahdhib)؛ لغة بمعنى الجرأة (mufradat)؛ ما أعملهم بعمل أهل النار (mufradat)
- **B014** kendini tutarak bekleme — kendini tutarak bekleme · yöneticinin hükmünün gerçekleşmesini bekle
  يعبر عن الانتظار بالصبر لما كان حق الانتظار أن لا ينفك عن الصبر (mufradat)؛ فاصبر لحكم ربك أي انتظر حكمه (mufradat)
- **B015** kendini tutma türü olarak oruç — oruç, kendini tutmanın bir türüdür · oruç ayı
  سمي الصوم صبرا لكونه كالنوع له (mufradat)؛ صيام شهر الصبر (mufradat)
- **B016** bir Arap boyunun adı — belirli bir Arap topluluğuna bağlı boyun adı
  الصبر أيضا بطن من غسان (sihah)
- **B017** dağ ya da dağların orta kesimi — dağ · dağların orta kesimi
  الصبير الأقدر وهو الوسط من الجبال (tahdhib)؛ الصبير الجبل (tahdhib)
- **B018** şişe tıkacı ve tıkama — şişe tıkacı ya da kapakçığı · kabın ağzını tıkaçla kapattı
  أصبر سد رأس الحوجلة بالصبار وهو السداد (tahdhib)؛ الصبار صمام القارورة (tahdhib)

## و ب ق (root_001618): 42:34 يُوبِقْهُنَّ

- **B001** iki şey arasındaki ayırıcı engel — 
  لكل شيء حال بين شيئين موبق (maqayis)؛ موبقا أي حاجزا، وكل حاجز بين شيئين فهو موبق (tahdhib)
- **B002** yok olmak ya da yok etmek — ölüp yok olmak · yok etmek · yok etme · yok olmuş ya da yok oluşa düşmüş · yok edilmiş ya da yok oluşa uğramış
  وبق: هلك، وأوبقه الله (maqayis)؛ وبق الإنسان إذا هلك وبقا وأوبقته أنا إيباقا (jamhara)؛ وبق يبق وبوقا: هلك، وأوبقه أي أهلكه (sihah)؛ أوبقت فلانا ذنوبه أي أهلكته فوبق يوبق وبقا وموبقا إذا هلك (tahdhib)؛ وبق إذا تثبط فهلك، وأوبقه كذا (mufradat)
- **B003** takılıp kurtulamamak; kimi kullanımlarda bu yüzden yok olmak veya başkasını alıkoyup yok oluşa sürüklemek — takılıp kurtulamayarak yok olmak · hayvanların çamura saplanıp kalması · işlediği kötülüğe saplanıp ondan kurtulamamak · yaptıkları yüzünden onları alıkoyup boğularak ölmelerine yol açmak
  وبقت الإبل في الطين إذا وحلت فنشبت فيه، ووبق في ذنبه إذا نشب فيه فلم يتخلص منه (tahdhib)؛ يوبقهن أي يحبسهن فيهلكوا غرقا (tahdhib)؛ وبق إذا تثبط فهلك (mufradat)
- **B004** kararlaştırılmış buluşma zamanı veya yeri — 
  الموبق: الموعد (maqayis)؛ الموبق: الموعد، يعني بموعد (tahdhib)

## ج د ل (root_000229): 42:35 يُجَٰدِلُونَ

- **B001** sıkıca bükme ve sağlam örgü — sıkı ve sağlam büküm · halatı sıkıca bükmek · bükülmüş yular ya da kuşak · halkaları sıkıca örülmüş zırh · demirin kenarlarını döverek yuvarlatmak · kuş düzeneğinde kullanılan bükülü bağ
  استحكام الشيء (maqayis)؛ جديل الناقة زمامها إذا كان مجدول الفتل (ayn)؛ جدلت الحَبْل أي فتلته فتلا محكما (sihah)؛ الجدل شدة الفتل (tahdhib)؛ جدلت الحَبْل أي أحكمت فتله ومنه الجديل ودرع مجدولة (mufradat)
- **B002** çekişmeli sözlü tartışma — şiddetli ve uzayan sözlü çekişme · üstün gelme amaçlı tartışma · sözle çekişmek · karşılıklı sözlü çekişme · çok çekişen kimse · tartışmada karşısındakini yenmek
  امتداد الخصومة ومراجعة الكلام (maqayis)؛ رجل جدل مجدال أي خصم مخصام والفعل جادل يجادل مجادلة (ayn)؛ جادله أي خاصمه مجادلة وجدالا والاسم الجدل وهو شدة الخصومة (sihah)؛ إنه لجدل إذا كان شديد الخصام وقد جادل فلانا جدالا ومجادلة (tahdhib)؛ الجدال المفاوضة على سبيل المنازعة والمغالبة (mufradat)
- **B003** yere atma ve yere serilme — birini yere atıp sermek · yere düşüp serilmek · yere atılmış veya yere düşmüş
  طعنه فجدله أي رماه بالأرض (maqayis)؛ جدلته تجديلا أي صرعته (ayn)؛ طعنه فجدله أي رماه بالأرض فانجدل أي سقط (sihah)؛ جدلته فانجدل صريعا وهو مجدول (tahdhib)؛ الصراع وإسقاط الإنسان صاحبه على الجدالة (mufradat)
- **B004** sert zemin — sert yer veya sert zemin
  الجدالة وهي الأرض وهي صلبة (maqayis)؛ الجدالة الأرض (sihah)؛ الجدالة اسم للأرض (tahdhib)؛ الجدالة وهي الأرض الصلبة (mufradat)
- **B005** küçük akarsu veya su kolu — küçük akarsu veya küçük su kanalı · büyük bir akarsudan ayrılan küçük kol
  الجدول نهر صغير وهو ممتد وماؤه أقوى في اجتماع أجزائه (maqayis)؛ الجديل نهر يأخذ من دجلة والجدول نهر الحوض ونحوه من الأنهار الصغار (ayn)؛ الجدول النهر الصغير (sihah)؛ الجدول نهر الحوض ونحو ذلك من الأنهار الصغار (tahdhib)
- **B006** uzun uzuvlar ve ince, sıkı beden yapısı — bir uzuv veya uzun uzuv kemiği · uzuvlar veya kol ve bacakların uzun kemikleri · zayıflıktan kaynaklanmayan ince kemikli beden · düzgün ve sıkı beden yapısı
  رجل مجدول إذا كان قضيف الخلقة من غير هزال والجدول الأعضاء واحدها جدل (maqayis)؛ جدول الإنسان قصب اليدين والرجلين وإنسان مجدول الخلق أي لطيف القصب (ayn)؛ جارية مجدولة الخلق والمجدول القضيف لا من هزال (sihah)؛ حسن الجدل إذا كان حسن أسر الخلق وجدول الإنسان قصب اليدين والرجلين ورجل مجدول الخلق لطيف القصب (tahdhib)
- **B007** gelişimde güçlenme veya sağlam yapılı olma — güçlenip serpilmiş oğlan · başaktaki tanenin güçlenmesi · rasih aşamasını geçip annesiyle yürüme eşiğinin üstüne çıkmış genç deve · yeşillenip yuvarlaklaşmış, henüz tam sertleşmemiş hurma · güçlü ve sağlam yapılı avcı kuş · sağlam yapılı avcı kuş
  غلام جادل إذا اشتد وجدل الحب في سنبله قوي والأجدل الصقر سمي بذلك لقوته (maqayis)؛ الأجدل من صفة الصقر (ayn)؛ الجادل من ولد الناقة فوق الراشح وهو الذي قوي ومشى مع أمه والجدال البلح إذا اخضر واستدار قبل أن يشتد (sihah)؛ إذا قوي الفصيل ومشى فهو راشح فإذا ارتفع عن الراشح فهو جادل والأجادل الصقور (tahdhib)؛ الأجدل الصقر المحكم البنية (mufradat)
- **B008** yan, tutulan yol, ilk durum veya kabile — yan, tutulan yol veya ilk durum · kabile veya ona bağlı topluluk · bir kabileye mensup · kendi yönünde veya önceki durumunda · kabileye mensup kişi · saçma ve değersiz görüş
  جديلة قبيلة (ayn)؛ الجديلة الشاكلة والجديلة القبيلة والناحية (sihah)؛ القوم على جديلة أمرهم أي على حالهم الأول وفلان على جديلته كقولك على ناحيته وجديلة طيئ قبيلة (tahdhib)
- **B009** sağlam yüksek yapı ve yapıyı pekiştirme — yüksek saray veya sağlam yapı · yüksek ve sağlam saraylar · yapıyı sağlamlaştırmak
  المجدل القصر وهو قياس الباب (maqayis)؛ المجدل القصر المنيف ويجمع مجادل (ayn)؛ المجدل القصر (sihah)؛ المجدل القصر المشرف وجمعه مجادل (tahdhib)؛ جدلت البناء أحكمته والمجدل القصر المحكم البناء (mufradat)

## ح ي ص (root_000378): 42:35 مَّحِيصٍ

- **B001** bir şeyden sapıp başka yöne dönme — bir şeyden ya da doğrudan sapmak, başka yöne dönmek · sapma, kaçamaklı yön değiştirme ve geri kalma · uzaklaşılacak yön, çıkış ya da kaçış yolu · amaçlanan yönden sapma · sapma ve başka yöne dönme · yön değiştirme ve sapma · bir şeyden sapma ve uzaklaşma
  الحاء والياء والصاد أصل واحد وهو الميل في جور وتلدد (maqayis)؛ حاص عن الحق يحيص حيصا إذا جار (maqayis)؛ الحيص الحيد عن الشيء والمحيص المحيد (ayn)؛ حاص عنه يحيص حيصا وحيوصا ومحيصا ومحاصا وحيصانا أي عدل وحاد (sihah)؛ ما عنه محيص أي محيد ومهرب (sihah)؛ الحيص الرواغ والتخلف (sihah)؛ حاص عن الحق يحيص أي حاد عنه إلى شدة ومكروه (mufradat)
- **B002** ağır bir sıkıntıya düşme — darlık, sıkışıklık · içinden çıkılamayan karışık ve sıkıntılı durum
  وقعوا في حيص بيص أي شدة (maqayis)؛ حيص بيص يتكلم به عند اختلاط الأمر أي فيما لا أقدر على الخروج منه أي في ضيق وأصل الحيص الضيق (ayn)؛ وقع في حيص بيص إذا وقع في أمر لا يتخلص منه (jamhara)؛ وقعوا في حيص بيص أي في اختلاط من أمرهم لا مخرج لهم منه ويقال في ضيق وشدة (sihah)؛ أصله من حيص بيص أي شدة (mufradat)

## م ت ع (root_001395): 42:36 فَمَتَٰعُ

- **B001** yararlanma, haz alma ve yarar sağlayan şey — bir şeyden yararlanıp haz almak · yararlanılan ve haz alınan şey · yarar sağlayan ve kullanılan şey
  أصل صحيح يدل على منفعة وامتداد مدة في خير؛ المتعة والمتاع المنفعة (maqayis)؛ المتعة ما تمتعت به (jamhara)؛ المتاع أيضا المنفعة وما تمتعت به، وتمتعت بكذا واستمتعت به بمعنى (sihah)؛ كل شيء ينتفع به ويتبلغ به ويتزود (tahdhib)؛ كل ما ينتفع به على وجه ما فهو متاع ومتعة (mufradat)
- **B002** uzama, yükselme ve kimi bağlamlarda doruğa ulaşma — günün uzayıp yükselmesi ve öğle öncesinde doruğa yaklaşması · kuşluk vaktinin en yüksek düzeyine ulaşması · serabın günün başında uzayıp yükselmesi · bitkinin ilk büyümesinde boy atması · uzama ve yükselme
  متع النهار طال؛ متع النبات؛ متع السراب طال في أول النهار (maqayis)؛ متع النهار متوعا وذلك قبل الزوال، ومتع الضحى إذا بلغ غايته (ayn)؛ متع النهار إذا ارتفع، ومتع السراب إذا ارتفع في أول النهار (jamhara)؛ متع النهار أي ارتفع وطال (sihah)؛ متع النهار متوعا إذا ارتفع حتى بلغ غاية ارتفاعه قبل أن يزول (tahdhib)؛ المتوع الامتداد والارتفاع (mufradat)
- **B003** işe yarayan eşya, mal ve azık — gereksinimlerde kullanılan eşya veya mal · evde gereksinimler için kullanılan eşyalar · az miktardaki azıklar
  المتاع من أمتعة البيت ما يستمتع به الإنسان في حوائجه (maqayis)؛ المتاع السلعة (sihah)؛ كل شيء ينتفع به ويتبلغ به ويتزود، الزاد القليل (tahdhib)؛ لما فتحوا متاعهم أي طعامهم، وقيل وعاءهم (mufradat)
- **B004** boşanan kadına verilen yararlanma desteği [kalıp] — boşanan kadına yararlanması için verilen mal veya destek · boşanma nedeniyle verilen yararlanma desteği
  متعت المطلقة بالشيء لأنها تنتفع به (maqayis)؛ متعة الطلاق لأنه انتفاع (sihah)؛ متعة ومتاعا، بما ينفعها به من ثوب أو خادم أو دراهم أو طعام (tahdhib)؛ المتاع والمتعة ما يعطى المطلقة لتنتفع به مدة عدتها (mufradat)
- **B005** evlilik ilişkisinden yararlanma ve süreli evlilik anlaşması — evlilik bağının kurulması veya eşlerin birleşmesi · belirli para ve süreye bağlı evlilik · belirli bir süre şartına bağlanan evlilik
  نكاح المتعة التي كرهت أحسبها من هذا (maqayis)؛ نكاح المتعة الذي ذكر أحسبه من هذا (jamhara)؛ منه متعة النكاح لأنه انتفاع (sihah)؛ فما استمتعتم به منهن على عقد التزويج؛ المتعة الشرطية (tahdhib)؛ متعة النكاح هي أن الرجل كان يشارط المرأة بمال معلوم إلى أجل معلوم (mufradat)
- **B006** iki kutsal ziyareti birleştirip arada serbest kalma — iki kutsal ziyareti birleştirip arada yasaklardan çıkma · küçük kutsal ziyareti yapıp büyük ziyarete kadar serbest kalma
  متعة الحج لأنه انتفاع (sihah)؛ سمي متمتعا بالعمرة إلى الحج لأنه حل له كل شيء كان حرم عليه في إحرامه (tahdhib)؛ متعة الحج ضم العمرة إليه (mufradat)
- **B007** yaşatıp yararlanacağı süre verme — Tanrı'nın birini yaşatıp yararlanmasını sağlaması · belirli bir sona kadar sağlık içinde yaşatmak
  متع الله به فلانا تمتيعا وأمتعه به إمتاعا أي أبقاه ليستمتع به (maqayis)؛ أمتعه الله بكذا ومتعه بمعنى (sihah)؛ يمتعكم متاعا حسنا إلى أجل مسمى أي يبقيكم بقاء في عافية، ومتع الله فلانا وأمتعه إذا أبقاه وأنسأه (tahdhib)؛ متعناهم إلى حين، نمتعهم قليلا، فأمتعه قليلا (mufradat)
- **B008** alanında üstün, güçlü veya fazla — alanında üstün, güçlü veya fazla · uzun, iyi bükülmüş ve sağlam ip · koyu kızıl veya çok nitelikli mayalı içki · niteliğiyle haz veren ve kızıl olabilen içki · güçlü deve · ağır basan ve fazlalık gösteren tartı
  حبل ماتع جيد، ماتع راجح زائد، وشراب ماتع أحمر (maqayis)؛ الماتع الطويل من كل شيء، حبل ماتع جيد الفتل، نبيذ ماتع شديد الحمرة، وكل شيء جيد فهو ماتع (sihah)؛ الماتع من كل شيء البالغ في الجودة الغاية في بابه، نبيذ ماتع إذا كان أحمر (tahdhib)؛ شراب ماتع قيل أحمر وإنما هو الذي يمتع بجودته، وجمل ماتع قوي، ماتع أي راجح زائد (mufradat)
- **B009** bir şeyi alıp gitme veya birine gerek duymama — bir şeyi alıp onunla gitmek · birine gerek duymamak
  وقد متع به يمتع متعا، لئن اشتريت هذا الغلام لتمتعن منه بغلام صالح أي لتذهبن به، أمتعت عن فلان أي استغنيت عنه (sihah)؛ متعت بالشيء ذهبت به، لتمتعن منه بغلام صالح أي لتذهبن، أمتعت عن فلان أي استغنيت عنه (tahdhib)

## ح ي و (root_005544): documented alternative for 42:36 ٱلْحَيَوٰةِ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

- **B001** yaşam ve canlı olma — 
  الحيوة كتبت بالواو؛ يقال حيي يحيا فهو حي؛ ولغة أخرى حي يحي والجميع حيوا (ayn)
- **B002** canlı varlık — 
  والحيوان كل ذي روح الواحد والجميع فيه سواء (ayn)
- **B003** cennette, değdiği her şeyi Tanrı'nın izniyle canlandıran su — 
  والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله (ayn)
- **B004** yılan adının yaşam kökenli çözümlemesi — 
  والحَيَّة اشتقاقها من الحياة؛ هي في أصل البناء حيوة؛ ومن قال لصاحب الحَيّات حاي فهو فاعل من هذا البناء؛ ومن قال حواء على فعال فإنه يقول اشتقاق الحَيَّة من حَوَيْت لأنها تتحوى في التوائها (ayn)
- **B005** toprağı canlandıran bahar yağmuru — 
  والحَيَا مقصور حَيَا الربيع وهو ما تحيا به الأرض من الغيث (ayn)

## خ ي ر (root_000452): 42:36 خَيْرٌ

- **B001** arzulanan iyilik — iyilik; yarar veya üstünlük taşıyan olumlu şey
  فالخير خلاف الشر لأن كل أحد يميل إليه (maqayis)؛ الخير ضد الشر (jamhara;sihah)؛ الخير ما يرغب فيه الكل وضده الشر (mufradat)؛ يقابل به الشر مرة والضر مرة (mufradat)
- **B002** iyi ve seçkin olma — iyi ve üstün nitelikli · üstün, güzel veya seçkin olan · üstün veya seçkin kimse ya da şey · iyi ve erdemli kişiler · üstün, güzel veya seçilmiş olanlar
  رجل خير وامرأة خيرة فاضلة وقوم خيار وأخيار في صلاحها وامرأة خيرة في جمالها وميسمها (maqayis;ayn)؛ رجل خير إذا كان فيه خير ورجل خيار من قوم خيار وأخيار والأخيار خلاف الأشرار (jamhara)؛ الخيرات جمع خيرة وهي الفاضلة من كل شيء (sihah)؛ فيهن مختارات لا رذل فيهن والخير الفاضل المختص بالخير (mufradat)
- **B003** daha iyi olanı seçme — seçim veya seçim hakkı · seçim, seçilmiş şey veya seçim sonucu · daha iyi olanı arayıp seçme · seçmek veya üstün tutmak · Yaratıcıdan kişi için iyi sonucu dilemek · Yaratıcının kişi için iyi olanı seçip vermesi · iki şey arasında seçim hakkını ona bırakmak · seçimde üstün gelmek veya diğerini geçmek · seçen ya da seçilmiş olan
  الخيرة الخيار والاستخارة أن تسأل خير الأمرين لك ويقال خايرت فلانا فخرته وتقول اختر (maqayis)؛ خايرت فلانا فخرته والله يخير للعبد إذا استخاره وهذا وهذه وهؤلاء خيرتي وهو ما تختاره (ayn)؛ الخيار الاسم من الاختيار والخيرة من قولك خار الله لك والاختيار الاصطفياء والاستخارة الخيرة وخيرته بين الشيئين (sihah)؛ الاختيار طلب ما هو خير وفعله واستخار الله العبد فخار له وخايرت فلانا كذا فخرته (mufradat)
- **B004** mal, özellikle çok veya övülen bir yoldan edinilmiş servet — mal, özellikle çok veya iyi yoldan edinilmiş servet
  إن ترك خيرا أي مالا (sihah;mufradat)؛ لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب (mufradat)؛ وإنه لحب الخير لشديد أي المال الكثير (mufradat)؛ ما كان مجموعا من المال من وجه محمود (mufradat)
- **B005** cömertlik ve armağan verme — cömertlik, armağan ve verme
  والخير الكرم (maqayis)؛ الخير الهبة (ayn)؛ رجل ذو خير إذا كان كثير الخير (jamhara)؛ الخير بالكسر الكرم (sihah)
- **B006** bir geçidi tıkayıp hayvanı yuvasından çıkarma [kalıp] — sırtlanı, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma · çöl sıçanını, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma
  استخاره الضبع وهو أن تجعل خشبة في ثقبة بيتها حتى تخرج من مكان إلى آخر (maqayis)؛ يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء (ayn)

## ب ق ي (root_000142): 42:36 وَأَبْقَىٰ

- **B001** varlığını sürdürme ve yok olmama — varlığını sürdürdü, yok olmadı · sürdü, kalıcı oldu · varlığını sürdürme, yok olmama · varlığını sürdüren, yok olmayan · kalmasını sağladı veya ömrünü uzattı · daha kalıcı, daha uzun süreli · karşılığı kalıcı olan iyi işler veya ibadetler · kalma, geride kalan kişi veya topluluk
  أصل واحد وهو الدوام (maqayis)؛ بقي الشيء يبقى بقاء وهو ضد الفناء (maqayis;ayn;tahdhib)؛ بقى الشيء يبقى بقاء وبقي الرجل زمانا طويلا أي عاش (sihah)؛ البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء (mufradat)؛ الباقيات الصالحات هي الصلوات الخمس وقيل الأعمال الصالحة كلها (tahdhib;mufradat)
- **B002** bir şeyden geriye kalan bölüm — bir şeyden geriye kalan, artık · geriye kalan bölüm · gelir veya vergiden kalan tutar · kendilerinde iyilik ve sağlamlık kalmış kimseler · Tanrı'nın size helal olarak bıraktığı şey; ayrıca Tanrı'yı gözetme
  نشدتك الله والبقيا وهي البقية (maqayis;ayn;tahdhib)؛ بقي من الشيء بقية والباقية توضع موضع المصدر (sihah)؛ الباقي حاصل الخراج ونحوه (tahdhib)؛ بقيت الله أي ما أبقى لكم من الحلال (tahdhib)؛ أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير (tahdhib)؛ فهل ترى لهم من باقية أي جماعة باقية أو فعلة لهم باقية وقيل معناه بقية (mufradat)
- **B003** bağışlayıp sağ bırakma — Tanrı aşkına bize acıyın ve bizi sağ bırakın · acıma ve sağ bırakma · ona acıdı ve onu sağ bıraktı · onu bağışlayıp sağ bıraktı veya sevgisini korudu · bizi yok etmeyin, sağ bırakın
  استبقيت فلانا أن تعفو عن زلله فتستبقي مودته (maqayis)؛ استبقيت فلانا إذا أوجبت عليه قتلا وعفوت عنه واستبقيت مودته (ayn;tahdhib)؛ أبقيت على فلان إذا أرعيت عليه ورحمته واستبقاه استحياه (sihah)؛ العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا (tahdhib)
- **B004** bir bölümünü ayırıp elde tutma — bir bölümünü ayırıp elde tuttum · koşu gücünün bir bölümünü sonraya saklayan atlar
  إذا أعطيت شيئا وحبست بعضه قلت استبقيت بعضه (ayn;tahdhib)؛ استبقيت من الشيء أي تركت بعضه (sihah)؛ المبقيات من الخيل التي تبقي بعض جريها تدخره (tahdhib)
- **B005** gözetleyerek bekleme — onu gözetip bekledim · onu gözleriyle izleyip gözetliyor · geceyi şimşeğin nerede parlayacağını gözleyerek geçirdi · ibadet çağrısını benim için gözet · Tanrı'nın elçisini uzun süre bekleyip gözledik · ona bakıp onu gözetledi · ona bakıp onu gözetledi · ona bakıp onu gözetledi
  يبقى الشيء ببصره إذا كان ينظر إليه ويرصده (maqayis;ayn)؛ بات فلان يبقي البرق أي ينظر إليه من أين يلمع (maqayis;ayn)؛ بقيت فلانا أبقيه إذا رعيته وانتظرته (maqayis)؛ بقيته أبقيه أي نظرت إليه وترقبته وبقينا رسول الله أي انتظرناه (sihah)؛ بقينا رسول الله أي انتظرناه وترصدنا له مدة كثيرة (mufradat)

## ج ن ب (root_000262): 42:37 يَجْتَنِبُونَ

- **B001** bedenin veya şeyin yanı ve bitişik çevresi — insanın veya hayvanın böğrü · yan, taraf · evin önü veya topluluğun yerleşimine bitişik çevre · vadinin, ordunun veya ırmağın iki yanı · devenin böğür derisinden alınan parça · ordunun sağ ve sol kanadı
  أصل الجنب الجارحة وجمعه جنوب (mufradat)؛ الجنب للإنسان وغيره (maqayis)؛ الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء (ayn)؛ الجنب معروف والجانب الناحية (sihah)؛ جنبتا الوادي ناحيتاه وجناب القوم ما حولهم (tahdhib)؛ جنب الإنسان والدابة معروف وأعطني جنبة جلد جنب بعير (jamhara)
- **B002** yanında yakın bulunma ve eşlik etme — yaklaşması ve ilişki kurması kolay · yol arkadaşı veya yakın eşlikçi · Tanrı'ya yakınlıkta veya Tanrı'nın buyruğu ve yolu üzerinde · kardeşin hakkında, özellikle onu çekiştirme konusunda
  رجل لين الجانب والجنب أي سهل القرب (ayn;tahdhib)؛ الصاحب بالجنب صاحبك في السفر (sihah)؛ الجنب القرب وفي قرب الله وجواره (tahdhib)؛ في أمره وحده الذي حده لنا (mufradat)
- **B003** uzak durma veya uzaklaştırma — uzak durmak, sakınmak veya bırakmak · birini bir şeyden uzaklaştırmak veya kötülükten korumak · beni ve çocuklarımı putlara tapmaktan uzak tut · insanlardan ayrı bir yerde durma · akrabalıkta, soyda veya yerleşimde uzak olan yabancı · başka bir topluluktan gelip akrabalığı bulunmayan komşu · uzaktan ve yabancı olarak · birini iyilikten yoksun bırakmak
  الأصل الآخر البعد والجنابة (maqayis)؛ جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها (ayn)؛ الجناب مصدر جانبته مجانبة وهو من المباعدة (jamhara)؛ جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه (sihah)؛ أجنب تباعد والجنابة ضد القرابة (tahdhib)؛ جنبته عن كذا أي أبعدته واجتنبوا عبارة عن تركهم إياه (mufradat)
- **B004** cinsel ilişki sonrası arınma gerektiren dinsel durum — cinsel ilişkiden sonra arınana dek dinsel kısıt altında bulunan kişi · cinsel ilişki sonrası arınma gerektiren duruma girmek
  الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد (maqayis)؛ أجنب الرجل إذا أصابته الجنابة (ayn;jamhara;sihah;tahdhib)؛ رجل جنب وامرأة جنب وقوم جنب (jamhara;sihah;tahdhib)؛ سميت الجنابة بذلك لكونها سببا لتجنب الصلاة في حكم الشرع (mufradat)
- **B005** yanında yönlendirerek götürme — hayvanı veya atı yanında yürütmek · tutsağı yürütmek veya hayvanın yanına bağlamak · yanda çekilerek götürülen hayvan · yarış atının yanında yedek bir at koşturma yasağı
  جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير (maqayis;jamhara)؛ الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة (ayn)؛ جنبت الدابة إذا قدتها إلى جنبك ومنه خيل مجنبة (sihah)؛ جنبت الفرس أجنبه جنبا إذا قدته والجنيبة الدابة تقاد (tahdhib)؛ من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك (mufradat)
- **B006** güneyden esen yel — güney yeli · yelin güneyden esmesi veya topluluğun bu yele girip ona tutulması · güney yelinin sürüklediği bulut
  مما شذ عن الباب ريح الجنوب (maqayis)؛ الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح (ayn)؛ الجنوب ريح معروفة (jamhara)؛ الجنوب الريح التي تقابل الشمال (sihah)؛ الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور (tahdhib)؛ الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة (mufradat)
- **B007** böğür bölgesini tutan ağrı veya hastalık — böğrü ağrımak veya akciğer zarı hastalığına tutulmak · vurarak böğrünü incitmek veya kırmak · devenin aşırı susuzluktan akciğeri böğrüne yapışacak ölçüde hastalanması
  الجنب أن يشتد عطش البعير حتى تلتصق رئته بجنبه (maqayis)؛ أجنب فلان إذا أخذته ذات الجنب والجنيب الذي يشتكي جنبه (ayn)؛ جنب الرجل إذا اشتكى جنبه (jamhara)؛ المجنوب الذي به ذات الجنب وجنب البعير من شدة العطش (sihah)؛ ذات الجنب علة صعبة وجنب جنبا إذا اشتكى جنبه (tahdhib)؛ جنب شكا جنبه (mufradat)
- **B008** develerde sütün azalması veya tükenmesi — topluluğun develerinde sütün azalması veya tükenmesi · süt kıtlığı yaşanan yıl
  جنب القوم إذا قلت ألبانهم (maqayis;sihah)؛ جنب بنو فلان إذا لم يكن في إبلهم لبن (ayn;tahdhib)؛ جنب الرجل إذا قلت ألبان إبله (jamhara)؛ جنب بنو فلان إذا لم يكن في إبلهم اللبن (mufradat)
- **B009** çok miktarda iyilik veya kötülük [kalıp] — pek çok iyilik veya kötülük
  المجنب الخير الكثير كأنه إلى جنب الإنسان (maqayis)؛ شرا مجنبا وخيرا مجنبا أي كثيرا (ayn)؛ خيرا مجنبة ومجنبا وشرا مجنبا أي كثيرا (jamhara)؛ المجنب بالفتح الشيء الكثير وخيرا مجنبا وشرا مجنبا (sihah)؛ المجنب الخير الكثير والمجنب يقال في الشر إذا كثر (tahdhib)؛ جنب فلان خيرا وجنب شرا (mufradat)
- **B010** yazın kalan köklü küçük bitkiler — yazın kalan, köklü küçük bitki veya çalı
  الجنبة اسم يقع على عامة الشجر يترك في الصيف (ayn)؛ الجنبة ضرب من النبت (jamhara)؛ الجنبة اسم لكل نبت يتربل في الصيف (sihah)؛ الجنبة اسم واحد لنبوت كثيرة هي كلها عروة (tahdhib)
- **B011** yanı koruyan kalkan veya örtü — kişinin yanında taşıdığı kalkan veya koruyucu örtü
  سمي الترس مجنبا لأنه إلى جنب الإنسان (maqayis)؛ المجنب الترس (ayn;sihah;tahdhib)؛ المجنب الترس ويقال المجنب والمجنب الستر أيضا (jamhara)
- **B012** atın bacaklarında doğuştan ölçülü açıklık — atın bacaklarının doğuştan birbirinden ayrı durması, fakat aşırı ayrık olmaması
  التجنيب انحناء وتوتير في رجل الفرس (sihah)؛ المجنب من الخيل البعيد ما بين الرجلين من غير فجج والتجنيب بالجيم في الرجلين (tahdhib)؛ التجنيب الروح في الرجلين وذلك إبعاد إحدى الرجلين عن الأخرى خلقة (mufradat)

## ء ث م (root_000013): 42:37 ٱلْإِثْمِ

- **B001** gecikme ve iyilikten geri bırakan suç — geri kalan veya ağır ilerleyen dişi deve · günah; iyilikten ve ödülden geri bırakan kötü eylem · günah veya günaha düşülen yer · günaha girmek · günah işleyen veya günah yükünü taşıyan kimse · günahla nitelenen kimse · çok günah işleyen veya ahlaksız kimse · çokça günah işleyen kimse · günah veya ödülden geri bırakan eylemler
  أصل واحد وهو البطء والتأخر (maqayis)؛ ناقة آثمة أي متأخرة (maqayis)؛ ناقة آثمة ونوق آثمات أي مبطئات (sihah)؛ الإثم مشتق من ذلك لأن ذا الإثم بطيء عن الخير (maqayis)؛ الأثم الذنب (sihah)؛ أثم فلان يأثم إثما أي وقع في الإثم (sihah;tahdhib;ayn)؛ الإثم والأثام اسم للأفعال المبطئة عن الثواب (mufradat)؛ الأثيم والأثام والأثيمة في كثرة ركوب الإثم والآثم الفاعل (ayn)
- **B002** günahtan sakınma ve günah yükünden çıkma — günahtan sakınmak, ondan geri durmak veya günahından sıyrılmak
  فإذا تحرج وكف قيل تأثم (maqayis)؛ تأثم أي تحرج عنه وكف (sihah)؛ تأثم أي تحرج من الإثم وكف عنه (tahdhib;ayn)؛ وتأثم خرج من إثمه (mufradat)
- **B003** günahın cezası ve karşılığı — günahın cezası, karşılığı veya azabı · günahının karşılığını görmüş veya cezalandırılmış kimse
  الأثام جزاء الإثم (sihah)؛ الأثام في جملة التفسير عقوبة الإثم (tahdhib;ayn)؛ تأويل الأثام المجازاة (tahdhib)؛ يلق أثاما أي عذابا (mufradat)؛ العبد مأثوم أي مجزي جزاء إثمه (tahdhib)
- **B004** günah sayma, günaha sokma, suçlama veya cezalandırma — bir davranışın kişiye günah sayılması veya kişinin günahının karşılığını görmesi · birini günaha sokmak · birine günah işlediğini söylemek veya onu günahla suçlamak
  أثمه الله أي عده عليه إثما (sihah)؛ آثمه أوقعه في الإثم (sihah)؛ آثمه بالتشديد أي قال له أثمت (sihah)؛ أثمه الله أي جازاه جزاء الإثم (tahdhib)؛ فعل ما يؤثمه (mufradat)
- **B005** şarap için tartışmalı ad — 
  أن الإثم الخمر (maqayis)؛ وقد تسمى الخمر إثما (sihah)؛ الإثم من أسماء الخمر (tahdhib)؛ وليس الإثم في أسماء الخمر بمعروف ولم يصح فيه بيت صحيح (tahdhib)؛ ولا أعلم كيف صحته (maqayis)

## ف ح ش (root_001134): 42:37 وَٱلْفَوَٰحِشَ

- **B001** ağır ve yüz kızartıcı çirkinlik — ağır ve ürkütücü çirkinlik · çok çirkin ve yüz kızartıcı şey · doğru olana uymayan ağır çirkin iş
  تدل على قبح في شيء وشناعة (maqayis)؛ الفحش معروف والفحشاء اسم للفاحشة (ayn;tahdhib)؛ الفحش معروف (jamhara)؛ الفحشاء الفاحشة (sihah)؛ ما عظم قبحه من الأفعال والأقوال (mufradat)
- **B002** hoş karşılanmayan ölçü aşımı — sınırını aştığı için hoş karşılanmayan · iş sınırını aştı ve ağırlaştı · giderek daha aşırı ve çirkin duruma gelmek
  كل شيء جاوز قدره فهو فاحش ولا يكون ذلك إلا فيما يتكره (maqayis)؛ كل شئ جاوز حده فهو فاحش (sihah)؛ كل شيء جاوز حده وقدره فهو فاحش (tahdhib)
- **B003** ağır çirkin söz söyleme veya davranışta bulunma — ağır çirkin söz söylemek veya davranışta bulunmak · utanmazca konuşur veya davranır duruma gelmek · sık sık ağır çirkin söz söyleyen veya davranan · birine ağır çirkin sözler söylemek · konuşmasında bilerek sövgüye ve çirkinliğe başvurmak · insanlara sövmeyi ve kırıcı konuşmayı bilerek sürdüren kişi
  أفحش الرجل قال الفحش وفحش وهو فحاش (maqayis)؛ أفحش في القول والعمل (ayn)؛ جاء الرجل بالفحش والفحشاء إذا أفحش (jamhara)؛ أفحش عليه في المنطق أي قال الفحش وتفحش في كلامه (sihah)؛ قال قولا فاحشا وذو الفحش والخنا من قول وفعل والمتفحش الذي يتكلف سب الناس (tahdhib)؛ ما عظم قبحه من الأفعال والأقوال والمتفحش الذي يأتي بالفحش (mufradat)
- **B004** yasaklanmış ağır davranış — evlilik dışı cinsel ilişki · boşanmış kadının kendisini boşayan kocasının izni olmadan evden çıkması · kadının kocasının yakınlarına kırıcı ve saldırgan konuşması · cinsel yoldan çıkma · evlilik dışı cinsel ilişki veya cinsel yoldan çıkma · yasaklanmış ağır davranışı yapan kişi
  فاحشة مبينة يعني خروجها من بيتها بغير إذن زوجها المطلقها (ayn)؛ ربما جعلوا الفحشاء الفجور (jamhara)؛ يسمى الزنى فاحشة (sihah)؛ الفاحشة المبينة أن تزني أو خروجها من بيتها أو بذاءتها وسلاطة لسانها والفاحشة المنهي عنها وجمعها الفواحش (tahdhib)؛ كناية عن الزنا واللاتي يأتين الفاحشة (mufradat)
- **B005** aşırı cimrilik — cimri veya vermekte aşırı katı kişi · cimrilik
  الفاحش البخيل وهذا على الاتساع والبخل أقبح خصال المرء (maqayis)؛ الذي جاوز الحد في البخل (sihah)؛ الفحشاء هاهنا البخل والعرب تسمي البخيل فاحشا (tahdhib)؛ العظيم القبح في البخل (mufradat)

## ص ل و (root_000879): 42:38 ٱلصَّلَوٰةَ

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## ECHO ص ل ي (root_000880): for 42:38 ٱلصَّلَوٰةَ: withheld observed target; not identity

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ش و ر (root_000827): 42:38 شُورَىٰ

- **B001** gösterme ve sınamaya sunma — hayvanı satışa veya sınamaya sunmak · hayvanların gösterildiği yer · hayvanı yürüyüşünü veya koşusunu görmek için denemek
  أصل إبداء شيء وإظهاره وعرضه (maqayis)؛ شرت الدابة شورا إذا عرضتها والمشوار موضع عرض الدواب (maqayis;sihah)؛ التشوير أن تشور الدابة كيف سيرتها وشرت الفرس ركضته (ayn)؛ شرت الدابة استخرجت عدوه (mufradat)
- **B002** balı yerinden çıkarıp toplama — balı bulunduğu yerden çıkarıp toplamak · bal toplama işi · balı çıkarmak; aktarılan bir söyleyiş · balı toplayıp almak · bal alınan kovan · bal toplayıcısının kullandığı tutacak veya çubuk · arıların yerleşip bal yaptığı yer
  شرت العسل أشوره وأشرته واشترته (ayn;sihah;mufradat)؛ الباب الآخر قولهم شرت العسل أشوره (maqayis)؛ المشار الخلية يشتار منها العسل (maqayis;sihah)؛ المشاور المخابض الواحد مشور عود يكون مع مشتار العسل (sihah)
- **B003** görüş alışverişiyle karar arama — bir işinde birine danışmak · onun görüşünü istemek · danışma ve karşılıklı görüşme · danışılan konu veya danışma süreci · ona görüş ve öğüt vermek · danışılmaya elverişli kimse
  شاورت فلانا في أمري والمستشير يأخذ الرأي من غيره (maqayis)؛ المشورة اشتق من الإشارة أشرت عليهم بكذا (ayn)؛ أشار عليه بالرأي وشاورته في الأمر واستشرته بمعنى والمشعورة الشورى (sihah)؛ التشاور والمشاورة والمشورة استخراج الرأي بمراجعة البعض إلى البعض والشورى الأمر الذي يتشاور فيه (mufradat)
- **B004** elle işaret etme — ona eliyle işaret etmek · ona eliyle yönelip işaret etmek · işaret parmağı
  المشيرة الإصبع التي يقال لها السبابة (ayn)؛ أشار إليه باليد أومأ وشور إليه بيده أي أشار (sihah)
- **B005** mahrem yer ve onu açığa vururcasına utandırma — birini mahrem yerini açmış gibi utandırmak · mahrem yer; cinsel organ · Tanrı onun mahrem yerini açığa çıkardı
  شور به إذا أخجله من الشوار والشوار فرج الرجل وأبدى شواره (maqayis)؛ التشوير التخجيل شورت بفلان وتشور فلان (ayn)؛ الشوار فرج المرأة والرجل ومنه شور به كأنه أبدى عورته (sihah)؛ الشوار يكنى به عن الفرج وشورت به فعلت به ما خجلته (mufradat)
- **B006** görünür eşya, güzel giyim ve görünüş — dışarıda görünen eşya veya ev eşyası · güzel giyim ve hoş görünüş
  الشوار متاع البيت أيضا فإن كان صحيحا (maqayis)؛ الشارة الهيئة واللباس الحسن (ayn)؛ الشوار والشارة اللباس والهيئة وحسن الصورة والشورة (sihah)؛ الشوار ما يبدو من المتاع (mufradat)
- **B007** hayvanın semirip güzelleşmesi — semiz ve güzel atlar · develerin biraz semirmesi · atın semirip güzelleşmesi · semiz deve
  هو السمين (maqayis)؛ خيل شيار أي سمان حسان (ayn)؛ اشتارت الإبل إذا سمنت بعض السمن وجاءت الإبل شيارا أي سمانا حسانا وشار الفرس أي سمن وحسن (sihah)
- **B008** döl tutmamış dişiyi ayırt eden erkek deve — döl tutmamış dişiyi diğerlerinden ayırt eden erkek deve
  المستشير البعير الذي يعرف الحائل من غير الحائل ويقال بل هو السمين (maqayis)؛ المستشير الفحل الذى يعرف الحائل من غيرها وأبو عمرو المستشير السمين (sihah)
- **B009** tarladaki ekim bölmesi — tarladaki ekim bölmesi veya tarla sırtı
  المشارة الدبرة التي في المزرعة (sihah)

## ن ف ق (root_001537): 42:38 يُنفِقُونَ

- **B001** tükenip sona erme; özel kullanımlarda alıcı bulma, çabuk kesilme veya yüzeyden ayrılma — hayvan öldü · tükendi, sona erdi · fiyat veya satış canlandı, mal alıcı buldu · topluluğun pazarı canlandı, malları alıcı buldu · eşi bulunmayan kadına evlenme isteğiyle başvuranlar çoğaldı · koşusu çabuk kesilen at · kesintiye uğrayan gidiş · yaranın kabuğu soyuldu · develerin semirmeden dolayı tüyleri döküldü · insanlara söven kişi karşılığında sövgü görür ve onurunu diline düşürür
  نفقت الدابة نفوقا أي ماتت (maqayis;ayn;sihah;tahdhib;mufradat); نفق الشيء فني ونفد (maqayis;sihah;tahdhib;mufradat); نفق السعر أو البيع نفاقا وكثر مشتروه (maqayis;ayn;sihah;tahdhib;mufradat); فرس نفق الجري وسير نفق سريع الانقطاع (maqayis;sihah;tahdhib); نفق الجرح إذا انقشر وانتثرت الأوبار عن سمن (tahdhib)
- **B002** bir şeyi gider olarak elden çıkarma; özel kullanımda elindekini tüketip yoksullaşma — geçim için yapılan gider; harcanan şey · harcadı, elden çıkardı · adam malı tükenince yoksullaştı · çok harcayan kişi
  النَّفَقَة لأنها تمضي لوجهها (maqayis); النَّفَقَة ما أنفقت واستنفقت على العيال ونفسك (ayn;tahdhib); أنفقت الدرهم من النَّفَقَة ورجل منقاق كثير النَّفَقَة (sihah); الإنفاق قد يكون في المال وفي غيره واجبا وتطوعا (mufradat); أنفق الرجل افتقر وذهب ما عنده أو ماله (maqayis;sihah;tahdhib;mufradat)
- **B003** başka bir yere açılan yer altı geçidi ve kemirgen yuvasındaki gizli çıkış — çıkışı bulunan yer altı geçidi · kemirgen yuvasındaki inceltilmiş gizli çıkış · kemirgen yuvasındaki gizli çıkış · gizli çıkıştan dışarı çıktı · kemirgeni sıkıştırıp gizli çıkışından kaçırdık · kemirgen gizli çıkışına girdi
  النفق سرب في الأرض له مخلص إلى مكان (maqayis;ayn;sihah;tahdhib); النفق الطريق النافذ والسرب في الأرض النافذ فيه (mufradat); النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج (maqayis;ayn;sihah;tahdhib); بعضهم يسمي النافقاء النَّفَقَة (ayn;sihah;tahdhib)
- **B004** içindeki inanç veya tutumun tersini göstererek bağlı görünme — içindekinin tersini gösterme ve inançta ikiyüzlülük · içindekinden başkasını göstererek ikiyüzlü davrandı · içinde sakladığının tersini gösteren kimse
  النفاق لأن صاحبه يكتم خلاف ما يظهر (maqayis); النفاق الخلاف والكفر والفعل نافق نفاقا (ayn); ومنه اشتقاق المنافق في الدين (sihah); سمي المنافق منافقا للنفق وهو السرب في الأرض (tahdhib); النفاق الدخول في الشرع من باب والخروج عنه من باب (mufradat)

## ج ز ي (root_000244): 42:40 وَجَزَٰٓؤُا۟

- **B001** iyiliğe ya da kötülüğe denk karşılık verme — birine yaptığını iyilikle ya da kötülükle karşılama · birine yaptığının karşılığını verme · yapılana verilen iyi ya da kötü karşılık · çok geçmeden öç alma karşılığı · iyi işlerin ve yerine getirilmesi gereken yükümlülüklerin karşılıkları
  جزى يجزي جزاء أي كافأ بالإحسان وبالإساءة (ayn)؛ جزيته بما صنع جزاء وجازيته (sihah)؛ الجزاء يكون ثوابا ويكون عقابا؛ جزيت فلانا بما صنع جزاء؛ جزاء العطاس؛ الجوازي معناها الجزاء (tahdhib)؛ الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر؛ جزيته بكذا وجازيته (mufradat)؛ مكافأته إياه؛ جزيت فلانا أجزيه جزاء وجازيته مجازاة (maqayis)
- **B002** yerini tutup yükümlülüğü karşılama — yeterlilik ve bir işi başkası adına yerine getirme · bu işi benim yerime görüp tamamlama · bir koyunun senin adına yükümlülüğü karşılaması · yeterli olan ve başkasının yerini tutan kimse · birinin alacağını ya da borcunu ödeme
  فلان ذو غناء وجزاء (ayn)؛ جزى عني هذا الأمر أي قضى؛ جزت عنك شاة؛ رجل جازيك أي حسبك (sihah)؛ الجزاء أيضا القضاء؛ لا تقضي فيه نفس عن نفس شيئا؛ جزيت فلانا حقه؛ جزيته قرضه؛ صدقتك جزت عنك؛ هذا رجل حسبك وناهيك وكافيك وجازيك (tahdhib)؛ الجزاء الغناء والكفاية؛ لا يجزي والد عن ولده؛ جازيك فلان أي كافيك (mufradat)؛ قيام الشيء مقام غيره؛ ينوب مناب كل أحد؛ جزى عني هذا الأمر يجزي كما تقول قضى يقضي (maqayis)
- **B003** alacağı talep etme — borcumu ondan isteme · alacağını isteyen veya borcun ödenmesini talep eden kimse
  تجازيت ديني تقاضيته (ayn)؛ تجازيت ديني على فلان إذا تقاضيته؛ المتجازي المتقاضي (sihah)؛ أمرت فلانا يتجازى ديني أي يتقاضاه؛ أهل المدينة يسمون المتقاضي المتجازي (tahdhib)؛ تجازيت ديني على فلان أي تقاضيته؛ أهل المدينة يسمون المتقاضي المتجازي (maqayis)
- **B004** koruma statüsüne bağlı tarihsel vergi — koruma statüsündeki topluluklardan alınan tarihsel vergi · koruma statüsüne bağlı tarihsel vergiler
  الجزية ما يؤخذ من أهل الذمة والجمع الجزى (sihah)؛ الجزية جزية الناس التي تؤخذ من أهل الذمة؛ الجزية الخراج المجعول على الذمي سميت جزية لأنها قضاء منه لما عليه (tahdhib)؛ الجزية ما يؤخذ من أهل الذمة وتسميتها بذلك للاجتزاء بها عن حقن دمهم (mufradat)
- **B005** karşılık vermede üstün gelme [kalıp] — karşılık verme yarışında ötekine üstün gelme
  جازيته فجزيته أي غلبته (sihah)

## ECHO ج ز ز (root_000242): for 42:40 وَجَزَٰٓؤُا۟: withheld observed target; not identity

- **B001** saç, yün veya bitkiyi kırkıp kesme — saçı, yünü veya bitkiyi kırkıp kesmek · kırkma aleti · yünü kırkılan koyunlar
  جززت الصوف جزا (maqayis); الجز جز الشعر والصوف وغيره (ayn); جززت البر والنخل والصوف أجزه جزا والمجز ما يجز به (sihah); الجز جز الشعر والصوف والحشيش ونحوه وقد جززت الكبش والنعجة (tahdhib)
- **B002** kesim ya da hasat vaktinin gelmesi — kırkım, hasat veya ürün toplama zamanı · ağaç ürününün, ekinin veya koyunun kesim ya da kırkım vaktinin gelmesi · topluluğun koyunlarını kırkma ya da ekinini biçme vaktinin gelmesi · ekinin biçilecek duruma gelmesi
  هذا زمن الجزاز والجزاز (maqayis); الجزاز كالحصاد يقع على الحين والأوان وأجز النخل مثل أحصد البر (ayn); هذا زمن الجزاز والجزاز أي زمن الحصاد وصرام النخل وأجز النخل والبر والغنم واستجز البر (sihah); الجزاز كالحصاد واقع على الحين والأوان وأجز النخل حان له أن يجز وأجز القوم إذا حان أن تجز غنمهم (tahdhib)
- **B003** yeni kırkılmış yün veya kesimden kalan parça — henüz kullanılmamış kırkılmış yün · bir koyundan bir yılda kırkılan yün · deri veya başka bir şey kesilince düşen ya da fazla kalan parça · bir tutam yün
  الجزيزة خصلة من صوف والجمع جزائز والجزازة ما سقط من الأديم (maqayis); الجزز الصوف الذي لم يستعمل بعد ما جز وصوف كل شاة جزة والجزاز ما فضل من الأديم (ayn); الجزة صوف شاة والجزازة ما سقط من الأديم والجزيزة خصلة من الصوف (sihah); الجزز الصوف الذي لم يستعمل بعدما جز وهذه جزة هذه الشاة والجزاز ما فضل من الأديم (tahdhib)
- **B004** asılan boyalı yün süsü veya süs boncuğu — deve üzerindeki yolcu bölmesine bağlanan veya asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesine asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesinden sarkan boyalı yün parçası · insanı süslemek için kullanılan bir boncuk türü
  الجزائر عهون تشد على الهوادج (ayn); الجزجزة وهي عهنة تعلق من الهودج (sihah); الجزاجز خصل العهن والصوف المصبوغة تعلق على هوادج الظعائن وهي الثكن والجزائز وقيل الجزيز ضرب من الخرز (tahdhib)
- **B005** hurmanın kuruması veya hurmadaki kuruluk — hurmanın kuruması · hurmanın kuruması · hurmadaki kuruluk veya kuruma durumu
  جز التمر يجز بالكسر جزوزا أي يبس وأجز مثله وتمر فيه جزوز (sihah); قد جز التمر إذا يبس يجز جزوزا وتمر فيه جزوز (tahdhib)
- **B006** rivayette bir çıkış yeri olarak anılan yer adı — rivayette bir çıkış yeri olarak anılan yer adı
  جزة اسم أرض يقال إن الدجال يخرج منها (ayn); جزة اسم أرض منها يخرج الدجال فيما روي (tahdhib)

## ح ب ب (root_000286): 42:40 يُحِبُّ

- **B001** tane, tohum ve taneye benzeyen tek parça — tahıl tanesi ve yenebilir bitki tohumu · tek tane, tohum veya taneye benzeyen parça · dolu tanesi
  الحبة واحد الحب (jamhara;sihah)؛ الحب والحبة في الحنطة والشعير وبزور الرياحين (maqayis;tahdhib;mufradat)؛ الحبة من الشيء القطعة منه وحب الغمام وحب المزن وحب قر والحب القرط من حبة واحدة (sihah;tahdhib)
- **B002** sevgi ve yeğleme — sevgi; nefretin karşıtı · iyi görülen şeye yönelen güçlü sevgi · sevmek veya sevdirmek · yeğlemek veya sevmeye yönelmek · birbirini sevmek
  الحب والمحبة اشتقاقه من أحبه إذا لزمه (maqayis)؛ أحببته نقيض أبغضته (ayn)؛ المحبة إرادة ما تراه أو تظنه خيرا (mufradat)؛ استحبوا أي آثروه عليه (mufradat)
- **B003** övgü, güçlü istek ve kabul bildiren kalıplar — ne güzel; ne iyi · en büyük isteğin bunu yapmaktır · peki, memnuniyetle ve baş üstüne
  حبذا حرفان حب وذا تقول حبذا زيد (ayn;sihah;tahdhib)؛ حبابك أن تفعل ذاك معناه غاية محبتك (ayn;sihah;tahdhib;mufradat)؛ الحبة بالضم الحب يقال نعم وحبة وكرامة (sihah)
- **B004** kalbin içindeki kara öz [kalıp] — kalbin kara iç noktası veya özü
  حبة القلب سويداؤه ويقال ثمرته (maqayis;sihah)؛ حبة القلب هي العلقة السوداء التي تكون داخل القلب (tahdhib)؛ حبة القلب تشبيها بالحبة في الهيئة (mufradat)
- **B005** devenin güçsüzlükten yerinden ayrılamaması — devenin güçsüzlükten durup yerinden ayrılamaması · devenin hastalık veya güçsüzlükten çökmesi
  المحب البعير الذي يحسر فيلزم مكانه (maqayis)؛ بعير محب وقد أحب إحبابا وهو أن يصيبه مرض أو كسر فلا يبرح من مكانه (sihah;tahdhib)؛ أحب البعير إذا حرن ولزم مكانه (mufradat)
- **B006** suyla dolmak veya doldurup dolulaştırmak — su içip dolmak veya suya kanmak · doldurup dolu hale getirmek
  تحبب الحمار إذا امتلأ من الماء وشربت الإبل حتى حببت (sihah)؛ أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره (tahdhib)
- **B007** iri küp ve iki kulplu küpün dört parçalı desteği — iri küp veya büyük saklama kabı · iki kulplu küpün dört parçalı ayağı
  الحب الجرة الضخمة ويجمع على حببة وحباب (ayn;tahdhib)؛ الحب الخابية فارسي معرب والجمع حباب وحببة (sihah)؛ الحب الخشبات الأربع التي توضع عليها الجرة ذات العروتين (ayn;tahdhib)
- **B008** su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy — su kabarcıkları, suyun ana kütlesi, dalgası veya yüzey çizgileri · ağaç üzerindeki çiy
  حباب الماء فقاقيعه الطافية (ayn;tahdhib)؛ حباب الماء معظمه (maqayis;ayn;sihah;tahdhib)؛ حباب الماء موجه والطرائق التي في الماء (tahdhib)؛ الحباب من الماء النفاخات تشبيها به (mufradat)؛ الحباب الطل على الشجر (tahdhib)
- **B009** düzenli diş dizisi ve beyaz tükürük parıltısı — düzenli diş dizisi veya dişlerdeki beyaz tükürük parıltısı
  الحبب تنضد الأسنان (maqayis;ayn;sihah;tahdhib)؛ الحبب تنضد الأسنان تشبيها بالحب (mufradat)؛ حبب الفم ما يتحبب من بياض الريق على الأسنان (tahdhib)
- **B010** kısa veya küçük yapılı; develerde cılız — kısa boylu veya küçük bedenli kimse · cılız develer
  الحبحاب الرجل القصير (maqayis)؛ الحباحب الصغار (maqayis;sihah)؛ الحبحاب الصغير الجسم (tahdhib)؛ إبل حبحبة مهازيل (tahdhib)
- **B011** yararsız zayıf kıvılcım veya gece ışıldayan böcek — yararsız zayıf kıvılcım veya gece ışıldayan böcek · zayıf kıvılcımın tutuşması
  نار الحباحب ما اقتدحت من شرار النار في الهواء من تصادم الحجارة (ayn;tahdhib)؛ نار الحباحب ما أورت الخيل لا ينتفع به (maqayis;sihah;tahdhib)؛ ذباب يطير بالليل له شعاع كالسراج (ayn;sihah;tahdhib)
- **B012** yılan; yılanla ilişkilendirilen kötücül ruh adı — yılan veya yılanla ilişkilendirilen kötücül ruh adı
  ومما شذ عن الباب الحباب وهو الحية (maqayis)؛ الحباب أيضا الحية (sihah)؛ الحباب الحية وإنما قيل الحباب اسم شيطان لأن الحية يقال لها شيطان (tahdhib)

## س ب ل (root_000672): 42:41 سَبِيلٍ, 42:42 ٱلسَّبِيلُ, 42:44 سَبِيلٍ, 42:46 سَبِيلٍ

- **B001** yol ve bir amaca ulaştıran yol — yol; bir şeye ulaştıran bağlantı veya yöntem · yollar, izlenen güzergahlar · dinsel doğruluk ve iyilik yolu
  السبيل وهو الطريق سمي بذلك لامتداده (maqayis)؛ والسبيل يذكر ويؤنث وجمعه سبل (ayn)؛ السبيل معروف تذكر وتؤنث والجمع سبل وهي الطرق (jamhara)؛ السبيل الطريق؛ أي سببا ووصلة (sihah)؛ السبيل الطريق؛ لا يستطيعون في أمرك حيلة (tahdhib)؛ السبيل الطريق الذي فيه سهولة؛ لكل ما يتوصل به إلى شيء (mufradat)
- **B002** yol kullanan kişi veya yolcu — yollarda gidip gelenler · yolu izleyen kişi · evinden uzaktaki veya yolda kalmış yolcu
  السابلة المختلفة في السبل جائية وذاهبة (maqayis)؛ السابلة المختلفة في الطرقات للحوائج (ayn)؛ السابلة هم الذين يسلكون السبل (jamhara)؛ السابلة أبناء السبيل المختلفة في الطرقات (sihah)؛ ابن السبيل المسافر الذي انقطع به (tahdhib)؛ قيل لسالكه سابل؛ وابن السبيل المسافر البعيد عن منزله (mufradat)
- **B003** malı sürekli iyilik kullanımına ayırmak [kalıp] — malı veya taşınmazı sürekli iyilik kullanımına ayırmak · yol gideri olmayan savaş görevlisine ayrılan yardım payı
  سبلت مالا في سبيل الله أي وقفته (ayn)؛ سبل ضيعته أي جعلها في سبيل الله (sihah)؛ حبس الرجل عقدة له وسبل ثمرها أو غلتها فإنه يسلك بما سبل سبل الخير (tahdhib)؛ ادع إلى سبيل ربك؛ قتلوا في سبيل الله (mufradat)
- **B004** aşağı doğru salmak — perdeyi aşağı salmak · yağmak; bulutun suyunu aşağı bırakması · giysiyi veya eteği yere doğru sarkıtmak · atın kuyruğunu aşağı salması · giysisini sürekli yere doğru sarkıtan kişi
  إرسال شيء من علو إلى سفل؛ أسبلت الستر أسبلت السحابة ماءها (maqayis)؛ الفرس أسبل ذنبه والمرأة أسبلت ذيلها؛ رجل مسبال عادته إسبال ثيابه (ayn)؛ أسبلت الستر إسبالا إذا أرخيته؛ أسبل الرجل إزاره (jamhara)؛ أسبل المطر والدمع إذا هطل؛ أسبل إزاره أي أرخاه (sihah)؛ الفرس يسبل ذنبه والمرأة تسبل ذيلها؛ أسبل فلان ثيابه إذا طولها وأرسلها إلى الأرض (tahdhib)؛ أسبل الستر والذيل وفرس مسبل الذنب (mufradat)
- **B005** yağan yağmur — yağmur, özellikle düşmekte olan yağmur · geniş ve bol sağanak
  السبل المطر الجود (maqayis)؛ السبل المطر (ayn)؛ والسبل المطر (jamhara)؛ السبل بالتحريك المطر؛ المطر بين السحاب والأرض (sihah)؛ السبل المطر المسبل؛ السبلة المطرة الواسعة؛ السبل المطر بين السحاب والأرض (tahdhib)؛ سبل المطر وأسبل؛ قيل للمطر سبل ما دام سابلا (mufradat)
- **B006** üst dudak ve sakal önündeki sarkan kıl — üst dudak kılı, bıyık veya sakalın öne sarkan bölümü · üst dudak kılı ya da sakalı uzun olan · ağız kılını yayarak tehdit etmek; bıyıklı kimseleri betimlemek
  سبال الإنسان من هذا لأنه شعر منسدل (maqayis)؛ السبلة ما على الشفة العليا من الشعر (ayn)؛ السبلة ما أسبل من شعر الشارب في اللحية (jamhara)؛ السبلة الشارب والجمع السبال (sihah)؛ السبلة مقدم اللحية وما أسبل منها على الصدر (tahdhib)؛ خص السبلة بشعر الشفة العليا لما فيها من التحدر (mufradat)
- **B007** kap kenarı veya hayvanın boğaz kesim yeri [kalıp] — kovanın dudakları veya kabın üst kenarı · büyükbaş hayvanın boğaz kesim noktası ve çevresi
  لأعالي الدلو أسبال (maqayis)؛ لتب في سبل الناقة إذا طعن في ثغرة نحرها (jamhara)؛ أسبال الدلو شفاهها (sihah)؛ السبلة المنحر من البعير وهو التريبة؛ ملأ الإناء إلى سبلته أي إلى رأسه (tahdhib)
- **B008** tahıl başağı ve başak çıkarmak — tahıl başağı; başaklar · ekinin başak çıkarması veya başaklı hale gelmesi · mısır, pirinç ve benzeri ürünlerin başağı
  سمي السنبل سنبلا لامتداده؛ أسبل الزرع إذا خرج سنبله (maqayis)؛ السبولة سنبلة الذرة والأرز وأسبل الزرع أي سنبل (ayn)؛ أسبل الزرع وسنبل إذا صار فيه السنبل (jamhara)؛ السبل أيضا السنبل؛ أسبل الزرع أي خرج سنبله (sihah)؛ السبولة هي سنبلة الذرة والأرز؛ قد أسبل الزرع إذا سنبل (tahdhib)؛ السنبلة جمعها سنابل؛ أسبل الزرع صار ذا سنبلة (mufradat)
- **B009** eski pay oyunundaki beşinci veya altıncı çubuk — eski pay oyunundaki beşinci veya altıncı çubuk
  المسبل اسم خامس سهام القداح (ayn)؛ المسبل السادس من سهام الميسر (sihah)؛ المسبل من قداح الميسر السادس وفيه ستة فروض (tahdhib)؛ المسبل اسم القدح الخامس (mufradat)
- **B010** kırmızı damarlı ağsı göz perdesi — kırmızı damarlı, ağsı perde oluşturan göz hastalığı
  السبل داء في العين شبه غشاوة كأنها نسج العنكبوت بعروق حمر (sihah)

## ء ن س (root_000059): 42:42 ٱلنَّاسَ, 42:48 ٱلْإِنسَٰنَ, 42:48 ٱلْإِنسَٰنَ

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

## غ ي ر (root_001119): 42:42 بِغَيْرِ

- **B001** yarar sağlayıp durumunu iyileştirme — aileyi geçindiren azık ve ihtiyaç payı · aileye geçimlik ve yarar sağlama · ailesine geçimlik sağladı ve yarar dokundurdu · ona yarar sağladı ve ihtiyacını giderdi · Tanrı onlara yağmur verip durumlarını iyileştirdi · yağmur toprağı suladı · sulanmış toprak · sulanmış toprak · yük takımlarını düzeltiyorlar · devesinin yükünü indirip durumunu düzeltti · hayvanı rahatlatmak için yük takımını düzenleyen kişi
  الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)
- **B002** cana karşılık ceza yerine kabul edilen kan bedeli — bana kan bedelini ödedi · kan bedeli · cana karşılık ceza yerine kabul edilen kan bedeli
  غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)
- **B003** biçimini değiştirme veya yerine başkasını koyma — şeyi değiştirdi ve öncekinden farklı hale getirdi · biçimini değiştirme veya yerine başkasını koyma · durumundan ayrılıp farklı hale geldi · yanlış olanı doğru olanla değiştirip giderdi · onunla alışverişte karşılıklı değiş tokuş yaptı · yerine konan karşılık
  الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)
- **B004** eşini veya ailesini kıskanarak koruma duygusu — eşini veya ailesini kıskanarak koruma duygusu · eşini veya ailesini kıskanıp sakındı · eşine veya ailesine karşı kıskanç ve korumacı · eşine veya ailesine karşı kıskanç erkek · eşine veya ailesine karşı kıskanç kadın · eşine veya ailesine karşı çok kıskanç kişi · eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi
  الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)
- **B005** başka olma, dışta bırakma veya olumsuzlama — başka, aynı olmayan veya aykırı · dışında, dışta bırakarak · değil, olmayan · doğru olmayan, yanlış · biri öteki olmayan iki şey · şeyler birbirinden farklılaştı
  هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)

## ع ز م (root_001010): 42:43 عَزْمِ

- **B001** kesin karar ve kararlı sebat — bir işi yapmaya kesin karar verme · işi yapmaya kesin karar verdi · kesin karar ve kararlılık · kesinleştirilmiş karar · kararında sebatı yok · sağlam ve kararlı görüşlü · inançsızlarla bağlarını kesme kararlılığı gösteren elçiler · sabır · sözünü yerine getiren adam · işlerin en iyisi, kararın, görüşün ve niyetin sağlamlaştırıldığı işlerdir
  أصل واحد صحيح يدل على الصريمة والقطع (maqayis)؛ العزم ما عقد عليه القلب (maqayis;ayn;tahdhib)؛ أردت فعله وقطعت عليه (sihah)؛ صريمة أمر (sihah;tahdhib)؛ عقد القلب على إمضاء الأمر (mufradat)؛ ماله معزم ولا عزيمة ولا عزم (tahdhib)؛ العزم الصبر (tahdhib)
- **B002** yeminle ya da kesin emirle yükümlü kılma — sana yeminle söylüyorum veya kesin olarak emrediyorum · muhatabı bağlayan ciddi emir · okuyup üfleyenin hastalığa veya yılana karşı yeminli sözü
  عزمت عليك إلا فعلت كذا أي جعلته أمرا عزما (maqayis)؛ عزمت عليك بمعنى أقسمت عليك (sihah)؛ عزمت عليك لتفعلن أي أقسمت (tahdhib)؛ أمرتك أمرا جدا وهي العزمة (tahdhib)
- **B003** şifa ve korunma amaçlı sözlü okuma — görünmez varlıklara karşı okunan koruyucu söz · hastaya iyileşme umuduyla kutsal metinden okunan bölümler · okuyup üfleyenin hastalığa veya yılana karşı yeminli sözü
  عزمت على الجني وذلك أن تقرأ عليه من عزائم القرآن (maqayis)؛ الآيات التي يرجى بها قطع الآفة عن المؤوف (maqayis)؛ العزيمة الرقى ونحوها يعزم على الجن ونحوها من الأرواح (ayn)؛ العزائم الرقى (sihah)؛ العزيمة من الرقى التي يعزم بها على الجن والأرواح (tahdhib)؛ العزيمة تعويذ وجمعها العزائم (mufradat)
- **B004** yönünden dönmeden ilerleme — yönü tutup ilerlemeyi sürdürme · yolcu tuttuğu yönde ilerledi · yolda ilerleyip geri dönmüyor · atın dizgine aldırmadan koşması
  اعتزم السائر إذا سلك القصد قاطعا له (maqayis)؛ الرجل يعتزم الطريق يمضي فيه لا ينثني (maqayis;ayn;tahdhib)؛ الاعتزام لزوم القصد في الحضر والمشي (ayn)؛ الاعتزام لزوم القصد في المشي (sihah)؛ الفرس إذا وصف بالاعتزام فمعناه تجليحه في حضره غير مجيب لراكبه إذا كبحه (tahdhib)
- **B005** uyulması zorunlu hüküm ve görev — yöneticilerin uyulması gereken bağlayıcı buyruğu · Tanrı'nın zorunlu kıldığı görevler ve haklar · Tanrı'nın zorunlu kıldığı haklardan biri · kutsal metinde yere kapanmanın emredildiği bölümler · zorunlu ve bağlayıcı hüküm · işlerin en iyisi zorunlu görevleridir
  كانوا يرون لعزمة الخلفاء طاعة (maqayis)؛ عزائمه فرائضه التي أوجبها وأمرنا بها (tahdhib)؛ عزمة من عزمات الله حق من حقوق الله أي واجب مما أوجبه الله (tahdhib)؛ عزائم السجود ما أمر السجود فيها (tahdhib)؛ هذا أمر عزم وهذا فرض وحكم (tahdhib)
- **B006** yaşlı dişi deve veya yaşlı kadın — gençlik gücünden iz taşıyan yaşlı dişi deve veya yaşlı kadın · çok yaşlı dişi deve veya yaşlı kadın · yaşlı kadınlar
  العوزم الناقة المسنة وفيها بقية من شباب (sihah)؛ العوزم العجوز (sihah)؛ العزوم والعرزم الناقة الهرمة الدلقم (tahdhib)؛ العزم العجائز واحدتهن عزوم (tahdhib)
- **B007** kuru üzüm çekirdeği ve sap kırıntısı — kuru üzüm çekirdeği · kuru üzümün sap ve çöp kırıntısı · kuru üzüm sapı satıcısı
  العزم عجم الزبيب واحدها عزم (tahdhib)؛ العزم شجير الزبيب (tahdhib)؛ العزمي بياع الشجير (tahdhib)
- **B008** kişinin ailesi ve kabilesi — erkeğin ailesi ve kabilesi · aile ve kabile çevreleri
  عزمة الرجل أسرته وقبيلته وجماعها العزم (tahdhib)
- **B009** dostluğu onaran kişiler — dostluğu düzelten ve sağlamlaştıran kişiler
  العزمة المصححون للمودة (tahdhib)
- **B010** sert ve sıkı diye nitelenen kıç — sert ve sıkı diye nitelenen kıç · kıç için kullanılan örtmeceli ad · kişinin kıçı için kullanılan iyelikli örtmece
  إنها لعزوم مفزعة أراد بالعزوم استه (tahdhib)؛ العزوم ذات صرامة وحزم (tahdhib)؛ الدبر يقال لها أم عزم (tahdhib)؛ كذبته أم عزمه (tahdhib)

## ECHO م ر د (root_001413): for 42:44 مَرَدٍّ, 42:47 مَرَدَّ: withheld observed target; not identity

- **B001** doğal örtüsünden yoksun veya arındırılmış olma — üzerindeki doğal örtüden yoksun · sakalı henüz çıkmamış genç · yapraksız veya kabuğu soyulmuş dal · yapraksız ağaç · bitkisiz, düz kumluk · bitki bitmeyen düz arazi veya kumluk · çenesinin altında tüy bulunmayan at · kasık kılları bulunmayan kadın
  تجريد الشيء من قشره أو ما يعلوه من شعره؛ شجرة مرداء وغصن أمرد ورملة مرداء وغلام أمرد وفرس أمرد (maqayis;sihah;tahdhib;mufradat)؛ الرمال المرداء التي لا تنبت شجرة والأمرد الذي لم تنبت له لحية (ayn)
- **B002** yüzeyi düzleyip pürüzsüzleştirme ve böyle işlenmiş yapı — düz ve pürüzsüz; düzgün ve yüksek yapı · yapıyı sıvayıp düzleştirme · bir şeyi yumuşatıp perdahlamak veya pürüzsüzleştirmek
  الممرد البناء الطويل (maqayis)؛ تمريد البناء تمليسه (sihah)؛ الممرد المملس والتمريد التمليس والتطيين (tahdhib)؛ ممرد من قوارير أي مملس (mufradat)؛ التمريد تمليس الطين والتسوية (ayn)
- **B003** iyilikten kopup azgınca direnme ve kötülükte ısrar etme — iyilikten yoksun, azgın ve başkaldıran kimse · şiddetle başkaldıran, iyilikten yoksun kimse · ikiyüzlülüğe alışıp onda yerleşmek · kötülükte azıp sınırı aşmak · ona başkaldırıp direnmek · bir şeye alışıp onda beceri kazanma
  المارد العاتي وكذا المريد كأنه تجرد من الخير (maqayis)؛ المارد العاتي والمرود على الشيء المرون عليه (sihah)؛ المريد من شياطين الإنس والجن وتمرد علينا أي عتا واستعصى ومرد على الشر أي عتا وطغى (tahdhib)؛ المارد والمريد المتعري من الخيرات ومردوا على النفاق أي ارتكسوا عن الخير (mufradat)؛ تمرد عليه أي عصى واستعصى ومرد على الشيء أي عتا وطغى (ayn)
- **B004** yiyeceği ezip sıvıyla karıştırarak yumuşatma — yiyeceği ezip karıştırarak yumuşatmak · ekmeği suda ezip yumuşatmak · sütte bekletilip yumuşatılmış hurma · çocuğun annesinin memesini emmesi
  مرد الطعام يمرد مردا ماثه حتى يلين وهو من الإبدال والأصل مرس (maqayis)؛ مرد الخبز يمرده مردا أي ماثه حتى يلين والمريد التمر ينقع في اللبن ومرد الصبي ثدي أمه (sihah)؛ المرد الثريد ومرد الطعام إذا ماثه حتى يلين فقد مرده وتمر مريد (tahdhib)
- **B005** Salvadora persica ağacının ham meyvesi — Salvadora persica ağacının ham meyvesi
  المرد حمل الأراك (ayn)؛ المرد ثمر الأراك الغض منه (sihah)؛ البرير ثمر الأراك فالغض منه المرد والنضيج الكباث (tahdhib)
- **B006** tekneyi sırıkla iterek ilerletme — tekneyi uzun bir sırıkla iterek ilerletmek · tekneyi itmeye yarayan uzun sırık
  المرد دفعك السفينة بالمردي أي خشبة يدفع بها الملاح السفينة والفعل مرد يمرد (ayn)؛ المرد دفعك السفينة بالمروي وهي خشبة يدفع بها الملاح (tahdhib)
- **B007** güvercinlikteki küçük yumurtlama bölmesi — güvercinlikteki küçük yumurtlama bölmesi · üst üste dizilmiş güvercin yuvalıkları
  التمراد بيت الحمام يجعل لمبيضه فإذا جعلت نسقا بعضها فوق بعض فهي التماريد (ayn)؛ التمراد بيت صغير يجعل في بيت الحمام لمبيضه فإذا جعلت نسقا بعضها فوق بعض فهي التماريد (tahdhib)
- **B008** boyun — boyun
  المراد العنق وهو القياس إن صح (maqayis)؛ المراد بالفتح العنق (sihah)

## ع ر ض (root_001001): 42:45 يُعْرَضُونَ, 42:48 أَعْرَضُوا۟

- **B001** en, yan ve enli kılma — en; bir şeyin yanı veya tarafı · enli, geniş · bir şeyi enli duruma getirmek · sütten kesilmiş, henüz erginleşmemiş güçlü oğlak
  العرض خلاف الطول (maqayis;ayn;sihah;tahdhib;mufradat)؛ عرض الشيء فهو عريض (maqayis;ayn;sihah;tahdhib)؛ العرض الجانب من كل شيء (tahdhib;mufradat)
- **B002** görmeye veya incelemeye sunma [kalıp] — bir şeyi birine göstermek veya sunmak · malı satışa çıkarmak · askerleri gözden geçirmek · kitabı okumak veya başka bir nüshayla karşılaştırmak
  عرض المتاع يعرضه عرضا (maqayis)؛ يعرض علينا المتاع عرضا للبيع والهبة (ayn)؛ عرضت عليه أمر كذا وعرضت له الشيء أظهرته له وأبرزته إليه (sihah)؛ عرضت المتاع وغيره على البيع وكذلك عرض الجند والكتاب (tahdhib)؛ عرضت الشيء على البيع وعلى فلان وعرضنا جهنم (mufradat)
- **B003** uzaktan belirme ve beliren oluşum — uzaktan belirmek, görünmek · uzaktan beliren oluşum; özellikle bulut kümesi
  أعرض لك الشيء من بعيد إذا ظهر لك وبدا (maqayis)؛ عرض له أمر كذا أي ظهر (sihah)؛ أعرض لك الشيء أي بدا وظهر (tahdhib)؛ العارض البادي عرضه وتارة يخص بالسحاب (mufradat)
- **B004** araya girip engelleme ve karşısına dikilme — önüne geçip engel olmak · birinin karşısına dikilmek, ona sataşmak · insanları ayrım gözetmeden öldürmek veya yakalamak
  اعترض في الأمر إذا أدخل نفسه فيه (maqayis)؛ عرض القوم على السيف (ayn)؛ اعترض الشيء دون الشيء أي حال دونه (sihah)؛ كل مانع منعك فهو عارض (tahdhib)؛ اعترض الشيء في حلقه وقف فيه بالعرض (mufradat)
- **B005** yüz çevirip ilgiyi kesme — birinden yüz çevirmek, onunla ilgiyi kesmek
  أعرضت عن فلان وأعرضت عن هذا الأمر وأعرض بوجهه (maqayis)؛ الإعراض عن الشيء الصد عنه (sihah)؛ أعرض عني فمعناه ولى مبديا عرضه (mufradat)
- **B006** denk karşılık verme, karşılaştırma veya değişme — birinin hizasında gitmek veya yaptığına denk karşılık vermek · iki metni karşılaştırmak · bir malı başka bir malla değiştirmek
  عارضت فلانا في السير إذا سرت حياله وعارضته مثل ما صنع (maqayis)؛ عارضته في المسير وعارضت كتابي بكتابه (sihah)؛ عارضته بمتاع أو دابة معارضة إذا بادلته به وعارضت كتابي بكتابه (tahdhib)
- **B007** sonradan ortaya çıkan kalıcı olmayan durum veya nitelik — sonradan gelen geçici hastalık veya olay · nereden atıldığı bilinmeden isabet eden ok · birine ansızın gönül bağlamak
  العرض من أحداث الدهر كالمرض ونحوه (maqayis)؛ عرضه عارض من الحمى ونحوها (sihah)؛ العرض الأمر يعرض للرجل يبتلى به وسهم عرض (tahdhib)؛ العرض ما لا يكون له ثبات (mufradat)
- **B008** dünya malı, nakit dışı eşya ve mal karşılığı — dünya malı ve geçici dünyevi pay · nakit dışındaki ticari eşyalar · hakkı yerine bir mal vermek · yol azığı olarak verilen yiyecek veya aileye götürülen hediye
  العرض طمع الدنيا والدنيا عرض حاضر (maqayis)؛ العرض المتاع والعروض الأمتعة (sihah)؛ جميع متاع الدنيا عرض وما خالف الثمنين عروض (tahdhib)؛ تريدون عرض الدنيا ولو كان عرضا قريبا أي مطلبا سهلا (mufradat)
- **B009** kişinin bedeni, saygınlığı ve yüzünün yanı — kişinin bedeni, benliği veya saygınlığı · ayıplanacak yanı olmayan, itibarı temiz · yüzün veya yanağın yanı; ön dişlerin yan bölümü
  العرض عرض الإنسان حسبة أو نفسه (maqayis)؛ العرض الجسد والنفس والحسب (sihah)؛ العرض بدن كل الحيوان والنفس وحسبه (tahdhib)؛ العارض بالخد وتارة بالسن والعوارض للثنايا (mufradat)
- **B010** üstü kapalı, çift yönlü anlatım — görünür anlamının altında başka bir anlam taşıyan sözler · açıkça söylemeyip üstü kapalı anlatma
  معاريض الكلام يخرج في معرض غير لفظه الظاهر (maqayis)؛ التعريض خلاف التصريح والمعاريض في الكلام (sihah)؛ التعريض ما كان خلاف التصريح والمعاريض من الكلام (tahdhib)؛ التعريض كلام له وجهان من صدق وكذب أو ظاهر وباطن (mufradat)
- **B011** hedef olarak ortaya koyma veya bir işe hazır olma — hedef veya engel olarak ortaya konmuş şey · yolculuğa dayanıklı ve hazır deve
  فلان عرضة للناس لا يزالون يقعون فيه (maqayis)؛ فلان عرضة لذاك أي مقرن له قوي عليه وجعلت فلانا عرضة لكذا أي نصبته له (sihah)؛ لا تجعلوا الحلف بالله معترضا مانعا وجعلت فلانا عرضة أي نصبته له (tahdhib)؛ العرضة ما يجعل معرضا للشيء ولا تجعلوا الله عرضة لأيمانكم (mufradat)
- **B012** yana saparak ilerleme — atın koşarken yanını göstererek veya yana saparak gitmesi · yürüyüşü zor ve doğrultusunu korumayan dişi deve
  عرض الفرس في عدوه كأنه يرى الناظر عرضه (maqayis)؛ عرض الفرس في عدوه إذا مر عارضا على جنب واحد (ayn)؛ اعترض الفرس في رسنه لم يستقم لقائده وناقة عرضية فيها صعوبة (sihah)؛ تعرض فلان في الجبل أخذ يمينا وشمالا (tahdhib)؛ اعترض الفرس في مشيه وفيه عرضية أي اعتراض في مشيه من الصعوبة (mufradat)
- **B013** enine yerleştirme, enine parça ve yana giden ok — çubuğu kabın üzerine enlemesine koymak · tüysüz veya yana doğru giden özel ok · kapı sövelerini üstten tutan enine kiriş
  عرضت العود على الإناء وضعته عليه عرضا (maqayis;ayn;sihah;tahdhib;mufradat)؛ المعراض سهم يمضي عرضا (maqayis;sihah;tahdhib)؛ عارضة الباب والعوارض سقائف المحمل (maqayis;sihah;tahdhib)
- **B014** yön, dağ yolu, bölge adı ve şiir ölçüsü — şiir ölçüsü ve vezin bilimi · yön, dağ yolu veya belirli bölge
  العروض الناحية أو ناحية من العلم (maqayis)؛ العروض ميزان الشعر والعروض طريق في الجبل ومكة والمدينة وما حولهما (sihah)؛ العروض عروض الشعر وأخذ في عروض أي ناحية واستعمل على العروض (tahdhib)

## خ ش ع (root_000412): 42:45 خَٰشِعِينَ

- **B001** boyun eğip dinginleşme — boyun eğip başını ya da bedenini alçaltmak · beden, ses, bakış ve organlarda beliren boyun eğiş ve dinginlik · boyun eğen, kendini alçaltan; kimi kullanımda eğilerek duran · göğsünü eğip alçakgönüllü bir tutum almak · boyun eğişi zorlayarak sergilemek veya öyle görünmeye çalışmak · yalvararak boyun eğen ve kendini alçaltan · alçakgönüllü görünerek başını eğmek · bakışını kısmak veya yere indirmek · seslerin dinip alçalması · içteki yakarışın organların sakin duruşuna yansıması
  أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه؛ الخاشع المستكين والراكع (maqayis)؛ الخشوع رميك ببصرك إلى الأرض؛ متخشع متضرع؛ خشعت الأصوات أي سكنت (ayn)؛ الخاشع المستكين؛ الخاشع الراكع؛ خشع ببصره إذا غضه (jamhara)؛ الخشوع الخضوع؛ التخشع تكلف الخشوع (sihah)؛ التخشع لله الإخبات والتذلل؛ خشع الرجل إذا رمى ببصره إلى الأرض؛ الخشوع في البدن والصوت والبصر (tahdhib)؛ الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح (mufradat)
- **B002** yere yakın arazi parçası — yere yakın arazi parçası veya küçük yükselti · yere yakın, basık sırt veya yükselti · tozlu ve yerleşimsiz yöre · kurumuş, bitkisiz ve cansız toprak · çöküp yerle bir olmuş duvar
  الخشعة قطعة من الأرض قف قد غلبت عليه السهولة؛ قف خاشع لاطئ بالأرض؛ بلدة خاشعة مغبرة (maqayis)؛ الخشعة قف غلبت عليه السهولة؛ أكمة خاشعة لاطئة بالأرض (ayn)؛ الخشعة قطعة من الأرض تغلظ؛ الخاشع المطمئن من الأرض (jamhara)؛ بلدة خاشعة مغبرة؛ مكان خاشع؛ الخشعة أكمة متواضعة (sihah)؛ الحثمة اللاطئة بالأرض هي الخشعة؛ الخشعة الأكمة؛ إذا يبست الأرض ولم تمطر قيل قد خشعت؛ أرض خاشعة هامدة؛ جدار خاشع (tahdhib)
- **B003** görünürlüğü azalıp kaybolmaya yaklaşma [kalıp] — güneşin tutulup kararması · yıldızların ufka inip batmaya yaklaşması
  خشعت الشمس وكسفت وخسفت بمعنى واحد؛ خشوع الكواكب إذا غارت فكادت تغيب في مغيبها؛ خشعت الكواكب إذا دنت من المغيب (tahdhib)
- **B004** hörgücün yağını yitirip çökmesi [kalıp] — devenin hörgücünün yağını yitirip çökmesi
  خشع سنام البعير إذا ذهب إلا أقله (maqayis)؛ خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه (tahdhib)
- **B005** göğüsten yapışkan salgı çıkarmak [kalıp] — göğüsten gelen yapışkan salgıyı çıkarıp atmak
  خشع خراشي صدره إذا ألقى بزاقا لزجا (maqayis)؛ خشع الإنسان خراشي صدره إذا ألقى من صدره بزاقا لزجا (jamhara)؛ خشع الرجل خراشي صدره إذا رمى بها؛ جعل خشع واقعا ولم أسمعه لغيره (tahdhib)

## ذ ل ل (root_000519): 42:45 ٱلذُّلِّ

- **B001** hor ve güçsüz duruma düşüp boyun eğme — horluk içinde boyun eğme · hor düşmüş ve güçsüz kişi · horluk ve güçsüzlük hali · hor düşürülme ve aşağılanma · güçsüz ve korumasız kimseler · onu hor düşürdü · onu boyun eğdirip horladı · onu hor görüp aşağılamaya çalıştı · ona boyun eğdi · adamın yanındakiler güçsüz düştü · aileyi ve malı korumak için bir ölçüde boyun eğmek · acıma duygusuyla ezilmiş gibi boyun eğmek · güçsüzlük yüzünden edinilen koruyucu müttefik
  الخضوع والاستكانة واللين والذل ضد العز (maqayis)؛ الذل ضد العز ورجل ذليل بين الذل والذلة والمذلة (sihah)؛ الذل الخسة ولم يكن له ولي من الذل (tahdhib)؛ الذل ما كان عن قهر (mufradat)
- **B002** değerini yitirmeden gönüllü yumuşaklık [kalıp] — inananlara karşı yumuşak ve sevecen olmak · sevecenlikten gelen yumuşaklık ve uyum
  أذلة على المؤمنين رحماء رفيقين وجانبهم لين ليس أنهم أذلاء مهانون (tahdhib)؛ الذل متى كان من جهة الإنسان نفسه لنفسه فمحمود (mufradat)
- **B003** direnç veya güçlüğün azalıp yönlendirme, erişim ya da kullanıma elverişli hale gelmesi — zorluktan sonra yumuşayıp uysallaşma · uysal ve kolay yönlendirilen · aileyi ve malı koruyan ölçülü yumuşaklık veya eziyete sabır · yürünerek kolay geçilir olmuş yol · meyve salkımlarını sarkıtıp kolay erişilir kılmak · hurma salkımlarını indirip toplamayı kolaylaştırmak · sulanıp ürün vermeye elverişli kılınmış hurma ağaçları · suyun oraya giden yolunu kolaylaştırdı · kolay izlenen yollar veya direnmeden yönelen arılar · uyaklar ozan için kolaylaştı · huysuzluktan sonra uysallaşan binek
  الذل خلاف الصعوبة ودابة ذلول وذلل القطف تذليلا إذا لان وتدلى (maqayis)؛ الذل بالكسر اللين ضد الصعوبة ودابة ذلول وذللت قطوفها (sihah)؛ طريق مذلل إذا كان موطوءا سهلا وسبل ربك ذللا وذللت قطوفها وتسهيل القوافي (tahdhib)؛ الذل ما كان بعد تصعب وشماس وذلت الدابة وسبل ربك ذللا وذللت قطوفها (mufradat)
- **B004** işleri uygun akışında yürütme [kalıp] — işleri kendi uygun yolu ve halinde yürütmek · kendi hali veya yönü üzere
  أجر الأمور على أذلالها أي استقامتها (maqayis)؛ جاء على أذلاله أي على وجهه وأمور الله جارية على أذلالها أي على مجاريها وطرقها (sihah)؛ أجر الأمور على أذلالها أي على أحوالها التي تصلح عليها وتتيسر وتسهل وعلى أذلاله أي على وجهه (tahdhib)؛ الأمور تجري على أذلالها أي مسالكها وطرقها (mufradat)
- **B005** aşağı sarkan alt bölüm ve fiziksel kısalık — gömleğin yere yakın sarkan etek uçları · gömleğin tek bir alt etek ucu · kısa veya alçak duvar, ev ve mızrak
  ذلاذل القميص ما يلي الأرض من أسافله (maqayis)؛ ذلاذل القميص ما يلي الأرض من أسافله وقصر الذلاذل (sihah)؛ حائط ذليل أي قصير وبيت ذليل قصير السمك ورمح ذليل قصير والذلاذل أسافل القميص الطويل (tahdhib)
- **B006** başı darbeyle yarılan kazık [kalıp] — başı darbelerle yarılan kazık
  عير المذلة الوتد لأنه يشج رأسه (sihah)
- **B007** belirli fiil biçiminde hızla ilerleme — adam hızla ilerledi
  اذلولى الرجل إذليلاء إذا أسرع وهو من الباب (maqayis)

## ن ظ ر (root_001520): 42:45 يَنظُرُونَ

- **B001** bakıp inceleme — bakma ve inceleme · bir şeye bakıp onu görmek · bir konuyu düşünüp incelemek · bakanlar veya seyredenler
  تأمل الشيء ومعاينته؛ نظرت إلى الشيء إذا عاينته (maqayis)؛ النظر تأمل الشئ بالعين (sihah)؛ نظر العين ونظر القلب؛ نظرت في الأمر احتمل أن يكون تفكرا وتدبرا بالقلب (tahdhib)؛ تقليب البصر والبصيرة لإدراك الشيء ورؤيته؛ التأمل والفحص؛ المعرفة الحاصلة بعد الفحص؛ مشاهدون؛ تعتبرون (mufradat)
- **B002** bekleme veya süre tanıma — onu beklemek · bekleme · durup beklemek · ona süre verip ertelemek · ondan ek süre istemek · bekleyip geleceğini gözetmek · erteleme ve geciktirme · süre verme ve erteleme · bekle · önce Tanrı'dan, sonra senden iyilik umarım · kendisinden iyilik umulan
  نظرته أي انتظرته؛ ينظر إلى الوقت الذي يأتي فيه (maqayis)؛ النظر الانتظار؛ النظرة التأخير؛ أنظرته أي أخرته؛ استنظره أي استمهله (sihah)؛ إنما أنظر إلى الله ثم إليك أي أتوقع فضل الله ثم فضلك؛ أنظرني أي انتظرني قليلا؛ أمهلته؛ النظرة إنظار (tahdhib)؛ النظر الانتظار؛ نظرته وانتظرته وأنظرته أي أخرته (mufradat)
- **B003** görüş doğrultusunda karşı karşıya olma [kalıp] — birbirini görebilen komşu topluluk · evim onun evine bakar ve karşısındadır · dağ yol üzerinde karşına çıktı
  حي حلال نظر متجاورون ينظر بعضهم إلى بعض (maqayis)؛ حي حلال ونظر أي متجاورون يرى بعضهم بعضا؛ داري تنظر إلى دار فلان؛ دورنا تناظر أي تقابل؛ فنظر إليك الجبل (sihah)؛ داري تنظر إلى دار فلان ودورنا تناظر إذا كانت متحاذية (tahdhib)؛ حي نظر أي متجاورون يرى بعضهم بعضا (mufradat)
- **B004** bakıldığında görülen dış görünüş — toprak bitkisini gösterdi · bakıldığında görülen dış görünüş · güzel dış görünüş · bakılması ve dinlenmesi hoş bir durumda
  نظرت الأرض أرت نباتها (maqayis)؛ منظره خير من مخبره؛ حسنة المنظر والمنظرة (sihah)؛ المنظرة منظر الرجل إذا نظرت إليه فأعجبك أو ساءك؛ ذو منظرة بلا مخبرة؛ المنظر الشيء الذي يعجب الناظر إذا نظر إليه فسره؛ في منظر ومستمع (tahdhib)
- **B005** zamanın vurup yok etmesi [kalıp] — zaman onları vurup yok etti
  نظر الدهر إلى بني فلان فأهلكهم (maqayis;sihah)؛ نظر الدهر إليهم فابتهل؛ خانهم فأهلكهم (mufradat)
- **B006** eş veya denk karşılık — eş, benzer veya denk karşılık · birbirine benzeyen eşler · Tanrı'nın kitabına hiçbir şeyi denk tutma · ikişer ikişer sayılan develer
  هذا نظير هذا؛ إذا نظر إليه وإلى نظيره كانا سواء (maqayis)؛ نظير الشئ مثله؛ النظر والنظير بمعنى واحد مثل الند والنديد؛ نظائر (sihah)؛ فلان نظيرك أي مثلك؛ النظائر لاشتباه بعضها ببعض؛ لا تجعل شيئا نظيرا (tahdhib)؛ النظير المثيل وأصله المناظر (mufradat)
- **B007** özel adlandırma kümesi — hızlı bir bakış · bakıştan doğan heybet · onda solgunluk, çirkinlik veya kusur var · görünmeyen varlıkların kem gözünden etkilenmiş · kem gözden zarar görmüş kişi
  به نظرة أي شحوب (maqayis)؛ النظرة عين الجن؛ رجل فيه نظرة أي شحوب (sihah)؛ النظرة اللمحة بالعجلة؛ النظرة الهيبة؛ فيه نظرة أي شحوب؛ النظرة الشنعة والقبح؛ فيه نظرة أي قبح؛ بها إصابة عين من نظر الجن (tahdhib)؛ به نظرة؛ من أعين الجن نظرة (mufradat)
- **B008** biçime bağlı adlandırmalar — göz bebeği veya gözdeki küçük siyah bölüm · göz · gözyaşı yolunda burnun iki yanındaki damarlar
  الناظر في المقلة السواد الأصغر؛ يقال للعين الناظرة؛ الناظران عرقان في مجرى الدمع على الأنف من جانبيه (sihah)؛ ناظر العين النقطة السوداء الصافية؛ الناظر في العين كالمرآة؛ الناظران عرقان مكتنفا الأنف؛ هما عرقان في مجرى الدمع (tahdhib)
- **B009** biçime bağlı adlandırmalar — bağ bekçisi · koruyucu veya inceleme için gönderilen görevli · yüksek gözetleme yeri · suçsuzluğundan gözünü kaçırmadan bakan
  الناطر والناطور حافظ الكرم؛ الناظر الحافظ؛ المنظرة المرقبة (sihah)؛ المنظرة موضع في رأس جبل فيه رقيب ينظر العدو ويحرسه؛ شديد الناظر إذا كان بريئا من التهمة؛ بعث ناظرا (tahdhib)
- **B010** karşılıklı tartışıp inceleme — karşılıklı tartışıp inceleme · araştırma ve kanıta dayalı inceleme
  ناظره من المناظرة (sihah)؛ المناظرة أن تناظر أخاك في أمر إذا نظرتما فيه معا كيف تأتيانه؛ نظيرك أيضا الذي يناظرك وتناظره (tahdhib)؛ المناظرة المباحثة والمباراة في النظر واستحضار كل ما يراه ببصيرته؛ النظر البحث (mufradat)
- **B011** merhametle iyilik yöneltme — merhamet · Tanrı kullarına iyilik etti ve iyiliklerini bolca verdi
  النظرة الرحمة (tahdhib)؛ نظر الله تعالى إلى عباده هو إحسانه إليهم وإفاضة نعمه عليهم (mufradat)
- **B012** bakıp da görememe ve kavrayamama [kalıp] — bakıyorlar ama göremiyor ve kavrayamıyorlar
  يستعمل النظر في التحير في الأمور؛ ينظرون إليك وهم لا يبصرون؛ نظر عن تحير دال على قلة الغناء (mufradat)

## ط ر ف (root_000931): 42:45 طَرْفٍ

- **B001** kenar, uç veya yan — kenar, uç, yan veya yön · uçlar, kenarlar veya yönler · iki tarafından hangisinin üstün olduğu bilinmez · ekinin uçlarından alınan bölüm · burnunda ve kuyruğunda birer iğne bulunan yılan
  طرف الشيء والثوب والحائط (maqayis)؛ الطرف الناحية من النواحي والطائفة من الشئ (sihah)؛ أطراف الأرض نواحيها وأطراف النهار ساعاته وأطراف الأصابع (tahdhib)؛ طرف الشيء جانبه ويستعمل في الأجسام والأوقات (mufradat)؛ كريم الطرفين أي الأب والأم وقيل الذكر واللسان (mufradat)
- **B002** göz kırpma ve bakış — göz kırpma veya göz kapaklarını kapatma · göz, görme veya bakış · bakışlarını indirenler · aslanın gözleri sayılan iki yıldız · gözler
  الطرف تحريك الجفون في النظر (maqayis;ayn;tahdhib)؛ الطرف العين (sihah)؛ الطرف اسم جامع للبصر (ayn;tahdhib)؛ طرف بصره إذا أطبق أحد جفنيه على الآخر (sihah)؛ طرف العين جفنه والطرف تحريك الجفن وعبر به عن النظر (mufradat)
- **B003** gözü etkileyip yaşartma — erkeklere gözü kayan veya bir erkeğe bağlı kalmayan kadın · gözüne bir şey değdi ve gözü yaşardı · bir şeyin değmesiyle yaşaran göz · keder onu ağlatıp gözünü etkiledi · çokluğu veya şaşırtıcılığıyla gözü hayrete düşüren şey
  عين مطروفة يصيبها طرف شيء ثوب أو غيره فتغرورق دمعا وطرفها الحزن (maqayis)؛ الطرف إصابتك عينا بثوب أو غيره وطرفها الحزن بالبكاء (ayn)؛ طرفت عينه إذا أصبتها بشئ فدمعت والطرفة نقطة حمراء من الدم (sihah)؛ الدنيا قد طرفت أعينكم ومطروفة العينين (tahdhib)؛ طرف فلان أصيب طرفه (mufradat)؛ جاء فلان بطارفة عين أي بشيء تتحير له العين من كثرته (maqayis)؛ جاء فلان بطارفة عين إذا جاء بمال كثير (sihah)
- **B004** soylu ve köklü — anne ve baba tarafından soylu · yakın akrabalar veya seçkinler · iki tarafından hangisinin üstün olduğu bilinmez · soylu at, soylu kişi veya köklü soy
  هو كريم الطرفين يراد به نسب الأب والأم (maqayis;sihah;tahdhib;mufradat)؛ أطرافه أبواه وإخوته وأعمامه وكل قريب له محرم (sihah;tahdhib)؛ الأطراف بمعنى الأشراف (sihah;tahdhib)؛ الطرف الفرس الكريم (maqayis;sihah;tahdhib)؛ فلان طريف النسب (tahdhib)
- **B005** yeni veya yeni edinilmiş — yeni şey veya yeni edinilmiş mal · yenisini edinmek veya yeni satın almak · yeni edinilip beğenilen şey
  الشيء المستحدث طريف وهو خلاف التليد واطرفت الشيء إذا استحدثته (maqayis)؛ اطرفت الشئ أي اشتريته حديثا والطارف والطريف من المال المستحدث وهو خلاف التالد والتليد (sihah)؛ هل وراك طريفة خبر تطرفنا والطرفة كل شيء استحدثته فأعجبك (tahdhib)؛ وقد أطرفت مالا والطريف ما يتناوله (mufradat)
- **B006** bir yerde durmayıp yenisine yönelme — otlak kenarlarında veya çayırlar arasında dolaşan deve · eşine, arkadaşına veya sözüne bağlı kalmayan kişi · erkeklere gözü kayan veya bir erkeğe bağlı kalmayan kadın
  ناقة طرفة ترعى أطراف المرعى ولا تختلط بالنوق (maqayis)؛ الرجل الطرف الذي لا يثبت على امرأة ولا صاحب والمرأة المطروفة لا تثبت على رجل (maqayis)؛ ناقة طرفة لا تثبت على مرعى واحد ورجل طرف لا يثبت على امرأة ولا على صاحب (sihah)؛ ناقة طرفة إذا كانت تطرف الرياض روضة بعد روضة ورجل طرف وامرأة طرفة إذا كانا لا يثبتان على عهد (tahdhib)؛ ناقة طرفة ومستطرفة ترعى أطراف المرعى (mufradat)
- **B007** çadır kenarı ve uçları işaretli giysi — çadırın dışarı bakmak için kaldırılan yanları · uçlarında iki işaret veya bordür bulunan giysi · deriden yapılmış çadır
  الطوارف من الخباء ما رفعت من جوانبه لتنظر (maqayis;sihah;tahdhib)؛ المطرف من الثياب ما جعل في طرفيه علمان (sihah;tahdhib)؛ الطراف بيت من أدم (maqayis;sihah;tahdhib)؛ الطراف بيت أدم يؤخذ طرفه ومطرف الخز ما يجعل له طرف (mufradat)
- **B008** uçları farklı renkte — uçları gövdesinden farklı renkte hayvan · kız parmak uçlarını boya ile renklendirdi
  المطرف من الخيل هو الأبيض الرأس والذنب وسائر جسده يخالف ذلك (sihah)؛ نعجة مطرفة وهي التي اسودت أطراف أذنيها وسائرها أبيض (tahdhib)؛ طرفت الجارية بنانها إذا خصبت أطراف أصابعها بالحناء (tahdhib)
- **B009** çevirip geri püskürtme — onu bir şeyden çevirip geri döndürdü · ordunun uç kesiminde savaşıp karşıdakileri geri sürdü · birini arkadaşlarının gerisinden geri çevirme
  طرفه عنه أي صرفه ورده (sihah)؛ طرف فلان إذا قاتل حول العسكر لأنه يحمل على طرف منهم فيردهم إلى الجمهور (sihah)؛ طرفت فلانا إذا صرفته عن شيء (tahdhib)؛ التطريف أن يرد الرجل الرجل عن أخريات أصحابه (tahdhib)
- **B010** belirli ağaç ve olgun ot adları — belirli ağaç topluluğu ve onun tek ağacı · olgunlaşıp beyazlaşmış belirli ot · bu otun bol bulunduğu arazi
  الطرفاء شجر والواحدة طرفة (sihah)؛ الطريفة النصى إذا ابيض وأرض مطروفة كثيرة الطريفة (sihah)؛ الطرف اسم يجمع الطرفاء والواحدة طرفة (tahdhib)؛ الطريفة من النصي والصليان إذا أعتما وتما وقد أطرفت الأرض (tahdhib)

## خ ف ي (root_000428): 42:45 خَفِىٍّ

- **B001** gizli kalma ya da gizleme — şey gizli kaldı, görünmedi · şeyi ve onun haberini sakladı · şeyi gizledi ve sakladı · gizlilik ve saklılık hâli · gizlilik, görünmezlik · gizlenip gözden uzaklaştı · bir aktarıma göre gizlendi · gizlenen kişi · onunla gizlice buluştum
  خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته (maqayis); أخفيت الصوت إخفاء وفعله اللازم اختفى والخافية ضد العلانية ولقيته خفيا أي سرا (ayn); خفيت الشئ أخفيه كتمته وأخفيت الشئ سترته وكتمته واستخفيت منك أي تواريت (sihah); خفي الشيء خفية استتر وأخفيته أوليته خفاء وذلك إذا سترته ويقابل به الإبداء والإعلان (mufradat)
- **B002** örten ya da gizli kalan şey — gizli ya da örtülü şey · örtü veya örten giysi · kanadın iç tüyleri; hurma göbeğine yakın yapraklar · görünmeyen varlık · kanadın iç tüylerinden biri · bedende gizlendiğine inanılan görünmeyen varlık · kuyu, koruluk veya gizli yer · bu adla anılan iki aslan yatağı · su tulumunun üzerine atılan örtüler · kadının sesi ile yerdeki ayak izi
  الخوافي سعفات يلين قلب النخلة والخافي الجن (maqayis); الخفا مقصور الشيء الخافي والموضع الخافي والخفاء رداء تلبسه المرأة وكل شيء غطيت به شيئا فهو خفاء والخفية غيضة والخفية بئر والخوافي من الجناحين (ayn); الخافي الجن والخافية ما يخفى في البدن من الجن والخفية الركية والخوافى ما دون الريشات العشر والخوافي من السعف (sihah); الخفاء ما يستر به كالغطاء والخوافي جمع خافية وهي ما دون القوادم من الريش (mufradat)
- **B003** gizliliği giderip açığa çıkarma — gizli olan açığa çıktı, sır belli oldu · şeyi açığa çıkardı · şeyin gizliliğini giderip onu gösterdi · yağmur fareleri yuvalarından çıkardı · gizli şeyi çıkarıp ortaya koydu · kefenleri çıkardığı için mezar soyguncusu
  الأصل الآخر الإظهار وخفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن (maqayis); الخفا إخراجك الشيء الخفي وإظهاركه وخفيت الخرزة من تحت التراب أخفيها خفيا (ayn); وخفيته أيضا أظهرته وهو من الأضداد وخفى المطر الفأر إذا أخرجهن واستخفيت الشئ أي استخرجته وأخفيها أي أزيل عنها خفاءها (sihah); وخفيته أزلت خفاه وذلك إذا أظهرته (mufradat)
- **B004** belli belirsiz şimşek çakması — şimşek belli belirsiz ve zayıfça çaktı
  خفا البرق خفوا إذا لمع ويكون ذلك في أدنى ضعف (maqayis); وخفا البرق يخفو خفوا ويخفى خفيا أي ظهر من الغيم (ayn); خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا (jamhara); وخفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم (sihah)

## خ س ر (root_000409): 42:45 ٱلْخَٰسِرِينَ, 42:45 خَسِرُوٓا۟

- **B001** eksilme ve değer yitimi — eksilme ve değerden düşme · eksilme, azalma ve değer yitimi · azalmak veya bir eksilmeye uğramak · eksilme ya da eksik kalan sonuç
  أصل واحد يدل على النقض (maqayis); الخسر النقصان والخسران كذلك (ayn;tahdhib); خسر إذا نقص ميزانا أو غيره (tahdhib)
- **B002** alım satımda kazanç sağlayamama veya anaparadan yitirme — satıcının anaparasından yitirmesi veya kazanç sağlayamaması · satışta kazanç sağlayamamak · alışverişinde kazanç sağlayamayan veya anaparasından yitiren kişi · alım satımda kazanç sağlayamama ya da anaparadan yitirme · kazanç getirmeyen alışveriş · alışveriş işinin kazanç getirmemesi veya anaparayı eksiltmesi
  الخاسر الذي وضع في تجارته (ayn;tahdhib); خسر التاجر إذا وضع من رأس ماله (jamhara); خسر في البيع خسرا وخسرانا (sihah); انتقاص رأس المال (mufradat); صفقة خاسرة أي غير مربحة (ayn;tahdhib)
- **B003** ölçü ve tartıda eksiltme — teraziyi veya tartılan şeyi eksik bırakmak · ölçerken ya da tartarken eksik vermek · verirken eksik ölçüp alırken daha çoğunu isteyen kişi · ölçü ve tartıda eksiltmeyin, haksızlık etmeyin
  خسرت الميزان وأخسرته إذا نقصته (maqayis); كلته ووزنته فأخسرته أي نقصته (ayn;tahdhib); أخسرت الميزان وخسرته (tahdhib); خسرت الشيء وأخسرته نقصته (sihah); ولا تخسروا الميزان (mufradat); ينقصون في الكيل والوزن (tahdhib)
- **B004** doğru yoldan sapıp iyiliklerini yitirerek yıkıma düşme — doğru yoldan sapma ve yıkıma uğrama · sapma, yitim ve yıkım · maddi olmayan iyilikleri de kapsayan yitim ve yıkım · yıkıma uğramak · yıkıma uğratma veya iyilikten uzaklaştırma · bu dünyadaki ve öte dünyadaki kazanımlarını yitirmek · kendilerini ve yakınlarını yitirmek · yarar sağlamayan dönüş · yaptıkları en çok boşa giden
  الخسر والخسار والخسران واحد وهو الضلال (jamhara); التخسير الإهلاك (sihah); الخسار والخسارة والخيسرى الضلال والهلاك (sihah); خسر إذا هلك (tahdhib); لفي عقوبة بذنوبه (tahdhib); غير إبعاد من الخير (tahdhib); المقتنيات النفسية كالصحة والسلامة والعقل والإيمان والثواب (mufradat)
- **B005** yitim, yıkım veya güçsüz kişileri bildiren genişlemiş biçimler — yitim veya kayıp bildiren genişlemiş biçim · yitim ya da yıkım bildiren genişlemiş biçim · güçsüz veya aşağı görülen insanlar · tekili bulunmayan, yıkım anlamındaki çoğul biçim
  رجل خنسرى وقالوا خيسرى في موضع الخسران النون والياء زائدتان (jamhara); الخناسر جمع خنسر وهو نحو الخنسرى وفي معناه وهم لئام الناس ورذالهم (jamhara); الخناسر الضعاف من الناس (jamhara); الخناسير الهلاك لا واحد له (sihah)

## ء ه ل (root_000064): 42:45 وَأَهْلِيهِمْ

- **B001** yakın çevre ve bağlı topluluk — yakınlık, ev, din veya başka bir bağla birleşen insan çevresi · bir erkeğin eşi ve en yakın insanları · evin sakinleri ve eve bağlı sayılan kişiler · Islam'a bağlı olan kişiler · yakın çevre veya ev halkı için çoğul biçimler
  أهل الرجل زوجه وأخص الناس به؛ أهل البيت سكانه؛ أهل الإسلام من يدين به (maqayis;ayn;tahdhib)؛ أهل الرجل من يجمعه وإياهم نسب أو دين أو صناعة وبيت وبلد (mufradat)؛ أهل الرجال وأهل الدار (sihah)
- **B002** evlenip yakın çevre edinmek — evlenmek ve eş edinmek · bir kadını eş olarak almak · Allah sana cennette eş ve yakın çevre versin
  التأهل التزوج (maqayis;ayn)؛ أهل فلان يأهل أهولا أي تزوج وكذلك تأهل (sihah)؛ أهل الرجل يأهل أهولا إذا تزوج للأنس الذي بين الزوجين (tahdhib)؛ تأهل إذا تزوج ومنه آهلك الله في الجنة أي زوجك فيها وجعل لك فيها أهلا (mufradat)
- **B003** uygun ve layık olmak — bir şey için uygun ve yaraşır olmak · saygı gösterilmeye ve bağışlamaya layık olan · onu bu iş için uygun ve hazır hale getirdi · bu işi hak etmiş sayılan kimse; kullanımı tartışmalı
  أهلته لهذا الأمر تأهيلا (maqayis;ayn;tahdhib)؛ فلان أهل كذا أو كذا (ayn;tahdhib)؛ هو أهل التقوى وأهل المغفرة أي أهل لأن يتقى وأهل لمغفرة من اتقاه (ayn;tahdhib)؛ فلان أهل لكذا أي خليق به (mufradat)؛ فلان أهل لكذا ولا تقل مستأهل (sihah)
- **B004** sakinli ve alışılmış yerleşiklik — sakinleri bulunan yer · içinde yaşayanları olan yer · eskiden içinde yaşanmış konaklama yerleri · insanlara ve yerleşim yerlerine alışmış, evcil · onunla yakınlık duydum ve yabancılık çekmedim · insanları ve sakinleri bulunan hale geldi
  مكان آهل مأهول (maqayis)؛ مكان مأهول فيه أهل ومكان آهل له أهل (ayn;tahdhib)؛ منزل آهل أي به أهله (sihah)؛ كل شيء من الدواب وغيرها إذا ألف مكانا فهو آهل وأهلي (maqayis;tahdhib)؛ كل دابة ألف مكانا يقال أهل وأهلي (mufradat)؛ أهلت به إذا استأنست به (sihah;tahdhib)
- **B005** rahatlatan karşılama sözü — geniş yer ve yakın insanlar buldun; rahat ol, yabancılık çekme
  مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش (sihah)؛ مرحبا وأهلا ومعناه نزلت رحبا أي سعة وأتيت أهلا لا غرباء (tahdhib)؛ مرحبا وأهلا في التحية للنازل بالإنسان أي وجدت سعة مكان عندنا (mufradat)
- **B006** eritilmiş yemeklik yağ — kuyruk yağı, iç yağı, don yağı, sıvı yağ veya katık yapılan yağlı madde · bu yağlı maddeden alan veya onu yiyen kimse · bu yağlı maddeyi yemeğe katık yaptı
  الأصل الآخر الإهالة وهي الألية ونحوها يؤخذ فيقطع ويذاب (maqayis)؛ الإهالة الودك والمستأهل الذي يأخذ الإهالة أو يأكلها (sihah)؛ الإهالة هي الشحم والزيت قط؛ كل ما اؤتدم به من زبد وودك شحم ودهن سمسم وغيره فهو إهالة؛ استأهل الرجل إذا ائتدم بالإهالة (tahdhib)

## ل ج ء (root_001343): 42:47 مَّلْجَإٍ

- **B001** sığınma ve sığınılan korunak — bir yere sığınmak · ona sığınmak · sığınma · sığınılan yer ya da şey · sığınak · korunak, sığınılan yer · bir şeyi sığınakta koruma altına almak
  اللجأ والملجأ المكان يلتجأ إليه (maqayis)؛ لجأت إليه والتجأت إليه والموضع أيضا لجأ وملجأ (sihah)؛ لجأت إلى المكان وألجأت الشيء إذا حصنته في ملجأ ولجاء (tahdhib)
- **B002** birini bir işe zorlamak — birini bir şeye zorlamak · zorlama
  التلجئة الإكراه وألجأته إلى الشئ اضطررته إليه (sihah)؛ ألجأت فلانا إلى الشيء إلجاء إذا اضطررته وألجأته إلى كذا أي اضطررته (tahdhib)
- **B003** işini Tanrı'ya bırakmak [kalıp] — işini Tanrı'ya bırakmak
  ألجأت أمري إلى الله أسندت
- **B004** birine görünüşü gerçeğinden farklı işlem yaptırma veya malı böyle düzenleme — iç yüzü görünüşünden farklı bir işlem yaptırma · malını bağış görünümünde mirasçılarından yalnız bir kısmına ayırmak
  التلجئة أن يلجئك أن تأتي أمرا باطنه خلاف ظاهره؛ لجأ فلان ماله؛ التلجئة أن يجعله لبعض ورثته دون بعض كأنه يتصدق به عليه وهو وارثه
- **B005** eş olan kadın — eş olan kadın
  ألك لجأ يا فلان؟ واللجأ الزوجة

## ن ك ر (root_001550): 42:47 نَّكِيرٍ

- **B001** tanımama ve tanınmış saymama — tanımamak; içten veya sözle kabul etmemek · tanımamak ya da yadsımak · yadırgayarak sormak veya karşı çıkmak · tanınmayan ya da belirsiz olan · yadsıma ve kabul etmeme · birbirini tanımıyormuş gibi davranma
  خلاف المعرفة التي يسكن إليها القلب (maqayis)؛ نكر الشيء وأنكره لم يقبله قلبه ولم يعترف به لسانه (maqayis)؛ النكرة نقيض المعرفة (ayn;tahdhib)؛ النكرة ضد المعرفة (sihah)؛ الإنكار ضد العرفان (mufradat)؛ الإنكار خلاف الاعتراف (maqayis)
- **B002** uyanıklık ve ince kavrayış — uyanıklık ve ince kavrayış · uyanık ve işbilir adam · uyanık ve işbilir adam · uyanık ve aklı başında kimse · işbilir uyanıklık
  النكر الدهاء (maqayis;ayn;tahdhib;mufradat)؛ رجل نكر ورجل منكر داه (ayn;sihah;tahdhib)؛ النكارة الدهاء (sihah)
- **B003** çetin ve yadırgatıcı durum — çetin ve ağır durum · tanınması güç, çetin iş · işin güçleşip ağırlaşması
  النكراء الأمر الصعب الشديد (maqayis)؛ النكر نعت للأمر الشديد (ayn;tahdhib)؛ النكر المنكر (sihah)؛ الأمر الصعب الذي لا يعرف (mufradat)؛ نكر الأمر نكارة (maqayis;sihah;mufradat)
- **B004** tanınmazlaştırma veya kötüleşme — iyi bir durumdan kötü bir duruma dönüşme · değiştirip tanınmaz hale getirmek · bir şeyi tanınmaz hale getirme
  التنكر التنقل من حال تسر إلى أخرى تكره (maqayis)؛ نكره فتنكر أي غيره فتغير إلى مجهول (sihah)؛ التنكر التغير عن حال تسرك إلى حال تكرهها (tahdhib)؛ تنكير الشيء جعله بحيث لا يعرف (mufradat)
- **B005** kanlı ya da irinli bedensel akıntı — bedenden çıkan kanlı ya da irinli akıntı · kan ve cerahat boşaltmak
  لما يخرج من الحولاء من دم وما أشبهه نكرة (maqayis)؛ النكرة اسم لما خرج من الحولاء وهو الخراج من قيح ودم كالصديد وكذلك من الزجير (tahdhib)؛ أسهل فلان نكرة ودما (tahdhib)
- **B006** çirkin bulunan eylem ve onu engelleme — aklın çirkin bulduğu, geri çevrilmesi gereken eylem · kötü eylemi değiştirme veya yapanı caydırma · kötü eylemi değiştirme ve caydırma · birini yaptığı kötülükten caydıracak biçimde davranmak · seslerin en çirkini
  المنكر واحد المناكر (sihah)؛ النكير والإنكار تغيير المنكر (sihah)؛ المنكر كل فعل تحكم العقول الصحيحة بقبحه (mufradat)؛ نكرت على فلان وأنكرت إذا فعلت به فعلا يردعه (mufradat)؛ النكير اسم للإنكار الذي معناه التغيير (tahdhib)؛ أنكر الأصوات أقبح الأصوات (tahdhib)
- **B007** karşılıklı düşmanlık ve çatışma — karşılıklı düşmanlık ve çatışma · onunla savaşmak ya da ona düşmanlık etmek · birbirine düşman olup çatışmak
  ناكره أي قاتله (sihah)؛ المناكرة المحاربة (tahdhib)؛ بينهما مناكَرة أي معاداة وقتال (tahdhib)؛ استعيرت المناكرة للمحاربة (mufradat)

## ر س ل (root_000563): 42:48 أَرْسَلْنَٰكَ, 42:51 يُرْسِلَ, 42:51 رَسُولًا

- **B001** bir şeyi gönderme veya serbest bırakma — göndermek veya salıvermek · gönderme, yöneltme veya serbest bırakma · gönderilmiş rüzgarlar veya görevlendirilmiş melekler
  أصل واحد يدل على الانبعاث والامتداد (maqayis)؛ أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة (sihah)؛ إرسال الله أنبياءه وإرسال الشياطين تخليتهم وإياهم (tahdhib)؛ الإرسال يقابل الإمساك (mufradat)
- **B002** haber taşıyıcısı veya taşınan haber — elçi veya haberci · taşınan ileti veya haber · ileti veya taşınan haber · iletiler veya taşınan haberler · elçiler veya haberciler
  الرسول معروف (maqayis)؛ الرسول بمعنى الرسالة والرسائل جمع الرسالة (ayn)؛ أرسلت فلانا في رسالة فهو مرسل ورسول والرسول أيضا الرسالة (sihah)؛ الرسول معناه الذي يتابع أخبار الذي بعثه (tahdhib)؛ الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة (mufradat)
- **B003** harekette veya uzanışta yumuşak akıcılık — rahat ve yumuşak ilerleyiş · rahat yürüyen, bacakları ve eklemleri yumuşak dişi deve · rahat yürüyen deve · düz ve salık saç · saçın düzleşip salık duruma gelmesi · hızlı veya rahatça ilerleyen deve sürüleri · uzun ya da yumuşak ve rahat hareketli bacaklar
  فالرسل السير السهل وناقة رسلة لينة المفاصل وشعر رسل (maqayis)؛ ناقة رسلة القوائم سلسة لينة المفاصل (ayn)؛ شعر رسل وبعير رسل وناقة رسلة وإبل مراسيل (sihah)؛ الرسل الذي فيه لين واسترخاء وناقة مرسال رسلة القوائم (tahdhib)؛ ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا (mufradat)
- **B004** acele etmeden ölçülü ilerleme — Acele etme; yavaş ve sakin ol · işte veya konuşmada sakin, ağırbaşlı ve temkinli davranma · metni acele etmeden açık seçik okuma
  على رسلك أي على هينتك (maqayis)؛ تكلم على رسلك والترسل في الأمر والمنطق كالتمهل والتوقر والتثبت (ayn)؛ على رسلك أي اتئد فيه وترسل في قراءته (sihah)؛ الترسل من الرسل في الأمور والمنطق كالتمهل والتوقر والتثبت والترسيل التحقيق بلا عجلة (tahdhib)؛ على رسلك إذا أمرته بالرفق (mufradat)
- **B005** peş peşe gelen topluluklar — deve, koyun veya başka varlıklardan oluşan sürü · gruplar halinde, birbirinin ardından
  الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا (maqayis)؛ الرسل القطيع من كل شيء وجمعه أرسال (ayn)؛ الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا (sihah)؛ جاءت الإبل أرسالا رسل بعد رسل والرسل قطيع من الإبل (tahdhib)؛ جاءوا أرسالا أي متتابعين (mufradat)
- **B006** bol ve sürekli gelen süt — süt; özellikle bol ve sürekli gelen süt · hayvanlarından süt elde eder duruma gelmek
  الرِّسل اللبن لأنه يترسل من الضرع (maqayis)؛ والرسل اللبن (ayn)؛ والرسل أيضا اللبن وقد أرسل القوم أي صار لهم اللبن (sihah)؛ كثر الرسل العام أي كثر اللبن (tahdhib)؛ الرسل اللبن الكثير المتتابع الدر (mufradat)
- **B007** ısınıp güvenerek açılma — birine veya bir şeye ısınıp güvenmek · sana güvenip yanında rahat davranan kimse
  استرسلت إلى الشيء إذا انبعثت نفسك إليه وأنست (maqayis)؛ الاسترسال إلى شيء كالاستئناس والطمأنينة (ayn)؛ استرسل إليه أي انبسط واستأنس (sihah)؛ الاسترسال إلى الإنسان كالاستئناس والطمأنينة (tahdhib)
- **B008** karşılıklı iletişim ve eşlik — karşılıklı haberleşmek veya birbirine ayak uydurmak · atışmada veya başka bir uğraşta eşlik eden kişi · şarkıda veya işte bir öncekinin ardından giden eşlikçi
  رسيل الرجل الذي يقف معه في نضال أو غيره (maqayis)؛ راسله مراسلة فهو مراسل ورسيل الرجل الذي يراسله في نضال أو غيره (sihah)؛ العرب تسمي المراسل في الغناء والعمل المتالي (tahdhib)
- **B009** taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın [kalıp] — eşi ölmüş, boşanmış veya ayrılmak üzere olduğu için taliplerin haber gönderdiği kadın
  المرأة المراسل التي مات بعلها فالخطاب يراسلونها (maqayis)؛ امرأة مراسل كان لها زوج والخطاب يراسلونها الخطبة (ayn)؛ امرأة مراسل يموت زوجها أو أحست منه أنه يريد تطليقها (sihah)؛ امرأة مراسل وهي التي مات عنها زوجها أو طلقها (tahdhib)
- **B010** rahatlık ve gönül hoşluğuyla verme [kalıp] — sıkıntısında ve rahatlığında; gönül hoşluğuyla verirken
  النجدة الشدة والرسل الرخاء (maqayis)؛ في نجدتها ورسلها يريد الشدة والرخاء (sihah)؛ إلا من أعطى في رسلها أي بطيب نفس منه (tahdhib)
- **B011** özel adlandırma kümesi — kısa ok · iki damar · belirli bir topluluğun damızlık erkek devesi · aktarım zinciri kesintili söz · boncuklu kolye · başını henüz örtmeyen küçük kız
  الراسلان عرقان (maqayis)؛ المرسال سهم قصير (sihah)؛ هذا رسيل بني فلان أي فحل إبلهم وحديث مرسل والمرسلة القلادة وجارية رسل (tahdhib)

## ب ل غ (root_000151): 42:48 ٱلْبَلَٰغُ

- **B001** bir yere, şeye veya son sınıra ulaşma; bağlama göre yaklaşma ya da olgunluğa erme — yere veya şeye ulaşmak · yer, zaman veya iş bakımından en son sınıra varma · belirlenmiş sürenin sonuna yaklaşmak · çocuğun olgunluk çağına erişmesi · güç veya yaş bakımından belirlenmiş sınıra erişmek
  الوصول إلى الشيء؛ بلغت المكان إذا وصلت إليه (maqayis;sihah)؛ بلغت المكان بلوغا وصلت إليه (sihah)؛ بلغ الشيء يبلغ بلوغا (ayn)؛ البلوغ والبلاغ الانتهاء إلى أقصى المقصد والمنتهى مكانا كان أو زمانا أو أمرا (mufradat)؛ المشارفة بلوغا بحق المقاربة (maqayis)؛ بلغ الغلام أدرك (sihah)
- **B002** bir şeyi, özellikle iletiyi, hedefine ulaştırma — ulaştırmak veya erişmesini sağlamak · iletiyi yerine ulaştırmak · iletme ve ulaştırma işi
  أبلغته إبلاغا؛ بلغته تبليغا في الرسالة ونحوها (ayn)؛ بلغت الرسالة تبليغا (jamhara)؛ الإبلاغ الإيصال وكذلك التبليغ؛ بلغت الرسالة (sihah)
- **B003** yaşamı sürdürmeye yetecek ölçü ve geçim aracı — yeterli miktar veya yeten şey · yaşamı sürdürecek azık ve geçimlik · eldeki şeyle yetinmek · bir iş için yeterli olma
  البلغة ما يتبلغ به من عيش؛ لي في هذا بلاغ أي كفاية (maqayis)؛ في كذا بلاغ وتبليغ أي كفاية (ayn)؛ البلغة القوت يتبلغ به الإنسان (jamhara)؛ البلاغ أيضا الكفاية؛ البلغة ما يتبلغ به من العيش؛ تبلغ بكذا أي اكتفى به (sihah)
- **B004** amacını açık ve etkili sözle anlatma yetkinliği — amacını açık ve etkili sözle anlatma yetkinliği · dili güçlü, sözünü açık ve etkili anlatan kişi · anlatılmak isteneni açık ve etkili biçimde ileten söz
  البلاغة التي يمدح بها الفصيح اللسان لأنه يبلغ بها ما يريده (maqayis)؛ رجل بلغ بليغ وقد بلغ بلاغة (ayn)؛ كلام بلغ وبليغ؛ بلغ الرجل بلاغة إذا صار بليغا (jamhara)؛ البلاغة الفصاحة؛ بلغ الرجل أي صار بليغا (sihah)
- **B005** bir şeyi ulaşılabilir en ileri dereceye götürme — iyi veya nitelikli şey · bütün gücünü kullanıp eksik bırakmamak · eksiksiz buyruk veya en güçlü biçimde pekiştirilmiş ant
  شيء بالغ أي جيد؛ المبالغة أن تبلغ من العمل جهدك (ayn)؛ شيء بالغ أي جيد؛ بلغ في الجودة مبلغا؛ أمر الله بلغ أي بالغ؛ بالغ فلان في أمري إذا لم يقصر فيه (sihah)؛ أيمان علينا بالغة أي منتهية في التوكيد (mufradat)
- **B006** düşüncesizliğine karşın istediğine ulaşan kişi — düşüncesizliğine karşın istediğini elde eden kişi
  هو أحمق بلغ وبلغ أي إنه مع حماقته يبلغ ما يريده (maqayis)؛ أحمق بلغ أي أحمق يبلغ ما يريد (jamhara)؛ أحمق بلغ أي هو مع حماقته يبلغ ما يريده (sihah)
- **B007** atı hızlandırmak için dizgini ileri verme [kalıp] — binicinin atı hızlandırmak için dizgini ileri vermesi
  بلغ الفارس يراد به أنه يمد يده بعنان فرسه ليزيد في عدوه (maqayis)؛ بلغ الفارس إذا مد يده بعنان فرسه ليزيد في جريه (sihah)
- **B008** yokluk veya hastalığın kişiyi iyice sıkıştırması [kalıp] — yokluğun veya hastalığın kişinin üzerinde ağırlaşması
  تبلغت القلة بفلان إذا اشتدت (maqayis)؛ تبلغت به العلة أي اشتدت (sihah)
- **B009** üzücü olayı duyup ondan uzak kalmayı dileme — insanı üzen ve kendisine ulaşan haber · duyalım ama başımıza gelmesin dileği
  اللهم سمع لا بلغ أي نسمع بمثل هذا فلا تنزله بنا (ayn)؛ اللهم سمع لا بلغ معناه يسمع به ولا يتم (sihah)
- **B010** birini kötüleyici bildirimler — bir kimseyi kötüleyen bildirimler ve çekiştirmeler
  البلاغات كالوشايات (sihah)
- **B011** başa gelen ağır ve yıkıcı büyük olay — ağır ve yıkıcı büyük olay · başımıza ağır ve yıkıcı bir olay geldi
  البُلغين الداهية؛ بلغت منا البُلغين (sihah)

## ذ و ق (root_000526): 42:48 أَذَقْنَا

- **B001** ağızla tadını algılamak — yiyeceği ağzıyla tatmak · ağızla tatma · tat; ağızda algılanan nitelik · tatma veya algılanan tat · tatma; tadılan yiyecek miktarı · hiçbir şey tatmadım · yiyecekten hiçbir şey tatmadım · bir şeyi azar azar tatmak
  ذقت المأكول أذوقه ذوقا (maqayis)؛ ذواقه ومذاقه طيب أي طعمه (ayn;tahdhib)؛ ما ذقت ذوقا أي شيئا (sihah)؛ ما ذقت ذواقا وهو ما يذاق من الطعام (tahdhib)
- **B002** bizzat yaşayarak veya sınayarak tanımak — bir kişiyi sınayıp tanımak · birinin elindekini sınayıp tanımak · kötü bir olayı bizzat yaşamak · işinin kötü sonucunu veya cezasını yaşamak · azabı doğrudan yaşamak · açlık ve korku cezasını yaşatmak · denenmiş ve bilinen · birini sınayıp hakkında olumsuz sonuca varmak
  ذقت ما عند فلان اختبرته (maqayis)؛ كل ما نزل بإنسان من مكروه فقد ذاقه (maqayis;ayn;tahdhib)؛ ذقت فلانا وذقت ما عنده (ayn;tahdhib)؛ ذقت ما عند فلان أي خبرته (sihah)؛ أذاقه الله وبال أمره (sihah)؛ أمر مستذاق أي مجرب معلوم (sihah)؛ فذاقت وبال أمرها أي خبرت (tahdhib)؛ الذوق يكون بالفم وبغير الفم (tahdhib)
- **B003** yayı çekip gücünü sınamak — yayı çekip esnekliğini ve gücünü sınamak · tüccarların elleriyle yoklayıp sınadığı
  ذاق القوس إذا نظر ما مقدار إعطائها وكيف قوتها (maqayis)؛ ذقت القوس إذا جذبت وترها لتنظر ما شدتها (sihah)؛ ذق هذا القوس أي انزع فيها لتخبر لينها وشدتها (tahdhib)؛ نظر إلى القوس ورازها (tahdhib)
- **B004** eşinden çabuk bıkıp sürekli yeni eş arayan — evlilikte eşinden çabuk bıkan; sık evlenip boşanan · evlilikte eşlerine bağlanamayıp başkasına yönelen erkekler ve kadınlar · çok evlenip çok boşanan erkek
  لا يحب الذواقين والذواقات (ayn;tahdhib)؛ كلما تزوجا كرها ومدا أعينهما إلى غيرهما (ayn)؛ ألا يطمئن ولا تطمئن كلما تزوج أو تزوجت كرها وطمحا إلى غير الزوج (tahdhib)؛ الذواق الملول (sihah)؛ رجل ذواق مطلاق إذا كان كثير النكاح كثير الطلاق (tahdhib)
- **B005** cinsel birleşmenin hazzını yaşamak — kadına girip onunla cinsel birleşmenin hazzını yaşamak · erkekle cinsel birleşip birlikteliğin hazzını yaşamak
  ذاق الرجل عسيلة المرأة إذا أولج فيها أدافه حتى خبر طيب جماعها وذاقت هي عسيلته كذلك لما خالطها فوجدت حلاوة لذة الخلاط
- **B006** senden sonra belirli bir duruma gelmek — senden sonra seçkin biri oldu · senden sonra cömert oldu · at senden sonra hızlı koşar oldu
  أذاق فلان بعدك سروا أي صار سريا؛ أذاق بعدك كرما؛ أذاق الفرس بعدك عدوا أي صار عداء بعدك

## ف ر ح (root_001140): 42:48 فَرِحَ

- **B001** iç açan sevinç — sevinç; üzüntünün karşıtı olan iç açıcı duygu · sevindi; içi açıldı · bir şeyden ötürü sevinmek · sevinçli · çok sevinçli · sevinen; sevinçli · sevinme; sevinç · sık sık ve çok sevinen kimse · onu sevindirdi; onda sevinç doğurdu · kişiyi sevindiren şey · kendisine ya da olmasına sevinilen şey · sevindirme; kullanıldığı yere göre ağırlaştırma anlamı da taşıyabilir
  خلاف الحزن (maqayis;jamhara)؛ فرح به سر (sihah)؛ الفرح انشراح الصدر بلذة عاجلة (mufradat)؛ الفرحة المسرة (jamhara)؛ رجل فرح وفرحان وامرأة فرحة وفرحى (ayn;jamhara;tahdhib)؛ المفراح الكثير الفرح (sihah;mufradat)؛ ما يسرني به مفرح ومفروح به (ayn;sihah;tahdhib;mufradat)
- **B002** kınanan taşkın sevinç — haksız ve ölçüsüz, kınanan taşkın sevinç
  والفرح أيضا البطر (sihah)؛ تفرحون في الأرض بغير الحق (maqayis;mufradat)؛ أكثر ما يكون ذلك في اللذات البدنية الدنيوية (mufradat)
- **B003** yük altında bırakıp ağırlaştırma — ağırlaştırma; yük altında bırakma · borç yükü altında ezilmiş, ödeme gücü kalmamış kimse · borç onu ağırlaştırdı ve ödeme sıkıntısına soktu · korunmak üzere bırakılan şeyler sana ağır bir yük oldu · o şey beni ezdi ve ağır bir yük altında bıraktı · ağırlaştırma; kullanıldığı yere göre sevindirme anlamı da taşıyabilir
  الإفراح وهو الإثقال (maqayis)؛ رجل مفرح أثقله الدين (ayn;jamhara;sihah;tahdhib;mufradat)؛ أفرحه الدين أثقله (sihah;tahdhib)؛ أفرحتك الودائع (maqayis;ayn;sihah;tahdhib)؛ المفرح المفدوح (sihah;mufradat)؛ أفرحني الشيء مثل فدحني (jamhara)

## ق د م (root_001207): 42:48 قَدَّمَتْ

- **B001** ayak — ayak
  القدم ما يطأ عليه الإنسان (ayn;tahdhib)؛ القدم واحد الأقدام (sihah)؛ القدم قدم الرجل وجمعه أقدام (mufradat)؛ قدم الإنسان معروفة ولعلها سميت بذلك لأنها آلة للتقدم والسبق (maqayis)
- **B002** önceden oluşmuş etki veya paye — öncül etki, iyilik veya saygın konum · önceden kazanılmış iyi paye · önceden işlenmiş kötülük · önder ve saygın kişi · hükümdar veya önder
  القدمة والقدم أيضا السابقة في الأمر وللكافرين قدم شر (ayn)؛ القدم أيضا السابقة في الأمر ولفلان قدم صدق أي أثرة حسنة (sihah)؛ قدم الصدق المنزلة الرفيعة والقدم السابقة وكل ما قدمت من خير والعمل الصالح واليد والمعروف والصنيعة والشرف القديم (tahdhib)؛ متقدم على فلان أي أشرف منه (mufradat)؛ لفلان قدم صدق أي شيء متقدم من أثر حسن والملك هو المقدم (maqayis)؛ رجل قدموس سيد وهو ذلك المعنى (maqayis-variant)
- **B003** eskilik ve önceden var olma — eskilik; sonradan oluşmama · eski; geçmiş zamana dayanan · eskiden; geçmiş zamanda · eski olan
  القدم مصدر القديم من كل شيء (ayn)؛ قدم الشيء فهو قديم والقدم خلاف الحدوث وقدما كان كذا (sihah)؛ القدم العتق مصدر القديم وقد قدم يقدم (tahdhib)؛ حديث وقديم والقدم وجود فيما مضى (mufradat)؛ القدم خلاف الحدوث وشيء قديم إذا كان زمانه سالفا (maqayis)؛ القدموس القديم وأصله من القدم (maqayis-variant)
- **B004** öne geçme, önde ilerleme veya erken davranma — öne geçmek; önde olmak · öne geçme ve ilerleme · ön taraf; önde · önüne geçmek; vaktinden önce davranmak · duraksamadan ileri gitmek
  قدم فلان قومه أي يكون أمامهم والقدم المضي أمام ويمضي قدما أي لا ينثني وقدام خلاف وراء والقدم ضد الأخر (ayn)؛ قدم أي تقدم وقدم بين يديه أي تقدم ومضى قدما لم يعرج ولم ينثن واستقدم وتقدم بمعنى ومقدم نقيض مؤخر (sihah)؛ القدم المضي وهو الإقدام وقدام خلاف وراء والقدم ضد أخر وقدم فلان فلانا إذا تقدمه ولا تقدموا معناه لا تتقدموا قبل الوقت (tahdhib)؛ به اعتبر التقدم والتأخر (mufradat)؛ أصل صحيح يدل على سبق وأصله مضى فلان قدما لم يعرج ولم ينثن ومقدمة الجيش أوله (maqayis)
- **B005** yolculuktan dönüş — yolculuktan dönmek; geri gelmek · yolculuktan dönüş; yolcunun geliş zamanı · yolculuktan dönenler
  القدوم الرجوع من السفر وقدم يقدم (ayn)؛ قدم من سفره قدوما ومقدما والقدام القادمون من سفر (sihah)؛ القدوم الإياب من السفر وقدم فلان من سفره يقدم قدوما (tahdhib)؛ من الباب قدم من سفره قدوما ويقال القدام القادمون من سفر (maqayis)
- **B006** cesaretle öne atılma ve gözüpeklik — gözüpeklik; cesaretle öne atılma · bir işe cesaretle girişmek · gözüpek, atılgan savaşçı · ileri! · gözüpek ve öne atılan kişi
  رجل قدم مقتحم للأشياء يتقدم الناس ويمضي في الحرب قدما (ayn)؛ أقدم على الأمر إقداما والإقدام الشجاعة وأقدم زجر للفرس والمقدام الكثير الإقدام على العدو (sihah)؛ أقدم على قرنه إقداما وقدما ومقدما إذا تقدم عليه بجرأة وضده الإحجام ورجل مقدام في الحرب جريء (tahdhib)؛ أقدم على الشيء إقداما وأقدم زجر للفرس ومضى القوم في الحرب اليقدمية (maqayis)
- **B007** ön bölüm veya ilk kesim — ordunun öncü birliği · gözün veya başın ön kısmı · alın önü ve perçem bölgesi · kuşun ön kanat telekleri · eyer takımının ön kısmı · deve veya ineğin öndeki iki meme başı · dağın öne çıkan burnu · yüzüstü düşmek
  مقدم العين ما يلي الأنف والمقدمة الناصية وما استقبلك من الجبهة والجبين وقادمة الرحل والقادمة الريشة التي تلي منكب الجناح (ayn)؛ قوادم الطير مقاديم ريشه وقيدوم الجبل أنف يتقدم منه وقيدوم كل شيء مقدمه وصدره ومقدمة الجيش أوله وقادمتا الناقة (sihah)؛ مقدمة الجيش الذين يتقدمون الجيش ومقدم العين ومقدم الرأس والمقدمة الناصية وقادمة الرحل وللناقة قادمان وقوادم ريش الطائر (tahdhib)؛ قادمة الرحل خلاف آخرته وقادمة من أطباء الناقة وقادم الإنسان رأسه وقوادم الطير ومقدمة الجيش أوله وقيدوم الجبل أنف يتقدم منه (maqayis)
- **B008** ahşap yontma keseri — ahşap yontma keseri
  القدوم مخفقة الحديدة التي ينحت بها الخشب (ayn)؛ القدوم التي ينحت بها مخففة ولا تقل قدوم بالتشديد (sihah)؛ القدوم التي ينحت بها وجمعها قدم واختتن إبراهيم بالقدوم قال قطعه بها (tahdhib)؛ مما شذ عن هذا الأصل القدوم الحديدة ينحت بها وهي معروفة (maqayis)
- **B009** belirli bir yer adı — belirli bir yer adı
  القدوم أيضا اسم موضع (sihah)؛ القدوم مكان (maqayis)
- **B010** bir işe yönelip onu amaçlamak [kalıp] — bir işe yönelip onu amaçlamak
  قدم فلان إلى أمر كذا أي قصد له ومنه وقدمنآ إلى ما عملوا قال الفراء والزجاج قدمنا عمدنا وقصدنا (tahdhib)

## و ه ب (root_001685): 42:49 يَهَبُ, 42:49 وَيَهَبُ

- **B001** karşılıksız bağışlama — karşılıksız bağışlamak · karşılıksız bağış · bağış, karşılıksız armağan · bağışlanan şey ya da kişi · bağışlayan · bol bol bağışta bulunan · çok bağış yapan · pek çok bağış yapan · çokça bağışlayan kimse · kendini bağış olarak sunmak
  وهبت الشيء هبة وموهبا (maqayis)؛ وهب الله لك الشيء يهب هبة (ayn;tahdhib)؛ وهبت لك الشيء وهبا (jamhara)؛ وهبت له شيئا وهبا وهبة والاسم الموهب والموهبة (sihah)؛ الهبة أن تجعل ملكك لغيرك بغير عوض (mufradat)؛ الوهاب الواهب والكثير الهبات (tahdhib;sihah)
- **B002** bağışı kabul etme, isteme veya karşılıklı bağışlama — bağışı kabul etmek · bağış kabul etme · bağış kabul etmek · bağış isteme · karşılıklı bağışlaşmak
  انهبت الهبة قبلتها (maqayis)؛ لا أتهب أي لا أقبل هبة (ayn;tahdhib;mufradat)؛ الاتهاب قبول الهبة والاستيهاب سؤال الهبة (sihah)؛ تواهبه الناس بينهم وتواهب القوم (ayn;sihah)
- **B003** yağmur suyu tutan kaya çukuru — yağmur suyu biriken kaya çukuru
  الموهبة قلت يستنقع فيه الماء (maqayis)؛ الموهبة غدير ماء صغير في صخرة (jamhara)؛ نقرة في الجبل يستنقع فيها الماء والجمع مواهب (sihah)؛ نقرة في صخرة يستنقع فيها ماء السماء (tahdhib)
- **B004** belirli miktar paranın kişiye ulaşması [kalıp] — eline şu kadar para ulaşmak
  أوهب إلى من المال كذا أي ارتفع (maqayis)
- **B005** hazırlama; hazır ve elverişli olma — senin için hazırlamak · hazır, elverişli veya kişinin yanında bulunan · odunu bol
  أصبح فلان موهبا لكذا أي معدا له (maqayis)؛ أوهبت لك كذا أي أعددته لك (jamhara)؛ هو موهب أي معد عند الرجل (sihah;tahdhib)؛ أصبح فلان موهبا أي معدا قادرا (sihah;tahdhib)
- **B006** öyle sayıp kabul et — o kişiyi gitmiş say · beni öyle say ve kabul et
  هب زيدا منطلقا بمعنى أحسب (sihah)؛ هبني ذاك أي احسبني ذاك واعددني (tahdhib)؛ لا يستعمل منه ماض ولا مستقبل في هذا المعنى وكلمة وضعت للأمر (sihah;tahdhib)
- **B007** bir kimse için sürüp gitmek [kalıp] — bir kimse için sürüp gitmek
  أوهب له الشيء أي دام له (sihah)؛ أوهب الشيء إذا دام (tahdhib)

## ء ن ث (root_000058): 42:49 إِنَٰثًا, 42:50 وَإِنَٰثًا

- **B001** disi olma — erkegin karsiti olan disi · disiler toplulugu · siirde gelen disiler cogulu · kadinin kiz cocuk dogurmasi · adet olarak kiz doguran kadin · kadinlikta tam ve olgun sayilan kadin · disi yaratilisinda erkek
  الأنثى خلاف الذكر (maqayis;sihah;tahdhib;mufradat)؛ يجمع على إناث (sihah)؛ الإناث جماعة الأنثى ويجيء أناثى (tahdhib)؛ آنثت المرأة إذا ولدت أنثى (sihah)؛ هذه امرأة أنثى إذا مدحت بأنها كاملة من النساء (tahdhib)؛ المؤنث ذكر في خلق الأنثى (tahdhib)
- **B002** yumusak ve zayif is gorur olma — yumusak veya zayif is gorur demir · kesmeyen veya keskinligi iyi olmayan kilic · isinde yumusamak ve sert davranmamak · yumusak, edilgin veya kadinsil erkek
  سيف أنيث الحديد إذا كانت حديدته أنثى (maqayis)؛ الأنيث ما كان من الحديد غير ذكر (sihah)؛ سيف أنيث وهو الذي ليس بقطاع (tahdhib)؛ أنثت في أمرك أي لنت له (tahdhib)؛ الأنيث من الرجال المخنث (tahdhib)؛ لما يضعف عمله أنثى وحديد أنيث (mufradat)؛ المنفعل يقال له أنيث (mufradat)
- **B003** testisler veya kulaklar icin ikil ad — testisler · kulaklar
  الأنثيان الخصيتان (maqayis;tahdhib)؛ الأنثيان الخصيان (sihah)؛ الأنثيان أيضا الأذنان (maqayis;sihah)؛ الأنثيان الأذنان (tahdhib)؛ الخصية لتأنيث لفظ الأنثيين وكذلك الأذن (mufradat)
- **B004** yumusak ve bitirgen toprak — yumusak, iyi bitki veren arazi · bitkisi hizli ve bol cikan yer · bitki vermeye yatkin kolay arazi · bitki bitiren yer veya nitelik
  أرض أنيثة حسنة النبات (maqayis)؛ أرض أنيثة تنبت البقل سهلة (sihah)؛ مكان أنيث إذا أسرع نباته وكثر (tahdhib)؛ أرض مئناث سهلة خليقة بالنبات (tahdhib)؛ أرض أنيثة أي سهلة (tahdhib)؛ الأنيث الذي ينبت النبت (tahdhib)؛ أرض أنيث سهل أو بجودة إنباتها (mufradat)
- **B005** dilbilgisel disillestirme — adi veya soz hukumunu disil yapmak · onu disil yapti, o da disil hukum kazandi
  تأنيث الاسم خلاف تذكيره (sihah)؛ أنثته فتأنث (sihah)؛ إذا قلت للشيء تؤنثه فالنعت بالهاء (tahdhib)؛ لما شبه في حكم اللفظ بعض الأشياء بالذكر وبعضها بالأنثى (mufradat)
- **B006** kadinsi adli putlar — kadinsi adlarla anilan putlar veya ibadet nesneleri · cansiz ve edilgin varliklar · bir topluluga ait put diye adlandirma
  إن يدعون من دونه إلا إناثا (tahdhib;mufradat)؛ مواتا مثل الحجر والخشب والشجر (tahdhib)؛ سموا الأوثان إناثا لقولهم اللاتي والعزى ومناة (tahdhib)؛ كانوا يقولون للصنم أنثى بني فلان (tahdhib)؛ أسماء معبوداتهم مؤنثة (mufradat)؛ المنفعل يقال له أنيث (mufradat)
- **B007** renk veren kadin kokusu — giysiye renk veren kadin kokusu
  المؤنث من الطيب طيب النساء مثل الخلوق والزعفران وما يلون الثياب؛ ذكورة الطيب ما لا لون له مثل الغالية والكافور والمسك والعود والعنبر
- **B008** iki Arap kabilesinin adi — iki Arap kabilesi icin ortak ad
  الأنثيان من أحياء العرب بجيلة وقضاعة

## ذ ك ر (root_000516): 42:49 ٱلذُّكُورَ, 42:50 ذُكْرَانًا

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

## ع ق م (root_001037): 42:50 عَقِيمًا

- **B001** üremezlik ve çocuk sahibi olamama [kalıp] — döl yatağı döl tutmadı · kadın doğuramadı ve kısırlaştı · çocuk doğuramayan kadın · çocuğu olmayan erkek · döl tutmayan dişi deve
  عقمت الرحم عقما فلا تقبل الولد (maqayis;ayn;tahdhib)؛ امرأة عقيم لا تلد ورجل عقيم لا يولد له (sihah;tahdhib)؛ العَقِيم من النساء التي لا تقبل ماء الفحل (mufradat)
- **B002** döllemeyen ve yağmur getirmeyen rüzgar [kalıp] — döllemeyen, yağmur taşımayan ve yıkım getirebilen rüzgar
  الريح العقيم التي لا تلقح شجرا ولا سحابا (maqayis;ayn;sihah)؛ لا تلقح شجرا ولا تحمل مطرا وهي ريح الإهلاك (tahdhib)؛ لا تقبل أثر الخير (mufradat)
- **B003** eklemlerin kuruyup kapanması — ikiyüzlülerin bel eklemlerinin kuruyup kapanması · eklemleri kurudu · eklemler, özellikle atların eklemleri
  تعقم أصلاب المنافقين فيبس مفاصلهم (maqayis;tahdhib)؛ تعقم أصلاب المشركين أي تيبس وتسد (ayn)؛ المعاقم من الخيل المفاصل (sihah)؛ عقمت مفاصله (mufradat)
- **B004** iyileşmez hastalık [kalıp] — iyileşmeyen, iyileşmeyi kabul etmeyen hastalık
  داء عقام لا يبرأ منه (maqayis)؛ العقام أيضا الداء الذي لا يبرأ منه (sihah)؛ داء عقام لا يقبل البرء (mufradat)
- **B005** kimsenin kimseyi gözetemediği amansız savaş [kalıp] — kimsenin kimseyi gözetemediği amansız savaş · öldürmenin çok olduğu savaş
  حرب عقام وعقام لا يلوي فيها أحد على أحد لشدتها (maqayis;ayn;tahdhib)؛ الحرب الشديدة (sihah)؛ حرب عقيم يكثر فيها القتل (tahdhib)
- **B006** dar ve kötü huyluluk [kalıp] — dar ve kötü huylu erkek · kötü huylu kadın
  رجل عقام وهو الضيق الخلق (maqayis)؛ الرجل السيئ الخلق (sihah)؛ امرأة عقام ورجل عقام إذا كانا سيئي الخلق (tahdhib)
- **B007** aklın ya da dünya hayatının yarar vermemesi [kalıp] — sahibine hiçbir yarar sağlamayan akıl · sahibine iyilik getirmeyen dünya hayatı
  عقل عقيم لا يجدي على صاحبه شيئا (maqayis)؛ عقل صاحب الدنيا فعقيم وعقل صاحب الآخرة فمثمر (maqayis;ayn)؛ الدنيا عقيم لا ترد على صاحبها خيرا (maqayis;ayn)
- **B008** iktidarın soy bağını gözetmemesi [kalıp] — hükümdarlık soy ve akrabalık bağını gözetmez
  الملك عقيم يسد باب المحافظة على النسب (maqayis)؛ الملك عقيم لا ينفع فيه النسب (ayn)؛ الملك عقيم لأن الرجل قد يقتل ابنه (sihah)؛ العقم القطع ومنه قيل الملك عقيم (tahdhib)
- **B009** ardından gün gelmeyen ya da sevinçsiz gün [kalıp] — ardından başka gün gelmeyen ya da içinde sevinç bulunmayan gün
  يوم القيامة يوم عقيم لأنه لا يوم بعده (sihah)؛ يوم عقيم لا فرح فيه (mufradat)
- **B010** kapalı eski söz veya eylem türetilemeyen söz [kalıp] — bugün anlaşılmayan çok eski ve kapalı söz · kendisinden eylem biçimi türetilemeyen söz
  كلام عقمي من كلام الجاهلية لا يعرف (maqayis)؛ كلام عقمي أي غامض (sihah)؛ العقمي من الكلام غريب الغريب (tahdhib)؛ كلام عقيم لا يشتق منه فعل (tahdhib)
- **B011** kuyunun yanını veya aşağısını kazma — kuyunun yanlarını kazma veya kazıyı aşağı sürdürme · su başının ya da kuyunun yanlarında oyuk açmak
  الاعتقام الحفر في جوانب البئر (maqayis)؛ الاعتقام أن تحفر البئر ثم احتفرت بئرا صغيرة (sihah;tahdhib)؛ المضي في الحفر سفلا (tahdhib)
- **B012** karşı tarafı sözle sıkıştırarak çekişme — onunla çekişip sözle sıkıştırdı · karşı tarafı sözle sıkıştıran çekişmeci · çekişmede karşı tarafın yönünü büken kişi
  المعاقم المخاصم يضيق على صاحبه بالكلام (maqayis)؛ عاقمت فلانا إذا خاصمته (sihah)؛ ذو عقميات إذا كان يلوي بخصمه (tahdhib)
- **B013** desenli dokuma veya kırmızı örtü — bir tür desenli dokuma, örtü veya kırmızı kumaş · bu desenli dokumanın bir parçası
  العقم المرط أو ثوب يلبس في الجاهلية أو كل ثوب أحمر (ayn)؛ العقم والعقمة ضرب من الوشي (sihah;tahdhib)
- **B014** samandaki düğüm veya tane ayıran engel — samandaki düğüm veya samanla tane arasındaki engel · harman savrulurken samanla tane arasındaki engel
  الحاجز بين التبن والحب إذا ذري الطعام مقعم (maqayis)؛ المعقم أيضا عقدة في التبن (sihah)
- **B015** köklü cömertlik ve onur sahibi erkek — köklü cömertlik ve onur sahibi erkek
  العقمي الرجل القديم الكرم والشرف (tahdhib)
- **B016** denizde yaşayan bir yılan — denizde yaşayan bir yılanın adı
  العقام اسم حية تسكن البحر (tahdhib)
- **B017** bir işe veya meseleye girme — bir işe ya da meseleye girme
  الاعتقام الدخول في الأمر (ayn)

## و ر ي (root_001642): 42:51 وَرَآئِ

- **B001** iç organları bozan ya da akciğeri tutan hastalık — iç organları ya da akciğeri tutan hastalık · içi hastalıktan bozuldu; irin içini yedi · içi bu hastalıkla bozulmuş kimse · akciğeri tutan hastalık · akciğerinden yaraladı · yara, onu yoklayana bu hastalığı geçirdi
  الورى داء يداخل الجسم (maqayis)؛ وري جوف فلان فهو موري إذا فسد من داء يصيبه (jamhara)؛ ورى القيح جوفه يريه وريا: أكله (sihah)؛ الورى داء يصيب الرجل والبعير في أجوافهما (tahdhib)؛ الوارية داء يأخذ في الرئة (ayn;tahdhib)
- **B002** çakmaktan ateş çıkarma ve sönük ateşi harlama — çakmaktan ateş çıktı · sönük ateşi harlayıp yükseltti · ateş yakmaya yarayan araç
  ورى الزند خرجت ناره (maqayis;jamhara;sihah;mufradat)؛ إذا أخرج الزند النار قيل وري الزند يري (tahdhib)؛ أوريت النار إذا كانت خامدة فأججتها (ayn)؛ أريت النار تأرية إذا رفعتها (tahdhib)
- **B003** çakmak benzetmesiyle başarma, yardım görme ya da savunma [kalıp] — giriştiği işte başarıya ulaşan · sende yardım, içten öğüt ve cömertlik buldum · onu destekledi ve savundu
  ورت بك زنادي إذا أنجده وأعانه (jamhara)؛ وريت بك زنادي أي رأيت منك ما أحب من النصح والنجابة والسماحة (ayn)؛ لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب (tahdhib;mufradat)؛ لوريت عن مولاك أي نصرته ودفعت عنه (tahdhib)
- **B004** yağlı ve semiz olma; iliğin dolgunlaşması — yağlı ve semiz · semiz dişi deve · kemik iliği dolup yoğunlaştı
  اللحم الواري: السمين (maqayis;mufradat)؛ الواري الشحم السمين والوري مثله (ayn)؛ ناقة وارية بغير همز: سمينة (jamhara)؛ وري المخ إذا اكتنز وناقة وارية أي سمينة ولحم وري أي سمين (sihah)
- **B005** gizleme, gizlenme ve başka anlam gösterme — şeyi gizleyip gözden sakladı · gizlendi, gözden kayboldu · haberi gizleyip başka bir anlamı öne çıkarma · niyetini gizlemek için başka bir şey söyledi
  التورية إخفاء الخبر وعدم إظهار السر تقول وريته تورية (ayn)؛ واريت الشيء أي أخفيته وتوارى هو أي استتر (sihah)؛ التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره (tahdhib)؛ واريت كذا إذا سترته وتوارى استتر (mufradat)
- **B006** konuma göre arka, ön, öte ya da öbür yan — arka, ön, öte ya da öbür yan · geri çekil; yana açıl
  وراءك يكون من خلف ويكون من قدام (maqayis)؛ وراء ممدود خلاف قدام (ayn)؛ وراء بمعنى خلف وقد يكون بمعنى قدام وهي من الأضداد (sihah)؛ الوراء الخلف ويكون الأمام وبما وراءه أي بما سواه (tahdhib)؛ وراء زيد كذا لمن خلفه ويقال لما كان قدامه أو في أي جانب من الجدار (mufradat)
- **B007** torun — torun, özellikle oğlun oğlu
  الوراء ولد الولد (maqayis;sihah;mufradat)؛ الوراء ممدود ولد الولد (ayn)؛ الوراء ابن الابن (tahdhib)
- **B008** yeryüzündeki bütün yaratılmışlar — yeryüzündeki yaratılmışlar
  الورى: الخلق (maqayis;sihah;tahdhib)؛ الورى مقصور الأنام الذي على ظهر الأرض (ayn)؛ الورى الأنام الذين على وجه الأرض في الوقت (mufradat)
- **B009** sapıklık çakmağından kıvılcım çıkarmaya çalışma [kalıp] — sapıklık çakmağından kıvılcım çıkarmaya çalışıyor
  فلان يستوري زناد الضلالة

## ح ج ب (root_000294): 42:51 حِجَابٍ

- **B001** giriş veya erişimi engelleme — bir şeye ulaşmasını veya girmesini engellemek · erişimi engelleme · ulaşmayı önleme · erişimi engellenmiş kişi veya şey
  الحاء والجيم والباء أصل واحد وهو المنع (maqayis)؛ كل شيء منع شيئا من شيء فقد حجبه (ayn)؛ حجبه أي منعه عن الدخول (sihah)؛ كل شيء منع شيئا فقد حجبه (tahdhib)؛ الحجب والحجاب المنع من الوصول (mufradat)
- **B002** perdeyle ayırma veya görünmez olma — iki şeyi ayıran perde veya örtü · perde arkasına çekilip görünmez olmak · güneşin ufukta gözden kaybolması · örtmek veya gizlemek · perdeler veya örtüler · örtü arkasında gizlenmiş kadın · halkın görüşünden uzak duran hükümdar
  الحجاب الستر (jamhara;sihah)؛ الحجاب اسم ما حجبت به بين شيئين (tahdhib)؛ احتجب فلان إذا اكتن من وراء الحجاب (tahdhib)؛ احتجبت الشمس في السحاب إذا استترت فيه (jamhara)؛ حتى توارت بالحجاب يعني الشمس إذا استترت بالمغيب (mufradat)
- **B003** hükümdar kapıcılığı ve bu göreve atama — hükümdara girişleri düzenleme görevi · hükümdarın kapı görevlisi · onu kapı görevlisi atadı · hükümdarın kapı görevlileri · kapı görevlileri topluluğu
  الحجابة ولاية الحاجب (ayn;tahdhib)؛ حاجب الأمير جمعه حجاب (sihah)؛ استحجبه ولاه الحجبة (sihah)؛ الحاجب المانع عن السلطان (mufradat)
- **B004** yüreği karın boşluğundan ayıran zar — yüreği karın boşluğundan ayıran zar
  حجاب الجوف ما يحجب بين الفؤاد وسائر الجوف (maqayis)؛ حجاب الجوف جلدة تحجب بين الفؤاد وسائر البطن (ayn;tahdhib)؛ ما يحتجب بين الفؤاد وسائره (sihah)؛ حجاب الجوف ما يحجب عن الفؤاد (mufradat)
- **B005** gözü güneşten koruyan kaş bölgesi — kaş · kaşlar
  الحاجبان العظمان فوق العينين بالشعر واللحم (maqayis)؛ الحاجب عظم العين من فوق يستره بشعره ولحمه (ayn)؛ حاجب العين لأنه يحجب عنها شعاع الشمس (jamhara)؛ حاجب العين جمعه حواجب (sihah)؛ الحاجبان العظمان فوق العينين بشعره ولحمه (tahdhib)؛ الحاجبان في الرأس (mufradat)
- **B006** iki kalça kemiğinin çıkıntılı başları — kalça kemiğinin çıkıntılı başı · iki kalça kemiğinin çıkıntılı başları
  الحجبة رأس الورك (maqayis)؛ رؤوس عظم الوركين وما يلي الحرقفتين حجبتين (ayn)؛ الحجبة رأس الورك وهما حجبتان تشرفان على الخاصرتين (sihah)؛ الحجبتان رؤوس عظمي الوركين مما يلي الحرقفتين (tahdhib)
- **B007** bir şeyin kenarı, yanı veya öne çıkan ucu — bir şeyin kenarı veya yanı · güneş diskinin görünen kenarı · güneşin kenarları · ekmeğin kenarları · dağın çıkıntılı yüksek yeri · ay diskinin görünen kenarı
  حاجب كل شيء حرفه (jamhara)؛ بدا حاجب من الشمس أي بدت ناحية منها (jamhara)؛ حواجب الشمس نواحيها (sihah)؛ الحجاب ما أشرف من الجبل (tahdhib)؛ حاجب الشمس قرنها وهو ناحية من قرصها (tahdhib)؛ حواجب الرغيف حروفه (tahdhib)؛ حاجب الشمس سمي لتقدمه عليها (mufradat)
- **B008** kalıtta payı engelleme veya azaltma [kalıp] — annenin üçte birlik kalıt payını düşürmek
  الإخوة يحجبون الأم عن الثلث (sihah)؛ كما تحجب الأم الإخوة عن فريضتها (tahdhib)
- **B009** kör kişi — kör kişi
  المحجوب الضرير (sihah)
- **B010** gebeliğin dokuzuncu ayına bir-iki gün girmiş olma [kalıp] — gebeliğin dokuzuncu ayına bir gün girmiş olmak
  احتجبت الحامل بيوم من تاسعها وبيومين من تاسعها (tahdhib)؛ أصبحت محتجبة بيوم من تاسعها (tahdhib)
- **B011** sık ağaçlık — sık ağaçlık veya çalılık
  الحجيب الأجمة (jamhara)
- **B012** siyah taşlarla kaplı arazi — siyah taşlarla kaplı arazi
  الحجاب الحرة (tahdhib)

## ن و ر (root_001564): 42:52 نُورًا

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## ص ر ط (root_000858): 42:52 صِرَٰطٍ, 42:53 صِرَٰطِ

- **B001** yol, özellikle düz yol — yol, özellikle düz yol · yol veya düz yol · yol
  الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)
- **B002** geçişte gözden kaybolmak; özellikle yiyeceği yutmak — yiyeceği boğazdan geçirip gözden kaybolacak biçimde yutmak · kolayca yutulan pelte kıvamlı tatlı · geniş boğazlı
  أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب؛ السرطراط على فعلال الفالوذ لأنه يسترط (maqayis 1774)؛ السرطم: الواسع الحلق، والميم فيه زائدة، وإنما هو من سرط، إذا بلع (maqayis السرطم)
- **B003** vuruşta kesip ilerleyen kılıç — vuruşta kesip ilerleyen kılıç
  والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)



===== _commentary/v16/work/s042/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s042/reader_a_pilot.md)

# s042 Semantic Channel Discovery

## Parent Channels

### 1. P1 Assembly Against Fragmentation (42:1-15)
- Semantic invariant: Dispersed units become an ordered, transmissible whole.
- Surface relation: direct; revelation, recitation, scripture, communal gathering, and religious division appear at 42:3, 42:7, and 42:13-15.
- Surprising reach: The passage's communicative and communal coherence is materialized as inscription, stitching, and the physical joining of scattered pieces.

#### Subchannel A. Hidden Speech Becomes Legible
- Reading type: mixed
- Scene or process: A concealed communication passes into inscription, recitation, and meaningful verbal form.
- Active motifs: hidden conveyance of knowledge or speech `quranic:root_001633:B001/m01`; inscribed communication `quranic:root_001633:B003/m01`; voiced reading or recitation `quranic:root_001210:B002/m01`; ordered written object `quranic:root_001283:B002/m01`; meaningful word or phrase `quranic:root_001316:B002/m01`.
- Ayah anchors: و ح ي at 42:3, 42:7, 42:13; ق ر ء at 42:7; ك ت ب at 42:14-15; ك ل م at 42:14.
- Synthesis: Concealed speech is not left immaterial: it is impressed into a written object, sounded in recitation, and articulated as meaningful wording. The lexical scene gives revelation a sequence from hidden source to public legibility.

#### Subchannel B. Joining a Text and a People
- Reading type: mixed
- Scene or process: Scattered elements are gathered, joined, and transmitted, while division pulls the assembly apart.
- Active motifs: gathering dispersed units `quranic:root_000259:B001/m01`; assembly through reading `quranic:root_001210:B001/m01`; joining or stitching written units `quranic:root_001283:B001/m01`; connecting one thing to another `quranic:root_001656:B001/m01`; a settlement as gathered people `quranic:root_001222:B001/m01`; dispersal into parts `quranic:root_001148:B002/m01`.
- Ayah anchors: ج م ع at 42:7, 42:15; ق ر ء at 42:7; ك ت ب at 42:14-15; و ص ي at 42:13; ق ر ي at 42:7; ف ر ق at 42:7, 42:13-14.
- Synthesis: Reading, writing, testament, and settlement converge on one operation: units are joined into a durable assembly. The opposing image is not generic disagreement but a sewn or gathered whole coming apart into separate pieces.

### 2. P1 Provision as Regulated Hydrology (42:1-15)
- Semantic invariant: Provision moves from an elevated store through controlled release into receiving and distributing structures.
- Surface relation: indirect; sky, what lies above, provision, descent, and the keys of heaven and earth occur at 42:4-5 and 42:12-15.
- Surprising reach: Divine apportionment takes concrete form as a water system of clouds, pulses, basins, channels, and allotted irrigation turns.

#### Subchannel A. Stored Water Descends
- Reading type: latent/lexical
- Scene or process: An overhead canopy gathers moisture and releases it in measured pulses as provision.
- Active motifs: sky as cloud-bearing canopy `quranic:root_000745:B004/m01`; layered rain cloud `quranic:root_000532:B008/m01`; cloud water released in pulses `quranic:root_001188:B008/m01`; rain descending as provision `quranic:root_000560:B003/m01`; downward release or rainfall `quranic:root_001492:B001/m01`.
- Ayah anchors: س م و at 42:4-5, 42:11-12, 42:14; ر ب ب at 42:5, 42:10, 42:14-15; ف و ق at 42:5; ر ز ق at 42:12; ن ز ل at 42:15.
- Synthesis: The upper realm behaves as a layered reservoir: moisture is held, pulsed, and sent down as apportioned sustenance. This gives the surface language of keys and expanded or restricted provision a latent hydraulic mechanism.

#### Subchannel B. Water Is Received and Allotted
- Reading type: latent/lexical
- Scene or process: Descending water is caught in hollows and basins, routed through channels, and assigned by turn.
- Active motifs: water-holding basin `quranic:root_000018:B006/m01`; collected water in a large basin `quranic:root_000220:B002/m01`; water gathered in a hollow `quranic:root_000281:B003/m01`; allotted irrigation turn `quranic:root_001249:B007/m01`; distant channels feeding a reservoir `quranic:root_001510:B007/m01`; water gathered at a settlement or basin `quranic:root_001222:B002/m01`.
- Ayah anchors: ء خ ذ at 42:6, 42:9; ج ب ي at 42:13; ج ي ء at 42:14; ق ل د at 42:12; ن ص ر at 42:8; ق ر ي at 42:7.
- Synthesis: Reception is as structured as release. Hollows collect the flow, channels convey it, and irrigation turns allocate it, so abundance becomes usable only through custody and measure.

### 3. P1 Propagation Through Pairing and Containment (42:1-15)
- Semantic invariant: New life proceeds by joining, seeding, enclosure, and eventual emergence.
- Surface relation: direct; 42:11 names paired human and animal propagation, while creation and mercy recur across 42:5-11.
- Surprising reach: The paired creation formula opens into a detailed reproductive process extending from mating and seed to womb, fetus, and birth attendant.

#### Subchannel A. Coupling and Seeding
- Reading type: mixed
- Scene or process: Paired bodies join and seed is deposited to initiate generation.
- Active motifs: a pair joined for mating `quranic:root_000652:B001/m01`; marital spouse `quranic:root_000652:B002/m01`; seed cast into soil `quranic:root_000510:B003/m01`; female animal seeking the male `quranic:root_000248:B009/m01`; seminal fluid `quranic:root_001492:B009/m01`.
- Ayah anchors: ز و ج at 42:11; ذ ر ء at 42:11; ج ع ل at 42:8, 42:11; ن ز ل at 42:15.
- Synthesis: Pairing is rendered as an active generative mechanism: attraction and coupling precede the placement of seed. Agricultural deposition and bodily reproduction share the same functional transition from paired potential to initiated growth.

#### Subchannel B. Gestation and Reception at Birth
- Reading type: latent/lexical
- Scene or process: The developing child is enclosed and gathered in a womb, then received as it emerges.
- Active motifs: fetus enclosed in the womb `quranic:root_000266:B007/m01`; womb as the child's container `quranic:root_000552:B003/m01`; womb gathering the fetus `quranic:root_001210:B004/m01`; postpartum or birth blood `quranic:root_001533:B005/m01`; midwife receiving the emerging child `quranic:root_001198:B007/m01`.
- Ayah anchors: ج ن ن at 42:7; ر ح م at 42:5, 42:8; ق ر ء at 42:7; ن ف س at 42:11; ق ب ل at 42:3.
- Synthesis: Generation continues through protected containment: the womb encloses and gathers until emergence changes the scene from internal formation to external reception. Mercy resonates materially with the organ that shelters developing life.

### 4. P1 Route-Making and Binding Commitment (42:1-15)
- Semantic invariant: A viable way is opened, clarified, straightened, and made binding on those who enter it.
- Surface relation: direct; ordained religion, guidance, uprightness, command, proof, and justice cluster at 42:13-15.
- Surprising reach: Normative direction is rendered through road engineering and water access before becoming an obligation carried on the body.

#### Subchannel A. Opening and Straightening the Way
- Reading type: mixed
- Scene or process: An access point becomes a traceable road with forks, guidance, and correction toward straightness.
- Active motifs: opened water-access point `quranic:root_000789:B002/m01`; clear intended road `quranic:root_000295:B002/m01`; tracing lands, roads, and waters `quranic:root_001222:B005/m01`; road fork `quranic:root_001148:B006/m01`; gentle guidance onto a road `quranic:root_001583:B001/m01`; straightening or setting upright `quranic:root_001273:B008/m01`.
- Ayah anchors: ش ر ع at 42:13; ح ج ج at 42:15; ق ر ي at 42:7; ف ر ق at 42:7, 42:13-14; ه د ي at 42:13; ق و م at 42:13, 42:15.
- Synthesis: The prescribed way begins as opened access and becomes a navigable route whose forks require guidance. Uprightness is thus a corrective operation on a path, not only an abstract moral state.

#### Subchannel B. Entering a Binding Charge
- Reading type: mixed
- Scene or process: Entering the opened way places a transmitted command or covenant under personal obligation.
- Active motifs: binding command `quranic:root_000051:B002/m01`; obligation hung around the neck `quranic:root_001249:B004/m01`; transmitted covenant or testament `quranic:root_001656:B002/m01`; entering or undertaking an affair `quranic:root_000789:B003/m01`.
- Ayah anchors: ء م ر at 42:15; ق ل د at 42:12; و ص ي at 42:13; ش ر ع at 42:13.
- Synthesis: Once the route is entered, direction becomes charge. Command and testament are carried like a neck-bound obligation, turning a disclosed way into a personally borne commitment.

### 5. P1 Custody and Entrusted Rule (42:1-15)
- Semantic invariant: Authority is exercised by guarding, sustaining, receiving an entrustment, and deciding between claims.
- Surface relation: direct; protector, trustee, judgment, command, and divine care appear throughout 42:6-15.
- Surprising reach: Sovereignty is framed less as possession than as the practical work of custodianship, delegated office, repair, and arbitration.

#### Subchannel A. Sustained Protective Care
- Reading type: mixed
- Scene or process: A custodian watches over what has been entrusted and remains standing over its welfare.
- Active motifs: guarding and preserving `quranic:root_000342:B001/m01`; protective administration `quranic:root_001684:B003/m01`; sufficient custodian `quranic:root_001681:B006/m01`; sustained standing care `quranic:root_001273:B004/m01`.
- Ayah anchors: ح ف ظ at 42:6; و ل ي at 42:6, 42:8-9; و ك ل at 42:6, 42:10; ق و م at 42:13, 42:15.
- Synthesis: Protection is an ongoing posture rather than a single intervention. The guardian receives responsibility, remains over the charge, and suffices for its continued preservation.

#### Subchannel B. Delegated Judgment and Repair
- Reading type: mixed
- Scene or process: An affair is entrusted to an office that arbitrates, rules, and restores what is under its care.
- Active motifs: entrusting an affair `quranic:root_001681:B001/m01`; delegated arbitration `quranic:root_000348:B005/m01`; judgment between people `quranic:root_000348:B002/m01`; nurturing, repairing, and completing `quranic:root_000532:B002/m01`; office or governing authority `quranic:root_000051:B003/m01`.
- Ayah anchors: و ك ل at 42:6, 42:10; ح ك م at 42:3, 42:10; ر ب ب at 42:5, 42:10, 42:14-15; ء م ر at 42:15.
- Synthesis: Entrusted authority resolves difference through judgment, but its goal is not merely a verdict. The ruling office also tends, repairs, and brings its charge toward completion.

### 6. P2 Claims Under Load (42:16-29)
- Semantic invariant: A claim is tested by whether it slips and collapses or bears calibrated, fitted truth.
- Surface relation: direct; disputed proofs, truth, scripture, the balance, doubt, and the Hour appear at 42:16-18 and 42:24.
- Surprising reach: Argument is treated as a physical structure whose footing, weave, joints, and load-bearing measure can be inspected.

#### Subchannel A. Slipping and Collapsing Argument
- Reading type: mixed
- Scene or process: Adversarial speech is put forward as proof but loses footing and falls under pressure.
- Active motifs: prevailing proof or argument `quranic:root_000295:B003/m01`; slippery footing `quranic:root_000461:B001/m01`; argument collapsing into invalidity `quranic:root_000461:B003/m01`; sharp verbal dispute `quranic:root_001416:B003/m01`.
- Ayah anchors: ح ج ج at 42:16; د ح ض at 42:16; م ر ي at 42:18.
- Synthesis: The contest is both forensic and kinetic. A proof can initially press its claim, yet its footing gives way and the structure of dispute collapses.

#### Subchannel B. Weighed and Fitted Truth
- Reading type: mixed
- Scene or process: Truth is weighed, woven tightly, fitted at its joints, and fixed in writing.
- Active motifs: weighing and estimation `quranic:root_001645:B001/m01`; justice-bearing scale `quranic:root_001645:B002/m01`; stable truth `quranic:root_000347:B001/m01`; tightly woven speech `quranic:root_000347:B010/m01`; fitted joint or container `quranic:root_000347:B011/m01`; fixed written judgment `quranic:root_001283:B003/m01`.
- Ayah anchors: و ز ن at 42:17; ح ق ق at 42:17-18, 42:24; ك ت ب at 42:17.
- Synthesis: Reliable speech is not only correct; it is proportioned and structurally fitted. Measure, tight weave, joined parts, and written fixation all describe a claim able to bear examination.

### 7. P2 Cultivation and Accrual (42:16-29)
- Semantic invariant: Desired outcomes arise through planting and tending, then return as yield, gain, or allotted share.
- Surface relation: direct; 42:20 presents the two harvests, while earning, reward, increase, bounty, and provision recur at 42:22-27.
- Surprising reach: Moral and eschatological acquisition is expanded into a concrete field economy of sowing, watering, land repair, harvesting, and account allocation.

#### Subchannel A. Working the Field
- Reading type: latent/lexical
- Scene or process: Seed is sown and covered, the crop is first watered, the land is worked under an agreement, and yield arrives.
- Active motifs: sowing seed `quranic:root_000303:B002/m01`; covering seed with soil `quranic:root_001307:B008/m01`; first watering of a crop `quranic:root_000393:B004/m01`; repairing land through sharecropping `quranic:root_000387:B003/m01`; crop or palm yield `quranic:root_000009:B007/m01`.
- Ayah anchors: ح ر ث at 42:20; ك ف ر at 42:26; خ ت م at 42:24; خ ب ر at 42:27; ء ت ي at 42:20.
- Synthesis: Harvest is unfolded into its hidden labor. Seed must be covered, watered, and placed within a working arrangement that restores land before its produce can arrive.

#### Subchannel B. Posting the Yield to an Account
- Reading type: mixed
- Scene or process: Work produces an acquisition that adheres to its actor and is divided into wages, shares, surplus, and provision.
- Active motifs: labor and earning `quranic:root_000303:B001/m01`; acquired outcome `quranic:root_001296:B001/m01`; an acquired act clinging to its doer `quranic:root_001220:B003/m01`; wage or reward `quranic:root_000015:B001/m01`; allotted share `quranic:root_001507:B005/m01`; surplus or bounty `quranic:root_001163:B001/m01`; apportioned provision `quranic:root_000560:B001/m01`.
- Ayah anchors: ح ر ث at 42:20; ك س ب at 42:22; ق ر ف at 42:23; ء ج ر at 42:23; ن ص ب at 42:20; ف ض ل at 42:22, 42:26; ر ز ق at 42:19, 42:27.
- Synthesis: The field's yield becomes an account: what one works for adheres as personal acquisition, then appears as a specified wage or share. Increase and bounty remain apportioned rather than ownerless abundance.

### 8. P2 Rain Release and Garden Reception (42:16-29)
- Semantic invariant: Relief requires both a released supply and a receptive place able to retain and convert it into growth.
- Surface relation: direct; luxuriant gardens appear at 42:22, rain after despair at 42:28, and earthly life at 42:29.
- Surprising reach: Mercy is given a full ecological mechanism, from follow-up rain and revived pasture to saturation, depressions, and rock basins that retain water.

#### Subchannel A. Rain After Despair
- Reading type: mixed
- Scene or process: Despairing dryness is interrupted by descending rain that spreads life and arrives as sustaining follow-up.
- Active motifs: rain bringing relief `quranic:root_001118:B001/m01`; rainfall or downward release `quranic:root_001492:B001/m01`; dry pasture revived by rain `quranic:root_001503:B004/m01`; rain as sustenance `quranic:root_000560:B003/m01`; despair at failed supply `quranic:root_001261:B001/m01`; follow-up rain `quranic:root_001684:B010/m01`.
- Ayah anchors: غ ي ث at 42:28; ن ز ل at 42:17, 42:27-28; ن ش ر at 42:28; ر ز ق at 42:19, 42:27; ق ن ط at 42:28; و ل ي at 42:28.
- Synthesis: The release is timed against exhaustion: after supply seems closed, rain descends, spreads, and revives. Its role as sustaining follow-up makes mercy a continuing provision rather than an isolated shower.

#### Subchannel B. Garden as Receiving Vessel
- Reading type: latent/lexical
- Scene or process: A sheltered garden receives measured water, becomes saturated, and stores excess in hollows and stone basins.
- Active motifs: tree-hidden garden `quranic:root_000266:B003/m01`; measured waterbag amount `quranic:root_000611:B002/m01`; saturation and quenching `quranic:root_000611:B003/m01`; water-holding depression `quranic:root_001675:B008/m01`; rock basin retaining rain `quranic:root_000434:B011/m01`; fertile yielding earth `quranic:root_000025:B002/m01`.
- Ayah anchors: ج ن ن at 42:22; ر و ض at 42:22; و ق ع at 42:22; خ ل ق at 42:29; ء ر ض at 42:27, 42:29.
- Synthesis: The garden is not a decorative endpoint but a receiving apparatus. Measured water quenches the soil, while depressions and rock hollows retain what would otherwise pass away.

### 9. P2 Documentary Marks (42:16-29)
- Semantic invariant: A claim acquires authority through durable marks and loses it through tampering, counterfeit construction, or erasure.
- Surface relation: direct; scripture, sealing, truth, words, fabrication, and erasure converge at 42:17 and 42:24.
- Surprising reach: The divine confirmation or removal of speech is rendered through the craft vocabulary of signatures, cutting, leather repair, cancellation, and deceptive surfaces.

#### Subchannel A. Authentication by Inscription
- Reading type: mixed
- Scene or process: Speech is fixed as text, impressed with a seal, signed, and thereby established as true.
- Active motifs: ordered written text `quranic:root_001283:B002/m01`; seal or imprint `quranic:root_000393:B002/m01`; signature or writing trace `quranic:root_001675:B011/m01`; establishment of truth `quranic:root_000347:B005/m01`; meaningful word or phrase `quranic:root_001316:B002/m01`.
- Ayah anchors: ك ت ب at 42:17; خ ت م at 42:24; و ق ع at 42:22; ح ق ق at 42:17-18, 42:24; ك ل م at 42:21, 42:24.
- Synthesis: Meaning becomes authoritative when it leaves a durable trace. Text, signature, and seal form an authentication sequence in which wording is materially established as truth.

#### Subchannel B. Cutting, Counterfeiting, and Erasing the Record
- Reading type: latent/lexical
- Scene or process: A marked surface can be cut for repair, torn destructively, fabricated, invalidated, or wiped clean.
- Active motifs: leather cut for repair and stitching `quranic:root_001150:B001/m01`; destructive cut or tear `quranic:root_001150:B002/m01`; fabrication of a lie `quranic:root_001150:B003/m01`; erasure of text or trace `quranic:root_001404:B001/m01`; cancellation or invalidation `quranic:root_000127:B002/m01`; deceptive patterned surface `quranic:root_001290:B009/m01`; fabricated speech `quranic:root_000434:B007/m01`.
- Ayah anchors: ف ر ي at 42:24; م ح و at 42:24; ب ط ل at 42:24; ك ذ ب at 42:24; خ ل ق at 42:29.
- Synthesis: The record is vulnerable to two opposed crafts: cutting can mend a surface or destroy it, while a counterfeit pattern can imitate a valid mark. Erasure goes further by removing the trace on which the claim depended.

### 10. P2 Return and Trace Removal (42:16-29)
- Semantic invariant: Return becomes effective through response and acceptance, followed by removal of the old trace and renewed increase.
- Surface relation: direct; repentance, acceptance, pardon, knowledge of deeds, response, and increase dominate 42:25-26.
- Surprising reach: Forgiveness is materialized as footprints erased by wind and covering lifted or replaced, after which growth resumes.

#### Subchannel A. Answer and Readmission
- Reading type: mixed
- Scene or process: An invitation to return receives an answer and culminates in acceptance.
- Active motifs: acceptance or reception `quranic:root_001198:B004/m01`; invitation to repentance `quranic:root_000189:B003/m01`; answer, response, or dialogue `quranic:root_000273:B003/m01`.
- Ayah anchors: ق ب ل at 42:25; ت و ب at 42:25; ج و ب at 42:16, 42:26.
- Synthesis: Return is dialogical rather than unilateral. A call is issued, the returning party answers, and reception completes the movement back into relation.

#### Subchannel B. Erasing the Old Track and Regrowing
- Reading type: latent/lexical
- Scene or process: The prior offense is covered and its track erased, allowing growth to begin after what was left behind.
- Active motifs: pardon as erasure `quranic:root_001032:B001/m01`; wind erasing a footprint `quranic:root_001032:B006/m01`; protective covering of guilt `quranic:root_001096:B002/m01`; covering or removing an offense `quranic:root_001307:B009/m01`; growth after leaving something behind `quranic:root_001032:B007/m01`; renewed increase `quranic:root_000657:B001/m01`.
- Ayah anchors: ع ف و at 42:25; غ ف ر at 42:23; ك ف ر at 42:26; ز ي د at 42:20, 42:23, 42:26.
- Synthesis: Pardon changes the terrain: the incriminating track is covered until it can no longer guide pursuit. The same lexical field then turns from disappearance to fresh growth, linking forgiveness with renewed capacity.

### 11. P3 Maritime Propulsion and Arrest (42:30-43)
- Semantic invariant: Movement depends on an enabling force and can be converted abruptly into stillness, entrapment, or destruction.
- Surface relation: direct; ships running on the sea, wind made still, vessels left motionless, and destruction for what people earn appear at 42:32-34.
- Surprising reach: The ship scene includes load-bearing backs, navigation marks, steering equipment, and the difference between controlled stability and lethal stagnation.

#### Subchannel A. Vessel Underway
- Reading type: mixed
- Scene or process: Wind drives a loaded vessel across a broad surface while visible markers orient its passage.
- Active motifs: broad abundant water `quranic:root_000086:B001/m01`; flowing current or sailing `quranic:root_000240:B001/m01`; propelling wind `quranic:root_000609:B003/m01`; back or supporting surface `quranic:root_000970:B002/m01`; load-bearing mount `quranic:root_000970:B005/m01`; marker, flag, or landmark `quranic:root_001040:B002/m01`.
- Ayah anchors: ب ح ر at 42:32; ج ر ي at 42:32; ر و ح at 42:33; ظ ه ر at 42:33; ع ل م at 42:32.
- Synthesis: The vessel rides the sea as a burden rides a back: current and wind supply movement, the surface bears the load, and markers make the transit intelligible. Propulsion and orientation are jointly necessary.

#### Subchannel B. Arrested Motion and Entrapment
- Reading type: mixed
- Scene or process: Motion is stopped; steering becomes stabilization, then stillness hardens into being stuck and exposed to destruction.
- Active motifs: stopping movement `quranic:root_000726:B001/m01`; rudder or stabilizing device `quranic:root_000726:B008/m01`; stagnation after motion `quranic:root_000590:B001/m01`; destruction `quranic:root_001618:B002/m01`; being trapped until destruction `quranic:root_001618:B003/m01`.
- Ayah anchors: س ك ن at 42:33; ر ك د at 42:33; و ب ق at 42:34.
- Synthesis: Stillness has two possible functions: a rudder can restrain motion to preserve control, but imposed calm can immobilize the whole vessel. Once arrest becomes entrapment, the medium of travel becomes the place of destruction.

### 12. P3 Impact, Matched Redress, and Repair (42:30-43)
- Semantic invariant: Harm travels from deed to impact, may be answered proportionally, and can finally be interrupted by pardon and repair.
- Surface relation: direct; affliction from what hands earn, requital equal to injury, victory after wrong, pardon, reconciliation, and forgiveness span 42:30 and 42:39-43.
- Surprising reach: Moral consequence is staged as a projectile hitting its target, a wound exceeding its boundary, a matched counterstroke, and a footprint that can still be erased.

#### Subchannel A. Deed Reaches Its Target
- Reading type: mixed
- Scene or process: What hands acquire travels outward and returns as a precisely striking affliction.
- Active motifs: impact hitting its intended target `quranic:root_000889:B003/m01`; calamity striking a person `quranic:root_000889:B004/m01`; deeds of the hands `quranic:root_001693:B009/m01`; acquired outcome `quranic:root_001296:B001/m01`; wound festering beyond its boundary `quranic:root_000138:B004/m01`.
- Ayah anchors: ص و ب at 42:30, 42:39; ي د ي at 42:30; ك س ب at 42:30, 42:34; ب غ ي at 42:39, 42:42.
- Synthesis: Consequence has a trajectory: handwork becomes acquisition, acquisition becomes a returning strike, and an unchecked injury crosses its proper limit. The scene makes causation both personal and spatial.

#### Subchannel B. Proportional Counterstroke
- Reading type: mixed
- Scene or process: A grievance is answered with a corresponding measure that restores the victim's right without exceeding the original harm.
- Active motifs: corresponding requital `quranic:root_000244:B001/m01`; equivalence `quranic:root_001397:B001/m01`; retaliatory example that deters repetition `quranic:root_001397:B002/m01`; victim's redress `quranic:root_001510:B002/m01`; grievance or claim of wrong `quranic:root_000967:B003/m01`.
- Ayah anchors: ج ز ي at 42:40; م ث ل at 42:40; ن ص ر at 42:39, 42:41; ظ ل م at 42:40-42.
- Synthesis: Redress mirrors rather than amplifies the first injury. Equivalence turns retaliation into a bounded counterexample whose function is restoration and deterrence, not renewed aggression.

#### Subchannel C. Erasure and Repair
- Reading type: mixed
- Scene or process: The chain of matching injury is stopped by erasing its trace, covering exposure, and repairing the relation.
- Active motifs: pardon as erasure `quranic:root_001032:B001/m01`; wind removing a footprint `quranic:root_001032:B006/m01`; practical repair `quranic:root_000876:B001/m01`; reconciliation `quranic:root_000876:B002/m01`; nurturing repair toward completion `quranic:root_000532:B002/m01`; protective covering `quranic:root_001096:B002/m01`.
- Ayah anchors: ع ف و at 42:30, 42:34, 42:40; ص ل ح at 42:40; ر ب ب at 42:36, 42:38; غ ف ر at 42:37, 42:43.
- Synthesis: Pardon does more than decline a counterstroke: it removes the track by which injury would continue to be followed. Repair and reconciliation then fill the cleared space with a restored relation.

### 13. P3 Escape Closed, Recourse Opened (42:30-43)
- Semantic invariant: Wrongdoing closes evasive exits while legitimate grievance opens a bounded avenue of recourse.
- Surface relation: direct; inability to escape, lack of protector, no place of evasion, justified self-defense, and the path against aggressors appear at 42:31 and 42:35-42.
- Surprising reach: The ethical distinction is spatialized as a no-exit enclosure for evasion and an extended public road for lawful redress.

#### Subchannel A. No Evasive Exit
- Reading type: mixed
- Scene or process: A pursued party cannot outrun reach, veer away, or find an opening in the enclosure.
- Active motifs: inability to elude pursuit `quranic:root_000985:B002/m01`; veering away or escaping `quranic:root_000378:B001/m01`; no-exit trap `quranic:root_000378:B002/m01`.
- Ayah anchors: ع ج ز at 42:31; ح ي ص at 42:35.
- Synthesis: Escape is tested as movement under pursuit. Inability becomes concrete when every turn remains inside the same enclosure and no lateral route leads out.

#### Subchannel B. Avenue for a Just Claim
- Reading type: mixed
- Scene or process: A wronged party enters an acknowledged road of redress grounded in a claim and bounded by the right violated.
- Active motifs: extended road or avenue `quranic:root_000672:B001/m01`; protector or ally `quranic:root_001684:B004/m01`; victim's redress `quranic:root_001510:B002/m01`; grievance or claim `quranic:root_000967:B003/m01`; aggression beyond the limit `quranic:root_000138:B003/m01`; owned or established right `quranic:root_000347:B003/m01`.
- Ayah anchors: س ب ل at 42:41-42; و ل ي at 42:31; ن ص ر at 42:39, 42:41; ظ ل م at 42:40-42; ب غ ي at 42:39, 42:42; ح ق ق at 42:42.
- Synthesis: Recourse is not an escape hatch but an open civic way for a recognized grievance. Its legitimacy comes from the injured right and ends where redress would itself cross into aggression.

### 14. P3 Collective Circulation (42:30-43)
- Semantic invariant: A community remains ordered by drawing judgment inward from its members and sending material support outward among them.
- Surface relation: direct; response to the Lord, prayer, mutual consultation, and spending from provision meet at 42:38.
- Surprising reach: Consultation is pictured as harvesting a substance from a collective, while expenditure becomes the outward circulation that sustains the same body.

#### Subchannel A. Extracting Counsel
- Reading type: mixed
- Scene or process: Participants are connected in dialogue so that a considered judgment can be drawn from them.
- Active motifs: harvesting honey `quranic:root_000827:B002/m01`; extracting an opinion through review `quranic:root_000827:B003/m01`; consultation and planning `quranic:root_000051:B007/m01`; answer or dialogue `quranic:root_000273:B003/m01`; connective relation between parties `quranic:root_000170:B003/m01`.
- Ayah anchors: ش و ر at 42:38; ء م ر at 42:38; ج و ب at 42:38; ب ي ن at 42:38.
- Synthesis: Counsel is gathered as a useful substance is drawn from many contributors. Dialogue connects the participants, and review extracts a judgment no single voice simply deposits ready-made.

#### Subchannel B. Sending Provision Through the Group
- Reading type: mixed
- Scene or process: Members rise to act and direct apportioned resources outward for the benefit of others.
- Active motifs: rising to undertake action `quranic:root_001273:B003/m01`; expenditure of resources `quranic:root_001537:B002/m01`; apportioned provision `quranic:root_000560:B001/m01`; prayer or benefit directed to another `quranic:root_000879:B002/m01`.
- Ayah anchors: ق و م at 42:38; ن ف ق at 42:38; ر ز ق at 42:38; ص ل و at 42:38.
- Synthesis: The collective is sustained by outward movement as well as inward deliberation. Received provision is actively redistributed, and prayer likewise directs benefit beyond the self.

### 15. P4 Exposure and Restricted Gaze (42:44-53)
- Semantic invariant: Judgment forces hidden loss into view while constraining the condemned to partial, lowered, or furtive sight.
- Surface relation: direct; public exposure, humiliation, stealthy glances, seeing punishment, and calls to look appear at 42:44-45 and 42:48.
- Surprising reach: Visibility is anatomized through posture and eye mechanics: bowing, subjugation, blinking, tear-struck sight, and edge-of-eye observation.

#### Subchannel A. Forced Display and Abasement
- Reading type: mixed
- Scene or process: The condemned are placed on display, their bodies lowered as they are made mutually visible.
- Active motifs: display for inspection `quranic:root_001001:B002/m01`; bowed or downcast posture `quranic:root_000412:B001/m01`; broken subjugation `quranic:root_000519:B001/m01`; parties facing and seeing one another `quranic:root_000531:B004/m01`.
- Ayah anchors: ع ر ض at 42:45, 42:48; خ ش ع at 42:45; ذ ل ل at 42:45; ر ء ي at 42:44-45.
- Synthesis: Exposure is imposed bodily. Those displayed cannot control the scene: humiliation lowers their posture even as concealment is removed and mutual visibility is forced upon them.

#### Subchannel B. Seeing from the Eye's Edge
- Reading type: mixed
- Scene or process: Direct vision contracts into blink-sized, concealed, or tear-obstructed glances from the margin of the eye.
- Active motifs: blink or edge of the eye `quranic:root_000931:B002/m01`; eye struck or filled with tears `quranic:root_000931:B003/m01`; concealed perception `quranic:root_000428:B001/m01`; faint flash like hidden lightning `quranic:root_000428:B004/m01`; direct gaze `quranic:root_001520:B001/m01`; ordinary seeing `quranic:root_000531:B001/m01`.
- Ayah anchors: ط ر ف at 42:45; خ ف ي at 42:45; ن ظ ر at 42:45; ر ء ي at 42:44-45.
- Synthesis: The command to see is answered by impaired visual access. Sight survives only as a furtive edge-glance, a blink, or a brief flash through tears, making restricted perception part of the punishment.

### 16. P4 Closed Mobility and No Refuge (42:44-53)
- Semantic invariant: Misorientation becomes irreversible when roads no longer lead back and no protector, shelter, or return remains.
- Surface relation: direct; error, path, protector, return, refuge, and the unavoidable day recur at 42:44, 42:46-47.
- Surprising reach: Spiritual loss is rendered through missing-object and stray-animal imagery before tightening into failed retreat, blocked repulsion, and absent shelter.

#### Subchannel A. From Misrouting to Loss
- Reading type: latent/lexical
- Scene or process: Departure from the route progresses from being off course to the condition of a lost object or stray animal.
- Active motifs: being off course `quranic:root_000913:B001/m01`; lost object `quranic:root_000913:B003/m01`; stray animal `quranic:root_000913:B005/m01`; extended road or avenue `quranic:root_000672:B001/m01`.
- Ayah anchors: ض ل ل at 42:44, 42:46; س ب ل at 42:44, 42:46.
- Synthesis: Error is a progressive spatial condition. One first leaves the road, then becomes something no longer locatable within an ordered field, and finally wanders without self-directed return.

#### Subchannel B. Return and Shelter Withdrawn
- Reading type: mixed
- Scene or process: Attempts to turn back or repel the outcome fail because no ally receives the fugitive and no refuge remains.
- Active motifs: protector or ally `quranic:root_001684:B004/m01`; return `quranic:root_000555:B001/m01`; repelling or turning back `quranic:root_000555:B002/m01`; place of refuge `quranic:root_001343:B001/m01`; arrival of the awaited event `quranic:root_000009:B001/m01`; prior opportunity before arrival `quranic:root_001198:B002/m01`.
- Ayah anchors: و ل ي at 42:44, 42:46; ر د د at 42:44, 42:47; ل ج ء at 42:47; ء ت ي at 42:47; ق ب ل at 42:47.
- Synthesis: Irreversibility is defined by failed motions: the event arrives, repulsion cannot push it away, and return finds neither receiver nor shelter. The repeated call to respond before arrival marks the last open interval.

### 17. P4 Reproductive Allotment and Closure (42:44-53)
- Semantic invariant: Reproductive possibility is sovereignly allocated through gifting, pairing, measure, fertility, and closure.
- Surface relation: direct; dominion, creation, gifts of females and males, pairing, barrenness, knowledge, and power fill 42:49-50.
- Surprising reach: The allocation of offspring expands into fertile ground, sterile wind, sealed stone, and a rain pocket, making fecundity a question of whether a bounded place can receive and release life.

#### Subchannel A. Gift, Pair, and Measure
- Reading type: mixed
- Scene or process: A sovereign giver assigns female, male, or paired offspring according to measured capacity.
- Active motifs: gift without exchange `quranic:root_001685:B001/m01`; female `quranic:root_000058:B001/m01`; male `quranic:root_000516:B001/m01`; pairing or classification `quranic:root_000652:B003/m01`; assigning a state `quranic:root_000248:B002/m01`; measured amount `quranic:root_001205:B001/m01`; capacity or power `quranic:root_001205:B003/m01`; sovereignty `quranic:root_001444:B003/m01`.
- Ayah anchors: و ه ب at 42:49; ء ن ث at 42:49-50; ذ ك ر at 42:49-50; ز و ج at 42:50; ج ع ل at 42:50; ق د ر at 42:50; م ل ك at 42:49.
- Synthesis: Offspring are neither random yield nor exchange payment. They are gifts assigned into categories and combinations under a measure that joins sovereign capacity to each resulting state.

#### Subchannel B. Fertility Versus Sealed Capacity
- Reading type: latent/lexical
- Scene or process: A receiving place may be fertile and moisture-bearing or closed, sterile, and unable to transmit generation.
- Active motifs: fertile soft ground `quranic:root_000058:B004/m01`; sterile womb `quranic:root_001037:B001/m01`; infertile wind `quranic:root_001037:B002/m01`; sealed imperforate rock `quranic:root_000434:B012/m01`; rain pocket held in rock `quranic:root_001685:B003/m01`; measuring before making `quranic:root_000434:B001/m01`.
- Ayah anchors: ء ن ث at 42:49-50; ع ق م at 42:50; خ ل ق at 42:49; و ه ب at 42:49.
- Synthesis: Barrenness is a closure of passage: womb, wind, and stone can all lack the capacity to carry life onward. Against that closure, fertile ground and water held within rock preserve the possibility of emergence.

### 18. P4 Mediated Transmission Across a Boundary (42:44-53)
- Semantic invariant: Communication crosses distance or concealment through encoding, controlled access, authorized relay, embodiment, and orientation.
- Surface relation: direct; revelation, speech from behind a veil, permission, messenger, spirit, scripture, light, guidance, and the straight path occupy 42:51-53.
- Surprising reach: Revelation appears as a complete communication architecture, from barely perceptible signal and guarded threshold to dispatched carrier, luminous beacon, and traversable route.

#### Subchannel A. Hidden Encoding
- Reading type: mixed
- Scene or process: Meaning is encoded in concealed speech, gesture, inscription, or faint sound before it is openly understood.
- Active motifs: hidden conveyance of knowledge `quranic:root_001633:B001/m01`; communicative gesture `quranic:root_001633:B002/m01`; inscribed communication `quranic:root_001633:B003/m01`; hidden sound `quranic:root_001633:B005/m01`; speech connecting speakers `quranic:root_001316:B001/m01`.
- Ayah anchors: و ح ي at 42:51-52; ك ل م at 42:51.
- Synthesis: Communication begins below full public speech. Gesture, inscription, and faint sound are alternate encodings of a meaning that can cross distance without exposing its source directly.

#### Subchannel B. The Guarded Threshold
- Reading type: mixed
- Scene or process: A boundary blocks direct access and places communication behind a curtain under guarded control.
- Active motifs: prevention of access `quranic:root_000294:B001/m01`; curtain or veil `quranic:root_000294:B002/m01`; gatekeeping office `quranic:root_000294:B003/m01`; concealment behind a surface `quranic:root_001642:B005/m01`; location on the far side `quranic:root_001642:B006/m01`.
- Ayah anchors: ح ج ب at 42:51; و ر ي at 42:51.
- Synthesis: The veil is not empty distance but an administered threshold. Direct passage is prevented, a gatekeeping function regulates access, and the source remains on the far side of a concealing surface.

#### Subchannel C. Authorized Relay
- Reading type: mixed
- Scene or process: Permission opens the threshold for a dispatched messenger to bear the communication onward.
- Active motifs: attentive hearing and acceptance `quranic:root_000022:B002/m01`; authorization or permission `quranic:root_000022:B004/m01`; dispatching an emissary `quranic:root_000563:B001/m01`; messenger or carried message `quranic:root_000563:B002/m01`.
- Ayah anchors: ء ذ ن at 42:51; ر س ل at 42:51.
- Synthesis: Relay depends on authorization at both ends: permission admits the message into transmission, while attentive reception completes its passage. The messenger is the moving carrier between those controlled points.

#### Subchannel D. Message Embodied as Spirit, Text, and Light
- Reading type: mixed
- Scene or process: The transmitted meaning takes forms that animate, preserve, and illuminate.
- Active motifs: life-giving spirit `quranic:root_000609:B001/m01`; ordered written text `quranic:root_001283:B002/m01`; illumination `quranic:root_001564:B001/m01`.
- Ayah anchors: ر و ح at 42:52; ك ت ب at 42:52; ن و ر at 42:52.
- Synthesis: Once relayed, the message is not a single medium. As spirit it animates, as scripture it preserves ordered content, and as light it makes a field perceptible.

#### Subchannel E. Signal Becomes a Route
- Reading type: mixed
- Scene or process: Illumination functions as a beacon, a guide moves ahead, and the receiver is set upon a straight road.
- Active motifs: beacon or landmark `quranic:root_001564:B005/m01`; guidance onto the road `quranic:root_001583:B001/m01`; guide as leading vanguard `quranic:root_001583:B003/m01`; straight road `quranic:root_000858:B001/m01`; assigning or transforming a state `quranic:root_000248:B002/m01`.
- Ayah anchors: ن و ر at 42:52; ه د ي at 42:52; ص ر ط at 42:52-53; ج ع ل at 42:52.
- Synthesis: Illumination becomes actionable when it serves as a landmark and a guide takes the forward position. Transmission therefore ends not in passive possession of information but in relocation onto a traversable path.

### 19. P4 Sensory Feedback of Gift and Handwork (42:44-53)
- Semantic invariant: What is received is tested in experience, while what is sent ahead by one's own action returns as felt consequence.
- Surface relation: direct; tasting mercy, rejoicing, what hands have sent ahead, affliction, and ingratitude meet at 42:48.
- Surprising reach: Experience is rendered as tongue and instrument testing, then reversed so the actor's projected handwork comes back as a precisely targeted impact.

#### Subchannel A. Tasting and Testing the Gift
- Reading type: mixed
- Scene or process: Mercy is sampled through taste and practical testing, producing joy that can swell into exultation.
- Active motifs: physical taste `quranic:root_000526:B001/m01`; experiential testing `quranic:root_000526:B002/m01`; testing a bow's performance `quranic:root_000526:B003/m01`; mercy received `quranic:root_000552:B001/m01`; joy `quranic:root_001140:B001/m01`; boastful exultation `quranic:root_001140:B002/m01`.
- Ayah anchors: ذ و ق at 42:48; ر ح م at 42:48; ف ر ح at 42:48.
- Synthesis: Reception is known by trial rather than description alone. Taste and instrument testing make mercy experientially verifiable, while joy exposes the risk that successful reception becomes self-congratulation.

#### Subchannel B. Sending the Deed Ahead
- Reading type: mixed
- Scene or process: The actor intentionally projects handwork forward before encountering its result.
- Active motifs: sending something in advance `quranic:root_001207:B004/m01`; directing or intending an action `quranic:root_001207:B010/m01`; deeds produced by the hands `quranic:root_001693:B009/m01`.
- Ayah anchors: ق د م at 42:48; ي د ي at 42:48.
- Synthesis: Action is pictured as an advance shipment. Intention gives it direction, the hands produce it, and the deed occupies the future before its maker arrives there.

#### Subchannel C. The Return Strike
- Reading type: mixed
- Scene or process: Advanced handwork returns as a targeted affliction whose pressure can provoke denial of the earlier gift.
- Active motifs: impact hitting its target `quranic:root_000889:B003/m01`; calamity striking a person `quranic:root_000889:B004/m01`; distress or harmful pressure `quranic:root_000755:B002/m01`; concealing or denying a blessing `quranic:root_001307:B004/m01`.
- Ayah anchors: ص و ب at 42:48; س و ء at 42:48; ك ف ر at 42:48.
- Synthesis: Consequence closes the loop by returning with the precision of a strike. Under pressure, the recipient can reinterpret the gift by covering or denying it, turning sensory knowledge into ingratitude.

## Standalone Subchannels

### S1. P1 The Strained Overhead Canopy (42:1-15)
- Reading type: mixed
- Scene or process: An elevated canopy is held over the world while fissure and celestial motion place it under visible strain.
- Active motifs: opening or fissure `quranic:root_001165:B001/m01`; sky as overhead canopy `quranic:root_000745:B004/m01`; upper direction `quranic:root_001188:B001/m01`; swimming or coursing through air `quranic:root_000666:B004/m01`; ascent and height `quranic:root_001042:B001/m01`.
- Ayah anchors: ف ط ر at 42:5, 42:11; س م و at 42:4-5, 42:11-12, 42:14; ف و ق at 42:5; س ب ح at 42:5; ع ل و at 42:4.
- Synthesis: The sky is a roof-like upper structure traversed by coursing bodies, yet it is also close to splitting. Praise below the threatened fissure reads as a stabilizing response within a cosmos whose height is dynamic rather than inert.

### S2. P2 Creature Broadcast and Reassembly (42:16-29)
- Reading type: mixed
- Scene or process: Created life is spread across a field through creeping and hidden circulation, yet remains available for later gathering.
- Active motifs: scattering or broadcasting creatures `quranic:root_000083:B001/m01`; creeping movement `quranic:root_000457:B001/m01`; hidden circulation `quranic:root_000457:B003/m01`; gathering dispersed beings `quranic:root_000259:B001/m01`; bringing into created form `quranic:root_000434:B002/m01`; spreading or unfolding `quranic:root_001503:B001/m01`.
- Ayah anchors: ب ث ث at 42:29; د ب ب at 42:29; ج م ع at 42:29; خ ل ق at 42:29; ن ش ر at 42:28.
- Synthesis: Creation moves outward as broadcast: living beings creep and circulate beyond immediate sight as the field unfolds. Gathering reverses that vector, holding dispersed life within the reach of reassembly.

### S3. P2 Affection Beyond the Wage (42:16-29)
- Reading type: mixed
- Scene or process: A requested reward is displaced from transaction toward kinship, affection, good action, and glad response.
- Active motifs: affection or love `quranic:root_001634:B001/m01`; kinship relation `quranic:root_001212:B003/m01`; wage or recompense `quranic:root_000015:B001/m01`; glad news opening the face `quranic:root_000120:B005/m01`; beneficent action `quranic:root_000323:B002/m01`.
- Ayah anchors: و د د at 42:23; ق ر ب at 42:17, 42:23; ء ج ر at 42:23; ب ش ر at 42:23; ح س ن at 42:23.
- Synthesis: The wage frame is retained only to be transformed. What answers the message is not a detached payment but affection located in relationship, visible in the opened face and extended through good action.

### S4. P3 The Braided Dispute (42:30-43)
- Reading type: latent/lexical
- Scene or process: Argument twists strands together, entangles opponents, and turns verbal pressure into a contest of leverage and footing.
- Active motifs: tightly twisted rope `quranic:root_000229:B001/m01`; entangled dispute `quranic:root_000229:B002/m01`; throwing an opponent down `quranic:root_000229:B003/m01`; hard ground under the contest `quranic:root_000229:B004/m01`.
- Ayah anchors: ج د ل at 42:35.
- Synthesis: Disputation is a braided mechanism rather than loose talk: strands tighten, participants become entangled, and each tries to use the tension to throw the other onto hard ground. The image materializes resistance to the signs as self-tightening conflict.

### S5. P3 Boundary Control Under Anger (42:30-43)
- Reading type: mixed
- Scene or process: Provocation approaches a boundary; disciplined actors step aside from excess, contain eruptive anger, and cover the offense.
- Active motifs: moving or keeping to the side `quranic:root_000262:B003/m01`; exceeding a limit `quranic:root_001134:B002/m01`; eruptive wrath `quranic:root_001092:B001/m01`; protective covering `quranic:root_001096:B001/m01`; lagging behind the good `quranic:root_000013:B001/m01`.
- Ayah anchors: ج ن ب at 42:37; ف ح ش at 42:37; غ ض ب at 42:37; غ ف ر at 42:37; ء ث م at 42:37.
- Synthesis: Restraint is spatial and thermal: one keeps to the side of boundary-breaking conduct and contains anger before it erupts into action. Covering the offense prevents provocation from reproducing itself, while sin appears as falling behind the good course.

### S6. P4 The Household as Total Stake (42:44-53)
- Reading type: mixed
- Scene or process: Commercial loss expands into the loss of self and household, disclosed fully at the final standing.
- Active motifs: loss of trading capital `quranic:root_000409:B002/m01`; household or kin group `quranic:root_000064:B001/m01`; self or personal entity `quranic:root_001533:B012/m01`; resurrection standing `quranic:root_001273:B013/m01`.
- Ayah anchors: خ س ر at 42:45; ء ه ل at 42:45; ن ف س at 42:45; ق و م at 42:45.
- Synthesis: Loss is first legible as exhausted capital, then widens until the trader, the household, and the entire relational estate are gone. The final standing functions as the accounting moment when that total exposure can no longer be deferred.

### S7. Whole-Surah Lunar Timekeeping
- Reading type: latent/lexical
- Scene or process: The moon advances night by night through named stellar lodgings that divide its course into an ordered cycle.
- Active motifs: moon entering a nightly station `quranic:root_000018:B008/m01`; al-Ghafr as a three-star lunar mansion `quranic:root_001096:B006/m01`; the Heart of the Scorpion as a known star `quranic:root_001248:B010/m01`; al-Iklil as an encircling lunar mansion `quranic:root_001315:B005/m01`; assigned lodging or station `quranic:root_001492:B003/m01`; al-Na'a'im among the lunar mansions `quranic:root_001525:B007/m01`.
- Ayah anchors: ء خ ذ at 42:6, 42:9; غ ف ر at 42:5, 42:23, 42:37, 42:43; ق ل ب at 42:24; ك ل ل at 42:9, 42:12, 42:33; ن ز ل at 42:15, 42:17, 42:27-28; ن ع م at 42:11.
- Synthesis: The moon does not cross an undifferentiated sky; each night places it in a recognizable lodging within a measured sequence. This materializes the surah's divine measure and appointed return, while pressing human haste about the Hour against a celestial order that advances station by station.

### S8. Whole-Surah Perfume Preparation and Diffusion
- Reading type: latent/lexical
- Scene or process: Aromatic material is pounded, compounded, applied to body or garment, released into the air, and recognized by smell.
- Active motifs: broad stone for pounding perfume `quranic:root_000879:B008/m01`; perfume compound and its application `quranic:root_000434:B010/m01`; camphor as aromatic material `quranic:root_001307:B011/m01`; perfuming associated with women and garments `quranic:root_000058:B007/m01`; fragrance spreading outward `quranic:root_001503:B003/m01`; perceiving fragrance or corruption by smell `quranic:root_000609:B004/m01`.
- Ayah anchors: ص ل و at 42:38; خ ل ق at 42:29, 42:49; ك ف ر at 42:26, 42:48; ء ن ث at 42:49-50; ن ش ر at 42:28; ر و ح at 42:33, 42:52.
- Synthesis: Preparation converts a hidden aromatic capacity into a trace that leaves its point of application and becomes perceptible at a distance. The scene reframes the surah's movement from concealed communication to public guidance: an unseen source becomes known through a diffusing effect rather than direct sight.

### S9. Whole-Surah Turning Water-Lift
- Reading type: latent/lexical
- Scene or process: An upright well apparatus uses axle, wheel, toothed pulley, timber, and counterweight to raise water or a balanced load.
- Active motifs: well winch or water-lifting machine `quranic:root_000373:B016/m01`; turning handle and iron pulley axle `quranic:root_000610:B006/m01`; wheel for drawing water or hauling loads `quranic:root_000987:B003/m01`; counterbalancing load `quranic:root_000991:B004/m01`; toothed upper pulley `quranic:root_001188:B013/m01`; upright component of the well pulley `quranic:root_001273:B012/m01`; well timber named for its form `quranic:root_001525:B007/m02`.
- Ayah anchors: ح و ل at 42:7; ر و د at 42:20; ع ج ل at 42:18; ع د ل at 42:15; ف و ق at 42:5; ق و م at 42:13, 42:15, 42:38, 42:45, 42:52; ن ع م at 42:11.
- Synthesis: Vertical support, rotation, meshing teeth, and an opposing weight cooperate to bring an inaccessible supply upward. This materializes the surah's balance and apportioned provision as coordinated work: measure is the mechanism by which a resource below becomes available above.

### S10. Whole-Surah Recurrent Milking
- Reading type: latent/lexical
- Scene or process: Grazing fills the udder; a retained portion primes the next yield, massage releases it, fingertips draw it, and milk gathers again between milkings.
- Active motifs: residual milk left to summon the next flow `quranic:root_000478:B003/m01`; udder filling and gathering milk `quranic:root_000555:B007/m01`; successive flow of milk `quranic:root_000563:B006/m01`; abundant milk after pasture `quranic:root_000810:B003/m01`; milking with the fingertips `quranic:root_001165:B005/m01`; milk returning between two milkings `quranic:root_001188:B006/m01`; massaging the udder to induce letdown `quranic:root_001416:B001/m01`.
- Ayah anchors: د ع و at 42:13, 42:15; ر د د at 42:44, 42:47; ر س ل at 42:48, 42:51; ش ك ر at 42:23, 42:33; ف ط ر at 42:5, 42:11; ف و ق at 42:5; م ر ي at 42:18.
- Synthesis: Provision appears as a renewable but interval-bound flow whose continuity depends on pasture, retained supply, patient handling, and return between extractions. The scene supports the surah's measured expansion of provision and mercy after restraint: delay is replenishment, not proof that the source is empty.

### S11. Whole-Surah Kindling Hidden Fire
- Reading type: latent/lexical
- Scene or process: Latent fire is struck from stone or firestick, preserved in embers, stirred into flame, and brought close enough to warm, roast, or burn.
- Active motifs: weak sparks struck from stone or hoof `quranic:root_000286:B011/m01`; fire-striking white flint `quranic:root_001416:B002/m01`; concealed fire emerging from a firestick `quranic:root_001642:B002/m01`; stirring embers back into flame `quranic:root_001639:B005/m01`; poker or implement that agitates fire `quranic:root_000303:B005/m01`; ignition and blazing flame `quranic:root_000708:B001/m01`; exposure to fire for warmth, roasting, or burning `quranic:root_000879:B001/m01`.
- Ayah anchors: ح ب ب at 42:40; م ر ي at 42:18; و ر ي at 42:51; و ر ث at 42:14; ح ر ث at 42:20; س ع ر at 42:7; ص ل و at 42:38.
- Synthesis: What begins as a concealed potential or negligible spark becomes consequential through striking, preservation, and repeated agitation. This materializes the surah's warning of the Blaze and the return of deeds: an apparently small cause can be tended into the fire that finally meets its maker.

### S12. Whole-Surah Load Animal Under the Saddle
- Reading type: latent/lexical
- Scene or process: A pack and wooden saddle are placed over a protective pad, but pressure abrades the camel's back until pain or exhaustion arrests travel.
- Active motifs: pack carried on the back `quranic:root_000373:B012/m01`; wooden saddle frame `quranic:root_001029:B009/m01`; protective pad beneath the saddle `quranic:root_001684:B011/m01`; riding abrasion or saddle sore `quranic:root_001675:B010/m01`; underside of the camel's foot `quranic:root_000966:B007/m01`; camel halted by exhaustion, illness, or fracture `quranic:root_000286:B005/m01`.
- Ayah anchors: ح و ل at 42:7; ع ظ م at 42:4; و ل ي at 42:6, 42:8-9, 42:28, 42:31, 42:44, 42:46; و ق ع at 42:22; ظ ل ل at 42:33; ح ب ب at 42:40.
- Synthesis: Transport depends on how burden, frame, padding, back, and foot meet; a badly mediated load turns carriage into injury and then immobility. The scene materializes the surah's routes, entrusted burdens, and failed escape by showing that protective care determines whether a bearer can continue.

### S13. Whole-Surah Market Valuation
- Reading type: latent/lexical
- Scene or process: An active market appraises goods, sets a price, raises bids, resolves shared ownership, and transfers a sale at a known cost.
- Active motifs: requesting an increased bid `quranic:root_000657:B004/m01`; market price and its setting `quranic:root_000708:B003/m01`; appraisal and pricing of goods `quranic:root_001273:B010/m01`; market becoming active and saleable goods moving `quranic:root_001273:B018/m01`; co-owners bidding until one buys the others' shares `quranic:root_001274:B004/m01`; transferring a sale at its known purchase price `quranic:root_001684:B014/m01`.
- Ayah anchors: ز ي د at 42:20, 42:23, 42:26; س ع ر at 42:7; ق و م at 42:13, 42:15, 42:38, 42:45, 42:52; ق و ي at 42:19; و ل ي at 42:6, 42:8-9, 42:28, 42:31, 42:44, 42:46.
- Synthesis: Value emerges through a public sequence of appraisal, demand, competitive increase, and acknowledged transfer. This reframes the surah's balance, harvest, reward, and loss in concrete exchange terms, while sharpening 42:23: affection near kin is requested precisely where a market wage could have been named but is not.

### S14. Whole-Surah Debt Transfer and Discharge
- Reading type: latent/lexical
- Scene or process: Credit creates an obligation; a claimant pursues the right, the debt may be assigned to another party, and payment finally discharges it.
- Active motifs: claimant pursuing a debt or right `quranic:root_000175:B005/m01`; collecting and satisfying a debt `quranic:root_000244:B003/m01`; transferring a debt to another debtor `quranic:root_000373:B010/m01`; financial debt, loan, or credit sale `quranic:root_000504:B003/m01`; paying and taking receipt of the right due `quranic:root_001237:B006/m01`.
- Ayah anchors: ت ب ع at 42:15; ج ز ي at 42:40; ح و ل at 42:7; د ي ن at 42:13, 42:21; ق ض ي at 42:14, 42:21.
- Synthesis: Assignment can change who carries an obligation, but it does not erase the claimant or the amount due; only settlement closes the account. This materializes the surah's accountability and proportional recompense as a right that survives transfer until it is answered in full.

### S15. Cross-Pericope Guest Reception (P1-P4)
- Reading type: latent/lexical
- Scene or process: P1-P4; role-progression bridge: a host calls, a traveler carries provisions, a lodging is prepared, and the arriving guest receives food and drink from gathered vessels.
- Active motifs: invitation by spoken call, including a call to food `quranic:root_000478:B001/m01`; edible sustenance `quranic:root_000560:B002/m01`; stored travel provisions `quranic:root_000657:B005/m01`; quickly presented food or milk `quranic:root_000987:B005/m01`; palatable water, food, or drink `quranic:root_000994:B001/m01`; honoring a guest with gathered food `quranic:root_001222:B003/m01`; vessel gathering food or water `quranic:root_001222:B004/m01`; prepared lodging and fare for an arriving guest `quranic:root_001492:B005/m01`.
- Ayah anchors: د ع و at 42:13, 42:15; ر ز ق at 42:12, 42:19, 42:27, 42:38; ز ي د at 42:20, 42:23, 42:26; ع ج ل at 42:18; ع ذ ب at 42:16, 42:21, 42:26, 42:42, 42:44-45; ق ر ي at 42:7; ن ز ل at 42:15, 42:17, 42:27-28.
- Synthesis: The bridge is a host-to-guest role progression: invitation becomes travel, arrival, prepared place, and served provision. This supports the surah's call-and-response reading by making provision an act of reception rather than ambient wealth; what is offered reaches its purpose when the called guest arrives and accepts it.

### S16. Cross-Pericope Congregation Formed for Prayer (P1-P4)
- Reading type: mixed
- Scene or process: P1-P4; repeated-scene bridge: a summons gathers worshippers under a leader, turns them toward one direction, and orders their bodies through standing, bowing, and prayer.
- Active motifs: summons to approach `quranic:root_000383:B009/m01`; gathering place, day, or call that assembles people `quranic:root_000259:B004/m01`; imam or person followed `quranic:root_000053:B009/m01`; designated place of prayer `quranic:root_000879:B007/m01`; qibla as shared direction `quranic:root_001198:B005/m01`; bodily standing in prayer `quranic:root_001273:B002/m01`; bending with hands on knees or prostrating `quranic:root_000220:B006/m01`; prescribed prayer with standing, bowing, and prostration `quranic:root_000879:B003/m01`.
- Ayah anchors: ح ي ي at 42:9, 42:36; ج م ع at 42:7, 42:15, 42:29; ء م م at 42:7-8; ص ل و at 42:38; ق ب ل at 42:3, 42:25, 42:47; ق و م at 42:13, 42:15, 42:38, 42:45, 42:52; ج ب ي at 42:13.
- Synthesis: The bridge is a repeated scene signature of summons, assembly, leadership, common orientation, and coordinated posture. It materializes the surah's answer to religious division: unity is enacted as many bodies accepting one direction and one ordered rite, not asserted as a loose collective label.

### S17. Cross-Pericope Wound Treatment and Relapse (P1-P4)
- Reading type: latent/lexical
- Scene or process: P1-P4; causal-sequence bridge: a sore festers, pus gathers, the wound is probed and drained, a crust forms, and recovery remains vulnerable to relapse.
- Active motifs: ulcer festering with pus `quranic:root_000025:B011/m01`; pus gathered inside an abscess or wound `quranic:root_000282:B003/m01`; probing, measuring, and treating a deep head wound `quranic:root_000295:B004/m01`; blood or pus discharged from an abscess `quranic:root_001550:B005/m01`; dried wound skin forming and peeling away `quranic:root_001220:B001/m01`; illness or wound worsening again after improvement `quranic:root_001096:B004/m01`; fever or illness departing in recovery `quranic:root_001148:B010/m01`; consciousness and strength returning after illness `quranic:root_001188:B005/m01`.
- Ayah anchors: ء ر ض at 42:4-5, 42:11-12, 42:27, 42:29, 42:31, 42:42, 42:49, 42:53; ج ي ء at 42:14; ح ج ج at 42:15-16; ن ك ر at 42:47; ق ر ف at 42:23; غ ف ر at 42:5, 42:23, 42:37, 42:43; ف ر ق at 42:7, 42:13-14; ف و ق at 42:5.
- Synthesis: The bridge is a causal treatment sequence, not a general illness theme: hidden corruption must be exposed and removed before closure, restored strength, and durable recovery. This usefully pressures the surah's pardon-and-repair reading by showing why surface closure is insufficient; an unprobed injury can relapse after apparent improvement.

### S18. Cross-Pericope Bow Prepared and Aimed (P1-P4)
- Reading type: latent/lexical
- Scene or process: P1-P4; causal-mechanical bridge: an arrow is smoothed and fletched, its nock and the bow's string seats are prepared, tension separates string from bow, and the archer grips and aims.
- Active motifs: smooth finished arrow shaft `quranic:root_000434:B008/m01`; feathering fixed to an arrow `quranic:root_000970:B011/m01`; arrow nock that receives the string `quranic:root_001188:B009/m01`; grooves prepared for the bowstring `quranic:root_000303:B007/m01`; taut string standing away from the bow's belly `quranic:root_000170:B008/m01`; bow grip or handle `quranic:root_001693:B013/m01`; deliberate orientation of arrow or spear toward a target `quranic:root_000053:B012/m01`.
- Ayah anchors: خ ل ق at 42:29, 42:49; ظ ه ر at 42:33; ف و ق at 42:5; ح ر ث at 42:20; ب ي ن at 42:14-15, 42:21, 42:38; ي د ي at 42:30, 42:48; ء م م at 42:7-8.
- Synthesis: The bridge is a causal preparation-to-aim sequence: finish, feather, notch, string, tension, grip, and orientation jointly determine where the shot will go. This materializes the surah's straight guidance and deeds sent ahead as deliberate direction-setting, pressing against any reading of the eventual impact as accidental or detached from prior intention.

### S19. The Rein, the Pace, and the Veering Horse
- Reading type: latent/lexical
- Scene or process: A rider extends the reins to accelerate, settles into a controlled gait, repeats the run, and must keep exuberant speed from turning into lateral deviation.
- Active motifs: horse exulting or showing off in its run `quranic:root_000138:B007/m01`; rider extending the reins to increase speed `quranic:root_000151:B007/m01`; controlled equine gait below full gallop `quranic:root_001212:B014/m01`; successive runs following one another `quranic:root_001118:B005/m01`; horse veering sideways and resisting a straight line `quranic:root_001001:B012/m01`.
- Ayah anchors: ب غ ي at 42:14, 42:27, 42:39, 42:42; ب ل غ at 42:48; ق ر ب at 42:17, 42:23; غ ي ث at 42:28; ع ر ض at 42:45, 42:48.
- Synthesis: Speed is useful only while rein, gait, and line remain coordinated; exuberance can convert forward motion into sideways resistance. This usefully pressures the surah's contrast between haste and straight guidance: acceleration does not count as progress when the traveler no longer holds the course.

### S20. Divorce, Return, and Renewed Courtship
- Reading type: latent/lexical
- Scene or process: An irrevocable separation returns a woman to her family, suitors approach by message, and a new bond culminates in the bride's conveyance to an affectionate spouse.
- Active motifs: divorce that cuts off return to the former marriage `quranic:root_000170:B012/m01`; divorced woman returned to her family `quranic:root_000555:B006/m01`; eligible woman receiving courtship messages `quranic:root_000563:B009/m01`; bride conveyed to her husband `quranic:root_001583:B006/m01`; affectionate wife who openly loves her spouse `quranic:root_000996:B005/m01`.
- Ayah anchors: ب ي ن at 42:14-15, 42:21, 42:38; ر د د at 42:44, 42:47; ر س ل at 42:48, 42:51; ه د ي at 42:13, 42:52; ع ر ب at 42:7.
- Synthesis: The progression distinguishes return from reversal: going back to one's family closes one bond but creates the social position from which another courtship can begin. This reframes the surah's repeated language of return and kinship by showing that mercy may redirect a life into a renewed household rather than restore the prior state.

### S21. Binding Charm and Releasing Rite
- Reading type: latent/lexical
- Scene or process: A charm or facing bead seeks to bind attention and relationship, while recited incantation and a counter-rite seek to break the affliction.
- Active motifs: binding charm that seizes sight, judgment, or marriage `quranic:root_000018:B004/m01`; bead intended to turn one person's face toward another `quranic:root_001198:B016/m01`; healing incantation recited over afflicted persons or unseen beings `quranic:root_001010:B003/m01`; nushra rite intended to release an affliction `quranic:root_001503:B008/m01`.
- Ayah anchors: ء خ ذ at 42:6, 42:9; ق ب ل at 42:3, 42:25, 42:47; ع ز م at 42:43; ن ش ر at 42:28.
- Synthesis: The scene is organized by reversal: concealed words and objects first constrain agency, then a second recited operation attempts release. This pressures the surah's account of revelation, mediation, and protection by contrasting guidance that opens a path with hidden techniques that claim control over another person's face, judgment, or bond.

### S22. Hide Prepared as a Waterskin
- Reading type: latent/lexical
- Scene or process: A hide is stripped and opened, treated in measured tanning doses, stitched at its edges, formed into a vessel, filled, and ruined if left uncared for.
- Active motifs: removing the outer skin from a hide `quranic:root_000120:B004/m01`; opening and skinning a hide between its legs `quranic:root_000789:B006/m01`; small measured dose of tanning agent `quranic:root_001533:B007/m01`; stitching one hide edge to another `quranic:root_000121:B006/m01`; tanned leather made into a vessel `quranic:root_001220:B002/m01`; gathering water or milk in a waterskin `quranic:root_001249:B008/m01`; waterskin decaying after prolonged neglect `quranic:root_001237:B007/m01`.
- Ayah anchors: ب ش ر at 42:23, 42:51; ش ر ع at 42:13, 42:21; ن ف س at 42:11, 42:45; ب ص ر at 42:11, 42:27; ق ر ف at 42:23; ق ل د at 42:12; ق ض ي at 42:14, 42:21.
- Synthesis: Receptive capacity is manufactured through removal, measured treatment, and joined boundaries; the same vessel loses that capacity when custody lapses. This materializes the surah's provision and entrusted care: receiving abundance requires a prepared, maintained container rather than mere access to the source.

### S23. Bread Baked Before Maturity
- Reading type: latent/lexical
- Scene or process: Dough is worked until cohesive, placed in an excavated oven, and baked immediately even though its preparation has not fully matured.
- Active motifs: kneading dough until it gains strength and cohesion `quranic:root_001444:B001/m01`; pit-like oven excavated for baking `quranic:root_000708:B009/m01`; dough baked at once before reaching full readiness `quranic:root_001165:B006/m01`.
- Ayah anchors: م ل ك at 42:5, 42:49; س ع ر at 42:7; ف ط ر at 42:5, 42:11.
- Synthesis: The oven can finish a prepared loaf, but heat cannot recover maturation skipped through haste. This compact craft scene usefully pressures the surah's impatient demand for the Hour: forcing an outcome early is not the same as bringing a measured process to completion.

### S24. Funeral Concealment and Return
- Reading type: latent/lexical
- Scene or process: A death is followed by shrouding and burial, mourning and estate transfer, yet concealment in the earth is reversed by renewed life.
- Active motifs: a single occurrence or state of death `quranic:root_001454:B008/m01`; shrouding or placing the dead in a grave `quranic:root_000266:B009/m01`; sides of the grave `quranic:root_000840:B004/m01`; burial as disappearance into the earth `quranic:root_000913:B002/m01`; lamentation and weeping for the dead `quranic:root_001633:B009/m01`; estate passing from the deceased to an heir `quranic:root_001639:B001/m01`; dead person restored to life `quranic:root_001503:B002/m01`.
- Ayah anchors: م و ت at 42:9; ج ن ن at 42:7, 42:22; ص ب ر at 42:33, 42:43; ض ل ل at 42:18, 42:44, 42:46; و ح ي at 42:3, 42:7, 42:13, 42:51-52; و ر ث at 42:14; ن ش ر at 42:28.
- Synthesis: Burial appears to complete disappearance: the body is enclosed, mourners remain, and property moves to new hands. Resurrection reverses that apparent finality, materially supporting the surah's gathering and return by showing that earthly concealment and estate settlement do not terminate the person.

### S25. Marked Offering Conveyed to the Sanctuary
- Reading type: latent/lexical
- Scene or process: A pilgrim intends the sacred destination, marks an offering animal, conveys it to the sanctuary, prepares the blade, and relinquishes the gift at the place of sacrifice.
- Active motifs: intentional pilgrimage toward a sacred destination `quranic:root_000295:B001/m01`; sacrificial offering intended to draw near to God `quranic:root_001212:B005/m01`; collar marking an animal as a dedicated offering `quranic:root_001249:B002/m01`; offering animal or wealth conveyed to the sanctuary `quranic:root_001583:B005/m01`; erected stone used for sacrifice `quranic:root_001507:B002/m01`; blade sharpened on stone `quranic:root_001675:B009/m01`; knife bringing the slaughtered animal to stillness `quranic:root_000726:B007/m01`.
- Ayah anchors: ح ج ج at 42:15-16; ق ر ب at 42:17, 42:23; ق ل د at 42:12; ه د ي at 42:13, 42:52; ن ص ب at 42:20; و ق ع at 42:22; س ك ن at 42:33.
- Synthesis: The rite is a directed transfer: intention selects the destination, the collar changes the animal's status, conveyance removes it from ordinary use, and sacrifice completes relinquishment. This materializes the surah's ordained way and nearness to God as purposeful surrender, not proximity claimed without cost.

### S26. Burrow Hunt Through the Second Exit
- Reading type: latent/lexical
- Scene or process: A hunter identifies a through-burrow, blocks or probes one opening with a stick, and forces the hidden animal to emerge from the other exit.
- Active motifs: cutting, hollowing, or opening a passage `quranic:root_000273:B001/m01`; underground tunnel with a through-exit `quranic:root_001537:B003/m01`; luring a hyena or jerboa out by obstructing another burrow opening `quranic:root_000452:B006/m01`.
- Ayah anchors: ج و ب at 42:16, 42:26, 42:38, 42:47; ن ف ق at 42:38; خ ي ر at 42:36.
- Synthesis: The animal's hidden route is not a refuge once both openings are understood; the apparent alternative exit becomes the hunter's controlled point of emergence. This materializes the surah's denial of evasion and shelter by showing how concealed mobility can be converted into a forced disclosure.

### S27. Memory Held Without the Page
- Reading type: latent/lexical
- Scene or process: Material is retained in the heart, recited without consulting a written copy, recalled after absence, or lost when preservation fails.
- Active motifs: recitation from memory without a book `quranic:root_000970:B019/m01`; bringing something back to mind after forgetting `quranic:root_000516:B003/m01`; loss of memorized material `quranic:root_000913:B004/m01`.
- Ayah anchors: ظ ه ر at 42:33; ذ ك ر at 42:49-50; ض ل ل at 42:18, 42:44, 42:46.
- Synthesis: The page and the person are distinct repositories: inward retention can carry wording beyond the written object, but that internal store can also fail. This supports the surah's revelation-and-guidance reading by showing that receiving a message is not the same as preserving it in active memory.


