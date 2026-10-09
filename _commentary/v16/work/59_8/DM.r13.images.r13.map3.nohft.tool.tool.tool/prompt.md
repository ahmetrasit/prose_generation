Focus: 59:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_8/D.r13/context.md =====
# 59:8 — focus

لِلْفُقَرَآءِ ٱلْمُهَٰجِرِينَ ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا وَيَنصُرُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لِلْفُقَرَآءِ | فَقِير | ف ق ر | P;DET;N |
| 2 | ٱلْمُهَٰجِرِينَ | مُهَاجِر | ه ج ر | DET;ADJ |
| 3 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 4 | أُخْرِجُوا۟ | أَخْرَجَ | خ ر ج | V;PRON |
| 5 | مِن | مِن |  | P |
| 6 | دِيَٰرِهِمْ | دَار | د و ر | N;PRON |
| 7 | وَأَمْوَٰلِهِمْ | مَال | م و ل | CONJ;N;PRON |
| 8 | يَبْتَغُونَ | ٱبْتَغَىٰ | ب غ ي | V;PRON |
| 9 | فَضْلًا | فَضْل | ف ض ل | N |
| 10 | مِّنَ | مِن |  | P |
| 11 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 12 | وَرِضْوَٰنًا | رِضْوَٰن | ر ض و | CONJ;N |
| 13 | وَيَنصُرُونَ | نَصَرَ | ن ص ر | CONJ;V;PRON |
| 14 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 15 | وَرَسُولَهُۥٓ | رَسُول | ر س ل | CONJ;N;PRON |
| 16 | أُو۟لَٰٓئِكَ | أُولَٰٓئِك |  | DEM |
| 17 | هُمُ |  |  | PRON |
| 18 | ٱلصَّٰدِقُونَ | صَادِق | ص د ق | DET;N |


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
- 59:8 ◀ focus لِلْفُقَرَآءِ ٱلْمُهَٰجِرِينَ ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا وَيَنصُرُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ
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


===== _commentary/v16/work/59_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ف ق ر (root_001169) — identity root of لِلْفُقَرَآءِ (w1)

- **B001** omurga omurları — omurga omurları · tek bir omur · omur · omurgası kırılmış kimse · sırtı veya omurgası kırılmış
  الفقار للظهر الواحدة فقارة (maqayis)؛ الفقار منضد بعضه ببعض (ayn)؛ الفقارة واحدة فقار الظهر (sihah)؛ للإنسان أربع وعشرون فقارة (tahdhib)؛ أصل الفقير المكسور الفقار (mufradat)
- **B002** maddi yoksulluk — maddi yoksulluk ve ihtiyaç · yoksullaşma, ihtiyaç içine düşme · yoksul, ihtiyaç sahibi kimse · yoksullar, ihtiyaç sahipleri · maddi ihtiyaç alanları, geçim açıkları · Tanrı onu yoksul bıraktı
  الفقير مكسور فقار الظهر من ذلته ومسكنته (maqayis)؛ الفقر الحاجة وافتقر فلان (ayn)؛ رجل فقير من المال (sihah)؛ الفقر الحاجة وفعله الافتقار (tahdhib)؛ عدم المقتنيات (mufradat)
- **B003** Tanrı'ya zorunlu bağımlılık [kalıp] — Tanrı'ya zorunlu ihtiyaç · Tanrı'ya zorunlu olarak muhtaç olanlar
  وجود الحاجة الضرورية؛ الفقر إلى الله المشار إليه
- **B004** gönül doymazlığı [kalıp] — gönül doymazlığı, açgözlülük
  فقر النفس وهو الشره
- **B005** su çıkışı, kuyu veya işlevli yer çukuru — kanalın su çıkışı veya kuyu ağzı · su biriken çukur veya belirli kuyu · fidanın çevresine açılan dikim çukuru · yer çukuru veya atış sınırı işareti · fidan için çukur açtı · çok çukurlu arazi
  الفقير مخرج الماء من القناة (maqayis)؛ الفقرة حفرة لغرس فسيل (ayn)؛ الفقير حفير يحفر حول الفسيلة (sihah)؛ الفقير له ثلاثة مواضع (tahdhib)؛ لكل حفيرة يجتمع فيها الماء فقير (mufradat)
- **B006** çentik, oyuk veya delik açma — hayvanın burnuna çentik veya delik açtı · hayvanın burnundaki çentik · burnu çentilmiş veya delinmiş hayvan · boncuğu deldi · yüzünde çentikler bulunan kılıç · küçük oyukları nedeniyle özel ad verilmiş kılıç
  فقرت البعير إذا حززت خطمه (maqayis)؛ فقرت أنف البعير (sihah)؛ وفقرت الخرز أي ثقبته (tahdhib)؛ وأفقرت البعير ثقبت خطمه (mufradat)
- **B007** sırtı kullanıma verme veya hedefi atışa açma — ona bir binek hayvanını geçici olarak ödünç verdi · binek hayvanını geçici kullanma ödüncü · av omurga bölgesini atışa açtı · atış yapma olanağı verdi
  أفقرك الصيد أمكنك من فقاره (maqayis)؛ أفقرته دابة أعرته للحمل والمركب (ayn)؛ أفقرت فلانا ناقتي (sihah)؛ الإفقار أن يعطي الرجل دابته (tahdhib)؛ أفقرك الصيد فارمه (mufradat)
- **B008** omurgayı kıracak denli ağır felaket — omurgayı kıracak denli ağır felaket · başına belini büken bir felaket geldi · yıkıcı felaket onu ağır biçimde etkiledi
  فقرتهم الفاقرة وهي الداهية (maqayis)؛ الفاقرة الداهية تكسر فقار الظهر (ayn)؛ الفاقرة الداهية (sihah)؛ الفاقرة داهية تكسر الظهر (tahdhib)؛ فقرته فاقرة أي داهية تكسر الفقار (mufradat)
- **B009** üç büyük hayat meselesi veya üç dokunulmaz konu [kalıp] — insan hayatının üç büyük meselesi · dokunulmaz sayılan üç önemli konu
  فقرات ابن آدم ثلاث؛ الفقرات هي الأمور العظام؛ استحلوا الفقر الثلاث
- **B010** bir işi denetleyip yürütecek güçte olma [kalıp] — güçlü, belirli bir işi denetleyip yürütebilen kişi
  رجل مفقر أي قوي؛ لمفقر لذاك الأمر أي مقرن له ضابط

## ه ج ر (root_001578) — identity root of ٱلْمُهَٰجِرِينَ (w2)

- **B001** bağı kesip uzaklaşma — bağı ve gözetilmesi gereken ilgiyi kesme · onu bırakıp ondan uzaklaşmak · karşılıklı ilişki kesme
  الهجر ضد الوصل (maqayis;jamhara;sihah)؛ الهجر والهجران ترك ما يلزمك تعهده (ayn;tahdhib)؛ مفارقة الإنسان غيره إما بالبدن أو باللسان أو بالقلب (mufradat)؛ هجر الرجل هجرا إذا تباعد ونأى (tahdhib)
- **B002** yurdunu bırakıp başka yere göçme — ilk yeri bırakıp başka yere göçme · yurdunu bırakıp başka yerde yaşayan kimse
  هاجر القوم من دار إلى دار تركوا الأولى للثانية (maqayis)؛ هجرة المهاجرين لأنهم هجروا عشائرهم (ayn)؛ هاجر الرجل أهله وقومه (jamhara)؛ المهاجرة من أرض إلى أرض ترك الأولى للثانية (sihah)؛ كل من فارق رباعه وسكن بلدا آخر فهو مهاجر (tahdhib)؛ الخروج من دار الكفر إلى دار الإيمان (mufradat)
- **B003** bilerek çirkin ve edepsiz söz söyleme — çirkin ve edepsiz söz · bilerek çirkin söz söylemek · birine yöneltilen yüz kızartıcı sözler
  الهجر الإفحاش في المنطق (maqayis)؛ تقولون الهجر أي قول الخنا والإفحاش في المنطق (ayn)؛ الهجر ما لا ينبغي من الكلام (jamhara)؛ الهجر بالضم الاسم من الإهجار وهو الإفحاش في المنطق والخنا (sihah)؛ الهجر الإفحاش في المنطق والخنا (tahdhib)؛ الهجر الكلام القبيح المهجور لقبحه (mufradat)
- **B004** hastalık sırasında istemeden sayıklama — hastanın istemeden sayıklaması · hastanın düzensiz sayıklaması
  الهجر الهذيان يقال هجر الرجل (maqayis)؛ الهجر هذيان المبرسم (ayn)؛ هجر المريض إذا هذى (jamhara)؛ هجر المريض يهجر هجرا (sihah)؛ مثل كلام المبرسم والمحموم (tahdhib)؛ هجر المريض إذا أتى ذلك من غير قصد (mufradat)
- **B005** sıcağın bastırdığı öğle vakti — sıcağın bastırdığı öğle vakti · topluluk öğle sıcağında yola çıktı · öğle vakti yenen yemek
  الهجر والهجير والهاجرة نصف النهار عند اشتداد الحر (maqayis)؛ الهجر والهاجر والهجيرة نصف النهار (ayn)؛ الهجير والهاجرة والهجر انتصاف النهار (jamhara)؛ الهجر والهاجرة نصف النهار عند اشتداد الحر (sihah)؛ الهاجرة قبل الظهر بقليل وبعدها بقليل (tahdhib)؛ الهجير والهاجرة الساعة التي يمتنع فيها من السير كالحر (mufradat)؛ هجروا ساروا في ذلك الوقت (maqayis;jamhara;sihah;tahdhib)؛ الهجوري للطعام الذي يؤكل نصف النهار (tahdhib)
- **B006** vaktin başında erkenden gitme — vaktin başında erkenden gitme
  التهجير إلى الجمعة وغيرها التبكير (tahdhib)؛ الذهاب إليها في أول أوقاتها (tahdhib)؛ بهجير الفجر أي يبكرون بوقت السحر (tahdhib)
- **B007** hayvanın ayaklarını bağlayan ip — hayvanın ayaklarını bağlayan ip · deveyi ayak bağından bağlamak · yay kirişi
  أصل على شد شيء وربطه (maqayis)؛ الهجار مخالف للشكال تشد به يد الفحل إلى إحدى رجليه (ayn;tahdhib)؛ الهجار حبل يشد في حقو البعير ثم يشد في أحد رسغي يديه (jamhara)؛ الهجار حبل يشد في رسغ رجل البعير ثم يشد إلى حقوه (sihah)؛ الهجار حبل يشد به الفحل (mufradat)؛ هجار القوس وترها (sihah;tahdhib;mufradat)
- **B008** benzerlerini aşan üstünlük — eşsiz veya başkasından daha değerli · bir niteliği olağan ölçüyü aşmış
  هذا شيء هجر أي لا نظير له (maqayis)؛ هذا أهجر من هذا أي أكرم (maqayis;sihah)؛ أهجرت الجارية إذا شبت شبابا حسنا (jamhara)؛ ناقة مهجرة أي فائقة في الشحم والسير (sihah)؛ كل شيء جاوز حده في تمامه إنه لمهجر (tahdhib)؛ نخلة مهجرة إذا أفرطت في الطول (tahdhib)
- **B009** sürekli alışkanlık ve uğraş — sürekli işi, alışkanlığı veya dilinden düşürmediği konu
  الاسم الهجيرى (ayn)؛ ما زال ذاك هجيراه وإهجيراه أي دأبه (jamhara)؛ الهجير مثال الفسيق الدأب والعادة وكذلك الهجيرى والإهجيرى (sihah)؛ هجيرى الرجل كلامه ودأبه وشأنه (tahdhib)؛ فلان هجيراه كذا إذا أولع بذكره (mufradat)
- **B010** kurumuş bitki, özellikle tuzcul ot — hayvanların kırdığı kuru bitki veya tuzcul ot
  الهجير يبيس النبت الذي كسرته الماشية (maqayis)؛ الهجير يبيس الحمض الذي كسرته الماشية (sihah)؛ الهجير ما يبس من الحمض (tahdhib)
- **B011** su için ayrılmış büyük veya yapılı havuz — su için ayrılmış büyük veya yapılı havuz · bu adla anılan yapı türü
  الهجير الحوض الكبير سمي لأنه شيء يقتطع للماء (maqayis)؛ الهجير الحوض الكبير (sihah)؛ الهجير الحوض المبني (tahdhib)؛ الهاجري البناء (tahdhib)
- **B012** yer ve soy kolu adları — bilinen bir ülke adı · iki ayrı yer adı · bir soy kolunun adı · söz konusu ülkeye bağlı olan
  هجر بلد (ayn)؛ هجر بلد معروفة (jamhara)؛ الهجر موضع بالألف واللام (jamhara)؛ الهجير موضع أيضا (jamhara)؛ بنو هاجر بطن من بني ضبة (jamhara)؛ هجر اسم بلد والنسبة هاجري (sihah)
- **B013** yaklaşık bir yıllık aradan sonra — yaklaşık bir yıllık aradan sonra · bir tam yıl
  لقيت فلانا عن هجر بعد الحول ونحوه (tahdhib)؛ الهجيرة تصغير الهجرة وهي السنة التامة (tahdhib)

## خ ر ج (root_000400) — identity root of أُخْرِجُوا۟ (w4)

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

## د و ر (root_000499) — identity root of دِيَٰرِهِمْ (w6)

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

## م و ل (root_001457) — identity root of وَأَمْوَٰلِهِمْ (w7)

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ب غ ي (root_000138) — identity root of يَبْتَغُونَ (w8)

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

## ف ض ل (root_001163) — identity root of فَضْلًا (w9)

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

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w11)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ر ض و (root_000569) — identity root of وَرِضْوَٰنًا (w12)

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ن ص ر (root_001510) — identity root of وَيَنصُرُونَ (w13)

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

## ر س ل (root_000563) — identity root of وَرَسُولَهُۥٓ (w15)

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

## ص د ق (root_000852) — identity root of ٱلصَّٰدِقُونَ (w18)

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

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ر ض ي (root_000570) — for وَرِضْوَٰنًا (w12): withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:8, and ## Buluşmalar) =====
## Başka yerden gelen sel, yağmayan bulut, sönük çakmak

İkinci ayetteki "hesaba katmadıkları yerden geldi" sözü, kelime ailesinde bir sel sahnesiyle de işitilir: {ar:سيل أتي وأتاوي إذا جاءك ولم يصبك مطره, tr:seylun etiyyun ve etâviyyun izâ câ'eke ve lem yusıbke matarüh, gloss:yağmuru sana değmediği halde sana gelen sel, source:"ء ت ي,B005"}. Kişi kendi göğüne bakar, bulut görmez. Su ise başka bir diyarda yağmış ve vadiden ona gelmiştir. "Hesaba katmamak" fiili de gökten gelen dolu ile aynı ailededir: {ar:حسبان من السماء بالبرد, tr:husbân mine's-semâ' bi'l-berad, gloss:gökten gelen dolu, source:"ح س ب,B007"}. Onların kalbine atılan "ru'b" (korku) da vadiyi dolduran bir seldir: {ar:سيل راعب إذا ملأ الوادي, tr:seylun râ'ib izâ mele'e'l-vâdî, gloss:vadiyi doldurduğunda sel "râib" olur, source:"ر ع ب,B002"}. Bu korku kalpte bir duygu olarak kalmaz, vadiyi dolduran su gibi her yeri kaplar. Surenin başındaki "Azîz" ismi de, başka bir dalda, karşı konulmaz seli anlatır: {ar:سيل عز وهو السيل الغالب, tr:seylun 'izz, gloss:galip gelen sel, source:"ع ز ز,B008"}. "Haşr" kelimesinde ise kıtlık yılının insanları şehirlere sürmesi vardır: {ar:حشرتهم السنة إذا أصابهم الضر حتى يهبطوا الأمصار, tr:haşerethumu's-sene, gloss:sıkıntı onlara dokunup şehirlere inmeye zorlayınca "yıl onları sürdü" denir, source:"ح ش ر,B002"}. On beşinci ayette ise önceki topluluk bu suyun ağırlığını tatmıştır: {ar:ذَاقُوا۟ وَبَالَ أَمْرِهِمْ, tr:zâkû vebâle emrihim, gloss:işlerinin vebalini tattılar, source:59:15}. "Vebâl" sağanakla aynı köktendir: {ar:الوبل والوابل المطر الشديد, tr:el-vebl ve'l-vâbil el-matar eş-şedîd, gloss:vebl ve vâbil şiddetli yağmurdur, source:"و ب ل,B001"}. Bir anlamı da ağırlıktır {source:"و ب ل,B002"}. Firavun'un yakalanışı da {ar:أَخْذًا وَبِيلًا, tr:ahzen vebîlâ, gloss:ağır bir yakalayış, source:73:16} diye anlatılır. Aynı sözler başka bir surede de neredeyse aynen tekrarlanır: {ar:فَذَاقُوا۟ وَبَالَ أَمْرِهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ, tr:fe-zâkû vebâle emrihim ve lehum 'azâbun elîm, gloss:işlerinin vebalini tattılar, onlara acı bir azap da var, source:64:5}. Kur'an aynı sahneyi bir bahçe için de kurar: sahipleri ona güç yetirdiklerini sanırken {ar:أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًا فَجَعَلْنَٰهَا حَصِيدًا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:etâhâ emrunâ leylen ev nehâran fe-ce'alnâhâ hasîden ke-en lem tağne bi'l-ems, gloss:gece ya da gündüz emrimiz ona geldi, onu dünkü gün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Orada da "zannettiler" ve "geldi" fiilleri yan yana durur, tıpkı ikinci ayette olduğu gibi.

Su sahnesinin bir de ters yüzü vardır. Altıncı ayetteki "atlar" kelimesinin ailesinde, yağacakmış gibi görünen bulut vardır: {ar:الخيال غيم ينشأ يخيل إليك أنه ماطر, tr:el-hayâl ğaymun yenşe'u yuhayyilu ileyke ennehû mâtır, gloss:hayâl, sana yağacakmış gibi görünen buluttur, source:"خ ي ل,B004"}. On birinci ayette münafıklar {ar:وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ, tr:ve in kûtiltum le-nensurannekum, gloss:size savaş açılırsa mutlaka yardım ederiz, source:59:11} diye söz verir. "Yardım etmek" fiili, ailesinde yağmurun bir yeri sulamasıdır: {ar:نصر الغيث البلاد أرواها, tr:nasara'l-ğaysu'l-bilâd ervâhâ, gloss:yağmur ülkeye yardım etti, yani onu suladı, source:"ن ص ر,B004"}. Bu vaat de hiç yağmayan buluta döner. On birinci ayetin sonu da bunu söyler: {ar:وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ, tr:va'llâhu yeşhedu innehum le-kâzibûn, gloss:Allah şahitlik eder ki onlar yalancıdır, source:59:11}. Yalan kelimesi, ailesinde kesilen süt akışına da uzanır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü, süreceği sanılıp sürmeyince "yalan söyledi" denir, source:"ك ذ ب,B006"}. Aynı tanıklık münafıklar için başka bir yerde aynı sözlerle verilir {source:63:1}. Kur'an münafıkları ayrıca karanlık, gök gürültüsü ve şimşekle dolu bir sağanağa benzetir {source:2:19}. Burada ise sağanak bile yoktur, yalnızca yağmur gösterip yağmayan bir hayal vardır. Ensar'ın kurtulduğu cimrilik de suyla ilgili bir ifadeyle anlatılır: {ar:أرض شحاح لا تسيل إلا من مطر جود, tr:ardun şihâh, gloss:ancak bol yağmurla sel akıtan cimri toprak, source:"ش ح ح,B004"}.

Ateş tarafında da aynı şey görülür. Dokuzuncu ayetteki cimrilik, ailesinde ateş vermeyen çakmaktır: {ar:الزند الشحاح الذي لا يوري, tr:ez-zendu'ş-şihâh ellezî lâ yûrî, gloss:kıvılcım çıkarmayan cimri çakmak, source:"ش ح ح,B003"}. On dördüncü ayetteki "ardından" kelimesi ise ateş veren çakmağın köküdür: {ar:ورى الزند خرجت ناره, tr:verâ'z-zend, gloss:çakmak ateşini çıkardı, source:"و ر ي,B002"}. Aynı kökte bir deyim de vardır: {ar:لوريت عن مولاك أي نصرته ودفعت عنه, tr:le-verayte 'an mevlâk, gloss:dostuna ateş yaktın, yani ona yardım ettin ve onu korudun, source:"و ر ي,B003"}. Böylece duvarların "ardından" savaşanlar, vaat ettikleri çakmağı hiç yakmamış olurlar. Atların yararsız kıvılcımları da bu aileye girer: {ar:نار الحباحب ما أورت الخيل لا ينتفع به, tr:nâru'l-hubâhib, gloss:hubâhib ateşi, atların çıkardığı, işe yaramayan kıvılcımdır, source:"ح ب ب,B011"}. Gerçek ateşin Allah'ın verdiği bir nimet olduğu bir soruyla hatırlatılır: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-ra'eytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Savaş için yakılan ateşi Allah söndürür: {ar:كُلَّمَآ أَوْقَدُوا۟ نَارًا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ, tr:kullemâ evkadû nâren li'l-harbi atfe'ehâ'llâh, gloss:savaş için her ateş yaktıklarında Allah onu söndürdü, source:5:64}.

Aynı boşluk hücum sahnesinde de görülür. Altıncı ayet müminlere {ar:فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍ وَلَا رِكَابٍ, tr:fe-mâ evceftum 'aleyhi min haylin ve lâ rikâb, gloss:onun için ne at ne deve koşturdunuz, source:59:6} der. "Vecîf", dörtnaldan aşağı hızlı bir yürüyüştür {source:"و ج ف,B001"}. Hücum yapılmadan kazanç gelmiştir, çünkü {ar:وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ, tr:ve lâkinna'llâhe yusallıtu rusulehû 'alâ men yeşâ', gloss:fakat Allah elçilerini dilediğinin üzerine musallat eder, source:59:6}. Bedir'de de aynı ilke söylenir: {ar:وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَٰكِنَّ ٱللَّهَ رَمَىٰ, tr:ve mâ rameyte iz rameyte ve lâkinna'llâhe ramâ, gloss:attığın zaman sen atmadın, Allah attı, source:8:17}. Sekizinci ayetin muhacirleri {ar:أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ, tr:ulâike humu's-sâdıkûn, gloss:sadık olanlar onlardır, source:59:8} diye anılır. Bu kelime savaşta hakkını vermek anlamını da taşır: {ar:صدق في القتال إذا وفى حقه, tr:sadaka fi'l-kıtâl, gloss:savaşta hakkını verdiyse "sadık oldu" denir, source:"ص د ق,B004"}. Münafıkların "yalan"ı ise hücuma kalkıp yarıda durmaktır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezebe, gloss:hücuma kalktı sonra "yalan söyledi", yani hücumu sonuna kadar götürmedi, source:"ك ذ ب,B004"}. Böylece sekizinci ve on birinci ayetler bir süvari tablosunun iki yarısı olur. Aynı müminler başka bir surede de aynı kelimeyle kapanır {source:49:15}, ahitlerine sadık kalan adamlar da yine bu fiille anılır {source:33:23}. Münafıkların "savaş olacağını bilsek size uyardık" sözü de yarıda kalan hücumun bir örneğidir {source:3:167}.

Kaynaklar: 59:2 فَأَتَىٰهُمُ ء ت ي B005; 59:2 يَحْتَسِبُوا ح س ب B007; 59:2 ٱلرُّعْبَ ر ع ب B002; 59:1/23/24 ٱلْعَزِيزُ ع ز ز B008; 59:2 ٱلْحَشْرِ ح ش ر B002; 59:15 وَبَالَ و ب ل B001, B002; 59:6 خَيْلٍ خ ي ل B004; 59:11 لَنَنصُرَنَّكُمْ ن ص ر B004; 59:11 لَكَٰذِبُونَ ك ذ ب B006, B004; 59:9 شُحَّ ش ح ح B004, B003; 59:14 وَرَآءِ و ر ي B002, B003; 59:9 يُحِبُّونَ ح ب ب B011; 59:6 أَوْجَفْتُمْ و ج ف B001; 59:8 ٱلصَّٰدِقُونَ ص د ق B004

## Kanallar, havuzlar ve paylaştırma

Altıncı ve yedinci ayetler, savaşsız elde edilen malın kimlere gideceğini anlatır. Bu ayetlerin kelimeleri, yanlarında bir sulama düzeni de duyurur. {ar:وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟, tr:ve mâ âtâkumu'r-resûlu fe-huzûhu ve mâ nehâkum 'anhu fe'ntehû, gloss:Peygamber size neyi verdiyse onu alın, neyi yasakladıysa ondan vazgeçin, source:59:7}. "Vermek" fiilinin ailesinde, bir adamın tarlasına açtığı ark vardır: {ar:الأتي الجدول يؤتيه الرجل إلى أرضه, tr:el-etiyy el-cedvel yu'tîhi'r-raculu ilâ ardıh, gloss:etiyy, adamın toprağına getirdiği arktır, source:"ء ت ي,B004"}. "Almak" fiili suyu tutan çukurun adıdır: {ar:الإخاذة والإخذ ما حفرت لنفسك كهيئة الحوض تمسك الماء أياما, tr:el-ihâza, gloss:ihâza, kendin için kazdığın, suyu günlerce tutan havuz biçimli çukurdur, source:"ء خ ذ,B006"}. "Vazgeçmek" fiili de suyun durduğu gölcüğü anlatır: {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâhe'l-mâ', gloss:su gölcükte durup durulunca "tenâhâ" denir, source:"ن ه ي,B004"}. Aynı ayetteki {ar:أَهْلِ ٱلْقُرَىٰ, tr:ehli'l-kurâ, gloss:kasabalar halkı, source:59:7} ifadesinin "kasaba" kelimesi de havuzda su toplamaktır: {ar:قريت الماء في الحوض أي جمعت, tr:karaytu'l-mâ'e fi'l-havd, gloss:suyu havuzda topladım, source:"ق ر ي,B002"}. Sekizinci ayetteki fakirlerin adı da suyun kanaldan çıktığı yeri anlatır: {ar:الفقير مخرج الماء من القناة, tr:el-fakîr mahracu'l-mâ' mine'l-kanât, gloss:fakîr, suyun kanaldan çıktığı yerdir, source:"ف ق ر,B005"}. Muhacirlerin adı ise büyük havuzdur: {ar:الهجير الحوض الكبير, tr:el-hecîr el-havdu'l-kebîr, gloss:hecîr büyük havuzdur, source:"ه ج ر,B011"}. Bu sahnede su dağılmadan ihtiyacı olan çukurlara yönlendirilir. Ayetin amacı da tam budur: {ar:كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ, tr:key lâ yekûne dûleten beyne'l-ağniyâ'i minkum, gloss:aranızda yalnız zenginler arasında dolaşan bir şey olmasın diye, source:59:7}. "Dûle", elden ele geçip duran şeydir: {ar:الدولة اسم الشيء الذي يتداول, tr:ed-dûle ismu'ş-şey'i'llezî yutedâvel, gloss:dûle, el değiştirip dolaşan şeyin adıdır, source:"د و ل,B001"}. Aynı kökte bir dal, dolaşan şeyin eskiyip yıprandığını söyler: {ar:دال الثوب يدول إذا بلي, tr:dâle's-sevbu yedûlu, gloss:elbise eskiyince "dâle" denir, source:"د و ل,B002"}. Kur'an suyun da böyle paylaştırıldığını söyler: {ar:أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ, tr:enne'l-mâ'e kısmetun beynehum, gloss:suyun aralarında paylaştırılmış olduğunu, source:54:28}. Yedinci ayetteki alıcıların listesi ganimetin beşte biri için de aynen sayılır {source:8:41}.

"Fey'" kelimesinin kendisi de dönüşü anlatır: {ar:أصل الفيء الرجوع, tr:aslu'l-fey' er-rucû', gloss:fey'in aslı geri dönmektir, source:"ف ي ء,B001"}. Mal, asıl sahibine dönen bir gölge gibi geri gelir. Dokuzuncu ayet, Ensar'ın bu malın paylaşılmasında gösterdiği tavrı bir su başı sahnesiyle anlatır. {ar:يُحِبُّونَ مَنْ هَاجَرَ إِلَيْهِمْ, tr:yuhibbûne men hâcera ileyhim, gloss:kendilerine hicret edeni severler, source:59:9}. "Sevmek" fiilinin bir dalında, içerek suya kanmanın ilk aşaması vardır: {ar:أول الري التحبب, tr:evvelu'r-riyy et-tehabbub, gloss:kanmanın başı "tehabbub"dur, source:"ح ب ب,B006"}. {ar:وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةً, tr:ve lâ yecidûne fî sudûrihim hâce, gloss:göğüslerinde bir ihtiyaç duymazlar, source:59:9}. "Göğüs" kelimesi de sudan kanıp dönmeyi anlatır: {ar:الصدر الانصراف عن الورد, tr:es-sadr el-insırâf 'ani'l-vird, gloss:sadr, sudan dönüp ayrılmaktır, source:"ص د ر,B003"}. Onuncu ayette ise sonradan gelenler, kalplerinde bir "ğıll" olmamasını dilerler. Bu kelimenin bir dalı yakıcı susuzluktur: {ar:الغلة والغليل حرارة العطش, tr:el-ğulle ve'l-ğalîl harâratu'l-'ataş, gloss:ğulle ve ğalîl susuzluğun yakıcılığıdır, source:"غ ل ل,B002"}. Başka bir dalı da ganimeti paylaştırmadan saklamaktır: {ar:الغلول في الغنم وهو أن يخفى الشيء فلا يرد إلى القسم, tr:el-ğulûl, gloss:ğulûl, bir şeyi gizleyip paylaştırmaya getirmemektir, source:"غ ل ل,B004"}. Peygamberin bunu yapamayacağı açıkça söylenir: {ar:وَمَا كَانَ لِنَبِىٍّ أَن يَغُلَّ, tr:ve mâ kâne li-nebiyyin en yeğulle, gloss:hiçbir peygambere ganimetten bir şey saklamak yakışmaz, source:3:161}. Paylaşmadan önce susuz kalan kalp ile payı saklayan el böylece aynı kelimede birleşir. Ensar'ın "îsâr"ı (başkasını kendine tercih etmesi) ise tersine çevrilince bencillik olur: {ar:استأثر فلان بالشيء أي استبد به, tr:iste'sera fulânun bi'ş-şey', gloss:o şeyi kendine ayırdı, tek başına aldı, source:"ء ث ر,B006"}. Cimriliğin bir dalı da iki kişinin aynı şeyi kapışmasıdır: {ar:تشاح الرجلان على الأمر إذا أراد كل واحد منهما الفوز به ومنعه من صاحبه, tr:teşâhha'r-raculân, gloss:her biri o şeyi kazanıp ötekinden esirgemek isteyince iki adam "teşâhh" etti, source:"ش ح ح,B002"}. Bu ifadede, surenin yirminci ayetindeki "kazananlar" kelimesi ile ikinci ayetteki "engellemek" fiili birlikte geçer. Sure kazanmayı kapışanlara değil, cimrilikten korunanlara verir. Nefislerin cimriliğe hazır olduğu da söylenir: {ar:وَأُحْضِرَتِ ٱلْأَنفُسُ ٱلشُّحَّ, tr:ve uhdırati'l-enfusu'ş-şuhh, gloss:nefisler cimriliğe hazır kılınmıştır, source:4:128}. Dokuzuncu ayetin son cümlesi başka bir surede aynen tekrarlanır {source:64:16}. Münafıklar ise Allah lütfundan verince cimrilik edip yüz çevirmiştir {source:9:76}.

Kaynaklar: 59:7 ءَاتَىٰكُمُ ء ت ي B004; 59:7 فَخُذُوهُ ء خ ذ B006; 59:7 فَٱنتَهُوا ن ه ي B004; 59:7 ٱلْقُرَىٰ ق ر ي B002; 59:8 لِلْفُقَرَآءِ ف ق ر B005; 59:8 ٱلْمُهَٰجِرِينَ ه ج ر B011; 59:7 دُولَةً د و ل B001, B002; 59:6/7 أَفَآءَ ف ي ء B001; 59:9 يُحِبُّونَ ح ب ب B006; 59:9 صُدُورِهِمْ ص د ر B003; 59:10 غِلًّا غ ل ل B002, B004; 59:9 يُؤْثِرُونَ ء ث ر B006; 59:9 شُحَّ ش ح ح B002

## Yurttan çıkış, ıssızlaşan yurt, hazırlanan konak

Sure iki topluluğun evinden çıkışını anlatır. Birincisi, ikinci ayetteki çıkarılmadır: {ar:أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ, tr:ahrace'llezîne keferû min ehli'l-kitâbi min diyârihim li-evveli'l-haşr, gloss:kitap ehlinden inkâr edenleri ilk sürgünde yurtlarından çıkaran, source:59:2}. "Haşr" kelimesi burada bir topluluğu yerinden çıkarıp sürmek anlamını taşır: {ar:إخراج الجماعة عن مقرهم وإزعاجهم عنه, tr:ihrâcu'l-cemâ'a 'an makarrihim ve iz'âcuhum 'anh, gloss:topluluğu yurdundan çıkarıp oradan sökmek, source:"ح ش ر,B001"}. Bu ifadede, aynı ayetteki "çıkardı" fiili ile "haşr" kelimesi birleşir. Üçüncü ayetteki "celâ" (sürgün) da insanları evlerinden açık alana çıkarmaktır: {ar:أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها, tr:eclaytu'l-kavme 'an menâzilihim, gloss:topluluğu evlerinden çıkardım, yani onları açığa çıkardım, source:"ج ل و,B004"}. İkincisi, sekizinci ayetteki muhacirlerin çıkışıdır: {ar:ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ, tr:ellezîne uhricû min diyârihim ve emvâlihim, gloss:yurtlarından ve mallarından çıkarılanlar, source:59:8}. Hicret evden eve göçmektir: {ar:هاجر القوم من دار إلى دار تركوا الأولى للثانية, tr:hâcera'l-kavmu min dârin ilâ dâr, gloss:topluluk bir yurttan bir yurda göçtü, ilkini ikincisi için bıraktı, source:"ه ج ر,B002"}. Böylece aynı fiil iki çıkışı da anlatır, ama ikisinin sonu farklıdır. Birinciler, yurtlarını kendi elleriyle yıkıp gider. İkinciler ise kendilerine hazırlanmış bir yurda varır: {ar:وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ, tr:ve'llezîne tebevve'u'd-dâra ve'l-îmâne min kablihim, gloss:onlardan önce o yurdu ve imanı yerleşim yeri edinenler, source:59:9}. "Tebevvu'" fiili bir yeri konak edinmektir: {ar:المباءة منزل القوم في كل موضع وتبوأت منزلا وبوأت للرجل منزلا, tr:el-mebâ'e menzilu'l-kavm, gloss:mebâe, topluluğun konağıdır; konak edindim ve adama konak hazırladım, source:"ب و ء,B001"}. Ayetteki dikkat çekici nokta, imanın da yurt gibi konak edinilmesidir. Kur'an hicret edenlere de böyle bir konak vaat eder: {ar:لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةً, tr:le-nubevvi'ennehum fi'd-dunyâ hasene, gloss:onları dünyada güzel bir yere yerleştireceğiz, source:16:41}. Haksız yere yurtlarından çıkarılanlar için ise {ar:وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ, tr:ve le-yensuranna'llâhu men yensuruh, inna'llâhe le-kaviyyun 'azîz, gloss:Allah kendisine yardım edene mutlaka yardım eder; Allah güçlüdür, azîzdir, source:22:40} denir. Bu ayette, sekizinci ayetteki "yardım ederler" ile birinci ayetteki "Azîz" bir araya gelir. Barınak verip yardım edenler de muhacirlerle birlikte anılır {source:8:72}.

Yolun kendisi de suredeki kelimelerde vardır. Yedinci ayetteki {ar:وَٱبْنِ ٱلسَّبِيلِ, tr:ve'bni's-sebîl, gloss:ve yolda kalmış yolcu, source:59:7} ifadesi, yolculukta yolu kesilmiş kişiyi anlatır: {ar:ابن السبيل المسافر الذي انقطع به, tr:ibnu's-sebîl el-musâfir ellezi'nkutı'a bih, gloss:ibnu's-sebîl, yolu kesilmiş yolcudur, source:"س ب ل,B002"}. Beşinci ayetteki "kesmek" fiili bu yolculuğa iki ifadeyle bağlanır. Biri, bineği ölüp azığı biten yolcudur {source:"ق ط ع,B006"}. Öbürü yolcuları soyan eşkıyadır: {ar:قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق, tr:kuttâ'u't-turuk, gloss:yolcuların önünü kesip yolu onlara kapatan yol kesiciler, source:"ق ط ع,B023"}. İkinci ayetteki "ibret alın" fiili de yoldan geçmektir: {ar:رجل عابر سبيل أي مار, tr:raculun 'âbiru sebîl, gloss:yoldan geçen adam, source:"ع ب ر,B001"}. Uzak yolu anlatan kelimeler de surede vardır: dördüncü ayetteki "ayrılık" kelimesinin ailesinde uzun yolculuk {source:"ش ق ق,B005"}, on altıncı ayetteki "Şeytan" kelimesinin ailesinde de evin uzaklığı vardır: {ar:شطنت الدار شطونا إذا بعدت, tr:şatanati'd-dâr, gloss:yurt uzaklaşınca "şatanat" denir, source:"ش ط ن,B001"}.

Geride kalan yurt ise ıssızlaşır. On birinci ayette münafıklar {ar:وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًا, tr:ve lâ nutî'u fîkum ehaden ebedâ, gloss:sizin hakkınızda hiç kimseye asla boyun eğmeyiz, source:59:11} der. "Ebed" kelimesinin ailesinde, sahipleri gidip yaban hayvanlarına kalan ev vardır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:te'ebbede'l-menzil, gloss:ev ıssızlaştı ve yaban hayvanları ona alıştı, source:"ء ب د,B003"}. "Kimse" kelimesi de evle birlikte geçer: {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"}. Yurt kelimesi de yalnız bu tür olumsuz cümlelerde "kimse" anlamı taşır {source:"د و ر,B008"}. Yani "asla" diye verilen söz, yanında boşalmış bir evin sesini taşır. Yedinci ayetteki "zenginler" kelimesi de bir yerde oturmak anlamı taşır: {ar:غني القوم في دارهم أقاموا ومغانيهم منازلهم, tr:ğaniye'l-kavmu fî dârihim, gloss:topluluk yurdunda oturdu; meğânî onların konaklarıdır, source:"غ ن ي,B004"}. Aynı kökte bir deyim de vardır: {ar:كأن لم يغن بالأمس أي كأن لم يكن, tr:ke-en lem yağne bi'l-ems, gloss:sanki dün orada hiç oturmamış, yani hiç yokmuş gibi, source:"غ ن ي,B004"}. Kur'an bu deyimi yok edilen kavimler için kullanır: {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlar gibi, source:11:68}. Bahçe sahnesinde de aynı ifade vardır {source:10:24}. On yedinci ayetteki "ebedî kalıcılar" kelimesi, ailesinde harabeden geriye kalan ocak taşlarını da anlatır: {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid, gloss:uzun süre durdukları için ocak taşlarına havâlid denir, source:"خ ل د,B001"}. Kalıcılık burada artık yaşanan bir ev değil, yıkıntıda kalan taştır. On dokuzuncu ayetteki "unuttular" fiili de göçenlerin ardında bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sakata min menâzili'l-murtahılîn, gloss:nisy, göçenlerin konaklarından düşen değersiz eşyadır, source:"ن س ي,B003"}. Meryem de aynı kelimeyle {ar:وَكُنتُ نَسْيًا مَّنسِيًّا, tr:ve kuntu nesyen mensiyyâ, gloss:unutulup gitmiş bir şey olsaydım, source:19:23} der. Allah'ı unutanlar, kendilerini de unutturulmuş olarak terk edilmiş bir yurdun döküntüsü gibi bulur. İkinci ayetteki "ev" kelimesi de kabir anlamına gelir {source:"ب ي ت,B007"}. Kur'an boşalmış evleri böyle gösterir: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş evleri, source:27:52}. Az kalsın hiç oturulmamış meskenler de vardır {source:28:58}. Kuşatılmış başka bir topluluğun yurdu da müminlere miras kalmıştır {source:33:27}.

Kaynaklar: 59:2/8 أَخْرَجَ / أُخْرِجُوا خ ر ج B001; 59:2 ٱلْحَشْرِ ح ش ر B001; 59:3 ٱلْجَلَآءَ ج ل و B004; 59:8/9 ٱلْمُهَٰجِرِينَ / هَاجَرَ ه ج ر B002; 59:9 تَبَوَّءُو ب و ء B001; 59:7 ٱبْنِ ٱلسَّبِيلِ س ب ل B002; 59:5 قَطَعْتُم ق ط ع B006, B023; 59:2 فَٱعْتَبِرُوا ع ب ر B001; 59:4 شَآقُّوا ش ق ق B005; 59:16 ٱلشَّيْطَٰنِ ش ط ن B001; 59:11 أَبَدًا ء ب د B003; 59:11 أَحَدًا ء ح د B002; 59:2 دِيَٰرِهِمْ د و ر B008; 59:7 ٱلْأَغْنِيَآءِ غ ن ي B004; 59:17 خَٰلِدَيْنِ خ ل د B001; 59:19 نَسُوا ن س ي B003; 59:2 بُيُوتَهُم ب ي ت B007

## Misafir sofrası

Dokuzuncu ayetteki karşılama bir misafir ağırlama sahnesi olarak da işitilir. Yedinci ayetteki "kasabalar" kelimesi, ailesinde misafirin etrafında toplandığı büyük tası anlatır: {ar:المقراة الجفنة سميت لاجتماع الضيف عليها, tr:el-mikrâ el-cefne, gloss:mikrâ, misafirlerin etrafında toplandığı için bu adı alan büyük tastır, source:"ق ر ي,B003"}. Misafire ikram da aynı köktendir: {ar:القرى الإحسان إلى الضيف, tr:el-kırâ el-ihsân ile'd-dayf, gloss:kırâ misafire ikramdır, source:"ق ر ي,B003"}. Yirmi birinci ayetteki "indirmek" fiili de konuğa hazırlanan yemeği anlatır: {ar:النزل ما يهيأ للنزيل, tr:en-nuzul mâ yuheyye'u li'n-nezîl, gloss:nuzul, konuk için hazırlanan şeydir, source:"ن ز ل,B005"}. Kur'an'ın indirilişi böylece hem yağmurun hem de konuğa sunulan sofranın sesini taşır. "Ehl" kelimesi de karşılama sözünün içindedir: {ar:مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش, tr:merhaben ve ehlen, gloss:genişliğe ve ailene geldin, ısın, yabancılık çekme, source:"ء ه ل,B005"}. Dokuzuncu ayet bu karşılamayı açık bir dille söyler: {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ, tr:ve yu'sirûne 'alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri darlık içinde olsalar bile onları kendilerine tercih ederler, source:59:9}. "Esîr" kelimesi, kişinin lütfuyla öne çıkardığı değerli insandır: {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-esîr el-kerîm 'aleyk, gloss:esîr, lütfun ve ikramınla öne geçirdiğin değerli kişidir, source:"ء ث ر,B005"}. Bu ifadedeki "fazl" (lütuf) kelimesi sekizinci ayette de geçer. Muhacirler Allah'tan lütuf ararken, Ensar onlara kendi lütfundan verir. "Fazl" da birine kendi fazlasından vermektir {source:"ف ض ل,B003"}. Yedinci ayetteki "yoksullar" kelimesinin ailesinde ise insanın yanında ısındığı ateş vardır {source:"س ك ن,B004"}. On sekizinci ayetteki "yarın" kelimesi de sabah yemeğidir {source:"غ د و,B004"}. İbrahim'in misafir ağırlaması bu sahnenin Kur'an'daki örneğidir: {ar:فَجَآءَ بِعِجْلٍ سَمِينٍ, tr:fe-câe bi-'iclin semîn, gloss:semiz bir buzağı getirdi, source:51:26}, {ar:فَقَرَّبَهُۥٓ إِلَيْهِمْ, tr:fe-karrabehû ileyhim, gloss:onu önlerine koydu, source:51:27}. Dokuzuncu ayetteki tercih de sevilen şeyden yedirmektir: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا, tr:ve yut'ımûne't-ta'âme 'alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, sevdikleri halde yoksula, yetime ve esire yedirirler, source:76:8}. Orada da karşılık beklenmez {source:76:9}. On beşinci ayette ise tatma tersine döner. Tatmak önce yiyeceği tatmaktır {source:"ذ و ق,B001"}. Önceki topluluk ise sofrada değil, kendi işlerinin vebalinde tat alır.

Kaynaklar: 59:7 ٱلْقُرَىٰ ق ر ي B003; 59:21 أَنزَلْنَا ن ز ل B005; 59:2/7 أَهْلِ ء ه ل B005; 59:9 يُؤْثِرُونَ ء ث ر B005; 59:8 فَضْلًا ف ض ل B003; 59:7 ٱلْمَسَٰكِينِ س ك ن B004; 59:18 لِغَدٍ غ د و B004; 59:15 ذَاقُوا ذ و ق B001

## Kırık bel ve onu saran el

Sekizinci ayetteki "fakirler" kelimesi, kökünde beli kırılmış insanı anlatır: {ar:أصل الفقير المكسور الفقار, tr:aslu'l-fakîr el-meksûru'l-fakâr, gloss:fakîrin aslı, omurları kırılmış olandır, source:"ف ق ر,B001"}. Belin kemiklerini kıran felakete de bu adla denir {source:"ف ق ر,B008"}. Muhacirler yurtlarından ve mallarından çıkarılmıştır. Onların fakirliği, beli kırılmış bir insanın ayakta duramamasına benzer. Yirmi üçüncü ayetteki "Cebbâr" ismi bu kırığın karşısına konur: {ar:جبرت العظم فجبر, tr:cebertu'l-'azme fe-cebera, gloss:kemiği sardım, o da kaynadı, source:"ج ب ر,B001"}. Aynı fiil yoksulluğu gidermek için de kullanılır: {ar:جبرت فاقة الرجل إذا أغنيته, tr:cebertu fâkate'r-racul, gloss:adamın yokluğunu giderdim, yani onu zengin ettim, source:"ج ب ر,B001"}. Kırık kemiğe sarılan tahta da bu köktendir {source:"ج ب ر,B005"}. Bu ifadeler, sekizinci ayetin "fakirler"i, yedinci ayetin "zenginler"i ve yirmi üçüncü ayetin "Cebbâr" ismini birbirine bağlar. Fey' malının yoksullara ayrılması, kırık belin sarılmasıdır. Bu ismin anlamı da yalnız ezen bir güç değil, kırığı saran bir güçtür. Kur'an da {ar:وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ, tr:va'llâhu'l-ğaniyyu ve entumu'l-fukarâ', gloss:Allah zengindir, siz ise fakirsiniz, source:47:38} der. Aynı ayet cimrilik edenin ancak kendine cimrilik ettiğini de söyler {source:47:38}. Yirmi dördüncü ayetteki "Bâri'" ismi ile on altıncı ayetteki "uzağım" kelimesi aynı köktendir. Kökün bir dalı hastalıktan kurtulmaktır: {ar:البرء السلامة من السقم, tr:el-bur' es-selâme mine's-sekam, gloss:bur', hastalıktan kurtulup sağlığa kavuşmaktır, source:"ب ر ء,B003"}. Şeytan "ben senden uzağım" der ve kendini kurtarmaya çalışır. Sağlık ve kurtuluş ise yaratan Bâri' isminde kalır. Yirmi üçüncü ayetteki "Selâm" ismi de sağlığın kendisidir: {ar:السلامة أن يسلم الإنسان من العاهة والأذى, tr:es-selâme, gloss:selâmet, insanın sakatlıktan ve eziyetten kurtulmasıdır, source:"س ل م,B001"}.

Kaynaklar: 59:8 لِلْفُقَرَآءِ ف ق ر B001, B008; 59:23 ٱلْجَبَّارُ ج ب ر B001, B005; 59:16/24 بَرِىٓءٌ / ٱلْبَارِئُ ب ر ء B003; 59:23 ٱلسَّلَٰمُ س ل م B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

