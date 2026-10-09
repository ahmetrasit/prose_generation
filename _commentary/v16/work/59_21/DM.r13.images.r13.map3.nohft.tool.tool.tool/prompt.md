Focus: 59:21. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_21/D.r13/context.md =====
# 59:21 — focus

لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَوْ | لَو |  | COND |
| 2 | أَنزَلْنَا | أَنزَلَ | ن ز ل | V;PRON |
| 3 | هَٰذَا | هَٰذَا |  | DEM |
| 4 | ٱلْقُرْءَانَ | قُرْءَان | ق ر ء | DET;PN |
| 5 | عَلَىٰ | عَلَىٰ |  | P |
| 6 | جَبَلٍ | جَبَل | ج ب ل | N |
| 7 | لَّرَأَيْتَهُۥ | رَءَا | ر ء ي | EMPH;V;PRON |
| 8 | خَٰشِعًا | خَاشِع | خ ش ع | N |
| 9 | مُّتَصَدِّعًا | مُّتَصَدِّع | ص د ع | N |
| 10 | مِّنْ | مِن |  | P |
| 11 | خَشْيَةِ | خَشْيَة | خ ش ي | N |
| 12 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 13 | وَتِلْكَ | ذَٰلِك |  | REM;DEM |
| 14 | ٱلْأَمْثَٰلُ | مَثَل | م ث ل | DET;N |
| 15 | نَضْرِبُهَا | ضَرَبَ | ض ر ب | V;PRON |
| 16 | لِلنَّاسِ | نَّاس | ن و س | P;DET;N |
| 17 | لَعَلَّهُمْ | لَعَلّ |  | ACC;PRON |
| 18 | يَتَفَكَّرُونَ | يَتَفَكَّرُ | ف ك ر | V;PRON |


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
- 59:14 لَا يُقَٰتِلُونَكُمْ جَمِيعًا إِلَّا فِى قُرًۭى مُّحَصَّنَةٍ أَوْ مِن وَرَآءِ جُدُرٍۭ ۚ بَأْسُهُم بَيْنَهُمْ شَدِيدٌۭ ۚ تَحْسَبُهُمْ جَمِيعًۭا وَقُلُوبُهُمْ شَتَّىٰ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ
- 59:15 كَمَثَلِ ٱلَّذِينَ مِن قَبْلِهِمْ قَرِيبًۭا ۖ ذَاقُوا۟ وَبَالَ أَمْرِهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- 59:16 كَمَثَلِ ٱلشَّيْطَٰنِ إِذْ قَالَ لِلْإِنسَٰنِ ٱكْفُرْ فَلَمَّا كَفَرَ قَالَ إِنِّى بَرِىٓءٌۭ مِّنكَ إِنِّىٓ أَخَافُ ٱللَّهَ رَبَّ ٱلْعَٰلَمِينَ
- 59:17 فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- 59:18 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- 59:19 وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- 59:20 لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- 59:21 ◀ focus لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- 59:22 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- 59:23 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- 59:24 هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/work/59_21/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ز ل (root_001492) — identity root of أَنزَلْنَا (w2)

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

## ق ر ء (root_001210) — identity root of ٱلْقُرْءَانَ (w4)

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

## ق ر ء (root_001211) — identity root of ٱلْقُرْءَانَ (w4)

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

## ج ب ل (root_000217) — identity root of جَبَلٍ (w6)

- **B001** dağ — dağ · dağlar
  تجمع الشيء في ارتفاع؛ الجبل معروف (maqayis)؛ اسم لكل وتد من أوتاد الأرض إذا عظم وطال (ayn;tahdhib)؛ الجبل واحد الجبال (sihah)؛ الجبل جمعه أجبال وجبال (mufradat)
- **B002** çok büyük topluluk ya da çok miktarda mal — çok büyük insan topluluğu · büyük insan topluluğu veya geçmiş bir halk · çok miktarda mal · nüfusu çok kalabalık topluluk
  الجبل الجماعة العظيمة الكثيرة (maqayis)؛ الخلق الجبلة وكل أمة مضت فهي جبلة (ayn)؛ الجبل من الناس الجماعة (jamhara;sihah)؛ الجبل الناس الكثير (tahdhib)؛ الجماعة العظيمة جبل (mufradat)؛ مال جبل أي كثير (jamhara;sihah;tahdhib)
- **B003** bedensel irilik ve kalınlık; kalın ve kuru olma — iri ve kalın yapılı kimse · iri ve kalın yapılı · iri ve kalın yapılı kadın · hörgüç veya yaradılıştaki bedensel irilik · yüz derisi ya da baş derisi ve kemikleri kalın · kalın ve kuru şey
  الناقة العظيمة السنام جبلة؛ امرأة جبلة عظيمة الخلق (maqayis)؛ رجل جبل الوجه غليظ بشرة الوجه؛ رجل جبل الرأس غليظ جلد الرأس والعظام (ayn;tahdhib)؛ ذو جبلة إذا كان غليظ الجسم (jamhara;mufradat)؛ شيء جبل غليظ جاف؛ الجبلة السنام؛ امرأة مجبال غليظة الخلق (sihah)
- **B004** doğuştan yapı ve ona göre biçimlenme — doğuştan yapı, yaradılış ve huy · onu yarattı ve belli bir yapıyla donattı · insanı bir işe doğuştan yatkın kıldı · yaratılmış veya belli bir huyda biçimlenmiş kimseler · dağın yaratılıştan gelen yapısının kuruluşu
  الجبلة الخليقة (maqayis)؛ جبلة كل مخلوق توسه الذي طبع عليه؛ جبل الإنسان على هذا الأمر أي طبع عليه (ayn)؛ الجبلة الفطرة؛ خليقته التي خلق عليها (jamhara)؛ جبله الله أي خلقه؛ الجبلة الخلقة (sihah)؛ الجبل الخلق جبلهم الله فهم مجبولون؛ جبل الإنسان على هذا الأمر أي طبع عليه (tahdhib)؛ جبله الله على كذا؛ الطبع الذي يأبى على الناقل نقله (mufradat)
- **B005** kazarken kazılamayan sert zemine ulaşma [kalıp] — yerin sertliği · kazıda kazılamayan sert yere ulaşmak
  حفر القوم فأجبلوا إذا بلغوا مكانا صلبا (maqayis)؛ جبلة الأرض صلابها (ayn)؛ أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه (jamhara)؛ أجبل القوم إذا حفروا فبلغوا المكان الصلب (sihah)
- **B006** dağlara varma veya girme — topluluk dağa veya dağlara vardı · dağların içine girdiler
  أجبل القوم أي صاروا في الجبال وتجبلوا أي دخلوها (ayn;tahdhib)؛ أجبل القوم أي صاروا إلى الجبل (sihah)
- **B007** dokuması, ipliği ve bükümü iyi kumaş [kalıp] — dokuması, ipliği ve bükümü iyi kumaş
  الثوب الجيد النسج والغزل والفتل جيد الجبلة (ayn;tahdhib)؛ ثوب جيد الجبلة (mufradat)
- **B008** kurumuş ağaç — kurumuş ağaç veya ağaçlar
  الجبل الشجر اليابس (ayn;tahdhib)
- **B009** sözün tıkanması veya engelleme — ozanın söz söylemekte zorlanması · engelleme veya alıkonma alanındaki şey
  أجبل الشاعر إذا صعب عليه القول (jamhara)؛ المجبل في المنع (tahdhib)
- **B010** birini bir işi yapmaya zorlamak [kalıp] — birini belirli bir işi yapmaya zorlamak
  اجتبلت فلانا على أمر وجبلته أي أجبرته (tahdhib)
- **B011** geniş ve uzun kum sırtına rastlamak — geniş ve uzun bir kum sırtına rastlamak
  أجبل إذا صادف جبلا من الرمل وهو العريض الطويل؛ أحبل إذا صادف حبلا من الرمل وهو الدقيق الطويل (tahdhib)
- **B012** topluluğun önderi veya bilgini; ileri gelenler — topluluğun önderi ve bilgini · bir topluluğun önderleri ve ileri gelenleri
  الجبل سيد القوم وعالمهم؛ هؤلاء جبال بني فلان؛ أي سادتهم (tahdhib)

## ر ء ي (root_000531) — identity root of لَّرَأَيْتَهُۥ (w7)

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

## خ ش ع (root_000412) — identity root of خَٰشِعًا (w8)

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

## ص د ع (root_000850) — identity root of مُّتَصَدِّعًا (w9)

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

## خ ش ي (root_000413) — identity root of خَشْيَةِ (w11)

- **B001** korku duyma — korku; özellikle saygı ve bilgiyle karışan korku · korkmak · korkan erkek · korkan kadın · ondan daha çok korku duydum · bu yer ötekinden daha çok korku verir · onu korkuttu
  الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذاك أي أفزعه (ayn)؛ خشي الرجل يخشى خشية أي خاف فهو خشيان والمرأة خشياء؛ كنت أشد خشية منه؛ هذا المكان أخشى أي أشد خوفا؛ خشاه تخشية أي خوفه (sihah)؛ الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذلك المكان؛ معناها من الآدميين الخوف (tahdhib)؛ الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم (mufradat)؛ يدل على خوف وذعر فالخشية الخوف ورجل خشيان؛ كنت أشد خشية منه؛ هذا المكان أخشى من ذلك أي أشد خوفا (maqayis)
- **B002** bilmek — bildim
  خشيت بأن من تبع الهدى معناه علمت (sihah)؛ فخشينا أي فعلمنا (tahdhib)؛ المجاز قولهم خشيت بمعنى علمت؛ أي علمت (maqayis)
- **B003** istememe ve hoşnutsuzluk [kalıp] — Tanrı'ya yüklenen kullanımda istememe ve hoşnutsuzluk
  فخشينا أن يرهقهما طغيانا وكفرا قال الأخفش معناه كرهنا (sihah)؛ فخشينا عن الله لأن الخشية من الله تعالى معناها الكراهة ومعناها من الآدميين الخوف (tahdhib)
- **B004** kuruyup sertleşmiş veya buruşup niteliğini yitirmiş olma — buruşmuş, düşük nitelikli hurma · hurma ağacı buruşmuş, düşük nitelikli meyve verdi · kuru et
  الخشي وهو اليابس؛ الخشو الحشف من التمر؛ خشت النخلة تخشو إذا أحشفت (sihah)؛ مما شذ عن الباب وقد يمكن الجمع بينهما على بعد الخشو التمر الحشف؛ خشت النخلة تخشو خشوا؛ الخشي من اللحم اليابس (maqayis)

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w12)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## م ث ل (root_001397) — identity root of ٱلْأَمْثَٰلُ (w14)

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

## ض ر ب (root_000906) — identity root of نَضْرِبُهَا (w15)

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

## ء ن س (root_000059) — identity root of لِلنَّاسِ (w16)

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

## ف ك ر (root_001172) — identity root of يَتَفَكَّرُونَ (w18)

- **B001** bir şeyi akıl yoluyla zihinde evirip çevirerek inceleme — düşünme; zihinsel inceleme · düşünce; zihinsel inceleme gücü · derinlemesine düşünme ve inceleme · düşünme; zihinde tartma · işi üzerine düşünüp tartmak · düşünüp değerlendirmek · bir şey üzerine düşünüp incelemek · çok düşünen; düşünmeye düşkün · düşünce anlamındaki seyrek bir ad
  تردد القلب في الشيء (maqayis)؛ الفكر اسم التفكر والفكرة والفكر واحد (ayn)؛ التفكر التأمل والاسم الفكر والفكرة (sihah)؛ التفكر اسم للتفكير وكل ذلك معناه واحد (tahdhib)؛ الفكرة قوة مطرقة للعلم إلى المعلوم والتفكر جولان تلك القوة بحسب نظر العقل (mufradat)؛ رجل فكير كثير الفكر (maqayis)؛ رجل فكير كثير التفكر (ayn;sihah)؛ رجل فكير كثير الإقبال على التفكر والفكرة (tahdhib)؛ رجل فكير كثير الفكرة (mufradat)
- **B002** bu işte bir gereksinimim yok [kalıp] — bu işte bir gereksinimim yok
  يقال ليس لي في هذا الأمر فكر أي ليس لي فيه حاجة؛ الفتح فيه أفصح من الكسر

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ر و ي (root_000615) — for لَّرَأَيْتَهُۥ (w7): withheld observed target; not identity

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

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:21, and ## Buluşmalar) =====
## Yarılan kaya, dağılan topluluk, yarılan toprak

Dördüncü ayet sürgünün sebebini söyler: {ar:ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ, tr:zâlike bi-ennehum şâkku'llâhe ve resûleh, gloss:bu, onların Allah'a ve Resulüne karşı ayrılığa düşmeleri yüzündendir, source:59:4}. Bu fiilin kökü yarmaktır: {ar:شققت الشيء أشقه شقا إذا صدعته, tr:şekaktu'ş-şey', gloss:bir şeyi çatlattığımda "yardım" denir, source:"ش ق ق,B001"}. Topluluk için de kullanılır: {ar:الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت, tr:eş-şikâk, gloss:şikâk ayrılıktır; topluluk çatlayıp dağıldığında olur, source:"ش ق ق,B004"}. Bu tanımdaki "çatlamak" fiili, yirmi birinci ayetteki dağın {ar:مُّتَصَدِّعًا, tr:mutesaddi'an, gloss:parçalanmış, çatlamış, source:59:21} haliyle aynı köktendir. Kökün bir dalı topluluğun dağılmasını da anlatır: {ar:تصدع القوم إذا تفرقوا, tr:tesadda'a'l-kavm, gloss:topluluk dağılınca "tesadda'a" denir, source:"ص د ع,B005"}. Böylece dördüncü ve yirmi birinci ayetler aynı kelime alanına girer. Allah'a karşı ayrılığa düşenlerin bu yarılması kendi içlerine döner. On dördüncü ayet şöyle der: {ar:بَأْسُهُم بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ, tr:be'suhum beynehum şedîd, tahsebuhum cemî'an ve kulûbuhum şettâ, gloss:kendi aralarındaki çekişmeleri şiddetlidir; onları toplu sanırsın, oysa kalpleri dağınıktır, source:59:14}. "Şettâ" kelimesi, kenetlenmenin kalkmasıdır: {ar:ارتفاع الالتئام بينهما, tr:irtifâ'u'l-iltiâm beynehumâ, gloss:ikisi arasındaki kaynaşmanın kalkması, source:"ش ت ت,B003"}. "Aralarında" kelimesi de hem bağı hem kopuşu taşır: {ar:البين الفراق, tr:el-beyn el-firâk, gloss:beyn ayrılıktır, source:"ب ي ن,B001"}. Aynı kelime bir yerde de "bağ" anlamındadır {source:"ب ي ن,B003"}. "Toplu" kelimesinin ailesinde ise "dağınık" kelimesiyle aynı ifadede geçen bir anlam vardır: {ar:جماع الناس أخلاطهم وهم الأشابة من قبائل شتى, tr:cimâ'u'n-nâs, gloss:insanların cimâı, dağınık kabilelerden gelmiş karışık kalabalıktır, source:"ج م ع,B002"}. Yani dışarıdan toplu görünen şey, içten derlenip toplanmış bir yığından ibarettir. Kur'an bu cezayı başka bir yerde açıkça sayar: {ar:أَوْ يَلْبِسَكُمْ شِيَعًا وَيُذِيقَ بَعْضَكُم بَأْسَ بَعْضٍ, tr:ev yelbisekum şiya'an ve yuzîka ba'dakum be'se ba'd, gloss:ya da sizi gruplara ayırıp kiminize kiminizin şiddetini tattırmaya, source:6:65}. Dağılanlar işlerini {ar:فَتَقَطَّعُوٓا۟ أَمْرَهُم بَيْنَهُمْ زُبُرًا, tr:fe-tekatta'û emrehum beynehum zuburâ, gloss:işlerini aralarında parça parça böldüler, source:23:53} de bölmüşlerdir. Dördüncü ayetin sözleri Bedir için de aynen söylenir {source:8:13}. Yüz çevirenler için başka bir yerde {ar:فَإِنَّمَا هُمْ فِى شِقَاقٍ, tr:fe-innemâ hum fî şikâk, gloss:onlar ancak bir ayrılık içindedir, source:2:137} denir. Toplu sanılan kalabalığın sonu da bellidir: {ar:سَيُهْزَمُ ٱلْجَمْعُ وَيُوَلُّونَ ٱلدُّبُرَ, tr:se-yuhzemu'l-cem'u ve yuvellûne'd-dubur, gloss:o topluluk bozguna uğrayacak ve arkalarını dönüp kaçacaklar, source:54:45}. Müminlere ise bunun tersi verilmiştir: {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًا, tr:fe-ellefe beyne kulûbikum fe-asbahtum bi-ni'metihî ihvânâ, gloss:kalplerinizi birleştirdi de onun nimetiyle kardeş oldunuz, source:3:103}. Bu birleştirme, malla yapılabilecek bir iş de değildir {source:8:63}. Onuncu ayetteki {ar:وَلِإِخْوَٰنِنَا, tr:ve li-ihvâninâ, gloss:ve kardeşlerimize, source:59:10} duası bunun içindir.

Yarılmanın bir de bereketli yüzü vardır. Dokuzuncu ayetin "kurtuluşa erenler" kelimesi, kökünde yarmaktır: {ar:أصل يدل على شق, tr:aslun yedullu 'alâ şakk, gloss:yarmayı gösteren kök, source:"ف ل ح,B001"}. Çiftçi de toprağı yardığı için bu kelimeyle anılır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan, gloss:toprağı yardığı için ırgata "fellâh" denildi, source:"ف ل ح,B003"}. "Kâfir" kelimesi ise tohumu toprakla örten ekici de demektir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfir ez-zâri', gloss:kâfir, tohumu toprakla örttüğü için ekicidir, source:"ك ف ر,B008"}. Toprağı yaran filiz de "sad'" kökündendir: {ar:الصدع النبات لأنه يصدع الأرض, tr:es-sad' en-nebât, gloss:toprağı yardığı için bitkiye sad' denir, source:"ص د ع,B003"}. Böylece surede iki tür yarılma vardır. Biri, Allah'tan ayrılığa düşüp kendi içinden dağılmaktır. Öbürü, toprağı yarıp örtülü tohumu filizlendiren yarılmadır. Kur'an bu ikinci yarılmayı açıkça anlatır: {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّا, tr:summe şekaknâ'l-arda şakkâ, gloss:sonra toprağı iyice yardık, source:80:26}. Sekizinci ayetteki muhacirlerin tarifi, başka bir surede bir ekin benzetmesine bağlanır. Peygamberin yanındakiler orada da {ar:يَبْتَغُونَ فَضْلًا مِّنَ ٱللَّهِ وَرِضْوَٰنًا, tr:yebteğûne fadlen mina'llâhi ve ridvânâ, gloss:Allah'tan lütuf ve rıza ararlar, source:48:29} diye anılır ve {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ, tr:ke-zer'in ahrace şat'eh, gloss:filizini çıkarmış bir ekin gibi, source:48:29} oldukları söylenir. Bu ekin {ar:يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ, tr:yu'cibu'z-zurrâ'a li-yeğîza bihimu'l-kuffâr, gloss:ekicileri hayran bırakır, onlarla kâfirleri öfkelendirir, source:48:29}. Burada "küffâr" kelimesi ekicilerin hemen yanında durur. Dünya hayatı da {ar:كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ, tr:ke-meseli ğaysin a'cebe'l-kuffâra nebâtuh, gloss:bitkisi ekicileri hayran bırakan bir yağmur gibidir, source:57:20} diye anlatılır. Bu ayette "küffâr" kelimesi ekiciler anlamına daha da yakındır.

Kaynaklar: 59:4 شَآقُّوا ش ق ق B001, B004; 59:21 مُّتَصَدِّعًا ص د ع B005, B003; 59:14 شَتَّىٰ ش ت ت B003; 59:14 بَيْنَهُمْ ب ي ن B001, B003; 59:14 جَمِيعًا ج م ع B002; 59:9 ٱلْمُفْلِحُونَ ف ل ح B001, B003; 59:2/11 كَفَرُوا ك ف ر B008

## Dağa inen söz

Yirmi birinci ayet bir varsayım kurar: {ar:لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍ لَّرَأَيْتَهُۥ خَٰشِعًا مُّتَصَدِّعًا مِّنْ خَشْيَةِ ٱللَّهِ, tr:lev enzelnâ hâze'l-Kur'âne 'alâ cebelin le-raeytehû hâşi'an mutesaddi'an min haşyeti'llâh, gloss:bu Kur'an'ı bir dağa indirseydik, onu Allah korkusundan baş eğmiş, parça parça olmuş görürdün, source:59:21}. Bu sahnenin her kelimesi yağmur ve kuru toprak alanına da açılır. "İndirmek" fiili yağmurun inişini anlatır: {ar:نزل المطر من السماء نزولا, tr:nezele'l-matar mine's-semâ', gloss:yağmur gökten indi, source:"ن ز ل,B001"}. "Dağ" kelimesinin ailesi kaba ve kuru olanı adlandırır: {ar:شيء جبل غليظ جاف, tr:şey'un cibl ğalîz câff, gloss:kaba ve kuru şey, source:"ج ب ل,B003"}. Kazıcının kazamadığı kayaya varmasını anlatan bir ifade de vardır: {ar:أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه, tr:ecbele'l-hâfir, gloss:kazıcı kazamayacağı kayaya ulaşınca "ecbele" denir, source:"ج ب ل,B005"}. "Hâşi'" kelimesi gözünü yere indirmektir, ama aynı zamanda yağmursuz kalıp kurumuş topraktır: {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşa'at, gloss:toprak kuruyup yağmur almayınca "haşaat" denir, source:"خ ش ع,B002"}. "Korku" (haşyet) kelimesinin bir dalı da kurumuş olandır: {ar:الخشي وهو اليابس, tr:el-haşiyy, gloss:haşiyy kuru olandır, source:"خ ش ي,B004"}. Asıl anlamı ise bilgiden doğan saygılı bir korkudur: {ar:الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم, tr:el-haşye havfun yeşûbuhû ta'zîm, gloss:haşyet, yüceltmeyle karışık ve çoğu zaman bilgiden doğan korkudur, source:"خ ش ي,B001"}. "Parça parça olmuş" kelimesi de daha önce gördüğümüz gibi toprağı yaran filizi anlatır. Böylece dağ, üzerine yağmur inmiş kurak bir toprak gibidir. Önce susuzluktan yere çöker, sonra yarılır. Kur'an bu iki adımı başka bir yerde açıkça gösterir: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşi'aten fe-izâ enzelnâ 'aleyhe'l-mâe'htezzet ve rabet, gloss:toprağı kupkuru görürsün, üzerine suyu indirdiğimizde titreşir ve kabarır, source:41:39}. Ayetin sonundaki {ar:وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ, tr:ve tilke'l-emsâlu nadribuhâ li'n-nâs, gloss:bu misalleri insanlara veriyoruz, source:59:21} ifadesindeki "vermek" fiili de toprağa yağmurla vurmak anlamını taşır: {ar:ضرب الأرض بالمطر, tr:darbu'l-ard bi'l-matar, gloss:toprağa yağmurla vurmak, source:"ض ر ب,B013"}. Misal, bu ailede ibret demektir {source:"م ث ل,B011"}. Ayetin bitişi olan "düşünsünler" ise kalbin bir şey üzerinde gidip gelmesidir {source:"ف ك ر,B001"}.

Bu sahne, surenin geri kalanında ters bir aynayı tutar. Kalelerine güvenenler, dağın bile taşıyamadığı sözün karşısında katı kalmıştır. On üçüncü ayet onların korkusunun yanlış yöne gittiğini söyler. Onların gözünde müminler Allah'tan daha korkutucudur. Dağın "haşyet"i ise doğru yöne gider. Bir başka surede bazı insanlar için {ar:يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةً, tr:yahşevne'n-nâse ke-haşyeti'llâhi ev eşedde haşye, gloss:insanlardan Allah'tan korkar gibi, hatta daha çok korkarlar, source:4:77} denir. Taştan kalplere dair başka bir ayette bazı taşların bu sahneyi zaten yaşadığı söylenir: {ar:وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ, tr:ve inne minhâ le-mâ yeşşakkaku fe-yahrucu minhu'l-mâ', ve inne minhâ le-mâ yahbitu min haşyeti'llâh, gloss:taşlardan kimi yarılır da içinden su çıkar, kimi de Allah korkusundan yuvarlanıp düşer, source:2:74}. Musa'nın gördüğü dağ da tecelliye dayanamaz: {ar:فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ جَعَلَهُۥ دَكًّا, tr:fe-lemmâ tecellâ rabbuhû li'l-cebeli ce'alehû dekkâ, gloss:Rabbi dağa tecelli edince onu darmadağın etti, source:7:143}. Kur'an'ın dağları yürütebileceği varsayımı da aynı kuruluşu taşır {source:13:31}. Dağların taşımaktan çekindiği emanet de bu sahnenin yanında durur {source:33:72}. Beşinci ayetteki hurma adı "lîne"nin kökü de bu katılığın cevabını taşır: {ar:تلين جلودهم وقلوبهم إلى ذكر الله, tr:telînu culûduhum ve kulûbuhum ilâ zikri'llâh, gloss:derileri ve kalpleri Allah'ın zikrine yumuşar, source:"ل ي ن,B005"}. Bu ifade, Kur'an'ın kendi tasvirindeki sözlerle aynıdır {source:39:23}. Müminlerin kalplerinin "haşyet"e erme zamanının gelmediği mi diye sorulur. Hemen yanında, kalpleri katılaşmış olanlar ve ardından ölü toprağın diriltilmesi anılır {source:57:16}. Kur'an dinlendiğinde yere kapananlar da {ar:وَيَزِيدُهُمْ خُشُوعًا, tr:ve yezîduhum huşû'â, gloss:bu onların huşuunu artırır, source:17:109} diye anlatılır.

Kaynaklar: 59:21 أَنزَلْنَا ن ز ل B001; 59:21 جَبَلٍ ج ب ل B003, B005; 59:21 خَٰشِعًا خ ش ع B002; 59:21 مُّتَصَدِّعًا ص د ع B003; 59:21 خَشْيَةِ خ ش ي B001, B004; 59:21 نَضْرِبُهَا ض ر ب B013; 59:21 ٱلْأَمْثَٰلُ م ث ل B011; 59:21 يَتَفَكَّرُونَ ف ك ر B001; 59:5 لِّينَةٍ ل ي ن B005

## Gece örtüsü ve açılan gün

Surede örtmek anlamı taşıyan birçok kelime vardır. "Küfür" kelimesinin kökü örtmektir: {ar:الستر والتغطية, tr:es-setr ve't-tağtiye, gloss:örtme ve kapama, source:"ك ف ر,B001"}. Bu kökte gece de kâfirdir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfir, gloss:gece, karanlığıyla örttüğü için "kâfir"dir, source:"ك ف ر,B002"}. Onuncu ayetteki bağışlanma duası da aynı örtme alanındadır: {ar:الغفر الستر, tr:el-ğafr es-setr, gloss:ğafr örtmektir, source:"غ ف ر,B001"}. "Cennet" de gecenin karanlığıdır: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyl, gloss:gecenin cenânı, karanlığı ve eşyayı örtmesidir, source:"ج ن ن,B002"}. Nifak da bir örtüdür: {ar:النفاق لأن صاحبه يكتم خلاف ما يظهر, tr:en-nifâk, gloss:nifak, sahibinin gösterdiğinin tersini gizlemesidir, source:"ن ف ق,B004"}. On dördüncü ayetteki "ardından" kelimesi de saklamayı anlatır: {ar:التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره, tr:et-tevriye es-setr, gloss:tevriye örtmedir; haberi gizleyip başkasını gösterdiğinde "verraytu" dersin, source:"و ر ي,B005"}. Bu yüzden münafıkların duvar arkasında savaşması ile sözlerinin arkasına gizlenmesi aynı kelimeyle işitilir. Tek fark, bir örtünün kurtarması, ötekinin boğmasıdır. Onuncu ayette istenen bağış örtüsü, kişiyi koruyan bir örtüdür. Küfür ve nifak örtüsü ise onu karanlıkta bırakır. On yedinci ayetteki "zalimler" kelimesi karanlığın kendisidir: {ar:الظلمة خلاف النور, tr:ez-zulme hılâfu'n-nûr, gloss:zulmet nurun karşıtıdır, source:"ظ ل م,B001"}. Ayette geçen "ateş" kelimesi ise ışıkla aynı yoldan adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan adlandırılmıştır, source:"ن و ر,B002"}. Ama ateş burada aydınlatmaz, yakar. Münafıklar da bir ateş yakar ama Allah ışıklarını götürür ve onları {ar:فِى ظُلُمَٰتٍ لَّا يُبْصِرُونَ, tr:fî zulumâtin lâ yubsırûn, gloss:göremedikleri karanlıklarda, source:2:17} bırakır. Kıyamette münafıklar müminlerin ışığından almak ister, onlara {ar:ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًا, tr:irci'û verâekum fe'ltemisû nûrâ, gloss:arkanıza dönün de bir ışık arayın, source:57:13} denir. Hemen ardından iki tarafı birbirinden ayıran bir sur çekilir {source:57:13}. Bu ayette surun ardı, ışık ve ayrılık, bu surenin kale, "ardında" ve karanlık kelimeleri bir arada bulunur.

Örtünün karşısında sabah açılır. Yirmi birinci ayetteki "parça parça olmuş" kelimesinin ailesinde sabah da vardır: {ar:الصديع الصبح, tr:es-sadî' es-subh, gloss:sadî' sabahtır, source:"ص د ع,B006"}. Dokuzuncu ayetteki "nefisler" kelimesi de sabahın nefes almasıdır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subh, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Kur'an aynı ifadeyi yemin olarak kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. On sekizinci ayetteki "yarın" kelimesi de seher vaktidir: {ar:الغدوة ما بين صلاة الغداة وطلوع الشمس, tr:el-ğudve, gloss:ğudve, sabah namazı ile güneşin doğuşu arasıdır, source:"غ د و,B001"}. Üçüncü ayetteki "sürgün" (celâ) kelimesi de açığa çıkıp görünür olmaktır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey' ve burûzuh, gloss:bir şeyin açılıp ortaya çıkması, source:"ج ل و,B001"}. Bu kelimenin bir dalı da gündüzün beyazlığıdır {source:"ج ل و,B007"}. Kur'an bu fiili gündüz için kullanır: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Sürgün edilenler kalelerinden çıkarılıp açık alana konur. Gece onları örtüyordu, şimdi her şey gün ışığına çıkar. Yirmi ikinci ayet bu iki yarıyı Allah'ın bilgisinde birleştirir: {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ, tr:'âlimu'l-ğaybi ve'ş-şehâde, gloss:görünmeyeni ve görüneni bilen, source:59:22}. "Gayb" kelimesinin kökü gözlerden gizlenmektir, güneşin batmasına da bu kökle "gâbet" denir {source:"غ ي ب,B001"}. "Şehâdet" ise oradan bakıp görmektir {source:"ش ه د,B001"}. Yirmi birinci ayetteki "hâşi'" kelimesi de batmaya yaklaşan yıldızlar için kullanılır: {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşa'ati'l-kevâkib, gloss:yıldızlar batmaya yaklaşınca "haşaat" denir, source:"خ ش ع,B003"}. Böylece batan yıldızla doğan sabah aynı ayette yan yana durur. Gece ile gündüzde gizlenen ile açıkta yürüyenin Allah katında eşit olduğu da söylenir {source:13:10}.

Kaynaklar: 59:2 كَفَرُوا ك ف ر B001, B002; 59:10 ٱغْفِرْ غ ف ر B001; 59:20 ٱلْجَنَّةِ ج ن ن B002; 59:11 نَافَقُوا ن ف ق B004; 59:14 وَرَآءِ و ر ي B005; 59:17 ٱلظَّٰلِمِينَ ظ ل م B001; 59:3 ٱلنَّارِ ن و ر B002; 59:21 مُّتَصَدِّعًا ص د ع B006; 59:9 أَنفُسِهِمْ ن ف س B009; 59:18 لِغَدٍ غ د و B001; 59:3 ٱلْجَلَآءَ ج ل و B001, B007; 59:22 ٱلْغَيْبِ غ ي ب B001; 59:22 ٱلشَّهَٰدَةِ ش ه د B001; 59:21 خَٰشِعًا خ ش ع B003

## Misafir sofrası

Dokuzuncu ayetteki karşılama bir misafir ağırlama sahnesi olarak da işitilir. Yedinci ayetteki "kasabalar" kelimesi, ailesinde misafirin etrafında toplandığı büyük tası anlatır: {ar:المقراة الجفنة سميت لاجتماع الضيف عليها, tr:el-mikrâ el-cefne, gloss:mikrâ, misafirlerin etrafında toplandığı için bu adı alan büyük tastır, source:"ق ر ي,B003"}. Misafire ikram da aynı köktendir: {ar:القرى الإحسان إلى الضيف, tr:el-kırâ el-ihsân ile'd-dayf, gloss:kırâ misafire ikramdır, source:"ق ر ي,B003"}. Yirmi birinci ayetteki "indirmek" fiili de konuğa hazırlanan yemeği anlatır: {ar:النزل ما يهيأ للنزيل, tr:en-nuzul mâ yuheyye'u li'n-nezîl, gloss:nuzul, konuk için hazırlanan şeydir, source:"ن ز ل,B005"}. Kur'an'ın indirilişi böylece hem yağmurun hem de konuğa sunulan sofranın sesini taşır. "Ehl" kelimesi de karşılama sözünün içindedir: {ar:مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش, tr:merhaben ve ehlen, gloss:genişliğe ve ailene geldin, ısın, yabancılık çekme, source:"ء ه ل,B005"}. Dokuzuncu ayet bu karşılamayı açık bir dille söyler: {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ, tr:ve yu'sirûne 'alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri darlık içinde olsalar bile onları kendilerine tercih ederler, source:59:9}. "Esîr" kelimesi, kişinin lütfuyla öne çıkardığı değerli insandır: {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-esîr el-kerîm 'aleyk, gloss:esîr, lütfun ve ikramınla öne geçirdiğin değerli kişidir, source:"ء ث ر,B005"}. Bu ifadedeki "fazl" (lütuf) kelimesi sekizinci ayette de geçer. Muhacirler Allah'tan lütuf ararken, Ensar onlara kendi lütfundan verir. "Fazl" da birine kendi fazlasından vermektir {source:"ف ض ل,B003"}. Yedinci ayetteki "yoksullar" kelimesinin ailesinde ise insanın yanında ısındığı ateş vardır {source:"س ك ن,B004"}. On sekizinci ayetteki "yarın" kelimesi de sabah yemeğidir {source:"غ د و,B004"}. İbrahim'in misafir ağırlaması bu sahnenin Kur'an'daki örneğidir: {ar:فَجَآءَ بِعِجْلٍ سَمِينٍ, tr:fe-câe bi-'iclin semîn, gloss:semiz bir buzağı getirdi, source:51:26}, {ar:فَقَرَّبَهُۥٓ إِلَيْهِمْ, tr:fe-karrabehû ileyhim, gloss:onu önlerine koydu, source:51:27}. Dokuzuncu ayetteki tercih de sevilen şeyden yedirmektir: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا, tr:ve yut'ımûne't-ta'âme 'alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, sevdikleri halde yoksula, yetime ve esire yedirirler, source:76:8}. Orada da karşılık beklenmez {source:76:9}. On beşinci ayette ise tatma tersine döner. Tatmak önce yiyeceği tatmaktır {source:"ذ و ق,B001"}. Önceki topluluk ise sofrada değil, kendi işlerinin vebalinde tat alır.

Kaynaklar: 59:7 ٱلْقُرَىٰ ق ر ي B003; 59:21 أَنزَلْنَا ن ز ل B005; 59:2/7 أَهْلِ ء ه ل B005; 59:9 يُؤْثِرُونَ ء ث ر B005; 59:8 فَضْلًا ف ض ل B003; 59:7 ٱلْمَسَٰكِينِ س ك ن B004; 59:18 لِغَدٍ غ د و B004; 59:15 ذَاقُوا ذ و ق B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

