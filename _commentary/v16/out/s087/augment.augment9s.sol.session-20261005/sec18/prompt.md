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
  Unverified discovery rationale: terra: Those who desire worldly life and its adornment may receive the fruits of their deeds here, defining the preferred near-life branch.
- (11:16) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: Nothing awaits that branch in the Hereafter except fire and its worldly work comes to nothing, joining bad preference to the passing of apparent benefit.
- (11:40) [terra: strong (missing-ayat turn); basis: scene+theme] حَتَّىٰٓ إِذَا جَآءَ أَمْرُنَا وَفَارَ ٱلتَّنُّورُ قُلْنَا ٱحْمِلْ فِيهَا مِن كُلٍّۢ زَوْجَيْنِ ٱثْنَيْنِ وَأَهْلَكَ إِلَّا مَن سَبَقَ عَلَيْهِ ٱلْقَوْلُ وَمَنْ ءَامَنَ ۚ وَمَآ ءَامَنَ مَعَهُۥٓ إِلَّا قَلِيلٌۭ
  Unverified discovery rationale: terra: The flood sign begins when the oven gushes, so a vessel associated with fire becomes the source of overwhelming water in a striking meeting of the section's two scenes.
- (13:8) [terra: strong; basis: root+scene+theme] ٱللَّهُ يَعْلَمُ مَا تَحْمِلُ كُلُّ أُنثَىٰ وَمَا تَغِيضُ ٱلْأَرْحَامُ وَمَا تَزْدَادُ ۖ وَكُلُّ شَىْءٍ عِندَهُۥ بِمِقْدَارٍ
  Unverified discovery rationale: terra: God knows every pregnancy and what wombs diminish or increase, and everything with Him has a measure; womb, hidden knowledge, and measure meet in one ayah.
- (13:17) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶69] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
  Unverified discovery rationale: luna: The section sets the pasture that becomes source-word غُثَاءً beside the foam borne by a flood and the foam of smelting; this ayah says foam vanishes while what benefits people remains, giving the section’s passing-versus-lasting landscape its full truth/falsehood frame. | terra: The measured rain fills valleys according to their capacity, flood and smelting produce foam, the scum passes, and what benefits people remains; one ayah therefore gathers the section's measure, pasture-debris, fire, benefit, and permanence.
- (14:17) [luna: strong; terra: strong; basis: contrast+scene+theme] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
  Unverified discovery rationale: luna: In the punishment, death comes to the drinker from every side yet he does not die; this is a distinct elaboration of the section’s suspended “neither dies nor lives” condition. | terra: The condemned person has death coming from every side yet does not die, another precise Quranic rendering of the section's impossible state in fire.
- (14:35) [luna: strong; terra: strong; basis: root+scene+speaker+theme] وَإِذْ قَالَ إِبْرَٰهِيمُ رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ
  Unverified discovery rationale: luna: Abraham asks his Lord to keep him and his children away from idol worship; this is the specific Abrahamic prayer that the section says its closing reference to earlier pages recalls. | terra: Abraham asks his Lord to keep him and his children away from worshipping idols, the specific Abrahamic prayer the section hears behind the first scrolls and avoidance.
- (14:37) [terra: strong; basis: scene+speaker+theme] رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ
  Unverified discovery rationale: terra: Abraham settles his family in an uncultivated valley so they may establish prayer and asks that they receive fruits, joining barren land, prayer, inclination, and provision.
- (14:38) [terra: strong; basis: neighbour+speaker+theme] رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
  Unverified discovery rationale: terra: Within Abraham's prayer, God knows what people conceal and disclose, echoing the section's divine knowledge of hidden and open things.
- (14:40) [luna: strong; terra: strong; basis: neighbour+speaker+theme] رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ
  Unverified discovery rationale: luna: Abraham asks to be made an establisher of prayer, together with his descendants; it meets the section’s prayer-and-remembrance command received by Moses and its closing appeal to Abraham’s pages. | terra: Abraham asks to be made an establisher of prayer together with his descendants, completing the prayer behind the section's mention of his pages.
- (15:21) [terra: strong; basis: root+scene+theme] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: terra: God's treasuries are inexhaustible, but He sends each thing down only in a known measure, clarifying measured provision from what remains hidden.
- (15:29) [terra: strong (missing-ayat turn); basis: root+scene+theme] فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ
  Unverified discovery rationale: terra: After God fashions the human and breathes spirit into him, the angels must prostrate, joining bodily craft to prostration.
- (16:10) [luna: strong (missing-ayat turn); basis: root+scene] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
  Unverified discovery rationale: luna: Rain from the sky supplies drink and vegetation “in which you pasture” (تُسِيمُونَ); this is a direct rain-and-pasture formulation alongside the source pasture wording at 87:4.
- (16:96) [terra: strong; basis: root+theme] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: What people possess runs out while what is with God remains, stating in bare form the section's distinction between passing scum and lasting benefit.
- (16:121) [terra: strong (missing-ayat turn); basis: root+scene+theme] شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: terra: God chose Abraham and guided him to a straight path, pairing chosenness and guidance in the other prophet named by the section's final ayah.
- (17:18) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+scene+theme] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
  Unverified discovery rationale: luna: Whoever desires the immediate life is given some of it, then faces Hell; this develops the section’s warning about preferring near life. | terra: Whoever chooses the immediate life receives a measured portion and then reaches Hell, joining preference, allotment, and fire.
- (17:19) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+theme] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
  Unverified discovery rationale: luna: Whoever desires the Hereafter and strives for it as a believer has an appreciated effort; this supplies the section’s other side of the choice and its lasting reward. | terra: Whoever chooses the Hereafter and strives for it in faith has that striving appreciated, completing the opposite branch of the choice.
- (17:21) [terra: strong; basis: root+theme] ٱنظُرْ كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۚ وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًۭا
  Unverified discovery rationale: terra: God's worldly preferences between people are surpassed by the Hereafter's greater degrees and greater preference, joining allotment, selection, and height.
- (17:107) [terra: strong (missing-ayat turn); basis: scene+theme] قُلْ ءَامِنُوا۟ بِهِۦٓ أَوْ لَا تُؤْمِنُوٓا۟ ۚ إِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مِن قَبْلِهِۦٓ إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًۭا
  Unverified discovery rationale: terra: Those previously given knowledge fall on their faces in prostration when revelation is recited, paralleling the magicians' immediate bodily response to truth.
- (17:108) [terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
  Unverified discovery rationale: terra: While prostrate they glorify their Lord and affirm His promise, joining recited revelation to glorification.
- (17:109) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
  Unverified discovery rationale: terra: They fall down weeping and the recitation increases their humility, completing the posture of receptive remembrance.
- (18:45) [luna: strong; terra: strong; basis: contrast+scene+theme] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
  Unverified discovery rationale: luna: The worldly-life parable ends with vegetation becoming dry stubble scattered by wind; this repeats the section’s withered pasture and makes its passing quality explicit. | terra: Worldly life is likened to rain-grown vegetation that becomes dry fragments scattered by wind, the section's explicit meeting of the preferred lower life with spent pasture.
- (18:46) [luna: strong; terra: strong; basis: contrast+neighbour+root+scene+theme] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
  Unverified discovery rationale: luna: Wealth and children are the adornment of worldly life, but lasting good deeds are better with the Lord; this gives the section’s “what remains” a concrete human counterpart. | terra: Immediately after the dried vegetation, enduring good deeds are better in reward and hope; this ayah supplies the lasting selection on the other side of 18:45.
- (19:51) [terra: strong; basis: root+scene+theme] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مُوسَىٰٓ ۚ إِنَّهُۥ كَانَ مُخْلَصًۭا وَكَانَ رَسُولًۭا نَّبِيًّۭا
  Unverified discovery rationale: terra: Moses is described as chosen and as a messenger-prophet, confirming chosenness as a defining feature of his encounter.
- (19:52) [terra: strong; basis: neighbour+scene+theme] وَنَٰدَيْنَٰهُ مِن جَانِبِ ٱلطُّورِ ٱلْأَيْمَنِ وَقَرَّبْنَٰهُ نَجِيًّۭا
  Unverified discovery rationale: terra: God calls Moses from the right side of the mount and brings him near for intimate speech, another concise version of approach becoming revelation.
- (19:76) [terra: strong (missing-ayat turn); basis: root+theme] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
  Unverified discovery rationale: terra: God increases the guided in guidance, while enduring good deeds are better in reward and return, joining guidance to what lasts.
- (19:97) [terra: strong (missing-ayat turn); basis: root+speaker+theme] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لِتُبَشِّرَ بِهِ ٱلْمُتَّقِينَ وَتُنذِرَ بِهِۦ قَوْمًۭا لُّدًّۭا
  Unverified discovery rationale: terra: The Quran is eased in the Prophet's tongue to give good news to the God-fearing and warn opponents, combining ease, speech, fear, and warning.
- (20:10) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶68] إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى
  Unverified discovery rationale: luna: The source wording from 87:12 is entering the fire, while Moses at a fire seen from afar hopes to find هُدًى there; its fire directs him toward a guide rather than consuming him. | terra: Moses sees a fire from afar and approaches hoping for a brand or guidance at it, the exact meeting through which the section turns threatening fire into a road.
- (20:11) [terra: strong; basis: neighbour+scene] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
  Unverified discovery rationale: terra: Moses reaches the fire and is called by name; this row contributes the actual arrival and call between the sight in 20:10 and the selection in 20:13.
- (20:12) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
  Unverified discovery rationale: luna: This ayah places Moses at the sacred valley of Tuwa and tells him to remove his sandals; linked to 20:13–14, it supplies the consecrated setting for the section’s fire-side choosing and prayer command. | terra: At the fire Moses learns that the caller is his Lord and that he stands in the sacred valley of Tuwa, fixing the section's meeting in its revealed place.
- (20:13) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶68] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
  Unverified discovery rationale: luna: The source quote “I have chosen you” (وَأَنَا ٱخْتَرْتُكَ) is spoken to Moses at the fire; it places divine selection inside the same journey that the section compares with choosing a lasting life. | terra: At the fire God says that He has chosen Moses and commands him to listen, grounding the section's claim that selection is the first gift at this fire.
- (20:14) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶68] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
  Unverified discovery rationale: luna: At that encounter Moses is told to establish prayer “for My remembrance” (لِذِكْرِىٓ); the section pairs this command with 87:15’s remembrance of the Lord and prayer. | terra: The fire-side revelation commands Moses to worship God and establish prayer for His remembrance, directly joining the section's prayer and remembering scenes.
- (20:15) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶68] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
  Unverified discovery rationale: luna: The fire-call continues with the Hour’s coming and God’s nearly concealing it (أَكَادُ أُخْفِيهَا); that hidden judgment sharpens the section’s account of what God knows as hidden and what choice leads toward. | terra: The coming Hour is almost kept hidden so every soul may be repaid for its striving; this is the hidden reality the section places after prayer at the fire.
- (20:16) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+speaker+theme] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
  Unverified discovery rationale: luna: Moses is told not to be turned from the Hour by one who disbelieves and follows desire; this gives a concrete counterpart to the section’s warning about preferring near life. | terra: After the hidden Hour, Moses is warned not to be diverted by one who denies it and follows desire; this supplies the bad preference that resists the concealed reckoning.
- (20:33) [luna: strong (missing-ayat turn); basis: speaker+theme] كَىْ نُسَبِّحَكَ كَثِيرًۭا
  Unverified discovery rationale: luna: Moses says that he and Aaron may glorify God greatly (نُسَبِّحَكَ كَثِيرًا); this is a further Moses-scene meeting with the section’s opening command to glorify the Lord.
- (20:34) [luna: strong (missing-ayat turn); basis: speaker+theme] وَنَذْكُرَكَ كَثِيرًا
  Unverified discovery rationale: luna: Moses says that he and Aaron may remember God greatly (وَنَذْكُرَكَ كَثِيرًا); this joins the section’s remembrance command to its distinct prayer-and-remembrance scene at the fire.
- (20:40) [terra: strong; basis: root+scene+theme] إِذْ تَمْشِىٓ أُخْتُكَ فَتَقُولُ هَلْ أَدُلُّكُمْ عَلَىٰ مَن يَكْفُلُهُۥ ۖ فَرَجَعْنَٰكَ إِلَىٰٓ أُمِّكَ كَىْ تَقَرَّ عَيْنُهَا وَلَا تَحْزَنَ ۚ وَقَتَلْتَ نَفْسًۭا فَنَجَّيْنَٰكَ مِنَ ٱلْغَمِّ وَفَتَنَّٰكَ فُتُونًۭا ۚ فَلَبِثْتَ سِنِينَ فِىٓ أَهْلِ مَدْيَنَ ثُمَّ جِئْتَ عَلَىٰ قَدَرٍۢ يَٰمُوسَىٰ
  Unverified discovery rationale: terra: God recounts Moses' rescues and says that he came at an appointed measure, bringing divine measure into the very life that later reaches the fire.
- (20:41) [terra: strong; basis: root+scene+theme] وَٱصْطَنَعْتُكَ لِنَفْسِى
  Unverified discovery rationale: terra: God says that He fashioned or chose Moses for Himself, reinforcing the section's meeting between skilled formation and divine selection.
- (20:42) [terra: strong; basis: root+speaker+theme] ٱذْهَبْ أَنتَ وَأَخُوكَ بِـَٔايَٰتِى وَلَا تَنِيَا فِى ذِكْرِى
  Unverified discovery rationale: terra: Moses and Aaron are sent with God's signs and told not to slacken in His remembrance, extending the fire-side command into their mission.
- (20:44) [terra: strong; basis: root+speaker+theme] فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ
  Unverified discovery rationale: terra: They must speak gently to Pharaoh so that he may remember or fear, directly anticipating the section's person who takes reminder through fear.
- (20:50) [luna: strong; terra: strong; basis: root+scene+theme] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
  Unverified discovery rationale: luna: Moses answers Pharaoh that their Lord gave each thing its form and then guided it; that sequence directly meets the section’s “created, proportioned” and “measured, guided” account of the Lord’s work. | terra: Moses describes the Lord as the One who gave everything its created form and then guided it, a compact parallel to creating, fashioning, measuring, and guiding.
- (20:52) [luna: strong; basis: contrast+theme] قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى
  Unverified discovery rationale: luna: Moses says his Lord neither errs nor forgets (لَا يَضِلُّ رَبِّى وَلَا يَنسَىٰ); against the section’s “you will not forget, except what God wills,” this locates forgetting in the human reciter, not God’s knowledge.
- (20:53) [luna: strong (missing-ayat turn); basis: scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
  Unverified discovery rationale: luna: In Moses’s account, God makes the earth a resting place and roads, sends water down, and brings out varied plants; this passage joins the Moses thread to the section’s pasture, rain, and guidance images.
- (20:54) [luna: strong (missing-ayat turn); basis: neighbour+scene+theme] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
  Unverified discovery rationale: luna: The plants are food for people and pasture for their livestock; 20:53 contributes the earth, rain, and growth, while this ayah specifies who benefits from the growth.
- (20:70) [terra: strong; basis: scene+theme] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
  Unverified discovery rationale: terra: The magicians are cast down in prostration and declare faith, beginning the communal choice that the section reads beside purification and prayer.
- (20:71) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶70] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
  Unverified discovery rationale: luna: Pharaoh threatens the sorcerers with a harsher, more lasting punishment; the section specifically meets this claim with their rejection and their declaration that God is better and more lasting. | terra: Pharaoh threatens the believing magicians and claims that his punishment is more severe and more enduring, supplying the false claim to permanence that their answer overturns.
- (20:72) [luna: strong; terra: strong; basis: contrast+root+scene+speaker+theme] [cited in ¶70] قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ
  Unverified discovery rationale: luna: The sorcerers refuse to prefer Pharaoh over the clear signs and say he rules only this nearer life; their لَن نُّؤْثِرَكَ and ٱلْحَيَوٰةَ ٱلدُّنْيَا meet the section’s choice of the worldly life word for word. | terra: The magicians refuse to prefer Pharaoh over the clear proofs and say that he can decree only in this worldly life, directly joining preference, allotted judgment, and the lower life.
- (20:73) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶70] إِنَّآ ءَامَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَٰيَٰنَا وَمَآ أَكْرَهْتَنَا عَلَيْهِ مِنَ ٱلسِّحْرِ ۗ وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ
  Unverified discovery rationale: luna: The sorcerers answer Pharaoh that God is better and more lasting (خَيْرٌ وَأَبْقَىٰ); their reply supplies the lasting side of the section’s life-choice contrast. | terra: The magicians seek forgiveness and answer Pharaoh that God is better and more enduring, the precise confession heard again in the section's contrast between the present life and what lasts.
- (20:74) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶70] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
  Unverified discovery rationale: luna: The criminal in Hell “neither dies therein nor lives” (لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ); this is the section’s exact counterpart for 87:13’s suspended state in the fire. | terra: The criminal comes to Hell and there neither dies nor lives, exactly supplying the condition named in the section's fire sequence.
- (20:75) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶70] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
  Unverified discovery rationale: luna: The one who comes to God as a believer with good deeds receives the highest ranks; this meets the section’s joining of purification with ٱلدَّرَجَٰتُ ٱلْعُلَىٰ in Moses’s story. | terra: The believer who does righteous deeds receives the highest degrees, meeting the section's language of height within the same magician passage.
- (20:76) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶70] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
  Unverified discovery rationale: luna: The gardens are named as the reward of one who purifies himself (جَزَآءُ مَن تَزَكَّىٰ); this directly joins the source wording تَزَكَّىٰ to a lasting afterlife reward. | terra: Gardens and abiding reward are called the recompense of one who purifies himself, completing the section's movement from purification to lasting life.
- (20:114) [terra: strong (missing-ayat turn); basis: speaker+theme] فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۗ وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا
  Unverified discovery rationale: terra: The Prophet is told not to hurry the Quran before its revelation is completed and to ask for knowledge, a direct counterpart to receiving recitation without losing it.
- (20:131) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶71] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
  Unverified discovery rationale: luna: Moses is told not to look longingly at the flower (زَهْرَةَ) of worldly life; the same verse says what the Lord provides is better and more lasting, precisely the pasture-to-choice meeting described in the section. | terra: The flower of worldly life is a temporary trial while the Lord's provision is better and more enduring, directly merging pasture, provision, preference, and permanence.
- (20:132) [terra: strong; basis: neighbour+speaker+theme] وَأْمُرْ أَهْلَكَ بِٱلصَّلَوٰةِ وَٱصْطَبِرْ عَلَيْهَا ۖ لَا نَسْـَٔلُكَ رِزْقًۭا ۖ نَّحْنُ نَرْزُقُكَ ۗ وَٱلْعَٰقِبَةُ لِلتَّقْوَىٰ
  Unverified discovery rationale: terra: Immediately after the worldly flower, the Prophet is told to command his household to prayer and persist, while God provides; this joins prayer to the better provision of 20:131.
- (20:133) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+root+scene+theme] وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ
  Unverified discovery rationale: luna: In response to a demand for a sign, the ayah points to clear evidence in earlier scriptures; this echoes the section’s closing claim that its teaching was already in the first pages. | terra: In the same passage, the proof is said already to have come in the former scriptures, directly meeting the section's closing appeal to the earliest scrolls.
- (21:48) [terra: strong; basis: root+theme] وَلَقَدْ ءَاتَيْنَا مُوسَىٰ وَهَٰرُونَ ٱلْفُرْقَانَ وَضِيَآءًۭ وَذِكْرًۭا لِّلْمُتَّقِينَ
  Unverified discovery rationale: terra: Moses and Aaron receive the Criterion, light, and a reminder for the God-fearing, joining Musa's scripture to guidance and remembrance.
- (21:49) [terra: strong; basis: neighbour+root+theme] ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَهُم مِّنَ ٱلسَّاعَةِ مُشْفِقُونَ
  Unverified discovery rationale: terra: Those recipients fear their Lord unseen and dread the Hour, defining the fear that receives the Mosaic reminder.
- (22:5) [luna: strong; terra: strong; basis: root+scene+theme] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
  Unverified discovery rationale: luna: In one ayah, human formation passes through the womb and lifeless earth stirs, swells, and grows after rain; it makes explicit the section’s meeting of formed body and rain-raised pasture. | terra: One ayah moves from embryo stages and what is formed or unformed in wombs to dead earth stirring and growing after rain, exactly joining fashioned body to pasture.
- (22:77) [terra: strong (missing-ayat turn); basis: root+scene+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱرْكَعُوا۟ وَٱسْجُدُوا۟ وَٱعْبُدُوا۟ رَبَّكُمْ وَٱفْعَلُوا۟ ٱلْخَيْرَ لَعَلَّكُمْ تُفْلِحُونَ ۩
  Unverified discovery rationale: terra: Believers are commanded to bow, prostrate, worship, and do good so that they may prosper, linking the magicians' posture to the section's falah.
- (23:1) [luna: strong; terra: strong (missing-ayat turn); basis: root+theme] قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ
  Unverified discovery rationale: luna: The section identifies source wording أَفْلَحَ as the farmer’s success-word; this ayah opens by saying the believers have succeeded, letting that cultivated-success resonance accompany their ensuing description. | terra: The believers are declared prosperous, opening a passage that immediately identifies prayer as their first trait.
- (23:2) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ
  Unverified discovery rationale: terra: The prosperous believers are humble in prayer, explicitly connecting falah to the section's prayer branch.
- (23:13) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+root+scene] ثُمَّ جَعَلْنَٰهُ نُطْفَةًۭ فِى قَرَارٍۢ مَّكِينٍۢ
  Unverified discovery rationale: luna: The human drop is placed in a secure resting place (قَرَارٍ مَّكِينٍ); this identifies the womb stage in the bodily formation that the section joins to the pasture’s growth. | terra: The drop is placed in a secure lodging, locating the body-forming process in the womb.
- (23:14) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+root+scene+theme] ثُمَّ خَلَقْنَا ٱلنُّطْفَةَ عَلَقَةًۭ فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةًۭ فَخَلَقْنَا ٱلْمُضْغَةَ عِظَٰمًۭا فَكَسَوْنَا ٱلْعِظَٰمَ لَحْمًۭا ثُمَّ أَنشَأْنَٰهُ خَلْقًا ءَاخَرَ ۚ فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ
  Unverified discovery rationale: luna: The sequence from drop to clot to lump ends, “then We produced him as another creation”; it supplies the formed-body scene that the section reads alongside pasture and soil. | terra: The drop is successively made clot, lump, bones, flesh, and another creation, an extended scene of the shaping developed by the section.
- (23:18) [luna: strong; terra: strong; basis: root+scene+theme] وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ ۖ وَإِنَّا عَلَىٰ ذَهَابٍۭ بِهِۦ لَقَٰدِرُونَ
  Unverified discovery rationale: luna: God sends down water “in due measure,” settles it in the earth, and can take it away; this adds storage and possible loss to the section’s measured rain and pasture. | terra: Water is sent from the sky in due measure, lodged in the earth, and remains subject to removal, a close parallel to measured water and what stays or disappears.
- (23:27) [terra: strong (missing-ayat turn); basis: scene+theme] فَأَوْحَيْنَآ إِلَيْهِ أَنِ ٱصْنَعِ ٱلْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا فَإِذَا جَآءَ أَمْرُنَا وَفَارَ ٱلتَّنُّورُ ۙ فَٱسْلُكْ فِيهَا مِن كُلٍّۢ زَوْجَيْنِ ٱثْنَيْنِ وَأَهْلَكَ إِلَّا مَن سَبَقَ عَلَيْهِ ٱلْقَوْلُ مِنْهُمْ ۖ وَلَا تُخَٰطِبْنِى فِى ٱلَّذِينَ ظَلَمُوٓا۟ ۖ إِنَّهُم مُّغْرَقُونَ
  Unverified discovery rationale: terra: The repeated Noah account again makes the oven gush as the flood begins, confirming the fire-vessel and water conjunction.
- (23:41) [luna: medium; terra: strong; basis: contrast+root+scene+theme] فَأَخَذَتْهُمُ ٱلصَّيْحَةُ بِٱلْحَقِّ فَجَعَلْنَٰهُمْ غُثَآءًۭ ۚ فَبُعْدًۭا لِّلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: The source dictionary form غُثَاءً names the pasture’s dry debris and the flood foam; here the same word is what a destroyed people become after the cry, carrying that debris-word into a judgment scene. | terra: A destroyed people are made ghutha, debris swept away; the pasture word becomes a human fate and sharpens the section's image of what does not remain.
- (24:36) [terra: strong (missing-ayat turn); basis: root+scene+speaker] فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ
  Unverified discovery rationale: terra: In houses God permits to be raised, His name is remembered and He is glorified morning and evening, joining height, name, remembrance, and glorification.
- (24:37) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
  Unverified discovery rationale: terra: Trade does not distract these people from God's remembrance and establishing prayer, and they fear the coming Day; worldly business is subordinated to remembrance, prayer, and fear.
- (25:2) [luna: strong; terra: strong; basis: root+theme] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
  Unverified discovery rationale: luna: The source verb قَدَّرَ in 87:3 is echoed in God’s having “created everything and determined it with precise determination” (فَقَدَّرَهُۥ تَقْدِيرًا); the broader creation claim reinforces the section’s measured order. | terra: God creates everything and determines it with exact determination, stating together the two divine acts that organize the section.
- (26:46) [terra: strong; basis: scene] فَأُلْقِىَ ٱلسَّحَرَةُ سَٰجِدِينَ
  Unverified discovery rationale: terra: A further account again has the magicians thrown down in prostration, confirming the section's central posture across the repeated scene.
- (26:47) [terra: strong; basis: neighbour+scene] قَالُوٓا۟ ءَامَنَّا بِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The prostrate magicians say that they believe in the Lord of the worlds, contributing their confession to the repeated scene.
- (26:48) [terra: strong; basis: neighbour+scene] رَبِّ مُوسَىٰ وَهَٰرُونَ
  Unverified discovery rationale: terra: They specify the Lord of Moses and Aaron, tying that confession to Moses' mission.
- (26:49) [terra: strong; basis: scene+theme] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ فَلَسَوْفَ تَعْلَمُونَ ۚ لَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ أَجْمَعِينَ
  Unverified discovery rationale: terra: Pharaoh again denies their right to believe without his permission and threatens bodily punishment, repeating his claim over choice and life.
- (26:50) [terra: strong; basis: scene+theme] قَالُوا۟ لَا ضَيْرَ ۖ إِنَّآ إِلَىٰ رَبِّنَا مُنقَلِبُونَ
  Unverified discovery rationale: terra: The magicians answer that the threat does no harm because they will return to their Lord, making their preference for the lasting destination explicit.
- (26:51) [terra: strong; basis: scene+theme] إِنَّا نَطْمَعُ أَن يَغْفِرَ لَنَا رَبُّنَا خَطَٰيَٰنَآ أَن كُنَّآ أَوَّلَ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: They hope for their Lord's forgiveness because they were first to believe, showing what the section's chosen turn at the scene seeks.
- (26:77) [terra: strong (missing-ayat turn); basis: scene+theme] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: Abraham declares all former objects of worship enemies except the Lord of the worlds, giving his requested distance from idols a spoken form.
- (26:78) [terra: strong (missing-ayat turn); basis: neighbour+root+scene+theme] ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ
  Unverified discovery rationale: terra: Abraham identifies that Lord as the One who created him and guides him, joining his page to the section's creation-and-guidance pair.
- (26:79) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
  Unverified discovery rationale: terra: He says that God feeds him and gives him drink, adding provision to the Abrahamic confession.
- (26:81) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
  Unverified discovery rationale: terra: Abraham says that God causes him to die and then gives him life, bringing the life-and-death boundary into the same confession.
- (27:7) [luna: strong; terra: strong; basis: neighbour+scene] إِذْ قَالَ مُوسَىٰ لِأَهْلِهِۦٓ إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ
  Unverified discovery rationale: luna: Moses also sees a fire from a distance and hopes for news or a burning brand; this repeats the section’s distant-fire scene, though this telling does not mention finding guidance. | terra: Moses tells his family that he has perceived a fire and may return with news or a burning brand, the alternate opening of the section's fire-and-guidance scene.
- (27:8) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶68] فَلَمَّا جَآءَهَا نُودِىَ أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: At Moses’s fire the speech names blessing “whoever is in it and whoever is around it” and glorifies the Lord of the worlds; this is the section’s specific meeting of fire with tasbīḥ. | terra: When Moses reaches the fire, blessing is announced around it and God is glorified as Lord of the worlds; the fire scene thus actually voices the section's opening glorification.
- (27:9) [terra: strong; basis: neighbour+scene+speaker] يَٰمُوسَىٰٓ إِنَّهُۥٓ أَنَا ٱللَّهُ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: terra: After the glorification at the fire, the speaker identifies Himself to Moses as God, the Mighty and Wise; it completes whose voice turns the fire into guidance.
- (28:29) [luna: strong; terra: strong; basis: scene+theme] ۞ فَلَمَّا قَضَىٰ مُوسَى ٱلْأَجَلَ وَسَارَ بِأَهْلِهِۦٓ ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا قَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ
  Unverified discovery rationale: luna: After Moses completes his term and travels with his family, he sees a fire and hopes to bring them news or a burning brand; the fire is encountered on a journey, as in the section’s joined fire-and-way image. | terra: After completing his term, Moses sees a fire from the side of the mount and seeks news or a brand so his family may warm themselves, repeating the journey toward a useful fire.
- (28:30) [luna: strong; terra: strong; basis: neighbour+scene+speaker] فَلَمَّآ أَتَىٰهَا نُودِىَ مِن شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ فِى ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ مِنَ ٱلشَّجَرَةِ أَن يَٰمُوسَىٰٓ إِنِّىٓ أَنَا ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: The call to Moses comes from the tree in the blessed valley; this other fire-call account makes the distant flame a place of divine address, not the condemned person’s destination. | terra: When Moses reaches that fire, he is called from the blessed tract and told that the speaker is God, Lord of the worlds, completing the alternate fire revelation.
- (28:60) [luna: strong; terra: strong; basis: contrast+root+theme] وَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَزِينَتُهَا ۚ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ
  Unverified discovery rationale: luna: Worldly adornment is called temporary enjoyment, while what is with God is better and more lasting; this states the section’s preference contrast in nearly the same terms. | terra: Worldly goods are temporary adornment, while what is with God is better and more enduring, a direct restatement of the section's decisive choice.
- (28:68) [terra: strong; basis: root+theme] وَرَبُّكَ يَخْلُقُ مَا يَشَآءُ وَيَخْتَارُ ۗ مَا كَانَ لَهُمُ ٱلْخِيَرَةُ ۚ سُبْحَٰنَ ٱللَّهِ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
  Unverified discovery rationale: terra: The Lord creates what He wills and chooses, while creatures do not own the choice; creation and selection meet in one divine act.
- (28:77) [terra: strong (missing-ayat turn); basis: contrast+theme] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
  Unverified discovery rationale: terra: People must seek the Hereafter with what God has given while not forgetting their share of the world, a boundary that corrects preference without denying the worldly portion.
- (28:88) [terra: strong (missing-ayat turn); basis: root+theme] وَلَا تَدْعُ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ ۘ لَآ إِلَٰهَ إِلَّا هُوَ ۚ كُلُّ شَىْءٍ هَالِكٌ إِلَّا وَجْهَهُۥ ۚ لَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: Everything perishes except God's face, and judgment and return belong to Him, another exact formulation of what passes and what remains.
- (29:45) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
  Unverified discovery rationale: luna: The verse commands prayer and then names remembrance of God as greater; it supplies a direct formulation of the section’s pairing of salat with remembrance. | terra: The Prophet is commanded to recite revelation and establish prayer, and God's remembrance is declared greater; recitation, prayer, and remembrance meet explicitly.
- (31:34) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] إِنَّ ٱللَّهَ عِندَهُۥ عِلْمُ ٱلسَّاعَةِ وَيُنَزِّلُ ٱلْغَيْثَ وَيَعْلَمُ مَا فِى ٱلْأَرْحَامِ ۖ وَمَا تَدْرِى نَفْسٌۭ مَّاذَا تَكْسِبُ غَدًۭا ۖ وَمَا تَدْرِى نَفْسٌۢ بِأَىِّ أَرْضٍۢ تَمُوتُ ۚ إِنَّ ٱللَّهَ عَلِيمٌ خَبِيرٌۢ
  Unverified discovery rationale: luna: This ayah names rain and what wombs contain among matters known to God, then says no soul knows what it will earn tomorrow or where it will die; it joins the section’s womb and rain images to its claim that the hidden is known to God. | terra: Knowledge of the Hour, descending rain, and what is in wombs belongs to God, collecting the section's hidden Hour, pasture-making water, and formed body.
- (32:9) [terra: strong (missing-ayat turn); basis: root+scene] ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ ۖ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۚ قَلِيلًۭا مَّا تَشْكُرُونَ
  Unverified discovery rationale: terra: God fashions the human, breathes spirit into him, and grants hearing, sight, and hearts, a direct bodily use of the section's craft verb.
- (32:15) [terra: strong (missing-ayat turn); basis: root+scene+theme] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
  Unverified discovery rationale: terra: When believers are reminded of God's signs, they fall in prostration and glorify their Lord, a direct non-magician parallel to reminder becoming prostration and praise.
- (32:27) [terra: strong; basis: scene+theme] أَوَلَمْ يَرَوْا۟ أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ ۖ أَفَلَا يُبْصِرُونَ
  Unverified discovery rationale: terra: Water is driven to barren land and brings forth crops eaten by people and cattle, directly staging pasture as measured provision.
- (35:18) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
  Unverified discovery rationale: luna: The Prophet is told to warn those who fear their Lord unseen and establish prayer; whoever purifies himself does so for his own soul. This joins the section’s fear, prayer, and purification in one passage. | terra: Those who fear their Lord unseen and establish prayer can receive the warning, and whoever purifies does so for himself; the ayah gathers fear, prayer, hiddenness, and purification.
- (35:36) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
  Unverified discovery rationale: luna: The disbelievers are not allowed to die and their punishment is not lightened; the boundary illuminates the section’s “neither dead nor alive,” though this ayah states withheld death rather than the paired negation. | terra: The people of the Fire are neither finished by death nor relieved of punishment, a direct parallel to the section's life suspended between death and life.
- (36:11) [terra: strong; basis: speaker+theme] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
  Unverified discovery rationale: terra: Warning reaches the one who follows the Reminder and fears the Merciful unseen, combining receptive remembrance, fear, and hiddenness.
- (36:80) [terra: strong; basis: scene+theme] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
  Unverified discovery rationale: terra: God produces fire for people from the green tree, so vegetation and fire meet in one object as they do across the section.
- (38:72) [terra: strong (missing-ayat turn); basis: root+scene+theme] فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ
  Unverified discovery rationale: terra: The same command recurs: once the human is fashioned and given spirit, the angels are to fall prostrate, confirming that meeting of formation and worship.
- (39:6) [terra: strong (missing-ayat turn); basis: root+scene+theme] خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ ثُمَّ جَعَلَ مِنْهَا زَوْجَهَا وَأَنزَلَ لَكُم مِّنَ ٱلْأَنْعَٰمِ ثَمَٰنِيَةَ أَزْوَٰجٍۢ ۚ يَخْلُقُكُمْ فِى بُطُونِ أُمَّهَٰتِكُمْ خَلْقًۭا مِّنۢ بَعْدِ خَلْقٍۢ فِى ظُلُمَٰتٍۢ ثَلَٰثٍۢ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُصْرَفُونَ
  Unverified discovery rationale: terra: God creates people stage after stage in the womb within three darknesses, making bodily formation a hidden divine work.
- (39:9) [terra: strong (missing-ayat turn); basis: root+scene+theme] أَمَّنْ هُوَ قَٰنِتٌ ءَانَآءَ ٱلَّيْلِ سَاجِدًۭا وَقَآئِمًۭا يَحْذَرُ ٱلْءَاخِرَةَ وَيَرْجُوا۟ رَحْمَةَ رَبِّهِۦ ۗ قُلْ هَلْ يَسْتَوِى ٱلَّذِينَ يَعْلَمُونَ وَٱلَّذِينَ لَا يَعْلَمُونَ ۗ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: The devout person spends the night prostrating and standing, fears the Hereafter, hopes for mercy, and the ayah ends by distinguishing those who remember.
- (39:21) [luna: strong; terra: strong; basis: contrast+scene+theme] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: Rain brings out crops of differing colors, then they yellow and become debris (حُطَامًا); the ayah closely repeats the section’s growth-to-decay landscape. | terra: Rain becomes springs and many-colored crops, then withers yellow and turns to debris, and the whole scene is explicitly a reminder for understanding people.
- (40:64) [terra: strong (missing-ayat turn); basis: root+scene+theme] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ قَرَارًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ فَتَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: God makes earth a dwelling, raises heaven as a canopy, beautifies human forms, and provides good things, gathering height, bodily form, and provision.
- (40:67) [terra: strong (missing-ayat turn); basis: root+scene+theme] هُوَ ٱلَّذِى خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ يُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ثُمَّ لِتَكُونُوا۟ شُيُوخًۭا ۚ وَمِنكُم مَّن يُتَوَفَّىٰ مِن قَبْلُ ۖ وَلِتَبْلُغُوٓا۟ أَجَلًۭا مُّسَمًّۭى وَلَعَلَّكُمْ تَعْقِلُونَ
  Unverified discovery rationale: terra: Human life proceeds from dust and drop through clot, birth, maturity, old age, and an appointed term, joining formation to measured life and death.
- (41:39) [luna: strong; terra: strong; basis: scene+theme] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The earth is humble, then quivers and swells when water descends; this repeats the section’s transition from rain to living growth in the pasture. | terra: The humbled earth stirs and swells when water descends, and its revival proves that its Giver revives the dead, paralleling the womb-to-field movement.
- (41:47) [terra: strong; basis: scene+theme] ۞ إِلَيْهِ يُرَدُّ عِلْمُ ٱلسَّاعَةِ ۚ وَمَا تَخْرُجُ مِن ثَمَرَٰتٍۢ مِّنْ أَكْمَامِهَا وَمَا تَحْمِلُ مِنْ أُنثَىٰ وَلَا تَضَعُ إِلَّا بِعِلْمِهِۦ ۚ وَيَوْمَ يُنَادِيهِمْ أَيْنَ شُرَكَآءِى قَالُوٓا۟ ءَاذَنَّٰكَ مَا مِنَّا مِن شَهِيدٍۢ
  Unverified discovery rationale: terra: Knowledge of the Hour returns to God, and no fruit emerges or female conceives and gives birth outside His knowledge, linking hidden time, crop, and womb.
- (42:20) [luna: strong; terra: strong; basis: contrast+scene+theme] مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
  Unverified discovery rationale: luna: Whoever desires the harvest of the Hereafter has that harvest increased, while the seeker of the world gets some of it but no share in the Hereafter; this is the section’s two fields and chosen share made explicit. | terra: The ayah distinguishes the crop of the Hereafter, which is increased, from the crop of this world, which leaves no share in the Hereafter, making the section's two fields explicit.
- (42:27) [luna: strong; terra: strong (missing-ayat turn); basis: root+theme] ۞ وَلَوْ بَسَطَ ٱللَّهُ ٱلرِّزْقَ لِعِبَادِهِۦ لَبَغَوْا۟ فِى ٱلْأَرْضِ وَلَٰكِن يُنَزِّلُ بِقَدَرٍۢ مَّا يَشَآءُ ۚ إِنَّهُۥ بِعِبَادِهِۦ خَبِيرٌۢ بَصِيرٌۭ
  Unverified discovery rationale: luna: The section moves from water flowing by its measure to shares of provision; this ayah says God sends down provision in measure (بِقَدَرٍ), making that bridge concrete in its own account of livelihood. | terra: Unlimited provision would provoke transgression, so God sends it down by whatever measure He wills, clarifying measure as merciful apportionment.
- (42:36) [luna: strong; terra: strong; basis: contrast+root+theme] فَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
  Unverified discovery rationale: luna: What people have been given is worldly enjoyment, while what is with God is better and more lasting for believers; this restates the section’s nearer-life/final-life boundary. | terra: What people receive is enjoyment of worldly life, while what is with God is better and more enduring for trusting believers, repeating the section's scale of value.
- (43:11) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
  Unverified discovery rationale: luna: God sends water down in measure, revives dead land with it, and says people will likewise be brought forth; this joins the section’s measured rain and pasture to its passage from mortal life toward the Hereafter. | terra: Water descends from heaven in measure, revives dead land, and becomes an image of human emergence, linking pasture, measure, and bodily return.
- (43:32) [luna: medium; terra: strong (missing-ayat turn); basis: root+theme] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
  Unverified discovery rationale: luna: The section extends measure to an allotted share; this ayah says livelihood is apportioned among people, an explicit social counterpart to measured provision. | terra: God apportions livelihoods in worldly life and raises people in degrees, while His mercy is better than their accumulation; allotted share, height, and the better good meet explicitly.
- (48:29) [terra: strong (missing-ayat turn); basis: root+scene+theme] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
  Unverified discovery rationale: terra: The believers bow and prostrate while seeking God's bounty, and their growth is compared to a crop that strengthens and pleases its sowers; prostration, provision, and cultivated growth meet together.
- (50:9) [terra: strong (missing-ayat turn); basis: scene+theme] وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا فَأَنۢبَتْنَا بِهِۦ جَنَّٰتٍۢ وَحَبَّ ٱلْحَصِيدِ
  Unverified discovery rationale: terra: Blessed water descends from heaven and produces gardens and harvested grain, joining rain to useful cultivated growth.
- (50:11) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] رِّزْقًۭا لِّلْعِبَادِ ۖ وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ ٱلْخُرُوجُ
  Unverified discovery rationale: terra: The crop is provision for servants and revives a dead land, making bodily emergence legible in the field's renewal.
- (50:45) [luna: strong (missing-ayat turn); terra: strong; basis: speaker+theme] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
  Unverified discovery rationale: luna: The Prophet is told to remind by the Qur’an whoever fears God’s warning; this directly joins the section’s reminder, Qur’an, and fearful hearer. | terra: The Prophet is told to remind with the Quran whoever fears the warning, directly matching reminder addressed to fear.
- (51:55) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: “Remind, for the reminder benefits the believers” is the ayah’s instruction; it closely parallels the source wording “remind if the reminder benefits.” | terra: The Prophet is commanded to remind because reminder benefits believers, making explicit the benefit condition attached to reminder in the section.
- (53:29) [terra: strong (missing-ayat turn); basis: root+speaker+theme] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: terra: The Prophet must turn from one who turns from remembrance and wants only worldly life, directly joining rejected reminder to preference for the lower life.
- (53:36) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ
  Unverified discovery rationale: luna: The question asks what is in Moses’s scriptures; the linked 53:37 names Abraham, completing the pair of earlier-page figures named at the section’s close. This ayah contributes Moses’s scriptures. | terra: The listener is asked whether he was informed of what is in the scrolls of Moses, an independent Quranic witness to the section's closing scriptural memory.
- (53:37) [terra: strong; basis: neighbour+root+theme] وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ
  Unverified discovery rationale: terra: Abraham who fulfilled is named beside Moses' scrolls, completing the same pairing of Abraham and Moses that closes the section.
- (54:11) [terra: strong (missing-ayat turn); basis: neighbour+scene] فَفَتَحْنَآ أَبْوَٰبَ ٱلسَّمَآءِ بِمَآءٍۢ مُّنْهَمِرٍۢ
  Unverified discovery rationale: terra: The gates of heaven are opened with pouring water, beginning a flood that turns descending provision into overwhelming judgment.
- (54:12) [terra: strong (missing-ayat turn); basis: neighbour+root+scene+theme] وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ
  Unverified discovery rationale: terra: Springs burst from the earth and the two waters meet for a matter already decreed, joining flood, meeting, and divine measure in one ayah.
- (54:17) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: terra: The Quran is made easy for remembrance and the hearer is asked who will remember, fusing the section's promise of ease with its command to remind.
- (54:22) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: terra: The same ease-for-remembrance formulation recurs after an earlier destroyed people, making remembrance the benefit that survives their passing.
- (54:32) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: terra: The ease-for-remembrance refrain recurs after another warning narrative, repeating the section's offered but dividing reminder.
- (54:40) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: terra: A fourth occurrence again makes the Quran easy for remembrance, confirming the repeated divine stance behind the section's movement.
- (54:49) [luna: strong; terra: strong; basis: root+theme] إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ
  Unverified discovery rationale: luna: “Indeed, We created everything according to a measure” (بِقَدَرٍ) repeats the source’s q-d-r language and makes the section’s measured creation explicit. | terra: Everything is created according to measure, the universal formulation behind the measured valley, body, and human share.
- (55:5) [terra: strong (missing-ayat turn); basis: root+theme] ٱلشَّمْسُ وَٱلْقَمَرُ بِحُسْبَانٍۢ
  Unverified discovery rationale: terra: The sun and moon move by precise calculation, extending the section's divine measure into the ordered heavens.
- (55:6) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَٱلنَّجْمُ وَٱلشَّجَرُ يَسْجُدَانِ
  Unverified discovery rationale: terra: Plants and trees prostrate, letting the pasture itself assume the posture of the believing magicians.
- (55:7) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
  Unverified discovery rationale: terra: God raises the heaven and establishes the balance, joining height to measured order.
- (55:26) [terra: strong (missing-ayat turn); basis: theme] كُلُّ مَنْ عَلَيْهَا فَانٍۢ
  Unverified discovery rationale: terra: Everyone upon the earth passes away, stating the disappearance side of the section's debris-and-benefit contrast.
- (55:27) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
  Unverified discovery rationale: terra: The majestic face of the Lord remains, completing the contrast with the One enduring reality.
- (56:57) [terra: strong; basis: root+theme] نَحْنُ خَلَقْنَٰكُمْ فَلَوْلَا تُصَدِّقُونَ
  Unverified discovery rationale: terra: God asks why people do not affirm the One who created them, opening a sustained creation-field-fire sequence that closely matches the section's meetings.
- (56:59) [terra: strong; basis: neighbour+root+scene] ءَأَنتُمْ تَخْلُقُونَهُۥٓ أَمْ نَحْنُ ٱلْخَٰلِقُونَ
  Unverified discovery rationale: terra: The ayah asks whether humans create the emitted seed or God is its creator, making bodily creation the first scene in that sequence.
- (56:60) [terra: strong; basis: neighbour+root+theme] نَحْنُ قَدَّرْنَا بَيْنَكُمُ ٱلْمَوْتَ وَمَا نَحْنُ بِمَسْبُوقِينَ
  Unverified discovery rationale: terra: God says that He has measured death among people, joining bodily destiny to the section's measuring and its boundary between death and life.
- (56:63) [terra: strong; basis: scene+theme] أَفَرَءَيْتُم مَّا تَحْرُثُونَ
  Unverified discovery rationale: terra: The listener is asked to consider what he tills, directly staging the worked field behind the section's agricultural sense of falah.
- (56:64) [terra: strong; basis: neighbour+scene+theme] ءَأَنتُمْ تَزْرَعُونَهُۥٓ أَمْ نَحْنُ ٱلزَّٰرِعُونَ
  Unverified discovery rationale: terra: God asks whether people make the crop grow or He does, attributing the field's useful growth to the Creator.
- (56:65) [terra: strong; basis: neighbour+scene+theme] لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا فَظَلْتُمْ تَفَكَّهُونَ
  Unverified discovery rationale: terra: God could make the crop shattered dry debris, the direct reversal of growth and counterpart to the spent pasture.
- (56:68) [terra: strong; basis: scene+theme] أَفَرَءَيْتُمُ ٱلْمَآءَ ٱلَّذِى تَشْرَبُونَ
  Unverified discovery rationale: terra: The listener is next asked to consider the water he drinks, opening the water scene that feeds the field.
- (56:69) [terra: strong; basis: neighbour+scene+theme] ءَأَنتُمْ أَنزَلْتُمُوهُ مِنَ ٱلْمُزْنِ أَمْ نَحْنُ ٱلْمُنزِلُونَ
  Unverified discovery rationale: terra: God asks whether people send that water down from the raincloud or He does, locating provision in the descending water.
- (56:70) [terra: strong; basis: contrast+scene+theme] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
  Unverified discovery rationale: terra: God could make the water bitter, marking the boundary between offered provision and unusable water.
- (56:71) [terra: strong; basis: scene+theme] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
  Unverified discovery rationale: terra: The listener is then asked to consider the fire he kindles, moving the same sequence from water and field to fire.
- (56:72) [terra: strong; basis: neighbour+scene+theme] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
  Unverified discovery rationale: terra: God asks whether people produced the fire's tree or He did, joining vegetation, creative craft, and kindled fire.
- (56:73) [terra: strong; basis: neighbour+scene+theme] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
  Unverified discovery rationale: terra: God made that fire a reminder and a provision for travelers, the clearest parallel to the section's fire that guides rather than consumes.
- (56:74) [terra: strong; basis: neighbour+root+speaker+theme] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
  Unverified discovery rationale: terra: The creation, crop, water, and fire sequence ends by commanding glorification of the name of the mighty Lord, closely matching the section's opening command.
- (57:3) [luna: strong; basis: root+theme] هُوَ ٱلْأَوَّلُ وَٱلْءَاخِرُ وَٱلظَّٰهِرُ وَٱلْبَاطِنُ ۖ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌ
  Unverified discovery rationale: luna: God is “the First and the Last, the Manifest and the Hidden” (ٱلظَّٰهِرُ وَٱلْبَاطِنُ); the paired terms directly echo the section’s account of God knowing what is public and hidden.
- (57:20) [luna: strong; terra: strong; basis: contrast+scene+theme] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: luna: This verse explicitly compares worldly life to rain-grown vegetation that delights cultivators, then yellows and becomes debris; it joins the section’s pasture image to its choice between near life and the Hereafter. | terra: Worldly life is illustrated by rain-grown vegetation that delights cultivators, then yellows and becomes debris before the lasting judgment, joining pasture to preference.
- (62:9) [terra: strong (missing-ayat turn); basis: neighbour+scene+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: At the call to Friday prayer, believers must leave trade and hasten to God's remembrance; this sets worldly commerce beneath prayer before the remembrance-and-falah command in 62:10.
- (62:10) [terra: strong; basis: root+speaker+theme] فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: terra: After prayer people seek God's bounty and remember Him much so that they may prosper, joining provision, remembrance, and falah.
- (65:3) [terra: strong (missing-ayat turn); basis: root+theme] وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ ۚ وَمَن يَتَوَكَّلْ عَلَى ٱللَّهِ فَهُوَ حَسْبُهُۥٓ ۚ إِنَّ ٱللَّهَ بَٰلِغُ أَمْرِهِۦ ۚ قَدْ جَعَلَ ٱللَّهُ لِكُلِّ شَىْءٍۢ قَدْرًۭا
  Unverified discovery rationale: terra: God provides from an unexpected place, fulfills His command, and has set a measure for everything, joining hidden provision to universal measure.
- (65:4) [terra: strong (missing-ayat turn); basis: root+theme] وَٱلَّٰٓـِٔى يَئِسْنَ مِنَ ٱلْمَحِيضِ مِن نِّسَآئِكُمْ إِنِ ٱرْتَبْتُمْ فَعِدَّتُهُنَّ ثَلَٰثَةُ أَشْهُرٍۢ وَٱلَّٰٓـِٔى لَمْ يَحِضْنَ ۚ وَأُو۟لَٰتُ ٱلْأَحْمَالِ أَجَلُهُنَّ أَن يَضَعْنَ حَمْلَهُنَّ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا
  Unverified discovery rationale: terra: Whoever fears God receives ease in his affair, linking fear directly to divinely given ease.
- (65:7) [terra: strong (missing-ayat turn); basis: root+theme] لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ ۖ وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ ۚ لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا ۚ سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا
  Unverified discovery rationale: terra: Spending is apportioned according to provision, and God promises ease after hardship; share, provision, and ease meet in one ayah.
- (67:2) [terra: strong (missing-ayat turn); basis: root+theme] ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
  Unverified discovery rationale: terra: God creates death and life to test whose work is best, clarifying the ordered purpose behind the section's boundary between living and dying.
- (69:11) [terra: strong (missing-ayat turn); basis: neighbour+scene] إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ
  Unverified discovery rationale: terra: When the water overflowed, humanity's ancestors were carried in the vessel, recalling the flood as both destruction and preservation.
- (69:12) [terra: strong (missing-ayat turn); basis: neighbour+root+scene+theme] لِنَجْعَلَهَا لَكُمْ تَذْكِرَةًۭ وَتَعِيَهَآ أُذُنٌۭ وَٰعِيَةٌۭ
  Unverified discovery rationale: terra: The flood is made a reminder to be retained by a retaining ear, directly connecting passing waters to remembered speech that is not lost.
- (73:8) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
  Unverified discovery rationale: luna: The Prophet is told to remember the name of his Lord and devote himself wholly to Him; this repeats the section’s joining of the Lord’s name with remembrance and worship. | terra: The Prophet is commanded to remember the name of his Lord and devote himself wholly to Him, closely paralleling remembering the Lord's name before prayer.
- (74:54) [luna: strong (missing-ayat turn); terra: medium; basis: root+speaker+theme] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
  Unverified discovery rationale: luna: The passage calls the Qur’an a reminder (تَذْكِرَةٌ); this is a direct formulation of the reminder the section says is offered after recitation. | terra: The warning is called a reminder, beginning a short sequence about receiving it under divine will.
- (74:55) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+root+speaker+theme] فَمَن شَآءَ ذَكَرَهُۥ
  Unverified discovery rationale: luna: Whoever wills may remember it; this matches the section’s two different responses to the reminder. | terra: Whoever wills may remember it, placing human response beside the offered reminder.
- (74:56) [luna: strong (missing-ayat turn); terra: medium; basis: contrast+neighbour+root+speaker+theme] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
  Unverified discovery rationale: luna: They will not remember unless God wills, and He is worthy to be feared; this meets the section’s exception to not forgetting and the one who remembers because he fears. | terra: They remember only if God wills, closely paralleling the section's qualification of remembered recitation by divine will.
- (75:16) [luna: medium; terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ
  Unverified discovery rationale: luna: The Prophet is told not to hurry his tongue with the revelation; 75:17–19 complete the collection and recitation claim, while this cited ayah contributes the restraint around receiving the word. | terra: The Prophet is told not to move his tongue hurriedly with revelation, staging the concern about securely receiving the recited word.
- (75:17) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+root+speaker+theme] إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ
  Unverified discovery rationale: luna: God takes responsibility for its collection and recitation (جَمْعَهُۥ وَقُرْءَانَهُۥ); this concretizes the section’s word being gathered and recited without being forgotten. | terra: God takes responsibility for the revelation's collection and recitation, closely paralleling the section's promise that the gathered word will be read and retained.
- (75:18) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ
  Unverified discovery rationale: luna: The listener is told to follow the recitation when it is recited; this continues the section’s account of receiving and preserving the revealed word. | terra: Once God recites it, the Prophet is told to follow its recitation, completing the stance of guided reception.
- (75:19) [luna: strong; basis: theme] ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ
  Unverified discovery rationale: luna: The verse assigns its clarification to God; it completes the adjacent passage on recitation that the section connects to “We will make you recite.”
- (75:37) [terra: strong (missing-ayat turn); basis: neighbour+scene] أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ
  Unverified discovery rationale: terra: The human begins as a drop of emitted fluid, contributing the material stage immediately before creation and proportioning in 75:38.
- (75:38) [luna: strong; terra: strong; basis: root+scene] ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ
  Unverified discovery rationale: luna: The human is a clot, then God creates and proportions him (فَخَلَقَ فَسَوَّىٰ); this is a direct bodily use of the section’s source wording فَسَوَّىٰ. | terra: The drop becomes a clot and God then creates and proportions it, using the creation-and-fashioning pair in the embryonic sense developed by the section.
- (75:39) [terra: strong (missing-ayat turn); basis: neighbour+root+scene] فَجَعَلَ مِنْهُ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
  Unverified discovery rationale: terra: God makes the fashioned human into the male and female pair, completing the bodily differentiation after 75:38.
- (76:2) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: root+scene+theme] إِنَّا خَلَقْنَا ٱلْإِنسَٰنَ مِن نُّطْفَةٍ أَمْشَاجٍۢ نَّبْتَلِيهِ فَجَعَلْنَٰهُ سَمِيعًۢا بَصِيرًا
  Unverified discovery rationale: luna: The human is created from a mixed drop as a test; this links the section’s formed body to the later division between those who heed and those who turn away. | terra: The human is created from a mixed drop as a test and given hearing and sight, joining bodily formation to moral trial.
- (76:3) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+root+theme] إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا
  Unverified discovery rationale: luna: God guides the human to the way, then the human is grateful or ungrateful; this makes the section’s movement from divine guidance to two different responses explicit. | terra: God guides the human to the way, after which he may be grateful or ungrateful, stating the choice opened by guidance.
- (76:4) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا
  Unverified discovery rationale: terra: Chains and a blaze are prepared for the ungrateful, carrying one branch of that guided choice into fire.
- (76:25) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا
  Unverified discovery rationale: terra: The Prophet is commanded to remember his Lord's name morning and evening, a close parallel to the section's remembered divine name.
- (76:26) [terra: strong (missing-ayat turn); basis: neighbour+scene+speaker+theme] وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا
  Unverified discovery rationale: terra: He is told to prostrate and glorify God at night, bringing the section's prayer posture and glorification together.
- (77:21) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] فَجَعَلْنَٰهُ فِى قَرَارٍۢ مَّكِينٍ
  Unverified discovery rationale: luna: The human fluid is placed in a firm lodging; this supplies the womb setting for the section’s formed-body image. | terra: The fluid is placed in a secure lodging, identifying the womb-side containment of that formation.
- (77:22) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+root+scene+theme] إِلَىٰ قَدَرٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: luna: The lodging lasts to a known term; this makes the womb’s duration part of the measured life that the section contrasts with what lasts. | terra: It remains there until a known measure, joining gestation directly to appointed measure.
- (77:23) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+root+theme] فَقَدَرْنَا فَنِعْمَ ٱلْقَٰدِرُونَ
  Unverified discovery rationale: luna: God says He measured it and is the best of measurers; this repeats the source verb قَدَّرَ at 87:3 in the bodily context the section connects to measured creation. | terra: God says that He determined it and is the best determiner, closing bodily formation with divine measurement.
- (79:16) [terra: strong (missing-ayat turn); basis: neighbour+scene] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
  Unverified discovery rationale: terra: God calls Moses in the sacred valley of Tuwa, the concise alternate setting of the same encounter reached at the fire.
- (79:18) [terra: strong; basis: root+scene+speaker] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
  Unverified discovery rationale: terra: Moses asks Pharaoh whether he is willing to purify himself, placing purification at the center of another Musa encounter.
- (79:19) [terra: strong; basis: root+scene+theme] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
  Unverified discovery rationale: terra: Moses offers to guide Pharaoh to his Lord so that he will fear, directly joining guidance to the fear that makes reminder effective.
- (79:24) [luna: strong; terra: strong; basis: contrast+root+scene+speaker] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
  Unverified discovery rationale: luna: Pharaoh claims, “I am your most high lord” (أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ); his self-exaltation reverses the section’s opening command to glorify the Lord who is truly Most High. | terra: Pharaoh claims to be the highest lord; the claim is the explicit human usurpation of the section's opening name, the Lord Most High.
- (79:26) [terra: strong; basis: scene+theme] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
  Unverified discovery rationale: terra: Pharaoh's fate is called a lesson for one who fears, connecting the Musa narrative itself to the section's fear-responsive reminder.
- (79:28) [terra: strong (missing-ayat turn); basis: root+scene+theme] رَفَعَ سَمْكَهَا فَسَوَّىٰهَا
  Unverified discovery rationale: terra: God raises the heaven's canopy and proportions it, joining height to the act of fashioning.
- (79:31) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا
  Unverified discovery rationale: luna: God brings out the earth’s water and pasture (مَاءَهَا وَمَرْعَىٰهَا); the source wording at 87:4 is المَرْعَىٰ, and this gives a direct parallel for pasture as divine provision. | terra: God brings the earth's water and pasture out of it, restaging the provision that later dries and passes.
- (79:35) [terra: strong (missing-ayat turn); basis: root+theme] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
  Unverified discovery rationale: terra: On the exposed Day, the human remembers what he strove for, bringing remembered effort into the once-hidden reckoning.
- (79:36) [terra: strong; basis: scene+theme] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
  Unverified discovery rationale: terra: Hell is made visible to whoever sees, turning the once-hidden destination into the manifest fire before the human choice is judged.
- (79:37) [luna: strong; terra: strong; basis: contrast+neighbour+theme] فَأَمَّا مَن طَغَىٰ
  Unverified discovery rationale: luna: The one who transgresses and prefers worldly life (وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا) is the section’s same kind of chooser, now shown in its judgment context. | terra: The next division begins with the one who transgressed, identifying the person whose preference leads to the fire named around it.
- (79:38) [luna: strong; terra: strong; basis: contrast+neighbour+root+scene+theme] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: luna: Hell is the refuge of that worldly-life preferrer; this makes explicit where the section’s choice of the near life leads. | terra: That person prefers worldly life, using the section's exact act of preference in the same eschatological division.
- (79:39) [terra: strong; basis: neighbour+scene+theme] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: terra: Hell is then his refuge, directly joining preference for the lower life to entry into fire.
- (79:40) [luna: strong; terra: strong; basis: contrast+neighbour+speaker+theme] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
  Unverified discovery rationale: luna: The one who fears standing before his Lord and restrains himself from desire is the counterpart to the section’s fearful hearer and its rejected worldly preference. | terra: The opposite person fears standing before his Lord and restrains desire, stating the fear-led choice on the other branch.
- (79:41) [luna: strong; terra: strong; basis: contrast+neighbour+scene+theme] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: Paradise is the refuge of the one who restrains desire; this supplies the lasting counterpart to the fire named in the section. | terra: The Garden becomes that person's refuge, completing the alternative to the fire across the section's two human responses.
- (79:44) [terra: strong (missing-ayat turn); basis: theme] إِلَىٰ رَبِّكَ مُنتَهَىٰهَآ
  Unverified discovery rationale: terra: The Hour's endpoint belongs to the Lord alone, reinforcing the section's hidden Hour as divine knowledge.
- (79:45) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
  Unverified discovery rationale: luna: The Prophet is told that he is only a warner for whoever fears the Hour; this gives the section’s fearful hearer a direct counterpart in a warning about the end. | terra: The Prophet is only a warner to the one who fears the Hour, closely matching the command to remind and the one who will remember through fear.
- (80:3) [luna: strong; basis: speaker+theme] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
  Unverified discovery rationale: luna: The blind visitor may purify himself; this directly meets the section’s link between reminder, purification, and a person’s response.
- (80:4) [luna: strong; basis: speaker+theme] أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ
  Unverified discovery rationale: luna: The visitor may be reminded and benefit from the reminder (فَتَنفَعَهُ ٱلذِّكْرَىٰ); this closely echoes the section’s “remind if reminder benefits.”
- (80:8) [luna: strong; basis: contrast+speaker] وَأَمَّا مَن جَآءَكَ يَسْعَىٰ
  Unverified discovery rationale: luna: The one who comes hastening to the Prophet is introduced as fearing God; that stance meets the section’s person who will remember because he fears.
- (80:9) [luna: strong; basis: speaker+theme] وَهُوَ يَخْشَىٰ
  Unverified discovery rationale: luna: The visitor is fearful (وَهُوَ يَخْشَىٰ); this is the section’s stated disposition of the one who takes heed.
- (80:11) [terra: strong; basis: root+theme] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
  Unverified discovery rationale: terra: The revelation is itself called a reminder, beginning a short passage that joins willing remembrance to elevated purified scrolls.
- (80:12) [terra: strong; basis: neighbour+root+theme] فَمَن شَآءَ ذَكَرَهُۥ
  Unverified discovery rationale: terra: Whoever wills may remember it, making the hearer's choice part of the reminder scene.
- (80:13) [terra: strong; basis: neighbour+root+theme] فِى صُحُفٍۢ مُّكَرَّمَةٍۢ
  Unverified discovery rationale: terra: That reminder is in honored scrolls, directly meeting the section's close in the earlier scrolls.
- (80:14) [terra: strong; basis: neighbour+root+theme] مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ
  Unverified discovery rationale: terra: The scrolls are raised and purified, joining the section's height and purification within its scriptural image.
- (80:19) [luna: strong; terra: strong; basis: root+scene+theme] مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ
  Unverified discovery rationale: luna: The human is created from a drop and determined (فَقَدَّرَهُۥ); this supplies the bodily instance of the source’s measured formation. | terra: God creates the human from a drop and measures him, joining bodily origin to determination.
- (80:20) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ
  Unverified discovery rationale: luna: God then eases the human’s way (ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ); this repeats the section’s making-easy and guidance themes in the account of a human life. | terra: God then eases the human's way, directly pairing measured formation with the eased path promised in the section.
- (80:21) [luna: strong; basis: contrast+scene] ثُمَّ أَمَاتَهُۥ فَأَقْبَرَهُۥ
  Unverified discovery rationale: luna: God causes the human to die and assigns a grave; this marks the mortal boundary that the section contrasts with the one who neither dies nor lives in the fire.
- (80:22) [luna: strong; basis: contrast+theme] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
  Unverified discovery rationale: luna: Then, when He wills, God raises the human; this gives the section’s mortal life and later lasting outcome their resurrection horizon.
- (80:25) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
  Unverified discovery rationale: luna: God pours water down abundantly; this begins the rain-grown provision scene that meets the section’s measured water and pasture. | terra: God pours water abundantly, beginning the cultivated-field sequence behind the section's rain and pasture.
- (80:26) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا
  Unverified discovery rationale: luna: God splits the earth open for growth; this makes the field-breaking image in the section concrete as soil opened to bring forth food. | terra: God splits the earth open, supplying the cracked and worked ground through which the crop emerges.
- (80:27) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] فَأَنۢبَتْنَا فِيهَا حَبًّۭا
  Unverified discovery rationale: luna: Grain grows from that opened earth; this supplies the cultivated yield set against the section’s withered pasture. | terra: Grain is made to grow in that ground, the useful produce on the cultivated side of the section's field contrast.
- (80:32) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
  Unverified discovery rationale: luna: The produce is provision and enjoyment for people and their livestock; this completes 80:25–31’s rain-grown field and makes explicit the beneficiaries of pasture and crop. | terra: Those products are provision for people and their livestock, stating the benefit of the field and pasture.
- (81:27) [terra: strong; basis: root+theme] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The Quran is a reminder to all worlds, establishing the offered reminder before the following choice of path.
- (81:28) [terra: strong; basis: neighbour+root+theme] لِمَن شَآءَ مِنكُمْ أَن يَسْتَقِيمَ
  Unverified discovery rationale: terra: The reminder is for whoever wills to take a straight way, joining recollection, choice, and path.
- (81:29) [terra: strong; basis: neighbour+root+theme] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: Human willing remains under the will of God, Lord of the worlds, matching the section's exception for what God wills.
- (82:7) [luna: strong; terra: strong; basis: root+scene] ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ
  Unverified discovery rationale: luna: God “created you, proportioned you, and balanced you” (خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ); this repeats the source’s forming verb for the shaped body. | terra: God is the One who created, proportioned, and balanced the human, a direct bodily use of the section's craft vocabulary.
- (82:8) [luna: strong; basis: root+scene] فِىٓ أَىِّ صُورَةٍۢ مَّا شَآءَ رَكَّبَكَ
  Unverified discovery rationale: luna: God assembles a person in whatever form He wills; the ayah gives the bodily form that the section pairs with shaping and forming.
- (91:7) [terra: strong; basis: root+theme] وَنَفْسٍۢ وَمَا سَوَّىٰهَا
  Unverified discovery rationale: terra: The soul and the One who proportioned it extend the section's craft of bodily fashioning into moral formation.
- (91:8) [terra: strong; basis: neighbour+theme] فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
  Unverified discovery rationale: terra: The fashioned soul is shown its corruption and its piety, supplying the two possibilities that make purification a choice.
- (91:9) [luna: strong; terra: strong; basis: neighbour+root+theme] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
  Unverified discovery rationale: luna: “Successful is the one who purifies it” (قَدْ أَفْلَحَ مَن زَكَّىٰهَا) directly joins success and purification as in source 87:14. | terra: Prosperity belongs to the one who purifies the soul, the closest Quranic counterpart to the section's pairing of falah and tazakka.
- (91:10) [luna: strong; terra: strong; basis: contrast+root+theme] وَقَدْ خَابَ مَن دَسَّىٰهَا
  Unverified discovery rationale: luna: The next ayah says the one who corrupts the soul has failed; this is the explicit reversal of the section’s successful purification. | terra: Failure belongs to the one who buries or stunts the soul, the cultivated-field reversal of purification and growth.
- (92:5) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
  Unverified discovery rationale: luna: The one who gives and is mindful of God begins the same contrasting path as the section’s one who purifies and fears; the following ayat describe the ease and fire that divide the two paths. | terra: The easing passage begins with one who gives and fears, tying the receptive branch to the fear that accepts the section's reminder.
- (92:6) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] وَصَدَّقَ بِٱلْحُسْنَىٰ
  Unverified discovery rationale: luna: The giver affirms “the best” (بِٱلْحُسْنَىٰ); this makes belief in the better outcome the hinge of the section’s lasting-life choice. | terra: That person affirms the best promise, distinguishing the belief that precedes being eased toward ease.
- (92:7) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+root+speaker+theme] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
  Unverified discovery rationale: luna: For that giver, God eases the way to ease (لِلْيُسْرَىٰ); this is a direct counterpart to source 87:8’s easing toward ease. | terra: God promises to ease that person toward ease, the closest repeated formulation of the section's promise of the easy way.
- (92:8) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
  Unverified discovery rationale: luna: The other person withholds and thinks himself self-sufficient; this reverses the giving and trust that lead to lasting good in the section. | terra: The opposite branch begins with one who withholds and thinks himself self-sufficient, reversing provision used in trust.
- (92:9) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَكَذَّبَ بِٱلْحُسْنَىٰ
  Unverified discovery rationale: luna: The withholding person denies the best (بِٱلْحُسْنَىٰ); this reverses the other path’s affirmation and the section’s final-life preference. | terra: He denies the best promise, identifying the response that leads away from the easy course.
- (92:10) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+root+speaker+theme] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
  Unverified discovery rationale: luna: God eases this person toward hardship; the paired paths make the section’s two outcomes of preferring or turning away perceptible. | terra: God will ease him toward hardship, an explicit reversal that reveals ease as a morally chosen destination rather than mere comfort.
- (92:11) [luna: strong; basis: contrast+scene] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
  Unverified discovery rationale: luna: His wealth will not avail him when he falls; this puts the section’s passing worldly provision at the threshold of its fire scene.
- (92:12) [luna: strong; terra: strong; basis: root+speaker+theme] إِنَّ عَلَيْنَا لَلْهُدَىٰ
  Unverified discovery rationale: luna: The verse says guidance belongs to God; it recalls the source’s “determined, then guided” and Moses finding guidance at the fire. | terra: God declares that guidance belongs to Him, matching the section's guided road and the Lord who guides what He forms.
- (92:13) [luna: strong; terra: strong; basis: contrast+neighbour+theme] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
  Unverified discovery rationale: luna: The Hereafter and the first life belong to God; this directly frames the same two lives the section says people choose between. | terra: The Hereafter and the first life belong to God, setting the two temporal sides before the warning of fire.
- (92:14) [luna: strong; terra: strong; basis: contrast+neighbour+scene+speaker] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
  Unverified discovery rationale: luna: The warning is of a blazing fire (نَارًا تَلَظَّىٰ); it meets the section’s fire that one person enters and that another approaches as a source of guidance. | terra: God warns of a blazing fire, the same warning to which the section's people respond in opposite ways.
- (92:15) [luna: strong; terra: strong; basis: contrast+neighbour+root+scene] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
  Unverified discovery rationale: luna: Only the most wretched enters that fire; this is the section’s boundary between the person who enters the great fire and the one who fears. | terra: Only the most wretched enters that fire, an especially close parallel to the section's wretched person who burns in the greater fire.
- (92:16) [luna: strong; terra: strong; basis: contrast+neighbour+theme] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: luna: The one entering has denied and turned away; this states the avoidance of reminder that the section sets against recollection by the fearful. | terra: The most wretched is identified as the one who denied and turned away, explaining his rejection of reminder.
- (92:17) [luna: strong; terra: strong; basis: contrast+root+scene] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
  Unverified discovery rationale: luna: The most mindful person is kept far from the fire; this gives the section’s fear and purification the opposite end from entering it. | terra: The God-fearing person is kept away from the fire, reversing the wretched person's approach and echoing avoidance in the section.
- (92:18) [luna: strong; terra: strong; basis: neighbour+root+theme] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
  Unverified discovery rationale: luna: This person gives wealth to purify himself (يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ); it makes the section’s source wording تَزَكَّىٰ a concrete act rather than a bare label. | terra: He gives his wealth in order to purify himself, giving concrete action to the purification on the saved branch.
- (92:20) [luna: strong; terra: strong; basis: neighbour+root+speaker+theme] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
  Unverified discovery rationale: luna: The giver seeks only the face of his Lord, the Most High (وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ); this joins the section’s opening praise of the Most High with its purified person’s final aim. | terra: His aim is the face of his Lord, the Most High, bringing purification under the same divine name that opens the section.
- (92:21) [luna: strong; basis: contrast+theme] وَلَسَوْفَ يَرْضَىٰ
  Unverified discovery rationale: luna: The giver will be pleased; that promised outcome completes the section’s contrast between preferring near life and the better, lasting Hereafter.
- (95:4) [terra: strong; basis: root+scene+theme] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ
  Unverified discovery rationale: terra: Humanity is created in the finest form, supplying the well-fashioned body in the section's craft image.
- (95:6) [terra: strong; basis: neighbour+root+theme] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ
  Unverified discovery rationale: terra: Faith and good works receive an unending reward, completing the reversal from the lowest condition to what endures.
- (96:1) [terra: strong (missing-ayat turn); basis: root+speaker+theme] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
  Unverified discovery rationale: terra: The command to recite in the name of the Lord who created joins recitation, the divine name, and creation in one opening.
- (96:2) [terra: strong (missing-ayat turn); basis: neighbour+root+scene] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
  Unverified discovery rationale: terra: God creates the human from a clinging clot, giving the bodily scene attached to that command.
- (96:9) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
  Unverified discovery rationale: terra: A question introduces the person who forbids God's servant, opening a concrete obstruction of the prayer response.
- (96:10) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] عَبْدًا إِذَا صَلَّىٰٓ
  Unverified discovery rationale: terra: What he forbids is a servant praying, the direct inverse of the section's person who remembers his Lord and prays.
- (96:12) [terra: strong (missing-ayat turn); basis: contrast+root+theme] أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
  Unverified discovery rationale: terra: The forbidden servant may stand upon guidance and command piety, showing what the attempt to stop prayer actually opposes.
- (96:19) [terra: strong (missing-ayat turn); basis: scene+speaker+theme] كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩
  Unverified discovery rationale: terra: The Prophet is told not to obey the opponent but to prostrate and draw near, resolving the conflict through the same posture as the believing magicians.
- (98:2) [terra: strong; basis: root+scene+theme] رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
  Unverified discovery rationale: terra: God's messenger recites purified scrolls, bringing recitation and purification into the same written object recalled at the section's close.
- (98:3) [terra: strong; basis: neighbour+root+theme] فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
  Unverified discovery rationale: terra: Those scrolls contain upright writings, specifying the enduring content carried by the purified pages.

## medium (43)

- (3:44) [terra: medium (missing-ayat turn); basis: scene+theme] ذَٰلِكَ مِنْ أَنۢبَآءِ ٱلْغَيْبِ نُوحِيهِ إِلَيْكَ ۚ وَمَا كُنتَ لَدَيْهِمْ إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ وَمَا كُنتَ لَدَيْهِمْ إِذْ يَخْتَصِمُونَ
  Unverified discovery rationale: terra: The guardians cast their pens to determine who would care for Mary, another Quranic scene of selecting a share by cast shafts.
- (6:59) [luna: medium (missing-ayat turn); basis: scene+theme] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: God’s knowledge reaches a grain in the earth’s darkness and every leaf that falls; these concrete hidden plant details meet the section’s pasture and its claim that God knows what is hidden.
- (7:58) [luna: medium (missing-ayat turn); basis: contrast+scene] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
  Unverified discovery rationale: luna: Good land brings forth vegetation by its Lord’s leave, while bad land yields little; this gives the section’s growing field and drying pasture a specific fertile-versus-barren boundary.
- (9:38) [terra: medium; basis: root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ ۚ فَمَا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا قَلِيلٌ
  Unverified discovery rationale: terra: The believers are challenged for being content with worldly life instead of the Hereafter and told its enjoyment is slight, sharpening the scale of the choice.
- (14:3) [terra: medium; basis: root+theme] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
  Unverified discovery rationale: terra: Those who prefer worldly life over the Hereafter also obstruct God's path, joining bad preference to loss of the guided road.
- (14:5) [luna: medium (missing-ayat turn); basis: speaker+theme] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ أَنْ أَخْرِجْ قَوْمَكَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
  Unverified discovery rationale: luna: Moses is sent to bring his people from darkness into light; this is a specific mission-level counterpart to the section’s fire that gives Moses guidance, though the verse speaks metaphorically of deliverance rather than a flame.
- (16:11) [luna: medium (missing-ayat turn); basis: neighbour+scene] يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ وَٱلنَّخِيلَ وَٱلْأَعْنَٰبَ وَمِن كُلِّ ٱلثَّمَرَٰتِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The ayah names crops, palms, grapes, and other fruits grown by that water; 16:10 supplies the rain and grazing pasture, while this neighbor contributes the harvested abundance that meets the section’s cultivated field.
- (16:95) [terra: medium (missing-ayat turn); basis: neighbour+root+theme] وَلَا تَشْتَرُوا۟ بِعَهْدِ ٱللَّهِ ثَمَنًۭا قَلِيلًا ۚ إِنَّمَا عِندَ ٱللَّهِ هُوَ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: God's covenant must not be exchanged for a small price because what is with God is better, supplying the act of choice immediately before what remains in 16:96.
- (16:107) [terra: medium; basis: root+theme] ذَٰلِكَ بِأَنَّهُمُ ٱسْتَحَبُّوا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَأَنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: The condemned choice is explained as preferring worldly life over the Hereafter, a direct repeated use of the section's preference.
- (18:28) [terra: medium; basis: root+theme] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
  Unverified discovery rationale: terra: The Prophet must not follow one whose heart neglects God's remembrance and follows desire, connecting failed remembrance to worldly preference.
- (18:29) [terra: medium; basis: neighbour+scene+theme] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
  Unverified discovery rationale: terra: Truth is offered as a choice, but refusal leads to a surrounding fire; this gives the reminder-choice-fire sequence a concrete boundary.
- (18:96) [terra: medium (missing-ayat turn); basis: scene+theme] ءَاتُونِى زُبَرَ ٱلْحَدِيدِ ۖ حَتَّىٰٓ إِذَا سَاوَىٰ بَيْنَ ٱلصَّدَفَيْنِ قَالَ ٱنفُخُوا۟ ۖ حَتَّىٰٓ إِذَا جَعَلَهُۥ نَارًۭا قَالَ ءَاتُونِىٓ أُفْرِغْ عَلَيْهِ قِطْرًۭا
  Unverified discovery rationale: terra: Iron is heated until it becomes fire and molten copper is poured over it, a concrete craft-and-smelting scene behind the section's fire-borne metal foam.
- (20:7) [terra: medium; basis: root+theme] وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى
  Unverified discovery rationale: terra: God knows the secret and what is still more hidden, a close verbal and contextual counterpart to the hidden knowledge later named at the fire.
- (20:26) [terra: medium; basis: root+scene+speaker] وَيَسِّرْ لِىٓ أَمْرِى
  Unverified discovery rationale: terra: Moses asks his Lord to ease his task, placing the section's promised ease in the same life that is selected at the fire.
- (21:105) [terra: medium (missing-ayat turn); basis: root+theme] وَلَقَدْ كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ أَنَّ ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ
  Unverified discovery rationale: terra: God wrote in an earlier scripture, after the Reminder, that righteous servants inherit the earth; scripture, remembrance, writing, and lasting benefit meet specifically.
- (29:64) [terra: medium; basis: contrast+theme] وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ ۚ وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: terra: Worldly life is play and diversion while the Home of the Hereafter is the true life, clarifying the section's lower life and its state that is neither death nor real life.
- (35:22) [terra: medium; basis: contrast+theme] وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ ۚ إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ ۖ وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ
  Unverified discovery rationale: terra: The living and dead are not equal, and the Prophet cannot make those in graves hear; this boundary clarifies why the fire's neither-dead-nor-living state is anomalous.
- (36:33) [terra: medium (missing-ayat turn); basis: scene+theme] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
  Unverified discovery rationale: terra: Dead earth is revived and grain is brought from it for people to eat, another direct meeting of life, field, and provision.
- (37:141) [terra: medium; basis: scene+theme] فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ
  Unverified discovery rationale: terra: Jonah participates in drawing lots and becomes the losing party, another concrete scene in which an allotted share is selected rather than freely preferred.
- (40:39) [terra: medium; basis: theme] يَٰقَوْمِ إِنَّمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَا مَتَٰعٌۭ وَإِنَّ ٱلْءَاخِرَةَ هِىَ دَارُ ٱلْقَرَارِ
  Unverified discovery rationale: terra: The believer in Pharaoh's court calls worldly life brief enjoyment and the Hereafter the enduring home, restating the magician scene's scale in another Pharaonic speech.
- (53:45) [terra: medium (missing-ayat turn); basis: root+scene] وَأَنَّهُۥ خَلَقَ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰ
  Unverified discovery rationale: terra: God creates the two sexes, male and female, a bodily creation claim within the passage following the scrolls of Abraham and Moses.
- (53:46) [terra: medium (missing-ayat turn); basis: neighbour+scene] مِن نُّطْفَةٍ إِذَا تُمْنَىٰ
  Unverified discovery rationale: terra: That pair comes from a drop when emitted, specifying the bodily origin in the same scriptural sequence.
- (56:96) [terra: medium; basis: root+speaker+theme] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
  Unverified discovery rationale: terra: After the surah's divisions of death, reward, and fire, the command again tells the hearer to glorify the name of the mighty Lord, matching the section's framing command.
- (69:52) [terra: medium; basis: root+speaker] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
  Unverified discovery rationale: terra: The hearer is commanded to glorify the name of the mighty Lord after revelation is affirmed as certain truth, another exact stance of name-centered glorification.
- (75:20) [terra: medium; basis: root+theme] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
  Unverified discovery rationale: terra: People are said to love the immediate life, a close nonlexical parallel to preferring the nearer worldly life.
- (75:21) [terra: medium; basis: neighbour+theme] وَتَذَرُونَ ٱلْءَاخِرَةَ
  Unverified discovery rationale: terra: They leave the Hereafter aside, completing the two-sided preference begun in 75:20.
- (76:27) [terra: medium; basis: root+theme] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
  Unverified discovery rationale: terra: People love the immediate life and leave behind a weighty Day, again linking preference to neglect of the lasting reckoning.
- (76:29) [terra: medium; basis: root+theme] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًۭا
  Unverified discovery rationale: terra: The revelation is called a reminder, and whoever wills may take a way to his Lord, joining recollection, choice, and road.
- (76:30) [terra: medium; basis: neighbour+root+theme] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
  Unverified discovery rationale: terra: Human willing is dependent on God's will, repeating the section's boundary on choice and retention.
- (76:31) [terra: medium; basis: neighbour+scene+theme] يُدْخِلُ مَن يَشَآءُ فِى رَحْمَتِهِۦ ۚ وَٱلظَّٰلِمِينَ أَعَدَّ لَهُمْ عَذَابًا أَلِيمًۢا
  Unverified discovery rationale: terra: God admits whom He wills into mercy while preparing painful punishment for wrongdoers, completing the two destinations after the chosen way.
- (77:20) [terra: medium; basis: root+scene] أَلَمْ نَخْلُقكُّم مِّن مَّآءٍۢ مَّهِينٍۢ
  Unverified discovery rationale: terra: Human creation begins from a lowly fluid, opening a womb-and-measure sequence parallel to the section's fashioned embryo.
- (79:46) [terra: medium (missing-ayat turn); basis: theme] كَأَنَّهُمْ يَوْمَ يَرَوْنَهَا لَمْ يَلْبَثُوٓا۟ إِلَّا عَشِيَّةً أَوْ ضُحَىٰهَا
  Unverified discovery rationale: terra: When people see the Hour, worldly duration will seem no longer than an evening or morning, a specific measure of how little the preferred near life lasts.
- (80:1) [luna: medium; basis: contrast+neighbour+scene] عَبَسَ وَتَوَلَّىٰٓ
  Unverified discovery rationale: luna: The Prophet frowns and turns away; 80:2 identifies the approaching person as blind. This reverses the section’s wretched person turning away from the reminder, since here the messenger turns from the one seeking it.
- (80:5) [luna: medium; basis: contrast+neighbour+theme] أَمَّا مَنِ ٱسْتَغْنَىٰ
  Unverified discovery rationale: luna: The other man thinks himself self-sufficient; 80:6–7 complete the scene of the Prophet attending to him although he does not purify himself. This is a specific counterpart to the section’s preferrer of worldly life and avoids treating the two scenes as identical.
- (80:6) [luna: medium; basis: contrast+neighbour+speaker] فَأَنتَ لَهُۥ تَصَدَّىٰ
  Unverified discovery rationale: luna: The Prophet devotes attention to the self-sufficient man; 80:5 names his stance and 80:7 says his failure to purify is not the Prophet’s responsibility. This contrasts with the section’s reminder offered to two audiences.
- (80:7) [luna: medium; basis: contrast+neighbour+theme] وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ
  Unverified discovery rationale: luna: The Prophet is told that the other man’s failure to purify is not his charge; 80:5–6 supply that man’s self-sufficiency and the Prophet’s attention to him. This marks a boundary on the section’s call to remind.
- (80:10) [luna: medium; basis: contrast+neighbour+speaker] فَأَنتَ عَنْهُ تَلَهَّىٰ
  Unverified discovery rationale: luna: The fearful visitor is left unattended in the episode; 80:8–9 identify his haste and fear, while this ayah contributes the Prophet’s distraction from him, a reversal of the section’s fearful hearer taking heed.
- (80:24) [luna: medium (missing-ayat turn); basis: neighbour+scene] فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ
  Unverified discovery rationale: luna: The listener is told to look at human food; 80:25–32 complete the scene with rain, split earth, crops, fruit, herbage, and provision for people and livestock, while this ayah contributes the call to attend to that provision.
- (80:28) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَعِنَبًۭا وَقَضْبًۭا
  Unverified discovery rationale: luna: Grapes and fodder follow the grain; with 80:25–27 supplying rain, opened earth, and growth, this ayah adds plant food and herbage to the passage’s provision scene.
- (80:29) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَزَيْتُونًۭا وَنَخْلًۭا
  Unverified discovery rationale: luna: Olives and date palms continue the list of crops; this ayah’s own contribution is the orchard yield within the rain-grown field passage at 80:25–32.
- (80:30) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَحَدَآئِقَ غُلْبًۭا
  Unverified discovery rationale: luna: The next crop image is dense, lush gardens; this adds cultivated abundance to the section’s contrast between pasture that dries and a field whose yield is tended.
- (80:31) [luna: medium (missing-ayat turn); terra: medium; basis: neighbour+scene] وَفَٰكِهَةًۭ وَأَبًّۭا
  Unverified discovery rationale: luna: The ayah names fruit and fodder; its fodder detail is especially close to the source pasture, while 80:25–30 supply the growth that precedes it. | terra: Fruit and pasture are among the products of the split earth, bringing crop and grazing growth together.
- (93:4) [terra: medium (missing-ayat turn); basis: root+theme] وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ
  Unverified discovery rationale: terra: What comes later is declared better for the Prophet than what came first, a compact temporal analogue to the Hereafter being better than the nearer life.

## weak (1)

- (21:69) [luna: weak (missing-ayat turn); basis: contrast+scene] قُلْنَا يَٰنَارُ كُونِى بَرْدًۭا وَسَلَٰمًا عَلَىٰٓ إِبْرَٰهِيمَ
  Unverified discovery rationale: luna: The section centers Moses’s fire and closes by naming Abraham, but does not itself connect Abraham to fire. Here God makes the fire cool and safe for Abraham, a specific contrary fire scene; 21:68 supplies the threat to burn him.

## contrast (13)

- (2:17) [terra: contrast; basis: contrast+scene+theme] مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ
  Unverified discovery rationale: terra: A kindled fire briefly gives light, but God removes the light and leaves its people in darkness; it reverses Moses' fire, which yields guidance rather than lost sight.
- (4:142) [terra: contrast (missing-ayat turn); basis: contrast+root+scene] إِنَّ ٱلْمُنَٰفِقِينَ يُخَٰدِعُونَ ٱللَّهَ وَهُوَ خَٰدِعُهُمْ وَإِذَا قَامُوٓا۟ إِلَى ٱلصَّلَوٰةِ قَامُوا۟ كُسَالَىٰ يُرَآءُونَ ٱلنَّاسَ وَلَا يَذْكُرُونَ ٱللَّهَ إِلَّا قَلِيلًۭا
  Unverified discovery rationale: terra: Hypocrites stand for prayer lazily, showing off and remembering God only a little, another precise boundary around genuine prayer and remembrance.
- (5:3) [terra: contrast; basis: contrast+scene+theme] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: Seeking a divided share by divining arrows is forbidden, providing a concrete boundary for the section's carved shaft and its movement from allotment to chosen share.
- (5:90) [terra: contrast; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: terra: Divining arrows are classed with abominations to be avoided so that people may prosper, opposing illicit selection by lots to true falah.
- (20:69) [terra: contrast; basis: contrast+root+scene] وَأَلْقِ مَا فِى يَمِينِكَ تَلْقَفْ مَا صَنَعُوٓا۟ ۖ إِنَّمَا صَنَعُوا۟ كَيْدُ سَٰحِرٍۢ ۖ وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ
  Unverified discovery rationale: terra: Immediately before the magicians prostrate, the magician is said not to prosper wherever he comes; their purification scene crosses from failed magic to the falah of the purified.
- (44:56) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
  Unverified discovery rationale: terra: The people of the Garden taste no death beyond the first death and are protected from Hell, the saved reversal of being trapped in fire without death or life.
- (74:42) [terra: contrast; basis: contrast+neighbour+scene] مَا سَلَكَكُمْ فِى سَقَرَ
  Unverified discovery rationale: terra: The people of Saqar are asked what brought them into the fire, opening an explicit fire-versus-prayer explanation.
- (74:43) [terra: contrast; basis: contrast+neighbour+root+scene] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
  Unverified discovery rationale: terra: They answer that they were not among those who prayed, making neglected prayer the boundary opposite the section's person who remembers and prays.
- (89:15) [terra: contrast (missing-ayat turn); basis: contrast+theme] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
  Unverified discovery rationale: terra: A human mistakes expanded provision and honor for proof that the Lord has honored him, exposing a false equation between worldly share and true height.
- (89:16) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+theme] وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
  Unverified discovery rationale: terra: He likewise mistakes restricted provision for humiliation, defining the boundary between measured provision and divine worth.
- (95:5) [terra: contrast; basis: contrast+root+theme] ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ
  Unverified discovery rationale: terra: The well-formed human is then returned to the lowest of the low, a stark descent from fashioned height that illuminates the lower-life image.
- (107:4) [terra: contrast (missing-ayat turn); basis: contrast+scene] فَوَيْلٌۭ لِّلْمُصَلِّينَ
  Unverified discovery rationale: terra: Woe is pronounced upon some who pray, establishing that the bodily act alone does not guarantee the section's saved branch.
- (107:5) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+root+theme] ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
  Unverified discovery rationale: terra: Those worshippers are heedless of their prayer, showing that prayer severed from remembrance reverses the section's pairing.

## neighbours: within two ayat of a passage the section cites (13)

- (13:15) [next to 13:17] وَلِلَّهِ يَسْجُدُ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ طَوْعًۭا وَكَرْهًۭا وَظِلَٰلُهُم بِٱلْغُدُوِّ وَٱلْءَاصَالِ ۩
- (13:16) [next to 13:17] قُلْ مَن رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ قُلِ ٱللَّهُ ۚ قُلْ أَفَٱتَّخَذْتُم مِّن دُونِهِۦٓ أَوْلِيَآءَ لَا يَمْلِكُونَ لِأَنفُسِهِمْ نَفْعًۭا وَلَا ضَرًّۭا ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ أَمْ هَلْ تَسْتَوِى ٱلظُّلُمَٰتُ وَٱلنُّورُ ۗ أَمْ جَعَلُوا۟ لِلَّهِ شُرَكَآءَ خَلَقُوا۟ كَخَلْقِهِۦ فَتَشَٰبَهَ ٱلْخَلْقُ عَلَيْهِمْ ۚ قُلِ ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ وَهُوَ ٱلْوَٰحِدُ ٱلْقَهَّٰرُ
- (13:18) [next to 13:17] لِلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمُ ٱلْحُسْنَىٰ ۚ وَٱلَّذِينَ لَمْ يَسْتَجِيبُوا۟ لَهُۥ لَوْ أَنَّ لَهُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لَٱفْتَدَوْا۟ بِهِۦٓ ۚ أُو۟لَٰٓئِكَ لَهُمْ سُوٓءُ ٱلْحِسَابِ وَمَأْوَىٰهُمْ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمِهَادُ
- (13:19) [next to 13:17] ۞ أَفَمَن يَعْلَمُ أَنَّمَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ كَمَنْ هُوَ أَعْمَىٰٓ ۚ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (20:8) [next to 20:10] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:9) [next to 20:10] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:17) [next to 20:15] وَمَا تِلْكَ بِيَمِينِكَ يَٰمُوسَىٰ
- (20:77) [next to 20:75] وَلَقَدْ أَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ أَنْ أَسْرِ بِعِبَادِى فَٱضْرِبْ لَهُمْ طَرِيقًۭا فِى ٱلْبَحْرِ يَبَسًۭا لَّا تَخَٰفُ دَرَكًۭا وَلَا تَخْشَىٰ
- (20:78) [next to 20:76] فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ
- (20:129) [next to 20:131] وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَكَانَ لِزَامًۭا وَأَجَلٌۭ مُّسَمًّۭى
- (20:130) [next to 20:131] فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا ۖ وَمِنْ ءَانَآئِ ٱلَّيْلِ فَسَبِّحْ وَأَطْرَافَ ٱلنَّهَارِ لَعَلَّكَ تَرْضَىٰ
- (27:6) [next to 27:8] وَإِنَّكَ لَتُلَقَّى ٱلْقُرْءَانَ مِن لَّدُنْ حَكِيمٍ عَلِيمٍ
- (27:10) [next to 27:8] وَأَلْقِ عَصَاكَ ۚ فَلَمَّا رَءَاهَا تَهْتَزُّ كَأَنَّهَا جَآنٌّۭ وَلَّىٰ مُدْبِرًۭا وَلَمْ يُعَقِّبْ ۚ يَٰمُوسَىٰ لَا تَخَفْ إِنِّى لَا يَخَافُ لَدَىَّ ٱلْمُرْسَلُونَ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 87, "section": 18, "run_tag": "sol-session-20261005", "source_sha256": "5e9ef0a461cc99bfb9b4c0e1b4609dd85b292c96610df2a0bb8cfe5bd670daa3", "list_sha256": "580cb7112c41f5204756d7e5ec70120dd436c3e25997b6d3cf40e0c40cc63cb6", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec18/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 41, "unique_additions": 41, "repeated_proposals": [], "turn1_sha256": "ebaf95e978ae7967270fb3c8c468e6a8162ebdc6d279b58e25962adbc2e16323", "followup_sha256": "317d46a438b0164870f7d764a630434ebdebe6062df16f32516e1e46fbb997f7", "proposal_file": "followup.tsv", "proposal_sha256": "317d46a438b0164870f7d764a630434ebdebe6062df16f32516e1e46fbb997f7", "list_sha256": "bb8b91cdb3e904eb969b2e30808590d4842d2faa197c39825a083b2a24bb7c0f", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec18/luna/list.tsv", "rows": 130, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 1, "ref": "13:17", "arabic": "غُثَاءً", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 26, "ref": "25:2", "arabic": "قَدَّرَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 57, "ref": "92:18", "arabic": "تَزَكَّىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 60, "ref": "79:37", "arabic": "وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["79:38"], "matching_ref_count": 1}, {"line": 93, "ref": "3:6", "arabic": "فَسَوَّىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 98, "ref": "79:31", "arabic": "المَرْعَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 112, "ref": "77:23", "arabic": "قَدَّرَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec18/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 109, "unique_additions": 109, "repeated_proposals": [], "turn1_sha256": "72f4159a708cdcff91c1ef6db554646af589fd2a25692b91b6857a61d5d180a6", "followup_sha256": "d28ba372654b0a3fe1aafbe35f1b3b1c1e2d43376d1c5e680b50ae7ef125871a", "proposal_file": "followup.tsv", "proposal_sha256": "d28ba372654b0a3fe1aafbe35f1b3b1c1e2d43376d1c5e680b50ae7ef125871a", "list_sha256": "c28ad42f34b798e4d1470ada1ae04d64b45c2c517c06ec944a8d91387733b9f5", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec18/terra/list.tsv", "rows": 288, "schema_errors": [], "duplicates": {}, "arabic_findings": [], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

