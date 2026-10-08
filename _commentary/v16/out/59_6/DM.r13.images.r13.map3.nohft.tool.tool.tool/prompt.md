Focus: 59:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_6/D.r13/context.md =====
# 59:6 — focus

وَمَآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْهُمْ فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍۢ وَلَا رِكَابٍۢ وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَآ | مَا |  | CONJ;COND |
| 2 | أَفَآءَ | أَفَآءَ | ف ي ء | V |
| 3 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 4 | عَلَىٰ | عَلَىٰ |  | P |
| 5 | رَسُولِهِۦ | رَسُول | ر س ل | N;PRON |
| 6 | مِنْهُمْ | مِن |  | P;PRON |
| 7 | فَمَآ | مَا |  | RSLT;NEG |
| 8 | أَوْجَفْتُمْ | أَوْجَفْ | و ج ف | V;PRON |
| 9 | عَلَيْهِ | عَلَىٰ |  | P;PRON |
| 10 | مِنْ | مِن |  | P |
| 11 | خَيْلٍ | خَيْل | خ ي ل | N |
| 12 | وَلَا | لَا |  | CONJ;NEG |
| 13 | رِكَابٍ | رِكَاب | ر ك ب | N |
| 14 | وَلَٰكِنَّ | لَٰكِنّ |  | REM;ACC |
| 15 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 16 | يُسَلِّطُ | سَلَّطَ | س ل ط | V |
| 17 | رُسُلَهُۥ | رَسُول | ر س ل | N;PRON |
| 18 | عَلَىٰ | عَلَىٰ |  | P |
| 19 | مَن | مَن |  | REL |
| 20 | يَشَآءُ | شَآءَ | ش ي ء | V |
| 21 | وَٱللَّهُ | ٱللَّه | ء ل ه | CONJ;PN |
| 22 | عَلَىٰ | عَلَىٰ |  | P |
| 23 | كُلِّ | كُلّ | ك ل ل | N |
| 24 | شَىْءٍ | شَىْء | ش ي ء | N |
| 25 | قَدِيرٌ | قَدِير | ق د ر | N |


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
- 59:6 ◀ focus وَمَآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْهُمْ فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍۢ وَلَا رِكَابٍۢ وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
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


===== _commentary/v16/work/59_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ف ي ء (root_001191) — identity root of أَفَآءَ (w2)

- **B001** geri dönme; geri döndürme veya başka bir işe yöneltme — geri dönmek; bir işe yeniden yönelmek · geri döndürmek; bir kimseyi başka bir işe yöneltmek · öfkesinden çabuk dönmek; çabuk yatışmak
  فاء الرجل يفيء إذا رجع فيئة (jamhara)؛ فاء يفئ فيئا رجع (sihah)؛ أصل الفيء الرجوع (tahdhib)؛ الفيء والفيئة الرجوع إلى حالة محمودة (mufradat)؛ أفأت فلانا على الأمر إذا عدلته إلى أمر غيره (tahdhib)
- **B002** karşı taraftan topluluğa geçen, dar yorumda savaşsız edinilen mal — karşı taraftan inananlar topluluğuna geçen mal; özellikle savaşsız edinilen mal · bu malı topluluk payı olarak almak · topluluk için karşı taraftan mal alıp onlara getirmek
  أفاء الله عليهم فيئا كثيرا (jamhara)؛ الفئ الخراج والغنيمة (sihah)؛ الفيء ما رد الله على أهل دينه من أموال من خالف أهل دينه بلا قتال (tahdhib)؛ قيل للغنيمة التي لا يلحق فيها مشقة فيء (mufradat)
- **B003** öğleden sonra geri gelen gölge; güneş görmeyen yer — öğleden sonra geri gelen gölge · ağacın geri gelen gölgesi çoğalmak · ağacın veya başka bir şeyin gölgesine çekilmek · gölgelerin gün ortasından sonra geri gelmesi · güneş görmeyen yer
  الفيء ما نسخه الظل (jamhara)؛ الفيء ما بعد الزوال من الظل (sihah)؛ تفيؤ الظلال رجوعها بعد انتصاف النهار (tahdhib)؛ فاء الظل والفيء لا يقال إلا للراجع منه (mufradat)؛ المفيؤة المقنؤة للمكان الذي لا تطلع عليه الشمس (tahdhib)
- **B004** birbirine dayanan veya bir başkan çevresinde toplanan topluluk — birbirine dayanan veya bir başkan çevresinde toplanan insan topluluğu
  الفئة الجماعة من الناس يفيئون إلى الرئيس (jamhara)؛ الفئة الطائفة (sihah)؛ الفئة الجماعة المتظاهرة التي يرجع بعضهم إلى بعض في التعاضد (mufradat)
- **B005** kuş kümesi; küçük kuş sürüsü — kuş kümesi; küçük kuş sürüsü
  الفيء القطعة من الطير (jamhara)؛ يقال للقطعة من الطير فيء وعرقة وصف (tahdhib)
- **B006** sert hurma çekirdeği; toynak içinde çekirdeğe benzeyen sert oluşum [kalıp] — sert hurma çekirdekli; toynak içinde çekirdeğe benzetilen sert oluşumlu
  يقال لنوى التمر إذا كان صلبا ذو فيئة؛ ذو فيئة من نوى قران معجوم؛ خلق لها في بطن حوافرها نسور صلاب كأنها نوى قران (tahdhib)
- **B007** kadının eşine nazlı ve kıvrak davranması [kalıp] — kadının eşine nazlı ve kıvrak davranması
  تفيأت المرأة لزوجها إذا تكسرت له تدللا (tahdhib)
- **B008** parça parça gelen bulut kümeleri — 
  الأفى القطع من الغيم وهي الفرق يجئن قطعا؛ الواحدة أفاة؛ يقال هفاة أيضا (tahdhib)
- **B009** keskinliğini yitirip körelme [kalıp] — metal ağzı keskinliğini yitirip körelmek
  يقال للحديدة إذا كلت بعد حدتها قد فاءت (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w3)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ر س ل (root_000563) — identity root of رَسُولِهِۦ (w5)

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

## و ج ف (root_001628) — identity root of أَوْجَفْتُمْ (w8)

- **B001** hızlı yol alma; bineği hızlandırıp yürütme — hızlı yol alma · deve ya da atın hızlı yürümesi · deve ve atlara özgü, daha hızlı bir yürüyüş derecesinin altında kalan hızlı yürüyüş biçimi · deveyi ya da atı hızlandırıp yürütmek · bir yer üzerine at ya da binek sürüp bunları işletmek · bineğin hızla yürütüldüğü gidiş biçimi · atı zayıflayıncaya kadar hızla sürmek
  الوجف سرعة السير (ayn;tahdhib)؛ وجف البعير يجف وجفا ووجيفا (jamhara;sihah;tahdhib)؛ ضرب من سير الإبل والخيل (jamhara;sihah)؛ أوجفت البعير إذا حملته على الوجيف (jamhara)؛ أوجفت البعير أسرعته (mufradat)؛ ما أعملتم (sihah)؛ الوجيف دون التقريب من السير (tahdhib)
- **B002** sarsıntılı hareket; yüreğin çarpıp ürpermesi — sarsılıp düzensiz hareket etmek · sarsıntılı; yürek için çarpan ya da korkuyla ürperen · yürek çarpıntısı
  وجف الشيء أي اضطرب (sihah)؛ قلب واجف (sihah)؛ واجفة شديدة الاضطراب (tahdhib)؛ واجفة خائفة (tahdhib)؛ قلوب يومئذ واجفة أي مضطربة (mufradat)؛ وجيب القلب من الإبدال والأصل الوجيف (maqayis)
- **B003** sevginin gönlü alıp götürmesi [kalıp] — sevginin gönlünü alıp götürmesi
  استوجف الحب فؤاده إذا ذهب به (tahdhib)

## خ ي ل (root_000454) — identity root of خَيْلٍ (w11)

- **B001** kişinin ya da şeyin siluet, yansıma veya zihinsel görüntü olarak beliren benzeri — siluet, beliren görüntü veya zihinde canlanan biçim · siluet veya beliren görüntü · kuşları ve hayvanları korkutmak için dikilen insan biçimli korkuluk · aynada görülen yansıman · bir şeyi zihinde canlandırma veya göz önünde belirir gibi görme
  الخيال وهو الشخص (maqayis); الخيال كل شيء تراه كالظل وخيالك في المرآة (ayn); والخيال معروف (jamhara); الخيال والخيالة الشخص والطيف (sihah); الصورة المجردة كالصورة المتصورة في المنام وفي المرآة وفي القلب (mufradat)
- **B002** atlar topluluğu ve bağlama göre bu topluluğun atlıları — atlar topluluğu; bağlama göre atlar ve atlılar · atlar · atlılar veya at sahipleri · senin atlıların ve yayaların · atlılara yapılan binme çağrısı
  والخيل معروفة (maqayis); الخيل جماعة الفرس (ayn); الخيل جمع لا واحد له من لفظه (jamhara); الخيل أيضا الخيول والخيالة أصحاب الخيول (sihah); الخيل في الأصل اسم للأفراس والفرسان جميعا (mufradat)
- **B003** kendini üstün görerek böbürlenme ve bunu gösterişli yürüyüşle dışa vurma — kibir ve böbürlenerek yürüme · kibirli ve gösterişli biçimde yürüme · kibirli, böbürlenen · kibir ve büyüklük taslama · ağır ağır böbürlenerek yürüme
  لاختيالها والمختال في مشيته (maqayis); التخايل خيلاء في مهلة (ayn); الخيلاء التكبر في المشي (jamhara); الخال والخيلاء الكبر (sihah); الخيلاء التكبر عن تخيل فضيلة (mufradat)
- **B004** gökyüzünün yağmur umduran belirtiler göstermesi — yağmur umduran bulut veya hava belirtisi · gökyüzü bulutlanıp yağmura hazırlandı · gökyüzü bulutlanıp gök gürültüsü ve şimşekle yağmur belirtisi gösterdi · bulut yağmur umdurdu · yağmur umduran bulut · yağacak izlenimi verip geçen bulut
  تخيلت السماء إذا تهيأت للمطر والمخيلة السحابة (maqayis); الخيال غيم ينشأ يخيل إليك أنه ماطر (ayn); الخال الغيم وأخالت السحاب إذا كانت ترجى المطر (sihah); خيلت السماء أبدت خيالا للمطر (mufradat)
- **B005** kesin bilgi olmadan zihinde canlandırma, sanma veya karıştırma — bir şeyi zihinde canlandırma veya göz önünde belirir gibi görme · onu öyle sandım · sanırım · ona öyleymiş gibi gösterildi veya zihninde yanıltıcı bir izlenim uyandırıldı · benzerlik yüzünden adamı zan altında bıraktı · belirsizleşti veya karışık göründü · kuşkulu veya belirsiz görünen
  خيلت على الرجل تخييلا إذا وجهت التهمة إليه (maqayis); تخيل إلي أي شبه وكل شيء اشتبه عليك فهو مخيل (ayn); خلت الشيء خيلا أي ظننته وخيل إليه من التخييل والوهم (sihah); التخييل تصوير خيال الشيء في النفس وخلت بمعنى ظننت (mufradat)
- **B006** iyiliğe veya uygun sonuca elverişli görünme ve belirtilerinden sezilme [kalıp] — iyiliğe yatkın ve buna elverişli · onda iyilik sezip onu seçtim · dişi devenin iyi durumda veya sütlü olduğu belli oldu · bitkisi gelişip çiçeğe durmuş toprak
  تخيلت عليه تخيلا إذا تفرست فيه (maqayis); كل خليق لشيء فهو مخيل له وتخيل عليك إذا اختارك وتفرس فيك الخير وأخالت الناقة فهي مخيلة إذا كان في ضرعها لبن (ayn); فلان مخيل للخير أي خليق له وتخيلت على الرجل إذا اخترته وتفرست فيه الخير ووجدت أرضا متخيلة ومتخايلة إذا بلغ نبتها المدى وخرج زهرها (sihah); فلان مخيل بكذا أي خليق (mufradat)
- **B007** çoğunlukla gökkuzgun, bir aktarımda doğan sayılan renkli kuş türü — renkli bir kuş; çoğu aktarımda gökkuzgun, bir aktarımda doğan · söz konusu kuşun sağrısına konup yaraladığı deve · bu renkli kuşlar
  الأخيل طائر وأظنه ذا ألوان يقال هو الشقراق (maqayis); الأخيل طائر خضرته مشربة حمرة والأخيل الشاهين (ayn); الأخيل طائر هو الشقراق تتشاءم به (sihah); الأخيل الشقراق لكونه متلونا (mufradat)
- **B008** karşılıklı yarışma ve boy ölçüşme — karşılıklı yarışma veya boy ölçüşme
  المخايلة المباراة (sihah)
- **B009** bedendeki siyahımsı doğal ben — bedendeki siyahımsı ben · bedendeki benler · vücudunda çok ben bulunan · vücudunda çok ben bulunan
  الخَال الذي يكون في الجسد ويجمع على خيلان (sihah)

## ر ك ب (root_000589) — identity root of رِكَابٍ (w13)

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

## س ل ط (root_000732) — identity root of يُسَلِّطُ (w16)

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

## ش ي ء (root_000831) — identity root of يَشَآءُ (w20)

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

## ش ي ء (root_000832) — identity root of يَشَآءُ (w20)

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

## ك ل ل (root_001315) — identity root of كُلِّ (w23)

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

## ق د ر (root_001205) — identity root of قَدِيرٌ (w25)

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

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:6, and ## Buluşmalar) =====
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

## Hurmalık

Beşinci ayet, kuşatma sırasında bir hurmalıkta yapılan iki şeyi yan yana koyar: {ar:مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ, tr:mâ kata'tum min lînetin ev teraktumûhâ kâimeten 'alâ usûlihâ fe-bi-izni'llâh, gloss:hurma ağaçlarından neyi kestiyseniz ya da köklerinin üzerinde ayakta bıraktıysanız, Allah'ın izniyle oldu, source:59:5}. "Lîne" hurma ağacının adıdır ve türüne göre ayrılmaz: {ar:لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع, tr:lîne, gloss:lîne, yumuşak bir hurma ağacıdır; bir türe has değildir, source:"ل ي ن,B006"}. "Kesmek" ile "izin" bir ifadede de birleşir: {ar:أقطعته قضبانا أي أذنت له في قطعها, tr:akta'tuhû kudbânen, gloss:ona dal kesmeye izin verdim, source:"ق ط ع,B013"}. Böylece kesme de bırakma da yalnız sahibinin izniyle yapılabilir. "Kökler" kelimesi de hurmanın kalıcılığına bağlanır: {ar:النخل بأرضنا أصيل أي لا يفنى ولا يزول, tr:en-nahl bi-ardınâ asîl, gloss:bizim toprağımızda hurma köklüdür, yani tükenmez ve yok olmaz, source:"ء ص ل,B002"}. Aynı kökün bir dalı kökünden sökmektir {source:"ء ص ل,B001"}. Ayet ise ağacı sökmez, "kökleri üzerinde ayakta" bırakılabileceğini söyler. Kur'an bu farkı başka bir yerde iki ağaçla gösterir: güzel ağacın {ar:أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ, tr:asluhâ sâbitun ve far'uhâ fi's-semâ', gloss:kökü sabit, dalı göktedir, source:14:24} ve {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tu'tî ukulehâ kulle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman meyvesini verir, source:14:25}. Kötü ağaç ise {ar:ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ مَا لَهَا مِن قَرَارٍ, tr:uctussat min fevki'l-ardı mâ lehâ min karâr, gloss:yerin üstünden koparılmıştır, karar kılacak yeri yoktur, source:14:26}. Bu surede de "izin" kelimesi hurma ile birlikte geçer.

Aynı ayetin sonu {ar:وَلِيُخْزِىَ ٱلْفَٰسِقِينَ, tr:ve li-yuhziye'l-fâsikîn, gloss:ve fâsıkları rezil etmek için, source:59:5} der. "Fısk" kelimesi, hurma tablosunda olgun hurmanın kabuğundan sıyrılmasıdır: {ar:فسقت الرطبة عن قشرها, tr:fesekati'r-rutabe 'an kışrihâ, gloss:taze hurma kabuğundan çıktı, source:"ف س ق,B002"}. Ağaçlar köklerinde dururken, fâsıklar kabuklarından dışarı çıkar. Altıncı ayetteki "binek develeri" kelimesinin ailesinde de kökü toprağa ulaşmayan bir hurma filizi vardır: {ar:الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق, tr:er-râkib, gloss:râkib, hurma gövdesinde biten ve toprakta kökü olmayan filizdir, source:"ر ك ب,B007"}. Bu filiz, "kökleri üzerinde ayakta" duran ağacın tersidir. İkinci ayetteki "kalpler" kelimesi de hurmanın yenen özünü adlandırır: {ar:قلب النخلة شحمتها, tr:kalbu'n-nahle şahmetuhâ, gloss:hurmanın kalbi onun özüdür, source:"ق ل ب,B003"}. Bu dalda hurmanın özünü sökmek de anlatılır {source:"ق ل ب,B003"}. Korkunun atıldığı yer böylece ağacın canlı özüne benzer. Yirminci ayetteki "cennet" kelimesinde Araplar hurmalığı da görür: {ar:العرب تسمي النخيل جنة, tr:el-'Arab tusemmi'n-nahîle cenne, gloss:Araplar hurmalığa cennet derler, source:"ج ن ن,B003"}. Yirmi üçüncü ayetteki "Cebbâr" ismi de, ailesinde elin yetişemediği yüksek hurmayı anlatır: {ar:الجبار من النخل الذي قد فات اليد, tr:el-cebbâr mine'n-nahl ellezî kad fâte'l-yed, gloss:cebbâr, eli aşmış uzun hurmadır, source:"ج ب ر,B002"}. Böylece sure kesilen ya da bırakılan hurmalarla başlayıp, el yetişmeyen yüksekliğe ve kalıcı bahçeye varır. Kur'an'da terk edilmiş hurmalıklar ve harap yurtlar yan yana durur. Firavun'un halkı için {ar:كَمْ تَرَكُوا۟ مِن جَنَّٰتٍ وَعُيُونٍ, tr:kem terakû min cennâtin ve 'uyûn, gloss:nice bahçe ve pınar bırakıp gittiler, source:44:25} denir. Ad kavminin cesetleri de {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍ, tr:ke-ennehum a'câzu nahlin hâviye, gloss:içi boş hurma kütükleri gibi, source:69:7} yerde yatar. Yoksula kapıyı kapatmak için sabah erkenden ürünü kesmeye yemin eden bahçe sahipleri de vardır {source:68:17}. Onlar {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme 'aleykum miskîn, gloss:bugün oraya yanınıza hiçbir yoksul girmesin, source:68:24} diye fısıldaşmışlardır. Sonunda bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:biçilmiş gibi oldu, source:68:20}. Bu sahne, yedinci ayetin yoksullara ayırdığı payın tam tersidir. Bahçesi yıkılan öteki adam da {ar:يُقَلِّبُ كَفَّيْهِ, tr:yukallibu keffeyh, gloss:ellerini ovuşturur, source:18:42}.

Kaynaklar: 59:5 لِّينَةٍ ل ي ن B006; 59:5 قَطَعْتُم ق ط ع B013; 59:5 أُصُولِهَا ء ص ل B002, B001; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B002; 59:6 رِكَابٍ ر ك ب B007; 59:2 قُلُوبِهِمُ ق ل ب B003; 59:20 ٱلْجَنَّةِ ج ن ن B003; 59:23 ٱلْجَبَّارُ ج ب ر B002

## Göğse atılan

Sure, göğüslere ve kalplere sürekli bir şey yerleştirir. İkinci ayette korku kalplere atılır. Atmak fiili okla ve taşla atmaktır {source:"ق ذ ف,B001"}. Atılan korku da havuzu dolduran bir şeydir: {ar:رعبت الحوض إذا ملأته, tr:ra'abtu'l-havd, gloss:havuzu doldurdum, source:"ر ع ب,B002"}. Yani korku kalbe bir taş gibi atılır ve suyun havuzu doldurduğu gibi onu doldurur. Kur'an bunu başka bir kitap ehli topluluk için aynı sözlerle anlatır {source:33:26}. Bedir'de de {ar:سَأُلْقِى فِى قُلُوبِ ٱلَّذِينَ كَفَرُوا۟ ٱلرُّعْبَ, tr:se-ulkî fî kulûbi'llezîne keferu'r-ru'b, gloss:inkâr edenlerin kalplerine korku salacağım, source:8:12} denir. Altıncı ayetteki "koşturmak" fiili de çarpan bir kalbi anlatır: {ar:قلب واجف, tr:kalbun vâcif, gloss:çarpan kalp, source:"و ج ف,B002"}. Kur'an'da da {ar:قُلُوبٌ يَوْمَئِذٍ وَاجِفَةٌ, tr:kulûbun yevmeizin vâcife, gloss:o gün kalpler çarpar, source:79:8} diye geçer. Müminler at koşturmamıştır, ama kalpleri çarpan başkalarıdır.

Dokuzuncu ayet ise boş bir göğüs çizer: Ensar göğüslerinde, verilen şeye karşı bir "hâce" bulmaz. Bu kelime bir ifadede göğüsle birlikte geçer ve şüphe anlamı da taşır: {ar:ما في صدري به حوجاء ولا لوجاء ولا شك ولا مرية بمعنى واحد, tr:mâ fî sadrî bihî havcâ' ve lâ levcâ', gloss:göğsümde bu konuda ne bir ihtiyaç ne bir şüphe var, source:"ح و ج,B002"}. Kökün bir dalı da bir tür dikendir {source:"ح و ج,B003"}. Böylece Ensar'ın göğsü, batan bir dikenden de kıskançlıktan da boştur. Onuncu ayetteki "ğıll" ise göğse çakılan bir şeydir: {ar:غللت الشيء في الشيء إذا أثبته فيه كأنه غرزته, tr:ğalaltu'ş-şey'e fi'ş-şey', gloss:bir şeyi başka bir şeye saplayıp sabitledim, source:"غ ل ل,B001"}. Kin de göğüste böyle işler: {ar:الغل وهو الضغن ينغل في الصدر, tr:el-ğıll ed-dığn yenğallu fi's-sadr, gloss:ğıll, göğse sızan kindir, source:"غ ل ل,B005"}. Sonradan gelenler bu çivinin kalplerine girmemesi için dua eder. Cennet ehlinin göğsünden de bu çivi sökülür: {ar:وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ إِخْوَٰنًا, tr:ve neza'nâ mâ fî sudûrihim min ğıllin ihvânâ, gloss:göğüslerindeki kini söküp çıkardık, kardeşler olarak, source:15:47}. Burada "kin" ve "kardeşler" yan yana gelir, tıpkı onuncu ayette olduğu gibi. On üçüncü ayet münafıklara döner: {ar:لَأَنتُمْ أَشَدُّ رَهْبَةً فِى صُدُورِهِم مِّنَ ٱللَّهِ, tr:le-entum eşeddu rahbeten fî sudûrihim mina'llâh, gloss:onların göğüslerinde siz Allah'tan daha korkutucusunuz, source:59:13}. "Rehbe" kelimesinin bir dalı göğsün kemiğidir: {ar:الرهابة عظم الصدر الذي تقع عليه القلادة, tr:er-ruhâbe, gloss:ruhâbe, gerdanlığın üzerine düştüğü göğüs kemiğidir, source:"ر ه ب,B007"}. Asıl anlamı ise sakınma ve titremeyle karışık korkudur {source:"ر ه ب,B001"}. Bu korku göğsün tam ortasında oturur. Musa'ya da {ar:وَٱضْمُمْ إِلَيْكَ جَنَاحَكَ مِنَ ٱلرَّهْبِ, tr:va'dmum ileyke cenâhake mine'r-rahb, gloss:korkudan kurtulmak için kolunu kendine çek, source:28:32} denir. Orada kol göğse bastırılarak korku yatıştırılır. On dördüncü ayette kalpler dağınıktır. Görülmesi gereken körlük de gözlerde değil, göğüslerdeki kalplerdedir: {ar:وَلَٰكِن تَعْمَى ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ, tr:ve lâkin ta'ma'l-kulûbu'lletî fi's-sudûr, gloss:fakat göğüslerdeki kalpler kör olur, source:22:46}. Münafıklar ağızlarıyla kalplerinde olmayanı söyler {source:3:167}. Müminlerin göğüslerine ise şifa verilir {source:9:14}. Yedinci ayetteki "yoksullar" kelimesi de kökünde bu çalkantının tersini taşır: {ar:خلاف الاضطراب والحركة, tr:hılâfu'l-ıdtırâbi ve'l-hareke, gloss:çalkantı ve hareketin karşıtı, source:"س ك ن,B001"}. Bu kökten gelen "sekîne" de müminlerin kalbine indirilir {source:"س ك ن,B005"}.

Kaynaklar: 59:2 وَقَذَفَ ق ذ ف B001; 59:2 ٱلرُّعْبَ ر ع ب B002; 59:6 أَوْجَفْتُمْ و ج ف B002; 59:9 حَاجَةً ح و ج B002, B003; 59:10 غِلًّا غ ل ل B001, B005; 59:13 رَهْبَةً ر ه ب B007, B001; 59:7 ٱلْمَسَٰكِينِ س ك ن B001, B005

## Görmekten geçmeye

İkinci ayet, kuşatma sahnesini bir çağrıyla bitirir: {ar:فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:fa'teberû yâ uli'l-ebsâr, gloss:ibret alın ey basiret sahipleri, source:59:2}. "İ'tibâr" kelimesi bir geçiştir: {ar:الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد, tr:el-i'tibâr ve'l-'ibra, gloss:i'tibâr ve ibret, görülenin bilgisinden görülmeyene ulaştıran durumdur, source:"ع ب ر,B004"}. Rüyayı yorumlayan da dışından içine geçer {source:"ع ب ر,B002"}. Basiret ise kalpte delip geçen bir görmedir {source:"ب ص ر,B002"}. Beşinci ayetteki "kesmek" fiili de nehri geçmek anlamında kullanılır: {ar:قطعت النهر قطوعا عبرته, tr:kata'tu'n-nehra kutû'an, gloss:nehri kat ettim, yani geçtim, source:"ق ط ع,B003"}. Bu ifadede "kesmek" ile "geçmek" birleşir. İbret, gözün gördüğü yıkılmış evlerden, görülmeyen sebebe geçmektir. Kur'an aynı çağrıyı Bedir'deki iki birlik için de yapar: {ar:يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ... إِنَّ فِى ذَٰلِكَ لَعِبْرَةً لِّأُو۟لِى ٱلْأَبْصَٰرِ, tr:yeravnehum misleyhim ra'ye'l-'ayn ... inne fî zâlike le-'ibraten li-uli'l-ebsâr, gloss:onları göz görüşüyle kendilerinin iki katı görüyorlardı; bunda basiret sahipleri için elbette bir ibret vardır, source:3:13}. Gece ile gündüzün dönüşümü için de aynı sözler kullanılır {source:24:44}. Üçüncü ayetteki "sürgün" (celâ) kelimesi gözü de açar: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ el-ismid, gloss:celâ sürmedir, çünkü gözü parlatır, source:"ج ل و,B002"}. Sürgün, ona bakanların gözüne çekilen bir sürme gibidir.

Görmenin karşısında sure tahmini koyar. Kuşatılanlar kalelerinin kendilerini koruyacağını "zannetmiştir" ve gelişi "hesaba katmamışlardır". Zan, kesin olmayan bilgidir {source:"ظ ن ن,B003"}. Bir dalı da içinde su olup olmadığı bilinmeyen kuyudur: {ar:الظنون البئر لا يدرى أفيها ماء أم لا, tr:ez-zenûn el-bi'r, gloss:zenûn, içinde su olup olmadığı bilinmeyen kuyudur, source:"ظ ن ن,B006"}. On dördüncü ayetteki "sanırsın" fiili de zan demektir {source:"ح س ب,B002"}. Altıncı ayetteki "atlar" kelimesinin ailesinde de aynada görülen gölge vardır: {ar:الخيال كل شيء تراه كالظل وخيالك في المرآة, tr:el-hayâl kullu şey'in terâhu ke'z-zıll, gloss:hayâl, gölge gibi gördüğün her şey ve aynadaki görüntündür, source:"خ ي ل,B001"}. Kuşatılanların kaleleri, münafıkların vaatleri ve toplu görünen kalabalık, hepsi bu tür gölgelerdir. Bu yüzden sure iki kez "görmedin mi" ve "görürdün" diye sorar: on birinci ayette münafıklara, yirmi birinci ayette dağa. On sekizinci ayetteki "baksın" fiili de gözle ve basiretle bir şeyi evirip çevirmektir {source:"ن ظ ر,B001"}. Ayetin sonundaki "haberdar" ismi de dışın karşısında içi anlatır: {ar:المخبر خلاف المنظر, tr:el-mahber hılâfu'l-manzar, gloss:iç yüz, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. İnsan kendi görünüşüne bakar, Allah ise iç yüzünü bilir. On üçüncü ve on dördüncü ayetlerdeki "topluluk" kelimesinin ailesinde de, göz bebeği sağlam olduğu halde görmeyen göz vardır: {ar:عين قائمة ذهب بصرها والحدقة صحيحة, tr:'aynun kâime, gloss:göz bebeği sağlam olduğu halde görme gücü gitmiş göz, source:"ق و م,B021"}. Bu iki ayet o topluluğu {ar:قَوْمٌ لَّا يَفْقَهُونَ, tr:kavmun lâ yefkahûn, gloss:anlamayan bir topluluk, source:59:13} ve akıl etmeyen bir topluluk diye anar. Kur'an bu körlüğü açıkça tarif eder: {ar:وَلَهُمْ أَعْيُنٌ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Münafıkların görünüşü de insanı hayran bırakır, ama onlar dayalı kütükler gibidir {source:63:4}. Sekizinci ayetteki fakirlerin durumu ise tersine bir yanılgıdır: bilmeyen kişi onları {ar:يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ, tr:yahsebuhumu'l-câhilu ağniyâ', gloss:bilmeyen onları zengin sanır, source:2:273}. Göz, burada da dışa bakıp içi kaçırır.

Kaynaklar: 59:2 فَٱعْتَبِرُوا ع ب ر B004, B002; 59:2 ٱلْأَبْصَٰرِ ب ص ر B002; 59:5 قَطَعْتُم ق ط ع B003; 59:3 ٱلْجَلَآءَ ج ل و B002; 59:2 ظَنُّوا ظ ن ن B003, B006; 59:14 تَحْسَبُهُمْ ح س ب B002; 59:6 خَيْلٍ خ ي ل B001; 59:18 وَلْتَنظُرْ ن ظ ر B001; 59:18 خَبِيرٌ خ ب ر B001; 59:13/14 قَوْمٌ ق و م B021

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

