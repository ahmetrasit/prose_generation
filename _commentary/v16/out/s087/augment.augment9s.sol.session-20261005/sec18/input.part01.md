Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 18 of 18 ("Buluşmalar"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.

===== _commentary/v16/prompts/augment9s/augment.md =====
You are completing a finished Turkish commentary on the images of a surah,
written by another reader, with what the Quran itself says about it: the Quran
explaining the Quran. Below are one image section of that commentary, with its
prose paragraphs numbered [¶n] as in the whole commentary; the commentary's
ledger; and Quran passages from an image-based discovery list (two readers'
judgements of which ayat this image activates), each with its Arabic, its tier,
the bases given for it, and the paragraphs of the section that already cite it,
if any. A tier is that list's own judgement, not yours; the list is not
authoritative and may be incomplete.

Read the section first. Then judge every listed passage, one by one, against
every paragraph of the section: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the ayat the paragraph reads leave
unnamed. A shared word or root alone
does not make it relevant; the link must hold in what the passage says. A
passage is never added to a paragraph that already cites it. Judge it against
every other paragraph as if it were new: "already cited" is never a reason for
"not relevant". A paragraph that points to a passage without citing it ("başka
bir surede") takes that passage as a reference. If a passage shows that
something a paragraph says is wrong, do not add it: give it the verdict
"conflict ¶n" with what it shows. A passage that qualifies what a paragraph says
without showing it wrong is a reference whose link says what it adds.

The commentary's ledger names what its writer weighed and left out, and why.
Such a passage may still be added when it is relevant; its verdict then answers
the writer's reason.

Then go through the section paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; the other places where the image's scene,
object or act is staged, with or without a shared word; ayat that state the same thing in other
words; passages that stage the same act, scene, speaker or stance without
sharing a word; the neighbouring ayat (within two) of every passage it cites
(the list includes the nearest of them as a tier of their own) and of every
passage you add; and the passages the ledger names as weighed and left out.
Every ayah you look up gets a verdict.

There is no limit on the number of additions. Leaving out what is not relevant
is part of the work; adding what is not relevant weakens the commentary.

Every relevant passage is added to its paragraph in one of two forms.
- Prose, when the passage changes how the paragraph is understood: give its
  speaker and its situation only as the Quran itself tells them there and in
  the neighbouring ayat; the mechanism of the link (a shared root used in the
  same sense, the same construction, the same scene or speaker, a contrast, a
  completion, an order of events, a name for what the paragraph leaves
  unnamed); and what it adds. As long as the link needs and no longer.
- Reference, when the passage supports or parallels the paragraph without
  changing it: its source with the link in a few words, gathered in the
  paragraph's one reference line. The link names its mechanism: what in the
  passage meets what in the paragraph ("korkan için indirilen hatırlatma",
  not "aynı ifade", "aynı emir" or "aynı soru"). The test of relevance holds
  for references as for prose: a passage that shares only a word with the
  paragraph is not relevant. A wording the Quran repeats in several ayat (a
  refrain) is one reference: all its places together, then one link, e.g.
  {source:54:17} {source:54:22} {source:54:32} {source:54:40} <the link>.
  Consecutive ayat that one link covers are one reference too:
  {source:88:21} {source:88:22} <the link>.
A passage relevant to several paragraphs gets its prose once, where it changes
the understanding most, and a reference in the others. A passage the
commentary already explains in one of its paragraphs is a reference in any
other paragraph it is relevant to.

The additions are placed by the script after their paragraph, each prose
addition as a paragraph of its own and the reference line last; the
commentary's paragraphs are not touched, and the additions can be shown or
hidden together. So each prose addition opens from the paragraph it serves,
without repeating it, and stands on its own: it never leans on another
addition. It stops when the link is made: no formula opener such as "Kur'an bu … başka bir yerde de …", and no
closing sentence that sums up or draws the lesson.

Where the Quran does not name the speaker, or who is meant is disputed (the
speaker of 12:52-53; the two told to go down in 20:123), say only what the ayah
says, without naming anyone. Name another surah by its name ("Tâhâ
suresinde"); "aynı sure" and "bu sure" mean only the surah of the commentary.

Never change or contradict the commentary, and never restate its explanations:
citing a passage the commentary cites in another paragraph is not restating,
repeating what the commentary says about it is. Turkish prose in the commentary's register, warm and direct; explain, do
not dramatize; no first person and no talk about sources or process (no
"sözlük", "harita", "zincir", "liste", no mention of the list or the commentary
itself). Every Arabic quotation goes in the reader tag with its source, the one
ayah that holds the quoted words:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:<surah:ayah>}
A passage named without quoting it gets the source alone: {source:<surah:ayah>}.
For a listed passage, copy its Arabic letter for letter from the list; for any
other passage, read its Arabic with the lookup described above the brief before
you quote it, or name it by its source alone. Never
invent a sense, source, speaker, situation or citation. Use no hadith, no
exegetes' views and no report from outside the Quran (no occasion of
revelation, no name the Quran does not give, no date).

Output only this, with no preamble, notes or summary. For each prose addition, a block:
=== ADD ===
paragraph: <n>
ref: <surah:ayah>
text: <the addition, on one line>
For each paragraph that has references, one block:
=== REFS ===
paragraph: <n>
text: Ayrıca: {source:<surah:ayah>} <the link, naming its mechanism>; {source:<surah:ayah>} {source:<surah:ayah>} <one link for a refrain>; …
Then a line containing only
=== VERDICTS ===
then one line for every listed passage, in the list's order, and one for every
passage from your own knowledge that you weighed, marked "own". Paragraph
numbers are the ones shown: only this section's paragraphs may be served.
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 18 (prose paragraphs numbered) =====
[¶68] İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

[¶69] İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

[¶70] Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

[¶71] Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

[¶72] Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

[¶73] Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (333) =====
## strong (263)

- (2:125) [terra: strong (missing-ayat turn); basis: root+scene+theme] وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا وَٱتَّخِذُوا۟ مِن مَّقَامِ إِبْرَٰهِۦمَ مُصَلًّۭى ۖ وَعَهِدْنَآ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ أَن طَهِّرَا بَيْتِىَ لِلطَّآئِفِينَ وَٱلْعَٰكِفِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ
  Unverified discovery rationale: terra: Abraham's station is made a place of prayer and Abraham and Ishmael are commanded to purify the House for worshippers, joining Abraham, prayer, and purification.
- (2:130) [terra: strong (missing-ayat turn); basis: root+theme] وَمَن يَرْغَبُ عَن مِّلَّةِ إِبْرَٰهِۦمَ إِلَّا مَن سَفِهَ نَفْسَهُۥ ۚ وَلَقَدِ ٱصْطَفَيْنَٰهُ فِى ٱلدُّنْيَا ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
  Unverified discovery rationale: terra: God chose Abraham in the world and he is righteous in the Hereafter, joining prophetic selection to the two lives.
- (2:200) [terra: strong (missing-ayat turn); basis: root+theme] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: terra: After a command to remember God, some people ask only for this world and consequently have no share in the Hereafter, joining remembrance, preference, and portion.
- (2:201) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: Others ask for good in both this world and the Hereafter and protection from fire, stating the prayer of the alternative branch.
- (2:202) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: terra: Those people receive a share of what they earned, completing the passage's corrected meaning of allotment.
- (2:239) [terra: strong (missing-ayat turn); basis: root+scene+theme] فَإِنْ خِفْتُمْ فَرِجَالًا أَوْ رُكْبَانًۭا ۖ فَإِذَآ أَمِنتُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَمَا عَلَّمَكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
  Unverified discovery rationale: terra: Prayer continues even under fear, and after safety believers must remember God for what He taught them, joining fear, prayer, teaching, and remembrance.
- (2:261) [luna: strong; basis: scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: Spending in God’s way is likened to a grain producing seven spikes, each with a hundred grains; this supplies the section’s cultivated, multiplying field for lasting good.
- (3:6) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: God forms people in the wombs as He wills; the source wording at 87:2 is فَسَوَّىٰ, so this ayah repeats the forming root in the very bodily setting the section develops. | terra: God forms people in the wombs however He wills, directly joining bodily fashioning to divine choice.
- (3:145) [terra: strong (missing-ayat turn); basis: root+theme] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
  Unverified discovery rationale: terra: Death occurs only by God's permission at a fixed term, and whoever desires worldly or otherworldly reward receives a share; measure, choice, death, and allotted portion meet.
- (4:32) [terra: strong (missing-ayat turn); basis: root+theme] وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ ۚ لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبُوا۟ ۖ وَلِلنِّسَآءِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبْنَ ۚ وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
  Unverified discovery rationale: terra: People are told not to covet the preference God gives others; men and women each have a share of what they earn, directly joining preference to allotted share.
- (6:141) [luna: strong; terra: strong; basis: scene+theme] ۞ وَهُوَ ٱلَّذِىٓ أَنشَأَ جَنَّٰتٍۢ مَّعْرُوشَٰتٍۢ وَغَيْرَ مَعْرُوشَٰتٍۢ وَٱلنَّخْلَ وَٱلزَّرْعَ مُخْتَلِفًا أُكُلُهُۥ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُتَشَٰبِهًۭا وَغَيْرَ مُتَشَٰبِهٍۢ ۚ كُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
  Unverified discovery rationale: luna: God brings forth trellised and untended gardens, crops, and fruit, then commands that its due be given on harvest day; this meets the section’s worked field, growing produce, and portion paid. | terra: Cultivated gardens and crops grow, their fruit is eaten, and their due is given on harvest day; this is the worked field and paid right set against abandoned grass.
- (7:120) [terra: strong; basis: scene] وَأُلْقِىَ ٱلسَّحَرَةُ سَٰجِدِينَ
  Unverified discovery rationale: terra: In another telling, the magicians are cast down in prostration, directly repeating the bodily act through which the section's group makes its choice.
- (7:121) [terra: strong; basis: neighbour+scene+speaker] قَالُوٓا۟ ءَامَنَّا بِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The prostrate magicians declare faith in the Lord of the worlds, linking their response to the same divine title glorified at Moses' fire.
- (7:122) [terra: strong; basis: neighbour+scene] رَبِّ مُوسَىٰ وَهَٰرُونَ
  Unverified discovery rationale: terra: They identify that Lord as the Lord of Moses and Aaron, fixing the confession in the same Musa narrative rather than as a generic prostration.
- (7:123) [terra: strong; basis: scene+theme] قَالَ فِرْعَوْنُ ءَامَنتُم بِهِۦ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّ هَٰذَا لَمَكْرٌۭ مَّكَرْتُمُوهُ فِى ٱلْمَدِينَةِ لِتُخْرِجُوا۟ مِنْهَآ أَهْلَهَا ۖ فَسَوْفَ تَعْلَمُونَ
  Unverified discovery rationale: terra: Pharaoh objects that they believed before his permission and accuses them of conspiracy, repeating the worldly ruler's attempt to own their choice.
- (7:124) [terra: strong; basis: neighbour+scene+theme] لَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ ثُمَّ لَأُصَلِّبَنَّكُمْ أَجْمَعِينَ
  Unverified discovery rationale: terra: Pharaoh threatens mutilation and crucifixion, giving the temporal punishment against which the magicians choose the Lord's lasting judgment.
- (7:125) [terra: strong; basis: scene+theme] قَالُوٓا۟ إِنَّآ إِلَىٰ رَبِّنَا مُنقَلِبُونَ
  Unverified discovery rationale: terra: The magicians answer that they are returning to their Lord, stating why Pharaoh's worldly threat cannot be the enduring end.
- (7:126) [terra: strong; basis: scene+speaker+theme] وَمَا تَنقِمُ مِنَّآ إِلَّآ أَنْ ءَامَنَّا بِـَٔايَٰتِ رَبِّنَا لَمَّا جَآءَتْنَا ۚ رَبَّنَآ أَفْرِغْ عَلَيْنَا صَبْرًۭا وَتَوَفَّنَا مُسْلِمِينَ
  Unverified discovery rationale: terra: They ask for patience and to die in submission because their only offense was belief in the signs, resolving the threatened death through faithful prayer.
- (7:143) [terra: strong (missing-ayat turn); basis: scene+speaker+theme] وَلَمَّا جَآءَ مُوسَىٰ لِمِيقَٰتِنَا وَكَلَّمَهُۥ رَبُّهُۥ قَالَ رَبِّ أَرِنِىٓ أَنظُرْ إِلَيْكَ ۚ قَالَ لَن تَرَىٰنِى وَلَٰكِنِ ٱنظُرْ إِلَى ٱلْجَبَلِ فَإِنِ ٱسْتَقَرَّ مَكَانَهُۥ فَسَوْفَ تَرَىٰنِى ۚ فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ جَعَلَهُۥ دَكًّۭا وَخَرَّ مُوسَىٰ صَعِقًۭا ۚ فَلَمَّآ أَفَاقَ قَالَ سُبْحَٰنَكَ تُبْتُ إِلَيْكَ وَأَنَا۠ أَوَّلُ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: At the mountain encounter Moses falls unconscious, then glorifies God and repents when he revives; Mosaic revelation, height, and glorification meet in one scene.
- (7:144) [terra: strong; basis: root+scene+theme] قَالَ يَٰمُوسَىٰٓ إِنِّى ٱصْطَفَيْتُكَ عَلَى ٱلنَّاسِ بِرِسَٰلَٰتِى وَبِكَلَٰمِى فَخُذْ مَآ ءَاتَيْتُكَ وَكُن مِّنَ ٱلشَّٰكِرِينَ
  Unverified discovery rationale: terra: God tells Moses that He chose him over people through His messages and speech, an explicit counterpart to the fire-side selection.
- (7:187) [terra: strong (missing-ayat turn); basis: theme] يَسْـَٔلُونَكَ عَنِ ٱلسَّاعَةِ أَيَّانَ مُرْسَىٰهَا ۖ قُلْ إِنَّمَا عِلْمُهَا عِندَ رَبِّى ۖ لَا يُجَلِّيهَا لِوَقْتِهَآ إِلَّا هُوَ ۚ ثَقُلَتْ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ لَا تَأْتِيكُمْ إِلَّا بَغْتَةًۭ ۗ يَسْـَٔلُونَكَ كَأَنَّكَ حَفِىٌّ عَنْهَا ۖ قُلْ إِنَّمَا عِلْمُهَا عِندَ ٱللَّهِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
  Unverified discovery rationale: terra: Knowledge of the Hour belongs only to the Lord; it is heavy and comes suddenly, supplying the fuller Quranic context for the Hour kept hidden at Moses' fire.
- (8:45) [terra: strong (missing-ayat turn); basis: root+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا لَقِيتُمْ فِئَةًۭ فَٱثْبُتُوا۟ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: terra: Believers facing an enemy are told to stand firm and remember God much so that they may prosper, joining remembrance directly to falah.
- (9:103) [terra: strong; basis: root+speaker+theme] خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
  Unverified discovery rationale: terra: Charity purifies and develops believers, and the Prophet is told to pray for them, placing purification and prayer in one command.
- (10:24) [luna: strong; terra: medium; basis: contrast+scene+theme] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: Worldly life is likened to rain-grown plants that adorn the earth, then are cut down as if they had not flourished; this is a full parallel to the section’s pasture that grows and then becomes debris. | terra: Worldly life is rain-mixed vegetation that flourishes and is suddenly made a reaped field, a specific parallel to the pasture whose apparent life passes.
- (11:15) [terra: strong (missing-ayat turn); basis: neighbour+theme] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
