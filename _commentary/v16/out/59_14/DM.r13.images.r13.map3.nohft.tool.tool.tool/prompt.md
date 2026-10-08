Focus: 59:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_14/D.r13/context.md =====
# 59:14 — focus

لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًۭى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍۭ ۚ بَأْسُهُم بَيْنَهُمْ شَدِيدٌۭ ۚ تَحْسَبُهُمْ جَمِيعًۭا وَقُلُوبُهُمْ شَتَّىٰ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَا | لَا |  | NEG |
| 2 | يُقَٰتِلُونَكُمْ | قَٰتَلَ | ق ت ل | V;PRON |
| 3 | جَمِيعًا | جَمِيع | ج م ع | N |
| 4 | إِلَّا | إِلَّا |  | RES |
| 5 | فِى | فِى |  | P |
| 6 | قُرًى | قَرْيَة | ق ر ي | N |
| 7 | مُّحَصَّنَةٍ | مُّحَصَّنَة | ح ص ن | ADJ |
| 8 | أَوْ | أَو |  | CONJ |
| 9 | مِن | مِن |  | P |
| 10 | وَرَآءِ | وَرَآء | و ر ي | N |
| 11 | جُدُرٍۭ | جُدُر | ج د ر | N |
| 12 | بَأْسُهُم | بَأْس | ب ء س | N;PRON |
| 13 | بَيْنَهُمْ | بَيْن | ب ي ن | LOC;PRON |
| 14 | شَدِيدٌ | شَدِيد | ش د د | N |
| 15 | تَحْسَبُهُمْ | حَسِبَ | ح س ب | V;PRON |
| 16 | جَمِيعًا | جَمِيع | ج م ع | N |
| 17 | وَقُلُوبُهُمْ | قَلْب | ق ل ب | CIRC;N;PRON |
| 18 | شَتَّىٰ | شَتَّىٰ | ش ت ت | N |
| 19 | ذَٰلِكَ | ذَٰلِك |  | DEM |
| 20 | بِأَنَّهُمْ | أَنّ |  | P;ACC;PRON |
| 21 | قَوْمٌ | قَوْم | ق و م | N |
| 22 | لَّا | لَا |  | NEG |
| 23 | يَعْقِلُونَ | عَقَلُ | ع ق ل | V;PRON |


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
- 59:14 ◀ focus لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًۭى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍۭ ۚ بَأْسُهُم بَيْنَهُمْ شَدِيدٌۭ ۚ تَحْسَبُهُمْ جَمِيعًۭا وَقُلُوبُهُمْ شَتَّىٰ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ
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


===== _commentary/v16/work/59_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ت ل (root_001200) — identity root of يُقَٰتِلُونَكُمْ (w2)

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

## ج م ع (root_000259) — identity root of جَمِيعًا (w3)

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

## ق ر ي (root_001222) — identity root of قُرًى (w6)

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

## ح ص ن (root_000331) — identity root of مُّحَصَّنَةٍ (w7)

- **B001** korunaklı çevre, onu kurma, ona sığınma ve genel olarak sakınma — korunaklı yer; savunmalı yapılar · içine erişilemeyen, iyi korunan · yerin ya da köyün çevresi yapıyla korunur hale geldi · onu korunaklı hale getirdi ve korumaya aldı · korunak edindi, sığındı ve kendini korudu · sağlamlaştırılarak savunmalı yapıya dönüştürülmüş köyler · bedeni koruyan sık dokunmuş zırh · korunaklı yerlerde saklayıp koruduğunuz şeyler
  الحفظ والحياطة والحرز (maqayis); الحصن كل موضع حصين لا يوصل إلى ما في جوفه (ayn); حصنت القرية إذا بنيت حولها وتحصن العدو (sihah); يتجوز به في كل تحرز ومنه درع حصينة ومما تحصنون أي تحرزون (mufradat)
- **B002** yasak cinsel ilişkiden uzak durarak kendini koruma — cinsel davranışta kendini koruyan kadın · yasak cinsel ilişkiden uzak duran kadın · cinsel organını yasak ilişkiden koruyan kadın · kadın yasak cinsel ilişkiden uzak durdu · cinsel organını yasak ilişkiden korudu · kendisini ya da cinsel organını koruyarak yasak ilişkiden uzak duran kadın
  الحصان المرأة المتعففة الحاصنة فرجها (maqayis); امرأة حاصن بينة الحصن والحصانة أي العفافة عن الربية (ayn); أحصنت المرأة عفت وحصنت المرأة أي عفت (sihah); يقال حصان للعفيفة وأحصنت فرجها (mufradat)
- **B003** evlilik veya hukuki engelle kazanılan korunmuş durum — adam evlendi ve evli sayıldı · kocası onu evlilik bağıyla evli konuma getirdi · evlenmiş kadın · evlendirildiklerinde ya da evlendiklerinde · evli oldukları için kendileriyle evlenilmesi yasak kadınlar · saygınlığı, özgürlüğü veya hukuki engel nedeniyle korunan kadın
  كل امرأة متزوجة فهي محصنة وأحصن الرجل فهو محصن (maqayis); امرأة محصنة أحصنها زوجها (ayn); أحصن الرجل إذا تزوج وأحصنها زوجها وقرئ فإذا أحصن أي زوجن (sihah); أحصن أي تزوجن والمحصنات المزوجات أو بمانع من شرفها وحريتها (mufradat)
- **B004** aygır veya erkek at — aygır; erkek at · biniciyi koruyan atlar
  الحصان الفرس الفحل (ayn); سموا كل ذكر من الخيل حصانا (sihah); فرس حصان لكونه حصنا لراكبه (mufradat)

## و ر ي (root_001642) — identity root of وَرَآءِ (w10)

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

## ج د ر (root_000228) — identity root of جُدُرٍۭ (w11)

- **B001** duvar, yükseltilmiş set ve duvarla çevrili yer — duvar; yükseltilmiş yapı · duvarlar; su tutan yükseltilmiş tarla seti · duvarlar · duvarı yükseltti · koyunlar için taşla çevrili ağıl · çevresine duvar yapılmış yer
  الجدار وهو الحائط وجمعه جدر وجدران؛ الجديرة شيء يجعل للغنم كالحظيرة (maqayis)؛ الجدار جمعه جدر؛ الجدير مكان بني حواليه جدار مجدور (ayn)؛ الجدر والجدار الحائط؛ الحظيرة من صخر جديرة (sihah)؛ ما رفع من أعضاد المزرعة لتمسك الماء كالجدار؛ الجدير مكان قد بني حواليه جدار مجدور (tahdhib)؛ الجدار الحائط؛ جدرت الجدار رفعته (mufradat)
- **B002** bir iş için uygun ve yaraşır olma — bir iş için uygun ve yaraşır · uygun ve yaraşır kişiler; bu nitelikteki kadınlar · bir sonucu gerektirir nitelikte olan şey · bunu yapması daha uygun ve yerinde · uygun ve yaraşır olma
  هو جدير بكذا أي حري به؛ ينبغي أن يثبت ويبنى أمره عليه (maqayis)؛ هذا الأمر مجدرة لذلك أي محراة؛ فلان جدير بكذا أي خليق (sihah)؛ فلان جدير لذلك الأمر أي خليق له؛ جدر جدارة؛ أجدر به أن يفعل ذاك (tahdhib)؛ الجدير المنتهى؛ قد جدر بكذا فهو جدير؛ ما أجدره بكذا وأجدر به (mufradat)
- **B003** doğal yapı veya huy — doğal yapı veya huy
  الجديرة الطبيعة
- **B004** yeni çıkmış bitki; bitkinin, yaprağın veya meyvenin belirmesi — yerden veya ağaçtan yükselen bitki · tek bir çıkıntılı bitki veya hurma çiçeği tanesi · yer bitki çıkardı; ağaç yaprak veya meyve verdi · ağaç yapraklandı veya nohut gibi meyve verdi
  الجدر النبات؛ أجدر المكان وجدر إذا ظهر نباته (maqayis)؛ الجدر ضرب من النبات؛ أجدرت الشجرة وأجدرت الأرض (ayn)؛ الجدر أيضا نبت؛ أجدر المكان (sihah)؛ الجدر ضرب من النبات؛ أجدرت الأرض وأجدر الشجر؛ الجدرة الحبة من الطلع؛ أخرج ثمره كأنه الحمص (tahdhib)؛ جدر الشجر إذا خرج ورقه كأنه حمص؛ النبات الناتئ من الأرض جدرا (mufradat)
- **B005** kabarcıklı veya çukurlaştırıcı deri hastalığı, çıban ve ezik şişliği — çiçek hastalığı · çiçek hastalığına yakalandı ve döküntülendi · derisi hastalıktan çukurlaşmış koyun · çıban veya deri altı yumrusu · bedende çıkan yumru veya eşeğin boynundaki ezik şişliği · şişip kabardı
  الجدري معروف؛ شاة جدراء؛ الجدر سلعة تظهر في الجسد؛ الجدر أثر الكدم بعنق الحمار (maqayis)؛ شاة جدراء إذا تقوب جلدها؛ الجدري؛ جدر الرجل فهو مجدر؛ الجدرة خراج وهي السلعة (sihah)؛ الجدري قروح تنفط عن الجلد؛ الجدر انتبار في عنق الحمار؛ جدرت جدرا إذا انتبرت (tahdhib)؛ الجدري والجدرة سلعة تظهر في الجسد؛ شاة جدراء (mufradat)

## ب ء س (root_000079) — identity root of بَأْسُهُم (w12)

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

## ب ي ن (root_000170) — identity root of بَيْنَهُمْ (w13)

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

## ش د د (root_000782) — identity root of شَدِيدٌ (w14)

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

## ح س ب (root_000318) — identity root of تَحْسَبُهُمْ (w15)

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

## ق ل ب (root_001248) — identity root of وَقُلُوبُهُمْ (w17)

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

## ش ت ت (root_000775) — identity root of شَتَّىٰ (w18)

- **B001** dağılma ve dağıtma — dağılmak; dağılma · dağıtmak, dağınık hale getirmek · topluluğum işimi dağıttı · şu şey gönlümü dağıttı · yayılıp dağılmak · dağılıp yayılmak · ayrı kişiler veya dağınık parçalar halinde · dağınıklık ve ayrılık · dağılmış, dağınık · dağınık bir iş veya durum · çeşitli, birbirinden farklı · aynı soydan olmayan insanlar
  أصل يدل على تفرق وتزيل (maqayis)؛ الشت مصدر الشيء الشتيت وهو المتفرق (ayn)؛ شت يشت شتاتا وهو التفرق (jamhara)؛ أمر شت أي متفرق (sihah)؛ يصدر الناس أشتاتا أي متفرقين (tahdhib)؛ الشت تفريق الشعب (mufradat)
- **B002** güzel ve aralıklı diş dizisi [kalıp] — dişleri güzel, düzgün ve aralıklı ağız
  ثغر شتيت مفلج حسن (maqayis)؛ ثغر شتيت مفلج حسن (ayn)؛ ثغر شتيت أي مفلج (sihah)
- **B003** iki şey arasındaki büyük uzaklık ve uyuşmazlık — ne kadar uzak ve farklılar · ikisi birbirinden ne kadar uzak ve farklı · aralarında ne büyük uzaklık ve ayrılık var
  شتان ما هما (maqayis;ayn;sihah;tahdhib;mufradat)؛ شتان ما بينهما (maqayis;sihah;mufradat)؛ تباعد ما بينهما (tahdhib)؛ ارتفاع الالتئام بينهما (mufradat)

## ق و م (root_001273) — identity root of قَوْمٌ (w21)

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

## ع ق ل (root_001036) — identity root of يَعْقِلُونَ (w23)

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

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:14, and ## Buluşmalar) =====
## Kale, zırh ve içeriden açılan gedik

Bu surenin kelimeleri, ayetteki anlamlarının yanında, köklerinin taşıdığı başka sahneleri de duyurur. Bu aile imgeleri kelimenin ayetteki anlamının yerine geçmez, onun yanında işitilir. Aşağıda hep bu sınırla konuşulacak.

İkinci ayet bir kuşatmayı anlatır. Kuşatılanlar, {ar:مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ, tr:mâni'atuhum husûnuhum mina'llâh, gloss:kaleleri onları Allah'tan koruyacak, source:59:2} diye düşünmüşlerdir. Kale burada yalnızca yüksek bir yapı değildir. Kelime, içine ulaşılamayan kapalı yer demektir: {ar:الحصن كل موضع حصين لا يوصل إلى ما في جوفه, tr:el-hısn kullu mevdı'ın hasîn lâ yûsalu ilâ mâ fî cevfih, gloss:hısn, içindekine ulaşılamayan her korunaklı yerdir, source:"ح ص ن,B001"}. "Engelleyen" diye çevrilen fiil de aynı işi görür: araya girer ve içeri girilmesine izin vermez. Bu kelime ailesinde dokunulmazlık ile izzet tek bir ifadede birleşir: {ar:رجل منيع لا يخلص إليه وهو في عز ومنعة, tr:raculun meni' lâ yuhlasu ileyh ve huve fî 'izzin ve men'a, gloss:kendisine ulaşılamayan, izzet ve korunma içindeki adam, source:"م ن ع,B003"}. Sure ise bu izzeti baştan Allah'a verir: birinci ayet {ar:وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ, tr:ve huve'l-'azîzu'l-hakîm, gloss:O, mutlak güçlü, hüküm ve hikmet sahibidir, source:59:1} diye kapanır. "Azîz" kelimesi yenilmeyen, içine el uzatılamayan demektir: {ar:العزيز الممتنع فلا يغلبه شيء, tr:el-'azîzu'l-mümteni' fe-lâ yaglibuhû şey', gloss:azîz, hiçbir şeyin üstün gelemediği korunaklıdır, source:"ع ز ز,B001"}. "Hakîm" de bozulmayı önleyen bir tutmadır: {ar:حكم أصله منع منعا لإصلاح, tr:hakeme aslı men'a men'an li-ıslâh, gloss:hükmün aslı, düzeltmek için engellemektir, source:"ح ك م,B001"}. Böylece kale, yalnızca Allah'a ait olan dokunulmazlığı taş ile taklit eder. Sure bu iki ismi son ayette yine söyleyerek kuşatmayı iki ucundan kapatır.

Kuşatmanın işleyişi aynı ayetin fiillerinde görülür. {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. Burada surlar aşılmaz, saldırı hiç beklenmeyen bir yönden gelir. "Ev" kelimesinin ailesi, düşmana gece baskını yapmayı da anlatır: {ar:البيات والتبييت أن تأتي العدو ليلا, tr:el-beyâtu ve't-tebyît en te'tiye'l-'aduvve leylen, gloss:beyât, düşmana gece gelmektir, source:"ب ي ت,B004"}. Ayetteki "geldi" fiili ile "evler" kelimesi bu ifadede yan yana durur. Atılan şey de mancınık taşı gibidir: {ar:القذاف المنجنيق, tr:el-kazzâf el-mancınîk, gloss:kazzâf mancınıktır, source:"ق ذ ف,B001"}. Ama taş duvara değil kalplere düşer: {ar:وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ, tr:ve kazefe fî kulûbihimu'r-ru'b, gloss:kalplerine korku attı, source:59:2}. Gedik de dışarıdan açılmaz: {ar:يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ, tr:yuhribûne buyûtehum bi-eydîhim, gloss:evlerini kendi elleriyle yıkıyorlardı, source:59:2}. Bu fiilin kökü delmeyi ve gedik açmayı anlatır: {ar:أصل يدل على التثلم والتثقب, tr:asl yedullu 'ale't-tesellumi ve't-tesekkub, gloss:gedik ve delik açılmayı gösteren kök, source:"خ ر ب,B001"}. Yani kale, içine atılan bir korkunun açtırdığı deliklerle kendi içinden çöker. Benzer bir sahnede Allah, tuzak kuranların yapısına temelinden gelir: {ar:فَأَتَى ٱللَّهُ بُنْيَٰنَهُم مِّنَ ٱلْقَوَاعِدِ فَخَرَّ عَلَيْهِمُ ٱلسَّقْفُ, tr:fe-eta'llâhu bunyânehum mine'l-kavâ'idi fe-harra 'aleyhimu's-sakf, gloss:Allah yapılarına temellerinden geldi, tavan üstlerine çöktü, source:16:26}. Aynı ayet {ar:مِنْ حَيْثُ لَا يَشْعُرُونَ, tr:min haysu lâ yeş'urûn, gloss:farkına varmadıkları yerden, source:16:26} diye biter. Gece baskını da, kasabalara yöneltilen bir soruda geçer: {ar:أَن يَأْتِيَهُم بَأْسُنَا بَيَٰتًا وَهُمْ نَآئِمُونَ, tr:en ye'tiyehum be'sunâ beyâten ve hum nâimûn, gloss:onlar uyurken azabımızın gece baskınıyla gelmesinden, source:7:97}. Kitap ehlinden başka bir topluluk için de aynı söz söylenir: onlar {ar:مِن صَيَاصِيهِمْ, tr:min sayâsîhim, gloss:kalelerinden, source:33:26} indirilmiş ve kalplerine yine korku atılmıştır {source:33:26}.

On dördüncü ayet aynı kaleyi bu kez korkunun sığınağı olarak gösterir: {ar:لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍ, tr:lâ yukâtilûnekum cemî'an illâ fî kuran muhassanetin ev min verâi cudur, gloss:sizinle topluca ancak tahkimli kasabalarda ya da duvarlar ardından savaşırlar, source:59:14}. "Duvar" kelimesi, etrafı çevrili yeri anlatır: {ar:الجدير مكان بني حواليه جدار, tr:el-cedîr mekânun buniye havâleyhi cidâr, gloss:cedîr, çevresine duvar örülmüş yerdir, source:"ج د ر,B001"}. Ayet {ar:ذَٰلِكَ بِأَنَّهُمْ قَوْمٌ لَّا يَعْقِلُونَ, tr:zâlike bi-ennehum kavmun lâ ya'kılûn, gloss:çünkü onlar akıl etmeyen bir topluluktur, source:59:14} diye biter. Akıl kelimesinin ailesinde akıl ile sığınak aynı kelimedir: {ar:المعقل والعقل وهو الحصن, tr:el-ma'kılu ve'l-'akl ve huve'l-hısn, gloss:ma'kıl ve akıl, kaledir, source:"ع ق ل,B007"}. Dağa çekilip korunan ceylan da bu fiille anlatılır {source:"ع ق ل,B007"}. Böylece taştan surları çok olan topluluğun asıl eksiği iç kaledir. Nuh'un oğlu da böyle bir yanılgıya düşer ve {ar:سَـَٔاوِىٓ إِلَىٰ جَبَلٍ يَعْصِمُنِى مِنَ ٱلْمَآءِ, tr:se-âvî ilâ cebelin ya'sımunî mine'l-mâ', gloss:beni sudan koruyacak bir dağa sığınırım, source:11:43} der. Babası şöyle cevap verir: {ar:لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ, tr:lâ 'âsıme'l-yevme min emri'llâh, gloss:bugün Allah'ın emrinden koruyan yoktur, source:11:43}. Savaştan kaçan münafıklara da aynısı söylenir: {ar:وَلَوْ كُنتُمْ فِى بُرُوجٍ مُّشَيَّدَةٍ, tr:ve lev kuntum fî burûcin muşeyyede, gloss:sağlam yapılmış burçlarda olsanız bile, source:4:78}. O ayet de yine anlamayanlarla biter {source:4:78}. Allah'tan başka dost edinenlerin evi ise örümceğin evine benzer: {ar:وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ, tr:ve inne evhene'l-buyûti le-beytu'l-'ankebût, gloss:evlerin en zayıfı örümceğin evidir, source:29:41}. Buna karşılık Zülkarneyn'in demir seddini kuşatanlar onu delemez: {ar:وَمَا ٱسْتَطَٰعُوا۟ لَهُۥ نَقْبًا, tr:ve me'staṭâ'û lehû nakbâ, gloss:onu delmeye de güç yetiremediler, source:18:97}. Bu surede ise delik içeriden, sahiplerinin elleriyle açılır.

Dokuzuncu ayet bu kaleye karşı tersini koyar. Ensar, kendileri {ar:خَصَاصَةٌ, tr:hasâsa, gloss:darlık, yoksulluk, source:59:9} içindeyken bile başkalarını kendilerine tercih ederler. Bu kelimenin ailesinde kamıştan yapılmış aralıklı kulübe vardır: {ar:الخص بيت من قصب أو شجر وذلك لما يرى فيه من الخصاصة, tr:el-huss beytun min kasabin ev şecer, gloss:huss, aralıkları görünen kamış ya da dal evdir, source:"خ ص ص,B004"}. Delikli bu kulübe ayakta kalır, surlu kasaba ise içeriden yıkılır. Aynı ayet asıl tehlikeli duvarı içe, nefse yerleştirir: {ar:وَمَن يُوقَ شُحَّ نَفْسِهِۦ, tr:ve men yûka şuhha nefsih, gloss:kim nefsinin cimriliğinden korunursa, source:59:9}. Cimrilik kelimesinin aslı tutmak ve geri çevirmektir: {ar:الأصل فيه المنع ثم يكون منعا مع حرص, tr:el-aslu fîhi'l-men' summe yekûnu men'an ma'a hırs, gloss:aslı engellemedir, sonra hırsla engelleme olur, source:"ش ح ح,B001"}. Böylece "engelleyen kaleler" ile "engelleyen nefis" aynı kökten ses verir. Kurtuluş, bu iç kaleden "korunmak"tır. "Korunmak" fiili kalkan anlamıyla birlikte işitilir: {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:ittaki'llâh, gloss:Allah'tan sakın, yani kendinle O'nun azabı arasına bir siper koy, source:"و ق ي,B002"}. Zırh imgesi de buradan girer. "Kale" kelimesi zırhı anlatmak için de kullanılır: {ar:يتجوز به في كل تحرز ومنه درع حصينة, tr:yutecevvezu bihî fî kulli tahârruz, ve minhu dir'un hasîna, gloss:her korunma için mecazen kullanılır; sağlam zırh da buradandır, source:"ح ص ن,B001"}. Yirminci ayetin "cennet" kelimesi de kalkan ailesindendir: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micenn et-turs, ve'l-cunne ed-dir', gloss:micenn kalkandır, cunne zırhtır; seni koruyan her şey senin cunnendir, source:"ج ن ن,B008"}. Davud'a öğretilen zırh sanatı insanları {ar:لِتُحْصِنَكُم مِّنۢ بَأْسِكُمْ, tr:li-tuhsınekum min be'sikum, gloss:sizi savaşın şiddetinden korusun diye, source:21:80} içindir. Münafıklar ise yeminlerini kalkan edinir: {ar:ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةً, tr:ittehazû eymânehum cunne, gloss:yeminlerini kalkan edindiler, source:63:2}. Surenin yaşayan duvarı müminlerin safıdır: {ar:كَأَنَّهُم بُنْيَٰنٌ مَّرْصُوصٌ, tr:ke-ennehum bunyânun marsûs, gloss:sanki birbirine kenetlenmiş bir yapı, source:61:4}.

Kaynaklar: 59:2 حُصُونُهُم ح ص ن B001; 59:2 مَّانِعَتُهُمْ م ن ع B003; 59:1/23/24 ٱلْعَزِيزُ ع ز ز B001; 59:1/24 ٱلْحَكِيمُ ح ك م B001; 59:2 فَأَتَىٰهُمُ ء ت ي B011; 59:2 بُيُوتَهُم ب ي ت B004; 59:2 وَقَذَفَ ق ذ ف B001; 59:2 يُخْرِبُونَ خ ر ب B001; 59:14 جُدُرٍ ج د ر B001; 59:14 يَعْقِلُونَ ع ق ل B007; 59:9 خَصَاصَةٌ خ ص ص B004; 59:9 شُحَّ ش ح ح B001; 59:9/18 يُوقَ / ٱتَّقُوا و ق ي B002; 59:20 ٱلْجَنَّةِ ج ن ن B008

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

## Gece örtüsü ve açılan gün

Surede örtmek anlamı taşıyan birçok kelime vardır. "Küfür" kelimesinin kökü örtmektir: {ar:الستر والتغطية, tr:es-setr ve't-tağtiye, gloss:örtme ve kapama, source:"ك ف ر,B001"}. Bu kökte gece de kâfirdir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfir, gloss:gece, karanlığıyla örttüğü için "kâfir"dir, source:"ك ف ر,B002"}. Onuncu ayetteki bağışlanma duası da aynı örtme alanındadır: {ar:الغفر الستر, tr:el-ğafr es-setr, gloss:ğafr örtmektir, source:"غ ف ر,B001"}. "Cennet" de gecenin karanlığıdır: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyl, gloss:gecenin cenânı, karanlığı ve eşyayı örtmesidir, source:"ج ن ن,B002"}. Nifak da bir örtüdür: {ar:النفاق لأن صاحبه يكتم خلاف ما يظهر, tr:en-nifâk, gloss:nifak, sahibinin gösterdiğinin tersini gizlemesidir, source:"ن ف ق,B004"}. On dördüncü ayetteki "ardından" kelimesi de saklamayı anlatır: {ar:التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره, tr:et-tevriye es-setr, gloss:tevriye örtmedir; haberi gizleyip başkasını gösterdiğinde "verraytu" dersin, source:"و ر ي,B005"}. Bu yüzden münafıkların duvar arkasında savaşması ile sözlerinin arkasına gizlenmesi aynı kelimeyle işitilir. Tek fark, bir örtünün kurtarması, ötekinin boğmasıdır. Onuncu ayette istenen bağış örtüsü, kişiyi koruyan bir örtüdür. Küfür ve nifak örtüsü ise onu karanlıkta bırakır. On yedinci ayetteki "zalimler" kelimesi karanlığın kendisidir: {ar:الظلمة خلاف النور, tr:ez-zulme hılâfu'n-nûr, gloss:zulmet nurun karşıtıdır, source:"ظ ل م,B001"}. Ayette geçen "ateş" kelimesi ise ışıkla aynı yoldan adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan adlandırılmıştır, source:"ن و ر,B002"}. Ama ateş burada aydınlatmaz, yakar. Münafıklar da bir ateş yakar ama Allah ışıklarını götürür ve onları {ar:فِى ظُلُمَٰتٍ لَّا يُبْصِرُونَ, tr:fî zulumâtin lâ yubsırûn, gloss:göremedikleri karanlıklarda, source:2:17} bırakır. Kıyamette münafıklar müminlerin ışığından almak ister, onlara {ar:ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًا, tr:irci'û verâekum fe'ltemisû nûrâ, gloss:arkanıza dönün de bir ışık arayın, source:57:13} denir. Hemen ardından iki tarafı birbirinden ayıran bir sur çekilir {source:57:13}. Bu ayette surun ardı, ışık ve ayrılık, bu surenin kale, "ardında" ve karanlık kelimeleri bir arada bulunur.

Örtünün karşısında sabah açılır. Yirmi birinci ayetteki "parça parça olmuş" kelimesinin ailesinde sabah da vardır: {ar:الصديع الصبح, tr:es-sadî' es-subh, gloss:sadî' sabahtır, source:"ص د ع,B006"}. Dokuzuncu ayetteki "nefisler" kelimesi de sabahın nefes almasıdır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subh, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Kur'an aynı ifadeyi yemin olarak kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. On sekizinci ayetteki "yarın" kelimesi de seher vaktidir: {ar:الغدوة ما بين صلاة الغداة وطلوع الشمس, tr:el-ğudve, gloss:ğudve, sabah namazı ile güneşin doğuşu arasıdır, source:"غ د و,B001"}. Üçüncü ayetteki "sürgün" (celâ) kelimesi de açığa çıkıp görünür olmaktır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey' ve burûzuh, gloss:bir şeyin açılıp ortaya çıkması, source:"ج ل و,B001"}. Bu kelimenin bir dalı da gündüzün beyazlığıdır {source:"ج ل و,B007"}. Kur'an bu fiili gündüz için kullanır: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Sürgün edilenler kalelerinden çıkarılıp açık alana konur. Gece onları örtüyordu, şimdi her şey gün ışığına çıkar. Yirmi ikinci ayet bu iki yarıyı Allah'ın bilgisinde birleştirir: {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ, tr:'âlimu'l-ğaybi ve'ş-şehâde, gloss:görünmeyeni ve görüneni bilen, source:59:22}. "Gayb" kelimesinin kökü gözlerden gizlenmektir, güneşin batmasına da bu kökle "gâbet" denir {source:"غ ي ب,B001"}. "Şehâdet" ise oradan bakıp görmektir {source:"ش ه د,B001"}. Yirmi birinci ayetteki "hâşi'" kelimesi de batmaya yaklaşan yıldızlar için kullanılır: {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşa'ati'l-kevâkib, gloss:yıldızlar batmaya yaklaşınca "haşaat" denir, source:"خ ش ع,B003"}. Böylece batan yıldızla doğan sabah aynı ayette yan yana durur. Gece ile gündüzde gizlenen ile açıkta yürüyenin Allah katında eşit olduğu da söylenir {source:13:10}.

Kaynaklar: 59:2 كَفَرُوا ك ف ر B001, B002; 59:10 ٱغْفِرْ غ ف ر B001; 59:20 ٱلْجَنَّةِ ج ن ن B002; 59:11 نَافَقُوا ن ف ق B004; 59:14 وَرَآءِ و ر ي B005; 59:17 ٱلظَّٰلِمِينَ ظ ل م B001; 59:3 ٱلنَّارِ ن و ر B002; 59:21 مُّتَصَدِّعًا ص د ع B006; 59:9 أَنفُسِهِمْ ن ف س B009; 59:18 لِغَدٍ غ د و B001; 59:3 ٱلْجَلَآءَ ج ل و B001, B007; 59:22 ٱلْغَيْبِ غ ي ب B001; 59:22 ٱلشَّهَٰدَةِ ش ه د B001; 59:21 خَٰشِعًا خ ش ع B003

## Ön ve arka: topuk, iz ve el

On ikinci ayet münafıkların yardımının sonunu bir dönüş hareketiyle anlatır: {ar:وَلَئِن نَّصَرُوهُمْ لَيُوَلُّنَّ ٱلْأَدْبَٰرَ ثُمَّ لَا يُنصَرُونَ, tr:ve le-in nasarûhum le-yuvellunne'l-edbâra summe lâ yunsarûn, gloss:yardım etseler bile mutlaka arkalarını dönüp kaçarlar, sonra kendilerine de yardım edilmez, source:59:12}. "Arka" kelimesi önün karşıtıdır {source:"د ب ر,B001"}. Kaçmak da arka dönmektir {source:"و ل ي,B007"}. Dördüncü ve yedinci ayetlerdeki "ikâb" (ceza) ile on yedinci ayetteki "âkıbet" (son) kelimeleri topuk köküne bağlıdır: {ar:العقب مؤخر القدم, tr:el-'akib mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. Ceza da, suçun ardından en son geldiği için bu adla anılır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet 'ukûbeten, gloss:suçun ardından ikinci ve son geldiği için ukûbet denildi, source:"ع ق ب,B007"}. Arkasını dönen kişiye dönüp bakmamak da bu kökle ifade edilir: {ar:ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر, tr:vellâ mudbiren ve lem yu'akkıb, gloss:arkasını döndü ve geri dönüp bakmadı, source:"ع ق ب,B003"}. Sırtını dönüp kaçanın topuğunun dibinde ise ceza yürür. On altıncı ve on yedinci ayetler, Şeytan'ın insanı inkâra çağırıp sonra ondan uzaklaşmasını anlatır. Kur'an bu sahneyi Bedir'de bir dönüş hareketiyle de gösterir: {ar:نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌ مِّنكُمْ إِنِّىٓ أَرَىٰ مَا لَا تَرَوْنَ إِنِّىٓ أَخَافُ ٱللَّهَ ۚ وَٱللَّهُ شَدِيدُ ٱلْعِقَابِ, tr:nekesa 'alâ 'akibeyhi ve kâle innî berî'un minkum innî erâ mâ lâ teravne innî ehâfu'llâh, va'llâhu şedîdu'l-'ikâb, gloss:topukları üzerinde geri döndü ve "ben sizden uzağım, sizin görmediğinizi görüyorum, ben Allah'tan korkarım" dedi; Allah'ın cezası çetindir, source:8:48}. On altıncı ayetteki sözler ile dördüncü ayetin son sözleri bu ayette yan yana durur. Şeytan'ın uzaklaşması, topukları üzerinde geri dönmektir. İnsana karşı tavrı da {ar:وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًا, tr:ve kâne'ş-şeytânu li'l-insâni hazûlâ, gloss:şeytan insanı yüzüstü bırakandır, source:25:29} diye özetlenir. Arkasını dönüp kaçanın akıbeti başka bir ayette de aynen anlatılır {source:3:111}. Müminlerden de arkalarını dönmeyeceklerine dair ahit alınmıştır {source:33:15}.

Müminler ise bir yolda ardı ardına yürür. Onuncu ayetteki {ar:وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ, tr:vellezîne câû min ba'dihim, gloss:onlardan sonra gelenler, source:59:10} ifadesindeki "sonra" kelimesi topuk izine bağlanır: {ar:وما خلف بعقبه فهو من بعده, tr:ve mâ halefe bi-'akibihî fe-huve min ba'dih, gloss:topuğunun arkasında kalan, ondan sonradır, source:"ب ع د,B002"}. Onlar {ar:سَبَقُونَا بِٱلْإِيمَٰنِ, tr:sebekûnâ bi'l-îmân, gloss:bizden önce imana koştular, source:59:10} diye öncekileri anar. "Sebk" yolda öne geçmektir {source:"س ب ق,B001"}. Dokuzuncu ayetteki "îsâr" (tercih etmek) da iz sürmenin köküdür: {ar:الأثر الاستقفاء والاتباع وذهبت في إثره, tr:el-eser el-istikfâ' ve'l-ittibâ', gloss:eser, peşinden gitmek ve izine uymaktır, source:"ء ث ر,B004"}. Bu sırayı Kur'an da adlarıyla verir: {ar:وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم, tr:ve's-sâbikûne'l-evvelûne mine'l-muhâcirîne ve'l-ensâri ve'llezîne'ttebe'ûhum, gloss:muhacirlerden ve ensardan ilk öncüler ve onlara uyanlar, source:9:100}. Böylece münafıklar düşmana arkalarını döner, müminler ise öndekilerin izinden yürür. On sekizinci ayet bu düzende bakışı öne çevirir: {ar:وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ, tr:ve'l-tenzur nefsun mâ kaddemet li-ğad, gloss:herkes yarına ne gönderdiğine baksın, source:59:18}. "Önden göndermek" fiili önün ve arkanın kelimesidir: {ar:قدام خلاف وراء والقدم ضد الأخر, tr:kuddâm hılâfu verâ', gloss:ön, arkanın karşıtıdır, source:"ق د م,B004"}. Bu fiil on dördüncü ayetteki "ardından" ve üçüncü ayetteki "ahiret" kelimeleriyle bir karşıtlık kurar. "Ahiret" en son gelendir {source:"ء خ ر,B001"}. "Ardından" ise hem arkayı hem önü anlatabilir {source:"و ر ي,B006"}. Tedbir de akıbete bakmaktır: {ar:التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته, tr:et-tedbîr, gloss:tedbir, bir işin akıbetinin nereye varacağına bakmaktır, source:"د ب ر,B006"}. Bu ifadede on ikinci ayetin "arka" kökü, on yedinci ayetin "akıbet"i ve on sekizinci ayetin "bakmak" fiili birleşir. Kim akıbetine bakarsa, topuğunun ardındaki cezadan kurtulur. Kur'an bu bakışı başka yerlerde de anlatır: {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:'alimet nefsun mâ kaddemet ve ehharat, gloss:herkes önden ne gönderdiğini, geride ne bıraktığını bilir, source:82:5}. Pişman olan da {ar:يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önden bir şey gönderseydim, source:89:24} der.

El bu iki ayeti birbirine bağlar. İkinci ayette evler "kendi elleriyle" yıkılır. El, bir deyimde kişinin kendi işlediğinin sahibi olmasıdır: {ar:هذا ما قدمت يداك أي جنيته أنت, tr:hâzâ mâ kaddemet yedâk, gloss:bu senin ellerinin önden gönderdiğidir, yani bunu sen işledin, source:"ي د ي,B009"}. Bu ifadede ikinci ayetin "eller"i ile on sekizinci ayetin "önden gönderdi" fiili birleşir. Kur'an da {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâh, gloss:kişinin ellerinin önden gönderdiğine baktığı gün, source:78:40} der. Burada bakmak, önden göndermek ve el bir aradadır. On sekizinci ayetin çağrısının tersi de vardır: {ar:وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ, tr:ve nesiye mâ kaddemet yedâh, gloss:ellerinin önden gönderdiğini unuttu, source:18:57}. On dokuzuncu ayetteki unutanlar da aynı yere düşer. Münafıklar ise ellerini sıkar ve unutur: {ar:وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ, tr:ve yakbıdûne eydiyehum, nesu'llâhe fe-nesiyehum, inne'l-munâfıkîne humu'l-fâsikûn, gloss:ellerini sıkı tutarlar; Allah'ı unuttular, O da onları unuttu; münafıklar fâsıkların ta kendileridir, source:9:67}. Bu ayet, sure içinde dağınık duran unutma, fısk ve sıkı tutulan el kavramlarını tek cümlede toplar. Yedinci ayetteki "dûle" de elden ele geçmektir {source:"ي د ي,B007"}. El ayrıca nimet ve iyiliktir {source:"ي د ي,B003"}. Dokuzuncu ayette Ensar elindekini açar, sıkmaz. Kur'an eli boyna bağlamayı da yasaklar {source:17:29}.

Kaynaklar: 59:12 لَيُوَلُّنَّ و ل ي B007; 59:12 ٱلْأَدْبَٰرَ د ب ر B001, B006; 59:4/7 ٱلْعِقَابِ ع ق ب B002, B003, B007; 59:17 عَٰقِبَتَهُمَآ ع ق ب B002; 59:10 بَعْدِهِمْ ب ع د B002; 59:10 سَبَقُونَا س ب ق B001; 59:9 يُؤْثِرُونَ ء ث ر B004; 59:18 قَدَّمَتْ ق د م B004; 59:3 ٱلْءَاخِرَةِ ء خ ر B001; 59:14 وَرَآءِ و ر ي B006; 59:2 بِأَيْدِيهِمْ ي د ي B009; 59:7 دُولَةً ي د ي B007; 59:9 (Ensar'ın verişi) ي د ي B003

## Görmekten geçmeye

İkinci ayet, kuşatma sahnesini bir çağrıyla bitirir: {ar:فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:fa'teberû yâ uli'l-ebsâr, gloss:ibret alın ey basiret sahipleri, source:59:2}. "İ'tibâr" kelimesi bir geçiştir: {ar:الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد, tr:el-i'tibâr ve'l-'ibra, gloss:i'tibâr ve ibret, görülenin bilgisinden görülmeyene ulaştıran durumdur, source:"ع ب ر,B004"}. Rüyayı yorumlayan da dışından içine geçer {source:"ع ب ر,B002"}. Basiret ise kalpte delip geçen bir görmedir {source:"ب ص ر,B002"}. Beşinci ayetteki "kesmek" fiili de nehri geçmek anlamında kullanılır: {ar:قطعت النهر قطوعا عبرته, tr:kata'tu'n-nehra kutû'an, gloss:nehri kat ettim, yani geçtim, source:"ق ط ع,B003"}. Bu ifadede "kesmek" ile "geçmek" birleşir. İbret, gözün gördüğü yıkılmış evlerden, görülmeyen sebebe geçmektir. Kur'an aynı çağrıyı Bedir'deki iki birlik için de yapar: {ar:يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ... إِنَّ فِى ذَٰلِكَ لَعِبْرَةً لِّأُو۟لِى ٱلْأَبْصَٰرِ, tr:yeravnehum misleyhim ra'ye'l-'ayn ... inne fî zâlike le-'ibraten li-uli'l-ebsâr, gloss:onları göz görüşüyle kendilerinin iki katı görüyorlardı; bunda basiret sahipleri için elbette bir ibret vardır, source:3:13}. Gece ile gündüzün dönüşümü için de aynı sözler kullanılır {source:24:44}. Üçüncü ayetteki "sürgün" (celâ) kelimesi gözü de açar: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ el-ismid, gloss:celâ sürmedir, çünkü gözü parlatır, source:"ج ل و,B002"}. Sürgün, ona bakanların gözüne çekilen bir sürme gibidir.

Görmenin karşısında sure tahmini koyar. Kuşatılanlar kalelerinin kendilerini koruyacağını "zannetmiştir" ve gelişi "hesaba katmamışlardır". Zan, kesin olmayan bilgidir {source:"ظ ن ن,B003"}. Bir dalı da içinde su olup olmadığı bilinmeyen kuyudur: {ar:الظنون البئر لا يدرى أفيها ماء أم لا, tr:ez-zenûn el-bi'r, gloss:zenûn, içinde su olup olmadığı bilinmeyen kuyudur, source:"ظ ن ن,B006"}. On dördüncü ayetteki "sanırsın" fiili de zan demektir {source:"ح س ب,B002"}. Altıncı ayetteki "atlar" kelimesinin ailesinde de aynada görülen gölge vardır: {ar:الخيال كل شيء تراه كالظل وخيالك في المرآة, tr:el-hayâl kullu şey'in terâhu ke'z-zıll, gloss:hayâl, gölge gibi gördüğün her şey ve aynadaki görüntündür, source:"خ ي ل,B001"}. Kuşatılanların kaleleri, münafıkların vaatleri ve toplu görünen kalabalık, hepsi bu tür gölgelerdir. Bu yüzden sure iki kez "görmedin mi" ve "görürdün" diye sorar: on birinci ayette münafıklara, yirmi birinci ayette dağa. On sekizinci ayetteki "baksın" fiili de gözle ve basiretle bir şeyi evirip çevirmektir {source:"ن ظ ر,B001"}. Ayetin sonundaki "haberdar" ismi de dışın karşısında içi anlatır: {ar:المخبر خلاف المنظر, tr:el-mahber hılâfu'l-manzar, gloss:iç yüz, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. İnsan kendi görünüşüne bakar, Allah ise iç yüzünü bilir. On üçüncü ve on dördüncü ayetlerdeki "topluluk" kelimesinin ailesinde de, göz bebeği sağlam olduğu halde görmeyen göz vardır: {ar:عين قائمة ذهب بصرها والحدقة صحيحة, tr:'aynun kâime, gloss:göz bebeği sağlam olduğu halde görme gücü gitmiş göz, source:"ق و م,B021"}. Bu iki ayet o topluluğu {ar:قَوْمٌ لَّا يَفْقَهُونَ, tr:kavmun lâ yefkahûn, gloss:anlamayan bir topluluk, source:59:13} ve akıl etmeyen bir topluluk diye anar. Kur'an bu körlüğü açıkça tarif eder: {ar:وَلَهُمْ أَعْيُنٌ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Münafıkların görünüşü de insanı hayran bırakır, ama onlar dayalı kütükler gibidir {source:63:4}. Sekizinci ayetteki fakirlerin durumu ise tersine bir yanılgıdır: bilmeyen kişi onları {ar:يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ, tr:yahsebuhumu'l-câhilu ağniyâ', gloss:bilmeyen onları zengin sanır, source:2:273}. Göz, burada da dışa bakıp içi kaçırır.

Kaynaklar: 59:2 فَٱعْتَبِرُوا ع ب ر B004, B002; 59:2 ٱلْأَبْصَٰرِ ب ص ر B002; 59:5 قَطَعْتُم ق ط ع B003; 59:3 ٱلْجَلَآءَ ج ل و B002; 59:2 ظَنُّوا ظ ن ن B003, B006; 59:14 تَحْسَبُهُمْ ح س ب B002; 59:6 خَيْلٍ خ ي ل B001; 59:18 وَلْتَنظُرْ ن ظ ر B001; 59:18 خَبِيرٌ خ ب ر B001; 59:13/14 قَوْمٌ ق و م B021

## Bağlar, köstekler, ipler

On dördüncü ayetteki "akıl" kelimesi, kale anlamının yanında deveyi bağlamak anlamını da taşır: {ar:عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط, tr:'akaltu'l-ba'îr, gloss:devenin ayağını ipiyle bağladım; ikâl bağdır, source:"ع ق ل,B002"}. Akıl etmeyen bir topluluk, bağı olmayan bir sürü gibidir. Kalpleri dağınık olanlar ip tutmaz. Dördüncü ve yedinci ayetlerdeki {ar:شَدِيدُ ٱلْعِقَابِ, tr:şedîdu'l-'ikâb, gloss:cezası çetin, source:59:4} ifadesi de bir bağlama işini taşır: {ar:عقبت الرمح شددته بالعقب, tr:'akabtu'r-rumh, gloss:mızrağı sinirle sıkıca bağladım, source:"ع ق ب,B001"}. "Şiddet" de düğümü sıkmaktır {source:"ش د د,B001"}. Bu ceza kaçana gevşemeyen bir sinir bağı gibi sarılır. Onuncu ve on birinci ayetlerdeki "kardeşler" kelimesi, hayvanın bağlandığı kazığı da adlandırır: {ar:الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة, tr:el-âhiyye, gloss:âhiyye, hayvanın bağlandığı kazıktır; aynı zamanda saygınlık ve ahittir, source:"ء خ و,B002"}. Sure iki tür kardeşlik gösterir. Onuncu ayette müminler {ar:رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا, tr:rabbena'ğfir lenâ ve li-ihvâninâ, gloss:Rabbimiz, bizi ve kardeşlerimizi bağışla, source:59:10} diye dua eder. On birinci ayette ise münafıklar {ar:يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟, tr:yekûlûne li-ihvânihimu'llezîne keferû, gloss:inkâr eden kardeşlerine diyorlar, source:59:11}. Birinci bağ kazığa sağlam bağlıdır, ikincisi kriz anında çözülür. Kur'an müminlere sağlam bir ip gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Bu ayette, on dördüncü ayetteki "toplu" kelimesi bir ipe bağlanmış olur. Kitap ehli için de iki ip anılır {source:3:112}. On altıncı ayetteki "Şeytan" kelimesi de ip ailesindendir: {ar:الشطن الحبل الطويل الشديد الفتل يستقى به, tr:eş-şatan el-hablu't-tavîl, gloss:şatan, su çekilen uzun, sıkı bükülmüş iptir, source:"ش ط ن,B002"}. Bu kökte ayrıca birini niyetinin yönünden saptırmak da vardır {source:"ش ط ن,B003"}. Şeytan uzun bir iple insanı derin bir kuyuya indirir, sonra ipi bırakır. Kendi sözüyle de, insanlar üzerinde bir gücü olmadığını, onları kurtaramayacağını söyler {source:14:22}. Onuncu ayetteki "ğıll" kelimesi, başka bir harekeyle, elleri boyna bağlayan demir halkadır: {ar:الغل مختص بما يقيد به فيجعل الأعضاء وسطه, tr:el-ğull, gloss:ğull, uzuvları ortasına alarak bağlayan bukağıdır, source:"غ ل ل,B006"}. On dördüncü ayetteki "toplu" kelimesi de aynı bukağıyı adlandırır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull, gloss:câmia bukağıdır, çünkü elleri boyuna birleştirir, source:"ج م ع,B008"}. Böylece kalpteki kin ile ellerdeki bukağı aynı kökten ses verir. Toplu sanılan kalabalık da birbirine bukağıyla bağlanmış olur. Kur'an bukağıyı da gösterir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu da bukağılayın, source:69:30}. Birinci ve yirmi dördüncü ayetlerdeki "Hakîm" ismi de, ailesinde atın çenesini saran gem halkasıdır {source:"ح ك م,B006"}. On birinci ayetteki "boyun eğmek" fiili de dizgine kolay uyan atı anlatır {source:"ط و ع,B001"}. Münafıklar "kimseye boyun eğmeyiz" derken, aslında gemsiz kalırlar.

Kaynaklar: 59:14 يَعْقِلُونَ ع ق ل B002; 59:4/7 شَدِيدُ ٱلْعِقَابِ ع ق ب B001, ش د د B001; 59:10/11 إِخْوَٰن ء خ و B002; 59:16 ٱلشَّيْطَٰنِ ش ط ن B002, B003; 59:10 غِلًّا غ ل ل B006; 59:14 جَمِيعًا ج م ع B008; 59:1/24 ٱلْحَكِيمُ ح ك م B006; 59:11 نُطِيعُ ط و ع B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

