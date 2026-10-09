Focus: 59:18. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_18/D.r13/context.md =====
# 59:18 — focus

يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَٰٓأَيُّهَا | أَيُّهَا |  | VOC;N |
| 2 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 3 | ءَامَنُوا۟ | ءَامَنَ | ء م ن | V;PRON |
| 4 | ٱتَّقُوا۟ | ٱتَّقَىٰ | و ق ي | V;PRON |
| 5 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 6 | وَلْتَنظُرْ | نَّظَرَ | ن ظ ر | REM;IMPV;V |
| 7 | نَفْسٌ | نَفْس | ن ف س | N |
| 8 | مَّا | مَا |  | REL |
| 9 | قَدَّمَتْ | قَدَّمَ | ق د م | V |
| 10 | لِغَدٍ | غَد | غ د و | P;N |
| 11 | وَٱتَّقُوا۟ | ٱتَّقَىٰ | و ق ي | CONJ;V;PRON |
| 12 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 13 | إِنَّ | إِنّ |  | ACC |
| 14 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 15 | خَبِيرٌۢ | خَبِير | خ ب ر | N |
| 16 | بِمَا | مَا |  | P;REL |
| 17 | تَعْمَلُونَ | عَمِلَ | ع م ل | V;PRON |


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
- 59:18 ◀ focus يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- 59:19 وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- 59:20 لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- 59:21 لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- 59:22 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- 59:23 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- 59:24 هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/work/59_18/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء م ن (root_000054) — identity root of ءَامَنُوا۟ (w3)

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## و ق ي (root_001677) — identity root of ٱتَّقُوا۟ (w4)

- **B001** araya engel koyarak zarardan koruma — bir şeyi koruyucu bir engelle zarardan saklamak · koruma; zararı önleyen araç veya engel · bir şeyi korumaya yarayan araç ya da engel · zarardan koruyan şey · zararı savan koruyucu · kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez · koruyucu şeyler
  دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)
- **B002** korkulan şeyden ya da yanlış davranıştan kendini koruma — kendini korkulan ya da zarar verecek şeyden korumak · bir şeyi kendine koruyucu yapmak · Tanrı'ya karşı gelmekten sakınmak · kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması · sakınma ve kendini koruma · sakınan ve kendini yanlış davranıştan koruyan kimse · sakınma; kendini kötülükten koruma · sakınıp kendini koruma · kendini yanlış davranışlardan koruyan kimse · sakınan ve kendini yanlış davranıştan koruyan kimse
  اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)
- **B003** hafif topallama ve toynak ağrısıyla yürümekten çekinme — hafif topallama · topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at · hayvanın sırtında yara açmayan eyer · aksayışını gözet ve ağırdan al
  الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)
- **B004** kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü — kırk gümüş para ağırlığına eşit bilinen ölçü · yağ için yedi temel ağırlık birimine eşit ölçü · bu ağırlık ölçüsü adının çoğul biçimleri
  الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)
- **B005** örümcek kuşu — örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri
  الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهَ (w5)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ن ظ ر (root_001520) — identity root of وَلْتَنظُرْ (w6)

- **B001** bakıp inceleme — bakma ve inceleme · bir şeye bakıp onu görmek · bir konuyu düşünüp incelemek · bakanlar veya seyredenler
  تأمل الشيء ومعاينته؛ نظرت إلى الشيء إذا عاينته (maqayis)؛ النظر تأمل الشئ بالعين (sihah)؛ نظر العين ونظر القلب؛ نظرت في الأمر احتمل أن يكون تفكرا وتدبرا بالقلب (tahdhib)؛ تقليب البصر والبصيرة لإدراك الشيء ورؤيته؛ التأمل والفحص؛ المعرفة الحاصلة بعد الفحص؛ مشاهدون؛ تعتبرون (mufradat)
- **B002** bekleme veya süre tanıma — onu beklemek · bekleme · durup beklemek · ona süre verip ertelemek · ondan ek süre istemek · bekleyip geleceğini gözetmek · erteleme ve geciktirme · süre verme ve erteleme · bekle · önce Tanrı'dan, sonra senden iyilik umarım · kendisinden iyilik umulan
  نظرته أي انتظرته؛ ينظر إلى الوقت الذي يأتي فيه (maqayis)؛ النظر الانتظار؛ النظرة التأخير؛ أنظرته أي أخرته؛ استنظره أي استمهله (sihah)؛ إنما أنظر إلى الله ثم إليك أي أتوقع فضل الله ثم فضلك؛ أنظرني أي انتظرني قليلا؛ أمهلته؛ النظرة إنظار (tahdhib)؛ النظر الانتظار؛ نظرته وانتظرته وأنظرته أي أخرته (mufradat)
- **B003** görüş doğrultusunda karşı karşıya olma [kalıp] — birbirini görebilen komşu topluluk · evim onun evine bakar ve karşısındadır · dağ yol üzerinde karşına çıktı
  حي حلال نظر متجاورون ينظر بعضهم إلى بعض (maqayis)؛ حي حلال ونظر أي متجاورون يرى بعضهم بعضا؛ داري تنظر إلى دار فلان؛ دورنا تناظر أي تقابل؛ فنظر إليك الجبل (sihah)؛ داري تنظر إلى دار فلان ودورنا تناظر إذا كانت متحاذية (tahdhib)؛ حي نظر أي متجاورون يرى بعضهم بعضا (mufradat)
- **B004** bakıldığında görülen dış görünüş — toprak bitkisini gösterdi · bakıldığında görülen dış görünüş · güzel dış görünüş · bakılması ve dinlenmesi hoş bir durumda
  نظرت الأرض أرت نباتها (maqayis)؛ منظره خير من مخبره؛ حسنة المنظر والمنظرة (sihah)؛ المنظرة منظر الرجل إذا نظرت إليه فأعجبك أو ساءك؛ ذو منظرة بلا مخبرة؛ المنظر الشيء الذي يعجب الناظر إذا نظر إليه فسره؛ في منظر ومستمع (tahdhib)
- **B005** zamanın vurup yok etmesi [kalıp] — zaman onları vurup yok etti
  نظر الدهر إلى بني فلان فأهلكهم (maqayis;sihah)؛ نظر الدهر إليهم فابتهل؛ خانهم فأهلكهم (mufradat)
- **B006** eş veya denk karşılık — eş, benzer veya denk karşılık · birbirine benzeyen eşler · Tanrı'nın kitabına hiçbir şeyi denk tutma · ikişer ikişer sayılan develer
  هذا نظير هذا؛ إذا نظر إليه وإلى نظيره كانا سواء (maqayis)؛ نظير الشئ مثله؛ النظر والنظير بمعنى واحد مثل الند والنديد؛ نظائر (sihah)؛ فلان نظيرك أي مثلك؛ النظائر لاشتباه بعضها ببعض؛ لا تجعل شيئا نظيرا (tahdhib)؛ النظير المثيل وأصله المناظر (mufradat)
- **B007** özel adlandırma kümesi — hızlı bir bakış · bakıştan doğan heybet · onda solgunluk, çirkinlik veya kusur var · görünmeyen varlıkların kem gözünden etkilenmiş · kem gözden zarar görmüş kişi
  به نظرة أي شحوب (maqayis)؛ النظرة عين الجن؛ رجل فيه نظرة أي شحوب (sihah)؛ النظرة اللمحة بالعجلة؛ النظرة الهيبة؛ فيه نظرة أي شحوب؛ النظرة الشنعة والقبح؛ فيه نظرة أي قبح؛ بها إصابة عين من نظر الجن (tahdhib)؛ به نظرة؛ من أعين الجن نظرة (mufradat)
- **B008** biçime bağlı adlandırmalar — göz bebeği veya gözdeki küçük siyah bölüm · göz · gözyaşı yolunda burnun iki yanındaki damarlar
  الناظر في المقلة السواد الأصغر؛ يقال للعين الناظرة؛ الناظران عرقان في مجرى الدمع على الأنف من جانبيه (sihah)؛ ناظر العين النقطة السوداء الصافية؛ الناظر في العين كالمرآة؛ الناظران عرقان مكتنفا الأنف؛ هما عرقان في مجرى الدمع (tahdhib)
- **B009** biçime bağlı adlandırmalar — bağ bekçisi · koruyucu veya inceleme için gönderilen görevli · yüksek gözetleme yeri · suçsuzluğundan gözünü kaçırmadan bakan
  الناطر والناطور حافظ الكرم؛ الناظر الحافظ؛ المنظرة المرقبة (sihah)؛ المنظرة موضع في رأس جبل فيه رقيب ينظر العدو ويحرسه؛ شديد الناظر إذا كان بريئا من التهمة؛ بعث ناظرا (tahdhib)
- **B010** karşılıklı tartışıp inceleme — karşılıklı tartışıp inceleme · araştırma ve kanıta dayalı inceleme
  ناظره من المناظرة (sihah)؛ المناظرة أن تناظر أخاك في أمر إذا نظرتما فيه معا كيف تأتيانه؛ نظيرك أيضا الذي يناظرك وتناظره (tahdhib)؛ المناظرة المباحثة والمباراة في النظر واستحضار كل ما يراه ببصيرته؛ النظر البحث (mufradat)
- **B011** merhametle iyilik yöneltme — merhamet · Tanrı kullarına iyilik etti ve iyiliklerini bolca verdi
  النظرة الرحمة (tahdhib)؛ نظر الله تعالى إلى عباده هو إحسانه إليهم وإفاضة نعمه عليهم (mufradat)
- **B012** bakıp da görememe ve kavrayamama [kalıp] — bakıyorlar ama göremiyor ve kavrayamıyorlar
  يستعمل النظر في التحير في الأمور؛ ينظرون إليك وهم لا يبصرون؛ نظر عن تحير دال على قلة الغناء (mufradat)

## ن ف س (root_001533) — identity root of نَفْسٌ (w7)

- **B001** soluk alıp verme — soluk alıp verme · gövdeye girip çıkan hava; soluk · tek soluk ya da soluklanma arası · soluklar
  التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)
- **B002** sıkıntıyı hafifletip ferahlatma — Tanrı onun sıkıntısını giderdi · beni sıkıntıdan kurtarıp rahatlat · Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı
  نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)
- **B003** kem gözle zarar verme — zarar verdiğine inanılan bakış · ona kem göz değdi · kem gözle zarar veren kişi
  يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)
- **B004** canlıdaki akışkan kan — kaybıyla yaşamın da yitirildiği kan · hayvandaki akışkan kan
  النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)
- **B005** doğum ve doğuma bağlı kadın-çocuk durumu — doğum yapmış ya da doğum sonrası kanaması olan kadın · doğum ve doğum sonrası kanama dönemi · yeni doğan çocuk · doğmadan önce
  الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)
- **B006** soluk aralı içim ve bir içimlik yudum — bir solukta alınan yudum ya da içim · üç soluk arasıyla içme
  كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)
- **B007** bir deri işlemeye yetecek sepi maddesi payı — deriyi bir kez işlemeye yetecek sepi maddesi · bir işlemelik sepi maddesi payı
  في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)
- **B008** yaşamı sürdüren, bol ve doyurucu su — yaşamı ayakta tutan su · bol ve susuzluğu gideren içecek · tadı kötü, bayat ve içimi güç içecek
  يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)
- **B009** kalıba bağlı yarılıp açılma ve genişleme [kalıp] — yay çatladı ya da yarıldı · sabah söktü, aydınlık yayıldı · gündüz uzayıp genişledi · ırmağın suyu artıp yayıldı
  تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)
- **B010** değerli ve uğrunda yarışılan şey — değerli, önemli ve arzulanan · bir şeyi elde etme ya da üstünlere benzeme yarışı · başkasına vermeye kıyamayıp esirgemek · sahip olduğu şey yüzünden onu kıskanmak
  شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)
- **B011** bedene yaşam veren can — bedene yaşam veren can · insan ya da canlı birey
  النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)
- **B012** şeyin kendisi ve bütün öz varlığı [kalıp] — şeyin tam kendisi ve gerçeği · başkası aracılığıyla değil, bizzat kendisi
  كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)
- **B013** iç düşünce, niyet ve ayırt etme gücü — onun içinden geçen düşünce ya da niyet · ayırt etmeyi sağlayan zihinsel güç
  نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)
- **B014** sağlam, cömert ve onurlu yaradılış — sağlam karakterli, dayanıklı ve cömert adam · büyüklük duygusu, onur, yüksek amaç ve kendine saygı
  رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)
- **B015** uzaklık, genişlik ve zaman payı — işinde rahat hareket edecek genişlikte · ek süre ya da hareket alanı · daha uzak, daha uzun ya da daha geniş
  هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)
- **B016** eski bahis oyunundaki beşinci pay oku — eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok
  النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)

## ق د م (root_001207) — identity root of قَدَّمَتْ (w9)

- **B001** ayak — ayak
  القدم ما يطأ عليه الإنسان (ayn;tahdhib)؛ القدم واحد الأقدام (sihah)؛ القدم قدم الرجل وجمعه أقدام (mufradat)؛ قدم الإنسان معروفة ولعلها سميت بذلك لأنها آلة للتقدم والسبق (maqayis)
- **B002** önceden oluşmuş etki veya paye — öncül etki, iyilik veya saygın konum · önceden kazanılmış iyi paye · önceden işlenmiş kötülük · önder ve saygın kişi · hükümdar veya önder
  القدمة والقدم أيضا السابقة في الأمر وللكافرين قدم شر (ayn)؛ القدم أيضا السابقة في الأمر ولفلان قدم صدق أي أثرة حسنة (sihah)؛ قدم الصدق المنزلة الرفيعة والقدم السابقة وكل ما قدمت من خير والعمل الصالح واليد والمعروف والصنيعة والشرف القديم (tahdhib)؛ متقدم على فلان أي أشرف منه (mufradat)؛ لفلان قدم صدق أي شيء متقدم من أثر حسن والملك هو المقدم (maqayis)؛ رجل قدموس سيد وهو ذلك المعنى (maqayis-variant)
- **B003** eskilik ve önceden var olma — eskilik; sonradan oluşmama · eski; geçmiş zamana dayanan · eskiden; geçmiş zamanda · eski olan
  القدم مصدر القديم من كل شيء (ayn)؛ قدم الشيء فهو قديم والقدم خلاف الحدوث وقدما كان كذا (sihah)؛ القدم العتق مصدر القديم وقد قدم يقدم (tahdhib)؛ حديث وقديم والقدم وجود فيما مضى (mufradat)؛ القدم خلاف الحدوث وشيء قديم إذا كان زمانه سالفا (maqayis)؛ القدموس القديم وأصله من القدم (maqayis-variant)
- **B004** öne geçme, önde ilerleme veya erken davranma — öne geçmek; önde olmak · öne geçme ve ilerleme · ön taraf; önde · önüne geçmek; vaktinden önce davranmak · duraksamadan ileri gitmek
  قدم فلان قومه أي يكون أمامهم والقدم المضي أمام ويمضي قدما أي لا ينثني وقدام خلاف وراء والقدم ضد الأخر (ayn)؛ قدم أي تقدم وقدم بين يديه أي تقدم ومضى قدما لم يعرج ولم ينثن واستقدم وتقدم بمعنى ومقدم نقيض مؤخر (sihah)؛ القدم المضي وهو الإقدام وقدام خلاف وراء والقدم ضد أخر وقدم فلان فلانا إذا تقدمه ولا تقدموا معناه لا تتقدموا قبل الوقت (tahdhib)؛ به اعتبر التقدم والتأخر (mufradat)؛ أصل صحيح يدل على سبق وأصله مضى فلان قدما لم يعرج ولم ينثن ومقدمة الجيش أوله (maqayis)
- **B005** yolculuktan dönüş — yolculuktan dönmek; geri gelmek · yolculuktan dönüş; yolcunun geliş zamanı · yolculuktan dönenler
  القدوم الرجوع من السفر وقدم يقدم (ayn)؛ قدم من سفره قدوما ومقدما والقدام القادمون من سفر (sihah)؛ القدوم الإياب من السفر وقدم فلان من سفره يقدم قدوما (tahdhib)؛ من الباب قدم من سفره قدوما ويقال القدام القادمون من سفر (maqayis)
- **B006** cesaretle öne atılma ve gözüpeklik — gözüpeklik; cesaretle öne atılma · bir işe cesaretle girişmek · gözüpek, atılgan savaşçı · ileri! · gözüpek ve öne atılan kişi
  رجل قدم مقتحم للأشياء يتقدم الناس ويمضي في الحرب قدما (ayn)؛ أقدم على الأمر إقداما والإقدام الشجاعة وأقدم زجر للفرس والمقدام الكثير الإقدام على العدو (sihah)؛ أقدم على قرنه إقداما وقدما ومقدما إذا تقدم عليه بجرأة وضده الإحجام ورجل مقدام في الحرب جريء (tahdhib)؛ أقدم على الشيء إقداما وأقدم زجر للفرس ومضى القوم في الحرب اليقدمية (maqayis)
- **B007** ön bölüm veya ilk kesim — ordunun öncü birliği · gözün veya başın ön kısmı · alın önü ve perçem bölgesi · kuşun ön kanat telekleri · eyer takımının ön kısmı · deve veya ineğin öndeki iki meme başı · dağın öne çıkan burnu · yüzüstü düşmek
  مقدم العين ما يلي الأنف والمقدمة الناصية وما استقبلك من الجبهة والجبين وقادمة الرحل والقادمة الريشة التي تلي منكب الجناح (ayn)؛ قوادم الطير مقاديم ريشه وقيدوم الجبل أنف يتقدم منه وقيدوم كل شيء مقدمه وصدره ومقدمة الجيش أوله وقادمتا الناقة (sihah)؛ مقدمة الجيش الذين يتقدمون الجيش ومقدم العين ومقدم الرأس والمقدمة الناصية وقادمة الرحل وللناقة قادمان وقوادم ريش الطائر (tahdhib)؛ قادمة الرحل خلاف آخرته وقادمة من أطباء الناقة وقادم الإنسان رأسه وقوادم الطير ومقدمة الجيش أوله وقيدوم الجبل أنف يتقدم منه (maqayis)
- **B008** ahşap yontma keseri — ahşap yontma keseri
  القدوم مخفقة الحديدة التي ينحت بها الخشب (ayn)؛ القدوم التي ينحت بها مخففة ولا تقل قدوم بالتشديد (sihah)؛ القدوم التي ينحت بها وجمعها قدم واختتن إبراهيم بالقدوم قال قطعه بها (tahdhib)؛ مما شذ عن هذا الأصل القدوم الحديدة ينحت بها وهي معروفة (maqayis)
- **B009** belirli bir yer adı — belirli bir yer adı
  القدوم أيضا اسم موضع (sihah)؛ القدوم مكان (maqayis)
- **B010** bir işe yönelip onu amaçlamak [kalıp] — bir işe yönelip onu amaçlamak
  قدم فلان إلى أمر كذا أي قصد له ومنه وقدمنآ إلى ما عملوا قال الفراء والزجاج قدمنا عمدنا وقصدنا (tahdhib)

## غ د و (root_001076) — identity root of لِغَدٍ (w10)

- **B001** günün ilk vakti ve bu vakitte yola çıkma — günün erken vaktinde gitmek · günün ilk vakti ve bu vakitteki gidiş · erken ibadet ile güneşin doğuşu arasındaki vakit · günün erken vakti · günün erken vaktinde yola çıkma · birinin yanına günün erken vaktinde gitmek · ertesi günün erken vakti · sabahları ve akşamları gidip gelmek
  أصل صحيح يدل على زمان؛ الغدو يقال غدا يغدو (maqayis)؛ غدا غدوا واغتدى اغتداء (ayn)؛ الغدوة ما بين صلاة الغداة وطلوع الشمس؛ الغدو نقيض الرواح؛ غاداه أي غدا عليه (sihah)؛ غدوت أغدو غدوا؛ الغدو جمع مثل الغدوات (tahdhib)؛ الغدوة والغداة من أول النهار؛ قد غدوت أغدو (mufradat)
- **B002** yarın — ertesi günün erken vakti · yarın · yarın
  أفعل ذلك غدا؛ والأصل غدوا (maqayis)؛ الغد أصله غدو (sihah)؛ قدمت لغد بغير واو فإذا صرفوها قالوا غدوت أغدو (tahdhib)؛ غد يقال لليوم الذي يلي يومك الذي أنت فيه (mufradat)
- **B003** günün erken vaktinde beliren bulut — günün erken vaktinde beliren bulut · günün erken vaktinde beliren bulutlar
  الغادية سحابة تنشأ صباحا (maqayis)؛ الغادية سحابة تنشأ صباحا وجمعها غوادي (ayn)؛ الغادية سحابة تنشأ صباحا (sihah)؛ الغادية سحابة تنشأ صباحا وجمعها الغوادي (tahdhib)؛ الغادية السحاب ينشأ غدوة (mufradat)
- **B004** günün başında yenen yemek — günün başında yenen yemek · günün ilk öğününü yemek · günün ilk öğününü yiyen kişi · günün ilk öğününü yiyen kişi
  الغداء الطعام بعينه سمي بذلك لأنه يؤكل في ذلك الزمان (maqayis)؛ الغداء ما يؤكل من أول النهار (ayn)؛ الغداء الطعام بعينه وهو خلاف العشاء؛ تغدى؛ الغديان المتغدي (sihah)؛ الغداء ما يؤكل أول النهار وقد تغدى الرجل فهو متغد (tahdhib)؛ الغداء طعام يتناول في ذلك الوقت (mufradat)
- **B005** gebe hayvanın karnındaki yavru — gebe hayvanın karnındaki yavru; ayrıca beklenen yavruya dayalı belirsiz satış
  الغدوي كل ما كان في بطون الحوامل وربما جعل في الشاء خاصة (ayn)؛ الغدوي بالدال أن يبيع الشيء بنتاج ما نزى به الكبش ذلك العام؛ كل ما في بطون الحوامل غدوي من الإبل والشاء؛ نهي عن الغدوي وهو كل ما في بطون الحوامل؛ الغدوي الحمل والجدي لا يغذى بلبن أمه (tahdhib)

## خ ب ر (root_000387) — identity root of خَبِيرٌۢ (w15)

- **B001** bilgi edinme, bildirme ve deneyerek iç yüzü tanıma — bir olay veya durum hakkında edinilen ve aktarılan bilgi · bilgi vermek; bildirmek · bir konuyu sorup bilgi edinmek · sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma · sınayıp deneyerek bilgi sahibi olmuş kişi · bilgili; bir işin iç yüzüne hakim · dış görünüşün karşısındaki iç yüz ve gerçek nitelik
  الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)
- **B002** gevşek, alçak ve su tutan arazi veya su birikintisi — gevşek, yumuşak veya alçak olup su toplayan arazi · sıcak, ağaçlı ve suyu bol yer · akış yatağında oluşan geçilebilir su birikintisi
  الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)
- **B003** üründen pay karşılığı ortakçılık ve bunu yapan çiftçi — toprağı işleyen çiftçi · ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık
  الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)
- **B004** büyük su tulumu ve bolluğuyla ona benzetilen dişi deve — büyük ve geniş su tulumu · bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve
  الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)
- **B005** yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü — kesilip yenebilen yumuşak bitki · yün veya ince hayvan kılı · devenin ağzında oluşan veya ağzından çıkan köpük
  الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)
- **B006** ortak alınıp kesilen koyun veya bölüşülen et-balık payı — ortaklaşa alınıp kesilen ve eti bölüşülen koyun · et veya balıktan alınan pay
  الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)

## ع م ل (root_001046) — identity root of تَعْمَلُونَ (w17)

- **B001** bilerek yapılan iş veya eylem — bilerek yapılan iş veya eylem · iş yapan kimse · kendisi için çalışmak veya işe koyulmak · iş veya uğraş · işte kullanılan sığırlar · iyi ve kötü davranışlar
  أصل واحد صحيح وهو عام في كل فعل يفعل (maqayis); عمل عملا فهو عامل (ayn;sihah;tahdhib); كل فعل يكون من الحيوان بقصد (mufradat); الأعمال الصالحة والسيئة (mufradat)
- **B002** işe koşmak veya kullanmak — onu çalıştırdı · onu kullandı veya çalıştırdı · ondan çalışmasını istedi · görüşünü, sözünü veya mızrağını kullandı · kerpici yapıda kullandı · zihnini işletip düşündü
  يستعمل غيره ويعمل رأيه أو كلامه أو رمحه؛ والبناء يستعمل اللبن (maqayis); أعمله غيره واستعمله بمعنى؛ واستعمله أيضا أي طلب إليه العمل (sihah); أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه (tahdhib)
- **B003** işe görevli kılma veya görev üstlenme — bağışları toplayan görevliler · bağış işi görevlisi · resmi bir işi üstlendi · birine iş görevi verme · bir kimseyi bir şehirde görevli kılmak
  العاملين عليها هم السعاة الذين يأخذون الصدقات (tahdhib); استعمل فلان إذا ولي عملا من أعمال السلطان (tahdhib); التعميل تولية العمل (sihah); العاملين عليها هم المتولون على الصدقة (mufradat)
- **B004** iş ücreti — iş karşılığı ücret veya pay · iş ücreti
  العمالة أجر ما عمل (maqayis); العمالة بالضم رزق العامل (sihah); العمالة رزق العامل (tahdhib); العملة والعمالة أجر العمل (tahdhib); العمالة أجرته (mufradat)
- **B005** karşılıklı işlem — karşılıklı işlem veya alışveriş ilişkisi · bir kimseyle alışveriş veya benzeri işlem yaptı
  المعاملة مصدر من قولك عاملته وأنا أعامله معاملة (maqayis); عاملت الرجل أعامله معاملة في المبايعة وغيرها (tahdhib)
- **B006** el işçileri — elleriyle çalışan işçi topluluğu
  العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه (maqayis); العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره (tahdhib)
- **B007** zahmete girmek [kalıp] — kendini yorma · ihtiyacın için zahmete gireceğim · zahmet etme
  لا تتعمل في أمرك ذا كقولك لا تتعن (tahdhib); سوف أتعمل في حاجتك أي أتعنى (tahdhib); لا تعمل أي لا تتعن (tahdhib)
- **B008** işe yatkın ve dayanıklı — işe yatkın üstün dişi deve · işe nispet edilen dişi deve · işe yatkın adam · işe yatkın çalışkan adam · işe yatkın, güçlü ve üstün dişi deve
  اليعملة من الإبل اسم لها اشتق من العمل (maqayis); رجل عمل بكسر الميم أي مطبوع على العمل؛ ورجل عمول؛ اليعملة الناقة النجيبة المطبوعة على العمل (sihah); ناقة عملة بينة العمالة مثل اليعملة إذا كانت فارهة (tahdhib); اليعملة مشتقة من العمل (mufradat)
- **B009** mızrak ucunun alt bölümü — mızrağın sivri ucuna yakın ön gövde bölümü · mızrağın ucuna yakın gövde bölümü
  عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره (maqayis); عامل الرمح ما يلي السنان وهو دون الثعلب (sihah); عامل الرمح صدره دون السنان ويجمع عوامل (tahdhib); عامل الرمح ما يلي السنان (mufradat)
- **B010** iş gören beden parçası [kalıp] — hayvanın ayakları · uzağı gören göz
  عوامل الدابة قوائمه واحدها عاملة (tahdhib); وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر (tahdhib)
- **B011** işlek yol [kalıp] — işlek ve belirgin yol
  طريق معمل أي لحب مسلوك (sihah)
- **B012** yaya yolcular [kalıp] — yaya giden yolcular
  المسافرون إذا مشوا على أرجلهم يسمون بني العمل (tahdhib)

## و ل ه (root_005296) — documented alternative for ٱللَّهَ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:18, and ## Buluşmalar) =====
## Gece örtüsü ve açılan gün

Surede örtmek anlamı taşıyan birçok kelime vardır. "Küfür" kelimesinin kökü örtmektir: {ar:الستر والتغطية, tr:es-setr ve't-tağtiye, gloss:örtme ve kapama, source:"ك ف ر,B001"}. Bu kökte gece de kâfirdir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfir, gloss:gece, karanlığıyla örttüğü için "kâfir"dir, source:"ك ف ر,B002"}. Onuncu ayetteki bağışlanma duası da aynı örtme alanındadır: {ar:الغفر الستر, tr:el-ğafr es-setr, gloss:ğafr örtmektir, source:"غ ف ر,B001"}. "Cennet" de gecenin karanlığıdır: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyl, gloss:gecenin cenânı, karanlığı ve eşyayı örtmesidir, source:"ج ن ن,B002"}. Nifak da bir örtüdür: {ar:النفاق لأن صاحبه يكتم خلاف ما يظهر, tr:en-nifâk, gloss:nifak, sahibinin gösterdiğinin tersini gizlemesidir, source:"ن ف ق,B004"}. On dördüncü ayetteki "ardından" kelimesi de saklamayı anlatır: {ar:التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره, tr:et-tevriye es-setr, gloss:tevriye örtmedir; haberi gizleyip başkasını gösterdiğinde "verraytu" dersin, source:"و ر ي,B005"}. Bu yüzden münafıkların duvar arkasında savaşması ile sözlerinin arkasına gizlenmesi aynı kelimeyle işitilir. Tek fark, bir örtünün kurtarması, ötekinin boğmasıdır. Onuncu ayette istenen bağış örtüsü, kişiyi koruyan bir örtüdür. Küfür ve nifak örtüsü ise onu karanlıkta bırakır. On yedinci ayetteki "zalimler" kelimesi karanlığın kendisidir: {ar:الظلمة خلاف النور, tr:ez-zulme hılâfu'n-nûr, gloss:zulmet nurun karşıtıdır, source:"ظ ل م,B001"}. Ayette geçen "ateş" kelimesi ise ışıkla aynı yoldan adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan adlandırılmıştır, source:"ن و ر,B002"}. Ama ateş burada aydınlatmaz, yakar. Münafıklar da bir ateş yakar ama Allah ışıklarını götürür ve onları {ar:فِى ظُلُمَٰتٍ لَّا يُبْصِرُونَ, tr:fî zulumâtin lâ yubsırûn, gloss:göremedikleri karanlıklarda, source:2:17} bırakır. Kıyamette münafıklar müminlerin ışığından almak ister, onlara {ar:ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًا, tr:irci'û verâekum fe'ltemisû nûrâ, gloss:arkanıza dönün de bir ışık arayın, source:57:13} denir. Hemen ardından iki tarafı birbirinden ayıran bir sur çekilir {source:57:13}. Bu ayette surun ardı, ışık ve ayrılık, bu surenin kale, "ardında" ve karanlık kelimeleri bir arada bulunur.

Örtünün karşısında sabah açılır. Yirmi birinci ayetteki "parça parça olmuş" kelimesinin ailesinde sabah da vardır: {ar:الصديع الصبح, tr:es-sadî' es-subh, gloss:sadî' sabahtır, source:"ص د ع,B006"}. Dokuzuncu ayetteki "nefisler" kelimesi de sabahın nefes almasıdır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subh, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Kur'an aynı ifadeyi yemin olarak kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. On sekizinci ayetteki "yarın" kelimesi de seher vaktidir: {ar:الغدوة ما بين صلاة الغداة وطلوع الشمس, tr:el-ğudve, gloss:ğudve, sabah namazı ile güneşin doğuşu arasıdır, source:"غ د و,B001"}. Üçüncü ayetteki "sürgün" (celâ) kelimesi de açığa çıkıp görünür olmaktır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey' ve burûzuh, gloss:bir şeyin açılıp ortaya çıkması, source:"ج ل و,B001"}. Bu kelimenin bir dalı da gündüzün beyazlığıdır {source:"ج ل و,B007"}. Kur'an bu fiili gündüz için kullanır: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Sürgün edilenler kalelerinden çıkarılıp açık alana konur. Gece onları örtüyordu, şimdi her şey gün ışığına çıkar. Yirmi ikinci ayet bu iki yarıyı Allah'ın bilgisinde birleştirir: {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ, tr:'âlimu'l-ğaybi ve'ş-şehâde, gloss:görünmeyeni ve görüneni bilen, source:59:22}. "Gayb" kelimesinin kökü gözlerden gizlenmektir, güneşin batmasına da bu kökle "gâbet" denir {source:"غ ي ب,B001"}. "Şehâdet" ise oradan bakıp görmektir {source:"ش ه د,B001"}. Yirmi birinci ayetteki "hâşi'" kelimesi de batmaya yaklaşan yıldızlar için kullanılır: {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşa'ati'l-kevâkib, gloss:yıldızlar batmaya yaklaşınca "haşaat" denir, source:"خ ش ع,B003"}. Böylece batan yıldızla doğan sabah aynı ayette yan yana durur. Gece ile gündüzde gizlenen ile açıkta yürüyenin Allah katında eşit olduğu da söylenir {source:13:10}.

Kaynaklar: 59:2 كَفَرُوا ك ف ر B001, B002; 59:10 ٱغْفِرْ غ ف ر B001; 59:20 ٱلْجَنَّةِ ج ن ن B002; 59:11 نَافَقُوا ن ف ق B004; 59:14 وَرَآءِ و ر ي B005; 59:17 ٱلظَّٰلِمِينَ ظ ل م B001; 59:3 ٱلنَّارِ ن و ر B002; 59:21 مُّتَصَدِّعًا ص د ع B006; 59:9 أَنفُسِهِمْ ن ف س B009; 59:18 لِغَدٍ غ د و B001; 59:3 ٱلْجَلَآءَ ج ل و B001, B007; 59:22 ٱلْغَيْبِ غ ي ب B001; 59:22 ٱلشَّهَٰدَةِ ش ه د B001; 59:21 خَٰشِعًا خ ش ع B003

## Ön ve arka: topuk, iz ve el

On ikinci ayet münafıkların yardımının sonunu bir dönüş hareketiyle anlatır: {ar:وَلَئِن نَّصَرُوهُمْ لَيُوَلُّنَّ ٱلْأَدْبَٰرَ ثُمَّ لَا يُنصَرُونَ, tr:ve le-in nasarûhum le-yuvellunne'l-edbâra summe lâ yunsarûn, gloss:yardım etseler bile mutlaka arkalarını dönüp kaçarlar, sonra kendilerine de yardım edilmez, source:59:12}. "Arka" kelimesi önün karşıtıdır {source:"د ب ر,B001"}. Kaçmak da arka dönmektir {source:"و ل ي,B007"}. Dördüncü ve yedinci ayetlerdeki "ikâb" (ceza) ile on yedinci ayetteki "âkıbet" (son) kelimeleri topuk köküne bağlıdır: {ar:العقب مؤخر القدم, tr:el-'akib mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. Ceza da, suçun ardından en son geldiği için bu adla anılır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet 'ukûbeten, gloss:suçun ardından ikinci ve son geldiği için ukûbet denildi, source:"ع ق ب,B007"}. Arkasını dönen kişiye dönüp bakmamak da bu kökle ifade edilir: {ar:ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر, tr:vellâ mudbiren ve lem yu'akkıb, gloss:arkasını döndü ve geri dönüp bakmadı, source:"ع ق ب,B003"}. Sırtını dönüp kaçanın topuğunun dibinde ise ceza yürür. On altıncı ve on yedinci ayetler, Şeytan'ın insanı inkâra çağırıp sonra ondan uzaklaşmasını anlatır. Kur'an bu sahneyi Bedir'de bir dönüş hareketiyle de gösterir: {ar:نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌ مِّنكُمْ إِنِّىٓ أَرَىٰ مَا لَا تَرَوْنَ إِنِّىٓ أَخَافُ ٱللَّهَ ۚ وَٱللَّهُ شَدِيدُ ٱلْعِقَابِ, tr:nekesa 'alâ 'akibeyhi ve kâle innî berî'un minkum innî erâ mâ lâ teravne innî ehâfu'llâh, va'llâhu şedîdu'l-'ikâb, gloss:topukları üzerinde geri döndü ve "ben sizden uzağım, sizin görmediğinizi görüyorum, ben Allah'tan korkarım" dedi; Allah'ın cezası çetindir, source:8:48}. On altıncı ayetteki sözler ile dördüncü ayetin son sözleri bu ayette yan yana durur. Şeytan'ın uzaklaşması, topukları üzerinde geri dönmektir. İnsana karşı tavrı da {ar:وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًا, tr:ve kâne'ş-şeytânu li'l-insâni hazûlâ, gloss:şeytan insanı yüzüstü bırakandır, source:25:29} diye özetlenir. Arkasını dönüp kaçanın akıbeti başka bir ayette de aynen anlatılır {source:3:111}. Müminlerden de arkalarını dönmeyeceklerine dair ahit alınmıştır {source:33:15}.

Müminler ise bir yolda ardı ardına yürür. Onuncu ayetteki {ar:وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ, tr:vellezîne câû min ba'dihim, gloss:onlardan sonra gelenler, source:59:10} ifadesindeki "sonra" kelimesi topuk izine bağlanır: {ar:وما خلف بعقبه فهو من بعده, tr:ve mâ halefe bi-'akibihî fe-huve min ba'dih, gloss:topuğunun arkasında kalan, ondan sonradır, source:"ب ع د,B002"}. Onlar {ar:سَبَقُونَا بِٱلْإِيمَٰنِ, tr:sebekûnâ bi'l-îmân, gloss:bizden önce imana koştular, source:59:10} diye öncekileri anar. "Sebk" yolda öne geçmektir {source:"س ب ق,B001"}. Dokuzuncu ayetteki "îsâr" (tercih etmek) da iz sürmenin köküdür: {ar:الأثر الاستقفاء والاتباع وذهبت في إثره, tr:el-eser el-istikfâ' ve'l-ittibâ', gloss:eser, peşinden gitmek ve izine uymaktır, source:"ء ث ر,B004"}. Bu sırayı Kur'an da adlarıyla verir: {ar:وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم, tr:ve's-sâbikûne'l-evvelûne mine'l-muhâcirîne ve'l-ensâri ve'llezîne'ttebe'ûhum, gloss:muhacirlerden ve ensardan ilk öncüler ve onlara uyanlar, source:9:100}. Böylece münafıklar düşmana arkalarını döner, müminler ise öndekilerin izinden yürür. On sekizinci ayet bu düzende bakışı öne çevirir: {ar:وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ, tr:ve'l-tenzur nefsun mâ kaddemet li-ğad, gloss:herkes yarına ne gönderdiğine baksın, source:59:18}. "Önden göndermek" fiili önün ve arkanın kelimesidir: {ar:قدام خلاف وراء والقدم ضد الأخر, tr:kuddâm hılâfu verâ', gloss:ön, arkanın karşıtıdır, source:"ق د م,B004"}. Bu fiil on dördüncü ayetteki "ardından" ve üçüncü ayetteki "ahiret" kelimeleriyle bir karşıtlık kurar. "Ahiret" en son gelendir {source:"ء خ ر,B001"}. "Ardından" ise hem arkayı hem önü anlatabilir {source:"و ر ي,B006"}. Tedbir de akıbete bakmaktır: {ar:التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته, tr:et-tedbîr, gloss:tedbir, bir işin akıbetinin nereye varacağına bakmaktır, source:"د ب ر,B006"}. Bu ifadede on ikinci ayetin "arka" kökü, on yedinci ayetin "akıbet"i ve on sekizinci ayetin "bakmak" fiili birleşir. Kim akıbetine bakarsa, topuğunun ardındaki cezadan kurtulur. Kur'an bu bakışı başka yerlerde de anlatır: {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:'alimet nefsun mâ kaddemet ve ehharat, gloss:herkes önden ne gönderdiğini, geride ne bıraktığını bilir, source:82:5}. Pişman olan da {ar:يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önden bir şey gönderseydim, source:89:24} der.

El bu iki ayeti birbirine bağlar. İkinci ayette evler "kendi elleriyle" yıkılır. El, bir deyimde kişinin kendi işlediğinin sahibi olmasıdır: {ar:هذا ما قدمت يداك أي جنيته أنت, tr:hâzâ mâ kaddemet yedâk, gloss:bu senin ellerinin önden gönderdiğidir, yani bunu sen işledin, source:"ي د ي,B009"}. Bu ifadede ikinci ayetin "eller"i ile on sekizinci ayetin "önden gönderdi" fiili birleşir. Kur'an da {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâh, gloss:kişinin ellerinin önden gönderdiğine baktığı gün, source:78:40} der. Burada bakmak, önden göndermek ve el bir aradadır. On sekizinci ayetin çağrısının tersi de vardır: {ar:وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ, tr:ve nesiye mâ kaddemet yedâh, gloss:ellerinin önden gönderdiğini unuttu, source:18:57}. On dokuzuncu ayetteki unutanlar da aynı yere düşer. Münafıklar ise ellerini sıkar ve unutur: {ar:وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ, tr:ve yakbıdûne eydiyehum, nesu'llâhe fe-nesiyehum, inne'l-munâfıkîne humu'l-fâsikûn, gloss:ellerini sıkı tutarlar; Allah'ı unuttular, O da onları unuttu; münafıklar fâsıkların ta kendileridir, source:9:67}. Bu ayet, sure içinde dağınık duran unutma, fısk ve sıkı tutulan el kavramlarını tek cümlede toplar. Yedinci ayetteki "dûle" de elden ele geçmektir {source:"ي د ي,B007"}. El ayrıca nimet ve iyiliktir {source:"ي د ي,B003"}. Dokuzuncu ayette Ensar elindekini açar, sıkmaz. Kur'an eli boyna bağlamayı da yasaklar {source:17:29}.

Kaynaklar: 59:12 لَيُوَلُّنَّ و ل ي B007; 59:12 ٱلْأَدْبَٰرَ د ب ر B001, B006; 59:4/7 ٱلْعِقَابِ ع ق ب B002, B003, B007; 59:17 عَٰقِبَتَهُمَآ ع ق ب B002; 59:10 بَعْدِهِمْ ب ع د B002; 59:10 سَبَقُونَا س ب ق B001; 59:9 يُؤْثِرُونَ ء ث ر B004; 59:18 قَدَّمَتْ ق د م B004; 59:3 ٱلْءَاخِرَةِ ء خ ر B001; 59:14 وَرَآءِ و ر ي B006; 59:2 بِأَيْدِيهِمْ ي د ي B009; 59:7 دُولَةً ي د ي B007; 59:9 (Ensar'ın verişi) ي د ي B003

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

