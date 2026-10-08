Focus: 59:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_4/D.r13/context.md =====
# 59:4 — focus

ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ ۖ وَمَن يُشَآقِّ ٱللَّهَ فَإِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ذَٰلِكَ | ذَٰلِك |  | DEM |
| 2 | بِأَنَّهُمْ | أَنّ |  | P;ACC;PRON |
| 3 | شَآقُّوا۟ | شَآقُّ | ش ق ق | V;PRON |
| 4 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 5 | وَرَسُولَهُۥ | رَسُول | ر س ل | CONJ;N;PRON |
| 6 | وَمَن | مَن |  | REM;COND |
| 7 | يُشَآقِّ | شَآقُّ | ش ق ق | V |
| 8 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 9 | فَإِنَّ | إِنّ |  | RSLT;ACC |
| 10 | ٱللَّهَ | ٱللَّه | ء ل ه | PN |
| 11 | شَدِيدُ | شَدِيد | ش د د | N |
| 12 | ٱلْعِقَابِ | عِقَاب | ع ق ب | DET;N |


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
- 59:4 ◀ focus ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ ۖ وَمَن يُشَآقِّ ٱللَّهَ فَإِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
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


===== _commentary/v16/work/59_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ق ق (root_000807) — identity root of شَآقُّوا۟ (w3)

- **B001** yarma, yarılma ve açılma — bir şeyi yarıp açmak veya ikiye ayırmak · çatlak, yarık veya delik · dağda, yerde veya başka bir şeydeki çatlaklar · derinin çatlaması veya hayvanın bileklerindeki çatlak hastalığı · dişin çıkması veya tanın sökmesi
  شققت الشيء أشقه شقا إذا صدعته (maqayis); الشق مصدر قولك شققت والشقاق تشقق الجلد والصدوع في الجبال والأرضين (tahdhib); الشق الخرم الواقع في الشيء وشققته بنصفين (mufradat); شققت الشيء فانشق وشققت الحطب وغيره فتشقق وشق ناب البعير وشق الفجران (sihah;tahdhib)
- **B002** yarım veya yan — bir şeyin yarısı veya yanı · öz kardeş, denk veya insanın öteki yarısı · başın ve yüzün bir yarısını tutan ağrı, migren
  يقال لنصف الشيء الشق والشق أيضا الناحية من الجبل والشق الشقيق وشق نفسي (maqayis); الشق بالكسر نصف الشيء والشق أيضا الناحية من الجبل والشق أيضا الشقيق والشقيقة وجع يأخذ نصف الرأس والوجه (sihah); الشق الجانب والشق الشقيق وخذ هذا الشق لشقة الشاة والشقيقة صداع يأخذ في نصف الرأس والوجه (tahdhib); شققته بنصفين (mufradat)
- **B003** ağır güçlük ve çaba — ağır iş, güçlük ve yoğun çaba · bütün gücünü zorlayarak, çok güçlükle · bir işin kişiye ağır gelmesi
  أصاب فلانا شق ومشقة وذلك الأمر الشديد (maqayis); الشق المشقة ومنه بالغيه إلا بشق الأنفس (sihah); الشق المشقة في السير والعمل ومعناه إلا بجهد الأنفس وشق علي ذاك الأمر مشقة أي ثقل علي (tahdhib)
- **B004** anlaşmazlıkla bölünüp ayrılma — anlaşmazlık, düşmanlık ve topluluktan ayrılma · birliği bozup topluluktan ayrılmak
  الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت وشقوا عصا المسلمين (maqayis); شق فلان العصا أي فارق الجماعة والمشاقة والشقاق الخلاف والعداوة (sihah); الشقاق العداوة بين فريقين والخلاف بين اثنين وشق الخوارج عصا المسلمين (tahdhib)
- **B005** uzak yol ve uzun yolculuk — uzun yolculuk veya uzak yol mesafesi · uzak ve aşılması güç yol
  الشقة مسير بعيد إلى أرض نطية وهذه شقة شاقة ولكن بعدت عليهم الشقة (maqayis); الشقة أيضا السفر البعيد وشقة شاقة (sihah); الشقة بعد مسير إلى الأرض البعيدة يقال شقة شاقة (tahdhib)
- **B006** yarılıp ayrılmış parça — tahtadan kopan kıymık veya bir kumaş parçası · çok öfkelenip çılgına dönmek
  الشقة شظية تشظى من لوح أو خشبة وفطارت منه شقة والشقة من الثياب (maqayis); الشقة شظية تشظى من لوح أو خشبة والشقة بالضم من الثياب (sihah); الشقة شظية تشق من لوح أو خشبة وشقة في الأرض وشقة في السماء والشقة معروفة في الثياب (tahdhib)
- **B007** kum sırtları arasındaki otlu açıklık — kum sırtları arasında ot bitiren açıklık veya sert toprak · kırmızı anemon çiçeği · bol yağmur taşıyan bulutlar
  الشقيقة فرجة بين الرمال تنبت والشقيقة أرض غليظة بين حبلين من الرمل (maqayis); الشقيقة الفرجة بين الحبلين من حبال الرمل تنبت العشب وشقائق النعمان معروف (sihah); الشقيقة الفرجة بين الرمال تنبت العشب ونور أحمر يسمى شقائق النعمان والشقائق أيضا سحائب (tahdhib)
- **B008** devenin böğürme kesesi — devenin böğürürken ağzından çıkardığı boğaz dokusu · gür sesli ve sözünde usta hatip · erkek devenin böğürmesi veya kuşun özel ötüşü
  الشقشقة لهاة البعير ويقال للخطيب هو شقشقة (maqayis); شقشق الفحل شقشقة هدر والعصفور يشقشق والشقشقة شيء كالرئة يخرجها البعير وإذا قالوا للخطيب ذو شقشقة (sihah); الشقشقة لهاة الجمل وجمعها الشقاشق والخطيب الجهير الصوت هرت الشقاشق (tahdhib)
- **B009** amaç çizgisinden yana sapma — konuşmada veya tartışmada ana amaçtan sağa sola sapmak · koşarken bir yanına eğilen at
  اشتق في الكلام في الخصومات يمينا وشمالا مع ترك القصد وفرس أشق إذا مال في أحد شقيه عند عدوه (maqayis); الاشتقاق الأخذ في الكلام وفي الخصومة يمينا وشمالا وفرس أشق (sihah); الاشتقاق الأخذ في الخصومات يمينا وشمالا وفرس أشق وقد اشتق في عدوه (tahdhib)
- **B010** uzun veya bacak arası geniş at — uzun veya bacak arası geniş at; ayrıca zayıflayıp incelmek
  فرس أشق أي طويل والأنثى شقاء (sihah); فرس أشق له معنيان الأشق الطويل والأشق من الخيل الواسع ما بين الرجلين وتشقق الفرس تشققا إذا ضمر (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهَ (w4)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ر س ل (root_000563) — identity root of وَرَسُولَهُۥ (w5)

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

## ش د د (root_000782) — identity root of شَدِيدُ (w11)

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

## ع ق ب (root_001033) — identity root of ٱلْعِقَابِ (w12)

- **B001** bağlama ve kiriş yapımında kullanılan sert beyaz tendon — kiriş yapılan sert beyaz tendon · ayak bileklerinin arkasındaki gergin tendon · oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak
  العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)
- **B002** topuk ve hemen arkasında kalan iz — topuk, ayağın arka bölümü · topuklar · ardınca çok kişi yürüyen, çok izlenen · birinin hemen ardından, onun izinden
  العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)
- **B003** dönüp geri çekilmek [kalıp] — dönüp geri çekilmek · geri dönmedi, arkasına bakmadı veya beklemedi
  ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)
- **B004** ardında kalan çocuklar ve torunlar — kişinin ardından kalan çocukları ve torunları · ardında çocuk veya soy bırakmadı
  عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)
- **B005** birbirinin ardından gelme ve yerini alma — öncekinin ardından gelen ve onun yerini alan · ardıl, bir başkasının ardından gelen · gece ile gündüzün sırayla birbirinin yerini alması · sırayla nöbet değiştiren gece ve gündüz görevlileri · binme veya çalışma sırası, nöbet
  كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)
- **B006** sonuç ve varılan son durum — son, sonuç, varılan nihai durum · karşılık veya sonuç; kimi kullanımda iyi karşılık · buna yol açtı, ardından bunu doğurdu
  أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)
- **B007** suçtan sonra verilen kötü karşılık — ceza, cezalandırma · onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz
  عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)
- **B008** ardından izleyip yeniden inceleme — hak istemek veya itiraz etmek için ardından izleyen kişi · onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur · haberi veya işi yeniden dönüp araştırmak
  المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)
- **B009** aynı tür işi yeniden yapma — aynı tür işi yeniden yapma · atın bir koşudan sonra yeniden ve daha iyi koşması · bir otlak türünden ötekine dönüşümlü geçen deve sürüsü · kuşun yükselişiyle alçalışı arasındaki hareket evresi · ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü
  التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)
- **B010** bedel, satış başvurusu ve elde tutma güvencesi — tutsağın veya bir şeyin yerine alınan bedel · satılan maldan doğan başvuru hakkı ve sorumluluk · malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur
  أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)
- **B011** geride kalan son parça ya da iz — ağır hastalıktan kalan belirti · kapta kalan son yemek suyu · soyluluk ve güzellikten kişide kalan görünür iz
  العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)
- **B012** sarp dağ geçidi ve kayalık çıkıntı — dik ve zorlu dağ yolu veya geçidi · kuyu ya da dağ yüzündeki dışarı taşan kaya
  العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)
- **B013** kartal ve ona benzetilen büyük sancak — kartal, güçlü yırtıcı kuş · kartala benzetilen büyük sancak veya bayrak · korkunç ve ağır bela
  العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)
- **B014** özel adlandırma kümesi — erkek kişi adı · erkek keklik ve ona benzetilen at
  يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)
- **B015** bitkinin sararıp kurumaya yaklaşması [kalıp] — bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak
  عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)

## و ل ه (root_005296) — documented alternative for ٱللَّهَ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ش ق و (root_000808) — for شَآقُّوا۟ (w3): withheld observed target; not identity

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ن ش ق (root_001506) — for شَآقُّوا۟ (w3): withheld observed target; not identity

- **B001** bir bağa takılıp tutulma — tuzağa veya ipe takılıp kalmak · yavruların boynuna geçirilen bağ veya boyun bağı halkası · içinden kolayca çıkamayacağı bir işe düşmüş kişi · boyun bağının halkaları · onu ipe takıp tutmak · avının boynuna tuzak bağı geçen avcı · av paylaşımında boyun halkasına yakalanan pay
  أصل صحيح يدل على نشوب شيء (maqayis)؛ نشق الظبي في الحبالة علق فيها والنشقة حبل يجعل في أعناق البهم (maqayis)؛ رجل نشق إذا وقع في أمر لا يكاد يخلص منه (maqayis)؛ نشب الصيد في حبله ونشق وعلق وارتبق (tahdhib)؛ لحلق الربق نشق واحدها نشقة (tahdhib)
- **B002** burundan ilaç uygulama — ilacı veya burun ilacını buruna dökmek · burun deliklerine konup burundan alınan ilaç · burun ilacını buruna dökme · yakılmış pamuğu burna yaklaştırıp kokusunu içeri aldırmak · ilacı burundan almak · ilacı burundan içeri çekmek
  أنشقت الصبي الدواء صببته في أنفه (maqayis)؛ النشوق اسم لكل دواء ينشق (maqayis;tahdhib)؛ النشق صب سعوط في الأنف وأنشقته الدواء (ayn;tahdhib)؛ أنشقته قطنة محرقة أي أدنيتها من أنفه ليدخل ريحها في أنفه وخياشيمه (ayn;tahdhib)؛ النشوق سعوط يجعل في المنخرين (tahdhib)
- **B003** kokuyu burundan algılama [kalıp] — esintiyi veya kokuyu koklamak · koklaması hoş olmayan koku · birinden hoş bir koku almak
  استنشقت الريح تشممتها (maqayis;tahdhib)؛ ريح مكروهة النشق أي الشم (maqayis;ayn;tahdhib)؛ استنشقته أي تشممته (ayn)؛ نشقت من الرجل ريحا طيبة (tahdhib)
- **B004** suyu burnuna çekme [kalıp] — suyu burnuna çekip iç burun kanallarına ulaştırmak
  المتوضىء يستنشق الماء عند استنثاره (maqayis)؛ استنشقت الماء مددته بريح الأنف (ayn)؛ المتوضىء يستنشق إذا أبلغ الماء خياشيمه (tahdhib)
- **B005** umduğunu bulamayacağını söyleyerek geri çevirme — umduğunu bulamayacaksın diyerek isteğini geri çevirmek
  استنشق الريح فإنك لا تجد ما ترجو إذا أراد شيئا فخيبته (ayn)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:4, and ## Buluşmalar) =====
## Yarılan kaya, dağılan topluluk, yarılan toprak

Dördüncü ayet sürgünün sebebini söyler: {ar:ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ, tr:zâlike bi-ennehum şâkku'llâhe ve resûleh, gloss:bu, onların Allah'a ve Resulüne karşı ayrılığa düşmeleri yüzündendir, source:59:4}. Bu fiilin kökü yarmaktır: {ar:شققت الشيء أشقه شقا إذا صدعته, tr:şekaktu'ş-şey', gloss:bir şeyi çatlattığımda "yardım" denir, source:"ش ق ق,B001"}. Topluluk için de kullanılır: {ar:الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت, tr:eş-şikâk, gloss:şikâk ayrılıktır; topluluk çatlayıp dağıldığında olur, source:"ش ق ق,B004"}. Bu tanımdaki "çatlamak" fiili, yirmi birinci ayetteki dağın {ar:مُّتَصَدِّعًا, tr:mutesaddi'an, gloss:parçalanmış, çatlamış, source:59:21} haliyle aynı köktendir. Kökün bir dalı topluluğun dağılmasını da anlatır: {ar:تصدع القوم إذا تفرقوا, tr:tesadda'a'l-kavm, gloss:topluluk dağılınca "tesadda'a" denir, source:"ص د ع,B005"}. Böylece dördüncü ve yirmi birinci ayetler aynı kelime alanına girer. Allah'a karşı ayrılığa düşenlerin bu yarılması kendi içlerine döner. On dördüncü ayet şöyle der: {ar:بَأْسُهُم بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ, tr:be'suhum beynehum şedîd, tahsebuhum cemî'an ve kulûbuhum şettâ, gloss:kendi aralarındaki çekişmeleri şiddetlidir; onları toplu sanırsın, oysa kalpleri dağınıktır, source:59:14}. "Şettâ" kelimesi, kenetlenmenin kalkmasıdır: {ar:ارتفاع الالتئام بينهما, tr:irtifâ'u'l-iltiâm beynehumâ, gloss:ikisi arasındaki kaynaşmanın kalkması, source:"ش ت ت,B003"}. "Aralarında" kelimesi de hem bağı hem kopuşu taşır: {ar:البين الفراق, tr:el-beyn el-firâk, gloss:beyn ayrılıktır, source:"ب ي ن,B001"}. Aynı kelime bir yerde de "bağ" anlamındadır {source:"ب ي ن,B003"}. "Toplu" kelimesinin ailesinde ise "dağınık" kelimesiyle aynı ifadede geçen bir anlam vardır: {ar:جماع الناس أخلاطهم وهم الأشابة من قبائل شتى, tr:cimâ'u'n-nâs, gloss:insanların cimâı, dağınık kabilelerden gelmiş karışık kalabalıktır, source:"ج م ع,B002"}. Yani dışarıdan toplu görünen şey, içten derlenip toplanmış bir yığından ibarettir. Kur'an bu cezayı başka bir yerde açıkça sayar: {ar:أَوْ يَلْبِسَكُمْ شِيَعًا وَيُذِيقَ بَعْضَكُم بَأْسَ بَعْضٍ, tr:ev yelbisekum şiya'an ve yuzîka ba'dakum be'se ba'd, gloss:ya da sizi gruplara ayırıp kiminize kiminizin şiddetini tattırmaya, source:6:65}. Dağılanlar işlerini {ar:فَتَقَطَّعُوٓا۟ أَمْرَهُم بَيْنَهُمْ زُبُرًا, tr:fe-tekatta'û emrehum beynehum zuburâ, gloss:işlerini aralarında parça parça böldüler, source:23:53} de bölmüşlerdir. Dördüncü ayetin sözleri Bedir için de aynen söylenir {source:8:13}. Yüz çevirenler için başka bir yerde {ar:فَإِنَّمَا هُمْ فِى شِقَاقٍ, tr:fe-innemâ hum fî şikâk, gloss:onlar ancak bir ayrılık içindedir, source:2:137} denir. Toplu sanılan kalabalığın sonu da bellidir: {ar:سَيُهْزَمُ ٱلْجَمْعُ وَيُوَلُّونَ ٱلدُّبُرَ, tr:se-yuhzemu'l-cem'u ve yuvellûne'd-dubur, gloss:o topluluk bozguna uğrayacak ve arkalarını dönüp kaçacaklar, source:54:45}. Müminlere ise bunun tersi verilmiştir: {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًا, tr:fe-ellefe beyne kulûbikum fe-asbahtum bi-ni'metihî ihvânâ, gloss:kalplerinizi birleştirdi de onun nimetiyle kardeş oldunuz, source:3:103}. Bu birleştirme, malla yapılabilecek bir iş de değildir {source:8:63}. Onuncu ayetteki {ar:وَلِإِخْوَٰنِنَا, tr:ve li-ihvâninâ, gloss:ve kardeşlerimize, source:59:10} duası bunun içindir.

Yarılmanın bir de bereketli yüzü vardır. Dokuzuncu ayetin "kurtuluşa erenler" kelimesi, kökünde yarmaktır: {ar:أصل يدل على شق, tr:aslun yedullu 'alâ şakk, gloss:yarmayı gösteren kök, source:"ف ل ح,B001"}. Çiftçi de toprağı yardığı için bu kelimeyle anılır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan, gloss:toprağı yardığı için ırgata "fellâh" denildi, source:"ف ل ح,B003"}. "Kâfir" kelimesi ise tohumu toprakla örten ekici de demektir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfir ez-zâri', gloss:kâfir, tohumu toprakla örttüğü için ekicidir, source:"ك ف ر,B008"}. Toprağı yaran filiz de "sad'" kökündendir: {ar:الصدع النبات لأنه يصدع الأرض, tr:es-sad' en-nebât, gloss:toprağı yardığı için bitkiye sad' denir, source:"ص د ع,B003"}. Böylece surede iki tür yarılma vardır. Biri, Allah'tan ayrılığa düşüp kendi içinden dağılmaktır. Öbürü, toprağı yarıp örtülü tohumu filizlendiren yarılmadır. Kur'an bu ikinci yarılmayı açıkça anlatır: {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّا, tr:summe şekaknâ'l-arda şakkâ, gloss:sonra toprağı iyice yardık, source:80:26}. Sekizinci ayetteki muhacirlerin tarifi, başka bir surede bir ekin benzetmesine bağlanır. Peygamberin yanındakiler orada da {ar:يَبْتَغُونَ فَضْلًا مِّنَ ٱللَّهِ وَرِضْوَٰنًا, tr:yebteğûne fadlen mina'llâhi ve ridvânâ, gloss:Allah'tan lütuf ve rıza ararlar, source:48:29} diye anılır ve {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ, tr:ke-zer'in ahrace şat'eh, gloss:filizini çıkarmış bir ekin gibi, source:48:29} oldukları söylenir. Bu ekin {ar:يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ, tr:yu'cibu'z-zurrâ'a li-yeğîza bihimu'l-kuffâr, gloss:ekicileri hayran bırakır, onlarla kâfirleri öfkelendirir, source:48:29}. Burada "küffâr" kelimesi ekicilerin hemen yanında durur. Dünya hayatı da {ar:كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ, tr:ke-meseli ğaysin a'cebe'l-kuffâra nebâtuh, gloss:bitkisi ekicileri hayran bırakan bir yağmur gibidir, source:57:20} diye anlatılır. Bu ayette "küffâr" kelimesi ekiciler anlamına daha da yakındır.

Kaynaklar: 59:4 شَآقُّوا ش ق ق B001, B004; 59:21 مُّتَصَدِّعًا ص د ع B005, B003; 59:14 شَتَّىٰ ش ت ت B003; 59:14 بَيْنَهُمْ ب ي ن B001, B003; 59:14 جَمِيعًا ج م ع B002; 59:9 ٱلْمُفْلِحُونَ ف ل ح B001, B003; 59:2/11 كَفَرُوا ك ف ر B008

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

## Bağlar, köstekler, ipler

On dördüncü ayetteki "akıl" kelimesi, kale anlamının yanında deveyi bağlamak anlamını da taşır: {ar:عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط, tr:'akaltu'l-ba'îr, gloss:devenin ayağını ipiyle bağladım; ikâl bağdır, source:"ع ق ل,B002"}. Akıl etmeyen bir topluluk, bağı olmayan bir sürü gibidir. Kalpleri dağınık olanlar ip tutmaz. Dördüncü ve yedinci ayetlerdeki {ar:شَدِيدُ ٱلْعِقَابِ, tr:şedîdu'l-'ikâb, gloss:cezası çetin, source:59:4} ifadesi de bir bağlama işini taşır: {ar:عقبت الرمح شددته بالعقب, tr:'akabtu'r-rumh, gloss:mızrağı sinirle sıkıca bağladım, source:"ع ق ب,B001"}. "Şiddet" de düğümü sıkmaktır {source:"ش د د,B001"}. Bu ceza kaçana gevşemeyen bir sinir bağı gibi sarılır. Onuncu ve on birinci ayetlerdeki "kardeşler" kelimesi, hayvanın bağlandığı kazığı da adlandırır: {ar:الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة, tr:el-âhiyye, gloss:âhiyye, hayvanın bağlandığı kazıktır; aynı zamanda saygınlık ve ahittir, source:"ء خ و,B002"}. Sure iki tür kardeşlik gösterir. Onuncu ayette müminler {ar:رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا, tr:rabbena'ğfir lenâ ve li-ihvâninâ, gloss:Rabbimiz, bizi ve kardeşlerimizi bağışla, source:59:10} diye dua eder. On birinci ayette ise münafıklar {ar:يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟, tr:yekûlûne li-ihvânihimu'llezîne keferû, gloss:inkâr eden kardeşlerine diyorlar, source:59:11}. Birinci bağ kazığa sağlam bağlıdır, ikincisi kriz anında çözülür. Kur'an müminlere sağlam bir ip gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Bu ayette, on dördüncü ayetteki "toplu" kelimesi bir ipe bağlanmış olur. Kitap ehli için de iki ip anılır {source:3:112}. On altıncı ayetteki "Şeytan" kelimesi de ip ailesindendir: {ar:الشطن الحبل الطويل الشديد الفتل يستقى به, tr:eş-şatan el-hablu't-tavîl, gloss:şatan, su çekilen uzun, sıkı bükülmüş iptir, source:"ش ط ن,B002"}. Bu kökte ayrıca birini niyetinin yönünden saptırmak da vardır {source:"ش ط ن,B003"}. Şeytan uzun bir iple insanı derin bir kuyuya indirir, sonra ipi bırakır. Kendi sözüyle de, insanlar üzerinde bir gücü olmadığını, onları kurtaramayacağını söyler {source:14:22}. Onuncu ayetteki "ğıll" kelimesi, başka bir harekeyle, elleri boyna bağlayan demir halkadır: {ar:الغل مختص بما يقيد به فيجعل الأعضاء وسطه, tr:el-ğull, gloss:ğull, uzuvları ortasına alarak bağlayan bukağıdır, source:"غ ل ل,B006"}. On dördüncü ayetteki "toplu" kelimesi de aynı bukağıyı adlandırır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull, gloss:câmia bukağıdır, çünkü elleri boyuna birleştirir, source:"ج م ع,B008"}. Böylece kalpteki kin ile ellerdeki bukağı aynı kökten ses verir. Toplu sanılan kalabalık da birbirine bukağıyla bağlanmış olur. Kur'an bukağıyı da gösterir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu da bukağılayın, source:69:30}. Birinci ve yirmi dördüncü ayetlerdeki "Hakîm" ismi de, ailesinde atın çenesini saran gem halkasıdır {source:"ح ك م,B006"}. On birinci ayetteki "boyun eğmek" fiili de dizgine kolay uyan atı anlatır {source:"ط و ع,B001"}. Münafıklar "kimseye boyun eğmeyiz" derken, aslında gemsiz kalırlar.

Kaynaklar: 59:14 يَعْقِلُونَ ع ق ل B002; 59:4/7 شَدِيدُ ٱلْعِقَابِ ع ق ب B001, ش د د B001; 59:10/11 إِخْوَٰن ء خ و B002; 59:16 ٱلشَّيْطَٰنِ ش ط ن B002, B003; 59:10 غِلًّا غ ل ل B006; 59:14 جَمِيعًا ج م ع B008; 59:1/24 ٱلْحَكِيمُ ح ك م B006; 59:11 نُطِيعُ ط و ع B001

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

