Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:19; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_19/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_19.reading.tr.md (prose paragraphs numbered) =====
## Sure iki adla kapanıyor

[¶1] Son ayetin kendi fiili yok. On sekizinci ayet bir hüküm vermişti: {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâzâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18}. On dokuzuncu ayet bu "ilk sayfalar"ın hangileri olduğunu söyler. Aynı esreyle önceki ayetin son kelimelerine eklenir ve onları açıklayan bir ek ad gibi durur: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi ibrâhîme ve mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}. Ayet yeni bir hüküm getirmez. Önceki ayetin adsız bıraktığı yere iki ad koyar. "İlk sayfalar" uzak, kimsesiz bir geçmişi anlatabilirdi. Ayet onları iki tanınmış insana bağlar ve bu adlarla sure biter.

[¶2] "Bu" kelimesi geriye bakar. Ona en yakın olan, on altıncı ve on yedinci ayetlerdeki karşıtlıktır: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'sirûne'l-hayâte'd-dunyâ, gloss:hayır, siz dünya hayatını öne alıyorsunuz, source:87:16}, {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Ama işaret sözcüğü yalnızca bir cümleyi göstermek zorunda değildir. On dördüncü ayetteki arınanın kurtuluşu da, hatta surenin baştan sona söylediği her şey de bu "bu"nun kapsamına girebilir. Aşağıda görüleceği gibi, İbrahim'in ve Musa'nın Kur'an'da anlatılan sözleri bu surenin başına, ortasına ve sonuna dağılmış hâlde durur. Bu da işaretin geniş tutulmasını haklı çıkarır.

[¶3] Surenin bütün ayetleri uzun bir "â" sesiyle biter. Son ayet de bu sesi Musa'nın adıyla tamamlar: {ar:وَمُوسَىٰ, tr:ve mûsâ, gloss:ve Musa, source:87:19}. Kur'an aynı iki adı bir başka surede ters sırayla anar. Orada Allah, yüz çevirip az verdikten sonra elini çeken birinden söz eder ve sorar: {ar:أَعِندَهُۥ عِلْمُ ٱلْغَيْبِ فَهُوَ يَرَىٰٓ, tr:e-indehû ilmu'l-ğaybi fe-huve yerâ, gloss:gaybın bilgisi onun yanında mı ki görüyor, source:53:35}. Ardından şu soru gelir: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bimâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarında olan ona haber verilmedi mi, source:53:36}. Hemen ardından İbrahim gelir: {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'llezî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in, source:53:37}. İki yerde de bu sayfalar yüz çeviren birine karşı tanık olarak anılır. Bizim surede yüz çeviren, on birinci ayette öğütten kaçınan {ar:ٱلْأَشْقَى, tr:el-eşkâ, gloss:en bedbaht olan, source:87:11} kişidir.

## Sahîfe: üzerine söz serilen deri

[¶4] Ayetteki ilk kelime bir nesnedir ve önce o nesnenin ne olduğunu bilmek gerekir. Araplar sahîfe derken üzerine yazı yazılan bir parçayı kastederdi ve onu şöyle tarif ederlerdi: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıt'atu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhufun tekili sahîfedir; o, üzerine yazılan ak deri ya da parşömen parçasıdır, source:"ص ح ف,B002"}. Ayetteki "suhuf" bu kelimenin çoğuludur. Türkçede "sahife" ve ondan türeyen "sayfa", ciltli bir kitabın numaralı yüzüne dönüşmüştür. Bu sayfa bir bütünün parçasıdır, sırası ve numarası vardır. Arapçadaki sahîfe ise kendi başına bir yapraktı: tabaklanmış, ağartılmış, yazı yazılsın diye hazırlanmış tek bir deri ya da parşömen. Bu yapraklar toplanıp iki kapak arasına girdiğinde başka bir ad alırdı: {ar:المصحف ما جعل جامعا للصحف المكتوبة, tr:el-mushaf mâ cu'ile câmi'an li's-suhufi'l-mektûbe, gloss:mushaf yazılı sayfaları bir araya toplamak için yapılmış şeydir, source:"ص ح ف,B003"}. Bu ayette bir mushaf yok. İki ayrı insana ait, ayrı yapraklar var. Onları bir araya getiren cilt değil, on sekizinci ayetteki tek bir "bu"dur. Kapakları ayrı olan yapraklar aynı sözü taşır.

[¶5] Kelimenin buradaki anlamı "yazı yaprakları"dır. Aynı kökün başka kullanımlarından gelen resimler bu anlamın yanında duyulur, onun yerine geçmez. Kökün en temel resmi bir şeyin yayılıp genişlemesidir: {ar:أصل صحيح يدل على انبساط في شيء وسعة, tr:aslun sahîhun yedullu alâ inbisâtin fî şey'in ve se'a, gloss:bir şeydeki yayılmayı ve genişliği gösteren sağlam bir asıl, source:"ص ح ف,B001"}. Yeryüzünün açık yüzüne {ar:الصحيف وجه الأرض, tr:es-sahîf vechu'l-ard, gloss:sahîf yeryüzünün yüzüdür, source:"ص ح ف,B001"} denirdi. İnsan yüzünün derisine de aynı ad verilirdi: {ar:صحيفة الوجه بشرة جلده, tr:sahîfetu'l-vech beşeratu cildih, gloss:yüzün sahîfesi derisinin dış yüzüdür, source:"ص ح ف,B001"}. Yazı yaprağı da bu tür bir yüzeydir: {ar:الصحيفة المبسوط من الشيء كصحيفة الوجه, tr:es-sahîfetu'l-mebsûtu mine'ş-şey' ke-sahîfeti'l-vech, gloss:sahîfe bir şeyin yayılmış kısmıdır, yüzün sahîfesi gibi, source:"ص ح ف,B001"}. Bir yüzde ne varsa görünür. Söz de düz ve açık bir yüzeye serilir ki gözle okunabilsin.

[¶6] Kök, yayvan yüzeyin bir işini daha adlandırır. Geniş ve yayvan çanağa {ar:الصحفة القصعة المسلنطحة, tr:es-sahfatu'l-kas'atu'l-muslentıha, gloss:sahfe yayvan, geniş çanaktır, source:"ص ح ف,B004"} denirdi. Su birikmesi için kazılan küçük çukurlara da {ar:الصحاف مناقع صغار تتخذ للماء, tr:es-sıhâfu menâkı'u sığârun tuttehazu li'l-mâ', gloss:sıhâf su için yapılan küçük birikinti çukurlarıdır, source:"ص ح ف,B004"} adı verilirdi. Çanak da çukur da genişliğini bir şeyi tutmak için kullanır: açık yüzey, içine konanı dağıtmadan saklar. Yazı yaprağı bu iki işi birlikte yapar. Sözü bir yüz gibi gösterir, bir çanak gibi de tutar. Sure dördüncü ve beşinci ayetlerde yeşerip kuruyan, sonra selin götürdüğü bir otlak gösterir. O resim surenin geneline aittir. Burada yalnızca şu kadarı duyulur: surenin sonunda sözü tutan bir yüzey vardır ve bu yüzey yüzyıllar boyunca dağılmamıştır.

[¶7] Kur'an sayfaları açılıp serilen şeyler olarak da anar. Güneşin dürüldüğü ve yıldızların söndüğü bir sonun anlatıldığı yerde {ar:وَإِذَا ٱلصُّحُفُ نُشِرَتْ, tr:ve izâ's-suhufu nuşirat, gloss:sayfalar açılıp serildiği zaman, source:81:10} denir. Bir başka surede öğütten {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:ke-ennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri gibi, source:74:50} kaçanlardan söz edilir. Onların isteği şudur: {ar:بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ, tr:bel yurîdu kullu'mriin minhum en yu'tâ suhufen munecşşera, gloss:hayır, her biri kendisine açılıp serilmiş sayfalar verilmesini ister, source:74:52}. Taha suresinin sonunda da inkârcılar {ar:لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ, tr:levlâ ye'tînâ bi-âyetin min rabbih, gloss:bize Rabbinden bir ayet getirse ya, source:20:133} der ve şu cevabı alır: {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:ilk sayfalarda olanın açık delili onlara gelmedi mi, source:20:133}. Her biri kendine özel bir sayfa ister. Kur'an ise sayfanın zaten var olduğunu söyler: eskidir, iki tanınmış insanın adını taşır ve içindeki söz şimdi bir öğüt olarak yeniden gelmiştir.

## İki saklama: okutulan kalp ve yazılı yaprak

[¶8] Surenin altıncı ayeti sözü bir hafızaya emanet eder: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Okutmanın ve unutmamanın oluşturduğu sahne surenin geneline aittir. Bu ayet o sahneye bir karşılık ekler. Aynı söz yalnızca okutulan bir kalpte değil, yazılmış yapraklarda da durur. Böylece sure sözü saklamanın iki yolunu yan yana koyar.

[¶9] Yazılı yaprağın kendine özgü bir zayıflığı vardır ve Arapça bu zayıflığa aynı kökten bir ad vermiştir. Sayfayı yanlış okumaya taṣḥîf denirdi: {ar:التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه, tr:et-tashîf kırâetu'l-mushafi ve rivâyetuhû alâ ğayri mâ huve li'ştibâhi hurûfih, gloss:tashîf, harfleri birbirine benzediği için yazılı metni olduğundan başka türlü okuyup aktarmaktır, source:"ص ح ف,B005"}. Sözü bir hocanın ağzından değil yalnızca sayfadan alan, bu yüzden benzer harfleri karıştırıp yanlış aktaran kişiye de sahafî denirdi: {ar:الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف, tr:es-sahafiyyu'llezî yervi'l-hata'e an kırâeti's-suhufi bi-eşbâhi'l-hurûf, gloss:sahafî, sayfaları benzer harflerle okuyup yanlışı aktaran kişidir, source:"ص ح ف,B005"}. İşleyiş basittir. Yaprak harfin biçimini saklar ama sesini saklamaz. İki harfin biçimi birbirine yakınsa, sesi duymamış göz yanılabilir. Sayfa sözü tutar, ama okuyanın gözüne muhtaçtır.

[¶10] Bu surenin muhatabı sözü sayfadan almaz. Kur'an Peygamber'e, kendisine indirilen kitaptan söz ettiği yerde şöyle der: {ar:وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ, tr:ve mâ kunte tetlû min kablihî min kitâbin ve lâ tehuttuhû bi-yemînik, gloss:sen bundan önce hiçbir kitap okumuyordun, onu sağ elinle de yazmıyordun, source:29:48}. Yine de bir başka surede o, açık delilin gelişi anlatılırken {ar:رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ, tr:rasûlun mina'llâhi yetlû suhufen mutahhara, gloss:arınmış sayfaları okuyan, Allah'tan bir elçi, source:98:2} diye tanıtılır. Sayfa okuyan ama sayfadan okumayan bir elçi. Bu iki ayetin buluştuğu yerde sure altıncı ayetteki fiili koyar: sana okutacağız. Benzer harflerin gözü yanılttığı yaprağın yerine, sesin sese aktarıldığı bir okutma gelir. Bu bir yorumdur ama dayanağı açıktır: sure aynı sözün hem eski yapraklarda hem de okutulan bir kalpte durduğunu söyler, ve ikincisini Allah'ın kendi işi olarak verir.

[¶11] Bu iki saklamanın üstünde üçüncüsü durur ve onu Musa söyler. Firavun, Rabbinin kim olduğunu soran konuşmanın ortasında ona geçmiş nesilleri sorar: {ar:قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:kâle fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:o hâlde ilk nesillerin durumu ne, dedi, source:20:51}. Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb, lâ yadıllu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne şaşırır ne unutur, source:20:52}. Surenin "ilk" kelimesi de altıncı ayetin unutma fiili de bu cevapta geçer. Musa'nın sözüne göre ilklerin bilgisi, yanılmayan ve unutmayan birinin yanında yazılıdır. Gözün yanılabildiği yaprak ile kalbin unutabildiği hafıza, ikisi de bu korunmuş bilgiye dayanır.

## İlk sayfalar son yurdu anlatır

[¶12] On yedinci ve on sekizinci ayetlerde iki kelime yan yana gelir: biri {ar:وَٱلْءَاخِرَةُ, tr:ve'l-âhiratu, gloss:ve ahiret, source:87:17}, öbürü {ar:ٱلْأُولَىٰ, tr:el-ûlâ, gloss:ilk, source:87:18}. Kur'an bu iki kelimeyi başka yerlerde bir çift olarak kullanır. Allah bir surede {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:doğru yolu göstermek bize düşer, source:92:12} dedikten sonra {ar:وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ, tr:ve inne lenâ le'l-âhirate ve'l-ûlâ, gloss:sonuncu da ilki de bizimdir, source:92:13} der. Peygamber'e de {ar:وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ, tr:ve le'l-âhiratu hayrun leke mine'l-ûlâ, gloss:sonuncusu senin için ilkinden daha hayırlıdır, source:93:4} denir. Bu ayetlerde "ilk", bu dünyadaki hayatı anlatır. Bizim surede ise aynı kelime sayfaların sıfatıdır. Böylece on yedinci ayetin sonunda "son" duyulur, hemen ardından "ilk" gelir, ama bu kez ilk olan bir ömür değil, bir yazıdır. En eski yapraklar en son yurdu anlatır.

[¶13] O yaprakların içeriğini Kur'an, yukarıda anılan sorunun hemen ardından sıralar: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}, {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ se'â, gloss:insana ancak kendi çabası vardır, source:53:39}, {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:onun çabası görülecektir, source:53:40}, {ar:ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ, tr:summe yuczâhu'l-cezâe'l-evfâ, gloss:sonra karşılığı tam olarak verilecektir, source:53:41}, {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu sure insanları iki kişiye ayırır. Biri öğütten kaçınır ve büyük ateşe girer. Öbürü {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad efleha men tezekkâ, gloss:arınan kurtuluşa ermiştir, source:87:14}. İkisinin de sonucu kendi yaptığından doğar. Kimse başkasının yerine arınmaz, kimse başkasının yerine ateşe girmez. Eski yaprakların ilk maddesi bu ayrımın kuralını koyar.

[¶14] Liste aynı yerde devam eder ve on üçüncü ayetteki tuhaf durumun karşısına bir ölçü koyar. Yaprakların söylediğine göre Allah {ar:وَأَنَّهُۥ هُوَ أَمَاتَ وَأَحْيَا, tr:ve ennehû huve emâte ve ahyâ, gloss:öldüren de dirilten de odur, source:53:44}. Surede ateşe giren kişi ise {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:summe lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. Ölümü ve hayatı veren birinin varlığı, ikisinin de esirgendiği bir durumu anlaşılır kılar. Yapraklar bir dönüşü de söyler: {ar:وَأَنَّ عَلَيْهِ ٱلنَّشْأَةَ ٱلْأُخْرَىٰ, tr:ve enne aleyhi'n-neş'ete'l-uhrâ, gloss:öteki yaratılış da ona düşer, source:53:47}.

[¶15] Bu, on yedinci ayetteki "daha kalıcı" sözüne sessiz bir delil de ekler. Kalıcı olanın daha hayırlı olduğu söz, kendisi de kalıcı olmuştur. İbrahim'den ve Musa'dan bu yana yapraklar eskimiş ama söz düşmemiştir. Sure bunu açıkça söylemez. Ancak "ahiret daha kalıcıdır" cümlesinin hemen ardından "bu ilk sayfalarda vardır" demesi, iddiayı bir örnekle destekler.

## İbrahim'in sözü surenin başında

[¶16] Kur'an İbrahim'in kavmiyle konuşmasını şöyle anlatır. İbrahim babasına ve kavmine ne taptıklarını sorar. Onlar putlara taptıklarını söyler. İbrahim putların duyup duymadığını, işe yarayıp yaramadığını sorar: {ar:أَوْ يَنفَعُونَكُمْ أَوْ يَضُرُّونَ, tr:ev yenfe'ûnekum ev yedurrûn, gloss:yahut size fayda ya da zarar veriyorlar mı, source:26:73}. Kavmin tek dayanağı geçmiştir: {ar:بَلْ وَجَدْنَآ ءَابَآءَنَا كَذَٰلِكَ يَفْعَلُونَ, tr:bel vecednâ âbâenâ kezâlike yef'alûn, gloss:hayır, babalarımızı böyle yaparken bulduk, source:26:74}. İbrahim bu eskilere, {ar:أَنتُمْ وَءَابَآؤُكُمُ ٱلْأَقْدَمُونَ, tr:entum ve âbâukumu'l-akdemûn, gloss:siz ve en eski atalarınız, source:26:76}, yüz çevirir ve Rabbini şöyle tanıtır: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halekanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren odur, source:26:78}, {ar:وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ, tr:vellezî yumîtunî summe yuhyîn, gloss:beni öldürecek, sonra diriltecek olan odur, source:26:81}.

[¶17] Bu surenin açılışı da aynı kalıpla kurulmuştur: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:vellezî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Her ikisinde de Rab bir isimle değil, yaptıklarıyla tanıtılır. "O ki…" diye başlayan cümleler art arda gelir, "yarattı" ile "yol gösterdi" arasında da aynı "fe" bağlacı durur. Kelimeler aynı değildir: İbrahim kendi bedeninden, yiyeceğinden, hastalığından söz eder. Sure ise her şeyden söz eder. Ama yapı aynıdır. Sure son ayetinde İbrahim'in adını anınca, birinci ayetteki tanıtmanın daha önce kimin ağzından duyulduğu da anlaşılır.

[¶18] Burada bir incelik var. İbrahim'in kavmi "ilk" olana, yani atalara dayanıyordu. Bu sure de "ilk sayfalar"a dayanır. Ama surenin dayandığı ilk, atalarının yolunu bırakan adamın sayfasıdır. Eskilik kendi başına bir ölçü değildir. Sure eski bir alışkanlığı değil, eski bir uyarıyı çağırır.

[¶19] İbrahim'in başka sahneleri de surenin kelimeleriyle örtüşür. Kendisine hükümranlık verilmiş biriyle Rabbi hakkında tartışırken şöyle der: {ar:رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ, tr:rabbiye'llezî yuhyî ve yumît, gloss:Rabbim diriltendir, öldürendir, source:2:258}. Gece bir yıldız gördüğünde, sonra ayı ve güneşi gördüğünde her birinin batışını izler ve şöyle der: {ar:لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:lâ uhibbu'l-âfilîn, gloss:batıp gidenleri sevmem, source:6:76}. Bu, on altıncı ve on yedinci ayetlerdeki tercihin bir gökyüzü sahnesinde yaşanmasıdır: göze en parlak görünen bile batar, kalbin bağlanacağı şey kalıcı olandır. Ay battığında söylediği söz Fatiha'nın son kelimesini taşır: {ar:لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ, tr:le-in lem yehdinî rabbî le-ekûnenne mine'l-kavmi'd-dâllîn, gloss:Rabbim bana yol göstermezse yolunu şaşıranlardan olurum, source:6:77}. Her namazda okunan {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâte'l-mustekîm, gloss:bizi dosdoğru yola ilet, source:1:6} duası ilk kez İbrahim'in bu gecesinde dile gelmiş gibidir.

[¶20] Surenin ortasındaki kelimeler İbrahim'in dualarında da geçer. Oğluyla birlikte Evin temellerini yükseltirken Rabbinden bir elçi ister: {ar:يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِكَ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُزَكِّيهِمْ, tr:yetlû aleyhim âyâtike ve yu'allimuhumu'l-kitâbe ve'l-hikmete ve yuzekkîhim, gloss:onlara ayetlerini okuyacak, onlara kitabı ve hikmeti öğretecek ve onları arındıracak, source:2:129}. İbrahim'in istediği elçi okur ve arındırır. Bu surede elçiye okutulur ve {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad efleha men tezekkâ, gloss:arınan kurtuluşa ermiştir, source:87:14} denir. Arınmanın kökü İbrahim'in duasındaki kökle aynıdır. İbrahim kendisi için de şöyle dua eder: {ar:رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ, tr:rabbi'c'alnî mukîme's-salâh, gloss:Rabbim, beni namazı dosdoğru kılan biri yap, source:14:40}. Surenin kurtuluşa erdiği kişi ise {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve zekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kılar, source:87:15}. İbrahim'in bir duası da bu ayetin varlığına karşılık gibi durur: {ar:وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ, tr:vec'al lî lisâne sıdkın fi'l-âhirîn, gloss:sonra gelenler arasında benim için doğru bir dil var et, source:26:84}. Sonra gelen bir surenin son cümlesi onun adını doğru bir sözün sahibi olarak anar.

## Musa'nın görevi surenin ortasında

[¶21] Musa'nın sayfaları da surenin içinde okunabilir, özellikle de onun Firavun'a gönderilişinde. Allah Musa'yı kardeşiyle birlikte gönderirken önce {ar:وَلَا تَنِيَا فِى ذِكْرِى, tr:ve lâ teniyâ fî zikrî, gloss:beni anmakta gevşemeyin, source:20:42} der, sonra şöyle emreder: {ar:فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ, tr:fe-kûlâ lehû kavlen leyyinen le'allehû yetezekkeru ev yahşâ, gloss:ona yumuşak bir söz söyleyin, belki öğüt alır ya da korkar, source:20:44}. Bu surenin onuncu ayeti aynı iki fiili birleştirir: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:korkan öğüt alacaktır, source:87:10}. Musa'ya verilen görev "belki" ile biter. Bu surede Peygamber'e verilen görev de bir şartla kayıtlıdır: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefe'ati'z-zikrâ, gloss:öğüt fayda verecekse öğüt ver, source:87:9}. İki elçi de aynı işi yapar. Söz söylenir, ama öğüt almak muhatabın korkusuna bağlıdır.

[¶22] Aynı görevin bir başka anlatımında Musa'nın Firavun'a söyleyeceği söz bu surenin kelimeleriyle örülüdür: {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:de ki: arınmaya niyetin var mı, source:79:18}, {ar:وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ, tr:ve ehdiyeke ilâ rabbike fe-tahşâ, gloss:seni Rabbine ileteyim de korkasın, source:79:19}. Arınmak, yol göstermek ve korkmak bu surenin on dördüncü, üçüncü ve onuncu ayetlerindeki kelimelerdir. Musa'nın Firavun'a sunduğu şey, surenin kurtuluşa erdiği kişinin yoludur. Firavun bu yolu seçmez. Ona {ar:ٱلْءَايَةَ ٱلْكُبْرَىٰ, tr:el-âyete'l-kubrâ, gloss:en büyük ayet, source:79:20} gösterilir, o ise yalanlar, karşı gelir, arkasını döner, halkı toplar ve şöyle seslenir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:dedi ki: ben sizin en yüce Rabbinizim, source:79:24}. Bu surenin ilk ayeti aynı sıfatı gerçek sahibine verir: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Firavun'un sonu da anlatılır: {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonun ve ilkin ibret verici cezasıyla yakaladı, source:79:25}. Sonun ve ilkin bir arada anıldığı bu cümle, surenin on yedinci ve on sekizinci ayetlerindeki çifte bir başka açıdan bakar. Anlatım ise şöyle kapanır: {ar:إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ, tr:inne fî zâlike le-ibraten li-men yahşâ, gloss:bunda korkan için elbette bir ibret vardır, source:79:26}. Bu surede adı geçmeyen en bedbaht kişi, Musa'nın hikâyesinde bir yüz kazanır.

[¶23] Firavun, Rabbinin kim olduğunu sorduğunda, {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbukumâ yâ mûsâ, gloss:ey Musa, ikinizin Rabbi kim, dedi, source:20:49}, Musa'nın cevabı da İbrahim'inki gibi bir "o ki" cümlesidir: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunâ'llezî a'tâ kulle şey'in halkahû summe hedâ, gloss:Rabbimiz her şeye yaratılışını veren, sonra yol gösterendir, source:20:50}. Yaratmak ve yol göstermek, surenin ikinci ve üçüncü ayetlerindeki fiillerle aynı sıradadır. Konuşma devam eder ve "biz" diliyle yeryüzüne geçer: gökten su indirilir, {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkilerden çiftler çıkardık, source:20:53}. Ardından {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ, tr:kulû ver'av en'âmekum, gloss:yiyin ve hayvanlarınızı otlatın, source:20:54} denir. Bu, surenin dördüncü ayetindeki çıkarma fiili ve otlak kelimesiyle aynı köktendir: {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:vellezî ahraca'l-mer'â, gloss:otlağı çıkaran, source:87:4}. Böylece surenin ilk dört ayetinde tanıtılan Rab, Musa'nın Firavun'un karşısında tanıttığı Rabbin ta kendisidir, hem de neredeyse aynı sırayla: yaratma, yol gösterme, sonra yerden otlak çıkarma.

[¶24] Musa'nın hikâyesinde sihirbazların sahnesi de vardır. Sihirbazlar Firavun'u {ar:لَن نُّؤْثِرَكَ, tr:len nu'sirak, gloss:seni asla üstün tutmayız, source:20:72} diyerek reddeder ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:va'llâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Bu sahne surenin on altıncı ve on yedinci ayetlerinin kelimeleriyle kuruludur ve surenin bütünü içinde ele alınır. Son ayet Musa'nın adını anarak bu tercihin de, bu tercihi yapanların da daha önce nerede görüldüğünü gösterir. Sure, en yüce Rabbin adını anma emriyle açılmış ve bu adı yanlış yere takan birinin karşısında doğru adı söyleyen bir elçinin adıyla kapanmıştır.

===== _commentary/v16/out/87_19/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: 87:19 grammatically an apposition (badal) to al-suhuf al-ula, from case agreement
- memory: tashif arises because Arabic letters share shapes; the mechanism is described from general knowledge
- not written: sihaf of gold in 43:71 (B004) - a same-root echo with no theme to carry it
- not written: Musa's tablets (alwah) - the Quran does not equate them with these suhuf
- not written: names Ibrahim and Musa - no root given; no etymology attempted
- not written: 80:13-14 honoured, raised pages - images.md already covers them; no new theme here

===== passages not cited (185) =====
## strong (this ayah's own list) (40)

- (2:136) [listed for 87:19] قُولُوٓا۟ ءَامَنَّا بِٱللَّهِ وَمَآ أُنزِلَ إِلَيْنَا وَمَآ أُنزِلَ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَمَآ أُوتِىَ مُوسَىٰ وَعِيسَىٰ وَمَآ أُوتِىَ ٱلنَّبِيُّونَ مِن رَّبِّهِمْ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّنْهُمْ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (6:91) [listed for 87:19] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦٓ إِذْ قَالُوا۟ مَآ أَنزَلَ ٱللَّهُ عَلَىٰ بَشَرٍۢ مِّن شَىْءٍۢ ۗ قُلْ مَنْ أَنزَلَ ٱلْكِتَٰبَ ٱلَّذِى جَآءَ بِهِۦ مُوسَىٰ نُورًۭا وَهُدًۭى لِّلنَّاسِ ۖ تَجْعَلُونَهُۥ قَرَاطِيسَ تُبْدُونَهَا وَتُخْفُونَ كَثِيرًۭا ۖ وَعُلِّمْتُم مَّا لَمْ تَعْلَمُوٓا۟ أَنتُمْ وَلَآ ءَابَآؤُكُمْ ۖ قُلِ ٱللَّهُ ۖ ثُمَّ ذَرْهُمْ فِى خَوْضِهِمْ يَلْعَبُونَ
- (6:154) [listed for 87:19] ثُمَّ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ تَمَامًا عَلَى ٱلَّذِىٓ أَحْسَنَ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُم بِلِقَآءِ رَبِّهِمْ يُؤْمِنُونَ
- (7:145) [listed for 87:19] وَكَتَبْنَا لَهُۥ فِى ٱلْأَلْوَاحِ مِن كُلِّ شَىْءٍۢ مَّوْعِظَةًۭ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ فَخُذْهَا بِقُوَّةٍۢ وَأْمُرْ قَوْمَكَ يَأْخُذُوا۟ بِأَحْسَنِهَا ۚ سَأُو۟رِيكُمْ دَارَ ٱلْفَٰسِقِينَ
- (7:154) [listed for 87:19] وَلَمَّا سَكَتَ عَن مُّوسَى ٱلْغَضَبُ أَخَذَ ٱلْأَلْوَاحَ ۖ وَفِى نُسْخَتِهَا هُدًۭى وَرَحْمَةٌۭ لِّلَّذِينَ هُمْ لِرَبِّهِمْ يَرْهَبُونَ
- (11:17) [listed for 87:19] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ وَيَتْلُوهُ شَاهِدٌۭ مِّنْهُ وَمِن قَبْلِهِۦ كِتَٰبُ مُوسَىٰٓ إِمَامًۭا وَرَحْمَةً ۚ أُو۟لَٰٓئِكَ يُؤْمِنُونَ بِهِۦ ۚ وَمَن يَكْفُرْ بِهِۦ مِنَ ٱلْأَحْزَابِ فَٱلنَّارُ مَوْعِدُهُۥ ۚ فَلَا تَكُ فِى مِرْيَةٍۢ مِّنْهُ ۚ إِنَّهُ ٱلْحَقُّ مِن رَّبِّكَ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (17:2) [listed for 87:19] وَءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ أَلَّا تَتَّخِذُوا۟ مِن دُونِى وَكِيلًۭا
- (20:133) [listed for 87:19] [cited in ¶7] وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ
- (23:49) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ لَعَلَّهُمْ يَهْتَدُونَ
- (25:35) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَجَعَلْنَا مَعَهُۥٓ أَخَاهُ هَٰرُونَ وَزِيرًۭا
- (28:43) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ مِنۢ بَعْدِ مَآ أَهْلَكْنَا ٱلْقُرُونَ ٱلْأُولَىٰ بَصَآئِرَ لِلنَّاسِ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُمْ يَتَذَكَّرُونَ
- (32:23) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَلَا تَكُن فِى مِرْيَةٍۢ مِّن لِّقَآئِهِۦ ۖ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ
- (33:7) [listed for 87:19] وَإِذْ أَخَذْنَا مِنَ ٱلنَّبِيِّۦنَ مِيثَٰقَهُمْ وَمِنكَ وَمِن نُّوحٍۢ وَإِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَى ٱبْنِ مَرْيَمَ ۖ وَأَخَذْنَا مِنْهُم مِّيثَٰقًا غَلِيظًۭا
- (41:45) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَٱخْتُلِفَ فِيهِ ۗ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَقُضِىَ بَيْنَهُمْ ۚ وَإِنَّهُمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- (42:13) [listed for 87:19] ۞ شَرَعَ لَكُم مِّنَ ٱلدِّينِ مَا وَصَّىٰ بِهِۦ نُوحًۭا وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَمَا وَصَّيْنَا بِهِۦٓ إِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَىٰٓ ۖ أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ ۚ ٱللَّهُ يَجْتَبِىٓ إِلَيْهِ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَن يُنِيبُ
- (46:12) [listed for 87:19] وَمِن قَبْلِهِۦ كِتَٰبُ مُوسَىٰٓ إِمَامًۭا وَرَحْمَةًۭ ۚ وَهَٰذَا كِتَٰبٌۭ مُّصَدِّقٌۭ لِّسَانًا عَرَبِيًّۭا لِّيُنذِرَ ٱلَّذِينَ ظَلَمُوا۟ وَبُشْرَىٰ لِلْمُحْسِنِينَ
- (46:30) [listed for 87:19] قَالُوا۟ يَٰقَوْمَنَآ إِنَّا سَمِعْنَا كِتَٰبًا أُنزِلَ مِنۢ بَعْدِ مُوسَىٰ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ يَهْدِىٓ إِلَى ٱلْحَقِّ وَإِلَىٰ طَرِيقٍۢ مُّسْتَقِيمٍۢ
- (53:36) [listed for 87:19] [cited in ¶3] أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ
- (53:37) [listed for 87:19] [cited in ¶3] وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ
- (53:38) [listed for 87:19] [cited in ¶13] أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ
- (53:39) [listed for 87:19] [cited in ¶13] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
- (53:40) [listed for 87:19] [cited in ¶13] وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ
- (53:41) [listed for 87:19] [cited in ¶13] ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ
- (53:42) [listed for 87:19] [cited in ¶13] وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ
- (53:43) [listed for 87:19] وَأَنَّهُۥ هُوَ أَضْحَكَ وَأَبْكَىٰ
- (53:44) [listed for 87:19] [cited in ¶14] وَأَنَّهُۥ هُوَ أَمَاتَ وَأَحْيَا
- (53:45) [listed for 87:19] وَأَنَّهُۥ خَلَقَ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰ
- (53:46) [listed for 87:19] مِن نُّطْفَةٍ إِذَا تُمْنَىٰ
- (53:47) [listed for 87:19] [cited in ¶14] وَأَنَّ عَلَيْهِ ٱلنَّشْأَةَ ٱلْأُخْرَىٰ
- (53:48) [listed for 87:19] وَأَنَّهُۥ هُوَ أَغْنَىٰ وَأَقْنَىٰ
- (53:49) [listed for 87:19] وَأَنَّهُۥ هُوَ رَبُّ ٱلشِّعْرَىٰ
- (53:50) [listed for 87:19] وَأَنَّهُۥٓ أَهْلَكَ عَادًا ٱلْأُولَىٰ
- (53:51) [listed for 87:19] وَثَمُودَا۟ فَمَآ أَبْقَىٰ
- (53:52) [listed for 87:19] وَقَوْمَ نُوحٍۢ مِّن قَبْلُ ۖ إِنَّهُمْ كَانُوا۟ هُمْ أَظْلَمَ وَأَطْغَىٰ
- (53:53) [listed for 87:19] وَٱلْمُؤْتَفِكَةَ أَهْوَىٰ
- (53:54) [listed for 87:19] فَغَشَّىٰهَا مَا غَشَّىٰ
- (80:13) [listed for 87:19] فِى صُحُفٍۢ مُّكَرَّمَةٍۢ
- (80:14) [listed for 87:19] مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ
- (80:15) [listed for 87:19] بِأَيْدِى سَفَرَةٍۢ
- (80:16) [listed for 87:19] كِرَامٍۭ بَرَرَةٍۢ

## medium (this ayah's own list) (18)

- (2:53) [listed for 87:19] وَإِذْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَٱلْفُرْقَانَ لَعَلَّكُمْ تَهْتَدُونَ
- (2:87) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَقَفَّيْنَا مِنۢ بَعْدِهِۦ بِٱلرُّسُلِ ۖ وَءَاتَيْنَا عِيسَى ٱبْنَ مَرْيَمَ ٱلْبَيِّنَٰتِ وَأَيَّدْنَٰهُ بِرُوحِ ٱلْقُدُسِ ۗ أَفَكُلَّمَا جَآءَكُمْ رَسُولٌۢ بِمَا لَا تَهْوَىٰٓ أَنفُسُكُمُ ٱسْتَكْبَرْتُمْ فَفَرِيقًۭا كَذَّبْتُمْ وَفَرِيقًۭا تَقْتُلُونَ
- (3:65) [listed for 87:19] يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تُحَآجُّونَ فِىٓ إِبْرَٰهِيمَ وَمَآ أُنزِلَتِ ٱلتَّوْرَىٰةُ وَٱلْإِنجِيلُ إِلَّا مِنۢ بَعْدِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (3:84) [listed for 87:19] قُلْ ءَامَنَّا بِٱللَّهِ وَمَآ أُنزِلَ عَلَيْنَا وَمَآ أُنزِلَ عَلَىٰٓ إِبْرَٰهِيمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَمَآ أُوتِىَ مُوسَىٰ وَعِيسَىٰ وَٱلنَّبِيُّونَ مِن رَّبِّهِمْ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّنْهُمْ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (4:54) [listed for 87:19] أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۖ فَقَدْ ءَاتَيْنَآ ءَالَ إِبْرَٰهِيمَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَءَاتَيْنَٰهُم مُّلْكًا عَظِيمًۭا
- (4:125) [listed for 87:19] وَمَنْ أَحْسَنُ دِينًۭا مِّمَّنْ أَسْلَمَ وَجْهَهُۥ لِلَّهِ وَهُوَ مُحْسِنٌۭ وَٱتَّبَعَ مِلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۗ وَٱتَّخَذَ ٱللَّهُ إِبْرَٰهِيمَ خَلِيلًۭا
- (4:153) [listed for 87:19] يَسْـَٔلُكَ أَهْلُ ٱلْكِتَٰبِ أَن تُنَزِّلَ عَلَيْهِمْ كِتَٰبًۭا مِّنَ ٱلسَّمَآءِ ۚ فَقَدْ سَأَلُوا۟ مُوسَىٰٓ أَكْبَرَ مِن ذَٰلِكَ فَقَالُوٓا۟ أَرِنَا ٱللَّهَ جَهْرَةًۭ فَأَخَذَتْهُمُ ٱلصَّٰعِقَةُ بِظُلْمِهِمْ ۚ ثُمَّ ٱتَّخَذُوا۟ ٱلْعِجْلَ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ فَعَفَوْنَا عَن ذَٰلِكَ ۚ وَءَاتَيْنَا مُوسَىٰ سُلْطَٰنًۭا مُّبِينًۭا
- (7:150) [listed for 87:19] وَلَمَّا رَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا قَالَ بِئْسَمَا خَلَفْتُمُونِى مِنۢ بَعْدِىٓ ۖ أَعَجِلْتُمْ أَمْرَ رَبِّكُمْ ۖ وَأَلْقَى ٱلْأَلْوَاحَ وَأَخَذَ بِرَأْسِ أَخِيهِ يَجُرُّهُۥٓ إِلَيْهِ ۚ قَالَ ٱبْنَ أُمَّ إِنَّ ٱلْقَوْمَ ٱسْتَضْعَفُونِى وَكَادُوا۟ يَقْتُلُونَنِى فَلَا تُشْمِتْ بِىَ ٱلْأَعْدَآءَ وَلَا تَجْعَلْنِى مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (28:49) [listed for 87:19] قُلْ فَأْتُوا۟ بِكِتَٰبٍۢ مِّنْ عِندِ ٱللَّهِ هُوَ أَهْدَىٰ مِنْهُمَآ أَتَّبِعْهُ إِن كُنتُمْ صَٰدِقِينَ
- (29:27) [listed for 87:19] وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ وَجَعَلْنَا فِى ذُرِّيَّتِهِ ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ وَءَاتَيْنَٰهُ أَجْرَهُۥ فِى ٱلدُّنْيَا ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
- (37:117) [listed for 87:19] وَءَاتَيْنَٰهُمَا ٱلْكِتَٰبَ ٱلْمُسْتَبِينَ
- (40:53) [listed for 87:19] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْهُدَىٰ وَأَوْرَثْنَا بَنِىٓ إِسْرَٰٓءِيلَ ٱلْكِتَٰبَ
- (52:3) [listed for 87:19] فِى رَقٍّۢ مَّنشُورٍۢ
- (57:26) [listed for 87:19] وَلَقَدْ أَرْسَلْنَا نُوحًۭا وَإِبْرَٰهِيمَ وَجَعَلْنَا فِى ذُرِّيَّتِهِمَا ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ ۖ فَمِنْهُم مُّهْتَدٍۢ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (74:52) [listed for 87:19] [cited in ¶7] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
- (81:10) [listed for 87:19] [cited in ¶7] وَإِذَا ٱلصُّحُفُ نُشِرَتْ
- (98:2) [listed for 87:19] [cited in ¶10] رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- (98:3) [listed for 87:19] فِيهَا كُتُبٌۭ قَيِّمَةٌۭ

## named by the passage's own list as strong for this ayah (3)

- (3:3) [listed for 87:19] نَزَّلَ عَلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ وَأَنزَلَ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ
- (4:163) [listed for 87:19] ۞ إِنَّآ أَوْحَيْنَآ إِلَيْكَ كَمَآ أَوْحَيْنَآ إِلَىٰ نُوحٍۢ وَٱلنَّبِيِّۦنَ مِنۢ بَعْدِهِۦ ۚ وَأَوْحَيْنَآ إِلَىٰٓ إِبْرَٰهِيمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَعِيسَىٰ وَأَيُّوبَ وَيُونُسَ وَهَٰرُونَ وَسُلَيْمَٰنَ ۚ وَءَاتَيْنَا دَاوُۥدَ زَبُورًۭا
- (26:196) [listed for 87:19] وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ

## named by the passage's own list as medium for this ayah (17)

- (2:130) [listed for 87:19] وَمَن يَرْغَبُ عَن مِّلَّةِ إِبْرَٰهِۦمَ إِلَّا مَن سَفِهَ نَفْسَهُۥ ۚ وَلَقَدِ ٱصْطَفَيْنَٰهُ فِى ٱلدُّنْيَا ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
- (3:95) [listed for 87:19] قُلْ صَدَقَ ٱللَّهُ ۗ فَٱتَّبِعُوا۟ مِلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (4:162) [listed for 87:19] لَّٰكِنِ ٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ مِنْهُمْ وَٱلْمُؤْمِنُونَ يُؤْمِنُونَ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ ۚ وَٱلْمُقِيمِينَ ٱلصَّلَوٰةَ ۚ وَٱلْمُؤْتُونَ ٱلزَّكَوٰةَ وَٱلْمُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ أُو۟لَٰٓئِكَ سَنُؤْتِيهِمْ أَجْرًا عَظِيمًا
- (6:84) [listed for 87:19] وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ ۚ كُلًّا هَدَيْنَا ۚ وَنُوحًا هَدَيْنَا مِن قَبْلُ ۖ وَمِن ذُرِّيَّتِهِۦ دَاوُۥدَ وَسُلَيْمَٰنَ وَأَيُّوبَ وَيُوسُفَ وَمُوسَىٰ وَهَٰرُونَ ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُحْسِنِينَ
- (6:89) [listed for 87:19] أُو۟لَٰٓئِكَ ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ۚ فَإِن يَكْفُرْ بِهَا هَٰٓؤُلَآءِ فَقَدْ وَكَّلْنَا بِهَا قَوْمًۭا لَّيْسُوا۟ بِهَا بِكَٰفِرِينَ
- (6:90) [listed for 87:19] أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا ۖ إِنْ هُوَ إِلَّا ذِكْرَىٰ لِلْعَٰلَمِينَ
- (16:123) [listed for 87:19] ثُمَّ أَوْحَيْنَآ إِلَيْكَ أَنِ ٱتَّبِعْ مِلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۖ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (19:41) [listed for 87:19] وَٱذْكُرْ فِى ٱلْكِتَٰبِ إِبْرَٰهِيمَ ۚ إِنَّهُۥ كَانَ صِدِّيقًۭا نَّبِيًّا
- (19:50) [listed for 87:19] وَوَهَبْنَا لَهُم مِّن رَّحْمَتِنَا وَجَعَلْنَا لَهُمْ لِسَانَ صِدْقٍ عَلِيًّۭا
- (19:51) [listed for 87:19] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مُوسَىٰٓ ۚ إِنَّهُۥ كَانَ مُخْلَصًۭا وَكَانَ رَسُولًۭا نَّبِيًّۭا
- (19:56) [listed for 87:19] وَٱذْكُرْ فِى ٱلْكِتَٰبِ إِدْرِيسَ ۚ إِنَّهُۥ كَانَ صِدِّيقًۭا نَّبِيًّۭا
- (37:83) [listed for 87:19] ۞ وَإِنَّ مِن شِيعَتِهِۦ لَإِبْرَٰهِيمَ
- (37:114) [listed for 87:19] وَلَقَدْ مَنَنَّا عَلَىٰ مُوسَىٰ وَهَٰرُونَ
- (38:45) [listed for 87:19] وَٱذْكُرْ عِبَٰدَنَآ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ أُو۟لِى ٱلْأَيْدِى وَٱلْأَبْصَٰرِ
- (52:2) [listed for 87:19] وَكِتَٰبٍۢ مَّسْطُورٍۢ
- (68:1) [listed for 87:19] نٓ ۚ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ
- (85:22) [listed for 87:19] فِى لَوْحٍۢ مَّحْفُوظٍۭ

## weak (this ayah's own list) (13)

- (2:200) [listed for 87:19] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
- (2:220) [listed for 87:19] فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۗ وَيَسْـَٔلُونَكَ عَنِ ٱلْيَتَٰمَىٰ ۖ قُلْ إِصْلَاحٌۭ لَّهُمْ خَيْرٌۭ ۖ وَإِن تُخَالِطُوهُمْ فَإِخْوَٰنُكُمْ ۚ وَٱللَّهُ يَعْلَمُ ٱلْمُفْسِدَ مِنَ ٱلْمُصْلِحِ ۚ وَلَوْ شَآءَ ٱللَّهُ لَأَعْنَتَكُمْ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (3:33) [listed for 87:19] ۞ إِنَّ ٱللَّهَ ٱصْطَفَىٰٓ ءَادَمَ وَنُوحًۭا وَءَالَ إِبْرَٰهِيمَ وَءَالَ عِمْرَٰنَ عَلَى ٱلْعَٰلَمِينَ
- (3:67) [listed for 87:19] مَا كَانَ إِبْرَٰهِيمُ يَهُودِيًّۭا وَلَا نَصْرَانِيًّۭا وَلَٰكِن كَانَ حَنِيفًۭا مُّسْلِمًۭا وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (5:41) [listed for 87:19] ۞ يَٰٓأَيُّهَا ٱلرَّسُولُ لَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ مِنَ ٱلَّذِينَ قَالُوٓا۟ ءَامَنَّا بِأَفْوَٰهِهِمْ وَلَمْ تُؤْمِن قُلُوبُهُمْ ۛ وَمِنَ ٱلَّذِينَ هَادُوا۟ ۛ سَمَّٰعُونَ لِلْكَذِبِ سَمَّٰعُونَ لِقَوْمٍ ءَاخَرِينَ لَمْ يَأْتُوكَ ۖ يُحَرِّفُونَ ٱلْكَلِمَ مِنۢ بَعْدِ مَوَاضِعِهِۦ ۖ يَقُولُونَ إِنْ أُوتِيتُمْ هَٰذَا فَخُذُوهُ وَإِن لَّمْ تُؤْتَوْهُ فَٱحْذَرُوا۟ ۚ وَمَن يُرِدِ ٱللَّهُ فِتْنَتَهُۥ فَلَن تَمْلِكَ لَهُۥ مِنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ لَمْ يُرِدِ ٱللَّهُ أَن يُطَهِّرَ قُلُوبَهُمْ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (6:161) [listed for 87:19] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (16:120) [listed for 87:19] إِنَّ إِبْرَٰهِيمَ كَانَ أُمَّةًۭ قَانِتًۭا لِّلَّهِ حَنِيفًۭا وَلَمْ يَكُ مِنَ ٱلْمُشْرِكِينَ
- (26:69) [listed for 87:19] وَٱتْلُ عَلَيْهِمْ نَبَأَ إِبْرَٰهِيمَ
- (50:8) [listed for 87:19] تَبْصِرَةًۭ وَذِكْرَىٰ لِكُلِّ عَبْدٍۢ مُّنِيبٍۢ
- (82:11) [listed for 87:19] كِرَامًۭا كَٰتِبِينَ
- (83:9) [listed for 87:19] كِتَٰبٌۭ مَّرْقُومٌۭ
- (83:20) [listed for 87:19] كِتَٰبٌۭ مَّرْقُومٌۭ
- (90:9) [listed for 87:19] وَلِسَانًۭا وَشَفَتَيْنِ

## named by the passage's own list as weak for this ayah (18)

- (6:75) [listed for 87:19] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (7:122) [listed for 87:19] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (7:144) [listed for 87:19] قَالَ يَٰمُوسَىٰٓ إِنِّى ٱصْطَفَيْتُكَ عَلَى ٱلنَّاسِ بِرِسَٰلَٰتِى وَبِكَلَٰمِى فَخُذْ مَآ ءَاتَيْتُكَ وَكُن مِّنَ ٱلشَّٰكِرِينَ
- (11:75) [listed for 87:19] إِنَّ إِبْرَٰهِيمَ لَحَلِيمٌ أَوَّٰهٌۭ مُّنِيبٌۭ
- (20:1) [listed for 87:19] طه
- (20:70) [listed for 87:19] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (21:51) [listed for 87:19] ۞ وَلَقَدْ ءَاتَيْنَآ إِبْرَٰهِيمَ رُشْدَهُۥ مِن قَبْلُ وَكُنَّا بِهِۦ عَٰلِمِينَ
- (21:69) [listed for 87:19] قُلْنَا يَٰنَارُ كُونِى بَرْدًۭا وَسَلَٰمًا عَلَىٰٓ إِبْرَٰهِيمَ
- (21:72) [listed for 87:19] وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ نَافِلَةًۭ ۖ وَكُلًّۭا جَعَلْنَا صَٰلِحِينَ
- (22:43) [listed for 87:19] وَقَوْمُ إِبْرَٰهِيمَ وَقَوْمُ لُوطٍۢ
- (26:48) [listed for 87:19] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (29:31) [listed for 87:19] وَلَمَّا جَآءَتْ رُسُلُنَآ إِبْرَٰهِيمَ بِٱلْبُشْرَىٰ قَالُوٓا۟ إِنَّا مُهْلِكُوٓا۟ أَهْلِ هَٰذِهِ ٱلْقَرْيَةِ ۖ إِنَّ أَهْلَهَا كَانُوا۟ ظَٰلِمِينَ
- (37:109) [listed for 87:19] سَلَٰمٌ عَلَىٰٓ إِبْرَٰهِيمَ
- (37:113) [listed for 87:19] وَبَٰرَكْنَا عَلَيْهِ وَعَلَىٰٓ إِسْحَٰقَ ۚ وَمِن ذُرِّيَّتِهِمَا مُحْسِنٌۭ وَظَالِمٌۭ لِّنَفْسِهِۦ مُبِينٌۭ
- (37:120) [listed for 87:19] سَلَٰمٌ عَلَىٰ مُوسَىٰ وَهَٰرُونَ
- (40:54) [listed for 87:19] هُدًۭى وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (51:24) [listed for 87:19] هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ
- (56:78) [listed for 87:19] فِى كِتَٰبٍۢ مَّكْنُونٍۢ

## neighbours: within two ayat of a passage the commentary cites (76)

- (1:4) [next to 1:6] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (1:5) [next to 1:6] إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- (1:7) [next to 1:6] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- (2:127) [next to 2:129] وَإِذْ يَرْفَعُ إِبْرَٰهِۦمُ ٱلْقَوَاعِدَ مِنَ ٱلْبَيْتِ وَإِسْمَٰعِيلُ رَبَّنَا تَقَبَّلْ مِنَّآ ۖ إِنَّكَ أَنتَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (2:128) [next to 2:129] رَبَّنَا وَٱجْعَلْنَا مُسْلِمَيْنِ لَكَ وَمِن ذُرِّيَّتِنَآ أُمَّةًۭ مُّسْلِمَةًۭ لَّكَ وَأَرِنَا مَنَاسِكَنَا وَتُبْ عَلَيْنَآ ۖ إِنَّكَ أَنتَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:131) [next to 2:129] إِذْ قَالَ لَهُۥ رَبُّهُۥٓ أَسْلِمْ ۖ قَالَ أَسْلَمْتُ لِرَبِّ ٱلْعَٰلَمِينَ
- (2:256) [next to 2:258] لَآ إِكْرَاهَ فِى ٱلدِّينِ ۖ قَد تَّبَيَّنَ ٱلرُّشْدُ مِنَ ٱلْغَىِّ ۚ فَمَن يَكْفُرْ بِٱلطَّٰغُوتِ وَيُؤْمِنۢ بِٱللَّهِ فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ لَا ٱنفِصَامَ لَهَا ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
- (2:257) [next to 2:258] ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۖ وَٱلَّذِينَ كَفَرُوٓا۟ أَوْلِيَآؤُهُمُ ٱلطَّٰغُوتُ يُخْرِجُونَهُم مِّنَ ٱلنُّورِ إِلَى ٱلظُّلُمَٰتِ ۗ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:259) [next to 2:258] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (2:260) [next to 2:258] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ أَرِنِى كَيْفَ تُحْىِ ٱلْمَوْتَىٰ ۖ قَالَ أَوَلَمْ تُؤْمِن ۖ قَالَ بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِى ۖ قَالَ فَخُذْ أَرْبَعَةًۭ مِّنَ ٱلطَّيْرِ فَصُرْهُنَّ إِلَيْكَ ثُمَّ ٱجْعَلْ عَلَىٰ كُلِّ جَبَلٍۢ مِّنْهُنَّ جُزْءًۭا ثُمَّ ٱدْعُهُنَّ يَأْتِينَكَ سَعْيًۭا ۚ وَٱعْلَمْ أَنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (6:74) [next to 6:76] ۞ وَإِذْ قَالَ إِبْرَٰهِيمُ لِأَبِيهِ ءَازَرَ أَتَتَّخِذُ أَصْنَامًا ءَالِهَةً ۖ إِنِّىٓ أَرَىٰكَ وَقَوْمَكَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (6:78) [next to 6:76] فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ ۖ فَلَمَّآ أَفَلَتْ قَالَ يَٰقَوْمِ إِنِّى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:79) [next to 6:77] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (14:38) [next to 14:40] رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (14:39) [next to 14:40] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى وَهَبَ لِى عَلَى ٱلْكِبَرِ إِسْمَٰعِيلَ وَإِسْحَٰقَ ۚ إِنَّ رَبِّى لَسَمِيعُ ٱلدُّعَآءِ
- (14:41) [next to 14:40] رَبَّنَا ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ ٱلْحِسَابُ
- (14:42) [next to 14:40] وَلَا تَحْسَبَنَّ ٱللَّهَ غَٰفِلًا عَمَّا يَعْمَلُ ٱلظَّٰلِمُونَ ۚ إِنَّمَا يُؤَخِّرُهُمْ لِيَوْمٍۢ تَشْخَصُ فِيهِ ٱلْأَبْصَٰرُ
- (20:40) [next to 20:42] إِذْ تَمْشِىٓ أُخْتُكَ فَتَقُولُ هَلْ أَدُلُّكُمْ عَلَىٰ مَن يَكْفُلُهُۥ ۖ فَرَجَعْنَٰكَ إِلَىٰٓ أُمِّكَ كَىْ تَقَرَّ عَيْنُهَا وَلَا تَحْزَنَ ۚ وَقَتَلْتَ نَفْسًۭا فَنَجَّيْنَٰكَ مِنَ ٱلْغَمِّ وَفَتَنَّٰكَ فُتُونًۭا ۚ فَلَبِثْتَ سِنِينَ فِىٓ أَهْلِ مَدْيَنَ ثُمَّ جِئْتَ عَلَىٰ قَدَرٍۢ يَٰمُوسَىٰ
- (20:41) [next to 20:42] وَٱصْطَنَعْتُكَ لِنَفْسِى
- (20:43) [next to 20:42] ٱذْهَبَآ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (20:45) [next to 20:44] قَالَا رَبَّنَآ إِنَّنَا نَخَافُ أَن يَفْرُطَ عَلَيْنَآ أَوْ أَن يَطْغَىٰ
- (20:46) [next to 20:44] قَالَ لَا تَخَافَآ ۖ إِنَّنِى مَعَكُمَآ أَسْمَعُ وَأَرَىٰ
- (20:47) [next to 20:49] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
- (20:48) [next to 20:49] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:55) [next to 20:53] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
- (20:56) [next to 20:54] وَلَقَدْ أَرَيْنَٰهُ ءَايَٰتِنَا كُلَّهَا فَكَذَّبَ وَأَبَىٰ
- (20:71) [next to 20:72] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (20:74) [next to 20:72] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:75) [next to 20:73] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (20:131) [next to 20:133] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
- (20:132) [next to 20:133] وَأْمُرْ أَهْلَكَ بِٱلصَّلَوٰةِ وَٱصْطَبِرْ عَلَيْهَا ۖ لَا نَسْـَٔلُكَ رِزْقًۭا ۖ نَّحْنُ نَرْزُقُكَ ۗ وَٱلْعَٰقِبَةُ لِلتَّقْوَىٰ
- (20:134) [next to 20:133] وَلَوْ أَنَّآ أَهْلَكْنَٰهُم بِعَذَابٍۢ مِّن قَبْلِهِۦ لَقَالُوا۟ رَبَّنَا لَوْلَآ أَرْسَلْتَ إِلَيْنَا رَسُولًۭا فَنَتَّبِعَ ءَايَٰتِكَ مِن قَبْلِ أَن نَّذِلَّ وَنَخْزَىٰ
- (20:135) [next to 20:133] قُلْ كُلٌّۭ مُّتَرَبِّصٌۭ فَتَرَبَّصُوا۟ ۖ فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ
- (26:71) [next to 26:73] قَالُوا۟ نَعْبُدُ أَصْنَامًۭا فَنَظَلُّ لَهَا عَٰكِفِينَ
- (26:72) [next to 26:73] قَالَ هَلْ يَسْمَعُونَكُمْ إِذْ تَدْعُونَ
- (26:75) [next to 26:73] قَالَ أَفَرَءَيْتُم مَّا كُنتُمْ تَعْبُدُونَ
- (26:77) [next to 26:76] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
- (26:79) [next to 26:78] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (26:80) [next to 26:78] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (26:82) [next to 26:81] وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ
- (26:83) [next to 26:81] رَبِّ هَبْ لِى حُكْمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (26:85) [next to 26:84] وَٱجْعَلْنِى مِن وَرَثَةِ جَنَّةِ ٱلنَّعِيمِ
- (26:86) [next to 26:84] وَٱغْفِرْ لِأَبِىٓ إِنَّهُۥ كَانَ مِنَ ٱلضَّآلِّينَ
- (29:46) [next to 29:48] ۞ وَلَا تُجَٰدِلُوٓا۟ أَهْلَ ٱلْكِتَٰبِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ ۖ وَقُولُوٓا۟ ءَامَنَّا بِٱلَّذِىٓ أُنزِلَ إِلَيْنَا وَأُنزِلَ إِلَيْكُمْ وَإِلَٰهُنَا وَإِلَٰهُكُمْ وَٰحِدٌۭ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (29:47) [next to 29:48] وَكَذَٰلِكَ أَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ ۚ فَٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يُؤْمِنُونَ بِهِۦ ۖ وَمِنْ هَٰٓؤُلَآءِ مَن يُؤْمِنُ بِهِۦ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلْكَٰفِرُونَ
- (29:49) [next to 29:48] بَلْ هُوَ ءَايَٰتٌۢ بَيِّنَٰتٌۭ فِى صُدُورِ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلظَّٰلِمُونَ
- (29:50) [next to 29:48] وَقَالُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَٰتٌۭ مِّن رَّبِّهِۦ ۖ قُلْ إِنَّمَا ٱلْءَايَٰتُ عِندَ ٱللَّهِ وَإِنَّمَآ أَنَا۠ نَذِيرٌۭ مُّبِينٌ
- (53:33) [next to 53:35] أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ
- (53:34) [next to 53:35] وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ
- (74:48) [next to 74:50] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
- (74:49) [next to 74:50] فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ
- (74:51) [next to 74:50] فَرَّتْ مِن قَسْوَرَةٍۭ
- (74:53) [next to 74:52] كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ
- (74:54) [next to 74:52] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
- (79:16) [next to 79:18] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- (79:17) [next to 79:18] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (79:21) [next to 79:19] فَكَذَّبَ وَعَصَىٰ
- (79:22) [next to 79:20] ثُمَّ أَدْبَرَ يَسْعَىٰ
- (79:23) [next to 79:24] فَحَشَرَ فَنَادَىٰ
- (79:27) [next to 79:25] ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا
- (79:28) [next to 79:26] رَفَعَ سَمْكَهَا فَسَوَّىٰهَا
- (81:8) [next to 81:10] وَإِذَا ٱلْمَوْءُۥدَةُ سُئِلَتْ
- (81:9) [next to 81:10] بِأَىِّ ذَنۢبٍۢ قُتِلَتْ
- (81:11) [next to 81:10] وَإِذَا ٱلسَّمَآءُ كُشِطَتْ
- (81:12) [next to 81:10] وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ
- (92:10) [next to 92:12] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:11) [next to 92:12] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (92:14) [next to 92:12] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:15) [next to 92:13] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (93:2) [next to 93:4] وَٱلَّيْلِ إِذَا سَجَىٰ
- (93:3) [next to 93:4] مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ
- (93:5) [next to 93:4] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (93:6) [next to 93:4] أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ
- (98:0) [next to 98:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (98:1) [next to 98:2] لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- (98:4) [next to 98:2] وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ

