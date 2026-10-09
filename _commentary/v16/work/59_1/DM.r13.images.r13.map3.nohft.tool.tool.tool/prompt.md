Focus: 59:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/59_1/D.r13/context.md =====
# 59:1 — focus

سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | سَبَّحَ | سَبَّحَ | س ب ح | V |
| 2 | لِلَّهِ | ٱللَّه | ء ل ه | P;PN |
| 3 | مَا | مَا |  | REL |
| 4 | فِى | فِى |  | P |
| 5 | ٱلسَّمَٰوَٰتِ | سَمَآء | س م و | DET;N |
| 6 | وَمَا | مَا |  | CONJ;REL |
| 7 | فِى | فِى |  | P |
| 8 | ٱلْأَرْضِ | أَرْض | ء ر ض | DET;N |
| 9 | وَهُوَ |  |  | REM;PRON |
| 10 | ٱلْعَزِيزُ | عَزِيز | ع ز ز | DET;N |
| 11 | ٱلْحَكِيمُ | حَكِيم | ح ك م | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 59 — full text (context; no pericope)

- 59:1 ◀ focus سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
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
- 59:23 هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- 59:24 هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/work/59_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ب ح (root_000666) — identity root of سَبَّحَ (w1)

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

## ء ل ه (root_000047) — identity root of لِلَّهِ (w2)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## س م و (root_000745) — identity root of ٱلسَّمَٰوَٰتِ (w5)

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ء ر ض (root_000025) — identity root of ٱلْأَرْضِ (w8)

- **B001** yer ve yere bakan alt bölüm — yer, yeryüzü · yerler, ülkeler · bir şeyin yere bakan altı · hayvanın tırnağı veya ayaklarının altı
  كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)
- **B002** yumuşak ve verimli toprak — yumuşak, verimli ve bol bitkili toprak · yumuşak tabanlı geniş çayırlık · toprak verimlileşti · bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi · toprakta kök salmış fidan · oğlak yer bitkisini yedi veya onunla semirdi
  أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)
- **B003** iyiliğe yatkın ve layık [kalıp] — iyiliğe yatkın, layık ve alçak gönüllü kişi · bunu yapmaya en uygunları
  رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)
- **B004** yabancı kimse — yabancı kimse
  فلان ابن أرض أي غريب (maqayis)
- **B005** kalın yün veya kıl yaygı — kalın yün veya kıl yaygı
  الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)
- **B006** yere çökercesine ağırlaşıp oyalanmak — yere bağlı kalmak, ağırlaşıp oyalanmak
  تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)
- **B007** karşısına çıkıp kendini ortaya koymak — birinin karşısına çıkıp kendini ortaya koymak
  جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)
- **B008** titreme veya ürperme — insanı tutan titreme veya ürperme · titreme ve sarsılma
  الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)
- **B009** soğuk algınlığı — soğuk algınlığı · soğuk algınlığına yakalanmış · soğuk algınlığına uğratmak
  الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)
- **B010** odun yiyen küçük canlı — odun yiyen küçük canlı · odunu bu canlı yedi ve zarar verdi
  الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)
- **B011** yaranın irinlenip bozulması [kalıp] — yara irinlenip kabardı ve bozuldu
  أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)
- **B012** doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu — görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi
  المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)

## ع ز ز (root_001008) — identity root of ٱلْعَزِيزُ (w10)

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

## ح ك م (root_000348) — identity root of ٱلْحَكِيمُ (w11)

- **B001** alıkoyup geri çevirmek — haksızlıktan veya bozulmadan alıkoyup geri çevirmek · sorumsuz kişinin elini tutup zarar vermesini önlemek · yetimi bozulmadan koruyup durumunu düzeltmek · birini yapmak istediği şeyden alıkoymak
  الحكم وهو المنع من الظلم (maqayis)؛ كل شيء منعته من الفساد فقد حكمته وحكمته وأحكمته (ayn)؛ حكمت السفيه وأحكمته إذا أخذت على يده (sihah)؛ كل من منعته من شيء فقد حكمته وأحكمته (tahdhib)؛ حكم أصله منع منعا لإصلاح (mufradat)
- **B002** uyuşmazlığı bağlayıcı kararla sonuçlandırmak — insanlar arasında doğru ölçüyle karar vermek · biri lehine veya aleyhine karar vermek · karar verme veya işi karara bağlama · insanlar arasında karar veren kişi · karar verme işiyle özellikle görevli kişi · çekişmede verilen karar veya yaralanma karşılığını belirleme · çekişmeyi karar verecek bir mercie götürmek
  الحكم وهو المنع من الظلم (maqayis)؛ حاكمناه إلى الله دعوناه إلى حكم الله (ayn)؛ الحكم مصدر قولك حكم بينهم أي قضى (sihah)؛ الحكم أيضا القضاء بالعدل (tahdhib)؛ الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا (mufradat)
- **B003** bilgi ve usla doğruyu bulma yetkinliği — bilgi ve kavrayış ya da doğru bir önerme · bilgi ve usla doğruyu bulma yetkinliği · bilgili, deneyimli ve doğruyu bulan kişi · deneyimle olgunlaşmış bilge yaşlı
  الحكمة تمنع من الجهل (maqayis)؛ الحكمة مرجعها إلى العدل والعلم والحلم (ayn)؛ الحكمة من العلم والحكيم العالم وصاحب الحكمة (sihah)؛ الحكم العلم والفقه (tahdhib)؛ الحكمة إصابة الحق بالعلم والعقل (mufradat)
- **B004** sağlam ve kusursuz duruma getirmek — bir şeyi sağlamlaştırmak veya sağlam duruma gelmek · kusur ve kuşkuya yer bırakmayacak biçimde sağlamlaştırılmış · işleri sağlam ve kusursuz yapan · övgüye değer niteliğinde doruğa varmak · kendisine zarar verecek şeylerden bütünüyle uzaklaşmak
  استحكم الأمر وثق (ayn)؛ أحكمت الشيء فاستحكم أي صار محكما (sihah)؛ آياته أحكمت وفصلت (tahdhib)؛ المحكم ما لا يعرض فيه شبهة (mufradat)؛ حكم الرجل إذا بلغ النهاية في معناه (tahdhib)
- **B005** karar verme yetkisini başkasına bırakmak — bir işte karar verme yetkisini ona bırakmak · malı üzerinde uygun gördüğü gibi davranabilmek · yetim malını yönetmeye elverişli duruma geldiğinde malı üzerinde tasarruf etmesine izin vermek · birinin elini istediğini yapmakta serbest bırakmak
  حكم فلان في كذا إذا جعل أمره إليه (maqayis)؛ احتكم في ماله إذا جاز فيه حكمه (ayn)؛ حكمته في مالي إذا جعلت إليه الحكم فيه (sihah)؛ حكمنا فلانا بيننا أي أجزنا حكمه بيننا (tahdhib)؛ الحكمين أن يتوليا الحكم عليهم ولهم حسب ما يستصوبانه (mufradat)
- **B006** gemin çene çevresini kuşatan kısıtlayıcı parçası — gemin hayvanın çene çevresini kuşatıp koşmasını sınırlayan parçası · hayvana gem takmak veya onu gemle durdurmak · koyunun çenesi · başında gemin kısıtlayıcı parçası bulunan at
  حكمة الدابة لأنها تمنعها (maqayis)؛ حكمة اللجام ما أحاط بحنكيه (ayn)؛ حكمة اللجام ما أحاط بالحنك (sihah)؛ حكمة اللجام ما أحاط بحنكيه (tahdhib)؛ سميت اللجام حكمة الدابة (mufradat)
- **B007** bir şeyden geri dönmek veya birini döndürmek — bir şeyden geri dönmek · birini bir şeyden geri döndürmek
  حكم فلان عن الشيء أي رجع؛ وأحكمته أنا أي رجعته (tahdhib)

## و ل ه (root_005296) — documented alternative for لِلَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO و س م (root_001650) — for ٱلسَّمَٰوَٰتِ (w5): withheld observed target; not identity

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

===== _commentary/v16/out/s059/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 59:1, and ## Buluşmalar) =====
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

## Bağlar, köstekler, ipler

On dördüncü ayetteki "akıl" kelimesi, kale anlamının yanında deveyi bağlamak anlamını da taşır: {ar:عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط, tr:'akaltu'l-ba'îr, gloss:devenin ayağını ipiyle bağladım; ikâl bağdır, source:"ع ق ل,B002"}. Akıl etmeyen bir topluluk, bağı olmayan bir sürü gibidir. Kalpleri dağınık olanlar ip tutmaz. Dördüncü ve yedinci ayetlerdeki {ar:شَدِيدُ ٱلْعِقَابِ, tr:şedîdu'l-'ikâb, gloss:cezası çetin, source:59:4} ifadesi de bir bağlama işini taşır: {ar:عقبت الرمح شددته بالعقب, tr:'akabtu'r-rumh, gloss:mızrağı sinirle sıkıca bağladım, source:"ع ق ب,B001"}. "Şiddet" de düğümü sıkmaktır {source:"ش د د,B001"}. Bu ceza kaçana gevşemeyen bir sinir bağı gibi sarılır. Onuncu ve on birinci ayetlerdeki "kardeşler" kelimesi, hayvanın bağlandığı kazığı da adlandırır: {ar:الآخية واحدة الأواخي؛ تشد إليه الدابة؛ الآخية أيضا الحرمة والذمة, tr:el-âhiyye, gloss:âhiyye, hayvanın bağlandığı kazıktır; aynı zamanda saygınlık ve ahittir, source:"ء خ و,B002"}. Sure iki tür kardeşlik gösterir. Onuncu ayette müminler {ar:رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا, tr:rabbena'ğfir lenâ ve li-ihvâninâ, gloss:Rabbimiz, bizi ve kardeşlerimizi bağışla, source:59:10} diye dua eder. On birinci ayette ise münafıklar {ar:يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟, tr:yekûlûne li-ihvânihimu'llezîne keferû, gloss:inkâr eden kardeşlerine diyorlar, source:59:11}. Birinci bağ kazığa sağlam bağlıdır, ikincisi kriz anında çözülür. Kur'an müminlere sağlam bir ip gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Bu ayette, on dördüncü ayetteki "toplu" kelimesi bir ipe bağlanmış olur. Kitap ehli için de iki ip anılır {source:3:112}. On altıncı ayetteki "Şeytan" kelimesi de ip ailesindendir: {ar:الشطن الحبل الطويل الشديد الفتل يستقى به, tr:eş-şatan el-hablu't-tavîl, gloss:şatan, su çekilen uzun, sıkı bükülmüş iptir, source:"ش ط ن,B002"}. Bu kökte ayrıca birini niyetinin yönünden saptırmak da vardır {source:"ش ط ن,B003"}. Şeytan uzun bir iple insanı derin bir kuyuya indirir, sonra ipi bırakır. Kendi sözüyle de, insanlar üzerinde bir gücü olmadığını, onları kurtaramayacağını söyler {source:14:22}. Onuncu ayetteki "ğıll" kelimesi, başka bir harekeyle, elleri boyna bağlayan demir halkadır: {ar:الغل مختص بما يقيد به فيجعل الأعضاء وسطه, tr:el-ğull, gloss:ğull, uzuvları ortasına alarak bağlayan bukağıdır, source:"غ ل ل,B006"}. On dördüncü ayetteki "toplu" kelimesi de aynı bukağıyı adlandırır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull, gloss:câmia bukağıdır, çünkü elleri boyuna birleştirir, source:"ج م ع,B008"}. Böylece kalpteki kin ile ellerdeki bukağı aynı kökten ses verir. Toplu sanılan kalabalık da birbirine bukağıyla bağlanmış olur. Kur'an bukağıyı da gösterir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu da bukağılayın, source:69:30}. Birinci ve yirmi dördüncü ayetlerdeki "Hakîm" ismi de, ailesinde atın çenesini saran gem halkasıdır {source:"ح ك م,B006"}. On birinci ayetteki "boyun eğmek" fiili de dizgine kolay uyan atı anlatır {source:"ط و ع,B001"}. Münafıklar "kimseye boyun eğmeyiz" derken, aslında gemsiz kalırlar.

Kaynaklar: 59:14 يَعْقِلُونَ ع ق ل B002; 59:4/7 شَدِيدُ ٱلْعِقَابِ ع ق ب B001, ش د د B001; 59:10/11 إِخْوَٰن ء خ و B002; 59:16 ٱلشَّيْطَٰنِ ش ط ن B002, B003; 59:10 غِلًّا غ ل ل B006; 59:14 جَمِيعًا ج م ع B008; 59:1/24 ٱلْحَكِيمُ ح ك م B006; 59:11 نُطِيعُ ط و ع B001

## Yüzen yaratılış

Sure, tesbih ile başlar ve biter: {ar:سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ, tr:sebbaha li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard, gloss:göklerde ve yerde ne varsa Allah'ı tesbih etti, source:59:1} ve {ar:يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:yusebbihu lehû mâ fi's-semâvâti ve'l-ard, gloss:göklerde ve yerde ne varsa O'nu tesbih eder, source:59:24}. Tesbih kelimesinin kökü suda ve havada hızla geçmektir: {ar:السبح المر السريع في الماء وفي الهواء, tr:es-sebh el-merru's-serî' fi'l-mâ'i ve fi'l-hevâ', gloss:sebh, suda ve havada hızla geçmektir, source:"س ب ح,B004"}. Yıldızlar da yörüngelerinde yüzer {source:"س ب ح,B004"}. Kur'an bunu açıkça söyler: {ar:وَكُلٌّ فِى فَلَكٍ يَسْبَحُونَ, tr:ve kullun fî felekin yesbehûn, gloss:hepsi bir yörüngede yüzer, source:36:40}. Kanatlarını açmış kuşlar da her biri kendi tesbihini bilerek havada yüzer {source:24:41}. Bu tabloda tesbih, yaratılmış her şeyin kendi yörüngesinde, kendisine verilen akışa uyarak hareket etmesidir. Surenin ortasında yaşananlar, yani kalelere güvenmek, iki kapılı yuvadan kaçmak, sözünde durmamak, bu akıştan sapmaktır. Göklerdeki ve yerdeki her şey yüzer, bir tek bunlar akıntıya karşı direnir. Bu akışın insanlar tarafından anlaşılmadığı da söylenir: {ar:وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:ve lâkin lâ tefkahûne tesbîhahum, gloss:fakat siz onların tesbihini anlamazsınız, source:17:44}. On üçüncü ayetteki "anlamayan topluluk" ifadesi bunun yanında durur. Tesbih kökü atlar için de kullanılır: {ar:السابح من الخيل يمد يديه في الجري, tr:es-sâbih mine'l-hayl, gloss:sâbih, koşarken ön ayaklarını uzatan attır, source:"س ب ح,B004"}. Altıncı ayette müminlerin koşturmadığı atlar, böylece surenin başındaki tesbihin karşısına konur. Hücum eden atlar da yeminle anılır: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-'âdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}. Onların ardından kıvılcım çakanlar gelir {source:100:2}. Yüzenlerle yemin edilen bir ayet de vardır {source:79:3}.

Kaynaklar: 59:1/23/24 سَبَّحَ / سُبْحَٰنَ / يُسَبِّحُ س ب ح B004

## Buluşmalar

İmgeler en sık ikinci ayette buluşur. Aynı cümle hem bir kuşatmayı hem de başka yerden gelen bir seli anlatır: {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fe-etâhumu'llâhu min haysu lem yahtesibû, gloss:Allah onlara hesaba katmadıkları yerden geldi, source:59:2}. "Gelmek" fiili hem gece baskınını hem de başka yerde yağmış bir yağmurun selini taşır. "Hesaba katmamak" fiili hem küçük okları hem de doluyu anlatır {source:"ح س ب,B007"}. Kalbe atılan korku, mancınıkla atılan bir taş gibidir ve vadiyi dolduran bir sel gibi kalbi doldurur. Kale ise içeriden, sahiplerinin kendi elleriyle delinir. Kale ile in de bu ayette karşılaşır. Nadîr kalelerinde, münafıklar iki kapılı yuvalarında sığınak arar. İkisi de aynı iki fiille yıkılır: "geldi" ve "çıkardı". Gizli kapıdan kaçan münafık, kuşatılmış kaleyi yalnız bırakır. On birinci ve on ikinci ayetlerde "çıkmak" fiili aynı anda yuvanın kaçış kapısını, yağmayan bir bulutu ve yarıda kalan bir hücumu anlatır.

On dördüncü ayet ikinci bir buluşma yeridir. Tahkimli kasabalar, duvarlar, akıl etmeyen bir topluluk ve dağınık kalpler aynı ayette durur. "Akıl" hem bir sığınak hem de deveyi bağlayan iptir. Bu topluluğun ne iç kalesi ne de onu bir arada tutan bir bağı vardır. Toplu görünürler, ama ancak bir bukağıyla bir arada durabilirler. "Ardından" kelimesi aynı ayette hem duvarın arkasını, hem gizlemeyi, hem de yakılmamış çakmağı anlatır.

Dokuzuncu ayet, bu tabloların hepsinde karşı tarafı tutar. Kalenin karşısında aralıklı kamış kulübe, yağmayan bulutun karşısında kanana kadar su içme, ateş vermeyen çakmağın karşısında açık el, gizli kapının karşısında hazırlanmış konak durur. Cimrilik, engelleyen kaleyle, ateş vermeyen çakmakla ve kapışmayla aynı köktendir. Ondan korunan ise toprağı yararak kurtuluşa erer. Dokuzuncu ayette nefis ve göğüs aynı zamanda sabahın nefes alması ve sudan kanmış dönüştür.

Yirmi birinci ayette sure kendi imgelerini Kur'an'a çevirir. Nadîr'in kalesi, içine atılan korkuyla kendi elleriyle delinir. Dağ ise üzerine inen söz karşısında, bu kez saygıdan, aşağı iner ve yarılır. Gedik ile çatlak, iki katı yapının iki farklı cevabıdır. Bunlardan biri yıkım, öbürü filizlenmedir. "Hâşi'" kelimesi bu iki sahneyi birleştirir, çünkü ailesinde hem çökmüş duvarı hem de yağmur bekleyen kuru toprağı anlatır: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çökmüş duvar, source:"خ ش ع,B002"}. Yağmur sahnesi de bu ayette tamamlanır. İkinci ayette yağmuru başka yerde yağıp sel olarak gelen su, yedinci ayette yoksulların havuzlarına yönlendirilir. Yirmi birinci ayette ise gökten inen söz dağa yağar. Su, aynı kelimelerle hem boğar, hem paylaşılır, hem de diriltir. Sure, birinci ayette göklerde ve yerde yüzen her şeyle başlar, ayetler boyunca bu akıştan sapanların kalelerini, yuvalarını ve vaatlerini çökertir, yirmi dördüncü ayette yine aynı tesbihle kapanır. Başta ve sonda söylenen "Azîz" ve "Hakîm" isimleri, aradaki bütün sahnelerde gerçek dokunulmazlığın ve doğru yere yönlendirilen tutmanın kime ait olduğunu söyler.

