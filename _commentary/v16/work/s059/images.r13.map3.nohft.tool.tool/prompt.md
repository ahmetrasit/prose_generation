Surah: 59. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (59:1 to 59:24), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s059/surah.r2/text.md =====
# Surah 59

- 59:1 سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 59:2 هُوَ ٱلَّذِىٓ أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ ۚ مَا ظَنَنتُمْ أَن يَخْرُجُوا۟ ۖ وَظَنُّوٓا۟ أَنَّهُم مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟ ۖ وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ ۚ يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ وَأَيْدِى ٱلْمُؤْمِنِينَ فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ
- 59:3 وَلَوْلَآ أَن كَتَبَ ٱللَّهُ عَلَيْهِمُ ٱلْجَلَآءَ لَعَذَّبَهُمْ فِى ٱلدُّنْيَا ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابُ ٱلنَّارِ
- 59:4 ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ ۖ وَمَن يُشَآقِّ ٱللَّهَ فَإِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- 59:5 مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ وَلِيُخْزِىَ ٱلْفَٰسِقِينَ
- 59:6 وَمَآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْهُمْ فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍۢ وَلَا رِكَابٍۢ وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- 59:7 مَّآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْ أَهْلِ ٱلْقُرَىٰ فَلِلَّهِ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ ۚ وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- 59:8 لِلْفُقَرَآءِ ٱلْمُهَٰجِرِينَ ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا وَيَنصُرُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ
- 59:9 وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ يُحِبُّونَ مَنْ هَاجَرَ إِلَيْهِمْ وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةًۭ مِّمَّآ أُوتُوا۟ وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- 59:10 وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ
- 59:11 ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟ يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًۭا وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ
- 59:12 لَئِنْ أُخْرِجُوا۟ لَا يَخْرُجُونَ مَعَهُمْ وَلَئِن قُوتِلُوا۟ لَا يَنصُرُونَهُمْ وَلَئِن نَّصَرُوهُمْ لَيُوَلُّنَّ ٱلْأَدْبَٰرَ ثُمَّ لَا يُنصَرُونَ
- 59:13 لَأَنتُمْ أَشَدُّ رَهْبَةًۭ فِى صُدُورِهِم مِّنَ ٱللَّهِ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَفْقَهُونَ
- 59:14 لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًۭى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍۭ ۚ بَأْسُهُم بَيْنَهُمْ شَدِيدٌۭ ۚ تَحْسَبُهُمْ جَمِيعًۭا وَقُلُوبُهُمْ شَتَّىٰ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ
- 59:15 كَمَثَلِ ٱلَّذِينَ مِن قَبْلِهِمْ قَرِيبًۭا ۖ ذَاقُوا۟ وَبَالَ أَمْرِهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- 59:16 كَمَثَلِ ٱلشَّيْطَٰنِ إِذْ قَالَ لِلْإِنسَٰنِ ٱكْفُرْ فَلَمَّا كَفَرَ قَالَ إِنِّى بَرِىٓءٌۭ مِّنكَ إِنِّىٓ أَخَافُ ٱللَّهَ رَبَّ ٱلْعَٰلَمِينَ
- 59:17 فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- 59:18 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- 59:19 وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- 59:20 لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- 59:21 لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- 59:22 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- 59:23 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- 59:24 هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/out/s059/surah.map3.nohft.tool/map.md (without ## Not carried) =====
# Surah 59 — map of image chains

Note: every Quran passage outside the surah cited below is recalled from memory and its wording checked against the lookup text. Dictionary members are quoted from dictionary.md; branch ids are those of the root heading.

## Chains

### 1. The fortress that withholds
The Nadir trust walls that "withhold" (مانعة) them from God; the dictionary gives withholding and impregnability to the names that open and close the surah (العزيز الحكيم), so the fortress claims what is God's. In 59:14 the enclosed villages and walls are named again, and the same ayah says they lack عقل, which the dictionary calls a fortress. Against this stands the Ansar's reed hut full of gaps (خصاصة) that holds, and a guard turned against the self's own withholding (شح).
- 59:2 حُصُونُهُم — ح ص ن B001 «الحصن كل موضع حصين لا يوصل إلى ما في جوفه» (ayn); «حصنت القرية إذا بنيت حولها» (sihah) — the sealed enclosure.
- 59:2 مَّانِعَتُهُمْ — م ن ع B003 «رجل منيع لا يخلص إليه وهو في عز ومنعة» (ayn) — the dictionary joins منع and عز in one phrase.
- 59:1/23/24 ٱلْعَزِيزُ — ع ز ز B001 «العزيز الممتنع فلا يغلبه شيء» (tahdhib); «العزة حالة مانعة للإنسان من أن يغلب» (mufradat) — the impregnability the walls imitate.
- 59:1/24 ٱلْحَكِيمُ — ح ك م B001 «حكم أصله منع منعا لإصلاح» (mufradat) — withholding that sets right.
- 59:14 قُرًى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍ — ج د ر B001 «الجدير مكان بني حواليه جدار مجدور» (ayn) — the walled place.
- 59:14 يَعْقِلُونَ — ع ق ل B007 «المعقل والعقل وهو الحصن» (maqayis); «عقل الظبي إذا امتنع في الجبل» (maqayis;tahdhib) — the one fortress they do not have.
- 59:2 لِأَوَّلِ — ء و ل B009 «الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن» (maqayis) — the creature that takes a mountain as fortress.
- 59:2 دِيَٰرِهِمْ — د و ر B002 «الدار المنزل اعتبارا بدورانها الذي لها بالحائط» (mufradat) — the house as walled circuit.
- 59:23 ٱلْمَلِكُ — م ل ك B001 «حائط ليس له ملاك أي تماسك» (mufradat) — the cohesion a wall needs.
- 59:23 ٱلْمُهَيْمِنُ — ه م ن B001 «من آمن غيره من الخوف» (sihah) — true safety given, not built.
- 59:9 خَصَاصَةٌ — خ ص ص B004 «الخص بيت من قصب أو شجر وذلك لما يرى فيه من الخصاصة» (mufradat) — the gapped reed hut, reversal of the fortress.
- 59:9 شُحَّ — ش ح ح B001 «الأصل فيه المنع ثم يكون منعا مع حرص» (maqayis); B007 «الشجاع وهو المانع ما وراء ظهره» (maqayis) — the inner withholding the Ansar are guarded from.
- 59:17 ٱلظَّٰلِمِينَ — ظ ل م B008 «الظلمة المانعون أهل الحقوق حقوقهم» — withholding as wrong.
Outside: 11:43 (Noah's son: «سَـَٔاوِىٓ إِلَىٰ جَبَلٍۢ يَعْصِمُنِى مِنَ ٱلْمَآءِ», Noah: «لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ»); 15:82 (Thamud carved mountain houses «ءَامِنِينَ»); 4:78 (to the hypocrites: «وَلَوْ كُنتُمْ فِى بُرُوجٍۢ مُّشَيَّدَةٍۢ», closing «لَا يَكَادُونَ يَفْقَهُونَ»); 40:21 (earlier peoples «أَشَدَّ مِنْهُمْ قُوَّةًۭ ... وَمَا كَانَ لَهُم مِّنَ ٱللَّهِ مِن وَاقٍۢ»); 33:26 (Qurayza brought down «مِن صَيَاصِيهِمْ»); 61:4 (believers in rank «كَأَنَّهُم بُنْيَٰنٌۭ مَّرْصُوصٌۭ», the living wall).

### 2. Siege by night, breach from within
God "comes" to them from an unreckoned side; the dictionary's night-raid joins the two words of 59:2 (أتى, بيوت). The siege engine throws, but the stone lands in hearts; the besieged then bore holes in their own houses with their own hands.
- 59:2 فَأَتَىٰهُمُ — ء ت ي B011 [fixed expression] «أتي فلان إذا أطل عليه العدو» (tahdhib) — the enemy looming.
- 59:2 بُيُوتَهُم — ب ي ت B004 «البيات والتبييت أن تأتي العدو ليلا» (maqayis) — the dictionary joins أتى and بيت: the night raid.
- 59:2 لَمْ يَحْتَسِبُوا — ح س ب B007 «الحسبان سهام صغار»; «حسبان من السماء بالبرد» — missiles from above they did not reckon.
- 59:2 وَقَذَفَ — ق ذ ف B001 «القذاف المنجنيق» (ayn;tahdhib); «القذف الرمي البعيد» (mufradat) — the catapult; its target is the heart.
- 59:2 يُخْرِبُونَ — خ ر ب B001 «أصل يدل على التثلم والتثقب» (maqayis); «كل ثقب مستدير فهو خربة» (sihah); B002 «الخراب ضد العمارة» — the breach made from inside.
- 59:2 بِأَيْدِيهِمْ — ي د ي B009 [fixed expression] «هذا ما قدمت يداك أي جنيته أنت» (sihah) — own hands as authors.
- 59:1/24 ٱلْأَرْضِ — ء ر ض B010 «الأرضة بالتحريك دويبة تأكل الخشب» (sihah) — the termite hollowing timber from within.
- 59:10 جَآءُو — ج ي ء (root_000282) B002 «الجيأة مجتمع ماء في هبطة حوالي الحصون» (tahdhib) — the moat round the fort.
- 59:21 خَٰشِعًا — خ ش ع B002 «جدار خاشع» (tahdhib) — the sunken wall.
Outside: 7:97 (warning to towns: «أَن يَأْتِيَهُم بَأْسُنَا بَيَٰتًۭا وَهُمْ نَآئِمُونَ»); 16:26 (earlier plotters: «فَأَتَى ٱللَّهُ بُنْيَٰنَهُم مِّنَ ٱلْقَوَاعِدِ فَخَرَّ عَلَيْهِمُ ٱلسَّقْفُ ... وَأَتَىٰهُمُ ٱلْعَذَابُ مِنْ حَيْثُ لَا يَشْعُرُونَ»); 34:14 (Solomon's staff eaten: «دَآبَّةُ ٱلْأَرْضِ تَأْكُلُ مِنسَأَتَهُۥ ۖ فَلَمَّا خَرَّ»); 4:81 (hypocrites say «طَاعَةٌۭ» then «بَيَّتَ طَآئِفَةٌۭ مِّنْهُمْ»); 33:13 (hypocrites: «إِنَّ بُيُوتَنَا عَوْرَةٌۭ»); 3:151 (رعب cast into hearts).

### 3. The hunt at the burrow
حشر names small burrowing creatures; the hypocrite is named from the jerboa's hidden exit, which it bursts when approached from its other door — one phrase holding أتى and خرج of 59:2 and 59:11. The الفاسقين are the mouse that leaves its hole; the خالدين share their root with the blind mole-rat, set against أولي الأبصار. The hunter's gear sits in other words: hide, snare, falcon and its jesses.
- 59:2 ٱلْحَشْرِ — ح ش ر B004 «حشرات الأرض دوابها الصغار كاليرابيع والضباب وما أشبهها» (maqayis) — the burrow-dwellers driven out.
- 59:11 نَافَقُوا — ن ف ق B003 «النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج» (maqayis;ayn;sihah;tahdhib); «سمي المنافق منافقا للنفق وهو السرب في الأرض» (tahdhib) — the hidden back door; B004 «النفاق الدخول في الشرع من باب والخروج عنه من باب» (mufradat).
- 59:5/19 ٱلْفَٰسِقِينَ — ف س ق B003 «سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها» (mufradat) — the mouse out of its house.
- 59:17 خَٰلِدَيْنِ — خ ل د B005 «الخلد ضرب من الجرذان عمي لم يخلق لها عيون» (ayn) — the blind burrower.
- 59:16/24 بَرِىٓءٌ — ب ر ء B007 «برأة الصائد ناموسه وهي قترته» (maqayis) — the hunter's hide; Satan's disavowal is a retreat into cover.
- 59:23 يُشْرِكُونَ — ش ر ك B006 «الشرك حبالة يرتبك فيها الصيد» (ayn) — the snare.
- 59:1/24 ٱلسَّمَٰوَٰتِ — س م و B006 «السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد» (sihah).
- 59:3 ٱلْجَلَآءَ — ج ل و B008 «البازي يجلي إذا آنس الصيد فرفع طرفه ورأسه» (ayn); 59:16 ٱلْعَٰلَمِينَ — ع ل م B006 «العلام الصقر» (tahdhib); 59:10 سَبَقُونَا — س ب ق B003 «سباقا البازي قيداه من سير أو غيره» (sihah) — falcon, its lifted gaze, its jesses.
- 59:8 لِلْفُقَرَآءِ — ف ق ر B007 «أفقرك الصيد فارمه» (mufradat) — prey exposing its back.
Outside: 9:56–57 (hypocrites: «لَوْ يَجِدُونَ مَلْجَـًٔا أَوْ مَغَٰرَٰتٍ أَوْ مُدَّخَلًۭا لَّوَلَّوْا۟ إِلَيْهِ وَهُمْ يَجْمَحُونَ»); 13:10 («مُسْتَخْفٍۭ بِٱلَّيْلِ وَسَارِبٌۢ بِٱلنَّهَارِ»); 63:4 (hypocrites «يَحْسَبُونَ كُلَّ صَيْحَةٍ عَلَيْهِمْ»).

### 4. Torrent from an unreckoned quarter; rain that never falls
The coming "from where they did not reckon" is, in the dictionary, the flood that arrives from a land where rain fell elsewhere; رعب is the torrent that fills the valley, عز the overpowering flood, حشر the hard year driving people into towns, وبال the heavy downpour the predecessors tasted. Reversed: the hypocrites are a cloud that only seems to rain (خيال, 59:6) and a promise of rain (نصر) that never comes (59:11–12).
- 59:2 فَأَتَىٰهُمُ ... مِنْ حَيْثُ لَمْ يَحْتَسِبُوا — ء ت ي B005 [fixed expression] «الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك» (jamhara); «سيل أتي وأتاوي إذا جاءك ولم يصبك مطره» (sihah).
- 59:2 ٱلرُّعْبَ — ر ع ب B002 «سيل راعب إذا ملأ الوادي» (maqayis;sihah;mufradat).
- 59:1/23/24 ٱلْعَزِيزُ — ع ز ز B008 «سيل عز وهو السيل الغالب» (maqayis); «العزاء السنة الشديدة».
- 59:2 ٱلْحَشْرِ — ح ش ر B002 [fixed expression] «حشرتهم السنة إذا أصابهم الضر حتى يهبطوا الأمصار» (jamhara); «حشرت السنة مال فلان أي أهلكته» (sihah).
- 59:2 يَحْتَسِبُوا — ح س ب B007 «حسبان من السماء بالبرد»; «الحسبان بالضم العذاب».
- 59:15 وَبَالَ — و ب ل B001 «الوبل والوابل المطر الشديد» (maqayis); B002 «الوبال الثقل» (jamhara).
- 59:21 أَنزَلْنَا — ن ز ل B006 «النازلة الشديدة من شدائد الدهر تنزل بالقوم» (ayn); 59:21 نَضْرِبُهَا — ض ر ب B013 «الضريب الصقيع كأن السماء ضربت به الأرض» (maqayis).
- 59:6 خَيْلٍ — خ ي ل B004 «الخيال غيم ينشأ يخيل إليك أنه ماطر» (ayn) — the cloud that looks like rain.
- 59:11–12 لَنَنصُرَنَّكُمْ / لَا يَنصُرُونَهُمْ — ن ص ر B004 «نصر الغيث البلاد أرواها» (ayn); «نصر القوم إذا أغيثوا» (tahdhib) — promised rain.
- 59:11 لَكَٰذِبُونَ — ك ذ ب B006 [fixed expression] «كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم» (mufradat) — the flow that stops.
- 59:9 شُحَّ — ش ح ح B004 [fixed expression] «أرض شحاح لا تسيل إلا من مطر جود» (tahdhib).
Outside: 10:24 (the rain-grown land: «وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا ... كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ»); 34:15–16 (Saba's two gardens and «سَيْلَ ٱلْعَرِمِ»); 24:43 (hail sent down «مِن جِبَالٍۢ فِيهَا مِنۢ بَرَدٍۢ ... يَكَادُ سَنَا بَرْقِهِۦ يَذْهَبُ بِٱلْأَبْصَٰرِ») with 24:44 («لَعِبْرَةًۭ لِّأُو۟لِى ٱلْأَبْصَٰرِ»); 2:19 (hypocrites as a cloudburst «فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ»); 2:264–265 (rain «وَابِلٌۭ» on a bare rock leaves it «صَلْدًۭا», on a garden makes it «فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ», for those who spend «ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ»).

### 5. Channels, basins and the trough
The fay' passage (59:6–10) is heard as irrigation: water from far off is channelled (آتى), caught in dug basins (أخذ, قرى, فقير, هجير, جيأة), held by banks (جدر), and comes to rest where it ends (انتهوا). Then the trough: camels drink till full (يحبون), the waterer draws for them (قبل), they turn away watered (صدر) or are driven off (رهبة); some stay thirsty (غل). The closing names hold water as life (الملك), the basin stone (القدوس), the bucket (السلام). Sweet water (عذب) turns into punishment; the predecessors taste unwholesome water (وبيل).
- 59:7 ءَاتَىٰكُمُ — ء ت ي B004 «الأتي الجدول يؤتيه الرجل إلى أرضه» (sihah); «أت لهذا الماء أي سهل جريه» (maqayis).
- 59:7 فَخُذُوهُ — ء خ ذ B006 «الإخاذة والإخذ ما حفرت لنفسك كهيئة الحوض تمسك الماء أياما» (ayn).
- 59:7 فَٱنتَهُوا — ن ه ي B004 «النهي والنهي الغدير لأن الماء ينتهي إليه» (maqayis); «تناهى الماء إذا وقف في الغدير وسكن» (sihah).
- 59:7 ٱلْقُرَىٰ — ق ر ي B002 «قريت الماء في الحوض أي جمعت» (sihah).
- 59:8 لِلْفُقَرَآءِ — ف ق ر B005 «الفقير مخرج الماء من القناة» (maqayis); «لكل حفيرة يجتمع فيها الماء فقير» (mufradat).
- 59:8 ٱلْمُهَٰجِرِينَ — ه ج ر B011 «الهجير الحوض الكبير سمي لأنه شيء يقتطع للماء» (maqayis).
- 59:8 وَيَنصُرُونَ — ن ص ر B007 «تجيء من مكان بعيد حتى تقع في مجتمع الماء» — channels from afar.
- 59:14 جُدُرٍ — ج د ر B001 «ما رفع من أعضاد المزرعة لتمسك الماء كالجدار» (tahdhib).
- 59:9 يُحِبُّونَ — ح ب ب B006 «تحبب الحمار إذا امتلأ من الماء» (sihah); «أول الري التحبب» (tahdhib).
- 59:9 قَبْلِهِمْ — ق ب ل B014 «القبل أن يورد الرجل إبله ثم يستقي لها» (jamhara).
- 59:9 صُدُورِهِمْ — ص د ر B003 «الصدر الانصراف عن الورد وعن كل أمر» (ayn;tahdhib).
- 59:9 أَنفُسِهِمْ — ن ف س B008 «يقال للماء نفس ولأن قوام النفس به» (maqayis).
- 59:10 غِلًّا — غ ل ل B002 «الغلة والغليل حرارة العطش» (jamhara;sihah;tahdhib); 59:6 يُسَلِّطُ — س ل ط B007 «والسلاط الغليل» (ayn).
- 59:13 رَهْبَةً — ر ه ب B002 «الإرهاب وهو قدع الإبل من الحوض وذيادها» (maqayis).
- 59:16 ٱلشَّيْطَٰنِ — ش ط ن B002 «الشطن الحبل الطويل الشديد الفتل يستقى به» (ayn;tahdhib); B001 «بئر شطون بعيدة القعر» (sihah).
- 59:23 ٱلْمَلِكُ — م ل ك B007 [fixed expression] «الماء ملك أمر أي يقوم به الأمر» (sihah); 59:23 ٱلْقُدُّوسُ — ق د س B010 «القداس الحجر ينصب على مصب الماء في الحوض» (tahdhib); 59:23 ٱلسَّلَٰمُ — س ل م B011 «السلم الدلو لها عروة واحدة نحو دلو السقائين» (sihah).
- 59:17 ٱلظَّٰلِمِينَ — ظ ل م B004 «ظلم الوادي إذا بلغ الماء منه موضعا لم يكن بلغه» (sihah;tahdhib) — water overrunning its bed.
- 59:18 خَبِيرٌ — خ ب ر B002 «الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء» (jamhara); 59:24 ٱلْخَٰلِقُ — خ ل ق B011 «الخليقة نقر في صخرة يجتمع فيه ماء السماء» (jamhara).
- 59:3/15 عَذَابُ — ع ذ ب B001 «عذب الماء عذوبة فهو عذب طيب» (maqayis;ayn;tahdhib); 59:15 ذَاقُوا وَبَالَ — و ب ل B003 «ماء وبيل ووبيء ووخيم» (tahdhib); ذ و ق B002 «أذاقه الله وبال أمره» (sihah) — the dictionary joins ذاق and وبال.
- 59:20 ٱلْفَآئِزُونَ — ف و ز B003 «المفازة الفلاة التي لا ماء فيها» (tahdhib); «سميت مفازة تفاؤلا بالسلامة والفوز».
Outside: 54:28 (Thamud's water rota: «أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ»); 23:18 («وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ»); 15:22 («وَمَآ أَنتُمْ لَهُۥ بِخَٰزِنِينَ»); 47:15 (garden rivers of water and milk «كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ»).

### 6. Splitting
The dictionary defines شقاق by صدع and by the parting of a community, so 59:4 and 59:21 are one word-field: those who split from God split among themselves (59:14), while the farmer's splitting of the soil is success (المفلحون) and the mountain's crack is awe.
- 59:4 شَآقُّوا — ش ق ق B001 «شققت الشيء أشقه شقا إذا صدعته» (maqayis); «الشقاق تشقق الجلد والصدوع في الجبال والأرضين» (tahdhib); B004 «الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت» (maqayis).
- 59:21 مُّتَصَدِّعًا — ص د ع B001 «الصدع شق في شيء له صلابة» (tahdhib); B005 «تصدع القوم إذا تفرقوا» (maqayis;sihah;tahdhib).
- 59:14 شَتَّىٰ — ش ت ت B001 «أصل يدل على تفرق وتزيل» (maqayis); B003 «ارتفاع الالتئام بينهما» (mufradat).
- 59:14 بَيْنَهُمْ — ب ي ن B001 «البين الفراق» (maqayis;sihah); B003 «لقد تقطع بينكم أي وصلكم» (mufradat) — the between that is both bond and severance.
- 59:5 قَطَعْتُم — ق ط ع B007 «قطع رحمه قطيعة» (sihah).
- 59:9 ٱلْمُفْلِحُونَ — ف ل ح B001 «أصل يدل على شق» (maqayis); «الحديد بالحديد يفلح أي يشق أو يقطع».
- 59:9 أَنفُسِهِمْ — ن ف س B009 [fixed expression] «تنفست القوس انشقت» (maqayis).
- 59:16/22 ٱلْعَٰلَمِينَ — ع ل م B004 «العلم الشق في الشفة العليا» (maqayis); with ف ل ح B002 «الأفلح المشقوق الشفة السفلى» — upper and lower cleft.
Outside: 8:13 (Badr, identical wording «ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ ... شَدِيدُ ٱلْعِقَابِ»); 2:74 (hearts harder than stones, «وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ»); 30:43 («يَوْمَئِذٍۢ يَصَّدَّعُونَ»); 50:44 («يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًۭا ۚ ذَٰلِكَ حَشْرٌ»); 3:103 («وَلَا تَفَرَّقُوا۟ ... فَأَلَّفَ بَيْنَ قُلُوبِكُمْ»).

### 7. Seed covered, soil split, sprout breaking out
The كافر is the sower who covers seed; the مفلح the ploughman who splits earth; the خبير the sharecropper. The plant splits the ground (صدع), the earth shows its growth (نظر), dry earth without rain is خاشعة. The soft, good earth (أريضة) is described with the word لينة.
- 59:2/11/16 كَفَرُوا — ك ف ر B008 «الكافر الزارع لأنه يغطي البذر بالتراب» (sihah).
- 59:9 ٱلْمُفْلِحُونَ — ف ل ح B003 «سمي الأكار فلاحا لأنه يشق الأرض».
- 59:18 خَبِيرٌ — خ ب ر B003 «الخبير الأكار»; «المخابرة المزارعة بالنصف أو الثلث» (maqayis).
- 59:21 مُّتَصَدِّعًا — ص د ع B003 «الصدع النبات لأنه يصدع الأرض» (maqayis).
- 59:1/24 ٱلْأَرْضِ — ء ر ض B002 «أرض أريضة لينة طيبة» (maqayis;ayn) — joins earth with the word of 59:5.
- 59:9 يُحِبُّونَ — ح ب ب B001 «الحب والحبة في الحنطة والشعير وبزور الرياحين».
- 59:12 ٱلْأَدْبَٰرَ — د ب ر B015 «الدبار المشارات من الزرع» (maqayis).
- 59:14 جُدُرٍ — ج د ر B004 «الجدر النبات؛ أجدر المكان وجدر إذا ظهر نباته» (maqayis).
- 59:18 وَلْتَنظُرْ — ن ظ ر B004 «نظرت الأرض أرت نباتها» (maqayis); 59:7 ٱلسَّبِيلِ — س ب ل B008 «أسبل الزرع إذا خرج سنبله» (maqayis).
- 59:21 خَٰشِعًا — خ ش ع B002 «إذا يبست الأرض ولم تمطر قيل قد خشعت» (tahdhib).
Outside: 48:29 (the Companions «يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا» — 59:8's wording — likened to «زَرْعٍ أَخْرَجَ شَطْـَٔهُۥ ... يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ»); 57:20 («كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ»); 80:24–27 («فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ ... ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا فَأَنۢبَتْنَا فِيهَا حَبًّۭا»); 30:9 (earlier peoples «أَثَارُوا۟ ٱلْأَرْضَ وَعَمَرُوهَآ»).

### 8. Descent on the mountain
59:21 is a rain scene: what is sent down falls as rain falls; the mountain is hard, coarse and dry; خاشع is dry land lying low without rain; متصدع is earth cracking as the plant comes up; خشية shares its root with dryness and shrivelled dates. The parable (مثل) is a lesson (عبرة) for those who think.
- 59:21 أَنزَلْنَا — ن ز ل B001 «هبوط شيء ووقوعه؛ نزل المطر من السماء نزولا» (maqayis).
- 59:21 جَبَلٍ — ج ب ل B003 «شيء جبل غليظ جاف» (sihah); B005 [fixed expression] «أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه» (jamhara); B008 «الجبل الشجر اليابس» (ayn;tahdhib).
- 59:21 خَٰشِعًا — خ ش ع B001 «الخشوع رميك ببصرك إلى الأرض» (ayn); «إذا ضرع القلب خشعت الجوارح» (mufradat); B002 «أرض خاشعة هامدة» (tahdhib).
- 59:21 مُّتَصَدِّعًا — ص د ع B001, B003 (above).
- 59:21 خَشْيَةِ — خ ش ي B001 «الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم» (mufradat); B004 «الخشي وهو اليابس» (sihah).
- 59:21 نَضْرِبُهَا — ض ر ب B013 «ضرب الأرض بالمطر» (mufradat); «الضرب المطر اللين» (jamhara).
- 59:21 ٱلْأَمْثَٰلُ — م ث ل B011 «يكون المثل بمعنى العبرة» (tahdhib); 59:21 يَتَفَكَّرُونَ — ف ك ر B001 «تردد القلب في الشيء» (maqayis).
- 59:5 لِّينَةٍ — ل ي ن B005 [fixed expression] «تلين جلودهم وقلوبهم إلى ذكر الله إشارة إلى إذعانهم للحق وقبولهم له بعد تأبيهم منه وإنكارهم إياه» (mufradat) — softening as the answer to hardness.
Outside: 41:39 («تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ»); 22:5 (the earth «هَامِدَةًۭ»); 2:74 (above); 39:23 (the Book makes skins shiver «ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ»); 57:16–17 («أَن تَخْشَعَ قُلُوبُهُمْ ... فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ», then «يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا»); 7:143 (Moses: «فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ جَعَلَهُۥ دَكًّۭا»); 13:31 («قُرْءَانًۭا سُيِّرَتْ بِهِ ٱلْجِبَالُ أَوْ قُطِّعَتْ بِهِ ٱلْأَرْضُ»); 33:72 (the trust refused by the mountains).

### 9. The palm grove
59:5 names palms cut by permission or left standing on their roots; the dictionary then finds the palm in many other words — its heart, its blossom-sheath, offshoots without roots, young shoots, ripe dates leaving their skin, the tall palm out of reach, the palm cluster, and the Garden itself.
- 59:5 لِّينَةٍ — ل ي ن B006 «لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع» (mufradat).
- 59:5 قَطَعْتُم ... فَبِإِذْنِ — ق ط ع B013 [fixed expression] «أقطعته قضبانا أي أذنت له في قطعها» (sihah) — the dictionary joins قطع and إذن.
- 59:5 قَآئِمَةً عَلَىٰٓ أُصُولِهَا — ق و م B002 «تركتموها قائمة على أصولها» (mufradat); ء ص ل B002 «النخل بأرضنا أصيل أي لا يفنى ولا يزول» (ayn;tahdhib); B001 «استأصله أي قلعه من أصله» (sihah).
- 59:5 تَرَكْتُمُوهَا — ت ر ك B002 «كم تركوا من جنات» (mufradat).
- 59:5/19 ٱلْفَٰسِقِينَ — ف س ق B002 [fixed expression] «فسقت الرطبة عن قشرها» (maqayis;sihah).
- 59:2 قُلُوبِهِمُ — ق ل ب B003 «قلب النخلة شحمتها» (ayn); «قلبت النخلة نزعت قلبها» (maqayis;jamhara;sihah).
- 59:2 كَفَرُوا — ك ف ر B010 «الكافور الطلع ووعاء طلع النخل» (sihah).
- 59:6 رِكَابٍ — ر ك ب B007 «الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق» (ayn;sihah;tahdhib) — rootless, against «قائمة على أصولها».
- 59:6 شَيْءٍ — ش ي ء (root_000831) B008 «الإشاء الصغار من النخل واحدها أشاءة».
- 59:7 ءَاتَىٰكُمُ — ء ت ي B007 «إتاء النخلة ريعها وزكاؤها وكثرة ثمارها» (tahdhib).
- 59:10 غِلًّا — غ ل ل B003 «الماء الذي يجري في أصول الشجر» (tahdhib).
- 59:11 نُطِيعُ — ط و ع B007 «أطاع النخل والشجر إذا أدرك ثمره وأمكن أن يجتنى» (sihah).
- 59:21 خَشْيَةِ — خ ش ي B004 «خشت النخلة تخشو إذا أحشفت» (sihah).
- 59:20 ٱلْجَنَّةِ — ج ن ن B003 «العرب تسمي النخيل جنة» (sihah).
- 59:23 ٱلْجَبَّارُ — ج ب ر B002 «الجبار من النخل الذي قد فات اليد» (jamhara;sihah;tahdhib;mufradat); 59:24 ٱلْمُصَوِّرُ — ص و ر B005 «الصور جماعة النخل وهو الحائش» (maqayis).
Outside: 14:24–26 (the good tree «أَصْلُهَا ثَابِتٌۭ» and the bad «ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ»); 69:7 (ʿĀd lying «كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍۢ»); 44:25 (Pharaoh's people «كَمْ تَرَكُوا۟ مِن جَنَّٰتٍۢ وَعُيُونٍۢ»); 68:17–25 (garden owners swear to cut it at dawn, «أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ», «وَغَدَوْا۟ عَلَىٰ حَرْدٍۢ قَٰدِرِينَ», it becomes «كَٱلصَّرِيمِ»); 18:42 (the owner «يُقَلِّبُ كَفَّيْهِ» over his ruined palm-garden); 2:266 (a garden «مِّن نَّخِيلٍۢ» struck by «إِعْصَارٌۭ فِيهِ نَارٌۭ»); 6:141 (palms, «وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ»); 50:9–11 (rain, gardens, «ٱلنَّخْلَ بَاسِقَٰتٍۢ لَّهَا طَلْعٌۭ», «كَذَٰلِكَ ٱلْخُرُوجُ»).

### 10. Night cover, dawn split, the hidden and the witnessed
Covering words (كفر, غفر, جنة, وراء, غيب) are night words; ظلم is darkness against النار/نور; خشع is the sun eclipsed and stars sinking; صدع and نفس are the dawn breaking; غد is early morning; جلاء is the clear day; 59:22 joins غيب and شهادة.
- 59:2 كَفَرُوا — ك ف ر B001 «الستر والتغطية» (maqayis); B002 «الليل كافر لأنه ستر بظلمته» (tahdhib); «كفرت الشمس النجوم» (mufradat).
- 59:10 ٱغْفِرْ — غ ف ر B001 «الغفر الستر» (maqayis).
- 59:20 ٱلْجَنَّةِ — ج ن ن B002 «جنان الليل سواده وستره الأشياء» (maqayis).
- 59:14 وَرَآءِ — و ر ي B005 «التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره» (tahdhib).
- 59:11 نَافَقُوا — ن ف ق B004 «النفاق لأن صاحبه يكتم خلاف ما يظهر» (maqayis).
- 59:22 ٱلْغَيْبِ — غ ي ب B001 «أصل صحيح يدل على تستر الشيء عن العيون؛ ... غابت الشمس أي غربت».
- 59:17 ٱلظَّٰلِمِينَ — ظ ل م B001 «الظلمة خلاف النور» (maqayis;sihah); 59:3 ٱلنَّارِ — ن و ر B002 «النور والنار سميا بذلك من طريقة الإضاءة» (maqayis).
- 59:21 خَٰشِعًا — خ ش ع B003 [fixed expression] «خشعت الكواكب إذا دنت من المغيب» (tahdhib).
- 59:21 مُّتَصَدِّعًا — ص د ع B006 «الصديع الصبح» (sihah;tahdhib); 59:9 أَنفُسِهِمْ — ن ف س B009 [fixed expression] «تنفس الصبح أي تبلج» (sihah).
- 59:18 لِغَدٍ — غ د و B001 «الغدوة ما بين صلاة الغداة وطلوع الشمس» (sihah).
- 59:3 ٱلْجَلَآءَ — ج ل و B001 «انكشاف الشيء وبروزه» (maqayis); B007 «جلاء يوم واحد أي بياض يوم» (ayn;tahdhib).
- 59:22 ٱلشَّهَٰدَةِ — ش ه د B001 «الشهود والشهادة الحضور مع المشاهدة» (mufradat).
Outside: 6:76 («فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ»); 81:18 («وَٱلصُّبْحِ إِذَا تَنَفَّسَ»); 57:13 (to the hypocrites «ٱرْجِعُوا۟ وَرَآءَكُمْ ... فَضُرِبَ بَيْنَهُم بِسُورٍۢ لَّهُۥ بَابٌۢ بَاطِنُهُۥ فِيهِ ٱلرَّحْمَةُ وَظَٰهِرُهُۥ مِن قِبَلِهِ ٱلْعَذَابُ»); 2:17 (hypocrites' fire put out «وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ»); 35:20 («وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ»).

### 11. Armour
Fortress, eyes, leaving, guarding, forgiving, rancour and garden all have armour senses: the fortifying mail, the shield, the iron helmet, the protective cover, the mail coif, the shirt under the mail, the shield that screens.
- 59:2 حُصُونُهُم — ح ص ن B001 «يتجوز به في كل تحرز ومنه درع حصينة» (mufradat).
- 59:2 ٱلْأَبْصَٰرِ — ب ص ر B005 «البصيرة الدرع وما لبس من السلاح فهو بصائر السلاح» (ayn;tahdhib).
- 59:5 تَرَكْتُمُوهَا — ت ر ك B008 «التريكة بيضة النعام التي تتركها والتركة البيضة من الحديد» (sihah); «التريكة أصله البيض المتروك في مفازته ويسمى بيضة الحديد بها» (mufradat).
- 59:9/18 يُوقَ / ٱتَّقُوا — و ق ي B002 «اتق الله توقه أي اجعل بينك وبينه كالوقاية» (maqayis).
- 59:10 ٱغْفِرْ — غ ف ر B001 «المغفر وقاية للرأس» (ayn) — the dictionary joins غفر and وقي.
- 59:10 غِلًّا — غ ل ل B007 «الغلالة شعار يلبس تحت الثوب وبطانة تلبس تحت الدرع» (maqayis); B001 «غلائل الدروع مساميرها المدخلة فيها» (tahdhib).
- 59:20 ٱلْجَنَّةِ — ج ن ن B008 «المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك» (ayn).
- 59:2 كَفَرُوا — ك ف ر B001 «تكفر في السلاح» (mufradat); 59:14 بَأْسُهُم — ب ء س B001 «البأس الشدة في الحرب» (maqayis;sihah).
Outside: 21:80 (David's mail «لِتُحْصِنَكُم مِّنۢ بَأْسِكُمْ»); 16:81 («سَرَٰبِيلَ تَقِيكُم بَأْسَكُمْ», with «مِّنَ ٱلْجِبَالِ أَكْنَٰنًۭا»); 63:2 and 58:16 (hypocrites «ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ»).

### 12. Firestick and spark
The شح of 59:9 is a firestick that gives no fire; وراء of 59:14 is the firestick that does, and its idiom is giving aid — the aid the hypocrites promised. Horses' hooves strike useless sparks (59:6, 59:9); fire is seen from afar; at the end fire is the dwelling.
- 59:9 شُحَّ — ش ح ح B003 [fixed expression] «الزند الشحاح الذي لا يوري» (maqayis;sihah).
- 59:14 وَرَآءِ — و ر ي B002 «ورى الزند خرجت ناره» (maqayis;jamhara;sihah;mufradat); B003 [fixed expression] «لوريت عن مولاك أي نصرته ودفعت عنه» (tahdhib).
- 59:9 يُحِبُّونَ — ح ب ب B011 «نار الحباحب ما أورت الخيل لا ينتفع به» (maqayis;sihah;tahdhib) — joins حب, وري and خيل (59:6).
- 59:6 يُسَلِّطُ — س ل ط B005 «السليط ما يضاء به، ومن هذا قيل للزيت السليط» (tahdhib).
- 59:6 كُلِّ — ك ل ل B011 «انكل السحاب بالبرق إذا تبسم بالبرق» (tahdhib).
- 59:3/17/20 ٱلنَّارِ — ن و ر B003 [fixed expression] «تنورت النار من بعيد: تبصرتها» (sihah).
Outside: 56:71–72 («أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ»); 100:1–2 (charging horses «فَٱلْمُورِيَٰتِ قَدْحًۭا»); 2:17 (hypocrites «ٱسْتَوْقَدَ نَارًۭا» and lose its light); 5:64 (of the Jews, «كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ»).

### 13. What is thrust into the breast
The surah keeps putting things into hearts and chests: terror thrown in fills them like a flood (59:2), the gallop becomes a throbbing heart (59:6), the chest is free of need that is also doubt (59:9), rancour is driven in like a nail (59:10), fear sits on the breastbone (59:13), hearts scatter (59:14). Against these: stillness (سكينة), and the heart as the body's mainstay.
- 59:2 وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ — ق ذ ف B001 «القذف الرمي بالسهم والحصى» (ayn;tahdhib); ر ع ب B002 «رعبت الحوض إذا ملأته» (maqayis;sihah).
- 59:6 أَوْجَفْتُمْ — و ج ف B002 «قلب واجف» (sihah); «قلوب يومئذ واجفة أي مضطربة» (mufradat).
- 59:9 فِى صُدُورِهِمْ حَاجَةً — ح و ج B002 [fixed expression] «ما في صدري به حوجاء ولا لوجاء ولا شك ولا مرية بمعنى واحد» (sihah) — the dictionary joins صدر and حاجة; B003 «الحاج ضرب من الشوك» — a thorn.
- 59:10 غِلًّا — غ ل ل B001 «غللت الشيء في الشيء إذا أثبته فيه كأنه غرزته» (maqayis); B005 «الغل وهو الضغن ينغل في الصدر» (maqayis).
- 59:13 رَهْبَةًۭ فِى صُدُورِهِم — ر ه ب B007 «الرهابة عظم الصدر الذي تقع عليه القلادة» (jamhara); B001 «الرهبة والرهب مخافة مع تحرز واضطراب» (mufradat).
- 59:2/10/14 قُلُوب — ق ل ب B016 «قلبته أي أصبت قلبه» (sihah).
- 59:9 يُحِبُّونَ — ح ب ب B004 [fixed expression] «حبة القلب سويداؤه ويقال ثمرته» (maqayis;sihah).
- 59:23 ٱلْمَلِكُ — م ل ك B005 [fixed expression] «القلب ملاك الجسد» (ayn;sihah;mufradat); 59:20 ٱلْجَنَّةِ — ج ن ن B010 «الجنان القلب لكونه مستورا عن الحاسة» (mufradat).
- 59:7 ٱلْمَسَٰكِينِ — س ك ن B001 «خلاف الاضطراب والحركة»; B005 «أنزل السكينة في قلوب المؤمنين».
Outside: 33:26 (Qurayza: «وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ»); 79:8 («قُلُوبٌۭ يَوْمَئِذٍۢ وَاجِفَةٌ»); 15:47 and 7:43 («وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ»; 15:47 adds «إِخْوَٰنًا»); 22:46 («تَعْمَى ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ»); 3:167 (hypocrites «يَقُولُونَ بِأَفْوَٰهِهِم مَّا لَيْسَ فِى قُلُوبِهِمْ»); 9:77 («فَأَعْقَبَهُمْ نِفَاقًۭا فِى قُلُوبِهِمْ»); 63:3 («فَطُبِعَ عَلَىٰ قُلُوبِهِمْ فَهُمْ لَا يَفْقَهُونَ»); 9:14 («وَيَشْفِ صُدُورَ قَوْمٍۢ مُّؤْمِنِينَ»).

### 14. Gathering and scattering
A people driven together (حشر), a gathered battalion (الكتاب), villages as gatherings, the whole community coming with nobody left behind (جاءوا + غفر), and the dictionary's own pairing of جمع with شتى: "they seem together but their hearts are scattered."
- 59:2 ٱلْحَشْرِ — ح ش ر B001 «الحشر الجمع مع سوق» (maqayis).
- 59:14 جَمِيعًا ... شَتَّىٰ — ج م ع B002 «جماع الناس أخلاطهم وهم الأشابة من قبائل شتى» (sihah); B001 «الجمع خلاف التفريق» (jamhara).
- 59:2/11 ٱلْكِتَٰبِ — ك ت ب B001 «أصل صحيح واحد يدل على جمع شيء إلى شيء» (maqayis); «الكتيبة جماعة مستحيزة» (sihah;tahdhib).
- 59:7/14 ٱلْقُرَىٰ — ق ر ي B001 «القرية سميت قرية لاجتماع الناس فيها» (maqayis); 59:21 ٱلْقُرْءَانَ — ق ر ء B001 «أصل صحيح يدل على جمع واجتماع».
- 59:10 جَآءُو ... ٱغْفِرْ — غ ف ر B008 [fixed expression] «أي جاءوا بجماعتهم: الشريف والوضيع، ولم يتخلف أحد» (sihah).
- 59:6/7 أَفَآءَ — ف ي ء B004 «الفئة الجماعة المتظاهرة التي يرجع بعضهم إلى بعض في التعاضد» (mufradat).
- 59:2 أَيْدِى — ي د ي B016 [fixed expression] «المسلمون يد على من سواهم أي كلمتهم ونصرتهم واحدة» (tahdhib); B011 [fixed expression] «ذهب القوم أيدي سبا أي متفرقين في كل وجه» (tahdhib).
- 59:21 جَبَلٍ — ج ب ل B002 «الجبل الجماعة العظيمة الكثيرة» (maqayis).
- 59:5 قَطَعْتُم — ق ط ع B008 [fixed expression] «قطعناهم في الأرض أمما أي فرقناهم فرقا» (tahdhib); 59:21 مُّتَصَدِّعًا — ص د ع B005 (above).
Outside: 3:103 («وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟ ... فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًۭا»); 8:63 («لَوْ أَنفَقْتَ مَا فِى ٱلْأَرْضِ جَمِيعًۭا مَّآ أَلَّفْتَ بَيْنَ قُلُوبِهِمْ ... إِنَّهُۥ عَزِيزٌ حَكِيمٌۭ»); 61:4 (above).

### 15. Front and back, heel and track
Turning the back (59:12) is defined through the heel, the same root as the punishment (59:4, 59:7) and the end (59:17); the dictionary places ولى, دبر and عقب in one phrase. Those who came after walk in the track of those who went before (59:9–10); the self sends ahead what lies in front, as against behind (59:14) and last (59:3); planning means looking to the outcome (59:18).
- 59:12 لَيُوَلُّنَّ ٱلْأَدْبَٰرَ — و ل ي B007 [fixed expression] «ولى هاربا أي أدبر» (sihah); د ب ر B001 «الدبر خلاف القبل».
- 59:4/7 ٱلْعِقَابِ, 59:17 عَٰقِبَتَهُمَآ — ع ق ب B002 «العقب مؤخر القدم» (ayn); B003 [fixed expression] «ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر» (sihah); B007 «سميت عقوبة لأنها تكون آخرا وثاني الذنب» (maqayis).
- 59:10 بَعْدِهِمْ — ب ع د B002 «وما خلف بعقبه فهو من بعده» (ayn) — the dictionary joins بعد and عقب.
- 59:9/15 قَبْلِهِمْ — ق ب ل B001 «القبل خلاف الدبر» (ayn;tahdhib); 59:10 سَبَقُونَا — س ب ق B001 «أصل السبق التقدم في السير» (mufradat).
- 59:9 يُؤْثِرُونَ — ء ث ر B004 «الأثر الاستقفاء والاتباع وذهبت في إثره» (maqayis).
- 59:18 قَدَّمَتْ — ق د م B004 «قدام خلاف وراء والقدم ضد الأخر» (ayn) — joins 59:18 with 59:14 and 59:3.
- 59:14 وَرَآءِ — و ر ي B006 «وراءك يكون من خلف ويكون من قدام» (maqayis); 59:3 ٱلْءَاخِرَةِ — ء خ ر B001 «الآخر نقيض المتقدم» (maqayis).
- 59:12 ٱلْأَدْبَٰرَ — د ب ر B006 «التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته» (sihah;tahdhib) — joins دبر with نظر (59:18), عاقبة (59:17) and أول (59:2).
- 59:11 لَكَٰذِبُونَ — ك ذ ب B007 [fixed expression] «كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه» (jamhara).
Outside: 8:48 (Badr: Satan «نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌۭ مِّنكُمْ ... إِنِّىٓ أَخَافُ ٱللَّهَ ۚ وَٱللَّهُ شَدِيدُ ٱلْعِقَابِ» — 59:16–17 staged with the heel); 3:111 («يُوَلُّوكُمُ ٱلْأَدْبَارَ ثُمَّ لَا يُنصَرُونَ»); 48:22; 9:25 (Hunayn: «فَلَمْ تُغْنِ عَنكُمْ شَيْـًۭٔا ... ثُمَّ وَلَّيْتُم مُّدْبِرِينَ»); 9:100 («ٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم»); 75:13 and 82:5 («مَا قَدَّمَتْ وَأَخَّرَتْ»); 63:10 («لَوْلَآ أَخَّرْتَنِىٓ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ فَأَصَّدَّقَ»); 30:9, 40:21, 47:10 («فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ»).

### 16. The hand
Own hands bore into their houses (59:2), and the dictionary's "what your hands sent ahead" joins that hand to قدمت of 59:18. Between them, wealth passes hand to hand (دولة), is taken and given, and the hand is favour and authority.
- 59:2 بِأَيْدِيهِمْ — ي د ي B001 «اليَد الجارحة» (mufradat); B009 [fixed expression] (above).
- 59:7 دُولَةًۢ — ي د ي B007 «أعطيته مياداة أي من يدي إلى يده» (sihah); د و ل B001 «تداول القوم الشيء بينهم إذا صار من بعضهم إلى بعض» (maqayis).
- 59:7 فَخُذُوهُ — ء خ ذ B001 «خلاف العطاء وهو التناول» (tahdhib); 59:7/9 ءَاتَىٰ / أُوتُوا — ء ت ي B002 «الإيتاء الإعطاء».
- 59:9 — ي د ي B003 «اليد النعمة والإحسان» (sihah;tahdhib;mufradat).
- 59:6 يُسَلِّطُ — ي د ي B005 «اليد السلطان» (tahdhib).
- 59:18 تَعْمَلُونَ — ع م ل B006 «العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره» (tahdhib).
- 59:23 ٱلْجَبَّارُ — ج ب ر B002 «الجبار الذي طال وفات اليد» (maqayis).
Outside: 78:40 («يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ»); 18:57 («وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ»); 2:195 («وَلَا تُلْقُوا۟ بِأَيْدِيكُمْ إِلَى ٱلتَّهْلُكَةِ»); 9:67 (hypocrites «وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ»); 9:14 («يُعَذِّبْهُمُ ٱللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ»); 5:64 («غُلَّتْ أَيْدِيهِمْ»).

### 17. Exit, the far road, the new lodging
A people is brought out of its abode (59:2–3), migrates from house to house (59:8–9), travels far roads as stranded wayfarers whom highwaymen rob (59:7 with قطع of 59:5), and arrives at a lodging made ready (59:9).
- 59:2/8 أَخْرَجَ / أُخْرِجُوا — خ ر ج B001 «خرج خروجا برز من مقره أو حاله» (mufradat).
- 59:2 ٱلْحَشْرِ — ح ش ر B001 «إخراج الجماعة عن مقرهم وإزعاجهم عنه إلى الحرب ونحوها» (mufradat) — joins حشر and the أخرج of the same ayah.
- 59:3 ٱلْجَلَآءَ — ج ل و B004 «أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها» (mufradat).
- 59:8/9 ٱلْمُهَٰجِرِينَ / هَاجَرَ — ه ج ر B002 «هاجر القوم من دار إلى دار تركوا الأولى للثانية» (maqayis).
- 59:7 ٱبْنِ ٱلسَّبِيلِ — س ب ل B002 «ابن السبيل المسافر الذي انقطع به» (tahdhib).
- 59:5 قَطَعْتُم — ق ط ع B006 [fixed expression] «رجل منقطع به إذا كان مسافرا فأبدع به وعطبت راحلته وذهب زاده وماله» (tahdhib); B023 [fixed expression] «قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق» (tahdhib).
- 59:2 وَقَذَفَ — ق ذ ف B003 [fixed expression] «بلدة قذوف أي طروح لبعدها تترامى بالسفر» (maqayis); 59:4 شَآقُّوا — ش ق ق B005 «الشقة أيضا السفر البعيد وشقة شاقة» (sihah); 59:16 ٱلشَّيْطَٰنِ — ش ط ن B001 «شطنت الدار شطونا إذا بعدت» (tahdhib).
- 59:2 فَٱعْتَبِرُوا — ع ب ر B001 «رجل عابر سبيل أي مار» (maqayis;ayn;sihah).
- 59:9 تَبَوَّءُو — ب و ء B001 «المباءة منزل القوم في كل موضع وتبوأت منزلا وبوأت للرجل منزلا» (sihah).
- 59:21 أَنزَلْنَا — ن ز ل B001 «نزل في مكان كذا حط رحله» (mufradat); 59:2/7 أَهْلِ — ء ه ل B005 «مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش» (sihah).
Outside: 2:84–85 (to the Israelites: «وَتُخْرِجُونَ فَرِيقًۭا مِّنكُم مِّن دِيَٰرِهِمْ»); 3:195; 22:40 («ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِم بِغَيْرِ حَقٍّ ... وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ»); 4:100 («وَمَن يَخْرُجْ مِنۢ بَيْتِهِۦ مُهَاجِرًا»); 16:41 («لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةًۭ»); 10:93 («بَوَّأْنَا بَنِىٓ إِسْرَٰٓءِيلَ مُبَوَّأَ صِدْقٍۢ»); 8:72 («ءَاوَوا۟ وَّنَصَرُوٓا۟»).

### 18. The emptied camp and the house that becomes a grave
The abandoned abode taken by wild beasts sits under أبدا (59:11); "as though they had never dwelt there" under الأغنياء (59:7); the hearthstones that outlast the ruin under خالدين (59:17); erased traces under مثل; the refuse of departing travellers under نسوا (59:19); "nobody in the house" joins دار and أحد; the house becomes the grave.
- 59:11 أَبَدًا — ء ب د B003 [fixed expression] «تأبد المنزل أي أقفر وألفته الوحوش» (sihah); «خلا منها أهلها خلفتهم الوحش بها قد تأبدت» (tahdhib).
- 59:7 ٱلْأَغْنِيَآءِ — غ ن ي B004 «غني القوم في دارهم أقاموا ومغانيهم منازلهم» (maqayis); «كأن لم يغن بالأمس أي كأن لم يكن» (ayn).
- 59:17 خَٰلِدَيْنِ — خ ل د B001 «خوالد للأثافي والحجارة لطول مكثها» (ayn;sihah;mufradat).
- 59:15/16/21 مَثَل — م ث ل B006 «الماثل الدارس» (tahdhib); «مثل يمثل إذا زال عن موضعه» (jamhara).
- 59:19 نَسُوا — ن س ي B003 «النسي ما سقط من منازل المرتحلين من رذال أمتعتهم» (maqayis).
- 59:2 دِيَٰرِهِمْ / 59:11 أَحَدًا — د و ر B008 «وما بها ديور وديار أي أحد» (maqayis_dyr); ء ح د B002 «لا أحد في الدار؛ ما في الدار أحد» (sihah).
- 59:2 يُخْرِبُونَ — خ ر ب B002 «الخراب ضد العمارة»; 59:21 خَٰشِعًا — خ ش ع B002 «بلدة خاشعة مغبرة» (maqayis).
- 59:5 تَرَكْتُمُوهَا — ت ر ك B006 «تركة الميت تراثه المتروك» (sihah).
- 59:2 بُيُوتَهُم — ب ي ت B007 [fixed expression] «البيت القبر» (jamhara); 59:20 ٱلْجَنَّةِ — ج ن ن B009 «جننت الميت وأجننته أي واريته والجنن القبر» (sihah); 59:22 ٱلْغَيْبِ — غ ي ب B009 «غيبه غيابه أي دفن في قبره»; 59:2 كَفَرُوا — ك ف ر B012 «الكفر أيضا القرية والكفر أيضا القبر» (sihah); 59:2 لِأَوَّلِ — ء و ل B008 «الآلة الجنازة» (sihah) — the bier.
Outside: 11:68 (Thamud «كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ»); 10:24 (above); 27:52 («فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟»); 28:58 («فَتِلْكَ مَسَٰكِنُهُمْ لَمْ تُسْكَن مِّنۢ بَعْدِهِمْ إِلَّا قَلِيلًۭا»); 22:45 («خَاوِيَةٌ عَلَىٰ عُرُوشِهَا وَبِئْرٍۢ مُّعَطَّلَةٍۢ وَقَصْرٍۢ مَّشِيدٍ»); 33:27 («وَأَوْرَثَكُمْ أَرْضَهُمْ وَدِيَٰرَهُمْ وَأَمْوَٰلَهُمْ»).

### 19. The host's pot and the shared portion
The preference of 59:9 is heard as hosting: guests gathered round a bowl, food made ready for the lodger, welcome, fat melted into the pot, the pot lifted off the fire with a cloth, the morning meal, the taste, the guest preferred, the fire that comforts, a sheep bought and its meat shared. In 59:15 tasting turns to tasting ruin.
- 59:7/14 ٱلْقُرَىٰ — ق ر ي B003 «المقراة الجفنة سميت لاجتماع الضيف عليها أو لما جمع فيها من طعام» (maqayis); «القرى الإحسان إلى الضيف» (ayn).
- 59:21 أَنزَلْنَا — ن ز ل B005 «النزل ما يهيأ للنزيل؛ طعام ذو نزل؛ النزيل الضيف» (maqayis).
- 59:2/7/11 أَهْلِ — ء ه ل B006 «الإهالة الودك والمستأهل الذي يأخذ الإهالة أو يأكلها» (sihah).
- 59:6 قَدِيرٌ — ق د ر B007 «القدير اللحم يطبخ في القدر؛ القدار الجزار ويقال الطباخ» (maqayis); 59:10 تَجْعَلْ — ج ع ل B007 «الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر» (ayn).
- 59:18 لِغَدٍ — غ د و B004 «الغداء ما يؤكل من أول النهار» (ayn); 59:15 ذَاقُوا — ذ و ق B001 «ذقت المأكول أذوقه ذوقا» (maqayis).
- 59:9 يُؤْثِرُونَ — ء ث ر B005 «الأثير الكريم عليك الذي تؤثره بفضلك وصلتك» (maqayis) — joins أثر with فضل of 59:8.
- 59:8 فَضْلًا — ف ض ل B003 «أفضل فلان على فلان أناله من فضله وأحسن إليه» (ayn;tahdhib).
- 59:7 ٱلْمَسَٰكِينِ — س ك ن B004 «السكن النار التي يسكن بها»; 59:16 لِلْإِنسَٰنِ — ء ن س B003 «الأنس خلاف النفور» (mufradat).
- 59:18 خَبِيرٌ — خ ب ر B006 «تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها» (jamhara).
- 59:11/14 قُوتِلْتُمْ — ق ت ل B013 [fixed expression] «هو قاتل الشتوات أي يطعم فيها ويدفىء الناس» (tahdhib).
Outside: 51:24–27 (Abraham's guests: «فَجَآءَ بِعِجْلٍۢ سَمِينٍۢ فَقَرَّبَهُۥٓ إِلَيْهِمْ»); 76:8–9 («وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا»); 90:11–16 («فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ ... أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ يَتِيمًۭا ذَا مَقْرَبَةٍ أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ»); 18:77 (a town's people «فَأَبَوْا۟ أَن يُضَيِّفُوهُمَا», and a wall «يُرِيدُ أَن يَنقَضَّ»).

### 20. Seeing through
"Take heed, you with eyes" (59:2) is crossing over: the dictionary defines اعتبار as passing from what is seen to what is not, and joins جلاء of 59:3 to sight (kohl clears the eye). The river crossed is قطع of 59:5. Supposition (ظن, حسب, خيال) is set against seeing (رأى, نظر); outward look against inner reality (منظر/مخبر); an eye that stands open but sees nothing (قوم); the blind mole.
- 59:2 أُولِى ٱلْأَبْصَٰرِ — ب ص ر B002 «البصر نفاذ في القلب» (ayn;tahdhib).
- 59:2 فَٱعْتَبِرُوا — ع ب ر B004 «الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد» (mufradat); B002 «وهو العابر من ظاهرها إلى باطنها» (mufradat).
- 59:5 قَطَعْتُم — ق ط ع B003 [fixed expression] «قطعت النهر قطوعا عبرته» (sihah) — joins قطع and عبر.
- 59:3 ٱلْجَلَآءَ — ج ل و B002 «الجلا مقصور الإثمد لأنه يجلو البصر» (ayn); «جلوت بصري بالكحل والجلا كحل» (sihah;tahdhib).
- 59:2 ظَنُّوا — ظ ن ن B003 «ظننت الشيء إذا لم تتيقنه» (maqayis); B006 «الظنون البئر لا يدرى أفيها ماء أم لا» (maqayis).
- 59:14 تَحْسَبُهُمْ — ح س ب B002 «الحسبان الظن؛ حسبت كذا في معنى ظننت».
- 59:6 خَيْلٍ — خ ي ل B001 «الخيال كل شيء تراه كالظل وخيالك في المرآة» (ayn); B005 «خلت الشيء خيلا أي ظننته» (sihah).
- 59:11/21 تَرَ / رَأَيْتَهُ — ر ء ي B001 «نظر وإبصار بعين أو بصيرة» (maqayis).
- 59:18 وَلْتَنظُرْ — ن ظ ر B001 «تقليب البصر والبصيرة لإدراك الشيء ورؤيته» (mufradat); B012 [fixed expression] «ينظرون إليك وهم لا يبصرون» (mufradat).
- 59:18 خَبِيرٌ — خ ب ر B001 «المخبر خلاف المنظر» (sihah).
- 59:15/21 مَثَل — م ث ل B011 «يكون المثل بمعنى العبرة» (tahdhib).
- 59:13/14 قَوْمٌ — ق و م B021 «عين قائمة ذهب بصرها والحدقة صحيحة» (ayn).
- 59:16/21 لِلْإِنسَٰنِ / لِلنَّاسِ — ء ن س B005 «إنسان العين المثال الذي يرى في السواد أي سواد العين» (sihah).
Outside: 3:13 (Badr: «يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ... إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّأُو۟لِى ٱلْأَبْصَٰرِ»); 24:44; 22:46; 7:179 («لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا»); 7:198; 63:4 (hypocrites: «وَإِذَا رَأَيْتَهُمْ تُعْجِبُكَ أَجْسَامُهُمْ ... كَأَنَّهُمْ خُشُبٌۭ مُّسَنَّدَةٌۭ»); 35:19 («وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ»); 75:14.

### 21. Tethers and bonds
Hobble, sinew-binding, hobble-rope, tethering ring, well-rope, collar-shackle, jesses, sewn water-skin, snare, bridle, compact: the surah's bonds made and broken. "Severe in punishment" (59:4, 59:7) holds the sinew that binds a spear tight.
- 59:14 يَعْقِلُونَ — ع ق ل B002 «عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط» (maqayis).
- 59:4/7 شَدِيدُ ٱلْعِقَابِ — ع ق ب B001 «عقبت الرمح شددته بالعقب» (mufradat); «العقب العصب الذي تعمل منه الأوتار» (ayn); ش د د B001 «شددت العقد شدا» (maqayis).
- 59:8/9 ٱلْمُهَٰجِرِينَ — ه ج ر B007 «أصل على شد شيء وربطه» (maqayis) — the root of severance also ties.
- 59:10/11 إِخْوَٰن — ء خ و B002 «الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة» (sihah).
- 59:16 ٱلشَّيْطَٰنِ — ش ط ن B002 «شطنته أشطنه إذا شددته بالشطن» (sihah); B003 «شطنه يشطنه شطنا إذا خالفه عن نية وجهه» (sihah).
- 59:10 غِلًّا — غ ل ل B006 «الغل مختص بما يقيد به فيجعل الأعضاء وسطه» (mufradat); 59:14 جَمِيعًا — ج م ع B008 «الجامعة الغل لأنها تجمع اليدين إلى العنق» (sihah).
- 59:2/11 ٱلْكِتَٰبِ — ك ت ب B001 «كتبت السقاء إذا خرزته» (tahdhib).
- 59:1/24 ٱلْحَكِيمُ — ح ك م B006 «حكمة اللجام ما أحاط بحنكيه» (ayn); 59:11 نُطِيعُ — ط و ع B001 «فرس طوع العنان» (ayn;sihah;tahdhib).
- 59:10/16 رَبَّنَا — ر ب ب B011 «الربابة: العهد والميثاق» (sihah).
Outside: 3:103 (above); 3:112 (of the People of the Book: «إِلَّا بِحَبْلٍۢ مِّنَ ٱللَّهِ وَحَبْلٍۢ مِّنَ ٱلنَّاسِ وَبَآءُو بِغَضَبٍۢ»); 5:64 (above).

### 22. Shares: what returns, circulates, is withheld
Property that returns without fighting (فيء) must reach the named recipients and not circulate among the rich; the dictionary's غلول is hiding goods so they never reach the division; إيثار has its reverse in استئثار; rivals grab (تشاح); the surplus of division, allotments, levies, a wage for work that was not done here (59:6).
- 59:6/7 أَفَآءَ — ف ي ء B002 «الفيء ما رد الله على أهل دينه من أموال من خالف أهل دينه بلا قتال» (tahdhib); B001 «أصل الفيء الرجوع» (tahdhib).
- 59:7 دُولَةًۢ — د و ل B001 «الدولة اسم الشيء الذي يتداول» (tahdhib;mufradat); B002 «دال الثوب يدول إذا بلي» (maqayis;sihah) — what circulates wears thin.
- 59:7 ٱلْأَغْنِيَآءِ — غ ن ي B001 «الغنى في المال».
- 59:10 غِلًّا — غ ل ل B004 «الغلول في الغنم وهو أن يخفى الشيء فلا يرد إلى القسم» (maqayis).
- 59:9 يُؤْثِرُونَ — ء ث ر B006 «استأثر فلان بالشيء أي استبد به والاسم الأثرة» (sihah) — the reverse of 59:9.
- 59:9 شُحَّ — ش ح ح B002 [fixed expression] «تشاح الرجلان على الأمر إذا أراد كل واحد منهما الفوز به ومنعه من صاحبه» (maqayis) — joins شح, فوز (59:20) and منع (59:2).
- 59:8 فَضْلًا — ف ض ل B001 «فضول الغنائم ما فضل من القسم» (tahdhib).
- 59:5 قَطَعْتُم — ق ط ع B013 [fixed expression] «أقطع الوالي قطيعة أي طائفة من أرض الخراج» (ayn).
- 59:2 أَخْرَجَ — خ ر ج B003 «الخراج والخرج الإتاوة لأنه مال يخرجه المعطي» (maqayis); 59:21 نَضْرِبُهَا — ض ر ب B010 «الضريبة ما يضرب على الإنسان من جزية وغيرها» (maqayis); 59:17 جَزَٰٓؤُا — ج ز ي B004 «الجزية ما يؤخذ من أهل الذمة» (sihah).
- 59:10 تَجْعَلْ — ج ع ل B005 «الجعل ما جعلت لإنسان أجرا له على عمل يعمله» (ayn); 59:18 تَعْمَلُونَ — ع م ل B004 «العمالة أجر ما عمل» (maqayis) — wage for labour, against fay' gained «فما أوجفتم».
- 59:24 ٱلْخَٰلِقُ — خ ل ق B006 «الخلاق النصيب لأنه قد قدر لكل أحد نصيبه» (maqayis).
Outside: 8:41 (khums: «لِلَّهِ خُمُسَهُۥ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ» — the list of 59:7); 9:60; 3:161 («وَمَا كَانَ لِنَبِىٍّ أَن يَغُلَّ»); 3:140 («وَتِلْكَ ٱلْأَيَّامُ نُدَاوِلُهَا بَيْنَ ٱلنَّاسِ»); 9:75–77 (hypocrites: «فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ ... فَأَعْقَبَهُمْ نِفَاقًۭا ... وَبِمَا كَانُوا۟ يَكْذِبُونَ»); 47:38 («وَمَن يَبْخَلْ فَإِنَّمَا يَبْخَلُ عَن نَّفْسِهِۦ ۚ وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ ۚ وَإِن تَتَوَلَّوْا۟»); 64:16 («وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ»); 3:92 («حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ»).

### 23. The lot-arrows
A full maysir draw sits in the surah's words: the quiver, the fifth and sixth arrows, the stake, the winning arrow that comes out, the losing one that stays in, the steward of the arrows. 59:20 «الفائزون» and 59:12 «الأدبار» are winner and loser.
- 59:10/16 رَبَّنَا / رَبَّ — ر ب ب B010 «الربابة شبيهة بالكنانة تجمع فيها سهام الميسر» (sihah).
- 59:9/18/19 نَفْس — ن ف س B016 «النافس الخامس من قداح الميسر وفيه خمسة فروض» (tahdhib); 59:7 ٱلسَّبِيلِ — س ب ل B009 «المسبل السادس من سهام الميسر» (sihah).
- 59:10 سَبَقُونَا — س ب ق B002 «السبق الخطر يوضع بين أهل السباق» (ayn;sihah).
- 59:20 ٱلْفَآئِزُونَ — ف و ز B001 «إذا خرج قدح قوم في القمار قيل قد فاز» (ayn;tahdhib).
- 59:12 ٱلْأَدْبَٰرَ — د ب ر B019 «الدابر من القداح الذي لم يخرج وهو خلاف الفائز» (maqayis).
- 59:21 نَضْرِبُهَا — ض ر ب B018 «ضريب القداح هو الموكل بها» (maqayis;ayn;sihah;tahdhib).
Outside: 3:185 («فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ» — 59:20's terms).

### 24. The charge made and the charge that falters
59:6 names a mounted push not made; 59:8 «الصادقون» is, in the dictionary, carrying a charge through; 59:11 «لكاذبون» is charging and pulling up — the dictionary joins the two words. Their onslaught goes "among themselves" (59:14). Gait and tack lie in other words: the trot short of the canter, the stretching horse, the bridle, the saddle-pad.
- 59:6 أَوْجَفْتُمْ ... مِنْ خَيْلٍ وَلَا رِكَابٍ — و ج ف B001 «الوجيف دون التقريب من السير» (tahdhib) — joins وجف with the gait-word of قرب (59:7); خ ي ل B002 «الخيل في الأصل اسم للأفراس والفرسان جميعا» (mufradat); ر ك ب B001 «الركاب الإبل التي يسار عليها» (sihah;tahdhib).
- 59:8 ٱلصَّٰدِقُونَ — ص د ق B004 «صدق في القتال إذا وفى حقه» (mufradat).
- 59:11 لَكَٰذِبُونَ — ك ذ ب B004 [fixed expression] «حمل فلان ثم كذب أي لم يصدق في الحملة» (maqayis); «حمل فلان فما كذب أي ما جبن» (sihah).
- 59:14 بَأْسُهُم بَيْنَهُمْ شَدِيدٌ — ش د د B003 «شد على العدو إذا حمل عليه» (jamhara;sihah).
- 59:18 قَدَّمَتْ — ق د م B006 «أقدم على قرنه إقداما وقدما ومقدما إذا تقدم عليه بجرأة وضده الإحجام» (tahdhib).
- 59:1 سَبَّحَ — س ب ح B004 «السابح من الخيل يمد يديه في الجري» (tahdhib); 59:2 وَقَذَفَ — ق ذ ف B005 «فرس متقاذف سريع العدو» (maqayis;sihah).
- 59:12 لَيُوَلُّنَّ — و ل ي B011 «الولية البرذعة» (sihah); 59:23 ٱلْمَلِكُ — م ل ك B008 [fixed expression] «ملك الدابة قوائمها وهاديها» (sihah;tahdhib).
Outside: 3:167 (hypocrites: «لَوْ نَعْلَمُ قِتَالًۭا لَّٱتَّبَعْنَٰكُمْ»); 33:23 («رِجَالٌۭ صَدَقُوا۟ مَا عَٰهَدُوا۟ ٱللَّهَ عَلَيْهِ»); 49:15 («أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ», the closing words of 59:8); 8:60 («وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ»).

### 25. The hive
Bees whose weapon is in their rear (الأدبار, 59:12), their king (الملك, 59:23), comb honey (يشهد 59:11, الشهادة 59:22), the honey-gatherer's leather bag (أخاف 59:16), thick white honey (نضربها 59:21).
- 59:12 ٱلْأَدْبَٰرَ — د ب ر B014 «الدبر النحل والزنابير ونحوهما مما سلاحها في أدبارها» (mufradat).
- 59:23 ٱلْمَلِكُ — م ل ك B008 [fixed expression] «مليك النحل يعسوبها» (sihah).
- 59:11/22 يَشْهَدُ / ٱلشَّهَٰدَةِ — ش ه د B007 «الشَّهْد العسل في شمعها» (maqayis;sihah).
- 59:16 أَخَافُ — خ و ف B006 «الخافة خريطة من أدم يشتار فيها العسل» (sihah).
- 59:21 نَضْرِبُهَا — ض ر ب B015 «الضرب العسل الأبيض الغليظ» (sihah;tahdhib).
Outside: 16:68–69 (bees told «ٱتَّخِذِى مِنَ ٱلْجِبَالِ بُيُوتًۭا ... يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌۭ ... فِيهِ شِفَآءٌۭ لِّلنَّاسِ», ending «لِّقَوْمٍۢ يَتَفَكَّرُونَ» as 59:21 ends).

### 26. Wound and healing
An abscess rises (أخرج), pus gathers (جاءوا, القرى), eats the inside (وراء), festers (يبتغون), relapses (اغفر), pocks the skin (جدر); the spine is broken (فقراء). Then the closing names heal: the bone set and splinted (الجبار, which also relieves need), recovery (البارئ, بريء), soundness (السلام).
- 59:2 أَخْرَجَ — خ ر ج B004 «الخراج ورم وقرح يخرج من ذاته» (ayn).
- 59:10 جَآءُو — ج ي ء (root_000281) B006 «الجائية ما اجتمع في الخراج من المدة والقيح» (tahdhib) — joins جاء and خراج.
- 59:7 ٱلْقُرَىٰ — ق ر ي B002 «المدة تقري في الجرح أي تجتمع» (ayn).
- 59:14 وَرَآءِ — و ر ي B001 «ورى القيح جوفه يريه وريا: أكله» (sihah).
- 59:8 يَبْتَغُونَ — ب غ ي B004 [fixed expression] «بغى الجرح ورم وترامى إلى فساد» (sihah); 59:10 ٱغْفِرْ — غ ف ر B004 «غفر الجرح يغفر غفرا: نكس، وكذلك المريض» (sihah).
- 59:14 جُدُرٍ — ج د ر B005 «الجدري قروح تنفط عن الجلد» (tahdhib).
- 59:8 لِلْفُقَرَآءِ — ف ق ر B001 «أصل الفقير المكسور الفقار» (mufradat); B008 «الفاقرة الداهية تكسر فقار الظهر» (ayn).
- 59:23 ٱلْجَبَّارُ — ج ب ر B001 «جبرت العظم فجبر»; «جبرت فاقة الرجل إذا أغنيته» (ayn;sihah;tahdhib) — joins setting bone with ending poverty (فقراء, أغنياء); B005 «الجبارة الخشبة توضع على الكسر» (ayn).
- 59:16/24 بَرِىٓءٌ / ٱلْبَارِئُ — ب ر ء B003 «البرء السلامة من السقم» (maqayis;ayn).
- 59:23 ٱلسَّلَٰمُ — س ل م B001 «السلامة أن يسلم الإنسان من العاهة والأذى» (maqayis); B010 «السلامى عظام الأصابع والأشاجع والأكارع» (ayn).
Outside: 3:140 («إِن يَمْسَسْكُمْ قَرْحٌۭ ... وَتِلْكَ ٱلْأَيَّامُ نُدَاوِلُهَا بَيْنَ ٱلنَّاسِ» — wound and دولة); 9:14 («وَيَشْفِ صُدُورَ قَوْمٍۢ مُّؤْمِنِينَ»); 16:69 («فِيهِ شِفَآءٌۭ»).

### 27. Blades and spearheads: sharpened, aimed, dulled
The muster (حشر) is a spearhead thinned; fear (رهبة) a fine arrowhead; the spear is aimed (تبوءوا), bound with sinew (عقاب), couched (عقل); arrows short and long; an arrow overshooting (أدبار). Fay' — taken without fighting — is iron that has gone dull; «كل شيء» holds the dull sword.
- 59:2 ٱلْحَشْرِ — ح ش ر B006 «حشرت السنان أي رققته وألطفته» (ayn;tahdhib).
- 59:13 رَهْبَةً — ر ه ب B006 «الرهب النصل الرقيق من نصال السهام» (sihah).
- 59:15 أَمْرِهِمْ — ء م ر B011 «سنان مؤمر أي محدد»; 59:7 ٱلْقُرَىٰ — ق ر ي B012 «القارية من السنان أعلاه وحده» (sihah).
- 59:9 تَبَوَّءُو — ب و ء B007 [fixed expression] «بوأت الرمح نحوه أي سددته نحوه» (sihah); 59:14 يَعْقِلُونَ — ع ق ل B010 «اعتقل رمحه إذا وضعه بين ركابه وساقه» (maqayis;sihah;tahdhib;mufradat).
- 59:6 يُسَلِّطُ — س ل ط B006 «السلطة: السهم الطويل» (sihah); 59:2 يَحْتَسِبُوا — ح س ب B007 «الحسبان سهام صغار».
- 59:12 ٱلْأَدْبَٰرَ — د ب ر B018 «دبر السهم الهدف سقط خلفه» (mufradat).
- 59:3 ٱلْجَلَآءَ — ج ل و B002 «جلا الصيقل السيف واجتلاه» (ayn;tahdhib); 59:9 يُؤْثِرُونَ — ء ث ر B007 «الأثر فرند السيف والمأثور السيف» (sihah).
- 59:6/7 أَفَآءَ — ف ي ء B009 [fixed expression] «يقال للحديدة إذا كلت بعد حدتها قد فاءت» (tahdhib); 59:6 كُلِّ — ك ل ل B001 «الكليل السيف الذي لا حد له» (ayn).
- 59:18 قَدَّمَتْ — ق د م B008 «القدوم التي ينحت بها» (sihah); 59:2 أَيْدِى — ي د ي B013 [fixed expression] «يد الفأس مقبضها» (tahdhib) — adze and its haft.

### 28. Hide, tanning and the stitched water-skin
Flaying, tanning, measuring, cutting, joining seams, sewing the water-skin and its handle: a leather craft through the surah, ending in the Creator who "measures" (خلق as measuring hide before cutting).
- 59:10 غِلًّا — غ ل ل B012 «أغل الجازر في الإهاب إذا سلخ فترك من اللحم ملتزقا بالإهاب» (sihah); 59:20 أَصْحَٰبُ — ص ح ب B006 «جلد مصحب إذا كان عليه شعره وصوفه» (ayn).
- 59:9 أَنفُسِهِمْ — ن ف س B007 «النفس قدر دبغة مما يدبغ به الأديم» (sihah); 59:23 ٱلسَّلَٰمُ — س ل م B008 «سلمت الجلد إذا دبغته بالسلم» (sihah); 59:10 رَبَّنَا — ر ب ب B006 «رببت الأديم بالسمن» (mufradat).
- 59:24 ٱلْخَٰلِقُ — خ ل ق B001 «الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع» (sihah).
- 59:5 قَطَعْتُم — ق ط ع B012 «قطع الثوب؛ قطعت لهم ثياب من نار» (mufradat).
- 59:2 ٱلْأَبْصَٰرِ — ب ص ر B006 «البصر أن يضم أديم إلى أديم» (sihah); 59:2 ٱلْكِتَٰبِ — ك ت ب B001 «ضم أديم إلى أديم بالخياطة» (mufradat); «كتبت السقاء إذا خرزته» (tahdhib).
- 59:2 يُخْرِبُونَ — خ ر ب B001 «الخربة عروة المزادة» (maqayis); 59:18 خَبِيرٌ — خ ب ر B004 «الخبر المزادة العظيمة» (maqayis;sihah;mufradat); 59:7 ٱلْقُرْبَىٰ — ق ر ب B009 «القربة ما يستقى فيه الماء» (sihah).

### 29. The womb, the near birth, the midwife
Later arrivals (59:10) and mercy are heard as birth: the hidden fetus, the womb, birth drawing near, what lies in the bellies, the midwife who receives, the afterbirth, the grandchild.
- 59:10 رَّحِيمٌ — ر ح م B003 «الرحم بيت منبت الولد ووعاؤه في البطن» (ayn).
- 59:20 ٱلْجَنَّةِ — ج ن ن B007 «الجنين الولد في بطن أمه» (maqayis).
- 59:7/15 ٱلْقُرْبَىٰ / قَرِيبًا — ق ر ب B012 «المقرب الحامل التي قربت ولادتها» (mufradat); 59:3 ٱلدُّنْيَا — د ن و B004 [fixed expression] «أدنت الناقة إذا دنا نتاجها» (sihah).
- 59:18 لِغَدٍ — غ د و B005 «الغدوي كل ما كان في بطون الحوامل» (ayn).
- 59:9/15 قَبْلِهِمْ — ق ب ل B007 «القابلة التي تقبل الولد عند الولاد» (maqayis); 59:11 يَشْهَدُ — ش ه د B006 «الشاهد الذي يخرج مع الولد» (sihah).
- 59:14 وَرَآءِ — و ر ي B007 «الوراء ولد الولد» (maqayis;sihah;mufradat).

### 30. Swimming creation
تسبيح, at both ends of the surah, is in the dictionary swimming and swift passage in water and air, stars in their orbit; the sky is the overhead canopy and the rain; the striker in 59:21 is a swimmer; the messenger's root is easy, released motion.
- 59:1/23/24 سَبَّحَ / سُبْحَٰنَ / يُسَبِّحُ — س ب ح B004 «السبح المر السريع في الماء وفي الهواء» (mufradat); «النجوم تسبح في الفلك» (tahdhib).
- 59:1/24 ٱلسَّمَٰوَٰتِ — س م و B004 «السماء كل ما علاك فأظلك؛ السماء المطر» (sihah).
- 59:21 نَضْرِبُهَا — ض ر ب B018 «الضارب السابح» (sihah;tahdhib).
- 59:4/6/7/8 رَسُول — ر س ل B003 «ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا» (mufradat).
- 59:10 غِلًّا — غ ل ل B009 «الغلغلة سرعة السير ورسالة مغلغلة محمولة من بلد إلى بلد» (maqayis).
Outside: 36:40 («وَكُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ»); 79:3 («وَٱلسَّٰبِحَٰتِ سَبْحًۭا»).

## Interactions
- 1 Fortress × 13 Breast: 59:14 places walled villages and scattered hearts in one ayah; عقل is both the fortress (معقل) and what they lack.
- 1 Fortress × 2 Siege × 8 Mountain: the hard shell answers its impact differently — terror makes the Nadir breach their houses (59:2), awe makes the mountain lower and crack (59:21); خشع joins them as «جدار خاشع» and «أرض خاشعة».
- 1 Fortress × 5 Channels: the dictionary's جيأة is the water round the fort; جدر is both wall and the bank that holds water.
- 2 Siege × 4 Torrent: one phrase of 59:2 (أتاهم من حيث لم يحتسبوا) is both night raid and flood from elsewhere; حسبان is both small arrows and hail.
- 3 Hunt × 17 Exit: خرج runs through the jerboa phrase of نفق and the expulsion; the hypocrites promise «لنخرجن معكم» with a root named for an escape tunnel (9:57 stages the hole they would turn to).
- 3 Hunt × 20 Seeing: the blind mole of خالدين against أولي الأبصار.
- 4 Torrent × 5 Channels: the same water either overwhelms (عز, رعب, وبال) or is channelled to the needy (آتى, أخذ, قرى, فقراء); نصر is rain and the channels that bring it (59:8) and the rain the hypocrites never send (59:11–12).
- 4 Torrent × 8 Mountain: نزل and ضرب carry rain into 59:21; 24:43 stages hail-mountains and sight together.
- 5 Channels × 22 Shares: 59:7 is both irrigation and division; 54:28 «ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ» joins them; غل is both thirst and embezzling before division.
- 6 Splitting × 7 Sowing × 8 Mountain: صدع is crack, plant splitting earth and dawn; فلح is splitting soil and success; 2:74 and 80:25–27 stage split stone, water and grain.
- 6 Splitting × 14 Gathering: «انصدعت الجماعة وتفرقت» (شقق B004) and «جماع ... من قبائل شتى» (جمع B002) put both chains in dictionary phrases.
- 7 Sowing × 9 Palm: لينة (59:5) and «أرض أريضة لينة»; كافر as sower and as palm-sheath; 48:29 and 57:20 stage كفار as tillers.
- 9 Palm × 18 Emptied camp: «كم تركوا من جنات» (ترك B002) and 69:7 (hollow palm stumps) join abandoned groves and abandoned homes.
- 9 Palm × 16 Hand: the tall palm «فات اليد» is الجبار; 18:42 the owner wringing his hands over a ruined palm garden.
- 10 Night × 11 Armour: كفر, غفر, جنة, ورى are covering in both — night's cover and armour's; «وكل ما وقاك فهو جنتك».
- 11 Armour × 1 Fortress: «درع حصينة»; 21:80 «لِتُحْصِنَكُم مِّنۢ بَأْسِكُمْ».
- 12 Firestick × 4 Torrent × 24 Charge: the hypocrites' promised aid is rain that does not fall and a firestick that does not spark («لوريت عن مولاك أي نصرته»); horses' hooves strike useless sparks (نار الحباحب).
- 13 Breast × 5 Channels: صدر is leaving the water, رهبة is driving camels off the trough, حب is drinking full, غل is thirst — the chests of 59:9–13 are also a watering scene.
- 15 Front/back × 16 Hand: «هذا ما قدمت يداك» joins 59:2 and 59:18; 78:40 «يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ» stages نظر, قدم and يد.
- 15 Front/back × 23 Lot: الدابر is the losing arrow, الفائز the winner; 59:12 and 59:20.
- 15 Front/back × 3 Hunt: 8:48 Satan turning on his heels and disavowing; برأة is the hunter's hide.
- 17 Exit × 19 Host: the welcome «مرحبا وأهلا» and the prepared منزل/نزل receive the migrants; 51:24–27 stages arrival and the meal.
- 18 Emptied camp × 22 Shares: غني is both wealth and long dwelling; the wealthy of 59:7 carry «كأن لم يغن بالأمس».
- 19 Host × 5 Channels: قرى is both the guest-bowl and the water basin («المقراة» both).
- 20 Seeing × 17 Exit: عبر and قطع are both crossing a river; اعتبار is crossing from seen to unseen.
- 21 Tethers × 14 Gathering: the آخية of إخوان and the «حبل الله جميعا» of 3:103; جمع as the shackle «الجامعة الغل».
- 22 Shares × 26 Wound: الجبار «جبرت فاقة الرجل إذا أغنيته» joins setting a broken spine (فقير) with ending need; 3:140 joins wound and دولة.
- 25 Hive × 8 Mountain: 16:68 bees take houses in mountains; ضرب is thick honey and rain.
- 27 Blades × 22 Shares: fay' as dulled iron («فاءت») — gain without fighting.
- 30 Swimming × 24 Charge: «السابح من الخيل» joins the opening تسبيح to the horses of 59:6.

## Ayat
- 59:1 — 30 Swimming: سبح, السماوات add swimming and canopy; scene: all creation swims in its course. 1 Fortress: العزيز الحكيم = impregnable, withholding; scene: walls that "withhold" fail before the Withholder. 4 Torrent: العزيز = overpowering flood; scene: a flood from elsewhere and rain that never falls. 7 Sowing: الأرض = soft good soil; scene: covered seed, split soil, sprout. 2 Siege: الأرض = termite; scene: a night siege whose breach is made from inside. 24 Charge: سبح = stretching horse; scene: the charge made and the charge that falters.
- 59:2 — 1 Fortress (حصون, مانعة, لأول, ديار); 2 Siege (أتاهم, بيوت = night raid, لم يحتسبوا = missiles, قذف = catapult, يخربون = holes, أيديهم); 3 Hunt (الحشر = burrow-creatures, أتى/خرج of the jerboa); 4 Torrent (أتاهم = flood from elsewhere, الرعب = valley-filling torrent, الحشر = hard year); 13 Breast (قذف في قلوبهم الرعب); 14 Gathering (الحشر, الكتاب); 16 Hand (بأيديهم); 17 Exit (أخرج, ديارهم, الحشر); 18 Emptied camp (ديار, يخربون, بيوت = grave); 20 Seeing (أولي الأبصار, اعتبروا, ظنوا); 11 Armour (حصون, أبصار = shields); 10 Night (كفروا = night cover); 7 Sowing (كفروا = sowers); 9 Palm (قلوب = heart of palm, كفروا = sheath); 26 Wound (أخرج = abscess); 27 Blades (الحشر = sharpened spearhead); 28 Hide (الكتاب, الأبصار, يخربون); 22 Shares (أخرج = levy). Scenes as given under each chain heading: walled refuge that withholds; night siege breached from within; the jerboa bursting its hidden door; the flood from elsewhere; terror thrown into chests; a people driven together and scattered; own hands sending ahead; exile on far roads to a prepared lodging; the camp left to wild beasts; crossing from seen to unseen.
- 59:3 — 17 Exit (الجلاء = brought out to open ground); 20 Seeing (الجلاء = kohl clearing the eye); 10 Night (الجلاء = clear day; النار); 5 Channels (عذاب = sweet water turned punishment); 15 Front/back (الآخرة = the last, behind); 9 Palm (الآخرة: the palm whose fruit stays latest); 3 Hunt (الجلاء = falcon lifting its gaze); 27 Blades (polished sword); 29 Womb (الدنيا = birth drawing near). Scene lines: exile to a new lodging; seeing through; night giving way to clear day; water that heals or punishes; the heel where consequence follows.
- 59:4 — 6 Splitting (شاقوا = split like rock; the community parted); 15 Front/back (العقاب = heel, what comes last); 21 Tethers (شديد العقاب = sinew bound tight); 17 Exit (شقة = far journey); 30 Swimming (رسول = released motion). Scene: hard things crack — the hostile, their hearts, the soil, the mountain.
- 59:5 — 9 Palm (لينة, قطعتم by permission, تركتموها, قائمة على أصولها, الفاسقين = ripe date leaving skin); 3 Hunt (الفاسقين = mouse leaving its hole); 7 Sowing (لينة = soft soil); 8 Mountain (لينة = softening of hearts); 6 Splitting (قطع رحمه); 17 Exit (قطع = stranded traveller, highwaymen); 20 Seeing (قطعت النهر = crossing); 11 Armour (تركة = iron helmet); 18 Emptied camp (تركة = what the dead leave); 22 Shares (قطيعة = allotment); 28 Hide (cutting); 14 Gathering (قطعناهم أمما). Scene: a grove cut or left on its roots that becomes the Garden.
- 59:6 — 22 Shares (أفاء = return without fighting); 24 Charge (أوجفتم, خيل, ركاب = the push not made); 4 Torrent (خيل = cloud that only seems to rain); 20 Seeing (خيل = shadow-image); 12 Firestick (خيل's sparks, يسلط = lamp oil, كل = lightning); 13 Breast (أوجفتم = throbbing heart); 9 Palm (ركاب = rootless offshoot, شيء = young palms); 16 Hand (يسلط = hand as authority); 19 Host (قدير = meat in the pot); 27 Blades (أفاء = dulled iron, كل = dull sword); 5 Channels (يسلط = burning thirst); 14 Gathering (أفاء = band that rallies). Scene: what returns is distributed like channelled water, not like a wage for a charge.
- 59:7 — 5 Channels (آتاكم = channel, فخذوه = basin, فانتهوا = pool where water rests, القرى = gathered water); 22 Shares (أفاء, دولة, الأغنياء, the recipients); 16 Hand (دولة hand to hand, خذوه, آتاكم); 18 Emptied camp (الأغنياء = "as though they never dwelt"); 19 Host (القرى = guest bowl, المساكين = comforting fire); 17 Exit (ابن السبيل = stranded traveller; أهل welcome); 9 Palm (آتاكم = palm's yield, القرى = palm base); 23 Lot (السبيل = sixth arrow); 13 Breast (المساكين = stillness); 26 Wound (القرى = pus gathering); 27 Blades (القرى = spear point); 29 Womb (القربى = near birth); 28 Hide (القربى = water-skin); 24 Charge (القربى = gait). Scene: water led by channels into basins for the needy, not pooled among the rich.
- 59:8 — 5 Channels (الفقراء = channel mouth/dug pit, المهاجرين = great basin, ينصرون = channels from afar); 17 Exit (أخرجوا, المهاجرين); 24 Charge (الصادقون = charge carried through); 19 Host (فضلا = giving from one's surplus); 22 Shares (فضل = surplus of division); 3 Hunt (الفقراء = prey's back exposed); 26 Wound (الفقراء = broken spine; يبتغون = festering); 21 Tethers (هجر = hobble-rope); 9 Palm (مهجرة = very tall palm). Scene lines as under the chains.
- 59:9 — 5 Channels (يحبون = drink till full, قبلهم = drawing water for camels, صدورهم = turning from the water, أنفسهم = water as life); 13 Breast (no حاجة/doubt in chests; حبة القلب); 1 Fortress (خصاصة = gapped reed hut; شح = withholding; يوق); 19 Host (يؤثرون, تبوءوا = lodging made ready); 22 Shares (إيثار vs استئثار; تشاح); 12 Firestick (شح = firestick that won't spark; يحبون = useless sparks); 6 Splitting & 7 Sowing (المفلحون = splitting soil); 11 Armour (يوق = protective cover); 15 Front/back (يؤثرون = following in the track); 4 Torrent (أرض شحاح); 10 Night (أنفس = dawn breathing); 17 Exit (تبوءوا); 23 Lot (نفس = fifth arrow); 27 Blades (تبوءوا = spear aimed; أثر = sword-pattern); 28 Hide (نفس = tanning dose).
- 59:10 — 14 Gathering (جاءوا + اغفر = the whole community coming); 13 Breast (غل driven into hearts); 15 Front/back (بعدهم = at the heel, سبقونا); 11 Armour (اغفر = mail coif, غل = undershirt beneath mail); 21 Tethers (إخوان = tether ring, غل = shackle, ربنا = compact); 22 Shares (غل = embezzling before division); 5 Channels (غل = thirst; جاءوا = water pit); 9 Palm (غل = water at the palm roots; تجعل = short palms); 2 Siege (جاءوا = moat); 26 Wound (جاءوا = pus, اغفر = relapse); 29 Womb (رحيم = womb); 23 Lot (ربنا = quiver, سبقونا = stake); 3 Hunt (سبقونا = falcon's jesses); 19 Host (تجعل = pot-cloth); 28 Hide (غل, ربنا); 30 Swimming (غلغلة).
- 59:11 — 3 Hunt (نافقوا = jerboa's hidden exit; لنخرجن); 4 Torrent (لننصرنكم = promised rain; كاذبون = flow that fails); 24 Charge (كاذبون = charge that pulls up); 12 Firestick (نصر = spark of aid); 21 Tethers (إخوان tether, نطيع = led by the rein); 18 Emptied camp (أبدا = abode taken by beasts; أحدا = nobody in the house); 10 Night (نافقوا = hiding the opposite); 15 Front/back (كاذبون = beast that stops to look behind); 9 Palm (نطيع = palm ready to pick); 25 Hive (يشهد = comb honey); 20 Seeing (ألم تر); 26 Wound (نفق الجرح).
- 59:12 — 15 Front/back (يولن الأدبار); 24 Charge; 4 Torrent (no rain-aid); 23 Lot (الأدبار = losing arrow); 25 Hive (الأدبار = bees, weapon in the rear); 7 Sowing (الدبار = field plots); 27 Blades (arrow falling behind the target); 3 Hunt (fleeing). Scene: backs turned, heels not turning back, consequence following.
- 59:13 — 13 Breast (رهبة in صدور = breastbone, fear and agitation); 5 Channels (رهبة = driving camels off the trough); 27 Blades (رهب = fine arrowhead); 20 Seeing (يفقهون; قوم = open eye that sees nothing). Scene lines as under the chains.
- 59:14 — 1 Fortress (قرى محصنة, جدر, لا يعقلون = no معقل); 14 Gathering (جميعا vs شتى); 6 Splitting (شتى, بينهم); 13 Breast (قلوبهم شتى); 24 Charge (بأس شديد among themselves); 12 Firestick (وراء = firestick that gives fire = aid); 10 Night (وراء = concealment); 15 Front/back (وراء); 20 Seeing (تحسبهم); 5 Channels (جدر = banks holding water); 7 Sowing (جدر = sprouting); 21 Tethers (يعقلون = hobble; جميعا = shackle); 11 Armour (بأس); 26 Wound (وراء = pus eating inside; جدر = pox); 27 Blades (يعقلون = couched spear); 29 Womb (وراء = grandchild).
- 59:15 — 4 Torrent (وبال = heavy downpour); 5 Channels (ذاقوا وبال = unwholesome water; عذاب); 18 Emptied camp (مثل = erased trace); 20 Seeing (مثل = lesson); 19 Host (ذاقوا = tasting turned to ruin); 15 Front/back (قبلهم); 29 Womb (قريبا); 27 Blades (أمر = sharpened point); 26 Wound (أليم).
- 59:16 — 15 Front/back (Satan's disavowal, staged in 8:48 as turning on his heels); 3 Hunt (بريء = hunter's hide); 5 Channels (الشيطان = long well-rope, deep well); 21 Tethers (شطن = rope, turning one from his aim); 17 Exit (شطن = far away); 25 Hive (أخاف = honey bag); 6 Splitting (العالمين = cleft lip); 19 Host (الإنسان = intimacy vs aversion); 20 Seeing (الإنسان = pupil); 26 Wound (بريء = recovery); 23 Lot (رب = quiver).
- 59:17 — 15 Front/back (عاقبتهما = what follows at the heel); 18 Emptied camp (خالدين = hearthstones outlasting the ruin); 3 Hunt (خالدين = blind mole); 1 Fortress (الظالمين = withholders of rights); 10 Night (الظالمين = darkness; النار); 5 Channels (ظلم = water overrunning its bed); 12 Firestick (النار as dwelling); 22 Shares (جزاء = levy); 13 Breast (خلد = what settles in the heart).
- 59:18 — 15 Front/back (قدمت, غد, نظر = looking to the outcome); 16 Hand (what the hands sent ahead; تعملون = hand-labour); 20 Seeing (لتنظر; خبير = inner reality vs outward look); 7 Sowing (خبير = sharecropper, نظر = earth showing growth); 11 Armour (اتقوا); 10 Night (غد = early morning); 19 Host (غد = morning meal; خبير = shared slaughter); 5 Channels (خبير = low ground where rain collects); 22 Shares (عمل = wage); 24 Charge (قدم = bold advance); 27 Blades (قدوم = adze); 28 Hide (خبير = great water-skin); 29 Womb (غد = what is in the bellies); 23 Lot (نفس).
- 59:19 — 18 Emptied camp (نسوا = refuse left by departing travellers); 3 Hunt and 9 Palm (الفاسقون = mouse out of its hole, date out of its skin); 16 Hand (9:67 joins closed hands and forgetting); 23 Lot (أنفس). Scene lines as under the chains.
- 59:20 — 9 Palm (الجنة = palm grove); 11 Armour (الجنة = shield); 10 Night (جنة = night's cover); 5 Channels (الفائزون = the waterless desert named for rescue); 23 Lot (الفائزون = winning arrow); 22 Shares (تشاح … الفوز); 13 Breast (جنان = heart); 18 Emptied camp (جنن = grave); 12 Firestick (النار); 29 Womb (جنين); 28 Hide (أصحاب = hide with hair left on); 21 Tethers (أصحب = led after resisting).
- 59:21 — 8 Mountain (أنزلنا = rain, جبل = hard dry mass, خاشع = barren land lying low, متصدع = earth cracked by the plant, خشية = awe and dryness, نضرب = rain on earth, الأمثال = lesson, يتفكرون); 6 Splitting; 7 Sowing; 10 Night (متصدع = dawn, خاشع = sinking stars); 2 Siege and 18 Emptied camp (جدار خاشع; بلدة خاشعة); 4 Torrent (نازلة, ضريب = frost); 14 Gathering (القرآن = gathering; جبل = great crowd); 9 Palm (خشية = shrivelled dates); 19 Host (أنزلنا = food for the guest); 17 Exit (نزل = setting down one's load); 20 Seeing (رأيته; أمثال); 25 Hive (نضرب = thick honey); 23 Lot (ضريب القداح); 22 Shares (ضريبة); 30 Swimming (الضارب السابح).
- 59:22 — 10 Night (الغيب = hidden, sun setting; الشهادة = witnessed presence); 18 Emptied camp (غيب = burial); 3 Hunt (غيابة = hiding hollow); 25 Hive (الشهادة = comb honey); 24 Charge (الشاهد = the running that proves the horse); 6 Splitting (عالم = cleft lip); 3 Hunt (عالم = falcon). Scene lines as under the chains.
- 59:23 — 1 Fortress (الملك = cohesion of a wall, المهيمن = safety from fear, العزيز, المؤمن); 5 Channels (الملك = water as life, القدوس = basin stone, السلام = bucket); 26 Wound (الجبار = bone set and splinted and need relieved; السلام = soundness, finger bones); 9 Palm (الجبار = palm beyond reach); 16 Hand (فات اليد); 13 Breast (القلب ملاك الجسد); 25 Hive (مليك النحل); 24 Charge (ملك الدابة); 3 Hunt and 21 Tethers (يشركون = snare); 30 Swimming (سبحان); 28 Hide (السلام = tanning tree).
- 59:24 — 30 Swimming (يسبح, السماوات); 9 Palm (المصور = palm cluster); 28 Hide (الخالق = measuring hide before cutting); 5 Channels (الخالق = rock hollow holding rainwater); 22 Shares (خلاق = portion); 26 Wound (البارئ = recovery); 3 Hunt (البارئ = hunter's hide; السماوات = hunters); 1 Fortress (العزيز الحكيم); 7 Sowing (الأرض).

