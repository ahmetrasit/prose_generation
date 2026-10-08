Surah: 40. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S40 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s040/surah.r2/text.md =====
# Surah 40

- 40:1 حمٓ
- 40:2 تَنزِيلُ ٱلْكِتَٰبِ مِنَ ٱللَّهِ ٱلْعَزِيزِ ٱلْعَلِيمِ
- 40:3 غَافِرِ ٱلذَّنۢبِ وَقَابِلِ ٱلتَّوْبِ شَدِيدِ ٱلْعِقَابِ ذِى ٱلطَّوْلِ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ إِلَيْهِ ٱلْمَصِيرُ
- 40:4 مَا يُجَٰدِلُ فِىٓ ءَايَٰتِ ٱللَّهِ إِلَّا ٱلَّذِينَ كَفَرُوا۟ فَلَا يَغْرُرْكَ تَقَلُّبُهُمْ فِى ٱلْبِلَٰدِ
- 40:5 كَذَّبَتْ قَبْلَهُمْ قَوْمُ نُوحٍۢ وَٱلْأَحْزَابُ مِنۢ بَعْدِهِمْ ۖ وَهَمَّتْ كُلُّ أُمَّةٍۭ بِرَسُولِهِمْ لِيَأْخُذُوهُ ۖ وَجَٰدَلُوا۟ بِٱلْبَٰطِلِ لِيُدْحِضُوا۟ بِهِ ٱلْحَقَّ فَأَخَذْتُهُمْ ۖ فَكَيْفَ كَانَ عِقَابِ
- 40:6 وَكَذَٰلِكَ حَقَّتْ كَلِمَتُ رَبِّكَ عَلَى ٱلَّذِينَ كَفَرُوٓا۟ أَنَّهُمْ أَصْحَٰبُ ٱلنَّارِ
- 40:7 ٱلَّذِينَ يَحْمِلُونَ ٱلْعَرْشَ وَمَنْ حَوْلَهُۥ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ وَيُؤْمِنُونَ بِهِۦ وَيَسْتَغْفِرُونَ لِلَّذِينَ ءَامَنُوا۟ رَبَّنَا وَسِعْتَ كُلَّ شَىْءٍۢ رَّحْمَةًۭ وَعِلْمًۭا فَٱغْفِرْ لِلَّذِينَ تَابُوا۟ وَٱتَّبَعُوا۟ سَبِيلَكَ وَقِهِمْ عَذَابَ ٱلْجَحِيمِ
- 40:8 رَبَّنَا وَأَدْخِلْهُمْ جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدتَّهُمْ وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 40:9 وَقِهِمُ ٱلسَّيِّـَٔاتِ ۚ وَمَن تَقِ ٱلسَّيِّـَٔاتِ يَوْمَئِذٍۢ فَقَدْ رَحِمْتَهُۥ ۚ وَذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- 40:10 إِنَّ ٱلَّذِينَ كَفَرُوا۟ يُنَادَوْنَ لَمَقْتُ ٱللَّهِ أَكْبَرُ مِن مَّقْتِكُمْ أَنفُسَكُمْ إِذْ تُدْعَوْنَ إِلَى ٱلْإِيمَٰنِ فَتَكْفُرُونَ
- 40:11 قَالُوا۟ رَبَّنَآ أَمَتَّنَا ٱثْنَتَيْنِ وَأَحْيَيْتَنَا ٱثْنَتَيْنِ فَٱعْتَرَفْنَا بِذُنُوبِنَا فَهَلْ إِلَىٰ خُرُوجٍۢ مِّن سَبِيلٍۢ
- 40:12 ذَٰلِكُم بِأَنَّهُۥٓ إِذَا دُعِىَ ٱللَّهُ وَحْدَهُۥ كَفَرْتُمْ ۖ وَإِن يُشْرَكْ بِهِۦ تُؤْمِنُوا۟ ۚ فَٱلْحُكْمُ لِلَّهِ ٱلْعَلِىِّ ٱلْكَبِيرِ
- 40:13 هُوَ ٱلَّذِى يُرِيكُمْ ءَايَٰتِهِۦ وَيُنَزِّلُ لَكُم مِّنَ ٱلسَّمَآءِ رِزْقًۭا ۚ وَمَا يَتَذَكَّرُ إِلَّا مَن يُنِيبُ
- 40:14 فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- 40:15 رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ
- 40:16 يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ ۚ لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
- 40:17 ٱلْيَوْمَ تُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ ۚ لَا ظُلْمَ ٱلْيَوْمَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- 40:18 وَأَنذِرْهُمْ يَوْمَ ٱلْءَازِفَةِ إِذِ ٱلْقُلُوبُ لَدَى ٱلْحَنَاجِرِ كَٰظِمِينَ ۚ مَا لِلظَّٰلِمِينَ مِنْ حَمِيمٍۢ وَلَا شَفِيعٍۢ يُطَاعُ
- 40:19 يَعْلَمُ خَآئِنَةَ ٱلْأَعْيُنِ وَمَا تُخْفِى ٱلصُّدُورُ
- 40:20 وَٱللَّهُ يَقْضِى بِٱلْحَقِّ ۖ وَٱلَّذِينَ يَدْعُونَ مِن دُونِهِۦ لَا يَقْضُونَ بِشَىْءٍ ۗ إِنَّ ٱللَّهَ هُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- 40:21 ۞ أَوَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ كَانُوا۟ مِن قَبْلِهِمْ ۚ كَانُوا۟ هُمْ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَأَخَذَهُمُ ٱللَّهُ بِذُنُوبِهِمْ وَمَا كَانَ لَهُم مِّنَ ٱللَّهِ مِن وَاقٍۢ
- 40:22 ذَٰلِكَ بِأَنَّهُمْ كَانَت تَّأْتِيهِمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَكَفَرُوا۟ فَأَخَذَهُمُ ٱللَّهُ ۚ إِنَّهُۥ قَوِىٌّۭ شَدِيدُ ٱلْعِقَابِ
- 40:23 وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَا وَسُلْطَٰنٍۢ مُّبِينٍ
- 40:24 إِلَىٰ فِرْعَوْنَ وَهَٰمَٰنَ وَقَٰرُونَ فَقَالُوا۟ سَٰحِرٌۭ كَذَّابٌۭ
- 40:25 فَلَمَّا جَآءَهُم بِٱلْحَقِّ مِنْ عِندِنَا قَالُوا۟ ٱقْتُلُوٓا۟ أَبْنَآءَ ٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ وَٱسْتَحْيُوا۟ نِسَآءَهُمْ ۚ وَمَا كَيْدُ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍۢ
- 40:26 وَقَالَ فِرْعَوْنُ ذَرُونِىٓ أَقْتُلْ مُوسَىٰ وَلْيَدْعُ رَبَّهُۥٓ ۖ إِنِّىٓ أَخَافُ أَن يُبَدِّلَ دِينَكُمْ أَوْ أَن يُظْهِرَ فِى ٱلْأَرْضِ ٱلْفَسَادَ
- 40:27 وَقَالَ مُوسَىٰٓ إِنِّى عُذْتُ بِرَبِّى وَرَبِّكُم مِّن كُلِّ مُتَكَبِّرٍۢ لَّا يُؤْمِنُ بِيَوْمِ ٱلْحِسَابِ
- 40:28 وَقَالَ رَجُلٌۭ مُّؤْمِنٌۭ مِّنْ ءَالِ فِرْعَوْنَ يَكْتُمُ إِيمَٰنَهُۥٓ أَتَقْتُلُونَ رَجُلًا أَن يَقُولَ رَبِّىَ ٱللَّهُ وَقَدْ جَآءَكُم بِٱلْبَيِّنَٰتِ مِن رَّبِّكُمْ ۖ وَإِن يَكُ كَٰذِبًۭا فَعَلَيْهِ كَذِبُهُۥ ۖ وَإِن يَكُ صَادِقًۭا يُصِبْكُم بَعْضُ ٱلَّذِى يَعِدُكُمْ ۖ إِنَّ ٱللَّهَ لَا يَهْدِى مَنْ هُوَ مُسْرِفٌۭ كَذَّابٌۭ
- 40:29 يَٰقَوْمِ لَكُمُ ٱلْمُلْكُ ٱلْيَوْمَ ظَٰهِرِينَ فِى ٱلْأَرْضِ فَمَن يَنصُرُنَا مِنۢ بَأْسِ ٱللَّهِ إِن جَآءَنَا ۚ قَالَ فِرْعَوْنُ مَآ أُرِيكُمْ إِلَّا مَآ أَرَىٰ وَمَآ أَهْدِيكُمْ إِلَّا سَبِيلَ ٱلرَّشَادِ
- 40:30 وَقَالَ ٱلَّذِىٓ ءَامَنَ يَٰقَوْمِ إِنِّىٓ أَخَافُ عَلَيْكُم مِّثْلَ يَوْمِ ٱلْأَحْزَابِ
- 40:31 مِثْلَ دَأْبِ قَوْمِ نُوحٍۢ وَعَادٍۢ وَثَمُودَ وَٱلَّذِينَ مِنۢ بَعْدِهِمْ ۚ وَمَا ٱللَّهُ يُرِيدُ ظُلْمًۭا لِّلْعِبَادِ
- 40:32 وَيَٰقَوْمِ إِنِّىٓ أَخَافُ عَلَيْكُمْ يَوْمَ ٱلتَّنَادِ
- 40:33 يَوْمَ تُوَلُّونَ مُدْبِرِينَ مَا لَكُم مِّنَ ٱللَّهِ مِنْ عَاصِمٍۢ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- 40:34 وَلَقَدْ جَآءَكُمْ يُوسُفُ مِن قَبْلُ بِٱلْبَيِّنَٰتِ فَمَا زِلْتُمْ فِى شَكٍّۢ مِّمَّا جَآءَكُم بِهِۦ ۖ حَتَّىٰٓ إِذَا هَلَكَ قُلْتُمْ لَن يَبْعَثَ ٱللَّهُ مِنۢ بَعْدِهِۦ رَسُولًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَنْ هُوَ مُسْرِفٌۭ مُّرْتَابٌ
- 40:35 ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِ ٱللَّهِ بِغَيْرِ سُلْطَٰنٍ أَتَىٰهُمْ ۖ كَبُرَ مَقْتًا عِندَ ٱللَّهِ وَعِندَ ٱلَّذِينَ ءَامَنُوا۟ ۚ كَذَٰلِكَ يَطْبَعُ ٱللَّهُ عَلَىٰ كُلِّ قَلْبِ مُتَكَبِّرٍۢ جَبَّارٍۢ
- 40:36 وَقَالَ فِرْعَوْنُ يَٰهَٰمَٰنُ ٱبْنِ لِى صَرْحًۭا لَّعَلِّىٓ أَبْلُغُ ٱلْأَسْبَٰبَ
- 40:37 أَسْبَٰبَ ٱلسَّمَٰوَٰتِ فَأَطَّلِعَ إِلَىٰٓ إِلَٰهِ مُوسَىٰ وَإِنِّى لَأَظُنُّهُۥ كَٰذِبًۭا ۚ وَكَذَٰلِكَ زُيِّنَ لِفِرْعَوْنَ سُوٓءُ عَمَلِهِۦ وَصُدَّ عَنِ ٱلسَّبِيلِ ۚ وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ
- 40:38 وَقَالَ ٱلَّذِىٓ ءَامَنَ يَٰقَوْمِ ٱتَّبِعُونِ أَهْدِكُمْ سَبِيلَ ٱلرَّشَادِ
- 40:39 يَٰقَوْمِ إِنَّمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَا مَتَٰعٌۭ وَإِنَّ ٱلْءَاخِرَةَ هِىَ دَارُ ٱلْقَرَارِ
- 40:40 مَنْ عَمِلَ سَيِّئَةًۭ فَلَا يُجْزَىٰٓ إِلَّا مِثْلَهَا ۖ وَمَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ يُرْزَقُونَ فِيهَا بِغَيْرِ حِسَابٍۢ
- 40:41 ۞ وَيَٰقَوْمِ مَا لِىٓ أَدْعُوكُمْ إِلَى ٱلنَّجَوٰةِ وَتَدْعُونَنِىٓ إِلَى ٱلنَّارِ
- 40:42 تَدْعُونَنِى لِأَكْفُرَ بِٱللَّهِ وَأُشْرِكَ بِهِۦ مَا لَيْسَ لِى بِهِۦ عِلْمٌۭ وَأَنَا۠ أَدْعُوكُمْ إِلَى ٱلْعَزِيزِ ٱلْغَفَّٰرِ
- 40:43 لَا جَرَمَ أَنَّمَا تَدْعُونَنِىٓ إِلَيْهِ لَيْسَ لَهُۥ دَعْوَةٌۭ فِى ٱلدُّنْيَا وَلَا فِى ٱلْءَاخِرَةِ وَأَنَّ مَرَدَّنَآ إِلَى ٱللَّهِ وَأَنَّ ٱلْمُسْرِفِينَ هُمْ أَصْحَٰبُ ٱلنَّارِ
- 40:44 فَسَتَذْكُرُونَ مَآ أَقُولُ لَكُمْ ۚ وَأُفَوِّضُ أَمْرِىٓ إِلَى ٱللَّهِ ۚ إِنَّ ٱللَّهَ بَصِيرٌۢ بِٱلْعِبَادِ
- 40:45 فَوَقَىٰهُ ٱللَّهُ سَيِّـَٔاتِ مَا مَكَرُوا۟ ۖ وَحَاقَ بِـَٔالِ فِرْعَوْنَ سُوٓءُ ٱلْعَذَابِ
- 40:46 ٱلنَّارُ يُعْرَضُونَ عَلَيْهَا غُدُوًّۭا وَعَشِيًّۭا ۖ وَيَوْمَ تَقُومُ ٱلسَّاعَةُ أَدْخِلُوٓا۟ ءَالَ فِرْعَوْنَ أَشَدَّ ٱلْعَذَابِ
- 40:47 وَإِذْ يَتَحَآجُّونَ فِى ٱلنَّارِ فَيَقُولُ ٱلضُّعَفَٰٓؤُا۟ لِلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُنَّا لَكُمْ تَبَعًۭا فَهَلْ أَنتُم مُّغْنُونَ عَنَّا نَصِيبًۭا مِّنَ ٱلنَّارِ
- 40:48 قَالَ ٱلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُلٌّۭ فِيهَآ إِنَّ ٱللَّهَ قَدْ حَكَمَ بَيْنَ ٱلْعِبَادِ
- 40:49 وَقَالَ ٱلَّذِينَ فِى ٱلنَّارِ لِخَزَنَةِ جَهَنَّمَ ٱدْعُوا۟ رَبَّكُمْ يُخَفِّفْ عَنَّا يَوْمًۭا مِّنَ ٱلْعَذَابِ
- 40:50 قَالُوٓا۟ أَوَلَمْ تَكُ تَأْتِيكُمْ رُسُلُكُم بِٱلْبَيِّنَٰتِ ۖ قَالُوا۟ بَلَىٰ ۚ قَالُوا۟ فَٱدْعُوا۟ ۗ وَمَا دُعَٰٓؤُا۟ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍ
- 40:51 إِنَّا لَنَنصُرُ رُسُلَنَا وَٱلَّذِينَ ءَامَنُوا۟ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَيَوْمَ يَقُومُ ٱلْأَشْهَٰدُ
- 40:52 يَوْمَ لَا يَنفَعُ ٱلظَّٰلِمِينَ مَعْذِرَتُهُمْ ۖ وَلَهُمُ ٱللَّعْنَةُ وَلَهُمْ سُوٓءُ ٱلدَّارِ
- 40:53 وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْهُدَىٰ وَأَوْرَثْنَا بَنِىٓ إِسْرَٰٓءِيلَ ٱلْكِتَٰبَ
- 40:54 هُدًۭى وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- 40:55 فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَسَبِّحْ بِحَمْدِ رَبِّكَ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
- 40:56 إِنَّ ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِ ٱللَّهِ بِغَيْرِ سُلْطَٰنٍ أَتَىٰهُمْ ۙ إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ مَّا هُم بِبَٰلِغِيهِ ۚ فَٱسْتَعِذْ بِٱللَّهِ ۖ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- 40:57 لَخَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ أَكْبَرُ مِنْ خَلْقِ ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- 40:58 وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَلَا ٱلْمُسِىٓءُ ۚ قَلِيلًۭا مَّا تَتَذَكَّرُونَ
- 40:59 إِنَّ ٱلسَّاعَةَ لَءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- 40:60 وَقَالَ رَبُّكُمُ ٱدْعُونِىٓ أَسْتَجِبْ لَكُمْ ۚ إِنَّ ٱلَّذِينَ يَسْتَكْبِرُونَ عَنْ عِبَادَتِى سَيَدْخُلُونَ جَهَنَّمَ دَاخِرِينَ
- 40:61 ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلَّيْلَ لِتَسْكُنُوا۟ فِيهِ وَٱلنَّهَارَ مُبْصِرًا ۚ إِنَّ ٱللَّهَ لَذُو فَضْلٍ عَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- 40:62 ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ خَٰلِقُ كُلِّ شَىْءٍۢ لَّآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- 40:63 كَذَٰلِكَ يُؤْفَكُ ٱلَّذِينَ كَانُوا۟ بِـَٔايَٰتِ ٱللَّهِ يَجْحَدُونَ
- 40:64 ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ قَرَارًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ فَتَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- 40:65 هُوَ ٱلْحَىُّ لَآ إِلَٰهَ إِلَّا هُوَ فَٱدْعُوهُ مُخْلِصِينَ لَهُ ٱلدِّينَ ۗ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 40:66 ۞ قُلْ إِنِّى نُهِيتُ أَنْ أَعْبُدَ ٱلَّذِينَ تَدْعُونَ مِن دُونِ ٱللَّهِ لَمَّا جَآءَنِىَ ٱلْبَيِّنَٰتُ مِن رَّبِّى وَأُمِرْتُ أَنْ أُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- 40:67 هُوَ ٱلَّذِى خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ يُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ثُمَّ لِتَكُونُوا۟ شُيُوخًۭا ۚ وَمِنكُم مَّن يُتَوَفَّىٰ مِن قَبْلُ ۖ وَلِتَبْلُغُوٓا۟ أَجَلًۭا مُّسَمًّۭى وَلَعَلَّكُمْ تَعْقِلُونَ
- 40:68 هُوَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ ۖ فَإِذَا قَضَىٰٓ أَمْرًۭا فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ
- 40:69 أَلَمْ تَرَ إِلَى ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِ ٱللَّهِ أَنَّىٰ يُصْرَفُونَ
- 40:70 ٱلَّذِينَ كَذَّبُوا۟ بِٱلْكِتَٰبِ وَبِمَآ أَرْسَلْنَا بِهِۦ رُسُلَنَا ۖ فَسَوْفَ يَعْلَمُونَ
- 40:71 إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ
- 40:72 فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
- 40:73 ثُمَّ قِيلَ لَهُمْ أَيْنَ مَا كُنتُمْ تُشْرِكُونَ
- 40:74 مِن دُونِ ٱللَّهِ ۖ قَالُوا۟ ضَلُّوا۟ عَنَّا بَل لَّمْ نَكُن نَّدْعُوا۟ مِن قَبْلُ شَيْـًۭٔا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ ٱلْكَٰفِرِينَ
- 40:75 ذَٰلِكُم بِمَا كُنتُمْ تَفْرَحُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَبِمَا كُنتُمْ تَمْرَحُونَ
- 40:76 ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- 40:77 فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۚ فَإِمَّا نُرِيَنَّكَ بَعْضَ ٱلَّذِى نَعِدُهُمْ أَوْ نَتَوَفَّيَنَّكَ فَإِلَيْنَا يُرْجَعُونَ
- 40:78 وَلَقَدْ أَرْسَلْنَا رُسُلًۭا مِّن قَبْلِكَ مِنْهُم مَّن قَصَصْنَا عَلَيْكَ وَمِنْهُم مَّن لَّمْ نَقْصُصْ عَلَيْكَ ۗ وَمَا كَانَ لِرَسُولٍ أَن يَأْتِىَ بِـَٔايَةٍ إِلَّا بِإِذْنِ ٱللَّهِ ۚ فَإِذَا جَآءَ أَمْرُ ٱللَّهِ قُضِىَ بِٱلْحَقِّ وَخَسِرَ هُنَالِكَ ٱلْمُبْطِلُونَ
- 40:79 ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَنْعَٰمَ لِتَرْكَبُوا۟ مِنْهَا وَمِنْهَا تَأْكُلُونَ
- 40:80 وَلَكُمْ فِيهَا مَنَٰفِعُ وَلِتَبْلُغُوا۟ عَلَيْهَا حَاجَةًۭ فِى صُدُورِكُمْ وَعَلَيْهَا وَعَلَى ٱلْفُلْكِ تُحْمَلُونَ
- 40:81 وَيُرِيكُمْ ءَايَٰتِهِۦ فَأَىَّ ءَايَٰتِ ٱللَّهِ تُنكِرُونَ
- 40:82 أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ كَانُوٓا۟ أَكْثَرَ مِنْهُمْ وَأَشَدَّ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ
- 40:83 فَلَمَّا جَآءَتْهُمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَرِحُوا۟ بِمَا عِندَهُم مِّنَ ٱلْعِلْمِ وَحَاقَ بِهِم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- 40:84 فَلَمَّا رَأَوْا۟ بَأْسَنَا قَالُوٓا۟ ءَامَنَّا بِٱللَّهِ وَحْدَهُۥ وَكَفَرْنَا بِمَا كُنَّا بِهِۦ مُشْرِكِينَ
- 40:85 فَلَمْ يَكُ يَنفَعُهُمْ إِيمَٰنُهُمْ لَمَّا رَأَوْا۟ بَأْسَنَا ۖ سُنَّتَ ٱللَّهِ ٱلَّتِى قَدْ خَلَتْ فِى عِبَادِهِۦ ۖ وَخَسِرَ هُنَالِكَ ٱلْكَٰفِرُونَ


===== _commentary/v16/work/s040/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ز ل (root_001492): 40:2 تَنزِيلُ, 40:13 وَيُنَزِّلُ

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

## ك ت ب (root_001283): 40:2 ٱلْكِتَٰبِ, 40:53 ٱلْكِتَٰبَ, 40:70 بِٱلْكِتَٰبِ

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

## ء ل ه (root_000047): 40:2 ٱللَّهِ, 40:3 إِلَٰهَ, 40:4 ٱللَّهِ, 40:10 ٱللَّهِ, 40:12 ٱللَّهُ, 40:12 لِلَّهِ, 40:14 ٱللَّهَ, 40:16 ٱللَّهِ, 40:16 لِلَّهِ, 40:17 ٱللَّهَ, 40:20 وَٱللَّهُ, 40:20 ٱللَّهَ, 40:21 ٱللَّهُ, 40:21 ٱللَّهِ, 40:22 ٱللَّهُ, 40:28 ٱللَّهُ, 40:28 ٱللَّهَ, 40:29 ٱللَّهِ, 40:31 ٱللَّهُ, 40:33 ٱللَّهِ, 40:33 ٱللَّهُ, 40:34 ٱللَّهُ, 40:34 ٱللَّهُ, 40:35 ٱللَّهِ, 40:35 ٱللَّهِ, 40:35 ٱللَّهُ, 40:37 إِلَٰهِ, 40:42 بِٱللَّهِ, 40:43 ٱللَّهِ, 40:44 ٱللَّهِ, 40:44 ٱللَّهَ, 40:45 ٱللَّهُ, 40:48 ٱللَّهَ, 40:55 ٱللَّهِ, 40:56 ٱللَّهِ, 40:56 بِٱللَّهِ, 40:61 ٱللَّهُ, 40:61 ٱللَّهَ, 40:62 ٱللَّهُ, 40:62 إِلَٰهَ, 40:63 ٱللَّهِ, 40:64 ٱللَّهُ, 40:64 ٱللَّهُ, 40:64 ٱللَّهُ, 40:65 إِلَٰهَ, 40:65 لِلَّهِ, 40:66 ٱللَّهِ, 40:69 ٱللَّهِ, 40:74 ٱللَّهِ, 40:74 ٱللَّهُ, 40:77 ٱللَّهِ, 40:78 ٱللَّهِ, 40:78 ٱللَّهِ, 40:79 ٱللَّهُ, 40:81 ٱللَّهِ, 40:84 بِٱللَّهِ, 40:85 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 40:2 ٱللَّهِ, 40:3 إِلَٰهَ, 40:4 ٱللَّهِ, 40:10 ٱللَّهِ, 40:12 ٱللَّهُ, 40:12 لِلَّهِ, 40:14 ٱللَّهَ, 40:16 ٱللَّهِ, 40:16 لِلَّهِ, 40:17 ٱللَّهَ, 40:20 وَٱللَّهُ, 40:20 ٱللَّهَ, 40:21 ٱللَّهُ, 40:21 ٱللَّهِ, 40:22 ٱللَّهُ, 40:28 ٱللَّهُ, 40:28 ٱللَّهَ, 40:29 ٱللَّهِ, 40:31 ٱللَّهُ, 40:33 ٱللَّهِ, 40:33 ٱللَّهُ, 40:34 ٱللَّهُ, 40:34 ٱللَّهُ, 40:35 ٱللَّهِ, 40:35 ٱللَّهِ, 40:35 ٱللَّهُ, 40:37 إِلَٰهِ, 40:42 بِٱللَّهِ, 40:43 ٱللَّهِ, 40:44 ٱللَّهِ, 40:44 ٱللَّهَ, 40:45 ٱللَّهُ, 40:48 ٱللَّهَ, 40:55 ٱللَّهِ, 40:56 ٱللَّهِ, 40:56 بِٱللَّهِ, 40:61 ٱللَّهُ, 40:61 ٱللَّهَ, 40:62 ٱللَّهُ, 40:62 إِلَٰهَ, 40:63 ٱللَّهِ, 40:64 ٱللَّهُ, 40:64 ٱللَّهُ, 40:64 ٱللَّهُ, 40:65 إِلَٰهَ, 40:65 لِلَّهِ, 40:66 ٱللَّهِ, 40:69 ٱللَّهِ, 40:74 ٱللَّهِ, 40:74 ٱللَّهُ, 40:77 ٱللَّهِ, 40:78 ٱللَّهِ, 40:78 ٱللَّهِ, 40:79 ٱللَّهُ, 40:81 ٱللَّهِ, 40:84 بِٱللَّهِ, 40:85 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ع ز ز (root_001008): 40:2 ٱلْعَزِيزِ, 40:8 ٱلْعَزِيزُ, 40:42 ٱلْعَزِيزِ

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

## ع ل م (root_001040): 40:2 ٱلْعَلِيمِ, 40:7 وَعِلْمًا, 40:19 يَعْلَمُ, 40:42 عِلْمٌ, 40:57 يَعْلَمُونَ, 40:64 ٱلْعَٰلَمِينَ, 40:65 ٱلْعَٰلَمِينَ, 40:66 ٱلْعَٰلَمِينَ, 40:70 يَعْلَمُونَ, 40:83 ٱلْعِلْمِ

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

## غ ف ر (root_001096): 40:3 غَافِرِ, 40:7 وَيَسْتَغْفِرُونَ, 40:7 فَٱغْفِرْ, 40:42 ٱلْغَفَّٰرِ, 40:55 وَٱسْتَغْفِرْ

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

## ذ ن ب (root_000521): 40:3 ٱلذَّنۢبِ, 40:11 بِذُنُوبِنَا, 40:21 بِذُنُوبِهِمْ, 40:55 لِذَنۢبِكَ

- **B001** günah veya kötü sonuç doğuran suç — günah, suç veya kötü sonuç doğuran davranış · günah ya da suç işlemek
  الذنب والجرم (maqayis)؛ الذنب معروف أذنب يذنب إذنابا (jamhara)؛ الذنب الجرم وقد أذنب الرجل (sihah)؛ الذنب الإثم والمعصية (tahdhib)؛ يستعمل في كل فعل يستوخم عقباه (mufradat)
- **B002** kuyruk; bir şeyin arka ucu veya sonu — hayvan kuyruğu veya bir şeyin arka ucu · kuşun kuyruğu veya kuyruk kökü; at ve devede de kullanılan ad · bir şeyin sonu veya arka ucu · uzun kuyruklu at · başlığından kuyruk gibi bir parçayı aşağı sarkıtmak · çok öne geçip yakalanamaz olmak · geçmiş bir işin ardından gidip kaçırdığına hayıflanmak
  ذنب وهو مؤخر الدواب (maqayis)؛ ذنب الدابة معروف (jamhara)؛ ذنب الطائر وذناباه وذنب الفرس وذناباه (jamhara)؛ الذنب واحد الأذناب والذنابى ذنب الطائر (sihah)؛ ذنب كل شيء آخره (tahdhib)؛ ذنب الدابة وغيرها معروف (mufradat)
- **B003** ardından giden takipçiler — halkın aşağı görülen, geriden gelen takipçileri · birinin veya bir şeyin ardından gelen takipçi · sürünün kuyruğu yanında duran veya izini bırakmadan ardından giden kişi · takipçileriyle birlikte gelmek
  الأتباع الذنابي (maqayis)؛ أذناب الناس رذالهم (jamhara)؛ الذنابى الأتباع والذانب التابع (sihah)؛ ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء (tahdhib)؛ يعبر به عن المتأخر والرذل (mufradat)
- **B004** su yatağı ve vadinin son kesimi — yamaçlı dere yataklarındaki su akış yolları · vadinin veya nehrin sonu, suyunun ulaştığı yer · iki yamaçlı dere yatağı arasındaki su yolu · su yolu veya çayırlıktan dışarı akan küçük kanal
  المذانب مذانب التلاع وهي مسايل الماء فيها (maqayis)؛ ذنبة الوادي والنهر آخره وذِنابته (jamhara)؛ المذنب مسيل ماء وذنابة الوادي (sihah)؛ ذنب التلعة ومذنب النهر والمذنب كهيئة الجدول (tahdhib)؛ مذانب التلاع لمسائل مياهها (mufradat)
- **B005** hurmanın uçtan başlayarak kısmen olgunlaşması — bir ucundan olgunlaşmaya başlamış hurma · ham hurmanın kuyruk sayılan ucundan olgunlaşmaya başlaması · ucu olgunlaşmaya başlamış ham hurma
  المذنب من الرطب ما أرطب بعضه (maqayis)؛ ذنب البسر وأذنب إذا أرطب مما يلي أقماعه وهو التذنوب (jamhara)؛ التذنوب البسر الذي قد بدأ فيه الإرطاب من قبل ذنبه (sihah)؛ إذا بدت نكت من الإرطاب في البسر من قبل ذنبها قيل قد ذنبت فهي مذنبة (tahdhib)؛ المذنب ما أرطب من قبل ذنبه (mufradat)
- **B006** kişiye düşen pay veya nasip — pay veya nasip, özellikle azaptan düşen pay · eksik bir paya razı olmak
  الثالث كالحظ والنصيب (maqayis)؛ الذنوب في التنزيل هو النصيب (jamhara)؛ الذنوب النصيب (sihah)؛ تذهب به إلى النصيب والحظ (tahdhib)؛ استعير للنصيب (mufradat)
- **B007** kova; özellikle büyük, dolu veya kuyruk ipli olanı — büyük, dolu veya kuyruk ipi bulunan kova
  الذنوب الدلو (jamhara)؛ الذنوب الدلو الملأى ماء (sihah)؛ الذنوب الدلو العظيمة (tahdhib)؛ الدلو التي لها ذنب (mufradat)
- **B008** kepçe — kepçe veya büyük servis kaşığı
  المذانب أيضا المغارف والواحدة مذنب ومذنبة (jamhara)؛ المذنب المغرفة (sihah)؛ المذانب المغارف واحدها مذنبة (tahdhib)
- **B009** tilkikuyruğu da denen bir bitki — tilkikuyruğu da denen bilinen bir bitki
  الذنبان ضرب من النبت (jamhara)؛ الذنبان نبت (sihah)؛ الذنبان نبت معروف الواحدة ذنبانة وبعض العرب تسميه ذنب الثعلب (tahdhib)
- **B010** hayvanın kuyruğa bağlı özel davranışı — çekirgenin yumurtlamak için arka kısmını yere saplaması · kertenkelenin kuyruğu önde geri çıkması veya kuyruğuyla vurması · hayvanın kuyruğa bağlı çiftleşme veya vurma davranışı
  ذنب الجراد إذا غرز ليبيض (jamhara)؛ ذنب الضب إذا خرج بذنبه من جحره موليا (jamhara)؛ التذنيب للضباب والفراش إذا أرادت التعاظل والسفاد (tahdhib)؛ إنما يقال للضب مذنب إذا ضرب بذنبه (tahdhib)

## ق ب ل (root_001198): 40:3 وَقَابِلِ, 40:5 قَبْلَهُمْ, 40:21 قَبْلِهِمْ, 40:34 قَبْلُ, 40:67 قَبْلُ, 40:74 قَبْلُ, 40:78 قَبْلِكَ, 40:82 قَبْلِهِمْ

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

## ت و ب (root_000189): 40:3 ٱلتَّوْبِ, 40:7 تَابُوا۟

- **B001** yanlistan Tanri'ya donus — yanlisindan donup Tanri'ya yoneldi · yanlistan donme, pismanlikla birakma · yanlistan donme eylemi · Tanri'ya tam bir donus · Tanri'ya donen kisi · Rabbine sikca donen kul · yaraticiniza donun
  كلمة واحدة تدل على الرجوع (maqayis)؛ التوب مصدر تاب يتوب توبا (jamhara)؛ التوبة الرجوع من الذنب (sihah)؛ تاب عاد إلى الله ورجع وأناب (tahdhib)؛ التوب ترك الذنب على أجمل الوجوه (mufradat)
- **B002** Tanri'nin donusu kabul etmesi — Tanri onun donusunu kabul etti ve bagisladi · kullarin donusunu cokca kabul eden Tanri · Tanri kulunun donusunu kabul edendir
  وقد تاب الله عليه وفقه لها (sihah)؛ تاب الله عليه أي عاد عليه بالمغفرة (tahdhib)؛ تاب الله عليه أي قبل توبته (mufradat)؛ التواب من صفات الله هو الذي يتوب على عباده (tahdhib)؛ يقال ذلك لله تعالى لكثرة قبوله توبة العباد (mufradat)
- **B003** donuse cagirma — ondan yanlisindan donmesini istedi veya bunu teklif etti
  استتابه سأله أن يتوب (sihah)؛ استتبت فلانا أي عرضت عليه التوبة مما اقترف (tahdhib)
- **B004** hafifletmeye dondurme — sizi hafifletmeye dondurdu veya onceki yasagi serbest kildi
  فتاب عليكم أي رجع بكم إلى التخفيف (tahdhib)؛ أي أباح لكم ما كان حظر عليكم (tahdhib)

## ت ب ب (root_000172): 40:37 تَبَابٍ (also echo for 40:3 ٱلتَّوْبِ, 40:7 تَابُوا۟)

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع

## ش د د (root_000782): 40:3 شَدِيدِ, 40:21 أَشَدَّ, 40:22 شَدِيدُ, 40:46 أَشَدَّ, 40:67 أَشُدَّكُمْ, 40:82 وَأَشَدَّ

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

## ع ق ب (root_001033): 40:3 ٱلْعِقَابِ, 40:5 عِقَابِ, 40:21 عَٰقِبَةُ, 40:22 ٱلْعِقَابِ, 40:82 عَٰقِبَةُ

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

## ط و ل (root_000959): 40:3 ٱلطَّوْلِ

- **B001** uzunluk ve boyca geçme — uzunluk · uzamak, uzun duruma gelmek · uzun, daha uzun ya da uzun boylu · birini boyca geçmek · üst dudağı alt dudağından uzun deve · bakmak için doğrulup başını ve gövdesini uzatmak · Kur'an'ın yedi uzun suresi · uzun boylu bir çocuk doğurmak
  أصل صحيح يدل على فضل وامتداد في الشيء (maqayis)؛ طال الشيء يطول طولا فهو طويل (maqayis;ayn;tahdhib)؛ الطول خلاف العرض (maqayis;sihah)؛ الأطول نقيض الأقصر (ayn;tahdhib)؛ الطول والقصر من الأسماء المتضايفة (mufradat)؛ طال فلان فلانا أي فاته في الطول (ayn;tahdhib)
- **B002** uzun otlatma ipi — uzun otlatma ipi · atın bağını merada gevşetmek · hayvanı otlatırken ayağına bağlanan uzun ip
  للحبل الطول لطوله وامتداده (maqayis)؛ الطول اسم حبل تشد به قوائم الدابة ثم ترسل في المرعى (ayn)؛ الحبل الذي يطول للدابة فترعى فيه (sihah;tahdhib)؛ الحبل المرخي على الدابة (mufradat)؛ طول فرسك أي أرخ له حبله في مرعاه (ayn;tahdhib)
- **B003** zamanın uzayıp gitmesi [kalıp] — bütün zaman boyunca · süresi uzamak, işte oyalanıp ağır davranmak
  لا أكلمه طوال الدهر (maqayis;ayn;sihah;tahdhib)؛ طال طولك إذا طال تماديه في أمر وتراخيه عنه (ayn;tahdhib)؛ طال طولك وطيلك أي طالت مدته (tahdhib)؛ يستعمل في الأعراض كالزمان (mufradat)؛ تطاول عليهم العمر (mufradat)
- **B004** güç, varlık ve iyilik üstünlüğü — güç, varlık, bolluk, üstünlük ve iyilik · güç ve bolluk sahibi · evlenme bedeli ve geçim giderini karşılayacak maddi güç · insanlara iyilik ve bağışla üstünlük göstermek
  يدل على فضل وامتداد (maqayis)؛ الطول القدرة وإن فلانا لذو طول أي ذو قدرة (ayn)؛ الطول بالفتح المن (sihah)؛ الطول هنا القدرة على المهر (tahdhib)؛ الطول الغنى والطول الفضل (tahdhib)؛ الطول خص به الفضل والمن (mufradat)؛ طولا كناية عما يصرف إلى المهر والنفقة (mufradat)
- **B005** işe yarar değer — işe yarar yanı ve kayda değer üstünlüğü olmayan iş · işe yarar değer ve ayırt edici üstünlük
  أمر غير طائل إذا لم يكن فيه غناء (maqayis)؛ للخسيس الدون هذا غير طائل (ayn;tahdhib)؛ أمر لا طائل فيه إذا لم يكن فيه غناء ومزية (sihah)؛ اشتقاق الطائل من الطول (ayn;tahdhib)
- **B006** üstünlük taslama ve baskın çıkma — başkalarına tepeden bakıp böbürlenme · onlardan daha çok kişi öldürerek baskın çıkmak
  استطالوا عليهم إذا قتلوا منهم أكثر مما قتلوا (maqayis)؛ التطاول هو الاستطالة على الناس إذ رفع رأسه ورأى أن له عليهم فضلا (ayn;tahdhib)؛ استطال عليه أي تطاول (sihah)؛ التطاول مذموم وكذلك الاستطالة يوضعان موضع التكبر (tahdhib)؛ تطاول فلان إذا أظهر الطول أو الطول (mufradat)
- **B007** uzatma, sürüncemede bırakma ve süre tanıma — uzatmak veya sürdürmek · işi sürüncemede bırakmak · birine süre tanımak
  المطاولة في الأمر هي التطويل (ayn;tahdhib)؛ طاولته في الأمر أي ماطلته (sihah)؛ أطلت الشيء وأطولت بمعنى (sihah)؛ طول له تطويلا أي أمهله (sihah)
- **B008** düşmanlık ve öç alacağı — düşmanlık, öç alacağı ve kan davası
  بينهم طائلة أي عداوة وترة (sihah)؛ الطوائل الأوتار والذحول (tahdhib)؛ يطلب بني فلان بطائلة أي بوتر (tahdhib)

## ص ي ر (root_000897): 40:3 ٱلْمَصِيرُ

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

## ج د ل (root_000229): 40:4 يُجَٰدِلُ, 40:5 وَجَٰدَلُوا۟, 40:35 يُجَٰدِلُونَ, 40:56 يُجَٰدِلُونَ, 40:69 يُجَٰدِلُونَ

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

## ء ي ي (root_000074): 40:4 ءَايَٰتِ, 40:13 ءَايَٰتِهِۦ, 40:23 بِـَٔايَٰتِنَا, 40:35 ءَايَٰتِ, 40:56 ءَايَٰتِ, 40:63 بِـَٔايَٰتِ, 40:69 ءَايَٰتِ, 40:78 بِـَٔايَةٍ, 40:81 ءَايَٰتِهِۦ, 40:81 ءَايَٰتِ

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

## ك ف ر (root_001307): 40:4 كَفَرُوا۟, 40:6 كَفَرُوٓا۟, 40:10 كَفَرُوا۟, 40:10 فَتَكْفُرُونَ, 40:12 كَفَرْتُمْ, 40:14 ٱلْكَٰفِرُونَ, 40:22 فَكَفَرُوا۟, 40:25 ٱلْكَٰفِرِينَ, 40:42 لِأَكْفُرَ, 40:50 ٱلْكَٰفِرِينَ, 40:74 ٱلْكَٰفِرِينَ, 40:84 وَكَفَرْنَا, 40:85 ٱلْكَٰفِرُونَ

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

## غ ر ر (root_001078): 40:4 يَغْرُرْكَ

- **B001** katlama ve kırılma izi — kumaşta veya deride kat ve kırık izi · kumaşı ilk kat izinden katla
  الغر وهو الكسر في الثوب (maqayis)؛ الغر الكسر في الثوب وفي الجلد (ayn)؛ غر الثوب وهو أثر تكسر الطي (jamhara)؛ الغرور مكاسر الجلد وطويت الثوب على غره (sihah)؛ مكاسر الجلد وخنثه أي على كسره (tahdhib)؛ غر الثوب أثر كسره (mufradat)
- **B002** örnek kalıp ve aynı örüntü — örnek kalıp; aynı biçimde ilerleyen düzen · aynı yol veya örüntü üzerinde
  الغرار المثال الذي يطبع عليه السهام وولدت على غرار واحد (maqayis)؛ الغرار المثال الذي تطبع عليه نصال السهام (ayn)؛ الغرار الطريقة وعلى غرار واحد (sihah)؛ الغرار الطريقة والمثال الذي يضرب النصال (tahdhib)
- **B003** alındaki ak leke ve görünür aklık — atın alnındaki ak leke; görünür aklık · ak; alnında belirgin aklık bulunan
  الغرة البياض وكل أبيض أغر (maqayis)؛ الغرة في الجبهة بياض والأغر الأبيض (ayn)؛ غرة الفرس وكل شيء بدا لك من ضوء (jamhara)؛ الغرة بياض في جبهة الفرس والأغر الأبيض (sihah)؛ الغرة من البياض في وجه الفرس (tahdhib)؛ غرة الفرس (mufradat)
- **B004** seçkinlik, önderlik ve güzel yaradılış — topluluğun önderi veya en seçkini · bağlama göre bir şeyin başlangıcı ya da en seçkin yanı · iyi ve yumuşak yaradılış
  غرة كل شيء أكرمه والغرير الخلق الحسن (maqayis)؛ فلان غرة من غرر قومه وغرة المتاع (ayn)؛ غرة القوم سيدهم (jamhara)؛ فلان غرة قومه أي سيدهم وغرة كل شيء أوله وأكرمه (sihah)؛ غرة المال أفضله وغرة القوم سيدهم (tahdhib)؛ فلان أغر إذا كان مشهورا كريما (mufradat)
- **B005** başlangıç ve ayın ilk geceleri — bağlama göre bir şeyin başlangıcı ya da en seçkin yanı · ayın ilk üç gecesi · ayın ince yayınının ilk görüldüğü gece
  لثلاث ليال من أول الشهر غرة (maqayis)؛ غرة كل شيء أوله وغرة الهلال والغرر ثلاثة أيام (ayn)؛ ثلاث ليال لأول الشهر يسمين الغرر (jamhara)؛ غرة كل شيء أوله والغرر ثلاث ليال (sihah)؛ ثلاث غرر واحدتها غرة وبياض الهلال (tahdhib)؛ الغرر لثلاث ليال من أول الشهر (mufradat)
- **B006** dölüt için köleyle ödenen kan bedeli [kalıp] — dölüt için erkek ya da kadın köleyle ödenen kan bedeli
  في الجنين غرة عبد أو أمة (maqayis)؛ في الجنين غرة يعني عبدا أو أمة (jamhara)؛ قضى في الجنين بغرة كأنه عبر عن الجسم كله بالغرة (sihah)؛ جعل في الجنين غرة عبدا أو أمة (tahdhib)
- **B007** deneyimsiz ve kötülüğü sezmeyen saflık — az deneyimli, saf ve uyanıksız · deneyimsiz veya kolayca aldanan · deneyim azlığı ve dalgın saflık
  الغرارة كالغفلة ومن نقصان الفطنة (maqayis)؛ الغر الذي لم يجرب الأمور والمؤمن غر كريم (ayn)؛ رجل غر إذا لم يجرب الأمور (jamhara)؛ رجل غر وغرير أي غير مجرب والغرة الغفلة (sihah)؛ الغر الذي لا يفطن للشر (tahdhib)؛ الغرة غفلة في اليقظة (mufradat)
- **B008** yanıltıcı görünüşle aldatma — birini yalan görünüş veya sözle aldatmak · kişiyi aldatan şey veya ayartıcı
  الغرور من غر يغر فيغتر به المغرور والغرور الشيطان (ayn)؛ غر الرجل الرجل إذا أوطأه عشوة أو خبره بكذب (jamhara)؛ غره يغره غرورا خدعه والغرور الشيطان (sihah)؛ لا تغرنكم الدنيا والغرور الشيطان والباطل (tahdhib)؛ الغرور كل ما يغر الإنسان من مال وجاه وشهوة وشيطان (mufradat)
- **B009** sonucu belirsiz tehlike — sonucu belirsiz tehlike · sonucu ve konusu belirsiz, güvencesiz satış · kendini tehlikeye atmak
  بيع الغرر وهو الخطر الذي لا يدري أيكون أم لا (maqayis)؛ الغرر كالخطر وغرر بماله أي حمله على الخطر (ayn)؛ الغرر الخطر وبيع الغرر (sihah)؛ بيع الغرر على غير عهدة ولا ثقة والبيوع المجهولة (tahdhib)؛ الغرر الخطر (mufradat)
- **B010** azalma, azlık ve eksik bırakma — azalma, azlık veya tamamlanmama · ibadeti ve selam karşılığını eksik bırakmamak · az ve kısa uyku · dişi devenin sütü azalmak
  غارت الناقة إذا نقص لبنها ولا غرار في صلاة والغرار النوم القليل (maqayis)؛ غرار نقصان لبن الناقة ولا غرار في الصلاة والغرار النوم القليل (ayn)؛ الغرار النوم القليل ونقصان لبن الناقة ولا غرار في صلاة (sihah)؛ الغرار النقصان وقل لبنها وغرار النوم قلته وما أقمت إلا غرارا وغارت السوق إذا كسدت (tahdhib)؛ الغرار لبن قليل وغارت الناقة قل لبنها (mufradat)
- **B011** ağza besin itme veya su kabını doldurma — kuş yavrusunun ağzına veya kursağına besin vermek · su kabını suya sokup elle doldurmak
  غر الطائر فرخه إذا زقه (maqayis)؛ الطائر يغر فرخه إذا زقه (ayn)؛ غر الطير فرخه إذا زقه (jamhara)؛ غر الطائر فرخه أي زقه (sihah)؛ الطائر يغر فرخه وغر في سقائك وغررت الأساقي إذا ملأتها (tahdhib)
- **B012** kılıcın veya bıçağın keskin ağzı [kalıp] — kılıcın keskin ağzı veya kesen kenarı
  غرار السيف وهو حده وكل شيء له حد فحده غرار (maqayis)؛ الغرار حد الشفرة والسيف (ayn)؛ الغراران شفرتا السيف وكل شيء له حد فحده غراره (sihah)؛ الغرار حد السيف وحد السكين الغرار (tahdhib)؛ غرار السيف أي حده (mufradat)
- **B013** yük taşımaya yarayan büyük çuval — yük taşımaya yarayan çuval veya büyük torba
  الغرارة وعاء (ayn)؛ الغرارة واحدة الغرائر التي للتبن وأظنه معربا (sihah)؛ الغرارة الجوالق وجمعها غرائر (tahdhib)
- **B014** biçime bağlı adlandırmalar — boğazda çalkalanma veya boğazdan yinelenen ses · ağız ve boğazda çalkalanan ilaç
  الغرغرة التغرغر في الحلق (ayn)؛ الغرغرة تردد الروح في الحلق والراعي يغرغر بصوته ويتغرغر بالدواء (sihah)؛ تغرغرت عينه بالدمع والغرغرة حكاية صوت وغرغر بالدواء (tahdhib)

## ق ل ب (root_001248): 40:4 تَقَلُّبُهُمْ, 40:18 ٱلْقُلُوبُ, 40:35 قَلْبِ

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

## ب ل د (root_000148): 40:4 ٱلْبِلَٰدِ

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

## ك ذ ب (root_001290): 40:5 كَذَّبَتْ, 40:24 كَذَّابٌ, 40:28 كَٰذِبًا, 40:28 كَذِبُهُۥ, 40:28 كَذَّابٌ, 40:37 كَٰذِبًا, 40:70 كَذَّبُوا۟

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

## ق و م (root_001273): 40:5 قَوْمُ, 40:29 يَٰقَوْمِ, 40:30 يَٰقَوْمِ, 40:31 قَوْمِ, 40:32 وَيَٰقَوْمِ, 40:38 يَٰقَوْمِ, 40:39 يَٰقَوْمِ, 40:41 وَيَٰقَوْمِ, 40:46 تَقُومُ, 40:51 يَقُومُ

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

## ح ز ب (root_000315): 40:5 وَٱلْأَحْزَابُ, 40:30 ٱلْأَحْزَابِ

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

## ب ع د (root_000131): 40:5 بَعْدِهِمْ, 40:31 بَعْدِهِمْ, 40:34 بَعْدِهِۦ

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

## ه م م (root_001602): 40:5 وَهَمَّتْ

- **B001** bir şeyi içinden geçirme, isteme veya ona karar verme — bir şeyi içinden geçirmek, istemek veya yapmaya karar vermek · kişinin içinde yapmayı düşündüğü iş · bir işi yapmaya yönelik istek ve kararlılık · isteği ve kararlılığı çok güçlü yönetici veya kişi · bunu düşünmüyorum ve yapmayacağım
  هم بالشيء يهم هما إذا عزم عليه أو حدث به نفسه (jamhara)؛ الهمة التي يجيلها الإنسان في خلده (jamhara)؛ هممت بالشئ أهم هما إذا أردته (sihah)؛ الهمة واحدة الهمم (sihah)؛ الهم ما هممت به من أمر في نفسك (tahdhib)؛ الهمة ما هممت به من أمر لتفعله (tahdhib)؛ لا يكاد ولا يهم (tahdhib)؛ الهم ما هممت به في نفسك وهو الأصل (mufradat)؛ الهم ما هممت به وكذلك الهمة (maqayis)؛ الهمام الملك العظيم الهمة (sihah;tahdhib;maqayis)؛ لا همام أي لا أهم بذلك ولا أفعله (sihah;tahdhib;maqayis)
- **B002** üzüntü, tasa ve kaygı — üzüntü, tasa ve kaygı · beni kaygılandırdı ve üzdü · ağır ve çetin iş · kaygılanma veya birinin işiyle ilgilenme · kaygılandı ve ilgilendi
  همه الحزن والمرض إذا أذابه (jamhara)؛ أهمني الشيء إذا أحزنني (jamhara)؛ الهم الحزن (sihah;tahdhib)؛ أهمني الأمر إذا أقلقك وحزنك (sihah)؛ المهم الأمر الشديد (sihah)؛ الاهتمام الاغتمام (sihah)؛ اهتم له بأمره (sihah)؛ المهمات من الأمور الشدائد (tahdhib)؛ ما أهمك أي ما أحزنك وقيل ما أقلقك (tahdhib)؛ الهم الحزن الذي يذيب الإنسان (mufradat)؛ أهمني كذا أي حملني على أن أهم به (mufradat)؛ الهم الذي هو الحزن عندنا من هذا القياس (maqayis)؛ مهم الأمر شديده وأهمني أقلقني (maqayis)؛ احتم الرجل فالحاء مبدلة من هاء وإنما هو من اهتم (maqayis-ibdal)
- **B003** eritme, erime ve eriyip akma — hastalık onu eritip tüketti · yağı eritip akıtmak · yağ veya buz eridi · eriyip akan yağ veya erimiş madde · eriyen karın akan suyu · güneş karı eritti · alnından ter aktı · sütü kaba sağdı
  هممت الشحمة في النار إذا أذبتها (jamhara)؛ الهاموم ما خرج منها (jamhara)؛ ما ذاب من البرد الهمام (jamhara)؛ همنى المرض أذا بنى (sihah)؛ انهم الشحم والبرد ذابا (sihah)؛ الهاموم ما أذيب من السنام (sihah)؛ الانهمام الانهضام في ذوبان الشيء واسترخائه بعد جموده (tahdhib)؛ كل شيء ذائب يسمى هاموما (tahdhib)؛ همت الشمس الثلج أذابته (tahdhib)؛ همام الثلج ما سال من مائه إذا ذاب (tahdhib)؛ انهم العرق من جبينه إذا سال (tahdhib)؛ هم اللبن في الصحن إذا حلبه (tahdhib)؛ هممت الشحم فانهم (mufradat)؛ همني الشيء أذابني وانهم الشحم ذاب (maqayis)؛ الهاموم الشحم الكثير الإهالة (maqayis)
- **B004** suyu bol kuyu veya bol yağışlı bulut — suyu bol kuyu · bol yağış boşaltan bulut
  الهموم البئر الكثيرة الماء (sihah)؛ السحاب الهاموم الكثير الصوب (maqayis)؛ الهموم البئر الكثيرة الماء (maqayis)
- **B005** sürünüş ve yerde sürünen küçük canlılar — yerde sürünme, küçük canlıların sürünüşü · yerde sürünen böcekler, yılanlar ve zehirli küçük canlılar · sürünen küçük canlılardan biri; özellikle yılan · yılan adamı soktu
  الهميم الدبيب (sihah)؛ الهامة واحدة الهوام (sihah)؛ لا يقع هذا الاسم إلا على المخوف من الأحناش (sihah)؛ الهميم دبيب هوام الأرض (tahdhib)؛ الهوام ما كان من خشاش الأرض (tahdhib)؛ الهامة الحية (tahdhib)؛ الحية قد همت الرجل (tahdhib)؛ أيؤذيك هوام رأسك أراد بها القمل (tahdhib)؛ ما رأيت هامة قط أكرم منه (tahdhib)؛ الهوام حشرات الأرض (mufradat)؛ الهوام حشرات الأرض سميت لهميمها أي دبيبها (maqayis)
- **B006** yaşlılıktan eriyip tükenmiş kimse — yaşlılıktan eriyip tükenmiş erkek · yaşlılıktan eriyip tükenmiş kadın
  قولهم للشيخ هم كأنهم أرادوا نحوله من الكبر (jamhara)؛ الهم بالكسر الشيخ الفاني والمرأة همة (sihah)؛ الهم الشيخ البالي (tahdhib)؛ رجل هم وامرأة همة أي كبير قد همه العمر (mufradat)؛ الهم الرجل المسن والمرأة همة كأنهما قد ذابا من الكبر (maqayis)
- **B007** ince taneli hafif yağmur veya yumuşak esinti — ince taneli, hafif ve yumuşak yağmur · zayıf ve hafif yağmur
  الهميمة مطر لين دقاق القطر (sihah)؛ التهميم المطر الضعيف (tahdhib)؛ الهميمة من المطر الشيء الهين (tahdhib)؛ الهميمة المطرة الخفيفة والريح الريدانة اللينة الهبوب (maqayis)
- **B008** göğüste yinelenen boğuk uğultu — göğüste yinelenen boğuk uğultu · anırmasını göğsünde boğuk boğuk yineleyen eşek · gök gürültüsü uğuldadı · adam anlaşılmaz biçimde mırıldandı
  الهمهمة ترديد الصوت في الصدر (sihah)؛ حمار هم هيم يهمهم في صوته (sihah)؛ الهمهمة تردد الزئير في الصدر من الهم والحزن (tahdhib)؛ الهمهمة نحو أصوات البقر والفيلة (tahdhib)؛ القصب إذا هزته الريح إنه لهمهوم (tahdhib)؛ الحمار إذا ردد نهيقه في صدره إنه لهمهيم (tahdhib)؛ همهم الرعد إذا سمعت له دويا (tahdhib)؛ همهم الأسد وهمهم الرجل إذا لم يبين كلامه (tahdhib)
- **B009** çocuğu yumuşak sesle uyutma — kadın çocuğu yumuşak bir sesle uyuttu
  هممت المرأة في رأس الصبي إذا نومته بصوت ترققه له (sihah)
- **B010** saçı parmaklarla aralayıp yoklama — parmaklarını saçlarının arasında ileri geri gezdirdi · başını ayıklayıp temizledi
  همم في رأسه جعل اصابعه في خلال شعره يجيء بها ويذهب لينام (maqayis)؛ كأن اصابعه تدب في خلال شعره (maqayis)؛ هو يتهمم رأسه أي يفليه (tahdhib)
- **B011** bir şeyi arayıp izini sürme; kalıpta kendi yararını gözetme — onu aramaya ve nerede olduğunu araştırmaya gittim · kendi yararını ara ve kendi işinle ilgilen
  ذهبت أتهممه أي أطلبه (sihah;tahdhib)؛ ذهبت أتهممه أنظر أين هو (tahdhib)؛ هم لنفسك ولا تهم لهؤلاء أي اطلب لها واحفل (tahdhib)
- **B012** hiçbir şey kalmadığını bildiren cevap sözü — hiçbir şey kalmadı
  إذا قيل لنا أبقى عندكم شئ نقول همهام أي لم يبق شئ (sihah)؛ أبقي عندكم شيء قالوا همهام وحمحام ومحماح وبحباح أي لم يبق شيء (tahdhib)
- **B013** birini değer ve yeterliğiyle öven kalıp [kalıp] — ne değerli adam, böylesi yeter
  هذا رجل همك من رجل وهمتك من رجل كما تقول ناهيك من رجل (mufradat)
- **B014** güzel yürüyüşlü dişi deve — güzel yürüyüşlü dişi deve
  الهموم الناقة الحسنة المشية (tahdhib)؛ والقرواح التي تعاف الشرب مع الكبار فإذا جاء الدهداه شربت معهن (tahdhib)

## ك ل ل (root_001315): 40:5 كُلُّ, 40:7 كُلَّ, 40:17 كُلُّ, 40:27 كُلِّ, 40:35 كُلِّ, 40:48 كُلٌّ, 40:62 كُلِّ (also echo for 40:79 تَأْكُلُونَ)

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

## ء م م (root_000053): 40:5 أُمَّةٍۭ

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

## ر س ل (root_000563): 40:5 بِرَسُولِهِمْ, 40:22 رُسُلُهُم, 40:23 أَرْسَلْنَا, 40:34 رَسُولًا, 40:50 رُسُلُكُم, 40:51 رُسُلَنَا, 40:70 أَرْسَلْنَا, 40:70 رُسُلَنَا, 40:78 أَرْسَلْنَا, 40:78 رُسُلًا, 40:78 لِرَسُولٍ, 40:83 رُسُلُهُم

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

## ء خ ذ (root_000018): 40:5 لِيَأْخُذُوهُ, 40:5 فَأَخَذْتُهُمْ, 40:21 فَأَخَذَهُمُ, 40:22 فَأَخَذَهُمُ

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

## ب ط ل (root_000127): 40:5 بِٱلْبَٰطِلِ, 40:78 ٱلْمُبْطِلُونَ

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

## د ح ض (root_000461): 40:5 لِيُدْحِضُوا۟

- **B001** ayağın kayıp tutunamaması — ayağı kaymak, ayağının tutuşunu yitirmek · kayma, kayganlık · kaygan yer · ayağın tutunmadığı kaygan yer · basınca ayağın tutmadığı kaygan yer · yeri kayganlaştıran su · kaydırma
  الدحض الزلق (maqayis;ayn;jamhara;tahdhib)؛ دحضت رجله زلقت (maqayis;sihah)؛ دحضت رجل البعير زلقت (ayn;tahdhib)؛ كل موضع لا تطمئن فيه القدم فهو مدحض (jamhara)؛ مكان دحض أي زلق (sihah)؛ أصله من دحض الرجل (mufradat)
- **B002** güneşin göğün ortasından ayrılması [kalıp] — güneş göğün orta noktasından ayrıldı
  دحضت الشمس زالت (maqayis)؛ دحضت الشمس عن بطن السماء أي زالت (ayn;tahdhib)؛ دحضت الشمس عن كبد السماء زالت (sihah)؛ دحضت الشمس مستعار من ذلك (mufradat)
- **B003** bir savın geçersizleşmesi veya geçersiz kılınması — savı geçersiz kaldı, gerekçesi çürük çıktı · savını çürüttü, geçersiz kıldı · geçersiz veya çürük sav · çürütülmüş, geçersiz bırakılmış
  دحضت حجة فلان إذا لم تثبت (maqayis)؛ دحضت حجته أي بطلت (ayn)؛ ودحضت حجته فهي داحضة وأدحضها الله (jamhara)؛ حجتهم داحضة بمعنى مدحوضة (jamhara)؛ دحضت حجته بطلت وأدحضها الله (sihah)؛ دحضت حجته إذا بطلت وأدحض حجته إذا أبطلها (tahdhib)؛ حجتهم داحضة أي باطلة زائلة (mufradat)؛ ليدحضوا به الحق (mufradat)

## ح ق ق (root_000347): 40:5 ٱلْحَقَّ, 40:6 حَقَّتْ, 40:20 بِٱلْحَقِّ, 40:25 بِٱلْحَقِّ, 40:55 حَقٌّ, 40:75 ٱلْحَقِّ, 40:77 حَقٌّ, 40:78 بِٱلْحَقِّ

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

## ك و ن (root_001332): 40:5 كَانَ, 40:21 كَانَ, 40:21 كَانُوا۟, 40:21 كَانُوا۟, 40:21 كَانَ, 40:22 كَانَت, 40:28 يَكُ, 40:28 يَكُ, 40:47 كُنَّا, 40:50 تَكُ, 40:63 كَانُوا۟, 40:67 لِتَكُونُوا۟, 40:68 كُن, 40:68 فَيَكُونُ, 40:73 كُنتُمْ, 40:74 نَكُن, 40:75 كُنتُمْ, 40:75 كُنتُمْ, 40:78 كَانَ, 40:82 كَانَ, 40:82 كَانُوٓا۟, 40:82 كَانُوا۟, 40:83 كَانُوا۟, 40:84 كُنَّا, 40:85 يَكُ

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

## ك ل م (root_001316): 40:6 كَلِمَتُ

- **B001** anlaşılır konuşma, hitap ve söz alışverişi — anlaşılır konuşma · ona hitap etti · birine söz yöneltme · ona sözle karşılık verdi · bir uzaklaşmadan sonra yeniden karşılıklı konuştuk · seninle konuşan ve senin de konuştuğun kişi · konuşulacak yer · sözünü iyi ve akıcı söyleyen kimse · iyi konuşan adam
  أحدهما يدل على نطق مفهم (maqayis)؛ كلمته أكلمه تكليما وهو كليمى إذا كلمك أو كلمته (maqayis)؛ كليمك الذي يكلمك وتكلمه (ayn;tahdhib)؛ الكليم الذي يكلمك وكلمته تكليما وكلاما (sihah)؛ كالمته إذا جاوبته وتكالمنا بعد التهاجر (sihah)؛ ما أجد متكلما أي موضع كلام والكلماني المنطيق (sihah)؛ رجل تكلامة يحسن الكلام (tahdhib)
- **B002** anlam taşıyan tek söz birimi — anlamlı tek söz veya harf · en az üç sözden oluşan sözler topluluğu · sözler · bütün bir anlatı, şiir veya söylev · Tanrı'nın sözü · Tanrı'nın söylediği söz
  يسمون اللفظة الواحدة المفهمة كلمة والقصة كلمة والقصيدة بطولها كلمة ويجمعون الكلمة كلمات وكلما (maqayis)؛ الكلمة لغة حجازية والكلمة تميمية والجميع الكلم (ayn;tahdhib)؛ الكلام اسم جنس يقع على القليل والكثير والكلم لا يكون أقل من ثلاث كلمات والكلمة أيضا القصيدة بطولها (sihah)؛ الكلمة تقع على الحرف الواحد من حروف الهجاء وتقع على لفظة واحدة مؤلفة من جماعة حروف لها معنى وتقع على قصيدة بكمالها وخطبة بأسرها (tahdhib)؛ كلمة الله وكلام الله وكلم الله وكلمات الله (sihah;tahdhib)
- **B003** yaralama ve yara — yara · yaralar · yaralar · onu yaraladı · yaralayan · yaralanmış · yaralı kişi · yaralılar · yaralama · onları yaralayıp damgalaması
  الأصل الآخر الكلم وهو الجرح والكلام الجراحات وجمع الكلم كلوم (maqayis)؛ الكلم الجرح والجميع الكلوم وكلمته أكلمه كلما وأنا كالم وهو مكلوم أي جرحته (ayn)؛ الكلم الجراحة والجمع كلوم وكلام والتكليم التجريح (sihah)؛ الكلم الجرح والجميع كلوم وكلمته وأنا أكلمه كلما وأنا كالم وهو مكلوم (tahdhib)؛ تكلمهم فسر تجرحهم وتسمهم (sihah;tahdhib)

## ر ب ب (root_000532): 40:6 رَبِّكَ, 40:7 رَبِّهِمْ, 40:7 رَبَّنَا, 40:8 رَبَّنَا, 40:11 رَبَّنَآ, 40:26 رَبَّهُۥٓ, 40:27 بِرَبِّى, 40:27 وَرَبِّكُم, 40:28 رَبِّىَ, 40:28 رَّبِّكُمْ, 40:49 رَبَّكُمْ, 40:55 رَبِّكَ, 40:60 رَبُّكُمُ, 40:62 رَبُّكُمْ, 40:64 رَبُّكُمْ, 40:64 رَبُّ, 40:65 رَبِّ, 40:66 رَّبِّى, 40:66 لِرَبِّ

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

## ECHO ر ب و (root_000537): for 40:6 رَبِّكَ, 40:7 رَبِّهِمْ, 40:7 رَبَّنَا, 40:8 رَبَّنَا, 40:11 رَبَّنَآ, 40:26 رَبَّهُۥٓ, 40:27 بِرَبِّى, 40:27 وَرَبِّكُم, 40:28 رَبِّىَ, 40:28 رَّبِّكُمْ, 40:49 رَبَّكُمْ, 40:55 رَبِّكَ, 40:60 رَبُّكُمُ, 40:62 رَبُّكُمْ, 40:64 رَبُّكُمْ, 40:64 رَبُّ, 40:65 رَبِّ, 40:66 رَّبِّى, 40:66 لِرَبِّ: withheld observed target; not identity

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

## ص ح ب (root_000844): 40:6 أَصْحَٰبُ, 40:43 أَصْحَٰبُ

- **B001** süreğen eşlik ve yakın birliktelik — eşlik etmek veya birlikte bulunmak · sürekli eşlik eden kimse veya yoldaş · eşlik edenler topluluğu veya yoldaşlar · eşlik etme ve birlikte bulunma durumu · karşılıklı ve süreğen biçimde birlikte bulunma · bir şeyin sahibi veya o şeye sahip kişi · bir topluluğun ya da yöneticinin işini yürüten görevli · ey arkadaşım · iyi ve istekli biçimde arkadaşlık eden · yanında bir eşlikçisi bulunmak
  أصل واحد يدل على مقارنة شيء ومقاربته (maqayis)؛ الصاحب يجمع بالصحب والصحبان والصحبة والصحاب والأصحاب (ayn)؛ الصحب والصحاب والأصحاب والصحابة واحد (jamhara)؛ صحبه يصحبه صحبة وصحابة وجمع الصاحب صحب (sihah)؛ الصاحب الملازم إنسانا كان أو حيوانا أو مكانا أو زمانا (mufradat)؛ المصاحبة والاصطحاب أبلغ من الاجتماع (mufradat)؛ يقال للمالك للشيء هو صاحبه (mufradat)؛ وأصحب الرجل إذا كان ذا صاحب (ayn)
- **B002** eşlik eden koruma ve destek — Tanrı seni korusun · Tanrı onu korumasın · korunmak veya dinginlik ve destek görmek
  صحبك الله أي حفظك (ayn)؛ صحبه الله وأصحبه وصاحبه أي حفظه (jamhara)؛ لا يكون لهم من جهتنا ما يصحبهم من سكينة وروح وترفيق (mufradat)
- **B003** boyun eğip uyumlu duruma gelme — boyun eğmek ve güçlükten sonra uyumlu duruma gelmek · bir kimsenin ardından boyun eğerek gitmek
  أصحب فلان إذا انقاد (maqayis)؛ أصحبت الرجل إذا اتبعته منقادا (jamhara)؛ أصحب البعير والدابة إذا انقاد بعد صعوبة (sihah)؛ الإصحاب للشيء الانقياد له (mufradat)
- **B004** eşlikçi kılmak, yanında götürmek veya uygun düşmek — bir şeyi ona eşlikçi kılmak · kitabı veya başka bir şeyi yanına alıp götürmek · ona uygun düşmek ve onunla bağdaşmak
  كل شيء لاءم شيئا فقد استصحبه (maqayis;ayn;sihah)؛ أصحبته الشيء جعلته له صاحبا (sihah)؛ استصحبته الكتاب وغيره (sihah)؛ أصحب فلان فلانا جعل صاحبا له (mufradat)
- **B005** oğlunun büyüyüp babasına yoldaş olması — oğlu büyüyüp kendisine yoldaş olacak yaşa gelmek
  أصحب الرجل إذا بلغ ابنه (maqayis;sihah)؛ أصحب فلان إذا كبر ابنه فصار صاحبه (mufradat)
- **B006** kılı veya yünü üzerinde bırakılmış deri — kılı veya yünü üzerinde bırakılmış deri, post ya da tulum · hayvanı yüzerken kılı veya yünü deri üzerinde bırakmak
  الأديم إذا ترك عليه شعره مصحب (maqayis)؛ جلد مصحب إذا كان عليه شعره وصوفه (ayn)؛ صحبت المذبوح إذا سلخته وأبقيت على الجلد صوفا أو شعرا (jamhara)؛ أديم مصحب إذا دبغته وتركت عليه بعض الصوف أو الشعر (jamhara)؛ المصحب من الزقاق ما الشعر عليه (sihah)؛ أصحبته إذا تركت صوفه أو شعره عليه (sihah)؛ أديم مصحب أصحب الشعر الذي عليه ولم يجز عنه (mufradat)
- **B007** suyun yüzünü yosun kaplaması — suyun yüzü yosunla kaplanmak
  أصحب الماء إذا علاه الطحلب (maqayis;sihah)
- **B008** kızıla çalan açık toprak renginde eşek — kızıla çalan açık toprak renginde eşek
  حمار أصحب أي أصحر يضرب لونه إلى الحمرة (sihah)

## ن و ر (root_001564): 40:6 ٱلنَّارِ, 40:41 ٱلنَّارِ, 40:43 ٱلنَّارِ, 40:46 ٱلنَّارُ, 40:47 ٱلنَّارِ, 40:47 ٱلنَّارِ, 40:49 ٱلنَّارِ, 40:72 ٱلنَّارِ

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

## ح م ل (root_000357): 40:7 يَحْمِلُونَ, 40:80 تُحْمَلُونَ

- **B001** bir yükü kaldırıp götürme veya üstlenme — bir şeyi kaldırıp taşımak · sırtta, başta veya başka bir yerde dıştan taşınan yük · selin sürükleyip getirdiği çer çöp ve köpük
  حملت الشيء أحمله حملا (maqayis)؛ حملت الشئ على ظهرى أحمله حملا (sihah)؛ حمل الشيء يحمله حملا وحملانا (ayn;tahdhib)؛ حملت الثقل والرسالة والوزر حملا (mufradat)؛ حميل السيل ما يحمله من غثائه (maqayis)؛ حميل السيل ما يحمل من الغثاء (ayn;sihah)؛ حميل السيل ما حمله السيل (tahdhib)؛ حملناكم في الجارية (mufradat)
- **B002** gebelik veya ağacın meyve yükü — rahimdeki yavru veya ağacın üzerindeki meyve · gebe kadın · gebe olmadan sütü gelmek
  الحمل ما كان في بطن أو على رأس شجر (maqayis;sihah)؛ الحمل ما في البطن (ayn)؛ حمل الشجر (ayn)؛ حملت المرأة والشجرة حملا (sihah)؛ حملت المرأة حبلت وكذا حملت الشجرة (mufradat)؛ حملت حملا خفيفا (mufradat)
- **B003** görev veya suç yükünü üstlenme [kalıp] — suçun ve kötülüğün yükünü üzerine almak · güvenilerek verilen işi üstlenmek veya onu yerine getirmemek · iletiyi ulaştırma görevini üstlenmek
  حملت الثقل والرسالة والوزر حملا (mufradat)؛ كلفوا أن يتحملوها أي يقوموا بحقها فلم يحملوها (mufradat)؛ حمل الأمانة أي خيانتها وترك أدائها (tahdhib)؛ من باء بالإثم يسمى حاملا للإثم (tahdhib)؛ وساء لهم يوم القيامة حملا أي وزرا (sihah)
- **B004** başkasının borcunu üstlenip güvence verme — uzlaşma için üstlenilen kan bedeli veya ödeme yükü · başkası adına güvence vermek · borcun ödenmesini güvence altına alan kişi
  الحمالة أن يحمل الرجل دية ثم يسعى عليها والضمان حمالة (maqayis)؛ الحمالة الدية يحملها قوم عن قوم (ayn)؛ الحمالة ما يحمله القوم من الديات (jamhara)؛ حملت به حمالة أي كفلت (sihah)؛ الحميل الكفيل (jamhara;tahdhib;mufradat)؛ الحميل لكونه حاملا للحق مع من عليه الحق (mufradat)
- **B005** soy bağı doğrulanamayan getirilmiş çocuk — terk edilmiş, başka yerden getirilmiş veya soyu doğrulanamayan çocuk · soyu doğrulanamayan kişinin mirası
  الحميل المنبوذ يحمل فيربى (ayn;tahdhib)؛ الحميل الولد في بطن الأم إذا أخذت من أرض الشرك (ayn;tahdhib)؛ الحميل الذي يحمل من بلده صغيرا ولم يولد في الإسلام (sihah)؛ الحميل الدعي (maqayis;sihah)؛ ميراث الحميل لمن لا يتحقق نسبه (mufradat)
- **B006** taşıma kayışı, binek düzeneği veya yük hayvanı — kılıç askısı · deve üzerinde yolcu taşıyan iki yanlı düzenek · yük taşımaya ayrılmış deve veya başka hayvan · yükleri veya yolcu düzenekleriyle birlikte develer · armağan olarak verilen binek hayvanı
  الحمالة والمحمل علاقة السيف (maqayis;ayn;sihah)؛ حمالة السيف وحميلته والجمع الحمائل (jamhara)؛ المحمل الشقان على البعير يحمل فيهما نفسان (ayn)؛ المحمل واحد محامل الحاج (sihah)؛ الحمولة الإبل تحمل عليها الأثقال (maqayis;ayn)؛ الحمولة ما احتمل عليه الحي من بعير أو حمار أو غيره (sihah;tahdhib)
- **B007** zorlanarak yüklenme, eğilme veya dayanak olma — güç bir işe zorlanarak girişmek · yolculukta kendini sonuna kadar zorlamak · birinin üzerine doğru eğilmek veya yüklenmek · güvenilip dayanılan kişi veya şey
  تحاملت إذا تكلفت الشيء على مشقة (maqayis)؛ تحاملت في الشيء إذا تكلفته على مشقة (ayn)؛ حمل على نفسه في السير أي جهدها فيه (sihah)؛ تحامل عليه أي مال (sihah)؛ ما على فلان محمل أي معتمد (sihah;tahdhib)؛ المحمل بفتح الميم المعتمد (tahdhib)
- **B008** öfkeye kapılma veya incinmeye ağırbaşlılıkla katlanma — öfkelenmek veya öfkenin etkisine kapılmak · incitici davranışa öfkesini tutarak katlanmak
  الاحتمال الغضب (maqayis)؛ احتمل إذا غضب (maqayis;tahdhib)؛ احتمله الغضب وأقله الغضب (maqayis)؛ حملت عنه أي حلمت عنه (ayn)؛ احتمل الرجل إذا غضب ويكون بمعنى حلم (tahdhib)
- **B009** kuzu — kuzu
  الحمل الخروف والجميع الحملان (ayn;tahdhib)؛ الحمل من الضأن معروف وهو الجذع فما دونه (jamhara)؛ خص الضأن الصغير بذلك لكونه محمولا (mufradat)
- **B010** Koç burcu ve onunla ilişkilendirilen yağışlı gök olayı — Koç, burçlar kuşağının ilk burcu · bol su taşıyan kara bulut veya şimşek · bol su taşıyan bulut · Koç burcuna bağlanan yağış dönemi
  الحمل برج من البروج (ayn;tahdhib)؛ الحمل أول البروج (sihah)؛ البرق يقال له حمل (maqayis)؛ الحمل السحاب الكثير الماء (jamhara)؛ الحمل السحاب الأسود (tahdhib)؛ الحمل النوء وهو الطلي (tahdhib)؛ الحميل السحاب الكثير الماء لكونه حاملا للماء (mufradat)

## ع ر ش (root_001000): 40:7 ٱلْعَرْشَ, 40:15 ٱلْعَرْشِ

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

## ح و ل (root_000373): 40:7 حَوْلَهُۥ

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

## س ب ح (root_000666): 40:7 يُسَبِّحُونَ, 40:55 وَسَبِّحْ

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

## ح م د (root_000355): 40:7 بِحَمْدِ, 40:55 بِحَمْدِ, 40:65 ٱلْحَمْدُ

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

## ء م ن (root_000054): 40:7 وَيُؤْمِنُونَ, 40:7 ءَامَنُوا۟, 40:10 ٱلْإِيمَٰنِ, 40:12 تُؤْمِنُوا۟, 40:25 ءَامَنُوا۟, 40:27 يُؤْمِنُ, 40:28 مُّؤْمِنٌ, 40:28 إِيمَٰنَهُۥٓ, 40:30 ءَامَنَ, 40:35 ءَامَنُوا۟, 40:38 ءَامَنَ, 40:40 مُؤْمِنٌ, 40:51 ءَامَنُوا۟, 40:58 ءَامَنُوا۟, 40:59 يُؤْمِنُونَ, 40:84 ءَامَنَّا, 40:85 إِيمَٰنُهُمْ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## و س ع (root_001647): 40:7 وَسِعْتَ

- **B001** genişlik, genişleme ve genişletme — geniş duruma gelmek · bir şeyi genişletmek · genişlemek · genişlemek veya daha çok alan istemek · genişletme · oturma yerinde birbirine yer açmak · uzamsal genişlik · geniş, dar olmayan
  خلاف الضيق والعسر؛ وسع الشيء واتسع (maqayis)؛ وسعت الشيء فاتسع واستوسع؛ توسعوا في المجلس (sihah)؛ وسعت البيت وغيره فاتسع واستوسع؛ جعلنا بينها وبين الأرض سعة (tahdhib)؛ السعة تقال في الأمكنة؛ وسع الشيء اتسع (mufradat)
- **B002** güç yetirme ve alma kapasitesi — güç yetirme kapasitesi · gücü ve maddi varlığı ölçüsünde · bir işe gücü yetmek · bir kabın belirli miktarı içine alması · evinde kalıp onunla yetinmek
  الوسع الجدة والطاقة (maqayis;sihah)؛ الوسع جدة الرجل وقدرة ذات يده؛ طاقتك؛ لا يسعك (ayn)؛ ما أطيقه؛ هل تسع هذا أي هل تطيقه؛ هذا الوعاء يسع عشرين كيلا (tahdhib)؛ الوسع من القدرة؛ لا يكلف الله نفسا إلا وسعها (mufradat)
- **B003** para ve geçim bolluğu — varlık ve para gücü · para ve geçim bolluğu · varlıklı duruma gelmek · varlıklı ve ödeme gücü olan · varlıklı, geçimi bol · Tanrı sana bolluk verdi · gücü ve maddi varlığı ölçüsünde · zengin ve bolluk sahibi
  الوسع الغنى؛ والله الواسع أي الغني؛ الجدة؛ ذو سعة من سعته؛ أوسع الرجل كان ذا سعة (maqayis)؛ جدة الرجل وقدرة ذات يده؛ صار ذا سعة في المال؛ ذو سعة في عيشه (ayn)؛ الجدة والطاقة؛ سعة وغنى؛ أوسع الله عليك أي أغناك (sihah)؛ موسع وهو المليء؛ كثر ماله؛ سعة من عيشه (tahdhib)؛ في الحال؛ الموسع قدره؛ الغنى؛ صار ذا سعة (mufradat)
- **B004** her şeyi kuşatan bilgi, esirgeme, güç ve bağış — bilgisi, esirgemesi, gücü ve bağışı her şeyi kuşatan · Tanrı'nın esirgemesi her şeyi kuşattı · bilgisiyle her şeyi kuşatmak
  رحمة الله وسعت كل شيء (ayn)؛ الواسع من صفات الله؛ وسع رزقه جميع خلقه؛ وسعت رحمته كل شيء؛ المحيط بكل شيء؛ الكثير العطايا (tahdhib)؛ وسع ربنا كل شيء علما؛ والله واسع عليم؛ سعة قدرته وعلمه ورحمته وإفضاله (mufradat)
- **B005** kolaylık tanıyıp güçlüğü azaltma [kalıp] — geniş kolaylık tanıyan ve her şeyi bilen · mal yetmese de güler yüzle insanları hoşnut etmek
  خلاف الضيق والعسر (maqayis)؛ توسعة على الناس في شيء رخص لهم (tahdhib)؛ يكلف عبده دوين ما ينوء به قدرته؛ يريد الله بكم اليسر ولا يريد بكم العسر (mufradat)
- **B006** geniş ve uzun adımlı hızlı gidiş — geniş adımlı, uzun erişimli ve hızlı · geniş adımlı ve hızlı koşan at · atın adım ve bacak erişimi genişliği · geniş ve uzun adımlı gidiş
  الفرس الذريع الخطو وساع (maqayis)؛ وسع الفرس سعة ووساعة فهو وساع؛ سير وسيع ووساع (ayn)؛ فرس وساع أي واسع الخطو؛ وسع وساعة (sihah)؛ فرس وساع إذا كان جوادا ذا سعة في خطوه وذرعه؛ وسع وساعة (tahdhib)؛ فرس وساع الخطو شديد العدو (mufradat)

## س و ع (root_000760): 40:46 ٱلسَّاعَةُ, 40:59 ٱلسَّاعَةَ (also echo for 40:7 وَسِعْتَ)

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

## ش ي ء (root_000831): 40:7 شَىْءٍ, 40:15 يَشَآءُ, 40:16 شَىْءٌ, 40:20 بِشَىْءٍ, 40:62 شَىْءٍ, 40:74 شَيْـًٔا

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

## ش ي ء (root_000832): 40:7 شَىْءٍ, 40:15 يَشَآءُ, 40:16 شَىْءٌ, 40:20 بِشَىْءٍ, 40:62 شَىْءٍ, 40:74 شَيْـًٔا

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

## ر ح م (root_000552): 40:7 رَّحْمَةً, 40:9 رَحِمْتَهُۥ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ت ب ع (root_000175): 40:7 وَٱتَّبَعُوا۟, 40:38 ٱتَّبِعُونِ, 40:47 تَبَعًا

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

## س ب ل (root_000672): 40:7 سَبِيلَكَ, 40:11 سَبِيلٍ, 40:29 سَبِيلَ, 40:37 ٱلسَّبِيلِ, 40:38 سَبِيلَ

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

## و ق ي (root_001677): 40:7 وَقِهِمْ, 40:9 وَقِهِمُ, 40:9 تَقِ, 40:21 وَاقٍ, 40:45 فَوَقَىٰهُ

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

## ع ذ ب (root_000994): 40:7 عَذَابَ, 40:45 ٱلْعَذَابِ, 40:46 ٱلْعَذَابِ, 40:49 ٱلْعَذَابِ

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

## ج ح م (root_000225): 40:7 ٱلْجَحِيمِ

- **B001** şiddetle harlanan büyük ateş ve yakıcı sıcaklık — şiddetle harlanan büyük ateş · çok sıcak yer ya da harlanmış ateş · ateşin harlanıp korunun çoğalması · ateşin güçlü biçimde harlanması · sıkışıp daralmak ya da hırs ve cimrilikten içi yanmak
  عظمها به الحرارة وشدتها والجاحم المكان الشديد الحر وبه سميت الجحيم (maqayis)؛ الجحيم النار الشديدة التأجج والالتهاب (ayn)؛ الجحيم اسم من أسماء النار وكل نار عظيمة في مهواة فهي جحيم (sihah)؛ كل نار توقد على نار جحيم والجمر بعضه على بعض جحيم ورأيت جحمة النار أي توقدها (tahdhib)؛ الجحمة شدة تأجج النار ومنه الجحيم (mufradat)
- **B002** savaşta öldürmenin ve ölüm tehlikesinin doruğa çıkması — savaştaki yoğun öldürme · ölümün iyice şiddetlenmesi · sıkışıp daralmak ya da hırs ve cimrilikten içi yanmak
  الموت جاحم (maqayis;sihah)؛ جاحم الحرب شدة القتل في معركتها (ayn;tahdhib)؛ الحرب لا يبقى لجاحمها التخيل والمراح (tahdhib)
- **B003** göz; dik ve keskin bakış; iri kızıl göz; göz şişliği hastalığı — göz · aslanın iki parlak gözü · gözlerini dikerek açmak · keskin keskin bakmak · iri ve koyu kızıl gözlü · gözleri şişiren bir göz hastalığı
  الجحمة العين بلغة اليمن وجحمتا الأسد عيناه وجحم الرجل إذا فتح عينيه كالشاخص والعين جاحمة والجحام داء يصيب الإنسان في عينيه والأجحم الشديد حمرة العين مع سعتها (maqayis)؛ الجحمة العين بلغة حمير وجحمتا الأسد عيناه بكل لغة والأجحم الشديد حمرة العين مع سعتها (ayn)؛ جحم الرجل فتح عينيه كالشاخص وجحمني بعينيه تجحيما أحد إلي النظر والجحام داء يصيب الانسان فترم عيناه (sihah)؛ الجحمة هي العين بلغة حمير وجحمتا الأسد عيناه بكل لغة والأجحم الشديد حمرة العين مع سعتها والجحام داء معروف (tahdhib)؛ جحمتا الأسد عيناه لتوقدهما (mufradat)
- **B004** yüzün yoğun öfkeden ateş gibi alevlenmesi — yüzü yoğun öfkeden alev alev olmak
  جحم وجهه من شدة الغضب استعارة من جحمة النار وذلك من ثوران حرارة القلب (mufradat)
- **B005** utanma duygusu az olan kişi — utanma duygusu az olan kişi
  الجحم القليلو الحياء (tahdhib)

## د خ ل (root_000464): 40:8 وَأَدْخِلْهُمْ, 40:40 يَدْخُلُونَ, 40:46 أَدْخِلُوٓا۟, 40:60 سَيَدْخُلُونَ, 40:76 ٱدْخُلُوٓا۟

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

## ج ن ن (root_000266): 40:8 جَنَّٰتِ, 40:40 ٱلْجَنَّةَ

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

## و ع د (root_001662): 40:8 وَعَدتَّهُمْ, 40:28 يَعِدُكُمْ, 40:55 وَعْدَ, 40:77 وَعْدَ, 40:77 نَعِدُهُمْ

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

## ECHO ع د د (root_000989): for 40:8 وَعَدتَّهُمْ, 40:28 يَعِدُكُمْ, 40:31 وَعَادٍ, 40:55 وَعْدَ, 40:77 وَعْدَ, 40:77 نَعِدُهُمْ: withheld observed target; not identity

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

## ECHO ع و م (root_001063): for 40:8 وَعَدتَّهُمْ, 40:28 يَعِدُكُمْ, 40:55 وَعْدَ, 40:77 وَعْدَ, 40:77 نَعِدُهُمْ: withheld observed target; not identity

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

## ص ل ح (root_000876): 40:8 صَلَحَ, 40:40 صَٰلِحًا, 40:58 ٱلصَّٰلِحَٰتِ

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

## ء ب و (root_000007): 40:8 ءَابَآئِهِمْ

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ز و ج (root_000652): 40:8 وَأَزْوَٰجِهِمْ

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

## ذ ر ر (root_000511): 40:8 وَذُرِّيَّٰتِهِمْ

- **B001** küçük karıncalar ve bunlardan biri — küçük karıncalar; tekil biçimin çoğulu · küçük karıncalardan biri, en küçük karınca · küçük karınca adından türetilmiş erkek adı · küçük karınca adından türetilmiş erkek lakabı
  الذر صغار النمل الواحدة ذرة (maqayis)؛ الذر جمع ذرة وهي أصغر النمل (sihah)
- **B002** taneli ya da toz maddeyi serperek dağıtmak — tahıl, ilaç veya tuzu serperek dağıtmak · serpip dağıtma
  ذررت الملح والدواء (maqayis)؛ ذررت الحب والدواء والملح أذره ذرا فرقته (sihah)
- **B003** bilinen ince toz veya hoş kokulu madde — bilinen ince bir toz veya hoş kokulu madde · aynı maddenin dilsel varyantı olan ad · bu varyant adın çoğul biçimi
  الذريرة معروفة (maqayis)؛ الذرور بالفتح لغة في الذريرة (sihah)
- **B004** güneşin ince ışıkla doğması ya da bitkinin yerden çıkması — güneşin doğup ince, yayılmış ışığını göstermesi · güneşin doğuşu · gün doğduğu sürece · güneşin kenarı göründüğü sürece · bitkinin topraktan çıkması
  ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر (maqayis)؛ ما ذر شارق وما ذر قرن الشمس (maqayis)؛ ذر البقل إذا طلع من الأرض (maqayis;sihah)؛ ذرت الشمس تذر ذرورا طلعت (sihah)
- **B005** huysuzlaşmak veya öfkeyle yüz çevirmek — 
  ذارت الناقة وهي مذار إذا ساء خلقها (maqayis)؛ ذارت الناقة تذار مذارة وذرارا أي ساء خلقها وهي مذار (sihah)؛ في فلان ذرار أي إعراض غضبا كذرار الناقة (maqayis;sihah)

## ECHO  (): for 40:8 وَذُرِّيَّٰتِهِمْ: non-dominant observed target (1 occ.); not identity

- () no Turkish dictionary entry

## ح ك م (root_000348): 40:8 ٱلْحَكِيمُ, 40:12 فَٱلْحُكْمُ, 40:48 حَكَمَ

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

## س و ء (root_000755): 40:9 ٱلسَّيِّـَٔاتِ, 40:9 ٱلسَّيِّـَٔاتِ, 40:37 سُوٓءُ, 40:40 سَيِّئَةً, 40:45 سَيِّـَٔاتِ, 40:45 سُوٓءُ, 40:52 سُوٓءُ, 40:58 ٱلْمُسِىٓءُ

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

## ف و ز (root_001186): 40:9 ٱلْفَوْزُ

- **B001** iyiliğe erişip kötülükten kurtulma — iyiliğe erişip kötülükten kurtulma · kurtulup iyiliğe erişmek · kurtulup iyiliğe erişen kimse · bir şeyi ele geçirip onunla uzaklaşmak · Tanrı'nın ona bir şeyi alıp götürtmesi · kumarda kura payının sahibine çıkması
  الفوز الظفر بالخير والنجاة من الشر (ayn;sihah;tahdhib;mufradat)؛ فاز بالأمر إذا ذهب به وخلص (maqayis;sihah)؛ إذا خرج قدح قوم في القمار قيل قد فاز (ayn;tahdhib)
- **B002** ölüp dünyadan ayrılma — ölmek, yaşamını yitirmek
  فوز الرجل إذا مات (maqayis;sihah;tahdhib)؛ فوز الرجل إذا هلك (mufradat)؛ صار في مفازة بين الدنيا والآخرة (ayn;tahdhib)
- **B003** kurtuluş; susuz ve tehlikeli ıssız çöl — susuz çöle girip orada yol almak · cezadan kurtuluş · susuz, ölüm tehlikesi taşıyan ıssız çöl · kurtuluş veya kurtuluş yeri
  المفازة المنجاة (maqayis;ayn;sihah;tahdhib)؛ المفازة الفلاة التي لا ماء فيها (tahdhib)؛ سميت مفازة تفاؤلا بالسلامة والفوز (maqayis;sihah;mufradat)؛ سميت من فوز إذا هلك (maqayis;sihah;mufradat)؛ فوز الرجل تفويزا ركب المفازة ومضى فيها (ayn;tahdhib)
- **B004** askerî konak yerinde kurulan yapı veya direkli gölgelik — askerî konak yerinde kurulan yapı veya direkli gölgelik
  الفازة من أبنية الحزق وغيرها تبنى في العساكر (ayn;tahdhib)؛ الفازة مظلة تمد بعمود (sihah)

## ع ظ م (root_001029): 40:9 ٱلْعَظِيمُ

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

## ن د و (root_001486): 40:10 يُنَادَوْنَ, 40:32 ٱلتَّنَادِ

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

## ECHO ن د ي (root_001487): for 40:10 يُنَادَوْنَ, 40:32 ٱلتَّنَادِ: withheld observed target; not identity

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

## ECHO ن و د (root_001563): for 40:10 يُنَادَوْنَ, 40:32 ٱلتَّنَادِ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## م ق ت (root_001436): 40:10 لَمَقْتُ, 40:10 مَّقْتِكُمْ, 40:35 مَقْتًا

- **B001** çirkin davranışta bulunana duyulan en güçlü nefret — çirkin bir davranışta bulunana duyulan çok güçlü nefret · çirkin bir iş yaptığı için ondan güçlü biçimde nefret etmek · çirkin bir işi yüzünden insanların nefret ettiği biri durumuna gelmek · çirkin davranışı yüzünden nefret edilen · çirkin davranışı yüzünden nefret edilen
  كلمة واحدة تدل على شناءة وقبح (maqayis)؛ المقت بغض من أمر قبيح ركبه (ayn;tahdhib)؛ مقته مقتا أبغضه (sihah)؛ المقت البغض الشديد لمن تراه تعاطى القبيح (mufradat)؛ المقت أشد البغض (tahdhib)
- **B002** İslam öncesinde bir erkeğin babasının eşiyle evlenmesi — İslam öncesinde bir erkeğin babasının eşiyle evlenmesi · bir erkeğin babasının eşiyle evlenmesinden doğan çocuk
  ونكاح المقت كان في الجاهلية أن يتزوج الرجل امرأة أبيه (maqayis;sihah)؛ كان يقال له مقت (tahdhib)؛ كان المولود عليه يقال له المقتي (tahdhib)؛ وكان يسمى تزوج الرجل امرأة أبيه نكاح المقت (mufradat)

## ك ب ر (root_001281): 40:10 أَكْبَرُ, 40:12 ٱلْكَبِيرِ, 40:27 مُتَكَبِّرٍ, 40:35 كَبُرَ, 40:35 مُتَكَبِّرٍ, 40:47 ٱسْتَكْبَرُوٓا۟, 40:48 ٱسْتَكْبَرُوٓا۟, 40:56 كِبْرٌ, 40:57 أَكْبَرُ, 40:60 يَسْتَكْبِرُونَ, 40:76 ٱلْمُتَكَبِّرِينَ

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

## ن ف س (root_001533): 40:10 أَنفُسَكُمْ, 40:17 نَفْسٍۭ

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

## د ع و (root_000478): 40:10 تُدْعَوْنَ, 40:12 دُعِىَ, 40:14 فَٱدْعُوا۟, 40:20 يَدْعُونَ, 40:26 وَلْيَدْعُ, 40:41 أَدْعُوكُمْ, 40:41 وَتَدْعُونَنِىٓ, 40:42 تَدْعُونَنِى, 40:42 أَدْعُوكُمْ, 40:43 تَدْعُونَنِىٓ, 40:43 دَعْوَةٌ, 40:49 ٱدْعُوا۟, 40:50 فَٱدْعُوا۟, 40:50 دُعَٰٓؤُا۟, 40:60 ٱدْعُونِىٓ, 40:65 فَٱدْعُوهُ, 40:66 تَدْعُونَ, 40:74 نَّدْعُوا۟

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

## ECHO د ع ع (root_000477): for 40:10 تُدْعَوْنَ, 40:12 دُعِىَ, 40:14 فَٱدْعُوا۟, 40:20 يَدْعُونَ, 40:26 وَلْيَدْعُ, 40:41 أَدْعُوكُمْ, 40:41 وَتَدْعُونَنِىٓ, 40:42 تَدْعُونَنِى, 40:42 أَدْعُوكُمْ, 40:43 تَدْعُونَنِىٓ, 40:43 دَعْوَةٌ, 40:49 ٱدْعُوا۟, 40:50 فَٱدْعُوا۟, 40:50 دُعَٰٓؤُا۟, 40:60 ٱدْعُونِىٓ, 40:65 فَٱدْعُوهُ, 40:66 تَدْعُونَ, 40:74 نَّدْعُوا۟: withheld observed target; not identity

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

## ق و ل (root_001272): 40:11 قَالُوا۟, 40:24 فَقَالُوا۟, 40:25 قَالُوا۟, 40:26 وَقَالَ, 40:27 وَقَالَ, 40:28 وَقَالَ, 40:28 يَقُولَ, 40:29 قَالَ, 40:30 وَقَالَ, 40:34 قُلْتُمْ, 40:36 وَقَالَ, 40:38 وَقَالَ, 40:44 أَقُولُ, 40:47 فَيَقُولُ, 40:48 قَالَ, 40:49 وَقَالَ, 40:50 قَالُوٓا۟, 40:50 قَالُوا۟, 40:50 قَالُوا۟, 40:60 وَقَالَ, 40:66 قُلْ, 40:68 يَقُولُ, 40:73 قِيلَ, 40:74 قَالُوا۟, 40:84 قَالُوٓا۟

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

## ق ل ل (root_001251): 40:58 قَلِيلًا (also echo for 40:11 قَالُوا۟, 40:24 فَقَالُوا۟, 40:25 قَالُوا۟, 40:26 وَقَالَ, 40:27 وَقَالَ, 40:28 وَقَالَ, 40:28 يَقُولَ, 40:29 قَالَ, 40:30 وَقَالَ, 40:34 قُلْتُمْ, 40:36 وَقَالَ, 40:38 وَقَالَ, 40:44 أَقُولُ, 40:47 فَيَقُولُ, 40:48 قَالَ, 40:49 وَقَالَ, 40:50 قَالُوٓا۟, 40:50 قَالُوا۟, 40:50 قَالُوا۟, 40:60 وَقَالَ, 40:66 قُلْ, 40:68 يَقُولُ, 40:73 قِيلَ, 40:74 قَالُوا۟, 40:84 قَالُوٓا۟)

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

## م و ت (root_001454): 40:11 أَمَتَّنَا, 40:68 وَيُمِيتُ

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

## ث ن ي (root_000208): 40:11 ٱثْنَتَيْنِ, 40:11 ٱثْنَتَيْنِ

- **B001** iki olma, ikiye çıkarma veya ikili oluşturma — onu iki yaptı; yanına bir ikincisini kattı · ona ikinci oldu; yanında ikinci kişi olarak yer aldı · malının yarısını aldı · iki sayısı; birlikte bulunan iki öğe · iki kişiden veya iki öğeden biri · ikişer ikişer · iki çocuk doğurmuş ya da ikinci doğumunu yapmış kadın
  الاثنان في العدد معروفان؛ امرأة ثنى ولدت اثنين (maqayis)؛ ثنيته تثنية أي جعلته اثنين؛ اثنان من عدد المذكر واثنتان للمؤنث؛ هذا ثاني اثنين أي أحد الاثنين (sihah)؛ فلان ثاني اثنين أي هو أحدهما؛ وإذا فعل الرجل أمرا ثم ضم إليه أمرا آخر قيل ثنى بالأمر الثاني (tahdhib)؛ الثني والاثنان أصل لمتصرفات هذه الكلمة؛ كنت له ثانيا أو ضممت إليه ما صار به اثنين (mufradat)
- **B002** önderden sonra gelen veya alt sıradaki kişi — önderin ardından gelen, ondan aşağı sıradaki kişi · ailesinin en düşük konumdaki kişisi
  الثنى والثنيان الذي يكون بعد السيد كأنه ثانية (maqayis)؛ الثنيان بالضم الذي يكون دون السيد في المرتبة؛ فلان ثنية أهل بيته أي أرذلهم (sihah)؛ الذي يجيء ثانيا في السؤدد ولا يجيء أولا ثنى وثنيان وثني (tahdhib)؛ الثنيان الذي يثنى به إذا عد السادات؛ فلان ثنية أهل بيته كناية عن قصور منزلته (mufradat)
- **B003** bir şeyi ikinci kez ya da art arda yineleme — iki kez veya art arda yapılan iş · ödemenin ikinci kez alınmaması; ayrıca geri dönülmemesi yorumu · payı yeniden almak veya iyiliği yinelemek; ayrıca kesilen kura hayvanından artan paylar
  الثنى الأمر يعاد مرتين؛ لا ثنى في الصدقة يعني لا تؤخذ في السنة مرتين (maqayis)؛ الثني مقصور الأمر يعاد مرتين؛ لا ثني في الصدقة أي لا تؤخذ في السنة مرتين؛ مثنى الأيادي أن يأخذ القسم مرة بعد مرة (sihah)؛ الثنى إعادة الشيء مرة بعد مرة؛ مثنى الأيادي أن يعيد معروفه مرتين أو ثلاثا (tahdhib)؛ الثنى ما يعاد مرتين؛ لا ثنى في الصدقة أي لا تؤخذ في السنة مرتين (mufradat)
- **B004** tekrar okunan Kur'an bütünü ya da bölümleri — tekrar tekrar okunan Kur'an bütünü, ayetleri veya bölümleri · okunup yinelenen kitap parçası
  المثناة ما قرئ من الكتاب وكرر؛ سبعا من المثاني أراد أن قراءتها تثنى وتكرر (maqayis)؛ المثاني من القرآن ما كان أقل من المائتين؛ فاتحة الكتاب مثاني لأنها تثنى في كل ركعة؛ جميع القرآن مثاني (sihah)؛ سمى الله القرآن كله مثاني؛ وسمى فاتحة الكتاب مثاني؛ المثاني ما دون المئين (tahdhib)؛ سميت سور القرآن مثاني لأنها تثنى على مرور الأوقات وتكرر (mufradat)
- **B005** bükme, katlama ve yönünden çevirme — bir şeyi bükmek, eğmek veya katlamak · alıkoymak ya da yöneldiği yerden çevirmek · içindekini gizlemek için kapanmak · yanını çevirerek yüz çevirmek · bir şeyin katları ve kıvrımları · adı ilk sırada sayılırken parmakların büküldüğü kimse
  ثنيت الشيء إذا حنيته وعطفته وطويته؛ كل شيء عطفته فقد ثنيته؛ يثنون صدورهم أي يطوون ما فيها ويسترونه؛ إذا أراد الرجل وجها فصرفته عن وجهه قلت ثنيته ثنيا؛ ثني الثوب لما كف من أطرافه (tahdhib)؛ الثنى واحد أثناء الشيء أي تضاعيفه؛ في ثنى كتابي أي في طيه؛ ثنيت الشيء ثنيا عطفته؛ ثناه أي كفه؛ انثنى أي انعطف (sihah)؛ يقال للاوي الشيء قد ثناه؛ يثنون صدورهم؛ ثاني عطفه عبارة عن التنكر والإعراض؛ ثنيت الشيء أثنيه عقدته بثنايين (mufradat)
- **B006** dağ ya da vadi kıvrımındaki geçit — dağ veya vadinin kıvrımı ya da kesildiği yer · yokuş yolu veya çıkılarak aşılan dağ geçidi
  الثني من الوادي والجبل منعطفه؛ الثنية طريق العقبة (sihah)؛ مثاني الوادي ومحانيه معاطفه؛ كل عقبة مسلوكة ثنية وجمعها ثنايا وهي المدارج أيضا (tahdhib)؛ الثنية من الجبل ما يحتاج في قطعه وسلوكه إلى صعود وحدود فكأنه يثني السير (mufradat)
- **B007** iki uçlu bağlama ipi ve katlanmış dizgin ucu — saç veya yünden yapılan, iki ucuyla bağlanan ip · devenin iki ön ayağını tek ipin iki ucuyla bağladı · hayvan bağı ve benzeri katlanmış ip · dizginin burun bağındaki katlanmış ucu
  الثناية حبل من شعر أو صوف؛ المثناة طرف الزمام في الخشاش كأنه ثاني الزمام (maqayis)؛ الثناية حبل من شعر أو صوف؛ عقلت البعير بثنايين؛ ثني الحبل ما ثنيت (sihah)؛ مثنية بثنايين؛ يسمى ذلك الحبل الثناية؛ ثنيا الحبل طرفاه؛ الثناية حبل يشد طرفاه في قتب السانية (tahdhib)؛ ثنيت الشيء أثنيه عقدته بثنايين؛ المثناة ما ثني من طرف الزمام (mufradat)
- **B008** genel hükmün bir bölümünü kapsam dışında bırakma — genel sözün doğurduğu hükmün bir bölümünü kaldırma · yeminde konan dışarıda bırakma veya koşul kaydı · kesilen hayvanın sahibince ayrılan başı veya ayakları · inancı uğruna ölenlerin toplu çarpılmadan ayrı tutulduğu sözü
  الثنيا من الجزور الرأس أو غيره إذا استثناه صاحبه؛ معنى الاستثناء من قياس الباب (maqayis)؛ الثنيا بالضم الاسم من الاستثناء وكذلك الثنوي بالفتح (sihah)؛ حلف يمينا ليس فيها ثنيا ولا ثنوى ولا ثنية ولا مثنوية ولا استثناء؛ الثنيا المنهي عنها في البيع أن يستثنى منه شيء مجهول؛ الثنيا من الجزور الرأس والقوائم (tahdhib)؛ حلف يمينا فيها ثنيا وثنوى وثنية ومثنوية؛ الاستثناء إيراد لفظ يقتضي رفع بعض ما يوجبه عموم لفظ متقدم (mufradat)
- **B009** ön kesici diş ve bu dişle belirlenen hayvan yaş evresi — ön kesici dişlerden biri · ön kesici dişini dökmüş veya bu diş yaşına girmiş hayvan · hayvan ön kesici dişini döktü
  الثنية واحدة الثنايا من السن؛ الثني الذي يلقى ثنيته (sihah)؛ ثنايا الإنسان في فمه الأربع التي في مقدم فيه؛ البعير إذا استكمل الخامسة وطعن في السادسة فهو ثني؛ الثني من الغنم الذي استكمل الثانية ودخل في الثالثة (tahdhib)؛ الثنية من السن تشبيها بالثنية من الجبل في الهيئة والصلابة؛ الثني من الشاة ما دخل في السنة الثانية وما سقطت ثنيته من البعير (mufradat)
- **B010** iyi yönlerini yeniden anarak övme — iyi yönleri zaman zaman yeniden anılarak söylenen övgü · onu iyi sözlerle andı ve övdü
  أثنى عليه خيرا والاسم الثناء (sihah)؛ الثنوى والثناء ما يذكر في محامد الناس فيثنى حالا فحالا ذكره يقال أثني عليه؛ يصح أن يكون ذلك من الثناء (mufradat)
- **B011** hareket ederken bedeni, boynu veya kalçayı bükme — salınarak veya kurumlu biçimde yürümek · hayvanın boynunu koşarken bükmek · inerken kalçasını bükmek · hayvanın dizleri ve dirsekleri
  يقال للفارس إذا ثنى عنق دابته جاء ثاني العنان؛ جاء سابقا ثانيا إذا جاء وقد ثنى عنقه نشاطا؛ ثنى وركه فنزل (tahdhib)؛ تثنى في مشيته تأود (sihah)؛ تثنى في مشيته نحو تبختر (mufradat)

## ح ي ي (root_000383): 40:11 وَأَحْيَيْتَنَا, 40:25 وَٱسْتَحْيُوا۟, 40:39 ٱلْحَيَوٰةُ, 40:51 ٱلْحَيَوٰةِ, 40:65 ٱلْحَىُّ, 40:68 يُحْىِۦ

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

## ع ر ف (root_001002): 40:11 فَٱعْتَرَفْنَا

- **B001** kalıp sözlerde peş peşe gelme veya üst üste yığılma [kalıp] — birbiri ardından peş peşe gelme · at yelesi gibi art arda gönderilenler · katları üst üste konmuş yemek · çokluktan dolayı üst üste yığmak
  تتابع الشيء متصلا بعضه ببعض (maqayis)؛ جاءت القطا عرفا عرفا (maqayis;mufradat)؛ المرسلات عرفا متتابعة كعرف الفرس (sihah;tahdhib;mufradat)؛ خزير معرف بعضه على بعض (tahdhib)
- **B002** bir şeyin üzerindeki belirgin tepe, sırt veya üst çıkıntı — yele, ibik ya da belirgin yükselti · atın yelesini kırpmak · iki düzlük arasındaki yüksekçe arazi veya kum sırtı · yüksek yerler ya da yüksek bir duvar · denizin dalgalarının yükselmesi veya sıvının köpüklenmesi
  العرف عرف الفرس (maqayis;sihah;tahdhib;mufradat)؛ العرفة أرض منقادة مرتفعة (maqayis)؛ عرفت الفرس أي جززت عرفه (sihah)؛ الأعراف جمع عرف وهو كل عال مرتفع (tahdhib)؛ العرف والعرف الرمل المرتفع (sihah)؛ أعراف الرياح والسحاب أوائلها وأعاليها (tahdhib)
- **B003** bir iz veya belirti üzerinden tanıyıp ayırt etme — iz veya belirti üzerinden tanıma ve ayırt etme · bir şeyi bilip başkalarından ayırt etmek · bilinen ve ayırt edilmiş, bilinmez olmayan · topluluktakilerin birbirini tanıması · bildirme ve bilinir duruma getirme · birinin elindekini araştırıp öğrenmek · anlatının bir bölümünü bildirip bir bölümünü bırakmak · yerlerini önceden betimleyip tanınır kılmak
  عرف فلان فلانا عرفانا ومعرفة (maqayis)؛ عرفت الشيء معرفة وعرفانا (ayn;sihah;tahdhib)؛ المعرفة والعرفان إدراك الشيء بتفكر وتدبر لأثره (mufradat)؛ تعارف القوم أي عرف بعضهم بعضا (sihah;mufradat)؛ التعريف الإعلام (sihah)؛ تعرفت ما عند فلان أي تطلبت حتى عرفت (sihah)
- **B004** koku; ayrıca güzel kokulu duruma getirme — hoş ya da kötü olabilen koku · bir şeyi güzel kokulu duruma getirme · güzel kokuyla işlenmiş veya süslenmiş yemek · onlar için güzel kokulu ve süslü duruma getirmek · güzel kokuyu çok kullanmak ya da kullanmayı bırakmak
  العرف وهي الرائحة الطيبة (maqayis)؛ العرف الريح طيبة كانت أو منتنة (sihah)؛ العرف الرائحة تكون طيبة وغير طيبة (tahdhib)؛ التعريف التطييب (sihah)؛ عرفها لهم أي طيبها وزينها (mufradat)
- **B005** iyi sayılan ve benimsenen davranış veya iyilik — iyilik ve başkasına iyi davranma · düşünce veya bağlayıcı ölçülerce iyi sayılan davranış · bilinen ve beğenilen iş
  العرف المعروف (maqayis;ayn;tahdhib;mufradat)؛ المعروف ضد المنكر والعرف ضد النكر (sihah)؛ كل ما تعرفه النفس من الخير وتبسأ به وتطمئن إليه (tahdhib)؛ اسم لكل فعل يعرف بالعقل أو الشرع حسنه (mufradat)
- **B006** topluluğu tanıyan ve işlerini gözeten görevli — topluluğun işlerini bilen gözetmen veya temsilci · topluluk gözetmenliği görevi veya yetkisi
  العريف القيم بأمر قوم (maqayis;ayn)؛ العريف النقيب وهو دون الرئيس (sihah)؛ عريف القوم سيدهم (tahdhib)؛ العريف بمن يعرف الناس ويعرفهم (mufradat)
- **B007** belirli ibadet yeri, onun günü ve orada bulunup durma — belirli bir ibadet bölgesinin adı · insanların o ibadet yerinde durduğu belirli gün · belirli ibadet yerinde bulunup durma
  عرفات سميت بذلك لأن آدم وحواء تعارفا بها (maqayis)؛ يوم عرفة موقف الناس بعرفات (ayn)؛ عرفات موضع (sihah)؛ عرف الناس إذا شهدوا عرفة وهو المعرف للموقف بعرفات (tahdhib)؛ عرفات اسم لبقعة مخصوصة (mufradat)
- **B008** tanıyanı duyuruyla arama veya sorarak haber öğrenme [kalıp] — kayıp veya bulunan şeyi tanıyanı duyuruyla arama · insanlara bir haber öğrenmek için sormak · bulunan şeyi özelliklerinden tanıyan kişi
  التعريف تعريف الضالة واللقطة أن يقول من يعرف هذا (maqayis)؛ التعريف أن تصيب شيئا فتعرفه إذا ناديت من يعرف هذا (ayn)؛ التعريف إنشاد الضالة (sihah)؛ اعترفت القوم سألتهم (sihah;tahdhib)؛ من يعترفها فمعناه معرفته إياها بصفتها (tahdhib)
- **B009** bir şeyi veya suçu açıkça kabul edip üstlenme — bir şeyi veya suçu açıkça kabul etme · kişinin kendi suçunu kabul etmesi · kimsenin beni yenebileceğini kabul etmem
  اعترف بالشيء إذا أقر (maqayis)؛ الاعتراف الإقرار بالذنب والذل والمهانة والرضى به (ayn)؛ المعرف الاسم من الاعتراف وله علي ألف عرفا أي اعترافا (sihah)؛ عرف الرجل ذنبه إذا أقر به (tahdhib)؛ اعترف فلان إذا ذل وانقاد (tahdhib)
- **B010** yüklenilen duruma dayanıp içten sakinleşme — üzerine yüklenene dayanıp sakinleşen ruh · sıkıntı karşısında sabırlı kişi · sabır ve dayanma
  النفس عروف إذا حملت على أمر فباءت به أي اطمأنت (maqayis)؛ النفس عروف إذا حملت على أمر بسأت به أي اطمأنت (ayn)؛ العارف الصبور والعروف مثله (sihah)؛ رجل عارف أي صبور ونفس عروف صبور (tahdhib)؛ العرف بالكسر الصبر (tahdhib)
- **B011** avuç içinin açık bölümünde çıkan yara veya çıban — avuç içinin açık renkli bölümünde çıkan yara
  العرفة قرحة تخرج في بياض الكف (sihah;tahdhib)؛ عرف الرجال فهو معروف أي خرجت به تلك القرحة (sihah)
- **B012** gizli haber iddiacısı, hekim veya işinin uzmanı — gizli haber bildiğini öne süren kişi, hekim veya işinin uzmanı
  العراف الكاهن والطبيب (sihah)؛ للحازي عراف وللقناقن عراف وللطبيب عراف (tahdhib)؛ العراف كالكاهن إلا أن العراف يختص بمن يخبر بالأحوال المستقبلة (mufradat)
- **B013** yüzü veya araziyi tanıtan belirgin görünür bölümler — yüzler ve yüzün görünen bölümleri · arazinin tanınan ve görünür kısımları
  امرأة حسنة المعارف أي الوجه وما يظهر منها (sihah)؛ المعارف الوجوه والمعرف واحد (tahdhib)؛ معارف الأرض ما عرف منها (tahdhib)؛ أصبت عرفه أي خده (mufradat)
- **B014** kötülüğe hazırlanıp sert ve saldırgan bir tavır alma [kalıp] — kötülüğe hazırlanıp sert bir tavır almak
  اعرورف الرجل أي تهيأ للشر (sihah)؛ اعرورف فلان للشر كقولك اجثأل وتشزن (tahdhib)

## خ ر ج (root_000400): 40:11 خُرُوجٍ, 40:67 يُخْرِجُكُمْ

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

## و ح د (root_001631): 40:12 وَحْدَهُۥ, 40:16 ٱلْوَٰحِدِ, 40:84 وَحْدَهُۥ

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

## ش ر ك (root_000791): 40:12 يُشْرَكْ, 40:42 وَأُشْرِكَ, 40:73 تُشْرِكُونَ, 40:84 مُشْرِكِينَ

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

## ع ل و (root_001042): 40:12 ٱلْعَلِىِّ

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

## ر ء ي (root_000531): 40:13 يُرِيكُمْ, 40:29 أُرِيكُمْ, 40:29 أَرَىٰ, 40:69 تَرَ, 40:77 نُرِيَنَّكَ, 40:81 وَيُرِيكُمْ, 40:84 رَأَوْا۟, 40:85 رَأَوْا۟

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

## ECHO ر و ي (root_000615): for 40:13 يُرِيكُمْ, 40:29 أُرِيكُمْ, 40:29 أَرَىٰ, 40:69 تَرَ, 40:77 نُرِيَنَّكَ, 40:81 وَيُرِيكُمْ, 40:84 رَأَوْا۟, 40:85 رَأَوْا۟: withheld observed target; not identity

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

## س م و (root_000745): 40:13 ٱلسَّمَآءِ, 40:37 ٱلسَّمَٰوَٰتِ, 40:57 ٱلسَّمَٰوَٰتِ, 40:64 وَٱلسَّمَآءَ, 40:67 مُّسَمًّى

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

## ECHO و س م (root_001650): for 40:13 ٱلسَّمَآءِ, 40:37 ٱلسَّمَٰوَٰتِ, 40:57 ٱلسَّمَٰوَٰتِ, 40:64 وَٱلسَّمَآءَ, 40:67 مُّسَمًّى: withheld observed target; not identity

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

## ر ز ق (root_000560): 40:13 رِزْقًا, 40:40 يُرْزَقُونَ, 40:64 وَرَزَقَكُم

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

## ذ ك ر (root_000516): 40:13 يَتَذَكَّرُ, 40:40 ذَكَرٍ, 40:44 فَسَتَذْكُرُونَ, 40:54 وَذِكْرَىٰ, 40:58 تَتَذَكَّرُونَ

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

## ن و ب (root_001562): 40:13 يُنِيبُ

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

## ECHO ن ي ب (root_001571): for 40:13 يُنِيبُ: withheld observed target; not identity

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

## ECHO ن ب ء (root_001464): for 40:13 يُنِيبُ: withheld observed target; not identity

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

## خ ل ص (root_000430): 40:14 مُخْلِصِينَ, 40:65 مُخْلِصِينَ

- **B001** arındırıp durultma — karışandan arınıp durulmak · bulanıklıktan ve kirden arıtmak · karışanı giderilmiş, duru
  أصل واحد مطرد وهو تنقية الشيء وتهذيبه (maqayis)؛ خلص الشيء خلوصا (ayn;tahdhib)؛ صفيته من كدر أو درن (jamhara)؛ صار خالصا (sihah)؛ الخالص هو ما زال عنه شوبه بعد أن كان فيه (mufradat)
- **B002** takıldığı bağdan kurtulma — takıldığı şeyden kurtulmak · takıldığı şeyden kurtarmak · kaçıp gitmek
  خلصته من كذا وخلص هو (maqayis)؛ كان قد نشب ثم نجا وسلم (ayn;tahdhib)؛ تخلص الظبي والطائر من الحبالة إذا أفلت منها (jamhara)؛ نجيته فتخلص (sihah)؛ التخليص التنحية من كل منشب (tahdhib)؛ خلبص الرجل إذا فر والباء فيه زائدة وهو من خلص (maqayis)
- **B003** hedefe ulaşıp varma [kalıp] — birine ulaşıp varmak
  خلصت إليه وصلت إليه (ayn)؛ خلص إليه الشيء وصل (sihah)؛ خلص فلان إلى فلان أي وصل إليه (tahdhib)
- **B004** özgüleme ve başkalarından ayrılma — yalnız sana ayrılmış · kendisi için seçip ayırmak · ötekilerden ayrılıp gizlice konuşmak
  هذا الشيء خالصة لك أي خالص لك خاصة (ayn;tahdhib)؛ خذ هذه خالصة لك (jamhara)؛ استخلصه لنفسه أي استخصه (sihah)؛ خلصوا نجيا معناه تميزوا عن الناس (tahdhib)؛ انفردوا خالصين عن غيرهم (mufradat)؛ خلصت للمؤمنين في الآخرة ولا يشركهم فيها كافر (tahdhib)
- **B005** inancı yalnız Tanrı'ya yöneltme — inancı yalnız Tanrı'ya yöneltme ve gösterişten kaçınma · inancını yalnız Tanrı'ya yöneltmek · Tanrı'nın birliğini bildiren tanıklık sözü · Tanrı'nın birliğini anlatan bölüm
  الإخلاص التوحيد لله خالصا (ayn;tahdhib)؛ أخلصت لله ديني أمحضته (ayn)؛ شهادة الإخلاص شهادة أن لا إله إلا الله (jamhara)؛ الإخلاص في الطاعة ترك الرياء (sihah)؛ أخلصوا دينهم لله (mufradat)؛ حقيقة الإخلاص التبري عن كل ما دون الله تعالى (mufradat)
- **B006** Tanrı'nın kişileri seçip kendine ayırması — onları seçip yalnız kendine ayırdı
  المخلَصون المختارون (ayn;tahdhib)؛ إنا أخلصناهم بخالصة ذكرى الدار (tahdhib)؛ معنى أخلصناهم جعلناهم لنا خالصين (tahdhib)
- **B007** içten dostluk ve özel yakınlık — yakın dostlarım ve özel çevrem · sevgiyi içten ve katışıksız kılmak · ilişkide içten ve dürüst davranmak
  خالصتي وخلصاني وخلصائي أي أخلائي (ayn)؛ أخلص الرجل الود إخلاصا (jamhara)؛ فلان من خلصاء فلان ومن خلصانه إذا كان من خاصته (jamhara)؛ خالصه في العشرة أي صافاه (sihah)؛ خلصت مودتهما (tahdhib)
- **B008** geleneksel yağ ayırma, kalıntı ve hurma şurubu adları — yağı ayrıştırmak için katılan hurma veya kavrulmuş un · pişirmeden sonra ayrılan yağ özü · kabın dibinde kalan tortulu artık · hurmadan yapılan koyu şurup · yağı süt ve tortudan ayırmak için katılan madde · yağın dibinde kalan tortu
  خلاصة السمن ما ألقي فيه من تمر أو سويق ليخلص به (maqayis;jamhara)؛ الخلاص زبد اللبن يستخلص منه (ayn)؛ خلاصة السمن ما خلص منه (sihah)؛ الخلاص رب يتخذ من التمر (ayn;tahdhib)؛ الثفل الذي يكون أسفل هو الخلوص (sihah;tahdhib)؛ الخلاصة ما بقي في أسفل البرمة من الخلاص وغيره (tahdhib)

## د ي ن (root_000504): 40:14 ٱلدِّينَ, 40:26 دِينَكُمْ, 40:65 ٱلدِّينَ

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

## ك ر ه (root_001295): 40:14 كَرِهَ

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

## ر ف ع (root_000582): 40:15 رَفِيعُ

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

## د ر ج (root_000468): 40:15 ٱلدَّرَجَٰتِ

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

## ل ق ي (root_001372): 40:15 يُلْقِى, 40:15 ٱلتَّلَاقِ

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

## ر و ح (root_000609): 40:15 ٱلرُّوحَ

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

## ء م ر (root_000051): 40:15 أَمْرِهِۦ, 40:44 أَمْرِىٓ, 40:66 وَأُمِرْتُ, 40:68 أَمْرًا, 40:78 أَمْرُ

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

## ع ب د (root_000973): 40:15 عِبَادِهِۦ, 40:31 لِّلْعِبَادِ, 40:44 بِٱلْعِبَادِ, 40:48 ٱلْعِبَادِ, 40:60 عِبَادَتِى, 40:66 أَعْبُدَ, 40:85 عِبَادِهِۦ

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

## ن ذ ر (root_001488): 40:15 لِيُنذِرَ, 40:18 وَأَنذِرْهُمْ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ي و م (root_001700): 40:15 يَوْمَ, 40:16 يَوْمَ, 40:16 ٱلْيَوْمَ, 40:17 ٱلْيَوْمَ, 40:17 ٱلْيَوْمَ, 40:18 يَوْمَ, 40:27 بِيَوْمِ, 40:29 ٱلْيَوْمَ, 40:30 يَوْمِ, 40:32 يَوْمَ, 40:33 يَوْمَ, 40:46 وَيَوْمَ, 40:49 يَوْمًا, 40:51 وَيَوْمَ, 40:52 يَوْمَ

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

## ب ر ز (root_000105): 40:16 بَٰرِزُونَ

- **B001** görünür hâle gelme veya getirme — gizlilikten çıkıp görünmek · görünür kılmak, ortaya çıkarmak · bir şeyi gösterip belirginleştirmek · görünür; kitap için yayımlanmış · yayımlanmış veya görünür durumdaki kitap
  أصل واحد وهو ظهور الشيء وبدوه؛ برز الشيء فهو بارز؛ أبرزت الشيء أبرزه إبرازا؛ المبروز الظاهر؛ وقال قوم المبروز المنشور (maqayis)؛ برز فلان أي ظهر بعد الخفاء؛ أبرزت الكتاب والشيء أي أظهرته؛ كتاب مبروز مبرز أي منشور (ayn)؛ برزت الشيء تبريزا أي أظهرته وبينته؛ كتاب مبروز أي منشور (sihah)؛ برز أي هو منكشف الشأن ظاهره؛ برز مخفف فمعناه ظهر بعد الخفاء (tahdhib)؛ أن يظهر بذاته؛ أن ينكشف عنه ما كان مستورا منه (mufradat)
- **B002** geniş ve açık arazi — geniş, açık ve örtüsüz arazi · açık araziye çıkmak veya orada bulunmak
  البراز المتسع من الأرض لأنه باد ليس بغائط ولا دحل ولا هوة (maqayis)؛ البراز المكان الفضاء من الأرض البعيد الواسع؛ تبرز فلان خرج إلى البراز (ayn)؛ برز الرجل يبرز بروزا خرج؛ البراز بالفتح الفضاء الواسع؛ الموضع الذي ليس به خمر من شجر ولا غيره؛ تبرز الرجل أي خرج إلى البراز للحاجة (sihah)؛ البراز المكان الفضاء من الأرض البعيد الواسع؛ خرج الإنسان إلى ذلك الموضع قيل قد برز (tahdhib)؛ البراز الفضاء؛ برز حصل في براز (mufradat)
- **B003** saflardan çıkıp teke tek dövüşme — savaşta teke tek çarpışma · rakibinin karşısına savaşmak için çıkmak · karşılıklı olarak saftan çıkıp teke tek dövüşmek
  انفراد الشيء من أمثاله نحو تبارز الفارسين؛ كل واحد منهما ينفرد عن جماعته إلى صاحبه (maqayis)؛ البراز المبارزة من القرنين في الحرب؛ تبارزا؛ بارز القرن مبارزة وبرازا (ayn)؛ البراز المبارزة في الحرب (sihah)؛ المبارزة الحرب؛ البراز أخذ من هذا؛ تبارز القرنان (tahdhib)؛ المبارزة للقتال وهي الظهور من الصف (mufradat)
- **B004** yarışta veya erdemde öne geçme — arkadaşlarını geride bırakmak veya onlardan üstün olmak
  برز الرجل والفرس إذا سبقا وهو من الباب (maqayis)؛ إذا تسابقت الخيل قيل لسابقها قد برز عليها (ayn)؛ برز الرجل أيضا فاق على أصحابه؛ وكذلك الفرس إذا سبق (sihah)؛ إذا تسابقت الخيل قيل لسابقها قد برز عليها (tahdhib)؛ أن يظهر بفضله وهو أن يسبق في فعل محمود (mufradat)
- **B005** insanlar önünde saygın, güvenilir ve iffetli kimse — açık tavırlı, temiz karakterli ve iffetli · insanlar önünde saygın, görüşüne güvenilen ve iffetli kadın
  امرأة برزة أي جليلة تبرز وتجلس بفناء بيتها؛ رجل برز وامرأة برزة يوصفان بالجهارة والعقل؛ رجل برز طاهر عفيف (maqayis)؛ رجل برز أي طاهر الخلق عفيف؛ امرأة برزة موثوق برأيها وفضلها وعفافها (ayn)؛ امرأة برزة أي جليلة تبرز وتجلس للناس؛ رجل برز وامرأة برزة يوصفان بالجهارة والعقل؛ رجل برز أي عفيف (sihah)؛ البرزة من النساء الجليلة التي تظهر للناس ويجلس إليها القوم؛ رجل برز طاهر الخلق عفيف؛ امرأة برزة موثوق برأيها وعفافها (tahdhib)؛ امرأة برزة عفيفة لأن رفعتها بالعفة (mufradat)
- **B006** büyük abdestini yapma örtmecesi — büyük abdestini yapmak · dışkı · ayakyolu, ihtiyaç giderme yeri
  تبرز في التغوط كناية عنه؛ أي خرج إلى براز من الأرض (ayn)؛ البراز كناية عن ثفل الغذاء وهو الغائط؛ المبرز المتوضأ؛ تبرز الرجل أي خرج إلى البراز للحاجة (sihah)؛ قيل في التغوط تبرز فلان كناية أي خرج إلى براز من الأرض (tahdhib)؛ يقال تبرز فلان كناية عن التغوط (mufradat)
- **B007** seyahate çıkmaya kesin karar verme — seyahate çıkmaya kesin karar vermek
  أبرز الرجل إذا عزم على السفر (tahdhib)
- **B008** iki şeyi ayıran engel — iki şeyin arasındaki ayırıcı engel
  البرزخ الحائل بين الشيئين؛ كأن بينهما برازا أي متسعا من الأرض؛ الخاء زائدة (maqayis)
- **B009** belirli bir aslan adı — aslan; köken açıklamasında rakibinin karşısına çıkan aslan
  الهزبر الأسد؛ زيدت فيه الهاء؛ من برز أي إنه مبارز (maqayis)

## خ ف ي (root_000428): 40:16 يَخْفَىٰ, 40:19 تُخْفِى

- **B001** gizli kalma ya da gizleme — şey gizli kaldı, görünmedi · şeyi ve onun haberini sakladı · şeyi gizledi ve sakladı · gizlilik ve saklılık hâli · gizlilik, görünmezlik · gizlenip gözden uzaklaştı · bir aktarıma göre gizlendi · gizlenen kişi · onunla gizlice buluştum
  خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته (maqayis); أخفيت الصوت إخفاء وفعله اللازم اختفى والخافية ضد العلانية ولقيته خفيا أي سرا (ayn); خفيت الشئ أخفيه كتمته وأخفيت الشئ سترته وكتمته واستخفيت منك أي تواريت (sihah); خفي الشيء خفية استتر وأخفيته أوليته خفاء وذلك إذا سترته ويقابل به الإبداء والإعلان (mufradat)
- **B002** örten ya da gizli kalan şey — gizli ya da örtülü şey · örtü veya örten giysi · kanadın iç tüyleri; hurma göbeğine yakın yapraklar · görünmeyen varlık · kanadın iç tüylerinden biri · bedende gizlendiğine inanılan görünmeyen varlık · kuyu, koruluk veya gizli yer · bu adla anılan iki aslan yatağı · su tulumunun üzerine atılan örtüler · kadının sesi ile yerdeki ayak izi
  الخوافي سعفات يلين قلب النخلة والخافي الجن (maqayis); الخفا مقصور الشيء الخافي والموضع الخافي والخفاء رداء تلبسه المرأة وكل شيء غطيت به شيئا فهو خفاء والخفية غيضة والخفية بئر والخوافي من الجناحين (ayn); الخافي الجن والخافية ما يخفى في البدن من الجن والخفية الركية والخوافى ما دون الريشات العشر والخوافي من السعف (sihah); الخفاء ما يستر به كالغطاء والخوافي جمع خافية وهي ما دون القوادم من الريش (mufradat)
- **B003** gizliliği giderip açığa çıkarma — gizli olan açığa çıktı, sır belli oldu · şeyi açığa çıkardı · şeyin gizliliğini giderip onu gösterdi · yağmur fareleri yuvalarından çıkardı · gizli şeyi çıkarıp ortaya koydu · kefenleri çıkardığı için mezar soyguncusu
  الأصل الآخر الإظهار وخفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن (maqayis); الخفا إخراجك الشيء الخفي وإظهاركه وخفيت الخرزة من تحت التراب أخفيها خفيا (ayn); وخفيته أيضا أظهرته وهو من الأضداد وخفى المطر الفأر إذا أخرجهن واستخفيت الشئ أي استخرجته وأخفيها أي أزيل عنها خفاءها (sihah); وخفيته أزلت خفاه وذلك إذا أظهرته (mufradat)
- **B004** belli belirsiz şimşek çakması — şimşek belli belirsiz ve zayıfça çaktı
  خفا البرق خفوا إذا لمع ويكون ذلك في أدنى ضعف (maqayis); وخفا البرق يخفو خفوا ويخفى خفيا أي ظهر من الغيم (ayn); خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا (jamhara); وخفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم (sihah)

## م ل ك (root_001444): 40:16 ٱلْمُلْكُ, 40:29 ٱلْمُلْكُ

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

## ق ه ر (root_001266): 40:16 ٱلْقَهَّارِ

- **B001** üstün gelerek boyun eğdirme ve zorla alma — ona üstün geldi ve onu boyun eğdirdi · üstün gelme ve boyun eğdirme · üstün gelen ve boyun eğdiren · karşı konulamaz biçimde üstün gelen · başına onu ezecek birini getirdi · onu yenik ve ezilmiş durumda buldu · yenik ve aşağılanmış duruma düştü · onayı dışında zorla aldı · zorunlu bırakarak aldı
  تدل على غلبة وعلو (maqayis)؛ القاهر الغالب (maqayis)؛ القهر الغلبة والأخذ من فوق (ayn;tahdhib)؛ أخذهم قهرا أي من غير رضاهم (ayn)؛ أخذوا دون رضاهم على سبيل الغلبة (tahdhib)؛ الغلبة والتذليل معا (mufradat)؛ فلا تقهر أي لا تذلل (mufradat)؛ أقهره سلط عليه من يقهره (mufradat)؛ أقهرته وجدته مقهورا (sihah)؛ أقهر الرجل إذا صير في حال يذل فيها (maqayis)
- **B002** etin ateşte suyunu salıp değişmesi [kalıp] — eti ateşte suyunu salıp değişinceye kadar pişirdi
  قهر اللحم طبخ حتى يسيل ماؤه (maqayis)؛ قهر اللحم إذا أخذته النار وسال ماؤه (sihah)؛ قهرنا اللحم وذلك أول ما تأخذ فيه النار فيسيل ماؤه (tahdhib)؛ ضبحته النار وضبته وقهرته إذا غيرته (tahdhib)
- **B003** kızgın taşla kaynatılıp un katılan süt yemeği — kızgın taşla kaynatılıp un katılan süt yemeği
  القهيرة محض يلقى فيه الرضف فإذا غلى ذر عليه الدقيق وسيط به ثم أكل (tahdhib)
- **B004** sert ya da pürüzsüz öğütme taşı — sert ya da pürüzsüz taş · bir şeyi ezmekte kullanılan taşlar · aynı kümedeki daha büyük taş
  القهقر الحجر الصلب (maqayis)؛ القهقر الحجر (ayn)؛ القهقرى بتشديد الراء الحجر الصلب (sihah)؛ القهقر الحجر الأملس (tahdhib)؛ القهقر والقهاقر وهو ما سهكت به الشيء والقهر أعظم منه (tahdhib)
- **B005** topukları üzerinde geriye çekilme — geriye doğru gitme; topukları üzerinde geri çekilme · topukları üzerinde geriye gitti
  رجع القهقرى إذا رجع إلى خلفه (maqayis)؛ القهقرى الرجوع إلى خلف (sihah)؛ القهقرى التراجع إلى الخلف (tahdhib)؛ رجع فلان القهقرى إذا رجع على عقبه (tahdhib)؛ القهقرى المشي إلى خلف (mufradat)؛ معناه الارتداد عما كانوا عليه (tahdhib)
- **B006** kapta istiflenmiş bol yiyecek — kapta istiflenmiş bol yiyecek
  القهقر بالتخفيف الطعام الكثير الذي في الأوعية منضودا (tahdhib)؛ القهقر الطعام الكثير الذي في العيبة (tahdhib)
- **B007** türü belirtilmeyen küçük hayvan — türü belirtilmeyen küçük bir hayvan
  القهيقران دويبة (tahdhib)

## ج ز ي (root_000244): 40:17 تُجْزَىٰ, 40:40 يُجْزَىٰٓ

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

## ECHO ج ز ز (root_000242): for 40:17 تُجْزَىٰ, 40:40 يُجْزَىٰٓ: withheld observed target; not identity

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

## ك س ب (root_001296): 40:17 كَسَبَتْ, 40:82 يَكْسِبُونَ

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

## ظ ل م (root_000967): 40:17 ظُلْمَ, 40:18 لِلظَّٰلِمِينَ, 40:31 ظُلْمًا, 40:52 ٱلظَّٰلِمِينَ

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

## س ر ع (root_000698): 40:17 سَرِيعُ

- **B001** hızlı olma ve hızlanma — hız · hızlı oldu · hızlı · suyun hızlı akışı veya yağmurun hızla boşalması · hızla, öne atılarak · çabuk, çabuk! · yol alırken hızlandı · yürümeyi ve yazmayı hızlandırdı · ona doğru hızla ilerledi · topluluğun binekleri hızlı oldu · ona doğru çabucak yöneldi · ona doğru hep birlikte hızlandılar · kötülüğe düşünmeden atıldı · iyiliğe ya da kötülüğe hızla yönelen · hesabı çabuk gören · cezayı çabuk veren
  أصل صحيح يدل على خلاف البطء (maqayis)؛ السرع من السرعة في جري الماء وانهمار المطر (ayn)؛ السرعة نقيض البطء وأسرع في السير والمسارعة إلى الشيء (sihah)؛ سرع الرجل إذا أسرع في كلامه وفعاله وأسرع المشي والكتابة وسارع بمعنى أسرع (tahdhib)؛ السرعة ضد البطء ويستعمل في الأجسام والأفعال (mufradat)
- **B002** önden giden hızlı kişiler — topluluğun önden giden hızlı kişileri
  سرعان الناس أوائلهم الذين يتقدمون (maqayis)؛ سرغان الناس أوائلهم (sihah)؛ سرعان الناس أوائلهم وسرعان الناس محرك لمن يسرع من العسكر (tahdhib)؛ سرعان القوم أوائلهم السراع (mufradat)
- **B003** ne çabuk oldu! [kalıp] — çıkışı ne kadar çabuk! · bunu ne çabuk yaptın! · çıkışı ne çabuk! · bu ne çabuk oldu! · bu ne çabuk oldu!
  لسرعان ما صنعت كذا أي ما أسرع ما صنعته (maqayis)؛ سرعان ذا خروجا ولسرعان ما صنعت كذا أي ما أسرع (sihah)؛ سرعان ذا خروجا ولسرع ذا خروجا (tahdhib)؛ سرعان ذا إهالة مبني من سرع (mufradat)
- **B004** körpe dal; narin genç — bu yıl çıkmış körpe asma dalı; taze dal · körpe asma dalları · tek bir körpe asma dalı · taze ve yumuşak dal; yumuşak yapılı genç · yumuşak ve narin kadın · körpe ve yumuşak bir gençlik
  السرع من قضبان الكرم أسرع ما يطلع منه ومثله السرعرع ثم يشبه به الإنسان الرطيب الناعم (maqayis)؛ السرع القضيب من قضبان الكرم الغض لسنته وكل قضيب رطب سرع وسرعرع والسرعرع الشاب الناعم البدن (sihah)؛ السرع قضيب سنة من قضبان الكرم ويقال لكل قضيب ما دام رطبا غضا سرعرع والسرعرعة من النساء اللينة الناعمة (tahdhib)
- **B005** bitkide veya kumda yaşayan çizgili kurtçuk — bitkide veya kumda yaşayan, kelebeğe dönüşen kırmızı tırtıl · kırmızı ya da kırmızı başlı beyaz kurtçuk · kumda veya bitkide yaşayan çizgili kurtçuklar
  اليسروع والأسروع دودة حمراء تكون في البقل ثم تنسلخ فتصير فراشة والأسروع دود حمر الرؤوس بيض الجسد تكون في الرمل (sihah)؛ أساريع الرمل ديدان تظهر في الربيع مخططة بسواد وحمرة ويشبه بها بنان العذارى (tahdhib)
- **B006** özellikle yay üzerindeki çizgi ve yollar — yay üzerindeki çizgi ve yollar · çizgiler ve yol biçimli izler
  الأسروع واحد أساريع القوس وهي خطوط فيها وطرائق (sihah)؛ الأساريع الطرق التي في القوس واحدتها طرقة والأساريع الطرائق (tahdhib)
- **B007** asma dibinden çıkan ekşi körpe filiz [kalıp] — asma dibinden çıkan, bazen ekşi ve yaşken yenen filizler
  الأساريع شكر تخرج في أصل الحبلة (sihah)؛ أساريع العنب شكر تخرج في أصول الحبلة وربما أكلت حامضة رطبة (tahdhib)
- **B008** etten ayrılıp yay kirişi yapılan sırt kirişi — sırtın iki yanından alınıp etten temizlenen ve yay kirişi yapılan sinirler · etten temizlenip yay kirişi yapılmak üzere bükülen sırt sinirleri · bu sırt sinirlerinden tek bir parça
  سرعان عقب المتنين شبه الخضل تخلص من اللحم ثم تفتل أوتارا للقسي يقال لها السرعان وواحدة سرعان العقب سرعانة (tahdhib)
- **B009** büyük kum tümseği — büyük kum tümseği veya kum tepesi · büyük kum tümsekleri
  السروعة النبكة العظيمة من الرمل وتجمع سروعات وسراوع والسروعة الرابية من الرمل (tahdhib)
- **B010** ceylan bacağının iç kirişi [kalıp] — ceylanın ön ve arka bacaklarının iç yanında uzanan kiriş
  أسروع الظبي عصبة تستبطن يده ورجله (tahdhib)
- **B011** çalı ateşine verilen lakap — belirli bir çalıda yanan ateşe verilen lakap
  أبو سريع هو كنية النار في العرفج (tahdhib)

## ح س ب (root_000318): 40:17 ٱلْحِسَابِ, 40:27 ٱلْحِسَابِ, 40:40 حِسَابٍ

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

## ء ز ف (root_000029): 40:18 ٱلْءَازِفَةِ

- **B001** yaklaşma ve vaktin daralması — yaklaşmak; vakti yaklaşmak · yaklaşan son gün · yakınlık yüzünden zaman darlığı
  أزف الرحيل إذا اقترب ودنا (maqayis)؛ أزف الشيء يأزف أزفا وأزوفا والآزفة القيامة (ayn)؛ أزف الترحل يأزف أزفا أي دنا وأفد (sihah)؛ كل شيء اقترب فقد أزف أزفا ودنت القيامة (tahdhib)؛ أزفت الآزفة أي دنت القيامة والأزف ضيق الوقت (mufradat)
- **B002** mekansal yakınlık ve sıkışıklık — dar mekan · birbirine yakın adımlar · kısa ve sık yapılı erkek · topluluk birbirine yaklaştı · dar geçitlerdeki kirli yerler · dar geçitteki kirli yer
  رجل متآزف أي قصير متقارب الخلق وتآزف القوم إذا تدانى بعضهم من بعض والمآزف المواضع القذرة لا يكاد يكون إلا في مضيق (maqayis)؛ المتآزف المكان الضيق والخطو المتقارب والقصير من الرجال (ayn)؛ المتآزف القصير وهو المتدانى (sihah)؛ المتآزف المكان الضيق والخطو المتقارب والقصير من الرجال (tahdhib)
- **B003** acele ettirme veya acele etme — beni acele ettirdi · başkasını acele ettirme · adam acele etti · aceleci kimse
  آزفني فلان أي أعجلني يؤزف إيزافا (maqayis)؛ أزف الرجل أي عجل فهو آزف (sihah)

## ح ن ج ر (root_000360): 40:18 ٱلْحَنَاجِرِ

- **B001** gırtlağın iç boşluğu veya dıştan görülen üst kısmı — gırtlak; boğaz borusunun iç boşluğu veya dıştan görülen gırtlak çıkıntısının üst kısmı · gırtlaklar · gırtlak
  الحَنْجَرة جوف الحلقوم والحنجور الحنجرة (ayn)؛ جمع حنجرة وهي رأس الغلصمة من خارج (mufradat)

## ك ظ م (root_001303): 40:18 كَٰظِمِينَ

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

## ح م م (root_000001): 40:18 حَمِيمٍ, 40:72 ٱلْحَمِيمِ

- **B001** kömürleşme ve kara is — kömür, yanık kül · bir kömür parçası · kara duman veya kapkara şey · yüzünü isle kararttı · yavrunun tüyleri çıktı · tıraştan sonra başı karardı · siyah, kara renkli · kapkara şey veya kara renkli bitki · siyahlık, kara renk
  الحمم الفحم؛ اليحموم الدخان؛ حممته إذا سخمت وجهه بالسخام (maqayis)؛ الحمم أيضا الفحم البارد؛ جارية حمة أي سوداء؛ اليحموم الدخان (ayn)؛ الحمحم الشديد السواد؛ الأحم الأسود؛ الحمم الرماد والفحم؛ اليحموم أيضا الدخان (sihah)؛ الحمم الفحم البارد؛ اليحموم الشديد السواد؛ حممت وجه الرجل إذا سودته بالحمم؛ حمم رأسه بعد الحلق إذا اسود (tahdhib)
- **B002** sıcak su ve onun kullanımı — sıcak veya kaynar su · sıcak su kaynağı · suyu ısıttı · sıcak suyla yıkandı; sonradan genel olarak yıkandı · ısıtılmış su
  الحميم الماء الحار والاستحمام الاغتسال به (maqayis)؛ الحميم الماء الحار؛ الحمة عين فيها ماء حار (ayn)؛ الحميم الماء الحار؛ الحمة العين الحارة؛ حممت الماء أي سخنته (sihah)؛ الحميم الماء الحار؛ الحمة عين ماء فيها ماء حار؛ الحميمة الماء يسخن (tahdhib)؛ الحميم الماء الشديد الحرارة (mufradat)
- **B003** eritilmiş yağ veya yağ artığı — eritilmiş kuyruk yağı veya yağ artığı · eritilmiş yağdan bir parça · kuyruk yağını eritti
  الحم وهي الألية تذاب فالذي يبقى منها بعد الذوب حم واحدته حمة (maqayis)؛ الحم ما اصطهرت إهالته من الألية والشحم الواحدة حمة (ayn)؛ الحم ما يبقى من الألية بعد الذوب؛ حممت الألية أي أذبتها (sihah)؛ الحم ما اصطهرت إهالته من الألية والشحم؛ ما أذيب من الألية فهو حم (tahdhib)
- **B004** sıcağın ter ve yaz üzerindeki etkisi — ter · at terledi · sıcak yaz yağmuru · yakıcı yaz sıcağı
  الحميم وهو العرق (maqayis)؛ الحميم العرق؛ استحم الفرس إذا عرق (ayn)؛ الحميم العرق؛ استحم أي عرق؛ الحميم المطر الذي يأتي في شدة الحر؛ الحميم القيظ (sihah)؛ الحميم العرق؛ استحم الفرس إذا عرق؛ الحميم المطر الذي يكون في الصيف حين تسخن الأرض (tahdhib)
- **B005** ateşli hastalık ve ona bağlı nitelemeler — deve veya hayvan ateşi · adam ateşli hastalığa tutuldu · arazi ateşli hastalığın yaygın olduğu yer oldu · yiyeni ateşli hastalığa düşüren yiyecek
  الحمام وهو حمى الإبل؛ أحمت الأرض إذا صارت ذات حمى (maqayis)؛ أحمت الأرض؛ حم الرجل فهو محموم؛ الحمام حمى الإبل والدواب (ayn)؛ حم الرجل من الحمى؛ أحمت الأرض صارت ذات حمى؛ الحمام بالضم حمى الإبل؛ أرض محمة ذات حمى (sihah)؛ حم البعير حماما؛ حم الرجل حمى شديدة؛ المحمة أرض ذات حمى؛ طعام محمة (tahdhib)
- **B006** vakti yaklaşmak ve gelmek [kalıp] — ihtiyaç yaklaştı, vakti geldi · iş yaklaştı, zamanı geldi
  أحمت الحاجة حضرت وأحم الأمر دنا (maqayis)؛ أحمت حاجة الغد أي حانت ولزمت (ayn)؛ أحم خروجنا أي دنا؛ أجم الأمر وأحم أي حان وقته (sihah)؛ أحمت الحاجة وأجمت إذا دنت؛ أحم قدومهم دنا (tahdhib)
- **B007** atın alçak yem isteme sesi — atın kişnemeden alçak sesi · at alçak ses çıkardı
  الحمحمة حمحمة الفرس عند العلف (maqayis)؛ الحمحمة صوت الفرس دون الصوت العالي (ayn)؛ حمحم الفرس وتحمحم وهو صوته إذا طلب العلف (sihah)؛ الحمحمة صوت للبرذون دون الصوت العالي وللفرس دون الصهيل (tahdhib)
- **B008** hedefe yönelmek ve peşine düşmek — onun hedeflediği şeye yöneldim · onu istedim, peşine düştüm · bineğin yola çıkışını hızlandırdım
  حممت حمة أي قصدت قصده (maqayis)؛ حم هذا لذاك أي قضي وقدر وقصد (ayn)؛ حممت حمك أي قصدت قصدك؛ حممت ارتحال البعير أي عجلته؛ حاممته أي طالبته (sihah)؛ حممت حمه أي قصدت قصده؛ حاممته محامة طالبته (tahdhib)
- **B009** boşanma sonrası maddi destek vermek — boşadığı kadına maddi destek verdi · boşanma desteği olarak verilen giysiler
  حممها إذا متعها بثوب أو نحوه (maqayis)؛ يطلق المرأة فيحممها أي يمتعها تحميما (ayn)؛ حمم امرأته أي متعها بشيء بعد الطلاق (sihah)؛ حممها إياها أي متعها بها بعد الطلاق؛ ثياب التحمة ما يلبس المطلق امرأته إذا متعها (tahdhib)
- **B010** belirlenmiş yazgı ve ölüm payı — iş karara bağlandı ve belirlendi · belirlenmiş ölüm payı · belirlenmiş ayrılık payı · ölümler, ölüm payları
  حم الأمر قضي؛ الحمام قضاء الموت؛ حم هذا لذاك أي قضي وقدر؛ الحمم المنايا (ayn)؛ حم أيضا بمعنى قدر؛ الحمام بالكسر قدر الموت؛ حمة الفراق ما قدر وقضي (sihah)؛ حم الأمر إذا قدر؛ نزل به حمامه أي قدره وموته؛ عجلت بنا حمة الفراق وحمة الموت (tahdhib)
- **B011** sevilen yakın ve özel aile çevresi — sevilen ve seven yakın kişi · kişinin yakın ailesi ve akrabaları
  الحامة خاصة الرجل من أهله وولده وذوي قرابته؛ الحميم الذي يودك وتوده (ayn)؛ حميمك قريبك الذي تهتم لأمره؛ الحامة الخاصة أقرباؤه (sihah)؛ الحميم القريب الذي توده ويودك؛ الحامة خاصة الرجل من أهله وولده وذي قرابته؛ الحميم القرابة (tahdhib)
- **B012** güvercin türünden kuş — güvercinler ve güvercin türleri · bir güvercin; kimi kullanımlarda erkek veya dişi
  الحمام طائر؛ حمامة ذكر وحمامة أنثى والجميع حمام (ayn)؛ الحمام عند العرب ذوات الأطواق؛ الواحدة حمامة؛ اليمام الحمام الوحشي (sihah)؛ الحمامة طائر؛ الحمام كل ما كان ذا طوق؛ كل ما عب وهدر فهو حمام (tahdhib)
- **B013** su ısıtma kabı veya yıkanma yapısı — küçük su ısıtma kabı · yıkanma yapısı
  المحم القمقم الصغير يسخن فيه الماء؛ الحمام مشددا واحد الحمامات المبنية (sihah)؛ جاء بمحم أي بقمقم يسخن فيه الماء؛ طاب حميمك وحمتك للذي يخرج من الحمام (tahdhib)
- **B014** malın seçkin ve değerli bölümü — seçkin develer veya değerli mallar · seçkin develer · malın en değerli parçası
  الحميمة واحدة الحمائم وهي كرائم المال؛ إبل حامة إذا كانت خيارا (sihah)؛ الحميمة وجمعها حمائم كرائم الإبل؛ الحمامة خيار المال (tahdhib)
- **B015** canlıya göre değişen arka beden bölgesi — insanın arka alt bölgesi, kaba et · devenin hörgüç çıkıntısı veya atın sağrısı
  الحماء الدبر لأنه محمم بالشعر (ayn)؛ الحماء سافلة الإنسان (sihah)؛ الحمامة سعدانة البعير؛ الحمامة من الفرس القص (tahdhib)
- **B016** biçime bağlı yalıtık adlandırmalar — ayna; saray avlusu; kuyu makarası; güzel kadın; kapı halkası
  الحمامة المرآة؛ الحمامة ساحة القصر النقية؛ الحمامة بكرة الدلو؛ الحمامة المرأة الجميلة؛ الحمامة حلقة الباب (tahdhib)
- **B017** bir işte kararlı ve sabit kalmak — bu işte kararlı ve sabitim
  أنا محام على هذا الأمر أي ثابت عليه (tahdhib)

## ش ف ع (root_000802): 40:18 شَفِيعٍ

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

## ط و ع (root_000956): 40:18 يُطَاعُ

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

## ECHO س ط ع (root_000706): for 40:18 يُطَاعُ: withheld observed target; not identity

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

## خ و ن (root_000449): 40:19 خَآئِنَةَ

- **B001** güveni gizlice bozup sözünden dönme — birine verdiği sözü veya onun güvenini gizlice çiğnemek · bağlılıktaki eksilme ve güveni kötüye kullanma · verilmiş sözü ve güveni gizlice çiğneme · güveni kötüye kullanma · güveni kötüye kullanmaya yönelme ve bunu kollama · güveni kötüye kullanan kimse · güveni kötüye kullanan kadın veya bunu ağır biçimde yapan kimse · güveni kötüye kullanan topluluk · birini güveni kötüye kullanmakla suçlamak
  الخاء والواو والنون أصل واحد وهو التنقص (maqayis)؛ خانه يخونه خونا وذلك نقصان الوفاء (maqayis)؛ الخون مصدر خان يخون خونا وخيانة (jamhara)؛ خانه في كذا يخونه خونا وخيانة ومخانة واختانه (sihah)؛ الخيانة مخالفة الحق بنقض العهد في السر (mufradat)
- **B002** bir şeyden pay alarak eksiltme — bir payı ya da şeyi eksiltme
  تخونني فلان حقي أي تنقصني (maqayis)؛ تخونها مرا سحاب ومرا بارح ترب (maqayis;sihah)؛ التخون أيضا التنقص (sihah)؛ إلا ما تنقص نومه دعاء أمه له (sihah)؛ تخونها نزولي وارتحالي أي تنقص لحمها وشحمها (sihah)
- **B003** aslan — aslan
  الخوان الأسد والقياس واحد (maqayis)؛ الخوان الأسد (sihah)

## ع ي ن (root_001069): 40:19 ٱلْأَعْيُنِ

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

## ص د ر (root_000849): 40:19 ٱلصُّدُورُ, 40:56 صُدُورِهِمْ, 40:80 صُدُورِكُمْ

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

## ق ض ي (root_001237): 40:20 يَقْضِى, 40:20 يَقْضُونَ, 40:68 قَضَىٰٓ, 40:78 قُضِىَ

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

## د و ن (root_000502): 40:20 دُونِهِۦ, 40:66 دُونِ, 40:74 دُونِ

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

## س م ع (root_000741): 40:20 ٱلسَّمِيعُ, 40:56 ٱلسَّمِيعُ

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

## ب ص ر (root_000121): 40:20 ٱلْبَصِيرُ, 40:44 بَصِيرٌۢ, 40:56 ٱلْبَصِيرُ, 40:58 وَٱلْبَصِيرُ, 40:61 مُبْصِرًا

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

## س ي ر (root_000769): 40:21 يَسِيرُوا۟, 40:82 يَسِيرُوا۟

- **B001** yol almak ve birini ya da bir şeyi ilerletmek — yol almak, ilerlemek · yol alma, ilerleme · yolculuk ya da gidilen yol · yol alma, ilerleme · yolcu; çok gezen kimse · hayvan kendi başına ilerledi · hayvanı yürüttü · onunla birlikte yol aldı ya da onu yürüttü · onu yürüttü ya da yol almaya zorladı · buyurarak ya da zorlayarak yürütme · onunla aynı hızda yürüdü · birbirleriyle aynı hızda yürüdüler · bir günlük yol uzaklığı
  أصل يدل على مضي وجريان (maqayis); سار يسير سيرا ومسيرا (ayn;sihah); السير المضي في الأرض (mufradat); سرت وسرت بفلان وسرته وسيرته (mufradat); التسيير ضربان بالأمر وبالقهر (mufradat)
- **B002** izlenen yol ve içinde bulunulan durum — izlenen yol, davranış biçimi ya da durum · onlara iyi davrandı ya da onları iyi yönetti · ilk durumu · senin yürürlüğe koyduğun uygulama
  السيرة الطريقة والسنة (maqayis); السيرة الطريقة وسار بهم سيرة حسنة (sihah); السيرة الحالة التي يكون عليها الإنسان وغيره (mufradat); سنعيدها سيرتها الأولى (mufradat)
- **B003** deri kayış — deri kayış ya da bağ · deri kayışlar
  السير الجلد معروف (maqayis); السير الشراك والجمع سيور (ayn); السير ما يقد من الجلد والجمع السيور (sihah)
- **B004** çizgilemek ve çizgili dokuma — giyside ve okta çizgiler oluşturdu · kayışa benzer çizgileri olan dokuma · çizgili, kimi türü ipek karışımlı örtü
  المسير من الثياب الذي فيه خطوط كأنه سيور (maqayis); سيرت الثوب والسهم جعلت فيهما خطوطا (ayn); السيراء برود يخالطها حرير (ayn); المسير من الثياب الذي فيه خطوط كالسيور (sihah); السيراء برد فيه خطوط صفر (sihah)
- **B005** örtüyü üzerinden almak ya da kişiyi yurdundan çıkarmak [kalıp] — hayvanın sırt örtüsünü çıkarıp attı · onu ülkesinden çıkardı, sürdü
  سيرت الجل عن الدابة إذا ألقيته عنه (maqayis); سيره من بلده أي أخرجه وأجلاه (sihah); سيرت الجل عن ظهر الدابة نزعته عنه (sihah)
- **B006** yolcu topluluğu — yolcu topluluğu ya da kafile
  السيارة القافلة (sihah); السيارة الجماعة (mufradat); وجاءت سيارة (mufradat)
- **B007** aldırma, katlan ve çekişmeyi bırak [kalıp] — aldırma, katlan ve çekişmeyle kuşkuyu bırak
  قولهم في المثل سر عنك أي تغافل واحتمل; سر ودع عنك المراء والشك
- **B008** azık ve azık edinme — azık · azık arayıp edinme · bu kökten türemiş sayılan ad
  السيرة أيضا الميرة; الاستيار الامتيار; المستار مفتعل من السير

## ء ر ض (root_000025): 40:21 ٱلْأَرْضِ, 40:21 ٱلْأَرْضِ, 40:26 ٱلْأَرْضِ, 40:29 ٱلْأَرْضِ, 40:57 وَٱلْأَرْضِ, 40:64 ٱلْأَرْضَ, 40:75 ٱلْأَرْضِ, 40:82 ٱلْأَرْضِ, 40:82 ٱلْأَرْضِ

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

## ن ظ ر (root_001520): 40:21 فَيَنظُرُوا۟, 40:82 فَيَنظُرُوا۟

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

## ق و ي (root_001274): 40:21 قُوَّةً, 40:22 قَوِىٌّ, 40:82 قُوَّةً

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

## ء ث ر (root_000011): 40:21 وَءَاثَارًا, 40:82 وَءَاثَارًا

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

## ECHO ث و ر (root_000210): for 40:21 وَءَاثَارًا, 40:82 وَءَاثَارًا: withheld observed target; not identity

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

## ء ت ي (root_000009): 40:22 تَّأْتِيهِمْ, 40:35 أَتَىٰهُمْ, 40:50 تَأْتِيكُمْ, 40:53 ءَاتَيْنَا, 40:56 أَتَىٰهُمْ, 40:59 لَءَاتِيَةٌ, 40:78 يَأْتِىَ

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

## ب ي ن (root_000170): 40:22 بِٱلْبَيِّنَٰتِ, 40:23 مُّبِينٍ, 40:28 بِٱلْبَيِّنَٰتِ, 40:34 بِٱلْبَيِّنَٰتِ, 40:48 بَيْنَ, 40:50 بِٱلْبَيِّنَٰتِ, 40:66 ٱلْبَيِّنَٰتُ, 40:83 بِٱلْبَيِّنَٰتِ

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

## س ل ط (root_000732): 40:23 وَسُلْطَٰنٍ, 40:35 سُلْطَٰنٍ, 40:56 سُلْطَٰنٍ

- **B001** boyun eğdirme gücü — 
  أصل واحد وهو القوة والقهر؛ السلاطة من التسلط وهو القهر (maqayis)؛ أصله من التسليط (ayn)؛ السلاطة: القهر، وقد سلطه الله فتسلط عليهم (sihah)؛ سمي سلطانا لتسليطه، إلا أنا سلطناه عليهم (tahdhib)؛ السلاطة: التمكن من القهر، يقال سلطته فتسلط (mufradat)
- **B002** üstün gelen güçlü kanıt — 
  والسلطان الحجة (maqayis)؛ السلطان في معنى الحجة، أي حجتيه (ayn)؛ السلطان أيضا: الحجة والبرهان (sihah)؛ كل سلطان في القرآن فهو حجة، والسلطان: الحجة (tahdhib)؛ سمي الحجة سلطانا، فأتونا بسلطان مبين (mufradat)
- **B003** yönetme yetkisi ya da yetkili yönetici — 
  السلطان قدرة الملك، وقدرة من جعل ذلك له (ayn)؛ السلطان: الوالي (sihah)؛ قيل للأمراء: سلاطين؛ السلطان: قدرة الملك وقدرة من جعل ذلك له (tahdhib)؛ قد يقال لذي السلاطة وهو الأكثر (mufradat)
- **B004** keskin, akıcı ve güçlü konuşma — akıcı ve sivri dilli erkek · gürültücü, sivri ya da uzun dilli kadın · dil keskinliği ve söz söyleme gücü · uzun dilli oldu ve gürültülü biçimde çıkıştı · söz söyleme gücü ve dil keskinliği; çoğunlukla yergi bildirir · sivri ya da uzun dilli kadın
  السليط من الرجال الفصيح اللسان الذرب، والسليطة المرأة الصخابة (maqayis)؛ سلطت إذا طال لسانها واشتد صخبها (ayn)؛ رجل سليط فصيح حديد اللسان، وامرأة سليطة صخابة (sihah)؛ امرأة سليطة اللسان: حديدة اللسان أو طويلة اللسان (tahdhib)؛ سلاطة اللسان: القوة على المقال، وذلك في الذم أكثر (mufradat)
- **B005** aydınlatmada kullanılan bitkisel yağ — aydınlatmada kullanılan bitkisel yağ; kimi aktarımlarda özellikle susam yağı
  ومما شذ عن الباب السليط الزيت بلغة أهل اليمن، وبلغة غيرهم دهن السمسم (maqayis)؛ السليط الزيت (ayn)؛ السليط: الزيت عند عامة العرب، وعند أهل اليمن دهن السمسم (sihah)؛ السليط ما يضاء به، ومن هذا قيل للزيت السليط (tahdhib)؛ السليط: الزيت بلغة أهل اليمن (mufradat)
- **B006** uzun, keskin ya da sert parça — uzun ok · uzun oklar ya da keskin uçlar · anahtar dişleri · tek bir anahtar dişi · keskin ya da güçlü ve uzun toynak uçları · bilenmiş keskin uçlar · uzun bacaklar · sert ve dayanıklı toynak ya da taban
  السلطة: السهم الطويل؛ المساليط: أسنان المفاتيح؛ سنابك سلطات، أي حداد (sihah)؛ السلاطة بمعنى الحدة؛ نصالا محددة؛ السلط: القوائم الطوال؛ سلط الحافر (tahdhib)؛ سنابك سلطات: لها تسلط بقوتها وطولها (mufradat)
- **B007** iç yakan yoğun susuzluk — iç yakan yoğun susuzluk
  والسلاط الغليل (ayn)

## س ح ر (root_000682): 40:24 سَٰحِرٌ

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

## ج ي ء (root_000281): 40:25 جَآءَهُم, 40:28 جَآءَكُم, 40:29 جَآءَنَا, 40:34 جَآءَكُمْ, 40:34 جَآءَكُم, 40:66 جَآءَنِىَ, 40:78 جَآءَ, 40:83 جَآءَتْهُمْ

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

## ج ي ء (root_000282): 40:25 جَآءَهُم, 40:28 جَآءَكُم, 40:29 جَآءَنَا, 40:34 جَآءَكُمْ, 40:34 جَآءَكُم, 40:66 جَآءَنِىَ, 40:78 جَآءَ, 40:83 جَآءَتْهُمْ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ع ن د (root_001052): 40:25 عِندِنَا, 40:35 عِندَ, 40:35 وَعِندَ, 40:83 عِندَهُم

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

## ق ت ل (root_001200): 40:25 ٱقْتُلُوٓا۟, 40:26 أَقْتُلْ, 40:28 أَتَقْتُلُونَ

- **B001** canını alarak öldürme — öldürme, canına son verme · onu kötü ve çirkin bir biçimde öldürme · tek bir öldürme olayı · öldürülmüş kimse · insan bedenindeki ölümcül noktalar
  القتل معروف (ayn;jamhara;sihah;tahdhib)؛ قتله إذا أماته بضرب أو جرح أو حجر أو سم أو علة (ayn;tahdhib)؛ أصل القتل إزالة الروح عن الجسد (mufradat)؛ مقاتل الإنسان المواضع التي إذا أصيبت قتله ذلك (maqayis;jamhara;sihah)
- **B002** boyun eğdirme; hayvanı işe alıştırma; deneyimle pişme — uysallaştırılmış ve işe alıştırılmış · işlerce sınanmış, deneyimli adam
  أصل صحيح يدل على إذلال وإماتة (maqayis)؛ المقتل من الدواب ما ذل ومرن على العمل (ayn;tahdhib)؛ رجل مقتل أي مجرب (sihah;tahdhib)؛ قتلت فلانا وقتلته إذا ذللته (tahdhib;mufradat)
- **B003** eksiksiz ve kesin olarak bilme — bir şeyi eksiksiz ve kesin olarak bilmek
  قتلت الشيء خبرا وعلما (maqayis;sihah)؛ قتلته علما وقتلته يقينا للرأي والحديث (tahdhib)؛ قتلت كذا علما وما قتلوه يقينا أي ما علموا كونه مصلوبا علما يقينا (mufradat)
- **B004** nazlıca salınma; gereksinime yumuşakça yaklaşma; kadına yalvarma — delikanlı için süslenip nazlıca salınmak · gereksinimini ince ve yumuşak yollarla elde etmeye çalışmak · kadına boyun eğip yalvarmak
  تقتلت الجارية للرجل حتى عشقها كأنها خضعت له (maqayis)؛ تقتلت الجارية للفتى تزينت ومشت مشية حسنة تقلبت فيها وتثنت وتكسرت (ayn)؛ تقتل الرجل لحاجته إذا تأتى لها والرجل يتقتل للمرأة يتضرع إليها (jamhara)؛ تقتلت المرأة في مشيتها إذا تقلبت وتثنت وتكسرت (sihah)؛ معنى تقتلها وتدللها واختيالها (tahdhib)
- **B005** öldürülmeye açık kılma veya ölüm nedeni hazırlama — onu öldürülme tehlikesine atmak · insanın ölüm nedeni iki çenesi arasındadır, yani dilidir
  أقتلت فلانا عرضته للقتل (maqayis;ayn;sihah;tahdhib;mufradat)؛ مقتل الرجل بين فكيه أي سبب قتله بين لحييه (tahdhib)
- **B006** aşka yenik düşmüş yürek; aşk veya görünmeyen varlıklar yüzünden aklın bozulması — aşka yenik düşmüş yürek · aşk ya da görünmeyen varlıklar yüzünden aklı karışıp kendinden geçmek
  قلب مقتل إذا قتله العشق (maqayis;ayn;sihah;tahdhib)؛ إذا قتله العشق أو الجن قيل اقتتل (maqayis;sihah)؛ اقتتله العشق والجن ولا يقال ذلك في غيرهما (mufradat)؛ اقتتل الرجل إذا جن واقتتلته الجن أي خبلوه (tahdhib)
- **B007** içkiyi suyla karıştırıp sertliğini giderme [kalıp] — içkiyi suyla karıştırıp sertliğini gidermek
  قتلت الخمر بالماء إذا مزجت (maqayis;jamhara;sihah;mufradat)؛ الخمر مقتولة إذا مزجت بالماء حتى ذهبت شدتها فصار رياضة لها (tahdhib)
- **B008** düşman veya denk rakip — düşman veya rakip · onun dengi, benzeri ve rakibi
  القتل العدو وجمعه أقتال (maqayis;sihah)؛ قوم أقتال أي أهل الوتر والترة أي أعداء ذوي ترات (ayn)؛ فلان قتل فلان أي نظيره وابن عمه (jamhara)؛ الأقتال الأعداء واحدهم قتل وهم الأقران (tahdhib)؛ القتل العدو والقرن (mufradat)
- **B009** can; dişi deve için sağlam ve iri beden yapısı — can veya bedende kalan yaşam · sağlam ve iri yapılı dişi deve
  القتال النفس (maqayis;sihah)؛ القتال بقية النفس (tahdhib)؛ ناقة ذات قتال إذا كانت وثيقة أو غليظة وثيقة الخلق (maqayis;jamhara;sihah)
- **B010** Tanrı'nın lanetlemesi, yok etmesi veya düşman olması dileği [kalıp] — Tanrı onları lanetlesin veya yok etsin · kahrolsun insan
  قاتلهم الله أي لعنهم (ayn;tahdhib)؛ قتل الإنسان معناه لعن الإنسان وقاتله الله لعنه (tahdhib)؛ قتل الخراصون لفظ قتل دعاء عليهم (mufradat)؛ قاتل الله فلانا أي عاداه (tahdhib)
- **B011** öldürme amacıyla karşılıklı savaşma — birbiriyle savaşmak · karşılıklı savaşma, çatışma · savaşabilecek durumdaki kişiler · topluluk birbirleriyle savaştı
  اقتتل القوم وتقتلوا في معنى تقاتلوا (jamhara)؛ المقاتلة القتال وقد قاتلته قتالا وقيتالا (sihah)؛ قاتل فلان فلانا لا يكون إلا بين اثنين (tahdhib)؛ المقاتلة المحاربة وتحري القتل والاقتتال كالمقاتلة (mufradat)
- **B012** ölümü göze alıp kendini tehlikeye atma — ölümü göze alıp kendini tehlikeye atmak
  استقتل أي استمات (sihah)
- **B013** kışın insanları doyurup ısıtan kişi [kalıp] — kışın insanları doyurup ısıtan kişi
  هو قاتل الشتوات أي يطعم فيها ويدفىء الناس (tahdhib)

## ب ن ي (root_000156): 40:25 أَبْنَآءَ, 40:36 ٱبْنِ, 40:53 بَنِىٓ, 40:64 بِنَآءً

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

## ب ن و (root_001959): documented alternative for 40:25 أَبْنَآءَ, 40:53 بَنِىٓ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## ن س و (root_001500): 40:25 نِسَآءَهُمْ

- **B001** kadın topluluğunu bildiren ayrı biçimli çoğullar — kadınlar topluluğu; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu; aynı biçimden tekili bulunmayan çoğul · kadınlar; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu adının küçültme biçimi · kadınlar topluluğu adının çoğul küçültme biçimi
  النُّسوة والنِّسوان والنِّسون كله جملة النساء (ayn)؛ النَّسوة والنُّسوة والنساء والنِّسوان جمع امرأة من غير لفظها وتصغير نسوة نسية ونسيات (sihah)؛ النساء والنسوان والنسوة جمع المرأة من غير لفظها (mufradat)

## ك ي د (root_001334): 40:25 كَيْدُ, 40:37 كَيْدُ

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

## ض ل ل (root_000913): 40:25 ضَلَٰلٍ, 40:33 يُضْلِلِ, 40:34 يُضِلُّ, 40:50 ضَلَٰلٍ, 40:74 ضَلُّوا۟, 40:74 يُضِلُّ

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

## و ذ ر (root_001638): 40:26 ذَرُونِىٓ

- **B001** et parçası; bir aktarımda etsiz kemik parçası — et parçası; bir aktarıma göre etsiz kemik parçası · et parçaları · bol et parçalı ekmek yemeği
  الوذرة وهي الفدرة من اللحم (maqayis)؛ الوذرة قطعة عظم لا لحم فيه (ayn)؛ الوذرة بالتسكين الفدرة وهي القطعة من اللحم (sihah)؛ الوذرة القطعة من اللحم مثل الفدرة (tahdhib)؛ الوذر بضع اللحم (tahdhib)؛ الوذرة قطعة من اللحم (mufradat)؛ ثريدة كثيرة الوذر (tahdhib)
- **B002** eti parçalama veya yarayı çizerek açma — eti parçalama veya yarayı çizerek açma · eti parçalara ayırmak · yarayı çizerek açmak · et parçasını küçük parçalara bölmek
  التوذير أن يشرط الجرح (maqayis)؛ وذرت اللحم توذيرا قطعته وكذلك الجرح إذا شرطته (sihah)؛ وقد وذرت الوذرة أذرها وذرا إذا بضعتها بضعا (tahdhib)
- **B003** bir şeyi bırakmak — bir şeyi bırakmak · önemsiz gördüğü şeyi bir yana atmak · bunu bırak · onu bırakmak
  ذر ذا (maqayis)؛ أماتت المصدر من يذر والفعل الماضي واستعملته في الحاضر والأمر (ayn)؛ ذره أي دعه وهو يذره (sihah)؛ ذرذا ودع ذا ولا يقال وذرته (tahdhib)؛ يذر الشيء أي يقذفه لقلة اعتداده به (mufradat)
- **B004** cinsel göndermeli ağır soy sövgüsü; ad biçiminde klitoris — cinsel organ göndermeli ağır bir soy sövgüsü · ağır bir soy sövgüsü · klitoris
  يا ابن شامة الوذر (maqayis;ayn;sihah;tahdhib)؛ كلمة قذف (sihah)؛ كلمة معناها القذف (tahdhib)؛ عرض لها بأعضاء الرجال (maqayis)؛ أراد المذاكير (tahdhib)؛ أرادوا بها القلف (tahdhib)؛ الوذفة والوذرة بظارة المرأة (tahdhib)

## خ و ف (root_000447): 40:26 أَخَافُ, 40:30 أَخَافُ, 40:32 أَخَافُ

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

## ب د ل (root_000095): 40:26 يُبَدِّلَ

- **B001** yerine gecme ve yerine koyma — bir seyin yerini tutan karsilik · karsilik, bedel anlami veren diger soyleyis · baskasinin yerine gecen sey veya kisi · bir seyi kaldirip yerine baskasini koymak · bir seyi giderip yerine baskasini getirmek · bir seyi baska bir seyin yerine almak · karsilikli olarak degis tokus etmek · biri gidince yerine ayni nitelikte baskasi gelen secilmis kisiler
  قيام الشيء مقام الشيء الذاهب (maqayis)؛ البديل البدل (sihah)؛ استبدل الشيء بغيره وتبدله به إذا أخذه مكانه (sihah)؛ أبدلت الخاتم بالحلقة إذا نحيت هذا وجعلت هذا مكانه (tahdhib)؛ الأبدال خيار بدل من خيار (tahdhib)
- **B002** bicimini veya halini degistirme — yerine karsilik getirmeden bir seyi degistirmek · cevheri ayni kalirken bicimi veya hali degistirme · yuzugu eritip ayni maddeden halka bicimine sokmak
  بدلت الشيء إذا غيرته وإن لم تأت له ببدل (maqayis)؛ تبديل الشيء أيضا تغييره وإن لم يأت ببدل (sihah)؛ التبديل تغيير الصورة إلى صورة أخرى والجوهرة بعينها (tahdhib)
- **B003** gogus eti — gogus eti; boyun ile kopru kemigi arasindaki kisim
  البآدل لحم الصدر واحدتها بأدلة (jamhara)؛ البآدل واحدتها بأدلة وهي ما بين العنق إلى الترقوة (tahdhib)؛ البأدلة لحم الصدر (tahdhib)
- **B004** el ve ayak agrisi — ellerde ve ayaklarda agri · ellerinde ve ayaklarinda bu agriya tutulmak
  البَدَل وجع في اليدين والرجلين
- **B005** yiyecek saticisi — her tur yiyecek maddesini satan kisi
  العرب تقول للذي يبيع كل شيء من المأكولات بَدّال

## ظ ه ر (root_000970): 40:26 يُظْهِرَ, 40:29 ظَٰهِرِينَ

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

## ف س د (root_001154): 40:26 ٱلْفَسَادَ

- **B001** bozulma ve bozma — bozulmak; düzgün ve elverişli durumdan çıkmak · bozulma; düzgünlüğün ve dengenin yitmesi · bozulma, bozuk duruma gelme · bozuk, düzgünlüğünü yitirmiş · bozulmuş, bozuk · bozuk kimseler · bozmak, bozuk hâle getirmek · bozma, bozuk hâle getirme · bozan veya bozulmaya yol açan kimse · bozulmayı isteme; düzeltmenin karşıtı yönde davranma · zarar doğuran şey; yararın karşıtı · bir şeyi mahvetmek veya yok etmek · saldırdığı topluluğun gerisini kesip dağıtan askerî birlik
  فسد الشيء يفسد فسادا وفسودا وهو فاسد وفسيد (maqayis;sihah;tahdhib)؛ الفساد نقيض الصلاح (ayn;tahdhib)؛ الفساد خروج الشيء عن الاعتدال (mufradat)؛ أفسدته وأفسده غيره (ayn;sihah;mufradat)؛ أفسد فلان المال وفسد الشيء إذا أباره (tahdhib)؛ الاستفساد خلاف الاستصلاح والمفسدة خلاف المصلحة (sihah)

## ع و ذ (root_001059): 40:27 عُذْتُ, 40:56 فَٱسْتَعِذْ

- **B001** korunmak için birine ya da bir yere sığınmak — başkasına sığınmak ve onun korumasına tutunmak · korunmak için sığınmak · sığınarak korunmak · Tanrı'ya sığınırım · senden korunmak için Tanrı'ya sığınırım · Tanrı'ya sığınırım · o senin sığınağındır · kendisine sığınılan koruyucu yer ya da varlık
  أصل صحيح يدل على معنى واحد وهو الالتجاء إلى الشيء (maqayis)؛ أعوذ بالله أي ألجأ إلى الله عوذا وعياذا (ayn)؛ عذت بفلان واستعذت به أي لجأت إليه وهو عياذي أي ملجئي (sihah)؛ عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به (tahdhib)؛ العوذ الالتجاء إلى الغير والتعلق به (mufradat)
- **B002** koruyucu söz, yazı veya nesneyle korunma sağlama — birini koruma altına almak · koruyucu sözlerle birini sakınmak · korku ya da kötülükten korunmak için kullanılan söz veya nesne · koruyucu söz söyleme, okuma ya da yazma işi · kutsal kitabın korunmak için okunan iki bölümü
  العوذة والمعاذة التي يعوذ بها الإنسان من فزع أو جنون (maqayis)؛ ومنه العوذة والتعويذ والمعاذة التي يعوذ بها الإنسان (ayn)؛ العوذة والمعاذة والتعويذ كله بمعنى (sihah)؛ التعاويذ التي تكتب وتعلق على الإنسان من العين تسمى المعاذات وهي العوذ واحدتها عوذة (tahdhib)؛ العوذة ما يعاذ به من الشيء ومنه قيل للتميمة والرقية عوذة (mufradat)
- **B003** doğumdan sonraki ilk günlerindeki dişi — doğumdan sonraki ilk günlerindeki dişi · doğumdan sonraki ilk günlerinde bulunan dişiler
  لكل أنثى إذا وضعت عائذ وتكون كذا سبعة أيام والجمع عوذ (maqayis)؛ كل أنثى عائذ إذا وضعت مدة سبعة أيام والجميع عوذ (ayn)؛ العوذ الحديثات النتاج من الظباء والإبل والخيل واحدتها عائذ (sihah)؛ الناقة إذا وضعت ولدها فهي عائذ أياما وجمعها عوذ (tahdhib)؛ كل أنثى وضعت فهي عائذ إلى سبعة أيام (mufradat)
- **B004** bir şeye yapışıp onun yanında kalan şey — diken dibinde ya da erişilmesi güç sert yerde yetişen ot · kemiğe yapışık et · rüzgârla bir taşın ya da kütüğün çevresinde dönen şey
  كل شيء لصق بشيء أو لازمه (maqayis)؛ العوذ النبت في أصل الشوك أو في المكان الحزن لا يكاد المال يناله (sihah)؛ أطيب اللحم عوذه وهو ما عاذ بالعظم ولزمه (sihah)؛ العوذ ما دار به الشيء الذي تضربه الريح فهو يدور بالعوذ من حجر أو أرومة (tahdhib)
- **B005** atın tasma yerindeki dairesel beden işareti — atın tasma geçen boyun yerindeki dairesel işaret · atın tasma yerindeki dairesel beden işareti
  معوذ الفرس موضع القلادة ودائرة المعوذ تستحب (sihah)؛ من دوائر الخيل المعوذ وهي التي تكون في موضع القلادة يستحبونها (tahdhib)
- **B006** rakibin korkutmasından ya da sonuçsuz öldürme girişiminden kurtulmak [kalıp] — rakibin korkutmasından ya da öldürmeyen saldırısından kurtulmak
  أفلت منه فلان عوذا إذا خوفه ولم يضربه أو ضربه وهو يريد قتله فلم يقتله (sihah)؛ أفلت فلان من فلان عوذا إذا خوفه ولم يضربه أو ضربه وهو يريد قتله فلم يقتله (tahdhib)
- **B007** savaşta işi birbirine bırakıp birbirine sığınmak — savaşta işi birbirine bırakıp birbirine sığınmak
  تعاوذ القوم في الحرب إذا تواكلوا وعاذ بعضهم ببعض (tahdhib)
- **B008** birini ondan hoşlanmadığı için bırakmak [kalıp] — birini ondan hoşlanmadığı için bırakmak · birini ondan hoşlanmadığı için bırakmak
  ما تركت فلانا إلا عوذا منه بالتحريك وعواذا منه أي كراهة (sihah)

## ر ج ل (root_000546): 40:28 رَجُلٌ, 40:28 رَجُلًا

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

## ء و ل (root_000067): 40:28 ءَالِ, 40:45 بِـَٔالِ, 40:46 ءَالَ, 40:54 لِأُو۟لِى

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

## و ل ي (root_001684): 40:33 تُوَلُّونَ (also echo for 40:28 ءَالِ, 40:45 بِـَٔالِ, 40:46 ءَالَ, 40:54 لِأُو۟لِى)

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

## ك ت م (root_001284): 40:28 يَكْتُمُ

- **B001** gizleyip açıklamamak — bir şeyi veya sözü gizlemek · gizli tutma, açıklamama · bir şeyi gizleyip saklamak · özenle saklanan sır · iyice gizlenmiş şey · ondan sırrımı saklamasını istedim · sırrını benden sakladı · sırrını saklayan adam · gördüğü iyiliği gizleyerek nankörlük etmek
  أصل صحيح يدل على إخفاء وستر؛ كتمت الحديث كتما وكتمانا (maqayis)؛ الكتمان نقيض الإعلان (ayn;tahdhib)؛ كتمت الشيء أكتمه كتما وكتمانا (jamhara;sihah)؛ ستر الحديث (mufradat)
- **B002** beklenen sesi çıkarmama [kalıp] — binilince böğürmeyen dişi deve · gök gürültüsü çıkarmayan bulut · bırakıldığında çınlamayan yay · böğürmeyen erkek deve
  ناقة كتوم لا ترغو إذا ركبت (maqayis;ayn;sihah;tahdhib)؛ سحاب مكتتم لا رعد فيه (maqayis;sihah)؛ الكاتم من القسي التي لا ترن إذا أنبضت (ayn;tahdhib)؛ الكتيم الجمل الذي لا يرغو (tahdhib)
- **B003** çatlağı olmayan yay [kalıp] — gövdesinde çatlak bulunmayan yay
  قيل هي التي لا شق فيها وأكثر القول هي التي لا صدع في نبعها (ayn)؛ الكتوم القوس التي لا شق فيها (sihah;tahdhib)؛ الكتيم القوس التي لا تنشق (tahdhib)
- **B004** dikişlerinden su sızdırmama [kalıp] — su sızdırmayan dikiş · su sızdırmayan deri su kabı · dikilmiş deri kabın dikiş sızıntısı kesildi
  خرز كتيم لا ينضح الماء (maqayis)؛ خرز كتيم لا يخرج منه الماء وسقاء كتيم (sihah)؛ كتمت المزادة تكتم كتوما إذا ذهب مرحها وسيلان الماء من مخارزها (tahdhib)
- **B005** siyah saç boyası karışımında kullanılan kırmızımsı bitki — siyah saç boyası karışımında kullanılan kırmızımsı boya bitkisi
  الكتم فنبات يختضب به (maqayis)؛ الكتم نبات يخلط مع الوسمة للخضاب الأسود (ayn)؛ الكتم شجر يخضب به الشعر (jamhara)؛ الكتم نبت يخلط بالوسمة يختضب به (sihah;tahdhib)؛ الكتم نبت فيه حمرة (tahdhib)
- **B006** atın dar burun deliği yüzünden nefesinin tutulması [kalıp] — atın dar burun deliği yüzünden nefesinin tutulması
  يقال للفرس إذا ضاق منخره عن نفسه قد كتم الربو

## ص د ق (root_000852): 40:28 صَادِقًا

- **B001** sözün inançla ve gerçekle uyuşması — doğruluk; sözün inançla ve gerçekle uyuşması · konuşurken doğruyu söylemek · birine doğru söz söylemek veya onun sözünü doğru saymak · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse · çok doğru sözlü kimse
  الصدق خلاف الكذب (maqayis;ayn;sihah;tahdhib)؛ الصدق والكذب أصلهما في القول (mufradat)؛ الصدق مطابقة القول الضمير والمخبر عنه معا (mufradat)
- **B002** nesnenin sağlamlığı veya düzgünlüğü — bir nesnedeki sertlik veya düzgünlük · sert ve güçlü nesne ya da mızrak
  شيء صدق أي صلب (maqayis)؛ رمح صدق (maqayis)؛ الصدق الصلب والمستوي (sihah;tahdhib)
- **B003** tamlık, iyilik ve güvenilirlik — iyi, güvenilir ve erdemli kişi ya da topluluk · bir şeyde tamlık ve kusursuzluk · övülmeye değer, iyi ve sağlam durum
  رجل صدق (maqayis;ayn;sihah;tahdhib)؛ الصدق الكامل من كل شيء (ayn;tahdhib)؛ في مقعد صدق وقدم صدق ومدخل صدق ومخرج صدق ولسان صدق (mufradat)
- **B004** sözü veya beklentiyi doğrulayıp gerçekleştirme — savaşta gereğini yerine getirip sebat etmek · atılımında veya koşusunda verdiği sözü tutan · tahmini gerçekleşmek veya tahminini gerçekleştirmek · bir sözün veya durumun doğruluğunu ortaya koyma ve onaylama · öncekini doğrulayan ve destekleyen · sözü doğru kabul edip onaylayan kimse · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse
  صدقوهم القتال (maqayis;sihah;tahdhib)؛ صدق في القتال إذا وفى حقه (mufradat)؛ صدق ظني (mufradat)؛ لقد صدق عليهم إبليس ظنه أي حقق ظنه (tahdhib)؛ مصدق لما معهم (mufradat)
- **B005** içten sevgiye dayalı dostluk — dost veya yakın arkadaş · içten sevgiye dayalı arkadaşlık ve dostluk kurma
  الصداقة مشتقة من الصدق في المودة (maqayis)؛ الصداقة مصدر الصديق (ayn;tahdhib)؛ الصداقة والمصادقة المخالة (sihah)؛ الصداقة صدق الاعتقاد في المودة (mufradat)
- **B006** mal vererek yardım etme veya haktan vazgeçme — iyilik amacıyla maldan verilen yardım veya bu adla anılan yükümlü pay · bir hakkından bağışlayarak vazgeçmek · mali yardım veren kimse · hayvanlara ilişkin yardım paylarını toplayan görevli · mali yardım veren erkekler ve kadınlar
  الصدقة ما يتصدق به المرء عن نفسه وماله (maqayis)؛ المتصدق المعطي للصدقة (ayn;sihah;tahdhib)؛ المصدق الذي يأخذ صدقات الغنم (maqayis;sihah;tahdhib)؛ الصدقة ما يخرجه الإنسان من ماله على وجه القربة (mufradat)؛ من تجافى عنه (mufradat)
- **B007** kadına belirlenen evlilik hakkı olan mal — kadına verilen veya belirlenen evlilik hakkı olan mal · kadının evlilikte aldığı mal veya kadınlara ait bu tür mallar · kadına evlilik hakkı olarak mal belirlemek
  الصداق صداق المرأة (maqayis)؛ الصداق والصدقة والصدقة المهر (ayn)؛ الصداق والصداق مهر المرأة (sihah)؛ صداق المرأة وصدقة المرأة (tahdhib)؛ صداق المرأة وصداقها وصدقتها ما تعطى من مهرها (mufradat)

## ص و ب (root_000889): 40:28 يُصِبْكُم

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

## ن ص ب (root_001507): 40:47 نَصِيبًا (also echo for 40:28 يُصِبْكُم)

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

## ب ع ض (root_000133): 40:28 بَعْضُ, 40:77 بَعْضَ

- **B001** parça ve parçalara ayırma — bir şeyin parçası, bölümü veya ondan bir kesim · parçalar, bölümler · bir şeyi parçalara ayırmak · parçalara ayrılmak
  بعض كل شيء طائفة منه (maqayis;ayn;tahdhib)؛ بعض الشيء جزء منه (mufradat)؛ بعض الشيء واحد أبعاضه (sihah)؛ بعض الشيء معروف (jamhara)؛ بعضت الشيء تبعيضا إذا فرقته أجزاء (maqayis;ayn;tahdhib)؛ تبعض الشيء وبعضته أي فرقته (jamhara)؛ بعضته تبعيضا أي جزأته فتبعض (sihah)؛ بعضت كذا جعلته أبعاضا نحو جزأته (mufradat)
- **B002** sivrisinek ve ona bağlı zarar veya bulunma kullanımları — sivrisinek · sivrisinekler, sivrisinek topluluğu veya tahtakurusu · sivrisineğin çok olduğu gece · topluluğa sivrisineklerin zarar vermesi · sivrisineklerden zarar görmüş topluluk · bulundukları yerde sivrisinek olması · sivrisinek bulunan arazi · aşırı küçüklüğü veya olanaksızlığı yüzünden elde edilemeyen şey
  البعوضة وهي معروفة والجمع بعوض (maqayis)؛ البعوض جمع البعوضة وهي المؤذية العاضة في الصيف (ayn)؛ البعوض البق الواحدة بعوضة (sihah)؛ قوم مبعوضون وقد بعض القوم إذا آذاهم البعوض وأبعضوا إذا كان في أرضهم بعوض (tahdhib)؛ البعوض بني لفظه من بعض وذلك لصغر جسمها (mufradat)

## ه د ي (root_001583): 40:28 يَهْدِى, 40:29 أَهْدِيكُمْ, 40:33 هَادٍ, 40:38 أَهْدِكُمْ, 40:53 ٱلْهُدَىٰ, 40:54 هُدًى

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

## ECHO ه د د (root_001580): for 40:28 يَهْدِى, 40:29 أَهْدِيكُمْ, 40:33 هَادٍ, 40:38 أَهْدِكُمْ, 40:53 ٱلْهُدَىٰ, 40:54 هُدًى: withheld observed target; not identity

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

## س ر ف (root_000699): 40:28 مُسْرِفٌ, 40:34 مُسْرِفٌ, 40:43 ٱلْمُسْرِفِينَ

- **B001** sınırı ve uygun ölçüyü aşma — sınırı veya uygun ölçüyü aşma · ölçüsüzlük ve savurganlık · sınırı aştı · işinde sınırı aşan kimse · öldürmede sınırı aşma; fail dışındaki birini öldürme · harcamada savurganlık; parayı uygun olmayan yere harcama · sulama veya başka bir yarar sağlamadan akıp giden su · yemede ölçüyü aşma veya yenmemesi gereken şeyi yeme
  تعدي الحد (maqayis); مجاوزة القدر (maqayis); الإسراف نقيض الاقتصاد (ayn); السرف ضد القصد (sihah;tahdhib); الإسراف في النفقة التبذير (sihah); تجاوز ما حد لك (tahdhib); سرف الماء ما ذهب منه في غير سقي ولا نفع (tahdhib); مجاوزة القصد في الأكل (tahdhib); تجاوز الحد في كل فعل (mufradat); فلا يسرف في القتل (tahdhib;mufradat)
- **B002** yanılma, gözden kaçırma veya bilememe — yanılma, gözden kaçırma ve bilmeme · bilgisiz kimse · şeyi yanlış yaptı, gözden kaçırdı veya bilemedi · sizi ıskaladım, fark etmedim veya tanımadım · yüreği yanılan ve dalgın kimse · sağ eli belirsiz kaldı ve tanınmadı · yanıldı veya fark etmedi
  الإغفال (maqayis;tahdhib); السرف الجهل (maqayis;ayn;tahdhib); السرف الخطأ (ayn;sihah;tahdhib); مررت بكم فسرفتكم (maqayis;ayn;sihah;mufradat); سرفت الشيء أي أخطأته وأغفلته (tahdhib); إخطاء الشيء وضعه في غير موضعه (tahdhib); سرفت يمينه أي لم أعرفها (tahdhib)
- **B003** ete alışkanlık derecesinde düşkünlük [kalıp] — ete güçlü bir alışkanlık geliştirme ve onu sık sık satın alma
  إن للحم سرفا كسرف الخمر (maqayis;sihah;tahdhib); للحم سرف كسرف الخمر وهو الضراوة (ayn); ضراوة كضراوة الخمر (tahdhib)
- **B004** ağaç delen, yaprak veya odun yiyen küçük böcek — yaprak veya odun yiyen, ağacı delip yuva kuran küçük böcek · ağaç böceğin saldırısına uğradı veya yaprakları yendi · bu böceğin saldırısına uğramış ağaç · yuva yapmada bu böcekten bile daha usta
  السرفة دويبة تأكل الخشب (maqayis); دويبة صغيرة تنقب الشجر وتبني فيه بيتا (ayn); دويبة تتخذ لنفسها بيتا (sihah); أصابته السرفة (ayn;tahdhib); السرف مصدر سرفت الشجرة (tahdhib); السرفة دويبة تأكل الورق (mufradat); سرفت الشجرة فهي مسروفة (sihah;mufradat)

## ن ص ر (root_001510): 40:29 يَنصُرُنَا, 40:51 لَنَنصُرُ

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

## ب ء س (root_000079): 40:29 بَأْسِ, 40:76 فَبِئْسَ, 40:84 بَأْسَنَا, 40:85 بَأْسَنَا

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

## ر ش د (root_000565): 40:29 ٱلرَّشَادِ, 40:38 ٱلرَّشَادِ

- **B001** doğru yolu bulma ve gösterme — doğru yolu bulma · doğru yolda olma · yolların varış yerleri · en doğru ve en kestirme yol · doğru yolu buldu · doğru yolu gösterdi · yol gösterme · doğru yolu bulan kişi · doğru yolu bulan kişi
  أصل واحد يدل على استقامة الطريق؛ الرشد والرشد خلاف الغي (maqayis)؛ نقيض الغي ونقيض الضلال (ayn;tahdhib)؛ الإرشاد الدلالة والهداية (ayn;tahdhib)؛ الرشاد خلاف الغي والطريق الأرشد نحو الأقصد (sihah)؛ يستعمل استعمال الهداية (mufradat)
- **B002** işin doğrusunu bulup yerinde davranma — bir işte doğru olanı bulma ve yerinde davranma · işin doğru yönünü buldu · doğru karar veren kişi · doğru karar veren kişi
  أصاب فلان من أمره رشدا ورشدا ورشده (maqayis)؛ رشد فلان إذا أصاب وجه الأمر (ayn)؛ إذا أصاب وجه الأمر والطريق فقد رشد (tahdhib)؛ فإن آنستم منهم رشدا وبين الرشدين بون بعيد (mufradat)
- **B003** evlilik içinde doğmuş olma — evlilik içi doğum · evlilik içinde doğmuş çocuk
  وهو لرشدة خلاف لغيه (maqayis)؛ الرشدة نقيض الغية وولد لرشدة (ayn)؛ هو لرشدة خلاف قولك لزنية (sihah)؛ ولد فلان لغير رشدة وولد لغية ولزنية (tahdhib)
- **B004** uğurlu ad verilen avuç dolduran taş ve tere tohumu — avucu dolduran taş · tek bir avuçluk taş · tere tohumu
  الرشاد الحجر سمي به تطيرا من الحرف وصلابة الحجر (ayn)؛ حب الرشاد كأنهم تطيروا من لفظ الحرف؛ الرشاد الحجر الذي يملأ الكف الواحدة رشادة (tahdhib)

## م ث ل (root_001397): 40:30 مِّثْلَ, 40:31 مِثْلَ, 40:40 مِثْلَهَا

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

## د ء ب (root_000456): 40:31 دَأْبِ

- **B001** bir işi kararlılıkla ve sürekli sürdürme — bir şey üzerinde yılmadan ve sürekli çalışmak · yolculuğu kesintisiz sürdürme · durmaksızın ve yoğun çabayla yol alma · işini ya da devinimini sürekli sürdüren · sürekli birbirini izleyen gece ile gündüz
  ملازمة ودوام (maqayis)؛ دأب الرجل في عمله إذا جد (maqayis)؛ دأب فلان في عمله أي جد وتعب ودؤوبا فهو دائب (sihah)؛ الدؤوب المبالغة في السير ودأبت الناقة دؤوبا (tahdhib)؛ الدأب إدامة السير ودأب في السير والشمس والقمر دائبين (mufradat)؛ الدائبان الليل والنهار (maqayis;sihah)
- **B002** süregelen alışkanlık ve tutum — süregelen alışkanlık, tutum veya durum · senin alışkanlığın ve süregelen tutumun
  الدأب العادة والشأن (maqayis;sihah)؛ كدأب آل فرعون أي كشأن آل فرعون وكأمر آل فرعون (tahdhib)؛ دأبك وديدنك كله في العادة (tahdhib)؛ العادة المستمرة دائما على حالة (mufradat)
- **B003** bir başkasını yormak — bir başkasını uzun süre yürütüp ya da çalıştırıp yormak · bir başkasını sürekli yürütme veya çalıştırma yoluyla yorma
  أدأبته أنا إدآبا (maqayis)؛ وأدأبته أنا (sihah)؛ أدأب الرجل الدابة إدآبا إذا أتعبها (tahdhib)

## ع و د (root_001058): 40:31 وَعَادٍ

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

## ر و د (root_000610): 40:31 يُرِيدُ

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

## ر د د (root_000555): 40:43 مَرَدَّنَآ (also echo for 40:31 يُرِيدُ)

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

## د ب ر (root_000458): 40:33 مُدْبِرِينَ

- **B001** arka taraf — bir şeyin arkası ve önünün karşıtı · söyleneni duymazdan gelmek ve önemsememek
  الدبر خلاف القبل (maqayis;jamhara;sihah;tahdhib;mufradat)؛ جعلت قوله دبر أذني (maqayis;jamhara;sihah;tahdhib)
- **B002** sonuna erip geçme — günün sonuna gelmesi veya geçip gitmesi · ibadetlerin son bölümleri ya da hemen sonrası · geçip gitmiş dün · bir sürenin son vakti
  دبر النهار وأدبر إذا جاء آخره (maqayis;sihah;tahdhib;mufradat)؛ أدبار السجود أواخر الصلوات (tahdhib;mufradat)؛ أمس الدابر الذاهب (jamhara;sihah;tahdhib)؛ الدبر الموت (tahdhib)
- **B003** sırtını dönüp uzaklaşma — sırtını dönmek, yüz çevirmek veya kaçmak · yenilgi; bağlama göre savaşta üstünlük
  الإدبار خلاف الإقبال (jamhara;sihah;mufradat)؛ يولون الدبر (tahdhib;mufradat)؛ جعلت كلامه دبر أذني أي أعرضت عنه (maqayis;jamhara;sihah;tahdhib)؛ الدبرة الهزيمة (sihah;tahdhib)
- **B004** son izine kadar yok etme — bir topluluğun son kalanını ve soyunu tümüyle yok etmek · yok oluş ve iz kalmaması
  قطع الله دابرهم أي آخر من بقي منهم (maqayis;sihah;tahdhib;mufradat)؛ الدبار الهلاك وانقطاع الأثر (jamhara;sihah;tahdhib;mufradat)؛ الدابر الأصل والعقب (tahdhib)
- **B005** karşılıklı sırt çevirip bağ kesme — birine sırt çevirip düşmanlık etmek · karşılıklı ilişkiyi kesip düşmanlaşmak
  دابرت فلانا عاديته (maqayis;sihah;mufradat)؛ لا تدابروا (maqayis;sihah;tahdhib;mufradat)؛ تدابر القوم إذا تقاطعوا وتعادوا (jamhara;sihah;tahdhib)
- **B006** sonucunu düşünerek planlama — bir işi sonucunu düşünerek planlamak · bir işin sonunu ve sonuçlarını düşünüp değerlendirmek
  التدبير أن يدبر الإنسان أمره (maqayis)؛ التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته (sihah;tahdhib)؛ التدبير التفكر في دبر الأمور (mufradat)
- **B007** ölümden sonra özgür bırakma — köle durumundaki kişiyi sahibinin ölümünden sonra özgür bırakma · sahibi öldükten sonra özgür olacak köle durumundaki kişi
  التدبير عتق الرجل عبده أو أمته عن دبر (maqayis)؛ عبد مدبر إذا قيل له إذا مت فأنت حر (jamhara)؛ التدبير عتق العبد عن دبر (sihah;mufradat)؛ أن يعتق الرجل عبده بعد موته (tahdhib)
- **B008** başkasından söz aktarma — 
  دبرت الحديث عن فلان إذا حدثت به عنه (maqayis)؛ دبرت الحديث إذا حدثت به عن غيرك (sihah;tahdhib)؛ ليس بمعروف وإنما هو يذبره (tahdhib)
- **B009** arka uzuv bölümü — kuşun ayağındaki arka parmak · toynağın bileğe yakın arka bölümü · insanın topuk arkası
  دابرة الطائر الإصبع التي في مؤخر رجله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ دابرة الإنسان عرقوبه (jamhara;sihah;tahdhib)؛ دابرة الحافر ما حاذى مؤخر الرسغ (maqayis;sihah;tahdhib;mufradat)
- **B010** geriye yönelmiş işleme — ipliğin geriye doğru bükülen bölümü · kulağının arka tarafı yarılmış hayvan · kulağın arkasındaki yarık veya kıvrım
  الدبير ما أدبرت به المرأة من غزلها (maqayis;sihah;mufradat)؛ القبيل ما فتلته إلى قدام والدبير ما فتلته إلى خلف (jamhara;tahdhib)؛ الشاة مدابرة تشق أذنها من قبل قفاها (maqayis;jamhara;sihah;tahdhib;mufradat)
- **B011** iki yandan arı soylu [kalıp] — hem anne hem baba yönünden arı ve saygın soylu
  رجل مقابل مدابر كريم النسب من قبل أبويه (maqayis)؛ مقابل ومدابر إذا كان محضا من أبويه (jamhara;sihah;tahdhib;mufradat)
- **B012** karşıt yönlü batı rüzgârı — karşı yöndeki rüzgârın zıddı sayılan batı rüzgârı · rüzgârın bu batı yönlü türe dönüşmesi
  الدبور ريح تقبل من دبر الكعبة (maqayis)؛ الدبور الريح المعروفة (jamhara;mufradat)؛ الدبور الريح التي تقابل الصبا (sihah;tahdhib)؛ دبرت الريح إذا صارت دبورا (jamhara;sihah)
- **B013** öndeki kümeyi izleyen yıldız — belirli yıldız kümesini izleyen yıldız veya küçük yıldız kümesi
  الدبران نجم سمي بذلك لأنه يدبر الثريا (maqayis;tahdhib)؛ الدبران معروف لأنه يدبر الثريا (jamhara)؛ الدبران خمسة كواكب من الثور (sihah)؛ الدابر يقال للتابع (mufradat)
- **B014** arı topluluğu — arı ve eşek arısı topluluğu · bu topluluğun tek bir arısı
  الدبر النحل الواحدة دبرة (jamhara;mufradat)؛ الدبر جماعة النحل ويجمع على دبور (sihah)؛ الدبر النحل وجمعه دبور (tahdhib)؛ الدبر النحل والزنابير ونحوهما مما سلاحها في أدبارها (mufradat)
- **B015** ekim alanındaki tarla parçası — ekim alanındaki tarla bölmeleri · ekim alanındaki tek tarla bölmesi
  الدبار المشارات من الزرع (maqayis)؛ الدبار واحدها دبارة وهي المشارات (jamhara)؛ الدبرة والدبارة المشارة في المزرعة (sihah)؛ الدبار المشارات واحدتها دبرة (tahdhib)؛ الدبرة من المزرعة جمعها دبار (mufradat)
- **B016** çok miktarda mal — çok ve kalıcı mal · çok malı olan kişi
  المال الكثير يقال مال دبر (maqayis;jamhara;sihah;tahdhib)؛ المدبور الكثير المال (tahdhib)؛ الدبر المال الكثير الذي يبقى بعد صاحبه (mufradat)
- **B017** hayvan sırtındaki yara — devenin veya başka bir hayvanın sırtındaki yara · hayvanın sırtında yara oluşmak
  الدبرة في ظهر البعير وغيره (jamhara)؛ أدبرت البعير فدبر (sihah)؛ دبر البعير يدبر دبرا (tahdhib)؛ دبر البعير دبرا فهو أدبر ودبر (mufradat)
- **B018** okun hedefin arkasına düşmesi — okun hedefi geçip arkasına düşmesi · hedefin arkasına çıkan ok
  دابر من السهام الذي يخرج من الهدف (maqayis;sihah)؛ دبر السهم الهدف إذا سقط وراءه (jamhara)؛ دبر السهم الهدف إذا صار من وراء الهدف (tahdhib)؛ دبر السهم الهدف سقط خلفه (mufradat)
- **B019** bahisli çekimde kaybeden ok — bahisli ok çekiminde kazanamayan ok · bahisli oyunda malını yitirmek
  الدابر من القداح الذي لم يخرج وهو خلاف الفائز (maqayis)؛ الدابر من القداح خلاف الفائز وصاحبه مدابر (sihah)؛ المدابر الذي يضرب بالقداح (tahdhib)؛ دبر بالقمار إذا ذهب به (maqayis)
- **B020** Çarşamba gününün eski adı — Çarşamba gününün eski dönemlerdeki adı
  دبار اسم يوم الأربعاء وفي مثل هذا نظر (maqayis)؛ دبار اسم يوم أحسبه يوم الأربعاء (jamhara)؛ دبار اسم يوم الأربعاء من أسمائهم القديمة (sihah)؛ دبار يوم الأربعاء (tahdhib)؛ سمي يوم الأربعاء في الجاهلية دبارا (mufradat)
- **B021** denizde su basıp açılan yükselti — denizde su yükselince örtülen, çekilince açılan ada benzeri yer
  الدبر قطعة تغلظ في البحر كالجزيرة يعلوها الماء وينضب عنها (jamhara)
- **B022** güreşte özel düşürme tutuşu — güreşte rakibi düşürmeye yarayan özel tutuş
  الدابرة ضرب من أخذ الصرع (maqayis)؛ الدابرة ضرب من الشغزبية في الصراع (sihah;tahdhib)

## ع ص م (root_001021): 40:33 عَاصِمٍ

- **B001** engelleyerek koruma ve koruyucuya tutunma — engelledi, korudu, zarardan uzak tuttu · engelleme, koruma ve zarardan uzak tutma · engelleyen veya koruyan · korunmuş, zarardan uzak tutulmuş · sığındı, tutundu, direnip kaçındı · Tanrı'ya sığınıp onun korumasına tutundu · Tanrı'nın ahdine sıkıca tutundu · direndi, boyun eğmedi, sıkıca tutundu · bir şeye sığındı veya sıkıca bağlandı · düşmemek için atının yelesine veya bir bağa tutunan beceriksiz binici · yemek onu açlıktan korudu · kavrulmuş tahıl içeceği için kullanılan takma ad · arkadaşından ayrılmadı, ona bağlı kaldı
  يدل على إمساك ومنع وملازمة (maqayis)؛ العصمة أن يعصمك الله من الشر أي يدفع عنك (ayn)؛ العصمة المنع، والعصمة الحفظ، واعتَصمت بالله (sihah)؛ العصمة في كلام العرب المنع، وامتنع به، واستعصم إذا امتنع وأبى (tahdhib)؛ العصم الإمساك، والاعتصام الاستمساك، واستعصم استمسك (mufradat)
- **B002** bağlayıcı kayış ve tutunma desteği — ona tutunabileceği bir destek hazırladı · tutunulan her türlü destek · bağlamaya ve tutunmaya yarayan ip veya kayış · su kabını bağlayıp taşımaya yarayan kayış · yük taşıma düzeneğinin iki yanını sıkan bağ · su kabına taşıma kayışı taktı veya onu kayışla bağladı · bağlayıp tutmaya yarayan bağlar
  أعصمت فلانا أي هيأت له شيئا يعتصم بما نالته يده (maqayis)؛ أعصمت أي لجأت إلى شيء اعتصمت به (ayn)؛ العصام رباط القربة، وأعصمت القربة جعلت لها عصاما، وأعصمت فلانا إذا هيأت له ما يعتصم به (sihah)؛ عصام المحمل شكاله وقيده، والعصام رباط القربة، والحبال التي تنشب في خرب الروايا (tahdhib)؛ العصام ما يعصم به أي يشد (mufradat)
- **B003** çevreleyici takı ve takıldığı bilek bölgesi — kolye veya bilezik benzeri takı · ön kolun bilezik takılan bölümü · köpeklerin boynundaki sarkan bağlar veya tasmalar
  العصمة القلادة (maqayis;sihah)؛ معصم المرأة موضع السوارين من ساعديها (maqayis)؛ المعصم موضع السوار من الساعد (sihah)؛ أعصام الكلاب عذباتها التي في أعناقها (tahdhib)؛ معصما المرأة موضعا السوارين من ساعديها (tahdhib)؛ العصمة شبه السوار، والمعصم موضعها من اليد (mufradat)
- **B004** maddeden kalan artık veya iz — katran, boya veya benzeri maddeden kalan artık ve iz · boyar maddeden kalan kalıcı iz · kınandan kalan veya akıp ayrılan pay
  العصيم وهو الصدأ من الهناء والبول ييبس على فخذ الناقة، وأثر الخضاب عصيم، والعصم أثر كل شيء من ورس أو زعفران (maqayis)؛ العصيم بقية كل شيء وأثره من القطران والخضاب ونحوه، والعصم بالضم مثله (sihah)؛ العصيم بقية كل شيء وأثره من القطران والخضاب ونحوه، والصدأ من العرق والهناء والدرز والوسخ والبول، والعصم أثر كل شيء من ورس أو زعفران (tahdhib)
- **B005** hayvanın ön uzvundaki beyaz işaret — hayvanın bileğinde veya ön uzvunda bulunan beyazlık · ön uzvunda ya da kanadında beyaz işaret bulunan hayvan · ön uzvunda beyaz işaret bulunan dişi hayvan · ön uzuvları beyaz işaretli hayvanlar veya dağ keçileri
  العصمة البياض يكون برسغ ذي القوائم، والوعل الأعصم وعصمته بياض في رسغه، وغراب أعصم (maqayis)؛ الغراب الأعصم الذي في جناحه ريشة بيضاء، والأعصم من الظباء والوعول الذي في ذراعيه بياض، والاسم العصمة (sihah)؛ الغراب الأعصم الأبيض اليدين، والأعصم من الظباء والوعول الذي في ذراعيه بياض، والعصمة في الخيل بياض بيديه دون رجليه (tahdhib)؛ قيل للبياض بالرسغ عصمة تشبيها بالسوار، وعلى هذا قيل غراب أعصم (mufradat)
- **B006** tüyü üzerinde bırakılmış kuru deri — tüyü alınmadan üzerinde bırakılmış deri · tüyü üzerinde kurumuş veya tüyü alınmamış ham deri
  المعصم الجلد لم ينح وبره عنه بل ألزم شعره لأنه لا ينتفع به، يقال أعصمنا الإهاب (maqayis)؛ المعصم الجلد الذي يجف بشعره ولم يعطن لأنه أعصم أي ألزم شعره، وإهاب عصيم وأهب عصم (tahdhib)
- **B007** edinmek — edindi, kazandı
  عصم يعصم عصما: اكتسب (sihah)
- **B008** çok yiyen kişi — çok yiyen; kadın için ayrıca uzun uyuyan ve uyanınca anlaşılmaz sesler çıkaran · çok yiyen, obur erkek
  عيصوم فيقال هي الأَكول، ومنهم من يرويه بالضاد معجمة (sihah)؛ العيصوم من النساء الكثيرة الأكل الطويلة النوم المدمدمة إذا انتبهت، ورجل عيصوم وعيصام إذا كان أكولا (tahdhib)

## ز ي ل (root_000659): 40:34 زِلْتُمْ

- **B001** ayırt ederek ayırma ve ayrışma — ayrışma ve farklılaşma · onları birbirinden ayırmak · bir şeyi ayırt edip ayırmak · koyunları keçilerden ayırmak · onu ayırıp ayrışmasını sağlamak · birbirinden ayrılma · ondan ayrılmak · farklılaşıp ayrışma · dağılıp birbirinden ayrılmak · onların arasını ayırmak
  التزيل التباين وزيلت بينهم أي فرقت (ayn); زلت الشيء أي مزته وفرقته وزيلته فتزيل والمزايلة المفارقة والتزايل التباين (sihah); تزيلوا تفرقوا وفزيلنا بينهم (mufradat)
- **B002** yerinden giderme veya hareketsiz bırakma [kalıp] — bir şeyi bulunduğu yerden çıkarmak · başına bela ve ölüm gelsin diye beddua etmek · başına bela ve ölüm gelsin diye beddua etmek · varlığını veya işini ortadan kaldırmak · korkudan yüreğini yerinden oynatmak · hareketini ortadan kaldırıp hareketsiz bırakmak
  زلت الشيء من مكانه أزيله زيلا لغة في أزلته (sihah); زال الله زواله وأزال الله زواله بمعنى إذا دعا عليه بالبلاء والهلاك (sihah); زيل قلبها من الفزع (sihah); زاله يزيله زيلا أي أذهب الله حركتها (mufradat); زال منها زويلها (mufradat)
- **B003** süreklilik bildiren yardımcı yapı — yapmayı sürdürmek; hâlâ yapmak · yapmayı hâlâ sürdürmek · bir işi yapmayı sürdürmek; edilgenlik bildirmemek
  ما زال فلان يفعل كذا يريد دوام ذلك (ayn); ما زيل فلان يفعل ذلك لا يراد به معنى مفعول مجهول (ayn); ما زال ولا يزال خصا بالعبارة وأجريا مجرى كان (mufradat); أصله من الياء لقولهم زيلت ومعناه معنى ما برحت (mufradat)
- **B004** uylukların ayrık duruşu — uylukların birbirinden açık durması
  الزيل بالتحريك تباعد ما بين الفخذين كالفحج (sihah)

## ECHO ز و ل (root_000655): for 40:34 زِلْتُمْ: withheld observed target; not identity

- **B001** yer veya konumdan ayrılma ve ayırma — yerinden ya da bulunduğu konumdan ayrılmak · güneşin tepe noktasından batıya kayması · iktidarın elden gitmesi · yerinden ya da bulunduğu konumdan uzaklaştırmak · yerinden kaldırıp uzaklaştırmak · topluluğun bulunduğu yerden çekilmesi · bulunduğu konumdan ayrılma ya da geçiş
  تنحي الشيء عن مكانه؛ زال الشيء زوالا؛ أزلته عن المكان وزولته عنه (maqayis)؛ والزوال ذهاب الملك؛ زوال الشمس (ayn)؛ زال الشيء من مكانه يزول زوالا وأزاله غيره وزوله (sihah)؛ زال القوم عن مكانهم إذا حاصوا عنه وتنحوا؛ لا يستطيع من منزلة زويلا ولا حويلا (tahdhib)؛ زال الشيء يزول زوالا فارق طريقته جانحا عنه؛ أزلته وزولته (mufradat)
- **B002** yerinde durmayıp hareket etme — yerinde durmayan hareketli canlı ya da şey · atların binicileriyle birlikte hareket etmesi · hareket etmek, kımıldamak · yürürken çok kıpırdayan kimse · ağlama, kaygı ve huzursuz hareket
  الزائلة كل شيء يتحرك (maqayis)؛ زالت الخيل بركبانها زوالا (ayn)؛ الزوال الذي يتحرك في مشيته كثيرا؛ الزائلة كل شيء يتحرك (sihah)؛ الزول الحركة؛ رأيت شبحا ثم زال أي تحرك؛ الزائلة كل ذي روح من الحيوان يزول عن موضعه ولا يقر في مكانه؛ أخذه البكاء والقلق والحركة (tahdhib)؛ الزوال التصرف؛ أذهب الله حركتها (mufradat)
- **B003** bir şeyi ele alıp onunla uğraşma — bir şeyi ele alıp onunla uğraşma ve onu deneme · bir gereksinimi gidermek için uğraşmak · biriyle uğraşmak ya da çekişmek · birbirleriyle uğraşmak ya da çekişmek
  المزاولة المعالجة في الأشياء (ayn)؛ المزاولة مثل المحاولة والمعالجة؛ تزاولوا تعالجوا؛ يزاولنا عن نفسه ونزاوله (sihah)؛ المزاولة معالجة الرجل الشيء ومحاولته؛ فلان يزاول حاجة له؛ زاولته مزاولة إذا عالجته (tahdhib)
- **B004** biçime bağlı adlandırmalar — çevik ve zarif erkek ya da genç · çevik, gözü açık ya da toplum içinde görünür kadın · çevik ve zarif erkekler ya da gençler · şahin · erkeklik organı · yiğit ya da cömert kişi
  امرأة زولة أي خفيفة (maqayis)؛ الزول الفتى الخفيف الظريف؛ وصيفة زولة؛ فتيان أزوال (ayn)؛ الزول الرجل الخفيف الظريف؛ المرأة زولة؛ هي الفطنة الداهية (sihah)؛ الزول الغلام الظريف؛ الزول الصقر؛ الزول فرج الرجل؛ الزول الشجاع؛ الزول الجواد؛ الزولة المرأة البرزة (tahdhib)
- **B005** şaşkınlık uyandıran olağan dışılık — şaşkınlık uyandıran olağan dışılık ya da böyle bir şey · şaşırtıcı, olağan dışı şey
  شيء زول أي عجب (maqayis)؛ الزول العجب (sihah)؛ الزول العجب (tahdhib)
- **B006** kalıba göre sarsılma, açığa vurma ya da ortadan kalkma [kalıp] — korkuya kapılmak ya da içindekini bütünüyle açığa vurmak · yok olup gitsin; görüntüsü ya da hareketi ortadan kalktı · korku ve iç sarsıntısı
  زيل منا زويلها (maqayis)؛ زال زوال فلان وزويله؛ أزال الله زوالها؛ زال الخيال زوالها (ayn)؛ زيل زويله أي بلغ مكنون نفسه؛ زيل زويله وزواله من الذعر والفرق؛ زال زواله إذا دعي عليه بالهلاك (tahdhib)؛ زال زوالها أي أذهب الله حركتها؛ زال منها زويلها (mufradat)
- **B007** ayırma ve birbirinden seçme — 
  ليست من زلت وإنما هي من زلت الشيء فأنا أزيله إذا فرقت؛ فزيلنا بينهم؛ زال الشيء من الشيء يزيله زيلا (tahdhib)؛ تزيلوا تفرقوا؛ فزيلنا بينهم؛ أصله من الياء لقولهم زيلت (mufradat)
- **B008** olmayı ya da yapmayı sürdürme — bir şeyi yapmayı ya da bir durumda olmayı sürdürmek · hâlâ yapmak ya da olmak; sürmekte olmak · siz hâlâ aynı durumda bulunuyordunuz
  ما زال فلان يفعل كذا؛ ما زيل يفعل كذا (sihah)؛ ما زال يفعل كذا ولا يزال؛ لا يتكلم به إلا بحرف نفي؛ يراد بهما ملازمة الشيء والحال الدائمة (tahdhib)؛ ما زال ولا يزال أجريا مجرى كان؛ معناه معنى ما برحت؛ فما زلتم في شك (mufradat)

## ECHO ز ل ل (root_000641): for 40:34 زِلْتُمْ: withheld observed target; not identity

- **B001** yerinden kayma veya kaydırma — kaymak veya bulunduğu yerden sapmak · ayağı kaymak · kaygan iniş yeri · ayağın kaydığı tutunmasız yer
  زل عن مكانه زليلا (maqayis)؛ زل السهم عن الدرع زليلا (ayn;tahdhib)؛ زلت قدمه (ayn;tahdhib)؛ زل في طين (sihah)؛ أزل فلان فلانا عن مكانه (tahdhib)؛ المزلة المكان الدحض (maqayis;ayn;sihah;tahdhib)؛ الزلة في الأصل استرسال الرجل من غير قصد (mufradat)
- **B002** istemeden yanlışa düşme — yanılmak; sözde veya inançta hata etmek · kasıtsız hata veya sürçme · kötü bir ayartıcının doğru yoldan saptırması · açığını kollayıp yanlışa sürüklemek
  الزلة الخطأ (maqayis)؛ زل في مقال أو نحوه (ayn;tahdhib)؛ أزله الشيطان عن الحق (ayn)؛ زل في دينه (tahdhib)؛ أزلهما الشيطان أي كسبهما الزلة (tahdhib)؛ الذنب من غير قصد (mufradat)؛ استزله إذا تحرى زلته (mufradat)
- **B003** arı ve berrak; su için tatlı ve kolay içimli — berrak, tatlı, serin ve kolay içimli su · saf ve katışıksız altın · seyrek bir anlatımla su içmek
  الماء الزلال العذب لأنه يزل عن ظهر اللسان (maqayis)؛ ماء زلال أي عذب (sihah)؛ ماء زلال صاف عذب بارد (tahdhib)؛ ماء زلال يزل في الحلق (tahdhib)؛ ذهب زلال صاف خالص (tahdhib)؛ ما زلزلت ماء قط أي ما شربت (tahdhib)
- **B004** taşınan yiyecek ya da ulaştırılan iyilik ve hak — taşınan yemek veya insanlara sunulan iyilik · birine iyilik ulaştırmak · birine hakkından bir şey vermek · çok hediye veren ve iyilik yapan kimse
  اتخذ فلان زلة للناس أي صنيعا (ayn)؛ الزلة اسم لما يحمل من المائدة (ayn;tahdhib)؛ أزللت إليه نعمة أي أسديت (sihah;tahdhib)؛ أزللت إليه من حقه شيئا أي أعطيت (sihah)؛ من أوصل إليه نعمة بلا قصد (mufradat)
- **B005** ölçüde veya payda eksiklik — paralar ağırlıkça eksik çıktı · ağırlığı eksik para · ölçülebilir eksiklik
  زلت الدراهم تزل زلولا أي نقصت في الوزن (sihah;tahdhib)؛ في ميراثه ذلل أي نقصان (tahdhib)؛ زلل أي نقصان (tahdhib)
- **B006** hafif ve hızlı ilerleme — hafif yürüyüş veya hızlı geçiş · koşmak veya hızla geçmek · hafif ve çevik delikanlı
  زل إذا عدا (maqayis)؛ الزليل مشي خفيف (ayn;tahdhib)؛ يزل زليلا خفيفا (ayn;tahdhib)؛ يزل من موضع إلى موضع لطلب الكلا (sihah)؛ زل يزل زليلا وزلولا إذا مر مرا سريعا (tahdhib)
- **B007** arka kısmı küçük ve az etli olma — arka kısmı küçük ve kalçaları hafif olan · belirgin kalçası olmayan kadın · arka kısmı küçük ve az etli yırtıcı hayvan
  الذئب الأزل وهو الأرسح (maqayis)؛ اللحم قد زل عن مؤخره (maqayis)؛ الأزل الأرسح (ayn)؛ امرأة زلاء (maqayis;ayn;sihah;tahdhib)؛ الأزل الخفيف الوركين (sihah)؛ السمع الأزل (ayn;sihah;tahdhib)؛ لا عجيزة لها (tahdhib)
- **B008** şiddetle sarsma veya sarsılma — şiddetle sarsma veya sarsılma · sarsıntı · büyük sıkıntılar ve dehşet verici olaylar · bir topluluğu korkutup sarsmak · huzursuzluk veya sarsıntılı durum
  تزلزلت الأرض اضطربت (maqayis)؛ الزلزل كالقلق (maqayis)؛ الزلزلة تحريك الشيء (ayn)؛ زلزل الله الأرض زلزلة وزلزالا (sihah)؛ الزلازل البلايا (ayn)؛ الزلازل الأهوال (tahdhib)؛ زلزلوا أي خوفوا وحذروا (tahdhib)؛ زعزعوا من الرعب (mufradat)
- **B009** ev eşyası — ev eşyası ve döşeme gereçleri · ev eşyası
  الزلزل الأثاث والمتاع (maqayis;sihah;tahdhib)؛ الزلز أيضا (tahdhib)؛ احتمل القوم بزلزهم (tahdhib)؛ قماش البيت (tahdhib)

## ش ك ك (root_000812): 40:34 شَكٍّ

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

## ه ل ك (root_001596): 40:34 هَلَكَ

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

## ب ع ث (root_000129): 40:34 يَبْعَثَ

- **B001** durgun olanı harekete geçirme — harekete geçirmek; uyandırmak · devenin bağını çözüp onu ayağa kaldırmak · uyuyanı uyandırmak · kargaşanın kabarmaları ve alevlenmeleri · neredeyse hiç uyumayan adam · neredeyse hiç çökmeyen dişi deve
  الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)
- **B002** gönderme veya yöneltme — göndermek; yöneltmek · görevle göndermek; yola çıkarmak · birini bir iş için göndermek · birini bir işi yapmaya isteklendirip yöneltmek · asker birliğini düşmana karşı göndermek · göreve gönderilmiş topluluk veya birlik · gönderilmiş ordular
  البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)
- **B004** yola koyulup ilerleme — harekete geçip ilerlemek; hızlanmak · yola koyulma ve ilerleme · şiir benden akıp geldi
  انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)

## ر ي ب (root_000616): 40:34 مُّرْتَابٌ, 40:59 رَيْبَ

- **B001** kuşku ve güvensizlik — kuşku ve zihinsel kararsızlık · suçlayıcı kuşku ve güven eksikliği · bende kuşku ve korku uyandırdı · bende kuşku uyandırdı · kuşkulu duruma geldi veya kuşku uyandırır oldu · ondan veya o şeyden kuşkulandı · onda kuşku uyandıran bir belirti gördü · kuşku duyan veya kuşku uyandıran
  الريب الشك (maqayis;ayn;jamhara;sihah)؛ الريب التهمة (jamhara)؛ ما رابك من أمر تخوفت عاقبته (ayn)؛ رابني هذا الأمر إذا أدخل عليك شكا وخوفا (maqayis;ayn)؛ الريبة اسم من الريب تدل على دغل وقلة يقين (mufradat)؛ أراب الرجل صار ذا ريبة (maqayis;ayn;sihah)؛ ارتبت به أي ظننت به (ayn)
- **B002** zamanın değişimleri ve olayları [kalıp] — zamanın değişimleri, olayları ve terslikleri · ölümün ne zaman geleceğine ilişkin korkulan olaylar
  ريب الدهر صروفه (maqayis;jamhara;mufradat)؛ الريب صرف الدهر وعرضه وحدثه (ayn)؛ ريب المنون حوادث الدهر (sihah)؛ ريب المنون من جهة وقته لا من جهة كونه (mufradat)
- **B003** karşılanması gereken gereksinim — elden kaçırma kaygısıyla aranan gereksinim
  الريب الحاجة (sihah)؛ فيقال إن الريب الحاجة (maqayis)؛ طالب الحاجة شاك على ما به من خوف الفوت (maqayis)

## غ ي ر (root_001119): 40:35 بِغَيْرِ, 40:40 بِغَيْرِ, 40:56 بِغَيْرِ, 40:75 بِغَيْرِ

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

## ط ب ع (root_000926): 40:35 يَطْبَعُ

- **B001** mühürleyerek iz bırakma ve belirli biçimde yapma — bir şeyin üzerine mühür basmak · kalbi öğüde ve doğru yönelişe kapatmak · mühür; mühür basma aracı · parayı basmak; kılıcı işleyip tamamlamak · kilden testi veya tuğla yapıp biçimlendirmek · demiri işleyip düzelten usta · basımcılık; baskı işi · hükümdarın belgeleri mühürlemekte kullandığı kil parçası
  الطابع الخاتم يختم به (maqayis)؛ طبعت على الكتاب أي ختمت (jamhara;sihah)؛ طبع الله على قلب الكافر أي ختم عليه (maqayis;tahdhib)؛ أن تصور الشيء بصورة ما كطبع السكة وطبع الدراهم (mufradat)؛ طبعت الدرهم والسيف أي عملت (sihah)؛ طبعان الأمير طينه الذي يختم به الكتب (tahdhib)
- **B002** yaratılıştan gelen yapı ve huy — insanın doğuştan gelen huyu ve yaradılışı · bir varlığın yaratılıştan gelen temel yapısı · doğuştan gelen huylar ve yaradılış özellikleri
  طبع الإنسان وسجيته (maqayis)؛ الطبع السجية التي جبل عليها الإنسان (sihah)؛ الطبيعة الخليقة التي جبل عليها (jamhara)؛ طبع الله الخلق على الطبائع (tahdhib)؛ الطبيعة التي هي السجية (mufradat)
- **B003** son sınırına kadar doldurma veya dolma — ölçeği, kovayı veya su kabını ağzına kadar doldurmak · nehir dolup taşmak · yüküyle iyice ağırlaşmış veya et ve yağla dolgunlaşmış dişi deve · doluluk; ağzına kadar dolu şey
  ملء المكيال طبع (maqayis)؛ طبعت الدلو إذا ملأتها (jamhara)؛ طبعت السقاء تطبيعا ملأته فتطبع أي امتلأ (sihah;tahdhib)؛ ناقة مطبعة مثقلة بحملها (jamhara;sihah;tahdhib)؛ طبعت المكيال إذا ملأته (mufradat)
- **B004** nehir; suyla dolu nehir — nehir; suyla dolu nehir · nehirler; suyla dolu nehirler
  الطبع النهر والجمع الطباع (maqayis)؛ الطبع النهر المملوء ماء (jamhara)؛ الطبع بالكسر النهر والجمع أطباع (sihah)؛ الطبع في بيت لبيد ما قاله الأصمعي أنه النهر (tahdhib)
- **B005** pas, yoğun kir ve bunlardan aktarılan kusur — pas, yoğun kir, leke ve kusur · kılıcın yüzeyini pas veya kir kaplamak · erdemli işlerde ilerleme gücü olmayan kusurlu kişi · tembelleşmek
  الطبع الوسخ الشديد على السيف (ayn)؛ الطبع الصدأ (jamhara;sihah)؛ أصل الطبع الصدأ يكثر على السيف وغيره (tahdhib)؛ طبع السيف صدؤه ودنسه (mufradat)؛ رجل طبع (maqayis;ayn;tahdhib;mufradat)؛ طبع بمعنى كسل (sihah)
- **B006** örnek alınan kalıp, biçim ve ölçü — örnek, kalıp, biçim ve ölçü · bunu onun örneğine ve ölçüsüne göre yap
  الطبع المثال (tahdhib)؛ اضربه على طبع هذا وعلى غراره وصيغته وهديته أي على قدره (tahdhib)
- **B007** enseye vururken eli etkili biçimde ulaştırmak — elini ensesine sağlamca indirmek
  إذا مكنت اليد من القفا قلت طبعت قفاه (tahdhib)
- **B008** bölgesel olarak bilinen çok zararlı bir böcek — kaynakta belirtilen bölgede çok zararlı olan bir böcek
  الطبوع دابة من الحشرات شديدة الأذى بالشأم (tahdhib)

## ج ب ر (root_000216): 40:35 جَبَّارٍ

- **B001** kırığı onarma veya eksikliği giderip yeniden bütünleme — kırık kemiği onarıp kaynatmak · kemiğin kaynaması veya kırığın iyileşmesi · yoksulun ihtiyacını giderip onu yeterli duruma getirmek · inanç düzenini düzeltip tamamlamak · yenmiş veya kurumuş bitkinin yeniden sürmesi · ihtiyacı giderdiği için ekmeğe verilen ad · hesapta eksikliği gidermek için bir nicelik ekleme işlemi · kırık kemikleri onarıp kaynatan kişi
  جبرت العظم فجبر (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ جبرت فاقة الرجل إذا أغنيته (ayn;sihah;tahdhib)؛ قد جبر الدين الإله فجبر (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ تجبر النبت بعد الأكل (sihah;tahdhib;mufradat)؛ الخبز جابر بن حبة (sihah;tahdhib;mufradat)
- **B002** erişilemeyecek ölçüde yükselme ve kendini büyük görme — el erişmeyecek kadar uzun, iri ve güçlü · kendini büyük gören, kibirli ve öğüt kabul etmeyen · kibir, büyüklük taslama ve kendini üstün görme · Tanrı için: erişilemez yücelikte olan veya yaratılanlara dilediğini yaptıran
  الجبار الذي طال وفات اليد (maqayis)؛ الجبار من النخل الذي قد بلغ غاية الطول (ayn)؛ الجبار من النخل الذي قد فات اليد (jamhara;sihah;tahdhib;mufradat)؛ رجل جبار طويل عظيم قوي (tahdhib)؛ الجبار من الناس العظيم في نفسه (ayn)؛ فيه جبرية وجبروة وجبروت وجبورة (maqayis;ayn;sihah;tahdhib)؛ قلب جبار ذو كبر (ayn;tahdhib;mufradat)
- **B003** birini istemediği bir şeye zorla yöneltme — Tanrı için: erişilemez yücelikte olan veya yaratılanlara dilediğini yaptıran · birini istemediği işe zorlamak · zorla egemen olan veya haksız yere öldüren kişi · insan eylemlerini zorunlu sayıp özgür seçimi reddeden öğreti
  أجبرت فلانا على الأمر (maqayis;sihah;tahdhib;mufradat)؛ الجبر أن تجبر إنسانا على ما لا يريد (ayn)؛ أجبرت الرجل إذا أكرهته عليه (jamhara)؛ الجبار القاهر المسلط (tahdhib;mufradat)؛ الجبار القتال في غير حق (tahdhib)؛ الجبر خلاف القدر والجبرية (sihah;tahdhib;mufradat)
- **B004** tazmin sorumluluğu doğurmayan zarar — bedeli ödenmeyen ve kimseye yüklenmeyen zarar · hayvan, kuyu veya maden kaynaklı olup tazmin edilmeyen zarar
  الجبار وهو الهدر (maqayis;sihah;tahdhib)؛ العجماء جبار أي ما أصاب الدابة فهو هدر (ayn;sihah;tahdhib)؛ الجبار الذي لا أرش له (jamhara)؛ الجبار لما يسقط من الأرش (mufradat)؛ البئر جبار والمعدن جبار (maqayis;sihah;tahdhib)
- **B005** kırığı sabitleyen atel ve ona benzeyen kol takısı — kırığı sabitlemek için bağlanan tahta, çubuk veya bez · atele biçimce benzeyen bilezik veya kol halkası · kırık kemikleri onarıp kaynatan kişi
  الخشب الذي يضم به العظم الكسير جبارة والجمع جبائر (maqayis)؛ الجبارة الخشبة توضع على الكسر (ayn)؛ الجبارة واحدة الجبائر وهو الخشب الذي يشد على العضو المكسور (jamhara)؛ العيدان التي تجبر بها العظام (sihah)؛ الخشبات التي توضع على موضع الكسر (tahdhib)؛ الجبيرة للخرقة والجبارة للخشبة (mufradat)؛ الجبارة دملوج المرأة من الحلي (ayn;jamhara;sihah;tahdhib;mufradat)
- **B006** biçime bağlı adlandırmalar — eski kullanımda salı gününe verilen ad · aynı söz ailesinden türetilmiş kişi adları · kaynağa göre hükümdar, adam veya yiğit kişi · farklı söylenişleri bulunan bir melek adı ve öğelerine ilişkin açıklama
  الجبار اسم يوم الثلاثاء (ayn;jamhara;sihah;tahdhib)؛ سمت العرب جبرا وجبيرا وجابرا (jamhara)؛ جبرائيل اسم وفيه لغات (sihah)؛ جبر هو الرجل وإيل الربوبية (tahdhib)؛ الجبر الملك (jamhara;tahdhib)

## ص ر ح (root_000854): 40:36 صَرْحًا

- **B001** açığa çıkma, açığa çıkarma ve açıkça söyleme — içindekini açıkça söylemek; işi açığa çıkarıp açıklamak · açık ve doğrudan anlatım; üstü kapalı anlatımın karşıtı · açıkça ve alenen; yüz yüze · açık ve yüz yüze konuşma · onunla açık seçik konuştu · gerçek gizlendikten sonra açığa çıktı
  أصل يدل على ظهور الشيء وبروزه (maqayis)؛ صرح بما في نفسه أظهره (maqayis;sihah;mufradat)؛ صرحت الأمر تصريحا إذا كشفته وأوضحته (jamhara)؛ التصريح خلاف التعريض (sihah;mufradat)؛ جاء صراحا جهارا (maqayis;ayn;mufradat)؛ مصارحة وصراحا كفاحا ومواجهة (maqayis;sihah)
- **B002** katışıksız ya da örtüsünden arınmış olma — saf, katışıksız ve arı · her şeyin katışıksız olanı · soyu temiz ve karışmamış · soyları veya bağlılıkları karışmamış olanlar · safkan atlar · köpüğü çekilmiş saf süt · başka bir içecekle karıştırılmamış içki dolu kadeh · içkinin köpüğü gitti ve içki duruldu · bulutsuz gün · katışıksız ve içten öğüt · katışıksız gerçek · bağlılığı başka bağlarla karışmamış kimse · kamburlaştı ve şiddeti katıksızlaştı · her şeyin katışıksızı; baştaki ünsüzün sonradan eklendiği düşünülen tartışmalı biçim
  الصريح المحض الحسب وكل خالص صريح (maqayis;ayn)؛ الصرح والصريح الخالص من كل شيء (ayn;sihah)؛ اللبن الصريح إذا ذهبت رغوته (ayn;jamhara;sihah;mufradat)؛ كأس صراح إذا لم تشب بمزاج (maqayis;ayn;sihah)؛ صرحت الخمر ذهب عنها الزبد (maqayis;ayn;sihah)؛ يوم مصرح ليس فيه سحاب (maqayis;sihah)
- **B003** yer, düz zemin ya da avlu alanı — 
  الصرحة المكان والمتن من الأرض (maqayis;ayn;sihah)؛ صرحة الدار ساحتها أو عرصتها (jamhara;sihah)؛ الصرح الأرض المملسة (jamhara)
- **B004** yüksekliği belirgin yapı — 
  الصرح بيت واحد يبنى منفردا ضخما طويلا في السماء وكل بناء عال (maqayis)؛ الصرح بيت منفرد يبنى ضخما طويلا في السماء (ayn)؛ الصرح القصر وكل بناء عال (sihah)؛ الصرح بيت عال مزوق (mufradat)
- **B005** çekirgeye benzeyen kuş — çekirgeye benzeyen bir kuş
  الصراح طائر كالجندب عربي صحيح (jamhara)

## ب ل غ (root_000151): 40:36 أَبْلُغُ, 40:56 بِبَٰلِغِيهِ, 40:67 لِتَبْلُغُوٓا۟, 40:67 وَلِتَبْلُغُوٓا۟, 40:80 وَلِتَبْلُغُوا۟

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

## س ب ب (root_000664): 40:36 ٱلْأَسْبَٰبَ, 40:37 أَسْبَٰبَ

- **B001** kesme ve bağı koparma — kesmek veya kesilmiş duruma getirmek · dişi devenin arka bacaklarını kesip onu yere düşürmek · karşılıklı olarak ilişkiyi kesmek · akrabalık bağını koparmak
  أصل هذا الباب القطع؛ السب العقر (maqayis)؛ أصل السب القطع (jamhara)؛ سبه أيضا بمعنى قطعه؛ التساب التقاطع (sihah)؛ السب القطع؛ سبسب إذا قطع رحمه (tahdhib)
- **B002** ağır sözlerle aşağılama — sövmek ve onuruna saldırmak · karşılıklı sövüşmek · insanlara çok söven kimse · çok sövülen veya çok söven adam · kişinin yüzüne vurulan ayıp · insanların birbirine söverken kullandığı konu · çok çirkin biçimde sövmek
  السب الشتم (maqayis)؛ سبه فلان سبا (ayn)؛ صار السب شتما لأن السب خرق الأعراض (jamhara)؛ السب الشتم؛ التساب التشاتم؛ السبة العار (sihah)؛ السب مصدر سببته سبا؛ عير بالبخل (tahdhib)؛ السب الشتم الوجيع؛ السبة ما يسب (mufradat)
- **B003** ulaştıran bağ veya araç — erişmek, tırmanmak veya inmek için kullanılan ip · başka bir şeye ulaştıran araç veya bağ · akrabalık, soy veya inanç bağı · istenen yere ulaştıran yol · göğün yönleri, katları veya girişleri · bir şeyi başka bir şeye ulaştıran araç kılma · ip · ipler
  الحبل فالسبب؛ أصل آخر يدل على طول وامتداد (maqayis)؛ السبب الحبل؛ كل ما تسببت به من رحم أو يد أو دين؛ سبب الأمر الذي يوصل به؛ الطريق (ayn)؛ السب بلغة هذيل الحبل (jamhara)؛ السبب الحبل؛ كل شئ يتوصل به إلى غيره؛ اعتلاق قرابة؛ أسباب السماء نواحيها (sihah)؛ السبب الحبل؛ المودة؛ تواصلهم؛ المنازل؛ أبوابها؛ كل شيء يتوصل به إلى شيء (tahdhib)؛ السبب الحبل الذي يصعد به النخل؛ كل ما يتوصل به إلى شيء سببا؛ ذريعة يتوصل بها (mufradat)
- **B004** ince örtü veya kumaş parçası — başörtüsü veya sarık · ince keten kumaş parçası · ince kumaşlar
  السب الخمار (maqayis)؛ السب الثوب الرقيق؛ السبيبة (ayn)؛ السب الشقة البيضاء من الثياب؛ العمامة؛ السبيبة (jamhara)؛ السب الخمار؛ العمامة؛ شقة كتان رقيقة؛ السبيبة (sihah)؛ السب الخمار؛ السبوب الثياب الرقاق؛ السبائب؛ السب العمامة (tahdhib)؛ سمي العمامة والخمار والثوب الطويل سببا (mufradat)
- **B005** uzunca bir zaman dilimi [kalıp] — geçmişten ayrılan uzunca bir zaman dilimi
  مضت سبة من الدهر يريد مضت قطعة منه (maqayis)؛ مضت سبة من الدهر وسنبة من الدهر أي ملاوة (jamhara)؛ ما رأيته منذ سبه أي منذ زمن من الدهر؛ مضت سبة من الدهر (sihah)؛ سبة من الدهر؛ الدهر سبات أي أحوال؛ أصابتنا سبة من برد (tahdhib)
- **B006** arka çıkış bölgesi — örtmeceyle anılan arka çıkış bölgesi · arka tarafından yaralamak
  السبة الدبر؛ طعنته في السبة (jamhara)؛ السبة الاست؛ طعنه في السبة (sihah)؛ السب الطبيجات؛ السبة وهي الدبر (tahdhib)؛ السبة ما يسب وكني بها عن الدبر (mufradat)
- **B007** sarkan perçem, yele veya kuyruk kılı — alın perçemi, yele veya kuyruk kılı
  السبيب شعر الناصية والعرف والذنب (sihah)؛ السبيب شعر الذنب؛ شعر الناصية (tahdhib)
- **B008** geniş ve çorak ıssız arazi — geniş, uzak ve çorak ıssız arazi
  السبسب المفازة الواسعة (maqayis)؛ السبسب المفازة (ayn)؛ السبسب المفازة؛ بلد سبسب (sihah)؛ السبسب الأرض القفر البعيدة؛ القفار؛ الأرض الشأسبة الجدبة (tahdhib)
- **B009** Hristiyanlara ait belirli bir bayram günü — Hristiyanlara ait bayram günü; özellikle Dallar Bayramı
  السباسب فيوم عيد لهم ولا أدري مم اشتقاقه (maqayis)؛ يوم السباسب يوم السعانين (ayn)؛ يوم السباسب يعني به عيدا لهم (sihah)
- **B010** övgüyle seçkin sayılan develer — övgüyle seçkin ve çok iyi sayılan develer
  الإبل مسببة؛ قاتلها الله فما أكرمها مالا (maqayis)؛ إبل مسببة أي خيار؛ قاتلها الله (sihah)؛ مسببة قب البطون؛ فمن نظر إليها سبها وقال لها قاتلها الله ما أجودها (tahdhib)
- **B011** sövüşmedeki karşı taraf ve denk — sövüşmede karşı taraf veya denk
  يقال للذي يساب سب؛ فلست بسبي (maqayis)؛ فلان سب فلان أي نظيره؛ فلست بسبي (jamhara)؛ سبك الذي يسابك؛ فلست بسبي (sihah)؛ سبك الذي يسابك؛ فلست بسبي (tahdhib)؛ السب المسابب؛ فلست بسبي (mufradat)
- **B012** işaret parmağı — işaret parmağı
  السبابة الإصبع بعد الإبهام (ayn)؛ السبابة من الاصابع التي تلى الابهام (sihah)؛ السبابة الإصبع التي تلي الإبهام وهي المسبحة (tahdhib)؛ السبابة سميت للإشارة بها عند السب؛ المسبحة (mufradat)
- **B013** yumuşak bir yürüyüşle ilerleme — yumuşak bir yürüyüşle ilerlemek
  سبسب إذا سار سيرا لينا (tahdhib)
- **B014** asılsız sözler ve saçmalıklar — asılsız sözler ve saçmalıklar
  منه قيل للأباطيل الترهات البسابس (tahdhib)

## ط ل ع (root_000945): 40:37 فَأَطَّلِعَ

- **B001** güneşin, ayın, yıldızın veya tanın doğması; doğuş olayı ve yeri [kalıp] — güneşin, tanın, yıldızın ya da ayın doğması · güneşin doğduğu yer veya yön · tanın sökmesi; tan vakti ya da tanın belirdiği yer
  المطلع الموضع الذي تطلع عليه الشمس؛ والمطلع مصدر من طلع (ayn)؛ طلعت الشمس والكوكب طلوعا ومطلعا؛ والمطلع موضع طلوعها (sihah)؛ طلعت الشمس؛ وكذلك طلع الفجر والنجم والقمر؛ المطلع بالفتح هو الطلوع والمطلع بالكسر هو الموضع (tahdhib)؛ طلع الشمس طلوعا ومطلعا؛ والمطلع موضع الطلوع (mufradat)؛ أصل واحد صحيح يدل على ظهور وبروز؛ طلعت الشمس طلوعا ومطلعا؛ والمطلع موضع طلوعها (maqayis)
- **B002** bir topluluğun karşısına çıkmak; ayrı kuruluşta onlardan gözden kaybolmak [kalıp] — topluluğun karşısına çıkmak, yanına gelmek ya da baskın verircesine belirmek; sınırlı bir aktarımda gözden kaybolmak · onların yanından ayrılıp gözden kaybolmak
  طلع علينا فلان يطلع طلوعا إذا هجم (ayn)؛ طلعت على القوم إذا أتيتهم؛ طلعت عنهم إذا غبت عنهم (sihah)؛ يقال طلع فلان علينا من بعيد؛ طلعت على صاحبي إذا أقبلت عليه؛ طلعت على القوم إذا غبت عنهم حتى لا يروك (tahdhib)؛ وعنه استعير طلع علينا فلان واطلع؛ وطلعت عنه غبت (mufradat)؛ طلع علينا فلان إذا هجم (maqayis)
- **B003** bir şeyi öğrenmek ya da başkasına gösterip bildirmek; görüşünü yoklamak [kalıp] — bir şeye yukarıdan bakmak veya iç yüzünü bütünüyle öğrenmek · başkasına bir işi ya da saklı sözü gösterip bildirmek · başını dışarı çıkarıp görünür kılmak · birinin görüşünü öğrenmek için ne düşündüğünü araştırmak · bir şeyi inceleyip içinde ne bulunduğunu öğrenmek
  أطلع فلان رأسه أظهره؛ اطلع أشرف على الشيء؛ أطلع غيره إطلاعا؛ أطلعني طلع هذا الأمر حتى علمته كله؛ استطلعت رأيه (ayn)؛ اطلعت على باطن أمره؛ طالعت الشيء أي اطلعت عليه؛ أطلعتك على سري؛ استطلعت رأي فلان (sihah)؛ اطلع فلان إذا أشرف على شيء؛ أطلع غيره؛ استطلعت رأي فلان إذا نظرت ما رأيه؛ أطلعني فلان (tahdhib)؛ اطلع؛ أطلع الغيب؛ أطلعتك على كذا؛ واستطلعت رأيه (mufradat)؛ أطلعتك على الأمر إطلاعا؛ أطلعتك طلعه؛ استطلعت رأي فلان إذا نظرت ما الذي يبرز إليك منه (maqayis)
- **B004** düşmanı gözlemek için önden gönderilen gözcü veya gözcü birliği — düşmanı gözlemek için önden gönderilen gözcü kişi veya birlik · önden gönderilen gözcü toplulukları
  الطليعة قوم يبعثون ليطلعوا طلع العدو؛ الطلائع الجماعات في السرية (ayn)؛ طليعة الجيش من يبعث ليطلع طلع العدو (sihah)؛ طليعة القوم الذين يبعثون ليطلعوا طلع العدو (tahdhib)؛ وطليعة الجيش أول من يطلع (mufradat)؛ وطليعة الجيش من يطلع طلع العدو (maqayis)
- **B005** palmiye ağacının kapalı çiçek salkımı; salkımın veya ekinin belirmesi — palmiye ağacının henüz açılmamış çiçek salkımı · kılıf içindeki tek bir palmiye çiçek salkımı · palmiye ağacının çiçek salkımını çıkarması · ekinin belirip görünmesi
  الطلع طلع النخلة الواحدة طلعة؛ وأطلعت النخلة؛ وطلع الزرع بدا (ayn)؛ والطلع طلع النخلة؛ واطلع النخل إذا خرج طلعه (sihah)؛ طلع الزرع إذا بدا؛ وأطلعت النخلة إذا أخرجت طلعها؛ الطلع كفراها قبل أن تنشق (tahdhib)؛ تشبيها بالطلوع قيل طلع النخل؛ لها طلع نضيد؛ وقد أطلعت النخل (mufradat)؛ والطلع طلع النخلة؛ وقد أطلعت النخلة (maqayis)
- **B006** dağa çıkma ve çıkış yolu; bir işin yaklaşım yönü veya ürkütücü eşiği [kalıp] — dağa tırmanıp çıkmak · dağa çıkılan yol veya dağa erişilen yön · bir işin ele alınacağı yön veya giriş yolu · yüksekten bakınca önünde açılan ağır durumun ürkütücülüğü
  طلعت الجبل أي علوته؛ المطلع المأتى؛ موضع الإطلاع من إشراف إلى انحدار (sihah)؛ طلعت الجبل إذا علوته؛ المطلع موضع الاطلاع من إشراف إلى الانحدار؛ وقد يكون المطلع المصعد؛ مطلع هذا الجبل مصعده ومأتاه؛ ما لهذا الأمر مطلع أي وجه ولا مأتى (tahdhib)؛ والمطلع المأتى؛ أين مطلع هذا الأمر أي مأتاه؛ هول المطلع (maqayis)
- **B007** bir alanı sınırına kadar doldurma; ayrı aktarımda güneşin gördüğü yeryüzü [kalıp] — yeryüzünü dolduracak çokluk; başka bir aktarımda güneşin gördüğü yeryüzü · avucu dolduran şey; özellikle gövdesi avucu dolduran yay · ağzına kadar dolu kap veya su gözü · ölçü kabını taşacak kadar doldurmak
  الطلاع ما طلعت عليه الشمس؛ وطلاع الأرض ملء الأرض؛ وقوس طلاع إذا كان عجسها يملأ الكف (ayn)؛ طلاع الشيء ملؤه؛ طلاع الأرض ملؤها؛ قوس طلاع الكف (sihah)؛ طلاع الأرض ملؤها حتى يطالع أعلى الأرض؛ طلاع الأرض ما طلعت عليه الشمس؛ قدح طلاع ممتلىء؛ عين طلاعة ممتلئة (tahdhib)؛ الطلاع ما طلعت عليه الشمس والإنسان؛ وقوس طلاع الكف ملء الكف (mufradat)؛ الطلاع ما طلعت عليه الشمس من الأرض؛ قوس طلاع الكف إذا كان عجسها يملأ الكف (maqayis)
- **B008** bir şeye istekle yönelme; bir görünüp bakıp bir gizlenme [kalıp] — bir şeye sürekli ve güçlü biçimde yönelen iç istek · bir görünüp bakıp bir geri çekilerek gizlenen kadın
  إن نفسك لطلعة إلى هذا الأمر؛ أي تتطلع إليه؛ وامرأة طلعة قبعة تنظر ساعة وتتنحى أخرى (ayn)؛ وتطلعت إلى ورود كتابك؛ ونفس طلعة؛ وامرأة طلعة (sihah)؛ نفسك لطلعة إلى هذا الأمر؛ وإنها لتطلع إليه أي لتنازع إليه؛ وامرأة طلعة قبعة تنظر ساعة ثم تختبىء ساعة (tahdhib)؛ امرأة طلعة قبعة تظهر رأسها مرة وتستر أخرى (mufradat)؛ ونفس طلعة تتطلع للشيء؛ وامرأة طلعة إذا كانت تكثر الإطلاع (maqayis)
- **B009** bir insanın görülüşü ve göz önündeki görünüşü — bir insanın yüzü, genel görünüşü veya görülüşü
  والطلعة الرؤية؛ ما أحسن طلعته أي رؤيته؛ حيا الله طلعتك (ayn)؛ والطلعة الرؤية (sihah)؛ طلعته رؤيته؛ يقال حيا الله طلعتك (tahdhib)؛ وطلعة الإنسان رؤيته لأنها تطلع (maqayis)
- **B010** okun nişan alınan yerin üstünden geçip arkasına düşmesi [kalıp] — yükselip nişan alınan yerin üstünden geçerek arkasına düşen ok · attığı ok nişan alınan yerin üstünden geçmek
  وأطلع الرامي أي جاز سهمه من فوق الغرض (sihah)؛ والطالع من السهام الذي يقع وراء الهدف؛ يسجد للطالع؛ شخص سهمه فارتفع عن الرمية (tahdhib)؛ ورمى فلان فأطلع وأشخص إذا مر سهمه برأس الغرض (maqayis)
- **B011** kusmak ve kusmuk — kusmak · kusmuk
  وأطلع أي قاء؛ والطلعاء القيء (sihah)؛ أطلع الرجل إطلاعا إذا قاء؛ الطولع الطلعاء وهو القيء (tahdhib)؛ ومن الباب الطلعاء القيء؛ يقال أطلع إذا قاء (maqayis)
- **B012** çevresindeki palmiye ağaçlarını boyca aşma; uzun boylu erkek — yanındaki palmiye ağaçlarından daha uzun olan palmiye · uzun boylu adam
  نخلة مطلعة إذا طالت النخيل (sihah)؛ نخلة مطلعة إذا طالت النخلة التي بحذائها فكانت أطول منها (tahdhib)؛ الهطلع الرجل الطويل زيدت فيه الهاء من طلع (maqayis)

## ظ ن ن (root_000969): 40:37 لَأَظُنُّهُۥ

- **B001** belirtiye dayanıp kesin bilgiye varan güçlü inanış — kesin olarak bilmek; emin olmak · bir belirtiden doğup güçlendikçe bilgiye, zayıfladıkça kuruntuya yaklaşan inanış
  ظننت ظنا أي أيقنت (maqayis)؛ قد يوضع موضع العلم؛ أي استيقنوا (sihah)؛ الظن يقين وشك؛ أي علمت (tahdhib)؛ متى قويت أدت إلى العلم (mufradat)
- **B002** bir şeyin bulunduğu düşünülen yer veya onu gösteren belirti — bir şeyin bulunduğu düşünülen yer, alışılmış alan veya onu gösteren belirti
  مظنة الشيء وهو معلمه ومكانه (maqayis)؛ مظنة الشيء موضعه ومألفه الذي يظن كونه فيه (sihah)؛ فلان مظنة من كذا ومئنة أي معلم (tahdhib)
- **B003** zayıf belirtiye dayalı kesinleşmemiş inanış — bir belirtiden doğup güçlendikçe bilgiye, zayıfladıkça kuruntuya yaklaşan inanış · kesin bilmeden öyle sanmak; kuşku duymak · sanıya dayanarak düşünme
  الشك؛ ظننت الشيء إذا لم تتيقنه (maqayis)؛ باليقين لا بالشك (sihah)؛ الظن يقين وشك (tahdhib)؛ متى ضعفت جدا لم يتجاوز حد التوهم (mufradat)
- **B004** birini suçlu sayma, suçlama ve suçlanan kişi — suçlama · hakkında suç kuşkusu bulunan kişi · onu suçladı · onu suçladı · o kişiyi suçladım
  الظنة التهمة؛ الظنين المتهم (maqayis)؛ الظنة التهمة؛ فلان ظنين أي متهم (jamhara)؛ الظنين الرجل المتهم؛ اطنه واظنه إذا اتهمه (sihah)؛ الظنين المتهم؛ ظننت بزيد أي اتهمت (tahdhib)؛ بظنين أي بمتهم (mufradat)
- **B005** başkaları hakkında kötü düşünme ve kötülük bekleme — herkese kuşkuyla bakan kimse · onun hakkında kötü düşündüm · kötülük yakıştıran düşünce
  الظنون السيئ الظن؛ سؤت به ظنا (maqayis)؛ الظنون الرجل السيئ الظن (sihah)؛ الظنون الرجل السيىء الظن بكل أحد (tahdhib)
- **B006** varlığı, doğruluğu veya sonucu belirsiz olduğu için güven vermeyen şey — su veya başka bir konuda güven vermeyen şey · suyu olup olmadığı bilinmeyen kuyu · ödenip ödenmeyeceği bilinmeyen alacak · sonucu bilinmeyen iş · o konudaki bilgisi güvenilir değil · iyiliği az kimse
  الظنون البئر لا يدرى أفيها ماء أم لا؛ الدين الظنون الذي لا يدرى أيقضى أم لا (maqayis)؛ الدين الظنون؛ الظنون البئر لا يدرى أفيها ماء أم لا (sihah)؛ الظنون كل ما لا يوثق به من ماء وغيره؛ علمه بالشيء ظنون إذا لم يوثق به؛ كل أمر تطالبه ولا تدري على أي شيء أنت منه فهو ظنون (tahdhib)
- **B007** düşmanlık eden kişi — düşmanlık eden kişi
  الظنين المعادي (tahdhib)
- **B008** bağlama göre güçsüz ya da yükleneni kaldırabilen kişi — bağlama göre güçsüz ya da yükleneni kaldırabilir · güçsüz veya çaresi az kimse
  ما هو بضعيف؛ هو محتمل له؛ الرجل الضعيف أو القليل الحيلة؛ ربما دلك على الرأي الظنون (tahdhib)
- **B009** evlenince kendisinden çocuk beklenen saygın kadın — evlenince kendisinden çocuk beklenen saygın kadın
  الظنون من النساء التي لها شرف تتزوج؛ سميت ظنونا لأن الولد يرتجى منها (tahdhib)

## ز ي ن (root_000660): 40:37 زُيِّنَ

- **B001** ayıptan uzak güzellik — güzellik; ayıp ve çirkinliğin karşıtı · güzel ve alımlı yüz · güzelliği onu güzel ve alımlı kıldı
  الزين نقيض الشين (maqayis;ayn;tahdhib)؛ زانه الحسن يزينه زينا (ayn;tahdhib)؛ الزينة الحقيقية ما لا يشين الإنسان (mufradat)
- **B002** güzelleştirme ve güzelliğini görünür kılma — bir şeyi güzelleştirmek ve güzelliğini ortaya çıkarmak · onun güzelliğini davranışla ya da sözle görünür kılmak · yer, otlarıyla güzelleşip canlandı · yer güzelleşip canlandı · yer güzelleşip canlandı · onu gönlünde güzel ve sevimli göstermek · yaptığı işi ona güzel göstermek · yeryüzündekileri ona güzel göstermek · dünya hayatını güzel göstermek · yakın göğü kandillerle bezemek
  أصل صحيح يدل على حسن الشيء وتحسينه (maqayis)؛ زينت الشيء تزيينا (maqayis)؛ ازدانت الأرض بعشبها وازينت وتزينت (ayn;tahdhib)؛ زانه وزينه إذا أظهر حسنه إما بالفعل أو بالقول (mufradat)؛ زينا السماء الدنيا بمصابيح وزينة الكواكب (mufradat)
- **B003** bezenmeye yarayan nitelik ve şeylerin bütünü — bezenmek için kullanılan her şeyin ortak adı · kişiyi hiçbir durumda ayıplı kılmayan gerçek güzellik · bilgi ve iyi inanç gibi içsel güzellik · güç ve uzun boy gibi bedensel güzellik · mal ve saygınlık gibi dışsal süs · mal, eşya ve saygınlık türünden dünyalık süs · Tanrı'nın sunduğu süs; başka yorumlarda cömertlik ya da kötülükten sakınma erdemi · yıldızların gözle algılanan süsü
  الزينة جامع لكل ما يتزين به (ayn)؛ الزينة اسم جامع لكل شيء يتزين به (tahdhib)؛ الزينة بالقول المجمل ثلاث: زينة نفسية وزينة بدنية وزينة خارجية (mufradat)؛ فهي الزينة الدنيوية من المال والأثاث والجاه (mufradat)

## ع م ل (root_001046): 40:37 عَمَلِهِۦ, 40:40 عَمِلَ, 40:40 عَمِلَ, 40:58 وَعَمِلُوا۟

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

## ص د د (root_000848): 40:37 وَصُدَّ

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

## ح ي و (root_005544): documented alternative for 40:39 ٱلْحَيَوٰةُ, 40:51 ٱلْحَيَوٰةِ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## د ن و (root_000493): 40:39 ٱلدُّنْيَا, 40:43 ٱلدُّنْيَا, 40:51 ٱلدُّنْيَا

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

## م ت ع (root_001395): 40:39 مَتَٰعٌ

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

## ء خ ر (root_000019): 40:39 ٱلْءَاخِرَةَ, 40:43 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## د و ر (root_000499): 40:39 دَارُ, 40:52 ٱلدَّارِ

- **B001** dönme ve çevreleme — dönmek veya çevresini dolanmak · dönme hareketi · bir tam dönüş · bir şeyi döndürmek · bir şeyi yuvarlaklaştırmak · dönme odağı veya dönülen yer · halka, çember veya yuvarlak çizgi · kuyu kovası biçiminde dikilmiş deri kap
  أصل واحد يدل على إحداق الشيء بالشيء من حواليه؛ دار يدور دورانا (maqayis)؛ دار دورة واحدة؛ المدار موضع للشيء الذي تدير به؛ الدائرة الحلقة والشيء المستدير (ayn)؛ دار الشيء يدور دورا ودورانا؛ تدوير الشيء جعله مدورا؛ الدائرة واحدة الدوائر (sihah)؛ الدار اعتبارا بدورانها؛ الدائرة عبارة عن الخط المحيط؛ دار يدور دورانا (mufradat)
- **B002** yerleşilen yer ve yurt — ev, konut veya insanların yerleştiği yer · kabile veya yerleşik topluluk · evler, konutlar veya yurtlar · çevresi yükseltilerle ya da sınırla kuşatılmış yer · ayın çevresindeki ışık halkası · bu yaşamın yurdu · öte yaşamın yurdu · esenlik yurdu · yıkım yurdu · yoldan çıkanların varacağı yurt
  الدار القبيلة؛ الدارة أرض سهلة تدور بها جبال؛ أصل الدار دارة (maqayis)؛ الدار كل موضع حل به قوم؛ الدار اسم جامع للعرصة والبناء والمحلة؛ الدارة دارة القمر وكل موضع يدار به شيء يحجزه (ayn)؛ الدار مؤنثة؛ الكثير ديار ودور؛ الدارة أخص من الدار؛ الدارة التي حول القمر وهي الهالة (sihah)؛ الدار المنزل اعتبارا بدورانها الذي لها بالحائط؛ تسمى البلدة دارا والصقع دارا والدنيا دارا والدار الآخرة (mufradat)
- **B003** durumların dönüp değişmesi — insanın durumlarını değiştirip duran zaman · işleri evirip çevirerek ele alma
  الدواري الدهر لأنه يدور بالناس أحوالا (maqayis)؛ الدواري الدهر الدوار بالناس؛ الدائرة الدولة؛ مداورة الشؤون معالجتها (ayn)؛ المداورة كالمعالجة؛ الدواري الدهر يدور بالإنسان أحوالا (sihah)؛ الدواري الدهر الدائر بالإنسان من حيث إنه يدور بالإنسان (mufradat)
- **B004** kuşatan kötü durum veya yenilgi — kuşatıcı kötü durum veya yenilgi · dönüp sahibini bulacak kötülük
  دارت بهم الدوائر أي الحالات المكروهة أحدقت بهم (maqayis)؛ الدائرة الهزيمة؛ عليهم دائرة السوء (sihah)؛ الدورة والدائرة في المكروه (mufradat)
- **B005** baş dönmesi ve baygınlık — baş dönmesi · başı döndü veya bayıldı
  الدوار في الرأس هو من الباب؛ يقال دير به وأدير به (maqayis)؛ الدوار أن يأخذ الإنسان في رأسه كهيئة الدوران تقول دير به أي غشي عليه (ayn)؛ الدوار أيضا من دوار الرأس؛ يقال دير بالرجل وأدير به (sihah)
- **B006** çevresinde dönülen tapınma nesnesi veya yeri — çevresinde dönülen taş, dikili tapınma nesnesi veya yer
  الدوار مثقل ومخفف حجر كان يؤخذ من الحرم إلى ناحية ويطاف به (maqayis)؛ الدوار صنم كانت العرب تنصبه يجعلون موضعا حوله يدورون فيه واسم ذلك الصنم والموضع الدوار (ayn)؛ دوار بالضم صنم وقد يفتح (sihah)
- **B007** yere bağlı kişi — yer bağlantısıyla adlandırılan koku ve baharat satıcısı · evinde oturan yerleşik kişi veya sürü sahibi
  الداري العطار؛ وإنما سمي داريا من الدار أي هو يسكن الدار؛ الداري الرجل المقيم في داره (maqayis)؛ الداري العطار وهو منسوب إلى دارين؛ والداري أيضا رب النعم سمي بذلك لأنه مقيم في داره (sihah)
- **B008** manastır ve ona bağlı kullanımlar — Hristiyan manastırı veya kilisesi · manastır sahibi, görevlisi veya sakini · orada hiç kimse yok · topluluğun başındaki kişi
  الدال والياء والراء أظنه منقلبا عن الواو من الدار والدور؛ ومن الباب الدير؛ وما بها ديور وديار أي أحد؛ رأس الدير (maqayis_dyr)؛ الدير البيعة وساكنه وعامله ديراني وديار؛ الديور الواحد الفرد من الناس (ayn)؛ دير النصارى أصله الواو والجمع أديار؛ الديراني صاحب الدير؛ هو رأس الدير (sihah)

## ق ر ر (root_001215): 40:39 ٱلْقَرَارِ, 40:64 قَرَارًا

- **B001** soğukluk, üşüme ve yıkanmalık soğuk su — soğukluk, üşüme · soğuk gün, soğuk gece veya soğuk sabah · soğukluk; ateş nöbetinin soğuk evresi · yıkanmada kullanılan soğuk su
  القر وهو البرد (maqayis)؛ القر وهو البرد يوم قر وليلة قرة وغداة قرة (jamhara)؛ القر بالضم البرد ويوم قر وليلة قرة والقرة بالكسر البرد (sihah)؛ القر البرد ورجل مقرور وليلة قرة ويوم قر وطعام قار (tahdhib)؛ يوم قر وليلة قرة وقر فلان فهو مقرور (mufradat)؛ القرور الماء البارد يغتسل به (maqayis;tahdhib)
- **B002** gözü aydın olup huzur bulmak [kalıp] — gözü aydın oldu, sevindi ve huzur buldu · ona göz aydınlığı ve huzur versin · göz aydınlığı, sevinç kaynağı
  أقر الله عينه (maqayis)؛ قرت عينه تقر وتقر ورجل قرير العين (sihah)؛ قرت عينه والقرة كل شيء قرت به عينك (tahdhib)؛ قرت عينه تقر سرت وقرة عين (mufradat)
- **B003** yerleşmek ve sabit kılmak — bulunduğu yere yerleşip kaldı · yerleşti, sabit hâle geldi · sabit yer veya yerleşik durum · onu kendi yerine koyup sabitledi
  الأصل الآخر التمكن يقال قر واستقر (maqayis)؛ القرار في المكان الاستقرار فيه (sihah)؛ القرار المستقر من الأرض وأقررت الشيء في مقره ليقر (tahdhib)؛ قر في مكانه يقر قرارا إذا ثبت ثبوتا جامدا (mufradat)
- **B004** binek üstü taşıma düzeneği — binek üstü taşıma düzeneği, kimi açıklamada tahtırevan
  القَرّ مركب من مراكب النساء (maqayis)؛ القَرّ مركب للرجال بين الرحل والسرج وقال غيره القَرّ الهودج (sihah)؛ القَرّ أيضا مركب النساء (tahdhib)
- **B005** tek seferde dökmek veya kulağa aktarmak — suyu bir şeyin içine veya başına tek seferde dökmek · yanmasın diye kaba soğuk su dökmek · sözü kulağına doğrudan aktarıp anlatmak
  القر صب الماء في الشيء والقر صب الكلام في الأذن (maqayis)؛ قررت على رأسه دلوا من ماء بارد وقر الحديث في أذنه (sihah)؛ القر صب الماء دفقة واحدة وقررت الكلام في أذنه (tahdhib)؛ قررت القدر أقرها صببت فيها ماء قارا (mufradat)
- **B006** düz taban, çukur taban ve dip tortusu — düz ve pürüzsüz çıplak zemin · alçak veya yuvarlak tabanlı yer; kap dibi kalıntısı · kabın dibine yapışan tortu
  القرقر القاع الأملس والقرارة ما يلتزق بأسفل القدر (maqayis)؛ القرار المستقر من الأرض والقرارة القاع المستدير والقرقر القاع الأملس (sihah)؛ القرار مستقر الماء في الروضة والقرارة الأرض المطمئنة والقرقر المستوي الأملس (tahdhib)
- **B007** kabul edip doğrulamak ve sabitlemek — kabul etme, doğrulama ve itiraf · hakkı kabul edip kendi üzerinde tanımak · kabul ettirme; açıklayıp sabitleme
  الإقرار ضد الجحود (maqayis)؛ أقر بالحق اعترف به وقرره بالحق غيره حتى أقر (sihah)؛ الإقرار الاعتراف بالشيء ويقال أقررت الكلام لفلان أي بينته له (tahdhib)؛ الإقرار إثبات الشيء وأقر بالحق اعترف به وأثبته على نفسه (mufradat)
- **B008** kesim gününün ertesi konaklama günü [kalıp] — kesim gününün ertesi, yolcuların konak yerlerinde kaldığı gün
  يوم القر يوم يستقر الناس بمنى وذلك غداه يوم النحر (maqayis)؛ يوم القر اليوم الذي بعد يوم النحر لأن الناس يقرون في منازلهم (sihah)؛ يوم القر الغد من يوم النحر قروا بمنى (tahdhib)؛ يوم القر بعد يوم النحر لاستقرار الناس فيه بمنى (mufradat)
- **B009** sabah ve akşam — sabah ve akşam; sabah akşam
  القرتان الغداة والعشي (sihah)؛ يأتيه بالغداة والعشي (tahdhib)
- **B010** küçük, kısa bacaklı koyun tipi — küçük, kısa bacaklı bir koyun tipi
  القرار والقرارة النقد وهو ضرب من الغنم قصار الأرجل قباح الوجوه (sihah)؛ القرار النقد من الشاء وهي صغار وأجود الصوف صوف النقد (tahdhib)
- **B011** yinelenen tok veya gür ses çıkarma — güvercin dem çekti, tekrarlı biçimde öttü · karnı guruldadı · deve veya damızlık erkek hayvan gür ve yankılı ses çıkardı · gür veya temiz sesli
  قرقرت الحمامة قرقرة (maqayis)؛ قرقر بطنه أي صوت وقرقر البعير إذا صفا صوته ورجع (sihah)؛ القرقرة قرقرة البطن وقرقرة الفحل وقرقرة الحمام وحكاية صوت الريح قرقارا (tahdhib)
- **B012** cam şişe; benzetmeyle narin kadın — cam şişe veya cam kap · cam kaplara benzetilen narin kadınlar
  القارورة واحدة القوارير من الزجاج (sihah)؛ القوارير النساء شبههن بالقوارير (tahdhib)؛ القارورة معروفة وجمعها قوارير أي من زجاج (mufradat)
- **B013** rahimde tutunma veya doyup semirme — devenin gebeliği tutundu · deve semirdi veya hayvan doydu · erkekten gelen üreme sıvısı rahimde yerleşti
  أقرت الناقة إذا ثبت حملها واقتر ماء الفحل في الرحم أي استقر واقترت الناقة سمنت (sihah)؛ الاقترار ماء الفحل في الرحم وقد اقترت وقد اقتر المال إذا شبع والاقترار الشبع (tahdhib)
- **B014** yerleşik zanaatkâr, özellikle terzi — terzi, zanaatkâr veya göçmeyen yerleşik kentli
  القراري الخياط (sihah)؛ القراري الحضري الذي لا ينتجع الكلأ ويقال إن كل صانع عند العرب قراري وللخياط القراري (tahdhib)
- **B015** kuş kursağı — kuşun kursağı
  القِرّية الحوصلة مثل الجرية (sihah)؛ القِرّية الحوصلة يقال ألقه في قريتك (tahdhib)

## ء ن ث (root_000058): 40:40 أُنثَىٰ

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

## ن ج و (root_001476): 40:41 ٱلنَّجَوٰةِ

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

## ل ي س (root_001390): 40:42 لَيْسَ, 40:43 لَيْسَ

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

## ج ر م (root_000239): 40:43 جَرَمَ

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

## ECHO م ر د (root_001413): for 40:43 مَرَدَّنَآ: withheld observed target; not identity

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

## ف و ض (root_001187): 40:44 وَأُفَوِّضُ

- **B001** bir işi başkasına bırakıp ona güvenme — işi ona bırakıp ona güvenmek · işimi Tanrı'ya bırakıp ona güveniyorum
  أصل صحيح يدل على اتكال في الأمر على آخر ورده عليه (maqayis)؛ فوض إليه أمره إذا رده (maqayis)؛ فوضت إليه الأمر أي جعلته إليه (ayn)؛ وأفوض أمري إلى الله أي أتكل عليه (ayn)؛ فوض إليه الأمر أي رده إليه (sihah)؛ أرده إليه (mufradat)
- **B002** dağınık, karışık veya başsız topluluk durumu — dağınık, karışık veya başsız topluluk durumu · malları aralarında ortak olmak · karışık veya ortak durumda olma
  باتوا فوضى أي مختلطين (maqayis)؛ مالهم فوضى بينهم إذا لم يخالف أحدهم الآخر (maqayis)؛ صار الناس فوضى أي متفرقين (ayn)؛ الوحش فوضى أي متفرقة مترددة (ayn)؛ قوم فوضى أي متساوون لا رئيس لهم (sihah)؛ نعام فوضى مختلط بعضه ببعض (sihah)؛ أموالهم فوضى بينهم أي هم شركاء فيها (sihah)؛ مالهم فوضى بينهم (mufradat)
- **B003** bütün malı veya alanı kapsayan ortaklık [kalıp] — iki ortağın malın tamamında ortak olması ve işini ötekine bırakması · her şeyi kapsayan ortaklık · o konuda ortak olmaları
  تفاوض الشريكان في المال إذا اشتركا ففوض كل أمره إلى صاحبه (maqayis)؛ شركة المفاوضة الاشتراك في كل شيء (ayn)؛ بينهم فوض إذا كانوا فيه شركاء (ayn)؛ تفاوض الشريكان في المال إذا اشتركا فيه أجمع (sihah)؛ شركة المفاوضة (sihah;mufradat)
- **B004** evlilik bedeli belirlenmeden evlendirme [kalıp] — evlilik bedeli belirlenmeden evlendirme
  التفويض في النكاح التزويج بلا مهر (sihah)
- **B005** bir işi karşılıklı ele alma — işinde ona ayak uydurmak · konuyu aralarında görüşmek
  فاوضه في أمره أي جاراه (sihah)؛ تفاوض القوم في الأمر أي فاوض فيه بعضهم بعضا (sihah)

## م ك ر (root_001438): 40:45 مَكَرُوا۟

- **B001** gizli hileyle amacından saptırma — gizli hile ve aldatmayla amacından saptırma · birine hile yapmak ve onu aldatmak · hileye karşılık ceza verme · savaşta taktik düzen ve hile
  المكر: الاحتيال والخداع (maqayis;sihah)؛ المكر احتيال في خفية (ayn;tahdhib)؛ صرف الغير عما يقصده بحيلة (mufradat)؛ المكرة: التدبير والحيلة في الحرب (tahdhib)؛ المكر من الله: جزاء (tahdhib)
- **B002** dolgun ve biçimli baldır — baldırın dolgun ve güzel biçimli oluşu · dolgun ve biçimli baldırlı kadın · sıkı ve toplu yapılı kadın · kalınca ve güzel biçimli baldır
  المكر: خدالة الساق؛ امرأة ممكورة الساقين (maqayis)؛ المكر حسن خدالة الساق؛ مرتوية الساق خدلة (ayn;tahdhib)؛ الممكورة: المطوية الخلق من النساء؛ خدلاء (sihah)؛ المكرة: الساق الغليظة الحسناء (tahdhib)
- **B003** belirli bir bitki veya ağaç türü — belirli bir bitki türü · bu bitkinin tek bir örneği · bir ağaç türü veya ağaç türleri · bu bitkinin meyvesi
  المكر ضرب من النبات الواحدة مكرة وسميت لارتوائها (ayn;tahdhib)؛ المكور ضرب من الشجر وضروب من الشجر (ayn;sihah;tahdhib)؛ الواحد مكر وفراخ المكر ثمره (sihah)
- **B004** boyamada kullanılan aşı boyası — boyamada kullanılan aşı boyası · aşı boyasıyla boyamak ve boyanmak · sakalların aşı boyasıyla boyanması
  المكر: المغرة (ayn;sihah)؛ مكره فامتكر أي خضبه فاختضب (sihah)؛ تمتكر اللحى أي تختضب؛ طلي بالمغرة (tahdhib)
- **B005** toprağı veya ürünü sulama — toprağı sulama · sert toprağı sulayıp sonra sürmek · ürüne verilen bir sulama · sulanmış ürün
  المكر: سقي الأرض؛ امكروا الأرض فإنها صلبة ثم احرثوها؛ المكرة: السقية للزرع؛ زرع ممكور أي مسقي (tahdhib)
- **B006** bozulmuş yaş hurma — bozulmuş yaş hurma
  المكرة: الرطبة الفاسدة (tahdhib)

## ح ي ق (root_000381): 40:45 وَحَاقَ, 40:83 وَحَاقَ

- **B001** kötülüğün başa gelip kuşatması — kötü bir şey onun başına gelip onu kuşattı · kişinin yaptığı kötülüğün dönüp başına gelmesi · kötülüğün onların başına gelip onları kuşatması · Tanrı kötülüğü onun başına getirip onu kuşattı · kötülük onların başına gelip onları kuşattı · ağır sonuç onları kuşatıp başlarına geldi veya kaçınılmaz oldu · kötü düzen dönüp sahibini buldu
  نزول الشيء بالشيء؛ حاق به السوء (maqayis)؛ الحيق ما حاق بالإنسان من منكر أو سوء يعمله فينزل به ذلك؛ أحاق الله به (ayn)؛ حاق بهم الشر يحيق حيقا وحيقانا وحيوقا (jamhara)؛ حاق به الشيء يحيق أي أحاط به؛ حاق بهم العذاب أي أحاط بهم ونزل (sihah)؛ حاق بهم العذاب كأنه وجب عليهم؛ الحيق ما حاق بالإنسان من مكر أو سوء يعمله فينزل ذلك به؛ أحاط بهم العذاب ونزل بهم (tahdhib)؛ لا ينزل ولا يصيب (mufradat)

## ع ر ض (root_001001): 40:46 يُعْرَضُونَ

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

## غ د و (root_001076): 40:46 غُدُوًّا

- **B001** günün ilk vakti ve bu vakitte yola çıkma — günün erken vaktinde gitmek · günün ilk vakti ve bu vakitteki gidiş · erken ibadet ile güneşin doğuşu arasındaki vakit · günün erken vakti · günün erken vaktinde yola çıkma · birinin yanına günün erken vaktinde gitmek · ertesi günün erken vakti · sabahları ve akşamları gidip gelmek
  أصل صحيح يدل على زمان؛ الغدو يقال غدا يغدو (maqayis)؛ غدا غدوا واغتدى اغتداء (ayn)؛ الغدوة ما بين صلاة الغداة وطلوع الشمس؛ الغدو نقيض الرواح؛ غاداه أي غدا عليه (sihah)؛ غدوت أغدو غدوا؛ الغدو جمع مثل الغدوات (tahdhib)؛ الغدوة والغداة من أول النهار؛ قد غدوت أغدو (mufradat)
- **B002** yarın — ertesi günün erken vakti · yarın · yarın
  أفعل ذلك غدا؛ والأصل غدوا (maqayis)؛ الغد أصله غدو (sihah)؛ قدمت لغد بغير واو فإذا صرفوها قالوا غدوت أغدو (tahdhib)؛ غد يقال لليوم الذي يلي يومك الذي أنت فيه (mufradat)
- **B003** günün erken vaktinde beliren bulut — günün erken vaktinde beliren bulut · günün erken vaktinde beliren bulutlar
  الغادية سحابة تنشأ صباحا (maqayis)؛ الغادية سحابة تنشأ صباحا وجمعها غوادي (ayn)؛ الغادية سحابة تنشأ صباحا (sihah)؛ الغادية سحابة تنشأ صباحا وجمعها الغوادي (tahdhib)؛ الغادية السحاب ينشأ غدوة (mufradat)
- **B004** günün başında yenen yemek — günün başında yenen yemek · günün ilk öğününü yemek · günün ilk öğününü yiyen kişi · günün ilk öğününü yiyen kişi
  الغداء الطعام بعينه سمي بذلك لأنه يؤكل في ذلك الزمان (maqayis)؛ الغداء ما يؤكل من أول النهار (ayn)؛ الغداء الطعام بعينه وهو خلاف العشاء؛ تغدى؛ الغديان المتغدي (sihah)؛ الغداء ما يؤكل أول النهار وقد تغدى الرجل فهو متغد (tahdhib)؛ الغداء طعام يتناول في ذلك الوقت (mufradat)
- **B005** gebe hayvanın karnındaki yavru — gebe hayvanın karnındaki yavru; ayrıca beklenen yavruya dayalı belirsiz satış
  الغدوي كل ما كان في بطون الحوامل وربما جعل في الشاء خاصة (ayn)؛ الغدوي بالدال أن يبيع الشيء بنتاج ما نزى به الكبش ذلك العام؛ كل ما في بطون الحوامل غدوي من الإبل والشاء؛ نهي عن الغدوي وهو كل ما في بطون الحوامل؛ الغدوي الحمل والجدي لا يغذى بلبن أمه (tahdhib)

## ع ش و (root_001017): 40:46 وَعَشِيًّا, 40:55 بِٱلْعَشِىِّ

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

## ح ج ج (root_000295): 40:47 يَتَحَآجُّونَ (also echo for 40:80 حَاجَةً)

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

## ض ع ف (root_000909): 40:47 ٱلضُّعَفَٰٓؤُا۟

- **B001** güçsüzlük — zayıflık, güçsüzlük · zayıflamak, güçten düşmek · zayıf veya güçsüz kimse · zayıflar, zayıf kimseler · zayıf kadınlar · zayıflatmak, güçsüz kılmak · zayıf bulmak veya saymak ve ezmek · zayıflıkla niteleme · yürüyüş onu zayıflattı · hafif yağmur almış arazi · aklı zayıf adam · gözü görmeyen kimse
  الضعف خلاف القوة (maqayis;ayn;sihah;mufradat)؛ الضعف في العقل والرأي والضعف في الجسد (ayn;tahdhib;mufradat)؛ الضعف قد يكون في النفس وفي البدن وفي الحال (mufradat)؛ أضعفته أي صيرته ضعيفا واستضعفته وجدته ضعيفا (ayn;sihah;tahdhib;mufradat)؛ أرض مضعفة أصابها مطر ضعيف (tahdhib)
- **B002** bir şeyi iki veya daha çok katına çıkarma — bir şeyi iki veya daha çok katına çıkarmak · bir katı veya ona eklenen eş miktar · iki katı · katları veya çoğaltılmış miktarları · iki kez veya iki katlık miktar · katlanmış veya bir eşi eklenmiş şey · bir topluluğa karşı sayıca iki kat olmak · topluluğa iki kat verilmek · halkaları ikişer örülmüş zırh · katlı veya katlanmış kumaşlar
  أضعفت الشيء وضعفته وضاعفته وهو أن يزاد على أصل الشيء فيجعل مثلين أو أكثر (maqayis;ayn;sihah;tahdhib;mufradat)؛ ضعف الشيء مثله وضعفاه مثلاه وأضعافه أمثاله (sihah;tahdhib;mufradat)؛ الضعف في الأصل زيادة غير محصورة (tahdhib)؛ المضاعفة الدرع نسجت حلقتين حلقتين والثياب المضعفة (maqayis;sihah;tahdhib)
- **B003** satır araları, kenar ve bedenin iç bölümleri — kitabın satır araları veya kenarı · bedenin kemikleri veya organları · bedenin iç boşluğu veya iç kısmı
  وقع في أضعاف كتابه أي في أثناء السطور أو الحاشية (sihah)؛ أضعاف الجسد عظامه وأعضاؤه والأضعاف الجوف (tahdhib)
- **B004** bineği zayıf adam [kalıp] — bineği zayıf adam
  أضعف الرجل ضعفت دابته (sihah)؛ الضعيف في بدنه والمضعف الذي دابته ضعيفة (tahdhib)
- **B005** mülkleri çok ve dağınık adam [kalıp] — mülkleri çok ve dağınık adam
  يقال للرجل إذا انتشرت ضيعته وكثرت أضعف الرجل فهو مضعف (tahdhib)

## غ ن ي (root_001110): 40:47 مُّغْنُونَ, 40:82 أَغْنَىٰ

- **B001** maddi bolluk ve ihtiyaçtan bağımsızlık — maddi zenginlik, bolluk ve ihtiyaçsızlık · varlıklı, zengin · zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek · ona ihtiyaç duymamak · onunla yetinip başka bir şeye ihtiyaç duymamak · bir şeye ihtiyaç duymama durumu · zenginlik ve bolluk · gönül tokluğu ve az şeye ihtiyaç duyma · zengin etmek veya yoksunluğunu gidermek · Kur'an'la yetinip başka bir şeye ihtiyaç duymamak
  الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)
- **B002** ihtiyacı karşılayıp yarar sağlama ve yerini tutma — yeterlilik, ihtiyacı karşılama ve yarar · onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak · bu sana yetmez ve yarar sağlamaz · yeterli ve ihtiyacı karşılayan · birinin yerini tutan yeterlilik ve işlev · zararını benden uzak tut
  الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)
- **B003** sesle ezgi söyleme, dinleme ve ezgili okuma — şarkı söyleme, ezgili seslendirme ve dinleti · şarkı; ezgili söylenen parça · şarkı söylemek · şarkı söylemek veya sesi ezgili ve duygulu kullanmak · Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak
  الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)
- **B004** bir yerde uzun süre kalıp yaşama — bir yerde oturmak ve uzun süre kalmak · sanki daha dün orada hiç yaşamamıştı · bir topluluğun oturduğu evler ve yurtlar · oturma eylemi veya oturulan yer
  غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)
- **B005** süsten bağımsız sayılan; bazen genç, güzel veya evli kadın — eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın · bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar
  الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)
- **B006** evlenme ve evlendirme — evlenme; bekâr kişi için koruyucu sayılan evlilik · gelinleri evlendirme
  الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)

## خ ز ن (root_000406): 40:49 لِخَزَنَةِ

- **B001** saklayarak koruma — bir şeyi saklayarak koruma · bir şeyi güvenli bir yere koyup saklamak · bir şeyi saklamak veya kendine ayırmak · sırrı gizli tutmak · onu şükürle koruyup sürdürebilecek değilsiniz
  خزن الشيء إذا أحرزه في خزانة واختزنته لنفسي (ayn)؛ خزنت المال واختزنته جعلته في الخزانة وخزنت السر واختزنته كتمته (sihah)؛ خزن الشيء إذا أحرزه في خزانة واختزنه لنفسه وخزن المال إذا غيبه (tahdhib)؛ الخزن حفظ الشيء في الخزانة ثم يعبر به عن كل حفظ كحفظ السر ونحوه وما أنتم له بخازنين قيل حافظين له بالشكر (mufradat)؛ أصل يدل على صيانة الشيء وخزنت الدرهم وغيره وخزنت السر (maqayis)
- **B002** saklama yeri ve mecazi kaynak — saklama yeri · depo · saklama yerleri; mecazen kaynaklar · Tanrı'nın gizli bilgisi, yapabilecekleri, sınırsız iyiliği ve kudreti · göklerde ve yerde var edilebilecek her şeyin Tanrı'nın kudretinde bulunması · kalp, insanın sakladıklarının deposudur · Kur'an'ın her bölümü, içindeki anlamı saklayan bir kap gibidir · bir kentin, bir topluluğun bilgi ve dil bakımından başlıca dayanağı olması
  الخزانة الموضع الذي يخزن فيه الشيء وخزانتي قلبي والبصرة خزانة العرب (ayn)؛ المخزن ما يخزن فيه الشيء والخزانة واحدة الخزائن (sihah)؛ الخزانة اسم المكان الذي يخزن فيه الشيء وخزائن الله غيوب علم الله وآيات القرآن خزائن وشبه الآية بالوعاء الذي يجمع فيه المال المخزون فيه (tahdhib)؛ خزائنه ولله خزائن السماوات والأرض إشارة إلى قدرته أو إلى الحالة وخزائن الله مقدوراته وجوده الواسع وقدرته وقوله كن (mufradat)
- **B003** saklananı koruyan görevli ve koruma görevi — saklananı koruyan görevli · koruma görevlileri · koruma görevi · dilim, içimde tuttuklarımın koruyucusudur
  خازني لساني وإذا كان خازنك حفيظا والخزانة عمل الخازن (ayn)؛ خازنك حفيظا يعني اللسان والخزانة عمل الخازن (tahdhib)؛ الخزنة جمع الخازن وقال لهم خزنتها في صفة النار وصفة الجنة (mufradat)
- **B004** etin kokup bozulması [kalıp] — et kokup bozuldu
  خزن اللحم أي تغير (ayn)؛ خزن اللحم أنتن مثل خنز مقلوب منه (sihah)؛ خزن اللحم وخنز كله بمعنى واحد إذا تغير (tahdhib)؛ الخزن في اللحم أصله الادخار فكني به عن نتنه وخزن اللحم إذا أنتن وخنز بتقدم النون (mufradat)؛ خزن اللحم تغيرت رائحته فليس من هذا إنما هذا من المقلوب والأصل خنز (maqayis)؛ خنز اللحم إذا تغيرت رائحته وخزن وقد مضى (maqayis)
- **B005** en kısa yolu seçme [kalıp] — kestirme yolu seçmek · yolun en yakın ve kısa bölümleri
  اختزنت طريقا واختصرته وأخذنا مخازن الطريق ومخاصرها أي أخذنا أقربها (tahdhib)
- **B006** yoksulluktan sonra varlıklı olma — yoksulluktan sonra varlıklı olmak
  أخزن الرجل إذا استغنى بعد فقر (tahdhib)

## خ ف ف (root_000427): 40:49 يُخَفِّفْ

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

## ش ه د (root_000822): 40:51 ٱلْأَشْهَٰدُ

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

## ن ف ع (root_001536): 40:52 يَنفَعُ, 40:80 مَنَٰفِعُ, 40:85 يَنفَعُهُمْ

- **B001** zararın karşıtı olan ve iyiliğe ulaştıran yarar — zararın karşıtı olan, iyiliğe ulaşmaya yardım eden yarar · ona yarar sağladı · ondan yararlandı · yarar · yarar · yararlı · insanlara sürekli yarar sağlayan ve zarar vermeyen kişi
  النون والفاء والعين كلمة تدل على خلاف الضر (maqayis)؛ النفع ضد الضر (ayn;sihah;tahdhib)؛ نفعه نفعا وانتفعت بكذا (ayn)؛ نفعه ينفعه نفعا ومنفعة وانتفع بكذا (maqayis)؛ ما يستعان به في الوصول إلى الخيرات (mufradat)؛ ما عندهم نفيعة أي منفعة (tahdhib)؛ رجل نفاع إذا كان ينفع الناس ولا يضرهم (tahdhib)
- **B002** deri su kabının iki yanındaki yarılmış deri parçalardan biri — deri yarılarak su kabının iki yanına yerleştirilen parçalardan biri
  النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة (ayn)؛ النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة (tahdhib)
- **B003** değnek — değnek · değnek alıp satmak
  النَّفعة العصا وهي فعلة من النفع؛ أنفع الرجل إذا اتجر في النفعات وهي العصي

## ع ذ ر (root_000995): 40:52 مَعْذِرَتُهُمْ

- **B001** kınamayı kaldıran gerekçe ve bunun kabulü — kınamayı ya da suç yükünü kaldıran gerekçe · bağışlanma isteme veya bağışlatan gerekçe · kendisi için gerekçe ileri sürmek · gerekçesini kabul edip kınamamak
  العذر معروف (maqayis); عذرته عذرا ومعذرة (ayn); الاعتذار من الذنب (sihah); معذرة إلى ربكم (tahdhib); العذر تحري الإنسان ما يمحو به ذنوبه (mufradat)
- **B002** kötülük yapanı kınayıp karşılık vereni haklı sayma [kalıp] — onu değil, kötülük yapan kişiyi kınadım · o kişiye karşılık verirsem beni kim haklı sayar
  عذرته من فلان أي لمته ولم ألم هذا (maqayis;ayn); عذيرك من فلان (sihah); من يعذرني من فلان (tahdhib)
- **B003** kişinin gerçekleştirmeye çalıştığı durum — kişinin gerçekleştirmeye çalıştığı iş veya durum
  عذير الرجل ما يروم ويحاول (maqayis); العذير الحال التي يحاولها المرء (sihah); العذير أيضا الحال وجمعه عذر (tahdhib)
- **B004** kınanmayacak ölçüde elinden geleni yapmak veya uyarmak — kınanmayacak ölçüde elinden geleni yapmak veya önceden uyarmak
  أعذر فلان إذا أبلى عذرا فلم يلم (maqayis); أعذر في الأمر أي بالغ فيه (sihah); قد أعذر من أنذر (tahdhib); أعذر أتى بما صار به معذورا (mufradat)
- **B005** işi eksik bırakıp geçersiz gerekçe göstermek — işi eksik bırakıp gerekçe göstermek · geçerli gerekçesi olmadığı halde varmış gibi davranan kişi
  عذر الرجل تعذيرا إذا لم يبالغ (maqayis); التعذير في الأمر التقصير فيه (sihah); التعذير وهو التقصير (tahdhib); المعذر من يرى أن له عذرا ولا عذر له (mufradat)
- **B006** işin yoluna girmemesi veya güçleşmesi — iş yoluna girmedi, güçleşti veya yapılamaz hale geldi
  تعذر الأمر إذا لم يستقم (maqayis); تعذر عليه الأمر أي تعسر (sihah); تعذر علي هذا الأمر إذا لم يستقم (tahdhib)
- **B007** maddi veya duygusal izin silinmesi — izin silinmesi, aşınması veya kesintiye uğraması
  الاعتذار أيضا الدروس (sihah); اعتذرت المنازل إذا درست (tahdhib); الاعتذار محو أثر الموجدة (tahdhib)
- **B008** yanak boyunca uzanan dizgin parçası veya benzer yan çizgi — dizgin takımının yanak boyunca uzanan parçası · dizgini atıp taşkınlığa dalmak · ata dizgin takmak veya yanağındaki bağı sıkmak
  العذار عذار اللجام (maqayis); ما كان على الخدين من كي أو كدح طولا فهو عذار (maqayis); العذار للدابة (sihah); العذار سمة في موضع العذار (sihah); عذارا الحائط والوادي جانباه (tahdhib); عذار من الشجر أي سكة مصطفة (tahdhib)
- **B009** sevinçli bir olay için verilen çağrılı yemek — çocuk işlemi veya sevinçli olay için verilen yemek · çocuğun geleneksel kesme işlemi için verilen yemek
  العذار وهو طعام يدعى إليه لحادث سرور (maqayis); هو طعام الختان خاصة (maqayis); الإعذار طعام الختان (sihah;tahdhib); العذار طعام البناء (tahdhib)
- **B010** çocukta geleneksel kesme işlemi ve kesilen bölüm — erkek çocuğuna geleneksel kesme işlemi yapmak · erkek çocukta kesilen deri kıvrımı veya kesim yeri
  عذر الغلام إذا ختن (maqayis); عذر الغلام ختنه (sihah); عذرت الغلام والجارية أي ختنتهما (sihah); قلفة الصبي أيضا عذرة (tahdhib); عذرت الصبي إذا طهرته وأزلت عذرته (mufradat)
- **B011** cinsel ilişkiye girmemiş olma ve el değmemişlik — cinsel dokunulmamışlık veya kızlık zarı · cinsel ilişkiye girmemiş kişi veya el değmemiş şey
  العذرة عذرة الجارية العذراء (maqayis); العذرة البكارة والعذراء البكر (sihah); خاتم البكر (tahdhib); العذراء الرملة التي لم توطأ (tahdhib); جلدة البكارة عذرة (mufradat)
- **B012** geniş içli ve sert ısıran; geniş egemenlikli veya kötü huylu — geniş içli ve sert ısıran, geniş egemenlikli ya da kötü huylu
  العذور الواسع الجوف الشديد العضاض (maqayis); ملكا عذورا (maqayis); العذور السيئ الخلق (sihah); حمار عذور وهو الواسع الجوف وملك عذور واسع عريض (tahdhib)
- **B013** çocukta da görülen boğaz rahatsızlığı — boğazda veya küçük dil çevresinde ağrılı rahatsızlık · bu boğaz rahatsızlığına tutulmuş kişi
  العذرة وجع يأخذ في الحلق (maqayis); وجع الحلق من الدم (sihah); العذرة وجع في الحلق (tahdhib); العارض في حلق الصبي عذرة (mufradat)
- **B014** doğuşunda sıcaklığın arttığı yıldız veya yıldız kümesi — doğuşuyla sıcaklığın arttığı yıldız veya beşli yıldız kümesi
  العذرة نجم إذا طلع اشتد الحر (maqayis); العذرة كواكب في آخر المجرة خمسة (sihah); العذرة نجم إذا طلع اشتد غم الحر (tahdhib)
- **B015** saç veya at yelesinden bir tutam — saç tutamı, ön saç veya at yelesinden bir tutam
  العذرة خصلة من شعر والخصلة من عرف الفرس (maqayis); العذرة الخصلة من الشعر (sihah); العذرة الناصية وجمعها عذر (tahdhib)
- **B016** evin önü veya avlusu; buraya bırakılan dışkı — evin önü veya avlusu; dolaylı olarak dışkı
  العذرة فناء الدار (maqayis); سميت بذلك لأن العذرة كانت تلقى في الأفنية (sihah); العذرة أصلها فناء الدار (tahdhib)
- **B017** kalan iz veya ayırt edici çizgi damgası — yara veya başka bir etkiden kalan iz · hayvanı ayırt eden çizgi biçimli damga
  العاذر أثر الجرح (sihah); العاذور سمة كالخط (sihah); العواذير جمع عاذور (tahdhib); أعذر عني فيخط في الميسم خطا (tahdhib)
- **B018** kötü eylemleri ve eksik yanları çoğalıp bozulmak — kötü eylemleri ve eksik yanları çoğalmak, bozulmak
  عذرى أي كثرت عيوبه وذنوبه وكذلك أعذر (sihah); حتى تكثر ذنوبهم وعيوبهم (tahdhib); أعذر الرجل إعذارا إذا صار ذا عيب وفساد (tahdhib)
- **B019** bölgesel kullanımda perdeler veya örtüler — bölgesel kullanımda perdeler veya örtüler
  المعاذير الستور بلغة أهل اليمن واحدها معذار (tahdhib)
- **B020** elleri boyna bağlayan pranga benzeri bağlar — elleri boyna bağlayan pranga benzeri bağlar
  العذارى هي الجوامع كالأغلال تجمع بها الأيدي إلى الأعناق (tahdhib)
- **B021** işte başarıya ulaşma veya savaşta üstün gelme — bir işte başarı veya savaşta üstünlük
  العذر النجح ولي في هذا الأمر عذر (tahdhib); في الحرب لمن العذر أي النجح والغلبة (tahdhib)

## ل ع ن (root_001359): 40:52 ٱللَّعْنَةُ

- **B001** öfkeyle iyilikten uzaklaştırıp dışlama — öfkeyle iyilikten uzaklaştırma · Tanrı'nın kişiyi iyilikten ve esirgemesinden uzaklaştırması · kovulmuş, insanlardan ayrı bırakılmış kimse · iyilikten uzaklaştırılıp dışlanmış
  أصل صحيح يدل على إبعاد وإطراد (maqayis); أبعده عن الخير والجنة (maqayis); ولعنه الله باعده (ayn); الطرد والإبعاد من الخير (sihah); اللعن الإبعاد (tahdhib); الطرد والإبعاد على سبيل السخط (mufradat)
- **B002** başkasına kötülük dileme ya da ağır sövgü yöneltme — başkasına kötülük dileme veya ağır biçimde sövme · birine yöneltilen kötülük dileği · başkalarına sık sık kötülük dileyen adam · kötülüğü yüzünden herkesin kendisine kötülük dilediği adam · insanlara çok sık kötülük dileyen kimse · başkalarına durmadan kötülük dileyen adam · bir çekişmede kendisine de kötülük dileme · utanmazca davranıp kötülükten geri durmama · eti ve yağı bol olduğu için kimsenin kötülemediği kazan
  ولعنه كثير اللعن (maqayis); لعنته سببته؛ اللعنة الدعاء عليه (ayn); رجل لَعنة يلعن الناس كثيرا (sihah;tahdhib); من الإنسان دعاء على غيره (mufradat); التعن فلان لعن نفسه (mufradat)
- **B003** acı çektirme, biçim bozma ya da yıkıma uğratma — acı çektirme, biçimini bozma ya da yıkıma uğratma · Tanrı'nın acı çektirmesi veya yok etmesi · kutsal metindeki kullanımda ağır yaptırım · biçimi bozulmuş ya da aşağılanıp yok edilmiş · acı çektirilen kimse
  اللعن التعذيب؛ الملعن المعذب؛ اللعنة في القرآن العذاب (ayn;tahdhib); استحق العذاب فصار هالكا (tahdhib); اللعن المسخ أيضا؛ المخزى المهلك (tahdhib); اللعين الممسوخ (sihah); من الله تعالى في الآخرة عقوبة (mufradat)
- **B004** iki tarafın birbirine ya da kendi üzerine kötülük dilemesi — karşılıklı kötülük dileme; eşler arasındaki özel yargısal işlem · tarafların birbirine veya kendi üzerlerine kötülük dilemesi
  اللعان الملاعنة (maqayis); تلاعنوا لعن بعضهم بعضا؛ ملاعنة الرجل امرأته منه في الحكم (ayn); الملاعنة واللعان المباهلة (sihah); الملاعنة بين الزوجين إذا قذف الرجل امرأته (tahdhib); التلاعن والملاعنة أن يلعن كل واحد منهما نفسه أو صاحبه (mufradat)
- **B005** insan biçimli tarla korkuluğu — insan biçimli tarla korkuluğu
  اللعين ما يتخذ في المزارع كهيئة رجل (ayn;tahdhib); الرجل اللعين شيء ينصب وسط المزارع تستطرد به الوحوش (sihah); كهيئة خيال يذعر منه السباع والطيور (tahdhib)
- **B006** dışkılayan kişiye kötülük dilenen ortak kullanım yeri — dışkılama yüzünden kirletene kötülük dilenen yol ve gölgelik yerler · kirleten kişiye kötülük dilenen yol kenarı veya konak yeri
  المَلاعِن قارعة الطريق ومنزل الناس (sihah); المَلاعِن جواد الطريق وظلال الشجر ينزلها الناس؛ يلعنون من جلس للغائط عليها (tahdhib)
- **B007** Kınanıp kötülük dilenecek bir iş yapmazsın [kalıp] — Kınanıp kötülük dilenecek bir iş yapmazsın
  أبيت اللعن أي لا تأتي أمرا تلحى عليه وتلعن (ayn); تحيي ملوكها بأن تقول للملك أبيت اللعن؛ أبيت أيها الملك أن تأتي أمرا تلعن عليه (tahdhib)

## و ر ث (root_001639): 40:53 وَأَوْرَثْنَا

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

## ل ب ب (root_001338): 40:54 ٱلْأَلْبَٰبِ

- **B001** yerinde kalıp bağlılığını sürdürme — bir yerde kalıp oraya yerleşmek · bir yerde kalmak · bir işe bağlı kalmak · sevgiyle yakın durup bağlı kalmak · buyruğa tekrar tekrar karşılık verip bağlı kalma sözü · çağrıya bağlılık ve boyun eğmeyle karşılık verme · bir evin öteki evin karşısında bulunması · çağrıya karşılık veren ve bağlı kalan kimse
  ألب بالمكان إذا أقام به (maqayis;sihah)؛ رجل لب بهذا الأمر إذا لازمه (maqayis;sihah)؛ لبيك أي أنا مقيم على طاعتك (maqayis;sihah)؛ لب بالمكان وألب به إذا أقام به (jamhara;tahdhib;mufradat)؛ إجابة لك بعد إجابة (tahdhib)؛ اللب الطاعة وأصله من الإقامة (tahdhib)؛ داري تلب دارك أي تحاذيها (sihah)
- **B002** sevecenlikle acıyıp gözetme — sevecenlik ve acıma · koyunun yavrusunu dudaklarıyla yalayıp gözetmesi · acıyan ve yumuşak davranan kimse
  لبلب من الشيء أشفق (maqayis)؛ اللبلبة الرقة على الولد (sihah)؛ لبلبت الشاة على ولدها إذا لحسته (sihah)؛ اللبلبة الشفقة على الإنسان (tahdhib)؛ فعل الشاة بولدها إذا لحسته بشفتيها (tahdhib)
- **B003** bir şeyin özü ve seçkin iç bölümü — öz, iç bölüm veya seçkin kısım · bir şeyin özü ve arı bölümü · soyun arı ve seçkin kesimi · develerin en seçkinleri · develerin seçkinleri ya da boğaz kesim yeri çevreleri
  اللُّب معروف من كل شيء وهو خالصه (maqayis)؛ لب كل شيء خالصه (jamhara;sihah)؛ خالص كل شيء لبابه (maqayis)؛ لب النخل قلبها (sihah)؛ لب الجوز واللوز ما في جوفه (sihah)؛ اللباب الخالص من كل شيء (tahdhib)؛ لباب الإبل خيارها (tahdhib)؛ لب الطعام خالصه (mufradat)
- **B004** us, özellikle arı ve sağlam düşünme gücü — us; özellikle arı ve sağlam düşünme gücü · düşünme ve anlama güçleri · iyi anlayan ve sağlam düşünen kimse · anlayıp doğru düşünebilir duruma gelmek · sağlam düşünme ve anlayışlı olma
  سمى العقل لبا (maqayis)؛ رجل لبيب أي عاقل (maqayis;sihah)؛ لب الرجل إذا صار لبيبا (jamhara)؛ اللب العقل والجمع الألباب (sihah)؛ لب الرجل ما جعل في قلبه من العقل (tahdhib)؛ العقل الخالص من الشوائب (mufradat)؛ كل لب عقل وليس كل عقل لبا (mufradat)
- **B005** boyun altı ile üst göğsün birleştiği bölge — develerin seçkinleri ya da boğaz kesim yeri çevreleri · boyun altı, boğaz kesim yeri veya kolyenin durduğu göğüs bölgesi · kolye yeri ya da hayvanın göğsüne geçirilen kayış · birine boyun altı ile üst göğüs arasından vurmak · birinin giysisini göğsünde toplayıp onu çekmek · giysisini göğsünde sıkıca bağlayıp hazırlanmak
  اللَّبّة موضع القلادة من الصدر (maqayis;sihah)؛ اللَّبّة باطن العنق (jamhara)؛ اللَّبّة المنحر (sihah;tahdhib)؛ اللبب موضع القلادة من الصدر (maqayis;sihah)؛ لببت الرجل ضربت لبته (maqayis;mufradat)؛ لببت فلانا إذا جمعت ثيابه عند صدره ونحره (sihah;tahdhib)؛ متلببا به أي تحزم بثوبه عند صدره (tahdhib)؛ لبب الفرس (maqayis)؛ ما يشد على صدر الدابة (sihah)
- **B006** kumun incelip ovaya bağlanan yakın ucu [kalıp] — kumun dağa veya kum sırtına yakın, incelen uç bölümü
  اللبب من الرمل ما كان قريبا من جبل متصلا بسهل (maqayis)؛ اللبب ما استرق من الرمل (sihah)؛ اللبب من الرمل ما كان قريبا من حبل الرمل (tahdhib)
- **B007** ağaca sarılan, sağaltımda kullanılan ot — ağaca sarılarak büyüyen ve sağaltımda kullanılan ot
  اللبلاب نبت (maqayis)؛ اللبلاب نبت يلتوي على الشجر (sihah)؛ اللبلاب بقلة معروفة يتداوى بها (tahdhib)
- **B008** ince duygunun kaynağı sayılan kalp damarları — ince duygunun kaynağı sayılan kalp damarları
  بنات ألبب عروق في القلب يكون منها الرقة (sihah)
- **B009** yarık üstlüğe benzetilen giysi — yarık üstlüğe benzetilen bir giysi
  اللبيبة ثوب كالبقيرة (sihah)
- **B010** bolluk, esenlik ve güven içinde olma [kalıp] — bolluk, genişlik ve güven içinde olmak
  فلان في لبب رخي إذا كان في حال واسعة (sihah)؛ في سعة وخصب وأمن (tahdhib)؛ في سعة (mufradat)
- **B011** koyun sürüsünün toplu gürültüsü — koyun sürüsünün toplu sesleri ve gürültüsü
  لبالب الغنم جلبتها وأصواتها (sihah)

## ص ب ر (root_000840): 40:55 فَٱصْبِرْ, 40:77 فَٱصْبِرْ

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

## ب ك ر (root_000143): 40:55 وَٱلْإِبْكَٰرِ

- **B001** günün ilk vakti ve o vakitte harekete geçme — günün ilk saatleri · günün ilk saatlerine girmek · günün ilk saatlerinde yola çıkmak · erken davranmak veya işe erken başlamak · bir şeye vakit geçirmeden yönelmek · birini başkasına erkenden göndermek · akşam namazını güneş kaybolur kaybolmaz kılmak · işine erkenden koyulan kimse · yağış döneminin başında gelen yağmur veya gecenin sonunda ilerleyen bulut
  البكرة وهي الغداة (maqayis); البكرة وهي الغداة (ayn); أتيته بكرة أي باكرا (sihah); البكور والتبكير الخروج في ذلك الوقت (tahdhib); البكرة التي هي أول النهار (mufradat)
- **B002** bir şeyin ilki veya ilk ortaya çıkanı — bir şeyin ilki · ilk olgunlaşan ürün · bir şeyin ilkini ele geçirmek · ilk kez ürün veren asma · erken meyve vermek veya ilk olgunlaşan hurma olmak · bitkiyi ilk çıkaran toprak · yağış döneminin başında gelen yağmur veya gecenin sonunda ilerleyen bulut · ikinci vuruşa gerek bırakmayan kesin darbe · başka ateşten alınmamış ateş · yeni ortaya çıkan gereksinim · genç işçi arıların yaptığı ya da genç kızların yumuşattığı bal
  البكر من كل أمر أوله (maqayis); البكر من كل شيء أوله (ayn); الباكورة أول الفاكهة (sihah); الباكور من كل شيء المبكر السريع الإدراك (tahdhib); لكل متعجل في أمر بكر (mufradat); ضربة بكر أي قاطعة لا تثنى (sihah); نار بكر لم تقتبس من نار وحاجة بكر طلبت حديثا (tahdhib)
- **B003** erginlik eşiğine gelmemiş genç deve veya inek — erginlik dişi çıkmamış genç deve · erginlik dişi çıkmamış genç dişi deve · genç erkek deve · henüz gebe kalmamış veya doğurmamış genç inek
  البكر من الإبل ما لم يبزل (maqayis;ayn;tahdhib); البكر الفتي من الإبل (sihah); بقرة بكر فتية لم تحمل (maqayis;ayn;tahdhib); لا فارض ولا بكر هي التي لم تلد (mufradat)
- **B004** daha önce cinsel ilişki yaşamamış olma — daha önce cinsel ilişkiye girmemiş kadın · cinsel ilişki yaşamamış olma durumu · daha önce cinsel ilişkiye girmemiş erkek · bir kadının daha önce cinsel ilişki yaşamamış olma durumunu ilk birleşmeyle sona erdirmek · genç işçi arıların yaptığı ya da genç kızların yumuşattığı bal
  البكر من النساء التي لم تمسس قط (maqayis); البكر التي لم تمس من النساء (ayn); البكر العذراء (sihah); البكر من الرجال الذي لم يقرب النساء بعد (tahdhib); سميت التي لم تفتض بكرا (mufradat); ابتكر الرجل المرأة أي أخذ قضتها (ayn)
- **B005** ilk çocuk ve ilk kez anne ya da baba olma — anne babasının ilk çocuğu · onun ilk çocuğu · kendileri de ilk çocuk olan anne babanın ilk çocuğu · yalnız bir kez doğum yapmış kadın · ilk çocuğunu doğurmak; özel kullanımda ilk çocuğu erkek olmak
  إذا ولدت المرأة واحدا فهي بكر (maqayis); البكر أول ولد الرجل (ayn); البكر المرأة التي ولدت بطنا واحدا وبكرها ولدها (sihah); بكر أبويه وهو أول ولد يولد لهما (tahdhib); وسمي أول الولد بكرا وكذلك أبواه (mufradat); ابتكرت الحامل إذا ولدت بكرها (tahdhib)
- **B006** su çekme ipinin döndüğü oluklu makara — kuyudan su çekerken ipin döndüğü oluklu makara · kılıç süslemesindeki halkalar
  البكرة التي يستقى عليها (maqayis;sihah); خشبة مستديرة في وسطها محز للحبل (ayn;tahdhib); البكرة المحالة الصغيرة (mufradat); الحلق التي في حلية السيف هي البكرات (maqayis;ayn;tahdhib)
- **B007** hepsi eksiksiz biçimde birlikte gelmek — hepsi birlikte, aynı yoldan veya art arda gelmek · hepsi birden · insan topluluğu
  جاءوا على بكرة أبيهم للجماعة إذا جاءوا معا ولم يتخلف منهم أحد وليس هناك بكرة في الحقيقة (sihah); جاءوا على طريقة واحدة وجاءوا بأجمعهم وجاءوا بعضهم في إثر بعض وليس ثم بكرة (tahdhib)

## خ ل ق (root_000434): 40:57 لَخَلْقُ, 40:57 خَلْقِ, 40:62 خَٰلِقُ, 40:67 خَلَقَكُم

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

## ء ن س (root_000059): 40:57 ٱلنَّاسِ, 40:57 ٱلنَّاسِ, 40:59 ٱلنَّاسِ, 40:61 ٱلنَّاسِ, 40:61 ٱلنَّاسِ

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

## ك ث ر (root_001286): 40:57 أَكْثَرَ, 40:59 أَكْثَرَ, 40:61 أَكْثَرَ, 40:82 أَكْثَرَ

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

## س و ي (root_000766): 40:58 يَسْتَوِى

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

## ع م ي (root_001049): 40:58 ٱلْأَعْمَىٰ

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

## ECHO ع م م (root_001047): for 40:58 ٱلْأَعْمَىٰ: withheld observed target; not identity

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

## ج و ب (root_000273): 40:60 أَسْتَجِبْ

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

## ECHO ج ي ب (root_000283): for 40:60 أَسْتَجِبْ: withheld observed target; not identity

- **B001** gömlek açıklığı ve onu oyup oluşturma — gömlek açıklığı veya açıklığın yeri · gömleğin açıklığını oyarak açmak · gömleğe açıklık yapmak
  الجيب جيب القميص (maqayis;sihah)؛ جيب القميص معروف (jamhara)؛ جبيت القميص تجبيبا جعلت له جيبا (ayn)؛ جبت القميص قورت جيبه وجيبته جعلت له جيبا (maqayis)؛ جيبت القميص تجييبا إذا جعلت له جيبا (sihah)؛ جمع جيب (mufradat)

## ECHO ج ب ي (root_000220): for 40:60 أَسْتَجِبْ: withheld observed target; not identity

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

## ECHO ج ب ب (root_000214): for 40:60 أَسْتَجِبْ: withheld observed target; not identity

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

## د خ ر (root_000463): 40:60 دَاخِرِينَ

- **B001** aşağı duruma düşüp boyun eğme — küçük düşüp istemeden boyun eğmek · aşağılanmış ve küçük düşmüş kimse · küçük düşme ve aşağılanma · onu aşağılayıp boyun eğer duruma getirmek
  أصل يدل على الذل؛ دخر الرجل وهو داخر إذا ذل؛ أدخره غيره أذله (maqayis)؛ الداخر الصاغر؛ دخر يدخر دخورا أي صغر؛ يفعل ما تأمره كرها على صغر ودخور (ayn)؛ دخر الرجل يدخر دخرا إذا ذل؛ أدخره غيره إدخارا (jamhara)؛ الدخور الصغار والذل؛ دخر الرجل فهو داخر؛ أدخره غيره (sihah)؛ أذلاء؛ أدخرته فدخر أي أذللته فذل (mufradat)

## ج ع ل (root_000248): 40:61 جَعَلَ, 40:64 جَعَلَ, 40:79 جَعَلَ

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

## ل ي ل (root_001392): 40:61 ٱلَّيْلَ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## س ك ن (root_000726): 40:61 لِتَسْكُنُوا۟

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

## ن ه ر (root_001559): 40:61 وَٱلنَّهَارَ

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

## ف ض ل (root_001163): 40:61 فَضْلٍ

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

## ش ك ر (root_000810): 40:61 يَشْكُرُونَ

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

## ء ن ي (root_000063): 40:62 فَأَنَّىٰ, 40:69 أَنَّىٰ

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

## ECHO ء و ن (root_000068): for 40:62 فَأَنَّىٰ, 40:69 أَنَّىٰ: withheld observed target; not identity

- **B001** yumuşak ve rahat davranma — yumuşak davrandı · rahatlık, dinginlik ve yumuşak davranma · yolculukta kendini yorma, rahat git · yumuşak ve rahat davrandın · rahat ve dingin adam · rahat ve dingin geceler
  كلمة واحدة تدل على الرفق (maqayis); آن يؤون أونا إذا رفق (maqayis); الأون: الدعة والسكينة والرفق (sihah); أن على نفسك أي ارفق في السير واتدع (maqayis;sihah); رجل آئن (maqayis); رجل آين أي رافه وادع (sihah); ليال أوائن روافه وآينات وادعات (sihah)
- **B002** yük yanı — yük kabının bir yanı; dengeli yük parçası · iki yanlı çıkın veya çift yanlı yük · eşeğin yiyip içince karnı ve iki yanı yük gibi doldu
  الأون: أحد جانبي الخرج (sihah); الأون: العدل (sihah); أون الحمار إذا أكل وشرب وامتلأ بطنه وامتدت خاصرتاه فصار مثل الأون (sihah)
- **B003** belirli zaman — belirli zaman · ayrı zamanlar, ara ara gelen vakitler · o işi ara sıra yapar ve ara sıra bırakır
  الأوان: الحين، والجمع آونة (sihah); فلان يصنع ذلك الأمر آونة إذا كان يصنعه مرارا ويدعه مرارا (sihah)
- **B004** büyük kemerli yapı bölümü — büyük kemerli yapı bölümü · büyük kemerli yapı bölümü; belirli saray örneğiyle de anılır · büyük kemerli yapı bölümü · büyük kemerli yapı bölümleri · büyük kemerli yapı bölümleri
  الأوان والإيوان: الصفة العظيمة كالأزج (sihah); إيوان كسرى (sihah); جمع الإوان أون وجمع الإيوان إيوانات وأواوين (sihah)

## ء ف ك (root_000041): 40:62 تُؤْفَكُونَ, 40:63 يُؤْفَكُ

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

## ج ح د (root_000224): 40:63 يَجْحَدُونَ

- **B001** içten bildiğinin tersini söyleyerek bile bile yadsıma — doğru olduğunu bilerek yadsıma; içten benimsediğinin tersini söyleme · doğru olduğunu bildiği şeyi yadsımak veya içten benimsediğinin tersini söylemek · birine düşen payı ya da alacağı tanımamak · bile bile yadsımaya özgü biçimde davranmak
  الجحود وهو ضد الإقرار ولا يكون إلا مع علم الجاحد به أنه صحيح (maqayis); الجحود ضد الاقرار كالانكار والمعرفة (ayn;tahdhib); الجحود الإنكار مع العلم وجحده حقه وبحقه (sihah); الجحود نفي ما في القلب إثباته وإثبات ما في القلب نفيه (mufradat)
- **B002** iyilik, geçim, mal, yağmur ya da bitki bakımından azlık ve darlık — azlık, darlık, eli sıkılık ve iyilik azlığı · iyilik ve yarar azlığı · iyilik ve yarar azlığı · yoksul, eli dar, cimri ve az iyilik yapan kişi · eli dar ve az iyilik yapan olmak; malı tükenmek · malı tükenmek ve darlık durumuna düşmek · yağmuru az yıl · az ve kısa kalmak; yeterince büyümemek · bitkisi az toprak · darlık ve iyilik azlığı dileyen kınama veya beddua sözü · malı tükenmiş veya elindeki varlık azalmış
  أصل يدل على قلة الخير وعام جحد قليل المطر ورجل جحد فقير والجحد من كل شيء القلة وأجحد الرجل وجحد إذا أنفض وذهب ماله (maqayis); الجحد من الضيق والشح ورجل جحد قليل الخير (ayn); الجحد قلة الخير وجحد الرجل إذا كان ضيقا قليل الخير وعام جحد قليل المطر وجحد النبت إذا قل ولم يطل (sihah); الجحد من الضيق والشح وجحد عيشهم إذا ضاق واشتد (tahdhib); رجل جحد شحيح قليل الخير يظهر الفقر وأرض جحدة قليلة النبت (mufradat)
- **B003** kısa ve kalın yapılı at — kalın gövdeli, kısa boylu at · kalın gövdeli, kısa boylu dişi at · kalın gövdeli, kısa boylu atlar
  فرس جحد والأنثى جحدة والجميع جحاد وهو الغليظ القصير (tahdhib)
- **B004** süt dolu tulum veya hurma ya da buğday dolu büyük çuval — 
  الجحادية قربة ملئت لبنا أو غرارة ملئت تمرا أو حنطة (tahdhib)

## ص و ر (root_000891): 40:64 وَصَوَّرَكُمْ, 40:64 صُوَرَكُمْ

- **B001** bir yöne eğilme veya yöneltme — 
  صور يصور إذا مال؛ صرت الشيء أصوره وأصرته إذا أملته إليك (maqayis)؛ يصور عنقه إلى الشيء إذا مال نحوه (ayn;tahdhib)؛ الصور بالتحريك الميل؛ أصاره فانصار؛ طعنه فتصور أي مال للسقوط؛ صر إلي وصر وجهك إلي أي أقبل علي (sihah)؛ صرعه فتجور وتصور إذا سقط (tahdhib)
- **B002** toplama ya da kesip ayırma — 
  صرهن أي ضمهن ويقال قطعهن (ayn)؛ صرت الشيء أيضا قطعته وفصلته؛ فصرهن بضم الصاد وكسرها (sihah)
- **B003** ayırt edici görünüş ve biçim — bir şeyin ayırt edici görünüşü veya somut ya da zihinsel biçimi · varlıklara görünüş ve biçim veren · güzel görünümlü erkek · bir şeyi zihnimde canlandırdım · yapılmış görüntüler veya heykeller
  الصورة صورة كل مخلوق وهي هيئة خلقته؛ البارئ المصور؛ رجل صير إذا كان جميل الصورة (maqayis)؛ صورت صورة وتجمع على صور (ayn)؛ صوره الله صورة حسنة فتصور؛ تصورت الشيء؛ التصاوير التماثيل (sihah)؛ المصور من صفات الله تعالى لتصويره صور الخلق؛ حسن الصورة والهيئة (tahdhib)؛ الصورة ما ينتقش به الأعيان ويتميز بها غيرها؛ محسوس؛ معقول (mufradat)
- **B004** üfleme boynuzu — içine üflenilen boynuz biçimli araç
  الصور القرن (sihah)؛ الصور القرن فهو واحد لا يجوز أن يقال واحدته صورة؛ صاحب القرن قد التقم القرن (tahdhib)
- **B005** palmiye kümesi — palmiye kümesi veya genç palmiyelik · palmiye ağacı · ağaçlı arazi · atın palmiye kümesine benzetilen alın yelesi
  الصور جماعة النخل وهو الحائش؛ شعر الناصية من الفرس يسمى صورا؛ التشبيه بصور النخل؛ الصارة أرض ذات شجر (maqayis)؛ الصور النخل الصغار (ayn)؛ الصور بالتسكين النخل المجتمع الصغار؛ كأن عرفا مائلا من صوره؛ أرض ذات شجر (sihah)؛ دخل صور نخل؛ الصور جماع النخل؛ الصورة النخلة (tahdhib)
- **B006** sığır sürüsü — sığır sürüsü, özellikle yabani sığır sürüsü · sığır sürüleri · az sayıdaki sığır sürülerini bildiren çoğul
  الصوار وهو القطيع من البقر والجمع صيران (maqayis)؛ الصوار والصوار القطيع من بقر الوحش والعدد أصورة ويجمع على صيران (ayn)؛ الصيران جمع صوار وهو القطيع من البقر (sihah)؛ الصوار والصوار القطيع من البقر والعدد أصورة والجميع صيران (tahdhib)
- **B007** miskin kokusu, kabı, kesesi veya parçası — miskin kokusu, kabı, keseleri veya parçaları · misk keseleri ya da gömlek düğmelerine yerleştirilen misk parçaları · miskle ilgili aynı adın değişik söylenişi
  الصوار صوار المسك؛ قال قوم هو ريحه وقال قوم هو وعاؤه (maqayis)؛ أصورة المسك نافقاته؛ الصوار ريح المسك؛ أصورة المسك قطع تجعل في أزرار القمص (ayn)؛ الصوار أيضا وعاء المسك (sihah)؛ أصورة المسك نافقاته (tahdhib)
- **B008** baş derisinde kaşıntı — başta, saçı ayıklatma isteği veren kaşıntı benzeri duyum
  أجد في رأسي صورة أي حكة (maqayis)؛ أجد في رأسي صورة وهي شبه الحكة حتى يشتهي أن يفلى رأسه (sihah)؛ الصورة الحكة انتغاش الحطى في الرأس؛ تشفيني من الصورة (tahdhib)
- **B009** çağrılınca karşılık veren serçe [kalıp] — çağrılınca karşılık veren serçe
  عصفور صوار وهو الذي إذا دعي أجاب؛ لا أحسبه عربيا؛ إن صح أن يكون من الباب لأنه يميل إلى داعيه (maqayis)؛ عصفور صوار وهو الذي يجيب الداعي (ayn;tahdhib)؛ عصفور صوار للذي يجيب إذا دعي (sihah)
- **B010** ağzın iki köşesi — ağzın iki köşesi · ağzın iki köşesi için kullanılan halk söyleyişi
  الصواران صماغا الفم؛ العامة تسميهما الصوارين وهما الصامغان أيضا (tahdhib)

## ح س ن (root_000323): 40:64 فَأَحْسَنَ

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

## ط ي ب (root_000961): 40:64 ٱلطَّيِّبَٰتِ

- **B001** bağlama göre hoş, temiz, iyi veya dinen izinli olan — hoş, iyi veya temiz duruma gelmek; öyle olmak · kötünün karşıtı olan hoş, temiz ve iyi şey · kullanılmasına veya tüketilmesine izin verilen · yenmesine izin verilen, hoş ve insana dokunmayan yiyecek · bilgisizlikten ve kötü davranışlardan arınmış, inançlı ve iyi insan · üzerinde pislik bulunmayan temiz toprak · hoş, temiz ve iyi olan · son derece hoş ve iyi
  الطيب ضد الخبيث (maqayis)؛ طاب يطيب طيبا فهو طيب (ayn;mufradat)؛ الطيب خلاف الخبيث (jamhara;sihah)؛ أصل الطيب ما تستلذه الحواس وما تستلذه النفس (mufradat)؛ الطعام الطيب في الشرع ما كان متناولا من حيث ما يجوز (mufradat)؛ الطيب من الإنسان من تعرى من نجاسة الجهل والفسق (mufradat)؛ صعيدا طيبا أي ترابا لا نجاسة به (mufradat)؛ الطاب الطيب (maqayis;sihah;mufradat)؛ شيء طياب أي طيب جدا (sihah)
- **B002** aldatmasız ve antlaşmayı bozmadan tutsak alma [kalıp] — aldatma veya antlaşmayı bozma olmadan gerçekleştirilen tutsak alma
  سبي طيبة أي طيب (maqayis)؛ سبي طيبة صحيح السباء لم يكن عن غدر ولا نقض عهد (sihah)
- **B003** tuvalet sonrası pisliği gidererek temizlenme — tuvalet sonrasında bedendeki pisliği giderip temizlenme
  الاستطابة الاستنجاء لأن الرجل يطيب نفسه مما عليه من الخبث بالاستنجاء (maqayis)؛ الاستطابة أيضا الاستنجاء (sihah)؛ سمي الاستنجاء استطابة لما فيه من التطيب والتطهر (mufradat)
- **B004** yeme ile cinsel birlikteliği birlikte adlandıran ikili — yeme ve cinsel birlikteliği birlikte gösteren ikili ifade
  الأطيبان الأكل والنكاح (maqayis)؛ الأطيبان الأكل والجماع (sihah)؛ قيل الأطيبان الأكل والنكاح (mufradat)
- **B005** Peygamber'in şehri için kullanılan özel ad — Peygamber'in şehri için kullanılan özel ad
  طيبة مدينة الرسول (maqayis)؛ المدينة تسمى طيبة (jamhara)؛ طيبة اسم مدينة الرسول (sihah)؛ سميت المدينة طيبة (mufradat)
- **B006** içten razı olma ve iç rahatlığı bulma [kalıp] — kendi isteğimle, hiçbir baskı görmeden · içime sindi ve ondan hoşnut oldum · iç rahatlatan, insana ferahlık veren şey
  هذا طعام مطيبة للنفس (maqayis)؛ فعلت ذاك بطيبة نفسي إذا لم يكرهك عليه أحد (sihah)؛ طبت به نفسا أي طابت نفسي به (sihah)؛ طعام مطيبة للنفس إذا طابت به النفس (mufradat)
- **B007** güzel koku sürünmek için kullanılan koku maddesi — güzel koku sürünmek için kullanılan koku maddesi
  الطيب ما يتطيب به (sihah)؛ ما به من الطيب (sihah)
- **B008** biriyle şakalaşıp hoşça takılmak — biriyle şakalaşmak ve ona hoşça takılmak
  طايبه أي مازحه (sihah)
- **B009** sonsuz mutluluk yurdundaki özel ağaç veya bütün güzel şeyler — sonsuz mutluluk yurdundaki özel bir ağaç ya da oradaki bütün güzel şeyler
  طوبى فعلى من الطيب (sihah)؛ طوبى اسم شجرة في الجنة (sihah)؛ طوبى لهم قيل هو اسم شجرة في الجنة وقيل بل إشارة إلى كل مستطاب في الجنة (mufradat)

## ب ر ك (root_000109): 40:64 فَتَبَارَكَ

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

## ن ه ي (root_001560): 40:66 نُهِيتُ

- **B001** bir eylemi yasaklama, engelleme veya ondan geri durma — yasaklama ve engelleme · onu bundan alıkoyup bıraktırdı · ondan geri durdu · kötülükten birbirlerini alıkoydular · benliği tutkudan alıkoymak · kötülükten sık sık alıkoyan · onu bizden alıkoyacak kimse yok
  النهي خلاف الأمر (ayn;sihah)؛ النهي الزجر عن الشيء (mufradat)؛ نهيته عنه فانتهى عنك (maqayis;sihah)؛ وتناهوا عن المنكر أي نهى بعضهم بعضا (sihah)؛ ما تنهاه عنا ناهية أي ما تكفه عنا كافة (ayn)
- **B002** son noktaya varma veya bir şeyi hedefine ulaştırma — bitiş noktası ve son sınır · varış sınırı · son sınır · haberi ona ulaştırdı · oku ona ulaştırdı · ulaştırma ve bildirme · devenin burun bağının uç bölümü
  النهاية الغاية حيث ينتهي إليه الشيء وهو النهاء (ayn)؛ نهاية كل شيء غايته (maqayis)؛ أنهيت إليه الخبر بلغته إياه (maqayis;mufradat)؛ الإنهاء الإبلاغ وأنهيت إليه الخبر فانتهى وتناهى أي بلغ (sihah)؛ النهاية طرف العران الذي في أنف البعير (ayn)
- **B003** kötü davranışı önleyen akıl ve sağduyu — kötü davranışı önleyen sağduyu · kötü davranışı önleyen akıllar · onu durduracak aklı yok
  النهية العقل لأنه ينهى عن قبيح الفعل والجمع نهى (maqayis)؛ النهية العقول لأنها تنهى عن القبيح (sihah)؛ النهية العقل الناهي عن القبائح جمعها نهى (mufradat)
- **B004** akış sonunda suyun durulup biriktiği yer — suyun akıp toplandığı doğal gölcük · suyun akıp toplandığı doğal gölcük · su gölcükte durup sakinleşti · vadide sel sularının son bulup yayıldığı yer
  النهي والنهي الغدير لأن الماء ينتهي إليه (maqayis)؛ النهي الغدير حيث ينخرم السيل في الغدير (ayn)؛ تناهى الماء إذا وقف في الغدير وسكن (sihah)؛ تنهية الوادي حيث ينتهي إليه السيول (maqayis;mufradat)
- **B005** başkasını aratmayacak kadar yeterli [kalıp] — başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli kadın
  فلان ناهيك من رجل ونهيك كما يقال حسبك (maqayis)؛ هذا رجل ناهيك من رجل ونهيك من رجل ونهاك من رجل (sihah)؛ ناهيك من رجل كقولك حسبك (mufradat)
- **B006** semizliğin doruğuna ulaşmış deve [kalıp] — semizliğin doruğuna ulaşmış dişi deve · iri ve semiz kesimlik deve
  ناقة نهية تناهت سمنا (maqayis;mufradat)؛ جزور نهية أي ضخمة سمينة (sihah)
- **B007** sonuçtan bağımsız olarak ihtiyacı aramayı bırakma [kalıp] — ihtiyacı aramayı, bulsa da bulmasa da bıraktı
  طلب الحاجة حتى نهي عنها تركها ظفر بها أم لا (maqayis)؛ طلب الحاجة حتى نهى عنها أي تركها ظفر بها أو لم يظفر (sihah)؛ طلب الحاجة حتى نهي عنها أي انتهى عن طلبها ظفر بها أو لم يظفر (mufradat)
- **B008** günün veya suyun yükselmesi [kalıp] — günün yükselip öğleye yaklaşması · suyun yükselmesi
  نهاء النهار ارتفاعه (maqayis;mufradat)؛ نهاء النهار ارتفاعه قراب نصف النهار (ayn)؛ نهاء الماء بالضم ارتفاعه (sihah)
- **B009** şişe veya cam eşya için tartışmalı ad — 
  النهاء القوارير وليس كذلك عندنا (maqayis)؛ النهاء القوارير والزجاج (sihah)
- **B010** yaklaşık yüzlük miktar [kalıp] — yaklaşık yüz kişi veya öğelik miktar
  هم نهاء مائة ونهاء مائة أيضا أي قدر مائة (sihah)

## س ل م (root_000737): 40:66 أُسْلِمَ

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

## ت ر ب (root_000178): 40:67 تُرَابٍ

- **B001** toprak ve toprağa bağlı kullanımlar — toprak ve toprağın değişik adları · yerin kendisi veya toprağın kendisi · yer toprağının yüzü veya toprak yapısı · bir şeyin toprağa bulanması · bir şeyi toprakla bulamak veya düzeltmek · bir şeyin üzerine toprak koymak · toprak taşıyan rüzgar · ölünün toprakla örtülü gömü yeri
  التراب وهو التيرب والتوراب (maqayis)؛ التراب والتيرب والتورب كله من أسماء التراب (jamhara)؛ الترباء الأرض نفسها (maqayis;sihah;mufradat)؛ ترب الشيء أصابه التراب (sihah)؛ تترب إذا تلوث في التراب (tahdhib)؛ ريح تربة جاءت بالتراب (maqayis;sihah;mufradat)؛ تربة الميت رمسه (jamhara)
- **B002** toprağa düşmüş yoksulluk — toprağa yapışmış gibi yoksullaşmak · yoksulluk, düşkünlük ve geçim darlığı · yoksulluktan toprağa yapışmış düşkün kimse · görünüşte yoksulluk dileği olan kalıplaşmış söz · az mal sahibi olma
  ترب الرجل إذا افتقر كأنه لصق بالتراب (maqayis;sihah;mufradat)؛ المتربة الفقر (jamhara)؛ مسكين ذو متربة أي لاصق بالتراب (sihah;mufradat)؛ رجل ترب فقير (tahdhib)؛ تربت يداك (sihah;tahdhib;mufradat)
- **B003** varlıklı hale gelmek — varlıklı olmak ve malı çoğalmak · çok mal sahibi olma
  أترب إذا استغنى كأنه صار له من المال بقدر التراب (maqayis;sihah;mufradat)؛ أترب الرجل إذا استغنى (jamhara)؛ أترب الرجل فهو مترب إذا كثر ماله (tahdhib)؛ التتريب كثرة المال (tahdhib)
- **B004** yaşıt ve denk arkadaş — yaşıt, birlikte yetişmiş arkadaş veya denk kişi · yaşıtlar veya denk kişiler
  الترب الخدن والجمع أتراب (maqayis)؛ الترب اللدة الذي ينشأ معك والجمع أتراب (jamhara)؛ هذه ترب هذه أي لدتها وهن أتراب (sihah)؛ أترابا أي أمثالا وهما تربان (tahdhib)؛ أتراب أي لدات تنشأن معا (mufradat)
- **B005** göğsün kolye yeri — göğüs kemikleri veya göğüste kolye yeri · göğüste kemik uçlarının denk durduğu bölge
  التريب الصدر عند تساوي رءوس العظام (maqayis)؛ التريبة مجال القلادة في الصدر والجمع الترائب (jamhara)؛ التريبة واحدة الترائب وهي عظام الصدر ما بين الترقوة إلى الثندؤة (sihah)؛ الترائب موضع القلادة من الصدر (tahdhib)؛ الترائب ضلوع الصدر الواحدة تريبة (mufradat)
- **B006** parmak uçları — parmak uçları; tekili parmak ucu
  التربات وهي الأنامل الواحدة تربة (maqayis)؛ التربات الأنامل الواحدة تربة (sihah)
- **B007** belirli bir bitki — belirli bir bitki adı
  التربة وهو نبت (maqayis)؛ التربة ضرب من النبت (jamhara)؛ التربة أيضا نبت (sihah)
- **B008** belirli yer adları — belirli bir yerin adı; yüzey biçimi burada üretilmez · belirli bir yer veya vadinin adı; yüzey biçimi burada üretilmez · belirli bir yerin adı; yüzey biçimi burada üretilmez
  يترب موضع قريب من اليمامة (jamhara;sihah)؛ تربة موضع لا تدخله الألف واللام (jamhara)؛ تربة واد من أودية اليمن (tahdhib)؛ تربان موضع معروف (jamhara)
- **B009** uysal deve — uysal ve kolay yönetilir deve
  جمل تربوت وناقة تربوت أي ذلول (sihah)؛ بعير تربوت إذا كان ذلولا وناقة تربوت كذلك (tahdhib)

## ن ط ف (root_001518): 40:67 نُّطْفَةٍ

- **B001** inci veya küpe türü kulak süsü — inci veya küpe · tek inci tanesi veya tek küpe · kulağında inci veya küpe bulunan · kadın küpe taktı
  النطف اللؤلؤ الواحدة نطفة (maqayis;ayn;tahdhib;mufradat)؛ بل النطف القرطة (maqayis)؛ النطفة القرط والجمع نطف (sihah)؛ وصيفة منطفة مقرطة (ayn;sihah;tahdhib)؛ تنطفت المرأة أي تقرطت (sihah)؛ صبي منطف إذا كان في أذنه لؤلؤة (mufradat)
- **B002** damladan denize duru su ve erkek üreme sıvısı — az veya çok miktarda duru su · çocuğun oluşumuna katılan erkek üreme sıvısı · iki deniz veya iki büyük su kütlesi
  النطفة الماء الصافي (maqayis;mufradat)؛ النطفة الماء الصافي قل أو كثر (ayn;sihah)؛ في القربة نطفة من ماء مثل الجرعة (tahdhib)؛ المويهة القليلة والماء الكثير نطفة (tahdhib)؛ النطفة التي يكون منها الولد (ayn)؛ النطفة ماء الرجل (sihah;mufradat)؛ المني نطفة (tahdhib;mufradat)؛ النطفة أي البحر وماؤه والنطفتين بحر المشرق وبحر المغرب (tahdhib)
- **B003** sıvının akması veya damlaması — su aktı veya damladı · sabaha kadar yağmur yağan gece · akan veya damlayan sıvı; koyulaşmamış akışkan tatlı · akıntısı çok olan burun · ter · iyiliği bol bol veren kişi
  ليلة نطوف مطرت حتى الصباح (maqayis;ayn;sihah;tahdhib;mufradat)؛ النطف الصب والقطر والناطف القاطر وأنف نطوف كثير القطران (ayn)؛ نطفان الماء سيلانه (sihah)؛ نطف الماء ينطف نطفا ونطفانا إذا قطر (tahdhib)؛ النطاف العرق (maqayis)؛ الناطف السائل من المائعات ومنه الناطف المعروف وفلان منطف المعروف (mufradat)؛ الناطف القبيط (ayn;sihah)؛ القبيط لأنه ينطف قبل استضرابه (tahdhib)
- **B004** ayıp, kuşku veya suçlamayla lekeleme; bozulma — ayıp, kuşku ve kınamayla lekelenme · onu kötülükle lekeledi veya yüz kızartıcı bir davranışla suçladı · kişi kuşkuyla suçlandı veya kuşkulu duruma düştü · ona bulaşıp lekelendim · şey bozuldu · pis ve inançsız diye aşağılanan topluluk · suçlama; sesleri yer değiştirmiş biçim
  النطف التلطخ بالعيب (maqayis;ayn;sihah;tahdhib)؛ فلان ينطف بسوء أي يلطخ (ayn;tahdhib)؛ فلان ينطف بفجور أي يقذف به (ayn;tahdhib)؛ فلان ينطف بسوء (mufradat)؛ هم أهل الريب والنطف ونطف الرجل إذا اتهم بريبة (sihah)؛ نطف الشيء فسد (sihah;maqayis)؛ قوم نطفون وحرون نجسون كفار (tahdhib)؛ الطنف في التهمة من المقلوب كأنه من النطف (maqayis-cross)
- **B005** iç boşluğa veya beyne dayanan derin yara — iç boşluğa veya beyne dayanan derin yara · yara içe kadar derinleşti · sırt yarası iç boşluğa yaklaşmış deve
  النطف عقر الجرح ونطف الجرح أي عقر (ayn)؛ النطف إشراف الشجة على الدماغ والدبرة على الجوف وقد نطف البعير (sihah)؛ النطف عقر الجرح وأنطف الجرح (tahdhib)؛ البعير النطف الذي قد أشرفت دبرته على الجوف وكذلك الذي أشرفت شجته على الدماغ (tahdhib)
- **B006** aşırı yiyip yiyecekten usanma [kalıp] — kişi tıka basa yiyip yiyecekten usandı
  نطف فلان ينطف نطفا إذا بشم (tahdhib)
- **B007** iğrenip uzak durma veya kendini üstün görme — iğrenip uzak durma; kendini üstün görme
  التنطف التقزز (ayn)؛ التنطف التعزز (tahdhib)

## ع ل ق (root_001039): 40:67 عَلَقَةٍ

- **B001** takılma ve bağlı kalma — bir şeye takılıp kalmak · bir şeyi başka bir şeye asmak · kapıyı yerine takıp kurmak · askı parçası veya kapı sürgüsü · kamçı, yay ya da kılıç askısı · kabı asmaya yarayan bağ · kolye ve küpe askı süsleri · göç imkanı kalmayacak biçimde yerleşmek · dikilen fidanın tutması · öldürülen kişinin kan sorumluluğunun birine yüklenmesi
  يناط الشيء بالشيء العالي (maqayis)؛ علق به إذا لزمه (maqayis)؛ علق بالشيء نشب به (ayn)؛ كل شيء علق به شيء فهو معلاقه (ayn;sihah;tahdhib)؛ تعليق الباب نصبه وتركيبه (ayn;tahdhib)؛ علق القربة الذي تشد به ثم تعلق (sihah;tahdhib)
- **B002** makara taşıyıcı su çekme düzeneği — makarayı taşıyan su çekme düzeneği
  العلق ما تعلق به البكرة من القامة (maqayis;ayn;sihah)؛ آلة البكرة (maqayis;sihah)؛ اسم جامع لجميع آلات الاستقاء بالبكرة (tahdhib)؛ الحبل المعلق بالبكرة (tahdhib)
- **B003** pıhtılaşmış kan ve kan emici su canlısı — koyu veya pıhtılaşmış kan · bir parça pıhtılaşmış kan · suda yaşayan kan emici sülük · boğazına sülük yapışmış kimse veya hayvan · su içerken boğazına sülük yapışmak
  العلق الدم الجامد والقطعة منه علقة (maqayis;ayn)؛ الدم الغليظ والقطعة منه علقة (sihah)؛ العلقة الدم الجامد الغليظ (tahdhib)؛ دويبة في الماء تجمع على علق (ayn;sihah)؛ أخذ العلق بحلقه (maqayis;ayn;tahdhib)
- **B004** kalbe yerleşen sevgi — kalbe yerleşen sevgi · bir kadına gönül vermek · kalıcı sevgi bağı · eşini seven ve ona bağlı kadın
  العلق الهوى (maqayis;sihah)؛ نظرة من ذي علق أي ذي هوى (maqayis;sihah)؛ علقت فلانة أي أحببتها (ayn)؛ علاقة الحب (sihah)؛ العلاقة الهوى اللازم للقلب (tahdhib)؛ العلوق من النساء المحبة لزوجها (maqayis;ayn)
- **B005** yapışkan ve ısrarlı çekişme — biriyle çatışıp çekişmek · kişiye bağlı dava veya çekişme · sert ve ısrarlı tartışmacı · tartışmada etkili dil · birine diliyle saldırmak
  علق فلان بفلان خاصمه (maqayis;ayn)؛ العلاقة الخصومة (maqayis)؛ علاقة الخصومة (sihah)؛ رجل معلاق إذا كان شديد الخصومة (maqayis;ayn;sihah;tahdhib)؛ الدعوى يقال لها علاقة (tahdhib)؛ علقه إذا تناوله بلسانه (tahdhib)
- **B006** yaşamı sürdürecek az besin — hayvanın yetindiği kıt otlak · yaşamı sürdürecek az yiyecek · devenin ağzıyla koparıp yediği ot · meyveleri ağzıyla alıp yemek · hayvana asılan yem veya ağaca sarılan bitki · devenin otladığı bir bitki · azla yetinen, seçerek yaşayan gibi değildir
  العلاق الذي يجتزىء به الماشية من الكلأ (maqayis)؛ ما يأكل فلان إلا علقة أي ما يمسك نفسه (maqayis)؛ كل شيء يتبلغ به فهو علقة (ayn;sihah)؛ العلقة من الطعام القليل الذي يتبلغ به (tahdhib)؛ العلوق ما تعلقه الإبل أي ترعاه (maqayis;ayn;sihah;tahdhib)؛ تعلق من ثمار الجنة أي تناول بأفواهها (sihah;tahdhib)
- **B007** elden çıkarılmaya kıyılmayan değerli şey — elden çıkarılmaya kıyılmayan değerli şey · özenle sakınılan değerli şey · değerli sayılan bir içki veya hurma içkisi
  هذا علق من الأعلاق للشيء النفيس (maqayis)؛ علق مضنة ومضنة (maqayis;sihah;tahdhib)؛ العلق المال الذي يكرم عليك تضن به (ayn)؛ العلق بالكسر النفيس من كل شيء (sihah)؛ يقال للشراب عليق (ayn;tahdhib)
- **B008** evlilikte askıda bırakılmış kadın — evlilikte askıda bırakılmış kadın · konuşursa boşanır, susarsa askıda kalır
  كالمعلقة هي التي لا تكون أيما ولا ذات بعل (maqayis)؛ المعلقة من النساء التي فقد زوجها (sihah)؛ امرأة معلقة إذا لم ينفق عليها زوجها ولم يطلقها فهي لا أيم ولا ذات بعل (tahdhib)؛ إن أنطق أطلق وإن أسكت أعلق (maqayis)
- **B009** döllenmenin tutup gebeliğin başlaması — kadının gebe kalması · döllenmesi tutmuş dişi veya erkek üreme sıvısı
  علقت المرأة حبلت (maqayis;sihah)؛ العلوق التي قد علقت لقاحا (ayn)؛ علقت وعقدت على الماء (tahdhib)؛ العلوق ماء الفحل (tahdhib)
- **B010** yavruyu benimsemeyip sütünü esirgeyen deve — yavruyu benimsemeyip sütünü esirgeyen deve · yavruyu benimsemeyen veya süt vermeyen develer · başkasının çocuğunu emziren kadın
  العلوق الناقة التي تأبى أن ترأم ولدها (maqayis)؛ من النوق التي تألف الفحل ولا ترأم البو (ayn)؛ المرأة إذا أرضعت ولد غيرها يقال لها علوق (ayn)؛ العلوق والمعالق الناقة تعطف على غير ولدها فلا ترأمه (sihah)؛ ناقة علوق إذا رئمت بأنفها ومنعت درتها (tahdhib)
- **B011** avın tuzağa takılıp yakalanması — ceylanın veya avın tuzağa takılması · avcının tuzağına av düşmesi
  علق الظبي في الحبالة يعلق إذا نشق فيها (maqayis)؛ أعلق الحابل إذا وقع في حبالته الصيد (maqayis)؛ علق الظبي في الحبالة (sihah)؛ أعلقت فأدرك أي علق الصيد في حبالتك (sihah)
- **B012** biçime bağlı adlandırmalar — sülüğü kan emmesi için bedene yerleştirme · çocuğun boğazındaki hastalıklı bölgeyi parmakla tedavi etme
  أعلقت الأم من عذرة الصبي بيدها (maqayis)؛ الإعلاق إرسال العلق على الموضع ليمص الدم (sihah)؛ الإعلاق أيضا الدغر (sihah)؛ معالجة عذرة الصبي ورفعها بالإصبع (tahdhib)؛ غمز حلق الصبي المعذور (tahdhib)
- **B013** sahibi adına erzak getirmeye gönderilen yük hayvanı — sahibi adına erzak getirmeye gönderilen yük hayvanı
  العليقة الدابة تدفع إلى الرجل ليمتار عليها لصاحبها (maqayis)؛ البعير يوجهه الرجل مع قوم يمتارون (sihah)؛ الناقة يعطيها الرجل القوم يمتارون (tahdhib)
- **B014** insanın peşini bırakmayan ağır bela — kişinin başına gelen büyük bela · insanı yakalayıp bırakmayan ölüm · belalar, ölümler veya insanı bağlayan uğraşlar
  جاء فلان بعلق فلق أي بداهية (maqayis;sihah;tahdhib)؛ أعلق وأفلق (maqayis;tahdhib)؛ المنية علوق (maqayis;sihah;tahdhib)؛ العلق الدواهي والمنايا والأشغال (tahdhib)
- **B015** bele kadar inen küçük üst giysisi — bele veya göbeğe kadar inen küçük üst giysisi
  العلقة قميص يكون إلى السرة (maqayis)؛ ثوب صغير وهو أول ثوب يتخذ للصبي (sihah)؛ العلقة الإتب (tahdhib)؛ الصدرة تلبسها الجارية (tahdhib)
- **B016** bir eylemi yapmaya koyulmak — belirtilen eylemi yapmaya koyulmak
  علق يفعل كذا كأنه يتعلق بالأمر الذي يريده (maqayis)؛ علق فلان يفعل كذا أي طنق وصار (ayn)؛ علق يفعل كذا مثل طفق (sihah)؛ علق فلان يفعل كذا كقولك طفق يفعل كذا (tahdhib)؛ يقال أحبه واعتاده (sihah)

## ط ف ل (root_000942): 40:67 طِفْلًا

- **B001** insan ya da hayvanın küçük yavrusu — insan ya da hayvanın küçük yavrusu · çocuklar veya küçük yavrular · küçük kız veya dişi yavru · çocukluk, küçük yaş dönemi
  الأصل المولود الصغير (maqayis)؛ الطفل الصغير من الأولاد للناس والبقر والظباء ونحوها (ayn)؛ الطفل: المولود وولد كل وحشية أيضا طفل والجمع أطفال (sihah)؛ الصبي يدعى طفلا حين يسقط من أمه إلى أن يحتلم (tahdhib)؛ الطفل: الولد ما دام ناعما وقد يقع على الجمع (mufradat)
- **B002** yavrulu dişi; yavrular için yavaş sürme — yavrusu yanında bulunan kadın veya dişi hayvan · yavrusu yanındaki dişi hayvan · yavruları yanlarında olan dişi hayvanlar · develeri yavruları için yavaş sürmek
  المطفل الظبية معها طفلها (maqayis)؛ أطفلت المرأة والظبية والنعم إذا كان معها ولد طفل (ayn;tahdhib)؛ أطفلت المرأة والمطفل الظبية معها طفلها وكذلك الناقة (sihah)؛ المطفل من الظبية التي معها طفلها (mufradat)؛ طفلت الإبل تطفيلا إذا كان معها أولادها فرفقنا بها في السير (maqayis;sihah;tahdhib)
- **B003** narin ve yumuşak; ot için kısa — narin, yumuşak ve gevşek dokulu · beyaz, narin ve yumuşak parmaklı · hafif ve yumuşak esen rüzgâr · henüz uzamamış kısa ot
  المرأة الناعمة طفلة (maqayis)؛ امرأة طفلة الأنامل أي رخصتها في بياض بينة الطفولة (ayn)؛ الطفل بالفتح: الناعم، جارية طفلة وبنان طفل (sihah)؛ الطفل: البنان الرخص وجارية طفلة إذا كانت رخصة (tahdhib)؛ باعتبار النعومة قيل امرأة طفلة (mufradat)؛ ريح طفل إذا كانت لينة الهبوب وعشب طفل لم يطل (tahdhib)
- **B004** günün ve ateşin ilk ışığı ya da ilk karanlık — sabahın veya akşamın ilk zayıf ışığı · güneş doğmaya başladı veya batmaya yöneldi · gecenin çöken ilk karanlığı · yeni tutuşturulan ateş
  طفل الظلام وهو أوله (maqayis)؛ طفل الليل أقبل ظلامه (maqayis;sihah)؛ الطفل طفل الغداة وطفل العشي، طفلت الشمس (ayn;tahdhib)؛ الطفل بالتحريك بعد العصر إذا طفلت الشمس للغروب (sihah)؛ للنار ساعة تقدح طفل وطفلة (tahdhib)؛ طفلت الشمس إذا همت بالدور ولما يستمكن الضح من الأرض (mufradat)
- **B005** belirli yıldız kümesine bağlanan yağmur [kalıp] — belirli yıldız kümesine bağlanan yağmur
  طفل الثريا فالطفل هنا المطر (maqayis)؛ الطفل أيضا مطر، لوهد جاده طفل الثريا (sihah)
- **B006** çağrılmadan yemeğe katılma ve katılan kişi — çağrılmadan yemeğe veya şölene katılma · çağrılmadan yemeğe katılan kişi · çağrılmadığı yemeğe veya düğüne katılmak
  التطفيل أن يأتي الرجل وليمة أو صنيعا لم يدع إليه (ayn)؛ طفيلي للذي يدخل وليمة لم يدع إليها وقد تطفل (sihah)؛ الطفيلي هو الذي يدخل على القوم من غير أن يدعوه (tahdhib)؛ طفل إذا أتى طعاما لم يدع إليه (mufradat)
- **B007** küçük ve kolay gereksinimler [kalıp] — küçük ve kolay gereksinimler
  أطفال الحوائج صغارها، واحدها طفل، يعني حاجة يسيرة (tahdhib)

## ش ي خ (root_000834): 40:67 شُيُوخًا

- **B001** yaşlı kişi, yaşlılık ve yaşlanma — yaşlı erkek · yaşlılık · yaşlanmak, yaşlı duruma gelmek · yaşlanmak, ileri yaşa gelmek · yaşlı kadın
  الشيخ بين الشيخوخة والشيخ والتشييخ (maqayis)؛ رجل شيخ بين الشيخوخة؛ شاخ يشيخ شيوخة؛ الشيخة المرأة (ayn)؛ شاخ الرجل يشيخ شيخا وشيخوخة فهو شيخ؛ امرأة شيخة (jamhara)؛ شاخ الرجل يشيخ شيخا؛ وشيخوخة؛ وشيخ تشييخا أي شاخ (sihah)؛ شاخ الرجل يشيخ شيوخة فهو شيخ؛ قد شيخ الشيخ تشييخا إذا كبر (tahdhib)؛ لمن طعن في السن الشيخ؛ شيخ بين الشيخوخة والشيخ والتشييخ (mufradat)
- **B002** saygı duyulan bilgin — çok bilgili ve saygı duyulan kişi · ona saygı bildiren bir adla seslendi
  شيخته دعوته شيخا للتبجيل (sihah)؛ يعبر به عمن يكثر علمه (mufradat)
- **B003** kadının kocası [kalıp] — kadının kocası, genç olsa bile onun erkek eşi
  لزوج المرأة وإن كان شابا هو شيخها (tahdhib)
- **B004** kötü yanlarını açığa vurup utandırmak [kalıp] — erkeğin kötü yanlarını açığa vurup onu utandırmak
  شيخت بالرجل تشييخا إذا فضحته (tahdhib)
- **B005** aspir ağacı — aspir ağacı için kullanılan özel ad · aynı aspir ağacı için kullanılan tamlamalı ad
  من الأشجار الشيخ؛ شجرة الشيوخ؛ ثمرتها جرو؛ شجرة العصفر (tahdhib)

## و ف ي (root_001669): 40:67 يُتَوَفَّىٰ, 40:77 نَتَوَفَّيَنَّكَ

- **B001** eksiksiz tamamlama ve tam olarak karşılama — tamamlanmak; eksiksiz hale gelmek · sözünü eksiksiz yerine getirme · sözüne bağlı ve hakkı eksiksiz gözeten · tam ve eksiksiz · sözünü tutmak · ölçüyü ve tartıyı tam vermek · hakkını ya da ücretini eksiksiz vermek · tamamını almak · bir şeyi bütünüyle almak · eksiksiz verme ve tamamlama · mali kayıt hesabını hak eksiksiz ödenmiş olarak kapatma
  كلمة تدل على إكمال وإتمام؛ الوفاء إتمام العهد وإكمال الشرط؛ وفى يفي وفاء فهو واف؛ كل شيء بلغ تمام الكمال فقد وفى وتم؛ الوفاء ضد الغدر؛ أوفيت الكيل والوزن؛ توفية الشيء بذله وافيا واستيفاؤه تناوله وافيا؛ توفيت الشيء واستوفيته إذا أخذته كله
- **B002** canın bütünüyle alınması; uykuda bilincin askıya alınması — ölüm · ölmek; canı alınmak · uykuya dalarken bilinci ve ayırt etmesi askıya alınmak
  يقال للميت توفاه الله؛ الوفاة المنية وتوفي فلان وتوفاه الله إذا قبض نفسه؛ توفاه الله أي قبض روحه والوفاة الموت؛ توفي الميت بمعنى استيفاء مدته؛ عبر عن الموت والنوم بالتوفي
- **B003** yüksek bir yere çıkıp yukarıdan bakmak — yüksek bir yere çıkıp yukarıdan bakmak · kuşun çevreyi gözetlemek için konduğu yüksek yer · sık sık yüksek çıkıntılara çıkan
  أوفى على شرف من الأرض إذا أشرف فوقها؛ أوفى الرجل على الجبل أو العلم إذا فرعه أي صار في فرعه؛ أوفى على الشيء أي أشرف؛ الميفاة الموضع الذي يوفي فوقه البازي
- **B004** belirlenen zamanda gelip buluşma ve tam kadro hazır bulunma — gelmek; varmak · sözleşilen zamanda birinin yanına gelme · topluluğun bütün üyeleriyle hazır bulunması
  الموافاة أن توافي إنسانا في الميعاد؛ وافى فلان أتى وتوافى القوم تتاموا؛ ووافيت أوافي؛ الموافاة التي يكتبها كتاب دواوين الخراج مأخوذة من أوفيته حقه
- **B005** fırın kapağı veya tuğla pişirme yapısı — fırın kapağı; tuğla pişirme yapısı
  الميفى طبق التنور؛ البيت الذي يطبخ فيه الآجر يقال له الميفى

## ء ج ل (root_000016): 40:67 أَجَلًا

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

## ع ق ل (root_001036): 40:67 تَعْقِلُونَ

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

## ص ر ف (root_000860): 40:69 يُصْرَفُونَ

- **B001** yönünden veya durumundan geri çevirmek — bir şeyi veya kişiyi yönünden ya da durumundan geri çevirmek · geri dönmek veya yön değiştirmek · bir şeyin yöneltildiği yer veya yön
  معظم بابه يدل على رجع الشيء؛ صرفت القوم صرفا وانصرفوا إذا رجعتهم فرجعوا (maqayis)؛ الصرف أن تصرف إنسانا على وجه يريده إلى مصرف غير ذلك (ayn;tahdhib)؛ صرفت الرجل عني فانصرف؛ صرف الله عنك الأذى (sihah)؛ رد الشيء من حالة إلى حالة أو إبداله بغيره (mufradat)
- **B002** çeşitli yön ve durumlara dönüştürmek — bir şeyi çeşitli yön ve durumlara çevirme · rüzgarları yön ve durumdan duruma çevirme · bildirimleri değişik yönleriyle açıklayıp yineleme · sözcüğü çekimleme veya sonunu dil bilgisel olarak işletme
  تصريف الرياح تصرفها من وجه إلى وجه وحال إلى حال وكذلك تصريف الخيول والسيول والأمور (ayn)؛ تصريف الآيات تبيينها (tahdhib)؛ التصريف كالصرف إلا في التكثير وأكثر ما يقال في صرف الشيء من حالة إلى حالة (mufradat)
- **B003** işlerde çareyle kıvrakça hareket etmek — işlerde çare ve kıvraklık · bir işi türlü yollarla yürütmek · işlerinde kıvrak ve deneyimli kimse · geçim kazanmak
  صيرفيات الأمور متصرفاتها أي تتقلب بالناس (ayn)؛ الصرف الحيلة؛ الصيرف المحتال المتصرف في الأمور (sihah)؛ الصرف التقلب والحيلة؛ يصطرف لعياله أي يكتسب لهم؛ الصيرف والصيرفي المحتال المتقلب في أموره المجرب لها (tahdhib)
- **B004** kabul veya kurtuluş sağlayacak yol — kendisine hiçbir kabul yolu ya da karşılık tanınmaması · cezayı savuşturacak yol da yardım da bulamama
  الصرف في القرآن التوبة (maqayis)؛ الصرف التوبة؛ الصرف الحيلة؛ فما يستطيعون صرفا ولا نصرا (sihah)؛ الصرف التوبة والعدل الفدية؛ الصرف النافلة والعدل الفريضة؛ الصرف الحيلة؛ فما تستطيعون صرفا ولا نصرا (tahdhib)؛ لا يقبل منه صرف ولا عدل؛ لا يقدرون أن يصرفوا عن أنفسهم العذاب (mufradat)
- **B005** para değiştirme ve değer farkı — para değiştirme; paralar arasındaki değer veya ayar farkı · para değiştiricisi
  الصرف فضل الدرهم على الدرهم في القيمة؛ الدينار صرف إلى الدراهم؛ الصيرفي لتصريفه أحدهما إلى الآخر (maqayis)؛ الصرف فضل الدرهم في القيمة وجودة الفضة وبيع الذهب بالفضة (ayn)؛ صرفت الدراهم بالدنانير؛ بين الدرهمين صرف (sihah)؛ صرف الدراهم؛ الصرف الفضل (tahdhib)
- **B006** sözü eklemelerle süsleyip ilgi çekmek [kalıp] — konuşmayı ilavelerle süsleyip gönülleri ona çekmek · sözü süslemek veya sözler arasında üstünlük
  صرف الكلام تزيينه والزيادة فيه؛ صرف الأسماع إلى استماعه (maqayis)؛ من طلب صرف الحديث؛ صرف الحديث تزيينه بالزيادة فيه (sihah)؛ صرف الحديث أن يزيد فيه ليميل قلوب الناس إليه؛ صرف الكلام فضل بعض الكلام على بعض (tahdhib)
- **B007** zamanın olayları ve sıkıntılı dönüşleri — zamanın olayları ve felaketleri · zamanın felaketleri ve dönüşleri · gece ile gündüz; kaynaklarda başka anlamları da bulunan ikili ad
  حدث الدهر صرف والجمع صروف؛ يتصرف بالناس أي يقلبهم ويرددهم (maqayis)؛ صيرفيات الأمور متصرفاتها أي تتقلب بالناس؛ صرف الدهر حدثه (ayn)؛ صرف الدهر حدثانه ونوائبه؛ الصرفان الليل والنهار (sihah)؛ صرف الدهر حدثه (tahdhib)
- **B008** mevsim dönüşünü bildiren tek yıldızlık ay durağı — soğuğun çekilişiyle ilişkilendirilen tek yıldızlık ay durağı
  الصرفة نجم؛ سميت صرفة لانصراف البرد عند طلوعها (maqayis)؛ الصرفة كوكب واحد؛ أول الخريف؛ أول الربيع؛ الصرفة ناب الدهر (ayn)؛ الصرفة منزل من منازل القمر؛ سمي صرفة لانصراف البرد وإقبال الحر (sihah)؛ الصرفة كوكب واحد خلف خراتي الأسد؛ ناب الدهر (tahdhib)
- **B009** gönlü çevirdiğine inanılan boncuk — erkeğin gönlünü istediğinden çevirdiğine inanılan boncuk
  الصرفة خرزة يؤخذ بها الرجال؛ يصرفون بها القلب عن الذي يريده (maqayis)؛ الصرفة خرزة من الخرز الذي يذكر في الأخذ (sihah)
- **B010** dişi hayvanın çiftleşme isteği — dişi hayvanın çiftleşme isteği · çiftleşmek isteyen dişi köpek · erkek hayvanı kendine yönelten çiftleşme dönemindeki keçi
  الصراف حرمة الشاء والبقر والكلاب؛ تصرف أي تردد وتراجع فيه (maqayis)؛ الصراف حرمة الشاء والبقر والكلاب؛ كلبة صارف (ayn)؛ كلبة صارف إذا اشتهت الفحل؛ تصرف صروفا وصرافا (sihah)؛ السباع كلها تجعل وتصرف إذا اشتهت الفحل؛ حرمة الشاء والكلاب والبقر (tahdhib)؛ عنز صارف كأنها تصرف الفحل إلى نفسها (mufradat)
- **B011** sürtünme veya dönmeden çıkan gıcırtı — diş, makara veya kapının sürtünme ve dönme sesi
  الصريف صوت ناب البعير؛ يردده ويرجعه (maqayis)؛ الصريف صوت ناب البعير؛ الصريف صوت البكرة (ayn)؛ صريف البكرة؛ صريف الباب؛ صريف ناب البعير (sihah)؛ الصريف صوت الأنياب والأبواب (tahdhib)؛ تصريف الناب يقال لنا به صريف (mufradat)
- **B012** sağım evresindeki süt veya iyi şarap — yeni sağılmış sıcak veya köpüğü yatışmış süt; iyi şarap · iyi şarap; adı tazeliğe ya da bir yere bağlanan içki
  الصريف اللبن ساعة يحلب وينصرف به (maqayis)؛ الصريف اللبن الحليب ساعة يحلب؛ الصريف الخمر الطيبة؛ أخذت من الدن ساعتئذ كاللبن الصريف (ayn)؛ الصريف اللبن ينصرف به عن الضرع حارا إذا حلب؛ الصريفية من الخمر (sihah)؛ الصريف اللبن الذي ينصرف به عن الضرع حارا؛ الصريف الخمر الطيبة (tahdhib)؛ الصريف اللبن إذا سكنت رغوته (mufradat)
- **B013** katışıksız olan; saf içki veya saf kırmızı boya — su katılmamış, saf içki · saf kırmızı boya veya derinin koyu kırmızı rengi
  الصرف شيء من الصبغ يصبغ به الأديم؛ شرب الشراب صرفا إذا لم يمزجه (maqayis)؛ شراب صرف غير ممزوج؛ الصرف كل شيء لم يخلط بشيء؛ الصرف الأديم الشديد الحمرة (ayn)؛ الصرف صبغ أحمر؛ شراب صرف أي بحت غير ممزوج (sihah)؛ الصرف الخمر التي لم تمزج بالماء؛ كل شيء لا خلط فيه؛ الصرف شيء أحمر يدبغ به الأديم (tahdhib)؛ الصرف صبغ أحمر خالص؛ لكل خالص عن غيره صرف (mufradat)

## غ ل ل (root_001102): 40:71 ٱلْأَغْلَٰلُ

- **B001** bir şeyin içine girme veya sokup sabitleme — bir şeyi başka bir şeyin içine saplarcasına yerleştirmek · bir şeyin içine girip ortasına ulaşmak · içine sokulunca girmek · aralıklara işleyerek içeri girmek · hoş kokulu maddeyi cilde ve saç diplerine sürmek · mideye iyi gelen yiyecek veya içecek · koçun dişiye çiftleşmek üzere girmesi · hançer ya da mızrağı fark ettirmeden sokmak · zırha geçirilmiş perçinler · sözün insanlardan gizli kalmaması
  غللت الشيء في الشيء إذا أثبته فيه كأنه غرزته (maqayis)؛ غله فانغل أي أدخله فدخل (sihah)؛ غل أيضا دخل (sihah)؛ غل في الشيء وانغل وتغلغل فيه إذا دخل فيه (tahdhib)؛ تدرع الشيء وتوسطه (mufradat)؛ تغللت بالغالية وكل شيء ألصقته بجلدك وأصول شعرك (tahdhib)؛ نعم غلول الشيخ هذا يعني الطعام الذي يدخله جوفه (sihah;tahdhib)؛ نعم الغلول شراب شربته أو طعام إذا وافقني (tahdhib)؛ منها ما يغل يعني من الكباش أي يدخل قضيبه (jamhara;sihah)؛ غله له أي دسه له وهو لا يشعر به (tahdhib)؛ غلائل الدروع مساميرها المدخلة فيها (tahdhib)؛ لا يذهب كلامك غللا أي لا ينبغي أن ينطوي عن الناس (tahdhib)
- **B002** susuzluktan içi yanma — susuzluğun içte yakan harareti · susuzluk veya yoğun duygudan doğan iç harareti · susuzluğunu giderememiş çok susamış deve · içeceği özleyerek içmek
  الغلة والغليل العطش (maqayis)؛ الغليل حر الجوف لوحا وامتعاضا (ayn;tahdhib)؛ الغلة والغليل حرارة العطش (jamhara;sihah;tahdhib)؛ ربما سميت حرارة الحب أو الحزن غليلا (jamhara)؛ ما يتدرعه الإنسان في داخله من العطش ومن شدة الوجد والغيظ (mufradat)؛ غل البعير يغل غللا إذا لم يقض ريه (ayn;sihah;tahdhib)؛ اغتللت الشراب شربته وأنا مغتل إليه أي مشتاق إليه (tahdhib)
- **B003** ağaçlık yerdeki sığ su, çukur yer ve bitki adları — ağaçlar ve kökler arasında akan ya da az görünen su · ağaçlı çukur arazi veya gizli vadi · bir bitki adı · denizden ayrılıp kıyıda biriken su
  الغلل الماء الجاري بين الشجر (maqayis)؛ الماء الذي ليس له جرية وإنما يظهر على وجه الأرض ظهورا قليلا فيخفى مرة ويظهر مرة (sihah)؛ الماء الذي يجري في أصول الشجر (tahdhib)؛ الغلل للماء الجاري بين الشجر (mufradat)؛ الغلان الأودية الغامضة واحدها غال (maqayis)؛ الغال أرض مطمئنة ذات شجر (sihah;tahdhib)؛ الغال أيضا نبت والجمع غلان (sihah)؛ أغل الوادي إذا أنبت الغلان (sihah)؛ الغالة ماء ينقطع من ماء البحر فيجتمع في موضع من الساحل (jamhara)
- **B004** paylaştırılacak malı gizlice aşırma ve ihanet — paylaştırılacak maldan bir şeyi gizlice aşırma · paylaştırılacak maldan gizlice alarak ihanet etmek · ihanet; özellikle ortak malda hainlik · birini ortak maldan aşırmakla suçlamak · ihanet de hırsızlık da yok
  الغلول في الغنم وهو أن يخفى الشيء فلا يرد إلى القسم (maqayis)؛ غل يغل غلا إذا خان (jamhara)؛ غل من المغنم غلولا أي خان (sihah)؛ الغلول في المغنم خاصة (sihah;tahdhib)؛ الإغلال الخيانة في المغانم وغيرها (tahdhib)؛ الغلول تدرع الخيانة (mufradat)؛ أغللت فلانا نسبته إلى الغلول (mufradat)؛ لا إغلال ولا إسلال أي لا خيانة ولا سرقة (tahdhib;mufradat)
- **B005** içte beslenen gizli kin — içte beslenen kin, husumet veya kötü niyet · kin ve husumet · inananın kalbi kin tutmaz
  الغل وهو الضغن ينغل في الصدر (maqayis)؛ الغل الحقد (jamhara)؛ الغل بالكسر الغش والحقد أيضا (sihah)؛ الغليل الضغن والحقد مثل الغل (sihah)؛ الغل وهو الضغن والشحناء (tahdhib)؛ الغل العداوة (mufradat)؛ لا يغل أي لا يضطغن (mufradat)
- **B006** uzvu kuşatan pranga ve mecazi kısıtlama — boyun veya eli kuşatan demir ya da ham deri pranga · prangalar ve boyun bağları · elini boynuna bağlamak · eli bağlı; eli sıkı
  الغل المعروف من حديد أو قد (jamhara)؛ الغل بالضم واحد الأغلال (sihah)؛ في رقبته غل من حديد (sihah;tahdhib)؛ غللت يده إلى عنقه (sihah)؛ الغل مختص بما يقيد به فيجعل الأعضاء وسطه (mufradat)؛ ويضع عنهم إصرهم والأغلال التي كانت عليهم (tahdhib;mufradat)؛ ولا تجعل يدك مغلولة إلى عنقك (mufradat)
- **B007** giysi veya zırh altında giyilen içlik — giysi veya zırh altında ya da iki giysi arasında giyilen içlik · giysiyi diğer giysilerin altına giymek
  الغلالة شعار يلبس تحت الثوب وبطانة تلبس تحت الدرع (maqayis)؛ الغلالة شعار يلبس تحت الثوب وتحت الدرع أيضا (sihah)؛ الغلالة الثوب الذي يلبس تحت الثياب أو تحت الدرع (tahdhib)؛ الغلالة ما يلبس بين الثوبين (mufradat)؛ اغتللت الثوب أي لبسته تحت الثياب (tahdhib)؛ الغلة ما تواريت فيه (tahdhib)؛ الغلالة الثوب الذي تشده المرأة على عجيزتها (tahdhib)
- **B008** ibrik ağzına bağlanan süzgeç bezi — ibrik ağzına bağlanan bez, tıkaç veya süzgeç
  الغلة وهو الفدام يكون على رأس الإبريق والجمع غلل (maqayis)؛ الغلل المصفاة (sihah)؛ الغلة خرقة تشد على رأس الإبريق وجمعها غلل (tahdhib)
- **B009** hızlı seyir veya yerler arasında taşınan ileti — hızlı seyir · bir yerden başka yere taşınan ileti
  الغلغلة سرعة السير ورسالة مغلغلة محمولة من بلد إلى بلد (maqayis)؛ الغلغلة سرعة السير والمغلغلة الرسالة المحمولة من بلد إلى بلد (sihah)؛ الغلغلة سرعة السير ورسالة مغلغلة محمولة من بلد إلى بلد (tahdhib)؛ المغلغلة الرسالة التي تتغلغل بين القوم (mufradat)
- **B010** deveye verilen çekirdekli yem karışımı — deveye verilen, bitkisel yemle karıştırılmış hurma çekirdeği
  الغليل النوى يغل في القت يخلط به تعلفه الإبل (maqayis)؛ الغليل النوى يخلط بالقت تعلفه الناقة (sihah)
- **B011** taşınmazdan elde edilen ürün veya gelir — ev veya araziden elde edilen ürün ya da gelir · mülk ürün veya gelir vermek · ailesine ürün veya gelir getirmek · gelir getiren varlıkların gelirini tahsil etmek
  الغلة من غلة الدار وما أشبهها (jamhara)؛ أغلت الضياع من الغلة (sihah)؛ أغل القوم إذا بلغت غلتهم (sihah)؛ فلان يغل على عياله إذا أتاهم بالغلة (sihah;tahdhib)؛ الغلة ما يتناوله الإنسان من دخل أرضه (mufradat)؛ استغلال المستغلات أخذ غلتها (sihah)
- **B012** deriyi yüzerken üzerinde et veya yağ bırakmak [kalıp] — deriyi yüzerken üzerinde et veya yağ bırakmak · kasabın deride yapışık et bırakması
  أغللت في الإهاب غللا أي أبقيت عليه شحما بعد السلخ (ayn)؛ أغللت في الإهاب إذا سلخته وتركت فيه لحما (jamhara)؛ أغل الجازر في الإهاب إذا سلخ فترك من اللحم ملتزقا بالإهاب (sihah)؛ أغللت الجلد إذا سلخته فأبقيت فيه شيئا من الشحم (tahdhib)؛ أغل الجازر والسالخ إذا ترك في الإهاب من اللحم شيئا (mufradat)

## ع ن ق (root_001053): 40:71 أَعْنَٰقِهِمْ

- **B001** baş ile gövde arasındaki boyun ve boyuna bağlı nitelikler — boyun · boyunlar; bağlama göre başlar · uzun boyunlu · boynunda halka gibi beyazlık bulunan köpek · boynuna tasma ya da kordon takmak · boyun tasması
  العنق وهو وصلة ما بين الرأس والجسد؛ رجل أعنق أي طويل العنق؛ أعنقت الكلب إذا جعلت في عنقه قلادة أو وترا؛ المعنقة قلادة الكلب (maqayis)؛ العنق معروف يخفف ويثقل ويؤنث؛ الأعنق الطويل العنق؛ الأعنق الكلب الذي في عنقه بياض كالطوق (ayn)؛ العنق والعنق يذكر ويؤنث؛ الأعنق الطويل العنق؛ أعنقت الكلب أي جعلت في عنقه القلادة (sihah)؛ العنق مؤنثة؛ قيل أي رقابهم؛ المعنقة القلادة؛ لها أطواق في أعناقها ببياض (tahdhib)؛ العنق الجارحة وجمعه أعناق؛ فاضربوا فوق الأعناق أي رؤوسهم؛ رجل أعنق طويل العنق؛ كلب أعنق في عنقه بياض؛ أعنقته كذا جعلته في عنقه (mufradat)
- **B002** belirli yapılardaki boyun biçimli uzantı ya da yükselti [kalıp] — yüksek, çıkıntılı ve uzamış dağ ya da yer · uzun veya çıkıntılı tepe · çevresi düz olan uzun ve sert yükselti · rahmin daralan alt bölümü · işkembenin alt ya da kubbemsi bölümü · olgunlaşırken sap çevresinde halka kalan ham hurma · kum sıralarının önündeki küçük setler
  جبل أعنق مشرف؛ نجد أعنق وهضبة عنقاء؛ هضبة معنقة؛ المعنق الطويل؛ عنق الرحم ما استدق منها؛ عنق الكرش أسفلها؛ عنقت كوافير النخل إذا طالت؛ معانيق الرمال حبال صغار (maqayis)؛ المعنق من جلد الأرض ما صلب وارتفع وما حواليه سهل وهو منقاد في طول؛ مخرج أعناق الجبال من السراب (ayn)؛ رأس خلقاء من عنقاء مشرفة يصف جبلا (sihah)؛ مخرج أعناق الجبال من السراب؛ العنقاء أكمة فوق جبل مشرف؛ معانيق الرمال حبال صغار (tahdhib)
- **B003** bağlı topluluk veya bir bütünden ayrılan pay — birbirine bağlı topluluk · bölük bölük · iyilikten ya da işten bir pay · ateşten çıkan bir bölüm
  للجماعة عنق لأنه شيء يتصل بعضه ببعض؛ فظلت أعناقهم لها خاضعين أي جماعتهم (maqayis)؛ أعناقهم أي جماعاتهم؛ جاء القوم رسلا رسلا وعنقا عنقا إذا جاءوا فرقا (ayn)؛ هم عنق إليك أي مائلون إليك ومنتظروك (sihah)؛ الأعناق في هذه الآية إلى الجماعات؛ جاء القوم عنقا عنقا إذا جاءوا فرقا؛ كل جماعة منهم عنق؛ العنق الجمع الكثير من الناس؛ العنق القطعة من المال؛ العنق أيضا القطعة من العمل؛ لفلان عنق من الخير؛ يخرج عنق من النار؛ أعناقها جماعاتها؛ وقال غيره ساداتها (tahdhib)؛ قيل لأشراف القوم أعناق؛ فظلت أعناقهم لها خاضعين (mufradat)
- **B004** uzayıp hızlanan hayvan yürüyüşü ve ilerleme uzantıları — hayvanın uzayıp hızlanan yürüyüşü · bu özel yürüyüş biçimi · hayvan hafif ve hızlı yürüdü · bu yürüyüşte hızlı ve iyi hayvan · hızla ilerleyenler · uzak ülke ya da toprak · yıldız kümesi batmaya yöneldi
  العنق من سير الدواب والنعت معناق وعنيق؛ العنق المسبطر من السير؛ أعنق الفرس؛ المشي الخفيف؛ برذون معناق؛ المعناق من الإبل الخفيفة؛ المعنق السابق؛ أعنقت النجوم إذا تقدمت للمغيب (maqayis)؛ العنق من سير الدواب؛ والنعت معناق ومعنق وعنيق؛ سير عنيق؛ برذون عنق (ayn)؛ العنق ضرب من سير الدابة والإبل؛ سير مسبطر؛ وقد أعنق الفرس؛ فرس معناق أي جيد العنق (sihah)؛ المعنقة المتقدمات فيها؛ العنق والعنيق من السير؛ أعنقت الدابة؛ أعلقت في الأرض وأعنقت وبلاد معلقة ومعنقة أي بعيدة؛ أعنقت الثريا إذا غابت؛ أعنقت النجوم إذا تقدمت للمغيب؛ المعنق السابق؛ جاء الفرس معنقا؛ دابة معناق (tahdhib)
- **B005** doğa öğesinin kaynağından çıkıp uzayan kolu [kalıp] — uzayıp yükselen rüzgar kolları veya rüzgarın kaldırdığı toz · ırmaktan çıkıp akan su kolu · ana bulut kümesinden çıkan beyaz bulut
  يقال لما سطع من الرياح أعناق الرياح؛ أعنقت الريح بالتراب (maqayis)؛ إذا خرج من النهر ماء فجرى فقد خرج عنق؛ عنقت السحابة إذا خرجت من معظم الغيم؛ يوم غيم عنقت فيه الصبر (tahdhib)
- **B006** boyun çevresinden sarılma, boğuşma veya bir işe bağlanma — sarılma · ona sarıldı · savaşta birbirine sarılıp boğuşmak · işi üstlenmek
  الاعتناق من المعانقة أيضا غير أن المعانقة في المودة والاعتناق في الحرب ونحوها؛ اعتنقوا في الحرب؛ عانق فلان فلانا (maqayis)؛ الاعتناق من المعانقة؛ المعانقة في حال المودة والاعتناق في الحرب ونحوها؛ اعتنقوا في الحرب (ayn)؛ العناق المعانقة؛ عانقه إذا جعل يديه على عنقه وضمه إلى نفسه؛ تعانقا واعتنقا (sihah)؛ عانق الرجل جاريته؛ تعانقا؛ الاعتناق فأكثر ما يستعمل في الحرب؛ وقد يجوز الاعتناق في غير الحرب بمعنى التعانق (tahdhib)؛ استعير اعتنق الأمر (mufradat)
- **B007** hayvanın boynunu çamurdan çıkarma veya oyuğa sokma — hayvan çamurdan boynunu çıkardı · tavşan boynunu oyuğa soktu; bir aktarıma göre boynunu kaldırdı · tavşanın ya da çöl faresinin boynuna dek girdiği gevşek topraklı oyuk
  اعتنقت الدابة في الوحل إذا أخرجت عنقها؛ تعنق الأرنب في العانقاء؛ جحر مملوء ترابا رخوا؛ يدس رأسه وعنقه فيه؛ العانقاء تراب لغيزى اليربوع وتراب مجراه (maqayis)؛ اعتنقت الدابة إذا وقعت في الوحل فأخرجت أعناقها؛ تعنقت الأرنب في العانقاء؛ جحر مملوء ترابا رخوا؛ تعنق اليربوع لأنه يدس عنقه فيه (ayn)؛ العانقاء جحر من جحرة اليربوع يملؤه ترابا؛ فإذا خاف اندس فيه إلى عنقه فيقال تعنق (tahdhib)؛ تعنق الأرنب رفع عنقه (mufradat)
- **B008** efsanevi büyük kuş ve onunla anlatılan bulunmaz oluş — varlığı belirsiz, efsanevi büyük kuş · ortadan kaybolup bulunmaz oldu
  العنقاء فيما يقال طائر لم يبق إلا اسمه؛ سميت عنقاء لبياض كان في عنقها؛ في المثل لما لا يوجد طارت به العنقاء (maqayis)؛ العنقاء طائر لم يبق في أيدي الناس من صفتها غير اسمها؛ سميت به لبياض في عنقها كالطوق (ayn)؛ أصل العنقاء طائر عظيم معروف الاسم مجهول الجسم؛ حلقت به عنقاء مغرب وطارت به العنقاء (sihah)؛ العنقاء المغرب؛ طائر لم يره أحد؛ طائر لم يبق في أيدي الناس من صفتها غير اسمها؛ ألوى به العنقاء المغرب (tahdhib)؛ عنقاء مغرب قيل هو طائر متوهم لا وجود له في العالم (mufradat)
- **B009** dehşetli felaket ve onu büyüten kalıp anlatımlar — korkunç felaket · ağır felaket; bağlama göre yüzsüzce büyük yalan · dehşetli felaket
  العنقاء فيقال هي الداهية وسميت بذلك تقبيحا وتهويلا؛ العناق الداهية؛ لاقين منه أذنى عناق (maqayis)؛ عنقفير الداهية؛ هول أيضا بالزيادة؛ يقولون للداهية عنقاء ثم يزيدون هذه الزيادات (maqayis)؛ العنقاء الداهية (ayn)؛ العناق الداهية؛ لقي منه أذني عناق أي داهية وأمرا شديدا؛ العنقاء الداهية (sihah)؛ العنقاء من أسماء الداهية؛ لقيت منه أذني عناق أي داهية وأمرا شديدا؛ جاء فلان بأذني عناق أي جاء بالكذب الفاحش (tahdhib)
- **B010** yaş sınırı değişken dişi keçi veya küçükbaş yavrusu — dişi oğlak; bazı aktarımlarda dişi küçükbaş yavrusu · yüksek konumdan aşağı konuma düşmek · dişi yavru doğuran koyun
  العناق الأنثى من أولاد المعز والجمع عنوق؛ العنوق بعد النوق؛ العناق من حين تلقيها أمها حتى تجذع؛ الأنثى من أولاد الغنم ما بين أن تولد إلى أن يأتي عليها الحول؛ شاة معناق إذا كانت تلد العنوق (maqayis)؛ العناق الأنثى من أولاد المعز ويجمع العنوق؛ العنوق بعد النوق (ayn)؛ العناق الأنثى من ولد المعز والجمع أعنق وعنوق (sihah)؛ العناق الأنثى من أولاد المعزى إذا أتت عليها السنة وجمعها عنوق؛ ثلاث أعنق وأربع أعنق؛ هذه العنوق بعد النوق (tahdhib)؛ العناق الأنثى من المعز (mufradat)
- **B011** küçük etçil kara hayvanı veya boynu halkalı küçük kemirgen — leopardan küçük veya ona benzer etçil kara hayvanı · boynunda beyaz halkalar bulunan küçük kemirgenler
  عناق الأرض شيء أصغر من الفهد (maqayis)؛ عناق الأرض حيوان أسود الرأس طويل الظهر أصغر من الفهد ويجمع على عنوق (ayn)؛ العناق أيضا شيء من دواب الأرض كالفهد (sihah)؛ عناق الأرض دابة فويق الكلب الصيني يصيد كما يصيد الفهد ويأكل اللحم؛ جمعه عنوق؛ المعنقة دويبة؛ المعانق هي مقرضات الأساقي لها أطواق في أعناقها ببياض (tahdhib)
- **B012** başarısız olup eli boş dönme — başarısızlık veya eli boş dönüş · eli boş döndünüz
  قولهم للخيبة عناق فليس بأصل؛ كنوا عن الخيبة بالعناق؛ ربما قالوا العناقة بالهاء؛ أبتم بالعناق (maqayis)؛ العناق الخيبة؛ أبتم بالعناق (sihah)؛ رجع فلان بالعناق إذا رجع خائبا؛ يوضع العناق موضع الخيبة؛ أبتم بالعناق (tahdhib)
- **B013** kişi, hayvan, topluluk ve yere verilmiş özel adlar — haberlerde kişi, at ya da varlıklı yönetici için kullanılan ad · kişi, hükümdar veya topluluk adı ya da lakabı · belirli bir vadinin adı
  الأعنق رجل من العرب وهو قيس بن الحارث؛ بنو الأعنق؛ بنو العنقاء؛ العنقاء ثعلبة ابن عمرو بن مالك من خزاعة (maqayis)؛ العنقاء اسم ملك (ayn)؛ العنقاء لقب رجل من العرب واسمه ثعلبة بن عمرو (sihah)؛ الأعنق فحل من خيل العرب معروف؛ اختلفوا في أعنق فقال قائل هو اسم فرس وقال آخرون هو دهقان كثير المال؛ وادي العناق بالحمى في أرض غني (tahdhib)
- **B014** çok eski zamanlarda [kalıp] — eski çağlarda
  كان ذلك على عنق الدهر أي على قديم الدهر (tahdhib)

## س ل س ل (root_000731): 40:71 وَٱلسَّلَٰسِلُ

- **B001** boğazdan kolay geçen tatlı, duru, serin ve hızlı akan su — suyun boğazdan ya da eğimli bir yerde kolayca akması · onu boğaza döktü · tatlı ve duru olduğu için boğazdan kolay geçen su · tatlı ve duru olduğu için kolay içilen su ya da içecek · boğazdan kolay geçen, bazen serin diye nitelenen su · kolay içilen, lezzetli ve hızlı akan su; hızlı akan pınar
  تسلسل الماء في الحلق جرى (sihah)؛ ماء سلسل وسلسال سهل الدخول في الحلق لعذوبته وصفائه (sihah)؛ السلاسل الماء السهل في الحلق ويقال هو البارد (tahdhib)؛ السلسل الماء العذب الصافي الذي إذا شرب تسلسل في الحلق (tahdhib)؛ ماء سلسل متردد في مقره حتى صفا (mufradat)؛ سلسبيلا سهلا لذيذا سلسا حديد الجرية (mufradat)
- **B002** birbirine bağlı halkalar veya parçalardan oluşan zincir — zincir; birbirine bağlı halkalar ya da parçalar dizisi · birbirine bağlı zincirler ya da bağlar · parçaları birbirine bağlı, zincirleme
  شيء مسلسل متصل بعضه ببعض ومنه سلسلة الحديد (sihah)؛ السلسلة معروفة (tahdhib)؛ ومنه السلسلة (mufradat)
- **B003** bulutta uzanan şimşek kolu veya kıvrımlı bağlı kum sırtları [kalıp] — bulut boyunca uzanan ve art arda parlayan şimşek kolu · birbirine bağlanıp kıvrılarak uzanan kum sırtları
  سلسلة البرق وما استطال منه في عرض السحاب (sihah)؛ السلاسل رمل ينعقد بعضه على بعض وينقاد (sihah)؛ برق ذو سلاسل ورمل ذو سلاسل وهو تسلسله الذي يرى في التوائه (tahdhib)
- **B004** art arda salınıp kararsız biçimde hareket etme — art arda sallanıp kararsız biçimde hareket etmek · kılıç yüzeyinde yürür gibi ilerleyen parıltı
  تسلسل الشيء اضطرب كأنه تصور منه تسلل متردد (mufradat)؛ تردد لفظه تنبيها على تردد معناه (mufradat)؛ التسلسل بريق فرند السيف ودبيبه (tahdhib)

## س ح ب (root_000680): 40:71 يُسْحَبُونَ

- **B001** çekip sürüklemek — çekmek, uzatmak veya sürüklemek · çekilerek ilerleyen veya uzanan
  أصل صحيح يدل على جر شيء مبسوط ومده (maqayis)؛ السحب جرك الشيء (ayn;tahdhib)؛ سحبت الشيء إذا جررته وكل منجر منسحب (jamhara)؛ سحبت ذيلي جررته فانجر (sihah)؛ أصل السحب الجر كسحب الذيل والإنسان على الوجه (mufradat)
- **B002** bulut; benzetmeyle gölge veya karanlık — bulut · benzetme yoluyla gölge veya karanlık
  سمي السحاب سحابا تشبيها له بذلك كأنه ينسحب في الهواء (maqayis)؛ سمي السحاب لانسحابه في الهواء (ayn)؛ منه اشتقاق السحاب لانسحابه في الهواء (jamhara)؛ السحابة الغيم والجمع سحاب وسحب وسحائب (sihah)؛ سمي السحاب سحابا لانسحابه في الهواء (tahdhib)؛ السحاب الغيم فيها ماء أو لم يكن وقد يذكر لفظه ويراد به الظل والظلمة على طريق التشبيه (mufradat)
- **B003** birine karşı cüretkâr ve teklifsiz davranmak — birine karşı cüret etmek, teklifsiz davranmak veya nazlanmak
  تسحب فلان على فلان إذا اجترأ عليه كأنه امتد عليه امتدادا (maqayis)؛ تسحب عليه أي أدل (sihah)؛ فلان يتسحب علينا أي يتدلل (tahdhib)؛ فلان يتسحب على فلان إذا تجرأ عليه (mufradat)
- **B004** şiddetle yiyip içme — 
  السحب شدة الأكل والشرب رجل أسحوب أكول شروب ورجل متسحب حريص على أكل ما يوضع بين يديه (ayn)؛ السحب شدة الأكل والشرب ورجل أسحوب أي أكول شروب (sihah)؛ السحب شدة الأكل والشرب ورجل أسحوب أكول شروب (tahdhib)؛ ناس يقولون السحب شدة الأكل وأظنه تصحيفا (maqayis)
- **B005** bütün gün boyunca [kalıp] — bütün gün boyunca
  ما زلت أفعل ذلك سحابة يومي أي طول يومي (jamhara)
- **B006** silip süpüren kişi ve örnek söz ustası — önüne gelen her şeyi silip süpüren adam · hitabeti, açık anlatımı ve söz ustalığıyla örnek gösterilen kişi · örnek gösterilen kişiden daha güçlü hatip · örnek gösterilen kişiden daha güzel ve açık konuşan
  سحبان اسم الذي يضرب به المثل فيقال أخطب من سحبان وائل (jamhara)؛ سحبان اسم رجل من وائل كان لسنا بليغا يضرب به المثل في البيان (sihah)؛ رجل سحبان أي جراف يجرف كل ما مر به وبه سمي سحبان وائل الذي يضرب به المثل في الفصاحة (tahdhib)
- **B007** gölette kalan az miktarda su — gölette kalan su artığı · çok az kalmış su
  السحبة فضلة ماء تبقى في الغدير ما بقي في الغدير إلا سحيبة ماء أي مويهة قليلة (tahdhib)

## س ج ر (root_000676): 40:72 يُسْجَرُونَ

- **B001** doldurma; suyu dökme veya fışkırtma — bir şeyi başka bir şeyle doldurmak · nehri, sığ su çukurlarını veya kabı doldurmak · selin kuyuları ve su birikintilerini doldurması · selin gelip doldurduğu yer · suyu sütünden fazla olan süt · suyu bol inci · boğaza su dökmek · suyu istenen yönden fışkırtmak
  البحر المسجور أي المملوء (maqayis); السجور امتلاء البحر والعين وكثرة مائه (ayn); كل شيء ملأته من شيء فقد سجرته به (jamhara); سجرت النهر ملأته (sihah); المسجور في كلام العرب المملوء (tahdhib); المسجور اللبن الذي ماؤه أكثر من لبنه (sihah;tahdhib); لؤلؤة مسجورة إذا كانت كثيرة الماء (tahdhib); سجرت الماء في حلقه صببته (tahdhib); سجر هذا الماء أي فجره حيث تريد (tahdhib)
- **B002** suyun çekilip tükenmesi — 
  وإذا البحار سجرت أي غيضت (ayn); زعم قوم أنه الفارغ (jamhara); إذا البحار سجرت أي خلت من الماء (jamhara); المسجور يكون المملوء ويكون الذي ليس فيه شيء (tahdhib); وقيل غيضت مياهها (mufradat)
- **B003** yakın dost — yakın dost, içten arkadaş
  السجير الصاحب والخليط (maqayis); السجير خليل الرجل وصفية (ayn); السجير الخليل المصافي (jamhara); سجیر الرجل صفيه وخليله (sihah); السجير الصديق (tahdhib); السجير الخليل الذي يسجر في مودة خليله (mufradat)
- **B004** göz akına veya renge karışan kızıllık — akı kızıllıkla karışmış göz · gözdeki kızıllık veya bulanık renk · gölette, suda veya hayvanda görülen kızılımsı ya da bulanık renk
  عين سجراء إذا خالط بياضها حمرة (maqayis); السجرة والسجر حمرة في بياض العين (ayn); عين سجراء إذا علت بياضها حمرة (jamhara); عين سجراء بينة السجر إذا خالط بياضها حمرة (sihah); السجر والسجرة حمرة في العين في بياضها (tahdhib); ويقال للأسد أسجر إما لحمرة عينه وإما للونه (jamhara)
- **B005** ateş yakıp harlandırma — fırını yakıtla yakıp ısıtmak · fırın yakıtı, odun · fırındaki yakıtı karıştırma tahtası
  سجرت التنور إذا أوقدته (maqayis); سجرت التنور أسجره سجرا والسجور اسم للحطب (ayn); سجرت التنور وغيره إذا ملأته حطبا ونارا (jamhara); سجرت التنور أسجره سجرا إذا أحميته (sihah); السجر إيقادك في التنور (tahdhib); السجر تهييج النار (mufradat); ثم في النار يسجرون (mufradat)
- **B006** saçın uzanması; incinin dizilmesi veya saçılması [kalıp] — gür ve serbestçe uzanan saç · dizi halinde uzanan veya dizisinden saçılmış inci
  الشعر المنسجر وهو الذي يفر حتى يسترسل من كثرته (maqayis); اللؤلؤ المسجور المنظوم المسترسل (sihah); شعر منسجر وهو المسترسل (sihah); المسجر الشعر المرسل (tahdhib); لؤلؤ مسجور إذا انتثر من نظامه (tahdhib)
- **B007** devenin yavrusu ardından uzun ve güçlü inlemesi [kalıp] — devenin yavrusu ardından güçlü ve uzun inlemesi
  سجرت الناقة إذا حنت حنينا شديدا (maqayis); سجرت الناقة تسجر سجرا إذا مدت حنينها (jamhara); سجرت الناقة تسجر سجرا وسجورا إذا مدت حنينها (sihah); إذا حنت الناقة فطربت في إثر ولدها قيل سجرت (tahdhib)
- **B008** develerin güçlü, peş peşe veya özel bir yürüyüşle ilerlemesi — develerin yürüyüşte güçlü biçimde ilerlemesi · iki deve yürüyüşü arasındaki özel gidiş · develerin yürüyüşte peş peşe gitmesi
  استجرت الإبل على نجائها إذا جدت كأنها تتقد في سيرها اتقادا (maqayis); السجر أيضا ضرب من سير الإبل بين الخبب والهملجة (jamhara); انسجرت الإبل في السير تتابعت (sihah); سجرت الناقة استعارة لالتهابها في العدو (mufradat)
- **B009** boyunduruk veya prangayla bağlama — köpeğin boynuna geçirilen tahta boyunduruk · boynunda tahta boyunduruk bulunan köpek · bağlanmış ve prangaya vurulmuş
  الساجور خشبة تجعل في عنق الكلب (sihah); كلب مسجور في عنقه ساجور (tahdhib); مسمعا مسوجرا أي مقيدا مغلولا (tahdhib)

## ف ر ح (root_001140): 40:75 تَفْرَحُونَ, 40:83 فَرِحُوا۟

- **B001** iç açan sevinç — sevinç; üzüntünün karşıtı olan iç açıcı duygu · sevindi; içi açıldı · bir şeyden ötürü sevinmek · sevinçli · çok sevinçli · sevinen; sevinçli · sevinme; sevinç · sık sık ve çok sevinen kimse · onu sevindirdi; onda sevinç doğurdu · kişiyi sevindiren şey · kendisine ya da olmasına sevinilen şey · sevindirme; kullanıldığı yere göre ağırlaştırma anlamı da taşıyabilir
  خلاف الحزن (maqayis;jamhara)؛ فرح به سر (sihah)؛ الفرح انشراح الصدر بلذة عاجلة (mufradat)؛ الفرحة المسرة (jamhara)؛ رجل فرح وفرحان وامرأة فرحة وفرحى (ayn;jamhara;tahdhib)؛ المفراح الكثير الفرح (sihah;mufradat)؛ ما يسرني به مفرح ومفروح به (ayn;sihah;tahdhib;mufradat)
- **B002** kınanan taşkın sevinç — haksız ve ölçüsüz, kınanan taşkın sevinç
  والفرح أيضا البطر (sihah)؛ تفرحون في الأرض بغير الحق (maqayis;mufradat)؛ أكثر ما يكون ذلك في اللذات البدنية الدنيوية (mufradat)
- **B003** yük altında bırakıp ağırlaştırma — ağırlaştırma; yük altında bırakma · borç yükü altında ezilmiş, ödeme gücü kalmamış kimse · borç onu ağırlaştırdı ve ödeme sıkıntısına soktu · korunmak üzere bırakılan şeyler sana ağır bir yük oldu · o şey beni ezdi ve ağır bir yük altında bıraktı · ağırlaştırma; kullanıldığı yere göre sevindirme anlamı da taşıyabilir
  الإفراح وهو الإثقال (maqayis)؛ رجل مفرح أثقله الدين (ayn;jamhara;sihah;tahdhib;mufradat)؛ أفرحه الدين أثقله (sihah;tahdhib)؛ أفرحتك الودائع (maqayis;ayn;sihah;tahdhib)؛ المفرح المفدوح (sihah;mufradat)؛ أفرحني الشيء مثل فدحني (jamhara)

## م ر ح (root_001412): 40:75 تَمْرَحُونَ

- **B001** ölçüyü aşan, yerinde durdurmayan sevinç ve canlılık — ölçüyü aşan şiddetli sevinç, canlılık ve yerinde duramama · taşkın sevinç ve canlılık durumu · canlı, hareketli ve yerinde durmaz hayvan · canlı ve hareketli; hayvan, atak yay veya başta coşkunluk uyandıran etki için kullanılan niteleme · otlak onu canlandırıp hareketlendirdi
  أصل يدل على مسرة لا يكاد يستقر معها طربا (maqayis)؛ المرح شدة الفرح حتى يجاوز قدره (ayn;tahdhib)؛ المرح النشاط (jamhara)؛ المرح شدة الفرح والنشاط (sihah)؛ المرح شدة الفرح والتوسع فيه (mufradat)؛ فرس ممراح ومروح وناقة ممراح مروح (ayn;tahdhib)؛ فرس ممراح ومروح أي نشيط (sihah)؛ ناقة بينة المرح أي النشاط (jamhara)؛ قوس مروح كأن بها مرحا من حسن إرسالها السهم (maqayis;sihah)؛ لها مراح في الرأس وسورة يمرح من يشربها (sihah)
- **B002** Ne güzel, başardın! — Ne güzel, vurdun!
  مرحى كلمة تعجب وإعجاب يقال للرامي إذا أصاب (maqayis)؛ مرحى كلمة تقولها العرب عند الإصابة (ayn)؛ للرامي إذا أصاب مرحى فإن أخطأوا قالوا برحى (jamhara)؛ للرامي إذا أصاب مرحى وهو تعجب (sihah)؛ إذا رمى الرجل فأصاب قيل مرحى له وهو تعجب (tahdhib)؛ مرحى كلمة تعجب (mufradat)
- **B003** yeni tulumu suyla alıştırma veya kokulu otlarla hazırlama — yeni tulumu suyla doldurup dikişlerini alıştırma veya kokulu otlarla hazırlama · dikişlerini ıslatmak ve sızıntısını denetlemek ya da kapatmak için tulumu suyla doldurdu · tulumun dikiş delikleri kapandı ve su sızmaz oldu
  مرحت المزادة ملأتها لتتسرب وتسيل (maqayis)؛ التمريح أن تملأ المزادة أول ما تخرز حتى تكتم خروزها (ayn)؛ مرحت القربة أي سربتها وهو أن تملأها ماء لتنسد عيون الخرز (sihah)؛ التمريح أن تأخذ المزادة أول ما تخرز فتملأها ماء حتى تنتفخ خروزها (tahdhib)؛ التمريح تطييب القربة الجديدة بإذخر أو شيح (tahdhib)؛ ذهب مرح المزادة إذا انسدت عيونها فلم يسل منها شيء (tahdhib)
- **B004** gözün rahatsızlanıp bol bol yaşarması [kalıp] — göz rahatsızlanıp kabardı ve şiddetle yaşardı · çok yaşaran veya kolay ağlayan göz
  مرحت العين مرحانا (maqayis)؛ مرحت العين مرحانا اشتد سيلانها (ayn)؛ مرحت عينه مرحانا فسدت وهاجت (sihah)؛ عين ممراح غزيرة الدمع (sihah)؛ المرح خروج الدمع إذا كثر (tahdhib)؛ عين ممراح سريعة البكاء (tahdhib)
- **B005** deriye yağ sürmek [kalıp] — deriyi yağla veya yağ sürerek işle
  ويقال مرح جلدك أي ادهنه؛ مدبوغة لم تمرح (ayn)
- **B006** yağmurla hızla yeşeren toprak veya ilk başağını çıkaran ekin [kalıp] — yağmur alınca hızla yeşeren veya bir yılın ardından bitkisini canlandıran toprak · ekin ilk başaklarını çıkardı
  أرض ممراح إذا كانت سريعة النبات حين يصيبها المطر؛ الممراح من الأرض التي حالت سنة فهي تمرح بنباتها؛ أمرح الزرع إمراحا ومرح مرحا إذا أفرخ سنابله أول ما يخرجه (tahdhib)

## ب و ب (root_000163): 40:76 أَبْوَٰبَ

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

## خ ل د (root_000429): 40:76 خَٰلِدِينَ

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

## ث و ي (root_000211): 40:76 مَثْوَى

- **B001** bir yere yerleşip uzun süre kalma — bir yerde yerleşip kalmak · yerleşip uzun süre kalma · bir yerde kalıp yaşayan kişi · bir yerde yerleşip kalmak · öldürülüp yerde kalmış olmak · iki kutsal bölgede komşu olarak yaşama · savaşta dayanıklı olan ya da kapatılıp tutulan kişi · yerleşip kalma
  ثوى يثوي ثويا إذا أقام بالمكان والاسم الثواء (jamhara)؛ ثوى بالمكان أقام به وثويت البصرة وأثويت بالمكان لغة في ثويت (sihah)؛ الثواء طول المقام ويقال للمقتول قد ثوى والغريب إذا أقام ببلدة فهو ثاو والثوي المجاورة في الحرمين والثوي الصبور في المغازي المحجر وهو المحبوس (tahdhib)؛ الثواء الإقامة مع الاستقرار (mufradat)؛ كلمة واحدة صحيحة تدل على الإقامة ويقال ثوى يثوي فهو ثاو ويقال أثوى أيضا (maqayis)
- **B002** kalınan yer ve konuk ağırlama düzeni — kalınan yer; ev · kalınan yerler; evler · birini yanına yerleştirip ağırlamak · birini kalması için yerleştirmek · konuğu ağırlayan erkek ev sahibi · konuğu ağırlayan kadın ev sahibi · kimin evine konuk oldun? · konuk · ev içindeki ayrı bölüm; konuğa ayrılmış yer · bir yer adı
  المثوى الموضع الذي يثوي فيه الرجل وأم مثوى الرجل صاحبة منزله والثوية اسم موضع (jamhara)؛ الثوى الضيف وأبو مثوى الرجل صاحب منزله والثوية اسم موضع (sihah)؛ المثوى الموضع الذي يقام به ويقال أنزلني فلان وأثواني ثواء حسنا ورب البيت أبو مثواه وربة البيت أم مثواه والثوي بيت في جوف بيت والبيت المهيأ للضيف والثوي الضيف نفسه ومثوى الرجل منزله (tahdhib)؛ من أم مثواك كناية عمن نزل به ضيف (mufradat)؛ الثوية مكان وأم مثوى الرجل صاحبة منزله (maqayis)
- **B003** sürü barınağı, çoban gölgeliği veya taş dönüş imi — koyun barınağı · koyun ya da deve barınağı; çobanın dallardan yaptığı gölgelik · çobanın gece dönüşü için yükselttiği taş imi
  الثاية ظلة يتخذها الراعي من أغصان الشجر (jamhara)؛ الثوية مأوى الغنم وكذلك الثاية والثاية أيضا حجارة ترفع فتكون علما بالليل للراعي إذا رجع (sihah)؛ الثوية مأوى الغنم (mufradat)؛ الثوية والثاية مأوى الغنم والثاية أيضا حجارة ترفع للراعي يرجع إليها ليلا تكون علما له (maqayis)
- **B004** çalkalama kabı altlığı ve ev eşyası — süt tulumunu çalkalarken altına serilen koruyucu bez · ev eşyası
  الثَّوَة مثل الصوة خرقة تطرح تحت الوطب إذا مخض تقيه عن الأرض (jamhara)؛ الثوى قماش البيت واحدتها ثَوَة والخرقة التي تبل ويجعل عليها السقاء إذا مخض لئلا ينقطع الثَّوَة (tahdhib)

## ر ج ع (root_000544): 40:77 يُرْجَعُونَ

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

## ق ص ص (root_001232): 40:78 قَصَصْنَا, 40:78 نَقْصُصْ

- **B001** izi adım adım sürme — izini sürmek · izini adım adım takip etmek · izini işaret işaret izlemek · iz boyunca geri gitmek · onun izini takip et
  أصل صحيح يدل على تتبع الشيء؛ اقتصصت الأثر إذا تتبعته (maqayis)؛ اقتفاء الأثر قصص؛ فارتدا على آثارهما قصصا (jamhara)؛ قص أثره أي تتبعه؛ اقتص أثره وتقصص أثره (sihah)؛ قصيه أي اتبعي أثره؛ أصل القص اتباع الأثر (tahdhib)؛ القص تتبع الأثر؛ القصص الأثر (mufradat)
- **B002** olayları sırasıyla anlatma — sözü olay sırasıyla anlatmak · anlatıyı aslına uygun aktarmak · ona haberi anlatmak · öykü veya anlatılan olay · birbirini izleyen anlatılar · yazılı öyküler
  القصة والقصص كل ذلك يتتبع فيذكر (maqayis)؛ قص الحديث يقصه قصصا؛ القصة من القصص معروفة (jamhara)؛ القصة الأمر والحديث؛ اقتصصت الحديث رويته على وجهه؛ قص عليه الخبر (sihah)؛ القص فعل القاص إذا قص القصص؛ القاص لاتباعه خبرا بعد خبر (tahdhib)؛ القصص الأخبار المتتبعة؛ قص عليه القصص (mufradat)
- **B003** zarara denk karşılık verme — işlenene denk karşılık verme · yönetici, zarar görenin failden denk karşılık almasını sağladı · kendisi için denk karşılık uygulanmasını istedi · karşılıklı hak ve hesaplarını denkleştirdiler
  القصاص في الجراح؛ يفعل به مثل فعله بالأول (maqayis)؛ القصاص القود؛ جرحه مثل جرحه أو قتله قودا؛ تقاص القوم في حساب أو غيره (sihah)؛ القصاص والتقاص في الجراحات والحقوق شيء بشيء (tahdhib)؛ القصاص تتبع الدم بالقود؛ الجروح قصاص (mufradat)
- **B004** kesip eşitleme — saçını kesip eşitledi · tırnağını kesti · makas · kanadı kesilmiş
  قصصت الشعر؛ سويت بين كل شعرة وأختها (maqayis)؛ قص الشيء بالمقصين يقصه قصا (jamhara)؛ قصصت الشعر قطعته؛ طائر مقصوص الجناح؛ المقص المقراض (sihah)؛ القص أخذ الشعر بالمقص؛ أصل القص القطع؛ قصصت ما بينهما أي قطعت؛ المقص ما قصصت به (tahdhib)؛ قصصت ظفره (mufradat)
- **B005** göğüs orta kemiği — göğüs kemiğinin orta bölümü veya üst başı · hayvanın göğüs kemiği ya da göğüste kıl çıkan yer
  الصدر فهو القص؛ متساوي العظام (maqayis)؛ القص عظم الصدر من الناس وغيرهم وهو القصص (jamhara)؛ القص رأس الصدر؛ القصص للشاة وغيرها (sihah)؛ القص هو المشاش في وسط الصدر؛ قصص زوره وهو منبت شعره على صدره (tahdhib)
- **B006** ön saç tutamı ve saç çizgisi — perçem veya ön saç tutamı · saçın ön ve arka bitiş çizgisi · saç çizgisinin çevresi
  قصاص الشعر نهاية منبته؛ القصة الناصية (maqayis)؛ القصة الخصلة من الشعر؛ ناصية الفرس قصة (jamhara)؛ قصاص الشعر حيث تنتهي نبتته؛ القصة بالضم شعر الناصية (sihah)؛ القصة تتخذها المرأة في مقدم رأسها؛ قصاصة الشعر نهاية منبته؛ قصاص شعره حيث ينتهي (tahdhib)
- **B007** alçı, alçıyla sıvama ve alçı gibi beyazlık — alçı veya alçı beyazlığı · alçıyla sıvanmış ev · evini alçıyla sıvadı · mezarları alçıyla sıvama · aybaşı bitiminde görülen katışıksız beyazlık
  القصة الجص؛ بيت مقصص أي مجصص؛ بيضاء مثل القصة (jamhara)؛ القصة الجص؛ قصص داره أي جصصها؛ القصة البيضاء (sihah)؛ التقصيص هو التجصيص؛ القصة البيضاء؛ كأنها قصة لا يخالطها صفرة (tahdhib)؛ القص الجص؛ تقصيص القبور (mufradat)
- **B008** gebeliği belli olma — koyun veya kısrağın gebeliği belli oldu · gebeliği belli olmuş koyun veya kısrak
  أقصت الشاة استبان حملها (maqayis)؛ أقصت الشاة والفرس استبان حملهما (sihah)؛ أقصت الفرس إذا حملت؛ استبان حملها (tahdhib)
- **B009** yer mantarı yanı bitkisi veya otlakta kalan ot — yer mantarı kökleri yanında çıkan ya da otlaktan kalan bitki · yer mantarının yanında çıkan bitki · toprak bu bitkiyi çıkardı
  القصيص نبت (maqayis)؛ القصيصة نبت يخرج إلى جانبه الكمأة؛ الجمع قصيص (sihah)؛ القصيص نبت ينبت في أصول الكمأة؛ القصيصة نبت يخرج إلى جانب الكمأة (tahdhib)؛ ما يبقى من الكلإ فيتتبع أثره قصيص (mufradat)
- **B010** ölümün eşiğine gelme [kalıp] — onu ölümün eşiğine getirdi · ölüm ona çok yaklaştı · ölümün eşiğinden döndü
  ضرب فلان فلانا فأقصه أي أدناه من الموت؛ يقص أثر المنية (maqayis)؛ ضربه حتى أقصه من الموت؛ قصه الموت وأقصه بمعنى (sihah)؛ أدناه من الموت حتى أشرف عليه؛ أقصته شعوب إذا أشرف عليها ثم نجا (tahdhib)؛ ضربه ضربا فأقصه أي أدناه من الموت (mufradat)
- **B011** zayıf yük devesi veya kervan izini süren deve [kalıp] — yiyecek ve eşya taşıyan zayıf yük devesi · kervanın izini süren deve
  القصيصية من الإبل البعير يقص أثر الركاب (maqayis)؛ القصيصة من الإبل الزاملة يحمل عليها الطعام والمتاع لضعفها (sihah)؛ الزاملة الضعيفة قصيصة (tahdhib)

## ء ذ ن (root_000022): 40:78 بِإِذْنِ

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

## خ س ر (root_000409): 40:78 وَخَسِرَ, 40:85 وَخَسِرَ

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

## ن ع م (root_001525): 40:79 ٱلْأَنْعَٰمَ

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

## ر ك ب (root_000589): 40:79 لِتَرْكَبُوا۟

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

## ء ك ل (root_000043): 40:79 تَأْكُلُونَ

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

## ح و ج (root_000367): 40:80 حَاجَةً

- **B001** bir şeye zorunlu olarak gereksinim duyma veya ondan yoksun olma — gereksinim, yoksunluk · gereksinim, arayış veya yoksulluk · gereksinim duymak, bir şeye bağlı kalmak · onu bir başkasına gereksinir duruma getirmek · gereksinim duymak · gereksinim içindeyken istemekten kaçınmak · gereken şeyi aramak · gereksinim · gereksinim · gerçek ve ivedi gereksinim · gereksinimler · gereksinimler · gereksinimler
  أصل واحد وهو الاضطرار إلى الشيء (maqayis)؛ الحوج من الحاجة... أي احتاج (ayn;tahdhib)؛ الحائجة والحوجاء والحاجة بمعنى واحد (jamhara)؛ الحاجة معروفة... حاج يحوج حوجا أي احتاج وأحوجه إليه غيره (sihah)؛ الحوج الطلب والحوج الفقر (tahdhib)؛ الحاجة إلى الشيء الفقر إليه مع محبته وحاج يحوج احتاج (mufradat)
- **B002** kuşku bulunmaması ya da hiçbir sözle karşılık verilmemesi [kalıp] — Bu konuda içimde hiçbir kuşku yok. · Senin işinde hiçbir kuşku yok. · Bu konuda hiçbir kuşkum ve bağım yok. · Onunla konuştum, bana tek sözle bile karşılık vermedi.
  ما في صدري به حوجاء ولا لوجاء ولا شك ولا مرية بمعنى واحد (sihah)؛ ليس في أمرك حويجاء ولا لويجاء ولا رويغة (sihah)؛ كلمته فما رد علي حوجاء ولا لوجاء... كلمة قبيحة ولا حسنة (sihah;tahdhib)
- **B003** belirli bir dikenli bitki veya ağaç — bir tür dikenli bitki veya ağaç · dikenli bitki adının küçültme biçimi · toprak bu dikenli bitkiyi yetiştirdi
  الحاج ضرب من الشوك وهو شاذ عن الأصل (maqayis)؛ الحاج من الشوك ضرب منه (ayn)؛ الحاج... ضرب من الشجر (jamhara)؛ الحاج ضرب من الشوك (sihah;tahdhib;mufradat)؛ أحيجت الأرض وأحاجت إذا أنبتت الحاج (tahdhib)
- **B004** tökezleme veya kötü bir olay anında esenlik dileği — Tökezlediğinde veya başına kötü bir olay geldiğinde esenlik seninle olsun.
  الحوج لغة يمانية يقول الرجل للرجل عند العثرة أو المصيبة حوجا لك أي سلامة لك (jamhara)

## ف ل ك (root_001177): 40:80 ٱلْفُلْكِ

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

## ن ك ر (root_001550): 40:81 تُنكِرُونَ

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

## ه ز ء (root_001587): 40:83 يَسْتَهْزِءُونَ

- **B001** alay etme; gizli şakayla küçümseme — alay etme; gizli veya şakaya benzer küçümseme · onunla alay etti · onunla alay etmeye yöneldi ya da alay etti · onunla alay etti · alay etme, küçümseyici şaka · alay edilen adam · insanlarla alay eden adam · onu alay ve oyun konusu yaptı · alay etmeye yönelme veya alay etme
  هزىء واستهزأ إذا سخر (maqayis)؛ الهزء السخرية يقال هزيء به واستهزأ به وتهزأ به (ayn)؛ الهزء والهزؤ السخرية ورجل هزءة يهزأ به وهزأة يهزأ بالناس (sihah)؛ الهزء السخرية ورجل هزأة يهزأ بالناس ورجل هزأة يهزأ به (tahdhib)؛ الهزء مزح في خفية وقد يقال لما هو كالمزح (mufradat)
- **B002** alaylarına karşılık ceza verme veya süre verip ansızın yakalama — Tanrı, alaylarına karşılık onları cezalandırır veya süre verip ansızın yakalar
  الله يستهزىء بهم أي يجازيهم على هزئهم بالعذاب فسمي جزاء الذنب باسمه (tahdhib)؛ الاستهزاء من الله في الحقيقة لا يصح وقوله الله يستهزئ بهم أي يجازيهم جزاء الهزؤ (mufradat)؛ أمهلهم مدة ثم أخذهم مغافصة فسمى إمهاله إياهم استهزاء (mufradat)
- **B003** şiddetli soğuğa uğrama veya soğuktan ölme — 
  هزأني البرد أصابني شدته واهتزأت صرت في شدة البرد ويقال إنما هو بالراء (ayn)؛ أهزأه البرد وأهرأه إذا قتله ومثله فيما تعاقب فيه الزاي والراء (tahdhib)
- **B004** binek hayvanını hareket ettirme — binek hayvanını hareket ettirdi
  نزأت الراحلة وهزأتها إذا حركتها (tahdhib)

## س ن ن (root_000750): 40:85 سُنَّتَ

- **B001** izlenen yol ve yerleşik davranış kuralı — izlenen yol, yerleşik davranış biçimi veya uyulan hüküm · yol, yöntem ve izlenen doğrultu · kendi yolunda ve doğrultunda ilerle
  السنة وهي السيرة (maqayis); المسنن طريق يسلك (ayn); السنن الطريقة (sihah); السنة الطريقة المستقيمة المحمودة (tahdhib); سنة الله حكمه وأمره ونهيه (tahdhib)
- **B002** dağılmadan, kolayca döküp yayma [kalıp] — suyu yüzüme kolayca ve dağıtmadan döktüm · zırhı onun üzerine döktü · toprağı yere kolayca döktü
  سننت الماء على وجهي إذا أرسلته إرسالا (maqayis); سن عليه الدرع يسنها سنا إذا صبها؛ سن الماء على وجهه أي صبه عليه صبا سهلا (tahdhib); سننت الماء على وجهي إذا أرسلته إرسالا من غير تفريق؛ سنت التراب صببته (sihah)
- **B003** taşta keskinleştirme ve keskin uç — bıçağı bileği taşında keskinleştirmek · bileği taşı · mızrak ucu · taş sürtülürken dökülen kötü kokulu kırıntı
  سننت الحديدة أسنها سنا إذا أمررتها على السنان (maqayis); المسن الحجر الذي يسن عليه السكين أي يحدد (ayn); سننت السكين أحددته والمسن حجر يحدد به (sihah); سننت السنان أسنه سنا فهو مسنون إذا أحددته على المسن (tahdhib)
- **B004** diş; diş gelişimiyle belirlenen yaş ve olgunluk — tek bir diş · diş gelişimiyle ölçülen yaş · adam yaşlandı · belirli diş evresine erişmiş olgun hayvan · dişleri temizleyip güçlendiren ağız ilacı
  السن واحدة الأسنان؛ كبرت سن الرجل؛ أسن الرجل كبر (ayn); السن واحد الأسنان وقد يعبر بالسن عن العمر؛ أسن الرجل كبر (sihah); أسن إذا نبت سنه؛ المسن إذا أثنى (tahdhib); السن معروف وجمعه أسنان (mufradat)
- **B005** belirli söz öbeklerinde biçimlenmiş veya değişmiş madde ve biçimli yüz [kalıp] — dökülmüş, biçimlenmiş veya değişip kötü kokmuş çamur · yüzün biçimi ve çizgileri · uzun, konik veya yontulmuş gibi düzgün yüzlü
  الحمأ المسنون كأنه قد صب صبا (maqayis); حمأ مسنون قيل هو المنتن والمسنون المصور (ayn); الحمأ المسنون المتغير المنتن؛ سنة الوجه صورته؛ المسنون المصور والمملس (sihah); حمإ مسنون أي متغير؛ المصبوب على صورة؛ الوجه المسنون كالمخروط (tahdhib)
- **B006** iyi otlatıp güçlendirme ve bakımlı hale getirme [kalıp] — develeri iyi otlatıp bakımlı ve güçlü hale getirmek · binekleri güçlendirecek meraya bırakın
  سن إبله إذا رعاها حتى حسنت بشرتها (maqayis); سن الرجل إبله إذا أحسن رعيتها (sihah); سن الإبل إذا أحسن رعيتها حتى كأنه صقلها؛ أصابت الإبل سنا من الرعي (tahdhib)
- **B007** kovalayıp veya ısırıp çöktürme — erkek devenin dişiyi kovalayıp veya ısırıp çöktürmesi · erkek devenin dişiyi yüzüstü çöktürmesi · erkek develerin birbirini ısırıp çekişmesi
  الفحل يسان الناقة مسانة وسنانا إذا طردها حتى تنوخها (sihah); سن الفحل الناقة إذا كبها على وجهها؛ تسانت الفحول إذا تكادمت (tahdhib); سان البعير الناقة عاضها حتى أبركها (mufradat)
- **B008** ani ve güçlü biçimde ileri atılma [kalıp] — atın sıçrayıp koşuda ileri atılması · yara kanının birden fışkırması · deve veya at topluluğunun durdurulamaz biçimde gelmesi
  السنة مالج الفرس في عدوه وإقباله وأدباره (ayn); استن الفرس قمص؛ استنت الفصال حتى القرعى (sihah); استنت الدابة على وجه الأرض؛ استن دم الطعنة إذا جاءت دفعة منها؛ جاء من الإبل والخيل سنن ما يرد وجهه (tahdhib)
- **B009** diş gibi ayrılan veya uzanan parça — sarımsak dişi · orağın tırtıklı kesici dişleri · kalemin yontulan ucu · toprağı yaran tarım aleti demiri
  سن من ثوم أي حبة من رأسه؛ أسنان المنجل ونحوه (ayn); سنة من ثوم فصة منه؛ سن القلم موضع البرى منه؛ السنة السكة (sihah); الحديدة التي يحرث بها الأرض يقال لها السنة والسكة؛ أسنان المنجل؛ سن من ثوم (tahdhib)
- **B010** omurların üst kemik çıkıntıları — omurların üst kenarları ve çıkıntılı kemik başları
  السناسن أطراف فقار الظهر (maqayis); السناسن حروف فقار الظهر العليا (ayn); السناسن رءوس المحالة وحروف فقار الظهر (sihah); السناسن والشناشن العظام؛ السناسن رؤوس المحال (tahdhib)
- **B011** uzun kum şeridi; tek yönden değişmeden gelen rüzgar — yeryüzünde uzanan yükselmiş veya ayrık kum şeridi · rüzgarın yön değiştirmeden aynı doğrultudan gelmesi
  جاءت الريح سنائن إذا جاءت على طريقة واحدة (maqayis); السنينة من الرمل الشقيقة المنقطعة وجمعها سنائن (ayn); السنينة رمال مرتفعة تستطيل على وجه الأرض؛ جاءت الريح سنائن إذا جاءت على طريقة واحدة لا تختلف (sihah); السنائن رمال تستطيل على وجه الأرض؛ جاءت الرياح سنائن إذا جاءت على وجه واحد لا تختلف (tahdhib)

## خ ل و (root_000436): 40:85 خَلَتْ

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



===== _commentary/v16/work/s040/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s040/reader_a_pilot.md)

# s040 Semantic Channel Discovery

## Parent Channels

### 1. P1 Argument as Tension and Loss of Footing
- Semantic invariant: Contested speech applies torsion until either the claim holds or its bearer loses stability.
- Surface relation: direct; 40:4-6, 20 (يجادل، جادلوا، ليدحضوا، الباطل، الحق، كلمة).
- Surprising reach: Rope-work, tight weaving, thrusting, and slippery footing materialize argument as a load-bearing mechanical contest.

#### Subchannel A. Braided Disputation
- Reading type: mixed
- Scene or process: Opposing speakers twist propositions together and drive them against a tightly formed claim.
- Active motifs: verbal entanglement `quranic:root_000229:B002/m01`; tightly woven speech `quranic:root_000347:B010/m01`; penetrating straight thrust `quranic:root_000347:B009/m01`; speech exchange `quranic:root_001316:B001/m01`; speech as a wound `quranic:root_001316:B003/m01`.
- Ayah anchors: 40:4-5 (يجادل، جادلوا); 40:5, 20 (الحق); 40:6 (كلمة).
- Synthesis: Disputation is not merely talk: it is twisted material pressed against a compact, penetrating utterance. The wound-sense of speech sharpens the scene into reciprocal verbal force.

#### Subchannel B. The Defeated Claim Loses Ground
- Reading type: mixed
- Scene or process: A false argument attempts to knock truth down but instead forfeits its own footing and collapses.
- Active motifs: throwing or felling onto hard ground `quranic:root_000229:B003/m01`; hard supporting ground `quranic:root_000229:B004/m01`; slipping foot and lost stability `quranic:root_000461:B001/m01`; collapsed argument `quranic:root_000461:B003/m01`; loss of truth and stability `quranic:root_000127:B001/m01`.
- Ayah anchors: 40:4-5 (يجادل، جادلوا); 40:5 (ليدحضوا، الباطل).
- Synthesis: The attempt to fell truth becomes a reversal: falsehood is the position that slips. Physical footing and propositional validity share one outcome, collapse under pressure.

### 2. P1 Provision Released from Held Stores
- Semantic invariant: Life-sustaining material descends only after being borne, retained, or measured in an elevated container.
- Surface relation: indirect; 40:7, 13, 15 (يحملون العرش، ينزل لكم من السماء رزقا، ذو العرش).
- Surprising reach: The celestial descent of provision expands into clouds, catchments, grain, and udders as variants of controlled storage and release.

#### Subchannel A. Elevated Bearing and Descent
- Reading type: mixed
- Scene or process: A raised canopy bears a load above, a cloud carries water, and provision is sent down from that held height.
- Active motifs: raised canopy or shelter `quranic:root_001000:B002/m01`; bearing a load aloft `quranic:root_000357:B010/m01`; water-bearing cloud `quranic:root_000745:B004/m01`; stacked cloud `quranic:root_000532:B008/m01`; descent `quranic:root_001492:B001/m01`; sending down provision or water `quranic:root_001492:B002/m01`.
- Ayah anchors: 40:7, 15 (العرش); 40:7 (يحملون، ربهم); 40:13 (السماء، ينزل).
- Synthesis: Throne-bearing and rain-bearing are linked by supported height. What is above is not inert elevation; it is a loaded structure from which a needed allotment descends.

#### Subchannel B. Rain Becomes Revived Yield
- Reading type: latent/lexical
- Scene or process: Rain descends through the interval between sky and earth, revives the land, and terminates in edible grain.
- Active motifs: rain as provision `quranic:root_000560:B003/m01`; land revived by rain `quranic:root_000383:B002/m01`; rain falling between cloud and earth `quranic:root_000672:B005/m01`; grain ear `quranic:root_000672:B008/m01`.
- Ayah anchors: 40:13 (رزقا); 40:11 (أحييتنا); 40:7, 11 (سبيل، أحييتنا).
- Synthesis: The provision of 40:13 acquires a full hydraulic and vegetal sequence: descent, reanimation, and grain-bearing. The route-sense and ear-sense of the same root make yield the endpoint of a traversed channel.

#### Subchannel C. Milk Retained for Timed Yield
- Reading type: latent/lexical
- Scene or process: Milk is deliberately left in the udder, held there, then released in repeated or paired milkings.
- Active motifs: starter milk left in the udder `quranic:root_000478:B003/m01`; repeated milk flow `quranic:root_000563:B006/m01`; milk retained in the udder `quranic:root_000582:B007/m01`; two pails milked together `quranic:root_000802:B005/m01`.
- Ayah anchors: 40:10 (تدعون); 40:12 (دعي); 40:14 (فادعوا); 40:20 (يدعون); 40:5 (رسل); 40:15 (رفيع); 40:18 (شفيع).
- Synthesis: Lexical milk imagery supplies a domestic analogue to celestial provision. Sustenance is useful because it is held rather than exhausted, then released in an ordered recurrence.

### 3. P1 Concealment Forced into Observation
- Semantic invariant: Judgment removes protective cover and places hidden contents within an active field of perception.
- Surface relation: direct; 40:16, 19-20 (بارزون، لا يخفى، خائنة الأعين، تخفي الصدور، السميع البصير).
- Surprising reach: Exposure is not only visibility; it recruits extraction from hiding, watch-duty, and perceptive understanding.

#### Subchannel A. Extraction into Open Ground
- Reading type: mixed
- Scene or process: Concealed contents are pulled from cover and made to stand in an exposed, unobstructed place.
- Active motifs: appearance and disclosure `quranic:root_000105:B001/m01`; open exposed space `quranic:root_000105:B002/m01`; concealment `quranic:root_000428:B001/m01`; removal from hiding `quranic:root_000428:B003/m01`.
- Ayah anchors: 40:16 (بارزون، لا يخفى); 40:19 (تخفي).
- Synthesis: The bare appearance of persons and the extraction of what breasts hide form one disclosure event. Exposure changes both the setting and the state of its contents.

#### Subchannel B. The Watched Interior
- Reading type: mixed
- Scene or process: Eye, watcher, hearing, sight, and inward insight jointly register an attempted hidden breach.
- Active motifs: eye `quranic:root_001069:B001/m01`; watcher or custodian `quranic:root_001069:B003/m01`; spy or lookout `quranic:root_001069:B005/m01`; physical sight `quranic:root_000121:B001/m01`; inward insight `quranic:root_000121:B002/m01`; hearing `quranic:root_000741:B001/m01`; understanding through hearing `quranic:root_000741:B003/m01`.
- Ayah anchors: 40:19 (الأعين); 40:20 (البصير، السميع).
- Synthesis: Treacherous looking is enclosed by a wider surveillance apparatus. Perception reaches from the ocular act to comprehension of the concealed intention behind it.

### 4. P1 Pressure at Bounded Passages
- Semantic invariant: A contained substance or force becomes critical where an opening is narrow, sealed, or liable to leak.
- Surface relation: direct; 40:18-19 (القلوب لدى الحناجر كاظمين، الأعين).
- Surprising reach: Choked emotion is extended through wells, springs, catchments, seals, and punctured skins as a general hydraulics of containment.

#### Subchannel A. The Heart at the Throat
- Reading type: mixed
- Scene or process: Inner pressure rises until the heart reaches a constricted bodily passage while breath and expression are suppressed.
- Active motifs: heart as inner organ `quranic:root_001248:B001/m01`; throat as narrow passage `quranic:root_000360:B001/m01`; held breath and silenced pressure `quranic:root_001303:B002/m01`; imminence drawing near `quranic:root_000029:B001/m01`.
- Ayah anchors: 40:18 (القلوب، الحناجر، كاظمين، الآزفة).
- Synthesis: The approaching day is felt as pressure migrating through the body. Nearness, constriction, and suppressed breath make dread a mechanically compressed state.

#### Subchannel B. Sealed Reservoirs and Escaping Flow
- Reading type: latent/lexical
- Scene or process: Water is held in a catchment or linked wells, forced toward an opening, and threatened by a leak through its container.
- Active motifs: sealed full opening `quranic:root_001303:B004/m01`; connected wells or channels `quranic:root_001303:B005/m01`; binding channel ends `quranic:root_001303:B006/m01`; well `quranic:root_001248:B007/m01`; spring `quranic:root_001069:B006/m01`; puncture leaking from a skin `quranic:root_001069:B007/m01`; water catchment `quranic:root_000018:B006/m01`.
- Ayah anchors: 40:18 (كاظمين، القلوب); 40:19 (الأعين); 40:5 (ليأخذوه).
- Synthesis: The bodily constriction opens into a latent water system: wells are linked, ends bound, and outlets sealed. A puncture threatens release, clarifying why containment itself is the operative pressure.

### 5. P1 Judgment as Exact Settlement
- Semantic invariant: An act generates a matching liability that is counted, collected, and discharged without remainder.
- Surface relation: direct; 40:3, 5, 17, 20 (العقاب، يقضي، تجزى، كسبت، الحساب، الحق).
- Surprising reach: Moral recompense takes the concrete form of account balancing, debt collection, and enforcement of an owned claim.

#### Subchannel A. Counted Earnings Receive Their Match
- Reading type: mixed
- Scene or process: Each acquired act is entered into an account and returned as an equivalent recompense.
- Active motifs: counting and account `quranic:root_000318:B001/m01`; earning or acquisition `quranic:root_001296:B001/m01`; matching an act with recompense `quranic:root_000244:B001/m01`; collection of a debt `quranic:root_000244:B003/m01`.
- Ayah anchors: 40:17 (الحساب، كسبت، تجزى).
- Synthesis: The verse's rapid reckoning is a completed transaction. What the self acquires is precisely what the account makes return to it.

#### Subchannel B. Claim, Verdict, and Penalty Collection
- Reading type: mixed
- Scene or process: A valid claim is adjudicated, its debt settled, and its penalty enforced after the offense.
- Active motifs: settlement or collection of debt `quranic:root_001237:B006/m01`; owned and enforceable claim `quranic:root_000347:B003/m01`; punishment following offense `quranic:root_001033:B007/m01`; sin or offense `quranic:root_000521:B001/m01`.
- Ayah anchors: 40:20 (يقضي، بالحق); 40:3, 5 (العقاب); 40:3, 11 (الذنب، ذنوبنا).
- Synthesis: Divine judgment is rendered as enforceable settlement, not only declaration. Offense creates a claim whose verdict and collection belong to the same exact process.

### 6. P2 History Read as a Ground Trace
- Semantic invariant: Earlier events remain legible as marks whose following discloses a recurrent outcome.
- Surface relation: direct; 40:21, 30-31, 34 (يسيروا، فينظروا، عاقبة، من قبلهم، دأب، من بعده).
- Surprising reach: Historical reflection behaves like expert tracking through hoof marks, footprints, and a customary trail.

#### Subchannel A. Following Material Traces
- Reading type: mixed
- Scene or process: A traveler moves through the land, directs sight toward surviving marks, and follows a predecessor's footprint.
- Active motifs: travel through terrain `quranic:root_000769:B001/m01`; directed inspection `quranic:root_001520:B001/m01`; surviving mark `quranic:root_000011:B003/m01`; following a predecessor's trace `quranic:root_000011:B004/m01`; marked hoofprint used for tracking `quranic:root_000011:B008/m01`; heel or footprint `quranic:root_001033:B002/m01`.
- Ayah anchors: 40:21 (يسيروا، فينظروا، آثارا، عاقبة).
- Synthesis: Ruins are not passive remains. They function as a track that asks the traveler to reconstruct movement and endpoint from marks left on the ground.

#### Subchannel B. Recurrent Precedent and Outcome
- Reading type: mixed
- Scene or process: A prior course becomes a repeatable pattern whose successors inherit the same terminal consequence.
- Active motifs: succession after a predecessor `quranic:root_001033:B005/m01`; terminal outcome `quranic:root_001033:B006/m01`; repeated punitive return `quranic:root_001033:B009/m01`; persistent customary course `quranic:root_000456:B001/m01`; established pattern `quranic:root_000456:B002/m01`; exemplary likeness `quranic:root_001397:B011/m01`.
- Ayah anchors: 40:21 (عاقبة، قبلهم); 40:30-31 (مثل، دأب، من بعدهم); 40:34 (من قبل، من بعده).
- Synthesis: The ground trace becomes a historical rule. What is followed is both a predecessor's path and an exemplary configuration that can return in later communities.

### 7. P2 Coercive Force and Protective Holding
- Semantic invariant: Political force attempts to seize and destroy, while refuge works by holding the threatened subject out of that force's reach.
- Surface relation: direct; 40:25-29, 33, 35 (اقتلوا، أقتل، عذت، عاصم، ينصرنا، جبار).
- Surprising reach: Refuge is rendered as a retaining rope, barrier, or protective binding that counters coercive control.

#### Subchannel A. Violence as Sovereign Control
- Reading type: surface-primary
- Scene or process: A ruler deploys killing, compulsion, and domination as instruments for controlling belief and public order.
- Active motifs: killing `quranic:root_001200:B001/m01`; exposing a target to killing `quranic:root_001200:B005/m01`; coercion or compulsion `quranic:root_000216:B003/m01`; dominating force `quranic:root_000732:B001/m01`; sovereign authority `quranic:root_000732:B003/m01`; warlike plotting `quranic:root_001334:B004/m01`.
- Ayah anchors: 40:25-26, 28 (اقتلوا، أقتل، أتقتلون); 40:35 (جبار، سلطان); 40:25 (كيد).
- Synthesis: The order to kill is one operation in a larger apparatus: sovereign force tries to compel a public settlement by eliminating the dissenter.

#### Subchannel B. Refuge as Restraint against Seizure
- Reading type: mixed
- Scene or process: The threatened speaker seeks a protector who can interpose a barrier, retain him securely, and vindicate him against attack.
- Active motifs: refuge `quranic:root_001059:B001/m01`; protective amulet `quranic:root_001059:B002/m01`; escape from threatened killing `quranic:root_001059:B006/m01`; holding or preventing seizure `quranic:root_001021:B001/m01`; retaining rope or strap `quranic:root_001021:B002/m01`; protective barrier `quranic:root_001677:B001/m01`; vindicating aid `quranic:root_001510:B002/m01`.
- Ayah anchors: 40:27 (عذت); 40:33 (عاصم); 40:21 (واق); 40:29 (ينصرنا).
- Synthesis: Refuge is not simple withdrawal. It is a counter-grip: a protective holder prevents hostile seizure and preserves the speaker long enough for vindication.

### 8. P2 Proof and Doubt as Competing Materials
- Semantic invariant: Evidence seeks stable, penetrative clarity while doubt encloses, interlocks, and disturbs reception.
- Surface relation: direct; 40:22-25, 28, 34-35 (البينات، سلطان مبين، الحق، شك، مرتاب).
- Surprising reach: Proof becomes a solid straight object or sharp edge, whereas doubt behaves like piercing threads and enclosing armor.

#### Subchannel A. Clear Proof with a Hard Edge
- Reading type: mixed
- Scene or process: A disclosed sign arrives as stable truth backed by an overpowering and verbally sharp proof.
- Active motifs: clear disclosure or evidence `quranic:root_000170:B004/m01`; revealing meaning in a sign or speech `quranic:root_000170:B005/m01`; truthful statement `quranic:root_000852:B001/m01`; solid straight object `quranic:root_000852:B002/m01`; complete stable rightness `quranic:root_000852:B003/m01`; overpowering proof `quranic:root_000732:B002/m01`; sharp tongue `quranic:root_000732:B004/m01`.
- Ayah anchors: 40:22-23, 28, 34 (البينات، مبين); 40:25, 28 (الحق، صادقا); 40:23, 35 (سلطان).
- Synthesis: Evidence is both disclosure and resistant material. Its straightness lets it bear weight; its edge lets it cut through the opposing account.

#### Subchannel B. Doubt as Piercing Enclosure
- Reading type: mixed
- Scene or process: Doubt penetrates, threads states together, and finally encloses the subject in an interlocked defensive casing.
- Active motifs: two interpenetrating states of doubt `quranic:root_000812:B001/m01`; piercing or threading `quranic:root_000812:B002/m01`; enclosing armor `quranic:root_000812:B003/m01`; interlocked rank `quranic:root_000812:B005/m01`; disturbed suspicion `quranic:root_000616:B001/m01`.
- Ayah anchors: 40:34 (شك، مرتاب).
- Synthesis: Doubt does not appear as an empty absence of proof. It is an active structure that pierces and then surrounds, explaining its persistence after repeated evidence.

### 9. P2 Closed Interiors
- Semantic invariant: An inward state is kept from circulation by concealment, sealing, or saturation to a fixed limit.
- Surface relation: direct; 40:28, 35 (يكتم إيمانه، يطبع الله على كل قلب).
- Surprising reach: Secret belief and stamped arrogance occupy different moral positions but share the mechanics of an interior closed to outward flow.

#### Subchannel A. Belief Held behind a Watertight Seam
- Reading type: mixed
- Scene or process: Faith is retained inside while its bearer prevents testimony from leaking into a hostile setting.
- Active motifs: hiding testimony `quranic:root_001284:B001/m01`; watertight closed seam `quranic:root_001284:B004/m01`; constricted breath `quranic:root_001284:B006/m01`; settled belief `quranic:root_000054:B002/m01`.
- Ayah anchors: 40:28 (يكتم، إيمانه).
- Synthesis: Concealed faith is a deliberate seal under pressure. The seam and held-breath imagery make silence a protective operation, not an empty absence of confession.

#### Subchannel B. The Heart Filled and Stamped
- Reading type: mixed
- Scene or process: Arrogance fills an interior to its limit, after which a stamp closes the vessel against further reception.
- Active motifs: stamp or seal `quranic:root_000926:B001/m01`; filling a vessel or river to its limit `quranic:root_000926:B003/m01`; encrusted defect `quranic:root_000926:B005/m01`; heart as interior center `quranic:root_001248:B001/m01`.
- Ayah anchors: 40:35 (يطبع، قلب).
- Synthesis: The stamped heart is not merely externally barred. It is already saturated and encrusted, so closure completes an inward condition the subject has made full.

### 10. P2 Directed and Lost Routes
- Semantic invariant: Guidance places a leader and direction at the head of a road; straying removes both route and recoverable position.
- Surface relation: direct; 40:28-29, 33-34 (يهدي، سبيل الرشاد، يضلل، هاد، ضلال).
- Surprising reach: Error extends from wrong direction to disappearance, burial, and lost possession.

#### Subchannel A. The Guide at the Road's Head
- Reading type: mixed
- Scene or process: A guide takes the leading position and conducts followers along a straight, maturing route.
- Active motifs: gentle guidance to a road `quranic:root_001583:B001/m01`; direction and conduct `quranic:root_001583:B002/m01`; leader at the head `quranic:root_001583:B003/m01`; straight route toward maturity `quranic:root_000565:B001/m01`; road `quranic:root_000672:B001/m01`.
- Ayah anchors: 40:28-29, 33 (يهدي، أهديكم، هاد); 40:29 (سبيل الرشاد).
- Synthesis: Guidance is a social and spatial arrangement: someone goes first, supplies orientation, and makes the road traversable toward a sound endpoint.

#### Subchannel B. Straying until the Object Vanishes
- Reading type: latent/lexical
- Scene or process: A traveler misses the goal, drops from view, and becomes like a possession whose location can no longer be recovered.
- Active motifs: straying from the goal `quranic:root_000913:B001/m01`; vanishing or burial `quranic:root_000913:B002/m01`; lost possession `quranic:root_000913:B003/m01`; stray animal `quranic:root_000913:B005/m01`.
- Ayah anchors: 40:25, 33-34 (ضلال، يضلل، يضل).
- Synthesis: Misguidance is intensified from a route error into loss of locatability. The subject is not simply on another road but progressively absent from a recoverable course.

### 11. P3 The Tower as an Engineered Route to the Hidden
- Semantic invariant: A constructed ascent promises access to a concealed object, but obstruction converts engineered reach into collapse.
- Surface relation: direct; 40:36-37 (ابن لي صرحا، أبلغ الأسباب، أسباب السماوات، فأطلع، صد عن السبيل، في تباب).
- Surprising reach: Architectural ribs, rope-like means, lookout work, and cut barriers expose the tower as a failed routing system rather than merely a tall monument.

#### Subchannel A. Assembling the Vertical Route
- Reading type: mixed
- Scene or process: Builders erect a ribbed high structure whose linked means are intended to carry the ruler toward a remote goal.
- Active motifs: assembled building `quranic:root_000156:B001/m01`; structural ribs or posts `quranic:root_000156:B009/m01`; high tower `quranic:root_000854:B004/m01`; rope, means, or connecting link `quranic:root_000664:B003/m01`; reaching a goal `quranic:root_000151:B001/m01`.
- Ayah anchors: 40:36 (ابن، صرحا، أبلغ، الأسباب); 40:37 (أسباب).
- Synthesis: The tower is a fabricated chain of supports and links. Its height matters because it is meant to become a continuous means of reaching.

#### Subchannel B. The Lookout into Concealed Space
- Reading type: mixed
- Scene or process: The climber gains a lookout, inspects what is hidden, and substitutes conjecture for attained certainty.
- Active motifs: ascent to a lookout `quranic:root_000945:B006/m01`; inspection of hidden matter `quranic:root_000945:B003/m01`; scouting from elevation `quranic:root_000945:B004/m01`; conviction from a sign `quranic:root_000969:B001/m01`; weak conjecture `quranic:root_000969:B003/m01`; unreliable outcome `quranic:root_000969:B006/m01`.
- Ayah anchors: 40:37 (فأطلع، لأظنه).
- Synthesis: Height is used as an epistemic instrument, yet the observer never crosses from scouting to knowledge. The lookout amplifies the mismatch between physical elevation and uncertain inference.

#### Subchannel C. Route Cut into Ruin
- Reading type: mixed
- Scene or process: The intended road is blocked, its connection cut, and the entire project terminates in loss.
- Active motifs: cutting a route `quranic:root_000664:B001/m01`; turning or blocking `quranic:root_000848:B001/m01`; mountain-like barrier `quranic:root_000848:B005/m01`; ruin or loss `quranic:root_000172:B001/m01`; severance `quranic:root_000172:B004/m01`; plotting `quranic:root_001334:B002/m01`.
- Ayah anchors: 40:37 (صد، السبيل، كيد، تباب).
- Synthesis: The tower's failure is a broken connection. Its claimed means do not open the route; obstruction and severance make the engineered ascent self-defeating.

### 12. P3 Calls that Assign Destinations
- Semantic invariant: A call draws its hearer toward a place, so rival calls disclose rival endpoints.
- Surface relation: direct; 40:38, 41-43, 49-50 (اتبعون، سبيل الرشاد، أدعوكم، تدعونني، النار، ادعوا، فادعوا).
- Surprising reach: Calling recruits spatial attraction, safe high ground, beacon fire, and custodial petition.

#### Subchannel A. A Call toward Rescue
- Reading type: mixed
- Scene or process: A caller draws the people onto a guided road leading toward separation from danger and elevated safety.
- Active motifs: drawing by speech `quranic:root_000478:B001/m01`; rescue or separation `quranic:root_001476:B001/m01`; high ground safe from flood `quranic:root_001476:B004/m01`; straight route `quranic:root_000565:B001/m01`; road `quranic:root_000672:B001/m01`; following `quranic:root_000175:B001/m01`.
- Ayah anchors: 40:38, 41-42 (اتبعون، سبيل الرشاد، أدعوكم); 40:38, 47 (اتبعون، تبعا).
- Synthesis: The believing man's call is a relocation operation. Following his voice means entering a road whose endpoint is raised beyond the threatening flood.

#### Subchannel B. The Countercall toward Fire
- Reading type: mixed
- Scene or process: The opposing call recruits companions for a fire that functions at once as destination and visible beacon.
- Active motifs: call toward an undesired descent `quranic:root_000478:B004/m01`; fire `quranic:root_001564:B002/m01`; beacon or landmark `quranic:root_001564:B005/m01`; companion or resident `quranic:root_000844:B001/m01`; entry `quranic:root_000464:B001/m01`.
- Ayah anchors: 40:41-43 (تدعونني، النار، أصحاب النار); 40:46-47, 49 (النار); 40:40, 46 (يدخلون، أدخلوا).
- Synthesis: The rival invitation is legible by its destination. Fire is both the landmark toward which the call points and the residence created by obeying it.

#### Subchannel C. Petition from Custody
- Reading type: mixed
- Scene or process: Confined inhabitants appeal through their keepers for a temporary reduction, but the call returns without a route out.
- Active motifs: house empty of a caller `quranic:root_000478:B008/m01`; storekeeper or guard `quranic:root_000406:B001/m01`; custodial guardian `quranic:root_000406:B003/m01`; lightening a burden `quranic:root_000427:B001/m01`; reducing an amount `quranic:root_000427:B003/m01`; lost route `quranic:root_000913:B001/m01`.
- Ayah anchors: 40:49-50 (لخزنة، ادعوا، يخفف، فادعوا، ضلال).
- Synthesis: The request travels up a custodial chain but produces no opening. Even a one-day reduction is inaccessible because the petition itself remains inside the lost route.

### 13. P3 Judgment as a Settlement Ledger
- Semantic invariant: Deeds, shares, testimony, and excuses are converted into exact allocations at settlement.
- Surface relation: direct; 40:37, 40, 47, 51-52 (عمله، عمل، يجزى، مثلها، نصيبا، حساب، الأشهاد، معذرتهم).
- Surprising reach: Wages, commercial exchange, rations, assigned shares, and witness tongues materialize eschatological allocation.

#### Subchannel A. Work Paid at Equivalence
- Reading type: mixed
- Scene or process: Intended work enters a transaction and receives wages no greater or less than its moral equivalent.
- Active motifs: intended work `quranic:root_001046:B001/m01`; wages for labor `quranic:root_001046:B004/m01`; commercial transaction `quranic:root_001046:B005/m01`; matching recompense `quranic:root_000244:B001/m01`; equivalence or likeness `quranic:root_001397:B001/m01`; counting an account `quranic:root_000318:B001/m01`.
- Ayah anchors: 40:37, 40 (عمله، عمل); 40:40 (يجزى، مثلها، حساب).
- Synthesis: Action is processed like compensated labor. Equivalence governs the exchange, while uncounted garden provision marks the positive surplus beyond punitive matching.

#### Subchannel B. Shares, Rations, and Sufficiency
- Reading type: mixed
- Scene or process: Dependents request that powerful associates absorb an assigned share, but each party remains inside the allotted whole.
- Active motifs: allotted provision `quranic:root_000560:B001/m01`; rations `quranic:root_000560:B004/m01`; assigned share `quranic:root_001507:B005/m01`; sufficing for another `quranic:root_001110:B002/m01`; benefit or utility `quranic:root_001536:B001/m01`.
- Ayah anchors: 40:40 (يرزقون); 40:47 (مغنون، نصيبا); 40:52 (ينفع).
- Synthesis: The followers try to turn association into risk transfer. The ledger refuses: no patron can make another's allocated portion disappear or supply the needed sufficiency.

#### Subchannel C. Witness against Excuse
- Reading type: mixed
- Scene or process: Witnesses rise, testimony becomes present, and attempted excuses lose their power to alter the settled record.
- Active motifs: witness presence `quranic:root_000822:B001/m01`; testimony `quranic:root_000822:B002/m01`; witness tongue `quranic:root_000822:B005/m01`; offered excuse `quranic:root_000995:B001/m01`; deficient or false excuse `quranic:root_000995:B005/m01`; erased-trace excuse `quranic:root_000995:B007/m01`; expulsion or curse `quranic:root_001359:B001/m01`.
- Ayah anchors: 40:51 (الأشهاد); 40:52 (معذرتهم، اللعنة).
- Synthesis: Testimony fixes presence and trace just as excuse tries to remove them. Once witnesses stand, the attempted erasure fails and exclusion follows.

### 14. P3 Abodes as Moral Placement
- Semantic invariant: Conduct resolves into a mode of residence, ranging from low temporary lodging to stable enclosure.
- Surface relation: direct; 40:39-40, 43, 46, 52 (الحياة الدنيا، دار القرار، يدخلون الجنة، أصحاب النار، سوء الدار).
- Surprising reach: Nearness, lowness, settlement, enclosure, and companionship make the afterlife a topology of residence.

#### Subchannel A. Low Nearness versus Settled Residence
- Reading type: mixed
- Scene or process: A low, nearby life provides temporary use, while the later abode supplies fixed settlement.
- Active motifs: nearest world `quranic:root_000493:B002/m01`; lowness `quranic:root_000493:B003/m01`; resident at home `quranic:root_000499:B007/m01`; fixed settlement `quranic:root_001215:B003/m01`.
- Ayah anchors: 40:39 (الدنيا، دار القرار).
- Synthesis: The contrast is spatial as well as temporal. The present is near and low; the later house is where movement resolves into residence.

#### Subchannel B. Enclosed Garden or Fire Residence
- Reading type: mixed
- Scene or process: Entry places a person inside either a covered garden enclosure or the continuing company of fire.
- Active motifs: covered enclosure or garden `quranic:root_000266:B003/m01`; entry `quranic:root_000464:B001/m01`; companion or resident `quranic:root_000844:B001/m01`; fire `quranic:root_001564:B002/m01`.
- Ayah anchors: 40:40 (يدخلون الجنة); 40:43, 46 (أصحاب النار، النار، أدخلوا).
- Synthesis: Garden and fire are not passing encounters. Entry and companionship transform each destination into an inhabited enclosure.

### 15. P3 The Day Marked by Repeated Exposure
- Semantic invariant: Recurrent times disclose what a subject repeatedly faces and to what it is oriented.
- Surface relation: direct; 40:46, 55 (يعرضون عليها غدوا وعشيا، سبح بحمد ربك بالعشي والإبكار).
- Surprising reach: Morning departure, evening fire-seeking, display, beacon, and dawn turn paired time markers into opposite routines.

#### Subchannel A. Morning and Evening before Fire
- Reading type: mixed
- Scene or process: At both daily thresholds, the same group is brought out and displayed before fire.
- Active motifs: morning departure `quranic:root_001076:B001/m01`; evening `quranic:root_001017:B004/m01`; evening search for fire `quranic:root_001017:B002/m01`; display or exposure `quranic:root_001001:B002/m01`; fire `quranic:root_001564:B002/m01`.
- Ayah anchors: 40:46 (يعرضون، غدوا، عشيا، النار).
- Synthesis: Repetition makes exposure a daily placement rather than an isolated glimpse. The evening root's fire-seeking image makes the destination a grim answer to the search for a beacon.

#### Subchannel B. Evening and Dawn in Praise
- Reading type: mixed
- Scene or process: The day is opened and closed by repeated praise and prayer.
- Active motifs: evening `quranic:root_001017:B004/m01`; dawn or early morning `quranic:root_000143:B001/m01`; prayerful praise `quranic:root_000666:B001/m01`; praise `quranic:root_000355:B001/m01`.
- Ayah anchors: 40:55 (سبح، بحمد، بالعشي، الإبكار).
- Synthesis: The same temporal gates that mark punitive exposure can be occupied by praise within this pericope. Daily recurrence becomes a discipline of orientation.

### 16. P3 Adverse Force Rebounded
- Semantic invariant: Hostile action is redirected so that protection and public vindication replace the intended harm.
- Surface relation: direct; 40:44-45, 51 (أفوض أمري، فوقاه الله، سيئات ما مكروا، حاق، لننصر رسلنا).
- Surprising reach: Shielding, encirclement, and the rising witness convert private survival into a reversal visible at judgment.

#### Subchannel A. The Plot Encircles Its Makers
- Reading type: mixed
- Scene or process: A protective barrier intercepts a plot, while the harm curves back and surrounds the plotters' household.
- Active motifs: protective barrier `quranic:root_001677:B001/m01`; self-shielding `quranic:root_001677:B002/m01`; harm descending and encircling `quranic:root_000381:B001/m01`; evil outcome `quranic:root_000755:B001/m01`.
- Ayah anchors: 40:45 (فوقاه، سيئات، مكروا، حاق).
- Synthesis: Protection and punishment are one redirected trajectory. The believer is screened off precisely as the released harm closes around its originators.

#### Subchannel B. Support Becomes Public Standing
- Reading type: mixed
- Scene or process: Aid preserves messengers and believers until witnesses stand and their case becomes publicly vindicated.
- Active motifs: active aid `quranic:root_001510:B001/m01`; vindication after wrong `quranic:root_001510:B002/m01`; standing upright `quranic:root_001273:B002/m01`; witness presence `quranic:root_000822:B001/m01`.
- Ayah anchors: 40:51 (لننصر، يقوم، الأشهاد).
- Synthesis: Rescue is completed not merely by survival but by standing. The protected party reaches a public scene in which supporting testimony can appear.

### 17. P4 Measured Making Produces a Habitable Fit
- Semantic invariant: Creation is a measured fitting of structure, form, and provision into a stable place of life.
- Surface relation: direct; 40:57, 61-64 (خلق السماوات والأرض، جعل، الأرض قرارا، السماء بناء، صوركم، رزقكم).
- Surprising reach: Architectural ribs, balanced cutting, bodily formation, reservoir, pasture, and good provision join cosmic and human making as one fitted habitat.

#### Subchannel A. A Structured and Stable Cosmos
- Reading type: mixed
- Scene or process: Measured construction joins low ground, raised canopy, supports, and stable floor into a habitable whole.
- Active motifs: measuring and cutting a plan `quranic:root_000434:B001/m01`; balanced completed form `quranic:root_000434:B003/m01`; making or creating `quranic:root_000248:B001/m01`; assembled structure `quranic:root_000156:B001/m01`; structural supports `quranic:root_000156:B009/m01`; stable floor `quranic:root_001215:B006/m01`; low ground `quranic:root_000025:B001/m01`; canopy `quranic:root_000745:B004/m02`.
- Ayah anchors: 40:57, 62, 64 (خلق، جعل، السماوات، الأرض، قرارا، السماء، بناء).
- Synthesis: The cosmos is presented as fitted construction: measured parts establish a low floor beneath a borne canopy. Stability is an achieved relation among components.

#### Subchannel B. The Human Form Finished Well
- Reading type: mixed
- Scene or process: Human material is proportioned into an image whose completed fit is judged beautiful and sound.
- Active motifs: measured creation `quranic:root_000434:B002/m01`; image or form `quranic:root_000891:B003/m01`; beauty `quranic:root_000323:B001/m01`; making well `quranic:root_000323:B002/m01`.
- Ayah anchors: 40:64 (صوركم، فأحسن صوركم); 40:57, 62 (خلق).
- Synthesis: Formation is not mere appearance. Measuring and finishing make the image function as a well-fitted component of the larger habitat.

#### Subchannel C. Provision Sustains Settlement
- Reading type: mixed
- Scene or process: Wholesome allotment, pasture, and stored water maintain the inhabitants within the place made for them.
- Active motifs: sustaining dwelling or pasture `quranic:root_000726:B010/m01`; allotted provision `quranic:root_000560:B001/m01`; wholesome good `quranic:root_000961:B001/m01`; reservoir `quranic:root_000109:B003/m01`; lasting growth or blessing `quranic:root_000109:B004/m01`.
- Ayah anchors: 40:61, 64 (جعل لكم، رزقكم، الطيبات، تبارك).
- Synthesis: A habitat remains habitable through replenishment. Reservoir, pasture, and wholesome allotment make provision part of the architecture of settlement.

### 18. P4 Night and Day as Alternating Apertures
- Semantic invariant: The daily cycle alternately closes movement for rest and opens the world for perceptive activity.
- Surface relation: direct; 40:61 (الليل لتسكنوا فيه والنهار مبصرا).
- Surprising reach: Night is a cessation mechanism, while daylight is an opening widened until movement and perception can flow.

#### Subchannel A. Night Stops Motion
- Reading type: mixed
- Scene or process: Darkness closes ordinary activity and brings bodies into still, comforting settlement.
- Active motifs: night and darkness `quranic:root_001392:B001/m01`; cessation of motion `quranic:root_000726:B001/m01`; comforting rest `quranic:root_000726:B004/m01`.
- Ayah anchors: 40:61 (الليل، لتسكنوا).
- Synthesis: Night functions as a closure that arrests motion without becoming punitive confinement. Its outcome is restorative stillness.

#### Subchannel B. Day Opens Perception
- Reading type: mixed
- Scene or process: Daylight opens and widens the perceptual field until seeing and outward activity can proceed.
- Active motifs: daylight opening `quranic:root_001559:B002/m01`; widening an opening until flow `quranic:root_001559:B003/m01`; physical sight `quranic:root_000121:B001/m01`.
- Ayah anchors: 40:61 (النهار، مبصرا).
- Synthesis: Day is not merely bright time. It is an aperture whose widening releases perceptive movement after the stillness of night.

### 19. P4 Life Assembled in Stages
- Semantic invariant: A human life is a sequence of material bindings, emergences, thresholds, and final completion.
- Surface relation: direct; 40:67-68 (تراب، نطفة، علقة، يخرجكم طفلا، تبلغوا، شيوخا، يتوفى، أجلا، يحيي ويميت).
- Surprising reach: Dripping liquid, clinging clot, softness, ripening thresholds, and collection at death make biography a controlled manufacturing process.

#### Subchannel A. Binding the Form from Materials
- Reading type: mixed
- Scene or process: Loose earth gives way to a dripping fluid that clings and fixes within the womb.
- Active motifs: dust or soil `quranic:root_000178:B001/m01`; semen or formative water `quranic:root_001518:B002/m01`; dripping flow `quranic:root_001518:B003/m01`; clinging attachment `quranic:root_001039:B001/m01`; clot or thick blood `quranic:root_001039:B003/m01`; conception fixed in the womb `quranic:root_001039:B009/m01`.
- Ayah anchors: 40:67 (تراب، نطفة، علقة).
- Synthesis: Formation advances by increasing cohesion: dispersed material becomes a drop, then an attachment, then a fixed embodied beginning.

#### Subchannel B. Emergence through Maturing Thresholds
- Reading type: mixed
- Scene or process: The child emerges soft, reaches strength, and passes into old age through marked thresholds.
- Active motifs: child `quranic:root_000942:B001/m01`; softness of infancy `quranic:root_000942:B003/m01`; emergence `quranic:root_000400:B001/m01`; reaching a stage `quranic:root_000151:B001/m01`; old age `quranic:root_000834:B001/m01`.
- Ayah anchors: 40:67 (يخرجكم طفلا، تبلغوا، شيوخا).
- Synthesis: Life is not treated as undifferentiated duration. Each change crosses a functional threshold, from bodily emergence to strength and decline.

#### Subchannel C. Completion at the Appointed Limit
- Reading type: mixed
- Scene or process: A life reaches its named term, is collected in full, and enters the stillness of death.
- Active motifs: collection to completion `quranic:root_001669:B001/m01`; soul collected at death `quranic:root_001669:B002/m01`; appointed term `quranic:root_000016:B001/m01`; loss of life `quranic:root_001454:B001/m01`; stillness in death `quranic:root_001454:B012/m01`; completed decree `quranic:root_001237:B004/m01`.
- Ayah anchors: 40:67 (يتوفى، أجلا مسمى); 40:68 (يميت، قضى).
- Synthesis: Death is represented as completion and collection rather than accidental interruption. The appointed boundary closes the staged process exactly.

### 20. P4 Calling Opens What Pride Closes
- Semantic invariant: Responsive worship opens a relation of reception, while pride refuses that opening and ends in forced abasement.
- Surface relation: direct; 40:60, 65-66 (ادعوني أستجب لكم، يستكبرون عن عبادتي، داخرين، فادعوه، أعبد، تدعون).
- Surprising reach: Answering is a cut that opens passage; arrogance reverses voluntary humility into compelled lowliness.

#### Subchannel A. Call and Answer as an Opening
- Reading type: mixed
- Scene or process: A spoken appeal reaches a hearer whose answer pierces closure and opens a path of reception.
- Active motifs: spoken call `quranic:root_000478:B001/m01`; piercing or cutting an opening `quranic:root_000273:B001/m01`; answering a call `quranic:root_000273:B003/m01`; opened passage `quranic:root_000273:B004/m01`; hearing `quranic:root_000741:B001/m01`; worshipful obedience `quranic:root_000973:B003/m01`.
- Ayah anchors: 40:60, 65-66 (ادعوني، أستجب، فادعوه، أعبد، تدعون); 40:56 (السميع).
- Synthesis: Response is an aperture in relationship. Calling, hearing, and answering form a passage that worship keeps open.

#### Subchannel B. Pride Forced Downward
- Reading type: mixed
- Scene or process: The one who elevates himself above worship is made to enter in a lowered, submissive state.
- Active motifs: arrogance and self-magnification `quranic:root_001281:B006/m01`; abasement `quranic:root_000463:B001/m01`; humility or still submission `quranic:root_000726:B006/m01`; entry `quranic:root_000464:B001/m01`.
- Ayah anchors: 40:60 (يستكبرون، عبادتي، سيدخلون، داخرين); 40:61 (لتسكنوا).
- Synthesis: Refusal to bow does not preserve elevation. The scene reverses self-raised posture into compelled low entry.

### 21. P4 Perception as Route Orientation
- Semantic invariant: Seeing and remembering preserve directional coherence; blindness and diversion remove the marks by which a route can be held.
- Surface relation: direct; 40:58, 62-63, 69 (الأعمى والبصير، تذكرون، تؤفكون، يصرفون).
- Surprising reach: Blindness becomes unmarked terrain, while diversion becomes crosswind, verbal displacement, and a heart turned by enchantment.

#### Subchannel A. Sight on Marked Terrain
- Reading type: mixed
- Scene or process: A seeing traveler can distinguish a balanced course because perception and recollection preserve its marks.
- Active motifs: physical blindness `quranic:root_001049:B001/m01`; blind inward perception `quranic:root_001049:B002/m01`; unmarked terrain `quranic:root_001049:B006/m01`; physical sight `quranic:root_000121:B001/m01`; fair middle or straight course `quranic:root_000766:B006/m01`; remembered marker `quranic:root_000516:B009/m01`.
- Ayah anchors: 40:58 (الأعمى، البصير); 40:58 (تذكرون).
- Synthesis: The blind-seeing contrast becomes navigational. What blindness lacks is not only light but the terrain marks needed to recognize a balanced route.

#### Subchannel B. Diversion by Crosswind and Displaced Signs
- Reading type: latent/lexical
- Scene or process: A subject is turned from course as crosswinds redirect movement, signs are shifted, and inward attention is charmed away.
- Active motifs: turning away `quranic:root_000041:B001/m01`; opposing crosswinds `quranic:root_000041:B004/m01`; distorted judgment `quranic:root_000041:B006/m01`; redirecting a course `quranic:root_000860:B001/m01`; shifting signs or words `quranic:root_000860:B002/m01`; charm turning the heart `quranic:root_000860:B009/m01`; knowing denial `quranic:root_000224:B001/m01`.
- Ayah anchors: 40:62-63 (تؤفكون، يؤفك، يجحدون); 40:69 (يصرفون).
- Synthesis: Diversion is a composite loss of orientation. External winds, displaced signs, and inward fascination all prevent the subject from holding a straight interpretive course.

### 22. P5 Transport under Compulsion or Support
- Semantic invariant: Bodies and burdens move by an external carrier, but the relation ranges from violent traction to useful conveyance.
- Surface relation: direct; 40:71, 79-80 (الأغلال في أعناقهم والسلاسل يسحبون، لتركبوا، عليها وعلى الفلك تحملون).
- Surprising reach: Neck speed, coiled links, animal equipment, and wave-borne ships place punishment and provision inside one mechanics of directed motion.

#### Subchannel A. Chained Dragging
- Reading type: mixed
- Scene or process: A neck-bound subject is linked into a chain and pulled forward without control over direction.
- Active motifs: shackle binding hand to neck `quranic:root_001102:B006/m01`; connected chain links `quranic:root_000731:B002/m01`; coiled extension `quranic:root_000731:B003/m01`; neck `quranic:root_001053:B001/m01`; forced forward motion `quranic:root_001053:B004/m01`; dragging `quranic:root_000680:B001/m01`; neck yoke `quranic:root_000676:B009/m01`.
- Ayah anchors: 40:71 (الأغلال، أعناقهم، السلاسل، يسحبون); 40:72 (يسجرون).
- Synthesis: The chain converts the body into cargo. Its linked extension transmits force through the neck and fixes both pace and destination.

#### Subchannel B. Mounted Carriage
- Reading type: mixed
- Scene or process: Livestock bear riders and equipment so that a desired journey can be completed.
- Active motifs: livestock `quranic:root_001525:B005/m01`; riding animal `quranic:root_000589:B001/m01`; fitted riding components `quranic:root_000589:B004/m01`; carrying on an animal `quranic:root_000357:B001/m01`; carrying equipment `quranic:root_000357:B006/m01`.
- Ayah anchors: 40:79-80 (الأنعام، لتركبوا، عليها تحملون).
- Synthesis: Unlike dragging, mounted movement aligns the carrier with the rider's need. External force extends agency instead of cancelling it.

#### Subchannel C. Shipborne Carriage
- Reading type: mixed
- Scene or process: A vessel carries persons across moving water while waves support and threaten the route.
- Active motifs: carrying in a vessel `quranic:root_000357:B001/m02`; ship `quranic:root_001177:B003/m01`; moving waves `quranic:root_001177:B007/m01`.
- Ayah anchors: 40:80 (الفلك، تحملون).
- Synthesis: The ship is a mobile container whose support comes through an unstable medium. Carriage here depends on managing motion rather than resisting it.

### 23. P5 Entry into Permanent Confinement
- Semantic invariant: Admission passes through controlled thresholds and resolves into a residence that cannot be left.
- Surface relation: direct; 40:76 (ادخلوا أبواب جهنم خالدين فيها، فبئس مثوى المتكبرين).
- Surprising reach: Gatekeeping, prolonged detention, guest lodging, and clinging permanence turn entry into a complete custodial architecture.

#### Subchannel A. Controlled Thresholds
- Reading type: mixed
- Scene or process: Entrants pass through gates under implicit custodial control into a bounded interior.
- Active motifs: gate or entryway `quranic:root_000163:B001/m01`; gatekeeper `quranic:root_000163:B003/m01`; entry `quranic:root_000464:B001/m01`.
- Ayah anchors: 40:76 (ادخلوا، أبواب).
- Synthesis: The plural gates are active checkpoints, not decorative boundaries. Entry transfers the subject into another authority's controlled space.

#### Subchannel B. Lodging that Does Not End
- Reading type: mixed
- Scene or process: What resembles lodging becomes prolonged detention and then an enduring state to which the inhabitant clings.
- Active motifs: prolonged stay or confinement `quranic:root_000211:B001/m01`; lodging or guest house `quranic:root_000211:B002/m01`; enduring state `quranic:root_000429:B001/m01`; clinging or remaining `quranic:root_000429:B002/m01`.
- Ayah anchors: 40:76 (خالدين، مثوى).
- Synthesis: The language of lodging is inverted. A place normally associated with temporary reception becomes a permanent custodial abode.

### 24. P5 Husbandry Converts Provision into Use
- Semantic invariant: Animals and their produce are maintained through controlled feeding and watering so they can support human need.
- Surface relation: direct; 40:79-80 (الأنعام، منها تأكلون، منافع، حاجة).
- Surprising reach: Fodder mixtures, watering at the mouth, polished herds, lambs, and suckling restraints reveal the labor beneath apparently ready provision.

#### Subchannel A. Feeding, Watering, and Herd Condition
- Reading type: latent/lexical
- Scene or process: A herd is watered at the trough, given mixed fodder, and strengthened through grazing.
- Active motifs: date pits mixed with fodder `quranic:root_001102:B010/m01`; watering camels at the mouth `quranic:root_001198:B014/m01`; grazing that strengthens or polishes a herd `quranic:root_000750:B006/m01`; livestock `quranic:root_001525:B005/m01`.
- Ayah anchors: 40:71 (الأغلال); 40:74, 78, 82 (قبل); 40:85 (سنت); 40:79 (الأنعام).
- Synthesis: Livestock usefulness rests on a concealed maintenance system. Feed composition, watering, and grazing condition the animals before they appear as transport or food.

#### Subchannel B. Yield Directed to Human Need
- Reading type: mixed
- Scene or process: Herds yield food, young animals, carriage, and practical benefit, while their production is actively regulated.
- Active motifs: eating `quranic:root_000043:B001/m02`; fattened sheep or edible prey `quranic:root_000043:B007/m01`; feeding vessel `quranic:root_000043:B013/m01`; lamb `quranic:root_000357:B009/m01`; device preventing a kid from suckling `quranic:root_001177:B006/m01`; practical benefit `quranic:root_001536:B001/m01`.
- Ayah anchors: 40:79 (تأكلون); 40:80 (منافع، تحملون، الفلك); 40:85 (ينفعهم).
- Synthesis: Human benefit is produced by selective access to animal yield. Food and transport emerge from regulating who or what receives the herd's resources.

### 25. P5 History as Tracked and Narrated Evidence
- Semantic invariant: The past reaches the present through both traversable remains and ordered report.
- Surface relation: direct; 40:78, 82-85 (رسل، قصصنا، يسيروا، فينظروا، عاقبة، آثارا، سنة الله).
- Surprising reach: Footprint tracking and sequential storytelling become parallel ways of following a prior course to its result.

#### Subchannel A. Traversing the Remaining Track
- Reading type: mixed
- Scene or process: Travelers follow visible marks through the land until the marks disclose the predecessors' outcome.
- Active motifs: travel `quranic:root_000769:B001/m01`; directed inspection `quranic:root_001520:B001/m01`; tracking footprints `quranic:root_001232:B001/m01`; surviving trace `quranic:root_000011:B003/m01`; terminal outcome `quranic:root_001033:B006/m01`.
- Ayah anchors: 40:78 (قصصنا); 40:82 (يسيروا، فينظروا، آثارا، عاقبة).
- Synthesis: Physical travel turns historical consequence into inspectable evidence. The route is read backward from remnants to the acts that produced them.

#### Subchannel B. Narrating the Messenger Sequence
- Reading type: mixed
- Scene or process: Reports select and order earlier messengers, preserving enough of the sequence to expose a repeated divine course.
- Active motifs: sequential narration `quranic:root_001232:B002/m01`; sending a messenger `quranic:root_000563:B002/m01`; preserved report or trace `quranic:root_000011:B002/m01`; established road or custom `quranic:root_000750:B001/m01`; predecessor relation `quranic:root_001198:B002/m01`.
- Ayah anchors: 40:78 (أرسلنا، رسلا، قبلك، قصصنا، نقصص); 40:82, 85 (قبلهم، سنة الله).
- Synthesis: Narration is a non-spatial form of tracking. Selected reports preserve sequence and make the repeated course legible even where material traces are absent.

### 26. P5 Recognition at the Limit of Usefulness
- Semantic invariant: Denied signs become undeniable under force, but recognition arriving after practical agency has closed cannot alter the outcome.
- Surface relation: direct; 40:81-85 (آياته، تنكرون، البينات، علم، رأوا بأسنا، آمنا، لم يك ينفعهم، خسر).
- Surprising reach: Recognition, nonrecognition, commercial gain, short measure, and sufficiency make late belief an unusable asset in a closed transaction.

#### Subchannel A. Signs Made Unrecognizable
- Reading type: mixed
- Scene or process: Displayed signs are knowingly rejected until the subject treats the recognizable as alien or unacceptable.
- Active motifs: seeing or recognition `quranic:root_000531:B001/m01`; reflective seeing `quranic:root_000531:B002/m01`; sign `quranic:root_000074:B003/m01`; nonrecognition or denial `quranic:root_001550:B001/m01`; making something unrecognizable `quranic:root_001550:B004/m01`; rejected wrong `quranic:root_001550:B006/m01`.
- Ayah anchors: 40:81 (يريكم، آياته، آيات، تنكرون); 40:83 (البينات); 40:84-85 (رأوا).
- Synthesis: Denial is an operation performed on perception: what has been shown is recoded as unrecognizable. The later sight of force removes that recoding but too late.

#### Subchannel B. Force Compels Confession
- Reading type: surface-primary
- Scene or process: Overwhelming force closes alternatives and produces a declaration of sole allegiance.
- Active motifs: force or might `quranic:root_000079:B001/m01`; secure belief `quranic:root_000054:B002/m01`; divine oneness `quranic:root_001631:B004/m01`; covering over `quranic:root_001307:B001/m01`; assigning a share or associate `quranic:root_000791:B001/m01`.
- Ayah anchors: 40:82, 84-85 (قوة، بأسنا); 40:84-85 (آمنا، وحده، كفرنا، مشركين، إيمانهم).
- Synthesis: Confession is semantically correct but pragmatically constrained: it is produced only when force has eliminated the field in which allegiance could operate as a choice.

#### Subchannel C. The Closed Transaction
- Reading type: mixed
- Scene or process: Stored knowledge and accumulated earnings are tested for utility, fail to suffice, and resolve as commercial loss.
- Active motifs: possessed knowledge `quranic:root_001040:B001/m01`; practical benefit `quranic:root_001536:B001/m01`; earned acquisition `quranic:root_001296:B001/m01`; sufficing or standing in for another `quranic:root_001110:B002/m01`; loss `quranic:root_000409:B001/m01`; commercial loss `quranic:root_000409:B002/m01`; short measure `quranic:root_000409:B003/m01`.
- Ayah anchors: 40:82-83 (أغنى، يكسبون، العلم); 40:85 (ينفعهم، خسر).
- Synthesis: The final test is not possession but usability. Knowledge, earning, and late belief cannot be converted after settlement, so apparent assets register as a deficient trade.

### 27. P5 Authorized Outcomes Reach Completion
- Semantic invariant: A promised outcome arrives through authorized message and is then executed as a binding decision.
- Surface relation: direct; 40:77-78 (وعد الله حق، نرينك، نتوفينك، يرجعون، بإذن الله، أمر الله، قضي بالحق).
- Surprising reach: Promise, full collection, return, permission, command, and debt-like settlement form a chain from announcement to completion.

#### Subchannel A. Promise Completed despite Deferred Sight
- Reading type: mixed
- Scene or process: A true promise remains operative whether part of it is shown now or the addressee is collected before its completion and returned.
- Active motifs: binding promise `quranic:root_001662:B001/m01`; appointed promise `quranic:root_001662:B003/m01`; full collection `quranic:root_001669:B001/m01`; return `quranic:root_000544:B001/m01`; reply or restoration `quranic:root_000544:B005/m01`.
- Ayah anchors: 40:77 (وعد، نرينك، نعدهم، نتوفينك، يرجعون).
- Synthesis: Visibility does not govern fulfillment. The promise spans partial disclosure, death, and return because completion belongs to the obligation itself.

#### Subchannel B. Permission, Command, and Decisive Settlement
- Reading type: mixed
- Scene or process: A messenger acts under permission; when the governing command arrives, the matter is settled by an enforceable right.
- Active motifs: permission `quranic:root_000022:B004/m01`; binding command `quranic:root_000051:B002/m01`; adjudication `quranic:root_001237:B001/m01`; debt-like settlement `quranic:root_001237:B006/m01`; enforceable right `quranic:root_000347:B003/m01`; messenger or transmitted message `quranic:root_000563:B002/m01`.
- Ayah anchors: 40:78 (رسلا، رسول، بإذن، أمر، قضي، بالحق).
- Synthesis: Message and outcome are joined by authorization. Permission governs the sign's arrival, command activates the terminal event, and judgment closes it as a valid settlement.

## Standalone Subchannels

### S1. P1 Failed Kin-Backed Intercession
- Reading type: mixed
- Scene or process: A threatened person seeks help from intimate kin or an advocate who joins his petition, but no such joined party can act.
- Active motifs: close kin or intimate relation `quranic:root_000001:B011/m01`; kinship bond `quranic:root_000552:B002/m01`; joining one party to another `quranic:root_000802:B001/m01`; advocate joining a petitioner `quranic:root_000802:B002/m01`; obedience to an advocate `quranic:root_000956:B001/m01`.
- Ayah anchors: 40:18 (حميم، شفيع، يطاع); 40:7, 9 (رحمة، رحمته).
- Synthesis: Intercession is a social joining operation grounded in closeness and accepted speech. The scene fails because neither kinship nor an obediently heard advocate is available to attach the wrongdoer to relief.

### S2. P2 Selective Destruction of a Household Line
- Reading type: mixed
- Scene or process: State violence removes sons while preserving women alive, selectively reshaping the future of a believing household.
- Active motifs: assembled lineage or sons `quranic:root_000156:B007/m01`; preserving alive `quranic:root_000383:B006/m01`; women as a group `quranic:root_001500:B001/m01`; household or kin `quranic:root_000067:B003/m01`; killing `quranic:root_001200:B001/m01`.
- Ayah anchors: 40:25 (اقتلوا أبناء الذين آمنوا، استحيوا نساءهم); 40:28 (آل فرعون).
- Synthesis: The order is selective rather than indiscriminate: it attacks one branch of household continuity while retaining another under control. Lineage itself becomes the object of political engineering.

### S3. P3 A Ritual Circuit around a Standing Object
- Reading type: latent/lexical
- Scene or process: Worshippers circulate around a fixed cult object or standing sacrificial marker.
- Active motifs: object or place ritually circled `quranic:root_000499:B006/m01`; named idol `quranic:root_000760:B003/m01`; standing sacrificial stone `quranic:root_001507:B002/m01`; object of worship `quranic:root_000047:B001/m01`.
- Ayah anchors: 40:39, 52 (دار); 40:46 (الساعة); 40:47 (نصيبا); 40:42, 44, 48 (الله، العباد).
- Synthesis: The lexical images assemble a compact cultic scene: a fixed center, a standing marker, and bodies ordered around it. It usefully pressures the pericope's dispute over whom calls and worship actually orient people around.

### S4. P4 The Executable Utterance
- Reading type: mixed
- Scene or process: A spoken command does not describe a future object; it precisely executes the object's coming-to-be.
- Active motifs: precise execution or making `quranic:root_001237:B005/m01`; binding command `quranic:root_000051:B002/m01`; spoken utterance `quranic:root_001272:B001/m01`; occurrence in time `quranic:root_001332:B001/m01`; creation `quranic:root_000434:B002/m01`.
- Ayah anchors: 40:68 (قضى أمرا، يقول، كن، فيكون); 40:57, 62, 67 (خلق).
- Synthesis: Speech, command, and event collapse into one operation. The utterance is executable because its saying is already the precise completion of making.

### S5. P4 Reason as Tether and Refuge
- Reading type: latent/lexical
- Scene or process: Reason restrains impulsive wandering as a tether controls an animal and a fortified place protects its occupant.
- Active motifs: reason restraining ignorance `quranic:root_001036:B001/m01`; camel tether `quranic:root_001036:B002/m01`; fortified refuge `quranic:root_001036:B007/m01`; winding or entangled route `quranic:root_001036:B011/m01`.
- Ayah anchors: 40:67 (تعقلون).
- Synthesis: Reason is active restraint, not mere cognition. It checks movement before it enters an entangled route and thereby functions as a protective enclosure.

### S6. P5 The Boiling Furnace
- Reading type: mixed
- Scene or process: Bound bodies are dragged into boiling liquid and then into a furnace whose heat fills the interior and intensifies thirst.
- Active motifs: boiling water `quranic:root_000001:B002/m01`; melted fat under heat `quranic:root_000001:B003/m01`; sweat or extreme heat `quranic:root_000001:B004/m01`; pouring liquid into the throat `quranic:root_000676:B001/m01`; kindled furnace `quranic:root_000676:B005/m01`; thirst and heat in the gut `quranic:root_001102:B002/m01`; fire `quranic:root_001564:B002/m01`.
- Ayah anchors: 40:72 (الحميم، النار، يسجرون); 40:71 (الأغلال).
- Synthesis: The punishment is a thermal process as well as a destination. Boiling, pouring, internal heat, and furnace-kindling move the body from external restraint to invasive burning.

### S7. The Lot Bag and Its Winning and Losing Arrows
- Reading type: latent/lexical
- Scene or process: Gaming arrows are kept together in a leather case, a named lot is drawn, and the result assigns a winner and a loser.
- Active motifs: leather case holding gambling arrows `quranic:root_000532:B010/m01`; fifth gambling arrow `quranic:root_001533:B016/m01`; losing lot and failed gambler `quranic:root_000458:B019/m01`; winning lot coming out for its owner `quranic:root_001186:B001/m02`.
- Ayah anchors: 40:7 (ربهم); 40:17 (نفس); 40:33 (مدبرين); 40:9 (الفوز).
- Synthesis: The lot scene usefully pressures any reading of judgment as arbitrary allocation. A gambling result emerges from a blind draw, whereas the surah repeatedly grounds final shares in witnessed deeds, exact equivalence, and a settled account.

### S8. Prey Caught, Checked, and Released from a Snare
- Reading type: latent/lexical
- Scene or process: A hunter sets a noose, prey becomes entangled, its condition is checked, and extraction from the trap becomes deliverance.
- Active motifs: hunter's noose `quranic:root_000791:B006/m01`; prey caught in a snare `quranic:root_001039:B011/m01`; checking whether struck prey has died `quranic:root_001454:B014/m01`; escape from an entanglement `quranic:root_000430:B002/m01`; deliverance from harm `quranic:root_001186:B001/m01`.
- Ayah anchors: 40:42 (أشرك); 40:67 (علقة); 40:68 (يميت); 40:14 (مخلصين); 40:9 (الفوز).
- Synthesis: The hunting sequence materializes the surah's repeated plots to seize messengers and believers. Rescue is not vague safety but the precise reversal of capture: the hunted subject is worked free from the mechanism meant to hold it.

### S9. The Two-Bucket Well Hoist
- Reading type: latent/lexical
- Scene or process: A standing frame supports a rotating wheel and suspended line so that paired buckets can alternate between descent and ascent.
- Active motifs: rotating well pulley `quranic:root_000143:B006/m01`; water-lifting wheel `quranic:root_000373:B016/m01`; suspended pulley, rope, and two-bucket gear `quranic:root_001039:B002/m01`; upright well-frame component `quranic:root_001273:B012/m01`.
- Ayah anchors: 40:55 (الإبكار); 40:7 (حول); 40:67 (علقة); 40:51 (يقوم).
- Synthesis: The hoist materializes a linkage among the surah's vertical movements of provision, ascent, and return. Unlike Pharaoh's tower, useful elevation depends on a complete linked mechanism in which descent, support, and a returning stroke make ascent possible.

### S10. The Hidden-Hand Riddle and Color-Changing Toy
- Reading type: latent/lexical
- Scene or process: Players conceal an object in a hand, issue an opaque challenge, and manipulate a toy that displays a different color when pulled from the other side.
- Active motifs: guessing game about what a hand conceals `quranic:root_000400:B010/m01`; riddling challenge with a hidden answer `quranic:root_000478:B007/m01`; two-sided color-changing toy `quranic:root_000682:B006/m01`; deliberate obscuring and confusion `quranic:root_001049:B004/m01`.
- Ayah anchors: 40:11 (خروج); 40:43 (دعوة); 40:24 (ساحر); 40:58 (الأعمى).
- Synthesis: This game usefully pressures the opponents' treatment of signs as magic, riddles, or manipulable appearances. Their dispute converts disclosure into entertainment based on hidden contents and shifting color, while the surah's signs demand recognition rather than trick-solving.

### S11. Wood Consumed from Within
- Reading type: latent/lexical
- Scene or process: Small wood-eating creatures enter a structure or tree, bore through its material, and leave the apparently sound body internally ruined.
- Active motifs: termite consuming timber `quranic:root_000025:B010/m01`; boring insect eating leaves or wood until the tree is damaged `quranic:root_000699:B004/m01`; material eaten into corrosion and decay `quranic:root_000043:B006/m01`.
- Ayah anchors: 40:57 (الأرض); 40:43 (المسرفين); 40:79 (تأكلون).
- Synthesis: Internal consumption materializes how imposing structures and powerful peoples can fail despite visible hardness. It reframes the ruined traces and failed tower as outcomes whose weakness may precede collapse unseen inside the material.

### S12. An Abscess Brought to the Surface and Cleansed
- Reading type: latent/lexical
- Scene or process: A lesion rises on the body, pus accumulates inside it, corrupt matter discharges, and the contaminated area is cleaned.
- Active motifs: boil or ulcer emerging on the body `quranic:root_000400:B004/m01`; pus gathered in a wound or abscess `quranic:root_000281:B006/m01`; blood or pus expelled from an interior `quranic:root_001550:B005/m01`; cleansing away bodily filth `quranic:root_000961:B003/m01`.
- Ayah anchors: 40:67 (يخرجكم); 40:25 (جاءهم); 40:81 (تنكرون); 40:64 (الطيبات).
- Synthesis: The abscess process materializes the surah's movement from concealment to exposure. Corruption becomes treatable only after it declares itself at the surface and is expelled, usefully pressuring every attempt to preserve a clean appearance over a sealed interior.

### S13. A Written Contract for Manumission
- Reading type: latent/lexical
- Scene or process: An enslaved person and owner enter a written, guaranteed agreement whose promised payments establish an enforceable route to release.
- Active motifs: reducing a person to enslaved service `quranic:root_000973:B004/m01`; written manumission contract with scheduled payment `quranic:root_001283:B005/m01`; surety and written guarantee `quranic:root_001198:B008/m01`; reciprocal promise `quranic:root_001662:B004/m01`; parties arriving to complete an appointment `quranic:root_001669:B004/m01`.
- Ayah anchors: 40:60 (عبادتي); 40:2 (الكتاب); 40:3 (قابل); 40:77 (وعد); 40:77 (نتوفينك).
- Synthesis: The contract reframes liberation as a documented path whose terms can be fulfilled and enforced. It usefully pressures Pharaoh's arbitrary command over bodies by placing servitude beside covenant, guarantee, settlement, and an authored exit.

### S14. Invitation and Unauthorized Entry at a Feast
- Reading type: mixed
- Scene or process: A host calls guests to a celebratory meal while an uninvited outsider enters and attempts to mingle with the invited company.
- Active motifs: invitation to food `quranic:root_000478:B001/m02`; feast for a celebration or new event `quranic:root_000995:B009/m01`; uninvited banquet guest `quranic:root_000942:B006/m01`; outsider intruding into a group `quranic:root_000464:B005/m01`.
- Ayah anchors: 40:60 (ادعوني); 40:52 (معذرتهم); 40:67 (طفلا); 40:76 (ادخلوا).
- Synthesis: The feast scene reframes the surah's calls and admissions as a social relation between invitation, entry, and belonging. It supports the distinction between destinations opened by an authorized call and a claimed association that cannot make an outsider part of the company.

### S15. A Leader Bee Organizes the Swarm at Its Hive
- Reading type: latent/lexical
- Scene or process: A lead bee goes before a gathered swarm and orders its collective movement around a shared hive.
- Active motifs: honeybee hive `quranic:root_000436:B012/m01`; swarm of bees or wasps `quranic:root_000458:B014/m01`; lead bee at the head of the animals `quranic:root_001444:B008/m01`.
- Ayah anchors: 40:85 (خلت); 40:33 (مدبرين); 40:29 (الملك).
- Synthesis: The hive materializes guidance as ordered collective motion toward a common dwelling. It supports the surah's contrast between leadership that gives a community direction and Pharaoh's kingship, which gathers followers around a route ending in fire.

### S16. Reins, Bit, and the Sidling Horse
- Reading type: latent/lexical
- Scene or process: A rider uses bit and rein to urge a horse into a faster gait, but the animal veers sideways and protects its hoof on rough ground.
- Active motifs: restraining bit around a horse's jaw `quranic:root_000348:B006/m01`; rider extending the rein to increase speed `quranic:root_000151:B007/m01`; horse alternating between gaits `quranic:root_000546:B015/m01`; horse sidling instead of running straight `quranic:root_001001:B012/m01`; horse guarding a sore hoof from rough terrain `quranic:root_001677:B003/m01`.
- Ayah anchors: 40:48 (حكم); 40:36 (أبلغ); 40:28 (رجل); 40:46 (يعرضون); 40:45 (فوقاه).
- Synthesis: This riding scene usefully pressures the equation of speed or force with guidance. More rein and a harder drive can increase motion without correcting direction; the surah likewise distinguishes power and ambitious reach from a straight route.

### S17. Sharpening and Setting the Blade
- Reading type: latent/lexical
- Scene or process: A craftsperson hones an edge, fixes a point to its shaft, and turns prepared sharpness into a strike that stills a body.
- Active motifs: sharpening iron, knife, or spearpoint on a whetstone `quranic:root_000750:B003/m01`; fitting a shaft with a sharpened point `quranic:root_000051:B011/m01`; cutting edge of blade or sword `quranic:root_001078:B012/m01`; sword's gleam or trace of its blow `quranic:root_000011:B007/m01`; knife stilling a slaughtered animal `quranic:root_000726:B007/m01`.
- Ayah anchors: 40:85 (سنت); 40:68 (أمرا); 40:4 (يغررك); 40:21 (آثارا); 40:61 (تسكنوا).
- Synthesis: Prepared metal materializes how a ruler's order to kill can pass through an instrument into bodily stillness. The craft scene usefully pressures the claim that command and effective force amount to rightful judgment: sharp execution can be technically exact while morally false.

### S18. Perfume Prepared, Applied, and Carried through a Garment
- Reading type: latent/lexical
- Scene or process: Aromatic material is prepared on a perfume slab, compounded and applied, then remains perceptible in the colored or scented garment.
- Active motifs: perfume substance `quranic:root_000961:B007/m01`; compounding and coating with khaluq perfume `quranic:root_000434:B010/m01`; women's perfume that colors clothing `quranic:root_000058:B007/m01`; scent and the act of perfuming `quranic:root_001002:B004/m01`; perfume slab `quranic:root_000973:B012/m01`.
- Ayah anchors: 40:64 (الطيبات); 40:67 (خلقكم); 40:40 (أنثى); 40:11 (اعترفنا); 40:60 (عبادتي).
- Synthesis: Fragrance materializes disclosure through a medium that otherwise covers the body. Scent crosses the garment and makes an unseen source knowable, supporting the surah's insistence that concealed interiors still leave perceptible evidence.

### S19. Marriage Contract, Pairing, and Garland
- Reading type: mixed
- Scene or process: Two parties are joined by a marriage contract, supplied for the new household, and marked by a surrounding wedding garland.
- Active motifs: pairing one person with another `quranic:root_000652:B003/m01`; marriage contract `quranic:root_001444:B004/m01`; wedding provision that establishes the couple `quranic:root_001110:B006/m01`; encircling garland or crown `quranic:root_001315:B005/m01`.
- Ayah anchors: 40:8 (أزواجهم); 40:29 (الملك); 40:47 (مغنون); 40:7 (كل).
- Synthesis: The rite materializes the prayer that spouses and righteous kin be admitted together as an ordered household rather than a loose aggregate. It also usefully pressures Pharaoh's language of kingship by setting coercive possession against a public, covenantal union.

### S20. The Call Changes Hands and Tests Its Addressee
- Reading type: mixed
- Scene or process: P1 (40:1-20), P3 (40:36-55), P4 (40:56-70), and P5 (40:71-85); bridge: a repeated call scene undergoes role progression and reversal as speakers exchange invitations, the divine addressee answers, and rival addressees finally vanish.
- Active motifs: spoken call `quranic:root_000478:B001/m01`; invocation of descending harm `quranic:root_000478:B004/m01`; answering a call `quranic:root_000273:B003/m01`; addressee vanishing from reach `quranic:root_000913:B002/m01`.
- Ayah anchors: 40:12, 14 (دعي، ادعوا); 40:41-43, 49-50 (أدعوكم، تدعونني، ادعوا، دعاء); 40:60, 65 (ادعوني، فادعوه); 40:74 (ندعوا، ضلوا).
- Synthesis: The repeated form makes invocation a test of relationship rather than speech alone. It supports the primary contrast among destinations by showing that a call's direction, its addressee's power to answer, and that addressee's final availability determine where the caller is being drawn.

### S21. From Sealed Heart to Closed Gate
- Reading type: mixed
- Scene or process: P2 (40:21-35), P4 (40:56-70), and P5 (40:71-85); bridge: a causal aperture sequence moves from an internally stamped receiver, through an offered opening in call and answer, to an external gate and prolonged confinement.
- Active motifs: stamp or seal `quranic:root_000926:B001/m01`; answering a call `quranic:root_000273:B003/m01`; opened passage `quranic:root_000273:B004/m01`; gate or entryway `quranic:root_000163:B001/m01`; prolonged stay or confinement `quranic:root_000211:B001/m01`.
- Ayah anchors: 40:35 (يطبع); 40:60 (ادعوني أستجب); 40:76 (أبواب، مثوى).
- Synthesis: The terminal gate materializes a closure first established in reception. The intervening answer functions as a real aperture, so the sequence reframes permanent confinement as the outcome of refusing an available opening rather than as an unrelated final barrier.

### S22. The Patron Cannot Carry the Dependent's Share
- Reading type: mixed
- Scene or process: P1 (40:1-20), P2 (40:21-35), P3 (40:36-55), and P5 (40:71-85); bridge: a repeated patron-dependent scene and role reversal test every claimed protector by whether it can join the petition, provide aid, absorb an assigned share, or remain present at settlement.
- Active motifs: advocate joining a petitioner `quranic:root_000802:B002/m01`; active aid `quranic:root_001510:B001/m01`; assigned share `quranic:root_001507:B005/m01`; sufficing for another `quranic:root_001110:B002/m01`; practical benefit `quranic:root_001536:B001/m01`; patron vanishing from reach `quranic:root_000913:B002/m01`.
- Ayah anchors: 40:18 (شفيع); 40:29 (ينصرنا); 40:47, 51 (مغنون، نصيبا، لننصر); 40:74, 85 (ضلوا، ينفعهم).
- Synthesis: Allegiance is pressured by a liability-bearing criterion. A patron who directs dependents but cannot take any portion of their consequence is exposed as a failed protector, while effective aid belongs to the one who can actually stand with those under judgment.

### S23. Evidence Becomes Unavoidable Too Late
- Reading type: mixed
- Scene or process: P1 (40:1-20), P2 (40:21-35), P4 (40:56-70), and P5 (40:71-85); bridge: a causal progression moves from displayed sign and clear disclosure, through armored doubt and pathless blindness, to forced sight after practical benefit has closed.
- Active motifs: visible sign `quranic:root_000074:B003/m01`; clear disclosure or evidence `quranic:root_000170:B004/m01`; enclosing armor of doubt `quranic:root_000812:B003/m01`; unmarked terrain `quranic:root_001049:B006/m01`; sight and recognition `quranic:root_000531:B001/m01`; nonrecognition or denial `quranic:root_001550:B001/m01`; overpowering force `quranic:root_000079:B001/m01`; practical benefit `quranic:root_001536:B001/m01`.
- Ayah anchors: 40:13 (يريكم آياته); 40:22-23, 34-35 (البينات، شك، آيات الله); 40:56, 58, 63 (آيات الله، الأعمى، بآيات الله); 40:81, 84-85 (يريكم آياته، تنكرون، رأوا بأسنا، ينفعهم).
- Synthesis: Late confession is the last stage of a perceptual process, not an isolated surprise. The bridge supports the surah's primary warning by showing that evidence can become irresistible only after repeated denial has removed the agency in which recognition could still be useful.

### S24. The Daily Cycle Changes Its Occupant and Use
- Reading type: mixed
- Scene or process: P3 (40:36-55) and P4 (40:56-70); bridge: a repeated daily-cycle scene signature and contrast assigns morning and evening first to compulsory exposure, then to praise, while night and day are ordered for rest and sight.
- Active motifs: morning movement `quranic:root_001076:B001/m01`; evening `quranic:root_001017:B004/m01`; display or exposure `quranic:root_001001:B002/m01`; fire `quranic:root_001564:B002/m01`; dawn or early morning `quranic:root_000143:B001/m01`; prayerful praise `quranic:root_000666:B001/m01`; night and darkness `quranic:root_001392:B001/m01`; cessation of motion `quranic:root_000726:B001/m01`; daylight opening `quranic:root_001559:B002/m01`.
- Ayah anchors: 40:46 (يعرضون عليها غدوا وعشيا); 40:55 (سبح بالعشي والإبكار); 40:61 (الليل لتسكنوا فيه والنهار مبصرا).
- Synthesis: The same temporal thresholds can be occupied by punishment, worship, or creaturely repose. This contrast reframes the twice-daily exposure as an inverted devotional schedule and supports the primary reading that ordered time receives its moral character from what repeatedly fills it.

### S25. Bearer, Passenger, and Cargo
- Reading type: mixed
- Scene or process: P1 (40:1-20) and P5 (40:71-85); bridge: carrying roles progress and reverse as exalted servants bear a royal seat, humans travel as supported passengers, and bound bodies are reduced to dragged cargo.
- Active motifs: elevated royal seat `quranic:root_001000:B001/m01`; bearing a raised load `quranic:root_000357:B001/m03`; passenger carried on an animal `quranic:root_000357:B001/m01`; passenger carried in a vessel `quranic:root_000357:B001/m02`; shackle binding hand to neck `quranic:root_001102:B006/m01`; dragging `quranic:root_000680:B001/m01`.
- Ayah anchors: 40:7 (يحملون العرش); 40:71 (الأغلال، يسحبون); 40:80 (عليها وعلى الفلك تحملون).
- Synthesis: The reversal materializes the difference between honored support and compelled transport. It supports the surah's primary distinction between service ordered around praise, carriage given as benefit, and movement imposed when a person has forfeited the agency of a passenger.

### S26. The Household Policy Reversed on Pharaoh's House
- Reading type: mixed
- Scene or process: P1 (40:1-20), P2 (40:21-35), and P3 (40:36-55); bridge: a household-role reversal contrasts petitioned reunion with a ruler's selective editing of believing lineages, then makes that ruler's own household the named unit of encircling punishment.
- Active motifs: pairing one person with another `quranic:root_000652:B003/m01`; lineage or sons `quranic:root_000156:B007/m01`; preserving alive `quranic:root_000383:B006/m01`; women as a group `quranic:root_001500:B001/m01`; killing `quranic:root_001200:B001/m01`; household or kin `quranic:root_000067:B003/m01`; harm descending and encircling `quranic:root_000381:B001/m01`.
- Ayah anchors: 40:8 (أزواجهم); 40:25, 28 (اقتلوا أبناء، استحيوا نساءهم، آل فرعون); 40:45-46 (حاق، آل فرعون).
- Synthesis: Household continuity is first sought through righteous joining, then attacked through selective coercion, and finally returned as a corporate outcome upon the coercer's own house. The reversal supports the primary account of plotting that rebounds while refusing to equate family power with inherited protection.

### S27. From Carried Word to Executed Command
- Reading type: mixed
- Scene or process: P1 (40:1-20), P2 (40:21-35), P3 (40:36-55), P4 (40:56-70), and P5 (40:71-85); bridge: a causal sequence and role progression move authoritative discourse from written object and delivered message, through a messenger who carries it, to an utterance whose command becomes event and binding settlement.
- Active motifs: written book or record `quranic:root_001283:B002/m01`; delivery of a revealed book `quranic:root_001492:B002/m02`; messenger or word-carrier `quranic:root_000563:B002/m01`; spoken utterance `quranic:root_001272:B001/m01`; permission `quranic:root_000022:B004/m01`; binding command `quranic:root_000051:B002/m01`; precise execution or making `quranic:root_001237:B005/m01`; occurrence in time `quranic:root_001332:B001/m01`.
- Ayah anchors: 40:2, 5 (تنزيل الكتاب، رسول); 40:22-23, 34 (رسلهم، أرسلنا، رسولا); 40:50-53 (رسل، رسلنا، الكتاب); 40:68, 70 (قضى أمرا، يقول كن فيكون، الكتاب); 40:78, 83 (رسلا، رسول، بإذن الله، أمر الله، رسلهم).
- Synthesis: Revelation is not left as inert content: it is delivered, carried, spoken under authorization, and completed in an event. This sequence supports the primary reading by making rejection of the message resistance to an operative command whose final settlement belongs to the same chain of authority.

### S28. Rope Twisted, Knotted, and Put under Tension
- Reading type: latent/lexical
- Scene or process: A rope is tightly twisted, doubled at its ends, secured as a knot or bond, extended as a tether, and used to lift a restraint from a bound limb.
- Active motifs: tightly twisted rope `quranic:root_000229:B001/m01`; doubled-end rope or halter `quranic:root_000208:B007/m01`; knot and secure bond `quranic:root_000782:B001/m01`; long tether `quranic:root_000959:B002/m01`; cord lifting a prisoner's restraint `quranic:root_000582:B009/m01`.
- Ayah anchors: 40:3 (شديد، الطول); 40:4-5 (يجادل، جادلوا); 40:11 (اثنتين); 40:15 (رفيع).
- Synthesis: The rope scene materializes restraint as an engineered relation of fibers, knots, length, and applied tension. It supports the surah's primary contrast between attempted seizure and terminal binding by showing how control is constructed, while the lifted restraint preserves the possibility that a human bond can still be released.

### S29. A Raised Call, Its Reach, and Its Reverberation
- Reading type: mixed
- Scene or process: A herald announces openly, projects the voice across a distance, makes another hear, and receives the sound back as repetition or reverberation.
- Active motifs: public announcement by call `quranic:root_000022:B003/m01`; voice projected from the body `quranic:root_000239:B008/m01`; raised and far-reaching call `quranic:root_001486:B002/m01`; causing another to hear `quranic:root_000741:B004/m01`; returning or reverberating sound `quranic:root_000544:B007/m01`.
- Ayah anchors: 40:10, 32 (ينادون، التناد); 40:20, 56 (السميع); 40:43 (لا جرم); 40:77 (يرجعون); 40:78 (بإذن).
- Synthesis: Audibility is not yet answer. The scene usefully pressures the surah's many calls by distinguishing a voice that travels and returns as sound from an addressee who hears and acts; range and echo can simulate response but cannot provide rescue.

### S30. Basin, Channel, Tributary, and Terminal Pool
- Reading type: latent/lexical
- Scene or process: Water is gathered in a storage basin, released into a directed channel, divided through smaller courses and valley outlets, and allowed to settle at the end of its run.
- Active motifs: storage basin releasing water to crops `quranic:root_000016:B007/m01`; directing a watercourse `quranic:root_000009:B004/m01`; extended small channel `quranic:root_000229:B005/m01`; tributary and valley outlet `quranic:root_000521:B004/m01`; river cutting a course through land `quranic:root_001559:B001/m01`; terminal pool at a flood's end `quranic:root_001560:B004/m01`.
- Ayah anchors: 40:3 (ذنب); 40:4 (يجادل); 40:22 (تأتي); 40:61 (النهار); 40:66 (نهيت); 40:67 (أجلا).
- Synthesis: The hydraulic system materializes provision as controlled movement rather than static possession. It supports the primary account of a fitted, sustaining creation and reframes guidance as a route that actually delivers its charge, in contrast to an ambitious route that rises without carrying anything useful to a destination.

### S31. Probing a Head Wound and Assessing Its Due
- Reading type: latent/lexical
- Scene or process: A head wound is examined for penetration toward the brain, probed and measured, then assigned either a specified indemnity or equivalent retaliation by judgment.
- Active motifs: wound reaching the brain case `quranic:root_000053:B003/m01`; penetrating wound approaching brain or cavity `quranic:root_001518:B005/m01`; probing and measuring a wound `quranic:root_000295:B004/m01`; injury carrying required compensation `quranic:root_001488:B003/m01`; blood money or indemnity `quranic:root_001036:B004/m01`; equivalent retaliation `quranic:root_001232:B003/m01`; judicial assessment of injury `quranic:root_000348:B002/m01`.
- Ayah anchors: 40:5 (أمة); 40:8, 12 (حكيم، الحكم); 40:15, 18 (ينذر، أنذر); 40:47 (يتحاجون); 40:67 (نطفة، تعقلون); 40:78 (نقصص).
- Synthesis: The medical-legal scene materializes exact judgment as diagnosis before allocation. Depth, location, and consequence must be established before a due is fixed, supporting the primary claim that recompense is measured to the act rather than imposed as an undifferentiated penalty.

### S32. Hide Flayed, Tanned, Oiled, and Cut into Straps
- Reading type: latent/lexical
- Scene or process: A hide is stripped, checked for flesh left by the skinner, treated with tanning bark in measured applications, oiled, and cut into usable leather strips.
- Active motifs: flaying and stripping hide `quranic:root_001476:B003/m01`; flesh left on the hide `quranic:root_001102:B012/m01`; hide retaining hair or wool `quranic:root_000844:B006/m01`; tanning bark `quranic:root_000737:B008/m01`; measured application of tanning material `quranic:root_001533:B007/m01`; oiling tanned leather `quranic:root_001412:B005/m01`; cut leather strap `quranic:root_000769:B003/m01`.
- Ayah anchors: 40:6 (أصحاب); 40:10, 17 (أنفس، نفس); 40:21, 82 (يسير); 40:41 (نجاة); 40:66 (أسلم); 40:71 (الأغلال); 40:75 (تمرحون).
- Synthesis: The craft extends animal benefit beyond eating and riding into a sequence that converts a body covering into durable equipment. It supports the surah's primary provision scene by making usefulness depend on careful removal, treatment, and finishing rather than on raw possession alone.

### S33. Sewing and Sealing a Leather Water Carrier
- Reading type: latent/lexical
- Scene or process: Hide panels are joined edge to edge, stitched into a waterskin, fitted with side pieces and a carrying lug, then filled so moisture swells and seals the new seams.
- Active motifs: sewing hide edges together `quranic:root_000121:B006/m01`; stitching a waterskin `quranic:root_001283:B001/m01`; side panels of a water carrier `quranic:root_001536:B002/m01`; conditioning a new waterskin until its seams seal `quranic:root_001412:B003/m01`; carrying lug or handle `quranic:root_000741:B008/m01`.
- Ayah anchors: 40:2 (الكتاب); 40:20, 56 (السميع، البصير); 40:52, 80, 85 (ينفع، منافع، ينفعهم); 40:75 (تمرحون).
- Synthesis: The container materializes the relation between provision and receptivity: available water is useful only when a receiver can take and retain it without leaking. This reframes sealing as potentially protective and therefore sharpens the surah's contrasting heart-seal, which prevents reception rather than preserving what has entered.

### S34. Partners Appraise and Buy Out a Shared Asset
- Reading type: latent/lexical
- Scene or process: Partners delegate management to one another, establish the value of jointly held property, bid on the shares, and complete a partition or buyout that leaves one party with a defined possession.
- Active motifs: partnership by mutual delegation `quranic:root_001187:B003/m01`; appraisal and pricing `quranic:root_001273:B010/m01`; bidding to acquire a partner's share `quranic:root_001274:B004/m01`; partners partitioning or withdrawing shares `quranic:root_000400:B012/m01`; possession separated from partnership `quranic:root_000430:B004/m01`.
- Ayah anchors: 40:5 (قوم); 40:11 (خروج); 40:14 (مخلصين); 40:21 (قوة); 40:44 (أفوض).
- Synthesis: Genuine partnership entails reciprocal authorization, valued shares, and enforceable transfer. The scene usefully pressures the surah's claimed divine associates by showing that assertion alone cannot create partnership, assign ownership, or make another party answerable for a share.

### S35. Raising a Standard That Can Be Seen and Followed
- Reading type: mixed
- Scene or process: A standard is raised, installed upright in open view, and used as a distinguishing marker by which observers can identify a direction.
- Active motifs: raising an object `quranic:root_000582:B001/m01`; installing something upright and prominent `quranic:root_001507:B001/m01`; visible raised standard `quranic:root_000531:B011/m01`; distinguishing and guiding marker `quranic:root_001040:B002/m01`.
- Ayah anchors: 40:2 (عليم); 40:13 (يريكم); 40:15 (رفيع); 40:47 (نصيبا).
- Synthesis: A raised object becomes a sign only when its visibility supplies orientation. This materializes the surah's displayed signs and pressures Pharaoh's tower: elevation used for self-authorizing spectacle is not equivalent to a marker whose function is to guide those who see it.

### S36. Clarifying Butter and Preserving Its Extract
- Reading type: latent/lexical
- Scene or process: Milk thickens, its butter or fat is separated and melted, the clarified extract is retained, and the dense residue is reused to preserve or improve food.
- Active motifs: milk thickening and setting `quranic:root_000067:B005/m01`; extracting clarified butter or food `quranic:root_000430:B008/m01`; final butter or milk essence `quranic:root_000011:B009/m01`; melting and flowing after solidity `quranic:root_001602:B003/m01`; thick residue used to improve food `quranic:root_000532:B006/m01`.
- Ayah anchors: 40:5 (همت); 40:6 (ربك); 40:14 (مخلصين); 40:21 (آثارا); 40:28 (آل).
- Synthesis: The food process materializes provision as transformation into a concentrated, usable yield. It supports the primary distinction between possession and benefit: value appears through separation and skilled conversion, while unprocessed abundance or residue alone is not the finished provision.

### S37. Weighing and Exchanging Coin
- Reading type: latent/lexical
- Scene or process: Present coin is weighed against a fixed unit, checked for an even standard, assigned a price, and exchanged across currencies with any premium made visible.
- Active motifs: present cash or coin `quranic:root_001069:B011/m01`; fixed ounce weight `quranic:root_001677:B004/m01`; equal-weight dinar `quranic:root_001273:B015/m01`; currency exchange and premium `quranic:root_000860:B005/m01`.
- Ayah anchors: 40:5 (قوم); 40:7, 9, 21, 45 (ق، تق، واق، وقى); 40:19 (أعين); 40:69 (يصرف).
- Synthesis: The exchange scene materializes exact reckoning through declared units, balanced weight, and exposed premium. It supports the surah's settlement imagery while pressuring worldly valuations: a coin can command a market difference, but no exchange premium can alter the final standard applied to deeds.

### S38. Captain, Steering Stern, and Opposing Winds
- Reading type: mixed
- Scene or process: A captain directs a large vessel, its stern or steering structure checks instability, and changing winds drive or moderate its motion through water.
- Active motifs: captain of sailors `quranic:root_000532:B017/m01`; large ship `quranic:root_000436:B011/m01`; steering stern that stabilizes a ship `quranic:root_000726:B008/m01`; west or following wind `quranic:root_000458:B012/m01`; opposing east wind `quranic:root_001198:B012/m01`; gentle south wind `quranic:root_001525:B009/m01`; swimming or gliding motion `quranic:root_000666:B004/m01`.
- Ayah anchors: 40:3 (قابل); 40:6 (ربك); 40:7, 55 (يسبحون، سبح); 40:33 (مدبرين); 40:61 (تسكنوا); 40:79 (الأنعام); 40:85 (خلت).
- Synthesis: Shipborne carriage is materialized as coordinated command, steering, resistance, and propulsion rather than effortless motion. The scene supports the primary presentation of vessels as a benefit and sign by exposing the ordered system that makes carriage possible, unlike Pharaoh's model of direction through solitary command.

### S39. Rumor Escalates into Feud and an Unsettled Blood Claim
- Reading type: mixed
- Scene or process: A circulating report is used to incite people against one another, hardens into enmity, produces a blood claim, and leaves the injured group seeking vengeance or compensation.
- Active motifs: tale-bearing that incites conflict `quranic:root_000043:B009/m01`; report spreading among people `quranic:root_001272:B007/m01`; feud or enmity between groups `quranic:root_001564:B007/m01`; vengeance obligation for a killing `quranic:root_000959:B008/m01`; blood left without vengeance or compensation `quranic:root_000127:B006/m01`; blood trace grounding a claim `quranic:root_000121:B004/m01`.
- Ayah anchors: 40:3 (الطول); 40:5 (الباطل); 40:6 (النار); 40:11 (قالوا); 40:20 (بصير); 40:79 (تأكلون).
- Synthesis: The causal scene shows how speech can become social violence and how private retaliation can leave justice unresolved. It usefully pressures the surah's disputes and plots by distinguishing rumor-driven escalation from judgment that establishes the act, fixes the due, and closes the claim.

### S40. Fresh Dates Packed, Covered, and Found Spoiled
- Reading type: latent/lexical
- Scene or process: Fresh dates are packed in a woven palm-leaf basket, placed within a box or carried sack, covered for protection, and later found spoiled inside the container.
- Active motifs: woven palm-leaf basket for fresh dates `quranic:root_000464:B010/m01`; box or chest used as a container `quranic:root_000468:B006/m01`; protective covering `quranic:root_001096:B001/m01`; carried storage sack `quranic:root_001078:B013/m01`; spoiled date `quranic:root_001438:B006/m01`.
- Ayah anchors: 40:3 (غافر); 40:4 (يغررك); 40:8 (أدخل); 40:15 (الدرجات); 40:45 (مكر).
- Synthesis: Storage creates the appearance that provision has been secured, yet concealment can preserve neither quality nor usefulness by itself. The scene reframes the surah's failed assets and late recognition: what is possessed and covered may already be unusable when the container is finally opened.


