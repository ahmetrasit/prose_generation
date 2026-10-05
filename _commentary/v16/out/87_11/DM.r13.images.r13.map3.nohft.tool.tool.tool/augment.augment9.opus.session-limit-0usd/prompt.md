Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:11; its ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/augment9/augment.md =====
You are completing a finished Turkish commentary written by another reader with
what the Quran itself says about it: the Quran explaining the Quran. Below are
the commentary, with its prose paragraphs numbered [¶n]; its ledger; and Quran
passages from an earlier cross-reference list, each with its Arabic, its tier,
and the paragraphs of the commentary that already cite it, if any. A tier is
that list's own judgement, not yours; the list is not authoritative and may be
incomplete.

Read the commentary first. Then judge every listed passage, one by one, against
every paragraph: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the paragraph's ayah leaves
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

Then go through the commentary paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; ayat that state the same thing in other
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
passage from your own knowledge that you weighed, marked "own":
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/87_11/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_11.reading.tr.md (prose paragraphs numbered) =====
## Öğüdü yanına koymak

[¶1] On birinci ayet iki kelimeden oluşur: {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ise ondan uzak duracaktır, source:87:11}. İki kelime de kendinden öncekine yaslanır. Fiilin sonundaki dişil zamir, yani "onu", dokuzuncu ayetin son kelimesine döner: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt fayda verirse, source:87:9}. Uzak durulan şey öğüttür. Ateş ancak bir sonraki ayette gelir. Onuncu ayet {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10} diye başlar. Fiilin başındaki gelecek eki "ve" bağlacının üstünden bu ayete de geçer: biri öğüdü alacak, öbürü ondan uzak duracak. Öğüt tektir ve aynı ağızdan herkese sunulur. Ayrılık sunuşta değil, karşılayışta başlar.

[¶2] İki fiilin kalıbı da bu ayrılığı anlatır. يَذَّكَّرُ aslında "yetezekkeru" biçimidir, iki ses birbirine kaynaşmıştır. Böylece يَتَجَنَّبُ ile aynı kalıba, tefa''ul kalıbına girer. On dördüncü ayetteki {ar:تَزَكَّىٰ, tr:tezekkâ, gloss:arındı, source:87:14} de bu kalıptandır. Bu kalıp, kişinin bir işi kendi üzerinde, emek vererek yapmasını anlatır. Böylece surede insanın öğüde verdiği üç karşılık aynı kalıptan çıkar: öğüdü kendi içine almak, onu kendi yanına koymak, kendini arıtmak. Öğüt değişmez. Değişen, insanın onunla kendine yaptığı şeydir.

[¶3] Özneler de farklı kurulmuştur. Onuncu ayetin öznesi {ar:مَن يَخْشَىٰ, tr:men yahşâ, gloss:kim içi titrerse, source:87:10}. Bu açık bir "kim"dir ve bir fiile bağlıdır: korkuya giren herkes bu kapıdan geçer. On birinci ayetin öznesi ise belirli bir sıfattır, üstelik en uç derecesindedir: ٱلْأَشْقَى, "en bedbaht". Birinde bir eylem anlatılır, ötekinde bir konum. Bu kelime surenin kafiyesinde de yerini alır. Sure {ar:رَبِّكَ ٱلْأَعْلَى, tr:rabbike'l-a'lâ, gloss:en yüce Rabbin, source:87:1} sözüyle açılmış, sekizinci ayette {ar:لِلْيُسْرَىٰ, tr:li'l-yusrâ, gloss:en kolaya, source:87:8} demiştir. On ikinci ayette de {ar:ٱلنَّارَ ٱلْكُبْرَىٰ, tr:en-nâre'l-kubrâ, gloss:en büyük ateş, source:87:12} diyecektir. "En bedbaht" surenin bu "en"lerinden biridir ve hemen ardından en büyük ateşe bağlanır. Uçta duran, uçta olanla karşılaşır.

[¶4] Fiilin kökü ج ن ب bedenin yanını, böğrü adlandırır. Bundan sonra anılacak aile görüntüleri, kelimenin bu ayetteki anlamının, "uzak durmak"ın yanında duyulur. Hiçbiri o anlamın yerine geçmez. Araplar kökün aslını bir organda görürdü: {ar:أصل الجنب الجارحة, tr:aslu'l-cenbi'l-câriha, gloss:cenbin aslı bedendeki organdır, yani böğür, source:"ج ن ب,B001"}. Kök oradan her şeyin yanına genişler: {ar:الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء, tr:el-cânibu ve'l-cevânibu ma'rûfe ve'l-cenbetâni nâhiyetâ kulli şey', gloss:yan ve yanlar bilinir; iki yan her şeyin iki kenarıdır, source:"ج ن ب,B001"}. Uzak durmayı anlatan fiiller de bu yandan türer ve hepsi bir anlamda sayılır: {ar:جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه, tr:cânebehû ve tecânebehû ve tecennebehû ve'ctenebehû kulluhû bi-ma'nâ ve cennebtuhu'ş-şey'e ey nahheytuhû anh, gloss:bunların hepsi aynı anlamdadır; onu o şeyden kenara çektim, source:"ج ن ب,B003"}. Arapçada kaçınmak böylece bir mekân hareketi olur: bir şeyi yüzünün önünden alıp yanına, kenara koymak, ona yüzünü değil böğrünü dönmek.

[¶5] Kur'an bu beden hareketini aynı kökten bir kelimeyle başka bir yerde de çizer. Allah insanın bir huyunu anlatır: {ar:وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ, tr:ve iẕâ en'amnâ ale'l-insâni a'rada ve neâ bi-cânibih, gloss:insana nimet verdiğimizde yüz çevirir ve yanını alıp uzaklaşır, source:17:83}. Ayetin devamında, ona kötülük dokununca umutsuzluğa düştüğü söylenir. Yüz çevirmek ile yanını uzaklaştırmak burada yan yana duran iki harekettir. Öğütten dönmenin başka bir resmi de vardır ve ondan farkı öğreticidir. Allah öğütten dönenler için {ar:فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ, tr:fe-mâ lehum ani't-teẕkirati mu'ridîn, gloss:onlara ne oluyor da öğütten yüz çeviriyorlar, source:74:49} diye sorar. Sonra onları {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:ke-ennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri, source:74:50} ve {ar:فَرَّتْ مِن قَسْوَرَةٍۭ, tr:ferret min kaswera, gloss:aslandan kaçmışlar, source:74:51} diye anlatır. Orada bir panik, bir kaçış vardır. يَتَجَنَّبُ ise bir kaçış değildir. En bedbaht kişi öğütten ürkmez, ona saldırmaz da. Onun yanından geçer, onu böğrünün hizasında, kenarda tutarak yürür. Bu sakin, ölçülü ve sürekli bir kenara koyuştur.

## Putlardan sakınmayı anlatan fiil öğüde yöneltilince

[¶6] Bu kök Kur'an'da "uzak durmak" anlamıyla geçtiğinde, uzak durulan şey hemen her zaman aynı türdendir. Allah her topluluğa bir elçi gönderdiğini anlatır ve elçinin sözü şudur: {ar:أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ, tr:eni'budullâhe vectenibu't-tâğût, gloss:Allah'a kulluk edin ve azgın sahte ilahlardan uzak durun, source:16:36}. Hac ibadetlerinin anlatıldığı yerde {ar:فَٱجْتَنِبُوا۟ ٱلرِّجْسَ مِنَ ٱلْأَوْثَٰنِ وَٱجْتَنِبُوا۟ قَوْلَ ٱلزُّورِ, tr:fectenibu'r-ricse mine'l-evŝâni vectenibû kavle'z-zûr, gloss:putların pisliğinden uzak durun, yalan sözden uzak durun, source:22:30} denir. İyi kullar {ar:ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ, tr:elleẕîne yectenibûne kebâira'l-ismi ve'l-fevâhiş, gloss:günahın büyüklerinden ve çirkin işlerden uzak duranlar, source:53:32} diye tanıtılır. Put, pislik, yalan söz, büyük günah: Kur'an'da bu fiilin nesnesi, insanın kendini koruması gereken şeylerdir. Dilin kendisi de bunu taşır: {ar:جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها, tr:cennebtuhû an keẕâ fectenebe ey tecennebehû ve cennebtuhû ey defa'tu anhu mekrûhen, gloss:onu şundan uzak tuttum, o da uzak durdu; onu uzak tuttum, yani ondan hoş olmayan bir şeyi savdım, source:"ج ن ب,B003"}. Birini bir şeyden uzak tutmak, ondan bir kötülüğü savmaktır.

[¶7] On birinci ayet bu fiili alır ve nesnesinin yerine öğüdü koyar. En bedbaht kişi, müminin puta yaptığını öğüde yapar. Öğüdü kendinden savılacak bir kötülük gibi kenara iter. Dokuzuncu ayet öğüdü "fayda" kelimesiyle anmıştı ve fayda zararın karşıtıdır. Bedbahtlığın en ucu, faydayı zararın yerine koyabilmektir. Bu tersine çevirmenin doğrusunu Kur'an tek bir pasajda gösterir. Allah kendisine yönelen kulları müjdelerken onları önce {ar:وَٱلَّذِينَ ٱجْتَنَبُوا۟ ٱلطَّٰغُوتَ أَن يَعْبُدُوهَا, tr:velleẕîne'ctenebu't-tâğûte en ya'budûhâ, gloss:sahte ilaha kulluk etmekten uzak duranlar, source:39:17} diye anar. Hemen ardından da {ar:ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ, tr:elleẕîne yestemi'ûne'l-kavle fe-yettebi'ûne ahsenah, gloss:sözü dinleyip en güzeline uyanlar, source:39:18} der. Bu kullar uzak durulacak olandan uzak durmuş, dinlenecek olana kulak vermiştir. En bedbaht kişide bu iki hareket yer değiştirmiştir.

[¶8] Kökün din hayatında bir durum adı da vardır. Eşiyle birleşen kişiye cünüp denir ve bu ad uzaklıktan gelir: {ar:الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد, tr:el-cunubu'lleẕî yucâmiu ehlehû muştakkun min hâẕâ li-ennehû yeb'udu ani's-salâti ve'l-mescid, gloss:eşiyle birleşene cünüp denir, bu adı uzaklıktan alır, çünkü namazdan ve mescitten uzak kalır, source:"ج ن ب,B004"}. Kur'an bu durumu müminlere şöyle bildirir: {ar:لَا تَقْرَبُوا۟ ٱلصَّلَوٰةَ وَأَنتُمْ سُكَٰرَىٰ حَتَّىٰ تَعْلَمُوا۟ مَا تَقُولُونَ وَلَا جُنُبًا إِلَّا عَابِرِى سَبِيلٍ حَتَّىٰ تَغْتَسِلُوا۟, tr:lâ takrabu's-salâte ve entum sukârâ hattâ ta'lemû mâ tekûlûne ve lâ cunuben illâ âbirî sebîlin hattâ tağtesilû, gloss:sarhoşken, ne dediğinizi bilinceye kadar namaza yaklaşmayın; cünüpken de, yoldan geçenler dışında, yıkanıncaya kadar yaklaşmayın, source:4:43}. Bu uzaklık geçicidir ve sınırı bellidir: su ile biter, kişi yıkanır ve namaza döner. Surenin on dördüncü ayeti arınanı kurtulmuş sayar. On beşinci ayet de o kişiyi {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kılan, source:87:15} diye tanıtır. Namazdan uzak kalmanın adı ile öğütten uzak durmanın fiili dilde aynı kökten gelir. Bu bir dil yankısıdır, ayetin söylediği bir şey değildir. Ama ayrımı keskinleştirir: cünübün uzaklığını yıkanmak kapatır, en bedbahtın uzaklığı ise kapanmaz, çünkü o arınmanın kendisini kenara koymuştur.

## Yan: yoldaş da orada durur, yabancı da

[¶9] "Yan" yalnızca bir şeyi koyup uzaklaştırdığın yer değildir. Aynı kök, yanda duranın yakınlığını da adlandırır. Kolay yaklaşılan adama {ar:رجل لين الجانب والجنب أي سهل القرب, tr:raculun leyyinu'l-cânibi ve'l-cenb ey sehlu'l-kurb, gloss:yanı yumuşak adam, yani yaklaşması kolay kişi, source:"ج ن ب,B002"} derlerdi. Yolculukta yanında yürüyen arkadaş için {ar:الصاحب بالجنب صاحبك في السفر, tr:es-sâhibu bi'l-cenbi sâhibuke fi's-sefer, gloss:yandaki arkadaş, yolculuktaki arkadaşındır, source:"ج ن ب,B002"} denirdi. Ama aynı kökle akrabalığın karşıtı da söylenir: {ar:أجنب تباعد والجنابة ضد القرابة, tr:ecnebe tebâade ve'l-cenâbetu diddu'l-karâbe, gloss:ecnebe uzaklaştı demektir; cenâbe akrabalığın karşıtıdır, source:"ج ن ب,B003"}.

[¶10] Kur'an bu iki anlamı tek bir ayette yan yana koyar. Allah kendisine hiçbir şeyi ortak koşmadan kulluk etmeyi buyurur, sonra iyilik edilecekleri sayar: ana baba, yakınlar, yetimler, yoksullar, akraba komşu, {ar:وَٱلْجَارِ ٱلْجُنُبِ, tr:ve'l-câri'l-cunub, gloss:yabancı komşu, source:4:36}, {ar:وَٱلصَّاحِبِ بِٱلْجَنۢبِ, tr:ve's-sâhibi bi'l-cenb, gloss:yanındaki arkadaş, source:4:36} ve yolda kalmış olan. Aynı kökten bir kelime komşunun yabancılığını, öbürü arkadaşın yakınlığını söyler. Yan, hem yoldaşın hem yabancının durduğu yerdir.

[¶11] On birinci ayetteki öğüt de bu yerdedir. En bedbaht kişi öğütten habersiz değildir. Öğüt ondan uzakta söylenmemiştir. Onu yanına almıştır, ama yolculuk arkadaşı gibi değil, yabancı komşu gibi tutmuştur: bitişikte, eli uzansa erişeceği yerde, ama aralarında hiçbir bağ yokken. Ayetin acısı da buradadır: uzak durduğu şey hep yanındadır.

[¶12] Yan, bir şeylerin geldiği yön de olabilir. Rüzgârlardan biri adını bu kökten almıştır: {ar:الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح, tr:el-cenûbu rîhun tecîu an yemîni'l-kıbleti ve kad cenebeti'r-rîh, gloss:cenûb kıblenin sağından gelen rüzgârdır; rüzgârın güneyden esmesi de bu kökle söylenir, source:"ج ن ب,B006"}. Sıcak bir rüzgârdır ve doğudan esen sabâ ile batıdan esen debûr arasındaki yönden gelir: {ar:الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور, tr:el-cenûbu mine'r-riyâhi hârratun ve mehebbuhâ mâ beyne mehebbeyi's-sabâ ve'd-debûr, gloss:cenûb rüzgârların sıcak olanıdır; sabâ ile debûrun estiği yerlerin arasından eser, source:"ج ن ب,B006"}. Önüne bulut katıp sürer {source:"ج ن ب,B006"}. Adı da gelişinin yönüyle açıklanmıştır: {ar:الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة, tr:el-cenûbu yesıhhu en yu'tebera fîhâ ma'na'l-mecîi min cânibi'l-Ka'be, gloss:cenûbda Kâbe'nin yanından gelme anlamı görülebilir, source:"ج ن ب,B006"}. Bu rüzgârın sürdüğü bulut, dördüncü ayette otlağı çıkaran yağmurun sahnesine aittir. Bu ayetin kelimesi açısından önemli olan şudur: Arapçanın "yan"ı rahmetin estiği bir yön de olabilir, yoldaşın yürüdüğü yer de. En bedbaht kişi ise onu yalnızca bir şeyi koyup bıraktığı kenar olarak kullanır. Surenin daha geniş resminde bu kelime, dokuzuncu ayetteki "fayda" kökünün adını verdiği yamaların dikildiği su kırbasının iki yanını da adlandırır {source:"ج ن ب,B001"}.

[¶13] Türkçe bu kökün birçok parçasını yaşatır, ama onları artık tek bir "yan"dan doğmuş olarak duymaz. Güney için "cenup", yabancı için "ecnebi", dinî durum için "cenabet", eskiden sakınmak için "içtinap", Allah anılırken de "Cenab-ı Hak" denir. Sonuncusu bu ayeti anlamak için özellikle değerlidir. Cenâb bir topluluğun çevresi, yanı başıdır: {ar:جناب القوم ما حولهم, tr:cenâbu'l-kavmi mâ havlehum, gloss:bir topluluğun cenâbı çevresidir, source:"ج ن ب,B001"}. Aynı kökten cenb kelimesi yakınlık için de kullanılır: {ar:الجنب القرب وفي قرب الله وجواره, tr:el-cenbu'l-kurb ve fî kurbillâhi ve civârih, gloss:cenb yakınlıktır; Allah'ın yakınında ve komşuluğunda demektir, source:"ج ن ب,B002"}. Kur'an bu kelimeyi pişman bir ağızda kullanır. Allah kendi aleyhine aşırı giden kullarına seslenir {source:39:53}. Azap ansızın gelmeden önce kendilerine indirilenin en güzeline uymalarını ister {source:39:55}. Yoksa bir can şöyle diyecektir: {ar:يَٰحَسْرَتَىٰ عَلَىٰ مَا فَرَّطتُ فِى جَنۢبِ ٱللَّهِ, tr:yâ hasretâ alâ mâ farrattu fî cenbillâh, gloss:Allah'ın yanında, O'na karşı olan işte savsakladıklarıma yazıklar olsun, source:39:56}. Aynı can ardından {ar:لَوْ أَنَّ ٱللَّهَ هَدَىٰنِى, tr:lev ennallâhe hedânî, gloss:Allah bana yol gösterseydi, source:39:57} diyecek, azabı görünce de {ar:لَوْ أَنَّ لِى كَرَّةًۭ, tr:lev enne lî kerraten, gloss:keşke bir kez daha dönebilsem, source:39:58} diyecektir. Dünyada öğüdü yanına koyup geçen kişi, sonunda kaybettiğini yine bir "yan" diye anar. Bu bağı dil değil, okuma kurar. Ama kelime aynı köktendir ve kenara itilen şeyin kimin yanından geldiğini duyurur.

## İbrahim'in duası: yedekte götürülmek

[¶14] Kökün bir başka somut kullanımı yolculuktan gelir. Araplar bir hayvanı binmeden, yularından tutup yanlarında yürüttüklerinde bu fiili kullanırdı: {ar:جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير, tr:cenebtu'd-dâbbete iẕâ kudtuhâ ilâ cenbike ve keẕâlike cenebtu'l-esîr, gloss:hayvanı yanımda yedeğe aldım; esiri de öyle yürüttüm, source:"ج ن ب,B005"}. Yedekte götürülen hayvana ve binek hayvanının yanına bağlanan esire ayrı adlar verilmişti: {ar:الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة, tr:el-cenîbetu kullu dâbbetin tukâdu ve'l-cenîbu'l-esîru meşdûdun ilâ cenbi'd-dâbbe, gloss:cenîbe yedekte götürülen her hayvandır; cenîb, binek hayvanının yanına bağlanmış esirdir, source:"ج ن ب,B005"}. İşleyiş basittir. Binici önde, kendi hayvanının üstündedir. Yedek at bir iple onun yanına bağlıdır, sırtında kimse yoktur, yolunu kendi seçmez, binicinin gittiği yere onunla yan yana gider. Böylece "yanda tutmak" bir şeyi uzaklaştırmak olduğu kadar, bir şeyi kendi yolunda yanında götürmek de olabilir.

[¶15] Kur'an bu kökü bir duada kullanır. Dua, surenin son ayetinde sayfaları anılan İbrahim'indir: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi ibrâhîme ve mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}. İbrahim Rabbine şöyle seslenir: {ar:رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ, tr:rabbi'c'al hâẕe'l-belede âminen vecnubnî ve beniyye en na'bude'l-esnâm, gloss:Rabbim, bu beldeyi güvenli kıl; beni ve oğullarımı putlara tapmaktan uzak tut, source:14:35}. Bir sonraki ayette putların insanlardan pek çoğunu yoldan çıkardığını söyler {source:14:36}. Bu dua, yedek atın görüntüsüyle de anlaşılmıştır: {ar:من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك, tr:min cenebtu'l-ferese ke-ennemâ seelehû en yekûdehû an cânibi'ş-şirk, gloss:atı yedeğe aldım sözünden gelir; sanki Rabbinden kendisini şirkin yanından uzağa, yedekte götürmesini istemiştir, source:"ج ن ب,B005"}. İbrahim kendi ipini Rabbinin eline verir. Uzak durmayı kendi gücüne bırakmaz, Rabbinden ister. Uzak tutulmak istediği şey de puttur.

[¶16] On birinci ayet aynı kökü ters yönde çalıştırır. En bedbaht kişi kimsenin yedeğinde değildir. İp kendi elindedir ve kenara çektiği şey öğüttür. İbrahim puttan uzak tutulmayı ister, en bedbaht ise öğütten uzak durur.

[¶17] İbrahim'in hikâyesinde ayetin öbür kelimesi de geçer. İbrahim babasına, işitmeyen, görmeyen ve ona hiçbir yarar sağlamayan bir şeye neden taptığını sorar {source:19:42}. Babası onu taşlamakla tehdit eder ve uzun süre kendisinden uzak durmasını söyler {source:19:46}. İbrahim ona selam verir ve Rabbinden onun için bağışlanma dileyeceğini söyler {source:19:47}. Sonra şöyle der: {ar:وَأَعْتَزِلُكُمْ وَمَا تَدْعُونَ مِن دُونِ ٱللَّهِ وَأَدْعُوا۟ رَبِّى عَسَىٰٓ أَلَّآ أَكُونَ بِدُعَآءِ رَبِّى شَقِيًّۭا, tr:ve a'tezilukum ve mâ ted'ûne min dûnillâhi ve ed'û rabbî asâ ellâ ekûne bi-duâi rabbî şakıyyâ, gloss:sizden ve Allah'tan başka yalvardıklarınızdan ayrılıyorum, Rabbime yalvarıyorum; umarım Rabbime yalvarışımda bedbaht, eli boş biri olmam, source:19:48}. Hemen ardından, onlardan ayrılınca kendisine İshak ile Yakup'un bağışlandığı anlatılır {source:19:49}. İbrahim'in sözünde uzak durmak ile bedbaht olmamak aynı cümlededir. Uzak durduğu şey putlardır, ve bu ayrılık duasının boş dönmeyeceği umudunu taşır. On birinci ayetteki kişide aynı iki kelime ters bir bağla birleşir: öğütten uzak durur ve bedbahtların en ucu olur.

## Şekavet: kolaylığın karşısındaki zahmet

[¶18] ٱلْأَشْقَى kelimesinin kökü ش ق و Türkçeye en tanıdık hâliyle girmiştir, ama bambaşka bir yüzle. Türkçede "şaki" haydut, "eşkıya" yol kesen, "şekavet" haydutluk demektir. Türkçe bu kelimelerde yalnızca toplumun dışına düşmüş, silahlı adamı tutmuştur. Ayetteki ٱلْأَشْقَى bir yol kesici değildir. Arapçada bu kök, payına sıkıntı düşmüş, bahtı kara insanı anlatır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hilâfu's-seâde, gloss:şikve mutluluğun karşıtıdır, source:"ش ق و,B001"}. Bu bahtsızlık yalnızca öbür dünyaya ait değildir: {ar:الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية, tr:eş-şekâvetu hilâfu's-seâde ve'ş-şekâvetu'l-uhreviyyetu ve'd-dunyeviyye, gloss:şekâvet mutluluğun karşıtıdır; ahirette de olur, dünyada da, source:"ش ق و,B001"}. Kur'an bu karşıtlığı hesap gününün ayrımında kullanır. O gün hiçbir can Allah'ın izni olmadan konuşamaz, ve {ar:فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ, tr:fe-minhum şakıyyun ve saîd, gloss:onlardan kimi bedbahttır, kimi mutlu, source:11:105}. {ar:فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ, tr:fe-emme'lleẕîne şakû fe-fi'n-nâr, gloss:bedbaht olanlar ise ateştedir, source:11:106}.

[¶19] Kökün daha somut yüzü zahmettir: {ar:أصل يدل على المعاناة وخلاف السهولة, tr:aslun yedullu ale'l-muânâti ve hilâfi's-suhûle, gloss:katlanıp uğraşmayı ve kolaylığın karşıtını gösteren bir kök, source:"ش ق و,B002"}. Biriyle uzun uzun uğraşmak, ona dayanmak da bu kökle söylenir: {ar:الشقاء: الشدة والعسر، وشاقيته أي صابرته, tr:eş-şekâu'ş-şiddetu ve'l-usr ve şâkaytuhû ey sâbertuh, gloss:şekâ sıkıntı ve zorluktur; şâkaytuhû, ona sabırla dayandım demektir, source:"ش ق و,B002"}. Bu anlam sekizinci ayetin tam karşısına düşer. Peygamber'e {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolaya kolaylaştıracağız, source:87:8} denmişti. En kolayın karşısında, en çok zahmet çeken durur. İki kelime de en üst derecededir, biri kolaylığın, öbürü zahmetin. Ama dilde bir ayrım da yapılmıştır: {ar:يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة, tr:yûda'u'ş-şekâu mevdia't-teab ve kullu şekâvetin teabun ve leyse kullu teabin şekâve, gloss:şekâ yorgunluk yerine kullanılır; her şekâvet yorgunluktur, ama her yorgunluk şekâvet değildir, source:"ش ق و,B002"}.

[¶20] Kur'an bu ayrımı öğüt üzerinden yapar. Bir surenin başında Allah Peygamber'e şöyle der: {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana zahmete düşesin diye indirmedik, source:20:2}, {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkiraten li-men yahşâ, gloss:ancak içi titreyen için bir öğüt olarak indirdik, source:20:3}. Dokuzuncu, onuncu ve on birinci ayetlerin üç kelimesi, yani öğüt, içi titreyen ve zahmet, bu iki ayette yan yana durur. Orada zahmet öğüdü taşıyandan uzak tutulur: öğüdü taşımak yorucu olabilir ama bedbahtlık değildir. Burada ise zahmet öğüdü kenara koyanın üstüne çöker. Bedbahtlık öğüdün içinde değil, ondan uzak durmaktadır.

[¶21] Aynı surede, Âdem'in hikâyesinde, Kur'an bu zahmetin ne olduğunu da somut olarak söyler. Allah Âdem'e şeytanın onun ve eşinin düşmanı olduğunu bildirir ve uyarır: {ar:فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ, tr:fe-lâ yuhricennekumâ mine'l-cenneti fe-teşkâ, gloss:sakın sizi bahçeden çıkarmasın, yoksa zahmete düşersin, source:20:117}. Ardından bahçede neyin olmadığını sayar: {ar:إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ, tr:inne leke ellâ tecûa fîhâ ve lâ ta'râ, gloss:orada ne acıkırsın ne de çıplak kalırsın, source:20:118}, {ar:وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ, tr:ve enneke lâ tazmeu fîhâ ve lâ tadhâ, gloss:orada ne susarsın ne de güneşin altında yanarsın, source:20:119}. Açlık, çıplaklık, susuzluk ve güneşin yakıcılığı: Kur'an'ın kendi tanımında zahmet budur, bedenin dışarıdaki çetin hayatı. Âdem ile eşi bahçeden indirilirken söylenen söz ise çıkış yolunu gösterir: {ar:فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ, tr:fe-meni'ttebea hudâye fe-lâ yadillu ve lâ yeşkâ, gloss:kim benim gösterdiğim yola uyarsa ne yolunu şaşırır ne de bedbaht olur, source:20:123}. Ardından: {ar:وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:ve men a'rada an ẕikrî fe-inne lehû maîşeten danka, gloss:kim benim öğüdümden yüz çevirirse onun geçimi dar olur, source:20:124}. Zahmetten kurtuluş, gösterilen yola uymaktır. Öğütten yüz çevirmek ise darlıktır. On birinci ayet bu iki ucu tek bir kelimede birleştirir: öğütten uzak duran, zahmetin en ucundadır.

[¶22] Kök bir yer adı da verir, ve bu ad zahmetin neden ibaret olduğunu düşündürür: {ar:الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان, tr:eş-şâkî min huyûdi'l-cibâli't-tâliu't-tavîl ve mea tûlihî eyseru suûden ve akdaru mak'aden li'l-insân, gloss:şâkî, dağdan uzayıp yükselen sırttır; uzunluğuna rağmen tırmanması daha kolay, insanın oturmasına daha elverişlidir, source:"ش ق و,B004"}. Bu tarifte zahmet kökünden gelen bir sırt, sekizinci ayetteki "kolay" kökünün üstünlük biçimiyle, أيسر kelimesiyle aynı cümlededir. Sırtı bu köke bağlayan şey dikliği değil, uzunluğudur. Kökün temelinde de bir şeyle uzun uzun uğraşmak, ona dayanmak vardır. Bu da şekâvetin özünde uzunluk yattığını düşündürür. Dağın sırtında uzunluk kolaylıkla birlikte gelir. En bedbahtın payında ise uzunluk kalır, kolaylık gider. On üçüncü ayet onun hâlini tam böyle bir uzunlukla anlatır: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. Bu ne ölümle biten ne de hayatla soluk alan bir katlanıştır. Bu bağ okumanın bağıdır. Kelimenin kendisi yalnızca sırtı ve zahmeti aynı kökte toplar.

[¶23] Kökün bir kullanımı da bir boğuşmanın sonucunu anlatır: {ar:شاقاني فلان فشقوته أشقوه، أي غلبته فيه, tr:şâkânî fulânun fe-şekavtuhû eşkûhu ey ğalebtuhû fîh, gloss:falanca benimle uğraştı, ben de o işte onu yendim, source:"ش ق و,B003"}. Kur'an'ın ateştekilerin ağzından aktardığı bir cümle bu kullanımın yanında ayrı bir ses kazanır. Allah onlara {ar:أَلَمْ تَكُنْ ءَايَٰتِى تُتْلَىٰ عَلَيْكُمْ فَكُنتُم بِهَا تُكَذِّبُونَ, tr:e-lem tekun âyâtî tutlâ aleykum fe-kuntum bihâ tukeẕẕibûn, gloss:ayetlerim size okunmuyor muydu, siz de onları yalanlıyordunuz, source:23:105} diye sorar. Cevapları şudur: {ar:رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا وَكُنَّا قَوْمًۭا ضَآلِّينَ, tr:rabbenâ ğalebet aleynâ şikvetunâ ve kunnâ kavmen dâllîn, gloss:Rabbimiz, bedbahtlığımız bize üstün geldi, biz yolunu şaşırmış bir topluluktuk, source:23:106}. Okunan ayetler, yani sunulan öğüt, yanlarından geçip gitmiştir. Şimdi bedbahtlıklarını, kendilerini yenmiş bir hasım gibi anlatırlar. Söyledikleri son kelime, her namazda okunan Fâtiha'nın da son kelimesidir: {ar:وَلَا ٱلضَّآلِّينَ, tr:ve le'd-dâllîn, gloss:yolunu şaşıranlarınkine de değil, source:1:7}.

## Uzak duran ve uzak tutulan: iki "en"

[¶24] Bu ayetin iki kelimesi Kur'an'da başka bir surede, birkaç ayet arayla, yeniden buluşur. Geceye yeminle açılan o sure de insanları iki yola ayırır. Birinin yolu en kolaya, ötekinin yolu en zora kolaylaştırılır {source:92:7} {source:92:10}. Sonra şöyle der: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enẕertukum nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}, {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:elleẕî keẕẕebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16}. Ardından: {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en çok sakınan ise ondan uzak tutulacaktır, source:92:17}, {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:elleẕî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18}.

[¶25] İki surenin parçaları aynıdır: "en bedbaht", ateşe girme fiili, ج ن ب kökünden bir fiil, fiilin sonunda dişil "onu" zamiri ve başında gelecek eki. Ama roller yer değiştirmiştir. Bu surede en bedbaht, uzak durmanın öznesidir. Kendini kendi emeğiyle uzak tutar ve uzak durduğu şey öğüttür. Öbür surede uzak tutulan, en çok sakınandır. Orada fiil edilgendir: onu ateşten bir başkası uzak tutar. Dil bu iki hareketi zaten bir zincir olarak bilir: {ar:جنبته عن كذا فاجتنب, tr:cennebtuhû an keẕâ fectenebe, gloss:onu şundan uzak tuttum, o da uzak kaldı, source:"ج ن ب,B003"}. Biri tutar, öbürü uzak kalır. En çok sakınan bu zincirin ikinci halkasındadır. Ateşten uzak tutulması kendi işi değil, Rabbinin işidir. Onun işi sakınmak ve malını verip arınmaktır. En bedbaht ise zincirin iki halkasını da kendi eline almıştır: kendini kendisi uzak tutar, ama yanlış şeyden. Öğütten kendini uzak tutan, ateşten uzak tutulmaz. O, on ikinci ayetin {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yaslâ'n-nâre'l-kubrâ, gloss:en büyük ateşe girecek olan, source:87:12} dediği kişidir. Ateşten uzak tutulan ise, on dördüncü ayetin kelimesiyle, arınandır. İki surede öğüt de ateş de aynı dişil zamirle, "onu" diye anılır. Birini kenara koyan, öbürünün kenarında tutulmaz.

===== _commentary/v16/out/87_11/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: يذّكّر is assimilated يتذكّر (Form V), same pattern as يتجنب and تزكّى
- memory: Form V (tafa''ul) conveys a self-directed, effortful act
- memory: Quranic ijtināb objects are almost always harmful things (idols, ṭāghūt, sins, false speech)
- memory: Turkish şaki/eşkıya/şekavet derive from Arabic شقي / {أشقياء} plural
- memory: Turkish cenup, ecnebi, cenabet, içtinap, Cenab-ı Hak derive from ج ن ب
- not written: elative أشقى may mean intensity without comparison - left unargued; the surah's string of superlatives carried the point
- not written: ج ن ب B007 side pain/pleurisy - no supported tie to avoidance
- not written: ج ن ب B008 milk scarcity - no tie to the ayah's themes
- not written: ج ن ب B009 abundant good/evil (fixed expression) - no thematic work
- not written: ج ن ب B010 summer plants - pasture link would be forced
- not written: ج ن ب B011 shield carried at the side - reminder-as-shield unsupported
- not written: ج ن ب B012 horse's legs set apart - no tie
- not written: valley's two sides (B001) - added nothing beyond "side"
- not written: 74:17-26 the man who measured and was sent to burn - too far from this ayah's words
- not written: 6:26 "they keep away from it" - repeats the 17:83 point
- not written: echo root ش ق ي - not identity; senses duplicate ش ق و

===== passages not cited (231) =====
## strong (this ayah's own list) (36)

- (14:35) [listed for 87:11] [cited in ¶15] وَإِذْ قَالَ إِبْرَٰهِيمُ رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ
- (16:36) [listed for 87:11] [cited in ¶6] وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ ۖ فَمِنْهُم مَّنْ هَدَى ٱللَّهُ وَمِنْهُم مَّنْ حَقَّتْ عَلَيْهِ ٱلضَّلَٰلَةُ ۚ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (17:46) [listed for 87:11] وَجَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۚ وَإِذَا ذَكَرْتَ رَبَّكَ فِى ٱلْقُرْءَانِ وَحْدَهُۥ وَلَّوْا۟ عَلَىٰٓ أَدْبَٰرِهِمْ نُفُورًۭا
- (18:57) [listed for 87:11] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ فَأَعْرَضَ عَنْهَا وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ ۚ إِنَّا جَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۖ وَإِن تَدْعُهُمْ إِلَى ٱلْهُدَىٰ فَلَن يَهْتَدُوٓا۟ إِذًا أَبَدًۭا
- (20:2) [listed for 87:11] [cited in ¶20] مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ
- (20:44) [listed for 87:11] فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ
- (20:48) [listed for 87:11] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:74) [listed for 87:11] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:117) [listed for 87:11] [cited in ¶21] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (20:123) [listed for 87:11] [cited in ¶21] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (20:124) [listed for 87:11] [cited in ¶21] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
- (21:42) [listed for 87:11] قُلْ مَن يَكْلَؤُكُم بِٱلَّيْلِ وَٱلنَّهَارِ مِنَ ٱلرَّحْمَٰنِ ۗ بَلْ هُمْ عَن ذِكْرِ رَبِّهِم مُّعْرِضُونَ
- (23:66) [listed for 87:11] قَدْ كَانَتْ ءَايَٰتِى تُتْلَىٰ عَلَيْكُمْ فَكُنتُمْ عَلَىٰٓ أَعْقَٰبِكُمْ تَنكِصُونَ
- (25:29) [listed for 87:11] لَّقَدْ أَضَلَّنِى عَنِ ٱلذِّكْرِ بَعْدَ إِذْ جَآءَنِى ۗ وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًۭا
- (26:5) [listed for 87:11] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
- (32:22) [listed for 87:11] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ ثُمَّ أَعْرَضَ عَنْهَآ ۚ إِنَّا مِنَ ٱلْمُجْرِمِينَ مُنتَقِمُونَ
- (39:17) [listed for 87:11] [cited in ¶7] وَٱلَّذِينَ ٱجْتَنَبُوا۟ ٱلطَّٰغُوتَ أَن يَعْبُدُوهَا وَأَنَابُوٓا۟ إِلَى ٱللَّهِ لَهُمُ ٱلْبُشْرَىٰ ۚ فَبَشِّرْ عِبَادِ
- (41:41) [listed for 87:11] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (41:51) [listed for 87:11] وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ وَإِذَا مَسَّهُ ٱلشَّرُّ فَذُو دُعَآءٍ عَرِيضٍۢ
- (43:36) [listed for 87:11] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (45:8) [listed for 87:11] يَسْمَعُ ءَايَٰتِ ٱللَّهِ تُتْلَىٰ عَلَيْهِ ثُمَّ يُصِرُّ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍۢ
- (53:29) [listed for 87:11] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (72:17) [listed for 87:11] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
- (74:31) [listed for 87:11] وَمَا جَعَلْنَآ أَصْحَٰبَ ٱلنَّارِ إِلَّا مَلَٰٓئِكَةًۭ ۙ وَمَا جَعَلْنَا عِدَّتَهُمْ إِلَّا فِتْنَةًۭ لِّلَّذِينَ كَفَرُوا۟ لِيَسْتَيْقِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَيَزْدَادَ ٱلَّذِينَ ءَامَنُوٓا۟ إِيمَٰنًۭا ۙ وَلَا يَرْتَابَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْمُؤْمِنُونَ ۙ وَلِيَقُولَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ وَٱلْكَٰفِرُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَمَا يَعْلَمُ جُنُودَ رَبِّكَ إِلَّا هُوَ ۚ وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ
- (74:49) [listed for 87:11] [cited in ¶5] فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ
- (79:45) [listed for 87:11] إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
- (80:11) [listed for 87:11] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
- (80:12) [listed for 87:11] فَمَن شَآءَ ذَكَرَهُۥ
- (88:21) [listed for 87:11] فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- (88:23) [listed for 87:11] إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- (91:9) [listed for 87:11] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- (92:14) [listed for 87:11] [cited in ¶24] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:15) [listed for 87:11] [cited in ¶24] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (92:16) [listed for 87:11] [cited in ¶24] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:17) [listed for 87:11] [cited in ¶24] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- (92:18) [listed for 87:11] [cited in ¶24] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ

## medium (this ayah's own list) (55)

- (3:191) [listed for 87:11] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
- (5:90) [listed for 87:11] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
- (6:4) [listed for 87:11] وَمَا تَأْتِيهِم مِّنْ ءَايَةٍۢ مِّنْ ءَايَٰتِ رَبِّهِمْ إِلَّا كَانُوا۟ عَنْهَا مُعْرِضِينَ
- (6:157) [listed for 87:11] أَوْ تَقُولُوا۟ لَوْ أَنَّآ أُنزِلَ عَلَيْنَا ٱلْكِتَٰبُ لَكُنَّآ أَهْدَىٰ مِنْهُمْ ۚ فَقَدْ جَآءَكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ وَهُدًۭى وَرَحْمَةٌۭ ۚ فَمَنْ أَظْلَمُ مِمَّن كَذَّبَ بِـَٔايَٰتِ ٱللَّهِ وَصَدَفَ عَنْهَا ۗ سَنَجْزِى ٱلَّذِينَ يَصْدِفُونَ عَنْ ءَايَٰتِنَا سُوٓءَ ٱلْعَذَابِ بِمَا كَانُوا۟ يَصْدِفُونَ
- (7:2) [listed for 87:11] كِتَٰبٌ أُنزِلَ إِلَيْكَ فَلَا يَكُن فِى صَدْرِكَ حَرَجٌۭ مِّنْهُ لِتُنذِرَ بِهِۦ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
- (7:201) [listed for 87:11] إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ
- (10:12) [listed for 87:11] وَإِذَا مَسَّ ٱلْإِنسَٰنَ ٱلضُّرُّ دَعَانَا لِجَنۢبِهِۦٓ أَوْ قَاعِدًا أَوْ قَآئِمًۭا فَلَمَّا كَشَفْنَا عَنْهُ ضُرَّهُۥ مَرَّ كَأَن لَّمْ يَدْعُنَآ إِلَىٰ ضُرٍّۢ مَّسَّهُۥ ۚ كَذَٰلِكَ زُيِّنَ لِلْمُسْرِفِينَ مَا كَانُوا۟ يَعْمَلُونَ
- (11:105) [listed for 87:11] [cited in ¶18] يَوْمَ يَأْتِ لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِۦ ۚ فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ
- (11:106) [listed for 87:11] [cited in ¶18] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (14:3) [listed for 87:11] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (17:83) [listed for 87:11] [cited in ¶5] وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ ۖ وَإِذَا مَسَّهُ ٱلشَّرُّ كَانَ يَـُٔوسًۭا
- (18:28) [listed for 87:11] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (19:4) [listed for 87:11] قَالَ رَبِّ إِنِّى وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًۭا وَلَمْ أَكُنۢ بِدُعَآئِكَ رَبِّ شَقِيًّۭا
- (19:32) [listed for 87:11] وَبَرًّۢا بِوَٰلِدَتِى وَلَمْ يَجْعَلْنِى جَبَّارًۭا شَقِيًّۭا
- (19:48) [listed for 87:11] [cited in ¶17] وَأَعْتَزِلُكُمْ وَمَا تَدْعُونَ مِن دُونِ ٱللَّهِ وَأَدْعُوا۟ رَبِّى عَسَىٰٓ أَلَّآ أَكُونَ بِدُعَآءِ رَبِّى شَقِيًّۭا
- (19:52) [listed for 87:11] وَنَٰدَيْنَٰهُ مِن جَانِبِ ٱلطُّورِ ٱلْأَيْمَنِ وَقَرَّبْنَٰهُ نَجِيًّۭا
- (20:14) [listed for 87:11] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:16) [listed for 87:11] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (20:42) [listed for 87:11] ٱذْهَبْ أَنتَ وَأَخُوكَ بِـَٔايَٰتِى وَلَا تَنِيَا فِى ذِكْرِى
- (23:106) [listed for 87:11] [cited in ¶23] قَالُوا۟ رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا وَكُنَّا قَوْمًۭا ضَآلِّينَ
- (29:45) [listed for 87:11] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
- (32:16) [listed for 87:11] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (35:18) [listed for 87:11] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (36:11) [listed for 87:11] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
- (38:32) [listed for 87:11] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
- (39:22) [listed for 87:11] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (39:56) [listed for 87:11] [cited in ¶13] أَن تَقُولَ نَفْسٌۭ يَٰحَسْرَتَىٰ عَلَىٰ مَا فَرَّطتُ فِى جَنۢبِ ٱللَّهِ وَإِن كُنتُ لَمِنَ ٱلسَّٰخِرِينَ
- (42:37) [listed for 87:11] وَٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ وَإِذَا مَا غَضِبُوا۟ هُمْ يَغْفِرُونَ
- (46:3) [listed for 87:11] مَا خَلَقْنَا ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَآ إِلَّا بِٱلْحَقِّ وَأَجَلٍۢ مُّسَمًّۭى ۚ وَٱلَّذِينَ كَفَرُوا۟ عَمَّآ أُنذِرُوا۟ مُعْرِضُونَ
- (50:37) [listed for 87:11] إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِمَن كَانَ لَهُۥ قَلْبٌ أَوْ أَلْقَى ٱلسَّمْعَ وَهُوَ شَهِيدٌۭ
- (53:32) [listed for 87:11] [cited in ¶6] ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ إِلَّا ٱللَّمَمَ ۚ إِنَّ رَبَّكَ وَٰسِعُ ٱلْمَغْفِرَةِ ۚ هُوَ أَعْلَمُ بِكُمْ إِذْ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ ۖ فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ
- (54:17) [listed for 87:11] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:22) [listed for 87:11] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:32) [listed for 87:11] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:40) [listed for 87:11] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (57:16) [listed for 87:11] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (58:19) [listed for 87:11] ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ ۚ أَلَآ إِنَّ حِزْبَ ٱلشَّيْطَٰنِ هُمُ ٱلْخَٰسِرُونَ
- (62:9) [listed for 87:11] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (63:9) [listed for 87:11] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (65:10) [listed for 87:11] أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا ۖ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟ ۚ قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا
- (69:48) [listed for 87:11] وَإِنَّهُۥ لَتَذْكِرَةٌۭ لِّلْمُتَّقِينَ
- (73:19) [listed for 87:11] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (74:54) [listed for 87:11] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
- (74:55) [listed for 87:11] فَمَن شَآءَ ذَكَرَهُۥ
- (76:29) [listed for 87:11] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًۭا
- (79:18) [listed for 87:11] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
- (79:21) [listed for 87:11] فَكَذَّبَ وَعَصَىٰ
- (79:26) [listed for 87:11] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (80:3) [listed for 87:11] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
- (80:4) [listed for 87:11] أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ
- (81:27) [listed for 87:11] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (81:28) [listed for 87:11] لِمَن شَآءَ مِنكُمْ أَن يَسْتَقِيمَ
- (91:12) [listed for 87:11] إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- (92:10) [listed for 87:11] [cited in ¶24] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (96:13) [listed for 87:11] أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ

## named by the passage's own list as strong for this ayah (11)

- (8:21) [listed for 87:11] وَلَا تَكُونُوا۟ كَٱلَّذِينَ قَالُوا۟ سَمِعْنَا وَهُمْ لَا يَسْمَعُونَ
- (17:41) [listed for 87:11] وَلَقَدْ صَرَّفْنَا فِى هَٰذَا ٱلْقُرْءَانِ لِيَذَّكَّرُوا۟ وَمَا يَزِيدُهُمْ إِلَّا نُفُورًۭا
- (17:82) [listed for 87:11] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
- (27:81) [listed for 87:11] وَمَآ أَنتَ بِهَٰدِى ٱلْعُمْىِ عَن ضَلَٰلَتِهِمْ ۖ إِن تُسْمِعُ إِلَّا مَن يُؤْمِنُ بِـَٔايَٰتِنَا فَهُم مُّسْلِمُونَ
- (37:13) [listed for 87:11] وَإِذَا ذُكِّرُوا۟ لَا يَذْكُرُونَ
- (51:55) [listed for 87:11] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
- (71:6) [listed for 87:11] فَلَمْ يَزِدْهُمْ دُعَآءِىٓ إِلَّا فِرَارًۭا
- (74:26) [listed for 87:11] سَأُصْلِيهِ سَقَرَ
- (80:6) [listed for 87:11] فَأَنتَ لَهُۥ تَصَدَّىٰ
- (82:14) [listed for 87:11] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (83:16) [listed for 87:11] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ

## named by the passage's own list as medium for this ayah (18)

- (2:175) [listed for 87:11] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ وَٱلْعَذَابَ بِٱلْمَغْفِرَةِ ۚ فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ
- (20:100) [listed for 87:11] مَّنْ أَعْرَضَ عَنْهُ فَإِنَّهُۥ يَحْمِلُ يَوْمَ ٱلْقِيَٰمَةِ وِزْرًا
- (21:50) [listed for 87:11] وَهَٰذَا ذِكْرٌۭ مُّبَارَكٌ أَنزَلْنَٰهُ ۚ أَفَأَنتُمْ لَهُۥ مُنكِرُونَ
- (25:73) [listed for 87:11] وَٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانًۭا
- (36:64) [listed for 87:11] ٱصْلَوْهَا ٱلْيَوْمَ بِمَا كُنتُمْ تَكْفُرُونَ
- (37:30) [listed for 87:11] وَمَا كَانَ لَنَا عَلَيْكُم مِّن سُلْطَٰنٍۭ ۖ بَلْ كُنتُمْ قَوْمًۭا طَٰغِينَ
- (38:87) [listed for 87:11] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (48:13) [listed for 87:11] وَمَن لَّمْ يُؤْمِنۢ بِٱللَّهِ وَرَسُولِهِۦ فَإِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَعِيرًۭا
- (50:8) [listed for 87:11] تَبْصِرَةًۭ وَذِكْرَىٰ لِكُلِّ عَبْدٍۢ مُّنِيبٍۢ
- (50:45) [listed for 87:11] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
- (59:17) [listed for 87:11] فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- (68:52) [listed for 87:11] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (70:15) [listed for 87:11] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (74:50) [listed for 87:11] [cited in ¶5] كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ
- (79:36) [listed for 87:11] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- (80:1) [listed for 87:11] عَبَسَ وَتَوَلَّىٰٓ
- (84:12) [listed for 87:11] وَيَصْلَىٰ سَعِيرًا
- (92:7) [listed for 87:11] [cited in ¶24] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ

## weak (this ayah's own list) (32)

- (2:187) [listed for 87:11] أُحِلَّ لَكُمْ لَيْلَةَ ٱلصِّيَامِ ٱلرَّفَثُ إِلَىٰ نِسَآئِكُمْ ۚ هُنَّ لِبَاسٌۭ لَّكُمْ وَأَنتُمْ لِبَاسٌۭ لَّهُنَّ ۗ عَلِمَ ٱللَّهُ أَنَّكُمْ كُنتُمْ تَخْتَانُونَ أَنفُسَكُمْ فَتَابَ عَلَيْكُمْ وَعَفَا عَنكُمْ ۖ فَٱلْـَٰٔنَ بَٰشِرُوهُنَّ وَٱبْتَغُوا۟ مَا كَتَبَ ٱللَّهُ لَكُمْ ۚ وَكُلُوا۟ وَٱشْرَبُوا۟ حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ ۖ ثُمَّ أَتِمُّوا۟ ٱلصِّيَامَ إِلَى ٱلَّيْلِ ۚ وَلَا تُبَٰشِرُوهُنَّ وَأَنتُمْ عَٰكِفُونَ فِى ٱلْمَسَٰجِدِ ۗ تِلْكَ حُدُودُ ٱللَّهِ فَلَا تَقْرَبُوهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَّقُونَ
- (2:266) [listed for 87:11] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (4:31) [listed for 87:11] إِن تَجْتَنِبُوا۟ كَبَآئِرَ مَا تُنْهَوْنَ عَنْهُ نُكَفِّرْ عَنكُمْ سَيِّـَٔاتِكُمْ وَنُدْخِلْكُم مُّدْخَلًۭا كَرِيمًۭا
- (4:43) [listed for 87:11] [cited in ¶8] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْرَبُوا۟ ٱلصَّلَوٰةَ وَأَنتُمْ سُكَٰرَىٰ حَتَّىٰ تَعْلَمُوا۟ مَا تَقُولُونَ وَلَا جُنُبًا إِلَّا عَابِرِى سَبِيلٍ حَتَّىٰ تَغْتَسِلُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُمْ ۗ إِنَّ ٱللَّهَ كَانَ عَفُوًّا غَفُورًا
- (4:103) [listed for 87:11] فَإِذَا قَضَيْتُمُ ٱلصَّلَوٰةَ فَٱذْكُرُوا۟ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِكُمْ ۚ فَإِذَا ٱطْمَأْنَنتُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ ۚ إِنَّ ٱلصَّلَوٰةَ كَانَتْ عَلَى ٱلْمُؤْمِنِينَ كِتَٰبًۭا مَّوْقُوتًۭا
- (9:35) [listed for 87:11] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
- (12:104) [listed for 87:11] وَمَا تَسْـَٔلُهُمْ عَلَيْهِ مِنْ أَجْرٍ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (15:9) [listed for 87:11] إِنَّا نَحْنُ نَزَّلْنَا ٱلذِّكْرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ
- (16:35) [listed for 87:11] وَقَالَ ٱلَّذِينَ أَشْرَكُوا۟ لَوْ شَآءَ ٱللَّهُ مَا عَبَدْنَا مِن دُونِهِۦ مِن شَىْءٍۢ نَّحْنُ وَلَآ ءَابَآؤُنَا وَلَا حَرَّمْنَا مِن دُونِهِۦ مِن شَىْءٍۢ ۚ كَذَٰلِكَ فَعَلَ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ فَهَلْ عَلَى ٱلرُّسُلِ إِلَّا ٱلْبَلَٰغُ ٱلْمُبِينُ
- (17:68) [listed for 87:11] أَفَأَمِنتُمْ أَن يَخْسِفَ بِكُمْ جَانِبَ ٱلْبَرِّ أَوْ يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا ثُمَّ لَا تَجِدُوا۟ لَكُمْ وَكِيلًا
- (22:30) [listed for 87:11] [cited in ¶6] ذَٰلِكَ وَمَن يُعَظِّمْ حُرُمَٰتِ ٱللَّهِ فَهُوَ خَيْرٌۭ لَّهُۥ عِندَ رَبِّهِۦ ۗ وَأُحِلَّتْ لَكُمُ ٱلْأَنْعَٰمُ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ ۖ فَٱجْتَنِبُوا۟ ٱلرِّجْسَ مِنَ ٱلْأَوْثَٰنِ وَٱجْتَنِبُوا۟ قَوْلَ ٱلزُّورِ
- (22:36) [listed for 87:11] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (26:90) [listed for 87:11] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ
- (26:91) [listed for 87:11] وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ
- (26:214) [listed for 87:11] وَأَنذِرْ عَشِيرَتَكَ ٱلْأَقْرَبِينَ
- (28:11) [listed for 87:11] وَقَالَتْ لِأُخْتِهِۦ قُصِّيهِ ۖ فَبَصُرَتْ بِهِۦ عَن جُنُبٍۢ وَهُمْ لَا يَشْعُرُونَ
- (28:44) [listed for 87:11] وَمَا كُنتَ بِجَانِبِ ٱلْغَرْبِىِّ إِذْ قَضَيْنَآ إِلَىٰ مُوسَى ٱلْأَمْرَ وَمَا كُنتَ مِنَ ٱلشَّٰهِدِينَ
- (37:8) [listed for 87:11] لَّا يَسَّمَّعُونَ إِلَى ٱلْمَلَإِ ٱلْأَعْلَىٰ وَيُقْذَفُونَ مِن كُلِّ جَانِبٍۢ
- (43:2) [listed for 87:11] وَٱلْكِتَٰبِ ٱلْمُبِينِ
- (47:6) [listed for 87:11] وَيُدْخِلُهُمُ ٱلْجَنَّةَ عَرَّفَهَا لَهُمْ
- (49:12) [listed for 87:11] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱجْتَنِبُوا۟ كَثِيرًۭا مِّنَ ٱلظَّنِّ إِنَّ بَعْضَ ٱلظَّنِّ إِثْمٌۭ ۖ وَلَا تَجَسَّسُوا۟ وَلَا يَغْتَب بَّعْضُكُم بَعْضًا ۚ أَيُحِبُّ أَحَدُكُمْ أَن يَأْكُلَ لَحْمَ أَخِيهِ مَيْتًۭا فَكَرِهْتُمُوهُ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ تَوَّابٌۭ رَّحِيمٌۭ
- (55:43) [listed for 87:11] هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى يُكَذِّبُ بِهَا ٱلْمُجْرِمُونَ
- (74:29) [listed for 87:11] لَوَّاحَةٌۭ لِّلْبَشَرِ
- (74:35) [listed for 87:11] إِنَّهَا لَإِحْدَى ٱلْكُبَرِ
- (77:32) [listed for 87:11] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
- (83:21) [listed for 87:11] يَشْهَدُهُ ٱلْمُقَرَّبُونَ
- (83:28) [listed for 87:11] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
- (88:24) [listed for 87:11] فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- (89:27) [listed for 87:11] يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- (90:11) [listed for 87:11] فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- (91:8) [listed for 87:11] فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- (96:7) [listed for 87:11] أَن رَّءَاهُ ٱسْتَغْنَىٰٓ

## named by the passage's own list as weak for this ayah (3)

- (37:66) [listed for 87:11] فَإِنَّهُمْ لَءَاكِلُونَ مِنْهَا فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (59:20) [listed for 87:11] لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- (108:3) [listed for 87:11] إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ

## neighbours: within two ayat of a passage the commentary cites (76)

- (1:5) [next to 1:7] إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- (1:6) [next to 1:7] ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (4:34) [next to 4:36] ٱلرِّجَالُ قَوَّٰمُونَ عَلَى ٱلنِّسَآءِ بِمَا فَضَّلَ ٱللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍۢ وَبِمَآ أَنفَقُوا۟ مِنْ أَمْوَٰلِهِمْ ۚ فَٱلصَّٰلِحَٰتُ قَٰنِتَٰتٌ حَٰفِظَٰتٌۭ لِّلْغَيْبِ بِمَا حَفِظَ ٱللَّهُ ۚ وَٱلَّٰتِى تَخَافُونَ نُشُوزَهُنَّ فَعِظُوهُنَّ وَٱهْجُرُوهُنَّ فِى ٱلْمَضَاجِعِ وَٱضْرِبُوهُنَّ ۖ فَإِنْ أَطَعْنَكُمْ فَلَا تَبْغُوا۟ عَلَيْهِنَّ سَبِيلًا ۗ إِنَّ ٱللَّهَ كَانَ عَلِيًّۭا كَبِيرًۭا
- (4:35) [next to 4:36] وَإِنْ خِفْتُمْ شِقَاقَ بَيْنِهِمَا فَٱبْعَثُوا۟ حَكَمًۭا مِّنْ أَهْلِهِۦ وَحَكَمًۭا مِّنْ أَهْلِهَآ إِن يُرِيدَآ إِصْلَٰحًۭا يُوَفِّقِ ٱللَّهُ بَيْنَهُمَآ ۗ إِنَّ ٱللَّهَ كَانَ عَلِيمًا خَبِيرًۭا
- (4:37) [next to 4:36] ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ وَيَكْتُمُونَ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۗ وَأَعْتَدْنَا لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
- (4:38) [next to 4:36] وَٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُونَ بِٱللَّهِ وَلَا بِٱلْيَوْمِ ٱلْءَاخِرِ ۗ وَمَن يَكُنِ ٱلشَّيْطَٰنُ لَهُۥ قَرِينًۭا فَسَآءَ قَرِينًۭا
- (4:41) [next to 4:43] فَكَيْفَ إِذَا جِئْنَا مِن كُلِّ أُمَّةٍۭ بِشَهِيدٍۢ وَجِئْنَا بِكَ عَلَىٰ هَٰٓؤُلَآءِ شَهِيدًۭا
- (4:42) [next to 4:43] يَوْمَئِذٍۢ يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ وَعَصَوُا۟ ٱلرَّسُولَ لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ وَلَا يَكْتُمُونَ ٱللَّهَ حَدِيثًۭا
- (4:44) [next to 4:43] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يَشْتَرُونَ ٱلضَّلَٰلَةَ وَيُرِيدُونَ أَن تَضِلُّوا۟ ٱلسَّبِيلَ
- (4:45) [next to 4:43] وَٱللَّهُ أَعْلَمُ بِأَعْدَآئِكُمْ ۚ وَكَفَىٰ بِٱللَّهِ وَلِيًّۭا وَكَفَىٰ بِٱللَّهِ نَصِيرًۭا
- (11:103) [next to 11:105] إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّمَنْ خَافَ عَذَابَ ٱلْءَاخِرَةِ ۚ ذَٰلِكَ يَوْمٌۭ مَّجْمُوعٌۭ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌۭ مَّشْهُودٌۭ
- (11:104) [next to 11:105] وَمَا نُؤَخِّرُهُۥٓ إِلَّا لِأَجَلٍۢ مَّعْدُودٍۢ
- (11:107) [next to 11:105] خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۚ إِنَّ رَبَّكَ فَعَّالٌۭ لِّمَا يُرِيدُ
- (11:108) [next to 11:106] ۞ وَأَمَّا ٱلَّذِينَ سُعِدُوا۟ فَفِى ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۖ عَطَآءً غَيْرَ مَجْذُوذٍۢ
- (14:33) [next to 14:35] وَسَخَّرَ لَكُمُ ٱلشَّمْسَ وَٱلْقَمَرَ دَآئِبَيْنِ ۖ وَسَخَّرَ لَكُمُ ٱلَّيْلَ وَٱلنَّهَارَ
- (14:34) [next to 14:35] وَءَاتَىٰكُم مِّن كُلِّ مَا سَأَلْتُمُوهُ ۚ وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱلْإِنسَٰنَ لَظَلُومٌۭ كَفَّارٌۭ
- (14:37) [next to 14:35] رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ
- (14:38) [next to 14:36] رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (16:34) [next to 16:36] فَأَصَابَهُمْ سَيِّـَٔاتُ مَا عَمِلُوا۟ وَحَاقَ بِهِم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (16:37) [next to 16:36] إِن تَحْرِصْ عَلَىٰ هُدَىٰهُمْ فَإِنَّ ٱللَّهَ لَا يَهْدِى مَن يُضِلُّ ۖ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (16:38) [next to 16:36] وَأَقْسَمُوا۟ بِٱللَّهِ جَهْدَ أَيْمَٰنِهِمْ ۙ لَا يَبْعَثُ ٱللَّهُ مَن يَمُوتُ ۚ بَلَىٰ وَعْدًا عَلَيْهِ حَقًّۭا وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (17:81) [next to 17:83] وَقُلْ جَآءَ ٱلْحَقُّ وَزَهَقَ ٱلْبَٰطِلُ ۚ إِنَّ ٱلْبَٰطِلَ كَانَ زَهُوقًۭا
- (17:84) [next to 17:83] قُلْ كُلٌّۭ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًۭا
- (17:85) [next to 17:83] وَيَسْـَٔلُونَكَ عَنِ ٱلرُّوحِ ۖ قُلِ ٱلرُّوحُ مِنْ أَمْرِ رَبِّى وَمَآ أُوتِيتُم مِّنَ ٱلْعِلْمِ إِلَّا قَلِيلًۭا
- (19:40) [next to 19:42] إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا وَإِلَيْنَا يُرْجَعُونَ
- (19:41) [next to 19:42] وَٱذْكُرْ فِى ٱلْكِتَٰبِ إِبْرَٰهِيمَ ۚ إِنَّهُۥ كَانَ صِدِّيقًۭا نَّبِيًّا
- (19:43) [next to 19:42] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (19:44) [next to 19:42] يَٰٓأَبَتِ لَا تَعْبُدِ ٱلشَّيْطَٰنَ ۖ إِنَّ ٱلشَّيْطَٰنَ كَانَ لِلرَّحْمَٰنِ عَصِيًّۭا
- (19:45) [next to 19:46] يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ فَتَكُونَ لِلشَّيْطَٰنِ وَلِيًّۭا
- (19:50) [next to 19:48] وَوَهَبْنَا لَهُم مِّن رَّحْمَتِنَا وَجَعَلْنَا لَهُمْ لِسَانَ صِدْقٍ عَلِيًّۭا
- (19:51) [next to 19:49] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مُوسَىٰٓ ۚ إِنَّهُۥ كَانَ مُخْلَصًۭا وَكَانَ رَسُولًۭا نَّبِيًّۭا
- (20:0) [next to 20:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (20:1) [next to 20:2] طه
- (20:4) [next to 20:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:115) [next to 20:117] وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا
- (20:116) [next to 20:117] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ
- (20:120) [next to 20:118] فَوَسْوَسَ إِلَيْهِ ٱلشَّيْطَٰنُ قَالَ يَٰٓـَٔادَمُ هَلْ أَدُلُّكَ عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ
- (20:121) [next to 20:119] فَأَكَلَا مِنْهَا فَبَدَتْ لَهُمَا سَوْءَٰتُهُمَا وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِن وَرَقِ ٱلْجَنَّةِ ۚ وَعَصَىٰٓ ءَادَمُ رَبَّهُۥ فَغَوَىٰ
- (20:122) [next to 20:123] ثُمَّ ٱجْتَبَٰهُ رَبُّهُۥ فَتَابَ عَلَيْهِ وَهَدَىٰ
- (20:125) [next to 20:123] قَالَ رَبِّ لِمَ حَشَرْتَنِىٓ أَعْمَىٰ وَقَدْ كُنتُ بَصِيرًۭا
- (20:126) [next to 20:124] قَالَ كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ
- (22:28) [next to 22:30] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:29) [next to 22:30] ثُمَّ لْيَقْضُوا۟ تَفَثَهُمْ وَلْيُوفُوا۟ نُذُورَهُمْ وَلْيَطَّوَّفُوا۟ بِٱلْبَيْتِ ٱلْعَتِيقِ
- (22:31) [next to 22:30] حُنَفَآءَ لِلَّهِ غَيْرَ مُشْرِكِينَ بِهِۦ ۚ وَمَن يُشْرِكْ بِٱللَّهِ فَكَأَنَّمَا خَرَّ مِنَ ٱلسَّمَآءِ فَتَخْطَفُهُ ٱلطَّيْرُ أَوْ تَهْوِى بِهِ ٱلرِّيحُ فِى مَكَانٍۢ سَحِيقٍۢ
- (22:32) [next to 22:30] ذَٰلِكَ وَمَن يُعَظِّمْ شَعَٰٓئِرَ ٱللَّهِ فَإِنَّهَا مِن تَقْوَى ٱلْقُلُوبِ
- (23:103) [next to 23:105] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (23:104) [next to 23:105] تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ
- (23:107) [next to 23:105] رَبَّنَآ أَخْرِجْنَا مِنْهَا فَإِنْ عُدْنَا فَإِنَّا ظَٰلِمُونَ
- (23:108) [next to 23:106] قَالَ ٱخْسَـُٔوا۟ فِيهَا وَلَا تُكَلِّمُونِ
- (39:15) [next to 39:17] فَٱعْبُدُوا۟ مَا شِئْتُم مِّن دُونِهِۦ ۗ قُلْ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَا ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (39:16) [next to 39:17] لَهُم مِّن فَوْقِهِمْ ظُلَلٌۭ مِّنَ ٱلنَّارِ وَمِن تَحْتِهِمْ ظُلَلٌۭ ۚ ذَٰلِكَ يُخَوِّفُ ٱللَّهُ بِهِۦ عِبَادَهُۥ ۚ يَٰعِبَادِ فَٱتَّقُونِ
- (39:19) [next to 39:17] أَفَمَنْ حَقَّ عَلَيْهِ كَلِمَةُ ٱلْعَذَابِ أَفَأَنتَ تُنقِذُ مَن فِى ٱلنَّارِ
- (39:20) [next to 39:18] لَٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ غُرَفٌۭ مِّن فَوْقِهَا غُرَفٌۭ مَّبْنِيَّةٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ ٱلْمِيعَادَ
- (39:51) [next to 39:53] فَأَصَابَهُمْ سَيِّـَٔاتُ مَا كَسَبُوا۟ ۚ وَٱلَّذِينَ ظَلَمُوا۟ مِنْ هَٰٓؤُلَآءِ سَيُصِيبُهُمْ سَيِّـَٔاتُ مَا كَسَبُوا۟ وَمَا هُم بِمُعْجِزِينَ
- (39:52) [next to 39:53] أَوَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (39:54) [next to 39:53] وَأَنِيبُوٓا۟ إِلَىٰ رَبِّكُمْ وَأَسْلِمُوا۟ لَهُۥ مِن قَبْلِ أَن يَأْتِيَكُمُ ٱلْعَذَابُ ثُمَّ لَا تُنصَرُونَ
- (39:59) [next to 39:57] بَلَىٰ قَدْ جَآءَتْكَ ءَايَٰتِى فَكَذَّبْتَ بِهَا وَٱسْتَكْبَرْتَ وَكُنتَ مِنَ ٱلْكَٰفِرِينَ
- (39:60) [next to 39:58] وَيَوْمَ ٱلْقِيَٰمَةِ تَرَى ٱلَّذِينَ كَذَبُوا۟ عَلَى ٱللَّهِ وُجُوهُهُم مُّسْوَدَّةٌ ۚ أَلَيْسَ فِى جَهَنَّمَ مَثْوًۭى لِّلْمُتَكَبِّرِينَ
- (53:30) [next to 53:32] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (53:31) [next to 53:32] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
- (53:33) [next to 53:32] أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ
- (53:34) [next to 53:32] وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ
- (74:47) [next to 74:49] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
- (74:48) [next to 74:49] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
- (74:52) [next to 74:50] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
- (74:53) [next to 74:51] كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ
- (92:5) [next to 92:7] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (92:6) [next to 92:7] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:8) [next to 92:7] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- (92:9) [next to 92:7] وَكَذَّبَ بِٱلْحُسْنَىٰ
- (92:11) [next to 92:10] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (92:12) [next to 92:10] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:13) [next to 92:14] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:19) [next to 92:17] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (92:20) [next to 92:18] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ

