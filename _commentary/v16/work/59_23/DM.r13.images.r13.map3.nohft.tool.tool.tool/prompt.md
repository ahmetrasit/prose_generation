Focus: 59:23. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_23/D.r13/context.md =====
# 59:23 — focus

هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | هُوَ |  |  | PRON |
| 2 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 3 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 4 | لَآ | لَا |  | NEG |
| 5 | إِلَٰهَ | إِلَٰه | ء ل ه | N |
| 6 | إِلَّا | إِلَّا |  | EXP |
| 7 | هُوَ |  |  | PRON |
| 8 | ٱلْمَلِكُ | مَلِك | م ل ك | DET;ADJ |
| 9 | ٱلْقُدُّوسُ | قُدُّوس | ق د س | DET;ADJ |
| 10 | ٱلسَّلَٰمُ | سَلَٰم | س ل م | DET;ADJ |
| 11 | ٱلْمُؤْمِنُ | مُؤْمِن | ء م ن | DET;ADJ |
| 12 | ٱلْمُهَيْمِنُ | مُهَيْمِن | ه م ن | DET;ADJ |
| 13 | ٱلْعَزِيزُ | عَزِيز | ع ز ز | DET;ADJ |
| 14 | ٱلْجَبَّارُ | جَبَّار | ج ب ر | DET;ADJ |
| 15 | ٱلْمُتَكَبِّرُ | مُتَكَبِّر | ك ب ر | DET;ADJ |
| 16 | سُبْحَٰنَ | سُبْحَٰن | س ب ح | N |
| 17 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 18 | عَمَّا | عَن;مَا |  | P;SUB |
| 19 | يُشْرِكُونَ | أَشْرَكَ | ش ر ك | V;PRON |


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
- 59:21 لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- 59:22 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- 59:23 ◀ focus هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- 59:24 هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/work/59_23/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w2)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## م ل ك (root_001444) — identity root of ٱلْمَلِكُ (w8)

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

## ق د س (root_001206) — identity root of ٱلْقُدُّوسُ (w9)

- **B001** arınma, arıtma ve eksiklikten uzak sayma — arılık, arınma ve eksiklikten uzak sayma · arıtma ve eksiklikten uzak sayma · arındı, arı duruma geldi · arındırdı, arı duruma getirdi · kendimizi ya da şeyleri senin için arındırırız · seni her türlü eksiklikten uzak diye niteleriz
  يدل على الطهر (maqayis)؛ القدس تنزيه الله وهو القدوس والمقدس والمتقدس (ayn)؛ القدس والقدس الطهر والتقديس التطهير وتقدس أي تطهر (sihah)؛ نقدس لك أي نطهر أنفسنا لك ونقدسه أي نطهره والقدوس الطاهر والقدوس المبارك وأرض مقدسة أي مباركة (tahdhib)؛ التقديس التطهير الإلهي ونقدس لك أي نطهر الأشياء ارتساما لك وقيل نقدسك أي نصفك بالتقديس (mufradat)
- **B002** arınmış veya bereketli sayılan yer [kalıp] — arınmış veya bereketli toprak · arınmışların bulunduğu ölüm sonrası mutluluk yurdu · arınmanın kazanıldığı dinî yol ve kurallar bütünü · günah ve ortak koşma kirinden arındırdığı düşünülen tapınak
  الأرض المقدسة هي المطهرة وحظيرة القدس أي الطهر (maqayis)؛ الأرض المقدسة المطهرة وبيت المقدس والمقدس (sihah)؛ بيت المقدس البيت المطهر وأرض مقدسة أي مباركة (tahdhib)؛ البيت المقدس هو المطهر من النجاسة وكذلك الأرض المقدسة وحظيرة القدس قيل الجنة وقيل الشريعة (mufradat)
- **B003** Tanrı'dan kutsallıkla inen belirli vahiy meleği [kalıp] — Tanrı'dan kutsallıkla inen belirli vahiy meleği
  جبرئيل عليه السلام روح القدس (maqayis)؛ روح القدس جبريل عليه السلام (sihah)؛ روح القدس يعني به جبريل من حيث إنه ينزل بالقدس من الله (mufradat)
- **B004** Tanrı'nın mutlak arılığını ve eksiksizliğini bildiren adı — Tanrı'nın mutlak arılığını ve eksiksizliğini bildiren adı · Tanrı'yı arı ve eksiklikten uzak diye niteleyen, kullanımı tartışmalı söz · Tanrı'yı arı ve eksiklikten uzak diye niteleyen, kaynakta kabulü tartışmalı söz
  في صفة الله تعالى القدوس وهو منزه عن الأضداد والأنداد والصاحبة والولد (maqayis)؛ القدس تنزيه الله وهو القدوس والمقدس والمتقدس (ayn)؛ القدوس اسم من أسماء الله تعالى وهو فعول من القدس وهو الطهارة (sihah)؛ القدوس الطاهر وهو من أسماء الله ولم يجىء في صفة الله غير القدوس ولا أعرف المتقدس في صفاته (tahdhib)
- **B005** yıkanıp arınmak için kullanılan kova — yıkanıp arınmak için kullanılan kova
  القدس بالتحريك السطل بلغة أهل الحجاز لأنه يتطهر فيه (sihah)؛ قيل للسطل القدس لأنه يتقدس منه أي يتطهر (tahdhib)
- **B006** gümüşten yapılmış boncuk benzeri süs — gümüşten yapılmış boncuk veya boncuk benzeri süs
  القداس شيء كالجمان يعمل من فضة (maqayis)؛ القداس الجمان من فضة (ayn)؛ القداس بالضم شئ يعمل كالجمان من فضة (sihah)؛ القداس الجمان من فضة (tahdhib)
- **B007** kutsallık dilenen hac konaklama yerinin özel adı — kutsallık dilenen ve hac yolcularına konak sayılan yerin özel adı
  القادسية سميت بذلك وإن إبراهيم دعا لها بالقدس وأن تكون محلة الحاج (maqayis)؛ القادسية دعا لها إبراهيم عليه السلام بالقدس وأن تكون محلة الحاج (sihah)
- **B008** belirli büyük bir dağın özel adı — belirli büyük bir dağın özel adı
  قدس جبل (maqayis)؛ قدس بالتسكين جبل عظيم بأرض نجد (sihah)
- **B009** büyük gemi — büyük gemiler · büyük gemi
  القوادس السفن الكبار والقادس السفينة العظيمة (tahdhib)
- **B010** develerin suya doyduğunu gösteren havuz taşı — suyun örttüğünde develerin doyduğu anlaşılan havuz taşı
  القداس الحجر ينصب على مصب الماء في الحوض وحجر يكون في وسط الحوض إذا غمره الماء رويت الإبل (tahdhib)
- **B011** arınmış tapınağın bulunduğu yere mensup kimse — arınmış tapınağın bulunduğu yere mensup; tanıkta Yahudi
  بيت المقدس والمقدس والنسبة إليه مقدسي مثال مجلسي ومقدسي ويعنى يهوديا (sihah)
- **B012** bereket umulan Hristiyan rahip — bereket umularak giysisine dokunulan Hristiyan rahip
  أراد بالمقدس الراهب وصبيان النصارى يتبركون به ويمسحون ثيابه (tahdhib)

## س ل م (root_000737) — identity root of ٱلسَّلَٰمُ (w10)

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

## ء م ن (root_000054) — identity root of ٱلْمُؤْمِنُ (w11)

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ه م ن (root_001603) — identity root of ٱلْمُهَيْمِنُ (w12)

- **B001** tanıklık eden, gözeten ve güven sağlayan sorumlu koruyucu — 
  المهيمن الشاهد (sihah)؛ من آمن غيره من الخوف (sihah)؛ وشاهدا عليه (tahdhib)؛ رقيبا عليه (tahdhib)؛ مؤتمنا عليه (tahdhib)؛ القائم على خلقه (tahdhib)
- **B002** bele bağlanan kuşak, giysi bağı veya para kesesi — bele bağlanan giysi bağı veya kuşak · içine harcanacak para konup bele bağlanan kese
  الهميان التكة؛ قيل للمنطقة هميان؛ الذي تجعل فيه النفقة ويشد على الوسط هميان؛ الهميان دخيل معرب؛ يشدوا همايينها على أحقائها
- **B003** başkasının duasına kabul dileğiyle sözlü onay vermek — 
  إني داع فهيمنوا؛ أراد إني داع فأمنوا على دعائي؛ قلب إحدى حرفي التشديدة في أمنوا ياء؛ ثم قلبت الهمزة هاء

## ع ز ز (root_001008) — identity root of ٱلْعَزِيزُ (w13)

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

## ج ب ر (root_000216) — identity root of ٱلْجَبَّارُ (w14)

- **B001** kırığı onarma veya eksikliği giderip yeniden bütünleme — kırık kemiği onarıp kaynatmak · kemiğin kaynaması veya kırığın iyileşmesi · yoksulun ihtiyacını giderip onu yeterli duruma getirmek · inanç düzenini düzeltip tamamlamak · yenmiş veya kurumuş bitkinin yeniden sürmesi · ihtiyacı giderdiği için ekmeğe verilen ad · hesapta eksikliği gidermek için bir nicelik ekleme işlemi · kırık kemikleri onarıp kaynatan kişi
  جبرت العظم فجبر (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ جبرت فاقة الرجل إذا أغنيته (ayn;sihah;tahdhib)؛ قد جبر الدين الإله فجبر (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ تجبر النبت بعد الأكل (sihah;tahdhib;mufradat)؛ الخبز جابر بن حبة (sihah;tahdhib;mufradat)
- **B002** erişilemeyecek ölçüde yükselme ve kendini büyük görme — el erişmeyecek kadar uzun, iri ve güçlü · kendini büyük gören, kibirli ve öğüt kabul etmeyen · kibir, büyüklük taslama ve kendini üstün görme · Tanrı için: erişilemez yücelikte olan veya yaratılanlara dilediğini yaptıran
  الجبار الذي طال وفات اليد (maqayis)؛ الجبار من النخل الذي قد بلغ غاية الطول (ayn)؛ الجبار من النخل الذي قد فات اليد (jamhara;sihah;tahdhib;mufradat)؛ رجل جبار طويل عظيم قوي (tahdhib)؛ الجبار من الناس العظيم في نفسه (ayn)؛ فيه جبرية وجبروة وجبروت وجبورة (maqayis;ayn;sihah;tahdhib)؛ قلب جبار ذو كبر (ayn;tahdhib;mufradat)
- **B003** birini istemediği bir şeye zorla yöneltme — Tanrı için: erişilemez yücelikte olan veya yaratılanlara dilediğini yaptıran · birini istemediği işe zorlamak · zorla egemen olan veya haksız yere öldüren kişi · insan eylemlerini zorunlu sayıp özgür seçimi reddeden öğreti
  أجبرت فلانا على الأمر (maqayis;sihah;tahdhib;mufradat)؛ الجبر أن تجبر إنسانا على ما لا يريد (ayn)؛ أجبرت الرجل إذا أكرهته عليه (jamhara)؛ الجبار القاهر المسلط (tahdhib;mufradat)؛ الجبار القتال في غير حق (tahdhib)؛ الجبر خلاف القدر والجبرية (sihah;tahdhib;mufradat)
- **B004** tazmin sorumluluğu doğurmayan zarar — bedeli ödenmeyen ve kimseye yüklenmeyen zarar · hayvan, kuyu veya maden kaynaklı olup tazmin edilmeyen zarar
  الجبار وهو الهدر (maqayis;sihah;tahdhib)؛ العجماء جبار أي ما أصاب الدابة فهو هدر (ayn;sihah;tahdhib)؛ الجبار الذي لا أرش له (jamhara)؛ الجبار لما يسقط من الأرش (mufradat)؛ البئر جبار والمعدن جبار (maqayis;sihah;tahdhib)
- **B005** kırığı sabitleyen atel ve ona benzeyen kol takısı — kırığı sabitlemek için bağlanan tahta, çubuk veya bez · atele biçimce benzeyen bilezik veya kol halkası · kırık kemikleri onarıp kaynatan kişi
  الخشب الذي يضم به العظم الكسير جبارة والجمع جبائر (maqayis)؛ الجبارة الخشبة توضع على الكسر (ayn)؛ الجبارة واحدة الجبائر وهو الخشب الذي يشد على العضو المكسور (jamhara)؛ العيدان التي تجبر بها العظام (sihah)؛ الخشبات التي توضع على موضع الكسر (tahdhib)؛ الجبيرة للخرقة والجبارة للخشبة (mufradat)؛ الجبارة دملوج المرأة من الحلي (ayn;jamhara;sihah;tahdhib;mufradat)
- **B006** biçime bağlı adlandırmalar — eski kullanımda salı gününe verilen ad · aynı söz ailesinden türetilmiş kişi adları · kaynağa göre hükümdar, adam veya yiğit kişi · farklı söylenişleri bulunan bir melek adı ve öğelerine ilişkin açıklama
  الجبار اسم يوم الثلاثاء (ayn;jamhara;sihah;tahdhib)؛ سمت العرب جبرا وجبيرا وجابرا (jamhara)؛ جبرائيل اسم وفيه لغات (sihah)؛ جبر هو الرجل وإيل الربوبية (tahdhib)؛ الجبر الملك (jamhara;tahdhib)

## ك ب ر (root_001281) — identity root of ٱلْمُتَكَبِّرُ (w15)

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

## س ب ح (root_000666) — identity root of سُبْحَٰنَ (w16)

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

## ش ر ك (root_000791) — identity root of يُشْرِكُونَ (w19)

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

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:23, and ## Buluşmalar) =====
## İnin gizli kapısı

İkinci ayetin sonundaki {ar:لِأَوَّلِ ٱلْحَشْرِ, tr:li-evveli'l-haşr, gloss:ilk toplayıp sürmede, source:59:2} ifadesindeki "haşr" kelimesi, ailesinde yeryüzünün küçük in hayvanlarını da adlandırır: {ar:حشرات الأرض دوابها الصغار كاليرابيع والضباب, tr:haşarâtu'l-ard devâbbuhe's-sığâr ke'l-yerâbî' ve'd-dıbâb, gloss:haşarât, arap tavşanı ve keler gibi küçük yer hayvanlarıdır, source:"ح ش ر,B004"}. Buradaki sahnede insanlar yuvalarından çıkarılıp topluca sürülür.

On birinci ayet, bu yuvanın mimarisini münafıklara bağlar: {ar:أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟, tr:e-lem tera ile'llezîne nâfekû, gloss:münafıklık edenleri görmedin mi, source:59:11}. Kelimenin kökünde arap tavşanının yuvası vardır. Hayvan yuvasına bir giriş kazar, bir de yüzeye kadar inceltip kapalı bıraktığı gizli bir çıkış yapar. Avcı girişten gelince başıyla bu ince kabuğu kırıp kaçar: {ar:النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج, tr:en-nâfikâ' mevdı'un yurakkıkuhu'l-yerbû', fe-izâ utiye min kıbeli'l-kâsı'â' darabehâ bi-ra'sihî fe'ntefeka, gloss:nâfikâ, tavşanın incelttiği yerdir; kâsıâ tarafından gelinince başıyla vurur ve dışarı fırlar, source:"ن ف ق,B003"}. Bu aile, aynı tabloyu dine de taşır: {ar:النفاق الدخول في الشرع من باب والخروج عنه من باب, tr:en-nifâk ed-duhûl fi'ş-şer'i min bâb ve'l-hurûc 'anhu min bâb, gloss:nifak, dine bir kapıdan girip öbür kapıdan çıkmaktır, source:"ن ف ق,B004"}. Bu tabloda iki fiil öne çıkar: "gelinmek" ve "çıkmak". Surede de aynı iki fiil işler. Allah Nadîr'e beklenmedik yerden "gelir" ve onları "çıkarır". Münafıklar ise {ar:لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ, tr:le-in uhrictum le-nahrucenne me'akum, gloss:çıkarılırsanız sizinle çıkarız, source:59:11} diye söz verir. On ikinci ayet bunun karşılığını verir: {ar:لَئِنْ أُخْرِجُوا۟ لَا يَخْرُجُونَ مَعَهُمْ, tr:le-in uhricû lâ yahrucûne me'ahum, gloss:çıkarılırlarsa onlarla çıkmazlar, source:59:12}. Gizli kapının sahibi kimseyle birlikte çıkmaz, yalnız kendi deliğinden kaçar. İki kapılı yuva, münafıkların iki yüzlü konuşmasında da görülür: {ar:وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ إِلَىٰ شَيَٰطِينِهِمْ قَالُوٓا۟ إِنَّا مَعَكُمْ, tr:ve izâ lakû'llezîne âmenû kâlû âmennâ ve izâ halev ilâ şeyâtînihim kâlû innâ me'akum, gloss:müminlerle karşılaşınca "inandık" derler, şeytanlarıyla baş başa kalınca "sizinleyiz" derler, source:2:14}. Başka bir yerde Kur'an onların aradığı deliği açıkça söyler: {ar:لَوْ يَجِدُونَ مَلْجَـًٔا أَوْ مَغَٰرَٰتٍ أَوْ مُدَّخَلًا لَّوَلَّوْا۟ إِلَيْهِ وَهُمْ يَجْمَحُونَ, tr:lev yecidûne melce'en ev meğârâtin ev muddehalen le-vellev ileyhi ve hum yecmehûn, gloss:bir sığınak, mağaralar ya da girilecek bir delik bulsalar, dizginsiz koşarak oraya kaçarlardı, source:9:57}. Bu sözden hemen önce onların {ar:قَوْمٌ يَفْرَقُونَ, tr:kavmun yefrakûn, gloss:korkan bir topluluk, source:9:56} oldukları söylenir. Her sesi kendilerine karşı sanmaları da aynı ürkek hayvanın tavrıdır {source:63:4}.

Beşinci ve on dokuzuncu ayetlerdeki "fâsıklar" kelimesi aynı tabloya bir hayvan daha ekler. Fare, yuvasından çıkıp zarar verdiği için bu kökle adlandırılmıştır: {ar:سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها, tr:summiyeti'l-fe'ratu fuveysika ... li-hurûcihâ min beytihâ, gloss:fareye, evinden çıktığı için küçük fâsık denildi, source:"ف س ق,B003"}. Fısk, buna göre bulunması gereken kabuktan ve yerden dışarı çıkmaktır. On dokuzuncu ayet, Allah'ı unutanları {ar:أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ, tr:ulâike humu'l-fâsikûn, gloss:onlar yoldan çıkanların ta kendileridir, source:59:19} diye adlandırırken bu çıkışı ahlaki bir anlamla söyler. On yedinci ayetteki "ebedî kalıcılar" kelimesinin ailesinde ise kör bir yer hayvanı vardır: {ar:الخلد ضرب من الجرذان عمي لم يخلق لها عيون, tr:el-huld darbun mine'l-cirzân 'umy, gloss:huld, gözsüz yaratılmış kör bir sıçan türüdür, source:"خ ل د,B005"}. İkinci ayetteki {ar:يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ, tr:yâ uli'l-ebsâr, gloss:ey basiret sahipleri, source:59:2} hitabının karşı ucunda bu körlük durur. Yirmi üçüncü ayetteki "ortak koşmak" fiilinin ailesinde de avın dolandığı tuzak ipi vardır: {ar:الشرك حبالة يرتبك فيها الصيد, tr:eş-şerek hibâle yertebiku fîhe's-sayd, gloss:şerek, avın içinde dolaştığı tuzak ağıdır, source:"ش ر ك,B006"}. Ortak koşan kişi, kurtuluş sandığı bağlara kendini dolar.

Kaynaklar: 59:2 ٱلْحَشْرِ ح ش ر B004; 59:11 نَافَقُوا ن ف ق B003, B004; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B003; 59:17 خَٰلِدَيْنِ خ ل د B005; 59:23 يُشْرِكُونَ ش ر ك B006

## Hurmalık

Beşinci ayet, kuşatma sırasında bir hurmalıkta yapılan iki şeyi yan yana koyar: {ar:مَا قَطَعْتُم مِّن لِّينَةٍ أَوْ تَرَكْتُمُوهَا قَآئِمَةً عَلَىٰٓ أُصُولِهَا فَبِإِذْنِ ٱللَّهِ, tr:mâ kata'tum min lînetin ev teraktumûhâ kâimeten 'alâ usûlihâ fe-bi-izni'llâh, gloss:hurma ağaçlarından neyi kestiyseniz ya da köklerinin üzerinde ayakta bıraktıysanız, Allah'ın izniyle oldu, source:59:5}. "Lîne" hurma ağacının adıdır ve türüne göre ayrılmaz: {ar:لينة أي من نخلة ناعمة؛ لا يختص بنوع منه دون نوع, tr:lîne, gloss:lîne, yumuşak bir hurma ağacıdır; bir türe has değildir, source:"ل ي ن,B006"}. "Kesmek" ile "izin" bir ifadede de birleşir: {ar:أقطعته قضبانا أي أذنت له في قطعها, tr:akta'tuhû kudbânen, gloss:ona dal kesmeye izin verdim, source:"ق ط ع,B013"}. Böylece kesme de bırakma da yalnız sahibinin izniyle yapılabilir. "Kökler" kelimesi de hurmanın kalıcılığına bağlanır: {ar:النخل بأرضنا أصيل أي لا يفنى ولا يزول, tr:en-nahl bi-ardınâ asîl, gloss:bizim toprağımızda hurma köklüdür, yani tükenmez ve yok olmaz, source:"ء ص ل,B002"}. Aynı kökün bir dalı kökünden sökmektir {source:"ء ص ل,B001"}. Ayet ise ağacı sökmez, "kökleri üzerinde ayakta" bırakılabileceğini söyler. Kur'an bu farkı başka bir yerde iki ağaçla gösterir: güzel ağacın {ar:أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِى ٱلسَّمَآءِ, tr:asluhâ sâbitun ve far'uhâ fi's-semâ', gloss:kökü sabit, dalı göktedir, source:14:24} ve {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tu'tî ukulehâ kulle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman meyvesini verir, source:14:25}. Kötü ağaç ise {ar:ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ مَا لَهَا مِن قَرَارٍ, tr:uctussat min fevki'l-ardı mâ lehâ min karâr, gloss:yerin üstünden koparılmıştır, karar kılacak yeri yoktur, source:14:26}. Bu surede de "izin" kelimesi hurma ile birlikte geçer.

Aynı ayetin sonu {ar:وَلِيُخْزِىَ ٱلْفَٰسِقِينَ, tr:ve li-yuhziye'l-fâsikîn, gloss:ve fâsıkları rezil etmek için, source:59:5} der. "Fısk" kelimesi, hurma tablosunda olgun hurmanın kabuğundan sıyrılmasıdır: {ar:فسقت الرطبة عن قشرها, tr:fesekati'r-rutabe 'an kışrihâ, gloss:taze hurma kabuğundan çıktı, source:"ف س ق,B002"}. Ağaçlar köklerinde dururken, fâsıklar kabuklarından dışarı çıkar. Altıncı ayetteki "binek develeri" kelimesinin ailesinde de kökü toprağa ulaşmayan bir hurma filizi vardır: {ar:الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق, tr:er-râkib, gloss:râkib, hurma gövdesinde biten ve toprakta kökü olmayan filizdir, source:"ر ك ب,B007"}. Bu filiz, "kökleri üzerinde ayakta" duran ağacın tersidir. İkinci ayetteki "kalpler" kelimesi de hurmanın yenen özünü adlandırır: {ar:قلب النخلة شحمتها, tr:kalbu'n-nahle şahmetuhâ, gloss:hurmanın kalbi onun özüdür, source:"ق ل ب,B003"}. Bu dalda hurmanın özünü sökmek de anlatılır {source:"ق ل ب,B003"}. Korkunun atıldığı yer böylece ağacın canlı özüne benzer. Yirminci ayetteki "cennet" kelimesinde Araplar hurmalığı da görür: {ar:العرب تسمي النخيل جنة, tr:el-'Arab tusemmi'n-nahîle cenne, gloss:Araplar hurmalığa cennet derler, source:"ج ن ن,B003"}. Yirmi üçüncü ayetteki "Cebbâr" ismi de, ailesinde elin yetişemediği yüksek hurmayı anlatır: {ar:الجبار من النخل الذي قد فات اليد, tr:el-cebbâr mine'n-nahl ellezî kad fâte'l-yed, gloss:cebbâr, eli aşmış uzun hurmadır, source:"ج ب ر,B002"}. Böylece sure kesilen ya da bırakılan hurmalarla başlayıp, el yetişmeyen yüksekliğe ve kalıcı bahçeye varır. Kur'an'da terk edilmiş hurmalıklar ve harap yurtlar yan yana durur. Firavun'un halkı için {ar:كَمْ تَرَكُوا۟ مِن جَنَّٰتٍ وَعُيُونٍ, tr:kem terakû min cennâtin ve 'uyûn, gloss:nice bahçe ve pınar bırakıp gittiler, source:44:25} denir. Ad kavminin cesetleri de {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍ, tr:ke-ennehum a'câzu nahlin hâviye, gloss:içi boş hurma kütükleri gibi, source:69:7} yerde yatar. Yoksula kapıyı kapatmak için sabah erkenden ürünü kesmeye yemin eden bahçe sahipleri de vardır {source:68:17}. Onlar {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme 'aleykum miskîn, gloss:bugün oraya yanınıza hiçbir yoksul girmesin, source:68:24} diye fısıldaşmışlardır. Sonunda bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:biçilmiş gibi oldu, source:68:20}. Bu sahne, yedinci ayetin yoksullara ayırdığı payın tam tersidir. Bahçesi yıkılan öteki adam da {ar:يُقَلِّبُ كَفَّيْهِ, tr:yukallibu keffeyh, gloss:ellerini ovuşturur, source:18:42}.

Kaynaklar: 59:5 لِّينَةٍ ل ي ن B006; 59:5 قَطَعْتُم ق ط ع B013; 59:5 أُصُولِهَا ء ص ل B002, B001; 59:5/19 ٱلْفَٰسِقِينَ ف س ق B002; 59:6 رِكَابٍ ر ك ب B007; 59:2 قُلُوبِهِمُ ق ل ب B003; 59:20 ٱلْجَنَّةِ ج ن ن B003; 59:23 ٱلْجَبَّارُ ج ب ر B002

## Kırık bel ve onu saran el

Sekizinci ayetteki "fakirler" kelimesi, kökünde beli kırılmış insanı anlatır: {ar:أصل الفقير المكسور الفقار, tr:aslu'l-fakîr el-meksûru'l-fakâr, gloss:fakîrin aslı, omurları kırılmış olandır, source:"ف ق ر,B001"}. Belin kemiklerini kıran felakete de bu adla denir {source:"ف ق ر,B008"}. Muhacirler yurtlarından ve mallarından çıkarılmıştır. Onların fakirliği, beli kırılmış bir insanın ayakta duramamasına benzer. Yirmi üçüncü ayetteki "Cebbâr" ismi bu kırığın karşısına konur: {ar:جبرت العظم فجبر, tr:cebertu'l-'azme fe-cebera, gloss:kemiği sardım, o da kaynadı, source:"ج ب ر,B001"}. Aynı fiil yoksulluğu gidermek için de kullanılır: {ar:جبرت فاقة الرجل إذا أغنيته, tr:cebertu fâkate'r-racul, gloss:adamın yokluğunu giderdim, yani onu zengin ettim, source:"ج ب ر,B001"}. Kırık kemiğe sarılan tahta da bu köktendir {source:"ج ب ر,B005"}. Bu ifadeler, sekizinci ayetin "fakirler"i, yedinci ayetin "zenginler"i ve yirmi üçüncü ayetin "Cebbâr" ismini birbirine bağlar. Fey' malının yoksullara ayrılması, kırık belin sarılmasıdır. Bu ismin anlamı da yalnız ezen bir güç değil, kırığı saran bir güçtür. Kur'an da {ar:وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ, tr:va'llâhu'l-ğaniyyu ve entumu'l-fukarâ', gloss:Allah zengindir, siz ise fakirsiniz, source:47:38} der. Aynı ayet cimrilik edenin ancak kendine cimrilik ettiğini de söyler {source:47:38}. Yirmi dördüncü ayetteki "Bâri'" ismi ile on altıncı ayetteki "uzağım" kelimesi aynı köktendir. Kökün bir dalı hastalıktan kurtulmaktır: {ar:البرء السلامة من السقم, tr:el-bur' es-selâme mine's-sekam, gloss:bur', hastalıktan kurtulup sağlığa kavuşmaktır, source:"ب ر ء,B003"}. Şeytan "ben senden uzağım" der ve kendini kurtarmaya çalışır. Sağlık ve kurtuluş ise yaratan Bâri' isminde kalır. Yirmi üçüncü ayetteki "Selâm" ismi de sağlığın kendisidir: {ar:السلامة أن يسلم الإنسان من العاهة والأذى, tr:es-selâme, gloss:selâmet, insanın sakatlıktan ve eziyetten kurtulmasıdır, source:"س ل م,B001"}.

Kaynaklar: 59:8 لِلْفُقَرَآءِ ف ق ر B001, B008; 59:23 ٱلْجَبَّارُ ج ب ر B001, B005; 59:16/24 بَرِىٓءٌ / ٱلْبَارِئُ ب ر ء B003; 59:23 ٱلسَّلَٰمُ س ل م B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

