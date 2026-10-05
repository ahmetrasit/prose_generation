Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:17; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_17/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_17.reading.tr.md (prose paragraphs numbered) =====
## Tercihin yanına konan cümle

[¶1] On altıncı ayet, önceki ayetlerde "o" diye anılan insanlardan birden "siz"e döner: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır, siz yakın hayatı öne alıyorsunuz, source:87:16}. Odak ayet bu sözün hemen ardından bir "ve" ile gelir ve hiçbir fiil taşımaz: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa sonraki hayat daha hayırlı ve daha kalıcıdır, source:87:17}. Buradaki "ve" yeni bir konu açmaz. Tercihin yapıldığı anda orada duran bir durumu tercihin yanına koyar. Cümle şöyle işler: siz yakını öne alıyorsunuz, oysa öteki o sırada da daha iyidir. Kınanan şey bilmeden yapılmış bir seçim değildir. Daha iyisi göz önündeyken yapılmış bir seçimdir.

[¶2] Ayetin öznesi aslında bir sıfattır. On altıncı ayette "hayat" kelimesi "yakın" sıfatıyla gelmişti. On yedinci ayette aynı kelime söylenmez, yalnızca sıfatı kalır: "sonraki". Düşen isim açıkça söylendiğinde şöyle tamamlanır: {ar:تقدير الإضافة دار الحياة الآخرة, tr:takdîru'l-idâfeti dâru'l-hayâti'l-âhira, gloss:tamlamanın açık hali: sonraki hayatın yurdu, source:"ء خ ر,B004"}. Bu sonraki hayat başka bir yerde {ar:يعبر بالدار الآخرة عن النشأة الثانية, tr:yu'abbaru bi'd-dâri'l-âhirati ani'n-neş'eti's-ŝâniye, gloss:"sonraki yurt" ikinci yaratılışı anlatır, source:"ء خ ر,B004"} diye açıklanır. Yani iki ayet birbirinden kopuk iki şeyden söz etmez. Aynı hayatın iki bölümünü anlatır: yakın olanı ve sonra geleni.

[¶3] Ayetin iki yüklemi de karşılaştırmadır. Arapçada "daha …" anlamı çoğunlukla أبقى kelimesindeki gibi başında e- bulunan bir kalıpla kurulur. خير ise bu kalıba girmeden aynı işi görür, hem "iyi" hem "daha iyi" olabilir. Karşılaştırmanın öbür ucu söylenmez, çünkü bir önceki ayette zaten durmaktadır. Burada küçük ama önemli bir ayrıntı var: karşılaştırma, karşılaştırılan şeye bir pay tanır. "Daha hayırlı" diyen, yakın hayatta da hayır olduğunu kabul eder. "Daha kalıcı" diyen de onun bir süre kaldığını kabul eder. Ayet yakın hayata "boştur" demez, onu ikinci sıraya koyar. Hata değersiz bir şeyi sevmek değildir, sıralamayı ters kurmaktır.

[¶4] Sure baştan sona sıralama diliyle konuşur. Rab {ar:ٱلْأَعْلَى, tr:el-a'lâ, gloss:en yüce, source:87:1} diye anılır. Sekizinci ayette {ar:لِلْيُسْرَىٰ, tr:li'l-yusrâ, gloss:en kolay olana, source:87:8} ifadesi geçer. On birinci ayette {ar:ٱلْأَشْقَى, tr:el-eşkâ, gloss:en bedbaht olan, source:87:11}, on ikinci ayette {ar:ٱلنَّارَ ٱلْكُبْرَىٰ, tr:en-nâra'l-kubrâ, gloss:en büyük ateş, source:87:12} vardır. On sekizinci ayet de sayfaları {ar:ٱلْأُولَىٰ, tr:el-ûlâ, gloss:ilk, source:87:18} diye niteler. On altıncı ayetin "dünya" kelimesi de bu türdendir ve "daha yakın olan" demektir. Bu kelimelerin her biri bir şeyi başka şeyler arasında bir basamağa yerleştirir. On yedinci ayet ise bu dilin iki şeyi açıkça tartıp birini öbürünün üstüne koyduğu tek yerdir. Surenin sıralama alışkanlığı burada bir hükme dönüşür.

## "Ahiret" kelimesinin unuttuğu yön

[¶5] Türkçede "ahiret" yalnızca öbür dünyanın adıdır. Kelimede bir yön ya da bir sıra duyulmaz. Arapçada الآخرة önce sıradan bir sıfattır: sonra gelen, arkada kalan. Bundan sonra anılacak kelime resimleri ayetteki anlamın yerine geçmez, onun yanında duyulur. Ayet yine "ahiret" der, ama Arapça bilen kulak kelimenin gündelik kullanımlarını da işitir. Kökün temeli öne geçenin karşıtıdır: {ar:الآخر نقيض المتقدم, tr:el-âhiru nakîdu'l-mutekaddim, gloss:âhir, öne geçenin karşıtıdır, source:"ء خ ر,B001"}. Yürüyen bir topluluğun en gerisinde kalanlar bu kelimeyle anılırdı: {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun uhrâsı, en arkada olanlarıdır, source:"ء خ ر,B001"}. Deve semerinin iki ucunda yükselen birer tahta vardır. Öndekine kâdime, arkadakine âhira denirdi: {ar:آخرة الرحل وقادمته, tr:âhiratu'r-rahli ve kâdimetuh, gloss:semerin arka tahtası ve ön tahtası, source:"ء خ ر,B003"}. Binici bu ikisinin arasında oturur. Öndeki tahta gidilen yöne, arkadaki geride kalan yola bakar.

[¶6] Karşısındaki kelime de bir uzaklık ölçüsüdür: {ar:سميت الدنيا لدنوها, tr:summiyeti'd-dunyâ li-dunuvvihâ, gloss:dünya, yakınlığından dolayı bu adı almıştır, source:"د ن و,B002"}. "Dünya ve ahiret" Arapçada aslında "yakın olan ve sonra gelen" demektir. Biri mesafeyle, öbürü sırayla ölçülür ve ikisi de dinleyenin şu an durduğu yerden ölçülür. Yakın hayat yakındır çünkü onun içindeyiz. Sonraki hayat sonradır çünkü onun ardından gelir. Kelimelerin hiçbiri "bu âlem" ile "öbür âlem" diye iki ayrı ülkeyi anlatmaz. Türkçe kullanım onları iki ayrı diyara ayırmıştır, Arapça ise aynı yolun iki uzunluğu olarak tutar.

[¶7] Kur'an "sonraki" kelimesini bazen "yakın" ile değil, "ilk" ile eşler. Bir surede Allah önce kuşluk vaktine ve sükûna eren geceye yemin eder, sonra Peygamber'e {ar:مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ, tr:mâ vedde'ake rabbuke ve mâ kalâ, gloss:Rabbin seni bırakmadı, sana darılmadı da, source:93:3} der. Ardından odak ayetin cümlesinin, karşılaştırmanın öbür ucu da söylenmiş halini getirir: {ar:وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ, tr:ve le'l-âhiratu hayrun leke mine'l-ûlâ, gloss:sonraki senin için ilkinden elbette daha hayırlıdır, source:93:4}. Hemen arkasından da {ar:وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ, tr:ve le-sevfe yu'tîke rabbuke fe-terdâ, gloss:Rabbin sana verecek, sen de hoşnut olacaksın, source:93:5} gelir. Özne aynıdır, yüklem aynıdır. Burada kelimenin sıra anlamı o kadar canlıdır ki "sonraki" hem ölümden sonraki hayat olarak hem de bir ömrün sonraki bölümü olarak duyulabilir. Başka bir yerde Allah {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek elbette bize düşer, source:92:12} dedikten sonra {ar:وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ, tr:ve inne lenâ le'l-âhirate ve'l-ûlâ, gloss:sonraki de ilk de elbette bizimdir, source:92:13} der. Bir başka yerde, insanın her dilediğine sahip olup olmadığı sorulduktan sonra {ar:فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ, tr:fe-lillâhi'l-âhiratu ve'l-ûlâ, gloss:sonraki de ilk de Allah'ındır, source:53:25} denir. Bizim surede de "sonraki" kelimesinden hemen sonra "ilk" gelir: bu söz ilk sayfalarda yazılıdır. Sonra gelenin haberi en baştan beri verilmiştir.

[¶8] Surede bu ön ile arka sırası bir koşuya da dönüşür. O sahneyi on beşinci ve on altıncı ayetlerin kelimeleri kurar: öndekinin ardından gelen at ve birinin izinden gitmek.

## Vadeye bırakılan, sona kalan

[¶9] Aynı kök ertelemeyi de anlatır. Araplar veresiye satış için şöyle derlerdi: {ar:بعته بأخرة وبنظرة أي بنسيئة, tr:bi'tuhû bi-ehiratin ve bi-nazıratin ey bi-nesîe, gloss:onu vadeyle, mühletle sattım, source:"ء خ ر,B002"}. Böyle bir satışta alıcı malı hemen alır, bedeli belirli bir süre sonra öder. Satıcı da elindekini bugün verip karşılığını sonraya bırakmayı kabul etmiş olur. "Sonraki hayat" kelimesinin yanında bu çarşı dili de duyulur. Ahiret, peşin ödenmeyen bedeldir. Yakını öne alan, vadeli büyük bir bedel yerine eline hemen geçecek küçük bir bedeli seçen satıcıya benzer.

[¶10] Kur'an bu peşin ile vadeli karşıtlığını başka bir kelimeyle de kurar ve bu kez sahne şaşırtıcı biçimde bizim sureye benzer. Allah Peygamber'e vahyi aceleyle tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleye getirmek için dilini kıpırdatma, source:75:16}. Ardından {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak ve okutmak bize düşer, source:75:17} der. Birkaç ayet sonra da insanlara döner: {ar:كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ, tr:kellâ bel tuhibbûne'l-âcile, gloss:hayır, siz hemen geleni seviyorsunuz, source:75:20}, {ar:وَتَذَرُونَ ٱلْءَاخِرَةَ, tr:ve teẕerûne'l-âhira, gloss:sonraki olanı da bırakıyorsunuz, source:75:21}. Bizim surede de önce Peygamber'e güvence verilir: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Sonra aynı "hayır, siz…" kalıbıyla yakını öne alanlar kınanır. İki surede de aynı sıra vardır: Peygamber'e sözün kendisi için acele etmemesi, çünkü sonrasının güvence altında olduğu öğretilir. İnsanlar ise hemen elde edileni kapıp sonra geleni bırakmakla kınanır. Kur'an başka bir yerde iki isteği yan yana tartar: {ar:مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ, tr:men kâne yurîdu'l-âcilete accelnâ lehû fîhâ mâ neşâu li-men nurîd, gloss:kim hemen geleni isterse, dilediğimize dilediğimizi orada hemen veririz, source:17:18}. Öbürü için de {ar:وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ, tr:ve men erâde'l-âhirate ve se'â lehâ sa'yehâ ve huve mu'min, gloss:kim de iman ederek sonrakini ister ve onun hakkını vererek onun için çalışırsa, source:17:19} der. Peşin alan bile istediğini değil, "dilediğimizi" alır. Kendilerinden alınan ahdi bozanlar anlatılırken de çarşı dili açıkça kullanılır: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ, tr:ulâike'lleẕîne'şteravu'l-hayâte'd-dunyâ bi'l-âhira, gloss:onlar yakın hayatı sonrakine karşılık satın alanlardır, source:2:86}.

[¶11] Kökün bir kelimesi de sonraya kalmanın, kalıcı olmaya bitişik olduğunu gösterir. Bir tür hurma ağacına mi'hâr denirdi: {ar:المئخار النخلة التي يبقى حملها إلى آخر الصرام, tr:el-mi'hâr en-nahletu'lletî yebkâ hamluhâ ilâ âhiri's-sırâm, gloss:mi'hâr, meyvesi hurma kesiminin sonuna dek dalında kalan ağaçtır, source:"ء خ ر,B002"}. Hurma kesiminde olgunlaşan salkımlar kesilip toplanır. Çoğu ağaç erken boşalır. Bu ağaç ise yükünü en sona kadar taşır. Adını "sonra" kökünden alır, ama onu tarif eden cümle on yedinci ayetin ikinci kelimesinin fiiliyle kurulur: yükü kalan. İki kök ayrıdır ve birbirinden türemez. Onları bir araya getiren, konuşanların bu ağacı anlatırken kendiliğinden "kalmak" fiiline uzanmasıdır. Geç toplanan, dalda uzun kalandır. Ayet sonraki hayat için aynı şeyi söyler: o hem sonradır hem kalıcıdır, ve bu iki nitelik birbirinden ayrılmaz.

[¶12] "Kalıcı" kelimesinin kökünde koşuya dair bir ad da vardır: {ar:المبقيات من الخيل التي تبقي بعض جريها تدخره, tr:el-mubkıyâtu mine'l-hayli elletî tubkî ba'da cerihâ teddehıruh, gloss:mubkıyât, koşusunun bir kısmını geri tutup biriktiren atlardır, source:"ب ق ي,B004"}. Böyle bir at bütün hızını ilk anda harcamaz, bir kısmını yolun sonuna saklar. Yakını öne almak, koşunun tamamını ilk düzlükte tüketmektir. Aynı kökte hesap dilinden bir kelime daha var: {ar:الباقي حاصل الخراج ونحوه, tr:el-bâkî hâsılu'l-harâci ve nahvuh, gloss:bâkî, hasılattan ve benzerinden geriye kalan tutardır, source:"ب ق ي,B002"}. On dördüncü ayetin "kurtuldu" fiili toprağı yarmaktan gelir ve o ayetin tarla sahnesi hasılattan geriye kalanı adlandıran bu kelimede tamamlanır.

[¶13] Ertelemenin değerini bazıları geç anlar. Araplar {ar:ما عرفته إلا بأخرة, tr:mâ araftuhû illâ bi-ehira, gloss:onu ancak sonradan, geç tanıdım, source:"ء خ ر,B002"} derlerdi. Kur'an bu geç tanımanın sahnesini gösterir. Allah Peygamber'e, insanları azabın geleceği günle uyarmasını söyler. O gün haksızlık edenler {ar:رَبَّنَآ أَخِّرْنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ نُّجِبْ دَعْوَتَكَ, tr:rabbenâ ahhirnâ ilâ ecelin karîbin nucib da'veteke, gloss:Rabbimiz, bizi yakın bir süreye kadar ertele de çağrına uyalım, source:14:44} derler. Bir zamanlar küçümsedikleri erteleme şimdi diledikleri şey olmuştur, üstelik "yakın" bir erteleme. Aynı ayette cevap gelir: {ar:أَوَلَمْ تَكُونُوٓا۟ أَقْسَمْتُم مِّن قَبْلُ مَا لَكُم مِّن زَوَالٍۢ, tr:e-ve lem tekûnû aksemtum min kablu mâ lekum min zevâl, gloss:siz daha önce, sizin için hiçbir yok oluş olmadığına yemin etmemiş miydiniz, source:14:44}. Yakını öne alanlar ona kalıcılık da yakıştırmıştı. On yedinci ayetin kalıcılık kelimesi, yakın olanın elinden işte bu sahte payı alır.

## Hayır: seçenin aradığı şey

[¶14] Türkçede "hayır" iyilik ve hayır işi anlamında yaşar. Ama aynı kökten gelen "muhtar" kelimesinin aslında "seçilmiş" demek olduğu artık pek hissedilmez. Arapçada bu bağ canlıdır. Önce hayır, herkesin yöneldiği şeydir: {ar:فالخير خلاف الشر لأن كل أحد يميل إليه, tr:fe'l-hayru hilâfu'ş-şerri li-enne kulle ehadin yemîlu ileyh, gloss:hayır kötülüğün karşıtıdır, çünkü herkes ona meyleder, source:"خ ي ر,B001"}. Seçmek fiili de bu kelimenin üstüne kurulur: {ar:الاختيار طلب ما هو خير وفعله, tr:el-ihtiyâru talebu mâ huve hayrun ve fi'luh, gloss:seçmek, daha hayırlı olanı arayıp onu yapmaktır, source:"خ ي ر,B003"}. On altıncı ayetin fiili ise öne koymak, öncelik tanımaktır: {ar:له أصل تقديم الشيء, tr:lehû aslu takdîmi'ş-şey', gloss:bir şeyi öne koyma anlamına dayanır, source:"ء ث ر,B001"}. Böylece iki ayet arasında bir karşılıklı konuşma kurulur. Biri "öne alıyorsunuz" der. Öbürü, öne alınmayı hak eden şeyi seçmenin aradığı şeyin adıyla anar. Ayet tercihin kendisini kınamaz. Herkesin hayra meylettiğini bilir ve o meyli doğru hedefe çevirir.

[¶15] Seçilen şey ayıklanmış şeydir. Bir sürü hakkında {ar:فيهن مختارات لا رذل فيهن, tr:fîhinne muhtârâtun lâ reẕle fîhinn, gloss:aralarında seçkinler var, döküntü yok, source:"خ ي ر,B002"} denirdi. Surede bu ayıklama, beşinci ayetin döküntü kelimesi ile on altıncı ayetin "yakın" kelimesinin değersiz anlamı karşı kefeye konarak bir seçim sahnesine dönüşür.

[¶16] Kur'an yakın hayatın mallarına da hayır der ve bu ayeti duymak için bu önemlidir. Allah, insanın Rabbine karşı nankör olduğunu söyledikten sonra {ar:وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ, tr:ve innehû li-hubbi'l-hayri le-şedîd, gloss:o, mal sevgisinde gerçekten pek şiddetlidir, source:100:8} der. Ölümü yaklaşan kişiye de {ar:إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ, tr:in terake hayran el-vasiyye, gloss:geride mal bırakacaksa vasiyet etmesi, source:2:180} yazılmıştır. Ama mala her zaman hayır denmez: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne keŝîran ve min mekânin tayyib, gloss:mal bol olmadıkça ve temiz bir yerden gelmedikçe ona hayır denmez, source:"خ ي ر,B004"}. Odak ayetin "daha hayırlı" sözü bu gerçek hayrın üstüne konur. Sonraki hayat, insanın şiddetle sevdiği hayırdan da daha hayırlıdır. Ölüm anındaki ayet bir şeyi daha gösterir: yakın hayatın hayrı "bırakılan" hayırdır. Sahibi gider, mal burada kalır. Ayetin ikinci kelimesi tam bu noktada devreye girer.

[¶17] "Daha hayırlı ve daha kalıcı" ikilisi Kur'an'da kalıplaşmış bir sözdür ve her geçtiği yerde Allah'ı ya da O'nun katında olanı anlatır. Musa'nın karşısındaki sihirbazlar secdeye kapanınca Firavun onları el ve ayaklarını çaprazlama kesmekle tehdit eder. Sonra da {ar:وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ, tr:ve le-ta'lemunne eyyunâ eşeddu azâben ve ebkâ, gloss:hangimizin azabı daha çetin ve daha kalıcıymış, göreceksiniz, source:20:71} der ve kalıcılığı kendine mal eder. Sihirbazlar on altıncı ayetin fiilini olumsuz söyleyerek cevap verir: {ar:لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا, tr:len nu'ŝirake alâ mâ câenâ mine'l-beyyinâti ve'lleẕî feteranâ, gloss:seni, bize gelen açık delillere ve bizi yaratana asla tercih etmeyiz, source:20:72}. Sözlerini de {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:va'llâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} diye bitirirler. Bu sahne surenin on üçüncü ve on dördüncü ayetlerinin kelimelerini de taşır, çünkü sihirbazlar hemen ardından ne ölünüp ne yaşanan yeri ve arınanın karşılığını anarlar. Aynı surenin ilerisinde Allah Peygamber'e, söylenenlere sabretmesini ve güneş doğmadan önce ve batmadan önce Rabbini hamd ile tesbih etmesini söyler {source:20:130}. Ardından şöyle der: {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temuddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhum zehrate'l-hayâti'd-dunyâ, gloss:onlardan bazılarına yararlansınlar diye verdiğimiz yakın hayatın çiçeğine gözlerini dikme, source:20:131}. Ayet {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike hayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131} diye biter. Sonraki ayet de ailesine namazı emretmesini söyler {source:20:132}. Tesbih, yakın hayat, "daha hayırlı ve daha kalıcı" ve namaz: bizim surenin birinci, on beşinci, on altıncı ve on yedinci ayetlerinin taşıdığı dört şey orada da bir arada durur. Kalıp başka yerlerde de geçer. Kişiye verilen her şeyin yakın hayatın geçimliği ve süsü olduğu söylendikten sonra {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ, tr:ve mâ indallâhi hayrun ve ebkâ e-fe-lâ ta'kılûn, gloss:Allah katında olan daha hayırlı ve daha kalıcıdır; akıl etmez misiniz, source:28:60} denir. Aynı söz iman edip Rablerine dayananlar için de söylenir {source:42:36}. Bizim ayet bu kalıbı ahiret için kullanır ve böylece ahireti "Allah katında olan"ın yerine koyar.

## Kalmak: ilk halinde durmak

[¶18] Ayetin ikinci kelimesinin kökü, yok olmanın karşıtıdır: {ar:بقي الشيء يبقى بقاء وهو ضد الفناء, tr:bakıye'ş-şey'u yebkâ bekâen ve huve diddu'l-fenâ, gloss:şey kaldı, kalır; bu yok oluşun karşıtıdır, source:"ب ق ي,B001"}. Kalmak yalnızca uzun sürmek değildir: {ar:البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء, tr:el-bekâu ŝebâtu'ş-şey'i alâ hâlihi'l-ûlâ ve huve yudâddu'l-fenâ, gloss:bekâ, bir şeyin ilk halinde sabit durmasıdır ve yok oluşun karşıtıdır, source:"ب ق ي,B001"}. Kalıcı olan, zaman geçtikçe başka bir şeye dönüşmeyendir. Surede ilk halinde durmayan şey dördüncü ayetin otlağıdır. Beşinci ayet onu yeşilden kararmış bir sel döküntüsüne çevirir ve gökten otlağa uzanan sahneyi o iki ayetin kelimeleri taşır. Kur'an bu dönüşümü yakın hayatın benzetmesi yapar. Allah Peygamber'e der ki yakın hayatın örneği, gökten inen ve toprağın bitkisine karışan bir sudur. Sonra bitki {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen ardından iki kefe kurulur: {ar:ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:el-mâlu ve'l-benûne zînetu'l-hayâti'd-dunyâ, gloss:mal ve oğullar yakın hayatın süsüdür, source:18:46}, {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Odak ayetin iki kökü orada da yan yanadır: kalan şey, daha hayırlı olandır. Selin benzetmesinde de insanlara fayda veren suyun yerde kalması, beşinci ve dokuzuncu ayetlerin kelimeleriyle surenin sel sahnesini kurar.

[¶19] Kalmak, yaşamak da demektir: {ar:بقي الرجل زمانا طويلا أي عاش, tr:bakıye'r-raculu zemânen tavîlen ey âşe, gloss:adam uzun zaman kaldı, yani yaşadı, source:"ب ق ي,B001"}. Hayatın en dolu adı da kalıcılıkla tarif edilir: {ar:ما له البقاء الأبدي, tr:mâ lehu'l-bekâu'l-ebediyy, gloss:sonsuz kalıcılığı olan, source:"ح ي ي,B003"}. Kur'an bu adı sonraki yurda verir: {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ, tr:ve inne'd-dâre'l-âhirete le-hiye'l-hayevân lev kânû ya'lemûn, gloss:sonraki yurt, işte asıl hayat odur; keşke bilselerdi, source:29:64}. Aynı ayetin başında yakın hayat oyun ve eğlence diye anılır. Böylece on altıncı ayette "yakın" sıfatıyla küçültülen "hayat" kelimesi, on yedinci ayetin "daha kalıcı" sözüyle kendi tam anlamına kavuşur.

[¶20] Kalıcılık tek başına iyi bir şey değildir. Bu yüzden ayet ona "hayırlı" kelimesini eşlik ettirir. Firavun azabının kalıcılığıyla övünmüştü. Allah da Adem'in hikâyesinden sonra, kendi zikrinden yüz çevirenin dar bir geçimi olacağını ve kıyamet günü kör olarak haşredileceğini söyler {source:20:124}. Ardından {ar:وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ, tr:ve le-azâbu'l-âhirati eşeddu ve ebkâ, gloss:sonraki hayatın azabı elbette daha çetin ve daha kalıcıdır, source:20:127} der. Bizim surede de on üçüncü ayetteki adam en büyük ateşte kalır, ama orada ne ölür ne yaşar. Kalır, ama yaşamaz. On yedinci ayetin iki kelimesi bu iki ihtimali ayırır: sonraki hayat yalnızca kalıcı değil, hayırla kalıcıdır. Bu birleşimin bir adı da vardır. On dördüncü ayetin "kurtuluşa erdi" fiilinin kökünden gelen felâh şöyle tanımlanır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh, hayır içinde kalmaktır, source:"ف ل ح,B005"}. On dördüncü ayet arınanın kurtulduğunu söyler. On yedinci ayet de o kurtuluşun tanımındaki iki kelimeyi sonraki hayata yükler. Biri kişiyi, öbürü onun kalacağı yeri anlatır.

[¶21] Kalmak çoğu zaman bağışlanan bir şeydir. {ar:أبقيت على فلان إذا أرعيت عليه ورحمته, tr:ebkaytu alâ fulânin iẕâ er'aytu aleyhi ve rahimtuh, gloss:falancayı sağ bıraktım, yani onu gözettim ve ona acıdım, source:"ب ق ي,B003"}. Yenilen taraf savaşta galip gelene tek bir kelimeyle seslenirdi: {ar:العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا, tr:el-arabu tekûlu li'l-aduvvi iẕâ ğalebe el-bakıyye ey ebkû aleynâ ve lâ testa'sılûnâ, gloss:galip gelen düşmana "bakıyye!" derlerdi, yani bizi sağ bırakın, kökümüzü kazımayın, source:"ب ق ي,B003"}. Kalıcılık, onu verebilecek güçte olanın elindedir. Bu güç kimdedir, bunu on altıncı ayetin fiili söyler: {ar:استأثر الله بالبقاء أي انفرد بالبقاء, tr:ista'ŝerallâhu bi'l-bekâi ey infarada bi'l-bekâ, gloss:Allah kalıcılığı kendine ayırdı, yani kalıcılıkta tek kaldı, source:"ء ث ر,B006"}. İnsanların yakın hayatı öne almak için kullandığı fiil, Allah'ın kalıcılığı yalnızca kendine ayırması için de kullanılır. Kur'an aynı şeyi açıkça söyler: {ar:كُلُّ مَنْ عَلَيْهَا فَانٍۢ, tr:kullu men aleyhâ fân, gloss:yeryüzünde olan herkes yok olucudur, source:55:26}, {ar:وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ, tr:ve yebkâ vechu rabbike ẕu'l-celâli ve'l-ikrâm, gloss:yalnızca celal ve ikram sahibi Rabbinin yüzü kalır, source:55:27}. Allah'ın ahdini az bir bedele satmamaları istenenlere ise {ar:مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ, tr:mâ indekum yenfedu ve mâ indallâhi bâk, gloss:sizin yanınızdaki tükenir, Allah'ın katındaki ise kalır, source:16:96} denir. Sonraki hayatın daha kalıcı olması kendinden değildir. Kalıcılığı elinde tutanın katında olmasındandır.

[¶22] Kök, insanların içinde kalan iyiliği de adlandırır: {ar:أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير, tr:ulû bakıyyetin min dînin kavmun lehum bakıyyetun iẕâ kânet bihim misketun ve fîhim hayr, gloss:dinden bir bakıyyesi olanlar, kendilerinde tutunacak bir şey ve iyilik bulunan topluluktur, source:"ب ق ي,B002"}. Ayetin iki kökü burada tek bir tanımda buluşur: kalan şey, içteki hayırdır. Kur'an, yok edilen kavimlerin hikâyelerinden sonra bunu bir eksiklik olarak anar: {ar:فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ, tr:fe-lev lâ kâne mine'l-kurûni min kablikum ulû bakıyyetin yenhevne ani'l-fesâdi fi'l-ard, gloss:sizden önceki nesiller arasında yeryüzündeki bozgunculuğu önleyecek bir kalıntı sahipleri olsaydı ya, source:11:116}. Aynı ayet, haksızlık edenlerin kendilerine verilen bolluğun peşine düştüğünü söyler. Yakını öne almak, içte kalabilecek hayrı da bu bolluğa harcamaktır.

## Gözleyerek beklemek

[¶23] Aynı kökte, ayetteki "kalmak" fiilinden ayrı çekimlenen bir fiil daha vardır ve bir bekleyişi anlatır. Ayetin kelimesi bu fiilden gelmez. Ama sonraki hayattan söz eden bir cümlede bu fiil de kulağa ulaşır. Çölde bir adam için {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca geceyi şimşeği gözleyerek geçirdi, yani nereden çakacağına baktı, source:"ب ق ي,B005"} denirdi. Ufukta çakan şimşek, bulutun nereye yağacağını, dolayısıyla otun nerede biteceğini haber verir. Şimşeği gözleyen, henüz görmediği bir yağmurun yerini öğrenmek için uykusundan vazgeçen kişidir. Bu gözleyişin bulutu, yedinci ayette gizli olanı anlatan fiilin kökünden gelen zayıf şimşekle ve dördüncü ayetteki otlağı çıkarma fiiliyle surenin yağmur sahnesine bağlanır. Aynı fiil insanlar için de kullanılır: {ar:بقينا رسول الله أي انتظرناه, tr:bakaynâ rasûlallâhi ey intazarnâh, gloss:Allah'ın elçisini gözledik, yani onu bekledik, source:"ب ق ي,B005"}.

[¶24] Sonra gelen şey, beklenen şeydir. Yakını öne alan, ufka bakmayı bırakmış kişidir. Elindeki otla yetinir ve gelecek yağmurun haberini kollamaz. Kur'an, kalıcı iyi işlerin Rabbin katında daha hayırlı olduğunu söylediği ayeti şu sözle bitirir: {ar:وَخَيْرٌ أَمَلًۭا, tr:ve hayrun emelâ, gloss:umut bağlamak bakımından da daha hayırlıdır, source:18:46}. Umut, gözü bir şeyin gelişine dikmektir. Odak ayetin iki kelimesi bu bekleyişe bir güvence verir. Gözlenen şey geldiğinde iyi olacaktır, geldiğinde de bir daha gitmeyecektir. Hasattan sonra dalında yükü duran ağaç gibi, sonra gelen şey sona kalandır.

===== _commentary/v16/out/87_17/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: khayr functions as elative without af'al form
- memory: dunyā, kubrā, yusrā, ūlā are fuʿlā elative/rank forms
- memory: vowelling bi-akhiratin / bi-naẓiratin in deferred-sale phrase
- memory: lightning watched at night to locate rain and coming pasture
- memory: ṣirām = cutting/harvesting of dates
- memory: Turkish "muhtar" from Arabic mukhtār, root خ ي ر
- not written: hyena-burrow istikhāra (خ ي ر B006) - kalıp image did no work in any theme
- not written: khayr as gift/generosity (B005) - only a loose link to 93:5, would be forced
- not written: الآخر الغائب (ayn) - vowel and sense uncertain, not used
- not written: dictionary gloss of al-bāqiyāt al-ṣāliḥāt as five prayers - exegetical view, excluded
- not written: 20:130 and 93:5 shared "tarḍā" - echo beyond this ayah's themes

===== passages not cited (253) =====
## strong (this ayah's own list) (44)

- (2:86) [listed for 87:17] [cited in ¶10] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
- (3:14) [listed for 87:17] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
- (3:15) [listed for 87:17] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:185) [listed for 87:17] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (4:77) [listed for 87:17] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
- (6:32) [listed for 87:17] وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَعِبٌۭ وَلَهْوٌۭ ۖ وَلَلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ
- (7:169) [listed for 87:17] فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌۭ وَرِثُوا۟ ٱلْكِتَٰبَ يَأْخُذُونَ عَرَضَ هَٰذَا ٱلْأَدْنَىٰ وَيَقُولُونَ سَيُغْفَرُ لَنَا وَإِن يَأْتِهِمْ عَرَضٌۭ مِّثْلُهُۥ يَأْخُذُوهُ ۚ أَلَمْ يُؤْخَذْ عَلَيْهِم مِّيثَٰقُ ٱلْكِتَٰبِ أَن لَّا يَقُولُوا۟ عَلَى ٱللَّهِ إِلَّا ٱلْحَقَّ وَدَرَسُوا۟ مَا فِيهِ ۗ وَٱلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ
- (8:67) [listed for 87:17] مَا كَانَ لِنَبِىٍّ أَن يَكُونَ لَهُۥٓ أَسْرَىٰ حَتَّىٰ يُثْخِنَ فِى ٱلْأَرْضِ ۚ تُرِيدُونَ عَرَضَ ٱلدُّنْيَا وَٱللَّهُ يُرِيدُ ٱلْءَاخِرَةَ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌۭ
- (9:38) [listed for 87:17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ ۚ فَمَا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا قَلِيلٌ
- (11:15) [listed for 87:17] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
- (11:16) [listed for 87:17] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
- (11:86) [listed for 87:17] بَقِيَّتُ ٱللَّهِ خَيْرٌۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ ۚ وَمَآ أَنَا۠ عَلَيْكُم بِحَفِيظٍۢ
- (12:57) [listed for 87:17] وَلَأَجْرُ ٱلْءَاخِرَةِ خَيْرٌۭ لِّلَّذِينَ ءَامَنُوا۟ وَكَانُوا۟ يَتَّقُونَ
- (12:109) [listed for 87:17] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ إِلَّا رِجَالًۭا نُّوحِىٓ إِلَيْهِم مِّنْ أَهْلِ ٱلْقُرَىٰٓ ۗ أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۗ وَلَدَارُ ٱلْءَاخِرَةِ خَيْرٌۭ لِّلَّذِينَ ٱتَّقَوْا۟ ۗ أَفَلَا تَعْقِلُونَ
- (13:26) [listed for 87:17] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ وَفَرِحُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا مَتَٰعٌۭ
- (14:3) [listed for 87:17] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (16:30) [listed for 87:17] ۞ وَقِيلَ لِلَّذِينَ ٱتَّقَوْا۟ مَاذَآ أَنزَلَ رَبُّكُمْ ۚ قَالُوا۟ خَيْرًۭا ۗ لِّلَّذِينَ أَحْسَنُوا۟ فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةٌۭ ۚ وَلَدَارُ ٱلْءَاخِرَةِ خَيْرٌۭ ۚ وَلَنِعْمَ دَارُ ٱلْمُتَّقِينَ
- (16:96) [listed for 87:17] [cited in ¶21] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (16:107) [listed for 87:17] ذَٰلِكَ بِأَنَّهُمُ ٱسْتَحَبُّوا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَأَنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (17:18) [listed for 87:17] [cited in ¶10] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
- (17:19) [listed for 87:17] [cited in ¶10] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
- (17:21) [listed for 87:17] ٱنظُرْ كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۚ وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًۭا
- (18:45) [listed for 87:17] [cited in ¶18] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
- (18:46) [listed for 87:17] [cited in ¶18, ¶24] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
- (19:76) [listed for 87:17] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
- (20:71) [listed for 87:17] [cited in ¶17] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (20:72) [listed for 87:17] [cited in ¶17] قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ
- (20:73) [listed for 87:17] [cited in ¶17] إِنَّآ ءَامَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَٰيَٰنَا وَمَآ أَكْرَهْتَنَا عَلَيْهِ مِنَ ٱلسِّحْرِ ۗ وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ
- (20:127) [listed for 87:17] [cited in ¶20] وَكَذَٰلِكَ نَجْزِى مَنْ أَسْرَفَ وَلَمْ يُؤْمِنۢ بِـَٔايَٰتِ رَبِّهِۦ ۚ وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ
- (20:131) [listed for 87:17] [cited in ¶17] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
- (28:60) [listed for 87:17] [cited in ¶17] وَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَزِينَتُهَا ۚ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ
- (28:61) [listed for 87:17] أَفَمَن وَعَدْنَٰهُ وَعْدًا حَسَنًۭا فَهُوَ لَٰقِيهِ كَمَن مَّتَّعْنَٰهُ مَتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ثُمَّ هُوَ يَوْمَ ٱلْقِيَٰمَةِ مِنَ ٱلْمُحْضَرِينَ
- (29:64) [listed for 87:17] [cited in ¶19] وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ ۚ وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- (33:28) [listed for 87:17] يَٰٓأَيُّهَا ٱلنَّبِىُّ قُل لِّأَزْوَٰجِكَ إِن كُنتُنَّ تُرِدْنَ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا فَتَعَالَيْنَ أُمَتِّعْكُنَّ وَأُسَرِّحْكُنَّ سَرَاحًۭا جَمِيلًۭا
- (33:29) [listed for 87:17] وَإِن كُنتُنَّ تُرِدْنَ ٱللَّهَ وَرَسُولَهُۥ وَٱلدَّارَ ٱلْءَاخِرَةَ فَإِنَّ ٱللَّهَ أَعَدَّ لِلْمُحْسِنَٰتِ مِنكُنَّ أَجْرًا عَظِيمًۭا
- (40:39) [listed for 87:17] يَٰقَوْمِ إِنَّمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَا مَتَٰعٌۭ وَإِنَّ ٱلْءَاخِرَةَ هِىَ دَارُ ٱلْقَرَارِ
- (42:20) [listed for 87:17] مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
- (43:28) [listed for 87:17] وَجَعَلَهَا كَلِمَةًۢ بَاقِيَةًۭ فِى عَقِبِهِۦ لَعَلَّهُمْ يَرْجِعُونَ
- (43:35) [listed for 87:17] وَزُخْرُفًۭا ۚ وَإِن كُلُّ ذَٰلِكَ لَمَّا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَٱلْءَاخِرَةُ عِندَ رَبِّكَ لِلْمُتَّقِينَ
- (57:20) [listed for 87:17] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (75:20) [listed for 87:17] [cited in ¶10] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
- (75:21) [listed for 87:17] [cited in ¶10] وَتَذَرُونَ ٱلْءَاخِرَةَ
- (76:27) [listed for 87:17] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
- (79:38) [listed for 87:17] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا

## medium (this ayah's own list) (51)

- (2:200) [listed for 87:17] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
- (2:212) [listed for 87:17] زُيِّنَ لِلَّذِينَ كَفَرُوا۟ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَيَسْخَرُونَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ ۘ وَٱلَّذِينَ ٱتَّقَوْا۟ فَوْقَهُمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
- (2:217) [listed for 87:17] يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ ۖ وَصَدٌّ عَن سَبِيلِ ٱللَّهِ وَكُفْرٌۢ بِهِۦ وَٱلْمَسْجِدِ ٱلْحَرَامِ وَإِخْرَاجُ أَهْلِهِۦ مِنْهُ أَكْبَرُ عِندَ ٱللَّهِ ۚ وَٱلْفِتْنَةُ أَكْبَرُ مِنَ ٱلْقَتْلِ ۗ وَلَا يَزَالُونَ يُقَٰتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ ٱسْتَطَٰعُوا۟ ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِۦ فَيَمُتْ وَهُوَ كَافِرٌۭ فَأُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:248) [listed for 87:17] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ءَايَةَ مُلْكِهِۦٓ أَن يَأْتِيَكُمُ ٱلتَّابُوتُ فِيهِ سَكِينَةٌۭ مِّن رَّبِّكُمْ وَبَقِيَّةٌۭ مِّمَّا تَرَكَ ءَالُ مُوسَىٰ وَءَالُ هَٰرُونَ تَحْمِلُهُ ٱلْمَلَٰٓئِكَةُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
- (3:56) [listed for 87:17] فَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَأُعَذِّبُهُمْ عَذَابًۭا شَدِيدًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (3:145) [listed for 87:17] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
- (3:152) [listed for 87:17] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
- (4:134) [listed for 87:17] مَّن كَانَ يُرِيدُ ثَوَابَ ٱلدُّنْيَا فَعِندَ ٱللَّهِ ثَوَابُ ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَكَانَ ٱللَّهُ سَمِيعًۢا بَصِيرًۭا
- (5:41) [listed for 87:17] ۞ يَٰٓأَيُّهَا ٱلرَّسُولُ لَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ مِنَ ٱلَّذِينَ قَالُوٓا۟ ءَامَنَّا بِأَفْوَٰهِهِمْ وَلَمْ تُؤْمِن قُلُوبُهُمْ ۛ وَمِنَ ٱلَّذِينَ هَادُوا۟ ۛ سَمَّٰعُونَ لِلْكَذِبِ سَمَّٰعُونَ لِقَوْمٍ ءَاخَرِينَ لَمْ يَأْتُوكَ ۖ يُحَرِّفُونَ ٱلْكَلِمَ مِنۢ بَعْدِ مَوَاضِعِهِۦ ۖ يَقُولُونَ إِنْ أُوتِيتُمْ هَٰذَا فَخُذُوهُ وَإِن لَّمْ تُؤْتَوْهُ فَٱحْذَرُوا۟ ۚ وَمَن يُرِدِ ٱللَّهُ فِتْنَتَهُۥ فَلَن تَمْلِكَ لَهُۥ مِنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ لَمْ يُرِدِ ٱللَّهُ أَن يُطَهِّرَ قُلُوبَهُمْ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (6:70) [listed for 87:17] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (6:158) [listed for 87:17] هَلْ يَنظُرُونَ إِلَّآ أَن تَأْتِيَهُمُ ٱلْمَلَٰٓئِكَةُ أَوْ يَأْتِىَ رَبُّكَ أَوْ يَأْتِىَ بَعْضُ ءَايَٰتِ رَبِّكَ ۗ يَوْمَ يَأْتِى بَعْضُ ءَايَٰتِ رَبِّكَ لَا يَنفَعُ نَفْسًا إِيمَٰنُهَا لَمْ تَكُنْ ءَامَنَتْ مِن قَبْلُ أَوْ كَسَبَتْ فِىٓ إِيمَٰنِهَا خَيْرًۭا ۗ قُلِ ٱنتَظِرُوٓا۟ إِنَّا مُنتَظِرُونَ
- (7:51) [listed for 87:17] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (9:69) [listed for 87:17] كَٱلَّذِينَ مِن قَبْلِكُمْ كَانُوٓا۟ أَشَدَّ مِنكُمْ قُوَّةًۭ وَأَكْثَرَ أَمْوَٰلًۭا وَأَوْلَٰدًۭا فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ فَٱسْتَمْتَعْتُم بِخَلَٰقِكُمْ كَمَا ٱسْتَمْتَعَ ٱلَّذِينَ مِن قَبْلِكُم بِخَلَٰقِهِمْ وَخُضْتُمْ كَٱلَّذِى خَاضُوٓا۟ ۚ أُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (10:7) [listed for 87:17] إِنَّ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا وَرَضُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَٱطْمَأَنُّوا۟ بِهَا وَٱلَّذِينَ هُمْ عَنْ ءَايَٰتِنَا غَٰفِلُونَ
- (10:24) [listed for 87:17] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
- (10:70) [listed for 87:17] مَتَٰعٌۭ فِى ٱلدُّنْيَا ثُمَّ إِلَيْنَا مَرْجِعُهُمْ ثُمَّ نُذِيقُهُمُ ٱلْعَذَابَ ٱلشَّدِيدَ بِمَا كَانُوا۟ يَكْفُرُونَ
- (11:116) [listed for 87:17] [cited in ¶22] فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ إِلَّا قَلِيلًۭا مِّمَّنْ أَنجَيْنَا مِنْهُمْ ۗ وَٱتَّبَعَ ٱلَّذِينَ ظَلَمُوا۟ مَآ أُتْرِفُوا۟ فِيهِ وَكَانُوا۟ مُجْرِمِينَ
- (12:101) [listed for 87:17] ۞ رَبِّ قَدْ ءَاتَيْتَنِى مِنَ ٱلْمُلْكِ وَعَلَّمْتَنِى مِن تَأْوِيلِ ٱلْأَحَادِيثِ ۚ فَاطِرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ أَنتَ وَلِىِّۦ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ تَوَفَّنِى مُسْلِمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (15:5) [listed for 87:17] مَّا تَسْبِقُ مِنْ أُمَّةٍ أَجَلَهَا وَمَا يَسْتَـْٔخِرُونَ
- (17:10) [listed for 87:17] وَأَنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًۭا
- (18:28) [listed for 87:17] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (18:44) [listed for 87:17] هُنَالِكَ ٱلْوَلَٰيَةُ لِلَّهِ ٱلْحَقِّ ۚ هُوَ خَيْرٌۭ ثَوَابًۭا وَخَيْرٌ عُقْبًۭا
- (22:11) [listed for 87:17] وَمِنَ ٱلنَّاسِ مَن يَعْبُدُ ٱللَّهَ عَلَىٰ حَرْفٍۢ ۖ فَإِنْ أَصَابَهُۥ خَيْرٌ ٱطْمَأَنَّ بِهِۦ ۖ وَإِنْ أَصَابَتْهُ فِتْنَةٌ ٱنقَلَبَ عَلَىٰ وَجْهِهِۦ خَسِرَ ٱلدُّنْيَا وَٱلْءَاخِرَةَ ۚ ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (24:14) [listed for 87:17] وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ لَمَسَّكُمْ فِى مَآ أَفَضْتُمْ فِيهِ عَذَابٌ عَظِيمٌ
- (24:19) [listed for 87:17] إِنَّ ٱلَّذِينَ يُحِبُّونَ أَن تَشِيعَ ٱلْفَٰحِشَةُ فِى ٱلَّذِينَ ءَامَنُوا۟ لَهُمْ عَذَابٌ أَلِيمٌۭ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (24:23) [listed for 87:17] إِنَّ ٱلَّذِينَ يَرْمُونَ ٱلْمُحْصَنَٰتِ ٱلْغَٰفِلَٰتِ ٱلْمُؤْمِنَٰتِ لُعِنُوا۟ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
- (28:70) [listed for 87:17] وَهُوَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ ۖ وَلَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
- (30:7) [listed for 87:17] يَعْلَمُونَ ظَٰهِرًۭا مِّنَ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ عَنِ ٱلْءَاخِرَةِ هُمْ غَٰفِلُونَ
- (31:33) [listed for 87:17] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمْ وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا ۚ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (33:57) [listed for 87:17] إِنَّ ٱلَّذِينَ يُؤْذُونَ ٱللَّهَ وَرَسُولَهُۥ لَعَنَهُمُ ٱللَّهُ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَأَعَدَّ لَهُمْ عَذَابًۭا مُّهِينًۭا
- (35:5) [listed for 87:17] يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۖ وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (37:77) [listed for 87:17] وَجَعَلْنَا ذُرِّيَّتَهُۥ هُمُ ٱلْبَاقِينَ
- (42:36) [listed for 87:17] [cited in ¶17] فَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (47:36) [listed for 87:17] إِنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ ۚ وَإِن تُؤْمِنُوا۟ وَتَتَّقُوا۟ يُؤْتِكُمْ أُجُورَكُمْ وَلَا يَسْـَٔلْكُمْ أَمْوَٰلَكُمْ
- (53:25) [listed for 87:17] [cited in ¶7] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (53:47) [listed for 87:17] وَأَنَّ عَلَيْهِ ٱلنَّشْأَةَ ٱلْأُخْرَىٰ
- (53:51) [listed for 87:17] وَثَمُودَا۟ فَمَآ أَبْقَىٰ
- (63:9) [listed for 87:17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (63:10) [listed for 87:17] وَأَنفِقُوا۟ مِن مَّا رَزَقْنَٰكُم مِّن قَبْلِ أَن يَأْتِىَ أَحَدَكُمُ ٱلْمَوْتُ فَيَقُولَ رَبِّ لَوْلَآ أَخَّرْتَنِىٓ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ فَأَصَّدَّقَ وَأَكُن مِّنَ ٱلصَّٰلِحِينَ
- (63:11) [listed for 87:17] وَلَن يُؤَخِّرَ ٱللَّهُ نَفْسًا إِذَا جَآءَ أَجَلُهَا ۚ وَٱللَّهُ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (64:15) [listed for 87:17] إِنَّمَآ أَمْوَٰلُكُمْ وَأَوْلَٰدُكُمْ فِتْنَةٌۭ ۚ وَٱللَّهُ عِندَهُۥٓ أَجْرٌ عَظِيمٌۭ
- (69:8) [listed for 87:17] فَهَلْ تَرَىٰ لَهُم مِّنۢ بَاقِيَةٍۢ
- (74:28) [listed for 87:17] لَا تُبْقِى وَلَا تَذَرُ
- (75:13) [listed for 87:17] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
- (79:37) [listed for 87:17] فَأَمَّا مَن طَغَىٰ
- (79:39) [listed for 87:17] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
- (79:40) [listed for 87:17] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
- (79:41) [listed for 87:17] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- (92:13) [listed for 87:17] [cited in ¶7] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (93:4) [listed for 87:17] [cited in ¶7] وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ
- (102:1) [listed for 87:17] أَلْهَىٰكُمُ ٱلتَّكَاثُرُ

## named by the passage's own list as strong for this ayah (24)

- (2:61) [listed for 87:17] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (2:96) [listed for 87:17] وَلَتَجِدَنَّهُمْ أَحْرَصَ ٱلنَّاسِ عَلَىٰ حَيَوٰةٍۢ وَمِنَ ٱلَّذِينَ أَشْرَكُوا۟ ۚ يَوَدُّ أَحَدُهُمْ لَوْ يُعَمَّرُ أَلْفَ سَنَةٍۢ وَمَا هُوَ بِمُزَحْزِحِهِۦ مِنَ ٱلْعَذَابِ أَن يُعَمَّرَ ۗ وَٱللَّهُ بَصِيرٌۢ بِمَا يَعْمَلُونَ
- (3:196) [listed for 87:17] لَا يَغُرَّنَّكَ تَقَلُّبُ ٱلَّذِينَ كَفَرُوا۟ فِى ٱلْبِلَٰدِ
- (3:197) [listed for 87:17] مَتَٰعٌۭ قَلِيلٌۭ ثُمَّ مَأْوَىٰهُمْ جَهَنَّمُ ۚ وَبِئْسَ ٱلْمِهَادُ
- (5:100) [listed for 87:17] قُل لَّا يَسْتَوِى ٱلْخَبِيثُ وَٱلطَّيِّبُ وَلَوْ أَعْجَبَكَ كَثْرَةُ ٱلْخَبِيثِ ۚ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تُفْلِحُونَ
- (15:3) [listed for 87:17] ذَرْهُمْ يَأْكُلُوا۟ وَيَتَمَتَّعُوا۟ وَيُلْهِهِمُ ٱلْأَمَلُ ۖ فَسَوْفَ يَعْلَمُونَ
- (16:95) [listed for 87:17] وَلَا تَشْتَرُوا۟ بِعَهْدِ ٱللَّهِ ثَمَنًۭا قَلِيلًا ۚ إِنَّمَا عِندَ ٱللَّهِ هُوَ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (16:109) [listed for 87:17] لَا جَرَمَ أَنَّهُمْ فِى ٱلْءَاخِرَةِ هُمُ ٱلْخَٰسِرُونَ
- (18:34) [listed for 87:17] وَكَانَ لَهُۥ ثَمَرٌۭ فَقَالَ لِصَٰحِبِهِۦ وَهُوَ يُحَاوِرُهُۥٓ أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا
- (18:35) [listed for 87:17] وَدَخَلَ جَنَّتَهُۥ وَهُوَ ظَالِمٌۭ لِّنَفْسِهِۦ قَالَ مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا
- (18:104) [listed for 87:17] ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا
- (23:56) [listed for 87:17] نُسَارِعُ لَهُمْ فِى ٱلْخَيْرَٰتِ ۚ بَل لَّا يَشْعُرُونَ
- (26:205) [listed for 87:17] أَفَرَءَيْتَ إِن مَّتَّعْنَٰهُمْ سِنِينَ
- (26:207) [listed for 87:17] مَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يُمَتَّعُونَ
- (28:77) [listed for 87:17] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (28:80) [listed for 87:17] وَقَالَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ وَيْلَكُمْ ثَوَابُ ٱللَّهِ خَيْرٌۭ لِّمَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا وَلَا يُلَقَّىٰهَآ إِلَّا ٱلصَّٰبِرُونَ
- (28:83) [listed for 87:17] تِلْكَ ٱلدَّارُ ٱلْءَاخِرَةُ نَجْعَلُهَا لِلَّذِينَ لَا يُرِيدُونَ عُلُوًّۭا فِى ٱلْأَرْضِ وَلَا فَسَادًۭا ۚ وَٱلْعَٰقِبَةُ لِلْمُتَّقِينَ
- (31:24) [listed for 87:17] نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ
- (38:31) [listed for 87:17] إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ
- (45:35) [listed for 87:17] ذَٰلِكُم بِأَنَّكُمُ ٱتَّخَذْتُمْ ءَايَٰتِ ٱللَّهِ هُزُوًۭا وَغَرَّتْكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ لَا يُخْرَجُونَ مِنْهَا وَلَا هُمْ يُسْتَعْتَبُونَ
- (53:29) [listed for 87:17] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (55:27) [listed for 87:17] [cited in ¶21] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (62:11) [listed for 87:17] وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ
- (77:46) [listed for 87:17] كُلُوا۟ وَتَمَتَّعُوا۟ قَلِيلًا إِنَّكُم مُّجْرِمُونَ

## named by the passage's own list as medium for this ayah (18)

- (3:176) [listed for 87:17] وَلَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ ۚ إِنَّهُمْ لَن يَضُرُّوا۟ ٱللَّهَ شَيْـًۭٔا ۗ يُرِيدُ ٱللَّهُ أَلَّا يَجْعَلَ لَهُمْ حَظًّۭا فِى ٱلْءَاخِرَةِ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌ
- (10:23) [listed for 87:17] فَلَمَّآ أَنجَىٰهُمْ إِذَا هُمْ يَبْغُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ ۗ يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّمَا بَغْيُكُمْ عَلَىٰٓ أَنفُسِكُم ۖ مَّتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ ثُمَّ إِلَيْنَا مَرْجِعُكُمْ فَنُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (11:3) [listed for 87:17] وَأَنِ ٱسْتَغْفِرُوا۟ رَبَّكُمْ ثُمَّ تُوبُوٓا۟ إِلَيْهِ يُمَتِّعْكُم مَّتَٰعًا حَسَنًا إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى وَيُؤْتِ كُلَّ ذِى فَضْلٍۢ فَضْلَهُۥ ۖ وَإِن تَوَلَّوْا۟ فَإِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍۢ كَبِيرٍ
- (12:20) [listed for 87:17] وَشَرَوْهُ بِثَمَنٍۭ بَخْسٍۢ دَرَٰهِمَ مَعْدُودَةٍۢ وَكَانُوا۟ فِيهِ مِنَ ٱلزَّٰهِدِينَ
- (18:7) [listed for 87:17] إِنَّا جَعَلْنَا مَا عَلَى ٱلْأَرْضِ زِينَةًۭ لَّهَا لِنَبْلُوَهُمْ أَيُّهُمْ أَحْسَنُ عَمَلًۭا
- (25:24) [listed for 87:17] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (27:59) [listed for 87:17] قُلِ ٱلْحَمْدُ لِلَّهِ وَسَلَٰمٌ عَلَىٰ عِبَادِهِ ٱلَّذِينَ ٱصْطَفَىٰٓ ۗ ءَآللَّهُ خَيْرٌ أَمَّا يُشْرِكُونَ
- (38:47) [listed for 87:17] وَإِنَّهُمْ عِندَنَا لَمِنَ ٱلْمُصْطَفَيْنَ ٱلْأَخْيَارِ
- (43:32) [listed for 87:17] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (46:20) [listed for 87:17] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَذْهَبْتُمْ طَيِّبَٰتِكُمْ فِى حَيَاتِكُمُ ٱلدُّنْيَا وَٱسْتَمْتَعْتُم بِهَا فَٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَسْتَكْبِرُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَبِمَا كُنتُمْ تَفْسُقُونَ
- (70:41) [listed for 87:17] عَلَىٰٓ أَن نُّبَدِّلَ خَيْرًۭا مِّنْهُمْ وَمَا نَحْنُ بِمَسْبُوقِينَ
- (75:5) [listed for 87:17] بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ
- (77:17) [listed for 87:17] ثُمَّ نُتْبِعُهُمُ ٱلْءَاخِرِينَ
- (92:20) [listed for 87:17] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (93:5) [listed for 87:17] [cited in ¶7] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (97:3) [listed for 87:17] لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ
- (100:8) [listed for 87:17] [cited in ¶16] وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- (103:1) [listed for 87:17] وَٱلْعَصْرِ

## weak (this ayah's own list) (25)

- (2:184) [listed for 87:17] أَيَّامًۭا مَّعْدُودَٰتٍۢ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۚ وَعَلَى ٱلَّذِينَ يُطِيقُونَهُۥ فِدْيَةٌۭ طَعَامُ مِسْكِينٍۢ ۖ فَمَن تَطَوَّعَ خَيْرًۭا فَهُوَ خَيْرٌۭ لَّهُۥ ۚ وَأَن تَصُومُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (2:220) [listed for 87:17] فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۗ وَيَسْـَٔلُونَكَ عَنِ ٱلْيَتَٰمَىٰ ۖ قُلْ إِصْلَاحٌۭ لَّهُمْ خَيْرٌۭ ۖ وَإِن تُخَالِطُوهُمْ فَإِخْوَٰنُكُمْ ۚ وَٱللَّهُ يَعْلَمُ ٱلْمُفْسِدَ مِنَ ٱلْمُصْلِحِ ۚ وَلَوْ شَآءَ ٱللَّهُ لَأَعْنَتَكُمْ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (2:278) [listed for 87:17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَذَرُوا۟ مَا بَقِىَ مِنَ ٱلرِّبَوٰٓا۟ إِن كُنتُم مُّؤْمِنِينَ
- (3:22) [listed for 87:17] أُو۟لَٰٓئِكَ ٱلَّذِينَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (3:45) [listed for 87:17] إِذْ قَالَتِ ٱلْمَلَٰٓئِكَةُ يَٰمَرْيَمُ إِنَّ ٱللَّهَ يُبَشِّرُكِ بِكَلِمَةٍۢ مِّنْهُ ٱسْمُهُ ٱلْمَسِيحُ عِيسَى ٱبْنُ مَرْيَمَ وَجِيهًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَمِنَ ٱلْمُقَرَّبِينَ
- (3:114) [listed for 87:17] يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَيَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَيُسَٰرِعُونَ فِى ٱلْخَيْرَٰتِ وَأُو۟لَٰٓئِكَ مِنَ ٱلصَّٰلِحِينَ
- (4:59) [listed for 87:17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ وَأُو۟لِى ٱلْأَمْرِ مِنكُمْ ۖ فَإِن تَنَٰزَعْتُمْ فِى شَىْءٍۢ فَرُدُّوهُ إِلَى ٱللَّهِ وَٱلرَّسُولِ إِن كُنتُمْ تُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ ذَٰلِكَ خَيْرٌۭ وَأَحْسَنُ تَأْوِيلًا
- (7:85) [listed for 87:17] وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ فَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
- (8:23) [listed for 87:17] وَلَوْ عَلِمَ ٱللَّهُ فِيهِمْ خَيْرًۭا لَّأَسْمَعَهُمْ ۖ وَلَوْ أَسْمَعَهُمْ لَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ
- (8:30) [listed for 87:17] وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ ۚ وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ ۖ وَٱللَّهُ خَيْرُ ٱلْمَٰكِرِينَ
- (9:3) [listed for 87:17] وَأَذَٰنٌۭ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلنَّاسِ يَوْمَ ٱلْحَجِّ ٱلْأَكْبَرِ أَنَّ ٱللَّهَ بَرِىٓءٌۭ مِّنَ ٱلْمُشْرِكِينَ ۙ وَرَسُولُهُۥ ۚ فَإِن تُبْتُمْ فَهُوَ خَيْرٌۭ لَّكُمْ ۖ وَإِن تَوَلَّيْتُمْ فَٱعْلَمُوٓا۟ أَنَّكُمْ غَيْرُ مُعْجِزِى ٱللَّهِ ۗ وَبَشِّرِ ٱلَّذِينَ كَفَرُوا۟ بِعَذَابٍ أَلِيمٍ
- (9:61) [listed for 87:17] وَمِنْهُمُ ٱلَّذِينَ يُؤْذُونَ ٱلنَّبِىَّ وَيَقُولُونَ هُوَ أُذُنٌۭ ۚ قُلْ أُذُنُ خَيْرٍۢ لَّكُمْ يُؤْمِنُ بِٱللَّهِ وَيُؤْمِنُ لِلْمُؤْمِنِينَ وَرَحْمَةٌۭ لِّلَّذِينَ ءَامَنُوا۟ مِنكُمْ ۚ وَٱلَّذِينَ يُؤْذُونَ رَسُولَ ٱللَّهِ لَهُمْ عَذَابٌ أَلِيمٌۭ
- (9:74) [listed for 87:17] يَحْلِفُونَ بِٱللَّهِ مَا قَالُوا۟ وَلَقَدْ قَالُوا۟ كَلِمَةَ ٱلْكُفْرِ وَكَفَرُوا۟ بَعْدَ إِسْلَٰمِهِمْ وَهَمُّوا۟ بِمَا لَمْ يَنَالُوا۟ ۚ وَمَا نَقَمُوٓا۟ إِلَّآ أَنْ أَغْنَىٰهُمُ ٱللَّهُ وَرَسُولُهُۥ مِن فَضْلِهِۦ ۚ فَإِن يَتُوبُوا۟ يَكُ خَيْرًۭا لَّهُمْ ۖ وَإِن يَتَوَلَّوْا۟ يُعَذِّبْهُمُ ٱللَّهُ عَذَابًا أَلِيمًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَمَا لَهُمْ فِى ٱلْأَرْضِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (18:81) [listed for 87:17] فَأَرَدْنَآ أَن يُبْدِلَهُمَا رَبُّهُمَا خَيْرًۭا مِّنْهُ زَكَوٰةًۭ وَأَقْرَبَ رُحْمًۭا
- (18:95) [listed for 87:17] قَالَ مَا مَكَّنِّى فِيهِ رَبِّى خَيْرٌۭ فَأَعِينُونِى بِقُوَّةٍ أَجْعَلْ بَيْنَكُمْ وَبَيْنَهُمْ رَدْمًا
- (22:15) [listed for 87:17] مَن كَانَ يَظُنُّ أَن لَّن يَنصُرَهُ ٱللَّهُ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ فَلْيَمْدُدْ بِسَبَبٍ إِلَى ٱلسَّمَآءِ ثُمَّ لْيَقْطَعْ فَلْيَنظُرْ هَلْ يُذْهِبَنَّ كَيْدُهُۥ مَا يَغِيظُ
- (22:30) [listed for 87:17] ذَٰلِكَ وَمَن يُعَظِّمْ حُرُمَٰتِ ٱللَّهِ فَهُوَ خَيْرٌۭ لَّهُۥ عِندَ رَبِّهِۦ ۗ وَأُحِلَّتْ لَكُمُ ٱلْأَنْعَٰمُ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ ۖ فَٱجْتَنِبُوا۟ ٱلرِّجْسَ مِنَ ٱلْأَوْثَٰنِ وَٱجْتَنِبُوا۟ قَوْلَ ٱلزُّورِ
- (23:118) [listed for 87:17] وَقُل رَّبِّ ٱغْفِرْ وَٱرْحَمْ وَأَنتَ خَيْرُ ٱلرَّٰحِمِينَ
- (26:120) [listed for 87:17] ثُمَّ أَغْرَقْنَا بَعْدُ ٱلْبَاقِينَ
- (26:172) [listed for 87:17] ثُمَّ دَمَّرْنَا ٱلْءَاخَرِينَ
- (29:16) [listed for 87:17] وَإِبْرَٰهِيمَ إِذْ قَالَ لِقَوْمِهِ ٱعْبُدُوا۟ ٱللَّهَ وَٱتَّقُوهُ ۖ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (38:48) [listed for 87:17] وَٱذْكُرْ إِسْمَٰعِيلَ وَٱلْيَسَعَ وَذَا ٱلْكِفْلِ ۖ وَكُلٌّۭ مِّنَ ٱلْأَخْيَارِ
- (55:70) [listed for 87:17] فِيهِنَّ خَيْرَٰتٌ حِسَانٌۭ
- (61:11) [listed for 87:17] تُؤْمِنُونَ بِٱللَّهِ وَرَسُولِهِۦ وَتُجَٰهِدُونَ فِى سَبِيلِ ٱللَّهِ بِأَمْوَٰلِكُمْ وَأَنفُسِكُمْ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (99:7) [listed for 87:17] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ

## named by the passage's own list as weak for this ayah (17)

- (2:263) [listed for 87:17] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
- (3:54) [listed for 87:17] وَمَكَرُوا۟ وَمَكَرَ ٱللَّهُ ۖ وَٱللَّهُ خَيْرُ ٱلْمَٰكِرِينَ
- (3:157) [listed for 87:17] وَلَئِن قُتِلْتُمْ فِى سَبِيلِ ٱللَّهِ أَوْ مُتُّمْ لَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرَحْمَةٌ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (17:45) [listed for 87:17] وَإِذَا قَرَأْتَ ٱلْقُرْءَانَ جَعَلْنَا بَيْنَكَ وَبَيْنَ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ حِجَابًۭا مَّسْتُورًۭا
- (23:109) [listed for 87:17] إِنَّهُۥ كَانَ فَرِيقٌۭ مِّنْ عِبَادِى يَقُولُونَ رَبَّنَآ ءَامَنَّا فَٱغْفِرْ لَنَا وَٱرْحَمْنَا وَأَنتَ خَيْرُ ٱلرَّٰحِمِينَ
- (26:64) [listed for 87:17] وَأَزْلَفْنَا ثَمَّ ٱلْءَاخَرِينَ
- (26:66) [listed for 87:17] ثُمَّ أَغْرَقْنَا ٱلْءَاخَرِينَ
- (27:5) [listed for 87:17] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَهُمْ سُوٓءُ ٱلْعَذَابِ وَهُمْ فِى ٱلْءَاخِرَةِ هُمُ ٱلْأَخْسَرُونَ
- (37:62) [listed for 87:17] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (41:49) [listed for 87:17] لَّا يَسْـَٔمُ ٱلْإِنسَٰنُ مِن دُعَآءِ ٱلْخَيْرِ وَإِن مَّسَّهُ ٱلشَّرُّ فَيَـُٔوسٌۭ قَنُوطٌۭ
- (43:74) [listed for 87:17] إِنَّ ٱلْمُجْرِمِينَ فِى عَذَابِ جَهَنَّمَ خَٰلِدُونَ
- (53:20) [listed for 87:17] وَمَنَوٰةَ ٱلثَّالِثَةَ ٱلْأُخْرَىٰٓ
- (56:40) [listed for 87:17] وَثُلَّةٌۭ مِّنَ ٱلْءَاخِرِينَ
- (64:9) [listed for 87:17] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (70:21) [listed for 87:17] وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا
- (75:6) [listed for 87:17] يَسْـَٔلُ أَيَّانَ يَوْمُ ٱلْقِيَٰمَةِ
- (91:10) [listed for 87:17] وَقَدْ خَابَ مَن دَسَّىٰهَا

## neighbours: within two ayat of a passage the commentary cites (74)

- (2:84) [next to 2:86] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ لَا تَسْفِكُونَ دِمَآءَكُمْ وَلَا تُخْرِجُونَ أَنفُسَكُم مِّن دِيَٰرِكُمْ ثُمَّ أَقْرَرْتُمْ وَأَنتُمْ تَشْهَدُونَ
- (2:85) [next to 2:86] ثُمَّ أَنتُمْ هَٰٓؤُلَآءِ تَقْتُلُونَ أَنفُسَكُمْ وَتُخْرِجُونَ فَرِيقًۭا مِّنكُم مِّن دِيَٰرِهِمْ تَظَٰهَرُونَ عَلَيْهِم بِٱلْإِثْمِ وَٱلْعُدْوَٰنِ وَإِن يَأْتُوكُمْ أُسَٰرَىٰ تُفَٰدُوهُمْ وَهُوَ مُحَرَّمٌ عَلَيْكُمْ إِخْرَاجُهُمْ ۚ أَفَتُؤْمِنُونَ بِبَعْضِ ٱلْكِتَٰبِ وَتَكْفُرُونَ بِبَعْضٍۢ ۚ فَمَا جَزَآءُ مَن يَفْعَلُ ذَٰلِكَ مِنكُمْ إِلَّا خِزْىٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَيَوْمَ ٱلْقِيَٰمَةِ يُرَدُّونَ إِلَىٰٓ أَشَدِّ ٱلْعَذَابِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (2:87) [next to 2:86] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَقَفَّيْنَا مِنۢ بَعْدِهِۦ بِٱلرُّسُلِ ۖ وَءَاتَيْنَا عِيسَى ٱبْنَ مَرْيَمَ ٱلْبَيِّنَٰتِ وَأَيَّدْنَٰهُ بِرُوحِ ٱلْقُدُسِ ۗ أَفَكُلَّمَا جَآءَكُمْ رَسُولٌۢ بِمَا لَا تَهْوَىٰٓ أَنفُسُكُمُ ٱسْتَكْبَرْتُمْ فَفَرِيقًۭا كَذَّبْتُمْ وَفَرِيقًۭا تَقْتُلُونَ
- (2:88) [next to 2:86] وَقَالُوا۟ قُلُوبُنَا غُلْفٌۢ ۚ بَل لَّعَنَهُمُ ٱللَّهُ بِكُفْرِهِمْ فَقَلِيلًۭا مَّا يُؤْمِنُونَ
- (2:178) [next to 2:180] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُتِبَ عَلَيْكُمُ ٱلْقِصَاصُ فِى ٱلْقَتْلَى ۖ ٱلْحُرُّ بِٱلْحُرِّ وَٱلْعَبْدُ بِٱلْعَبْدِ وَٱلْأُنثَىٰ بِٱلْأُنثَىٰ ۚ فَمَنْ عُفِىَ لَهُۥ مِنْ أَخِيهِ شَىْءٌۭ فَٱتِّبَاعٌۢ بِٱلْمَعْرُوفِ وَأَدَآءٌ إِلَيْهِ بِإِحْسَٰنٍۢ ۗ ذَٰلِكَ تَخْفِيفٌۭ مِّن رَّبِّكُمْ وَرَحْمَةٌۭ ۗ فَمَنِ ٱعْتَدَىٰ بَعْدَ ذَٰلِكَ فَلَهُۥ عَذَابٌ أَلِيمٌۭ
- (2:179) [next to 2:180] وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تَتَّقُونَ
- (2:181) [next to 2:180] فَمَنۢ بَدَّلَهُۥ بَعْدَمَا سَمِعَهُۥ فَإِنَّمَآ إِثْمُهُۥ عَلَى ٱلَّذِينَ يُبَدِّلُونَهُۥٓ ۚ إِنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (2:182) [next to 2:180] فَمَنْ خَافَ مِن مُّوصٍۢ جَنَفًا أَوْ إِثْمًۭا فَأَصْلَحَ بَيْنَهُمْ فَلَآ إِثْمَ عَلَيْهِ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (11:114) [next to 11:116] وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ وَزُلَفًۭا مِّنَ ٱلَّيْلِ ۚ إِنَّ ٱلْحَسَنَٰتِ يُذْهِبْنَ ٱلسَّيِّـَٔاتِ ۚ ذَٰلِكَ ذِكْرَىٰ لِلذَّٰكِرِينَ
- (11:115) [next to 11:116] وَٱصْبِرْ فَإِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
- (11:117) [next to 11:116] وَمَا كَانَ رَبُّكَ لِيُهْلِكَ ٱلْقُرَىٰ بِظُلْمٍۢ وَأَهْلُهَا مُصْلِحُونَ
- (11:118) [next to 11:116] وَلَوْ شَآءَ رَبُّكَ لَجَعَلَ ٱلنَّاسَ أُمَّةًۭ وَٰحِدَةًۭ ۖ وَلَا يَزَالُونَ مُخْتَلِفِينَ
- (14:42) [next to 14:44] وَلَا تَحْسَبَنَّ ٱللَّهَ غَٰفِلًا عَمَّا يَعْمَلُ ٱلظَّٰلِمُونَ ۚ إِنَّمَا يُؤَخِّرُهُمْ لِيَوْمٍۢ تَشْخَصُ فِيهِ ٱلْأَبْصَٰرُ
- (14:43) [next to 14:44] مُهْطِعِينَ مُقْنِعِى رُءُوسِهِمْ لَا يَرْتَدُّ إِلَيْهِمْ طَرْفُهُمْ ۖ وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ
- (14:45) [next to 14:44] وَسَكَنتُمْ فِى مَسَٰكِنِ ٱلَّذِينَ ظَلَمُوٓا۟ أَنفُسَهُمْ وَتَبَيَّنَ لَكُمْ كَيْفَ فَعَلْنَا بِهِمْ وَضَرَبْنَا لَكُمُ ٱلْأَمْثَالَ
- (14:46) [next to 14:44] وَقَدْ مَكَرُوا۟ مَكْرَهُمْ وَعِندَ ٱللَّهِ مَكْرُهُمْ وَإِن كَانَ مَكْرُهُمْ لِتَزُولَ مِنْهُ ٱلْجِبَالُ
- (16:94) [next to 16:96] وَلَا تَتَّخِذُوٓا۟ أَيْمَٰنَكُمْ دَخَلًۢا بَيْنَكُمْ فَتَزِلَّ قَدَمٌۢ بَعْدَ ثُبُوتِهَا وَتَذُوقُوا۟ ٱلسُّوٓءَ بِمَا صَدَدتُّمْ عَن سَبِيلِ ٱللَّهِ ۖ وَلَكُمْ عَذَابٌ عَظِيمٌۭ
- (16:97) [next to 16:96] مَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَلَنُحْيِيَنَّهُۥ حَيَوٰةًۭ طَيِّبَةًۭ ۖ وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (16:98) [next to 16:96] فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ فَٱسْتَعِذْ بِٱللَّهِ مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ
- (17:16) [next to 17:18] وَإِذَآ أَرَدْنَآ أَن نُّهْلِكَ قَرْيَةً أَمَرْنَا مُتْرَفِيهَا فَفَسَقُوا۟ فِيهَا فَحَقَّ عَلَيْهَا ٱلْقَوْلُ فَدَمَّرْنَٰهَا تَدْمِيرًۭا
- (17:17) [next to 17:18] وَكَمْ أَهْلَكْنَا مِنَ ٱلْقُرُونِ مِنۢ بَعْدِ نُوحٍۢ ۗ وَكَفَىٰ بِرَبِّكَ بِذُنُوبِ عِبَادِهِۦ خَبِيرًۢا بَصِيرًۭا
- (17:20) [next to 17:18] كُلًّۭا نُّمِدُّ هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ مِنْ عَطَآءِ رَبِّكَ ۚ وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا
- (18:43) [next to 18:45] وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا
- (18:47) [next to 18:45] وَيَوْمَ نُسَيِّرُ ٱلْجِبَالَ وَتَرَى ٱلْأَرْضَ بَارِزَةًۭ وَحَشَرْنَٰهُمْ فَلَمْ نُغَادِرْ مِنْهُمْ أَحَدًۭا
- (18:48) [next to 18:46] وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا لَّقَدْ جِئْتُمُونَا كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۭ ۚ بَلْ زَعَمْتُمْ أَلَّن نَّجْعَلَ لَكُم مَّوْعِدًۭا
- (20:69) [next to 20:71] وَأَلْقِ مَا فِى يَمِينِكَ تَلْقَفْ مَا صَنَعُوٓا۟ ۖ إِنَّمَا صَنَعُوا۟ كَيْدُ سَٰحِرٍۢ ۖ وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ
- (20:70) [next to 20:71] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (20:74) [next to 20:72] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:75) [next to 20:73] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (20:122) [next to 20:124] ثُمَّ ٱجْتَبَٰهُ رَبُّهُۥ فَتَابَ عَلَيْهِ وَهَدَىٰ
- (20:123) [next to 20:124] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (20:125) [next to 20:124] قَالَ رَبِّ لِمَ حَشَرْتَنِىٓ أَعْمَىٰ وَقَدْ كُنتُ بَصِيرًۭا
- (20:126) [next to 20:124] قَالَ كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ
- (20:128) [next to 20:127] أَفَلَمْ يَهْدِ لَهُمْ كَمْ أَهْلَكْنَا قَبْلَهُم مِّنَ ٱلْقُرُونِ يَمْشُونَ فِى مَسَٰكِنِهِمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:129) [next to 20:127] وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَكَانَ لِزَامًۭا وَأَجَلٌۭ مُّسَمًّۭى
- (20:133) [next to 20:131] وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ
- (20:134) [next to 20:132] وَلَوْ أَنَّآ أَهْلَكْنَٰهُم بِعَذَابٍۢ مِّن قَبْلِهِۦ لَقَالُوا۟ رَبَّنَا لَوْلَآ أَرْسَلْتَ إِلَيْنَا رَسُولًۭا فَنَتَّبِعَ ءَايَٰتِكَ مِن قَبْلِ أَن نَّذِلَّ وَنَخْزَىٰ
- (28:58) [next to 28:60] وَكَمْ أَهْلَكْنَا مِن قَرْيَةٍۭ بَطِرَتْ مَعِيشَتَهَا ۖ فَتِلْكَ مَسَٰكِنُهُمْ لَمْ تُسْكَن مِّنۢ بَعْدِهِمْ إِلَّا قَلِيلًۭا ۖ وَكُنَّا نَحْنُ ٱلْوَٰرِثِينَ
- (28:59) [next to 28:60] وَمَا كَانَ رَبُّكَ مُهْلِكَ ٱلْقُرَىٰ حَتَّىٰ يَبْعَثَ فِىٓ أُمِّهَا رَسُولًۭا يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِنَا ۚ وَمَا كُنَّا مُهْلِكِى ٱلْقُرَىٰٓ إِلَّا وَأَهْلُهَا ظَٰلِمُونَ
- (28:62) [next to 28:60] وَيَوْمَ يُنَادِيهِمْ فَيَقُولُ أَيْنَ شُرَكَآءِىَ ٱلَّذِينَ كُنتُمْ تَزْعُمُونَ
- (29:62) [next to 29:64] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥٓ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (29:63) [next to 29:64] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
- (29:65) [next to 29:64] فَإِذَا رَكِبُوا۟ فِى ٱلْفُلْكِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ إِذَا هُمْ يُشْرِكُونَ
- (29:66) [next to 29:64] لِيَكْفُرُوا۟ بِمَآ ءَاتَيْنَٰهُمْ وَلِيَتَمَتَّعُوا۟ ۖ فَسَوْفَ يَعْلَمُونَ
- (42:34) [next to 42:36] أَوْ يُوبِقْهُنَّ بِمَا كَسَبُوا۟ وَيَعْفُ عَن كَثِيرٍۢ
- (42:35) [next to 42:36] وَيَعْلَمَ ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِنَا مَا لَهُم مِّن مَّحِيصٍۢ
- (42:37) [next to 42:36] وَٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ وَإِذَا مَا غَضِبُوا۟ هُمْ يَغْفِرُونَ
- (42:38) [next to 42:36] وَٱلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَمْرُهُمْ شُورَىٰ بَيْنَهُمْ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (53:23) [next to 53:25] إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ وَمَا تَهْوَى ٱلْأَنفُسُ ۖ وَلَقَدْ جَآءَهُم مِّن رَّبِّهِمُ ٱلْهُدَىٰٓ
- (53:24) [next to 53:25] أَمْ لِلْإِنسَٰنِ مَا تَمَنَّىٰ
- (53:26) [next to 53:25] ۞ وَكَم مِّن مَّلَكٍۢ فِى ٱلسَّمَٰوَٰتِ لَا تُغْنِى شَفَٰعَتُهُمْ شَيْـًٔا إِلَّا مِنۢ بَعْدِ أَن يَأْذَنَ ٱللَّهُ لِمَن يَشَآءُ وَيَرْضَىٰٓ
- (53:27) [next to 53:25] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ لَيُسَمُّونَ ٱلْمَلَٰٓئِكَةَ تَسْمِيَةَ ٱلْأُنثَىٰ
- (55:24) [next to 55:26] وَلَهُ ٱلْجَوَارِ ٱلْمُنشَـَٔاتُ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ
- (55:25) [next to 55:26] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:28) [next to 55:26] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:29) [next to 55:27] يَسْـَٔلُهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ كُلَّ يَوْمٍ هُوَ فِى شَأْنٍۢ
- (75:14) [next to 75:16] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
- (75:15) [next to 75:16] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
- (75:18) [next to 75:16] فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ
- (75:19) [next to 75:17] ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ
- (75:22) [next to 75:20] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
- (75:23) [next to 75:21] إِلَىٰ رَبِّهَا نَاظِرَةٌۭ
- (92:10) [next to 92:12] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:11) [next to 92:12] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (92:14) [next to 92:12] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:15) [next to 92:13] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (93:1) [next to 93:3] وَٱلضُّحَىٰ
- (93:2) [next to 93:3] وَٱلَّيْلِ إِذَا سَجَىٰ
- (93:6) [next to 93:4] أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ
- (93:7) [next to 93:5] وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ
- (100:6) [next to 100:8] إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- (100:7) [next to 100:8] وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- (100:9) [next to 100:8] ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- (100:10) [next to 100:8] وَحُصِّلَ مَا فِى ٱلصُّدُورِ

