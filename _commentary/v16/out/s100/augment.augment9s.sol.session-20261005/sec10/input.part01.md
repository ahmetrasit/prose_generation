Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 10 of 11 ("Görmek, bilmek, içini bilmek"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 10 (prose paragraphs numbered) =====
[¶45] Surenin ikinci yarısı üç bilme biçimini sırayla dizer. Yedinci ayette insan tanıktır, dokuzuncu ayette bilip bilmediği sorulur, on birinci ayette ise Rabbinin onlardan haberdar olduğu söylenir. Tanıklığın kökü hazır bulunmak ve görmektir: {ar:الشهود والشهادة الحضور مع المشاهدة, tr:eş-şuhûdu ve'ş-şehâdetu'l-huzûru me'a'l-muşâhede, gloss:"şuhûd" ve "şehâdet", görerek hazır bulunmaktır, source:"ش ه د,B001"}. Tanıklık üç şeyi bir arada tutar: {ar:الشهادة يجمع الحضور والعلم والإعلام, tr:eş-şehâdetu yecma'u'l-huzûra ve'l-ilme ve'l-i'lâm, gloss:şahitlik, hazır bulunmayı, bilmeyi ve bildirmeyi bir araya getirir, source:"ش ه د,B002"}. Tanıklık aynı zamanda bir haberdir: {ar:الشهادة خبر قاطع, tr:eş-şehâdetu haberun kâtı', gloss:şahitlik kesin bir haberdir, source:"ش ه د,B002"}. Kökün ailesinde tanığın aleti de vardır: {ar:الشاهد اللسان, tr:eş-şâhidu'l-lisân, gloss:"şâhid", dildir, source:"ش ه د,B005"}. Dokuzuncu ayetin bilme fiili ise bir şeyi gerçeğiyle kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi-hakîkatih, gloss:bir şeyi hakikatiyle kavramak, source:"ع ل م,B001"}. Bu fiil de haberle bağlantılıdır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberik, ey mâ şa'artu bih, gloss:"haberini bilmedim", yani farkına varmadım, source:"ع ل م,B001"}. Son ayetin kelimesi bu iki bilgiyi bir araya getirir: {ar:الخبير العالم, tr:el-habîru'l-âlim, gloss:"habîr", bilendir, source:"خ ب ر,B001"}.Bu bilgi deneyerek kazanılır: {ar:الخبرة الاختبار, tr:el-hibratu'l-ihtibâr, gloss:"hibre", sınayarak denemektir, source:"خ ب ر,B001"}. Ulaştığı yer de işin iç yüzüdür: {ar:الخبرة المعرفة ببواطن الأمر, tr:el-hibratu'l-ma'rifetu bi-bevâtıni'l-emr, gloss:"hibre", işin iç yüzünü bilmektir, source:"خ ب ر,B001"}. Altıncı ayetteki insan kelimesinin kökü de bu sıralamanın başına bir duyu ekler: {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestu'ş-şey'e izâ raeytehû ve ânestuhû izâ semi'teh, gloss:bir şeyi gördüğünde de işittiğinde de "ânestu" dersin, source:"ء ن س,B002"}. Kök görmekten bilmeye kadar uzanır: {ar:آنست منه رشدا علمته, tr:ânestu minhu ruşden, alimtuh, gloss:"ondan bir olgunluk sezdim", yani onu öğrendim, source:"ء ن س,B002"}. Su başı deyimi de aynı yolu izler. Çok göletten içen kişi, işleri deneye deneye {ar:حتى خبرها, tr:hattâ haberahâ, gloss:sonunda iç yüzlerini öğrendi, source:"ن ق ع,B008"} diye anılır.

[¶46] Bu yolun sure içinde aldığı biçim şöyledir. Yedinci ayette insan hazırdır ve görmektedir. Kendi nankörlüğüne tanıktır, yani bilgisi gözünün önündedir. Dokuzuncu ayet buna rağmen bir soru sorar: {ar:أَفَلَا يَعْلَمُ, tr:e-fe-lâ ya'lem, gloss:bilmez mi, source:100:9}. Bu soru, görmekle bilmek arasındaki boşluğu açığa çıkarır. İnsan kendi halini görür ama bu halin nereye varacağını hakikatiyle kavramaz. Sure soruya cevap vermez. Cevabın yerine Rabbin bilgisini koyar: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevme'izin le-habîr, gloss:şüphesiz Rableri o gün onlardan tamamen haberdardır, source:100:11}. Ayet "yaptıklarından" demez, "onlardan" der. Bilginin konusu insanın kendisidir. "Habîr" kelimesi görünüşe değil iç yüze bakar. Böylece surenin bilgi sırası, insanın kendi dışını görmesinden Rabbin onun içini bilmesine doğru ilerler.

[¶47] Kur'an aynı kuruluşu bir başka surede de kullanır. Allah sözü gizlenen ile açığa vurulanı bir tutar: {ar:وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌ بِذَاتِ ٱلصُّدُورِ, tr:ve esirrû kavlekum evi'cherû bih, innehû alîmun bi-zâti's-sudûr, gloss:sözünüzü gizleyin ya da açığa vurun; O, göğüslerin içindekini bilendir, source:67:13}. Ardından bir soru gelir: {ar:أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ, tr:e-lâ ya'lemu men halak, ve huve'l-latîfu'l-habîr, gloss:yaratan bilmez mi? O, en ince şeyi bilen ve her şeyden haberdar olandır, source:67:14}. Göğüsler, "bilmez mi" sorusu ve "habîr" bu iki ayette de bu sırayla dizilir. Ancak soru orada yaratanın bilgisi üzerine sorulur, bizim surede ise insanın bilgisi üzerine. Bir başka yerde insan kendi kendisinin tanığıdır: {ar:يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍ بِمَا قَدَّمَ وَأَخَّرَ, tr:yunebbeu'l-insânu yevme'izin bimâ kaddeme ve ahhar, gloss:o gün insana öne sürdüğü ve geride bıraktığı bildirilir, source:75:13}; {ar:بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌ, tr:beli'l-insânu alâ nefsihî basîra, gloss:aslında insan kendi kendine karşı bir göz, bir tanıktır, source:75:14}; {ar:وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ, tr:ve lev elkâ meâzîreh, gloss:mazeretlerini ortaya dökse bile, source:75:15}. Kökün "dil" anlamı da o günün tanıklığında yer alır: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ, tr:yevme teşhedu aleyhim elsinetuhum ve eydîhim ve erculuhum bimâ kânû ya'melûn, gloss:o gün dilleri, elleri ve ayakları yaptıklarına dair aleyhlerine tanıklık eder, source:24:24}. Bedenin kendi derisine sorduğu soru da kaydedilir: {ar:وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا ۖ قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ, tr:ve kâlû li-culûdihim lime şehidtum aleynâ, kâlû entakanâ'llâhu'llezî entaka kulle şey', gloss:derilerine "neden aleyhimize tanıklık ettiniz" derler; onlar da "her şeyi konuşturan Allah bizi konuşturdu" der, source:41:21}. İnsanın içine dair bilgi en yakın yerden gelir: {ar:وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve le-kad halakna'l-insâne ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:insanı biz yarattık ve nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Görünüşte iman edip sıkıntı gelince dönen kişi için de şu sorulur: {ar:أَوَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِمَا فِى صُدُورِ ٱلْعَٰلَمِينَ, tr:e-ve-leysa'llâhu bi-a'leme bimâ fî sudûri'l-âlemîn, gloss:Allah, âlemlerin göğüslerinde olanı en iyi bilen değil midir, source:29:10}. Yerin kendisi de o gün bir haberci olur: {ar:يَوْمَئِذٍ تُحَدِّثُ أَخْبَارَهَا, tr:yevme'izin tuhaddisu ahbârahâ, gloss:o gün yer haberlerini anlatır, source:99:4}. Haberlerini anlatan bu yer, kabirleri altüst edilen yerdir. "Ahbâr" kelimesi de surenin son kelimesiyle aynı köktendir.

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: chain 7 (rain on the land) as its own section - merged into chain 6 as one image of kenûd
- not developed: chain 9 (shared pot) as its own section - merged into chain 8 as the counter-scene of the closed hand
- not developed: غ ي ر B001 "God's rain/provision" member in chains 6 and 7 - wrong root for al-mughīrāt, dropped
- not developed: ضبح as owl and echo calls (chain 4) - relies on pre-Islamic lore outside the Quran, dropped
- not developed: ربيون "great crowds" (chain 11) - too loose a link to rabb, dropped
- not developed: the map's meysir lore (chain 9) and its commentators remark (chain 6) - reports from outside the Quran, dropped
- memory: al-mughīrāt is the form IV participle of أغار "to raid", root غ و ر
- memory: غار يغير "to provide rain" is a separate verb and not the root of al-mughīrāt
- memory: the preposition عن in 38:32 can mean both "because of" and "away from"

===== passages from the discovery list (243) =====
## strong (170)

- (2:77) [terra: strong; basis: speaker+theme] أَوَلَا يَعْلَمُونَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
  Unverified discovery rationale: terra: أَوَلَا يَعْلَمُونَ أَنَّ اللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ asks whether people know that God knows both their secret and public expression.
- (2:140) [terra: strong; basis: root+speaker+theme] أَمْ تَقُولُونَ إِنَّ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطَ كَانُوا۟ هُودًا أَوْ نَصَٰرَىٰ ۗ قُلْ ءَأَنتُمْ أَعْلَمُ أَمِ ٱللَّهُ ۗ وَمَنْ أَظْلَمُ مِمَّن كَتَمَ شَهَٰدَةً عِندَهُۥ مِنَ ٱللَّهِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
  Unverified discovery rationale: terra: أَأَنْتُمْ أَعْلَمُ أَمِ اللَّهُ confronts human knowledge, then condemns concealing testimony and says God is not unaware; it closely parallels the section's unanswered human question and divine answer.
- (2:143) [terra: strong (missing-ayat turn); basis: root+theme] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: The change of direction serves to make known who follows the messenger and who turns back; an observable response to trial discloses allegiance.
- (2:204) [terra: strong (missing-ayat turn); basis: root+theme] وَمِنَ ٱلنَّاسِ مَن يُعْجِبُكَ قَوْلُهُۥ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَيُشْهِدُ ٱللَّهَ عَلَىٰ مَا فِى قَلْبِهِۦ وَهُوَ أَلَدُّ ٱلْخِصَامِ
  Unverified discovery rationale: terra: A speaker calls God to witness what is in his heart while his conduct makes him the fiercest adversary; claimed inward testimony and the person's true condition sharply diverge.
- (2:235) [terra: strong (missing-ayat turn); basis: theme] وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا عَرَّضْتُم بِهِۦ مِنْ خِطْبَةِ ٱلنِّسَآءِ أَوْ أَكْنَنتُمْ فِىٓ أَنفُسِكُمْ ۚ عَلِمَ ٱللَّهُ أَنَّكُمْ سَتَذْكُرُونَهُنَّ وَلَٰكِن لَّا تُوَاعِدُوهُنَّ سِرًّا إِلَّآ أَن تَقُولُوا۟ قَوْلًۭا مَّعْرُوفًۭا ۚ وَلَا تَعْزِمُوا۟ عُقْدَةَ ٱلنِّكَاحِ حَتَّىٰ يَبْلُغَ ٱلْكِتَٰبُ أَجَلَهُۥ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِىٓ أَنفُسِكُمْ فَٱحْذَرُوهُ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
  Unverified discovery rationale: terra: God knows what people harbor within themselves even when a matter is kept as a secret promise, making the self's unspoken content the object of knowledge.
- (2:283) [luna: strong; terra: strong; basis: root+scene+theme] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section treats testimony as a decisive report that joins knowing and informing; this ayah forbids concealing testimony and locates the sin of concealment in the heart. | terra: Concealing testimony makes the heart sinful, and God knows what people do; spoken witness, hidden interior, and divine knowledge meet in one warning.
- (2:284) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The section says 100:10 gathers what is in people's breasts and 100:11 says the Lord knows them; this ayah says whether people reveal or conceal what is within themselves, God will call them to account. | terra: Whether people reveal or conceal what is within themselves, God will call them to account for it; inward content itself becomes the object of judgment.
- (3:18) [terra: strong; basis: root+theme] شَهِدَ ٱللَّهُ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا هُوَ وَٱلْمَلَٰٓئِكَةُ وَأُو۟لُوا۟ ٱلْعِلْمِ قَآئِمًۢا بِٱلْقِسْطِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: terra: God bears witness, along with angels and أُولُو الْعِلْمِ, to the truth of His oneness; testimony and knowledge converge in one decisive declaration.
- (3:29) [luna: strong (missing-ayat turn); terra: strong; basis: scene+speaker+theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section says God's knowledge reaches the person beyond what is visible; this ayah directly says He knows what people conceal within themselves and what they reveal. | terra: People are told that whether they hide what is in their breasts or reveal it, God knows it; the visible-hidden distinction cannot limit divine knowledge.
- (3:30) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: terra: On the day every soul finds its good and evil deeds present, the person's moral interior history stands visibly before it.
- (3:118) [terra: strong; basis: scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ بِطَانَةًۭ مِّن دُونِكُمْ لَا يَأْلُونَكُمْ خَبَالًۭا وَدُّوا۟ مَا عَنِتُّمْ قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ ۖ إِن كُنتُمْ تَعْقِلُونَ
  Unverified discovery rationale: terra: Hatred appears from mouths while what breasts conceal is greater, a precise outward sign/inner reality relation.
- (3:119) [terra: strong; basis: neighbour+theme] هَٰٓأَنتُمْ أُو۟لَآءِ تُحِبُّونَهُمْ وَلَا يُحِبُّونَكُمْ وَتُؤْمِنُونَ بِٱلْكِتَٰبِ كُلِّهِۦ وَإِذَا لَقُوكُمْ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ عَضُّوا۟ عَلَيْكُمُ ٱلْأَنَامِلَ مِنَ ٱلْغَيْظِ ۚ قُلْ مُوتُوا۟ بِغَيْظِكُمْ ۗ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: After private rage exposes the group behind its public face, God is said to know ذات الصدور; divine knowledge reaches what social observation only partly detects.
- (3:142) [terra: strong (missing-ayat turn); basis: root+speaker+theme] أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ وَلَمَّا يَعْلَمِ ٱللَّهُ ٱلَّذِينَ جَٰهَدُوا۟ مِنكُمْ وَيَعْلَمَ ٱلصَّٰبِرِينَ
  Unverified discovery rationale: terra: The question denies entry into the Garden before the strivers and steadfast are made known; trial reveals the reality behind aspiration.
- (3:154) [luna: strong; terra: strong; basis: root+scene+theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section distinguishes visible state from what is inside the person; this ayah says the trial was to test what was in breasts and purify what was in hearts. | terra: The trial is said to test what is in breasts and purify what is in hearts, followed by God's knowledge of ذات الصدور; experiential testing reaches the hidden interior.
- (3:166) [terra: strong; basis: neighbour+root+theme] وَمَآ أَصَٰبَكُمْ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ فَبِإِذْنِ ٱللَّهِ وَلِيَعْلَمَ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: The battlefield event occurs so that God may make the believers known, treating lived trial as a disclosure of real condition.
- (3:167) [terra: strong; basis: neighbour+root+theme] وَلِيَعْلَمَ ٱلَّذِينَ نَافَقُوا۟ ۚ وَقِيلَ لَهُمْ تَعَالَوْا۟ قَٰتِلُوا۟ فِى سَبِيلِ ٱللَّهِ أَوِ ٱدْفَعُوا۟ ۖ قَالُوا۟ لَوْ نَعْلَمُ قِتَالًۭا لَّٱتَّبَعْنَٰكُمْ ۗ هُمْ لِلْكُفْرِ يَوْمَئِذٍ أَقْرَبُ مِنْهُمْ لِلْإِيمَٰنِ ۚ يَقُولُونَ بِأَفْوَٰهِهِم مَّا لَيْسَ فِى قُلُوبِهِمْ ۗ وَٱللَّهُ أَعْلَمُ بِمَا يَكْتُمُونَ
  Unverified discovery rationale: terra: The same trial makes hypocrites known: they say with mouths what is not in hearts, while God best knows what they conceal.
