Surah: 43. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S43 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s043/surah.r2/text.md =====
# Surah 43

- 43:1 حمٓ
- 43:2 وَٱلْكِتَٰبِ ٱلْمُبِينِ
- 43:3 إِنَّا جَعَلْنَٰهُ قُرْءَٰنًا عَرَبِيًّۭا لَّعَلَّكُمْ تَعْقِلُونَ
- 43:4 وَإِنَّهُۥ فِىٓ أُمِّ ٱلْكِتَٰبِ لَدَيْنَا لَعَلِىٌّ حَكِيمٌ
- 43:5 أَفَنَضْرِبُ عَنكُمُ ٱلذِّكْرَ صَفْحًا أَن كُنتُمْ قَوْمًۭا مُّسْرِفِينَ
- 43:6 وَكَمْ أَرْسَلْنَا مِن نَّبِىٍّۢ فِى ٱلْأَوَّلِينَ
- 43:7 وَمَا يَأْتِيهِم مِّن نَّبِىٍّ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- 43:8 فَأَهْلَكْنَآ أَشَدَّ مِنْهُم بَطْشًۭا وَمَضَىٰ مَثَلُ ٱلْأَوَّلِينَ
- 43:9 وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ خَلَقَهُنَّ ٱلْعَزِيزُ ٱلْعَلِيمُ
- 43:10 ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَجَعَلَ لَكُمْ فِيهَا سُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
- 43:11 وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
- 43:12 وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا وَجَعَلَ لَكُم مِّنَ ٱلْفُلْكِ وَٱلْأَنْعَٰمِ مَا تَرْكَبُونَ
- 43:13 لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
- 43:14 وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ
- 43:15 وَجَعَلُوا۟ لَهُۥ مِنْ عِبَادِهِۦ جُزْءًا ۚ إِنَّ ٱلْإِنسَٰنَ لَكَفُورٌۭ مُّبِينٌ
- 43:16 أَمِ ٱتَّخَذَ مِمَّا يَخْلُقُ بَنَاتٍۢ وَأَصْفَىٰكُم بِٱلْبَنِينَ
- 43:17 وَإِذَا بُشِّرَ أَحَدُهُم بِمَا ضَرَبَ لِلرَّحْمَٰنِ مَثَلًۭا ظَلَّ وَجْهُهُۥ مُسْوَدًّۭا وَهُوَ كَظِيمٌ
- 43:18 أَوَمَن يُنَشَّؤُا۟ فِى ٱلْحِلْيَةِ وَهُوَ فِى ٱلْخِصَامِ غَيْرُ مُبِينٍۢ
- 43:19 وَجَعَلُوا۟ ٱلْمَلَٰٓئِكَةَ ٱلَّذِينَ هُمْ عِبَٰدُ ٱلرَّحْمَٰنِ إِنَٰثًا ۚ أَشَهِدُوا۟ خَلْقَهُمْ ۚ سَتُكْتَبُ شَهَٰدَتُهُمْ وَيُسْـَٔلُونَ
- 43:20 وَقَالُوا۟ لَوْ شَآءَ ٱلرَّحْمَٰنُ مَا عَبَدْنَٰهُم ۗ مَّا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَخْرُصُونَ
- 43:21 أَمْ ءَاتَيْنَٰهُمْ كِتَٰبًۭا مِّن قَبْلِهِۦ فَهُم بِهِۦ مُسْتَمْسِكُونَ
- 43:22 بَلْ قَالُوٓا۟ إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّهْتَدُونَ
- 43:23 وَكَذَٰلِكَ مَآ أَرْسَلْنَا مِن قَبْلِكَ فِى قَرْيَةٍۢ مِّن نَّذِيرٍ إِلَّا قَالَ مُتْرَفُوهَآ إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّقْتَدُونَ
- 43:24 ۞ قَٰلَ أَوَلَوْ جِئْتُكُم بِأَهْدَىٰ مِمَّا وَجَدتُّمْ عَلَيْهِ ءَابَآءَكُمْ ۖ قَالُوٓا۟ إِنَّا بِمَآ أُرْسِلْتُم بِهِۦ كَٰفِرُونَ
- 43:25 فَٱنتَقَمْنَا مِنْهُمْ ۖ فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- 43:26 وَإِذْ قَالَ إِبْرَٰهِيمُ لِأَبِيهِ وَقَوْمِهِۦٓ إِنَّنِى بَرَآءٌۭ مِّمَّا تَعْبُدُونَ
- 43:27 إِلَّا ٱلَّذِى فَطَرَنِى فَإِنَّهُۥ سَيَهْدِينِ
- 43:28 وَجَعَلَهَا كَلِمَةًۢ بَاقِيَةًۭ فِى عَقِبِهِۦ لَعَلَّهُمْ يَرْجِعُونَ
- 43:29 بَلْ مَتَّعْتُ هَٰٓؤُلَآءِ وَءَابَآءَهُمْ حَتَّىٰ جَآءَهُمُ ٱلْحَقُّ وَرَسُولٌۭ مُّبِينٌۭ
- 43:30 وَلَمَّا جَآءَهُمُ ٱلْحَقُّ قَالُوا۟ هَٰذَا سِحْرٌۭ وَإِنَّا بِهِۦ كَٰفِرُونَ
- 43:31 وَقَالُوا۟ لَوْلَا نُزِّلَ هَٰذَا ٱلْقُرْءَانُ عَلَىٰ رَجُلٍۢ مِّنَ ٱلْقَرْيَتَيْنِ عَظِيمٍ
- 43:32 أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- 43:33 وَلَوْلَآ أَن يَكُونَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ لَّجَعَلْنَا لِمَن يَكْفُرُ بِٱلرَّحْمَٰنِ لِبُيُوتِهِمْ سُقُفًۭا مِّن فِضَّةٍۢ وَمَعَارِجَ عَلَيْهَا يَظْهَرُونَ
- 43:34 وَلِبُيُوتِهِمْ أَبْوَٰبًۭا وَسُرُرًا عَلَيْهَا يَتَّكِـُٔونَ
- 43:35 وَزُخْرُفًۭا ۚ وَإِن كُلُّ ذَٰلِكَ لَمَّا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَٱلْءَاخِرَةُ عِندَ رَبِّكَ لِلْمُتَّقِينَ
- 43:36 وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- 43:37 وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
- 43:38 حَتَّىٰٓ إِذَا جَآءَنَا قَالَ يَٰلَيْتَ بَيْنِى وَبَيْنَكَ بُعْدَ ٱلْمَشْرِقَيْنِ فَبِئْسَ ٱلْقَرِينُ
- 43:39 وَلَن يَنفَعَكُمُ ٱلْيَوْمَ إِذ ظَّلَمْتُمْ أَنَّكُمْ فِى ٱلْعَذَابِ مُشْتَرِكُونَ
- 43:40 أَفَأَنتَ تُسْمِعُ ٱلصُّمَّ أَوْ تَهْدِى ٱلْعُمْىَ وَمَن كَانَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- 43:41 فَإِمَّا نَذْهَبَنَّ بِكَ فَإِنَّا مِنْهُم مُّنتَقِمُونَ
- 43:42 أَوْ نُرِيَنَّكَ ٱلَّذِى وَعَدْنَٰهُمْ فَإِنَّا عَلَيْهِم مُّقْتَدِرُونَ
- 43:43 فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ ۖ إِنَّكَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 43:44 وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ
- 43:45 وَسْـَٔلْ مَنْ أَرْسَلْنَا مِن قَبْلِكَ مِن رُّسُلِنَآ أَجَعَلْنَا مِن دُونِ ٱلرَّحْمَٰنِ ءَالِهَةًۭ يُعْبَدُونَ
- 43:46 وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَقَالَ إِنِّى رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- 43:47 فَلَمَّا جَآءَهُم بِـَٔايَٰتِنَآ إِذَا هُم مِّنْهَا يَضْحَكُونَ
- 43:48 وَمَا نُرِيهِم مِّنْ ءَايَةٍ إِلَّا هِىَ أَكْبَرُ مِنْ أُخْتِهَا ۖ وَأَخَذْنَٰهُم بِٱلْعَذَابِ لَعَلَّهُمْ يَرْجِعُونَ
- 43:49 وَقَالُوا۟ يَٰٓأَيُّهَ ٱلسَّاحِرُ ٱدْعُ لَنَا رَبَّكَ بِمَا عَهِدَ عِندَكَ إِنَّنَا لَمُهْتَدُونَ
- 43:50 فَلَمَّا كَشَفْنَا عَنْهُمُ ٱلْعَذَابَ إِذَا هُمْ يَنكُثُونَ
- 43:51 وَنَادَىٰ فِرْعَوْنُ فِى قَوْمِهِۦ قَالَ يَٰقَوْمِ أَلَيْسَ لِى مُلْكُ مِصْرَ وَهَٰذِهِ ٱلْأَنْهَٰرُ تَجْرِى مِن تَحْتِىٓ ۖ أَفَلَا تُبْصِرُونَ
- 43:52 أَمْ أَنَا۠ خَيْرٌۭ مِّنْ هَٰذَا ٱلَّذِى هُوَ مَهِينٌۭ وَلَا يَكَادُ يُبِينُ
- 43:53 فَلَوْلَآ أُلْقِىَ عَلَيْهِ أَسْوِرَةٌۭ مِّن ذَهَبٍ أَوْ جَآءَ مَعَهُ ٱلْمَلَٰٓئِكَةُ مُقْتَرِنِينَ
- 43:54 فَٱسْتَخَفَّ قَوْمَهُۥ فَأَطَاعُوهُ ۚ إِنَّهُمْ كَانُوا۟ قَوْمًۭا فَٰسِقِينَ
- 43:55 فَلَمَّآ ءَاسَفُونَا ٱنتَقَمْنَا مِنْهُمْ فَأَغْرَقْنَٰهُمْ أَجْمَعِينَ
- 43:56 فَجَعَلْنَٰهُمْ سَلَفًۭا وَمَثَلًۭا لِّلْءَاخِرِينَ
- 43:57 ۞ وَلَمَّا ضُرِبَ ٱبْنُ مَرْيَمَ مَثَلًا إِذَا قَوْمُكَ مِنْهُ يَصِدُّونَ
- 43:58 وَقَالُوٓا۟ ءَأَٰلِهَتُنَا خَيْرٌ أَمْ هُوَ ۚ مَا ضَرَبُوهُ لَكَ إِلَّا جَدَلًۢا ۚ بَلْ هُمْ قَوْمٌ خَصِمُونَ
- 43:59 إِنْ هُوَ إِلَّا عَبْدٌ أَنْعَمْنَا عَلَيْهِ وَجَعَلْنَٰهُ مَثَلًۭا لِّبَنِىٓ إِسْرَٰٓءِيلَ
- 43:60 وَلَوْ نَشَآءُ لَجَعَلْنَا مِنكُم مَّلَٰٓئِكَةًۭ فِى ٱلْأَرْضِ يَخْلُفُونَ
- 43:61 وَإِنَّهُۥ لَعِلْمٌۭ لِّلسَّاعَةِ فَلَا تَمْتَرُنَّ بِهَا وَٱتَّبِعُونِ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 43:62 وَلَا يَصُدَّنَّكُمُ ٱلشَّيْطَٰنُ ۖ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
- 43:63 وَلَمَّا جَآءَ عِيسَىٰ بِٱلْبَيِّنَٰتِ قَالَ قَدْ جِئْتُكُم بِٱلْحِكْمَةِ وَلِأُبَيِّنَ لَكُم بَعْضَ ٱلَّذِى تَخْتَلِفُونَ فِيهِ ۖ فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ
- 43:64 إِنَّ ٱللَّهَ هُوَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 43:65 فَٱخْتَلَفَ ٱلْأَحْزَابُ مِنۢ بَيْنِهِمْ ۖ فَوَيْلٌۭ لِّلَّذِينَ ظَلَمُوا۟ مِنْ عَذَابِ يَوْمٍ أَلِيمٍ
- 43:66 هَلْ يَنظُرُونَ إِلَّا ٱلسَّاعَةَ أَن تَأْتِيَهُم بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ
- 43:67 ٱلْأَخِلَّآءُ يَوْمَئِذٍۭ بَعْضُهُمْ لِبَعْضٍ عَدُوٌّ إِلَّا ٱلْمُتَّقِينَ
- 43:68 يَٰعِبَادِ لَا خَوْفٌ عَلَيْكُمُ ٱلْيَوْمَ وَلَآ أَنتُمْ تَحْزَنُونَ
- 43:69 ٱلَّذِينَ ءَامَنُوا۟ بِـَٔايَٰتِنَا وَكَانُوا۟ مُسْلِمِينَ
- 43:70 ٱدْخُلُوا۟ ٱلْجَنَّةَ أَنتُمْ وَأَزْوَٰجُكُمْ تُحْبَرُونَ
- 43:71 يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- 43:72 وَتِلْكَ ٱلْجَنَّةُ ٱلَّتِىٓ أُورِثْتُمُوهَا بِمَا كُنتُمْ تَعْمَلُونَ
- 43:73 لَكُمْ فِيهَا فَٰكِهَةٌۭ كَثِيرَةٌۭ مِّنْهَا تَأْكُلُونَ
- 43:74 إِنَّ ٱلْمُجْرِمِينَ فِى عَذَابِ جَهَنَّمَ خَٰلِدُونَ
- 43:75 لَا يُفَتَّرُ عَنْهُمْ وَهُمْ فِيهِ مُبْلِسُونَ
- 43:76 وَمَا ظَلَمْنَٰهُمْ وَلَٰكِن كَانُوا۟ هُمُ ٱلظَّٰلِمِينَ
- 43:77 وَنَادَوْا۟ يَٰمَٰلِكُ لِيَقْضِ عَلَيْنَا رَبُّكَ ۖ قَالَ إِنَّكُم مَّٰكِثُونَ
- 43:78 لَقَدْ جِئْنَٰكُم بِٱلْحَقِّ وَلَٰكِنَّ أَكْثَرَكُمْ لِلْحَقِّ كَٰرِهُونَ
- 43:79 أَمْ أَبْرَمُوٓا۟ أَمْرًۭا فَإِنَّا مُبْرِمُونَ
- 43:80 أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ
- 43:81 قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ
- 43:82 سُبْحَٰنَ رَبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبِّ ٱلْعَرْشِ عَمَّا يَصِفُونَ
- 43:83 فَذَرْهُمْ يَخُوضُوا۟ وَيَلْعَبُوا۟ حَتَّىٰ يُلَٰقُوا۟ يَوْمَهُمُ ٱلَّذِى يُوعَدُونَ
- 43:84 وَهُوَ ٱلَّذِى فِى ٱلسَّمَآءِ إِلَٰهٌۭ وَفِى ٱلْأَرْضِ إِلَٰهٌۭ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْعَلِيمُ
- 43:85 وَتَبَارَكَ ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا وَعِندَهُۥ عِلْمُ ٱلسَّاعَةِ وَإِلَيْهِ تُرْجَعُونَ
- 43:86 وَلَا يَمْلِكُ ٱلَّذِينَ يَدْعُونَ مِن دُونِهِ ٱلشَّفَٰعَةَ إِلَّا مَن شَهِدَ بِٱلْحَقِّ وَهُمْ يَعْلَمُونَ
- 43:87 وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَهُمْ لَيَقُولُنَّ ٱللَّهُ ۖ فَأَنَّىٰ يُؤْفَكُونَ
- 43:88 وَقِيلِهِۦ يَٰرَبِّ إِنَّ هَٰٓؤُلَآءِ قَوْمٌۭ لَّا يُؤْمِنُونَ
- 43:89 فَٱصْفَحْ عَنْهُمْ وَقُلْ سَلَٰمٌۭ ۚ فَسَوْفَ يَعْلَمُونَ


===== _commentary/v16/work/s043/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ت ب (root_001283): 43:2 وَٱلْكِتَٰبِ, 43:4 ٱلْكِتَٰبِ, 43:19 سَتُكْتَبُ, 43:21 كِتَٰبًا, 43:80 يَكْتُبُونَ

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

## ب ي ن (root_000170): 43:2 ٱلْمُبِينِ, 43:15 مُّبِينٌ, 43:18 مُبِينٍ, 43:29 مُّبِينٌ, 43:32 بَيْنَهُم, 43:38 بَيْنِى, 43:38 وَبَيْنَكَ, 43:40 مُّبِينٍ, 43:52 يُبِينُ, 43:62 مُّبِينٌ, 43:63 بِٱلْبَيِّنَٰتِ, 43:63 وَلِأُبَيِّنَ, 43:65 بَيْنِهِمْ, 43:85 بَيْنَهُمَا

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

## ج ع ل (root_000248): 43:3 جَعَلْنَٰهُ, 43:10 جَعَلَ, 43:10 وَجَعَلَ, 43:12 وَجَعَلَ, 43:15 وَجَعَلُوا۟, 43:19 وَجَعَلُوا۟, 43:28 وَجَعَلَهَا, 43:33 لَّجَعَلْنَا, 43:45 أَجَعَلْنَا, 43:56 فَجَعَلْنَٰهُمْ, 43:59 وَجَعَلْنَٰهُ, 43:60 لَجَعَلْنَا

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

## ق ر ء (root_001210): 43:3 قُرْءَٰنًا, 43:31 ٱلْقُرْءَانُ

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

## ق ر ء (root_001211): 43:3 قُرْءَٰنًا, 43:31 ٱلْقُرْءَانُ

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

## ع ر ب (root_000996): 43:3 عَرَبِيًّا

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

## ع ق ل (root_001036): 43:3 تَعْقِلُونَ

- **B001** bilgiyi edinip kavrama, ayırt etme ve davranışı denetleme yetisi — kavrama, ayırt etme ve bilgi edinme yetisi · bilmediğini kavramak veya yanlış davranıştan geri durmak · anlayışlı ve ayırt etme gücü olan · çok iyi anlayan ve duyduğunu unutmayan · zihinde kavranan şey veya kavrama gücü · anlayışlı görünmeye çalışmak · öyle olmadığı halde anlayışlı görünmek
  العقل نقيض الجهل (maqayis;ayn)؛ عقل يعقل عقلا إذا عرف ما كان يجهله أو انزجر عما كان يفعله (maqayis)؛ العقل الحجر والنهى (sihah)؛ القوة المتهيئة لقبول العلم والعلم الذي يستفيده الإنسان (mufradat)؛ العقل التثبت في الأمور والقلب (tahdhib)
- **B002** devenin ön ayağını büküp bağlayarak tutma — devenin ön ayağını büküp bağlamak · devenin ön ayağını bağlayan ip · kadının saçını tarayıp toplaması
  عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط (maqayis)؛ عقلت البعير عقلا شددت يده بالعقال أي الرباط (ayn)؛ عقلت البعير أعقله عقلا وهو أن تثني وظيفه مع ذراعه (sihah)؛ أصل العقل مصدر عقلت البعير بالعقال والعقال حبل (tahdhib)؛ كعقل البعير بالعقال (mufradat)؛ عقلت المرأة شعرها (sihah;tahdhib;mufradat)
- **B003** dilin tutulup konuşamaz hâle gelmesi — dili tutulup konuşamaz hâle gelmek · dilini tutup konuşmasını engellemek
  اعتقل لسان فلان إذا احتبس عن الكلام (maqayis)؛ اعتقل لسانه إذا لم يقدر على الكلام (sihah;tahdhib)؛ عقل لسانه كفه (mufradat)
- **B004** öldürme veya yaralama karşılığı ödeme ve bu yükü paylaşma düzeni — öldürme veya yaralama için ödenen karşılık · öldürülen kişinin karşılığını ödemek · birinin yaralama yükünü üstlenip karşılığını ödemek · yanlışlıkla öldürmede ödemeyi üstlenen baba yanından yakınlar · bir topluluğun üstüne düşen öldürme karşılığı payı · yaralama karşılıklarında belirli sınıra kadar denk olmak
  العقل وهي الدية (maqayis;sihah;tahdhib)؛ عقلت القتيل أعطيته ديته (maqayis;ayn;sihah;tahdhib;mufradat)؛ العاقلة القوم تقسم عليهم الدية (maqayis)؛ العاقلة هم العصبة (tahdhib)؛ دية معقلة على قومه (mufradat)
- **B005** yıllık hayvan vergisi ve bunun tahsili — bir yıllık hayvan vergisi veya onunla birlikte verilen pay · iki yıllık hayvan vergisi · vergi görevlisinin zorunlu payı teslim alması
  العقال صدقة عام من الإبل (ayn)؛ الصدقة كلها عقال (maqayis)؛ العقال صدقة عام (sihah;tahdhib;mufradat)؛ على بني فلان عقالان أي صدقة سنتين (sihah)؛ أعطى معها عقلها وأرويتها (maqayis)
- **B006** ishali yiyecek veya ilaçla durdurma — yiyecek veya ilacın ishali durdurması · ishal kesici ilaç
  عقل الطعام بطنه إذا أمسكه (maqayis)؛ العقول من الدواء ما يمسك البطن (maqayis;sihah)؛ عقل بطن المريض بعدما استطلق استمسك (ayn)؛ عقل الدواء بطنه أي أمسكه (sihah;tahdhib;mufradat)
- **B007** korunaklı sığınak ve oraya çekilerek korunma — sığınak ve sağlam korunaklı yer · korunmak için sığınılan yer · geyik veya dağ keçisinin yüksek dağa sığınıp korunması
  المعقل والعقل وهو الحصن (maqayis)؛ العقل الحصن وجمعه العقول وهو المعقل أيضا (ayn)؛ العقل الملجأ والمعقل الملجأ (sihah)؛ المعقل وهو الملجأ (tahdhib;mufradat)؛ عقل الظبي إذا امتنع في الجبل (maqayis;tahdhib)؛ عقل الوعل أي امتنع في الجبل العالي (sihah)
- **B008** bir topluluğun veya türün en seçkin ve değerli örneği — seçkin ve değerli kadın, kişi veya hayvan · her şeyin en değerli ve seçkin olanı · denizin değerli incisi
  فلانة عقيلة قومها فهي كريمتهم وخيارهم (maqayis)؛ العقيلة المرأة المخدرة المحبوسة في بيتها (ayn)؛ عقيلة كل شيء أكرمه (maqayis;ayn;sihah;tahdhib)؛ الدرة عقيلة البحر (maqayis;ayn;sihah;tahdhib)؛ العقيلة من النساء والدر وغيرهما التي تعقل أي تحرس وتمنع (mufradat)
- **B009** diz çarpışmasına yol açan bacak eğriliği veya hayvanlarda bacak hastalığı — dizlerin çarpışması veya bacak eğriliği · bacağı eğri ve dışa açık deve · hayvanın bacaklarını tutan hastalık veya topallık
  العقل في الرجلين اصطكاك الركبتين (maqayis)؛ العقل في الرجل اصطكاك الركبتين وقيل إلتواء في الرجل (ayn)؛ بعير أعقل وناقة عقلاء بين العقل وهو إلتواء في رجل البعير (ayn;sihah;tahdhib)؛ العقال داء يأخذ الدواب في الرجلين (maqayis;ayn)؛ العقال ظلع يأخذ في قوائم الدابة (sihah;tahdhib)
- **B010** bir şeyi bükülmüş bacaklar arasında sıkıştırıp tutma — mızrağı üzengi ile baldır arasına sıkıştırmak · koyunun ayağını sağmak için bacaklar arasında tutmak · güreşte rakibin bacaklarını kilitleme tekniği · rakibin bacağına bacağını dolayarak onu düşürmek
  اعتقل رمحه إذا وضعه بين ركابه وساقه (maqayis;sihah;tahdhib;mufradat)؛ اعتقل شاته إذا وضع رجلها بين فخذه وساقه فحلبها (maqayis;sihah;tahdhib)؛ لفلان عقلة يعتقل بها الناس إذا صارعهم عقل أرجلهم (maqayis;sihah;tahdhib)؛ اعتقل الرحل إذا ثنى رجله فوضعها على المورك (tahdhib)
- **B011** eğrilip kıvrılan bölüm veya iç içe yığılmış kum tepesi — nehir, vadi veya kumun eğri ve kıvrımlı bölümü · işlerin dolaşık ve çözülmesi güç yanları · iç içe geçmiş büyük kum tepesi
  العاقول من النهر والوادي ومن الأمور أيضا ما التبس واعوج (maqayis)؛ العاقول من النهر والوادي والرمل المعوج منه وعواقيل الأمور ما التبس منها (sihah)؛ العقنقل من الرمل وهو ما أرتكم منه (maqayis)؛ كل ما تحوى والتوى فهو عقنقل (maqayis)؛ العقنقل الكثيب العظيم المتداخل الرمل (sihah)
- **B012** gün ortasında gölgenin kısalıp sabit görünmesi — gölgenin gün ortasında kısalıp sabit görünmesi · topluluğun gölgenin kısaldığı öğle vaktine girmesi
  عقل الظل أي قام قائم الظهيرة (sihah)؛ أعقل القوم إذا عقل بهم الظل أي لجأ وقلص عند انتصاف النهار (sihah)؛ عقل الظل إذا قام قائم الظهيرة (tahdhib)
- **B013** kırmızı veya desenli dokuma giysi türü — kırmızı giysi veya desenli dokuma türü
  العقل ثوب تتخذه نساء الأعراب (ayn)؛ العقل ثوب أحمر (sihah)؛ يقال هما ضربان من البرود (ayn;sihah)؛ العقل ضرب من الوشي (tahdhib)
- **B014** büyünün bağlayıcı etkisi ve bunu çözme uygulaması — büyünün bağlayıcı etkisi
  به عقلة من السحر وقد عملت له نشرة (sihah)

## ء م م (root_000053): 43:4 أُمِّ, 43:22 أُمَّةٍ, 43:23 أُمَّةٍ, 43:33 أُمَّةً

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

## ع ل و (root_001042): 43:4 لَعَلِىٌّ

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

## ح ك م (root_000348): 43:4 حَكِيمٌ, 43:63 بِٱلْحِكْمَةِ, 43:84 ٱلْحَكِيمُ

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

## ض ر ب (root_000906): 43:5 أَفَنَضْرِبُ, 43:17 ضَرَبَ, 43:57 ضُرِبَ, 43:58 ضَرَبُوهُ

- **B001** bir şeyi başka bir şeyin üzerine vurmak — bir şeyi el, sopa, kılıç veya benzeri bir araçla vurmak
  ضربت ضربا إذا أوقعت بغيرك ضربا (maqayis)؛ الضرب مصدر ضربته ضربا (jamhara;sihah;tahdhib)؛ الضرب إيقاع شيء على شيء (mufradat)
- **B002** bir amaçla yeryüzünde yolculuk etmek [kalıp] — geçim, alışveriş, savaş veya dinsel bir amaçla yeryüzünde yolculuk etmek
  ضرب في الأرض تجارة وغيرها من السفر (maqayis)؛ ضرب في التجارة وفي الأرض وفي سبيل الله (ayn;tahdhib)؛ خرج فيها تاجرا أو غازيا (jamhara)؛ سار في ابتغاء الرزق (sihah)؛ الضرب في الأرض الذهاب فيها وضربها بالأرجل (mufradat)
- **B003** örnek vererek açıklamak [kalıp] — bir şeyi açıklamak için örnek vermek
  ضرب الله مثلا أي وصف وبين (sihah)؛ اضرب لهم مثلا أي اذكر لهم مثلا ومثل لهم مثلا (tahdhib)؛ ضرب المثل ذكر شيء أثره يظهر في غيره (mufradat)
- **B004** bir işten geri durup yüz çevirmek [kalıp] — bir işten geri durmak ve ondan yüz çevirmek · evinde kalmak
  أضرب عن الأمر إذا كف (maqayis;ayn;tahdhib)؛ أضرب عنه أي أعرض (sihah)؛ أضرب الرجل عن الأمر إضرابا (jamhara)؛ أفنضرب عنكم الذكر صفحا (mufradat)؛ أضرب فلان في بيته أي أقام (maqayis;ayn;sihah;tahdhib)
- **B005** birinin giriştiği işi engellemek [kalıp] — birini giriştiği işten alıkoymak
  ضرب فلان على يد فلان إذا حجر عليه (maqayis;sihah;tahdhib)؛ ضرب يده إلى كذا وضرب على يد فلان حبس عليه أمرا (ayn)
- **B006** biçime bağlı adlandırmalar [kalıp] — duymaz ve uyanmaz biçimde uyutmak · aşağılanmışlıkla çepeçevre kuşatılmak
  ضرب الخيمة بضرب أوتادها وتشبيها بالخيمة ضربت عليهم الذلة (mufradat)؛ فضربنا على آذانهم معناه أنمناهم (tahdhib)؛ فضرب بينهم بسور (mufradat)؛ فاضرب لهم طريقا في البحر (mufradat)
- **B007** tür ya da biçim kalıbı — tür, sınıf veya biçim kalıbı
  الضرب الصيغة وهذا من ضرب فلان أي صيغته (maqayis)؛ الضرب النحو والصنف (ayn)؛ هذا ضرب من المتاع أي نوع منه (jamhara)؛ الضرب الصيغة والصنف من الأشياء (sihah)؛ الضرب الصنف من الأشياء وعندي من هذا الضرب (tahdhib)
- **B008** benzer ve denk karşılık — benzeri, dengi veya karşılığı
  الضريب المثل (maqayis)؛ ضريب ذاك أي مثله (ayn)؛ فلان ضريب فلان إذا كان شبيها به (jamhara)؛ ضريب الشيء مثله وشكله (sihah)؛ فلان ضريب فلان أي نظيره (tahdhib)
- **B009** yerleşik yaradılış ve huy — yaradılış, huy ve yerleşik kişilik özellikleri
  السجية والطبيعة الضريبة كأن الإنسان قد ضرب عليها (maqayis)؛ الضريبة الطبيعة (ayn;jamhara)؛ كريم الضريبة ولئيم الضريبة (sihah)؛ الضريبة الخليقة (tahdhib)؛ بذلك شبه السجية وقيل لها الضريبة والطبيعة (mufradat)
- **B010** kişiye ya da toprağa yüklenen mali ödeme — kişiye, çalışana veya toprağa yüklenen vergi ya da düzenli mali pay
  الضريبة ما يضرب على الإنسان من جزية وغيرها (maqayis)؛ الضريبة غلة تضرب على العبد (ayn;tahdhib)؛ وظيفة أو إتاوة يأخذها الملك (jamhara)؛ الضرائب التي تؤخذ في الأرصاد والجزية (sihah)؛ ضرائب الأرضين في وظائف الخراج (tahdhib)
- **B011** erkek devenin dişiyle çiftleşmesi [kalıp] — erkek devenin dişi deveyle çiftleşmesi
  ضراب الفحل الناقة وأضربت الناقة (maqayis)؛ الفحل من الإبل يضرب الشول ضرابا (ayn)؛ ضرب الفحل الناقة ضرابا وأضربته (jamhara)؛ ضرب الفحل الناقة ضرابا (sihah;tahdhib)؛ ضرب الفحل الناقة واستضراب الناقة (mufradat)
- **B012** düzensiz ve yinelenen hareket — düzensiz hareket, sallanma veya karışıklık · damarın ağrıyla atması
  الاضطراب تضرب الولد في البطن واضطرب الحبل بين القوم (ayn;tahdhib)؛ ضرب العرق ضربانا (jamhara;tahdhib)؛ ضرب الجرح ضربانا والموج يضطرب واضطرب أمره (sihah)؛ ضرب البعير في جهازه أي نفر (sihah;tahdhib)؛ الاضطراب كثرة الذهاب في الجهات (mufradat)
- **B013** hava olayının toprağa veya bitkiye etkisi — toprağı ve bitkiyi etkileyen kırağı veya buz · hafif ya da yumuşak yağmur
  الضريب الصقيع كأن السماء ضربت به الأرض (maqayis)؛ أضرب الريح والبرد النبات وأضربت السمائم الماء (ayn)؛ الضريب الجليد والضرب المطر اللين (jamhara)؛ الضريب الصقيع وضربت الأرض (sihah)؛ أضربها الضريب وأرض ضربة (tahdhib)؛ ضرب الأرض بالمطر (mufradat)
- **B014** vurma aracı, bölgesi, yeri veya işi — kılıcın darbeyi indiren uç bölümü
  مضرب السيف المكان الذي يضرب به منه (maqayis)؛ الضريبة مضرب السيف والصوف يضرب بالمطرق (ayn)؛ مضرب السيف والمضرب المكان والفسطاط (jamhara)؛ المضراب الذي يضرب به العود وضرب النجاد المضربة (sihah)؛ المضرب فسطاط الملك والضريبة الصوف يضرب بالمطرق (tahdhib)؛ ضرب الخيمة بضرب أوتادها وضرب العود والناي والبوق (mufradat)
- **B015** yoğun bal veya karışıp koyulaşmış süt — beyaz, koyu veya katı bal · farklı sağımların karıştığı veya koyulaşmış süt
  الضريب من اللبن ما خلط محضه بحقينه والضرب العسل الغليظة (maqayis)؛ الضرب العسل الخالص والضريب من اللبن والضريب الشهد (ayn)؛ الضريب اللبن الخاثر والضرب العسل الصلب (jamhara)؛ الضرب العسل الأبيض الغليظ وضريب الشول لبن يحلب بعضه على بعض (sihah)؛ الضرب العسل الأبيض الغليظ والضريب من عدة من الإبل (tahdhib)
- **B016** para-emek ortaklığı — bir tarafın para, ötekinin emek koyduğu ve kazancı paylaştığı ticaret ortaklığı
  ضارب فلان لفلان في ماله إذا تجر فيه (jamhara)؛ ضاربه في المال من المضاربة وهي القراض (sihah)؛ المضاربة أن تعطي إنسانا من مالك ما يتجر فيه والربح بينكما (tahdhib)؛ المضاربة ضرب من الشركة (mufradat)
- **B017** çatışmaya kışkırtmak — insanları birbirine karşı veya savaşmaya kışkırtmak
  التضريب بين القوم الإغراء (sihah)؛ التضريب تحريض الشجاع في الحرب (tahdhib)؛ التضريب التحريض كأنه حث على الضرب (mufradat)
- **B018** özel adlandırma kümesi — hafif yapılı veya az etli erkek · oklardan sorumlu görevli · soyda veya malda dayanak oluşturan kök
  الرجل الخفيف الجسم ضرب (maqayis)؛ رجل مضرب شديد الضرب (maqayis;ayn;sihah)؛ الضارب السابح (sihah;tahdhib)؛ الضارب الوادي الكثير الشجر (ayn;sihah;tahdhib)؛ الضارب قطعة من الأرض غليظة تستطيل (jamhara)؛ الضارب الطويل من كل شيء (tahdhib)؛ ضريب القداح هو الموكل بها (maqayis;ayn;sihah;tahdhib)؛ مضرب عسلة من النسب والمال (sihah;tahdhib)

## ذ ك ر (root_000516): 43:5 ٱلذِّكْرَ, 43:13 تَذْكُرُوا۟, 43:36 ذِكْرِ, 43:44 لَذِكْرٌ

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

## ص ف ح (root_000867): 43:5 صَفْحًا, 43:89 فَٱصْفَحْ

- **B001** enine yüz, geniş yassı parça ve enli kılma — en, yan veya yan yüz · insanın ya da hayvanın böğrünün enli yanı · yüzün yanı · kılıcın yassı yüzü · kılıcın enli yüzü · dağın yamacı veya yanı · dağın yamacı veya yanı · enli yassı parça, geniş taş veya geniş kılıç · geniş yassı parçalar veya levhalar · geniş ve yassı taşlar · yüz derisi · geniş veya hafifçe uzamış baş · geniş göğüs · bir şeyi enli duruma getirme · hörgüçleri enine geniş develer
  الصفح الجنب من كل شيء وصفحتا السيف وجهاه وكل حجر عريض أو خشبة أو لوح أو حديدة أو سيف له طول وعرض فهو صفيحة (ayn)؛ صفحة الإنسان والدابة عرض جنبه والصفيحة النصل العريض من السيوف والقطعة من الصخر العريضة ورأس مصفح (jamhara)؛ صفحة كل شيء جانبه وصفح الجبل مضطجعه وصفائح الباب ألواحه وتصفيح الشيء جعله عريضا (sihah)؛ صفح الشيء عرضه وجانبه كصفحة الوجه وصفحة السيف وصفحة الحجر (mufradat)؛ صفح الشيء عرضه والصفيحة كل سيف عريض وكل حجر عريض صفيحة (maqayis)؛ سفح الجبل من باب الإبدال والأصل فيه صفح (maqayis)
- **B002** başa kakmadan bağışlayıp yüz çevirme — başa kakmadan bağışlama · kusurunu bağışlayıp ondan yüz çevirmek · ondan yüz çevirip onu bırakmak · bir şeyi bırakıp ondan yüz çevirmek · başa kakmadan güzelce bağışlama
  صفحت عنه أي عفوت عنه (ayn)؛ صفحت عن الرجل إذا عفوت عن جرمه وأضربت عن هذا الأمر صفحا إذا تركته (jamhara)؛ صفحت عن فلان إذا أعرضت عن ذنبه وقد ضربت عنه صفحا إذا أعرضت عنه وتركته (sihah)؛ الصفح ترك التثريب وهو أبلغ من العفو (mufradat)؛ صفح عنه وذلك إعراضه عن ذنبه (maqayis)
- **B003** sayfa sayfa veya kişi kişi gözden geçirme — yazılı yaprakları çevirmek · topluluğu kişi kişi gözden geçirmek · sayfalarına veya aralarına bakarak incelemek
  صفحت ورق المصحف صفحا وصفحت القوم عرضتهم واحدا واحدا وتصفحتهم نظرت في خلالهم (ayn)؛ تصفحت الشيء إذا نظرت في صفحاته (sihah)؛ تصفحت الكتاب (mufradat)
- **B004** el sıkışma — el sıkışma · iki kişinin avuçlarını birbirine değdirerek el sıkışması
  المصافحة معروفة (ayn)؛ تصافح الرجلان بكفيهما إذا ألصق كل واحد منهما كفه بكف صاحبه (jamhara)؛ المصافحة الأخذ باليد والتصافح مثله (sihah)؛ المصافحة الإفضاء بصفحة اليد (mufradat)؛ المصافحة باليد كأنه ألصق يده بصفحة يد ذاك (maqayis)
- **B005** çekişmede kendini karşısındakine açık etmek [kalıp] — çekişmede kendini karşısındakine açık etmek
  أبدى فلان لي صفحته إذا أمكنك من نفسه في خصومة أو حرد
- **B006** bir yöne eğilmiş veya çevrilmiş olma — bir yöne eğilmiş veya çevrilmiş · gerçekten yüz çevirmiş iç yöneliş · gerçeğe yönelmiş veya ona bağlı iç yöneliş
  المصفح الممال وقلب المنافق مصفح أي ممال عن الحق (jamhara)؛ المصفح أيضا الممال وقلب المؤمن مصفح على الحق (sihah)
- **B007** kılıcın yassı yüzüyle vurma [kalıp] — kılıcın yassı yüzüyle vurmak · kılıcın keskin ağzıyla değil yassı yüzüyle vurmak
  ضربته بالسيف مصفحا ومصفوحا إذا ضربته بعرضه ولم تضربه بحده (jamhara)؛ ضربه بصفح السيف أي بعرضه وصفحته وأصفحته إذا ضربته بالسيف مصفحا أي بعرضه (sihah)
- **B008** el çırpma — el çırpma
  التصفيح التصفيق باليدين (jamhara)؛ التصفيح مثل التصفيق (sihah)
- **B009** istekte bulunanı geri çevirip vermemek [kalıp] — istekte bulunanı geri çevirip istediğini vermemek
  صفحت فلانا وأصفحته إذا سألك فرددته (sihah)؛ صفحت الرجل وأصفحته إذا سألك فمنعته وهو من أنك أريته صفحتك معرضا عنه (maqayis)
- **B010** develeri suluk boyunca geçirmek [kalıp] — develeri suluk boyunca geçirmek
  صفحت الإبل على الحوض إذا أمررتها (sihah)؛ صفحت الإبل على الحوض إذا أمررتها عليه وكأنك أريت الحوض صفحاتها وهي جنوبها (maqayis)
- **B011** talih oyunundaki altıncı ok — talih oyunundaki altıncı ok; başka bir adla da anılır
  المصفح أيضا السادس من سهام الميسر ويقال له المسبل أيضا
- **B012** bir erkeğe herhangi bir içecek verme [kalıp] — bir erkeğe herhangi bir içecek vermek
  مما شذ عن الباب قولهم صفحت الرجل صفحا إذا سقيته أي شراب كان

## ك و ن (root_001332): 43:5 كُنتُمْ, 43:7 كَانُوا۟, 43:13 كُنَّا, 43:25 كَانَ, 43:33 يَكُونَ, 43:40 كَانَ, 43:54 كَانُوا۟, 43:69 وَكَانُوا۟, 43:72 كُنتُمْ, 43:76 كَانُوا۟, 43:81 كَانَ

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

## ق و م (root_001273): 43:5 قَوْمًا, 43:26 وَقَوْمِهِۦٓ, 43:43 مُّسْتَقِيمٍ, 43:44 وَلِقَوْمِكَ, 43:51 قَوْمِهِۦ, 43:51 يَٰقَوْمِ, 43:54 قَوْمَهُۥ, 43:54 قَوْمًا, 43:57 قَوْمُكَ, 43:58 قَوْمٌ, 43:61 مُّسْتَقِيمٌ, 43:64 مُّسْتَقِيمٌ, 43:88 قَوْمٌ

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

## س ر ف (root_000699): 43:5 مُّسْرِفِينَ

- **B001** sınırı ve uygun ölçüyü aşma — sınırı veya uygun ölçüyü aşma · ölçüsüzlük ve savurganlık · sınırı aştı · işinde sınırı aşan kimse · öldürmede sınırı aşma; fail dışındaki birini öldürme · harcamada savurganlık; parayı uygun olmayan yere harcama · sulama veya başka bir yarar sağlamadan akıp giden su · yemede ölçüyü aşma veya yenmemesi gereken şeyi yeme
  تعدي الحد (maqayis); مجاوزة القدر (maqayis); الإسراف نقيض الاقتصاد (ayn); السرف ضد القصد (sihah;tahdhib); الإسراف في النفقة التبذير (sihah); تجاوز ما حد لك (tahdhib); سرف الماء ما ذهب منه في غير سقي ولا نفع (tahdhib); مجاوزة القصد في الأكل (tahdhib); تجاوز الحد في كل فعل (mufradat); فلا يسرف في القتل (tahdhib;mufradat)
- **B002** yanılma, gözden kaçırma veya bilememe — yanılma, gözden kaçırma ve bilmeme · bilgisiz kimse · şeyi yanlış yaptı, gözden kaçırdı veya bilemedi · sizi ıskaladım, fark etmedim veya tanımadım · yüreği yanılan ve dalgın kimse · sağ eli belirsiz kaldı ve tanınmadı · yanıldı veya fark etmedi
  الإغفال (maqayis;tahdhib); السرف الجهل (maqayis;ayn;tahdhib); السرف الخطأ (ayn;sihah;tahdhib); مررت بكم فسرفتكم (maqayis;ayn;sihah;mufradat); سرفت الشيء أي أخطأته وأغفلته (tahdhib); إخطاء الشيء وضعه في غير موضعه (tahdhib); سرفت يمينه أي لم أعرفها (tahdhib)
- **B003** ete alışkanlık derecesinde düşkünlük [kalıp] — ete güçlü bir alışkanlık geliştirme ve onu sık sık satın alma
  إن للحم سرفا كسرف الخمر (maqayis;sihah;tahdhib); للحم سرف كسرف الخمر وهو الضراوة (ayn); ضراوة كضراوة الخمر (tahdhib)
- **B004** ağaç delen, yaprak veya odun yiyen küçük böcek — yaprak veya odun yiyen, ağacı delip yuva kuran küçük böcek · ağaç böceğin saldırısına uğradı veya yaprakları yendi · bu böceğin saldırısına uğramış ağaç · yuva yapmada bu böcekten bile daha usta
  السرفة دويبة تأكل الخشب (maqayis); دويبة صغيرة تنقب الشجر وتبني فيه بيتا (ayn); دويبة تتخذ لنفسها بيتا (sihah); أصابته السرفة (ayn;tahdhib); السرف مصدر سرفت الشجرة (tahdhib); السرفة دويبة تأكل الورق (mufradat); سرفت الشجرة فهي مسروفة (sihah;mufradat)

## ر س ل (root_000563): 43:6 أَرْسَلْنَا, 43:23 أَرْسَلْنَا, 43:24 أُرْسِلْتُم, 43:29 وَرَسُولٌ, 43:45 أَرْسَلْنَا, 43:45 رُّسُلِنَآ, 43:46 أَرْسَلْنَا, 43:46 رَسُولُ, 43:80 وَرُسُلُنَا

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

## ن ب ء (root_001464): 43:6 نَّبِىٍّ, 43:7 نَّبِىٍّ

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

## ء و ل (root_000067): 43:6 ٱلْأَوَّلِينَ, 43:8 ٱلْأَوَّلِينَ, 43:81 أَوَّلُ

- **B001** başlangıç ve öncelik — ilk; önde gelen · ilk olan kadın ya da dişil şey · ilkler; öncekiler · topluluğun önünde bulunma · sürünün önünde giden dişi ya da erkek deve · önceki yıl · her şeyden önce
  الأول وهو مبتدأ الشيء؛ ناقة أولة وجمل أول إذا تقدما الإبل (maqayis)؛ أول في اللغة على الحقيقة ابتداء الشيء؛ جاء فلان في أولية الناس إذا جاء في أولهم (tahdhib)
- **B002** sonuca dönme ve varma — geri dönmek; sonunda bir duruma varmak · hükmü sahiplerine geri vermek · bedeni zayıflamak · sözün sonucu veya anlamının açıklanması · açıklamak; anlamına döndürmek · onunla ilgili ödülü gözetmek ve aramak
  آل يؤول أى رجع؛ تأويل الكلام وهو عاقبته وما يؤول إليه (maqayis)؛ التأويل تفسير ما يؤول إليه الشئ؛ آل أي رجع (sihah)؛ آل يؤول أي رجع وعاد؛ التأويل المرجع والمصير (tahdhib)
- **B003** aile ve bağlı çevre — kişinin ailesi, ev halkı ve yakınları · onun izleyicileri ve bağlıları · kişinin sığındığı ev halkı · kişinin kökü ve bağlı olduğu aile
  آل الرجل أهل بيته؛ لأنه إليه مآلهم وإليهم مآله (maqayis)؛ آل الرجل أهله وقرابته (jamhara)؛ آل الرجل أهله وعياله؛ وآله أيضا أتباعه (sihah)؛ إلة الرجل أهل بيته؛ إيلة الرجل فهم أصله الذين يؤول إليهم (tahdhib)
- **B004** iyi yönetip düzene koyma — iyi yönetme ve gözetme · yöneticinin halkını iyi yönetip gözetmesi · malını düzeltip iyi yönetmek · düzeltme ve iyi yönetme · Tanrı işini toparlayıp düzeltsin
  الإيالة السياسة؛ آل الرجل رعيته يؤولها إذا أحسن سياستها (maqayis)؛ الايالة السياسة؛ آل الأمير رعيته يؤولها أولا وإيالا؛ آل ما له أي أصلحه وساسه (sihah)؛ ألت الشيء جمعته وأصلحته؛ أول الله عليك أمرك أي جمعه (tahdhib)
- **B005** koyulaşıp pıhtılaşma — sütün koyulaşıp pıhtılaşması · katranın veya balın koyulaşıp katılaşması · pıhtılaşmış süt
  آل اللبن أي خثر؛ لا يخثر إلا آخر أمره؛ آل القطران إذا خثر (maqayis)؛ آل القطران أو العسل إذا أعقد بالنار (jamhara)؛ آل القطران والعسل أي خثر؛ الآيل اللبن الخاثر (sihah)
- **B006** görünür siluet ve dış uçlar — görünür siluet; uzaktan beliren görüntü · adamın görünen silueti · dağın uçları ve yanları
  آل الرجل شخصه؛ آل كل شيء؛ آل الجبل أطرافه ونواحيه (maqayis)؛ الآل السراب؛ آل كل شيء شخصه (jamhara)؛ الآل الشخص؛ الآل الذي تراه في أول النهار وآخره كأنه يرفع الشخوص وليس هو السراب (sihah)
- **B007** içinde bulunulan durum — içinde bulunulan durum
  الآلة الحالة (maqayis)؛ والآلة الحالة (jamhara)؛ والآلة الحالة يقال هو بآلة سوء (sihah)
- **B008** araç ve taşıyıcı düzen — araç · çadır direkleri ve taşıyıcı ağaçları · cenaze veya ölüyü taşıyan sedye
  آل الخيمة العمد (maqayis)؛ الآلة الأداة؛ خشبات تبنى عليها الخيمة؛ الآلة الجنازة (sihah)
- **B009** erkek yabani dağ keçisi — erkek yabani dağ keçisi
  الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن (maqayis)؛ الايل أيضا الذكر من الاوعال (sihah)
- **B010** içecek olgunlaştırma kabı — içecek olgunlaştırma kabı
  الإيال على فعال وعاء يجمع فيه الشراب اياما حتى يجود (maqayis)
- **B011** kumda yetişen yem bitkisi — kumda yetişen bir yem bitkisi
  التأويل نبت يعتلفه الحمار؛ التأويل اسم بقلة يولع بها بقر الوحش تنبت في الرمل (tahdhib)

## ECHO و ل ي (root_001684): for 43:6 ٱلْأَوَّلِينَ, 43:8 ٱلْأَوَّلِينَ, 43:81 أَوَّلُ: withheld observed target; not identity

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

## ء ت ي (root_000009): 43:7 يَأْتِيهِم, 43:21 ءَاتَيْنَٰهُمْ, 43:66 تَأْتِيَهُم

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

## ه ز ء (root_001587): 43:7 يَسْتَهْزِءُونَ

- **B001** alay etme; gizli şakayla küçümseme — alay etme; gizli veya şakaya benzer küçümseme · onunla alay etti · onunla alay etmeye yöneldi ya da alay etti · onunla alay etti · alay etme, küçümseyici şaka · alay edilen adam · insanlarla alay eden adam · onu alay ve oyun konusu yaptı · alay etmeye yönelme veya alay etme
  هزىء واستهزأ إذا سخر (maqayis)؛ الهزء السخرية يقال هزيء به واستهزأ به وتهزأ به (ayn)؛ الهزء والهزؤ السخرية ورجل هزءة يهزأ به وهزأة يهزأ بالناس (sihah)؛ الهزء السخرية ورجل هزأة يهزأ بالناس ورجل هزأة يهزأ به (tahdhib)؛ الهزء مزح في خفية وقد يقال لما هو كالمزح (mufradat)
- **B002** alaylarına karşılık ceza verme veya süre verip ansızın yakalama — Tanrı, alaylarına karşılık onları cezalandırır veya süre verip ansızın yakalar
  الله يستهزىء بهم أي يجازيهم على هزئهم بالعذاب فسمي جزاء الذنب باسمه (tahdhib)؛ الاستهزاء من الله في الحقيقة لا يصح وقوله الله يستهزئ بهم أي يجازيهم جزاء الهزؤ (mufradat)؛ أمهلهم مدة ثم أخذهم مغافصة فسمى إمهاله إياهم استهزاء (mufradat)
- **B003** şiddetli soğuğa uğrama veya soğuktan ölme — 
  هزأني البرد أصابني شدته واهتزأت صرت في شدة البرد ويقال إنما هو بالراء (ayn)؛ أهزأه البرد وأهرأه إذا قتله ومثله فيما تعاقب فيه الزاي والراء (tahdhib)
- **B004** binek hayvanını hareket ettirme — binek hayvanını hareket ettirdi
  نزأت الراحلة وهزأتها إذا حركتها (tahdhib)

## ه ل ك (root_001596): 43:8 فَأَهْلَكْنَآ

- **B001** yok olma veya yok etme — yok olmak, bozulmak veya ölmek · yok oluş, kayıp, bozulma veya ölüm · sahibinin elinden çıkıp başka birinde kalmak · yiyecek bozulmak · yok etmek veya mahvetmek · yok etmek · yok olmuş şey veya yok oluş · yatağın üzerine düşmek
  يدل على كسر وسقوط (maqayis)؛ الهلك الهلاك (ayn;tahdhib)؛ هلك الشيء يهلك هلاكا وهلوكا (sihah)؛ الهلاك على أوجه افتقاد الشيء واستحالة وفساد والموت وبطلان الشيء وعدمه (mufradat)؛ يقال للعذاب والخوف والفقر الهلاك (mufradat)
- **B002** kendini ölümcül tehlikeye atma ve buna götüren tehlike — sonu yok oluşa varan tehlike · kendini ölümcül tehlikeye atma · korkudan kendini tehlikeli yere atmak
  الاهتلاك رمي الإنسان نفسه في تهلكة (ayn;tahdhib)؛ التهلكة كل شيء يصير عاقبته إلى الهلاك (ayn;tahdhib)؛ اهتلكت القطاة خوف البازي رمت بنفسها على المهالك (maqayis;sihah)؛ التهلكة ما يؤدي إلى الهلاك (mufradat)
- **B003** salınarak ve kırıtılarak yürüme — yürürken salınmak ve kırıtmak · kırıtarak yürüyen; eski kullanımda ahlaksız diye nitelenen kadın
  امرأة هلوك إذا تهالكت في غنجها متكسرة (maqayis)؛ الهلوك المرأة الفاجرة (ayn;tahdhib)؛ الهلوك من النساء الفاجرة المتساقطة على الرجال (sihah)؛ تهالكت المرأة في مشيتها (tahdhib)؛ كني بالهلوك عن الفاجرة لتمايلها (mufradat)
- **B004** geçinmek için sürekli yardım arayan yoksullar — kendisine bakacak birini sürekli arayan yoksul · iyilik ve yardım arayan yoksullar
  المهتلك الذي يهتلك أبدا إلى من يكفله وناس مهتلكون وهلاك (maqayis)؛ الهلاك الصعاليك الذين ينتابون الناس طلبا لمعروفهم من سوء الحال (ayn;tahdhib)؛ الأرامل والهلاك يعني به الفقراء (sihah)
- **B005** kurak arazi, çetin kıtlık yılı veya yağmursuz dağılan bulut — uzun süredir yağış almamış çorak arazi · üzerinde hiçbir şey yetişmeyen kurak arazi · çetin kıtlık yılı
  الأرض الهلكين الجدبة (maqayis)؛ أرض هلكون إذا لم يكن فيها شيء (tahdhib)؛ تركتها آرمة هلكين إذا لم يصبها الغيث منذ دهر طويل (tahdhib)؛ الهلك السنة الشديدة (tahdhib)؛ هالكة من السحاب المصوب ثم يقلع فلا يكون له مطر (tahdhib)
- **B006** ölümcül ıssız arazi veya dağlar arasındaki uçurum — geçeni ölüme götüren ıssız arazi · geçenleri öldüren tehlikeli ıssız arazi · dağlar arasındaki uçurum veya uçurum kenarı
  الهلك المهوى بين الجبلين (maqayis;tahdhib)؛ الهلكة مشرفة المهواة (ayn;tahdhib)؛ المهلكة والمهلكة المفازة (sihah)؛ مفازة هالكة من سلكها أي هالكة السالكين (ayn;tahdhib)
- **B007** belirli bir toplulukla anılan demirci — belirli bir toplulukla anılan demirci; genelleşmiş olarak demirci
  الهالكي الحداد (ayn)؛ الهالكي فالحداد نسب إلى الهالك بن عمرو (maqayis)؛ الهالكي الحداد نسب إلى الهالك ابن عمرو بن أسد (sihah)؛ أراد بالهالكي الحداد (tahdhib)؛ الهالكي كان حدادا من قبيلة هالك فسمي كل حداد هالكيا (mufradat)
- **B008** her durumda — her durumda; nasıl anlaşılırsa anlaşılsın
  افعل ذاك إما هلكت هلك أي على كل حال (sihah)؛ إما هلكت هلك أي على ما خيلت أي على كل حال (tahdhib)؛ إن شبه عليكم بكل معنى وعلى كل حال (tahdhib)
- **B009** kendini bir uğurda tüketmek veya yolda tükenmek [kalıp] — bir iş uğruna kendini tüketmek · geçen yolcuyu tüketen yol
  استهلك الرجل في كذا وكذا إذا جهد نفسه واهتلك مثله (tahdhib)؛ أي يجهد قلبه في إثرها (tahdhib)؛ طريق مستهلك الورد أي يجهد من سلكه (tahdhib)
- **B010** çölde yönünü şaşırıp dolanmak [kalıp] — ıssız arazide yönünü şaşırıp dönmek
  كنت أتهلك في مفاوز أي كنت أدور فيها شبه المتحير (tahdhib)؛ بين السماء وبين الأرض تهتلك (tahdhib)
- **B011** boş ve asılsız bir işe saplanmak — boş ve asılsız bir işe saplanma
  وقع في وادي تهلك بضم التاء والهاء واللام مشددة وهو غير مصروف مثل تخيب ومعناهما الباطل (sihah)
- **B012** doymaz bir istekle saldırırcasına yönelme — doymaz bir istekle yönelmek · doymak bilmeyen, aşırı istekli kadın ve erkekler · doymak bilmeyen istek taşıyan benlik
  الهلكى الشرهون من الرجال والنساء (tahdhib)؛ الهالكة النفس الشرهة (tahdhib)؛ هلك يهلك هلاكا إذا شره (tahdhib)؛ يقال للمزاحم على الموائد المتهالك (tahdhib)
- **B013** ailesi içinde yok olan ya da ailesini yok eden kimse [kalıp] — ailesi içinde yok olan veya ailesini yok eden kimse
  هالك أهل الذي يهلك في أهله وكذلك الذي يهلك أهله (ayn)؛ هو الذي يهلك في أهله ويكون هالك أهل الذي يهلك أهله (tahdhib)

## ش د د (root_000782): 43:8 أَشَدَّ

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

## ب ط ش (root_000126): 43:8 بَطْشًا

- **B001** ezici güç ve zor kullanarak sertçe ele alma — ezici güçle sertçe ele alma · onu zor kullanarak sertçe ele almak · zor kullanılarak yapılan sert bir ele alış · güçle kavrayan ve zor kullanan el · zor kullanarak ele almada çok güçlü · ona karşı ezici güçle sertçe mücadele etmek · öfkeyle kırbaç ya da kılıç kullanarak vurmak veya öldürmek
  أخذ الشيء بقهر وغلبة وقوة؛ يد باطشة (maqayis)؛ البطش التناول عند الصولة؛ الأخذ الشديد في كل شيء؛ ذو البأس والأخذ لأعدائه (ayn)؛ بطش يبطش بطشا وهو الأخذ الشديد؛ رجل شديد البطش (jamhara)؛ البطشة السطوة والأخذ بالعنف؛ باطشه مباطشة (sihah)؛ البطش التناول عند الصولة؛ تقتلون عند الغضب؛ بالسوط والسيف (tahdhib)؛ البطش تناول الشيء بصولة؛ يد باطشة (mufradat)

## م ض ي (root_001430): 43:8 وَمَضَىٰ

- **B001** geçip gitme — geçip gitmek · bir yerden veya yerin üzerinden geçmek · geçip gitme · içinden geçip ilerleme · geçip gitmeye koyulma
  أصل صحيح يدل على نفاذ ومرور (maqayis)؛ مضى الشيء يمضي مضيا (ayn)؛ مضى الشئ مضيا ذهب (sihah)؛ مضيت بالمكان أو مضيت عليه (tahdhib)؛ المضي والمضاء النفاذ في الأعيان والأحداث (mufradat)
- **B002** yürürlüğe koyma ve geçerli sayma — işin yürürlüğe girmesi · işin uygulanır duruma gelmesi · işi uygulamayı sürdürmek · uygulanması kararlaştırılmış iş · işi yürürlüğe koymak · satışı onaylamak · onaylamak · satışı geçerli saymak · işi uygulamayı sürdürmek
  المضاء النفاذ في الأمر (maqayis)؛ مضى في أمره مضاء (ayn)؛ مضى في الأمر مضاء نفذ وأمضيت الأمر أنفذته (sihah)؛ مضيت ببيعي أي أجزته ومضيت على بيعي أي أجزته (tahdhib)؛ مضيت على الأمر مضوا وهذا أمر ممضو عليه (tahdhib)
- **B003** öne geçme — öne geçme · ata verilen geleneksel ad
  المضواء التقدم (maqayis;sihah;tahdhib)؛ يكنى الفرس أبا المضاء (ayn)؛ الفرس يكنى أبا المضاء (tahdhib)
- **B004** yaşamdan ayrılma — yaşamdan ayrıldı
  يقال للرجل إذا مات قد مضى (tahdhib)

## م ث ل (root_001397): 43:8 مَثَلُ, 43:17 مَثَلًا, 43:56 وَمَثَلًا, 43:57 مَثَلًا, 43:59 مَثَلًا

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

## س ء ل (root_000661): 43:9 سَأَلْتَهُم, 43:19 وَيُسْـَٔلُونَ, 43:44 تُسْـَٔلُونَ, 43:45 وَسْـَٔلْ, 43:87 سَأَلْتَهُم

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 43:9 سَأَلْتَهُم, 43:19 وَيُسْـَٔلُونَ, 43:44 تُسْـَٔلُونَ, 43:45 وَسْـَٔلْ, 43:87 سَأَلْتَهُم: withheld observed target; not identity

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

## خ ل ق (root_000434): 43:9 خَلَقَ, 43:9 خَلَقَهُنَّ, 43:12 خَلَقَ, 43:16 يَخْلُقُ, 43:19 خَلْقَهُمْ, 43:87 خَلَقَهُمْ

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

## س م و (root_000745): 43:9 ٱلسَّمَٰوَٰتِ, 43:11 ٱلسَّمَآءِ, 43:82 ٱلسَّمَٰوَٰتِ, 43:84 ٱلسَّمَآءِ, 43:85 ٱلسَّمَٰوَٰتِ

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

## ECHO و س م (root_001650): for 43:9 ٱلسَّمَٰوَٰتِ, 43:11 ٱلسَّمَآءِ, 43:82 ٱلسَّمَٰوَٰتِ, 43:84 ٱلسَّمَآءِ, 43:85 ٱلسَّمَٰوَٰتِ: withheld observed target; not identity

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

## ء ر ض (root_000025): 43:9 وَٱلْأَرْضَ, 43:10 ٱلْأَرْضَ, 43:60 ٱلْأَرْضِ, 43:82 وَٱلْأَرْضِ, 43:84 ٱلْأَرْضِ, 43:85 وَٱلْأَرْضِ

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

## ق و ل (root_001272): 43:9 لَيَقُولُنَّ, 43:13 وَتَقُولُوا۟, 43:20 وَقَالُوا۟, 43:22 قَالُوٓا۟, 43:23 قَالَ, 43:24 قَٰلَ, 43:24 قَالُوٓا۟, 43:26 قَالَ, 43:30 قَالُوا۟, 43:31 وَقَالُوا۟, 43:38 قَالَ, 43:46 فَقَالَ, 43:49 وَقَالُوا۟, 43:51 قَالَ, 43:58 وَقَالُوٓا۟, 43:63 قَالَ, 43:77 قَالَ, 43:81 قُلْ, 43:87 لَيَقُولُنَّ, 43:88 وَقِيلِهِۦ, 43:89 وَقُلْ

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

## ECHO ق ل ل (root_001251): for 43:9 لَيَقُولُنَّ, 43:13 وَتَقُولُوا۟, 43:20 وَقَالُوا۟, 43:22 قَالُوٓا۟, 43:23 قَالَ, 43:24 قَٰلَ, 43:24 قَالُوٓا۟, 43:26 قَالَ, 43:30 قَالُوا۟, 43:31 وَقَالُوا۟, 43:38 قَالَ, 43:46 فَقَالَ, 43:49 وَقَالُوا۟, 43:51 قَالَ, 43:58 وَقَالُوٓا۟, 43:63 قَالَ, 43:77 قَالَ, 43:81 قُلْ, 43:87 لَيَقُولُنَّ, 43:88 وَقِيلِهِۦ, 43:89 وَقُلْ: withheld observed target; not identity

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

## ع ز ز (root_001008): 43:9 ٱلْعَزِيزُ

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

## ع ل م (root_001040): 43:9 ٱلْعَلِيمُ, 43:20 عِلْمٍ, 43:46 ٱلْعَٰلَمِينَ, 43:61 لَعِلْمٌ, 43:84 ٱلْعَلِيمُ, 43:85 عِلْمُ, 43:86 يَعْلَمُونَ, 43:89 يَعْلَمُونَ

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

## م ه د (root_001451): 43:10 مَهْدًا

- **B001** beşik — beşik; bebeğin uyuması için hazırlanmış yer
  المهد الموضع يهيأ لينام فيه الصبي (ayn;tahdhib)؛ المهد مهد الصبي (sihah)؛ المهد ما يهيأ للصبي (mufradat)؛ ومنه المهد (maqayis)
- **B002** döşek veya döşenip düzlenmiş yer — döşek, altlık; döşenip düzlenmiş yer · döşeklerin veya hazırlanmış yerlerin çoğul biçimleri · yatağı sermek ve bastırıp düzlemek · düz ve kolay geçilir alçak zemin
  المهاد اسم أجمع من المهد كالأرض جعلها الله مهادا للعباد (ayn;tahdhib)؛ المهاد الفراش (sihah)؛ المهد والمهاد المكان الممهد الموطأ (mufradat)؛ المهاد الوطاء من كل شيء (maqayis)؛ المهدة من الأرض ما انخفض في سهولة واستواء (tahdhib)
- **B003** hazırlayıp düzene koyma; yerleşip sağlamlaşma — işi hazırlamak, önünü açmak ve düzene koymak · kendisi için bir iyiliğin yolunu hazırlamak · işleri düzeltip yoluna koyma · mazereti açıklayıp kabul edilir hale getirme · yerleşme, tutunma ve sağlamlaşma
  مهدت الأمر وطأته (maqayis)؛ مهدت لنفسي خيرا أي هيأته ووطأته (ayn;tahdhib)؛ تمهيد الأمور تسويتها وإصلاحها وتمهيد العذر بسطه وقبوله (sihah)؛ مهدت لك كذا هيأته وسويته (mufradat)
- **B004** hörgücün yükselip yayvanlaşması veya dolgunlaşması [kalıp] — hörgücü veya sırt çıkıntısı yükselip yayvanlaşmak ve düzgünleşmek · hörgücü dolgunlaşıp güzel görünmek
  امتهد سنام البعير وغيره ارتفع (maqayis)؛ أي ارتفع وتوى وصار كالمهاد (maqayis)؛ امتهاد السنام انبساطه وارتفاعه (sihah)؛ امتهد السنام أي تسوى فصار كمهاد أو مهد (mufradat)؛ وامتهد الغارب فعل الدمل (ayn;tahdhib)؛ اسمهد السنام إذا حسن وامتلأ (maqayis)
- **B005** daha önce hiçbir iyiliği dokunmamış olmak — bana daha önce hiçbir iyiliği dokunmadı
  ما امتهد فلان عندي يدا لم يولك نعمة ولا معروفا؛ ما امتهد فلان عندي مهد ذاك

## س ب ل (root_000672): 43:10 سُبُلًا, 43:37 ٱلسَّبِيلِ

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

## ه د ي (root_001583): 43:10 تَهْتَدُونَ, 43:22 مُّهْتَدُونَ, 43:24 بِأَهْدَىٰ, 43:27 سَيَهْدِينِ, 43:37 مُّهْتَدُونَ, 43:40 تَهْدِى, 43:49 لَمُهْتَدُونَ

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

## ECHO ه د د (root_001580): for 43:10 تَهْتَدُونَ, 43:22 مُّهْتَدُونَ, 43:24 بِأَهْدَىٰ, 43:27 سَيَهْدِينِ, 43:37 مُّهْتَدُونَ, 43:40 تَهْدِى, 43:49 لَمُهْتَدُونَ: withheld observed target; not identity

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

## ن ز ل (root_001492): 43:11 نَزَّلَ, 43:31 نُزِّلَ

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

## م و ه (root_001458): 43:11 مَآءًۢ

- **B001** su ve su adının biçim ailesi — bilinen ve içilen su · su adının küçültme biçimi · su adının çoğul biçimleri · suya ilişkin, suyla ilgili · su adının tekil veya dişil biçimi · suyun rengi
  الموه أصل بناء الماء (maqayis)؛ الموهة لون الماء وتصغير الماء مويه والجميع المياه (ayn)؛ الماء معروف وأصله الهاء مكان الهمزة (jamhara)؛ الماء الذي يشرب وأصله موه ويجمع على أمواه ومياه وتصغيره مويه (sihah)؛ أصل الماء ماه وجمع الماء مياه وأمواه (tahdhib)؛ أصل ماء موه بدلالة أمواه ومياه ومويه (mufradat)
- **B002** suyun belirmesi, çoğalması, içeri girmesi veya bir şeyi doldurması [kalıp] — kuyunun suyu belirdi veya çoğaldı · gemiye su girdi · toprakta sızıntı suyu belirdi · gök bol su akıttı · hurma veya üzüm meyvesi suyla dolup olgunlaşmaya hazırlandı · suyu bol kuyu
  ماهت السفينة تموه وتماه دخل فيها الماء وأماهت الأرض ظهر فيها نز (maqayis;ayn)؛ ماهت الركي إذا كثر ماؤها (jamhara)؛ ماهت الركية إذا ظهر ماؤها وكثر وكذلك السفينة إذا دخل فيها الماء وأماهت الأرض ظهر فيها النز (sihah)؛ موهت السماء أسالت ماء كثيرا وماهت البئر وأماهت في كثرة مائها وتموه ثمر النخل والعنب إذا امتلأ ماء (tahdhib)؛ ماهت الركية تميه وتماه وبئر ميهة وماهة (mufradat)
- **B003** su verme, içine su koyma ve sulanmış hale getirme — nesneye su verdi veya içine su koydu · adama su verdi · adama veya bıçağa su verdi · hokkaya su döktü · bana su ver · sulanmış ağaç
  موهت الشيء كأنك سقيته الماء وأمهت السكين وأمهيته سقيته (maqayis)؛ مهت الرجل ومهته إذا سقيته الماء وأمهت الرجل والسكين وأمهت الدواة صببت فيها الماء (sihah)؛ موه فلان حوضه إذا جعل فيه الماء وأمهني أي اسقني وشجر موهي إذا كان مسقويا (tahdhib)
- **B004** üreme sıvısını dişinin döl yatağına bırakma — erkek, üreme sıvısını dişinin döl yatağına bıraktı
  أماه الفحل ألقى ماءه في رحم الأنثى (maqayis;sihah)
- **B005** başka metali altın veya gümüşle kaplama ve gerçeği görünüşle gizleme — nesneyi, alttaki başka metali örtecek biçimde gümüş veya altınla kapladı · kılıcı veya başka bir nesneyi altınla kaplama · gerçeği başka göstererek aldatma · yanlışı doğru gibi gösteren aldatıcı · yanlışı doğru görünümüne soktu
  موهت الشيء طليته بفضة أو ذهب (maqayis)؛ موهت الشيء طليته بفضة أو ذهب وتحت ذلك نحاس أو حديد ومنه التمويه وهو التلبيس (sihah)؛ الميه طلاء السيف وغيره بماء الذهب ومنه قيل للمخادع مموه وقد موه علي الباطل إذا لبسه (tahdhib)
- **B006** belirli kalıplarda yüz güzelliği, söz tatlılığı, üzüm olgunluğu veya hayvan varlığının semirmesi [kalıp] — üzüm olgunlaşıp güzel renk aldı · yüzündeki gençlik canlılığı ve güzellik · üzerinde canlı bir güzellik var · güzel ve tatlı söz · ailesinin süsü ve güzelliği · hayvan varlığı bahar otuyla semirdi
  ما أحسن موهة وجهه أي ترقرق ماء الشباب فيه (maqayis)؛ الموهة لون الماء يقال ما أحسن موهة وجهه (ayn)؛ عليه موهة من حسن وتموه المال للسمن وتموه العنب إذا جرى فيه الينع وحسن لونه وكلام عليه موهة أي حسن وحلاوة (tahdhib)
- **B007** kaya kristali veya ayna — kaya kristali · suyla ilişkilendirilen ayna
  الماوية حجر البلور وكذلك الماوية المرآة (maqayis)؛ الماوية المرآة كأنها منسوبة إلى الماء (sihah)
- **B008** gönlünde suyu çok denilen, bazı aktarımlarda anlayışı kıt adam [kalıp] — anlayışı kıt ve ağır adam · gönlünde suyun çok olduğu söylenen adam
  رجل ماه القلب أي كثير ماء القلب ويكون صاحب ذلك بليدا (maqayis)؛ رجل ماه أي كثير ماء القلب أي بليد (sihah)؛ رجل ماهي القلب كثر ماء قلبه (mufradat)

## ق د ر (root_001205): 43:11 بِقَدَرٍ, 43:42 مُّقْتَدِرُونَ

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

## ن ش ر (root_001503): 43:11 فَأَنشَرْنَا

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

## ب ل د (root_000148): 43:11 بَلْدَةً

- **B001** sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan — yerleşilmiş ya da boş, sınırları belirli yer · yerler, yöreler · mezarlık, mezar veya toprak · açık, çıplak alan
  البلد معروف والبلدة أيضا والبلاد جمع بلد (jamhara)؛ البلد كل موضع مستحيز من الأرض عامر أو غير عامر أو خال أو مسكون (tahdhib)؛ البلد المكان المحيط المحدود المتأثر باجتماع قطانه وإقامتهم فيه (mufradat)؛ البلد المقبرة ويقال هو نفس القبر وربما جاء البلد يعني به التراب (tahdhib)؛ من البلد وهو الفضاء البراز (maqayis)
- **B002** göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma — boğazın altındaki göğüs çukuru ve çevresi · göğüs · deve çökerken göğsünü yere koydu
  بلدة النحر وسطه (jamhara)؛ البلدة الصدر وفلان واسع البلدة أي واسع الصدر (sihah)؛ البلدة بلدة النحر وهي الثغرة وما حولها (tahdhib)؛ سميت الكركرة بلدة لذلك وربما استعير ذلك لصدر الإنسان (mufradat)؛ الأصل الصدر ويقال وضعت الناقة بلدتها بالأرض إذا بركت (maqayis)
- **B003** kaşların arasındaki açıklık ve kaşları birleşmemiş olma — kaşların arasındaki açık ve temiz bölge · kaşları birleşmemiş
  ربما سميت البلجة بلدة (jamhara)؛ البلدة والبلدة نقاوة ما بين الحاجبين ورجل أبلد أي أبلج بين البلد (sihah)؛ الأبلد من الرجال الذي ليس بمقرون وهي البلدة والبلدة (tahdhib)؛ البلدة البلجة ما بين الحاجبين تشبيها بالبلد لتمددها (mufradat)؛ الأبلد الذي ليس بمقرون الحاجبين يقال لما بين حاجبيه بلدة (maqayis)
- **B004** yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı — Ay durağı veya yıldızsız gök bölgesi · göksel aslanın göğüs bölgesi
  البلدة منزل من منازل القمر (jamhara)؛ البلدة من منازل القمر وهي ستة أنجم من القوس (sihah)؛ البلدة في السماء موضع لا نجوم فيه بين النعائم وسعد الذابح (tahdhib)؛ البلدة منزل من منازل القمر (mufradat)؛ البلدة النجم يقولون هو بلدة الأسد أي صدره (maqayis)
- **B005** şaşkınlıkla duraksama; metaneti yitirip boyun eğme — şaşkınlığa düşüp kararsızca duraksamak · bir işte şaşırıp ne yapacağını bilememek · metaneti yitirip sinme ve boyun eğme
  تبلد الرجل من هذا إذا لحقته حيرة فضرب بيده على بلدة نحره (jamhara)؛ تبلد أي تردد متحيرا (sihah)؛ المتبلد الذي يتردد متحيرا (tahdhib)؛ التبلد نقيض التجلد وهو استكانة وخضوع (tahdhib)؛ قيل للمتحير بلد في أمره وأبلد وتبلد (mufradat)؛ تبلد الرجل إذا وضع يده على صدره عند تحيره في الأمر (maqayis)
- **B006** bedende, deride veya başka bir yüzeyde kalan iz — bedende veya başka bir yüzeyde kalan iz; izler
  البلد الأثر في البدن وغيره والجمع أبلاد (jamhara)؛ البلد الأثر والجمع أبلاد (sihah)؛ البلد الأثر بالجسد وجمعه أبلاد (tahdhib)؛ ولاعتبار الأثر قيل بجلده بلد أي أثر وجمعه أبلاد (mufradat)؛ البلد الأثر وجمعه أبلاد (maqayis)
- **B007** kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma — zeka, kavrayış ve atılganlık düşüklüğü · ağır kavrayışlı; yarışta geri kalan · işte ve cömertlikte gerileyip güçsüzleşti
  رجل بليد بين البلادة ضد النحرير (jamhara)؛ البلادة ضد الذكاء وقد بلد بالضم فهو بليد (sihah)؛ أبلد الرجل إذا كانت دابته بليدة (sihah)؛ البلادة نقيض النفاذ والمضاء في الأمور (tahdhib)؛ فرس بليد إذا تأخر عن الخيل السوابق (tahdhib)؛ بلد إذا نكس في العمل وضعف حتى في الجود (tahdhib)؛ لكثرة وجود البلادة فيمن كان جلف البدن (mufradat)
- **B008** iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı — iri ve kaba yapılı · enli; deve için sert ve dayanıklı
  رجل أبلد غليظ الخلق (jamhara)؛ الأبلد الرجل العظيم الخلق والبلندى العريض والمبلندى من الجمال الصلب الشديد (sihah)؛ رجل أبلد عبارة عن عظيم الخلق (mufradat)
- **B009** bir yerde kalıp ikamet etme ve orada oturan kişi — bir yerde kalıp ikamet etmek · bir yerde oturan, sakin
  بلد بالمكان أقام به فهو بالد (sihah)؛ بلدت بالمكان أبلد بلودا أي أقمت به (tahdhib)؛ بلد لزم البلد (mufradat)؛ البالد قياسا المقيم بالبلد (maqayis)
- **B010** kendini yere atıp yapışma; yere yapışık eski havuz — kendini yere atmak veya yere yapışmak · yere yapışık eski havuz
  بلد تبليدا ضرب بنفسه الأرض وأبلد لصق بالأرض (sihah)؛ المبلد الحوض القديم ههنا وأراد ملبد فقلب وهو اللاصق بالأرض (tahdhib)؛ بلد الرجل بالأرض إذا لزق بها (maqayis)؛ مبلد بين موماة يذكر حوضا لاصقا بالأرض (maqayis)
- **B011** kılıç veya sopalarla karşılıklı vuruşma — kılıç veya sopalarla karşılıklı dövüşme
  المبالدة مثل المباطلة (sihah)؛ المبالدة كالمبالطة بالسيوف والعصي إذا تجالدوا بها (tahdhib)؛ المبالدة بالسيوف مثل المبالطة وقال بعضهم اشتق من الأول كأنهم لزموا الأرض فقاتلوا عليها (maqayis)
- **B012** deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası — deve kuşunun yumurta çukuru · deve kuşunun bırakıp gittiği yumurta
  البلد أدحي النعام يقال هو أذل من بيضة البلد أي من بيضة النعام التي تتركها (sihah)

## م و ت (root_001454): 43:11 مَّيْتًا

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

## خ ر ج (root_000400): 43:11 تُخْرَجُونَ

- **B001** bir yerden ya da durumdan dışarı çıkma — dışarı çıktı; bir yerden veya durumdan ayrıldı · dışarı çıkma; bir durumdan ayrılma · dışarı çıkan veya ayrılan · çıkış yeri veya çıkış yönü
  النفاذ عن الشيء (maqayis)؛ الخروج نقيض الدخول (ayn;jamhara;tahdhib)؛ خرج خروجا برز من مقره أو حاله (mufradat)
- **B002** bir şeyi çıkarma, elde etme veya yetiştirme — dışarı çıkardı veya ortaya koydu · nesneleri dışarı çıkarma veya görünür kılma · çıkarıp elde etti · işleyip ortaya çıkarma veya çeşitlere ayırma · eğitim görüp yetişti · birinin elinde yetişmiş öğrenci
  اخترجت الرجل واستخرجته سواء (ayn)؛ الاستخراج كالاستنباط (sihah)؛ الإخراج أكثر ما يقال في الأعيان (mufradat)؛ خريج فلان كأنه أخرجه من حد الجهل (maqayis)
- **B003** düzenli mali yükümlülük, getiri veya gider — mali ödeme, vergi veya ürün getirisi · ürün getirisi, vergi veya zorunlu ödeme · hizmetindeki kişiyle aylık ödeme üzerinde anlaştı · efendisine düzenli ödeme yapmakla yükümlü köle · sorumluluk karşılığında elde edilen ürün getirisi
  الخراج والخرج الإتاوة لأنه مال يخرجه المعطي (maqayis)؛ الخرج والخراج ما يخرج من المال في السنة بقدر معلوم (ayn;tahdhib)؛ الخراج الغلة (tahdhib)؛ الخرج بإزاء الدخل (mufradat)
- **B004** bedende çıkan irinli şişlik veya yara — bedende çıkan şişlik, çıban veya irinli yara
  الخراج بالجسد (maqayis)؛ الخراج ورم وقرح يخرج من ذاته (ayn)؛ ما خرج على الجسد من دمل ونحوه (jamhara)؛ ما يخرج في البدن من القروح (sihah)؛ ورم وقرح يخرج بدابة أو غيرها من الحيوان (tahdhib)
- **B005** bulutun ilk kez oluşup belirmesi [kalıp] — bulut oluşmaya veya belirmeye başladı · gökyüzü bulutlandıktan sonra açıldı
  الخروج خروج السحابة (maqayis)؛ الخروج السحاب أول ما يبدأ (ayn)؛ السحاب أول ما ينشأ (sihah)؛ أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن (tahdhib)؛ الخرج أيضا من السحاب (mufradat)
- **B006** yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma — kendi değeriyle seçkinleşen kimse · soyu seçkin olmadığı halde üstün çıkan at · yöneticinin itaatinden ayrılan topluluk · birinin yeteneğinin ve iş bilirliğinin ortaya çıkması
  الخارجي الرجل المسود بنفسه من غير أن يكون له قديم (maqayis)؛ الخارجي الذي لم يكن له شرف في آبائه فيخرج ويشرف بنفسه (ayn)؛ فرس خارجي إذا خرج جوادا بين مقرفين (jamhara)؛ الخارجية من الخيل التي ليس لها عرق في الجودة فتخرج سوابق (tahdhib)؛ الخوارج خارجين عن طاعة الإمام (mufradat)
- **B007** iki renkli ya da yer yer kesintili görünüm — bir işi çeşitlendirme veya yer yer farklılaştırma · iki renkli veya kesintili görünüm · siyahı beyazından çok olan iki renkli · iki renkli dişi hayvan veya iki renkli yer · bitkisi yer yer çıkan arazi · otlağın bir bölümünü yiyip bir bölümünü bıraktı · yazı yüzeyinde bazı yerleri boş bıraktı · verimli ve verimsiz yerleri bir arada bulunan yıl
  الخرج لونان بين سواد وبياض (maqayis)؛ الأخرج لون سواده أكثر من بياضه (ayn;tahdhib)؛ أرض مخرجة نبتها في مكان دون مكان (ayn;sihah;tahdhib;mufradat)؛ خرج الغلام لوحه إذا ترك فيه مواضع لم يكتبها (tahdhib)
- **B008** erkek deve yapısında doğmuş dişi deve [kalıp] — erkek deve yapısında doğmuş dişi deve
  ناقة مخترجة إذا خرجت على خلقة الجمل (maqayis;ayn;sihah)؛ المخترجة أنها جبلت على خلقة الجمل (tahdhib)
- **B009** iki gözlü taşıma torbası — iki gözlü taşıma torbası · iki gözlü taşıma torbaları
  الخرج والخرجة جمعه جوالق ذو أونين (ayn)؛ الخرج من الأوعية معروف والجمع خرجة (sihah)؛ الخرج هذا الوعاء ثلاثة خرجة وهو جوالق ذو أونين (tahdhib)
- **B010** özel çağrılı geleneksel çocuk oyunu — erkek çocukların oynadığı geleneksel oyun · çocukların oynadığı geleneksel oyun · oyunda eldekini çıkarmayı isteyen çağrı
  الخريج لعبة لفتيان العرب يقال فيها خراج خراج (maqayis;sihah)؛ الخراج والخريج مخارجة لعبة لفتيان العرب (ayn)؛ الخراج لعبة يلعب بها الصبيان (jamhara)؛ خراج اسم لعبة لهم معروفة (tahdhib)
- **B011** uyakta bağlantı sesinden sonraki elif harfi — uyakta bağlantı sesinden sonra gelen elif harfi
  الخروج الألف التي بعد الصلة في القافية (ayn;tahdhib)
- **B012** ortak payları karşılıklı bölüşüp tasfiye etme — karşılıklı katkı ve bölüşme · ortakların veya mirasçıların paylarını tasfiye etmesi · iki ortağın mal ve alacak üzerinde karşılıklı hesaplaşması
  المخارجة المناهدة بالأصابع والتخارج التناهد (sihah)؛ يتخارج الشريكان وأهل الميراث (tahdhib)؛ لا بأس أن يتخارجا يعني العين والدين (tahdhib)
- **B013** uzun boyunlu at niteliği — uzun boynuyla dizginin erişimini aşan at
  الخروج من صفات الخيل وهو الذي يطول عنقه (tahdhib)

## ز و ج (root_000652): 43:12 ٱلْأَزْوَٰجَ, 43:70 وَأَزْوَٰجُكُمْ

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

## ك ل ل (root_001315): 43:12 كُلَّهَا, 43:35 كُلُّ (also echo for 43:73 تَأْكُلُونَ)

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

## ف ل ك (root_001177): 43:12 ٱلْفُلْكِ

- **B001** dairesel olma ve dönme — dairesel dönme; yuvarlaklık
  أصل صحيح يدل على استدارة في شيء (maqayis)؛ الفلك دوران السماء وهو اسم للدوران خاصة (ayn;tahdhib)؛ استدارة السماء (tahdhib)
- **B002** göksel yörünge düzeni — göksel yörünge; gök çemberi · bir yörüngede; dönme içinde
  فلك السماء (maqayis)؛ الفلك دوران السماء (ayn;tahdhib)؛ سبعة أطواق دون السماء ركبت فيها النجوم (ayn;tahdhib)؛ مجرى الكواكب (mufradat)؛ موج مكفور تجري فيه الشمس والقمر والكواكب (tahdhib)
- **B003** gemi; gemiler topluluğu — gemi; gemiler topluluğu
  السفينة تسمى فلكا ولعلها تسمى فلكا لأنها تدار في الماء (maqayis)؛ الفلك السفينة يذكر ويؤنث وهي واحدة وتكون جمعا (ayn;tahdhib)؛ الفلك جماعة السفن (ayn)؛ الفلك: السفينة ويستعمل ذلك للواحد والجمع (mufradat)
- **B004** yuvarlak tepeli küçük yükselti — çevresine göre yükselen yuvarlak arazi parçası · tek parça taşlı, yuvarlak küçük tepe · çevresi açık kum tepesinin etrafında dolanan
  الفلك قطع من الأرض مستديرة مرتفعة عما حولها (maqayis)؛ الفلكة أكمة من حجر واحد مستديرة كأنها فلكة مغزل (ayn)؛ الأفلك الذي يدور حول الفلك وهو التل من الرمل حوله فضاء (tahdhib)؛ أصاغر الإكام وإنما فلكها اجتماع رأسها كأنها فلكة مغزل (tahdhib)
- **B005** iğ ağırlığı ve ona benzeyen yuvarlak biçim — iğin yuvarlak ağırlık parçası; ağırşak · dil kökünün sert bölümü · kadının memesinin yuvarlaklaşıp ağırşak biçimi alması · genç kızın memesinin ağırşak gibi yuvarlaklaşması · memesi ağırşak gibi yuvarlaklaşmış kadın · ağırşak biçimli kalçası olan erkek köle
  فلكة المغزل سميت لاستدارتها (maqayis)؛ فلك ثدي المرأة إذا استدار (maqayis)؛ فلكت الجارية أي صار ثديها كالفلكة (ayn;tahdhib)؛ فلكة اللسان ما صلب من أصله (maqayis)؛ العبد الذي له ألية على خلقة الفلكة (tahdhib)؛ فلكة المغزل ومنه اشتق فلك ثدي المرأة (mufradat)
- **B006** yavrunun diline engel yerleştirerek emmesini önleme — oğlağın diline emmesini önleyen bir engel yerleştirmek · deve yavrusunun dilini delip ağırşak biçimli kıl engel yerleştirerek emmesini önleme
  فلكت الجدى بقضيب أو هلب أدرته على لسانه لئلا يرتضع (maqayis)؛ فلكت الجدي وهو قضيب يدار على لسانه لئلا يرضع (ayn;tahdhib)؛ التفليك أن يجعل الراعي من الهلب مثل فلكة المغزل ثم يثقب لسان الفصيل فيجعله فيه لئلا يرضع (tahdhib)؛ فلكت الجدي إذا جعلت في لسانه مثل فلكة يمنعه عن الرضاع (mufradat)
- **B007** ileri geri çalkalanan deniz dalgası — ileri geri çalkalanan deniz dalgası · dönüp durma içinde; çalkantı içinde
  الفلك الموج إذا ماج في البحر فاضطرب وجاء وذهب (tahdhib)؛ كأنه يدور في فلك (tahdhib)

## ن ع م (root_001525): 43:12 وَٱلْأَنْعَٰمِ, 43:13 نِعْمَةَ, 43:59 أَنْعَمْنَا

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

## ر ك ب (root_000589): 43:12 تَرْكَبُونَ

- **B001** bineğe ya da tekneye binme ve üzerinde veya içinde bulunma — hayvana ya da tekneye binmek · binen kimse; özellikle deve yolcusu · binekli yolcu topluluğu · yolcu taşıyan develer · gemi yolcuları · binilen hayvan ya da taşıt · binek hayvanı veya kara ya da deniz taşıtı; binme yeri veya binme eylemi · eyer üzengisi · develerle taşınan yağ · binmeye elverişli dişi deve · binilecek çağa gelmek · başkasının atıyla savaşa katılan kimse
  يقال ركب ركوبا يركب والركاب المطي (maqayis); الركوب في الأصل كون الإنسان على ظهر حيوان وقد يستعمل في السفينة (mufradat); الركبان والأركوب والركب فراكبو الدابة وركاب السفينة الذين يركبونها (ayn;tahdhib); الركاب الإبل التي يسار عليها والركوب والركوبة ما يركب (sihah;tahdhib); ركاب السرج معروف (jamhara;sihah;tahdhib); المركب الذي يغزو على فرس غيره (maqayis;ayn;jamhara;tahdhib)
- **B002** üstüne çıkma veya üst üste yığılma — bir şeyin başka bir şeyin üstüne çıkması · hörgücün önündeki üst üste yağ katmanları · üst üste binmiş, yığılmış · bulutları taşıyan ya da üstlerine çıkan rüzgarlar
  أصل واحد مطرد منقاس وهو علو شيء شيئا (maqayis); كل شيء علا شيئا فقد ركبه (ayn;tahdhib); رواكب الشحم طرائق بعضها فوق بعض (maqayis;ayn;tahdhib); تراكب السحاب وتراكم صار بعضه فوق بعض (tahdhib); المتراكب ما ركب بعضه بعضا (mufradat); الرياح ركاب السحاب (ayn;tahdhib)
- **B003** işe girişme, yükleme veya yük altında kalma — birine iş yüklemek; işi ya da suçu işlemek · borç altında kalmak · vergi toplayan görevlilere haksız yük çıkaran kişi
  ركب فلان فلانا بأمر وارتكبه وكل شيء علا شيئا فقد ركبه وركبه الدين ونحوه (ayn;tahdhib); ارتكاب الذنوب إتيانها (sihah); ركيب السعاة بمعنى الراكب يركب السعاة فيظلمهم (tahdhib)
- **B004** parçayı yerine geçirip sabitleme — bir parçayı bir şeyin içine yerleştirip sabitlemek · yerine takılmış parça · parçaların düzenli biçimde birleştirilmesi
  كل شيء أثبته في شيء فقد ركبته نحو السنان في الرمح وغيره (jamhara); تركيب الفص في الخاتم والنصل في السهم ركبته فتركب فهو مركب وركيب (sihah); المركب المثبت في الشيء كتركيب الفصوص (ayn); شيء حسن التركيب والركيب اسما للمركب في الشيء مثل الفص ونحوه (tahdhib)
- **B005** diz eklemi ve dizle kurulan vurma ilişkisi — diz eklemi · dizi iri ya da kusurlu olan · dizine vurmak ya da kendi diziyle vurmak
  ركبة الإنسان وهي عالية على ما هي فوقه (maqayis); ركبة البعير في يده (ayn;tahdhib); الركبة معروفة (jamhara;sihah;mufradat); الأركب العظيم الركبة (maqayis;sihah;tahdhib); ركبته أصبت ركبته وأصبته بركبتي (mufradat); ركبت الرجل إذا ضربته بركبتك أو ضربته بركبته (maqayis;jamhara;sihah)
- **B006** kasık ve üreme organı çevresindeki beden bölgesi — kasık kıllarının çıktığı bölge veya üreme organı çevresindeki etli kısım
  الركب ركب المرأة ولا يقال للرجل (maqayis;tahdhib); الأركاب للنساء خاصة (ayn); الركبان أصلا الفخذين اللذان عليهما لحم الفرج من الرجل والمرأة (jamhara); الركب منبت العانة للمرأة خاصة وقال الفراء للرجل والمرأة (sihah); الركب كناية عن فرج المرأة (mufradat)
- **B007** gövdeye bağlı köksüz sürgün ve bağlı bitki parçaları — gövdeye bağlı, toprağa kök salmamış hurma sürgünü · başakta ilk çıkan öncü parçalar · kesilmiş yabani otun dip kısmı
  الركابة شبه فسيلة من أعلى النخلة عند قمتها (maqayis;ayn;tahdhib); الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق (ayn;sihah;tahdhib); الراكبة فسيلة تتعلق بالنخلة لا تبلغ الأرض (jamhara); ركبان السنبل سوابق السنبل التي تخرج في أوله (tahdhib); الركبة أصل الصليانة إذا قطعت (tahdhib)
- **B008** saygın soy ve toplumsal köken [kalıp] — soyu, kökeni ve toplumsal dayanağı saygın olan
  المركب الأصل والمنبت يقال هو كريم المركب (maqayis); رجل كريم المركب أي كريم أصل منصبه في قومه (ayn;sihah); هذا الرجل كريم المركب أي كريم الأصل (tahdhib)
- **B009** kanallar arası toprak sırtı ve tarımsal uzantıları — bağ kanalları arasındaki yüksek sırt; sıraya dikilmiş hurmalık ya da ekili tarla
  الركيب ما بين نهري الكرم وهو الظهر الذي بين النهرين ويكون عاليا على دونه (maqayis;ayn); الركيب ما بين نهري الكرم (tahdhib); ركيب من نخل وهو ما غرس سطرا على جدول أو غير جدول (tahdhib); يقال للقراح الذي يزرع فيه ركيب (tahdhib)
- **B010** koyunlarda sırtı etkileyen hastalık — koyunların sırtını etkileyen hastalık
  الراكب داء يأخذ الغنم في ظهورها (maqayis)

## س و ي (root_000766): 43:13 لِتَسْتَوُۥا۟, 43:13 ٱسْتَوَيْتُمْ

- **B001** iki şeyi birbirine denk kılma veya denk sayma — bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek · iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme · bir işte aynı düzeyde ve eşit durumda · eş, benzer · ikisi de bir, ikisi eşit · özellikle, hele
  أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)
- **B002** kendi içinde düzgün ve tam duruma gelme — bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek · eğrilikten kurtulup doğrulmak · yapısı düzgün, eksiksiz ve sağlıklı · çocuklarımız ve hayvanlarımız iyi durumda · düz arazi
  سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)
- **B003** üzerine çıkıp yerleşmek veya egemen olmak [kalıp] — bineğinin sırtına çıkıp yerleşmek · üzerine çıkmak ya da egemen olmak
  استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)
- **B004** bir hedefe yönelip onu amaç edinmek [kalıp] — göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek
  استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)
- **B005** gençlik olgunluğuna erişmek — gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak
  استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)
- **B006** iki yanın ortasında ve ikisine karşı yansız olma — orta; iki yana eşit ve yansız durum · iki yana eşit, ortada ve herkesçe bilinen yer · iki tarafın da hakkını gözeten ortak söz
  السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)
- **B007** başka ve ayrı olan — başka, öteki
  سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)
- **B008** birinin yöneldiği hedefe yönelmek [kalıp] — birinin tuttuğu yöne ya da hedefe yönelmek
  يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)
- **B009** geniş ve açık arazi — geniş, açık ya da pürüzsüz arazi
  السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)
- **B010** devenin sırtına konan dolgulu binme örtüsü — devenin sırtına ya da hörgücü çevresine konan binme örtüsü
  السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)
- **B011** atlayıp dışarıda bırakmak — atlamak, dışarıda bırakmak ve göz ardı etmek
  أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)
- **B012** ayın on üçüncü gecesi — ayın dengeli göründüğü on üçüncü gece
  ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)
- **B013** başına denk mal ve bolluk [kalıp] — başına denk sayılan mal miktarı ya da bolluk
  جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)

## ظ ه ر (root_000970): 43:13 ظُهُورِهِۦ, 43:33 يَظْهَرُونَ

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

## ر ب ب (root_000532): 43:13 رَبِّكُمْ, 43:14 رَبِّنَا, 43:32 رَبِّكَ, 43:32 رَبِّكَ, 43:35 رَبِّكَ, 43:46 رَبِّ, 43:49 رَبَّكَ, 43:64 رَبِّى, 43:64 وَرَبُّكُمْ, 43:77 رَبُّكَ, 43:82 رَبِّ, 43:82 رَبِّ, 43:88 يَٰرَبِّ

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

## ECHO ر ب و (root_000537): for 43:13 رَبِّكُمْ, 43:14 رَبِّنَا, 43:32 رَبِّكَ, 43:32 رَبِّكَ, 43:35 رَبِّكَ, 43:46 رَبِّ, 43:49 رَبَّكَ, 43:64 رَبِّى, 43:64 وَرَبُّكُمْ, 43:77 رَبُّكَ, 43:82 رَبِّ, 43:82 رَبِّ, 43:88 يَٰرَبِّ: withheld observed target; not identity

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

## س ب ح (root_000666): 43:13 سُبْحَٰنَ, 43:82 سُبْحَٰنَ

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

## س خ ر (root_000685): 43:13 سَخَّرَ, 43:32 سُخْرِيًّا

- **B001** bir şeyi istenen işe boyun eğdirip yöneltme — boyun eğdirme ve istenen işe yöneltme · bir şeyi buyruğa boyun eğdirip biri için kolaylaştırmak · istenen işe koşulmuş olan · geminin söz dinleyip uygun rüzgarla rahat yol alması
  سخر الله الشيء إذا ذلله لأمره وإرادته (maqayis)؛ سخر الله لفلان أي سهله له (jamhara)؛ التسخير التذليل وسفن سواخر إذا أطاعت وطابت لها الريح (sihah)؛ سخرت السفينة إذا أطاعت وطاب لها السير وقد سخرها الله تسخيرا (tahdhib)؛ التسخير سياقة إلى الغرض المختص قهرا (mufradat)
- **B002** karşılıksız zorla çalıştırma — karşılıksız zorla çalışma · birini karşılıksız zorla çalıştırmak · bir hizmetçiyi ya da binek hayvanını karşılık vermeden kullanmak · zorla hizmete koşulan kimse · zorla çalıştırılan kimse
  رجل سخره يسخر في العمل (maqayis)؛ كلفته عملا بلا أجرة وهي السخرة (jamhara)؛ سخره تسخيرا كلفه عملا بلا أجرة وكذلك تسخره (sihah)؛ ما تسخرت من خادم أو دابة بلا أجر ولا ثمن وعبيدا وإماء وأجراء وتسخرت دابة ركبتها بغير أجر (tahdhib)؛ السخري هو الذي يقهر فيتسخر بإرادته (mufradat)
- **B003** birini küçümseyerek alaya alma — biriyle alay etmek · biriyle alay etmek · alay etme, alay · birini alay konusu yapmak · başkalarıyla alay eden kimse · başkalarının alay ettiği kimse · alaylı gülüş
  سخرت منه إذا هزئت به (maqayis)؛ سخرت من الرجل سخرية وسخرا وسخريا ورجل سخرة يسخر من الناس وسخرة يسخر الناس منه (jamhara)؛ سخرت منه وسخرت به وهزئت منه وهزئت به والاسم السخرية والسخرى والسخري (sihah)؛ سخر منه وبه إذا تهزأ به والسخرية مصدر (tahdhib)؛ سخرت منه واستسخرته للهزء منه والسخرية لفعل الساخر (mufradat)

## ق ر ن (root_001221): 43:13 مُقْرِنِينَ, 43:36 قَرِينٌ, 43:38 ٱلْقَرِينُ, 43:53 مُقْتَرِنِينَ

- **B001** bir şeyi başka bir şeye katıp bağlama — bir şeyi başka bir şeye katmak veya bağlamak · iki şeyi bağlayan ip; iki şeyi birleştirme · iki ibadeti tek uygulamada birleştirmek · iki hurmayı birlikte yemek · zincirlerde birbirine bağlanmış
  قارنت بين الشيئين؛ القران الحبل يقرن به شيئان؛ القران أن تقرن حجة بعمرة؛ القران أن تقرن بين تمرتين (maqayis)؛ قرنت الشيء أقرنه قرنا أي شددته إلى شيء؛ لا قران ولا تفتيش في أكل التمر (ayn)؛ قرنت الشئ بالشئ وصلته به؛ مقرنين في الاصفاد؛ قرن بين الحج والعمرة قرانا (sihah)؛ قرنت بين البعيرين وقرنتهما إذا جمعت بينهما في حبل قرنا؛ جاءوا قرانى وجاءوا فرادى (tahdhib)؛ الاقتران كالازدواج في كونه اجتماع شيئين أو أشياء؛ قرنت البعير بالبعير (mufradat)
- **B002** yalıtık adlandırmalar — yakın arkadaş, eşlik eden kimse · erkeğin eşi, hayat arkadaşı
  القرينة نفس الإنسان كأنهما قد تقارنا؛ قرينة الرجل امرأته (maqayis)؛ القرين صاحبك الذي يقارنك؛ قرينة الرجل امرأته (ayn)؛ القرين المصاحب؛ قرينة الرجل امرأته (sihah)؛ القرين صاحبك الذي يقارنك؛ قرينة الرجل امرأته (tahdhib)؛ قرينه؛ فهو له قرين؛ وجمعه قرناء؛ وقيضنا لهم قرناء (mufradat)
- **B003** yaşça ya da güççe denk kişi — yaşıt, aynı yaştaki kişi · güç ve yiğitlikte denk rakip
  قرنك في الشجاعة؛ القرن مثلك في السن (maqayis)؛ القرن في السن اللدة؛ القرن ضدك في القوة (ayn)؛ القرن مثلك في السن؛ القرن بالكسر كفؤك في الشجاعة (sihah)؛ هو على قرنه أي على سنه؛ هو قرنه في السن؛ قرنه بكسر إذا كان مثله في الشدة والشجاعة (tahdhib)؛ فلان قرن فلان في الولادة وقرينه وقرنه في الجلادة وفي القوة (mufradat)
- **B004** bir şeyin üstesinden gelebilen — gücü yeten, üstesinden gelebilen
  فلان مقرن لكذا أي مطيق له؛ وما كنا له مقرنين؛ يجوز أن يكون قرنا له (maqayis)؛ أقرنت لهذا البعير أو البرذون أي أطعته؛ وما كنا له مقرنين أي مطيقين (ayn)؛ أقرن له أي أطاقه وقوي عليه؛ وما كنا له مقرنين أي مطيقين (sihah)؛ أقرن الرجل إذا أطاق أمر ضيعته؛ أقرن له إذا قوي عليه؛ ما كنا له مطيقين؛ أنا لفلان مقرن أي مطيق (tahdhib)
- **B005** aynı çağın insanları veya kuşak dönemi — aynı çağda yaşayan kuşak
  القرن الأمة من الناس والجمع قرون؛ وقرونا بين ذلك كثيرا (maqayis)؛ القرن الأمة؛ قرن بعد قرن؛ عمر كل قرن ستون سنة (ayn)؛ القرن من الناس أهل زمان واحد؛ القرن أيضا ثمانون سنة ويقال ثلاثون سنة (sihah)؛ القرن أهل كل مدة؛ الذين كانوا مقترنين في ذلك الوقت؛ القرن الوقت من الزمان (tahdhib)؛ القرن القوم المقترنون في زمن واحد وجمعه قرون (mufradat)
- **B006** boynuz veya boynuz biçimli çıkıntı — hayvan boynuzu · boynuz gibi saç tutamları veya örgüler · İki Boynuzlu lakabı
  القرن للشاة وغيرها وهو ناتىء قوي؛ الذوائب قرونا؛ ذات القرون؛ القرن جبيل صغير منفرد (maqayis)؛ قرن الثور معروف وموضعه من رأس الإنسان قرن أيضا؛ لكل رأس قرنان؛ القرن جبل صغير منفرد؛ القرنان ما يبنى على رأس البئر؛ الأقرن والقرناء من الشاء ذات القرون؛ سمي ذا القرنين لأنه ضرب ضربتين على قرنيه (ayn)؛ القرن للثور وغيره؛ القرن الخصلة من الشعر؛ القرن جبيل صغير منفرد؛ قرن الشمس أعلاها وأول ما يبدو منها؛ القرنة الطرف الشاخص من كل شئ؛ ذو القرنين لقب إسكندر الرومي (sihah)؛ القرن قرن الشاة والبقر وغيرهما؛ القرن الخصلة من الشعر؛ قرنا الشيطان ناحيتا رأسه؛ القرن جبيل صغير؛ قرنا البئر؛ ذو قرنيها؛ ذكر ذا القرنين فقال ضربوه على قرنيه ضربتين (tahdhib)
- **B007** yaya bağlı ok kılıfı ve silahlı taşıyıcısı — yaya bağlanan ok kılıfı; küçük ok kılıfı · yanında kılıç ve ok taşıyan kişi
  القرن جعيبة صغيرة تضم إلى الجعبة الكبيرة؛ القارن الذي معه سيف ونبل (maqayis)؛ القرن جعبة صغيرة تضم إلى الجعبة الكبيرة؛ في القرن يكون حبلا ويكون جعبة (ayn)؛ القرن بالتحريك الجعبة؛ القرن أيضا السيف والنبل؛ رجل قارن معه سيف ونبل (sihah)؛ القرن السيف والنبل؛ رجل قارن؛ القرن جعبة من جلود؛ القرن من خشب وعليه أديم؛ القرن الجعبة (tahdhib)؛ القرن الجعبة ولا يقال لها قرن إلا إذا قرنت بالقوس (mufradat)
- **B008** uzuvları veya hareketleri eşleşen binek — uzuvlarını veya ayak izlerini eşleyen binek
  القرون من النوق المقرنة القادمين والآخرين من أخلافها؛ القرون التي إذا جرت وضعت يديها ورجليها معا (maqayis)؛ القرون الناقة إذا جرت وضعت يديها ورجليها معا؛ القرون من النوق المقترنة القادمين والآخرين؛ القرون التي إذا بعرت قارنت بعرها (ayn)؛ قرن الفرس إذا وقعت حوافر رجليه مواقع حوافر يديه؛ القرون الناقة التي تجمع بين محلبين؛ القرون الذي تقع حوافر رجليه مواقع حوافر يديه (sihah)؛ القرون الناقة التي تجمع بين محلبين؛ التي تضع خف رجليها على خف يدها؛ التي إذا بعرت قارنت بعرها (tahdhib)؛ القرون من البعير الذي يضع رجله موضع يده؛ ناقة قرون إذا دنا أحد خلفيها من الآخر (mufradat)
- **B009** bedene bağlı iç benlik — kişinin iç benliği; razı olan veya boyun eğen içi
  القرينة نفس الإنسان؛ سامحته قرينته وقرونته وقرونه أي نفسه (maqayis)؛ القرون النفس؛ قرينته وقرينه قهرها (ayn)؛ أسمحت قرينه وقرونه وقرونته وقرينته أي ذلت نفسه وتابعته على الأمر (sihah)؛ سامحت قرونه وهي النفس؛ أسمحت قرونته باليأس أي طابت نفسه (tahdhib)؛ القرون النفس لكونها مقترنة بالجسم (mufradat)
- **B010** bir terleme nöbeti veya çabuk terleyen at — bir ter boşalması veya terleme nöbeti
  القرن الدفعة من العرق والجمع قرون (maqayis)؛ القرن حلبة من عرق والجمع القرون؛ حلبنا الفرس قرنا أو قرنين أي عرقناه؛ القرون من الدواب الذي يعرق سريعا (sihah)؛ القرن الدفعة من العرق؛ القرون العرق؛ القرون الفرس الذي يعرق سريعا إذا جرى (tahdhib)

## ق ل ب (root_001248): 43:14 لَمُنقَلِبُونَ

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

## ع ب د (root_000973): 43:15 عِبَادِهِۦ, 43:19 عِبَٰدُ, 43:20 عَبَدْنَٰهُم, 43:26 تَعْبُدُونَ, 43:45 يُعْبَدُونَ, 43:59 عَبْدٌ, 43:64 فَٱعْبُدُوهُ, 43:68 يَٰعِبَادِ, 43:81 ٱلْعَٰبِدِينَ

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

## ج ز ء (root_000241): 43:15 جُزْءًا

- **B001** yetip başka bir şeye gerek bırakmama — bir şeyle yetinmek ve onu yeterli bulmak · bir şeyin ihtiyaca yeterli gelmesi · başkasının yerini tutup ihtiyacı karşılamak · yetinme ve başka bir şeye gereksinim duymama · develerin taze otla yetinip suya gereksinim duymaması · taze otla yetinip suya gereksinim duymayan ceylan · birinin yerini tutup onun gördüğü işi görmek
  اجتزأت بالشيء إذا اكتفيت به (maqayis); أجزأني الشيء إجزاء إذا كفاني (maqayis); أجزأني الشيء مهموز أي كفاني (ayn); تجزأت بكذا واجتزأت به أي اكتفيت به (ayn); يجزئ عن هذا (ayn); جزأت بالشيء أي اكتفيت به (sihah); جزئت الإبل بالرطب عن الماء (ayn;sihah); أجزأت عنك شاة أي قضت (sihah); أجزأت عنك مجزأ فلان ومجزأة فلان أي أغنيت عنك مغناه (sihah)
- **B002** bütünün bölümü ve bölümlere ayırma — bütünün parçası, bölümü veya onu oluşturan öğe · bir şeyi bölümlere ayırmak · kullarından bir bölümü O'na pay saydılar
  الجزء الطائفة من الشيء (maqayis); الجزء واحد الأجزاء (sihah); جزأت الشيء جزءا قسمته وجعلته أجزاء (sihah); جزء الشيء ما يتقوم به جملته (mufradat); وجعلوا له من عباده جزءا أنه اصطفى البنات على البنين (maqayis)
- **B003** el aleti sapı ve alete sap takma — bıçak, biz veya ayakkabı dikme aracının sapı · bir el aletine sap takmak
  الجزأة نصاب السكين وقد أجزأتها إجزاء إذا جعلت لها جزأة (maqayis); الجزأة بالضم نصاب الإشفى والمخصف وقد أجزأته جعلت له نصابا (sihah)

## ء ن س (root_000059): 43:15 ٱلْإِنسَٰنَ, 43:33 ٱلنَّاسُ

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

## ك ف ر (root_001307): 43:15 لَكَفُورٌ, 43:24 كَٰفِرُونَ, 43:30 كَٰفِرُونَ, 43:33 يَكْفُرُ

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

## ء خ ذ (root_000018): 43:16 ٱتَّخَذَ, 43:32 لِّيَتَّخِذَ, 43:48 وَأَخَذْنَٰهُم

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

## ب ن ي (root_000156): 43:16 بَنَاتٍ, 43:16 بِٱلْبَنِينَ, 43:57 ٱبْنُ, 43:59 لِّبَنِىٓ

- **B001** parçaları birleştirerek yapı kurma, kurulan yapı ve kurmaya olanak sağlama — parçaları birleştirip yapı kurmak · kurulmuş yapı; duvar, ev veya gök · çok sayıda saray yapmak · bir ev yapmak ve edinmek · birine ev yapması için ev ya da gerekli gereci vermek · keçi sürüsü çadır kurmaya yetecek kıl ve topluluk sağlamaz
  بناء الشيء بضم بعضه إلى بعض (maqayis)؛ بنى البناء يبني بنيا وبناء (ayn;tahdhib;mufradat)؛ بنى فلان بيتا من البنيان وبنى قصورا (sihah)؛ البنيان الحائط (sihah)؛ البناء اسم لما يبنى بناء (mufradat)؛ السماء بنيناها (mufradat)؛ أبنيت فلانا بيتا إذا أعطيته بيتا يبنيه (sihah;tahdhib)
- **B002** kuruluş biçimi ve doğuştan yapı — kuruluş biçimi; doğuştan beden yapısı
  فلان صحيح البنية أي الفطرة (sihah)؛ البنية الهيئة التي بني عليها (tahdhib)
- **B003** Kabe, Allah'ın Evi veya Mekke için özel ad — Kabe, Allah'ın Evi veya Mekke için kullanılan ad
  تسمى مكة البنية (maqayis)؛ البنية الكعبة (ayn;sihah;tahdhib)؛ البنية يعبر بها عن بيت الله (mufradat)
- **B004** deriden örtü, çadırımsı kap, yaygı veya saklama kabı — deriden çadırımsı örtü, yaygı, hasır ya da kap · yağmurdan korunmak ya da yere sermek için yaygı · otururken bacaklarını birbirinden ayırmak
  المبناة كهيئة الستر؛ كهيئة القبة تجلل بيتا عظيما (ayn)؛ المبناة النطع؛ ويقال هي العيبة (sihah;tahdhib)؛ المبناة قبة من أدم (tahdhib)؛ المبناة حصير أو نطع يبسطه التاجر على بيعه (tahdhib)؛ بسطنا له بناء أي نطعا (tahdhib)
- **B005** kirişine aşırı yapışan kusurlu yay — kirişine yapışıp onu kopma sınırına getiren kusurlu yay · kirişine yapışan kusurlu yay için bölgesel biçim
  قوس بانية وهي التي بنت على وترها (maqayis;sihah;tahdhib)؛ يكاد وترها ينقطع للصوقه بها (maqayis;tahdhib)؛ طيئ تقول قوس باناة (maqayis;tahdhib)؛ البائنة التي بانت من وترها وكلاهما عيب (tahdhib)
- **B006** gelini yeni evine götürme, eşle birleşme ve bunu yapan damat — gelini yeni evine götürmek veya eşiyle birleşmek · düğün sonrası eşiyle birleşen damat
  بنى على أهله بناء أي زفها (sihah)؛ الداخل بأهله كان يضرب عليها قبة ليلة دخوله بها (sihah)؛ الباني العروس الذي بنى على أهله (tahdhib)؛ بنى فلان على أهله وقد زفها (tahdhib)؛ العامة تقول بنى بأهله وليس من كلام العرب (sihah;tahdhib)
- **B007** oğul ve kız bağı, çocuk edinme ve kaynağa dayalı adlandırma — oğul; bir kaynaktan çıkan veya onun yetiştirdiği kimse · kız çocuk · oğullar, çocuklar ve kızlar · oğulluk ve çocukluk bağı · birini oğul edinmek veya oğulluğunu ileri sürmek · bir şeye kaynağı, yetişmesi, hizmeti ya da sürekli bağlılığı nedeniyle bağlanan kimse
  الابن أصله بنو (sihah;mufradat)؛ البنوة مصدر الابن (tahdhib)؛ تبنيت فلانا إذا اتخذته ابنا (sihah)؛ تبنيته إذا ادعيت بنوته (tahdhib)؛ سماه بذلك لكونه بناء للأب (mufradat)؛ كل ما يحصل من جهة شيء أو من تربيته أو بتفقده أو كثرة خدمته له أو قيامه بأمره هو ابنه (mufradat)؛ فلان ابن الحرب وابن السبيل وابن الليل وابن العلم (mufradat)؛ بنت فلان وابنة فلان وبنات (sihah;tahdhib;mufradat)
- **B008** küçük, dallanmış veya yerden çıkan şeylere çocuk adı verme — ana yoldan ayrılan küçük yollar · kız çocukların oynadığı küçük insan biçimli oyuncaklar · tapınma yerindeki çakıl taşları · bir çakıl taşı ile bir ot türü
  بنيات الطريق هي الطرق الصغار تتشعب من الجادة (sihah)؛ البنات التماثيل الصغار التي تلعب بها الجواري (sihah)؛ إحدى بنات مساجد الله كأنه جعله حصاة (sihah)؛ بنت الأرض الحصاة وابن الأرض ضرب من البقل (sihah)؛ يقال لكل ما يحصل من جهة شيء هو ابنه (mufradat)
- **B009** kaburgalar veya ev direkleri; yerleşip huzur bulma — göğüs kafesi kaburgaları veya ev direkleri · bir yere yerleşip huzur bulmak
  البواني أضلاع الزور؛ ألقى بوانيه إذا أقام بالمكان واطمأن؛ البوائن جمع البوان وهو اسم كل عمود في البيت
- **B010** yiyeceğin eti büyütüp besili kılması — yiyeceğin eti büyütüp besili kılması · otururken bacaklarını birbirinden ayırmak
  بنى لحم فلان طعامه يبنيه بناء إذا عظم من الأكل؛ بنى السويق لحمها؛ كما بنى بخت العراق القت

## ب ن و (root_001959): documented alternative for 43:16 بَنَاتٍ, 43:16 بِٱلْبَنِينَ, 43:57 ٱبْنُ, 43:59 لِّبَنِىٓ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## ص ف و (root_000873): 43:16 وَأَصْفَىٰكُم

- **B001** arınma, arıtma ve arı özü ayırma — karışım veya bulanıklıktan arınmak · arılık ve duruluk · bir şeyin arı özü ve en iyi bölümü · arıtmak veya arı bölümünü ayırmak · su birikintisinin duru bölümünü alıp ayırmak · süzgeç veya arıtma aracı
  أصل واحد يدل على خلوص من كل شوب (maqayis)؛ الصفو نقيض الكدر وصفوة كل شيء خالصه وخيره (ayn)؛ الصفاء خلاف الكدر وصفوة الشيء خالصه وصفيته تصفية والمصفاة الراوق (sihah)؛ الصفو نقيض الكدر وصفوة كل شيء خالصه والمصفاة الراووق وصفيت الشراب (tahdhib)؛ أصل الصفاء خلوص الشيء من الشوب (mufradat)
- **B002** en iyiyi seçme ve ayrıcalık tanıma — Tanrı'nın seçtiği ve üstün kıldığı kişi · en iyiyi seçip ayırma · onu başkaları arasından seçtim · seçilmiş ve üstün tutulmuş kişi · bir şeyi yalnız ona ayırarak ayrıcalık tanımak
  محمد صفوة الله وخيرته ومصطفاه (maqayis)؛ الاصطفاء الاختيار افتعال من الصفوة (ayn)؛ اصطفيته اخترته وأصفيته بالشيء إذا آثرته به (sihah)؛ الاصطفاء الاختيار افتعال من الصفوة وأصفيت فلانا بكذا أي آثرته به (tahdhib)؛ الاصطفاء تناول صفو الشيء واصطفيت كذا على كذا أي اخترت (mufradat)
- **B003** bölüşüm öncesi yönetici payı ve ayrılmış mülk — yöneticinin bölüşümden önce kendine ayırdığı özel pay · bölüşümden önce seçilip ayrılan pay ve bunun çoğulu · hükümdarın yakın çevresine ayırdığı mülkler
  الصفي ما اصطفاه الإمام من المغنم لنفسه والصفية والجمع الصفايا (maqayis)؛ الصفي ما كان رسول الله يصطفيه لنفسه من الغنيمة (ayn)؛ الصفي ما يصطفيه الرئيس من المغنم لنفسه قبل القسمة والصفية أيضا (sihah)؛ الصفي من الغنيمة ما اختاره الرئيس قبل القسمة ومنه الصوافي (tahdhib)؛ الصفي والصفية ما يصطفيه الرئيس لنفسه (mufradat)
- **B004** içten ve karşılıklı dostluk — sevgi ve kardeşlikte içten arılık · içten dostluk kurduğu kişi · ona içten ve arı bir sevgi göstermek
  الصفاء مصافاة المودة والإخاء وصفي الإنسان الذي يصافيه المودة (ayn)؛ أصفيته الود أخلصته له وصافيته وتصافينا تخالصنا (sihah)؛ الصفاء مصافاة المودة والإخاء وصفي الإنسان أخوه الذي يصافيه الإخاء (tahdhib)
- **B005** bol sütlü hayvan veya çok meyveli hurma ağacı — bol süt veren dişi deve · çok meyve veren hurma ağacı
  الصفية والصفي الناقة الكثيرة اللبن والنخلة الكثيرة الحمل والجمع الصفايا وسميت صفيا لأن صاحبها يصطفيها (maqayis)؛ ناقة صفي كثيرة اللبن ونخلة صفي كثيرة الحمل وتجمع صفايا (ayn)؛ الصفي الناقة الغزيرة الدر والجمع صفايا (sihah)؛ ناقة صفي كثيرة اللبن ونخلة صفي كثيرة الحمل والناقة الصفي الغزيرة (tahdhib)؛ يقالان للناقة الكثيرة اللبن والنخلة الكثيرة الحمل (mufradat)
- **B006** pürüzsüz, geniş ve çıplak kaya — pürüzsüz, geniş ve çıplak kaya · pürüzsüz kaya · pürüzsüz taşlar veya düz kaya · pürüzsüz taş veya taşlık yüzey · kutsal kentteki bilinen tepe
  الصفا الحجر الأملس وهو الصفوان وسميت صفوانة لأنها تصفو من الطين والرمل (maqayis)؛ الصفا حجر صلب أملس وصفوانة حجارة ملس لا تنبت شيئا (ayn)؛ الصفاة صخرة ملساء والصفواء الحجارة اللينة الملس وكذلك الصفوان والصفا موضع بمكة (sihah)؛ الصفا العريض من الحجارة الأملس ومنه الصفا والمروة (tahdhib)؛ الصفا للحجارة الصافية والصفوان كالصفا (mufradat)
- **B007** güneşli, açık ve çok soğuk gün [kalıp] — güneşi açık, çok soğuk gün
  يقال يوم صفوان إذا كان صافي الشمس شديد البرد (maqayis)؛ يوم صفوان إذا كان صافي الشمس شديد البرد (sihah)؛ يوم صفوان صافي الشمس شديد البرد (mufradat)
- **B008** üretimin kesilmesi veya ilerleyişin engele takılması [kalıp] — tavuğun yumurtlaması kesildi · şairin şiir söylemesi kesildi · kazıcı, ilerlemeyi durduran kaya tabakasına ulaştı · erkeğin üreme sıvısını tüketmesi · adamın maldan ve görgüden yoksun kalması
  أصفت الدجاجة إذا انقطع بيضها وشبه بذلك الشاعر إذا انقطع شعره (maqayis)؛ أصفت الدجاجة إذا انقطع بيضها وأصفى الشاعر إذا انقطع شعره (sihah)؛ أصفت الدجاجة إصفاء إذا انقطع بيضها وأصفى الشاعر إذا لم يقل شعرا (tahdhib)؛ أصفت الدجاجة إذا انقطع بيضها وأصفى الشاعر إذا انقطع شعره وأصفى الحافر إذا بلغ صفا (mufradat)

## ب ش ر (root_000120): 43:17 بُشِّرَ

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

## ء ح د (root_000017): 43:17 أَحَدُهُم

- **B001** tek ve eşi olmayan olma — bir tane; tek ve eşsiz · yalnız bir, yalnız bir
  أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)
- **B002** hiç kimse — olumsuzlukta hiç kimse
  لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)
- **B003** bir sayısı, onlu kuruluşları ve on bire çıkarma — saymanın başlangıcındaki bir · on bir, on bir dişil biçimi ve yirmi bir · onları on bire çıkarmak
  أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)
- **B004** iki kişiden biri, ilk olan ve haftanın ilk günü — ikinizden biri · Pazar günü · Pazar günleri
  أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)
- **B005** tek başına kalma ve birer birer gelme — tek başına kalmak; işi yalnız üstlenmek · birer birer, ayrı ayrı
  ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)
- **B006** Medine'deki belirli bir dağın özel adı — Medine'deki dağın özel adı
  أحد جبل بالمدينة (sihah)

## ر ح م (root_000552): 43:17 لِلرَّحْمَٰنِ, 43:19 ٱلرَّحْمَٰنِ, 43:20 ٱلرَّحْمَٰنُ, 43:32 رَحْمَتَ, 43:32 وَرَحْمَتُ, 43:33 بِٱلرَّحْمَٰنِ, 43:36 ٱلرَّحْمَٰنِ, 43:45 ٱلرَّحْمَٰنِ, 43:81 لِلرَّحْمَٰنِ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ظ ل ل (root_000966): 43:17 ظَلَّ

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

## و ج ه (root_001630): 43:17 وَجْهُهُۥ

- **B001** yüz ve bir şeyin öne bakan yanı — yüz; bir şeyin öne bakan veya görünen yanı · kötü bir yüz ifadesiyle bakmak
  الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)
- **B002** yön ve hedef; o yöne sevk etme veya yolu belli etme — yön, taraf · yönelinen yön veya hedef · bir şeyi belirli bir yöne çevirmek veya göndermek · tek bir yöne çevrilmiş · bir şeye doğru yönelmek · rüzgarın çakılı bir yöne sürüklemesi · yolu yürüyerek izini belirginleştirmek · perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak
  الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)
- **B003** karşı karşıya gelme ve doğrudan yüzüne söyleme — birinin karşısına çıkmak, onunla yüz yüze gelmek · karşılaşma, yüzleşme · karşında, tam karşı tarafta
  واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)
- **B004** yüzün varlığın kendisini temsil etmesi — 
  ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)
- **B005** amaç edinip yönelme; ibadette içtenlikle bağlanma — 
  وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)
- **B006** toplumsal itibar, yüksek mevki ve önde gelen kişi — topluluğun önderi · yerleşimin ileri gelenleri · itibarlı, yüksek mevkili · toplumsal itibar ve mevki · itibarlı ve yüksek mevkili olmak · onu itibarlı ve yüksek mevkili kılmak
  وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)
- **B007** günün başı, ilk saatleri [kalıp] — günün başı, ilk saatleri
  وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)
- **B008** sözün veya işin doğru yönü ve ona uygun düzenleme — sözün amaçlanan yönü · doğru görüş · aklına bir görüş gelmek · bir şeyi doğru yolundan saptırmak · işi gerektiği gibi düzenleyip her şeyi yerine koymak · hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi
  وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)
- **B009** yaşlanıp ömrünün son dönemine girmek — yaşlanıp ömrünün son dönemine girmek
  توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)
- **B010** doğumda ellerin veya ön ayakların önce çıkması — elleri veya ön ayakları önce çıkan yavru · yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak
  للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)
- **B011** kurucu uzun ünlü ile ana uyak harfi arasındaki harf — kurucu uzun ünlü ile ana uyak harfi arasındaki harf
  التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)
- **B012** hıyar veya kavunun altını kazıp yana yatırma — hıyar veya kavunun altını kazıp yana yatırma
  التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)
- **B013** yüzüne vurma ve yüzüne vurulmuş olma — birinin yüzüne vurmak · yüzüne vurulmuş
  وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)
- **B014** yanına gelen kişiyi geri çevirmek — yanına gelen kişiyi geri çevirmek
  أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)
- **B015** iki yüzlü nesne; içiyle dışı uyuşmayan kişi [kalıp] — iki yüzü bulunan kumaş · içiyle dışı uyuşmayan iki yüzlü kimse
  كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)

## س و د (root_000757): 43:17 مُسْوَدًّا

- **B001** karalık, kararma ve karartma — kara renk, karalık · kara renkli · kararmak · beyazlığını giderip karartmak · kara tenli bir oğlu olmak
  خلاف البياض في اللون (maqayis)؛ السواد نقيض البياض (ayn;tahdhib)؛ السواد لون وقد اسود الشيء وسودته أنا (sihah)؛ سودت الشيء إذا غيرت بياضه سوادا (tahdhib)
- **B002** görünür kişi ya da nesne silueti — insanın veya nesnenin görünen silueti · eşya, ölü veya başka şeylerin görünen siluetleri
  سواد كل شيء شخصه (maqayis)؛ السواد الشخص (ayn;sihah)؛ السواد عند العرب الشخص وكذلك البياض (tahdhib)؛ الأساود الشخوص من المتاع (tahdhib)
- **B003** yakından ve gizlice konuşma — gizli ve özel konuşma · biriyle gizlice konuşmak
  السواد السرار يقال ساوده مساودة وسوادا إذا ساره (maqayis)؛ السواد السرار ساودته مساودة وسوادا أي ساررته (ayn;sihah)؛ السرار لا يكون إلا من إدناء السواد من السواد (tahdhib)
- **B004** topluluk içinde üstünlük ve önderlik — topluluğunun önderi ve iyilikte üstünü · topluluk içindeki üstünlük ve önderlik · topluluğuna önder olmak · topluluğu tarafından önder yapılmak · birinden daha üstün konumda olmak · onun kocası · önder nitelikli bir oğlu olmak · bir topluluğun önderini öldürmek, tutsak etmek veya ondan kız istemek · seçkin bir kadınla evlenmek
  السيادة ... سمي سيدا لأن الناس يلتجئون إلى سواده (maqayis)؛ السودد معروف والمسود الذي سوده قومه (ayn)؛ ساد قومه يسودهم سيادة وسوددا فهو سيدهم (sihah)؛ السيد الذي يفوق في الخير قومه؛ سيدها وبعلها أي زوجها (tahdhib)
- **B005** kalabalık, halk kitlesi ve çoğunluk — büyük insan topluluğu · halkın geneli ve çoğunluğu · en büyük çoğunluk · ordugahın çadırları, araçları ve hayvanları · insan toplulukları
  السواد العدد الكثير (maqayis)؛ السواد جماعة من الناس (ayn)؛ سواد الناس عامتهم وكل عدد كثير (sihah)؛ السواد الأعظم من الناس هم الجمهور الأعظم والعدد الأكثر (tahdhib)
- **B006** kent çevresindeki köyler ve kırsal bölgeler [kalıp] — iki kentin çevresindeki köyler ve kırsal bölgeler · bir yönetim merkezinin çevresindeki köyler ve kırsal bölgeler
  السواد ما حوالي الكوفة من القرى والرساتيق (ayn)؛ سواد الكوفة والبصرة قراهما (sihah)؛ كورة كذا وسوادها أي ما حوالي قصبتها وفسطاطها من قراها ورساتيقها (tahdhib)
- **B007** iri kara yılan — iri kara yılan · kara yılanlar · yılan ile akrep · her yıl deri değiştiren iri yılan
  الأساود جمع الأسود وهي الحيات (maqayis)؛ الأساود حيات سود واحدها أسود (ayn)؛ الأسود العظيم من الحيات وفيه سواد (sihah;tahdhib)؛ الأسودين الحية والعقرب (tahdhib)
- **B008** hurma ile su veya süt ikilisi [kalıp] — hurma ile su veya hurma ile süt çifti
  الأسودان التمر والماء (maqayis;sihah;tahdhib)؛ الأسودان التمر واللبن ويقال التمر والماء (ayn)؛ نعتا معا بنعت واحد (tahdhib)
- **B009** özel adlandırma kümesi — kalbin özü ve iç bölümü · kalbin en iç özü · çörek otu tanesi
  سواد القلب وسويداؤه وهي حبته (maqayis)؛ السويداء حبة الشونيز وسواد القلب حبته (ayn)؛ سواد القلب حبته وكذلك أسوده وسوداؤه وسويداؤه (sihah)؛ السويداء حبة الشينيز؛ سواد قلبه (tahdhib)
- **B010** kara, taşlık ve düz yamaç — kara, kaba taşlı ve düz yamaç · bu taşlı yamaç türünün bir parçası · bu tür kara taşlı yamaç alanları
  السود سفح مستو بالأرض كثير الحجارة خشنها والغالب عليها لون السواد (ayn;tahdhib)؛ القطعة منها سودة والجميع الأسواد (ayn;tahdhib)

## ك ظ م (root_001303): 43:17 كَظِيمٌ

- **B001** öfkeyi içine atıp dışa vurmama — öfkeyi içine gömüp dışa vurmama · öfkesini içine atıp belli etmemek · öfkelerini içlerine atıp belli etmeyenler
  الكظم اجتراع الغيظ والإمساك عن إبدائه (maqayis)؛ كظم الرجل غيظه اجترعه (ayn)؛ كظم غيظه كظما اجترعه (sihah)؛ كظمت الغيظ إذا أمسكت على ما في نفسك منه (tahdhib)؛ كظم الغيظ حبسه (mufradat)
- **B002** soluk çıkışı ve soluğun tutulup daralması — soluğu tutulduğu için sessiz kalma · sessiz duran topluluk · soluğunu içinde tutmak · soluk çıkış yolu · soluk yolunu sıkıp nefes alamaz hâle getirmek · soluğu daralmış, bunalmış · soluğu tutulmuş, sıkıntıya düşmüş
  الكظوم السكوت (maqayis)؛ الكظم مخرج النفس (maqayis;ayn;tahdhib;mufradat)؛ أخذ بكظمه فما يقدر أن يتنفس (ayn)؛ الكظوم احتباس النفس (mufradat)؛ كظم فلان حبس نفسه (mufradat)؛ قوم كظم أي ساكتون (sihah)
- **B003** devenin geviş lokmasını yutup gevişi kesmesi — devenin geviş lokmasını yutup gevişi kesmesi · geviş getirmeyi kesmiş deve · geviş getirmeyen dişi deve ya da develer
  الكظوم إمساك البعير عن الجرة (maqayis)؛ كظم البعير جرته إذا ازدردها وكف عنها (ayn;mufradat)؛ إذا أمسك عن الجرة فهو كاظم (sihah)؛ كظم البعير إذا لم يجتر (tahdhib)
- **B004** açıklığı kapatıp geçişi kesme — kapının kapatılması · kanalı tıkayıp akış yolunu kapatmak · dolu tulumun ağzını sıkıca bağlamak
  كظمت القناة سددتها (ayn)؛ الكظيم غلق الباب (sihah)؛ كظم السقاء شده بعد ملئه مانعا لنفسه (mufradat)
- **B005** kuyular ve aralarındaki su iletim yolu — yan yana kuyular ve aralarındaki su geçidi · kuyular arasında suyun aktığı kazılmış geçitlerden biri · kuyular arasında su taşıyan kazılmış geçitler
  الكظائم خروق تحفر يجرى فيها الماء من بئر إلى بئر (maqayis)؛ الكظيمة واحدة الكظائم وهي خروق تحفر فيجري فيها الماء (ayn)؛ الكظامة بئر إلى جنبها بئر وبينهما مجرى (sihah)؛ آبار تحفر ويخرق ما بين كل بئرين بقناة تؤدي الماء (tahdhib)؛ الكظائم خروق بين البئرين يجري فيها الماء (mufradat)
- **B006** uçları bir arada tutan bağlayıcı parça — terazi demirinin ucundaki ipleri toplayan halka · yayın üst ucunu kirişe bağlayan kayış · devenin burnunu bağlamaya yarayan ip · ok tüylerinin başlarını tutan sinir bağ
  الكظامة الحلقة التي تجمع خيوط حديدة الميزان (maqayis;sihah;mufradat)؛ الكظامة سير يوصل بوتر القوس العربية (maqayis;ayn;mufradat)؛ حبلا يكظم به خطم البعير (ayn)؛ الكظامة العقب الذي على رؤوس القذذ (sihah;tahdhib)
- **B007** deniz canlısınca yutulup içinde kapalı kalan kişi — büyük bir deniz canlısınca yutulup içinde kapalı kalan kişi
  المكظوم الذي يلتقمه الحوت (ayn)؛ كظم فلان حبس نفسه (mufradat)
- **B008** çölde ya da kıyıda bulunan belirli bir yer adı — çölde ya da deniz kıyısında bulunan belirli bir yer adı
  كاظمة موضع بالبادية (ayn)؛ كاظمة موضع (sihah)؛ كاظمة جو على سيف البحر وفيها ركايا كثيرة (tahdhib)
- **B009** işin güvenilir dayanağına tutunma [kalıp] — işin güvenilir dayanağına tutunup onu esas almak
  أخذت بكظام الأمر أي بالثقة (tahdhib)

## ن ش ء (root_001502): 43:18 يُنَشَّؤُا۟

- **B001** yükselmek veya yükseltmek — yükselmek, yukarı çıkmak · bulutun havada oluşup yükselmesi · Tanrı'nın bulutu yükseltmesi · yelkenleri kaldırılmış gemiler · yelkenlerini kaldıran gemiler · yükseltilmiş kum tepeleri
  أصل صحيح يدل على ارتفاع في شيء وسمو، ونشأ السحاب ارتفع، وأنشأه الله رفعه (maqayis)؛ أنشأ الله السحاب فنشأ أي ارتفع (ayn)؛ نشأت السحابة ارتفعت، والجوار المنشآت السفن التي رفع قلعها (sihah)؛ نشأ ارتفع، ونشأت السحابة ارتفعت، والمنشآت السفن المرفوعات الشرع (tahdhib)
- **B002** büyüyüp gençliğe erişmek — gençler, genç kuşak · çocukluk sınırını aşmaya yaklaşan gençler · çocukluğu geride bırakmış genç · büyüyüp gençliğe erişen kız · bir topluluk içinde büyüyüp yetişmek · süs içinde yetiştirilmek
  النشء والنشأ أحداث الناس، ونشأ فلان في بني فلان، والناشئ الشاب الذي نشأ وارتفع وعلا (maqayis)؛ النشأ أحداث الناس الصغار، والناشئ الشاب (ayn)؛ الناشئ الحدث الذي قد جاوز حد الصغر، ونشأت في بني فلان إذا شببت فيهم (sihah)؛ الناشئ الشاب حين نشأ أي بلغ قامة الرجل، وغلام ناشئ وجارية ناشئة (tahdhib)؛ أومن ينشأ في الحلية أي يربى (mufradat)
- **B003** gece içinde başlayan kalkış ya da zaman dilimi — Tanrı'ya yönelmek için geceleyin kalkıp ayakta durma · gecenin başı veya ilk saatleri · gecenin bütün saatleri veya gece içinde ortaya çıkanlar · uykudan sonraki gece bölümü
  ناشئة الليل يراد بها القيام والانتصاب للصلاة (maqayis;mufradat)؛ الناشئة أول الليل (ayn)؛ ناشئة الليل أول ساعاته أو ما ينشأ في الليل من الطاعات (sihah)؛ ناشئة الليل ساعاته كلها أو أوله أو ما كان بعد النوم أو متى قمت (tahdhib)
- **B004** bir işe ya da söze başlamak [kalıp] — bir işi yapmaya başlamak · bir konuşmaya başlamak · anlatılar kurup ortaya koymak · şiir söylemeye veya söylev vermeye başlamak ve bunu iyi yapmak
  أنشأ فلان حديثا وأنشأ ينشد ويقول (maqayis)؛ أنشأت حديثا ابتدأت (ayn)؛ أنشأ يفعل كذا أي ابتدأ، وفلان ينشئ الأحاديث أي يضعها (sihah)؛ أنشأ إذا أنشد شعرا أو خطب خطبة، وأنشأ فلان حديثا أي ابتدأ حديثا ورفعه (tahdhib)
- **B005** rüzgârı burnuna çekerek koklamak [kalıp] — rüzgârı burnuna çekerek koklamak
  استنشأت الريح تشممتها كأنك ترفعها إلى أنفك (maqayis)؛ الذئب يستنشئ الريح بالهمز، وإنما هو من نشيت الريح غير مهموز أي شممتها (sihah)
- **B006** var edip geliştirmek — Tanrı'nın bir şeyi yaratıp var etmesi · var oluş, meydana getirilme ve yetiştirilme · yaratma ve meydana getirme · bir şeyi var etme ve geliştirip yetiştirme · öteki yaşamı yaratıp var etme
  أنشأه الله خلقه، والاسم النشأة والنشاءة (sihah)؛ النشء والنشأة إحداث الشيء وتربيته، والإنشاء إيجاد الشيء وتربيته (mufradat)
- **B007** havuzun ilk ya da destekleyici taş bölümü — havuzun destek, başlangıç veya taban taşı
  نشيئة الحوض أعضاده إذا كان الحوض على وجه الأرض رفعت له نصائب الحجارة (ayn)؛ النشيئة أول ما يعمل من الحوض، وحجر يجعل أسفل الحوض (sihah)؛ النشيئة الحجر الذي يجعل أسفل الحوض، والنصائب ما نصب حوله (tahdhib)
- **B008** bir yere yönelip gelmek — yönelmek ya da bir yerden gelmek · nereden geldin · ihtiyacım için kalkıp ona doğru yürüdüm · işi için sabahleyin yola koyulmak · yaklaşıp uzaklaşan gemiler
  من أين أنشأت أي من أين جئت، وأنشأ فلان أقبل، وتنشأت إلى حاجتي نهضت إليها ومشيت، وتنشأ فلان غاديا إذا ذهب لحاجته، والمنشآت فهن اللائي يقبلن ويدبرن (tahdhib)
- **B009** dişi devenin gebe kalması [kalıp] — dişi devenin gebe kalması
  أنشأت الناقة فهي مبشئ إذا لقحت (tahdhib)

## ح ل ي (root_000353): 43:18 ٱلْحِلْيَةِ

- **B001** takı, süsleme parçası ve bunları takma — kadının taktığı ziynet eşyaları · takı veya nesneye eklenen süsleme parçası · kadın takılarını taktı · bileziklerle süslendi · takı takmış ve süslenmiş kadın
  الحلي حلى المرأة (maqayis)؛ الحلي كل حلية حليت به امرأة أو سيفا أو نحوه والجميع حلي (ayn)؛ الحلي جمع الحلي؛ يحلون فيها من أساور؛ وحلوا أساور؛ في الحلية (mufradat)
- **B002** nitelik ve yüzü betimleme — nitelik veya betimleyici özellik · bir erkeğin yüzünü betimleme
  هذه حلية الشيء أي صفته؛ حلية السيف (maqayis)؛ الحلية تحليتك وجه الرجل إذا وصفته (ayn)
- **B003** birinden iyilik görmek [kalıp] — birinden iyilik görmek
  حلي منه بخير يحلى حلى مقصور إذا أصاب خيرا (ayn)
- **B004** bir ot türünün kurusu ve ekin benzeri bitki — bir ot türünün kurusu ve ekine benzeyen bitki
  الحلي يبيس النصي وكل نبات يشبه نبات الزرع (ayn)

## خ ص م (root_000416): 43:18 ٱلْخِصَامِ, 43:58 خَصِمُونَ

- **B001** karşılıklı çekişme ve uyuşmazlık tarafı — çekişen taraf; uyuşmazlığın karşı tarafı · karşılıklı çekişme · onunla çekişti; ona karşı sav ileri sürdü · çekişen taraflar · çekişen kimse; çok çekişen kimse · karşılıklı çekişme ve savlaşma · birbirleriyle çekiştiler · çekişmede onu yendi · çok çekişen kimse · ona karşısındakine sunacağı savı öğretti
  المنازعة والخصم الذي يخاصم (maqayis)؛ خصيمك الذي يخاصمك والخصومة الاسم من التخاصم والاختصام (ayn;tahdhib)؛ خاصمته مخاصمة وخصاما (maqayis;ayn;sihah;tahdhib;mufradat)؛ الخصيم أيضا الخصم والخصم بكسر الصاد الشديد الخصومة (sihah)؛ الخصيم الكثير المخاصمة والخصم المختص بالخصومة (mufradat)؛ أخصمت فلانا إذا لقنته حجته على خصمه وخصمت فلانا غلبته فيما خاصمته فيه (tahdhib)
- **B002** yan, kenar veya çevresel bölüm — yük kabının yanı; nesnenin kenarı · her şeyin yanı ve çevresi · gözün kapaklarla çevrilen yanları · su kabının boşaltma ağzının karşısında kalan ucu · yastıkların, çuvalların ve döşeklerin köşeleri · yatağın yanı · bulutun yanları
  جانب وعاء وجانب العدل الذي فيه العروة (maqayis)؛ جانب كل شيء خصم وأخصام العين ما ضمت عليه الأشفار (maqayis;sihah)؛ طرف الراوية الذي بحيال العزلاء (ayn;tahdhib)؛ زوايا الوسائد والجواليق والفرش كلها أخصام (ayn)؛ خصم كل شيء جانبه وناحيته (sihah;tahdhib)؛ خصم الفراش أو خصم فراشي (tahdhib;mufradat)؛ خصوم السحابة جوانبها (tahdhib)
- **B003** kılıcın keskinliğiyle kınını aşındırması — kılıç keskinliğiyle kınını yiyip aşındırır
  السيف يختصم جفنه إذا أكله من حدته (sihah)

## غ ي ر (root_001119): 43:18 غَيْرُ

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

## م ل ك (root_001444): 43:19 ٱلْمَلَٰٓئِكَةَ, 43:51 مُلْكُ, 43:53 ٱلْمَلَٰٓئِكَةُ, 43:60 مَّلَٰٓئِكَةً, 43:77 يَٰمَٰلِكُ, 43:85 مُلْكُ, 43:86 يَمْلِكُ

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

## ء ن ث (root_000058): 43:19 إِنَٰثًا

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

## ش ه د (root_000822): 43:19 أَشَهِدُوا۟, 43:19 شَهَٰدَتُهُمْ, 43:86 شَهِدَ

- **B001** hazır bulunup görme — hazır bulunmak ve bizzat görmek · görerek hazır bulunma · bizzat görme ve gözle karşılaşma · insanların bulunduğu veya toplandığı yer · hac törenlerinin yapıldığı yerler · eşi yanında bulunan kadın
  أصل يدل على حضور (maqayis)؛ شهده شهودا أي حضره (sihah)؛ الشهود والشهادة الحضور مع المشاهدة (mufradat)؛ المشهد مجمع الناس (ayn;tahdhib)؛ امرأة مشهد إذا حضر زوجها (maqayis;sihah;mufradat;tahdhib)
- **B002** bilgiye dayalı tanıklık — bilgiye dayalı kesin tanıklık sözü · bildiğini tanık olarak açıklamak · tanıklık eden kişi · tanık olan veya başkası hakkında tanıklık eden kişi · birinden tanıklık etmesini istemek · birini bir konuda tanık kılmak · ilahi nitelik olarak güvenilir tanık veya bilgisine hiçbir şey uzak kalmayan
  الشهادة يجمع الحضور والعلم والإعلام (maqayis)؛ الشهادة خبر قاطع (sihah)؛ شهد فلان بحق فهو شاهد وشهيد (tahdhib)؛ الشهادة قول صادر عن علم (mufradat)؛ شهد علي فلان بكذا شهادة وهو شاهد وشهيد (ayn)
- **B003** tanıklık bildirme sözü — tanıklık sözüyle yemin etmek veya bildirmek · namazda okunan tanıklık ve selamlama bölümü
  التشهد في الصلاة من قولك أشهد (ayn)؛ قولهم أشهد بكذا أي احلف (sihah)؛ أشهد أن لا إله إلا الله وأبين (tahdhib)؛ التشهد هو أن يقول أشهد أن لا إله إلا الله (mufradat)
- **B004** Tanrı yolunda öldürülen kişi — Tanrı yolunda öldürülen veya ölüm anında bulunan kişi · bu özel ölüm statüsüyle ölmek
  الشهيد القتيل في سبيل الله (maqayis;sihah)؛ استشهد فلان فهو شهيد (ayn;sihah;tahdhib)؛ الشهيد هو المحتضر (mufradat)؛ الشهيد الحي (tahdhib)
- **B005** ifade eden dil — dil veya sahibini belli eden ifade · ne görünüşü ne de dili var
  الشاهد اللسان (maqayis;sihah;tahdhib)؛ ما لفلان رواء ولا شاهد أي ماله منظر ولا لسان (tahdhib)؛ لفلان شاهد حسن أي عبارة جميلة (tahdhib)
- **B006** doğum ve erginlik belirtisi — doğumda çocuğun başıyla ya da çocukla birlikte çıkan şey · devenin doğurduğu yerde kalan kan veya zar izi · erkek çocuğun salgıyla, kız çocuğun adetle erginleşmesi · meni öncesi salgı çıkarmak
  الشهود ما يخرج على رأس الصبي (maqayis;ayn;tahdhib)؛ الشاهد الذي يخرج مع الولد (sihah)؛ شهود الناقة آثار موضع منتجها من دم أو سلى (maqayis;sihah)؛ أشهد الغلام إذا أمذى وأدرك وأشهدت الجارية إذا حاضت وأدركت (tahdhib)
- **B007** petekli bal — petek içindeki süzülmemiş bal · petekli baldan bir parça · petekli ballar
  الشَّهْد العسل في شمعها (maqayis;sihah)؛ الشهد العسل ما لم يعصر من شمعه (ayn;tahdhib)؛ الواحدة شهدة وشهدة والجمع شهاد (ayn;sihah;tahdhib)
- **B008** durumu gösteren belirti — geceye işaret eden yıldız · akşam namazı için kullanılan ad · atın üstünlüğünü ve iyi koştuğunu gösteren koşu
  الشاهد النجم (tahdhib)؛ صلاة الشاهد صلاة المغرب (tahdhib)؛ الشاهد من جريه ما يشهد له على سبقه وجودته (tahdhib)

## ش ي ء (root_000831): 43:20 شَآءَ, 43:60 نَشَآءُ

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

## ش ي ء (root_000832): 43:20 شَآءَ, 43:60 نَشَآءُ

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

## خ ر ص (root_000403): 43:20 يَخْرُصُونَ

- **B001** sezgiye dayalı miktar kestirimi — kesin bilgi olmadan tahminle ölçüp biçme · hurma veya bağ ürününün miktarını tahminen belirlemek · meyve miktarını ve buna göre alınacak payı kestiren kişi · bir işi sezgisel değerlendirmeyle açıklığa kavuşturmak · kavrayışlı ve bilgili kişi
  الخرص الحزر في العدد والكيل (ayn)؛ الخرص حزر ما على النخل من الرطب تمرا (sihah)؛ أصل الخرص التظني فيما لا يستيقنه (tahdhib)؛ كل قول مقول عن ظن وتخمين يقال خرص (mufradat)؛ الخرص وهو حزر الشيء (maqayis)؛ من خرص الشيء إذا قدره بفطنته وذكائه (maqayis)
- **B002** bilmeden yalan söyleme — yalan ve bilgisizce söylenen söz · bilmeden konuşan yalancılar · yalan söylemek ve doğrulanmamış söz ileri sürmek · asılsız bir sözü uydurup ortaya atmak
  الخرص الكذب والخراصون الكذابون (ayn)؛ الخراص الكذاب وتخرص أي كذب (sihah)؛ تخرص فلان علي الباطل واخترصه أي اختلقه وافتعله (tahdhib)؛ لعن الكذابون (mufradat)؛ الخراص الكذاب وهو من هذا لأنه يقول ما لا يعلم ولا يحق (maqayis)
- **B003** küçük takı halkası — küçük takı halkası veya halka küpe · halkalar; halkalı yapısından ötürü zırhlar · yaradan kalan küçük halka benzeri iz · boncuklardan yapılmış bir süs
  الخرص القرط بحبة واحدة في حلقة واحدة (ayn)؛ الخرص الحلقة من الذهب والفضة (sihah)؛ الخرص الحلقة الصغيرة من الحلي كحلقة القرط ونحوها (tahdhib)؛ الحلقة من الذهب خرص (maqayis)؛ لأن الخرص الحلقة (maqayis)
- **B004** yan havza, kıyı, koy veya ada — nehre veya denize bağlı yan havza, kıyı ya da koy
  الخريص شبه حوض واسع ينبثق فيه الماء من نهر ثم يعود إلى النهر والخريص ممتلي (ayn)؛ الخريص السنان وماء خريص (sihah)؛ خريص النهر جانبه والخريص الخليج من البحر والخريص جزيرة البحر (tahdhib)؛ كل ذي شعبة من الشيء ذي الشعب فالخريص من البحر الخليج منه (maqayis)
- **B005** soğukla birlikte açlık çekme — açlıkla birlikte soğuk çekmek · açlık ve soğuğa uğramış develer
  الخرص الذي به جوع وبرد (ayn)؛ خرص الرجل فهو خرص أي جائع مقرور ولا يقال للجوع بلا برد خرص ولا يقال للبرد بلا جوع خصر (sihah)؛ إبل خرصة وخرصات إذا أصابها برد وجوع (tahdhib)؛ الخرص صفة الجائع المقرور (maqayis)
- **B006** soğuk su [kalıp] — soğuk su
  ماء خريص مثل خصر أي بارد (sihah)
- **B007** ince çubuk, kısa mızrak veya mızrak ucu — ince çubuk, kısa mızrak veya mızrak ucu · mızrağın sivri ucu · mızrak uçları · bal toplayıcısının kullandığı çubuklar · su tulumunun düğümüne saplanan sivri küçük çubuk · en küçük bir şeye bile sahip olmamak · ince ve kısa mızraklar, mızrak uçları veya çubuklar
  الخرص من الرماح رمح قصير ويقال لدقاق القناة وقصارها خرصان والخرص العود (ayn)؛ الخرص ما علا الجبة من السنان وربما سمى الرمح بذلك والخرص الجريد والخرص عويد محدد الرأس (sihah)؛ الخرص السنان وجمعه خرصان والخرص الرمح اللطيف (tahdhib)؛ الخرص كل قضيب من شجرة ومن هذا الأصل تسميتهم الرمح الخرص ومنه الأخراص وهي عيدان (maqayis)
- **B008** istediğini torbaya koyma — istediği şeyi torbaya koymak
  هو يخترص أي يجعل في الخرص ما يريد وهو الجراب (tahdhib)

## ق ب ل (root_001198): 43:21 قَبْلِهِۦ, 43:23 قَبْلِكَ, 43:45 قَبْلِكَ

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

## م س ك (root_001424): 43:21 مُسْتَمْسِكُونَ, 43:43 فَٱسْتَمْسِكْ

- **B001** tutup alıkoymak veya sıkıca bağlanmak — bir şeyi tutmak, korumak veya alıkoymak · bir şeye sıkıca tutunmak ve onu dayanak edinmek · konuşmaktan kaçınıp susmak · bir şeyi ondan esirgemek veya ona vermemek · kendini tutmak veya sağlam durmak · onunla kokulan veya onu elinde tut · bir sözü birinin aleyhine kanıt olarak kullanmak · kitaba inanıp hükümlerine uymak
  حبس الشيء أو تحبسه (maqayis)؛ مسكت بالشيء وتمسكت به واستمسكت به (ayn)؛ أمسكت الشيء وتمسكت به واستمسكت به كله بمعنى اعتصمت به (sihah)؛ التمسك استمساكك بالشيء (tahdhib)؛ إمساك الشيء التعلق به وحفظه (mufradat)
- **B002** elindekini vermeyen cimrilik — elindekini vermeyen cimri · cimri adam · cimrilik ve eli sıkılık · cimri veya tuttuğunu bırakmayan adam
  البخيل ممسك والإمساك البخل والمسيك البخيل (maqayis)؛ في فلان إمساك ومساك ومسكة كله من البخل (ayn)؛ المسيك البخيل وفيه إمساك ومساك ومساكة أي بخل (sihah)؛ كل ذلك من البخل والتمسك بما لديه ضنا به (tahdhib)؛ كني عن البخل بالإمساك (mufradat)
- **B003** yaşamı sürdüren az miktar veya kalan pay [kalıp] — canı sürdürecek kadar yiyecek veya içecek · iyilik, güç veya akıldan kalan küçük pay
  المسكة ما يمسك الرمق من طعام أو شراب (ayn)؛ فيه مسكة من خير أي بقية (sihah)؛ المسكة من الطعام والشراب ما يمسك الرمق (tahdhib)؛ ما بفلان مسكة أي ما به قوة ولا عقل (tahdhib)؛ المسكة من الطعام والشراب ما يمسك الرمق (mufradat)
- **B004** suyu emmeden veya sızdırmadan tutan yer ya da kap [kalıp] — suyu emmeden tutan yer veya toprak · kuyunun örülmesi gerekmeyen sert kesimi · suyu sızdırmadan tutan su kabı · suyu emmeyen sert toprak
  المسكة من البئر المكان الصلب الذي لا يحتاج إلى طي (maqayis)؛ المساك من الأرض ما يمسك الماء (ayn)؛ سقاء مسيك كثير الأخذ (ayn)؛ المساك المكان الذي يمسك الماء (sihah)؛ قد بلغوا مسكة صلبة (tahdhib)؛ أرض مسيكة لا تنشف الماء (tahdhib)؛ التناهي التي تمسك ماء السماء مساك ومساكة (tahdhib)؛ المسيك من الأساقي الذي يحبس الماء فلا ينضح (tahdhib)
- **B005** gövdeyi veya kap içeriğini saran deri ve post — gövdeyi veya içindekini saran deri ve post · tilki postları
  المسك الإهاب لأنه يمسك فيه الشيء إذا جعل سقاء (maqayis)؛ المسك الإهاب (ayn)؛ المسك بالفتح الجلد (sihah)؛ المسك الجلد (tahdhib)؛ من مسك فرس ذبح (tahdhib)؛ الجلد الممسك للبدن (mufradat)
- **B006** boynuz veya fildişinden bilezik — boynuz veya fildişinden yapılmış bilezik
  المسك السوار من الذبل (maqayis)؛ المسك الذبل الواحدة مسكة (ayn)؛ أسورة من ذبل أو عاج (sihah)؛ مثل الأسورة من قرون أو عاج (tahdhib)؛ الذبل المشدود على المعصم (mufradat)
- **B007** kokulanmada kullanılan belirli yoğun koku maddesi — kokulanmada kullanılan yoğun koku maddesi · bu koku maddesiyle boyanmış kumaş · onunla kokulan veya onu elinde tut
  مما شذ عنه المسك من الطيب (maqayis)؛ المسك معروف ليس بعربي محض (ayn)؛ المسك من الطيب فارسي معرب (sihah)؛ المسك معروف إلا أنه ليس بعربي محض (tahdhib)؛ تمسكي أي تطيبي من المسك (tahdhib)
- **B008** ateşi oyukta yakıtla veya toprağa gömerek korumak [kalıp] — ateşi yakıtla örterek veya toprağa gömerek korumak
  مسكت بالنار تمسيكا وثقبت بها تثقيبا إذا فحصت لها في الأرض ثم جعلت عليها بعرا أو خشبا أو دفنتها في التراب
- **B009** insanları bağlayan sıkı akrabalık ilişkisi [kalıp] — insanları birbirine bağlayan sıkı akrabalık
  بيننا ماسكة رحم كقولك ماسة رحم وواشجة رحم
- **B010** yenidoğanın baş ve el uçlarındaki özel deri — yenidoğanın başında ve el uçlarında bulunan özel deri
  الماسكة الجلدة التي تكون على رأس الولد وعلى أطراف يديه
- **B011** at bacaklarının beyazlık dağılımını karşıt biçimde niteleme — sağ ve sol bacakları beyazlık dağılımına göre karşıt nitelenen at
  هو ممسك الأيامن مطلق الأياسر؛ كل قائمة بها بياض فهي ممسكة؛ جانب أمسك لا بياض
- **B012** düşmanına diken gibi takılan cesur kişi — düşmanına diken gibi takılan cesur kişi
  فلان حسكة مسكة أي شجاع كأنه حسك في حلق عدوه
- **B013** alışveriş için önceden verilen para — alışveriş için önceden verilen para
  المسكان العربان ويجمع مساكين يقال أعطه المسكان

## و ج د (root_001626): 43:22 وَجَدْنَآ, 43:23 وَجَدْنَآ, 43:24 وَجَدتُّمْ

- **B001** bulma ve duyusal ya da zihinsel olarak algılama — bir şeyi bulmak veya ona erişmek · yitiği bulmak · bulma ve erişme · birini aradığı şeye ulaştırmak · duyularla veya akılla algılama · onları gördüğünüz veya kendilerine eriştiğiniz yerde
  الشيء يلفيه (maqayis)؛ وجدت الضالة وجدانا (maqayis;sihah)؛ الوجدان والجدة من قولك وجدت الشيء أي أصبته (ayn)؛ وجدت الشيء أجده وجدانا (jamhara)؛ وجد مطلوبه يجده وجودا (sihah)؛ الوجود أضرب: وجود بإحدى الحواس الخمس ... ووجود بالعقل (mufradat)؛ حيث وجدتموهم أي حيث رأيتموهم (mufradat)
- **B002** varlığa gelme, var olma ve var etme — yokluktan sonra varlığa gelmek · var olan, mevcut · Tanrı onu var etti · var olan şeyler
  وجد الشيء عن عدم فهو موجود (sihah)؛ أوجده الله (sihah)؛ الموجودات ثلاثة أضرب (mufradat)
- **B003** varlıklı veya yeterli olmak; varlıklı ya da güçlü kılmak — maddi genişlik ve varlıklılık · malca genişleyip varlıklı olmak · varlıklı ve ödeme gücü bulunan kimse · onu varlıklı kılmak · onu zayıflıktan sonra güçlendirmek · imkanınız ve maddi gücünüz ölçüsünde · suya ulaşmaya gücünüz yetmediyse
  الوجدان والجدة من قولك وجدت الشيء أي أصبته (ayn)؛ وجدت في المال جدة ووجدا ووجدا؛ الواجد الغني (jamhara)؛ وجد في المال وجدا ووجدا وجدة أي استغنى؛ أوجده أي أغناه؛ آجدني بعد ضعف أي قواني (sihah)؛ يعبر عن التمكن من الشيء بالوجود؛ من وجدكم أي تمكنكم وقدر غناكم (mufradat)
- **B004** üzüntü veya sevgi duymak; güçlü isteğin doyumunu yaşamak — üzüntü ve keder · sevgi ve duygusal bağlılık · ona sevgi duymak · üzüntü duymak · bir kimse için üzülmek · güçlü iştahla doyuma erişmek
  الوجد من الخزن (ayn)؛ الوجد: الحب؛ وجدت به أجد وجدا (jamhara)؛ وجد في الحزن وجدا؛ توجدت لفلان أي حزنت له (sihah)؛ وجود بقوة الشهوة؛ يعبر عن الحزن والحب بالوجد (mufradat)
- **B005** öfke duymak ve birine kızmak — öfke ve kızgınlık · öfkeye kapılmak · o kişiye kızmak · öfke bağlamındaki kızgınlık duygusu
  وجدت في الغضب وجدانا (maqayis)؛ الموجدة من الغضب (ayn)؛ وجدت على الرجل موجدة (jamhara)؛ وجد عليه في الغضب موجدة ووجدانا (sihah)؛ يعبر عن الغضب بالموجدة (mufradat)

## ECHO ج د د (root_000227): for 43:22 وَجَدْنَآ, 43:23 وَجَدْنَآ, 43:24 وَجَدتُّمْ: withheld observed target; not identity

- **B001** değer ve konum yüceliği — büyüklük, yücelik ve yüksek değer
  العظمة (maqayis)؛ جد ربنا عظمته (ayn)؛ تعالى جد ربنا أي عظمة ربنا؛ جد في عيني أي عظم (sihah)؛ جد ربنا جلال ربنا؛ جل قدره وعظم (tahdhib)؛ جد ربنا أي فيضه وقيل عظمته (mufradat)
- **B002** iyi yazgı ve varlık payı — iyi yazgı, dünyalık pay ve varlık · iyi yazgı veya varlık sahibi
  الغني والحظ؛ لا ينفع ذا الجد منك الجد (maqayis)؛ جد الرجل بخته (ayn)؛ الجد الحظ والبخت؛ لا ينفع ذا الجد منك الجد أي لا ينفع ذا الغنى (sihah)؛ الجد الغنى والحظ في الرزق؛ صاعد الجد؛ رجل جديد إذا كان ذا حظ (tahdhib)؛ الحظوظ الدنيوية جدا وهو البخت (mufradat)
- **B003** kesme ve ayırma — bir şeyi kesmek · kesilmiş · hurma ağaçlarının ürününü kesip toplamak · hurma ürününü kesip toplama ve bunun vakti · dişi devenin meme uçlarını bağ yüzünden kesip zedelemek · birine annesinden kopması için ilenmek · kulağı kesik koyun · ekildiğinde yüz ölçek ürün veren tarla
  جددت الشيء جدا وهو مجدود وجديد أي مقطوع؛ الجداد صرام النخل (maqayis)؛ جداد النخل صرامه؛ جد ثدي أمك اذدعي عليه بالقطيعة (ayn)؛ جددت الشيء أجده جدا قطعته؛ جد النخل أي صرمه؛ جدت أخلاف الناقة (sihah)؛ جد التمرة؛ الجداد الصرام؛ أصل الجد القطع؛ جد ثدي أمه (tahdhib)؛ جددت الثوب إذا قطعته؛ جد ثدي أمه على طريق الشتم (mufradat)
- **B004** yeni olma ve yenilenme — yeni, eskimemiş veya yenilenmiş · gece ile gündüz · yenilik ve yeni olma
  ثوب جديد؛ سمي كل شيء لم تأت عليه الأيام جديدا؛ الليل والنهار الجديدين والأجدين (maqayis)؛ الجدة مصدر الجديد؛ الجديدان الليل والنهار (ayn)؛ صار جديدا؛ تجدد الشيء صار جديدا؛ الجديدان والأجدان الليل والنهار (sihah)؛ ثوب جديد جد حديثا أي قطع؛ الجدة مصدر الجديد؛ الجديدان والأجدان الليل والنهار (tahdhib)؛ ثوب جديد أصله المقطوع؛ جعل لكل ما أحدث إنشاؤه؛ الجديدان والأجدان (mufradat)
- **B005** belirgin şerit veya ana yol — çevresinden ayrılan yol veya çizgi · dağlardaki farklı renkli şeritler · yolun ortası veya en çok kullanılan ana bölümü · farklı çizgiler taşıyan dokuma
  كل جدة طريقة؛ جادة الطريق سواؤه (maqayis)؛ الجدد والجديد وجه الأرض؛ الزم الطريق الجدد؛ الجادة الطريق (ayn)؛ الجدة الخطة؛ كل خط جدة؛ جدد بيض أي طرائق تخالف لون الجبل (jamhara)؛ الجدة الطريقة؛ جادة الطريق؛ كساء مجدد فيه خطوط مختلفة (sihah)؛ الجدد الخطط والطرق تكون في الجبال؛ كل طريقة جدة وجادة؛ كساء مجدد فيه خيوط مختلفة (tahdhib)؛ جدد بيض جمع جدة أي طريقة ظاهرة؛ جادة الطريق (mufradat)
- **B006** su kıyısı — ırmak veya dere yatağı kıyısı · deniz kıyısı; ayrıca kıyıdaki belirli yer
  جدة النهر أي ما قرب من الأرض؛ الجدة ساحل البحر بمكة (ayn)؛ جدة النهر حافته وكذلك الوادي (jamhara)؛ جدة بلد على الساحل (sihah)؛ الجدة شاطىء النهر؛ الجدة ساحل البحر بحذاء مكة (tahdhib)
- **B007** düz ve sert yer yüzeyi — düz veya sert yer · düz ve pürüzsüz yer · yerin yüzü · tümseksiz ve geçişi kolay düz yol
  الجدجد الأرض المستوية؛ الجدد مثل الجدجد؛ الجديد وجه الأرض (maqayis)؛ الجدد والجديد وجه الأرض؛ الجدجد الفيف الأملس (ayn)؛ الجدد الأرض الصلبة؛ الجدجد الأرض الصلبة المستوية (sihah)؛ الأرض المستوية التي ليس فيها رمل ولا اختلاف جدد؛ جديد الأرض وجهها (tahdhib)؛ قطع الأرض المستوية؛ طريق مجدود (mufradat)
- **B008** şakadan uzak kararlı çaba — şaka olmayan gerçek ve kararlı tutum · bir işe var gücüyle sarılıp kararlılıkla uğraşmak · bir işte bütün gücünü ortaya koymak · gerçekten mi, kesin kararın bu mu · işine var gücüyle sarılan kimse · bir işte haklılık çekişmesine girmek
  الجد في الأمر والمبالغة فيه؛ أجدك تفعل كذا أي أجدا منك أصريمة منك أعزيمة منك (maqayis)؛ الجد نقيض الهزل؛ جد فلان في أمره وسيره (ayn)؛ الجد نقيض الهزل؛ الجد الاجتهاد في الأمور؛ جاد مجد (sihah)؛ الجد إنما هو الاجتهاد في العمل؛ أجد الرجل في أمره؛ جاد مجد؛ جد فلان في أمره إذا كان ذا حقيقة ومضاء (tahdhib)؛ جد في سيره؛ جد في أمره (mufradat)
- **B009** büyükanne ve büyükbaba — anne veya baba tarafından büyükbaba · anne veya baba tarafından büyükanne
  الجد أبو الأب وأبو الأم (sihah)؛ الجد أب الأب؛ أم الأم وأم الأب يقال لها جدة (tahdhib)؛ الجد أبو الأب وأبو الأم (mufradat)
- **B010** otlak kuyusu — bol ot bulunan yerdeki kuyu
  الجد البئر؛ البئر تقطع لها الأرض قطعا (maqayis)؛ الجد البئر تكون في موضع الكلأ (ayn)؛ الجد بالضم البئر التي تكون في موضع كثير الكلا (sihah)؛ الجد بلا هاء البئر الجيدة الموضع من الكلأ (tahdhib)
- **B011** susuz yer veya sütü kesilmiş dişi hayvan — susuz ve kuru kır · sütü azalmış veya kesilmiş dişi hayvan · sütü kesilmiş, memesi kurumuş dişi hayvan
  الجداء الأرض التي لا ماء بها؛ الجدود والجداء من الضان التي جف لبنها ويبس ضرعها (maqayis)؛ الجدود كل أنثى يبس لبنها؛ الجداء مفازة يابسة؛ شاة جداء يابسة اللبن (ayn)؛ فلاة جداء لا ماء بها؛ الجدود النعجة التي قل لبنها؛ الجداء التي ذهب لبنها (sihah)؛ ناقة جدود؛ نعجة جدود؛ الجداء الناقة التي قد انقطع لبنها (tahdhib)؛ الجدود والجداء من الضأن التي انقطع لبنها (mufradat)
- **B012** düğümlü ipler ve dolaşık kalıntılar — çadır ipleri; dolaşmış ip ve dallar; eskimiş kumaş parçaları
  جدادها الخيوط التي تعقد بالخيمة؛ جداد الخيمة الخيوط؛ الجداد صغار الشجر (maqayis)؛ الجداد الخلقان من الثياب؛ كل شيء تعقد بعضه في بعض من الخيوط وأغصان الشجر فهو جداد (sihah)؛ الجداد خيوط المظلة؛ الجداد بالنبطية الخيوط المعقدة (tahdhib)
- **B013** cırcır böceği — cırcır böceği
  الجدجد دويبة على خلقة الجندب (ayn)؛ الجدجد صرار الليل وفيه شبه من الجراد (sihah)
- **B014** kıyı ve kır yer adları — kıyıda bulunan bir yerin adı · çölde veya su bulunan yerdeki bir yerin adı
  جدة موضع؛ جدود موضع بالبادية (ayn)؛ جدة بلد على الساحل؛ جدود موضع فيه ماء (sihah)

## ء ب و (root_000007): 43:22 ءَابَآءَنَا, 43:23 ءَابَآءَنَا, 43:24 ءَابَآءَكُمْ, 43:26 لِأَبِيهِ, 43:29 وَءَابَآءَهُمْ

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ء ث ر (root_000011): 43:22 ءَاثَٰرِهِم, 43:23 ءَاثَٰرِهِم

- **B001** en başa almak; yapmaya kesin karar vermek [kalıp] — her şeyden önce · ilk iş olarak · yapmaya kesin karar verdi
  له أصل تقديم الشيء (maqayis)؛ آثرا ما وآثر ذي أثير أي أول كل شيء (maqayis;sihah;tahdhib)؛ إن آثرت أن تأتينا فأتنا وقد أثر أن يفعل ذلك الأمر أي فرغ له وعزم عليه (tahdhib)؛ خذه آثرا ما وإثرا ما وأثر ذي أثير (mufradat)
- **B002** aktarılıp kalıcılaşan anlatı veya bilgi — sözü başkasından aktardı · kuşaktan kuşağa aktarılan söz · anlatılagelen değerli işler · aktarılmış veya yazıya geçirilmiş bilgi
  من قولك أثرت الحديث وحديث مأثور (maqayis)؛ أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور (sihah)؛ حديث مأثور أي يخبر الناس به بعضهم بعضا (tahdhib)؛ أثرت العلم رويته وآثره أثرا وأثارة وأثرة (mufradat)؛ المآثر ما يروى من مكارم الإنسان (mufradat;tahdhib)
- **B003** geride kalan belirti veya iz — geride kalan iz · yara izi · bilgiden kalma bir parça veya belirti
  الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة (maqayis)؛ الأثر بالتحريك ما بقي من رسم الشيء (sihah)؛ أثر الشيء حصول ما يدل على وجوده (mufradat)؛ أثارة من علم بقية من علم وعلامة (tahdhib)؛ الأثر من الجرح وغيره في الجسد يبرأ ويبقى أثره (sihah;tahdhib)
- **B004** izinden giderek takip etmek — ardından, izinden giderek · öncekinin geçtiğini gösteren yol
  الأثر الاستقفاء والاتباع وذهبت في إثره (maqayis)؛ خرجت في إثره أي في أثره (sihah)؛ جاء فلان على إثري وأثري وجاء في أثره وإثره (tahdhib)؛ الطريق المستدل به على من تقدم آثار وهم أولاء على أثري (mufradat)
- **B005** üstün tutmak ve gözde saymak — başkasını veya bir şeyi üstün tutma · özel yakınlık gören gözde kişi
  الأثير الكريم عليك الذي تؤثره بفضلك وصلتك (maqayis)؛ آثرت فلانا على نفسي من الإيثار (sihah)؛ آثرتك إيثارا أي فضلتك وآثرك الله علينا (tahdhib)؛ الإيثار للتفضل ويؤثرون على أنفسهم وتالله لقد آثرك الله علينا (mufradat)
- **B006** başkalarını dışlayarak kendine ayırmak — bir şeyi yalnız kendine ayırma · başkaları dışlanarak sağlanan ayrıcalık · ortaklarına karşı her şeyi kendine ayıran kişi
  استأثر الله بفلان واستأثرت عليك ورجل أثر يستأثر على أصحابه وستَرون بعدي أثرة (maqayis)؛ استأثر فلان بالشيء أي استبد به والاسم الأثرة (sihah)؛ رجل أثر وهو الذي يستأثر على أصحابه وإنكم ستلقون بعدي أثرة واستأثر الله بالبقاء أي انفرد بالبقاء (tahdhib)؛ الاستئثار التفرد بالشيء من دون غيره وسيكون بعدي أثرة (mufradat)
- **B007** kılıcın yüzey deseni, parlaklığı veya darbesi — kılıcın yüzey deseni, parlaklığı veya darbesi · yüzeyinde özel bir iz bulunan ya da insanüstü varlıkların yaptığı söylenen kılıç
  أثر السيف ضربته والأثر في السيف الفرند ويسمى السيف مأثورا (maqayis)؛ الأثر فرند السيف والمأثور السيف (sihah)؛ أثر السيف فرنده وأثر السيف ضربته وأثره مفتوح رونقه (tahdhib)؛ أثر السيف جوهره وأثر جودته وهو الفرند وسيف مأثور (mufradat)
- **B008** deve ayağını iz bırakacak biçimde işaretleme ve işaretleme demiri — deve ayağı işaretleme demiri · devenin ayağına yerde iz bırakacak işaret koydu
  الآثر الذي يؤثر خف البعير والمئثرة حديدة يؤثر بها في باطن فرسن البعير (maqayis)؛ الأثرة أن يسحى باطن خف البعير بحديدة وتلك الحديدة مئثرة (sihah)؛ المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض (tahdhib)؛ أثرت البعير جعلت على خفه أثرة أي علامة تؤثر في الأرض (mufradat)
- **B009** eski yağ kalıntısı, yağ özü veya arınmış süt — devede önceden kalma yağ · yağ özü veya tereyağından ayrılarak arınmış süt
  الإبل على أثارة أي على شحم قديم وإذا تخلص اللبن من الزبد وخلص فهو الأثر (maqayis)؛ الأثر بالكسر خلاصة السمن وسمنت الإبل على أثارة أي بقية شحم (sihah)؛ الأثر خلاصة السمن والإثر بكسر الهمزة خلاصة السمن وسمنت الناقة على أثارة (tahdhib)؛ سمنت الإبل على أثارة أي على أثر من شحم (mufradat)
- **B010** ömrün sonu veya kişinin ardından kalan işler — ömrün belirlenmiş sonu · kişinin ardından kalan işler ve uygulamalar
  ينسأ في أثره أي في أجله وسمي الأجل أثرا لأنه يتبع العمر (tahdhib)؛ ونكتب ما قدموه من الأعمال وسنوه من سنن يعمل بها (tahdhib)
- **B011** alışarak kavrayıp ustalaşmak [kalıp] — konuyu iyice kavrayıp ustalaştı
  أثر فلان يقول كذا وطبن وطبق ودبق ولفق وفطن وذلك إذا أبصر الشيء وضري بمعرفته وحذقه (tahdhib)
- **B012** keçi memesi koruyucu torbası — keçinin memesine bağlanan koruyucu torba
  الإثار شبه الشمال يشد على ضرع العنز شبه كيس لئلا تعان (tahdhib)

## ECHO ث و ر (root_000210): for 43:22 ءَاثَٰرِهِم, 43:23 ءَاثَٰرِهِم: withheld observed target; not identity

- **B001** gizlilikten çıkıp belirerek yayılma — durgunluktan çıkıp belirmek ve yayılmak · tozun veya bulutun yükselip yayılması · hastalık döküntüsünün ortaya çıkıp yayılması · böcek sürüsünün saklandığı yerden çıkıp sıçrayarak yayılması · alacakaranlığın yayılması veya en yoğun bölümünün görünmesi · içi kalkmak · saçı dağılıp kabarmış
  أصل انبعاث الشيء (maqayis)؛ ثار الغبار والسحاب ونحوهما انتشر ساطعا (mufradat)؛ ثار الغبار يثور ثورا وثورانا أي سطع (sihah)؛ ثارت الحصبة... وثار الجراد... وثار الماء... وثار الغبار وغيره كذلك (jamhara)
- **B002** yerinden kaldırıp harekete geçirme — bir şeyi yerinden oynatıp harekete geçirmek · toprağı eşeleyip kaldırmak · erkek sığırın toprağı ayaklarıyla eşeleyip kaldırması · tavşanı ürkütüp saklandığı yerden çıkarmak · Kur'an bilgisini derinlemesine araştırıp ortaya çıkarmak · rahatsız edip yerinden kaldırmak
  أثرت الأرض إثارة (jamhara)؛ أثار الثور التراب إذا بحثه بقوائمه (jamhara)؛ وأثاره غيره (sihah)؛ وثور القرآن أي بحث عن علمه (sihah)؛ فتثير سحابا... وأثاروا الأرض (mufradat)
- **B003** saldırgan biçimde kabarıp karşı koyma — birinin üzerine atılıp saldırmak · halkın birinin üzerine ayaklanması · kötülüğü kışkırtıp onlara karşı ortaya çıkarmak · öfkesi kabarıp dışa vurulmak · taşkınlık ve kargaşa
  ثاور فلان فلانا إذا واثبه (maqayis;jamhara)؛ ثار به الناس أي وثبوا عليه (sihah)؛ المثاورة المواثبة (sihah)؛ انتظر حتى تسكن هذه الثورة وهي الهيج (sihah)؛ ثور فلان عليهم الشرا أي هيجه وأظهره (sihah)؛ ثار ثائره كناية عن انتشار غضبه (mufradat)
- **B004** erkek sığır — yabani veya evcil erkek sığır · dişi sığır · erkek sığırlar · sığırların sudan kaçınması üzerine söylenen, hayvan ya da yosun diye yorumlanan örnek söz
  جنس من الحيوان (maqayis)؛ والثور ذكر البقر الوحشية والأهلية (jamhara)؛ والثور الذكر من البقر والأنثى ثورة (sihah)؛ والثور البقر الذي يثار به الأرض (mufradat)
- **B005** kurutulmuş çökelek parçası — kurutulmuş çökelekten bir parça, özellikle iri bir parça
  الثور فالقطعة من الأقط (maqayis)؛ والثور القطعة العظيمة من الأقط والجمع أثوار وثورة (jamhara)؛ والثور قطعة من الأقط والجمع ثورة (sihah)
- **B006** dağ, topluluk veya burç için özel ad — belirli bir dağın adı · belirli bir boyun veya kabilenin adı · gökteki belirli bir burcun adı
  وثور جبل وثور قوم من العرب وهذا على التشبيه (maqayis)؛ والثور جبل معروف يسمى ثور أطحل وبنو ثور بطن من الرباب (jamhara)؛ وثور أبو قبيلة من مضر وثور جبل بمكة... والثور برج من السماء (sihah)
- **B007** su yüzeyini kaplayan yosun — su yüzeyine çıkıp tabaka oluşturan yosun · sığırların sudan kaçınması üzerine söylenen, hayvan ya da yosun diye yorumlanan örnek söz
  الثور فيمن يقول إنه الطحلب... ثار على متن الماء (maqayis)؛ يقال للطحلب ثور الماء (sihah)

## ق ر ي (root_001222): 43:23 قَرْيَةٍ, 43:31 ٱلْقَرْيَتَيْنِ

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

## ن ذ ر (root_001488): 43:23 نَّذِيرٍ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ت ر ف (root_000179): 43:23 مُتْرَفُوهَآ

- **B001** bolluk içinde yaşatılarak şımartılma ve serbest bırakılma — bolluk, geniş ve rahat yaşayış · bolluk içinde yaşayan, rahatına düşkün ve şımartılmış kimse · bolluk içinde yaşamak veya yaşatılmak · bolluk onu azdırdı ve küstahlaştırdı · ailesi onu güzel yiyecekler ve özel ikramlarla şımarttı · dilediğini yapmasına ve keyif sürmesine engel olunmayan şımartılmış kimse · oranın bolluk içinde azmış zorba ileri gelenleri
  رجل مترف منعم، وترفه أهله إذا نعموه بالطعام الطيب والشيء يخص به (maqayis)؛ وأترفته النعمة أي أطغته (sihah)؛ الترفة النعمة، وصبي مترف إذا كان منعم البدن مدللا، والمترف الذي أبطرته النعمة وسعة العيش (tahdhib)؛ المترف المتروك يصنع ما يشاء لا يمنع منه (tahdhib)؛ الترفة التوسع في النعمة، يقال أترف فلان فهو مترف (mufradat)

## ق د و (root_001208): 43:23 مُّقْتَدُونَ

- **B001** izlenen örnek, öncü ve dayanak — örnek alınan kişi ya da şey · örnek alma yollarının dallandığı temel · örnek alınan kişi ya da şey · örnek alınan kişiler veya şeyler
  فلان قدوة يقتدى به (maqayis;sihah)؛ القدوة الإسوة (sihah)؛ القدو أصل البناء الذي ينشعب منه تصريف الاقتداء (tahdhib)؛ القدوة التقدم (tahdhib)
- **B002** ölçüce denk getirme; karşılaştırmada erişilemez olma [kalıp] — bir mızrak, karış veya yay uzunluğu kadar · hiç kimse ona yaklaşamaz veya onunla boy ölçüşemez
  مقادرة في الشيء حتى يأتي به مساويا لغيره (maqayis)؛ هذا قدى رمح أي قيسه (maqayis)؛ قدى رمح أي قدر رمح (sihah)؛ قدى وقيد وقاد كله بمعنى قدر الشيء (tahdhib)؛ لا يقاديه أحد إذا برز في الخلال كلها (tahdhib)
- **B003** izlenen gidişi düzgünce sürdürme — atını alışılmış düzenli gidişinde sürmek · bineği üzerinde düzgün bir gidişle ilerlemek · din yolunda doğru olmak veya haberde doğru çıkmak · yapmakta olduğun işi sürdür
  فلان يقدو به فرسه إذا لزم سنن السيرة (maqayis)؛ تقدى فلان على دابته إذا سار سيرة على استقامة (maqayis)؛ مر فلان يقدو به فرسه (sihah)؛ أقدى إذا استوى في طريق الدين واستقام في الخبر (tahdhib)؛ خذ في هديتك وقديتك أي فيما كنت فيه (sihah;tahdhib)
- **B004** yolculuktan geliş, ilk gelenler ve yerleşen yeni gruplar — ilk gelen küçük insan grubu · yolculuktan gelme veya yaklaşma · bir yere ayrı ayrı gelip orada yerleşen insanlar · yolculuktan gelmek
  أتتنا قادية من الناس وهم أول من يطرأ عليك (maqayis;sihah;tahdhib)؛ القدو القدوم من السفر والقدو بالقرب (tahdhib)؛ قدا وأقداء وهم الناس يتساقطون بالبلد فيقيمون به (tahdhib)؛ أقدى إذا قدم من سفر (tahdhib)
- **B005** yiyeceğin hoş kokusu, tadı ve kokulandırılması — etin veya yemeğin hoş kokması · pişmiş yemeğin hoş kokulu olması · tenceredeki yemeğin hoş kokusu veya hoş kokulu oluşu · bu yemeğin tadı ve kokusu ne güzel · güzel kokulu maddeleri karıştırıp tütsüleyerek kokulandırmak · yiyeceğin tazeyken taşıdığı hoş tat ve koku
  قدا اللحم إذا شممت له رائحة طيبة (maqayis)؛ قدا اللحم والطعام إذا شممت له رائحة طيبة (sihah)؛ ما أقدى طعام فلان أي ما أطيب طعمه ورائحته (sihah)؛ إذا كان الطبيخ طيب الريح قلت قدي (tahdhib)؛ قداه بالطيب تقدية إذا خلط العود بالعنبر والمسك (tahdhib)؛ ذهبت قداوة الطعام إذا أتى عليه وقت يتغير فيه طعمه وريحه وطيبه (tahdhib)
- **B006** atın hızlanması ve tırısa benzer özel yürüyüşü — atın hızlanması · hızlanma · atın ön ayaklarını kaldırıp arka ayaklarını toplayarak tırısa benzer yürümesi
  قدى الفرس أي أسرع (sihah)؛ القديان والذميان الإسراع (tahdhib)؛ تقدي الفرس استعانته بهاديه في مشيه برفع يديه وقبض رجليه شبه الخبب (tahdhib)
- **B007** insanda güçlü sırt ve kısa boyun; devede sağlam yapı — 
  رجل قندأو شديد الظهر قصير العنق (maqayis)؛ الناقة الصلبة الشديدة وجمل قندأو وسندأو والنون زائدة (tahdhib)
- **B008** yaşlanıp ölüme ulaşmak — yaşlanıp ölüm sınırına ulaşmak
  أقدى أيضا إذا أسن وبلغ الموت (tahdhib)

## ج ي ء (root_000281): 43:24 جِئْتُكُم, 43:29 جَآءَهُمُ, 43:30 جَآءَهُمُ, 43:38 جَآءَنَا, 43:47 جَآءَهُم, 43:53 جَآءَ, 43:63 جَآءَ, 43:63 جِئْتُكُم, 43:78 جِئْنَٰكُم

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

## ج ي ء (root_000282): 43:24 جِئْتُكُم, 43:29 جَآءَهُمُ, 43:30 جَآءَهُمُ, 43:38 جَآءَنَا, 43:47 جَآءَهُم, 43:53 جَآءَ, 43:63 جَآءَ, 43:63 جِئْتُكُم, 43:78 جِئْنَٰكُم

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ن ق م (root_001545): 43:25 فَٱنتَقَمْنَا, 43:41 مُّنتَقِمُونَ, 43:55 ٱنتَقَمْنَا

- **B001** hoşnutsuzlukla yadırgama ve ayıplama — yadırgamak, ayıplamak ve hoşnutsuzluk duymak · yadırgama ve ayıplama · ayıplayıp hoşnutsuzluğunu gösteren kimse · yadırgama ve hoşnutsuzluk
  إنكار شيء وعيبه؛ أنكرت عليه فعله (maqayis)؛ أنكر ولم يرض (ayn)؛ عتبت عليه؛ كرهته (sihah)؛ بالغت في كراهة الشيء؛ النقمة الإنكار (tahdhib)؛ أنكرته إما باللسان وإما بالعقوبة (mufradat)
- **B002** cezalandırarak karşılık verme ve öç alma — cezalandırma, acı çektirme ve öç alma · yaptığı kötülüğe ceza ile karşılık vermek · öldürülen yakınının öcünü almak · öldürülürse onun öcünü almak
  النقمة من العذاب والانتقام؛ فعاقبه (maqayis)؛ انتقمت منه كافأته عقوبة بما صنع (ayn)؛ انتقم الله منه أي عاقبه؛ النقمة (sihah)؛ نقم فلان وتره أي انتقم؛ النقمة العقوبة (tahdhib)؛ النقمة العقوبة (mufradat)

## ن ظ ر (root_001520): 43:25 فَٱنظُرْ, 43:66 يَنظُرُونَ

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

## ع ق ب (root_001033): 43:25 عَٰقِبَةُ, 43:28 عَقِبِهِۦ

- **B001** bağlama ve kiriş yapımında kullanılan sert beyaz tendon — kiriş yapılan sert beyaz tendon · ayak bileklerinin arkasındaki gergin tendon · oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak
  العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)
- **B002** topuk ve hemen arkasında kalan iz — topuk, ayağın arka bölümü · topuklar · ardınca çok kişi yürüyen, çok izlenen · birinin hemen ardından, onun izinden
  العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)
- **B003** dönüp geri çekilmek [kalıp] — dönüp geri çekilmek · geri dönmedi, arkasına bakmadı veya beklemedi
  ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)
- **B004** ardında kalan çocuklar ve torunlar — kişinin ardından kalan çocukları ve torunları · ardında çocuk veya soy bırakmadı
  عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)
- **B005** birbirinin ardından gelme ve yerini alma — öncekinin ardından gelen ve onun yerini alan · ardıl, bir başkasının ardından gelen · gece ile gündüzün sırayla birbirinin yerini alması · sırayla nöbet değiştiren gece ve gündüz görevlileri · binme veya çalışma sırası, nöbet
  كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)
- **B006** sonuç ve varılan son durum — son, sonuç, varılan nihai durum · karşılık veya sonuç; kimi kullanımda iyi karşılık · buna yol açtı, ardından bunu doğurdu
  أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)
- **B007** suçtan sonra verilen kötü karşılık — ceza, cezalandırma · onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz
  عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)
- **B008** ardından izleyip yeniden inceleme — hak istemek veya itiraz etmek için ardından izleyen kişi · onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur · haberi veya işi yeniden dönüp araştırmak
  المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)
- **B009** aynı tür işi yeniden yapma — aynı tür işi yeniden yapma · atın bir koşudan sonra yeniden ve daha iyi koşması · bir otlak türünden ötekine dönüşümlü geçen deve sürüsü · kuşun yükselişiyle alçalışı arasındaki hareket evresi · ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü
  التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)
- **B010** bedel, satış başvurusu ve elde tutma güvencesi — tutsağın veya bir şeyin yerine alınan bedel · satılan maldan doğan başvuru hakkı ve sorumluluk · malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur
  أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)
- **B011** geride kalan son parça ya da iz — ağır hastalıktan kalan belirti · kapta kalan son yemek suyu · soyluluk ve güzellikten kişide kalan görünür iz
  العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)
- **B012** sarp dağ geçidi ve kayalık çıkıntı — dik ve zorlu dağ yolu veya geçidi · kuyu ya da dağ yüzündeki dışarı taşan kaya
  العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)
- **B013** kartal ve ona benzetilen büyük sancak — kartal, güçlü yırtıcı kuş · kartala benzetilen büyük sancak veya bayrak · korkunç ve ağır bela
  العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)
- **B014** özel adlandırma kümesi — erkek kişi adı · erkek keklik ve ona benzetilen at
  يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)
- **B015** bitkinin sararıp kurumaya yaklaşması [kalıp] — bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak
  عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)

## ك ذ ب (root_001290): 43:25 ٱلْمُكَذِّبِينَ

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

## ب ر ء (root_000099): 43:26 بَرَآءٌ

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · yaratma anlamındaki ad · Tanrı için kullanılan yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;ayn;sihah;tahdhib)؛ البارئ (maqayis;ayn;sihah;tahdhib;mufradat)؛ البرية الخلق (sihah;tahdhib;mufradat)
- **B002** ilişik kesip uzak durma — bir kimseden uzaklaşıp ilişiğini kesti · istenmeyen şeyden sakınıp uzak durdu · kusurdan ve istenmeyenden temiz olma · istenmeyen şeyden ayrılmış ve uzak duran · açık uyarı ve ilişik kesme bildirimi
  التباعد من الشيء ومزايلته (maqayis)؛ أصل البرء والبراء والتبري التقصي مما يكره مجاورته (mufradat)؛ برئت منك وبرئت من فلان وتبرأت (sihah;tahdhib;mufradat)؛ البراءة من العيب والمكروه (maqayis;ayn)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşti · hastalıktan kurtulup sağlığa dönme · hastalığından iyileşmiş · Tanrı hastalığını giderip iyileştirdi
  البرء السلامة من السقم (maqayis;ayn)؛ برأ من المرض برءا (jamhara;sihah;tahdhib)؛ أبرأه الله من مرضه إبراء (sihah;tahdhib)؛ برأت من المرض وبرئت من المرض (mufradat;tahdhib)
- **B004** hak veya borçtan salıverme — hakkımı sana bıraktım ve ondan çekildim · borç yükünden çıktı · kişiyi borç veya güvence yükünden salıverdi · onu üzerindeki haktan salıverdi · eş veya ortakla karşılıklı bağları çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ برئت من الديون (sihah)؛ أبرأت من الدين والضمان (maqayis;ayn)؛ أبرأته مما لي عليه وبرأته تبرئة (sihah)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis;sihah)؛ بارأت الرجل أي برئ إلي وبرئت إليه (ayn)
- **B005** boşluğu yoklayıp temizleme — boşluğu araştırıp güvenceye alma · satın alınan kadınla ilişki öncesi bekledi · elindeki şeyi yoklayıp arıttı · idrar sonrası organı temizleme
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis;ayn)؛ استبرأت الجارية واستبرأت ما عندك (sihah)؛ الاستبراء إنقاء الذكر بعد البول (ayn)
- **B006** özel ay gecesi adı — ayın son gecesi için özel ad · ayın ilk gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ البراء أول ليلة من الشهر (sihah)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ البرأة بالهمز ناموس الصائد والجمع برأ (jamhara)؛ البرأة بالضم قترة الصائد والجمع برأ (sihah)

## ب ر ء (root_000100): 43:26 بَرَآءٌ

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · Tanrı için yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;tahdhib)؛ البارئ الله جل ثناؤه (maqayis)؛ الله البارىء الذارىء (tahdhib)؛ البرية الخلق (tahdhib)
- **B002** ilişik kesip uzak durma — bir şeyden temiz, uzak ve kurtulmuş · muhataptan veya benimsenmeyen şeyden ilişik kesme bildirimi · açık uyarı ve ilişik kesme bildirimi · kusurdan ve istenmeyenden uzak olma
  التباعد من الشيء ومزايلته (maqayis)؛ البراءة من العيب والمكروه (maqayis)؛ برىء إذا تخلض وتنزه وتباعد (tahdhib)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)؛ أنا براء منك (maqayis;tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşme · hastalıktan kurtulup iyileşti · Tanrı hastalığını giderip iyileştirdi
  البرء وهو السلامة من السقم (maqayis)؛ برئت وبرأت (maqayis)؛ برأت من المرض برءا وبرئت أبرأ برءا (tahdhib)؛ أبرأه الله من مرضه إبراء (tahdhib)
- **B004** hak bağını çözme [kalıp] — borç yükünden kurtuldu · hakkımı sana bırakıp ondan çekildim · borç ve güvence yükünü düşürdü · eşinden karşılıklı bağ çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ أبرأت من الدين والضمان (maqayis)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis)؛ برئت من الدين (tahdhib)؛ برئت إليك من فلان (tahdhib)
- **B005** ilişki öncesi boşluk yoklama — satın alınan kadınla ilişki öncesi bekleyip kuşkudan boşluğu sağlama
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis)؛ برئت من الريبة التي تمنع المشتري من مباشرتها (maqayis)
- **B006** ayın son gecesi adı — ayın son gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ يبرأ فيها القمر من الشمس (tahdhib)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ قد زايل إليها كل أحد (maqayis)

## ف ط ر (root_001165): 43:27 فَطَرَنِى

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

## ك ل م (root_001316): 43:28 كَلِمَةًۢ

- **B001** anlaşılır konuşma, hitap ve söz alışverişi — anlaşılır konuşma · ona hitap etti · birine söz yöneltme · ona sözle karşılık verdi · bir uzaklaşmadan sonra yeniden karşılıklı konuştuk · seninle konuşan ve senin de konuştuğun kişi · konuşulacak yer · sözünü iyi ve akıcı söyleyen kimse · iyi konuşan adam
  أحدهما يدل على نطق مفهم (maqayis)؛ كلمته أكلمه تكليما وهو كليمى إذا كلمك أو كلمته (maqayis)؛ كليمك الذي يكلمك وتكلمه (ayn;tahdhib)؛ الكليم الذي يكلمك وكلمته تكليما وكلاما (sihah)؛ كالمته إذا جاوبته وتكالمنا بعد التهاجر (sihah)؛ ما أجد متكلما أي موضع كلام والكلماني المنطيق (sihah)؛ رجل تكلامة يحسن الكلام (tahdhib)
- **B002** anlam taşıyan tek söz birimi — anlamlı tek söz veya harf · en az üç sözden oluşan sözler topluluğu · sözler · bütün bir anlatı, şiir veya söylev · Tanrı'nın sözü · Tanrı'nın söylediği söz
  يسمون اللفظة الواحدة المفهمة كلمة والقصة كلمة والقصيدة بطولها كلمة ويجمعون الكلمة كلمات وكلما (maqayis)؛ الكلمة لغة حجازية والكلمة تميمية والجميع الكلم (ayn;tahdhib)؛ الكلام اسم جنس يقع على القليل والكثير والكلم لا يكون أقل من ثلاث كلمات والكلمة أيضا القصيدة بطولها (sihah)؛ الكلمة تقع على الحرف الواحد من حروف الهجاء وتقع على لفظة واحدة مؤلفة من جماعة حروف لها معنى وتقع على قصيدة بكمالها وخطبة بأسرها (tahdhib)؛ كلمة الله وكلام الله وكلم الله وكلمات الله (sihah;tahdhib)
- **B003** yaralama ve yara — yara · yaralar · yaralar · onu yaraladı · yaralayan · yaralanmış · yaralı kişi · yaralılar · yaralama · onları yaralayıp damgalaması
  الأصل الآخر الكلم وهو الجرح والكلام الجراحات وجمع الكلم كلوم (maqayis)؛ الكلم الجرح والجميع الكلوم وكلمته أكلمه كلما وأنا كالم وهو مكلوم أي جرحته (ayn)؛ الكلم الجراحة والجمع كلوم وكلام والتكليم التجريح (sihah)؛ الكلم الجرح والجميع كلوم وكلمته وأنا أكلمه كلما وأنا كالم وهو مكلوم (tahdhib)؛ تكلمهم فسر تجرحهم وتسمهم (sihah;tahdhib)

## ب ق ي (root_000142): 43:28 بَاقِيَةً

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

## ر ج ع (root_000544): 43:28 يَرْجِعُونَ, 43:48 يَرْجِعُونَ, 43:85 تُرْجَعُونَ

- **B001** geri dönmek veya geri döndürmek — kendiliğinden önceki yere veya duruma dönmek · birini ya da bir şeyi yerine geri göndermek · başkasını geri döndürmek
  أصل كبير مطرد منقاس يدل على رد وتكرار (maqayis)؛ رجعت رجوعا ورجعته يستوي فيه اللازم والمجاوز (ayn)؛ رجعته إلى أهله أي رددته إليهم (jamhara)؛ رجع بنفسه رجوعا ورجعة غيره رجعا (sihah)؛ رجعته رجعا فرجع رجوعا (tahdhib)؛ الرجوع العود إلى ما كان منه البدء والرجع الإعادة (mufradat)
- **B002** ölümden sonra dönüş ve yeniden diriliş — Tanrı'ya dönüş veya nihai varış · Tanrı'ya kaçınılmaz dönüş · ölümden sonra dünyaya yeniden gelme
  إلى الله عز وجل مرجعك ورجوعك ورجعاك (jamhara)؛ فلان يؤمن بالرجعة أي بالرجوع إلى الدنيا بعد الموت (sihah)؛ إنه على بعثه يوم القيامة لقادر (tahdhib)؛ إلى الله مرجعكم وإن إلى ربك الرجعى (mufradat)
- **B003** bir şeyden vazgeçip geri dönmek [kalıp] — bir işten vazgeçmek veya yanlış davranışı bırakmak
  رجعت عن كذا رجعا؛ يرجعون عن الذنب؛ حرمنا عليهم أن يتوبوا ويرجعوا عن الذنب (mufradat)
- **B004** boşama sonrası evlilik bağına geri alma — boşanan eşi geri alma hakkı · boşadığı eşini evlilik bağına geri almak · eşi öldükten veya boşandıktan sonra ailesine dönen kadın
  راجع الرجل امرأته وهي الرجعة (maqayis)؛ طلاقا يملك الرجعة والرجعة والرجعى (jamhara)؛ له على امرأته رجعة (sihah)؛ المراجع من النساء التي يموت زوجها أو يطلقها فترجع إلى أهلها (tahdhib)؛ الرجعة والرجعة في الطلاق (mufradat)
- **B005** iletiye dönen yanıt — mektubun veya iletinin yanıtı · geri dönen yanıt · cevabı sahibine geri iletmek
  المرجوع جواب الرسالة (maqayis)؛ رجعى رسالتي أي مرجوعها ورجعان الكتاب جوابه (sihah)؛ رجع الجواب ورجع الرشق في الرمي ما يرد عليه (tahdhib)؛ بم يرجع المرسلون فمن رجع الجواب (mufradat)
- **B006** yinelenen yağmur veya biriken su — yağmur veya yeniden biriken su · su birikintileri veya su toplayan vadi üstleri
  الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث (maqayis)؛ الرجع الغدير أو الماء يترقرق والرجع المطر (jamhara)؛ الرجع المطر والرجع الغدير (sihah)؛ ذات الرجع أي ذات المطر والرجع في كلام العرب الماء والرجعان أعالي التلاع (tahdhib)؛ والسماء ذات الرجع أي المطر وسمي الغدير رجعا (mufradat)
- **B007** sesi yineleyip dalgalandırma — okuma veya söylemede sesi yineleyip dalgalandırma · namaza çağrıda tanıklık sözlerini tekrarlama · gök gürültüsünün yinelenen sesi
  الترجيع في الصوت ترديده (maqayis)؛ الترجيع تقارب ضروب الحركات في الصوت (ayn)؛ ترجيع الصوت ترديده في الحلق والترجيع في الأذان (sihah)؛ يقولون للرعد رجع والترجيع في الأذان (tahdhib)؛ الترجيع ترديد الصوت باللحن في القراءة وفي الغناء وتكرير قول مرتين فصاعدا (mufradat)
- **B008** hayvanın ön ayak adımı [kalıp] — hayvanın ön ayaklarını geri getirerek attığı adım · dişi devenin yürüyüş biçimini değiştirmesi
  الرجع رجع الدابة يديها في السير (maqayis)؛ الرجع ترجيع الدابة يدها في السير (ayn)؛ رجع الدابة يديها في السير خطوها (sihah)؛ الرجع الخطو وراجعت الناقة رجاعا إذا كانت في ضرب من السير فرجعت إلى سير سواه (tahdhib)
- **B009** çizgileri yeniden çekip karartmak [kalıp] — dövme çizgilerini yeniden çekmek veya karartmak
  ترجيع وشي النقش والوشم والكتابة خطوطها (ayn)؛ رجع الواشمة خطها (sihah)؛ رجع الوشم والنقوش وترجيعه أن يعاد عليه السواد مرة بعد أخرى (tahdhib)
- **B010** elini geriye uzatmak [kalıp] — elini geriye, ok kılıfına veya kılıca uzatmak
  أرجع الرجل يده في كنانته (maqayis)؛ أرجع يده إلى سيفه ليستله أو إلى كنانته ليأخذ سهما (jamhara)؛ أرجع الرجل إذا أهوى بيده إلى خلفه ليتناول شيئا (sihah)؛ أرجع الرجل يده إذا أهوى بها إلى كنانته (tahdhib)؛ أرجع يده إلى سيفه ليستله (mufradat)
- **B011** satış bedeliyle yerine mal almak — hayvanları satıp bedeliyle yerlerine başkalarını almak · satılanın bedeliyle alınan veya tahsilde yerine kabul edilen karşılık
  الراجعة الناقة تباع ويشترى بثمنها مثلها (maqayis)؛ ارتجع فلان إبلا إذا باع الذكور واشترى الإناث (jamhara)؛ الرجعة في الصدقة إذا أخذ المصدق مكانها أسنانا فوقها أو دونها (sihah)؛ الارتجاع أن يبيعها ثم يشتري بثمنها مثلها أو غيرها (tahdhib)؛ دابة لها مرجوع يمكن بيعها بعد الاستعمال وارتجع إبلا (mufradat)
- **B012** kuşların göçten geri dönüşü — kuşların mevsimsel geçişten sonra geri dönüşü
  الرجاع رجوع الطير بعد قطاعها (maqayis)؛ الرجاع رجوع الطير بعد قطاعها إذا رجعت من المواضع الحارة إلى المواضع الباردة (jamhara)؛ الرجاع أيضا رجوع الطير بعد قطاعها (sihah)؛ الرجاع مختص برجوع الطير بعد قطاعها (mufradat)
- **B013** gebeliğin oluşmaması veya çok erken sona ermesi [kalıp] — çiftleştiği halde gebe kalmayan veya gebe sanılıp boş çıkan dişi deve · yavrusu biçimlenmeden düşük yapmak
  ناقة راجع وهي التي يضربها الفحل فلا تلقح (jamhara)؛ أتان راجع وناقة راجع فيظن أن بها حملا ثم تخلف (sihah)؛ إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت (tahdhib)؛ ناقة راجع ترد ماء الفحل فلا تقبله (mufradat)
- **B014** yolculukta yıpranma veya güçsüzlükten sonra toparlanma [kalıp] — bir yolculuktan ötekine sürülerek bitkin düşmüş hayvan · zayıflıktan sonra semirip iyi duruma gelmek · hastalıktan sonra kendini ve gücünü yeniden bulmak
  الرجيع من الدواب ما رجعته من سفر إلى سفر وأرجعت الإبل إذا كانت مهازيل فسمنت (maqayis)؛ بعير رجيع سفر مثل نضو سفر (jamhara)؛ الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال (sihah)؛ يقال للمريض إذا ثابت إليه نفسه بعد تهوك من العلة راجع (tahdhib)؛ من الدابة ما رجعته من سفر إلى سفر ورجع سفر كناية عن النضو (mufradat)
- **B015** geri çıkan veya yeniden işlenen şey — sindirimden sonra çıkan dışkı veya bağırsak artığı · hayvanın ağzına getirip yeniden çiğnediği geviş · sahibine geri çevrilen veya yinelenen söz · eskimiş veya sökülüp yeniden yapılmış giysi · soğuduktan sonra yeniden ısıtılmış yemek
  الرجيع الجرة لأنه يردد مضغها (maqayis)؛ الرجيع يكنى به عن ذي البطن وحبل رجيع وثوب رجيع (jamhara)؛ الرجيع الروث والبعر وذو البطن وكل شئ يردد فهو رجيع (sihah)؛ الرجيع يكون الروث والعذرة والرجيع العرق وكل طعام برد فأعيد على النار فهو رجيع (tahdhib)؛ الرجيع كناية عن أذى البطن وجبة رجيع أعيدت بعد نقضها (mufradat)

## م ت ع (root_001395): 43:29 مَتَّعْتُ, 43:35 مَتَٰعُ

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

## ح ق ق (root_000347): 43:29 ٱلْحَقُّ, 43:30 ٱلْحَقُّ, 43:78 بِٱلْحَقِّ, 43:78 لِلْحَقِّ, 43:86 بِٱلْحَقِّ

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

## س ح ر (root_000682): 43:30 سِحْرٌ, 43:49 ٱلسَّاحِرُ

- **B001** boğaz ve yemek borusu çevresindeki göğüs üstü iç organ bölgesi — boğaz ve yemek borusuna bağlı göğüs üstü iç organ bölgesi · korkudan içi kabardı · kesimde çıkarılıp atılan boğaz-göğüs dokusu · geniş karınlı ya da göğüs içi hasta · iç boşluğu bulunan ve besine gereksinen canlı
  السحر وهو ما لصق بالحلقوم والمرئ من أعلى البطن (maqayis)؛ السحر والسحر الرئة في البطن وما تعلق بالحلقوم؛ السحر أعلى الصدر (ayn)؛ السحر الرئة وما تعلق بها؛ انتفخ سحرك؛ كل ما كان له سحر فهو مسحر (jamhara)؛ السحر الرئة؛ انتفخ سحره (sihah)؛ السحر خفيف ما لصق بالحلقوم وبالمريء من أعلى البطن؛ انتفخ سحره للجبان (tahdhib)؛ السحر طرف الحلقوم والرئة؛ السحارة ما ينزع من السحر عند الذبح (mufradat)
- **B002** aldatma ve gerçeğinden saptırma — büyü, aldatma ve göz yanıltma · gizli güçlerden yardım alarak yapılan büyü · bazı sözler büyü gibi etkiler · aldattı ya da yönünden çevirdi · gözü yanıltıp gerçeği başka gösterdi · büyü yapan kimse; kimi eski kullanımlarda bilgili ve etkili kişi · çokça veya ustalıkla büyü yapan kimse · büyüden etkilenmiş ya da aklı ve durumu bozulmuş · işlevi bozulmuş yiyecek · ürün vermeyen ya da aşırı yağmurla bozulmuş toprak · sütü azalmış keçi · suyu aşırı olup zarar veren yağmur
  إخراج الباطل في صورة الحق؛ الخديعة (maqayis)؛ كل ما كان من الشيطان فيه معونة؛ الأخذة التي تأخذ العين؛ البيان في الفطنة (ayn)؛ السحر معروف سحر يسحر سحرا والفاعل ساحر وسحار (jamhara)؛ كل ما لطف مأخذه ودق فهو سحر؛ سحره بمعنى خدعه (sihah)؛ أصل السحر صرف الشيء عن حقيقته؛ تصرفون؛ ما سحرك عن وجه كذا؛ مسحورا ذاهب العقل مفسدا (tahdhib)؛ الخداع وتخييلات لا حقيقة لها؛ استجلاب معاونة الشيطان (mufradat)
- **B003** yiyecek ve içecekle besleme — besin; yiyecek veya içecekle doyurma · yiyecek ve içecekle beslenip oyalanırız · iç boşluğu bulunan ve besine gereksinen canlı
  من كان ذا سحر لم يجد بدا من مطعم ومشرب (maqayis)؛ السحر الغذو؛ المخلوق الذي يطعم ويسقى (ayn)؛ المرزوق الذي يأكل الرزق؛ نسحر بالطعام وبالشراب (jamhara)؛ نسحر بالطعام وبالشراب؛ المسحر من المعللين (sihah)؛ السحر الغذاء؛ نسحر بالطعام أي نعلل به (tahdhib)؛ سموا الغذاء سحرا؛ محتاج إلى الغذاء (mufradat)
- **B004** tan ağarmadan önceki son gece dilimi — tan ağarmadan önceki son gece dilimi · tan öncesi vaktin sabaha en yakın bölümü · belirsiz bir gecenin tan öncesi vaktinde · tan öncesi vaktin en üst ucu, sabahın ilk soluğu · tan öncesi vakte girdik ya da o vakitte yola çıktık · tan öncesinde yola çıktı ya da kuş o vakitte öttü · tan ağarmadan önce yola çıkan kimse · erken davrandı ya da tan öncesinde çıktı
  السحر والسحرة وهو قبل الصبح؛ أتيتك سحر؛ أتيتك سحرا (maqayis)؛ السحر آخر الليل؛ أسحرنا (ayn)؛ أسحر القوم إذا خرجوا في السحر؛ استحر الطائر إذا غرد في السحر؛ أعلى سحرين (jamhara)؛ السحر قبيل الصبح؛ السحرة السحر الأعلى؛ استحر الديك (sihah)؛ السحر قطعة من الليل؛ السحر آخر الليل؛ أسحرنا؛ استحرنا؛ سحر إذا بكر (tahdhib)؛ السحر والسحرة اختلاط ظلام آخر الليل بضياء النهار؛ المسحر الخارج سحرا (mufradat)
- **B005** tan öncesi öğünü — tan ağarmadan önce yenilen öğün · tan öncesi öğününü yeme
  تسحرنا أكلنا سحورا؛ السحور على فعول وضع اسما لما يؤكل في ذلك الوقت (ayn)؛ السحور ما أكل في السحر (jamhara)؛ السحور ما يتسحر به (sihah)؛ السحور ما يتسحر به وقت السحر من طعام أو لبن أو سويق؛ تسحر الرجل ذلك الطعام (tahdhib)؛ السحور اسم للطعام المأكول سحرا؛ التسحر أكله (mufradat)
- **B006** iki renk gösteren çekmeli çocuk oyuncağı — çekildiği yana göre başka renk gösteren çocuk oyuncağı
  السحارة شيء يلعب به الصبيان إذا مد خرج على لون وإذا مد من جانب آخر خرج على لون آخر (ayn;tahdhib)
- **B007** hayvanları semirten saplı bir ot — hayvanları semirten, saplı, küçük yapraklı ve siyah tohumlu ot
  الإسحارة بقلة يسمن عليها المال (ayn;tahdhib)؛ بقلة حارة تنبت على ساق لها ورق صغار لها حبة سوداء (tahdhib)
- **B008** bir şeyin kenarı, sonu ya da üst ucu — her şeyin kenarı ya da sonu · açık arazinin kıyıları · vadinin üst kesimi · siyahın üstünde görünen beyazlık
  السحر والسحرة بياض يعلو السواد؛ سحر كل شيء طرفه؛ أسحار الفلاة أطرافها؛ سحر الوادي أعلاه (tahdhib)

## ر ج ل (root_000546): 43:31 رَجُلٍ

- **B001** bacak uzvu — insan veya hayvanın bacak uzvu · koyunu bacağından asmak · kişiyi bacağından yakalamak · iri bacaklı
  الرجل رجل الإنسان وغيره (maqayis)؛ الرجل واحدة الأرجل (sihah)؛ الرجل العضو المخصوص بأكثر الحيوان (mufradat)؛ رجلت الشاة علقتها برجلها (maqayis;sihah)؛ ارتجلت الرجل أخذت برجله (maqayis;sihah)؛ الأرجل العظيم الرجل (maqayis;ayn;sihah)
- **B002** erkek insan — kadın olmayan erkek insan · bazı özellikleriyle erkeğe benzetilen kadın · erkekçe olgunluk ve dayanıklılık
  هذا رجل أي ليس بأنثى (ayn)؛ الرجل خلاف المرأة (sihah)؛ الرجل مختص بالذكر من الناس (mufradat)؛ الرجولية والجلادة (mufradat)؛ يقال للمرأة الرجلة (maqayis;sihah)
- **B003** yaya giden kişi — yaya giden, binici olmayan kişi · yayalar topluluğu · yürümeye güçlü ve dayanıklı kimse · yürünmesi güç, çok taşlı arazi · bineğinden inip yaya olmak
  الرجل الرجالة (maqayis)؛ هذا رجل أي راجل (ayn)؛ الرجل خلاف الفارس (sihah)؛ اشتق من الرجل رجل وراجل للماشي بالرجل (mufradat)؛ رجل رجيل أي قوي على المشى (sihah)؛ ترجل القوم نزلوا على دوابهم (ayn)؛ حرة رجلاء يصعب فيها المشي (jamhara)
- **B004** birinin devrinde [kalıp] — belirtilen kişinin devrinde ve zamanında
  كان ذاك على رجل فلان أي في زمانه (maqayis)؛ كان ذلك على رجل فلان أي في عهده وزمانه (sihah)؛ استعير الرجل لزمان الإنسان (mufradat)
- **B005** bir bacağı beyaz hayvan [kalıp] — bir bacağında beyazlık bulunan at veya başka bir hayvan
  الأرجل من الدواب الذي ابيض أحد رجليه (maqayis)؛ الرجلة أيضا مصدر الأرجل من الدواب بإحدى رجليه بياض (ayn)؛ فرس أرجل والأنثى رجلاء إذا كان في إحدى رجليه بياض (jamhara)؛ الأرجل من الخيل الذي في إحدى رجليه بياض (sihah)؛ الأرجل الأبيض الرجل من الفرس (mufradat)
- **B006** büyük çekirge sürüsü [kalıp] — büyük çekirge kümesi veya sürüsü
  الرجل القطيع من الجراد ونحوه من الخلق (ayn)؛ رأيت رجلا من جراد أي قطعة عظيمة (jamhara)؛ الرجل أيضا الجماعة الكثيرة من الجراد خاصة (sihah)؛ استعير الرجل للقطعة من الجراد (mufradat)
- **B007** semizotu diye bilinen ot — semizotu diye anılan ot; bazı tanıklıklarda tuzcul bitki · kereviz
  الرجلة هي التي يقال لها البقلة الحمقاء (maqayis)؛ الرجلة منبت العرفج الكثير (ayn)؛ التراجيل الكرفس (ayn)؛ الرجلة نبت من الحمض (jamhara)؛ الرجلة بقلة وتسمى الحمقاء (sihah)؛ الرجلة البقلة الحمقاء (mufradat)
- **B008** su akıntısı yatağı [kalıp] — suyun aktığı tek bir doğal yol veya yatak
  قال قوم بل الرجل مسايل الماء واحدتها رجلة (maqayis)؛ الرجلة أيضا واحدة الرجل وهي مسايل الماء (sihah)؛ استعير الرجل لمسيل الماء الواحدة رجلة (mufradat)
- **B009** ayak benzetmeli özel adlar [kalıp] — yayın üst veya alt kolu · kuş ayağı biçimindeki damga · yavrunun emmesini engelleyen meme bağı
  رجل القوس سيتها العليا (maqayis)؛ رجل القوس سيتها السفلى (ayn;sihah)؛ رجل الطائر ضرب من الميسم (maqayis)؛ رجل الطائر ميسم (sihah)؛ رجل الغراب ضرب من صر أخلاف النوق (maqayis)؛ رجل الغراب ضرب من الابل لا يقدر الفصل على أن يرضع معه (sihah)
- **B010** orta kıvırcıklıkta saç — ne çok kıvırcık ne dümdüz olan saç · saçı tarayıp düzene sokmak
  رجلت الشعر (maqayis)؛ رجل رجل بين الرجل أي شعره رجل (ayn)؛ رجل الرجل شعره إذا سرحه (jamhara)؛ شعر رجل إذا لم يكن شديد الجعودة ولا سبطا (sihah)؛ رجل شعره (mufradat)
- **B011** hazırlıksız söylemek — sözü veya konuşmayı önceden hazırlamadan söylemek
  ارتجل الكلام (ayn)؛ ارتجل خطبة إذا أنشأها (jamhara)؛ ارتجال الخطبة والشعر ابتداؤه من غير تهيئة (sihah)؛ ارتجل الكلام أورده قائما من غير تدبر (mufradat)
- **B012** günün yükselip aydınlığın yayılması — günün yükselip aydınlığın yayılması
  ترجل النهار إذا ارتفع (maqayis;ayn;sihah)؛ ترجلت الضحى إذا انبسطت (jamhara)؛ ترجل النهار انحطت الشمس عن الحيطان (mufradat)
- **B013** kuyuya iple indirilmeden inmek — kuyuya iple sarkıtılmadan kendi başına inmek
  ترجلت في البئر إذا نزلت فيها من غير أن تدلى (maqayis)؛ ترجلت البئر أي نزلتها من غير تدل (ayn)؛ ترجل الرجل في البئر إذا رمى بنفسه فيها (jamhara)؛ ترجل في البئر أي نزل فيها من غير أن يدلى (sihah)؛ ترجل في البئر تشبيها بذلك (mufradat)
- **B014** yavruyu annesiyle serbest bırakmak — yavruyu annesiyle bırakıp dilediğinde emmesine izin vermek
  أرجلت الفصيل تركته يمشي مع أمه يرضع متى شاء (maqayis)؛ أرجلت الفصيل مع أمه يرضع متى شاء (jamhara)؛ الرجل أن ترسل البهة مع أمها ترضعها متى شاءت (sihah)؛ أرجلت الفصيل أرسلته مع أمه (mufradat)
- **B015** atın iki yürüyüşü karıştırması — atın koşarken iki farklı yürüyüş düzenini birbirine katması
  ارتجل الفرس ارتجالا إذا خلط العنق بالهملجة (maqayis)؛ ارتجل الفرس إذا خلط العنق بشئ من الهملجة (sihah)؛ ارتجل الفرس في عدوه (mufradat)
- **B016** dik duran pişirme kazanı — dik konulan, özellikle bakır pişirme kazanı
  المرجل مشتق من هذا أيضا لأنه إذا نصب فكأنه أقيم على رجل (maqayis)؛ المرجل معروف عربي صحيح (jamhara)؛ المرجل قدر من نحاس (sihah)؛ المرجل القدر المنصوبة (mufradat)
- **B017** koyunların art arda doğurması — koyunların birbiri ardınca doğurması
  إذا ولدت الغنم بعضها بعد بعض قالوا ولدتها الرجيلاء (maqayis)؛ إذا ولدت الغنم بعضها بعد بعض قيل ولدتها الرجيلاء (sihah)
- **B018** hayvanın biniciye ödetilmeyen vuruş zararı [kalıp] — hayvanın vuruşundan doğan ve binicisine ödetilmeyen zarar
  الرجل جبار وهو أن تنفحه الدابة ليس على راكبها غرم وهو هدر (ayn)
- **B019** işine bütün gücüyle sarılmak [kalıp] — önemli işine ciddiyetle ve bütün gücüyle sarılmak
  فلان قائم على رجل إذا جد في أمر حزبه (ayn)
- **B020** bir işe atılıp ilerlemek — bir işe güçlü biçimde atılıp onda ilerlemek
  ارتجل الرجل ركب رجليه في صاحبه ومضى (ayn)؛ ارتجل ما ارتجلت أي اركب ما ركبت من الأمر (ayn)

## ع ظ م (root_001029): 43:31 عَظِيمٍ

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

## ق س م (root_001226): 43:32 يَقْسِمُونَ, 43:32 قَسَمْنَا

- **B001** yüz güzelliği — güzellik, güzel görünüş · eksiksiz güzellik · yüz, özellikle yüzün güzel bölümü · yakışıklı ya da güzel yaradılışlı erkek · güzel yüzlü · yüzü güzel ve uyumlu · güzel yüz · güzel yüzlü kadın · güzel
  القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)
- **B002** şiddetli öğle sıcağı veya vakti — şiddetli öğle sıcağı veya öğle sıcağı vakti
  والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)
- **B003** paylara ayırma ve ayrılmış pay — bir şeyi parçalara veya paylara ayırmak · paylara ayırma · pay, kişiye düşen bölüm · bölüştürme, paylaşma · arazi veya evleri paylaştıran kimse · birlikte paylaşan ortak · öteki araziden ayrılmış arazi · az suyu eşit paylaştırmaya yarayan taş · kişilere ayrılmış paylar · ayırma ve dağıtma · zaman onları ayırıp dağıttı
  تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)
- **B004** yemin etme ve öldürme davasında paylaştırılan yeminler — yemin · yemin etti · ona yemin etti veya onunla antlaştı · Tanrı adına karşılıklı yemin ettiler · öldürme davasında yakınlara paylaştırılan yeminler
  اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)
- **B005** işaretli ok çekerek karar arama [kalıp] — işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme
  الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)
- **B006** işi ölçüp biçme; kaygıyla zihnin dağılması — işini ölçüp biçiyor ve nasıl yapacağını düşünüyor · kaygının dağıttığı zihin · kaygılar yüzünden düşüncesi dağılmış
  أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)
- **B007** yalıtık adlandırmalar — giysiyi ilk kez katlayıp kat izlerini oluşturan kimse · iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at
  القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)
- **B008** düşman ile Müslümanlar arasındaki ateşkes — düşman ile Müslümanlar arasındaki ateşkes
  القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)

## ع ي ش (root_001067): 43:32 مَّعِيشَتَهُمْ

- **B001** yaşam ve yaşayış durumu — yaşam · yaşadı · Tanrı ona hoşnut olacağı bir yaşam verdi · yaşayış biçimi · iyi bir yaşayış · övgüye değer bir yaşayış · dar ve sıkıntılı yaşam · durumu iyi olan kimse
  العيش الحياة (maqayis;ayn;sihah); العيش الحياة المختصة بالحيوان (mufradat); عيشة صالحة وراضية وصدق وسوء وضنك (maqayis;sihah;tahdhib;mufradat); رجل عائش حاله حسنة (maqayis;tahdhib)
- **B002** geçim araçları, ortamı ve geçinme uğraşı — yaşamı sağlayan yiyecek ve içecek · geçim kaynağı · geçim kaynakları · geçim aracı veya geçinilen yer · gündüz, geçim arama zamanı · yeryüzü, geçim sağlanan yer · geçim · geçinme yollarını sağlamak için çabalama · geçinebilecek kadar olanağa sahip olma · geçim · o topluluğun geçimliği süttür
  المعيشة ما يعاش به (maqayis;ayn;tahdhib); المطعم والمشرب وما يكون به الحياة (maqayis;ayn;tahdhib); كل شيء يعاش به أو فيه فهو معاش (maqayis;ayn); كل شيء يعاش به فهو معاش (tahdhib); ما يتعيش منه (mufradat); التعيش تكلف أسباب المعيشة (sihah); يتعيشون إذا كانت لهم بلغة من عيش (maqayis;tahdhib)

## ح ي ي (root_000383): 43:32 ٱلْحَيَوٰةِ, 43:35 ٱلْحَيَوٰةِ

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

## ح ي و (root_005544): documented alternative for 43:32 ٱلْحَيَوٰةِ, 43:35 ٱلْحَيَوٰةِ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## د ن و (root_000493): 43:32 ٱلدُّنْيَا, 43:35 ٱلدُّنْيَا

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

## ر ف ع (root_000582): 43:32 وَرَفَعْنَا

- **B001** bir şeyi yukarı kaldırmak — bir şeyi bulunduğu yerden yukarı kaldırmak · kendiliğinden yükselmek · yapıyı yükseltip uzatmak · üst üste serilmiş döşekler · onu göğe çıkarmak veya onurlandırmak · bir şeyi eliyle kaldırmak
  رفعت الشيء رفعا وهو خلاف الخفض (maqayis;ayn); الرفع ضد الخفض (tahdhib); الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها (mufradat); في البناء إذا طولته (mufradat)
- **B002** saygınlığı yüksek olmak veya yükseltmek — değerli ve onurlu döşekler · anılışını yüceltmek · konumunu ve saygınlığını yükseltmek · saygın ve yüksek konumlu · yüksek saygınlık ve onur · bir topluluğu alçaltıp diğerini yükselten · onu göğe çıkarmak veya onurlandırmak · değerli ve onurlandırılmış sayfalar · evleri onurlandırıp yüceltmek
  رفع الرجل يرفع رفاعة فهو رفيع إذا شرف (ayn;tahdhib); رجل رفيع أي شريف (sihah); الرفعة نقيض الذلة (tahdhib); في الذكر إذا نوهته (mufradat); في المنزلة إذا شرفتها (mufradat)
- **B003** bineğin orta-üst hızda ilerlemesi veya ilerletilmesi — devenin yürüyüşünü hızlandırmak · ağır yürüyüşle tam koşu arasında hızlı gidiş · hızı yer yer artan koşu
  مرفوع الناقة في سيرها خلاف الموضوع (maqayis); المرفوع من حضر الفرس والبرذون دون الحضر وفوق الموضوع (ayn;tahdhib); رفع البعير في السير أي بالغ (sihah); مرفوع السير شديدة (mufradat)
- **B004** yaklaştırmak veya yetkili önüne sunmak — kullanacaklara yaklaştırılmış döşekler · yaklaştırma · yönetici veya yargıç önüne sunmak · yargılanması için yetkili önüne çıkarmak · dilekçesini veya şikayetini sunmak · onu iki perdenin bulunduğu yere kadar ilerletmek · bir topluluğu savaşta öne sürmek
  الرفع تقريب الشيء (maqayis;sihah); رفعته للسلطان (maqayis); رفعته إلى السلطان (sihah); رفعت فلانا إلى الحاكم أي قدمته إليه (tahdhib); رفعت قصتي قدمتها (tahdhib)
- **B005** haberi açığa çıkarıp yaymak — açığa çıkarıp yayma · birinin yönetici hakkındaki haberini yaymak · iletileni duyurup yayan topluluk
  الرفع إذاعة الشيء وإظهاره (maqayis); كل رافعة رفعت علينا من البلاغ (maqayis;sihah;tahdhib); رفع فلان على العامل إذا أذاع خبره (maqayis;tahdhib); أذاع خبر ما احتجبه (mufradat)
- **B006** hasat ürününü harman yerine taşımak — hasat edilen ürünü harman yerine taşımak · ürünün harman yerine taşındığı dönem veya bu iş
  رفع الزرع أن يحمل بعد الحصاد إلى البيدر (maqayis;sihah); جاء زمن الرفاع إذا رفع الزرع (tahdhib); الرفاع أن يحصد الزرع ويرفع (tahdhib)
- **B007** dişi devenin sütünü memesinde tutması [kalıp] — sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve
  ناقة رافع إذا رفعت اللبأ في ضرعها (maqayis;sihah); التي رفعت لبنها فلم تدر رافع (tahdhib)
- **B008** kalçayı büyük gösteren dolgu — kadının kalçasını büyük göstermek için kullandığı dolgu
  الرفاعة ما تتعظم به المرأة الرسحاء (sihah); الرفاعة شيء تعظم به المرأة عجيزتها (tahdhib); الرفاعة ما ترفع به المرأة عجيزتها (mufradat)
- **B009** bağı yukarı çekmeye yarayan ip — bağlı kişinin bağını yukarı çekmekte kullandığı ip · bağlı kişinin elinde tutup bağını kaldırdığı ip
  رفاعة المقيد خيط يرفع به قيده إليه (sihah); الرفاع حبل القيد يأخذه المقيد بيده يرفعه إليه (tahdhib)
- **B010** sesin yüksekliği [kalıp] — sesin yüksekliği
  في صوته رفاعة ورفاعة (sihah;tahdhib); إذا كان رفيع الصوت (tahdhib)
- **B011** toplulukça ülke içinde ilerlemek — topluluğun ülke içinde yola koyulup ilerlemesi · yolculukta ilerleyenler
  رفع القوم فهم رافعون إذا أصعدوا في البلاد (tahdhib); الروافع إذا رفعوا في سيرهم (tahdhib)
- **B012** dil bilgisinde ötreye karşılık gelen çekim durumu — dil bilgisinde ötreye karşılık gelen çekim durumu
  الرفع في الإعراب كالضم في البناء (sihah); وهو من أوضاع النحويين (sihah)

## ب ع ض (root_000133): 43:32 بَعْضَهُمْ, 43:32 بَعْضٍ, 43:32 بَعْضُهُم, 43:32 بَعْضًا, 43:63 بَعْضَ, 43:67 بَعْضُهُمْ, 43:67 لِبَعْضٍ

- **B001** parça ve parçalara ayırma — bir şeyin parçası, bölümü veya ondan bir kesim · parçalar, bölümler · bir şeyi parçalara ayırmak · parçalara ayrılmak
  بعض كل شيء طائفة منه (maqayis;ayn;tahdhib)؛ بعض الشيء جزء منه (mufradat)؛ بعض الشيء واحد أبعاضه (sihah)؛ بعض الشيء معروف (jamhara)؛ بعضت الشيء تبعيضا إذا فرقته أجزاء (maqayis;ayn;tahdhib)؛ تبعض الشيء وبعضته أي فرقته (jamhara)؛ بعضته تبعيضا أي جزأته فتبعض (sihah)؛ بعضت كذا جعلته أبعاضا نحو جزأته (mufradat)
- **B002** sivrisinek ve ona bağlı zarar veya bulunma kullanımları — sivrisinek · sivrisinekler, sivrisinek topluluğu veya tahtakurusu · sivrisineğin çok olduğu gece · topluluğa sivrisineklerin zarar vermesi · sivrisineklerden zarar görmüş topluluk · bulundukları yerde sivrisinek olması · sivrisinek bulunan arazi · aşırı küçüklüğü veya olanaksızlığı yüzünden elde edilemeyen şey
  البعوضة وهي معروفة والجمع بعوض (maqayis)؛ البعوض جمع البعوضة وهي المؤذية العاضة في الصيف (ayn)؛ البعوض البق الواحدة بعوضة (sihah)؛ قوم مبعوضون وقد بعض القوم إذا آذاهم البعوض وأبعضوا إذا كان في أرضهم بعوض (tahdhib)؛ البعوض بني لفظه من بعض وذلك لصغر جسمها (mufradat)

## ف و ق (root_001188): 43:32 فَوْقَ

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

## د ر ج (root_000468): 43:32 دَرَجَٰتٍ

- **B001** yol boyunca ilerleme — çocuğun veya yaşlının kendine özgü yürüyüşü · çocuk yürümeye başladı · adam ya da kertenkele yürüyüp ilerledi · geçit, yol veya geçilen güzergah · tepeyi ya da dağ aralarını kesen yollar · geldiği yoldan geri döndü · kertenkelenin yolunu açık bırak · geçip giden rüzgar · bineğin ayakları · burası senin yuvan değil, yoluna git · yürüyenlerle ölüp gidenleri birlikte anarak aşırı yalancılığı anlatan söz · çocuğun ilk yürüyüşünde tutunup ilerlediği araç
  أصل واحد يدل على مضي الشيء والمضي في الشيء؛ رجع فلان أدراجه؛ درج الصبي إذا مشى مشيته؛ مدارج الأكمة الطرق المعترضة فيها (maqayis)؛ الدرجان مشية الشيخ والصبي؛ المدرجة ممر الأشياء؛ رجعت في أدراجي ودرجي أي طريقي (ayn)؛ درج الصبي إذا مشى؛ فلان على درج كذا أي على سبيله؛ مدرجة الطريق قارعته (jamhara)؛ درج الرجل والضب أي مشى؛ المدرجة المذهب والمسلك؛ رجعت أدراجي (sihah)؛ الريح التي تدرج أي تمر مرا؛ درج في غير مثل هذا الموضع مثل دب؛ للطريق الذي يدرج فيه الغلام والريح وغيرهما مدرج ومدرجة ودرج (tahdhib)؛ مدرجة قارعة الطريق؛ درج الشيخ والصبي درجانا مشى (mufradat)
- **B002** yükseliş dizisindeki basamak veya düzey — basamaklar ve yükselen sıralar · düzey, sıra veya yüksek konum · cennet katları ve düzeyleri · gök kuşağının ölçü bölümü
  الدرج جماعة عتب الدرجة؛ الدرجة في الرفعة والمنزلة؛ درجات الجنان منازل؛ كل برج من بروج السماء ثلاثون درجة (ayn)؛ الدرج الواحدة درجة وهي المنزلة؛ فلان في درجة عالية أي في منزلة رفيعة (jamhara)؛ الدرجة المرقاة؛ الدرجة واحدة الدرجات وهي الطبقات من المراتب (sihah)؛ الدرجة الرفعة في المنزلة؛ كل برج من بروج السماء ثلاثون درجة (tahdhib)؛ الدرجة نحو المنزلة إذا اعتبرت بالصعود؛ درجات النجوم (mufradat)
- **B003** aşama aşama ilerleme veya ilerletme — onu bir şeye azar azar yaklaştırdı · kandırıp yavaş yavaş bir işe çekti · bir konuda basamak basamak ilerledi · hastaya önce az verip yiyeceği giderek artırdı · onları azar azar ele geçireceğiz
  درجه إلى كذا واستدرجه أي أدناه منه على التدريج (sihah)؛ سنأخذهم قليلا قليلا ولا نباغتهم؛ استدرجه أي خدعه حتى حمله على أن درج في ذلك؛ درجت العليل تدريجا إذا أطعمته شيئا قليلا ثم زدته؛ استدرجه كلامي أي أقلقه حتى تركه يدرج (tahdhib)؛ يتدرج في كذا أي يتصعد فيه درجة درجة؛ نأخذهم درجة فدرجة؛ إدناؤهم من الشيء شيئا فشيئا (mufradat)
- **B004** tükenip geride kimse bırakmama — topluluk yok olup tükendi · adam öldü ve soy bırakmadı · yaşayanlarla ölüp gidenleri birlikte anarak aşırı yalancılığı anlatan söz
  درج الشيء إذا مضى لسبيله؛ درج الرجل إذا مضى ولم يخلف نسلا (maqayis)؛ درج قرن بعد قرن أي فنوا (ayn)؛ درج أي مات وانقرض؛ درج الرجل إذا لم يخلف نسلا وليس كل من مات درج (jamhara)؛ درج القوم إذا انقرضوا؛ أكذب الأحياء والأموات (sihah)؛ درج قرن بعد قرن أي فنوا؛ يقال للقوم إذا انقرضوا درجوا (tahdhib)؛ استعير الدرج للموت؛ من مات فطوى أحواله (mufradat)
- **B005** katlayıp içine sararak kapatma — bir yoruma göre onları kitap gibi dürüp kapatacağız · belgeyi katladı veya katının içine yerleştirdi · ölüyü kefenlerine sardı · bükümleri birbirine geçmiş sıkı nesne
  أصل آخر يدل على ستر وتغطية؛ أدرجت الكتاب وأدرجت الحبل (maqayis:درج)؛ المحدرج المفتول حتى يتداخل بعضه في بعض؛ درج من أدرجت (maqayis:المحدرج)؛ أدرجت الكتاب وفي درج الكتاب كذا (ayn)؛ درجت الشيء وأدرجته إذا طويته (jamhara)؛ أدرجت الكتاب طويته؛ في درج الكتاب أي في طيه (sihah)؛ أدرجت الكتاب إدراجا؛ الإدراج لف الشيء في الشيء؛ أدرج الميت في أكفانه؛ أدرجت الكتاب في الكتاب إذا جعلته في درجه أي في طيه (tahdhib)؛ الدرج طي الكتاب والثوب؛ يقال للمطوي درج (mufradat)
- **B006** eşya koymaya yarayan kutu veya kap — özellikle güzel koku ve kişisel araçlar için kullanılan küçük eşya kutusu
  الدرج لبعض الأصونة والآلات أصل آخر يدل على ستر وتغطية (maqayis)؛ الدرج حفش من أحفاش النساء (ayn)؛ الدرج سفيط صغير تجعل فيه المرأة طيبها (jamhara)؛ الدرج الذي يكتب فيه؛ الدرج بالضم حفش النساء (sihah)؛ الدرج درج المرأة تضع فيه طيبها وأداتها وهو الحفش (tahdhib)؛ الدرج سفط يجعل فيه الشيء (mufradat)
- **B007** yabancı yavruyu benimseten sarılı bez — dişi deveye başka yavruyu benimsetmek için kullanılan sarılı bez
  الدرجة خرق تجعل في حياء الناقة ثم تسل فإذا شمتها الناقة حسبتها ولدها فعطفت عليه (maqayis)؛ الدرجة خرقة تدرج فتجعل في حياء الناقة إذا ظئرت (ayn)؛ الدرجة خرق تلف وتدخل في حياء الناقة تعالج بها (jamhara)؛ الدرجة شيء يدرج فيدخل في حياء الناقة ثم تشمه فتظنه ولدها فترأمه (sihah)؛ الخرق التي تدرج إدراجا وتلف وتدس في حياء الناقة يقال لها الدرجة (tahdhib)؛ الدرجة خرقة تلف فتدخل في حياء الناقة (mufradat)
- **B008** doğum zamanı bakımından nitelenen dişi deve — doğum zamanıyla ilişkisi kaynaklara göre farklı açıklanan gebe dişi deve
  المدراج الناقة تضمر حتى يلحق حقبها بالتصدير؛ المدراج أيضا الناقة لا تجاوز يومها الذي ضربت فيه حتى تنتج والتي تجاوز يقال لها الجرور (ayn)؛ ناقة مدراج إذا تأخرت عن وقت ولادها أياما (jamhara)؛ درجت الناقة وأدرجت إذا جازت السنة ولم تنتج فهي مدراج (sihah)؛ ناقة مدراج إذا كانت تؤخر جهازها؛ المدراج الناقة التي تجر الحمل إذا أتت على مضربها (tahdhib)
- **B009** belirli bir kuş türü — yürüyüşü veya rengiyle betimlenen belirli bir kuş türü
  الدراج من الطير بمنزلة الحيقطان من طير العراق أرقط (ayn)؛ الدراج ضرب من الطير أحسبه مولدا (jamhara)؛ الدرجة طائر أسود باطن الجناحين؛ الدراج الدراجة ضرب من الطير (sihah)؛ الدرجة طائر أسود باطن الجناحين؛ الدراج من الطير بمنزلة الحيقطان (tahdhib)؛ الدراج طائر يدرج في مشيته (mufradat)

## خ ي ر (root_000452): 43:32 خَيْرٌ, 43:52 خَيْرٌ, 43:58 خَيْرٌ

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

## ج م ع (root_000259): 43:32 يَجْمَعُونَ, 43:55 أَجْمَعِينَ

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

## و ح د (root_001631): 43:33 وَٰحِدَةً

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

## ب ي ت (root_000166): 43:33 لِبُيُوتِهِمْ, 43:34 وَلِبُيُوتِهِمْ

- **B001** barınak mesken — ev, mesken, barınak · gece kalınan yer · Tanri'nin evi veya eski ev diye anılan kutsal yer · orumcegin yuvası
  أصل واحد وهو المأوى والمآب ومجمع الشمل (maqayis)؛ البيت معروف (jamhara;sihah)؛ البيت سمي بيتا لأنه يبات فيه (tahdhib)؛ أصل البيت مأوى الإنسان بالليل (mufradat)
- **B002** hane halkı [kalıp] — ev halkı, haneye bağlı kimseler · erkeğin ailesi, hane halkı veya mecazen eşi
  البيت عيال الرجل والذين يبيت عندهم (maqayis)؛ امرأة الرجل بيته (jamhara;tahdhib)؛ أهل البيت (mufradat)؛ غير بيت من المسلمين إشارة إلى جماعة البيت (mufradat)
- **B003** şiir dizesi [kalıp] — ölçülü şiir dizesi
  لبيت الشعر بيت على التشبيه لأنه مجمع الألفاظ والحروف والمعاني (maqayis)؛ سمي البيت من الشعر بيتا لضمه الحروف والكلام (jamhara)؛ بيت شعر كتبه بالقلم (sihah)؛ كلام جمع منظوما (tahdhib)؛ الأبيات بالشعر (mufradat)
- **B004** geceleyin yapmak — geceleyin yapmak veya gece boyunca uğraşmak · bir işi gece tasarlamak veya planlamak · düşmana gece baskını yapmak · gece vakti geliş
  بيت الأمر إذا دبره ليلا (maqayis;sihah)؛ البيات والتبييت أن تأتي العدو ليلا (maqayis)؛ بيت القوم إذا أوقعت بهم ليلا (jamhara)؛ بات يفعل كذا إذا فعله ليلا (sihah)؛ كل ما فكر فيه أو خيض فيه بليل فقد بيت (tahdhib)؛ البيات والتبييت قصد العدو ليلا (mufradat)
- **B005** bir gecelik azık [kalıp] — bir gecelik yiyecek veya azık
  ما لفلان بيته ليلة أي ما يبيت عليه من طعام وغيره (maqayis)؛ ماله بيت ليلة وبيته ليلة أي قوت ليلة (sihah)؛ ما عند فلان بيت ليلة وبيتة ليلة أي ما عنده قوت ليلة (tahdhib)
- **B006** gece beklemiş şey [kalıp] — gece kapta beklemiş veya soğumuş su ya da sut · bayat haber, taze olmayan haber
  البيوت الماء الذي يبيت ليلا (maqayis)؛ ماء بيوت إذا بات ليلة في إنائه (jamhara)؛ خبر بائت وكذلك البيوت (sihah)؛ بيوت السقاء أي من لبن حلب ليلا وحقن في السقاء (tahdhib)؛ الماء إذا برد في المزادة ليلا بيوت (tahdhib)
- **B007** mezar evi [kalıp] — ev diye anılan mezar
  البيت القبر (jamhara)؛ وإنما أراد بالبيت القبر (tahdhib)
- **B008** soylu hane [kalıp] — kabilenin şerefi, soylu hanesi
  البيت من بيوتات العرب الذي يجمع شرف القبيلة (jamhara)؛ بيت العرب شرفها (tahdhib)؛ بيت تميم في بني حنظلة أي شرفها (tahdhib)
- **B009** bitişik komşu [kalıp] — ev eve bitişik komşum
  فلان جاري بيت بيت أي ملاصقا (sihah)؛ هو جاري يبت بيت وبيتا لبيت وبيت لبيت (tahdhib)
- **B010** evlenip zifafa girmek [kalıp] — erkeğin evlenmesi · eşi için ev kurup zifafa girmek
  بات الرجل يبيت بيتا إذا تزوج (tahdhib)؛ بنى فلان على امرأته بيتا إذا أعرس بها (tahdhib)

## س ق ف (root_000720): 43:33 سُقُفًا

- **B001** üst örtüsü; benzetmeyle gök — çatı; bir yapının veya şeyin üst örtüsü · gök, yeryüzünün çatısıdır · eve çatı yapmak
  السقف سقف البيت لأنه عال مطل (maqayis)؛ السقف عماد البيت والسماء سقف فوق الأرض (ayn)؛ السقف للبيت والسقف السماء (sihah)؛ السقف غماء البيت والسماء سقف فوق الأرض (tahdhib)؛ سقف البيت وجعل السماء سقفا (mufradat)
- **B002** üstü örtülü yapı bölümü — üstü örtülü yer veya yapı bölümü
  السقيفة الصفة (maqayis;sihah)؛ السقيفة كل بناء سقف به صفة أو شبه صفة مما يكون بارزا (ayn;tahdhib)؛ السقيفة كل مكان له سقف كالصفة والبيت (mufradat)
- **B003** geniş çatı parçası ve benzeri destekler — çatı yapmaya elverişli geniş tahta veya taş · geniş tahtalar, kaburgalar veya sabitleme çubukları
  السقيفة كل لوح عريض في بناء إذا ظهر من حائط (maqayis)؛ السقيفة كل خشبة عريضة كاللوح وحجر عريض يستطاع أن يسقف به (ayn;tahdhib)؛ السقائف ألواح السفينة (sihah)؛ سقائف جنب البعير أضلاعه وعيدان المجبر (tahdhib)
- **B004** uzun ve eğik olma — uzunlukla birlikte eğiklik · uzun ve eğilmiş adam · uzun ve sarkık sakal
  الأسقف من الرجال وهو الطويل المنحني (maqayis)؛ لحي سقف أي طويل مسترخ والسقف بالتحريك طول في انحناء (sihah)؛ الأسقف الطويل والأسقف المنحني (tahdhib)؛ السقف طول في انحناء تشبيها بالسقف (mufradat)
- **B005** üst düzey Hristiyan din önderi — üst düzey Hristiyan din önderi
  الأسقف رأس من رؤوس النصارى ويجمع أساقفة (ayn;tahdhib)؛ اشتق أسقف النصارى لأنه يتخاشع وهو رئيس من رؤسائهم في الدين (sihah)

## ف ض ض (root_001162): 43:33 فِضَّةٍ

- **B001** parçalarını ayırarak kırmak — bir şeyi parçalarını ayırarak kırmak · yazının mührünü kırıp açmak · Tanrı dişlerini dökmesin · toprak keseklerini kırmaya yarayan alet · kırılıp dağılmak
  فضضت الشيء إذا فرقته (maqayis)؛ فضضت الخاتم من الكتاب كسرته؛ الفض كسر الأسنان (ayn)؛ فضضت الشيء إذا كسرته أو فرقته ولا يكون إلا الكسر بالتفرقة نحو فضضت الختام (jamhara)؛ الفض الكسر بالتفرقة وفضضت ختم الكتاب ولا يفضض الله فاك (sihah)؛ فضضت الخاتم من الكتاب أي كسرته؛ لا يفضض الله فاك؛ معناه لا يسقط الله أسنانك (tahdhib)؛ الفض كسر الشيء والتفريق بين بعضه وبعضه كفض ختم الكتاب (mufradat)
- **B002** topluluğu dağıtmak veya toplulukça dağılmak — topluluğu dağıtmak · toplulukça dağılıp gitmek · hizmet topluluğunuzu dağıtmak
  انفض القوم تفرقوا (maqayis)؛ الفض تفريقك حلقة من الناس بعد اجتماع؛ فضضتهم فانفضوا (ayn)؛ الانفضاض التفرق وانفض القوم وارفضوا إذا تفرقوا (jamhara)؛ فضضت القوم فانفضوا أي فرقتهم فتفرقوا (sihah)؛ تفريقك حلقة من الناس بعد اجتماعهم؛ فضضتهم فانفضوا؛ لانفضوا من حولك أي تفرقوا (tahdhib)؛ عنه استعير انفض القوم (mufradat)
- **B003** gümüş — gümüş · gümüş kakmalı gem
  وممكن أن يكون الفضة من هذا الباب (maqayis)؛ الفضة وتجمع على فضض (ayn)؛ الفضة معروفة (jamhara)؛ الفضة معروفة ولجام مفضض أي مرصع بالفضة (sihah)؛ الفضة معروفة؛ قوارير من فضة (tahdhib)؛ الفضة اختصت بأدون المتعامل بها من الجواهر (mufradat)
- **B004** kırılıp saçılan parçalar — bir şey kırılınca ondan ayrılan parçalar · kırıntı ve dağınık kalıntı · sen ondan kopmuş bir parçasın · parçalanıp dağılmak
  الفضاض ما تفضض من الشيء إذا انفض (maqayis)؛ كل شيء تفرق من شيء تكسر فهو فضاضة؛ فضض من لعنة الله (jamhara)؛ فضاض الشيء ما تفرق منه عند كسرك إياه؛ كل شيء تفرق فهو فضض؛ أنت فضض من لعنة الله (sihah)؛ أنت فضض منه أرادت أنك قطعة منه (tahdhib)
- **B005** geniş ve bol olmak — giysi, zırh veya yaşayışta genişlik ve bolluk · bol ve geniş giysi · geniş zırh · ferah ve bolluk içindeki yaşayış · çok su taşıyan bulut · uzun, iri yapılı ve eti dolgun genç kadın · çok veren, eli açık adam · idrarın dişi devenin butlarına yayılması
  الفضفضة سعة الثوب وثوب فضفاض ودرع فضفاضة (maqayis)؛ الفضفضة سعة الثوب ودرع فضفاضة واسعة وسحابة فضفاضة كثيرة الماء (ayn)؛ الفضفضة سعة الثوب والدرع والعيش؛ ثوب فضفاض وعيش فضفاض ودرع فضفاضة (sihah)؛ الفضفاضة الدرع الواسعة؛ قميص فضفاض واسع؛ جارية فضفاضة كثيرة اللحم؛ رجل فضفاض كثير العطاء؛ تفضفض البول (tahdhib)؛ درع فضفاضة وفضفاض واسعة (mufradat)
- **B006** tatlı ve akıcı su — tatlı, akıcı ve içimi kolay su · suya çıktığı ilk anda erişmek · temizlenirken çevreye yayılan su
  الفضيض الماء العذب سمي لفضاضته وسهولة مره في الحلق (maqayis)؛ الفضيض ماء عذب تصيبه ساعة يخرج (ayn)؛ الفضيض الماء العذب؛ افتضضت الماء إذا أصبته ساعة يخرج؛ الفضيض الماء السائل (sihah)؛ الفضيض الماء السائل؛ فضض الماء ما انتشر منه إذا تطهر به (tahdhib)
- **B007** dağıtıcı büyük felaket — dağıtıp perişan eden büyük felaket
  الفاضة الداهية والجمع فواض كأنها تفض أي تفرق (maqayis)؛ الفاضة الداهية (sihah)
- **B008** ilk alan olup el değmemiş durumunu sona erdirmek — bir şeyi ilk alan olup el değmemiş durumunu sona erdirmek · kadın kölesiyle ilk kez cinsel ilişkiye girmek · bekleme süresinde mahrem yerini bezle silip bezi atmak
  افتضضته أي كنت أول من أخذ منه كما يفتض الرجل المرأة (ayn)؛ افتض فلان جاريته واقتضها إذا افترعها (tahdhib)؛ تفتض بها؛ وهو من فضضت الشيء أي كسرته (tahdhib)

## ع ر ج (root_000997): 43:33 وَمَعَارِجَ

- **B001** bacağındaki bozukluk yüzünden aksamak — bacağındaki bozukluk yüzünden aksak hale gelmek ve aksayarak yürümek · bacakta aksaklık ve aksayarak yürüme durumu · bacağında aksaklık bulunan kimse · bacakta aksaklığın bulunduğu yer veya bıraktığı iz · yaradılışındaki aksaklığa benzer özellik nedeniyle böyle anılan sırtlan · sağır sayılan, efsuna tepki vermeyen ve sıçrayarak ilerleyen bir yılan türü · idrar yolu bozukluğu yüzünden idrarı düzgün çıkmayan deve
  العرج مصدر الأعرج إذا صار أعرج (maqayis); عرج الأعرج يعرج عرجا والأنثى عرجاء (ayn); عرج الرجل إذا صار أعرج (jamhara); عرج إذا أصابه شيء في رجله فخمع ومشى مشية العرجان (sihah); العرج مصدر عرج الرجل إذا صار أعرج (tahdhib); العروج ذهاب في صعود وعرج عروجا وعرجانا مشى مشي العارج (mufradat); العرجاء الضبع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat); الأعيرج حية صماء لا تقبل الرقية (ayn;jamhara;tahdhib)
- **B002** düz doğrultudan sapıp kıvrılmak — yolun düz doğrultudan sapıp kıvrılması · vadi ya da nehir yatağının sağa veya sola döndüğü kıvrım · düzene girmemiş, sonuca bağlanmamış veya karışık iş · yapıyı eğip kıvrımlı hale getirmek
  يقال للطريق إذا مال انعرج وانعرج الوادي ومنعرجه حيث يميل يمنة ويسرة (maqayis); انعرج الطريق إذا مال وكذلك عرج الوادي والنهر ومنعرجه حيث يميل يمنة ويسرة (jamhara); عرج البناء تعريجا أي ميله فتعرج وانعرج الشيء أي انعطف ومنعرج الوادي منعطفه (sihah); يقال للطريق إذا مال قد انعرج وانعرج الوادي ومنعرجه حيث يميل يمنة ويسرة (tahdhib); أمر عريج إذا لم يستقم (maqayis;sihah;tahdhib)
- **B003** ilerleyişi kesip durarak bir süre kalmak — birine yönelip bineğini yanında durdurmak ve orada kalmak · bizi bu yerde indirip burada konaklayın · onun yanında durup oyalanmam veya kalmam söz konusu değil · aşırı yükselme yönündeki gidişini biraz durdur
  التعرج حبس المطايا في مناخ أو موقف وعرجت عليه أي حبست مطيتي عليه (maqayis); عرجت على فلان أي عطفت عليه وعرجوا بنا في هذا المكان أي انزلوا بنا فيه وما لي عليه عرجة ولا تعريج ولا معرج أي تلبث (jamhara); التعريج على الشيء الإقامة عليه وعرج فلان على المنزل إذا حبس مطيته عليه وأقام (sihah); التعريج أن تحبس مطيتك مقيما على رفقتك أو لحاجة (tahdhib); عرج قليلا عن مدى غلوائك أي احبسه عن التصعد (mufradat)
- **B004** bir yol veya basamak boyunca yukarı çıkmak — basamakta veya merdivende yukarı çıkmak · yukarı doğru çıkma ve yükselme · yukarı çıkılan yol veya yükselen güzergâh · yukarı çıkmaya yarayan merdiven veya basamaklı düzenek · yukarı çıkılan yollar, basamaklar veya yükselme düzenekleri · güneşin gözden kaybolması veya batıya yönelerek batması
  العروج الارتقاء وعرج يعرج عروجا ومعرجا والمعرج المصعد (maqayis); عرج في الأدرجة إذا صعد فيها يعرج عروجا والمعارج معارج الملائكة إلى السماء (jamhara); عرج في الدرجة والسلم يعرج عروجا إذا ارتقى والمعراج السلم والمعارج المصاعد والعرج غيبوبة الشمس (sihah); عرج يعرج عروجا ومعرجا والمعرج المصعد والطريق الذي تصعد فيه الملائكة والمعراج شبه سلم أو درجة والعرج غيبوبة الشمس (tahdhib); العروج ذهاب في صعود والمعارج المصاعد (mufradat)
- **B005** sayısı kesin olmayan büyük deve sürüsü — sayısı kaynaklara göre değişen büyük deve sürüsü · büyük bir deve sürüsüne sahip olmak · sana büyük bir deve sürüsü bağışladım
  من الإبل ثمانون إلى تسعين والجمع عروج وأعراج ويقال العرج مائة وخمسون (maqayis); العرج من الإبل ثمانون إلى تسعين ويقال القطيع الضخم من الإبل نحو خمس مائة (ayn); العرج القطعة من الإبل ما بين ثلاثمائة إلى الألف (jamhara); العرج القطيع من الإبل نحو من الثمانين ومائة وخمسون وخمسمائة إلى الألف والجمع أعراج (sihah); العرج الكثير من الإبل وإذا جاوزت الإبل المائتين وقاربت الألف فهي عرج وعروج وأعراج (tahdhib); العرج قطيع ضخم من الإبل كأنه قد عرج كثرة أي صعد (mufradat)
- **B006** develeri gün aşırı değişen vakitlerde sulama düzeni — develerin bir gün sabah, başka bir gün akşam ya da öğle sulandığı dönüşümlü düzen · her gün yalnızca bir kez yemek · canlıların sıcaktan korunacak yere yöneldiği sıcak vakit için ileri sürülen koşullu adlandırma
  العريجاء الهاجرة وإن صح هذا فلأن كل شيء ينعرج إلى مكان يقيه الحر وأن ترد الإبل يوما غدوة ويوما عشية (maqayis); العريجاء ظمء من أظماء الإبل وهو أن تشرب يوما بالغداة ويوما بالعشي (jamhara); العريجاء في الورد أن ترد الإبل يوما نصف النهار ويوما غدوة (sihah); إذا وردت الإبل يوما نصف النهار ويوما غدوة فتلك العريجاء ويقال إن فلانا ليأكل العريجاء إذا أكل كل يوم مرة واحدة (tahdhib)
- **B007** aktarılmış yer ve topluluk adları — bilinen belirli bir tepenin adı · belirli bir yerin adı · Hicaz bölgesinde, Mekke yolu üzerinde ve Mekke ile Medine arasında bulunduğu belirtilen konak yeri · Araplar içindeki belirli bir topluluğun adı · Araplar içindeki belirli bir alt topluluğun adı
  العرجاء هضبة معروفة (maqayis); العريجاء موضع والعرج موضع بالحجاز معروف وبنو الأعرج حي وبنو عريج بطن (jamhara); العرج منزل بطريق مكة وإليه ينسب العرجي (sihah); العرج منزل بين مكة والمدينة (tahdhib)

## ب و ب (root_000163): 43:34 أَبْوَٰبًا

- **B001** giriş yeri veya kapı — giriş yeri veya kapı · kapılar · yalnız söz eşlemesi içinde kullanılabilen ve tek başına kullanılamayan kısıtlı çoğul biçimi
  الباب أصل ألفه واو (maqayis)؛ الباب معروف (ayn)؛ الباب يجمع أبوابا (sihah)؛ الباب يقال لمدخل الشيء (mufradat)
- **B002** bölümlere ayırıp düzenleme — bölümlere veya sınıflara ayırıp düzenleme · sınıflandırılmış, düzenlenmiş bölümler
  الفعل منه التبويب (ayn)؛ أبواب مبوبة كما يقال أصناف مصنفة (sihah)
- **B003** kapı görevlisi; kapı görevlisi tutma — kapı görevlisi tutmak · kapıda giriş çıkışı gözeten görevli
  تبوبت بوابا أي اتخذت بوابا (maqayis)؛ البواب الحاجب (ayn)؛ تبوبت بوابا اتخذته (sihah)
- **B004** son sınır veya sınır yeri — sınır veya hesapta ulaşılan son nokta · Bizans sınırlarındaki bir sınır yeri · Hazar sınırlarındaki özel adlı bir yer
  البابة في الحدود والحساب ونحوه الغاية؛ البابة ثغر من ثغور الروم؛ باب الأبواب من ثغور الخزر
- **B005** çöl düzlüğü ve belirli yer adları — Karn'dan Taif'e uzanan güzergâhta ilk görünen yer · geniş, ıssız çöl düzlüğü · Bahreyn'de bu adla bilinen yer
  البوباة مكان وهو أول ما يبدو من قرن إلى الطائف (maqayis)؛ البوباة الفلاة وهي الموماة (ayn)؛ بالبحرين موضع يعرف ببابين (ayn)
- **B006** dolaşarak su dağıtan görevli — Basra pazarlarında dolaşarak su dağıtan görevli
  يسمون الساقي الذي يطوف عليهم بالماء بيابا
- **B007** kişiye uygun şey — bu sana uygun veya senin işine yarayan bir şey
  هذا شيء من بابتك أي يصلح لك

## س ر ر (root_000697): 43:34 وَسُرُرًا, 43:80 سِرَّهُمْ

- **B001** saklama ve gizli paylaşım — gizlenen bilgi veya durum · kişinin gizli iç durumu veya gizlice yaptığı iş · bir şeyi gizleyip saklamak · birine bir sözü gizlice açmak · kulağına gizlice söylemek · kendi aralarında gizlice konuşmak · gizlice konuşmaya yarayan tomar benzeri araç
  السر خلاف الإعلان (maqayis)؛ السر ما أسررت والسريرة عمل السر (ayn)؛ السر الذي يكتم والسريرة مثله (sihah)؛ الإسرار خلاف الإعلان والسر هو الحديث المكتم في النفس (mufradat)؛ ساره في أذنه وتساروا (sihah)
- **B002** açığa vurma, tartışmalı kullanım — 
  أسررته أعلنته (maqayis)؛ أسررت الشيء أظهرته وكتمته أيضا (jamhara)؛ أسررت الشيء كتمته وأعلنته أيضا (sihah)؛ قال الفراء أخطأ أبو عبيدة (maqayis)؛ لم أسمع ذلك لغيره (tahdhib)
- **B003** gizli tutulan evlilik veya cinsel ilişki — 
  السر وهو النكاح (maqayis)؛ السر الجماع والسر الذكر (sihah)؛ السر النكاح والزنى وخطبة المعتدة (tahdhib)؛ كني عن النكاح بالسر من حيث إنه يخفى (mufradat)
- **B004** ayın görünmediği ay sonu — ayın sonunda hilalin görünmediği bir veya iki günlük dönem · ayın son gecesi
  السرار ليلة يستسر الهلال (maqayis)؛ السرار يوم يستسر فيه الهلال آخر يوم من الشهر (ayn)؛ سرر الشهر آخر ليلة منه وكذلك سراره (sihah)؛ السرار اليوم الذي يستتر فيه القمر آخر الشهر (mufradat)
- **B005** bir şeyin arı özü veya en seçkin bölümü [kalıp] — bir şeyin katkısız özü · topluluğunun merkezindeki en seçkin kesim · soyun katkısız ve en seçkin kolu · vadinin toprağı en iyi veya en elverişli yeri · bir şeyin özü ve üstün niteliğinin çekirdeği
  السر خالص الشيء وسر النسب (maqayis)؛ سر كل شيء خالصه وسر الوادي وسراره أطيبه ترابا (jamhara)؛ في سر قومه أي في أوسطهم وسر الوادي أفضل موضع (sihah)؛ استعير للخالص ومنه سر الوادي وسرارته (mufradat)
- **B006** göbek ve kesilen göbek bağı parçası — göbek · bebekten kesilen göbek bağı parçası · bebeğin göbek bağı parçasını kesmek
  السرة سرة الإنسان (maqayis)؛ السرة في البطن موضع السرر الذي يقطع من الصبي (jamhara)؛ السر ما تقطعه القابلة من سرة الصبي (sihah)؛ سرة البطن ما يبقى بعد القطع والسر والسرر لما يقطع منها (mufradat)
- **B007** devede gövde içi ağrı hastalığı — devede göbek, göğüs veya göğüs altı ağrısı · bu gövde ağrısına tutulmuş deve
  السرر داء يأخذ البعير في سرته (maqayis)؛ السرر داء يصيب الإبل في صدورها (jamhara)؛ بعير أسر وناقة سراء (sihah)؛ وجع يأخذ في الكركرة (tahdhib)
- **B008** içi oyuk olma ve oyuğa çubuk yerleştirme — ateş çubuğunun oyuğuna tutuşturma çubuğu yerleştirmek · içi oyuk boru biçimli çubuk · içi oyuk kişi
  سررت الزند وذلك أن يبقى أسر أي أجوف (maqayis)؛ قناة سراء أي جوفاء (maqayis)؛ سر زندك فإنه أسر أي أجوف (sihah)؛ رجل أسر إذا كان أجوف (tahdhib)
- **B009** avuç ve alın çizgileri — avuç içi çizgileri · alın veya yüz çizgileri ve kırışıklıkları
  الأسرار خطوط باطن الراحة (maqayis)؛ السر والسرار والجميع الأسرار خطوط راحة الكف (ayn)؛ السرر واحد أسرار الكف والجبهة (sihah)؛ أسرة الراحة وأسارير الجبهة (mufradat)
- **B010** sevinç ve gönence — üzüntüden uzak iç sevinci · beni sevindirdi · rahatlık, bolluk ve gönence · iyilik eden ve sevindiren kişi
  السرور أمر خال من الحزن (maqayis)؛ السر ضد الضر وقال قوم السر والسرور واحد (jamhara)؛ السراء الرخاء نقيض الضراء (sihah)؛ السرور ما ينكتم من الفرح (mufradat)
- **B011** oturma, yaslanma veya dinlenme yeri — oturulan, yaslanılan veya yatılan yer · başın dayandığı yer · yaşamın yerleşik rahatlığı ve dinginliği
  السرير وجمعه سرر وأسرة (maqayis)؛ سرير الرأس مستقره (maqayis)؛ السرير معروف والعدد أسرة والجميع السرر (tahdhib)؛ السرير الذي يجلس عليه من السرور (mufradat)
- **B012** bitkinin nemli üst bölümleri [kalıp] — bitkilerin nemli uçları veya gövdelerinin üst yarıları
  أطراف الريحان تسمى سرورا لأنها أرطب شيء فيه (maqayis)؛ السرور من النبات أنصاف سوقها العلى (tahdhib)
- **B013** yer mantarı üzerindeki kabuk ve toprak [kalıp] — yer mantarı üzerindeki kabuk, çamur ve toprak
  السرر ما على الكمأة من القشور والطين (sihah)؛ السرار ما على الكمأة من القشور والتراب (tahdhib)
- **B014** işlerin inceliğini bilen becerikli kişi — işlerin inceliğini bilen kavrayışlı kişi · sevdiğim ve çok yakın bulduğum kişi
  السرسور العالم الفطن (maqayis)؛ السرسور العالم الفطن الدخال في الأمور (sihah)؛ سرسور هذا الأمر إذا كان عالما به (tahdhib)؛ سرسوري وسرسورتي أي حبيبي وخاصتي (tahdhib)
- **B015** tepecik üzerindeki kum tabakası — küçük bir tepenin üzerindeki kum
  السري ما على الأكمة من الرمل (maqayis)

## و ك ء (root_001678): 43:34 يَتَّكِـُٔونَ

- **B001** kap agzini sikica baglayan bag — tulum ya da kap agzini sikica baglayan ip veya kayis · tulumu ya da kabi agiz bagiyla sikica baglamak
  الوكاء الذي يشد به (maqayis)؛ الوكاء كل سير أو خيط يشد به السقاء أو الوعاء (tahdhib)؛ الوكاء رباط الشيء (mufradat)
- **B002** vermekten kacinma veya agzini tutup susma — cimrilik edip vermekten kacinmak · elinden hicbir sey cikarmayan cimri · agzini tutup konusmamak · agzini kapa ve sus · iki yer arasinda konusmamak
  سألته فأوكى على أي بخل (maqayis)؛ فلان لوكاء ما يبض بشيء (maqayis)؛ يوكي فاه فلا يتكلم (tahdhib)؛ أوك حلقك أي شد فمك واسكت (tahdhib)
- **B003** arayi siddetli yuruyusle butunuyle katetme — iki yer arasini siddetli yuruyusle butunuyle katetmek · yuruyusunu sertlestirip kendini zorlayan kisi
  يوكى بين الصفا والمروة أي يملأ ما بينهما سعيا (maqayis)؛ الإيكاء في كلام العرب يكون بمعنى السعي الشديد (tahdhib)؛ الموكي الذي يتشدد في مشيه (tahdhib)؛ يملأ ما بينهما سعيا كما يوكى السقاء بعد الملء (mufradat)
- **B004** yaslanma, dayanak saglama ve yaslandirma — bir seye yaslanip ondan destek almak · bir seye dayanip yaslanmak · cok yaslanan kimse · yaslanilan sey · yaslanilan yer ya da dayanak · oturulan yer · birine yaslanacagi dayanak hazirlamak · birini destek uzerine koyup yaslandirmak · birini yaslanan kisi durusuna sokmak
  توكأت على كذا أي اتكأت (maqayis)؛ التوكؤ التحامل على العصا (ayn;tahdhib)؛ اتكأ على الشيء فهو متكئ والموضع متكأ (sihah)؛ أوكأت فلانا إيكاء إذا نصبت له متكأ (ayn;sihah;tahdhib)؛ توكأ على العصا اعتمد بها وتشدد بها (mufradat)
- **B005** cinsel birlesmeye siddetle ihtiyac duyma [kalıp] — cinsel birlesmeye siddetle ihtiyac duyan
  فلان موكي الغلمة ومزك الغلمة ومشط الغلمة إذا كانت به حاجة شديدة إلى الخلاط (tahdhib)
- **B006** dogum sancisinda devenin kivranmasi [kalıp] — devenin dogum sancisinda kivranip carpinmasi
  توكأت الناقة وهو تصلقها عند مخاضها (ayn;tahdhib)
- **B007** dolup dolgunlasma veya bosaltimin tutulmasi — develerin yaglanip dolgunlasmasi · insanin karninin tutulup diski cikaramamasi · tulumun ya da benzeri bir kabin dolmasi · kalin derili tulum agzi icin kullanilan, anlami belirsiz niteleme
  استوكت الإبل استيكاء إذا امتلأت سمنا (tahdhib)؛ استوكى بطن الإنسان وهو أن لا يخرج منه نجوه (tahdhib)؛ للسقاء ونحوه إذا امتلأ قد استوكى (tahdhib)

## ز خ ر ف (root_000628): 43:35 وَزُخْرُفًا

- **B001** süsleyip güzelleştirme — süs ve bezeme · süslenmiş, bezeli · onu süsledi · süsleme, bezeme · süslendi, özenle bezendi · Kâbe'yi süsleyen nakışlar ve resimler · yerin çiçeklerle güzelliğine kavuşması
  الزخرف الزينة وبيت مزخرف؛ تزخرف الرجل تزين (ayn)؛ المزخرف المزين (sihah)؛ الزخرف الزينة؛ بيت مزخرف وقد زخرفته زخرفة؛ تزخرف الرجل إذا تزين؛ أخذت الأرض زخرفها أي زينتها (tahdhib)؛ الزخرف الزينة المزوقة؛ أخذت الأرض زخرفها (mufradat)؛ الزخرف الزينة (maqayis)
- **B002** altın, özellikle süs değeriyle — altın; özellikle süs değeriyle anılan altın · bezeli altından yapılmış ev
  الزخرف الذهب (ayn)؛ الزخرف الذهب (sihah)؛ الزخرف الذهب؛ أصل الزخرف الذهب؛ زخرفا؛ الزخرف الذهب في غيره (tahdhib)؛ منه قيل للذهب زخرف؛ بيت من زخرف أي ذهب مزوق؛ وزخرفا (mufradat)؛ يقال الزخرف الذهب (maqayis)
- **B003** aldatıcı biçimde süslenmiş söz [kalıp] — aldatıcı biçimde süslenmiş söz
  يشبه به كل مموه مزور (sihah)؛ زخرف القول غرورا أي حسن القول بترقيش الكذب (tahdhib)؛ زخرف القول غرورا أي المزوقات من الكلام (mufradat)
- **B004** suyun yüzeyindeki çizgisel desenler [kalıp] — suyun yüzeyindeki çizgiler ve yol benzeri biçimler
  زخارف الماء طرائقه (sihah)؛ زخارف الماء طرائق تكون فيه (maqayis)
- **B005** gemi; bazı kullanımda bezeli gemi — gemi veya gemiler; bazı aktarımda bezeli gemiler
  الزخارف ما يزخرف من السفن (ayn)؛ الزخارف السفن (tahdhib)
- **B006** su üstünde uçan dört ayaklı küçük canlılar — su üstünde uçan, dört ayaklı, sineğe benzer küçük canlılar
  الزخارف دويبات تطير على الماء ذوات أربع مثل الذباب (ayn)؛ الزخارف دويبات تطير على الماء ذوات أربع مثل الذباب (tahdhib)

## ء خ ر (root_000019): 43:35 وَٱلْءَاخِرَةُ, 43:56 لِّلْءَاخِرِينَ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ع ن د (root_001052): 43:35 عِندَ, 43:49 عِندَكَ, 43:85 وَعِندَهُۥ

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

## و ق ي (root_001677): 43:35 لِلْمُتَّقِينَ, 43:63 فَٱتَّقُوا۟, 43:67 ٱلْمُتَّقِينَ

- **B001** araya engel koyarak zarardan koruma — bir şeyi koruyucu bir engelle zarardan saklamak · koruma; zararı önleyen araç veya engel · bir şeyi korumaya yarayan araç ya da engel · zarardan koruyan şey · zararı savan koruyucu · kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez · koruyucu şeyler
  دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)
- **B002** korkulan şeyden ya da yanlış davranıştan kendini koruma — kendini korkulan ya da zarar verecek şeyden korumak · bir şeyi kendine koruyucu yapmak · Tanrı'ya karşı gelmekten sakınmak · kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması · sakınma ve kendini koruma · sakınan ve kendini yanlış davranıştan koruyan kimse · sakınma; kendini kötülükten koruma · sakınıp kendini koruma · kendini yanlış davranışlardan koruyan kimse · sakınan ve kendini yanlış davranıştan koruyan kimse
  اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)
- **B003** hafif topallama ve toynak ağrısıyla yürümekten çekinme — hafif topallama · topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at · hayvanın sırtında yara açmayan eyer · aksayışını gözet ve ağırdan al
  الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)
- **B004** kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü — kırk gümüş para ağırlığına eşit bilinen ölçü · yağ için yedi temel ağırlık birimine eşit ölçü · bu ağırlık ölçüsü adının çoğul biçimleri
  الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)
- **B005** örümcek kuşu — örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri
  الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)

## ع ش و (root_001017): 43:36 يَعْشُ

- **B001** karanlık ve görüş açıklığının azalması — gecenin ilk karanlığı ve koyuluğu · gece karanlığı · gecenin başlangıç karanlığı; bilgisizliğin karanlığı
  يدل على ظلام وقلة وضوح في الشيء؛ العشاء وهو أول ظلام الليل (maqayis)؛ عشواء الليل ظلمته (maqayis)؛ مضى من الليل عشوة وهو ما بين أوله إلى ربعه (sihah)؛ أخذت عليهم بالعشوة أي بالسواد من الليل (sihah)؛ العشوة ظلمة الكفر وكلما ركب الإنسان أمرا بجهل لا يبصر وجهه فهو عشوة (tahdhib)
- **B002** gece kılavuz ateşe yönelme — gece ateşe, ışığından yol bularak yönelmek · gecenin başında yerini bildiği ailesine yönelmek · gece ateş ışığıyla yolunu bulmak · gece görünen alev ya da ateş · gece ateş ışığına gelen varlık
  عشوت إلى ناره ولا يكون ذلك إلا أن تخبط إليه الظلام (maqayis)؛ العاشية كل شيء يعشو بالليل إلى ضوء نار (maqayis)؛ عشوته قصدته ليلا (sihah)؛ عشوت إلى النار إذا استدللت عليها ببصر ضعيف (sihah)؛ عشا يعشو إذا أتى نارا للضيافة (tahdhib)؛ العشو إتيانك نارا ترجو عندها هدى أو خيرا (tahdhib)؛ استعشى فلان نارا إذا اهتدى بها (tahdhib)؛ العشوة أيضا الشعلة من النار (tahdhib)؛ عشوت النار قصدتها ليلا (mufradat)؛ النار التي تبدو بالليل عشوة (mufradat)
- **B003** görmezden gelip yüz çevirme — bilmezden gelme · bir işi bilmez ve görmez gibi davranmak · bir şeyden yüz çevirmek veya onu görmezden gelmek · birinin hakkını görmezden gelip ona haksızlık etmek
  التعاشي التجاهل في الأمر (maqayis)؛ عشوت عنه (sihah)؛ ومن يعش عن ذكر الرحمن (sihah)؛ تعاشى الرجل في أمري إذا تجاهل (tahdhib)؛ عشي الرجل عن حق أصحابه إذا ظلمهم (tahdhib)؛ عشي علي فلان ظلمني (tahdhib)؛ عشوت عنها أي أعرضت عنها (tahdhib)؛ عشي عن كذا نحو عمي عنه (mufradat)؛ ومن يعش عن ذكر الرحمن (mufradat)
- **B004** öğle sonrasından gecenin başına uzanan akşam vakti — öğle sonrasından gecenin başına uzanan akşam vakti · bir günün akşamı · gün batımından gecenin koyulaşmasına kadarki vakit; bu vakitteki gece namazı · gün batımı ve gecenin koyulaşma vakitleri · gün batımı namazından sonraki gece namazı · akşamcık; akşam sözünün küçültme biçimi
  العشي آخر النهار (maqayis)؛ فإذا قلت عشية فهو ليوم واحد (maqayis)؛ كل ما كان بعد الزوال فهو عشي (maqayis)؛ العشي والعشية من صلاة المغرب إلى العتمة (sihah)؛ العشاء بالكسر والمد مثل العشي (sihah)؛ العشاءان المغرب والعتمة (sihah)؛ صلاة العشاء هي التي بعد صلاة المغرب (tahdhib)؛ إذا زالت الشمس دعي ذلك الوقت العشي (tahdhib)؛ العشاء من صلاة المغرب إلى العتمة (mufradat)
- **B005** akşam yemeği ve akşam otlatması — günün sonunda veya gecenin başında yenen akşam yemeği · akşam yemeği yemek · birine akşam yemeği yedirmek · gece otlayan develer · develeri gece veya öğleden sonra otlatmak · Akşam otlayan sürü, otlamayanı da harekete geçirir.
  العشاء هو الطعام الذي يؤكل من آخر النهار وأول الليل (maqayis)؛ عشيت الإبل إذا تعشت فهي عاشية (sihah)؛ العواشي هي التي ترعى ليلا (sihah)؛ عشوت أي تعشيت (sihah)؛ عشوته فتعشى أي أطعمته عشاء (sihah)؛ عشيت الإبل إذا رعيتها بعد غروب الشمس إلى ثلث الليل (tahdhib)؛ عشيتها أيضا إذا رعيتها بعد الزوال إلى غروب الشمس (tahdhib)؛ عشيت الرجل إذا أطعمته العشاء (tahdhib)؛ العواشي الإبل التي ترعى ليلا (mufradat)؛ العشاء طعام العشاء (mufradat)
- **B006** körlüğe varmayan, özellikle gece belirginleşen görme zayıflığı — özellikle geceleri görülen görme zayıflığı · görmesi zayıf veya geceleri göremeyen kişi · görmesi zayıf kişiler · görmesi zayıfmış gibi davranmak · görmesi zayıf veya geceleri göremeyen kadın
  العشا مقصور مصدر الأعشى والمرأة عشواء (maqayis)؛ الذي لا يبصر بالليل وهو بالنهار بصير (maqayis)؛ العشا مصدر الأعشى وهو الذي لا يبصر بالليل ويبصر بالنهار (sihah)؛ العشو جمع الأعشى (tahdhib)؛ العشا يكون سوء البصر من غير عمى (tahdhib)؛ يكون الذي لا يبصر بالليل ويبصر بالنهار (tahdhib)؛ عشا يعشو إذا ضعف بصره (tahdhib)؛ العشا ظلمة تعترض في العين (mufradat)؛ رجل أعشى وامرأة عشواء (mufradat)
- **B007** önünü görmeden sonuç düşünmeksizin ilerleme — önünü göremeyip karşısına çıkanlara çarpan dişi deve · körlemesine ve sonucunu düşünmeden davranmak · bir işi ne yaptığını bilmeden yürütmek · birini doğru yönü belli olmayan bir işe sürüklemek
  العشواء من النوق التي كأنها لا تبصر ما أمامها فتخبط كل شيء بيديها (maqayis)؛ في عشواء من أمرهم (maqayis)؛ العشواء الناقة التي لا تبصر أمامها فهي تخبط بيديها كل شيء (sihah)؛ ركب فلان العشواء إذا خبط أمره على غير بصيرة (sihah)؛ العشوة أن تركب أمرا على غير بيات (sihah)؛ يخبط خبط عشواء يضرب مثلا للسادر الذي يركب رأسه ولا يهتم لعاقبته (tahdhib)؛ أوطأته عشوة حمله على أن يركب أمرا غير مستبين الرشد (tahdhib)؛ يخبط خبط عشواء (mufradat)
- **B008** bir şeye yumuşak ve özenli davranma — bir şeye yumuşak ve özenli davranmak
  عشيت عنه أيضا رفقت به (tahdhib)

## ق ي ض (root_001275): 43:36 نُقَيِّضْ

- **B001** çatlayan üst yumurta kabuğu ve nesnenin çatlayıp yarılması — yumurtanın üst kabuğu ve ondan çatlayarak ayrılan parçalar · düşmeden çatlamak veya uzunlamasına yarılmak · çatlayıp parçalara ayrılmak veya çatlama sonrasında düşmek · onu çatlatmak veya yarılmasına yol açmak
  القيض البيض قد خرج فرخه وماؤه كله (ayn)؛ فانقاضت أي انشقت (ayn)؛ انقاض الجدار انقياضا أي تصدع من غير أن يسقط (sihah)؛ تقيضت البيضة إذا انكسرت فلقا (sihah)؛ القيض ما تفلق من قشور البيض الأعلى (sihah)؛ استيلاء القيض على البيض وهو القشر الأعلى (mufradat)
- **B002** suyu bol kuyu [kalıp] — suyu bol kuyu
  وبئر مقيضة كثيرة الماء
- **B003** mal takası, karşılık verme ve birbirinin dengi olma — başkasıyla mal karşılığında mal takas etmek · karşılık; denk tutma · ikisi birbirinin dengi veya karşılığıdır · birine verdiğinin veya yaptığının karşılığını vermek
  أعطيته فرسا بفرسين قيضين؛ وقايضني وقايضته (ayn)؛ قايضت الرجل مقايضة أي عاوضته بمتاع؛ وهما قيضان (sihah)؛ هما قيضان أي مثلان؛ القيض العوض؛ القيض التمثيل؛ قاض يقيض إذا عاضه؛ المقايضة في البيع شبه المبادلة (tahdhib)
- **B004** Tanrı'nın birini başkası için ortaya çıkarıp erişilebilir kılması [kalıp] — Tanrı'nın birini bir başkası için ortaya çıkarıp ona erişilebilir kılması
  وقيض له قرين سوء كما قيض الشياطين للكفار (ayn)؛ قيض الله فلانا لفلان أي جاء به وأتاحه له (sihah)؛ قيض الله فلانا لفلان جاء به؛ نسبب له شيطانا؛ سببنا لهم من حيث لم يحتسبوه (tahdhib)؛ وقيضنا لهم قرناء؛ نقيض له شيطانا؛ أي نتح ليستولي عليه استيلاء القيض على البيض (mufradat)
- **B005** babasına çekmek [kalıp] — babasına benzemek, babasına çekmek
  تقيض فلان أباه أي أشبهه (sihah)؛ تقيض فلان أباه تقيله تقيضا وتقيلا إذا نزع إليه الشبه (tahdhib)
- **B006** ısıtılmış taşla hayvanı dağlayıp işaretleme ve damga taşı — hayvanlarını ısıtılmış taşla dağlayıp işaretlemek · hayvan damgalamak için ısıtılan taş · koyunun belirli bir noktasını dağlamada kullanılan küçük taş
  قيض إبله إذا وسمها بالقيض وهو حجر يحمى؛ القيضة حجير يكوى به نقرة الغنم

## ش ط ن (root_000796): 43:36 شَيْطَٰنًا, 43:62 ٱلشَّيْطَٰنُ

- **B001** uzaklaşma ve uzaklaştırma — uzaklaşmak, uzak olmak · uzaklaştırmak · evin uzakta kalması · uzaklara düşüren ayrılık · uzak sefer · yurttan çok uzakta kalış · dibi çok uzakta olan kuyu
  أصل مطرد صحيح يدل على البعد (maqayis)؛ شطن عنه بعد وأشطنه أبعده وبئر شطون بعيدة القعر ونوى شطون بعيدة (sihah)؛ غزوة شطون أي بعيدة وشطنت الدار شطونا إذا بعدت (tahdhib)؛ الشيطان من شطن أي تباعد (mufradat)
- **B002** uzun kuyu ipi ve onunla bağlama — su çekmeye yarayan uzun, sıkı bükülmüş ip · uzun ipler · uzun iple bağlamak · iki yanından iki iple bağlanmış at · iki ip arasında çırpınmak; azgın ve güçlü kişi için de söylenir · kuyudan kovayı iki iple çeken kişi
  الشطن الحبل وهو القياس لأنه بعيد ما بين الطرفين (maqayis)؛ الشطن الحبل الطويل الشديد الفتل يستقى به (ayn;tahdhib)؛ شطنته أشطنه إذا شددته بالشطن (sihah)؛ المشاطن الذي ينزع الدلو من البئر بحبلين (tahdhib)
- **B003** yönünden ayırma ve bağlama göre eğrilik ya da çetinlik — birini niyet ettiği yönden ayırmak · bir yana yatık kalça · kıvrımlı ve eğri kuyu · ağır ve çetin savaş · uzun ve eğri mızrak
  شطنه يشطنه شطنا إذا خالفه عن نية وجهه (sihah)؛ خالفه عن نيته ووجهه وألية شطون إذا كانت مائلة في شق وبئر شطون ملتوية عوجاء وحرب شطون عسرة شديدة ورمح شطون طويل أعوج (tahdhib)
- **B004** azgın ve başkaldıran kötü varlık — iyiden uzaklaşmış, azgın ve başkaldıran kötü varlık · insanlar, görünmez varlıklar veya hayvanlar arasındaki her azgın başkaldıran · azgın ve başkaldıran kötü varlık · kişinin kötücül varlık gibi olup onun yaptığını yapması · kişinin kötücül varlığa dönüşüp onun gibi davranması
  كل عات متمرد من الجن والإنس والدواب شيطان (maqayis;sihah)؛ الشيطان فيعال من شطن أي بعد وشيطن الرجل وتشيطن إذا صار كالشيطان وفعل فعله (tahdhib)؛ الشيطان اسم لكل عارم من الجن والإنس والحيوانات وسمي كل خلق ذميم للإنسان شيطانا (mufradat)
- **B005** çirkin yılan ve bitki adıyla ürkütücü baş benzetmesi — kötü varlık adı verilen çirkin görünüşlü yılan · çirkin bir yılanın ya da bitkinin başları; ürkütücü çirkinlik benzetmesi
  الحية تسمى شيطانا (maqayis)؛ العرب تسمي الحية شيطانا ونبت قبيح يسمى رءوس الشياطين (sihah)؛ بعض الحيات شيطانا وهو حية ذو عرف قبيح المنظر والشيطان نبت قبيح يسمى برؤوس الشياطين (tahdhib)؛ كأنه رؤوس الشياطين قيل هي حية خفيفة الجسم وقيل أراد به عارم الجن فتشبه به لقبح تصورها (mufradat)

## ص د د (root_000848): 43:37 لَيَصُدُّونَهُمْ, 43:57 يَصِدُّونَ, 43:62 يَصُدَّنَّكُمُ

- **B001** yüz çevirme ve alıkoyma — yüz çevirmek, uzaklaşmak · onu işten alıkoyup uzaklaştırmak · yüz çevirme, uzaklaşma
  الصَّدّ الإعراض؛ صددت فلانا عن الأمر إذا عدلته عنه (maqayis); صددته عن كذا أي عدلته عنه؛ صددت عنه بنفسي صُدودا (ayn); صد يصد صدا وصدودا إذا صدف عن الشيء أو أعرض عنه؛ أصددته عن ذلك الأمر إذا صرفته عنه (jamhara); صد عنه يصد صدودا أعرض؛ وصده عن الأمر منعه وصرفه عنه (sihah); صده يصده صدا؛ صددت فلانا عن أمره أصده صدا (tahdhib); الصدود والصد قد يكون انصرافا عن الشيء وامتناعا؛ وقد يكون صرفا ومنعا (mufradat)
- **B002** vadinin iki yanı — vadinin, yarın veya dağın iki yanı
  الصَّدان جانبا الوادي؛ الواحد صد (maqayis); الصَّدان ناحيتا الشعب أو الوادي (jamhara); الصَّدان ناحيتا الجبل؛ الصَّدان الجبلان (tahdhib)
- **B003** karşıda ve yakında bulunma — karşı, karşı taraf; yakınlık · ona yönelmek, karşısına çıkmak
  الصدد ما استقبل؛ الصدد القرب (maqayis); الصدد ما استقبلك؛ هذه الدار على صدد هذه أي قبالتها (ayn); الصدد القرب؛ داري صدد داره أي قبالتها (sihah); تتعرض له وتميل إليه وتقبل عليه؛ تصديت له أي أقبلت عليه؛ أصله من الصدد وهو ما استقبلك وصار قبالتك؛ تتقرب إليه (tahdhib)
- **B004** suya giden yol — suya giden yol
  الصَّداد الطريق إلى الماء (maqayis;sihah)
- **B005** engel oluşturan dağ — dağ; dağın engel olan bölümü
  الصَّدّ الجبل (maqayis;sihah); الصَّدّ من الجبل ما يحول (mufradat)
- **B006** yaygara koparmak — yaygara koparmak, gürültüyle gülmek
  صد يصد وذلك إذا ضج (maqayis); صد يصد صدا وهو شدة الضحك والجلبة؛ يصدون ويضحكون (ayn); يصدون يضجون (jamhara); صد يصد ويصد صديدا أي ضج (sihah); يضجون ويعجون؛ يضحكون (tahdhib)
- **B007** kanlı irinli yara akıntısı — kanla karışık irinli yara akıntısı · kan ve irinli akıntıdan oluşan özel içecek · yara irinlenmek
  الصديد الدم المختلط بالقيح؛ أصد الجرح (maqayis); الصديد الدم المختلط بالقيح في الجرح؛ أصد إصدادا؛ ما سال من أهل النار؛ الحميم أغلي حتى خثر (ayn); صديد الجرح ماؤه الرقيق المختلط بالدم قبل أن تغلظ المدة؛ أصد الجرح (sihah); الصديد ما يسيل من أهل النار من الدم والقيح؛ الدم المختلط بالقيح في الجرح؛ الحميم أغلي حتى خثر (tahdhib); الصديد ما حال بين اللحم والجلد من القيح وضرب مثلا لمطعم أهل النار (mufradat)
- **B008** türü tartışmalı küçük hayvan — sıçan ya da kertenkele sayılan küçük hayvan
  الصَّداد ضرب من الجرذان ويقال من دواب الأرض (ayn); الصَّداد الوزغ؛ الجمع صداديد (jamhara); الصَّداد دويبة وهي من جنس الجرذان؛ سام أبرص (sihah); الصَّداد سام أبرص؛ ضرب من الجرذان (tahdhib)
- **B009** bir kadın adı — bir kadın adı
  صد صد اسم امرأة (ayn); صدصد اسم امرأة (tahdhib)
- **B010** tatlı sulu bir kuyunun adı — bilinen bir suyun veya tatlı sulu kuyunun adı
  صداء ماء معروف (jamhara); صداء اسم ركية عذبة الماء؛ ماء ولا كصداء (sihah)
- **B011** alkışlamak — alkışlama, el çırpma
  صدى يصدي تصدية إذا صفق؛ وأصله صد ويصدد (tahdhib)
- **B012** kadın örtüsü — kadının örtündüğü örtü
  الصَّداد ما اصطدت به المرأة وهو الستر (tahdhib)
- **B013** aynada hazırlanmış göz boyası — aynaya sürtülüp göze uygulanan madde
  الصُّدود ما دلكته على مرآة ثم كحلت به عينا (tahdhib)

## ح س ب (root_000318): 43:37 وَيَحْسَبُونَ, 43:80 يَحْسَبُونَ

- **B001** sayarak nicelik belirleme — nesneyi saymak ve niceliğini çıkarmak · sayma ve nicelik belirleme işlemi · sayma işlemi · sayı yoluyla belirleme · belirli sayı düzeni ve zaman ölçüsü · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · sayıp değerlendiren ve gözeten
  الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان
- **B002** öyle olduğunu sanmak — öyle sanmak ve zihnen öyle olduğuna hükmetmek · sanı ve kesin olmayan yargı
  الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين
- **B003** gereksinimi karşılayacak kadar yetmek — bu sana yeter; bununla yetin · Tanrı bize yeter · bu bana yetti · ona yetecek veya onu hoşnut edecek kadar vermek · yeterli ya da bol armağan · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü
  الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا
- **B004** atalardan gelen saygınlık ve iyi işler birikimi — atalardan gelen saygınlık ve övünülecek işler · soylu, saygın veya eli açık kişi · soyluluk ya da yeterlik diye yorumlanan şiir sözü
  الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه
- **B005** Tanrı katında karşılığını beklemek — bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek · Tanrı katında karşılık umularak yapılan iş
  احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى
- **B006** işi gözetme, kötü davranışı sorgulama ve kamusal denetim — kötü davranışından dolayı kınamak ve yaptığını sorgulamak · işi iyi çekip çevirmek ve gözetmek · kentte kamu düzenini ve davranışları gözeten görevli
  حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر
- **B007** kısa ok veya yukarıdan gelen yıkıcı gönderim — kısa oklar veya atılan küçük nesneler · gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey
  الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا
- **B008** yalıtık adlandırmalar — küçük yastık · deriden yapılmış veya baş altına konan yastık · birini yastığa oturtmak veya başına yastık koymak · yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış
  الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة
- **B009** deri veya tüyde karışık ak, kızıl ve koyu görünüm — derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve · koyu zemin üstünde bozluk ya da kızıla çalan karalık
  الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة
- **B010** yalıtık adlandırmalar — haberi sorup izini sürmek · birinin elinde ne olduğunu sınayıp öğrenmek
  بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها

## ب ع د (root_000131): 43:38 بُعْدَ

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

## ش ر ق (root_000790): 43:38 ٱلْمَشْرِقَيْنِ

- **B001** doğmak, ışımak; doğu ve doğuya yönelmek — doğmak, doğu ufkundan yükselmek · ışımak, aydınlatmak · yüzü sevinç ve güzellikle ışıldamak · güneşin doğuşu · doğan, yükselen · doğu, güneşin doğduğu yön; bazı kullanımlarda güneş · güneşin doğduğu yer veya mevsimlere göre doğuş yerleri · doğuya ait, doğu tarafındaki · doğuya yönelme · güneşin doğduğu vakte girmek · güneş yükseldikten sonraki vakit; başka bir açıklamada ölüm anında tükürüğüne boğulma
  شرقت الشمس إذا طلعت (maqayis;sihah;mufradat)؛ وأشرقت إذا أضاءت (maqayis;sihah;mufradat)؛ الشرق خلاف الغرب (ayn)؛ المشرق والمغرب (mufradat)؛ مكانا شرقيا (mufradat)؛ التشريق الأخذ في ناحية المشرق (sihah)
- **B002** eti güneşte kurutmak [kalıp] — eti güneşe serip kurutma · kurban etlerinin güneşte kurutulduğu günler · eti güneş alan yere koymak
  لحوم الأضاحي تشرق فيها للشمس (maqayis;sihah)؛ تشريقهم اللحم في الشمس بمنى (ayn)؛ تشريق اللحم تقديده (sihah)؛ شرقت اللحم ألقيته في المشرقة (mufradat)
- **B003** rengin güçlenip doygunlaşması — kanı andıracak kadar kızarmak · utançtan yüzü kan kırmızısına dönmek · kırmızı boya · çok koyu kırmızı · kırmızı, yağsız et · safrana iyice doyurulmuş · suyu belli olan gür yeşil arazi
  اللحم الأحمر يسمى شرقا (maqayis)؛ شرق شرقا إذا حمرته بدم أو بحسن لون أحمر (ayn;tahdhib)؛ الشرقي الأحمر من الصبغ (ayn)؛ أحمر شارق شديد الحمرة (mufradat)؛ الشريق المشبع بالزعفران (tahdhib)؛ الشرقة الأرض الشديدة الخضرة الريا (tahdhib)
- **B004** koyunun kulağını yarıp ikiye ayırmak — koyunun kulağını yarmak · bir veya iki kulağı ikiye yarılmış koyun
  الشاة الشرقاء المشقوقة الأذن (maqayis)؛ شاة شرقاء مشقوقة الأذنين نصفين (ayn)؛ شرقت الشاة أشرقها أي شققت أذنها (sihah)
- **B005** suya, tükürüğe veya yiyeceğe boğulmak — tükürüğüne boğulmak · suya boğulmak, su içerken tıkanmak · boğaza takılma, boğulma · güneş yükseldikten sonraki vakit; başka bir açıklamada ölüm anında tükürüğüne boğulma
  شرق بالماء إذا غص به شرقا (maqayis)؛ شرق فلان بريقه والشرق كالغص بالطعام (ayn)؛ الشرق الشجا والغصة وشرق بريقه (sihah)؛ شرق فلان بريقه وكذلك غص بريقه (tahdhib)
- **B006** güneş alan oturma yeri ve bayram namazı alanı — güneş alan oturma yeri · güneş alan yerde oturmak · bayram namazı kılınan alan
  المشرقة متشرق القوم في الشمس (ayn)؛ المشرقة موضع القعود في الشمس (sihah)؛ تشرقت أي جلست فيه (sihah)؛ المشرقة المكان الذي يظهر للشرق (mufradat)؛ المشرق مصلى العيد (mufradat)

## ب ء س (root_000079): 43:38 فَبِئْسَ

- **B001** zorlayıcı sert güç — savaşta sert güç, ağır karşılık ve yıldırıcı zarar · savaşta cesur ve güçlü adam · sert gücü olan cesur kişi · ağır ve sert karşılık · çok ağır karşılık · savaş ve yıldırıcı sertlik
  البأس الشدة في الحرب (maqayis;sihah); رجل ذو بأس وبئيس أي شجاع (maqayis;ayn;sihah;tahdhib); البأس العذاب وعذاب بئيس أي شديد (sihah;tahdhib); البأس والبأساء في النكاية (mufradat)
- **B002** ağır geçim sıkıntısı — geçimde sert darlık, yoksulluk ve kötü hal · başına yoksunluk ya da kötü hal gelmiş acınacak kişi · adam yoksullaştı ve ihtiyacı ağırlaştı · güçlük, zarar ve açlık hali · yoksulluk · kötü günler ya da büyük yıkıcı durum · başına yoksulluk gelsin anlamında beddua · iyi halin karşıtı olan darlık · yoksullukla boyun eğme ya da kendini düşkün gösterme
  البؤس الشدة في العيش (maqayis); البأساء اسم للحرب والمشقة والضرر (ayn;tahdhib); بئس الرجل اشتدت حاجته فهو بائس (sihah); البائس الرجل النازل به بلية أو عدم (ayn;tahdhib); البأساء الجوع (tahdhib); الأبؤس الداهية (sihah); بؤسا له وتوسا وجوسا بمعنى واحد (tahdhib); البؤس والتباؤس والتبؤس أي الضراعة للفقر أو أن يجعل نفسه ذليلا (mufradat)
- **B003** üzülüp yakınma — hoşnutsuz ve üzgün kişi · hoşlanmadığı bir şey kendisine ulaştı ve üzüldü · üzülme ve yakınma
  المبتئس المفتعل من الكراهة والحزن (maqayis); لا تبتئس أي لا تحزن ولا تشتك (sihah); ابتأس الرجل إذا بلغه شيء يكرهه (tahdhib); غير حزين ولا كاره (tahdhib); لا تلزم البؤس ولا تحزن (mufradat)
- **B004** kötüleme sözü — övgünün karşıtı olan kötüleme sözü · sonrasındaki sözle birlikte kullanılan kötüleme kalıbı
  بئس نقيض صلح يجري مجرى نعم (ayn); بئس ضد نعم (jamhara); بئس كلمة ذم ونعم كلمة مدح (sihah); بئس مستوفية لجميع الذم (tahdhib); بئس كلمة تستعمل في جميع المذام (mufradat)
- **B005** sana zarar yok — sana zarar yok; güvendesin · sana zarar yok anlamındaki yerel söz
  إذا قال الرجل لعدوه لا بأس عليك فقد أمنه (tahdhib); لبات أي لا بأس (tahdhib)

## ن ف ع (root_001536): 43:39 يَنفَعَكُمُ

- **B001** zararın karşıtı olan ve iyiliğe ulaştıran yarar — zararın karşıtı olan, iyiliğe ulaşmaya yardım eden yarar · ona yarar sağladı · ondan yararlandı · yarar · yarar · yararlı · insanlara sürekli yarar sağlayan ve zarar vermeyen kişi
  النون والفاء والعين كلمة تدل على خلاف الضر (maqayis)؛ النفع ضد الضر (ayn;sihah;tahdhib)؛ نفعه نفعا وانتفعت بكذا (ayn)؛ نفعه ينفعه نفعا ومنفعة وانتفع بكذا (maqayis)؛ ما يستعان به في الوصول إلى الخيرات (mufradat)؛ ما عندهم نفيعة أي منفعة (tahdhib)؛ رجل نفاع إذا كان ينفع الناس ولا يضرهم (tahdhib)
- **B002** deri su kabının iki yanındaki yarılmış deri parçalardan biri — deri yarılarak su kabının iki yanına yerleştirilen parçalardan biri
  النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة (ayn)؛ النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة (tahdhib)
- **B003** değnek — değnek · değnek alıp satmak
  النَّفعة العصا وهي فعلة من النفع؛ أنفع الرجل إذا اتجر في النفعات وهي العصي

## ي و م (root_001700): 43:39 ٱلْيَوْمَ, 43:65 يَوْمٍ, 43:68 ٱلْيَوْمَ, 43:83 يَوْمَهُمُ

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

## ظ ل م (root_000967): 43:39 ظَّلَمْتُمْ, 43:65 ظَلَمُوا۟, 43:76 ظَلَمْنَٰهُمْ, 43:76 ٱلظَّٰلِمِينَ

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

## ع ذ ب (root_000994): 43:39 ٱلْعَذَابِ, 43:48 بِٱلْعَذَابِ, 43:50 ٱلْعَذَابَ, 43:65 عَذَابِ, 43:74 عَذَابِ

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

## ش ر ك (root_000791): 43:39 مُشْتَرِكُونَ

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

## س م ع (root_000741): 43:40 تُسْمِعُ, 43:80 نَسْمَعُ

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

## ص م م (root_000884): 43:40 ٱلصُّمَّ

- **B001** işitme kaybı ve işitmezlik — işitme kaybı; söylenene kulak vermeme · işitmeyen, sağır · işitmeyenler, sağırlar · işitmez oldu · Tanrı onu işitmez kıldı · onu işitmez durumda buldum · işitmiyormuş gibi davrandı · çağrıya karşılık vermeyen yılan
  الصمم ذهاب السمع (ayn;tahdhib)؛ رجل أصم بين الصمم (sihah)؛ الصمم فقدان حاسة السمع وبه يوصف من لا يصغي إلى الحق ولا يقبله (mufradat)؛ الصمم في الأذن (maqayis)؛ الحية التي لا تجيب الراقي صماء (tahdhib)
- **B002** açıklığı tıkayıp kapatma — şişe tıkacı · şişe tıkacı, kapak · şişenin ağzını sıkıca kapattım · şişenin ağzını tıkadım · tek giysiyle bütünüyle sarınma
  الصمام رأس القارورة والفعل صممتها (ayn)؛ صمام القارورة سدادها (sihah)؛ صمت القارورة إذا سددت رأسها (tahdhib)؛ صممت القارورة شددت فاها (mufradat)؛ صمام القارورة سمي بذلك لأنه يسد الفرجة واشتمال الصماء (maqayis)
- **B003** boşluksuz katılık ve sıkılık — kamışın içinin dolgunluğu · katı ve yekpare taş · iri, güçlü ve atılgan adam · sıkı yapılı güçlü at · taşları dikleşmiş kalın tepe · aralıksız biçimde toplanmış kalabalık
  الاكتناز في جوف القنا والصلابة في الحجر (ayn;tahdhib)؛ حجر أصم صلب مصمت (sihah)؛ الصمصم الرجل الغليظ (sihah;tahdhib;maqayis)؛ الصمم الشديد الأسر المعصوب (tahdhib)؛ الصمصمة الجماعة كأنها اجتمعت حتى لا خلل فيها (maqayis)
- **B004** sert ve taşlı kalın arazi — kalın ve sert toprak · sert, kalın arazi; kum kenarındaki taşlık · kum yanında bulunan sert taşlı arazi
  الصمان أرض إلى جنب رمل عالج وكل أرض كذلك إلى جنب رمل صلبة الحجارة (ayn)؛ الصماء من الأرض الغليظة والصمان موضع (sihah)؛ الصمان أرض غليظة دون الجبل (tahdhib)؛ الصمان أرض غليظة (mufradat)؛ الرمل فيه خلل والصمانة ليست كذلك (maqayis)
- **B005** çıkış bırakmayan ağır felaket — çıkış bırakmayan ağır sınanma · çok ağır felaket, büyük sıkıntı
  الشدة في الأمر وفتنة صماء (ayn;tahdhib)؛ الصماء الداهية وفتنة صماء شديدة (sihah)؛ الداهية الشديدة صماء وصمام (tahdhib)؛ الصماء الداهية كأنه أمر لا فرجة له فيه (maqayis)
- **B006** beklenen sesin duyulmaması [kalıp] — çatışma sesi duyulmayan kutsal ay · kan öyle çoğaldı ki taşın düşüşü bile duyulmadı
  رجبا شهر الله الأصم لا يسمع فيه صوت مستغيث ولا حركة قتال ولا قعقعة سلاح (sihah)؛ صمت حصاة بدم لو وقعت حصاة لم يسمع لها صوت (tahdhib)؛ شبه ما لا صوت له به ولذلك قيل صمت حصاة بدم (mufradat)؛ الأصل في ذلك قولهم صمت حصاة بدم (maqayis)
- **B007** iç dayanak ve katışıksız öz — organı ayakta tutan iç kemik, temel dayanak · topluluğunun katışıksız özünden · atlarının seçkin ve asli bölümü
  الصميم العظم الذي هو قوام العضو وصميم قومه من خالصهم وأصلهم (ayn)؛ صميم الشيء خالصه (sihah)؛ الصميم هو العظم الذي به قوام العضو وفلان من صميم قومه إذا كان من خالصهم (tahdhib)
- **B008** sıcağın veya soğuğun en şiddetlisi [kalıp] — sıcağın ya da soğuğun en şiddetli derecesi
  صميم الحر والشتاء أشد حرا وبردا (ayn)؛ صميم الحر وصميم البرد أشده (sihah)؛ صميم القيظ أشده حرا وصميم الشتاء أشده بردا (tahdhib)
- **B009** aldırmadan kararlılıkla ilerleme — kesin karar verip ilerleme · kimseyi dinlemeden işte diretti · yoluna devam etti · topluluğa saldırıp geri dönmedi
  التصميم المضي في كل أمر (ayn)؛ صمم في السير وغيره أي مضى (sihah)؛ الذي يشد على القوم ولا ينثني قد صمم تصميما (tahdhib)؛ صمم في الأمر مضى فيه غير مصغ إلى من يردعه (mufradat)؛ صمم في الأمر إذا مضى فيه راكبا رأسه (maqayis)
- **B010** ısırıp dişleri sabitleme — ısırıp dişlerini geçirdi ve bırakmadı
  صمم في عضته إذا نيب فلم يرسل ما عض (ayn)؛ صمم أي عض ونيب فلم يرسل ما عض (sihah)؛ صمم الحية في نهشه إذا نيب (tahdhib)؛ صمم إذا عض في الشيء فأثبت أسنانه فيه (maqayis)
- **B011** eğilmeyen, kemiği yaran keskin kılıç — eğilmeyen keskin kılıç · kemiğin içinden geçen kılıç · kılıç kemiğin içinden geçip onu kesti
  الصمصامة اسم للسيف القاطع (ayn)؛ الصمصام والصمصامة السيف الصارم الذي لا ينثني (sihah)؛ صمم السيف إذا مضى في العظم وقطعه (sihah)؛ المصمم من السيوف الذي يمر في العظام والصمصامة السيف الصارم (tahdhib)؛ اشتق منه السيف الصمصام والصمصامة (maqayis)
- **B012** çok sert darbe indirme — ona sopayla ya da taşla vurdu · çok sert vurdu · çok sert darbe · güçlü darbe indiren yiğit
  صمه بالعصا أي ضربه بها وصمه بحجر (sihah)؛ صم إذا ضرب ضربا شديدا (tahdhib)؛ ضربة صماء (mufradat)؛ الصمة للشجاع الذي يصم بالضربة (mufradat)
- **B013** yiğit ve erişilmesi güç varlık — yiğit ve erişilmesi güç adam · aslan · erkek yılan · aslan
  الصمة والصم من أسماء الأسد (ayn)؛ الصم اسم من أسماء الأسد والداهية والصمة الرجل الشجاع والذكر من الحيات (sihah)؛ الصمة الشجاع والصمة من أسماء الأسد (tahdhib)؛ الصمة للشجاع الذي يصم بالضربة (mufradat)؛ الأسد صمة كأنه لا وصول إليه من وجه (maqayis)
- **B014** işitmeyi yok eden şiddetli ses [kalıp] — kulakları sağır eden ses
  صوت مصم يصم الصماخ (ayn;tahdhib)
- **B015** susun ya da saldırın buyruğu — sessiz olun, susun · düşmana saldırın
  صمام صمام بمعنيين أي تصاموا في السكوت واحملوا في الحملة (ayn)؛ صمام صمام أي تصاموا في السكوت (sihah)؛ صمام صمام يحمل على معنى تصاموا واسكتوا وعلى معنى احملوا على العدو (tahdhib)
- **B016** ağır olayı büyüten kalıplaşmış söz — ne büyük olay; ne ağır felaket · ne ağır felaket; ey dağın yankısı
  صمي صمام وصمي ابنة الجبل يضرب مثلا للداهية الشديدة (tahdhib)؛ يقولون صمي ابنة الجبل ويقال أراد الصدى (sihah)؛ العرب تقول في تعظيم الأمر صمي صمام والأصل صمت حصاة بدم (maqayis)
- **B017** karşılık alamayınca eylemi aşırı yineleme [kalıp] — bezle durmadan işaret etme · peş peşe ve aşırı vurma · durmadan ve yüksek sesle çağırma
  لمع الأصم كأنه لا يسمع الجواب فهو يديم اللمع؛ ضربه ضرب الأصم إذا تابع الضرب وبالغ فيه؛ دعاه دعوة الأصم إذا بالغ في النداء (tahdhib)
- **B018** gebe dişi deve — gebe dişi deve; gebe develer
  الصماء من النوق اللاقح إبل صم (tahdhib)
- **B019** son derece cimri kişi — son derece cimri kişi
  الصمصم البخيل النهاية في البخل (tahdhib)
- **B020** koyulaşıp topaklanmış süt — koyulaşıp topaklanmış süt
  الصمالخ اللبن الخاثر المتلبد ومن الصمم فكأن اللبن إذا خثر لم يكن له عند صبه صوت (maqayis)

## ع م ي (root_001049): 43:40 ٱلْعُمْىَ

- **B001** iki gözde görme yitimi — iki gözde görme yitimi · iki gözü görmeyen erkek veya kadın · körmüş gibi davranmak · birini kör olarak bulmak
  العمى ذهاب البصر (ayn;sihah); العمى ذهاب البصر من العينين كلتيهما (tahdhib;maqayis); يقال في افتقاد البصر والبصيرة، ويقال في الأول أعمى (mufradat); رجل أعمى وامرأة عمياء، ولا يقع هذا النعت على العين الواحدة (ayn;tahdhib;maqayis); عميت عيناه وعينان عمياوان وعمياوات (ayn;tahdhib;maqayis); تعامى الرجل أرى من نفسه ذلك (sihah); أعميت الرجل إذا وجدته أعمى (maqayis)
- **B002** kavrayış ve doğru yönü seçme yoksunluğu — zihinsel kavrayış yoksunluğu · konunun anlaşılmaz duruma gelmesi · işini veya doğru yönü kavrayamayan kimse · sevgi insanın sağlıklı yargısını köreltir
  رجل عم وقوم عمون من عمى القلب (ayn); رجل عمي القلب أي جاهل، وعمية القلب (sihah); عمي عليه الأمر إذا التبس (sihah); فيهم عميتهم أي جهلهم (sihah); أعمى عن الحجة (tahdhib); عمي فلان عن رشده وعمي عليه طريقه (tahdhib); عمى القلب (tahdhib); رجل عم في أمره لا يبصره (tahdhib); العمى يقال في افتقاد البصر والبصيرة (mufradat); رجل عم إذا كان أعمى القلب وقوم عمون (maqayis); فلان في عمياء إذا لم يدر وجه الحق (maqayis); الحب أعمى (maqayis)
- **B003** körü körüne sapma ve yandaşlık — sapma, inatçı yanılgı veya kör yandaşlık · yönü sorgulanmayan yandaşlık çağrısı ya da sancağı
  العماية الغواية وهي اللجاجة (ayn;tahdhib;maqayis); العمية الضلالة وفي لغة عمية (ayn); العمية الضلالة وكذلك العمية (maqayis); عمية الجاهلية قالوا أراد الكبر (maqayis); وقتيل عميا أي لم يدر من قتله (maqayis); راية عمية يغضب لعصبة أو ينصر عصبة أو يدعو إلى عصبة (tahdhib); الأمر الأعمى العصبية لا يستبين ما وجهه (tahdhib); العمية الدعوة العمياء (tahdhib); العمية الفتنة وقيل الضلالة (tahdhib)
- **B004** anlamı gizleyip karıştırma — bir şeyi gizleyip anlaşılmaz kılma
  التعمية أن تعمي شيئا على إنسان حتى تلبه عليه (ayn); عميت معنى البيت تعمية، ومنه المعمى من الشعر (sihah); التعمية أن تعمي على إنسان شيئا فتلبسه عليه تلبيسا (tahdhib); التعمية أن تعمي على إنسان شيئا فتلبسه عليه لبسا (maqayis)
- **B005** görüşü örten yoğun bulut veya toz karanlığı — yoğun kapalı bulut, koyu karanlık veya örtücü toz
  العماية والعماء السحاب الكثيف المطبق (ayn); القطعة منها عماءة (ayn); العماء ممدود السحاب، هو شبه الدخان يركب رءوس الجبال (sihah); العماء في كلام العرب السحاب (tahdhib); العماية والعماءة السحابة الكثيفة المطبقة (tahdhib); العماء الذي قد حمل الماء وارتفع (tahdhib); هو في عماية شديدة وعماء أي مظلم (maqayis); العماء الغبار (maqayis)
- **B006** izi ve işareti olmayan bilinmeyen arazi — yerleşim izi ve yol işareti olmayan bilinmeyen arazi
  المعامي الأرض المجهولة (ayn); المعامي من الأرضين الأغفال، التي ليس بها أثر عمارة ولا معلم (sihah); بلد عامية أعماؤه (ayn;sihah;tahdhib;maqayis); المعامي من الأرضين الأغفال التي ليس بها أثر من عمارة (maqayis); أعماؤه مجاهله، بلد مجهل وعمى لا يهتدى فيه (tahdhib); أرض عمياء وعامية ومكان أعمى لا يهتدى فيه (tahdhib); عم طريقا وعم مسلكا يريد الطريق ليس مبين الأثر (tahdhib)
- **B007** dalganın çöp ve köpüğü yukarı atması — dalganın çöp ve köpüğü su yüzeyine atması · devenin böğürürken salyasını başının üstüne atması
  العمي على لفظ الرمي رفع الأمواج القذى والزبد في أعاليه (ayn); عمى الموج بالفتح يعمى عميا إذا رمى القذى والزبد (sihah); العمي على مثال الرمي دفع الأمواج القذى والزبد في أعاليها (tahdhib); ومن الباب العمي على وزن رمي وذلك دفع الأمواج القذى والزبد في أعاليها (maqayis); البعير إذا هدر عمى بلغامه على هامته عميا (ayn;tahdhib;maqayis)
- **B008** öğle sıcağının en şiddetli vakti [kalıp] — göz açtırmayan en şiddetli öğle sıcağı vakti
  أتيته صكة عمى أي وقت الهاجرة (sihah); أتيته ظهرا صكة عمي إذا أتيته في الظهيرة (maqayis); يراد حين يكاد الحر يعمي (maqayis); صكة عمي هو أشد الهاجرة حرا (tahdhib); لقيته صكة عمى وصكة أعمى أي نصف النهار في شدة الحر (tahdhib); يصير كالأعمى (tahdhib)
- **B009** seçip özellikle yönelme — bir şeyi seçip amaç edinme · başka hedef gözetmeden ona gitme
  الاعتماء الاختيار (ayn); اعتميت الشيء اخترته وهو قلب الاعتيام (sihah); عميت إلى كذا أعمى عميانا إذا ذهبت إليه لا تريد غيره (tahdhib); اعتمتيه اعتماء أي قصدته، واعتمتيه اخترته، وكذلك اعتمته (tahdhib)
- **B010** sel, gece veya saldırgan deve için özel ad — sel, gece veya saldırgan kızgın deve için kullanılan ad
  الأعميان السيل والجمل الهائج الصئول (sihah); الأعمى الليل، والأعمى السيل، وهما الأبهمان (tahdhib)
- **B011** biçime bağlı adlandırmalar — 
  عمى الماء يعمي إذا سال وهمى يهمي مثله (tahdhib); عمى النبت يعمي واعتم واعتمى ثلاث لغات (tahdhib); عمى يعمي إذا سال، يقول سال عليها الآل (tahdhib)

## ECHO ع م م (root_001047): for 43:40 ٱلْعُمْىَ: withheld observed target; not identity

- **B001** babanın erkek ya da kız kardeşi — babanın erkek kardeşi · babanın kız kardeşi · babanın erkek ve kız kardeşleri · baba ve anne tarafındaki erkek akrabaları çok ya da saygın olan · birini babanın erkek kardeşi saymak · birine babanın erkek kardeşi diye seslenmek
  الأعمام والعمومة جماعة العم والعمة (ayn); العم أخو الأب والجمع أعمام وعمومة (sihah); العم أخ الأب (tahdhib); العم أخو الأب والعمة أخته (mufradat); استعم عما وتعممه (sihah;tahdhib;mufradat)
- **B002** başa sarılan kumaş örtü — başa sarılan kumaş örtü · başına kumaş örtü sarmak · birinin başına kumaş örtü sarmak · başına tören örtüsü sararak önder ilan etmek · baş örtüsünü güzel sarış
  العمامة معروفة والجمع عمامات وعمائم (maqayis); العمامة معروفة والجمع العمائم (ayn;sihah;tahdhib); تعممت بالعمامة واعتممت (maqayis;sihah;tahdhib); عممته ألبسته العمامة (sihah); عمم الرجل سود لأن تيجان القوم العمائم (maqayis;ayn;sihah;tahdhib); كني بذلك عن السيادة (mufradat)
- **B003** hayvanın başını çevreleyen renk işareti — başı sargılı gibi farklı renkte olan koyun · alın akı yele köküne ve baş çevresine inen at
  شاة معممة إذا كانت سوداء الرأس (maqayis); شاة معمة بيضاء الرأس (ayn); المعمم من الخيل وغيره الذي ابيض أذناه ومنبت ناصيته وما حولها (sihah); شاة معممة في هامتها بياض (sihah); فرس معمم إذا انحدر بياض ناصيته إلى منبتها وما حولها من الرأس (tahdhib); شاة معممة مبيضة الرأس كأن عليها عمامة (mufradat)
- **B004** uzayıp tam gelişmiş olma — bitki için uzun ya da tam gelişmiş · uzun ya da yapısı tam gelişmiş dişi · bedeni ya da yapısı tam gelişmiş · beden, gençlik ya da varlık bakımından tam düzeye erişmek · bitkinin gürleşip uzaması ya da olgunlaşması · belirli bir yabani otun kurusu
  العميم الطويل من النبات (maqayis;ayn); نخلة عميمة والجمع عم (maqayis); جارية عميمة أي طويلة (maqayis); استوى النبات على عممه أي على تمامه (maqayis); عشب عميم وقد اعتم (maqayis); العم التامة في طولها والتفافها واحدتها عميمة (tahdhib); اعتم النبت اعتماما إذا التف وطال (tahdhib); شيء عميم أي تام (sihah); استوى على عممه يريدون تمام جسمه وشبابه وماله (sihah); جسم عمم أي تام (sihah); العميم يبيس البهمى (sihah)
- **B005** herkesi ya da her yeri kapsama — bütün topluluğu ya da tüm yerleri kapsamak · seçkin kesimin karşıtı olan geniş çoğunluk · insan toplulukları · işimizi sana yükümlülük olarak vermek · topluluğun işlerini üstlenen ve iyiliği herkese erişen önder · az olan ordusunu çoğaltmak
  عمنا هذا الأمر يعمنا عموما إذا أصاب القوم أجمعين (maqayis); العامة ضد الخاصة (maqayis;sihah); العمائم الجماعات واحدها عم (maqayis); العم الجماعة من الناس (maqayis;sihah;tahdhib); العماعم الجماعات (sihah;tahdhib); عم الشيء بالناس إذا بلغ المواضع كلها (ayn); عم الشيء يعم عموما شمل الجماعة (sihah); عمهم بالعطية (sihah); قد عممناك أمرنا أي ألزمناك (tahdhib); يعم الناس فضله ومعروفه (tahdhib); أصل ذلك من العموم وهو الشمول (mufradat)
- **B006** yeni sağılmış katıksız sütün köpürmesi — yeni sağılmış katıksız sütün üstünde örtü gibi köpük oluşması
  عمم اللبن أرغى (maqayis;sihah); لا يكون ذلك إلا إذا كان صريحا ساعة يحلب (maqayis); كأن رغوته شبهت بالعمامة (sihah)
- **B007** yalıtık adlandırmalar — 
  إن فيه لعمية أي كبرا (maqayis); العمية مثل العبية الكبر (sihah); فلان ذو عمية أي إنه يعم بنصره أصحابه (maqayis)
- **B008** bir topluluğun katışıksız özünden olma [kalıp] — onların içine sonradan karışmamış öz kesiminden
  هو من عميمهم وصميمهم وهو الخالص الذي ليس بمؤتشب (maqayis); هو من عميمهم أي صميمهم (sihah)
- **B009** birbirine bağlanmış ağaçlardan su geçiş aracı — birbirine bağlanmış ağaç parçalarından yapılmış sal
  العامة عيدان يضم بعضها إلى بعض في البحر ثم تركب (ayn); العامة عيدان يشد بعضها إلى بعض ويعبر عليها (tahdhib)
- **B010** görüş alanında beliren kişi — görüş alanında beliren kişi
  العامة الشخص إذا بدا لك (ayn)

## ض ل ل (root_000913): 43:40 ضَلَٰلٍ

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

## ذ ه ب (root_000522): 43:41 نَذْهَبَنَّ, 43:53 ذَهَبٍ, 43:71 ذَهَبٍ

- **B001** altın ve altından bir parça — altın, işlenmemiş altın · altından bir parça
  الذَّهَب معروف (maqayis;jamhara;sihah)؛ الذَّهَب التبر (ayn;tahdhib)؛ القطعة منه ذهبة (maqayis;ayn;sihah;tahdhib)
- **B002** altınla kaplama ve altın kaplı nesne — altınla kaplanmış veya bezenmiş nesne · altınla bezenmiş kayışlar, deriler veya kumaşlar · altınla kaplama · altınla kaplama
  المذاهب سيور تموه بالذهب (maqayis;sihah)؛ كل شيء مموه بذهب فهو مذهب (maqayis;sihah)؛ الشيء المطلي بماء الذهب (ayn;tahdhib)؛ التمويه بالذهب (sihah)
- **B003** altın görünce şaşakalma, gözü kamaşma veya ürkme — altını görünce şaşakalmak, gözü kamaşmak veya ürkmek
  ذهب الرجل إذا رأى معدن الذهب فدهش (maqayis)؛ إذا رأى ذهبا في المعدن فبرق بصره (sihah;tahdhib)؛ فأفزعه (jamhara)
- **B004** kızılına sarılık çalan doru at rengi — kızılına sarılık çalan doru at · kızılına sarılık çalan dişil renk biçimi
  كميت مذهب إذا علته حمرة إلى اصفرار (maqayis)؛ كميت مذهب للذي تعلو حمرته صفرة (sihah;tahdhib)
- **B005** bir biçimde iyi yağmur, öbüründe hafif yağmur — yağmur, özellikle iyi ve yararlı yağmur · hafif, az veya güçsüz yağmurlar
  الذهبة فمطر جود (maqayis)؛ الذهبة المطرة الجودة (ayn;tahdhib)؛ الذهاب مطر خفيف قليل (jamhara)؛ الذهاب الأمطار الضعيفة (tahdhib)؛ الذهبة المطرة (sihah)
- **B006** gitme, geçme ve uzaklaşma — gitmek, geçmek · gitme ve geçme · gitmesini sağlamak veya ortadan kaldırmak · gitme
  ذهاب الشيء مضيه (maqayis)؛ الذهاب والذهوب مصدر ذهبت (ayn)؛ ذهب يذهب ذهابا وذهوبا (jamhara;sihah;tahdhib)؛ الذهاب المرور (sihah)
- **B007** gidilen yol, yer veya zaman; izlenen yöntem ve tutum — yol, gidilen yer veya vakit; gereksinim giderme yeri · çıkış yolları daraldı · iyi veya kötü tutum ve yöntem
  ضاقت عليه مذاهبه أي طرقه (jamhara)؛ مذهب الرجل ممشاه لقضاء الحاجة (jamhara)؛ حسن المذهب وقبيح المذهب أي الطريقة (jamhara)؛ المذهب اسما للموضع ووقتا من الزمان (ayn)؛ موضع الغائط الخلاء والمذهب (tahdhib)؛ ذهب مذهبا حسنا (maqayis;sihah)
- **B008** Yemen'de kullanılan bir ölçü — Yemen halkınca kullanılan bilinen bir ölçü
  الذهب مكيال لأهل اليمن (ayn;jamhara;sihah;tahdhib)؛ الجمع أذهاب ثم أذاهب (ayn;sihah;tahdhib)
- **B009** su kullanımı veya abdestte yinelemeli kuruntu ve abdestte veya başka durumlarda ayartan şeytanın adı — su kullanımı ve abdest sırasında yinelemeli kuşku veya kuruntu · abdestte veya başka durumlarda insanları ayarttığı söylenen şeytanın adı
  المذهب اسم شيطان من ولد إبليس (ayn;tahdhib)؛ به مذهب يعنون به الوسوسة في الماء (sihah)؛ للموسوس به المذهب (tahdhib)؛ هذا الداء الذي يسمى المذهب فما أحسبه عربيا صحيحا (jamhara)

## ر ء ي (root_000531): 43:42 نُرِيَنَّكَ, 43:48 نُرِيهِم

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

## ECHO ر و ي (root_000615): for 43:42 نُرِيَنَّكَ, 43:48 نُرِيهِم: withheld observed target; not identity

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

## و ع د (root_001662): 43:42 وَعَدْنَٰهُمْ, 43:83 يُوعَدُونَ

- **B001** iyi ya da kötü bir şeyi yapacağını sözle bildirme — iyi ya da kötü bir şeyi yapacağını bildirme; verilen söz · ona iyi ya da kötü bir şeyi yapacağını bildirdi · verilen söz; söz verme · verilmiş söz · söz verme; verilen söz · ona iyilik yapacağını bildirdi
  تدل على ترجية بقول ويكون ذلك بخير وشر (maqayis)؛ الوعد والعدة يكونان مصدرا واسما (ayn;tahdhib)؛ الوعد يستعمل في الخير والشر (sihah)؛ الوعد يكون في الخير والشر (mufradat)
- **B002** kötülük yapacağını söyleyerek gözdağı verme — kötülük yapacağını bildirerek korkutma · zarar vereceğini bildirerek gözdağı verme · ona kötülük ya da dayakla gözdağı verdi · gözdağı verme
  فأما الوعيد فلا يكون إلا بشر (maqayis)؛ الوعيد من التهدد أوعدته ضربا (ayn)؛ في الشر الإيعاد والوعيد والتوعد التهدد (sihah)؛ إذا أدخلوا الباء لم يكن إلا في الشر كقولك أوعدته بالضرب (tahdhib)؛ الوعيد في الشر خاصة (mufradat)
- **B003** bir söz için belirlenmiş zaman ya da yer — söz için kararlaştırılan zaman ya da yer · sözleşilen zaman ya da yer · gerçekleşeceği önceden bildirilen belirli gün
  الموعد موضع التواعد وهو الميعاد والميعاد لا يكون إلا وقتا أو موضعا (ayn)؛ الميعاد المواعدة والوقت والموضع وكذلك الموعد (sihah)؛ يكون الموعد وقتا للعدة والميعاد لا يكون إلا وقتا أو موضعا (tahdhib)؛ فاجعل بيننا وبينك موعدا وقل لكم ميعاد يوم (mufradat)
- **B004** karşılıklı söz verme — karşılıklı söz verme; buluşmak üzere anlaşma · karşılıklı söz verme · onunla karşılıklı sözleştim · topluluk birbirine söz verdi
  والمواعدة من الميعاد (maqayis)؛ موضع التواعد (ayn)؛ تواعد القوم أي وعد بعضهم بعضا (sihah)؛ واعدت فلانا إذا وعدته ووعدني (tahdhib)؛ واعدته وتواعدنا (mufradat)
- **B005** erkek hayvanın saldırı öncesi kükremesi [kalıp] — erkek hayvanın saldırı öncesi kükremesi
  وعيد الفحل هديره إذا هم أن يصول (maqayis)؛ وعيد الفحل إذا هم أن يصول (ayn)؛ وعيد الفحل هديره إذا هم أن يصول (sihah)
- **B006** belirtileri gelecekteki bir durumu bekleten — belirtileri ilerideki durumu umduran · yağmur ve bitki bakımından umut veren toprak · başlangıcı sıcak ya da soğuk olacağını gösteren gün · iyiliği ve gelişmesi umulan hayvan ya da sürü · belirtileri cömertlik ve sağlam huy bekleten
  أرض بني فلان واعدة إذا رجي خيرها من المطر والإعشاب ويوم واعد (maqayis)؛ يوم واعد إذا وعد أوله بحر أو برد وأرض واعدة إذا رجي خيرها من النبت (sihah)؛ أرض واعدة إذا رجي خيرها ويقال للدابة والماشية واعد ويومنا يعد بردا وهذا غلام تعد مخايله كرما (tahdhib)

## ECHO ع د د (root_000989): for 43:42 وَعَدْنَٰهُمْ, 43:62 عَدُوٌّ, 43:67 عَدُوٌّ, 43:83 يُوعَدُونَ: withheld observed target; not identity

- **B001** sayma, sayı ve sayıya göre bir topluluğa katma — bir şeyi sayıp miktarını belirlemek · sayı; sayılanın miktarı · sayıca çokluk · sayılmış veya sayıyla sınırlandırılmış · iyiler arasında sayılmak · az ya da çok sayıda topluluk · sayıları on bini aşmak
  عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)
- **B002** gelecekteki bir iş için hazırlama ve hazır bulundurma — bir şeyi ilerideki iş için hazırlamak · ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç · bir işe hazırlanmak ve donanmak
  أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)
- **B003** sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi — kadının yeniden evlenmeden önce beklemesi gereken süre · kaçırılan günler kadar başka günlerde yerine getirmek · sayılı ve belirli günler
  عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)
- **B004** kaynağı kesilmeyen kalıcı su ve su yeri — eskiden beri var olan, tükenmeyen sürekli su · sürekli sular veya kalıcı su yerleri · köklü ve eski saygınlık
  العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)
- **B005** belirli zaman ve bilinen aralıklarla geri gelme — sokulma ağrısının belirli aralıklarla alevlenmesi · bana belirli zamanlarda yeniden baş göstermek · zaman, dönem veya en parlak çağ · yayın tekrarlanan titreşimi veya sesi · ayda bir gerçekleşen buluşma · dağıtım, yoklama veya geçici toplanma günü · belirli aralıklarla gelen akıl bulanıklığı
  العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)
- **B006** karşılıklı paydaşlık, pay ve denk sayılma — mal veya değer bakımından karşılıklı paydaş olmak · paylar, denkler veya mirastaki karşılıklı paydaşlar · onun dengi ve karşılığı
  هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)

## ECHO ع و م (root_001063): for 43:42 وَعَدْنَٰهُمْ, 43:83 يُوعَدُونَ: withheld observed target; not identity

- **B001** yüzme ve yüzmeye benzer akıcı ilerleme — suda yüzme · yüzüyormuş gibi akıcı ilerlemek · yüzer gibi akıcı koşan at · suda yüzen küçük canlı · güneşin gök kuşağındaki bölümler boyunca yüzüyormuş gibi ilerlemesi
  العوم السباحة (ayn;sihah;mufradat)؛ السفينة والإبل والنجوم تعوم في سيرها (ayn)؛ سير الإبل والسفينة عوم (sihah)؛ فرس عوام يعوم في جريه (ayn)؛ العوام الفرس السابح في جريه (sihah)؛ العومة دويبة صغيرة تسبح في الماء (sihah)
- **B002** bir kış ve bir yazı kapsayan yıl — yıl; bir kış ve bir yazı kapsayan yıllık çevrim; özellikle bolluk ve verimlilik dönemi için kullanılan yıl sözü · nice yıllar; pekiştirilmiş çoğul yıl ifadesi
  العام حول يأتي على شتوة وصيفة (ayn)؛ العام السنة (sihah)؛ سنون عوم (sihah)؛ العام كالسنة (mufradat)
- **B003** üzerinden bir yıl geçmiş — üzerinden bir yıl geçmiş; bir yıllık eski
  رسم عامي أو حولي أتى عليه عام (ayn)؛ نبت عامي أي يابس أتى عليه عام (sihah)
- **B004** bir yıl ürün verip bir yıl vermeme [kalıp] — hurma ağacının bir yıl ürün verip ertesi yıl vermemesi
  عاومت النخلة أي حملت سنة ولم تحمل سنة
- **B005** yıllara göre işlem yapma — yıllara göre işlem yapma · ekin veya ağaç ürününü iki ya da üç yıl için satmaya dayalı yasak işlem
  عامله معاومة كما تقول مشاهرة؛ المعاومة المنهي عنها أن تبيع زرع عامك أو ثمر نخلك أو شجرك لعامين أو ثلاثة
- **B006** dallardan yapılmış geçiş salı — dallar ve benzeri malzemelerden yapılmış geçiş salı
  العامة تتخذ من أغصان الشجر ونحوه تعبر عليها الأنهار كعبور السفن (ayn)؛ العامة أيضا الطوف الذي يركب في الماء (sihah)
- **B007** uzaktan görünen binici başı — açık arazide uzaktan görünen binici başı · açık arazide uzaktan görünen binici başı · sarığıyla görünen binici başı; sarığın baş çevresindeki kıvrımı
  العام والعومة والعامة هامة الراكب إذا بدا لك رأسه في الصحراء (ayn)؛ لا يسمى رأسه عامة حتى ترى عمامة عليه (ayn)؛ العامة كور العمامة (sihah)
- **B008** en seçkin olanı seçip ayırma — bir kimsenin malının en iyisini seçip ayırma · bir kişiyi veya malının en iyisini seçip ayırmak · ölüm canları seçip alır
  الاعتيام اصطفاء خيار مال الرجل؛ اعتمت أفضل ماله؛ الموت يعتام النفوس
- **B009** biçilmiş ürünü avuç avuç yığma — biçilmiş ürünü avuç avuç koyup biriktirme · avuç avuç biriktirilmiş hasat yığını
  التعويم وضع الحصد قبضة قبضة فإذا اجتمع فهي عامة والجمع عام
- **B010** yıllar arasındaki bir vakitte karşılaşma [kalıp] — yıllar arasındaki bir vakitte karşılaşma
  لقيته ذات العويم وذلك إذا لقيته بين الأعوام

## و ح ي (root_001633): 43:43 أُوحِىَ

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

## ص ر ط (root_000858): 43:43 صِرَٰطٍ, 43:61 صِرَٰطٌ, 43:64 صِرَٰطٌ

- **B001** yol, özellikle düz yol — yol, özellikle düz yol · yol veya düz yol · yol
  الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)
- **B002** geçişte gözden kaybolmak; özellikle yiyeceği yutmak — yiyeceği boğazdan geçirip gözden kaybolacak biçimde yutmak · kolayca yutulan pelte kıvamlı tatlı · geniş boğazlı
  أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب؛ السرطراط على فعلال الفالوذ لأنه يسترط (maqayis 1774)؛ السرطم: الواسع الحلق، والميم فيه زائدة، وإنما هو من سرط، إذا بلع (maqayis السرطم)
- **B003** vuruşta kesip ilerleyen kılıç — vuruşta kesip ilerleyen kılıç
  والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)

## د و ن (root_000502): 43:45 دُونِ, 43:86 دُونِهِ

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

## ء ل ه (root_000047): 43:45 ءَالِهَةً, 43:58 ءَأَٰلِهَتُنَا, 43:63 ٱللَّهَ, 43:64 ٱللَّهَ, 43:84 إِلَٰهٌ, 43:84 إِلَٰهٌ, 43:87 ٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 43:45 ءَالِهَةً, 43:58 ءَأَٰلِهَتُنَا, 43:63 ٱللَّهَ, 43:64 ٱللَّهَ, 43:84 إِلَٰهٌ, 43:84 إِلَٰهٌ, 43:87 ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ء ي ي (root_000074): 43:46 بِـَٔايَٰتِنَآ, 43:47 بِـَٔايَٰتِنَآ, 43:48 ءَايَةٍ, 43:69 بِـَٔايَٰتِنَا

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

## م ل ء (root_001441): 43:46 وَمَلَإِي۟هِۦ

- **B001** doldurma, doluluk ve bir kap dolusu miktar — doldurmak · doldurma · bir kap dolusu miktar · dolu · dolmak · yiyip içerek karnını doldurmak · öfkeden dolup taşmak · yayı güçlüce çekmek · çok yemekten doğan tıkanma ve ağırlık
  ملأت الشيء أملؤه ملئا (maqayis)؛ ملأته فامتلأ وهو ملآن مملوء ممتلئ (ayn)؛ الملء اسم ما يأخذه الإناء إذا امتلأ (sihah)؛ الملء مقدار ما يأخذه الإناء الممتلئ (mufradat)؛ أملأت النزع في القوس (maqayis;sihah)
- **B002** danışmak üzere toplananlar veya ileri gelenler — danışmak üzere toplananlar; ileri gelenler · ortak danışma ve toplanma sonucunda
  الملأ الأشراف من الناس (maqayis)؛ الملأ جماعة من الناس يجتمعون ليتشاوروا ويتحادثوا (ayn)؛ الملأ الجماعة (sihah)؛ الملأ جماعة يجتمعون على رأي (mufradat)
- **B003** bir işte birleşip destek olma [kalıp] — bir işte onun yanında yer alıp yardım etmek · bir iş üzerinde birleşip anlaşmak
  مالأت فلانا على الأمر أي كنت معه في مشورته (ayn)؛ الممالأة المعاونة مالأت على فلان أي عاونت عليه (ayn)؛ مالأته على الأمر ممالأة ساعدته عليه وشايعته (sihah)؛ تمالؤوا على الامر اجتمعوا عليه (sihah)؛ مالأته عاونته وصرت من ملئه أي جمعه (mufradat)
- **B004** göz dolduran güzellik ve görkem [kalıp] — göz dolduracak kadar güzel ve alımlı · görenlerin gözünde büyük ve etkileyici
  شاب مالئ العين حسنا (ayn;sihah;mufradat)؛ فلان ملء العيون أي معظم عند من رآه (mufradat)؛ فيملئون العيون رواء ومنظرا والنفوس بهاء وجلالا (mufradat)
- **B005** huy ve geçinme biçimi — huy ve insanlarla geçinme biçimi · geçimleri ve huyları ne güzel
  أراد به الخلق (maqayis)؛ حسن الخلق من سجايا الملأ (maqayis)؛ الملا أيضا الخلق (sihah)؛ ما أحسن ملأ بني فلان أي عشرتهم وأخلاقهم (sihah)؛ الملأ الخلق المملوء جمالا (mufradat)
- **B006** başı dolduran soğuk algınlığı veya benzeri ağırlık — çok yemekten doğan soğuk algınlığı benzeri baş ağırlığı · soğuk algınlığı · soğuk algınlığına tutulmak · başı dolduran soğuk algınlığı
  الملأة ثقل يأخذ في الرأس كالزكام من امتلاء المعدة (ayn)؛ الملاة الزكام (sihah)؛ ملئ الرجل وأملأه الله أي أزكمه (sihah)؛ الملاءة الزكام الذي يملأ الدماغ (mufradat)
- **B007** bürünme örtüsü veya geniş üst giysi — bürünme örtüsü; geniş üst giysi
  الملاءة الريطة والجميع الملاء (ayn;sihah)
- **B008** güvenilir ödeme gücü ve maddi yeterlilik — varlıklı, ödeme gücü olan ve güvenilir kişi · ödeme gücü ve güvenilirlik · varlıklı ve güvenilir hale gelmek · ödeme gücü olan varlıklı topluluk
  الملاءة مصدر المليء الغني الذي عنده ما يؤدي (ayn)؛ ملا الرجل صار مليئا أي ثقة فهو غنى ملئ بين الملاءة (sihah)؛ هو مليء بكذا (mufradat)

## ض ح ك (root_000903): 43:47 يَضْحَكُونَ

- **B001** sevinçten yüzü açılıp dişleri görünecek biçimde gülmek — gülmek · gülme; gülüş · bir kez gülme · çok gülen · çok gülen kadın · gülmek veya güler görünmek · gülmek veya gülmeye koyulmak · güldürmek · çok gülen adam
  ضحك الإنسان (maqayis)؛ ضحك يضحك ضحكا (ayn;sihah;tahdhib)؛ الضحك معروف (jamhara;tahdhib)؛ انبساط الوجه وتكشر الأسنان من سرور النفس (mufradat)
- **B002** gülünç hedef olma veya alay ederek gülme — gülünecek şey · gülünçlük; alay konusu · alay konusu olan adam · biriyle alay edip gülmek
  الأضحوكة ما يضحك منه (maqayis;sihah)؛ الضحكة ما يضحك منه (ayn;tahdhib)؛ رجل ضحكة يضحك منه (maqayis;jamhara;sihah;tahdhib)؛ استعير الضحك للسخرية (mufradat)
- **B003** gülme anlatımıyla sevinmek veya şaşırmak — sevinip bunu gülerek göstermek · şaşırıp bunu gülerek göstermek
  ضحكت سرورا بالأمن (tahdhib)؛ ضحكت عجبت من فزع إبراهيم (tahdhib)؛ يستعمل في السرور المجرد (mufradat)؛ استعمل للتعجب المجرد (mufradat)
- **B004** gülünce görünen küçük azı dişi — gülünce görünen küçük azı dişi · gülünce görünen küçük azı dişleri
  الضاحكة كل سن تبدو من مقدم الأسنان والأضراس عند الضحك (maqayis)؛ الضاحكة كل سن من مقدم الأضراس (ayn)؛ الضواحك وهي أربعة أسنان بعد الأنياب (jamhara)؛ الضاحكة السن التي بين الأنياب والأضراس (sihah)؛ أربعة ضواحك والواحد ضاحك (tahdhib)؛ سميت مقدمات الأسنان الضواحك (mufradat)
- **B005** açık seçik yol veya karışıklık taşımayan görüş — açık seçik yol · açık ve belirgin yol · açık seçik görüş
  الضحوك الطريق الواضح (maqayis)؛ الضحوك من الطرق ما وضح فاستبان (ayn;tahdhib)؛ الضحوك الطريق الواسع (sihah)؛ الضحك المحجة (tahdhib)؛ رأي ضاحك ظاهر غير ملتبس (tahdhib)؛ طريق ضحوك واضح (mufradat)
- **B006** belirli bir yüzeyde güçlü biçimde parıldamak — şimşek çakan bulut · parıldayan veya beyaz görünen taş · güneşe karşı ışıldamak · doluluğundan parıldayan gölcük
  الضاحك من السحاب مثل العارض إلا أنه إذا برق (maqayis;sihah)؛ الضاحك حجر شديد البريق يبدو في الجبل (maqayis)؛ الضاحك حجر أبيض يبدو في الجبل (jamhara)؛ تلألؤها بالضحك (mufradat)؛ البرق العارض ضاحكا والحجر يبرق ضاحكا (mufradat)؛ ضحك الغدير تلألأ من امتلائه (mufradat)
- **B007** hurma çiçek kılıfının yarılması ve açığa çıkan bölüm — yarılıp açılmakta olan ham hurma · yarılan hurma çiçek kılıfı veya içi · hurma ağacının çiçek kılıfı yarıldı
  هو البلح (maqayis)؛ الطلع هو الكافور والضحك جميعا حين ينفتق (maqayis)؛ جوف الطلع (ayn)؛ ضحكت النخلة إذا انشق كافورها (ayn)؛ الطلع إذا تشقق ضحكا (jamhara)؛ الضحك الطلع حين ينشق (sihah)؛ وليع الطلعة الذي يؤكل (tahdhib)؛ البلح حين يتفتق ضاحكا (mufradat)
- **B008** taşacak kadar doldurmak veya doluluktan ışıldamak — gölcük doluluktan ışıldadı · havuzu taşacak kadar doldurmak
  أضحكت حوضك إذا ملأته حتى يفيض (maqayis;tahdhib)؛ ضحك الغدير تلألأ من امتلائه وقد أضحكته (mufradat)
- **B009** özel adlandırma kümesi — beyaz bal · petek balı, tereyağı veya kar · ışık veya görünür beyazlık
  الضحك العسل (maqayis;tahdhib)؛ الضحك الثلج (ayn)؛ الشهد ويقال الزبد ويقال العسل (ayn)؛ العسل الأبيض (jamhara)؛ يسمى الزبد أيضا ضحكا (jamhara)؛ شبه بياض العسل ببياضه (sihah)؛ الثلج وقيل هو الشهد وقيل هو الزبد (tahdhib)؛ الضحك النور (tahdhib)
- **B010** tartışmalı adet görme yorumu — 
  يعني طمثت (ayn)؛ ذكر المفسرون أنها حاضت (jamhara)؛ حاضت فلم نسمعه من ثقة (tahdhib)؛ فضحكت حاضت فليس بشيء (tahdhib)؛ حاضت فليس ذلك تفسيرا لقوله فضحكت (mufradat)
- **B011** hayvanın diş göstermesi, ses çıkarması veya sevinir görünmesi — sırtlanın dişlerini göstermesi veya sevinir gibi görünmesi · maymunun ses çıkarması · yaban eşeğinin dişlerini göstermesi
  تضحك الضبع أي تكشر (jamhara;tahdhib)؛ كأنها تستبشر بالقتلى (jamhara)؛ القرد يضحك إذا صوت (sihah)؛ يضحك الضبع لقتلى هذيل (mufradat)؛ الضحك يختص بالإنسان (mufradat)

## ك ب ر (root_001281): 43:48 أَكْبَرُ

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

## ء خ و (root_000020): 43:48 أُخْتِهَا

- **B001** kardeşlik ve kardeş sayılan kişiler — erkek kardeş · kız kardeş · doğumdan kardeşler · kardeşler; özellikle kardeş sayılan arkadaşlar · kardeş olmak · birbirini kardeş saymak; kardeşlik bağı kurmak · birini kardeş edinmek · o kişi senin kardeşin değildir
  الأخ أصله أخو (sihah)؛ أكثر ما يستعمل الإخوان في الأصدقاء والإخوة في الولادة (sihah)؛ أخت بينة الأخوة (sihah)؛ الأخت أصلها التأنيث (ayn)
- **B002** bağlama halkası veya gözetilen bağ — hayvan bağlama halkası veya bağı · hayvan için bağlama halkası veya bağı yapmak · gözetilmesi gereken ilişki, hak veya yükümlülük bağı
  وكذلك الآخية (maqayis)؛ الآخية واحدة الأواخي (sihah)؛ تشد إليه الدابة (sihah)؛ الآخية أيضا الحرمة والذمة (sihah)
- **B003** özenle araştırıp yönelmek [kalıp] — bir şeyi özenle araştırıp hedef edinmek
  وتأخيت الشيء أيضا مثل تحريته (sihah)

## د ع و (root_000478): 43:49 ٱدْعُ, 43:86 يَدْعُونَ

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

## ECHO د ع ع (root_000477): for 43:49 ٱدْعُ, 43:86 يَدْعُونَ: withheld observed target; not identity

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

## ع ه د (root_001055): 43:49 عَهِدَ

- **B001** yenileyerek koruyup gözetme — koruyup gözetme ve ilgiyi yenileme · yeniden ilgilenip bakımını üstlenme · karşılıklı veya sürekli gözetip kollama · yeniden yoklayıp koruma · eski dostluğun ve saygının hakkını gözetme
  الاحتفاظ بالشيء وإحداث العهد به (maqayis)؛ التعاهد الاحتفاظ بالشيء وإحداث العهد به وكذلك التعهد والاعتهاد (ayn)؛ الحفاظ والوصية والتعهد التحفظ بالشئ وتجديد العهد به (sihah)؛ الحفاظ ورعاية الحرمة والمعاهدة والاعتهاد والتعاهد والتعهد واحد وهو إحداث العهد بما عهدته (tahdhib)؛ حفظ الشيء ومراعاته حالا بعد حال (mufradat)
- **B002** korunup uygulanacak ön buyruk — korunup uygulanacak buyruk veya son istek · birine koruyup uygulayacağı bir buyruk bırakmak · yöneticilere verilen görev ve yetki yazısı
  عهد الرجل يعهد عهدا وهو من الوصية والعهد الذي يكتب للولاة (maqayis)؛ العهد الوصية والتقدم إلى صاحبك بشيء وقد عهد إليه (ayn)؛ الوصية وقد عهدت إليه أي أوصيته ومنه اشتق العهد الذي يكتب للولاة (sihah)؛ منها الوصية وألم أعهد إليكم يعني الوصية (tahdhib)؛ عهد فلان إلى فلان أي ألقى إليه العهد وأوصاه بحفظه (mufradat)
- **B003** bağlayıcı söz ve güvence — bağlayıcı söz, ant veya güvence · Tanrı'ya verilen bağlayıcı söz veya ant · Tanrı'ya bağlayıcı bir söz vermek · sözleşmeyle güvence altına alınan topluluk · sözleşmeli ve koruma altındaki kişi · geçerli bir güvence sözleşmesi bulunan kişi · seninle karşılıklı sözleşme yapan kişi
  العهد الموثق وأهل العهد هم المعاهدون (maqayis)؛ العهد الموثق والمعاهد الذمي وعهيدك الذي يعاهدك (ayn)؛ الأمان واليمين والموثق والذمة وعلي عهد الله والمعاهد الذمي وعهيدك (sihah)؛ العهد الأمان واليمين والميثاق وأهل العهد للذمة وذو عهد في عهده (tahdhib)؛ الموثق الذي يلزم مراعاته عهدا والمعاهد وذو العهد (mufradat)
- **B004** önceki karşılaşmadan kalan bilgi — bunu daha önce bilmiyorum veya görmedim · onu yakın zamanda görmüş veya tanımış · onu en son gördüğümdeki bilgim · önceden bilinen veya tanıdık · üzerinden uzun zaman geçmiş eski şey · uzun zamandır var olan eski köy
  العهد الذي معناه الالتقاء والإلمام وقريب العهد به والعهيد الشيء الذي قدم عهده (maqayis)؛ العهد الالتقاء والإلمام وما لي عهد بكذا وقريب العهد به (ayn)؛ المعهود الذي عهد وعرف وعهدته بمكان كذا وعهدي به قريب وقرية عهيدة قديمة (sihah)؛ عهد الرجل على حال أو في مكان وعهدي بفلان أي أدركته فرأيته والمعهود ما كان من أمس (tahdhib)
- **B005** tanıdık ve geri dönülen yer — ayrıldıktan sonra geri dönülen bilindik konut · önceden bilinen veya anıların bağlı olduğu yer
  العهد المنزل الذي لا يزال القوم إذا انتووا عنه يرجعون إليه والمعهد مثل ذلك (maqayis)؛ العهد المنزل والمعهد الموضع الذي كنت عهدته أو عهدت فيه هوى لك (ayn)؛ العهد المنزل وكذلك المعهد والمعهد الموضع الذي كنت تعهد به شيئا (sihah)؛ المعهد الموضع الذي كنت عهدته أو عهدت به هوى لك (tahdhib)
- **B006** ayıp ve hak başvurusunu güvenceleyen şart — satış güvencesi ve sorumluluk belgesi · bu işte giderilmemiş bir bozukluk var · bu satışta geri dönüş ve güvence yok · ayıp veya hak sorununun giderilmesini ona yüklemek · birine yazılı güvence ve şart yüklemek · zihninde belirgin bir zayıflık var
  العهدة الكتاب الذي يستوثق به في البيعات وفي هذا الأمر لعهدة ما أحكمت والملسى لا عهدة (maqayis)؛ العهدة كتاب الشراء وشيء فيه فساد ولما يحكم بعد (ayn)؛ العهدة كتاب الشراء ولا عهدة أي لا رجعة وعهدته على فلان وما أدرك فيه من درك فإصلاحه عليه (sihah)؛ العهدة المشترطة وبرئت إليك من عهدة هذا العبد واستعهد أي كتب عليه عهدة والملسى لا عهدة له (tahdhib)؛ الوثيقة بين المتعاقدين عهدة وفي هذا الأمر عهدة لما أمر به أن يستوثق منه (mufradat)
- **B007** toprağı yenileyen ardışık ya da ilk mevsim yağmuru — önceki yağışın ardından gelen veya ilk sayılan yağmur · ardışık ya da mevsimin ilk yağmurları · yenileyici yağmur almış toprak veya çayır · ilk yağmur
  العهد من المطر الذي يأتي بعد الوسمي وكل مطر يكون بعد مطر فهو عهاد وروضة معهودة (maqayis)؛ العهد من المطر أن يكون الوسمي قد مضى قبله وكل مطر يكون بعد مطر فهو عهاد وعهدت الروضة (ayn)؛ العهد المطر الذي يكون بعد المطر وقد عهدت الأرض فهي معهودة (sihah)؛ العهدة أول مطر والعهاد أوائل الوسمي والعهد المطر الأول وأرض معهودة (tahdhib)؛ للتفقد قيل للمطر عهد وعهاد وروضة معهودة (mufradat)

## ك ش ف (root_001302): 43:50 كَشَفْنَا

- **B001** örtüyü kaldırıp açığa çıkarma — örtüyü kaldırıp açığa çıkarmak · açığa çıkmak · açığa çıkmak · sıkıntısını gidermek · kötülüğü gidermek ve uzaklaştırmak
  سرو الشيء عن الشيء (maqayis)؛ كشفت الثوب وغيره (maqayis)؛ رفعك شيئا عما يواريه ويغطيه (ayn;tahdhib)؛ كشفت الشئ فانكشف وتكشف (sihah)؛ كشفت الثوب عن الوجه وغيره (mufradat)؛ كشف غمه (mufradat)؛ يكشف السوء (mufradat)
- **B002** belirli yapılarda güçlü biçimde açığa çıkma [kalıp] — şimşek görünüşüyle göğü doldurdu · birbirlerinin kusurları karşılıklı olarak açığa çıktı
  تكشف البرق إذا ملأ السماء (maqayis;sihah)؛ لأن المتكشف بارز (maqayis)؛ لو تكاشفتم ما تدافنتم أي لو انكشف عيب بعضكم لبعض (sihah)
- **B003** belirli beden ve donanım durumlarında açıkta kalma veya biçim özelliği — alın saç çizgisindeki halka biçimli veya yukarı doğru çıkan saç · alın saç çizgisindeki halka veya yukarı yönlü saç dönüşü · alın saç çizgisinde halka ya da yukarı yönlü saç dönüşü bulunan kimse · atın kuyruk sokumundaki eğrilik · savaşta kalkanı bulunmayan adam · gülerken dudağı dönüp diş etleri görünmek
  الكشفة دائرة في قصاص الناصية (maqayis;ayn;tahdhib)؛ الكشف في الخيل التواء في عسيب الذنب (maqayis;sihah)؛ الأكشف الرجل الذي لا ترس معه في الحرب (maqayis;sihah;tahdhib)؛ أكشف الرجل إكشافا إذا ضحك فانقلبت شفته حتى تبدو درادره (tahdhib)
- **B004** düşmanlığı açıkça başlatma [kalıp] — ona karşı düşmanlığı açıkça başlatmak
  كاشفه بالعداوة أي بادأه بها (sihah)
- **B005** dişi devenin üreme aralığına ilişkin tartışmalı teknik kullanım — 
  الكشاف نتاج في إثر نتاج (maqayis)؛ أن تبقى الأنثى سنتين أو ثلاثا لا يحمل عليها (maqayis)؛ الكشوف الناقة التي يضربها الفحل وهي حامل (ayn;sihah;tahdhib)؛ هذا التفسير خطأ (tahdhib)؛ الكشاف أن يحمل على الناقة بعد نتاجها وهي عائذ قد وضعت حديثا (tahdhib)؛ إذا حمل على الناقة سنتين متواليتين فذاك الكشاف (sihah;tahdhib)
- **B006** şiddetli durumun ortaya çıkması — 
  يوم يكشف عن ساق (mufradat)؛ أصله من قامت الحرب على ساق أي ظهرت الشدة (mufradat)؛ وقال بعضهم أصله من تذمير الناقة (mufradat)

## ن ك ث (root_001547): 43:50 يَنكُثُونَ

- **B001** iplikli yapıyı çözme; eski dokumayı yeniden eğirmeye hazırlama — sağlamken çözülüp bozulmak · eski dokuma ya da eğrilmiş ipliği söküp yeniden eğirme · ipi çözmek · çözülmüş ip · çözülmüş ip · çözülmüş ip · topluluk biçimli sıfatla anılan çözülmüş ip
  نقض شيء (maqayis)؛ نكثت الحبل إذا نقضته (jamhara)؛ النكث أن تنقض أخلاق الأكسية والأخبية لتغزل ثانية (sihah)؛ نكثت خيوطها المبرمة وخلطت بالصوف الجديد وغزلت ثانية (tahdhib)؛ نكث الأكسية والغزل قريب من النقض (mufradat)
- **B002** pekiştirilmiş bağlayıcı sözü bozma — pekiştirilmiş sözleşmeyi bozmak · bağlılık sözünü bozmak · bağlılık sözünü bozma ya da bozulmuş bağlılık sözü · topluluğun karşılıklı sözleşmelerini bozması · pekiştirilmiş antları bozmak
  نكث العهد ينكثه نكثا (maqayis)؛ نكث العهد نقضه بعد إحكامه ونكث البيعة (ayn)؛ نكثت العهد تشبيها بنكث الحبل وتناكث القوم عهودهم (jamhara)؛ نكث العهد والحبل فانتكث (sihah)؛ من هذا نكث العهد وهو نقضه بعد إحكامه (tahdhib)؛ استعير لنقض العهد (mufradat)
- **B003** uç veya benzer yüzeyi soyup liflendirme ve bundan kalan parça — diş temizleme çubuğunu soyup ucunu liflendirmek · diş temizleme çubuğunun ucunun liflenmesi · çubuğu liflendirirken ağızda kalan parçacık
  نكثت السواك والساف عن أصول الأظفار وشبهه إذا قشرته وشعثته؛ انتكث هذا السواك وهو تشعث رأسه؛ النكاثة ما كان في فيك من تشعيث السواك ونحوه
- **B004** çetin iş ile sonuna dek zorlanan dayanma gücü — insanları zorlayan çetin iş ya da durum · çok dayanıklı ve güçlü kimse · devenin yürüyüşteki gücünü son sınırına dek zorlamak · gücünün sonuna varmak · develerin güçleri
  النكيثة خطة صعبة ينكث فيها القوم (maqayis;sihah)؛ رجل شديد النكيثة أي شديد النفس (jamhara;sihah)؛ بلغت نكيثته إذا جهد قوته ونكائث الإبل قواها (tahdhib)؛ كل خصلة ينكث فيها القوم يقال لها نكيثة (mufradat)
- **B005** sözden cayma veya ilk kararından dönme [kalıp] — çelişki ya da cayma bulunmayan söz · ilk kararından dönüp başka bir işe yönelmek
  قال قولا لا نكيثة فيه أي لا خلف (maqayis;sihah)؛ طلب حاجة ثم انتكث لأخرى كأنه نقض عزمه الأول (maqayis)؛ طلب فلان حاجة ثم انتكث لأخرى أي انصرف إليها (sihah)
- **B006** deve hastalığı ve semizken zayıflamış deve durumu — develeri tutan hastalık · semizken zayıflamış deve
  النكاف والنكاث داء يأخذ الإبل؛ بعير منتكث إذا كان سمينا فهزل

## ن د و (root_001486): 43:51 وَنَادَىٰ, 43:77 وَنَادَوْا۟

- **B001** topluluğun buluşma yeri ve toplantısı — toplantı yeri, toplantı ve orada bulunanlar · toplanmış topluluğun buluşması · danışma toplantısı ve buluşma yeri · toplanma yeri ve toplantı · danışmak üzere toplanılan yer · toplantıya katıldım · topluluğu toplantıda bir araya getirdim · onunla toplantıda oturdu veya danıştı
  النادي والندى المجلس يندو القوم حواليه (maqayis)؛ الندى مجلس القوم ومتحدثهم وكذلك الندوة والنادي والمنتدى (sihah)؛ النادي المجلس يندو إليه من حواليه (tahdhib)؛ قيل للمجلس النادي والمنتدى والندي (mufradat)
- **B002** yüksek sesle çağırma ve sesin uzağa erişmesi — seslenme ve yüksek sesle çağırma · ona seslendi ve onu çağırdı · birbirlerine seslendiler · namaza çağrı · çağrıda bulunan kimse · sesin eriştiği uzaklık ve yayılma · sesi daha uzağa ulaşan
  النداء الصوت وناداه مناداة ونداء أي صاح به (sihah)؛ النداء رفع الصوت وظهوره (mufradat)؛ النداء ممدود والدعاء أرفع الصوت وندى الصوت بعد مذهبه (tahdhib)
- **B003** çiğ, yağmur ve bunların oluşturduğu ıslaklık — çiğ, nem, ıslaklık veya yağmur · toprağın nemi ve ıslaklığı · ıslandı ve nemlendi · onu ıslattı · nemli toprak · nemli ağaç · hayvansal yağ
  الأصل الآخر الندى من البلل (maqayis)؛ الندى المطر والبلل وندى الأرض نداوتها وبللها (sihah)؛ ندى الماء فمنه المطر وما أصابك من البلل (tahdhib)؛ أصل النداء من الندى أي الرطوبة ويسمى الشجر ندى (mufradat)
- **B004** eli açıklık ve bol iyilikte bulunma — cömertlik, iyilik ve bağış · eli açık ve cömert · ondan daha cömert ve daha çok iyilik eden · arkadaşlarına karşı cömert davranır · adamın bağışı ve iyiliği çoğaldı
  وهو أندى من فلان أي أكثر خيرا منه وهو يتندى على أصحابه (maqayis)؛ الندى الجود وفلان ندي الكف إذا كان سخيا (sihah)؛ ندى الخير هو المعروف وإن يده لندية بالمعروف (tahdhib)؛ يعبر عن السخاء بالندى (mufradat)
- **B005** kötülüğe bulaşma ve utandırıcı leke — elimi onun hoşlanmayacağı bir kötülüğe bulaştırmadım · utandırıcı eylemler veya sözler
  ما نديت كفي لفلان بشيء يكرهه (maqayis)؛ المنديات المخزيات وما نديت بشيء تكرهه (sihah)؛ ما نديني من فلان شيء أكرهه ما بلني ولا أصابني والمنديات المخزيات (tahdhib)؛ منديات الكلم المخزيات (mufradat)
- **B006** hayvanları su ile yakın otlak arasında dolaştırma — develerin sudan yakın otlağa gidip yeniden suya dönmesi · develer iki sulama arasında otladı · develerini su ile otlak arasında gidip gelir duruma getirdi · hayvanların iki sulama arasında otladığı yer · atları su ile otlak arasında dolaştırma; ayrıca terleyinceye dek çalıştırma
  ندوة الإبل أن تندو من المشرب إلى المرعى القريب منه ثم تعود إلى الماء (maqayis)؛ ندت الإبل إذا رعت فيما بين النهل والعلل والموضع مندى (sihah)؛ التندية في الإبل والخيل والتندية معنى آخر وهو تضمير الخيل حتى تعرق (tahdhib)
- **B007** dişi devenin soyca seçkin develere çekmesi [kalıp] — dişi deve soyca seçkin develere çekiyor
  هذه الناقة تندو إلى نوق كرام أي تنزع في النسب (sihah)؛ إن هذه الناقة تندو إلى نوق كرام أي تنزع إليها في النسب (tahdhib)
- **B008** seslenircesine belirginleşme ve kendini belli etme [kalıp] — şey seslenircesine belirginleşti · yol kendini açıkça gösteriyor · onu bildirdim veya ona açıkça gösterdim
  نادى ظهر وناديته علمته وهذا الطريق يناديك (tahdhib)؛ كالكرم إذ نادى أي ظهر ظهور صوت المنادي (mufradat)
- **B009** merkezden ayrılıp uzakta veya dışta kalma — zaman zaman ortaya çıkan söz parçaları · uzak yanlar ve uçlar · o kişi ayrılıp uzaklaştı · sudan uzakta bulunan hurma ağaçları · onlardan hiç kimse kalmadı
  نوادي كلامك أي ما يخرج منك وقتا بعد وقت؛ النوادي النواحي؛ ندا فلان يندو ندوا إذا اعتزل وتنحى؛ الناديات من النخيل البعيدة من الماء؛ لم يند منهم ناد لم يبق منهم أحد (tahdhib)

## ECHO ن د ي (root_001487): for 43:51 وَنَادَىٰ, 43:77 وَنَادَوْا۟: withheld observed target; not identity

- **B001** yüksek sesle seslenme ve çağırma — yüksek sesli çağrı ve sesleniş · ona seslenip çağırdı · birbirlerine seslendiler
  النداء الصوت وقد يضم مثل الدعاء (sihah)؛ ناداه مناداة ونداء أي صاح به (sihah)؛ النداء رفع الصوت وظهوره (mufradat)؛ وقد يقال ذلك للصوت المجرد وللمركب الذي يفهم منه المعنى (mufradat)؛ ندى الصوت بعد مذهبه والنداء ممدود والدعاء أرفع الصوت وقد ناديته نداء (tahdhib)
- **B002** sesin erişim uzaklığı ve menzili — sesin uzaklara erişmesi ve sürmesi · sesi daha uzağa erişen veya daha yüksek çıkan · son sınır, menzil
  ومن الباب ندى الصوت بعد مذهبه وهو أندى صوتا منه أي أبعد (maqayis)؛ الندى الغاية مثل المدى (sihah)؛ الندى أيضا بعد ذهاب الصوت (sihah)؛ فلان أندى صوتا من فلان إذا كان بعيد الصوت (sihah)؛ ندى الصوت بعد مذهبه (tahdhib)؛ فلان أندى صوتا من فلان أي أبعد مذهبا وأرفع صوتا (tahdhib)؛ صوت ندي رفيع (mufradat)
- **B003** topluluğun buluşup görüştüğü toplantı yeri — topluluğun toplantı yeri · toplantı ve sohbet yeri · toplanma ve danışma kurulu · buluşma ve toplantı yeri · yakın topluluğu veya toplantı çevresi · toplantıya katıldı · topluluğu toplantı yerinde bir araya getirdi · onunla toplantı yerinde oturup görüştü
  الأول النادي والندى المجلس يندو القوم حواليه وإذا تفرقوا فليس بندى (maqayis)؛ دار الندوة بمكة لأنهم كانوا يندون فيها أي يجتمعون (maqayis)؛ ناديته جالسته في الندى (maqayis)؛ الندى مجلس القوم ومتحدثهم وكذلك الندوة والنادي والمنتدى (sihah)؛ فإن تفرق القوم فليس بندي (sihah)؛ فليدع ناديه أي عشيرته وإنما هم أهل النادي (sihah)؛ ندوت أي حضرت الندي وانتديت مثله (sihah)؛ ندوت القوم جمعتهم في الندي (sihah)؛ النادي المجلس يندو إليه من حواليه ولا يسمى ناديا حتى يكون فيه أهله (tahdhib)؛ أناديك أشاورك وأجالسك من النادي (tahdhib)؛ يعبر عن المجالسة بالنداء حتى قيل للمجلس النادي والمنتدى والندي (mufradat)
- **B004** hayvanı su ile yakın otlak arasında döndürme — develerin su ile yakın otlak arasında gidip dönmesi · hayvanı sulayıp kısa süre otlattıktan sonra yeniden suya getirme · atın su, otlak ve dönüş döngüsünü yapması · hayvanın su ile otlak arasında döndürüldüğü yer · develerin sulama yeri · iki sulama arasındaki otlama öğünü
  ندوة الإبل أن تندو من المشرب إلى المرعى القريب منه ثم تعود إلى الماء (maqayis)؛ وكذلك تندو من الحمض إلى الخلة وأندى إبله من هذا (maqayis)؛ ندت الإبل إذا رعت فيما بين النهل والعلل فهي نادية (sihah)؛ أنديتها أنا ونديتها تندية والموضع مندى (sihah)؛ الندوة بالضم موضع شرب الإبل (sihah)؛ التندية في الإبل والخيل أن يوردها الماء ثم يردها إلى المرعى ساعة ثم يعيدها (tahdhib)؛ وقد ندا الفرس يندو إذا فعل ذلك (tahdhib)؛ الندى الأكلة بين الشربتين (tahdhib)
- **B005** ıslaklık ve nem; yağmur ve çiy — yağmur, çiy, ıslaklık ve nem · ıslanıp nemlenmek · yerin nemi ve ıslaklığı
  الأصل الآخر الندى من البلل معروف (maqayis)؛ الندى المطر والبلل (sihah)؛ ندى الأرض نداوتها وبللها (sihah)؛ ندي الشيء إذا ابتل فهو ند (sihah)؛ ندى الماء فمنه المطر أصابه ندى من طل ويوم ندي وليلة ندية (tahdhib)؛ الندى ما أصابك من البلل (tahdhib)؛ أصل النداء من الندى أي الرطوبة (mufradat)
- **B006** yağmur nemiyle yetişen otlak bitkisi — yağmur nemiyle yetişen ot ve otlak bitkisi · nemle yetişmiş ağaç
  الندى الكلأ (sihah)؛ تسف الند (sihah)؛ قيل للنبت ندى لأنه عن ندى المطر نبت (tahdhib)؛ يسمى الشجر ندى لكونه منه وذلك لتسمية المسبب باسم سببه (mufradat)
- **B007** hayvan yağı — hayvan yağı
  ربما عبروا عن الشحم بالندى (maqayis)؛ الندى الشحم (sihah)؛ فالندى الأول المطر والثاني الشحم (sihah)؛ قيل للشحم ندى لأنه عن ندى النبت يكون (tahdhib)؛ أراد بالندى الثاني الشحم وبالأول الغيث (tahdhib)
- **B008** iyilik ve vermede eli açıklık — cömertlik, iyilik ve bol verme · eli açık, cömert · vermesi ve iyiliği arttı · arkadaşlarına cömert davranıyor · ondan hiçbir cömertlik payı elde etmedim
  هو أندى من فلان أي أكثر خيرا منه (maqayis)؛ وهو يتندى على أصحابه أي يتسخى (maqayis)؛ الندى الجود (sihah)؛ فلان ندي الكف إذا كان سخيا (sihah)؛ فلان يتندى على أصحابه أي يتسخى (sihah)؛ الندوة السخاء (tahdhib)؛ ندى الخير هو المعروف (tahdhib)؛ أندى الرجل إذا كثر نداه على إخوانه وكذلك انتدى وتندى (tahdhib)؛ يعبر عن السخاء بالندى (mufradat)؛ فلان أندى كفا من فلان وهو يتندى على أصحابه أي يتسخى (mufradat)
- **B009** kötü bir şeye uğrama veya bulaşma ve utandırıcı şeyler — istemediğim bir şeye uğramadım · utandırıcı sözler veya davranışlar · yasak kana bulaşmak
  ما نديت كفي لفلان بشيء يكرهه (maqayis)؛ المنديات المخزيات ويقال ما نديت بشيء تكرهه (sihah)؛ ما نديت كفي بشر وما نديت بشيء تكرهه (tahdhib)؛ من لقي الله ولم يتند من الدم الحرام بشيء (tahdhib)؛ منديات الكلم المخزيات التي تعرف (mufradat)
- **B010** dişi devenin seçkin bir soya çekmesi [kalıp] — dişi deve soyca seçkin develere çekiyor
  هذه الناقة تندو إلى نوق كرام أي تنزع في النسب (sihah)؛ هذه الناقة تندو إلى نوق كرام أي تنزع إليها في النسب (tahdhib)
- **B011** açıkça belirme, bildirme ve yön gösterme — açıkça belirdi · ona bildirdi ve açıkladı · bu yol sana açıkça yön gösteriyor
  نادى ظهر (tahdhib)؛ ناديته علمته (tahdhib)؛ هذا الطريق يناديك (tahdhib)؛ كالكرم إذ نادى من الكافور أي ظهر ظهور صوت المنادي (mufradat)
- **B012** aralıklı çıkan sözler ve uzakta kalan uçlar — zaman zaman ağızdan çıkan sözler · yanlar ve uzak uçlar · ayrılıp uzaklaştı · sudan uzaktaki hurma ağaçları
  نوادي كلامك أي ما يخرج منك وقتا بعد وقت (tahdhib)؛ النوادي النواحي (tahdhib)؛ ندا فلان يندو ندوا إذا اعتزل وتنحى (tahdhib)؛ أراد بنواديه قواصيه (tahdhib)؛ الناديات من النخيل البعيدة من الماء (tahdhib)
- **B013** renk şeridi veya sıcak külde pişirme — etin renginden farklı bir yağ şeridi, gökkuşağı veya bulut kızıllığı · eti sıcak küle gömüp pişirdi · pişmiş yemek
  إذا همز تغير إلى شيء يدل على طرائق وآثار (maqayis)؛ الندأة طريقة من الشحم مخالفة للون اللحم (maqayis)؛ الندأة قوس قزح والحمرة التي تكون في الغيم نحو الشفق (maqayis)؛ ندأت اللحم في الملة دفنته حتى ينضج (maqayis)؛ الندىء مثل الطبيخ (maqayis)

## ECHO ن و د (root_001563): for 43:51 وَنَادَىٰ, 43:77 وَنَادَوْا۟: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## ل ي س (root_001390): 43:51 أَلَيْسَ

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

## م ص ر (root_001428): 43:51 مِصْرَ

- **B001** parmak uçlarıyla azar azar çekme veya dağıtma — memeyi parmak uçlarıyla sağma · sütü yavaş çıkan ve azar azar sağılan dişi hayvan · memede kalan az sütü sağma · bir şeyi ona azar azar vermek · örtüsünü parça parça dağıtmak · keçinin sütünün azalması ve yavaş çıkar hale gelmesi · sütü az koyun · iki parmağıyla sağar
  المصر حلب بأطراف الأصابع (maqayis;ayn;sihah;tahdhib)؛ وناقة مصور لبنها بطيء الخروج (maqayis;ayn;sihah;tahdhib)؛ التمصر حلب بقايا اللبن (maqayis;ayn;sihah;tahdhib)؛ مصر عليه الشيء أعطاه قليلا قليلا (maqayis;ayn)؛ يمصر أي يحتلب بإصبعيه (mufradat)؛ مصر غطاءه تمصيرا إذا فرقه قليلا قليلا (tahdhib)
- **B002** iki şey arasındaki sınır veya engel — iki şey arasındaki sınır ve engel · bütün çevre sınırlarıyla birlikte · iki su arasındaki ayırıcı · onu arada bir sınır haline getirdiler
  المصر وهو الحد (maqayis)؛ المصر الحد والحاجز بين الشيئين (sihah)؛ المصر الحاجز بين الشيئين (tahdhib)؛ الماصر الحاجز بين الماءين (mufradat)؛ بمصورها أي بحدودها (maqayis;sihah;tahdhib;mufradat)
- **B003** sınırları belirlenmiş yönetim ve yerleşim merkezi — kamu işlerinin yürütüldüğü yönetim bölgesi veya kent · bilinen ülke veya belirli kent · yönetim bölgeleri ve kentler · iki belirli kentin ortak adı · sınırları belirlenmiş bir kent kurmak · yerleri kentler halinde düzenlemek
  المصر كل كورة يقسم فيها الفيء والصدقات (maqayis)؛ كل كورة تقام فيها الحدود وتغزى منها الثغور ويقسم فيها الفيء والصدقات (ayn;tahdhib)؛ مصر هي المدينة المعروفة والمصر واحد الأمصار (sihah)؛ المصر اسم لكل بلد ممصور (mufradat)؛ المصران الكوفة والبصرة (sihah;tahdhib)
- **B004** bağırsak ve ona bağlı adlandırmalar — bağırsak · bağırsaklar · doğruluğu tartışmalı toplu bağırsak çoğulu · düşük nitelikli bir hurma türü
  المصير المعى وجمعه مصران (maqayis;ayn;sihah;tahdhib;mufradat)؛ مصران الفأرة ضرب من رديء التمر (maqayis;sihah)؛ المصارين خطأ (ayn;tahdhib)
- **B005** boya görünümüyle nitelenen kumaş — hafif sarı, bitki boyalı veya rengi doymuş kumaş · boyanın benekli çıkması ve kumaşa tam yerleşmemesi
  الممصر ثوب مصبوغ فيه صفرة قليلة (ayn)؛ الثياب الممصرة التي فيها شيء من صفرة ليست بالكثيرة (tahdhib)؛ ثوب ممصر مصبوغ بالعشرق (tahdhib)؛ التمصير في الصبغ أن يخرج المصبوغ مبقعا لم يستحكم صبغه (tahdhib)؛ ثوب ممصر مشبع الصبغ (mufradat)
- **B006** ipliğin bozulup kopması ve kumaşın eskimeden yırtılması — ipliğin kopup biçimini yitirmesi · ipliği bozup kopar duruma getirmek · iplik yumağı · kumaşın eskimeden yarılıp delinmesi
  المصر تقطع الغزل وتمسخه (tahdhib)؛ امصر الغزل إذا تمسخه (tahdhib)؛ الممصرة كبة الغزل (tahdhib)؛ التمصر في الثياب أن تتمشق تخرقا من غير بلى (tahdhib)

## ن ه ر (root_001559): 43:51 ٱلْأَنْهَٰرُ

- **B001** bol su taşıyan doğal akarsu yatağı — taşkın suyun aktığı doğal akarsu yatağı · akarsu yatakları · akarsular veya akarsu yatakları · akarsu yatağı sağlam bir güzergah edindi · su aktı ve kendine bir yatak açtı · bol sulu veya geniş akarsu · suyun kazıp açtığı yatak yeri · kuyu kazısı suya ulaştı
  النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)
- **B002** şafaktan gün batımına aydınlık gündüz — şafaktan güneş batımına kadar süren aydınlık gündüz · aydınlık gündüz süreleri · gündüz vaktinde baskın yapan kimse · gündüzün aydınlığına girdik
  النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)
- **B003** bir şeyi açma veya genişletme — genişlik veya aydınlıkla birlikte genişlik · kanı açıp serbest bırakarak akıttı · yaranın veya yarığın açıklığını genişletti · genişledi · evlerin önleri arasında atık bırakılan açık alan · bağırsağı çözüldü ve akarsu gibi boşaldı · tehlikeler; birleşik bir türetme olarak açıklanan biçim
  أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)
- **B004** sert sözle azarlayıp engelleme [kalıp] — onu sert sözle azarlayıp engelledi
  نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)
- **B005** bazı kuşların yavrusu — türü aktarıma göre değişen bir kuş yavrusu
  النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)
- **B006** fırsat kollayıp gizlice kapma — fırsat kollayıp ani biçimde gizlice kapma
  النهر الدغرة وهي الخلسة (tahdhib)
- **B007** kişi, yer ve yıldızlara ait özel adlar — belirli bir topluluktan bir şairin adı · bir yer adı · sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad
  نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)
- **B008** bulut — bulut
  الناهُور السحاب (tahdhib)

## ج ر ي (root_000240): 43:51 تَجْرِى

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

## ت ح ت (root_000177): 43:51 تَحْتِىٓ

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ب ص ر (root_000121): 43:51 تُبْصِرُونَ

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

## م ه ن (root_001453): 43:52 مَهِينٌ

- **B001** değersizlik, güçsüzlük ve azlık — değersiz, güçsüz ve yetersiz · değersizlik ve azlık · güçsüz kimseler
  أصل صحيح يدل على احتقار وحقارة في الشيء (maqayis)؛ مهين أي حقير (maqayis;sihah)؛ رجل مهين أي حقير ضعيف (ayn;tahdhib)؛ المهانة الحقارة (maqayis)؛ المهانة وهي القلة (tahdhib)
- **B002** hizmet etme veya işte ustalık — hizmet; işte ustalık · onlara hizmet etti · hizmet eden kimse veya köle · kendi toprağında çalıştı · ailesine hizmet edip kendini onların işlerine verdi
  المهن الخدمة والمهنة (maqayis)؛ المهنة الخدمة (ayn;sihah;tahdhib)؛ المهنة الحذاقة في العمل ونحوه (ayn;tahdhib)؛ الماهن الخادم (maqayis;sihah)؛ الماهن العبد (ayn;tahdhib)؛ مهنهم أي خدمهم (ayn;tahdhib)؛ مهن القوم يمهنهم مهنة أي خدمهم (sihah)؛ إذا عمل في ضيعته (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)
- **B003** giysiyi çekmek [kalıp] — giysiyi çekti · çekilmiş giysi
  مهنت الثوب جذبته وثوب ممهون (maqayis)
- **B004** develeri sağmak, özellikle dönüş vaktinde [kalıp] — develeri dönüş vaktinde sağdı
  مهنت الإبل حلبتها (maqayis)؛ مهنت الإبل أمهنها إذا جلبتها عند الصدر (ayn)؛ مهنت الإبل مهنة إذا حليتها عن الصدر (sihah)؛ مهنت الإبل مهنة إذا حلبها عند الصدر (tahdhib)
- **B005** kullanıma koşup yıpratma veya güçten düşürme — onu kullanıp değerden düşürdü · onu güçsüzleştirdi · kendini hizmet için kullandı · var olan koşu gücünü sonuna kadar kullandı ve tüketti · ailesine hizmet edip kendini onların işlerine verdi
  امتهنت الشئ ابتذلته (sihah)؛ أمهنته أضعفته (sihah)؛ امتهن نفسه أي مستخدم (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)؛ أخرج ما عنده من العدو وابتذله (tahdhib)
- **B006** üreme sıvısı yetersiz olduğu için dölleyemeyen — üreme sıvısı az ve güçsüz olduğu için dölleyemeyen erkek hayvan
  للفحل من الإبل والغنم إذا لم يلقح من مائه مهين (tahdhib)؛ من ماء قليل ضعيف (tahdhib)

## ك و د (root_001329): 43:52 يَكَادُ

- **B001** bir şeyi biraz güçlükle aramak — bir şeyi biraz güçlükle aradı
  التماس شيء ببعض العناء؛ كاد يكود كودا ومكادا
- **B002** eyleme ramak kalmak; olumluda yapmamak, olumsuzda güçlükle yapmak — az kalsın yapacaktı, ama yapmadı · güçlükle de olsa yaptı · az kalsın yapacaktı · bir kimse az kalsın yapacaktı
  فأما قولهم في المقاربة كاد فمعناها قارب (maqayis)؛ كاد يفعل كذا يكاد كودا ومكادة أي قارب ولم يفعل (sihah)؛ مجردة فلم يقع ذلك الشيء وقرنت بجحد فقد وقع (maqayis)؛ مجرده ينبئ عن نفي الفعل ومقرونه بالجحد ينبئ عن وقوع الفعل (sihah)
- **B003** vermeyi ya da yapmayı kesin biçimde reddetmek [kalıp] — Hayır, vermeye hiç niyetim yok. · Bunu kesinlikle yapmam. · Bunu ne önemsiyorum ne de yapmaya yanaşıyorum.
  لمن يطلب منك الشيء فلا تريد إعطاءه لا ولا مكادة (maqayis)؛ لا أفعل ذلك ولا كودا (sihah)؛ لا مهمة لي ولا مكادة أي لا أهم ولا أكاد (sihah)
- **B004** istemek, niyet etmek — ondan ne istendiği · onu gizlemek istiyorum
  عرف فلان ما يكاد منه أي ما يراد منه؛ قال بعضهم في قوله أكاد أخفيها أريد أخفيها؛ كادت وكدت وتلك خير إرادة

## ECHO ك ي د (root_001334): for 43:52 يَكَادُ: withheld observed target; not identity

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

## ل ق ي (root_001372): 43:53 أُلْقِىَ, 43:83 يُلَٰقُوا۟

- **B001** yüzü veya ağız köşesini eğrilten hastalık — yüzü ya da ağız köşesini eğrilten yüz hastalığı · bu yüz hastalığına tutulmuş kişi
  اللقوة داء يأخذ في الوجه يعوج منه (maqayis)؛ اللقوة داء في الوجه يقال منه لقي الرجل فهو ملقو (sihah)؛ اللقوة داء يأخذ في الوجه يعوج منه الشدق (tahdhib)
- **B002** biçime bağlı adlandırmalar — kuyuya salınınca başka bir kovayı yukarı çeken kova · gagası eğri veya ağız açıklığı geniş dişi kartal
  اللقوة الدلو التي إذا أرسلتها في البئر وارتفعت أخرى شالت معها (maqayis)؛ اللقوة العقاب سميت لاعوجاجها في منقارها (maqayis)؛ اللقوة العقاب الأنثى سميت لقوة لسعة أشداقها (sihah;tahdhib)
- **B003** çabuk gebe kalma — çabuk gebe kalan dişi deve, kadın veya dişi hayvan · çabuk gebe kalan ile çabuk dölleyenin denk gelmesi; birbirine uygun iki kişi
  اللقوة الناقة السريعة اللقاح (maqayis)؛ اللقوة الناقة السريعة اللقاح وفي المثل لقوة صادفت قبيسا (sihah)؛ السريعات اللقح من جميع الحيوان واللقوة من النساء السريعة اللقح (tahdhib)
- **B004** karşılaşma, karşılama veya karşısında bulunma — karşılaşmak, rastlamak veya yüz yüze gelmek · karşılaşmak ve buluşmak · birini karşılamak · onun tam karşısında oturmak · birini belirli bir şeyle karşılamak · kıyamette Tanrı'nın huzuruna çıkma ve O'na dönüş · öncekilerle sonrakilerin toplanıp herkesin yaptıklarıyla yüzleştiği kıyamet günü
  اللقاء الملاقاة وتوافي الاثنين متقابلين (maqayis)؛ اللقيان كل شيئين يلقى أحدهما صاحبه (ayn;tahdhib)؛ التقوا وتلاقوا بمعنى وتلقاه أي استقبله وجلس تلقاءه أي حذاءه (sihah)؛ اللقاء مقابلة الشيء ومصادفته معا (mufradat)
- **B005** bir şeyi atma, bırakma veya birine yöneltme — atmak, fırlatmak veya bırakmak · birine sevgi yöneltmek veya göstermek · çözmesi için birine bilmece niteliğinde söz yöneltmek
  ألقيته نبذته إلقاء (maqayis)؛ ألقيته أي طرحته وألقيت إليه المودة وألقيت عليه ألقية (sihah)؛ ألقيت عليه ألقية كلمة معاياة يلقيها عليه (tahdhib)؛ الإلقاء طرح الشيء حيث تلقاه ثم صار اسما لكل طرح (mufradat)
- **B006** atılmış veya terk edilmiş şey — atılmış, terk edilmiş veya değersiz görülüp bırakılmış şey · eski dönemde kutsal yapının çevresinde dönerken çıkarılıp bırakılan giysi
  الشيء الطريح لقى والملقى لقى (maqayis)؛ اللقى ما ألقى الناس من خرقة ونحوه (ayn)؛ اللقى بالفتح الشيء الملقى لهوانه وجمعه ألقاء (sihah)؛ اللقى ثوب المحرم يلقيه وكل شيء متروك مطروح كاللقطة (tahdhib)
- **B007** iyilik ya da kötülükle karşılaşma — başına sürekli kötülük gelen bahtsız kişi · kişinin karşılaştığı güçlükler ve kötülükler · iyilik ya da kötülükle karşılaşmak
  رجل لقي شقي لا يزال يلقى شرا والألاقي من عسر وشر (ayn)؛ شقي لقي إتباع له (sihah)؛ رجل شقي لقي لا يزال يلقى شرا (tahdhib)؛ يقال لقي فلان خيرا وشرا (mufradat)
- **B008** kervanı pazar öncesinde karşılayıp malını satın alma [kalıp] — pazara gelmeden önce kervanları karşılayıp mallarını satın alma
  نهي عن التلقي أي يتلقى الحضري البدوي فيبتاع منه متاعه بالرخيص (ayn)؛ نهى النبي عن تلقي الركبان والأجلاب والتلقي هو الاستقبال (tahdhib)
- **B009** sırtüstü uzanma — sırtüstü uzanma
  الاستلقاء على القفا وكل شيء فيه كالانبطاح فيه استلقاء (ayn)؛ استلقى على قفاه (sihah)؛ الاستلقاء على القفا وكل شيء كان فيه كالانبطاح ففيه استلقاء (tahdhib)
- **B010** iki tarafı birbirine kavuşturma — iki kişiyi buluşturup bir araya getirmek · bir çubuğun iki ucunu eğip birbirine kavuşturmak
  لاقيت بين فلان وفلان وبين طرفي القضيب ونحوه حتى تلاقيا واجتمعا (ayn)؛ لاقيت بين فلان وفلان ولاقيت بين طرفي قضيب حنيته حتى تلاقيا والتقيا (tahdhib)
- **B011** sözü aktarıp öğretme veya birinden alıp öğrenme — sözü veya okumayı öğretip tekrarlatmak · sözü birinden alıp öğrenmek · sözleri veya vahiy metnini birinden alıp öğrenmek
  الرجل يلقي الكلام والقراءة أي يلقنه وتلقيت الكلام منه أخذته عنه (ayn)؛ إذ تلقونه بألسنتكم أي يأخذه بعض عن بعض (sihah)؛ فتلقى آدم من ربه كلمات أي أخذها عنه وتعلمها (tahdhib)؛ إنك لتلقى القرآن (mufradat)
- **B012** biçime bağlı adlandırmalar — dağ kenarlarındaki çıkıntılar veya iki dağ arasındaki birleşim yeri · rahim ağzındaki dallar veya üreme organındaki dar geçitler
  الملقى إشراف نواحي الجبل والملقاة والجميع الملاقي شعب رأس الرحم (ayn)؛ الملقاة وجمعها الملاقي شعب رأس الرحم وشعب دون ذلك أيضا (tahdhib)؛ الذي رواه الليث إن صح فهو ملتقى ما بين الجبلين والملقات واحدتها ملقة والميم أصلية (tahdhib)

## س و ر (root_000758): 43:53 أَسْوِرَةٌ

- **B001** şiddetle yükselip atılma — öfkeyle kabarıp taşmak · öfkenin kabarıp taşan şiddeti · savaşta çok güçlü ve atılgan · içkinin keskinliği ve taşkın etkisi · içkinin hızla başa vurup taşkınlık yaratması · birinin başına doğru atılıp onu yakalamak · başı yakalayan köpek · atak, sıçrayıcı ve taşkın
  يدل على علو وارتفاع؛ سار يسور إذا غضب وثار؛ سورة الخمر حدتها وغليانها (maqayis)؛ فلان ذو سورة في الحرب أي ذو بطش شديد؛ السوار الرجل الذي يسور في راسه الشراب؛ بذي عربدة وخفة؛ ساورت فلانا تناولت رأسه (ayn)؛ السور وثوب مع علو؛ يستعمل في الغضب وفي الشراب؛ فلان سوار وثاب (mufradat)
- **B002** çevreleyen yüksek duvar — kenti çevreleyen yüksek duvar · duvara tırmanmak veya duvarı aşmak
  السور جمع سورة وهي كل منزلة من البناء؛ أعالي السور (maqayis)؛ السور حائط المدينة ونحوه؛ تسورت الحائط وسرته سورا (ayn)؛ سور المدينة حائطها المشتمل عليها (mufradat)
- **B003** yüksek kat veya çevrelenmiş yazı bölümü — yüksek yapı katları veya bütünlüklü bölümler · yüksek yapı katı ya da yüksek düzey · kutsal yazının çevrelenmiş bağımsız bölümü
  السور جمع سورة وهي كل منزلة من البناء (maqayis)؛ السورة المنزلة الرفيعة؛ سورة القرآن تشبيها بها لكونه محاطا بها إحاطة السور بالمدينة أو لكونها منزلة كمنازل القمر؛ سورة أنزلناها أي جملة من الأحكام والحكم (mufradat)
- **B004** bilezik ve bilezikle süsleme — bilezik · bir kadına bilezik takıp onu süslemek
  سوار المرأة (maqayis)؛ السوار سوار المرأة والجميع أسورة وأساور والكثير سور (ayn)؛ سوار المرأة معرب؛ سورت الجارية وجارية مسورة؛ أسورة من ذهب؛ أساور من فضة (mufradat)
- **B005** tarihsel komutan veya okçu unvanı — tarihsel bir askerî toplulukta komutan ya da özellikle okçu
  الإسوار من أساورة الفرس وهم القادة (maqayis)؛ الأسوار من أساورة كسرى أي قواده (ayn)؛ الإسوار من أساورة الفرس أكثر ما يستعمل في الرماة؛ فارسي معرب (mufradat)
- **B006** deri yaslanma minderi — deriden yapılmış yaslanma minderi
  المسورة متكأ من أدم وجمعها المساور (ayn)

## خ ف ف (root_000427): 43:54 فَٱسْتَخَفَّ

- **B001** ağırlığın veya yükün az olması ve azaltılması — ağırlığı azalmak · az ağırlıklı, taşıması kolay · ağırlık, yük veya güçlük azlığı · ağırlığını azaltmak · yükünü azaltmak · ağırlığı az bulmak · durumu kolaylaşıp yükü azalmak · taşınması kolay eşya · dile kolay gelen söz
  خف الشيء يخف خفة وهو خفيف (maqayis;sihah)؛ الخفة خفة الوزن وخفة الحال (ayn;tahdhib)؛ التخفيف ضد التثقيل واستخفه خلاف استثقله (sihah)؛ خففه تخفيفا وتخفف تخففا وخف المتاع وكلام خفيف على اللسان (mufradat)؛ خفوا في السجود ولا ترسل نفسك إرسالا ثقيلا (tahdhib)
- **B002** hızla yola çıkmak — topluluk hızla yola çıktı · konaktan hızlı ayrılış, yola çıkma vakti · topluluğun binekleri hızlıydı · hızlı deve kuşu
  خف القوم ارتحلوا (maqayis)؛ الخفوف سرعة السير من المحلة وحان الخفوف وخف القوم إذا ارتحلوا مسرعين (ayn;tahdhib)؛ أخف القوم إذا كانت دوابهم خفافا (sihah)؛ خفوا عن منازلهم ارتحلوا منها في خفة (mufradat)؛ الخفانة النعامة السريعة (ayn)
- **B003** sayısı veya ölçülen payı az olmak — topluluğun sayısı azaldı · kalabalıkları azaldı · arkadaşlarından küçük bir topluluk içinde · ölçülen iyi işleri az geldi
  خرج فلان في خف من أصحابه أي في جماعة قليلة وخف القوم خفوفا أي قلوا وقد خفت زحمتهم (sihah)؛ فمن خفت موازينه إشارة إلى كثرة الأعمال الصالحة وقلتها (mufradat)
- **B004** kararlılığını yitirip ölçüsüzce yönelmek — kişinin düşüncesiz ve ölçüsüz davranması · çabuk coşan, yerinde duramayan · sevinç onu hareketlendirdi · seni kararından oynatmasın · bilgisizliğini kullanıp yanlış yola sürükledi
  وخفة الرجل طيشه وخفته في عمله (ayn;tahdhib)؛ خفيف القلب في توقده فهو خفاف (ayn;tahdhib)؛ الخفيف فيمن يطيش (mufradat)؛ لا يستخفنك أي لا يزعجنك ويزيلنك عن اعتقادك (mufradat)؛ استخفه الفرح إذا ارتاح لأمر (tahdhib)؛ استخفه فلان إذا استجهله فحمله على اتباعه في غيه (tahdhib)
- **B005** aşağılayıp değersiz saymak — onu aşağılayıp değersiz saydı · hakkımı önemsemedi
  استخف به أهانه (sihah)؛ استخف فلان بحقي إذا استهان به (tahdhib)
- **B006** deve ayağı ucu veya kapalı ayak giysisi — devenin tabanlı ayak ucu · ayağa giyilen kapalı ayak giysisi · sandaldan daha kalın ayak giysisi · deve türünden yarış hayvanı · deve veya deve kuşunun ayak ucu
  الخف مجمع فرسن البعير (ayn;tahdhib)؛ الخف ما يلبسه الإنسان (ayn;tahdhib)؛ الخف واحد أخفاف البعير والخف واحد الخفاف التي تلبس والخف في الأرض أغلظ من النعل (sihah)؛ الخف فمن الباب لأن الماشي يخف وهو لابسه وخف البعير منه أيضا (maqayis)؛ الخف الملبوس وخف النعامة والبعير تشبيها بخف الإنسان (mufradat)؛ لا سبق إلا في خف أو نصل أو حافر فالخف الإبل ها هنا (tahdhib)
- **B007** uyup boyun eğmek — ona uyup boyun eğdi · dişi eşekler erkek eşeğe uydu · hizmetine çevikçe koştu · topluluğunu kendisiyle birlikte harekete geçirip kendine uydurdu
  خف فلان لفلان إذا أطاعه وانقاد له وخفت الأتن لعيرها إذا أطاعته (tahdhib)؛ استخف قومه فأطاعوه أي حملهم أن يخفوا معه أو وجدهم خفافا في أبدانهم وعزائمهم (mufradat)
- **B008** develerin birbirini izleyerek art arda gelmesi [kalıp] — develerin birbirini izlediği tek sıra halinde
  جاءت الإبل على خف واحد إذا تبع بعضها بعضا مقطورة كانت أو غير مقطورة (tahdhib)
- **B009** köpek sesi veya giysi hışırtısı; kanat çırparak uçan kuş — köpeklerin çıkardığı ses · yeni gömleği hareket ettirip hışırtı çıkarmak · kanatlarını çırparak uçan kuş
  أصوات الكلاب فيقال لها الخفخفة فهو قريب من الباب (maqayis)؛ خفخف إذا حرك قميصه الجديد فسمعت له خفخفة أي صوتا (tahdhib)؛ الخفخوف الطائر الذي يصفق بجناحيه إذا طار (tahdhib)

## ط و ع (root_000956): 43:54 فَأَطَاعُوهُ, 43:63 وَأَطِيعُونِ

- **B001** zorlanmadan boyun eğme ve kolay yönlenme — zorlamanın karşıtı olan isteyerek boyun eğme · emre uyma ve gereğini yerine getirme · ona boyun eğdi · emrini yerine getirdi · zorlanmadan uyan kimse · uyan ve boyun eğen kimse · çok söz dinleyen ve kolay uyan kimse · kolay yönlendirilen ve söz dinleyen · elin altında ve tasarrufa hazır · dizginle kolay yönlendirilen · yatak arkadaşına uyum gösteren · dili buna dönmüyor · güçlüklere alışkın ve onları göğüsleyen
  أصل صحيح واحد يدل على الإصحاب والانقياد (maqayis); الطوع نقيض الكره (ayn;tahdhib;mufradat); طاع له إذا انقاد له (ayn;sihah;tahdhib;mufradat); فرس طوع العنان (ayn;sihah;tahdhib); بعير طيع سلس القياد (tahdhib); لسانه لا يطوع بكذا (sihah)
- **B002** taraflar arasında uyum gösterme — ona uyum gösterdi veya onu izledi · taraflar arasında uyum gösterme · uyumlu olma ve kolay söz dinleme niteliği
  لمن وافق غيره قد طاوعه (maqayis); إذا وافقك فقد طاوعك (ayn;tahdhib); الطواعية اسم لما يكون مصدر المطاوعة (ayn;tahdhib); المطاوعة الموافقة (sihah)
- **B003** bir işi yapabilecek güç ve elverişlilik — bir işi yapabilecek güç ve elverişli durum · bir şeyi yapabildi veya yapabilir oldu
  الاستطاعة مشتقة من الطوع (maqayis;ayn); الاستطاعة الإطاقة (sihah); الاستطاعة استفالة من الطوع وذلك وجود ما يصير به الفعل متأتيا (mufradat); يقال ما أستطيع وما اسطيع وما أسطيع وما أستيع (tahdhib)
- **B004** yapabilir hale gelmek için kendini zorlama — işi yapabilir hale gelene kadar kendini zorladı · yapmaya kendini zorladı veya isteyerek üstlendi
  تطاوع لهذا الأمر حتى تستطيعه (maqayis;ayn;sihah;tahdhib); تطوع أي تكلف استطاعته (maqayis;sihah;tahdhib); وتطوع كذا تحمله طوعا (mufradat)
- **B005** yükümlü olmadığı iyiliği gönüllü yapma — yükümlü olmadığı şeyi gönüllü olarak verdi veya yaptı · zorunlu olmayan iyiliği gönüllü yapma · savaş hizmetine gönüllü katılan topluluk
  التبرع بالشيء قد تطوع به (maqayis); لا يقال هذا إلا في باب الخير والبر (maqayis); التطوع ما تبرعت به مما لا يلزمك فريضته (ayn;sihah;tahdhib); المطوعة القوم الذين يتطوعون بالجهاد (ayn;sihah;tahdhib); التطوع في التعارف التبرع بما لا يلزم كالتنفل (mufradat)
- **B006** iç benliğin işi kolay gösterip yöneltmesi — nefsi ona işi kolay gösterdi ve ona yöneltti
  قد تطوع لك طوعا إذا انقاد (ayn); فطوعت له نفسه رخصت وسهلت (sihah); فتابعته نفسه (tahdhib); شجعته (tahdhib); أعانته على ذلك وأجابته إليه (tahdhib); سمحت وسهلت له نفسه (tahdhib); أسمحت له قرينته وانقادت له وسولت (mufradat)
- **B007** otlak veya meyvenin yararlanılabilir hale gelmesi — otlağı bulup ondan istediği kadar yedi · otlak ona genişleyip otlamaya elverişli oldu · meyveli ağaç ürünü olgunlaşıp toplanabilir oldu · otlak ona genişleyip otlamayı mümkün kıldı
  أطاع لها الكلأ إذا أصابت فأكلت منه ما شاءت (ayn); أطاع النخل والشجر إذا أدرك ثمره وأمكن أن يجتنى (sihah); أطاع له المرتع إذا اتسع له وأمكنه من الرعي (sihah;tahdhib); قد يقال في هذا الموضع طاع (tahdhib)

## ECHO س ط ع (root_000706): for 43:54 فَأَطَاعُوهُ, 43:63 وَأَطِيعُونِ: withheld observed target; not identity

- **B001** havada uzama, yükselme veya yayılma — havada yükselmek, uzamak veya yayılmak · yukarı doğru uzanan sabah aydınlığı · sabah aydınlığı · okun göğe yükselip parlaması · misk kokusunun burnuna ulaşması
  أصل يدل على طول الشيء وارتفاعه في الهواء (maqayis)؛ كل شيء ينتشر فينبسط نحو البرق والغبار والريح الطيبة (ayn)؛ سطع الغبار والرائحة والصبح إذا ارتفع (sihah)؛ سطع ضوؤه في السماء والبرق يسطع في السماء وسطع السهم فشخص في السماء وسطعت الرائحة إذا فاحت (tahdhib)
- **B002** boyun uzunluğu — boyun uzunluğu · başını kaldırıp boynunu uzatmak · uzun boyunlu erkek devekuşu · uzun boyunlu dişi devekuşu
  السطع وهو طول العنق وظليم أسطع ونعامة سطعاء (maqayis)؛ السطع طول العنق نعامة سطعاء (sihah)؛ ظليم أسطع إذا كان عنقه طويلا والأنثى سطعاء وفي عنقه سطع أي طول (tahdhib)
- **B003** ev direği — ev veya çadır direği · direğe benzetilen uzun deve
  السطاع عمود من عمد البيت (maqayis)؛ السطاع عمود البيت (sihah)؛ السطاع عمود من أعمدة البيت وللبعير الطويل سطاع تشبيها بسطاع البيت (tahdhib)
- **B004** deve boynundaki uzunlamasına damga — deve boynundaki uzunlamasına damga · boynu uzunlamasına damgalı deve
  السطاع سمة في عنق البعير بالطول يقال بعير مسطع (sihah)؛ السطاع من سمات الإبل في العنق بالطول وناقة مسطوعة وإبل مسطعة (tahdhib)
- **B005** avuç ya da parmak vuruşu ve sesi — bir şeye avuç içiyle veya parmakla vurma · vuruş sesi · vuruş veya vuruş sesi
  السطع ارتفاع صوت الشيء إذا ضربت عليه شيئا يقال سطعة (maqayis)؛ السطع أن تسطع شيئا براحتك أو بإصبعك ضربا وسمعت لضربته سطعا يعني صوت الضربة (tahdhib)
- **B006** belirli bir dağın özel adı — belirli bir dağın özel adı
  أما السطاع في شعر هذيل فهو جبل بعينه (maqayis)؛ السطاع اسم جبل بعينه (tahdhib)

## ف س ق (root_001156): 43:54 فَٰسِقِينَ

- **B001** itaatten çıkıp Tanrı'nın buyruğuna karşı gelme ve kötülüğe yönelme — itaatten çıkma, Tanrı'nın buyruğunu bırakma ve kötülüğe yönelme · itaatten çıkıp buyruğa karşı gelmek; kötülük etmek · Tanrı'nın buyruğuna karşı gelmek ve itaatinden çıkmak · itaatten çıkmış, dinsel kuralları bütünüyle ya da kısmen çiğneyen kimse · itaatten çıkma; günah işleme ya da Tanrı'ya ortak koşma · itaatten çıkmış ve kötülüğe yönelmiş adam · sürekli olarak itaatten çıkan ve dinsel kuralları çiğneyen kimse
  الفسق وهو الخروج عن الطاعة (maqayis)؛ الفسق الترك لأمر الله؛ الميل إلى المعصية (ayn;tahdhib)؛ فسق الرجل يفسق فسقا وفسوقا أي فجر؛ فسق عن أمر ربه أي خرج (sihah)؛ الفسوق معناه الخروج؛ الشرك ويكون الإثم (tahdhib)؛ خرج عن حجر الشرع؛ أعم من الكفر (mufradat)
- **B002** taze hurmanın kabuğundan çıkması [kalıp] — taze hurma tanesinin kabuğundan çıkması
  فسقت الرطبة عن قشرها (maqayis;sihah)؛ فسقت الرطبة من قشرها لخروجها منه (tahdhib)؛ فسق الرطب إذا خرج عن قشره (mufradat)
- **B003** küçültmeli bir kötüleme adıyla anılan fare — küçültmeli bir kötüleme adıyla anılan fare
  إن الفأرة فويسقة (maqayis)؛ الفويسقة الفأرة (ayn;sihah)؛ سميت فويسقة لخروجها من جحرها (tahdhib)؛ سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها (mufradat)

## ء س ف (root_000032): 43:55 ءَاسَفُونَا

- **B001** güçlü üzüntü; yitirilene yönelik kullanımda hayıflanma — yitirdiği şeye üzülüp hayıflanmak · güçlü üzüntü · üzülüp hayıflanmak · çabuk üzülüp ağlayan, ince duygulu kimse · üst konumdaki kişi beni üzdü
  يدل على الفوت والتلهف (maqayis)؛ الأسف الحزن في حال (ayn)؛ الأسف أشد الحزن وقد أسف على ما فاته وتأسف أي تلهف (sihah)؛ الأسيف السريع الحزن والكآبة (tahdhib)
- **B002** öfkelenme ve öfkelendirme — öfkeli; kimi kullanımlarda üzüntülü ve hayıflanan · ona öfkelenmek · onu öfkelendirmek
  الأسف الغضبان (maqayis)؛ آسفونا أي أغضبونا (ayn)؛ أسف عليه أسفا أي غضب وآسفه أغضبه (sihah)؛ آسفونا أغضبونا والأسيف والأسف الغضبان (tahdhib)؛ الأسيف الغضبان (mufradat)
- **B003** köleleştirilmiş veya boyunduruk altında çalıştırılan kişi — köleleştirilmiş veya boyunduruk altında çalıştırılan kişi
  الأسيف العبد لأنه مقهور محزون (ayn)؛ الأسيف العبد (sihah;tahdhib)؛ يستعار للمستخدم المسخر (mufradat)
- **B004** toprağın bitirememesi veya devenin semirememesi — ince, az bitkili veya bitkisiz toprak · bir türlü semirmeyen deve
  الأسافة الأرض التي لا تنبت شيئا والجمل الأسيف الذي لا يكاد يسمن (maqayis)؛ الأسيفة والأسافة الأرض القليلة النبات (ayn)؛ أرض أسيفة رقيقة لا تكاد تنبت شيئا (sihah)؛ الأسافة رقة الأرض ويقال للأرض الرقيقة أسيفة (tahdhib)
- **B005** Kureyş'e ait bir putun özel adı — Kureyş'e ait bir putun adı · Kureyş'e ait iki putun adları
  إساف اسم صنم كان لقريش (ayn;tahdhib)؛ إساف ونائلة صنمان كانا لقريش (sihah)
- **B006** ansızın gelen ölüm — ansızın gelen ölüm
  يقال لموت الفجأة أخذة أسف (tahdhib)

## غ ر ق (root_001080): 43:55 فَأَغْرَقْنَٰهُمْ

- **B001** suda batıp boğulma veya boğma; bunaltıcı bir şey içinde kalma — suda boğulmak; borç, bela veya nimet içinde kalmak · boğulan kimse; borç ya da belanın bastırdığı kimse · suda boğulmakta olan · birini suda boğmak · boğulmak üzere olanın çaresiz yakarışı
  الغرق في الماء (maqayis); رجل غرق وغريق رسب في الماء وابتلي بالدين والبلوى تشبيها به (ayn); غرق في الماء غرقا وأغرقه غيره (sihah); الغرق الرسوب في الماء ويشبه به الذي ركبه الدين وغمرته البلايا (tahdhib); الغرق الرسوب في الماء وفي البلاء وفلان غرق في نعمة فلان تشبيها بذلك (mufradat)
- **B002** sıvıyla boğarak öldürme ve bunun genelleşmiş öldürme kullanımı — sıvıda boğarak öldürme; genel olarak öldürme · ebenin doğum sıvısını bebeğin burnuna kaçırarak onu öldürmesi
  والتغريق القتل وغرقته القابلة في ماء السلا ثم تخرجه ميتا (ayn); والتغريق القتل وكانت تغرق المولود في ماء السلى حتى يموت ثم جعل كل قتل تغريقا (sihah); غرقت القابلة الولد وذلك إذا لم ترفق بالمولود حتى تدخل السابياء أنفه فتقتله (tahdhib)
- **B003** gözün yaşla, toprağın suyla dolması — suya doymuş toprak · gözlerin yaşla dolması, fakat yaşların dışarı taşmaması
  والغرقة أرض تكون في غاية الري وأغرورقت العين والأرض (maqayis); اغرورقت عيناه دمعتا (sihah); وأغرورقت عيناه إذا امتلأتا دموعا ولم تفيضاها (tahdhib)
- **B004** yayı son sınırına kadar çekme [kalıp] — yayı veya oku son çekiş sınırına kadar germek · oku atmak için yayı son sınırına kadar çekmek; aşırılığa varmak
  أغرقت في القوس مددتها غاية المد (maqayis); أغرقت النبل وغرقته بلغت به غاية المد في القوس (ayn); أغرق النازع في القوس أي استوفى مدها (sihah); الإغراق في النزع أن ينزع حتى يشرب بالرصاف (tahdhib)
- **B005** bir alanı tümüyle kapsama; sürüye karışıp öne geçme — atların arasına karışıp sonra hepsini geçmek · bütünüyle kapsama ve hiçbir bölümü dışarıda bırakmama · nefesi verirken soluk kapasitesini sonuna kadar kullanma · insanların bütün bakışlarını kendine çekmek · hayvanın iri gövdesinin göğüs ve karın kayışlarını doldurup dar bırakması
  اغترق الفرس في الخيل إذا خالطها ثم سبقها (maqayis); الفرس إذا خالط الخيل ثم سبقها يقال اغترقها (ayn); الاستغراق الاستيعاب واغتراق النفس استيعابه في الزفير (sihah); فلانة تغترق نظر الناس وقد اغترق التصدير والبطان واستغرقه (tahdhib)
- **B006** bir içimlik süt ya da başka içecek — bir içimlik veya küçük bir kap kadar süt ya da başka içecek
  الغرقة من اللبن قدر ثلث الإناء والجمع غرق (maqayis); الغرقة القليل من اللبن قدر قدح أو أقل (ayn); الغرقة بالضم مثل الشربة من اللبن وغيره والجمع غرق (sihah); الغرقة مثل الشربة من اللبن وغيره من الأشربة وجمعها غرق (tahdhib)
- **B007** yumurtanın iç kabuğu ya da yenilen beyazı — yumurtanın iç kabuğu veya yenilen beyaz kısmı
  الغرقىء قشرة البيض الداخلة (ayn); الغرقيء البياض الذي يؤكل واتفق النحويون على همز الغرقيء وأن همزته ليست بأصلية (tahdhib)
- **B008** baştan başa süslenmiş gem [kalıp] — baştan başa süslenmiş veya gümüşle kaplanmış gem
  لجام مغرق بالفضة أي محلى (sihah); لجام مغرق إذا عمته الحلية (tahdhib)

## س ل ف (root_000733): 43:56 سَلَفًا

- **B001** önce gelme, önde bulunma ve geçmişte kalma — geçti, öne geçti · öncekiler, geçmiş atalar ve akrabalar · önden giden, önceki · önden giden topluluk · geçmiş topluluklar ve kuşaklar · ordunun öncü bölüğü · topluluk bölüm bölüm art arda geldi
  أصل يدل على تقدم وسبق (maqayis)؛ السلف الذين مضوا (maqayis)؛ سلف يسلف سلوفا أي مضى (ayn;sihah)؛ الأمم السالفة الماضية (ayn;mufradat)؛ القوم السلاف المتقدمون (maqayis;sihah)؛ السالفة والسلاف المتقدمون في حرب أو سفر (mufradat)؛ سلاف العسكر مقدمتهم (tahdhib)؛ جاء القوم سلفة سلفة إذا جاء بعضهم في إثر بعض (tahdhib)
- **B002** ilk akan özsu veya bir şeyin seçkin özü — üzümün sıkılmadan önce akan özsuyu · bir şeyin en duru ve seçkin özü · üzüm içkisinin seçkin özü; bir görüşte kalan özsu
  السلاف السائل من عصير العنب قبل أن يعصر (maqayis)؛ سلافة كل شيء خلاصته (ayn)؛ السلاف ما سال من عصير العنب قبل أن يعصر (sihah)؛ السلافة من الخمر أخلصها وأفضلها (tahdhib)؛ سلافة الخمر ما بقي من العصير (mufradat)
- **B003** ana yemekten önce verilen küçük yiyecek — ana yemekten önce verilen küçük yiyecek · topluluğa ana yemekten önce küçük yiyecek sundu
  السلفة المعجل من الطعام قبل الغداء (maqayis)؛ السلفة ما يتسلف الرجل فيأكل قبل غدائه (ayn)؛ السلفة ما يتعجله الرجل من الطعام قبل الغداء (sihah)؛ الطعام الذي يتعلل به قبل الغذاء السلفة (tahdhib)؛ السلفة ما يقدم من الطعام على القرى (mufradat)
- **B004** suya giden sürünün önündeki dişi deve — suya varan sürünün önündeki dişi deve
  السلوف الناقة تكون في أوائل الإبل إذا وردت (maqayis)؛ السلوف الناقة تكون في أوائل الإبل إذا وردت الماء (sihah)
- **B005** ödünç verilen veya vadeli mal için peşin ödenen para — ödünç verilen para veya vadeli mal için peşin bedel · bedeli peşin, teslimi vadeli satış · ona ödünç para verdim · ondan ödünç para istedim
  السلف في البيع وهو مال يقدم لما يشتري نساء (maqayis)؛ أسلفته مالا أقرضته والسلف من القرض (ayn)؛ السلف نوع من البيوع يعجل فيه الثمن (sihah)؛ السلف في المعاملات له معنيان القرض والسلم (tahdhib)؛ السلف ما قدم من الثمن على المبيع (mufradat)
- **B006** bacanaklık veya eltilik bağı — karısının kız kardeşinin kocası, bacanak · kız kardeşlerle evli iki erkek, bacanaklar · erkek kardeşlerle evli iki kadından biri, elti
  السلف سلف الرجال وهما اللذان يتزوج هذا أختا وهذا أختا (maqayis)؛ السلفان رجلان تزوجا بأختين (ayn;tahdhib)؛ سلف الرجل زوج أخت امرأته (sihah)؛ المرأة سلفة لصاحبتها إذا تزوجت أختان بأخوين (ayn;tahdhib)
- **B007** boynun yan, ön veya üst bölümü — boynun yan yüzü, üstü veya ön bölümü · atın boynunun önde uzanan bölümü
  السالفتين وهما صفحتا العنق (maqayis)؛ السالفة أعلى العنق وسالفة الفرس هاديته (ayn;tahdhib)؛ السالفة ناحية مقدم العنق (sihah)؛ السالفة صفحة العنق (mufradat)
- **B008** iri torba — iri torba
  السلف وهو الجراب (maqayis)؛ السلف جراب ضخم والجميع سلوف (ayn)؛ السلف بالتسكين الجراب الضخم (sihah)؛ السلف الجراب وجمعه سلوف (tahdhib)
- **B009** erkek çocuğun üreme organının uç derisi — erkek çocuğun üreme organının uç derisi · erkek çocuğun üreme organının uç derisi
  يقال إن القلفة تسمى سلفا (maqayis)؛ السلف غرلة الصبي (ayn)؛ تسمى غرلة الصبي سلفة (tahdhib)
- **B010** toprağı ekim için düzleme, düzlenmiş parça ve düzleme taşı — toprağı ekim için araçla düzledi · toprağı ekim için düzledi · düzlenmiş arazi · toprak düzlemeye yarayan taş veya araç · düzlenmiş arazi parçası
  أسلفت الأرض للزرع إذا سويتها (maqayis)؛ سلفت الأرض بالمسلفة إذا سويتها للزرع (ayn)؛ سلفت الأرض أسلفها سلفا إذا سويتها بالمسلفة (sihah)؛ أرض الجنة مسلوفة هي المستوية (sihah;tahdhib)؛ الحجر الذي تسوى به الأرض مسلفة (tahdhib)
- **B011** keklik yavrusu — keklik yavruları · keklik yavrusu
  السلفان أولاد الحجل واحدها سلف (ayn)؛ السلفان أولاد الحجل الواحد سلف (sihah)؛ السلف والسلك من أولاد الحجل وجمعه سلفان (tahdhib)؛ واحد السلفان سلف وهو الفرخ (tahdhib)
- **B012** kırk beş yaşlarına gelmiş kadın [kalıp] — kırk beş yaşlarına gelmiş kadın
  المسلف من النساء التي بلغت خمسا وأربعين ونحوها (ayn)؛ المسلف من النساء التي بلغت خمسا وأربعين أو نحوها (sihah)؛ المسلف من النساء التي قد بلغت خمسا وأربعين ونحوها (tahdhib)
- **B013** deri ayakkabı için ince deri iç astar — deri ayakkabının iç astarı yapılan ince deri
  السلفة جلد رقيق يجعل بطانة للخفاف أحمر وأصفر (ayn)؛ السلفة جلد رقيق يجعل بطانة للخفاف (tahdhib)
- **B014** uzun ok ucu — uzun ok ucu
  السلوف من نصال السهام ما طال (ayn)؛ السلوف من نصال السهام ما طال (tahdhib)

## ج د ل (root_000229): 43:58 جَدَلًۢا

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

## خ ل ف (root_000433): 43:60 يَخْلُفُونَ, 43:63 تَخْتَلِفُونَ, 43:65 فَٱخْتَلَفَ

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

## س و ع (root_000760): 43:61 لِّلسَّاعَةِ, 43:66 ٱلسَّاعَةَ, 43:85 ٱلسَّاعَةِ

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

## م ر ي (root_001416): 43:61 تَمْتَرُنَّ

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

## ECHO م و ر (root_001456): for 43:61 تَمْتَرُنَّ: withheld observed target; not identity

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

## ت ب ع (root_000175): 43:61 وَٱتَّبِعُونِ

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

## ع د و (root_000993): 43:62 عَدُوٌّ, 43:67 عَدُوٌّ

- **B001** hakkı aşan saldırganlık — uygun sınırı aşma · açık haksızlık ve saldırganlık · hakkı çiğneyerek sınırı aşma · sınırı aşan haksızlık · ona saldırıp malını alma ya da onu vurma · baskın yapan atlılar
  التعدي تجاوز ما ينبغي أن يقتصر عليه (maqayis;ayn)؛ العدوان الظلم الصراح (maqayis;sihah)؛ الاعتداء مجاوزة الحق (mufradat)؛ العادية الخيل المغيرة (ayn;sihah)
- **B002** yaya ya da atla koşma — yaya koşu ya da at koşusu · koşmak · atın iyi ve çok koşması
  العَدْو هو الحضر (maqayis;ayn;sihah)؛ يقال من عدو الفرس عدوان أي جيد العدو وكثيره (maqayis)؛ بالمشي فيقال له العدو (mufradat)
- **B003** düşmanlık ve düşman — düşman, dostun karşıtı · düşmanlar · düşmanlar · düşmanlık
  العَدُوّ ضد الولي والجمع الأعداء (sihah)؛ العداوة والمعاداة (sihah;mufradat)؛ يقال للواحد والاثنين والجمع عَدُوّ (maqayis)
- **B004** aşma, dışarıda bırakma ve öteye geçirme — belirtilen ögeyi kapsam dışında tutma · konuyu geçip başkasına yönelme · eylemin etkisini nesneye geçirme
  ما عدا زيدا أي ما جاوز زيدا (maqayis;ayn)؛ عدا فعل يستثنى به (sihah)؛ ما عدا كذا يستعمل في الاستثناء (mufradat)؛ عد عن هذا الأمر أي تجاوزه وخذ في غيره (maqayis)
- **B005** yetkiliden hakkını almasını isteme — yetkiliden yardım ve hakkını almasını isteme
  العَدْوى طلبك إلى وال أو قاض أن يعديك على من ظلمك (maqayis)؛ طلبك إلى وال ليعديك على من ظلمك (ayn;sihah)
- **B006** hastalığın bulaşması — hastalığın bulaşması · hastalığın birinden ötekine geçmesi
  العَدْوى ما يقال إنه يعدي من جرب أو داء (maqayis;ayn)؛ ما يعدي من جرب أو غيره ومجاوزته من صاحبه إلى غيره (sihah)
- **B007** işten alıkoyan uğraş veya engel — işten alıkoyan uğraş veya kötü olay · zamanın getirdiği engeller ve sıkıntılar · bir iş beni senden alıkoydu
  العادية شغل من أشغال الدهر يعدوك عن أمرك (maqayis;ayn)؛ عوادي الدهر عوائقه (sihah)؛ عدواء الشغل موانعه (sihah)
- **B008** iki avı peş peşe ele geçirme — iki avı peş peşe izleyip ele geçirme
  العِداء أن يعادي الفرس أو الكلب أو الصياد بين صيدين (maqayis)؛ العِداء الموالاة بين الصيدين (sihah)؛ فعادى عداء بين ثور ونعجة أي أعدى أحدهما إثر الآخر (mufradat)
- **B009** boyunca uzanan yan ve kıyı — bir şeyin eni ya da boyu boyunca uzanan yanı · ırmak kıyısı boyunca uzanan yan · vadinin yanı ve kıyısı
  العَداء طوار كل شيء (maqayis;sihah)؛ لزمت عداء النهر وطريق يأخذ عداء الجبل (maqayis)؛ العدوة جانب الوادي وحافته (sihah)؛ بالعدوة الدنيا أي الجانب المتجاوز للقرب (mufradat)
- **B010** sert, kuru ve engebeli yer — sert, kuru ve engebeli yer
  العَدْواء الأرض اليابسة الصلبة (maqayis)؛ العدواء المكان الذي لا يطمئن من قعد عليه (sihah)؛ مكان ذو عدواء أي غير متلائم الأجزاء (mufradat)
- **B011** develerin otladığı yaz yeşermesi — bahar geçince yeşeren ve develerin otladığı yaz bitkisi
  العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر فترعاه الإبل (maqayis)؛ العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر صغار الشجر فترعاه الإبل (sihah)
- **B012** eğrilik ve güçlük — eğrilik ve güçlük
  العَنْدَأْوَة التواء وعسر وهو من العداء (maqayis)

## ECHO ع و د (root_001058): for 43:62 عَدُوٌّ, 43:67 عَدُوٌّ: withheld observed target; not identity

- **B001** geri dönme ve yeniden yapma — geri dönmek · geri dönüş; yeniden yönelme · bir şeyi yeniden yapmak veya yinelemek · bir şeyin yeniden yapılmasını istemek · önceki işe yeniden dönmek · aynı soruyu tekrar tekrar sormak · ateşi yeniden nüksetmek · önceden yenmişken yeniden sunulan yemek · sık sık dönen; geri dön buyruğu
  أصل يدل على تثنية في الأمر (maqayis)؛ بدأ ثم عاد (maqayis;ayn)؛ عاد إليه يعود عودة وعودا رجع (sihah)؛ العود الرجوع إلى الشيء بعد الانصراف عنه (mufradat)؛ استعدته الشيء فأعاده (sihah)؛ تعاود القوم في الحرب وغيرها (sihah)؛ عاودته الحمى وعاوده بالمسألة (sihah)؛ عواد بمعنى عد (sihah)؛ العوادة ما أعيد من الطعام (sihah)
- **B002** dönüş yeri ve son varış — son varış; dönüş zamanı veya yeri
  المعاد كل شيء إليه المصير (maqayis)؛ والآخرة معاد للناس (maqayis)؛ الحج معاد الحاج (ayn)؛ لرادك إلى معاد يعني مكة (ayn)؛ المعاد المصير والمرجع (sihah)؛ الآخرة معاد الخلق (sihah)؛ المعاد يقال للعود وللزمان الذي يعود فيه وقد يكون للمكان الذي يعود إليه (mufradat)
- **B003** tek söz söylememek — ne söze başlamak ne de karşılık vermek
  رأيت فلانا ما يبدئ وما يعيد أي ما يتكلم ببادية ولا عادية (ayn)؛ ما يبدئ وما يعيد أي ما يتكلم ببادئة ولا عائدة (maqayis)
- **B004** tekrarla alışkanlık ve yatkınlık kazanma — alışkanlık; tekrarla yerleşen davranış · alışmak; alışkanlık edinmek · ısrarla sürdüren; deneyimli · alıştığı için yapabilen · çiftleşmeye alışmış erkek hayvan
  العادة الدربة والتمادي في شيء حتى يصير له سجية (maqayis;ayn)؛ المواظب على الشيء المعاود (maqayis;ayn)؛ بطل معاود (maqayis;ayn)؛ العادة معروفة والجمع عاد وعادات (sihah)؛ عاده واعتاده وتعوده (sihah)؛ عود كلبه الصيد فتعوده (sihah)؛ فلان معيد لهذا الأمر أي مطيق له (sihah;ayn)؛ المعيد الفحل الذي قد ضرب في الإبل مرات (sihah)؛ العادة اسم لتكرير الفعل والانفعال حتى يصير ذلك سهلا (mufradat)
- **B005** hasta veya yas ziyareti — hasta ziyareti · hasta ziyaretçileri · insanların ziyaret ettiği felaket veya yas hâli
  العيادة أن تعود مريضا (maqayis)؛ عدت المريض أعوده عيادة (sihah)؛ من العود عيادة المريض (mufradat)؛ الرجال عواد المريض والنساء عود (ayn)؛ فلان في معادة أي مصيبة يغشاه الناس (ayn)؛ لآل فلان معادة أي أمر يغشاهم الناس له (maqayis)
- **B006** kişiye dönen yarar ve iyilik — kişiye ulaşan yarar, şefkat veya bağış · bu senin için daha yararlı veya elverişlidir · iyilik yaptıktan sonra iyiliğini artırdı
  عاد فلان بمعروفه إذا أحسن ثم زاد (ayn)؛ العائدة وهو المعروف والصلة (maqayis)؛ ما أكثر عائدة فلان علينا (maqayis)؛ العائدة العطف والمنفعة (sihah)؛ هذا الشيء أعود عليك من كذا أي أنفع (sihah)؛ هذا الأمر أعود عليك أي أرفق بك (tahdhib)؛ العائدة اسم ما عاد به عليك المفضل من صلة أو فضل (tahdhib)؛ العائدة كل نفع يرجع إلى الإنسان (mufradat)
- **B007** yeniden gelen özel gün veya hâl — bayram; tekrarlanan toplanma veya sevinç günü · kişiye yeniden gelen kaygı, sevgi veya hâl · bayrama katılmak
  العيد ما يعتاد من خيال أو هم (maqayis)؛ العيد كل يوم مجمع (maqayis)؛ لأنه يعود كل عام (maqayis)؛ عيد قد مضى ذكره في محله لأن ذلك هو الأصل (maqayis-crossref)؛ العيد ما اعتادك من هم أو غيره (sihah)؛ العيد واحد الأعياد (sihah)؛ وقد عيدوا أي شهدوا العيد (sihah)؛ العيد ما يعاود مرة بعد أخرى (mufradat)؛ يستعمل العيد في كل يوم فيه مسرة (mufradat)
- **B008** gücü kalmış yaşlı deve — gücü kalmış yaşlı deve · yaşlı dişi deve veya koyun · ileri yaşa ulaşmak · savaşta yaşlı ve deneyimli kişilerden yardım al
  الجمل المسن فهو يسمى عودا (maqayis)؛ كأنه عاود الأسفار والرحل مرة بعد مرة (maqayis)؛ العود الجمل المسن وفيه سورة أي بقية (ayn)؛ العود المسن من الإبل (sihah)؛ زاحم بعود أو دع (sihah)؛ العود الجمل المسن الذي فيه بقية قوة (tahdhib)؛ عود الرجل تعويدا إذا أسن (tahdhib)؛ لا يقال عود إلا لبعير أو لشاة (tahdhib)؛ أنثى عودة (tahdhib)؛ البعير المسن اعتبارا بمعاودته السير والعمل (mufradat)
- **B009** eski yol ve köklü geçmiş — eski ve yeniden kullanılan yol · köklü saygınlık · eski akrabalık bağı
  العود الطريق القديم (ayn)؛ رحم عودة يعني قديمة (ayn)؛ السودد العود (maqayis)؛ الطريق القديم عود (maqayis)؛ العود الطريق القديم (sihah)؛ سودد عود أي قديم (sihah)؛ طريق عود إذا كان عاديا (tahdhib)؛ العود الطريق القديم الذي يعود إليه السفر (mufradat)
- **B010** tahta parçası, tütsülük odun veya telli çalgı — tahta parçası veya ince dal · tütsü için yakılan kokulu odun · telli müzik aleti
  الأصل الآخر فالعود وهو كل خشبة دقت (maqayis)؛ كل خشبة عود (maqayis)؛ العود الذي يتبخر به معروف (maqayis)؛ العود بالضم من الخشب واحد العيدان والأعواد (sihah)؛ العود الذي يضرب به (sihah)؛ العود الذي يتبخر به (sihah)؛ العود في الأصل الخشب الذي من شأنه أن يعود إذا قطع (mufradat)؛ خص بالمزهر المعروف وبالذي يتبخر به (mufradat)
- **B011** bağlayıcı eş sözünden ilgili davranışa dönüş — eş hakkındaki bağlayıcı sözden sonra ilgili davranışa dönmek
  ثم يعودون لما قالوا (mufradat)؛ عند أهل الظاهر هو أن يقول للمرأة ذلك ثانيا (mufradat)؛ عند أبي حنيفة العود في الظهار هو أن يجامعها (mufradat)؛ عند الشافعي هو إمساكها (mufradat)؛ يحمل على فعل ما حلف له أن لا يفعل (mufradat)
- **B012** biçime bağlı adlandırmalar — eski bir kavmin adı · eski; eski bir kavme bağlanan · erkek adı · bir kavme veya erkek deveye bağlanan soylu develer
  عاد قبيلة وهم قوم هود (sihah)؛ شيء عادي أي قديم كأنه منسوب إلى عاد (sihah)؛ عادياء اسم رجل (sihah)؛ العيدية نجائب منسوبة قالوا نسبت إلى عاد (maqayis)؛ العيدية إبل منسوبة إلى فحل يقال له عيد (mufradat)

## ح ز ب (root_000315): 43:65 ٱلْأَحْزَابُ

- **B001** insan topluluğu veya herhangi bir bütünün bölüğü — topluluk, bölük veya aynı yönelimde birleşen takım · bir kişinin görüşünü izleyen yandaşları ve destekçileri · savaşmak üzere birleşen topluluklar · topluluğun bir araya gelip ayrı takımlar oluşturması · topluluğun birbirini kollayarak ittifak kurması · insanları toplayıp ayrı takımlara ayırmak
  الحزب الجماعة من الناس والطائفة من كل شيء حزب (maqayis)؛ الحزب أصحاب الرجل على رأيه وأمره وكل طائفة تكون أهواؤهم واحدة (ayn)؛ حزب الرجل الذين يميلون إليه وتحازب القوم إذا مالأ بعضهم بعضا (jamhara)؛ الحزب الطائفة وتحزبوا تجمعوا والأحزاب الطوائف التي تجتمع على محاربة الأنبياء (sihah)؛ كل قوم تشاكلت قلوبهم وأعمالهم فهم أحزاب وتحزب القوم إذا تجمعوا (tahdhib)؛ الحزب جماعة فيها غلظ وأنصار الله (mufradat)
- **B002** kişiye ayrılan bölüm, pay veya sıra — düzenli okunan metin veya ibadet bölümü · okunacak metni bölümlere ayırmak veya ondan düzenli bir bölüm almak · maldaki payım · suya varma sırası
  قرأ حزبه من القرآن (maqayis)؛ الحزب الورد وقد حزبت القرآن (sihah)؛ ورد الرجل من القرآن والصلاة حزبه والحزب النصيب أعطني حزبي من المال والحزب النوبة في ورود الماء (tahdhib)
- **B003** kişinin başına gelen veya ona isabet eden iş — bir işin kişinin başına gelmesi, ona isabet etmesi veya ağır gelmesi · kişinin başına inen sıkıntı · ağır veya kişinin başına gelen iş
  حزب الأمر يحزب حزبا إذا نابك (ayn)؛ حزبني الأمر إذا اشتد علي وأمر حازب وحزيب (jamhara)؛ حزبه أمر أي أصابه (sihah)؛ حزب الأمر إذا نابك والحازب من الشغل ما نابك (tahdhib)
- **B004** arazide sert veya engebeli, kimi kullanımda yüksek; bedende kalın, kısa veya sıkı yapı — sert veya engebeli arazi; kimi kullanımda yüksek yer · kalın veya sıkı yapılı, kimi biçimde kısa insan veya hayvan · kısa ve kalın yapılı
  الحزباء الأرض الغليظة والحزابية الحمار المجموع الخلق (maqayis)؛ الحزباءة أرض حزنة غليظة وعير حزابية وركب حزابية (ayn)؛ الحزابي الغليظ القصير والحزباء الأرض الغليظة والحزباءة أخص منه والحنزاب أيضا مثل الحزابي وهو الغليظ القصير (sihah)؛ الحزباءة أرض غليظة حزنة وبعير حزابية ورجل حزاب وحزابية أي غليظ وحمار حزابية (tahdhib)
- **B005** yaşlı kadını belirten özel söz biçimi — yaşlı kadın · yaşlı kadın; sesçe değişik biçim
  الحيزبون العجوز وزادوا فيه الياء والواو والنون (maqayis)؛ الحيزبون العجوز النون زائدة (ayn)؛ الحيزبون العجوز (sihah)؛ الحيزنون العجوز والنون زائدة والحيزبون العجوز (tahdhib)
- **B006** karada yetişen havuç türünün özel adı — karada yetişen bir havuç türü
  الحنزاب جزر البر والقسط جزر البحر (sihah)

## ء ل م (root_000046): 43:65 أَلِيمٍ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ب غ ت (root_000135): 43:66 بَغْتَةً

- **B001** beklenmedik anda ortaya çıkma veya hazırlıksız yakalama — beklenmedik anda ortaya çıkma; hazırlıksız yakalama · ansızın; beklenmedik biçimde · onu ansızın hazırlıksız yakaladı · onu beklenmedik anda hazırlıksız yakaladı · beklenmedik anda hazırlıksız yakalama · onunla ansızın karşılaştım · ansızın, hazırlıksız yakalayacak biçimde · tekrarlanan ani gelişler; beklenmedik sürprizler · ansızın ve beklenmedik biçimde ortaya çıktı
  البغت وهو أن يفجأ الشيء (maqayis)؛ البغت البغتة؛ باغته مباغتة أي فاجأه بغتة (ayn)؛ البغت المفاجأة؛ باغته الأمر مباغتة وبغاتا وبغتة إذا فاجأه؛ الباغوت أعجمي معرب وهو عيد للنصارى (jamhara)؛ البغت أن يفجأك الشيء؛ لقيته بغتة أي فجأة؛ بغتات العدو أي فجآته (sihah)؛ البغت مفاجأة الشيء من حيث لا يحتسب؛ بغت كذا فهو باغت (mufradat)

## ش ع ر (root_000798): 43:66 يَشْعُرُونَ

- **B001** bedensel kıl ve kılımsı ince tüylenme — insanda ve başka canlılarda çıkan kıl · tek bir kıl teli · başının ya da bedeninin kılları çok veya uzun olan · toynak çevresinde derinin bitip kılın başladığı halka biçimli bölüm · dölütün kılları çıkmak · yüzeyi ince tüylü bir şeftali türü · ince tüylü ya da kıla dadanan bir sinek türü · kıllı veya tüylü diye nitelenen büyük bela
  الشعر معروف والواحدة شعرة (maqayis;ayn;sihah;tahdhib;mufradat)؛ رجل أشعر طويل شعر الرأس والجسد (maqayis;ayn;tahdhib)؛ الأشعر ما استدار بالحافر (maqayis;ayn;sihah;tahdhib;mufradat)؛ الشعراء فاكهة يعلوها كالزغب وذبابة (maqayis;sihah;mufradat)
- **B002** sık ağaçlı veya bol bitkili yer ve buna bağlı bitki adı — çok ve sık ağaçlık; yumuşak alçak yerdeki ağaç topluluğu · çok ve sık ağaç · ağacı ya da bitkisi bol çayır · belirli otları çıkaran kumluk · yeşilimsi boz renkli bir çalı veya tuzcul bitki türü
  الشعار الشجر أرض كثيرة الشعار (maqayis;sihah;tahdhib)؛ الشعراء الشجر الكثير (maqayis;sihah)؛ روضة شعراء كثيرة الشجر ورملة شعراء تنبت النصي (maqayis;tahdhib)؛ الشعران ضرب من الرمث (ayn)
- **B003** arpa, arpa tanesi ve biçimce ona benzetilen küçük şeyler — arpa · bir arpa tanesi · bıçak ağzını sapa tutturmaya yarayan küçük metal parça · arpa tanesi biçiminde altın ya da gümüş süs parçası · küçük hıyarlar
  الشعير وهو معروف (maqayis;tahdhib;mufradat)؛ الشعيرة الحديدة التي تجعل مساكا لنصل السكين (maqayis;ayn;sihah;tahdhib)؛ الشعيرة من الحلي تتخذ أمثال الشعير (ayn;tahdhib)؛ الشعارير صغار القثاء (maqayis;ayn;sihah;tahdhib)
- **B004** tene değen iç giysi ve onun gibi en yakın ya da içine sinmiş olan — öteki giysilerin altında tene doğrudan değen içlik · sen herkesten daha yakın ve özelsin · kaygıyı kalbine giydirdi; kaygıyı içine yerleştirdi · korkuyu içine gömüp sürekli duydu · sevgi onu hastalıkla sarıp kuşattı · onu, tenine değen iç giysisi yapın
  الشعار ما ولي الجسد من الثياب (maqayis;ayn;sihah;tahdhib;mufradat)؛ أشعر فلان قلبي هما أي ألبسه بالهم (ayn)؛ استشعر فلان خوفا (sihah)؛ أشعره الحب مرضا (maqayis;sihah;mufradat)
- **B005** dikkatle fark edip bilme ve bunu sağlayan duyular — bir şeyi fark edip bilmek ve algılamak · keşke bilsem · bunu sana ne bildirir; nereden bileceksin · duyular ve algı yolları
  شعرت بالشيء إذا علمته وفطنت له (maqayis;ayn;sihah;tahdhib)؛ ليت شعري أي ليتني علمت (maqayis;ayn;sihah;tahdhib)؛ وما يشعرك أي ما يدريك (ayn;tahdhib)؛ المشاعر الحواس (sihah;mufradat)
- **B006** ayırt edici belirti veya çağrı, törensel gösterge ve kanatarak belirleme — savaşta birbirini tanımaya yarayan ortak çağrı veya belirti · kutsal ziyaretin belirtileri, törenleri ve uygulamaları · kutsal törenin yapıldığı belirlenmiş yer · kutsal ziyaret için adanmış büyükbaş hayvan · adanmış hayvanı, adandığı anlaşılsın diye hörgücünden yaralayıp kanatma · birini mızraklayıp derinden yaralama ve kanatma
  الشعار الذي يتنادى به القوم في الحرب (maqayis;ayn;sihah;tahdhib;mufradat)؛ شعائر الله أعلام الحج وأعماله ومناسك الحج (maqayis;ayn;sihah;tahdhib;mufradat)؛ المشعر موضع المنسك (maqayis;ayn;sihah;tahdhib;mufradat)؛ إشعار الهدي أن يطعن في سنامه حتى يسيل الدم (maqayis;ayn;sihah;tahdhib;mufradat)؛ الإشعار الإدماء بطعن أو رمي (tahdhib)
- **B007** ölçülü uyaklı söz ve onu söyleme sanatı — ölçülü ve uyaklı söz; koşuk · ölçülü uyaklı söz söyleyen kimse; ozan · ozanlar · ölçülü söz söyleyerek yarışıp üstün gelmek · ozanlık taslayan veya ölçülü söz söylemeye çalışan kimse · mecazen yalan söz veya yanıltıcı kanıt
  الشعر القريض المحدد بعلامات (ayn;tahdhib)؛ الشعر واحد الأشعار والشاعر جمعه الشعراء (sihah)؛ سمي الشاعر لأنه يفطن لما لا يفطن له غيره (maqayis;ayn;sihah;mufradat)؛ صار اسما للموزون المقفى من الكلام (mufradat)؛ شاعرته فشعرته أي غلبته بالشعر (sihah)؛ الشعر يعبر عن الكذب والشاعر الكاذب (mufradat)
- **B008** yıldız, dağ, boy ve çocuk oyunu için gelenekleşmiş özel adlar — bilinen parlak bir yıldız · belirli bir dağın adı · Yemen kökenli bir boyun veya boy atasının adı · bilinen bir Arap boyunun adı · erkek çocukların oynadığı, adı tekil kullanılmayan bir oyun · bir kişiye verilmiş küçültmeli ozan lakabı
  الشعرى كوكب (ayn;sihah;tahdhib;mufradat)؛ شعر جبل (ayn;tahdhib)؛ الأشعر أبو قبيلة من اليمن (sihah)؛ بنو الشعيراء قبيلة (ayn;tahdhib)؛ الشعارير لعبة للصبيان (ayn;sihah;tahdhib)

## خ ل ل (root_000435): 43:67 ٱلْأَخِلَّآءُ

- **B001** aralık ve aradan geçen açıklık — iki şey arasındaki açıklık · evlerin, toplulukların veya bulutların arası · kumlar arasından geçen yol · aralıklara girip ilerlemek · bulutların yağmur çıkan açıklıkları
  الخلل بين الشيئين؛ الفرجة بين الشيئين (sihah;mufradat)؛ خلال الدار وما بين بيوتها (ayn)؛ خلالكم بمعنى وسطكم (tahdhib)؛ الخل الطريق في الرمل (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** ihtiyaç ve giderilmesi gereken eksiklik — ihtiyaç, yoksulluk ve darlık · yoksul veya muhtaç kişi · bir şeye ihtiyaç duymak · muhtaç duruma düşmek · ayrılan kişinin bıraktığı yeri doldur
  الخلة الفقر (maqayis;sihah)؛ نزلت به خلة أي حاجة وخصاصة (ayn)؛ الخلة الحاجة (tahdhib;mufradat)؛ خل الرجل إذا احتاج (tahdhib)؛ اسدد خلته يريد الفرجة التي ترك (sihah;tahdhib)
- **B003** içten dostluk ve yakın arkadaşlık — içten dostluk ve yakınlık · yakın dost, sevgili veya yoldaş · sevgi bağı veya dost · biriyle dostluk kurmak · dostum veya sevgilim
  الخليل الذي يخالك (maqayis)؛ فلان خلتي (jamhara;tahdhib)؛ الخل الود والصديق (sihah)؛ الخلال المخالة والمصادقة (sihah;tahdhib)؛ الخلة المودة (mufradat)؛ الخليل الحبيب والصادق والناصح والرفيق (tahdhib)
- **B004** etten düşüp cılızlaşma — ince ve az etli adam · eti azalıp cılızlaşmak · bedeni zayıflayıp incelmek · ince yapılı genç deve · zayıf genç deve veya az etli et; bir aktarımda tersine semiz
  الرجل الخل وهو النحيف الجسم (maqayis)؛ رجل خل أي مهزولون (ayn)؛ الرجل النحيف المختل الجسم (sihah)؛ خل لحمه أي قل ونحف (sihah;tahdhib;mufradat)؛ فصيل مخلول أي مهزول (sihah;tahdhib)
- **B005** aralığa sokulan ince araçla delip tutturma — aralığa sokulan ince çubuk veya metal parça · giysiyi ince çubukla tutturmak · emmesini önlemek için yavrunun dilini veya burnunu yarmak · ince çubukla diş aralarını temizlemek · ok veya mızrakla delip geçirmek
  خللك الكساء على نفسك بالخلال (maqayis)؛ الخلال اسم خشبة أو حديدة يخل بها (ayn)؛ الخلال العود الذي يتخلل به وما يخل به الثوب (sihah)؛ خل ثوبه بخلال يخله (tahdhib;mufradat)؛ خللت لسان الفصيل (sihah)؛ اختله بسهم (sihah)؛ طعنته فاختللت فؤاده بالرمح (tahdhib)
- **B006** sirke ve içeceğin sirkeleşmesi — sirke · içecek bozulup ekşiyerek sirkeye dönüşmek · sirkeleşme sınırına gelmiş ekşi şarap
  الخل معروف (sihah)؛ الاختلال من الخل الذي يتخذ من عصير العنب والتمر (ayn)؛ شراب فلان قد خلل أي فسد (tahdhib)؛ الخلة الخمرة الحامضة (sihah;tahdhib;mufradat)
- **B007** ekşi olmayan tatlı mera otu — ekşi olmayan tatlı mera otu · tatlı otlu, ekşi otsuz arazi · develeri tatlı mera otunda otlatmak
  الخلة من النبات ما ليس بحمص (ayn)؛ الخلة بالضم ما حلا من النبت (sihah)؛ الخلة كل نبت حلو (tahdhib)؛ أرض خلة وخلل الأرض التي لا حمض بها (tahdhib)؛ أخللت الإبل أي رعيتها في الخلة (sihah)
- **B008** kişisel özellik ve nitelikler — iyi veya kötü kişisel özellik · kişinin özellikleri ve nitelikleri
  الخلة الخصلة (sihah)؛ الخلال جمع الخلة وهي الخصلة (tahdhib)؛ فيه خلة صالحة وخلة سيئة (tahdhib)؛ فسرت الخلة بالحاجة والخصلة (mufradat)
- **B009** incelikle ilişkili geleneksel somut adlar — eski veya dokusu incelmiş kumaş · kılıç kını, kın astarı veya ince yay kayışı · boyunda başa bağlanan damar · ayak bileziği veya takıldığı yer
  الخل الثوب البالي (ayn;sihah;tahdhib)؛ الخلة جفن السيف (maqayis;sihah;tahdhib)؛ السيور التي تلبس ظهور السيتين (maqayis;sihah)؛ الخل عرق في العنق (maqayis;ayn;sihah;tahdhib)؛ الخلخال من الباب أيضا لدقته (maqayis)
- **B010** işleyişi aksatan zayıflık ve bozukluk — işte, savaşta veya görüşte aksaklık ve bozukluk · terk ederek veya eksilterek aksatmak
  الخلل في الحرب وفي الأمر كالوهن (ayn;tahdhib;mufradat)؛ الخلل أيضا فساد في الأمر (sihah)؛ أخل بهم إذا غاب عنهم (ayn)؛ أخل الوالي بالثغور إذا قلل الجند بها (ayn)؛ أخل الرجل بمركزه أي تركه (sihah)
- **B011** genel kapsamı bazılarına özgülemek — genel tutmayıp yalnızca bir bölümüne özgülemek · yağmurun yalnızca bazı yerlere düşmesi
  خلل الشيء إذا لم يعم (maqayis)؛ عم في دعائه وخل أي خص (sihah;tahdhib)؛ خلل بالتشديد أي خصص (tahdhib)؛ تخلل المطر إذا خص ولم يكن عاما (sihah)
- **B012** ne iyiliği ne kötülüğü olmak [kalıp] — onda ne iyilik ne de kötülük var
  ما فلان بخل ولا خمر أي لا خير فيه ولا شر (sihah;tahdhib)؛ الخل والخمر الخير والشر (tahdhib)
- **B013** olgunlaşmamış ham hurma — olgunlaşmamış ham hurma; bazı aktarımda tekili ayrıca belirtilir
  الخلال وهو البلح (maqayis)؛ الخلال بالفتح البلح (sihah)؛ الخلال البلح وهي بلغة أهل البصرة واحدتها خلالة (tahdhib)

## ECHO خ ل و (root_000436): for 43:67 ٱلْأَخِلَّآءُ: withheld observed target; not identity

- **B001** içinde ya da üzerinde bir şey bulunmaması — bir şeyin başka bir şeyden yoksun veya sıyrılmış olması · evde ya da yerde kimsenin veya hiçbir şeyin kalmaması · boş yer; ayrıca ayakyolu veya açık arazi · bir yeri boş bulmak
  تعري الشيء من الشيء (maqayis)؛ خلا الشيء يخلو خلوا فهو خال (ayn;sihah;tahdhib)؛ خلت الدار وأخلت (maqayis;tahdhib)
- **B002** başkalarını dışarıda bırakarak baş başa kalmak veya tek şeyle yetinmek — biriyle baş başa buluşmak · biriyle baş başa bir araya gelmek · özel görüşme ya da boş bir oturum yeri istemek · yalnız sütle veya etle yetinmek
  خلوت به خلوة وخلاء (sihah;tahdhib)؛ خلوت إليه إذا اجتمعت معه في خلوة (sihah)؛ استخليت الملك فأخلاني (ayn;tahdhib)؛ خلا فلان على اللبن أو على اللحم (tahdhib)
- **B003** zaman içinde geçip gitmiş olmak — geçmiş çağlar veya geçmiş topluluklar · geçip gitmek · ölmek
  القرون الخالية المواضي (maqayis;sihah)؛ خلا قرن أي مضى (ayn;tahdhib)؛ خلا فيها نذير أي مضى وأرسل (sihah)؛ خلا فلان أي مات (tahdhib)
- **B004** genel hükmün dışında tutmak [kalıp] — birini genel hükmün dışında tutmak · belirli çekimi gerektiren dışlama kalıbı · yalnızca sana öğüt vermiş olmam dışında
  ما في الدار أحد خلا زيد وزيدا (maqayis;ayn;sihah;tahdhib)؛ ما خلا زيدا نصبت لا غير (sihah;tahdhib)؛ خلا أني وعظتك أي إلا أني وعظتك (ayn;tahdhib)
- **B005** artık kınanacak bir yanın yok [kalıp] — artık kınanacak bir yanın yok
  افعل ذاك وخلاك ذم أي عداك (maqayis)؛ وخلاك ذم أي أعذرت وسقط عنك الذم (sihah;tahdhib)
- **B006** bir kişiyle, işle veya suçla bağ ve sorumluluk taşımamak [kalıp] — senden ve sorumluluğundan uzağım · bu işten uzak ve sorumsuz
  أنت خلو منه (ayn)؛ أنا منك خلاء أي براء (sihah)؛ أنا خلي من هذا وخلاء (tahdhib)؛ خلا إذا تبرأ من ذنب (tahdhib)
- **B007** kaygı ve keder taşımamak — kaygısız, tasasız
  الخلي الخالي من الغم (maqayis)؛ الخلي الذي لا هم له (ayn;tahdhib)؛ الخلى الخالى من الهم خلاف الشجي (sihah)
- **B008** engeli kaldırıp serbest bırakmak veya iki tarafı baş başa bırakmak [kalıp] — serbest bırakmak; yolunu açmak · ikisini baş başa bırakmak veya aralarındaki engeli kaldırmak
  خليت عنه أي أرسلته (ayn)؛ خليت عنه خليت سبيله فهو مخلى (sihah)؛ أخليت فلانا وصاحبه وخليت بينهما (ayn)؛ خاليته أي تاركته (tahdhib)
- **B009** eşi ya da çocuğu olmama ve boşanmış sayılma [kalıp] — boşanmış ya da eşi ve çocuğu olmayan kadın · boşama niyetiyle söylenen ayrılık sözü · eşi olmayan erkek
  امرأة خلية كناية عن الطلاق (maqayis;sihah)؛ أنت خلية برية فتطلق بها المرأة (tahdhib)؛ امرأة خلية لا أزواج لهن ولا أولاد (tahdhib)؛ رجل خلي لا نساء لهم (tahdhib)
- **B010** yavrusundan ayrılıp başka yavruya alıştırılan dişi deve — yavrusu ayrılmış ve başka yavruya alıştırılmış dişi deve
  الخلية الناقة تعطف على غير ولدها (maqayis)؛ الخلية الناقة خلت من ولدها ورعت ولد غيرها (ayn)؛ الخلية الناقة تعطف مع أخرى على ولد واحد (sihah)؛ الخلية الناقة تنتج فينحر ولدها (tahdhib)
- **B011** gemi; özellikle büyük veya çekilmeden ilerleyen gemi — gemi, özellikle büyük gemi
  الخلية السفينة (maqayis)؛ الخلية السفينة تسير من ذاتها من غير جذب (ayn)؛ الخلية السفينة العظيمة (sihah)؛ الخلية العظيمة من السفن (tahdhib)
- **B012** arıların barındığı ve bal yaptığı yuva — arıların bal yaptığı yuva veya kovan
  الخلية بيت النحل (maqayis;sihah)؛ الخلى والخلية الموضع الذي يعسل فيه النحل (ayn)؛ الخلية ما يعسل النحل فيه من راقود أو طين أو خشب (tahdhib)
- **B013** ot ve onu biçip kökünden alma — ot veya kökünden sökülmüş bitki · otu biçmek ya da kökünden koparmak · biçilmiş otun konduğu torba · kılıcın kesip biçmesi
  الخلى مقصور هو الحشيش (maqayis;ayn;sihah;tahdhib)؛ الخلاة كل بقلة قلعتها (tahdhib)؛ اختليته وبه سميت المخلاة (ayn;sihah;tahdhib)؛ السيف يختلى أي يقطع (maqayis;sihah)
- **B014** karşı karşıya gelmek veya aradaki barışı sona erdirmek — biriyle güreşmek veya karşı karşıya ayrışmak · düşmanla aradaki ateşkesi ve anlaşmayı sona erdirmek · birine karşı çıkmak
  خاليت فلانا إذا صارعته (ayn;tahdhib)؛ خلاني فلان مخالاة أي خالفني (tahdhib)؛ خاليت العدو أي تركت ما بيني وبينه من الموادعة (tahdhib)؛ عدو مخال أي ليس له عهد (tahdhib)
- **B015** alay etmek veya kandırmak [kalıp] — biriyle alay etmek · birini kandırmak
  خلا به إذا سخر به (maqayis)؛ خلوت به أي سخرت به (sihah)؛ فلان خلا لفلان أي خادعه (ayn)؛ يخلو بفلان إذا خادعه (tahdhib)
- **B016** koruyucusuz olduğu için kolay hedef olan kimse veya şey — koruyucusu olmadığı için kolay hedef olan kimse veya şey
  الخلاة ممن يطمع فيه ولا حافظ له (maqayis)

## خ و ف (root_000447): 43:68 خَوْفٌ

- **B001** bir belirtiye dayanarak kötü bir şey bekleme korkusu — korku · korkmak · korku hali · korku halleri · korku ve sakınma · korkan kimse · çok korkan adam · korkan topluluk · korkan topluluk · kork! · onun başına bir şey gelmesinden korkmak
  الخوف ضد الأمن خاف يخاف خوفا (jamhara خفو)؛ والخيفة مثل الخوف والجمع خيف (jamhara خيف)؛ خاف الرجل يخاف خوفا وخيفة ومخافة فهو خائف؛ والخيفة الخوف والجمع خيف وأصله الواو (sihah)؛ الخوف توقع مكروه عن أمارة مظنونة أو معلومة ويضاد الخوف الأمن (mufradat)؛ أصل واحد يدل على الذعر والفزع؛ خفت الشيء خوفا وخيفة (maqayis 992)؛ الخيف فجمع خيفة وليس من هذا الباب وقد ذكر في باب الواو بعد الخاء (maqayis 1001)؛ الخيفة الخوف (ayn)
- **B002** korku doğurma ya da korkulur kılma — korkutma veya korkuyla sakındırma · başkasını korkutma · korkutucu · korkulan veya tehlikeli · insanların korktuğu tehlikeli yol · Tanrı'nın korku uyandırarak sakındırması
  ومنه التخويف والإخافة؛ طريق مخوف يخافه الناس ومخيف يخيف الناس؛ خوفت الرجل جعلت فيه الخوف؛ خوفت الرجل أي صيرته بحال يخافه الناس (ayn)؛ الإخافة التخويف؛ وجع مخيف أي يخيف من رآه؛ طريق مخوف لأنه لا يخيف وإنما يخيف فيه قاطع الطريق (sihah)؛ التخويف من الله تعالى هو الحث على التحرز؛ ذلك يخوف الله به عباده؛ الشيطان يخوف أولياءه (mufradat)
- **B003** korkuda yarışıp ötekinden daha çok korkma — korkuda yarışıp ötekinden daha çok korkmak
  خاوفه فخافه يخوفه غلبه بالخوف أي كان أشد خوفا منه (sihah)؛ خاوفني فلان فخفته أي كنت أشد خوفا منه (maqayis)
- **B004** bir şeyden alarak eksiltme — bir şeyi eksiltip ondan bir bölüm almak
  والتخوف التنقص (ayn)؛ وتخوفه أي تنقصه (sihah)؛ تخوفناهم أي تنقصناهم تنقصا اقتضاه الخوف منه (mufradat)؛ تخوفت الشيء أي تنقصته فهو الصحيح الفصيح إلا أنه من الإبدال والأصل النون من التنقص (maqayis)
- **B005** korkunun kişide dışa vurması — korkunun kişide dışa vurması
  والتخوف ظهور الخوف من الإنسان (mufradat)
- **B006** arıcı ya da su taşıyıcısının deri torbası veya üstlüğü — arıcı veya su taşıyıcısının deri torbası, kabı ya da üstlüğü · aynı eşyanın küçük biçimi
  الخافة تصغيرها خويفة واشتقاقها من الخوف وهي جبة يلبسها العسال والسقاء والخافة العيبة (ayn)؛ الخافة خريطة من أدم يشتار فيها العسل (sihah)

## ح ز ن (root_000317): 43:68 تَحْزَنُونَ

- **B001** sevinç karşıtı ağır üzüntü — ağır üzüntü ve iç sıkıntısı · üzülmek, üzgün duruma gelmek · üzmek, üzüntüye düşürmek · üzmek, üzgün duruma getirmek · üzüntüye uğramış, üzgün · üzüntü veren, üzücü · üzüntüye bürünmek, üzülmek · okurken sesi üzgün bir tona inceltme
  الحزن والحزن لغتان وأصابه حزن شديد (ayn;tahdhib)؛ الحزن والحزن خلاف السرور (sihah)؛ خشونة في النفس لما يحصل فيه من الغم ويضاده الفرح (mufradat)؛ الحزن معروف يقال حزنني الشيء يحزنني وقد قالوا أحزنني (maqayis)؛ صوت محزن وأمر محزن ولا يقال حازن (ayn;tahdhib)؛ يقرأ بالتحزين إذا أرق صوته به (sihah)
- **B002** sert ve engebeli arazi — sert ve engebeli arazi ya da kaba yapılı hayvan · engebeli ve taşlı arazi parçaları · tek bir sert ve engebeli yer; kaba yapılı dişi hayvan · arazinin ya da hayvanın sertliği ve kabalığı · engebeli arazide otlayan deve · huysuz koyun · sert ve engebeli araziye girmek · yüksek, sert ve engebeli arazi
  الحزن من الأرض والدواب ما فيه خشونة (ayn;tahdhib)؛ الحزن ما غلظ من الأرض وفيها حزونة (sihah)؛ الجبال الغلاظ الواحدة حزنة (sihah)؛ أول حزون الأرض قفافها وجبالها وقواقيها وخشنها ورضمها (tahdhib)؛ الحزن وهو ما غلظ من الأرض (maqayis)؛ خشونة في الأرض (mufradat)؛ الحزم من الأرض والأصل حزن والحزم أرفع من الحزن (maqayis-hazm)؛ الحزون الشاة السيئة الخلق (sihah)
- **B003** kaygı duyulan aile ve yakın çevre — kişinin durumları için kaygılandığı aile, ev halkı ve yakınlar · Arapların Arap olmayan topluluklara yüklediği, Arap konukları barındırma, ağırlama ve yol azığı verme yükümlülüğü
  حزانتك أهلك ومن تتحزن له (maqayis)؛ الحزانة عيال الرجل الذي يتحزن بأمرهم (sihah;tahdhib)؛ كيف حشمك وحزانتك أي من تتحزن بأمرهم (tahdhib)؛ تسمى سفنجقانية العرب على العجم حزانة (ayn;tahdhib)

## ECHO ح ز ز (root_000316): for 43:68 تَحْزَنُونَ: withheld observed target; not identity

- **B001** kesme, çentme ve kesik izi oluşturma — kesik veya çentik açma · kesmek ya da çentik açmak · kesip ayırmak, özellikle boynu kesmek · parçalara ayrılma · çok sayıda çentik veya tırtık bulunması · uzunlamasına kesilmiş et parçası · devenin dirseğinin göğüs altını kesip kanatmasıyla oluşan iz · kesilen veya çentilen yer · bıçakla kesilip bükülen bir işaretle damgalanmış deve
  الفرض في الشيء بحديدة أو غيرها (maqayis)؛ الحز قطع في اللحم غير بائن والفرض في العظم والعود (ayn;tahdhib)؛ حزه واحتزه أي قطعه والتحزز التقطع (sihah)؛ حزة من لحم إذا قطع طولا (sihah;tahdhib)؛ تحزيز كأسنان المنجل وأطراف الأسنان (sihah;tahdhib)
- **B002** gönlü kemiren öfke ve acı — gönülde öfke, acı veya yanma · gönlü kemiren öfke, sitem veya keder · yanlış davranış gönülleri tırmalar ve incitir
  الحزاز ما في النفس من غيظ فإنه يحز القلب (maqayis)؛ الحزازة وجع في القلب من غيظ ونحوه (ayn;sihah;tahdhib)؛ كل شيء حك في صدرك فقد حز (maqayis;sihah)؛ الإثم حزاز القلوب (maqayis;sihah)
- **B003** baş derisi kepeği — baş derisindeki kepek · baş derisindeki tek bir kepek pulu
  الحزاز وهو هبرية في الرأس (maqayis)؛ الحزازة هبرية في الرأس وتجمع على حزاز (ayn)؛ الحزاز الهبرية في الرأس الواحدة حزازة (sihah)؛ الحزاز هبرية في الرأس الواحدة حزازة كأنها نخالة (tahdhib)
- **B004** sert, engebeli ve uzanıp giden arazi — sert, engebeli, uzanan veya çakıllı yer · sert ve uzanan arazi parçaları · sert ve uzanan yerler · iki engebeli yer arasında uzanan çukur arazi
  الحزيز وهو مكان غليظ منقاد والجمع أحزة (maqayis)؛ الحزيز المكان الغليظ المنقاد والجمع حزان وأحزة (sihah)؛ الحزيز ما غلظ وصلب من جلد الأرض مع إشراف قليل (tahdhib)؛ لا يكون الحزيز إلا في أرض كثيرة الحصباء (tahdhib)
- **B005** an, zaman ve içinde bulunulan durum — yadırgatıcı bir durum veya saat · an veya zaman · saat veya geliş zamanı
  جئت على حزة منكرة أي حال وساعة (maqayis)؛ حزه حزة منكرة وليس هذا موضعه (jamhara)؛ الحز الحين والوقت (sihah)؛ الحزة الساعة أي حزة أتيتني (tahdhib)؛ الحز الوقت والحين (tahdhib)
- **B006** pantolonun bel kuşağı ve boyundan yakalama benzetmesi [kalıp] — pantolonun belden bağlanan bölümü · birini boynundan yakalamak
  حزة السراويل حجزته (sihah)؛ آخذ بحزته يريد بعنقه وهو على التشبيه (sihah)؛ أخذ بحزته يقال أخذ بعنقه وهو من السراويل حزة وحجزة (tahdhib)
- **B007** onurca üstün gelmek [kalıp] — birinin onurunu ve saygınlığını aşmak
  الحز الزيادة على الشرف؛ ليس في القبيل أحد يحز على كرم فلان أي يزيد عليه (tahdhib)
- **B008** sürmede, savaşta ve işte sert ve güçlü adam — sürmede, savaşta ve işte sert ve güçlü adam
  الحزاز من الرجال الشديد على السوق والقتال (tahdhib)؛ الحزاز من الرجال الشديد على السوق والقتال والعمل (tahdhib)
- **B009** enine boyuna araştırma — enine boyuna araştırma
  المحازة الاستقصاء (tahdhib)
- **B010** karşılıklı güvensizliğe dayalı ortaklık [kalıp] — tarafların birbirine güvenmediği ortaklık
  بينهما شركة حزاز إذا كان كل واحد منهما لا يثق بصاحبه (tahdhib)
- **B011** savaş sıralarını öne ve geriye alarak düzenleme — savaş sıralarında bazılarını öne, bazılarını geriye alma · işleri karışık ve dalgalı durumda olmak
  الحزحزة من فعل الرئيس في الحرب عند تعبئة الصفوف؛ يقدم هذا ويؤخر هذا؛ هم في حزاحز من أمرهم (tahdhib)
- **B012** kendi işi başından aşkın olmak — kendi işi başından aşkın olduğu için başka şeyle ilgilenememek
  حزت حازة من كوعها يضرب عند اشتغال القوم؛ الحازة قد شغلها ما هي فيه عن غيره (tahdhib)

## ء م ن (root_000054): 43:69 ءَامَنُوا۟, 43:88 يُؤْمِنُونَ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## س ل م (root_000737): 43:69 مُسْلِمِينَ, 43:89 سَلَٰمٌ

- **B001** kusur ve zarardan uzak esenlik — hastalık, kusur ve zarardan uzak olma · hastalık ve zararlı etkilerden kurtulmak · iç kötülükten arınmış yürek · seni koruyana andolsun anlamındaki yemin kalıbı
  السلامة أن يسلم الإنسان من العاهة والأذى (maqayis)؛ السلام يكون بمعنى السلامة (ayn)؛ السلام البراءة من العيوب وقلب سليم أي سالم (sihah)؛ السلامة والعافية (tahdhib)؛ السلم والسلامة التعري من الآفات الظاهرة والباطنة (mufradat)
- **B002** ilahi ad, esenlik selamı ve esenlik yurdu — Tanrı'nın kusur ve yok oluştan uzaklığını bildiren adı · esenlik sizinle olsun · sonsuz esenlik yurdu, cennet · kutsal taşa elle dokunma ya da onu öpme
  الله جل ثناؤه هو السلام وداره الجنة (maqayis)؛ السلام عليكم أي السلامة من الله عليكم وقيل اسم من أسماء الله (ayn)؛ السلام اسم من أسماء الله تعالى (sihah)؛ السلام دعاء للإنسان بأن يسلم من الآفات واسم الله (tahdhib)
- **B003** buyruğa boyun eğip onu kabul etme — Tanrı'nın buyruğuna boyun eğip itaati kabul etme · boyun eğmek · boyun eğip itaate girme
  الإسلام وهو الانقياد لأنه يسلم من الإباء والامتناع (maqayis)؛ الإسلام الاستسلام لأمر الله تعالى وهو الانقياد لطاعته والقبول لأمره (ayn)؛ السلم الاستسلام وأسلم أي دخل في السلم (sihah)؛ الإسلام إظهار الخضوع والقبول (tahdhib)
- **B004** barış ve karşılıklı uzlaşma — barış, uzlaşma ve savaşsızlık · karşılıklı barışma ve çatışmayı bırakma
  السلام المسالمة (maqayis)؛ السلم ضد الحرب (ayn)؛ السلم الصلح والتسالم التصالح والمسالمة المصالحة (sihah)؛ السلم والسلم الصلح (tahdhib)
- **B005** bedeli peşin ödenen vadeli satış — bedeli peşin ödenen vadeli satış · yiyeceğin bedelini önceden ödemek
  السلم الذي يسمى السلف كأنه مال أسلم (maqayis)؛ السلم ما أسلفت به (ayn)؛ السلم بالتحريك السلف وأسلم الرجل في الطعام أي أسلف فيه (sihah)؛ السلم السلف يقال أسلم في كذا وأسلف فيه (tahdhib)
- **B006** merdiven ve amaca ulaştıran araç — merdiven veya bir hedefe ulaştıran araç
  السلم أي السبب والمرقاة والجميع السلاليم (ayn)؛ السلم واحد السلاليم التي يرتقى عليها (sihah)؛ السلم الذي يرتقى عليه والسبب إلى الشيء (tahdhib)
- **B007** sert taşlar ve tekil sert taş — sert taşlar topluluğu · tek bir sert taş · kutsal taşa elle dokunma ya da onu öpme
  الحجارة سميت سلاما لأنها أبعد شيء من الفناء لشدتها (maqayis)؛ السلام الحجارة (ayn)؛ السلمة واحدة السلام وهي الحجارة (sihah)؛ السلام بكسر السين الحجارة الصلبة والواحدة سلمة (tahdhib)
- **B008** deri tabaklamada kullanılan dikenli ağaç — deri tabaklamada kullanılan dikenli ağaç · bir ağaç adı · ağacın yaprak ya da kabuğuyla deriyi tabaklamak
  السلامة شجر والسلم شجر والسلامان شجر (maqayis)؛ السلم ضرب من الشجر وورقه القرظ يدبغ به (ayn)؛ السلم شجر من العضاه والواحدة سلمة وسلمت الجلد إذا دبغته بالسلم (sihah)؛ السلام شجر والسلمة شجرة ذات شوك يدبغ بورقها وقشرها (tahdhib)
- **B009** iyileşme dileğiyle adlandırılan yılan ısırığı mağduru — iyileşme dileğiyle adlandırılan yılan ısırığı mağduru · yılan tarafından ısırılmış kişi · tartışmalı bir aktarımda yılan ısırması
  السليم وهو اللديغ قيل أسلم لما به وقيل تفاءلوا بالسلامة (maqayis)؛ السلم لدغ الحية والملدوغ مسلوم وسليم (ayn)؛ السلام والسليم اللديغ تفاءلوا له بالسلامة ويقال أسلم لما به (sihah)؛ الملدوغ مسلوم وسليم ثم قلت وما قاله غيره في السلم اللدغ (tahdhib)
- **B010** parmak, ayak veya deve tırnağındaki küçük kemik — parmak, ayak veya deve tırnağındaki küçük kemik
  السلامى عظام الأصابع والأشاجع والأكارع (ayn)؛ السلاميات عظام الأصابع والسلامى في الأصل عظم يكون في فرسن البعير (sihah)؛ السلامى عظم يكون في فرسن البعير وعظام القدم كلها سلاميات (tahdhib)
- **B011** tek kulplu kova — tek kulplu uzun kova
  السلم الدلو التي لها عروة واحدة (maqayis)؛ السلم دلو مستطيل له عروة واحدة (ayn)؛ السلم الدلو لها عروة واحدة نحو دلو السقائين (sihah)؛ السلم الدلو التي لها عروة واحدة (tahdhib)
- **B012** bir şeyi başkasına verme veya yüzüstü bırakma [kalıp] — bir şeyi ona verip almasını sağlamak · onu yüzüstü bırakmak veya başkasının eline vermek
  سلمت إليه الشيء فتسلمه أي أخذه وأسلمه أي خذله (sihah)؛ أسلم أمره إلى الله أي سلم (sihah)؛ أسلمت عنها أي تركتها وكل شيء تركته فقد أسلمت عنه (tahdhib)
- **B013** birini tutsak almak [kalıp] — birini tutsak almak
  أخذه سلما أي أسره (ayn)

## د خ ل (root_000464): 43:70 ٱدْخُلُوا۟

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

## ج ن ن (root_000266): 43:70 ٱلْجَنَّةَ, 43:72 ٱلْجَنَّةُ

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

## ح ب ر (root_000287): 43:70 تُحْبَرُونَ

- **B001** kalıcı iz — bir şeyden kalan iz · yara iyileşip iz bırakmak
  الحبار الأثر؛ الحبر والحبار أثر الشيء؛ حبر الرجل إذا كان بجلده قروح فبرئت وبقيت لها آثار؛ وحبر الجرح أيضا حبرا أي برأ وبقيت له آثار؛ الحبر الأثر المستحسن
- **B002** güzellik ve güzelleştirme — güzellik, parlaklık ve hoş görünüş · güzelliği ve dış görünüşü · güzelleştirmek; özellikle yazıyı, şiiri veya sözü özenli kılmak · süslenmiş veya güzelleştirilmiş · yeni, güzel veya özenle işlenmiş giysi · işlemeli bir üstlük kumaşı türü · yontusu özenle yapılmış çubuk
  الحبر الجمال والبهاء؛ الحبر والسبر الجمال والبهاء؛ ذهب حبره وسبره أي بهاؤه وحسنه؛ حبرته حبرا إذا حسنته؛ تحبير الخط والشعر تحسينه؛ التحبير حسن الخط والمنطق؛ ثوب حبير محسن
- **B003** yazı mürekkebi — yazı mürekkebi · mürekkep kabı veya hokka
  الذي يكتب به حبر؛ الحبر المداد؛ الحبر الذي يكتب به؛ محبرة للآنية التي يجعل فيها الحبر
- **B004** din bilgini — din bilgini; özellikle Yahudi din bilgini · din bilginleri; özellikle Yahudi din bilginleri
  الحبر العالم وجمعه أحبار؛ الحبر والحبر العالم من علماء أهل الدين وجمعه أحبار؛ الحبر والحبر واحد أحبار اليهود؛ حبر وحبر للعالم؛ الحبر العالم وجمعه أحبار
- **B005** nimet, ikram ve sevinç — sevinç, ferahlık ve nimet · nimetlendirilmek, ağırlanmak ve sevindirilmek · nimet içinde veya sevinçli · bu olay beni sevindirdi · nimet ve rahatlık içinde yaşayan erkek
  الحبرة الفرح؛ الحبرة النعمة ويحبرون أي ينعمون؛ الحبور السرور وكذلك الحبرة؛ يحبرون أي ينعمون ويكرمون ويسرون؛ الحبرة النعمة التامة والحبر السرور؛ يحبرون أي يفرحون حتى يظهر عليهم حبار نعيمهم
- **B006** dişteki sarı tabaka — dişleri kaplayan sarı tabaka veya diş taşı · dişleri kalın biçimde sararmak veya diş taşı bağlamak
  الحبر صفرة تعلو الأسنان؛ الحبر صفرة تقع على الأسنان؛ حبرت أسنانه إذا اصفرت صفرة غليظة؛ الحبرة القلح في الأسنان؛ الحبر صفرة تركب الإنسان وهي الحبرة أيضا
- **B007** çabuk bitki veren toprak ve su yüklü bulut [kalıp] — bitkiyi veya otu çabuk çıkaran toprak · çok su taşıyan, su bolluğundan benekli görünen bulut
  أرض محبار سريعة النبات؛ المحبار الأرض السريعة الكلأ؛ الحبير من السحاب الكثير الماء؛ الحبير من السحاب ما يرى فيه التنمير من كثرة الماء؛ الحبير من السحاب
- **B008** belirli bir kuş türü — bilinen bir kuş türü · bu kuş adının çoğul biçimi · bir kuş türü; bir görüşe göre söz konusu kuşun erkeği · söz konusu kuşun yavruları
  الحبارى طائر؛ الحبارى معروفة واليحبور ضرب من الطير؛ الحبارى ذكرها الحرب وتجمع حباريات
- **B009** olumsuzlukta en küçük bir şey — olumsuz cümlede en küçük bir şey · olumsuzlukta bir şey bile · başında tek tel saç bile
  ما فيه حبربر أي شيء؛ ما على رأسه حبر برة أي شعرة؛ ما أصاب منه حبرا برا أي ما أصاب منه شيئا؛ ما أغنى فلان عني حبربرا أي شيئا؛ ما على رأسه حبربرة أي ما على رأسه شعرة
- **B010** çölde bilinen bir yer — çölde bilinen bir yer adı
  حبر موضع؛ اسم البلد حبر مشددة الراء؛ حبر موضع معروف في البادية

## ط و ف (root_000957): 43:71 يُطَافُ

- **B001** bir şeyin çevresinde dolaşma — bir şeyin çevresinde dolaşmak · yapının çevresinde dönmek · çevresinde dolaşma · tekrar tekrar çevresinde dolaşmak · bir şeyin çevresini dolaşmak · bir konuyu her yönüyle kuşatıp incelemek · çokça dolaşmak · çok dolaşan adam · sürekli dolaşan hizmetçiler · bir şeyin çevresinde yürüme
  طاف به وبالبيت يطوف طوفا وطوافا واطاف به واستطاف (maqayis)؛ طاف بالبيت يطوف فالمصدر طواف (ayn)؛ طاف حول الشئ يطوف طوفا وطوفانا وتطوف واستطاف (sihah)؛ الطوف المشي حول الشيء؛ الطوافون عبارة عن الخدم (mufradat)
- **B002** her yanı kaplayan baskın su veya olay — her yanı kaplayan baskın su, yağmur veya olay
  لما يدور بالأشياء ويغشيها من الماء طوفان (maqayis)؛ الطوفان الماء الذي يغشى كل مكان ويشبه به الظلام (ayn)؛ الطوفان المطر الغالب والماء الغالب يغشى كل شئ (sihah)؛ الطوفان كل حادثة تحيط بالإنسان (mufradat)
- **B003** kişiye gelip yaklaşan varlık, görüntü veya olay — kişiye gelip dokunan görünmeyen varlık, görüntü veya olay · zihinde beliren görüntü · ona gelip yaklaşmak
  الطيف والطائف ما أطاف بالإنسان من الجنان؛ في الخيال طاف وأطاف (maqayis)؛ أطاف به أي ألم به وقاربه (sihah)؛ استعير الطائف من الجن والخيال والحادثة؛ طيف خيال الشيء وصورته (mufradat)
- **B004** topluluk veya bütünden ayrılan parça — bir veya daha çok kişiden oluşabilen topluluk · bir şeyden veya kumaştan ayrılan parça
  الطائفة من الناس فكأنها جماعة تطيف بالواحد أو بالشيء؛ طائفة من الثوب أي قطعة منه (maqayis)؛ طائفة من الناس والليل أي قطعة (ayn)؛ الطائفة من الشئ قطعة منه (sihah)؛ الطائفة من الناس جماعة منهم ومن الشيء القطعة منه (mufradat)
- **B005** gece dolaşan koruma görevlisi — geceleri dolaşarak koruma yapan görevli
  الطائف وهو العاس (maqayis)؛ الطائف العاس بالليل (ayn)؛ الطائف العسس (sihah)؛ الطائف لمن يدور حول البيوت حافظا (mufradat)
- **B006** bağlı tulum veya ağaçtan yapılan yük ve geçiş salı — bağlı tulumlardan veya ağaçtan yapılan yük ve geçiş salı
  الطوف قرب ينفخ فيها ثم يشد بعضها إلى بعض كهيئة سطح فوق الماء يحمل عليها الميرة ويعبر عليها (ayn)؛ الطوف قرب ينفخ فيها ثم يشد بعضها إلى بعض فتجعل كهيئة السطح يركب عليها في الماء ويحمل عليها وهو الرمث وربما كان من خشب (sihah)
- **B007** örtmeceli dışkı adı ve dışkılamaya gitme — örtmeceli olarak dışkı · dışkılamaya gitmek
  الطوف الغائط؛ طاف يطوف طوفا واطاف اطيافا إذا ذهب إلى البراز ليتغوط (sihah)؛ الطوف كني به عن العذرة (mufradat)
- **B008** yayın uç ile göbek arasındaki göbeğe bitişik kesimi [kalıp] — yayın dış ucu ile göbeği arasındaki göbeğe bitişik kesim
  طائف القوس فهو ما يلي أبهرها (maqayis)؛ طائف القوس ما بين السية والابهر (sihah)؛ طائف القوس ما يلي أبهرها (mufradat)
- **B009** boynunun çevresinden yakalamak [kalıp] — boynunun çevresinden yakalamak · boynunun çevresinden yakalamak
  أخذه بطوف رقبته وبطاف رقبته مثل صوف رقبته (sihah)
- **B010** yerleşimi kuşatan sağlam duvar ve bundan türeyen yer adı — yerleşimi kuşatan sağlam duvar ve bu duvardan adını alan yerleşim
  الطائف الذي بالغور سمي به الحائط الذي بنوا حولها في الجاهلية حصنوها به (ayn)؛ طائف بلاد ثقيف (sihah)

## ص ح ف (root_000845): 43:71 بِصِحَافٍ

- **B001** yayılmış geniş yüzey — yayılmış geniş yüzey · yeryüzünün görünen yüzü · yüz derisi
  أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)
- **B002** yazı yaprağı veya kitap — yazı yazılan yaprak veya kitap · yazı yaprakları · yazı yaprakları · yazı yaprakları için seyrek bir çoğul biçim
  الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)
- **B003** iki kapak arasında toplanmış yazı yaprakları — iki kapak arasında toplanmış yazı yaprakları bütünü · yazı yapraklarını iki kapak arasında toplamak
  سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)
- **B004** yayvan çanak; küçük su biriktirme çukuru — geniş ve yayvan çanak · geniş ve yayvan çanaklar · su için yapılmış küçük biriktirme çukurları
  الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)
- **B005** harf benzerliğinden doğan yanlış okuma veya aktarım — benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım · benzer harfleri karıştırıp metni yanlış aktaran kişi
  الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)

## ك و ب (root_001328): 43:71 وَأَكْوَابٍ

- **B001** kulpsuz içme kabı — kulpu ya da kulağı olmayan içme kabı · kulpu ya da kulağı olmayan içme kapları
  الكوب القدح لا عروة له (maqayis;mufradat)؛ الكوب كوز لا عروة له (ayn;sihah)؛ الكوب الإبريق بلا عروة (jamhara)؛ الكوب الكوز المستدير الرأس الذي لا أذن له (tahdhib)
- **B002** davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı — davul veya küçük, ortası dar davul · uzun saplı telli çalgı · deri parçasına birleştirilip üflenerek çalınan borular
  الكوبة الطبل للعب (maqayis)؛ الكوبة الطبل الذي يلعب به (mufradat)؛ الكوبة الطبل (jamhara)؛ الطبل والطنبور (jamhara)؛ الكوبة الطبل الصغير المخصر (sihah)؛ الكوبة قصبات تجمع في قطعة أديم ويزمر فيها (ayn)
- **B003** satranç — satranç
  الكوبة الشطرنجة (ayn)
- **B004** üst üste getirip yapıştırmak — parçalarını birbirinin üzerine getirip yapıştırmak
  بعضها كُوب على بعض أي ألزق (ayn)
- **B005** kulpsuz içme kabından içmek — kulpsuz içme kabından içmek
  كاب يكوب إذا شرب بالكوب (tahdhib)
- **B006** ince boyunluluk ve iri başlılık — boynun inceliği ve başın büyüklüğü
  الكَوَب دقة العنق وعظم الرأس (tahdhib)

## ش ه و (root_000825): 43:71 تَشْتَهِيهِ

- **B001** istenene yönelme; istek, istenen şey veya isteme gücü — kişinin istediği şeye içten yönelmesi ve onu istemesi · istenen şey · isteme gücü · karşılanmadığında bedenin zarar göreceği gerçek gereksinime dayalı istek · karşılanmadığında bedene zarar vermeyecek yersiz istek · istekler ve istenen şeyler · istemek ve bir şeye içten yönelmek · bir şeyi istemek · istemek · istenir, beğenilir ve hoş · isteği çok güçlü olan erkek · isteği çok güçlü olan kadın · istekle ilgili veya isteği çok güçlü · yemeye karşı çok güçlü istek duyanlar
  الشهوة ورجل شهوان وشيء شهي (maqayis)؛ رجل شهوان وامرأة شهوى وأنا إليه شهوان وشهي يشهى وشها يشهو إذا اشتهى (ayn;tahdhib)؛ الشهوة معروفة وطعام شهي أي مشتهى وشهيت الشيء إذا اشتهيته وهذا شيء يشهى الطعام أي يحمل على اشتهائه (sihah)؛ أصل الشهوة نزوع النفس إلى ما تريده وقد يسمى المشتهى شهوة والقوة التي تشتهي الشيء شهوة (mufradat)
- **B002** art arda istek bildirme; eşten isteme veya eş için sağlama — bir isteğin ardından başka bir istek ileri sürme · kadının istediği şeyi kocasından istemesi · kadının istediği şeyi onun için arayıp sağlamak
  التشهي شهوة بعد شهوة وتشهت المرأة على زوجها فأشهاها أي أطلبها ما تشهت أي طلب لها (ayn)؛ التشهي اقتراح شهوة بعد شهوة وتشهت المرأة على زوجها فأشهاها أي أطلبها شهواتها (tahdhib)
- **B003** içte saklanıp sürdürülerek gizlice yapılan kötü iş isteği [kalıp] — içte saklanıp sürdürülen ve gizlice yapılan kötü işlere yönelik istek
  الشهوة الخفية ليس بمخصوص بشيء واحد ولكنه في كل شيء من المعاصي يضمره صاحبه ويصر عليه (tahdhib)؛ الشهوة الخفية من الفواحش ما لا يحل مما يستخفي به الإنسان (tahdhib)؛ الشهوة الخفية للمعاصي والشهوة لها في قلبه مخفاة وإذا استخفى بها عملها (tahdhib)

## ن ف س (root_001533): 43:71 ٱلْأَنفُسُ

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

## ل ذ ذ (root_001352): 43:71 وَتَلَذُّ

- **B001** hoş tat ve tadını çıkarma — hoş tat ve bundan alınan olumlu duygu · hoş tat ve hoş bulma · sohbeti hoş adam · hoş olmak veya hoş tat vermek · yiyecek ve içeceği hoş bulmak · onu hoş bulmak veya hoş saymak · tadı hoş olanlar · tadı hoş yemek · tadı hoş yemek · hoş tatlar ve bunlardan alınan duygular · onu hoş buldum ve ondan tat aldım · ondan tat aldım · ondan tat aldım · tadı hoş içecek · tadı hoş içecek · tadı hoş · bolluk ve yeterlik içinde yiyip içmeden alınan pay
  طيب طعم الشيء واللذة واللذاذة طيب طعم الشيء ورجل لذ حسن الحديث (maqayis); لذ الطعام وغيره إذا كان لذيذا واستلذه استلذاذا وطعام لذ ولذيذ (jamhara); لذذت الشيء أي وجدته لذيذا والتذذت به وتلذذت به واستلذه عده لذيذا وشراب لذ ولذيذ (sihah); اللذة واللذاذة واللذيد واللذوى كله الأكل والشرب بنعمة وكفاية ولذ الشيء يلذ إذا كان لذيذا ولذت أحاديث الغوي أي استلذ بها (tahdhib)
- **B002** uyku — uyku
  واللذ النوم في قوله ولذ كطعم الصرخدي (maqayis); واللذ النوم في قول الشاعر ولذ كطعم الصرخدي طرحته (sihah); اللذ النوم وأنشد ولذ كطعم الصرخدي تركته (tahdhib)

## ع ي ن (root_001069): 43:71 ٱلْأَعْيُنُ

- **B001** gören göz — göz, görme organı
  العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)
- **B002** gözle görüp kesin biçimde tanıma — gözle görerek, yüz yüze · yüz yüze görerek · bilerek, görüp emin olarak · gördükten sonra ayrıca iz aramam
  رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)
- **B003** koruyup gözetme — korumam altında, özenle gözeterek · gözümün önünde, korumam altında · gözetimimiz ve korumamız altında
  أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)
- **B004** kötü bakışla zarar verme — gözüyle zarar verdi · gözü değen kimse · göz değmiş kimse · gözü sık değen kimse
  عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)
- **B005** haber toplayan gizli gözcü — gizli gözcü veya öncü · gizli gözcü · bizim için çevreyi yoklayıp haber getirdi
  العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)
- **B006** akan su kaynağı — akan su kaynağı · göz önünde akan su · su aktı veya kaynağı ortaya çıktı
  العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)
- **B007** su sızdıran ince delik — su kabındaki ince veya delik sızıntı yeri · incelip su tutamaz olmuş su kabı · dikiş delikleri kapansın diye kaba su döktü
  عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)
- **B008** güneş yuvarlağı — güneşin gövdesi veya yuvarlağı
  عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)
- **B009** göze benzer çukur, yer veya eğim — dizin önündeki çukur · kuyunun kaynak yeri veya çukuru · terazideki küçük eğim veya dengesizlik · yayda merminin yerleştiği bölüm
  عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)
- **B010** belirli yönden gelen bulut veya dinmeyen yağmur — kıblenin sağından gelen bulut · günlerce dinmeyen yağmur
  العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)
- **B011** hemen elde bulunan para — elde hazır bulunan para · altın para, eldeki para
  العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)
- **B012** ertelenmiş ödemeli alımla para edinme — önceden verilen para veya para sağlamak için yapılan satış · malı ödemesi ertelenmiş olarak satın aldı
  العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)
- **B013** şeyin bizzat kendisi ve belirlenmiş olanı — şeyin bizzat kendisi · tam kendisi, yerine başkası değil · bir şeyi topluluk içinden belirleyip ayırma
  عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)
- **B014** bir şeyin en iyi ve seçkin bölümü — bir şeyin en iyi ve seçkin bölümü
  عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)
- **B015** önde gelen kişiler veya anne baba bir kardeşler — topluluğun önde gelen seçkin kişileri · anne baba bir kardeşler veya aynı kadının çocukları
  أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)
- **B016** geniş ve güzel gözlü olma — geniş ve güzel gözlü · gözlerinin güzelliğiyle adlandırılan yaban sığırı · geniş ve güzel gözlü kadınlar · göz benzeri küçük kare desenli kumaş
  توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)
- **B017** kimse veya orada bulunan insanlar — orada hiç kimse yok · ev halkı veya orada bulunanlar · bir topluluk içinde
  ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)

## خ ل د (root_000429): 43:71 خَٰلِدُونَ, 43:74 خَٰلِدُونَ

- **B001** kalıcı olma ve durumunu koruma — kalmak; varlığını sürdürmek · kalıcılık; bulunduğu durumda kalma · kalıcılık; kalıcı yaşam yurdu · sonsuz yaşam bahçesi · ölümden sonraki kalıcı yaşam yurdu · kalıcı kılmak; kalacağına hükmetmek · yaşlandığı halde saçına ak düşmeyen · ön kesici dişleri, yan kesici dişleri çıkana kadar düşmeyen hayvan · yıkıntılar yok olduktan sonra kalan ocak taşları ve kayalar
  أصل واحد يدل على الثبات والملازمة (maqayis)؛ الخلود البقاء فيها (ayn)؛ دوام البقاء (jamhara;sihah)؛ دار الخلود والخلد الآخرة والجنة (jamhara)؛ بقاؤه على الحالة التي هو عليها (mufradat)؛ مخلد إذا أبطأ عنه الشيب (maqayis;jamhara;sihah;mufradat)؛ خوالد للأثافي والحجارة لطول مكثها (ayn;sihah;mufradat)
- **B002** yönelip bağlanma, yapışma ya da ayrılmadan kalma [kalıp] — yere yapışmak veya ona bağlanmak · ona yönelmek ve ondan hoşnut olmak · o yerde kalmak · arkadaşının yanından ayrılmamak
  أخلد إلى الأرض إذا لصق بها (maqayis;jamhara)؛ أخلد إلى كذا أي ركن إليه ورضي به (ayn)؛ أخلدت إلى فلان أي ركنت إليه (sihah)؛ أخلد بالمكان أقام به وأخلد بصاحبه لزمه (sihah)؛ ركن إليها ظانا أنه يخلد فيها (mufradat)
- **B003** küpe; küpe veya bilezikle süslenmiş olma — küpe; bir tür kulak süsü
  ولدان مخلدون مقرطون (ayn;mufradat)؛ من الخلد والخلد جمع خلدة وهي القرط (maqayis)؛ مقرطون مشنفون (maqayis)؛ مسورون لغة يمانية (jamhara)
- **B004** akıl ve akla gelen düşünce — akıl; zihinde yer eden düşünce · aklıma geldi
  الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت (maqayis)؛ ما يقع ذلك في خلدي (ayn)؛ وقع ذلك في خلدي أي في قلبي (jamhara)؛ وقع ذلك في خلدي أي في ورعي وقلبي (sihah)
- **B005** gözsüz faremsi küçük hayvan — gözleri olmayan, fareye veya sıçana benzeyen küçük hayvan
  الخلد ضرب من الجرذان عمي لم يخلق لها عيون (ayn)؛ الخلد دويبة تشبه الفأرة (jamhara)؛ ضرب من الجرذان أعمى (sihah)

## و ر ث (root_001639): 43:72 أُورِثْتُمُوهَا

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

## ع م ل (root_001046): 43:72 تَعْمَلُونَ

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

## ف ك ه (root_001174): 43:73 فَٰكِهَةٌ

- **B001** neşeli hoşnutluk içinde olup elindekinin tadını çıkarma — neşeli, güler yüzlü ve şakacı · rahatlık içinde, elindekinden hoşnut · kendisine verilenlerden hoşnut ve memnun · neşeli ve şakacı olma hali · ondan tat alıp yararlandım · yiyeceği veya meyveyi tat alarak yemek · neşeli ve şakacı kimse · neşeli ve şakacı kadın
  الرجل الفكه الطيب النفس (maqayis)؛ فاكهين أي ناعمين معجبين بما هم فيه والفكه الطيب النفس (ayn)؛ فكه إذا كان طيب النفس مزاحا وفاكهين أي ناعمين وتفكهت بالشيء تمتعت به (sihah)؛ الفكه الطيب النفس الضحوك والفاكه أيضا الناعم والفكه المعجب (tahdhib)
- **B002** yenmesi hoş meyve — meyve; yenmesi hoş bulunan ürünler · topluluğa meyve yedirmek veya sunmak · meyve satıcısı · yiyeceği veya meyveyi tat alarak yemek
  الفاكهة لأنها تستطاب وتستطرف (maqayis)؛ كل الثمار فاكهة وفكهت القوم بالفاكهة تفكيها (ayn)؛ الفاكهة معروفة وأجناسها الفواكه والفاكهاني الذي يبيعها (sihah)؛ كل الثمار فاكهة ولم يخرجهما من الفاكهة (tahdhib)؛ الفاكهة قيل هي الثمار كلها وقيل ما عدا العنب والرمان (mufradat)
- **B003** tatlı sözlerle şakalaşma — neşeli ve şakacı olma hali · şaka ve yakın kimselerin sıcak söyleşisi · tatlı sözlerle karşılıklı şakalaşma · toplulukla tatlı sözlerle şakalaşmak · şakacı kimse
  المفاكهة وهي المزاحة وما يستحلى من كلام (maqayis)؛ فاكهتهم مفاكهة بملح الكلام والمزاح والفكاهة المزاح والفاكه المازح (ayn)؛ الفكاهة المزاح والمفاكهة الممازحة (sihah)؛ فاكهت مازحت والفاكه ههنا المازح (tahdhib)؛ الفكاهة حديث ذوي الأنس (mufradat)
- **B004** doğumdan önce sütün gelmesi veya koyulaşması — devenin doğumdan önce sütünün gelmesi veya koyulaşması · doğumu yaklaşmış ve sütü belirginleşmiş deve · doğumdan önce sütü akmaya başlayan deve
  أفكهت الناقة والشاة إذا درتا عند أكل الربيع وكان في اللبن أدنى خثورة وهو أطيب اللبن (maqayis)؛ أفكهت الناقة إذا رأيت في لبنها خثورة قبل أن تضع فهي مفكه (ayn)؛ أفكهت الناقة إذا درت عند أكل الربيع قبل أن تضع فهي مفكهة (sihah)؛ المفكه من النوق التي يهراق لبنها عند النتاج قبل أن تضع وقد أفكهت وناقة مفكهة ومفكه (tahdhib)
- **B005** özel adlandırma kümesi — 
  فليس من هذا وهو من باب الإبدال والأصل تفكنون وهو من التندم (maqayis)؛ تفكهنا من كذا أي تعجبنا ويقال تفكهون تندمون (ayn)؛ تفكه تعجب ويقال تندم (sihah)؛ تتعجبون مما نزل بكم ويقال معنى فظلتم تندمون وكذلك تفكنون (tahdhib)؛ تفكهون قيل تتعاطون الفكاهة وقيل تتناولون الفاكهة (mufradat)
- **B006** şımarık ve küstah taşkınlık — şımarık, küstah ve ölçüsüz
  وما كان لأهل النار فكهين أي أشرين بطرين (ayn)؛ والفكه أيضا الأشر البطر وقرئ فكهين أي أشرين (sihah)؛ الفكه الأشر وما كان من وصف أهل النار فكهين يعني أشرين بطرين (tahdhib)
- **B007** birini arkasından kötüleyip çekiştirme [kalıp] — insanların saygınlığına dil uzatıp onları çekiştirmek · birini arkasından kötüleyip çekiştirmek
  يتفكه بالطعام أو بالفاكهة أو بأعراض الناس؛ تركت القوم يتفكهون بفلان أي يغتابونه ويتناولون منه؛ الفكه الذي ينال من أعراض الناس (tahdhib)

## ك ث ر (root_001286): 43:73 كَثِيرَةٌ, 43:78 أَكْثَرَكُمْ

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

## ء ك ل (root_000043): 43:73 تَأْكُلُونَ

- **B001** yeme, yiyecek ve yeme rolleri — yemek yemek · yiyecek · bir öğünlük yeme veya tek lokma · çok yiyen, obur · birlikte yemek yiyen kişi · başkasını doyuran kişi · yenilen şey, yiyecek · yenmek üzere hazırlanmış yiyecek
  الأكل معروف؛ أكلت الطعام أكلا ومأكلا؛ الأكل تناول المطعم؛ الأكلة المرة واللقمة؛ رجل أكول كثير الأكل؛ أكيلك الذي يؤاكلك؛ المؤكل المطعم
- **B002** ağaç ve ekin ürünü — ağacın meyvesi veya verimi
  أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر؛ أكل بستانك دائم وأكله ثمره؛ والأكل لما يؤكل قال تعالى أكلها دائم
- **B003** verilen pay ve geçimlik — dünya payı ve geniş geçimliği olan · yöneticilerin verdiği tahsisatlar · kişiye ayrılmış, hesabı sorulmayan pay
  الأكل حظ الرجل وما يعطاه من الدنيا؛ المأكلة ما جعل للإنسان لا يحاسب عليه؛ فلان ذو أكل إذا كان ذا حظ من الدنيا ورزق واسع؛ الأكل الطعمة؛ يعبر به عن النصيب
- **B004** malı harcama veya ele geçirme [kalıp] — malı harcamak veya tüketerek elden çıkarmak · insanların mallarını alıp onları sömürmek
  يستأكل قوما أي يأكل أموالهم؛ فلان يستأكل الضعفاء أي يأخذ أموالهم؛ يعبر بالأكل عن إنفاق المال؛ أكل المال بالباطل صرفه إلى ما ينافيه الحق
- **B005** ateşin tüketmesi, beslenmesi ve harlanması — ateş odunu yakıp tüketti · ateşi odunla besledi · ateş iyice harlandı · öfkesinden alevlendi · kılıç keskinliğinden parladı
  أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ الرجل إذا اشتد غضبه يأتكل؛ تأكل السيف أي توهج من الحدة؛ وعلى طريق التشبيه قيل أكلت النار الحطب
- **B006** aşınma, bozulma ve kaşıntı — beden veya baş kaşıntısı · dişlerde aşınma veya çürüme · deride işlenince ortaya çıkan ince kusurlu yer · gebe deve, yavrusunun çıkan tüyünden kaşınıp rahatsız oldu · aşınıp bozulmak
  الأكال الحكاك؛ الأكل في الأديم مكان رقيق؛ بأسنانه أكل؛ والأكال أن يتأكل عود أو شيء؛ في جسدي إكلة من الأكال؛ تأكل كذا فسد؛ أصابه إكال في رأسه وفي أسنانه
- **B007** av olmuş veya yenmek için ayrılmış hayvan — yırtıcının yiyip bıraktığı av · kurdun yediği koyun veya başka av · yenmek için ayrılıp beslenen koyun · ürünü yenmek üzere ayrılmış hurma ağaçları
  أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته؛ الأكولة من الشاء التي ترعى للأكل لا للنسل والبيع؛ الأكولة الشاة التي تعزل للأكل وتسمن؛ أكيلة السبع؛ الأكولة من الغنم ما يؤكل
- **B008** arkadan çekiştirip saygınlığı zedeleme [kalıp] — birinin saygınlığını arkadan çekiştirerek zedelemek · insanları sürekli arkalarından çekiştiren
  فلان ذو أكلة في الناس إذا كان يغتابهم؛ ذو أكلة وإكلة إذا كان يغتاب الناس؛ تأكل لحومنا وتغتابنا؛ أكل فلان فلانا اغتابه وكذا أكل لحمه
- **B009** söz taşıyarak arayı bozma [kalıp] — aralarında söz taşıyıp onları birbirine düşürmek · ara bozucu söz taşıyıcı
  آكلت بين القوم أفسدت؛ المؤكل النمام؛ الإيكال بين الناس السعي بينهم بالنمائم؛ آكلت بين القوم أي حرشت وأفسدت
- **B010** biçime bağlı adlandırmalar [kalıp] — bana yapmadığım veya almadığım şeyi yükledin · onu senin erişimine bıraktım
  أكلتني ما لم آكل أي ادعيته علي؛ آكلتني أيضا أي ادعيته علي؛ آكلتك فلانا إذا أمكنته منه؛ أليس قبيحا أن تؤكلني ما لم آكل
- **B011** bir başla doyacak kadar az topluluk [kalıp] — tek bir hayvan başının doyuracağı kadar az topluluk
  ما هم إلا أكلة رأس؛ هم أكلة رأس أي هم قليل يشبعهم رأس واحد؛ عبارة عن ناس من قلتهم يشبعهم رأس
- **B012** biçime bağlı adlandırmalar [kalıp] — ipliği çok, sık dokulu ve güçlü kumaş · akıl ve sağlam görüş sahibi kişi
  ثوب ذو أكل أي كثير الغزل؛ رجل ذو أكل ذو رأي وعقل؛ ثوب ذو أكل إذا كان كثير الغزل صفيقا؛ رجل ذو أكل إذا كان ذا عقل ورأي؛ ثوب ذو أكل كثير الغزل كذلك
- **B013** yemek yenilen kap veya yer — içinde yemek yenilen çanak veya tencere · kendisinden yemek yenilen yer
  المئكل إناء يؤكل فيه؛ المئكلة قصعة تشبع الرجلين والثلاثة؛ المأكلة والمأكلة الموضع الذي منه يؤكل؛ المئكلة ضرب من البرام وضرب من الأقداح وكل ما أكل فيه
- **B014** ete işleyen kesici veya vurucu araç [kalıp] — et kesen bıçak; ayrıca sivri sopa veya kamçı
  للسكين آكلة اللحم؛ آكلة اللحم عصا محددة؛ الأصل في هذا أنها السكين؛ قيل في آكلة اللحم إنها السياط

## ج ر م (root_000239): 43:74 ٱلْمُجْرِمِينَ

- **B001** kesip ayırma — kesme, kesip ayırma · hurma ürününü ağaçtan kesip toplamak · hurma kesim zamanı veya kesim işi · koyunun yününü kırkmak · ondan keserek almak · hurma ürününü kesip toplayan topluluk · yerden kesilmiş bir parça gibi yükselip yerleşen köklü oluşum
  فالجرم القطع؛ لصرام النخل الجرام؛ جرمت صوف الشاة وأخذته (maqayis)؛ الجرم القطع وقد جرم النخل واجترمه أي صرمه وجرمت صوف الشاة أي جززته (sihah)؛ جرمه يجرمه جرما إذا قطعه؛ جرم النخل وجزمه إذا خرصه وجززه (tahdhib)؛ أصل الجرم قطع الثمرة عن الشجر (mufradat)؛ جرثومة من كلمتين من جرم وجثم كأنه اقتطع من الأرض قطعة فجثم فيها (maqayis-routing)
- **B002** hurma hasadı artığı ve çekirdeği — kesimden sonra düşen veya toplanan hurma artığı · hurma çekirdeği veya kuru hurma · bir müd tutarında yiyecek · hurma salkımının çıktığı çekirdek
  الجرامة ما سقط من التمر إذا جرم؛ الجرام والجريم التمر اليابس (maqayis)؛ الجرامة ما سقط من التمر إذا جرم؛ الجريم النوى وهما أيضا التمر اليابس (sihah)؛ الجرامة ما التقط من التمر بعدما يصرم؛ الجريم النوى وقيل البؤرة التي يرضخ فيها النوى؛ الجرام والجريم هما النوى وهما أيضا التمر اليابس؛ المد يدعى بالحجاز جريما (tahdhib)
- **B003** kazanıp edinme ve bir sonuca sürükleme — kazanmak, elde etmek · ailesinin geçimini kazanan kişi · sizi buna sürüklemesin veya size bunu kazandırmasın · topluluğa öfke kazandırdı veya onu öfkeye sürükledi
  جرم أي كسب لأن الذي يحوزه فكأنه اقتطعه؛ فلان جريمة أهله أي كاسبهم؛ جرمت فزارة أي كسبتهم غضبا (maqayis)؛ جرم يجرم أي كسب؛ فلان جريمة أهله أي كاسبهم؛ ولا يجرمنكم أي لا يحملنكم ويقال لا يكسبنكم (sihah)؛ خرج يجرم قومه أي يكسبهم؛ لا يحملنكم ولا يكسبنكم؛ أجرمني كذا وجرمني وجرمت وأجرمت بمعنى واحد (tahdhib)
- **B004** suç veya günah işleme — suç, günah veya haksız fiil · suç veya günah · suç veya günah işlemek · suçlu veya günahkar kişi · suç işleyen veya haksızlık yapan kişi · birine işlemediği bir suçu yüklemek
  فلان له جريمة أي جرم وهو مصدر الجارم الذي يجرم على نفسه وقومه شرا؛ الجرم الذنب وفعله الإجرام والمجرم المذنب والجارم الجاني (ayn)؛ الجرم الذنب والجريمة مثله؛ جرم وأجرم واجترم بمعنى (sihah)؛ الجرم مصدر الجارم؛ الجارم الجاني والمجرم والمذنب؛ لا يدخلنكم في الجرم؛ الجرم التعدي والجرم الذنب (tahdhib)؛ الجرم والجريمة الذنب وهو من الأول لأنه كسب (maqayis)
- **B005** kuşkusuz ve kaçınılmaz olarak — kuşkusuz, mutlaka veya kaçınılmazdır · kesinlik bildiren kalıplaşmış söyleyiş
  لا جرم يجري مجرى لا بد ويفسر حقا (ayn)؛ لاجرم كانت في الأصل بمنزلة لا بد ولا محالة ثم صارت بمنزلة حقا؛ لا جرم لآتينك (sihah)؛ لا جرم بمنزلة لا بد ولا محالة؛ صارت بمنزلة حقا؛ لا ذا جرم ولا جر (tahdhib)؛ لا جرم هو من قولهم جرمت أي كسبت (maqayis)
- **B006** bir zaman döneminin tamamlanıp sona ermesi — tamamlanıp sona ermiş bir yıl · eksiksiz tamamlanmış bir yıl · bu yılı tamamlayıp geride bıraktık · yıl geçti ve sona erdi
  أقمت عنده حولا مجرما أي حولا تاما حتى انقضى؛ جرمنا هذه السنة أي خرجنا منها وتجرمت السنة والشتاء والصيف (ayn)؛ حول مجرم وسنة محرمة أي تامة؛ تجرمت السنون أي انقضت؛ تجرم الليل ذهب (sihah)؛ سنة مجرمة وشهر مجرم ويوم مجرم وهو التام؛ جرمنا هذه السنة أي خرجنا منها؛ تجرمت السنة؛ كله من الجرم وهو القطع (tahdhib)؛ سنة مجرمة أي تامة كأنها تصرمت عن تمام؛ تجرم الليل ذهب (maqayis)
- **B007** beden, gövde ve bedensel büyüklük — beden, gövde veya cismani yapı · gövdeli veya cüsseli erkek ve kadın · iri gövdeli develer
  الجرم ألواح الجسد وجثمانه؛ رجل جريم وامرأة جريمة أي ذات جرم أي جسم (ayn)؛ الجرم بالكسر الجسد؛ جلة جريم أي عظام الأجرام (sihah)؛ الجرم الجسد؛ الجرم البدن؛ جرم إذا عظم جرمه؛ ألواح الجسد وجثمانه (tahdhib)؛ الجسد جرم لأن له قدرا وتقطيعا؛ مشيخة جلة جريم أي عظام الأجرام (maqayis)
- **B008** sesin gürlüğü ve bedenden iyi çıkışı [kalıp] — sesin gürlüğü veya bedenden iyi çıkışı · ses ya da boğaz berraklığı denmiş, ancak yanlış sayılmış kullanım
  جرم الصوت جهارته؛ ما عرفته إلا بجرم صوته (ayn)؛ الجرم الصوت؛ فلان صافي الجرم أي الصوت أو الحلق وهو خطأ (sihah)؛ الجرم الصوت؛ جرم الصوت جهارته؛ ما عرفته إلا بجرم صوته (tahdhib)؛ قال قوم الصوت يقال له الجرم وأصح من ذلك حسن خروج الصوت من الجرم (maqayis)
- **B009** renk ve rengin durulaşması — rengi saflaştı veya duruldu · renk
  الجرم اللون (sihah)؛ الجرم اللون؛ جرم لونه إذا صفا؛ الجرم اللون والصوت والبدن (tahdhib)
- **B010** sıcaklık ve sıcak bölge — soğuk yerin karşıtı olan sıcak toprak · sıcaklık
  أرض جرم وأرض صرد دخيلان مستعملان في الحر والبرد (ayn)؛ الجرم الحر فارسي معرب؛ الجروم من البلاد خلاف الصرود (sihah)؛ الجرم نقيض الصرد؛ أرض جرم وأرض صرد دخيلان مستعملان في الحر والبرد (tahdhib)
- **B011** Arap kabilesi ve topluluk adı — bir Arap kabilesi veya kabile kolunun adı · bir Arap topluluğunun adı
  جرم قبيلة من اليمن (ayn;tahdhib)؛ جرم بطنان من العرب أحدهما في قضاعة والآخر في طيئ؛ بنو جارم قوم من العرب (sihah)؛ بنو جارم في العرب؛ جرم سميت به وهما بطنان أحدهما في قضاعة والآخر في طي (maqayis)

## ف ت ر (root_001125): 43:75 يُفَتَّرُ

- **B001** şiddetini yitirerek zayıflama, yumuşama ve durulma — zayıflamak; sertliği ya da şiddeti azalıp durulmak · bir şeyi zayıflatmak ya da şiddetini gidermek · bir şeyi zayıflatmak veya ılık duruma getirmek · şiddetten sonra durulma, sertlikten sonra yumuşama ve güçten sonra zayıflama · bedende ya da iç dünyada kırılma ve güçsüzlük · keskin olmayan, durgun bakış · göz kapakları zayıflayıp bakışı kırılmak · içilince bedeni gevşeten şey · sıcak ile soğuk arasında, ılık su · sıcağın şiddeti kırılıp azalmak · yağmur suyunu boşaltıp kesilmek ve duraksamak · taşkınlıktan sonra benim izlediğim yola yönelip durulmak
  أصل صحيح يدل على ضعف في الشيء (maqayis)؛ الفترة الانكسار والضعف (sihah)؛ الفتور سكون بعد حدة ولين بعد شدة وضعف بعد قوة (mufradat)؛ فتر فلان إذا سكن عن حدته ولان بعد شدته (tahdhib)؛ فتر الإنسان إذا لانت مفاصله وضعفت (jamhara)؛ لا يفتر أي لا يضعف (maqayis)؛ لا يسكنون عن نشاطهم (mufradat)؛ المفتر الذي يفتر الجسد (tahdhib)؛ ماء فاتر بين الحار والبارد (tahdhib)؛ فتر مطر فرغ ماءه وكف وتحير (tahdhib)
- **B002** iki elçinin gelişi arasındaki dönem — iki elçinin gelişi arasındaki, yeni bir elçinin gelmediği dönem
  الفترة ما بين كل نبيين (jamhara)؛ الفترة ما بين الرسولين من رسل الله عزوجل (sihah)؛ على فترة من الرسل أي سكون حال عن مجيء رسول الله (mufradat)
- **B003** başparmak ile işaret parmağı arasındaki açıklık ve bununla ölçme — başparmak ile işaret parmağı açıldığında uçları arasında kalan açıklık · bir şeyi başparmak ile işaret parmağı arasındaki açıklığı kullanarak ölçmek
  الفتر ما بين طرف الإبهام وطرف السبابة إذا فتحتهما (maqayis)؛ الفتر ما بين طرفي السبابة وطرف الإبهام إذا فتحتهما (jamhara)؛ الفتر ما بين طرف السبابة والابهام إذا فتحتهما (sihah)؛ الفتر قدر ما بين طرف الإبهام وطرف المسبحة وقد فترت الشيء إذا قدرته بفترك (tahdhib)؛ الفتر ما بين طرف الإبهام وطرف السبابة يقال فترته بفتري (mufradat)

## ب ل س (root_000149): 43:75 مُبْلِسُونَ

- **B001** umudu tümüyle kesme — umudunu kesmek, ümitsizliğe düşmek · umudu kesme, ümitsizliğe düşme · umudunu kesmiş kimse · merhametten umudunu kestiği için bu adın verildiği söylenen varlık
  أبلس من الخير أي أويس (ayn)؛ أبلس الرجل إبلاسا فهو مبلس إذا يئس (jamhara)؛ أبلس من رحمة الله أي يئس (sihah)؛ الإبلاس معناه في اللغة القنوط وقطع الرجاء من رحمة الله (tahdhib)؛ فالأصل اليأس يقال أبلس إذا يئس (maqayis)
- **B002** kederden çökkün ve donuk olma — kederli, çökkün, pişman ve bahtsız kimse · şiddetli sıkıntıdan doğan kırgınlık ve keder · donuk ve somurtkan kimse · yüzünü asıp buruşturmak
  المبلس الكئيب الحزين المتندم؛ المبلس البائس (ayn)؛ الإبلاس أيضا الانكسار والحزن (sihah)؛ الإبلاس الحزن المعترض من شدة البأس (mufradat)؛ البلس الواجم (maqayis)؛ بلسم الرجل كره وجهه فالميم فيه زائدة وإنما هو من المبلس وهو الكئيب الحزين المتندم (maqayis)
- **B003** kederden ya da cevapsızlıktan susup kalma [kalıp] — kederden ya da söyleyecek cevabı kalmadığı için susup kalmak
  أبلس فلان إذا سكت غما (sihah)؛ الذي يسكت عند انقطاع حجته ولا يكون عنده جواب قد أبلس (tahdhib)؛ أبلس الرجل إذا انقطع فلم تكن له حجة (tahdhib)؛ أبلس فلان إذا سكت وإذا انقطعت حجته (mufradat)؛ ومن هذا الباب أبلس الرجل سكت (maqayis)
- **B004** çiftleşme isteğinin şiddetinden böğürmeme — dişi devenin çiftleşme isteğinin şiddetinden böğürmemesi · çiftleşme isteğinin şiddetinden böğürmeyen dişi deve
  أبلست الناقة إذا لم ترغ من شدة الضبعة فهي مبلاس (sihah)؛ أبلست الناقة فهي مبلاس إذا لم ترع من شدة الضبعة (mufradat)؛ ومنه أبلست الناقة وهي مبلاس إذا لم ترغ من شدة الضبعة (maqayis)؛ ومن ذلك الناقة (maqayis)
- **B005** kaba çul ve ondan yapılmış büyük çuval — kaba çul · kaba çullar; bu malzemeden yapılmış büyük çuvallar · kaba çul satıcısı · Tanrı seni büyük çuvalların üzerinde teşhir etsin
  البلس جمع بلاس وهو فارسي معرب وهي المسوح (jamhara)؛ أهل المدينة يسمون المسح بلاسا وهو فارسي معرب (sihah)؛ البلس بالضم غرائر كبار من مسوح يجعل فيها التين ويشهر عليها من ينكل به (sihah)؛ المسح تسميه البلاس وجمعه بلس؛ يقال لبائعه البلاس (tahdhib)؛ البلاس للمسح ففارسي معرب (mufradat)
- **B006** olgun incir ya da incire benzer meyve — olgun incir meyvesi veya incire benzer meyve · bu meyvenin bir tanesi
  البلس بالتحريك شيء يشبه التين يكثر باليمن (sihah)؛ البلس ثمر التين إذا أدرك الواحدة بلسة (tahdhib)؛ البلس هو التين إن كانت الرواية بفتح الباء واللام (tahdhib)
- **B007** mercimek veya mercimeğe benzer tane — mercimek · mercimek veya mercimeğe benzer tane
  البلسن حب شبه العدس أو العدس بعينه يمكن أن تكون النون فيه زائدة (jamhara)؛ البلس بضم الباء واللام العدس (tahdhib)؛ البلسن وهو العدس (tahdhib)
- **B008** tohumu ilaçta kullanılan yağlı tohumlu ağaç — tohumu ilaçta kullanılan ve değerli yağ veren ağaç
  البلسان شجر حبه يجعل في الدواء ولحبه دهن يتنافس فيه (ayn)؛ بلسان أراه روميا (tahdhib)
- **B009** hiçbir şey yememiş olma — hiçbir şey yemedim
  ما ذقت علوسا ولا بلوسا أي ما أكلت شيئا (tahdhib)

## ق ض ي (root_001237): 43:77 لِيَقْضِ

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

## م ك ث (root_001437): 43:77 مَّٰكِثُونَ

- **B001** bekleyerek durup kalma — bekleme, oyalanma ve bir yerde kalma · durdu, bekledi veya bir yerde kaldı · bekleyen ya da bir yerde kalan kimse · oyalandı; bir işi bekledi veya üzerinde durdu · bekleyip kalma · bir yerde kalan kimse
  كلمة تدل على توقف وانتظار (maqayis)؛ المكث الانتظار والماكث المنتظر (ayn)؛ المكث المقام وربما جعل المكث في معنى الانتظار (jamhara)؛ المكث: اللبث والانتظار وتمكث: تلبث (sihah)؛ الماكث: المنتظر وتمكث إذا انتظر أمرا أو أقام عليه (tahdhib)؛ المكث: ثبات مع انتظار (mufradat)
- **B002** acele etmeyen ağırbaşlılık — ağırbaşlı, acele etmeyen · ağırbaşlılık ve acele etmeme · adam yavaş ve ağırdan alarak yürüdü · ağırbaşlı ve acele etmeyen kimseler
  رجل مكيث رزين غير عجول (maqayis)؛ مكث مكاثة فهو مكيث أي رزين لا يعجل (ayn)؛ سار الرجل متمكثا أي متلوما ورجل مكيث أي رزين (sihah)؛ رجل مكيث الرزين الذي لا يعجل في أمره والماكث المنتظر وإن لم يكن مكيثا في الرزانة (tahdhib)

## ك ر ه (root_001295): 43:78 كَٰرِهُونَ

- **B001** hoşlanmama ve istememe — bir şeyden hoşlanmamak ve onu istememek · hoşnutsuzluk; istenmeyen şey · hoşnutsuzluk ve tiksinme · hoşnutsuzluk ve tiksinme · hoşnutsuzluk ve kaçınma · sevimsiz, ağır gelen · istenmeyen, hoş görülmeyen · bir şeyi birine sevimsiz göstermek · hoşa gitmeyen, ağır gelen iş
  خلاف الرضا والمحبة (maqayis)؛ كرهت الشيء أكرهه كرها والكراهية (maqayis)؛ الكره المكروه وأمر كريه مستكره مكروه وكرهته كراهة وكراهية ومكرهة (ayn)؛ كرهت الشئ أكرهه كراهة وكراهية فهو شئ كريه ومكروه وكرهت إليه الشئ تكريها نقيض حببته إليه (sihah)؛ يقال كرهت الشيء كرها وكرها وكراهة وكراهية والكره المكروه وكره إلي هذا الأمر تكريها (tahdhib)؛ ما يعاف من حيث الطبع وما يعاف من حيث العقل أو الشرع (mufradat)
- **B002** isteksizce katlanılan güçlük — güçlük; isteksizce yapılan iş · güçlük içinde ve gönülsüzce · bir şeyi istemeye istemeye yapmak · bir işi gönülsüzce yapmak · bundan hoşnut olmayarak · bundan hoşnut olmayarak
  الكره المشقة والكره أن تكلف الشيء فتعمله كارها (maqayis)؛ فعلته على كره وفعلته كرها (ayn)؛ الكره بالضم المشقة قمت على كره أي على مشقة (sihah)؛ كراهتهم القتال أنهم كرهوه على جنس غلظه عليهم ومشقته (tahdhib)؛ الكره المشقة التي تنال الإنسان من خارج والكره ما يناله من ذاته وهو يعافه (mufradat)
- **B003** istemediği bir şeye zorlama — birini istemediği bir işe zorlamak · bir insanı istemediği şeye zorlama · zor kullanılarak cinsel saldırıya uğratılmış kadın
  امرأة مستكرهة غصبت نفسها فأكرهت على ذلك وأكرهته حملته على أمر وهو كاره (ayn)؛ أكرهته على كذا حملته عليه كرها (sihah)؛ امرأة مستكرهة إذا غصبت نفسها وأكرهت فلانا حملته على أمر هو له كاره (tahdhib)؛ الإكراه يقال في حمل الإنسان على ما يكرهه (mufradat)
- **B004** savaşın ağır şiddeti — savaşın ağır şiddeti · zamanın felaketleri ve ağır olayları · darbede işleyen keskin kılıç
  الكريهة الشدة في الحرب والسيف الماضي في الضرائب ذو الكريهة (maqayis)؛ الكريهة الشدة في الحرب وكذلك الكرائه وهي نوازل الدهر (ayn)؛ الكريهة الشدة في الحرب وذو الكريهة السيف الماضي في الضريبة (sihah)؛ الكريهة الشدة في الحرب وكذلك كرايه الدهر نوازل الدهر وذو الكريهة وهو الذي يمضي في الضرائب (tahdhib)
- **B005** inatçı ve zor mizaçlı [kalıp] — başı sert, yönlendirilmeye direnen deve · zor mizaçlı, hoşnutsuz ve içine kapanık adam
  الكره الجمل الشديد الرأس كأنه يكره الانقياد (maqayis)؛ رجل كره متكره وجمل كره شديد الرأس (ayn)؛ الكره الجمل الشديد الرأس (sihah)؛ رجل كره متكره وجمل كره شديد الرأس (tahdhib)
- **B006** çukurun üst bölümü — çukurun üst bölümü
  الكرهاء أعلى النقرة بلغة هذيل (ayn)؛ الكرهاء هي أعلى النقرة بلغة هذيل (tahdhib)
- **B007** sert ve kaba arazi — sert ve kaba yapılı arazi
  يقال للأرض الصلبة الغليظة مثل القف وما قاربه كرهة (tahdhib)

## ب ر م (root_000110): 43:79 أَبْرَمُوٓا۟, 43:79 مُبْرِمُونَ

- **B001** sağlam büküm ve kesin karara bağlama — işi kesin karara bağlamak · sağlamlaştırma ve kesinleştirme · ipi sağlamca bükmek · çift kat bükülmüş iplik veya kumaş · iki telin birlikte büküldüğü ip veya iplik
  أبرمت الأمر أحكمته؛ أبرمت الحبل إذا فتلته متينا (maqayis)؛ الإبرام إحكام الشيء (ayn)؛ الإبرام خلاف النقض (jamhara)؛ المبرم والبريم الحبل الذي جمع بين مفتولين (sihah)؛ البريم خيط يفتل على طاقين (tahdhib)؛ أصله من إبرام الحبل (mufradat)
- **B002** bıkıp usanma ve bezdirme — bir şeyden bıkıp usanmak · onu bezdirip usandırmak · bıkkınlık ve usanma · çekilmez, ısrarcı veya tatsız konuşan kimse · kötü huylu topluluk
  برمت بالأمر عييت به؛ برمت بكذا أي ضجرت به برما (maqayis)؛ برمت بكذا أي ضجرت منه؛ أبرمني فلان إبراما (ayn)؛ الذي يتبرم بالناس؛ تبرمت بالشيء تبرما إذا استثقلته (jamhara)؛ برم به إذا سئمه؛ أبرمه أي أمله وأضجره (sihah)؛ لا تبرمني بكثرة فضولك؛ المبرم الثقيل (tahdhib)؛ المبرم الذي يلح ويشدد في الأمر (mufradat)
- **B003** paylı şans oyununa katılmayan cimri — topluluğun paylı şans oyununa katılmayan kimse · paylı şans oyununa katılmayan kimseler · oyuna ortak olmayıp hurmayı da ikişer yiyen kimse
  البرم الذي لا يياسر القوم ولا يدخل معهم في الميسر (ayn)؛ الذي لا يأخذ في الميسر (jamhara)؛ الذي لا يدخل مع القوم في الميسر (sihah;tahdhib)؛ قيل للبخيل الذي لا يدخل في الميسر برم؛ من يأكل تمرتين تمرتين برم (mufradat)
- **B004** iki renkli veya iki türden oluşan karışım — iki renkli veya iki türden oluşan karışım · Arap ve Arap olmayan savaşçılardan oluşan iki ordu · koyun ve keçilerden oluşan karma sürü · gece karanlığıyla karışık ilk sabah aydınlığı · birlikte sarılan karaciğer ve hörgüç yağı · boncuk dizilmiş, bele veya kola bağlanan ip
  البريمين النوعان من كل ذي خلطين؛ الدمع مع الإثمد بريم؛ الصبح أول ما يبدو بريما؛ لفيفهم من كل لون (maqayis)؛ البريم كل ذي لونين (ayn)؛ كل لونين اجتمعا فهو بريم؛ قطيع بريم (jamhara)؛ الحبل المفتول يكون فيه لونان؛ الجيش بريم؛ بريميها أي من الكبد والسنام (sihah)؛ كل ذي لونين بريم؛ البريمان الجيشان عرب وعجم؛ ضوء الشمس مع بقية سواد الليل؛ القطيع من الغنم من ضأن ومعزى؛ ثوب فيه قز وكتان (tahdhib)؛ سمي كل ذي لونين به من جيش مختلط أسود وأبيض ولغنم مختلط (mufradat)
- **B005** dikenli ağaç meyvesi veya çiçeği — dikenli ağaçların meyvesi · dikenli bir ağacın beyaz veya sarı çiçeği ya da meyvesi · ağaç ilk meyvesini verdi · karınca başı büyüklüğündeki çok küçük üzüm taneleri · dikenli ağaç meyvesini toplayan kişi
  البرم وأطيبها ريحا برم السلم؛ برمة العرفط؛ أبرم الطلح؛ البرمة الزهرة التي تخرج فيها الحبلة؛ البرم حبوب العنب (maqayis)؛ البرم ثمر الأراك وشبهه من الأشجار (ayn)؛ البرم ثمر العلف (jamhara)؛ البرم ثمر العضاه؛ برمة السلم أطيب البرم ريحا (sihah)؛ المبرم الذي يجني البرم وهو ثمر الأراك (tahdhib)
- **B006** taş tencere — taş tencere · taş tencereler · az veya çok sayıdaki taş tencereler · taş tencere yapan ve yontan usta
  البرمة وهي القدر (maqayis)؛ البرام جمع البرمة وهو قدر من حجر (ayn)؛ البرمة والجمع برم وبرم وبرام قدور من حجارة (jamhara)؛ البرام جمع برمة وهي القدر (sihah)؛ البرم قدور من حجارة؛ المبرم الذي يسوي البرام وينحتها ويقطعها (tahdhib)؛ البرمة في الأصل هي القدر المبرمة وجمعها برام (mufradat)
- **B007** iri, sıkıca yapışan kene — iri veya sıkıca yapışmış kene · keneden daha sıkı yapışan
  البرام وهو القراد الكبير؛ هو ألزق من برام (maqayis)؛ البرام القراد؛ لصوق البرام (jamhara)؛ البرام بالضم القراد (sihah)
- **B008** küçük dağ veya kum tepeleri — küçük dağ dorukları veya kum tepeleri
  البرم قنان صغار من الجبال الواحدة برمة يعني جبال الرمل (ayn)

## ء م ر (root_000051): 43:79 أَمْرًا

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

## ن ج و (root_001476): 43:80 وَنَجْوَىٰهُم

- **B001** ayrilarak kurtulma — serden ayrilip kurtulmak · baskasini kurtarmak · kurtulus sebebi
  ينجو من شيء بذهاب عنه (maqayis)؛ نجا فلان من الشر ينجو نجاة (ayn)؛ نجوت من كذا نجاء ونجاة وأنجيت غيري ونجيته (sihah)؛ نجا الرجل من الشر ينجو نجوا أو نجاة (tahdhib)؛ أصل النجاء الانفصال من الشيء ومنه نجا فلان من فلان وأنجيته ونجيته (mufradat)
- **B002** hizla gitme — hizlanip one gecmek · hizli deve · yolda acele etmek
  نجا الإنسان ينجو نجاة ونجاء في السرعة؛ ناقة ناجية ونجاة سريعة (maqayis)؛ نجا ينجو في السرعة نجاء فهو ناج وناقة ناجية سريعة (ayn)؛ نجوت أيضا نجاء أي أسرعت وسبقت (sihah)؛ النجاء النجاء؛ استنجوا معناه أسرعوا السير (tahdhib)
- **B003** soyup ayirma — deriyi kaziyip yuzmek · dali agactan kesip almak · ince cubugu agactan kesmek · agaci kokunden kesmek · soyulmus dal veya cubuklar · teli cekip ayirmak
  نجوت الجلد أنجوه والجلد نجا إذا كشطته؛ يستنجي من شجرها العصي؛ أنجني عصا (maqayis)؛ نجوت العود إذا اقتضبته من الشجرة؛ نجوت الجلد عن الناقة إذا كشطته (jamhara)؛ نجوت جلد البعير عنه وأنجيته إذا سلخته؛ النجاة الغصن (sihah)؛ أنجيت قضيبا من الشجرة؛ نجوت الوتر واستنجيته إذا خلصته (tahdhib)؛ نجوت قشر الشجرة وجلد الشاة؛ النجا عيدان قد قشرت (mufradat)
- **B004** sel basmaz yuksek yer — sel basmaz yuksek yer · selden korunmus yuksek arazi · arazide genis aciklik · arazisini su basmasin diye yukseltmek
  النجاة والنجوة من الأرض وهي التي لا يعلوها سيل؛ بيني وبينهم نجاوة من الأرض أي سعة (maqayis)؛ النجاة النجوة من الأرض أي الارتفاع لا يعلوه الماء (ayn)؛ النجوة الربوة من الأرض (jamhara)؛ النجوة والنجاة المكان المرتفع الذي تظن أنه نجاؤك لا يعلوه السيل (sihah)؛ كل سند مشرف لا يعلوه السيل فهو نجوة من الأرض (tahdhib)؛ النجوة والنجاة المكان المرتفع المنفصل بارتفاعه عما حوله (mufradat)
- **B005** gizli konusma — gizli konusma veya sir · biriyle gizlice konusmak · kendi aralarinda sirlasmak · birini sir icin ayirmak · gizli konusma arkadasi
  النجو والنجوى السر بين اثنين وناجيته وتناجوا وانتجوا (maqayis)؛ النجو كلام بين اثنين كالسر والتسار (ayn)؛ النجوى الكلام المسر؛ نجوت الرجل إذا أقعدته نجيا لتناجيه (jamhara)؛ النجو السر بين اثنين؛ ناجيته؛ تناجوا؛ انتجيته (sihah)؛ النجوى في الكلام ما يتفرد به الجماعة والاثنان (tahdhib)؛ ناجيته أي ساررته؛ انتجيت فلانا استخلصته لسري (mufradat)
- **B006** bedensel cikinti ve temizlenme — tuvalet sonrasi temizlenmek · bedenden cikan diski veya gaz · bedenden cikinti cikarmak · ilacin bagirsaklari bosaltmasi
  استنجى إذا أراد قضاء حاجته أتى نجوة من الأرض تستره (maqayis)؛ الاستنجاء التنظف بمدر أو ماء؛ النجو ما خرج من البطن من ريح وغيرها؛ النجو استطلاق البطن (ayn)؛ النجو كناية عن ذي البطن؛ احتبس نجوه في بطنه؛ استنجى (jamhara)؛ النجو ما يخرج من البطن؛ استنجى أي مسح موضع النجو أو غسله؛ شرب دواء فما أنجاه (sihah)؛ النجو العذرة نفسها؛ استنجيت بالماء الحجارة أي تطهرت بها؛ أنجى إذا عرق؛ أنجاني الدواء أي أقعدني (tahdhib)؛ كني عما يخرج من الإنسان بالنجو؛ الاستنجاء تحري إزالة النجو أو طلب نجوة لإلقاء الأذى (mufradat)
- **B007** bulut adi [kalıp] — durumu tartismali bulut adi · bulutun uzaklasmasi
  النجو السحاب والجمع النجاء وهو من انكشافه؛ أنجت السحابة ولت (maqayis)؛ نجو السحاب أول ما ينشأ والجميع النجاء (ayn)؛ النجو السحاب والجمع نجاء (jamhara)؛ النجو السحاب الذي هراق ماءه؛ أنجت السحابة إذا ولت (sihah)؛ النجو السحاب الذي هراق ماءه (tahdhib)
- **B008** agiz kokusunu sinama [kalıp] — birinin agiz kokusunu sinamak
  نجوت فلانا استنكهته (maqayis)؛ نجوته استنهكته (ayn)؛ نجوت فلانا إذا استنكهته (sihah)؛ نجوت فلانا إذا استنكهته (tahdhib)؛ فليس في البيت حجة له وإنما أراد أني ساررته (mufradat)
- **B009** gerinme — gerinme
  النجواء التمطي مثل المطواء

## و ل د (root_001683): 43:81 وَلَدٌ

- **B001** ana babadan doğan kişi veya kişiler — birinin çocuğu; bir veya birden çok doğmuş kişi · çocuklar · doğmuş çocuk; yeni doğan · kim olduğunu bilmiyorum · birbirlerinden çocuk sahibi olup çoğaldılar
  أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)
- **B002** öz ana baba — öz baba · öz ana · ana baba
  الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)
- **B003** çocuğu dünyaya getirme — kadın çocuğunu dünyaya getirdi · doğum; çocuğu dünyaya getirme · doğum zamanı geldi · gebe koyun · koyunun doğumunu üstlendik · birbirlerinden çocuk sahibi olup çoğaldılar
  ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)
- **B004** yeni doğmuş çocuk veya köle — yeni doğmuş erkek çocuk; erkek köle · kız çocuk; kadın köle
  الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)
- **B005** bir şeyden nedenle türeme veya sonradan oluşturulma — bir şeyin başka bir şeyden bir nedenle ortaya çıkması · sonradan oluşturulmuş, uydurulmuş veya katışıksız olmayan · katışıksız sayılmayan dil veya kişi
  تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)
- **B006** yaşıt — yaşıt; aynı yaşta olan kimse
  اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)
- **B007** çok büyük bir durum ya da pek bol bir şey [kalıp] — çok büyük veya ağır bir durum yahut çok bol bir şey için söylenen kalıp söz
  أمر لا ينادى وليده؛ قيل ذلك لكل أمر عظيم ولكل شيء كثير (sihah)؛ هو أمر لا ينادى وليده؛ أمر جليل شديد؛ أصله في الغارة؛ طعام لا ينادى وليده؛ عشب لا ينادى وليده (tahdhib)

## ع ر ش (root_001000): 43:82 ٱلْعَرْشِ

- **B001** hükümdar tahtı ve yönetim makamı — hükümdarın tahtı ve yönetim makamı · insanın gerçek niteliğini bilemediği, yalnız adını bildiği Tanrı tahtı
  العرش سرير الملك (maqayis;sihah)؛ العرش في كلام العرب سرير الملك (tahdhib)؛ سمي مجلس السلطان عرشا (mufradat)؛ عرش الله ما لا يعلمه البشر إلا بالاسم (mufradat)
- **B002** üstü örtülü barınak ve gölgelik — evin tavanı · altında gölgelenilen üstü örtülü yapı · çubuklardan yapılıp üstü gölgelenen evler · hayvanları soğuktan koruyan çevrili barınak
  كل بناء يستظل به عرش وعريش (maqayis)؛ العرش سقف البيت (sihah;tahdhib)؛ العرش والعريش ما يستظل به (sihah;tahdhib)؛ العرش في الأصل شيء مسقف (mufradat)؛ عروش مكة بيوتها (sihah;tahdhib)؛ الحظيرة التي تسوى للماشية تكنها من البرد عريش (tahdhib)
- **B003** asmaya çardak kurma ve asmanın çardağa tırmanması — asmaya çardak kurup onu desteğe almak · üzüm asmasının çardağın üzerine tırmanması · çardak üzerinde yetiştirilen asmalar
  تعريش الكرم لأنه رفعه والتوثق منه (maqayis)؛ عرشت الكرم بالعروش تعريشا (sihah;tahdhib)؛ عرشت الكرم إذا جعلت له كهيئة سقف (mufradat)؛ اعترش العنب إذا علا على العراش (sihah)؛ اعترش العنب العريش إذا علاه (tahdhib)
- **B004** kuyuyu ahşapla kaplama ve ağız platformu kurma — kuyunun ahşap kaplaması ve ağız üstü çalışma yeri · altı taşla, geri kalanı ahşapla örülmüş kuyu
  عرش البئر طيها بالخشب (maqayis;sihah)؛ العرش الذي يكون على فم البئر يقوم عليه الساقي (maqayis)؛ بئر معروشة وهي التي تطوى قدر قامة من أسفلها بالحجارة ثم يطوى سائرها بالخشب (tahdhib)؛ عرشت البئر جعلت له عريشا (mufradat)
- **B005** deve üzerindeki örtülü kadın taşıma bölmesi — kadının deve üzerinde oturduğu örtülü taşıma bölmesi
  العريش شبه الهودج يتخذ للمرأة تقعد فيه على بعيرها (maqayis;sihah;tahdhib)؛ العرش شبه هودج للمرأة شبيها في الهيئة بعرش الكرم (mufradat)
- **B006** işin, iktidarın ve saygınlığın dayanağı — kişinin işini ayakta tutan dayanak · işi çöktü, iktidarı ve saygınlığı sona erdi · iktidar, yönetme gücü ve saygınlık
  قيل لأمر الرجل وقوامه عرش وإذا زال ذلك عنه قيل ثل عرشه (maqayis)؛ ثل عرشه أي وهى أمره وذهب عزه (sihah)؛ العرش الملك يقال ثل عرشه أي زال ملكه وعزه (tahdhib)؛ كني به عن العز والسلطان والمملكة قيل فلان ثل عرشه (mufradat)
- **B007** boyun yanları, ayak üstü ve bunlara bağlı beden adları — boynun iki yanındaki uzun etli bölümler · ayağın parmaklarla orta çıkıntı arasındaki üst bölümü · boyun yanlarına komşulukla aynı ad verilen iki kulak · at yelesindeki kılların son bölümü · iki yanı iri ve geniş deve
  العرش عرش العنق عرشان بينهما الفقرا وفيهما الأخدعان (maqayis)؛ العرش في القدم ما بين العير والأصابع من ظهر القدم (maqayis)؛ العرش بالضم أحد عرشي العنق (sihah)؛ للعنق عرشان بينهما القفا وفيهما الأخدعان (tahdhib)؛ ظهر القدم العرش وباطنه الأخمص (tahdhib)؛ الأذنان تسميان عرشين لمجاورتهما العرشين (tahdhib)؛ العرشان من الفرس آخر شعر العرف (tahdhib)
- **B008** Simak'ın Arşı ve Süreyya'nın Arşı diye anılan iki özel yıldız grubu — Simak'ın Arşı adıyla Avva'nın altında bulunan ve Aslan'ın arka kısmı sayılan dört küçük yıldız · Süreyya'nın Arşı adıyla Süreyya yakınındaki yıldızlar
  عرش السماك أربعة كواكب أسفل من الغواء (maqayis)؛ عرش السماك أربعة كواكب صغار أسفل من العواء (sihah)؛ عرش الثريا كواكب قريب منها (tahdhib)
- **B009** sürüsüne yöneltilen eşeğin başını kaldırıp ağzını açması [kalıp] — eşeğin sürüsüne yönelince başını kaldırıp ağzını açması
  إذا حمل الحمار على العانة رافعا رأسه شاحيا فاه قيل عرش بعانته تعريشا (maqayis)؛ عرش الحمار بعانته تعريشا إذا حمل عليها ورفع رأسه وشحا فاه (sihah)؛ عرش الحمار بعانته تعريشا وذلك إذا حمل على عانته فرفع رأسه شاخسا فاه (tahdhib)
- **B010** koyunların otlamasını engelleme — koyunların otlamasını engelleme
  الإعراش أن تمنع الغنم أن ترتع وقد أعرشتها إذا منعتها أن ترتع (tahdhib)
- **B011** bineğin üzerine çıkıp binme [kalıp] — bineğin üzerine çıkıp binmek
  اعروشت الدابة واعترشته وتعروشته إذا ركبته (tahdhib)
- **B012** bir yerde sabit kalıp yerleşme [kalıp] — bir ülkede sabit kalıp yerleşmek
  تعرشنا ببلاد كذا أي ثبتنا وتعرش فلان بها (tahdhib)

## و ص ف (root_001654): 43:82 يَصِفُونَ

- **B001** bir şeyi nitelikleriyle betimleme ve onu belirleyen nitelik — bir şeyi ayırt edici nitelikleriyle betimlemek · bir şeyi tanıtan nitelik, durum veya kalıcı belirti · betimlenebilir duruma gelmek veya belirli nitelikler kazanmak · bir şeyi karşılıklı olarak betimlemek · dil bilgisinde niteleme ögesi
  أصل واحد هو تحلية الشيء (maqayis)؛ الوصف وصفك الشيء بحليته ونعته (ayn;tahdhib)؛ وصفت الشيء وصفا وصفة (sihah)؛ الوصف ذكر الشيء بحليته ونعته والصفة الحالة التي عليها الشيء (mufradat)؛ اتصف الشيء احتمل أن يوصف/صار متواصفا (maqayis;sihah;mufradat)؛ الصفة عندهم هي النعت (sihah)
- **B002** görmeden, nitelik tarifine göre satış [kalıp] — malı görmeden, tarif edilen niteliklerine göre satış · güvence altına alınmış nitelik tarifine göre görmeden satış
  كره المواصفة في البيع (ayn;tahdhib)؛ بيع المواصفة أن تبيع الشيء بصفة من غير رؤية (sihah)؛ إذا باع شيئا عنده على الصفة لزمه البيع/بيع الصفة المضمونة (tahdhib)
- **B003** hayvanın iyi ve beğenilir bir yürüyüş sergilemesi — devenin iyi ve beğenilir biçimde yürümesi · tayın iyi bir yürüyüş biçimine yönelmesi
  وصفت الناقة وصوفا إذا أجادت السير (maqayis)؛ للمهر إذا توجه لشيء من حسن السيرة قد وصف/وصف المشي (ayn;tahdhib)؛ وصفت يداها لها الإدلاج يريد أجادت السير (sihah)؛ وصف البعير وصوفا إذا أجاد السير (mufradat)
- **B004** hizmet çağına gelmiş genç hizmetçi — hizmet çağına gelmiş genç erkek veya kadın hizmetçi · hizmet çağına gelmiş genç kadın hizmetçi · oğlanın hizmet görebilecek çağa gelmesi · genç hizmetçinin boyca gelişimini tamamlaması veya hizmet çağına gelmesi · genç kadının hizmetçi sayılacak olgunluğa erişmesi
  الخادم وصيف وللخادمة وصيفة/أوصفت الجارية لأنهما يوصفان عند البيع (maqayis)؛ يقال للوصيف قد أوصف وأوصفت الجارية ووصيف ووصفاء ووصيفة ووصائف (ayn)؛ الوصيف الخادم غلاما كان أو جارية/وصف الغلام إذا بلغ حد الخدمة (sihah)؛ أوصف الوصيف إذا تم قده وأوصفت الجارية (tahdhib)؛ الوصيف الخادم والوصيفة الخادمة ويقال أوصفت الجارية (mufradat)
- **B005** doktordan hastalık için tedavi tarifi isteme — hastalığım için doktordan tedavi yolu tarif etmesini istemek
  استوصفت الطبيب لدائي إذا سألته أن يصف لك ما تتعالج به (sihah)

## و ذ ر (root_001638): 43:83 فَذَرْهُمْ

- **B001** et parçası; bir aktarımda etsiz kemik parçası — et parçası; bir aktarıma göre etsiz kemik parçası · et parçaları · bol et parçalı ekmek yemeği
  الوذرة وهي الفدرة من اللحم (maqayis)؛ الوذرة قطعة عظم لا لحم فيه (ayn)؛ الوذرة بالتسكين الفدرة وهي القطعة من اللحم (sihah)؛ الوذرة القطعة من اللحم مثل الفدرة (tahdhib)؛ الوذر بضع اللحم (tahdhib)؛ الوذرة قطعة من اللحم (mufradat)؛ ثريدة كثيرة الوذر (tahdhib)
- **B002** eti parçalama veya yarayı çizerek açma — eti parçalama veya yarayı çizerek açma · eti parçalara ayırmak · yarayı çizerek açmak · et parçasını küçük parçalara bölmek
  التوذير أن يشرط الجرح (maqayis)؛ وذرت اللحم توذيرا قطعته وكذلك الجرح إذا شرطته (sihah)؛ وقد وذرت الوذرة أذرها وذرا إذا بضعتها بضعا (tahdhib)
- **B003** bir şeyi bırakmak — bir şeyi bırakmak · önemsiz gördüğü şeyi bir yana atmak · bunu bırak · onu bırakmak
  ذر ذا (maqayis)؛ أماتت المصدر من يذر والفعل الماضي واستعملته في الحاضر والأمر (ayn)؛ ذره أي دعه وهو يذره (sihah)؛ ذرذا ودع ذا ولا يقال وذرته (tahdhib)؛ يذر الشيء أي يقذفه لقلة اعتداده به (mufradat)
- **B004** cinsel göndermeli ağır soy sövgüsü; ad biçiminde klitoris — cinsel organ göndermeli ağır bir soy sövgüsü · ağır bir soy sövgüsü · klitoris
  يا ابن شامة الوذر (maqayis;ayn;sihah;tahdhib)؛ كلمة قذف (sihah)؛ كلمة معناها القذف (tahdhib)؛ عرض لها بأعضاء الرجال (maqayis)؛ أراد المذاكير (tahdhib)؛ أرادوا بها القلف (tahdhib)؛ الوذفة والوذرة بظارة المرأة (tahdhib)

## خ و ض (root_000446): 43:83 يَخُوضُوا۟

- **B001** suya girip içinde ilerlemek — suya girip içinde ilerleme · suya girip içinde yürümek · suyun içinde yürümek · suyun içinde yoğun biçimde yürümek · hayvanını suya sokmak · topluluğun atlarının suya girmesi · suda yaya veya binek üzerinde geçilen yer · sudaki geçiş yerleri · sudaki geçiş yerleri · tehlikelere veya derinliklere atılmak · suya girip yürüme eylemi
  توسط شيء ودخول (maqayis)؛ خضت الماء خوضا وخياضا أي مشيت فيه (ayn)؛ خضت الماء أخوضه خوضا وكذلك كل شيء خضته (jamhara)؛ الموضع مخاضة؛ أخاض القوم أي خاضت خيلهم الماء؛ خضت الغمرات اقتحمتها (sihah)؛ الشروع في الماء والمرور فيه (mufradat)
- **B002** konuşmaya veya işe girip onun içinde yer almak — işe veya söze dalma, çoğunlukla kınanan konuşmaya girişme · topluluğun konuşup görüş alışverişinde bulunması · konuşma veya iş üzerinde karşılıklı görüşmek ve sözleri iç içe geçirmek · bir işe girmek veya o işte karışıklığa düşmek · konuşmada karşılıklı görüşme eylemi
  تخاوضوا في الحديث والأمر أي تفاوضوا وتداخل كلامهم (maqayis)؛ الخوض اللبس في الأمر؛ الخوض من الكلام ما فيه الكذب والباطل (ayn)؛ خاض القوم في الحديث وتخاوضوا فيه خوضا ومخاوضة إذا تفاوضوا (jamhara)؛ خاض القوم في الحديث وتخاوضوا أي تفاوضوا فيه (sihah)؛ يستعار في الأمور وأكثر ما ورد في القرآن فيما يذم الشروع فيه؛ تخاوضوا في الحديث تفاوضوا (mufradat)
- **B003** suyla çırparak karıştırmak — yiyecek veya içeceği karıştırmaya yarayan araç · kavrulmuş tahıl unundan yapılan yiyeceği suyla çırpıp karıştırmak · içeceği su katarak karıştırmak · kılıcını vurduğu bedenin içinde oynatmak · kanının içinde şiddetle hareket ettirilmek
  المخوض المجدح الذي تخوض به السويق (ayn)؛ خضت له السويق وما أشبهه من الشراب إذا أوخفته بالماء أي ضربته بالماء حتى يختلط؛ المخوض كل شيء حركت به السويق ونحوه حتى يختلط (jamhara)؛ المخوض للشراب كالمجدح للسويق؛ خضت الشراب؛ خاضه بالسيف أي حرك سيفه في المضروب؛ خوض في نجيعه (sihah)

## ل ع ب (root_001358): 43:83 وَيَلْعَبُوا۟

- **B001** oyun; ciddi bir amaç gütmeyen eğlenceli davranış — oynamak; ciddi bir amaç gütmeden şakalaşmak · tekrar tekrar oynamak · oyuna çok düşkün kimse · oyun veya oyun aracı · oyun türü ya da kişinin iyi yaptığı oyun tarzı · bir kez oynama · oyun yeri · çocuğun oynarken giydiği kolsuz giysi · oyunculuğu meslek edinmiş kimse · çok oyun oynayan genç kız · oyun veya oyun aracı · bir erkekle karşılıklı oynamak
  اللعب معروف (maqayis;sihah)؛ اللعب ضد الجد وكل هازل لاعب (jamhara)؛ فعل غير قاصد به مقصدا صحيحا (mufradat)؛ تلعب لعب مرة بعد أخرى ورجل تلعابة كثير اللعب (ayn;sihah;tahdhib)؛ اللعبة ما يلعب به وكل ملعوب به فهو لعبة (ayn;jamhara;sihah;tahdhib)؛ الملعب موضع اللعب (maqayis;ayn;sihah;tahdhib)؛ اللعاب من يكون حرفته اللعب (ayn;tahdhib)
- **B002** ağızdan akan salya — ağızdan akan salya · çocuğun salyası akmak · çocuğun salyası akmaya başlamak · salya bulunan ağız
  اللعاب ما يسيل من فم الصبي (maqayis)؛ لعاب الصبي ما سال من فيه (ayn)؛ اللعاب ما يسيل من فم الصبي من ريقه (jamhara)؛ اللعاب ما يسيل من الفم (sihah)؛ لعب الصبي إذا سال لعابه (jamhara;sihah;tahdhib;mufradat)؛ ألعب الصبي إذا صار له لعاب يسيل من فيه وثغر ملعوب أي ذو لعاب (sihah)
- **B003** arı balı ve yılan zehri için kalıplaşmış adlandırma [kalıp] — arı balı veya arının yaptığı bal · yılan zehri
  لعاب النحل العسل (maqayis;sihah)؛ لعاب النحل ما تعسله (tahdhib)؛ لعاب الحية سمها (jamhara;tahdhib)
- **B004** sıcakta görülen ipliksi hava titreşimi; serapla özdeşliği tartışmalı [kalıp] — sıcakta görülen ipliksi hava titreşimi; bazı kullanımlarda serap
  لعاب الشمس السراب (maqayis;ayn;sihah)؛ لعاب الشمس ما تراه كأنه ينحدر من السماء إذا حميت الشمس (jamhara)؛ لعاب الشمس هو شبه الخيط تراه في الهواء إذا اشتد الحر (tahdhib)؛ من قال إن لعاب الشمس السراب فقد أبطل (tahdhib)
- **B005** rüzgârın iz silmesi, geçiş yolları ve bilinmeyen yer [kalıp] — rüzgârın evi aşındırıp izlerini silmesi · rüzgârın geçiş yolları · nerede olduğu bilinmeyen yer
  لعبت الريح بالمنزل إذا درسته (jamhara)؛ ملاعب الريح مدارجها (jamhara)؛ تركته في ملاعب الجن أي حيث لا يدرى أين هو (jamhara)
- **B006** eski meyvesi dururken yeni çiçek salkımı vermek [kalıp] — hurma ağacının eski ürünü üzerindeyken yeni çiçek salkımı vermesi
  استلعبت النخلة إذا أطلعت طلعا وفيها بقية من حملها الأول (tahdhib)

## ب ر ك (root_000109): 43:85 وَتَبَارَكَ

- **B001** çöküp yerinde durma — deve çöktü ve yerinde kaldı · deveyi çöktürdü · çökmüş develer topluluğu · develerin çöktüğü yer · çökme veya yerleşip kalma
  أبركت الناقة فبركت؛ البرك الإبل البوارك (ayn)؛ برك البعير يبرك بروكا أي استناخ؛ كل شيء ثبت وأقام فقد برك؛ ما أحسن بركة هذه الناقة وهو اسم للبروك (sihah)؛ البرك الإبل البروك؛ أبركت الناقة فبركت بروكا؛ التبراك بفتح التاء البروك (tahdhib)؛ أصل البرك صدر البعير؛ وبرك البعير ألقى بركه (mufradat)؛ أصل واحد وهو ثبات الشيء؛ برك البعير يبرك بروكا؛ مبرك الإبل (maqayis)؛ تبراك فالتاء فيه زائدة وإنما هو تفعال من برك أي ثبت وأقام (maqayis-tabraak)
- **B002** göğüsle bastırma — devenin göğsü ve alt göğüs bölgesi · hayvanın yere değen karın ve göğüs derisi · göğsüyle sürttü veya ezdi · göğsünü yere veya bir şeyin üstüne bıraktı · onu yere serip altında bıraktı
  البرك كلكل البعير وصدره الذي يدوك به الشيء تحته؛ حكه ودكه ببركه (ayn)؛ البرك أيضا الصدر؛ بركة زور؛ ابترك الرجل أي ألقى بركه؛ ابتركته إذا صرعته وجعلته تحت بركك (sihah)؛ البركة ما ولي الأرض من جلد بطن البعير وما يليه من الصدر؛ البرك كلكل البعير وصدره؛ حكه ودكه وداكه ببركه ودلكه (tahdhib)؛ أصل البرك صدر البعير (mufradat)؛ البرك أيضا كلكل البعير وصدره؛ البركة ما ولى الأرض من جلد البطن وما يليه من الصدر من كل دابة (maqayis)
- **B003** su tutan havuzcuk — suyun durduğu havuz veya su tutma çukuru
  البركة أيضا كالحوض والجمع البرك؛ سميت بذلك لإقامة الماء فيها (sihah)؛ البركة شبه حوض يحفر في الأرض؛ الصهاريج التي سويت بالآجر وصرجت بالنورة بركا (tahdhib)؛ سمي محبس الماء بركة (mufradat)؛ البركة شبه حوض يحفر في الأرض؛ البركة المصنعة وجمعها برك (maqayis)
- **B004** kalıcı hayır artışı — hayırda artış ve kalıcı iyilik · hayır ve artış dileme · Tanrının ona hayır ve artış vermesini dilemek · kendinde veya kendisinden çok hayır bulunan · ondan iyi sonuç ve hayır umdu · hayrı bol yiyecek
  البركة النماء والزيادة؛ التبريك الدعاء بالبركة؛ بارك الله لك وفيك وعليك؛ تبركت به أي تيمنت به؛ طعام بريك كأنه مبارك (sihah)؛ معنى البركة الكثرة في كل خير؛ المبارك ما يأتي من قبله الخير الكثير؛ أصل البركة الزيادة والنماء؛ التبريك الدعاء للإنسان وغيره بالبركة؛ بركت عليه تبريكا أي قلت بارك الله عليك؛ البركات السعادة (tahdhib)؛ البركة ثبوت الخير الإلهي في الشيء؛ المبارك ما فيه ذلك الخير؛ يقال لكل ما يشاهد منه زيادة غير محسوسة هو مبارك وفيه بركة (mufradat)؛ البركة من الزيادة والنماء؛ التبريك أن تدعو بالبركة؛ طعام بريك أي ذو بركة (maqayis)
- **B005** Tanrıyı yüceltme — Tanrı yücedir, uludur, kutsaldır ve bütün hayır ona özgüdür
  تبارك الله أي بارك (sihah)؛ تبارك ارتفع؛ تبارك تعالى وتعاظم؛ تبارك الله تمجيد وتعظيم؛ تبارك تقدس (tahdhib)؛ كل موضع ذكر فيه لفظ تبارك فهو تنبيه على اختصاصه تعالى بالخيرات المذكورة (mufradat)؛ تبارك الله تمجيد وتجليل؛ وفسر على تعالى الله (maqayis)
- **B006** işe yapışıp sürdürme — savaşta yer tutup çatışmayı sürdürdüler · savaşta direnme ve çatışma yeri · koşuda var gücüyle çabaladı · onun hakkında kötülemeyi ısrarla sürdürdü · işe devam etti ve onu bırakamadı · bulut aynı yere durmadan yağmur bıraktı
  ابترك أي أسرع في العدو وجد؛ البراكاء الثبات في الحرب والجد؛ براك براك أي ابركوا (sihah)؛ ابترك الرجل في عرض أخيه إذا اجتهد في ذمه؛ الابتراك في العدو الاجتهاد فيه؛ ابترك القوم في الحرب إذا جثوا على الركب ثم اقتتلوا؛ البراكاء مباحة القتال؛ ابترك السحاب إذا ألح بالمطر؛ باركت على التجارة وغيرها أي واظبت عليها (tahdhib)؛ ابتركوا في الحرب أي ثبتوا ولازموا موضع الحرب؛ براكاء الحرب وبروكاؤها للمكان الذي يلزمه الأبطال (mufradat)؛ ابترك الرجل في آخر يتنقصه ويشتمه؛ ابتركوا في الحرب؛ براك براك بمعنى ابركوا؛ برك فلان على الأمر وبارك جميعا إذا واظب عليه؛ ابترك الفرس في عدوه أي اجتهد؛ ابترك السحاب إذا ألح بالمطر (maqayis)
- **B007** çökmüş devenin sabah sütü [kalıp] — çökmüş dişi devenin memesinde birikip sabah sağılan süt · çökeğinde biriken sütünü sağdı
  البركة أن يدر لبن الناقة باركة فيقيمها ويحلبها؛ حلبت بركتها (tahdhib)؛ البركة أن تحلب قبل أن تخرج؛ حلبت الناقة بركتها وحلبت الإبل بركتها إذا حلبت لبنها الذي اجتمع في ضرعها في مبركها؛ لا يسمى بركة إلا ما اجتمع في ضرعها بالليل وحلب بالغدوة (maqayis)
- **B008** beyaz su kuşu — beyaz bir su kuşu
  البركة بالضم طائر من طير الماء أبيض والجمع برك (sihah)؛ البرك واحدتها بركة وهو من طير الماء أبيض (tahdhib)
- **B009** büyük oğlu varken evlenen kadın — büyük oğlu veya büyük çocuğu varken evlenen kadın
  البروك من النساء التي تتزوج ولها ابن بالغ كبير (sihah)؛ البروك من النساء التي تتزوج ولها ولد كبير واسم ذلك الولد الجرنبذ (tahdhib)

## ش ف ع (root_000802): 43:86 ٱلشَّفَٰعَةَ

- **B001** benzerini ekleyerek çiftleştirme — çift olan veya bir benzeri eklenerek çift yapılmış şey · tek olana bir benzerini ekleyip çift yapmak · kuşluk namazının iki bölümü
  الشفع خلاف الوتر (maqayis;sihah)؛ الشفع ما كان من العدد أزواجا (ayn)؛ الشفع الزيادة (tahdhib)؛ ضم الشيء إلى مثله (mufradat)؛ شفعة الضحى ركعتا الضحى (tahdhib)
- **B002** başkası adına aracılık edip destek olma — başkası adına aracılık etme ve ona destek olma · başkası adına istekte bulunan aracı · birinin işi için aracılık eden destekçi · birini aracı kılıp yardımını istemek · birinin işi için başkasına aracılık etmek · aracılığını kabul edip isteğini yerine getirmek · iyi ya da kötü bir işte birine katılıp onu güçlendirmek · düşmanlıkta birine karşı yardım etmek veya ona karşı koymak
  شفع فلان لفلان إذا جاء ثانية ملتمسا مطلبه ومعينا له (maqayis)؛ الشافع الطالب لغيره (ayn;tahdhib)؛ الشفاعة كلام الشفيع للملك في حاجة يسألها لغيره (tahdhib)؛ الانضمام إلى آخر ناصرا له وسائلا عنه (mufradat)؛ يشفع لي بالعداوة أي يعين علي (maqayis)؛ يشفع لي بعداوة أي يضادني (tahdhib)
- **B003** taşınmaz satışında öncelikli alım hakkı — ev veya arazi satışında öncelikli alım hakkı · öncelikli alım hakkını isteyen kişi · satılanı öncelikle alma yetkisini ona vermek
  الشفعة في الدار (maqayis)؛ الشفعة في الدار والأرض (sihah)؛ الشفعة الزيادة حتى تضمه إلى ما عندك (tahdhib)؛ فشفعه وجعله أولى ممن بعد سببه (tahdhib)
- **B004** yavrulu koyun veya iki yavru durumundaki dişi deve — yavrusu yanında bulunan koyun · karnında yavru taşıyan veya ardından başka yavrusu gelen dişi deve
  الشاة الشافع التي معها ولدها (maqayis)؛ ناقة شافع في بطنها ولد ويتبعها آخر (sihah)؛ الشافع التي معها ولدها (tahdhib)؛ ناقة شافع إذا كان في بطنها ولد يتلوها آخر (tahdhib)
- **B005** tek sağımda iki kap dolduran dişi deve — tek sağımda iki kap dolduracak süt veren dişi deve
  ناقة شفوع وهي التي تجمع بين محلبين في حلبة واحدة (maqayis;sihah)؛ ناقة شفوع تجمع بين محلبين في حلبة (tahdhib)
- **B006** tek nesneyi çift görme — tek nesneyi çift gören göz · bir kişiyi iki kişi gibi gösteren görme bozukluğu
  عين شافعة تنظر نظرين (tahdhib)؛ أرى الشخص الواحد شخصين لضعف بصري (tahdhib)

## ء ن ي (root_000063): 43:87 فَأَنَّىٰ

- **B001** ağırdan alma ve geciktirme — ağırbaşlılık ve acele etmeme · bir işte acele etmemek, bekleyip yumuşak davranmak · işlerde duraklayıp acele etmeme · bir şeyi geciktirmek, bekletmek ve yavaşlatmak · birini aceleye sürmemek, onun için beklemek · acele etmeyen, ağırbaşlı kişi · ağırbaşlı kadın veya kalkarken gevşek davranan kadın
  الأناة الحلم والفعل منه تأنى وتأيا (maqayis)؛ التأني (maqayis)؛ آنيت يعني أخرت المجيء وأبطأت (maqayis)؛ الإيناء بمعنى الإبطاء وآنيت الشيء أي أخرته (ayn)؛ آناه يؤنيه إيناء أي أخره وحبسه وأبطأه (sihah)؛ الأناة التؤدة وتأنيت تأخرت (mufradat)
- **B002** gecenin zaman bölümleri — gecenin zaman bölümleri · gecenin tek bir zaman bölümü · ara sıra, zaman zaman
  الإني والأنى ساعة من ساعات الليل والجمع آناء (maqayis;ayn)؛ وآناء الليل واحدها إني وهي الساعة من الليل (jamhara)؛ آناء الليل ساعاته (sihah;tahdhib;mufradat)
- **B003** zamanı gelip olgunluğa erişme — bir şeyin zamanı, olgunluğu veya erişme noktası · zamanı gelmek, olgunlaşmak ve erişmek · senin için zamanı gelmedi mi · yemeğin pişip olgunlaşmasını beklemek · ısısı doruğa varmış çok sıcak su · ısısı yükselmiş sıcak kaynak · olgunlaşmış ve erişmiş
  الإني إدراك الشيء (maqayis)؛ انتظرنا إنى الطعام أي إدراكه (maqayis;ayn)؛ ما أنى لك ولم يأن لك أي لم يحن (maqayis;ayn)؛ حميم آن قد انتهى حره وعين آنية (maqayis;ayn)؛ أنى الشيء يأنى إنى أي حان وأنى أيضا أدرك (sihah)؛ بلغ إناه من شدة الحر (mufradat)
- **B004** içine şey konan kap — içine bir şey konan kap · kaplar ve daha geniş çoğul biçimi
  الإناء ممدود من الآنية والأواني جمع جمع (maqayis)؛ الإناء معروف وجمعه آنية والأواني (sihah)؛ الإناء ما يوضع فيه الشيء وجمعه آنية (mufradat)
- **B005** nereden ve nasıl diye sorma sözü — nereden, hangi yönden, nasıl veya ne zaman · bu sana nereden ya da nasıl geldi · hangi yönden gelirsen, sana gelirim · nereye ya da nasıl yönelirse
  أنى معناها كيف ومن أين (ayn)؛ أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف (sihah)؛ أنى أداة لها معنيان متى ومن أين ويحتمل كيف (tahdhib)؛ أنى للبحث عن الحال والمكان (mufradat)

## ECHO ء و ن (root_000068): for 43:87 فَأَنَّىٰ: withheld observed target; not identity

- **B001** yumuşak ve rahat davranma — yumuşak davrandı · rahatlık, dinginlik ve yumuşak davranma · yolculukta kendini yorma, rahat git · yumuşak ve rahat davrandın · rahat ve dingin adam · rahat ve dingin geceler
  كلمة واحدة تدل على الرفق (maqayis); آن يؤون أونا إذا رفق (maqayis); الأون: الدعة والسكينة والرفق (sihah); أن على نفسك أي ارفق في السير واتدع (maqayis;sihah); رجل آئن (maqayis); رجل آين أي رافه وادع (sihah); ليال أوائن روافه وآينات وادعات (sihah)
- **B002** yük yanı — yük kabının bir yanı; dengeli yük parçası · iki yanlı çıkın veya çift yanlı yük · eşeğin yiyip içince karnı ve iki yanı yük gibi doldu
  الأون: أحد جانبي الخرج (sihah); الأون: العدل (sihah); أون الحمار إذا أكل وشرب وامتلأ بطنه وامتدت خاصرتاه فصار مثل الأون (sihah)
- **B003** belirli zaman — belirli zaman · ayrı zamanlar, ara ara gelen vakitler · o işi ara sıra yapar ve ara sıra bırakır
  الأوان: الحين، والجمع آونة (sihah); فلان يصنع ذلك الأمر آونة إذا كان يصنعه مرارا ويدعه مرارا (sihah)
- **B004** büyük kemerli yapı bölümü — büyük kemerli yapı bölümü · büyük kemerli yapı bölümü; belirli saray örneğiyle de anılır · büyük kemerli yapı bölümü · büyük kemerli yapı bölümleri · büyük kemerli yapı bölümleri
  الأوان والإيوان: الصفة العظيمة كالأزج (sihah); إيوان كسرى (sihah); جمع الإوان أون وجمع الإيوان إيوانات وأواوين (sihah)

## ء ف ك (root_000041): 43:87 يُؤْفَكُونَ

- **B001** tersine çevirip yönünden saptırmak — bir şeyi tersine çevirip yönünden saptırmak · birini bir şeyden çevirip alıkoymak · hakikatten batıla saptırılmış
  أصل واحد يدل على قلب الشيء وصرفه عن جهته (maqayis)؛ أفكته عن الأمر صرفته عنه بالكذب والباطل (ayn)؛ قلبه وصرفه عن الشيء (sihah)؛ يصرف عن الإيمان وصرفنا وتصدنا (tahdhib)؛ كل مصروف عن وجهه الذي يحق أن يكون عليه (mufradat)
- **B002** doğruluktan saptıran yalan ve günah — yalan ve günah · yalan söylemek · büyük yalan · Ne büyük yalan! · insanları yalanla doğrudan saptıran yalancı
  أفك الرجل إذا كذب والإفك الكذب (maqayis)؛ الإفك الكذب والأفاك الذي يأفك الناس عن الحق (ayn)؛ الإفك الكذب والأفيكة ورجل أفاك أي كذاب (sihah)؛ الإفك الإثم والإفك الكذب ويا للأفيكة وهي الكذبة العظيمة (tahdhib)؛ من الصدق في المقال إلى الكذب واستعمل ذلك في الكذب (mufradat)
- **B003** ters çevrilip yok edilmiş yerleşim veya topluluk — ters çevrilip yok edilmiş kentler veya topluluklar · beldenin halkıyla birlikte ters çevrilmesi
  والمؤتكفة الأمم الماضية الضالة المهلكة (ayn)؛ ائتفكت البلدة بأهلها أي انقلبت والمؤتفكات المدن التي قلبها الله (sihah)؛ المؤتفكات جمع مؤتفكة ائتفكت بهم الأرض أي انقلبت (tahdhib)؛ والمؤتفكات بالخاطئة والمؤتفكة أهوى (mufradat)
- **B004** farklı yönlerden esen rüzgarlar [kalıp] — farklı yönlerden esen rüzgarlar
  المؤتفكات الرياح التي تختلف مهابها (maqayis)؛ المؤتفكات الرياح تختلف مهابها (sihah)؛ بالرياح مؤتفك أي اختلفت عليه الأرواح من كل وجه (tahdhib)؛ الرياح العادلة عن المهاب مؤتفكة (mufradat)
- **B005** yağmursuz kalıp kuruyan toprak [kalıp] — yağmur almamış, kuruyup bitkisiz kalmış toprak · toprağın kuraklıktan kavrulması
  أرض مأفوكة أي لم يصبها مطر وليس بها نبات (sihah)؛ أرض مأفوكة وهي التي لم يصبها المطر فأمحلت (tahdhib)؛ ائتفكت تلك الأرض أي احترقت من الجدب (tahdhib)
- **B006** aklı ve muhakemesi zayıflamış olma — tedbir ve çareden yoksun kimse · aklı ve görüşü zayıf, sağlıklı düşünceden uzaklaşmış kimse
  والأفيك المكذب عن حيلته وحزمه والمأفوك الذي يقبل الإفك (ayn)؛ المأفوك المأفون وهو الضعيف العقل والرأي (sihah)؛ الأفيك الذي لا حزم له ولا حيلة والمأفوك الذي لا زور له (tahdhib)؛ أفك يؤفك صرف عقله ورجل مأفوك العقل (mufradat)



===== _commentary/v16/work/s043/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s043/reader_a_pilot.md)

# s043 Semantic Channel Discovery

## Parent Channels

### 1. A Message Gathered, Articulated, and Sent (P1: 43:2-8)
- Semantic invariant: Disclosure is preserved by being gathered, bound, clarified, cognitively held, and carried through successive media.
- Surface relation: direct; 43:2-4 anchors the clear book, Arabic recitation, understanding, and the source of the book, while 43:5-8 follows the reminder through possible withdrawal, prophetic delivery, mockery, and precedent.
- Surprising reach: Recitation behaves like assembly, writing like fastening, reason like a tether, and withdrawal of reminder like turning a page; the passage therefore presents communication as a materially controlled transfer rather than disembodied speech.

#### Subchannel A. The Assembled Inscription
- Reading type: mixed
- Scene or process: Dispersed utterance is collected, joined into a written body, and referred back to an originating register whose form is firmly made.
- Active motifs: gathering into one `quranic:root_001210:B001/m01`; recitation `quranic:root_001210:B002/m01`; joining one thing to another `quranic:root_001283:B001/m01`; written text `quranic:root_001283:B002/m01`; origin and reference point `quranic:root_000053:B002/m01`; firm workmanship `quranic:root_000348:B004/m01`
- Ayah anchors: 43:2 `كِتَٰبِ`; 43:3 `قُرْءَٰنًا`; 43:4 `أُمِّ ٱلْكِتَٰبِ`, `حَكِيمٌ`
- Synthesis: The recitation is not merely voiced: its lexical field first gathers, then the book binds components into a durable textual object. The "mother/source" gives that object an originating register, while wisdom's firmness makes the whole transmission a stabilized construction.

#### Subchannel B. Articulation Under Cognitive Restraint
- Reading type: mixed
- Scene or process: Meaning is exposed in speech and received by an intelligence whose proper action is to restrain error.
- Active motifs: disclosing meaning by speech or sign `quranic:root_000170:B005/m01`; clear articulation `quranic:root_000996:B001/m01`; reason that restrains ignorance `quranic:root_001036:B001/m01`; accurate wisdom `quranic:root_000348:B003/m01`
- Ayah anchors: 43:2 `مُبِينِ`; 43:3 `عَرَبِيًّا`, `تَعْقِلُونَ`; 43:4 `حَكِيمٌ`
- Synthesis: Clarity is jointly produced by an articulating medium and a disciplined receiver. The latent image of reason as restraint usefully reframes understanding as holding the mind to the disclosed course, not simply possessing information.

#### Subchannel C. The Page That May Be Turned Away
- Reading type: mixed
- Scene or process: A reminder stands at the edge of withdrawal, figured both as withholding a communication and as turning over its page because its audience has crossed a limit.
- Active motifs: withdrawing or withholding `quranic:root_000906:B004/m01`; turning and inspecting pages `quranic:root_000867:B003/m01`; gracious turning aside `quranic:root_000867:B002/m01`; reminder-token `quranic:root_000516:B009/m01`; crossing the boundary `quranic:root_000699:B001/m01`
- Ayah anchors: 43:5 `نَضْرِبُ`, `ٱلذِّكْرَ`, `صَفْحًا`, `مُّسْرِفِينَ`
- Synthesis: The same verse activates a page, an act of withholding, and excess beyond a boundary. The reminder is thus pictured as a legible surface that can be turned from view, while the gracious sense of turning aside keeps withdrawal from becoming mere retaliation.

#### Subchannel D. News Carried into a Chain of Precedent
- Reading type: mixed
- Scene or process: Prophetic news is dispatched, repeatedly mocked, and then converted by destruction into an exemplary trace for later hearers.
- Active motifs: consequential reported news `quranic:root_001464:B002/m01`; one who reports from God `quranic:root_001464:B003/m01`; dispatch `quranic:root_000563:B001/m01`; messenger and message `quranic:root_000563:B002/m01`; ridicule `quranic:root_001587:B001/m01`; passing away `quranic:root_001430:B001/m01`; destruction `quranic:root_001596:B001/m01`; exemplary warning `quranic:root_001397:B011/m01`
- Ayah anchors: 43:6 `أَرْسَلْنَا`, `نَّبِىٍّ`; 43:7 `نَّبِىٍّ`, `يَسْتَهْزِءُونَ`; 43:8 `أَهْلَكْنَا`, `مَضَىٰ`, `مَثَلُ`
- Synthesis: Delivery is a moving chain: news arrives through a commissioned carrier, rejection interrupts reception, and the destroyed community itself becomes the next transmissible sign. Failed hearing does not stop the message; it changes the material in which the message is carried.

### 2. The Prepared Route of Return (P1: 43:9-14)
- Semantic invariant: Created surfaces, measured water, and conveyances are prepared to carry life or riders along bounded courses toward a remembered return.
- Surface relation: direct; 43:9-11 moves from earth and cradle to paths, measured rain, dead land, and emergence, while 43:12-14 moves through ships, cattle, riding, settled backs, subjection, remembrance, and return.
- Surprising reach: Earth, water, vessel, and animal back form one transport ecology: each is a prepared substrate that bears something else and thereby rehearses final return.

#### Subchannel A. A Leveled Surface with Courses
- Reading type: mixed
- Scene or process: The lower, cultivable earth is spread as a prepared resting surface and traversed by extended paths that permit orientation.
- Active motifs: fertile lower earth `quranic:root_000025:B002/m01`; leveled resting-place `quranic:root_001451:B002/m01`; preparing and making even `quranic:root_001451:B003/m01`; extended traversable road `quranic:root_000672:B001/m01`; gentle direction to a route `quranic:root_001583:B001/m01`
- Ayah anchors: 43:9 `أَرْضَ`; 43:10 `أَرْضَ`, `مَهْدًا`, `سُبُلًا`, `تَهْتَدُونَ`
- Synthesis: The cradle image is extended from comfort into infrastructure: a surface is leveled, routes are laid through it, and guidance becomes practical orientation within a made terrain.

#### Subchannel B. Measured Water Reactivates Dormant Ground
- Reading type: mixed
- Scene or process: Water is delivered in a fitted measure to inert land, where it reopens vegetative life and models emergence.
- Active motifs: measured limit `quranic:root_001205:B001/m01`; fitted planning and apportionment `quranic:root_001205:B005/m01`; conveying water by pouring `quranic:root_001458:B003/m01`; uncultivated dead ground `quranic:root_001454:B003/m01`; reviving the dead `quranic:root_001503:B002/m01`; rain reviving dry pasture `quranic:root_001503:B004/m01`
- Ayah anchors: 43:11 `نَزَّلَ`, `مَآءًۢ`, `بِقَدَرٍ`, `بَلْدَةً مَّيْتًا`, `أَنشَرْنَا`, `تُخْرَجُونَ`
- Synthesis: Revival is materially staged as controlled delivery rather than undirected abundance. The exact measure makes dead ground a receiving vessel, and vegetative reopening supplies a concrete mechanism for the verse's final emergence.

#### Subchannel C. Circular Vessel and Layered Rider
- Reading type: latent/lexical
- Scene or process: A rounded carrier moves through water while a rider is placed as one layer upon another, making transport an assembly of fitted bodies.
- Active motifs: circular motion and form `quranic:root_001177:B001/m01`; ship moving in water `quranic:root_001177:B003/m01`; mounting a carrier's back `quranic:root_000589:B001/m01`; layering one thing above another `quranic:root_000589:B002/m01`
- Ayah anchors: 43:12 `ٱلْفُلْكِ`, `تَرْكَبُونَ`
- Synthesis: Ship and mount converge as fitted carriers. The latent geometry of circularity and layering materializes the verse's broad category of "what you ride" as a composed transport mechanism rather than a list of vehicles.

#### Subchannel D. Settling on a Back, Then Reversing Home
- Reading type: mixed
- Scene or process: The rider becomes stable on a bearing surface, recognizes its subjection, remembers the giver, and anticipates reversal toward the point of return.
- Active motifs: stable settlement upon something `quranic:root_000766:B003/m01`; the bearing back `quranic:root_000970:B002/m01`; being driven and subjected to a purpose `quranic:root_000685:B001/m01`; remembered presence `quranic:root_000516:B003/m01`; turning toward one's destination `quranic:root_001248:B005/m01`
- Ayah anchors: 43:13 `تَسْتَوُۥا`, `ظُهُورِهِ`, `سَخَّرَ`, `تَذْكُرُوا۟`; 43:14 `مُنقَلِبُونَ`
- Synthesis: Bodily balance on a mount becomes a cognitive and eschatological exercise. The stable back is temporary; its proper use triggers remembrance that every carried journey ends in a reversal toward the Lord.

### 3. Fabricated Kinship as Unwarranted Allocation (P1: 43:15-20)
- Semantic invariant: A claimed divine genealogy is exposed as an act of partition, preference, social formation, and classification that cannot survive evidentiary testing.
- Surface relation: direct; 43:15-16 assigns a part and preferred children, 43:18 invokes ornamented upbringing and dispute, and 43:19-20 tests gender classification by witness, writing, knowledge, and conjecture.
- Surprising reach: Kinship language behaves like property division and record entry, while the discourse's own gendered evaluations become objects of pressure rather than neutral descriptions.

#### Subchannel A. A Portion Carved into a Preferred Line
- Reading type: mixed
- Scene or process: Servants are treated as owned material from which a portion is assigned, while one descendant category is selectively reserved.
- Active motifs: servitude under ownership `quranic:root_000973:B001/m01`; a separated portion `quranic:root_000241:B002/m01`; selecting a preferred part `quranic:root_000873:B002/m01`; a specially reserved share `quranic:root_000873:B003/m01`; lineage branching from an origin `quranic:root_000156:B007/m01`
- Ayah anchors: 43:15 `عِبَادِهِۦ`, `جُزْءًا`; 43:16 `أَصْفَىٰكُم`, `بَنِينَ`
- Synthesis: The genealogy claim is rendered as allocation: a whole is partitioned, a preferred share is selected, and lineage is treated as a divisible possession. That material logic exposes the asymmetry in assigning to God what the speakers refuse for themselves.

#### Subchannel B. Ornamental Formation and Constricted Contest
- Reading type: mixed
- Scene or process: A child is socially formed within ornament, then represented as constrained in adversarial speech; the female category imports a further lexical association of softness.
- Active motifs: youthful formation and upbringing `quranic:root_001502:B002/m01`; ornament `quranic:root_000353:B001/m01`; contest between adversaries `quranic:root_000416:B001/m01`; disclosing meaning in speech `quranic:root_000170:B005/m01`; softness attached to female classification `quranic:root_000058:B002/m01`
- Ayah anchors: 43:18 `يُنَشَّؤُا۟`, `ٱلْحِلْيَةِ`, `ٱلْخِصَامِ`, `غَيْرُ مُبِينٍ`; 43:19 `إِنَٰثًا`
- Synthesis: The scene joins social production, decorative environment, and contested articulation. The latent softness sense does not validate the classification; it reveals how the classification itself can carry an evaluative script into the argument.

#### Subchannel C. Classification Entered into an Evidentiary Record
- Reading type: mixed
- Scene or process: A gender assignment is tested as if before a record office: Was it witnessed, can it be stated from knowledge, and will it be written for later questioning?
- Active motifs: female classification `quranic:root_000058:B001/m01`; witnessed presence `quranic:root_000822:B001/m01`; testimony stated from knowledge `quranic:root_000822:B002/m01`; written text `quranic:root_001283:B002/m01`; entering a name into a register `quranic:root_001283:B004/m01`; estimation by conjecture `quranic:root_000403:B001/m01`; speech without knowledge `quranic:root_000403:B002/m01`
- Ayah anchors: 43:19 `إِنَٰثًا`, `شَهِدُوٓا۟`, `شَهَٰدَتُهُمْ`, `تُكْتَبُ`, `يُسْـَٔلُونَ`; 43:20 `عِلْمٍ`, `يَخْرُصُونَ`
- Synthesis: The claim is converted from inherited assertion into accountable evidence. Presence, informed testimony, inscription, and later questioning form a chain of custody that conjecture cannot complete.

### 4. Inherited Guidance as a Traced Track (P2: 43:21-25)
- Semantic invariant: Authority is imagined as something grasped or followed along an existing track, but an incoming guide can expose whether that track leads to a defensible outcome.
- Surface relation: direct; 43:21 asks whether a book is being held, 43:22-24 repeatedly finds fathers and their traces, and 43:25 shows the track's punitive terminus.
- Surprising reach: Inheritance is not only belief transmission; it is a physical ecology of grip, footprint, leader, path, and heel whose destination can be inspected.

#### Subchannel A. Holding a Book or Finding Footprints
- Reading type: mixed
- Scene or process: The community lacks a held textual warrant and instead discovers a parental route through marks left by earlier movement.
- Active motifs: grasping and holding fast `quranic:root_001424:B001/m01`; finding a thing `quranic:root_001626:B001/m01`; a remaining mark `quranic:root_000011:B003/m01`; walking behind a predecessor `quranic:root_000011:B004/m01`; parental formation `quranic:root_000007:B001/m01`; communal way `quranic:root_000053:B005/m01`
- Ayah anchors: 43:21 `كِتَٰبًا`, `مُسْتَمْسِكُونَ`; 43:22-24 `وَجَدْنَا`, `ءَابَآءَنَا`, `أُمَّةٍ`, `ءَاثَٰرِهِم`
- Synthesis: The contrast is tactile. One authority would be deliberately held; the other is encountered as residual marks and then followed because parental formation has already made the route feel communal.

#### Subchannel B. The Incoming Leader Against Imitative Momentum
- Reading type: mixed
- Scene or process: A warning-bearing messenger offers a more directing lead, while inherited imitation converts a precedent into an unquestioned straight practice.
- Active motifs: model followed by others `quranic:root_001208:B001/m01`; straight customary practice `quranic:root_001208:B003/m01`; gentle direction to truth `quranic:root_001583:B001/m01`; a guide who advances before others `quranic:root_001583:B003/m01`; warning that awakens caution `quranic:root_001488:B001/m01`; messenger and message `quranic:root_000563:B002/m01`; covering the truth `quranic:root_001307:B003/m01`
- Ayah anchors: 43:23 `نَّذِيرٍ`, `ءَابَآءَنَا`, `مُّقْتَدُونَ`; 43:24 `أَهْدَىٰ`, `أُرْسِلْتُم`, `كَٰفِرُونَ`
- Synthesis: Both sides possess a leader-image, but one is only anterior while the other actively directs. The scene distinguishes the momentum of copying from guidance that can answer for the route it opens.

#### Subchannel C. The Track Ends in an Outcome
- Reading type: mixed
- Scene or process: Denial is followed to its rearward end, where looking, consequence, and retaliatory penalty coincide.
- Active motifs: charging another with falsehood `quranic:root_001290:B002/m01`; punishment after repudiation `quranic:root_001545:B002/m01`; directed inspection `quranic:root_001520:B001/m01`; final outcome `quranic:root_001033:B006/m01`; penalty following an offense `quranic:root_001033:B007/m01`
- Ayah anchors: 43:25 `فَٱنتَقَمْنَا`, `فَٱنظُرْ`, `عَٰقِبَةُ`, `ٱلْمُكَذِّبِينَ`
- Synthesis: The inherited route is judged by where its heel lands. Looking at the deniers' outcome transforms "following" from a claim of continuity into a test of destination.

### 5. The Enduring Word in the Descendant Heel (P2: 43:26-28)
- Semantic invariant: Abraham breaks from an inherited object of worship so that a directing word can remain as a trace in the line that follows him.
- Surface relation: direct; 43:26-27 separates Abraham from worship and names the originator who guides, while 43:28 places a remaining word in his descendants for return.
- Surprising reach: A spoken word behaves like a durable residue lodged at the heel of a lineage, joining discourse, bodily succession, and return.

#### Subchannel A. Separation Opens onto Origination
- Reading type: mixed
- Scene or process: Abraham withdraws from inherited worship, then identifies the one who first opens and originates creation as the source of direction.
- Active motifs: separation and disavowal `quranic:root_000099:B002/m01`; obedient worship `quranic:root_000973:B003/m01`; opening by splitting `quranic:root_001165:B001/m01`; originating a thing `quranic:root_001165:B002/m01`; directing gently to truth `quranic:root_001583:B001/m01`
- Ayah anchors: 43:26 `بَرَآءٌ`, `تَعْبُدُونَ`; 43:27 `فَطَرَنِى`, `سَيَهْدِينِ`
- Synthesis: Disavowal is not an empty severance. It clears the inherited field so guidance can be grounded in origination rather than merely in anterior custom.

#### Subchannel B. Speech Deposited as Lineage Residue
- Reading type: latent/lexical
- Scene or process: An intelligible word is made durable, deposited among descendants as heel, offspring, and remaining trace, and oriented toward reversal.
- Active motifs: intelligible word `quranic:root_001316:B002/m01`; lasting existence `quranic:root_000142:B001/m01`; remainder retained from a whole `quranic:root_000142:B002/m01`; heel and rear footprint `quranic:root_001033:B002/m01`; descendant line `quranic:root_001033:B004/m01`; remaining trace `quranic:root_001033:B011/m01`; return to a prior point `quranic:root_000544:B001/m01`
- Ayah anchors: 43:28 `كَلِمَةًۢ`, `بَاقِيَةً`, `عَقِبِهِۦ`, `يَرْجِعُونَ`
- Synthesis: The word is transmitted less like a momentary utterance than like a lodged residue. Heel, descendant, remainder, and return make lineage a moving archive in which the word persists behind each new step.

### 6. The Built Economy of Rank (P2: 43:32-35)
- Semantic invariant: Social rank and material luxury are both produced through distribution, elevation, service, and temporary use, while the protected outcome lies outside that structure.
- Surface relation: direct; 43:32 divides livelihood and raises degrees, 43:33-34 constructs silver roofs, stairs, doors, and couches, and 43:35 names ornament as worldly use against the hereafter.
- Surprising reach: Hierarchy becomes literal architecture: apportioned livelihood rises into stairs and roofs, while wealth's apparent solidity is undercut by silver's lexical dispersal and enjoyment's limited duration.

#### Subchannel A. Divided Livelihood and Vertical Service
- Reading type: mixed
- Scene or process: Livelihood is apportioned into shares, persons are raised by degrees, and the resulting difference places some labor at the service of others.
- Active motifs: separating and assigning a share `quranic:root_001226:B003/m01`; means of living `quranic:root_001067:B002/m01`; elevation of standing `quranic:root_000582:B002/m01`; proceeding step by step `quranic:root_000468:B003/m01`; compelled unpaid service `quranic:root_000685:B002/m01`
- Ayah anchors: 43:32 `يَقْسِمُ`, `قَسَمْنَا`, `مَّعِيشَتَهُمْ`, `رَفَعْنَا`, `دَرَجَٰتٍ`, `سُخْرِيًّا`
- Synthesis: Distribution is spatialized. Shares create height, degrees turn height into a traversable hierarchy, and service becomes the social mechanism that holds its unequal levels together.

#### Subchannel B. An Architecture of Dispersed Metal and Ascent
- Reading type: latent/lexical
- Scene or process: Silver is spread into overhead structures and entrances, linked by ascending devices to rooms furnished for settled repose.
- Active motifs: silver metal `quranic:root_001162:B003/m01`; scattered fragments `quranic:root_001162:B004/m01`; high roof `quranic:root_000720:B001/m01`; ascent upward `quranic:root_000997:B004/m01`; entrance `quranic:root_000163:B001/m01`; supported reclining `quranic:root_001678:B004/m01`; place of settled repose `quranic:root_000697:B011/m01`; ornament `quranic:root_000628:B001/m01`; gold ornament `quranic:root_000628:B002/m01`
- Ayah anchors: 43:33 `فِضَّةٍ`, `سُقُفًا`, `مَعَارِجَ`, `يَظْهَرُونَ`; 43:34 `أَبْوَٰبًا`, `سُرُرًا`, `يَتَّكِـُٔونَ`; 43:35 `زُخْرُفًا`
- Synthesis: The social verticality of the preceding verse hardens into a house. Yet the latent dispersal in silver keeps the structure from reading as ultimate permanence: dazzling material is spread across roofs, stairs, portals, and couches as a constructed arrangement.

#### Subchannel C. Temporary Utility and the Protected Outcome
- Reading type: mixed
- Scene or process: Worldly goods provide real use for an extended interval, but their nearness and delay are contrasted with a later condition secured by protective restraint.
- Active motifs: useful enjoyment `quranic:root_001395:B001/m01`; extended permission to enjoy `quranic:root_001395:B007/m01`; the near and lower world `quranic:root_000493:B002/m01`; what comes later `quranic:root_000019:B001/m01`; placing oneself in protection `quranic:root_001677:B002/m01`
- Ayah anchors: 43:35 `مَتَٰعُ`, `ٱلدُّنْيَا`, `ءَاخِرَةُ`, `ٱلْمُتَّقِينَ`
- Synthesis: The passage does not deny utility; it limits its horizon. Near-world enjoyment is a usable interval, whereas the later outcome belongs to those whose self-restraint places them behind a different kind of protection.

### 7. Captured Orientation and the Counter-Grip (P3: 43:36-44)
- Semantic invariant: Orientation can be captured through dimmed attention, attached companionship, blocked routes, and sealed senses, or stabilized by gripping an inscribed straight course.
- Surface relation: direct; 43:36-38 joins dimness, assigned companion, obstruction, false guidance, and distance, 43:40 stages deafness and blindness, and 43:43-44 answers with held revelation and a straight path.
- Surprising reach: Misguidance appears as an engineered navigation failure, while revelation behaves simultaneously as hidden transfer, inscription, legal reminder, and a road that can be physically held.

#### Subchannel A. Dimming Produces an Attached Substitute
- Reading type: latent/lexical
- Scene or process: Attention dims and turns away; an exchange installs a long tether and binds a companion to the subject.
- Active motifs: low nocturnal visibility `quranic:root_001017:B001/m01`; deliberate turning-blind `quranic:root_001017:B003/m01`; exchange of an equivalent `quranic:root_001275:B003/m01`; binding one thing to another `quranic:root_001221:B001/m01`; attached companion `quranic:root_001221:B002/m01`; long binding cord `quranic:root_000796:B002/m01`; rebellious adversary `quranic:root_000796:B004/m01`
- Ayah anchors: 43:36 `يَعْشُ`, `ذِكْرِ`, `نُقَيِّضْ`, `شَيْطَٰنًا`, `قَرِينٌ`; 43:38 `قَرِينُ`
- Synthesis: The companion is not merely nearby; the branch network materializes assignment as substitution plus fastening. A dimmed perceptual field permits a rival guide to become structurally attached.

#### Subchannel B. Obstructed Route Misread as Guidance
- Reading type: mixed
- Scene or process: A route is turned aside and blocked like a pass behind a barrier, yet calculation mistakes the resulting movement for directed travel until radical distance becomes visible.
- Active motifs: diversion from a course `quranic:root_000848:B001/m01`; blocking mountain `quranic:root_000848:B005/m01`; extended road `quranic:root_000672:B001/m01`; supposition `quranic:root_000318:B002/m01`; direction to truth `quranic:root_001583:B001/m01`; adopted course and manner `quranic:root_001583:B002/m01`; remoteness `quranic:root_000131:B001/m01`; eastern emergence of light `quranic:root_000790:B001/m01`
- Ayah anchors: 43:37 `يَصُدُّونَهُمْ`, `ٱلسَّبِيلِ`, `يَحْسَبُونَ`, `مُّهْتَدُونَ`; 43:38 `بُعْدَ`, `ٱلْمَشْرِقَيْنِ`
- Synthesis: False guidance is not immobility but motion inside a rerouted system. Only the wished-for span between two eastern horizons discloses how far the attached guide has carried its partner from the intended course.

#### Subchannel C. Sealed Hearing and Interior Blindness
- Reading type: mixed
- Scene or process: Auditory and visual apertures close, preventing sound from becoming comprehension and sight from becoming insight.
- Active motifs: loss of hearing `quranic:root_000884:B001/m01`; a sealed gap `quranic:root_000884:B002/m01`; hearing sound `quranic:root_000741:B001/m01`; hearing as understanding and compliance `quranic:root_000741:B003/m01`; loss of physical sight `quranic:root_001049:B001/m01`; blindness of insight `quranic:root_001049:B002/m01`
- Ayah anchors: 43:40 `تُسْمِعُ ٱلصُّمَّ`, `تَهْدِى ٱلْعُمْىَ`, `ضَلَٰلٍ مُّبِينٍ`
- Synthesis: The scene distinguishes organ from uptake. Sound may reach an ear without producing compliance, and visible form may remain without insight; misguidance is therefore a failure of conversion between sensory input and directed response.

#### Subchannel D. Holding the Covertly Inscribed Road
- Reading type: latent/lexical
- Scene or process: A recipient grips a communication delivered in hidden form, also figured as inscription, prophetic report, documentary reminder, and a straight road.
- Active motifs: holding fast `quranic:root_001424:B001/m01`; covert transfer of knowledge `quranic:root_001633:B001/m01`; writing and engraving `quranic:root_001633:B003/m01`; divine report and inspiration `quranic:root_001633:B004/m01`; documentary right and reminder `quranic:root_000516:B008/m01`; straight road `quranic:root_000858:B001/m01`
- Ayah anchors: 43:43 `ٱسْتَمْسِكْ`, `أُوحِىَ`, `صِرَٰطٍ مُّسْتَقِيمٍ`; 43:44 `ذِكْرٌ`, `تُسْـَٔلُونَ`
- Synthesis: Against the attached companion stands a deliberate counter-attachment. Revelation is held because it has the durability of an inscription and charter as well as the directional force of a road.

### 8. Visible Signs and the Unravelled Covenant (P3: 43:45-50)
- Semantic invariant: Signs intensify from visible display to punitive pressure, but temporary relief only reveals whether a pledged bond will remain woven.
- Surface relation: direct; 43:46-48 displays signs, laughter, increasing signs, and punishment, while 43:49-50 moves through covenantal appeal, uncovering punishment, and broken terms.
- Surprising reach: Mockery converts a sign into a spectacle, whereas covenant-breaking is rendered as undoing a cord after it has been tightly made.

#### Subchannel A. A Sign Turned into Spectacle and Pressure
- Reading type: mixed
- Scene or process: An exposed marker is met by visible laughter; subsequent markers grow in magnitude until punitive restraint replaces comic display.
- Active motifs: visible marker `quranic:root_000074:B003/m01`; opened face and exposed teeth `quranic:root_000903:B001/m01`; a visibly clear road `quranic:root_000903:B005/m01`; flashing appearance `quranic:root_000903:B006/m01`; enlarged magnitude `quranic:root_001281:B001/m01`; the greater part of an affair `quranic:root_001281:B002/m01`; withholding and restraint `quranic:root_000994:B003/m01`; inflicted punishment `quranic:root_000994:B005/m01`
- Ayah anchors: 43:46-48 `ـَٔايَٰتِنَا`, `يَضْحَكُونَ`, `ءَايَةٍ`, `أَكْبَرُ`, `ٱلْعَذَابِ`
- Synthesis: Laughter initially makes the sign a public visual event, but escalation changes the sign's operation. What was displayed for recognition becomes pressure that restrains, disclosing the cost of treating a clear marker as entertainment.

#### Subchannel B. A Kept Bond Unthreaded after Relief
- Reading type: latent/lexical
- Scene or process: A party invokes a guarded covenant under pressure, the covering is lifted, and the compact is then pulled apart like finished thread.
- Active motifs: preserving a charge through time `quranic:root_001055:B001/m01`; protected covenant `quranic:root_001055:B003/m01`; lifting a covering `quranic:root_001302:B001/m01`; undoing a finished cord `quranic:root_001547:B001/m01`; breaking a confirmed pact `quranic:root_001547:B002/m01`; reversing an earlier intention `quranic:root_001547:B005/m01`
- Ayah anchors: 43:49 `عَهِدَ`; 43:50 `كَشَفْنَا`, `ٱلْعَذَابَ`, `يَنكُثُونَ`
- Synthesis: Relief tests the material integrity of the promise. Once pressure is uncovered, the pact does not merely lapse; it is actively unworked, strand by strand, after having presented itself as a guarded bond.

### 9. Sovereignty Performed before a Lightened Crowd (P3: 43:51-56)
- Semantic invariant: Pharaoh's rule is staged through public voice, visible infrastructure, bodily ranking, encircling display, and crowd manipulation before water converts the performance into a cautionary precedent.
- Surface relation: direct; 43:51-54 contains the public proclamation, Egypt and its rivers, denigration of Moses, gold and angelic display, and induced obedience; 43:55-56 ends in vengeance, drowning, and example.
- Surprising reach: Political authority is not treated as a single possession but as a production assembled from acoustics, water control, visual rank, bodily depreciation, and managed mass response.

#### Subchannel A. Public Call Makes Rule Visible
- Reading type: mixed
- Scene or process: A ruler gathers an audience, raises a voice whose reach advertises itself, and turns dominion into a thing the crowd is told to see.
- Active motifs: assembly in a public council `quranic:root_001486:B001/m01`; raised public call `quranic:root_001486:B002/m01`; visibility like a calling voice `quranic:root_001486:B008/m01`; dominion and political rule `quranic:root_001444:B003/m01`; physical seeing `quranic:root_000121:B001/m01`
- Ayah anchors: 43:51 `نَادَىٰ`, `قَوْمَهُ`, `مُلْكُ`, `تُبْصِرُونَ`
- Synthesis: The proclamation performs what it claims. Voice convenes the political body, and commanded sight turns sovereignty into a public spectacle whose apparent evidence is the ruler's own display.

#### Subchannel B. Bounded Waterworks as Political Capital
- Reading type: latent/lexical
- Scene or process: A bounded city is sustained by channels that split the ground, widen it, and carry a regular flow beneath the sovereign's position.
- Active motifs: boundary and barrier `quranic:root_001428:B002/m01`; established city `quranic:root_001428:B003/m01`; water that secures a community's affairs `quranic:root_001444:B007/m01`; river channel cutting the ground `quranic:root_001559:B001/m01`; opening and widening for flow `quranic:root_001559:B003/m01`; running current `quranic:root_000240:B001/m01`; established course or routine `quranic:root_000240:B002/m01`
- Ayah anchors: 43:51 `مُلْكُ`, `مِصْرَ`, `ٱلْأَنْهَٰرُ`, `تَجْرِى`, `تَحْتِىٓ`
- Synthesis: The rivers function as more than scenery. Their bounded, cut, widened, and regular flow materializes a hydraulic basis for rule, allowing Pharaoh to present controlled circulation as proof of personal dominion.

#### Subchannel C. A Rival Reduced through Body and Speech
- Reading type: mixed
- Scene or process: Moses is depreciated as socially low and instrumentally weak, while near-failure of articulation is made into a status argument.
- Active motifs: abasement and weakness `quranic:root_001453:B001/m01`; degradation through use `quranic:root_001453:B005/m01`; approaching but not completing an act `quranic:root_001329:B002/m01`; disclosing meaning in speech `quranic:root_000170:B005/m01`
- Ayah anchors: 43:52 `مَهِينٌ`, `لَا يَكَادُ`, `يُبِينُ`
- Synthesis: Pharaoh turns communicative friction into social inferiority. The latent "used-up" sense of abasement sharpens the maneuver: the rival is framed as a defective instrument whose speech cannot support rule.

#### Subchannel D. Encircling Display Manufactures Rank
- Reading type: latent/lexical
- Scene or process: Elevation is displayed through encircling metal and attached attendants, so prestige appears as what surrounds and accompanies a body.
- Active motifs: elevated enclosure `quranic:root_000758:B002/m01`; bracelet enclosing the hand `quranic:root_000758:B004/m01`; gold metal `quranic:root_000522:B001/m01`; gilding that overlays another material `quranic:root_000522:B002/m01`; binding companions together `quranic:root_001221:B001/m01`; attached entourage `quranic:root_001221:B002/m01`
- Ayah anchors: 43:53 `أَسْوِرَةٌ مِّن ذَهَبٍ`, `مَلَٰٓئِكَةُ`, `مُقْتَرِنِينَ`
- Synthesis: Rank is externalized into enclosure and accompaniment. Gold covers, bracelets circle, and attendants bind themselves to the claimant; authority is imagined as a visible shell and retinue.

#### Subchannel E. The Crowd Is Made Light Enough to Obey
- Reading type: mixed
- Scene or process: A ruler strips weight from collective judgment, producing volatility and then easy compliance.
- Active motifs: reduction of weight `quranic:root_000427:B001/m01`; lightheaded instability `quranic:root_000427:B004/m01`; contemptuous belittling `quranic:root_000427:B005/m01`; lightness yielding compliance `quranic:root_000427:B007/m01`; obedience `quranic:root_000956:B001/m01`; making the self readily yield `quranic:root_000956:B006/m01`
- Ayah anchors: 43:54 `فَٱسْتَخَفَّ قَوْمَهُ`, `فَأَطَاعُوهُ`
- Synthesis: Obedience is manufactured by changing the crowd's weight. Belittlement and instability make the collective easier to move, so compliance becomes the outcome of a deliberate reduction in deliberative resistance.

#### Subchannel F. Flooded Rule Becomes Precedent
- Reading type: mixed
- Scene or process: Accumulated anger becomes retaliation, water overwhelms the whole group, and the destroyed regime is placed in front of later people as an exemplary warning.
- Active motifs: anger mixed with grief `quranic:root_000032:B002/m01`; punitive retaliation `quranic:root_001545:B002/m01`; drowning in water `quranic:root_001080:B001/m01`; total engulfment `quranic:root_001080:B005/m01`; what advances before another `quranic:root_000733:B001/m01`; exemplary punishment `quranic:root_001397:B002/m01`; warning example `quranic:root_001397:B011/m01`
- Ayah anchors: 43:55 `ءَاسَفُونَا`, `ٱنتَقَمْنَا`, `أَغْرَقْنَٰهُمْ أَجْمَعِينَ`; 43:56 `سَلَفًا`, `مَثَلًا`
- Synthesis: The waterworks claimed as evidence of rule reverse into the medium of its erasure. Drowning then advances the regime into history as a precedent: the spectacle of sovereignty becomes the spectacle that warns against it.

### 10. Example as a Directional Marker (P4: 43:57-65)
- Semantic invariant: An example can orient hearers toward a straight course, but argumentative twisting, noise, and partisan divergence can convert the same marker into obstruction.
- Surface relation: direct; 43:57-59 disputes the example of Mary's son, 43:61-64 makes him a marker and joins wisdom to a straight path, and 43:62-65 opposes that route with satanic obstruction and divided parties.
- Surprising reach: The passage treats argument as twisted cord and examples as navigational signs; interpretation is therefore a contest over what kind of route a sign will open.

#### Subchannel A. The Example Twisted into Noise
- Reading type: mixed
- Scene or process: A represented example is seized by adversaries, tightly twisted into contention, and amplified as collective noise.
- Active motifs: making an example visible `quranic:root_000906:B003/m01`; proverbial comparison `quranic:root_001397:B003/m01`; exemplary sign `quranic:root_001397:B011/m01`; public clamor `quranic:root_000848:B006/m01`; tightly twisted cord `quranic:root_000229:B001/m01`; entangled dispute `quranic:root_000229:B002/m01`; adversarial contest `quranic:root_000416:B001/m01`
- Ayah anchors: 43:57 `ضُرِبَ`, `مَثَلًا`, `يَصِدُّونَ`; 43:58 `ضَرَبُوهُ`, `جَدَلًۢا`, `خَصِمُونَ`
- Synthesis: The problem is not lack of a sign but manipulation of it. The example is wound into a verbal cord whose tightness sustains contest, while noise substitutes for directional uptake.

#### Subchannel B. The Servant Becomes a Marker
- Reading type: mixed
- Scene or process: A favored servant is made an example whose distinguishing mark points beyond himself toward the Hour.
- Active motifs: worshipful servanthood `quranic:root_000973:B003/m01`; bestowed good condition `quranic:root_001525:B001/m01`; example as instructive sign `quranic:root_001397:B011/m01`; distinguishing mark that guides `quranic:root_001040:B002/m01`
- Ayah anchors: 43:59 `عَبْدٌ`, `أَنْعَمْنَا`, `مَثَلًا`; 43:61 `عِلْمٌ لِّلسَّاعَةِ`
- Synthesis: Servanthood and favor prevent the example from becoming an independent rival. His exemplary status instead functions like a landmark, directing attention through him toward the promised temporal horizon.

#### Subchannel C. Wisdom Clarifies a Traversable Course
- Reading type: mixed
- Scene or process: Clear signs and accurate judgment disclose disputed matters, then become a straight path to be followed.
- Active motifs: disclosing meaning `quranic:root_000170:B005/m01`; accurate wisdom `quranic:root_000348:B003/m01`; a restraining bit that governs motion `quranic:root_000348:B006/m01`; straight road `quranic:root_000858:B001/m01`; following behind `quranic:root_000175:B001/m01`; tracing step after step `quranic:root_000175:B003/m01`
- Ayah anchors: 43:61 `ٱتَّبِعُونِ`, `صِرَٰطٌ مُّسْتَقِيمٌ`; 43:63 `بِٱلْبَيِّنَٰتِ`, `ٱلْحِكْمَةِ`, `أُبَيِّنَ`; 43:64 `صِرَٰطٌ مُّسْتَقِيمٌ`
- Synthesis: Wisdom supplies both discernment and control, like a bit that keeps movement aligned. Clarification is complete only when the disclosed distinction becomes a course that bodies and communities can actually follow.

#### Subchannel D. Obstruction Produces Partisan Divergence
- Reading type: mixed
- Scene or process: A distant, rebellious adversary diverts travelers behind a barrier; parties then take mutually different routes until disagreement becomes a pressuring event.
- Active motifs: distance and severance `quranic:root_000796:B001/m01`; rebellious adversary `quranic:root_000796:B004/m01`; diversion from a route `quranic:root_000848:B001/m01`; blocking barrier `quranic:root_000848:B005/m01`; each taking another route `quranic:root_000433:B004/m01`; faction united around an opinion `quranic:root_000315:B001/m01`; event that presses upon a party `quranic:root_000315:B003/m01`
- Ayah anchors: 43:62 `يَصُدَّنَّكُمُ ٱلشَّيْطَٰنُ`; 43:65 `ٱخْتَلَفَ ٱلْأَحْزَابُ مِنۢ بَيْنِهِمْ`
- Synthesis: Divergence is the downstream product of obstruction. Once the shared route is blocked, difference hardens into organized parties, and the parties' own cohesion intensifies separation from one another.

### 11. Relational Topology Reversed (P4: 43:67-69)
- Semantic invariant: The Hour tests what actually occupies the space between persons: intimacy without protection reverses into hostility, while protected trust removes fear and grief.
- Surface relation: direct; 43:67 reverses intimate friends into enemies except the protected, and 43:68-69 addresses believing, submitted servants with security from fear and grief.
- Surprising reach: Friendship is pictured as something that enters the gaps of the self, whereas protection is a barrier that preserves affective and social bonds under eschatological pressure.

#### Subchannel A. Intimacy Fills a Gap, Then Turns Hostile
- Reading type: latent/lexical
- Scene or process: Affection enters the interstices between persons, but an unprotected bond reverses under pressure into direct enmity.
- Active motifs: gap between things `quranic:root_000435:B001/m01`; affection permeating the self `quranic:root_000435:B003/m01`; hostility between enemies `quranic:root_000993:B003/m01`
- Ayah anchors: 43:67 `ٱلْأَخِلَّآءُ`, `لِبَعْضٍ عَدُوٌّ`, `ٱلْمُتَّقِينَ`
- Synthesis: The latent geometry of friendship explains the severity of the reversal. What had occupied the inner gaps of relation does not merely disappear; it turns across those same gaps as hostility.

#### Subchannel B. Protection Stabilizes Trust and Affect
- Reading type: mixed
- Scene or process: Self-protection creates a barrier against anticipated harm, allowing inward trust, safety, and submission to replace fear and roughened grief.
- Active motifs: placing oneself behind protection `quranic:root_001677:B002/m01`; anticipated fear `quranic:root_000447:B001/m01`; inward roughness of grief `quranic:root_000317:B001/m01`; secure stillness of heart `quranic:root_000054:B001/m01`; trusted affirmation `quranic:root_000054:B002/m01`; safety from harm `quranic:root_000737:B001/m01`
- Ayah anchors: 43:67 `ٱلْمُتَّقِينَ`; 43:68 `لَا خَوْفٌ`, `لَا تَحْزَنُونَ`; 43:69 `ءَامَنُوا۟`, `مُسْلِمِينَ`
- Synthesis: Protection is not isolation but the condition under which relation survives the Hour. It quiets the expected harm that produces fear and smooths the inner roughness of grief, leaving trust capable of submission.

### 12. The Inherited Garden Feast (P4: 43:70-73)
- Semantic invariant: Entry, enclosure, circulation, desire, labor, inheritance, fruit, and eating form a complete economy of enduring delight.
- Surface relation: direct; 43:70 joins entry, spouses, and delight, 43:71 circulates gold vessels around desire and sight, and 43:72-73 links inherited garden, work, abundant fruit, and eating.
- Surprising reach: The garden is both social feast and functioning ecology: concealment by vegetation, latent water, circulating vessels, and harvest make delight materially sustainable.

#### Subchannel A. Paired Entry into Delight
- Reading type: mixed
- Scene or process: Persons cross an interior threshold with their partners and enter a condition of beautified, bestowed joy.
- Active motifs: entering an interior `quranic:root_000464:B001/m01`; intimate spousal entry `quranic:root_000464:B002/m01`; paired companion `quranic:root_000652:B001/m01`; marriage partner `quranic:root_000652:B002/m01`; beauty and splendor `quranic:root_000287:B002/m01`; bestowed delight `quranic:root_000287:B005/m01`
- Ayah anchors: 43:70 `ٱدْخُلُوا۟ ٱلْجَنَّةَ`, `أَزْوَٰجُكُمْ`, `تُحْبَرُونَ`
- Synthesis: Entry is relational rather than solitary. The threshold opens into paired belonging, and delight appears as a state actively conferred upon those who enter together.

#### Subchannel B. An Enclosed, Watered Ecology
- Reading type: latent/lexical
- Scene or process: Dense vegetation conceals and encloses a fertile space whose water-bearing terms support sustained growth.
- Active motifs: garden concealed by trees `quranic:root_000266:B003/m01`; interwoven, surging vegetation `quranic:root_000266:B011/m01`; fertility and water `quranic:root_000287:B007/m01`; flowing spring `quranic:root_001069:B006/m01`
- Ayah anchors: 43:70 `ٱلْجَنَّةَ`, `تُحْبَرُونَ`; 43:71 `أَعْيُنُ`; 43:72 `ٱلْجَنَّةُ`
- Synthesis: The garden's concealment is productive rather than merely hidden. Tree cover, interwoven growth, fertility, and the eye/spring resonance supply an ecological substrate beneath the feast's visible luxury.

#### Subchannel C. Circulating Vessels Meet Desire and Sight
- Reading type: mixed
- Scene or process: Service moves in a circuit with broad plates and handleless cups, bringing metal, drink, appetite, pleasure, and vision into one recurring feast.
- Active motifs: circulation around a center `quranic:root_000957:B001/m01`; broad plate `quranic:root_000845:B004/m01`; gold metal `quranic:root_000522:B001/m01`; handleless drinking cup `quranic:root_001328:B001/m01`; drinking from a cup `quranic:root_001328:B005/m01`; movement of desire `quranic:root_000825:B001/m01`; sensory pleasure `quranic:root_001352:B001/m01`; seeing eye `quranic:root_001069:B001/m01`
- Ayah anchors: 43:71 `يُطَافُ`, `صِحَافٍ مِّن ذَهَبٍ`, `أَكْوَابٍ`, `تَشْتَهِيهِ ٱلْأَنفُسُ`, `تَلَذُّ ٱلْأَعْيُنُ`
- Synthesis: Delight is organized as circulation, not static possession. Vessels repeatedly close the distance between provision and appetite, while gold and sight give the service a visible rhythm.

#### Subchannel D. Work Becomes Inherited Harvest
- Reading type: mixed
- Scene or process: Deliberate work yields an inheritance whose abundant fruit supplies both delight and repeated nourishment.
- Active motifs: inheritance from a predecessor `quranic:root_001639:B001/m01`; intentional work `quranic:root_001046:B001/m01`; recompense for labor `quranic:root_001046:B004/m01`; desirable fruit `quranic:root_001174:B002/m01`; eating `quranic:root_000043:B001/m01`; produce of tree and field `quranic:root_000043:B002/m01`; edible share and provision `quranic:root_000043:B003/m01`; numerical abundance `quranic:root_001286:B001/m01`
- Ayah anchors: 43:72 `أُورِثْتُمُوهَا`, `تَعْمَلُونَ`; 43:73 `فَٰكِهَةٌ كَثِيرَةٌ`, `تَأْكُلُونَ`
- Synthesis: Inheritance does not erase work; it names the form in which work's recompense is received. Fruit unites aesthetic delight, agricultural yield, allotted provision, and the bodily act of eating.

### 13. Irreversible Confinement and the Refused End (P5: 43:74-78)
- Semantic invariant: A self-produced offense settles into a fixed condition whose intensity does not slacken, whose inhabitants lose speech and hope, and whose requested termination is denied by the truth they resisted.
- Surface relation: direct; 43:74-76 joins criminality, permanence, unrelieved punishment, despair, and self-wronging, while 43:77-78 asks for decisive ending and receives continued residence after rejected truth.
- Surprising reach: Hell is figured less as a moment of impact than as a failed exit system: cutting, attachment, weakened force, silence, delayed verdict, and continued waiting all prevent closure.

#### Subchannel A. A Cut-Off State That Does Not Slack
- Reading type: latent/lexical
- Scene or process: Offense cuts its agents off and reaches completion, then fixes them to a state whose punitive force never relaxes.
- Active motifs: cutting and severance `quranic:root_000239:B001/m01`; culpable offense `quranic:root_000239:B004/m01`; a term reaching its cutoff `quranic:root_000239:B006/m01`; unfailing permanence `quranic:root_000429:B001/m01`; clinging residence `quranic:root_000429:B002/m01`; weakness after intensity `quranic:root_001125:B001/m01`
- Ayah anchors: 43:74 `ٱلْمُجْرِمِينَ`, `عَذَابِ جَهَنَّمَ`, `خَٰلِدُونَ`; 43:75 `لَا يُفَتَّرُ`
- Synthesis: Criminality's latent cut becomes the boundary of confinement. Permanence adds adhesion, while the denied slackening means no loss of punitive force can open an exit.

#### Subchannel B. Despair Silences the Self-Wronging
- Reading type: mixed
- Scene or process: Hope is cut off until speech stops, while injustice is exposed as placing and holding the self outside its due position.
- Active motifs: severed hope `quranic:root_000149:B001/m01`; silence under despair `quranic:root_000149:B003/m01`; placing a thing in the wrong position `quranic:root_000967:B004/m01`; withholding a due right `quranic:root_000967:B008/m01`
- Ayah anchors: 43:75 `مُبْلِسُونَ`; 43:76 `ظَلَمْنَٰهُمْ`, `ٱلظَّٰلِمِينَ`
- Synthesis: Despair is not just emotion but communicative shutdown. The adjoining injustice senses locate the cause in a distorted placement and withheld due, making silence the settled outcome of self-misplacement.

#### Subchannel C. A Call for Decisive Closure Meets Waiting
- Reading type: mixed
- Scene or process: The confined raise a call to authority for a death-dealing verdict, but the answer fixes them in continued, expectant residence.
- Active motifs: raised call `quranic:root_001486:B002/m01`; sovereign authority `quranic:root_001444:B003/m01`; decisive judgment `quranic:root_001237:B001/m01`; death as executed decree `quranic:root_001237:B003/m01`; completion and ending `quranic:root_001237:B004/m01`; fixed waiting `quranic:root_001437:B001/m01`
- Ayah anchors: 43:77 `نَادَوْا۟`, `يَٰمَٰلِكُ`, `لِيَقْضِ`, `مَّٰكِثُونَ`
- Synthesis: Their request seeks closure in every sense of judgment: verdict, death, and completion. The answer substitutes waiting residence, turning the desired endpoint into further duration.

#### Subchannel D. Refused Truth Becomes the Governing Condition
- Reading type: mixed
- Scene or process: Stable truth is delivered and made evident, but aversion refuses its fit; the rejected standard now explains the confinement.
- Active motifs: truth stable against falsehood `quranic:root_000347:B001/m01`; making truth manifest `quranic:root_000347:B005/m01`; aversion opposed to acceptance `quranic:root_001295:B001/m01`
- Ayah anchors: 43:78 `جِئْنَٰكُم بِٱلْحَقِّ`, `لِلْحَقِّ كَٰرِهُونَ`
- Synthesis: Truth is not introduced as new information at the end of the scene; it is the refused measure that makes the fixed outcome intelligible. Their aversion converts an offered correspondence with reality into an enduring mismatch.

### 14. The Tightened Plot in an Audible Archive (P5: 43:79-80)
- Semantic invariant: Human planning attempts to close itself into a hidden, firmly twisted decision, but divine hearing and written mediation keep it open to an external record.
- Surface relation: direct; 43:79 repeats the making-fast of a plan, and 43:80 joins secret, private counsel, hearing, messengers, and writing.
- Surprising reach: Plotting is a rope-making operation, while surveillance is not passive awareness but a relay from sound through commissioned recorders into binding inscription.

#### Subchannel A. Resolve Twisted Shut
- Reading type: latent/lexical
- Scene or process: Deliberation is pulled into a cord-like, tightly finished decision, answered by an equally settled counter-resolution.
- Active motifs: tightly twisting a cord `quranic:root_000110:B001/m01`; counsel and deliberate planning `quranic:root_000051:B007/m01`
- Ayah anchors: 43:79 `أَبْرَمُوا۟ أَمْرًا`, `مُبْرِمُونَ`
- Synthesis: The repeated verb gives planning a material finish: a decision is not merely held but twisted until it seems closed. The answering resolution denies that closure any monopoly over the outcome.

#### Subchannel B. Secrecy Withdraws into an Interior
- Reading type: latent/lexical
- Scene or process: Speech is hidden in an inner place and restricted to private interlocutors who assume the enclosure is complete.
- Active motifs: concealment in an interior `quranic:root_000697:B001/m01`; penetrating hidden matters `quranic:root_000697:B014/m01`; confidential exchange `quranic:root_001476:B005/m01`
- Ayah anchors: 43:80 `سِرَّهُمْ`, `نَجْوَىٰهُم`
- Synthesis: Secret and private counsel create nested interiors, but the same lexical field contains penetration into hidden matters. The attempted enclosure therefore carries its own latent breach.

#### Subchannel C. Heard Speech Becomes a Written Register
- Reading type: mixed
- Scene or process: Sound is received as intelligible content, passed through commissioned agents, joined into script, and entered into a durable register.
- Active motifs: hearing sound `quranic:root_000741:B001/m01`; hearing as comprehension `quranic:root_000741:B003/m01`; messenger and commission `quranic:root_000563:B002/m01`; written text `quranic:root_001283:B002/m01`; binding determination in writing `quranic:root_001283:B003/m01`; registering an entry `quranic:root_001283:B004/m01`
- Ayah anchors: 43:80 `نَسْمَعُ`, `رُسُلُنَا`, `يَكْتُبُونَ`
- Synthesis: The record is a conversion chain: acoustic event becomes understood content, commissioned mediation, and fixed inscription. Private speech cannot remain ephemeral because the archive gives it a second, durable body.

### 15. Sovereign Canopy without Genealogy (P5: 43:81-85)
- Semantic invariant: Divine sovereignty is grounded in origination, servanthood, encompassing height, throne, possession, knowledge, and return rather than biological derivation.
- Surface relation: direct; 43:81-82 rejects the child claim and transcends description, while 43:84-85 spans deity in heaven and earth, kingdom, knowledge of the Hour, and return.
- Surprising reach: The denial of genealogy is answered with architecture and jurisdiction: sky, lower earth, elevated throne, and the stable frame of rule replace lineage as the model of relation.

#### Subchannel A. Offspring Claim Recast as Servitude
- Reading type: mixed
- Scene or process: A claim of biological derivation is tested against ownership, obedient service, leveled submission, and transcendence from the category itself.
- Active motifs: biological offspring `quranic:root_001683:B001/m01`; something generated from another thing `quranic:root_001683:B005/m01`; servitude under ownership `quranic:root_000973:B001/m01`; obedient worship `quranic:root_000973:B003/m01`; leveling a road for submission `quranic:root_000973:B005/m01`; declaring transcendence `quranic:root_000666:B002/m01`
- Ayah anchors: 43:81 `وَلَدٌ`, `لِّلرَّحْمَٰنِ`, `ٱلْعَٰبِدِينَ`; 43:82 `سُبْحَٰنَ`
- Synthesis: Biological production and servanthood propose incompatible relation-types. The passage replaces derivation from divine substance with owned, obedient, and leveled relation, then marks the biological description as beneath the transcendent frame.

#### Subchannel B. Sky, Earth, and Throne Form an Encompassing Structure
- Reading type: latent/lexical
- Scene or process: Height overspreads the lower earth beneath a raised throne whose canopy and structural stability encompass the intervening realm.
- Active motifs: elevation `quranic:root_000745:B001/m01`; sky as what rises and shades `quranic:root_000745:B004/m01`; lower realm beneath the sky `quranic:root_000025:B001/m01`; fertile earth `quranic:root_000025:B002/m01`; elevated royal seat `quranic:root_001000:B001/m01`; raised canopy `quranic:root_001000:B002/m01`; stable frame of an order `quranic:root_001000:B006/m01`
- Ayah anchors: 43:82 `ٱلسَّمَٰوَٰتِ`, `ٱلْأَرْضِ`, `ٱلْعَرْشِ`; 43:84-85 `ٱلسَّمَآءِ`, `ٱلْأَرْضِ`, `ٱلسَّمَٰوَٰتِ`, `وَمَا بَيْنَهُمَا`
- Synthesis: The response to false genealogy is a total spatial frame. What is above, below, and between is held under a throne that is both seat and supporting structure, making sovereignty architectonic rather than reproductive.

#### Subchannel C. Dominion Knows and Receives the Return
- Reading type: mixed
- Scene or process: Lordship perfects and owns the whole order, knowledge exposes its appointed horizon, and all movement reverses back into that dominion.
- Active motifs: lordship and ownership `quranic:root_000532:B001/m01`; formative completion `quranic:root_000532:B002/m01`; dominion and rule `quranic:root_001444:B003/m01`; disclosed knowledge `quranic:root_001040:B001/m01`; a marker that directs `quranic:root_001040:B002/m01`; return to the point of origin `quranic:root_000544:B001/m01`; returning speech or answer `quranic:root_000544:B005/m01`
- Ayah anchors: 43:82 `رَبِّ`; 43:84 `ٱلْحَكِيمُ ٱلْعَلِيمُ`; 43:85 `مُلْكُ`, `عِلْمُ ٱلسَّاعَةِ`, `تُرْجَعُونَ`
- Synthesis: Possession, formative care, and knowledge converge on return. The Hour is not an external interruption of the order but its known marker, and return is the answering motion by which all claims re-enter the sovereign frame.

### 16. Truth-Bearing Access versus Deflected Acknowledgment (P5: 43:86-87)
- Semantic invariant: Legitimate access requires actual possession, a joining role, witnessed truth, and knowledge; bare acknowledgment without directional integrity cannot supply it.
- Surface relation: direct; 43:86 denies possession of intercession except for knowledgeable truth-witness, and 43:87 records acknowledgment of the creator followed by deflection.
- Surprising reach: Intercession is a joining operation rather than verbal preference, and falsehood is a force that physically turns an acknowledged fact away from its proper course.

#### Subchannel A. Invocation Cannot Manufacture Possession
- Reading type: latent/lexical
- Scene or process: A call asserts a relation or claim, but the invoked party lacks ownership and therefore cannot add itself as a mediating second.
- Active motifs: calling and drawing by speech `quranic:root_000478:B001/m01`; asserted claim or affiliation `quranic:root_000478:B002/m01`; ownership and disposal `quranic:root_001444:B002/m01`; dominion `quranic:root_001444:B003/m01`; joining a thing to its like `quranic:root_000802:B001/m01`; mediator joining another party `quranic:root_000802:B002/m01`
- Ayah anchors: 43:86 `يَدْعُونَ`, `مِن دُونِهِ`, `لَا يَمْلِكُونَ`, `ٱلشَّفَٰعَةَ`
- Synthesis: Calling does not create capacity. Intercession requires a real joining power grounded in possession; asserted affiliation alone cannot add an unauthorized party to the relation.

#### Subchannel B. Testimony Must Carry Knowledge of Truth
- Reading type: mixed
- Scene or process: A witness must be present, state what is known, and make truth manifest rather than merely lend a tongue to a claim.
- Active motifs: presence at an event `quranic:root_000822:B001/m01`; testimony from knowledge `quranic:root_000822:B002/m01`; the witnessing tongue `quranic:root_000822:B005/m01`; truth corresponding to reality `quranic:root_000347:B001/m01`; manifesting truth `quranic:root_000347:B005/m01`; disclosed knowledge `quranic:root_001040:B001/m01`
- Ayah anchors: 43:86 `شَهِدَ بِٱلْحَقِّ`, `يَعْلَمُونَ`
- Synthesis: The exception is evidentiary, not merely personal. Presence, informed statement, truthful correspondence, and knowledge form the minimum structure by which testimony can mediate.

#### Subchannel C. Acknowledged Creation Is Turned off Course
- Reading type: mixed
- Scene or process: The speakers identify the originator, but a deflecting operation reverses that recognition away from its proper consequence.
- Active motifs: originating creation `quranic:root_000434:B002/m01`; turning a thing from its direction `quranic:root_000041:B001/m01`; falsehood diverted from truth `quranic:root_000041:B002/m01`
- Ayah anchors: 43:87 `سَأَلْتَهُم`, `خَلَقَهُمْ`, `ٱللَّهُ`, `يُؤْفَكُونَ`
- Synthesis: The defect lies after cognition. Creation is acknowledged, but the inference is rotated away from the fact just confessed; falsehood operates as directional reversal rather than simple ignorance.

### 17. Speech Left to Run, Then Released (P5: 43:83, 88-89)
- Semantic invariant: Aimless discourse is temporarily left to move within its own medium until a fixed encounter, while the answering speech adopts disciplined disengagement and peace.
- Surface relation: direct; 43:83 leaves them to wade and play until the promised day, and 43:88-89 moves from the complaint of unbelief to gracious turning, peace, and future knowledge.
- Surprising reach: Discourse behaves like water that can be entered and stirred, whereas the final response behaves like turning a page and releasing one's hold; the contrast is between immersion and controlled exit.

#### Subchannel A. Wading and Play under a Fixed Appointment
- Reading type: latent/lexical
- Scene or process: Participants enter and stir a discursive medium without serious aim, but their movement remains bounded by a set time of encounter.
- Active motifs: entering water `quranic:root_000446:B001/m01`; entering discussion or an affair `quranic:root_000446:B002/m01`; purposeless play `quranic:root_001358:B001/m01`; appointed time and place `quranic:root_001662:B003/m01`; meeting face to face `quranic:root_001372:B004/m01`; encountering one's outcome `quranic:root_001372:B007/m01`
- Ayah anchors: 43:83 `يَخُوضُوا۟`, `يَلْعَبُوا۟`, `يُلَٰقُوا۟`, `يَوْمَهُمُ`, `يُوعَدُونَ`
- Synthesis: The command permits motion but not escape. Wading captures the immersive, self-stirring quality of their discourse, while appointment and encounter impose a shore it cannot move.

#### Subchannel B. Complaint Gives Way to Gracious Release
- Reading type: mixed
- Scene or process: Unbelief is named, but the response turns over the contentious surface, releases reciprocal hostility, and speaks peace while deferring disclosure to later knowledge.
- Active motifs: trusted affirmation refused `quranic:root_000054:B002/m01`; gracious turning aside `quranic:root_000867:B002/m01`; turning a page `quranic:root_000867:B003/m01`; safety from harm `quranic:root_000737:B001/m01`; peaceful relation `quranic:root_000737:B004/m01`; releasing one's hold `quranic:root_000737:B012/m01`; disclosed knowledge `quranic:root_001040:B001/m01`
- Ayah anchors: 43:88 `قَوْمٌ لَّا يُؤْمِنُونَ`; 43:89 `فَٱصْفَحْ`, `سَلَٰمٌ`, `يَعْلَمُونَ`
- Synthesis: The final speech refuses to re-enter the wading contest. Page-turning, release, and peace form a controlled exit from reciprocal antagonism, while "they will know" leaves final disclosure to the approaching encounter.

## Standalone Subchannels

### S1. The Face as a Sealed Pressure Vessel (P1: 43:17)
- Reading type: latent/lexical
- Scene or process: News first alters the exposed skin, then blackens the visible face while emotion is held inside like a filled opening that has been stopped.
- Active motifs: news that opens the skin with joy `quranic:root_000120:B005/m01`; visible face and frontal surface `quranic:root_001630:B001/m01`; blackness against white `quranic:root_000757:B001/m01`; anger or grief held in the interior `quranic:root_001303:B001/m01`; stopping an outlet after filling `quranic:root_001303:B004/m01`
- Ayah anchors: 43:17 `بُشِّرَ`, `وَجْهُهُۥ`, `مُسْوَدًّا`, `كَظِيمٌ`
- Synthesis: Affect is written onto and beneath the body at once. The news changes the skin's visible color, while the sealed-outlet image makes suppressed grief an internal pressure whose expression has been physically closed.

### S2. Truth Forced through a Status Gate (P2: 43:29-31)
- Reading type: mixed
- Scene or process: Extended respite ends when stable truth arrives, but the community recasts it as deceptive deflection and demands that revelation be placed according to human rank.
- Active motifs: extended permission to benefit `quranic:root_001395:B007/m01`; truth stable against falsehood `quranic:root_000347:B001/m01`; tightly fitted true speech `quranic:root_000347:B010/m01`; deceptive turning `quranic:root_000682:B002/m01`; placing a thing in its assigned rank `quranic:root_001492:B004/m01`; pedestrian human bearer `quranic:root_000546:B003/m01`; social honor and inviolability `quranic:root_001029:B010/m01`
- Ayah anchors: 43:29 `مَتَّعْتُ`, `جَآءَهُمُ ٱلْحَقُّ`, `رَسُولٌ مُّبِينٌ`; 43:30 `ٱلْحَقُّ`, `سِحْرٌ`; 43:31 `نُزِّلَ`, `ٱلْقُرْءَانُ`, `رَجُلٍ`, `عَظِيمٍ`
- Synthesis: The objection turns revelation into a placement problem: truth is accepted only if it descends into a socially elevated bearer. The pedestrian sense of "man" exposes the artificiality of the gate, while magic names the rhetorical deflection used when truth arrives outside the preferred hierarchy.

### S3. Generation as an Embodied Passage
- Reading type: latent/lexical
- Scene or process: A fetus is gathered and concealed in the womb, emerges covered and hands first into a receiver's hands, and is delivered with postpartum traces.
- Active motifs: womb gathering fetus and blood `quranic:root_001210:B004/m01`; fetus concealed in the abdomen `quranic:root_000266:B007/m01`; membrane covering the emerging child's head and hands `quranic:root_001424:B010/m01`; hands-first presentation `quranic:root_001630:B010/m01`; midwife receiving the child into her hands `quranic:root_001198:B007/m01`; giving birth and releasing the pregnancy `quranic:root_001683:B003/m01`; newborn emergence and postpartum blood `quranic:root_001533:B005/m01`; afterbirth and blood emerging with the child `quranic:root_000822:B006/m01`
- Ayah anchors: 43:3 `قُرْءَٰنًا`; 43:17 `وَجْهُ`; 43:19 `شَهِدُ`, `شَهَٰدَتُ`; 43:21 `قَبْلِ`, `مُسْتَمْسِكُونَ`; 43:23 `قَبْلِ`; 43:31 `قُرْءَانُ`; 43:43 `ٱسْتَمْسِكْ`; 43:45 `قَبْلِ`; 43:70 `جَنَّةَ`; 43:71 `أَنفُسُ`; 43:72 `جَنَّةُ`; 43:81 `وَلَدٌ`; 43:86 `شَهِدَ`
- Synthesis: This reproductive sequence materially pressures the surah's divine-child claims in 43:15-20 and 43:81-82. A generated child is enclosed, covered, physically presented, received, delivered, and accompanied by bodily residue; the dependency chain makes offspring an embodied event within created life, not an attribute of the sovereign Lord of heaven, earth, and throne.

### S4. A Waterskin Made to Hold
- Reading type: latent/lexical
- Scene or process: A hide surface is stripped and tanned in measured doses, its pieces and side panels are sewn into a vessel, and its mouth and weak points are closed against leakage.
- Active motifs: stripping the outer hide surface `quranic:root_000120:B004/m01`; acacia bark and leaves used for tanning `quranic:root_000737:B008/m01`; a small measured dose of tanning material `quranic:root_001533:B007/m01`; sewing hide to hide or joining waterskin halves `quranic:root_000121:B006/m01`; hide side panel of a waterskin `quranic:root_001536:B002/m01`; skin made to hold its contents `quranic:root_001424:B005/m01`; cord tying the vessel's mouth `quranic:root_001678:B001/m01`; thin hole where water leaks or is stopped `quranic:root_001069:B007/m01`
- Ayah anchors: 43:17 `بُشِّرَ`; 43:21 `مُسْتَمْسِكُونَ`; 43:34 `يَتَّكِـُٔ`; 43:39 `يَنفَعَ`; 43:43 `ٱسْتَمْسِكْ`; 43:51 `تُبْصِرُ`; 43:69 `مُسْلِمِينَ`; 43:71 `أَعْيُنُ`, `أَنفُسُ`; 43:89 `سَلَٰمٌ`
- Synthesis: The craft reframes repeated holding at 43:21 and 43:43 as made reliability: stripping, tanning, joining, tying, and sealing turn a surface into dependable containment. Against the ornamental roofs, doors, couches, and gold of 43:33-35, value is tested by whether worked material preserves water; the activation therefore materializes sustaining provision rather than display.

### S5. Calling Down Milk by Hand
- Reading type: latent/lexical
- Scene or process: An udder is protected, accumulated milk is released by touch and fingertip work, a portion is retained to summon the next yield, and milk returns in successive flows.
- Active motifs: bag tied around a goat's udder `quranic:root_000011:B012/m01`; overnight accumulation and morning milking of a kneeling camel `quranic:root_000109:B007/m01`; rubbing the udder to let down milk `quranic:root_001416:B001/m01`; milk retained to call forth the next yield `quranic:root_000478:B003/m01`; fingertip milking `quranic:root_001165:B005/m01`; milk returning between milkings `quranic:root_001188:B006/m01`; recurrent milk and successive flow `quranic:root_000563:B006/m01`
- Ayah anchors: 43:6 `أَرْسَلْ`; 43:22-23 `ءَاثَٰرِ`; 43:23 `أَرْسَلْ`; 43:24 `أُرْسِلْ`; 43:27 `فَطَرَ`; 43:29 `رَسُولٌ`; 43:32 `فَوْقَ`; 43:45 `أَرْسَلْ`, `رُّسُلِ`; 43:46 `أَرْسَلْ`, `رَسُولُ`; 43:49 `ٱدْعُ`; 43:61 `تَمْتَرُ`; 43:80 `رُسُلُ`; 43:85 `تَبَارَكَ`; 43:86 `يَدْعُ`
- Synthesis: The scene materializes the cattle gift of 43:12-13 and God's apportioning of livelihood in 43:32 as managed, delayed yield. Milk depends on protection, touch, restraint, recurrence, and timing; provision is not passive possession, sharpening the command to remember the giver rather than merely ride or own the animal.

### S6. The Lot Vessel and the Withholding Player
- Reading type: latent/lexical
- Scene or process: A leather vessel gathers the named arrows of a maysir game while one member of the social circle withholds participation.
- Active motifs: leather vessel gathering gaming arrows `quranic:root_000532:B010/m01`; sixth maysir arrow `quranic:root_000867:B011/m01`; fifth maysir arrow `quranic:root_001533:B016/m01`; player refusing to join the maysir circle `quranic:root_000110:B003/m01`
- Ayah anchors: 43:5 `صَفْحًا`; 43:13-14 `رَبِّ`; 43:32 `رَبِّ`; 43:35 `رَبِّ`; 43:46 `رَبِّ`; 43:49 `رَبَّ`; 43:64 `رَبِّ`, `رَبُّ`; 43:71 `أَنفُسُ`; 43:77 `رَبُّ`; 43:79 `أَبْرَمُ`, `مُبْرِمُونَ`; 43:82 `رَبِّ`; 43:88 `رَبِّ`; 43:89 `ٱصْفَحْ`
- Synthesis: The activation reframes human allotment as a game mechanism: named pieces are gathered in a container while participation can be withheld. Set beside God's actual division of livelihood in 43:32, the adversaries' resolved plotting in 43:79, and play under an appointed day in 43:83, chance-allocation becomes a concrete countermodel of sovereignty: humans arrange and refuse the game but do not control the appointed outcome.

### S7. The Timbered Wellhead and Raised Bucket
- Reading type: latent/lexical
- Scene or process: Water is held beneath a timbered well mouth where upright gear, a long rope, and a balanced handled bucket coordinate the drawer and receiver.
- Active motifs: firm well ground holding water `quranic:root_001424:B004/m01`; timber lining and the water-drawer's station at the well mouth `quranic:root_001000:B004/m01`; upright pulley fitting at a well `quranic:root_001273:B012/m01`; long bucket rope `quranic:root_000796:B002/m02`; elongated one-handled water carrier's bucket `quranic:root_000737:B011/m01`; bucket handle or crosspiece balancing the load `quranic:root_000741:B008/m01`; receiver taking the raised bucket into hand `quranic:root_001198:B007/m02`
- Ayah anchors: 43:5 `قَوْمًا`; 43:21 `قَبْلِ`, `مُسْتَمْسِكُونَ`; 43:23 `قَبْلِ`; 43:26 `قَوْمِ`; 43:36 `شَيْطَٰنًا`; 43:40 `تُسْمِعُ`; 43:43 `مُّسْتَقِيمٍ`, `ٱسْتَمْسِكْ`; 43:45 `قَبْلِ`; 43:51 `قَوْمِ`; 43:54 `قَوْمَ`, `قَوْمًا`; 43:57 `قَوْمُ`; 43:58 `قَوْمٌ`; 43:61 `مُّسْتَقِيمٌ`; 43:62 `شَّيْطَٰنُ`; 43:64 `مُّسْتَقِيمٌ`; 43:69 `مُسْلِمِينَ`; 43:80 `نَسْمَعُ`; 43:82 `عَرْشِ`; 43:88 `قَوْمٌ`; 43:89 `سَلَٰمٌ`
- Synthesis: The apparatus materializes the surah's water-and-rule contrast: access requires a holding site, supports, upright gear, rope, a balanced handle, and coordinated hands. It usefully pressures Pharaoh's boast that rivers run beneath him in 43:51 by exposing visible flow as dependent on structure and labor, while the throne-root at 43:82 lends sovereignty a functional resonance of ordered support above provision rather than ornamental display.

### S8. A Grave Rite That Multiplies Death
- Reading type: latent/lexical
- Scene or process: A dead person is carried, wrapped, concealed in a grave understood as a house, while a camel is bound at the owner's grave without food or water until it too dies.
- Active motifs: loss of life `quranic:root_001454:B001/m01`; bier or carrier for the dead `quranic:root_000067:B008/m01`; wrapping the dead in shrouds `quranic:root_000468:B005/m01`; concealing the dead in grave and shroud `quranic:root_000266:B009/m01`; grave as the dead person's house `quranic:root_000166:B007/m01`; grave camel tethered without food or water until death `quranic:root_000154:B006/m01`
- Ayah anchors: 43:6,8 `أَوَّلِينَ`; 43:11 `مَّيْتًا`; 43:32 `دَرَجَٰتٍ`; 43:33-34 `بُيُوتِ`; 43:70 `جَنَّةَ`; 43:72 `جَنَّةُ`; 43:81 `أَوَّلُ`; surface anchor unavailable for the grave-camel motif (root `ب ل ي`)
- Synthesis: The rite reframes the inherited track of 43:21-25 and the luxury houses of 43:33-35 through a customary sequence that carries, wraps, houses, and then adds an animal's death to the owner's. Its activation usefully pressures ancestral continuity: ritual repetition can reproduce death but cannot produce return, whereas 43:11 locates revival with the one who sends water and brings dead land forth.

### S9. A Fully Drawn Shot That Falls Harmless
- Reading type: latent/lexical
- Scene or process: An archer reaches to a coupled quiver, seats and binds an arrow, aims and draws an overstrained bow fully, yet the projectile veers away without a scratch.
- Active motifs: hand returning to the quiver for an arrow `quranic:root_000544:B010/m01`; quiver coupled to the bow `quranic:root_001221:B007/m01`; arrow notch receiving the string `quranic:root_001188:B009/m01`; binding loop joining bowstring or arrow feathers `quranic:root_001303:B006/m01`; directing the projectile toward its target `quranic:root_000053:B012/m01`; drawing the bow to its furthest extent `quranic:root_001080:B004/m01`; overstrained bow clinging to its string near rupture `quranic:root_000156:B005/m01`; arrow veering and falling without scratching `quranic:root_001464:B005/m01`
- Ayah anchors: 43:4 `أُمِّ`; 43:6-7 `نَّبِىٍّ`; 43:13 `مُقْرِنِينَ`; 43:16 `بَنَاتٍ`, `بَنِينَ`; 43:17 `كَظِيمٌ`; 43:22-23 `أُمَّةٍ`; 43:28 `يَرْجِعُ`; 43:32 `فَوْقَ`; 43:33 `أُمَّةً`; 43:36 `قَرِينٌ`; 43:38 `قَرِينُ`; 43:48 `يَرْجِعُ`; 43:53 `مُقْتَرِنِينَ`; 43:55 `أَغْرَقْ`; 43:57 `ٱبْنُ`; 43:59 `بَنِىٓ`; 43:85 `تُرْجَعُ`
- Synthesis: The mechanism materializes apparent force as conditional and fallible: retrieval, coupling, notching, binding, aim, and maximum draw still do not secure effect. The harmless fall usefully pressures Pharaoh's spectacle and drowning reversal in 43:51-56 and the opponents' sealed plot in 43:79-80; tension, intent, and equipment cannot guarantee an outcome.

### S10. The Body Turns toward Its Deity (P1-P5; Shared Invariant and Contrast)
- Reading type: mixed
- Scene or process: A worshipper identifies the one treated as deity, aligns face and prayer direction, yields bodily, and performs voluntary glorifying prayer.
- Active motifs: deity or object made into a deity `quranic:root_000047:B001/m01`; prayer and worship through glorification `quranic:root_000666:B001/m01`; voluntary act beyond obligation `quranic:root_000956:B005/m01`; prayer direction or qibla `quranic:root_001198:B005/m01`; submissive bodily yielding `quranic:root_001332:B004/m01`; face, direction, and destination `quranic:root_001630:B002/m01`
- Ayah anchors: 43:5 `كُن`; 43:13 `سُبْحَٰنَ`; 43:17 `وَجْهُ`; 43:21,23 `قَبْلِ`; 43:45 `ءَالِهَةً`, `قَبْلِ`; 43:54 `أَطَاعُ`; 43:58 `أَٰلِهَتُ`; 43:63 `ٱللَّهَ`, `أَطِيعُ`; 43:64 `ٱللَّهَ`; 43:69 `كَانُ`; 43:81 `كَانَ`; 43:82 `سُبْحَٰنَ`; 43:84 `إِلَٰهٌ`; 43:87 `ٱللَّهُ`
- Synthesis: The bridge across P1 (43:13-20), P2 (43:21-28), P3 (43:45-54), P4 (43:58-69), and P5 (43:81-87) is a shared invariant of directed submission, sharpened by the contrast between voluntary worship and Pharaoh's elicited obedience. Deity, qibla, face, bodily yielding, and voluntary glorification form one oriented act, materializing the surah's correction of allegiance as the alignment of body and will rather than a proposition alone.

### S11. Negotiation Descends to Combat, Then Peace Interrupts It (P1-P5; Causal Sequence and Reversal)
- Reading type: mixed
- Scene or process: Negotiators harden into standing opponents, descend to a duel, grapple and exchange weapon blows, and then transmit a peace greeting that reverses the escalation.
- Active motifs: negotiation over an affair `quranic:root_001272:B009/m01`; standing against another in contest `quranic:root_001273:B014/m01`; descending together for combat `quranic:root_001492:B007/m01`; grappling hold that restrains an opponent `quranic:root_000018:B011/m01`; fighting with swords or sticks while holding ground `quranic:root_000148:B011/m01`; conveying a formula of peace `quranic:root_001211:B006/m01`
- Ayah anchors: 43:3 `قُرْءَٰنًا`; 43:11 `بَلْدَةً`, `نَزَّلَ`; 43:16 `ٱتَّخَذَ`; 43:20 `قَالُ`; 43:22-24 `قَالُ`, `قَالَ`, `قَٰلَ`; 43:26 `قَالَ`, `قَوْمِ`; 43:31 `قُرْءَانُ`, `قَالُ`, `نُزِّلَ`; 43:32 `يَتَّخِذَ`; 43:38 `قَالَ`; 43:43-44 `مُّسْتَقِيمٍ`, `قَوْمِ`; 43:46 `قَالَ`; 43:48 `أَخَذْ`; 43:49 `قَالُ`; 43:51 `قَالَ`, `قَوْمِ`; 43:54 `قَوْمَ`, `قَوْمًا`; 43:57-58 `قَوْمُ`, `قَوْمٌ`, `قَالُ`; 43:61,64 `مُّسْتَقِيمٌ`; 43:63 `قَالَ`; 43:77 `قَالَ`; 43:81 `قُلْ`; 43:87 `يَقُولُ`; 43:88 `قِيلِ`, `قَوْمٌ`; 43:89 `قُلْ`
- Synthesis: The bridge across P1 (claims and warnings), P2 (messengers negotiating with inherited positions), P3 (Moses confronting Pharaoh), P4 (the contested example and factional dispute), and P5 (the resolved plot and final release) is causal escalation followed by reversal. Speech becomes standing opposition, descent, restraint, and weapon exchange; the transmitted peace formula breaks that sequence before reciprocity completes it, giving 43:89's peace the structural force of refusing the combat script prepared by the preceding disputes.

### S12. A Stone Pot Worked through Heat
- Reading type: latent/lexical
- Scene or process: A pot-maker carves a stone cooking vessel, a cook tends its contents in an upright cauldron, and a folded cloth lowers or removes the hot pot without burning the hand.
- Active motifs: carved stone cooking pot and its maker `quranic:root_000110:B006/m01`; cloth for lowering a pot from fire and guarding against heat `quranic:root_000248:B007/m01`; upright cauldron standing as if on a leg `quranic:root_000546:B016/m01`; cooking pot, broth, and the cook attending slaughter and cooking `quranic:root_001205:B007/m01`
- Ayah anchors: 43:3 `جَعَلْ`; 43:10 `جَعَلَ`, `جَعَلَ`; 43:11 `قَدَرٍ`; 43:12 `جَعَلَ`; 43:15,19 `جَعَلُ`; 43:28 `جَعَلَ`; 43:31 `رَجُلٍ`; 43:33 `جَعَلْ`; 43:42 `مُّقْتَدِرُونَ`; 43:45,56,59-60 `جَعَلْ`; 43:79 `أَبْرَمُ`, `مُبْرِمُونَ`
- Synthesis: The worked apparatus materializes both apportioned livelihood in 43:32 and the feast of 43:70-73 as skilled provision. An earthly meal passes through carving, slaughter, cooking, a stable vessel, and protection from heat; the circulating vessels of the inherited garden therefore signify not display alone but provision freed from this chain of labor and hazard.

### S13. A Fire Banked, Stirred, and Fed
- Reading type: latent/lexical
- Scene or process: A fire-bed is excavated and covered so fuel remains alive, its embers are stirred back into ignition, wood is fed to it, and the resulting blaze roars.
- Active motifs: banking fuel in earth to preserve a fire `quranic:root_001424:B008/m01`; stirring embers until they ignite `quranic:root_001639:B005/m01`; feeding wood to a consuming fire `quranic:root_000043:B005/m01`; roar and flame of a fire `quranic:root_001434:B001/m01`
- Ayah anchors: 43:21 `مُسْتَمْسِكُونَ`; 43:43 `ٱسْتَمْسِكْ`; 43:72 `أُورِثْ`; 43:73 `تَأْكُلُ`; surface anchor unavailable for the roaring-fire motif (root `م ع ع`)
- Synthesis: The maintenance sequence materializes the unrelieved punishment of 43:74-78. Fire persists because it is preserved, reopened, supplied, and brought to audible force; the refusal to slacken is thus rendered as a continuous operation rather than a static backdrop.

### S14. A Food-Dependent Body Fails and Is Treated
- Reading type: latent/lexical
- Scene or process: A creature must take food to sustain its belly, hidden corruption enters body or food, the failed intake returns as waste and diarrhea, and cleansing plus an astringent remedy restores retention while a remnant preserves life.
- Active motifs: embodied creature whose belly requires food `quranic:root_000682:B003/m01`; hidden defect in the body, belly, or food `quranic:root_000464:B004/m01`; returned bodily matter and diarrhea `quranic:root_000544:B015/m01`; excretion, cleansing, and administration of medicine `quranic:root_001476:B006/m01`; food or medicine that arrests diarrhea `quranic:root_001036:B006/m01`; remnant of food, drink, or strength that keeps one alive `quranic:root_001424:B003/m01`
- Ayah anchors: 43:3 `تَعْقِلُ`; 43:21 `مُسْتَمْسِكُونَ`; 43:28 `يَرْجِعُ`; 43:30 `سِحْرٌ`; 43:43 `ٱسْتَمْسِكْ`; 43:48 `يَرْجِعُ`; 43:49 `سَّاحِرُ`; 43:70 `ٱدْخُلُ`; 43:80 `نَجْوَىٰ`; 43:85 `تُرْجَعُ`
- Synthesis: This dependency chain usefully pressures the divine-child and rival-deity claims of 43:15-20, 43:59-64, and 43:81-84. A body that needs intake, produces waste, loses retention, and requires treatment belongs to dependent created life; embodied servanthood can be favored, but it cannot be converted into divine genealogy or sovereignty.

### S15. Familiar Talk Corrodes Its Own Bond
- Reading type: latent/lexical
- Scene or process: Kin and companions begin within an existing bond, exchange witty familiar talk, let a saying circulate through the group, and encounter a talebearer whose instigation corrupts the relation.
- Active motifs: social bond connecting persons `quranic:root_000170:B003/m01`; close kinship and its maintenance or severance `quranic:root_000552:B002/m01`; witty banter among familiar companions `quranic:root_001174:B003/m01`; favorable or hostile saying circulating among people `quranic:root_001272:B007/m01`; talebearing that incites people and corrupts their relations `quranic:root_000043:B009/m01`
- Ayah anchors: 43:2 `مُبِينِ`; 43:9 `يَقُولُ`; 43:13 `تَقُولُ`; 43:15 `مُّبِينٌ`; 43:17 `رَّحْمَٰنِ`; 43:18 `مُبِينٍ`; 43:19 `رَّحْمَٰنِ`; 43:20 `رَّحْمَٰنُ`, `قَالُ`; 43:22 `قَالُ`; 43:23 `قَالَ`; 43:24 `قَٰلَ`, `قَالُ`; 43:26 `قَالَ`; 43:29 `مُّبِينٌ`; 43:30-31 `قَالُ`; 43:32 `بَيْنَ`, `رَحْمَتَ`, `رَحْمَتُ`; 43:33,36 `رَّحْمَٰنِ`; 43:38 `بَيْنِ`, `بَيْنَ`, `قَالَ`; 43:40 `مُّبِينٍ`; 43:45 `رَّحْمَٰنِ`; 43:46 `قَالَ`; 43:49 `قَالُ`; 43:51 `قَالَ`; 43:52 `يُبِينُ`; 43:58 `قَالُ`; 43:62 `مُّبِينٌ`; 43:63 `بَيِّنَٰتِ`, `أُبَيِّنَ`, `قَالَ`; 43:65 `بَيْنِ`; 43:73 `تَأْكُلُ`, `فَٰكِهَةٌ`; 43:77 `قَالَ`; 43:81 `رَّحْمَٰنِ`, `قُلْ`; 43:85 `بَيْنَ`; 43:87 `يَقُولُ`; 43:88 `قِيلِ`; 43:89 `قُلْ`
- Synthesis: The causal social scene materializes the clamor around the example in 43:57-58 and the reversal of intimates into enemies in 43:67. Pleasant exchange does not itself secure relation: once speech becomes circulating reputation and targeted instigation, the same network that carried familiarity carries corrosion through the bond.

### S16. Wear Opens a Garment, Repair Closes It
- Reading type: latent/lexical
- Scene or process: Use strips a garment's surface and wears it thin, yarn breaks or cloth tears, and the damaged place is patched so the object can return to service.
- Active motifs: object or garment worn out through use `quranic:root_000154:B001/m01`; garment torn and stripped of its nap by wear `quranic:root_000434:B009/m01`; broken yarn and cloth torn apart `quranic:root_001428:B006/m01`; repair at the garment's worn place `quranic:root_000433:B007/m01`
- Ayah anchors: 43:9 `خَلَقَ`, `خَلَقَ`; 43:12 `خَلَقَ`; 43:16 `يَخْلُقُ`; 43:19 `خَلْقَ`; 43:51 `مِصْرَ`; 43:60 `يَخْلُفُ`; 43:63 `تَخْتَلِفُ`; 43:65 `ٱخْتَلَفَ`; 43:87 `خَلَقَ`; surface anchor unavailable for wear through use (root `ب ل ي`)
- Synthesis: The wear-and-repair cycle materializes the limited horizon assigned to roofs, doors, couches, gold, and ornament in 43:33-35. Utility consumes its own surface and periodically exposes structure; worldly furnishing can be serviceable and repaired, but it cannot supply the protected permanence reserved for the later outcome.

### S17. Installments Open a Legal Exit from Bondage
- Reading type: latent/lexical
- Scene or process: An enslaved person and owner enter an agreement, write scheduled payments toward emancipation, attach liability and warranty to the transaction, and retain substitute security until the price is discharged.
- Active motifs: mutual covenant over an affair `quranic:root_000055:B005/m01`; right or claim that remains attached as liability `quranic:root_000175:B006/m01`; substitute security and retention pending payment `quranic:root_001033:B010/m01`; written transaction warranty and recourse for defect `quranic:root_001055:B006/m01`; installment manumission contract leading to release `quranic:root_001283:B005/m01`
- Ayah anchors: 43:2,4 `كِتَٰبِ`; 43:19 `تُكْتَبُ`; 43:21 `كِتَٰبًا`; 43:25 `عَٰقِبَةُ`; 43:28 `عَقِبِ`; 43:49 `عَهِدَ`; 43:61 `ٱتَّبِعُ`; 43:80 `يَكْتُبُ`; surface anchor unavailable for the mutual-agreement motif (root `ء م ه`)
- Synthesis: The contract materializes human bondage as a legal and economic status with a written route toward release. That mutability usefully pressures the projection of human ownership into divine kinship at 43:15 and 43:81, while sharpening 43:32: worldly ranks can bind persons through payment, liability, and title, but they do not define the sovereign relation between creator and servant.

### S18. A Herd Queued and Returned to Water
- Reading type: latent/lexical
- Scene or process: Camels approach in a following file behind a lead animal, pass the trough in order, drink directly at their mouths, return a still-thirsty animal for a second turn, alternate watering periods, and move back to nearby pasture before returning again.
- Active motifs: camels traveling one behind another in a file `quranic:root_000427:B008/m01`; successive herds sent toward pasture or water `quranic:root_000563:B005/m01`; lead she-camel at the front of the watering herd `quranic:root_000733:B004/m01`; passing camels along the trough `quranic:root_000867:B010/m01`; watering directly at the animals' mouths `quranic:root_001198:B014/m01`; returning a thirsty camel for another drink `quranic:root_000464:B007/m01`; alternating morning and evening watering periods `quranic:root_000997:B006/m01`; moving between water and nearby pasture before returning `quranic:root_001486:B006/m01`
- Ayah anchors: 43:5 `صَفْحًا`; 43:6 `أَرْسَلْ`; 43:21 `قَبْلِ`; 43:23 `أَرْسَلْ`, `قَبْلِ`; 43:24 `أُرْسِلْ`; 43:29 `رَسُولٌ`; 43:33 `مَعَارِجَ`; 43:45 `أَرْسَلْ`, `رُّسُلِ`, `قَبْلِ`; 43:46 `أَرْسَلْ`, `رَسُولُ`; 43:51 `نَادَىٰ`; 43:54 `ٱسْتَخَفَّ`; 43:56 `سَلَفًا`; 43:70 `ٱدْخُلُ`; 43:77 `نَادَ`; 43:80 `رُسُلُ`; 43:89 `ٱصْفَحْ`
- Synthesis: The watering routine materializes the cattle and mounts of 43:12-13 and the apportioned livelihood of 43:32 as scheduled access rather than bare possession. Lead position, queue, direct service, repeated turns, and the circuit between pasture and trough show provision operating through ordered care, while remembrance keeps that managed yield tied to its giver.

### S19. A Hidden Hunter Lets Motion Become Capture
- Reading type: latent/lexical
- Scene or process: Hunters go out, conceal themselves in a blind, set a snare for a waterbird, take successive quarry, and inspect a struck animal to determine whether it has died.
- Active motifs: hunter's concealed blind `quranic:root_000099:B007/m01`; white waterbird as quarry `quranic:root_000109:B008/m01`; hunters departing in search of game `quranic:root_000745:B006/m01`; snare in which prey becomes entangled `quranic:root_000791:B006/m01`; successive quarry taken in one release `quranic:root_000993:B008/m01`; inspection to establish whether struck game is dead `quranic:root_001454:B014/m01`
- Ayah anchors: 43:9 `سَّمَٰوَٰتِ`; 43:11 `سَّمَآءِ`, `مَّيْتًا`; 43:26 `بَرَآءٌ`; 43:39 `مُشْتَرِكُونَ`; 43:62,67 `عَدُوٌّ`; 43:82 `سَّمَٰوَٰتِ`; 43:84 `سَّمَآءِ`; 43:85 `تَبَارَكَ`, `سَّمَٰوَٰتِ`
- Synthesis: The covert hunting mechanism usefully reframes the attached companion and obstructed route of 43:36-39. The prey appears to move under its own direction while concealment and a placed snare convert that motion into capture; the surface sharing of punishment at 43:39 gains a same-root pressure in which partnership is also entanglement.

### S20. Service, Sale, and Menstrual Clearance
- Reading type: latent/lexical
- Scene or process: A female servant reaches the threshold at which she is described for service and sale, performs labor, has menstrual signs inspected, and undergoes a waiting procedure intended to establish clearance before sexual access.
- Active motifs: female servant reaching serviceable age and being described in sale `quranic:root_001654:B004/m01`; service and skilled labor performed by servant or slave `quranic:root_001453:B002/m01`; menstrual and purity cycle used as a legal interval `quranic:root_001210:B003/m01`; visible discharge used to distinguish menstruation from purity `quranic:root_000531:B007/m01`; menstrual clearance of an enslaved woman before intercourse `quranic:root_000099:B005/m01`
- Ayah anchors: 43:3,31 `قُرْءَٰنًا`, `قُرْءَانُ`; 43:26 `بَرَآءٌ`; 43:42 `نُرِيَ`; 43:48 `نُرِي`; 43:52 `مَهِينٌ`; 43:82 `يَصِفُ`
- Synthesis: This social procedure materially pressures the gendered valuation exposed in 43:16-19. Female status is not left as an abstract classification: the activation shows a body made legible for labor, sale, reproductive uncertainty, and sexual access. It also sharpens the hierarchy of 43:32 by exposing one coercive human arrangement that cannot be projected onto God as genealogy or used to measure divine favor.


