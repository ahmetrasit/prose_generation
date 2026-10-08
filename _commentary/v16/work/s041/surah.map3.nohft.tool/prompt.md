Surah: 41. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S41 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s041/surah.r2/text.md =====
# Surah 41

- 41:1 حمٓ
- 41:2 تَنزِيلٌۭ مِّنَ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 41:3 كِتَٰبٌۭ فُصِّلَتْ ءَايَٰتُهُۥ قُرْءَانًا عَرَبِيًّۭا لِّقَوْمٍۢ يَعْلَمُونَ
- 41:4 بَشِيرًۭا وَنَذِيرًۭا فَأَعْرَضَ أَكْثَرُهُمْ فَهُمْ لَا يَسْمَعُونَ
- 41:5 وَقَالُوا۟ قُلُوبُنَا فِىٓ أَكِنَّةٍۢ مِّمَّا تَدْعُونَآ إِلَيْهِ وَفِىٓ ءَاذَانِنَا وَقْرٌۭ وَمِنۢ بَيْنِنَا وَبَيْنِكَ حِجَابٌۭ فَٱعْمَلْ إِنَّنَا عَٰمِلُونَ
- 41:6 قُلْ إِنَّمَآ أَنَا۠ بَشَرٌۭ مِّثْلُكُمْ يُوحَىٰٓ إِلَىَّ أَنَّمَآ إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَٱسْتَقِيمُوٓا۟ إِلَيْهِ وَٱسْتَغْفِرُوهُ ۗ وَوَيْلٌۭ لِّلْمُشْرِكِينَ
- 41:7 ٱلَّذِينَ لَا يُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- 41:8 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ
- 41:9 ۞ قُلْ أَئِنَّكُمْ لَتَكْفُرُونَ بِٱلَّذِى خَلَقَ ٱلْأَرْضَ فِى يَوْمَيْنِ وَتَجْعَلُونَ لَهُۥٓ أَندَادًۭا ۚ ذَٰلِكَ رَبُّ ٱلْعَٰلَمِينَ
- 41:10 وَجَعَلَ فِيهَا رَوَٰسِىَ مِن فَوْقِهَا وَبَٰرَكَ فِيهَا وَقَدَّرَ فِيهَآ أَقْوَٰتَهَا فِىٓ أَرْبَعَةِ أَيَّامٍۢ سَوَآءًۭ لِّلسَّآئِلِينَ
- 41:11 ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ وَهِىَ دُخَانٌۭ فَقَالَ لَهَا وَلِلْأَرْضِ ٱئْتِيَا طَوْعًا أَوْ كَرْهًۭا قَالَتَآ أَتَيْنَا طَآئِعِينَ
- 41:12 فَقَضَىٰهُنَّ سَبْعَ سَمَٰوَاتٍۢ فِى يَوْمَيْنِ وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا ۚ وَزَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَحِفْظًۭا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ
- 41:13 فَإِنْ أَعْرَضُوا۟ فَقُلْ أَنذَرْتُكُمْ صَٰعِقَةًۭ مِّثْلَ صَٰعِقَةِ عَادٍۢ وَثَمُودَ
- 41:14 إِذْ جَآءَتْهُمُ ٱلرُّسُلُ مِنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ أَلَّا تَعْبُدُوٓا۟ إِلَّا ٱللَّهَ ۖ قَالُوا۟ لَوْ شَآءَ رَبُّنَا لَأَنزَلَ مَلَٰٓئِكَةًۭ فَإِنَّا بِمَآ أُرْسِلْتُم بِهِۦ كَٰفِرُونَ
- 41:15 فَأَمَّا عَادٌۭ فَٱسْتَكْبَرُوا۟ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَقَالُوا۟ مَنْ أَشَدُّ مِنَّا قُوَّةً ۖ أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ ٱلَّذِى خَلَقَهُمْ هُوَ أَشَدُّ مِنْهُمْ قُوَّةًۭ ۖ وَكَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- 41:16 فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا فِىٓ أَيَّامٍۢ نَّحِسَاتٍۢ لِّنُذِيقَهُمْ عَذَابَ ٱلْخِزْىِ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَخْزَىٰ ۖ وَهُمْ لَا يُنصَرُونَ
- 41:17 وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ فَأَخَذَتْهُمْ صَٰعِقَةُ ٱلْعَذَابِ ٱلْهُونِ بِمَا كَانُوا۟ يَكْسِبُونَ
- 41:18 وَنَجَّيْنَا ٱلَّذِينَ ءَامَنُوا۟ وَكَانُوا۟ يَتَّقُونَ
- 41:19 وَيَوْمَ يُحْشَرُ أَعْدَآءُ ٱللَّهِ إِلَى ٱلنَّارِ فَهُمْ يُوزَعُونَ
- 41:20 حَتَّىٰٓ إِذَا مَا جَآءُوهَا شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- 41:21 وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا ۖ قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍۢ وَهُوَ خَلَقَكُمْ أَوَّلَ مَرَّةٍۢ وَإِلَيْهِ تُرْجَعُونَ
- 41:22 وَمَا كُنتُمْ تَسْتَتِرُونَ أَن يَشْهَدَ عَلَيْكُمْ سَمْعُكُمْ وَلَآ أَبْصَٰرُكُمْ وَلَا جُلُودُكُمْ وَلَٰكِن ظَنَنتُمْ أَنَّ ٱللَّهَ لَا يَعْلَمُ كَثِيرًۭا مِّمَّا تَعْمَلُونَ
- 41:23 وَذَٰلِكُمْ ظَنُّكُمُ ٱلَّذِى ظَنَنتُم بِرَبِّكُمْ أَرْدَىٰكُمْ فَأَصْبَحْتُم مِّنَ ٱلْخَٰسِرِينَ
- 41:24 فَإِن يَصْبِرُوا۟ فَٱلنَّارُ مَثْوًۭى لَّهُمْ ۖ وَإِن يَسْتَعْتِبُوا۟ فَمَا هُم مِّنَ ٱلْمُعْتَبِينَ
- 41:25 ۞ وَقَيَّضْنَا لَهُمْ قُرَنَآءَ فَزَيَّنُوا۟ لَهُم مَّا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَحَقَّ عَلَيْهِمُ ٱلْقَوْلُ فِىٓ أُمَمٍۢ قَدْ خَلَتْ مِن قَبْلِهِم مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ إِنَّهُمْ كَانُوا۟ خَٰسِرِينَ
- 41:26 وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَسْمَعُوا۟ لِهَٰذَا ٱلْقُرْءَانِ وَٱلْغَوْا۟ فِيهِ لَعَلَّكُمْ تَغْلِبُونَ
- 41:27 فَلَنُذِيقَنَّ ٱلَّذِينَ كَفَرُوا۟ عَذَابًۭا شَدِيدًۭا وَلَنَجْزِيَنَّهُمْ أَسْوَأَ ٱلَّذِى كَانُوا۟ يَعْمَلُونَ
- 41:28 ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- 41:29 وَقَالَ ٱلَّذِينَ كَفَرُوا۟ رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ نَجْعَلْهُمَا تَحْتَ أَقْدَامِنَا لِيَكُونَا مِنَ ٱلْأَسْفَلِينَ
- 41:30 إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟ تَتَنَزَّلُ عَلَيْهِمُ ٱلْمَلَٰٓئِكَةُ أَلَّا تَخَافُوا۟ وَلَا تَحْزَنُوا۟ وَأَبْشِرُوا۟ بِٱلْجَنَّةِ ٱلَّتِى كُنتُمْ تُوعَدُونَ
- 41:31 نَحْنُ أَوْلِيَآؤُكُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَفِى ٱلْءَاخِرَةِ ۖ وَلَكُمْ فِيهَا مَا تَشْتَهِىٓ أَنفُسُكُمْ وَلَكُمْ فِيهَا مَا تَدَّعُونَ
- 41:32 نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- 41:33 وَمَنْ أَحْسَنُ قَوْلًۭا مِّمَّن دَعَآ إِلَى ٱللَّهِ وَعَمِلَ صَٰلِحًۭا وَقَالَ إِنَّنِى مِنَ ٱلْمُسْلِمِينَ
- 41:34 وَلَا تَسْتَوِى ٱلْحَسَنَةُ وَلَا ٱلسَّيِّئَةُ ۚ ٱدْفَعْ بِٱلَّتِى هِىَ أَحْسَنُ فَإِذَا ٱلَّذِى بَيْنَكَ وَبَيْنَهُۥ عَدَٰوَةٌۭ كَأَنَّهُۥ وَلِىٌّ حَمِيمٌۭ
- 41:35 وَمَا يُلَقَّىٰهَآ إِلَّا ٱلَّذِينَ صَبَرُوا۟ وَمَا يُلَقَّىٰهَآ إِلَّا ذُو حَظٍّ عَظِيمٍۢ
- 41:36 وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ ۖ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- 41:37 وَمِنْ ءَايَٰتِهِ ٱلَّيْلُ وَٱلنَّهَارُ وَٱلشَّمْسُ وَٱلْقَمَرُ ۚ لَا تَسْجُدُوا۟ لِلشَّمْسِ وَلَا لِلْقَمَرِ وَٱسْجُدُوا۟ لِلَّهِ ٱلَّذِى خَلَقَهُنَّ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- 41:38 فَإِنِ ٱسْتَكْبَرُوا۟ فَٱلَّذِينَ عِندَ رَبِّكَ يُسَبِّحُونَ لَهُۥ بِٱلَّيْلِ وَٱلنَّهَارِ وَهُمْ لَا يَسْـَٔمُونَ ۩
- 41:39 وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- 41:40 إِنَّ ٱلَّذِينَ يُلْحِدُونَ فِىٓ ءَايَٰتِنَا لَا يَخْفَوْنَ عَلَيْنَآ ۗ أَفَمَن يُلْقَىٰ فِى ٱلنَّارِ خَيْرٌ أَم مَّن يَأْتِىٓ ءَامِنًۭا يَوْمَ ٱلْقِيَٰمَةِ ۚ ٱعْمَلُوا۟ مَا شِئْتُمْ ۖ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌ
- 41:41 إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- 41:42 لَّا يَأْتِيهِ ٱلْبَٰطِلُ مِنۢ بَيْنِ يَدَيْهِ وَلَا مِنْ خَلْفِهِۦ ۖ تَنزِيلٌۭ مِّنْ حَكِيمٍ حَمِيدٍۢ
- 41:43 مَّا يُقَالُ لَكَ إِلَّا مَا قَدْ قِيلَ لِلرُّسُلِ مِن قَبْلِكَ ۚ إِنَّ رَبَّكَ لَذُو مَغْفِرَةٍۢ وَذُو عِقَابٍ أَلِيمٍۢ
- 41:44 وَلَوْ جَعَلْنَٰهُ قُرْءَانًا أَعْجَمِيًّۭا لَّقَالُوا۟ لَوْلَا فُصِّلَتْ ءَايَٰتُهُۥٓ ۖ ءَا۬عْجَمِىٌّۭ وَعَرَبِىٌّۭ ۗ قُلْ هُوَ لِلَّذِينَ ءَامَنُوا۟ هُدًۭى وَشِفَآءٌۭ ۖ وَٱلَّذِينَ لَا يُؤْمِنُونَ فِىٓ ءَاذَانِهِمْ وَقْرٌۭ وَهُوَ عَلَيْهِمْ عَمًى ۚ أُو۟لَٰٓئِكَ يُنَادَوْنَ مِن مَّكَانٍۭ بَعِيدٍۢ
- 41:45 وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَٱخْتُلِفَ فِيهِ ۗ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَقُضِىَ بَيْنَهُمْ ۚ وَإِنَّهُمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- 41:46 مَّنْ عَمِلَ صَٰلِحًۭا فَلِنَفْسِهِۦ ۖ وَمَنْ أَسَآءَ فَعَلَيْهَا ۗ وَمَا رَبُّكَ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
- 41:47 ۞ إِلَيْهِ يُرَدُّ عِلْمُ ٱلسَّاعَةِ ۚ وَمَا تَخْرُجُ مِن ثَمَرَٰتٍۢ مِّنْ أَكْمَامِهَا وَمَا تَحْمِلُ مِنْ أُنثَىٰ وَلَا تَضَعُ إِلَّا بِعِلْمِهِۦ ۚ وَيَوْمَ يُنَادِيهِمْ أَيْنَ شُرَكَآءِى قَالُوٓا۟ ءَاذَنَّٰكَ مَا مِنَّا مِن شَهِيدٍۢ
- 41:48 وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَدْعُونَ مِن قَبْلُ ۖ وَظَنُّوا۟ مَا لَهُم مِّن مَّحِيصٍۢ
- 41:49 لَّا يَسْـَٔمُ ٱلْإِنسَٰنُ مِن دُعَآءِ ٱلْخَيْرِ وَإِن مَّسَّهُ ٱلشَّرُّ فَيَـُٔوسٌۭ قَنُوطٌۭ
- 41:50 وَلَئِنْ أَذَقْنَٰهُ رَحْمَةًۭ مِّنَّا مِنۢ بَعْدِ ضَرَّآءَ مَسَّتْهُ لَيَقُولَنَّ هَٰذَا لِى وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّجِعْتُ إِلَىٰ رَبِّىٓ إِنَّ لِى عِندَهُۥ لَلْحُسْنَىٰ ۚ فَلَنُنَبِّئَنَّ ٱلَّذِينَ كَفَرُوا۟ بِمَا عَمِلُوا۟ وَلَنُذِيقَنَّهُم مِّنْ عَذَابٍ غَلِيظٍۢ
- 41:51 وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ وَإِذَا مَسَّهُ ٱلشَّرُّ فَذُو دُعَآءٍ عَرِيضٍۢ
- 41:52 قُلْ أَرَءَيْتُمْ إِن كَانَ مِنْ عِندِ ٱللَّهِ ثُمَّ كَفَرْتُم بِهِۦ مَنْ أَضَلُّ مِمَّنْ هُوَ فِى شِقَاقٍۭ بَعِيدٍۢ
- 41:53 سَنُرِيهِمْ ءَايَٰتِنَا فِى ٱلْءَافَاقِ وَفِىٓ أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ ٱلْحَقُّ ۗ أَوَلَمْ يَكْفِ بِرَبِّكَ أَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
- 41:54 أَلَآ إِنَّهُمْ فِى مِرْيَةٍۢ مِّن لِّقَآءِ رَبِّهِمْ ۗ أَلَآ إِنَّهُۥ بِكُلِّ شَىْءٍۢ مُّحِيطٌۢ


===== _commentary/v16/work/s041/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ز ل (root_001492): 41:2 تَنزِيلٌ, 41:14 لَأَنزَلَ, 41:30 تَتَنَزَّلُ, 41:32 نُزُلًا, 41:39 أَنزَلْنَا, 41:42 تَنزِيلٌ

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

## ر ح م (root_000552): 41:2 ٱلرَّحْمَٰنِ, 41:2 ٱلرَّحِيمِ, 41:32 رَّحِيمٍ, 41:50 رَحْمَةً

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ك ت ب (root_001283): 41:3 كِتَٰبٌ, 41:41 لَكِتَٰبٌ, 41:45 ٱلْكِتَٰبَ

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

## ف ص ل (root_001159): 41:3 فُصِّلَتْ, 41:44 فُصِّلَتْ

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

## ء ي ي (root_000074): 41:3 ءَايَٰتُهُۥ, 41:15 بِـَٔايَٰتِنَا, 41:28 بِـَٔايَٰتِنَا, 41:37 ءَايَٰتِهِ, 41:39 ءَايَٰتِهِۦٓ, 41:40 ءَايَٰتِنَا, 41:44 ءَايَٰتُهُۥٓ, 41:53 ءَايَٰتِنَا

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

## ق ر ء (root_001210): 41:3 قُرْءَانًا, 41:26 ٱلْقُرْءَانِ, 41:44 قُرْءَانًا

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

## ق ر ء (root_001211): 41:3 قُرْءَانًا, 41:26 ٱلْقُرْءَانِ, 41:44 قُرْءَانًا

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

## ع ر ب (root_000996): 41:3 عَرَبِيًّا, 41:44 وَعَرَبِىٌّ

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

## ق و م (root_001273): 41:3 لِّقَوْمٍ, 41:6 فَٱسْتَقِيمُوٓا۟, 41:30 ٱسْتَقَٰمُوا۟, 41:40 ٱلْقِيَٰمَةِ, 41:50 قَآئِمَةً

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

## ع ل م (root_001040): 41:3 يَعْلَمُونَ, 41:9 ٱلْعَٰلَمِينَ, 41:12 ٱلْعَلِيمِ, 41:22 يَعْلَمُ, 41:36 ٱلْعَلِيمُ, 41:47 عِلْمُ, 41:47 بِعِلْمِهِۦ

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

## ب ش ر (root_000120): 41:4 بَشِيرًا, 41:6 بَشَرٌ, 41:30 وَأَبْشِرُوا۟

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

## ن ذ ر (root_001488): 41:4 وَنَذِيرًا, 41:13 أَنذَرْتُكُمْ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ع ر ض (root_001001): 41:4 فَأَعْرَضَ, 41:13 أَعْرَضُوا۟, 41:51 أَعْرَضَ, 41:51 عَرِيضٍ

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

## ك ث ر (root_001286): 41:4 أَكْثَرُهُمْ, 41:22 كَثِيرًا

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

## س م ع (root_000741): 41:4 يَسْمَعُونَ, 41:20 سَمْعُهُمْ, 41:22 سَمْعُكُمْ, 41:26 تَسْمَعُوا۟, 41:36 ٱلسَّمِيعُ

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

## ق و ل (root_001272): 41:5 وَقَالُوا۟, 41:6 قُلْ, 41:9 قُلْ, 41:11 فَقَالَ, 41:11 قَالَتَآ, 41:13 فَقُلْ, 41:14 قَالُوا۟, 41:15 وَقَالُوا۟, 41:21 وَقَالُوا۟, 41:21 قَالُوٓا۟, 41:25 ٱلْقَوْلُ, 41:26 وَقَالَ, 41:29 وَقَالَ, 41:30 قَالُوا۟, 41:33 قَوْلًا, 41:33 وَقَالَ, 41:43 يُقَالُ, 41:43 قِيلَ, 41:44 لَّقَالُوا۟, 41:44 قُلْ, 41:47 قَالُوٓا۟, 41:50 لَيَقُولَنَّ, 41:52 قُلْ

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

## ECHO ق ل ل (root_001251): for 41:5 وَقَالُوا۟, 41:6 قُلْ, 41:9 قُلْ, 41:11 فَقَالَ, 41:11 قَالَتَآ, 41:13 فَقُلْ, 41:14 قَالُوا۟, 41:15 وَقَالُوا۟, 41:21 وَقَالُوا۟, 41:21 قَالُوٓا۟, 41:25 ٱلْقَوْلُ, 41:26 وَقَالَ, 41:29 وَقَالَ, 41:30 قَالُوا۟, 41:33 قَوْلًا, 41:33 وَقَالَ, 41:43 يُقَالُ, 41:43 قِيلَ, 41:44 لَّقَالُوا۟, 41:44 قُلْ, 41:47 قَالُوٓا۟, 41:50 لَيَقُولَنَّ, 41:52 قُلْ: withheld observed target; not identity

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

## ق ل ب (root_001248): 41:5 قُلُوبُنَا

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

## ك ن ن (root_001324): 41:5 أَكِنَّةٍ

- **B001** koruyucu bir örtü içinde saklama — koruyucu örtü veya korunak · koruyucu örtü ya da kap · bir şeyi örtüp korunak içine koymak · gizlemek; bazı kullanımlarda içinde saklamak · örtüler, koruyucu kaplamalar · örtülü, saklı ve korunmuş
  أصل واحد يدل على ستر أو صون (maqayis)؛ الكن كل شيء وقى شيئا فهو كنه وكنانه (ayn;tahdhib)؛ كننت الشيء إذا خبأته وسترته (jamhara)؛ الكن السترة؛ والأكنة الأغطية (sihah)؛ الكن ما يحفظ فيه الشيء (mufradat)
- **B002** içinde saklayıp açığa vurmama — gizlemek; özellikle içinde saklamak · bir şeyi içinde saklamak · içte saklama, gizli tutma · içte beslenen kin
  أكننت الشيء أخفيته (maqayis)؛ الإكنان ما أضمرت في ضميرك (ayn)؛ أكننته في صدري (jamhara)؛ أكننته في نفسي أسررته؛ المستكنة الحقد (sihah)؛ أو أكننتم في أنفسكم؛ أكننت بما يستر في النفس (tahdhib;mufradat)
- **B003** korunağa girip gizlenme — korunağa girip gizlenmek · utanıp yüzünü örtmek · mağara benzeri doğal sığınaklar · korunağında kalmak · birinin koruması altında olmak
  استكن الرجل واكتن صار في كن؛ اكتنت المرأة سترت وجهها حياء (ayn)؛ اكتن واستكن استتر (sihah)؛ تكنى لزم الكن؛ الأكنان الغيران ونحوها يسكن فيها (tahdhib)؛ وجعل لكم من الجبال أكنانا (mufradat)
- **B004** küçük, kapalı okluk — küçük okluk; okların konduğu kap
  الكنانة المعروفة وهي القياس (maqayis)؛ الكنانة كالجعبة غير أنها صغيرة تتخذ للنبل (ayn;tahdhib)؛ الكنانة التي تجعل فيها السهام (sihah)؛ الكنانة جعبة غير مشقوقة (mufradat)
- **B005** örtücü ev çıkması veya iç niş — kapı üstü gölgelik veya duvar saçağı; iç niş ya da raf
  الكنة كالجناح يخرجه الرجل من حائطه وهو كالسترة (maqayis)؛ الكنة فصلة يخرجها الرجل من حائطه كالجناح (ayn)؛ الكنة مخدع أو رف في البيت (jamhara)؛ الكنة بالضم سقيفة تشرع فوق باب الدار (sihah)؛ الكنة والسدة كالصفة؛ والظلة تكون بباب الدار (tahdhib)
- **B006** oğlun eşi; kimi kullanımda erkek kardeşin eşi — gelin; kimi kaynaklarda yenge
  فأما الكنة فشاذة عن هذا الأصل؛ امراة الابن (maqayis)؛ الكنة امرأة الابن أو الأخ (ayn;tahdhib)؛ كنة الرجل امرأة أخيه أو ابنه (jamhara)؛ الكنة بالفتح امرأة الابن (sihah)؛ سميت المرأة المتزوجة كنة لكونها في كن من حفظ زوجها (mufradat)
- **B007** biçime bağlı adlandırmalar — ocak; ateş yakılan veya ısınılan yer · kış ortasındaki iki ayın birlikte adı · ağır adam
  الكانون لأنه يستر ما تحته؛ الرجل الثقيل كانونا (maqayis)؛ الكانون المصطلى؛ الكانونان شهران في قلب الشتاء (ayn)؛ الكانون والكانونة الموقد؛ كانون الأول وكانون الآخر شهران (sihah)؛ الكانون المصطلى؛ الكوانين الثقلاء من الرجال (tahdhib)

## ك و ن (root_001332): 41:15 وَكَانُوا۟, 41:17 كَانُوا۟, 41:18 وَكَانُوا۟, 41:20 كَانُوا۟, 41:22 كُنتُمْ, 41:25 كَانُوا۟, 41:27 كَانُوا۟, 41:28 كَانُوا۟, 41:29 لِيَكُونَا, 41:30 كُنتُمْ, 41:37 كُنتُمْ, 41:44 مَّكَانٍۭ, 41:48 كَانُوا۟, 41:52 كَانَ (also echo for 41:5 أَكِنَّةٍ)

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

## د ع و (root_000478): 41:5 تَدْعُونَآ, 41:31 تَدَّعُونَ, 41:33 دَعَآ, 41:48 يَدْعُونَ, 41:49 دُعَآءِ, 41:51 دُعَآءٍ

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

## ECHO د ع ع (root_000477): for 41:5 تَدْعُونَآ, 41:31 تَدَّعُونَ, 41:33 دَعَآ, 41:48 يَدْعُونَ, 41:49 دُعَآءِ, 41:51 دُعَآءٍ: withheld observed target; not identity

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

## ء ذ ن (root_000022): 41:5 ءَاذَانِنَا, 41:44 ءَاذَانِهِمْ, 41:47 ءَاذَنَّٰكَ

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

## و ق ر (root_001674): 41:5 وَقْرٌ, 41:44 وَقْرٌ

- **B001** işitme ağırlığı — kulakta işitme ağırlığı · kulağı ağırlaştı, işitmesi güçleşti · işitmesi ağırlaşmış kulak
  الوَقْر ثقل في الأذن (maqayis;ayn;sihah;tahdhib;mufradat)؛ وقرت أذنه فهي موقورة (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** ağır yük — sırtta, başta veya hayvanda taşınan ağır yük · ona ağır yük taşıttı · çok ürünle yüklü ağaç · ağır yük taşıyan kadın · borç onu ağır yük altında bıraktı · yiyecekten taşıyabileceği kadarını aldı · borç yükü altında ezilmiş yoksul; ayrıca uyaklı pekiştirme sözü
  الوِقْر الحمل (maqayis;ayn;sihah;tahdhib;mufradat)؛ نخلة موقرة وموقر (maqayis;ayn;sihah;tahdhib;mufradat)؛ امرأة موقرة إذا حملت حملا ثقيلا (sihah;tahdhib)؛ أوقره الدين (ayn;sihah;tahdhib)
- **B003** sakin ve ölçülü ağırbaşlılık — sakinlik, ölçülülük ve ağırbaşlılık · sakin ve ağırbaşlı kimse · ölçülü ve ağırbaşlı kimse · birini yüceltti ve ona saygı gösterdi · saygı gösterme ve yüceltme · ağırbaşlılık veya saygı gösterme için kullanılan değişken biçim · ağırbaşlılık sahibi
  الوقار الحلم والرزانة (maqayis;ayn;sihah;tahdhib)؛ السكينة والوداعة (ayn;tahdhib)؛ التوقير التبجيل (ayn)؛ وقرت الرجل إذا عظمته (tahdhib)؛ لا ترجون لله وقارا أي عظمة (sihah;tahdhib)؛ التيقور لغة في التوقير (ayn;sihah;tahdhib)
- **B004** hareketsiz kalma veya oturma — 
  ليس من الوقار إنما هو من الجلوس يقال منه وقرت (maqayis)؛ وقر يقر وقارا إذا سكن والأمر منه قر (tahdhib)؛ وقرت أقر وقرا أي جلست (mufradat)
- **B005** sert yüzeyde çentik veya oyuk — gözde, toynakta, taşta veya kemikte çentik ve oyuk · kemiği çatlattı veya ezdi · kayada su tutabilen oyuk · hayvanın toynağı taşa çarpıp incindi
  الوقيرة نقر في الصخر (maqayis)؛ الوقرة في العظم (maqayis)؛ وقرت العظم صدعته (sihah)؛ الوقرة شبه وكتة لها حفرة في العين والحافر والحجر (ayn;tahdhib)؛ الوقر في العظم شيء من الكسر وهو الهزم (tahdhib)
- **B006** koyun sürüsü — koyun veya küçükbaş sürüsü · insanlardan veya başka varlıklardan oluşan topluluk · koyun topluluğunun adı
  الوقير القطيع من الضأن (maqayis;ayn;mufradat)؛ الوقير الغنم (sihah;tahdhib)؛ الوقير صغار الشاء (ayn)؛ الوقير الجماعة من الناس وغيرهم (tahdhib)
- **B007** deneyimle pişip dayanıklı olma [kalıp] — olayların veya yolculukların pişirdiği deneyimli kişi · yolculuklar beni sertleştirdi ve koşullarına alıştırdı
  رجل موقر مجرب (maqayis;sihah)؛ رجل موقر إذا وقحته الأمور واستمر عليها (tahdhib)؛ وقرتني الأسفار أي صلبتني ومرنتني عليها (tahdhib)

## ب ي ن (root_000170): 41:5 بَيْنِنَا, 41:5 وَبَيْنِكَ, 41:14 بَيْنِ, 41:25 بَيْنَ, 41:34 بَيْنَكَ, 41:34 وَبَيْنَهُۥ, 41:42 بَيْنِ, 41:45 بَيْنَهُمْ, 41:53 يَتَبَيَّنَ

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

## ح ج ب (root_000294): 41:5 حِجَابٌ

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

## ع م ل (root_001046): 41:5 فَٱعْمَلْ, 41:5 عَٰمِلُونَ, 41:8 وَعَمِلُوا۟, 41:20 يَعْمَلُونَ, 41:22 تَعْمَلُونَ, 41:27 يَعْمَلُونَ, 41:33 وَعَمِلَ, 41:40 ٱعْمَلُوا۟, 41:40 تَعْمَلُونَ, 41:46 عَمِلَ, 41:50 عَمِلُوا۟

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

## م ث ل (root_001397): 41:6 مِّثْلُكُمْ, 41:13 مِّثْلَ

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

## و ح ي (root_001633): 41:6 يُوحَىٰٓ, 41:12 وَأَوْحَىٰ

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

## ء ل ه (root_000047): 41:6 إِلَٰهُكُمْ, 41:6 إِلَٰهٌ, 41:14 ٱللَّهَ, 41:15 ٱللَّهَ, 41:19 ٱللَّهِ, 41:21 ٱللَّهُ, 41:22 ٱللَّهَ, 41:28 ٱللَّهِ, 41:30 ٱللَّهُ, 41:33 ٱللَّهِ, 41:36 بِٱللَّهِ, 41:37 لِلَّهِ, 41:52 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 41:6 إِلَٰهُكُمْ, 41:6 إِلَٰهٌ, 41:14 ٱللَّهَ, 41:15 ٱللَّهَ, 41:19 ٱللَّهِ, 41:21 ٱللَّهُ, 41:22 ٱللَّهَ, 41:28 ٱللَّهِ, 41:30 ٱللَّهُ, 41:33 ٱللَّهِ, 41:36 بِٱللَّهِ, 41:37 لِلَّهِ, 41:52 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## و ح د (root_001631): 41:6 وَٰحِدٌ

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

## غ ف ر (root_001096): 41:6 وَٱسْتَغْفِرُوهُ, 41:32 غَفُورٍ, 41:43 مَغْفِرَةٍ

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

## ش ر ك (root_000791): 41:6 لِّلْمُشْرِكِينَ, 41:47 شُرَكَآءِى

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

## ء ت ي (root_000009): 41:7 يُؤْتُونَ, 41:11 ٱئْتِيَا, 41:11 أَتَيْنَا, 41:40 يَأْتِىٓ, 41:42 يَأْتِيهِ, 41:45 ءَاتَيْنَا

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

## ز ك و (root_000637): 41:7 ٱلزَّكَوٰةَ

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

## ء خ ر (root_000019): 41:7 بِٱلْءَاخِرَةِ, 41:16 ٱلْءَاخِرَةِ, 41:31 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ك ف ر (root_001307): 41:7 كَٰفِرُونَ, 41:9 لَتَكْفُرُونَ, 41:14 كَٰفِرُونَ, 41:26 كَفَرُوا۟, 41:27 كَفَرُوا۟, 41:29 كَفَرُوا۟, 41:41 كَفَرُوا۟, 41:50 كَفَرُوا۟, 41:52 كَفَرْتُم

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

## ء م ن (root_000054): 41:8 ءَامَنُوا۟, 41:18 ءَامَنُوا۟, 41:40 ءَامِنًا, 41:44 ءَامَنُوا۟, 41:44 يُؤْمِنُونَ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ص ل ح (root_000876): 41:8 ٱلصَّٰلِحَٰتِ, 41:33 صَٰلِحًا, 41:46 صَٰلِحًا

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

## ء ج ر (root_000015): 41:8 أَجْرٌ

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## غ ي ر (root_001119): 41:8 غَيْرُ, 41:15 بِغَيْرِ

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

## م ن ن (root_001449): 41:8 مَمْنُونٍ

- **B001** kesip eksilterek sürekliliği sona erdirme — ipi kesmek · kesme veya eksiltme · kesintisiz ve eksiltilmemiş · ömürleri kesip sayıyı azaltan ölüm veya zaman · yürümeyi kestiren aşırı yorgunluk
  المن: القطع؛ مننت الحبل: قطعته؛ المنون: المنية لأنها تنقص العدد وتقطع المدد؛ المن: الإعياء... المعيي ينقطع عن السير (maqayis)؛ المن: القطع ويقال النقص؛ لهم أجر غير ممنون؛ المنون: الدهر؛ المنون: المنية... تقطع المدد وتنقص العدد (sihah)؛ غير مقطوع ولا منقوص؛ المنون للمنية لأنها تنقص العدد وتقطع المدد (mufradat)
- **B002** ayakta tutan güç ve bu gücün zayıflığı — insanı ayakta tutan güç · dayanma gücü zayıf · güçsüz veya dayanıksız
  المنة، وهي القوة التي بها قوام الإنسان (maqayis)؛ المنة بالضم: القوة؛ هو ضعيف المنة؛ رجل منين؛ المنين: الحبل الضعيف؛ المنين: الغبار الضعيف (sihah)
- **B003** iyilik yapma ve bunu yük ya da başa kakma haline getirme — birine iyilik etmek veya yaptığı iyilikle onu yük altında bırakmak · karşıdakini yük altında bırakan iyilik · yaptığı iyiliği sözle başa kakma · bol bol bağışlayıp iyilik eden · yaptığı iyiliği çokça başa kakan · ver veya harca · verdiğini başa kakma ya da daha çoğunu bekleyerek verme
  من يمن منا، إذا صنع صنعا جميلا (maqayis)؛ من عليه منا: أنعم؛ المنان؛ من عليه منة، أي امتن عليه؛ المنة تهدم الصنيعة؛ كثير الامتنان (sihah)؛ المنة: النعمة الثقيلة؛ من فلان على فلان: إذا أثقله بالنعمة؛ المنة منهم بالقول، ومنة الله عليهم بالفعل (mufradat)
- **B004** tutsağı karşılıksız serbest bırakma [kalıp] — sonrasında tutsağı karşılıksız serbest bırakma
  فإما منا بعد وإما فداء؛ فالمن إشارة إلى الإطلاق بلا عوض (mufradat)
- **B005** eski ağırlık ölçüsü ve ölçülüp tartılmış olma — ağırlık ölçüsü veya tartılmış miktar · iki alt ağırlık birimine eşit ölçü · miktarı belirlenmiş veya tartılmış
  المن: المنا، وهو رطلان، والجمع أمنان، وجمع المنا أمناء (sihah)؛ المن: ما يوزن به؛ من، ومنان، وأمنان؛ ويقال لما يقدر: ممنون كما يقال: موزون (mufradat)
- **B006** ağaçlara çiy gibi düşen tatlı madde ve bağışlanan azık — ağaçlara çiy gibi düşen tatlı doğal madde · tatlı yiyecekle bıldırcından oluşan bağışlanmış azık
  المن: شيء حلو كالطرنجبين؛ الكمأة من المن (sihah)؛ المن شيء كالطل فيه حلاوة يسقط على الشجر؛ المن والسلوى... ما أنعم الله به عليهم (mufradat)

## خ ل ق (root_000434): 41:9 خَلَقَ, 41:15 خَلَقَهُمْ, 41:21 خَلَقَكُمْ, 41:37 خَلَقَهُنَّ

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

## ء ر ض (root_000025): 41:9 ٱلْأَرْضَ, 41:11 وَلِلْأَرْضِ, 41:15 ٱلْأَرْضِ, 41:39 ٱلْأَرْضَ

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

## ي و م (root_001700): 41:9 يَوْمَيْنِ, 41:10 أَيَّامٍ, 41:12 يَوْمَيْنِ, 41:16 أَيَّامٍ, 41:19 وَيَوْمَ, 41:40 يَوْمَ, 41:47 وَيَوْمَ

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

## ج ع ل (root_000248): 41:9 وَتَجْعَلُونَ, 41:10 وَجَعَلَ, 41:29 نَجْعَلْهُمَا, 41:44 جَعَلْنَٰهُ

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

## ن د د (root_001484): 41:9 أَندَادًا

- **B001** başını alıp kaçma ve dağılma — deve ürküp başını alarak gitti · insanların birbirinden kaçıp dağıldığı gün · her yöne dağılmış olarak · onlardan kaçıp gitmesi söz konusu değildir
  أصل صحيح يدل على شرود وفراق (maqayis)؛ ند البعير ندا وندودا إذا ذهب على وجهه شاردا (jamhara)؛ ند البعير يند نداء وندادا وندودا نفر وذهب على وجهه شاردا (sihah)؛ ند البعير يند ندودا إذا شرد (tahdhib)؛ يند بعضهم من بعض (mufradat)
- **B002** özde benzer denk ya da karşıt rakip — denk, benzer veya karşıt · denk ve benzer · denk ve benzer · eşler, benzerler veya karşıtlar · ona karşı çıktım ve onunla çekiştim · bana karşı çıkıp ters yönde çekişen kişi · özünü paylaşan benzeri
  الند والنديد الذي يناد في الامر أي يأتي برأي غير رأى صاحبه (maqayis)؛ الند المثل وكذلك النديد والنديدة (jamhara)؛ الند بالكسر المثل والنظير وكذلك النديد والنديدة (sihah)؛ الند الضد والشبه وفلان ند فلان ونديده ونديدته أي مثله وشبهه (tahdhib)؛ نديد الشيء مشاركه في جوهره وذلك ضرب من المماثلة (mufradat)
- **B003** kötüleyip söverek teşhir etme [kalıp] — onu kötüleyerek teşhir etti
  ندد به أي شهره وسمع به (sihah)؛ نددت بالرجل تنديدا وسمعت به تسميعا إذا أسمعته القبيح وشتمته (tahdhib)
- **B004** sesi yükseltme ve yüksek sesle çağırma — sesi yükseltme ve çağrıyı güçlendirme · çağrıda aşırı derecede yükseltilen ses
  التنديد رفع الصوت؛ الصوت المندد المبالغ في النداء (tahdhib)
- **B005** yüksek tepe — yüksek tepe
  الند التل المرتفع في السماء ويكون هذا قريبا من قياسه (maqayis)؛ الند التل المرتفع في السماء لغة يمانية (jamhara)؛ الند التل المرتفع في السماء (sihah)
- **B006** kökeni tartışmalı tütsü türü veya amber — bir tütsü türü veya amber; kökeni tartışmalı koku maddesi
  الند من الطيب ليس عربيا (maqayis)؛ الند المستعمل من الطيب فلا أحسبه عربيا صحيحا (jamhara)؛ الند من الطيب ليس بعربي (sihah)؛ الند ضرب من الدخنة؛ يقال للعنبر الند (tahdhib)

## ر ب ب (root_000532): 41:9 رَبُّ, 41:14 رَبُّنَا, 41:23 بِرَبِّكُمْ, 41:29 رَبَّنَآ, 41:30 رَبُّنَا, 41:38 رَبِّكَ, 41:43 رَبَّكَ, 41:45 رَّبِّكَ, 41:46 رَبُّكَ, 41:50 رَبِّىٓ, 41:53 بِرَبِّكَ, 41:54 رَبِّهِمْ (also echo for 41:39 وَرَبَتْ)

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

## ر ب و (root_000537): 41:39 وَرَبَتْ (also echo for 41:9 رَبُّ, 41:14 رَبُّنَا, 41:23 بِرَبِّكُمْ, 41:29 رَبَّنَآ, 41:30 رَبُّنَا, 41:38 رَبِّكَ, 41:43 رَبَّكَ, 41:45 رَّبِّكَ, 41:46 رَبُّكَ, 41:50 رَبِّىٓ, 41:53 بِرَبِّكَ, 41:54 رَبِّهِمْ)

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

## ر س و (root_000564): 41:10 رَوَٰسِىَ

- **B001** sağlamca yerinde kalmak; sabitlemek — yerinde sabit kaldı · sabitledi, sağlamca yerleştirdi · sabit ve sağlam yerleşmiş · yerinden ayrılmayan, sabit · sağlamca yerleşmiş sabit dağlar · duruşta veya savaşta ayakları sağlam bastı · yerinden ayrılmayan sabit kazan · bulut bir yerde kaldı ve orada devam etti · bir işin sabitlenip yerleşeceği zaman
  رسا الشيء يرسو إذا ثبت (maqayis;ayn;sihah;mufradat)؛ أرسى الجبال أي أثبتها (maqayis;mufradat)؛ رواسي من الجبال الثوابت الرواسخ (sihah)؛ رست قدماه في الموقف والحرب (ayn;sihah)؛ قدر راسية لا تبرح مكانها (ayn)؛ ألقت السحابة مراسيها ثبتت في موضع أو دامت (maqayis;ayn;sihah;mufradat)
- **B002** geminin demirleyip hareketsiz kalması — gemi demirleyip ilerlemez oldu · demirleme; demirleme yeri, zamanı veya demirlenen şey · gemiyi yerinde tutan çapa
  رست السفينة انتهت إلى قرار الماء فبقيت لا تسير (ayn)؛ رست السفينة ترسوا رسوا أي وقفت على اللنجر (sihah)؛ المرساة أنجر يشد بالحبال فيرسل في البحر فيمسك بالسفينة ويرسيها فلا تسير (ayn)؛ المرساة التي ترسى بها السفينة (sihah)؛ مرساها من أجريت وأرسيت، فالمرسى يقال للمصدر والمكان والزمان والمفعول (mufradat)
- **B003** anlatıyı nakletmek, kısmen söylemek veya zihinde pekiştirmek [kalıp] — ondan bir anlatı nakledip aktardı · işin veya anlatının bir bölümünü ona söyledi · anlatıyı kendi zihninde iyice pekiştirdi
  رسوت عنه حديثا أرسوه إذا حدثت به عنه (maqayis)؛ رسوت لفلان من هذا الأمر أو الحديث أي ذكرت له طرفا منه (ayn;sihah)؛ رسوت الحديث أحكمته فيما بينك وبين نفسك (ayn)
- **B004** insanların arasını düzeltip barışı yerleştirmek [kalıp] — insanların arasını düzeltip barışı yerleştirdi
  رسوت بين القوم رسوا إذا أصلحت (maqayis;sihah)؛ رسوت بين القوم أي أثبت بينهم إيقاع الصلح (mufradat)
- **B005** erkek devenin dağılan dişileri çağırıp geri toplaması [kalıp] — erkek deve dağılan dişi grubunu çağırıp geri topladı
  الفحل إذا تفرقت عنه شوله فصاح بها استقرت فيقال رسا بها (maqayis)؛ الفحل من الإبل إذا تفرق عنه شوله فهدر بها وراغت إليه وسكنت قيل رسا بها (ayn)؛ قد رسا الفحل بالشول وذلك إذا قعا عليها (sihah)

## ف و ق (root_001188): 41:10 فَوْقِهَا

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

## ب ر ك (root_000109): 41:10 وَبَٰرَكَ

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

## ق د ر (root_001205): 41:10 وَقَدَّرَ, 41:12 تَقْدِيرُ, 41:39 قَدِيرٌ

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

## ق و ت (root_001268): 41:10 أَقْوَٰتَهَا

- **B001** yaşamı sürdürecek azık ve bu azığı sağlama ya da edinme — yaşamı ve bedeni sürdürecek azık · azıklar ve geçim payları · azık verip geçindirmek · geçinmesine yetecek azık sağlamak · azık edinmek veya verilen azıktan yararlanmak · bir şeyi kendine azık edinmek · birinden azık istemek · bir gecelik azık ve yeterlik · geçinmeye yetecek ölçüde
  القوت ما يمسك الرمق (maqayis;ayn;tahdhib;mufradat)؛ جمعه أقوات (mufradat)؛ البلغة من الطعام (jamhara)؛ ما يقوم به بدن الإنسان من الطعام (sihah)؛ قات عياله يقوتهم قوتا (jamhara;sihah)؛ أعوله برزق قليل (ayn;tahdhib)؛ أقاته يقيته جعل له ما يقوته (mufradat)؛ فلان يتقوت بكذا واستقاته سأله القوت (sihah)
- **B002** gerekeni ölçüp koruyan, tanık olan ve gücü yeten — koruyup gözeten, tanıklık eden, gücü yeten ve gereken ölçüyü belirleyen · bir şeye gücü yetmek · yapılanların dökümünü bilmek
  مقيتا أي حافظا له شاهدا عليه وقادرا (maqayis)؛ المقيت المقتدر والمقدر (tahdhib)؛ المقيت المقتدر (sihah;mufradat)؛ المقيت الحافظ والشاهد (sihah;mufradat)؛ الحفيظ الذي يعطي الشيء قدر الحاجة من الحفظ (tahdhib)؛ قائما عليه يحفظه ويقيته (mufradat)؛ الموقوف على الشيء (tahdhib)
- **B003** ateşi odunla besleme veya hafifçe üfleyerek canlandırma [kalıp] — ateşi odunla beslemek veya hafifçe üfleyerek canlandırmak
  اقتت لنارك قيتة أي أطعمها الحطب (maqayis;sihah)؛ اقتت لها نفخك قيتة تأمره بالرفق والنفخ القليل (ayn;tahdhib)؛ وأحيها بروحك واقتته لها قيتة قدرا (mufradat)
- **B004** azar azar alıp sonunda bütünüyle tüketme [kalıp] — yolculukta devenin hörgüç yağını azar azar tüketmek · canı soluk soluk alıp yaşamı sona erdirmek
  يقتات فضل سنامها الرحل أي يأخذ الرحل وأنا راكب شحم سنام هذه الناقة قليلا قليلا حتى لا يبقى منه شيء؛ وقائت نفسي أراد بنفسه روحه والمعنى أنه يقبض روحه نفسا بعد نفس حتى يتوفاه كله

## ر ب ع (root_000536): 41:10 أَرْبَعَةِ

- **B001** dört ve dördüncü olma — dört · dört · kırk · dörder; dört katlı · topluluğun dördüncü üyesi olmak
  ربعتهم أربعهم إذا كنت لهم رابعا (maqayis)؛ وربعت القوم فأنار رابعهم (ayn)؛ ربع القوم إذا صار رابعهم؛ أربعة ضرب من العدد (jamhara)؛ الأربعة في عدد المذكر والأربع في عدد المؤنث والأربعون بعد الثلاثين؛ أربع القوم أي صاروا أربعة (sihah)؛ ربعت القوم أربعهم إذا كنت لهم رابعا (tahdhib)؛ أربعة وأربعون وربع ورباع كلها من أصل واحد (mufradat)
- **B002** dörtte bir pay — dörtte bir · topluluğun mallarının dörtte birini almak · önderin ele geçirilen mallardan aldığı dörtte bir pay
  الربع من الشيء؛ ربعت القوم إذا أخذت ربع أموالهم؛ المرباع ربع المغنم (maqayis)؛ أخذ المرباع وهو ربع الغنيمة؛ ربع المال جزء من أربعة (jamhara)؛ الربع جزء من أربعة؛ تأخذ المرباع (sihah)؛ المرباع شيء كانوا في الجاهلية؛ أخذ الرئيس ربع الغنيمة (tahdhib)؛ ولهن الربع؛ أخذت ربع أموالهم (mufradat)
- **B003** dört kollu bükme veya kareleştirme — ipi ya da teli dört koldan bükmek · kare biçimine getirme
  عنانا على أربع قوى (maqayis)؛ ربع وتره إذا جعله على أربع قوى (jamhara)؛ ربع وتره أي فتله من أربع قوى؛ التربيع جعل الشيء مربعا (sihah)؛ ربعت الوتر إذا فتلته على أربع قوى؛ وتر مربوع (tahdhib)؛ ربعت الحبل جعلته على أربع قوى (mufradat)
- **B004** dört sayısına bağlı dönemsel nöbet — dört sayısına bağlı sulama ya da ateş nöbeti · develeri dört sayılı nöbette sulamak · ateşin dört sayılı nöbetle yeniden gelmesi
  الربع في الحمى والورد ما يكون في اليوم الرابع (maqayis)؛ الربع من الورد أن تحبس الإبل عن الماء أربعة أيام ثم ترد اليوم الخامس (ayn)؛ أخذت حمى الربع من أوراد الإبل؛ ترد في اليوم الرابع (jamhara)؛ الربع في الحمى أن تأخذ يوما وتدع يومين؛ الربع أيضا الظمء (sihah)؛ الربع من أظماء الإبل؛ الربع الحمى التي تأخذ كل أربعة أيام (tahdhib)؛ الربع من أظماء الإبل والحمى (mufradat)
- **B005** bereketli bahar dönemi — bahar; bereketli mevsim · bahar yağmuru, otu veya akarsuyu · baharlık konak yeri · baharda doğan ilk deve yavrusu · baharda doğuran deve
  الربيع زمان من أربعة أزمنة؛ المربع منزل القوم في ذلك الزمان؛ الربع الفصيل ينتج في الربيع (maqayis)؛ الربيع جزء من أجزاء السنة؛ سمي الغيث ربيعا؛ الكلأ ربيعا؛ النهر ربيعا؛ ناقة مربع تنتج في أول الربيع (jamhara)؛ الربيع عند العرب ربيعان؛ الربيع المطر في الربيع؛ الربيع الجدول؛ المربع منزل القوم في الربيع (sihah)؛ أول مطر يقع بالأرض أيام الخريف ربيع؛ ربيع الكلأ؛ ربيع النهر؛ ولد الناقة ينتج في أول النتاج ربع (tahdhib)
- **B006** yerleşme ve yerleşik kalma — ev, konut veya mahalle · bir yerde kalmak · bekle, yavaşla ve kendini zorlama · eski yerlerinde veya ilk düzenlerinde kalmaları
  الأصل الآخر الإقامة؛ الربع محلة القوم؛ اربع على ظلعك أي تمكث وانتظر (maqayis)؛ ربع الرجل بالمكان إذا أقام به؛ بنو فلان على رباعتهم أي على مواضعهم (jamhara)؛ الربع الدار؛ الربع المحلة؛ ربع الرجل إذا وقف وتحبس؛ الناس على ربعاتهم (sihah)؛ الربع هو الدار؛ الربع مثل السكن؛ قد ربع الرجل إذا وقف وتحبس؛ اربع على ظلعك معناه انتظر (tahdhib)
- **B007** kaldırma ve birlikte yük taşıma — taşı elle kaldırmak · iki kişinin kullandığı kısa taşıma sırığı · bir başkasıyla birlikte yük kaldırmak
  الأصل الثالث ربعت الحجر إذا أشلته؛ المربعة العصا التي تحمل بها الأحمال؛ رابعني فلان إذا حمل معك الحمل (maqayis)؛ ربع فلان الحجر إذا ازدمله بيده؛ المربعة عصا قصيرة يحمل بها العكم (jamhara)؛ ربعت الحجر وارتبعته إذا أشلته؛ المربعة عصية يأخذ الرجلان بطرفيها؛ رابعتني (sihah)؛ الربع أن يشال الحجر باليد؛ المربعة عصا يحمل بها الأثقال؛ رابعت الرجل إذا رفعت معه العدل (tahdhib)
- **B008** orta boylu ve dengeli yapılı — orta boylu, dengeli yapılı · ne uzun ne kısa
  رجل ربعة من الرجال؛ وقياس الربعة من الباب الثاني (maqayis)؛ رجل مربوع ومرتبع وربع وربعة إذا كان معتدل الخلق؛ المرابيع من الخيل المجتمعة الخلق (jamhara)؛ رجل ربعة أي مربوع الخلق لا طويل ولا قصير (sihah)؛ المربوع الذي ليس بطويل ولا قصير؛ رجل ربعة وامرأة ربعة (tahdhib)
- **B009** yan kesici diş ve buna bağlı yaş evresi — yan kesici diş · yan kesici dişini değiştirmiş hayvan
  رباعيات الأسنان ما دون الثنايا (maqayis)؛ الرباعي من الدواب الذي سقطت رباعيتاه؛ رباعية الإنسان معروفة (jamhara)؛ الرباعية السن التي بين الثنية والناب؛ الذي يلقي رباعيته رباع (sihah)؛ رباعيته فتنبت مكانها سن فهو رباع؛ للإنسان رباعيتان (tahdhib)
- **B010** Çarşamba — Çarşamba
  الأربعاء على أفعلاء من الأيام (maqayis)؛ الأربعاء معروف بكسر الباء؛ الأربعاء بفتح الباء موضع (jamhara)؛ الاربعاء من الأيام؛ الجمع أربعاوات (sihah)؛ يوم الأربعاء بكسر الباء ممدود (tahdhib)
- **B011** bağdaş kurarak oturma [kalıp] — bağdaş kurup oturmak · bağdaş kurarak oturmak
  تربع في جلوسه (sihah)؛ قعد فلان الأربعاء والأربعاوى أي متربعا (tahdhib)
- **B012** devenin bütün ayaklarıyla en hızlı koşusu [kalıp] — devenin bütün ayaklarıyla en hızlı biçimde koşması
  ارتبع البعير ارتباعا وربعة وهو أشد العدو (jamhara)؛ الربعة أشد عدو الإبل؛ مر البعير يرتبع إذا ضرب بقوائمه كلها (sihah)؛ ارتبع البعير يرتبع ارتباعا والاسم الربعة وهو أشد عدو البعير (tahdhib)

## س و ي (root_000766): 41:10 سَوَآءً, 41:11 ٱسْتَوَىٰٓ, 41:34 تَسْتَوِى

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

## س ء ل (root_000661): 41:10 لِّلسَّآئِلِينَ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 41:10 لِّلسَّآئِلِينَ: withheld observed target; not identity

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

## س م و (root_000745): 41:11 ٱلسَّمَآءِ, 41:12 سَمَٰوَاتٍ, 41:12 سَمَآءٍ, 41:12 ٱلسَّمَآءَ

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

## ECHO و س م (root_001650): for 41:11 ٱلسَّمَآءِ, 41:12 سَمَٰوَاتٍ, 41:12 سَمَآءٍ, 41:12 ٱلسَّمَآءَ: withheld observed target; not identity

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

## د خ ن (root_000465): 41:11 دُخَانٌ

- **B001** yakıttan yükselen duman — ateşten veya yakıttan çıkan duman · ateşin dumanı yükseldi veya çoğaldı · toz, duman gibi havaya yükseldi · duman · duman · dumanlar
  الدخان دخونا سطع؛ دخن الغبار أي سطع؛ اشتقاقه من الدخان والدخان يسمى الدخن أيضا؛ دخان النار معروف والجمع دواخن؛ الدخان كالعثان المستصحب للهيب؛ أصل واحد وهو الذي يكون عن الوقود؛ الدخ فقد ذكر في بابه وهو الدخان
- **B002** dumanla tütsüleme veya bozma — evi tütsülemekte kullanılan kokulu madde · ateşe odun atıp onu bozarak dumanını artırdı · yemek dumandan bozuldu · tencereye duman sindi ve içindeki yemeği etkiledi · bozulmuş veya duman sinmiş yemek
  الدخنة بخنور يدخن به؛ وطعام دخن فاسد؛ دخنت النار إذا ألقيت عليها حطبا وأفسدتها حتى يهيج لذلك دخان؛ دخن الطبيخ إذا تدخنت القدر؛ الدخنة منه لكن تعورف فيما يتبخر به من الطيب؛ دخن الطبيخ أفسده الدخان؛ والدخنة بخور يدخن به البيت
- **B003** dumanımsı bulanık siyah renk — siyah içinde dumanımsı bulanıklık · külümsü bulanıklık taşıyan siyaha çalar renk · dumanımsı bulanık siyah renkli · dumanımsı bulanık siyah renkli · dumanımsı bulanık siyah renge sahip
  الدخنة من لون الأدخن وهو كدرة في سواد كالدخان؛ شاة دخناء وكبش أدخن؛ لون أسود فيه غبرة حمار أدخن وأتان دخناء؛ الدخن أيضا الكدورة إلى السواد؛ الدخنة من الالوان كالكدرة في سواد؛ وتصور من الدخان اللون فقيل شاة دخناء وذات دخنة؛ والدخنة من الألوان كدرة في سواد
- **B004** örtük bozukluk ve dinmeyen düşmanlık — içinde bozukluk ve hoşnutsuzluk kalan ateşkes · kalpte eski düşmanlıktan kalan bozukluk · huyu ve iç yapısı bozuk
  هدنة على دخن أي صلح واستقرار على أمور مكروهة؛ فساد في القلب من باقي عداوة؛ هدنة على دخن أي سكون لعلة لا لصلح؛ رجل دخن الخلق؛ تصور منه التأذي به فقيل هو دخن الخلق وروي هدنة على دخن أي على فساد دخلة؛ يشبه به كل شيء يشبهه من عداوة ونظيرها
- **B005** darı — darı; yenip ekmek yapılabilen tahıl · bir darı tanesi
  الدخن الجاورس والحبة منه دخنة؛ والدخن عربي حب يختبز ويؤكل؛ والدخن الجاورس
- **B006** yalıtık adlandırmalar — duman çıkış açıklığı · tütsü kabı · topluluğun görülen dumanları
  الداخنة كوى فيها إردبات تتخذ على المقالي والأتونات؛ رأيت دواخن القوم إذا رأيت دخانهم؛ والمدخنة والمبخرة واحد
- **B007** duman basmışçasına sıcak ve boğucu zaman [kalıp] — duman çökmüşçesine sıcak ve boğucu gece · çok sıcak ve bunaltıcı gün
  ليلة دخنانة كأنما يغشاها دخان من شدة حرها وغمها؛ ويوم دخنان سخنان؛ وليلة دخنانة؛ وتصور من الدخان اللون فقيل ليلة دخنانة؛ وليلة دخنانة
- **B008** bir tür serçe — bir tür serçe
  والدخناء ضرب من العصافير

## ط و ع (root_000956): 41:11 طَوْعًا, 41:11 طَآئِعِينَ

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

## ECHO س ط ع (root_000706): for 41:11 طَوْعًا, 41:11 طَآئِعِينَ: withheld observed target; not identity

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

## ك ر ه (root_001295): 41:11 كَرْهًا

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

## ق ض ي (root_001237): 41:12 فَقَضَىٰهُنَّ, 41:45 لَقُضِىَ

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

## س ب ع (root_000669): 41:12 سَبْعَ

- **B001** yedi sayısı ve yediye dayalı pay, sıra, dönem, işlem ve çokluk anlatımları — yedi · yedide bir · altı kişilik topluluğun yedincisi oldu · topluluğun malının yedide birini aldı · develer için yediye bağlı sulama aralığı · hafta; yedi günlük dönem · yapının çevresinde yedi tur döndü · metnin tamamını yedi geceye bölerek okudu · eşinin yanında yedi gece kaldı · bebeğin yedinci gününde saçını kesip onun için hayvan kesti · kabı yedi kez yıkadı · Tanrı onun ödülünü yedi katına ya da kat kat çıkardı · bir şeyi yedi yapmak ya da kat kat çoğaltmak · yetmiş; kimi bağlamlarda pek çok · yedide bir ya da yediye bağlı sulama aralığı için seyrek kullanılan biçim
  السين والباء والعين أصلان أحدهما في العدد؛ السبعة؛ السبع جزء من سبعة؛ سبعت القوم إذا أخذت سبع أموالهم أو كنت لهم سابعا؛ السبع ظمء من أظماء الإبل (maqayis)؛ السبع من العدد معروف؛ صرت سابعهم؛ سبع الشيء واحد من سبعة؛ الأسبوع؛ طفت بالبيت سبعا وسبوعا؛ سبع المولود؛ سبعت الإناء؛ سبع الله لك أي أعطاك أجرك سبع مرات (jamhara)؛ سبعة رجال وسبع نسوة؛ السبع جزء من سبعة؛ السبع الظمء؛ الأسبوع من الأيام؛ تسبيعا جعلته سبعة؛ وزن سبعة (sihah)؛ السبع من العدد معروف؛ السبعون معروف؛ أقام عندها سبعا؛ سبع فلان القرآن؛ الأسبوع؛ التكثير والتضعيف لا من باب حصر العدد (tahdhib)؛ أصل السبع العدد؛ سبع سماوات؛ سبعين مرة؛ سبعا من المثاني؛ السبع الطوال؛ السبيع والسبع في الورود؛ الأسبوع؛ طفت بالبيت أسبوعا؛ سبعت القوم (mufradat)
- **B002** avlayan yırtıcı hayvan ve onun saldırısına bağlı durumlar — yırtıcı hayvan · dişi yırtıcı; özellikle dişi aslan · yırtıcı hayvanların bol bulunduğu yer · onu yırtıcı hayvana yem etti · kurt sürüye saldırıp hayvanları parçaladı · yavrusu yırtıcı tarafından yenmiş dişi sığır ya da yabani hayvan · sürüsüne yırtıcı hayvan saldırmış çoban
  السبع واحد من السباع؛ أرض مسبعة إذا كثر سباعها؛ أسبعته أطعمته السبع؛ سبعت الذئاب الغنم إذا فرستها وأكلتها (maqayis)؛ السبع واحد السباع والأنثى سبعة (ayn)؛ السبع اسم يجمع السباع أسودها وذئابها؛ الذكر من السباع سبع والأنثى سبعة؛ أرض مسبعة ذات سباع (jamhara)؛ السبع واحد السباع؛ السبعة اللبؤة؛ أرض مسبعة ذات سباع؛ سبع الذئب الغنم أي فرسها؛ المسبوعة البقرة التي أكل السبع ولدها (sihah)؛ السبع يقع على ماله ناب من السباع ويعدو على الناس والدواب فيفترسها مثل الأسد والذئب والنمر والفهد؛ الثعلب ليس بسبع؛ الضبع لا يعد من السباع العادية؛ أرض مسبعة كثيرة السباع؛ سبعت الوحشية إذا أكل السبع ولدها (tahdhib)؛ والسبع معروف؛ قد وقع السبع في غنمه؛ المسبع موضع السبع (mufradat)
- **B003** birini kötüleyip arkasından çekiştirmek; sınırlı kullanımda ısırmak — onu kötüledi, arkasından çekiştirdi ya da ona sövdü · onu dişiyle ısırdı
  سبعته إذا وقعت فيه كأنه شبه نفسه بسبع في ضرره وعضه (maqayis)؛ سبعت فلانا عند فلان إذا وقعت فيه وقيعة مضرة (ayn)؛ سبعت الرجل عند السلطان وغيره إذا طعنت فيه (jamhara)؛ سبعته أي شتمته ووقعت فيه (sihah)؛ سبع فلان فلانا إذا قصبه واقترضه أي عابه واغتابه؛ سبع فلانا إذا عضه بسنه؛ يتساب الرجلان فيرمي كل واحد منهما صاحبه بما يسوءه (tahdhib)؛ سبع فلان فلانا اغتابه وأكل لحمه أكل السباع (mufradat)
- **B004** biçime bağlı adlandırmalar — el üstünde tutulmuş, bolluk içinde yaşatılan hizmetli · sürüsüne yırtıcı hayvan saldırmış çoban · başıboş bırakılmış kimse · babası bilinmeyen ya da soyu kuşkulu kimse · yedi aylık doğmuş bebek · çocuğunu sütanneye verdi · yırtıcı hayvanın bulunduğu yer
  عبد مسبع؛ أحدها المترف؛ الراعي؛ لم يكن لرشده؛ عبد إلى سبعة آباء؛ ولد لسبعة أشهر؛ المسبع المهمل (maqayis)؛ عبد مسبع عبد مترف؛ هو في لغة الدعي؛ المسبع الراعي الذي أغارت السباع على غنمه (ayn)؛ رجل مسبع إذا عاث السبع في غنمه؛ غلام مسبع إذا أهمل حتى صار كأنه سبع؛ المسبع الدعي (jamhara)؛ أسبع ابنه دفعه إلى الظؤورة؛ أسبع عبده أهمله؛ عبد قد صادف في غنمه سبعا؛ المسبوعة البقرة التي أكل السبع ولدها (sihah)؛ المسبع المهمل؛ ينسب إلى أربع أمهات؛ إلى سبع أمهات؛ التابعة؛ يولد لسبعة أشهر؛ وقع السباع في ماشيته (tahdhib)؛ وقع السبع في غنمه؛ المهمل مع السباع؛ كني بالمسبع عن الدعي الذي لا يعرف أبوه؛ المسبع موضع السبع (mufradat)
- **B005** çok sert biçimde ele geçirmek ya da en ağır kötülüğü yapmak [kalıp] — onu çok sert biçimde ele geçirdi · ona yapılabilecek en ağır kötülüğü yaptı
  لأفعلن به فعل سبعة يريدون به المبالغة في الشر؛ أراد بالسبعة اللبؤة؛ أراد سبعة فخفف (maqayis)؛ لأفعلن بك فعل سبعة؛ كان سبعة رجلا ماردا؛ فنكل به فصار مثلا (jamhara)؛ أخذه أخذ سبعة؛ أصلها سبعة فخففت؛ اللبؤة أنزق من الأسد؛ سبعة ابن عوف وكان رجلا شديدا (sihah)؛ أخذه أخذ سبعة؛ أصلها سبعة فخففت؛ اللبؤة أنزق من الأسد؛ سبعة بن عوف وكان رجلا شديدا؛ لأعملن بفلان عمل سبعة المبالغة وبلوغ الغاية (tahdhib)

## ك ل ل (root_001315): 41:12 كُلِّ, 41:21 كُلَّ, 41:39 كُلِّ, 41:53 كُلِّ, 41:54 بِكُلِّ

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

## ء م ر (root_000051): 41:12 أَمْرَهَا

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

## ز ي ن (root_000660): 41:12 وَزَيَّنَّا, 41:25 فَزَيَّنُوا۟

- **B001** ayıptan uzak güzellik — güzellik; ayıp ve çirkinliğin karşıtı · güzel ve alımlı yüz · güzelliği onu güzel ve alımlı kıldı
  الزين نقيض الشين (maqayis;ayn;tahdhib)؛ زانه الحسن يزينه زينا (ayn;tahdhib)؛ الزينة الحقيقية ما لا يشين الإنسان (mufradat)
- **B002** güzelleştirme ve güzelliğini görünür kılma — bir şeyi güzelleştirmek ve güzelliğini ortaya çıkarmak · onun güzelliğini davranışla ya da sözle görünür kılmak · yer, otlarıyla güzelleşip canlandı · yer güzelleşip canlandı · yer güzelleşip canlandı · onu gönlünde güzel ve sevimli göstermek · yaptığı işi ona güzel göstermek · yeryüzündekileri ona güzel göstermek · dünya hayatını güzel göstermek · yakın göğü kandillerle bezemek
  أصل صحيح يدل على حسن الشيء وتحسينه (maqayis)؛ زينت الشيء تزيينا (maqayis)؛ ازدانت الأرض بعشبها وازينت وتزينت (ayn;tahdhib)؛ زانه وزينه إذا أظهر حسنه إما بالفعل أو بالقول (mufradat)؛ زينا السماء الدنيا بمصابيح وزينة الكواكب (mufradat)
- **B003** bezenmeye yarayan nitelik ve şeylerin bütünü — bezenmek için kullanılan her şeyin ortak adı · kişiyi hiçbir durumda ayıplı kılmayan gerçek güzellik · bilgi ve iyi inanç gibi içsel güzellik · güç ve uzun boy gibi bedensel güzellik · mal ve saygınlık gibi dışsal süs · mal, eşya ve saygınlık türünden dünyalık süs · Tanrı'nın sunduğu süs; başka yorumlarda cömertlik ya da kötülükten sakınma erdemi · yıldızların gözle algılanan süsü
  الزينة جامع لكل ما يتزين به (ayn)؛ الزينة اسم جامع لكل شيء يتزين به (tahdhib)؛ الزينة بالقول المجمل ثلاث: زينة نفسية وزينة بدنية وزينة خارجية (mufradat)؛ فهي الزينة الدنيوية من المال والأثاث والجاه (mufradat)

## د ن و (root_000493): 41:12 ٱلدُّنْيَا, 41:16 ٱلدُّنْيَا, 41:31 ٱلدُّنْيَا

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

## ص ب ح (root_000839): 41:12 بِمَصَٰبِيحَ, 41:23 فَأَصْبَحْتُم

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

## ح ف ظ (root_000342): 41:12 وَحِفْظًا

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

## ع ز ز (root_001008): 41:12 ٱلْعَزِيزِ, 41:41 عَزِيزٌ

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

## ص ع ق (root_000864): 41:13 صَٰعِقَةً, 41:13 صَٰعِقَةِ, 41:17 صَٰعِقَةُ

- **B001** çok güçlü ve sert ses — çok güçlü ses, özellikle güçlü anırma · boğanın veya eşeğin çok güçlü sesi · güçlü sesli eşek
  أصل واحد يدل على صلقة وشدة صوت؛ الصعق، وهو الصوت الشديد (maqayis)؛ الصعاق الصوت الشديد للثور والحمار؛ حمار صعق الصوت أي شديده (ayn)؛ حمار صعق الصوت، أي شديده (sihah)؛ شدة نهيقه وصوته (tahdhib)
- **B002** yıkıcı gök gürlemesi veya yıldırım çarpması — yıkıcı gök gürlemesi veya yıldırım çarpması · işiteni bayıltan veya öldüren çığlık · yıldırımlar veya güçlü gök gürlemeleri · gök üzerlerine yıldırım düşürdü · yıldırım ona çarparak bayılttı veya öldürdü · ses değişmesiyle söylenen bir yıldırım adı
  الصاعقة، وهي الوقع الشديد من الرعد (maqayis)؛ الصاعقة صيحة العذاب؛ الوقع الشديد من صوت الرعد يسقط معه قطعة من نار (ayn)؛ الصاعقة: نار تسقط من السماء في رعد شديد؛ الصاعقة أيضا: صيحة العذاب (sihah)؛ الصاعقة والصعقة: الصيحة؛ أصوات الرعد (tahdhib)؛ الصاعقة هي الصوت الشديد من الجو؛ يكون منها نار فقط، أو عذاب، أو موت (mufradat)
- **B003** sarsıcı bir etkiyle bilinci yitirme veya ölme — sarsıcı bir etki yüzünden ölmek · bir ses veya duyusal etkiyle bayılıp bilincini yitirmek · baygın, bilincini yitirmiş kimse · birini bayıltmak veya öldürmek · göksel çarpmaya uğrayıp bayılmış veya ölmüş kimse · yıldırım ona çarparak bayılttı veya öldürdü
  صعق، إذا مات، كأنه أصابته صاعقة (maqayis)؛ الصعق المغشي عليه؛ غشي عليه من صوت يسمعه أو حس أو نحوه؛ صعق صعقا مات (ayn)؛ صعق الرجل صعقة وتصعاقا، أي غشي عليه؛ فصعق... أي مات (sihah)؛ فسروه الموت ها هنا؛ معناه مغشيا عليه؛ الصعق مثل الغشي يأخذ الإنسان من الحر وغيره (tahdhib)؛ الموت... أشياء حاصلة من الصاعقة (mufradat)

## ع و د (root_001058): 41:13 عَادٍ, 41:15 عَادٌ (also echo for 41:19 أَعْدَآءُ, 41:28 أَعْدَآءِ, 41:34 عَدَٰوَةٌ)

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

## ECHO ع د د (root_000989): for 41:13 عَادٍ, 41:15 عَادٌ, 41:19 أَعْدَآءُ, 41:28 أَعْدَآءِ, 41:30 تُوعَدُونَ, 41:34 عَدَٰوَةٌ: withheld observed target; not identity

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

## ج ي ء (root_000281): 41:14 جَآءَتْهُمُ, 41:20 جَآءُوهَا, 41:41 جَآءَهُمْ

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

## ج ي ء (root_000282): 41:14 جَآءَتْهُمُ, 41:20 جَآءُوهَا, 41:41 جَآءَهُمْ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ر س ل (root_000563): 41:14 ٱلرُّسُلُ, 41:14 أُرْسِلْتُم, 41:16 فَأَرْسَلْنَا, 41:43 لِلرُّسُلِ

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

## ي د ي (root_001693): 41:14 أَيْدِيهِمْ, 41:25 أَيْدِيهِمْ, 41:42 يَدَيْهِ

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

## ECHO ء ي د (root_000071): for 41:14 أَيْدِيهِمْ, 41:25 أَيْدِيهِمْ, 41:42 يَدَيْهِ: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## خ ل ف (root_000433): 41:14 خَلْفِهِمْ, 41:25 خَلْفَهُمْ, 41:42 خَلْفِهِۦ, 41:45 فَٱخْتُلِفَ

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

## ع ب د (root_000973): 41:14 تَعْبُدُوٓا۟, 41:37 تَعْبُدُونَ, 41:46 لِّلْعَبِيدِ

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

## ش ي ء (root_000831): 41:14 شَآءَ, 41:21 شَىْءٍ, 41:39 شَىْءٍ, 41:40 شِئْتُمْ, 41:53 شَىْءٍ, 41:54 شَىْءٍ

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

## ش ي ء (root_000832): 41:14 شَآءَ, 41:21 شَىْءٍ, 41:39 شَىْءٍ, 41:40 شِئْتُمْ, 41:53 شَىْءٍ, 41:54 شَىْءٍ

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

## م ل ك (root_001444): 41:14 مَلَٰٓئِكَةً, 41:30 ٱلْمَلَٰٓئِكَةُ

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

## ك ب ر (root_001281): 41:15 فَٱسْتَكْبَرُوا۟, 41:38 ٱسْتَكْبَرُوا۟

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

## ح ق ق (root_000347): 41:15 ٱلْحَقِّ, 41:25 وَحَقَّ, 41:53 ٱلْحَقُّ

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

## ش د د (root_000782): 41:15 أَشَدُّ, 41:15 أَشَدُّ, 41:27 شَدِيدًا

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

## ق و ي (root_001274): 41:15 قُوَّةً, 41:15 قُوَّةً

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

## ر ء ي (root_000531): 41:15 يَرَوْا۟, 41:29 أَرِنَا, 41:39 تَرَى, 41:52 أَرَءَيْتُمْ, 41:53 سَنُرِيهِمْ

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

## ECHO ر و ي (root_000615): for 41:15 يَرَوْا۟, 41:29 أَرِنَا, 41:39 تَرَى, 41:52 أَرَءَيْتُمْ, 41:53 سَنُرِيهِمْ: withheld observed target; not identity

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

## ج ح د (root_000224): 41:15 يَجْحَدُونَ, 41:28 يَجْحَدُونَ

- **B001** içten bildiğinin tersini söyleyerek bile bile yadsıma — doğru olduğunu bilerek yadsıma; içten benimsediğinin tersini söyleme · doğru olduğunu bildiği şeyi yadsımak veya içten benimsediğinin tersini söylemek · birine düşen payı ya da alacağı tanımamak · bile bile yadsımaya özgü biçimde davranmak
  الجحود وهو ضد الإقرار ولا يكون إلا مع علم الجاحد به أنه صحيح (maqayis); الجحود ضد الاقرار كالانكار والمعرفة (ayn;tahdhib); الجحود الإنكار مع العلم وجحده حقه وبحقه (sihah); الجحود نفي ما في القلب إثباته وإثبات ما في القلب نفيه (mufradat)
- **B002** iyilik, geçim, mal, yağmur ya da bitki bakımından azlık ve darlık — azlık, darlık, eli sıkılık ve iyilik azlığı · iyilik ve yarar azlığı · iyilik ve yarar azlığı · yoksul, eli dar, cimri ve az iyilik yapan kişi · eli dar ve az iyilik yapan olmak; malı tükenmek · malı tükenmek ve darlık durumuna düşmek · yağmuru az yıl · az ve kısa kalmak; yeterince büyümemek · bitkisi az toprak · darlık ve iyilik azlığı dileyen kınama veya beddua sözü · malı tükenmiş veya elindeki varlık azalmış
  أصل يدل على قلة الخير وعام جحد قليل المطر ورجل جحد فقير والجحد من كل شيء القلة وأجحد الرجل وجحد إذا أنفض وذهب ماله (maqayis); الجحد من الضيق والشح ورجل جحد قليل الخير (ayn); الجحد قلة الخير وجحد الرجل إذا كان ضيقا قليل الخير وعام جحد قليل المطر وجحد النبت إذا قل ولم يطل (sihah); الجحد من الضيق والشح وجحد عيشهم إذا ضاق واشتد (tahdhib); رجل جحد شحيح قليل الخير يظهر الفقر وأرض جحدة قليلة النبت (mufradat)
- **B003** kısa ve kalın yapılı at — kalın gövdeli, kısa boylu at · kalın gövdeli, kısa boylu dişi at · kalın gövdeli, kısa boylu atlar
  فرس جحد والأنثى جحدة والجميع جحاد وهو الغليظ القصير (tahdhib)
- **B004** süt dolu tulum veya hurma ya da buğday dolu büyük çuval — 
  الجحادية قربة ملئت لبنا أو غرارة ملئت تمرا أو حنطة (tahdhib)

## ر و ح (root_000609): 41:16 رِيحًا

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

## ص ر ص ر (root_000857): 41:16 صَرْصَرًا

- **B001** küçük bir canlı — küçük bir canlı
  الصرصر: دويبة
- **B002** çekirge cırıltısı ve şahinin benzer ses çıkarması — çekirge cırıltısı · şahin için cırıltılı ses çıkarmak · şahinin cırıltılı ses çıkarması
  والصرصرة: صوت صر الجندب؛ والبازي صر صرا وصرصر يصرصر صرصرة
- **B003** bir deve çeşidi veya onun yavrusu — belirli bir deve çeşidi veya onun yavrusu
  والصرصور: البختي من الإبل وولد البختي بالصاد والسين
- **B004** soğuk rüzgar [kalıp] — soğuk rüzgar · soğuk rüzgar
  وريح صر وصرصر: باردة

## ن ح س (root_001480): 41:16 نَّحِسَاتٍ

- **B001** uğursuzluk ve ters talih — uğursuzluk, ters talih · uğursuz hâle gelmek · uğursuz, bahtsız · uğursuz gün · uğursuz günler · uğursuz yıl · uğursuz sayılan yıldızlar ve benzerleri · uğursuzluklar, kötü alametler
  النحس خلاف السعد (maqayis;ayn;jamhara); النحس ضد السعد (sihah;tahdhib;mufradat); يوم نحس وأيام نحسات (maqayis;ayn;sihah;tahdhib;mufradat); المناحس المشائم (jamhara)
- **B002** soğuk rüzgâr ve rüzgârda soğuma — çok soğuk günler · soğuk rüzgâr; rüzgârda soğuma
  العرب تسمي الريح الباردة إذا دبرت نحسا (tahdhib); لنحس أي وضعت في ريح فبردت (tahdhib); قيل شديدات البرد (mufradat)
- **B003** kuraklıkta göğü kaplayan veya kalkan toz — kuraklıkta göğü kaplayan veya kalkan toz · toz kalktı
  النحس الغبار في أقطار السماء إذا عكف الجدب عليها (jamhara); النحس الغبار، يقال هاج النحس أي الغبار (tahdhib)
- **B004** kızılımsı bakır veya pirinç türü metal — bakır, pirinç türü metal veya bu metalden kap
  النحاس من هذه الجواهر (maqayis); النحاس ضرب من الصفر شديد الحمرة (ayn); النحاس القطر عربي معروف (jamhara); النحاس معروف (sihah); النحاس الصفر والآنية (tahdhib); تشبيه في اللون بالنحاس (mufradat)
- **B005** alevsiz duman — 
  النحاس الدخان لا لهب فيه (maqayis); النحاس الدخان الذي لا لهب فيه (ayn;jamhara); النحاس أيضا دخان لا لهب فيه (sihah); النحاس الدخان (tahdhib)
- **B006** dumansız alev — 
  فالنحاس اللهيب بلا دخان (mufradat); تشبيه في اللون بالنحاس (mufradat); أصل النحس أن يحمر الأفق فيصير كالنحاس (mufradat)
- **B007** köken, tabiat ve yaradılış — köken, tabiat ve yaradılış · soylu yaradılışlı · soylu bir kökten
  مبلغ أصل الشيء نحاس (maqayis); النحاس مبلغ طبع وأصله (ayn); فلان من نحاس صدق أي من أصل كريم (jamhara); النحاس الطبيعة والأصل وكريم النحاس (sihah); النحاس والنحاس جميعا الطبيعة، ونحاس الرجل ونحاسه سجيته وطبيعته (tahdhib)
- **B008** haberi soruşturup izini sürmek — haberleri soruşturup izlemek · haberin izini sürüp araştırmak
  تنحست الأخبار وعن الأخبار إذا تخبرت عنها وتتبعتها بالاستخبار سرا وعلانية (sihah); استنحست الخبر إذا تندسته وتحسسته (tahdhib)
- **B009** acıkmak; belirli kullanımda hayvan eti yemeyi bırakmak — Hristiyanlar hayvan eti yemeyi bıraktı · acıkmak, aç kalmak
  تنحس النصارى عربي صحيح لتركهم أكل الحيوان ولا أدري ما أصله (jamhara); تنحس فلان إذا تجوع (jamhara)

## ذ و ق (root_000526): 41:16 لِّنُذِيقَهُمْ, 41:27 فَلَنُذِيقَنَّ, 41:50 أَذَقْنَٰهُ, 41:50 وَلَنُذِيقَنَّهُم

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

## ع ذ ب (root_000994): 41:16 عَذَابَ, 41:16 وَلَعَذَابُ, 41:17 ٱلْعَذَابِ, 41:27 عَذَابًا, 41:50 عَذَابٍ

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

## خ ز ي (root_000407): 41:16 ٱلْخِزْىِ, 41:16 أَخْزَىٰ

- **B001** aşağılanıp küçük düşürülme — aşağılanma, küçük düşme ve değersiz görülme · aşağılandı ve değersiz duruma düştü · aşağıladı, küçük düşürdü veya gözden çıkarıp uzaklaştırdı · Konuklarım yüzünden beni küçük düşürmeyin · aşağılanmış ve değersiz görülen kimse
  أخزاه الله أي أبعده ومقته والاسم الخزي (maqayis)؛ خزي أي ذل وهان وأخزاه الله (sihah)؛ الخزي السوء والخزي الهوان وأخزيته أي فضحته (tahdhib)؛ من غيره ضرب من الاستخفاف ومصدره الخزي (mufradat)
- **B002** utançtan içten ezilme — aşırı utanç ve içten ezilme · yaptığından utanıp içten ezildi · ondan utandım · utancından içten ezilen kimse · Cennetteki eşleri davranışlarınız ve eksikleriniz yüzünden utandırmayın · utandırdı ve içten ezilmelerine yol açtı
  خزي الرجل استحيا من قبح فعله خزاية فهو خزيان (maqayis)؛ خزي خزاية أي استحياء فهو خزيان وقوم خزايا وامرأة خزياء (sihah)؛ من الحياء ممدود خزاية وخزيت فلانا إذا استحييت منه ورجل خزيان (tahdhib)؛ من نفسه هو الحياء المفرط ومصدره الخزاية (mufradat)
- **B003** ağır sıkıntı ve kötülüğe düşmek — ağır sıkıntı ve kötülüğe düştü; yıkıma uğradı
  وقع في بلية (sihah)؛ من الهلاك خزي الرجل يخزى خزيا؛ خزي يخزى خزيا إذا وقع في بلية وشر (tahdhib)

## ح ي ي (root_000383): 41:16 ٱلْحَيَوٰةِ, 41:31 ٱلْحَيَوٰةِ, 41:39 أَحْيَاهَا, 41:39 لَمُحْىِ

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

## ح ي و (root_005544): documented alternative for 41:16 ٱلْحَيَوٰةِ, 41:31 ٱلْحَيَوٰةِ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## ن ص ر (root_001510): 41:16 يُنصَرُونَ

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

## ه د ي (root_001583): 41:17 فَهَدَيْنَٰهُمْ, 41:17 ٱلْهُدَىٰ, 41:44 هُدًى

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

## ECHO ه د د (root_001580): for 41:17 فَهَدَيْنَٰهُمْ, 41:17 ٱلْهُدَىٰ, 41:44 هُدًى: withheld observed target; not identity

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

## ح ب ب (root_000286): 41:17 فَٱسْتَحَبُّوا۟

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

## ع م ي (root_001049): 41:17 ٱلْعَمَىٰ, 41:44 عَمًى

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

## ECHO ع م م (root_001047): for 41:17 ٱلْعَمَىٰ, 41:44 عَمًى: withheld observed target; not identity

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

## ء خ ذ (root_000018): 41:17 فَأَخَذَتْهُمْ

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

## ه و ن (root_001608): 41:17 ٱلْهُونِ

- **B001** yumuşak, ağırbaşlı sakinlik — sakinlik, ağırbaşlılık ve yumuşaklık · ağırbaşlı ve sakin yürümek · ölçülü ve aşırılığa kaçmadan · acele etmeden, sakince · uysal, sakin ve yumuşak huylu
  الهون مصدر الهين في معنى السكينة والوقار؛ هو يمشي هونا؛ تكلم على هينتك؛ رجل هين لين (ayn)؛ الهون: السكينة والوقار؛ يمشي على الأرض هونا؛ قوم هينون لينون؛ امش على هينتك أي على رسلك (sihah)؛ تذلل الإنسان في نفسه لما لا يلحق به غضاضة؛ يمشون على الأرض هونا؛ المؤمن هين لين (mufradat)؛ أصيل يدل على سكون أو سكينة أو ذل؛ الهون السكينة والوقار (maqayis)
- **B002** kolay ve hafif olma — kolaylık ve yükün hafifliği · birine kolay ve hafif gelmek · onun için kolaylaştırıp hafifletmek · kolay, hafif ve güç olmayan · daha kolay ve daha hafif
  الهون: مصدر هان عليه الشيء أي خف؛ هونه الله عليه أي سهله وخففه؛ شيء هين أي سهل (sihah)؛ هان الأمر على فلان: سهل؛ هو علي هين؛ وهو أهون عليه؛ وتحسبونه هينا (mufradat)؛ الهين: الأمر الهين وهو من الواو وقد مر (maqayis)
- **B003** küçümsenmeden doğan aşağılanma ve onur kaybı — aşağılanma, değersizlik ve güçsüzlük · küçümsenmeden doğan aşağılanma ve küçük düşürülme · değersizlik, küçük düşmüşlük ve güçsüzlük · insanlarca değersiz ve saygıya layık görülmeyen · onu aşağılayıp küçük düşürmek · onu hor görüp değersiz saymak · onu küçümseyerek önemsememek · aşağılayıcı ve küçük düşürücü ceza · aşağılayan ve küçük düşüren
  الهون هوان الشيء الحقير؛ الهين الذي لا كرامة له؛ أهنت فلانا وتهاونت به واستهنت به (ayn)؛ الهون بالضم: الهوان؛ أهانه: استخف به؛ الهوان والمهانة؛ ذل وضعف؛ استهان به وتهاون به: استحقره (sihah)؛ الهوان من جهة متسلط مستخف به؛ عذاب الهون؛ عذاب مهين؛ من يهن الله (mufradat)؛ الهون: الهوان (maqayis)
- **B004** içinde ya da kendisiyle dövme yapılan araç — içinde ya da kendisiyle dövme yapılan araç
  الهاون: الذي يدق فيه، معرب، وكان أصله هاوون (sihah)؛ الهاوون: فاعول من الهون، ولا يقال هارون (mufradat)؛ الهاوون للذي يدق به عربي صحيح كأنه فاعول من الهون (maqayis)

## ECHO م ه ن (root_001453): for 41:17 ٱلْهُونِ: withheld observed target; not identity

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

## ECHO و ه ن (root_001687): for 41:17 ٱلْهُونِ: withheld observed target; not identity

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

## ك س ب (root_001296): 41:17 يَكْسِبُونَ

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

## ن ج و (root_001476): 41:18 وَنَجَّيْنَا

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

## و ق ي (root_001677): 41:18 يَتَّقُونَ

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

## ح ش ر (root_000324): 41:19 يُحْشَرُ

- **B001** topluluğu sevk ederek toplama — topluluğu sevk ederek toplama · toplayıp bir hedefe sevk etmek · toplanma yeri · insanları toplayıp önden götüren · bütün yaratılmışların toplanıp yeniden diriltildiği gün · kadınlar savaşa çıkarılmaz
  السوق والبعث والانبعاث، والحشر الجمع مع سوق، والمحشر، والحاشر يحشر الناس على قدميه (maqayis)؛ الحشر حشر يوم القيامة، والمحشر المجمع الذي يحشر إليه القوم (ayn;tahdhib)؛ حشرتهم إذا جمعتهم، والمحشر مجتمعهم (jamhara)؛ جمعتهم ومنه يوم الحشر، والمحشر موضع الحشر، والحاشر اسم من أسماء النبي (sihah)؛ إخراج الجماعة عن مقرهم وإزعاجهم عنه إلى الحرب ونحوها، ولا يقال الحشر إلا في الجماعة (mufradat)
- **B002** çetin yılın insanları kentlere sürüp malı tüketmesi [kalıp] — çetin yıl onları kentlere sürdü · çetin yıl malı tüketti
  حشرت مال بني فلان السنة كأنها جمعته ذهبت به وأتت عليه (maqayis)؛ حشرتهم السنة تضمهم من النواحي إلى الأمصار (ayn;tahdhib)؛ حشرتهم السنة إذا أصابهم الضر حتى يهبطوا الأمصار (jamhara)؛ حشرت السنة مال فلان أي أهلكته (sihah)؛ حشرت السنة مال بني فلان أي أزالته عنهم (mufradat)
- **B003** hayvanların ölmesi — yaban hayvanlarının ölmesi
  قيل هو الموت (ayn)؛ حشرها موتها (sihah;tahdhib)
- **B004** küçük kara hayvanları — küçük kara hayvanı · küçük kara hayvanları · karada yaşayan küçük hayvanlar
  حشرات الأرض دوابها الصغار كاليرابيع والضباب وما أشبهها (maqayis)؛ الحشرة ما كان من صغار دواب الأرض مثل اليرابيع والقنافذ والضباب ونحوها (ayn;tahdhib)؛ حشرات الأرض دوابها الصغار واحدتها حشرة (jamhara)؛ الحشرة واحدة الحشرات وهي صغار دواب الأرض (sihah)
- **B005** sıkı yapılılık ya da iri karınlılık — sıkı yapılı veya iri karınlı · sıkı yapılı veya yanları kabarık · cinsel organı ve karnı iri olmak
  الحشور من الرجال العظيم الخلق أو البطن (maqayis)؛ الحشور كل ملزز الخلق شديدة (ayn)؛ دابة حشورة إذا كان ملزز الخلق شديده، والعظيم البطن من الرجال حشور (jamhara)؛ الحشور المنتفخ الجنبين، فرس حشور والأنثى حشورة (sihah)؛ حشر فلان في ذكره وفي بطنه إذا كانا ضخمين، والحشور من الدواب كل ملزز الخلق شديده ومن الرجال العظيم البطن (tahdhib)
- **B006** ince, sivri ya da hafif olma — ince, küçük ve sivri kulak · ince ve sivri kulak · ince ok tüyleri · ince sivriltilmiş mızrak ucu · hafif ok · mızrak ucunu inceltip sivriltmek · hafif ve çevik adam · kulakları yayvan ve sivri adam
  أذن حشرة مجتمعة الخلق، والحشر من القذذ ما لطف، وسنان حشر أي دقيق، وقد حشرته، والرجل الخفيف حشر (maqayis)؛ الحشر من الآذان ومن قذذ السهام ما لطف، وحشرت السنان أي رققته وألطفته (ayn;tahdhib)؛ سهم حشر خفيف، وأذن حشرة مؤللة أي دقيقة (jamhara)؛ أذن حشر أي لطيفة، والحشر من القذذ ما لطف، وسنان حشر دقيق، وقد حشرته، سهم حشر (sihah)؛ رجل حشر الأذنين أي في أذنيه انتشار وحدة (mufradat)
- **B007** taneye bitişik iç kabuk — taneye bitişik iç kabuk · taneye bitişik iç kabuklar
  الحبة عليها قشرتان، فالتي تلي الحبة الحشرة والجميع الحشر، والتي فوق الحشرة القصرة (tahdhib)
- **B008** hasat sonrası tarlada kalan bitki örtüsü — hasat sonrası tarlada kalan ve otlatılan bitki örtüsü
  المحشرة في لغة أهل اليمن ما بقي في الأرض وما فيها من نبات بعدما يحصد الزرع، فربما ظهر من تحته نبات أخضر، أرسلوا دوابهم في المحشرة (tahdhib)

## ع د و (root_000993): 41:19 أَعْدَآءُ, 41:28 أَعْدَآءِ, 41:34 عَدَٰوَةٌ

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

## ن و ر (root_001564): 41:19 ٱلنَّارِ, 41:24 فَٱلنَّارُ, 41:28 ٱلنَّارُ, 41:40 ٱلنَّارِ

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

## و ز ع (root_001644): 41:19 يُوزَعُونَ

- **B001** alıkoyup düzen içinde tutma — onu o işten alıkoydu · kendini tuttu ve vazgeçti · öndekiler arkadakilere yetişecek biçimde tutuluyor · ordunun önünü arkasına yetişecek biçimde tuttum · dizginleyen ve düzen sağlayan görevli ya da otorite · dizginleyici görevliler
  وزعته عن الأمر: كففته (maqayis)؛ الوزع كف النفس عن هواها (ayn)؛ وزعته أزعه وزعا: كففته (sihah)؛ وزعته عن كذا: كففته عنه (mufradat)؛ فهم يوزعون أي يحبس أولهم على آخرهم (maqayis)؛ وزعت الجيش إذا حبست أولهم على آخرهم (sihah)؛ حبس أولهم على آخرهم (mufradat)؛ الوازع ... سلطان يكفهم (sihah)
- **B002** içine güçlü bir yöneliş yerleştirme veya ona kapılma — Tanrı onun içine şükretme isteği doğurdu · bir şeye tutkuyla bağlandı · onu o şeye düşkün etti · ona tutkuyla bağlanmış · Tanrı'dan şükretme isteğini içime doğurmasını diledim · Bana verdiğin iyilikler için şükretme isteğini içime doğur · bir şeye tutkuyla bağlanma · bir şeye çok düşkün adam
  اوزع الله فلانا الشكر: ألهمه إياه؛ من أوزع بالشيء إذا أولع به (maqayis)؛ أوزعته بالشئ: أغريته به؛ استوزعت الله شكره فأوزعني أي استلهمته فألهمني (sihah)؛ أوزع الله فلانا إذا ألهمه الشكر؛ من أوزع بالشيء إذا أولع به (mufradat)
- **B003** paylara ayırıp dağıtma — bölme ve dağıtma · onu kendi aralarında paylaştılar
  التوزيع: القسمة والتفريق؛ توزعوه فيما بينهم أي تقسموه
- **B004** insan toplulukları ve bir kabile kolu adı — orada insan toplulukları var · belirli bir kabile kolunun adı
  بها أوزاع من الناس أي جماعات (maqayis;sihah)؛ الاوزاع: بطن من همدان (sihah)
- **B005** dişi devenin çiftleşme sonrası idrarını kesik kesik fırlatması [kalıp] — dişi deve çiftleşmeden sonra idrarını kesik kesik fırlattı
  أوزعت الناقة ببولها إذا رمت به رميا وقطعته؛ ولا يكون ذلك إلا إذا ضربها الفحل
- **B006** güçlü ve dayanıklı mizaç — güçlü ve dayanıklı mizaçlı kimse
  المتزع: الشديد النفس

## ش ه د (root_000822): 41:20 شَهِدَ, 41:21 شَهِدتُّمْ, 41:22 يَشْهَدَ, 41:47 شَهِيدٍ, 41:53 شَهِيدٌ

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

## ب ص ر (root_000121): 41:20 وَأَبْصَٰرُهُمْ, 41:22 أَبْصَٰرُكُمْ, 41:40 بَصِيرٌ

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

## ج ل د (root_000253): 41:20 وَجُلُودُهُم, 41:21 لِجُلُودِهِمْ, 41:22 جُلُودُكُمْ

- **B001** gövdeyi örten deri — hayvan gövdesini örten deri · tek bir deri parçası; göz derisi · gövdeler; örtmeceyle cinsel organlar · gövde, beden ve organlar
  الجلد غشاء جسد الحيوان ويقال جلدة العين (ayn;tahdhib)؛ الجلد معروف وهو أقوى وأصلب مما تحته من اللحم (maqayis)؛ الجلد قشر البدن وجمعه جلود (mufradat)؛ الجلد واحد الجلود والجلدة أخص منه (sihah)؛ أجلاد الرجل جسمه وكذلك تجاليده (jamhara;sihah;tahdhib;maqayis)؛ يفسر لفروجهم فكني بالجلود عنها (ayn;tahdhib)؛ الجلود عبارة عن الأبدان (mufradat)
- **B002** güçlü sertlik ve dayanıklılık — sertlik, güç ve dayanıklılık · güçlü, sert ve dayanıklı adam · işe ve yolculuğa dayanıklı güçlü deve · darbeye ürkmeyen dayanıklı at · sert ve sıkı hurma
  أصل واحد وهو يدل على قوة وصلابة (maqayis)؛ رجل جلد جليد وقد جلد جلادة (ayn)؛ الجلد الشديد رجل جلد بين الجلادة والجلد (jamhara)؛ الجلد الصلابة والجلادة؛ رجل جلد وجليد بين الجلد والجلادة والجلودة (sihah)؛ ورجل جلد وجليد بين الجلد والجلادة (tahdhib)؛ فرس مجلد إذا كان لا يجزع من الضرب (jamhara;sihah;maqayis)؛ ناقة جلدة وهي القوية على العمل والسير (ayn;tahdhib)؛ تمرة جلدة صلبة مكتنزة (tahdhib)
- **B003** sert zemin — sert, kalın veya düz zemin
  الجلد ما صلب من الأرض واستوى متنه (ayn)؛ أرض جلد أي صلبة شديدة؛ الجلد الأرض الصلبة (jamhara)؛ الجلد أيضا الأرض الصلبة؛ وكذلك الأجلد (sihah)؛ الجلد الغليظ من الأرض؛ أرض جلدة ومكان جلد (tahdhib)؛ الجلد الأرض الغليظة الصلبة (maqayis)
- **B004** vurmak, dövüşmek ve yere sermek — kamçıyla, ceza olarak ya da kılıçla vurmak · kılıçlarla vuruşma ve dövüşme · birini yere çalıp devirmek
  جلده بالسوط جلدا أي ضرب جلده (ayn)؛ جلده الحد جلدا أي ضربه وأصاب جلده (sihah)؛ جلدته بالسيف جلدا إذا ضربت جلده (tahdhib)؛ الجلاد بالسيوف الضراب (ayn)؛ وجالدناهم بالسيوف جلادا أي ضاربناهم (tahdhib)؛ المجالدة المباطلة وتجالد القوم بالسيوف واجتلدوا (sihah)؛ جلدت به الأرض أي صرعته (ayn;tahdhib)
- **B005** hayvan derisini yüzme ve kullanma — devenin derisini yüzmek · başka yavruya giydirilen veya doldurulan yüzülmüş yavru derisi · yas tutan kadının yüzüne vurduğu deri parçası
  تجليد الجزور مثل سلخ الشاة (sihah)؛ جلد الرجل جزوره إذا نزع عنها جلدها ولا يقال سلخ جزوره (maqayis)؛ جلدت الجمل لا تقول العرب غير ذلك (tahdhib)؛ الجلد أن يسلخ جلد البعير أو غيره فيلبسه غيره من الدواب (ayn;tahdhib;maqayis)؛ الجلد جلد حوار يسلخ فيلبس حوارا آخر لتشمه أم المسلوخ فترأمه (jamhara;sihah)؛ أن يسلخ جلد الحوار ثم يحشى ثماما أو غيره من الشجر (tahdhib;maqayis)؛ المجلد قطعة من جلد تكون في يد النائحة (jamhara;sihah)؛ المجالد مثل المآلي واحدها مجلد وهي من جلود (ayn)
- **B006** yavrusuz, sütsüz ya da az sütlü iri develer — yavruları yanında olmayan, sütü kalmamış iri develer · başka bir deve sınıfından daha az süt veren develer · sütü ve yavrusu olmayan koyun
  الجلد الكبار من النوق التي لا أولاد لها ولا ألبان (sihah)؛ الجلد من الإبل الكبار التي لا صغار فيها (tahdhib)؛ التي لا أولاد معها فتصبر على الحر والبرد (tahdhib)؛ الجلد من الإبل التي لا ألبان لها وقد ولى عنها أولادها (tahdhib)؛ الجلد من البعران الكبار لا صغار فيها (maqayis)؛ الجلاد من الإبل تكون أقل لبنا من الخور الواحدة جلدة (maqayis)؛ شاة جلدة إذا لم يكن لها لبن ولا ولد (sihah)
- **B007** donmuş su, kırağı ve koyu pıhtılı süt — buz; yerde donmuş çiy veya kırağı · yeri veya bitkiyi kırağı vurmak · koyu ve pıhtılaşmış süt
  الجليد ما جمد من الماء وما وقع على الأرض من الصقيع فجمد (ayn)؛ الجليد ما يسقط من السماء من الندى فيجمد على الأرض وهو السقيط والضريب (jamhara;sihah)؛ جلدت الأرض من الجليد وأجلد الناس وجلد البقل (tahdhib)؛ العجلد اللبن الخاثر وهذا مما زيدت فيه العين كأنه شبه بالجلد في كثافته (maqayis-alijlad)

## ن ط ق (root_001519): 41:21 أَنطَقَنَا, 41:21 أَنطَقَ

- **B001** konuşma ve anlaşılır sesli söz üretme — konuşmak; anlaşılır ses çıkarmak · konuşma; dinleyenin anladığı sesli söz · konuşturmak · onunla konuşmak, ona söz yöneltmek · konuşmaya çağırmak ya da onunla konuşmak · konuşan; ses çıkaran canlı · çok ve etkili konuşan · konuşma, söz söyleme · iyi söyleme, bel bağı bağlama ya da atı yanda götürme arasında yoruma açık söz
  المنطق ونطق ينطق نطقا (maqayis)؛ نطق الناطق ينطق نطقا وهو منطيق بليغ (ayn;tahdhib)؛ المنطق الكلام وقد نطق نطقا (sihah)؛ الأصوات المقطعة التي يظهرها اللسان (mufradat)؛ الناطق الحيوان والصامت ما سواه (sihah;tahdhib)
- **B002** konuşurcasına anlam bildirme [kalıp] — anlamını açıkça bildiren yazı · bir şeyden anlaşılan bildiri · anlamı kavranan kuş sesleri · sözsüzce bildiren göstergeler ve ders veren olaylar
  كلام أو ما أشبهه (maqayis)؛ الكتاب الناطق البين (ayn;tahdhib)؛ كلام كل شيء منطقه (ayn;tahdhib)؛ الدلائل المخبرة والعبر الواعظة (mufradat)؛ علمنا منطق الطير (maqayis;mufradat)
- **B003** bele bağlanan kuşak ve onu bağlama — bele bağlanan eteklik ya da kuşak · bele sarılan bağ · bele takılan özel kuşak · bel bağı takmak · kuşağını beline bağlamak · bir başkasının beline kuşak bağlamak · iki bel bağıyla anılan kadın unvanı · kalçasını iri göstermek için dolgulu kuşak bağlayan kadın · iyi söyleme, bel bağı bağlama ya da atı yanda götürme arasında yoruma açık söz
  النطاق إزار فيه تكة (maqayis)؛ المنطق كل ما شددت به وسطك والمنطقة اسم خاص (ayn;tahdhib)؛ النطاق شقة تلبسها المرأة وتشد وسطها (sihah)؛ النطاق شبه إزار فيه تكة (tahdhib)؛ المنطق والمنطقة ما يشد به الوسط (mufradat)؛ ذات النطاقين (tahdhib)؛ منطيق تأتزر بحشية تعظم بها عجيزتها (tahdhib)
- **B004** kuşak hizasına benzetilen yan veya orta seviye — belin yan bölümü, böğür · beli hizasında kızıl işaret bulunan koyun · suyun ağacın ya da tepenin yarısına ulaşması · bulutların doruğuna erişemediği yüksek dağ · bir tepenin adı
  الخاصرة الناطقة لأنها بموضع النطاق (maqayis)؛ الشاة التي يعلم عليها في موضع النطاق (maqayis)؛ إذا بلغ الماء النصف من الشجر يقال نطقها (ayn)؛ جبل أشم منطق لأن السحاب لا يبلغ أعلاه (sihah)؛ بلغ الماء النصف من الشجرة والأكمة يقال نطقها (tahdhib)
- **B005** atı binmeden yanında götürme — atı binmeden yanında götürmek ya da çekmek · iyi söyleme, bel bağı bağlama ya da atı yanda götürme arasında yoruma açık söz
  جاء فلان منتطقا فرسه إذا جانبه ولم يركبه (maqayis;sihah)؛ انتطق فلان فرسه إذا قاده (tahdhib)؛ منتطقا جانبا أي قائدا فرسا لم يركبه (mufradat)
- **B006** baba soyunun çokluğundan güç alma [kalıp] — baba tarafından akrabaları çok olanın onlarla güçlendiğini anlatan kalıplaşmış söz
  من يطل ذيل أبيه ينتطق به (maqayis;sihah;mufradat)؛ من كثر بنو أبيه أعانوه (maqayis)؛ من كثر بنو أبيه يتقوى بهم (sihah)

## ء و ل (root_000067): 41:21 أَوَّلَ

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

## و ل ي (root_001684): 41:31 أَوْلِيَآؤُكُمْ, 41:34 وَلِىٌّ (also echo for 41:21 أَوَّلَ)

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

## م ر ر (root_001414): 41:21 مَرَّةٍ

- **B001** geçip gitme ve yolunu izleyerek sürme — geçip gitmek · sürmek, yolunda ilerlemek · birini köprünün üzerinden geçirmek
  مر الشيء يمر إذا مضى (maqayis)؛ المر المرور (ayn)؛ مر عليه وبه يمر مرا ومرورا ذهب واستمر مثله (sihah)؛ أمررت فلانا على الجسر إذا سلكت به عليه (tahdhib)؛ المرور المضي والاجتياز بالشيء (mufradat)
- **B002** kerelik gerçekleşme ve tekrarı — bir kez, bir kerelik gerçekleşme · defalarca, tekrar tekrar
  لقيته مرة ومرتين عبارة عن زمان قد مر (maqayis)؛ المر المرة (ayn)؛ جئتك مرا أو مرين تريد مرة أو مرتين (jamhara)؛ يصنع ذلك الأمر ذات المرار (sihah)؛ يصنعه مرارا ويدعه مرارا (tahdhib)؛ مرة ومرتين وذلك لجزء من الزمان (mufradat)
- **B003** acı tat ve acılaşma — acı, tatlı olmayan · acı tat, acılık · acılaşmak, acı duruma gelmek · çok acı bir bitki · acılı katık
  خلاف الحلاوة والطيب (maqayis)؛ المر نقيض الحلو (ayn)؛ المر ضد الحلو (jamhara)؛ المرارة ضد الحلاوة وشيء مر (sihah)؛ مر هذا الطعام في فمي أي صار مرا (tahdhib)؛ مر الشيء وأمر إذا صار مرا (mufradat)
- **B004** ağır sıkıntılar ve yıkımlar — ağır sıkıntılar, büyük belalar · kaygı ve hastalık
  لقيت منه الأمرين أي شدائد غير طيبة (maqayis)؛ لقيت منه الأمرين أي الداهية أو الأمر العظيم (ayn)؛ الأمرين الفقر والهرم (sihah)؛ لقيت منه الأمرين والبرحين والأقورين أي لقيت منه الشر (tahdhib)
- **B005** ipi sıkıca burma ve sıkı burulmuş ip — ipi sıkıca burmak · sıkı burulmuş ince ve uzun ip · ip, sıkıca burulmuş bağ · ipin burulmuş bir kolu
  أمررت الحبل فتلته وهو ممر والمر شدة الفتل (maqayis)؛ المرير الحبل المفتول وقد أمررته إمرارا (ayn)؛ المرة القوة من قوى الحبل والجمع مرر (jamhara)؛ المرير من الحبال ما لطف وطال واشتد فتله (sihah)؛ أصل المرة إحكام الفتل (tahdhib)؛ أمررت الحبل إذا فتلته والمرير والممر المفتول (mufradat)
- **B006** sağlam güç, kararlılık ve özsaygı — güçlü ve sağlam bedenli · güç ve akıl sağlamlığı · kararlılık ve özsaygı · güçlü, dirençli · kararlılığı pekişti
  المريرة القوة منه والمريرة عزة النفس (maqayis)؛ ذو مرة أي قوي صحيح البدن (ayn)؛ رجل ذو مرة إذا كان سليم الأعضاء صحيحها (jamhara)؛ المرة القوة وشدة العقل ورجل مرير أي قوي ذو مرة (sihah)؛ المرة القوة (tahdhib)؛ ذو مرة كأنه محكم الفتل (mufradat)
- **B007** eski tıptaki acı beden sıvısı ve öd kesesi — eski tıptaki acı beden sıvısı veya buna bağlı hastalık · öd kesesi · acı beden sıvısı baskın sayılan kişi
  المرة مزاج من أمزجة الجسد وهو داء (ayn)؛ المرة أحد أمشاج البدن (jamhara)؛ المرة إحدى الطبائع الأربع والممرور الذي غلبت عليه المرة (sihah)؛ المرارة لكل حيوان والمرة مزاج من أمزجة الجسد (tahdhib)
- **B008** biçime bağlı adlandırmalar — dışkının toplandığı bağırsaklar · iki acı huy
  الأمر المصارين يجتمع فيها الفرث (maqayis)؛ الأمر المصارين يجتمع فيها الفرث (sihah)؛ الأمر المصارين يجتمع فيها الفرث (tahdhib)؛ هما المريان الخصلتان المرتان (tahdhib)

## ر ج ع (root_000544): 41:21 تُرْجَعُونَ, 41:50 رُّجِعْتُ

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

## س ت ر (root_000674): 41:22 تَسْتَتِرُونَ

- **B001** örtme, perdeleme ve gizlenme — bir şeyi örtmek ve görünmez kılmak · örtme, kapatma · örtü veya perde · arkasına saklanılan örtü ya da engel · örten perde · güneşi veya başka bir şeyi kesen perde · bir kadının önüne indirilen perde · örtü · gizlenmek, gözden kaybolmak · örtünmek · kalın perde veya örten perde · belirli kutsal yapıyı örten kumaşlar
  كلمة تدل على الغطاء (maqayis)؛ سترت الشيء سترا (maqayis;ayn;jamhara;sihah;tahdhib)؛ إذا غطيته (jamhara;sihah)؛ تغطية الشيء (mufradat)؛ السترة ما استترت به (maqayis;ayn;sihah;tahdhib;mufradat)؛ الستار والستارة (maqayis;ayn;jamhara;sihah;tahdhib)؛ الاستتار الاختفاء (mufradat)
- **B002** utanma duygusu ve cinsel ölçülülük — utanma duygusu · onda ne utanma duygusu ne de akıl var · utangaç ve çekingen kadın · gözlerden uzak tutulan genç kadın · cinsel ilişkilerde kendini sakınan · cinsel ilişkilerde kendini sakınan
  امرأة ستيرة ذات ستارة (ayn;tahdhib)؛ امرأة ستيرة حيية وخفرة (jamhara)؛ جارية مسترة أي مخدرة (sihah)؛ رجل مستور وستير أي عفيف (sihah)؛ الستر الحياء (ayn;tahdhib)
- **B003** bir yer ya da dağ adı ile iki vadinin adı — bir yerin ya da bir dağın özel adı · iki vadinin ortak özel adı
  الستار موضع (ayn;jamhara)؛ الستار فيذبل فهما جبلان (sihah)؛ الستاران واديان (tahdhib)
- **B004** yalıtık adlandırmalar — 
  العرب تسمى الأربعة الإستار (maqayis)؛ الإستار في العدد أربعة (sihah)؛ الإستار أيضا وزن أربعة مثاقيل ونصف (sihah)؛ لكل أربعة إستار (tahdhib)؛ هذا الوزن الذي يقال له الإستار معرب (tahdhib)
- **B005** iki kişi arasında elçilik yapan aracı [kalıp] — iki kişi arasında elçilik yapan aracı
  فلان بيني وبينك سترة إذا كان سفيرا بينك وبينه (tahdhib)

## ظ ن ن (root_000969): 41:22 ظَنَنتُمْ, 41:23 ظَنُّكُمُ, 41:23 ظَنَنتُم, 41:48 وَظَنُّوا۟, 41:50 أَظُنُّ

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

## ر د ي (root_000558): 41:23 أَرْدَىٰكُمْ

- **B001** taş atma ve taş kırma taşı — ona taş attı · taşı bir kaya ya da kazmayla vurarak kırdı · atmak veya başka taşları kırmak için kullanılan taş · atılan taş · kaya · kayalar · bir topluluk adına taş atarak karşı koydu
  رديته بالحجارة أرديه رميته (maqayis); المردى حجر يرمى به (sihah); المرداة الحجر الذي يرمى به (tahdhib); المرداة حجر تكسر بها الحجارة فترديها (mufradat)
- **B002** atın özel hızlı gidişi, insanın tek ayaklı sekmesi ve karganın sekmesi — at koşu ile sert yürüyüş arasında hızla gitti · eşeğin bağlandığı yerle yuvarlandığı yer arasındaki koşusu · çocuk bir ayağını kaldırıp ötekiyle sıçradı · genç kızlar oyun oynarken tek ayak üzerinde sektiler · karga sekerek yürüdü · deve ve filin ağır, sert basan bacakları
  ردى الفرس أسرع (maqayis); ردى الفرس بين العدو والمشى الشديد (sihah); الجواري يردين إذا رفعت إحداهن رجلها ومشت على رجل (tahdhib); الغراب يردي إذا حجل (tahdhib)
- **B003** düşerek ya da başka yolla ölme, yok olma veya yok etme — ölüm ve yok oluş · öldü veya yok oldu · onu öldürdü veya yok etti · uçuruma yuvarlanma ve ölüm tehlikesine girme · kuyuya düştü · dağdan aşağı yuvarlandı · nereye gittiğini bilmiyorum · kendini ölüm tehlikelerine atan kişi · kötü ve tiksindirici şey
  الردى وهو الهلاك (maqayis); أرداه الله أهلكه (maqayis); ردى في البئر وتردى إذا سقط في بئر (sihah); التردي هو التهور في مهواة (tahdhib); الردى الهلاك والتردي التعرض للهلاك (mufradat)
- **B004** omuz giysisi, onu giyme ve örten ya da bezeyen şey — omuzlara alınan dış giysi · omuz giysisini giydi · omuz giysisini güzel taşıma biçimi · iyiliği bol ve eli açık · borcu veya yükümlülüğü az · boyna bağlı bir yükümlülük olarak borç · askılarıyla omuzda taşınan kılıç · çapraz takılan kuşak · genç kız çapraz kuşak taktı · gençliğin güzelliği, canlılığı ve esenliği
  الرداء الذي يلبس (maqayis); تردى وارتدى بمعنى أي لبس الرداء (sihah); يسمى الدين رداء (tahdhib); كل ما زينك فهو رداؤك (tahdhib)
- **B005** belirli bir ölçünün üstüne ekleme — ellinin üzerine çıktı · ellinin üstüne ekledi · artış veya eklenen pay · verdiğin ek pay · sözüne yaptığın ek
  أردى على الخمسين إذا زاد عليها (maqayis); رديت على الخمسين وأرديت أي زدت (sihah); الردى الزيادة (tahdhib); ردى عطائك أي زيادتك في العطية (tahdhib)
- **B006** yumuşakça razı etmeye çalışma ve idare etme — adamı yumuşakça razı etmeye çalıştı veya idare etti · gemin ağızlık parçası için yumuşakça pazarlık edilir
  يرادى على فأس اللجام (maqayis;sihah;tahdhib); فليس هذا من الباب لأن هذا مقلوب ومعناه يراود (maqayis); راداه بمعنى داراه (sihah); راديت الرجل وداجيته وداليته وفانيته بمعنى واحد (tahdhib)

## خ س ر (root_000409): 41:23 ٱلْخَٰسِرِينَ, 41:25 خَٰسِرِينَ

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

## ص ب ر (root_000840): 41:24 يَصْبِرُوا۟, 41:35 صَبَرُوا۟

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

## ث و ي (root_000211): 41:24 مَثْوًى

- **B001** bir yere yerleşip uzun süre kalma — bir yerde yerleşip kalmak · yerleşip uzun süre kalma · bir yerde kalıp yaşayan kişi · bir yerde yerleşip kalmak · öldürülüp yerde kalmış olmak · iki kutsal bölgede komşu olarak yaşama · savaşta dayanıklı olan ya da kapatılıp tutulan kişi · yerleşip kalma
  ثوى يثوي ثويا إذا أقام بالمكان والاسم الثواء (jamhara)؛ ثوى بالمكان أقام به وثويت البصرة وأثويت بالمكان لغة في ثويت (sihah)؛ الثواء طول المقام ويقال للمقتول قد ثوى والغريب إذا أقام ببلدة فهو ثاو والثوي المجاورة في الحرمين والثوي الصبور في المغازي المحجر وهو المحبوس (tahdhib)؛ الثواء الإقامة مع الاستقرار (mufradat)؛ كلمة واحدة صحيحة تدل على الإقامة ويقال ثوى يثوي فهو ثاو ويقال أثوى أيضا (maqayis)
- **B002** kalınan yer ve konuk ağırlama düzeni — kalınan yer; ev · kalınan yerler; evler · birini yanına yerleştirip ağırlamak · birini kalması için yerleştirmek · konuğu ağırlayan erkek ev sahibi · konuğu ağırlayan kadın ev sahibi · kimin evine konuk oldun? · konuk · ev içindeki ayrı bölüm; konuğa ayrılmış yer · bir yer adı
  المثوى الموضع الذي يثوي فيه الرجل وأم مثوى الرجل صاحبة منزله والثوية اسم موضع (jamhara)؛ الثوى الضيف وأبو مثوى الرجل صاحب منزله والثوية اسم موضع (sihah)؛ المثوى الموضع الذي يقام به ويقال أنزلني فلان وأثواني ثواء حسنا ورب البيت أبو مثواه وربة البيت أم مثواه والثوي بيت في جوف بيت والبيت المهيأ للضيف والثوي الضيف نفسه ومثوى الرجل منزله (tahdhib)؛ من أم مثواك كناية عمن نزل به ضيف (mufradat)؛ الثوية مكان وأم مثوى الرجل صاحبة منزله (maqayis)
- **B003** sürü barınağı, çoban gölgeliği veya taş dönüş imi — koyun barınağı · koyun ya da deve barınağı; çobanın dallardan yaptığı gölgelik · çobanın gece dönüşü için yükselttiği taş imi
  الثاية ظلة يتخذها الراعي من أغصان الشجر (jamhara)؛ الثوية مأوى الغنم وكذلك الثاية والثاية أيضا حجارة ترفع فتكون علما بالليل للراعي إذا رجع (sihah)؛ الثوية مأوى الغنم (mufradat)؛ الثوية والثاية مأوى الغنم والثاية أيضا حجارة ترفع للراعي يرجع إليها ليلا تكون علما له (maqayis)
- **B004** çalkalama kabı altlığı ve ev eşyası — süt tulumunu çalkalarken altına serilen koruyucu bez · ev eşyası
  الثَّوَة مثل الصوة خرقة تطرح تحت الوطب إذا مخض تقيه عن الأرض (jamhara)؛ الثوى قماش البيت واحدتها ثَوَة والخرقة التي تبل ويجعل عليها السقاء إذا مخض لئلا ينقطع الثَّوَة (tahdhib)

## ع ت ب (root_000977): 41:24 يَسْتَعْتِبُوا۟, 41:24 ٱلْمُعْتَبِينَ

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

## ق ي ض (root_001275): 41:25 وَقَيَّضْنَا

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

## ق ر ن (root_001221): 41:25 قُرَنَآءَ

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

## ء م م (root_000053): 41:25 أُمَمٍ

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

## خ ل و (root_000436): 41:25 خَلَتْ

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

## ق ب ل (root_001198): 41:25 قَبْلِهِم, 41:43 قَبْلِكَ, 41:48 قَبْلُ

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

## ج ن ن (root_000266): 41:25 ٱلْجِنِّ, 41:29 ٱلْجِنِّ, 41:30 بِٱلْجَنَّةِ

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

## ء ن س (root_000059): 41:25 وَٱلْإِنسِ, 41:29 وَٱلْإِنسِ, 41:49 ٱلْإِنسَٰنُ, 41:51 ٱلْإِنسَٰنِ

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

## ل غ و (root_001361): 41:26 وَٱلْغَوْا۟

- **B001** dikkate alınmayan veya geçersiz kılınan şey — dikkate alınmayan, hesaba katılmayan şey · içten bağlanılmamış, bağlayıcı olmayan yemin · kan bedelinin hesabına katılmayan deve yavruları · bir şeyi geçersiz kılmak veya bir sözü boş ve gereksiz saymak · onu sayıdan çıkarmak ve hesaba katmamak · içten bağlanmadan yemin etmek · ciddi ve amaçlı olmayan koşu
  اللغو ما لا يعتد به من أولاد الإبل في الدية (maqayis;sihah;mufradat)؛ لغو الأيمان ما لم تعقدوه بقلوبكم وما لا عقد عليه (maqayis;sihah;tahdhib;mufradat)؛ ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب (ayn;tahdhib)؛ ألغيت الشيء: أبطلته وألغاه من العدد: ألقاه منه (sihah;tahdhib)؛ فرسك لملاغي الجري إذا كان جريه غير جري جد (tahdhib)
- **B002** batıl veya çirkin söz — batıl veya çirkin söz · çirkin ya da açık saçık söz · onu batıl veya çirkin söze yöneltmek · haftalık toplu ibadet konuşması sırasında söz söylemek
  لغا يلغو لغوا يعني اختلاط الكلام في الباطل (ayn;tahdhib)؛ لغا يلغو لغوا أي قال باطلا (sihah)؛ كل كلام قبيح لغوا (mufradat)؛ لاغية كلمة قبيحة أو فاحشة (ayn;tahdhib)؛ قال قتادة باطلا ومأثما وقال مجاهد شتما (tahdhib)؛ استلغوني أرادوني على اللغو (tahdhib)
- **B003** ses ve gürültü — konuşma sesini yükselterek şaşırtmak · ses ve gürültü · köpek havlaması · kuş sesleri
  والغوا فيه يعني رفع الصوت بالكلام ليغلطوا المسلمين (ayn)؛ اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا (sihah)؛ لغوى الطير أصواتها (tahdhib)؛ اللغا صوت العصافير ونحوها من الطيور (mufradat)
- **B004** bir şeye düşkün olup onunla sürekli meşgul olma — bir şeye düşkün olmak ve onunla sürekli meşgul olmak · bir içeceği çok tüketmek · bir topluluğun dili veya aynı anlamı farklı sözlerle anlatma biçimi · kendilerine sormadan konuşmalarını dinleyip dil kullanımlarını öğrenmek
  لغى بالأمر إذا لهج به ويقال إن اشتقاق اللغة منه (maqayis)؛ اللغة واللغات اختلاف الكلام في معنى واحد (ayn;tahdhib)؛ لغي به أي لهج به ولغي بالشراب أكثر منه واللغة أصلها لغى أو لغو (sihah)؛ لغي فلان بفلان إذا أولع به ولغي فلان بالماء إذا أكثر منه واستلغهم اسمع من لغاتهم (tahdhib)؛ لغي بكذا أي لهج به ومنه قيل للكلام الذي يلهج به فرقة فرقة لغة (mufradat)
- **B005** doğru olandan sapmak — doğru olandan sapmak
  لغا فلان عن الصواب أي مال عنه (tahdhib)
- **B006** umduğunu bulamama veya birini başarısızlığa uğratma — haftalık toplu ibadet konuşması sırasında konuşup umduğunu bulamamak · onu umduğundan yoksun bırakıp başarısızlığa uğratmak
  من تكلم يوم الجمعة والإمام يخطب فقد لغا أي خاب؛ وألغيته أي خيبته (tahdhib)

## غ ل ب (root_001098): 41:26 تَغْلِبُونَ

- **B001** güçle üstün gelme ve boyun eğdirme — yenmek; üstün gelmek · üstün gelme, yenme · üstünlük kurma, boyun eğdirme · üzerinde egemenlik kurmak; etkisi altına almak · üstün gelmek için çekişmek · üstünlük çekişmesi, mücadele · çok kez üstün gelen · üstünlük için karşılıklı mücadele · üstün gelme, üstünlük kazanma · sürekli yenilen; benzerlerine yenik düşen · üstün olduğuna karar verilen; başkalarından üstün tutulan · çok kez veya çabucak üstün gelen kimse · hastalık yüzünden yenik düşmek · birini başkasına üstün ilan etmek veya üstün kılmak
  أصل صحيح يدل على قوة وقهر وشدة؛ غلب الرجل غلبا وغلبة؛ والغلاب المغالبة؛ والمغلب من الشعراء المغلوب مرارا؛ والمغلب أيضا الذي غلب خصمه أو قرنه (maqayis)؛ غلب يغلب غلبا وغلبة؛ والغلاب النزاع؛ والمغلب الذي يغلبه أقرانه فيما يمارس؛ والمغلب قد يكون المفضل على غيره (ayn)؛ لمن الغلب والغلبة؛ رجل غلبة كثير الغلب؛ غالب الرجل الرجل مغالبة وغلابا؛ المغلبة الاسم من الغلب (jamhara)؛ تغلب على بلد كذا استولى عليه قهرا؛ والمغلب المغلوب مرارا؛ والمغلب أيضا من الشعراء المحكوم له بالغلبة على قرنه (sihah)؛ الغلبة القهر؛ غلب عليه كذا أي استولى (mufradat)
- **B002** kalın boyunlu ve güçlü yapılı olma — kalın boyunlu ve güçlü yapılı · kalın, iri ve güçlü yapılı · kalın ve sık yapılı olanlar · iri, kalın yapılı tepe · güçlü ve sarsılmaz onur · sık ve iç içe geçmiş bahçe · sık ve iç içe geçmiş bahçeler · ot iyice gelişip sıklaşarak birbirine dolandı
  والأغلب الغليظ الرقبة؛ هضبة غلباء وعزة غلباء؛ اغلولب العشب بلغ كل مبلغ (maqayis)؛ والأغلب الغليظ الشديد القصرة وأسد أغلب؛ هضبة غلباء وعزة غلباء؛ اغلولب العشب في الأرض إذا بلغ كل مبلغ (ayn)؛ رجل أغلب بين الغلب إذا كان غليظ العنق والأسد أغلب والأنثى غلباء (jamhara)؛ رجل أغلب بين الغلب إذا كان غليظ الرقبة؛ هضبة غلباء وعزة غلباء؛ حديقة غلباء ملتفة وحدائق غلب؛ اغلولب العشب بلغ والتف (sihah)؛ والأغلب الغليظ الرقبة؛ رجل أغلب وامرأة غلباء وهضبة غلباء؛ حدائق غلبا (mufradat)

## ج ز ي (root_000244): 41:27 وَلَنَجْزِيَنَّهُمْ, 41:28 جَزَآءُ, 41:28 جَزَآءًۢ

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

## ECHO ج ز ز (root_000242): for 41:27 وَلَنَجْزِيَنَّهُمْ, 41:28 جَزَآءُ, 41:28 جَزَآءًۢ: withheld observed target; not identity

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

## س و ء (root_000755): 41:27 أَسْوَأَ, 41:34 ٱلسَّيِّئَةُ, 41:46 أَسَآءَ

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

## د و ر (root_000499): 41:28 دَارُ

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

## خ ل د (root_000429): 41:28 ٱلْخُلْدِ

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

## ض ل ل (root_000913): 41:29 أَضَلَّانَا, 41:48 وَضَلَّ, 41:52 أَضَلُّ

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

## ت ح ت (root_000177): 41:29 تَحْتَ

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ق د م (root_001207): 41:29 أَقْدَامِنَا

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

## س ف ل (root_000715): 41:29 ٱلْأَسْفَلِينَ

- **B001** aşağıda veya altta olma — alt bölüm; aşağı taraf · alt kısım · daha aşağıdaki; alt · altta bulunan · alt taraf; aşağı yön · alttaki; daha aşağıdaki · aşağıda olma; alçalma · aşağıda bulunma · altta bulunma · aşağıya inmek; alçalmak · en aşağıların aşağısı; en alt düzey
  ما كان خلاف العلو والسفول ضد العلو (maqayis)؛ سفل وعلو وسفلى وعليا وسفال وعلاء نقائض (ayn)؛ نقيض العلو والسافل نقيض العالي (sihah)؛ الأسفل نقيض الأعلى والسفل نقيض العلو في البناء والسافلة نقيض العالية في النهر والرمح (tahdhib)؛ السفل ضد العلو وأسفل ضد أعلى (mufradat)
- **B002** toplumsal düşüklük ve değersizlik — alçaklık; bayağılık · aşağılık kimseler; ayak takımı · durumları düşük düzeyde · alçalmak; bayağılaşmak · en aşağı düzey; en düşük durum
  السفلة الدون من الناس وإن أمرهم لفي سفال (maqayis)؛ سفلة وعلية نقائض (ayn)؛ السفالة بالفتح النذالة والسفلة السقاط من الناس (sihah)؛ السفلة نقيض العلية وهم السفلة لأراذل الناس (tahdhib)؛ السفلة من الناس النذل نحو الدون وأمرهم في سفال (mufradat)
- **B003** rüzgâra göre aşağı taraf [kalıp] — rüzgâra göre aşağı taraf; rüzgârın karşı yönü
  قعد بسفالة الريح وعلاوتها والعلاوة من حيث تهب والسفالة ما كان بإزاء ذلك (maqayis)؛ قعدت بسفالة الريح وعلاوتها والعلاوة حيث تهب والسفالة بإزاء ذلك (sihah)؛ كن في علاوة الريح وسفالة الريح فأما علاوتها فأن يكون فوق الصيد وأما سفالتها فأن يكون تحت الصيد (tahdhib)؛ سفالة الريح حيث تمر الريح والعلاوة ضده (mufradat)
- **B004** aşağı yöneltme veya aşağıya yönelme — aşağı yöneltme; aşağı çevirme · aşağıya yönelme; aşağı inme
  التسفيل التصويب والتسفل التصوب (sihah)؛ السفل نقيض العلو في التسفل والتعلي (tahdhib)
- **B005** devenin ayakları [kalıp] — devenin ayakları
  السفلة بكسر الفاء قوائم البعير (sihah)؛ سفلة البعير قوائمه (tahdhib)
- **B006** genç develer veya deve yavruları — genç develer; deve yavruları
  الاسافل صغار الابل (sihah)؛ أسافل الإبل صغارها أي قليل الأولاد (tahdhib)
- **B007** oturma bölgesi ve anüs — oturma bölgesi; anüs
  السافلة المقعدة والدبر (sihah)

## خ و ف (root_000447): 41:30 تَخَافُوا۟

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

## ح ز ن (root_000317): 41:30 تَحْزَنُوا۟

- **B001** sevinç karşıtı ağır üzüntü — ağır üzüntü ve iç sıkıntısı · üzülmek, üzgün duruma gelmek · üzmek, üzüntüye düşürmek · üzmek, üzgün duruma getirmek · üzüntüye uğramış, üzgün · üzüntü veren, üzücü · üzüntüye bürünmek, üzülmek · okurken sesi üzgün bir tona inceltme
  الحزن والحزن لغتان وأصابه حزن شديد (ayn;tahdhib)؛ الحزن والحزن خلاف السرور (sihah)؛ خشونة في النفس لما يحصل فيه من الغم ويضاده الفرح (mufradat)؛ الحزن معروف يقال حزنني الشيء يحزنني وقد قالوا أحزنني (maqayis)؛ صوت محزن وأمر محزن ولا يقال حازن (ayn;tahdhib)؛ يقرأ بالتحزين إذا أرق صوته به (sihah)
- **B002** sert ve engebeli arazi — sert ve engebeli arazi ya da kaba yapılı hayvan · engebeli ve taşlı arazi parçaları · tek bir sert ve engebeli yer; kaba yapılı dişi hayvan · arazinin ya da hayvanın sertliği ve kabalığı · engebeli arazide otlayan deve · huysuz koyun · sert ve engebeli araziye girmek · yüksek, sert ve engebeli arazi
  الحزن من الأرض والدواب ما فيه خشونة (ayn;tahdhib)؛ الحزن ما غلظ من الأرض وفيها حزونة (sihah)؛ الجبال الغلاظ الواحدة حزنة (sihah)؛ أول حزون الأرض قفافها وجبالها وقواقيها وخشنها ورضمها (tahdhib)؛ الحزن وهو ما غلظ من الأرض (maqayis)؛ خشونة في الأرض (mufradat)؛ الحزم من الأرض والأصل حزن والحزم أرفع من الحزن (maqayis-hazm)؛ الحزون الشاة السيئة الخلق (sihah)
- **B003** kaygı duyulan aile ve yakın çevre — kişinin durumları için kaygılandığı aile, ev halkı ve yakınlar · Arapların Arap olmayan topluluklara yüklediği, Arap konukları barındırma, ağırlama ve yol azığı verme yükümlülüğü
  حزانتك أهلك ومن تتحزن له (maqayis)؛ الحزانة عيال الرجل الذي يتحزن بأمرهم (sihah;tahdhib)؛ كيف حشمك وحزانتك أي من تتحزن بأمرهم (tahdhib)؛ تسمى سفنجقانية العرب على العجم حزانة (ayn;tahdhib)

## ECHO ح ز ز (root_000316): for 41:30 تَحْزَنُوا۟: withheld observed target; not identity

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

## و ع د (root_001662): 41:30 تُوعَدُونَ

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

## ECHO ع و م (root_001063): for 41:30 تُوعَدُونَ: withheld observed target; not identity

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

## ش ه و (root_000825): 41:31 تَشْتَهِىٓ

- **B001** istenene yönelme; istek, istenen şey veya isteme gücü — kişinin istediği şeye içten yönelmesi ve onu istemesi · istenen şey · isteme gücü · karşılanmadığında bedenin zarar göreceği gerçek gereksinime dayalı istek · karşılanmadığında bedene zarar vermeyecek yersiz istek · istekler ve istenen şeyler · istemek ve bir şeye içten yönelmek · bir şeyi istemek · istemek · istenir, beğenilir ve hoş · isteği çok güçlü olan erkek · isteği çok güçlü olan kadın · istekle ilgili veya isteği çok güçlü · yemeye karşı çok güçlü istek duyanlar
  الشهوة ورجل شهوان وشيء شهي (maqayis)؛ رجل شهوان وامرأة شهوى وأنا إليه شهوان وشهي يشهى وشها يشهو إذا اشتهى (ayn;tahdhib)؛ الشهوة معروفة وطعام شهي أي مشتهى وشهيت الشيء إذا اشتهيته وهذا شيء يشهى الطعام أي يحمل على اشتهائه (sihah)؛ أصل الشهوة نزوع النفس إلى ما تريده وقد يسمى المشتهى شهوة والقوة التي تشتهي الشيء شهوة (mufradat)
- **B002** art arda istek bildirme; eşten isteme veya eş için sağlama — bir isteğin ardından başka bir istek ileri sürme · kadının istediği şeyi kocasından istemesi · kadının istediği şeyi onun için arayıp sağlamak
  التشهي شهوة بعد شهوة وتشهت المرأة على زوجها فأشهاها أي أطلبها ما تشهت أي طلب لها (ayn)؛ التشهي اقتراح شهوة بعد شهوة وتشهت المرأة على زوجها فأشهاها أي أطلبها شهواتها (tahdhib)
- **B003** içte saklanıp sürdürülerek gizlice yapılan kötü iş isteği [kalıp] — içte saklanıp sürdürülen ve gizlice yapılan kötü işlere yönelik istek
  الشهوة الخفية ليس بمخصوص بشيء واحد ولكنه في كل شيء من المعاصي يضمره صاحبه ويصر عليه (tahdhib)؛ الشهوة الخفية من الفواحش ما لا يحل مما يستخفي به الإنسان (tahdhib)؛ الشهوة الخفية للمعاصي والشهوة لها في قلبه مخفاة وإذا استخفى بها عملها (tahdhib)

## ن ف س (root_001533): 41:31 أَنفُسُكُمْ, 41:46 فَلِنَفْسِهِۦ, 41:53 أَنفُسِهِمْ

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

## ح س ن (root_000323): 41:33 أَحْسَنُ, 41:34 ٱلْحَسَنَةُ, 41:34 أَحْسَنُ, 41:50 لَلْحُسْنَىٰ

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

## س ل م (root_000737): 41:33 ٱلْمُسْلِمِينَ

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

## د ف ع (root_000480): 41:34 ٱدْفَعْ

- **B001** itip uzaklaştırma ve zararı savuşturma — bir şeyi itip yerinden uzaklaştırmak · birini bir zarardan koruyup onu savuşturmak · birini savunup kötülüğü ondan uzak tutmak · Tanrı'dan kötülükleri uzaklaştırmasını istemek · birbirini itmek · mevkiinde rakipsiz ve yerinden edilemez
  يدل على تنحية الشيء (maqayis)؛ دفعت عنه كذا وكذا دفعا أي منعت ودافع الله عنك المكروه (ayn)؛ دافع عنه ودفع بمعنى واستدفعت الله الأسواء وتدافع القوم أي دفع بعضهم بعضا (sihah)؛ دفع الله عنك المكروه دفعا ودافع عنك دفاعا وفلان سيد قومه غير مدافع أي غير مزاحم (tahdhib)؛ إذا عدي بعن اقتضى معنى الحماية (mufradat)
- **B002** bir şeyi birine ulaştırıp vermek [kalıp] — bir şeyi birine vermek veya ulaştırmak
  دفعت إلى فلان شيئا (sihah)؛ إذا عدي بإلى اقتضى معنى الإنالة (mufradat)
- **B003** atılıp ilerleme ve bir hedefe varma — hızla ileri atılmak · konuşmaya koyulmak · yeryüzünde ilerleme · bir yere ya da kişiye varmak · bulutun bir topluluktan ayrılıp başka bir topluluğa yönelmesi · bir topluluğun bir yere tek seferde varması
  الدفعة انتهاء جماعة قوم إلى موضع بمرة (ayn;tahdhib)؛ اندفع الفرس أي أسرع في سيره واندفعوا في الحديث (sihah)؛ الاندفاع المضي في الأرض وهذا طريق يدفع إلى مكان كذا أي ينتهي إليه ودفع فلان إلى فلان أي انتهى إليه وغشيتنا سحابة فدفعناها إلى بني فلان أي انصرفت عنا إليهم (tahdhib)
- **B004** bir kerelik itiş ya da toplu boşalma — yağmurun, kanın veya kaptaki sıvının bir kerede boşalan miktarı · bir kez itme
  الدفعة من المطر والدم وغيره (maqayis)؛ الدفعة ما دفع من إناء أو سقاء فانصب بمرة (ayn;tahdhib)؛ الدفعة من المطر وغيره مثل الدفقة والدفعة بالفتح المرة الواحدة (sihah)؛ دفع المطر ونحوه (tahdhib)؛ الدفعة من المطر (mufradat)
- **B005** kabarıp birbirini iten büyük kütle — büyük sel veya kabaran dalga kütlesi · birbirini iterek ilerleyen kalabalık ya da hızlanan hareket
  الدفاع فالسيل العظيم (maqayis;sihah;mufradat)؛ الدفاع طحمة الموج والسيل (tahdhib)؛ الدفاع الكثير من الناس ومن السير ومن جري الفرس إذا تدافع جريه وجاء دفاع من الرجال والنساء إذا ازدحموا (tahdhib)
- **B006** su yatağı ve selin dağıldığı çıkış — su yatakları ve akıntı yolları · suyun vadilere döküldüğü alt kesimler · başka bir küçük su yoluna dökülen akıntı yolu · selin dökülüp suyunun ayrıldığı vadi tabanı
  المدفع واحد مدافع المياه التي تجري فيها (sihah)؛ الدوافع أسافل الميث حيث تدفع في الأودية والدافعة التلعة تدفع في تلعة أخرى والمدافع المجاري والمسايل ومدفع الوادي حيث يدفع السيل وهو أسفله حيث يتفرق ماؤه (tahdhib)
- **B007** herkesçe geri çevrilen yoksul ve hor kişi — herkesçe geri çevrilen yoksul ve hor kişi
  المدفع الفقير لأن هذا يدافعه عند سؤاله (maqayis)؛ المدفع الفقير والذليل لأن كلا يدفعه عن نفسه (sihah)؛ المدفع الرجل المحقور الذي لا يقرى إن ضاف ولا يجدى إن اجتدى (tahdhib)؛ المدفع الذي يدفعه كل أحد (mufradat)
- **B008** birinin işini sürüncemede bırakmak — bir gereksinimi karşılamayı sürüncemede bırakma · birini işi konusunda oyalayıp sonucunu vermemek
  المدافعة المماطلة (sihah)؛ دافع فلان فلانا في حاجته إذا ماطله فيها فلم يقضها (tahdhib)
- **B009** doğum öncesi sütün memeye gelmesi — doğumdan önce sütü memeye gelen koyun veya deve · doğumdan önce sütü memeye gelen koyun · yavrusu karnındayken sütü memeye dolmak
  الدافع الشاة أو الناقة التي تدفع اللبأ في ضرعها قبيل النتاج (sihah)؛ الدافع الناقة التي تدفع اللبن على رأس ولدها وكذا الشاة المدفاع ويقال دفعت بلبنها وباللبن إذا كان ولدها في بطنها فإذا نتجت فلا يقال دفعت (tahdhib)
- **B010** yükten esirgenen değerli veya damızlık deve — değerli veya damızlık sayıldığı için binilmeyen ve yüklenmeyen deve
  المدفع البعير الكريم وهو الذي كلما جيء به ليحمل عليه أخر وجيء بغيره إكراما له (maqayis)؛ بعير مدفع كالمقرم الذي يودع للفحلة فلا يركب ولا يحمل عليه (tahdhib)
- **B011** bir işe tutulup bütünüyle dalmak [kalıp] — bir işe tutulup ona bütünüyle dalmak
  دافع الرجل أمر كذا وكذا إذا أولع به وانهمك فيه (tahdhib)

## ح م م (root_000001): 41:34 حَمِيمٌ

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

## ل ق ي (root_001372): 41:35 يُلَقَّىٰهَآ, 41:35 يُلَقَّىٰهَآ, 41:40 يُلْقَىٰ, 41:54 لِّقَآءِ

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

## ح ظ ظ (root_000339): 41:35 حَظٍّ

- **B001** kişiye düşen pay ve bundan gelen iyi şans — kişiye düşen pay; iyi şans · pay sahibi olmak veya bir pay elde etmek · şanslı · geçim imkânları bakımından şanslı · pay sahibi veya şanslı · bir başkasından daha şanslı · paylar; iyi şanslar · pay anlamındaki sözün azlık ve kuralsız çokluk bildiren çoğul biçimleri
  الحظ النصيب والجد (maqayis;sihah)؛ الحظ النصيب المقدر (mufradat)؛ رجل حظيظ ذو حظ (jamhara;sihah)؛ محظوظ (maqayis;sihah;mufradat)
- **B002** küçük eğitim oku ve buna dayalı uyarıcı söz — ok atmayı öğrenmekte kullanılan küçük oklar · küçümsendiği hâlde korkutucu olan şey için kullanılan kalıplaşmış söz
  الحظاء سهام صغار يتعلم بها الرمي؛ إحدى حظيات لقمان للشيء الذي تستهين به وهو مخوف
- **B003** bir ilaç adının dilsel varyantı — 
  الحُظُظ والحُظَظ لغة في الحُضُض، وهو دواء

## ع ظ م (root_001029): 41:35 عَظِيمٍ

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

## ن ز غ (root_001490): 41:36 يَنزَغَنَّكَ, 41:36 نَزْغٌ

- **B001** ilişkileri bozma, kışkırtma ve bozmak için işe karışma — topluluğun arasını bozup insanları birbirine düşürmek · bozguncu ve kışkırtıcı düşmanlar · bir işe onu bozmak amacıyla karışma
  تدل على إفساد بين اثنين (maqayis)؛ أفسد ذات بينهم (maqayis)؛ حمل بعضهم على بعض بفساد ذات بينهم (ayn)؛ أفسد وأغرى (sihah)؛ دخول في أمر لإفساده (mufradat)
- **B002** birini bir sözle iğneleyip yerme [kalıp] — birini bir sözle iğneleyip yermek
  نزغه بكلمة أي طعن فيه (sihah)

## ش ط ن (root_000796): 41:36 ٱلشَّيْطَٰنِ

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

## ع و ذ (root_001059): 41:36 فَٱسْتَعِذْ

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

## ل ي ل (root_001392): 41:37 ٱلَّيْلُ, 41:38 بِٱلَّيْلِ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ن ه ر (root_001559): 41:37 وَٱلنَّهَارُ, 41:38 وَٱلنَّهَارِ

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

## ش م س (root_000818): 41:37 وَٱلشَّمْسُ, 41:37 لِلشَّمْسِ

- **B001** güneş, güneş diski ve ışığı; güneşli olma ve güneşe çıkma — güneş; güneşin görünen diski ve yayılan ışığı · gündüzünün tamamı güneşli olan gün · günümüz güneşli oldu; güneşi güçlendi · güneşte yapılmış ya da güneşe tutulmuş · güneşe çıkıp ona yönelmek
  الشمس معروفة (maqayis)؛ الشمس عين الضح (ayn;tahdhib)؛ الشمس يقال للقرصة وللضوء المنتشر عنها (mufradat)؛ يوم شامس وقد شمس يشمس شموسا (ayn;tahdhib)؛ شيء مشمس وتشمس (sihah)
- **B002** ürküp kaçınma, durulmama ve güçlük çıkarma — yerinde durmayan, dürtülünce sırtını kullandırmayan hayvan · huysuz, geçimsiz ve tutumu değişken adam · kuşkulu bir durumdan ürküp uzak duran kadın · kaçıp yerinde durmadı
  الشموس من الدواب الذي لا يكاد يستقر (maqayis)؛ الشمس والشموس من الدواب الذي إذا نخس لم يستقر (ayn;tahdhib)؛ شمس الفرس شموسا وشماسا أي منع ظهره (sihah)؛ رجل شموس عسر (ayn;tahdhib)؛ رجل شموس صعب الخلق (sihah)؛ امرأة شموس إذا كانت تنفر من الريبة (maqayis)؛ شمس فلان شماسا إذا ند ولم يستقر (mufradat)
- **B003** birine düşmanlığını açıkça göstermek [kalıp] — bana düşmanlığını açıkça gösterdi ve sert davrandı
  شمس لي فلان إذا أبدى لك عداوته (maqayis;sihah)؛ شمس لي فلان إذا أبدى لك عدواته (ayn)؛ شمس لي فلان إذا أبدى لك عداوته كأنه قد هم أن يفعل (tahdhib)
- **B004** kolye sarkıtları ya da bir kolye türü — kolyeye asılan süsler ya da bir kolye türü
  الشموس معاليق القلائد (ayn;tahdhib)؛ الشمس ضرب من القلائد (sihah)
- **B005** başı ortadan tıraşlı, kiliseye bağlı Hristiyan önder din görevlisi — başının ortasını tıraş eden ve kiliseye sürekli bağlı kalan Hristiyan önder din görevlisi
  الشماس من رؤساء النصارى الذي يحلق وسط رأسه لازما للبيعة (ayn;tahdhib)؛ الجميع الشمامسة (ayn;tahdhib)
- **B006** arkasındakini koruma, topluluğunu savunma ve iyiliğini esirgeme — arkasındakini koruyup engelleyen ya da topluluğunu güçlü biçimde savunan adam · bize karşı cimrilik etti ve iyiliğini esirgedi
  المتشمس من الرجال الذي يمنع ما وراء ظهره (tahdhib)؛ وهو الشديد القومية (tahdhib)؛ البخيل أيضا متشمس (tahdhib)؛ تشمس علينا أي بخل (tahdhib)
- **B007** güneş kökünden kişi, topluluk, put ve yer adları ile bağlılık türetmeleri — kul ve güneş öğelerinden kurulmuş birleşik bir Arap kişi adı · güneş adı verilen eski bir put · güneş adı verilen tanınmış bir su kaynağı · belirli bir topluluk içinde güneş sözcüğüne bağlanan kişi ya da soy adı · güneş öğeli kişi ya da soy adına mensup olan · güneş öğeli topluluğa antlaşma, koruma ilişkisi ya da bağlılık yoluyla bağlanmak · çıkışı zor olduğu için bu kökten adlandırılmış tanınmış bir tepe · Firdevs'in karşısında bulunan iki bahçenin ortak adı
  عبد شمس (maqayis;sihah)؛ الشمس صنم قديم (maqayis)؛ شمس عين ماء معروفة (maqayis)؛ عبشمس وعبشمي (maqayis;sihah)؛ تعبشم الرجل (sihah)؛ الشموس هضبة معروفة (tahdhib)؛ الشميستان جنتان بإزاء الفردوس (tahdhib)

## ق م ر (root_001255): 41:37 وَٱلْقَمَرُ, 41:37 لِلْقَمَرِ

- **B001** Ay, ay ışığı ve ayla aydınlanan gece — gökteki Ay · küçük Ay; Ay adının küçültme biçimi · ay ışığı · ay ışığıyla aydınlanan gece · Ay üzerimize doğdu
  القمر قمر السماء سمى قمرا لبياضه (maqayis)؛ القمراء ضوء القمر وليلة مقمرة (ayn;tahdhib)؛ القمر بعد ثلاث ليال إلى آخر الشهر (sihah)؛ القمر قمر السماء يقال عند الامتلاء (mufradat)
- **B002** ay ışığını andıran beyaz ya da yeşile çalan açık renk — beyaz ya da yeşile çalan açık renkli · yeşile çalan beyazımsı renk
  حمار أقمر أي أبيض (maqayis)؛ القمرة لون الحمار الأقمر وهو لون يضرب إلى الخضرة (ayn;tahdhib)؛ سحاب أقمر وأتان قمراء بيضاء وهجان أقمر (sihah;tahdhib)؛ حمار أقمر على لون القمراء (mufradat)
- **B003** ay ışığında yaklaşma, avı gafil yakalama ve avlama — ona ay ışığında gitti · aslan ay ışığında ava çıktı · kuşların gece görüşünü şaşırtıp onları avladılar · ona ay ışığında gitti; gafletinden yararlanıp aldattı; başka bir açıklamada onunla evlenip onu götürdü
  تقمرته أتيته في القمراء (maqayis;sihah;mufradat)؛ تقمر الأسد إذا خرج في القمراء يطلب الصيد (maqayis;sihah)؛ قمر القوم الطير إذا عشوها ليلا فصادوها (maqayis)؛ تقمرها أتاها في القمراء وطلب غرتها وخدعها (tahdhib)؛ تقمر الصياد الظباء والطير بالليل فتقمر أبصارها فتصاد (tahdhib)
- **B004** olgunlaşmadan soğuğa uğrayıp tatsızlaşma — palmiye meyvesi olgunlaşmadan soğuğa uğrayıp tadını ve tatlılığını yitirdi
  قمر التمر وأقمر إذا ضربه البرد فذهبت حلاوته قبل أن ينضج (maqayis)؛ أقمر التمر أي لم ينضج حتى أصابه البرد فذهبت حلاوته وطعمه (ayn;tahdhib)؛ أقمر التمر ضربه البرد فذهبت حلاوته قبل أن ينضج (sihah)
- **B005** kar beyazlığından gözü kamaşıp görememe — kar beyazlığında gözü kamaşıp göremez oldu
  قمر الرجل إذا لم يبصر في الثلج (maqayis;sihah)؛ قمر الرجل إذا حار بصره في الثلج فلم يبصر (tahdhib)
- **B006** su tulumunun ay aydınlığı ya da katman arası suyla bozulması — su tulumu ay aydınlığından yanmış gibi ya da su deri katmanları arasına girdiği için bozuldu
  قمرت القربة وهو شيء يصيبها كالاحتراق من القمر (maqayis)؛ قمرت القربة... يصيبها من القمر كالاحتراق فيدخل الماء بين الأدمة والبشرة (sihah)؛ قمرت القربة... دخل الماء بين الأدمة والبشرة فأصابها قضاء وفساد (tahdhib)؛ قمرت القربة فسدت بالقمراء (mufradat)
- **B007** değer ortaya koyulan talih oyununda karşılaşma, yenme ve aldatma — para ya da mal ortaya konan talih oyunu ve bu oyunda karşılıklı yarışma · onunla talih oyununda yarışıp onu yendi · oynayacak rakip aradı ya da rakibini yendi · onu hileyle aldattı
  القمار من المقامرة... تقمر الرجل إذا طلب من يقامره (maqayis)؛ قامرته فقمرته من القمار (ayn)؛ تقمر فلان أي غلب من يقامره وتقامروا لعبوا القمار وقمرت الرجل إذا لاعبته فغلبته (sihah)؛ القمار مأخوذ من الخداع يقال قامره بالخداع فقمره (tahdhib)؛ قمرت فلانا خدعته عنه (mufradat)
- **B008** su ve otlağın bol olması — su ve otlak bol oldu
  قمر الماء والكلأ إذا كثر (tahdhib)
- **B009** ay ışığında uykusu kaçıp uyuyamama — ay ışığında uykusu kaçtı ve uyuyamadı
  قمر الرجل أرق في القمر فلم ينم (tahdhib)
- **B010** develerin akşam yeminin gecikmesi — develerin akşam yemi gecikti
  قمرت الإبل إذا تأخر عشاؤها (tahdhib)
- **B011** hayvan sürüsünü gece çobansız ve gözetimsiz bırakma [kalıp] — hayvan sürüsünü gece çobansız ve gözetimsiz bıraktım
  استرعيت مالي القمر إذا تركته هملا ليلا بلا راع يحفظه (tahdhib)؛ لم أسترعها الشمس والقمر أي لم أهملها (tahdhib)
- **B012** üveyik ya da güvercin benzeri kuş — üveyik ya da güvercin benzeri kuş ve bu kuşların çoğulu
  القمري طائر كالفاختة مسكنه الحجاز (ayn)؛ القمرى منسوب إلى طير قمر والجمع قماري (sihah)؛ القمري طائر يشبه الحمام (tahdhib)

## س ج د (root_000675): 41:37 تَسْجُدُوا۟, 41:37 وَٱسْجُدُوا۟

- **B001** alçalıp boyun eğme ve alnı yere koyma — boyun eğmek veya alnını yere koymak · alçalıp boyun eğme; isteyerek ya da zorunlu düzene bağlılık · bir kez alnını yere koyarak eğilme veya bu eğilişin biçimi
  أصل واحد مطرد يدل على تطامن وذل (maqayis)؛ سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض (sihah)؛ سجد إذا وضع جبهته بالأرض (tahdhib)؛ السجود أصله التطامن والتذلل (mufradat)
- **B002** alnı yere koyma yeri, buna ayrılmış yapı veya küçük yaygı — toplu tapınma yeri veya bu amaçla kurulmuş yapı · zeminde alnın konduğu yer · iki belirli kutsal kentteki iki tanınmış tapınma yapısı · üzerinde alnı yere koyarak eğilinen küçük dokuma yaygı · tapınma yerleri veya alnı yere koymaya elverişli yerler
  المسجد اسم جامع يجمع المسجد وحيث لا يسجد بعد أن يكون اتخذ لذلك (ayn)؛ المسجد معروف (jamhara)؛ المسجد والمسجد واحد المساجد والمسجدان مسجد مكة ومسجد المدينة (sihah)؛ المسجد موضع الصلاة (mufradat)؛ السجادة الخمرة (sihah)
- **B003** yere dayanan beden bölümleri ve alındaki temas izi — alnı yere koyarken yere dayanan beden bölümleri · alnın yere değen ve temas izi oluşan bölümü · alında tekrarlanan yere temasın bıraktığı iz
  المسجد الإرب الذي يسجد عليه مثل الكفين والركبتين والقدمين والجبهة (jamhara)؛ الآراب السبعة مساجد والمسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود (sihah)؛ المساجد مواضع السجود من الإنسان الجبهة والأنف واليدان والركبتان والرجلان (tahdhib;mufradat)
- **B004** başı ve gövdeyi aşağı eğme veya yük altında yana yatma — başını alçaltıp gövdesini öne eğmek · belden öne eğilmiş durumda olmak · meyve yüküyle eğilip yana yatmış hurma ağacı
  أسجد الرجل إذا طأطأ رأسه وانحنى (maqayis;sihah;tahdhib)؛ أسجد للبعير أي طأطأ لها لتركبه (sihah;tahdhib)؛ سجدا أي ركعا (tahdhib)؛ نخلة ساجدة إذا أمالها حملها (tahdhib)
- **B005** bakışı aşağıda ve devinimsiz tutma, göz kapaklarında gevşeklik — bakışı aşağı yönelmiş durumda uzun süre ve devinimsiz tutma · durgun ve gevşek bakışlı göz · gözleri durgun ve gevşek görünen kadınlar
  الإسجاد إذا أدام النظر في خفض (maqayis)؛ الإسجاد إدامة النظر مع سكون (ayn;tahdhib)؛ أصل السجود إدامة النظر في إطراق إلى الأرض (jamhara)؛ الإسجاد إدامة النظر وإمراض الأجفان (sihah)؛ نساء سجد فاترات الأعين وامرأة ساجدة ساجية (ayn)؛ الإسجاد أيضا فتور الطرف (tahdhib)
- **B006** önünde eğilinilen hükümdar betimli sikkeler [kalıp] — üzerlerindeki betimler veya betimlenen hükümdar önünde eğilinilen sikkeler
  دراهم الإسجاد دراهم كانت عليها صور فيها صور ملوكهم وكانوا إذا رأوها سجدوا لها (maqayis)؛ دراهم كانت عليها صور يسجدون لها (sihah)؛ دراهم عليها صورة ملك سجدوا له (mufradat)
- **B007** Yahudiler için ad, baş vergisi ve bu verginin parası — Yahudiler · baş vergisi · baş vergisi olarak verilen para
  الإسجاد بكسر الهمزة اليهود (tahdhib)؛ أعطونا إسجادا أي الجزية (tahdhib)؛ دراهم الأسجاد عنى دراهم الجزية (tahdhib)

## ع ن د (root_001052): 41:38 عِندَ, 41:50 عِندَهُۥ, 41:52 عِندِ

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

## س ب ح (root_000666): 41:38 يُسَبِّحُونَ

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

## س ء م (root_000662): 41:38 يَسْـَٔمُونَ, 41:49 يَسْـَٔمُ

- **B001** uzun süren bir şeyden usanma — bir şeyden usanmak veya bıkmak · usanma, bıkkınlık · usanma, bıkkınlık · usanma, bıkkınlık · uzun sürmesi yüzünden bir şeyden usanma · sık sık usanan kimse
  سئمت من الشئ أسأم سأما وسأمة وسآما وسآمة، إذا مللته (sihah)؛ السآمة: الملالة مما يكثر لبثه، فعلا كان أو انفعالا (mufradat)

## خ ش ع (root_000412): 41:39 خَٰشِعَةً

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

## م و ه (root_001458): 41:39 ٱلْمَآءَ

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

## ه ز ز (root_001588): 41:39 ٱهْتَزَّتْ

- **B001** sarsarak hareket ettirme ve sarsılma — bir şeyi şiddetle sarsma · mızrağı ya da benzerini sallayıp titreştirme · sarsılıp hareket etme · yıldızın kayarken titreşmesi · bir şeyi tekrar tekrar sarsma
  أصل يدل على اضطراب في شيء وحركة (maqayis)؛ هززت الرمح ونحوه فاهتز (ayn)؛ هززت السيف أهزه هزا (jamhara)؛ هززت الشئ هزا فاهتز أي حركته فتحرك (sihah)؛ الهز تحريكك الشيء كما تهز القناة فتضطرب وتهتز (tahdhib)؛ الهز التحريك الشديد (mufradat)
- **B002** bitkinin canlanıp salınması ve toprağın yeşermesi [kalıp] — bitkinin canlanıp salınması veya boy atması · toprağın su aldıktan sonra bitki vermesi
  اهتز النبات وهزته الريح (maqayis)؛ اهتزت الأرض نبتت (ayn)؛ اهتز النبات إذا طال واهتزت الأرض إذا أنبتت (tahdhib)؛ اهتز النبات إذا تحرك لنضارته (mufradat)
- **B003** iyiliğe heveslendirme ve içten coşma — birini iyiliğe veya vermeye heveslendirme · insanı saran coşku ve içten istek · gönlüm ona ısındı ve yakınlık duydu · sevinme diye yorumlanan, anlamı tartışmalı kullanım
  هززت فلانا للخير فاهتز للخير (ayn;tahdhib)؛ أخذت فلانا هزة إذا مدح فأخذته أريحية (jamhara)؛ الهزة النشاط والارتياح (sihah)؛ هززت فلانا للعطاء (mufradat)؛ تهزهز إليه قلبي أي ارتاح وهش (tahdhib)
- **B004** ezgiyle develeri yürütme ve çevikçe hızlanma — ezgili çağrıyla develeri yürüyüşe geçirme · develerin çevik yürüyüşü veya kervanın hızlanması
  هز الحادي الإبل بحدائه واهتزت هي في سيرها (maqayis)؛ هز الحادي الإبل هزا فاهتزت هي إذا تحركت في سيرها لحدائه (sihah)؛ الهزيز في السير تحريك الإبل في خفتها، هزها السير وهزها الحادي (tahdhib)؛ يهتز أي يسرع (tahdhib)
- **B005** hareketin çıkardığı uğultu ve hışırtı — rüzgarın ağaçları sallarken çıkardığı uğultu · kervanın hışırtısı ve toplu gürültüsü · tencerenin kaynama sesi
  هزيز الريح حركتها وصوتها (maqayis)؛ هزة الموكب إذا سمعت حفيفه (jamhara)؛ الهزة صوت غليان القدر واهتزاز الموكب صوتهم وجلبتهم وهزيز الريح دويها عند هزها الشجر (sihah)
- **B006** insanları altüst eden kargaşa ve savaşlar — insanları altüst eden kargaşalar, yıkımlar ve savaşlar
  الهزاهز الفتن يهتز فيها الناس (maqayis;sihah)؛ الهزهزة والهزاهز تحريك البلايا والحروب للناس (ayn;tahdhib)
- **B007** iyi salınan parlak kılıç; dalgalı ve berrak akan su [kalıp] — parlak ve iyi salınan kılıç · akarken dalgalanan veya berrak görünen su · suyu dalgalanarak akan ırmak
  سيف هزهاز وهزهز صاف حسن الاهتزاز، وماء هزهز اهتز في جريانه (maqayis)؛ ماء هزهز وهزاهز وهزهاز وكذلك يقال للسيف (jamhara)؛ سيف هزهاز ونهر هزهز (sihah)؛ ماء هزهز في اهتزازه إذا جرى، وماء صافيا كالسيف اليماني في صفائه (tahdhib)؛ سيف هزهاز وماء هزهز (mufradat)
- **B008** hafif ve çevik hareketli adam — hafif ve çevik hareketli adam
  الهزهز الرجل الخفيف (maqayis)؛ رجل هزهز خفيف (mufradat)
- **B009** dibi çok derin kuyu [kalıp] — dibi çok derin kuyu
  بئر هزهز بعيدة القعر (tahdhib)

## م و ت (root_001454): 41:39 ٱلْمَوْتَىٰٓ

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

## ل ح د (root_001345): 41:40 يُلْحِدُونَ

- **B001** haktan ve doğru yoldan sapma — doğru amaçtan, haktan ve inanç yolundan sapmak · haktan ve doğru amaçtan sapmak · doğru amaçtan yanlışlığa, haksızlığa veya ortak koşmaya sapma · kutsal yerde doğru davranıştan ayrılıp haksızlığa yönelme · Tanrı'nın adlarına uygunsuz nitelikler yükleme veya onları yakışıksız yorumlama · inancı geçersiz kılan biçimde Tanrı'ya ortak koşmaya yönelme · inancı zayıflatan biçimde nedenlere bağımsız güç yükleyip ortak koşmaya yönelme · haktan ayrılıp yanlış olana yönelen kimse · haktan yanlış olana sapan kimse
  أصل يدل على ميل عن استقامة (maqayis)؛ مال عن طريقة الحق والإيمان (maqayis)؛ مال عن القصد ومال إلى الظلم (ayn)؛ مال عن القصد (jamhara)؛ حاد عنه وعدل (sihah)؛ العادل عن الحق (tahdhib)؛ الميل عن القصد (tahdhib)؛ مال عن الحق (mufradat)؛ إلحاد إلى الشرك بالله وإلحاد إلى الشرك بالأسباب (mufradat)
- **B002** mezarın yan oyuğu — mezarın yan oyuğu veya ortadan yana eğilen çukuru · mezarın yan oyuğunu kazmak · onun için mezarın yan oyuğunu kazmak · ölüyü mezarın yan oyuğuna yerleştirmek · ölüyü mezarın yan oyuğuna yerleştirmek · mezarın yan oyuğuna yerleştirilmiş veya bu oyuğa ait · yan oyuğu bulunan mezar veya yan oyuk yeri
  سمي اللحد لأنه مائل في أحد جانبي الجدث (maqayis)؛ اللحد ما حفر في عرض القبر (ayn;tahdhib)؛ اللحد معروف والجمع لحود وألحاد (jamhara)؛ الشق في جانب القبر (sihah;tahdhib)؛ اللحد حفرة مائلة عن الوسط (mufradat)
- **B003** sığınma yeri veya ona sığınma — sığınak veya sığınma yeri · bir şeye yönelip ona sığınmak
  الملتحد الملجأ (maqayis)؛ يلتحد إلى الشيء يلجأ إليه ويميل (ayn)؛ الملتحد المجأ لأن اللاجئ يميل إليه (sihah)؛ ملتحدا أي ملجأ ولا سربا ألجأ إليه (tahdhib)؛ التجاء أو موضع التجاء (mufradat)
- **B004** sözle yönelme, itiraz etme veya tartışma — sözünü bir şeye veya kimseye yöneltmek · ona yönelmek · ona itiraz etmek veya yönelmek · tartışmak ve çekişmek
  لحد إليه بلسانه (ayn)؛ لسان الذي يلحدون إليه (ayn;sihah;tahdhib;mufradat)؛ يلحدون أراد يميلون إليه ويلحدون يعترضون (tahdhib)؛ ألحدت ماريت وجادلت (tahdhib)؛ لحد بلسانه إلى كذا مال (mufradat)
- **B005** kenar veya fiziksel yana sapma — herhangi bir şeyin kenarı veya yanı · eğrilmek ve düz doğrultudan sapmak · doğru doğrultudan ayrılmış eğri kuyu · okun hedefin bir yanına sapması
  أصل يدل على ميل عن استقامة (maqayis)؛ لحد كل شيء حرفه وناحيته (tahdhib)؛ ركية لحود زوراء أي مخالفة عن القصد (tahdhib)؛ ألحد السهم الهدف مال في أحد جانبيه (mufradat)

## خ ف ي (root_000428): 41:40 يَخْفَوْنَ

- **B001** gizli kalma ya da gizleme — şey gizli kaldı, görünmedi · şeyi ve onun haberini sakladı · şeyi gizledi ve sakladı · gizlilik ve saklılık hâli · gizlilik, görünmezlik · gizlenip gözden uzaklaştı · bir aktarıma göre gizlendi · gizlenen kişi · onunla gizlice buluştum
  خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته (maqayis); أخفيت الصوت إخفاء وفعله اللازم اختفى والخافية ضد العلانية ولقيته خفيا أي سرا (ayn); خفيت الشئ أخفيه كتمته وأخفيت الشئ سترته وكتمته واستخفيت منك أي تواريت (sihah); خفي الشيء خفية استتر وأخفيته أوليته خفاء وذلك إذا سترته ويقابل به الإبداء والإعلان (mufradat)
- **B002** örten ya da gizli kalan şey — gizli ya da örtülü şey · örtü veya örten giysi · kanadın iç tüyleri; hurma göbeğine yakın yapraklar · görünmeyen varlık · kanadın iç tüylerinden biri · bedende gizlendiğine inanılan görünmeyen varlık · kuyu, koruluk veya gizli yer · bu adla anılan iki aslan yatağı · su tulumunun üzerine atılan örtüler · kadının sesi ile yerdeki ayak izi
  الخوافي سعفات يلين قلب النخلة والخافي الجن (maqayis); الخفا مقصور الشيء الخافي والموضع الخافي والخفاء رداء تلبسه المرأة وكل شيء غطيت به شيئا فهو خفاء والخفية غيضة والخفية بئر والخوافي من الجناحين (ayn); الخافي الجن والخافية ما يخفى في البدن من الجن والخفية الركية والخوافى ما دون الريشات العشر والخوافي من السعف (sihah); الخفاء ما يستر به كالغطاء والخوافي جمع خافية وهي ما دون القوادم من الريش (mufradat)
- **B003** gizliliği giderip açığa çıkarma — gizli olan açığa çıktı, sır belli oldu · şeyi açığa çıkardı · şeyin gizliliğini giderip onu gösterdi · yağmur fareleri yuvalarından çıkardı · gizli şeyi çıkarıp ortaya koydu · kefenleri çıkardığı için mezar soyguncusu
  الأصل الآخر الإظهار وخفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن (maqayis); الخفا إخراجك الشيء الخفي وإظهاركه وخفيت الخرزة من تحت التراب أخفيها خفيا (ayn); وخفيته أيضا أظهرته وهو من الأضداد وخفى المطر الفأر إذا أخرجهن واستخفيت الشئ أي استخرجته وأخفيها أي أزيل عنها خفاءها (sihah); وخفيته أزلت خفاه وذلك إذا أظهرته (mufradat)
- **B004** belli belirsiz şimşek çakması — şimşek belli belirsiz ve zayıfça çaktı
  خفا البرق خفوا إذا لمع ويكون ذلك في أدنى ضعف (maqayis); وخفا البرق يخفو خفوا ويخفى خفيا أي ظهر من الغيم (ayn); خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا (jamhara); وخفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم (sihah)

## خ ي ر (root_000452): 41:40 خَيْرٌ, 41:49 ٱلْخَيْرِ

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

## ذ ك ر (root_000516): 41:41 بِٱلذِّكْرِ

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

## ب ط ل (root_000127): 41:42 ٱلْبَٰطِلُ

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

## ح ك م (root_000348): 41:42 حَكِيمٍ

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

## ح م د (root_000355): 41:42 حَمِيدٍ

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

## ع ق ب (root_001033): 41:43 عِقَابٍ

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

## ء ل م (root_000046): 41:43 أَلِيمٍ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ع ج م (root_000988): 41:44 أَعْجَمِيًّا, 41:44 ءَاۚعْجَمِىٌّ

- **B001** açık anlatımın, anlaşılır sesin veya yanıtın yokluğu — açık ve anlaşılır konuşamama · sözünü açık anlatamayan · dilini açık konuşamayan kimse; açık olmayan dil veya yazı · Arap olmayan topluluğa mensup kişi · Arap olmayan halklar · konuşamayan hayvan · başıboş hayvanın verdiği zarar için sahibinin sorumlu tutulmaması · okumanın sesli yapılmadığı gündüz ibadeti · yanıt verecek kimsenin kalmadığı ev · sözün veya okunan metnin anlaşılmaz hale gelmesi · kilitli kapı veya çözülmesi güç iş · ses çıkarmayan dalga · böğürmeyen deve · sözü anlaşılmaz veya yabancı dilde söylemek · kitabın harflerini seçememek
  العجمة خلاف الإبانة (mufradat)؛ أحدها يدل على سكوت وصمت (maqayis)؛ الأعجم الذي لا يفصح (maqayis;ayn;sihah;tahdhib)؛ العجم ضد العرب (ayn;sihah;mufradat)؛ العجماء البهيمة لأنها لا تتكلم (maqayis;ayn;sihah;tahdhib;mufradat)؛ صلاة النهار عجماء (maqayis;ayn;sihah;tahdhib;mufradat)؛ استعجمت الدار عن جواب السائل (maqayis;ayn;mufradat)؛ باب معجم مبهم (mufradat)؛ قفل معجم وأمر معجم إذا اعتاص (tahdhib)؛ الأعجم من الموج الذي لا يتنفس (sihah)
- **B002** harfleri ayırt etmek için yazıyı noktalama — alfabenin ayrı ayrı yazı harfleri · yazıyı ayırt etmek için harfleri noktalamak · yazının belirsizliğini noktalama yoluyla gidermek
  حروف المعجم الحروف المقطعة (maqayis;ayn;sihah;tahdhib;mufradat)؛ تعجيم الكتاب تنقيطه (maqayis;ayn;sihah;tahdhib)؛ أعجمت الكتابة أزلت عجمتها (mufradat)؛ العجم النقط بالسواد (sihah)
- **B003** azı dişleriyle sertçe ısırma — azı dişleriyle sertçe ısırma · çubuğu sertliğini anlamak için ısırma · ok saplarını ısırarak veya bastırarak sertliklerini sınama · çekirdekli hurmayı ağızda çiğneme · boğanın boynuzunu ağaca sürterek temizlemesi veya sınaması · kılıcı denemek için sallama · ısırmaya yarayan dişler · dikenli çalıları yiyerek beslenen develer
  العجم العض (sihah;tahdhib)؛ أصل يدل على عض ومذاقه (maqayis)؛ عجمت العود عضضت عليه بأسناني أيها أصلب (ayn)؛ عجمت العود إذا عضضته لتعلم صلابته (sihah;tahdhib)؛ العجم العض عليه (mufradat)؛ الثور يعجم قرنه (ayn;sihah;tahdhib)؛ عجم السيف هزه للتجربة (sihah)
- **B004** sınamada ortaya çıkan sertlik ve dayanıklılık — sınanınca sağlam ve güçlü çıkan kişi · güçlü, semiz ve yola dayanıklı deve · sert ve güçlü dişi deve · yolculuğa dayanıklı güçlü dişi deve
  أصل يدل على صلابة وشدة (maqayis)؛ صلب المعجم (ayn;sihah;tahdhib;mufradat)؛ ناقة ذات معجمة (ayn;sihah;tahdhib)؛ العجمجمة من النوق الشديدة (sihah;tahdhib)
- **B005** yenebilir meyvenin çekirdeği — çekirdekli hurmayı ağızda çiğneme · meyve çekirdeği veya yenebilir şeyin içindeki sert kısım · tek çekirdek; çekirdekten yetişen hurma fidanı · meyve eti soyulmuş çekirdek · çekirdeği parçalanıp bozuluncaya kadar fazla pişirmek
  عجم التمر نواه (ayn)؛ العجم النوى وكل ما كان في جوف مأكول (sihah)؛ العجم نوى التمر والنبق (tahdhib)؛ العجم النوى الواحدة عجمة (mufradat)؛ العجمة النخلة تنبت من النواة (sihah)؛ نعجم النوى طبخا أي نبالغ في طبخه (tahdhib)
- **B006** yalıtık adlandırmalar — kumluğun en iri ve yığılmış bölümü ya da sonu · vadilerde yükselen kayalar
  عجمة الرمل أكثره وأضخمه وأكثره تراكما في وسط الرمل (ayn)؛ عجمة الرمل آخره (sihah)؛ العجمات صخور تنبت في الأودية (tahdhib)
- **B007** genç develer — yavruluktan çıkmış, henüz yetişkin olmayan erkek ve dişi develer
  العجم أيضا صغار الإبل (sihah)؛ العجم صغار الإبل ويجمع عجوما (tahdhib)
- **B008** kuyruk kökü, kuyruk sokumu — kuyruk kökü veya kuyruk sokumu
  العجم أصل الذنب مثل العجب وهو العصعص (sihah)
- **B009** gözün birini seçip tanır gibi olması [kalıp] — gözün birini seçip tanır gibi olması veya uzun süredir görmemesi
  ما عجمتك عيني أي ما أخذتك (ayn;sihah)؛ جعلت عيني تعجمه كأنها تعرفه (sihah)؛ تعجمك عيني أي كأني أعرفك (tahdhib)
- **B010** tat veya deneyimle anlaşılmış nitelik — tadı hoş veya denenince iyi bulunan · tat veya deneyimle anlaşılmış nitelik
  أصل يدل على عض ومذاقه (maqayis)؛ حلو المعجم أي محمود الخبر (ayn)؛ المعجم ههنا المذاق (ayn)

## ش ف ي (root_000806): 41:44 وَشِفَآءٌ

- **B001** rahatsızlığı giderip iyileştirme veya içi rahatlatma — hastalıktan kurtulma ve iyileşme · onu hastalığından kurtarıp iyileştirdi · iyileşmenin yolunu aradı · ona iyileştirici bir şey verdi · sana iyileşmekte kullanacağın şeyi verdim · ona iyileştirecek bir ilaç önerdi · balı onun için iyileştirici kıldı · bilmezliği gidermenin yolu sormaktır · öfkemi giderip rahatladım · ondan öç alarak içimi soğuttum · haberin doğruluğuna inanıp içim rahatladı
  الشفاء معروف وهو ما يبرئ من السقم (ayn;tahdhib)؛ شفاه الله من مرضه شفاء واستشفى طلب الشفاء وأشفيتك الشيء أعطيتكه تستشفي به (sihah)؛ سمي الشفاء شفاء لغلبته للمرض وإشفائه عليه واستشفى فلان إذا طلب الشفاء وأشفيتك الشيء (maqayis)؛ الشفاء من المرض موافاة شفا السلامة وصار اسما للبرء وهدى وشفاء وشفاء لما في الصدور ويشف صدور قوم مؤمنين (mufradat)؛ شفاء العي السؤال (ayn;tahdhib)؛ تشفيت من غيظي (sihah)؛ اشتفيت به أي نقعت بصحته وصدقه وتشفيت من فلان إذا أنكى في عدوه نكاية تسره (tahdhib)
- **B002** kenar, eşiğe yaklaşma veya sondan kalan azlık — bir şeyin kenarı veya kıyısı · kuyunun ağzı veya kenarı · çukurun ya da yarın kenarı · bir şeyin eşiğine gelip çok yaklaşmak · yok oluşun eşiğine gelmek · hasta ölümün eşiğine geldi · bir vasiyet veya emaneti gözetmek · sonda kalan küçük bölüm · geriye yalnızca pek azı kaldı · güneşin batmasına çok az kaldı · güneş batmak üzereydi · ayın seyrinde gecenin son bölümü
  شفا كل شيء حرفه وأشفى على الشيء وأشفى المريض على الموت وما بقي منه إلا شفا أي قليل (sihah)؛ شفا كل شيء جرفه والشفا بقية الهلال وبقية البصر وبقية النهار وأشفى فلان على الهلكة وشفت الشمس إذا غابت إلا قليلا (tahdhib)؛ شفا البئر وغيرها حرفه ويضرب به المثل في القرب من الهلاك وأشفى فلان على الهلاك (mufradat)؛ الشين والفاء والحرف المعتل يدل على الإشراف على الشيء وشفى كل شيء حرفه وما بقي منه إلا شفى أي قليل وأشفت الشمس على الغروب (maqayis)
- **B003** biz — biz, deri delme aleti · bizler, deri delme aletleri
  الإشفى المثقب والجميع الأشافي (ayn)؛ الإشفى الذي للأساكفة وما كان للأساقى والمزاود وأشباهها والمخصف للنعال (sihah)
- **B004** dudak ve dudağa dayanan kullanımlar — dudak · dudaklar · dudaklar · küçük dudak · ağızdan ağıza yüz yüze konuşma · dudaksıl, dudakla ilgili · iri dudaklı adam · dudakları kapanmayan adam
  الشفة نقصانها واو تقول شفة وثلاث شفوات ومنهم من يقول نقصانها هاء وتجمع شفاها والمشافهة مفاعلة منه والباء والميم شفويتان (tahdhib)؛ الشفة قيل الناقص منها واو وقال قوم الشفة حذفت منها الهاء والمشافهة بالكلام مواجهة من فيك إلى فيه ورجل شفاهي عظيم الشفتين ورجل أشفى إذا كان لا ينضم شفتاه (maqayis)

## ن د و (root_001486): 41:44 يُنَادَوْنَ, 41:47 يُنَادِيهِمْ

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

## ECHO ن د ي (root_001487): for 41:44 يُنَادَوْنَ, 41:47 يُنَادِيهِمْ: withheld observed target; not identity

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

## ECHO ن و د (root_001563): for 41:44 يُنَادَوْنَ, 41:47 يُنَادِيهِمْ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## ب ع د (root_000131): 41:44 بَعِيدٍ, 41:50 بَعْدِ, 41:52 بَعِيدٍ

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

## ك ل م (root_001316): 41:45 كَلِمَةٌ

- **B001** anlaşılır konuşma, hitap ve söz alışverişi — anlaşılır konuşma · ona hitap etti · birine söz yöneltme · ona sözle karşılık verdi · bir uzaklaşmadan sonra yeniden karşılıklı konuştuk · seninle konuşan ve senin de konuştuğun kişi · konuşulacak yer · sözünü iyi ve akıcı söyleyen kimse · iyi konuşan adam
  أحدهما يدل على نطق مفهم (maqayis)؛ كلمته أكلمه تكليما وهو كليمى إذا كلمك أو كلمته (maqayis)؛ كليمك الذي يكلمك وتكلمه (ayn;tahdhib)؛ الكليم الذي يكلمك وكلمته تكليما وكلاما (sihah)؛ كالمته إذا جاوبته وتكالمنا بعد التهاجر (sihah)؛ ما أجد متكلما أي موضع كلام والكلماني المنطيق (sihah)؛ رجل تكلامة يحسن الكلام (tahdhib)
- **B002** anlam taşıyan tek söz birimi — anlamlı tek söz veya harf · en az üç sözden oluşan sözler topluluğu · sözler · bütün bir anlatı, şiir veya söylev · Tanrı'nın sözü · Tanrı'nın söylediği söz
  يسمون اللفظة الواحدة المفهمة كلمة والقصة كلمة والقصيدة بطولها كلمة ويجمعون الكلمة كلمات وكلما (maqayis)؛ الكلمة لغة حجازية والكلمة تميمية والجميع الكلم (ayn;tahdhib)؛ الكلام اسم جنس يقع على القليل والكثير والكلم لا يكون أقل من ثلاث كلمات والكلمة أيضا القصيدة بطولها (sihah)؛ الكلمة تقع على الحرف الواحد من حروف الهجاء وتقع على لفظة واحدة مؤلفة من جماعة حروف لها معنى وتقع على قصيدة بكمالها وخطبة بأسرها (tahdhib)؛ كلمة الله وكلام الله وكلم الله وكلمات الله (sihah;tahdhib)
- **B003** yaralama ve yara — yara · yaralar · yaralar · onu yaraladı · yaralayan · yaralanmış · yaralı kişi · yaralılar · yaralama · onları yaralayıp damgalaması
  الأصل الآخر الكلم وهو الجرح والكلام الجراحات وجمع الكلم كلوم (maqayis)؛ الكلم الجرح والجميع الكلوم وكلمته أكلمه كلما وأنا كالم وهو مكلوم أي جرحته (ayn)؛ الكلم الجراحة والجمع كلوم وكلام والتكليم التجريح (sihah)؛ الكلم الجرح والجميع كلوم وكلمته وأنا أكلمه كلما وأنا كالم وهو مكلوم (tahdhib)؛ تكلمهم فسر تجرحهم وتسمهم (sihah;tahdhib)

## س ب ق (root_000671): 41:45 سَبَقَتْ

- **B001** harekette ya da işte öne geçme ve yarışarak ön alma — koşuda, işte ya da bir şeyde başkasının önüne geçmek · öne geçme; koşuda ya da işte önce gelme · bir işte önceden kazanılmış öncelik · yarışma; koşuda ve benzeri bir alanda birbirini geçmeye çalışma · yarışmak ya da bir şeye önce davranmak · atış yarışmasına gitmek · kapıya ilk varmak için birbirinden önce davranmak · yolu aşıp geçerek yönünü kaybetmek · yarışta başa geçen at ya da benzeri varlık · iyi işlerle ödüle önden koşanlar · önceden kesinleşip yürürlüğe girmek
  أصل واحد صحيح يدل على التقديم (maqayis)؛ السبق القدمة في الجري وفي الأمر (ayn;tahdhib)؛ وسبق يسبق سبقا (jamhara)؛ سابقته فسبقته سبقا واستبقنا في العدو أي تسابقنا (sihah)؛ أصل السبق التقدم في السير والاستباق التسابق (mufradat)
- **B002** yarışta ortaya konup kazananın aldığı pay — yarışta ya da atışta ortaya konup kazananın aldığı pay · yarış payını almak ya da yarış payını vermek · ortaya konan yarış payını kazandı
  السبق الخطر الذي يأخذه السابق (maqayis)؛ السبق الخطر يوضع بين أهل السباق (ayn;sihah)؛ السبق الرهن (jamhara)؛ الخطر الذي يوضع في النضال والرهان في الخيل فمن سبق أخذه (tahdhib)
- **B003** avcı kuşun ayaklarına takılan iki bağ — avcı kuşun ayaklarına takılan iki bağ · avcı kuşun ayaklarına bu iki bağı takmak
  السباقان قيد أرجل الطائر الجارح بسير أو خيط (ayn)؛ سباقا البازي قيداه من سير أو غيره (sihah)؛ السباقان في رجل الطائر الجارح قيداه من سير أو خيط وسبقت البازي إذا جعلت السباقان في رجليه (tahdhib)
- **B004** yakalanmaktan kurtulacak kadar öne kaçma — takip edenin elinden kaçıp kurtulmak · kaçıp kurtulmuş olmamak; takip edeni aşamamış olmak
  وما نحن بمسبوقين أي لا يفوتوننا؛ ولا يحسبن الذين كفروا سبقوا؛ وما كانوا سابقين (mufradat)

## ش ك ك (root_000812): 41:45 شَكٍّ

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

## ر ي ب (root_000616): 41:45 مُرِيبٍ

- **B001** kuşku ve güvensizlik — kuşku ve zihinsel kararsızlık · suçlayıcı kuşku ve güven eksikliği · bende kuşku ve korku uyandırdı · bende kuşku uyandırdı · kuşkulu duruma geldi veya kuşku uyandırır oldu · ondan veya o şeyden kuşkulandı · onda kuşku uyandıran bir belirti gördü · kuşku duyan veya kuşku uyandıran
  الريب الشك (maqayis;ayn;jamhara;sihah)؛ الريب التهمة (jamhara)؛ ما رابك من أمر تخوفت عاقبته (ayn)؛ رابني هذا الأمر إذا أدخل عليك شكا وخوفا (maqayis;ayn)؛ الريبة اسم من الريب تدل على دغل وقلة يقين (mufradat)؛ أراب الرجل صار ذا ريبة (maqayis;ayn;sihah)؛ ارتبت به أي ظننت به (ayn)
- **B002** zamanın değişimleri ve olayları [kalıp] — zamanın değişimleri, olayları ve terslikleri · ölümün ne zaman geleceğine ilişkin korkulan olaylar
  ريب الدهر صروفه (maqayis;jamhara;mufradat)؛ الريب صرف الدهر وعرضه وحدثه (ayn)؛ ريب المنون حوادث الدهر (sihah)؛ ريب المنون من جهة وقته لا من جهة كونه (mufradat)
- **B003** karşılanması gereken gereksinim — elden kaçırma kaygısıyla aranan gereksinim
  الريب الحاجة (sihah)؛ فيقال إن الريب الحاجة (maqayis)؛ طالب الحاجة شاك على ما به من خوف الفوت (maqayis)

## ظ ل م (root_000967): 41:46 بِظَلَّٰمٍ

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

## ر د د (root_000555): 41:47 يُرَدُّ

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

## ECHO م ر د (root_001413): for 41:47 يُرَدُّ: withheld observed target; not identity

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

## س و ع (root_000760): 41:47 ٱلسَّاعَةِ, 41:50 ٱلسَّاعَةَ

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

## خ ر ج (root_000400): 41:47 تَخْرُجُ

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

## ث م ر (root_000205): 41:47 ثَمَرَٰتٍ

- **B001** agac yemisi — agacin yemisi; tekili ve cogulu olan yenebilir agac urunu · agacin yemisi cikti veya belirdi · yemis veren, yemisi olgunlasmis ya da yemisli agac · yemis olgunlasti ve olgun yemis durumuna geldi · tuzcul bir bitkinin kizil cicegi veya olgunlasan kizil yemisi
  الثمر معروف (maqayis;jamhara)؛ الثمر حمل الشجر (tahdhib)؛ اسم لكل ما يتطعم من أحمال الشجر (mufradat)؛ أثمر الشجر أي طلع ثمره (sihah;tahdhib)؛ الشجر الثامر الذي بلغ أوان يثمر (maqayis;jamhara)؛ شجر ثامر إذا أدرك ثمره وشجرة ثمراء ذات ثمر (sihah)؛ الثامر ما نضج (tahdhib)
- **B002** artan varlik — cok veya elde edilmis para ve varlik · kisi varligina iyi bakti ve onu ozenle yonetti · Tanri onun varligini artirsin diye dua etmek · kisi varlikli oldu veya varligi cogaldi
  ثَمَّر الرجل ماله أحسن القيام عليه (maqayis;jamhara)؛ ثَمَّر الله ماله أي نماه (maqayis;jamhara)؛ الثمر أيضا المال المثمر (sihah)؛ فسر بأنواع الأموال (sihah)؛ الثمر أنواع المال (tahdhib)؛ أثمر الرجل كثر ماله (sihah;tahdhib)؛ يكنى به عن المال المستفاد (mufradat)
- **B003** faydali sonuc — bir seyden dogan fayda veya sonuc · yararli sonuc ureten verimli zihin
  ويقال لكل نفع يصدر عن شيء ثمرة (mufradat)؛ ثمرة العلم العمل الصالح (mufradat)؛ ثمرة القلب (tahdhib)؛ العقل المثمر عقل المسلم (tahdhib)
- **B004** sutte yag tanesi — sutte toplanmadan once beliren veya tanelenen yag · tulumun uzerinde yag tanelenmesi belirdi · yag toplandi ve olustu · yayiklanmaya hazir olup ustunde yag taneleri beliren sut
  الثميرة من اللبن حين يثمر (maqayis)؛ ما يظهر من الزبد قبل أن يجتمع (sihah)؛ قد ثمر السقاء تثميرا وكذلك أثمر (sihah)؛ أثمر الزبد اجتمع (tahdhib)؛ إذا أدرك اللبن ليمخض فظهر عليه تحبب وزبد فهو المثمر (tahdhib)؛ الثميرة من اللبن ما تحبب من الزبد (mufradat)
- **B005** kamci ucu dugumu — kamcinin ucu veya uclarindaki dugum · dilin ucu
  عقدة السوط ثمرة (maqayis)؛ ثمر السياط عقد أطرافها (sihah)؛ أخذ بثمرة لسانه (tahdhib)؛ يريد طرف لسانه (tahdhib)؛ ثمرة السوط طرفه (tahdhib)؛ ثمرة السوط عقدة أطرافها (mufradat)
- **B006** aydinlik ay gecesi — ay isigiyla aydinlik geceyi bildiren sabit ad
  ليلة ابن ثمير وهي الليلة القمراء (maqayis)؛ ليلة ابن ثمير الليلة القمراء (jamhara)؛ ابن ثمير الليلة القمراء (sihah)

## ك م م (root_001319): 41:47 أَكْمَامِهَا

- **B001** kolu veya başı örten giysi parçası — gömleğin eli ve kolu örten kol kısmı · takke benzeri yuvarlak başlık · başlık taktı veya başını örttü · başını başlığa benzer bir örtüyle kapatan kadın
  الكمة وهي القلنسوة (maqayis)؛ والكم كم القميص (maqayis;ayn;tahdhib)؛ والكمة من القلانس (ayn;tahdhib)؛ الكمة: القلنسوة المدورة لأنها تغطي الرأس (sihah)؛ الكم: ما يغطي اليد من القميص، والكمة: ما يغطي الرأس كالقلنسوة (mufradat)
- **B002** bitki kılıfı ve bitkiyi kılıfa alma — tomurcuk, çiçek veya meyve kılıfı · tomurcuk ve meyve kılıfları · tomurcuk veya çiçek kılıfı · ağaç kılıfını çıkardı veya meyvesi ağırlaştı · ağaç tomurcuk ve meyve kılıflarını çıkardı · körpe sürgünü güçleninceye kadar özenle örttü · meyvesi taze kalsın ve kuşlarla sıcaktan korunsun diye örtülmüş salkım
  والكم وعاء الطلع والجمع الأكمام، والأكاميم أغطية النور، ويقال كم الفسيل إذا أشفق عليه فستر حتى يقوى (maqayis)؛ والكم الطلع، لكل شجرة كم وهو برعومته، وقد كمت النخلة كما وكموما (ayn)؛ والكم والكمة بالكسر والكمامة: وعاء الطلع وغطاء النور، وكمت النخلة فهي مكمومة، وكم الفسيل إذا أشفق عليه فستر حتى يقوى، وأكمت النخلة وكممت أي أخرجت كمامها (sihah)؛ وكل شجرة تخرج ما هو مكمم فهي ذات أكمام، وأكمام النخلة ما غطى جمارها، والمكموم من العذوق ما غطي (tahdhib)؛ والكم: ما يغطي الثمرة، وجمعه أكمام (mufradat)
- **B003** hayvanın ağız ve burun örtüsü — hayvanın ağzına veya burnuna geçirilen ağızlık · ağzına ağızlık geçirilmiş deve · eşeğin burnuna geçirilen torba biçimli ağızlık
  والكمام شيء يجعل في فم البعير أو البرذون لئلا يعض (ayn)؛ والكمام بالكسر والكمامة أيضا: ما يكم به فم البعير لئلا يعض، بعير مكموم (sihah)؛ الكمامة التي يجعلها على منخرها لئلا يؤذيها الذباب، والمغمة والمكمة شيء يوضع على أنف الحمار كالكيس (tahdhib)
- **B004** örtmek, sıkıca kapatmak veya bastırıp gizlemek — nesnenin üstünü örttü veya çamurla sıvadı · tanenin ya da kabın ağzını sıkıca bağladı · tulumun ağzını kapatıp çamurla sıvadı · tanıklığı bastırıp gizledi · toprağı kabarttı, ardından diş izlerini bir tahtayla silip düzeltti
  أصل واحد يدل على غشاء وغطاء (maqayis)؛ وكممت الشيء طينته (ayn)؛ وكممت الشيء: غطيته، وكممت الحب إذا شددت رأسه (sihah)؛ الكمة: كل ظرف غطيت به شيئا، وكممت رأس الدن أي سددته وطينته، وقيل كمت أي غطيت، والكم: قمع الشيء وستره، ومنه كميت الشهادة إذا قمعتها وسترتها (tahdhib)
- **B005** sıkı yapılı olma veya bir araya toplanma — sıkı ve toplu yapılı kimse · bir araya toplandılar
  ومن الباب الكمكام المجتمع الخلق (maqayis)؛ بل لو شهدت الناس إذ تكموا أي اجتمعوا (ayn)
- **B006** bunaltıcı bir örtü altında bilincini yitirmek — bunaltıcı bir örtüyle kaplanıp bayıldılar
  وتكموا أي أغمي عليهم وغطوا (sihah)؛ تكموا أي ألبسوا غمة كموا بها، والغمة ما غطاك من شيء (tahdhib)

## ح م ل (root_000357): 41:47 تَحْمِلُ

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

## ء ن ث (root_000058): 41:47 أُنثَىٰ

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

## و ض ع (root_001657): 41:47 تَضَعُ

- **B001** bir şeyi indirip yerine koyma; konduğu yer — bir şeyi yerine koymak veya elden bırakmak · yer, konum · yerine konmuş şey · ev yapmak veya kurmak · yazılı kayıtları ortaya çıkarmak
  أصل واحد يدل على الخفض للشيء وحطه (maqayis)؛ الوضع مصدر قولك وضع يضع (ayn)؛ الموضع المكان ومصدر وضعت الشيء من يدي (sihah)؛ وضعت الشيء أضعه وضعا وهو ضد رفعته (tahdhib)؛ الوضع أعم من الحط ومنه الموضع (mufradat)
- **B002** doğumla yükü bırakma ve özel gebe kalma zamanı — kadının çocuğunu doğurması · adet öncesi temizlik sonunda gebe kalma
  وضعت المرأة ولدها (maqayis)؛ وضعت المرأة وضعا بالفتح أي ولدت (sihah)؛ وضعت المرأة فهي تضع وضعا وتضعا فهي واضع (tahdhib)؛ وضعت المرأة الحمل وضعا (mufradat)؛ ما حملته أمه وضعا أي ما حملته على حيض (tahdhib)
- **B003** hayvanın hızlı ya da özel yürüyüşle ilerlemesi — bineğin hızlı gitmesi veya koşması · sürücünün bineği hızlandırması · bu yürüyüşü güzel olan
  الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع (maqayis)؛ الدابة تضع السير وضعا وهو سير دون (ayn)؛ وضع البعير وغيره أي أسرع في سيره (sihah)؛ وضع البعير إذا عدا وأوضعته أنا (tahdhib)؛ وضعت الدابة تضع في سيرها وضعا أسرعت (mufradat)
- **B004** ticarette zarar ve sermaye indirimi — ticarette zarar etmek · sermayeden düşülen indirim veya eksilti
  وضع في تجارته يوضع خسر (maqayis)؛ الوضيعة ما تضعه من رأس مالك (ayn)؛ وضع الرجل في تجارته خسر (sihah)؛ الوضيعة الحطيطة وقد استوضع (tahdhib)؛ الوضيعة الحطيطة من رأس المال (mufradat)
- **B005** düşük konum ve kendini alçaltma — düşük konumlu kişi · aşağı konum, düşüklük · kendini alçaltarak boyun eğme
  الوضيع الرجل الدني (maqayis)؛ الوضاعة الضعة (ayn)؛ الوضيع الدنئ من الناس وفي حسبه ضعة (sihah)؛ رجل وضيع ضد الشريف والتواضع التذلل (tahdhib)؛ رجل وضيع بين الضعة في مقابلة رفيع (mufradat)
- **B006** yerleştirilmiş topluluk, kayıtlı asker ya da yük — başka bir yere taşınıp yerleştirilen topluluklar · bölgeye kaydedilen askerler veya topluluğun yükleri
  الوضائع قوم ينقلون من أرض إلى أرض (maqayis)؛ الوضيعة نحو وضائع كسرى (ayn)؛ الوضيعة واحدة الوضائع وهي أثقال القوم (sihah)؛ الوضيعة قوم من الجند يجعل أسماؤهم في كورة (tahdhib)
- **B007** devenin tuzcul otu otlaması ve orada konaklaması — tuzcul otu otlayan veya yanında konaklayan dişi deve · tuzcul bitkiyi otlayan develer · tuzcul yemlik bitki veya develerin kaldığı otlak
  الواضعات الإبل تأكل الخلة (maqayis)؛ ناقة واضعة للتي ترعاها وأصحاب الوضيعة أصحاب حمض (sihah)؛ إبل واضعة أي مقيمة في الحمض (tahdhib)؛ الحمض يقال له الوضيعة والجمع وضائع (tahdhib)
- **B008** kumaşa pamuk serip dikme — kumaşa pamuk koyma veya sonra giysiyi dikme
  الخياط يوضع القطن على الثوب توضيعا (ayn)؛ التوضيع خياطة الجبة بعد وضع القطن (sihah)؛ الخياط يوضع القطن توضيعا على الثوب (tahdhib)
- **B009** baş örtüsünü çıkarıp baş örtüsüz kalma [kalıp] — baş örtüsünü çıkardığı için baş örtüsüz kadın
  وضعت المرأة خمارها وامرأة واضع أي لا خمار عليها (sihah)؛ امرأة واضع بغير هاء إذا وضعت خمارها (tahdhib)
- **B010** saklaması için birine bırakma [kalıp] — bir şeyi saklaması için birinin yanına bırakmak
  وضعت عند فلان وضيعا أي استودعته وديعة (sihah)؛ يقال للوديعة وضيع وقد وضعت عند فلان وضيعا إذا استودعته وديعة (tahdhib)
- **B011** karşılıklı anlaşma ve görüşme — bir işte karşılıklı anlaşmak ve onu görüşmek · karşılıklı para koymalı sözleşme veya satışı bırakma
  المواضعة أن تواضع أخاك أمرا فتناظره فيه (ayn)؛ المواضعة المراهنة والمواضعة متاركة البيع وواضعته في الأمر (sihah)؛ المواضعة أن تواضع صاحبك أمرا تناظره فيه (tahdhib)
- **B012** sağlamlık eksikliği ve kusurlu yumuşama — işi veya yapısı sağlam olmayan, kadınsı sayılan kişi · kadın konuşmasına benzetilen yumuşama · alt bacağını yayarak yürüyen kusurlu at
  الرجل الموضع الذي ليس بمستحكم الأمر (maqayis)؛ في كلامه توضيع إذا كان فيه تأنيث كلام النساء (ayn)؛ رجل موضع أي مطرح ليس بمستحكم الخلق (sihah)؛ يقال في فلان توضيع أي تخنيث وفلان موضع إذا كان مخنثا (tahdhib)؛ فرس موضع إذا كان يفترش وظيفه وهو عيب (tahdhib)
- **B013** binmek için devenin boynunu alçaltma — binmek için devenin boynunu veya başını alçaltması
  الاتضاع أن تخفض رأس البعير لتضع قدمك على عنقه فتركب (sihah)؛ اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه (tahdhib)

## ح ي ص (root_000378): 41:48 مَّحِيصٍ

- **B001** bir şeyden sapıp başka yöne dönme — bir şeyden ya da doğrudan sapmak, başka yöne dönmek · sapma, kaçamaklı yön değiştirme ve geri kalma · uzaklaşılacak yön, çıkış ya da kaçış yolu · amaçlanan yönden sapma · sapma ve başka yöne dönme · yön değiştirme ve sapma · bir şeyden sapma ve uzaklaşma
  الحاء والياء والصاد أصل واحد وهو الميل في جور وتلدد (maqayis)؛ حاص عن الحق يحيص حيصا إذا جار (maqayis)؛ الحيص الحيد عن الشيء والمحيص المحيد (ayn)؛ حاص عنه يحيص حيصا وحيوصا ومحيصا ومحاصا وحيصانا أي عدل وحاد (sihah)؛ ما عنه محيص أي محيد ومهرب (sihah)؛ الحيص الرواغ والتخلف (sihah)؛ حاص عن الحق يحيص أي حاد عنه إلى شدة ومكروه (mufradat)
- **B002** ağır bir sıkıntıya düşme — darlık, sıkışıklık · içinden çıkılamayan karışık ve sıkıntılı durum
  وقعوا في حيص بيص أي شدة (maqayis)؛ حيص بيص يتكلم به عند اختلاط الأمر أي فيما لا أقدر على الخروج منه أي في ضيق وأصل الحيص الضيق (ayn)؛ وقع في حيص بيص إذا وقع في أمر لا يتخلص منه (jamhara)؛ وقعوا في حيص بيص أي في اختلاط من أمرهم لا مخرج لهم منه ويقال في ضيق وشدة (sihah)؛ أصله من حيص بيص أي شدة (mufradat)

## م س س (root_001423): 41:49 مَّسَّهُ, 41:50 مَسَّتْهُ, 41:51 مَسَّهُ

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

## ش ر ر (root_000787): 41:49 ٱلشَّرُّ, 41:51 ٱلشَّرُّ

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## ECHO ش ر ي (root_000792): for 41:49 ٱلشَّرُّ, 41:51 ٱلشَّرُّ: withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

## ي ء س (root_001690): 41:49 فَيَـُٔوسٌ

- **B001** umudu kesme veya birine umudunu kestirme — umudu kesme, umutsuzluk · umudunu kesmek, umutsuzluğa düşmek · umudunu kesmek, umutsuzluğa düşmek · büsbütün umudunu kesmek · birine bir şeyden umudunu kestirmek · umudu kesme, umutsuzluk · çok umutsuz, umudunu çabuk kesen · umudunu kesmek
  اليأس قطع الرجاء (maqayis)؛ اليأس ضد الرجاء (jamhara)؛ اليأس القنوط (sihah)؛ اليأس انتفاء الطمع (mufradat)؛ آيسه فلان من كذا فاستيأس منه بمعنى أيس (sihah)؛ أيس يأيس وآيسته أي أيأسته وهو اليأس والإياس (tahdhib)
- **B002** bilme diye açıklanan tartışmalı kullanım — 
  ألم تيأس أي ألم تعلم (maqayis)؛ يئس أيضا بمعنى علم في لغة النخع (sihah)؛ أفلم ييأس أفلم يعلم (tahdhib)؛ ييأس بمعنى يعلم لغة للنخع (tahdhib)؛ ولم يرد أن اليأس موضوع في كلامهم للعلم (mufradat)

## ق ن ط (root_001261): 41:49 قَنُوطٌ

- **B001** umudu kesmek — bir şeyden, iyilikten ya da Tanrı'nın esirgemesinden umudu kesmek · iyilikten umudu kesme; umutsuzluk · umudunu kesmiş, umutsuz · umudunu kesmiş kimse · umudu kesme, umutsuzluk · insanların Tanrı'nın bağışlayıcılığından umutlarını kesmelerine yol açmak
  تدل على اليأس من الشيء (maqayis)؛ القنوط الإياس (ayn)؛ القنوط اليأس (sihah)؛ القنوط الإياس من الخير (tahdhib)؛ يقنطون الناس من رحمة الله أي يؤيسونهم (tahdhib)؛ القنوط اليأس من الخير (mufradat)

## ض ر ر (root_000907): 41:50 ضَرَّآءَ

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

## ن ب ء (root_001464): 41:50 فَلَنُنَبِّئَنَّ

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

## غ ل ظ (root_001099): 41:50 غَلِيظٍ

- **B001** kalınlaşma ve kalınlık — kalınlaşmak · kalın, yoğun · kalınlaşmaya hazırlanmak veya kalınlaşmak · kumaşı kalın bulmak · kumaşı kalın olarak satın almak · kalın olduğu için satın almamak · kalınlık; inceliğin karşıtı
  غلظ الشيء غلظا فهو غليظ (ayn)؛ واستغلظ النبات والشجر (ayn)؛ غلظ الشئ يغلظ غلظا: صار غليظا، واستغلظ مثله (sihah)؛ الغلظة ضد الرقة، وأصله أن يستعمل في الأجسام (mufradat)؛ استغلظ تهيأ لذلك، وقد يقال إذا غلظ (mufradat)
- **B002** kaba ve sert davranma; çok ağır olma — sertlik ve kabalık · kabalık ve sertlik · ona sert ve kaba söz söylemek · ona karşı sertleşmek ve kaba davranmak · ağır ve çetin iş · ağır ceza · onlara karşı sert davranmak
  غلظت عليه وأغلظت له في المنطق (ayn)؛ وأمر غليظ (ayn)؛ رجل فيه غلظة وغلاظة أي فيه فظاظة، وأغلظ له في القول (sihah)؛ وليجدوا فيكم غلظة أي خشونة، وعذاب غليظ، واغلظ عليهم (mufradat)
- **B003** antı veya can bedelini ağırlaştırma [kalıp] — antı ağırlaştırma · ağırlaştırılmış ant · kasıt benzeri öldürmede gereken ağırlaştırılmış can bedeli
  التغليظ الشدة في اليمين (ayn)؛ اليمين المغلظة، ومنه الدية المغلظة التي تجب في شبه العمد (sihah)

## ن ع م (root_001525): 41:51 أَنْعَمْنَا

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

## ن ء ي (root_001463): 41:51 وَنَـَٔا

- **B001** uzak olma, uzaklaşma, uzaklaştırma ve uzak yer — uzak olmak veya uzaklaşmak · bir şeyi bulunduğu yerden uzaklaştırmak · birini veya bir şeyi uzaklaştırıp uzaklaşmasına yol açmak · uzaklaşmak · birbirinden uzaklaşmak · uzak yer · sesleri yer değiştirmiş biçimiyle uzaklaşmak · uzakta bulunan
  النأي فالبعد؛ نأى ينأى نأيا وانتأي؛ المنتأى الموضع البعيد؛ ناء وإنما هو نأى (maqayis)؛ النأي البعد؛ أنأيته إنئاء؛ نأيت الدمع عن عيني بإصبعي؛ الانتياء الافتعال من النأي؛ ناء عني على القلب (ayn)؛ نأى ينأى نأيا إذا بعد؛ النائي البعيد (jamhara)؛ نأيته ونأيت عنه نأيا؛ أنأيته فانتأى؛ تناءوا أي تباعدوا؛ المنتأى الموضع البعيد (sihah)؛ نأى ينأى نأيا؛ تباعد؛ انتأى؛ المنتأى الموضع البعيد (mufradat)
- **B002** yanını çevirerek yüz çevirmek veya uzaklaşmak [kalıp] — yanını çevirerek yüz çevirmek veya uzaklaşmak; bağlama göre kibir göstermek
  نأى بجانبه؛ أعرض؛ تباعد؛ نأى بجانبه أي نهض به عبارة عن التكبر؛ ناء بجانبه أي تباعد
- **B003** yağmur suyunu konuttan uzak tutan çevre çukuru veya toprak engel — yağmur suyunu uzak tutmak için çadırın veya evin çevresine açılan çukur ya da yapılan toprak engel · çadırın çevresine su çukuru veya toprak engel yapmak · evin veya çadırın çevresine su çukuru ya da toprak engel yapmak · çevre su engelini yapmak veya onarmak · çevre çukurunun veya toprak engelin bulunduğu yer
  النؤى حفيرة حول الخباء يدفع ماء المطر عن الخباء (maqayis)؛ النؤي حفرة تحفر حول الخباء؛ المنتأى موضعه (ayn)؛ النؤي حاجز من التراب يطيف بالبيت ليمنع الماء أن يدخله (jamhara)؛ النؤي حفيرة حول الخباء لئلا يدخله ماء المطر؛ نؤيك أي أصلحه (sihah)؛ النؤي حفيرة حول الخباء تباعد الماء عنه (mufradat)

## ج ن ب (root_000262): 41:51 بِجَانِبِهِۦ

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

## ش ق ق (root_000807): 41:52 شِقَاقٍۭ

- **B001** yarma, yarılma ve açılma — bir şeyi yarıp açmak veya ikiye ayırmak · çatlak, yarık veya delik · dağda, yerde veya başka bir şeydeki çatlaklar · derinin çatlaması veya hayvanın bileklerindeki çatlak hastalığı · dişin çıkması veya tanın sökmesi
  شققت الشيء أشقه شقا إذا صدعته (maqayis); الشق مصدر قولك شققت والشقاق تشقق الجلد والصدوع في الجبال والأرضين (tahdhib); الشق الخرم الواقع في الشيء وشققته بنصفين (mufradat); شققت الشيء فانشق وشققت الحطب وغيره فتشقق وشق ناب البعير وشق الفجران (sihah;tahdhib)
- **B002** yarım veya yan — bir şeyin yarısı veya yanı · öz kardeş, denk veya insanın öteki yarısı · başın ve yüzün bir yarısını tutan ağrı, migren
  يقال لنصف الشيء الشق والشق أيضا الناحية من الجبل والشق الشقيق وشق نفسي (maqayis); الشق بالكسر نصف الشيء والشق أيضا الناحية من الجبل والشق أيضا الشقيق والشقيقة وجع يأخذ نصف الرأس والوجه (sihah); الشق الجانب والشق الشقيق وخذ هذا الشق لشقة الشاة والشقيقة صداع يأخذ في نصف الرأس والوجه (tahdhib); شققته بنصفين (mufradat)
- **B003** ağır güçlük ve çaba — ağır iş, güçlük ve yoğun çaba · bütün gücünü zorlayarak, çok güçlükle · bir işin kişiye ağır gelmesi
  أصاب فلانا شق ومشقة وذلك الأمر الشديد (maqayis); الشق المشقة ومنه بالغيه إلا بشق الأنفس (sihah); الشق المشقة في السير والعمل ومعناه إلا بجهد الأنفس وشق علي ذاك الأمر مشقة أي ثقل علي (tahdhib)
- **B004** anlaşmazlıkla bölünüp ayrılma — anlaşmazlık, düşmanlık ve topluluktan ayrılma · birliği bozup topluluktan ayrılmak
  الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت وشقوا عصا المسلمين (maqayis); شق فلان العصا أي فارق الجماعة والمشاقة والشقاق الخلاف والعداوة (sihah); الشقاق العداوة بين فريقين والخلاف بين اثنين وشق الخوارج عصا المسلمين (tahdhib)
- **B005** uzak yol ve uzun yolculuk — uzun yolculuk veya uzak yol mesafesi · uzak ve aşılması güç yol
  الشقة مسير بعيد إلى أرض نطية وهذه شقة شاقة ولكن بعدت عليهم الشقة (maqayis); الشقة أيضا السفر البعيد وشقة شاقة (sihah); الشقة بعد مسير إلى الأرض البعيدة يقال شقة شاقة (tahdhib)
- **B006** yarılıp ayrılmış parça — tahtadan kopan kıymık veya bir kumaş parçası · çok öfkelenip çılgına dönmek
  الشقة شظية تشظى من لوح أو خشبة وفطارت منه شقة والشقة من الثياب (maqayis); الشقة شظية تشظى من لوح أو خشبة والشقة بالضم من الثياب (sihah); الشقة شظية تشق من لوح أو خشبة وشقة في الأرض وشقة في السماء والشقة معروفة في الثياب (tahdhib)
- **B007** kum sırtları arasındaki otlu açıklık — kum sırtları arasında ot bitiren açıklık veya sert toprak · kırmızı anemon çiçeği · bol yağmur taşıyan bulutlar
  الشقيقة فرجة بين الرمال تنبت والشقيقة أرض غليظة بين حبلين من الرمل (maqayis); الشقيقة الفرجة بين الحبلين من حبال الرمل تنبت العشب وشقائق النعمان معروف (sihah); الشقيقة الفرجة بين الرمال تنبت العشب ونور أحمر يسمى شقائق النعمان والشقائق أيضا سحائب (tahdhib)
- **B008** devenin böğürme kesesi — devenin böğürürken ağzından çıkardığı boğaz dokusu · gür sesli ve sözünde usta hatip · erkek devenin böğürmesi veya kuşun özel ötüşü
  الشقشقة لهاة البعير ويقال للخطيب هو شقشقة (maqayis); شقشق الفحل شقشقة هدر والعصفور يشقشق والشقشقة شيء كالرئة يخرجها البعير وإذا قالوا للخطيب ذو شقشقة (sihah); الشقشقة لهاة الجمل وجمعها الشقاشق والخطيب الجهير الصوت هرت الشقاشق (tahdhib)
- **B009** amaç çizgisinden yana sapma — konuşmada veya tartışmada ana amaçtan sağa sola sapmak · koşarken bir yanına eğilen at
  اشتق في الكلام في الخصومات يمينا وشمالا مع ترك القصد وفرس أشق إذا مال في أحد شقيه عند عدوه (maqayis); الاشتقاق الأخذ في الكلام وفي الخصومة يمينا وشمالا وفرس أشق (sihah); الاشتقاق الأخذ في الخصومات يمينا وشمالا وفرس أشق وقد اشتق في عدوه (tahdhib)
- **B010** uzun veya bacak arası geniş at — uzun veya bacak arası geniş at; ayrıca zayıflayıp incelmek
  فرس أشق أي طويل والأنثى شقاء (sihah); فرس أشق له معنيان الأشق الطويل والأشق من الخيل الواسع ما بين الرجلين وتشقق الفرس تشققا إذا ضمر (tahdhib)

## ECHO ش ق و (root_000808): for 41:52 شِقَاقٍۭ: withheld observed target; not identity

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ن ش ق (root_001506): for 41:52 شِقَاقٍۭ: withheld observed target; not identity

- **B001** bir bağa takılıp tutulma — tuzağa veya ipe takılıp kalmak · yavruların boynuna geçirilen bağ veya boyun bağı halkası · içinden kolayca çıkamayacağı bir işe düşmüş kişi · boyun bağının halkaları · onu ipe takıp tutmak · avının boynuna tuzak bağı geçen avcı · av paylaşımında boyun halkasına yakalanan pay
  أصل صحيح يدل على نشوب شيء (maqayis)؛ نشق الظبي في الحبالة علق فيها والنشقة حبل يجعل في أعناق البهم (maqayis)؛ رجل نشق إذا وقع في أمر لا يكاد يخلص منه (maqayis)؛ نشب الصيد في حبله ونشق وعلق وارتبق (tahdhib)؛ لحلق الربق نشق واحدها نشقة (tahdhib)
- **B002** burundan ilaç uygulama — ilacı veya burun ilacını buruna dökmek · burun deliklerine konup burundan alınan ilaç · burun ilacını buruna dökme · yakılmış pamuğu burna yaklaştırıp kokusunu içeri aldırmak · ilacı burundan almak · ilacı burundan içeri çekmek
  أنشقت الصبي الدواء صببته في أنفه (maqayis)؛ النشوق اسم لكل دواء ينشق (maqayis;tahdhib)؛ النشق صب سعوط في الأنف وأنشقته الدواء (ayn;tahdhib)؛ أنشقته قطنة محرقة أي أدنيتها من أنفه ليدخل ريحها في أنفه وخياشيمه (ayn;tahdhib)؛ النشوق سعوط يجعل في المنخرين (tahdhib)
- **B003** kokuyu burundan algılama [kalıp] — esintiyi veya kokuyu koklamak · koklaması hoş olmayan koku · birinden hoş bir koku almak
  استنشقت الريح تشممتها (maqayis;tahdhib)؛ ريح مكروهة النشق أي الشم (maqayis;ayn;tahdhib)؛ استنشقته أي تشممته (ayn)؛ نشقت من الرجل ريحا طيبة (tahdhib)
- **B004** suyu burnuna çekme [kalıp] — suyu burnuna çekip iç burun kanallarına ulaştırmak
  المتوضىء يستنشق الماء عند استنثاره (maqayis)؛ استنشقت الماء مددته بريح الأنف (ayn)؛ المتوضىء يستنشق إذا أبلغ الماء خياشيمه (tahdhib)
- **B005** umduğunu bulamayacağını söyleyerek geri çevirme — umduğunu bulamayacaksın diyerek isteğini geri çevirmek
  استنشق الريح فإنك لا تجد ما ترجو إذا أراد شيئا فخيبته (ayn)

## ء ف ق (root_000040): 41:53 ٱلْءَافَاقِ

- **B001** uzak yönler ve kenarlar — uzak yönler, kenarlar ve sınır bölgeleri · gök ve yerin görüş sınırındaki yönleri · çadır evinin üst yapısının altındaki yanı · yolun yüzü veya izlenecek yönü · uzak bölgelerden olan; yıldız için görüş sınırına yakın seyreden
  الآفاق النواحي والأطراف (maqayis;sihah;mufradat); واحد الآفاق أفق وهي النواحي من الأرض وآفاق السماء نواحيها (ayn;tahdhib); أفق البيت ما دون سمكه (ayn;tahdhib); أفق الطريق وجهه ومنهاجه (maqayis;tahdhib); رجل أفقي من أهل الآفاق (maqayis;sihah;tahdhib;mufradat)
- **B002** uzak bölgelere gitmek — adamın yeryüzünde ve uzak bölgelerde gitmesi · uzak yönlerden almak veya toplamak · uzak bir yönden gelmek, uğramak · kazanç için yeryüzünün uzak bölgelerinde dolaşmak
  أفق الرجل إذا ذهب في الأرض (maqayis;sihah); ركب رأسه فمضى في الآفاق (ayn;tahdhib); يأخذ من الآفاق (ayn;tahdhib); تأفق إذا جاء من أفق وألم بنا (tahdhib); أفاق يضرب في آفاق الأرض كاسبا (tahdhib); أفق فلان إذا ذهب في الآفاق (mufradat)
- **B003** üstün derecede olmak — cömertlikte, bilgide veya iyilikte son dereceye varmış kimse · üstün gelmek, faziletle geçmek · üstün gelme · vermede bazılarına daha fazla pay ayırmak · fazilet bakımından başkasını geçmek
  الآفق الذي بلغ النهاية في الكرم (maqayis;sihah;mufradat); الآفق الذي بلغ في العلم الغاية وفي غيره من أبواب الخير (tahdhib); أفق يأفق أفقا إذا غلب (maqayis;tahdhib); يأفق يفضل وأفقه إذا سبقه بالفضل (tahdhib); أفق في العطاء أي فضل وأعطى بعضا أكثر (sihah)
- **B004** soylu ve etkileyici hayvan [kalıp] — etkileyici, soylu ve iyi nitelikli at veya deve
  فرس أفق أي رائعة (maqayis;sihah;tahdhib); بعير آفق وفرس آفق إذا كان رائعا كريما (tahdhib); فرس آفق قوبل من آفق وآفقة إذا كان كريم الطرفين (sihah)
- **B005** işlenme aşamasındaki deri — işlenme sürecindeki ara veya yeni işlenmiş deri · deriyi bu ara işlenmiş hale getirmek
  الأفيق الأديم إذا فرغ من دباغه وريحه فيه بعد (ayn); الجلد الذي لم تتم دباغته (sihah); الجلد أول ما يدبغ فهو منيئة ثم أفيق ثم يكون أديما (tahdhib); الجلد بعد الدبغ الأفيق وجمعه أفق (maqayis); أفقته وقد أفق أديمه (sihah;tahdhib)
- **B006** deri kenarı parçası — hayvan derisinin yumuşak kenar parçası
  الأفقة مرقة من مرق الإهاب (ayn;tahdhib)
- **B007** böğür — böğür; çoğul olarak beden yanları
  الأفقة الخاصرة والجماعة الأفق (maqayis); الأفقة الخاصرة (tahdhib)
- **B008** üstün nitelikli kova [kalıp] — diğer kovalardan üstün veya daha iyi kova
  دلو أفيق إذا كانت فاضلة على الدلاء (maqayis)
- **B009** belirli bir yer adı — belirli bir yer adı · bu yere bağlı belirli bir gün adı
  أفاقة موضع (maqayis); أفاقة موضع ذكره لبيد (tahdhib); يوم الأفاقة (maqayis)

## ك ف ي (root_001310): 41:53 يَكْفِ

- **B001** işi görüp ihtiyacı karşılamak — işi üstlenip ihtiyacı karşılayacak sonucu sağlamak · açığı kapatıp amacı gerçekleştirecek yeterlilik · onu yeterli bulup onunla yetinmek · birinden bir işi üstlenip yerine getirmesini istemek · Tanrı'nın yeterli olması ya da Tanrı'yı yeterli görmek · gereken işi görmeye yeterli kişi
  كفاك الشىء يكفيك وقد كفى كفاية إذا قام بالأمر (maqayis)؛ كفى يكفي كفاية إذا قام بالأمر (ayn;tahdhib)؛ كفاه مؤنته كفاية واكتفيت به واستكفيته الشئ فكفانيه (sihah)؛ الكفاية ما فيه سد الخلة وبلوغ المراد في الأمر (mufradat)
- **B002** sana yeter demek; kendi türünde yeterli saymak — bu sana yeter · adam olarak sana yeter; yeterli bir adamdır · sana yeter
  حسبك زيد من رجل وكافيك (maqayis)؛ كفاك هذا أي حسبك ورجلا كافيك من رجل (ayn;tahdhib)؛ كافيك من رجل وكَفْيُك بتسكين الفاء أي حسبك (sihah)؛ كافيك فلان من رجل كقولك حسبك من رجل (mufradat)
- **B003** ihtiyaca yetecek azık — ihtiyaca yetecek azık · ihtiyaca yetecek azıklar
  الكُفْية القوت (maqayis)؛ الكُفْية بالضم القوت والجمع الكُفَى (sihah)؛ الكُفَى الأقوات واحدتها كُفْية (tahdhib)؛ الكُفْية من القوت ما فيه كفاية والجمع كُفَى (mufradat)
- **B004** vadi tabanı — vadi tabanı · vadi tabanları
  الكَفِيّ بطن الوادي والجميع الأكفاء (tahdhib)

## ECHO ك ف ف (root_001308): for 41:53 يَكْفِ: withheld observed target; not identity

- **B001** avuç ve ona benzer kavrayıcı organ — avuç · kuşun tuttuğunu kavrayan ayak bölümü
  الكف للإنسان لأنها تقبض الشيء (maqayis)؛ الكف كف اليد (ayn;tahdhib)؛ الكف في اليد معروفة (jamhara)؛ الكف واحدة الأكف (sihah)؛ الكف كف الإنسان وهي ما بها يقبض ويبسط (mufradat)؛ كف الطائر لأنه يكف بها على ما أخذ (jamhara)
- **B002** geri durmak veya alıkoymak — bir şeyden geri durmak · birini bir şeyden alıkoymak · geri çevirmek ve durdurmak · gözyaşını tutmak
  كففت فلانا عن الأمر وكفكفته (maqayis)؛ كف الرجل عن أمر كذا وكففته (ayn)؛ كففت عن الشيء إذا امتنعت عنه (jamhara)؛ كففت الرجل عن الشيء فكف (sihah)؛ كففت فلانا عن السوء (tahdhib)؛ الكفكفة ردك الشيء عن الشيء (ayn;tahdhib)؛ تعورف الكف بالدفع (mufradat)
- **B003** toplayıp çevreleyerek kapatmak — toplamak veya çevresini kuşatmak · bir bezle sarmak · içindekilerin üzerine kapatılıp bağlanmış kap
  كل شيء جمعته فقد كففته (jamhara)؛ كفه بخرقة أي اجعلها حوله (jamhara)؛ أحيط الجمر بأجذال (jamhara)؛ عيبة مكفوفة أي مشرجة مشدودة (sihah)؛ عيبة مكفوفة التي أشرجت على ما فيها (tahdhib)؛ الشر مكفوفا كما نكف العيبة (tahdhib)
- **B004** belirli bir nesnenin çevresel kenarı [kalıp] — giysinin etek ucu veya kenarı · giysinin kenarları · diş etinin diş diplerine inen eteği · bulutun kenarı · kumluğun kıyısı · dağın çıkıntılı sırtları ve yanları
  كفة الثوب وحاشيته وكفة الرمل (maqayis)؛ كفة اللثة ما انحدر منها (ayn;tahdhib)؛ كفة السحاب وكفافه نواحيه (ayn;tahdhib)؛ كفاف الثوب نواحيه (ayn;tahdhib)؛ كفة القميص ما استدار حول الذيل (sihah)؛ كفة الرمل والقميص فطرتهما وما حولهما (tahdhib)؛ أكافيف الجبل حيوده (tahdhib)؛ كففت الثوب إذا خطت نواحيه (mufradat)
- **B005** taşıyan veya çevreleyen yuvarlak araç bölümü [kalıp] — terazinin tartılan nesneyi taşıyan gözü · avı çevreleyen halka biçimli tuzak · fırlatma aracının yükü tutan yuvası
  كل ما استدار فهو كفة نحو كفة الميزان وكفة الصائد (maqayis)؛ كفة الميزان التي توضع فيها الدراهم والكفة ما يصاد به الظبي (ayn)؛ كفة الميزان والمنجنيق (jamhara)؛ كفة الميزان وكفة الصائد وهي حبالته (sihah)؛ كفة الحبالة يجعل كالطوق (tahdhib)؛ كفة الميزان تشبيه بالكف وكذا كفة الحبالة (mufradat)
- **B006** bütünü eksiksiz kapsayan — 
  الناس كافة كلهم داخل فيه (ayn)؛ الكافة الجميع من الناس (sihah)؛ كافة بمعنى الجميع والإحاطة (tahdhib)؛ ادخلوا في السلم كله أي في جميع شرائعه (tahdhib)؛ الجماعة يقال لهم الكافة (mufradat)
- **B007** fazlasız yeter geçimlik — fazlası olmayan yeterli geçimlik
  كفاف الرزق القوت وهو ما كف عن الناس (sihah)؛ نفقته الكفاف أي ليس فيها فضل (tahdhib)؛ ما يكف وجهه عن الناس (tahdhib)؛ لا تلام على كفاف (tahdhib)
- **B008** görme yetisini yitirme — görme yetisini yitirmiş kişi · görme yetisi yok olmak
  المكفوف الأعمى (maqayis;tahdhib)؛ المكفوف الذاهب البصر (ayn)؛ المكفوف الضرير (sihah)؛ كف بصره (sihah;tahdhib)؛ رجل مكفوف لمن قبض بصره (mufradat)
- **B009** el açarak istemek — el açıp istemek · isteyen kişinin elini açması
  يستكف ويتكفف (maqayis)؛ استكف السائل بسط يده (ayn)؛ يمد كفه يسأل الناس (sihah)؛ يتكففون الناس معناه يسألون الناس بأكفهم (tahdhib)؛ تكفف الرجل إذا مد يده سائلا (mufradat)
- **B010** görebilmek için eli göze siper etmek — görebilmek için eli kaş üstüne siper etmek · güneşe karşı eliyle gölge yapmak
  استكففت الشيء وهو أن تضع يدك على حاجبيك (maqayis)؛ تضع يدك على حاجبك كالذي يستظل من الشمس (sihah;tahdhib)؛ استكف الشمس دفعها بكفه (mufradat)؛ يضع كفه على حاجبه مستظلا من الشمس ليرى ما يطلبه (mufradat)
- **B011** yüz yüze karşılaşma [kalıp] — yüz yüze veya ansızın karşılaşma · yüz yüze karşılaşma
  لقيته كفة كفة إذا فاجأته كأن كفك مست كفه (maqayis)؛ لقيته كفة لكفة وكفة عن كفة أي مفاجأة مواجهة (ayn)؛ لقيته كفة كفة أي كفاحا إذا استقبلته مواجهة (sihah)؛ لقيته كفة كفة وكفة لكفة أي مواجهة (tahdhib)
- **B012** çevresini kuşatıp bakmak [kalıp] — bir şeyin çevresinde toplanıp ona bakmak
  استكف القوم حول الشيء إذا داروا به ناظرين إليه (maqayis)؛ استكف القوم بالشيء أحدقوا به (ayn)؛ استكف القوم حول الشيء أي أحاطوا به ينظرون إليه (sihah)؛ استكف به الناس إذا عصبوا به (tahdhib)؛ استكفت الحية إذا ترحت كالكفة (tahdhib)
- **B013** dişleri yaşlılıktan tükenmek üzere olan deve — dişleri yaşlılıktan kısalıp tükenmek üzere olan deve
  يقال للبعير إذا كبر فقصرت أسنانه حتى تكاد تذهب هو كاف (sihah)؛ بعير كاف وكذلك الأنثى بغير هاء وقد كفت أسنانها (tahdhib)
- **B014** dövmedeki daire biçimli izler [kalıp] — dövmedeki halka biçimli izler
  الكفف في الوشم دارات تكون فيه (maqayis)؛ الكفف في الوشم دارات تكون فيه (sihah)
- **B015** mefâîlün kalıbının son n sesini düşürerek mefâîl yapma [kalıp] — klasik şiir ölçüsünde mefâîlün kalıbının son n sesi düşürülerek oluşan mefâîl biçimi
  المكفوف في علل العروض مفاعيل كان أصله مفاعيلن فلما ذهبت النون (ayn;tahdhib)
- **B016** ölçüce denk ve tam uyumlu olma [kalıp] — bir şeyin dengi ve ölçüde karşılığı · etin deriyi taşmadan tam doldurması
  كفاف الشيء بالفتح مثله وقيسه (sihah)؛ لحمه كفاف لأديمه إذا امتلأ جلده من لحمه (tahdhib)؛ كفاف اللحم (tahdhib)

## م ر ي (root_001416): 41:54 مِرْيَةٍ

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

## ECHO م و ر (root_001456): for 41:54 مِرْيَةٍ: withheld observed target; not identity

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

## ح و ط (root_000372): 41:54 مُّحِيطٌۢ

- **B001** fiziksel olarak çevresini sarma — bir şeyin çevresini fiziksel olarak sardı · çevresine duvar ördü · bir yeri çevreleyen duvar · yiyecek için yapılmış çevrili saklama yeri · atlar kişinin çevresini sardı
  هو الشيء يطيف بالشيء (maqayis)؛ احتاطت الخيل بفلان وأحاطت به أي أحدقت (ayn;sihah;tahdhib)؛ الحائط لأنه يحوط ما فيه وحوطت حائطا (ayn;tahdhib)؛ الحائط الجدار الذي يحوط بالمكان (mufradat)؛ الحواطة حظيرة تتخذ للطعام (maqayis;sihah)
- **B002** koruyup gözetme — onu koruyup gözetti · koruma, gözetme ve sürekli ilgilenme · güvenli yolu seçerek önlem alma · sana karşı şefkat ve yakınlık besliyor · alıkonulmanız dışında · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  حطت الرجل أحوطه حوطا إذا حفظته (jamhara)؛ حاطه حيطة إذا تعاهده (ayn;tahdhib)؛ كلأه ورعاه (sihah)؛ الحياطة الحفظ والاحتياط استعمال ما فيه الحياطة (mufradat)؛ تستعمل في المنع (mufradat)؛ مع فلان حيطة لك أي تحنن وتعطف (sihah)
- **B003** eşeğin sürüsünü bir araya toplaması [kalıp] — eşek kendi sürüsünü toplayıp bir araya sürdü
  الحمار يحوط عانته يجمعها (maqayis;ayn;sihah;tahdhib)
- **B004** bir şeyi bütünüyle bilme veya elde etme [kalıp] — onu bütün yönleriyle eksiksiz bildi · şeyin tamamını elde edip denetim altına aldı · hakkında eksiksiz bilgi edinmediği şey
  كل من أحرز شيئا كله وبلغ علمه أقصاه فقد أحاط به (ayn;tahdhib)؛ أحاط به علما (sihah)؛ الإحاطة بالشيء علما هي أن تعلم وجوده وجنسه وقدره وكيفيته (mufradat)
- **B005** çevresinde dönme veya dolaylı yoldan razı etmeye çalışma — o işin çevresinde dönüp duruyorum · istemediği bir şeyi ondan elde etmek için dolaylı yollardan uğraştı
  أنا أحوط حول ذلك الأمر أي أدور (sihah)؛ حاوطت فلانا محاوطة إذا داورته في أمر تريده منه وهو يأباه (tahdhib)
- **B006** karşı konulmaz bir güçle kuşatılıp yıkıma sürüklenme [kalıp] — sonunu getirecek bir gücün altında kaldı · ürünü yok olup bozuldu · karşı koyamayacakları bir güçle kuşatıldılar
  أحيط بفلان إذا دنا هلاكه فهو محاط به (tahdhib)؛ أصابه ما أهلكه وأفسده (tahdhib)؛ أحيط بهم فذلك إحاطة بالقدرة (mufradat)
- **B007** yuvarlak veya hilal biçimli gümüş süs — yuvarlak gümüş süs veya boncuklu iki renkli ipteki gümüş hilal · çocuğa gümüş hilal biçimli süs taktı · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  الحوط شيء مستدير تعلقه المرأة على جبينها من فضة (maqayis)؛ الحوط خيط مفتول من لونين أحمر وأسود وهلال من فضة (tahdhib)؛ أن يحلي صبيه بالحوط وهو هلال من فضة (tahdhib)
- **B008** eksik para tutarını tamamlayan ek miktar — eksik para tutarını tamamlayan ek miktar
  الدراهم إذا نقصت في الفرائض أو غيرها هلم حوطها؛ الحوط ما يتم به دراهمه



===== _commentary/v16/work/s041/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s041/reader_a_pilot.md)

# s041 Semantic Channel Discovery

## Parent Channels

### 1. P1: Message Assembled and Dispatched
- Semantic invariant: Knowledge moves from a hidden source into a joined, segmented, readable, and publicly voiced form.
- Surface relation: direct; 41:2-6 and 41:12-14 anchor the channel in `تنزيل`, `كتاب`, `فصلت`, `آياته`, `قرآنا`, `عربيا`, `يوحى`, `أوحى`, `الرسل`, `بشيرا`, and `نذيرا`.
- Surprising reach: Revelation materializes as a stitched and gathered artifact whose inner inscription is converted into carried speech.

#### Subchannel A. Stitched, Gathered, and Articulated Text
- Reading type: mixed
- Scene or process: A text-maker joins material, orders letters, gathers them for recitation, and inserts articulating boundaries.
- Active motifs: joining or stitching material `quranic:root_001283:B001/m01`; ordered letters and written artifact `quranic:root_001283:B002/m01`; gathered utterance `quranic:root_001210:B001/m01`; reading and recitation `quranic:root_001210:B002/m01`; textual separators and verse endings `quranic:root_001159:B011/m01`; articulating tongue `quranic:root_001159:B004/m01`; clear expression `quranic:root_000996:B001/m01`; verse-sign as a gathered body of letters `quranic:root_000074:B003/m02`.
- Ayah anchors: 41:3 `كتاب`, `فصلت`, `آياته`, `قرآنا`, `عربيا`.
- Synthesis: Joining and gathering give the text a body, while writing, recitation, and internal separators give that body an ordered voice. The visible sign is therefore not only a message-unit but also a compact assembly of letters whose joints make meaning distinguishable.

#### Subchannel B. Hidden Inscription Becomes Carried Address
- Reading type: mixed
- Scene or process: Concealed knowledge is inscribed, delivered downward, carried by a messenger, and differentiated as welcome or warning.
- Active motifs: hidden transmission of knowledge `quranic:root_001633:B001/m01`; writing and engraving `quranic:root_001633:B003/m01`; divine inspiration and report `quranic:root_001633:B004/m01`; descending delivery of revelation `quranic:root_001492:B002/m01`; messenger and carried message `quranic:root_000563:B002/m01`; spoken utterance `quranic:root_001272:B001/m01`; glad-news proclamation `quranic:root_000120:B005/m01`; danger-warning that awakens caution `quranic:root_001488:B001/m01`.
- Ayah anchors: 41:2 `تنزيل`; 41:4 `بشيرا`, `نذيرا`; 41:6 `قل`, `يوحى`; 41:12 `أوحى`; 41:13 `أنذرتكم`; 41:14 `الرسل`, `أنزل`, `أرسلتم`.
- Synthesis: The channel begins with communication that is hidden, gestural, or engraved and ends with an audible human address. Descent and messenger-bearing form the transfer mechanism, while good news and warning are the two public effects of the same dispatched knowledge.

### 2. P1: Layered Barricades Against Reception
- Semantic invariant: Access is blocked by nested coverings and burdens that run from the inner core to the outer senses.
- Surface relation: direct; 41:4-5 and 41:13 anchor the channel in `أعرض`, `يسمعون`, `قلوبنا`, `أكنة`, `آذاننا`, `وقر`, and `حجاب`.
- Surprising reach: Refusal becomes both architecture and body mechanics: an enclosed heart lies behind a diaphragm-like partition while an overloaded ear and turned flank close the approach.

#### Subchannel A. Heart Inside Nested Screens
- Reading type: mixed
- Scene or process: An inner core is placed inside a protective casing, then separated from the caller by successive screens.
- Active motifs: protective casing `quranic:root_001324:B001/m01`; concealment in the breast or mind `quranic:root_001324:B002/m01`; prevention of access `quranic:root_000294:B001/m01`; separating screen `quranic:root_000294:B002/m01`; diaphragm within the torso `quranic:root_000294:B004/m01`; heart as organ and understanding `quranic:root_001248:B001/m01`; inner pith or core `quranic:root_001248:B002/m01`.
- Ayah anchors: 41:5 `قلوبنا`, `أكنة`, `حجاب`.
- Synthesis: The heart is both the cognitive center and the protected kernel. Cover, screen, and inner diaphragm turn non-reception into a layered enclosure rather than a merely abstract refusal.

#### Subchannel B. Loaded Ear and Averted Side
- Reading type: mixed
- Scene or process: The auditory opening is loaded until acceptance fails, while the body presents its side and withdraws.
- Active motifs: ear as bodily opening `quranic:root_000022:B001/m01`; listening that accepts what is heard `quranic:root_000022:B002/m01`; auditory perception `quranic:root_000741:B001/m01`; understanding and compliance through hearing `quranic:root_000741:B003/m01`; heaviness lodged in the ear `quranic:root_001674:B001/m01`; heavy carried load `quranic:root_001674:B002/m01`; turning away by presenting the side `quranic:root_001001:B005/m01`.
- Ayah anchors: 41:4 `أعرض`, `يسمعون`; 41:5 `آذاننا`, `وقر`; 41:13 `أعرضوا`.
- Synthesis: The same lexical field makes hearing both a physical aperture and an act of obedient uptake. Weight disables that uptake, and the turned side completes the bodily withdrawal.

### 3. P1: The Measured Habitat
- Semantic invariant: The world is produced as a surveyed, fitted, stabilized, and maintained construction.
- Surface relation: direct; 41:9-12 anchor the channel in `خلق`, `جعل`, `قدر`, `سواء`, `استوى`, `رواسي`, `السماء`, `قضى`, `مصابيح`, and `حفظا`.
- Surprising reach: Creation is rendered as workshop practice, structural engineering, and ongoing maintenance rather than as undifferentiated origination.

#### Subchannel A. Survey, Sizing, and Fabrication
- Reading type: mixed
- Scene or process: A maker measures before cutting, assigns form and condition, levels the result, and completes the work.
- Active motifs: measuring before cutting or acting `quranic:root_000434:B001/m01`; bringing a formed creation into existence `quranic:root_000434:B002/m01`; manufacturing or producing `quranic:root_000248:B001/m01`; assigning a thing to a condition `quranic:root_000248:B002/m01`; exact amount and limit `quranic:root_001205:B001/m01`; planning by calculation and fit `quranic:root_001205:B005/m01`; rectification after unevenness `quranic:root_000766:B002/m01`; completed and executed workmanship `quranic:root_001237:B005/m01`.
- Ayah anchors: 41:9 `خلق`, `جعل`; 41:10 `جعل`, `قدر`, `سواء`; 41:11 `استوى`; 41:12 `قضاهن`, `تقدير`; 41:15 `خلقهم`.
- Synthesis: Creation begins as measurement, not random accumulation. Making, assigning, straightening, and finishing form one fabrication sequence in which every part reaches a fitted limit.

#### Subchannel B. Foundation, Roof, Anchor, Lamp, and Guard
- Reading type: mixed
- Scene or process: A lower foundation is paired with an overhead roof, fixed by anchors, lit by lamps, and placed under guard.
- Active motifs: earth as the lower support opposite the sky `quranic:root_000025:B001/m01`; sky as roof and whatever rises to shade `quranic:root_000745:B004/m01`; fixed and rooted mass `quranic:root_000564:B001/m01`; ship-like anchoring `quranic:root_000564:B002/m01`; lamp or sconce `quranic:root_000839:B005/m01`; guarding and maintenance `quranic:root_000342:B001/m01`; upper direction `quranic:root_001188:B001/m01`.
- Ayah anchors: 41:9 `الأرض`; 41:10 `رواسي`, `فوقها`; 41:11-12 `السماء`; 41:12 `مصابيح`, `حفظا`.
- Synthesis: Earth and sky become the floor and roof of a maintained habitation. The mountains carry an anchoring function, while the lamps and guard extend construction into illumination and upkeep.

### 4. P1: Stored Provision in Managed Cycles
- Semantic invariant: Sustenance depends on contained reserves released in measured and recurring portions.
- Surface relation: indirect; 41:10-11 anchor the channel in `بارك`, `أقواتها`, `أربعة`, `فوقها`, `قدر`, and `طوعا`.
- Surprising reach: The allotted provisions of the earth open into two concrete systems: a rain-fed reservoir and the replenishing udder of a managed herd.

#### Subchannel A. Reservoir and Rain-Fed Reserve
- Reading type: latent/lexical
- Scene or process: Water is held in a basin, replenished from cloud-borne pulses, and allotted to produce stable growth and food.
- Active motifs: fixed water in a basin `quranic:root_000109:B003/m01`; stable and growing benefit `quranic:root_000109:B004/m01`; food that sustains the body `quranic:root_001268:B001/m01`; recurring cloud-water pulses `quranic:root_001188:B008/m01`; spring rain and pasture `quranic:root_000536:B005/m01`; measured allotment `quranic:root_001205:B001/m01`.
- Ayah anchors: 41:10 `بارك`, `قدر`, `أقواتها`, `أربعة`, `فوقها`; 41:12 `تقدير`.
- Synthesis: Blessing takes the material form of a stable water reserve whose measured releases sustain pasture and food. The reservoir scene gives spatial and temporal mechanics to the provision allotted in the surface passage.

#### Subchannel B. Kneeling Camel and Replenishing Udder
- Reading type: latent/lexical
- Scene or process: A camel kneels at pasture, milk is drawn, and the udder refills between measured rounds.
- Active motifs: kneeling camel fixed in place `quranic:root_000109:B001/m01`; milk drawn from a kneeling she-camel `quranic:root_000109:B007/m01`; milk returning between milkings `quranic:root_001188:B006/m01`; intake in timed small portions `quranic:root_001188:B007/m01`; pasture ready for grazing `quranic:root_000956:B007/m01`; recurring watering turn `quranic:root_000536:B004/m01`; spring pasture `quranic:root_000536:B005/m01`; sustaining feed `quranic:root_001268:B001/m01`.
- Ayah anchors: 41:10 `بارك`, `أقواتها`, `أربعة`, `فوقها`; 41:11 `طوعا`, `طائعين`.
- Synthesis: The herd scene organizes nourishment through posture, pasture-readiness, watering turns, and udder replenishment. It reframes measured provision as a living reserve that is repeatedly drawn without losing its regulated cycle.

### 5. P1: Sovereign Alignment
- Semantic invariant: Undivided authority establishes the terms of relation and elicits either willing alignment or compelled compliance.
- Surface relation: direct; 41:6, 41:9, and 41:11-12 anchor the channel in `إلهكم إله واحد`, `المشركين`, `أندادا`, `رب`, `أمرا`, `طوعا`, and `كرها`.
- Surprising reach: The cosmic command reads simultaneously as polity, contract, and bodily readiness.

#### Subchannel A. Command Met Willingly or Under Compulsion
- Reading type: mixed
- Scene or process: An obligation is issued, the addressee becomes ready to approach, and compliance is distinguished from coerced performance.
- Active motifs: binding command `quranic:root_000051:B002/m01`; readiness and compliant access `quranic:root_000009:B003/m01`; obedience and yielding `quranic:root_000956:B001/m01`; mutual agreement and compliance `quranic:root_000956:B002/m01`; capacity to perform `quranic:root_000956:B003/m01`; aversion `quranic:root_001295:B001/m01`; coercion into an unwanted act `quranic:root_001295:B003/m01`; straight and balanced course `quranic:root_001273:B008/m01`.
- Ayah anchors: 41:6 `فاستقيموا`; 41:11 `ائتيا`, `طوعا`, `كرها`, `أتينا`, `طائعين`; 41:12 `أمرها`.
- Synthesis: The scene distinguishes capacity, willingness, aversion, and force as separate relations to one command. Straightness is the stable outcome of alignment, while coercion names the opposed route by which the same demand can be met.

#### Subchannel B. Undivided Rule Without Rival
- Reading type: mixed
- Scene or process: A sovereign claim excludes co-ownership, rival equivalence, and divided worship.
- Active motifs: divine unity without partner `quranic:root_001631:B004/m01`; shared ownership or participation `quranic:root_000791:B001/m01`; religious partnership `quranic:root_000791:B002/m01`; rival counterpart `quranic:root_001484:B002/m01`; lordship and mastery `quranic:root_000532:B001/m01`; kingship and political rule `quranic:root_001444:B003/m01`.
- Ayah anchors: 41:6 `إلهكم إله واحد`, `المشركين`; 41:9 `أندادا`, `رب`; 41:14 `ربنا`, `ملائكة`.
- Synthesis: Partnership is first a concrete relation of shared possession, then the theological error of assigning a co-holder to undivided rule. Rival likeness and kingship make the exclusion of peers a structured sovereignty claim.

### 6. P1: Weather Becomes Sentence
- Semantic invariant: A meteorological strike crosses hearing, bodily sensation, and social standing to execute judgment.
- Surface relation: direct; 41:13 and 41:16-17 anchor the channel in `صاعقة`, `ريحا صرصرا`, `نحسات`, `نذيقهم`, `عذاب`, `الخزي`, and `الهون`.
- Surprising reach: The punishment is not one image but a sensory sequence of cry, cold, haze, taste, and public abasement.

#### Subchannel A. Acoustic Cold Front
- Reading type: mixed
- Scene or process: A severe sound descends with a frigid wind, shocks its hearers, and drives a dust-darkened front.
- Active motifs: violent animal-like cry `quranic:root_000864:B001/m01`; upper-world thunderclap `quranic:root_000864:B002/m01`; stunned or dead victim `quranic:root_000864:B003/m01`; shrill rasping sound `quranic:root_000857:B002/m01`; frigid gale `quranic:root_000857:B004/m01`; cold ill-omened wind `quranic:root_001480:B002/m01`; drought-dust driven into the air `quranic:root_001480:B003/m01`; wind as overpowering force `quranic:root_000609:B011/m01`.
- Ayah anchors: 41:13 `صاعقة`; 41:16 `ريحا`, `صرصرا`, `نحسات`; 41:17 `صاعقة`.
- Synthesis: The thunderclap is at once sound, atmospheric blow, and cause of stunned collapse. Cold wind and driven dust extend the strike from an instant of noise into a sustained weather front.

#### Subchannel B. Smoke, Taste, and Shame
- Reading type: mixed
- Scene or process: A darkened atmosphere enters the body as tasted experience and exits socially as exposed humiliation.
- Active motifs: rising smoke `quranic:root_000465:B001/m01`; smoke-darkened haze `quranic:root_000465:B003/m01`; smoke without flame `quranic:root_001480:B005/m01`; tasting food `quranic:root_000526:B001/m01`; experiential tasting and trial `quranic:root_000526:B002/m01`; sweet and potable substance `quranic:root_000994:B001/m01`; painful punishment `quranic:root_000994:B005/m01`; public shame and expulsion `quranic:root_000407:B001/m01`; abasement by contempt `quranic:root_001608:B003/m01`.
- Ayah anchors: 41:11 `دخان`; 41:16 `نحسات`, `لنذيقهم`, `عذاب`, `الخزي`; 41:17 `عذاب`, `الهون`.
- Synthesis: Taste ordinarily tests sweetness and suitability; here the same sensorium is made to register punishment. Smoke supplies the enveloping medium, while shame and abasement translate bodily affliction into a destroyed public position.

### 7. P1: From Trackless Ground to Protected Height
- Semantic invariant: Guidance establishes a traversable course, while protection completes that course in elevated safety.
- Surface relation: direct; 41:17-18 anchor the channel in `هديناهم`, `العمى`, `الهدى`, `نجينا`, `آمنوا`, and `يتقون`.
- Surprising reach: The contrast between guidance and blindness becomes a topography of unmarked land, flood-safe high ground, and a barrier placed against harm.

#### Subchannel A. The Chosen Route and the Unmarked Waste
- Reading type: mixed
- Scene or process: A guide marks a direction, but the traveler prefers a landscape with no recognizable track.
- Active motifs: gentle guidance to a path `quranic:root_001583:B001/m01`; direction and manner of travel `quranic:root_001583:B002/m01`; leader or foremost guide `quranic:root_001583:B003/m01`; blindness of judgment `quranic:root_001049:B002/m01`; unmarked land in which one cannot navigate `quranic:root_001049:B006/m01`; preference lodged in the heart `quranic:root_000286:B002/m01`.
- Ayah anchors: 41:17 `هديناهم`, `استحبوا`, `العمى`, `الهدى`.
- Synthesis: Guidance supplies both a leader and a marked direction. Preferred blindness removes the landmarks, turning the rejected guidance into the image of a traveler deliberately entering trackless terrain.

#### Subchannel B. Raised Refuge Behind a Protective Barrier
- Reading type: mixed
- Scene or process: Escape separates the threatened person from danger and places that person on high ground behind a guard.
- Active motifs: escape by separation `quranic:root_001476:B001/m01`; flood-safe elevated ground `quranic:root_001476:B004/m01`; barrier against injury `quranic:root_001677:B001/m01`; placing oneself in protection `quranic:root_001677:B002/m01`; security and trust `quranic:root_000054:B001/m01`; assent that settles the heart `quranic:root_000054:B002/m01`.
- Ayah anchors: 41:8 `آمنوا`; 41:18 `نجينا`, `آمنوا`, `يتقون`.
- Synthesis: Rescue is not only removal from danger but relocation to terrain the flood cannot overtake. Faith and protective vigilance become the inner and outer forms of the same secure placement.

### 8. P1: Work Accrues a Return
- Semantic invariant: Intentional action produces a return that can appear as wage, acquired proceeds, or liability that takes hold of its earner.
- Surface relation: direct; 41:8 and 41:17 anchor the channel in `عملوا الصالحات`, `أجر غير ممنون`, `أخذتهم`, and `يكسبون`.
- Surprising reach: Moral consequence is materialized through labor contracts and possession rather than through an abstract reward-punishment vocabulary alone.

#### Subchannel A. Uncut Wage for Completed Work
- Reading type: mixed
- Scene or process: Purposeful labor is repaired into right action and paid with a wage that is neither reduced nor cut off.
- Active motifs: wage and recompense for labor `quranic:root_000015:B001/m01`; intentional work `quranic:root_001046:B001/m01`; worker's wage or allowance `quranic:root_001046:B004/m01`; repair and right functioning `quranic:root_000876:B001/m01`; cutting or diminishing an ongoing allotment `quranic:root_001449:B001/m01`.
- Ayah anchors: 41:8 `عملوا`, `الصالحات`, `أجر`, `ممنون`.
- Synthesis: The verse's reward is recast as earned pay attached to purposeful work. The negative form of cutting preserves the wage as an uninterrupted return rather than a one-time gratuity.

#### Subchannel B. Acquisition Ends in Seizure
- Reading type: mixed
- Scene or process: The agent gathers proceeds through action, but those proceeds become the ground on which accountability takes possession of the agent.
- Active motifs: earning and acquiring benefit `quranic:root_001296:B001/m01`; taking possession `quranic:root_000018:B001/m01`; holding a person to account for an offense `quranic:root_000018:B002/m01`; intentional work `quranic:root_001046:B001/m01`.
- Ayah anchors: 41:5 `فاعمل`, `عاملون`; 41:8 `عملوا`; 41:17 `أخذتهم`, `يكسبون`.
- Synthesis: Earning first describes what the actor brings into possession. The reversal is that the consequence then takes possession of the actor, tightening acquisition and seizure into one causal loop.

### 9. P2: The Marshaled Tribunal
- Semantic invariant: Hidden action is converted into ordered public evidence through forced assembly, embodied testimony, and disclosure.
- Surface relation: direct; 41:19-23 anchor the channel in `يحشر`, `يوزعون`, `شهد`, `سمعهم`, `أبصارهم`, `جلودهم`, `أنطقنا`, `تستترون`, `ظننتم`, and `يعلم`.
- Surprising reach: The body is not merely present at judgment; its apertures, hide, and tongue form an evidentiary apparatus.

#### Subchannel A. Restrained Procession to the Hearing
- Reading type: mixed
- Scene or process: A hostile crowd is driven together, held in ordered ranks, and brought to a fiery venue.
- Active motifs: gathering with forced movement `quranic:root_000324:B001/m01`; organized restraint of a column or army `quranic:root_001644:B001/m01`; enemy relation `quranic:root_000993:B003/m01`; fire `quranic:root_001564:B002/m01`; arrival at a place or event `quranic:root_000281:B001/m01`; day as a severe event `quranic:root_001700:B003/m01`.
- Ayah anchors: 41:19 `يوم`, `يحشر`, `أعداء`, `النار`, `يوزعون`; 41:20 `جاءوها`.
- Synthesis: Gathering is joined to restraint, so the movement resembles a marshaled column rather than a loose crowd. Arrival at fire supplies the destination, while the event-day gives the procession its judicial time.

#### Subchannel B. The Body Gives Evidence
- Reading type: mixed
- Scene or process: Skin, ear, eye, and tongue become distinct witnesses that expose intentional work.
- Active motifs: skin as bodily sheath `quranic:root_000253:B001/m01`; hearing by the ear `quranic:root_000741:B001/m01`; visual perception `quranic:root_000121:B001/m01`; presence with direct observation `quranic:root_000822:B001/m01`; testimony that declares known fact `quranic:root_000822:B002/m01`; tongue as witness `quranic:root_000822:B005/m01`; articulated speech `quranic:root_001519:B001/m01`; an indication that speaks for itself `quranic:root_001519:B002/m01`; intentional work `quranic:root_001046:B001/m01`.
- Ayah anchors: 41:20 `شهد`, `سمعهم`, `أبصارهم`, `جلودهم`, `يعملون`; 41:21 `جلودهم`, `شهدتم`, `أنطقنا`.
- Synthesis: The body divides into evidentiary roles: ear and eye register, skin stores and appears, and tongue declares. The latent image of a sign that speaks for itself lets bodily material function as proof without depending on the defendant's chosen account.

#### Subchannel C. Concealment Undone by Knowledge
- Reading type: mixed
- Scene or process: Attempted covering fails because conjecture about the observer is replaced by disclosed knowledge.
- Active motifs: covering and hiding `quranic:root_000674:B001/m01`; weak conjecture `quranic:root_000969:B003/m01`; suspicious disposition `quranic:root_000969:B005/m01`; inward unspoken thought `quranic:root_001272:B012/m01`; knowledge as disclosed recognition `quranic:root_001040:B001/m01`; insight of the heart `quranic:root_000121:B002/m01`.
- Ayah anchors: 41:20, 41:22 `أبصارهم`, `أبصاركم`; 41:21 `قالوا`; 41:22 `تستترون`, `ظننتم`, `يعلم`, `تعملون`; 41:23 `ظنكم`, `ظننتم`.
- Synthesis: Covering presumes that sight can be managed from outside, but conjecture has already misdescribed the knower. Once knowledge is framed as disclosure, concealment and supposition collapse together.

### 10. P2: Bad Estimate Becomes Material Ruin
- Semantic invariant: An unreliable estimate fixes the wrong location or outcome, then resolves as a fall and measurable loss.
- Surface relation: direct; 41:22-23 and 41:25 anchor the channel in repeated `ظن`, `أرداكم`, and `الخاسرين`.
- Surprising reach: Faulty belief becomes an unstable well-site, a stone cast into a drop, and capital removed from an account.

#### Subchannel A. The Unreliable Place of Expectation
- Reading type: latent/lexical
- Scene or process: A person marks where a thing should be found, but the estimate has no dependable outcome.
- Active motifs: expected location or habitual place `quranic:root_000969:B002/m01`; conjecture without certainty `quranic:root_000969:B003/m01`; a well or affair whose outcome cannot be trusted `quranic:root_000969:B006/m01`; inward unspoken proposition `quranic:root_001272:B012/m01`; belief or doctrinal position `quranic:root_001272:B013/m01`.
- Ayah anchors: 41:21 `قالوا`; 41:22 `ظننتم`; 41:23 `ظنكم`, `ظننتم`.
- Synthesis: Assumption is spatial before it is doctrinal: it marks a presumed site. The unreliable well-image makes the epistemic failure concrete, because the expected resource may not be present and the final depth cannot be trusted.

#### Subchannel B. Stone, Fall, and Capital Loss
- Reading type: mixed
- Scene or process: A stone is cast, the subject falls into destruction, and the result is booked as lost capital and short measure.
- Active motifs: stone used for throwing or breaking `quranic:root_000558:B001/m01`; fall into an abyss and destruction `quranic:root_000558:B003/m01`; general diminution `quranic:root_000409:B001/m01`; loss of trading capital `quranic:root_000409:B002/m01`; deficient measure `quranic:root_000409:B003/m01`.
- Ayah anchors: 41:23 `أرداكم`, `الخاسرين`; 41:25 `خاسرين`.
- Synthesis: Ruin unfolds as a physical drop and an economic deficit. The stone and abyss materialize the sudden collapse, while capital loss and deficient measure describe what remains after the fall.

### 11. P2: Destinations as Hospitality
- Semantic invariant: Final outcomes are organized as dwellings with opposed host relations: coercive permanence or welcomed nearness.
- Surface relation: direct; 41:24, 41:28, and 41:30-32 anchor the channel in `النار مثوى`, `دار الخلد`, `تتنزل`, `أولياؤكم`, `الجنة`, `تشتهي`, `تدعون`, and `نزلا`.
- Surprising reach: Judgment becomes a hospitality system in which residence, host, guest provision, and duration all reverse between the two destinations.

#### Subchannel A. Fire as Fixed and Irreconcilable Residence
- Reading type: mixed
- Scene or process: The condemned enter a house-like enclosure, remain attached to it, and find no threshold back to favor.
- Active motifs: fire `quranic:root_001564:B002/m01`; long settlement in a place `quranic:root_000211:B001/m01`; dwelling, householder, and guest-place `quranic:root_000211:B002/m01`; circular enclosure or home `quranic:root_000499:B001/m01`; hostile encirclement `quranic:root_000499:B004/m01`; durable permanence `quranic:root_000429:B001/m01`; clinging residence `quranic:root_000429:B002/m01`; calamity with no exit `quranic:root_000840:B006/m01`; return that restores an offended party's favor `quranic:root_000977:B006/m01`.
- Ayah anchors: 41:24 `يصبروا`, `النار`, `مثوى`, `يستعتبوا`, `المعتبين`; 41:28 `النار`, `دار`, `الخلد`.
- Synthesis: Fire is both venue and enclosing house. Permanence and clinging remove mobility, while the denied return to favor closes the social threshold through which a guest might otherwise repair the relation.

#### Subchannel B. Straight Guests Receive a Descending Welcome
- Reading type: mixed
- Scene or process: Upright guests are met by a descending reception party, reassured, and placed under nearby guardianship in a sheltered garden.
- Active motifs: straight and balanced course `quranic:root_001273:B008/m01`; angelic descent as delivered arrival `quranic:root_001492:B002/m03`; covered orchard `quranic:root_000266:B003/m01`; prepared guest provision `quranic:root_001492:B005/m01`; nearness without a gap `quranic:root_001684:B001/m01`; guardianship and care `quranic:root_001684:B003/m01`; loving protection `quranic:root_001684:B004/m01`; glad news `quranic:root_000120:B005/m01`; promise that opens hope `quranic:root_001662:B001/m01`; merciful care `quranic:root_000552:B001/m01`; forgiveness that covers the offense `quranic:root_001096:B002/m01`.
- Ayah anchors: 41:30 `استقاموا`, `تتنزل`, `الملائكة`, `أبشروا`, `الجنة`, `توعدون`; 41:31 `أولياؤكم`; 41:32 `نزلا`, `غفور`, `رحيم`.
- Synthesis: Straightness prepares the guest, descent brings the welcoming party, and nearness becomes durable guardianship. The garden and prepared provision give material form to promise, mercy, and forgiveness.

#### Subchannel C. Desire Answered on Demand
- Reading type: mixed
- Scene or process: The resident's appetite becomes a summons to which the host's prepared provision responds.
- Active motifs: appetite directed toward a desired object `quranic:root_000825:B001/m01`; a precious object for which selves compete `quranic:root_001533:B010/m01`; calling and summoning `quranic:root_000478:B001/m01`; prepared provision for a guest `quranic:root_001492:B005/m01`.
- Ayah anchors: 41:31 `تشتهي أنفسكم`, `تدعون`; 41:32 `نزلا`.
- Synthesis: Desire is not left as inward appetite; it is converted into a call. Prepared hospitality closes the sequence by making the summoned object available within the residence.

### 12. P2: Companionship Captures Direction
- Semantic invariant: Corrupt companions control orientation by binding the person, occupying the soundscape, and manipulating rank.
- Surface relation: direct; 41:25-26 and 41:29 anchor the channel in `قرناء`, `زينوا`, `بين أيديهم`, `خلفهم`, `لا تسمعوا`, `الغوا`, `تغلبون`, `أضلانا`, `تحت أقدامنا`, and `الأسفلين`.
- Surprising reach: Misguidance operates as a yoke, an acoustic jamming campaign, and a forced vertical ordering.

#### Subchannel A. The Yoked Companion and Enclosed Field
- Reading type: mixed
- Scene or process: A companion is attached like a bound partner, substituted into the person's field, and beautifies what lies before and behind.
- Active motifs: binding two things or prisoners together `quranic:root_001221:B001/m01`; attached companion `quranic:root_001221:B002/m01`; quiver bound beside a bow `quranic:root_001221:B007/m01`; substitution by exchange `quranic:root_001275:B003/m01`; beautifying and displaying attractiveness `quranic:root_000660:B002/m01`; what lies in front `quranic:root_001693:B008/m01`; what lies behind `quranic:root_000433:B002/m01`.
- Ayah anchors: 41:25 `قيضنا`, `قرناء`, `زينوا`, `بين أيديهم`, `خلفهم`.
- Synthesis: The companion is not merely nearby but attached as a paired restraint. Substitution installs that companion, and adornment then colonizes the entire directional field before and behind the person.

#### Subchannel B. Acoustic Jamming of Recitation
- Reading type: mixed
- Scene or process: A coordinated crowd raises mixed and worthless sound to prevent recitation from becoming heard and understood.
- Active motifs: discarded speech that does not count `quranic:root_001361:B001/m01`; corrupt or obscene speech `quranic:root_001361:B002/m01`; mixed disruptive noise `quranic:root_001361:B003/m01`; auditory perception `quranic:root_000741:B001/m01`; making another hear `quranic:root_000741:B004/m01`; reading and recitation `quranic:root_001210:B002/m01`; domination by force `quranic:root_001098:B001/m01`.
- Ayah anchors: 41:26 `لا تسمعوا`, `القرآن`, `الغوا`, `تغلبون`.
- Synthesis: Noise is treated as an active counter-signal, not an absence of listening. By filling the auditory channel with mixed speech, the group attempts to turn reception into a contest of domination.

#### Subchannel C. Underfoot Reversal of Rank
- Reading type: mixed
- Scene or process: Misleaders are dragged from prior precedence to a position beneath the feet and among the lowest ranks.
- Active motifs: lower direction beneath a thing `quranic:root_000177:B001/m01`; despised underclass `quranic:root_000177:B002/m01`; physical foot `quranic:root_001207:B001/m01`; advancing to the front `quranic:root_001207:B004/m01`; low place `quranic:root_000715:B001/m01`; degraded rank `quranic:root_000715:B002/m01`; forcing downward `quranic:root_000715:B004/m01`; deviation from the guided course `quranic:root_000913:B001/m01`.
- Ayah anchors: 41:29 `أضلانا`, `نجعلهما`, `تحت`, `أقدامنا`, `الأسفلين`.
- Synthesis: The request reverses both motion and status. Those who once directed others forward are imagined beneath the feet, with spatial lowering and social baseness becoming one punitive placement.

### 13. P3: Transformative Counterforce
- Semantic invariant: Harmful momentum is redirected until the relation it carried changes from hostility to protective nearness.
- Surface relation: direct; 41:34-35 anchor the channel in `الحسنة`, `السيئة`, `ادفع`, `أحسن`, `عداوة`, `ولي حميم`, and `صبروا`.
- Surprising reach: Ethical response is materialized first as hydraulic or mechanical deflection and then as social reconciliation.

#### Subchannel A. Redirecting the Incoming Surge
- Reading type: mixed
- Scene or process: An incoming harmful force is pushed from its course and conducted into a better outlet.
- Active motifs: removing or repelling harm `quranic:root_000480:B001/m01`; movement driven toward a destination `quranic:root_000480:B003/m01`; surge of flood, wave, or crowd `quranic:root_000480:B005/m01`; water channels and outlets `quranic:root_000480:B006/m01`; moral badness and defective action `quranic:root_000755:B001/m01`; beneficent action beyond strict equivalence `quranic:root_000323:B002/m01`.
- Ayah anchors: 41:34 `السيئة`, `ادفع`, `أحسن`.
- Synthesis: Repulsion is not simple resistance; its lexical extensions supply a moving surge and the channels that redirect it. Superior action therefore changes both the direction and the quality of the incoming force.

#### Subchannel B. Enemy Converted Into Intimate Protector
- Reading type: mixed
- Scene or process: Hostility is dissolved, connection is restored, and the former enemy occupies the role of close ally.
- Active motifs: enemy and enmity `quranic:root_000993:B003/m01`; loving protection and alliance `quranic:root_001684:B004/m01`; intimate relative or cherished close one `quranic:root_000001:B011/m01`; reconciliation that removes estrangement `quranic:root_000876:B002/m01`; peace opposed to war `quranic:root_000737:B004/m01`; restored connection between parties `quranic:root_000170:B003/m01`; holding the self against reactive distress `quranic:root_000840:B001/m01`.
- Ayah anchors: 41:33 `صالحا`, `المسلمين`; 41:34 `بينك`, `عداوة`, `ولي`, `حميم`; 41:35 `صبروا`.
- Synthesis: The transformation is a role reversal, not merely a reduction in hostility. Patience holds the responder steady long enough for severed connection to become peace, alliance, and intimate proximity.

### 14. P3: Verbal Incitement Meets Shelter
- Semantic invariant: An invasive verbal impulse that splits relations is countered by attachment to a protective enclosure.
- Surface relation: direct; 41:36 anchors the channel in repeated `نزغ`, `الشيطان`, `فاستعذ`, `السميع`, and `العليم`.
- Surprising reach: Incitement becomes a word-stab delivered along a long tether, while refuge becomes both shelter and protective amulet.

#### Subchannel A. The Corrosive Prod
- Reading type: mixed
- Scene or process: A rebel at a distance sends a verbal puncture that enters a relation in order to spoil it.
- Active motifs: corruption between parties `quranic:root_001490:B001/m01`; stabbing with a word `quranic:root_001490:B002/m01`; remoteness and severance `quranic:root_000796:B001/m01`; long, tightly twisted tether `quranic:root_000796:B002/m01`; rebellious and overreaching agent `quranic:root_000796:B004/m01`.
- Ayah anchors: 41:36 `ينزغنك`, `الشيطان`, `نزغ`.
- Synthesis: The verbal prod is precise enough to wound yet aimed at the bond between people. Distance and tethering explain how the hostile agent can remain remote while still transmitting a disruptive impulse.

#### Subchannel B. Refuge as Cover and Protective Attachment
- Reading type: mixed
- Scene or process: The threatened person enters protection, attaches to its shelter, and addresses an all-hearing, all-knowing protector.
- Active motifs: seeking a refuge or sanctuary `quranic:root_001059:B001/m01`; protective charm or amulet `quranic:root_001059:B002/m01`; clinging beneath the cover of a stronger thing `quranic:root_001059:B004/m01`; hearing by the ear `quranic:root_000741:B001/m01`; knowledge as full recognition `quranic:root_001040:B001/m01`.
- Ayah anchors: 41:36 `فاستعذ`, `السميع`, `العليم`.
- Synthesis: Refuge is both a place entered and a protective bond worn close. Hearing receives the appeal, while knowledge closes the possibility that the invasive impulse remains hidden.

### 15. P3: Bodies Maintain Ordered Service
- Semantic invariant: Celestial and embodied agents preserve assigned motion and orientation without fatigue.
- Surface relation: direct; 41:37-38 anchor the channel in `الليل`, `النهار`, `الشمس`, `القمر`, `تسجدوا`, `اسجدوا`, `يسبحون`, and `لا يسأمون`.
- Surprising reach: Worship joins orbital swimming, bodily lowering, and continuous labor into one choreography.

#### Subchannel A. Night, Day, Sun, and Moon in Motion
- Reading type: mixed
- Scene or process: Alternating lights traverse a continuous course like swimmers or runners through an open medium.
- Active motifs: night and its darkness `quranic:root_001392:B001/m01`; daylight opening in brightness `quranic:root_001559:B002/m01`; sun and sunlight `quranic:root_000818:B001/m01`; moon and moonlight `quranic:root_001255:B001/m01`; swimming or running through water, air, or orbit `quranic:root_000666:B004/m01`; broad movement through one's sphere of activity `quranic:root_000666:B005/m01`; visible cosmic sign `quranic:root_000074:B003/m01`.
- Ayah anchors: 41:37 `آياته`, `الليل`, `النهار`, `الشمس`, `القمر`; 41:38 `بالليل`, `النهار`, `يسبحون`.
- Synthesis: The paired lights are defined by alternation but connected by continuous movement. Swimming supplies the kinetic invariant that lets different celestial bodies occupy one ordered service.

#### Subchannel B. Lowered Limbs and Unwearied Attendance
- Reading type: mixed
- Scene or process: The worshipper lowers the body at its contact points and maintains service without boredom or exhaustion.
- Active motifs: prostrating submission `quranic:root_000675:B001/m01`; limbs and contact points of prostration `quranic:root_000675:B003/m01`; bending the head and body `quranic:root_000675:B004/m01`; worship through submissive obedience `quranic:root_000973:B003/m01`; self-exalting arrogance `quranic:root_001281:B006/m01`; weariness from prolonged repetition `quranic:root_000662:B001/m01`.
- Ayah anchors: 41:37 `تسجدوا`, `اسجدوا`, `تعبدون`; 41:38 `استكبروا`, `يسبحون`, `لا يسأمون`.
- Synthesis: Prostration distributes submission across concrete bodily joints and surfaces. The contrast with arrogance concerns orientation, while the absence of weariness makes repeated service a stable state rather than a temporary exertion.

### 16. P3: Infusion Activates Hidden Life
- Semantic invariant: A concealed capacity becomes visible life when an inward medium enters, disturbs, and nourishes it.
- Surface relation: direct; 41:39 anchors the channel in `الأرض خاشعة`, `أنزلنا عليها الماء`, `اهتزت`, `ربت`, `أحياها`, and `الموتى`.
- Surprising reach: The revived field opens into a parallel gestational mechanism in which seminal water enters a containing organ and develops hidden life.

#### Subchannel A. Irrigated Ground Rises From Dormancy
- Reading type: mixed
- Scene or process: Low, dormant soil receives water, shakes, swells, and becomes living growth.
- Active motifs: fertile and plant-bearing earth `quranic:root_000025:B002/m01`; low and dormant ground `quranic:root_000412:B002/m01`; rain or water brought down `quranic:root_001492:B002/m02`; water supplied by pouring or irrigation `quranic:root_001458:B003/m01`; earth and vegetation shaking into life `quranic:root_001588:B002/m01`; swelling and increase `quranic:root_000537:B001/m01`; life of earth through rain and plants `quranic:root_000383:B002/m01`; dead uncultivated land `quranic:root_001454:B003/m01`.
- Ayah anchors: 41:39 `الأرض`, `خاشعة`, `أنزلنا`, `الماء`, `اهتزت`, `ربت`, `أحياها`, `الموتى`.
- Synthesis: Water does not merely cover the soil; it triggers motion, swelling, and renewed growth. The dead-land sense makes resurrection a change of state in a material substrate.

#### Subchannel B. Gestational Water and Inward Growth
- Reading type: latent/lexical
- Scene or process: Generative water enters a containing organ, is gathered as a pregnancy, and is nourished toward growth.
- Active motifs: seminal water placed in a womb `quranic:root_001458:B004/m01`; emitted generative fluid `quranic:root_001492:B009/m01`; womb gathering a pregnancy `quranic:root_001210:B004/m01`; nourishment and development of a child `quranic:root_000537:B005/m01`; concealed reproductive organ or womb `quranic:root_000383:B011/m01`.
- Ayah anchors: 41:39 `أنزلنا`, `الماء`, `ربت`, `أحياها`; 41:44 `قرآنا`.
- Synthesis: The same roots that describe descent, water, swelling, and life assemble a gestational analogue. Containment and nourishment explain how hidden potential can pass through an inward phase before it becomes perceptible growth.

### 17. P3: Protected Text That Clarifies and Heals
- Semantic invariant: A guarded message is assembled and articulated so that it can guide and repair reception.
- Surface relation: direct; 41:41-44 anchor the channel in `الذكر`, `كتاب عزيز`, `لا يأتيه الباطل`, `بين يديه`, `خلفه`, `تنزيل`, `قرآنا`, `فصلت آياته`, `أعجمي وعربي`, `هدى`, `شفاء`, `وقر`, `عمى`, and `ينادون من مكان بعيد`.
- Surprising reach: The text is simultaneously a fortified artifact, a pointed and segmented script, a road-marker, and a medicine.

#### Subchannel A. Guarded Front and Rear
- Reading type: mixed
- Scene or process: A hard-to-reach written object is secured on both approaches so that destabilizing material cannot enter it.
- Active motifs: written artifact `quranic:root_001283:B002/m01`; rarity and difficulty of access `quranic:root_001008:B003/m01`; hard compact substrate `quranic:root_001008:B007/m01`; falsehood losing stability `quranic:root_000127:B001/m01`; active removal or invalidation `quranic:root_000127:B002/m01`; what lies in front `quranic:root_001693:B008/m01`; what lies behind `quranic:root_000433:B002/m01`; bridle-like prevention of corruption `quranic:root_000348:B001/m01`; perfected and secured construction `quranic:root_000348:B004/m01`; descending delivery of revelation `quranic:root_001492:B002/m01`.
- Ayah anchors: 41:41 `الذكر`, `كتاب`, `عزيز`; 41:42 `يأتيه`, `الباطل`, `بين يديه`, `خلفه`, `تنزيل`, `حكيم`.
- Synthesis: The book is made difficult to penetrate and structurally secure. Front and rear become defended approaches, while falsehood is the unstable material excluded from the completed construction.

#### Subchannel B. Pointed, Read, and Articulated Script
- Reading type: mixed
- Scene or process: Written units are gathered, read, marked to remove ambiguity, separated into meaningful sections, and voiced clearly.
- Active motifs: gathering language into a recitable whole `quranic:root_001210:B001/m01`; reading and recitation `quranic:root_001210:B002/m01`; ordered letters and written artifact `quranic:root_001283:B002/m01`; adding points that disambiguate script `quranic:root_000988:B002/m01`; inarticulate or foreign speech `quranic:root_000988:B001/m01`; clear Arabic expression `quranic:root_000996:B001/m01`; adapting a foreign name to Arabic form `quranic:root_000996:B019/m01`; textual separators `quranic:root_001159:B011/m01`; detailing and distinguishing parts `quranic:root_001159:B013/m01`; articulating tongue `quranic:root_001159:B004/m01`.
- Ayah anchors: 41:41 `كتاب`; 41:44 `قرآنا`, `أعجميا`, `فصلت`, `آياته`, `أعجمي`, `عربي`.
- Synthesis: Foreignness and clarity are mediated by the concrete work of pointing, separating, reading, and voicing. The text becomes intelligible through an engineered relation between graphic distinction and articulated speech.

#### Subchannel C. Road-Marker and Medicine Across Obstructed Senses
- Reading type: mixed
- Scene or process: Guidance marks a route and offers a cure, but a weighted ear and blinded traveler convert nearby instruction into a far-off call.
- Active motifs: gentle guidance to a route `quranic:root_001583:B001/m01`; leading guide at the front `quranic:root_001583:B003/m01`; cure that removes illness `quranic:root_000806:B001/m01`; heaviness in the ear `quranic:root_001674:B001/m01`; blindness of the eye `quranic:root_001049:B001/m01`; unmarked land in which one cannot navigate `quranic:root_001049:B006/m01`; far distance `quranic:root_000131:B001/m01`; projected summons `quranic:root_001486:B002/m01`; listening that accepts `quranic:root_000022:B002/m01`.
- Ayah anchors: 41:44 `هدى`, `شفاء`, `آذانهم`, `وقر`, `عمى`, `ينادون`, `مكان بعيد`.
- Synthesis: Guidance and healing address orientation and condition at once. When hearing is burdened and sight cannot find landmarks, the message does not cease to call; instead, the receiver experiences it as a signal arriving from extreme distance.

### 18. P4: Deferred Case and Contested Record
- Semantic invariant: A prior record holds judgment in suspension while interlocked claims prevent decisive separation.
- Surface relation: direct; 41:45 and 41:54 anchor the channel in `الكتاب`, `اختلف`, `كلمة سبقت`, `لقضي بينهم`, `شك مريب`, and `مرية`.
- Surprising reach: Epistemic conflict becomes both a docket awaiting closure and a rank of interpenetrating weapons.

#### Subchannel A. Prior Writ Delays Closure
- Reading type: mixed
- Scene or process: A written decree and preceding word govern when the case can be separated, completed, and settled.
- Active motifs: written record `quranic:root_001283:B002/m01`; inscription that imposes judgment or decree `quranic:root_001283:B003/m01`; meaningful word or clause `quranic:root_001316:B002/m01`; precedence and prior arrival `quranic:root_000671:B001/m01`; decisive judgment `quranic:root_001237:B001/m01`; completion and closure `quranic:root_001237:B004/m01`; settlement of a due `quranic:root_001237:B006/m01`; separation and distinction `quranic:root_000170:B001/m01`; disclosure that clarifies `quranic:root_000170:B004/m01`.
- Ayah anchors: 41:45 `آتينا`, `الكتاب`, `اختلف`, `كلمة`, `سبقت`, `لقضي`, `بينهم`.
- Synthesis: The earlier word functions like governing precedent on a written docket. It delays the otherwise decisive operation that would separate parties, close the matter, and settle what is due.

#### Subchannel B. Doubt as Interpenetrating Conflict
- Reading type: latent/lexical
- Scene or process: Claims overlap without resolution like objects pierced onto one point or soldiers fitted into one armed rank.
- Active motifs: two matters interpenetrating without certainty `quranic:root_000812:B001/m01`; piercing and stringing objects together `quranic:root_000812:B002/m01`; fitted armament around its bearer `quranic:root_000812:B003/m01`; interlocked row or military formation `quranic:root_000812:B005/m01`; turbulent suspicion `quranic:root_000616:B001/m01`; sharp verbal disputation `quranic:root_001416:B003/m01`; wavering doubt `quranic:root_001416:B004/m01`; divergent paths and disagreement `quranic:root_000433:B004/m01`.
- Ayah anchors: 41:45 `اختلف`, `شك`, `مريب`; 41:54 `مرية`.
- Synthesis: Doubt is not emptiness but an overfull state in which alternatives penetrate and hold one another. Armament and rank imagery give contested belief the form of an unresolved, mutually braced conflict.

### 19. P4: The Account Returns to Its Bearer
- Semantic invariant: Action, benefit, injury, and liability remain attached to the proper self rather than being displaced onto another.
- Surface relation: direct; 41:45-46, 41:50, and 41:53 anchor the channel in `عمل صالحا`, `فلنفسه`, `أساء`, `فعليها`, `بظلام للعبيد`, `عملوا`, and `الحق`.
- Surprising reach: Moral responsibility becomes a transaction whose owner, due, and place of settlement cannot be falsified.

#### Subchannel A. Action Settles on the Self
- Reading type: mixed
- Scene or process: Intentional work produces its return in a transaction that closes on the actor's own identity and inward purpose.
- Active motifs: intentional work `quranic:root_001046:B001/m01`; worker's earning or allowance `quranic:root_001046:B004/m01`; transaction between parties `quranic:root_001046:B005/m01`; repair and right action `quranic:root_000876:B001/m01`; defective or evil act `quranic:root_000755:B001/m01`; injury that grieves its recipient `quranic:root_000755:B002/m01`; self as the thing's own identity `quranic:root_001533:B012/m01`; inward purpose and judgment `quranic:root_001533:B013/m01`.
- Ayah anchors: 41:46 `عمل`, `صالحا`, `لنفسه`, `أساء`, `عليها`; 41:50 `عملوا`; 41:53 `أنفسهم`.
- Synthesis: Work is simultaneously deed, earning, and transaction. The repeated self-reference closes the circuit so that the result cannot migrate away from the identity and intention that produced it.

#### Subchannel B. A Right Is Neither Misplaced Nor Withheld
- Reading type: mixed
- Scene or process: A claimant's due is placed with its owner, settled in full, and never withheld by superior power.
- Active motifs: grievance seeking redress `quranic:root_000967:B003/m01`; putting an act in the wrong place or time `quranic:root_000967:B004/m01`; withholding a right `quranic:root_000967:B008/m01`; specific right owned by its claimant `quranic:root_000347:B003/m01`; settling and collecting a due `quranic:root_001237:B006/m01`; owned servant `quranic:root_000973:B001/m01`; subjecting another to servitude `quranic:root_000973:B004/m01`.
- Ayah anchors: 41:45 `لقضي`; 41:46 `بظلام`, `للعبيد`; 41:53 `الحق`.
- Synthesis: Injustice is made concrete as wrong placement or detention of another's property. The denial of injustice therefore protects both allocation and payment: each due reaches the servant to whom it belongs.

### 20. P4: Concealed Contents Move Into Disclosure
- Semantic invariant: A protected inner payload reaches maturity, exits its enclosure, and becomes publicly knowable.
- Surface relation: direct; 41:47 anchors the channel in `تخرج من ثمرات من أكمامها`, `تحمل من أنثى`, `تضع`, and repeated `علم`.
- Surprising reach: Fruit emergence and childbirth are parallel release mechanisms, each moving a living content from cover to evidence.

#### Subchannel A. Fruit Exits Its Sheath
- Reading type: mixed
- Scene or process: A growing result matures inside a plant covering, breaks concealment, and appears as knowable fruit.
- Active motifs: ripe fruit `quranic:root_000205:B001/m01`; result or benefit generated by a process `quranic:root_000205:B003/m01`; plant vessel and fruit sheath `quranic:root_001319:B002/m01`; covering, sealing, and suppressing emergence `quranic:root_001319:B004/m01`; fruit-cover or inflorescence sheath `quranic:root_001307:B010/m01`; tree-borne fruit as an inward load `quranic:root_000357:B002/m02`; emergence from an enclosure `quranic:root_000400:B001/m01`; extraction from concealment `quranic:root_000400:B002/m01`; knowledge as disclosure `quranic:root_001040:B001/m01`.
- Ayah anchors: 41:47 `علم`, `تخرج`, `ثمرات`, `أكمامها`, `تحمل`; 41:50, 41:52 `كفر`.
- Synthesis: The sheath is not an incidental cover; it is the vessel in which fruit develops. Exit and extraction describe the transition from hidden growth to a result that can be observed and known.

#### Subchannel B. Pregnancy Reaches Placement and Witness
- Reading type: mixed
- Scene or process: A female carries an inward load, releases it in birth, and the emerging child becomes a witnessed fact received outside the body.
- Active motifs: inward gestational load `quranic:root_000357:B002/m01`; entrusted burden carried by a person `quranic:root_000357:B003/m01`; female sex `quranic:root_000058:B001/m01`; delivery and laying down a pregnancy `quranic:root_001657:B002/m01`; childbirth and postpartum emergence `quranic:root_001533:B005/m01`; birth-sign that comes out with the child `quranic:root_000822:B006/m01`; receiving what emerges into the hand `quranic:root_001198:B007/m01`.
- Ayah anchors: 41:47 `تحمل`, `أنثى`, `تضع`, `بعلمه`, `شهيد`; 41:48 `قبل`; 41:53 `أنفسهم`, `شهيد`.
- Synthesis: Carrying is both biological load and entrusted burden, while placing down marks the terminal act of delivery. The birth-sign and receiving hand complete the passage from hidden content to external evidence.

### 21. P4: Claimed Partners Fail at the Hearing
- Semantic invariant: A claimed support must be produced, located, and made to testify, but it disappears when summoned.
- Surface relation: direct; 41:47-48 anchor the channel in `يناديهم`, `شركائي`, `آذناك`, `شهيد`, `ضل عنهم`, `يدعون`, `ظنوا`, and `محيص`.
- Surprising reach: The scene behaves like a hearing about absent co-owners, missing property, failed surety, and an attempted escape from process.

#### Subchannel A. Co-Claimants Are Summoned
- Reading type: mixed
- Scene or process: Alleged partners are called as co-holders or sureties, but no present witness can establish the claim.
- Active motifs: shared ownership or participation `quranic:root_000791:B001/m01`; partnership by affinity or alliance `quranic:root_000791:B003/m01`; claiming a right or attribution `quranic:root_000478:B002/m01`; projected public summons `quranic:root_001486:B002/m01`; presence with direct observation `quranic:root_000822:B001/m01`; testimony based on knowledge `quranic:root_000822:B002/m01`; guarantee or surety `quranic:root_001198:B008/m01`.
- Ayah anchors: 41:47 `يناديهم`, `شركائي`, `آذناك`, `شهيد`; 41:48 `يدعون`, `قبل`.
- Synthesis: Partnership is treated as a claim of shared title that must be supported at a hearing. Summons, presence, testimony, and surety make the partners' nonappearance a collapse of the claim's legal structure.

#### Subchannel B. Missing Property and No Exit
- Reading type: mixed
- Scene or process: The sought support is lost like ownerless stock, its expected location proves unreliable, and every evasive turn closes.
- Active motifs: lost object `quranic:root_000913:B003/m01`; stray ownerless animal `quranic:root_000913:B005/m01`; expected location `quranic:root_000969:B002/m01`; an affair or well with an unreliable outcome `quranic:root_000969:B006/m01`; evasive turn from a direction `quranic:root_000378:B001/m01`; trapped confusion with no way out `quranic:root_000378:B002/m01`.
- Ayah anchors: 41:48 `ضل`, `يدعون`, `ظنوا`, `محيص`.
- Synthesis: The missing partners become lost property that cannot be produced from its presumed place. The final recognition is spatial: there is neither a reliable location for the support nor a route by which the claimant can evade the failed claim.

### 22. P4: Circumstance Reorients the Human Body
- Semantic invariant: Immediate contact with harm or favor changes bodily posture, prayer, and belief, exposing an unstable relation to circumstance.
- Surface relation: direct; 41:49-51 anchor the channel in `دعاء الخير`, `مسه الشر`, `يئوس قنوط`, `أذقناه رحمة`, `ضراء مسته`, `هذا لي`, `أعرض`, `نأى بجانبه`, and `دعاء عريض`.
- Surprising reach: Human volatility is mapped as touch, expansion, turned flank, distance, and proprietary grasp.

#### Subchannel A. Pain Broadens Petition and Cuts Hope
- Reading type: mixed
- Scene or process: Harm makes urgent contact, severs expectation, and expands a previously narrow appeal across the available space.
- Active motifs: an effect making contact `quranic:root_001423:B004/m01`; urgent need that presses closely `quranic:root_001423:B006/m01`; harm and loss opposed to benefit `quranic:root_000907:B001/m01`; necessity that compels an unwanted condition `quranic:root_000907:B003/m01`; evil or injury `quranic:root_000787:B001/m01`; severed hope `quranic:root_001690:B001/m01`; despair of relief `quranic:root_001261:B001/m01`; calling and petition `quranic:root_000478:B001/m01`; breadth and lateral extension `quranic:root_001001:B001/m01`.
- Ayah anchors: 41:49 `دعاء`, `الخير`, `مسه`, `الشر`, `يئوس`, `قنوط`; 41:50 `ضراء`, `مسته`; 41:51 `مسه`, `الشر`, `دعاء`, `عريض`.
- Synthesis: Touch makes adversity immediate, while despair describes the cutting of a future line. The broad prayer reverses that closure spatially by spreading the appeal as far as possible.

#### Subchannel B. Favor Turns the Flank Away
- Reading type: mixed
- Scene or process: Ease softens the person's condition, but the body responds by presenting its side and increasing distance.
- Active motifs: favor and good condition `quranic:root_001525:B001/m01`; softness and luxurious ease `quranic:root_001525:B002/m01`; turning away by presenting the side `quranic:root_001001:B005/m01`; distancing the flank `quranic:root_001463:B002/m01`; side of the body `quranic:root_000262:B001/m01`; withdrawal and separation `quranic:root_000262:B003/m01`.
- Ayah anchors: 41:51 `أنعمنا`, `أعرض`, `نأى`, `بجانبه`.
- Synthesis: Favor changes condition but not orientation toward the giver. The side, flank, and increasing interval turn ingratitude into a measured bodily withdrawal.

#### Subchannel C. Relief Becomes Proprietary Presumption
- Reading type: mixed
- Scene or process: Mercy after harm is grasped as private possession, then extended into confident assumptions about time, return, and favored standing.
- Active motifs: merciful care `quranic:root_000552:B001/m01`; later succession after an event `quranic:root_000131:B002/m01`; conviction based on an indicator `quranic:root_000969:B001/m01`; uncertain conjecture `quranic:root_000969:B003/m01`; return to a prior source or state `quranic:root_000544:B001/m01`; desired goodness `quranic:root_000323:B001/m01`; nearness and presence `quranic:root_001052:B004/m01`; resurrection and the standing Hour `quranic:root_001273:B013/m01`; spoken claim `quranic:root_001272:B001/m01`.
- Ayah anchors: 41:50 `رحمة`, `بعد`, `يقولن`, `هذا لي`, `أظن`, `الساعة`, `قائمة`, `رجعت`, `عند`, `الحسنى`.
- Synthesis: Relief is first converted into ownership, then into a forecast that the favorable condition must persist. Return, nearness, and the standing Hour expose how immediate possession is projected into an unwarranted future entitlement.

### 23. P4: Evidence Closes From Horizon to Interior
- Semantic invariant: Evidence advances from the far boundary and the inner self until complete witnessing leaves no exterior position.
- Surface relation: direct; 41:53-54 anchor the channel in `نريهم آياتنا في الآفاق وفي أنفسهم`, `يتبين`, `الحق`, `شهيد`, `لقاء ربهم`, and `بكل شيء محيط`.
- Surprising reach: Demonstration becomes a spatial closure formed by horizon, interior identity, visible marks, witness-presence, and an enclosing ring.

#### Subchannel A. Boundary and Self Made Legible
- Reading type: mixed
- Scene or process: Marks are displayed at the outer limit and within the observer until their relation becomes visibly distinct as truth.
- Active motifs: far horizons and limits `quranic:root_000040:B001/m01`; traversing the horizons `quranic:root_000040:B002/m01`; self as identity and essence `quranic:root_001533:B012/m01`; inner mind and intention `quranic:root_001533:B013/m01`; visual perception `quranic:root_000531:B001/m01`; causing another to see `quranic:root_000531:B012/m01`; visible sign or marker `quranic:root_000074:B003/m01`; emergence into clarity `quranic:root_000170:B004/m01`; disclosure by speech or sign `quranic:root_000170:B005/m01`; truth stable against falsehood `quranic:root_000347:B001/m01`; establishment and display of truth `quranic:root_000347:B005/m01`.
- Ayah anchors: 41:53 `نريهم`, `آياتنا`, `الآفاق`, `أنفسهم`, `يتبين`, `الحق`.
- Synthesis: The horizon defines the farthest outward field, while the self supplies the innermost one. Showing, marking, and clarification connect those extremes until truth is not inferred from one isolated sign but becomes legible across the whole span.

#### Subchannel B. Witness Becomes Enclosure
- Reading type: mixed
- Scene or process: Present testimony gathers every part, circles it, and closes in until meeting and doubt both occur inside the same encompassing field.
- Active motifs: presence with direct observation `quranic:root_000822:B001/m01`; testimony based on knowledge `quranic:root_000822:B002/m01`; marker that bears witness `quranic:root_000822:B008/m01`; totality that gathers all parts `quranic:root_001315:B003/m01`; crown or ring that surrounds `quranic:root_001315:B005/m01`; physical encirclement `quranic:root_000372:B001/m01`; complete containment in knowledge `quranic:root_000372:B004/m01`; overwhelming enclosure `quranic:root_000372:B006/m01`; meeting face to face `quranic:root_001372:B004/m01`; wavering doubt `quranic:root_001416:B004/m01`.
- Ayah anchors: 41:53 `شهيد`, `كل`, `شيء`; 41:54 `مرية`, `لقاء`, `كل`, `شيء`, `محيط`.
- Synthesis: Witnessing is first presence and declaration, then a marker that covers the field of inquiry. Totality, ring, and encirclement make the final claim spatially exhaustive: even doubt about the meeting remains inside what is already encompassed.

## Standalone Subchannels

### S1. P1: Boasted Strength as a Structure Broken by Weather
- Reading type: mixed
- Scene or process: Claimed power is imagined as tied, load-bearing material that meets a stronger atmospheric force and loses its capacity to support or defend.
- Active motifs: tightened knot and binding `quranic:root_000782:B001/m01`; concentrated strength and hardness `quranic:root_000782:B002/m01`; rope-like strands of force `quranic:root_001274:B001/m01`; hard compact ground `quranic:root_001008:B007/m01`; overpowering rain or flood `quranic:root_001008:B008/m01`; self-exalting arrogance `quranic:root_001281:B006/m01`; wind as force and dominion `quranic:root_000609:B011/m01`; aid that makes one prevail `quranic:root_001510:B001/m01`.
- Ayah anchors: 41:12 `العزيز`; 41:15 `استكبروا`, `أشد`, `قوة`; 41:16 `ريحا`, `لا ينصرون`.
- Synthesis: Strength is assembled from knots, strands, compacted ground, and load-bearing capacity. The gale and flood senses provide the greater external force, while absent aid marks the structure's final failure.

### S2. P2: Recompense as Debt Collection
- Reading type: mixed
- Scene or process: Intentional work creates a due that is collected through equivalent return and embodied experience.
- Active motifs: reciprocal recompense `quranic:root_000244:B001/m01`; collection and settlement of a debt `quranic:root_000244:B003/m01`; intentional work `quranic:root_001046:B001/m01`; transaction between people `quranic:root_001046:B005/m01`; experiential tasting and trial `quranic:root_000526:B002/m01`; painful punishment `quranic:root_000994:B005/m01`.
- Ayah anchors: 41:27 `نذيقن`, `عذابا`, `لنجزينهم`, `يعملون`; 41:28 `جزاء`, `جزاء`, `يجحدون`.
- Synthesis: Recompense behaves like an account whose due must be settled rather than a free-standing penalty. Tasting makes collection bodily, and intentional work supplies the transaction from which the liability arose.

### S3. P3: Lateral Deviation Ends in Contrasted Arrivals
- Reading type: mixed
- Scene or process: One traveler leans into a side-cut and is cast into fire, while another approaches the same terminal day in security.
- Active motifs: deviation from the straight course `quranic:root_001345:B001/m01`; side-cut grave niche `quranic:root_001345:B002/m01`; leaning toward a side or edge `quranic:root_001345:B005/m01`; casting or throwing down `quranic:root_001372:B005/m01`; face-to-face arrival `quranic:root_001372:B004/m01`; fire `quranic:root_001564:B002/m01`; coming and reaching `quranic:root_000009:B001/m01`; secure state `quranic:root_000054:B001/m01`; resurrection and standing day `quranic:root_001273:B013/m01`.
- Ayah anchors: 41:40 `يلحدون`, `يلقى`, `النار`, `يأتي`, `آمنا`, `يوم القيامة`.
- Synthesis: The lexical side-cut gives deviation a terminal geometry resembling a burial niche. Casting and secure approach then define opposed modes of arrival at the same event.

### S4. P4: Schism Materialized as Distant Terrain
- Reading type: mixed
- Scene or process: Doctrinal opposition splits a common route into remote sides until the disagreement becomes a difficult journey across a rift.
- Active motifs: cracking and opening `quranic:root_000807:B001/m01`; group split by hostility `quranic:root_000807:B004/m01`; distant travel `quranic:root_000807:B005/m01`; deviation toward opposing sides `quranic:root_000807:B009/m01`; far distance `quranic:root_000131:B001/m01`; causing separation `quranic:root_000131:B003/m01`; hostility carried to an extreme `quranic:root_000131:B010/m01`; straying from the intended route `quranic:root_000913:B001/m01`; withdrawing to a side apart from the group `quranic:root_001052:B002/m01`.
- Ayah anchors: 41:52 `عند`, `أضل`, `شقاق`, `بعيد`.
- Synthesis: Schism is a crack in both group and route. Distance and difficult travel extend the split until opposition is experienced as inhabiting a far side rather than merely holding a different proposition.

### S5. Whole-surah: A Shot Drawn, Fitted, and Turned Aside
- Reading type: latent/lexical
- Scene or process: An archer reaches into a quiver, fits a lightly fletched shaft to a sinew string, directs it toward a target, and releases a shot that can turn aside without making contact.
- Active motifs: deliberate direction of an arrow toward its target `quranic:root_000053:B012/m01`; white sinew made into a bowstring `quranic:root_001033:B001/m01`; arrow nock seated on the string `quranic:root_001188:B009/m01`; quiver containing arrows `quranic:root_001324:B004/m01`; hand reaching to the quiver for a shaft `quranic:root_000544:B010/m01`; light shaft with fine fletching `quranic:root_000324:B006/m01`; veering shot that lands without scratching the target `quranic:root_001464:B005/m01`.
- Ayah anchors: 41:5 `أكنة`; 41:10 `فوقها`; 41:19 `يحشر`; 41:21 `ترجعون`; 41:25 `أمم`; 41:43 `عقاب`; 41:50 `رجعت`, `فلننبئن`.
- Synthesis: The completed mechanism materializes the surah's repeated problem of dispatch, reception, straightness, and deviation: a message may be carefully stored, fitted, and aimed, yet a turned trajectory ends without impact. It usefully pressures the hearers' treatment of clear revelation as though distance lay in the message itself by locating failure in deflection between release and contact.

### S6. Whole-surah: Fire Tended Beneath the Cooking Pot
- Reading type: latent/lexical
- Scene or process: Fire is struck from stone, kept alive with gentle fuel or breath, used beneath a cooking vessel where smoke can spoil the contents, and handled with a heat cloth.
- Active motifs: white flint that strikes fire `quranic:root_001416:B002/m01`; gently feeding a fire with wood or breath `quranic:root_001268:B003/m01`; cooking pot and the food prepared in it `quranic:root_001205:B007/m01`; smoke entering and spoiling a pot or its contents `quranic:root_000465:B002/m01`; cloth used to lower a pot from the fire `quranic:root_000248:B007/m01`.
- Ayah anchors: 41:9-10 `تجعل`, `جعل`; 41:10 `أقواتها`, `قدر`; 41:11 `دخان`; 41:12 `تقدير`; 41:39 `قدير`; 41:54 `مرية`.
- Synthesis: The controlled hearth materializes measured provision: allotted sustenance becomes the tending of flame, while measure becomes the vessel in which food is transformed. It reframes the surah's fire-and-taste polarity by showing that governed heat nourishes while smoke entering the vessel corrupts; placement, proportion, and handling determine whether fire serves provision or ruin.

### S7. Whole-surah: Foster-Calf Recognition Through a Borrowed Hide
- Reading type: latent/lexical
- Scene or process: A dam remains attached to her newborn, the calf is separated, and a bereft animal is induced to accept and nurse another calf by means of a stripped hide and stimulated udder.
- Active motifs: postpartum dam clinging to her young `quranic:root_001059:B003/m01`; calf separated from its mother or weaned `quranic:root_001159:B003/m01`; bereft she-camel induced to foster another calf `quranic:root_000436:B010/m01`; stripped calf hide worn or stuffed to prompt maternal acceptance `quranic:root_000253:B005/m01`; udder rubbed to draw milk `quranic:root_001416:B001/m01`.
- Ayah anchors: 41:3, 41:44 `فصلت`; 41:20-22 `جلودهم`; 41:25 `خلت`; 41:36 `فاستعذ`; 41:54 `مرية`.
- Synthesis: This husbandry practice usefully pressures the body's testimony in 41:20-22: a detached hide can counterfeit offspring identity and redirect maternal recognition, but the judgment scene makes each body's own skins speak rather than serve as disguises. The latent practice sharpens the primary claim that divine disclosure fixes testimony to the true bearer despite manipulable appearance.

### S8. Whole-surah: Hive, Comb, and Honey Gathering
- Reading type: latent/lexical
- Scene or process: A leading bee orders life in a hive, honey remains enclosed in wax cells until collection, and the honey gatherer carries away the thickening liquid.
- Active motifs: leading bee followed by the colony `quranic:root_001444:B008/m01`; hive in which bees make honey `quranic:root_000436:B012/m01`; honey still enclosed in its wax comb before pressing `quranic:root_000822:B007/m01`; leather carrier used by a honey gatherer `quranic:root_000447:B006/m01`; honey thickening and coagulating `quranic:root_000067:B005/m01`.
- Ayah anchors: 41:14, 41:30 `ملائكة`; 41:20-22 `شهد`, `يشهد`; 41:21 `أول`; 41:25 `خلت`; 41:30 `تخافوا`; 41:47, 41:53 `شهيد`.
- Synthesis: The hive materializes the surah's witness-and-disclosure pattern: `شهد` becomes valuable content already present but sealed cell by cell in wax until it is gathered and pressed. This supports the body's testimony and the signs shown across horizon and self by reframing hidden evidence as stored rather than absent; disclosure retrieves what a protected interior already holds.

### S9. Whole-surah: Body Carried, Covered, and Buried
- Reading type: latent/lexical
- Scene or process: A dead body is placed on a carrying frame, wrapped and concealed, buried until it disappears into the earth, and accompanied by lament.
- Active motifs: a single state or occurrence of death `quranic:root_001454:B008/m01`; funeral bier or carrying frame `quranic:root_000067:B008/m01`; shrouding the dead and enclosing the grave `quranic:root_000266:B009/m01`; burial until the body vanishes from sight `quranic:root_000913:B002/m01`; mourning and wailing for the dead `quranic:root_001633:B009/m01`.
- Ayah anchors: 41:6 `يوحى`; 41:12 `أوحى`; 41:21 `أول`; 41:25, 41:29 `الجن`; 41:29, 41:48, 41:52 `أضل`, `ضل`; 41:39 `الموتى`.
- Synthesis: The rite supports the surah's resurrection claim by distinguishing concealment from annihilation: carrying, shrouding, and burial produce social disappearance, but they remain ordered operations performed upon the dead. Against the revival of dead earth in 41:39, the scene pressures disappearance as finality; what vanishes from sight remains within the reach of revivification and account.

### S10. P1-P4: Message Held, Lost, and Recalled
- Reading type: latent/lexical
- Scene or process: P1-P4 bridge - causal sequence: content is given and brought into presence, fixed in memory, lost from memory, and restored by recollection.
- Active motifs: giving or presenting a thing `quranic:root_000009:B002/m01`; bringing a thing into presence `quranic:root_000281:B004/m01`; fixing heard content in memory `quranic:root_000342:B002/m01`; loss of retained content from memory `quranic:root_000913:B004/m01`; recollection after forgetting `quranic:root_000516:B003/m01`.
- Ayah anchors: 41:7 `يؤتون`; 41:12 `حفظا`; 41:14 `جاءتهم`; 41:20 `جاءوها`; 41:29 `أضلانا`; 41:41 `جاءهم`, `الذكر`; 41:45 `آتينا`; 41:48 `ضل`; 41:52 `أضل`.
- Synthesis: The causal bridge makes memory a custody process distinct from both delivery and later testimony. It supports the surah's message-response reading by showing that clear content can arrive yet become unavailable when it is not retained, while `الذكر` restores availability through recollection. Loss is thereby located in the receiver's custody, not in an absence or defect of the message.

### S11. P1-P3-P4: Counterfeit Report Reversed
- Reading type: latent/lexical
- Scene or process: P1, P3, and P4 bridge - contrast and role reversal: a speaker invents words, attributes them falsely, claims prophetic status, and is finally made the subject of an authoritative report.
- Active motifs: inventing or attributing words that were never spoken `quranic:root_001272:B005/m01`; asserting falsehood with no reality behind it `quranic:root_000127:B003/m01`; fraudulent claim to prophecy `quranic:root_001464:B004/m01`.
- Ayah anchors: 41:6 `قل`; 41:42 `الباطل`; 41:43 `يقال`; 41:50 `ليقولن`, `فلننبئن`.
- Synthesis: The contrast bridge sharpens the surah's revelation claim. The counterfeit speaker manufactures both wording and provenance, whereas the final reporting relation reverses the roles: the would-be source becomes the one authoritatively reported about. Authority moves from claimant to knower, clarifying why baseless speech cannot enter the protected text.

### S12. P2-P4: Office Passes; Account Does Not
- Reading type: latent/lexical
- Scene or process: P2-P4 bridge - role progression followed by contrast: a successor follows an absent holder, another stands in the station, and action continues in order, but moral account refuses the same transfer.
- Active motifs: one obligation or thing sufficing in another's place `quranic:root_000244:B002/m01`; successor arriving after loss and assuming the role `quranic:root_000433:B001/m01`; deputy standing in another's station `quranic:root_001273:B007/m01`; uninterrupted succession of acts or holders `quranic:root_001684:B002/m01`.
- Ayah anchors: 41:25 `خلفهم`; 41:27-28 `لنجزينهم`, `جزاء`; 41:30 `استقاموا`; 41:31 `أولياؤكم`; 41:45 `اختلف`; 41:50 `قائمة`.
- Synthesis: The role progression is social: offices and functions can pass to successors or deputies. The P2-P4 contrast usefully pressures that mechanism in accountability: although `جزاء` can carry a substitution sense, 41:46 attaches benefit and harm to the acting self, so no companion, successor, or claimed partner can serve as the bearer's moral deputy.

### S13. P1-P2-P4: A Fracture Set, Reinjured, or Healed
- Reading type: latent/lexical
- Scene or process: P1-P2-P4 bridge - causal sequence with opposed outcomes: a crooked fracture is set, but a treated wound can relapse, a set bone can break again, or the patient can recover.
- Active motifs: setting a fracture that has healed crooked `quranic:root_000015:B002/m01`; bodily or wound relapse after improvement `quranic:root_000996:B008/m01`; set bone broken again `quranic:root_000977:B011/m01`; patient recovering after illness `quranic:root_001397:B012/m01`.
- Ayah anchors: 41:3, 41:44 `عربيا`, `عربي`; 41:6, 41:13 `مثل`; 41:8 `أجر`; 41:24 `يستعتبوا`, `معتبين`.
- Synthesis: The clinical sequence gives the healing of 41:44 a concrete grammar of realignment, monitoring, and outcome. Repair addresses an established crookedness rather than merely soothing pain, while relapse and rebreaking show how an improved condition can be lost. The recovery branch completes the contrast and usefully pressures a passive reading of revelation as medicine: healing is a restoration that must take and hold.

### S14. P1-P4: Gaming Arrows Drawn From a Leather Lot-Case
- Reading type: latent/lexical
- Scene or process: P1-P4 bridge - contrast: a player draws among gaming arrows held in their leather case, including a named fifth arrow, and seeks victory through a wager that can involve deception.
- Active motifs: leather case holding gaming arrows `quranic:root_000532:B010/m01`; assembled lot of gaming arrows `quranic:root_000532:B010/m02`; named fifth maysir arrow `quranic:root_001533:B016/m01`; gambling victory and deception `quranic:root_001255:B007/m01`.
- Ayah anchors: 41:9, 41:14, 41:23, 41:29-30, 41:38, 41:43, 41:45-46, 41:50, 41:53-54 `رب`; 41:31, 41:46, 41:53 `أنفس`, `نفس`; 41:37 `القمر`.
- Synthesis: The lot scene materializes presumptive claims about the future as an opaque draw whose apparent winner may also deceive. The surah reverses that game structure: benefit and harm return to the acting self in 41:46, and neither conjecture nor a companion can manipulate the final allocation. Accountability is therefore not a fortunate arrow drawn from a concealed bundle.

### S15. P1-P4: The Staked Race and the Forbidden Side-Horse
- Reading type: latent/lexical
- Scene or process: P1-P4 bridge - shared race signature and reversal: a fitted racehorse contests a stake, an auxiliary horse is illicitly led beside the racer, and the winner reaches the goal.
- Active motifs: racehorse matching its hind hoofprints to its fore hoofprints `quranic:root_000347:B014/m01`; prize or stake placed between racers `quranic:root_000671:B002/m01`; forbidden side-horse introduced to cheat in a race `quranic:root_000262:B005/m01`; racer reaching the goal first `quranic:root_001684:B012/m01`.
- Ayah anchors: 41:15, 41:25, 41:53 `الحق`; 41:31, 41:34 `أولياؤكم`, `ولي`; 41:45 `سبقت`; 41:51 `جانبه`.
- Synthesis: The scene gives terms, bodily performance, attempted manipulation, and finish to a single contest. It usefully pressures the surah's boasts of strength and reliance on allies: an extra horse led at the racer's side is precisely an illicit effort to alter the outcome, while the claimed partners disappear when called. The word that has already preceded in 41:45 cannot be outpaced by importing an auxiliary advantage.

### S16. P1-P4: Perfume Prepared as a Transferable Coating
- Reading type: latent/lexical
- Scene or process: P1-P4 bridge - shared operation: camphor perfume is worked on a dedicated slab, applied as a coating, and leaves another thing carrying an acquired scent.
- Active motifs: dedicated perfume slab `quranic:root_000973:B012/m01`; camphor used as perfume `quranic:root_001307:B011/m01`; anointing or coating with perfume `quranic:root_000434:B010/m01`; scent or stench acquired from another thing `quranic:root_000609:B004/m01`.
- Ayah anchors: 41:9, 41:15, 41:21, 41:37 `خلق`; 41:14, 41:37, 41:46 `تعبدوا`, `للعبيد`; 41:16 `ريحا`; 41:7, 41:9, 41:14, 41:26-27, 41:29, 41:41, 41:50, 41:52 `كافرون`, `تكفرون`, `كفروا`, `كفرت`.
- Synthesis: The operation materializes the adornment of deeds in 41:25 as an applied sensory layer: coating can make another object acquire its scent without changing what bears the coating. Because the same transfer mechanism includes fragrance and stench, pleasant presentation cannot establish the quality of the underlying act. The scene therefore sharpens the later disclosure by bodies and deeds, where an acquired surface no longer controls the report.

### S17. P1-P4: A Water-Rich Well Worked by Pulley and Bucket
- Reading type: latent/lexical
- Scene or process: P1-P4 bridge - shared mechanism: abundant water below is reached through an upright pulley part, a one-handled bucket, and a balancing crosspiece until a full bucket becomes drink.
- Active motifs: water-rich well `quranic:root_001040:B005/m01`; upright part of a well pulley `quranic:root_001273:B012/m01`; elongated water-drawer's bucket with one handle `quranic:root_000737:B011/m01`; bucket handle or crosspiece that balances its load `quranic:root_000741:B008/m01`; water drawers drinking a full bucket `quranic:root_001274:B005/m01`.
- Ayah anchors: 41:3, 41:9, 41:12, 41:22, 41:36, 41:47 `يعلم`, `العالمين`, `العليم`, `علم`; 41:3, 41:6, 41:30, 41:40, 41:50 `قوم`, `استقيموا`, `استقاموا`, `القيامة`, `قائمة`; 41:4, 41:20, 41:22, 41:26, 41:36 `يسمع`, `سمعكم`, `تسمعوا`, `السميع`; 41:15 `قوة`; 41:33 `المسلمين`.
- Synthesis: The apparatus aligns latent senses of knowledge as a full well, hearing as the bucket's load-bearing handle, submission as the water-drawer's bucket, standing straight as the pulley support, and strength as drinking from the full vessel. It supports the surah's message-reception reading by distinguishing abundance at the source from successful access: the well need not be dry when the handle is unused or the lifting mechanism is misaligned. Refusal to hear is thus reframed as a failed draw rather than a defect in the available revelation.

### S18. P1-P2: The Fretted Oud as Ordered Sound
- Reading type: latent/lexical
- Scene or process: P1-P2 bridge - contrast: a wooden stringed instrument is organized by transverse frets and strings extended to its end, opposed to noise that suppresses articulated reception.
- Active motifs: wooden oud or mizhar instrument `quranic:root_001058:B010/m01`; transverse frets set across the instrument's face `quranic:root_000977:B009/m01`; strings extended along the instrument `quranic:root_000977:B009/m02`.
- Ayah anchors: 41:13, 41:15 `عاد`; 41:24 `يستعتبوا`, `معتبين`.
- Synthesis: The instrument is a mechanism of differentiated positions and sustained tension rather than an undivided sound source. That ordered construction usefully pressures the command in 41:26 to make noise against the Quran: adversarial noise works by erasing distinctions, whereas structured sound preserves intervals through which a sequence becomes intelligible. The scene therefore materializes the opposition between articulated speech and acoustic obstruction.


