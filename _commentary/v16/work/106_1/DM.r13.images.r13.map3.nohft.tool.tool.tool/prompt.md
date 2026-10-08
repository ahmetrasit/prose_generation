Focus: 106:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/106_1/D.r13/context.md =====
# 106:1 — focus

لِإِيلَٰفِ قُرَيْشٍ

Anchor translation (canonical reading, reference only):

Kureyş'in alışması nedeniyle,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لِإِيلَٰفِ | إِلَٰف | ء ل ف | P;N |
| 2 | قُرَيْشٍ | قُرَيْش |  | PN |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 106 — full text (context; no pericope)

- 106:1 ◀ focus لِإِيلَٰفِ قُرَيْشٍ
- 106:2 إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ
- 106:3 فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- 106:4 ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ


===== _commentary/v16/work/106_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ل ف (root_000045) — identity root of لِإِيلَٰفِ (w1)

- **B001** bin sayısı ve bine tamamlama — bilinen bin sayısı; çoğulu binler · bir topluluğu bin kişiye tamamlamak veya onların bin kişi olması · para miktarını bin değerine ulaştırmak
  الألف معروف والجمع الآلاف (maqayis)؛ الألف عدد والجمع ألوف وآلاف (sihah)؛ والألف من العدد معروف (tahdhib)؛ الألف العدد المخصوص (mufradat)؛ آلفت القوم صيرتهم ألفا (maqayis;sihah)؛ آلفت الدراهم أي بلغت بها الألف (mufradat)
- **B002** birleştirip düzenlemek — bir şeyin parçalarını birbirine katmak veya bağlamak · iki şeyin arasını birleştirmek veya ayrılıktan sonra toplamak · farklı parçalardan düzenlenmiş bütün
  انضمام الشيء إلى الشيء (maqayis)؛ كل شيء ضممت بعضه إلى بعض فقد ألفته تأليفا (maqayis)؛ ألفت بين الشيئين تأليفا (sihah)؛ ألفت بينهم تأليفا إذا جمعت بينهم بعد تفرق (tahdhib)؛ ألفت الشيء وصلت بعضه ببعض ومنه تأليف الكتب (tahdhib)؛ اجتماع مع التئام (mufradat)؛ المؤلف ما جمع من أجزاء مختلفة ورتب ترتيبا (mufradat)
- **B003** gönlünü kazanmak — gönülleri yakınlık ve destekle kazanılmaya çalışılan kimseler · birini yakınlık, ilgi veya destekle kazanmak
  تألفته على الإسلام ومنه المؤلفة قلوبهم (sihah)؛ والمؤلفة قلوبهم هؤلاء قوم من سادة العرب أمر الله نبيه بتألفهم أي بمقاربتهم وإعطائهم من الصدقات (tahdhib)؛ والمؤلفة قلوبهم هم الذين يتحرى فيهم بتفقدهم (mufradat)
- **B004** mevsimlik yolculuk düzeni — belirli topluluğun kış ve yaz yolculuklarını bağlama, hazırlama veya güvenceye alma ifadesi
  لإيلاف قريش (maqayis;mufradat)؛ لتؤلف قريش رحلة الشتاء والصيف أي تجمع بينهما (sihah)؛ لتؤلف قريش الرحلتين فيتصلا ولا ينقطعا (tahdhib)؛ يؤلفون يهيئون ويجهزون (tahdhib)؛ يؤلفون يجيرون (tahdhib)؛ لهم إلف وليس لكم إيلاف (tahdhib)
- **B005** ünsiyet ve alışma — alışılan, tanıdık ve ünsiyet duyulan kişi veya şey · bir yere alışmak, orada kalmayı sürdürmek · bir kimseyle ünsiyet kurmak · bir eve veya yere alışmış kuşlar
  ألفت الشيء آلفه والألفة مصدر الائتلاف (maqayis)؛ إلفك وأليفك الذي تألفه (maqayis)؛ آلفت المكان والقوم (maqayis)؛ أوالف الطير التي بمكة (maqayis)؛ فلان قد ألف هذا الموضع يألفه إلفا (sihah)؛ ألفت الشيء وآلفته بمعنى واحد أي لزمته (tahdhib)؛ ألفت فلانا إذا أنست به (tahdhib)؛ أوالف الحمام دواجنها التي تألف البيوت (tahdhib)؛ يقال للمألوف إلف وأليف (mufradat)؛ أوالف الطير ما ألفت الدار (mufradat)
- **B006** alfabe işareti adı — alfabedeki belirli yazı ve ses işaretinin adı ve teknik türleri
  الألف من حروف التهجي (mufradat)؛ أصول الألفات ثلاثة (tahdhib)؛ الألف الفاصلة (tahdhib)؛ ألف العبارة (tahdhib)؛ الألف اللينة (tahdhib)؛ هذه ألف مؤلفة (tahdhib)

===== _commentary/v16/out/s106/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 106:1, and ## Buluşmalar) =====
## İki mevsimin yolculuğunu birbirine bağlamak

Surenin ilk kelimesi bir bağlama işini adlandırır. Yolculuk için kullanıldığında {ar:إيلاف, tr:îlâf, gloss:bağlayıp sürdürme, source:"ء ل ف,B004"}, kış yolculuğunu yaz yolculuğuna eklemek ve ikisini tek bir çizgi hâline getirmektir: {ar:لتؤلف قريش رحلة الشتاء والصيف أي تجمع بينهما, tr:li-tu'life Kureyşun rihlete'ş-şitâi ve's-sayf ey tecma'a beynehumâ, gloss:Kureyş kış ve yaz yolculuğunu bağlasın yani ikisini bir araya getirsin, source:"ء ل ف,B004"}. Aynı işin amacı da açıkça söylenir: {ar:لتؤلف قريش الرحلتين فيتصلا ولا ينقطعا, tr:li-tu'life Kureyşun'r-rihleteyni fe-yettasılâ ve lâ yenkatı'â, gloss:Kureyş iki yolculuğu bağlasın da birbirine eklensinler ve kopmasınlar, source:"ء ل ف,B004"}. Kökün genel işleyişi de budur: parçaları birbirine ulamak, {ar:ألفت الشيء وصلت بعضه ببعض, tr:eleftu'ş-şey'e vasaltu ba'dahû bi-ba'd, gloss:şeyi bağladım yani bir kısmını öbürüne ekledim, source:"ء ل ف,B002"}, ve bu ulamanın sonunda ortaya çıkan şey dağınık bir yığın değil, kaynaşmış bir bütündür: {ar:اجتماع مع التئام, tr:ictimâ' ma'a'l-ti'âm, gloss:kaynaşarak bir araya gelme, source:"ء ل ف,B002"}.

Bağlanan parçaların ne olduğu da açıktır. {ar:رحلة, tr:rihle, gloss:yolculuk, source:"ر ح ل,B001"} tek bir kişinin gezisi değil, bir topluluğun yola koyulmasıdır: {ar:الرحلة اسم ارتحال القوم للمسير, tr:er-rihletu ismu'rtihâli'l-kavmi li'l-mesîr, gloss:rihle topluluğun yürüyüşe koyulmasının adıdır, source:"ر ح ل,B001"}. Kış ve yaz ise birbirinin karşıtı olarak tanımlanır: {ar:الشتاء خلاف الصيف, tr:eş-şitâu hilâfu's-sayf, gloss:kış yazın karşıtıdır, source:"ش ت و,B001"} ve {ar:الصيف الفصل المقابل للشتاء, tr:es-sayfu'l-faslu'l-mukâbilu li'ş-şitâ', gloss:yaz kışın karşısındaki mevsimdir, source:"ص ي ف,B001"}. Yani sahne şudur: yılın birbirine zıt iki yarısı, her birinin kendi çıkışı, kendi yükü, kendi güzergâhı vardır ve bu iki parça uç uca eklenerek arada boşluk kalmayacak biçimde bağlanır. Arapçanın bir yazlık ve kışlık yurtları tek bir yıllık dönüş içinde yan yana sayan kullanımı da bu tabloyu tamamlar: {ar:شتونا بالصمان وشتينا الصمان وهذه مشاتينا ومصايفنا ومرابعنا, tr:şetevnâ bi's-Sammân ve şeteyne's-Sammân ve hâzihî meşâtînâ ve mesâyifunâ ve merâbi'unâ, gloss:kışı Sammân'da geçirdik; işte kışlaklarımız ve yazlaklarımız ve baharlıklarımız, source:"ش ت و,B002"}. Yazın gelişi de bir öncekinin tamamlanması olarak söylenir: {ar:تمام الربيع الصَّيف, tr:temâmu'r-rebî'i's-sayf, gloss:baharın tamamı yazdır, source:"ص ي ف,B006"}. Halka böylece kapanır.

Aralıksız bağlanan şey zamanla alışkanlık olur. Aynı kök bu iç yüzü de taşır: {ar:ألفت الشيء وآلفته بمعنى واحد أي لزمته, tr:eliftu'ş-şey'e ve âleftuhû bi-ma'nen vâhid ey lezimtuh, gloss:şeye alıştım yani ondan ayrılmadım, source:"ء ل ف,B005"}. Dışarıdan bakınca iki yolculuğun eklenmesi, içeriden bakınca bir topluluğun o düzene bağlanıp kalmasıdır. Bu sayfada anılan aile imgeleri her zaman kelimenin kendi ayetindeki anlamının yanında duyulur, o anlamın yerine geçmez; burada da ayetin söylediği Kureyş'in iki yolculuğu ve onlara alışmasıdır, bağlama sahnesi bu anlamın içindeki işleyişi görünür kılar.

Düz bir aktarım "Kureyş'in kış ve yaz yolculuğuna alışkanlığı" der ve orada durur. Kelimenin işleyişi ise bu alışkanlığın bir ekler dizisi olduğunu gösterir: yılın güvenliği iki parçanın birbirine tutturulmasına dayanır ve bir halka koparsa bütün düzen durur. Sure, minnet konusu olarak tam da bu kesintisizliği gösterir.

Ayetler bu sahneyi sırayla kurar. Birinci ayet yalnızca bağlamanın adını ve kime ait olduğunu verir, {ar:لِإِيلَٰفِ قُرَيْشٍ, tr:li-îlâfi Kureyş, gloss:Kureyş'in bağlayıp sürdürmesi için, source:106:1}, ama neyin bağlandığını söylemez. İkinci ayet aynı kelimeyi tekrar eder, bu kez zamirle, {ar:إِۦلَٰفِهِمْ, tr:îlâfihim, gloss:onların bağlayıp sürdürmesi, source:106:2}, ve bağlananı adlandırır: {ar:رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ, tr:rihlete'ş-şitâi ve's-sayf, gloss:kışın ve yazın yolculuğu, source:106:2}. Dikkat çekici olan, iki mevsime tek bir "yolculuk" kelimesinin yetmesidir: dil düzeyinde iki sefer zaten tek bir rihledir. Birinci ayetteki "için" anlamındaki edat bir sonuca bağlanmayı bekler ve bu sonuç üçüncü ayetteki emirdir, {ar:فَلْيَعْبُدُوا۟, tr:fe'l-ya'budû, gloss:öyleyse kulluk etsinler, source:106:3}: kesintisiz halka, kulluğun gerekçesi olarak öne konmuştur. Dördüncü ayet bu halkanın ne verdiğini adlandırır: doyurulmak ve emin kılınmak.

Kur'an bağlanmış yolculuğu ve onun çözülmesini başka bir kavmin kıssasında sahneler. Allah Sebe' halkını anlatırken önce yurtlarındaki âyeti, sağlı sollu iki bahçeyi ve onlara söylenen sözü anar, {ar:كُلُوا۟ مِن رِّزْقِ رَبِّكُمْ وَٱشْكُرُوا۟ لَهُۥ, tr:kulû min rizkı rabbikum veşkurû leh, gloss:Rabbinizin rızkından yiyin ve O'na şükredin, source:34:15}; yüz çevirmeleri üzerine seli gönderir {source:34:16}. Ardından yolları anlatılır: aralarında ve bereketli kasabalar arasında birbirini gören konaklar kurulmuş, yürüyüş ölçülüp bölünmüştür, {ar:وَقَدَّرْنَا فِيهَا ٱلسَّيْرَ ۖ سِيرُوا۟ فِيهَا لَيَالِىَ وَأَيَّامًا ءَامِنِينَ, tr:ve kaddernâ fîhe's-seyr; sîrû fîhâ leyâliye ve eyyâmen âminîn, gloss:orada yürüyüşü ölçüp düzenledik; oralarda geceler ve günler boyu güven içinde yürüyün, source:34:18}. Bu, uç uca eklenmiş ve güvenle yürünen bir yoldur. Sonraki ayette ise o halk tam tersini ister: {ar:رَبَّنَا بَٰعِدْ بَيْنَ أَسْفَارِنَا, tr:rabbenâ bâ'id beyne esfârinâ, gloss:Rabbimiz seferlerimizin arasını uzaklaştır, source:34:19}. Bağlantının koparılmasını istemişlerdir ve karşılığı kendilerinin parçalanmasıdır: {ar:وَمَزَّقْنَٰهُمْ كُلَّ مُمَزَّقٍ, tr:ve mezzaknâhum kulle mumezzak, gloss:onları paramparça dağıttık, source:34:19}. Surenin minnet olarak andığı kesintisizlik, Sebe' kıssasında nankörlükle kaybedilen şeydir. Göç ile yerleşik oluşun bir hayatta nasıl birbirine eklendiğini Allah'ın nimet sayımı da gösterir: hayvan derilerinden {ar:بُيُوتًۭا تَسْتَخِفُّونَهَا يَوْمَ ظَعْنِكُمْ وَيَوْمَ إِقَامَتِكُمْ, tr:buyûten testehiffûnehâ yevme za'nikum ve yevme ikâmetikum, gloss:göç gününüzde ve konakladığınız günde hafif bulduğunuz evler, source:16:80}.

Kaynaklar: 106:1 لِإِيلَٰفِ ء ل ف B004; 106:1 لِإِيلَٰفِ ء ل ف B002; 106:1 لِإِيلَٰفِ ء ل ف B005; 106:2 إِۦلَٰفِهِمْ ء ل ف B004; 106:2 رِحْلَةَ ر ح ل B001; 106:2 ٱلشِّتَآءِ ش ت و B001; 106:2 ٱلشِّتَآءِ ش ت و B002; 106:2 وَٱلصَّيْفِ ص ي ف B001; 106:2 وَٱلصَّيْفِ ص ي ف B006; Kur'an: 34:15, 34:16, 34:18, 34:19, 16:80

## Yolculuğu taşıyan binek

Bir topluluğun yola çıkması, onu taşıyacak hayvan olmadan düşünülemez ve {ar:رحل, tr:rahl, gloss:semer, source:"ر ح ل,B002"} kökü bineği bütün donanımıyla getirir. Önce semer vardır: {ar:الرحل ما يوضع على البعير للركوب, tr:er-rahlu mâ yûda'u ale'l-ba'îri li'r-rukûb, gloss:rahl binmek için devenin üstüne konan şeydir, source:"ر ح ل,B002"}. Sonra semeri bağlama işi gelir, ki yola çıkışın ilk hareketidir: {ar:رحلت البعير أرحله رحلا إذا شددت على ظهره الرحل, tr:rahaltu'l-ba'îra erhaluhû rahlen izâ şedettu alâ zahrihi'r-rahl, gloss:deveyi semerledim yani sırtına semeri sıkıca bağladım, source:"ر ح ل,B003"}. Hayvanın bu yükü kaldırabilmesi gerekir ve kök bunu bir besleme süreci olarak anlatır: {ar:أرحلت الإبل سمنت بعد هزال فأطاقت الرحلة, tr:erhaleti'l-ibilu seminet ba'de huzâlin fe-etâkati'r-rihle, gloss:develer zayıflıktan sonra semirdi de yolculuğa güç yetirir oldu, source:"ر ح ل,B005"}. Sonuç yolculuğa elverişli hayvandır: {ar:الراحلة البعير الذي يصلح للارتحال, tr:er-râhiletu'l-ba'îru'llezî yasluhu li'l-irtihâl, gloss:râhile yola çıkmaya elverişli devedir, source:"ر ح ل,B005"}, {ar:بعير رحيل إذا كان قويا على حمل الرحل, tr:ba'îrun rahîl izâ kâne kaviyyen alâ hamli'r-rahl, gloss:semeri taşımaya güçlü deveye rahîl denir, source:"ر ح ل,B005"}. Kök bir de yardımlaşmayı adlandırır: başkasının yolculuğuna destek olmak ve ona binek vermek, {ar:راحلت فلانا إذا عاونته على رحلته وأرحلته إذا أعطيته راحلة, tr:râhaltu fulânen izâ â'antuhû alâ rihletihî ve erhaltuhû izâ a'taytuhû râhile, gloss:yolculuğunda ona yardım ettim ve ona binek verdim, source:"ر ح ل,B008"}. Surenin ilk kelimesinin de bu donanma işine bir yüzü vardır: {ar:يؤلفون يهيئون ويجهزون, tr:yu'lifûne yuhey'iûne ve yucehhizûn, gloss:îlâf ederler yani hazırlar ve donatırlar, source:"ء ل ف,B004"}.

Sonraki ayetlerin kelimeleri bu sahneyi tamamlar ve bunu, kelimelerin kendi anlamlarının yanında duyulan aile imgeleriyle yapar. Üçüncü ayetteki kulluk fiilinin kökü, aynı kök içinde, güçlü ve semiz dişi deveyi adlandırır: {ar:ناقة ذات عبدة أي ذات قوة وسمن, tr:nâkatun zâtu abede ey zâtu kuvvetin ve simen, gloss:abede sahibi dişi deve yani güçlü ve semiz deve, source:"ع ب د,B007"}. Aynı kök tersini de söyler, bineği yolda tükenip kalan yolcuyu: {ar:أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت, tr:u'bide bi-fulânin bi-ma'nâ ubdi'a bihî izâ kellet râhiletuhû ev atibet, gloss:bineği yorulunca ya da sakatlanınca adam yolda kaldı, source:"ع ب د,B011"}, {ar:أعبد به إذا ذهبت راحلته, tr:u'bide bihî izâ zehebet râhiletuh, gloss:bineği elinden gidince yolda kaldı, source:"ع ب د,B011"}. Bu ifadede geçen hayvan adı yolculuk kökünün râhilesidir. Bir de binicisine direnen deve vardır: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:ba'îrun muta'abbidun ve mute'ebbidun izâ imtene'a ale'n-nâsi su'ûbeten, gloss:huysuzluğundan insanlara boyun eğmeyen deve, source:"ع ب د,B011"}. Dördüncü ayetin besleme fiilinin kökü, ilik kemiğine kadar yağ bağlamış deveyi adlandırır: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم, tr:el-mut'amu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm, gloss:iliğinde yağ tadı bulunan deve, source:"ط ع م,B007"}. Aynı ayetin güven fiilinin kökü ise güvenilir dişi deveyi: {ar:الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها, tr:el-emûnu'n-nâkatu'l-emînetu'l-vesîka evi'lletî yu'menu futûruhâ ve usûruhâ, gloss:emûn sağlam ve güvenilir dişi devedir ya da gevşeyip tökezlemesinden korkulmayan devedir, source:"ء م ن,B001"}.

Sahne böylece işleyen bir binek olarak kurulur: semeri bağlanır, zayıflıktan semizliğe beslenir, gücü yerindedir, tökezlemesinden korkulmaz; bunun karşısında, hayvanı ortada tükendiği için yolun ortasında kalmış yolcu durur. Düz aktarım dördüncü ayetin iki nimetini soyut bırakır. Binek sahnesi ise doyurma ile güvenin yolculuğun en somut dayanağında, sırtında yük taşıyan hayvanda da var olduğunu gösterir: beslenmiş ve tökezlemeyen bir hayvan, aç kalmamış ve korkudan kurtulmuş bir kervanın ön şartıdır.

Ayetlerin sırası da sahneyi adım adım doldurur. Birinci ayette îlâf donanmadır. İkinci ayette {ar:رِحْلَةَ, tr:rihlete, gloss:yolculuk, source:106:2} kelimesi semeri, semerlemeyi, beslenmiş ve güçlü hayvanı, binek vermeyi taşır. Üçüncü ayetin kulluk fiili, anlamı kulluk olarak kalmak üzere, aynı kökten güçlü deveyi ve yolda kalan yolcuyu yanında duyurur. Dördüncü ayetin {ar:أَطْعَمَهُم, tr:et'amehum, gloss:onları doyurdu, source:106:4} ve {ar:وَءَامَنَهُم, tr:ve âmenehum, gloss:ve onları emin kıldı, source:106:4} fiilleri, iliğine kadar beslenmiş ve tökezlemeyen deveyi yanlarında taşır.

Kur'an bineği Allah'ın nimetleri arasında anar. Nahl suresinde Allah hayvanları sayarken önce şunu söyler: {ar:لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:lekum fîhâ dif'un ve menâfi'u ve minhâ te'kulûn, gloss:onlarda sizin için ısınma ve yararlar var ve onlardan yersiniz, source:16:5}; sonra yolculuğa geçer: {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:canınızı zorlamadan varamayacağınız bir diyara yüklerinizi taşırlar, source:16:7}, ve ayet {ar:إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ, tr:inne rabbekum le-raûfun rahîm, gloss:Rabbiniz çok şefkatli ve merhametlidir, source:16:7} diye biter; yük hayvanı ile Rab aynı cümlede buluşur. Yusuf kıssasında kıtlıkta erzak almaya gelen kardeşler {source:12:58} için Yusuf'un yaptığı iş tam bir kervan donatmasıdır: {ar:جَهَّزَهُم بِجَهَازِهِمْ, tr:cehhezehum bi-cehâzihim, gloss:onları yüklerini hazırlayarak donattı, source:12:59}. Yusuf adamlarına, mallarını {ar:فِى رِحَالِهِمْ, tr:fî rihâlihim, gloss:semer yüklerinin içine, source:12:62} koymalarını söyler; sonra su kabını {ar:فِى رَحْلِ أَخِيهِ, tr:fî rahli ehîh, gloss:kardeşinin semer yüküne, source:12:70} koydurur ve kervana {ar:أَيَّتُهَا ٱلْعِيرُ, tr:eyyetuhe'l-îr, gloss:ey kervan, source:12:70} diye seslenilir. Buradaki rahl, surenin rihlesiyle aynı köktendir ve kervanın sırtındaki semer yükünü adlandırır. Zuhruf suresinde Allah binilecek gemileri ve hayvanları anar ve binmenin amacını söyler: {ar:لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ, tr:li-testevû alâ zuhûrihî summe tezkurû ni'mete rabbikum, gloss:sırtlarına yerleşesiniz sonra Rabbinizin nimetini anasınız diye, source:43:13}. Binek sırtına yerleşmek ile Rabbin nimetini anmak tek bir harekettir. Hac çağrısında ise Allah İbrahim'e insanların Ev'e nasıl geleceğini söyler: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ kulli dâmirin ye'tîne min kulli feccin amîk, gloss:sana yaya olarak ve her uzak geçitten gelen incelmiş binekler üzerinde gelsinler, source:22:27}. Ev'e gelen hayvan yolun zayıflattığı hayvandır; semirtilmiş bineğin öbür ucu budur.

Kaynaklar: 106:1 لِإِيلَٰفِ ء ل ف B004; 106:2 رِحْلَةَ ر ح ل B002; 106:2 رِحْلَةَ ر ح ل B003; 106:2 رِحْلَةَ ر ح ل B005; 106:2 رِحْلَةَ ر ح ل B008; 106:3 فَلْيَعْبُدُوا۟ ع ب د B007; 106:3 فَلْيَعْبُدُوا۟ ع ب د B011; 106:4 أَطْعَمَهُم ط ع م B007; 106:4 وَءَامَنَهُم ء م ن B001; Kur'an: 16:5, 16:7, 12:58, 12:59, 12:62, 12:70, 43:13, 22:27

## Korunan yol: aman, ahit ve korkulan yol

Kervan başkalarının topraklarından geçer ve bu geçiş ancak birinin koruması altında mümkündür. Surenin ilk kelimesinin bir kullanımı tam olarak budur, himaye vermek: {ar:يؤلفون يجيرون, tr:yu'lifûne yucîrûn, gloss:îlâf ederler yani himaye verirler, source:"ء ل ف,B004"}. Bu himaye herkesin sahip olduğu bir şey değildir; birine ait olup ötekine ait olmayabilir: {ar:لهم إلف وليس لكم إيلاف, tr:lehum ilfun ve leyse lekum îlâf, gloss:onların himaye bağı var sizin ise îlâfınız yok, source:"ء ل ف,B004"}. Rab kelimesinin kökü de, kendi anlamı Rab olarak kalırken, bağlayıcı ahdi ve o ahde bağlı olanları adlandırır: {ar:الربابة: العهد والميثاق؛ الأربة أهل الميثاق, tr:er-ribâbetu el-ahdu ve'l-mîsâk; el-erıbbetu ehlu'l-mîsâk, gloss:ribâbe ahit ve antlaşmadır; erıbbe antlaşma ehlidir, source:"ر ب ب,B011"}, {ar:العقد في موالاة الغير: الربابة, tr:el-akdu fî muvâlâti'l-gayr er-ribâbe, gloss:başkasıyla dostluk bağı kurma akdi ribâbedir, source:"ر ب ب,B011"}.

Bunun karşısında korkulan yol durur. Burada ince bir ayrım vardır: yolun kendisi korkutmaz, korkutan yolun üzerindeki eşkıyadır: {ar:طريق مخوف لأنه لا يخيف وإنما يخيف فيه قاطع الطريق, tr:tarîkun mahûf li-ennehû lâ yuhîfu ve innemâ yuhîfu fîhi kâtı'u't-tarîk, gloss:yola mahûf denir çünkü kendisi korkutmaz; onda korkutan yol kesicidir, source:"خ و ف,B002"}, {ar:طريق مخوف يخافه الناس ومخيف يخيف الناس, tr:tarîkun mahûfun yehâfuhu'n-nâs ve muhîfun yuhîfu'n-nâs, gloss:insanların korktuğu ve insanları korkutan yol, source:"خ و ف,B002"}. Güven kökünün kendi terimi ise aman vermektir ve ona sığınmaktır: {ar:الأمان إعطاء الأمنة, tr:el-emânu i'tâu'l-emene, gloss:aman güvence vermektir, source:"ء م ن,B001"}, {ar:استأمن إليه دخل في أمانه, tr:iste'mene ileyhi dehale fî emânih, gloss:ondan aman istedi yani onun güvencesine girdi, source:"ء م ن,B001"}. Kervanın geçtiği açık arazi de kulluk kökünün bir kullanımında görünür: {ar:العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة, tr:el-abâbîdu ve'l-abâbîdu el-etrâfu'l-ba'îdetu ve'l-eşyâu'l-muteferrikatu ve't-turuku'l-muhtelife, gloss:uzak kenarlar ve dağınık şeyler ve her yöne ayrılan yollar, source:"ع ب د,B010"}.

Sahne, uzak kenarlara dağılan yollar arasında, himaye ve ahitlerle açık tutulan bir kervan yoludur; tersi ise eşkıyanın beklediği yoldur. Düz aktarımda dördüncü ayetin "korkudan emin kıldı" sözü bir iç huzur gibi okunabilir. Bu sahne ise o güvenin bir yolun geçilebilir olması, birinin kervana aman vermesi olduğunu görünür kılar: korkuyu yaratan yol değil yoldaki tehdittir, güveni sağlayan da tehdidin önünü alan himayedir.

Ayetler bu sahneyi şöyle doldurur. Birinci ayette îlâf himaye vermenin adıdır. İkinci ayetin iki mevsimlik yolculuğu korunması gereken güzergâhtır. Üçüncü ayette Rab kelimesi ahdi ve ahit ehlini, kulluk fiili her yöne dağılan yolları yanında duyurur. Dördüncü ayetin {ar:وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ve âmenehum min havf, gloss:ve onları korkudan emin kıldı, source:106:4} sözü hem korkulan yolu hem verilen amanı kapsar.

Kur'an Mekke'nin güvenliğini çevresindeki kapışmanın karşısına koyar. Ankebût suresinde Allah sorar: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا جَعَلْنَا حَرَمًا ءَامِنًۭا وَيُتَخَطَّفُ ٱلنَّاسُ مِنْ حَوْلِهِمْ, tr:e-ve lem yerev ennâ ce'alnâ haramen âminen ve yutehattafu'n-nâsu min havlihim, gloss:görmediler mi ki güvenli bir harem kıldık ve çevrelerinde insanlar kapılıp götürülüyor, source:29:67}, ve ayet {ar:وَبِنِعْمَةِ ٱللَّهِ يَكْفُرُونَ, tr:ve bi-ni'meti'llâhi yekfurûn, gloss:Allah'ın nimetine nankörlük mü ediyorlar, source:29:67} diye biter. Kasas suresinde aynı korkuyu Mekkeliler kendileri dile getirir: {ar:إِن نَّتَّبِعِ ٱلْهُدَىٰ مَعَكَ نُتَخَطَّفْ مِنْ أَرْضِنَآ, tr:in nettebi'i'l-hudâ me'ake nutehattaf min ardinâ, gloss:seninle birlikte doğru yola uyarsak yurdumuzdan kapılıp götürülürüz, source:28:57}. Allah'ın cevabı aynı ayettedir: {ar:أَوَلَمْ نُمَكِّن لَّهُمْ حَرَمًا ءَامِنًۭا, tr:e-ve lem numekkin lehum haramen âminâ, gloss:onları güvenli bir haremde yerleştirmedik mi, source:28:57}. Korkuları sure ile aynı kelimeyle adlandırılmış, güvenleri de aynı kökle verilmiştir. Mâide suresinde ise Ev'e yönelen yolcunun dokunulmazlığı bir emir olarak gelir: {ar:وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا, tr:ve lâ âmmîne'l-beyte'l-harâme yebteğûne fadlen min rabbihim ve rıdvânâ, gloss:Rablerinden lütuf ve hoşnutluk arayarak Beytülharam'a yönelenlere de dokunmayın, source:5:2}. Bakara suresi hac sırasında Rabden lütuf aramayı açıkça serbest bırakır: {ar:لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ, tr:leyse aleykum cunâhun en tebteğû fadlen min rabbikum, gloss:Rabbinizden bir lütuf aramanızda size bir günah yoktur, source:2:198}. Sebe' kıssasındaki {ar:سِيرُوا۟ فِيهَا لَيَالِىَ وَأَيَّامًا ءَامِنِينَ, tr:sîrû fîhâ leyâliye ve eyyâmen âminîn, gloss:oralarda geceler ve günler boyu güven içinde yürüyün, source:34:18} sözü de aynı korunmuş yolun adıdır.

Kaynaklar: 106:1 لِإِيلَٰفِ ء ل ف B004; 106:3 رَبَّ ر ب ب B011; 106:3 فَلْيَعْبُدُوا۟ ع ب د B010; 106:4 خَوْفٍۭ خ و ف B002; 106:4 وَءَامَنَهُم ء م ن B001; Kur'an: 29:67, 28:57, 5:2, 2:198, 34:18

## Konaklar, mevsimlik yurtlar ve dönülen ev

Yolculuk durmaksızın gitmek değil, kalkmak ile konmak arasında bir ritimdir. Yolculuk kökü bu ritmin birimini adlandırır, konaklama yerini ve iki konak arasındaki mesafeyi: {ar:المرحلة الموضع الذي تنزل به من حيث ترتحل, tr:el-merhaletu'l-mevdı'u'llezî tenzilu bihî min haysu tertehil, gloss:merhale yola koyulduğun yerden sonra konduğun yerdir, source:"ر ح ل,B006"}, {ar:المرحلة المنزل يرتحل منها وما بين المنزلين مرحلة, tr:el-merhaletu'l-menzilu yurtehalu minhâ ve mâ beyne'l-menzileyni merhale, gloss:merhale kalkılan konaktır; iki konak arası da merhaledir, source:"ر ح ل,B006"}. Rahl aynı zamanda insanın meskeni ve yanında taşıdığı eşyasıdır, ev de yolculukla birlikte yer değiştirir: {ar:الرحل مسكن الرجل وما يستصحبه من الاثاث, tr:er-rahlu meskenu'r-racul ve mâ yestashıbuhû mine'l-esâs, gloss:rahl adamın meskeni ve yanında götürdüğü eşyasıdır, source:"ر ح ل,B004"}. Kökün bir yüzü ise bu ritmin zorla bozulmasıdır, yerinden sökülmek: {ar:رحلته أظعنته أي أزلته عن مكانه, tr:rahhaltuhû az'antuhû ey ezeltuhû an mekânih, gloss:onu göçürdüm yani yerinden ettim, source:"ر ح ل,B007"}.

Mevsim kelimelerinin her biri de gitmeyi değil, bir yerde kalmayı da adlandırır. Kış kelimesinin fiili, kışı bir yerde geçirmektir: {ar:شتوت بموضع كذا وتشتيت أقمت به الشتاء, tr:şetevtu bi-mevdı'i kezâ ve teşetteytu ekamtu bihi'ş-şitâ', gloss:kışı falan yerde geçirdim, source:"ش ت و,B002"}, ve kışlanan yere {ar:المشتى, tr:el-meştâ, gloss:kışlak, source:"ش ت و,B002"} denir. Yaz kelimesinin fiili de yazı bir yerde geçirmektir: {ar:صاف بالمكان أي أقام به الصَّيف واصطاف مثله والموضع مصيف ومصطاف, tr:sâfe bi'l-mekâni ey ekâme bihi's-sayf vestâfe misluhû ve'l-mevdı'u masîfun ve mustâf, gloss:yazı o yerde geçirdi; yeri de yazlaktır, source:"ص ي ف,B003"}. Rab kelimesinin kökü, kendi anlamı yanında, bir yerde ayrılmadan kalmayı adlandırır: {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته, tr:erabbe fulânun bi'l-mekâni izâ ekâme bihî fe-lem yebrahh; merabbu'l-ibili ey haysu lezimeth, gloss:o yerde kaldı ve ayrılmadı; develerin merabbı ayrılmadıkları yerdir, source:"ر ب ب,B007"}, {ar:رب بالمكان وأرب إذا أقام به, tr:rabbe bi'l-mekâni ve erabbe izâ ekâme bih, gloss:o yerde ikamet etti, source:"ر ب ب,B007"}.

Bütün bu kalkış ve konuşların merkezinde ev durur. Ev kelimesinin kökü sığınağı ve dönülen yeri, dağınık olanın toplandığı yeri adlandırır: {ar:أصل واحد وهو المأوى والمآب ومجمع الشمل, tr:aslun vâhidun ve huve'l-me'vâ ve'l-meâbu ve mecme'u'ş-şeml, gloss:tek bir asıldır: sığınak ve dönülen yer ve dağınığın toplandığı yer, source:"ب ي ت,B001"}. Ev geceyi geçirdiğin yerdir: {ar:البيت سمي بيتا لأنه يبات فيه, tr:el-beytu summiye beyten li-ennehû yubâtu fîh, gloss:eve beyt denmiştir çünkü içinde gece geçirilir, source:"ب ي ت,B001"}, {ar:أصل البيت مأوى الإنسان بالليل, tr:aslu'l-beyti me'vâ'l-insâni bi'l-leyl, gloss:evin aslı insanın gece sığınağıdır, source:"ب ي ت,B001"}. Güven kökü de insanın konağını güven yeri olarak adlandırır: {ar:مأمنه منزله الذي فيه أمنه, tr:me'menuhû menziluhu'llezî fîhi emnuh, gloss:me'meni güvenliğinin bulunduğu konağıdır, source:"ء م ن,B001"}.

Bu sahnenin bir de kuş hâli vardır. Surenin ilk kelimesinin kökü, bir yere bağlanıp kalan kuşları adlandırır ve bunları Mekke'nin kuşları olarak anar: {ar:أوالف الطير التي بمكة, tr:evâlifu't-tayri'lletî bi-Mekke, gloss:Mekke'deki alışkın kuşlar, source:"ء ل ف,B005"}. Bunlar evlere alışmış ehli güvercinlerdir: {ar:أوالف الحمام دواجنها التي تألف البيوت, tr:evâlifu'l-hamâmi devâcinuhe'lletî te'lefu'l-buyût, gloss:güvercinlerin alışkınları evlere alışmış ehli olanlarıdır, source:"ء ل ف,B005"}, {ar:أوالف الطير ما ألفت الدار, tr:evâlifu't-tayri mâ elifeti'd-dâr, gloss:kuşların alışkınları yurda alışanlardır, source:"ء ل ف,B005"}. Kök bir yere ve onun insanlarına alışmayı, birine ısınmayı da söyler: {ar:فلان قد ألف هذا الموضع يألفه إلفا, tr:fulânun kad elife hâze'l-mevdı'a ye'lefuhû ilfen, gloss:falan bu yere alıştı, source:"ء ل ف,B005"}, {ar:ألفت فلانا إذا أنست به, tr:eliftu fulânen izâ enistu bih, gloss:ona ısındım ve yanında huzur buldum, source:"ء ل ف,B005"}. Güvercin her gün uçar ve her gün aynı eve döner; uçuşu bağın kopması değil, bağın bir parçasıdır.

Düz aktarımda iki yolculuk iki ayrı yöne açılan iki sefer gibi kalır. Bu sahne ise yolculuğu sabit bir noktanın etrafında dönen bir ritim olarak gösterir. Surenin metni de bunu destekler: iki yolculuğun mevsimi adlandırılır, ama varış yerleri hiç anılmaz; surede adı geçen tek yer {ar:هَٰذَا ٱلْبَيْتِ, tr:hâze'l-beyt, gloss:bu Ev, source:106:3}'tir. Gidilen yerler söylenmez, dönülen yer gösterilir.

Ayetlerin sırasında birinci ve ikinci ayetin îlâf kelimesi alışıp ayrılmamayı ve evlere bağlı kuşları yanında duyurur. İkinci ayetin yolculuk kelimesi konakları, taşınan evi, yerinden sökülme tehlikesini, mevsim kelimeleri de kışlak ve yazlağı taşır. Üçüncü ayette Rab kelimesi ayrılmadan kalmayı, ev kelimesi dönülen sığınağı yanında taşır. Dördüncü ayetin güven fiili konağı güvenin bulunduğu yer olarak adlandırır.

Kur'an Ev'i dönülen yer olarak tanımlar. Bakara suresinde Allah Ev'in kuruluşunu hatırlatır: {ar:وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا, tr:ve iz ce'alne'l-beyte mesâbeten li'n-nâsi ve emnâ, gloss:hani Evi insanlar için bir dönüş yeri ve güven kılmıştık, source:2:125}. Mesâbe tekrar tekrar dönülen yerdir ve aynı cümlede güvenle yan yana durur. İbrahim'in duası, soyunu Ev'in yanına yerleştirmesini anlatır: {ar:رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ, tr:rabbenâ innî eskentu min zurriyyetî bi-vâdin gayri zî zer'in inde beytike'l-muharram, gloss:Rabbimiz ben soyumdan bir kısmını ekin bitmeyen bir vadide senin dokunulmaz Evinin yanında yerleştirdim, source:14:37}, ve aynı dua insanların gönüllerinin onlara yönelmesini ister: {ar:فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ, tr:fec'al ef'ideten mine'n-nâsi tehvî ileyhim, gloss:insanlardan bir kısmının gönüllerini onlara meylettir, source:14:37}. Nahl suresinde Allah evleri hem yerleşik hem göçebe hayatın nimeti olarak sayar: {ar:وَٱللَّهُ جَعَلَ لَكُم مِّنۢ بُيُوتِكُمْ سَكَنًۭا, tr:va'llâhu ce'ale lekum min buyûtikum sekenâ, gloss:Allah size evlerinizi bir huzur yeri yaptı, source:16:80}; aynı ayetin devamı göç gününde ve konaklama gününde taşınan deri evleri anar {source:16:80}. Sebe' kıssasında ise konaklar birbirini görecek kadar yakındır: {ar:قُرًۭى ظَٰهِرَةًۭ, tr:kuran zâhira, gloss:birbirini gören kasabalar, source:34:18}.

Kaynaklar: 106:1 لِإِيلَٰفِ ء ل ف B005; 106:2 إِۦلَٰفِهِمْ ء ل ف B005; 106:2 رِحْلَةَ ر ح ل B006; 106:2 رِحْلَةَ ر ح ل B004; 106:2 رِحْلَةَ ر ح ل B007; 106:2 ٱلشِّتَآءِ ش ت و B002; 106:2 وَٱلصَّيْفِ ص ي ف B003; 106:3 رَبَّ ر ب ب B007; 106:3 ٱلْبَيْتِ ب ي ت B001; 106:4 وَءَامَنَهُم ء م ن B001; Kur'an: 2:125, 14:37, 16:80, 34:18

## Dağınıklıktan bir araya getirilmek

Bağlamanın toplu bir yüzü de vardır: dağılmış insanları yeniden bir araya getirmek. Surenin ilk kelimesinin kökü bunu doğrudan söyler: {ar:ألفت بينهم تأليفا إذا جمعت بينهم بعد تفرق, tr:elleftu beynehum te'lîfen izâ cema'tu beynehum ba'de teferruk, gloss:aralarını birleştirdim yani dağıldıktan sonra onları bir araya topladım, source:"ء ل ف,B002"}, {ar:كل شيء ضممت بعضه إلى بعض فقد ألفته تأليفا, tr:kullu şey'in damemte ba'dahû ilâ ba'din fe-kad elleftehû te'lîfâ, gloss:bir kısmını öbürüne kattığın her şeyi telif etmişsindir, source:"ء ل ف,B002"}. Aynı kök bir topluluğu bine tamamlamayı da adlandırır: {ar:آلفت القوم صيرتهم ألفا, tr:âleftu'l-kavme sayyertuhum elfâ, gloss:topluluğu bine tamamladım, source:"ء ل ف,B001"}. Bir de gönülleri yakınlaştırarak ve vererek kazanmayı: {ar:تألفته على الإسلام ومنه المؤلفة قلوبهم, tr:te'elleftuhû ale'l-islâm ve minhu'l-muellefetu kulûbuhum, gloss:onun gönlünü İslam'a ısındırdım; gönülleri ısındırılacaklar da buradandır, source:"ء ل ف,B003"}.

Rab kelimesinin kökü de kalabalıkları ve tek bir bütün hâlinde toplanmış topluluğu adlandırır: {ar:الربيون: الألوف؛ الربيون: الجماعات الكثيرة, tr:er-ribbiyyûn el-ulûf; er-ribbiyyûn el-cemâ'âtu'l-kesîre, gloss:ribbiyyûn binlercedir; ribbiyyûn kalabalık topluluklardır, source:"ر ب ب,B004"}, {ar:الرباب خمس قبائل تجمعوا, tr:er-ribâbu hamsu kabâ'ile tecemme'û, gloss:Ribâb bir araya toplanmış beş kabiledir, source:"ر ب ب,B004"}. Bu tanımın içinde "binler" anlamındaki kelimenin geçmesi bir yankıdır, iki kökü özdeşleştirmez; ama iki kelimenin aynı sahneyi, sayıca büyümüş ve birleşmiş topluluğu çağırdığını gösterir. Aynı kök bir sürüyü ve toplandığı için adlandırılmış suyu da anar: {ar:الربرب: جماعة البقر، وكذلك الإبل, tr:er-rabrabu cemâ'atu'l-bakar ve kezâlike'l-ibil, gloss:rabrab sığır sürüsüdür; deve sürüsü de öyle, source:"ر ب ب,B014"}, {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabebu ve huve'l-mâu'l-kesîr summiye bi-zâlike li'ctimâ'ih, gloss:rabeb çok sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Ev ise bu toplanmanın yeridir, {ar:مجمع الشمل, tr:mecme'u'ş-şeml, gloss:dağınığın toplandığı yer, source:"ب ي ت,B001"}. Sahnenin tersi kulluk kökünün bir kullanımında durur: her yöne dağılıp giden insan bölükleri, {ar:العباديد الفرق من الناس الذاهبون في كل وجه, tr:el-abâbîdu'l-firaku mine'n-nâsi'z-zâhibûne fî kulli vech, gloss:abâbîd her yöne giden insan bölükleridir, source:"ع ب د,B010"}.

Kabilenin adı da bu sahneye yakın durur. Arapçada {ar:تقرّش القوم, tr:tekarraşe'l-kavm, gloss:topluluk bir araya toplandı, source:"memory"} denir ve kelime toplamak ve kazanmak anlamlarında kullanılır. Bu kullanım kabile adının kökünü bir toplanma kelimesi yapar; ama bu bir yankıdır ve surenin metni bu adın anlamı üzerine bir şey söylemez.

Sahne, dağınık bir halkın bir kitleye dönüşmesi ve tek bir Ev'in etrafında bir arada tutulmasıdır. Düz aktarımın gösteremediği şey, bağlamanın yalnızca yolculukları değil insanları da bağladığıdır: iki seferi birbirine ekleyen iş, aynı zamanda dağılmaya meyilli bir topluluğu bir arada tutan iştir. Ayetlerin sırasında birinci ayetin îlâf kelimesi dağınığı toplamayı ve bine tamamlamayı, ikinci ayetin {ar:إِۦلَٰفِهِمْ, tr:îlâfihim, gloss:onların bağlayıp sürdürmesi, source:106:2} kelimesi gönül kazanmayı yanında duyurur. Üçüncü ayette Rab kelimesi kalabalıkları, sürüyü, toplanan suyu, ev kelimesi toplanma yerini, kulluk fiili de tersini, dağılan bölükleri yanında taşır.

Kur'an gönülleri birleştirmeyi Allah'ın işi olarak anlatır ve bunu surenin kelimesinin köküyle yapar. Âl-i İmrân suresinde Allah müminlere seslenir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemî'an ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sarılın ve dağılmayın, source:3:103}, ve hatırlatır: {ar:إِذْ كُنتُمْ أَعْدَآءًۭ فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًۭا, tr:iz kuntum a'dâen fe-ellefe beyne kulûbikum fe-asbahtum bi-ni'metihî ihvânâ, gloss:hani düşmanlardınız da gönüllerinizi birleştirdi ve onun nimetiyle kardeşler oldunuz, source:3:103}. Enfâl suresinde Allah Peygamber'e bu birleştirmenin satın alınamayacağını söyler: {ar:لَوْ أَنفَقْتَ مَا فِى ٱلْأَرْضِ جَمِيعًۭا مَّآ أَلَّفْتَ بَيْنَ قُلُوبِهِمْ وَلَٰكِنَّ ٱللَّهَ أَلَّفَ بَيْنَهُمْ, tr:lev enfakte mâ fi'l-ardı cemî'an mâ ellefte beyne kulûbihim ve lâkinna'llâhe ellefe beynehum, gloss:yeryüzündekilerin hepsini harcasan onların gönüllerini birleştiremezdin ama Allah aralarını birleştirdi, source:8:63}. Bağlamanın sahibi bu ayette açıkça Allah'tır. Tevbe suresindeki sadaka sayımında {ar:وَٱلْمُؤَلَّفَةِ قُلُوبُهُمْ, tr:ve'l-muellefeti kulûbuhum, gloss:gönülleri ısındırılacak olanlar, source:9:60} da aynı köktendir. Âl-i İmrân suresinde peygamberlerle birlikte savaşan kalabalıklar Rab köküyle adlandırılır: {ar:قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ, tr:kâtele me'ahû ribbiyyûne kesîr, gloss:onunla birlikte pek çok kalabalık savaştı, source:3:146}. Toplanmanın yeri olarak Ev'i de Kur'an böyle anar: {ar:إِنَّ أَوَّلَ بَيْتٍۢ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ, tr:inne evvele beytin vudı'a li'n-nâsi lellezî bi-Bekke, gloss:insanlar için kurulan ilk ev Bekke'deki evdir, source:3:96}. Tersini de Sebe' kıssası gösterir: bağlı yolculukların arasının açılmasını isteyen halk {ar:وَمَزَّقْنَٰهُمْ كُلَّ مُمَزَّقٍ, tr:ve mezzaknâhum kulle mumezzak, gloss:onları paramparça dağıttık, source:34:19} sözüyle dağıtılır.

Kaynaklar: 106:1 لِإِيلَٰفِ ء ل ف B002; 106:1 لِإِيلَٰفِ ء ل ف B001; 106:2 إِۦلَٰفِهِمْ ء ل ف B003; 106:3 رَبَّ ر ب ب B004; 106:3 رَبَّ ر ب ب B014; 106:3 رَبَّ ر ب ب B013; 106:3 ٱلْبَيْتِ ب ي ت B001; 106:3 فَلْيَعْبُدُوا۟ ع ب د B010; Kur'an: 3:103, 8:63, 9:60, 3:146, 3:96, 34:19

## Buluşmalar

Bu imgelerin en sık buluştuğu yer ikinci ayetin yolculuk kelimesidir. Aynı kök hem yola koyulmayı, hem semeri ve bineği, hem de iki konak arasındaki merhaleyi adlandırır; yani bağlanan iki yolculuk, onları taşıyan hayvan ve yolun bölündüğü konaklar tek bir kelimenin içinde tek bir güzergâhtır. Sebe' kıssasındaki ayet bu üçünü birden sahneler: birbirini gören kasabalar, ölçülüp bölünmüş yürüyüş ve güven içinde geçen geceler ve günler {source:34:18}.

Kış kelimesi bağlanmış yolculuk ile boş mideyi tek sahnede tutar. Kışın bir adı kıtlık olduğu için {source:"ش ت و,B004"}, kış yolculuğu aynı zamanda açlığa karşı yapılan yolculuktur; yaz kelimesinin sâifesi de eve getirilen erzaktır {source:"ص ي ف,B003"}. Böylece ikinci ayet, dördüncü ayetin açlığını ve doyurmasını kendi mevsim adlarının içinde önceden taşır. Binek de bu iki sahneyi birleştirir: zayıflıktan sonra semirip yolculuğa güç yetiren deve {ar:أرحلت الإبل سمنت بعد هزال فأطاقت الرحلة, tr:erhaleti'l-ibilu seminet ba'de huzâlin fe-etâkati'r-rihle, gloss:develer zayıflıktan sonra semirdi de yolculuğa güç yetirir oldu, source:"ر ح ل,B005"}, yolculuk kökünün içindeki bir "açlıktan doyurulma"dır ve dördüncü ayetin insanlar için söylediğini hayvanda gösterir. Güvenilir dişi deve {source:"ء م ن,B001"} ile bineği tükenip yolda kalan yolcu {source:"ع ب د,B011"} da binek sahnesini korku sahnesine bağlar: güven bineğin sırtında başlar.

Katranlanmış deve üç imgeyi tek bir nesnede toplar. {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-mu'abbedu'l-mehnû'u bi'l-katırâni'l-muzellel, gloss:katranla sıvanmış ve uysallaşmış deve, source:"ع ب د,B005"} ifadesinde katran hem kaplamadır hem yatıştırmanın aracıdır, hayvan da kervanın bineğidir. Bu uysallık sahnesi evin efendisi sahnesine kulluğun tanımıyla geçer: kulluk alçalmanın son derecesi olduğuna göre {source:"ع ب د,B003"}, yolun ve hayvanın yolcuya boyun eğmesi, kulun efendisine boyun eğmesiyle aynı kelimeyle söylenir. Zuhruf suresinde bu geçiş bir hareket hâlinde görülür: boyun eğdirilmiş bineğin sırtına yerleşen kişi Rabbinin nimetini anar {source:43:13}.

Korunan yol ile korkunun giderilmesi aynı sahnenin iki yanıdır. Korkulan yolda korkutan eşkıyadır {source:"خ و ف,B002"}, güven ise verilen amandır {source:"ء م ن,B001"}; Ankebût ve Kasas surelerinde güvenli harem ile çevresinde kapılıp götürülen insanlar aynı ayette durur {source:29:67}, {source:28:57}. Surenin ilk kelimesi de bu iki yanı kendi içinde birleştirir: aynı îlâf hem iki yolculuğu birbirine bağlamak {source:"ء ل ف,B004"} hem de himaye vermektir {ar:يؤلفون يجيرون, tr:yu'lifûne yucîrûn, gloss:himaye verirler, source:"ء ل ف,B004"}. Tek kelime, halkayı ve halkayı açık tutan güvenceyi birlikte adlandırır. Yaz kelimesinde de benzer bir kesişme vardır: yaz yolculuğunun mevsimini adlandıran kök, zararın döndürülmesini ve hedeften sapan oku da adlandırır {source:"ص ي ف,B005"}, ve Mushaf'ta hemen önceki sure Ev'in Rabbinin bir saldırının tuzağını boşa çıkarışını anlatır {source:105:2}.

Konaklar, evlere alışmış kuşlar ve dağınıklıktan toplanma, ev kelimesinin tek bir tanımında buluşur: sığınak, dönülen yer ve dağınığın toplandığı yer {source:"ب ي ت,B001"}. Yolcu oraya döner, güvercin oraya döner, dağınık topluluk orada toplanır; Rab kökünün bir yerde ayrılmadan kalma anlamı {source:"ر ب ب,B007"} bu üç dönüşün hepsinin yönünü verir. Bakara suresi Ev'i hem dönüş yeri hem güven olarak tek cümlede tanımlar {source:2:125}. Toplanma ile yolculuk arasındaki bağı yine îlâfın iki kullanımı kurar: dağılmış insanları bir araya getirmek {source:"ء ل ف,B002"} ile iki yolculuğu bir araya getirmek {source:"ء ل ف,B004"} aynı işlemdir. Sebe' kıssası bu ikisinin birlikte çözülüşünü gösterir: seferlerinin arasını açmak isteyen halk, kendisi paramparça dağıtılır {source:34:19}.

Boş mide ile korkunun giderilmesi birbirine paralel iki karşıtlıktır: açlık tokluğun karşıtı {source:"ج و ع,B001"}, güven korkunun karşıtıdır {source:"ء م ن,B001"}. Kur'an bu iki karşıtlığı birlikte tersine çevirir: nankörlük eden kasabaya {ar:لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ, tr:libâse'l-cû'i ve'l-havf, gloss:açlık ve korku elbisesi, source:16:112} tattırılır; İbrahim ise güveni ve rızkı birlikte ister {source:2:126}. Yağmur zinciri de boş mide sahnesine bağlanır: buluttan yağmura, yağmurdan otlağa uzanan zincirin Mekke vadisinde kırık olması {source:14:37}, yolculuğu ve doyuranı gerekli kılan boşluktur.

Korkunun giderilmesi ile evin efendisi, kulluk ile güven arasındaki sırada buluşur. Nûr suresindeki vaatte korkunun ardından güven, güvenin ardından kulluk gelir {source:24:55}; surenin üçüncü ayetindeki emir ile dördüncü ayetindeki güven aynı ilişkiyi kurar, yalnız sure güveni geçmiş zamanda, verilmiş bir şey olarak anar ve kulluğu onun karşılığı olarak ister. Evin efendisinin sahip olma ve büyütme yüzleri ise aynı hanenin başında birleşir: hem evin sahibidir hem evin halkını adım adım tamamlayandır, ve ev kelimesinin aile halkı anlamı {source:"ب ي ت,B002"} iki yüzün de muhatabıdır.

Bu buluşmalar surenin hareketini taşır. İlk iki ayet bir halka gösterir: iki zıt mevsimin yolculuğu, bineğiyle, konaklarıyla, himayesiyle birbirine eklenmiş ve bir topluluğun alışkanlığı olmuştur. Bu halka ilk bakışta Kureyş'in kendi işi gibi görünür, çünkü îlâf onlara nispet edilir. Üçüncü ayet, birinci ayetin açık bıraktığı "için" bağlantısını bir emirle kapatır ve bütün halkanın döndüğü sabit noktayı, bu Ev'i, ve o Ev'in sahibini gösterir. Dördüncü ayet ise halkanın iki ucunu, kışın adındaki açlığı ve yoldaki korkuyu, o sahibin iki işi olarak adlandırır: doyurmak ve emin kılmak. Böylece bağlama, alışkanlık, binek ve yol, Ev'in Rabbinin kendi halkı için kurduğu düzenin parçaları olarak yeniden okunur ve kulluk emri, o düzenden yararlanan halkın, onu kurana yönelmesi olarak yerini bulur.

