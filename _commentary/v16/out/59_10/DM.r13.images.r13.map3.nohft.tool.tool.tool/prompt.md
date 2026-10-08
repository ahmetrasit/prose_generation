Focus: 59:10. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_10/D.r13/context.md =====
# 59:10 — focus

وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلَّذِينَ | ٱلَّذِى |  | CONJ;REL |
| 2 | جَآءُو | جَآءَ | ج ي ء | V;PRON |
| 3 | مِنۢ | مِن |  | P |
| 4 | بَعْدِهِمْ | بَعْد | ب ع د | N;PRON |
| 5 | يَقُولُونَ | قَالَ | ق و ل | V;PRON |
| 6 | رَبَّنَا | رَبّ | ر ب ب | N;PRON |
| 7 | ٱغْفِرْ | غَفَرَ | غ ف ر | V |
| 8 | لَنَا |  |  | P;PRON |
| 9 | وَلِإِخْوَٰنِنَا | أَخ | ء خ و | CONJ;P;N;PRON |
| 10 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 11 | سَبَقُونَا | سَبَقَ | س ب ق | V;PRON |
| 12 | بِٱلْإِيمَٰنِ | إِيمَٰن | ء م ن | P;DET;N |
| 13 | وَلَا | لَا |  | CONJ;NEG |
| 14 | تَجْعَلْ | جَعَلَ | ج ع ل | V |
| 15 | فِى | فِى |  | P |
| 16 | قُلُوبِنَا | قَلْب | ق ل ب | N;PRON |
| 17 | غِلًّا | غِلّ | غ ل ل | N |
| 18 | لِّلَّذِينَ | ٱلَّذِى |  | P;REL |
| 19 | ءَامَنُوا۟ | ءَامَنَ | ء م ن | V;PRON |
| 20 | رَبَّنَآ | رَبّ | ر ب ب | N;PRON |
| 21 | إِنَّكَ | إِنّ |  | ACC;PRON |
| 22 | رَءُوفٌ | رَءُوف | ر ء ف | N |
| 23 | رَّحِيمٌ | رَّحِيم | ر ح م | ADJ |


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
- 59:10 ◀ focus وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ
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


===== _commentary/v16/work/59_10/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ي ء (root_000281) — identity root of جَآءُو (w2)

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

## ج ي ء (root_000282) — identity root of جَآءُو (w2)

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ب ع د (root_000131) — identity root of بَعْدِهِمْ (w4)

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

## ق و ل (root_001272) — identity root of يَقُولُونَ (w5)

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

## ر ب ب (root_000532) — identity root of رَبَّنَا (w6)

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

## غ ف ر (root_001096) — identity root of ٱغْفِرْ (w7)

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

## ء خ و (root_000020) — identity root of وَلِإِخْوَٰنِنَا (w9)

- **B001** kardeşlik ve kardeş sayılan kişiler — erkek kardeş · kız kardeş · doğumdan kardeşler · kardeşler; özellikle kardeş sayılan arkadaşlar · kardeş olmak · birbirini kardeş saymak; kardeşlik bağı kurmak · birini kardeş edinmek · o kişi senin kardeşin değildir
  الأخ أصله أخو (sihah)؛ أكثر ما يستعمل الإخوان في الأصدقاء والإخوة في الولادة (sihah)؛ أخت بينة الأخوة (sihah)؛ الأخت أصلها التأنيث (ayn)
- **B002** bağlama halkası veya gözetilen bağ — hayvan bağlama halkası veya bağı · hayvan için bağlama halkası veya bağı yapmak · gözetilmesi gereken ilişki, hak veya yükümlülük bağı
  وكذلك الآخية (maqayis)؛ الآخية واحدة الأواخي (sihah)؛ تشد إليه الدابة (sihah)؛ الآخية أيضا الحرمة والذمة (sihah)
- **B003** özenle araştırıp yönelmek [kalıp] — bir şeyi özenle araştırıp hedef edinmek
  وتأخيت الشيء أيضا مثل تحريته (sihah)

## س ب ق (root_000671) — identity root of سَبَقُونَا (w11)

- **B001** harekette ya da işte öne geçme ve yarışarak ön alma — koşuda, işte ya da bir şeyde başkasının önüne geçmek · öne geçme; koşuda ya da işte önce gelme · bir işte önceden kazanılmış öncelik · yarışma; koşuda ve benzeri bir alanda birbirini geçmeye çalışma · yarışmak ya da bir şeye önce davranmak · atış yarışmasına gitmek · kapıya ilk varmak için birbirinden önce davranmak · yolu aşıp geçerek yönünü kaybetmek · yarışta başa geçen at ya da benzeri varlık · iyi işlerle ödüle önden koşanlar · önceden kesinleşip yürürlüğe girmek
  أصل واحد صحيح يدل على التقديم (maqayis)؛ السبق القدمة في الجري وفي الأمر (ayn;tahdhib)؛ وسبق يسبق سبقا (jamhara)؛ سابقته فسبقته سبقا واستبقنا في العدو أي تسابقنا (sihah)؛ أصل السبق التقدم في السير والاستباق التسابق (mufradat)
- **B002** yarışta ortaya konup kazananın aldığı pay — yarışta ya da atışta ortaya konup kazananın aldığı pay · yarış payını almak ya da yarış payını vermek · ortaya konan yarış payını kazandı
  السبق الخطر الذي يأخذه السابق (maqayis)؛ السبق الخطر يوضع بين أهل السباق (ayn;sihah)؛ السبق الرهن (jamhara)؛ الخطر الذي يوضع في النضال والرهان في الخيل فمن سبق أخذه (tahdhib)
- **B003** avcı kuşun ayaklarına takılan iki bağ — avcı kuşun ayaklarına takılan iki bağ · avcı kuşun ayaklarına bu iki bağı takmak
  السباقان قيد أرجل الطائر الجارح بسير أو خيط (ayn)؛ سباقا البازي قيداه من سير أو غيره (sihah)؛ السباقان في رجل الطائر الجارح قيداه من سير أو خيط وسبقت البازي إذا جعلت السباقان في رجليه (tahdhib)
- **B004** yakalanmaktan kurtulacak kadar öne kaçma — takip edenin elinden kaçıp kurtulmak · kaçıp kurtulmuş olmamak; takip edeni aşamamış olmak
  وما نحن بمسبوقين أي لا يفوتوننا؛ ولا يحسبن الذين كفروا سبقوا؛ وما كانوا سابقين (mufradat)

## ء م ن (root_000054) — identity root of بِٱلْإِيمَٰنِ (w12)

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ج ع ل (root_000248) — identity root of تَجْعَلْ (w14)

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

## ق ل ب (root_001248) — identity root of قُلُوبِنَا (w16)

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

## غ ل ل (root_001102) — identity root of غِلًّا (w17)

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

## ر ء ف (root_000530) — identity root of رَءُوفٌ (w22)

- **B001** yüreği incelten esirgeyiş — yüreği incelten esirgeyiş · esirgeyiş ve yürek yumuşaklığı · ona acıyıp onu esirgemek · acıma ve esirgeyiş · çok esirgeyen, yumuşak yürekli · çok esirgeyen, yumuşak yürekli · esirgeyen, yumuşak yürekli · acıyan ve esirgeyen
  كلمة واحدة تدل على رقة ورحمة، وهي الرأفة (maqayis); الرأفة: أشد الرحمة (sihah); الرأفة: الرحمة (mufradat)

## ر ح م (root_000552) — identity root of رَّحِيمٌ (w23)

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ECHO ق ل ل (root_001251) — for يَقُولُونَ (w5): withheld observed target; not identity

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

## ECHO ر ب و (root_000537) — for رَبَّنَا (w6): withheld observed target; not identity

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

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:10, and ## Buluşmalar) =====
## Kanallar, havuzlar ve paylaştırma

Altıncı ve yedinci ayetler, savaşsız elde edilen malın kimlere gideceğini anlatır. Bu ayetlerin kelimeleri, yanlarında bir sulama düzeni de duyurur. {ar:وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟, tr:ve mâ âtâkumu'r-resûlu fe-huzûhu ve mâ nehâkum 'anhu fe'ntehû, gloss:Peygamber size neyi verdiyse onu alın, neyi yasakladıysa ondan vazgeçin, source:59:7}. "Vermek" fiilinin ailesinde, bir adamın tarlasına açtığı ark vardır: {ar:الأتي الجدول يؤتيه الرجل إلى أرضه, tr:el-etiyy el-cedvel yu'tîhi'r-raculu ilâ ardıh, gloss:etiyy, adamın toprağına getirdiği arktır, source:"ء ت ي,B004"}. "Almak" fiili suyu tutan çukurun adıdır: {ar:الإخاذة والإخذ ما حفرت لنفسك كهيئة الحوض تمسك الماء أياما, tr:el-ihâza, gloss:ihâza, kendin için kazdığın, suyu günlerce tutan havuz biçimli çukurdur, source:"ء خ ذ,B006"}. "Vazgeçmek" fiili de suyun durduğu gölcüğü anlatır: {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâhe'l-mâ', gloss:su gölcükte durup durulunca "tenâhâ" denir, source:"ن ه ي,B004"}. Aynı ayetteki {ar:أَهْلِ ٱلْقُرَىٰ, tr:ehli'l-kurâ, gloss:kasabalar halkı, source:59:7} ifadesinin "kasaba" kelimesi de havuzda su toplamaktır: {ar:قريت الماء في الحوض أي جمعت, tr:karaytu'l-mâ'e fi'l-havd, gloss:suyu havuzda topladım, source:"ق ر ي,B002"}. Sekizinci ayetteki fakirlerin adı da suyun kanaldan çıktığı yeri anlatır: {ar:الفقير مخرج الماء من القناة, tr:el-fakîr mahracu'l-mâ' mine'l-kanât, gloss:fakîr, suyun kanaldan çıktığı yerdir, source:"ف ق ر,B005"}. Muhacirlerin adı ise büyük havuzdur: {ar:الهجير الحوض الكبير, tr:el-hecîr el-havdu'l-kebîr, gloss:hecîr büyük havuzdur, source:"ه ج ر,B011"}. Bu sahnede su dağılmadan ihtiyacı olan çukurlara yönlendirilir. Ayetin amacı da tam budur: {ar:كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ, tr:key lâ yekûne dûleten beyne'l-ağniyâ'i minkum, gloss:aranızda yalnız zenginler arasında dolaşan bir şey olmasın diye, source:59:7}. "Dûle", elden ele geçip duran şeydir: {ar:الدولة اسم الشيء الذي يتداول, tr:ed-dûle ismu'ş-şey'i'llezî yutedâvel, gloss:dûle, el değiştirip dolaşan şeyin adıdır, source:"د و ل,B001"}. Aynı kökte bir dal, dolaşan şeyin eskiyip yıprandığını söyler: {ar:دال الثوب يدول إذا بلي, tr:dâle's-sevbu yedûlu, gloss:elbise eskiyince "dâle" denir, source:"د و ل,B002"}. Kur'an suyun da böyle paylaştırıldığını söyler: {ar:أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ, tr:enne'l-mâ'e kısmetun beynehum, gloss:suyun aralarında paylaştırılmış olduğunu, source:54:28}. Yedinci ayetteki alıcıların listesi ganimetin beşte biri için de aynen sayılır {source:8:41}.

"Fey'" kelimesinin kendisi de dönüşü anlatır: {ar:أصل الفيء الرجوع, tr:aslu'l-fey' er-rucû', gloss:fey'in aslı geri dönmektir, source:"ف ي ء,B001"}. Mal, asıl sahibine dönen bir gölge gibi geri gelir. Dokuzuncu ayet, Ensar'ın bu malın paylaşılmasında gösterdiği tavrı bir su başı sahnesiyle anlatır. {ar:يُحِبُّونَ مَنْ هَاجَرَ إِلَيْهِمْ, tr:yuhibbûne men hâcera ileyhim, gloss:kendilerine hicret edeni severler, source:59:9}. "Sevmek" fiilinin bir dalında, içerek suya kanmanın ilk aşaması vardır: {ar:أول الري التحبب, tr:evvelu'r-riyy et-tehabbub, gloss:kanmanın başı "tehabbub"dur, source:"ح ب ب,B006"}. {ar:وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةً, tr:ve lâ yecidûne fî sudûrihim hâce, gloss:göğüslerinde bir ihtiyaç duymazlar, source:59:9}. "Göğüs" kelimesi de sudan kanıp dönmeyi anlatır: {ar:الصدر الانصراف عن الورد, tr:es-sadr el-insırâf 'ani'l-vird, gloss:sadr, sudan dönüp ayrılmaktır, source:"ص د ر,B003"}. Onuncu ayette ise sonradan gelenler, kalplerinde bir "ğıll" olmamasını dilerler. Bu kelimenin bir dalı yakıcı susuzluktur: {ar:الغلة والغليل حرارة العطش, tr:el-ğulle ve'l-ğalîl harâratu'l-'ataş, gloss:ğulle ve ğalîl susuzluğun yakıcılığıdır, source:"غ ل ل,B002"}. Başka bir dalı da ganimeti paylaştırmadan saklamaktır: {ar:الغلول في الغنم وهو أن يخفى الشيء فلا يرد إلى القسم, tr:el-ğulûl, gloss:ğulûl, bir şeyi gizleyip paylaştırmaya getirmemektir, source:"غ ل ل,B004"}. Peygamberin bunu yapamayacağı açıkça söylenir: {ar:وَمَا كَانَ لِنَبِىٍّ أَن يَغُلَّ, tr:ve mâ kâne li-nebiyyin en yeğulle, gloss:hiçbir peygambere ganimetten bir şey saklamak yakışmaz, source:3:161}. Paylaşmadan önce susuz kalan kalp ile payı saklayan el böylece aynı kelimede birleşir. Ensar'ın "îsâr"ı (başkasını kendine tercih etmesi) ise tersine çevrilince bencillik olur: {ar:استأثر فلان بالشيء أي استبد به, tr:iste'sera fulânun bi'ş-şey', gloss:o şeyi kendine ayırdı, tek başına aldı, source:"ء ث ر,B006"}. Cimriliğin bir dalı da iki kişinin aynı şeyi kapışmasıdır: {ar:تشاح الرجلان على الأمر إذا أراد كل واحد منهما الفوز به ومنعه من صاحبه, tr:teşâhha'r-raculân, gloss:her biri o şeyi kazanıp ötekinden esirgemek isteyince iki adam "teşâhh" etti, source:"ش ح ح,B002"}. Bu ifadede, surenin yirminci ayetindeki "kazananlar" kelimesi ile ikinci ayetteki "engellemek" fiili birlikte geçer. Sure kazanmayı kapışanlara değil, cimrilikten korunanlara verir. Nefislerin cimriliğe hazır olduğu da söylenir: {ar:وَأُحْضِرَتِ ٱلْأَنفُسُ ٱلشُّحَّ, tr:ve uhdırati'l-enfusu'ş-şuhh, gloss:nefisler cimriliğe hazır kılınmıştır, source:4:128}. Dokuzuncu ayetin son cümlesi başka bir surede aynen tekrarlanır {source:64:16}. Münafıklar ise Allah lütfundan verince cimrilik edip yüz çevirmiştir {source:9:76}.

Kaynaklar: 59:7 ءَاتَىٰكُمُ ء ت ي B004; 59:7 فَخُذُوهُ ء خ ذ B006; 59:7 فَٱنتَهُوا ن ه ي B004; 59:7 ٱلْقُرَىٰ ق ر ي B002; 59:8 لِلْفُقَرَآءِ ف ق ر B005; 59:8 ٱلْمُهَٰجِرِينَ ه ج ر B011; 59:7 دُولَةً د و ل B001, B002; 59:6/7 أَفَآءَ ف ي ء B001; 59:9 يُحِبُّونَ ح ب ب B006; 59:9 صُدُورِهِمْ ص د ر B003; 59:10 غِلًّا غ ل ل B002, B004; 59:9 يُؤْثِرُونَ ء ث ر B006; 59:9 شُحَّ ش ح ح B002

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

## Bağlar, köstekler, ipler

On dördüncü ayetteki "akıl" kelimesi, kale anlamının yanında deveyi bağlamak anlamını da taşır: {ar:عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط, tr:'akaltu'l-ba'îr, gloss:devenin ayağını ipiyle bağladım; ikâl bağdır, source:"ع ق ل,B002"}. Akıl etmeyen bir topluluk, bağı olmayan bir sürü gibidir. Kalpleri dağınık olanlar ip tutmaz. Dördüncü ve yedinci ayetlerdeki {ar:شَدِيدُ ٱلْعِقَابِ, tr:şedîdu'l-'ikâb, gloss:cezası çetin, source:59:4} ifadesi de bir bağlama işini taşır: {ar:عقبت الرمح شددته بالعقب, tr:'akabtu'r-rumh, gloss:mızrağı sinirle sıkıca bağladım, source:"ع ق ب,B001"}. "Şiddet" de düğümü sıkmaktır {source:"ش د د,B001"}. Bu ceza kaçana gevşemeyen bir sinir bağı gibi sarılır. Onuncu ve on birinci ayetlerdeki "kardeşler" kelimesi, hayvanın bağlandığı kazığı da adlandırır: {ar:الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة, tr:el-âhiyye, gloss:âhiyye, hayvanın bağlandığı kazıktır; aynı zamanda saygınlık ve ahittir, source:"ء خ و,B002"}. Sure iki tür kardeşlik gösterir. Onuncu ayette müminler {ar:رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا, tr:rabbena'ğfir lenâ ve li-ihvâninâ, gloss:Rabbimiz, bizi ve kardeşlerimizi bağışla, source:59:10} diye dua eder. On birinci ayette ise münafıklar {ar:يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟, tr:yekûlûne li-ihvânihimu'llezîne keferû, gloss:inkâr eden kardeşlerine diyorlar, source:59:11}. Birinci bağ kazığa sağlam bağlıdır, ikincisi kriz anında çözülür. Kur'an müminlere sağlam bir ip gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Bu ayette, on dördüncü ayetteki "toplu" kelimesi bir ipe bağlanmış olur. Kitap ehli için de iki ip anılır {source:3:112}. On altıncı ayetteki "Şeytan" kelimesi de ip ailesindendir: {ar:الشطن الحبل الطويل الشديد الفتل يستقى به, tr:eş-şatan el-hablu't-tavîl, gloss:şatan, su çekilen uzun, sıkı bükülmüş iptir, source:"ش ط ن,B002"}. Bu kökte ayrıca birini niyetinin yönünden saptırmak da vardır {source:"ش ط ن,B003"}. Şeytan uzun bir iple insanı derin bir kuyuya indirir, sonra ipi bırakır. Kendi sözüyle de, insanlar üzerinde bir gücü olmadığını, onları kurtaramayacağını söyler {source:14:22}. Onuncu ayetteki "ğıll" kelimesi, başka bir harekeyle, elleri boyna bağlayan demir halkadır: {ar:الغل مختص بما يقيد به فيجعل الأعضاء وسطه, tr:el-ğull, gloss:ğull, uzuvları ortasına alarak bağlayan bukağıdır, source:"غ ل ل,B006"}. On dördüncü ayetteki "toplu" kelimesi de aynı bukağıyı adlandırır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull, gloss:câmia bukağıdır, çünkü elleri boyuna birleştirir, source:"ج م ع,B008"}. Böylece kalpteki kin ile ellerdeki bukağı aynı kökten ses verir. Toplu sanılan kalabalık da birbirine bukağıyla bağlanmış olur. Kur'an bukağıyı da gösterir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu da bukağılayın, source:69:30}. Birinci ve yirmi dördüncü ayetlerdeki "Hakîm" ismi de, ailesinde atın çenesini saran gem halkasıdır {source:"ح ك م,B006"}. On birinci ayetteki "boyun eğmek" fiili de dizgine kolay uyan atı anlatır {source:"ط و ع,B001"}. Münafıklar "kimseye boyun eğmeyiz" derken, aslında gemsiz kalırlar.

Kaynaklar: 59:14 يَعْقِلُونَ ع ق ل B002; 59:4/7 شَدِيدُ ٱلْعِقَابِ ع ق ب B001, ش د د B001; 59:10/11 إِخْوَٰن ء خ و B002; 59:16 ٱلشَّيْطَٰنِ ش ط ن B002, B003; 59:10 غِلًّا غ ل ل B006; 59:14 جَمِيعًا ج م ع B008; 59:1/24 ٱلْحَكِيمُ ح ك م B006; 59:11 نُطِيعُ ط و ع B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

