Surah: 30. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S30 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s030/surah.r2/text.md =====
# Surah 30

- 30:1 الٓمٓ
- 30:2 غُلِبَتِ ٱلرُّومُ
- 30:3 فِىٓ أَدْنَى ٱلْأَرْضِ وَهُم مِّنۢ بَعْدِ غَلَبِهِمْ سَيَغْلِبُونَ
- 30:4 فِى بِضْعِ سِنِينَ ۗ لِلَّهِ ٱلْأَمْرُ مِن قَبْلُ وَمِنۢ بَعْدُ ۚ وَيَوْمَئِذٍۢ يَفْرَحُ ٱلْمُؤْمِنُونَ
- 30:5 بِنَصْرِ ٱللَّهِ ۚ يَنصُرُ مَن يَشَآءُ ۖ وَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- 30:6 وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ وَعْدَهُۥ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- 30:7 يَعْلَمُونَ ظَٰهِرًۭا مِّنَ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ عَنِ ٱلْءَاخِرَةِ هُمْ غَٰفِلُونَ
- 30:8 أَوَلَمْ يَتَفَكَّرُوا۟ فِىٓ أَنفُسِهِم ۗ مَّا خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَآ إِلَّا بِٱلْحَقِّ وَأَجَلٍۢ مُّسَمًّۭى ۗ وَإِنَّ كَثِيرًۭا مِّنَ ٱلنَّاسِ بِلِقَآئِ رَبِّهِمْ لَكَٰفِرُونَ
- 30:9 أَوَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ كَانُوٓا۟ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَأَثَارُوا۟ ٱلْأَرْضَ وَعَمَرُوهَآ أَكْثَرَ مِمَّا عَمَرُوهَا وَجَآءَتْهُمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ ۖ فَمَا كَانَ ٱللَّهُ لِيَظْلِمَهُمْ وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- 30:10 ثُمَّ كَانَ عَٰقِبَةَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ ٱلسُّوٓأَىٰٓ أَن كَذَّبُوا۟ بِـَٔايَٰتِ ٱللَّهِ وَكَانُوا۟ بِهَا يَسْتَهْزِءُونَ
- 30:11 ٱللَّهُ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ ثُمَّ إِلَيْهِ تُرْجَعُونَ
- 30:12 وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يُبْلِسُ ٱلْمُجْرِمُونَ
- 30:13 وَلَمْ يَكُن لَّهُم مِّن شُرَكَآئِهِمْ شُفَعَٰٓؤُا۟ وَكَانُوا۟ بِشُرَكَآئِهِمْ كَٰفِرِينَ
- 30:14 وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يَوْمَئِذٍۢ يَتَفَرَّقُونَ
- 30:15 فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَهُمْ فِى رَوْضَةٍۢ يُحْبَرُونَ
- 30:16 وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَا وَلِقَآئِ ٱلْءَاخِرَةِ فَأُو۟لَٰٓئِكَ فِى ٱلْعَذَابِ مُحْضَرُونَ
- 30:17 فَسُبْحَٰنَ ٱللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ
- 30:18 وَلَهُ ٱلْحَمْدُ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَعَشِيًّۭا وَحِينَ تُظْهِرُونَ
- 30:19 يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَيُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ وَكَذَٰلِكَ تُخْرَجُونَ
- 30:20 وَمِنْ ءَايَٰتِهِۦٓ أَنْ خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ إِذَآ أَنتُم بَشَرٌۭ تَنتَشِرُونَ
- 30:21 وَمِنْ ءَايَٰتِهِۦٓ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا لِّتَسْكُنُوٓا۟ إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةًۭ وَرَحْمَةً ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- 30:22 وَمِنْ ءَايَٰتِهِۦ خَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْعَٰلِمِينَ
- 30:23 وَمِنْ ءَايَٰتِهِۦ مَنَامُكُم بِٱلَّيْلِ وَٱلنَّهَارِ وَٱبْتِغَآؤُكُم مِّن فَضْلِهِۦٓ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَسْمَعُونَ
- 30:24 وَمِنْ ءَايَٰتِهِۦ يُرِيكُمُ ٱلْبَرْقَ خَوْفًۭا وَطَمَعًۭا وَيُنَزِّلُ مِنَ ٱلسَّمَآءِ مَآءًۭ فَيُحْىِۦ بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- 30:25 وَمِنْ ءَايَٰتِهِۦٓ أَن تَقُومَ ٱلسَّمَآءُ وَٱلْأَرْضُ بِأَمْرِهِۦ ۚ ثُمَّ إِذَا دَعَاكُمْ دَعْوَةًۭ مِّنَ ٱلْأَرْضِ إِذَآ أَنتُمْ تَخْرُجُونَ
- 30:26 وَلَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ كُلٌّۭ لَّهُۥ قَٰنِتُونَ
- 30:27 وَهُوَ ٱلَّذِى يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ وَهُوَ أَهْوَنُ عَلَيْهِ ۚ وَلَهُ ٱلْمَثَلُ ٱلْأَعْلَىٰ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 30:28 ضَرَبَ لَكُم مَّثَلًۭا مِّنْ أَنفُسِكُمْ ۖ هَل لَّكُم مِّن مَّا مَلَكَتْ أَيْمَٰنُكُم مِّن شُرَكَآءَ فِى مَا رَزَقْنَٰكُمْ فَأَنتُمْ فِيهِ سَوَآءٌۭ تَخَافُونَهُمْ كَخِيفَتِكُمْ أَنفُسَكُمْ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْقِلُونَ
- 30:29 بَلِ ٱتَّبَعَ ٱلَّذِينَ ظَلَمُوٓا۟ أَهْوَآءَهُم بِغَيْرِ عِلْمٍۢ ۖ فَمَن يَهْدِى مَنْ أَضَلَّ ٱللَّهُ ۖ وَمَا لَهُم مِّن نَّٰصِرِينَ
- 30:30 فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا ۚ فِطْرَتَ ٱللَّهِ ٱلَّتِى فَطَرَ ٱلنَّاسَ عَلَيْهَا ۚ لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- 30:31 ۞ مُنِيبِينَ إِلَيْهِ وَٱتَّقُوهُ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَلَا تَكُونُوا۟ مِنَ ٱلْمُشْرِكِينَ
- 30:32 مِنَ ٱلَّذِينَ فَرَّقُوا۟ دِينَهُمْ وَكَانُوا۟ شِيَعًۭا ۖ كُلُّ حِزْبٍۭ بِمَا لَدَيْهِمْ فَرِحُونَ
- 30:33 وَإِذَا مَسَّ ٱلنَّاسَ ضُرٌّۭ دَعَوْا۟ رَبَّهُم مُّنِيبِينَ إِلَيْهِ ثُمَّ إِذَآ أَذَاقَهُم مِّنْهُ رَحْمَةً إِذَا فَرِيقٌۭ مِّنْهُم بِرَبِّهِمْ يُشْرِكُونَ
- 30:34 لِيَكْفُرُوا۟ بِمَآ ءَاتَيْنَٰهُمْ ۚ فَتَمَتَّعُوا۟ فَسَوْفَ تَعْلَمُونَ
- 30:35 أَمْ أَنزَلْنَا عَلَيْهِمْ سُلْطَٰنًۭا فَهُوَ يَتَكَلَّمُ بِمَا كَانُوا۟ بِهِۦ يُشْرِكُونَ
- 30:36 وَإِذَآ أَذَقْنَا ٱلنَّاسَ رَحْمَةًۭ فَرِحُوا۟ بِهَا ۖ وَإِن تُصِبْهُمْ سَيِّئَةٌۢ بِمَا قَدَّمَتْ أَيْدِيهِمْ إِذَا هُمْ يَقْنَطُونَ
- 30:37 أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- 30:38 فَـَٔاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ ۚ ذَٰلِكَ خَيْرٌۭ لِّلَّذِينَ يُرِيدُونَ وَجْهَ ٱللَّهِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- 30:39 وَمَآ ءَاتَيْتُم مِّن رِّبًۭا لِّيَرْبُوَا۟ فِىٓ أَمْوَٰلِ ٱلنَّاسِ فَلَا يَرْبُوا۟ عِندَ ٱللَّهِ ۖ وَمَآ ءَاتَيْتُم مِّن زَكَوٰةٍۢ تُرِيدُونَ وَجْهَ ٱللَّهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُضْعِفُونَ
- 30:40 ٱللَّهُ ٱلَّذِى خَلَقَكُمْ ثُمَّ رَزَقَكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ۖ هَلْ مِن شُرَكَآئِكُم مَّن يَفْعَلُ مِن ذَٰلِكُم مِّن شَىْءٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- 30:41 ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ بِمَا كَسَبَتْ أَيْدِى ٱلنَّاسِ لِيُذِيقَهُم بَعْضَ ٱلَّذِى عَمِلُوا۟ لَعَلَّهُمْ يَرْجِعُونَ
- 30:42 قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلُ ۚ كَانَ أَكْثَرُهُم مُّشْرِكِينَ
- 30:43 فَأَقِمْ وَجْهَكَ لِلدِّينِ ٱلْقَيِّمِ مِن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۖ يَوْمَئِذٍۢ يَصَّدَّعُونَ
- 30:44 مَن كَفَرَ فَعَلَيْهِ كُفْرُهُۥ ۖ وَمَنْ عَمِلَ صَٰلِحًۭا فَلِأَنفُسِهِمْ يَمْهَدُونَ
- 30:45 لِيَجْزِىَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِن فَضْلِهِۦٓ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْكَٰفِرِينَ
- 30:46 وَمِنْ ءَايَٰتِهِۦٓ أَن يُرْسِلَ ٱلرِّيَاحَ مُبَشِّرَٰتٍۢ وَلِيُذِيقَكُم مِّن رَّحْمَتِهِۦ وَلِتَجْرِىَ ٱلْفُلْكُ بِأَمْرِهِۦ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- 30:47 وَلَقَدْ أَرْسَلْنَا مِن قَبْلِكَ رُسُلًا إِلَىٰ قَوْمِهِمْ فَجَآءُوهُم بِٱلْبَيِّنَٰتِ فَٱنتَقَمْنَا مِنَ ٱلَّذِينَ أَجْرَمُوا۟ ۖ وَكَانَ حَقًّا عَلَيْنَا نَصْرُ ٱلْمُؤْمِنِينَ
- 30:48 ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَيَبْسُطُهُۥ فِى ٱلسَّمَآءِ كَيْفَ يَشَآءُ وَيَجْعَلُهُۥ كِسَفًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ ۖ فَإِذَآ أَصَابَ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
- 30:49 وَإِن كَانُوا۟ مِن قَبْلِ أَن يُنَزَّلَ عَلَيْهِم مِّن قَبْلِهِۦ لَمُبْلِسِينَ
- 30:50 فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- 30:51 وَلَئِنْ أَرْسَلْنَا رِيحًۭا فَرَأَوْهُ مُصْفَرًّۭا لَّظَلُّوا۟ مِنۢ بَعْدِهِۦ يَكْفُرُونَ
- 30:52 فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- 30:53 وَمَآ أَنتَ بِهَٰدِ ٱلْعُمْىِ عَن ضَلَٰلَتِهِمْ ۖ إِن تُسْمِعُ إِلَّا مَن يُؤْمِنُ بِـَٔايَٰتِنَا فَهُم مُّسْلِمُونَ
- 30:54 ۞ ٱللَّهُ ٱلَّذِى خَلَقَكُم مِّن ضَعْفٍۢ ثُمَّ جَعَلَ مِنۢ بَعْدِ ضَعْفٍۢ قُوَّةًۭ ثُمَّ جَعَلَ مِنۢ بَعْدِ قُوَّةٍۢ ضَعْفًۭا وَشَيْبَةًۭ ۚ يَخْلُقُ مَا يَشَآءُ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْقَدِيرُ
- 30:55 وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يُقْسِمُ ٱلْمُجْرِمُونَ مَا لَبِثُوا۟ غَيْرَ سَاعَةٍۢ ۚ كَذَٰلِكَ كَانُوا۟ يُؤْفَكُونَ
- 30:56 وَقَالَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ وَٱلْإِيمَٰنَ لَقَدْ لَبِثْتُمْ فِى كِتَٰبِ ٱللَّهِ إِلَىٰ يَوْمِ ٱلْبَعْثِ ۖ فَهَٰذَا يَوْمُ ٱلْبَعْثِ وَلَٰكِنَّكُمْ كُنتُمْ لَا تَعْلَمُونَ
- 30:57 فَيَوْمَئِذٍۢ لَّا يَنفَعُ ٱلَّذِينَ ظَلَمُوا۟ مَعْذِرَتُهُمْ وَلَا هُمْ يُسْتَعْتَبُونَ
- 30:58 وَلَقَدْ ضَرَبْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍۢ ۚ وَلَئِن جِئْتَهُم بِـَٔايَةٍۢ لَّيَقُولَنَّ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ أَنتُمْ إِلَّا مُبْطِلُونَ
- 30:59 كَذَٰلِكَ يَطْبَعُ ٱللَّهُ عَلَىٰ قُلُوبِ ٱلَّذِينَ لَا يَعْلَمُونَ
- 30:60 فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ وَلَا يَسْتَخِفَّنَّكَ ٱلَّذِينَ لَا يُوقِنُونَ


===== _commentary/v16/work/s030/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## غ ل ب (root_001098): 30:2 غُلِبَتِ, 30:3 غَلَبِهِمْ, 30:3 سَيَغْلِبُونَ

- **B001** güçle üstün gelme ve boyun eğdirme — yenmek; üstün gelmek · üstün gelme, yenme · üstünlük kurma, boyun eğdirme · üzerinde egemenlik kurmak; etkisi altına almak · üstün gelmek için çekişmek · üstünlük çekişmesi, mücadele · çok kez üstün gelen · üstünlük için karşılıklı mücadele · üstün gelme, üstünlük kazanma · sürekli yenilen; benzerlerine yenik düşen · üstün olduğuna karar verilen; başkalarından üstün tutulan · çok kez veya çabucak üstün gelen kimse · hastalık yüzünden yenik düşmek · birini başkasına üstün ilan etmek veya üstün kılmak
  أصل صحيح يدل على قوة وقهر وشدة؛ غلب الرجل غلبا وغلبة؛ والغلاب المغالبة؛ والمغلب من الشعراء المغلوب مرارا؛ والمغلب أيضا الذي غلب خصمه أو قرنه (maqayis)؛ غلب يغلب غلبا وغلبة؛ والغلاب النزاع؛ والمغلب الذي يغلبه أقرانه فيما يمارس؛ والمغلب قد يكون المفضل على غيره (ayn)؛ لمن الغلب والغلبة؛ رجل غلبة كثير الغلب؛ غالب الرجل الرجل مغالبة وغلابا؛ المغلبة الاسم من الغلب (jamhara)؛ تغلب على بلد كذا استولى عليه قهرا؛ والمغلب المغلوب مرارا؛ والمغلب أيضا من الشعراء المحكوم له بالغلبة على قرنه (sihah)؛ الغلبة القهر؛ غلب عليه كذا أي استولى (mufradat)
- **B002** kalın boyunlu ve güçlü yapılı olma — kalın boyunlu ve güçlü yapılı · kalın, iri ve güçlü yapılı · kalın ve sık yapılı olanlar · iri, kalın yapılı tepe · güçlü ve sarsılmaz onur · sık ve iç içe geçmiş bahçe · sık ve iç içe geçmiş bahçeler · ot iyice gelişip sıklaşarak birbirine dolandı
  والأغلب الغليظ الرقبة؛ هضبة غلباء وعزة غلباء؛ اغلولب العشب بلغ كل مبلغ (maqayis)؛ والأغلب الغليظ الشديد القصرة وأسد أغلب؛ هضبة غلباء وعزة غلباء؛ اغلولب العشب في الأرض إذا بلغ كل مبلغ (ayn)؛ رجل أغلب بين الغلب إذا كان غليظ العنق والأسد أغلب والأنثى غلباء (jamhara)؛ رجل أغلب بين الغلب إذا كان غليظ الرقبة؛ هضبة غلباء وعزة غلباء؛ حديقة غلباء ملتفة وحدائق غلب؛ اغلولب العشب بلغ والتف (sihah)؛ والأغلب الغليظ الرقبة؛ رجل أغلب وامرأة غلباء وهضبة غلباء؛ حدائق غلبا (mufradat)

## د ن و (root_000493): 30:3 أَدْنَى, 30:7 ٱلدُّنْيَا

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

## ء ر ض (root_000025): 30:3 ٱلْأَرْضِ, 30:8 وَٱلْأَرْضَ, 30:9 ٱلْأَرْضِ, 30:9 ٱلْأَرْضَ, 30:18 وَٱلْأَرْضِ, 30:19 ٱلْأَرْضَ, 30:22 وَٱلْأَرْضِ, 30:24 ٱلْأَرْضَ, 30:25 وَٱلْأَرْضُ, 30:25 ٱلْأَرْضِ, 30:26 وَٱلْأَرْضِ, 30:27 وَٱلْأَرْضِ, 30:42 ٱلْأَرْضِ, 30:50 ٱلْأَرْضَ

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

## ب ع د (root_000131): 30:3 بَعْدِ, 30:4 بَعْدُ, 30:19 بَعْدَ, 30:24 بَعْدَ, 30:50 بَعْدَ, 30:51 بَعْدِهِۦ, 30:54 بَعْدِ, 30:54 بَعْدِ

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

## ب ض ع (root_000123): 30:4 بِضْعِ

- **B001** kesip parçalara ayırma ve ayrılan parça — kesip parçalara ayırmak · toplu et parçası · et ve bedendeki etlilik · deriyi geçip eti yaran kesik · sürüden ayrılmış koyun topluluğu · damar ya da deri kesme aracı · değdiği yerden parça koparan kılıç
  بضعت اللحم أي قطعته (maqayis;ayn;sihah;tahdhib;mufradat)؛ والبضعة القطعة وهي الهبرة (maqayis;ayn;sihah;tahdhib)؛ الباضعة الشجة التي تشق اللحم (maqayis;sihah;tahdhib;mufradat)
- **B002** alım satıma ayrılmış varlık payı veya ürün — alım satıma ayrılmış varlık payı veya ürün · bir şeyi satılacak ürün olarak ayırmak · topluluğun satılacak ürünlerini getiren kişi · saygınlığını alınıp satılan bir şey gibi görmek
  بضاعة التاجر من ماله طائفة منه (maqayis)؛ البضاعة طائفة من مالك تبعثها للتجارة (sihah)؛ البضاعة السلعة وأصلها القطعة من المال الذي يتجر فيه (tahdhib)؛ قطعة وافرة من المال تقتنى للتجارة (mufradat)؛ البضائع كالعلائق وهي الجنائب (maqayis)
- **B003** cinsel organ, birleşme veya evlilik hakkı için örtmece — cinsel organ, evlilik veya cinsel birleşme için örtmece · onunla evlenmek veya evlilik akdini elinde bulundurmak · cinsel birleşmede bulunma · cinsel birleşme
  المباضعة المباشرة أو المجامعة (maqayis;sihah;tahdhib;mufradat)؛ ملك فلان بضع فلانة أي عقدة نكاحها أو تزوجها (maqayis;sihah;tahdhib;mufradat)؛ كني بالبضع عن الفرج (mufradat)
- **B004** üçten dokuza, kimi görüşte ona dek olan veya özellikle yediyi belirten sayı — üçten dokuza, kimi kaynaklarda ona dek belirsiz sayı · birkaç yıl · kullanımı tartışmalı yirmili belirsiz sayı kalıbı
  البضع من العدد ما بين الثلاثة إلى العشرة أو التسع (maqayis;sihah;tahdhib;mufradat)؛ بضع سنين (maqayis;sihah;tahdhib;mufradat)؛ البضع سبعة (maqayis;tahdhib)
- **B005** yer adı veya karadan kopuk ada — yer, ülke veya karadan kopuk ada · bir yer adı · bir kuyu adı
  البضيع بلد أو موضع (maqayis;sihah;tahdhib)؛ البضيع الجزيرة في البحر أو المنقطعة عن البر (maqayis;sihah;tahdhib;mufradat)؛ بئر بضاعة (sihah)
- **B006** susuzluğu veya bilgi gereksinimini giderme; birinden bıkma [kalıp] — sudan doyasıya içmek · su susuzluğumu giderdi · açıklayarak içini rahatlatmak · birinden bıkmak
  بضعت من الماء رويت (maqayis;sihah;tahdhib)؛ أبضعني الماء أرواني (sihah;tahdhib)؛ أبضعته إذا شفيته أو بينت له حتى يشتفي (maqayis;sihah;tahdhib)؛ بضعت من فلان إذا سئمت منه (sihah;tahdhib)
- **B007** terin akması veya terin kendisi — alnından ter akmak · terleyip kesik kesik akmak · ter
  جبهته تتبضع أي تسيل عرقا (sihah;tahdhib)؛ يتبضع يتفتح بالعرق ويسيل متقطعا (tahdhib)؛ البضيع العرق (sihah)
- **B008** pay veya iş ortağı — ortağım · ortaklarım
  هو شريكي وبضيعي وهم بضعائي وشركائي (tahdhib)

## س ن و (root_000751): 30:4 سِنِينَ

- **B001** suyu çekip toprağı ve ekini sulama — toprağı ve ekini sulamak için su çeken hayvan ya da düzenek · sulamak veya sulama suyu çekmek · sulama suyunu çeken kişi veya hayvan · bulutun toprağı yağmurla sulaması · kendi su ihtiyacı için su çekmek · kovayı kuyudan çekmek · sulanmış toprak · ancak hayvanlı bir düzenekle su çekilebilen derin kuyu
  سنت الناقة إذا سقت الأرض تسنو وهي السانية؛ السحابة تسنو الأرض؛ القوم يستنون إذا استقوا (maqayis)؛ السانية الناقة يسقى عليها للأرضين؛ سنوت الماء؛ السحاب يسنو المطر (ayn)؛ السانية الناضحة؛ سنت الناقة تسنو سناوة وسناية؛ الأرض مسنوة ومسنية (sihah)؛ السانية ما يسقى عليه الزروع والحيوان؛ سنت السانية تسنو؛ سنوت الدلو سناوة؛ الساني المستقي (tahdhib)
- **B002** gönlünü hoş tutup yumuşak davranma — birinin gönlünü hoş tutup ona yumuşak davranmak · istekte bulunurken yumuşak davranma ve iyi geçinme
  سانيت الرجل إذا راضيته (maqayis)؛ المساناة الملاينة في المطالبة (ayn)؛ سانيت الرجل إذا راضيته وداريته وأحسنت معاشرته (sihah)؛ سانيت الرجل راضيته وأحسنت معاشرته؛ المساناة الملاينة في المطالبة؛ المساناة المصانعة وهي المداراة؛ تسنيت فلانا إذا ترضيته (tahdhib)
- **B003** yüksek saygınlık ve yücelik — yüksek saygınlık ve yücelik · soyu bakımından yüksek saygınlıkta · yüce ve saygın · yükseltip yüceltmek · soyca yükselip saygın olmak
  السناء ممدود دل على الرفعة (maqayis)؛ فلانا لسني الحسب؛ سناء ممدود (ayn)؛ السناء من الرفعة والشرف ممدود؛ السني الرفيع؛ أسناه أي رفعه وأعلاه (sihah)؛ فلانا لسني الحسب؛ سناء ممدود؛ السناء من الشرف والمجد ممدود (tahdhib)
- **B004** şimşek ve ay ışığının parlak görünümü — şimşeğin veya ayın parlak ışığı · şimşeğin ışığı · şimşek ışığının eve, yere veya buluta yayılması
  السنا مقصور حد منتهى ضوء البدر والقمر (ayn)؛ السنا مقصور ضوء البرق (sihah)؛ السنا مقصور حد منتهى ضوء البدر والبرق؛ سنا البرق ضوءه (tahdhib)؛ يكاد سنا برقه يذهب بالأبصار (maqayis)
- **B005** meyvesi tedavide kullanılan bitki — meyvesi bulunan ve tedavide kullanılan bitki · bu türden tek bir bitki
  السنا نبات له حمل إذا يبس فحركته الريح سمعت له زجلا والواحدة سناة (ayn)؛ السنا أيضا نبت يتداوى به (sihah)؛ السنا نبات له حمل؛ السنا نبت (tahdhib)
- **B006** önünü açıp kolaylaştırma — açıp kolaylaştırmak · kapıyı açmak · işin önünü açıp kolaylaştırmak · işlerinde kolaylık bulmak
  سناه أي فتحه وسهله؛ إذا الله سنى عقد شيء تيسر (sihah)؛ سنيت الباب وسنوته إذا فتحته؛ سنيت الأمر إذا فتحت وجهه؛ تسنى الرجل إذا تسهل في أموره (tahdhib)
- **B007** taşkın suyunu düzenleyen bent — taşkını tutup ihtiyaç kadar su geçiren bent
  المسناة العرم (sihah)؛ المسناة ضفيرة تبنى للسيل لترد الماء؛ فيها مفاتيح للماء بقدر ما يحتاج إليه مما لا يغلب (tahdhib)
- **B008** yıl ve bir yıllık süre — yıl · bir yerde bir yıl kalmak · bir yıllık süre
  السنة إذا قلته بالهاء وجعلت نقصانه الواو فهو من هذا الباب؛ أسنى القوم إذا لبثوا في موضع سنة (sihah)؛ المساناة المسانهة وهي الأجل إلى سنة؛ تجمع السنة سنوات وسنين (tahdhib)
- **B009** bir şeyi bütünüyle almak [kalıp] — bir şeyi bütünüyle almak
  أخذه بسنايته وصنايته أي أخذه كله (sihah)
- **B010** erkek devenin çiftleşmek için dişiye çıkması [kalıp] — erkek devenin çiftleşmek için dişi devenin üzerine çıkması
  تسنى البعير الناقة إذا تسداها وقع عليها ليضربها (tahdhib)

## ECHO س ن ن (root_000750): for 30:4 سِنِينَ: withheld observed target; not identity

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

## ء ل ه (root_000047): 30:4 لِلَّهِ, 30:5 ٱللَّهِ, 30:6 ٱللَّهِ, 30:6 ٱللَّهُ, 30:8 ٱللَّهُ, 30:9 ٱللَّهُ, 30:10 ٱللَّهِ, 30:11 ٱللَّهُ, 30:17 ٱللَّهِ, 30:29 ٱللَّهُ, 30:30 ٱللَّهِ, 30:30 ٱللَّهِ, 30:37 ٱللَّهَ, 30:38 ٱللَّهِ, 30:39 ٱللَّهِ, 30:39 ٱللَّهِ, 30:40 ٱللَّهُ, 30:43 ٱللَّهِ, 30:48 ٱللَّهُ, 30:50 ٱللَّهِ, 30:54 ٱللَّهُ, 30:56 ٱللَّهِ, 30:59 ٱللَّهُ, 30:60 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 30:4 لِلَّهِ, 30:5 ٱللَّهِ, 30:6 ٱللَّهِ, 30:6 ٱللَّهُ, 30:8 ٱللَّهُ, 30:9 ٱللَّهُ, 30:10 ٱللَّهِ, 30:11 ٱللَّهُ, 30:17 ٱللَّهِ, 30:29 ٱللَّهُ, 30:30 ٱللَّهِ, 30:30 ٱللَّهِ, 30:37 ٱللَّهَ, 30:38 ٱللَّهِ, 30:39 ٱللَّهِ, 30:39 ٱللَّهِ, 30:40 ٱللَّهُ, 30:43 ٱللَّهِ, 30:48 ٱللَّهُ, 30:50 ٱللَّهِ, 30:54 ٱللَّهُ, 30:56 ٱللَّهِ, 30:59 ٱللَّهُ, 30:60 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ء م ر (root_000051): 30:4 ٱلْأَمْرُ, 30:25 بِأَمْرِهِۦ, 30:46 بِأَمْرِهِۦ

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

## ق ب ل (root_001198): 30:4 قَبْلُ, 30:9 قَبْلِهِمْ, 30:42 قَبْلُ, 30:43 قَبْلِ, 30:47 قَبْلِكَ, 30:49 قَبْلِ, 30:49 قَبْلِهِۦ

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

## ف ر ح (root_001140): 30:4 يَفْرَحُ, 30:32 فَرِحُونَ, 30:36 فَرِحُوا۟

- **B001** iç açan sevinç — sevinç; üzüntünün karşıtı olan iç açıcı duygu · sevindi; içi açıldı · bir şeyden ötürü sevinmek · sevinçli · çok sevinçli · sevinen; sevinçli · sevinme; sevinç · sık sık ve çok sevinen kimse · onu sevindirdi; onda sevinç doğurdu · kişiyi sevindiren şey · kendisine ya da olmasına sevinilen şey · sevindirme; kullanıldığı yere göre ağırlaştırma anlamı da taşıyabilir
  خلاف الحزن (maqayis;jamhara)؛ فرح به سر (sihah)؛ الفرح انشراح الصدر بلذة عاجلة (mufradat)؛ الفرحة المسرة (jamhara)؛ رجل فرح وفرحان وامرأة فرحة وفرحى (ayn;jamhara;tahdhib)؛ المفراح الكثير الفرح (sihah;mufradat)؛ ما يسرني به مفرح ومفروح به (ayn;sihah;tahdhib;mufradat)
- **B002** kınanan taşkın sevinç — haksız ve ölçüsüz, kınanan taşkın sevinç
  والفرح أيضا البطر (sihah)؛ تفرحون في الأرض بغير الحق (maqayis;mufradat)؛ أكثر ما يكون ذلك في اللذات البدنية الدنيوية (mufradat)
- **B003** yük altında bırakıp ağırlaştırma — ağırlaştırma; yük altında bırakma · borç yükü altında ezilmiş, ödeme gücü kalmamış kimse · borç onu ağırlaştırdı ve ödeme sıkıntısına soktu · korunmak üzere bırakılan şeyler sana ağır bir yük oldu · o şey beni ezdi ve ağır bir yük altında bıraktı · ağırlaştırma; kullanıldığı yere göre sevindirme anlamı da taşıyabilir
  الإفراح وهو الإثقال (maqayis)؛ رجل مفرح أثقله الدين (ayn;jamhara;sihah;tahdhib;mufradat)؛ أفرحه الدين أثقله (sihah;tahdhib)؛ أفرحتك الودائع (maqayis;ayn;sihah;tahdhib)؛ المفرح المفدوح (sihah;mufradat)؛ أفرحني الشيء مثل فدحني (jamhara)

## ء م ن (root_000054): 30:4 ٱلْمُؤْمِنُونَ, 30:15 ءَامَنُوا۟, 30:37 يُؤْمِنُونَ, 30:45 ءَامَنُوا۟, 30:47 ٱلْمُؤْمِنِينَ, 30:53 يُؤْمِنُ, 30:56 وَٱلْإِيمَٰنَ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ن ص ر (root_001510): 30:5 بِنَصْرِ, 30:5 يَنصُرُ, 30:29 نَّٰصِرِينَ, 30:47 نَصْرُ

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

## ش ي ء (root_000831): 30:5 يَشَآءُ, 30:37 يَشَآءُ, 30:40 شَىْءٍ, 30:48 يَشَآءُ, 30:48 يَشَآءُ, 30:50 شَىْءٍ, 30:54 يَشَآءُ

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

## ش ي ء (root_000832): 30:5 يَشَآءُ, 30:37 يَشَآءُ, 30:40 شَىْءٍ, 30:48 يَشَآءُ, 30:48 يَشَآءُ, 30:50 شَىْءٍ, 30:54 يَشَآءُ

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

## ع ز ز (root_001008): 30:5 ٱلْعَزِيزُ, 30:27 ٱلْعَزِيزُ

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

## ر ح م (root_000552): 30:5 ٱلرَّحِيمُ, 30:21 وَرَحْمَةً, 30:33 رَحْمَةً, 30:36 رَحْمَةً, 30:46 رَّحْمَتِهِۦ, 30:50 رَحْمَتِ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## و ع د (root_001662): 30:6 وَعْدَ, 30:6 وَعْدَهُۥ, 30:60 وَعْدَ

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

## ECHO ع د د (root_000989): for 30:6 وَعْدَ, 30:6 وَعْدَهُۥ, 30:11 يُعِيدُهُۥ, 30:27 يُعِيدُهُۥ, 30:60 وَعْدَ: withheld observed target; not identity

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

## ECHO ع و م (root_001063): for 30:6 وَعْدَ, 30:6 وَعْدَهُۥ, 30:60 وَعْدَ: withheld observed target; not identity

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

## خ ل ف (root_000433): 30:6 يُخْلِفُ, 30:22 وَٱخْتِلَٰفُ

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

## ك ث ر (root_001286): 30:6 أَكْثَرَ, 30:8 كَثِيرًا, 30:9 أَكْثَرَ, 30:30 أَكْثَرَ, 30:42 أَكْثَرُهُم

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

## ء ن س (root_000059): 30:6 ٱلنَّاسِ, 30:8 ٱلنَّاسِ, 30:30 ٱلنَّاسَ, 30:30 ٱلنَّاسِ, 30:33 ٱلنَّاسَ, 30:36 ٱلنَّاسَ, 30:39 ٱلنَّاسِ, 30:41 ٱلنَّاسِ, 30:58 لِلنَّاسِ

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

## ع ل م (root_001040): 30:6 يَعْلَمُونَ, 30:7 يَعْلَمُونَ, 30:22 لِّلْعَٰلِمِينَ, 30:29 عِلْمٍ, 30:30 يَعْلَمُونَ, 30:34 تَعْلَمُونَ, 30:54 ٱلْعَلِيمُ, 30:56 ٱلْعِلْمَ, 30:56 تَعْلَمُونَ, 30:59 يَعْلَمُونَ

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

## ظ ه ر (root_000970): 30:7 ظَٰهِرًا, 30:18 تُظْهِرُونَ, 30:41 ظَهَرَ

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

## ح ي ي (root_000383): 30:7 ٱلْحَيَوٰةِ, 30:19 ٱلْحَىَّ, 30:19 ٱلْحَىِّ, 30:19 وَيُحْىِ, 30:24 فَيُحْىِۦ, 30:40 يُحْيِيكُمْ, 30:50 يُحْىِ, 30:50 لَمُحْىِ

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

## ح ي و (root_005544): documented alternative for 30:7 ٱلْحَيَوٰةِ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## ء خ ر (root_000019): 30:7 ٱلْءَاخِرَةِ, 30:16 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## غ ف ل (root_001097): 30:7 غَٰفِلُونَ

- **B001** dalgınlıkla gözden kaçırma — bir şeyi dalgınlıkla gözden kaçırmak · dikkatsizlikten doğan dalgınlık · dalgın, dikkati uyanık olmayan kimse
  غفلت عن الشيء غفلة وغفولا إذا تركته ساهيا (maqayis)؛ غفل يغفل غفلفة وغفولا (ayn)؛ غفل عن الشيء يغفل غفلة وغفولا (sihah)؛ الغفلة سهو يعتري الإنسان من قلة التحفظ والتيقظ (mufradat)
- **B002** bilerek eksik bırakma — farkında olduğu halde bilerek bırakmak · yazının ayırt edici noktalarını koymamak · içini inançtan yoksun bırakmak ya da gerçekleri fark edemez kılmak
  وأغفلته إذا تركته على ذكر منك له (maqayis)؛ وأغفلت الشيء تركته غفلا وأنت له ذاكر (ayn)؛ وأغفلت الشيء إذا تركته على ذكر منك (sihah)؛ إغفال الكتاب تركه غير معجم، تركناه غير مكتوب فيه الإيمان (mufradat)
- **B003** birini bir şeye karşı dikkatsiz kılma — içini inançtan yoksun bırakmak ya da gerçekleri fark edemez kılmak · bir başkasına onu fark ettirmemek
  وأغفله عنه غيره (sihah)؛ جعلناه غافلا عن الحقائق (mufradat)
- **B004** bilerek görmezden gelme — bilerek görmezden gelme
  ربما كان عن عمد (maqayis)؛ التغافل التعمد (ayn)
- **B005** dalgınlığından yararlanarak kandırma — dalgınlığından yararlanıp kandırmak · onun dalgınlığını fırsat bilmek
  التغفل ختل عن غفلة (ayn)؛ تغافلت عنه وتغفلته إذا اهتبلت غفلته (sihah)
- **B006** ayırt edici izi bulunmama — yön belirtisi ve bayındırlık izi bulunmayan arazi · damgasız hayvan · damgasız dişi deve · yön belirtisi olmayan yol · işaretsiz, uzak ve ıssız düzlük · işlenmemiş ölü araziler
  لكل ما لا معلم له غفل، أرض غفل لا علم بها، وناقة غفل لا سمة عليها (maqayis)؛ الغفل سبسب متيه بعيد لا علامة فيها، وطريق غفل لا علامة فيه، ودابة غفل لا سمة عليها (ayn)؛ الأغفال الموات، أرض غفل لا علم بها ولا أثر عمارة، أرض غفل لم تمطر، ودابة غفل لا سمة عليها (sihah)؛ أرض غفل لا منار بها (mufradat)
- **B007** deneyimsiz ya da kavrayışsız kimse — deneyimsiz veya değeri bilinmeyen adam · kavrayışı kıt kimse
  رجل غفل لم يجرب الأمور (maqayis;sihah)؛ المغفل من لا فطنة له، ورجل غفل ليس يعرف ما عنده، لا يعرف له حسب (ayn)؛ رجل غفل لم تسمه التجارب (mufradat)
- **B008** kendini göz önünden uzak tutma — kendisini insanlar arasında saklayıp adını duyurmamak
  غفل فلان نفسه أي كتمها في الناس ولم يشهرها (ayn)
- **B009** iyiliği de kötülüğü de beklenmeyen bağlı kimse — ne iyiliği umulan ne kötülüğünden korkulan bağlı kimse · bağlanıp etkisiz duruma gelmek
  الغفل المقيد لا يرجى خيره ولا يخشى شره وقد اغتفل والجميع الأغفال (ayn)
- **B010** alt dudak altındaki sakal tutamının iki yanı — alt dudak altındaki küçük sakal tutamının iki yanı
  والمغفلة التي في الحديث جانبا العنفقة (sihah)

## ف ك ر (root_001172): 30:8 يَتَفَكَّرُوا۟, 30:21 يَتَفَكَّرُونَ

- **B001** bir şeyi akıl yoluyla zihinde evirip çevirerek inceleme — düşünme; zihinsel inceleme · düşünce; zihinsel inceleme gücü · derinlemesine düşünme ve inceleme · düşünme; zihinde tartma · işi üzerine düşünüp tartmak · düşünüp değerlendirmek · bir şey üzerine düşünüp incelemek · çok düşünen; düşünmeye düşkün · düşünce anlamındaki seyrek bir ad
  تردد القلب في الشيء (maqayis)؛ الفكر اسم التفكر والفكرة والفكر واحد (ayn)؛ التفكر التأمل والاسم الفكر والفكرة (sihah)؛ التفكر اسم للتفكير وكل ذلك معناه واحد (tahdhib)؛ الفكرة قوة مطرقة للعلم إلى المعلوم والتفكر جولان تلك القوة بحسب نظر العقل (mufradat)؛ رجل فكير كثير الفكر (maqayis)؛ رجل فكير كثير التفكر (ayn;sihah)؛ رجل فكير كثير الإقبال على التفكر والفكرة (tahdhib)؛ رجل فكير كثير الفكرة (mufradat)
- **B002** bu işte bir gereksinimim yok [kalıp] — bu işte bir gereksinimim yok
  يقال ليس لي في هذا الأمر فكر أي ليس لي فيه حاجة؛ الفتح فيه أفصح من الكسر

## ن ف س (root_001533): 30:8 أَنفُسِهِم, 30:9 أَنفُسَهُمْ, 30:21 أَنفُسِكُمْ, 30:28 أَنفُسِكُمْ, 30:28 أَنفُسَكُمْ, 30:44 فَلِأَنفُسِهِمْ

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

## خ ل ق (root_000434): 30:8 خَلَقَ, 30:11 ٱلْخَلْقَ, 30:20 خَلَقَكُم, 30:21 خَلَقَ, 30:22 خَلْقُ, 30:27 ٱلْخَلْقَ, 30:30 لِخَلْقِ, 30:40 خَلَقَكُمْ, 30:54 خَلَقَكُم, 30:54 يَخْلُقُ

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

## س م و (root_000745): 30:8 ٱلسَّمَٰوَٰتِ, 30:8 مُّسَمًّى, 30:18 ٱلسَّمَٰوَٰتِ, 30:22 ٱلسَّمَٰوَٰتِ, 30:24 ٱلسَّمَآءِ, 30:25 ٱلسَّمَآءُ, 30:26 ٱلسَّمَٰوَٰتِ, 30:27 ٱلسَّمَٰوَٰتِ, 30:48 ٱلسَّمَآءِ

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

## ECHO و س م (root_001650): for 30:8 ٱلسَّمَٰوَٰتِ, 30:8 مُّسَمًّى, 30:18 ٱلسَّمَٰوَٰتِ, 30:22 ٱلسَّمَٰوَٰتِ, 30:24 ٱلسَّمَآءِ, 30:25 ٱلسَّمَآءُ, 30:26 ٱلسَّمَٰوَٰتِ, 30:27 ٱلسَّمَٰوَٰتِ, 30:48 ٱلسَّمَآءِ: withheld observed target; not identity

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

## ب ي ن (root_000170): 30:8 بَيْنَهُمَآ, 30:9 بِٱلْبَيِّنَٰتِ, 30:21 بَيْنَكُم, 30:47 بِٱلْبَيِّنَٰتِ

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

## ح ق ق (root_000347): 30:8 بِٱلْحَقِّ, 30:38 حَقَّهُۥ, 30:47 حَقًّا, 30:60 حَقٌّ

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

## ء ج ل (root_000016): 30:8 وَأَجَلٍ

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

## ل ق ي (root_001372): 30:8 بِلِقَآئِ, 30:16 وَلِقَآئِ

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

## ر ب ب (root_000532): 30:8 رَبِّهِمْ, 30:33 رَبَّهُم, 30:33 بِرَبِّهِمْ (also echo for 30:39 رِّبًا, 30:39 لِّيَرْبُوَا۟, 30:39 يَرْبُوا۟)

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

## ر ب و (root_000537): 30:39 رِّبًا, 30:39 لِّيَرْبُوَا۟, 30:39 يَرْبُوا۟ (also echo for 30:8 رَبِّهِمْ, 30:33 رَبَّهُم, 30:33 بِرَبِّهِمْ)

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

## ك ف ر (root_001307): 30:8 لَكَٰفِرُونَ, 30:13 كَٰفِرِينَ, 30:16 كَفَرُوا۟, 30:34 لِيَكْفُرُوا۟, 30:44 كَفَرَ, 30:44 كُفْرُهُۥ, 30:45 ٱلْكَٰفِرِينَ, 30:51 يَكْفُرُونَ, 30:58 كَفَرُوٓا۟

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

## س ي ر (root_000769): 30:9 يَسِيرُوا۟, 30:42 سِيرُوا۟

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

## ن ظ ر (root_001520): 30:9 فَيَنظُرُوا۟, 30:42 فَٱنظُرُوا۟, 30:50 فَٱنظُرْ

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

## ك و ن (root_001332): 30:9 كَانَ, 30:9 كَانُوٓا۟, 30:9 كَانَ, 30:9 كَانُوٓا۟, 30:10 كَانَ, 30:10 وَكَانُوا۟, 30:13 يَكُن, 30:13 وَكَانُوا۟, 30:31 تَكُونُوا۟, 30:32 وَكَانُوا۟, 30:35 كَانُوا۟, 30:42 كَانَ, 30:42 كَانَ, 30:47 وَكَانَ, 30:49 كَانُوا۟, 30:55 كَانُوا۟, 30:56 كُنتُمْ

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

## ع ق ب (root_001033): 30:9 عَٰقِبَةُ, 30:10 عَٰقِبَةَ, 30:42 عَٰقِبَةُ

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

## ش د د (root_000782): 30:9 أَشَدَّ

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

## ق و ي (root_001274): 30:9 قُوَّةً, 30:54 قُوَّةً, 30:54 قُوَّةٍ

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

## ث و ر (root_000210): 30:9 وَأَثَارُوا۟, 30:48 فَتُثِيرُ (also echo for 30:50 ءَاثَٰرِ)

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

## ء ث ر (root_000011): 30:50 ءَاثَٰرِ (also echo for 30:9 وَأَثَارُوا۟, 30:48 فَتُثِيرُ)

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

## ع م ر (root_001044): 30:9 وَعَمَرُوهَآ, 30:9 عَمَرُوهَا

- **B001** yaşam süresi ve yaşamın sürmesi — yaşam süresi · yaşamak, uzun süre yaşamak · yaşam süresini uzatma veya uzun yaşam dileme · uzun yaşayan ya da kendisine uzun yaşam verilen kimse
  يدل على بقاء وامتداد زمان، العمر وهو الحياة (maqayis)؛ عمر الرجل أي عاش زمانا طويلا (sihah)؛ عمر الرجل يعمر عمرا أي عاش، ما يطول من عمر (tahdhib)؛ العمر والعمر اسم لمدة عمارة البدن بالحياة، والتعمير إعطاء العمر (mufradat)
- **B002** yaşamı tanık göstererek ant içme veya yakarma — 
  لعمرك يحلف بعمره أي حياته، عمرك الله أعمرك الله (maqayis)؛ لعمر الله قسمي، عمرك الله سألت الله أن يطيل عمرك (sihah)؛ لعمرك يقول بحياتك، عمرك الله مثل ناشدتك الله (tahdhib)؛ خص القسم بالعمر دون العمر، عمرك الله سألت الله عمرك (mufradat)
- **B003** bir yeri onarıp yaşanır kılma — toprağı işleyip yaşanır kılma · bir yeri onarıp yerleşmek veya yaşanır kılmak · yerleşilmiş ve işler durumda · yerleşilmiş, yapılmış veya bakımlı durumda · birine bir yeri yaşanır kılma görevi vermek · tapınma yerini yapılı tutmak, görmeye gitmek ya da orada kalmak
  عمارة الأرض، يعمرونها وهي عامرة معمورة، استعمر الله تعالى الناس في الأرض ليعمروها (maqayis)؛ عمرت الخراب أعمره عمارة فهو عامر أي معمور، استعمركم فيها جعلكم عمارها (sihah)؛ استعمركم فيها أي أذن لكم في عمارتها، عمر فلان بيتا، دار معمورة (tahdhib)؛ العمارة نقيض الخراب، أعمرته الأرض واستعمرته إذا فوضت إليه العمارة (mufradat)
- **B004** görmeye gitme ve kutsal törene yönelme — tapınma yerini yapılı tutmak, görmeye gitmek ya da orada kalmak · belirli kutsal yere yönelik özel tapınma töreni · görmeye gitme, yönelme veya özel törene katılma · görmeye gelen ya da özel törene yönelen kimse
  اعتمر الرجل إذا أهل بعمرته، رفعه صوته بالتلبية للعمرة (maqayis)؛ العمرة في الحج وأصلها من الزيارة، واعتمره أي زاره (sihah)؛ العمرة مأخوذة من الاعتمار وهو الزيارة، الاعتمار القصد (tahdhib)؛ الاعتمار والعمرة الزيارة التي فيها عمارة الود وجعل في الشريعة للقصد المخصوص (mufradat)
- **B005** baş üstüne konan örtü veya süs — baş üstüne konan örtü, başlık veya süs · başını bezle sarmak · başa konan örtü ya da süs
  العمار كل شيء جعلته على رأسك من عمامة أو قلنسوة أو إكليل أو تاج (maqayis)؛ اعتمر أي تعمم بالعمامة، العمارة كل شيء جعلته على رأسك (sihah)؛ العمار كل شيء علا الرأس من عمامة أو قلنسوة، يقال للمعتم معتمر (tahdhib)؛ العمار ما يضعه الرئيس على رأسه عمارة لرئاسته ريحانا كان أو عمامة (mufradat)
- **B006** bağırış ve karışık gürültü — bağırış, uğultu ve karışık gürültü
  العومرة الصياح والجلبة، اعتمر الرجل إذا أهل بعمرته وذلك رفعه صوته (maqayis)؛ تركت القوم في عومرة أي في صياح وجلبة، رفعنا له أصواتنا بالدعاء (sihah)؛ تركت القوم في عومرة أي في صياح وجلبة (tahdhib)؛ العومرة صخب يدل على عمارة الموضع بأربابه (mufradat)
- **B007** yeri yaşanır kılan yerleşik topluluk — tapınma yerini yapılı tutmak, görmeye gitmek ya da orada kalmak · büyük yerleşik topluluk, boy veya soy topluluğu · evlerin sakinleri, özellikle görünmeyen varlıklar
  الحي العظيم يسمى عمارة (maqayis)؛ العمارة القبيلة والعشيرة، عمار البيوت سكانها (sihah)؛ العمارة الحي العظيم، عمار المجتمع الأمر اللازم للجماعة (tahdhib)؛ العمارة أخص من القبيلة وهي اسم لجماعة بهم عمارة المكان (mufradat)
- **B008** yaşam boyu kullanıma bağlı karşılıksız verme — yaşam boyu kullanım için karşılıksız verilen mal · bir evi yaşam süresince kullanmak üzere vermek
  أعمرته دارا أو أرضا أو إبلا، والاسم العمرى (sihah)؛ العمرى أن يقول داري هذه لك عمرك أو عمري (tahdhib)؛ العمرى في العطية أن تجعل له شيئا مدة عمرك أو عمره (mufradat)
- **B009** dişler arasındaki diş eti dokusu — dişler arasındaki diş eti dokusu · dil kökündeki iki küçük kemik
  العمر ما بدا من اللثة وهي العمور (maqayis)؛ العمر واحد عمور الأسنان وهو ما بينها من اللحم (sihah)؛ العمر الواحد من عمور الأسنان، العمرتان عظمان صغيران في أصل اللسان (tahdhib)؛ العمر اللحم الذي يعمر به ما بين الأسنان وجمعه عمور (mufradat)
- **B010** özel adlandırma kümesi — bir palmiye türü, şeker palmiyesi · yaşlı hünnap ağacı
  العمر ضرب من النخل، وربما قالوا العمر (maqayis)؛ العمر نخل السكر، والعمري من السدر القديم (tahdhib)
- **B011** yaratana kulluk ve hizmet etme — 
  لعمرك لدينك الذي تعمر، عمرك الله أي عبادتك الله، عمرت ربي أي عبدته، فلان عامر لربه أي عابد، عمرت ربي وحججته أي خدمته
- **B012** geniş konut, sık dokulu kumaş veya güçlü kişi — sık ve güçlü dokunmuş kumaş · geniş konut veya içinde kalınan yer · güçlü, inancında kararlı ve sakınan kişi
  مكان عمير أي عامر، وثوب عمير أي صفيق، المعمر المنزل الواسع (sihah)؛ المعمر الذي يقام به، رجل عمار قوي الإيمان مأخوذ من العمير وهو الثوب الصفيق النسيج (tahdhib)

## ج ي ء (root_000281): 30:9 وَجَآءَتْهُمْ, 30:47 فَجَآءُوهُم, 30:58 جِئْتَهُم

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

## ج ي ء (root_000282): 30:9 وَجَآءَتْهُمْ, 30:47 فَجَآءُوهُم, 30:58 جِئْتَهُم

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ر س ل (root_000563): 30:9 رُسُلُهُم, 30:46 يُرْسِلَ, 30:47 أَرْسَلْنَا, 30:47 رُسُلًا, 30:48 يُرْسِلُ, 30:51 أَرْسَلْنَا

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

## ظ ل م (root_000967): 30:9 لِيَظْلِمَهُمْ, 30:9 يَظْلِمُونَ, 30:29 ظَلَمُوٓا۟, 30:57 ظَلَمُوا۟

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

## س و ء (root_000755): 30:10 أَسَٰٓـُٔوا۟, 30:10 ٱلسُّوٓأَىٰٓ, 30:36 سَيِّئَةٌۢ

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

## ك ذ ب (root_001290): 30:10 كَذَّبُوا۟, 30:16 وَكَذَّبُوا۟

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

## ء ي ي (root_000074): 30:10 بِـَٔايَٰتِ, 30:16 بِـَٔايَٰتِنَا, 30:20 ءَايَٰتِهِۦٓ, 30:21 ءَايَٰتِهِۦٓ, 30:21 لَءَايَٰتٍ, 30:22 ءَايَٰتِهِۦ, 30:22 لَءَايَٰتٍ, 30:23 ءَايَٰتِهِۦ, 30:23 لَءَايَٰتٍ, 30:24 ءَايَٰتِهِۦ, 30:24 لَءَايَٰتٍ, 30:25 ءَايَٰتِهِۦٓ, 30:28 ٱلْءَايَٰتِ, 30:37 لَءَايَٰتٍ, 30:46 ءَايَٰتِهِۦٓ, 30:53 بِـَٔايَٰتِنَا, 30:58 بِـَٔايَةٍ

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

## ه ز ء (root_001587): 30:10 يَسْتَهْزِءُونَ

- **B001** alay etme; gizli şakayla küçümseme — alay etme; gizli veya şakaya benzer küçümseme · onunla alay etti · onunla alay etmeye yöneldi ya da alay etti · onunla alay etti · alay etme, küçümseyici şaka · alay edilen adam · insanlarla alay eden adam · onu alay ve oyun konusu yaptı · alay etmeye yönelme veya alay etme
  هزىء واستهزأ إذا سخر (maqayis)؛ الهزء السخرية يقال هزيء به واستهزأ به وتهزأ به (ayn)؛ الهزء والهزؤ السخرية ورجل هزءة يهزأ به وهزأة يهزأ بالناس (sihah)؛ الهزء السخرية ورجل هزأة يهزأ بالناس ورجل هزأة يهزأ به (tahdhib)؛ الهزء مزح في خفية وقد يقال لما هو كالمزح (mufradat)
- **B002** alaylarına karşılık ceza verme veya süre verip ansızın yakalama — Tanrı, alaylarına karşılık onları cezalandırır veya süre verip ansızın yakalar
  الله يستهزىء بهم أي يجازيهم على هزئهم بالعذاب فسمي جزاء الذنب باسمه (tahdhib)؛ الاستهزاء من الله في الحقيقة لا يصح وقوله الله يستهزئ بهم أي يجازيهم جزاء الهزؤ (mufradat)؛ أمهلهم مدة ثم أخذهم مغافصة فسمى إمهاله إياهم استهزاء (mufradat)
- **B003** şiddetli soğuğa uğrama veya soğuktan ölme — 
  هزأني البرد أصابني شدته واهتزأت صرت في شدة البرد ويقال إنما هو بالراء (ayn)؛ أهزأه البرد وأهرأه إذا قتله ومثله فيما تعاقب فيه الزاي والراء (tahdhib)
- **B004** binek hayvanını hareket ettirme — binek hayvanını hareket ettirdi
  نزأت الراحلة وهزأتها إذا حركتها (tahdhib)

## ب د ء (root_000090): 30:11 يَبْدَؤُا۟, 30:27 يَبْدَؤُا۟

- **B001** baslatma ve baslangic noktasi yapma — bir seyle baslamak, onu one almak · bir seyi ilk olarak yapmak veya var etmek · baslama ve bir seyi baskasindan once getirme · bir seyin kuruldugu veya meydana geldigi kaynak · bir seyi baslatan veya ilk var edis noktasini kuran
  من افتتاح الشيء يقال بدأت بالأمر وابتدأت من الابتداء (maqayis)؛ بدأت بالشئ بدءا ابتدأت به وبدأت الشئ فعلته ابتداء (sihah)؛ بدأت بكذا وأبدأت وابتدأت أي قدمت والبدء والابتداء تقديم الشيء على غيره ومبدأ الشيء هو الذي منه يتركب أو منه يكون (mufradat)
- **B002** baslatip yeniden yapmak — once baslatir, sonra yeniden yapar · donus ve baslangic halinde yapmak · geldigi yoldan geri donmek · ne baslangic sozu ne de donus sozu soylemek
  والله تعالى المبدئ والبادئ وهو يبدئ ويعيد (maqayis)؛ فعل ذلك عودا وبدءا ورجع عوده على بدئه وما يبدئ وما يعيد (sihah)؛ الله هو المبدئ المعيد ورجع عوده على بدئه وفعل ذلك عائدا وبادئا ومعيدا ومبدئا (mufradat)
- **B003** once gelen ve once baslama hakki — once anilan onde gelen bey · baskalarindan once baslama hakki sende · ilk basta, en basta
  يقال للسيد البدء لأنه يبدأ بذكره (maqayis)؛ البدء السيد الأول في السيادة والبدء والبدئ أيضا الأول ولك البدء والبدأة أي لك أن تبدأ قبل غيرك (sihah)؛ يقال للسيد الذي يبدأ به إذا عد السادات بدء (mufradat)
- **B004** sira disi yeni sey — sasirtici veya sira disi is · sira disi bir sey getirmek · daha once alisilmamis sey
  يقال للأمر العجب بدي كأنه من عجبه يبدأ به (maqayis)؛ البدئ الأمر البديع وقد أبدأ الرجل إذا جاء به (sihah)؛ شيء بديء لم يعهد من قبل كالبديع في كونه غير معمول قبل (mufradat)
- **B005** bir yerden baska yere cikmak [kalıp] — bir yerden baska bir yere cikmak
  أبدأت من أرض إلى أخرى أبدئ إبداء إذا خرجت منها إلى غيرها (maqayis)؛ أبدأت من أرض كذا أي ابتدأت منها بالخروج (mufradat)
- **B006** pay ve buyuk et parcasi — paylasimda ayrilan pay veya hayvan payi · buyuk et parcasi · hayvan payi anlamindaki cogul bicimler
  البدأة النصيب وهو من هذا أيضا لأن كل ذي نصيب فهو يبدأ بذكره (maqayis)؛ البدء والبدأة النصيب من الجزور والجمع أبداء وبدوء (sihah)؛ البدأة النصيب المبدأ به في القسمة ومنه قيل لكل قطعة من اللحم عظيمة بدء (mufradat)
- **B007** parmak eklemleri — cikintili parmak eklemleri
  البدوء مفاصل الأصابع واحدها بدء وأظنه مما همز وليس أصله الهمز وإنما سميت بدوءا لبروزها وظهورها (maqayis)
- **B008** sonradan kazilmis kuyu — sonradan kazilmis, eski olmayan kuyu
  البدء والبدئ البئر التى حفرت في الإسلام وليست بعادية وفي الحديث حريم البئر البدئ خمس وعشرون ذراعا (sihah)
- **B009** ilk ham gorus — ilk beliren, olgunlasmamis gorus
  بادئ الرأي أي ما يبدأ من الرأي وهو الرأي الفطير وقرئ بادي بغير همزة أي الذي يظهر من الرأي ولم يرو فيه (mufradat)
- **B010** dokuntulu hastaliga tutulmak — cicek hastaligi veya kizamik tutmak
  قولهم بدئ فهو مبدوء إذا جدر أو حصب (maqayis)؛ بدئ الرجل يبدأ بدءا فهو مبدوء إذا أخذه الجدري أو الحصبة (sihah)

## ب د ء (root_000091): 30:11 يَبْدَؤُا۟, 30:27 يَبْدَؤُا۟

- **B001** baslatmak ve ilk var etmek — ise basladim · baslamaya girismek · bir seyi baslatan · bir seye ilk baslayan · baslatir ve yeniden yapar · yaratmayi ilk baslatmak
  من افتتاح الشيء يقال بدأت بالأمر وابتدأت من الابتداء؛ المبدئ والبادئ؛ يبدئ ويعيد؛ كيف بدأ الخلق
- **B002** sasilacak sey — saskinlik uyandiran is veya sey
  ويقال للأمر العجب بدي كأنه من عجبه يبدأ به؛ فلا بدي ولا عجيب
- **B003** adi once anilan bey — ustun oldugu icin adi once anilan bey
  ويقال للسيد البدء لأنه يبدأ بذكره؛ ترى ثنانا إذا ما جاء بدأهم
- **B004** once anilan pay — oneminden dolayi once anilan pay
  والبدأة النصيب؛ لأن كل ذي نصيب فهو يبدأ بذكره دون غيره وهو أهمها إليه
- **B005** bir yerden baska yere cikmak [kalıp] — bir yerden baska bir yere cikmak
  وتقول أبدأت من أرض إلى أخرى أبدئ إبداء إذا خرجت منها إلى غيرها
- **B006** cikintili parmak eklemleri — cikintili parmak eklemleri · parmak eklemlerinden biri
  والبدوء مفاصل الأصابع واحدها بدء؛ وأظنه مما همز وليس أصله الهمز؛ سميت بدوءا لبروزها وظهورها

## ع و د (root_001058): 30:11 يُعِيدُهُۥ, 30:27 يُعِيدُهُۥ

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

## ر ج ع (root_000544): 30:11 تُرْجَعُونَ, 30:41 يَرْجِعُونَ

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

## ي و م (root_001700): 30:12 وَيَوْمَ, 30:14 وَيَوْمَ, 30:43 يَوْمٌ, 30:55 وَيَوْمَ, 30:56 يَوْمِ, 30:56 يَوْمُ

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

## ق و م (root_001273): 30:12 تَقُومُ, 30:14 تَقُومُ, 30:21 لِّقَوْمٍ, 30:23 لِّقَوْمٍ, 30:24 لِّقَوْمٍ, 30:25 تَقُومَ, 30:28 لِقَوْمٍ, 30:30 فَأَقِمْ, 30:30 ٱلْقَيِّمُ, 30:31 وَأَقِيمُوا۟, 30:37 لِّقَوْمٍ, 30:43 فَأَقِمْ, 30:43 ٱلْقَيِّمِ, 30:47 قَوْمِهِمْ, 30:55 تَقُومُ

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

## س و ع (root_000760): 30:12 ٱلسَّاعَةُ, 30:14 ٱلسَّاعَةُ, 30:55 ٱلسَّاعَةُ, 30:55 سَاعَةٍ

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

## ب ل س (root_000149): 30:12 يُبْلِسُ, 30:49 لَمُبْلِسِينَ

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

## ج ر م (root_000239): 30:12 ٱلْمُجْرِمُونَ, 30:47 أَجْرَمُوا۟, 30:55 ٱلْمُجْرِمُونَ

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

## ش ر ك (root_000791): 30:13 شُرَكَآئِهِمْ, 30:13 بِشُرَكَآئِهِمْ, 30:28 شُرَكَآءَ, 30:31 ٱلْمُشْرِكِينَ, 30:33 يُشْرِكُونَ, 30:35 يُشْرِكُونَ, 30:40 شُرَكَآئِكُم, 30:40 يُشْرِكُونَ, 30:42 مُّشْرِكِينَ

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

## ش ف ع (root_000802): 30:13 شُفَعَٰٓؤُا۟

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

## ف ر ق (root_001148): 30:14 يَتَفَرَّقُونَ, 30:32 فَرَّقُوا۟, 30:33 فَرِيقٌ

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

## ع م ل (root_001046): 30:15 وَعَمِلُوا۟, 30:41 عَمِلُوا۟, 30:44 عَمِلَ, 30:45 وَعَمِلُوا۟

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

## ص ل ح (root_000876): 30:15 ٱلصَّٰلِحَٰتِ, 30:44 صَٰلِحًا, 30:45 ٱلصَّٰلِحَٰتِ

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

## ر و ض (root_000611): 30:15 رَوْضَةٍ

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

## ح ب ر (root_000287): 30:15 يُحْبَرُونَ

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

## ع ذ ب (root_000994): 30:16 ٱلْعَذَابِ

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

## ح ض ر (root_000333): 30:16 مُحْضَرُونَ

- **B001** gelip yakında hazır bulunma ve görülme — gelmek, hazır bulunmak veya tanık olmak · getirmek veya hazır etmek · birinin yanında veya gözü önünde · bir kişinin yakını ve çevresindeki yer · meclisinde bulunmayan kişileri iyilikle anan
  إيراد الشيء ووروده ومشاهدته (maqayis)؛ الحاضر خلاف الغائب وحضرت القوم إذا شهدتهم (jamhara)؛ الحضرة قرب الشيء وبمحضره (ayn;tahdhib)؛ حضرة الرجل قربه وفناؤه وبمشهد منه (sihah)؛ شهادة مكان أو إنسان ومحضرا مشاهدا معاينا (mufradat)
- **B002** göçebeliğin karşıtı olan yerleşik kent, köy ve kır yaşamı — göçebeliğin karşıtı olan yerleşik yaşam · kentte veya başka bir yerleşimde sürekli oturma · kentler, köyler, yerleşik kır çevresi veya bunların halkı · göçebe değil yerleşim halkından olan
  الحضر خلاف البدو والحاضرة خلاف البادية (maqayis;ayn;tahdhib)؛ الحاضرة المدن والقرى والريف وفلان حضري وفلان بدوي (sihah)؛ الحضر خلاف البدو والحضارة السكون بالحضر (mufradat)
- **B003** su başında bulunma ve otlaktan suya dönüş — topluluğun otlaktan sonra su kaynaklarına döndüğü yer · sürekli bir su kaynağı başında konaklayan · sahiplerinin gelip bulunduğu içme yeri
  محضر القوم مرجعهم إلى المياه بعد النجعة (jamhara;sihah)؛ حي حاضر على ماء عد والمقيم على الماء حاضر (tahdhib)؛ شرب محتضر أي يحضره أصحابه (mufradat)
- **B004** bineğin hızlı koşması veya koşturulması — bineğin koşusu · atın hızla koşması veya koşturulması · çok ve hızlı koşan at
  الحضر الذي هو العدو وأحضر الفرس وفرس محضير (maqayis)؛ الحضر والحضار من عدو الدابة والفعل الإحضار (ayn;tahdhib)؛ أحضر الفرس إذا عدا عدوا شديدا وفرس محضير (jamhara)؛ أحضر الفرس واحتضر أي عدا (sihah)؛ الحضر خص بما يحضر به الفرس إذا طلب جريه (mufradat)
- **B005** biriyle birlikte koşup ona ayak uydurma [kalıp] — bir kişiyle birlikte koşmak veya ona koşuda ayak uydurmak
  حاضرت الرجل إذا عدوت معه (maqayis)؛ حاضرت الرجل محاضرة وحضارا إذا عدوت معه (jamhara)؛ حاضرته حضارا عدوت معه (sihah)
- **B006** hak veya uyuşmazlıkta çekişip üstün gelmeye çalışma — hak veya uyuşmazlıkta çekişme ve karşı tarafı bastırma
  المحاضرة المغالبة وحاضرت الرجل جاثيته عند سلطان أو حاكم (maqayis)؛ أن يحاضرك إنسان بحقك فيذهب به مغالبة ومكابرة (ayn;tahdhib)؛ حاضرته إذا جاثيته عند السلطان أو في خصومة (jamhara;sihah)؛ حاضرته محاضرة وحضارا إذا حاججته (mufradat)
- **B007** hazır bulunan topluluk veya küçük savaş grubu — hazır bulunan büyük topluluk veya boy · birkaç kişilik topluluk veya küçük savaş grubu
  الحاضر الحي العظيم والحضيرة الجماعة ليست بالكثيرة (maqayis)؛ الحاضر اسم جامع والحضيرة ما بين الخمسة إلى العشرة (ayn;jamhara;sihah)؛ الحضور جمع الحاضر والحضيرة جماعة (tahdhib)؛ الحضيرة جماعة من الناس يحضر بهم الغزو (mufradat)
- **B008** yarada biriken irin veya doğum sonrası atılan eş — yarada biriken irin ve akıntı · koyunun doğumdan sonra eşini ve artıkları atması
  الحضيرة ما اجتمع من المدة في الجرح (maqayis)؛ الحضير ما اجتمع من المدة في الجرح وما اجتمع من السخد (ayn;tahdhib)؛ ألقت الشاة حضيرتها ما تلقيه بعد الولد (jamhara;sihah)
- **B009** zararlı bir varlık veya durumun gelip musallat olması — zararlı canlıların üşüştüğü ve kolay bozulan süt · kötücül görünmez varlıkların gelip zarar vermesi · ölüm döşeğine düşmek · kaygının birinin içine çökmesi
  اللبن محضور والكنف محضورة وأن يحضرون أي يصيبوني بسوء (maqayis)؛ اللبن محتضر ومحضور والكنف محضورة وحضره الهم (sihah)؛ حضر المريض واحتضر وحضرني الهم والمحتضر من اللمم والجنون (tahdhib)؛ أن يحضرني الجن وكني عن المجنون بالمحتضر وعمن حضره الموت (mufradat)
- **B010** beyaz veya soylu develer — beyaz veya soylu deve ya da deve topluluğu
  حضار الإبل بيضها (maqayis)؛ الحضار اسم جامع للإبل البيض (ayn;tahdhib)؛ الإبل الحضار البيض (jamhara)؛ الحضار من الإبل الهجان (sihah)
- **B011** güçlü ve iyi yürüyen yol devesi — güçlü, yolculuğa elverişli ve iyi yürüyen dişi deve
  ناقة حضار إذا جمعت قوة ورحلة أي جودة سير (sihah)؛ ناقة حضار إذا جمعت قوة ورحلة يعني جودة المشي وشمر لم يسمع الحضار بهذا المعنى (tahdhib)
- **B012** kent, yer, yıldız ve kabile adları — iki büyük ırmak arasındaki eski bir kent veya kalenin adı · güneyde bulunan bir yerin adı · belirli bir yıldızın adı · bir ülke veya kabilenin adı
  الحضر حصن وحضار كوكب وحضار الإبل بيضها (maqayis)؛ حضار اسم كوكب وحضرموت بلدة (ayn)؛ الحضر موضع وحضور موضع وحضير الكتائب وحضار والوزن نجمان (jamhara)؛ الحضر بلد وحضار نجم وحضور بلد وحضرموت اسم بلد وقبيلة (sihah)؛ الحضر مدينة وحضار كوكب (tahdhib)
- **B013** gel, burada hazır bulun — gel, burada hazır bulun
  حضار أي احضر مثل نزال بمعنى انزل (ayn)؛ يقال حضار بمعنى احضر (tahdhib)
- **B014** biçime bağlı adlandırmalar [kalıp] — yolculuğa elverişli olmayan kişi · iyilik getirerek gelen kişi
  رجل حضر إذا كان لا يصلح للسفر (maqayis)؛ رجل حضر لا يصلح للسفر (sihah)؛ رجل حضر إذا حضر بخير (tahdhib)

## س ب ح (root_000666): 30:17 فَسُبْحَٰنَ, 30:40 سُبْحَٰنَهُۥ

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

## ح ي ن (root_000382): 30:17 حِينَ, 30:17 وَحِينَ, 30:18 وَحِينَ

- **B001** zaman, süre ve gerçekleşme anı — zaman, süre veya çağ · bir şeyi yapma zamanı gelmek veya yaklaşmak · o sırada · zaman zaman; kimi zamanlar · belirli bir zamana kadar · her zaman veya yinelenen her dönemde
  الحين الزمان قليله وكثيره (maqayis)؛ الحين وقت من الزمان (ayn;tahdhib)؛ الحين حقبة من الدهر (jamhara)؛ الحين الوقت؛ الحين أيضا المدة (sihah)؛ الحين وقت بلوغ الشيء وحصوله (mufradat)
- **B002** yok olma veya ölme — yok oluş veya ölüm zamanı · yok olmak veya ölmek · yok olma tehlikesiyle karşı karşıya olan · öldürücü felaket; öldürücü felaketler · onu yok etmek
  للهلاك حين (maqayis)؛ الحين الهلاك؛ حان يحين حينا؛ الحائنة النازلة ذات الحين (ayn;tahdhib)؛ الحين مصدر حان يحين حينا وهو التعرض للهلاك (jamhara)؛ الحين بالفتح الهلاك؛ حان الرجل أي هلك (sihah)؛ الحين عبر به عن حين الموت (mufradat)
- **B003** zaman belirleme ve düzenli aralıklarla yineleme — ona bir zaman belirlemek · deve veya koyuna sağım zamanı belirlemek ya da onu belirli aralıklarla sağmak · belirli aralıklarla işlem yapmak · günde bir öğün
  عاملت فلانا محاينة من الحين؛ حينت الشاة إذا حلبتها مرة بعد مرة؛ حينتها جعلت لها حينا (maqayis)؛ حينت الشيء جعلت له حينا؛ التحيين أن تحلب الناقة في اليوم مرة واحدة (ayn)؛ حينت الناقة إذا جعلت لها في كل يوم وليلة وقتا تحلبها فيه؛ يأكل الحينة أي المرة الواحدة في اليوم والليلة (sihah)؛ التحيين أن تحلب الناقة في اليوم والليلة مرة واحدة؛ إبل محينة؛ يأكل الحينة أي وجبة في اليوم (tahdhib)؛ حينت الشيء جعلت له حينا؛ عاملته محاينة حينا وحينا (mufradat)
- **B004** bir yerde bir süre kalmak — bir yerde bir süre kalmak
  أحينت بالمكان أقمت به حينا (maqayis;mufradat)؛ أحينت بالمكان إذا أقمت به حينا (sihah)
- **B005** uygun zamanı bekleyip kollamak — bir şeyin zamanını beklemek veya onu kollamak
  تحين الوارش إذا انتظر وقت الأكل ليدخل (sihah)؛ تحينت رؤية فلان أي تنظرته (tahdhib)
- **B006** içki satılan yer veya genel satış dükkânı — 
  الحانات المواضع التي يباع فيها الخمر؛ الحانية الخمر منسوبة إلى الحانة؛ الحانوت معروف وأصله حانوة (sihah)

## م س و (root_001425): 30:17 تُمْسُونَ

- **B001** deve ya da kısrağın döl yatağına el sokup er suyunu çıkarma; devede yavruyu da çıkarma — deve ya da kısrağın döl yatağına el sokup er suyunu veya içindekini çıkarma · deve ya da kısrağın döl yatağındaki er suyunu el ile sıyırıp çıkarma · döl yatağındaki er suyunu çıkarma · devenin döl yatağına el sokup yavrusunu ya da içindekini çıkarma · devenin döl yatağına el sokup içindekini çıkarma
  المسي أن يدخل الراعي يده في رحم الناقة يمسط ماء الفحل من رحمها كراهة أن تحمل (maqayis)؛ المسو لغة في المسي وهو إدخال الناتج يده في رحم الناقة أو الرمكة فيمسط ماء الفحل من رحمها (ayn)؛ المسي إخراج النطفة من الرحم؛ مسيت الناقة إذا سطوت عليها وأخرجت ولدها (sihah)؛ المسي لغة في المسو إذا مسط الناقة؛ مسيت الناقة إذا سطوت عليها وهو إدخال اليد في الرحم والمسي استخراج الولد (tahdhib)

## ص ب ح (root_000839): 30:17 تُصْبِحُونَ

- **B001** günün ilk aydınlığı — tan ve günün ilk aydınlığı · günün başı, gecenin karşıtı olan erken gündüz · her günün ilk bölümü · günün ilk bölümüne girme ya da o an · günün ilk bölümüne varılan yer ya da o an
  الصباح نور النهار (maqayis)؛ الصبح والصباح أول النهار (mufradat)؛ الصبح الفجر والصباح نقيض المساء (sihah)؛ الصبح معروف والصبيحة من كل يوم أول النهار (jamhara)؛ صبحني فلان إذا أتاك صباحا والمصبح الموضع الذي يصبح فيه (ayn)
- **B002** günün başında gelmek — ona günün başında geldim ya da o bana günün başında geldi · onlara günün başında su getirdim · günün başına özgü esenlik sözü
  صبحني فلان إذا أتاك صباحا (ayn)؛ صبحته إذا أتيته صباحا وصبحته أي قلت له عم صباحا (sihah)؛ صبحتهم ماء كذا أتيتهم به صباحا (mufradat)
- **B003** günün başındaki içecek ve içme — günün başında içme ya da yeme; o vakitte içilen şey · ona günün başı içeceğini verdim · günün başında içti · günün başı içeceğini içmiş kimse · günün başı içeceğinin verildiği kap · günün başında içmek için kullanılan kadehler · günün başı içeceğinden önce oyalanılan şey
  لشرب الغداة الصبوح والمصابيح الأقداح التي يصطبح بها (maqayis)؛ الصبوح ما يشرب بالغداة وفعلك الاصطباح (ayn)؛ الصبوح الأكل والشرب في أول النهار وصبحت الإبل إذا سقيتها في أول النهار (jamhara)؛ الصبوح الشرب بالغداة وهو خلاف الغبوق (sihah)؛ الصبوح شرب الصباح يقال صبحته سقيته صبوحا والمصباح ما يسقى منه (mufradat)
- **B004** günün başında baskın — günün başındaki baskın günü · savaşta onlara günün başında atla vardık · tehlike anında söylenen yardım çağrısı
  يوم الصباح يوم الغارة (maqayis;sihah)؛ في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا (ayn)
- **B005** ışık veren lamba — lamba, kandil ya da lambalık · lambanın kendisi · onunla ışık yakmak ya da onu yakıt yapmak · gök cisimlerinin ışıkları
  سمي المصباح مصباحا لحمرته (maqayis)؛ الصباح السراج بعينه والمصباح المسرجة (jamhara)؛ المصباح السراج وقد استصبحت به إذا أسرجت والشمع مما يصطبح به أي يسرج به (sihah)؛ يقال للسراج مصباح والمصباح مقر السراج والمصابيح أعلام الكواكب (mufradat)
- **B006** kızılımsı parlak güzellik — kızıllıkla toprak rengi arası renk · kızılımsı ya da açık kestane renkte · güzel ve aydınlık yüzlü · saçtaki güçlü kızıllık · demir ve benzeri şeylerde parlaklık
  أصل واحد وهو لون من الألوان أصله الحمرة ووجه صبيح والصبح شدة حمرة في الشعر (maqayis)؛ الصبحة لون بين الحمرة والغبرة ورجل صبيح الوجه جميله (jamhara)؛ الصباحة الجمال ورجل أصبح وأسد أصبح بين الصبح والأصبح قريب من الأصهب (sihah)؛ الصبح شدة حمرة في الشعر وقيل صبح فلان أي وضؤ (mufradat)
- **B007** günün başı uykusu — günün başında ya da gün aydınlanınca uyuma
  التصبح النوم بالغداة (maqayis;mufradat)؛ الصبحة النوم بالغداة (jamhara)؛ ينام الصبحة أي ينام حين يصبح (sihah)
- **B008** gün doğana dek çöken deve — çökülü yerinden gün başına kadar kalkmayan dişi deve · gün başına kadar çökülü kalan dişi develer
  المصباح الناقة تبرك في معرسها فلا تنبعث حتى تصبح (maqayis)؛ ناقة مصباح والجمع مصابيح وهي التي تصبح في مبركها (jamhara)؛ المصباح الناقة التي تصبح في مبركها ولا ترتعي حتى يرتفع النهار (sihah)؛ من الإبل ما يبرك فلا ينهض حتى يصبح (mufradat)
- **B009** gün başı zaman kalıbı [kalıp] — her günün başında, gelme veya görüşme zamanı olarak · beşinci günün başında · belirli bir gün başında görüşme ya da eylem zamanı
  أتيته أصبوحة كل يوم ولقيته ذا صبوح وأتانا لصبح خامسة وصبح خامسة (maqayis)؛ أتيته لصبح خامسة وصبح خامسة وأتيته أصبوحة كل يوم ولقيته صباحا وذا صباح (sihah)
- **B010** bir duruma gelmek — bir duruma geçti, o hale geldi
  الإصباح مصدر أصبح إصباحا مثل قولهم أمسى إمساء (jamhara)؛ أصبح فلان عالما أي صار (sihah)

## ح م د (root_000355): 30:18 ٱلْحَمْدُ

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

## ع ش و (root_001017): 30:18 وَعَشِيًّا

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

## خ ر ج (root_000400): 30:19 يُخْرِجُ, 30:19 وَيُخْرِجُ, 30:19 تُخْرَجُونَ, 30:25 تَخْرُجُونَ, 30:48 يَخْرُجُ

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

## م و ت (root_001454): 30:19 ٱلْمَيِّتِ, 30:19 ٱلْمَيِّتَ, 30:19 مَوْتِهَا, 30:24 مَوْتِهَآ, 30:40 يُمِيتُكُمْ, 30:50 مَوْتِهَآ, 30:50 ٱلْمَوْتَىٰ, 30:52 ٱلْمَوْتَىٰ

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

## ت ر ب (root_000178): 30:20 تُرَابٍ

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

## ب ش ر (root_000120): 30:20 بَشَرٌ, 30:46 مُبَشِّرَٰتٍ, 30:48 يَسْتَبْشِرُونَ

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

## ن ش ر (root_001503): 30:20 تَنتَشِرُونَ

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

## ز و ج (root_000652): 30:21 أَزْوَٰجًا

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

## س ك ن (root_000726): 30:21 لِّتَسْكُنُوٓا۟, 30:38 وَٱلْمِسْكِينَ

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

## ج ع ل (root_000248): 30:21 وَجَعَلَ, 30:48 وَيَجْعَلُهُۥ, 30:54 جَعَلَ, 30:54 جَعَلَ

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

## و د د (root_001634): 30:21 مَّوَدَّةً

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

## ل س ن (root_001355): 30:22 أَلْسِنَتِكُمْ

- **B001** konuşma organı ve söyleyiş gücü — konuşma organı olan dil ve onun söyleyiş gücü · konuşma organı anlamındaki dilin çoğulu · konuşma organı anlamındaki dilin çoğulu
  اللسان معروف وهو مذكر والجمع ألسن (maqayis)؛ اللسان ما ينطق يذكر ويؤنث والألسن والألسنة (ayn)؛ اللسان جارحة الكلام (sihah)؛ اللسان يذكر ويؤنث وجمعه ألسن وألسنة (tahdhib)؛ اللسان الجارحة وقوتها (mufradat)
- **B002** birine sözle sataşma — birine sözle sataşmak veya çıkışmak · bana sözle sataştı veya üzerime geldi
  لسنته إذا أخذته بلسانك (maqayis)؛ لسن فلان فلانا يلسنه أي أخذه بلسانه (ayn)؛ لسنته إذا أخذته بلسانك (sihah)؛ لسنت الرجل ألسنه لسنا إذا أخذته بلسانك (tahdhib)
- **B003** açık ve etkili konuşma yetkinliği — açık, düzgün ve etkili konuşma yetkinliği · açık ve etkili konuşan · daha açık, etkili ve gerekçesi güçlü konuşan
  اللسن جودة اللسان والفصاحة (maqayis)؛ رجل لسن بين اللسن (ayn)؛ اللسن الفصاحة وقد لسن فهو لسن وألسن (sihah)؛ رجل لسن بين اللسن إذا كان ذا بيان وفصاحة (tahdhib)؛ أفصح وأبين كلاما وأقدر على الحجة (mufradat)
- **B004** dil ucunu andıran ince ve uzunca biçim — ucu dil gibi olan; ince ve hafif uzun · ön ucu dil biçiminde, ince ve uzunca ayakkabı · ince ve hafif uzun ayak
  أصل يدل على طول لطيف غير بائن ونعل ملسنة على صورة اللسان وقدم ملسنة فيها لطافة وطول يسير (maqayis)؛ شيء ملسن جعل طرفه كطرف اللسان (ayn)؛ الملسن من النعال الذي فيه طول ولطافة على هيئة اللسان وامرأة ملسنة القدمين (sihah)؛ نعل ملسنة إذا جعل طرف مقدمها كطرف اللسان (tahdhib)
- **B005** dil ucunun kesilmesi — kişinin dil ucunu kesmek · dilinin ucu kesilmiş kişi
  لسن الرجل أي قطع طرف لسانه فهو ملسون (ayn)
- **B006** bir topluluğun dili ve konuşması — bir topluluğun dili ve konuşması · bir topluluğun konuştuğu dil · söz, sözcük, haber veya ileti · topluluk adına konuşan kişi, topluluğun sözcüsü · insanların kişi hakkında söylediği övgü · farklı diller ve konuşma sesleri
  اللسن اللغة ويعبر بالرسالة عن اللسان (maqayis)؛ اللسان الكلام (ayn)؛ يكنى بها عن الكلمة واللسن اللغة لكل قوم لسن (sihah)؛ لكل قوم لسن أي لغة ولسان الناس عليك ثناؤهم ولسان بني عامر الكلمة أو الخبر (tahdhib)؛ لكل قوم لسان ولسن أي لغة واختلاف الألسنة إشارة إلى اختلاف اللغات والنغمات (mufradat)
- **B007** ödünç yavruyla dişi devenin sütünü indirtme — ödünç yavruya süt tattırıp onu uzaklaştırarak dişi devenin sütünü indirtme · bu işlem için ödünç yavru verilen yavrusuz dişi deve
  التلسين أن يعير الرجل الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis)؛ التلسين أن يعير الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis-routing)؛ الخلية من الإبل يقال لها المتلسنة وهو التلسن (tahdhib)
- **B008** iletiyi ulaştırma — iletiyi ulaştırma · o kişiden veya o kişiye haberi benim için ilet · o kişiyle ilgili sözü benim için ilet
  يعبر بالرسالة عن اللسان (maqayis)؛ الإلسان إبلاغ الرسالة وألسني فلانا وألسن لي فلانا كذا أي أبلغ لي (tahdhib)
- **B009** lifi ezip şeritlere ayırarak büküme hazırlama — lifi ezip ince şeritler hâline getirerek büküme hazırlamak · lifi ezip ince şeritlere ayırarak büküme hazırlama
  لسنت الليف إذا مشنته ثم جعلته فتائل مهيأة للفتل ويسمى ذلك التلسين (tahdhib)
- **B010** yalancı — yalancı; kullanımı tartışmalı
  الملسون الكذاب (sihah)؛ يقولون الملسون الكذاب وهذا مشتق من اللسان (maqayis)؛ الملسون الكذاب قال الشيخ لا أعرفه (tahdhib)

## ل و ن (root_001387): 30:22 وَأَلْوَٰنِكُمْ

- **B001** renk — renk · renkler
  سحنة الشيء ... اللون لون الشيء كالحمرة والسواد (maqayis); اللون: هيئة كالسواد والحمرة (sihah); اللون معروف وينطوي على الأبيض والأسود وما يركب منهما (mufradat)
- **B002** tür — tür
  اللون: النوع (sihah)
- **B003** renk verme veya başka renge bürünme — renklendirmek · başka bir renge bürünmek · ham hurmada olgunluk belirtisinin belirmesi
  لونته فتلون (sihah); لون البسر تلوينا إذا بدا فيه أثر النضج (sihah); تلون إذا اكتسى لونا غير اللون الذي كان له (mufradat)
- **B004** huyu değişken olma — bir huyda durmayan
  تلون فلان أختلفت أخلاقه (maqayis); فلان متلون إذا كان لا يثبت على خلق واحد (sihah)
- **B005** belirli bir hurma ağacı türü ve onun hurması — belirli bir hurma ağacı türü · bu türden tek bir hurma ağacı · bu türden hurma ağaçları · bu türden hurma ağacı toplulukları
  اللون جنس من التمر (maqayis); اللينة النخلة منه وأصل الياء فيها واو (maqayis); اللون الدقل وهو ضرب من النخل (sihah); واحدتها لينة ... وتمرها سمين يسمى العجوة (sihah)

## ن و م (root_001568): 30:23 مَنَامُكُم

- **B001** uyku ve uyuma — uyku · uyumak · uyku; uyuma
  منه النوم؛ نام ينام نوما ومناما (maqayis)؛ ينام نوما فهو نائم إذا رقد (ayn;tahdhib)؛ النوم معروف (sihah)؛ المنام النوم (mufradat)
- **B002** çok uyuma ve uykunun bastırması — çok uyuyan · çok uyuyan kimse · uykucu; çok uyuyan · uykusu bastırdı
  نؤوم ونومة كثير النوم (maqayis;mufradat)؛ يا نومان للكثير النوم (ayn;sihah)؛ أخذه نوام إذا جعل النوم يعتريه (sihah)؛ رجل نومان كثير النوم ورجل نومة ينام كثيرا (tahdhib)
- **B003** uyur gibi yapmak — uyur gibi yapmak · uyuma isteğiyle uyur gibi yapmak
  استنام أيضا إذا تناوم شهوة للنوم (ayn)؛ تناوم أرى من نفسه أنه نائم وليس به (sihah)؛ استنام الرجل بمعنى تناوم شهوة للنوم (tahdhib)
- **B004** adı sanı duyulmayan, önemsenmeyen kimse — adı sanı duyulmayan, önemsenmeyen kimse · dalgın, çevresinden habersiz kimse
  رجل نومة خامل لا يؤبه له (maqayis)؛ رجل نومة أيضا أي خامل الذكر (ayn)؛ رجل نومة أي لا يؤبه له (sihah)؛ النومة الخامل الذكر الغامض في الناس (tahdhib)؛ النومة أيضا خامل الذكر (mufradat)؛ رجل نويم ونومة أي مغفل (ayn;tahdhib)
- **B005** güvenip içi rahat etmek — birine ya da bir şeye güvenip içi rahat etmek
  استنام لي فلان إذا اطمأن إليه وسكن (maqayis)؛ استنام فلان إلى فلان إذا أنس به واطمأن إليه (ayn;tahdhib)؛ استنام إليه أي سكن إليه واطمأن (sihah)؛ استنام فلان إلى كذا اطمأن إليه (mufradat)؛ غير نائم أي غير واثق به (tahdhib)
- **B006** uyku örtüsü — uyumak için kullanılan örtü veya tüylü yaygı
  المنامة القطيفة لأنه ينام فيها (maqayis;tahdhib)؛ المنامة ثوب ينام فيه وهو القطيفة (sihah;mufradat)؛ ربما سموا الدكان منامة (sihah)
- **B007** pazarın durgunlaşması veya giysinin eskimesi [kalıp] — pazar durgunlaştı · giysi ya da kürk eskidi
  نامت السوق كسدت (maqayis;sihah;mufradat)؛ نامت السوق وحمقت إذا كسدت (tahdhib)؛ نام الثوب أخلق (maqayis;sihah;tahdhib;mufradat)؛ نام الثوب والفرو إذا أخلق (tahdhib)
- **B008** ölüm, öldürme ve ölü beden — hayvan öldü · onları öldürdü · ölü hayvan
  نامت الشاة وغيرها من الحيوان إذا ماتت؛ فأنيموهم أي اقتلوهم؛ النائمة الميتة؛ النامية الجثة (tahdhib)
- **B009** hareketten sonra durup yerinde kalmak [kalıp] — hareketi kesilip durmak · suyun yerinde durup kalması
  أصل صحيح يدل على جمود وسكون حركة (maqayis)؛ كل شيء سكن فقد نام (tahdhib)؛ ما نامت السماء الليلة مطرا (tahdhib)؛ نام الماء إذا دام وقام ومنامه حيث يقوم (tahdhib)
- **B010** ince kürk — ince kürk
  النيم الفرو الرقيق (ayn)

## ل ي ل (root_001392): 30:23 بِٱلَّيْلِ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ن ه ر (root_001559): 30:23 وَٱلنَّهَارِ

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

## ب غ ي (root_000138): 30:23 وَٱبْتِغَآؤُكُم, 30:46 وَلِتَبْتَغُوا۟

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

## ف ض ل (root_001163): 30:23 فَضْلِهِۦٓ, 30:45 فَضْلِهِۦٓ, 30:46 فَضْلِهِۦ

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

## س م ع (root_000741): 30:23 يَسْمَعُونَ, 30:52 تُسْمِعُ, 30:52 تُسْمِعُ, 30:53 تُسْمِعُ

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

## ر ء ي (root_000531): 30:24 يُرِيكُمُ, 30:37 يَرَوْا۟, 30:48 فَتَرَى, 30:51 فَرَأَوْهُ

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

## ECHO ر و ي (root_000615): for 30:24 يُرِيكُمُ, 30:37 يَرَوْا۟, 30:48 فَتَرَى, 30:51 فَرَأَوْهُ: withheld observed target; not identity

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

## ب ر ق (root_000108): 30:24 ٱلْبَرْقَ

- **B001** parlamak veya parlaklığını göstermek — şimşek parıltısı · gökte şimşek çaktı · parıldayan; şimşekli bulut · parlaklık, parıltı · kılıcını parıldatarak gösterdi · yemeği az yağla parlattı · süslenip kendini gösterdi
  أحدهما لمعان الشيء؛ البرق وميض السحاب؛ كل شيء يتلألأ لونه فهو بارق؛ للسيوف بوارق؛ برقت السماء إذا جاءت ببرق؛ برق وجهه بالدهن؛ برق طعامه بالزيت أو السمن (maqayis)؛ والبروق بيض السحاب؛ كل شيء يتلألا فهو بارق؛ يقال للسيوف بوارق (ayn)؛ برق السيف وغيره يبرق بروقا أي تلألأ؛ والبرق واحد بروق السحاب؛ أبرق الرجل إذا لمع بسيفه؛ برقوا لنا طعاما بزيت أو سمن (sihah)؛ برقت السماء ورعدت؛ أبرق الرجل بسيفه إذا لمع به؛ يقال للسلاح إذا رأيت بريقه رأيت البارقة؛ أبرقت المرأة وبرقت إذا تحسنت وتعرضت (tahdhib)؛ البرق لمعان السحاب؛ برق يقال في كل ما يلمع نحو سيف بارق؛ برق طعامه بزيت (mufradat)؛ الهبرقي الحداد أو الصائغ حتى يبرق (maqayis)
- **B002** şaşkınlık veya korkuyla gözün sabitlenip kırpılmaması ya da korkuyla oynayıp dolaşması [kalıp] — şaşkınlık ya da korkuyla gözünü dikip kırpmamak · gözün şiddetli dikilişle parlayıp sabitlenmesi · gözlerini iyice açıp keskin bakmak
  إذا بقى كالمتحير قيل برق بصره فهو برق فزع مبهوت؛ من قرأ برق البصر فإنه يقول تراه يلمع من شدة شخوصه؛ برق بعينه إذا لألأ من شدة النظر (maqayis)؛ برق بصره فهو برق أي بهت فهو فزع مبهوت؛ تراه يلمع من شدة شخوصه ولا يطرف؛ برق بعينه تبريقا إذا لألأها من شدة النظر (ayn)؛ برق البصر بالكسر إذا تحير فلا يطرف؛ برق البصر بالفتح بريقه إذا شخص؛ برق عينيه تبريقا أوسعهما وأحد النظر (sihah)؛ برق بكسر الراء فمعناه فزع؛ برق بفتح الراء من البريق أي شخص؛ فتح عينيه من الفزع؛ برق فلان بعينيه تبريقا إذا لألأ بهما من شدة النظر؛ البرق الدهش (tahdhib)؛ برق يقال في العين إذا اضطربت وجالت من خوف (mufradat)
- **B003** gürleyip ağır tehdit savurmak [kalıp] — gürleyip ağır tehdit savurmak · gürültüyle gözdağı verip tehdit etmek
  إذا شدد موعد بالوعيد قيل أبرق وأرعد؛ يقال برق ورعد أيضا؛ لتبرق وترعد يعني التهدد (maqayis)؛ إذا اشتد موعد بالوعيد يقال أبرق وأرعد؛ وبرق ورعد لغة (ayn)؛ رعد الرجل وبرق أي تهدد؛ رعدت المرأة وبرقت أي تزينت (sihah)؛ برق الرجل يبرق ورعد يرعد إذا تهدد؛ أبرق وأرعد أي تهدد (tahdhib)؛ برق فلان ورعد وأبرق وأرعد إذا تهدد (mufradat)
- **B004** gerçek karşılığı olmayan belirti vermek — yağmur getirmeyen şimşek · dişi deve gebe olmadığı halde gebelik belirtisi gösterdi · gebe olmadığı halde kuyruğuyla gebelik belirtisi veren dişi deve · gerçek dayanağı olmayan bir şey ortaya attı
  أبرقت الناقة إذا ضربت ذنبها مرة على فرجها ومرة على عجزها فهي بروق ومبرق؛ برق الرجل إذا أتى بشيء لا مصداق له؛ برقت وعرقت أي لوحت بشيء ليس له حقيقة (maqayis)؛ ابرقت الناقة ضربت بذنبها مرة على فرجها ومرة على عجزها (ayn)؛ برق الخلب وهو الذي ليس فيه مطر؛ أبرقت الناقة وبرقت إذا شالت بذنبها وتلقحت وليست بلاقح (sihah)؛ أبرقت الناقة وليست بلاقح؛ ناقة بروق إذا شالت بذنبها؛ برقت أي لوحت بشيء ليس له مصداق (tahdhib)؛ ناقة بروق تلمع بذنبها (mufradat)
- **B005** siyah ile beyazın veya iki rengin karışık görünmesi — siyah beyaz veya iki renkli alacalı · siyah ve beyaz iki lifle bükülmüş ip · siyah beyaz veya iki renkli arazi, göz ya da dişi taşıyıcı · taş, kum ve kili karışık; siyah beyaz arazi veya dağ · sarı ya da beyaz ve siyah çizgili çekirgeler
  الأصل الآخر اجتماع السواد والبياض في الشيء؛ تسمى العين برقاء لسوادها وبياضها؛ البرق مصدر الأبرق من الحبال والجبال؛ البرقاء من الأرض طرائق بقعة فيها حجارة سود تخالطها رملة بيضاء؛ البرقان ما اصفر من الجراد وتلونت فيه خطوط واسود؛ البرقاء من الغنم كالبلقاء من الخيل (maqayis)؛ البرق مصدر الأبرق من الحبال؛ الحبل الذي أبرم بقوة سوداء وقوة بيضاء؛ البرقاء من الأرض طرائق بقعة فيها حجارة سود يخالطها رملة بيضاء؛ البرقانة جرادة تلونت بخطوط صفر وسود (ayn)؛ الأبرق غلظ فيه حجارة ورمل وطين مختلطة؛ كل شيء اجتمع فيه سواد وبياض فهو أبرق؛ العين برقاء (sihah)؛ حبل أبرق لسواد فيه وبياض؛ كل شيئين خلطا من لونين فقد برقا؛ العين برقاء لسواد الحدقة مع بياض الشحمة؛ الجراد إذا كان فيه بياض وسواد برقان (tahdhib)؛ البرقة للأرض ذات حجارة مختلفة الألوان؛ الأبرق الجبل فيه سواد وبياض؛ سموا العين برقاء لذلك (mufradat)
- **B006** bilinen bir kap türü; parlaklığıyla adlandırılan kılıç — bilinen bir kap türü · bu kap türünün çoğulu · çok parlak kılıç veya parlaklığıyla adlandırılan nesne
  يقال للسيف ولكل ما له بريق إبريق؛ والإبريق معروف وهو من الباب (maqayis)؛ والأباريق جمع إبريق (ayn)؛ والإبريق واحد الأباريق فارسي معرب؛ والإبريق أيضا السيف الشديد البريق (sihah)؛ الإبريق إناء وجمعه أباريق؛ الإبريق السيف ها هنا سمي به لبريقه (tahdhib)؛ والبارقة والأبيرق السيف للمعانه؛ والإبريق معروف (mufradat)
- **B007** kalın ipekli kumaş — kalın ipekli kumaş
  والاستبرق: الديباج الغليظ، فارسي معرب (sihah)

## خ و ف (root_000447): 30:24 خَوْفًا, 30:28 تَخَافُونَهُمْ, 30:28 كَخِيفَتِكُمْ

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

## ط م ع (root_000951): 30:24 وَطَمَعًا

- **B001** bir şeyi güçlü umut ve istekle isteme — güçlü umutla isteme ve istenen şeye yönelme · bir şeyi güçlü biçimde isteyip elde etmeyi ummak · bir şeyi umut ve istekle isteme · bir şeyi elde etme umuduyla yapma · bir şeyi güçlü umutla isteyen kişi · çok şey uman ve güçlü istek duyan · güçlü umutla isteme veya umut bağlanan şey
  يدل على رجاء في القلب قوي للشيء (maqayis)؛ طمع طمعا فهو طامع (ayn)؛ طمع فيه طمعا وطماعة وطماعية (sihah)؛ الطمع ضد اليأس (tahdhib)؛ الطمع نزوع النفس إلى الشيء شهوة له (mufradat)
- **B002** başkasında elde etme umudu uyandırma — onda bir şeyi elde etme umudu uyandırdı · heveslendirip karşılık vermeyen kadın · elde edilmesi umulan şey · kötü niyetli kişide uygunsuz beklenti uyandıran yumuşak söz
  أطمعه غيره (ayn;sihah)؛ امرأة مطماع تطمع ولا تمكن (maqayis;ayn;sihah;tahdhib)؛ المطمع ما طمعت فيه (ayn;tahdhib)؛ قول المخاضعة من المرأة المطمعة في الفساد أي مما يطمع ذا الريبة فيها (tahdhib)
- **B003** askere verilen geçim payı — askerlerin geçim payları ve ödenekleri · bir askere verilen geçim payı
  الأطماع أرزاق الجند (ayn)؛ الطمع رزق الجند يقال أمر لهم الأمير بأطماعهم أي بأرزاقهم (sihah)؛ أخذ القوم أطماعهم أي أرزاقهم الواحد طمع (tahdhib)
- **B004** çok şey ummasına şaşma ya da çok şey umar hâle gelme — Bu kişi ne kadar da çok şey umuyor! · O kişi ne kadar da çok şey umuyor!
  لطمعت يا زيد كما يقولون لقضو القاضي هذا عند التعجب (maqayis)؛ إنه لطمع الرجل بضم الميم في التعجب (ayn;tahdhib)؛ طمع الرجل فلان بضم الميم أي صار كثير الطمع (sihah)
- **B005** ağa yerleştirilen çağrıcı kuş — başka kuşları çekmek için ağın ortasına yerleştirilen kuş
  المطمع الطائر الذي يوضع في وسط الشبك ليصاد بدلالته الطيور (tahdhib)

## ن ز ل (root_001492): 30:24 وَيُنَزِّلُ, 30:35 أَنزَلْنَا, 30:49 يُنَزَّلَ

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

## م و ه (root_001458): 30:24 مَآءً

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

## ع ق ل (root_001036): 30:24 يَعْقِلُونَ, 30:28 يَعْقِلُونَ

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

## د ع و (root_000478): 30:25 دَعَاكُمْ, 30:25 دَعْوَةً, 30:33 دَعَوْا۟, 30:52 ٱلدُّعَآءَ

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

## ECHO د ع ع (root_000477): for 30:25 دَعَاكُمْ, 30:25 دَعْوَةً, 30:33 دَعَوْا۟, 30:52 ٱلدُّعَآءَ: withheld observed target; not identity

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

## ك ل ل (root_001315): 30:26 كُلٌّ, 30:32 كُلُّ, 30:50 كُلِّ, 30:58 كُلِّ

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

## ق ن ت (root_001260): 30:26 قَٰنِتُونَ

- **B001** inanç yolunda buyruğa boyun eğerek bağlı kalma — buyruğa uydu, boyun eğdi ve inanç yolundan ayrılmadı · boyun eğerek buyruğa bağlı kalma ve inanç yolunda doğruluk · buyruğa uyan, boyun eğen ve Tanrı'nın buyruğunu yerine getiren · kadın kocasının sözünü dinledi
  أصل صحيح يدل على طاعة وخير في دين؛ كل استقامة في طريق الدين قنوتا (maqayis)؛ القنوت أي الطاعة وقانتون أي مطيعون؛ قنتت المرأة لزوجها أي أطاعته (ayn)؛ القنوت الطاعة (jamhara;sihah)؛ القانت المطيع؛ القانت العابد؛ حقيقة القانت أنه القائم بأمر الله (tahdhib)؛ القنوت لزوم الطاعة مع الخضوع؛ قيل خاضعون وقيل طائعون (mufradat)
- **B002** namazda ayakta ibadet etme — namazda uzun süre ayakta durma · namazda yalnız kulluğa yönelerek uzun süre ayakta kalma · namazda ayakta duran kimse
  قيل لطول القيام في الصلاة قنوت (maqayis)؛ القنوت في الصلاة طول القيام (jamhara)؛ ثم سمى القيام في الصلاة قنوتا؛ أفضل الصلاة طول القنوت (sihah)؛ القنوت في أشياء فمنها القيام؛ طول القيام (tahdhib)؛ طول القنوت أي الاشتغال بالعبادة ورفض كل ما سواه (mufradat)
- **B003** namazda ayakta Tanrı'ya yakarma — namazda ayakta Tanrı'ya yakarma · tek sayılı gece namazının sonunda ayakta yakarma · sabah namazında öne eğilme evresinden sonra yakardı
  القنوت الدعاء في آخر الوتر قائما؛ وهو الدعاء قياما (ayn)؛ قنت شهرا في صلاة الصبح بعد الركوع يدعو؛ المشهور في اللغة أن القنوت الدعاء؛ العبادة والدعاء لله في حال القيام (tahdhib)
- **B004** namazda insan sözü söylemeyip namaza yönelme — namazda insan sözü söylemeyip namaza yönelme · namazda insan sözü söylemeden duran kimse
  سمى السكوت في الصلاة والإقبال عليها قنوتا (maqayis)؛ فالقنوت ها هنا الإمساك عن الكلام في الصلاة (tahdhib)؛ قيل ساكتون ولم يعن به كل السكوت؛ لا يصح فيها شيء من كلام الآدميين (mufradat)

## ه و ن (root_001608): 30:27 أَهْوَنُ

- **B001** yumuşak, ağırbaşlı sakinlik — sakinlik, ağırbaşlılık ve yumuşaklık · ağırbaşlı ve sakin yürümek · ölçülü ve aşırılığa kaçmadan · acele etmeden, sakince · uysal, sakin ve yumuşak huylu
  الهون مصدر الهين في معنى السكينة والوقار؛ هو يمشي هونا؛ تكلم على هينتك؛ رجل هين لين (ayn)؛ الهون: السكينة والوقار؛ يمشي على الأرض هونا؛ قوم هينون لينون؛ امش على هينتك أي على رسلك (sihah)؛ تذلل الإنسان في نفسه لما لا يلحق به غضاضة؛ يمشون على الأرض هونا؛ المؤمن هين لين (mufradat)؛ أصيل يدل على سكون أو سكينة أو ذل؛ الهون السكينة والوقار (maqayis)
- **B002** kolay ve hafif olma — kolaylık ve yükün hafifliği · birine kolay ve hafif gelmek · onun için kolaylaştırıp hafifletmek · kolay, hafif ve güç olmayan · daha kolay ve daha hafif
  الهون: مصدر هان عليه الشيء أي خف؛ هونه الله عليه أي سهله وخففه؛ شيء هين أي سهل (sihah)؛ هان الأمر على فلان: سهل؛ هو علي هين؛ وهو أهون عليه؛ وتحسبونه هينا (mufradat)؛ الهين: الأمر الهين وهو من الواو وقد مر (maqayis)
- **B003** küçümsenmeden doğan aşağılanma ve onur kaybı — aşağılanma, değersizlik ve güçsüzlük · küçümsenmeden doğan aşağılanma ve küçük düşürülme · değersizlik, küçük düşmüşlük ve güçsüzlük · insanlarca değersiz ve saygıya layık görülmeyen · onu aşağılayıp küçük düşürmek · onu hor görüp değersiz saymak · onu küçümseyerek önemsememek · aşağılayıcı ve küçük düşürücü ceza · aşağılayan ve küçük düşüren
  الهون هوان الشيء الحقير؛ الهين الذي لا كرامة له؛ أهنت فلانا وتهاونت به واستهنت به (ayn)؛ الهون بالضم: الهوان؛ أهانه: استخف به؛ الهوان والمهانة؛ ذل وضعف؛ استهان به وتهاون به: استحقره (sihah)؛ الهوان من جهة متسلط مستخف به؛ عذاب الهون؛ عذاب مهين؛ من يهن الله (mufradat)؛ الهون: الهوان (maqayis)
- **B004** içinde ya da kendisiyle dövme yapılan araç — içinde ya da kendisiyle dövme yapılan araç
  الهاون: الذي يدق فيه، معرب، وكان أصله هاوون (sihah)؛ الهاوون: فاعول من الهون، ولا يقال هارون (mufradat)؛ الهاوون للذي يدق به عربي صحيح كأنه فاعول من الهون (maqayis)

## ECHO م ه ن (root_001453): for 30:27 أَهْوَنُ: withheld observed target; not identity

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

## ECHO و ه ن (root_001687): for 30:27 أَهْوَنُ: withheld observed target; not identity

- **B001** gücün veya kararlılığın azalması ya da azaltılması — güçsüzlük; zayıflık · güçsüzleşmek; zayıflamak · onu güçsüzleştirmek · gücünü azaltmak; zayıflatmak · güçsüzleştirme · güçsüz; gevşek · güçsüzleşmiş; bedence zayıflamış · güçsüzlük üstüne güçsüzlük; giderek artan güçsüzlük · düzenin etkisini kıran; düzeni zayıflatan
  وهن الشيء يهن وهنا: ضعف، وأوهنته أنا (maqayis)؛ الوهن الضعف في العمل وفي الأشياء وكذلك في العظم ونحوه (ayn;tahdhib)؛ الوهن: الضعف، وقد وهن الإنسان ووهنه غيره، يتعدى ولا يتعدى (sihah)؛ فما فتروا وما جبنوا عن قتال عدوهم (tahdhib)؛ الوهن: ضعف من حيث الخلق أو الخلق، موهن كيد الكافرين (mufradat)
- **B002** gecenin ortası dolaylarında geçen saat — gecenin ortası dolaylarında geçen saat · gecenin ortası dolaylarındaki saat · gecenin o saatine girdi veya o saatte yol aldı · ona gecenin o saatinde rastladım
  الوهن الموهن: ساعة تمضي من الليل، وأوهن الرجل: صار أو سار في تلك الساعة (maqayis)؛ الوهن: نحو من نصف الليل، والموهن مثله، هو حين يدبر الليل، وقد أوهنا: صرنا في تلك الساعة (sihah)؛ الموهن والوهن: نحو من نصف الليل، أوهن الرجل: دخل في ساعة من الليل (tahdhib)
- **B003** alt kaburga, omuz damarı ya da devenin köprücük kemiği — en kısa ya da en alttaki kaburga · omuz bağı altından omuza uzanan damar veya bölge · devenin iki köprücük kemiği
  الواهنة: القصيري من الأضلاع، وهي أسفلها (maqayis;sihah)؛ الواهن: عرق مستبطن حبل العاتق إلى الكتف (tahdhib)؛ الواهنتان: عظمان في ترقوة البعير، والترقوة من البعير: الواهنة (tahdhib)
- **B004** boyun yanı, üst kol veya omuz başındaki özel ağrı — boyun yanı, üst kol veya omuz başındaki özel ağrı · bu özel ağrıya tutulmuş · omuz çevresindeki özel ağrıdan etkilenmiş
  الواهنة: داء يصيب الإنسان في أخدعيه (maqayis)؛ الواهنة: مرض يأخذ في عضد الرجل (tahdhib)؛ به واهنة، وإنه ليشتكي واهنته، أوهنه الله فهو موهون (tahdhib)
- **B005** az hareketli, ağır ve ağırdan alan kadın — az hareketli, kalkıp oturması ağır, ağırdan alan ve işe üşenen kadın
  الوهنانة: المرأة القليلة الحركة، الثقيلة القيام والقعود (maqayis)؛ امرأة وهنانة: فيها فتور وأناة (sihah)؛ الوهنانة من النساء: الكسلى عن العمل تنعما، التي فيها فترة (tahdhib)
- **B006** yoğun deve topluluğu [kalıp] — yoğun deve topluluğu
  الوهن من الإبل: الكثيف (sihah)
- **B007** ücretli işçinin yanında durup onu çalışmaya teşvik eden kişi — ücretli işçinin yanında durup onu çalışmaya teşvik eden kişi
  الوهين بلغة أهل مضر: رجل يكون مع الأجير في العمل يحثه على العمل (tahdhib)
- **B008** mazeret için uydurulan boş söz [kalıp] — bahane olsun diye asılsız sözler söyledi
  كان وكان وهن بذي هنات، إذا قال كلاما باطلا يتعلل به (tahdhib)
- **B009** leş yiyip ağırlaşarak havalanamama [kalıp] — kuşun leş yiyip ağırlaşması ve havalanamaması
  يقال للطائر إذا ثقل من أكل الجيف فلم يقدر على النهوض: قد توهن توهنا (tahdhib)

## م ث ل (root_001397): 30:27 ٱلْمَثَلُ, 30:28 مَّثَلًا, 30:58 مَثَلٍ

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

## ع ل و (root_001042): 30:27 ٱلْأَعْلَىٰ, 30:40 وَتَعَٰلَىٰ

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

## ح ك م (root_000348): 30:27 ٱلْحَكِيمُ

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

## ض ر ب (root_000906): 30:28 ضَرَبَ, 30:58 ضَرَبْنَا

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

## م ل ك (root_001444): 30:28 مَلَكَتْ

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

## ي م ن (root_001698): 30:28 أَيْمَٰنُكُم

- **B001** uğur ve iyilik getirme, bunları umma — uğur, iyilik artışı ve mutluluk · uğurlu ve iyilik getiren · topluluğuna uğur ve iyilik getirdi · uğur ve iyilik getiren kimse · onu uğurlu sayıp iyilik umdu · onun görüşünü uğurlu sayıp iyilik umuyor · mutluluk ve iyi yazgı sahipleri · mutluluğa ve Tanrı'ya yakınlığa ulaştıran araç sayılan Kara Taş
  واليمن البركة وهو ميمون (maqayis)؛ يمن الرجل فهو ميمون والميمن الذي أتى باليمن والبركة (ayn)؛ اليمن البركة وتيمنت به تبركت (sihah)؛ اليمن نظير البركة ويمن الرجل فهو ميمون (tahdhib)؛ أصحاب اليمين أصحاب السعادات والميامن واستعير اليمين للتيمن والسعادة (mufradat)
- **B002** sağ el ve sağ yön — sağ el veya sağ yön · yanındakileri sağa götür · sağ taraf veya sağ yön · solun karşıtı olan sağ taraf · sağa doğru ilerledi · iki sağ eliyle verdiği azık · sağ eller
  فاليمين يمين اليد (maqayis)؛ واليمين اليد اليمنى والأيمان جمعه (ayn)؛ اليمنة خلاف اليسرة والأيمن والميمنة خلاف الأيسر والميسرة (sihah)؛ يقال لليد اليمنى يمين وأخذ فلان يمينا وأخذ يسارا ويامن بأصحابك (tahdhib)؛ اليمين أصله الجارحة والميمنة ناحية اليمين (mufradat)
- **B003** kutsal tanıklı ant ve söz güvencesi — ant veya kutsal tanıklı söz güvencesi · antlar ve bağlayıcı sözler · Tanrı adına ant olsun · senin adına ant olsun · Tanrı adına edilen ant · Tanrı adına ant olsun diyen kısaltılmış söz
  واليمين الحلف (maqayis)؛ واليمين من القسم والأيمان جماعته وأيمن حرف وضع للقسم (ayn)؛ اليمين القسم الجمع أيمن وأيمان وأيمن الله اسم وضع للقسم (sihah)؛ الأصل يمين الله وأيمن الله وليمنك (tahdhib)؛ اليمين في الحلف مستعار من اليد (mufradat)
- **B004** güç, savunma ve güçlü doğruluk dayanağı — güç, yetki veya doğruluğun güçlü tarafı · dinî gerekçe veya doğruluk yönünden · güçle veya doğruluğa dayanarak · güç kullanarak engelledi ve savdı
  اليمين القوة (maqayis)؛ واليمين القوة وعن اليمين من قبل الدين (sihah)؛ باليمين أي بالقوة وقيل بالقوة والحق وتخدعوننا بأقوى الأسباب من قبل الدين (tahdhib)؛ لأخذنا منه باليمين أي منعناه ودفعناه (mufradat)
- **B005** Yemen ülkesi, halkı ve ona aidiyet — Yemen ülkesi veya Yemen yönü · Yemenli veya Yemen'e ait · Yemenli veya Yemen'e ait · Yemenli kadın veya Yemen'e ait dişil varlık · Yemenli kadın veya Yemen yönünden olan · Yemen dokumasından yapılmış örtü · Yemen'e mensup oldu · Yemen yönüne gitti veya Yemen'e vardı
  وكذلك اليمن وهو بلد ورجل يماز وسيف يمان (maqayis)؛ واليمن أرض وجيل من الناس واليمن ما كان على يمين القبلة (ayn)؛ اليمن بلاد للعرب والنسبة إليها يمنى ويمان وتيمن تنسب إلى اليمن واليمنة البردة من برود اليمن (sihah)؛ تيامن القوم وأيمنوا إذا أتوا اليمن وقولهم رجل يمان منسوب إلى اليمن واليمنة ضرب من برود اليمين (tahdhib)
- **B006** antlaşma bağı veya kesin sahiplik bildiren sağ el sözleri — aranda antlaşma bulunan bağlı kişi · kesin sahip olduğum ve tasarrufumda bulunan şey
  ومولى اليمين هو من بينك وبينه معاهدة وملك يميني أنفذ وأبلغ من قولهم في يدي (mufradat)
- **B007** ölmek; mezarda sağ yana yatırılmayla ilişkilendirilen kullanım — öldü; mezarda sağ yanına yatırılmasıyla ilişkilendirilen kullanım
  والتيمن الموت يقال تيمن فلان تيمنا إذا مات والأصل فيه أنه يوسد يمينه إذا مات في قبره (tahdhib)

## ر ز ق (root_000560): 30:28 رَزَقْنَٰكُمْ, 30:37 ٱلرِّزْقَ, 30:40 رَزَقَكُمْ

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

## س و ي (root_000766): 30:28 سَوَآءٌ

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

## ف ص ل (root_001159): 30:28 نُفَصِّلُ

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

## ت ب ع (root_000175): 30:29 ٱتَّبَعَ

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

## ه و ي (root_001609): 30:29 أَهْوَآءَهُم

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

## غ ي ر (root_001119): 30:29 بِغَيْرِ, 30:55 غَيْرَ

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

## ه د ي (root_001583): 30:29 يَهْدِى, 30:53 بِهَٰدِ

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

## ECHO ه د د (root_001580): for 30:29 يَهْدِى, 30:53 بِهَٰدِ: withheld observed target; not identity

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

## ض ل ل (root_000913): 30:29 أَضَلَّ, 30:53 ضَلَٰلَتِهِمْ

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

## و ج ه (root_001630): 30:30 وَجْهَكَ, 30:38 وَجْهَ, 30:39 وَجْهَ, 30:43 وَجْهَكَ

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

## د ي ن (root_000504): 30:30 لِلدِّينِ, 30:30 ٱلدِّينُ, 30:32 دِينَهُمْ, 30:43 لِلدِّينِ

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

## ح ن ف (root_000362): 30:30 حَنِيفًا

- **B001** ayağın içe eğriliği — ayağın içe eğriliği · ayağı içe eğri olan kişi · ayağı içe eğri olan kadın · ayağı içe eğrilmek; ayağını içe eğmek
  الحنف اعوجاج في الرجل إلى داخل (maqayis); الحنف ميل في صدر القدم (ayn;tahdhib); انقلاب القدم حتى يصير ظهرها بطنها (jamhara); الاعوجاج في الرجل وهو أن تقبل إحدى إبهامي رجليه على الأخرى (sihah); الأحنف من في رجله ميل (mufradat)
- **B002** bir yana eğilme veya yönelme — eğilme; bir yana yönelme · bir şeye yönelmek
  أصل مستقيم وهو الميل (maqayis); تحنف فلان إلى الشيء تحنفا إذا مال إليه (ayn;tahdhib); الحنيف المائل من خير إلى شر ومن شر إلى خير (tahdhib); استعير للميل المجرد (mufradat)
- **B003** doğru tek tanrılı inanca yönelen kişi — doğru tek tanrılı inanca yönelip bağlı kalan kişi · hoşgörülü ve dosdoğru tek tanrılı inanç yolu · doğru inanç yolunu arayıp putlardan uzaklaşarak ibadete yönelmek
  الحنيف المائل إلى الدين المستقيم (maqayis); الحنيف المسلم الذي يستقبل قبلة البيت الحرام على ملة إبراهيم (ayn;tahdhib); الحنيف العادل عن دين إلى دين وبه سميت الحنيفية (jamhara); الحنيف المسلم وقد سمي المستقيم بذلك (sihah); اعتزل الأصنام وتعبد (sihah); الحنف ميل عن الضلال إلى الاستقامة (mufradat)
- **B004** kutsal ziyareti yapan ya da dinsel kesim töreninden geçen kişi — kutsal ziyareti yapan ya da dinsel kesim töreninden geçen kişi · kutsal ziyaret ibadetini veya bu inanç yoluna özgü bir töreni yerine getirenler
  كل من حج البيت فهو حنيف (jamhara); يقال اختتن ويقال اعتزل الأصنام وتعبد (sihah); في الجاهلية يقال لمن اختتن وحج البيت حنيف (tahdhib); حنفاء حجاجا (tahdhib); كل من حج أو اختتن حنيفا (mufradat)
- **B005** İslam'a yeni girmiş, eski geçmişi olmayan soy [kalıp] — İslam'a yeni girmiş, eski geçmişi olmayan soy
  حسب حنيف أي حديث إسلامي لا قديم له (ayn;tahdhib)

## ف ط ر (root_001165): 30:30 فِطْرَتَ, 30:30 فَطَرَ

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

## ب د ل (root_000095): 30:30 تَبْدِيلَ

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

## ن و ب (root_001562): 30:31 مُنِيبِينَ, 30:33 مُّنِيبِينَ

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

## ECHO ن ي ب (root_001571): for 30:31 مُنِيبِينَ, 30:33 مُّنِيبِينَ: withheld observed target; not identity

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

## ECHO ن ب ء (root_001464): for 30:31 مُنِيبِينَ, 30:33 مُّنِيبِينَ: withheld observed target; not identity

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

## و ق ي (root_001677): 30:31 وَٱتَّقُوهُ

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

## ص ل و (root_000879): 30:31 ٱلصَّلَوٰةَ

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

## ECHO ص ل ي (root_000880): for 30:31 ٱلصَّلَوٰةَ: withheld observed target; not identity

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

## ش ي ع (root_000836): 30:32 شِيَعًا

- **B001** ardından gitme, uğurlayarak eşlik etme ve arkasına ekleme — ayrılırken ardından gidip uğurlamak · ardından gitmek ve yetişmek · arkadan yetişen · oruç ayının ardından altı gün daha tutmak · selam sizinle olsun · yarın ya da ertesi gün
  شيع فلان فلانا عند شخوصه (maqayis); شيعته عند رحيله (sihah); شيعت فلانا أي خرجت معه لأودعه (tahdhib); المشايع اللاحق (sihah;tahdhib); آتيك غدا أو شيعه أي اليوم الذي بعده (maqayis;sihah;tahdhib); شيعنا شهر رمضان بست من شوال (tahdhib); شاعكم السلام أي تبعكم السلام (tahdhib)
- **B002** yandaş ve destekçiler topluluğu — yandaşlar, yardımcılar ve destekçiler · aynı düşüncede birleşen topluluklar · yanında yer alıp desteklemek · güçlü ve yiğit kişi · malı ona bu işi yapma gücü veriyor · belirli bir yandaş topluluğuna bağlanmak veya bağlı olduğunu ileri sürmek
  الشيعة الأعوان والأنصار (maqayis); شيعة الرجل أتباعه وأنصاره (sihah;tahdhib); كل قوم اجتمعوا على أمر فهم شيعة (tahdhib); الشيعة من يتقوى بهم الإنسان وينتشرون عنه (mufradat); يقال للشجاع المشيع (maqayis;sihah;tahdhib;mufradat); فلان يشيعه على ذلك مال أي يقويه (tahdhib)
- **B003** görünür olup yayılma ve parçalara dağılıp saçılma — haber duyulup yayıldı · haberi veya sırrı yaymak · suyun içinde dağılıp yayılmak · malı topluluk arasında dağıtmak · hayvanın idrarını kesik kesik saçması · dağınık ve ayrı ayrı · sır tutmayıp her şeyi yayan kişi · yayılmış haberler
  شاع الحديث إذا ذاع وانتشر (maqayis); شاع الخبر أي ذاع (sihah); شاع الشيء إذا ظهر وتفرق (tahdhib); قطرة من لبن في الماء فتشيع فيه أي تفرق فيه (tahdhib); شاع القوم انتشروا وكثروا (mufradat); أشاعت الناقة ببولها إذا رمت به وقطعته (sihah;tahdhib); جاءت الخيل شواعي وشوائع متفرقة (tahdhib); أشعت المال بين القوم والقدر في الحي إذا فرقته فيهم (tahdhib)
- **B004** bölünmemiş ortak pay ve ortaklık — bölünmemiş ve ayrılmamış ortak pay · ev veya arazide paydaş olan iki kişi · ev aralarında bölünmemiş ortak maldır
  له سهم شائع إذا كان غير مقسوم (maqayis); سهم مشاع وسهم شائع أي غير مقسوم (sihah); نصيب فلان شائع في جميع هذه الدار ومشاع فيها أي ليس بمقسوم ولا معزول (tahdhib); متشايعان ومشتاعان في دار أو أرض إذا كانا شريكين فيها (tahdhib)
- **B005** ateşe yakıt atarak alevini güçlendirme — ateşe odun atıp alevini güçlendirmek · onu ateşle yakmak · ateşi harlamakta kullanılan ince odun
  شيعت النار في الحطب إذا ألهبتها (maqayis); شيعته بالنار أي أحرقته (sihah); شيعت النار إذا ألقيت عليها حطبا تذكيها به (sihah); شيعت النار تشييعا إذا ألقيت عليها ما تذكيها به (tahdhib); شيعت النار بالحطب قويتها (mufradat)
- **B006** çobanın sürüyü sesle toplaması; çoban borusu ve sesi — çobanın hayvanlara seslenip onları toplaması · çoban borusu veya bu borunun sesi · çoban borusu ya da çağrısı olmadan
  شيع الراعي إبله إذا صاح فيها (maqayis); شايع الراعي بإبله أي صاح بها ودعاها إذا استأخر بعضها (sihah); شايعت بالإبل شياعا إذا دعوتها (tahdhib); صوت بها ليلحق أخراها أولاها (tahdhib); الشياع القصبة التي ينفخ فيها الراعي (maqayis); الشياع صوت مزمار الراعي (sihah;tahdhib); اللهم سقه بلا شياع أي بلا زمارة راع (tahdhib)
- **B007** arkadaş, akran, benzer veya denk — bu, onun benzeri veya dengidir · onların benzerleri, arkadaşları veya akranları
  يصاحب ويقارنه (maqayis); بأمثالهم من الشيع الماضية (sihah); عن أشياعهم يعني عن أصحابهم (sihah); هذا شيع هذا أي مثله (tahdhib)
- **B008** yaklaşık miktar veya izleyen zaman — yaklaşık miktar diye aktarılan tartışmalı kullanım · bir ay ve ona yakın bir süre · yarın ya da ertesi gün
  يقول ناس إن الشيع المقدار في قولهم أقام شهرا أو شيعه والصحيح ما قلته (maqayis); الشيع المقدار يقال أقام فلان شهرا أو شيعه (sihah); لم أره منذ شهر وشيعه أراد ونحوه (tahdhib); قال أبو شيعه أو بعد غد (tahdhib)
- **B009** aslan yavrusu — aslan yavrusu
  زعم ناس أن الشيع شبل الأسد ولم أسمعه من عالم سماعا (maqayis); الشيع أيضا ولد الأسد (sihah); الشيع من أولاد الأسد (tahdhib)
- **B010** doldurma, tamamlama veya artırma — Tanrı sizi selamla doldursun · iyilik senden ayrılmasın · bir şeyi tamamlayan veya artıran unsur · onu doldurdum · yarar sağlamayan, kötü huylu kertenkele
  شاعكم الله بالسلام يشاعكم شيعا أي ملأكم (tahdhib); شاعك الخير أي لا فارقك (tahdhib); كل شيء يكون به تمام الشيء أو زيادته فهو شياع له (tahdhib); شعته أشيعه شيعا إذا ملأته (tahdhib)

## ح ز ب (root_000315): 30:32 حِزْبٍۭ

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

## م س س (root_001423): 30:33 مَسَّ

- **B001** elle dokunup algılama — bir şeye elle dokunmak veya onu dokunarak algılamak · birini bir şeye dokundurmak · dokunma veya karşılıklı değme · duyusal dokunma · oyuncunun ötekinin bedenine dokunmasıyla oynanan oyun
  أصل صحيح واحد يدل على جس الشيء باليد (maqayis)؛ مسست الشيء بيدي مسا (ayn)؛ المس باليد مسسته أمسه مسا (jamhara)؛ مسست الشئ أمسه مسا (sihah;tahdhib)؛ المس كاللمس وفيه إدراك بحاسة اللمس (mufradat)
- **B002** cinsel birleşmeyi dokunma sözüyle anlatma — kadınla cinsel birleşmede bulunmak · cinsel birleşme için kullanılan örtmece · cinsel birleşme için kullanılan karşılıklı dokunma anlatımı
  مس المرأة ومماستها إتيانها (ayn)؛ المماسة كناية عن المباضعة وكذلك التماس (sihah)؛ المس والمسيس جماع الرجل المرأة (tahdhib)؛ كني به عن النكاح والمسيس كناية عن النكاح (mufradat)
- **B003** dokunma imgesiyle anlatılan akıl yitimi — aklını yitirmiş sayılan kimse · onda akıl bozukluğu var · aklını bozacak etkenlere uğradı
  الممسوس الذي به مس كأن الجن مسته (maqayis)؛ رجل ممسوس من الجنون وبه مس (ayn)؛ بفلان مس من جنون (jamhara)؛ الممسوس الذي به مس من جنون (sihah)؛ المس الجنون والعرب تقول رجل ممسوس (tahdhib)؛ كني بالمس عن الجنون (mufradat)
- **B004** iyi ya da kötü bir etkiye uğrama — kişinin zarara uğraması · malında iyi iz ve sonuç bırakma
  إنه لحسن المس في ماله يريد حسن الأثر والمس يكون في الخير والشر (tahdhib)؛ المس يقال في كل ما ينال الإنسان من أذى (mufradat)
- **B005** yakın hısımlık bağı [kalıp] — yakın hısımlık · onunla yakın hısımlığı bulunmak
  الرحم المساسة والماسة القريبة (ayn;tahdhib)؛ بينهما رحم ماسة أي قرابة قريبة (sihah)
- **B006** önemli veya ivedi gereksinim; gerek duyma [kalıp] — önemli ve ivedi gereksinim · ona gerek duymak
  حاجة ماسة أي مهمة وقد مست إليه الحاجة (sihah)
- **B007** el değmiş, az tuzlu ya da susuzluğu gideren su — 
  المسوس من الماء ما نالته الأيدي (maqayis)؛ المسوس من المياه ما نالته الأيدي (ayn)؛ المسوس من الماء الذي بين العذب والملح (sihah)؛ المسوس الذي يمس الغلة فيشفيها وكل ما شفى الغليل (tahdhib)
- **B008** birbirine dokunmama [kalıp] — dokunmak yok; birbirimize dokunmayalım
  لا مساس أي لا مماسة (ayn)؛ لا مساس أي لا أمس ولا أمس (sihah)؛ لا مساس أي لا يمس بعضنا بعضا (tahdhib)
- **B009** karışıp belirsizleşme — işin karışıp kuşkulu veya belirsiz hale gelmesi · bir işteki karışıklık ve belirsizlik
  المسمسة والمسماس اختلاط الأمر واشتباهه (ayn)؛ المسمسة اختلاط الأمر والتباسه والاسم المسماس (sihah)؛ المسمسة اختلاط الأمر واشتباهه (tahdhib)

## ض ر ر (root_000907): 30:33 ضُرٌّ

- **B001** zarar, eksilme ve kötü duruma düşme — zarar, kötü durum · zarar vermek, eksiltmek · zarar, eksilme · yararın karşıtı olan zarar · sıkıntı, süreğen düşkünlük veya kötü yıl · görme yetisini yitirmiş, hasta veya bedeni zarar görmüş adam · hasta veya görme yetisini yitirmiş kadın · görme yetisini yitirmiş topluluk · zarar verme ve zararla karşılık verme yoktur
  الضر ضد النفع (maqayis;tahdhib)؛ الضرر النقصان يدخل في الشيء (ayn;tahdhib)؛ الضر المرض والهزال (jamhara;maqayis)؛ الضر سوء الحال (sihah;mufradat)؛ رجل ضرير ذاهب البصر (ayn;sihah;tahdhib;mufradat)
- **B002** zarar verme ve karşılıklı zararlaşma — zarar verme, karşılıklı zararlaşma · zarar verme ve zararla karşılık verme yoktur · karşı çıkmak veya karşılıklı zarar vermek · kimse zarar vermesin veya zarara uğratılmasın
  الضرير المضارة وأكثر ما يستعمل في الغيرة (maqayis;ayn;sihah;tahdhib)؛ لا ضرر ولا ضرار (tahdhib)؛ ضاررته ضرارا ومضارة إذا خالفته (tahdhib)؛ ولا تضاروهن ولا يضار كاتب ولا شهيد (mufradat)
- **B003** zorunluluk ve mecbur kalma — zorunluluk, mecbur bırakan ihtiyaç · zorunluluk anlamındaki şiir dili biçimi · bir şeye mecbur kalmak · bir şeye mecbur bırakılmış kişi · mecbur bırakan bir ihtiyacı olan adam
  الضرورة اسم لمصدر الاضطرار (ayn;tahdhib)؛ الضرورة والضارورة واحد وهو الاضطرار إلى الشيء (jamhara)؛ اضطر فلان إلى كذا من الضرورة (maqayis;sihah)؛ الاضطرار حمل الإنسان على ما يضره (mufradat)
- **B004** kuma ilişkisi ve eşin üzerine evlenme — kuma, kocasının başka eşi bulunan kadın · aynı erkeğin iki eşi · aynı kocayı paylaşan eşler · eşin üzerine evlenme durumu · eşinin üzerine başka biriyle evlenmek · birden çok eşi olan erkek veya kuması olan kadın
  الضرة امرأة زوجها (sihah)؛ الضرتان امرأتان لرجل واحد (ayn;tahdhib)؛ الضر تزوج المرأة على ضرة (maqayis;jamhara;sihah;tahdhib)؛ رجل مضر ذو ضرائر (maqayis;ayn;sihah;tahdhib;mufradat)
- **B005** sıkıştırıcı yakınlık, darlık ve vadi kıyısı — beni sıkıştıracak kadar yaklaştı · yol topluluğa dar geldi ve onları sıkıştırdı · dar yer · vadinin iki yanı veya kıyısı · yere yakın, alçak bulut
  أضرني إضرارا أي دنا مني دنوا شديدا (ayn;sihah;tahdhib)؛ أضر الطريق بالقوم ضاق بهم ودنا منهم (ayn)؛ مكان ذو ضرار أي ضيق (sihah;tahdhib)؛ ضريرا الوادي جانباه (jamhara;sihah;tahdhib)؛ ضرير الوادي شاطئه الذي ضره الماء (mufradat)
- **B006** belirli kalıplarda toplu et, yağ veya mal kütlesi [kalıp] — memenin eti veya süt bulunan kökü · başparmağın altındaki et yastığı · kalçanın iki yanındaki yağlı bölümler · toplu veya çok miktarda mal ya da deve · çok veya toplu malı olan adam
  ضرة الضرع لحمته (maqayis;ayn;sihah;tahdhib)؛ ضرة الإبهام لحمة تحتها (maqayis;ayn;jamhara;sihah;tahdhib)؛ الضرتان الأليتان شحمتان (ayn;tahdhib)؛ الضرة المال الكثير (sihah;tahdhib)؛ المضر الذي له ضرة من مال (maqayis;ayn;sihah;tahdhib)
- **B007** iç güç, sabır ve dayanıklılık — iç güç ve kalan dayanma gücü · bir şeye sabırla dayanma gücü olan · güçlü, dayanıklı ve geç yorulan dişi deve · at gemin ağızlık parçasını sıkıca kavradı · biraz hızlanarak koştu · görüşünde kurnaz, güçlü ve çareci adam
  الضرير قوة النفس (maqayis)؛ ذو ضرير على الشيء إذا كان ذا صبر عليه ومقاساة (maqayis;sihah;tahdhib)؛ الضرير من الدواب الصبور على كل شيء (sihah)؛ ضريرها شدتها (tahdhib)؛ أضر الفرس على فأس اللجام إذا أزم عليه (maqayis;sihah;tahdhib)؛ رجل ضر أضرار إذا كان داهية في رأيه (tahdhib)
- **B008** belirli olumsuz kalıplarda daha fazlasını sağlamamak [kalıp] — bu adamın yeterliliğini aşacak başka bir adam bulamazsın · onun üstüne bir yük daha eklemez · onun üstüne bir kadın köle daha eklemez · kertenkeleye dayanma sabrını daha fazla artırmaz
  لا يضرك عليه رجل أي لا يزيدك (sihah;tahdhib)؛ ما يضرك عليها جارية أي ما يزيدك (tahdhib)؛ ما يضيرك على الضب صبرا أي ما يزيدك (tahdhib)

## ذ و ق (root_000526): 30:33 أَذَاقَهُم, 30:36 أَذَقْنَا, 30:41 لِيُذِيقَهُم, 30:46 وَلِيُذِيقَكُم

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

## ء ت ي (root_000009): 30:34 ءَاتَيْنَٰهُمْ, 30:38 فَـَٔاتِ, 30:39 ءَاتَيْتُم, 30:39 ءَاتَيْتُم, 30:43 يَأْتِىَ, 30:56 أُوتُوا۟

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

## م ت ع (root_001395): 30:34 فَتَمَتَّعُوا۟

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

## س ل ط (root_000732): 30:35 سُلْطَٰنًا

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

## ك ل م (root_001316): 30:35 يَتَكَلَّمُ

- **B001** anlaşılır konuşma, hitap ve söz alışverişi — anlaşılır konuşma · ona hitap etti · birine söz yöneltme · ona sözle karşılık verdi · bir uzaklaşmadan sonra yeniden karşılıklı konuştuk · seninle konuşan ve senin de konuştuğun kişi · konuşulacak yer · sözünü iyi ve akıcı söyleyen kimse · iyi konuşan adam
  أحدهما يدل على نطق مفهم (maqayis)؛ كلمته أكلمه تكليما وهو كليمى إذا كلمك أو كلمته (maqayis)؛ كليمك الذي يكلمك وتكلمه (ayn;tahdhib)؛ الكليم الذي يكلمك وكلمته تكليما وكلاما (sihah)؛ كالمته إذا جاوبته وتكالمنا بعد التهاجر (sihah)؛ ما أجد متكلما أي موضع كلام والكلماني المنطيق (sihah)؛ رجل تكلامة يحسن الكلام (tahdhib)
- **B002** anlam taşıyan tek söz birimi — anlamlı tek söz veya harf · en az üç sözden oluşan sözler topluluğu · sözler · bütün bir anlatı, şiir veya söylev · Tanrı'nın sözü · Tanrı'nın söylediği söz
  يسمون اللفظة الواحدة المفهمة كلمة والقصة كلمة والقصيدة بطولها كلمة ويجمعون الكلمة كلمات وكلما (maqayis)؛ الكلمة لغة حجازية والكلمة تميمية والجميع الكلم (ayn;tahdhib)؛ الكلام اسم جنس يقع على القليل والكثير والكلم لا يكون أقل من ثلاث كلمات والكلمة أيضا القصيدة بطولها (sihah)؛ الكلمة تقع على الحرف الواحد من حروف الهجاء وتقع على لفظة واحدة مؤلفة من جماعة حروف لها معنى وتقع على قصيدة بكمالها وخطبة بأسرها (tahdhib)؛ كلمة الله وكلام الله وكلم الله وكلمات الله (sihah;tahdhib)
- **B003** yaralama ve yara — yara · yaralar · yaralar · onu yaraladı · yaralayan · yaralanmış · yaralı kişi · yaralılar · yaralama · onları yaralayıp damgalaması
  الأصل الآخر الكلم وهو الجرح والكلام الجراحات وجمع الكلم كلوم (maqayis)؛ الكلم الجرح والجميع الكلوم وكلمته أكلمه كلما وأنا كالم وهو مكلوم أي جرحته (ayn)؛ الكلم الجراحة والجمع كلوم وكلام والتكليم التجريح (sihah)؛ الكلم الجرح والجميع كلوم وكلمته وأنا أكلمه كلما وأنا كالم وهو مكلوم (tahdhib)؛ تكلمهم فسر تجرحهم وتسمهم (sihah;tahdhib)

## ص و ب (root_000889): 30:36 تُصِبْهُمْ, 30:48 أَصَابَ

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

## ECHO ن ص ب (root_001507): for 30:36 تُصِبْهُمْ, 30:48 أَصَابَ: withheld observed target; not identity

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

## ق د م (root_001207): 30:36 قَدَّمَتْ

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

## ي د ي (root_001693): 30:36 أَيْدِيهِمْ, 30:41 أَيْدِى

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

## ECHO ء ي د (root_000071): for 30:36 أَيْدِيهِمْ, 30:41 أَيْدِى: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## ق ن ط (root_001261): 30:36 يَقْنَطُونَ

- **B001** umudu kesmek — bir şeyden, iyilikten ya da Tanrı'nın esirgemesinden umudu kesmek · iyilikten umudu kesme; umutsuzluk · umudunu kesmiş, umutsuz · umudunu kesmiş kimse · umudu kesme, umutsuzluk · insanların Tanrı'nın bağışlayıcılığından umutlarını kesmelerine yol açmak
  تدل على اليأس من الشيء (maqayis)؛ القنوط الإياس (ayn)؛ القنوط اليأس (sihah)؛ القنوط الإياس من الخير (tahdhib)؛ يقنطون الناس من رحمة الله أي يؤيسونهم (tahdhib)؛ القنوط اليأس من الخير (mufradat)

## ب س ط (root_000116): 30:37 يَبْسُطُ, 30:48 فَيَبْسُطُهُۥ

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

## ق د ر (root_001205): 30:37 وَيَقْدِرُ, 30:50 قَدِيرٌ, 30:54 ٱلْقَدِيرُ

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

## ق ر ب (root_001212): 30:38 ٱلْقُرْبَىٰ

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

## ب ن ي (root_000156): 30:38 وَٱبْنَ

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

## ب ن و (root_001959): documented alternative for 30:38 وَٱبْنَ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## س ب ل (root_000672): 30:38 ٱلسَّبِيلِ

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

## خ ي ر (root_000452): 30:38 خَيْرٌ

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

## ر و د (root_000610): 30:38 يُرِيدُونَ, 30:39 تُرِيدُونَ

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

## ر د د (root_000555): 30:43 مَرَدَّ (also echo for 30:38 يُرِيدُونَ, 30:39 تُرِيدُونَ)

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

## ف ل ح (root_001175): 30:38 ٱلْمُفْلِحُونَ

- **B001** yarmak veya kesip ayırmak — bir şeyi yarmak veya kesmek · toprağı sürmek üzere yarmak · toprağı sürmek üzere yarmak · demiri başka bir demirle yarmak veya kesmek · bir uzuvdaki yarıklar
  أصل يدل على شق (maqayis)؛ فلحت الأرض شققتها (maqayis;sihah;tahdhib)؛ فلحت الشيء إذا شققته أو قطعته (jamhara)؛ الحديد بالحديد يفلح أي يشق أو يقطع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)
- **B002** dudakta, özellikle alt dudakta yarık — dudaktaki yarık · alt dudağı yarık olan erkek · dudağında yarık bulunan kadın · dudaktaki yarığın kendisi
  الفلح الشق في الشفة (ayn;tahdhib)؛ الأفلح المشقوق الشفة السفلى (maqayis;jamhara;sihah;tahdhib)؛ امرأة فلحاء وعنترة الفلحاء لفلحة كانت به (maqayis;jamhara;sihah;tahdhib)
- **B003** çiftçi ve toprağı işleme işi — çiftçi, toprağı işleyen kimse · toprağı sürme ve çiftçilik işi
  سمي الأكار فلاحا لأنه يشق الأرض (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الفلاحون الزراعون (ayn)؛ الفلاحة الحراثة أو صناعة الفلاح (jamhara;sihah;tahdhib)
- **B004** çiftçiye benzetilen ücretli taşıyıcı — çiftçiye benzetilerek adlandırılan ücretli taşıyıcı
  الفلاح المكاري وإنما قيل له فلاح تشبيها بالأكار (ayn;tahdhib)؛ وجعله ابن أحمر المكاري (jamhara)
- **B005** iyilik içinde kalma, amaca ulaşma ve kurtuluş — iyilik içinde kalma, başarı ve kurtuluş · iyilik içinde kalma ve başarı · başarmak, amacına ulaşmak veya iyilik elde etmek · dilediğin biçimde yaşa · işinde başarı kazan ve onu kendi başına yürüt · kurtuluşa ve kalıcı iyiliğe yönel · iyilik elde eden başarılı kişi · dünya hayatında kalıcılık, varlık ve saygınlık elde etme · son bulmayan yaşam, yoksulluksuz varlık, aşağılanmayan saygınlık ve bilgisizlikten uzak bilgi · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الأصل الثاني الفلاح البقاء والفوز (maqayis)؛ الفلاح والفلح البقاء في الخير (ayn;tahdhib)؛ الفلح والفلاح البقاء (jamhara)؛ الفلاح الفوز والنجاة والبقاء (sihah)؛ أفلح وأنجح إذا أدرك مطلوبه (jamhara)؛ استفلحي بأمرك أي فوزي أو اظفري بأمرك (maqayis;sihah;tahdhib)؛ الفلاح الظفر وإدراك بغية (mufradat)
- **B006** orucu sürdürmeye güç veren şafak öncesi öğün — şafak öncesi öğün · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الفلاح السحور (maqayis;ayn;sihah;tahdhib)؛ سمي فلاحا لأن الإنسان تبقى معه قوته على الصوم (maqayis)؛ لأن به بقاء الصوم (sihah;tahdhib)؛ سمي السحور الفلاح (mufradat)
- **B007** alışverişi çekici gösterme; yalanla kandırma ve alaya alma — satış ve alışverişi satıcıya ve alıcıya çekici göstermek · satış ve alışverişi satıcıya ve alıcıya çekici göstermek · onları kandırıp gerçeğe aykırı söz söylemek · başkasını daha yüksek bedel vermeye kandırmak için kiracının bedeli artırması · kandırma ve alaya alma
  فلحت للقوم وبالقوم أفلح فلاحة وهو أن يزين البيع والشراء للبائع والمشتري (tahdhib)؛ فلحت بهم تفليحا إذا مكر بهم وقال لهم غير الحق (tahdhib)؛ الفلح النجس وهو زيادة المكتري ليزيد غيره فيغر به (tahdhib)؛ التفليح المكر والاستهزاء (tahdhib)

## م و ل (root_001457): 30:39 أَمْوَٰلِ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ع ن د (root_001052): 30:39 عِندَ

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

## ز ك و (root_000637): 30:39 زَكَوٰةٍ

- **B001** büyüyüp artma — büyümek, artmak ve verim kazanmak · büyüme ve artış · gelişmiş ve artışı belirgin · Tanrı onu büyütüp artırdı · ekin büyüyüp arttı · kişi bolluğa kavuşup rahat yaşadı
  أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)
- **B002** ahlaken arınıp düzgünleşme — arınmak ve düzgünleşmek · temiz, doğru ve kötülükten sakınan · arındırıp düzeltmek · arındırma, düzeltme ve iyiliklerle geliştirme · iç temizliği ve ahlaki düzgünlük · kendini övmek veya sözle temiz saymak · dinen uygun ve sonu zarar vermeyen yiyecek · temizlik ve düzgünlük
  الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)
- **B003** yoksula verilmesi gereken mal payı — yoksullara verilmesi gereken mal payı · malının gereken payını ödemek · malından karşılıksız vermek
  زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)
- **B004** yakışmamak [kalıp] — ona yakışmamak veya durumuna uygun düşmemek
  أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)
- **B005** çift olma — çift veya iki öğeli · tek veya çift · avuçtaki çift mi tek mi · avuçtaki şey için tek-çift söylemek
  الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)

## ض ع ف (root_000909): 30:39 ٱلْمُضْعِفُونَ, 30:54 ضَعْفٍ, 30:54 ضَعْفٍ, 30:54 ضَعْفًا

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

## ف ع ل (root_001167): 30:40 يَفْعَلُ

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

## ECHO ء ب و (root_000007): for 30:40 يَفْعَلُ: withheld observed target; not identity

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ف س د (root_001154): 30:41 ٱلْفَسَادُ

- **B001** bozulma ve bozma — bozulmak; düzgün ve elverişli durumdan çıkmak · bozulma; düzgünlüğün ve dengenin yitmesi · bozulma, bozuk duruma gelme · bozuk, düzgünlüğünü yitirmiş · bozulmuş, bozuk · bozuk kimseler · bozmak, bozuk hâle getirmek · bozma, bozuk hâle getirme · bozan veya bozulmaya yol açan kimse · bozulmayı isteme; düzeltmenin karşıtı yönde davranma · zarar doğuran şey; yararın karşıtı · bir şeyi mahvetmek veya yok etmek · saldırdığı topluluğun gerisini kesip dağıtan askerî birlik
  فسد الشيء يفسد فسادا وفسودا وهو فاسد وفسيد (maqayis;sihah;tahdhib)؛ الفساد نقيض الصلاح (ayn;tahdhib)؛ الفساد خروج الشيء عن الاعتدال (mufradat)؛ أفسدته وأفسده غيره (ayn;sihah;mufradat)؛ أفسد فلان المال وفسد الشيء إذا أباره (tahdhib)؛ الاستفساد خلاف الاستصلاح والمفسدة خلاف المصلحة (sihah)

## ب ر ر (root_000104): 30:41 ٱلْبَرِّ

- **B001** sözü ve işi doğrulukla yerine getirme — sözünde ya da işinde doğru olmak · yeminine sadık kalmak, yeminini bozmamak · yemini doğruluk üzere gerçekleştirmek ya da yemin edenin isteğini yerine getirmek · kabul edilmiş, günaha bulaşmamış hac · şaibesiz, yalansız ve hilesiz satış
  برت يمينه أي صدقت وأبرها أمضاها على الصدق (maqayis;ayn;sihah;tahdhib;mufradat)؛ حج مبرور أي مقبول أو لا يخالطه مأثم (maqayis;ayn;sihah;tahdhib;mufradat)؛ البيع المبرور الذي لا شبهة فيه ولا كذب ولا خيانة (tahdhib)
- **B002** inanç ve davranışta geniş kapsamlı iyilik — doğruluk, iyilik, sakınma ve her türlü iyi işi yapma · yaratana gönüllü biçimde uymak · çok şefkatli, merhametli, nazik ve cömert · iyilikte ileri giden doğru ve iyi kimseler
  البر الصلاح والخير والتقى وفعل كل خير (tahdhib;mufradat)؛ يبر ربه أو خالقه أي يطيعه (maqayis;ayn;sihah;mufradat)؛ البر متضمن للاعتقاد والأعمال (mufradat)
- **B003** ana babaya ve yakınlara sevgiyle iyilik etme — ana babaya geniş ölçüde iyilik etmek, onlara kötü davranmamak · yakınlarla bağı sürdürmek ve onlara iyilik etmek
  هو يبر ذا قرابته وأصله الصدق في المحبة (maqayis)؛ البر البار بذوي قرابته (ayn)؛ بررت والدي والبر خلاف العقوق (sihah)؛ بر رحمه إذا وصله وبروا الآباء والأبناء (tahdhib)؛ بر الوالدين التوسع في الإحسان إليهما وضده العقوق (mufradat)
- **B004** gürültülü seslenme ve gevezelik — koyunu sürme veya yeme çağırma sesi · dille çıkarılan gürültü, çok veya öfkeli konuşma · yararsız yere çok konuşan kimse · neyi neyden ayıramamak; açıklaması kaynaklara göre değişen söz
  البر الصوت بها إذا سيقت ودعاء الغنم إلى العلف (maqayis;tahdhib)؛ البربرة كثرة الكلام والجلبة باللسان أو الصوت (maqayis;ayn;sihah;tahdhib;mufradat)؛ لا يعرف هرا من بر (maqayis;sihah;tahdhib;mufradat)
- **B005** denizin karşıtı olan kara — denizin karşıtı olan kara · çöl, ıssız kır veya açık arazi · karaya çıkmak veya karadan yolculuk etmek
  البر خلاف البحر ونقيض الكن (maqayis;ayn;tahdhib;mufradat)؛ البرية الصحراء والقفار (maqayis;ayn;sihah;tahdhib)؛ أبر الرجل صار في البر أو ركب البر (maqayis;sihah)
- **B006** buğday — buğday · bir buğday tanesi · iri kırılmış buğday veya başak taneleriyle sütten yapılan yemek · toprak bol buğday vermek
  البر الحنطة والواحدة برة (maqayis;ayn;sihah;tahdhib)؛ البربور الجشيش من البر (maqayis;ayn;sihah)؛ البر معروف وأوسع ما يحتاج إليه في الغذاء (mufradat)؛ البرابير طعام من السنبل واللبن (tahdhib)
- **B007** misvak ağacının meyvesi ve benzer çöl ağaçlarının olgun meyvesi — misvak ağacının meyvesi veya benzer bir çöl ağacının olgun meyvesi · misvak ağacının tek bir meyvesi
  البرير حمل الأراك وثمر الأراك (maqayis;ayn;sihah;tahdhib;mufradat)؛ واحدتها بريرة (maqayis;sihah)؛ البرير اسم لما أدرك من ثمر العضاه (maqayis)
- **B008** üstün gelmek ve yenmek — onlara üstün gelmek veya onların üstüne çıkmak · yenme, üstün gelme ve bastırma · koşuda öne geçen veya koşusunda güven veren at
  أبر عليهم أي غلبهم أو علاهم (ayn;sihah;tahdhib)؛ الإبرار الغلبة والقهر (maqayis;tahdhib)؛ الجواد المبر (maqayis;tahdhib)

## ب ح ر (root_000086): 30:41 وَٱلْبَحْرِ

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

## ك س ب (root_001296): 30:41 كَسَبَتْ

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

## ب ع ض (root_000133): 30:41 بَعْضَ

- **B001** parça ve parçalara ayırma — bir şeyin parçası, bölümü veya ondan bir kesim · parçalar, bölümler · bir şeyi parçalara ayırmak · parçalara ayrılmak
  بعض كل شيء طائفة منه (maqayis;ayn;tahdhib)؛ بعض الشيء جزء منه (mufradat)؛ بعض الشيء واحد أبعاضه (sihah)؛ بعض الشيء معروف (jamhara)؛ بعضت الشيء تبعيضا إذا فرقته أجزاء (maqayis;ayn;tahdhib)؛ تبعض الشيء وبعضته أي فرقته (jamhara)؛ بعضته تبعيضا أي جزأته فتبعض (sihah)؛ بعضت كذا جعلته أبعاضا نحو جزأته (mufradat)
- **B002** sivrisinek ve ona bağlı zarar veya bulunma kullanımları — sivrisinek · sivrisinekler, sivrisinek topluluğu veya tahtakurusu · sivrisineğin çok olduğu gece · topluluğa sivrisineklerin zarar vermesi · sivrisineklerden zarar görmüş topluluk · bulundukları yerde sivrisinek olması · sivrisinek bulunan arazi · aşırı küçüklüğü veya olanaksızlığı yüzünden elde edilemeyen şey
  البعوضة وهي معروفة والجمع بعوض (maqayis)؛ البعوض جمع البعوضة وهي المؤذية العاضة في الصيف (ayn)؛ البعوض البق الواحدة بعوضة (sihah)؛ قوم مبعوضون وقد بعض القوم إذا آذاهم البعوض وأبعضوا إذا كان في أرضهم بعوض (tahdhib)؛ البعوض بني لفظه من بعض وذلك لصغر جسمها (mufradat)

## ق و ل (root_001272): 30:42 قُلْ, 30:56 وَقَالَ, 30:58 لَّيَقُولَنَّ

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

## ECHO ق ل ل (root_001251): for 30:42 قُلْ, 30:56 وَقَالَ, 30:58 لَّيَقُولَنَّ: withheld observed target; not identity

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

## ECHO م ر د (root_001413): for 30:43 مَرَدَّ: withheld observed target; not identity

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

## ص د ع (root_000850): 30:43 يَصَّدَّعُونَ

- **B001** sert cisimde yarılma — sert cisimde yarık veya açıklık · bir şeyi yarıp çatlatmak · yarılmak veya çatlamak · çatlayıp yarılmak
  أصل صحيح يدل على انفراج في الشيء (maqayis)؛ الصدع الشق (sihah)؛ الصدع شق في شيء له صلابة (tahdhib)؛ الصدع الشق في الأجسام الصلبة كالزجاج والحديد (mufradat)
- **B002** araziyi kesip geçme veya boyuna uzanan geçit — çölü kesip geçmek · çölü aşan yol gösterici · nehir yatağını yarmak · boylu boyunca uzanan dağ, yol veya vadi
  صدعت الفلاة قطعتها (maqayis;sihah;tahdhib)؛ صدع النهر شقه شقا (tahdhib)؛ جبل صادع ذاهب في الأرض طولا وكذلك سبيل صادع وواد صادع (tahdhib)
- **B003** toprağı yararak çıkan bitki — toprağı yararak çıkan bitki
  الصدع النبات لأنه يصدع الأرض (maqayis)؛ ذات الصدع تتصدع بالنبات (tahdhib)؛ الصدع نبات الأرض لأنه يصدع الأرض فتصدع به (tahdhib)
- **B004** açıkça duyurup ayırarak belirginleştirme — gerçeği açıkça söylemek · açıklayıp görünür kılmak · meseleyi ayırıp kesinleştirmek · hüküm veren ve doğruyla yanlışı ayıran · emredileni açıkça duyurmak
  صدع بالحق إذا تكلم به جهارا (maqayis;sihah;tahdhib)؛ صدعت الشيء أظهرته وبينته (sihah)؛ أظهر ما تؤمر به (tahdhib)؛ يصدع يفرق بين الحق والباطل (tahdhib)؛ صدع الأمر أي فصله (mufradat)
- **B005** topluluğun dağılması veya ayrılmış bölüğü — topluluğun dağılıp ayrılması · deve sürüsü bölüğü veya koyun grubu · deve sürüsü bölüğü ya da koyun ve ceylan grubu · koyunları iki gruba ayırmak · görüş ve eğilim ayrılıkları
  تصدع القوم إذا تفرقوا (maqayis;sihah;tahdhib)؛ الصدعة من الإبل قطعة كالستين (maqayis)؛ الصديع الصرمة من الإبل والفرقة من الغنم (sihah)؛ رأيت بين القوم صدعات أي تفرقا في الرأي والهوى (sihah;tahdhib)؛ يومئذ يصدعون (mufradat)
- **B006** karanlığı yararak beliren sabah — karanlığı yararak beliren sabah
  الصديع الصبح (sihah;tahdhib)؛ الصديع انصداع الصبح (tahdhib)؛ قد انصدع وانفطر وانفلق وانفجر إذا انشق (tahdhib)
- **B007** baş ağrısı — baş ağrısı · başı ağrımak
  الصداع وجع الرأس (sihah;tahdhib)؛ صدع الرجل تصديعا (sihah)؛ الصداع وهو شبه الاشتقاق في الرأس من الوجع (mufradat)
- **B008** genç ve ince yapılı insan; genç ya da orta gelişkinlikte hayvan — genç dağ keçisi · genç, ince yapılı ve düzgün bedenli adam · küçükle büyük arasında dağ keçisi, ceylan veya yaban eşeği
  الصدع الفتي من الأوعال (maqayis;ayn;tahdhib)؛ الرجل الشاب المستقيم القناة (ayn;tahdhib)؛ وعل بين وعلين (sihah;tahdhib)؛ رجل صدع وهو الضرب الخفيف اللحم الشاب (sihah;tahdhib)
- **B009** yeni yama veya yarılmış giysi — eski giyside yeni yama · yarılmış giysi veya üstlük · iki parçaya yarmak
  الصديع رقعة جديدة في ثوب خلق (tahdhib)؛ الرداء الذي شق صدعتين (tahdhib)؛ الصديع الثوب المشقق (tahdhib)
- **B010** bir şeye yönelmek veya birini işten çevirmek [kalıp] — bir şeye meyledip yönelmek · birini bir işten çevirmek
  صدعت إلى الشيء أصدع صدوعا ملت إليه (sihah)؛ ما صدعك عن هذا الأمر أي ما صرفك (sihah)
- **B011** birini veya emredilen şeyi amaçlamak — bir kimseyi amaçlayıp ona yönelmek · emredileni amaçlamak
  اصدع فلانا أي اقصده لأنه كريم (tahdhib)؛ معنى اصدع بما تؤمر أي اقصد بما تؤمر (tahdhib)

## م ه د (root_001451): 30:44 يَمْهَدُونَ

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

## ج ز ي (root_000244): 30:45 لِيَجْزِىَ

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

## ECHO ج ز ز (root_000242): for 30:45 لِيَجْزِىَ: withheld observed target; not identity

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

## ح ب ب (root_000286): 30:45 يُحِبُّ

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

## ر و ح (root_000609): 30:46 ٱلرِّيَاحَ, 30:48 ٱلرِّيَٰحَ, 30:51 رِيحًا

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

## ج ر ي (root_000240): 30:46 وَلِتَجْرِىَ

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

## ف ل ك (root_001177): 30:46 ٱلْفُلْكُ

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

## ش ك ر (root_000810): 30:46 تَشْكُرُونَ

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

## ن ق م (root_001545): 30:47 فَٱنتَقَمْنَا

- **B001** hoşnutsuzlukla yadırgama ve ayıplama — yadırgamak, ayıplamak ve hoşnutsuzluk duymak · yadırgama ve ayıplama · ayıplayıp hoşnutsuzluğunu gösteren kimse · yadırgama ve hoşnutsuzluk
  إنكار شيء وعيبه؛ أنكرت عليه فعله (maqayis)؛ أنكر ولم يرض (ayn)؛ عتبت عليه؛ كرهته (sihah)؛ بالغت في كراهة الشيء؛ النقمة الإنكار (tahdhib)؛ أنكرته إما باللسان وإما بالعقوبة (mufradat)
- **B002** cezalandırarak karşılık verme ve öç alma — cezalandırma, acı çektirme ve öç alma · yaptığı kötülüğe ceza ile karşılık vermek · öldürülen yakınının öcünü almak · öldürülürse onun öcünü almak
  النقمة من العذاب والانتقام؛ فعاقبه (maqayis)؛ انتقمت منه كافأته عقوبة بما صنع (ayn)؛ انتقم الله منه أي عاقبه؛ النقمة (sihah)؛ نقم فلان وتره أي انتقم؛ النقمة العقوبة (tahdhib)؛ النقمة العقوبة (mufradat)

## س ح ب (root_000680): 30:48 سَحَابًا

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

## ك س ف (root_001298): 30:48 كِسَفًا

- **B001** keserek ayırmak — art ayak kirişini kesmek · bir şeyi kesmek · kesme, kesip ayırma · parça parça kesme · hayvanın art ayak kirişini kesmek
  الكسف قطع العرقوب بالسيف، كسفه يكسفه (ayn)؛ الكسف بالفتح مصدر كسفت البعير إذا قطعت عرقوبه، وكذلك كسفت الثوب إذا قطعته، والتكسيف التقطيع (sihah)؛ الكسف قطع العرقوب، وكسفت الثوب أي قطعته، كل شيء قطعته فقد كسفته (tahdhib)؛ كسفت الثوب أكسفه كسفا إذا قطعته قطعا، وقيل كسفت عرقوب الإبل، قال بعضهم هو كسحت لا غير (mufradat)؛ القطع فيقال كسف العرقوب بالسيف كسفا يكسفه (maqayis)؛ كرسفت عرقوب الدابة، وهذا مما زيدت فيه الراء، والأصل كسفت (maqayis-variant)
- **B002** Güneş veya Ay ışığının tutulmayla kaybolması — tutulmak, ışığı kaybolmak · Güneş veya Ay tutulması · ışığını gidermek veya örtmek · yıldızları ışığıyla görünmez kılmak · yıldızların ışığını bastıran · tutulmak; kullanımı tartışmalı biçim
  كسف القمر يكسف كسوفا والشمس تكسف كذلك (ayn)؛ كسفت الشمس تكسف كسوفا، وكذلك كسف القمر (sihah)؛ كسوف القمر وهو زوال ضوئه (maqayis)؛ كسف القمر يكسف كسوفا وكذلك الشمس (tahdhib)؛ كسفت الشمس إذا ذهب ضوءها وكسف القمر إذا ذهب ضوءه (tahdhib)؛ كسفت الشمس تكسف كسوفا إذا اسودت بالنهار، وكسفت الشمس النجوم إذا غلب ضوءها النجوم فلم يبد منها شيء (tahdhib)؛ كسوف الشمس والقمر استتارهما بعارض مخصوص (mufradat)
- **B003** yüzü ve iç dünyası kararıp durumu kötüleşmek — yüzü asık, somurtkan · yüzüne karşı somurtmak · hali kötü, kaygılı · hali kötüleşmek · içine kötü düşünce doğmak veya umudu daralmak · kaygılı, rengi solmuş veya canlılığını yitirmiş
  رجل كاسف الوجه عابس من سوء الحال، كسف في وجهي وعبس كسوفا (ayn)؛ كسفت حال الرجل أي ساءت، ورجل كاسف البال سيئ الحال، وكاسف الوجه أي عابس (sihah)؛ رجل كاسف الوجه إذا كان عابسا، وهو كاسف البال أي سيء الحال (maqayis)؛ كسف الرجل إذا نكس طرفه وكسفت حاله إذا تغيرت (tahdhib)؛ الكسوف في الوجه الصفرة والتغير، ورجل كاسف مهموم تغير لونه وهزل من الحزن، وكسف ذهب نوره وتغير إلى السواد (tahdhib)؛ كسف باله إذا حدثته نفسه بالشر، وكسوف باله أن يضيق عليه أمله (tahdhib)؛ وبه شبه كسوف الوجه والحال فقيل كاسف الوجه وكاسف الحال (mufradat)
- **B004** bir bütünden ayrılmış parça — bir şeyden ayrılmış parça veya bölüm · parçalar veya bölümler · gökten veya buluttan parçalar
  الكسفة قطعة سحاب أو قطعة قطن أو صوف، فإذا كان واسعا كبيرا فهو كسف ولو سقط من السماء جانب فهو كسف (ayn)؛ الكسفة القطعة من الشيء، أعطني كسفة من ثوبك، والجمع كسف وكسف (sihah)؛ الكسف والكسف وجهان، والكسف جماع كسفة، أعطني كسفة يريد قطعة كقولك خرقة (tahdhib)؛ الكسفة قطعة من السحاب والقطن ونحو ذلك من الأجسام المتخلخلة الحائلة، وجمعها كسف (mufradat)؛ الكسفة الطائفة من الثوب، أعطني كسفة من ثوبك، والكسفة القطعة من الغيم (maqayis)؛ يقرأ كسفا جعلها جمع كسفة وهي القطعة (tahdhib)
- **B005** üstten örtmek ve örtücü tabaka oluşturmak — üstten kaplayan bir tabaka
  ومن قرأ كسفا قال أو تسقطها طبقا علينا، واشتقاقه من كسفت الشيء إذا غطيته (tahdhib)

## و د ق (root_001636): 30:48 ٱلْوَدْقَ

- **B001** yaklaşma ve yanında rahatlık duyma — ona alıştı, yanında rahat etti · ona doğru yaklaştı · rahatça gelinen veya durulan yer · bize hiçbir şey sunmadılar, yaklaştırmadılar
  ودقت به إذا أنست به ودقا (maqayis)؛ المودق المأتى والمكان الذي تقف فيه آنسا (maqayis)؛ ودقت إليه دنوت منه (sihah)؛ ودق العير إلى الماء أي دنا منه (sihah;tahdhib)؛ ما ودقوا لنا بشيء أي ما بذلوا وما قربوا لنا شيئا (tahdhib)
- **B002** tırnaklı dişinin çiftleşme isteği ve buna bağlı ıslaklık — çiftleşme isteğindeki tırnaklı dişi · çiftleşme isteğindeki tırnaklı dişi · tırnaklı dişi kızgınlığa geldi ve ıslaklık gösterdi · tırnaklı dişi çiftleşme isteğine girdi · tırnaklı dişi çiftleşme isteğine girdi · tırnaklı dişinin çiftleşme isteği dönemi
  أتان وديق إذا أرادت الفحل وبها وداق (maqayis)؛ كل ذات حافر توصف بالوديق وقد ودقت تودق وداقا أي حرصت على الفحل وأودقت واستودقت (ayn)؛ يقال لذوات الحافر إذا أرادت الفحل ودقت وأودقت واستودقت (sihah;tahdhib)؛ ودقت الدابة واستودقت وأتان وديق وودوق إذا أظهرت رطوبة عند إرادة الفحل (mufradat)
- **B003** yağmur ve gökten düşen damlaları — yağmur; bir yoruma göre yağmur arasındaki tozumsu görünüm · yağmur damladı ve yağdı · yağmur yüklü bulut
  الودق المطر لأنه يدق أي يجيء من السماء (maqayis)؛ الودق المطر كله شديده وهينه (ayn;tahdhib)؛ الودق المطر وقد ودق يدق ودقا أي قطر (sihah)؛ الودق قيل ما يكون من خلال المطر كأنه غبار وقد يعبر به عن المطر (mufradat)؛ فترى الودق يخرج من خلاله (mufradat)
- **B004** gözde kırmızı nokta veya kabarcıkla beliren rahatsızlık — gözdeki kırmızı noktalar veya göz rahatsızlığı · gözdeki kabarcık, kırmızı nokta veya göz ve şakak damarı rahatsızlığı · gözü bu rahatsızlığa tutuldu
  الودق نقط حمر تخرج في العين الواحدة ودقة (maqayis)؛ الودقة داء يأخذ في العين وعروق الصدغ (ayn)؛ في عينه ودقة خفيفة إذا كانت فيها بثرة أو نقطة شرقة بالدم (tahdhib)؛ وقد ودقت عينه تيدق ودقا (tahdhib)
- **B005** iki kat ya da iki yönden gelen ağır tehlike — iki kat şiddetli savaş · iki yönlü büyük bela; tehlikeli yılan veya ağır saplama için niteleme
  حرب ذات ودقين أي شديدة تشبه بسحابة ذات مطرتين شديدتين (ayn;tahdhib)؛ ذات ودقين الداهية أي ذات وجهين كأنها جاءت من وجهين (sihah)؛ يقال للداهية ذات ودقين (tahdhib)؛ ذات ودقين من صفة الحيات ومن صفة الطعنة (tahdhib)
- **B006** öğle vakti kavurucu sıcak ve sıcak hava dalgalanması — öğle vakti kavurucu sıcak veya sıcaktan havada oluşan dalgalanma
  الوديقة حر نصف النهار (ayn;tahdhib)؛ الوديقة شدة الحر (sihah;tahdhib)؛ سميت وديقة لأنها ودقت إلى كل شيء أي وصلت (tahdhib)؛ ما يبدو في الهواء عند شدة الحر وديقة (mufradat)
- **B007** kötülüğün çatışma alanı — kötülüğün çatışma alanı
  المودق معترك الشر (ayn;tahdhib)
- **B008** çok keskin, özellikle kılıç ağzı için — keskin; özellikle ağzı keskin kılıç için
  الوادق الحديد؛ حسام وادق حده (sihah)
- **B009** göbek deliğinin akıp gevşemesi veya çıkıntılı olması [kalıp] — göbek deliği akıp gevşedi · göbek deliği dışarı doğru çıkıntılı
  ودقت سرته تدق ودقا إذا سالت واسترخت؛ رجل وادق السرة شاخصها (tahdhib)

## خ ل ل (root_000435): 30:48 خِلَٰلِهِۦ

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

## ECHO خ ل و (root_000436): for 30:48 خِلَٰلِهِۦ: withheld observed target; not identity

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

## ع ب د (root_000973): 30:48 عِبَادِهِۦٓ

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

## ص ف ر (root_000869): 30:51 مُصْفَرًّا

- **B001** sarı renk ve sararma — sarı renk ve sararma · sarı; sarıya çalan koyu renkli · sarı renk atfedilen Doğu Roma hükümdarları ve halkı · altın ile safran; başka bir açıklamada sarı boya veren bitki ile safran · hastalıktan deriye yayılan sarılık · hastalık yüzünden teni sararmış kimse
  الأصل الأول لون من الألوان؛ الصفرة في الألوان؛ بنو الأصفر؛ الأصفر الأسود (maqayis)؛ الصفار صفرة تعلو اللون والبشرة من داء؛ الصفرة لون الأصفرار؛ ما يصيب المواشي فيغير الخلقة يسمى الصفرة؛ بنو الأصفر (ayn)؛ الصفرة لون الأصفر؛ فرس أصفر؛ بنو الأصفر؛ ربما سمت العرب الأسود أصفر؛ الأصفران الذهب والزعفران (sihah)؛ الصفار صفرة تعلو اللون والبشرة من داء؛ الصفرة لون الأصفر؛ الأصفر الأسود؛ سود الإبل صفرا (tahdhib)؛ الصفرة لون من الألوان التي بين السواد والبياض؛ قد يعبر بها عن السواد (mufradat)
- **B002** boşluk ve yoksunluk — boşalmak, beklenen içerikten yoksun kalmak · eşyasız ev; eli boş kimse · yoksullaşmak, eli boş kalmak · yoksullar, eli boş kimseler · hesapta sıfır işareti · aklı çekilmiş gibi görülen delilik durumu
  الأصل الثاني الشيء الخالي؛ هو صفر؛ ما له صفر إناؤه؛ في صفرة للذي به جنون كأنه خال بين عقله (maqayis)؛ الصفاريت وهم الفقراء والتاء فيه زائدة وإنما هو الصفر وهو الخالي (maqayis)؛ الصفر الشيء الخالي؛ صفر يصفر صفرا وصفورا فهو صفر (ayn)؛ الصفر أيضا الخالي؛ بيت صفر من المتاع؛ رجل صفر اليدين؛ أصفر الرجل فهو مصفر أي افتقر؛ الصفاريت الفقراء (sihah)؛ صفر الإناء من الطعام والشراب أي خلا؛ الصفر الشيء الخالي؛ الصفر في حساب الهند هو الدائرة (tahdhib)؛ صفر الإناء إذا خلا؛ ثم صار متعارفا في كل حال من الآنية وغيرها (mufradat)
- **B003** açlık boşluğu, karın canlısı inancı ve sarı sıvı birikimi — aç kalınca karında ısırdığına inanılan canlı · açlık ve karnın besinden boşalması · karnında açlık sancısı veya zararlı canlı bulunduğu düşünülen kişi · karında sarı sıvı birikmesi · karında böyle bir canlının bulunmadığını bildiren söz · Tanrı yolunda çekilen açlık
  الصفر يقع في الكبد وشراسيف الأضلاع؛ رجل مصفور في بطنه صفر؛ الإنسان يصفر من الصفر جدا (ayn)؛ الصفر حية في البطن تعض الإنسان إذا جاع؛ الصفار بالضم اجتماع الماء الأصفر في البطن (sihah)؛ الصفر دواب البطن؛ حية تكون في البطن؛ تشتد على الإنسان وتؤذيه إذا جاع؛ الصفر الجوع؛ الصفار الماء الأصفر (tahdhib)؛ خلو الجوف والعروق من الغذاء صفرا؛ اعتقدت جهلة العرب أن ذلك حية في البطن (mufradat)
- **B004** kap yapımına uygun iyi bakır cevheri — kap yapımında kullanılan iyi nitelikli bakır cevheri
  الأصل الثالث الصفر من جواهر الأرض؛ النحاس هو الصفر الذي تعمل منه الآنية (maqayis)؛ الصفر ما يتخذ من النحاس الجيد (ayn)؛ الصفر بالضم الذي تعمل منه الأواني (sihah)؛ الصفر النحاس الجيد (tahdhib)؛ الصفر المخرج من المعادن ومنه قيل للنحاس صفر (mufradat)
- **B005** ıslık sesi ve bu sesi çıkarma — kuş veya insan ıslığı; hayvan çağırma sesi · içine üflenerek çalınan düdük · orada hiç kimse yok · küçük ötücü kuş · korkak kimse · adı ötüşündeki ıslığa bağlanan kuş
  الأصل الرابع فالصفير للطائر؛ ما بها صافر من هذا أي كأنه يصوت (maqayis)؛ العصفور طائر ذكر العين فيه زائدة وإنما هو من الصفير الذي يصفره في صوته (maqayis)؛ الصفير من الصوت كما تصفر بالدواب؛ الصفارة هنة جوفاء من نحاس يصفر فيها الغلام؛ ما بها صافر أي أحد ذو صفير (ayn)؛ صفر الطائر يصفر صفيرا أي مكا؛ ما بها صافر أي أحد؛ كان في كلامه صفار يريد صفيرا؛ الصفارية طائر (sihah)؛ الصفير من الصوت بالدواب؛ الصفارة هنة جوفاء من نحاس؛ ما في الدار صافر؛ الصفارية الصعوة؛ الصافر الجبان (tahdhib)؛ قد يقال الصفير للصوت حكاية لما يسمع (mufradat)
- **B006** ay takviminin ikinci ayı ve son sıcak dönem sonrası mevsim — ay takviminin ikinci ayı · ay takviminin ilk iki ayı · sonbahar ile kış yağmurları arasındaki dönem · son sıcak dönemden sonra gerçekleşen doğum veya yağmur · ilk ayın dokunulmazlığını ikinci aya erteleme yoktur
  أما الزمان فصفر اسم هذا الشهر؛ الصفران شهران في السنة؛ الصفري في النتاج بعد اليقظي (maqayis)؛ صفر شهر بعد المحرم؛ الصفران؛ الصفرية زمان بين الخريف والوسمي (ayn)؛ صفر الشهر بعد المحرم والجمع أصفار؛ الصفران شهران من السنة؛ الصفري في النتاج بعد القيظي؛ الصفري المطر يأتي في ذلك الوقت (sihah)؛ الصفر شهر بعد المحرم؛ تأخيرهم المحرم إلى صفر في تحريمه؛ الصفرية من لدن طلوع سهيل إلى سقوط الذراع؛ أمطار هذا الوقت صفرية؛ الصفري بعد الصقعي (tahdhib)؛ الشهر يسمى صفرا لخلو بيوتهم فيه من الزاد؛ الصفري من النتاج ما يكون في ذلك الوقت (mufradat)
- **B007** mevsimlik bitki, kuru ot ve ilişkili bitki adları — sonbahar başında çıkıp yeri yeşerten bitki · bir bitki veya belirli bir otun kurumuş hâli · bir ot türü · aspir; yerli sayılırsa adı iki kökün birleşmesiyle açıklanan boya ve yağ bitkisi
  السادس نبت؛ الصفري نبات يكون في أول الخريف؛ الصفار نبت يقال إنه يبيس البهمى (maqayis)؛ العصفر نبات وإن كان عربيا فمنحوت من عصر وصفر (maqayis)؛ الصفرية نبات يكون في أول الخريف يخضر الأرض ويورق الشجر (ayn)؛ الصفرية نبات يكون في أول الخريف؛ الصفار بالفتح يبيس البهمى؛ الصفراء نبت (sihah)؛ الصفرية نبات يكون في أول الخريف؛ الصفار نبتان؛ الصفراء نبت من العشب (tahdhib)؛ ليبيس البهمى صفار (mufradat)
- **B008** hayvanın diş dibindeki yem artığı — hayvanın diş diplerinde kalan saman ve yem artığı
  الصفار والصفار ما بقي في أسنان الدابة من التبن والعلف للدواب كلها (ayn)؛ الصفار ما بقي في أصول أسنان الدابة من التبن والعلف للدواب كلها (tahdhib)

## ظ ل ل (root_000966): 30:51 لَّظَلُّوا۟

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

## ص م م (root_000884): 30:52 ٱلصُّمَّ

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

## و ل ي (root_001684): 30:52 وَلَّوْا۟

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

## د ب ر (root_000458): 30:52 مُدْبِرِينَ

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

## ع م ي (root_001049): 30:53 ٱلْعُمْىِ

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

## ECHO ع م م (root_001047): for 30:53 ٱلْعُمْىِ: withheld observed target; not identity

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

## س ل م (root_000737): 30:53 مُّسْلِمُونَ

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

## ش ي ب (root_000833): 30:54 وَشَيْبَةً

- **B001** saçın ağarması — saçın ağarması ve kişinin ak saçlı duruma girmesi · saçı ağarmak, ak saçlı duruma gelmek · saçları ağarmış kişi; saçları ağarmış topluluk · ak saçlar onun saçını veya başını beyazlattı · üzüntü onun başını veya saçını ağarttı · baş ak saçlarla dolup bembeyaz oldu · iyice ağarmış saç anlamında pekiştirmeli söyleyiş
  الشيب شيب الرأس يقال شاب يشيب (maqayis)؛ الشيب بياض الشعر والمشيب دخول الرجل في حد الشيب (maqayis;sihah)؛ شاب يشيب شيبا وشيبة ورجل أشيب وقوم شيب (ayn;tahdhib)؛ الشيب والمشيب بياض الشعر (mufradat)؛ شيب الحزن رأسه وأشاب الحزن رأسه (maqayis;sihah)
- **B002** karla beyazlaşmış dağ görünüşü — üzerine kar düşüp tepeleri beyazlaşmış dağlar · bir dağın adı · yerin kar veya kırağıyla beyazladığı çok soğuk iki kış ayının adları
  الشيب الجبال يسقط عليها الثلج (maqayis)؛ الشيب جبل معروف (jamhara)؛ الجبال يقع عليها الثلج فتشيب به (sihah)؛ سحائب بيض؛ جبال مبيضة الرؤوس من الثلج أو من الغبار؛ شيب اسم جبل (tahdhib)؛ شيبان وملحان شهرا قماح سميا بذلك لبياض الأرض بما عليها من الصقيع (maqayis;sihah)
- **B003** ilk birleşmede kızlığın giderildiği gece [kalıp] — kadının ilk cinsel birleşmeyle kızlığının giderildiği gece
  باتت فلانة بليلة شيباء إذا افتضت (maqayis;sihah)؛ الليلة التي تفترع فيها المرأة ليلة شيباء (ayn)؛ باتت بليلة شيباء إذا افتضت وبليلة حرة إذا لم تفتض (mufradat)؛ للبكر إذا زفت إلى زوجها فدخل بها ولم يقترعها ليلة حرة وإن اقترعها باتت بليلة شيباء (tahdhib)
- **B004** devenin su emerken çıkardığı dudak sesi — develer su içerken dudaklarından çıkan emme sesinin taklidi
  الشيب بالكسر حكاية أصوات مشافر الإبل عند الشرب (sihah)؛ الشيب حكاية ترشف مشافر الإبل الماء إذا شربت (tahdhib)

## ق س م (root_001226): 30:55 يُقْسِمُ

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

## ل ب ث (root_001339): 30:55 لَبِثُوا۟, 30:56 لَبِثْتُمْ

- **B001** bir yerde kalıp orada bulunmayı sürdürmek — bir yerde kalmak ve orada bulunmayı sürdürmek · bir yerde kalma ve ikamet etme · kalıp durma, ikamet etme · kalma ve ikamet etme · bir yerde kalan veya ikamet eden · birinin kalmasını sağlamak veya onu bulunduğu yerde tutmak · birini kalmaya yöneltmek veya onun kalmasını sağlamak
  حرف يدل على تمكث؛ لبث بالمكان أقام (maqayis)؛ لبث بالمكان يلبث (jamhara)؛ اللبث واللباث المكث (sihah)؛ اللبث المكث (tahdhib)؛ لبث بالمكان أقام به ملازما له (mufradat)
- **B002** bir işte duraksayıp ağırdan almak — bir mesele üzerinde durup beklemek ve ağırdan almak · yavaş davranan veya oyalanan · bir ihtiyaç karşısında ağırdan alan · duraksamak, ağırdan almak ve oyalanmak · duraksayan, ağır davranan veya oyalanan
  لي لبثة على هذا الأمر أي توقف (jamhara)؛ ذا لبث (sihah)؛ اللبث البطيء؛ تلبث تلبثا فهو متلبث (tahdhib)

## ء ف ك (root_000041): 30:55 يُؤْفَكُونَ

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

## ك ت ب (root_001283): 30:56 كِتَٰبِ

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

## ب ع ث (root_000129): 30:56 ٱلْبَعْثِ, 30:56 ٱلْبَعْثِ

- **B001** durgun olanı harekete geçirme — harekete geçirmek; uyandırmak · devenin bağını çözüp onu ayağa kaldırmak · uyuyanı uyandırmak · kargaşanın kabarmaları ve alevlenmeleri · neredeyse hiç uyumayan adam · neredeyse hiç çökmeyen dişi deve
  الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)
- **B002** gönderme veya yöneltme — göndermek; yöneltmek · görevle göndermek; yola çıkarmak · birini bir iş için göndermek · birini bir işi yapmaya isteklendirip yöneltmek · asker birliğini düşmana karşı göndermek · göreve gönderilmiş topluluk veya birlik · gönderilmiş ordular
  البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)
- **B004** yola koyulup ilerleme — harekete geçip ilerlemek; hızlanmak · yola koyulma ve ilerleme · şiir benden akıp geldi
  انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)

## ن ف ع (root_001536): 30:57 يَنفَعُ

- **B001** zararın karşıtı olan ve iyiliğe ulaştıran yarar — zararın karşıtı olan, iyiliğe ulaşmaya yardım eden yarar · ona yarar sağladı · ondan yararlandı · yarar · yarar · yararlı · insanlara sürekli yarar sağlayan ve zarar vermeyen kişi
  النون والفاء والعين كلمة تدل على خلاف الضر (maqayis)؛ النفع ضد الضر (ayn;sihah;tahdhib)؛ نفعه نفعا وانتفعت بكذا (ayn)؛ نفعه ينفعه نفعا ومنفعة وانتفع بكذا (maqayis)؛ ما يستعان به في الوصول إلى الخيرات (mufradat)؛ ما عندهم نفيعة أي منفعة (tahdhib)؛ رجل نفاع إذا كان ينفع الناس ولا يضرهم (tahdhib)
- **B002** deri su kabının iki yanındaki yarılmış deri parçalardan biri — deri yarılarak su kabının iki yanına yerleştirilen parçalardan biri
  النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة (ayn)؛ النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة (tahdhib)
- **B003** değnek — değnek · değnek alıp satmak
  النَّفعة العصا وهي فعلة من النفع؛ أنفع الرجل إذا اتجر في النفعات وهي العصي

## ع ذ ر (root_000995): 30:57 مَعْذِرَتُهُمْ

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

## ع ت ب (root_000977): 30:57 يُسْتَعْتَبُونَ

- **B001** eşik veya basamak — kapı eşiği, basamak veya benzeri yükselti · eşikler, basamaklar veya yükseltilmiş arazi parçaları · bizim için bir çıkış basamağı yap
  العتبة أسكفة الباب (ayn;jamhara;sihah;tahdhib;maqayis)؛ كل مرقاة من الدرج عتبة (ayn;sihah;tahdhib;maqayis)؛ عتبات الجبال وأشراف الأرض (ayn;maqayis)؛ العتب الغلظ من الأرض (jamhara)؛ عتبة الوادي جانبه الأقصى (tahdhib)؛ عتب لنا عتبة أي اتخذها (ayn;maqayis)
- **B002** eş için örtülü ad — kadın veya eş için kullanılan örtülü ad
  جعلها إبراهيم كناية عن امرأة إسماعيل (ayn)؛ العرب تكني عن المرأة بالعتبة (tahdhib)
- **B003** bozucu kusur veya pürüz — bozulma, kusur, eğrilik veya pürüz · eğriliği ve yapısal kusuru olmayan · ağır ve kötü sıkıntı
  العتب ما دخل في أمر يفسده ويغيره عن الخلوص (ayn)؛ غير ذي عتب أي غير ملتو عن الضريبة ولا ناب عنها (ayn;tahdhib;maqayis)؛ حمل على عتبة كريهة وعلى عتب كريه من البلاء والشر (ayn;sihah;tahdhib;maqayis)؛ ما في هذا الأمر رتب ولا عتب أي شدة (sihah)؛ ما في طاعة فلان عتب أي التواء ولا نبوة (tahdhib)؛ عتب أي عيب (tahdhib)
- **B004** üç ayakla aksayarak ilerleme — devenin üç ayak üzerinde aksayarak yürümesi · tek ayak üzerinde sıçramak
  الفحل المعقول أو الظالع إذا مشى على ثلاث قوائم يقال يعتب عتبانا (ayn;tahdhib;maqayis)؛ عتب البعير عتبانا إذا ظلع ومشى على ثلاث (jamhara;sihah)؛ إذا وثب الرجل على رجل واحدة (sihah)؛ الأقطع إذا مشى على خشبة (ayn)
- **B005** gücenip sitem etme — birine gücenip onu kınamak · sitem etme veya karşılıklı sitemleşme · çok sitem eden veya sitemden etkilenmeyen kişi
  عتبت على فلان عتبا ومعتبة أي وجدت عليه (ayn;jamhara;sihah;tahdhib;maqayis)؛ العتاب مخاطبة الإدلال ومذاكرة الموجدة (sihah;tahdhib)؛ التعاتب والمعاتبة والعتاب (ayn;sihah;tahdhib;maqayis)؛ العتب الرجل الذي يعاتب صاحبه والعتوب الذي لا يعمل فيه العتاب (tahdhib)
- **B006** gönlünü yeniden kazanma — gücendiren davranıştan dönüp gönlünü almak · yeniden hoşnutluğa dönüş veya verilen hoşnutluk · hoşnut olmanı sağlayacağım · hoşnut edilme, bağışlanma veya geri alma istemek · bağışlanmayı veya geri gönderilmeyi istemek
  أعتبني أي ترك ما كنت أجد عليه ورجع إلى مرضاتي (ayn;tahdhib;maqayis)؛ أعتبت الرجل إذا عاتبك فأرضيته (jamhara)؛ العتبى رجوع المستعتب إلى محبة صاحبه (tahdhib)؛ لك العتبى أي لك الرضا (jamhara)؛ استعتبته فأعتبني أي استرضيته فأرضاني (sihah)؛ الاستعتاب الاستقالة (tahdhib)
- **B007** yön değiştirip ayrılma — bir şeyden ayrılmak veya başka yöne dönmek · kolay yolu bırakıp sarp kesime girmek
  الاعتتاب الانصراف عن الشيء (sihah;tahdhib)؛ اعتتبت الطريق إذا تركت سهله وأخذت في وعره (sihah)؛ اعتتب أي قصد وركب الجبل (sihah)؛ اعتتب فلان إذا رجع عن أمر كان فيه إلى غيره (sihah)؛ إذا مضى ساعة ثم رجع قد اعتتب في طريقه (tahdhib)
- **B008** orta parmak ile yüzük parmağı arası — orta parmak ile yüzük parmağı arasındaki yer
  العتب ما بين الوسطى والبنصر (sihah)
- **B009** telli çalgının enine tel dayanakları — telli çalgının yüzündeki enine tel dayanakları
  العتب الدستانات؛ العتب العيدان المعروضة على وجه العود منها تمد الأوتار إلى طرف العود (tahdhib)
- **B010** pantolonun önünü katlayıp kaldırma [kalıp] — pantolonunun önünü katlayıp yukarı kaldırdı
  الثبنة ما عتبته من قدام السراويل؛ كان عتب سراويله فتشمر (tahdhib)
- **B011** kaynamış kemiğin yeniden kırılması — onarılmış kemiği yeniden kırmak veya yeniden kırılmak
  إذا أعنت العظم المجبور قيل قد أعتب وأتعب (tahdhib)؛ أتعب العظم إذا هيض بعد الجبر مقلوب من أعتب (maqayis)

## ق ر ء (root_001210): 30:58 ٱلْقُرْءَانِ

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

## ق ر ء (root_001211): 30:58 ٱلْقُرْءَانِ

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

## ب ط ل (root_000127): 30:58 مُبْطِلُونَ

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

## ط ب ع (root_000926): 30:59 يَطْبَعُ

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

## ق ل ب (root_001248): 30:59 قُلُوبِ

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

## ص ب ر (root_000840): 30:60 فَٱصْبِرْ

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

## خ ف ف (root_000427): 30:60 يَسْتَخِفَّنَّكَ

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

## ي ق ن (root_001696): 30:60 يُوقِنُونَ

- **B001** kuşkunun giderilmesiyle kesinleşen bilgi — kuşkunun kalkması ve bilginin kesinleşmesi · kuşkusuz ve sabit bilgi · kesin olarak bilmek; kuşkusu kalmamak · bir şeyin doğruluğunu kesin olarak bilmek · kesin olarak bilme · kesinliğe varmak; kesin olarak bilmek · bir şeyden kesin biçimde emin olmak; kuşkusu kalmamak · kesin olarak bilen, kuşkusu olmayan · kesin bilen; kendisine ulaşan haberi hemen doğru sayan · duyduğu her şeyi kesin doğru sayan kimse · onun hakkında hiçbir kuşkusu olmamak · kesin bilen kimseyi bildiren küçültme biçimi · kesin bilgi · kesinliğin bilgi diye adlandırılan mertebesi · kesinliğin göz diye adlandırılan mertebesi · kesinliğin hakikat diye adlandırılan mertebesi · öldürmenin gerçekleştiğini kesin olarak bilmek
  اليقن واليقين زوال الشك (maqayis)؛ اليقن اليقين وهو إزاحة الشك وتحقيق الأمر (ayn;tahdhib)؛ اليقين العلم وزوال الشك (sihah)؛ سكون الفهم مع ثبات الحكم (mufradat)؛ أيقن واستيقن وتيقن كله واحد (ayn;sihah;tahdhib)؛ رجل أذن يقن وهو الذي لا يسمع بشيء إلا أيقن به (tahdhib)؛ ما قتلوه يقينا أي ما قتلوه قتلا تيقنوه (mufradat)
- **B002** korunup gözden uzak tutulan genç kadın — koruma altında ve gözden uzak tutulan genç kadın
  الموقونة الجارية المصونة المخدرة (tahdhib)



===== _commentary/v16/work/s030/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s030/reader_a_pilot.md)

# s030 Semantic Channel Discovery

## Parent Channels

### 1. P1: Appointed Phases and Reversals
- Semantic invariant: A bounded phase carries a condition toward reversal, recurrence, or a final change of state.
- Surface relation: direct; defeat and victory are timed in 30:2-6, creation returns in 30:11, the Hour separates in 30:12-16, and daily and vital alternation appears in 30:17-19.
- Surprising reach: The political forecast, resurrection, ritual day, and celestial motion all behave like scheduled transitions whose limits make reversal intelligible.

#### Subchannel A. Bounded Reversal of Power
- Reading type: mixed
- Scene or process: A marked interval and binding appointment carry defeat into victory and public joy.
- Active motifs: conquering force `quranic:root_001098:B001/m01`; force thickening and interlocking `quranic:root_001098:B002/m01`; cut-off numerical interval `quranic:root_000123:B004/m01`; yearly term `quranic:root_000751:B008/m01`; sign and appointment `quranic:root_000051:B005/m01`; temporal advance `quranic:root_001198:B002/m01`; subsequent phase `quranic:root_000131:B002/m01`; binding promise `quranic:root_001662:B001/m01`; fixed meeting time `quranic:root_001662:B003/m01`; failed promise `quranic:root_000433:B005/m01`; aid against an opponent `quranic:root_001510:B001/m01`; opened joy `quranic:root_001140:B001/m01`.
- Ayah anchors: غ ل ب 30:2-3; ب ع د 30:3-4; ب ض ع، س ن و، ء م ر، ق ب ل، ف ر ح 30:4; ن ص ر 30:5; و ع د، خ ل ف 30:6.
- Synthesis: The few years are not loose chronology but a cut and counted term bounded by an appointment. Promise holds the sequence together, while the failed-promise sense of خ ل ف supplies the exact counterfactual: the reversal is dependable because the appointed commitment does not collapse.

#### Subchannel B. Origination, Return, and Final Sorting
- Reading type: surface-primary
- Scene or process: What is initiated is restored, brought out, stood up, and separated into terminal groups.
- Active motifs: beginning paired with return `quranic:root_000090:B002/m01`; return after departure `quranic:root_001058:B001/m01`; destination of return `quranic:root_001058:B002/m01`; restoration to an earlier state `quranic:root_000544:B001/m01`; emergence from an enclosure `quranic:root_000400:B001/m01`; loss of life and force `quranic:root_001454:B001/m01`; resurrection-standing `quranic:root_001273:B013/m01`; dispersal into parts `quranic:root_001148:B002/m01`.
- Ayah anchors: ب د ء، ع و د، ر ج ع 30:11; ق و م 30:12, 30:14; ف ر ق 30:14; خ ر ج، م و ت 30:19.
- Synthesis: Beginning and return form one closed process rather than two unrelated acts. خروج makes restoration spatially concrete: the returned creation is brought out, made to stand, and then distributed rather than merely resumed.

#### Subchannel C. The Day as a Scheduled Round
- Reading type: mixed
- Scene or process: Worship occupies a recurring timetable analogous to fixed rounds of milking, drinking, feeding, and rest.
- Active motifs: assigning a known time to an act `quranic:root_000382:B003/m01`; morning drink or feed `quranic:root_000839:B003/m01`; evening meal and night grazing `quranic:root_001017:B005/m01`; ritual praise and prayer `quranic:root_000666:B001/m01`; spoken praise `quranic:root_000355:B001/m01`; noon station `quranic:root_000970:B004/m01`; recurring time `quranic:root_000382:B001/m01`.
- Ayah anchors: س ب ح، ح ي ن، ص ب ح 30:17; ح م د، ح ي ن، ع ش و، ظ ه ر 30:18.
- Synthesis: The named times become a disciplined round in which each act has its proper slot. The pastoral senses of morning drink and evening feeding materialize praise as regular care rather than an occasional utterance.

#### Subchannel D. Celestial Navigation by Moving Lights
- Reading type: latent/lexical
- Scene or process: A traveler reads moving heavenly bodies and successive lights to orient through darkness into day.
- Active motifs: swimming or running through air `quranic:root_000666:B004/m01`; sky and overshadowing canopy `quranic:root_000745:B004/m01`; seeking a night fire for guidance `quranic:root_001017:B002/m01`; weak night vision `quranic:root_001017:B006/m01`; morning lamp `quranic:root_000839:B005/m01`; noon marker `quranic:root_000970:B004/m01`; delimited time `quranic:root_000382:B001/m01`.
- Ayah anchors: س ب ح، ح ي ن، ص ب ح 30:17; س م و، ع ش و، ح ي ن، ظ ه ر 30:18.
- Synthesis: The praise-times also furnish an orientation system: a night fire, a morning lamp, a noon station, and bodies swimming under the canopy. The sequence turns temporal devotion into navigable light.

### 2. P1: Inscribed and Deceptive Surfaces
- Semantic invariant: Knowledge depends on reading visible marks while distinguishing genuine disclosure from blank or fabricated surfaces.
- Surface relation: direct; outward worldly knowledge is contrasted with inward reflection in 30:7-8, and travel, looking, evidence, denial, and mockery occupy 30:9-10.
- Surprising reach: Terrain, bodies, cloth, and writing supply a material semiotics in which signs can guide, disappear, or lie.

#### Subchannel A. A Marked Route Through Terrain
- Reading type: mixed
- Scene or process: A traveler crosses a tract by finding waymarks; an unmarked expanse defeats orientation.
- Active motifs: waymark that identifies and guides `quranic:root_001040:B002/m01`; land or road without a mark `quranic:root_001097:B006/m01`; travel across the earth `quranic:root_000769:B001/m01`; moving caravan `quranic:root_000769:B006/m01`; directed inspection `quranic:root_001520:B001/m01`; tract extending to the limit of sight `quranic:root_000170:B007/m01`; raised ground surface `quranic:root_000970:B003/m01`.
- Ayah anchors: ع ل م 30:6-7; غ ف ل 30:7; ب ي ن 30:8-9; س ي ر، ن ظ ر 30:9; ظ ه ر 30:7.
- Synthesis: Historical travel becomes an act of route-reading. The contrast is not simply seeing versus failing to see, but marked land versus a blank expanse: آثار are recoverable only when the traveler treats the world as a legible route.

#### Subchannel B. Turning the Surface Toward the Interior
- Reading type: mixed
- Scene or process: The visible face of an object is turned over so its inner intention and measured design can be examined.
- Active motifs: outward disclosure `quranic:root_000970:B001/m01`; back opposed to belly `quranic:root_000970:B002/m01`; turning an affair back-to-belly `quranic:root_000970:B018/m01`; inward intent and discernment `quranic:root_001533:B013/m01`; the self as essence `quranic:root_001533:B012/m01`; thought circulating in the heart `quranic:root_001172:B001/m01`; measurement before making `quranic:root_000434:B001/m01`.
- Ayah anchors: ظ ه ر 30:7; ف ك ر، ن ف س، خ ل ق 30:8; ن ف س 30:9.
- Synthesis: “Outward” knowledge is a single exposed face. Reflection turns the object, passes from surface to interior, and asks after the prior measure by which the created form was made.

#### Subchannel C. Counterfeit Display Versus Verified Sign
- Reading type: mixed
- Scene or process: A visible mark is tested against disclosed evidence while fabricated speech and deceptive color imitate truth.
- Active motifs: manifest sign `quranic:root_000074:B003/m01`; evidence becoming visible `quranic:root_000170:B004/m01`; meaning disclosed by speech or mark `quranic:root_000170:B005/m01`; truth matching what is fixed `quranic:root_000347:B001/m01`; proof that establishes truth `quranic:root_000347:B005/m01`; fabricated speech `quranic:root_000434:B007/m01`; dyed cloth that lies by its appearance `quranic:root_001290:B009/m01`; covering over `quranic:root_001307:B001/m01`; exposed appearance `quranic:root_000970:B001/m01`.
- Ayah anchors: ظ ه ر 30:7; خ ل ق، ح ق ق، ب ي ن، ك ف ر 30:8; ب ي ن 30:9; ء ي ي، ك ذ ب 30:10.
- Synthesis: A sign is not accepted merely because it is vivid. The dyed cloth supplies a precise counterfeit mechanism: a manufactured surface can announce a condition it does not possess, whereas bayyinah and haqq disclose and establish what is actually fixed.

### 3. P1: Water-Borne Restoration
- Semantic invariant: Collected or descending water converts blocked, barren, or defeated potential into productive life.
- Surface relation: indirect; victory and mercy appear in 30:4-5, created land and worked earth in 30:8-9, and dead earth brought to life in 30:19.
- Surprising reach: Military aid and resurrection are materialized as irrigation, storage, release, and renewed growth.

#### Subchannel A. Victory as Irrigation and Relief
- Reading type: latent/lexical
- Scene or process: Rain-like aid is caught, regulated, and delivered to fertile ground as blessing and relief.
- Active motifs: victory-rain that relieves a land `quranic:root_001510:B004/m01`; watering by cloud, bucket, or irrigation device `quranic:root_000751:B001/m01`; flood barrier admitting only needed water `quranic:root_000751:B007/m01`; growth and blessing `quranic:root_000051:B004/m01`; merciful beneficence `quranic:root_000552:B001/m01`; fertile yielding earth `quranic:root_000025:B002/m01`; land enlivened by rain `quranic:root_000383:B002/m01`.
- Ayah anchors: س ن و، ء م ر 30:4; ن ص ر، ر ح م 30:5; ء ر ض 30:3, 30:8-9, 30:18-19; ح ي ي 30:19.
- Synthesis: Naṣr becomes an answering rainfall rather than only battlefield assistance. The sluice-like sense of سنو adds regulation: relief is effective because force is delivered in a measure that makes the ground productive.

#### Subchannel B. Reservoir, Channel, and Revived Ground
- Reading type: latent/lexical
- Scene or process: Water gathers in prepared basins and depressions before being released into land that can live again.
- Active motifs: reservoir collecting well, channel, or rainwater `quranic:root_000016:B007/m01`; rock hollow retaining rain `quranic:root_000434:B011/m01`; depression collecting water `quranic:root_000281:B003/m01`; yielding planted earth `quranic:root_000025:B002/m01`; rain-life and fresh growth `quranic:root_000383:B002/m01`; uncultivated dead land `quranic:root_001454:B003/m01`; emergence from confinement `quranic:root_000400:B001/m01`.
- Ayah anchors: ء ج ل، خ ل ق، ء ر ض 30:8; ج ي ء، ء ر ض 30:9; ح ي ي، م و ت، خ ر ج، ء ر ض 30:19.
- Synthesis: Creation and historical cultivation disclose a storage-and-release mechanism. The final خروج is thus more than motion outward: what was held in dead ground is made available as life.

### 4. P1: Claims Brought to Division
- Semantic invariant: Shared interests and earned acts become explicit claims before a forum that separates parties and outcomes.
- Surface relation: direct; partners, intercessors, compulsory presence, and separation structure 30:12-16.
- Surprising reach: Eschatological sorting is rendered through co-ownership, pre-emption, advocacy, wages, and adjudicated liability.

#### Subchannel A. Co-Ownership Without an Effective Advocate
- Reading type: mixed
- Scene or process: Partners hold a shared interest, a claimant seeks an advocate, and a disputed share is finally divided.
- Active motifs: shared ownership `quranic:root_000791:B001/m01`; advocate joining a claimant `quranic:root_000802:B002/m01`; neighbor adding a pre-empted share to his property `quranic:root_000802:B003/m01`; right owned by its claimant `quranic:root_000347:B003/m01`; adversaries each asserting the right `quranic:root_000347:B004/m01`; courtroom contest `quranic:root_000333:B006/m01`; dispersal into separate parts `quranic:root_001148:B002/m01`.
- Ayah anchors: ح ق ق 30:8; ش ر ك، ش ف ع 30:13; ف ر ق 30:14; ح ض ر 30:16.
- Synthesis: The denied intercession is a failed legal joinder inside a broken partnership. Separation resolves what the partners and absent advocate cannot: every claim is detached from the collective arrangement that once obscured it.

#### Subchannel B. Earned Liability and Compelled Appearance
- Reading type: mixed
- Scene or process: Deliberate work earns its return, while criminal acquisition becomes a liability that brings its bearer into compulsory presence.
- Active motifs: acquisition or earning `quranic:root_000239:B003/m01`; culpable offense `quranic:root_000239:B004/m01`; intended work `quranic:root_001046:B001/m01`; worker's wage `quranic:root_001046:B004/m01`; terminal consequence `quranic:root_001033:B006/m01`; punishment following offense `quranic:root_001033:B007/m01`; harmful presence that cannot be avoided `quranic:root_000333:B009/m01`; inflicted punishment `quranic:root_000994:B005/m01`.
- Ayah anchors: ع ق ب 30:9, 30:10; ج ر م 30:12; ع م ل 30:15; ع ذ ب، ح ض ر 30:16.
- Synthesis: Work and crime are both productive in the narrow sense that each generates a return. The difference appears at presentation: one yield is delight, while the other has matured into a claim that compels attendance.

### 5. P2: Pairing, Gestation, and Nurture
- Semantic invariant: A paired relation encloses, forms, reveals, and then sustains new life.
- Surface relation: direct; human formation and dispersal appear in 30:20, spouses and mercy in 30:21, and water, descent, differentiation, and signs in 30:22-24.
- Surprising reach: The human household opens into a detailed reproductive and dairy-husbandry sequence extending from contact and seed to pregnancy, milk, and weaning.

#### Subchannel A. From Earthly Matter to Paired Bodies
- Reading type: mixed
- Scene or process: Matter receives a visible bodily form; paired bodies meet, seed enters a womb, and humanity spreads.
- Active motifs: earth and dust material `quranic:root_000178:B001/m01`; exposed skin or surface `quranic:root_000120:B001/m01`; human as skin-bearing creature `quranic:root_000120:B002/m01`; completed visible formation `quranic:root_000434:B003/m01`; paired counterparts `quranic:root_000652:B001/m01`; marital pair `quranic:root_000652:B002/m01`; skin-to-skin contact `quranic:root_000120:B003/m01`; womb as generative enclosure `quranic:root_000552:B003/m01`; male generative fluid in the womb `quranic:root_001458:B004/m01`; seminal descent `quranic:root_001492:B009/m01`.
- Ayah anchors: خ ل ق، ت ر ب، ب ش ر 30:20; خ ل ق، ز و ج، ر ح م 30:21; ن ز ل، م و ه 30:24.
- Synthesis: The movement from dust to بشر is a movement from raw matter to an exposed bodily surface. Pairing and direct contact then relocate formation inside an enclosure, so انتشار becomes the outward multiplication of an inwardly completed process.

#### Subchannel B. Herd Pregnancy, Milk, and Weaning
- Reading type: latent/lexical
- Scene or process: Breeding is diagnosed, milk is induced and drawn, and the young is eventually separated from nursing.
- Active motifs: pregnancy becoming visibly detectable `quranic:root_000531:B010/m01`; false signal of pregnancy `quranic:root_000108:B004/m01`; residual milk drawing the next flow `quranic:root_000478:B003/m01`; inducing a dam's milk by presenting a young animal `quranic:root_001355:B007/m01`; milking with the fingertips `quranic:root_001165:B005/m01`; young animal separated from dam or nursing `quranic:root_001159:B003/m01`; paired breeding relation `quranic:root_000652:B001/m01`.
- Ayah anchors: ز و ج 30:21; ل س ن 30:22; ر ء ي، ب ر ق 30:24; د ع و 30:25; ف ص ل 30:28; ف ط ر 30:30.
- Synthesis: The sequence distinguishes appearance from material completion: a raised tail may falsely advertise conception, whereas visible pregnancy, milk response, and weaning mark successive realized states. The signs passage thereby resonates with practical husbandry, where life is known by diagnostic effects.

### 6. P2: Habitable Stillness
- Semantic invariant: Rest is an achieved stability that permits attachment, trust, and renewed circulation.
- Surface relation: direct; domestic repose is named in 30:21 and sleep, night, day, seeking, and bounty are joined in 30:23.
- Surprising reach: Home and sleep are not inert pauses; each is an anchoring mechanism that makes relation and livelihood possible.

#### Subchannel A. Household as an Anchorage
- Reading type: mixed
- Scene or process: Paired persons become residents whose affection and kinship form the connective interior of a home.
- Active motifs: marital pairing `quranic:root_000652:B002/m01`; settled dwelling `quranic:root_000726:B002/m01`; household residents `quranic:root_000726:B003/m01`; beloved object in which the self comes to rest `quranic:root_000726:B004/m01`; mutual affection `quranic:root_001634:B001/m01`; kinship bond `quranic:root_000552:B002/m01`; connective relation among parties `quranic:root_000170:B003/m01`.
- Ayah anchors: ز و ج، س ك ن، و د د، ر ح م، ب ي ن 30:21.
- Synthesis: Sakan is both the house and the cessation of restless motion within it. Affection and kinship are the relation that fills the “between,” turning juxtaposed persons into a stable household.

#### Subchannel B. Rest Followed by Livelihood
- Reading type: mixed
- Scene or process: Night settles the body into trusted rest; daylight reopens movement in search of surplus provision.
- Active motifs: sleep and repose `quranic:root_001568:B001/m01`; settling into trust `quranic:root_001568:B005/m01`; night and its darkness `quranic:root_001392:B001/m01`; day opening in light `quranic:root_001559:B002/m01`; seeking a need `quranic:root_000138:B001/m01`; surplus beyond immediate need `quranic:root_001163:B001/m01`; beneficent gift `quranic:root_001163:B003/m01`; hearing that becomes reception and response `quranic:root_000741:B003/m01`.
- Ayah anchors: ن و م، ل ي ل، ن ه ر، ب غ ي، ف ض ل، س م ع 30:23.
- Synthesis: Sleep is a trusted cessation that stores capacity rather than wasting time. Day then releases that capacity into pursuit, while “bounty” names what exceeds bare subsistence and returns rest as provision.

### 7. P2: Storm Signal and Hydrological Opening
- Semantic invariant: A visible atmospheric signal announces a descent that opens channels and restores productive ground.
- Surface relation: direct; lightning, fear, hope, descending water, revived earth, and reasoning are concentrated in 30:24.
- Surprising reach: Lightning can be both reliable precursor and empty lure, making hydrological renewal also a problem of discerning signals.

#### Subchannel A. Flash, Alarm, and Expectation
- Reading type: mixed
- Scene or process: A flash seizes the eye, carries threat and hope, and must be judged as either rain-bearing sign or empty lure.
- Active motifs: lightning flash and polished gleam `quranic:root_000108:B001/m01`; eye transfixed by alarm `quranic:root_000108:B002/m01`; threatening display `quranic:root_000108:B003/m01`; empty lightning without rain `quranic:root_000108:B004/m02`; fear expecting harm `quranic:root_000447:B001/m01`; heart's expectation `quranic:root_000951:B001/m01`; decoy bird placed inside a net `quranic:root_000951:B005/m01`; sight and inward perception `quranic:root_000531:B001/m01`; reason that restrains error `quranic:root_001036:B001/m01`.
- Ayah anchors: ر ء ي، ب ر ق، خ و ف، ط م ع، ع ق ل 30:24.
- Synthesis: The same flash can announce water, threaten, or prove hollow. The decoy sense of طمع sharpens the danger: expectation is drawn toward a visible promise, so reason must discriminate a productive sign from an attractive trap.

#### Subchannel B. Descent, Channel, and Renewed Pasture
- Reading type: mixed
- Scene or process: Water descends, cuts and fills channels, enters soil, and revives dried grazing ground.
- Active motifs: descent from above `quranic:root_001492:B001/m01`; water as material `quranic:root_001458:B001/m01`; water appearing and filling `quranic:root_001458:B002/m01`; delivery by pouring or irrigation `quranic:root_001458:B003/m01`; rain as provision `quranic:root_000560:B003/m01`; river cutting a course through earth `quranic:root_001559:B001/m01`; opening widened until flow passes `quranic:root_001559:B003/m01`; land living by rain `quranic:root_000383:B002/m01`; dry pasture greening after rain `quranic:root_001503:B004/m01`; fertile earth `quranic:root_000025:B002/m01`.
- Ayah anchors: ن ش ر 30:20; ن ه ر 30:23; ن ز ل، م و ه، ح ي ي، ء ر ض 30:24; ر ز ق 30:28.
- Synthesis: The storm is a causal assembly, not a cluster of weather terms: descent supplies matter, channel-opening supplies passage, and the earth's response supplies the outcome. The revived pasture makes resurrection-like life a visible hydrological effect.

### 8. P2: Pattern, Exemplar, and Unaltered Formation
- Semantic invariant: A durable form arises from measure and pattern, while alteration either follows or violates that formative rule.
- Surface relation: direct; creation, the highest exemplar, a struck likeness, detailed signs, innate formation, and non-substitution occupy 30:27-30.
- Surprising reach: Creation and religious disposition are rendered through modeling, pattern transfer, image alteration, and craft discipline.

#### Subchannel A. Making by an Exemplar
- Reading type: mixed
- Scene or process: A maker measures material, presents a model, transfers its pattern, and distinguishes the finished parts.
- Active motifs: measured preparation before making `quranic:root_000434:B001/m01`; completed visible form `quranic:root_000434:B003/m01`; making or bringing into form `quranic:root_000248:B001/m01`; describing a model whose effect appears elsewhere `quranic:root_000906:B003/m01`; pattern or type for fabrication `quranic:root_000906:B007/m01`; represented image `quranic:root_001397:B008/m01`; imitation by following an exemplar `quranic:root_001397:B010/m01`; example that functions as a sign `quranic:root_001397:B011/m01`; detailed separation of components and meanings `quranic:root_001159:B013/m01`.
- Ayah anchors: ج ع ل 30:21; خ ل ق، م ث ل 30:27; ض ر ب، م ث ل، ف ص ل 30:28.
- Synthesis: The struck example is a working model: it renders an otherwise abstract relation reproducible in another material. Creation and exposition share the same operation of measure, visible form, and articulated parts.

#### Subchannel B. Native Form Resistant to Substitution
- Reading type: mixed
- Scene or process: An originating split opens a form whose inner disposition and outward configuration should not be exchanged or distorted.
- Active motifs: opening or splitting a material `quranic:root_001165:B001/m01`; originating a new form `quranic:root_001165:B002/m01`; hasty forming before material matures `quranic:root_001165:B006/m01`; inward disposition `quranic:root_000434:B004/m01`; replacement by another thing `quranic:root_000095:B001/m01`; alteration of appearance while substance remains `quranic:root_000095:B002/m01`; impressed disposition or cast character `quranic:root_000906:B009/m01`; established habit and mode `quranic:root_000504:B005/m01`; upright and balanced form `quranic:root_001273:B008/m01`.
- Ayah anchors: ض ر ب 30:28; ق و م، د ي ن، ف ط ر، ب د ل، خ ل ق 30:30.
- Synthesis: Fiṭrah is an originating opening that establishes both configuration and disposition. The substitution contrast is exact: one may change a surface image while retaining matter, but that alteration no longer expresses the measure that first gave the form its integrity.

### 9. P2: Guided Gait and Fragmented Following
- Semantic invariant: Direction is enacted bodily by stance, facing, following, and controlled movement; deviation fragments both route and group.
- Surface relation: direct; following desire, guidance, setting the face, upright religion, turning back, and sectarian division structure 30:29-32.
- Surprising reach: Abstract guidance becomes a gait problem involving bent feet, leading fronts, protected hooves, forks, shepherd calls, and strayed animals.

#### Subchannel A. Orienting the Body on the Route
- Reading type: mixed
- Scene or process: A walker corrects a bent inclination, faces a destination, follows a guide, and protects footing against a misleading descent.
- Active motifs: bent or inverted foot `quranic:root_000362:B001/m01`; inclination toward a side `quranic:root_000362:B002/m01`; upright route and balanced stance `quranic:root_001273:B008/m01`; direction and destination `quranic:root_001630:B002/m01`; sound course of an affair `quranic:root_001630:B008/m01`; gentle guidance to the road `quranic:root_001583:B001/m01`; leading front or guide `quranic:root_001583:B003/m01`; deviation from the intended route `quranic:root_000913:B001/m01`; falling into a hollow `quranic:root_001609:B002/m01`; following a trace `quranic:root_000175:B001/m01`; hoof guarded from rough ground `quranic:root_001677:B003/m01`.
- Ayah anchors: ت ب ع، ه و ي، ه د ي، ض ل ل 30:29; ق و م، و ج ه، ح ن ف 30:30; و ق ي، ق و م 30:31.
- Synthesis: Guidance is a coordinated posture: foot, face, leader, and road agree. Desire introduces lateral pull and downward fall, while taqwā resonates as the animal's careful protection of its hoof from ground that would injure the journey.

#### Subchannel B. Flock and Party at the Fork
- Reading type: latent/lexical
- Scene or process: A shepherd's call gathers a flock, but rival portions and route-forks detach it into self-satisfied groups and strays.
- Active motifs: party gathered on one opinion `quranic:root_000315:B001/m01`; allotted portion or turn at water `quranic:root_000315:B002/m01`; supporting followers `quranic:root_000836:B002/m01`; shepherd's call or flute `quranic:root_000836:B006/m01`; scattering into parts `quranic:root_001148:B002/m01`; detached flock `quranic:root_001148:B005/m01`; fork of road `quranic:root_001148:B006/m01`; strayed animal `quranic:root_000913:B005/m01`; self-enclosed joy `quranic:root_001140:B001/m01`.
- Ayah anchors: ض ل ل 30:29; ف ر ق، ش ي ع، ح ز ب، ف ر ح 30:32.
- Synthesis: Sectarian division is a husbandry failure: a gathering signal no longer produces one directed flock. Each detached group treats its own portion and branch-route as complete, so joy becomes the affect of separation rather than arrival.

### 10. P2: Held Order and Authoritative Release
- Semantic invariant: A system remains upright because motion is restrained and maintained until an authoritative signal releases it.
- Surface relation: direct; heaven and earth stand by command, all submit, and a call brings people out in 30:25-26.
- Surprising reach: Cosmic stability resembles a bridled and tethered body whose stored motion can be released by voice.

#### Subchannel A. Standing Under Restraint
- Reading type: mixed
- Scene or process: A load-bearing structure is kept upright by maintenance, command, bridle, and tether.
- Active motifs: bodily standing `quranic:root_001273:B002/m01`; maintenance and governance `quranic:root_001273:B004/m01`; structural support and sustenance `quranic:root_001273:B009/m01`; immobilization and arrested motion `quranic:root_001273:B016/m01`; binding command `quranic:root_000051:B002/m01`; governing authority `quranic:root_000051:B003/m01`; bridle preventing uncontrolled running `quranic:root_000348:B006/m01`; tethering a camel's leg `quranic:root_001036:B002/m01`; overhead canopy `quranic:root_000745:B004/m01`.
- Ayah anchors: ع ق ل 30:24, 30:28; ق و م، س م و، ء م ر 30:25; س م و 30:26; ح ك م 30:27.
- Synthesis: “Standing by command” is load-bearing control, not static existence. Bridle and tether supply the mechanism: stability is active restraint that preserves the structure's capacity for later movement.

#### Subchannel B. The Call That Releases Emergence
- Reading type: mixed
- Scene or process: A voice reaches a held system, motion begins, and what was inside or below comes out in sequence.
- Active motifs: vocal summons drawing a respondent `quranic:root_000478:B001/m01`; falling or moving one after another `quranic:root_000478:B005/m01`; outward emergence `quranic:root_000400:B001/m01`; clinging and lingering on the ground `quranic:root_000025:B006/m01`; resurrection-standing `quranic:root_001273:B013/m01`; manifest sign `quranic:root_000074:B003/m01`.
- Ayah anchors: ء ي ي، ق و م، د ع و، ء ر ض، خ ر ج 30:25.
- Synthesis: The call functions as a release signal. It overcomes earth-bound lingering and converts hidden or arrested bodies into an ordered خروج, while the collapse sense of تداعي preserves the possibility that release also dismantles the prior arrangement.

### 11. P2: Shared Property and Settlement
- Semantic invariant: Possession shared among parties requires explicit shares, equality rules, authority, and a mechanism of settlement.
- Surface relation: direct; ownership, partners, provision, equality, fear, and detailed explanation meet in 30:28.
- Surprising reach: The theological comparison unfolds as a concrete property and commercial-partnership problem.

#### Subchannel A. Co-Owned Provision
- Reading type: mixed
- Scene or process: An owner confronts a proposed co-owner over an allotted asset and tests whether shares and authority are truly equal.
- Active motifs: ownership and disposal `quranic:root_001444:B002/m01`; shared interest `quranic:root_000791:B001/m01`; allotted provision `quranic:root_000560:B001/m01`; equal valuation `quranic:root_000766:B001/m01`; self or own person `quranic:root_001533:B012/m01`; right hand and operative power `quranic:root_001698:B004/m01`; fear expecting injury `quranic:root_000447:B001/m01`.
- Ayah anchors: ن ف س، م ل ك، ي م ن، ش ر ك، ر ز ق، س و ي، خ و ف 30:28.
- Synthesis: The example turns “partner” into an exact property relation. Equality would require not just access to goods but parity of disposition, valuation, and power; the fear response reveals that such equality is not actually granted.

#### Subchannel B. Traveling Commercial Partnership
- Reading type: latent/lexical
- Scene or process: Capital is entrusted to a traveler, profit is shared, and the parties later divide and settle the joint interest.
- Active motifs: commercial partnership funded for travel `quranic:root_000906:B016/m01`; travel in search of provision `quranic:root_000906:B002/m01`; allotted livelihood `quranic:root_000560:B001/m01`; division between partners `quranic:root_001159:B014/m01`; ownership and delegated disposal `quranic:root_001444:B002/m01`; oath or pledged undertaking `quranic:root_001698:B003/m01`; water that sustains a traveling party's affairs `quranic:root_001444:B007/m01`.
- Ayah anchors: ض ر ب، ر ز ق، م ل ك، ي م ن، ف ص ل 30:28.
- Synthesis: The same ownership comparison can be read as muḍārabah: one party supplies assets and another moves with them, but neither relation erases the need for explicit shares and settlement. This makes the implied partnership a governed contract, not vague association.

### 12. P3: Embodied Consequence and Systemic Injury
- Semantic invariant: Consequence becomes knowable by entering the body as contact, taste, wound, or loss of healthy balance.
- Surface relation: direct; harm touches, mercy is tasted, misfortune strikes, and hands send effects forward in 30:33-36, while corruption is made manifest and tasted in 30:41.
- Surprising reach: Emotional instability and ecological corruption are rendered as sensory testing, trauma, bitter medicine, ulceration, and systemic disease.

#### Subchannel A. Contact and Taste as Knowledge
- Reading type: mixed
- Scene or process: An external condition reaches the body by touch and is known by tasting its quality.
- Active motifs: tactile contact `quranic:root_001423:B001/m01`; effect reaching person or property `quranic:root_001423:B004/m01`; urgent bodily need `quranic:root_001423:B006/m01`; tasting food `quranic:root_000526:B001/m01`; learning through trial and experience `quranic:root_000526:B002/m01`; merciful beneficence `quranic:root_000552:B001/m01`; harm and bodily deficiency `quranic:root_000907:B001/m01`; despair as severed expectation `quranic:root_001261:B001/m01`.
- Ayah anchors: م س س، ض ر ر، ذ و ق، ر ح م 30:33; ذ و ق، ر ح م، ق ن ط 30:36; ذ و ق 30:41.
- Synthesis: Mercy and adversity enter the same sensory apparatus. “Taste” turns changing fortune into tested knowledge, while “touch” insists that the condition has crossed from report into bodily consequence.

#### Subchannel B. Hand, Impact, and Wound
- Reading type: latent/lexical
- Scene or process: An acting hand produces an impact whose damage appears as wound, pain, and bitter residue.
- Active motifs: inflicted harm `quranic:root_000907:B002/m01`; necessity forcing an unwanted state `quranic:root_000907:B003/m01`; impact or calamity striking a person `quranic:root_000889:B004/m01`; bitter plant extract `quranic:root_000889:B007/m01`; bad or damaged condition `quranic:root_000755:B001/m01`; wound carried by a word `quranic:root_001316:B003/m01`; deed and injury attributed to the hands `quranic:root_001693:B009/m01`; hand as bodily instrument `quranic:root_001693:B001/m01`.
- Ayah anchors: س و ء 30:36; ص و ب، ي د ي 30:36; ي د ي 30:41; ك ل م 30:35; ض ر ر 30:33.
- Synthesis: The hand is both instrument and source of attribution, so the blow cannot be detached from agency. Kalām's wound sense makes the speaking “authority” in 30:35 a sharp contrast: genuine proof would articulate, while false association leaves only injurious assertion.

#### Subchannel C. Land and Sea as a Diseased Body
- Reading type: latent/lexical
- Scene or process: A body's balance fails, a lesion suppurates, a wasting illness reaches crisis, and symptoms become visible so recovery can begin.
- Active motifs: corruption as departure from healthy balance `quranic:root_001154:B001/m01`; land as a festering ulcer `quranic:root_000025:B011/m01`; sea as a wasting disease `quranic:root_000086:B011/m01`; acute medical crisis `quranic:root_000086:B012/m01`; thirst that water cannot satisfy `quranic:root_000086:B014/m01`; injurious effect reaching its subject `quranic:root_001423:B004/m01`; symptom becoming manifest `quranic:root_000970:B001/m01`; restoration after illness or wasting `quranic:root_000544:B014/m01`.
- Ayah anchors: م س س 30:33; ظ ه ر، ف س د، ب ح ر، ر ج ع 30:41; ء ر ض 30:42.
- Synthesis: Land and sea form one afflicted organism: corruption is dysregulation, the land is a lesion, and the sea carries wasting and crisis. The commanded return then has a convalescent force, not merely a change of opinion.

### 13. P3: Disciplined Force Toward a Target
- Semantic invariant: Power becomes effective only when its instrument or carrier is tested, controlled, measured, and directed.
- Surface relation: indirect; trial, striking misfortune, authority, hands, measure, approach, and established right occur across 30:33-38.
- Surprising reach: The pericope's unstable reactions are pressured by two technologies of controlled force: archery and trained horsemanship.

#### Subchannel A. Testing the Bow and Making the Shot
- Reading type: latent/lexical
- Scene or process: A bow is tested for tension, a hard string is set, the hand grips the implement, and a measured shot reaches its mark.
- Active motifs: testing a bow by drawing its string `quranic:root_000526:B003/m01`; aiming and hitting a target `quranic:root_000889:B003/m01`; long sharp projectile or implement `quranic:root_000732:B006/m01`; hard sinew used for bowstrings and arrows `quranic:root_001033:B001/m01`; hand as power `quranic:root_001693:B002/m01`; handle or terminal grip `quranic:root_001693:B013/m01`; deliberate measuring and preparation `quranic:root_001205:B005/m01`.
- Ayah anchors: ذ و ق 30:33, 30:36, 30:41; س ل ط 30:35; ص و ب، ي د ي 30:36; ق د ر 30:37; ع ق ب 30:42.
- Synthesis: The same root that makes fortune “tasted” also tests the bow before release. Reliable force therefore requires prior knowledge of tension, a measured line, and a hand that can convert stored energy into a precise arrival.

#### Subchannel B. Schooling the Mount
- Reading type: latent/lexical
- Scene or process: A rider controls a strong mount, measures its stride, and advances it toward the goal without losing the line.
- Active motifs: strength and expertise in controlling a bridle `quranic:root_000907:B007/m01`; courageous forward advance `quranic:root_001207:B006/m01`; measured gallop below full sprint `quranic:root_001212:B014/m01`; hind hooves matching forehoof positions `quranic:root_000347:B014/m01`; form matching its proper measure `quranic:root_001205:B006/m01`; forelegs returning rhythmically in gait `quranic:root_000009:B009/m01`.
- Ayah anchors: ض ر ر 30:33; ق د م 30:36; ق د ر 30:37; ء ت ي، ح ق ق، ق ر ب 30:38.
- Synthesis: Controlled gait provides a contrast to the pericope's abrupt joy, despair, and reversal. Strength is not mere acceleration; it is a stride repeatedly landing in measure under a practiced hand.

### 14. P3: Measured Circulation and Productive Growth
- Semantic invariant: Provision acquires moral and material force through measured transfer, circulation, and a growth process that yields beyond its input.
- Surface relation: direct; expansion and restriction of provision, gifts to claimants, usury, alms, wealth, doubling, creation, and life occupy 30:37-40.
- Surprising reach: Economic increase is tested against irrigation, nourishment, swelling soil, ploughing, and grain formation rather than against quantity alone.

#### Subchannel A. Allotment, Claimant, and Transfer
- Reading type: mixed
- Scene or process: A measured stock is expanded or constrained, then transferred to recognized claimants and travelers.
- Active motifs: allotted provision `quranic:root_000560:B001/m01`; expansion and increase `quranic:root_000116:B003/m01`; constriction to a narrow measure `quranic:root_001205:B004/m01`; bounded quantity `quranic:root_001205:B001/m01`; giving or delivery `quranic:root_000009:B002/m01`; specific right held by a claimant `quranic:root_000347:B003/m01`; kinship claimant `quranic:root_001212:B003/m01`; traveler on the road `quranic:root_000672:B002/m01`; accumulated wealth `quranic:root_001457:B001/m01`; intended direction of will `quranic:root_000610:B001/m01`.
- Ayah anchors: ب س ط، ر ز ق، ق د ر 30:37; ء ت ي، ق ر ب، ح ق ق، س ب ل، ر و د 30:38; ء ت ي، م و ل، ر و د 30:39.
- Synthesis: Expansion and restriction establish the available measure; right and kinship identify where transfer is due. The traveler ensures that circulation crosses household boundaries, so provision is not complete while it remains only in the owner's hand.

#### Subchannel B. Swelling, Feeding, and Multiplication
- Reading type: mixed
- Scene or process: An input swells, feeds a developing body, and multiplies, but its increase may be either nourishing or merely added over principal.
- Active motifs: swelling and rising `quranic:root_000537:B001/m01`; increase added to capital `quranic:root_000537:B003/m01`; nourishment and growth `quranic:root_000537:B005/m01`; plant-like increase and blessing `quranic:root_000637:B001/m01`; purification and soundness `quranic:root_000637:B002/m01`; increase by a matching multiple `quranic:root_000909:B002/m01`; yield and productive issue `quranic:root_000009:B007/m01`; expanded provision `quranic:root_000116:B003/m01`.
- Ayah anchors: ب س ط 30:37; ء ت ي، ر ب و، ز ك و، ض ع ف 30:39.
- Synthesis: Not every enlargement is the same operation. Ribā can swell over principal, whereas zakāh joins increase to nourishment and purification; doubling is evaluated by the kind of process that produced it, not by final size.

#### Subchannel C. Irrigated Field and Grain Yield
- Reading type: latent/lexical
- Scene or process: Water is routed to soil, the ground is cut by the plough, shoots mature into grain, and harvest becomes transferable yield.
- Active motifs: watercourse directed into a basin `quranic:root_000009:B004/m01`; crop and palm yield `quranic:root_000009:B007/m01`; rain descending between cloud and earth `quranic:root_000672:B005/m01`; grain ear extending from the crop `quranic:root_000672:B008/m01`; cutting and opening soil `quranic:root_001175:B001/m01`; ploughman and cultivation `quranic:root_001175:B003/m01`; fertile planted ground `quranic:root_000025:B002/m01`; rain as provision `quranic:root_000560:B003/m01`; plant increase `quranic:root_000637:B001/m01`.
- Ayah anchors: ء ت ي 30:38-39; ز ك و 30:39; ر ز ق 30:37, 30:40; ء ر ض 30:42; س ب ل 30:38; ف ل ح 30:38.
- Synthesis: Gift and alms become an agricultural production chain: water must move, earth must open, and growth must reach an ear before yield can circulate. The scene distinguishes productive multiplication from increase detached from cultivation.

### 15. P3: Irreversible Route and Prepared Destination
- Semantic invariant: Present orientation and labor prepare the terrain on which a later, irreversible outcome is encountered.
- Surface relation: direct; travel and historical outcome appear in 30:42, the face is set before an unreturnable day in 30:43, and each person prepares for self in 30:44-45.
- Surprising reach: The final division is both a road splitting under the traveler and bedding laid in advance by the occupant.

#### Subchannel A. Facing the Route Before It Splits
- Reading type: mixed
- Scene or process: A traveler aligns with a straight route before the road cracks and its parties move into separate branches with no return.
- Active motifs: upright course `quranic:root_001273:B008/m01`; direction and destination `quranic:root_001630:B002/m01`; obedient path or order `quranic:root_000504:B001/m01`; what comes before `quranic:root_001198:B002/m01`; approaching event `quranic:root_000009:B001/m01`; severe event-day `quranic:root_001700:B003/m01`; barrier against return `quranic:root_000555:B002/m01`; crack in solid material `quranic:root_000850:B001/m01`; road cut lengthwise through terrain `quranic:root_000850:B002/m01`; groups split apart `quranic:root_000850:B005/m01`; extended route `quranic:root_000672:B001/m01`.
- Ayah anchors: س ب ل 30:38; ق و م، و ج ه، د ي ن، ق ب ل، ء ت ي، ي و م، ر د د، ص د ع 30:43.
- Synthesis: Orientation must precede the fracture because the split itself creates irreversible branches. The “no return” day is therefore not only a deadline but a terrain change after which a traveler cannot recover the former road.

#### Subchannel B. Laying One's Own Bedding
- Reading type: mixed
- Scene or process: A person repairs and levels a resting place in advance, and later occupies the condition produced by that work.
- Active motifs: infant's prepared bed `quranic:root_001451:B001/m01`; leveled bedding or ground `quranic:root_001451:B002/m01`; preparing and repairing an affair `quranic:root_001451:B003/m01`; intentional work `quranic:root_001046:B001/m01`; repair opposed to corruption `quranic:root_000876:B001/m01`; self as the beneficiary's own essence `quranic:root_001533:B012/m01`; return matching an act `quranic:root_000244:B001/m01`; surplus favor `quranic:root_001163:B001/m01`; beneficent gift `quranic:root_001163:B003/m01`.
- Ayah anchors: ع م ل، ص ل ح، ن ف س، م ه د 30:44; ج ز ي، ع م ل، ص ل ح، ف ض ل 30:45.
- Synthesis: “Preparing for themselves” becomes literal furnishing: action levels and repairs the place that will bear the actor. Recompense does not import an unrelated destination; it completes the bed already being made, while favor supplies what exceeds strict equivalence.

### 16. P4: Wind-Borne Circulation
- Semantic invariant: A moving medium carries command, matter, and benefit until its effects become visible as travel, rain, and renewed life.
- Surface relation: direct; winds, ships, seeking bounty, cloud formation, rainfall, and revived ground occupy 30:46-50.
- Surprising reach: The cloud is assembled like a dragged and cut covering, while wind links atmospheric transport, maritime circulation, and biological renewal.

#### Subchannel A. Cloud Assembly and Rainfall
- Reading type: surface-primary
- Scene or process: Wind raises suspended matter, drags and spreads cloud, divides it into masses, and releases rain through openings.
- Active motifs: sending and releasing `quranic:root_000563:B001/m01`; wind and moving air `quranic:root_000609:B003/m01`; stirring concealed matter into visibility `quranic:root_000210:B002/m01`; dragging and extending `quranic:root_000680:B001/m01`; cloud drawn through the air `quranic:root_000680:B002/m01`; spreading and extending `quranic:root_000116:B001/m01`; sky canopy `quranic:root_000745:B004/m01`; detached cloud-mass `quranic:root_001298:B004/m01`; opening between masses `quranic:root_000435:B001/m01`; descending rain `quranic:root_001636:B003/m01`; downward rainstroke `quranic:root_000889:B001/m01`; water emerging from confinement `quranic:root_000400:B001/m01`.
- Ayah anchors: ر س ل، ر و ح 30:46; ر س ل 30:47; ر س ل، ر و ح، ث و ر، س ح ب، ب س ط، س م و، ك س ف، خ ل ل، و د ق، خ ر ج، ص و ب 30:48.
- Synthesis: Each verb occupies a distinct stage: release, stirring, transport, extension, partition, passage, and impact. The rain is the output of an atmospheric mechanism whose parts remain intelligible without collapsing them into a general weather motif.

#### Subchannel B. A Cut and Perforated Canopy
- Reading type: latent/lexical
- Scene or process: A large covering is pulled out, spread, cut into pieces, pierced or left with openings, and made to shed fluid through them.
- Active motifs: cloth-like dragging `quranic:root_000680:B001/m01`; spreading material flat `quranic:root_000116:B001/m01`; cutting material apart `quranic:root_001298:B001/m01`; detached piece of cloth or wool `quranic:root_001298:B004/m02`; opening between pieces `quranic:root_000435:B001/m01`; peg or pin inserted through an opening `quranic:root_000435:B005/m01`; thin fabric or lining `quranic:root_000435:B009/m01`; overhead covering `quranic:root_000966:B003/m01`; rain issuing through the covering `quranic:root_001636:B003/m01`.
- Ayah anchors: س ح ب، ب س ط، ك س ف، خ ل ل، و د ق 30:48; ظ ل ل 30:51.
- Synthesis: The cloud body behaves like worked material: it is pulled, spread, cut, and opened. Rain then exits through those openings, giving the visible atmospheric scene a concrete fabrication model without replacing its meteorological reading.

#### Subchannel C. Ship, Current, and Trading Reach
- Reading type: mixed
- Scene or process: Wind drives a vessel through current and waves while an ordered venture seeks continuing surplus.
- Active motifs: wind as motive force `quranic:root_000609:B003/m01`; wind as strength and prevailing power `quranic:root_000609:B011/m01`; flowing water, wind, or ship `quranic:root_000240:B001/m01`; continuing provision `quranic:root_000240:B006/m01`; ship moving in water `quranic:root_001177:B003/m01`; oscillating wave `quranic:root_001177:B007/m01`; command and operative direction `quranic:root_000051:B002/m01`; deliberated management `quranic:root_000051:B007/m01`; seeking a need `quranic:root_000138:B001/m01`; surplus and gift `quranic:root_001163:B001/m01`; tarred or smoothed vessel `quranic:root_000973:B005/m01`.
- Ayah anchors: ر و ح، ج ر ي، ف ل ك، ء م ر، ب غ ي، ف ض ل 30:46; ع ب د 30:48.
- Synthesis: Wind and current make circulation possible, but command and deliberation give it a course. Bounty appears as the surplus reached through a vessel whose hull has been made serviceable for sustained passage.

#### Subchannel D. Reading the Trace of Revival
- Reading type: mixed
- Scene or process: An observer follows a visible remnant from rain's action to living ground and infers the capacity to revive the dead.
- Active motifs: enduring trace indicating a prior event `quranic:root_000011:B003/m01`; following a predecessor's trace `quranic:root_000011:B004/m01`; directed inspection `quranic:root_001520:B001/m01`; merciful beneficence `quranic:root_000552:B001/m01`; earth living by rain `quranic:root_000383:B002/m01`; uncultivated dead ground `quranic:root_001454:B003/m01`; power capable of producing the effect `quranic:root_001205:B003/m01`.
- Ayah anchors: ن ظ ر، ء ث ر، ر ح م، ح ي ي، م و ت، ق د ر 30:50.
- Synthesis: The revived ground is an evidentiary trace, not only an analogy. Looking follows the effect backward to the operative mercy and forward to a larger capacity, so resurrection is inferred through causal continuity.

### 17. P4: Closed and Misoriented Receivers
- Semantic invariant: A message fails when its receiving aperture is sealed or when the recipient turns away from the line of transmission.
- Surface relation: direct; the dead cannot be made to hear, the deaf turn their backs, and the blind cannot be guided in 30:52-53.
- Surprising reach: Deafness and blindness become physical channel failures involving stopped mouths, compact solids, blank terrain, dense cloud, and reversed facing.

#### Subchannel A. Acoustic Closure
- Reading type: mixed
- Scene or process: A call is emitted, but a stopped and compact receiver admits neither sound nor response.
- Active motifs: hearing sound `quranic:root_000741:B001/m01`; causing another to hear `quranic:root_000741:B004/m01`; vocal summons `quranic:root_000478:B001/m01`; loss of hearing or refusal to listen `quranic:root_000884:B001/m01`; stopper closing a vessel's mouth `quranic:root_000884:B002/m01`; compact body with no opening `quranic:root_000884:B003/m01`; sound whose impact disappears `quranic:root_000884:B006/m01`; overwhelming sound `quranic:root_000884:B014/m01`; stillness like sleep or worn matter `quranic:root_001454:B012/m01`; turning the back `quranic:root_000458:B003/m01`.
- Ayah anchors: س م ع، م و ت، ص م م، د ع و، د ب ر 30:52; س م ع 30:53.
- Synthesis: Increasing volume cannot solve a closed aperture. The stopper and compact-solid senses explain why even a “deafening” sound fails: the problem lies in admission and orientation, not in insufficient emission.

#### Subchannel B. Blind Route and Reversed Facing
- Reading type: mixed
- Scene or process: A traveler in blank terrain loses the route, while a guide and trace are rendered useless when the traveler faces away.
- Active motifs: loss of sight `quranic:root_001049:B001/m01`; blindness of judgment and route `quranic:root_001049:B002/m01`; dense dark cloud or dust `quranic:root_001049:B005/m01`; unknown unmarked land `quranic:root_001049:B006/m01`; deviation from the intended route `quranic:root_000913:B001/m01`; strayed animal `quranic:root_000913:B005/m01`; gentle route-guidance `quranic:root_001583:B001/m01`; leading front or marker `quranic:root_001583:B003/m01`; enduring trace `quranic:root_000011:B003/m01`; facing toward a signal `quranic:root_001684:B006/m01`; turning away `quranic:root_001684:B007/m01`.
- Ayah anchors: ء ث ر 30:50; و ل ي 30:52; ه د ي، ع م ي، ض ل ل 30:53.
- Synthesis: Blindness is not only lack of visual input; it is being unable to find a route in terrain with no mark. Guidance requires both an external lead and a receiver facing it, so turning away reproduces blindness even where a trace remains.

### 18. P4: Senescence Made Visible
- Semantic invariant: Declining vitality becomes legible in color, dryness, and loss of load-bearing strength.
- Surface relation: direct; vegetation turns yellow in 30:51 and human weakness, strength, renewed weakness, and white hair are sequenced in 30:54.
- Surprising reach: Crop senescence and human aging are parallel material transformations from growing tissue to pale, emptied structure.

#### Subchannel A. Vegetation Passing into Yellow Emptiness
- Reading type: mixed
- Scene or process: Wind acts on living growth until green tissue yellows, dries, and approaches the state of dead ground.
- Active motifs: wind and moving air `quranic:root_000609:B003/m01`; leafing and lengthening vegetation `quranic:root_000609:B017/m01`; yellow coloration `quranic:root_000869:B001/m01`; yellow or dried plant `quranic:root_000869:B007/m01`; emptiness after loss of contents `quranic:root_000869:B002/m01`; dead uncultivated ground `quranic:root_001454:B003/m01`; later phase following an earlier one `quranic:root_000131:B002/m01`.
- Ayah anchors: م و ت 30:50, 30:52; ر و ح، ص ف ر، ب ع د 30:51.
- Synthesis: Yellowing is the visible middle state between leafy vitality and empty dead matter. The reaction of covering or denial after seeing that change is pressured by the plant itself, whose color openly records the transition.

#### Subchannel B. Body Passing from Weakness to Strength and Back
- Reading type: mixed
- Scene or process: A formed body gains tensile strength, then loses it as hair and exposed surfaces whiten.
- Active motifs: bodily and mental weakness `quranic:root_000909:B001/m01`; gathered tensile strength like strands of rope `quranic:root_001274:B001/m01`; white hair of age `quranic:root_000833:B001/m01`; whitening like frost or snow on high ground `quranic:root_000833:B002/m01`; created visible form `quranic:root_000434:B003/m01`; later phase following an earlier one `quranic:root_000131:B002/m01`; measured capacity `quranic:root_001205:B001/m01`.
- Ayah anchors: خ ل ق، ض ع ف، ب ع د، ق و ي، ش ي ب، ق د ر 30:54.
- Synthesis: Strength is a temporary gathering of load-bearing strands, not the body's permanent essence. Whitening externalizes the later loosening of that gathered force, making age a visible phase change in the same created material.

### 19. P4: Text, Imprint, and False Inversion
- Semantic invariant: Meaning is assembled and patterned into a record whose imprint may authenticate truth or mechanically preserve a false orientation.
- Surface relation: direct; book, knowledge, Qur'an, examples, speech, falsehood, sealing, hearts, and truth occur in 30:56, 30:58-60.
- Surprising reach: Scripture and denial are treated through bookbinding, pattern transfer, stamping, counterfeit claims, and inversion of a form.

#### Subchannel A. Composed and Patterned Utterance
- Reading type: mixed
- Scene or process: Units are gathered, joined, written, read, and patterned into examples that carry meaning to an audience.
- Active motifs: gathering units into a whole `quranic:root_001210:B001/m01`; reading and recitation `quranic:root_001210:B002/m01`; joining or stitching material `quranic:root_001283:B001/m01`; ordered writing `quranic:root_001283:B002/m01`; inscription fixing judgment or decree `quranic:root_001283:B003/m01`; entry into a register `quranic:root_001283:B004/m01`; presenting a model `quranic:root_000906:B003/m01`; repeatable pattern or type `quranic:root_000906:B007/m01`; represented example `quranic:root_001397:B008/m01`; spoken utterance `quranic:root_001272:B001/m01`.
- Ayah anchors: ق و ل، ك ت ب 30:56; ض ر ب، ق ر ء، م ث ل، ق و ل 30:58.
- Synthesis: Qur'an is both gathered utterance and joined record. Examples are not ornaments added to that record; they are transferable patterns that make its judgments readable in another configuration.

#### Subchannel B. Authentication Versus Reversed Impression
- Reading type: mixed
- Scene or process: A stamp fixes an impression, but a reversed die or counterfeit claim reproduces distortion instead of truth.
- Active motifs: sealing and stamping by a die `quranic:root_000926:B001/m01`; formative imprint or disposition `quranic:root_000926:B002/m01`; die, measure, or template `quranic:root_000926:B006/m01`; truth matching a fixed reality `quranic:root_000347:B001/m01`; inversion away from proper direction `quranic:root_000041:B001/m01`; great lie turned from truth `quranic:root_000041:B002/m01`; falsehood without stability `quranic:root_000127:B001/m01`; false claim with no reality `quranic:root_000127:B003/m01`; turning a thing from face to face `quranic:root_001248:B004/m01`; attributing words never spoken `quranic:root_001272:B005/m01`.
- Ayah anchors: ء ف ك 30:55; ق و ل، ب ط ل 30:58; ط ب ع، ق ل ب 30:59; ح ق ق 30:60.
- Synthesis: A seal preserves whatever orientation the die carries. Thus sealing a heart is not neutral closure: repeated inversion has become a fixed impression, while haqq names the correctly aligned form against which the counterfeit can be tested.

### 20. P4: Risen Parties, Adjudicated Claims, and Release
- Semantic invariant: At an appointed event, held persons and recorded statuses are activated, claims are heard, and binding relations reach execution or release.
- Surface relation: direct; resurrection, disputed duration, the book, excuses, and judgment occupy 30:55-57, while promise and truth close the pericope in 30:60.
- Surprising reach: The final scene includes the mechanics of waking a tethered body, courtroom pleading, and a deferred manumission contract executable at death.

#### Subchannel A. Rousing and Correcting Duration
- Reading type: mixed
- Scene or process: A stationary body is roused and dispatched; its mistaken sense of elapsed time is corrected by a fixed record.
- Active motifs: stirring a resting or tethered creature `quranic:root_000129:B001/m01`; dispatching one sent on a task `quranic:root_000129:B002/m01`; group surging into motion `quranic:root_000129:B004/m01`; resurrection-standing `quranic:root_001273:B013/m01`; severe event-day `quranic:root_001700:B003/m01`; remaining in a place `quranic:root_001339:B001/m01`; delay and sluggishness `quranic:root_001339:B002/m01`; fixed decree in a record `quranic:root_001283:B003/m01`.
- Ayah anchors: ي و م، ق و م، ل ب ث 30:55; ك ت ب، ي و م، ب ع ث 30:56.
- Synthesis: Baʿth combines waking with dispatch: the formerly still body is not merely conscious but sent into the event. The book corrects subjective duration by supplying the fixed temporal record within which the stay actually occurred.

#### Subchannel B. Failed Excuse Before the Forum
- Reading type: mixed
- Scene or process: Parties swear, plead, and seek restored satisfaction, but a defective excuse cannot alter the adjudicated record.
- Active motifs: oath distributed among parties `quranic:root_001226:B004/m01`; division and allotment `quranic:root_001226:B003/m01`; criminal offense `quranic:root_000239:B004/m01`; grievance seeking redress `quranic:root_000967:B003/m01`; blame addressed to an offender `quranic:root_000977:B005/m01`; return intended to satisfy the aggrieved `quranic:root_000977:B006/m01`; plea for erasure of blame `quranic:root_000995:B001/m01`; feigned or deficient excuse `quranic:root_000995:B005/m01`; impossible or nonviable plea `quranic:root_000995:B006/m01`; absence of benefit `quranic:root_001536:B001/m01`; fixed judicial truth `quranic:root_001283:B003/m01`.
- Ayah anchors: ق س م، ج ر م 30:55; ك ت ب 30:56; ن ف ع، ظ ل م، ع ذ ر، ع ت ب 30:57.
- Synthesis: The excuse is a procedural attempt to reopen satisfaction, but its defect is now substantive: it cannot fit the fixed record. Oath and plea remain speech acts, yet neither changes the allotted status once the forum has reached execution.

#### Subchannel C. Deferred Manumission at Death
- Reading type: latent/lexical
- Scene or process: An enslaved person's release is promised for the owner's death and secured through a written manumission contract.
- Active motifs: enslaved property `quranic:root_000973:B001/m01`; making another a slave `quranic:root_000973:B004/m01`; incapacitation and interruption of service `quranic:root_000973:B011/m01`; deferred emancipation after an owner's death `quranic:root_000458:B007/m01`; written manumission contract `quranic:root_001283:B005/m01`; loss of life `quranic:root_001454:B001/m01`; reciprocal promise `quranic:root_001662:B004/m01`.
- Ayah anchors: ع ب د 30:48; م و ت 30:50, 30:52; د ب ر 30:52; ك ت ب 30:56; و ع د 30:60.
- Synthesis: Death, record, and promise assemble a complete legal release mechanism. The deferred contract gives resurrection-era freedom a precise pressure point: a status held under ownership can be terminated when the death-conditioned writing becomes executable.

### 21. P4: Steadiness Against Destabilization
- Semantic invariant: Endurance maintains inner position and bodily footing against forces that lighten, unsettle, or obstruct.
- Surface relation: indirect; hard closure and guidance appear in 30:52-53, failed pleading at a threshold in 30:57, and patience, promise, truth, lightness, and certainty in 30:60.
- Surprising reach: Final patience is both a sealed container preserving conviction and a careful ascent over rough stone.

#### Subchannel A. Containing Conviction
- Reading type: mixed
- Scene or process: A vessel and its contents are held steady against agitation, lightening, and attempted devaluation.
- Active motifs: self-restraint against agitation `quranic:root_000840:B001/m01`; stopper sealing a vessel `quranic:root_000840:B018/m01`; vessel's retaining sides `quranic:root_000840:B004/m01`; reduction of weight or burden `quranic:root_000427:B001/m01`; frivolous agitation `quranic:root_000427:B004/m01`; belittling a right `quranic:root_000427:B005/m01`; fixed knowledge beyond doubt `quranic:root_001696:B001/m01`; binding promise `quranic:root_001662:B001/m01`; appointed promise `quranic:root_001662:B003/m01`; truth fixed to reality `quranic:root_000347:B001/m01`; heart turned or kept in orientation `quranic:root_001248:B004/m01`.
- Ayah anchors: ق ل ب 30:59; ص ب ر، و ع د، ح ق ق، خ ف ف، ي ق ن 30:60.
- Synthesis: Patience acts as containment: it keeps conviction from spilling under agitation or being made “light.” Promise, truth, and certainty give the contents their weight, while the stopper image explains endurance as maintained closure rather than passivity.

#### Subchannel B. Footing on a Rough Ascent
- Reading type: latent/lexical
- Scene or process: A traveler crosses hard ground, negotiates an elevated threshold, and preserves joints and footing through the ascent.
- Active motifs: coarse stone and stony ground `quranic:root_000840:B005/m01`; mountain mass `quranic:root_000840:B017/m01`; raised threshold or step `quranic:root_000977:B001/m01`; broken three-footed gait over steps `quranic:root_000977:B004/m01`; hard compact terrain `quranic:root_000884:B004/m01`; hoof or protective footwear `quranic:root_000427:B006/m01`; bones and joints of foot and hand `quranic:root_000737:B010/m01`; route-guidance `quranic:root_001583:B001/m01`.
- Ayah anchors: ص م م 30:52; ه د ي، س ل م 30:53; ع ت ب 30:57; ص ب ر، خ ف ف 30:60.
- Synthesis: The closing exhortation also describes a problem of footing. Patience is the capacity to remain coordinated over stone and threshold, while those who would make the traveler light threaten the stable weight needed for ascent.

### 22. P1/P2/P3/P4: Water from Atmospheric Signal to Evidentiary Revival
- Semantic invariant: Water passes through an ordered relay of announcement, descent, capture or routing, cultivation, and visible restored life.
- Surface relation: direct; dead earth is brought to life in P1 at 30:19, lightning announces descending water and revived earth in P2 at 30:24, provision and productive increase are tested in P3 at 30:37-40, and winds, cloud, rain, and the trace of revival form a continuous sequence in P4 at 30:46-50.
- Pericopes and bridge: P1 (30:1-19) to P2 (30:20-32) to P3 (30:33-45) to P4 (30:46-60); a causal sequence and role progression from promised relief, through atmospheric opening and irrigated production, to inspectable evidence of revival.
- Canonical scene placements: P1, `Water-Borne Restoration`; P2, `Storm Signal and Hydrological Opening`; P3, `Irrigated Field and Grain Yield`; P4, `Cloud Assembly and Rainfall` and `Reading the Trace of Revival`.
- Surprising reach: Revival is credible not merely because rain and growth resemble resurrection, but because the surah repeatedly exposes the intervening mechanism. Mercy becomes effective by moving through each stage, and its final trace can therefore bear witness to the ordered power that produced it.

### 23. P1/P2/P3/P4: Route from Waymark to Irreversible Fork
- Semantic invariant: Guidance requires an external trace or lead to agree with the traveler's facing and footing before the route divides.
- Surface relation: direct; travel and آثار invite route-reading in P1 at 30:9, guidance is enacted by face, stance, and following in P2 at 30:29-32, the route reaches an unreturnable split in P3 at 30:42-43, and P4 contrasts the remaining trace with blind or reversed reception at 30:50-53 before closing on steadiness at 30:60.
- Pericopes and bridge: P1 (30:1-19) to P2 (30:20-32) to P3 (30:33-45) to P4 (30:46-60); a repeated scene signature and role progression, followed by reversal: waymark and moving guide, oriented walker and gathered followers, irreversible fork, then the traveler who turns away and loses the route.
- Canonical scene placements: P1, `A Marked Route Through Terrain` and `Celestial Navigation by Moving Lights`; P2, `Guided Gait and Fragmented Following`; P3, `Facing the Route Before It Splits`; P4, `Blind Route and Reversed Facing` and `Footing on a Rough Ascent`.
- Surprising reach: The signs do not operate as detached proofs. They furnish a traversable course whose success depends on bodily alignment before the terrain changes; final blindness is thus the reversal of sustained route-use, not simply the absence of available direction.

### 24. P1/P2/P4: Measure, Pattern, and Authenticated Impression
- Semantic invariant: A truthful form preserves correspondence with a prior measure or exemplar as it passes from design to visible surface, transferable pattern, record, and imprint.
- Surface relation: direct; P1 contrasts outward appearance with inward reflection, truth, and fabricated display at 30:7-10; P2 joins creation, exemplar, fitrah, and non-substitution at 30:27-30; P4 joins book, recitation, examples, falsehood, sealing, and truth at 30:55-60.
- Pericopes and bridge: P1 (30:1-19) to P2 (30:20-32) to P4 (30:46-60); a repeated craft signature and role progression, sharpened by contrast: measured interior and tested surface, exemplar and durable formation, then patterned utterance and an authentic or reversed impression.
- Canonical scene placements: P1, `Turning the Surface Toward the Interior` and `Counterfeit Display Versus Verified Sign`; P2, `Pattern, Exemplar, and Unaltered Formation`; P4, `Text, Imprint, and False Inversion`.
- Surprising reach: Creation, innate formation, example, scripture, and sealed response become successive problems of faithful pattern transmission. Falsehood is not merely missing information; it is a surface or impression that no longer corresponds to the measure it claims to express.

### 25. P1/P2/P3/P4: Claim from Shared Interest to Executed Status
- Semantic invariant: Shares, rights, acts, and binding statuses become explicit through transfer and are finally tested against an authoritative record.
- Surface relation: direct; partners, intercession, earned acts, and division appear in P1 at 30:12-16; ownership, equality, and shared provision in P2 at 30:28; measured provision, claimant rights, transfer, and increase in P3 at 30:37-40; and oath, record, excuse, judgment, and promise in P4 at 30:55-60.
- Pericopes and bridge: P1 (30:1-19) to P2 (30:20-32) to P3 (30:33-45) to P4 (30:46-60); a role progression and causal sequence from co-owner or would-be advocate, through owner, partner, giver, and claimant, to litigant or bound person whose status is executed or released.
- Canonical scene placements: P1, `Claims Brought to Division`; P2, `Shared Property and Settlement`; P3, `Allotment, Claimant, and Transfer`; P4, `Failed Excuse Before the Forum` and `Deferred Manumission at Death`.
- Surprising reach: Final division is not an arbitrary partition imposed after the fact. The surah first makes the grammar of share, authority, due transfer, and accrued liability concrete, so adjudication completes relations and statuses already formed within action.

### 26. P1/P4: Appointed Time and Corrected Duration
- Semantic invariant: Counted time acquires force from an appointment or promise, while subjective duration remains answerable to the fixed sequence and its record.
- Surface relation: direct; P1 binds reversal to a counted term and places praise within recurring daily rounds at 30:2-6 and 30:17-18, while P4 corrects disputed duration by the book and the Day at 30:55-56 and closes with the truth of the promise at 30:60.
- Pericopes and bridge: P1 (30:1-19) to P4 (30:46-60); a temporal role progression and contrast from prospective counting toward an appointed reversal to retrospective correction of a misremembered stay.
- Canonical scene placements: P1, `Bounded Reversal of Power` and `The Day as a Scheduled Round`; P4, `Rousing and Correcting Duration`.
- Surprising reach: The earlier bounded reversals and recurring rounds train attention on time as an ordered medium rather than an impression. At the final rousing, felt duration cannot revise that order; the record restores the interval to the appointment that gave it meaning.

### 27. P2/P4: Call, Release, and Closed Reception
- Semantic invariant: A summons changes state only where a receiver admits the signal and can convert hearing into directed response.
- Surface relation: direct; an authoritative call brings bodies out in P2 at 30:25, whereas the dead, deaf, and turned-away cannot be made to hear the call in P4 at 30:52-53.
- Pericopes and bridge: P2 (30:20-32) to P4 (30:46-60); an exact contrast and reversal between a call that releases emergence from a held system and the same call-role meeting a stopped aperture and reversed receiver.
- Canonical scene placements: P2, `The Call That Releases Emergence`; P4, `Acoustic Closure`.
- Surprising reach: Resurrection and guidance share a signal-transfer structure without becoming the same event. The successful scene exposes what the failed scene lacks: the obstacle is not weak emission but a receiver whose closure prevents summons from becoming movement.

## Standalone Subchannels

### S1. P1: Measured Joinery of Creation and Civilization
- Reading type: latent/lexical
- Scene or process: A planned structure is measured, tightly joined, bound, strengthened, furnished, inhabited, and kept standing by load-bearing parts.
- Active motifs: measurement before making `quranic:root_000434:B001/m01`; tightly finished weave or speech `quranic:root_000347:B010/m01`; fitted joint or socket `quranic:root_000347:B011/m01`; tightened binding `quranic:root_000782:B001/m01`; rope-strand strength `quranic:root_001274:B001/m01`; habitation repaired against ruin `quranic:root_001044:B003/m01`; structural support and subsistence `quranic:root_001273:B009/m01`; standing tool or component `quranic:root_001273:B012/m01`; thick woven floor covering `quranic:root_000025:B005/m01`.
- Ayah anchors: خ ل ق، ح ق ق 30:8; ء ر ض، ش د د، ق و ي، ع م ر 30:9; ق و م 30:12, 30:14.
- Synthesis: Creation and the stronger civilizations encountered in the earth resolve into an act of measured joinery. Fit, binding, tensile strength, upright supports, and repaired habitation materialize what it means for a world or polity to be soundly made; even a structure of great force remains dependent on its joints and upkeep.

### S2. P1: Womb, Delivery, and Loss
- Reading type: latent/lexical
- Scene or process: Life is conceived and enclosed, emerges into receiving hands through birth, and remains exposed to the death of a child.
- Active motifs: womb as a vessel of growth `quranic:root_000552:B003/m01`; reproductive organ `quranic:root_000383:B011/m01`; childbirth and postpartum blood `quranic:root_001533:B005/m01`; midwife receiving the emerging child `quranic:root_001198:B007/m01`; rapid conception `quranic:root_001372:B003/m01`; emergence from an enclosure `quranic:root_000400:B001/m01`; parental loss of a child `quranic:root_001454:B005/m01`.
- Ayah anchors: ر ح م 30:5; ل ق ي 30:8, 30:16; ن ف س 30:8, 30:9; ق ب ل 30:4, 30:9; ح ي ي، خ ر ج، م و ت 30:19.
- Synthesis: The claim that the living is brought from the dead acquires a complete bodily scene: conception, protected gestation, delivery into another's hands, and the possible reversal of parental bereavement. Emergence is neither abstract nor frictionless; life passes through a vulnerable enclosure and a blood-marked threshold.

### S3. P1: Watered and Adorned Garden
- Reading type: mixed
- Scene or process: A garden is saturated, made spacious and tractable through tending, then becomes lush, beautiful, and joy-bearing.
- Active motifs: saturation by watering `quranic:root_000611:B003/m01`; spaciousness of place and spirit `quranic:root_000611:B004/m01`; softening through repeated training or tending `quranic:root_000611:B005/m01`; beauty and adornment `quranic:root_000287:B002/m01`; joy, favor, and honor `quranic:root_000287:B005/m01`; lush land and water-heavy cloud `quranic:root_000287:B007/m01`; restorative cultivation against spoilage `quranic:root_000876:B001/m01`.
- Ayah anchors: ر و ض، ح ب ر، ص ل ح 30:15.
- Synthesis: The garden of 30:15 is not only a destination but a cultivated condition. Water saturates the ground, tending makes it responsive, and fertility flowers into both visible adornment and inward joy, so delight appears as the outcome of sustained restorative care.

### S4. Whole-Surah: Drawing the Gambling Arrows
- Reading type: latent/lexical
- Scene or process: Named gambling arrows are held in a leather container, drawn as allotted stakes, and distinguished by rank and loss.
- Active motifs: leather case holding a gambling-arrow set `quranic:root_000532:B010/m01`; the ma'la arrow in the set `quranic:root_001042:B009/m01`; the nafis fifth arrow `quranic:root_001533:B016/m01`; the losing dabir arrow and forfeited stake `quranic:root_000458:B019/m01`.
- Ayah anchors: ر ب ب، ن ف س 30:8; ع ل و 30:27; د ب ر 30:52.
- Synthesis: The draw converts concealed lots into public allotment, immediately separating a named share from the losing result. This scene usefully pressures the surah's appointed reversals and final division: those outcomes are not chance lots shaken from a case, but consequences fixed by promise, truth, and prior action.

### S5. Whole-Surah: Hunter's Lure, Snare, and Kill Check
- Reading type: latent/lexical
- Scene or process: Hunters go out, stage a decoy, set catching devices, entangle prey, and inspect the struck animal to determine whether it has died.
- Active motifs: departure on a hunt `quranic:root_000745:B006/m01`; hunter's noose or trapping net `quranic:root_000791:B006/m01`; snare deliberately set for capture `quranic:root_000879:B004/m01`; decoy bird placed inside a net `quranic:root_000951:B005/m01`; inspection establishing whether prey is dead `quranic:root_001454:B014/m01`.
- Ayah anchors: س م و 30:8; ش ر ك 30:13; ط م ع 30:24; ص ل و 30:31; م و ت 30:50.
- Synthesis: Attraction, capture, and verification form one controlled sequence: what looks approachable may have been positioned as bait, and the outcome must still be examined rather than assumed. The scene reframes the surah's visible signs, hope, and life-death contrasts by showing why perceptual attraction requires discernment and why a claim about death demands an established effect.

### S6. Whole-Surah: Summons, Qibla, and Prayer
- Reading type: mixed
- Scene or process: A summons gathers worshippers, who face a fixed direction, perform the bounded postures of prayer, and withhold ordinary speech while engaged in it.
- Active motifs: "come to prayer" summons `quranic:root_000383:B009/m01`; qibla as the direction faced in prayer `quranic:root_001198:B005/m01`; formal prayer with standing, bowing, and prostration `quranic:root_000879:B003/m01`; prayerful silence from ordinary human speech `quranic:root_001260:B004/m01`.
- Ayah anchors: ق ب ل 30:4; ح ي ي 30:19; ق ن ت 30:26; ص ل و 30:31.
- Synthesis: The rite materializes the command to set the face toward the upright religion and establish prayer in 30:30-31. Orientation becomes coordinated direction, posture, and speech restraint, while the factional turning of 30:32 is usefully pressured as a failure to sustain a shared embodied alignment.

### S7. Whole-Surah: Grinding and Applying Perfume
- Reading type: latent/lexical
- Scene or process: Camphor is worked on a broad grinding stone into an applied perfume whose scent is perceived as it diffuses beyond the treated surface.
- Active motifs: camphor as an aromatic material `quranic:root_001307:B011/m01`; broad stone for grinding aromatics `quranic:root_000879:B008/m01`; khaluq perfume and coating with it `quranic:root_000434:B010/m01`; scent acquired and perceived `quranic:root_000609:B004/m01`; fragrance spreading through the air `quranic:root_001503:B003/m01`.
- Ayah anchors: خ ل ق، ك ف ر 30:8; ن ش ر 30:20; ص ل و 30:31; ر و ح 30:46.
- Synthesis: Grinding, application, and diffusion turn a compact substance into a perceptible effect at a distance. This materializes the surah's wind-sign logic in 30:46-48: an unseen moving medium announces a prior source through what it carries, just as the mercy borne by wind becomes legible before its full result arrives.

### S8. Whole-Surah: Postpartum Complication and Restorative Food
- Reading type: latent/lexical
- Scene or process: A postpartum body suffers retained afterbirth, uterine pain, and discharge while a date-and-fenugreek remedy is cooked, safely removed from the fire, and taken during recovery.
- Active motifs: uterine pain, swelling, or retained afterbirth `quranic:root_000552:B004/m01`; pooled discharge and afterbirth following delivery `quranic:root_000333:B008/m01`; medicinal date-and-fenugreek dish for a postpartum woman `quranic:root_001148:B012/m01`; cooking pot, broth, and attending cook `quranic:root_001205:B007/m01`; cloth used to lower a hot pot from the fire `quranic:root_000248:B007/m01`; recovery from childbed `quranic:root_001042:B011/m01`.
- Ayah anchors: ر ح م 30:5; ف ر ق 30:14; ح ض ر 30:16; ع ل و 30:27; ق د ر 30:37; ج ع ل، ق د ر 30:54.
- Synthesis: The body does not pass immediately from delivery to restored strength; pain and retained matter create an interval answered by prepared food, careful handling, and convalescence. This usefully pressures the weakness-to-strength sequence of 30:54 with the hidden labor of care, making mercy and provision operative conditions of recovery rather than decorative accompaniments to it.

### S9. Whole-Surah: Marriage, Separation, and Return
- Reading type: latent/lexical
- Scene or process: A marriage is contracted and consummated; separation then either preserves a right of return or cuts it, after which a divorced or widowed woman may receive new suitors.
- Active motifs: marriage contract establishing marital access `quranic:root_000123:B003/m01`; marital touch and intimacy `quranic:root_001423:B002/m01`; divorce that severs the right of return `quranic:root_000170:B012/m01`; revocable return to one's wife `quranic:root_000544:B004/m01`; suitors approaching a divorced or widowed woman `quranic:root_000563:B009/m01`.
- Ayah anchors: ب ض ع 30:4; ب ي ن 30:21; م س س 30:33; ر ج ع 30:41; ر س ل 30:46.
- Synthesis: Pairing is shown as a social bond with enacted rights, alternative forms of separation, and possible re-entry into courtship. The scene usefully pressures the tranquility, affection, and mercy of 30:21: marital rest is not an automatic property of paired bodies, but a relationship whose continuity can be legally maintained, broken, or restored.

### S10. Whole-Surah: Well, Pulley, and Watering Line
- Reading type: latent/lexical
- Scene or process: A pulley turns over a well, a handled bucket is balanced and filled, and the lifted water is delivered directly to animals and water drawers.
- Active motifs: open well `quranic:root_001248:B007/m01`; rotating iron axle of a pulley `quranic:root_000610:B006/m01`; one-handled water-drawer's bucket `quranic:root_000737:B011/m01`; bucket handle or side that balances its load `quranic:root_000741:B008/m01`; filling a bucket to its limit `quranic:root_000926:B003/m01`; watering camels at their mouths `quranic:root_001198:B014/m01`; water drawers drinking from a full bucket `quranic:root_001274:B005/m01`.
- Ayah anchors: ر و د 30:38; ق ب ل 30:49; س م ع، س ل م 30:53; ق و ي 30:54; ق ل ب، ط ب ع 30:59.
- Synthesis: Water becomes usable through rotation, balance, measured capacity, lifting, and delivery to dependent bodies. This materializes the surah's rain and provision sequence: mercy does not remain atmospheric, but enters an ordered mechanism whose aligned parts carry it to mouths and restore bodily force.

### S11. Whole-Surah: Guided Swarm and Honey Harvest
- Reading type: latent/lexical
- Scene or process: A bee leader organizes a swarm that repeatedly returns to its home, producing thick honey or comb that a beekeeper gathers into a leather bag.
- Active motifs: swarm of bees or wasps `quranic:root_000458:B014/m01`; leading ya'sub of the bees `quranic:root_001444:B008/m01`; bees named for returning to their homes `quranic:root_001562:B005/m01`; thick honey or honeycomb `quranic:root_000906:B015/m01`; beekeeper's leather honey bag `quranic:root_000447:B006/m01`.
- Ayah anchors: خ و ف، ض ر ب، م ل ك 30:28; ن و ب 30:31; د ب ر 30:52.
- Synthesis: Coordinated following and repeated return culminate in stored provision that can be gathered and carried. The scene usefully pressures the surah's contrast between repentant return and factional fragmentation: unlike parties satisfied with separate portions, the swarm follows a leading order, returns to one home, and converts circulation into shared yield.

### S12. Whole-Surah: Water-Clear Mirror and Surface Inspection
- Reading type: mixed
- Scene or process: A viewer examines a face in a water-clear crystal mirror and judges the visible marks and appearance presented by its surface.
- Active motifs: mirror and facial appearance `quranic:root_000531:B006/m01`; water-clear crystal mirror `quranic:root_001458:B007/m01`; appearance pleasing or troubling to its viewer `quranic:root_001520:B004/m01`.
- Ayah anchors: ر ء ي 30:24, 30:37, 30:48, 30:51; م و ه 30:24; ن ظ ر 30:9, 30:42, 30:50.
- Synthesis: The mirror gives exact access to an outward image while withholding what lies behind it. It usefully pressures the contrast of 30:7-8: visible appearance can be clear and still remain only a reflected face, so reflection must pass beyond surface judgment to the measure and intention that produced the form.

### S13. Whole-Surah: Camel Saddle Layers Under Load
- Reading type: latent/lexical
- Scene or process: A saddlecloth and under-pad are fitted and strapped to a riding camel, but excessive pace abrades the loaded back until the animal sores and stops.
- Active motifs: saddlecloth around a camel's hump `quranic:root_000766:B010/m01`; joined bridle and tack components `quranic:root_001198:B010/m01`; riding or load-bearing camel `quranic:root_000970:B005/m01`; under-saddle blanket `quranic:root_001684:B011/m01`; pace that exhausts the back `quranic:root_000347:B012/m01`; saddle sore on a camel's back `quranic:root_000458:B017/m01`; camel halted by exhaustion or injury `quranic:root_000286:B005/m01`.
- Ayah anchors: س و ي 30:28; ق ب ل 30:4, 30:9, 30:42-43, 30:47, 30:49; ظ ه ر 30:7, 30:18, 30:41; و ل ي 30:52; ح ق ق 30:8, 30:38, 30:47, 30:60; د ب ر 30:52; ح ب ب 30:45.
- Synthesis: Stable travel depends on layered protection, joined restraints, and a load matched to the carrier. The scene materializes the surah's strength-to-weakness reversals and guided movement: force without measure consumes the body that bears the journey, while properly fitted restraint preserves its capacity to continue.

### S14. Whole-Surah: Sewn Mosquito Screen over a Sleeping Mat
- Reading type: mixed
- Scene or process: A mat is spread beneath a leather canopy and enclosed by a fine sewn screen that provides shade while excluding biting insects.
- Active motifs: biting mosquito `quranic:root_000133:B002/m01`; spread mat or level ground `quranic:root_000116:B002/m01`; leather dome or screen `quranic:root_000156:B004/m01`; protective shade `quranic:root_000966:B001/m01`; sewn mosquito-net enclosure `quranic:root_001315:B006/m01`.
- Ayah anchors: ب ع ض 30:41; ب س ط 30:37, 30:48; ب ن ي 30:38; ظ ل ل 30:51; ك ل ل 30:26, 30:32, 30:50, 30:58.
- Synthesis: Repose is produced by a selective boundary: the enclosure admits air and inhabitation while keeping small harms away from the sleeper. This materializes the dwelling and sleep of 30:21-23 as protected habitability, making tranquility an achieved relation between body, shelter, and surrounding disturbance.

### S15. Whole-Surah: Eye Film and Functionless Globe
- Reading type: mixed
- Scene or process: An eye remains visibly present, even protruding, while a vascular film or localized lesion covers it and leaves the intact globe without sight.
- Active motifs: vascular film spread over the eye `quranic:root_000672:B010/m01`; protruding visible eye `quranic:root_000970:B009/m01`; intact eye globe with lost sight `quranic:root_001273:B021/m01`; ocular spot, blister, or lesion `quranic:root_001636:B004/m01`.
- Ayah anchors: س ب ل 30:38; ظ ه ر 30:7, 30:18, 30:41; ق و م 30:12, 30:14, 30:21, 30:23-25, 30:28, 30:30-31, 30:37, 30:43, 30:47, 30:55; و د ق 30:48.
- Synthesis: The organ's visible presence does not guarantee its operation; a thin intervening layer can leave form intact while disabling reception. The diagnosis sharpens the blindness of 30:53: signs may remain before the receiver, yet an internalized obstruction can make a functioning route of sight unavailable.

### S16. Whole-Surah: Abscess from Swelling to Scar
- Reading type: mixed
- Scene or process: A wound swells and spreads beyond its initial boundary, gathers pus, rises outward as an abscess, and leaves a distinguishing mark.
- Active motifs: wound swelling and advancing into corruption `quranic:root_000138:B004/m01`; collected pus in a wound `quranic:root_000282:B003/m01`; abscess emerging from the body `quranic:root_000400:B004/m01`; residual wound mark or scar `quranic:root_000995:B017/m01`.
- Ayah anchors: ب غ ي 30:23, 30:46; ج ي ء 30:9, 30:47, 30:58; خ ر ج 30:19, 30:25, 30:48; ع ذ ر 30:57.
- Synthesis: Corruption develops as a causal pathology: a local breach exceeds its limit, concealed matter accumulates, and the injury becomes externally legible before persisting as a trace. This usefully reframes the appearing corruption of 30:41 as systemic damage made visible by what it produces and leaves behind.

### S17. Whole-Surah: Repairing Termite-Damaged Timber
- Reading type: latent/lexical
- Scene or process: Insect-eaten timber is cut with a saw, shaped with an adze, and fitted as ribs and supports that keep a structure from falling.
- Active motifs: termite consuming wood `quranic:root_000025:B010/m01`; adze for shaping timber `quranic:root_001207:B008/m01`; sawing wood `quranic:root_001503:B005/m01`; structural ribs and resting supports `quranic:root_000156:B009/m01`; load-bearing support that prevents collapse `quranic:root_000555:B009/m01`.
- Ayah anchors: ء ر ض 30:3, 30:8-9, 30:18-19, 30:22, 30:24-27, 30:42, 30:50; ق د م 30:36; ن ش ر 30:20; ب ن ي 30:38; ر د د 30:43.
- Synthesis: The repair scene exposes the dependence of monumental strength on small material conditions. It pressures the civilizations of 30:9 and the surah's created order: a structure may look established while insects hollow its members, and continued standing requires skilled removal, reshaping, and replacement of compromised support.

### S18. Whole-Surah: Fretted Oud and Alternating Song
- Reading type: latent/lexical
- Scene or process: A fretted wooden oud is played beneath singers who alternate and ornament a repeated melodic line for an attentive audience.
- Active motifs: wooden oud as musical instrument `quranic:root_001058:B010/m01`; transverse frets on the oud `quranic:root_000977:B009/m01`; implement used to play the instrument `quranic:root_000906:B014/m01`; repeated or ornamented vocal line `quranic:root_000544:B007/m01`; alternating performers `quranic:root_000563:B008/m01`; pleasurable singing and listening `quranic:root_000741:B007/m01`.
- Ayah anchors: ع و د 30:11, 30:27; ع ت ب 30:57; ض ر ب 30:28, 30:58; ر ج ع 30:11, 30:41; ر س ل 30:9, 30:46-48, 30:51; س م ع 30:23, 30:52-53.
- Synthesis: Instrument, fret, refrain, alternation, and listener form an ordered production of attractive sound. The scene usefully pressures 30:52-53: auditory pleasure and patterned repetition can secure attention without producing the responsive movement of guidance, so hearing sound is not equivalent to admitting a summons.

### S19. Whole-Surah: Gilded Copper under Weight and Appraisal
- Reading type: mixed
- Scene or process: Copper is coated to resemble gold or silver, then weighed against known standards, appraised, and rejected if its appearance proves false.
- Active motifs: copper as base metal `quranic:root_000869:B004/m01`; gold or silver plating that simulates another substance `quranic:root_001458:B005/m01`; balanced standard weight or coin `quranic:root_001273:B015/m01`; known ounce weight `quranic:root_001677:B004/m01`; appraisal and pricing `quranic:root_001273:B010/m01`; rejection of counterfeit or error `quranic:root_000555:B003/m01`.
- Ayah anchors: ص ف ر 30:51; م و ه 30:24; ق و م 30:12, 30:14, 30:21, 30:23-25, 30:28, 30:30-31, 30:37, 30:43, 30:47, 30:55; و ق ي 30:31; ر د د 30:43.
- Synthesis: Surface brilliance is tested by an independent measure rather than trusted as substance. This materializes the surah's counterfeit-sign and false-impression problem while pressing its economic discourse: apparent increase or value remains unstable until weight and appraisal establish what the object actually is.

### S20. Whole-Surah: Suhur, Fast-Breaking, and Social Ease
- Reading type: latent/lexical
- Scene or process: A pre-dawn meal sustains a bounded fast, whose completion releases eating and opens a relaxed, companionable meal.
- Active motifs: breaking a fast `quranic:root_001165:B004/m01`; suhur preserving the faster's strength `quranic:root_001175:B006/m01`; relaxed speech and countenance `quranic:root_000116:B005/m01`; social familiarity and ease `quranic:root_000563:B007/m01`; cheerful open face `quranic:root_000120:B006/m01`.
- Ayah anchors: ف ط ر 30:30; ف ل ح 30:38; ب س ط 30:37, 30:48; ر س ل 30:9, 30:46-48, 30:51; ب ش ر 30:20, 30:46, 30:48.
- Synthesis: Abstention is neither indefinite deprivation nor disembodied devotion; it is sustained by provision, bounded by time, and completed in restored social openness. The rite supports the scheduled praise of 30:17-18 and the provision logic of the surah by making restraint depend on a measured round of nourishment and release.

### S21. Whole-Surah: Closed-Hand Riddle Challenge
- Reading type: mixed
- Scene or process: A player conceals something in the hand while others issue an enigmatic challenge intended to draw out the hidden object or answer.
- Active motifs: closed-hand reveal game `quranic:root_000400:B010/m01`; riddling call for a concealed answer `quranic:root_000478:B007/m01`; deliberate obscuration and ambiguity `quranic:root_001049:B004/m01`.
- Ayah anchors: خ ر ج 30:19, 30:25, 30:48; د ع و 30:25, 30:33, 30:52; ع م ي 30:53.
- Synthesis: Concealment, challenge, and extraction make obscurity a deliberately manufactured rule of play. The scene usefully pressures the signs and examples of the surah: they ask for reflection, but they are not arbitrary riddles whose answer has been sealed in another's fist; blindness arises when disclosed guidance is treated as if no intelligible route to an answer exists.

### S22. Whole-Surah: Laying and Concealing the Dead
- Reading type: mixed
- Scene or process: A corpse is placed on its right side and buried until the body disappears within the earth.
- Active motifs: burial until a body is hidden in earth `quranic:root_000913:B002/m01`; condition or manner of death `quranic:root_001454:B008/m01`; corpse and death `quranic:root_001568:B008/m01`; laying the deceased on the right side `quranic:root_001698:B007/m01`.
- Ayah anchors: ض ل ل 30:29, 30:53; م و ت 30:19, 30:24, 30:40, 30:50, 30:52; ن و م 30:23; ي م ن 30:28.
- Synthesis: Burial turns death into deliberate spatial concealment: the body is oriented, lowered, and made absent from sight. This materializes resurrection as an exact reversal in 30:19 and 30:25, where what was placed and hidden in earth is released from enclosure rather than merely remembered.

### S23. Whole-Surah: Unmeasured Grain Heap as Household Provision
- Reading type: mixed
- Scene or process: Wheat and seed grain are accumulated as staple food on a broad cloth, stored among household goods, and sold or carried as an unmeasured heap.
- Active motifs: wheat and cereal food `quranic:root_000104:B006/m01`; seed grain bearing further grain `quranic:root_000286:B001/m01`; food as bodily sustenance `quranic:root_000560:B002/m01`; grain heap on a broad cloth sold without measure or weight `quranic:root_000840:B011/m01`; household stores `quranic:root_000970:B014/m01`; provisions carried to meet need `quranic:root_001395:B003/m01`.
- Ayah anchors: ب ر ر 30:41; ح ب ب 30:45; ر ز ق 30:28, 30:37, 30:40; ص ب ر 30:60; ظ ه ر 30:7, 30:18, 30:41; م ت ع 30:34.
- Synthesis: Productive seed becomes both nourishment and transferable stock, but the heap can enter exchange before quantity is made explicit. The scene usefully pressures 30:37-40: provision is materially necessary and generative, yet its just circulation still depends on measure, recognized claims, and a distinction between useful yield and unexamined accumulation.

### S24. Whole-Surah: Sail, Rudder, Tender, and Chief Mariner
- Reading type: mixed
- Scene or process: A chief mariner coordinates a sailing vessel whose rig captures wind, whose stern gear restrains yaw, and whose small tender serves the larger ship.
- Active motifs: Roman-style ship's sail `quranic:root_000614:B009/m01`; rudder or stern gear that steadies a vessel `quranic:root_000726:B008/m01`; small tender accompanying ships `quranic:root_001212:B011/m01`; chief of the sailors `quranic:root_000532:B017/m01`.
- Ayah anchors: ر و م 30:2; س ك ن 30:21, 30:38; ق ر ب 30:38; ر ب ب 30:8, 30:33.
- Synthesis: Wind becomes useful travel only through a configured control system and differentiated crew roles. This supports the ships seeking bounty in 30:46: atmospheric force supplies motion, but sail, steering gear, tender, and mariner convert that force into a stable commercial course.

### S25. Whole-Surah: Paired Milking Pails and Set Curd
- Reading type: latent/lexical
- Scene or process: An abundant udder yields a continuing flow into two pails during one milking, after which the milk is kept until it thickens into set curd.
- Active motifs: continuing and abundant milk flow `quranic:root_000563:B006/m01`; combining two milking pails in one session `quranic:root_000802:B005/m01`; full udder and plentiful yield `quranic:root_000810:B003/m01`; curd too thick to make sound when poured `quranic:root_000884:B020/m01`.
- Ayah anchors: ر س ل 30:9, 30:46-48, 30:51; ش ف ع 30:13; ش ك ر 30:46; ص م م 30:52.
- Synthesis: Abundance passes from living body to measured vessels and then into a storable food with a changed consistency. The scene materializes the surah's nurture and provision readings: fertility becomes sustaining mercy through skilled collection and transformation, not through quantity remaining inaccessible in the source.

### S26. Whole-Surah: Blood Claim, Retaliation, or Indemnity
- Reading type: mixed
- Scene or process: A killing generates a blood claim before a judge, who prevents the loss from going unanswered by authorizing retaliation or accepting a compensatory blood-wit.
- Active motifs: blood left without vengeance or compensation `quranic:root_000127:B006/m01`; retaliation preserving communal life `quranic:root_000383:B013/m01`; ruler-authorized requital `quranic:root_000840:B012/m01`; blood-wit and collective payment `quranic:root_001036:B004/m01`; indemnity taken in place of retaliation `quranic:root_001119:B002/m01`; judicial decision between parties `quranic:root_000348:B002/m01`.
- Ayah anchors: ب ط ل 30:58; ح ي ي 30:7, 30:19, 30:24, 30:40, 30:50; ص ب ر 30:60; ع ق ل 30:24, 30:28; غ ي ر 30:29, 30:55; ح ك م 30:27.
- Synthesis: Justice keeps embodied loss from becoming an erased trace and permits substitution only through an acknowledged claim and authoritative decision. This usefully pressures the surah's injury and adjudication readings: consequence must reach a forum, while compensation is a structured alternative to requital rather than a denial that harm occurred.

### S27. Whole-Surah: Bark-Tanning and Sandal Strap
- Reading type: latent/lexical
- Scene or process: A hide is scraped, treated in measured applications with tanning bark, cut into leather strips, and fitted as a repaired sandal strap.
- Active motifs: tanning foliage from the alaa tree `quranic:root_000076:B005/m01`; scraping the outer surface from a hide `quranic:root_000120:B004/m01`; acacia bark used to tan leather `quranic:root_000737:B008/m01`; one or two measured tanning applications `quranic:root_001533:B007/m01`; cut leather strip `quranic:root_000769:B003/m01`; sandal-strap repair `quranic:root_000791:B004/m01`.
- Ayah anchors: ء ل ي 30:11, 30:21, 30:31, 30:33, 30:47, 30:50, 30:56; ب ش ر 30:20, 30:46, 30:48; س ل م 30:53; ن ف س 30:8-9, 30:21, 30:28, 30:44; س ي ر 30:9, 30:42; ش ر ك 30:13, 30:28, 30:31, 30:33, 30:35, 30:40, 30:42.
- Synthesis: Durable footing emerges from a disclosed sequence of surface removal, measured treatment, cutting, and joining. The craft materializes the surah's concern with formation and route: legitimate alteration makes matter fit for sustained use through disciplined process, unlike a deceptive coating that only borrows another material's appearance.

### S28. Whole-Surah: Horse Race, Winner, and Second
- Reading type: mixed
- Scene or process: Horses are driven into a run, where a leading animal wins, a second follows close behind, and uneven conformation affects the ordered gait.
- Active motifs: driving a horse at a run `quranic:root_000333:B004/m01`; prevailing or winning horse `quranic:root_000104:B008/m01`; second horse following the leader in a race `quranic:root_000879:B006/m01`; separated or uneven hoof and hip conformation `quranic:root_001148:B007/m01`.
- Ayah anchors: ح ض ر 30:16; ب ر ر 30:41; ص ل و 30:31; ف ر ق 30:14, 30:32-33.
- Synthesis: Victory is rendered as a ranked moving sequence whose positions are legible through following distance and bodily coordination. The race reframes 30:2-4 and supports the surah's disciplined-force scenes: dominance is an outcome within measured motion, while defective alignment can alter how a contender holds its place.


