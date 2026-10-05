Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:8; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_8/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_8.reading.tr.md (prose paragraphs numbered) =====
## Yolu değil, yolcuyu kolaylaştırmak

[¶1] Sekizinci ayet iki kelimeden oluşur ve ikisi de aynı kökten gelir: {ar:وَنُيَسِّرُكَ, tr:ve nuyessiruke, gloss:ve seni kolaylaştıracağız, source:87:8} ve {ar:لِلْيُسْرَىٰ, tr:li'l-yusrâ, gloss:en kolay olana, source:87:8}. Konuşan "biz"dir. Bu, altıncı ayette {ar:سَنُقْرِئُكَ, tr:se-nukriuke, gloss:sana okutacağız, source:87:6} diyen sestir. Baştaki "ve" bu ikinci vaadi birinciye bağlar, gelecek zamanını da ondan alır: sana okutacağız, unutmayacaksın, seni kolaylaştıracağız. Arada yedinci ayet, unutmanın ancak Allah'ın dilediği kadar olacağını ve O'nun açıkta olanı da gizli kalanı da bildiğini söyler. Kolaylaştırma sözünü, insanın içinde gizli kalanı bilen biri verir.

[¶2] Cümlenin şaşırtıcı yanı nesnesindedir. İnsan genellikle bir işi ya da bir yolu kolaylaştırır. Kur'an bu alışılmış yapıyı başka yerlerde kullanır. Nankör insanı anlatan bir surede Allah'ın onu bir damladan yaratıp ölçüsünü koyduğu söylenir, ardından {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:summe's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} denir. Orada kolaylaştırılan yoldur. Surenin son ayetinde sayfaları anılan Musa da Firavun'a gönderilirken {ar:وَيَسِّرْ لِىٓ أَمْرِى, tr:ve yessir lî emrî, gloss:işimi bana kolaylaştır, source:20:26} diye dua eder. Orada kolaylaşan iştir, Musa ise bundan yararlanacak olandır. Sekizinci ayette ise fiilin doğrudan nesnesi muhatabın kendisidir. Kolaylaştırılan kişidir, yol ise yalnızca varılacak yer olarak anılır. Kelimenin kullanımı bunun ne demek olduğunu açar. Bir şey kolaylaşınca hazır hâle gelmiş sayılır: {ar:وتيسر واستيسر بمعنى تهيأ, tr:ve teyessera ve'steysera bi-ma'nâ teheyyee, gloss:teyessera ve isteysera "hazır hâle geldi" demektir, source:"ي س ر,B001"}. Birine kolaylık göstermek de ona yumuşak davranmaktır: {ar:ياسره أي ساهله, tr:yâserahû ey sâhelehû, gloss:ona kolaylık gösterdi, yani yumuşak davrandı, source:"ي س ر,B001"}. Öyleyse "seni kolaylaştıracağız" sözü "seni hazırlayacağız, sana yatkınlık vereceğiz" diye de duyulur. Yol olduğu gibi kalır, yürüyen ona göre hazırlanır.

[¶3] Türkçe bu fiilden türeyen bir kelimeyi hâlâ kullanır: müyesser, yani "kolaylaştırılmış". "Allah müyesser etsin", "hacca gitmek müyesser oldu" deriz. Türkçede müyesser olan hep bir iş ya da bir nimettir, insan ise onun nasip olduğu kişidir. Ayet bu kelimenin bugün yalnız işler için kullanılan anlamını insana çevirir: müyesser kılınan Peygamber'in kendisidir.

[¶4] Varılacak yerin adı da dikkatle seçilmiştir. Yusrâ, "kolay" sıfatının en üstün derecesinin dişil biçimidir: en kolay olan. Hangi isme sıfat olduğu söylenmez. Yol mu, hâl mi, son mu, belli değildir. Ayet ismi düşürüp yalnız niteliği bırakır. Kökün temel anlamı zorluğun karşıtıdır: {ar:اليسر: ضد العسر, tr:el-yusru diddu'l-usr, gloss:yüsr zorluğun zıddıdır, source:"ي س ر,B001"}. Bu karşıtlık, surenin başka ayetlerinde ve Kur'an'ın başka bir suresinde açık bir karşılık bulur.

## Hafif adımlı binek

[¶5] Kökün Arapçada bir insanı ve bir atı aynı sözle niteleyen bir kullanımı vardır. Bu kullanım ayetteki "kolaylaştırma" anlamının yerine geçmez, onun yanında duyulan bir resimdir. Kolay güdülen, çekildiği yöne hemen giden kişiye ya da ata yesr denirdi: {ar:يسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس, tr:yesrun ey leyyinu'l-inkıyâdi serîu'l-mutâbaa, yûsafu bihi'l-insânu ve'l-feres, gloss:yesr, yedekte yumuşak giden ve çabuk ardından gelen demektir; insan da at da böyle nitelenir, source:"ي س ر,B005"}. Hafif bacaklar {ar:اليسرات: القوائم الخفاف, tr:el-yeserât el-kavâimu'l-hıfâf, gloss:yeserât hafif bacaklardır, source:"ي س ر,B005"} diye anılır. İyi yürüyen bir hayvan için de {ar:فرس حسن التيسور أي حسن نقل القوائم, tr:ferasun hasenu't-teysûr ey hasenu nakli'l-kavâim, gloss:teysûru güzel at, yani ayaklarını güzel aktaran at, source:"ي س ر,B005"} derlerdi. Teysûr, bacakların sırayla, takılmadan ve birbirine çarpmadan yer değiştirmesidir. Böyle bir hayvanda binici dizginle uğraşmaz, hafif bir dokunuş yeter, hayvan yolu kendi adımıyla alır. Kolaylık burada yolun düzlüğünde değil, bacakların hafifliğinde ve başın yumuşaklığındadır.

[¶6] Bu resim ayetin nesne seçimini somutlaştırır. Yolu düzlemek bir şeydir, yolcuyu yola yatkın kılmak başka bir şey. Sekizinci ayet ikincisini söyler. Yol sarp da olsa düz de olsa, Peygamber onu hafif adımla alacak ve çekildiği yöne direnmeden dönecek biri hâline getirilir. Üçüncü ayetteki {ar:فَهَدَىٰ, tr:fe-hedâ, gloss:yol gösterdi, source:87:3} fiili önden giden kılavuzu çağırır. Önde giden ile ardından kolayca gelen binek arasındaki yolculuk sahnesini bu iki ayetin kelimeleri birlikte kurar. On altıncı ve on yedinci ayetlerdeki "öne koymak", "sonra gelen" ve "daha kalıcı" kelimeleri de aynı güzel adımı koşan bir dizinin içine yerleştirir.

[¶7] Kur'an bu kökün kelimesini bir hareket tarzı için de kullanır. Bir sure, adları verilmeyen varlıklar üzerine yeminle açılır. Önce savuranlar gelir, sonra {ar:فَٱلْحَٰمِلَٰتِ وِقْرًۭا, tr:fe'l-hâmilâti vikrâ, gloss:ağır yük taşıyanlar, source:51:2}, sonra da {ar:فَٱلْجَٰرِيَٰتِ يُسْرًۭا, tr:fe'l-câriyâti yusrâ, gloss:kolaylıkla akıp gidenler, source:51:3}. Yükün hemen ardından gelen bu akış, kolaylığın ne olduğunu gösterir: yük ortadan kalkmaz, ama yük altındaki gidiş kolaylaşır. Peygamber'e seslenen kısa bir sure de aynı sırayla konuşur. Allah ona göğsünü açtığını ve {ar:وَوَضَعْنَا عَنكَ وِزْرَكَ, tr:ve veda'nâ anke vizrak, gloss:yükünü senden indirdik, source:94:2} dediğini hatırlatır. Bu yük {ar:ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ, tr:elleẕî enkada zahrak, gloss:belini büken, source:94:3} bir yüktür. Sırtı yükle bükülmüş birinin yükü indirilir, ardından iki kez {ar:إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا, tr:inne mea'l-usri yusrâ, gloss:zorlukla birlikte bir kolaylık vardır, source:94:6} denir. Kolaylığın zorluktan sonra değil, zorlukla birlikte geldiği söylenir. Binek resmi bu sözü de açar: hafif ayaklı hayvan yokuşu ortadan kaldırmaz, yokuşu yokuşun içinde kolayca çıkar.

## Söz kolaylaşınca öğüt başlar

[¶8] Sekizinci ayet iki ayetin arasında durur ve ikisine de bağlıdır. Öncesinde okutma ve unutmama sözü vardır. Sonrasında {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öyleyse öğüt ver, eğer öğüt fayda verirse, source:87:9} emri gelir. Dokuzuncu ayetin başındaki "öyleyse", kolaylaştırmanın ne için olduğunu gösterir: okutulan, unutmayan ve kolaylaştırılan kişi artık hatırlatacaktır.

[¶9] Kur'an bu fiili başka yerlerde de sözle ve hatırlamayla birlikte kullanır. Geçmiş kavimlerin yalanlayıp helak edilişini tek tek anlatan bir surede her hikâyenin ardından {ar:وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ, tr:ve lekad yessernâ'l-kur'âne li'ẕ-ẕikri fe-hel min muddekir, gloss:andolsun, Kur'an'ı öğüt için kolaylaştırdık; öğüt alan var mı, source:54:17} denir. Kolaylaştırma, öğüt ve öğüt alan: dokuzuncu ve onuncu ayetlerin kelimeleri orada da bu sırayla durur. İki başka surenin sonunda Allah Peygamber'e {ar:فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ, tr:fe-innemâ yessernâhu bi-lisânike leallehum yetezekkerûn, gloss:biz onu senin dilinle kolaylaştırdık ki öğüt alsınlar, source:44:58} der. Ötekinde aynı cümle {ar:لِتُبَشِّرَ بِهِ ٱلْمُتَّقِينَ وَتُنذِرَ بِهِۦ قَوْمًۭا لُّدًّۭا, tr:li-tubeşşira bihi'l-muttakîne ve tunẕira bihî kavmen luddâ, gloss:onunla sakınanlara müjde veresin, inatçı bir topluluğu uyarasın diye, source:19:97} diye sürer. Bu ayetlerde kolaylaştırılan sözdür, Peygamber'in dili ise sözün aktığı yerdir. Sekizinci ayette kolaylaştırılan Peygamber'in kendisidir. Bunlar aynı işin iki yüzüdür: söz dile hafif gelir, dil de söze hazır olur. Altıncı ayetteki okutma sözüyle sekizinci ayetteki kolaylaştırma sözünün aynı "ve" ile bağlanması bu yüzden yerindedir.

[¶10] Gece ibadetini anlatan bir surenin son ayeti bu bağı okumayla kurar. Ayet Peygamber'e, Rabbinin onun ve yanındakilerin gecenin üçte ikisine yakınını, yarısını ya da üçte birini ayakta geçirdiğini bildiğini söyler. Allah bunu tam sayamayacaklarını bildiği için onlara döner ve {ar:فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ, tr:fakra'û mâ teyessera mine'l-kur'ân, gloss:Kur'an'dan kolay geleni okuyun, source:73:20} der. Aynı ayet hastaları, yolculuk edenleri ve savaşanları da sayar. Okumanın ölçüsü kolay gelendir. Oruç emredilirken de Kur'an'ın indirildiği ay anılır, hastaya ve yolcuya başka günler tanınır ve gerekçe olarak {ar:يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ, tr:yurîdullâhu bikumu'l-yusra ve lâ yurîdu bikumu'l-usr, gloss:Allah sizin için kolaylık ister, zorluk istemez, source:2:185} denir. Aynı ayet Allah'ı {ar:عَلَىٰ مَا هَدَىٰكُمْ, tr:alâ mâ hedâkum, gloss:size yol gösterdiği için, source:2:185} yüceltmeyi ister. İnen söz, yol gösterme, kolaylık ve Allah'ı yüceltmek orada bir aradadır. Bunlar bu surenin birinci, üçüncü, altıncı ve sekizinci ayetlerinin konularıdır.

[¶11] Bir başka sure Peygamber'e ilk sözünü olumsuz kurar: {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana zahmet çekesin diye indirmedik, source:20:2}. Hemen ardından {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkireten li-men yahşâ, gloss:ancak içi titreyen için bir öğüt olsun diye, source:20:3} gelir. Bu iki ayet, sekizinci ayetten on birinci ayete kadar süren bölümü öbür yönden söyler: zahmet değil kolaylık, bir öğüt ve içi titreyen biri. Onuncu ayet de {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10} der. Peygamber'in yükü öğüt vermektir. Kolaylık bu yükü boşa çıkarmaz, onu taşınabilir kılar.

[¶12] Bu kolaylık bir dinlenme de değildir. Yükün indirildiği ve zorlukla birlikte kolaylığın vaat edildiği surenin son iki ayeti {ar:فَإِذَا فَرَغْتَ فَٱنصَبْ, tr:fe-iẕâ feragte fensab, gloss:bir işi bitirince hemen yeniden koyul, source:94:7} ve {ar:وَإِلَىٰ رَبِّكَ فَٱرْغَب, tr:ve ilâ rabbike ferğab, gloss:ve yalnız Rabbine yönel, source:94:8} der. Kolaylaştırılan kişi kenara oturtulmaz, yeniden işe koşulur. Sekizinci ayetin ardından gelen "öyleyse öğüt ver" emri de bunu yapar.

## Kolaylığın karşı yakası

[¶13] Kolaylığın surede bir karşıtı vardır ve on birinci ayette görünür: öğütten {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ondan uzak durur, source:87:11}. Eşkâ kelimesinin kökü çekilen zahmeti ve kolaylığın zıddını anlatır: {ar:أصل يدل على المعاناة وخلاف السهولة, tr:aslun yedullu ale'l-muânâti ve hilâfi's-suhûle, gloss:çekilen zahmeti ve kolaylığın zıddını gösteren bir kök, source:"ش ق و,B002"}. Kolaylaştırılan Peygamber ile zahmetin en dibindeki kişi aynı öğüdün iki ucunda durur. Biri öğüdü taşır, öteki ondan yana çekilir. Kelimelerin kalıbı da bu karşılığı destekler, çünkü sure üstünlük sıfatlarıyla örülüdür: Rab {ar:ٱلْأَعْلَى, tr:el-a'lâ, gloss:en yüce, source:87:1} diye anılır, varılan yer {ar:لِلْيُسْرَىٰ, tr:li'l-yusrâ, gloss:en kolaya, source:87:8}, öğütten kaçan {ar:ٱلْأَشْقَى, tr:el-eşkâ, gloss:en bedbaht, source:87:11}, onun girdiği ateş {ar:ٱلنَّارَ ٱلْكُبْرَىٰ, tr:en-nâra'l-kubrâ, gloss:en büyük ateş, source:87:12}, ahiret ise {ar:خَيْرٌۭ وَأَبْقَىٰٓ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:87:17}. Bu dizide "en kolay", en yücenin verdiği şeydir ve "en bedbaht"ın tam karşısında durur.

[¶14] Kur'an bu karşıtlığı gece ve gündüz üzerine yeminle açılan bir surede bir terazi gibi kurar. Veren, sakınan ve en güzeli doğrulayan için {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu en kolaya hazırlayacağız, source:92:7} der. Cimrilik eden, kendini ihtiyaçsız sayan ve en güzeli yalanlayan için ise {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-usrâ, gloss:onu en zora hazırlayacağız, source:92:10} der. Fiil de nesnenin yeri de aynıdır, kolaylaştırılan yine kişidir. Ama fiil bu kez iki yöne çalışır: insan en zora doğru da "kolaylaştırılabilir". Bu durum fiilin "hazırlamak, yatkın kılmak" anlamını iyice belirginleştirir. Kişi hangi yöne hazırlanırsa o yöne kolayca gider, en zorun yoluna bile kolayca kayar. Sekizinci ayet bu iki ihtimalden yalnız birini Peygamber'e söyler.

[¶15] O surenin devamı bu surenin kelimelerini neredeyse tek tek tekrarlar. Önce {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek bize düşer, source:92:12} der. Sonra alevlenen bir ateşle uyarır ve {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15} der. Ardından {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en çok sakınan ondan uzak tutulacak, source:92:17} der ve bu kişiyi malını verip {ar:يَتَزَكَّىٰ, tr:yetezekkâ, gloss:arınan, source:92:18} kişi diye tanıtır. Yol gösterme, en bedbaht, ateşe girmek, uzak tutulmak ve arınmak, bu surenin üçüncü, on birinci, on ikinci ve on dördüncü ayetlerindeki kelimelerdir. Yalnız bir noktada iki sure birbirinin tersine döner. Orada en çok sakınan ateşten uzak tutulur, burada en bedbaht öğütten uzak durur. Kolaylığa hazırlananla zorluğa hazırlanan arasındaki fark, kimin neyden uzak durduğunda görünür.

## Varlık, kısmet ve verilen kolaylık

[¶16] Kökün bir de maddi yüzü vardır. Genişliğe ve zenginliğe meysere ve yesâr denir. Zenginleşen adam için {ar:وقد أيسر الرجل أي استغنى, tr:ve kad eysera'r-raculu ey istağnâ, gloss:adam varlıklı oldu, yani ihtiyaçsız hâle geldi, source:"ي س ر,B003"} denir. Bu açıklamadaki ikinci fiil, gece suresinde en zora hazırlanan kişinin fiilidir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stağnâ, gloss:cimrilik eden ve kendini ihtiyaçsız sayana gelince, source:92:8}. Varlığın kolaylığına eren ve bu yüzden kendini kimseye muhtaç görmeyen kişi en zorun yoluna hazırlanır. Sure hemen ardından {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû iẕâ tereddâ, gloss:yuvarlanıp düştüğünde malı ona hiçbir fayda sağlamaz, source:92:11} der. En kolaya hazırlanan ise malını verendir. Kur'an meysere kelimesini sabır ve bağış bağlamında da kullanır. Borçlu darlıktaysa {ar:فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ, tr:fe-nazıratun ilâ meysera, gloss:eli genişleyinceye kadar ona süre tanınır, source:2:280}, borcu bağışlamak ise daha hayırlıdır. Bu ayetlerde varlık kolaylığın kendisi değildir, insanın kolaylığa hazırlanıp hazırlanmadığının sınandığı yerdir. Sekizinci ayetteki "en kolay", malla gelen kolaylıktan başka bir şeydir.

[¶17] Kökün en beklenmedik kullanımı bir oyundur. Araplar bir araya gelip bir deve keser, parçalarını oklarla bölüşürlerdi ve bu oyuna meysir derlerdi. Toplananlar için {ar:الأيسار: القوم يجتمعون على الميسر، واحدهم يسر, tr:el-eysâr el-kavmu yectemiûne ale'l-meysir, vâhiduhum yesar, gloss:eysâr meysir için toplanan topluluktur; tekili yesar, source:"ي س ر,B007"} denirdi. Okları çeken oyuncunun adı {ar:الياسر: اللاعب بالقداح, tr:el-yâsir el-lâibu bi'l-kıdâh, gloss:yâsir oklarla oynayan kişidir, source:"ي س ر,B007"} idi. Deveyi bölüşmek de aynı kökten bir fiille söylenirdi: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yesera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını aralarında bölüştü, source:"ي س ر,B007"}. Oyunun işleyişi şudur: payı emek ya da hak değil, oyunda çekilen ok belirler. Kur'an bu oyunu adıyla anar ve hakkında {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:ikisinin günahı faydasından büyüktür, source:2:219} der. Başka bir yerde müminlere seslenip onu fal oklarıyla birlikte şeytanın işinden bir pislik sayar ve {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90} der.

[¶18] Oyunun adının sekizinci ayetteki fiille aynı kökten gelmesi, bir anlamın ötekinden doğduğunu göstermez. Ama ikisi yan yana konunca bir ayrım belirginleşir. Meysirde topluluk payını oklara bırakır. Sekizinci ayette ise "biz" diyen bir fail vardır: ikinci ve üçüncü ayetlerde yaratıp düzene koyan ve ölçüsünü koyan Rab. Ölçme ve paylaştırma sahnesi, üçüncü ayetteki ölçme fiilini bu ayetin köküyle buluşturur. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" kelimeleri, meysirin yasaklandığı ayette yan yana durur. Surede ise birincisi bedbahtın öğütten uzak durmasını, ikincisi arınanın kurtuluşunu anlatır. Meysirde pay şansa kalır. Sekizinci ayette ise kişi, kendisine verilecek olan en kolaya hazırlanır.

===== _commentary/v16/out/87_8/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: yusrā is the feminine elative (fuʿlā) of aysar
- memory: Turkish "müyesser" is the passive participle of yassara and in Turkish is said of things, not persons
- not written: B004 left hand/left side - Quran uses shimāl for the left; no theme here
- not written: B002 yasīr "little, easy" (e.g. "easy for God") - would scatter the focus
- not written: B006 sheep abundant in milk - fixed idiom, no link to the ayah's act
- not written: B008 palm creases / thigh brand - no bearing
- not written: B009 twisting downward, thrust at face level - no bearing
- not written: B010 place and person names, B011 young man - no bearing
- not written: 65:7 and 65:4 (ease after hardship, ease for the pious) - covered by 94:5-6 and 92
- not written: 18:88 Dhul-Qarnayn "yusrā" from our command - adds nothing to the theme

===== passages not cited (123) =====
## strong (this ayah's own list) (16)

- (19:97) [listed for 87:8] [cited in ¶9] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لِتُبَشِّرَ بِهِ ٱلْمُتَّقِينَ وَتُنذِرَ بِهِۦ قَوْمًۭا لُّدًّۭا
- (44:58) [listed for 87:8] [cited in ¶9] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (54:40) [listed for 87:8] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (65:7) [listed for 87:8] لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ ۖ وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ ۚ لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا ۚ سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا
- (73:20) [listed for 87:8] [cited in ¶10] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ
- (80:19) [listed for 87:8] مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ
- (80:20) [listed for 87:8] [cited in ¶2] ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ
- (92:5) [listed for 87:8] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (92:6) [listed for 87:8] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:7) [listed for 87:8] [cited in ¶14] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (92:8) [listed for 87:8] [cited in ¶16] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- (92:9) [listed for 87:8] وَكَذَّبَ بِٱلْحُسْنَىٰ
- (92:10) [listed for 87:8] [cited in ¶14] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:11) [listed for 87:8] [cited in ¶16] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (94:5) [listed for 87:8] فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- (94:7) [listed for 87:8] [cited in ¶12] فَإِذَا فَرَغْتَ فَٱنصَبْ

## medium (this ayah's own list) (34)

- (2:185) [listed for 87:8] [cited in ¶10] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
- (2:280) [listed for 87:8] [cited in ¶16] وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (2:286) [listed for 87:8] لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا ٱكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَآ إِصْرًۭا كَمَا حَمَلْتَهُۥ عَلَى ٱلَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِۦ ۖ وَٱعْفُ عَنَّا وَٱغْفِرْ لَنَا وَٱرْحَمْنَآ ۚ أَنتَ مَوْلَىٰنَا فَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (4:28) [listed for 87:8] يُرِيدُ ٱللَّهُ أَن يُخَفِّفَ عَنكُمْ ۚ وَخُلِقَ ٱلْإِنسَٰنُ ضَعِيفًۭا
- (5:6) [listed for 87:8] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (5:90) [listed for 87:8] [cited in ¶17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
- (7:157) [listed for 87:8] ٱلَّذِينَ يَتَّبِعُونَ ٱلرَّسُولَ ٱلنَّبِىَّ ٱلْأُمِّىَّ ٱلَّذِى يَجِدُونَهُۥ مَكْتُوبًا عِندَهُمْ فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ يَأْمُرُهُم بِٱلْمَعْرُوفِ وَيَنْهَىٰهُمْ عَنِ ٱلْمُنكَرِ وَيُحِلُّ لَهُمُ ٱلطَّيِّبَٰتِ وَيُحَرِّمُ عَلَيْهِمُ ٱلْخَبَٰٓئِثَ وَيَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ بِهِۦ وَعَزَّرُوهُ وَنَصَرُوهُ وَٱتَّبَعُوا۟ ٱلنُّورَ ٱلَّذِىٓ أُنزِلَ مَعَهُۥٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (17:28) [listed for 87:8] وَإِمَّا تُعْرِضَنَّ عَنْهُمُ ٱبْتِغَآءَ رَحْمَةٍۢ مِّن رَّبِّكَ تَرْجُوهَا فَقُل لَّهُمْ قَوْلًۭا مَّيْسُورًۭا
- (18:88) [listed for 87:8] وَأَمَّا مَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا فَلَهُۥ جَزَآءً ٱلْحُسْنَىٰ ۖ وَسَنَقُولُ لَهُۥ مِنْ أَمْرِنَا يُسْرًۭا
- (20:25) [listed for 87:8] قَالَ رَبِّ ٱشْرَحْ لِى صَدْرِى
- (20:26) [listed for 87:8] [cited in ¶2] وَيَسِّرْ لِىٓ أَمْرِى
- (20:27) [listed for 87:8] وَٱحْلُلْ عُقْدَةًۭ مِّن لِّسَانِى
- (20:28) [listed for 87:8] يَفْقَهُوا۟ قَوْلِى
- (20:34) [listed for 87:8] وَنَذْكُرَكَ كَثِيرًا
- (22:78) [listed for 87:8] وَجَٰهِدُوا۟ فِى ٱللَّهِ حَقَّ جِهَادِهِۦ ۚ هُوَ ٱجْتَبَىٰكُمْ وَمَا جَعَلَ عَلَيْكُمْ فِى ٱلدِّينِ مِنْ حَرَجٍۢ ۚ مِّلَّةَ أَبِيكُمْ إِبْرَٰهِيمَ ۚ هُوَ سَمَّىٰكُمُ ٱلْمُسْلِمِينَ مِن قَبْلُ وَفِى هَٰذَا لِيَكُونَ ٱلرَّسُولُ شَهِيدًا عَلَيْكُمْ وَتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ ۚ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱعْتَصِمُوا۟ بِٱللَّهِ هُوَ مَوْلَىٰكُمْ ۖ فَنِعْمَ ٱلْمَوْلَىٰ وَنِعْمَ ٱلنَّصِيرُ
- (36:4) [listed for 87:8] عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (50:44) [listed for 87:8] يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًۭا ۚ ذَٰلِكَ حَشْرٌ عَلَيْنَا يَسِيرٌۭ
- (50:45) [listed for 87:8] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
- (51:3) [listed for 87:8] [cited in ¶7] فَٱلْجَٰرِيَٰتِ يُسْرًۭا
- (51:4) [listed for 87:8] فَٱلْمُقَسِّمَٰتِ أَمْرًا
- (54:17) [listed for 87:8] [cited in ¶9] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (57:22) [listed for 87:8] مَآ أَصَابَ مِن مُّصِيبَةٍۢ فِى ٱلْأَرْضِ وَلَا فِىٓ أَنفُسِكُمْ إِلَّا فِى كِتَٰبٍۢ مِّن قَبْلِ أَن نَّبْرَأَهَآ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (65:4) [listed for 87:8] وَٱلَّٰٓـِٔى يَئِسْنَ مِنَ ٱلْمَحِيضِ مِن نِّسَآئِكُمْ إِنِ ٱرْتَبْتُمْ فَعِدَّتُهُنَّ ثَلَٰثَةُ أَشْهُرٍۢ وَٱلَّٰٓـِٔى لَمْ يَحِضْنَ ۚ وَأُو۟لَٰتُ ٱلْأَحْمَالِ أَجَلُهُنَّ أَن يَضَعْنَ حَمْلَهُنَّ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا
- (74:10) [listed for 87:8] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (79:19) [listed for 87:8] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- (84:8) [listed for 87:8] فَسَوْفَ يُحَاسَبُ حِسَابًۭا يَسِيرًۭا
- (90:10) [listed for 87:8] وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- (91:8) [listed for 87:8] فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- (92:4) [listed for 87:8] إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- (92:12) [listed for 87:8] [cited in ¶15] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (94:2) [listed for 87:8] [cited in ¶7] وَوَضَعْنَا عَنكَ وِزْرَكَ
- (94:3) [listed for 87:8] [cited in ¶7] ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- (94:6) [listed for 87:8] [cited in ¶7] إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- (94:8) [listed for 87:8] [cited in ¶12] وَإِلَىٰ رَبِّكَ فَٱرْغَب

## named by the passage's own list as strong for this ayah (1)

- (54:22) [listed for 87:8] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ

## named by the passage's own list as medium for this ayah (5)

- (12:65) [listed for 87:8] وَلَمَّا فَتَحُوا۟ مَتَٰعَهُمْ وَجَدُوا۟ بِضَٰعَتَهُمْ رُدَّتْ إِلَيْهِمْ ۖ قَالُوا۟ يَٰٓأَبَانَا مَا نَبْغِى ۖ هَٰذِهِۦ بِضَٰعَتُنَا رُدَّتْ إِلَيْنَا ۖ وَنَمِيرُ أَهْلَنَا وَنَحْفَظُ أَخَانَا وَنَزْدَادُ كَيْلَ بَعِيرٍۢ ۖ ذَٰلِكَ كَيْلٌۭ يَسِيرٌۭ
- (41:41) [listed for 87:8] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (54:32) [listed for 87:8] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (81:26) [listed for 87:8] فَأَيْنَ تَذْهَبُونَ
- (97:1) [listed for 87:8] إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ

## weak (this ayah's own list) (22)

- (2:196) [listed for 87:8] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (2:219) [listed for 87:8] [cited in ¶17] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ ۖ قُلْ فِيهِمَآ إِثْمٌۭ كَبِيرٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا ۗ وَيَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ قُلِ ٱلْعَفْوَ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (4:30) [listed for 87:8] وَمَن يَفْعَلْ ذَٰلِكَ عُدْوَٰنًۭا وَظُلْمًۭا فَسَوْفَ نُصْلِيهِ نَارًۭا ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًا
- (5:91) [listed for 87:8] إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
- (6:128) [listed for 87:8] وَيَوْمَ يَحْشُرُهُمْ جَمِيعًۭا يَٰمَعْشَرَ ٱلْجِنِّ قَدِ ٱسْتَكْثَرْتُم مِّنَ ٱلْإِنسِ ۖ وَقَالَ أَوْلِيَآؤُهُم مِّنَ ٱلْإِنسِ رَبَّنَا ٱسْتَمْتَعَ بَعْضُنَا بِبَعْضٍۢ وَبَلَغْنَآ أَجَلَنَا ٱلَّذِىٓ أَجَّلْتَ لَنَا ۚ قَالَ ٱلنَّارُ مَثْوَىٰكُمْ خَٰلِدِينَ فِيهَآ إِلَّا مَا شَآءَ ٱللَّهُ ۗ إِنَّ رَبَّكَ حَكِيمٌ عَلِيمٌۭ
- (13:33) [listed for 87:8] أَفَمَنْ هُوَ قَآئِمٌ عَلَىٰ كُلِّ نَفْسٍۭ بِمَا كَسَبَتْ ۗ وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ قُلْ سَمُّوهُمْ ۚ أَمْ تُنَبِّـُٔونَهُۥ بِمَا لَا يَعْلَمُ فِى ٱلْأَرْضِ أَم بِظَٰهِرٍۢ مِّنَ ٱلْقَوْلِ ۗ بَلْ زُيِّنَ لِلَّذِينَ كَفَرُوا۟ مَكْرُهُمْ وَصُدُّوا۟ عَنِ ٱلسَّبِيلِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (15:39) [listed for 87:8] قَالَ رَبِّ بِمَآ أَغْوَيْتَنِى لَأُزَيِّنَنَّ لَهُمْ فِى ٱلْأَرْضِ وَلَأُغْوِيَنَّهُمْ أَجْمَعِينَ
- (22:70) [listed for 87:8] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَآءِ وَٱلْأَرْضِ ۗ إِنَّ ذَٰلِكَ فِى كِتَٰبٍ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (25:46) [listed for 87:8] ثُمَّ قَبَضْنَٰهُ إِلَيْنَا قَبْضًۭا يَسِيرًۭا
- (26:90) [listed for 87:8] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ
- (29:19) [listed for 87:8] أَوَلَمْ يَرَوْا۟ كَيْفَ يُبْدِئُ ٱللَّهُ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥٓ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (31:3) [listed for 87:8] هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ
- (41:44) [listed for 87:8] وَلَوْ جَعَلْنَٰهُ قُرْءَانًا أَعْجَمِيًّۭا لَّقَالُوا۟ لَوْلَا فُصِّلَتْ ءَايَٰتُهُۥٓ ۖ ءَا۬عْجَمِىٌّۭ وَعَرَبِىٌّۭ ۗ قُلْ هُوَ لِلَّذِينَ ءَامَنُوا۟ هُدًۭى وَشِفَآءٌۭ ۖ وَٱلَّذِينَ لَا يُؤْمِنُونَ فِىٓ ءَاذَانِهِمْ وَقْرٌۭ وَهُوَ عَلَيْهِمْ عَمًى ۚ أُو۟لَٰٓئِكَ يُنَادَوْنَ مِن مَّكَانٍۭ بَعِيدٍۢ
- (47:5) [listed for 87:8] سَيَهْدِيهِمْ وَيُصْلِحُ بَالَهُمْ
- (72:6) [listed for 87:8] وَأَنَّهُۥ كَانَ رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ فَزَادُوهُمْ رَهَقًۭا
- (74:7) [listed for 87:8] وَلِرَبِّكَ فَٱصْبِرْ
- (74:17) [listed for 87:8] سَأُرْهِقُهُۥ صَعُودًا
- (84:19) [listed for 87:8] لَتَرْكَبُنَّ طَبَقًا عَن طَبَقٍۢ
- (89:4) [listed for 87:8] وَٱلَّيْلِ إِذَا يَسْرِ
- (93:5) [listed for 87:8] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (94:1) [listed for 87:8] أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- (94:4) [listed for 87:8] وَرَفَعْنَا لَكَ ذِكْرَكَ

## named by the passage's own list as weak for this ayah (1)

- (26:219) [listed for 87:8] وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ

## neighbours: within two ayat of a passage the commentary cites (44)

- (2:183) [next to 2:185] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُتِبَ عَلَيْكُمُ ٱلصِّيَامُ كَمَا كُتِبَ عَلَى ٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
- (2:184) [next to 2:185] أَيَّامًۭا مَّعْدُودَٰتٍۢ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۚ وَعَلَى ٱلَّذِينَ يُطِيقُونَهُۥ فِدْيَةٌۭ طَعَامُ مِسْكِينٍۢ ۖ فَمَن تَطَوَّعَ خَيْرًۭا فَهُوَ خَيْرٌۭ لَّهُۥ ۚ وَأَن تَصُومُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (2:186) [next to 2:185] وَإِذَا سَأَلَكَ عِبَادِى عَنِّى فَإِنِّى قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ ۖ فَلْيَسْتَجِيبُوا۟ لِى وَلْيُؤْمِنُوا۟ بِى لَعَلَّهُمْ يَرْشُدُونَ
- (2:187) [next to 2:185] أُحِلَّ لَكُمْ لَيْلَةَ ٱلصِّيَامِ ٱلرَّفَثُ إِلَىٰ نِسَآئِكُمْ ۚ هُنَّ لِبَاسٌۭ لَّكُمْ وَأَنتُمْ لِبَاسٌۭ لَّهُنَّ ۗ عَلِمَ ٱللَّهُ أَنَّكُمْ كُنتُمْ تَخْتَانُونَ أَنفُسَكُمْ فَتَابَ عَلَيْكُمْ وَعَفَا عَنكُمْ ۖ فَٱلْـَٰٔنَ بَٰشِرُوهُنَّ وَٱبْتَغُوا۟ مَا كَتَبَ ٱللَّهُ لَكُمْ ۚ وَكُلُوا۟ وَٱشْرَبُوا۟ حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ ۖ ثُمَّ أَتِمُّوا۟ ٱلصِّيَامَ إِلَى ٱلَّيْلِ ۚ وَلَا تُبَٰشِرُوهُنَّ وَأَنتُمْ عَٰكِفُونَ فِى ٱلْمَسَٰجِدِ ۗ تِلْكَ حُدُودُ ٱللَّهِ فَلَا تَقْرَبُوهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَّقُونَ
- (2:217) [next to 2:219] يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ ۖ وَصَدٌّ عَن سَبِيلِ ٱللَّهِ وَكُفْرٌۢ بِهِۦ وَٱلْمَسْجِدِ ٱلْحَرَامِ وَإِخْرَاجُ أَهْلِهِۦ مِنْهُ أَكْبَرُ عِندَ ٱللَّهِ ۚ وَٱلْفِتْنَةُ أَكْبَرُ مِنَ ٱلْقَتْلِ ۗ وَلَا يَزَالُونَ يُقَٰتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ ٱسْتَطَٰعُوا۟ ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِۦ فَيَمُتْ وَهُوَ كَافِرٌۭ فَأُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:218) [next to 2:219] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَاجَرُوا۟ وَجَٰهَدُوا۟ فِى سَبِيلِ ٱللَّهِ أُو۟لَٰٓئِكَ يَرْجُونَ رَحْمَتَ ٱللَّهِ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (2:220) [next to 2:219] فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۗ وَيَسْـَٔلُونَكَ عَنِ ٱلْيَتَٰمَىٰ ۖ قُلْ إِصْلَاحٌۭ لَّهُمْ خَيْرٌۭ ۖ وَإِن تُخَالِطُوهُمْ فَإِخْوَٰنُكُمْ ۚ وَٱللَّهُ يَعْلَمُ ٱلْمُفْسِدَ مِنَ ٱلْمُصْلِحِ ۚ وَلَوْ شَآءَ ٱللَّهُ لَأَعْنَتَكُمْ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (2:221) [next to 2:219] وَلَا تَنكِحُوا۟ ٱلْمُشْرِكَٰتِ حَتَّىٰ يُؤْمِنَّ ۚ وَلَأَمَةٌۭ مُّؤْمِنَةٌ خَيْرٌۭ مِّن مُّشْرِكَةٍۢ وَلَوْ أَعْجَبَتْكُمْ ۗ وَلَا تُنكِحُوا۟ ٱلْمُشْرِكِينَ حَتَّىٰ يُؤْمِنُوا۟ ۚ وَلَعَبْدٌۭ مُّؤْمِنٌ خَيْرٌۭ مِّن مُّشْرِكٍۢ وَلَوْ أَعْجَبَكُمْ ۗ أُو۟لَٰٓئِكَ يَدْعُونَ إِلَى ٱلنَّارِ ۖ وَٱللَّهُ يَدْعُوٓا۟ إِلَى ٱلْجَنَّةِ وَٱلْمَغْفِرَةِ بِإِذْنِهِۦ ۖ وَيُبَيِّنُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (2:278) [next to 2:280] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَذَرُوا۟ مَا بَقِىَ مِنَ ٱلرِّبَوٰٓا۟ إِن كُنتُم مُّؤْمِنِينَ
- (2:279) [next to 2:280] فَإِن لَّمْ تَفْعَلُوا۟ فَأْذَنُوا۟ بِحَرْبٍۢ مِّنَ ٱللَّهِ وَرَسُولِهِۦ ۖ وَإِن تُبْتُمْ فَلَكُمْ رُءُوسُ أَمْوَٰلِكُمْ لَا تَظْلِمُونَ وَلَا تُظْلَمُونَ
- (2:281) [next to 2:280] وَٱتَّقُوا۟ يَوْمًۭا تُرْجَعُونَ فِيهِ إِلَى ٱللَّهِ ۖ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (2:282) [next to 2:280] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (5:88) [next to 5:90] وَكُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ حَلَٰلًۭا طَيِّبًۭا ۚ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِىٓ أَنتُم بِهِۦ مُؤْمِنُونَ
- (5:89) [next to 5:90] لَا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا عَقَّدتُّمُ ٱلْأَيْمَٰنَ ۖ فَكَفَّٰرَتُهُۥٓ إِطْعَامُ عَشَرَةِ مَسَٰكِينَ مِنْ أَوْسَطِ مَا تُطْعِمُونَ أَهْلِيكُمْ أَوْ كِسْوَتُهُمْ أَوْ تَحْرِيرُ رَقَبَةٍۢ ۖ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ ۚ ذَٰلِكَ كَفَّٰرَةُ أَيْمَٰنِكُمْ إِذَا حَلَفْتُمْ ۚ وَٱحْفَظُوٓا۟ أَيْمَٰنَكُمْ ۚ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَشْكُرُونَ
- (5:92) [next to 5:90] وَأَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ وَٱحْذَرُوا۟ ۚ فَإِن تَوَلَّيْتُمْ فَٱعْلَمُوٓا۟ أَنَّمَا عَلَىٰ رَسُولِنَا ٱلْبَلَٰغُ ٱلْمُبِينُ
- (19:95) [next to 19:97] وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا
- (19:96) [next to 19:97] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَيَجْعَلُ لَهُمُ ٱلرَّحْمَٰنُ وُدًّۭا
- (19:98) [next to 19:97] وَكَمْ أَهْلَكْنَا قَبْلَهُم مِّن قَرْنٍ هَلْ تُحِسُّ مِنْهُم مِّنْ أَحَدٍ أَوْ تَسْمَعُ لَهُمْ رِكْزًۢا
- (20:0) [next to 20:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (20:1) [next to 20:2] طه
- (20:4) [next to 20:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:24) [next to 20:26] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (44:56) [next to 44:58] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
- (44:57) [next to 44:58] فَضْلًۭا مِّن رَّبِّكَ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (44:59) [next to 44:58] فَٱرْتَقِبْ إِنَّهُم مُّرْتَقِبُونَ
- (51:0) [next to 51:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (51:1) [next to 51:2] وَٱلذَّٰرِيَٰتِ ذَرْوًۭا
- (51:5) [next to 51:3] إِنَّمَا تُوعَدُونَ لَصَادِقٌۭ
- (54:15) [next to 54:17] وَلَقَد تَّرَكْنَٰهَآ ءَايَةًۭ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:16) [next to 54:17] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:18) [next to 54:17] كَذَّبَتْ عَادٌۭ فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:19) [next to 54:17] إِنَّآ أَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا فِى يَوْمِ نَحْسٍۢ مُّسْتَمِرٍّۢ
- (73:18) [next to 73:20] ٱلسَّمَآءُ مُنفَطِرٌۢ بِهِۦ ۚ كَانَ وَعْدُهُۥ مَفْعُولًا
- (73:19) [next to 73:20] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (80:18) [next to 80:20] مِنْ أَىِّ شَىْءٍ خَلَقَهُۥ
- (80:21) [next to 80:20] ثُمَّ أَمَاتَهُۥ فَأَقْبَرَهُۥ
- (80:22) [next to 80:20] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
- (92:13) [next to 92:11] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:14) [next to 92:12] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:16) [next to 92:15] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:19) [next to 92:17] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (92:20) [next to 92:18] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (94:0) [next to 94:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ

