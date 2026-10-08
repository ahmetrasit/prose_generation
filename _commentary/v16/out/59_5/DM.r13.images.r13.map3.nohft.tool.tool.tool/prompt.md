Focus: 59:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_5/D.r13/context.md =====
# 59:5 — focus

مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ وَلِيُخْزِىَ ٱلْفَٰسِقِينَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مَا | مَا |  | COND |
| 2 | قَطَعْتُم | قُطِعَ | ق ط ع | V;PRON |
| 3 | مِّن | مِن |  | P |
| 4 | لِّينَةٍ | لِّينَة | ل ي ن | N |
| 5 | أَوْ | أَو |  | CONJ |
| 6 | تَرَكْتُمُوهَا | تَرَكَ | ت ر ك | V;PRON |
| 7 | قَآئِمَةً | قَآئِمَة | ق و م | N |
| 8 | عَلَىٰٓ | عَلَىٰ |  | P |
| 9 | أُصُولِهَا | أَصْل | ء ص ل | N;PRON |
| 10 | فَبِإِذْنِ | إِذْن | ء ذ ن | RSLT;P;N |
| 11 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 12 | وَلِيُخْزِىَ | أَخْزَيْ | خ ز ي | CONJ;PRP;V |
| 13 | ٱلْفَٰسِقِينَ | فَاسِق | ف س ق | DET;N |


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
- 59:5 ◀ focus مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ وَلِيُخْزِىَ ٱلْفَٰسِقِينَ
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


===== _commentary/v16/work/59_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ط ع (root_001240) — identity root of قَطَعْتُم (w2)

- **B001** kesip ayırmak — bir şeyi kesip ayırmak · eli kesilmiş kimse
  قطعته قطعا ومقطعا فانقطع؛ الأقطع المقطوع اليد (ayn)؛ قطعت الشئ قطعا؛ الأقطع المقطوع اليد (sihah)؛ القطع مصدر قطعت؛ وقطعن أيديهن أي قطعنها قطعا بعد قطع وخدشن فيها خدوشا كثيرة (tahdhib)؛ القطع فصل الشيء مدركا بالبصر كالأجسام؛ قطع الأعضاء؛ فقطع أمعاءهم (mufradat)؛ يدل على صرم وإبانة شيء من شيء؛ قطعت الشيء أقطعه قطعا (maqayis)
- **B002** ayrılmış parça — ayrılmış bölüm veya parça · gecenin bir bölümü
  القطعة طائفة من كل شيء؛ قطعة أرضي (ayn)؛ القطعة من الشئ الطائفة منه؛ قطعة من الأرض إذا كانت مفروزة (sihah)؛ اسم ما قطع فسقط قطع؛ أعطني قطعة؛ قطعة من أرض؛ المقطع الشيء اليسير منه (tahdhib)؛ قطع من الليل قطعة منه (mufradat)؛ القطع الطائفة من الليل كأنه قطعة؛ أقطعت الرجل إقطاعا كأنه طائفة قد قطعت من بلد (maqayis)
- **B003** kat edip geçmek [kalıp] — nehri veya suyu geçmek · yolda ilerleyip yolu kat etmek
  قطعت النهر قطوعا (ayn)؛ قطعت النهر قطوعا عبرته؛ مقاطع الأنهار حيث تعبر فيه (sihah)؛ قطعت النهر قطعا وقطوعا؛ المقطع الموضع الذي يقطع فيه النهر من المعابر (tahdhib)؛ قطع الطريق يراد به السير والسلوك؛ قطع الماء بالسباحة عبوره (mufradat)؛ قطعت النهر قطوعا إذا عبرته (maqayis)
- **B004** kuşların göç etmesi [kalıp] — kuşların bir bölgeden başka bölgeye gitmesi · gidip dönen kuşlar
  الطير تقطع في طيرانها قطوعا وهن قواطع أي ذواهب ورواجع (ayn)؛ قطعت الطير قطوعا وقطاعا خرجت من بلاد البرد إلى بلاد الحر فهي قواطع ذواهب أو رواجع (sihah)؛ قطعت الطير تقطع قطوعا إذا جاءت من بلد إلى بلد في وقت حر أو برد؛ قطعت الغربان إلينا في الشتاء قطوعا (tahdhib)؛ قطعت الطير قطوعا إذا خرجت من بلاد البرد إلى بلاد الحر أو من تلك إلى هذه (maqayis)
- **B005** sona erip kesilmek — bir şeyin zamanı veya varlığı bitmek · bir şeyin sona erdiği yer · kuyu suyunun azalması veya tükenmesi
  منقطع كل شيء حيث تنتهي غايته؛ انقطع الشيء ذهب وقته؛ انقطع البرد والحر (ayn)؛ قطع ماء الركية أي انقطع وذهب؛ منقطع الرمل حيث ينقطع ولا رمل خلفه؛ منقطع كل شيء حيث ينتهى إليه طرفه (sihah)؛ منقطع كل شيء حيث ينقطع مثل منقطع الرمل والحرة؛ أقطعت السماء إذا انقطع المطر؛ قطع ماء قليبكم إذا قل ماؤها وذهب (tahdhib)؛ أصاب بئرهم قطع أي انقطع ماؤها؛ مقاطع الأودية مآخيرها (mufradat)؛ منقطع الرمل ومقطعه حيث ينقطع؛ أصاب بئر فلان قطع إذا نقص ماؤها (maqayis)
- **B006** umudu kesilmek veya yolda kalmak [kalıp] — umudu kesilmek veya yolculukta kalmak · yolculuğu sürdüremeyen kimse
  قطع بفلان انقطع رجاؤه؛ رجل منقطع به؛ عجز عن سفره من نفقة ذهبت أو قامت عليه راحلته (ayn)؛ قطع بفلان فهو مقطوع به؛ انقطع به فهو منقطع به إذا عجز عن سفره (sihah)؛ قطع بالرجل إذا انقطع رجاؤه؛ رجل منقطع به إذا كان مسافرا فأبدع به وعطبت راحلته وذهب زاده وماله؛ أقطع عن أهله فهو مقطع عنهم (tahdhib)؛ لليائس من الشيء قد قطع به كأنه أمل أمله فانقطع (maqayis)
- **B007** bağı koparmak — ilişkiyi bırakma ve bağ kopukluğu · kopuşu bildiren işaret · akrabalık bağını ve iyiliği kesmek
  قاطع الرحم؛ قطع رحمه إذا هجرها؛ الأقطوعة علامة أنها صارمتها؛ الهجر مقطعة للود (ayn)؛ قطع رحمه قطيعة؛ رحم قطعاء؛ الأقطوعة علامة للصريمة والهجران؛ التقاطع ضد التواصل (sihah)؛ تقطعت أسبابهم ووصلهم؛ قطعت حبال مودتها؛ قطع فلان رحمه؛ اتقوا القطيعاء أي أن ينقطع بعضكم من بعض في الحرب (tahdhib)؛ قطع الوصل هو الهجران؛ قطع الرحم يكون بالهجران ومنع البر (mufradat)؛ القطيعة الهجران؛ تقاطع الرجلان إذا تصارما؛ أقطوعة علامة للصريمة (maqayis)
- **B008** bölüp dağıtmak [kalıp] — işlerini kendi aralarında bölüp ayırmak · onları yeryüzünde gruplara ayırmak · topluluğun dağılıp ayrılması
  قطعت عليه العذاب تقطيعا أي لونته وجزأته عليه (ayn)؛ تقطعوا أمرهم بينهم أي تقسموه (sihah)؛ قطعناهم في الأرض أمما أي فرقناهم فرقا؛ فتقطعوا أمرهم بينهم زبرا؛ قطع فلان على فلان العذاب إذا لون عليه ضروبا (tahdhib)؛ تقضع القوم تفرقوا وهذا من الإبدال أيضا (maqayis ibdal)
- **B009** iple boğulmak [kalıp] — iple boğulmak
  قطع الرجل بحبل أي اختنق؛ ثم ليقطع أي ليختنق (ayn)؛ ثم ليقطع قالوا ليختنق؛ يقطع نفسه من الأرض حتى يختنق (sihah)؛ أجمع المفسرون على أن تأويل ثم ليقطع ثم ليختنق؛ يقطع حياته ونفسه خنقا (tahdhib)؛ ليقطع أجله بالاختناق؛ ثم ليختنق (mufradat)؛ في قوله ثم ليقطع إنه الاختناق (maqayis)
- **B010** kesin karara bağlamak [kalıp] — işi kesinleştirip sonuca bağlamak · hakkın yanlıştan ayrıldığı karar noktası
  مقطع الحق موضع التقاء الحكم فيه وهو ما يفصل الحق من الباطل (ayn)؛ مقطع الحق حيث يفصل بين الخصوم بنص الحكم (tahdhib)؛ قطع الأمر فصله؛ ما كنت قاطعة أمرا (mufradat)
- **B011** kökünü kazımak [kalıp] — bir soyun devamını yok etmek · bir topluluğun bir bölümünü yok etmek
  ليقطع طرفا أي يهلك جماعة منهم؛ قطع دابر الإنسان هو إفناء نوعه؛ إلا أن تقطع قلوبهم أي إلا أن يموتوا وقيل إلا أن يتوبوا توبة بها تنقطع قلوبهم ندما
- **B012** giysi biçip dikmek [kalıp] — onlara giysi biçip dikildi · biçilmiş veya kısa giysiler · kumaşın gömlek olmaya yetmesi
  المقطعات من الثياب شبه الجباب؛ الثياب المختلفة الألوان؛ القطع من الثياب ضرب منها (ayn)؛ المقطعات من الثياب شبه الجباب؛ مقطعات الثياب والشعر قصارها؛ هذا الثوب يقطعك قميصا (sihah)؛ قطعت لهم ثياب من نار أي خيطت وسويت وجعلت لبوسا؛ المقطعات من الثياب كل ثوب يقطع من قميص وغيره؛ الثوب يقطعك قميصا (tahdhib)؛ قطع الثوب؛ قطعت لهم ثياب من نار (mufradat)؛ هذا الثوب يقطعك قميصا؛ المقطعات الثياب القصار (maqayis)
- **B013** pay ayırıp vermek [kalıp] — valinin araziden pay vermesi · dalları kesmeme izin verdi · bir şeyden bölüm ayırıp almak
  أقطع الوالي قطيعة أي طائفة من أرض الخراج؛ أقطعني قضبانا أذن لي قطعها؛ أقطع فلان من مال فلان طائفة (ayn)؛ أقطعته قضبانا أي أذنت له في قطعها؛ أقطعته قطيعة أي طائفة من أرض الخراج؛ اقتطعت قطيعا من غنم فلان (sihah)؛ أقطعني فلان نهرا إذا أذن له في حفره؛ أقطعني قضبانا من كرمه؛ قاطعت فلانا على كذا من الأجر والعمل (tahdhib)؛ أقطعت الرجل إقطاعا كأنه طائفة قد قطعت من بلد؛ أقطعت فلانا قضبانا من الكرم إذا أذنت له في قطعها (maqayis)
- **B014** kesici alet — kesmeye yarayan alet · keskin kılıç · kısa enli ok ucu
  المقطع كل شيء يقطع به؛ قاطع فلان وفلان سيفيهما أي نظرا أيهما أقطع؛ القطع نصل صغير يجعل في السهم (ayn)؛ المقطع ما يقطع به الشئ؛ القطع نصل قصير عريض السهم (sihah)؛ سيف قاطع وقطاع ومقطع؛ كل شيء يقطع به فهو مقطع؛ القطاع لا القاطع؛ القطع من النصال القصير العريض (tahdhib)؛ القطع النصل من السهام العريض كأنه لما بري قطع (maqayis)
- **B015** kesilmiş donatı nesnesi — kesik uçlu veya şeritlerden yapılmış kamçı · eyer altına serilen yaygı
  القطيع السوط المقطوع طرفه؛ القطع من الثياب ضرب منها (ayn)؛ القطع طنفسة يجعلها الراكب تحته؛ القطيع السوط (sihah)؛ القطع طنفسة تكون تحت الرحل؛ القطيع السوط المتقطع؛ سمي قطيعا لأنه يقطع أربع طاقات ثم يلوي (tahdhib)؛ القطيع السوط؛ القطع الطنفسة تلقى على الرحل وكأنها سميت بذلك لأن ناسجها يقطعها من غيرها (maqayis)
- **B016** hayvan sürüsü [kalıp] — koyun veya benzeri hayvan sürüsü
  القطيع طائفة من الغنم والنعم ونحوها (ayn)؛ القطيع الطائفة من البقر والغنم؛ اقتطعت قطيعا من غنم فلان (sihah)؛ القطيع من الغنم جمعه قطعان كالصرمة والفرقة (mufradat)؛ القطيع القطعة من الغنم (maqayis)
- **B017** hızla geride bırakmak — atın diğer atları geçip geride bırakması · çok hızlı tavşan · hızlı hızlı ardı ardına gelenler
  الفرس الجواد يقطع الخيل إذا خلفها ومضى؛ الأرنب السريعة مقطعة النياط؛ جاءت الخيل مقطوطعات أي سراعا بعضها في إثر بعض (ayn)؛ قطع الفرس الخيل تقطيعا أي خلفها ومضى؛ جاءت الخيل مقطوطعات أي سراعا بعضها في إثر بعض (sihah)؛ يقال للأرنب السريعة مقطعة النياط ومقطعة الأسحار؛ الفرس الجواد يقطع الخيل تقطيعا؛ ليس فيكم من تقطع عليه الأعناق مثل أبي بكر (tahdhib)؛ مقطعة النياط الأرنب؛ قطع الفرس الخيل تقطيعا خلفها ومضى؛ جاءت الخيل مقطوطعات أي سراعا (maqayis)
- **B018** benzersiz olmak [kalıp] — belirli nitelikte eşi benzeri olmayan · kötülükte dizginsiz olan
  منقطع القرين في الكرم والسخاء إذا لم يكن له مثل؛ منقطع العقال في الشر والخبث (ayn)؛ فلان منقطع القرين في سخاء أو غيره (sihah)؛ فلان منقطع القرين إذا لم يكن له مثل في سخاء أو فضل (tahdhib)؛ فلان منقطع القرين في سخاء أو غيره (maqayis)
- **B019** yapıca benzer olmak [kalıp] — birine boy ve yapı bakımından benzeyen · düzgün ve güzel beden yapısı
  القطيع شبه النظير؛ هذا قطيع هذا أي شبهه في خلقه وقده؛ حسن التقطيع أي القد (ayn)؛ فلان قطيع فلان أي شبيهه في قده وخلقه؛ شيء حسن التقطيع إذا كان حسن القد (tahdhib)
- **B020** gücü kesilmek [kalıp] — zayıflık veya ağırlık yüzünden kalkamaz olan · cinsel eyleme güç yetiremeyen veya istemeyen · susturulup cevap veremeyen
  أقطع ضعف عن النكاح؛ قطيع القيام أي منقطع إذا أراد القيام من ثقل أو سمنة وربما من شدة ضعفه (ayn)؛ فلان قطيع القيام إذا وصف بالضعف أو السمن؛ أقطع الرجل إذا انقطعت حجته وبكتوه بالحق فلم يجب (sihah)؛ رجل قطيع القيام إذا كان ضعيفا؛ أقطع الرجل إذا لم يرد النساء؛ أقطع كلام الرجل إذا بكتوه بالحق فلم يقدر على الجواب (tahdhib)؛ جارية قطيع القيام كأنها من سمنها تنقطع عنه (maqayis)
- **B021** iç sancı, nefes sıkışması veya iç kopma — karın veya bağırsakta sancı · soluk daralması ve yüksek nefes · içinde damar veya yağ kopmuş olan
  التقطيع مغس تجده في الأمعاء؛ القطع بهر يأخذ الفرس؛ إن انقطع عرق في بطنه أو مشحمه فهو مقطوع (ayn)؛ أصابه قطع أي بهر؛ التقطيع مغص في البطن (sihah)؛ التقطيع مغص يجده الإنسان في بطنه وأمعائه؛ القطع البهر؛ الفرس أيضا يأخذه القطع؛ إذا انقطع عرق في بطنه أو شحم فهو مقطوع (tahdhib)؛ القطع البهر (maqayis)
- **B022** sözü veya şiiri bölmek [kalıp] — dil çevikliği gitmiş veya az konuşan · belirli ağızda kelime sonunu düşürme · şiiri ölçü parçalarına ayırma · kısa şiir parçaları
  قطيع اللسان إذا ذهبت السلاطة منه؛ القطعة في طيء أن يقول يا أبا الحكا وهو يريد يا أبا الحكم؛ المقطعات من الشعر والأراحيز (ayn)؛ تقطيع الشعر وزنه بأجزاء العروض؛ مقطعات الثياب والشعر قصارها (sihah)؛ امرأة قطيع الكلام إذا لم تكن سليطة؛ تقطيع البيت في بيوت الشعر تجزئته بالأفعال؛ القطعة في طيء كالعنعنة في تميم (tahdhib)
- **B023** yol kesmek [kalıp] — yolcuları durdurup soyan kimseler
  قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق (tahdhib)؛ قطع الطريق يقال على وجهين؛ الثاني يراد به الغصب من المارة والسالكين للطريق؛ يؤدي إلى انقطاع الناس عن الطريق (mufradat)
- **B024** şartlı anlaşmak [kalıp] — bir kimseyle belirli iş veya ödeme üzerinde anlaşmak
  قاطعته على كذا (sihah)؛ قاطعت فلانا على كذا وكذا من الأجر والعمل مقاطعة (tahdhib)

## ل ي ن (root_001393) — identity root of لِّينَةٍ (w4)

- **B001** yumuşak olma, yumuşama, yumuşatma ve yumuşak sayma — pürüzlülüğün karşıtı olan fiziksel yumuşaklık · yumuşadı · yumuşak · yumuşaklık · onu yumuşattı · onu yumuşak saydı
  اللِّين ضد الخشونة (maqayis;sihah;mufradat)؛ يستعمل ذلك في الأجسام (mufradat)؛ لان الشيء يلين لينا وشيء لين (sihah)؛ لينت الشيء وألينته أي صيرته لينا (sihah)؛ استلانه عده لينا (sihah)
- **B002** rahatlık ve bolluk içinde yaşama [kalıp] — rahatlık ve bolluk içinde yaşamak
  هو في ليان من عيش أي نعمة (maqayis)؛ هو في ليان من العيش أي في نعيم وخفض (sihah)
- **B003** insan ilişkilerinde yumuşaklık ve nezaket — insanlara yumuşak davranan kimse · yumuşak ve nazik davranma · birine yumuşak ve nazik davranma · bağlama göre yumuşak huylu kişi · onlara merhametle yumuşak davrandın
  فلان ملينة أي لين الجانب (maqayis)؛ الليان بالكسر الملاينة والملاطفة (sihah)؛ يستعار للخلق وغيره من المعاني فيقال فلان لين (mufradat)
- **B004** yaltaklanma — yaltaklandı
  تليّن تملق (sihah)
- **B005** dirençten sonra gerçeğe boyun eğip onu kabul etme [kalıp] — Tanrı'nın anılmasıyla tenleri ve gönülleri yumuşayıp gerçeğe boyun eğdi
  تلين جلودهم وقلوبهم إلى ذكر الله إشارة إلى إذعانهم للحق وقبولهم له بعد تأبيهم منه وإنكارهم إياه (mufradat)
- **B006** belirli bir türe özgü olmayan yumuşak hurma ağacı — belirli bir türe özgü olmayan yumuşak hurma ağacı
  لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع (mufradat)

## ت ر ك (root_000180) — identity root of تَرَكْتُمُوهَا (w6)

- **B001** bir seyden el cekme — bir seyi birakma ve ondan el cekme · hicbir sey birakmadi
  الترك ودعك الشيء تتركه (ayn;tahdhib)؛ تركت الشيء تركا خليته (sihah)؛ ترك الشيء رفضه قصدا واختيارا أو قهرا واضطرارا (mufradat)؛ الترك التخلية عن الشيء وهو قياس الباب (maqayis)؛ ما أترك أي ما ترك شيئا (sihah)
- **B002** geride iz birakma — arkada iz veya sey birakma
  الترك الإبقاء وتركنا عليه أي أبقينا عليه ذكرا حسنا (tahdhib)؛ ومن الثاني كم تركوا من جنات (mufradat)
- **B003** belirtilen halde bırakma [kalıp] — birini veya seyi belirtilen halde birakmak
  الترك الجعل في بعض الكلام تقول تركت الحبل شديدا أي جعلته (ayn;tahdhib)؛ قد يقال في كل فعل ينتهي به إلى حالة ما تركته كذا أو يجري مجرى جعلته كذا نحو تركت فلانا وحيدا (mufradat)؛ يقال تركت الحبل شديدا أي جعلته شديدا وما أحسب هذا من كلام الخليل (maqayis)
- **B004** bırak buyruğu sözü — birak anlaminda buyruk sozu
  تراك بمعنى اترك وهو اسم لفعل الأمر (sihah)؛ وتراك بمعنى أترك (maqayis)
- **B005** karsilikli cekilme [kalıp] — satisi karsilikli olarak birakmak
  تاركته البيع متاركة (sihah)؛ فاركت صاحبي مثل تاركته فهذا من باب الإبدال (maqayis-ibdal)
- **B006** ölenin ardinda kalani — olen kisinin ardinda kalan mal
  تركة الميت تراثه المتروك (sihah)؛ تركة فلان لما يخلفه بعد موته (mufradat)؛ تركه الميت ما يتركه من تراثه (maqayis)
- **B007** evlenmeden birakilan kadin — evlenmeden birakilan kadin · evlenmeden birakilmis kadinla evlenmek
  التريكة من النساء التي تترك فلا يتزوجها أحد (sihah)؛ ترك الرجل إذا تزوج بالتريكة وهي العانس في بيت أبويها (tahdhib)؛ امرأة تريكة وهي التي تترك فلا تتزوج (tahdhib)
- **B008** birakilmis deve kusu yumurtasi — bozkirda birakilmis deve kusu yumurtasi · deve kusu yumurtasi · yumurtaya benzetilen demir baslik
  الترك ضرب من البيض مستدير شبيه بالتركة والتركية وهي بيض النعام (ayn)؛ التريكة بيضة النعام التي تتركها والتركة البيضة من الحديد والجمع ترك (sihah)؛ الترك البيض للرأس واحدته تركة (tahdhib)؛ التريكة أصله البيض المتروك في مفازته ويسمى بيضة الحديد بها (mufradat)؛ تسمى البيضة بالعراء تريكة وتركه السلاح وهي البيضة محمول على هذا ومشبه به (maqayis)
- **B009** geride kalmis su veya cayir — selden geriye durgun kalan su · insanlarin otlatmadan biraktigi cayirlik
  التريكة ماء يمضي عنه السيل ويتركه ناقعا (ayn)؛ التريكة روضة يغفلها الناس فلا يرعونها (sihah;maqayis)
- **B010** insan toplulugu adi — bir insan toplulugu
  الترك جيل من الناس (ayn)؛ الترك جبل من الناس (sihah)

## ق و م (root_001273) — identity root of قَآئِمَةً (w7)

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

## ء ص ل (root_000038) — identity root of أُصُولِهَا (w9)

- **B001** kök ve dayanak — bir şeyin kökü, dayanağı ve alt bölümü · bu ağaç kök salıp yerleşti · kökünden söküp bütünüyle ortadan kaldırmak · kök salmak veya köklendirmek · hepsi birlikte geldi · şeyi bütünüyle, hiçbir parçasını bırakmadan almak
  أساس الشيء (maqayis)؛ الأصل أسفل كل شيء (ayn;tahdhib)؛ الأصل واحد الأصول واستأصله أي قلعه من أصله (sihah)؛ أصل الشيء قاعدته (mufradat)؛ أخذت الشيء بأصيلته أي كله بأصله (sihah)؛ أخذت الشيء بأصلته إذا لم تدع منه شيئا (tahdhib)
- **B002** köklülük ve sağlam yerleşiklik — soy kökü ve yetişilen çevre · sağlam ve köklü görüşlü · görüşte veya ünde köklülük · köklü ün ve yücelik · toprağına kök salmış, kalıcı hurma · bilinen bir soy kökü olan kişi
  مجد أصيل (maqayis;sihah;mufradat)؛ فلان أصيل الرأي (ayn;tahdhib)؛ النخل بأرضنا أصيل أي لا يفنى ولا يزول (ayn;tahdhib)؛ رجل أصيل له أصل (ayn;tahdhib)
- **B003** ikindi sonrası, gün batımından önceki zaman — ikindi sonrası, gün batımından önceki zaman · geç gündüz zamanının tekil ve çoğul adları · geç gündüz zamanında · geç gündüz zamanına girdik veya o sırada geldik
  الأصيل بعد العشي (maqayis)؛ الأصيل العشي (ayn;tahdhib)؛ الوقت بعد العصر إلى المغرب (sihah)؛ للعشية أصيل وأصيلة فجمع الأصيل أصل وآصال (mufradat)؛ لقيته أصيلالا وأصيلانا ومؤصلا (sihah;tahdhib)
- **B004** iri veya kısa gövdeli diye betimlenen bir yılan türü — iri, kısa ya da yuvarlak gövdeli diye betimlenen bir yılan türü
  الأصلة الحية العظيمة (maqayis)؛ الأصلة حية قصيرة تثب (ayn)؛ الأصلة جنس من الحيات وهي أخبثها (sihah)؛ الأصلة حية مثل رئة الشاة وقيل مثل الرحى (tahdhib)
- **B005** yok oluş — yok oluş, ortadan kalkma
  الأصيل الهلاك (ayn;tahdhib)
- **B006** yapmaya koyulmak — o işi yapmaya başladı, işe koyuldu
  أصل فلان يفعل كذا كقولك علق وطفق (tahdhib)

## ء ذ ن (root_000022) — identity root of فَبِإِذْنِ (w10)

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

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w11)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## خ ز ي (root_000407) — identity root of وَلِيُخْزِىَ (w12)

- **B001** aşağılanıp küçük düşürülme — aşağılanma, küçük düşme ve değersiz görülme · aşağılandı ve değersiz duruma düştü · aşağıladı, küçük düşürdü veya gözden çıkarıp uzaklaştırdı · Konuklarım yüzünden beni küçük düşürmeyin · aşağılanmış ve değersiz görülen kimse
  أخزاه الله أي أبعده ومقته والاسم الخزي (maqayis)؛ خزي أي ذل وهان وأخزاه الله (sihah)؛ الخزي السوء والخزي الهوان وأخزيته أي فضحته (tahdhib)؛ من غيره ضرب من الاستخفاف ومصدره الخزي (mufradat)
- **B002** utançtan içten ezilme — aşırı utanç ve içten ezilme · yaptığından utanıp içten ezildi · ondan utandım · utancından içten ezilen kimse · Cennetteki eşleri davranışlarınız ve eksikleriniz yüzünden utandırmayın · utandırdı ve içten ezilmelerine yol açtı
  خزي الرجل استحيا من قبح فعله خزاية فهو خزيان (maqayis)؛ خزي خزاية أي استحياء فهو خزيان وقوم خزايا وامرأة خزياء (sihah)؛ من الحياء ممدود خزاية وخزيت فلانا إذا استحييت منه ورجل خزيان (tahdhib)؛ من نفسه هو الحياء المفرط ومصدره الخزاية (mufradat)
- **B003** ağır sıkıntı ve kötülüğe düşmek — ağır sıkıntı ve kötülüğe düştü; yıkıma uğradı
  وقع في بلية (sihah)؛ من الهلاك خزي الرجل يخزى خزيا؛ خزي يخزى خزيا إذا وقع في بلية وشر (tahdhib)

## ف س ق (root_001156) — identity root of ٱلْفَٰسِقِينَ (w13)

- **B001** itaatten çıkıp Tanrı'nın buyruğuna karşı gelme ve kötülüğe yönelme — itaatten çıkma, Tanrı'nın buyruğunu bırakma ve kötülüğe yönelme · itaatten çıkıp buyruğa karşı gelmek; kötülük etmek · Tanrı'nın buyruğuna karşı gelmek ve itaatinden çıkmak · itaatten çıkmış, dinsel kuralları bütünüyle ya da kısmen çiğneyen kimse · itaatten çıkma; günah işleme ya da Tanrı'ya ortak koşma · itaatten çıkmış ve kötülüğe yönelmiş adam · sürekli olarak itaatten çıkan ve dinsel kuralları çiğneyen kimse
  الفسق وهو الخروج عن الطاعة (maqayis)؛ الفسق الترك لأمر الله؛ الميل إلى المعصية (ayn;tahdhib)؛ فسق الرجل يفسق فسقا وفسوقا أي فجر؛ فسق عن أمر ربه أي خرج (sihah)؛ الفسوق معناه الخروج؛ الشرك ويكون الإثم (tahdhib)؛ خرج عن حجر الشرع؛ أعم من الكفر (mufradat)
- **B002** taze hurmanın kabuğundan çıkması [kalıp] — taze hurma tanesinin kabuğundan çıkması
  فسقت الرطبة عن قشرها (maqayis;sihah)؛ فسقت الرطبة من قشرها لخروجها منه (tahdhib)؛ فسق الرطب إذا خرج عن قشره (mufradat)
- **B003** küçültmeli bir kötüleme adıyla anılan fare — küçültmeli bir kötüleme adıyla anılan fare
  إن الفأرة فويسقة (maqayis)؛ الفويسقة الفأرة (ayn;sihah)؛ سميت فويسقة لخروجها من جحرها (tahdhib)؛ سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها (mufradat)

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:5, and ## Buluşmalar) =====
## İnin gizli kapısı

İkinci ayetin sonundaki {ar:لِأَوَّلِ ٱلْحَشْرِ, tr:li-evveli'l-haşr, gloss:ilk toplayıp sürmede, source:59:2} ifadesindeki "haşr" kelimesi, ailesinde yeryüzünün küçük in hayvanlarını da adlandırır: {ar:حشرات الأرض دوابها الصغار كاليرابيع والضباب, tr:haşarâtu'l-ard devâbbuhe's-sığâr ke'l-yerâbî' ve'd-dıbâb, gloss:haşarât, arap tavşanı ve keler gibi küçük yer hayvanlarıdır, source:"ح ش ر,B004"}. Buradaki sahnede insanlar yuvalarından çıkarılıp topluca sürülür.

On birinci ayet, bu yuvanın mimarisini münafıklara bağlar: {ar:أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟, tr:e-lem tera ile'llezîne nâfekû, gloss:münafıklık edenleri görmedin mi, source:59:11}. Kelimenin kökünde arap tavşanının yuvası vardır. Hayvan yuvasına bir giriş kazar, bir de yüzeye kadar inceltip kapalı bıraktığı gizli bir çıkış yapar. Avcı girişten gelince başıyla bu ince kabuğu kırıp kaçar: {ar:النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج, tr:en-nâfikâ' mevdı'un yurakkıkuhu'l-yerbû', fe-izâ utiye min kıbeli'l-kâsı'â' darabehâ bi-ra'sihî fe'ntefeka, gloss:nâfikâ, tavşanın incelttiği yerdir; kâsıâ tarafından gelinince başıyla vurur ve dışarı fırlar, source:"ن ف ق,B003"}. Bu aile, aynı tabloyu dine de taşır: {ar:النفاق الدخول في الشرع من باب والخروج عنه من باب, tr:en-nifâk ed-duhûl fi'ş-şer'i min bâb ve'l-hurûc 'anhu min bâb, gloss:nifak, dine bir kapıdan girip öbür kapıdan çıkmaktır, source:"ن ف ق,B004"}. Bu tabloda iki fiil öne çıkar: "gelinmek" ve "çıkmak". Surede de aynı iki fiil işler. Allah Nadîr'e beklenmedik yerden "gelir" ve onları "çıkarır". Münafıklar ise {ar:لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ, tr:le-in uhrictum le-nahrucenne me'akum, gloss:çıkarılırsanız sizinle çıkarız, source:59:11} diye söz verir. On ikinci ayet bunun karşılığını verir: {ar:لَئِنْ أُخْرِجُوا۟ لَا يَخْرُجُونَ مَعَهُمْ, tr:le-in uhricû lâ yahrucûne me'ahum, gloss:çıkarılırlarsa onlarla çıkmazlar, source:59:12}. Gizli kapının sahibi kimseyle birlikte çıkmaz, yalnız kendi deliğinden kaçar. İki kapılı yuva, münafıkların iki yüzlü konuşmasında da görülür: {ar:وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ إِلَىٰ شَيَٰطِينِهِمْ قَالُوٓا۟ إِنَّا مَعَكُمْ, tr:ve izâ lakû'llezîne âmenû kâlû âmennâ ve izâ halev ilâ şeyâtînihim kâlû innâ me'akum, gloss:müminlerle karşılaşınca "inandık" derler, şeytanlarıyla baş başa kalınca "sizinleyiz" derler, source:2:14}. Başka bir yerde Kur'an onların aradığı deliği açıkça söyler: {ar:لَوْ يَجِدُونَ مَلْجَـًٔا أَوْ مَغَٰرَٰتٍ أَوْ مُدَّخَلًا لَّوَلَّوْا۟ إِلَيْهِ وَهُمْ يَجْمَحُونَ, tr:lev yecidûne melce'en ev meğârâtin ev muddehalen le-vellev ileyhi ve hum yecmehûn, gloss:bir sığınak, mağaralar ya da girilecek bir delik bulsalar, dizginsiz koşarak oraya kaçarlardı, source:9:57}. Bu sözden hemen önce onların {ar:قَوْمٌ يَفْرَقُونَ, tr:kavmun yefrakûn, gloss:korkan bir topluluk, source:9:56} oldukları söylenir. Her sesi kendilerine karşı sanmaları da aynı ürkek hayvanın tavrıdır {source:63:4}.

Beşinci ve on dokuzuncu ayetlerdeki "fâsıklar" kelimesi aynı tabloya bir hayvan daha ekler. Fare, yuvasından çıkıp zarar verdiği için bu kökle adlandırılmıştır: {ar:سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها, tr:summiyeti'l-fe'ratu fuveysika ... li-hurûcihâ min beytihâ, gloss:fareye, evinden çıktığı için küçük fâsık denildi, source:"ف س ق,B003"}. Fısk, buna göre bulunması gereken kabuktan ve yerden dışarı çıkmaktır. On dokuzuncu ayet, Allah'ı unutanları {ar:أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ, tr:ulâike humu'l-fâsikûn, gloss:onlar yoldan çıkanların ta kendileridir, source:59:19} diye adlandırırken bu çıkışı ahlaki bir anlamla söyler. On yedinci ayetteki "ebedî kalıcılar" kelimesinin ailesinde ise kör bir yer hayvanı vardır: {ar:الخلد ضرب من الجرذان عمي لم يخلق لها عيون, tr:el-huld darbun mine'l-cirzân 'umy, gloss:huld, gözsüz yaratılmış kör bir sıçan türüdür, source:"خ ل د,B005"}. İkinci ayetteki {ar:يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:yâ uli'l-ebsâr, gloss:ey basiret sahipleri, source:59:2} hitabının karşı ucunda bu körlük durur. Yirmi üçüncü ayetteki "ortak koşmak" fiilinin ailesinde de avın dolandığı tuzak ipi vardır: {ar:الشرك حبالة يرتبك فيها الصيد, tr:eş-şerek hibâle yertebiku fîhe's-sayd, gloss:şerek, avın içinde dolaştığı tuzak ağıdır, source:"ش ر ك,B006"}. Ortak koşan kişi, kurtuluş sandığı bağlara kendini dolar.

Kaynaklar: 59:2 ٱلْحَشْرِ ح ش ر B004; 59:11 نَافَقُوا ن ف ق B003, B004; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B003; 59:17 خَٰلِدَيْنِ خ ل د B005; 59:23 يُشْرِكُونَ ش ر ك B006

## Dağa inen söz

Yirmi birinci ayet bir varsayım kurar: {ar:لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍ لَّرَأَيْتَهُۥ خَٰشِعًا مُّتَصَدِّعًا مِّنْ خَشْيَةِ ٱللَّهِ, tr:lev enzelnâ hâze'l-Kur'âne 'alâ cebelin le-raeytehû hâşi'an mutesaddi'an min haşyeti'llâh, gloss:bu Kur'an'ı bir dağa indirseydik, onu Allah korkusundan baş eğmiş, parça parça olmuş görürdün, source:59:21}. Bu sahnenin her kelimesi yağmur ve kuru toprak alanına da açılır. "İndirmek" fiili yağmurun inişini anlatır: {ar:نزل المطر من السماء نزولا, tr:nezele'l-matar mine's-semâ', gloss:yağmur gökten indi, source:"ن ز ل,B001"}. "Dağ" kelimesinin ailesi kaba ve kuru olanı adlandırır: {ar:شيء جبل غليظ جاف, tr:şey'un cibl ğalîz câff, gloss:kaba ve kuru şey, source:"ج ب ل,B003"}. Kazıcının kazamadığı kayaya varmasını anlatan bir ifade de vardır: {ar:أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه, tr:ecbele'l-hâfir, gloss:kazıcı kazamayacağı kayaya ulaşınca "ecbele" denir, source:"ج ب ل,B005"}. "Hâşi'" kelimesi gözünü yere indirmektir, ama aynı zamanda yağmursuz kalıp kurumuş topraktır: {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşa'at, gloss:toprak kuruyup yağmur almayınca "haşaat" denir, source:"خ ش ع,B002"}. "Korku" (haşyet) kelimesinin bir dalı da kurumuş olandır: {ar:الخشي وهو اليابس, tr:el-haşiyy, gloss:haşiyy kuru olandır, source:"خ ش ي,B004"}. Asıl anlamı ise bilgiden doğan saygılı bir korkudur: {ar:الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم, tr:el-haşye havfun yeşûbuhû ta'zîm, gloss:haşyet, yüceltmeyle karışık ve çoğu zaman bilgiden doğan korkudur, source:"خ ش ي,B001"}. "Parça parça olmuş" kelimesi de daha önce gördüğümüz gibi toprağı yaran filizi anlatır. Böylece dağ, üzerine yağmur inmiş kurak bir toprak gibidir. Önce susuzluktan yere çöker, sonra yarılır. Kur'an bu iki adımı başka bir yerde açıkça gösterir: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşi'aten fe-izâ enzelnâ 'aleyhe'l-mâe'htezzet ve rabet, gloss:toprağı kupkuru görürsün, üzerine suyu indirdiğimizde titreşir ve kabarır, source:41:39}. Ayetin sonundaki {ar:وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ, tr:ve tilke'l-emsâlu nadribuhâ li'n-nâs, gloss:bu misalleri insanlara veriyoruz, source:59:21} ifadesindeki "vermek" fiili de toprağa yağmurla vurmak anlamını taşır: {ar:ضرب الأرض بالمطر, tr:darbu'l-ard bi'l-matar, gloss:toprağa yağmurla vurmak, source:"ض ر ب,B013"}. Misal, bu ailede ibret demektir {source:"م ث ل,B011"}. Ayetin bitişi olan "düşünsünler" ise kalbin bir şey üzerinde gidip gelmesidir {source:"ف ك ر,B001"}.

Bu sahne, surenin geri kalanında ters bir aynayı tutar. Kalelerine güvenenler, dağın bile taşıyamadığı sözün karşısında katı kalmıştır. On üçüncü ayet onların korkusunun yanlış yöne gittiğini söyler. Onların gözünde müminler Allah'tan daha korkutucudur. Dağın "haşyet"i ise doğru yöne gider. Bir başka surede bazı insanlar için {ar:يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةً, tr:yahşevne'n-nâse ke-haşyeti'llâhi ev eşedde haşye, gloss:insanlardan Allah'tan korkar gibi, hatta daha çok korkarlar, source:4:77} denir. Taştan kalplere dair başka bir ayette bazı taşların bu sahneyi zaten yaşadığı söylenir: {ar:وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ, tr:ve inne minhâ le-mâ yeşşakkaku fe-yahrucu minhu'l-mâ', ve inne minhâ le-mâ yahbitu min haşyeti'llâh, gloss:taşlardan kimi yarılır da içinden su çıkar, kimi de Allah korkusundan yuvarlanıp düşer, source:2:74}. Musa'nın gördüğü dağ da tecelliye dayanamaz: {ar:فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ جَعَلَهُۥ دَكًّا, tr:fe-lemmâ tecellâ rabbuhû li'l-cebeli ce'alehû dekkâ, gloss:Rabbi dağa tecelli edince onu darmadağın etti, source:7:143}. Kur'an'ın dağları yürütebileceği varsayımı da aynı kuruluşu taşır {source:13:31}. Dağların taşımaktan çekindiği emanet de bu sahnenin yanında durur {source:33:72}. Beşinci ayetteki hurma adı "lîne"nin kökü de bu katılığın cevabını taşır: {ar:تلين جلودهم وقلوبهم إلى ذكر الله, tr:telînu culûduhum ve kulûbuhum ilâ zikri'llâh, gloss:derileri ve kalpleri Allah'ın zikrine yumuşar, source:"ل ي ن,B005"}. Bu ifade, Kur'an'ın kendi tasvirindeki sözlerle aynıdır {source:39:23}. Müminlerin kalplerinin "haşyet"e erme zamanının gelmediği mi diye sorulur. Hemen yanında, kalpleri katılaşmış olanlar ve ardından ölü toprağın diriltilmesi anılır {source:57:16}. Kur'an dinlendiğinde yere kapananlar da {ar:وَيَزِيدُهُمْ خُشُوعًا, tr:ve yezîduhum huşû'â, gloss:bu onların huşuunu artırır, source:17:109} diye anlatılır.

Kaynaklar: 59:21 أَنزَلْنَا ن ز ل B001; 59:21 جَبَلٍ ج ب ل B003, B005; 59:21 خَٰشِعًا خ ش ع B002; 59:21 مُّتَصَدِّعًا ص د ع B003; 59:21 خَشْيَةِ خ ش ي B001, B004; 59:21 نَضْرِبُهَا ض ر ب B013; 59:21 ٱلْأَمْثَٰلُ م ث ل B011; 59:21 يَتَفَكَّرُونَ ف ك ر B001; 59:5 لِّينَةٍ ل ي ن B005

## Hurmalık

Beşinci ayet, kuşatma sırasında bir hurmalıkta yapılan iki şeyi yan yana koyar: {ar:مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ, tr:mâ kata'tum min lînetin ev teraktumûhâ kâimeten 'alâ usûlihâ fe-bi-izni'llâh, gloss:hurma ağaçlarından neyi kestiyseniz ya da köklerinin üzerinde ayakta bıraktıysanız, Allah'ın izniyle oldu, source:59:5}. "Lîne" hurma ağacının adıdır ve türüne göre ayrılmaz: {ar:لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع, tr:lîne, gloss:lîne, yumuşak bir hurma ağacıdır; bir türe has değildir, source:"ل ي ن,B006"}. "Kesmek" ile "izin" bir ifadede de birleşir: {ar:أقطعته قضبانا أي أذنت له في قطعها, tr:akta'tuhû kudbânen, gloss:ona dal kesmeye izin verdim, source:"ق ط ع,B013"}. Böylece kesme de bırakma da yalnız sahibinin izniyle yapılabilir. "Kökler" kelimesi de hurmanın kalıcılığına bağlanır: {ar:النخل بأرضنا أصيل أي لا يفنى ولا يزول, tr:en-nahl bi-ardınâ asîl, gloss:bizim toprağımızda hurma köklüdür, yani tükenmez ve yok olmaz, source:"ء ص ل,B002"}. Aynı kökün bir dalı kökünden sökmektir {source:"ء ص ل,B001"}. Ayet ise ağacı sökmez, "kökleri üzerinde ayakta" bırakılabileceğini söyler. Kur'an bu farkı başka bir yerde iki ağaçla gösterir: güzel ağacın {ar:أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ, tr:asluhâ sâbitun ve far'uhâ fi's-semâ', gloss:kökü sabit, dalı göktedir, source:14:24} ve {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tu'tî ukulehâ kulle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman meyvesini verir, source:14:25}. Kötü ağaç ise {ar:ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ مَا لَهَا مِن قَرَارٍ, tr:uctussat min fevki'l-ardı mâ lehâ min karâr, gloss:yerin üstünden koparılmıştır, karar kılacak yeri yoktur, source:14:26}. Bu surede de "izin" kelimesi hurma ile birlikte geçer.

Aynı ayetin sonu {ar:وَلِيُخْزِىَ ٱلْفَٰسِقِينَ, tr:ve li-yuhziye'l-fâsikîn, gloss:ve fâsıkları rezil etmek için, source:59:5} der. "Fısk" kelimesi, hurma tablosunda olgun hurmanın kabuğundan sıyrılmasıdır: {ar:فسقت الرطبة عن قشرها, tr:fesekati'r-rutabe 'an kışrihâ, gloss:taze hurma kabuğundan çıktı, source:"ف س ق,B002"}. Ağaçlar köklerinde dururken, fâsıklar kabuklarından dışarı çıkar. Altıncı ayetteki "binek develeri" kelimesinin ailesinde de kökü toprağa ulaşmayan bir hurma filizi vardır: {ar:الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق, tr:er-râkib, gloss:râkib, hurma gövdesinde biten ve toprakta kökü olmayan filizdir, source:"ر ك ب,B007"}. Bu filiz, "kökleri üzerinde ayakta" duran ağacın tersidir. İkinci ayetteki "kalpler" kelimesi de hurmanın yenen özünü adlandırır: {ar:قلب النخلة شحمتها, tr:kalbu'n-nahle şahmetuhâ, gloss:hurmanın kalbi onun özüdür, source:"ق ل ب,B003"}. Bu dalda hurmanın özünü sökmek de anlatılır {source:"ق ل ب,B003"}. Korkunun atıldığı yer böylece ağacın canlı özüne benzer. Yirminci ayetteki "cennet" kelimesinde Araplar hurmalığı da görür: {ar:العرب تسمي النخيل جنة, tr:el-'Arab tusemmi'n-nahîle cenne, gloss:Araplar hurmalığa cennet derler, source:"ج ن ن,B003"}. Yirmi üçüncü ayetteki "Cebbâr" ismi de, ailesinde elin yetişemediği yüksek hurmayı anlatır: {ar:الجبار من النخل الذي قد فات اليد, tr:el-cebbâr mine'n-nahl ellezî kad fâte'l-yed, gloss:cebbâr, eli aşmış uzun hurmadır, source:"ج ب ر,B002"}. Böylece sure kesilen ya da bırakılan hurmalarla başlayıp, el yetişmeyen yüksekliğe ve kalıcı bahçeye varır. Kur'an'da terk edilmiş hurmalıklar ve harap yurtlar yan yana durur. Firavun'un halkı için {ar:كَمْ تَرَكُوا۟ مِن جَنَّٰتٍ وَعُيُونٍ, tr:kem terakû min cennâtin ve 'uyûn, gloss:nice bahçe ve pınar bırakıp gittiler, source:44:25} denir. Ad kavminin cesetleri de {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍ, tr:ke-ennehum a'câzu nahlin hâviye, gloss:içi boş hurma kütükleri gibi, source:69:7} yerde yatar. Yoksula kapıyı kapatmak için sabah erkenden ürünü kesmeye yemin eden bahçe sahipleri de vardır {source:68:17}. Onlar {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme 'aleykum miskîn, gloss:bugün oraya yanınıza hiçbir yoksul girmesin, source:68:24} diye fısıldaşmışlardır. Sonunda bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:biçilmiş gibi oldu, source:68:20}. Bu sahne, yedinci ayetin yoksullara ayırdığı payın tam tersidir. Bahçesi yıkılan öteki adam da {ar:يُقَلِّبُ كَفَّيْهِ, tr:yukallibu keffeyh, gloss:ellerini ovuşturur, source:18:42}.

Kaynaklar: 59:5 لِّينَةٍ ل ي ن B006; 59:5 قَطَعْتُم ق ط ع B013; 59:5 أُصُولِهَا ء ص ل B002, B001; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B002; 59:6 رِكَابٍ ر ك ب B007; 59:2 قُلُوبِهِمُ ق ل ب B003; 59:20 ٱلْجَنَّةِ ج ن ن B003; 59:23 ٱلْجَبَّارُ ج ب ر B002

## Yurttan çıkış, ıssızlaşan yurt, hazırlanan konak

Sure iki topluluğun evinden çıkışını anlatır. Birincisi, ikinci ayetteki çıkarılmadır: {ar:أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ, tr:ahrace'llezîne keferû min ehli'l-kitâbi min diyârihim li-evveli'l-haşr, gloss:kitap ehlinden inkâr edenleri ilk sürgünde yurtlarından çıkaran, source:59:2}. "Haşr" kelimesi burada bir topluluğu yerinden çıkarıp sürmek anlamını taşır: {ar:إخراج الجماعة عن مقرهم وإزعاجهم عنه, tr:ihrâcu'l-cemâ'a 'an makarrihim ve iz'âcuhum 'anh, gloss:topluluğu yurdundan çıkarıp oradan sökmek, source:"ح ش ر,B001"}. Bu ifadede, aynı ayetteki "çıkardı" fiili ile "haşr" kelimesi birleşir. Üçüncü ayetteki "celâ" (sürgün) da insanları evlerinden açık alana çıkarmaktır: {ar:أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها, tr:eclaytu'l-kavme 'an menâzilihim, gloss:topluluğu evlerinden çıkardım, yani onları açığa çıkardım, source:"ج ل و,B004"}. İkincisi, sekizinci ayetteki muhacirlerin çıkışıdır: {ar:ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ, tr:ellezîne uhricû min diyârihim ve emvâlihim, gloss:yurtlarından ve mallarından çıkarılanlar, source:59:8}. Hicret evden eve göçmektir: {ar:هاجر القوم من دار إلى دار تركوا الأولى للثانية, tr:hâcera'l-kavmu min dârin ilâ dâr, gloss:topluluk bir yurttan bir yurda göçtü, ilkini ikincisi için bıraktı, source:"ه ج ر,B002"}. Böylece aynı fiil iki çıkışı da anlatır, ama ikisinin sonu farklıdır. Birinciler, yurtlarını kendi elleriyle yıkıp gider. İkinciler ise kendilerine hazırlanmış bir yurda varır: {ar:وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ, tr:ve'llezîne tebevve'u'd-dâra ve'l-îmâne min kablihim, gloss:onlardan önce o yurdu ve imanı yerleşim yeri edinenler, source:59:9}. "Tebevvu'" fiili bir yeri konak edinmektir: {ar:المباءة منزل القوم في كل موضع وتبوأت منزلا وبوأت للرجل منزلا, tr:el-mebâ'e menzilu'l-kavm, gloss:mebâe, topluluğun konağıdır; konak edindim ve adama konak hazırladım, source:"ب و ء,B001"}. Ayetteki dikkat çekici nokta, imanın da yurt gibi konak edinilmesidir. Kur'an hicret edenlere de böyle bir konak vaat eder: {ar:لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةً, tr:le-nubevvi'ennehum fi'd-dunyâ hasene, gloss:onları dünyada güzel bir yere yerleştireceğiz, source:16:41}. Haksız yere yurtlarından çıkarılanlar için ise {ar:وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ, tr:ve le-yensuranna'llâhu men yensuruh, inna'llâhe le-kaviyyun 'azîz, gloss:Allah kendisine yardım edene mutlaka yardım eder; Allah güçlüdür, azîzdir, source:22:40} denir. Bu ayette, sekizinci ayetteki "yardım ederler" ile birinci ayetteki "Azîz" bir araya gelir. Barınak verip yardım edenler de muhacirlerle birlikte anılır {source:8:72}.

Yolun kendisi de suredeki kelimelerde vardır. Yedinci ayetteki {ar:وَٱبْنِ ٱلسَّبِيلِ, tr:ve'bni's-sebîl, gloss:ve yolda kalmış yolcu, source:59:7} ifadesi, yolculukta yolu kesilmiş kişiyi anlatır: {ar:ابن السبيل المسافر الذي انقطع به, tr:ibnu's-sebîl el-musâfir ellezi'nkutı'a bih, gloss:ibnu's-sebîl, yolu kesilmiş yolcudur, source:"س ب ل,B002"}. Beşinci ayetteki "kesmek" fiili bu yolculuğa iki ifadeyle bağlanır. Biri, bineği ölüp azığı biten yolcudur {source:"ق ط ع,B006"}. Öbürü yolcuları soyan eşkıyadır: {ar:قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق, tr:kuttâ'u't-turuk, gloss:yolcuların önünü kesip yolu onlara kapatan yol kesiciler, source:"ق ط ع,B023"}. İkinci ayetteki "ibret alın" fiili de yoldan geçmektir: {ar:رجل عابر سبيل أي مار, tr:raculun 'âbiru sebîl, gloss:yoldan geçen adam, source:"ع ب ر,B001"}. Uzak yolu anlatan kelimeler de surede vardır: dördüncü ayetteki "ayrılık" kelimesinin ailesinde uzun yolculuk {source:"ش ق ق,B005"}, on altıncı ayetteki "Şeytan" kelimesinin ailesinde de evin uzaklığı vardır: {ar:شطنت الدار شطونا إذا بعدت, tr:şatanati'd-dâr, gloss:yurt uzaklaşınca "şatanat" denir, source:"ش ط ن,B001"}.

Geride kalan yurt ise ıssızlaşır. On birinci ayette münafıklar {ar:وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًا, tr:ve lâ nutî'u fîkum ehaden ebedâ, gloss:sizin hakkınızda hiç kimseye asla boyun eğmeyiz, source:59:11} der. "Ebed" kelimesinin ailesinde, sahipleri gidip yaban hayvanlarına kalan ev vardır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:te'ebbede'l-menzil, gloss:ev ıssızlaştı ve yaban hayvanları ona alıştı, source:"ء ب د,B003"}. "Kimse" kelimesi de evle birlikte geçer: {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"}. Yurt kelimesi de yalnız bu tür olumsuz cümlelerde "kimse" anlamı taşır {source:"د و ر,B008"}. Yani "asla" diye verilen söz, yanında boşalmış bir evin sesini taşır. Yedinci ayetteki "zenginler" kelimesi de bir yerde oturmak anlamı taşır: {ar:غني القوم في دارهم أقاموا ومغانيهم منازلهم, tr:ğaniye'l-kavmu fî dârihim, gloss:topluluk yurdunda oturdu; meğânî onların konaklarıdır, source:"غ ن ي,B004"}. Aynı kökte bir deyim de vardır: {ar:كأن لم يغن بالأمس أي كأن لم يكن, tr:ke-en lem yağne bi'l-ems, gloss:sanki dün orada hiç oturmamış, yani hiç yokmuş gibi, source:"غ ن ي,B004"}. Kur'an bu deyimi yok edilen kavimler için kullanır: {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlar gibi, source:11:68}. Bahçe sahnesinde de aynı ifade vardır {source:10:24}. On yedinci ayetteki "ebedî kalıcılar" kelimesi, ailesinde harabeden geriye kalan ocak taşlarını da anlatır: {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid, gloss:uzun süre durdukları için ocak taşlarına havâlid denir, source:"خ ل د,B001"}. Kalıcılık burada artık yaşanan bir ev değil, yıkıntıda kalan taştır. On dokuzuncu ayetteki "unuttular" fiili de göçenlerin ardında bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sakata min menâzili'l-murtahılîn, gloss:nisy, göçenlerin konaklarından düşen değersiz eşyadır, source:"ن س ي,B003"}. Meryem de aynı kelimeyle {ar:وَكُنتُ نَسْيًا مَّنسِيًّا, tr:ve kuntu nesyen mensiyyâ, gloss:unutulup gitmiş bir şey olsaydım, source:19:23} der. Allah'ı unutanlar, kendilerini de unutturulmuş olarak terk edilmiş bir yurdun döküntüsü gibi bulur. İkinci ayetteki "ev" kelimesi de kabir anlamına gelir {source:"ب ي ت,B007"}. Kur'an boşalmış evleri böyle gösterir: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş evleri, source:27:52}. Az kalsın hiç oturulmamış meskenler de vardır {source:28:58}. Kuşatılmış başka bir topluluğun yurdu da müminlere miras kalmıştır {source:33:27}.

Kaynaklar: 59:2/8 أَخْرَجَ / أُخْرِجُوا خ ر ج B001; 59:2 ٱلْحَشْرِ ح ش ر B001; 59:3 ٱلْجَلَآءَ ج ل و B004; 59:8/9 ٱلْمُهَٰجِرِينَ / هَاجَرَ ه ج ر B002; 59:9 تَبَوَّءُو ب و ء B001; 59:7 ٱبْنِ ٱلسَّبِيلِ س ب ل B002; 59:5 قَطَعْتُم ق ط ع B006, B023; 59:2 فَٱعْتَبِرُوا ع ب ر B001; 59:4 شَآقُّوا ش ق ق B005; 59:16 ٱلشَّيْطَٰنِ ش ط ن B001; 59:11 أَبَدًا ء ب د B003; 59:11 أَحَدًا ء ح د B002; 59:2 دِيَٰرِهِمْ د و ر B008; 59:7 ٱلْأَغْنِيَآءِ غ ن ي B004; 59:17 خَٰلِدَيْنِ خ ل د B001; 59:19 نَسُوا ن س ي B003; 59:2 بُيُوتَهُم ب ي ت B007

## Görmekten geçmeye

İkinci ayet, kuşatma sahnesini bir çağrıyla bitirir: {ar:فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:fa'teberû yâ uli'l-ebsâr, gloss:ibret alın ey basiret sahipleri, source:59:2}. "İ'tibâr" kelimesi bir geçiştir: {ar:الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد, tr:el-i'tibâr ve'l-'ibra, gloss:i'tibâr ve ibret, görülenin bilgisinden görülmeyene ulaştıran durumdur, source:"ع ب ر,B004"}. Rüyayı yorumlayan da dışından içine geçer {source:"ع ب ر,B002"}. Basiret ise kalpte delip geçen bir görmedir {source:"ب ص ر,B002"}. Beşinci ayetteki "kesmek" fiili de nehri geçmek anlamında kullanılır: {ar:قطعت النهر قطوعا عبرته, tr:kata'tu'n-nehra kutû'an, gloss:nehri kat ettim, yani geçtim, source:"ق ط ع,B003"}. Bu ifadede "kesmek" ile "geçmek" birleşir. İbret, gözün gördüğü yıkılmış evlerden, görülmeyen sebebe geçmektir. Kur'an aynı çağrıyı Bedir'deki iki birlik için de yapar: {ar:يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ... إِنَّ فِى ذَٰلِكَ لَعِبْرَةً لِّأُو۟لِى ٱلْأَبْصَٰرِ, tr:yeravnehum misleyhim ra'ye'l-'ayn ... inne fî zâlike le-'ibraten li-uli'l-ebsâr, gloss:onları göz görüşüyle kendilerinin iki katı görüyorlardı; bunda basiret sahipleri için elbette bir ibret vardır, source:3:13}. Gece ile gündüzün dönüşümü için de aynı sözler kullanılır {source:24:44}. Üçüncü ayetteki "sürgün" (celâ) kelimesi gözü de açar: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ el-ismid, gloss:celâ sürmedir, çünkü gözü parlatır, source:"ج ل و,B002"}. Sürgün, ona bakanların gözüne çekilen bir sürme gibidir.

Görmenin karşısında sure tahmini koyar. Kuşatılanlar kalelerinin kendilerini koruyacağını "zannetmiştir" ve gelişi "hesaba katmamışlardır". Zan, kesin olmayan bilgidir {source:"ظ ن ن,B003"}. Bir dalı da içinde su olup olmadığı bilinmeyen kuyudur: {ar:الظنون البئر لا يدرى أفيها ماء أم لا, tr:ez-zenûn el-bi'r, gloss:zenûn, içinde su olup olmadığı bilinmeyen kuyudur, source:"ظ ن ن,B006"}. On dördüncü ayetteki "sanırsın" fiili de zan demektir {source:"ح س ب,B002"}. Altıncı ayetteki "atlar" kelimesinin ailesinde de aynada görülen gölge vardır: {ar:الخيال كل شيء تراه كالظل وخيالك في المرآة, tr:el-hayâl kullu şey'in terâhu ke'z-zıll, gloss:hayâl, gölge gibi gördüğün her şey ve aynadaki görüntündür, source:"خ ي ل,B001"}. Kuşatılanların kaleleri, münafıkların vaatleri ve toplu görünen kalabalık, hepsi bu tür gölgelerdir. Bu yüzden sure iki kez "görmedin mi" ve "görürdün" diye sorar: on birinci ayette münafıklara, yirmi birinci ayette dağa. On sekizinci ayetteki "baksın" fiili de gözle ve basiretle bir şeyi evirip çevirmektir {source:"ن ظ ر,B001"}. Ayetin sonundaki "haberdar" ismi de dışın karşısında içi anlatır: {ar:المخبر خلاف المنظر, tr:el-mahber hılâfu'l-manzar, gloss:iç yüz, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. İnsan kendi görünüşüne bakar, Allah ise iç yüzünü bilir. On üçüncü ve on dördüncü ayetlerdeki "topluluk" kelimesinin ailesinde de, göz bebeği sağlam olduğu halde görmeyen göz vardır: {ar:عين قائمة ذهب بصرها والحدقة صحيحة, tr:'aynun kâime, gloss:göz bebeği sağlam olduğu halde görme gücü gitmiş göz, source:"ق و م,B021"}. Bu iki ayet o topluluğu {ar:قَوْمٌ لَّا يَفْقَهُونَ, tr:kavmun lâ yefkahûn, gloss:anlamayan bir topluluk, source:59:13} ve akıl etmeyen bir topluluk diye anar. Kur'an bu körlüğü açıkça tarif eder: {ar:وَلَهُمْ أَعْيُنٌ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Münafıkların görünüşü de insanı hayran bırakır, ama onlar dayalı kütükler gibidir {source:63:4}. Sekizinci ayetteki fakirlerin durumu ise tersine bir yanılgıdır: bilmeyen kişi onları {ar:يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ, tr:yahsebuhumu'l-câhilu ağniyâ', gloss:bilmeyen onları zengin sanır, source:2:273}. Göz, burada da dışa bakıp içi kaçırır.

Kaynaklar: 59:2 فَٱعْتَبِرُوا ع ب ر B004, B002; 59:2 ٱلْأَبْصَٰرِ ب ص ر B002; 59:5 قَطَعْتُم ق ط ع B003; 59:3 ٱلْجَلَآءَ ج ل و B002; 59:2 ظَنُّوا ظ ن ن B003, B006; 59:14 تَحْسَبُهُمْ ح س ب B002; 59:6 خَيْلٍ خ ي ل B001; 59:18 وَلْتَنظُرْ ن ظ ر B001; 59:18 خَبِيرٌ خ ب ر B001; 59:13/14 قَوْمٌ ق و م B021

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

