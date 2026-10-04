Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:3; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_3.reading.tr.md (prose paragraphs numbered) =====
## Üç "O ki" ve nesnesi olmayan iki fiil

[¶1] Sure Peygamber'e verilen bir emirle açılır: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Ardından bu Rabbi tanıtan üç cümle gelir ve her biri "O ki" diye başlar. İkinci ayet {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:O ki yarattı ve düzene koydu, source:87:2} der. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:O ki otlağı çıkardı, source:87:4} der. Ortadaki ayet üç kelimedir: {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:O ki ölçüyü koydu, ardından yol gösterdi, source:87:3}. Baştaki "ve" bu ayeti bir öncekinin devamı olarak değil, aynı Rabbin ayrı bir yüzü olarak getirir.

[¶2] İki fiilin de nesnesi yoktur. Arapça bu fiillerle genellikle neyin ölçüldüğünü ve kime yol gösterildiğini söyler. Burada söylemez. Bu bir eksiklik değil, bir genişliktir. İkinci ayette yaratılan neyse, burada ölçülen ve yol gösterilen de odur, yani her şey. Nesne ancak dördüncü ayette görünür ve o da otlaktır. Üç cümle böylece genelden somuta iner. Kur'an başka bir yerde bu sessizliği doldurur. Kendi yaratılışına nankörlük eden insana sorduğu soruda Allah önce {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddarah, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Orada ölçülen insandır, gösterilen de yoldur. Bizim ayetimiz bu ikisini adlandırmadığı için hükmü her varlığa yayılır.

[¶3] İki fiil arasındaki "fe" bağlacı ince bir iş görür. İkinci olayın birincinin hemen ardından ve onun sonucu olarak geldiğini söyler. Ölçü koymakla yol göstermek arasında bir aralık yoktur. Yol, ölçünün devamıdır.

[¶4] Türkçe bu iki kökü iyi tanır, ama daralmış hâlleriyle. "Takdir" bugün çoğunlukla beğenmek demektir, "kader" ise alına yazılmış, değişmez bir yazgı gibi duyulur. "Hidayet" de birinin imana gelmesiyle sınırlanmıştır. Ayetteki fiiller bunlardan daha somut ve daha geniştir. قدّر önce bir insanın işidir. Bir şeyi hazırladığında Araplar {ar:قدرت الشيء أي هيأته, tr:kadartu'ş-şey'e ey heyye'tuh, gloss:onu ölçtüm, yani hazırladım, source:"ق د ر,B005"} der, bir şey birinin kullanımına hazır hâle geldiğinde de {ar:تقدر له الشيء أي تهيأ, tr:tekaddera lehu'ş-şey'u ey teheyye'e, gloss:o şey onun için hazır oldu, source:"ق د ر,B005"} derlerdi. Fiil bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmeyi de anlatır: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını düşünüp tartmak, source:"ق د ر,B005"}. Bu tanımdaki "düzlemek" kelimesi, ikinci ayetin "düzene koydu" fiiliyle aynı köktendir. İki kök bir değildir, ama Arapça birini anlatırken ötekine başvurur. Ölçmenin özü de miktarı açığa çıkarmaktır: {ar:القدر والتقدير تبيين كمية الشيء, tr:el-kadru ve't-takdîru tebyînu kemmiyyeti'ş-şey', gloss:ölçü ve ölçmek, bir şeyin ne kadar olduğunu ortaya koymaktır, source:"ق د ر,B001"}. Takdir burada beğenmek değil, biçmektir: bir şeyin ne kadar olacağını belirleyip onu işine hazırlamak.

[¶5] Bu fiilin somut kullanımları ayetteki anlamın yerine geçmez. Onun yanında duyulur ve ona bir el ile bir malzeme kazandırır. En açık örnek demir örgüdür. Kur'an, Davud'a demirin yumuşatıldığını {source:34:10} ve ona bol zırhlar yapması, örgüde ölçüyü tutması emredildiğini anlatır {source:34:11}. Bu söz {ar:قدر في السرد أي أحكمه, tr:kaddir fi's-serdi ey ahkimhu, gloss:örgüde ölçüyü tut, yani onu sağlam kur, source:"ق د ر,B005"} diye açıklanır. Zırh birbirine geçirilmiş halkalardan örülür. Halkalar ve geçmeler birbirine uygun ölçüde olmazsa örgü ya açılır ya da tutmaz. Ölçü burada süs değil, nesnenin işini görebilmesinin şartıdır. Bir şey kendi ölçüsüne tam oturduğunda da {ar:جاء على قدره, tr:câe alâ kaderih, gloss:tam ölçüsünce geldi, source:"ق د ر,B006"} denir.

## Ölçünün içindeki varış ve son

[¶6] Bir şeyin kaderi, o şeyin kendi olarak nereye kadar uzandığıdır: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer, özü ve sonu, source:"ق د ر,B001"}. Bu tanımda üç şey birlikte durur: varış, öz ve son. Ölçü yalnız boy ve hacim değildir, süreyi de içine alır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve bir vadesi vardır, source:"ق د ر,B001"}. Fiil Allah'a nispet edildiğinde de aynı yapı korunur: {ar:قضاء الله تعالى الأشياء على مبالغها ونهاياتها, tr:kadâu'llâhi teâlâ el-eşyâe alâ mebâliğihâ ve nihâyâtihâ, gloss:Allah'ın her şeyi varacağı yere ve sonuna göre hükme bağlaması, source:"ق د ر,B002"}. Kur'an bunu genel bir cümleyle de söyler: {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49}. "Ölçüyü koydu" demek, her şeye nereye kadar varacağını ve nerede duracağını vermek demektir.

[¶7] Sure bunu hemen gösterir. Dördüncü ayette otlak çıkar, beşinci ayette {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-cealehû ğuŝâen ahvâ, gloss:sonra onu kararmış bir çer çöp yaptı, source:87:5} denir. Otlağın ölçüsünde yeşerdiği gün de vardır, kuruyup karardığı gün de. Ölçünün bir sonu olduğunu bilmek, bu iki ayeti bir çelişki olarak değil, tek bir ölçünün iki ucu olarak okutur. Kur'an aynı şeyi ay için de söyler. Allah ayı konaklara göre ölçmüştür, ay sonunda kuruyup kıvrılmış eski bir hurma salkımı sapı gibi geri döner {source:36:39}. Ölçülen her şey bir yerden geçer ve ölçüsünün ucuna varır. Otlağı besleyen yağmur için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-matar bi-mikdâr, gloss:yağmur belli bir ölçüyle iner, source:"ق د ر,B001"} denirdi.

[¶8] Ölçü vermek sınır koymaktır, çünkü sınırı olmayan bir şeyin ölçüsü olmaz. Aynı fiil bir kalıpta açıkça daraltmak anlamına gelir: {ar:قدرت عليه الشيء ضيقته, tr:kadartu aleyhi'ş-şey'e dayyaktuh, gloss:o şeyi ona dar tuttum, source:"ق د ر,B004"}, {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rizkuhû ey duyyika aleyh, gloss:rızkı ölçülen, yani rızkı daraltılan kimse, source:"ق د ر,B004"}. Kur'an insanın bu sınırı nasıl yanlış okuduğunu anlatır. Rabbi onu bollukla sınadığında insan "Rabbim beni ağırladı" der, rızkını ölçüp daralttığında ise "Rabbim beni küçük düşürdü" der {source:89:16}. Hemen ardından gelen ayet "Hayır!" diye başlar {source:89:17}. Üçüncü ayetin ışığında ölçü bir aşağılama değildir. Bir şey yola çıkarılmadan önce ona verilen biçimdir.

## Önden giden: boyun, temren, değnek

[¶9] "Hidayet" kelimesinin somut kullanımlarında yol göstermek öne geçmektir. Araplar her şeyin ilk ve öndeki bölümüne {ar:الهادي من كل شيء أوله, tr:el-hâdî min kulli şey'in evveluh, gloss:her şeyin hâdîsi onun ilk bölümüdür, source:"ه د ي,B003"} derlerdi. Atlar için {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelu ra'îl, gloss:atların hevâdîsi boyunları ya da ilk bölükleridir, source:"ه د ي,B003"} denirdi. Koşan bir atta önce boyun uzanır, baş hangi yana dönerse gövde oraya gider. Koyunun boynuna da {ar:هادية الشاة الرقبة, tr:hâdiyetu'ş-şâti'r-rakabe, gloss:koyunun hâdiyesi boynudur, source:"ه د ي,B003"} adı verilir. Okun demir ucu {ar:هادي السهم نصله, tr:hâdi's-sehmi nasluh, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"} diye anılır. Temren gövdenin önünden gider, hedefe ilk o değer ve gövdeyi ardından götürür. Değneğe de aynı ad verilir: {ar:الهادية العصا لأنها تتقدم ممسكها, tr:el-hâdiyetu'l-asâ li-ennehâ tetekaddemu mumsikehâ, gloss:değneğe hâdiye denir, çünkü tutanın önünden gider, source:"ه د ي,B003"}. Öne uzatılan değnek, yürüyenin ayağından önce yere ve engele değer. Kılavuz da bu yüzden aynı adı alır: {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlu yusemmâ hâdiyen li-tekaddumih, gloss:kılavuza önden gittiği için hâdî denir, source:"ه د ي,B003"}.

[¶10] Yol göstermenin tanımı da bu resme uyar: {ar:التقدم للإرشاد, tr:et-tekaddumu li'l-irşâd, gloss:doğru yolu göstermek için öne geçmek, source:"ه د ي,B001"}. Bir başka ifadede de {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîka ve'l-beyte hidâyeten ey arraftuh, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"} denir. Hidayet uzaktan parmakla işaret etmek değildir. Önden gidip hem yolu hem de varılacak evi tanıtmaktır.

[¶11] Bu resim ayetin sıralamasına yeni bir ışık tutar. Bir şey önce ölçülür, sonra ona bir ön, bir yön verilir. Yönü olmayan iş için Araplar {ar:ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة, tr:leyse li-hâẕe'l-emri hidyetun ve lâ kıbletun ve lâ dibratun ve lâ vichetun, gloss:bu işin ne yönü ne önü ne arkası ne de çevrildiği bir yüzü var, source:"ه د ي,B002"} derlerdi. Bir kimsenin tuttuğu yol ve gidiş de aynı kelimeyle söylenir: {ar:هدية فلان وهديه أي طريقته, tr:hidyetu fulânin ve hedyuhû ey tarîkatuh, gloss:falancanın hidyesi ve hedyi, onun tuttuğu yoldur, source:"ه د ي,B002"}. Ölçülüp de yolu gösterilmeyen bir şey, başı sonu belli olmayan bir iş gibi kalırdı. Ayet ölçüden hemen sonra yolu getirerek bunu önler. İkinci ayetin "yarattı" ve "düzene koydu" fiilleri ölçülüp doğrultulmuş bir oku hatırlatır, ve bu ayetin fiili o okun ucunu alıp hedefe dönmesi gibi duyulur. Yaban sürülerinin öncüleri için de {ar:هوادي الوحش متقدماتها الهادية لغيرها, tr:hevâdi'l-vahşi mutekaddimâtuhe'l-hâdiyetu li-ğayrihâ, gloss:yaban hayvanlarının hevâdîsi, ötekilere yol gösteren öndekileridir, source:"ه د ي,B003"} denir. Bu söz, birinci ayetteki Rab ile dördüncü ayetteki otlak arasına bir sürünün önünü yerleştirir.

[¶12] Kur'an değneği bir peygamberin elinde de gösterir. Musa ateşin başında seçildikten sonra Allah ona sağ elindekinin ne olduğunu sorar {source:20:17}. Musa bunun kendi değneği olduğunu, ona dayandığını, onunla koyunlarına yaprak silkelediğini ve onda başka işleri de bulunduğunu söyler {source:20:18}. O ayette hidayetin kökü geçmez. Buradaki bağ bir benzetmedir, kök birliği değildir. Yine de Arapçanın değneğe "önden giden" adını vermesi ile Musa'nın değneği hem dayanak hem sürüyü besleme aracı olarak anlatması aynı nesnenin iki yüzüdür.

[¶13] Kökün iki kullanımı daha hidayeti bir yürüyüş olarak duyurur. Güçsüz biri iki kişinin arasında onlara yaslanarak yürüdüğünde {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yuhâdî beyne'sneyni iẕâ kâne yemşî beynehumâ mu'temiden aleyhimâ min da'fihî ve temâyulih, gloss:zayıflığından ve sendelemesinden iki kişinin arasında onlara dayanarak yürür, source:"ه د ي,B008"} denir. Telaşsız, sakin bir gidiş için de {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusri' isrâa'l-munhezimi ve lâkin alâ sukûnin ve hedyin hasen, gloss:bozguna uğrayan gibi koşmadı, sakin ve güzel bir gidişle yürüdü, source:"ه د ي,B010"} söylenirdi. Bu kullanımlarda yol gösteren yalnızca önde değildir, yanında yürüyenle bir yürüyüşü de paylaşır. Sekizinci ayetin "kolaylaştıracağız" fiili ile on birinci ayetin "uzak durur" fiili bu yol resmini sürdürür.

## Armağan, gelin, kurbanlık: varılacak yere ulaştırmak

[¶14] Türkçedeki "hediye" ile "hidayet" aynı Arapça kökten gelir. Armağan için {ar:الهدية ما أهديت إلى ذي مودة من بر, tr:el-hediyyetu mâ ehdeyte ilâ ẕî meveddetin min birr, gloss:hediye, sevgi beslediğin birine iyilik olarak gönderdiğin şeydir, source:"ه د ي,B004"} denir. Hediyeyi hidayete bağlayan bir incelik vardır. Yol göstermek için {ar:الهداية دلالة بلطف, tr:el-hidâyetu delâletun bi-lutf, gloss:hidayet incelikle yol göstermektir, source:"ه د ي,B001"} denir, armağan için de {ar:الهدية مختصة باللطف, tr:el-hediyyetu muhtassatun bi'l-lutf, gloss:hediye inceliğe özgüdür, source:"ه د ي,B004"}. İkisi de karşıdakini zorlamadan, onun gönlünü gözeterek ona bir şey ulaştırır.

[¶15] Aynı fiil iki somut ulaştırmayı daha adlandırır. Gelini eşinin evine götürmek {ar:هديت العروس إلى زوجها, tr:hedeytu'l-arûse ilâ zevcihâ, gloss:gelini eşine götürdüm, source:"ه د ي,B006"} diye söylenirdi. Kutsal bölgeye gönderilen hayvana da {ar:الهدي ما يهدى إلى الحرم من النعم, tr:el-hedyu mâ yuhdâ ile'l-harami mine'n-ne'am, gloss:hedy, harem bölgesine gönderilen hayvandır, source:"ه د ي,B005"} denir. Bu hayvanın yolculuğu {ar:حتى يبلغ الهدى محله, tr:hattâ yebluğa'l-hedyu mahilleh, gloss:kurbanlık varacağı yere ulaşıncaya kadar, source:"ه د ي,B005"} ve {ar:هديا بالغ الكعبة, tr:hedyen bâliğa'l-Ka'be, gloss:Kâbe'ye ulaşan bir kurbanlık, source:"ه د ي,B005"} diye anlatılır. Her üç kullanımda da bir şey, varması gereken yere götürülür.

[¶16] Burada ayetin iki fiili birbirine kilitlenir. Ölçünün tanımında {ar:مبلغ الشيء, tr:mebleğu'ş-şey', gloss:bir şeyin vardığı yer, source:"ق د ر,B001"} vardı. Kurbanlığın yolculuğu da "ulaşıncaya kadar" diye anlatılır. İki ifade aynı "ulaşmak" fiilinden türemiştir. Bu, iki kökün aynı olduğunu göstermez. Yalnızca iki fiili tanımlayan sözlerin aynı noktada buluştuğunu gösterir. Ayetin sırası bu buluşmayı kendiliğinden kurar. Ölçmek, bir şeyin nereye kadar varacağını belirlemektir. Yol göstermek ise onu oraya götürmektir. Biri hedefi koyar, öteki o hedefe ulaştırır.

## Ölçülen şey yol gösterir: gök, yer ve arı

[¶17] Kur'an bu iki fiili gökte yan yana kullanır. Allah'ı tanıtan bir bölümde önce O'nun tohumu ve çekirdeği yardığı söylenir {source:6:95}. Ardından sabahı yardığı, geceyi dinlenme zamanı, güneşle ayı da hesap ölçüsü yaptığı anlatılır ve "Bu, aziz ve her şeyi bilen olanın takdiridir" denir {source:6:96}. Hemen sonraki ayette yıldızları, kara ile denizin karanlıklarında onlarla yolunuzu bulasınız diye sizin için kıldığı söylenir {source:6:97}. Ölçülen gök cisimleri yolcuya kılavuz olur. Bizim ayetimizde ölçüyle yol göstermek iki ayrı iştir. Orada ölçülen şeyin kendisi başkasına yolu gösterir.

[¶18] Başka bir yerde Kur'an, müşriklerin bile göğü ve yeri aziz ve her şeyi bilen olanın yarattığını söyleyeceklerini bildirir {source:43:9}. Sonra bu Rabbi, bizim suremizdekine çok benzeyen bir "O ki" dizisiyle anlatır. Yeri size beşik yapan ve yolunuzu bulasınız diye onda size yollar açan O'dur {source:43:10}. Gökten belli bir ölçüyle su indirip onunla ölü bir toprağı dirilten O'dur {source:43:11}. Bütün çiftleri yaratan da O'dur {source:43:12}. Yol bulmak, ölçüyle inen su ve yeşeren toprak orada da art arda gelir. Bizim surede de ölçüyü koyup yol gösterenin hemen ardından otlağı çıkaran gelir. Yolculukta ölçü bir yolun uzunluğu olarak da duyulur. İki yurt arasındaki mesafe için {ar:بين أرضك وأرض فلان ليلة قادرة, tr:beyne arzike ve arzi fulânin leyletun kâdira, gloss:senin toprağınla falancanınki arasında yol alması kolay bir gecelik mesafe var, source:"ق د ر,B006"} denirdi. Bu sözde ölçülü olan yol, yolcuya kolay da gelir.

[¶19] Ayetin fiillerinin nesnesi olmadığı için hüküm insanın ötesine geçer. Kur'an bir hayvanın yolunu da anlatır. Rabbin arıya, dağlardan, ağaçlardan ve insanların kurdukları çardaklardan kendine evler edinmesini vahyetmiştir {source:16:68}. Ardından ona her türlü meyveden yemesini ve Rabbinin kendisi için boyun eğdirilmiş yollarına girmesini söylemiştir. Arının karnından da renkleri türlü türlü bir içecek çıkar {source:16:69}. Bu ayetlerde hidayetin kökü geçmez, ama anlatılan iş aynıdır. Yaratılışı ölçülmüş bir varlığa, o ölçüye uygun bir yol gösterilir. Arı kendi yoluna girer ve meyveden bal çıkarır. Ölçü ile yol, onun yararlı olmasının iki şartıdır.

## Musa'nın cevabı, İbrahim'in sözü

[¶20] Surenin son ayeti, burada söylenenlerin {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi İbrâhîme ve Mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19} içinde de bulunduğunu bildirir. Kur'an o sayfaların metnini vermez. Ama başka yerlerde, bu iki peygamberin ağzından üçüncü ayete çok yakın sözler aktarır.

[¶21] Firavun, Musa ile kardeşine "Sizin Rabbiniz kim, ey Musa?" diye sorar {source:20:49}. Musa şöyle cevap verir: Rabbimiz, her şeye yaratılışını veren ve sonra yol gösterendir. Bu cevabın son fiili, bizim ayetimizin fiilinin kendisidir {source:20:50}. Firavun önceki nesillerin ne olduğunu sorunca Musa, onların bilgisinin Rabbinin katında bir yazıda olduğunu söyler ve "Rabbim ne şaşırır ne de unutur" der {source:20:52}. Bu sözdeki "şaşırmak" yol göstermenin karşıtıdır. "Unutmak" ise altıncı ayette Peygamber'e verilen {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6} sözünün fiilidir. Musa ardından yeri beşik yapan, onda yollar açan ve gökten su indirip türlü bitkiler çıkaran Rabbi anlatır {source:20:53}. Sözünü {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ, tr:kulû ver'av en'âmekum inne fî ẕâlike le-âyâtin li-uli'n-nuhâ, gloss:yiyin ve hayvanlarınızı otlatın; bunda akıl sahipleri için işaretler vardır, source:20:54} diye bağlar. Musa'nın tek cevabı surenin ikinci ayetinden altıncı ayetine kadar olan sırayı izler: yaratılış, yol gösterme, yollar, su ve otlak, unutmama.

[¶22] Aynı Musa, Firavun'un karşısına çıkmadan önce yolunu kaybetmiş bir yolcudur. Gece ailesiyle giderken uzakta bir ateş görür ve {ar:ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:imkuŝû innî ânestu nâran leallî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:burada kalın, ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında yol gösterecek birini bulurum, source:20:10} der. Buradaki "hudâ" yolcunun aradığı kılavuzdur. Musa'nın ateşin başında bulduğu ise başka türlü bir hidayettir: {ar:وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ, tr:ve ene'htertuke fe'stemi' li-mâ yûhâ, gloss:seni ben seçtim, vahyolunanı dinle, source:20:13}. Yol soran adam, Rabbin yol gösterdiğini Firavun'a anlatan elçi olur. Uzaktan görülen ateşin sahnesi ise on ikinci ayetin "ateş" kelimesine dayanır.

[¶23] İbrahim aynı ikiliyi birinci tekil şahısla söyler. Kavmine ve atalarına taptıkları putları sorar, onların kendisine düşman olduğunu, yalnız âlemlerin Rabbinin dost olduğunu söyler {source:26:77}. Sonra o Rabbi şöyle tanıtır: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Sonraki ayetlerde de kendisini yediren, içiren ve hastalandığında iyileştiren Rabbi anlatır {source:26:79}. İbrahim'in sözünde hem nesne vardır hem zaman değişir: "beni" yaratan, "bana" yol gösteren, hem de şimdi ve sürekli olarak. Üçüncü ayetin geçmiş zamanda ve herkes için söylediği şey, İbrahim'in ağzında süren, kişisel bir ilişkiye dönüşür. Sure de aynı yolu izler. Altıncı ayetten sonra Rabbin yol göstermesi doğrudan Peygamber'e yönelir: ona okutulacak, o unutmayacak, en kolaya kolaylaştırılacaktır.

## Gösterilen yol ve tutulan yol

[¶24] Arapça yol gösterilmekle yolu tutmayı iki ayrı fiille söyler: {ar:هدي فاهتدى, tr:hudiye fe'htedâ, gloss:ona yol gösterildi, o da yolu tuttu, source:"ه د ي,B001"}. Birinci fiil gösterenin işidir, ikincisi yolcunun. Üçüncü ayet yalnızca birinciyi söyler. İkinciyi surenin geri kalanı insanlar arasında bölüştürür. Sekizinci ayetteki {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana kolaylaştıracağız, source:87:8} sözüyle yol gösterilen Peygamber, dokuzuncu ayette {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt fayda verirse, source:87:9} emrini alır. Önden giden, kendisi de bir başkasının önüne geçer. Ardından yol ikiye ayrılır: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:Rabbinden korkan öğüt alacaktır, source:87:10} ve {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ise ondan uzak duracaktır, source:87:11}. Gösterilen yol aynıdır. Biri o yolu tutar, öteki yanından geçer.

[¶25] Kur'an bu ayrımı başka yerlerde de açıkça söyler. İnsan için {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhu's-sebîle immâ şâkiran ve immâ kefûrâ, gloss:biz ona yolu gösterdik; ister şükreden olsun ister nankör, source:76:3} der. Bir başka yerde {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhu'n-necdeyn, gloss:ona iki yüksek yolu gösterdik, source:90:10} der. Verenlerle cimrilik edenleri ayırdığı bir surede de {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. Yol göstermek Rabbin işidir ve eksiksiz yapılmıştır. Yolu tutmak ise yolcunun işidir. Kökün incelikle yol göstermek anlamı da buraya oturur. Hidayet zorla sürüklemek değildir.

[¶26] Bu yüzden her namazda okunan Fatiha'nın isteği, bu ayetin yanında yeni bir anlam kazanır: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-mustakîm, gloss:bizi dosdoğru yola ilet, source:1:6}. Üçüncü ayette nesnesi olmayan fiil burada iki nesne alır: "biz" ve "dosdoğru yol". Ayet Rabbin yaptığını genel olarak haber verir, namaz kılan ise aynı şeyi kendisi için ister. On beşinci ayette kurtuluşa eren kişi {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kılandır, source:87:15}. Namazında bu isteği dile getiren kişi, "yol gösterdi" sözünü kendi yolculuğuna çevirmiş olur. Kur'an bu isteğin cevabını Adem'in yere indirilişinde verir: {ar:فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ, tr:fe-meni't-tebea hudâye fe-lâ yadillu ve lâ yeşkâ, gloss:kim benim yol göstermemi izlerse ne yolunu şaşırır ne de bedbaht olur, source:20:123}. Bu ayetteki "bedbaht olmak" fiili, on birinci ayetteki "en bedbaht" kelimesiyle aynı köktendir.

## İnsanın kendi ölçüsü

[¶27] قدّر fiili insan için de kullanılır ve o zaman düşünüp tartmak anlamına gelir: {ar:التقدير من الإنسان التفكر في الأمر, tr:et-takdîru mine'l-insâni't-tefekkuru fi'l-emr, gloss:insanın takdiri, bir iş üzerine düşünmesidir, source:"ق د ر,B005"}. Bir başka ifadede {ar:نظرت فيه ودبرته وقايسته, tr:nazartu fîhi ve debbertuhû ve kâyestuh, gloss:onu inceledim, sonunu düşündüm ve ölçüp karşılaştırdım, source:"ق د ر,B005"} denir. Bu anlamın en ağır örneği Kur'an'dan gelen iki kelimedir: {ar:فكر وقدر, tr:fekkera ve kaddera, gloss:düşündü ve ölçüp biçti, source:"ق د ر,B005"}.

[¶28] Kur'an bu iki kelimeyi bir adamın hikâyesinde söyler. Allah Peygamber'e, tek başına yarattığı, bol mal ve yanından ayrılmayan oğullar verdiği o adamı kendisine bırakmasını söyler {source:74:11}. Adam daha fazlasını ister, ama Allah'ın ayetlerine karşı inat eder. Ayetler okununca düşünür ve ölçüp biçer {source:74:18}. Kur'an ardından iki kez "Kahrolası, nasıl da ölçüp biçti!" der {source:74:19}. Adam bakar, kaşlarını çatar, sırtını döner, büyüklenir ve sonunda bu sözün yalnızca aktarılan bir büyü, bir insan sözü olduğuna karar verir {source:74:24}. Hükmü de şudur: {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar ateşine sokacağım, source:74:26}. Buradaki "ateşe sokmak" fiili, on ikinci ayetteki {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yasle'n-nâra'l-kubrâ, gloss:o en büyük ateşe girecek olan, source:87:12} sözündeki fiille aynı köktendir. Aynı surenin sonunda da Kur'an kendisinin bir öğüt olduğunu ve dileyenin ondan öğüt alacağını söyler {source:74:54}.

[¶29] Bu hikâye ayetin iki fiilini birbirinden ayırıp gösterir. Rab ölçer ve yol gösterir; ölçüsünün ardından gelen bir yön vardır. Adam da ölçer, ama ölçüsü gösterilen yola değil, yoldan dönmeye varır. Öğüdü kendi terazisine koyar ve sonucu kendisi belirler. On birinci ayetteki en bedbahtın öğütten uzak durması, bu adamın yaptığının kısa bir adıdır. İnsanın düşünüp tartması yanlış değildir. İnsan da ölçer, ama Davud'un zırhında olduğu gibi kendisine verilmiş bir ölçüye uyarak ölçer. Yanlış olan, gösterilen yolun yerine kendi ölçüsünü koymaktır. Üçüncü ayet ölçüyü ve yolu aynı Rabbe verir. İnsana kalan, o yolu tutup tutmamaktır.

===== _commentary/v16/out/87_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: 20:50 wording "a'ṭā kulla shay'in khalqahu thumma hadā" (lookup unavailable)
- memory: 20:52 "lā yaḍillu rabbī wa lā yansā"
- memory: 6:96 "dhālika taqdīru l-'azīzi l-'alīm"; 6:97 "li-tahtadū bihā"
- memory: 43:10 "la'allakum tahtadūn"; 43:11 "mā'an bi-qadar"
- memory: 36:39 "qaddarnāhu manāzila … ka-l-'urjūni l-qadīm"
- memory: 89:16 "fa-qadara 'alayhi rizqahu"; 89:17 opens with "kallā"
- memory: 34:10–11 iron softened for Dawud, "wa qaddir fi s-sard"
- memory: 74:11–26 sequence, "fa-qutila kayfa qaddara"; 74:54 "innahu tadhkira"
- memory: 16:68–69 bee wording, no h-d-y word
- memory: 20:17–18 staff wording
- memory: vowels hidya, qibla, dibra, wijha in the h-d-y B002 phrase
- not written: qidr cooking pot (q-d-r B007) - nothing attested ties it to measuring
- not written: qudra, power (q-d-r B003) - did not shape a theme beyond measure
- not written: q-d-r B006 middle saddle, short-necked man, horse - no work in themes
- not written: h-d-y B007 protected refugee/captive, B009 dull man, B011 poetry exchange - no theme
- not written: echo root h-d-d (hoopoe, threat, rocking a child) - echo, not identity
- not written: fire as waymark (n-w-r B005) - belongs to twelfth ayah's fire, recalled only
- not written: running file, womb/body and lot-arrow scenes - carried by other ayat's words

===== passages not cited (260) =====
## strong (this ayah's own list) (28)

- (1:6) [listed for 87:3] [cited in ¶26] ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (2:38) [listed for 87:3] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (5:16) [listed for 87:3] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (6:91) [listed for 87:3] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦٓ إِذْ قَالُوا۟ مَآ أَنزَلَ ٱللَّهُ عَلَىٰ بَشَرٍۢ مِّن شَىْءٍۢ ۗ قُلْ مَنْ أَنزَلَ ٱلْكِتَٰبَ ٱلَّذِى جَآءَ بِهِۦ مُوسَىٰ نُورًۭا وَهُدًۭى لِّلنَّاسِ ۖ تَجْعَلُونَهُۥ قَرَاطِيسَ تُبْدُونَهَا وَتُخْفُونَ كَثِيرًۭا ۖ وَعُلِّمْتُم مَّا لَمْ تَعْلَمُوٓا۟ أَنتُمْ وَلَآ ءَابَآؤُكُمْ ۖ قُلِ ٱللَّهُ ۖ ثُمَّ ذَرْهُمْ فِى خَوْضِهِمْ يَلْعَبُونَ
- (6:125) [listed for 87:3] فَمَن يُرِدِ ٱللَّهُ أَن يَهْدِيَهُۥ يَشْرَحْ صَدْرَهُۥ لِلْإِسْلَٰمِ ۖ وَمَن يُرِدْ أَن يُضِلَّهُۥ يَجْعَلْ صَدْرَهُۥ ضَيِّقًا حَرَجًۭا كَأَنَّمَا يَصَّعَّدُ فِى ٱلسَّمَآءِ ۚ كَذَٰلِكَ يَجْعَلُ ٱللَّهُ ٱلرِّجْسَ عَلَى ٱلَّذِينَ لَا يُؤْمِنُونَ
- (13:8) [listed for 87:3] ٱللَّهُ يَعْلَمُ مَا تَحْمِلُ كُلُّ أُنثَىٰ وَمَا تَغِيضُ ٱلْأَرْحَامُ وَمَا تَزْدَادُ ۖ وَكُلُّ شَىْءٍ عِندَهُۥ بِمِقْدَارٍ
- (15:21) [listed for 87:3] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
- (17:9) [listed for 87:3] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
- (20:50) [listed for 87:3] [cited in ¶21] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (20:123) [listed for 87:3] [cited in ¶26] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (23:18) [listed for 87:3] وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ ۖ وَإِنَّا عَلَىٰ ذَهَابٍۭ بِهِۦ لَقَٰدِرُونَ
- (24:45) [listed for 87:3] وَٱللَّهُ خَلَقَ كُلَّ دَآبَّةٍۢ مِّن مَّآءٍۢ ۖ فَمِنْهُم مَّن يَمْشِى عَلَىٰ بَطْنِهِۦ وَمِنْهُم مَّن يَمْشِى عَلَىٰ رِجْلَيْنِ وَمِنْهُم مَّن يَمْشِى عَلَىٰٓ أَرْبَعٍۢ ۚ يَخْلُقُ ٱللَّهُ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (25:2) [listed for 87:3] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
- (26:78) [listed for 87:3] [cited in ¶23] ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ
- (28:56) [listed for 87:3] إِنَّكَ لَا تَهْدِى مَنْ أَحْبَبْتَ وَلَٰكِنَّ ٱللَّهَ يَهْدِى مَن يَشَآءُ ۚ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (36:39) [listed for 87:3] [cited in ¶7] وَٱلْقَمَرَ قَدَّرْنَٰهُ مَنَازِلَ حَتَّىٰ عَادَ كَٱلْعُرْجُونِ ٱلْقَدِيمِ
- (41:10) [listed for 87:3] وَجَعَلَ فِيهَا رَوَٰسِىَ مِن فَوْقِهَا وَبَٰرَكَ فِيهَا وَقَدَّرَ فِيهَآ أَقْوَٰتَهَا فِىٓ أَرْبَعَةِ أَيَّامٍۢ سَوَآءًۭ لِّلسَّآئِلِينَ
- (41:17) [listed for 87:3] وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ فَأَخَذَتْهُمْ صَٰعِقَةُ ٱلْعَذَابِ ٱلْهُونِ بِمَا كَانُوا۟ يَكْسِبُونَ
- (42:52) [listed for 87:3] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ رُوحًۭا مِّنْ أَمْرِنَا ۚ مَا كُنتَ تَدْرِى مَا ٱلْكِتَٰبُ وَلَا ٱلْإِيمَٰنُ وَلَٰكِن جَعَلْنَٰهُ نُورًۭا نَّهْدِى بِهِۦ مَن نَّشَآءُ مِنْ عِبَادِنَا ۚ وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (49:17) [listed for 87:3] يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا۟ ۖ قُل لَّا تَمُنُّوا۟ عَلَىَّ إِسْلَٰمَكُم ۖ بَلِ ٱللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَىٰكُمْ لِلْإِيمَٰنِ إِن كُنتُمْ صَٰدِقِينَ
- (54:49) [listed for 87:3] [cited in ¶6] إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ
- (65:3) [listed for 87:3] وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ ۚ وَمَن يَتَوَكَّلْ عَلَى ٱللَّهِ فَهُوَ حَسْبُهُۥٓ ۚ إِنَّ ٱللَّهَ بَٰلِغُ أَمْرِهِۦ ۚ قَدْ جَعَلَ ٱللَّهُ لِكُلِّ شَىْءٍۢ قَدْرًۭا
- (76:3) [listed for 87:3] [cited in ¶25] إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا
- (77:22) [listed for 87:3] إِلَىٰ قَدَرٍۢ مَّعْلُومٍۢ
- (79:19) [listed for 87:3] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- (90:10) [listed for 87:3] [cited in ¶25] وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- (92:12) [listed for 87:3] [cited in ¶25] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (93:7) [listed for 87:3] وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ

## medium (this ayah's own list) (67)

- (2:213) [listed for 87:3] كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ فَبَعَثَ ٱللَّهُ ٱلنَّبِيِّۦنَ مُبَشِّرِينَ وَمُنذِرِينَ وَأَنزَلَ مَعَهُمُ ٱلْكِتَٰبَ بِٱلْحَقِّ لِيَحْكُمَ بَيْنَ ٱلنَّاسِ فِيمَا ٱخْتَلَفُوا۟ فِيهِ ۚ وَمَا ٱخْتَلَفَ فِيهِ إِلَّا ٱلَّذِينَ أُوتُوهُ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ بَغْيًۢا بَيْنَهُمْ ۖ فَهَدَى ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ لِمَا ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
- (2:272) [listed for 87:3] ۞ لَّيْسَ عَلَيْكَ هُدَىٰهُمْ وَلَٰكِنَّ ٱللَّهَ يَهْدِى مَن يَشَآءُ ۗ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ فَلِأَنفُسِكُمْ ۚ وَمَا تُنفِقُونَ إِلَّا ٱبْتِغَآءَ وَجْهِ ٱللَّهِ ۚ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ يُوَفَّ إِلَيْكُمْ وَأَنتُمْ لَا تُظْلَمُونَ
- (3:86) [listed for 87:3] كَيْفَ يَهْدِى ٱللَّهُ قَوْمًۭا كَفَرُوا۟ بَعْدَ إِيمَٰنِهِمْ وَشَهِدُوٓا۟ أَنَّ ٱلرَّسُولَ حَقٌّۭ وَجَآءَهُمُ ٱلْبَيِّنَٰتُ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (6:82) [listed for 87:3] ٱلَّذِينَ ءَامَنُوا۟ وَلَمْ يَلْبِسُوٓا۟ إِيمَٰنَهُم بِظُلْمٍ أُو۟لَٰٓئِكَ لَهُمُ ٱلْأَمْنُ وَهُم مُّهْتَدُونَ
- (6:161) [listed for 87:3] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (7:158) [listed for 87:3] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ جَمِيعًا ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِ ٱلنَّبِىِّ ٱلْأُمِّىِّ ٱلَّذِى يُؤْمِنُ بِٱللَّهِ وَكَلِمَٰتِهِۦ وَٱتَّبِعُوهُ لَعَلَّكُمْ تَهْتَدُونَ
- (7:178) [listed for 87:3] مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِى ۖ وَمَن يُضْلِلْ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (10:25) [listed for 87:3] وَٱللَّهُ يَدْعُوٓا۟ إِلَىٰ دَارِ ٱلسَّلَٰمِ وَيَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (13:7) [listed for 87:3] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
- (13:26) [listed for 87:3] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ وَفَرِحُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا مَتَٰعٌۭ
- (13:27) [listed for 87:3] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦ ۗ قُلْ إِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَنْ أَنَابَ
- (14:4) [listed for 87:3] وَمَآ أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوْمِهِۦ لِيُبَيِّنَ لَهُمْ ۖ فَيُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (16:9) [listed for 87:3] وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ ۚ وَلَوْ شَآءَ لَهَدَىٰكُمْ أَجْمَعِينَ
- (16:36) [listed for 87:3] وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ ۖ فَمِنْهُم مَّنْ هَدَى ٱللَّهُ وَمِنْهُم مَّنْ حَقَّتْ عَلَيْهِ ٱلضَّلَٰلَةُ ۚ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (16:104) [listed for 87:3] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِـَٔايَٰتِ ٱللَّهِ لَا يَهْدِيهِمُ ٱللَّهُ وَلَهُمْ عَذَابٌ أَلِيمٌ
- (16:125) [listed for 87:3] ٱدْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِٱلْحِكْمَةِ وَٱلْمَوْعِظَةِ ٱلْحَسَنَةِ ۖ وَجَٰدِلْهُم بِٱلَّتِى هِىَ أَحْسَنُ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ ۖ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (17:30) [listed for 87:3] إِنَّ رَبَّكَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ كَانَ بِعِبَادِهِۦ خَبِيرًۢا بَصِيرًۭا
- (17:94) [listed for 87:3] وَمَا مَنَعَ ٱلنَّاسَ أَن يُؤْمِنُوٓا۟ إِذْ جَآءَهُمُ ٱلْهُدَىٰٓ إِلَّآ أَن قَالُوٓا۟ أَبَعَثَ ٱللَّهُ بَشَرًۭا رَّسُولًۭا
- (17:97) [listed for 87:3] وَمَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُمْ أَوْلِيَآءَ مِن دُونِهِۦ ۖ وَنَحْشُرُهُمْ يَوْمَ ٱلْقِيَٰمَةِ عَلَىٰ وُجُوهِهِمْ عُمْيًۭا وَبُكْمًۭا وَصُمًّۭا ۖ مَّأْوَىٰهُمْ جَهَنَّمُ ۖ كُلَّمَا خَبَتْ زِدْنَٰهُمْ سَعِيرًۭا
- (18:17) [listed for 87:3] ۞ وَتَرَى ٱلشَّمْسَ إِذَا طَلَعَت تَّزَٰوَرُ عَن كَهْفِهِمْ ذَاتَ ٱلْيَمِينِ وَإِذَا غَرَبَت تَّقْرِضُهُمْ ذَاتَ ٱلشِّمَالِ وَهُمْ فِى فَجْوَةٍۢ مِّنْهُ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ ۗ مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُۥ وَلِيًّۭا مُّرْشِدًۭا
- (19:43) [listed for 87:3] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (19:76) [listed for 87:3] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
- (20:40) [listed for 87:3] إِذْ تَمْشِىٓ أُخْتُكَ فَتَقُولُ هَلْ أَدُلُّكُمْ عَلَىٰ مَن يَكْفُلُهُۥ ۖ فَرَجَعْنَٰكَ إِلَىٰٓ أُمِّكَ كَىْ تَقَرَّ عَيْنُهَا وَلَا تَحْزَنَ ۚ وَقَتَلْتَ نَفْسًۭا فَنَجَّيْنَٰكَ مِنَ ٱلْغَمِّ وَفَتَنَّٰكَ فُتُونًۭا ۚ فَلَبِثْتَ سِنِينَ فِىٓ أَهْلِ مَدْيَنَ ثُمَّ جِئْتَ عَلَىٰ قَدَرٍۢ يَٰمُوسَىٰ
- (20:82) [listed for 87:3] وَإِنِّى لَغَفَّارٌۭ لِّمَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا ثُمَّ ٱهْتَدَىٰ
- (21:87) [listed for 87:3] وَذَا ٱلنُّونِ إِذ ذَّهَبَ مُغَٰضِبًۭا فَظَنَّ أَن لَّن نَّقْدِرَ عَلَيْهِ فَنَادَىٰ فِى ٱلظُّلُمَٰتِ أَن لَّآ إِلَٰهَ إِلَّآ أَنتَ سُبْحَٰنَكَ إِنِّى كُنتُ مِنَ ٱلظَّٰلِمِينَ
- (22:54) [listed for 87:3] وَلِيَعْلَمَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّكَ فَيُؤْمِنُوا۟ بِهِۦ فَتُخْبِتَ لَهُۥ قُلُوبُهُمْ ۗ وَإِنَّ ٱللَّهَ لَهَادِ ٱلَّذِينَ ءَامَنُوٓا۟ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (24:35) [listed for 87:3] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (24:46) [listed for 87:3] لَّقَدْ أَنزَلْنَآ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ ۚ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (24:54) [listed for 87:3] قُلْ أَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ ۖ فَإِن تَوَلَّوْا۟ فَإِنَّمَا عَلَيْهِ مَا حُمِّلَ وَعَلَيْكُم مَّا حُمِّلْتُمْ ۖ وَإِن تُطِيعُوهُ تَهْتَدُوا۟ ۚ وَمَا عَلَى ٱلرَّسُولِ إِلَّا ٱلْبَلَٰغُ ٱلْمُبِينُ
- (25:31) [listed for 87:3] وَكَذَٰلِكَ جَعَلْنَا لِكُلِّ نَبِىٍّ عَدُوًّۭا مِّنَ ٱلْمُجْرِمِينَ ۗ وَكَفَىٰ بِرَبِّكَ هَادِيًۭا وَنَصِيرًۭا
- (27:2) [listed for 87:3] هُدًۭى وَبُشْرَىٰ لِلْمُؤْمِنِينَ
- (27:57) [listed for 87:3] فَأَنجَيْنَٰهُ وَأَهْلَهُۥٓ إِلَّا ٱمْرَأَتَهُۥ قَدَّرْنَٰهَا مِنَ ٱلْغَٰبِرِينَ
- (27:63) [listed for 87:3] أَمَّن يَهْدِيكُمْ فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ وَمَن يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦٓ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ تَعَٰلَى ٱللَّهُ عَمَّا يُشْرِكُونَ
- (28:22) [listed for 87:3] وَلَمَّا تَوَجَّهَ تِلْقَآءَ مَدْيَنَ قَالَ عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ
- (29:62) [listed for 87:3] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥٓ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (29:69) [listed for 87:3] وَٱلَّذِينَ جَٰهَدُوا۟ فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا ۚ وَإِنَّ ٱللَّهَ لَمَعَ ٱلْمُحْسِنِينَ
- (30:37) [listed for 87:3] أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (34:6) [listed for 87:3] وَيَرَى ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (34:32) [listed for 87:3] قَالَ ٱلَّذِينَ ٱسْتَكْبَرُوا۟ لِلَّذِينَ ٱسْتُضْعِفُوٓا۟ أَنَحْنُ صَدَدْنَٰكُمْ عَنِ ٱلْهُدَىٰ بَعْدَ إِذْ جَآءَكُم ۖ بَلْ كُنتُم مُّجْرِمِينَ
- (34:36) [listed for 87:3] قُلْ إِنَّ رَبِّى يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (34:39) [listed for 87:3] قُلْ إِنَّ رَبِّى يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥ ۚ وَمَآ أَنفَقْتُم مِّن شَىْءٍۢ فَهُوَ يُخْلِفُهُۥ ۖ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ
- (36:21) [listed for 87:3] ٱتَّبِعُوا۟ مَن لَّا يَسْـَٔلُكُمْ أَجْرًۭا وَهُم مُّهْتَدُونَ
- (36:38) [listed for 87:3] وَٱلشَّمْسُ تَجْرِى لِمُسْتَقَرٍّۢ لَّهَا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ
- (39:18) [listed for 87:3] ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَىٰهُمُ ٱللَّهُ ۖ وَأُو۟لَٰٓئِكَ هُمْ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:23) [listed for 87:3] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (39:36) [listed for 87:3] أَلَيْسَ ٱللَّهُ بِكَافٍ عَبْدَهُۥ ۖ وَيُخَوِّفُونَكَ بِٱلَّذِينَ مِن دُونِهِۦ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (39:37) [listed for 87:3] وَمَن يَهْدِ ٱللَّهُ فَمَا لَهُۥ مِن مُّضِلٍّ ۗ أَلَيْسَ ٱللَّهُ بِعَزِيزٍۢ ذِى ٱنتِقَامٍۢ
- (39:52) [listed for 87:3] أَوَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (40:38) [listed for 87:3] وَقَالَ ٱلَّذِىٓ ءَامَنَ يَٰقَوْمِ ٱتَّبِعُونِ أَهْدِكُمْ سَبِيلَ ٱلرَّشَادِ
- (42:13) [listed for 87:3] ۞ شَرَعَ لَكُم مِّنَ ٱلدِّينِ مَا وَصَّىٰ بِهِۦ نُوحًۭا وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَمَا وَصَّيْنَا بِهِۦٓ إِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَىٰٓ ۖ أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ ۚ ٱللَّهُ يَجْتَبِىٓ إِلَيْهِ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَن يُنِيبُ
- (43:11) [listed for 87:3] [cited in ¶18] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
- (47:5) [listed for 87:3] سَيَهْدِيهِمْ وَيُصْلِحُ بَالَهُمْ
- (47:17) [listed for 87:3] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
- (54:12) [listed for 87:3] وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ
- (56:60) [listed for 87:3] نَحْنُ قَدَّرْنَا بَيْنَكُمُ ٱلْمَوْتَ وَمَا نَحْنُ بِمَسْبُوقِينَ
- (63:6) [listed for 87:3] سَوَآءٌ عَلَيْهِمْ أَسْتَغْفَرْتَ لَهُمْ أَمْ لَمْ تَسْتَغْفِرْ لَهُمْ لَن يَغْفِرَ ٱللَّهُ لَهُمْ ۚ إِنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْفَٰسِقِينَ
- (64:6) [listed for 87:3] ذَٰلِكَ بِأَنَّهُۥ كَانَت تَّأْتِيهِمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَقَالُوٓا۟ أَبَشَرٌۭ يَهْدُونَنَا فَكَفَرُوا۟ وَتَوَلَّوا۟ ۚ وَّٱسْتَغْنَى ٱللَّهُ ۚ وَٱللَّهُ غَنِىٌّ حَمِيدٌۭ
- (64:11) [listed for 87:3] مَآ أَصَابَ مِن مُّصِيبَةٍ إِلَّا بِإِذْنِ ٱللَّهِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ يَهْدِ قَلْبَهُۥ ۚ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (65:7) [listed for 87:3] لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ ۖ وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ ۚ لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا ۚ سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا
- (72:2) [listed for 87:3] يَهْدِىٓ إِلَى ٱلرُّشْدِ فَـَٔامَنَّا بِهِۦ ۖ وَلَن نُّشْرِكَ بِرَبِّنَآ أَحَدًۭا
- (74:18) [listed for 87:3] [cited in ¶28] إِنَّهُۥ فَكَّرَ وَقَدَّرَ
- (74:19) [listed for 87:3] [cited in ¶28] فَقُتِلَ كَيْفَ قَدَّرَ
- (74:20) [listed for 87:3] ثُمَّ قُتِلَ كَيْفَ قَدَّرَ
- (75:4) [listed for 87:3] بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ
- (77:23) [listed for 87:3] فَقَدَرْنَا فَنِعْمَ ٱلْقَٰدِرُونَ
- (80:19) [listed for 87:3] [cited in ¶2] مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ
- (97:1) [listed for 87:3] إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ

## named by the passage's own list as strong for this ayah (16)

- (2:29) [listed for 87:3] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (3:6) [listed for 87:3] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (6:1) [listed for 87:3] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَجَعَلَ ٱلظُّلُمَٰتِ وَٱلنُّورَ ۖ ثُمَّ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ يَعْدِلُونَ
- (6:117) [listed for 87:3] إِنَّ رَبَّكَ هُوَ أَعْلَمُ مَن يَضِلُّ عَن سَبِيلِهِۦ ۖ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (14:19) [listed for 87:3] أَلَمْ تَرَ أَنَّ ٱللَّهَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (15:60) [listed for 87:3] إِلَّا ٱمْرَأَتَهُۥ قَدَّرْنَآ ۙ إِنَّهَا لَمِنَ ٱلْغَٰبِرِينَ
- (17:84) [listed for 87:3] قُلْ كُلٌّۭ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًۭا
- (31:25) [listed for 87:3] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (33:38) [listed for 87:3] مَّا كَانَ عَلَى ٱلنَّبِىِّ مِنْ حَرَجٍۢ فِيمَا فَرَضَ ٱللَّهُ لَهُۥ ۖ سُنَّةَ ٱللَّهِ فِى ٱلَّذِينَ خَلَوْا۟ مِن قَبْلُ ۚ وَكَانَ أَمْرُ ٱللَّهِ قَدَرًۭا مَّقْدُورًا
- (55:7) [listed for 87:3] وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
- (57:22) [listed for 87:3] مَآ أَصَابَ مِن مُّصِيبَةٍۢ فِى ٱلْأَرْضِ وَلَا فِىٓ أَنفُسِكُمْ إِلَّا فِى كِتَٰبٍۢ مِّن قَبْلِ أَن نَّبْرَأَهَآ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (59:24) [listed for 87:3] هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (68:7) [listed for 87:3] إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (70:39) [listed for 87:3] كَلَّآ ۖ إِنَّا خَلَقْنَٰهُم مِّمَّا يَعْلَمُونَ
- (74:11) [listed for 87:3] [cited in ¶28] ذَرْنِى وَمَنْ خَلَقْتُ وَحِيدًۭا
- (88:17) [listed for 87:3] أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ

## named by the passage's own list as medium for this ayah (40)

- (2:5) [listed for 87:3] أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (2:21) [listed for 87:3] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
- (6:98) [listed for 87:3] وَهُوَ ٱلَّذِىٓ أَنشَأَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ فَمُسْتَقَرٌّۭ وَمُسْتَوْدَعٌۭ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَفْقَهُونَ
- (6:149) [listed for 87:3] قُلْ فَلِلَّهِ ٱلْحُجَّةُ ٱلْبَٰلِغَةُ ۖ فَلَوْ شَآءَ لَهَدَىٰكُمْ أَجْمَعِينَ
- (7:185) [listed for 87:3] أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا خَلَقَ ٱللَّهُ مِن شَىْءٍۢ وَأَنْ عَسَىٰٓ أَن يَكُونَ قَدِ ٱقْتَرَبَ أَجَلُهُمْ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ
- (10:31) [listed for 87:3] قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ أَمَّن يَمْلِكُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَمَن يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَمَن يُدَبِّرُ ٱلْأَمْرَ ۚ فَسَيَقُولُونَ ٱللَّهُ ۚ فَقُلْ أَفَلَا تَتَّقُونَ
- (10:35) [listed for 87:3] قُلْ هَلْ مِن شُرَكَآئِكُم مَّن يَهْدِىٓ إِلَى ٱلْحَقِّ ۚ قُلِ ٱللَّهُ يَهْدِى لِلْحَقِّ ۗ أَفَمَن يَهْدِىٓ إِلَى ٱلْحَقِّ أَحَقُّ أَن يُتَّبَعَ أَمَّن لَّا يَهِدِّىٓ إِلَّآ أَن يُهْدَىٰ ۖ فَمَا لَكُمْ كَيْفَ تَحْكُمُونَ
- (15:28) [listed for 87:3] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى خَٰلِقٌۢ بَشَرًۭا مِّن صَلْصَٰلٍۢ مِّنْ حَمَإٍۢ مَّسْنُونٍۢ
- (16:16) [listed for 87:3] وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ
- (16:37) [listed for 87:3] إِن تَحْرِصْ عَلَىٰ هُدَىٰهُمْ فَإِنَّ ٱللَّهَ لَا يَهْدِى مَن يُضِلُّ ۖ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (16:121) [listed for 87:3] شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (20:41) [listed for 87:3] وَٱصْطَنَعْتُكَ لِنَفْسِى
- (30:54) [listed for 87:3] ۞ ٱللَّهُ ٱلَّذِى خَلَقَكُم مِّن ضَعْفٍۢ ثُمَّ جَعَلَ مِنۢ بَعْدِ ضَعْفٍۢ قُوَّةًۭ ثُمَّ جَعَلَ مِنۢ بَعْدِ قُوَّةٍۢ ضَعْفًۭا وَشَيْبَةًۭ ۚ يَخْلُقُ مَا يَشَآءُ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْقَدِيرُ
- (32:24) [listed for 87:3] وَجَعَلْنَا مِنْهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا لَمَّا صَبَرُوا۟ ۖ وَكَانُوا۟ بِـَٔايَٰتِنَا يُوقِنُونَ
- (34:11) [listed for 87:3] [cited in ¶5] أَنِ ٱعْمَلْ سَٰبِغَٰتٍۢ وَقَدِّرْ فِى ٱلسَّرْدِ ۖ وَٱعْمَلُوا۟ صَٰلِحًا ۖ إِنِّى بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (34:24) [listed for 87:3] ۞ قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُلِ ٱللَّهُ ۖ وَإِنَّآ أَوْ إِيَّاكُمْ لَعَلَىٰ هُدًى أَوْ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (42:12) [listed for 87:3] لَهُۥ مَقَالِيدُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (43:12) [listed for 87:3] [cited in ¶18] وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا وَجَعَلَ لَكُم مِّنَ ٱلْفُلْكِ وَٱلْأَنْعَٰمِ مَا تَرْكَبُونَ
- (43:27) [listed for 87:3] إِلَّا ٱلَّذِى فَطَرَنِى فَإِنَّهُۥ سَيَهْدِينِ
- (45:4) [listed for 87:3] وَفِى خَلْقِكُمْ وَمَا يَبُثُّ مِن دَآبَّةٍ ءَايَٰتٌۭ لِّقَوْمٍۢ يُوقِنُونَ
- (51:1) [listed for 87:3] وَٱلذَّٰرِيَٰتِ ذَرْوًۭا
- (51:4) [listed for 87:3] فَٱلْمُقَسِّمَٰتِ أَمْرًا
- (51:49) [listed for 87:3] وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ
- (55:8) [listed for 87:3] أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ
- (56:62) [listed for 87:3] وَلَقَدْ عَلِمْتُمُ ٱلنَّشْأَةَ ٱلْأُولَىٰ فَلَوْلَا تَذَكَّرُونَ
- (68:25) [listed for 87:3] وَغَدَوْا۟ عَلَىٰ حَرْدٍۢ قَٰدِرِينَ
- (70:40) [listed for 87:3] فَلَآ أُقْسِمُ بِرَبِّ ٱلْمَشَٰرِقِ وَٱلْمَغَٰرِبِ إِنَّا لَقَٰدِرُونَ
- (71:14) [listed for 87:3] وَقَدْ خَلَقَكُمْ أَطْوَارًا
- (76:16) [listed for 87:3] قَوَارِيرَا۟ مِن فِضَّةٍۢ قَدَّرُوهَا تَقْدِيرًۭا
- (80:18) [listed for 87:3] مِنْ أَىِّ شَىْءٍ خَلَقَهُۥ
- (81:26) [listed for 87:3] فَأَيْنَ تَذْهَبُونَ
- (82:7) [listed for 87:3] ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ
- (84:19) [listed for 87:3] لَتَرْكَبُنَّ طَبَقًا عَن طَبَقٍۢ
- (86:6) [listed for 87:3] خُلِقَ مِن مَّآءٍۢ دَافِقٍۢ
- (90:5) [listed for 87:3] أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- (91:7) [listed for 87:3] وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- (92:3) [listed for 87:3] وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- (95:4) [listed for 87:3] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ
- (96:11) [listed for 87:3] أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- (97:2) [listed for 87:3] وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ

## weak (this ayah's own list) (17)

- (2:150) [listed for 87:3] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
- (2:196) [listed for 87:3] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (2:236) [listed for 87:3] لَّا جُنَاحَ عَلَيْكُمْ إِن طَلَّقْتُمُ ٱلنِّسَآءَ مَا لَمْ تَمَسُّوهُنَّ أَوْ تَفْرِضُوا۟ لَهُنَّ فَرِيضَةًۭ ۚ وَمَتِّعُوهُنَّ عَلَى ٱلْمُوسِعِ قَدَرُهُۥ وَعَلَى ٱلْمُقْتِرِ قَدَرُهُۥ مَتَٰعًۢا بِٱلْمَعْرُوفِ ۖ حَقًّا عَلَى ٱلْمُحْسِنِينَ
- (2:264) [listed for 87:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (5:105) [listed for 87:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ عَلَيْكُمْ أَنفُسَكُمْ ۖ لَا يَضُرُّكُم مَّن ضَلَّ إِذَا ٱهْتَدَيْتُمْ ۚ إِلَى ٱللَّهِ مَرْجِعُكُمْ جَمِيعًۭا فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (6:17) [listed for 87:3] وَإِن يَمْسَسْكَ ٱللَّهُ بِضُرٍّۢ فَلَا كَاشِفَ لَهُۥٓ إِلَّا هُوَ ۖ وَإِن يَمْسَسْكَ بِخَيْرٍۢ فَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (7:58) [listed for 87:3] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
- (13:1) [listed for 87:3] الٓمٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ۗ وَٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (20:72) [listed for 87:3] قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ
- (26:79) [listed for 87:3] [cited in ¶23] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (26:81) [listed for 87:3] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (26:82) [listed for 87:3] وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ
- (27:35) [listed for 87:3] وَإِنِّى مُرْسِلَةٌ إِلَيْهِم بِهَدِيَّةٍۢ فَنَاظِرَةٌۢ بِمَ يَرْجِعُ ٱلْمُرْسَلُونَ
- (35:31) [listed for 87:3] وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ مِنَ ٱلْكِتَٰبِ هُوَ ٱلْحَقُّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ ۗ إِنَّ ٱللَّهَ بِعِبَادِهِۦ لَخَبِيرٌۢ بَصِيرٌۭ
- (39:33) [listed for 87:3] وَٱلَّذِى جَآءَ بِٱلصِّدْقِ وَصَدَّقَ بِهِۦٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
- (57:26) [listed for 87:3] وَلَقَدْ أَرْسَلْنَا نُوحًۭا وَإِبْرَٰهِيمَ وَجَعَلْنَا فِى ذُرِّيَّتِهِمَا ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ ۖ فَمِنْهُم مُّهْتَدٍۢ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (64:1) [listed for 87:3] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ لَهُ ٱلْمُلْكُ وَلَهُ ٱلْحَمْدُ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ

## named by the passage's own list as weak for this ayah (11)

- (6:35) [listed for 87:3] وَإِن كَانَ كَبُرَ عَلَيْكَ إِعْرَاضُهُمْ فَإِنِ ٱسْتَطَعْتَ أَن تَبْتَغِىَ نَفَقًۭا فِى ٱلْأَرْضِ أَوْ سُلَّمًۭا فِى ٱلسَّمَآءِ فَتَأْتِيَهُم بِـَٔايَةٍۢ ۚ وَلَوْ شَآءَ ٱللَّهُ لَجَمَعَهُمْ عَلَى ٱلْهُدَىٰ ۚ فَلَا تَكُونَنَّ مِنَ ٱلْجَٰهِلِينَ
- (7:11) [listed for 87:3] وَلَقَدْ خَلَقْنَٰكُمْ ثُمَّ صَوَّرْنَٰكُمْ ثُمَّ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ لَمْ يَكُن مِّنَ ٱلسَّٰجِدِينَ
- (22:5) [listed for 87:3] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
- (22:6) [listed for 87:3] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّهُۥ يُحْىِ ٱلْمَوْتَىٰ وَأَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (28:82) [listed for 87:3] وَأَصْبَحَ ٱلَّذِينَ تَمَنَّوْا۟ مَكَانَهُۥ بِٱلْأَمْسِ يَقُولُونَ وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ ۖ لَوْلَآ أَن مَّنَّ ٱللَّهُ عَلَيْنَا لَخَسَفَ بِنَا ۖ وَيْكَأَنَّهُۥ لَا يُفْلِحُ ٱلْكَٰفِرُونَ
- (43:42) [listed for 87:3] أَوْ نُرِيَنَّكَ ٱلَّذِى وَعَدْنَٰهُمْ فَإِنَّا عَلَيْهِم مُّقْتَدِرُونَ
- (74:47) [listed for 87:3] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
- (77:2) [listed for 87:3] فَٱلْعَٰصِفَٰتِ عَصْفًۭا
- (79:4) [listed for 87:3] فَٱلسَّٰبِقَٰتِ سَبْقًۭا
- (91:1) [listed for 87:3] وَٱلشَّمْسِ وَضُحَىٰهَا
- (103:1) [listed for 87:3] وَٱلْعَصْرِ

## neighbours: within two ayat of a passage the commentary cites (81)

- (1:4) [next to 1:6] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (1:5) [next to 1:6] إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- (1:7) [next to 1:6] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- (6:93) [next to 6:95] وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ قَالَ أُوحِىَ إِلَىَّ وَلَمْ يُوحَ إِلَيْهِ شَىْءٌۭ وَمَن قَالَ سَأُنزِلُ مِثْلَ مَآ أَنزَلَ ٱللَّهُ ۗ وَلَوْ تَرَىٰٓ إِذِ ٱلظَّٰلِمُونَ فِى غَمَرَٰتِ ٱلْمَوْتِ وَٱلْمَلَٰٓئِكَةُ بَاسِطُوٓا۟ أَيْدِيهِمْ أَخْرِجُوٓا۟ أَنفُسَكُمُ ۖ ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَقُولُونَ عَلَى ٱللَّهِ غَيْرَ ٱلْحَقِّ وَكُنتُمْ عَنْ ءَايَٰتِهِۦ تَسْتَكْبِرُونَ
- (6:94) [next to 6:95] وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۢ وَتَرَكْتُم مَّا خَوَّلْنَٰكُمْ وَرَآءَ ظُهُورِكُمْ ۖ وَمَا نَرَىٰ مَعَكُمْ شُفَعَآءَكُمُ ٱلَّذِينَ زَعَمْتُمْ أَنَّهُمْ فِيكُمْ شُرَكَٰٓؤُا۟ ۚ لَقَد تَّقَطَّعَ بَيْنَكُمْ وَضَلَّ عَنكُم مَّا كُنتُمْ تَزْعُمُونَ
- (6:99) [next to 6:97] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (16:66) [next to 16:68] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ
- (16:67) [next to 16:68] وَمِن ثَمَرَٰتِ ٱلنَّخِيلِ وَٱلْأَعْنَٰبِ تَتَّخِذُونَ مِنْهُ سَكَرًۭا وَرِزْقًا حَسَنًا ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَعْقِلُونَ
- (16:70) [next to 16:68] وَٱللَّهُ خَلَقَكُمْ ثُمَّ يَتَوَفَّىٰكُمْ ۚ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَىْ لَا يَعْلَمَ بَعْدَ عِلْمٍۢ شَيْـًٔا ۚ إِنَّ ٱللَّهَ عَلِيمٌۭ قَدِيرٌۭ
- (16:71) [next to 16:69] وَٱللَّهُ فَضَّلَ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ فِى ٱلرِّزْقِ ۚ فَمَا ٱلَّذِينَ فُضِّلُوا۟ بِرَآدِّى رِزْقِهِمْ عَلَىٰ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَهُمْ فِيهِ سَوَآءٌ ۚ أَفَبِنِعْمَةِ ٱللَّهِ يَجْحَدُونَ
- (20:8) [next to 20:10] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:9) [next to 20:10] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:11) [next to 20:10] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
- (20:12) [next to 20:10] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
- (20:14) [next to 20:13] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:15) [next to 20:13] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (20:16) [next to 20:17] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (20:19) [next to 20:17] قَالَ أَلْقِهَا يَٰمُوسَىٰ
- (20:20) [next to 20:18] فَأَلْقَىٰهَا فَإِذَا هِىَ حَيَّةٌۭ تَسْعَىٰ
- (20:47) [next to 20:49] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
- (20:48) [next to 20:49] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:51) [next to 20:49] قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ
- (20:55) [next to 20:53] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
- (20:56) [next to 20:54] وَلَقَدْ أَرَيْنَٰهُ ءَايَٰتِنَا كُلَّهَا فَكَذَّبَ وَأَبَىٰ
- (20:121) [next to 20:123] فَأَكَلَا مِنْهَا فَبَدَتْ لَهُمَا سَوْءَٰتُهُمَا وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِن وَرَقِ ٱلْجَنَّةِ ۚ وَعَصَىٰٓ ءَادَمُ رَبَّهُۥ فَغَوَىٰ
- (20:122) [next to 20:123] ثُمَّ ٱجْتَبَٰهُ رَبُّهُۥ فَتَابَ عَلَيْهِ وَهَدَىٰ
- (20:124) [next to 20:123] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
- (20:125) [next to 20:123] قَالَ رَبِّ لِمَ حَشَرْتَنِىٓ أَعْمَىٰ وَقَدْ كُنتُ بَصِيرًۭا
- (26:75) [next to 26:77] قَالَ أَفَرَءَيْتُم مَّا كُنتُمْ تَعْبُدُونَ
- (26:76) [next to 26:77] أَنتُمْ وَءَابَآؤُكُمُ ٱلْأَقْدَمُونَ
- (26:80) [next to 26:78] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (34:8) [next to 34:10] أَفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَم بِهِۦ جِنَّةٌۢ ۗ بَلِ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ فِى ٱلْعَذَابِ وَٱلضَّلَٰلِ ٱلْبَعِيدِ
- (34:9) [next to 34:10] أَفَلَمْ يَرَوْا۟ إِلَىٰ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ إِن نَّشَأْ نَخْسِفْ بِهِمُ ٱلْأَرْضَ أَوْ نُسْقِطْ عَلَيْهِمْ كِسَفًۭا مِّنَ ٱلسَّمَآءِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّكُلِّ عَبْدٍۢ مُّنِيبٍۢ
- (34:12) [next to 34:10] وَلِسُلَيْمَٰنَ ٱلرِّيحَ غُدُوُّهَا شَهْرٌۭ وَرَوَاحُهَا شَهْرٌۭ ۖ وَأَسَلْنَا لَهُۥ عَيْنَ ٱلْقِطْرِ ۖ وَمِنَ ٱلْجِنِّ مَن يَعْمَلُ بَيْنَ يَدَيْهِ بِإِذْنِ رَبِّهِۦ ۖ وَمَن يَزِغْ مِنْهُمْ عَنْ أَمْرِنَا نُذِقْهُ مِنْ عَذَابِ ٱلسَّعِيرِ
- (34:13) [next to 34:11] يَعْمَلُونَ لَهُۥ مَا يَشَآءُ مِن مَّحَٰرِيبَ وَتَمَٰثِيلَ وَجِفَانٍۢ كَٱلْجَوَابِ وَقُدُورٍۢ رَّاسِيَٰتٍ ۚ ٱعْمَلُوٓا۟ ءَالَ دَاوُۥدَ شُكْرًۭا ۚ وَقَلِيلٌۭ مِّنْ عِبَادِىَ ٱلشَّكُورُ
- (36:37) [next to 36:39] وَءَايَةٌۭ لَّهُمُ ٱلَّيْلُ نَسْلَخُ مِنْهُ ٱلنَّهَارَ فَإِذَا هُم مُّظْلِمُونَ
- (36:40) [next to 36:39] لَا ٱلشَّمْسُ يَنۢبَغِى لَهَآ أَن تُدْرِكَ ٱلْقَمَرَ وَلَا ٱلَّيْلُ سَابِقُ ٱلنَّهَارِ ۚ وَكُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ
- (36:41) [next to 36:39] وَءَايَةٌۭ لَّهُمْ أَنَّا حَمَلْنَا ذُرِّيَّتَهُمْ فِى ٱلْفُلْكِ ٱلْمَشْحُونِ
- (43:7) [next to 43:9] وَمَا يَأْتِيهِم مِّن نَّبِىٍّ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (43:8) [next to 43:9] فَأَهْلَكْنَآ أَشَدَّ مِنْهُم بَطْشًۭا وَمَضَىٰ مَثَلُ ٱلْأَوَّلِينَ
- (43:13) [next to 43:11] لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
- (43:14) [next to 43:12] وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ
- (54:47) [next to 54:49] إِنَّ ٱلْمُجْرِمِينَ فِى ضَلَٰلٍۢ وَسُعُرٍۢ
- (54:48) [next to 54:49] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (54:50) [next to 54:49] وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌۭ كَلَمْحٍۭ بِٱلْبَصَرِ
- (54:51) [next to 54:49] وَلَقَدْ أَهْلَكْنَآ أَشْيَاعَكُمْ فَهَلْ مِن مُّدَّكِرٍۢ
- (74:9) [next to 74:11] فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ
- (74:10) [next to 74:11] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (74:12) [next to 74:11] وَجَعَلْتُ لَهُۥ مَالًۭا مَّمْدُودًۭا
- (74:13) [next to 74:11] وَبَنِينَ شُهُودًۭا
- (74:16) [next to 74:18] كَلَّآ ۖ إِنَّهُۥ كَانَ لِءَايَٰتِنَا عَنِيدًۭا
- (74:17) [next to 74:18] سَأُرْهِقُهُۥ صَعُودًا
- (74:21) [next to 74:19] ثُمَّ نَظَرَ
- (74:22) [next to 74:24] ثُمَّ عَبَسَ وَبَسَرَ
- (74:23) [next to 74:24] ثُمَّ أَدْبَرَ وَٱسْتَكْبَرَ
- (74:25) [next to 74:24] إِنْ هَٰذَآ إِلَّا قَوْلُ ٱلْبَشَرِ
- (74:27) [next to 74:26] وَمَآ أَدْرَىٰكَ مَا سَقَرُ
- (74:28) [next to 74:26] لَا تُبْقِى وَلَا تَذَرُ
- (74:52) [next to 74:54] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
- (74:53) [next to 74:54] كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ
- (74:55) [next to 74:54] فَمَن شَآءَ ذَكَرَهُۥ
- (74:56) [next to 74:54] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
- (76:1) [next to 76:3] هَلْ أَتَىٰ عَلَى ٱلْإِنسَٰنِ حِينٌۭ مِّنَ ٱلدَّهْرِ لَمْ يَكُن شَيْـًۭٔا مَّذْكُورًا
- (76:2) [next to 76:3] إِنَّا خَلَقْنَا ٱلْإِنسَٰنَ مِن نُّطْفَةٍ أَمْشَاجٍۢ نَّبْتَلِيهِ فَجَعَلْنَٰهُ سَمِيعًۢا بَصِيرًا
- (76:4) [next to 76:3] إِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا
- (76:5) [next to 76:3] إِنَّ ٱلْأَبْرَارَ يَشْرَبُونَ مِن كَأْسٍۢ كَانَ مِزَاجُهَا كَافُورًا
- (80:17) [next to 80:19] قُتِلَ ٱلْإِنسَٰنُ مَآ أَكْفَرَهُۥ
- (80:21) [next to 80:19] ثُمَّ أَمَاتَهُۥ فَأَقْبَرَهُۥ
- (80:22) [next to 80:20] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
- (89:14) [next to 89:16] إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- (89:15) [next to 89:16] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- (89:18) [next to 89:16] وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (89:19) [next to 89:17] وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- (90:8) [next to 90:10] أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- (90:9) [next to 90:10] وَلِسَانًۭا وَشَفَتَيْنِ
- (90:11) [next to 90:10] فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- (90:12) [next to 90:10] وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- (92:10) [next to 92:12] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:11) [next to 92:12] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (92:13) [next to 92:12] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:14) [next to 92:12] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ

