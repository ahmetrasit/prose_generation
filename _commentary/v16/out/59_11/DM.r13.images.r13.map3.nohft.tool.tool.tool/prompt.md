Focus: 59:11. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_11/D.r13/context.md =====
# 59:11 — focus

۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟ يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًۭا وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَلَمْ | لَم |  | INTG;NEG |
| 2 | تَرَ | رَءَا | ر ء ي | V |
| 3 | إِلَى | إِلَىٰ |  | P |
| 4 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 5 | نَافَقُوا۟ | نَافَقُ | ن ف ق | V;PRON |
| 6 | يَقُولُونَ | قَالَ | ق و ل | V;PRON |
| 7 | لِإِخْوَٰنِهِمُ | أَخ | ء خ و | P;N;PRON |
| 8 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 9 | كَفَرُوا۟ | كَفَرَ | ك ف ر | V;PRON |
| 10 | مِنْ | مِن |  | P |
| 11 | أَهْلِ | أَهْل | ء ه ل | N |
| 12 | ٱلْكِتَٰبِ | كِتَٰب | ك ت ب | DET;N |
| 13 | لَئِنْ | إِن |  | EMPH;COND |
| 14 | أُخْرِجْتُمْ | أَخْرَجَ | خ ر ج | V;PRON |
| 15 | لَنَخْرُجَنَّ | خَرَجَ | خ ر ج | EMPH;V |
| 16 | مَعَكُمْ | مَع |  | LOC;PRON |
| 17 | وَلَا | لَا |  | CONJ;NEG |
| 18 | نُطِيعُ | أَطَاعَ | ط و ع | V |
| 19 | فِيكُمْ | فِى |  | P;PRON |
| 20 | أَحَدًا | أَحَد | ء ح د | N |
| 21 | أَبَدًا | أَبَدًا | ء ب د | T |
| 22 | وَإِن | إِن |  | CONJ;COND |
| 23 | قُوتِلْتُمْ | قَٰتَلَ | ق ت ل | V;PRON |
| 24 | لَنَنصُرَنَّكُمْ | نَصَرَ | ن ص ر | EMPH;V;PRON |
| 25 | وَٱللَّهُ | ٱللَّه | ء ل ه | REM;PN |
| 26 | يَشْهَدُ | شَهِدَ | ش ه د | V |
| 27 | إِنَّهُمْ | إِنّ |  | ACC;PRON |
| 28 | لَكَٰذِبُونَ | كَٰذِب | ك ذ ب | EMPH;N |


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
- 59:11 ◀ focus ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟ يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًۭا وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ
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


===== _commentary/v16/work/59_11/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ء ي (root_000531) — identity root of تَرَ (w2)

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

## ن ف ق (root_001537) — identity root of نَافَقُوا۟ (w5)

- **B001** tükenip sona erme; özel kullanımlarda alıcı bulma, çabuk kesilme veya yüzeyden ayrılma — hayvan öldü · tükendi, sona erdi · fiyat veya satış canlandı, mal alıcı buldu · topluluğun pazarı canlandı, malları alıcı buldu · eşi bulunmayan kadına evlenme isteğiyle başvuranlar çoğaldı · koşusu çabuk kesilen at · kesintiye uğrayan gidiş · yaranın kabuğu soyuldu · develerin semirmeden dolayı tüyleri döküldü · insanlara söven kişi karşılığında sövgü görür ve onurunu diline düşürür
  نفقت الدابة نفوقا أي ماتت (maqayis;ayn;sihah;tahdhib;mufradat); نفق الشيء فني ونفد (maqayis;sihah;tahdhib;mufradat); نفق السعر أو البيع نفاقا وكثر مشتروه (maqayis;ayn;sihah;tahdhib;mufradat); فرس نفق الجري وسير نفق سريع الانقطاع (maqayis;sihah;tahdhib); نفق الجرح إذا انقشر وانتثرت الأوبار عن سمن (tahdhib)
- **B002** bir şeyi gider olarak elden çıkarma; özel kullanımda elindekini tüketip yoksullaşma — geçim için yapılan gider; harcanan şey · harcadı, elden çıkardı · adam malı tükenince yoksullaştı · çok harcayan kişi
  النَّفَقَة لأنها تمضي لوجهها (maqayis); النَّفَقَة ما أنفقت واستنفقت على العيال ونفسك (ayn;tahdhib); أنفقت الدرهم من النَّفَقَة ورجل منقاق كثير النَّفَقَة (sihah); الإنفاق قد يكون في المال وفي غيره واجبا وتطوعا (mufradat); أنفق الرجل افتقر وذهب ما عنده أو ماله (maqayis;sihah;tahdhib;mufradat)
- **B003** başka bir yere açılan yer altı geçidi ve kemirgen yuvasındaki gizli çıkış — çıkışı bulunan yer altı geçidi · kemirgen yuvasındaki inceltilmiş gizli çıkış · kemirgen yuvasındaki gizli çıkış · gizli çıkıştan dışarı çıktı · kemirgeni sıkıştırıp gizli çıkışından kaçırdık · kemirgen gizli çıkışına girdi
  النفق سرب في الأرض له مخلص إلى مكان (maqayis;ayn;sihah;tahdhib); النفق الطريق النافذ والسرب في الأرض النافذ فيه (mufradat); النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج (maqayis;ayn;sihah;tahdhib); بعضهم يسمي النافقاء النَّفَقَة (ayn;sihah;tahdhib)
- **B004** içindeki inanç veya tutumun tersini göstererek bağlı görünme — içindekinin tersini gösterme ve inançta ikiyüzlülük · içindekinden başkasını göstererek ikiyüzlü davrandı · içinde sakladığının tersini gösteren kimse
  النفاق لأن صاحبه يكتم خلاف ما يظهر (maqayis); النفاق الخلاف والكفر والفعل نافق نفاقا (ayn); ومنه اشتقاق المنافق في الدين (sihah); سمي المنافق منافقا للنفق وهو السرب في الأرض (tahdhib); النفاق الدخول في الشرع من باب والخروج عنه من باب (mufradat)

## ق و ل (root_001272) — identity root of يَقُولُونَ (w6)

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

## ء خ و (root_000020) — identity root of لِإِخْوَٰنِهِمُ (w7)

- **B001** kardeşlik ve kardeş sayılan kişiler — erkek kardeş · kız kardeş · doğumdan kardeşler · kardeşler; özellikle kardeş sayılan arkadaşlar · kardeş olmak · birbirini kardeş saymak; kardeşlik bağı kurmak · birini kardeş edinmek · o kişi senin kardeşin değildir
  الأخ أصله أخو (sihah)؛ أكثر ما يستعمل الإخوان في الأصدقاء والإخوة في الولادة (sihah)؛ أخت بينة الأخوة (sihah)؛ الأخت أصلها التأنيث (ayn)
- **B002** bağlama halkası veya gözetilen bağ — hayvan bağlama halkası veya bağı · hayvan için bağlama halkası veya bağı yapmak · gözetilmesi gereken ilişki, hak veya yükümlülük bağı
  وكذلك الآخية (maqayis)؛ الآخية واحدة الأواخي (sihah)؛ تشد إليه الدابة (sihah)؛ الآخية أيضا الحرمة والذمة (sihah)
- **B003** özenle araştırıp yönelmek [kalıp] — bir şeyi özenle araştırıp hedef edinmek
  وتأخيت الشيء أيضا مثل تحريته (sihah)

## ك ف ر (root_001307) — identity root of كَفَرُوا۟ (w9)

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

## ء ه ل (root_000064) — identity root of أَهْلِ (w11)

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

## ك ت ب (root_001283) — identity root of ٱلْكِتَٰبِ (w12)

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

## خ ر ج (root_000400) — identity root of أُخْرِجْتُمْ (w14)

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

## ط و ع (root_000956) — identity root of نُطِيعُ (w18)

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

## ء ح د (root_000017) — identity root of أَحَدًا (w20)

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

## ء ب د (root_000004) — identity root of أَبَدًا (w21)

- **B001** sonsuz süre ve kalıcı kılma — sonsuz zaman, çok uzun süre · sonsuza dek, kesintisiz olarak · çağlar boyunca, sonsuza dek · bütün zaman boyunca · kalıcı kılma · sürekli kılınmış, devredilemez · sonsuza dek veya çok uzun süre kalmak
  طول المدة (maqayis)؛ الأبد الدهر (maqayis;sihah)؛ أبد الآبدين وأبد الدهر (tahdhib)؛ الأبد الدائم والتأبيد التخليد (sihah)؛ مدة الزمان الممتد (mufradat)؛ وقفا مؤبدا وتأبيدا (tahdhib)
- **B002** yabanıllaşıp insandan ürkme — devenin yabanıllaşması · hayvanın yabanıllaşıp insandan ürkmesi · yabani ve ürkek hayvanlar · yabani inek
  تأبد البعير توحش (maqayis;mufradat)؛ أوابد كأوابد الوحش (maqayis;tahdhib)؛ أبدت البهيمة أي توحشت (sihah)؛ توحشت ونفرت من الإنس (tahdhib)؛ الوحشيات (mufradat)
- **B003** terk edilip ıssızlaşmak [kalıp] — evin terk edilip ıssızlaşması ve yabani hayvanlara kalması
  تأبد المنزل خلا (maqayis)؛ تأبد المنزل أي أقفر وألفته الوحوش (sihah)؛ خلا منها أهلها خلفتهم الوحش بها قد تأبدت (tahdhib)
- **B004** her yıl doğuran dişi — her yıl doğuran dişi eşek, kısrak veya köle kadın
  الإبد ذات النتاج من المال كالأمة والفرس والأتان (maqayis)؛ الابد الولود من أمة أو أتان (sihah)؛ أتان إبد في كل عام تلد (tahdhib)
- **B005** yüzün lekelenip sertleşmesi [kalıp] — yüzün lekelenmesi, sertleşmesi veya öfkeden değişmesi
  تأبد وجهه كلف (maqayis)؛ تأبد وجه فلان توحش وقد فسر بغضب (mufradat)
- **B006** bir yerde kalıp ayrılmama — bir yerde kalıp oradan ayrılmamak · kış yaz aynı arazide kalan kuşlar
  أبد بالمكان أي أقام به (sihah)؛ أبدت بالمكان إذا أقمت به ولم تبرحه (tahdhib)؛ الطير المقيمة بأرض شتاءها وصيفها أوابد (tahdhib)
- **B007** uzun süre anılan olağanüstü olay — uzun süre anılan olağanüstü iş veya olay · unutulmayacak kadar sıra dışı bir iş yapmak
  الأبدة الفعلة تبقى على الأبد (maqayis)؛ جاء فلان بآبدة أي بداهية يبقى ذكرها على الأبد (sihah)
- **B008** yadırgatıcı söz veya başıboş uyak — yadırgatıcı, alışılmadık sözcük · şiirin başıboş veya aykırı uyakları
  الشوارد من القوافي أوابد (sihah)؛ الكلمة الوحشية آبدة وجمعه الأوابد (tahdhib)
- **B009** öfkelenmek veya birine öfkelenmek [kalıp] — adamın öfkelenmesi · ona öfkelenmek
  أبد الرجل غضب (sihah)؛ أبد إذا غضب عليه (tahdhib)؛ وقد فسر بغضب (mufradat)

## ق ت ل (root_001200) — identity root of قُوتِلْتُمْ (w23)

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

## ن ص ر (root_001510) — identity root of لَنَنصُرَنَّكُمْ (w24)

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

## ء ل ه (root_000047) — identity root of وَٱللَّهُ (w25)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ش ه د (root_000822) — identity root of يَشْهَدُ (w26)

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

## ك ذ ب (root_001290) — identity root of لَكَٰذِبُونَ (w28)

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

## و ل ه (root_005296) — documented alternative for وَٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ر و ي (root_000615) — for تَرَ (w2): withheld observed target; not identity

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

## ECHO ق ل ل (root_001251) — for يَقُولُونَ (w6): withheld observed target; not identity

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

## ECHO س ط ع (root_000706) — for نُطِيعُ (w18): withheld observed target; not identity

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

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:11, and ## Buluşmalar) =====
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

## Gece örtüsü ve açılan gün

Surede örtmek anlamı taşıyan birçok kelime vardır. "Küfür" kelimesinin kökü örtmektir: {ar:الستر والتغطية, tr:es-setr ve't-tağtiye, gloss:örtme ve kapama, source:"ك ف ر,B001"}. Bu kökte gece de kâfirdir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfir, gloss:gece, karanlığıyla örttüğü için "kâfir"dir, source:"ك ف ر,B002"}. Onuncu ayetteki bağışlanma duası da aynı örtme alanındadır: {ar:الغفر الستر, tr:el-ğafr es-setr, gloss:ğafr örtmektir, source:"غ ف ر,B001"}. "Cennet" de gecenin karanlığıdır: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyl, gloss:gecenin cenânı, karanlığı ve eşyayı örtmesidir, source:"ج ن ن,B002"}. Nifak da bir örtüdür: {ar:النفاق لأن صاحبه يكتم خلاف ما يظهر, tr:en-nifâk, gloss:nifak, sahibinin gösterdiğinin tersini gizlemesidir, source:"ن ف ق,B004"}. On dördüncü ayetteki "ardından" kelimesi de saklamayı anlatır: {ar:التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره, tr:et-tevriye es-setr, gloss:tevriye örtmedir; haberi gizleyip başkasını gösterdiğinde "verraytu" dersin, source:"و ر ي,B005"}. Bu yüzden münafıkların duvar arkasında savaşması ile sözlerinin arkasına gizlenmesi aynı kelimeyle işitilir. Tek fark, bir örtünün kurtarması, ötekinin boğmasıdır. Onuncu ayette istenen bağış örtüsü, kişiyi koruyan bir örtüdür. Küfür ve nifak örtüsü ise onu karanlıkta bırakır. On yedinci ayetteki "zalimler" kelimesi karanlığın kendisidir: {ar:الظلمة خلاف النور, tr:ez-zulme hılâfu'n-nûr, gloss:zulmet nurun karşıtıdır, source:"ظ ل م,B001"}. Ayette geçen "ateş" kelimesi ise ışıkla aynı yoldan adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan adlandırılmıştır, source:"ن و ر,B002"}. Ama ateş burada aydınlatmaz, yakar. Münafıklar da bir ateş yakar ama Allah ışıklarını götürür ve onları {ar:فِى ظُلُمَٰتٍ لَّا يُبْصِرُونَ, tr:fî zulumâtin lâ yubsırûn, gloss:göremedikleri karanlıklarda, source:2:17} bırakır. Kıyamette münafıklar müminlerin ışığından almak ister, onlara {ar:ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًا, tr:irci'û verâekum fe'ltemisû nûrâ, gloss:arkanıza dönün de bir ışık arayın, source:57:13} denir. Hemen ardından iki tarafı birbirinden ayıran bir sur çekilir {source:57:13}. Bu ayette surun ardı, ışık ve ayrılık, bu surenin kale, "ardında" ve karanlık kelimeleri bir arada bulunur.

Örtünün karşısında sabah açılır. Yirmi birinci ayetteki "parça parça olmuş" kelimesinin ailesinde sabah da vardır: {ar:الصديع الصبح, tr:es-sadî' es-subh, gloss:sadî' sabahtır, source:"ص د ع,B006"}. Dokuzuncu ayetteki "nefisler" kelimesi de sabahın nefes almasıdır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subh, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Kur'an aynı ifadeyi yemin olarak kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. On sekizinci ayetteki "yarın" kelimesi de seher vaktidir: {ar:الغدوة ما بين صلاة الغداة وطلوع الشمس, tr:el-ğudve, gloss:ğudve, sabah namazı ile güneşin doğuşu arasıdır, source:"غ د و,B001"}. Üçüncü ayetteki "sürgün" (celâ) kelimesi de açığa çıkıp görünür olmaktır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey' ve burûzuh, gloss:bir şeyin açılıp ortaya çıkması, source:"ج ل و,B001"}. Bu kelimenin bir dalı da gündüzün beyazlığıdır {source:"ج ل و,B007"}. Kur'an bu fiili gündüz için kullanır: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Sürgün edilenler kalelerinden çıkarılıp açık alana konur. Gece onları örtüyordu, şimdi her şey gün ışığına çıkar. Yirmi ikinci ayet bu iki yarıyı Allah'ın bilgisinde birleştirir: {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ, tr:'âlimu'l-ğaybi ve'ş-şehâde, gloss:görünmeyeni ve görüneni bilen, source:59:22}. "Gayb" kelimesinin kökü gözlerden gizlenmektir, güneşin batmasına da bu kökle "gâbet" denir {source:"غ ي ب,B001"}. "Şehâdet" ise oradan bakıp görmektir {source:"ش ه د,B001"}. Yirmi birinci ayetteki "hâşi'" kelimesi de batmaya yaklaşan yıldızlar için kullanılır: {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşa'ati'l-kevâkib, gloss:yıldızlar batmaya yaklaşınca "haşaat" denir, source:"خ ش ع,B003"}. Böylece batan yıldızla doğan sabah aynı ayette yan yana durur. Gece ile gündüzde gizlenen ile açıkta yürüyenin Allah katında eşit olduğu da söylenir {source:13:10}.

Kaynaklar: 59:2 كَفَرُوا ك ف ر B001, B002; 59:10 ٱغْفِرْ غ ف ر B001; 59:20 ٱلْجَنَّةِ ج ن ن B002; 59:11 نَافَقُوا ن ف ق B004; 59:14 وَرَآءِ و ر ي B005; 59:17 ٱلظَّٰلِمِينَ ظ ل م B001; 59:3 ٱلنَّارِ ن و ر B002; 59:21 مُّتَصَدِّعًا ص د ع B006; 59:9 أَنفُسِهِمْ ن ف س B009; 59:18 لِغَدٍ غ د و B001; 59:3 ٱلْجَلَآءَ ج ل و B001, B007; 59:22 ٱلْغَيْبِ غ ي ب B001; 59:22 ٱلشَّهَٰدَةِ ش ه د B001; 59:21 خَٰشِعًا خ ش ع B003

## Yurttan çıkış, ıssızlaşan yurt, hazırlanan konak

Sure iki topluluğun evinden çıkışını anlatır. Birincisi, ikinci ayetteki çıkarılmadır: {ar:أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ, tr:ahrace'llezîne keferû min ehli'l-kitâbi min diyârihim li-evveli'l-haşr, gloss:kitap ehlinden inkâr edenleri ilk sürgünde yurtlarından çıkaran, source:59:2}. "Haşr" kelimesi burada bir topluluğu yerinden çıkarıp sürmek anlamını taşır: {ar:إخراج الجماعة عن مقرهم وإزعاجهم عنه, tr:ihrâcu'l-cemâ'a 'an makarrihim ve iz'âcuhum 'anh, gloss:topluluğu yurdundan çıkarıp oradan sökmek, source:"ح ش ر,B001"}. Bu ifadede, aynı ayetteki "çıkardı" fiili ile "haşr" kelimesi birleşir. Üçüncü ayetteki "celâ" (sürgün) da insanları evlerinden açık alana çıkarmaktır: {ar:أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها, tr:eclaytu'l-kavme 'an menâzilihim, gloss:topluluğu evlerinden çıkardım, yani onları açığa çıkardım, source:"ج ل و,B004"}. İkincisi, sekizinci ayetteki muhacirlerin çıkışıdır: {ar:ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ, tr:ellezîne uhricû min diyârihim ve emvâlihim, gloss:yurtlarından ve mallarından çıkarılanlar, source:59:8}. Hicret evden eve göçmektir: {ar:هاجر القوم من دار إلى دار تركوا الأولى للثانية, tr:hâcera'l-kavmu min dârin ilâ dâr, gloss:topluluk bir yurttan bir yurda göçtü, ilkini ikincisi için bıraktı, source:"ه ج ر,B002"}. Böylece aynı fiil iki çıkışı da anlatır, ama ikisinin sonu farklıdır. Birinciler, yurtlarını kendi elleriyle yıkıp gider. İkinciler ise kendilerine hazırlanmış bir yurda varır: {ar:وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ, tr:ve'llezîne tebevve'u'd-dâra ve'l-îmâne min kablihim, gloss:onlardan önce o yurdu ve imanı yerleşim yeri edinenler, source:59:9}. "Tebevvu'" fiili bir yeri konak edinmektir: {ar:المباءة منزل القوم في كل موضع وتبوأت منزلا وبوأت للرجل منزلا, tr:el-mebâ'e menzilu'l-kavm, gloss:mebâe, topluluğun konağıdır; konak edindim ve adama konak hazırladım, source:"ب و ء,B001"}. Ayetteki dikkat çekici nokta, imanın da yurt gibi konak edinilmesidir. Kur'an hicret edenlere de böyle bir konak vaat eder: {ar:لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةً, tr:le-nubevvi'ennehum fi'd-dunyâ hasene, gloss:onları dünyada güzel bir yere yerleştireceğiz, source:16:41}. Haksız yere yurtlarından çıkarılanlar için ise {ar:وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ, tr:ve le-yensuranna'llâhu men yensuruh, inna'llâhe le-kaviyyun 'azîz, gloss:Allah kendisine yardım edene mutlaka yardım eder; Allah güçlüdür, azîzdir, source:22:40} denir. Bu ayette, sekizinci ayetteki "yardım ederler" ile birinci ayetteki "Azîz" bir araya gelir. Barınak verip yardım edenler de muhacirlerle birlikte anılır {source:8:72}.

Yolun kendisi de suredeki kelimelerde vardır. Yedinci ayetteki {ar:وَٱبْنِ ٱلسَّبِيلِ, tr:ve'bni's-sebîl, gloss:ve yolda kalmış yolcu, source:59:7} ifadesi, yolculukta yolu kesilmiş kişiyi anlatır: {ar:ابن السبيل المسافر الذي انقطع به, tr:ibnu's-sebîl el-musâfir ellezi'nkutı'a bih, gloss:ibnu's-sebîl, yolu kesilmiş yolcudur, source:"س ب ل,B002"}. Beşinci ayetteki "kesmek" fiili bu yolculuğa iki ifadeyle bağlanır. Biri, bineği ölüp azığı biten yolcudur {source:"ق ط ع,B006"}. Öbürü yolcuları soyan eşkıyadır: {ar:قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق, tr:kuttâ'u't-turuk, gloss:yolcuların önünü kesip yolu onlara kapatan yol kesiciler, source:"ق ط ع,B023"}. İkinci ayetteki "ibret alın" fiili de yoldan geçmektir: {ar:رجل عابر سبيل أي مار, tr:raculun 'âbiru sebîl, gloss:yoldan geçen adam, source:"ع ب ر,B001"}. Uzak yolu anlatan kelimeler de surede vardır: dördüncü ayetteki "ayrılık" kelimesinin ailesinde uzun yolculuk {source:"ش ق ق,B005"}, on altıncı ayetteki "Şeytan" kelimesinin ailesinde de evin uzaklığı vardır: {ar:شطنت الدار شطونا إذا بعدت, tr:şatanati'd-dâr, gloss:yurt uzaklaşınca "şatanat" denir, source:"ش ط ن,B001"}.

Geride kalan yurt ise ıssızlaşır. On birinci ayette münafıklar {ar:وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًا, tr:ve lâ nutî'u fîkum ehaden ebedâ, gloss:sizin hakkınızda hiç kimseye asla boyun eğmeyiz, source:59:11} der. "Ebed" kelimesinin ailesinde, sahipleri gidip yaban hayvanlarına kalan ev vardır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:te'ebbede'l-menzil, gloss:ev ıssızlaştı ve yaban hayvanları ona alıştı, source:"ء ب د,B003"}. "Kimse" kelimesi de evle birlikte geçer: {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"}. Yurt kelimesi de yalnız bu tür olumsuz cümlelerde "kimse" anlamı taşır {source:"د و ر,B008"}. Yani "asla" diye verilen söz, yanında boşalmış bir evin sesini taşır. Yedinci ayetteki "zenginler" kelimesi de bir yerde oturmak anlamı taşır: {ar:غني القوم في دارهم أقاموا ومغانيهم منازلهم, tr:ğaniye'l-kavmu fî dârihim, gloss:topluluk yurdunda oturdu; meğânî onların konaklarıdır, source:"غ ن ي,B004"}. Aynı kökte bir deyim de vardır: {ar:كأن لم يغن بالأمس أي كأن لم يكن, tr:ke-en lem yağne bi'l-ems, gloss:sanki dün orada hiç oturmamış, yani hiç yokmuş gibi, source:"غ ن ي,B004"}. Kur'an bu deyimi yok edilen kavimler için kullanır: {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlar gibi, source:11:68}. Bahçe sahnesinde de aynı ifade vardır {source:10:24}. On yedinci ayetteki "ebedî kalıcılar" kelimesi, ailesinde harabeden geriye kalan ocak taşlarını da anlatır: {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid, gloss:uzun süre durdukları için ocak taşlarına havâlid denir, source:"خ ل د,B001"}. Kalıcılık burada artık yaşanan bir ev değil, yıkıntıda kalan taştır. On dokuzuncu ayetteki "unuttular" fiili de göçenlerin ardında bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sakata min menâzili'l-murtahılîn, gloss:nisy, göçenlerin konaklarından düşen değersiz eşyadır, source:"ن س ي,B003"}. Meryem de aynı kelimeyle {ar:وَكُنتُ نَسْيًا مَّنسِيًّا, tr:ve kuntu nesyen mensiyyâ, gloss:unutulup gitmiş bir şey olsaydım, source:19:23} der. Allah'ı unutanlar, kendilerini de unutturulmuş olarak terk edilmiş bir yurdun döküntüsü gibi bulur. İkinci ayetteki "ev" kelimesi de kabir anlamına gelir {source:"ب ي ت,B007"}. Kur'an boşalmış evleri böyle gösterir: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş evleri, source:27:52}. Az kalsın hiç oturulmamış meskenler de vardır {source:28:58}. Kuşatılmış başka bir topluluğun yurdu da müminlere miras kalmıştır {source:33:27}.

Kaynaklar: 59:2/8 أَخْرَجَ / أُخْرِجُوا خ ر ج B001; 59:2 ٱلْحَشْرِ ح ش ر B001; 59:3 ٱلْجَلَآءَ ج ل و B004; 59:8/9 ٱلْمُهَٰجِرِينَ / هَاجَرَ ه ج ر B002; 59:9 تَبَوَّءُو ب و ء B001; 59:7 ٱبْنِ ٱلسَّبِيلِ س ب ل B002; 59:5 قَطَعْتُم ق ط ع B006, B023; 59:2 فَٱعْتَبِرُوا ع ب ر B001; 59:4 شَآقُّوا ش ق ق B005; 59:16 ٱلشَّيْطَٰنِ ش ط ن B001; 59:11 أَبَدًا ء ب د B003; 59:11 أَحَدًا ء ح د B002; 59:2 دِيَٰرِهِمْ د و ر B008; 59:7 ٱلْأَغْنِيَآءِ غ ن ي B004; 59:17 خَٰلِدَيْنِ خ ل د B001; 59:19 نَسُوا ن س ي B003; 59:2 بُيُوتَهُم ب ي ت B007

## Bağlar, köstekler, ipler

On dördüncü ayetteki "akıl" kelimesi, kale anlamının yanında deveyi bağlamak anlamını da taşır: {ar:عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط, tr:'akaltu'l-ba'îr, gloss:devenin ayağını ipiyle bağladım; ikâl bağdır, source:"ع ق ل,B002"}. Akıl etmeyen bir topluluk, bağı olmayan bir sürü gibidir. Kalpleri dağınık olanlar ip tutmaz. Dördüncü ve yedinci ayetlerdeki {ar:شَدِيدُ ٱلْعِقَابِ, tr:şedîdu'l-'ikâb, gloss:cezası çetin, source:59:4} ifadesi de bir bağlama işini taşır: {ar:عقبت الرمح شددته بالعقب, tr:'akabtu'r-rumh, gloss:mızrağı sinirle sıkıca bağladım, source:"ع ق ب,B001"}. "Şiddet" de düğümü sıkmaktır {source:"ش د د,B001"}. Bu ceza kaçana gevşemeyen bir sinir bağı gibi sarılır. Onuncu ve on birinci ayetlerdeki "kardeşler" kelimesi, hayvanın bağlandığı kazığı da adlandırır: {ar:الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة, tr:el-âhiyye, gloss:âhiyye, hayvanın bağlandığı kazıktır; aynı zamanda saygınlık ve ahittir, source:"ء خ و,B002"}. Sure iki tür kardeşlik gösterir. Onuncu ayette müminler {ar:رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا, tr:rabbena'ğfir lenâ ve li-ihvâninâ, gloss:Rabbimiz, bizi ve kardeşlerimizi bağışla, source:59:10} diye dua eder. On birinci ayette ise münafıklar {ar:يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟, tr:yekûlûne li-ihvânihimu'llezîne keferû, gloss:inkâr eden kardeşlerine diyorlar, source:59:11}. Birinci bağ kazığa sağlam bağlıdır, ikincisi kriz anında çözülür. Kur'an müminlere sağlam bir ip gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Bu ayette, on dördüncü ayetteki "toplu" kelimesi bir ipe bağlanmış olur. Kitap ehli için de iki ip anılır {source:3:112}. On altıncı ayetteki "Şeytan" kelimesi de ip ailesindendir: {ar:الشطن الحبل الطويل الشديد الفتل يستقى به, tr:eş-şatan el-hablu't-tavîl, gloss:şatan, su çekilen uzun, sıkı bükülmüş iptir, source:"ش ط ن,B002"}. Bu kökte ayrıca birini niyetinin yönünden saptırmak da vardır {source:"ش ط ن,B003"}. Şeytan uzun bir iple insanı derin bir kuyuya indirir, sonra ipi bırakır. Kendi sözüyle de, insanlar üzerinde bir gücü olmadığını, onları kurtaramayacağını söyler {source:14:22}. Onuncu ayetteki "ğıll" kelimesi, başka bir harekeyle, elleri boyna bağlayan demir halkadır: {ar:الغل مختص بما يقيد به فيجعل الأعضاء وسطه, tr:el-ğull, gloss:ğull, uzuvları ortasına alarak bağlayan bukağıdır, source:"غ ل ل,B006"}. On dördüncü ayetteki "toplu" kelimesi de aynı bukağıyı adlandırır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull, gloss:câmia bukağıdır, çünkü elleri boyuna birleştirir, source:"ج م ع,B008"}. Böylece kalpteki kin ile ellerdeki bukağı aynı kökten ses verir. Toplu sanılan kalabalık da birbirine bukağıyla bağlanmış olur. Kur'an bukağıyı da gösterir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu da bukağılayın, source:69:30}. Birinci ve yirmi dördüncü ayetlerdeki "Hakîm" ismi de, ailesinde atın çenesini saran gem halkasıdır {source:"ح ك م,B006"}. On birinci ayetteki "boyun eğmek" fiili de dizgine kolay uyan atı anlatır {source:"ط و ع,B001"}. Münafıklar "kimseye boyun eğmeyiz" derken, aslında gemsiz kalırlar.

Kaynaklar: 59:14 يَعْقِلُونَ ع ق ل B002; 59:4/7 شَدِيدُ ٱلْعِقَابِ ع ق ب B001, ش د د B001; 59:10/11 إِخْوَٰن ء خ و B002; 59:16 ٱلشَّيْطَٰنِ ش ط ن B002, B003; 59:10 غِلًّا غ ل ل B006; 59:14 جَمِيعًا ج م ع B008; 59:1/24 ٱلْحَكِيمُ ح ك م B006; 59:11 نُطِيعُ ط و ع B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

