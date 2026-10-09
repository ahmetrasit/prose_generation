Focus: 59:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
  a speaker.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/59_2/D.r13/context.md =====
# 59:2 — focus

هُوَ ٱلَّذِىٓ أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ ۚ مَا ظَنَنتُمْ أَن يَخْرُجُوا۟ ۖ وَظَنُّوٓا۟ أَنَّهُم مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟ ۖ وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ ۚ يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ وَأَيْدِى ٱلْمُؤْمِنِينَ فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | هُوَ |  |  | PRON |
| 2 | ٱلَّذِىٓ | ٱلَّذِى |  | REL |
| 3 | أَخْرَجَ | أَخْرَجَ | خ ر ج | V |
| 4 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 5 | كَفَرُوا۟ | كَفَرَ | ك ف ر | V;PRON |
| 6 | مِنْ | مِن |  | P |
| 7 | أَهْلِ | أَهْل | ء ه ل | N |
| 8 | ٱلْكِتَٰبِ | كِتَٰب | ك ت ب | DET;N |
| 9 | مِن | مِن |  | P |
| 10 | دِيَٰرِهِمْ | دَار | د و ر | N;PRON |
| 11 | لِأَوَّلِ | أَوَّل | ء و ل | P;N |
| 12 | ٱلْحَشْرِ | حَشْر | ح ش ر | DET;N |
| 13 | مَا | مَا |  | NEG |
| 14 | ظَنَنتُمْ | ظَنَّ | ظ ن ن | V;PRON |
| 15 | أَن | أَن |  | SUB |
| 16 | يَخْرُجُوا۟ | خَرَجَ | خ ر ج | V;PRON |
| 17 | وَظَنُّوٓا۟ | ظَنَّ | ظ ن ن | CONJ;V;PRON |
| 18 | أَنَّهُم | أَنّ |  | ACC;PRON |
| 19 | مَّانِعَتُهُمْ | مَّانِعَت | م ن ع | N;PRON |
| 20 | حُصُونُهُم | حُصُون | ح ص ن | N;PRON |
| 21 | مِّنَ | مِن |  | P |
| 22 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 23 | فَأَتَىٰهُمُ | أَتَى | ء ت ي | REM;V;PRON |
| 24 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 25 | مِنْ | مِن |  | P |
| 26 | حَيْثُ | حَيْث | ح ي ث | N |
| 27 | لَمْ | لَم |  | NEG |
| 28 | يَحْتَسِبُوا۟ | يَحْتَسِبُ | ح س ب | V;PRON |
| 29 | وَقَذَفَ | قَذَفَ | ق ذ ف | CONJ;V |
| 30 | فِى | فِى |  | P |
| 31 | قُلُوبِهِمُ | قَلْب | ق ل ب | N;PRON |
| 32 | ٱلرُّعْبَ | رُعْب | ر ع ب | DET;N |
| 33 | يُخْرِبُونَ | يُخْرِبُ | خ ر ب | V;PRON |
| 34 | بُيُوتَهُم | بَيْت | ب ي ت | N;PRON |
| 35 | بِأَيْدِيهِمْ | يَد | ي د ي | P;N;PRON |
| 36 | وَأَيْدِى | يَد | ي د ي | CONJ;N |
| 37 | ٱلْمُؤْمِنِينَ | مُؤْمِن | ء م ن | DET;N |
| 38 | فَٱعْتَبِرُوا۟ | ٱعْتَبِرُ | ع ب ر | REM;V;PRON |
| 39 | يَٰٓأُو۟لِى | أُولِى | ء و ل | VOC;N |
| 40 | ٱلْأَبْصَٰرِ | بَصَر | ب ص ر | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 59 — full text (context; no pericope)

- 59:1 سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 59:2 ◀ focus هُوَ ٱلَّذِىٓ أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ ۚ مَا ظَنَنتُمْ أَن يَخْرُجُوا۟ ۖ وَظَنُّوٓا۟ أَنَّهُم مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟ ۖ وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ ۚ يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ وَأَيْدِى ٱلْمُؤْمِنِينَ فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ
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


===== _commentary/v16/work/59_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## خ ر ج (root_000400) — identity root of أَخْرَجَ (w3)

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

## ك ف ر (root_001307) — identity root of كَفَرُوا۟ (w5)

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

## ء ه ل (root_000064) — identity root of أَهْلِ (w7)

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

## ك ت ب (root_001283) — identity root of ٱلْكِتَٰبِ (w8)

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

## د و ر (root_000499) — identity root of دِيَٰرِهِمْ (w10)

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

## ء و ل (root_000067) — identity root of لِأَوَّلِ (w11)

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

## ح ش ر (root_000324) — identity root of ٱلْحَشْرِ (w12)

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

## ظ ن ن (root_000969) — identity root of ظَنَنتُمْ (w14)

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

## م ن ع (root_001448) — identity root of مَّانِعَتُهُمْ (w19)

- **B001** vermeme ve esirgeme — vermenin karşıtı olarak vermeme ve esirgeme · vermeyen veya verilecek şeyi elinde tutan · iyiliği sürekli esirgeyen çok cimri kişi · başkasına vermeyen, cimrice elinde tutan kişi · yalnızca vermemeyi hak edenden esirgeyen ve adaletle veren
  خلاف الإعطاء (maqayis;sihah)؛ ضد العطية (mufradat)؛ رجل منوع ومناع إذا كان بخيلا ممسكا (tahdhib)؛ مناع للخير (tahdhib;mufradat)
- **B002** isteğinden alıkoyma — onu istediği şeyden alıkoymak · seni bunu yapmaktan ne alıkoydu? · önüne engel çıkınca geri durmak
  منعته أمنعه منعا فامتنع أي حلت بينه وبين إرادته (ayn)؛ منعت الرجل عن الشئ فامتنع منه (sihah)؛ المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)؛ ما الذي صدك وحملك على ترك ذلك (mufradat)
- **B003** erişilmez kılan koruyucu güç — inananları çevreleyip koruyan ve destekleyen · gücü ve koruması sayesinde erişilemez · koruyucu güç, saygınlık ve destekçiler · saygınlık ve güçlü koruma içinde
  مكان منيع وهو في عز ومنعة (maqayis)؛ رجل منيع لا يخلص إليه وهو في عز ومنعة (ayn)؛ مكان منيع وقد منع مناعة؛ المنعة جمع مانع أي من يمنعه من عشيرته (sihah)؛ يحوطهم وينصرهم؛ في قوم يمنعونه ويحمونه (tahdhib)؛ يقال في الحماية ومنه مكان منيع وفلان ذو منعة (mufradat)
- **B004** cinsel ahlaksızlığa yanaşmayan kadın [kalıp] — cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın · ahlak dışı cinsel ilişkiyi kabul etmeyen kadın
  امرأة منيعة متمنعة لا تؤاتى على فاحشة (ayn)؛ امرأة منعة متمنعة لا تؤاتى على فاحشة (tahdhib)؛ امرأة منيعة كناية عن العفيفة (mufradat)
- **B005** Engelle! — Engelle!
  مناع بمعنى امنع (ayn)؛ مناع أي امنع كقولهم نزال أي انزل (mufradat)
- **B006** bir şey üzerinde karşılıklı engelleşme — bir şey üzerinde onunla karşılıklı engelleşmek
  مانعته الشئ ممانعة (sihah)
- **B007** çetin yıla direnen genç dişi deve ile dişi oğlak — gençlikleriyle çetin yıla direnen ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak · çetin yıla karşı koyan ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak
  المتمنعان البكرة والعناق تمتنعان على السنة بفتائهما (sihah)؛ المتمنعتان البكرة والعناق تمنعان على السنة لفنائهما (tahdhib)؛ المقاتلتان للزمان عن أنفسهما (sihah;tahdhib)

## ح ص ن (root_000331) — identity root of حُصُونُهُم (w20)

- **B001** korunaklı çevre, onu kurma, ona sığınma ve genel olarak sakınma — korunaklı yer; savunmalı yapılar · içine erişilemeyen, iyi korunan · yerin ya da köyün çevresi yapıyla korunur hale geldi · onu korunaklı hale getirdi ve korumaya aldı · korunak edindi, sığındı ve kendini korudu · sağlamlaştırılarak savunmalı yapıya dönüştürülmüş köyler · bedeni koruyan sık dokunmuş zırh · korunaklı yerlerde saklayıp koruduğunuz şeyler
  الحفظ والحياطة والحرز (maqayis); الحصن كل موضع حصين لا يوصل إلى ما في جوفه (ayn); حصنت القرية إذا بنيت حولها وتحصن العدو (sihah); يتجوز به في كل تحرز ومنه درع حصينة ومما تحصنون أي تحرزون (mufradat)
- **B002** yasak cinsel ilişkiden uzak durarak kendini koruma — cinsel davranışta kendini koruyan kadın · yasak cinsel ilişkiden uzak duran kadın · cinsel organını yasak ilişkiden koruyan kadın · kadın yasak cinsel ilişkiden uzak durdu · cinsel organını yasak ilişkiden korudu · kendisini ya da cinsel organını koruyarak yasak ilişkiden uzak duran kadın
  الحصان المرأة المتعففة الحاصنة فرجها (maqayis); امرأة حاصن بينة الحصن والحصانة أي العفافة عن الربية (ayn); أحصنت المرأة عفت وحصنت المرأة أي عفت (sihah); يقال حصان للعفيفة وأحصنت فرجها (mufradat)
- **B003** evlilik veya hukuki engelle kazanılan korunmuş durum — adam evlendi ve evli sayıldı · kocası onu evlilik bağıyla evli konuma getirdi · evlenmiş kadın · evlendirildiklerinde ya da evlendiklerinde · evli oldukları için kendileriyle evlenilmesi yasak kadınlar · saygınlığı, özgürlüğü veya hukuki engel nedeniyle korunan kadın
  كل امرأة متزوجة فهي محصنة وأحصن الرجل فهو محصن (maqayis); امرأة محصنة أحصنها زوجها (ayn); أحصن الرجل إذا تزوج وأحصنها زوجها وقرئ فإذا أحصن أي زوجن (sihah); أحصن أي تزوجن والمحصنات المزوجات أو بمانع من شرفها وحريتها (mufradat)
- **B004** aygır veya erkek at — aygır; erkek at · biniciyi koruyan atlar
  الحصان الفرس الفحل (ayn); سموا كل ذكر من الخيل حصانا (sihah); فرس حصان لكونه حصنا لراكبه (mufradat)

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w22)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ء ت ي (root_000009) — identity root of فَأَتَىٰهُمُ (w23)

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

## ح ي ث (root_000375) — identity root of حَيْثُ (w26)

- **B001** ardından gelen yan tümceyle belirlenen yer — ardından gelen yan tümceyle belirlenen yer · her nerede; nerede olursa · belirtilen yerden · aynı yer anlamındaki lehçe varyantı
  كلمة موضوعة لكل مكان وهي مبهمة (maqayis)؛ كلمة معروفة يستدل بها على المكان مبنية على الضم (jamhara)؛ كلمة تدل على المكان لأنه ظرف في الأمكنة بمنزلة حين في الأزمنة (sihah)؛ حيث ظرف من المكان أي الموضع الذي كنت فيه وإلى أي موضع شئت (tahdhib)؛ عبارة عن مكان مبهم يشرح بالجملة التي بعده (mufradat)

## ح س ب (root_000318) — identity root of يَحْتَسِبُوا۟ (w28)

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

## ق ذ ف (root_001209) — identity root of وَقَذَفَ (w29)

- **B001** fırlatıp atma — bir şeyi fırlatıp atmak · bir şeyi başka bir şeyin içine atmak · ok, çakıl, taş veya başka bir şeyi fırlatıp atma · fırlatılan nesne · ağır cisimleri uzağa fırlatan savaş düzeneği · avucu dolduracak kadar elde tutulup atılan şey · bir şeyi uzağa göndermek için kullanılan fırlatma aracı · karşılıklı sövüşme ve taş atışma
  أصل يدل على الرمي والطرح (maqayis)؛ قذف الشيء إذا رمى به (maqayis)؛ القذف الرمي بالسهم والحصى (ayn;tahdhib)؛ القذف بالحجارة الرمي بها (sihah)؛ القذف بالحجر والحذف بالعصا (tahdhib)؛ القذف الرمي البعيد (mufradat)؛ القذيفة الشيء يرمى به (maqayis;sihah)؛ القذاف المنجنيق (ayn;tahdhib)؛ القذاف ما قبضت بيدك مما يملأ الكف فرميت به (tahdhib)؛ القذافة والقذف جمع وهو الذي يرمى به الشيء فيبعد (tahdhib)
- **B002** sözle karalama ve suçlama — sözle saldırma, sövme ve ayıplama · iffetli bir kadına sözle ağır suç isnat etmek · karşılıklı sövüşme ve taş atışma
  القذف الرمي بالسهم والحصى والكلام (ayn;tahdhib)؛ قذف المحصنة أي رماها (sihah)؛ بينهم قذيفى أي سباب ورمي بالحجارة أيضا (tahdhib)؛ استعير القذف للشتم والعيب (mufradat)
- **B003** yolculukla aşılacak kadar uzak [kalıp] — yolculuğu uzatacak kadar uzak kasaba · uzak konak yeri · uzak ve geniş ıssız arazi · uzak çöl arazisi
  بلدة قذوف أي طروح لبعدها تترامى بالسفر (maqayis)؛ منزل قذف وقذيف أي بعيد (maqayis;sihah;mufradat)؛ سبسب قذف وقذوف وقذف أي بعيد (ayn;tahdhib)؛ فلاة قذف وقذف بعيدة (sihah)؛ الدار التي تنوى بعيدة كذلك (tahdhib)؛ بلدة قذوف بعيدة (mufradat)
- **B004** yan, kenar veya yüksekçe çıkıntı — dağın yanları · bir şeyin yanı veya kenarı · dağın yüksekçe öne çıkan başı veya sırtı · vadi ile ırmağın iki yanı
  أقذاف الجبل نواحيه الواحد قذف (maqayis)؛ القذف الناحية والقذفات النواحي من كل شيء (ayn)؛ القذفة ما أشرف من رؤوس الجبال (ayn;sihah)؛ قذف وهي الشرف الواحدة قذفة (sihah;tahdhib)؛ قذفا الوادي والنهر جانباه (tahdhib)
- **B005** hızlı ilerleme — yol almadaki hız · hızlı koşan · hızla ilerleyip sürünün önüne geçen deve
  القذاف سرعة السير (maqayis;ayn;sihah)؛ فرس متقاذف سريع العدو (maqayis;sihah)؛ ناقة متقاذفة سريعة الركض (ayn)؛ ناقة قذاف وقذوف وقذف وهي التي تتقدم من سرعتها وترمي بنفسها أمام الإبل في سيرها (tahdhib)
- **B006** etle dolgun ve iri olma [kalıp] — üzerine et yığılmış gibi dolgun deve · çok etli ve iri erkek
  ناقة مقذوفة باللحم كأنها رميت به (maqayis;ayn)؛ رجل مقذف أي كثير اللحم كأنه قذف باللحم قذفا (sihah)؛ قذفت الناقة باللحم قذفا ولدست به لدسا كأنها رميت به رميا فاكتنزت منه (tahdhib)؛ المقذف الذي قد رمي باللحم رميا فصار أغلب (tahdhib)
- **B007** midesindekini dışarı atarcasına kusma [kalıp] — midesindekini dışarı atar gibi kusmak
  قذف قاء كأنه رمى به (maqayis)؛ قذف الرجل أي قاء (sihah)

## ق ل ب (root_001248) — identity root of قُلُوبِهِمُ (w31)

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

## ر ع ب (root_000572) — identity root of ٱلرُّعْبَ (w32)

- **B001** korku ve korkutma — korku ve ürküntü · korkmak, ürkmek · birini korkutmak · korkutulmuş veya ürkmüş · korkmuş · ürkmüş · korkutmaya yönelik sözlü uygulama veya tehdit · korkutan kişi veya korkutucu söz söyleyen kişi · korkutucu sözleri söyleyen kişi · çok korkak kimse · güçsüz ve korkak kimse · ürkütücü ıssız arazi · korkutma eylemi
  الرعب الخوف (maqayis;ayn;jamhara;sihah;tahdhib)؛ رعبته أي أفزعته (maqayis;ayn;sihah)؛ رعبت فلانا رعبا فهو مرعوب مرتعب أي فزع (tahdhib)؛ الرعب رقية يرعبون ذا السحر بكلام أي يفزعونه (maqayis;jamhara)؛ الترعابة الفروقة (sihah;tahdhib;mufradat)؛ المرعبة القفرة المخيفة (tahdhib)
- **B002** suyla doldurmak veya dolmak — vadiyi dolduran sel · havuzu doldurmak · vadiyi suyla doldurmak veya vadinin suyla dolması
  سيل راعب إذا ملأ الوادي (maqayis;sihah;mufradat)؛ رعبت الحوض إذا ملأته (maqayis;sihah)؛ رعب الوادي إذا ملأه (tahdhib)؛ رعب الوادي بجنبتيه إذا امتلأ ماء وقد قالوا زغب بالزاي والزاي أكثر (jamhara)
- **B003** hörgücü şeritlere kesme ve kesilmiş parça — hörgücü kesmek · kesilmiş hörgüç · kesilmiş şey · uzunlamasına kesilmiş hörgüç şeritleri · hörgüçten kesilmiş parça · hörgüçten bir parça · genç, ince yapılı ve beyaz tenli kadın · bu nitelikteki genç kadın · hurma çiçek salkımının dibi · yağı damlayan hörgüç · yağla dolu hörgüç · yağı damlayan · hörgücün yağdan titremesi, kalınlaşması ve dolgunlaşması
  للشيء المقطع مرعب (maqayis)؛ الترعيب شطائب السنام إذا قطعت مستطيلة (jamhara)؛ السنام المرعب المقطع والترعيبة القطعة من السنام (sihah)؛ رعبت السنام قطعته (mufradat)؛ القطعة من السنام رعبوبة (maqayis;tahdhib)؛ جارية رعبوبة شطبة بيضاء (maqayis;sihah;tahdhib;mufradat)؛ أصل الطلعة رعبوبة أيضا (tahdhib)؛ سنام مرعوب يقطر دسما وسنام رعيب ممتلئ شحما (maqayis;sihah)
- **B004** güvercinin güçlü ötüşü — güçlü sesli güvercin · güçlü ötüşlü bir güvercin türü · bu güvercin türünün dişisi · sesi güçlenmek, güçlü ötmek · güvercinin güçlü ötüşü
  الحمام الرعبي والراعبي يرعب في صوته ترعيبا وهو شدة الصوت (ayn)؛ الحمام الراعبي يرعب في صوته ترعيبا وهو شدة الصوت (tahdhib)؛ الراعبي جنس من الحمام والأنثى راعبية (sihah)

## خ ر ب (root_000399) — identity root of يُخْرِبُونَ (w33)

- **B001** delik, oyuk veya geniş yarık; deri su kabında kulp ya da kulp yeri — delik veya geniş yarık · kulağı delinmiş veya yarılmış kimse · kulağı yarık veya delik kadın · yarılmış veya delinmiş · yarıklık veya yuvarlak deliklik durumu · kalça kemiğindeki delik · atın böğrünün üstündeki yuvarlak iz · deri su kabının kulpu veya kulp yeri · kova kulpunun geçtiği delik · iğne deliği
  أصل يدل على التثلم والتثقب؛ الخربة الثقبة؛ العبد الأخرب المثقوب الأذن؛ الخرب ثقب الورك؛ الخربة عروة المزادة (maqayis)؛ الخربة سعة خرت الأذن؛ كل ثقبة مستديرة فهي خربة؛ خرابة الإبرة خرتها (ayn)؛ خرق في الورك؛ الثقب في أذن الأخرب؛ عروة المزادة (jamhara)؛ كل ثقب مستدير فهو خربة؛ المخروب المشقوق؛ رجل أخرب للمشقوق الأذن (sihah)؛ الخربة شق واسع في الأذن؛ خربة المزادة (mufradat)
- **B002** yıkıma uğrama ve kullanılamaz hale gelme — yıkıntı ve kullanılamazlık durumu · yer yıkıntı durumuna gelmek · yıkık ve kullanılamaz · yıkık durumdaki · yıkıma uğratmak · yıkıp bozmak
  الخراب ضد العمارة (maqayis;jamhara;sihah)؛ خرب خرابا وخربته تخريبا؛ اللهم مخرب الدنيا ومعمر الآخرة أي خلقتها للخراب (ayn)؛ خرب المكان خرابا وهو ضد العمارة؛ أخربه وخربه؛ يخربون بيوتهم (mufradat)
- **B003** hırsızlıkla malda eksiltme — deve hırsızı; bazı kullanımlarda genel olarak hırsız · deve çalma · birinin develerini çalmak · hırsızlar veya deve hırsızları · malı tüketip götüren ağır zaman felaketi
  الخارب فسارق الإبل خاصة وهو القياس لأن السرق إيقاع ثلمة في المال (maqayis)؛ الخارب اللص؛ الخارب من شدائد الدهر؛ اللص من شدائد الدهر لأنه يستأصل أموال الناس (ayn)؛ الخرابة سرقة الإبل خاصة؛ اللص خارب (jamhara)؛ الخارب اللص؛ هو سارق البعران خاصة؛ خرب فلان بإبل فلان يخرب خرابة (sihah)؛ جعل الخارب مختصا بسارق الإبل (mufradat)
- **B004** bir toy kuşu türünün erkeği — bir toy kuşu türünün erkeği · bu toy kuşu türünün erkekleri
  الخرب وهو ذكر الحبارى والجمع خربان (maqayis)؛ الخرب الذكر من الحبارى ويجمع على خربان (ayn)؛ الخرب ذكر الحبارى والجمع خربان (jamhara)؛ الخرب ذكر الحبارى والجمع الخربان (sihah)؛ الخرب ذكر الحبارى وجمعه خربان (mufradat)
- **B005** keçiboynuzu; tek aktarımda başka bir ağaç — keçiboynuzu bitkisi · başka bir belirli ağaç türü · keçiboynuzu adının sesçe değişmiş biçimi
  الخروبة شجرة الينبوت (ayn)؛ الخروب نبت معروف (jamhara)؛ الخروب بالتشديد نبت معروف؛ والخرنوب لغة (sihah)
- **B006** iki ayrı yer adı — bir yer adı · bir kentte bulunan ve ikinci bir adla da bilinen yer adı
  أخرب موضع (maqayis)؛ خريبة موضع بالبصرة يسمى بصيرة الصغرى (ayn)؛ أخرب اسم موضع (jamhara)
- **B007** ana kum kütlesinin sona erdiği yer — ana kum kütlesinin sona erdiği yer
  الخرب منقطع الجمهور من الرمل (maqayis)؛ الخرب بالضم منقطع الجمهور من الرمل (sihah)
- **B008** kişide inanç bozukluğu veya lekeleyici kusur görmeme [kalıp] — onda inanç bozukluğu veya leke sayılan bir kusur görmedik
  ما رأينا من فلان خربا وخربة أي فسادا في دينه أو شينا (ayn)
- **B009** liften yapılmış, türü belirsiz nesne — liften veya benzeri malzemeden oluşan, türü belirsiz nesne
  الخرابة جبل من ليف ونحوه (ayn)

## ب ي ت (root_000166) — identity root of بُيُوتَهُم (w34)

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

## ي د ي (root_001693) — identity root of بِأَيْدِيهِمْ (w35)

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

## ء م ن (root_000054) — identity root of ٱلْمُؤْمِنِينَ (w37)

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ع ب ر (root_000974) — identity root of فَٱعْتَبِرُوا۟ (w38)

- **B001** bir yandan öbür yana geçme ve buna bağlı geçiş öğeleri — ırmağı geçmek · ırmak kıyısı ya da öte yan · geçiş yeri ya da geçiş aracı · ırmak geçiş teknesi · yoldan geçen kişi ya da yolcu · ölmek; yaşam yolunu geçmiş sayılmak · kullanımda geçerli dil biçimi
  أصل صحيح واحد يدل على النفوذ والمضي في الشيء (maqayis)؛ عبرت النهر عبورا (maqayis;ayn;sihah;tahdhib)؛ العبر شاطئ النهر وهما عبران (jamhara)؛ المعبر شط نهر هيء للعبور (maqayis;ayn;tahdhib)؛ المعبرة سفينة يعبر عليها النهر (ayn;tahdhib)؛ رجل عابر سبيل أي مار (maqayis;ayn;sihah)؛ عابر سبيل (mufradat)؛ عبر القوم أي ماتوا (sihah;tahdhib)
- **B002** düşün görünür içeriğinden örtük anlamını çıkarma — düşü yorumlamak · düş yorumu · düşünü yorumlatmak için birine anlatmak
  عبر الرؤيا يعبرها عبرا وعبارة ويعبرها تعبيرا إذا فسرها (maqayis)؛ عبر يعبر الرؤيا تعبيرا (ayn)؛ عبرت الرؤيا أعبرها وعبرتها تعبيرا والاسم العبارة (jamhara)؛ عبرت الرؤيا أعبرها عبارة فسرتها (sihah)؛ إن كنتم للرؤيا تعبرون (tahdhib;mufradat)؛ العابر الذي ينظر في الكتاب فيعبره أي يعتبر بعضه ببعض حتى يقع فهمه عليه (tahdhib)؛ التعبير مختص بتعبير الرؤيا وهو العابر من ظاهرها إلى باطنها (mufradat)
- **B003** düşünceyi sözle aktarma ve metni içten kavrama — sözü iyi aktarış · birinin söyleyemediğini onun adına dile getirmek · kitabı içinden okuyup düşünmek
  عبرت عن فلان تعبيرا إذا عي بحجته فتكلمت بها عنه (maqayis;ayn;tahdhib)؛ رجل حسن العبارة إذا كان حسن الأداء لما يسمع (jamhara)؛ عبرت الكتاب أعبره عبرا إذا تدبرته في نفسك ولم ترفع به صوتك (sihah;tahdhib)؛ اللسان يعبر عما في الضمير (sihah)؛ العبارة مختصة بالكلام العابر الهواء من لسان المتكلم إلى سمع السامع (mufradat)
- **B004** gözlenen durumdan karşılaştırmayla sonuç ve ders çıkarma — ders çıkarılacak olay ya da belirti · gözleyip karşılaştırarak ders çıkarmak
  العبرة الاعتبار لما مضى (ayn)؛ العبرة ما اعتبرت به من الآيات (jamhara)؛ فاعتبروا يا أولي الأبصار أي تدبروا وانظروا (tahdhib)؛ العبرة الاعتبار بما مضى (tahdhib;maqayis)؛ الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد (mufradat)؛ اعتبرت الشيء فكأنك نظرت إلى الشيء فجعلت ما يعنيك عبرا لذاك (maqayis)
- **B005** üzüntüyle gözyaşının birikip akması — gözyaşının akışı ya da gözyaşı · ağlamalı bir üzüntü yaşamak · gözleri yaşarmak · gözü yaşartan şey
  عبرة الدمع جريه والدمع أيضا نفسه عبرة (maqayis;ayn;tahdhib)؛ عبر فلان يعبر عبرا من الحزن وهو عبران والمرأة عبرى وعبرة (maqayis;ayn)؛ استعبر إذا جرت عبرته (maqayis;ayn;sihah)؛ العبرة تردد البكاء في الصدر وربما قيل لتردد الدمع في العين عبرة (jamhara)؛ العبرة بالفتح تحلب الدمع (sihah)؛ رأى فلان عبر عينيه أي ما يسخن عينيه (sihah;tahdhib)؛ عبر العين للدمع والعبرة كالدمعة (mufradat)
- **B006** uzun yolculukları sürdürecek güç ve dayanıklılık — uzun yolculuklara dayanıklı dişi deve · yolculuğa dayanıklı deve ya da develer · hızlı dişi deve
  ناقة عبر أسفار لا يزال يسافر عليها (maqayis;ayn)؛ ناقة عبر سفر إذا كانت قوية عليه (jamhara)؛ جمل عبر أسفار وجمال عبر أسفار وناقة عبر أسفار الذي لا يزال يسافر عليها (sihah)؛ فلان عبر أسفار إذا كان قويا على السفر (tahdhib)؛ العبار الإبل القوية على السير (tahdhib)؛ ناقة عبر أسفار (mufradat)؛ العبسرة الناقة السريعة والسين في ذلك زائدة وإنما هو من ناقة عبر أسفار (maqayis-routing)
- **B007** ırmak kıyısında yetişen iri ağaç ya da iri dikenli çalı — ırmak kıyısında yetişen iri ağaç; kimi kullanımda iri dikenli çalı
  العبري ضرب من السدر ويقال العبري الطويل من السدر الذي له سوق والضال ما صغر منه (ayn)؛ العبري السدر الذي ينبت على شاطئ الأنهار والضال ما نبت في السفوح وغيرها (jamhara)؛ العبري ما نبت من السدر على شطوط الأنهار وعظم (sihah)؛ العبري من السدر ما كان على شطوط الأنهار (tahdhib)؛ يقال للسدر وما عظم من العوسج العبري (tahdhib)؛ العبري ما ينبت على عبر النهر (mufradat)؛ ضرب من السدر عبري وإنما يكون كذلك إذا نبت على شطوط الأنهار (maqayis)
- **B008** Samanyolu'nu geçtiği söylenen belirli yıldız — Samanyolu'nu geçtiği söylenen yıldız
  الشعرى العبور نجم خلف الجوزاء (ayn)؛ الشعرى العبور سميت بذلك لأنها عبرت المجرة (jamhara)؛ الشعرى العبور إحدى الشعريين وهي التي خلف الجوزاء سميت بذلك لأنها عبرت المجرة (sihah)؛ الشعرى العبور سميت عبورا لأنها عبرت المجرة (tahdhib)؛ الشعرى العبور سميت بذلك لكونها عابرة (mufradat)
- **B009** paraları tek tek ya da ayrımdan sonra tartma; paraları çıkarma — paraları birer birer tartmak · paraları ayırdıktan sonra topluca tartmak · paraları dışarı çıkarmak
  عبرت الدنانير تعبيرا وزنتها دينارا دينارا (ayn;maqayis)؛ تعبير الدراهم وزنها جملة بعد التفاريق (sihah)؛ عبرت الدنانير تعبيرا إذا وزنتها دينارا دينارا (tahdhib)؛ لقد أسرعت استعبارك الدراهم أي استخراجك إياها (tahdhib)
- **B010** kesme ya da azaltma yapılmadan tam bırakılma — koyunların yününü bir yıl kırkmadan bırakmak · sünnet edilmemiş oğlan · cinsel organına kesim uygulanmamış kız · damızlık olması için yünü kırkılmamış koç · kılı yıllarca kırkılmamış teke · tüyleri tam bırakılmış ok
  كبش معبر إذا لم يجز صوفه ليستفحل (jamhara)؛ غلام معبر لم يختن (jamhara;sihah;tahdhib)؛ أعبرت الغنم إذا تركتها عاما لا تجزها (sihah;tahdhib)؛ جارية معبرة لم تخفض (sihah)؛ سهم معبر موفر الريش (sihah)؛ المعبر من الجمال الكثير الوبر والمعبر من الغلمان الذي لم يختن وما أدري ما وجه القياس في هذا (maqayis)؛ المعبر التيس الذي ترك عليه شعره سنوات فلم يجز (tahdhib)؛ العبر من الناس القلف واحدهم عبور (tahdhib)
- **B011** safran ya da safranlı kokulu madde karışımı — koku maddesi; safran ya da safranlı koku karışımı
  العبير ضرب من الطيب (ayn)؛ العبير ضرب من الطيب واختلف فيه أهل اللغة فقال قوم هو الزعفران بعينه وقال آخرون بل هو أنواع من الطيب تخلط (jamhara)؛ العبير أخلاط تجمع بالزعفران وقال أبو عبيدة العبير عند العرب الزعفران وحده (sihah)؛ العبير عند أهل الجاهلية الزعفران (tahdhib)؛ العبير ضرب من الطيب (tahdhib)؛ من هذا الشاذ العبير قال قوم هو الزعفران وقال قوم هي أخلاط طيب (maqayis)
- **B012** sayıca ya da miktarca çok olma — herhangi bir şeyin çoğu · çok kişinin bulunduğu oturum
  مجلس عبر كثير الأهل (jamhara)؛ العبر بالضم الكثير من كل شيء (sihah)؛ العبر أيضا الكثير في كل شيء (tahdhib)
- **B013** kaynağa göre yaşı ya da iriliği belirlenen dişi koyun — kaynağa göre belirli yaşta ya da irilikte dişi koyun
  العبور في بعض اللغات الجذعة من الغنم أو أصغر منها (jamhara)؛ العبور من الغنم فوق العظيم من إناث الغنم يقال لي نعجتان وثلاث عبائر (tahdhib)

## ب ص ر (root_000121) — identity root of ٱلْأَبْصَٰرِ (w40)

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

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO و ل ي (root_001684) — for لِأَوَّلِ (w11): withheld observed target; not identity

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

## ECHO ء ي د (root_000071) — for بِأَيْدِيهِمْ (w35): withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:2, and ## Buluşmalar) =====
## Kale, zırh ve içeriden açılan gedik

Bu surenin kelimeleri, ayetteki anlamlarının yanında, köklerinin taşıdığı başka sahneleri de duyurur. Bu aile imgeleri kelimenin ayetteki anlamının yerine geçmez, onun yanında işitilir. Aşağıda hep bu sınırla konuşulacak.

İkinci ayet bir kuşatmayı anlatır. Kuşatılanlar, {ar:مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ, tr:mâni'atuhum husûnuhum mina'llâh, gloss:kaleleri onları Allah'tan koruyacak, source:59:2} diye düşünmüşlerdir. Kale burada yalnızca yüksek bir yapı değildir. Kelime, içine ulaşılamayan kapalı yer demektir: {ar:الحصن كل موضع حصين لا يوصل إلى ما في جوفه, tr:el-hısn kullu mevdı'ın hasîn lâ yûsalu ilâ mâ fî cevfih, gloss:hısn, içindekine ulaşılamayan her korunaklı yerdir, source:"ح ص ن,B001"}. "Engelleyen" diye çevrilen fiil de aynı işi görür: araya girer ve içeri girilmesine izin vermez. Bu kelime ailesinde dokunulmazlık ile izzet tek bir ifadede birleşir: {ar:رجل منيع لا يخلص إليه وهو في عز ومنعة, tr:raculun meni' lâ yuhlasu ileyh ve huve fî 'izzin ve men'a, gloss:kendisine ulaşılamayan, izzet ve korunma içindeki adam, source:"م ن ع,B003"}. Sure ise bu izzeti baştan Allah'a verir: birinci ayet {ar:وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ, tr:ve huve'l-'azîzu'l-hakîm, gloss:O, mutlak güçlü, hüküm ve hikmet sahibidir, source:59:1} diye kapanır. "Azîz" kelimesi yenilmeyen, içine el uzatılamayan demektir: {ar:العزيز الممتنع فلا يغلبه شيء, tr:el-'azîzu'l-mümteni' fe-lâ yaglibuhû şey', gloss:azîz, hiçbir şeyin üstün gelemediği korunaklıdır, source:"ع ز ز,B001"}. "Hakîm" de bozulmayı önleyen bir tutmadır: {ar:حكم أصله منع منعا لإصلاح, tr:hakeme aslı men'a men'an li-ıslâh, gloss:hükmün aslı, düzeltmek için engellemektir, source:"ح ك م,B001"}. Böylece kale, yalnızca Allah'a ait olan dokunulmazlığı taş ile taklit eder. Sure bu iki ismi son ayette yine söyleyerek kuşatmayı iki ucundan kapatır.

Kuşatmanın işleyişi aynı ayetin fiillerinde görülür. {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. Burada surlar aşılmaz, saldırı hiç beklenmeyen bir yönden gelir. "Ev" kelimesinin ailesi, düşmana gece baskını yapmayı da anlatır: {ar:البيات والتبييت أن تأتي العدو ليلا, tr:el-beyâtu ve't-tebyît en te'tiye'l-'aduvve leylen, gloss:beyât, düşmana gece gelmektir, source:"ب ي ت,B004"}. Ayetteki "geldi" fiili ile "evler" kelimesi bu ifadede yan yana durur. Atılan şey de mancınık taşı gibidir: {ar:القذاف المنجنيق, tr:el-kazzâf el-mancınîk, gloss:kazzâf mancınıktır, source:"ق ذ ف,B001"}. Ama taş duvara değil kalplere düşer: {ar:وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ, tr:ve kazefe fî kulûbihimu'r-ru'b, gloss:kalplerine korku attı, source:59:2}. Gedik de dışarıdan açılmaz: {ar:يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ, tr:yuhribûne buyûtehum bi-eydîhim, gloss:evlerini kendi elleriyle yıkıyorlardı, source:59:2}. Bu fiilin kökü delmeyi ve gedik açmayı anlatır: {ar:أصل يدل على التثلم والتثقب, tr:asl yedullu 'ale't-tesellumi ve't-tesekkub, gloss:gedik ve delik açılmayı gösteren kök, source:"خ ر ب,B001"}. Yani kale, içine atılan bir korkunun açtırdığı deliklerle kendi içinden çöker. Benzer bir sahnede Allah, tuzak kuranların yapısına temelinden gelir: {ar:فَأَتَى ٱللَّهُ بُنْيَٰنَهُم مِّنَ ٱلْقَوَاعِدِ فَخَرَّ عَلَيْهِمُ ٱلسَّقْفُ, tr:fe-eta'llâhu bunyânehum mine'l-kavâ'idi fe-harra 'aleyhimu's-sakf, gloss:Allah yapılarına temellerinden geldi, tavan üstlerine çöktü, source:16:26}. Aynı ayet {ar:مِنْ حَيْثُ لَا يَشْعُرُونَ, tr:min haysu lâ yeş'urûn, gloss:farkına varmadıkları yerden, source:16:26} diye biter. Gece baskını da, kasabalara yöneltilen bir soruda geçer: {ar:أَن يَأْتِيَهُم بَأْسُنَا بَيَٰتًا وَهُمْ نَآئِمُونَ, tr:en ye'tiyehum be'sunâ beyâten ve hum nâimûn, gloss:onlar uyurken azabımızın gece baskınıyla gelmesinden, source:7:97}. Kitap ehlinden başka bir topluluk için de aynı söz söylenir: onlar {ar:مِن صَيَاصِيهِمْ, tr:min sayâsîhim, gloss:kalelerinden, source:33:26} indirilmiş ve kalplerine yine korku atılmıştır {source:33:26}.

On dördüncü ayet aynı kaleyi bu kez korkunun sığınağı olarak gösterir: {ar:لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍ, tr:lâ yukâtilûnekum cemî'an illâ fî kuran muhassanetin ev min verâi cudur, gloss:sizinle topluca ancak tahkimli kasabalarda ya da duvarlar ardından savaşırlar, source:59:14}. "Duvar" kelimesi, etrafı çevrili yeri anlatır: {ar:الجدير مكان بني حواليه جدار, tr:el-cedîr mekânun buniye havâleyhi cidâr, gloss:cedîr, çevresine duvar örülmüş yerdir, source:"ج د ر,B001"}. Ayet {ar:ذَٰلِكَ بِأَنَّهُمْ قَوْمٌ لَّا يَعْقِلُونَ, tr:zâlike bi-ennehum kavmun lâ ya'kılûn, gloss:çünkü onlar akıl etmeyen bir topluluktur, source:59:14} diye biter. Akıl kelimesinin ailesinde akıl ile sığınak aynı kelimedir: {ar:المعقل والعقل وهو الحصن, tr:el-ma'kılu ve'l-'akl ve huve'l-hısn, gloss:ma'kıl ve akıl, kaledir, source:"ع ق ل,B007"}. Dağa çekilip korunan ceylan da bu fiille anlatılır {source:"ع ق ل,B007"}. Böylece taştan surları çok olan topluluğun asıl eksiği iç kaledir. Nuh'un oğlu da böyle bir yanılgıya düşer ve {ar:سَـَٔاوِىٓ إِلَىٰ جَبَلٍ يَعْصِمُنِى مِنَ ٱلْمَآءِ, tr:se-âvî ilâ cebelin ya'sımunî mine'l-mâ', gloss:beni sudan koruyacak bir dağa sığınırım, source:11:43} der. Babası şöyle cevap verir: {ar:لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ, tr:lâ 'âsıme'l-yevme min emri'llâh, gloss:bugün Allah'ın emrinden koruyan yoktur, source:11:43}. Savaştan kaçan münafıklara da aynısı söylenir: {ar:وَلَوْ كُنتُمْ فِى بُرُوجٍ مُّشَيَّدَةٍ, tr:ve lev kuntum fî burûcin muşeyyede, gloss:sağlam yapılmış burçlarda olsanız bile, source:4:78}. O ayet de yine anlamayanlarla biter {source:4:78}. Allah'tan başka dost edinenlerin evi ise örümceğin evine benzer: {ar:وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ, tr:ve inne evhene'l-buyûti le-beytu'l-'ankebût, gloss:evlerin en zayıfı örümceğin evidir, source:29:41}. Buna karşılık Zülkarneyn'in demir seddini kuşatanlar onu delemez: {ar:وَمَا ٱسْتَطَٰعُوا۟ لَهُۥ نَقْبًا, tr:ve me'staṭâ'û lehû nakbâ, gloss:onu delmeye de güç yetiremediler, source:18:97}. Bu surede ise delik içeriden, sahiplerinin elleriyle açılır.

Dokuzuncu ayet bu kaleye karşı tersini koyar. Ensar, kendileri {ar:خَصَاصَةٌ, tr:hasâsa, gloss:darlık, yoksulluk, source:59:9} içindeyken bile başkalarını kendilerine tercih ederler. Bu kelimenin ailesinde kamıştan yapılmış aralıklı kulübe vardır: {ar:الخص بيت من قصب أو شجر وذلك لما يرى فيه من الخصاصة, tr:el-huss beytun min kasabin ev şecer, gloss:huss, aralıkları görünen kamış ya da dal evdir, source:"خ ص ص,B004"}. Delikli bu kulübe ayakta kalır, surlu kasaba ise içeriden yıkılır. Aynı ayet asıl tehlikeli duvarı içe, nefse yerleştirir: {ar:وَمَن يُوقَ شُحَّ نَفْسِهِۦ, tr:ve men yûka şuhha nefsih, gloss:kim nefsinin cimriliğinden korunursa, source:59:9}. Cimrilik kelimesinin aslı tutmak ve geri çevirmektir: {ar:الأصل فيه المنع ثم يكون منعا مع حرص, tr:el-aslu fîhi'l-men' summe yekûnu men'an ma'a hırs, gloss:aslı engellemedir, sonra hırsla engelleme olur, source:"ش ح ح,B001"}. Böylece "engelleyen kaleler" ile "engelleyen nefis" aynı kökten ses verir. Kurtuluş, bu iç kaleden "korunmak"tır. "Korunmak" fiili kalkan anlamıyla birlikte işitilir: {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:ittaki'llâh, gloss:Allah'tan sakın, yani kendinle O'nun azabı arasına bir siper koy, source:"و ق ي,B002"}. Zırh imgesi de buradan girer. "Kale" kelimesi zırhı anlatmak için de kullanılır: {ar:يتجوز به في كل تحرز ومنه درع حصينة, tr:yutecevvezu bihî fî kulli tahârruz, ve minhu dir'un hasîna, gloss:her korunma için mecazen kullanılır; sağlam zırh da buradandır, source:"ح ص ن,B001"}. Yirminci ayetin "cennet" kelimesi de kalkan ailesindendir: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micenn et-turs, ve'l-cunne ed-dir', gloss:micenn kalkandır, cunne zırhtır; seni koruyan her şey senin cunnendir, source:"ج ن ن,B008"}. Davud'a öğretilen zırh sanatı insanları {ar:لِتُحْصِنَكُم مِّنۢ بَأْسِكُمْ, tr:li-tuhsınekum min be'sikum, gloss:sizi savaşın şiddetinden korusun diye, source:21:80} içindir. Münafıklar ise yeminlerini kalkan edinir: {ar:ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةً, tr:ittehazû eymânehum cunne, gloss:yeminlerini kalkan edindiler, source:63:2}. Surenin yaşayan duvarı müminlerin safıdır: {ar:كَأَنَّهُم بُنْيَٰنٌ مَّرْصُوصٌ, tr:ke-ennehum bunyânun marsûs, gloss:sanki birbirine kenetlenmiş bir yapı, source:61:4}.

Kaynaklar: 59:2 حُصُونُهُم ح ص ن B001; 59:2 مَّانِعَتُهُمْ م ن ع B003; 59:1/23/24 ٱلْعَزِيزُ ع ز ز B001; 59:1/24 ٱلْحَكِيمُ ح ك م B001; 59:2 فَأَتَىٰهُمُ ء ت ي B011; 59:2 بُيُوتَهُم ب ي ت B004; 59:2 وَقَذَفَ ق ذ ف B001; 59:2 يُخْرِبُونَ خ ر ب B001; 59:14 جُدُرٍ ج د ر B001; 59:14 يَعْقِلُونَ ع ق ل B007; 59:9 خَصَاصَةٌ خ ص ص B004; 59:9 شُحَّ ش ح ح B001; 59:9/18 يُوقَ / ٱتَّقُوا و ق ي B002; 59:20 ٱلْجَنَّةِ ج ن ن B008

## İnin gizli kapısı

İkinci ayetin sonundaki {ar:لِأَوَّلِ ٱلْحَشْرِ, tr:li-evveli'l-haşr, gloss:ilk toplayıp sürmede, source:59:2} ifadesindeki "haşr" kelimesi, ailesinde yeryüzünün küçük in hayvanlarını da adlandırır: {ar:حشرات الأرض دوابها الصغار كاليرابيع والضباب, tr:haşarâtu'l-ard devâbbuhe's-sığâr ke'l-yerâbî' ve'd-dıbâb, gloss:haşarât, arap tavşanı ve keler gibi küçük yer hayvanlarıdır, source:"ح ش ر,B004"}. Buradaki sahnede insanlar yuvalarından çıkarılıp topluca sürülür.

On birinci ayet, bu yuvanın mimarisini münafıklara bağlar: {ar:أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟, tr:e-lem tera ile'llezîne nâfekû, gloss:münafıklık edenleri görmedin mi, source:59:11}. Kelimenin kökünde arap tavşanının yuvası vardır. Hayvan yuvasına bir giriş kazar, bir de yüzeye kadar inceltip kapalı bıraktığı gizli bir çıkış yapar. Avcı girişten gelince başıyla bu ince kabuğu kırıp kaçar: {ar:النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج, tr:en-nâfikâ' mevdı'un yurakkıkuhu'l-yerbû', fe-izâ utiye min kıbeli'l-kâsı'â' darabehâ bi-ra'sihî fe'ntefeka, gloss:nâfikâ, tavşanın incelttiği yerdir; kâsıâ tarafından gelinince başıyla vurur ve dışarı fırlar, source:"ن ف ق,B003"}. Bu aile, aynı tabloyu dine de taşır: {ar:النفاق الدخول في الشرع من باب والخروج عنه من باب, tr:en-nifâk ed-duhûl fi'ş-şer'i min bâb ve'l-hurûc 'anhu min bâb, gloss:nifak, dine bir kapıdan girip öbür kapıdan çıkmaktır, source:"ن ف ق,B004"}. Bu tabloda iki fiil öne çıkar: "gelinmek" ve "çıkmak". Surede de aynı iki fiil işler. Allah Nadîr'e beklenmedik yerden "gelir" ve onları "çıkarır". Münafıklar ise {ar:لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ, tr:le-in uhrictum le-nahrucenne me'akum, gloss:çıkarılırsanız sizinle çıkarız, source:59:11} diye söz verir. On ikinci ayet bunun karşılığını verir: {ar:لَئِنْ أُخْرِجُوا۟ لَا يَخْرُجُونَ مَعَهُمْ, tr:le-in uhricû lâ yahrucûne me'ahum, gloss:çıkarılırlarsa onlarla çıkmazlar, source:59:12}. Gizli kapının sahibi kimseyle birlikte çıkmaz, yalnız kendi deliğinden kaçar. İki kapılı yuva, münafıkların iki yüzlü konuşmasında da görülür: {ar:وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ إِلَىٰ شَيَٰطِينِهِمْ قَالُوٓا۟ إِنَّا مَعَكُمْ, tr:ve izâ lakû'llezîne âmenû kâlû âmennâ ve izâ halev ilâ şeyâtînihim kâlû innâ me'akum, gloss:müminlerle karşılaşınca "inandık" derler, şeytanlarıyla baş başa kalınca "sizinleyiz" derler, source:2:14}. Başka bir yerde Kur'an onların aradığı deliği açıkça söyler: {ar:لَوْ يَجِدُونَ مَلْجَـًٔا أَوْ مَغَٰرَٰتٍ أَوْ مُدَّخَلًا لَّوَلَّوْا۟ إِلَيْهِ وَهُمْ يَجْمَحُونَ, tr:lev yecidûne melce'en ev meğârâtin ev muddehalen le-vellev ileyhi ve hum yecmehûn, gloss:bir sığınak, mağaralar ya da girilecek bir delik bulsalar, dizginsiz koşarak oraya kaçarlardı, source:9:57}. Bu sözden hemen önce onların {ar:قَوْمٌ يَفْرَقُونَ, tr:kavmun yefrakûn, gloss:korkan bir topluluk, source:9:56} oldukları söylenir. Her sesi kendilerine karşı sanmaları da aynı ürkek hayvanın tavrıdır {source:63:4}.

Beşinci ve on dokuzuncu ayetlerdeki "fâsıklar" kelimesi aynı tabloya bir hayvan daha ekler. Fare, yuvasından çıkıp zarar verdiği için bu kökle adlandırılmıştır: {ar:سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها, tr:summiyeti'l-fe'ratu fuveysika ... li-hurûcihâ min beytihâ, gloss:fareye, evinden çıktığı için küçük fâsık denildi, source:"ف س ق,B003"}. Fısk, buna göre bulunması gereken kabuktan ve yerden dışarı çıkmaktır. On dokuzuncu ayet, Allah'ı unutanları {ar:أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ, tr:ulâike humu'l-fâsikûn, gloss:onlar yoldan çıkanların ta kendileridir, source:59:19} diye adlandırırken bu çıkışı ahlaki bir anlamla söyler. On yedinci ayetteki "ebedî kalıcılar" kelimesinin ailesinde ise kör bir yer hayvanı vardır: {ar:الخلد ضرب من الجرذان عمي لم يخلق لها عيون, tr:el-huld darbun mine'l-cirzân 'umy, gloss:huld, gözsüz yaratılmış kör bir sıçan türüdür, source:"خ ل د,B005"}. İkinci ayetteki {ar:يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:yâ uli'l-ebsâr, gloss:ey basiret sahipleri, source:59:2} hitabının karşı ucunda bu körlük durur. Yirmi üçüncü ayetteki "ortak koşmak" fiilinin ailesinde de avın dolandığı tuzak ipi vardır: {ar:الشرك حبالة يرتبك فيها الصيد, tr:eş-şerek hibâle yertebiku fîhe's-sayd, gloss:şerek, avın içinde dolaştığı tuzak ağıdır, source:"ش ر ك,B006"}. Ortak koşan kişi, kurtuluş sandığı bağlara kendini dolar.

Kaynaklar: 59:2 ٱلْحَشْرِ ح ش ر B004; 59:11 نَافَقُوا ن ف ق B003, B004; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B003; 59:17 خَٰلِدَيْنِ خ ل د B005; 59:23 يُشْرِكُونَ ش ر ك B006

## Başka yerden gelen sel, yağmayan bulut, sönük çakmak

İkinci ayetteki "hesaba katmadıkları yerden geldi" sözü, kelime ailesinde bir sel sahnesiyle de işitilir: {ar:سيل أتي وأتاوي إذا جاءك ولم يصبك مطره, tr:seylun etiyyun ve etâviyyun izâ câ'eke ve lem yusıbke matarüh, gloss:yağmuru sana değmediği halde sana gelen sel, source:"ء ت ي,B005"}. Kişi kendi göğüne bakar, bulut görmez. Su ise başka bir diyarda yağmış ve vadiden ona gelmiştir. "Hesaba katmamak" fiili de gökten gelen dolu ile aynı ailededir: {ar:حسبان من السماء بالبرد, tr:husbân mine's-semâ' bi'l-berad, gloss:gökten gelen dolu, source:"ح س ب,B007"}. Onların kalbine atılan "ru'b" (korku) da vadiyi dolduran bir seldir: {ar:سيل راعب إذا ملأ الوادي, tr:seylun râ'ib izâ mele'e'l-vâdî, gloss:vadiyi doldurduğunda sel "râib" olur, source:"ر ع ب,B002"}. Bu korku kalpte bir duygu olarak kalmaz, vadiyi dolduran su gibi her yeri kaplar. Surenin başındaki "Azîz" ismi de, başka bir dalda, karşı konulmaz seli anlatır: {ar:سيل عز وهو السيل الغالب, tr:seylun 'izz, gloss:galip gelen sel, source:"ع ز ز,B008"}. "Haşr" kelimesinde ise kıtlık yılının insanları şehirlere sürmesi vardır: {ar:حشرتهم السنة إذا أصابهم الضر حتى يهبطوا الأمصار, tr:haşerethumu's-sene, gloss:sıkıntı onlara dokunup şehirlere inmeye zorlayınca "yıl onları sürdü" denir, source:"ح ش ر,B002"}. On beşinci ayette ise önceki topluluk bu suyun ağırlığını tatmıştır: {ar:ذَاقُوا۟ وَبَالَ أَمْرِهِمْ, tr:zâkû vebâle emrihim, gloss:işlerinin vebalini tattılar, source:59:15}. "Vebâl" sağanakla aynı köktendir: {ar:الوبل والوابل المطر الشديد, tr:el-vebl ve'l-vâbil el-matar eş-şedîd, gloss:vebl ve vâbil şiddetli yağmurdur, source:"و ب ل,B001"}. Bir anlamı da ağırlıktır {source:"و ب ل,B002"}. Firavun'un yakalanışı da {ar:أَخْذًا وَبِيلًا, tr:ahzen vebîlâ, gloss:ağır bir yakalayış, source:73:16} diye anlatılır. Aynı sözler başka bir surede de neredeyse aynen tekrarlanır: {ar:فَذَاقُوا۟ وَبَالَ أَمْرِهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ, tr:fe-zâkû vebâle emrihim ve lehum 'azâbun elîm, gloss:işlerinin vebalini tattılar, onlara acı bir azap da var, source:64:5}. Kur'an aynı sahneyi bir bahçe için de kurar: sahipleri ona güç yetirdiklerini sanırken {ar:أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًا فَجَعَلْنَٰهَا حَصِيدًا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:etâhâ emrunâ leylen ev nehâran fe-ce'alnâhâ hasîden ke-en lem tağne bi'l-ems, gloss:gece ya da gündüz emrimiz ona geldi, onu dünkü gün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Orada da "zannettiler" ve "geldi" fiilleri yan yana durur, tıpkı ikinci ayette olduğu gibi.

Su sahnesinin bir de ters yüzü vardır. Altıncı ayetteki "atlar" kelimesinin ailesinde, yağacakmış gibi görünen bulut vardır: {ar:الخيال غيم ينشأ يخيل إليك أنه ماطر, tr:el-hayâl ğaymun yenşe'u yuhayyilu ileyke ennehû mâtır, gloss:hayâl, sana yağacakmış gibi görünen buluttur, source:"خ ي ل,B004"}. On birinci ayette münafıklar {ar:وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ, tr:ve in kûtiltum le-nensurannekum, gloss:size savaş açılırsa mutlaka yardım ederiz, source:59:11} diye söz verir. "Yardım etmek" fiili, ailesinde yağmurun bir yeri sulamasıdır: {ar:نصر الغيث البلاد أرواها, tr:nasara'l-ğaysu'l-bilâd ervâhâ, gloss:yağmur ülkeye yardım etti, yani onu suladı, source:"ن ص ر,B004"}. Bu vaat de hiç yağmayan buluta döner. On birinci ayetin sonu da bunu söyler: {ar:وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ, tr:va'llâhu yeşhedu innehum le-kâzibûn, gloss:Allah şahitlik eder ki onlar yalancıdır, source:59:11}. Yalan kelimesi, ailesinde kesilen süt akışına da uzanır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü, süreceği sanılıp sürmeyince "yalan söyledi" denir, source:"ك ذ ب,B006"}. Aynı tanıklık münafıklar için başka bir yerde aynı sözlerle verilir {source:63:1}. Kur'an münafıkları ayrıca karanlık, gök gürültüsü ve şimşekle dolu bir sağanağa benzetir {source:2:19}. Burada ise sağanak bile yoktur, yalnızca yağmur gösterip yağmayan bir hayal vardır. Ensar'ın kurtulduğu cimrilik de suyla ilgili bir ifadeyle anlatılır: {ar:أرض شحاح لا تسيل إلا من مطر جود, tr:ardun şihâh, gloss:ancak bol yağmurla sel akıtan cimri toprak, source:"ش ح ح,B004"}.

Ateş tarafında da aynı şey görülür. Dokuzuncu ayetteki cimrilik, ailesinde ateş vermeyen çakmaktır: {ar:الزند الشحاح الذي لا يوري, tr:ez-zendu'ş-şihâh ellezî lâ yûrî, gloss:kıvılcım çıkarmayan cimri çakmak, source:"ش ح ح,B003"}. On dördüncü ayetteki "ardından" kelimesi ise ateş veren çakmağın köküdür: {ar:ورى الزند خرجت ناره, tr:verâ'z-zend, gloss:çakmak ateşini çıkardı, source:"و ر ي,B002"}. Aynı kökte bir deyim de vardır: {ar:لوريت عن مولاك أي نصرته ودفعت عنه, tr:le-verayte 'an mevlâk, gloss:dostuna ateş yaktın, yani ona yardım ettin ve onu korudun, source:"و ر ي,B003"}. Böylece duvarların "ardından" savaşanlar, vaat ettikleri çakmağı hiç yakmamış olurlar. Atların yararsız kıvılcımları da bu aileye girer: {ar:نار الحباحب ما أورت الخيل لا ينتفع به, tr:nâru'l-hubâhib, gloss:hubâhib ateşi, atların çıkardığı, işe yaramayan kıvılcımdır, source:"ح ب ب,B011"}. Gerçek ateşin Allah'ın verdiği bir nimet olduğu bir soruyla hatırlatılır: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-ra'eytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Savaş için yakılan ateşi Allah söndürür: {ar:كُلَّمَآ أَوْقَدُوا۟ نَارًا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ, tr:kullemâ evkadû nâren li'l-harbi atfe'ehâ'llâh, gloss:savaş için her ateş yaktıklarında Allah onu söndürdü, source:5:64}.

Aynı boşluk hücum sahnesinde de görülür. Altıncı ayet müminlere {ar:فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍ وَلَا رِكَابٍ, tr:fe-mâ evceftum 'aleyhi min haylin ve lâ rikâb, gloss:onun için ne at ne deve koşturdunuz, source:59:6} der. "Vecîf", dörtnaldan aşağı hızlı bir yürüyüştür {source:"و ج ف,B001"}. Hücum yapılmadan kazanç gelmiştir, çünkü {ar:وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ, tr:ve lâkinna'llâhe yusallıtu rusulehû 'alâ men yeşâ', gloss:fakat Allah elçilerini dilediğinin üzerine musallat eder, source:59:6}. Bedir'de de aynı ilke söylenir: {ar:وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَٰكِنَّ ٱللَّهَ رَمَىٰ, tr:ve mâ rameyte iz rameyte ve lâkinna'llâhe ramâ, gloss:attığın zaman sen atmadın, Allah attı, source:8:17}. Sekizinci ayetin muhacirleri {ar:أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ, tr:ulâike humu's-sâdıkûn, gloss:sadık olanlar onlardır, source:59:8} diye anılır. Bu kelime savaşta hakkını vermek anlamını da taşır: {ar:صدق في القتال إذا وفى حقه, tr:sadaka fi'l-kıtâl, gloss:savaşta hakkını verdiyse "sadık oldu" denir, source:"ص د ق,B004"}. Münafıkların "yalan"ı ise hücuma kalkıp yarıda durmaktır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezebe, gloss:hücuma kalktı sonra "yalan söyledi", yani hücumu sonuna kadar götürmedi, source:"ك ذ ب,B004"}. Böylece sekizinci ve on birinci ayetler bir süvari tablosunun iki yarısı olur. Aynı müminler başka bir surede de aynı kelimeyle kapanır {source:49:15}, ahitlerine sadık kalan adamlar da yine bu fiille anılır {source:33:23}. Münafıkların "savaş olacağını bilsek size uyardık" sözü de yarıda kalan hücumun bir örneğidir {source:3:167}.

Kaynaklar: 59:2 فَأَتَىٰهُمُ ء ت ي B005; 59:2 يَحْتَسِبُوا ح س ب B007; 59:2 ٱلرُّعْبَ ر ع ب B002; 59:1/23/24 ٱلْعَزِيزُ ع ز ز B008; 59:2 ٱلْحَشْرِ ح ش ر B002; 59:15 وَبَالَ و ب ل B001, B002; 59:6 خَيْلٍ خ ي ل B004; 59:11 لَنَنصُرَنَّكُمْ ن ص ر B004; 59:11 لَكَٰذِبُونَ ك ذ ب B006, B004; 59:9 شُحَّ ش ح ح B004, B003; 59:14 وَرَآءِ و ر ي B002, B003; 59:9 يُحِبُّونَ ح ب ب B011; 59:6 أَوْجَفْتُمْ و ج ف B001; 59:8 ٱلصَّٰدِقُونَ ص د ق B004

## Yarılan kaya, dağılan topluluk, yarılan toprak

Dördüncü ayet sürgünün sebebini söyler: {ar:ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ, tr:zâlike bi-ennehum şâkku'llâhe ve resûleh, gloss:bu, onların Allah'a ve Resulüne karşı ayrılığa düşmeleri yüzündendir, source:59:4}. Bu fiilin kökü yarmaktır: {ar:شققت الشيء أشقه شقا إذا صدعته, tr:şekaktu'ş-şey', gloss:bir şeyi çatlattığımda "yardım" denir, source:"ش ق ق,B001"}. Topluluk için de kullanılır: {ar:الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت, tr:eş-şikâk, gloss:şikâk ayrılıktır; topluluk çatlayıp dağıldığında olur, source:"ش ق ق,B004"}. Bu tanımdaki "çatlamak" fiili, yirmi birinci ayetteki dağın {ar:مُّتَصَدِّعًا, tr:mutesaddi'an, gloss:parçalanmış, çatlamış, source:59:21} haliyle aynı köktendir. Kökün bir dalı topluluğun dağılmasını da anlatır: {ar:تصدع القوم إذا تفرقوا, tr:tesadda'a'l-kavm, gloss:topluluk dağılınca "tesadda'a" denir, source:"ص د ع,B005"}. Böylece dördüncü ve yirmi birinci ayetler aynı kelime alanına girer. Allah'a karşı ayrılığa düşenlerin bu yarılması kendi içlerine döner. On dördüncü ayet şöyle der: {ar:بَأْسُهُم بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ, tr:be'suhum beynehum şedîd, tahsebuhum cemî'an ve kulûbuhum şettâ, gloss:kendi aralarındaki çekişmeleri şiddetlidir; onları toplu sanırsın, oysa kalpleri dağınıktır, source:59:14}. "Şettâ" kelimesi, kenetlenmenin kalkmasıdır: {ar:ارتفاع الالتئام بينهما, tr:irtifâ'u'l-iltiâm beynehumâ, gloss:ikisi arasındaki kaynaşmanın kalkması, source:"ش ت ت,B003"}. "Aralarında" kelimesi de hem bağı hem kopuşu taşır: {ar:البين الفراق, tr:el-beyn el-firâk, gloss:beyn ayrılıktır, source:"ب ي ن,B001"}. Aynı kelime bir yerde de "bağ" anlamındadır {source:"ب ي ن,B003"}. "Toplu" kelimesinin ailesinde ise "dağınık" kelimesiyle aynı ifadede geçen bir anlam vardır: {ar:جماع الناس أخلاطهم وهم الأشابة من قبائل شتى, tr:cimâ'u'n-nâs, gloss:insanların cimâı, dağınık kabilelerden gelmiş karışık kalabalıktır, source:"ج م ع,B002"}. Yani dışarıdan toplu görünen şey, içten derlenip toplanmış bir yığından ibarettir. Kur'an bu cezayı başka bir yerde açıkça sayar: {ar:أَوْ يَلْبِسَكُمْ شِيَعًا وَيُذِيقَ بَعْضَكُم بَأْسَ بَعْضٍ, tr:ev yelbisekum şiya'an ve yuzîka ba'dakum be'se ba'd, gloss:ya da sizi gruplara ayırıp kiminize kiminizin şiddetini tattırmaya, source:6:65}. Dağılanlar işlerini {ar:فَتَقَطَّعُوٓا۟ أَمْرَهُم بَيْنَهُمْ زُبُرًا, tr:fe-tekatta'û emrehum beynehum zuburâ, gloss:işlerini aralarında parça parça böldüler, source:23:53} de bölmüşlerdir. Dördüncü ayetin sözleri Bedir için de aynen söylenir {source:8:13}. Yüz çevirenler için başka bir yerde {ar:فَإِنَّمَا هُمْ فِى شِقَاقٍ, tr:fe-innemâ hum fî şikâk, gloss:onlar ancak bir ayrılık içindedir, source:2:137} denir. Toplu sanılan kalabalığın sonu da bellidir: {ar:سَيُهْزَمُ ٱلْجَمْعُ وَيُوَلُّونَ ٱلدُّبُرَ, tr:se-yuhzemu'l-cem'u ve yuvellûne'd-dubur, gloss:o topluluk bozguna uğrayacak ve arkalarını dönüp kaçacaklar, source:54:45}. Müminlere ise bunun tersi verilmiştir: {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًا, tr:fe-ellefe beyne kulûbikum fe-asbahtum bi-ni'metihî ihvânâ, gloss:kalplerinizi birleştirdi de onun nimetiyle kardeş oldunuz, source:3:103}. Bu birleştirme, malla yapılabilecek bir iş de değildir {source:8:63}. Onuncu ayetteki {ar:وَلِإِخْوَٰنِنَا, tr:ve li-ihvâninâ, gloss:ve kardeşlerimize, source:59:10} duası bunun içindir.

Yarılmanın bir de bereketli yüzü vardır. Dokuzuncu ayetin "kurtuluşa erenler" kelimesi, kökünde yarmaktır: {ar:أصل يدل على شق, tr:aslun yedullu 'alâ şakk, gloss:yarmayı gösteren kök, source:"ف ل ح,B001"}. Çiftçi de toprağı yardığı için bu kelimeyle anılır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan, gloss:toprağı yardığı için ırgata "fellâh" denildi, source:"ف ل ح,B003"}. "Kâfir" kelimesi ise tohumu toprakla örten ekici de demektir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfir ez-zâri', gloss:kâfir, tohumu toprakla örttüğü için ekicidir, source:"ك ف ر,B008"}. Toprağı yaran filiz de "sad'" kökündendir: {ar:الصدع النبات لأنه يصدع الأرض, tr:es-sad' en-nebât, gloss:toprağı yardığı için bitkiye sad' denir, source:"ص د ع,B003"}. Böylece surede iki tür yarılma vardır. Biri, Allah'tan ayrılığa düşüp kendi içinden dağılmaktır. Öbürü, toprağı yarıp örtülü tohumu filizlendiren yarılmadır. Kur'an bu ikinci yarılmayı açıkça anlatır: {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّا, tr:summe şekaknâ'l-arda şakkâ, gloss:sonra toprağı iyice yardık, source:80:26}. Sekizinci ayetteki muhacirlerin tarifi, başka bir surede bir ekin benzetmesine bağlanır. Peygamberin yanındakiler orada da {ar:يَبْتَغُونَ فَضْلًا مِّنَ ٱللَّهِ وَرِضْوَٰنًا, tr:yebteğûne fadlen mina'llâhi ve ridvânâ, gloss:Allah'tan lütuf ve rıza ararlar, source:48:29} diye anılır ve {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ, tr:ke-zer'in ahrace şat'eh, gloss:filizini çıkarmış bir ekin gibi, source:48:29} oldukları söylenir. Bu ekin {ar:يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ, tr:yu'cibu'z-zurrâ'a li-yeğîza bihimu'l-kuffâr, gloss:ekicileri hayran bırakır, onlarla kâfirleri öfkelendirir, source:48:29}. Burada "küffâr" kelimesi ekicilerin hemen yanında durur. Dünya hayatı da {ar:كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ, tr:ke-meseli ğaysin a'cebe'l-kuffâra nebâtuh, gloss:bitkisi ekicileri hayran bırakan bir yağmur gibidir, source:57:20} diye anlatılır. Bu ayette "küffâr" kelimesi ekiciler anlamına daha da yakındır.

Kaynaklar: 59:4 شَآقُّوا ش ق ق B001, B004; 59:21 مُّتَصَدِّعًا ص د ع B005, B003; 59:14 شَتَّىٰ ش ت ت B003; 59:14 بَيْنَهُمْ ب ي ن B001, B003; 59:14 جَمِيعًا ج م ع B002; 59:9 ٱلْمُفْلِحُونَ ف ل ح B001, B003; 59:2/11 كَفَرُوا ك ف ر B008

## Hurmalık

Beşinci ayet, kuşatma sırasında bir hurmalıkta yapılan iki şeyi yan yana koyar: {ar:مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ, tr:mâ kata'tum min lînetin ev teraktumûhâ kâimeten 'alâ usûlihâ fe-bi-izni'llâh, gloss:hurma ağaçlarından neyi kestiyseniz ya da köklerinin üzerinde ayakta bıraktıysanız, Allah'ın izniyle oldu, source:59:5}. "Lîne" hurma ağacının adıdır ve türüne göre ayrılmaz: {ar:لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع, tr:lîne, gloss:lîne, yumuşak bir hurma ağacıdır; bir türe has değildir, source:"ل ي ن,B006"}. "Kesmek" ile "izin" bir ifadede de birleşir: {ar:أقطعته قضبانا أي أذنت له في قطعها, tr:akta'tuhû kudbânen, gloss:ona dal kesmeye izin verdim, source:"ق ط ع,B013"}. Böylece kesme de bırakma da yalnız sahibinin izniyle yapılabilir. "Kökler" kelimesi de hurmanın kalıcılığına bağlanır: {ar:النخل بأرضنا أصيل أي لا يفنى ولا يزول, tr:en-nahl bi-ardınâ asîl, gloss:bizim toprağımızda hurma köklüdür, yani tükenmez ve yok olmaz, source:"ء ص ل,B002"}. Aynı kökün bir dalı kökünden sökmektir {source:"ء ص ل,B001"}. Ayet ise ağacı sökmez, "kökleri üzerinde ayakta" bırakılabileceğini söyler. Kur'an bu farkı başka bir yerde iki ağaçla gösterir: güzel ağacın {ar:أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ, tr:asluhâ sâbitun ve far'uhâ fi's-semâ', gloss:kökü sabit, dalı göktedir, source:14:24} ve {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tu'tî ukulehâ kulle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman meyvesini verir, source:14:25}. Kötü ağaç ise {ar:ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ مَا لَهَا مِن قَرَارٍ, tr:uctussat min fevki'l-ardı mâ lehâ min karâr, gloss:yerin üstünden koparılmıştır, karar kılacak yeri yoktur, source:14:26}. Bu surede de "izin" kelimesi hurma ile birlikte geçer.

Aynı ayetin sonu {ar:وَلِيُخْزِىَ ٱلْفَٰسِقِينَ, tr:ve li-yuhziye'l-fâsikîn, gloss:ve fâsıkları rezil etmek için, source:59:5} der. "Fısk" kelimesi, hurma tablosunda olgun hurmanın kabuğundan sıyrılmasıdır: {ar:فسقت الرطبة عن قشرها, tr:fesekati'r-rutabe 'an kışrihâ, gloss:taze hurma kabuğundan çıktı, source:"ف س ق,B002"}. Ağaçlar köklerinde dururken, fâsıklar kabuklarından dışarı çıkar. Altıncı ayetteki "binek develeri" kelimesinin ailesinde de kökü toprağa ulaşmayan bir hurma filizi vardır: {ar:الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق, tr:er-râkib, gloss:râkib, hurma gövdesinde biten ve toprakta kökü olmayan filizdir, source:"ر ك ب,B007"}. Bu filiz, "kökleri üzerinde ayakta" duran ağacın tersidir. İkinci ayetteki "kalpler" kelimesi de hurmanın yenen özünü adlandırır: {ar:قلب النخلة شحمتها, tr:kalbu'n-nahle şahmetuhâ, gloss:hurmanın kalbi onun özüdür, source:"ق ل ب,B003"}. Bu dalda hurmanın özünü sökmek de anlatılır {source:"ق ل ب,B003"}. Korkunun atıldığı yer böylece ağacın canlı özüne benzer. Yirminci ayetteki "cennet" kelimesinde Araplar hurmalığı da görür: {ar:العرب تسمي النخيل جنة, tr:el-'Arab tusemmi'n-nahîle cenne, gloss:Araplar hurmalığa cennet derler, source:"ج ن ن,B003"}. Yirmi üçüncü ayetteki "Cebbâr" ismi de, ailesinde elin yetişemediği yüksek hurmayı anlatır: {ar:الجبار من النخل الذي قد فات اليد, tr:el-cebbâr mine'n-nahl ellezî kad fâte'l-yed, gloss:cebbâr, eli aşmış uzun hurmadır, source:"ج ب ر,B002"}. Böylece sure kesilen ya da bırakılan hurmalarla başlayıp, el yetişmeyen yüksekliğe ve kalıcı bahçeye varır. Kur'an'da terk edilmiş hurmalıklar ve harap yurtlar yan yana durur. Firavun'un halkı için {ar:كَمْ تَرَكُوا۟ مِن جَنَّٰتٍ وَعُيُونٍ, tr:kem terakû min cennâtin ve 'uyûn, gloss:nice bahçe ve pınar bırakıp gittiler, source:44:25} denir. Ad kavminin cesetleri de {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍ, tr:ke-ennehum a'câzu nahlin hâviye, gloss:içi boş hurma kütükleri gibi, source:69:7} yerde yatar. Yoksula kapıyı kapatmak için sabah erkenden ürünü kesmeye yemin eden bahçe sahipleri de vardır {source:68:17}. Onlar {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme 'aleykum miskîn, gloss:bugün oraya yanınıza hiçbir yoksul girmesin, source:68:24} diye fısıldaşmışlardır. Sonunda bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:biçilmiş gibi oldu, source:68:20}. Bu sahne, yedinci ayetin yoksullara ayırdığı payın tam tersidir. Bahçesi yıkılan öteki adam da {ar:يُقَلِّبُ كَفَّيْهِ, tr:yukallibu keffeyh, gloss:ellerini ovuşturur, source:18:42}.

Kaynaklar: 59:5 لِّينَةٍ ل ي ن B006; 59:5 قَطَعْتُم ق ط ع B013; 59:5 أُصُولِهَا ء ص ل B002, B001; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B002; 59:6 رِكَابٍ ر ك ب B007; 59:2 قُلُوبِهِمُ ق ل ب B003; 59:20 ٱلْجَنَّةِ ج ن ن B003; 59:23 ٱلْجَبَّارُ ج ب ر B002

## Gece örtüsü ve açılan gün

Surede örtmek anlamı taşıyan birçok kelime vardır. "Küfür" kelimesinin kökü örtmektir: {ar:الستر والتغطية, tr:es-setr ve't-tağtiye, gloss:örtme ve kapama, source:"ك ف ر,B001"}. Bu kökte gece de kâfirdir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfir, gloss:gece, karanlığıyla örttüğü için "kâfir"dir, source:"ك ف ر,B002"}. Onuncu ayetteki bağışlanma duası da aynı örtme alanındadır: {ar:الغفر الستر, tr:el-ğafr es-setr, gloss:ğafr örtmektir, source:"غ ف ر,B001"}. "Cennet" de gecenin karanlığıdır: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyl, gloss:gecenin cenânı, karanlığı ve eşyayı örtmesidir, source:"ج ن ن,B002"}. Nifak da bir örtüdür: {ar:النفاق لأن صاحبه يكتم خلاف ما يظهر, tr:en-nifâk, gloss:nifak, sahibinin gösterdiğinin tersini gizlemesidir, source:"ن ف ق,B004"}. On dördüncü ayetteki "ardından" kelimesi de saklamayı anlatır: {ar:التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره, tr:et-tevriye es-setr, gloss:tevriye örtmedir; haberi gizleyip başkasını gösterdiğinde "verraytu" dersin, source:"و ر ي,B005"}. Bu yüzden münafıkların duvar arkasında savaşması ile sözlerinin arkasına gizlenmesi aynı kelimeyle işitilir. Tek fark, bir örtünün kurtarması, ötekinin boğmasıdır. Onuncu ayette istenen bağış örtüsü, kişiyi koruyan bir örtüdür. Küfür ve nifak örtüsü ise onu karanlıkta bırakır. On yedinci ayetteki "zalimler" kelimesi karanlığın kendisidir: {ar:الظلمة خلاف النور, tr:ez-zulme hılâfu'n-nûr, gloss:zulmet nurun karşıtıdır, source:"ظ ل م,B001"}. Ayette geçen "ateş" kelimesi ise ışıkla aynı yoldan adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan adlandırılmıştır, source:"ن و ر,B002"}. Ama ateş burada aydınlatmaz, yakar. Münafıklar da bir ateş yakar ama Allah ışıklarını götürür ve onları {ar:فِى ظُلُمَٰتٍ لَّا يُبْصِرُونَ, tr:fî zulumâtin lâ yubsırûn, gloss:göremedikleri karanlıklarda, source:2:17} bırakır. Kıyamette münafıklar müminlerin ışığından almak ister, onlara {ar:ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًا, tr:irci'û verâekum fe'ltemisû nûrâ, gloss:arkanıza dönün de bir ışık arayın, source:57:13} denir. Hemen ardından iki tarafı birbirinden ayıran bir sur çekilir {source:57:13}. Bu ayette surun ardı, ışık ve ayrılık, bu surenin kale, "ardında" ve karanlık kelimeleri bir arada bulunur.

Örtünün karşısında sabah açılır. Yirmi birinci ayetteki "parça parça olmuş" kelimesinin ailesinde sabah da vardır: {ar:الصديع الصبح, tr:es-sadî' es-subh, gloss:sadî' sabahtır, source:"ص د ع,B006"}. Dokuzuncu ayetteki "nefisler" kelimesi de sabahın nefes almasıdır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subh, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Kur'an aynı ifadeyi yemin olarak kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. On sekizinci ayetteki "yarın" kelimesi de seher vaktidir: {ar:الغدوة ما بين صلاة الغداة وطلوع الشمس, tr:el-ğudve, gloss:ğudve, sabah namazı ile güneşin doğuşu arasıdır, source:"غ د و,B001"}. Üçüncü ayetteki "sürgün" (celâ) kelimesi de açığa çıkıp görünür olmaktır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey' ve burûzuh, gloss:bir şeyin açılıp ortaya çıkması, source:"ج ل و,B001"}. Bu kelimenin bir dalı da gündüzün beyazlığıdır {source:"ج ل و,B007"}. Kur'an bu fiili gündüz için kullanır: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Sürgün edilenler kalelerinden çıkarılıp açık alana konur. Gece onları örtüyordu, şimdi her şey gün ışığına çıkar. Yirmi ikinci ayet bu iki yarıyı Allah'ın bilgisinde birleştirir: {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ, tr:'âlimu'l-ğaybi ve'ş-şehâde, gloss:görünmeyeni ve görüneni bilen, source:59:22}. "Gayb" kelimesinin kökü gözlerden gizlenmektir, güneşin batmasına da bu kökle "gâbet" denir {source:"غ ي ب,B001"}. "Şehâdet" ise oradan bakıp görmektir {source:"ش ه د,B001"}. Yirmi birinci ayetteki "hâşi'" kelimesi de batmaya yaklaşan yıldızlar için kullanılır: {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşa'ati'l-kevâkib, gloss:yıldızlar batmaya yaklaşınca "haşaat" denir, source:"خ ش ع,B003"}. Böylece batan yıldızla doğan sabah aynı ayette yan yana durur. Gece ile gündüzde gizlenen ile açıkta yürüyenin Allah katında eşit olduğu da söylenir {source:13:10}.

Kaynaklar: 59:2 كَفَرُوا ك ف ر B001, B002; 59:10 ٱغْفِرْ غ ف ر B001; 59:20 ٱلْجَنَّةِ ج ن ن B002; 59:11 نَافَقُوا ن ف ق B004; 59:14 وَرَآءِ و ر ي B005; 59:17 ٱلظَّٰلِمِينَ ظ ل م B001; 59:3 ٱلنَّارِ ن و ر B002; 59:21 مُّتَصَدِّعًا ص د ع B006; 59:9 أَنفُسِهِمْ ن ف س B009; 59:18 لِغَدٍ غ د و B001; 59:3 ٱلْجَلَآءَ ج ل و B001, B007; 59:22 ٱلْغَيْبِ غ ي ب B001; 59:22 ٱلشَّهَٰدَةِ ش ه د B001; 59:21 خَٰشِعًا خ ش ع B003

## Göğse atılan

Sure, göğüslere ve kalplere sürekli bir şey yerleştirir. İkinci ayette korku kalplere atılır. Atmak fiili okla ve taşla atmaktır {source:"ق ذ ف,B001"}. Atılan korku da havuzu dolduran bir şeydir: {ar:رعبت الحوض إذا ملأته, tr:ra'abtu'l-havd, gloss:havuzu doldurdum, source:"ر ع ب,B002"}. Yani korku kalbe bir taş gibi atılır ve suyun havuzu doldurduğu gibi onu doldurur. Kur'an bunu başka bir kitap ehli topluluk için aynı sözlerle anlatır {source:33:26}. Bedir'de de {ar:سَأُلْقِى فِى قُلُوبِ ٱلَّذِينَ كَفَرُوا۟ ٱلرُّعْبَ, tr:se-ulkî fî kulûbi'llezîne keferu'r-ru'b, gloss:inkâr edenlerin kalplerine korku salacağım, source:8:12} denir. Altıncı ayetteki "koşturmak" fiili de çarpan bir kalbi anlatır: {ar:قلب واجف, tr:kalbun vâcif, gloss:çarpan kalp, source:"و ج ف,B002"}. Kur'an'da da {ar:قُلُوبٌ يَوْمَئِذٍ وَاجِفَةٌ, tr:kulûbun yevmeizin vâcife, gloss:o gün kalpler çarpar, source:79:8} diye geçer. Müminler at koşturmamıştır, ama kalpleri çarpan başkalarıdır.

Dokuzuncu ayet ise boş bir göğüs çizer: Ensar göğüslerinde, verilen şeye karşı bir "hâce" bulmaz. Bu kelime bir ifadede göğüsle birlikte geçer ve şüphe anlamı da taşır: {ar:ما في صدري به حوجاء ولا لوجاء ولا شك ولا مرية بمعنى واحد, tr:mâ fî sadrî bihî havcâ' ve lâ levcâ', gloss:göğsümde bu konuda ne bir ihtiyaç ne bir şüphe var, source:"ح و ج,B002"}. Kökün bir dalı da bir tür dikendir {source:"ح و ج,B003"}. Böylece Ensar'ın göğsü, batan bir dikenden de kıskançlıktan da boştur. Onuncu ayetteki "ğıll" ise göğse çakılan bir şeydir: {ar:غللت الشيء في الشيء إذا أثبته فيه كأنه غرزته, tr:ğalaltu'ş-şey'e fi'ş-şey', gloss:bir şeyi başka bir şeye saplayıp sabitledim, source:"غ ل ل,B001"}. Kin de göğüste böyle işler: {ar:الغل وهو الضغن ينغل في الصدر, tr:el-ğıll ed-dığn yenğallu fi's-sadr, gloss:ğıll, göğse sızan kindir, source:"غ ل ل,B005"}. Sonradan gelenler bu çivinin kalplerine girmemesi için dua eder. Cennet ehlinin göğsünden de bu çivi sökülür: {ar:وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ إِخْوَٰنًا, tr:ve neza'nâ mâ fî sudûrihim min ğıllin ihvânâ, gloss:göğüslerindeki kini söküp çıkardık, kardeşler olarak, source:15:47}. Burada "kin" ve "kardeşler" yan yana gelir, tıpkı onuncu ayette olduğu gibi. On üçüncü ayet münafıklara döner: {ar:لَأَنتُمْ أَشَدُّ رَهْبَةً فِى صُدُورِهِم مِّنَ ٱللَّهِ, tr:le-entum eşeddu rahbeten fî sudûrihim mina'llâh, gloss:onların göğüslerinde siz Allah'tan daha korkutucusunuz, source:59:13}. "Rehbe" kelimesinin bir dalı göğsün kemiğidir: {ar:الرهابة عظم الصدر الذي تقع عليه القلادة, tr:er-ruhâbe, gloss:ruhâbe, gerdanlığın üzerine düştüğü göğüs kemiğidir, source:"ر ه ب,B007"}. Asıl anlamı ise sakınma ve titremeyle karışık korkudur {source:"ر ه ب,B001"}. Bu korku göğsün tam ortasında oturur. Musa'ya da {ar:وَٱضْمُمْ إِلَيْكَ جَنَاحَكَ مِنَ ٱلرَّهْبِ, tr:va'dmum ileyke cenâhake mine'r-rahb, gloss:korkudan kurtulmak için kolunu kendine çek, source:28:32} denir. Orada kol göğse bastırılarak korku yatıştırılır. On dördüncü ayette kalpler dağınıktır. Görülmesi gereken körlük de gözlerde değil, göğüslerdeki kalplerdedir: {ar:وَلَٰكِن تَعْمَى ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ, tr:ve lâkin ta'ma'l-kulûbu'lletî fi's-sudûr, gloss:fakat göğüslerdeki kalpler kör olur, source:22:46}. Münafıklar ağızlarıyla kalplerinde olmayanı söyler {source:3:167}. Müminlerin göğüslerine ise şifa verilir {source:9:14}. Yedinci ayetteki "yoksullar" kelimesi de kökünde bu çalkantının tersini taşır: {ar:خلاف الاضطراب والحركة, tr:hılâfu'l-ıdtırâbi ve'l-hareke, gloss:çalkantı ve hareketin karşıtı, source:"س ك ن,B001"}. Bu kökten gelen "sekîne" de müminlerin kalbine indirilir {source:"س ك ن,B005"}.

Kaynaklar: 59:2 وَقَذَفَ ق ذ ف B001; 59:2 ٱلرُّعْبَ ر ع ب B002; 59:6 أَوْجَفْتُمْ و ج ف B002; 59:9 حَاجَةً ح و ج B002, B003; 59:10 غِلًّا غ ل ل B001, B005; 59:13 رَهْبَةً ر ه ب B007, B001; 59:7 ٱلْمَسَٰكِينِ س ك ن B001, B005

## Ön ve arka: topuk, iz ve el

On ikinci ayet münafıkların yardımının sonunu bir dönüş hareketiyle anlatır: {ar:وَلَئِن نَّصَرُوهُمْ لَيُوَلُّنَّ ٱلْأَدْبَٰرَ ثُمَّ لَا يُنصَرُونَ, tr:ve le-in nasarûhum le-yuvellunne'l-edbâra summe lâ yunsarûn, gloss:yardım etseler bile mutlaka arkalarını dönüp kaçarlar, sonra kendilerine de yardım edilmez, source:59:12}. "Arka" kelimesi önün karşıtıdır {source:"د ب ر,B001"}. Kaçmak da arka dönmektir {source:"و ل ي,B007"}. Dördüncü ve yedinci ayetlerdeki "ikâb" (ceza) ile on yedinci ayetteki "âkıbet" (son) kelimeleri topuk köküne bağlıdır: {ar:العقب مؤخر القدم, tr:el-'akib mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. Ceza da, suçun ardından en son geldiği için bu adla anılır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet 'ukûbeten, gloss:suçun ardından ikinci ve son geldiği için ukûbet denildi, source:"ع ق ب,B007"}. Arkasını dönen kişiye dönüp bakmamak da bu kökle ifade edilir: {ar:ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر, tr:vellâ mudbiren ve lem yu'akkıb, gloss:arkasını döndü ve geri dönüp bakmadı, source:"ع ق ب,B003"}. Sırtını dönüp kaçanın topuğunun dibinde ise ceza yürür. On altıncı ve on yedinci ayetler, Şeytan'ın insanı inkâra çağırıp sonra ondan uzaklaşmasını anlatır. Kur'an bu sahneyi Bedir'de bir dönüş hareketiyle de gösterir: {ar:نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌ مِّنكُمْ إِنِّىٓ أَرَىٰ مَا لَا تَرَوْنَ إِنِّىٓ أَخَافُ ٱللَّهَ ۚ وَٱللَّهُ شَدِيدُ ٱلْعِقَابِ, tr:nekesa 'alâ 'akibeyhi ve kâle innî berî'un minkum innî erâ mâ lâ teravne innî ehâfu'llâh, va'llâhu şedîdu'l-'ikâb, gloss:topukları üzerinde geri döndü ve "ben sizden uzağım, sizin görmediğinizi görüyorum, ben Allah'tan korkarım" dedi; Allah'ın cezası çetindir, source:8:48}. On altıncı ayetteki sözler ile dördüncü ayetin son sözleri bu ayette yan yana durur. Şeytan'ın uzaklaşması, topukları üzerinde geri dönmektir. İnsana karşı tavrı da {ar:وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًا, tr:ve kâne'ş-şeytânu li'l-insâni hazûlâ, gloss:şeytan insanı yüzüstü bırakandır, source:25:29} diye özetlenir. Arkasını dönüp kaçanın akıbeti başka bir ayette de aynen anlatılır {source:3:111}. Müminlerden de arkalarını dönmeyeceklerine dair ahit alınmıştır {source:33:15}.

Müminler ise bir yolda ardı ardına yürür. Onuncu ayetteki {ar:وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ, tr:vellezîne câû min ba'dihim, gloss:onlardan sonra gelenler, source:59:10} ifadesindeki "sonra" kelimesi topuk izine bağlanır: {ar:وما خلف بعقبه فهو من بعده, tr:ve mâ halefe bi-'akibihî fe-huve min ba'dih, gloss:topuğunun arkasında kalan, ondan sonradır, source:"ب ع د,B002"}. Onlar {ar:سَبَقُونَا بِٱلْإِيمَٰنِ, tr:sebekûnâ bi'l-îmân, gloss:bizden önce imana koştular, source:59:10} diye öncekileri anar. "Sebk" yolda öne geçmektir {source:"س ب ق,B001"}. Dokuzuncu ayetteki "îsâr" (tercih etmek) da iz sürmenin köküdür: {ar:الأثر الاستقفاء والاتباع وذهبت في إثره, tr:el-eser el-istikfâ' ve'l-ittibâ', gloss:eser, peşinden gitmek ve izine uymaktır, source:"ء ث ر,B004"}. Bu sırayı Kur'an da adlarıyla verir: {ar:وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم, tr:ve's-sâbikûne'l-evvelûne mine'l-muhâcirîne ve'l-ensâri ve'llezîne'ttebe'ûhum, gloss:muhacirlerden ve ensardan ilk öncüler ve onlara uyanlar, source:9:100}. Böylece münafıklar düşmana arkalarını döner, müminler ise öndekilerin izinden yürür. On sekizinci ayet bu düzende bakışı öne çevirir: {ar:وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ, tr:ve'l-tenzur nefsun mâ kaddemet li-ğad, gloss:herkes yarına ne gönderdiğine baksın, source:59:18}. "Önden göndermek" fiili önün ve arkanın kelimesidir: {ar:قدام خلاف وراء والقدم ضد الأخر, tr:kuddâm hılâfu verâ', gloss:ön, arkanın karşıtıdır, source:"ق د م,B004"}. Bu fiil on dördüncü ayetteki "ardından" ve üçüncü ayetteki "ahiret" kelimeleriyle bir karşıtlık kurar. "Ahiret" en son gelendir {source:"ء خ ر,B001"}. "Ardından" ise hem arkayı hem önü anlatabilir {source:"و ر ي,B006"}. Tedbir de akıbete bakmaktır: {ar:التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته, tr:et-tedbîr, gloss:tedbir, bir işin akıbetinin nereye varacağına bakmaktır, source:"د ب ر,B006"}. Bu ifadede on ikinci ayetin "arka" kökü, on yedinci ayetin "akıbet"i ve on sekizinci ayetin "bakmak" fiili birleşir. Kim akıbetine bakarsa, topuğunun ardındaki cezadan kurtulur. Kur'an bu bakışı başka yerlerde de anlatır: {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:'alimet nefsun mâ kaddemet ve ehharat, gloss:herkes önden ne gönderdiğini, geride ne bıraktığını bilir, source:82:5}. Pişman olan da {ar:يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önden bir şey gönderseydim, source:89:24} der.

El bu iki ayeti birbirine bağlar. İkinci ayette evler "kendi elleriyle" yıkılır. El, bir deyimde kişinin kendi işlediğinin sahibi olmasıdır: {ar:هذا ما قدمت يداك أي جنيته أنت, tr:hâzâ mâ kaddemet yedâk, gloss:bu senin ellerinin önden gönderdiğidir, yani bunu sen işledin, source:"ي د ي,B009"}. Bu ifadede ikinci ayetin "eller"i ile on sekizinci ayetin "önden gönderdi" fiili birleşir. Kur'an da {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâh, gloss:kişinin ellerinin önden gönderdiğine baktığı gün, source:78:40} der. Burada bakmak, önden göndermek ve el bir aradadır. On sekizinci ayetin çağrısının tersi de vardır: {ar:وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ, tr:ve nesiye mâ kaddemet yedâh, gloss:ellerinin önden gönderdiğini unuttu, source:18:57}. On dokuzuncu ayetteki unutanlar da aynı yere düşer. Münafıklar ise ellerini sıkar ve unutur: {ar:وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ, tr:ve yakbıdûne eydiyehum, nesu'llâhe fe-nesiyehum, inne'l-munâfıkîne humu'l-fâsikûn, gloss:ellerini sıkı tutarlar; Allah'ı unuttular, O da onları unuttu; münafıklar fâsıkların ta kendileridir, source:9:67}. Bu ayet, sure içinde dağınık duran unutma, fısk ve sıkı tutulan el kavramlarını tek cümlede toplar. Yedinci ayetteki "dûle" de elden ele geçmektir {source:"ي د ي,B007"}. El ayrıca nimet ve iyiliktir {source:"ي د ي,B003"}. Dokuzuncu ayette Ensar elindekini açar, sıkmaz. Kur'an eli boyna bağlamayı da yasaklar {source:17:29}.

Kaynaklar: 59:12 لَيُوَلُّنَّ و ل ي B007; 59:12 ٱلْأَدْبَٰرَ د ب ر B001, B006; 59:4/7 ٱلْعِقَابِ ع ق ب B002, B003, B007; 59:17 عَٰقِبَتَهُمَآ ع ق ب B002; 59:10 بَعْدِهِمْ ب ع د B002; 59:10 سَبَقُونَا س ب ق B001; 59:9 يُؤْثِرُونَ ء ث ر B004; 59:18 قَدَّمَتْ ق د م B004; 59:3 ٱلْءَاخِرَةِ ء خ ر B001; 59:14 وَرَآءِ و ر ي B006; 59:2 بِأَيْدِيهِمْ ي د ي B009; 59:7 دُولَةً ي د ي B007; 59:9 (Ensar'ın verişi) ي د ي B003

## Yurttan çıkış, ıssızlaşan yurt, hazırlanan konak

Sure iki topluluğun evinden çıkışını anlatır. Birincisi, ikinci ayetteki çıkarılmadır: {ar:أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ, tr:ahrace'llezîne keferû min ehli'l-kitâbi min diyârihim li-evveli'l-haşr, gloss:kitap ehlinden inkâr edenleri ilk sürgünde yurtlarından çıkaran, source:59:2}. "Haşr" kelimesi burada bir topluluğu yerinden çıkarıp sürmek anlamını taşır: {ar:إخراج الجماعة عن مقرهم وإزعاجهم عنه, tr:ihrâcu'l-cemâ'a 'an makarrihim ve iz'âcuhum 'anh, gloss:topluluğu yurdundan çıkarıp oradan sökmek, source:"ح ش ر,B001"}. Bu ifadede, aynı ayetteki "çıkardı" fiili ile "haşr" kelimesi birleşir. Üçüncü ayetteki "celâ" (sürgün) da insanları evlerinden açık alana çıkarmaktır: {ar:أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها, tr:eclaytu'l-kavme 'an menâzilihim, gloss:topluluğu evlerinden çıkardım, yani onları açığa çıkardım, source:"ج ل و,B004"}. İkincisi, sekizinci ayetteki muhacirlerin çıkışıdır: {ar:ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ, tr:ellezîne uhricû min diyârihim ve emvâlihim, gloss:yurtlarından ve mallarından çıkarılanlar, source:59:8}. Hicret evden eve göçmektir: {ar:هاجر القوم من دار إلى دار تركوا الأولى للثانية, tr:hâcera'l-kavmu min dârin ilâ dâr, gloss:topluluk bir yurttan bir yurda göçtü, ilkini ikincisi için bıraktı, source:"ه ج ر,B002"}. Böylece aynı fiil iki çıkışı da anlatır, ama ikisinin sonu farklıdır. Birinciler, yurtlarını kendi elleriyle yıkıp gider. İkinciler ise kendilerine hazırlanmış bir yurda varır: {ar:وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ, tr:ve'llezîne tebevve'u'd-dâra ve'l-îmâne min kablihim, gloss:onlardan önce o yurdu ve imanı yerleşim yeri edinenler, source:59:9}. "Tebevvu'" fiili bir yeri konak edinmektir: {ar:المباءة منزل القوم في كل موضع وتبوأت منزلا وبوأت للرجل منزلا, tr:el-mebâ'e menzilu'l-kavm, gloss:mebâe, topluluğun konağıdır; konak edindim ve adama konak hazırladım, source:"ب و ء,B001"}. Ayetteki dikkat çekici nokta, imanın da yurt gibi konak edinilmesidir. Kur'an hicret edenlere de böyle bir konak vaat eder: {ar:لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةً, tr:le-nubevvi'ennehum fi'd-dunyâ hasene, gloss:onları dünyada güzel bir yere yerleştireceğiz, source:16:41}. Haksız yere yurtlarından çıkarılanlar için ise {ar:وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ, tr:ve le-yensuranna'llâhu men yensuruh, inna'llâhe le-kaviyyun 'azîz, gloss:Allah kendisine yardım edene mutlaka yardım eder; Allah güçlüdür, azîzdir, source:22:40} denir. Bu ayette, sekizinci ayetteki "yardım ederler" ile birinci ayetteki "Azîz" bir araya gelir. Barınak verip yardım edenler de muhacirlerle birlikte anılır {source:8:72}.

Yolun kendisi de suredeki kelimelerde vardır. Yedinci ayetteki {ar:وَٱبْنِ ٱلسَّبِيلِ, tr:ve'bni's-sebîl, gloss:ve yolda kalmış yolcu, source:59:7} ifadesi, yolculukta yolu kesilmiş kişiyi anlatır: {ar:ابن السبيل المسافر الذي انقطع به, tr:ibnu's-sebîl el-musâfir ellezi'nkutı'a bih, gloss:ibnu's-sebîl, yolu kesilmiş yolcudur, source:"س ب ل,B002"}. Beşinci ayetteki "kesmek" fiili bu yolculuğa iki ifadeyle bağlanır. Biri, bineği ölüp azığı biten yolcudur {source:"ق ط ع,B006"}. Öbürü yolcuları soyan eşkıyadır: {ar:قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق, tr:kuttâ'u't-turuk, gloss:yolcuların önünü kesip yolu onlara kapatan yol kesiciler, source:"ق ط ع,B023"}. İkinci ayetteki "ibret alın" fiili de yoldan geçmektir: {ar:رجل عابر سبيل أي مار, tr:raculun 'âbiru sebîl, gloss:yoldan geçen adam, source:"ع ب ر,B001"}. Uzak yolu anlatan kelimeler de surede vardır: dördüncü ayetteki "ayrılık" kelimesinin ailesinde uzun yolculuk {source:"ش ق ق,B005"}, on altıncı ayetteki "Şeytan" kelimesinin ailesinde de evin uzaklığı vardır: {ar:شطنت الدار شطونا إذا بعدت, tr:şatanati'd-dâr, gloss:yurt uzaklaşınca "şatanat" denir, source:"ش ط ن,B001"}.

Geride kalan yurt ise ıssızlaşır. On birinci ayette münafıklar {ar:وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًا, tr:ve lâ nutî'u fîkum ehaden ebedâ, gloss:sizin hakkınızda hiç kimseye asla boyun eğmeyiz, source:59:11} der. "Ebed" kelimesinin ailesinde, sahipleri gidip yaban hayvanlarına kalan ev vardır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:te'ebbede'l-menzil, gloss:ev ıssızlaştı ve yaban hayvanları ona alıştı, source:"ء ب د,B003"}. "Kimse" kelimesi de evle birlikte geçer: {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"}. Yurt kelimesi de yalnız bu tür olumsuz cümlelerde "kimse" anlamı taşır {source:"د و ر,B008"}. Yani "asla" diye verilen söz, yanında boşalmış bir evin sesini taşır. Yedinci ayetteki "zenginler" kelimesi de bir yerde oturmak anlamı taşır: {ar:غني القوم في دارهم أقاموا ومغانيهم منازلهم, tr:ğaniye'l-kavmu fî dârihim, gloss:topluluk yurdunda oturdu; meğânî onların konaklarıdır, source:"غ ن ي,B004"}. Aynı kökte bir deyim de vardır: {ar:كأن لم يغن بالأمس أي كأن لم يكن, tr:ke-en lem yağne bi'l-ems, gloss:sanki dün orada hiç oturmamış, yani hiç yokmuş gibi, source:"غ ن ي,B004"}. Kur'an bu deyimi yok edilen kavimler için kullanır: {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlar gibi, source:11:68}. Bahçe sahnesinde de aynı ifade vardır {source:10:24}. On yedinci ayetteki "ebedî kalıcılar" kelimesi, ailesinde harabeden geriye kalan ocak taşlarını da anlatır: {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid, gloss:uzun süre durdukları için ocak taşlarına havâlid denir, source:"خ ل د,B001"}. Kalıcılık burada artık yaşanan bir ev değil, yıkıntıda kalan taştır. On dokuzuncu ayetteki "unuttular" fiili de göçenlerin ardında bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sakata min menâzili'l-murtahılîn, gloss:nisy, göçenlerin konaklarından düşen değersiz eşyadır, source:"ن س ي,B003"}. Meryem de aynı kelimeyle {ar:وَكُنتُ نَسْيًا مَّنسِيًّا, tr:ve kuntu nesyen mensiyyâ, gloss:unutulup gitmiş bir şey olsaydım, source:19:23} der. Allah'ı unutanlar, kendilerini de unutturulmuş olarak terk edilmiş bir yurdun döküntüsü gibi bulur. İkinci ayetteki "ev" kelimesi de kabir anlamına gelir {source:"ب ي ت,B007"}. Kur'an boşalmış evleri böyle gösterir: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş evleri, source:27:52}. Az kalsın hiç oturulmamış meskenler de vardır {source:28:58}. Kuşatılmış başka bir topluluğun yurdu da müminlere miras kalmıştır {source:33:27}.

Kaynaklar: 59:2/8 أَخْرَجَ / أُخْرِجُوا خ ر ج B001; 59:2 ٱلْحَشْرِ ح ش ر B001; 59:3 ٱلْجَلَآءَ ج ل و B004; 59:8/9 ٱلْمُهَٰجِرِينَ / هَاجَرَ ه ج ر B002; 59:9 تَبَوَّءُو ب و ء B001; 59:7 ٱبْنِ ٱلسَّبِيلِ س ب ل B002; 59:5 قَطَعْتُم ق ط ع B006, B023; 59:2 فَٱعْتَبِرُوا ع ب ر B001; 59:4 شَآقُّوا ش ق ق B005; 59:16 ٱلشَّيْطَٰنِ ش ط ن B001; 59:11 أَبَدًا ء ب د B003; 59:11 أَحَدًا ء ح د B002; 59:2 دِيَٰرِهِمْ د و ر B008; 59:7 ٱلْأَغْنِيَآءِ غ ن ي B004; 59:17 خَٰلِدَيْنِ خ ل د B001; 59:19 نَسُوا ن س ي B003; 59:2 بُيُوتَهُم ب ي ت B007

## Misafir sofrası

Dokuzuncu ayetteki karşılama bir misafir ağırlama sahnesi olarak da işitilir. Yedinci ayetteki "kasabalar" kelimesi, ailesinde misafirin etrafında toplandığı büyük tası anlatır: {ar:المقراة الجفنة سميت لاجتماع الضيف عليها, tr:el-mikrâ el-cefne, gloss:mikrâ, misafirlerin etrafında toplandığı için bu adı alan büyük tastır, source:"ق ر ي,B003"}. Misafire ikram da aynı köktendir: {ar:القرى الإحسان إلى الضيف, tr:el-kırâ el-ihsân ile'd-dayf, gloss:kırâ misafire ikramdır, source:"ق ر ي,B003"}. Yirmi birinci ayetteki "indirmek" fiili de konuğa hazırlanan yemeği anlatır: {ar:النزل ما يهيأ للنزيل, tr:en-nuzul mâ yuheyye'u li'n-nezîl, gloss:nuzul, konuk için hazırlanan şeydir, source:"ن ز ل,B005"}. Kur'an'ın indirilişi böylece hem yağmurun hem de konuğa sunulan sofranın sesini taşır. "Ehl" kelimesi de karşılama sözünün içindedir: {ar:مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش, tr:merhaben ve ehlen, gloss:genişliğe ve ailene geldin, ısın, yabancılık çekme, source:"ء ه ل,B005"}. Dokuzuncu ayet bu karşılamayı açık bir dille söyler: {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ, tr:ve yu'sirûne 'alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri darlık içinde olsalar bile onları kendilerine tercih ederler, source:59:9}. "Esîr" kelimesi, kişinin lütfuyla öne çıkardığı değerli insandır: {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-esîr el-kerîm 'aleyk, gloss:esîr, lütfun ve ikramınla öne geçirdiğin değerli kişidir, source:"ء ث ر,B005"}. Bu ifadedeki "fazl" (lütuf) kelimesi sekizinci ayette de geçer. Muhacirler Allah'tan lütuf ararken, Ensar onlara kendi lütfundan verir. "Fazl" da birine kendi fazlasından vermektir {source:"ف ض ل,B003"}. Yedinci ayetteki "yoksullar" kelimesinin ailesinde ise insanın yanında ısındığı ateş vardır {source:"س ك ن,B004"}. On sekizinci ayetteki "yarın" kelimesi de sabah yemeğidir {source:"غ د و,B004"}. İbrahim'in misafir ağırlaması bu sahnenin Kur'an'daki örneğidir: {ar:فَجَآءَ بِعِجْلٍ سَمِينٍ, tr:fe-câe bi-'iclin semîn, gloss:semiz bir buzağı getirdi, source:51:26}, {ar:فَقَرَّبَهُۥٓ إِلَيْهِمْ, tr:fe-karrabehû ileyhim, gloss:onu önlerine koydu, source:51:27}. Dokuzuncu ayetteki tercih de sevilen şeyden yedirmektir: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا, tr:ve yut'ımûne't-ta'âme 'alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, sevdikleri halde yoksula, yetime ve esire yedirirler, source:76:8}. Orada da karşılık beklenmez {source:76:9}. On beşinci ayette ise tatma tersine döner. Tatmak önce yiyeceği tatmaktır {source:"ذ و ق,B001"}. Önceki topluluk ise sofrada değil, kendi işlerinin vebalinde tat alır.

Kaynaklar: 59:7 ٱلْقُرَىٰ ق ر ي B003; 59:21 أَنزَلْنَا ن ز ل B005; 59:2/7 أَهْلِ ء ه ل B005; 59:9 يُؤْثِرُونَ ء ث ر B005; 59:8 فَضْلًا ف ض ل B003; 59:7 ٱلْمَسَٰكِينِ س ك ن B004; 59:18 لِغَدٍ غ د و B004; 59:15 ذَاقُوا ذ و ق B001

## Görmekten geçmeye

İkinci ayet, kuşatma sahnesini bir çağrıyla bitirir: {ar:فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:fa'teberû yâ uli'l-ebsâr, gloss:ibret alın ey basiret sahipleri, source:59:2}. "İ'tibâr" kelimesi bir geçiştir: {ar:الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد, tr:el-i'tibâr ve'l-'ibra, gloss:i'tibâr ve ibret, görülenin bilgisinden görülmeyene ulaştıran durumdur, source:"ع ب ر,B004"}. Rüyayı yorumlayan da dışından içine geçer {source:"ع ب ر,B002"}. Basiret ise kalpte delip geçen bir görmedir {source:"ب ص ر,B002"}. Beşinci ayetteki "kesmek" fiili de nehri geçmek anlamında kullanılır: {ar:قطعت النهر قطوعا عبرته, tr:kata'tu'n-nehra kutû'an, gloss:nehri kat ettim, yani geçtim, source:"ق ط ع,B003"}. Bu ifadede "kesmek" ile "geçmek" birleşir. İbret, gözün gördüğü yıkılmış evlerden, görülmeyen sebebe geçmektir. Kur'an aynı çağrıyı Bedir'deki iki birlik için de yapar: {ar:يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ... إِنَّ فِى ذَٰلِكَ لَعِبْرَةً لِّأُو۟لِى ٱلْأَبْصَٰرِ, tr:yeravnehum misleyhim ra'ye'l-'ayn ... inne fî zâlike le-'ibraten li-uli'l-ebsâr, gloss:onları göz görüşüyle kendilerinin iki katı görüyorlardı; bunda basiret sahipleri için elbette bir ibret vardır, source:3:13}. Gece ile gündüzün dönüşümü için de aynı sözler kullanılır {source:24:44}. Üçüncü ayetteki "sürgün" (celâ) kelimesi gözü de açar: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ el-ismid, gloss:celâ sürmedir, çünkü gözü parlatır, source:"ج ل و,B002"}. Sürgün, ona bakanların gözüne çekilen bir sürme gibidir.

Görmenin karşısında sure tahmini koyar. Kuşatılanlar kalelerinin kendilerini koruyacağını "zannetmiştir" ve gelişi "hesaba katmamışlardır". Zan, kesin olmayan bilgidir {source:"ظ ن ن,B003"}. Bir dalı da içinde su olup olmadığı bilinmeyen kuyudur: {ar:الظنون البئر لا يدرى أفيها ماء أم لا, tr:ez-zenûn el-bi'r, gloss:zenûn, içinde su olup olmadığı bilinmeyen kuyudur, source:"ظ ن ن,B006"}. On dördüncü ayetteki "sanırsın" fiili de zan demektir {source:"ح س ب,B002"}. Altıncı ayetteki "atlar" kelimesinin ailesinde de aynada görülen gölge vardır: {ar:الخيال كل شيء تراه كالظل وخيالك في المرآة, tr:el-hayâl kullu şey'in terâhu ke'z-zıll, gloss:hayâl, gölge gibi gördüğün her şey ve aynadaki görüntündür, source:"خ ي ل,B001"}. Kuşatılanların kaleleri, münafıkların vaatleri ve toplu görünen kalabalık, hepsi bu tür gölgelerdir. Bu yüzden sure iki kez "görmedin mi" ve "görürdün" diye sorar: on birinci ayette münafıklara, yirmi birinci ayette dağa. On sekizinci ayetteki "baksın" fiili de gözle ve basiretle bir şeyi evirip çevirmektir {source:"ن ظ ر,B001"}. Ayetin sonundaki "haberdar" ismi de dışın karşısında içi anlatır: {ar:المخبر خلاف المنظر, tr:el-mahber hılâfu'l-manzar, gloss:iç yüz, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. İnsan kendi görünüşüne bakar, Allah ise iç yüzünü bilir. On üçüncü ve on dördüncü ayetlerdeki "topluluk" kelimesinin ailesinde de, göz bebeği sağlam olduğu halde görmeyen göz vardır: {ar:عين قائمة ذهب بصرها والحدقة صحيحة, tr:'aynun kâime, gloss:göz bebeği sağlam olduğu halde görme gücü gitmiş göz, source:"ق و م,B021"}. Bu iki ayet o topluluğu {ar:قَوْمٌ لَّا يَفْقَهُونَ, tr:kavmun lâ yefkahûn, gloss:anlamayan bir topluluk, source:59:13} ve akıl etmeyen bir topluluk diye anar. Kur'an bu körlüğü açıkça tarif eder: {ar:وَلَهُمْ أَعْيُنٌ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Münafıkların görünüşü de insanı hayran bırakır, ama onlar dayalı kütükler gibidir {source:63:4}. Sekizinci ayetteki fakirlerin durumu ise tersine bir yanılgıdır: bilmeyen kişi onları {ar:يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ, tr:yahsebuhumu'l-câhilu ağniyâ', gloss:bilmeyen onları zengin sanır, source:2:273}. Göz, burada da dışa bakıp içi kaçırır.

Kaynaklar: 59:2 فَٱعْتَبِرُوا ع ب ر B004, B002; 59:2 ٱلْأَبْصَٰرِ ب ص ر B002; 59:5 قَطَعْتُم ق ط ع B003; 59:3 ٱلْجَلَآءَ ج ل و B002; 59:2 ظَنُّوا ظ ن ن B003, B006; 59:14 تَحْسَبُهُمْ ح س ب B002; 59:6 خَيْلٍ خ ي ل B001; 59:18 وَلْتَنظُرْ ن ظ ر B001; 59:18 خَبِيرٌ خ ب ر B001; 59:13/14 قَوْمٌ ق و م B021

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

