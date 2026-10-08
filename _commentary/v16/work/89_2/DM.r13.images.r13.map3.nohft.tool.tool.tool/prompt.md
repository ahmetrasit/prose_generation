Focus: 89:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_2/D.r13/context.md =====
# 89:2 — focus

وَلَيَالٍ عَشْرٍۢ

Anchor translation (canonical reading, reference only):

On geceye andolsun!

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَلَيَالٍ | لَيْل | ل ي ل | CONJ;N |
| 2 | عَشْرٍ | عَشْر | ع ش ر | ADJ |


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
- 89:2 ◀ focus وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
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


===== _commentary/v16/work/89_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ل ي ل (root_001392) — identity root of وَلَيَالٍ (w1)

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ع ش ر (root_001016) — identity root of عَشْرٍ (w2)

- **B001** on ve yirmi sayı adları — eril adlarla kullanılan on sayısı · dişil adlarla kullanılan on sayısı · yirmi sayısı · on bir sayısı
  العشرة والعشر في المؤنث (maqayis); العشر عدد المؤنث والعشرة عدد المذكر (ayn;tahdhib); عشرة رجال وعشر نسوة (sihah); العشرة والعشر والعشرون معروفة (mufradat)
- **B002** dokuzu ona tamamlama — dokuz kişiyi ona tamamlayan onuncu kişi · bir topluluğun onuncu kişisi olmak · dokuz kişiyi veya şeyi bir ekleyerek ona tamamlamak
  عشرت القوم إذا صرت عاشرهم (maqayis;ayn;tahdhib); كانوا تسعة فتموا بي عشرة (maqayis;ayn); أعشر القوم صاروا عشرة (sihah); عشرتهم صيرت مالهم عشرة (mufradat)
- **B003** onda bir — onda bir · onda bir · bir şeyin onda biri
  العشر جزء من الأجزاء العشرة وهو العشير والمعشار (maqayis); العشر جزء من عشرة أجزاء وهو العشير والمعشار (ayn); معشار الشيء عشره (sihah;mufradat); العشير والعشر واحد (tahdhib)
- **B004** maldan onda bir alma — mallarının onda birini almak · mallardan onda bir alan görevli
  عشرت القوم إذا أخذت عشر أموالهم (maqayis); عشرتهم تعشيرا أخذت العشر من أموالهم (ayn); إذا أخذت منهم عشر أموالهم ومنه العاشر والعشار (sihah); عشرت أموالهم إذا أخذت منهم العشر (tahdhib); عشرهم أخذ عشر مالهم (mufradat)
- **B005** onar onar gelme — onar onar · onar onar
  جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة (maqayis;ayn;tahdhib); عشار بالضم معدول من عشرة (sihah); جاءوا عشارى عشرة عشرة (mufradat)
- **B006** develerin onuncu gün sulanması — develerin onuncu gün suya gelmesi veya iki sulama arası · her on günde bir suya gelen develer
  العشر ورد الإبل يوم العاشر (maqayis;ayn;tahdhib); العشر بالكسر ما بين الوردين (sihah); العشر في الإظماء وإبل عواشر (mufradat)
- **B007** gebeliği on aya ulaşmış deve — gebeliği on aya ulaşmış deve · gebeliği on aya ulaşmış veya doğumu yaklaşmış develer
  ناقة عشراء وهي التي أقربت سميت عشراء لتمام عشرة أشهر لحملها (maqayis); الناقة التي أتت عليها عشرة أشهر (sihah); إذا بلغت الناقة في حملها عشرة أشهر فهي عشراء (tahdhib); ناقة عشراء مرت من حملها عشرة أشهر وجمعها عشار (mufradat); الظباء الحديثات العهد بالنتاج (tahdhib)
- **B008** eşeğin on kez yinelenen anırması — çok ve art arda anıran eşek · eşeğin on kez anırması
  المعشر الحمار الشديد النهيق (maqayis;ayn;tahdhib); تعشير الحمار نهيقه عشرة أصوات (sihah); التعشير نهاق الحمير لكونه عشرة أصوات (mufradat)
- **B009** parçalara, paylara veya dağınık kümelere ayrılma — kırık parçalar veya bölüşülmüş paylar · parça parça kırılmış çömlek · herhangi bir şeyden ayrılmış parça · her yana dağılmış topluluklar
  العشر القطعة تنكسر من القدح أو البرمة (maqayis); برمة أعشار إذا انكسرت قطعا قطعا (sihah;tahdhib); أعشار الجزور الأنصباء (sihah); قدح أعشار منكسر (mufradat); العشارة القطعة من كل شيء (tahdhib); ذهب القوم عشاريات متفرقين في كل وجه (tahdhib)
- **B010** on arşın uzunluğunda olan şey — on arşın uzunluğunda olan şey
  العشاري ما بلغ طوله عشر أذرع (maqayis); العشارى ما يقع طوله عشرة أذرع (sihah); العشاري ما طوله عشرة أذرع (mufradat)
- **B011** Muharrem ayının onuncu günü — Muharrem ayının onuncu günü · Muharrem ayının onuncu günü
  عاشوراء اليوم العاشر من المحرم (maqayis); يوم عاشوراء وعشوراء أيضا (sihah); يوم عاشوراء هو اليوم العاشر من المحرم (tahdhib)
- **B012** yakın ilişki ve birlikte yaşama — birlikte yaşama ve yakın ilişki · yakın ilişki içinde birlikte yaşama · yakın ilişki kurulan kimse veya eş
  المخالطة والمداخلة فالعشرة والمعاشرة وعشيرك الذي يعاشرك (maqayis); المعاشرة المخالطة وكذلك التعاشر (sihah); العشير الزوج سمي عشيرا لأنه يعاشرها وتعاشره (tahdhib); عاشرته صرت له كعشرة في المصاهرة والعشير المعاشر (mufradat)
- **B013** akraba topluluğu veya ortak amaçlı topluluk — kişinin ailesi, yakın akrabaları veya kabilesi · ortak bir işte birleşen topluluk
  عشيرة الرجل لمعاشرة بعضهم بعضا (maqayis); المعشر كل جماعة أمرهم واحد (maqayis;tahdhib); العشيرة القبيلة (sihah); العشيرة أهل الرجل الذين يتكثر بهم (mufradat)
- **B014** tatlı özsulu iri bir ağaç — tatlı özsuyu olan iri ağaç veya bitki
  العشر نبت (maqayis); العشر شجر له صمغ (sihah); العشر من كبار الشجر وله صمغ حلو (tahdhib)
- **B015** her on ayeti gösteren işaretleme — kutsal metin nüshasında her on ayete işaret koyma · kutsal metin nüshasında her on ayeti gösteren işaretler
  تعشير المصاحف جعل العواشر فيها (sihah); العاشرة حلقة التعشير من عواشر المصحف (tahdhib); العشور في المصاحف علامة العشر الآيات (mufradat)
- **B016** dokuzlu gecelerden sonraki üç gece — ayın dokuzlu gecelerinden sonraki üç gece
  يقال أيضا لثلاث ليال من ليالى الشهر عشر وهي بعد التسع (sihah); كان أبو عبيدة يبطل التسع والعشر إلا أشياء منه معروفة (sihah)
- **B017** kuşun öndeki uçuş telekleri — kuşun öndeki uçuş telekleri
  الأعشار قوادم ريش الطائر (sihah)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:2, and ## Buluşmalar) =====
## Gece örtüsü ve onu yaran şafak

Sure bir yarılmayla açılır: {ar:وَٱلْفَجْرِ, tr:ve'l-fecr, gloss:şafağa andolsun, source:89:1}. Arapçada fecr, karanlığın sabahtan ayrılıp açılmasıdır: {ar:الفجر انفجار الظلمة عن الصبح, tr:el-fecru'nficâru'z-zulmeti ani's-subh, gloss:fecr, karanlığın sabahtan yarılıp açılmasıdır, source:"ف ج ر,B002"}. Sabaha bu adın verilmesi de geceyi yarmasındandır: {ar:قيل للصبح فجر لكونه فجر الليل, tr:kîle li's-subhi fecrun li-kevnihî fecera'l-leyl, gloss:sabaha fecr denmesi geceyi yarmasındandır, source:"ف ج ر,B002"}. Sahnede gece her şeyin üstüne serilmiş bir örtüdür. Şafak bu örtüyü bir anda kaldırmaz, ufkun bir noktasından yırtar ve ışık o yarıktan sızar. Kelimenin ayetteki anlamı şafaktır. Aynı kökten gelen imgeler bu anlamın yanında duyulur, onun yerine geçmez. Aşağıdaki bütün imgeler de bu ölçüyle okunur.

Gecenin örtüsü Arapçada ayrı bir kökün işidir: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyli sevâduhû ve setruhu'l-eşyâ', gloss:gecenin cenânı, karanlığı ve şeyleri örtmesidir, source:"ج ن ن,B002"}. Kur'an bu fiili İbrahim'in sahnesinde kullanır. Gece onu örtünce bir yıldız görür ve "Bu Rabbimdir" der. Yıldız batınca batanları sevmediğini söyler: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا, tr:fe-lemmâ cenne aleyhi'l-leylu raâ kevkebâ, gloss:gece onu örtünce bir yıldız gördü, source:6:76}. Burada örtü görmeyi engellemez. Tersine, karanlığın içinde batanla batmayanı ayırmayı mümkün kılar.

İkinci ayet geceleri sayar: {ar:وَلَيَالٍ عَشْرٍۢ, tr:ve leyâlin aşr, gloss:ve on geceye, source:89:2}. Gece burada tek bir örtü değildir, birbirini izleyen karanlıklardır: {ar:ظلام الليل, tr:zalâmu'l-leyl, gloss:gecenin karanlığı, source:"ل ي ل,B001"}. Dördüncü ayet geceyi hareket hâlinde gösterir: {ar:وَٱلَّيْلِ إِذَا يَسْرِ, tr:ve'l-leyli izâ yesr, gloss:yürüyüp gittiğinde geceye, source:89:4}. Fiil gece yolculuğunu anlatır: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:surâ, gece yürüyüşüdür, source:"س ر ي,B001"}. Aynı harfler bir şeyin üstündeki örtüyü kaldırmayı da adlandırır: {ar:السرو كشف الشيء عن الشيء, tr:es-servu keşfu'ş-şey'i ani'ş-şey', gloss:bir şeyi başka bir şeyin üstünden açmak, source:"س ر ي,B004"}. Bir örnek: {ar:انسرى عني الهم انكشف, tr:insarâ anni'l-hemmu'nkeşef, gloss:tasa üzerimden kalktı, açıldı, source:"س ر ي,B004"}. Gece yürüdükçe gider, gittikçe altında kalanı açık bırakır. Örtü iki yolla kalkar: yırtılarak, ki bu fecrdir, ve kayarak, ki bu seryidir. Surenin ilk dört ayeti bu iki hareketi aynı gecenin iki ucuna yerleştirir.

Kur'an aynı ikiliyi başka yeminlerde de kurar. Tekvîr suresinde gece kararır ve sabah nefes alır: {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararıp çekildiğinde geceye, source:81:17}, {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha, source:81:18}. Müddessir suresinde gece arkasını döner ve sabah ağarır: {ar:وَٱلَّيْلِ إِذْ أَدْبَرَ, tr:ve'l-leyli iz edber, gloss:arkasını döndüğünde geceye, source:74:33}, {ar:وَٱلصُّبْحِ إِذَآ أَسْفَرَ, tr:ve's-subhi izâ esfer, gloss:ağardığında sabaha, source:74:34}. Leyl suresi ise geceye tam örttüğü anda yemin eder: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye, source:92:1}. Yarma işini Kur'an Allah'a da verir, ama başka bir kökle: {ar:فَالِقُ ٱلْإِصْبَاحِ, tr:fâliku'l-ısbâh, gloss:sabahı yarıp çıkaran, source:6:96}. Aynı kök Felak suresindeki sığınma sözünde de geçer {source:113:1}. Kökler ayrıdır ama mekanizma aynıdır: karanlık bir kabuk gibi çatlar. Oruç hükmü yarığın ne kadar ince olduğunu gösterir. Beyaz iplik siyah iplikten şafakta ayrılır: {ar:ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ, tr:el-haytu'l-ebyadu mine'l-hayti'l-esvedi mine'l-fecr, gloss:şafaktan beyaz iplik siyah iplikten, source:2:187}. Demek ki şafak bir alan değil, bir çizgidir. Kadir gecesi de bu çizgiye kadar sürer: {ar:سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ, tr:selâmun hiye hattâ matla'i'l-fecr, gloss:o, şafağın doğuşuna kadar esenliktir, source:97:5}.

Yarılmanın ters yüzü de aynı köktedir. Ahlâki yırtıklık anlamındaki fücur şöyle tarif edilir: {ar:الفجور شق ستر الديانة, tr:el-fucûru şakku sitri'd-diyâne, gloss:fücur, din örtüsünü yırtmaktır, source:"ف ج ر,B004"}. Şafak karanlığı yırtınca ışık gelir. İnsan dinin örtüsünü yırtınca açılan şey ışık değildir. Surenin ilk kelimesi bu iki yarılmayı birlikte taşır. On birinci ve on ikinci ayetlerde sınırı aşan kavimler anlatılırken ikinci yön duyulur.

Beşinci ayet yeminin kime söylendiğini sorar: {ar:هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ, tr:hel fî zâlike kasemun li-zî hicr, gloss:bunda akıl sahibi için bir yemin var mı, source:89:5}. Hicr kökü bir duvarın işini anlatır: {ar:المنع والإحاطة, tr:el-men'u ve'l-ihâta, gloss:alıkoymak ve çevrelemek, source:"ح ج ر,B001"}. Akla bu adın verilmesi de bundandır: {ar:العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي, tr:el-aklu yusemmâ hicran li-ennehû yemne'u min ityâni mâ lâ yenbeğî, gloss:akla hicr denir, çünkü yakışmayanı yapmaktan alıkoyar, source:"ح ج ر,B002"}. Örtüyü yırtan şafak, içinde bir duvar taşıyan birine seslenir. Akıl, insanı dışarı taşmaktan tutan iç duvardır. Kur'an aynı kelimeyi kıyamet gününün duvarı olarak da kullanır. Meleklerin görüldüğü gün suçlulara müjde yoktur ve o gün {ar:وَيَقُولُونَ حِجْرًۭا مَّحْجُورًۭا, tr:ve yekûlûne hicran mahcûrâ, gloss:ve "aşılmaz bir engel" derler, source:25:22}.

Sure bir örtünün içine girişle biter: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}, {ar:وَٱدْخُلِى جَنَّتِى, tr:vedhulî cennetî, gloss:ve cennetime gir, source:89:30}. Girmek, çıkmanın karşıtıdır: {ar:الدخول نقيض الخروج, tr:ed-duhûlu nakîdu'l-hurûc, gloss:girmek çıkmanın zıddıdır, source:"د خ ل,B001"}. Girilen yer gecenin örtüsüyle aynı köktendir. Bahçe {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:kullu bustânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bahçe, source:"ج ن ن,B003"} demektir, ahiretteki cennet de {ar:ثواب مستور عنهم اليوم, tr:sevâbun mestûrun anhumu'l-yevm, gloss:bugün onlardan gizli tutulan bir karşılık, source:"ج ن ن,B004"}. Kur'an bu gizliliği açıkça söyler: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ, tr:fe-lâ ta'lemu nefsun mâ uhfiye lehum min kurrati a'yun, gloss:onlar için gizlenmiş göz aydınlığını hiçbir can bilmez, source:32:17}. Aynı kök bir örtüyü daha adlandırır: {ar:الجنن القبر, tr:el-cenen el-kabr, gloss:cenen, kabirdir, source:"ج ن ن,B009"}. Yirmi birinci ayetin dövme fiili de ölünün üstüne toprak yığmayı anlatır: {ar:دككت التراب على الميت إذا هلته عليه, tr:dekektu't-turâbe ale'l-meyyiti izâ hiltuhû aleyh, gloss:toprağı ölünün üstüne yığdım, source:"د ك ك,B003"}. Yerin dövüldüğü ayette kabir toprağı da duyulur. Surenin son kelimesi ise ağaçların örtüsüdür. Ruh toprağın örtüsüne değil, bahçenin örtüsüne çağrılır.

Bir halka daha vardır. Yirmi yedinci ayette seslenilen {ar:ٱلنَّفْسُ, tr:en-nefs, gloss:can, source:89:27} kelimesinin kökü sabahın nefes almasını da adlandırır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subhu ey teballec, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Bu nefes alma şafağın yarılmasıyla açıklanır: {ar:إذا انشق الفجر وانفلق, tr:ize'nşakka'l-fecru ve'nfelak, gloss:şafak yarılıp açıldığında, source:"ن ف س,B009"}. Sure fecrle açılır ve son çağrısını nefse yapar. İkisini Tekvîr'in nefes alan sabahı birbirine bağlar {source:81:18}.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B002; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:2 وَلَيَالٍ ل ي ل B001; 89:4 يَسْرِ س ر ي B001; 89:4 يَسْرِ س ر ي B004; 89:5 حِجْرٍ ح ج ر B001; 89:5 حِجْرٍ ح ج ر B002; 89:21 دُكَّتِ د ك ك B003; 89:27 ٱلنَّفْسُ ن ف س B009; 89:29 فَٱدْخُلِى د خ ل B001; 89:30 جَنَّتِى ج ن ن B002; 89:30 جَنَّتِى ج ن ن B003; 89:30 جَنَّتِى ج ن ن B004; 89:30 جَنَّتِى ج ن ن B009

## Saf saf gelenler

Yer dövülüp düzlendikten sonra bir topluluk gelir: {ar:وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا, tr:ve câe rabbuke ve'l-meleku saffen saffâ, gloss:Rabbin ve melekler saf saf geldiğinde, source:89:22}. Gelmek (mecî') genel bir fiildir: {ar:المجيء كالإتيان لكن المجيء أعم, tr:el-mecîu ke'l-ityân, lâkinne'l-mecîe a'amm, gloss:mecî' gelmek gibidir, ama ondan daha geniştir, source:"ج ي ء,B001"}. Melek kelimesi burada tekildir, ama bütün sınıfı kapsar: {ar:الملك من الملائكة واحد وجمع, tr:el-melek mine'l-melâike vâhidun ve cem', gloss:melek kelimesi hem tekil hem çoğul için kullanılır, source:"م ل ك,B009"}. Kur'an aynı tekili yerin ve dağların ezildiği sahnede de kullanır: {ar:وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا, tr:ve'l-meleku alâ ercâihâ, gloss:melekler de göğün kenarlarındadır, source:69:17}. Saf, bir şeyi düz bir çizgi üzerine dizmektir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın mustevin, gloss:saf, bir şeyi düz bir çizgi üzerine dizmektir, source:"ص ف ف,B001"}. Durulan yer de bu kökten adlandırılır: {ar:المصف الموقف, tr:el-masaff el-mevkıf, gloss:masaff, durulan yerdir, source:"ص ف ف,B001"}. Kelimenin tekrarı bir dağıtım kalıbıdır. Arapça gelme fiilini tekrarlanan bir sayıyla aynı biçimde kurar: {ar:جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة, tr:câe'l-kavmu uşâra uşâr, ve ma'şera ma'şer, ey aşeraten aşera, gloss:topluluk onar onar geldi, source:"ع ش ر,B005"}. Ayetteki tekrar da aynı şeyi söyler: saf ardından saf gelir. İkinci ayetteki "on" kelimesinin kökü bu kalıbı önceden taşır.

Gelişin ritmi surenin önceki kelimelerinde de vardır. Üçüncü ayetteki tek kelimesinin kökünden birbiri ardınca gelmek anlamı türer: {ar:تترى من الوتر أي واحدا بعد واحد, tr:tetrâ mine'l-vetr, ey vâhiden ba'de vâhid, gloss:tetrâ vetr kökündendir, yani birbiri ardınca, source:"و ت ر,B004"}. Kur'an bu kelimeyi elçilerin ve onları yalanlayan ümmetlerin dizisi için kullanır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:summe erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}. Aynı ayette yalanlayan ümmetler de birbirinin ardınca yok edilip söz konusu edilen hikâyelere dönüştürülür. Surenin altıncı ve onuncu ayetleri arasında anılan kavimler de böyle bir dizi oluşturur. İlk kelimenin kökü de bir topluluğun ansızın üstüne gelişini anlatır: {ar:انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infeceret aleyhimu'd-devâhî izâ câehumu'l-kesîru minhâ bağteten, gloss:felaketler birdenbire ve çok sayıda gelince "üstlerine boşandı" denir, source:"ف ج ر,B003"}. Dövme fiili de kalabalığın bir şeye yüklenmesini anlatır: {ar:تداك عليه القوم إذا ازدحموا عليه, tr:tedâkke aleyhi'l-kavmu izezdehamû aleyh, gloss:insanlar onun üstüne üşüştü, source:"د ك ك,B008"}.

Yirmi üçüncü ayette cehennem getirilir: {ar:وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ, tr:ve cîe yevmeizin bi-cehennem, gloss:o gün cehennem getirildiğinde, source:89:23}. Bir şeyi getirmek onu hazır etmektir: {ar:وجاء بكذا: استحضره, tr:ve câe bi-kezâ: istahdarah, gloss:onu getirdi, yani hazır etti, source:"ج ي ء,B004"}. Uzakta sanılan şey göz önüne konur. Kur'an aynı edilgen fiili Sûr'dan sonraki sahnede kullanır: {ar:وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ, tr:ve cîe bi'n-nebiyyîne ve'ş-şuhedâ', gloss:peygamberler ve şahitler getirildi, source:39:69}. Cehennemin ortaya çıkarılmasını da şöyle anlatır: {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ, tr:ve burrizeti'l-cahîmu li-men yerâ, gloss:cehennem gören herkes için ortaya çıkarılır, source:79:36}, {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ, tr:ve burrizeti'l-cahîmu li'l-ğâvîn, gloss:cehennem azgınlara gösterilir, source:26:91}. Her can da yanında bir sürücü ve bir şahitle gelir: {ar:وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ, tr:ve câet kullu nefsin meahâ sâikun ve şehîd, gloss:her can yanında bir sürücü ve bir şahitle gelir, source:50:21}. Safın kendisi de başka sahnelerde vardır: {ar:يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا, tr:yevme yekûmu'r-rûhu ve'l-melâiketu saffâ, gloss:Ruh ve meleklerin saf hâlinde durduğu gün, source:78:38}, {ar:وَٱلصَّٰٓفَّٰتِ صَفًّۭا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1}. İnsanlar da Rabbe saf hâlinde sunulur: {ar:وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا, tr:ve urıdû alâ rabbike saffâ, gloss:Rabbine saf hâlinde sunuldular, source:18:48}. Bu geliş inkârcıların beklediği şeyin gerçekleşmesidir: {ar:هَلْ يَنظُرُونَ إِلَّآ أَن يَأْتِيَهُمُ ٱللَّهُ فِى ظُلَلٍۢ مِّنَ ٱلْغَمَامِ وَٱلْمَلَٰٓئِكَةُ, tr:hel yenzurûne illâ en ye'tiyehumu'llâhu fî zulelin mine'l-ğamâmi ve'l-melâike, gloss:onlar Allah'ın ve meleklerin bulut gölgeleri içinde gelmesinden başka bir şey mi bekliyorlar, source:2:210}. Aynı bekleyiş başka bir ayette de dile getirilir {source:6:158}. Göğün bulutla yarıldığı ve meleklerin indirildiği gün de anlatılır {source:25:25}.

Kaynaklar: 89:1 ٱلْفَجْرِ ف ج ر B003; 89:2 عَشْرٍۢ ع ش ر B005; 89:3 ٱلْوَتْرِ و ت ر B004; 89:21 دَكًّۭا د ك ك B008; 89:22 وَجَآءَ ج ي ء B001; 89:22 وَٱلْمَلَكُ م ل ك B009; 89:22 صَفًّۭا ص ف ف B001; 89:23 وَجِا۟ىٓءَ ج ي ء B004

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

