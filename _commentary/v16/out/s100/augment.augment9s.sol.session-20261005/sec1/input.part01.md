Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 1 of 11 ("Koşan at: soluk, adım, inceltilmiş beden"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 1 (prose paragraphs numbered) =====
[¶2] Sure, kim olduklarını adlarıyla değil, yalnızca yaptıklarıyla bildiren bir topluluk üzerine yeminle açılır: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}. Surenin hiçbir yerinde "at" kelimesi geçmez. Hayvan koşusundan, soluğundan, taşa vuran ayağından ve kaldırdığı tozdan tanınır. Kur'an başka yerlerde de yemini böyle açar: işiyle tanımlanan dişil çoğul bir topluluk getirir ve her yeni hareketi "fe" ile bir öncekinin hemen ardına bağlar. Bir örnek {ar:وَٱلصَّٰٓفَّٰتِ صَفًّا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1} ile {ar:فَٱلزَّٰجِرَٰتِ زَجْرًا, tr:fe'z-zâcirâti zecrâ, gloss:derken sürüp önlerine katanlara, source:37:2} çiftidir. Bir başkası {ar:وَٱلْمُرْسَلَٰتِ عُرْفًا, tr:ve'l-murselâti urfâ, gloss:ardı ardına gönderilenlere andolsun, source:77:1} ile {ar:فَٱلْعَٰصِفَٰتِ عَصْفًا, tr:fe'l-âsıfâti asfâ, gloss:derken fırtına gibi esenlere, source:77:2} çiftidir. Bu surede "fe" bağları koşuyu, kıvılcımı, sabahı, tozu ve kalabalığın ortasını tek bir hareketin ardışık aşamaları olarak dizer. Aşağıda bir kelimenin akrabalarından gelen görüntüler, o kelimenin ayetteki anlamının yanında duyulan ikinci bir ses olarak okunur. Bu görüntüler o anlamın yerine geçmez.

[¶3] Birinci ayetin ilk kelimesinin kökü, koşunun en hızlısını adlandırır: {ar:العَدْو هو الحضر, tr:el-advu huve'l-hudr, gloss:adv dörtnala koşmaktır, source:"ع د و,B002"}. İyi ve çok koşan ata da aynı kökten bir sıfat verilir: {ar:يقال من عدو الفرس عدوان أي جيد العدو وكثيره, tr:yukâlu min advi'l-ferasi advân, ey ceyyidu'l-advi ve kesîruh, gloss:atın koşusundan "advân" denir, yani iyi ve çok koşan, source:"ع د و,B002"}. Ardından gelen kelime bu koşunun sesidir: {ar:صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة, tr:savtu enfâsi'l-hayli izâ adevne ve leyse bi-sahîlin ve lâ hamhame, gloss:atların koşarken çıkardığı soluk sesi; ne kişneme ne homurtu, source:"ض ب ح,B001"}. Kişneme, hayvanın kendi sesidir. Burada duyulan ise zorlanan göğüsten dışarı itilen nefestir, yani kelime bir çabayı kulağa duyurur. Aynı kelime bir adım biçimini de adlandırır: {ar:ضبح الفرس وضبع إذا حرك ضبعيه في مشيه, tr:dabaha'l-ferasu ve daba'a izâ harreke dab'ayhi fî meşyih, gloss:at yürürken ön kollarını ileri atıp oynatınca "dabaha" denir, source:"ض ب ح,B002"}. Bu, {ar:هو عدو فوق التقريب وأصله ضبع, tr:huve advun fevka't-takrîbi ve asluhû dab', gloss:tırıştan hızlı bir koşudur, aslı "dab'"dır, source:"ض ب ح,B002"}. Böylece tek kelimede hem ileri uzanan ön ayaklar görülür hem de göğüsten çıkan nefes işitilir.

[¶4] İkinci ayetin {ar:قَدْحًا, tr:kadhâ, gloss:çakarak, source:100:2} kelimesi ateşi anlatır. Ama bu kökün kalıplaşmış bir söyleyişi atın bedenini de gösterir: {ar:قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح, tr:kaddaha'l-ferasu takdîhan izâ damura hattâ yasîra misle'l-kıdh, gloss:at, ok çubuğu gibi oluncaya dek inceltildiğinde "kaddaha" denir, source:"ق د ح,B008"}. Koşu için yetiştirilen at fazlasından arındırılır ve gövdesi bir ok çubuğu kadar inceltilir. Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesinin yanında da aynı kökten bir at deyimi duyulur: {ar:استجمع الفرس جريا, tr:isteceme'a'l-ferasu cerye, gloss:at bütün koşusunu tek bir atılışta topladı, source:"ج م ع,B010"}.

[¶5] Atın kökleri, insanı anlatan ayetlerde de geri gelir. Altıncı ayetteki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:100:6} kelimesinin kökü, bineğin bir yanını adlandırır: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbeti li'l-cânibi'llezî yelî'r-râkib, gloss:hayvanın "insî" yanı, binicinin bulunduğu taraftır, source:"ء ن س,B004"}. Hayvanın bir yanı insana dönüktür ve insan onun sırtındadır. Yedinci ayetteki {ar:لَشَهِيدٌ, tr:le-şehîd, gloss:elbette tanıktır, source:100:7} kelimesinin kökünde ise atın koşusu kendi kendinin tanığıdır: {ar:الشاهد من جريه ما يشهد له على سبقه وجودته, tr:eş-şâhidu min caryihî mâ yeşhedu lehû alâ sebkıhî ve cevdetih, gloss:koşusunun "tanığı", öne geçtiğine ve iyi cins olduğuna tanıklık eden kısımdır, source:"ش ه د,B008"}. Sekizinci ayetteki {ar:لَشَدِيدٌ, tr:le-şedîd, gloss:pek düşkündür, source:100:8} kelimesinin kökü de koşunun adıdır: {ar:الشد العدو والفعل اشتد, tr:eş-şeddu'l-advu ve'l-fi'lu iştedde, gloss:"şedd" koşudur, fiili "iştedde"dir, source:"ش د د,B003"}. Bu söyleyiş "şedd"i birinci ayetin "adv"ıyla aynı tanımda birleştirir. Onuncu ayetin {ar:ٱلصُّدُورِ, tr:es-sudûr, gloss:göğüsler, source:100:10} kelimesinin kökünde de yarışı göğsüyle kazanan at vardır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-ferasu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle öne geçerek gelince "sadera" denir, source:"ص د ر,B002"}.

[¶6] Bu görüntü sureye bir karşılaştırma katar. At soluğunu, bacaklarını, inceltilmiş bedenini ve bütün koşusunu sahibinin işine verir. Koşusu öne geçtiğine tanıklık eder, yarışı göğsüyle kazanır. Hemen ardından insan gelir ve onun hakkında söylenen ilk şey, Rabbine karşı {ar:لَكَنُودٌ, tr:le-kenûd, gloss:pek nankördür, source:100:6} olmasıdır. Atın tanığı kendi lehinedir, insanın tanıklığı ise kendi nankörlüğü üzerinedir. Atın "şedd"i koşusudur, insanınki ise malı sevmesidir. Göğüs at için yarışın kazanıldığı yerdir, insan için ise içindekilerin ayıklanacağı yerdir.

[¶7] Kur'an atları, sevilen malı ve Rab sözünü başka bir sahnede de bir araya getirir. Akşamüstü Süleyman'a soylu, çevik atlar sunulur: {ar:إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ, tr:iz uride aleyhi bi'l-aşiyyi's-sâfinâtu'l-ciyâd, gloss:akşamüstü ona durup bekleyen soylu atlar sunulduğunda, source:38:31}. Süleyman şöyle der: {ar:إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى, tr:innî ahbebtu hubbe'l-hayri an zikri rabbî, gloss:ben "hayır" sevgisini Rabbimin anılmasına bağlı olarak sevdim, source:38:32}. Arapçada "an" edatı hem "-den ötürü" hem "-den uzaklaşarak" anlamını taşıyabildiği için bu cümle iki yöne açıktır. Ama sözün devamı sabittir: {ar:حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ, tr:hattâ tevârat bi'l-hicâb, gloss:ta ki perdenin ardına gizleninceye dek, source:38:32}. Ardından {ar:رُدُّوهَا عَلَىَّ ۖ فَطَفِقَ مَسْحًا بِٱلسُّوقِ وَٱلْأَعْنَاقِ, tr:ruddûhâ aleyye, fe-tafika meshan bi's-sûkı ve'l-a'nâk, gloss:"Onları bana geri getirin" dedi ve bacaklarını, boyunlarını meshetmeye koyuldu, source:38:33}. Sekizinci ayetin "hubbu'l-hayr" ifadesi burada bir peygamberin ağzında, atlarla ve "Rabbim" sözüyle birlikte geçer. Bizim surede aynı ifade atların koşusundan hemen sonra, Rabbine nankör olan insanın bağlılığını adlandırır. Kur'an, insanlara süslü gösterilen sevgilerin listesine atları da koyar: {ar:زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ, tr:zuyyine li'n-nâsi hubbu'ş-şehevât, gloss:arzulanan şeylerin sevgisi insanlara süslü gösterildi, source:3:14}. O listede altın ve gümüş yığınlarının yanında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ, tr:ve'l-hayli'l-musevveme, gloss:salma, damgalı atlar, source:3:14} de sayılır. Böylece at hem koşan bir hayvan hem de sevilen bir maldır. Surenin karşılaştırması bu iki yüzün arasında kurulur.

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

===== passages from the discovery list (170) =====
## strong (79)

- (2:165) [luna: strong; terra: contrast; basis: contrast+root+theme] وَمِنَ ٱلنَّاسِ مَن يَتَّخِذُ مِن دُونِ ٱللَّهِ أَندَادًۭا يُحِبُّونَهُمْ كَحُبِّ ٱللَّهِ ۖ وَٱلَّذِينَ ءَامَنُوٓا۟ أَشَدُّ حُبًّۭا لِّلَّهِ ۗ وَلَوْ يَرَى ٱلَّذِينَ ظَلَمُوٓا۟ إِذْ يَرَوْنَ ٱلْعَذَابَ أَنَّ ٱلْقُوَّةَ لِلَّهِ جَمِيعًۭا وَأَنَّ ٱللَّهَ شَدِيدُ ٱلْعَذَابِ
  Unverified discovery rationale: luna: The section says the source's dictionary form شَدّ names the horse's run while the human is “shadīd” in love of wealth; “أَشَدُّ حُبًّا لِلَّهِ” redirects that intensity of love toward God. | terra: Believers are أَشَدُّ حُبًّا لِّلَّهِ, reversing the human who is shadid in love of property by directing the same intensity toward God.
- (2:177) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section shows love of wealth as the human counterpart to a horse's service; this verse's righteous person gives “الْمَالَ عَلَىٰ حُبِّهِ,” turning attachment into care for others. | terra: وَآتَى الْمَالَ عَلَىٰ حُبِّهِ makes loved wealth something the righteous give, rather than the terminus of the human's intense attachment.
- (3:14) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶7] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section says the horse is both a running animal and a beloved possession; this list places “الْخَيْلِ الْمُسَوَّمَةِ” among what people desire and love, making that double role explicit. | terra: الْخَيْلِ الْمُسَوَّمَةِ places horses inside the decorated human love of desires and stored wealth, directly supporting the section's two faces of the horse as runner and loved property.
- (3:29) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: root+scene+theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section's human chest is where concealed contents are sifted; this verse says what people hide or disclose within themselves is known to God, a direct parallel to that inward disclosure. | terra: Whether people hide what is in their breasts or disclose it, God knows it; this directly parallels the section's chest as a temporary container whose contents will be brought out.
- (3:92) [luna: strong; terra: contrast; basis: contrast+theme] لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: luna: Against the section's human clinging to wealth, this verse makes giving from what one loves a condition of reaching righteousness: “مِمَّا تُحِبُّونَ.” | terra: لَن تَنَالُوا الْبِرَّ حَتَّىٰ تُنفِقُوا مِمَّا تُحِبُّونَ turns attachment to valued property into its relinquishment for righteousness.
- (3:154) [luna: medium; terra: strong; basis: root+scene+theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section's image turns from the horse's winning chest to what is sifted from human chests; this verse says God tests “مَا فِي صُدُورِكُمْ” and purifies what is in hearts. | terra: In a battle setting, God tests what is in the breasts and purifies what is in the hearts; this directly answers the section's human chest whose contents will be sorted after the charge.
- (4:135) [terra: strong (missing-ayat turn); basis: root+speaker+theme] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ بِٱلْقِسْطِ شُهَدَآءَ لِلَّهِ وَلَوْ عَلَىٰٓ أَنفُسِكُمْ أَوِ ٱلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ ۚ إِن يَكُنْ غَنِيًّا أَوْ فَقِيرًۭا فَٱللَّهُ أَوْلَىٰ بِهِمَا ۖ فَلَا تَتَّبِعُوا۟ ٱلْهَوَىٰٓ أَن تَعْدِلُوا۟ ۚ وَإِن تَلْوُۥٓا۟ أَوْ تُعْرِضُوا۟ فَإِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
  Unverified discovery rationale: terra: كُونُوا قَوَّامِينَ بِالْقِسْطِ شُهَدَاءَ لِلَّهِ وَلَوْ عَلَىٰ أَنفُسِكُمْ commands precisely the self-opposing witness that the section reads in the human's testimony against himself.
- (5:7) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ وَمِيثَٰقَهُ ٱلَّذِى وَاثَقَكُم بِهِۦٓ إِذْ قُلْتُمْ سَمِعْنَا وَأَطَعْنَا ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: The remembered covenant and وَقُلْتُمْ سَمِعْنَا وَأَطَعْنَا are followed by God's knowledge of breasts, joining pledged service to the inward reality that will test it.
- (6:130) [terra: strong; basis: root+theme] يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَقُصُّونَ عَلَيْكُمْ ءَايَٰتِى وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ شَهِدْنَا عَلَىٰٓ أَنفُسِنَا ۖ وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
  Unverified discovery rationale: terra: وَشَهِدُوا عَلَىٰ أَنفُسِهِمْ makes the human beings' own testimony establish their unbelief, matching the section's reading of testimony against one's own ingratitude.
- (7:37) [terra: strong; basis: root+theme] فَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ كَذَّبَ بِـَٔايَٰتِهِۦٓ ۚ أُو۟لَٰٓئِكَ يَنَالُهُمْ نَصِيبُهُم مِّنَ ٱلْكِتَٰبِ ۖ حَتَّىٰٓ إِذَا جَآءَتْهُمْ رُسُلُنَا يَتَوَفَّوْنَهُمْ قَالُوٓا۟ أَيْنَ مَا كُنتُمْ تَدْعُونَ مِن دُونِ ٱللَّهِ ۖ قَالُوا۟ ضَلُّوا۟ عَنَّا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
  Unverified discovery rationale: terra: شَهِدُوا عَلَىٰ أَنفُسِهِمْ أَنَّهُمْ كَانُوا كَافِرِينَ gives the same self-incriminating witness that contrasts with the horse's run witnessing in its favor.
- (8:43) [terra: strong (missing-ayat turn); basis: root+scene+theme] إِذْ يُرِيكَهُمُ ٱللَّهُ فِى مَنَامِكَ قَلِيلًۭا ۖ وَلَوْ أَرَىٰكَهُمْ كَثِيرًۭا لَّفَشِلْتُمْ وَلَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَلَٰكِنَّ ٱللَّهَ سَلَّمَ ۗ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: Within a battle encounter, the enemy is shown as few and God is عَلِيمٌ بِذَاتِ الصُّدُورِ; the gathered-force setting and inward knowledge meet two distinct details of the section.
- (8:60) [luna: strong; terra: strong; basis: scene+theme] وَأَعِدُّوا۟ لَهُم مَّا ٱسْتَطَعْتُم مِّن قُوَّةٍۢ وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ وَعَدُوَّكُمْ وَءَاخَرِينَ مِن دُونِهِمْ لَا تَعْلَمُونَهُمُ ٱللَّهُ يَعْلَمُهُمْ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فِى سَبِيلِ ٱللَّهِ يُوَفَّ إِلَيْكُمْ وَأَنتُمْ لَا تُظْلَمُونَ
