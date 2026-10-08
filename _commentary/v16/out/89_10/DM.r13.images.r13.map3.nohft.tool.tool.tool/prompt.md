Focus: 89:10. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_10/D.r13/context.md =====
# 89:10 — focus

وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ

Anchor translation (canonical reading, reference only):

Kazıklar sahibi Firavun'a da.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَفِرْعَوْنَ | فِرْعَوْن |  | CONJ;PN |
| 2 | ذِى | ذُو |  | N |
| 3 | ٱلْأَوْتَادِ | أَوْتَاد | و ت د | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 89 — full text (context; no pericope)

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 ◀ focus وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_10/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ت د (root_001620) — identity root of ٱلْأَوْتَادِ (w3)

- **B001** kazık ve kazığı çakıp sabitleme — yere çakılan kazık · kazıklar; sabitleyici kazıklara benzetilen şeyler · kazığı çakıp sabitlemek · kazık gibi çakılmış ve sabitlenmiş · kazık çakma tokmağı · ses değişmesine uğramış kazık adı
  الوتد معروف (jamhara)؛ الوتد واحد الأوتاد؛ وتدت الوتد وتدا؛ تد وتدك بالميتدة (sihah)؛ يجمع الوتد أوتادا؛ الجبال أوتادا؛ تد الوتد يا واتد والوتد موتود؛ يقال للوتد وَدّ (tahdhib)؛ الوَتِد والوَتَد وقد وتدته؛ والجبال أوتادا؛ يصير وَدّا (mufradat)؛ كلمة واحدة وهي الوتد؛ وتده وتد وتدك (maqayis)؛ أما الوَدّ فالوتد (maqayis)
- **B002** kulaktaki kazıksı et çıkıntısı — kulağın ön bölümündeki küçük et çıkıntısı · kulaktaki kazıksı çıkıntı · iki kulaktaki kazıksı çıkıntılar
  الوتدة الهنية من اللحم في مقدم الأذن مما يلي الصدغ (jamhara)؛ الوتدان في الأذنين اللذان في باطنهما كأنهما وتد (sihah)؛ وتد الأذن هنية ناشزة في مقدمها (tahdhib)؛ الوتدان من الأذن تشبيها بالوتد للنتو فيهما (mufradat)؛ وتد الأذن الذي في باطنها كأنه وتد (maqayis)
- **B003** kazık gibi dimdik ve sabit durma — kazık gibi dimdik ve sabit · ayağını yere sağlamca sabitlemek
  وتد واتد؛ شبه الرجل بالجذل (sihah)؛ وتد واتد أي رأس منتصب؛ وتد فلان رجله في الأرض إذا ثبتها (tahdhib)
- **B004** erkeğin cinsel organının sertleşmesi [kalıp] — erkeğin cinsel organı sertleşti
  وتد الرجل أنعظ (sihah)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:10, and ## Buluşmalar) =====
## Kırbaç, kazık ve bağ

On üçüncü ayetteki ceza bir aletle sahnelenir: {ar:سَوْطَ عَذَابٍ, tr:savte azâb, gloss:azap kamçısı, source:89:13}. Kamçı örülmüş deriden yapılır: {ar:السوط الجلد المضفور الذي يضرب به, tr:es-savtu'l-cildu'l-madfûru'llezî yudrabu bih, gloss:savt, vurmak için örülmüş deridir, source:"س و ط,B002"}. Adı da derinin içine işlemesinden gelir: {ar:السوط لأنه يخالط الجلدة, tr:es-savtu li-ennehû yuhâlitu'l-cilde, gloss:kamçıya savt denir, çünkü deriye karışır, source:"س و ط,B001"}. Ayetteki ifade de bu karışmayla açıklanır: {ar:إشارة إلى ما خلط لهم من أنواع العذاب, tr:işâratun ilâ mâ hulita lehum min envâi'l-azâb, gloss:onlar için birbirine katılmış türlü azaplara işaret, source:"س و ط,B003"}. Tamlamanın ikinci kelimesi de kamçıya döner: {ar:عذبة السوط طرفه, tr:azebetu's-savti tarafuh, gloss:kamçının azebesi ucudur, source:"ع ذ ب,B006"}. Azabın aslı vurmaktır: {ar:أصل العذاب الضرب ثم استعير ذلك في كل شدة, tr:aslu'l-azâbi'd-darbu summe'stuîra zâlike fî kulli şidde, gloss:azabın aslı vurmaktır, sonra her şiddet için kullanılmıştır, source:"ع ذ ب,B005"}. "Azap kamçısı" tamlamasında iki kelime aynı şeyi iki uçtan söyler: biri örgülü deri, öteki onun vuran ucu. Fiil ise bu tabloya bir şey katar. Kamçı vurulur, dökülmez. Dökülen sudur. Fiil kamçıya bir sağanağın hacmini verir. Ortaya tek bir darbe değil, üstten inen bir kütle çıkar. Aynı fiil ayağı prangaya geçirmeyi de söyler: {ar:صب رجل فلان في القيد إذا قيد, tr:subbe riclu fulânin fi'l-kaydi izâ kuyyid, gloss:ayağı prangaya döküldü, yani bağlandı, source:"ص ب ب,B009"}.

Onuncu ayetteki kazıkların işi bir şeyi yere tutturmaktır: {ar:تد وتدك بالميتدة, tr:tid vetideke bi'l-mîtede, gloss:kazığını tokmakla çak, source:"و ت د,B001"}. Ayak için de {ar:وتد فلان رجله في الأرض إذا ثبتها, tr:vetede fulânun riclehû fi'l-ardı izâ sebbetehâ, gloss:ayağını yere çaktı, sabitledi, source:"و ت د,B003"} denir. Firavun kazık sahibidir, yani bir şeyi yere çakan, bağlayan ve tutan güç onda toplanmıştır. Kur'an onun azap iddiasını kendi ağzından aktarır. Musa'ya iman eden sihirbazlara şöyle der: {ar:وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ, tr:ve le-usallibennekum fî cuzûi'n-nahli ve le-ta'lemunne eyyunâ eşeddu azâben ve ebkâ, gloss:sizi hurma kütüklerine asacağım ve hangimizin azabının daha çetin ve daha kalıcı olduğunu bileceksiniz, source:20:71}.

Yirmi beşinci ve yirmi altıncı ayetler bu iddiaya cevap verir: {ar:فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:fe-yevmeizin lâ yuazzibu azâbehû ehad, gloss:o gün hiç kimse O'nun azabı gibi azap edemez, source:89:25}, {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:hiç kimse O'nun bağlaması gibi bağlayamaz, source:89:26}. Azap şiddetli acıdır: {ar:العذاب هو الإيجاع الشديد, tr:el-azâbu huve'l-îcâu'ş-şedîd, gloss:azap, şiddetli acı vermektir, source:"ع ذ ب,B005"}. Vesâk ise bağlamaya yarayan her şeydir: {ar:الوثاق: كل ما أوثقت به شيئا, tr:el-vesâk kullu mâ evsakte bihî şey'â, gloss:vesâk, bir şeyi bağladığın her şeydir, source:"و ث ق,B003"}. Bağlama da sağlamlaştırmaktır: {ar:وثقت الشيء: أحكمته, tr:vesiktu'ş-şey'e ahkemtuh, gloss:şeyi sağlamlaştırdım, source:"و ث ق,B002"}. Kur'an bu ipi savaş sahnesinde kullanır: {ar:فَشُدُّوا۟ ٱلْوَثَاقَ, tr:fe-şuddu'l-vesâk, gloss:bağı sıkı bağlayın, source:47:4}. Kıyamette ise ip zincire dönüşür. Kitabı sol eline verilen kişi için {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu, bağlayın, source:69:30} denir, sonra {ar:ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ, tr:summe fî silsiletin zer'uhâ seb'ûne zirâan feslukûh, gloss:sonra onu boyu yetmiş arşın olan bir zincire geçirin, source:69:32}. Sebebi de açıkça söylenir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmezdi, source:69:34}. Bu, surenin on sekizinci ayetinde kınanan şeyin ta kendisidir. Kur'an başka yerlerde de prangalar {ar:إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا, tr:inne ledeynâ enkâlen ve cahîmâ, gloss:bizim katımızda prangalar ve yakıcı bir ateş var, source:73:12}, birbirine zincirlenmiş suçlular {ar:مُّقَرَّنِينَ فِى ٱلْأَصْفَادِ, tr:mukarranîne fi'l-asfâd, gloss:zincirlere vurulmuş hâlde, source:14:49} ve boyunlardaki demir halkalar {source:40:71}, {source:76:4} anlatır. Surede kazık sahibinin yere çaktığı ayak, sonunda hiçbir insanın bağlayamayacağı bir bağla karşılanır.

Kaynaklar: 89:10 ٱلْأَوْتَادِ و ت د B001; 89:10 ٱلْأَوْتَادِ و ت د B003; 89:13 فَصَبَّ ص ب ب B009; 89:13 سَوْطَ س و ط B001; 89:13 سَوْطَ س و ط B002; 89:13 سَوْطَ س و ط B003; 89:13 عَذَابٍ ع ذ ب B005; 89:13 عَذَابٍ ع ذ ب B006; 89:25 يُعَذِّبُ عَذَابَهُۥٓ ع ذ ب B005; 89:26 يُوثِقُ وَثَاقَهُۥٓ و ث ق B002; 89:26 وَثَاقَهُۥٓ و ث ق B003

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

