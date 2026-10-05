Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:9; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_9/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_9.reading.tr.md (prose paragraphs numbered) =====
## Unutturulmayan hatırlatır

[¶1] Ayet bir "fe" ile, yani "öyleyse" anlamı veren bir bağlaçla açılır: {ar:فَذَكِّرْ, tr:fe-ẕekkir, gloss:öyleyse hatırlat, source:87:9}. Bu bağlaç emri hemen önceki üç ayete bağlar. Altıncı ayette Allah elçisine {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız da unutmayacaksın, source:87:6} der. Yedinci ayet bu sözü Allah'ın dilemesine bağlar. Sekizinci ayet de {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana yatkın kılacağız, source:87:8} der. Hatırlatma emri bu verilenlerin üzerine kurulur. Kendisine okutulan ve unutturulmayan kişiden şimdi başkalarına hatırlatması istenir.

[¶2] Arapça bu fiilin kökünü unutmanın karşıtı olarak tanımlar: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi hatırladım, yani onu unutmadım, source:"ذ ك ر,B003"}. Bu kökün ilk işi zihinde bir şeyi tutmaktır. Bir şeyi aklında tutan kişi {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey' ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; "o benim aklımda" denir, source:"ذ ك ر,B003"} diye konuşurdu. Ayetteki fiil bu kökün ettirgen kalıbıdır. Anlamı "birinin bir şeyi aklında tutmasını sağlamak"tır. Altıncı ayette unutmak elçiden uzaklaştırılmıştı. Dokuzuncu ayette aklında tutma işi ondan başkalarına geçer. İki ayet aynı kökü kullanmaz. Onları birbirine bağlayan, Arapçanın bu kökü unutmanın tam karşıtı olarak kurmasıdır.

[¶3] Türkçede "zikir" kelimesi daralmıştır. Bugün daha çok Allah'ın adlarının toplu ya da tek başına tekrar edilmesi anlaşılır. "Tezkire" resmî bir belge, "hatıra" da geçmişten kalan bir anı olmuştur. Arapça kelime ise önce zihinle ilgilidir: bir şeyi elden kaçırmamak, onu tutmak demektir. Sözle anma {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikru ceryu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinden akıp geçmesidir, source:"ذ ك ر,B004"} ve ibadet olarak anma bu kökün daha sonraki dallarıdır.

[¶4] Kur'an başka bir yerde bu sırayı açıkça kurar. Allah elçisine, kendisine gönderilenlerden önceki kavimlerin akıbetini anlattıktan sonra {ar:فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ, tr:fe'stemsik billeẕî ûhiye ileyk, gloss:sana vahyedilene sımsıkı tutun, source:43:43} der. Sonra da {ar:وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ, tr:ve innehû le-ẕikrun leke ve li-kavmik ve sevfe tus'elûn, gloss:o, senin için ve kavmin için bir zikirdir; hepiniz sorguya çekileceksiniz, source:43:44} diye ekler. Bu cümledeki zikir hem hatırlatma hem de şan olarak anlaşılmıştır. Araplar {ar:الذكر العلاء والشرف, tr:eẕ-ẕikru'l-alâu ve'ş-şeref, gloss:zikir yücelik ve şereftir, source:"ذ ك ر,B007"} derlerdi. Hangi anlam alınırsa alınsın sıra aynıdır: önce "sımsıkı tutun", sonra "senin için", en sonra "kavmin için". Bizim surede de önce okutma ve unutmama gelir, sonra hatırlatma.

## Hatırlatmak: kaçanı geri çağırmak

[¶5] Türkçe meal "öğüt" der. Ama ذكرى ilk anlamıyla yeni bir şey öğretmek değildir. Kişinin elinden kaçmış bir şeyi yeniden onun zihnine getirmektir. Kökün dönüşlü kalıbı için şu söylenir: {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür, elden kaçanı aramaktır, source:"ذ ك ر,B003"}. Peki surede elden kaçmış olan nedir? Sure buna iki yerden cevap verir. Başta herkesin gözü önünde olanı sayar: yaratmayı, düzene koymayı, ölçü koymayı, yol göstermeyi, otlağı çıkarıp sonra kararmış bir döküntüye çevirmeyi. Sonda ise {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâẕâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18} der. Yani hatırlatılan şey hem dünyada görülen bir şeydir hem de daha önce söylenmiş bir sözdür. Araplar peygamberlere indirilen kitaplara da bu adı verirdi: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîn ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntılarını içeren kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Kur'an da önceki bir kitabı bu adla anar. Allah, iyi kullarının yeryüzüne mirasçı olacağını Zebur'da {ar:مِنۢ بَعْدِ ٱلذِّكْرِ, tr:min ba'di'ẕ-ẕikr, gloss:zikirden sonra, source:21:105} yazdığını söyler. Burada "zikir", Zebur'dan önce gelmiş bir kitabın adıdır. Böylece dokuzuncu ayetteki hatırlatma ile on dokuzuncu ayetteki İbrahim'in ve Musa'nın sayfaları aynı kelimenin iki ucunda durur.

[¶6] Arapçada bu fiil iki nesne alabilir: kime hatırlatıldığı ve neyin hatırlatıldığı. Ayet ikisini de söylemez. Kökün bu kalıbı için şöyle denir: {ar:الذكرى اسم للتذكير والتذكير مجاوز, tr:eẕ-ẕikrâ ismun li't-teẕkîr ve't-teẕkîru mucâviz, gloss:zikrâ hatırlatmanın adıdır ve hatırlatma kişiden başkasına geçen bir iştir, source:"ذ ك ر,B009"}. Fiil başkasına geçer ama ayet o başkasının kim olduğunu belirtmez. Onu bir sonraki ayet doldurur: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi saygıyla titreyen hatırlayacaktır, source:87:10}. Neyin hatırlatıldığını ise on sekizinci ayetteki "bu" kelimesi gösterir.

[¶7] Sure içinde bu kök üç ayrı kalıpta görünür ve her seferinde başka birinin elindedir. Dokuzuncu ayette elçi hatırlatır. Onuncu ayette dinleyen, kaçanı arayan dönüşlü kalıpla hatırlamayı kendi üstüne alır. On beşinci ayette bu iş artık kimsenin yardımına muhtaç değildir ve yalın kalıpla söylenir: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekere'sme rabbihî fe-sallâ, gloss:Rabbinin adını anar ve namaz kılar, source:87:15}. Surenin ilk emri de elçiye {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1} diye verilmişti. "Rabbinin adı" ifadesi iki yerde de geçer. Hatırlatma, sonunda dinleyenin elçiye verilen ilk emri kendi dilinde yerine getirmesiyle tamamlanır. Hatırlatan bir şeyi verir, dinleyen onu arar. Bu ikisi buluşunca o şey dinleyenin kendi sözü olur.

## "Eğer fayda verirse": faydanın görünmeyen yeri

[¶8] {ar:إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:in nefeati'ẕ-ẕikrâ, gloss:eğer hatırlatma fayda verirse, source:87:9} bir şart cümlesidir. Fiil dişildir çünkü öznesi olan ذكرى dişildir. "Fayda vermek" de normalde bir nesne ister, ama ayette nesnesi yoktur. Kime fayda vereceği söylenmez. Faydanın nerede ortaya çıkacağını yedinci ayet sezdirir: {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açıkta olanı da gizli kalanı da bilir, source:87:7}. Hatırlatan yalnızca açıkta olanı görür. Sözün birinin içinde tutunup tutunmayacağı ise gizli kalan taraftadır. Onuncu ve on birinci ayet bu ayrımı insanlar üzerinden gösterir: içi saygıyla titreyen hatırlayacaktır, {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ise ondan uzak duracaktır, source:87:11}.

[¶9] Kur'an, sonucu baştan kestirmeye çalışan bir hatırlatıcıyı başka bir surede uyarır ve bunu bu ayetin kelimeleriyle yapar. Orada biri yüzünü ekşitip döner, çünkü yanına gözleri görmeyen bir adam gelmiştir. Sonra hitap ona çevrilir: {ar:وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ, tr:ve mâ yudrîke leallehû yezzekkâ, gloss:ne bilirsin, belki o arınacak, source:80:3}, {ar:أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ, tr:ev yeẕẕekkeru fe-tenfeahu'ẕ-ẕikrâ, gloss:ya da hatırlayacak da hatırlatma ona fayda verecek, source:80:4}. Kendini yeterli gören kişiye ilgi gösterilmiştir. Koşarak ve içi titreyerek gelen ise ihmal edilmiştir. Bu ihmal düzeltilirken bir sınır da çizilir: {ar:وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ, tr:ve mâ aleyke ellâ yezzekkâ, gloss:onun arınmamasından sen sorumlu değilsin, source:80:7}. Görünüşe bakarak "buna fayda vermez" demek, faydanın gizli yerini bildiğini sanmaktır. Bizim ayetteki şart bu yüzden bir hüküm vermez, bir yer gösterir. Fayda hatırlatanın elinde değil, dinleyenin içindedir. Başka bir surede bu iki taraf ayrı ayrı söylenir: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-ẕekkir innemâ ente muẕekkir, gloss:hatırlat, sen ancak bir hatırlatıcısın, source:88:21}, {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üzerinde bir zorba değilsin, source:88:22}. Bir yerde elçiye inkâr edenlerden yüz çevirmesi söylenir ve bunun için kınanmayacağı eklenir: {ar:فَتَوَلَّ عَنْهُمْ فَمَآ أَنتَ بِمَلُومٍۢ, tr:fe-tevelle anhum fe-mâ ente bi-melûm, gloss:onlardan yüz çevir, kınanacak değilsin, source:51:54}. Hemen ardından ise yine hatırlatma emri gelir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve ẕekkir fe-inne'ẕ-ẕikrâ tenfeu'l-mu'minîn, gloss:hatırlat, çünkü hatırlatma inananlara fayda verir, source:51:55}.

[¶10] Ayetteki "fayda" nesnesiz kaldığı için, faydayı hatırlatanın kendisinin görmesine de yer kalır. Kur'an bunu bir sahneyle anlatır. Deniz kıyısındaki bir kasabanın halkı cumartesi yasağını çiğner. Balıklar yasak günde yüzeye vurur, öbür günlerde gelmez. Kasabadan bir topluluk, öğüt verenlere sorar: {ar:لِمَ تَعِظُونَ قَوْمًا ۙ ٱللَّهُ مُهْلِكُهُمْ أَوْ مُعَذِّبُهُمْ عَذَابًۭا شَدِيدًۭا, tr:lime teizûne kavmen allâhu muhlikuhum ev muazzibuhum azâben şedîdâ, gloss:Allah'ın helak edeceği ya da çetin bir azapla cezalandıracağı bir kavme neden öğüt veriyorsunuz, source:7:164}. Onlar şöyle cevap verir: {ar:قَالُوا۟ مَعْذِرَةً إِلَىٰ رَبِّكُمْ وَلَعَلَّهُمْ يَتَّقُونَ, tr:kâlû ma'ziraten ilâ rabbikum ve leallehum yettekûn, gloss:Rabbinize karşı bir mazeret olsun diye; hem belki sakınırlar, source:7:164}. Sonrası şöyle anlatılır: {ar:فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦٓ أَنجَيْنَا ٱلَّذِينَ يَنْهَوْنَ عَنِ ٱلسُّوٓءِ, tr:fe-lemmâ nesû mâ ẕukkirû bihî enceyne'lleẕîne yenhevne ani's-sû', gloss:kendilerine hatırlatılanı unutunca kötülükten alıkoymaya çalışanları kurtardık, source:7:165}. Burada da altıncı ve dokuzuncu ayetteki karşıtlık vardır: hatırlatılanlar unutmuştur. Hatırlatma, hatırlatılanlara fayda vermemiş, hatırlatanlara vermiştir. Onlar Rablerine karşı mazeretlerini yerine getirmiş ve kurtulmuşlardır.

[¶11] Aynı kök bir şeyi daha gösterir. On birinci ayetteki "en bedbaht" kelimesinin kökü, Kur'an'ın elçiye verdiği bir güvencede de geçer. Allah {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana bedbaht olasın diye indirmedik, source:20:2} der ve şöyle devam eder: {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkiraten li-men yahşâ, gloss:ancak içi titreyen için bir hatırlatma olarak indirdik, source:20:3}. Sekizinci ayette elçiye "kolaylık" vaat edilmişti. On birinci ayette bedbahtlık, hatırlatmayı yanında tutup ondan uzak durana düşer. Hatırlatma elçiyi yıpratmak için verilmemiştir. Sonucun yükü, gizli kalan tarafta karar veren kişinin üzerindedir.

## Fayda: zararın karşıtı, iyiliğe taşıyan

[¶12] نفع kökü kendi başına bir yön taşır. Araplar faydayı önce zararın karşıtı olarak tanımlardı: {ar:النفع ضد الضر, tr:en-nef'u diddu'd-darr, gloss:fayda zararın zıddıdır, source:"ن ف ع,B001"}. Sonra da bir araç olarak: {ar:ما يستعان به في الوصول إلى الخيرات, tr:mâ yusteânu bihî fi'l-vusûli ile'l-hayrât, gloss:iyiliklere ulaşmak için yardım alınan şey, source:"ن ف ع,B001"}. Bu tanıma göre fayda bir varış yeri değil, oraya götüren şeydir. Hatırlatmanın faydası da kendisinde değil, götürdüğü yerdedir. Surede o yer on dördüncü ayetteki kurtuluşa ermek ve on beşinci ayetteki anmak ve namaz kılmaktır. Türkçeye geçen "menfaat" kelimesi kişisel çıkara kaymıştır. "Menfaatçi" bir kınama sözüdür. Arapçadaki fayda ise yüzünü başkasına döner. Araplar {ar:رجل نفاع إذا كان ينفع الناس ولا يضرهم, tr:raculun neffâun iẕâ kâne yenfau'n-nâse ve lâ yedurruhum, gloss:insanlara fayda verip zarar vermeyen kişiye neffâ' denir, source:"ن ف ع,B001"} derlerdi.

[¶13] Fayda ve zarar ikilisi, son ayette sayfaları anılan İbrahim'in kavmine yaptığı hatırlatmanın ölçüsüdür. Allah elçisine İbrahim'in haberini okumasını söyler. İbrahim babasına ve kavmine neye taptıklarını sorar. Putlara taptıklarını ve onların başından ayrılmadıklarını söylerler. İbrahim sorar: {ar:قَالَ هَلْ يَسْمَعُونَكُمْ إِذْ تَدْعُونَ, tr:kâle hel yesmeûnekum iẕ ted'ûn, gloss:dua ettiğinizde sizi duyuyorlar mı, source:26:72}, {ar:أَوْ يَنفَعُونَكُمْ أَوْ يَضُرُّونَ, tr:ev yenfeûnekum ev yedurrûn, gloss:yoksa size fayda ya da zarar mı veriyorlar, source:26:73}. Kavmi buna bir cevap veremez, yalnızca babalarını böyle bulduklarını söyler. İbrahim de Âlemlerin Rabbini anlatır: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Bu, surenin ikinci ve üçüncü ayetlerinin söylediğidir. Sözünü de faydanın son sınırıyla bitirir: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfeu mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88}, {ar:إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ, tr:illâ men etallâhe bi-kalbin selîm, gloss:ancak Allah'a temiz bir kalple gelen müstesna, source:26:89}. Başka bir anlatımda İbrahim putları kırdıktan sonra aynı soruyu sorar: {ar:أَفَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُكُمْ شَيْـًۭٔا وَلَا يَضُرُّكُمْ, tr:e-fe-ta'budûne min dûnillâhi mâ lâ yenfeukum şey'en ve lâ yedurrukum, gloss:Allah'ı bırakıp size hiçbir fayda da zarar da veremeyen şeylere mi tapıyorsunuz, source:21:66}. Mal ve oğullar on altıncı ayette tercih edilen dünya hayatının malıdır. İbrahim'in hatırlatması, insanın bel bağladığı şeylerin ölçüldüğü bir faydanın hatırlatmasıdır. Bizim ayetteki şart da bu ölçüyü taşır.

[¶14] Kur'an faydanın ne olduğunu bir sel sahnesinde de söyler. Gökten su iner, vadiler kendi ölçülerince akar, sel üstünde kabarık bir köpük taşır. Ziynet ya da eşya yapmak için ateşte eritilen madenin de benzer bir köpüğü olur. Sonra ayrım gelir: {ar:فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ, tr:fe-emme'z-zebedu fe-yeẕhebu cufâen ve emmâ mâ yenfau'n-nâse fe-yemkuŝu fi'l-ard, gloss:köpük atılıp gider; insanlara fayda veren ise yerde kalır, source:13:17}. Burada fayda, kalan şeyin adıdır. Bu sahne, beşinci ayetteki selin sürüklediği çerçöple ve on yedinci ayetteki "daha kalıcı" ile birlikte surenin büyük sel manzarasını kurar. Dokuzuncu ayetin bu manzaraya kattığı şey şudur: hatırlatmanın faydası, akıp gittikten sonra geride kalan sudur.

## Kırbanın yanı ve değnek

[¶15] Bu kök iki somut eşyaya da ad vermiştir. Bu adlar ayetteki "fayda vermek" anlamının yerine geçmez. Onun yanında duyulur ve faydanın nasıl bir şey olduğunu elle tutulur kılar.

[¶16] İlki deri bir su kabının parçasıdır. Mezâde yolda su taşımak için kullanılan büyük bir deri kaptır. Bu kabın iki yanındaki deri yarılır ve her yana bir parça yerleştirilir. Araplar bu parçaya nuf'a derlerdi: {ar:النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة, tr:en-nuf'atu fî cânibeyi'l-mezâde yuşakku'l-edîmu fe-yuc'alu fî kulli cânibin nuf'a, gloss:nuf'a, su kabının iki yanında deri yarılarak her yana konan parçadır, source:"ن ف ع,B002"}. Bu söz parçanın kabın duvarına yerleştirildiğinden başka bir şey söylemez. Ama bu kadarı da yeter: parça artık kabın kendi duvarıdır ve kabın yanlarını suyu tutacak biçimde tamamlar. "Fayda" kelimesinin kökü, suyu tutan bir kabın parçasına ad olmuştur. Sel sahnesinde fayda yerde kalan suydu. Burada da suyu tutan derinin bir parçasıdır. Hatırlatma ile ilgili kök de zaten tutmakla başlıyordu: zikir bir şeyi korumak, aklında tutmaktır. Hatırlatma, ancak tutulduğu bir kaba yerleşirse fayda verir. Kendisine okutulanı tutan elçi, başkalarında da bu tutmayı arar. Ailesinin resmini bütünleyen başka kökler de vardır. İkinci ayetteki "yarattı" fiili deriyi kesmeden önce ölçmeyi, birinci ayetteki "Rab" deriyi yağla terbiye etmeyi, yedinci ayetteki "açık" tulumu çalkalamayı, on birinci ayetteki "uzak durmak" ise kabın iki yanını adlandırır. Böylece surenin kelimeleri tek bir tulumda buluşur. Bu son kelimenin yanında bir ses yankısı da duyulur: fayda veren parça kabın yanına yerleştirilir, en bedbaht ise hatırlatmayı kendi yanında, uzakta tutar. Bu bir dil yankısıdır, ayetin kendi sözü değildir.

[¶17] İkinci eşya değnektir. Araplar değneğe nef'a da derlerdi ve bu adın faydadan türediğini söylerlerdi: {ar:النَّفعة العصا وهي فعلة من النفع, tr:en-nef'atu'l-asâ ve hiye fa'letun mine'n-nef', gloss:nef'a değnektir, adı faydadan gelir, source:"ن ف ع,B003"}. Değnek elde taşınır, yolda ona dayanılır, onunla hayvan sürülür. Fayda burada elden bırakılmayan ve yürürken iş gören bir şeydir. Kur'an değneğin bu işlerini, son ayette sayfaları anılan Musa'nın ağzından sayar. Kelime aynı değildir ama eşya aynıdır. Allah Musa'ya sağ elinde ne olduğunu sorar. Musa şöyle cevap verir: {ar:قَالَ هِىَ عَصَاىَ أَتَوَكَّؤُا۟ عَلَيْهَا وَأَهُشُّ بِهَا عَلَىٰ غَنَمِى وَلِىَ فِيهَا مَـَٔارِبُ أُخْرَىٰ, tr:kâle hiye asâye etevekkeu aleyhâ ve ehuşşu bihâ alâ ğanemî ve liye fîhâ meâribu uhrâ, gloss:bu benim değneğimdir; ona dayanırım, onunla koyunlarıma yaprak silkelerim, onda başka işlerim de var, source:20:18}. Ardından Allah ona değneği atmasını söyler ve değnek koşan bir yılana dönüşür. Sonra şöyle der: {ar:قَالَ خُذْهَا وَلَا تَخَفْ ۖ سَنُعِيدُهَا سِيرَتَهَا ٱلْأُولَىٰ, tr:kâle huẕhâ ve lâ tehaf se-nuîduhâ sîratehe'l-ûlâ, gloss:al onu, korkma; onu ilk hâline döndüreceğiz, source:20:21}. Musa'nın gündelik işler için kullandığı değnek bir anda bir ayete, bir işarete dönüşür, sonra yine eski hâline döner. Dokuzuncu ayetin "fayda"sı bu sırayı izler. Yolda dayanılan bir şey, aynı zamanda Rabbi gösteren bir işaret olabilir. Değnek surede bir başka kelimenin ailesinde de görünür. Üçüncü ayetteki "yol gösterdi" fiilinin ailesinde değnek, taşıyanın önünden gittiği için hâdî adını alır. İki kök aynı eşyayı ayrı yüzlerinden adlandırır: biri önden gidişinden, öbürü dayanılmasından.

===== _commentary/v16/out/87_9/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: mazāda is a large leather water bag for travel
- memory: ذكّر is the causative form II; يذّكّر is assimilated form V يتذكّر
- memory: ذكّر can take a person and a thing as objects; both omitted here
- memory: 43:44 dhikr read as honor (B007 phrase supports it)
- not written: ذ ك ر B001 male, offspring - unrelated to reminding, no theme
- not written: ذ ك ر B002 hard iron, sharp sword, heavy rain - ornament only, no Quranic support here
- not written: ذ ك ر B008 written deed of a right - fixed phrase, no textual tie to the pages
- not written: ذ ك ر B009 "كثرة الذكر" frequent remembrance - added nothing beyond 88:21
- not written: ن ف ع B003 trading in staves - no work in any theme
- not written: ذكرى/يسرى rhyme pattern - sound only, no meaning to build on
- not written: 6:70 "remind with it lest a soul be given up" - repeats 51:55's point

===== passages not cited (251) =====
## strong (this ayah's own list) (25)

- (7:201) [listed for 87:9] إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ
- (14:52) [listed for 87:9] هَٰذَا بَلَٰغٌۭ لِّلنَّاسِ وَلِيُنذَرُوا۟ بِهِۦ وَلِيَعْلَمُوٓا۟ أَنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ وَلِيَذَّكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (16:90) [listed for 87:9] ۞ إِنَّ ٱللَّهَ يَأْمُرُ بِٱلْعَدْلِ وَٱلْإِحْسَٰنِ وَإِيتَآئِ ذِى ٱلْقُرْبَىٰ وَيَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ وَٱلْبَغْىِ ۚ يَعِظُكُمْ لَعَلَّكُمْ تَذَكَّرُونَ
- (20:14) [listed for 87:9] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:113) [listed for 87:9] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
- (20:124) [listed for 87:9] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
- (21:2) [listed for 87:9] مَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّن رَّبِّهِم مُّحْدَثٍ إِلَّا ٱسْتَمَعُوهُ وَهُمْ يَلْعَبُونَ
- (21:50) [listed for 87:9] وَهَٰذَا ذِكْرٌۭ مُّبَارَكٌ أَنزَلْنَٰهُ ۚ أَفَأَنتُمْ لَهُۥ مُنكِرُونَ
- (25:29) [listed for 87:9] لَّقَدْ أَضَلَّنِى عَنِ ٱلذِّكْرِ بَعْدَ إِذْ جَآءَنِى ۗ وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًۭا
- (25:50) [listed for 87:9] وَلَقَدْ صَرَّفْنَٰهُ بَيْنَهُمْ لِيَذَّكَّرُوا۟ فَأَبَىٰٓ أَكْثَرُ ٱلنَّاسِ إِلَّا كُفُورًۭا
- (28:43) [listed for 87:9] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ مِنۢ بَعْدِ مَآ أَهْلَكْنَا ٱلْقُرُونَ ٱلْأُولَىٰ بَصَآئِرَ لِلنَّاسِ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُمْ يَتَذَكَّرُونَ
- (36:11) [listed for 87:9] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
- (38:29) [listed for 87:9] كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ مُبَٰرَكٌۭ لِّيَدَّبَّرُوٓا۟ ءَايَٰتِهِۦ وَلِيَتَذَكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:22) [listed for 87:9] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (39:23) [listed for 87:9] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (43:36) [listed for 87:9] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (50:37) [listed for 87:9] إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِمَن كَانَ لَهُۥ قَلْبٌ أَوْ أَلْقَى ٱلسَّمْعَ وَهُوَ شَهِيدٌۭ
- (57:16) [listed for 87:9] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (59:19) [listed for 87:9] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (65:11) [listed for 87:9] رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
- (74:31) [listed for 87:9] وَمَا جَعَلْنَآ أَصْحَٰبَ ٱلنَّارِ إِلَّا مَلَٰٓئِكَةًۭ ۙ وَمَا جَعَلْنَا عِدَّتَهُمْ إِلَّا فِتْنَةًۭ لِّلَّذِينَ كَفَرُوا۟ لِيَسْتَيْقِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَيَزْدَادَ ٱلَّذِينَ ءَامَنُوٓا۟ إِيمَٰنًۭا ۙ وَلَا يَرْتَابَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْمُؤْمِنُونَ ۙ وَلِيَقُولَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ وَٱلْكَٰفِرُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَمَا يَعْلَمُ جُنُودَ رَبِّكَ إِلَّا هُوَ ۚ وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ
- (74:49) [listed for 87:9] فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ
- (76:29) [listed for 87:9] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًۭا
- (80:4) [listed for 87:9] [cited in ¶9] أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ
- (88:21) [listed for 87:9] [cited in ¶9] فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ

## medium (this ayah's own list) (56)

- (2:152) [listed for 87:9] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
- (5:91) [listed for 87:9] إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
- (6:44) [listed for 87:9] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦ فَتَحْنَا عَلَيْهِمْ أَبْوَٰبَ كُلِّ شَىْءٍ حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ فَإِذَا هُم مُّبْلِسُونَ
- (6:69) [listed for 87:9] وَمَا عَلَى ٱلَّذِينَ يَتَّقُونَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَلَٰكِن ذِكْرَىٰ لَعَلَّهُمْ يَتَّقُونَ
- (6:158) [listed for 87:9] هَلْ يَنظُرُونَ إِلَّآ أَن تَأْتِيَهُمُ ٱلْمَلَٰٓئِكَةُ أَوْ يَأْتِىَ رَبُّكَ أَوْ يَأْتِىَ بَعْضُ ءَايَٰتِ رَبِّكَ ۗ يَوْمَ يَأْتِى بَعْضُ ءَايَٰتِ رَبِّكَ لَا يَنفَعُ نَفْسًا إِيمَٰنُهَا لَمْ تَكُنْ ءَامَنَتْ مِن قَبْلُ أَوْ كَسَبَتْ فِىٓ إِيمَٰنِهَا خَيْرًۭا ۗ قُلِ ٱنتَظِرُوٓا۟ إِنَّا مُنتَظِرُونَ
- (8:2) [listed for 87:9] إِنَّمَا ٱلْمُؤْمِنُونَ ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَإِذَا تُلِيَتْ عَلَيْهِمْ ءَايَٰتُهُۥ زَادَتْهُمْ إِيمَٰنًۭا وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (8:45) [listed for 87:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا لَقِيتُمْ فِئَةًۭ فَٱثْبُتُوا۟ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
- (9:67) [listed for 87:9] ٱلْمُنَٰفِقُونَ وَٱلْمُنَٰفِقَٰتُ بَعْضُهُم مِّنۢ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمُنكَرِ وَيَنْهَوْنَ عَنِ ٱلْمَعْرُوفِ وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ
- (10:98) [listed for 87:9] فَلَوْلَا كَانَتْ قَرْيَةٌ ءَامَنَتْ فَنَفَعَهَآ إِيمَٰنُهَآ إِلَّا قَوْمَ يُونُسَ لَمَّآ ءَامَنُوا۟ كَشَفْنَا عَنْهُمْ عَذَابَ ٱلْخِزْىِ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَمَتَّعْنَٰهُمْ إِلَىٰ حِينٍۢ
- (11:34) [listed for 87:9] وَلَا يَنفَعُكُمْ نُصْحِىٓ إِنْ أَرَدتُّ أَنْ أَنصَحَ لَكُمْ إِن كَانَ ٱللَّهُ يُرِيدُ أَن يُغْوِيَكُمْ ۚ هُوَ رَبُّكُمْ وَإِلَيْهِ تُرْجَعُونَ
- (11:114) [listed for 87:9] وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ وَزُلَفًۭا مِّنَ ٱلَّيْلِ ۚ إِنَّ ٱلْحَسَنَٰتِ يُذْهِبْنَ ٱلسَّيِّـَٔاتِ ۚ ذَٰلِكَ ذِكْرَىٰ لِلذَّٰكِرِينَ
- (13:17) [listed for 87:9] [cited in ¶14] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
- (14:5) [listed for 87:9] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ أَنْ أَخْرِجْ قَوْمَكَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (15:9) [listed for 87:9] إِنَّا نَحْنُ نَزَّلْنَا ٱلذِّكْرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ
- (16:44) [listed for 87:9] بِٱلْبَيِّنَٰتِ وَٱلزُّبُرِ ۗ وَأَنزَلْنَآ إِلَيْكَ ٱلذِّكْرَ لِتُبَيِّنَ لِلنَّاسِ مَا نُزِّلَ إِلَيْهِمْ وَلَعَلَّهُمْ يَتَفَكَّرُونَ
- (17:46) [listed for 87:9] وَجَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۚ وَإِذَا ذَكَرْتَ رَبَّكَ فِى ٱلْقُرْءَانِ وَحْدَهُۥ وَلَّوْا۟ عَلَىٰٓ أَدْبَٰرِهِمْ نُفُورًۭا
- (18:24) [listed for 87:9] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (18:28) [listed for 87:9] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (21:24) [listed for 87:9] أَمِ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ ۖ قُلْ هَاتُوا۟ بُرْهَٰنَكُمْ ۖ هَٰذَا ذِكْرُ مَن مَّعِىَ وَذِكْرُ مَن قَبْلِى ۗ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ ٱلْحَقَّ ۖ فَهُم مُّعْرِضُونَ
- (21:48) [listed for 87:9] وَلَقَدْ ءَاتَيْنَا مُوسَىٰ وَهَٰرُونَ ٱلْفُرْقَانَ وَضِيَآءًۭ وَذِكْرًۭا لِّلْمُتَّقِينَ
- (22:28) [listed for 87:9] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:35) [listed for 87:9] ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَٱلصَّٰبِرِينَ عَلَىٰ مَآ أَصَابَهُمْ وَٱلْمُقِيمِى ٱلصَّلَوٰةِ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (23:110) [listed for 87:9] فَٱتَّخَذْتُمُوهُمْ سِخْرِيًّا حَتَّىٰٓ أَنسَوْكُمْ ذِكْرِى وَكُنتُم مِّنْهُمْ تَضْحَكُونَ
- (24:37) [listed for 87:9] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
- (26:88) [listed for 87:9] [cited in ¶13] يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ
- (26:209) [listed for 87:9] ذِكْرَىٰ وَمَا كُنَّا ظَٰلِمِينَ
- (29:45) [listed for 87:9] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
- (33:41) [listed for 87:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (36:70) [listed for 87:9] لِّيُنذِرَ مَن كَانَ حَيًّۭا وَيَحِقَّ ٱلْقَوْلُ عَلَى ٱلْكَٰفِرِينَ
- (37:13) [listed for 87:9] وَإِذَا ذُكِّرُوا۟ لَا يَذْكُرُونَ
- (38:1) [listed for 87:9] صٓ ۚ وَٱلْقُرْءَانِ ذِى ٱلذِّكْرِ
- (40:54) [listed for 87:9] هُدًۭى وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (43:5) [listed for 87:9] أَفَنَضْرِبُ عَنكُمُ ٱلذِّكْرَ صَفْحًا أَن كُنتُمْ قَوْمًۭا مُّسْرِفِينَ
- (43:39) [listed for 87:9] وَلَن يَنفَعَكُمُ ٱلْيَوْمَ إِذ ظَّلَمْتُمْ أَنَّكُمْ فِى ٱلْعَذَابِ مُشْتَرِكُونَ
- (43:44) [listed for 87:9] [cited in ¶4] وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ
- (44:13) [listed for 87:9] أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ
- (50:45) [listed for 87:9] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
- (51:55) [listed for 87:9] [cited in ¶9] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
- (53:29) [listed for 87:9] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (54:40) [listed for 87:9] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (58:19) [listed for 87:9] ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ ۚ أَلَآ إِنَّ حِزْبَ ٱلشَّيْطَٰنِ هُمُ ٱلْخَٰسِرُونَ
- (62:9) [listed for 87:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (63:9) [listed for 87:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (65:10) [listed for 87:9] أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا ۖ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟ ۚ قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا
- (68:52) [listed for 87:9] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (69:48) [listed for 87:9] وَإِنَّهُۥ لَتَذْكِرَةٌۭ لِّلْمُتَّقِينَ
- (72:17) [listed for 87:9] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
- (73:8) [listed for 87:9] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
- (74:54) [listed for 87:9] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
- (74:55) [listed for 87:9] فَمَن شَآءَ ذَكَرَهُۥ
- (77:5) [listed for 87:9] فَٱلْمُلْقِيَٰتِ ذِكْرًا
- (80:11) [listed for 87:9] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
- (80:12) [listed for 87:9] فَمَن شَآءَ ذَكَرَهُۥ
- (81:27) [listed for 87:9] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (81:28) [listed for 87:9] لِمَن شَآءَ مِنكُمْ أَن يَسْتَقِيمَ
- (89:23) [listed for 87:9] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ

## named by the passage's own list as strong for this ayah (25)

- (6:126) [listed for 87:9] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
- (9:6) [listed for 87:9] وَإِنْ أَحَدٌۭ مِّنَ ٱلْمُشْرِكِينَ ٱسْتَجَارَكَ فَأَجِرْهُ حَتَّىٰ يَسْمَعَ كَلَٰمَ ٱللَّهِ ثُمَّ أَبْلِغْهُ مَأْمَنَهُۥ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْلَمُونَ
- (13:7) [listed for 87:9] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
- (16:125) [listed for 87:9] ٱدْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِٱلْحِكْمَةِ وَٱلْمَوْعِظَةِ ٱلْحَسَنَةِ ۖ وَجَٰدِلْهُم بِٱلَّتِى هِىَ أَحْسَنُ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ ۖ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (17:41) [listed for 87:9] وَلَقَدْ صَرَّفْنَا فِى هَٰذَا ٱلْقُرْءَانِ لِيَذَّكَّرُوا۟ وَمَا يَزِيدُهُمْ إِلَّا نُفُورًۭا
- (17:82) [listed for 87:9] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
- (20:44) [listed for 87:9] فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ
- (27:81) [listed for 87:9] وَمَآ أَنتَ بِهَٰدِى ٱلْعُمْىِ عَن ضَلَٰلَتِهِمْ ۖ إِن تُسْمِعُ إِلَّا مَن يُؤْمِنُ بِـَٔايَٰتِنَا فَهُم مُّسْلِمُونَ
- (37:3) [listed for 87:9] فَٱلتَّٰلِيَٰتِ ذِكْرًا
- (37:168) [listed for 87:9] لَوْ أَنَّ عِندَنَا ذِكْرًۭا مِّنَ ٱلْأَوَّلِينَ
- (38:49) [listed for 87:9] هَٰذَا ذِكْرٌۭ ۚ وَإِنَّ لِلْمُتَّقِينَ لَحُسْنَ مَـَٔابٍۢ
- (38:87) [listed for 87:9] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (39:18) [listed for 87:9] ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَىٰهُمُ ٱللَّهُ ۖ وَأُو۟لَٰٓئِكَ هُمْ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (44:58) [listed for 87:9] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (50:8) [listed for 87:9] تَبْصِرَةًۭ وَذِكْرَىٰ لِكُلِّ عَبْدٍۢ مُّنِيبٍۢ
- (51:49) [listed for 87:9] وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ
- (54:5) [listed for 87:9] حِكْمَةٌۢ بَٰلِغَةٌۭ ۖ فَمَا تُغْنِ ٱلنُّذُرُ
- (54:22) [listed for 87:9] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:51) [listed for 87:9] وَلَقَدْ أَهْلَكْنَآ أَشْيَاعَكُمْ فَهَلْ مِن مُّدَّكِرٍۢ
- (74:56) [listed for 87:9] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
- (76:25) [listed for 87:9] وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا
- (79:43) [listed for 87:9] فِيمَ أَنتَ مِن ذِكْرَىٰهَآ
- (80:3) [listed for 87:9] [cited in ¶9] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
- (80:6) [listed for 87:9] فَأَنتَ لَهُۥ تَصَدَّىٰ
- (80:7) [listed for 87:9] [cited in ¶9] وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ

## named by the passage's own list as medium for this ayah (65)

- (3:58) [listed for 87:9] ذَٰلِكَ نَتْلُوهُ عَلَيْكَ مِنَ ٱلْءَايَٰتِ وَٱلذِّكْرِ ٱلْحَكِيمِ
- (6:19) [listed for 87:9] قُلْ أَىُّ شَىْءٍ أَكْبَرُ شَهَٰدَةًۭ ۖ قُلِ ٱللَّهُ ۖ شَهِيدٌۢ بَيْنِى وَبَيْنَكُمْ ۚ وَأُوحِىَ إِلَىَّ هَٰذَا ٱلْقُرْءَانُ لِأُنذِرَكُم بِهِۦ وَمَنۢ بَلَغَ ۚ أَئِنَّكُمْ لَتَشْهَدُونَ أَنَّ مَعَ ٱللَّهِ ءَالِهَةً أُخْرَىٰ ۚ قُل لَّآ أَشْهَدُ ۚ قُلْ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ وَإِنَّنِى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:68) [listed for 87:9] وَإِذَا رَأَيْتَ ٱلَّذِينَ يَخُوضُونَ فِىٓ ءَايَٰتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦ ۚ وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (6:90) [listed for 87:9] أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا ۖ إِنْ هُوَ إِلَّا ذِكْرَىٰ لِلْعَٰلَمِينَ
- (7:2) [listed for 87:9] كِتَٰبٌ أُنزِلَ إِلَيْكَ فَلَا يَكُن فِى صَدْرِكَ حَرَجٌۭ مِّنْهُ لِتُنذِرَ بِهِۦ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
- (7:63) [listed for 87:9] أَوَعَجِبْتُمْ أَن جَآءَكُمْ ذِكْرٌۭ مِّن رَّبِّكُمْ عَلَىٰ رَجُلٍۢ مِّنكُمْ لِيُنذِرَكُمْ وَلِتَتَّقُوا۟ وَلَعَلَّكُمْ تُرْحَمُونَ
- (7:164) [listed for 87:9] [cited in ¶10] وَإِذْ قَالَتْ أُمَّةٌۭ مِّنْهُمْ لِمَ تَعِظُونَ قَوْمًا ۙ ٱللَّهُ مُهْلِكُهُمْ أَوْ مُعَذِّبُهُمْ عَذَابًۭا شَدِيدًۭا ۖ قَالُوا۟ مَعْذِرَةً إِلَىٰ رَبِّكُمْ وَلَعَلَّهُمْ يَتَّقُونَ
- (9:126) [listed for 87:9] أَوَلَا يَرَوْنَ أَنَّهُمْ يُفْتَنُونَ فِى كُلِّ عَامٍۢ مَّرَّةً أَوْ مَرَّتَيْنِ ثُمَّ لَا يَتُوبُونَ وَلَا هُمْ يَذَّكَّرُونَ
- (12:104) [listed for 87:9] وَمَا تَسْـَٔلُهُمْ عَلَيْهِ مِنْ أَجْرٍ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (13:19) [listed for 87:9] ۞ أَفَمَن يَعْلَمُ أَنَّمَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ كَمَنْ هُوَ أَعْمَىٰٓ ۚ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (13:28) [listed for 87:9] ٱلَّذِينَ ءَامَنُوا۟ وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ ٱللَّهِ ۗ أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ
- (14:25) [listed for 87:9] تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا ۗ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (15:6) [listed for 87:9] وَقَالُوا۟ يَٰٓأَيُّهَا ٱلَّذِى نُزِّلَ عَلَيْهِ ٱلذِّكْرُ إِنَّكَ لَمَجْنُونٌۭ
- (16:17) [listed for 87:9] أَفَمَن يَخْلُقُ كَمَن لَّا يَخْلُقُ ۗ أَفَلَا تَذَكَّرُونَ
- (16:43) [listed for 87:9] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ إِلَّا رِجَالًۭا نُّوحِىٓ إِلَيْهِمْ ۚ فَسْـَٔلُوٓا۟ أَهْلَ ٱلذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ
- (17:9) [listed for 87:9] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
- (17:89) [listed for 87:9] وَلَقَدْ صَرَّفْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍۢ فَأَبَىٰٓ أَكْثَرُ ٱلنَّاسِ إِلَّا كُفُورًۭا
- (18:6) [listed for 87:9] فَلَعَلَّكَ بَٰخِعٌۭ نَّفْسَكَ عَلَىٰٓ ءَاثَٰرِهِمْ إِن لَّمْ يُؤْمِنُوا۟ بِهَٰذَا ٱلْحَدِيثِ أَسَفًا
- (18:57) [listed for 87:9] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ فَأَعْرَضَ عَنْهَا وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ ۚ إِنَّا جَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۖ وَإِن تَدْعُهُمْ إِلَى ٱلْهُدَىٰ فَلَن يَهْتَدُوٓا۟ إِذًا أَبَدًۭا
- (18:101) [listed for 87:9] ٱلَّذِينَ كَانَتْ أَعْيُنُهُمْ فِى غِطَآءٍ عَن ذِكْرِى وَكَانُوا۟ لَا يَسْتَطِيعُونَ سَمْعًا
- (20:3) [listed for 87:9] [cited in ¶11] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
- (20:125) [listed for 87:9] قَالَ رَبِّ لِمَ حَشَرْتَنِىٓ أَعْمَىٰ وَقَدْ كُنتُ بَصِيرًۭا
- (21:10) [listed for 87:9] لَقَدْ أَنزَلْنَآ إِلَيْكُمْ كِتَٰبًۭا فِيهِ ذِكْرُكُمْ ۖ أَفَلَا تَعْقِلُونَ
- (21:84) [listed for 87:9] فَٱسْتَجَبْنَا لَهُۥ فَكَشَفْنَا مَا بِهِۦ مِن ضُرٍّۢ ۖ وَءَاتَيْنَٰهُ أَهْلَهُۥ وَمِثْلَهُم مَّعَهُمْ رَحْمَةًۭ مِّنْ عِندِنَا وَذِكْرَىٰ لِلْعَٰبِدِينَ
- (23:71) [listed for 87:9] وَلَوِ ٱتَّبَعَ ٱلْحَقُّ أَهْوَآءَهُمْ لَفَسَدَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ وَمَن فِيهِنَّ ۚ بَلْ أَتَيْنَٰهُم بِذِكْرِهِمْ فَهُمْ عَن ذِكْرِهِم مُّعْرِضُونَ
- (23:85) [listed for 87:9] سَيَقُولُونَ لِلَّهِ ۚ قُلْ أَفَلَا تَذَكَّرُونَ
- (24:1) [listed for 87:9] سُورَةٌ أَنزَلْنَٰهَا وَفَرَضْنَٰهَا وَأَنزَلْنَا فِيهَآ ءَايَٰتٍۭ بَيِّنَٰتٍۢ لَّعَلَّكُمْ تَذَكَّرُونَ
- (24:34) [listed for 87:9] وَلَقَدْ أَنزَلْنَآ إِلَيْكُمْ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ وَمَثَلًۭا مِّنَ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُمْ وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
- (25:18) [listed for 87:9] قَالُوا۟ سُبْحَٰنَكَ مَا كَانَ يَنۢبَغِى لَنَآ أَن نَّتَّخِذَ مِن دُونِكَ مِنْ أَوْلِيَآءَ وَلَٰكِن مَّتَّعْتَهُمْ وَءَابَآءَهُمْ حَتَّىٰ نَسُوا۟ ٱلذِّكْرَ وَكَانُوا۟ قَوْمًۢا بُورًۭا
- (25:73) [listed for 87:9] وَٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانًۭا
- (26:194) [listed for 87:9] عَلَىٰ قَلْبِكَ لِتَكُونَ مِنَ ٱلْمُنذِرِينَ
- (28:46) [listed for 87:9] وَمَا كُنتَ بِجَانِبِ ٱلطُّورِ إِذْ نَادَيْنَا وَلَٰكِن رَّحْمَةًۭ مِّن رَّبِّكَ لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (29:51) [listed for 87:9] أَوَلَمْ يَكْفِهِمْ أَنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ يُتْلَىٰ عَلَيْهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَرَحْمَةًۭ وَذِكْرَىٰ لِقَوْمٍۢ يُؤْمِنُونَ
- (32:22) [listed for 87:9] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ ثُمَّ أَعْرَضَ عَنْهَآ ۚ إِنَّا مِنَ ٱلْمُجْرِمِينَ مُنتَقِمُونَ
- (34:6) [listed for 87:9] وَيَرَى ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (36:19) [listed for 87:9] قَالُوا۟ طَٰٓئِرُكُم مَّعَكُمْ ۚ أَئِن ذُكِّرْتُم ۚ بَلْ أَنتُمْ قَوْمٌۭ مُّسْرِفُونَ
- (36:69) [listed for 87:9] وَمَا عَلَّمْنَٰهُ ٱلشِّعْرَ وَمَا يَنۢبَغِى لَهُۥٓ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ وَقُرْءَانٌۭ مُّبِينٌۭ
- (37:155) [listed for 87:9] أَفَلَا تَذَكَّرُونَ
- (38:43) [listed for 87:9] وَوَهَبْنَا لَهُۥٓ أَهْلَهُۥ وَمِثْلَهُم مَّعَهُمْ رَحْمَةًۭ مِّنَّا وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (38:46) [listed for 87:9] إِنَّآ أَخْلَصْنَٰهُم بِخَالِصَةٍۢ ذِكْرَى ٱلدَّارِ
- (40:58) [listed for 87:9] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَلَا ٱلْمُسِىٓءُ ۚ قَلِيلًۭا مَّا تَتَذَكَّرُونَ
- (41:41) [listed for 87:9] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (47:17) [listed for 87:9] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
- (47:18) [listed for 87:9] فَهَلْ يَنظُرُونَ إِلَّا ٱلسَّاعَةَ أَن تَأْتِيَهُم بَغْتَةًۭ ۖ فَقَدْ جَآءَ أَشْرَاطُهَا ۚ فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ
- (52:29) [listed for 87:9] فَذَكِّرْ فَمَآ أَنتَ بِنِعْمَتِ رَبِّكَ بِكَاهِنٍۢ وَلَا مَجْنُونٍ
- (54:15) [listed for 87:9] وَلَقَد تَّرَكْنَٰهَآ ءَايَةًۭ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:17) [listed for 87:9] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:25) [listed for 87:9] أَءُلْقِىَ ٱلذِّكْرُ عَلَيْهِ مِنۢ بَيْنِنَا بَلْ هُوَ كَذَّابٌ أَشِرٌۭ
- (54:32) [listed for 87:9] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (56:62) [listed for 87:9] وَلَقَدْ عَلِمْتُمُ ٱلنَّشْأَةَ ٱلْأُولَىٰ فَلَوْلَا تَذَكَّرُونَ
- (56:73) [listed for 87:9] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
- (62:2) [listed for 87:9] هُوَ ٱلَّذِى بَعَثَ فِى ٱلْأُمِّيِّۦنَ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍۢ
- (62:5) [listed for 87:9] مَثَلُ ٱلَّذِينَ حُمِّلُوا۟ ٱلتَّوْرَىٰةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ ٱلْحِمَارِ يَحْمِلُ أَسْفَارًۢا ۚ بِئْسَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِ ٱللَّهِ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (68:51) [listed for 87:9] وَإِن يَكَادُ ٱلَّذِينَ كَفَرُوا۟ لَيُزْلِقُونَكَ بِأَبْصَٰرِهِمْ لَمَّا سَمِعُوا۟ ٱلذِّكْرَ وَيَقُولُونَ إِنَّهُۥ لَمَجْنُونٌۭ
- (69:12) [listed for 87:9] لِنَجْعَلَهَا لَكُمْ تَذْكِرَةًۭ وَتَعِيَهَآ أُذُنٌۭ وَٰعِيَةٌۭ
- (69:42) [listed for 87:9] وَلَا بِقَوْلِ كَاهِنٍۢ ۚ قَلِيلًۭا مَّا تَذَكَّرُونَ
- (73:19) [listed for 87:9] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (74:1) [listed for 87:9] يَٰٓأَيُّهَا ٱلْمُدَّثِّرُ
- (74:48) [listed for 87:9] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
- (74:50) [listed for 87:9] كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ
- (79:35) [listed for 87:9] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (90:9) [listed for 87:9] وَلِسَانًۭا وَشَفَتَيْنِ
- (92:7) [listed for 87:9] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (92:14) [listed for 87:9] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (94:4) [listed for 87:9] وَرَفَعْنَا لَكَ ذِكْرَكَ

## weak (this ayah's own list) (21)

- (2:123) [listed for 87:9] وَٱتَّقُوا۟ يَوْمًۭا لَّا تَجْزِى نَفْسٌ عَن نَّفْسٍۢ شَيْـًۭٔا وَلَا يُقْبَلُ مِنْهَا عَدْلٌۭ وَلَا تَنفَعُهَا شَفَٰعَةٌۭ وَلَا هُمْ يُنصَرُونَ
- (2:219) [listed for 87:9] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ ۖ قُلْ فِيهِمَآ إِثْمٌۭ كَبِيرٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا ۗ وَيَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ قُلِ ٱلْعَفْوَ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (5:76) [listed for 87:9] قُلْ أَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَمْلِكُ لَكُمْ ضَرًّۭا وَلَا نَفْعًۭا ۚ وَٱللَّهُ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:71) [listed for 87:9] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (7:188) [listed for 87:9] قُل لَّآ أَمْلِكُ لِنَفْسِى نَفْعًۭا وَلَا ضَرًّا إِلَّا مَا شَآءَ ٱللَّهُ ۚ وَلَوْ كُنتُ أَعْلَمُ ٱلْغَيْبَ لَٱسْتَكْثَرْتُ مِنَ ٱلْخَيْرِ وَمَا مَسَّنِىَ ٱلسُّوٓءُ ۚ إِنْ أَنَا۠ إِلَّا نَذِيرٌۭ وَبَشِيرٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (10:49) [listed for 87:9] قُل لَّآ أَمْلِكُ لِنَفْسِى ضَرًّۭا وَلَا نَفْعًا إِلَّا مَا شَآءَ ٱللَّهُ ۗ لِكُلِّ أُمَّةٍ أَجَلٌ ۚ إِذَا جَآءَ أَجَلُهُمْ فَلَا يَسْتَـْٔخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
- (10:106) [listed for 87:9] وَلَا تَدْعُ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُكَ وَلَا يَضُرُّكَ ۖ فَإِن فَعَلْتَ فَإِنَّكَ إِذًۭا مِّنَ ٱلظَّٰلِمِينَ
- (12:21) [listed for 87:9] وَقَالَ ٱلَّذِى ٱشْتَرَىٰهُ مِن مِّصْرَ لِٱمْرَأَتِهِۦٓ أَكْرِمِى مَثْوَىٰهُ عَسَىٰٓ أَن يَنفَعَنَآ أَوْ نَتَّخِذَهُۥ وَلَدًۭا ۚ وَكَذَٰلِكَ مَكَّنَّا لِيُوسُفَ فِى ٱلْأَرْضِ وَلِنُعَلِّمَهُۥ مِن تَأْوِيلِ ٱلْأَحَادِيثِ ۚ وَٱللَّهُ غَالِبٌ عَلَىٰٓ أَمْرِهِۦ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (12:42) [listed for 87:9] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (13:16) [listed for 87:9] قُلْ مَن رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ قُلِ ٱللَّهُ ۚ قُلْ أَفَٱتَّخَذْتُم مِّن دُونِهِۦٓ أَوْلِيَآءَ لَا يَمْلِكُونَ لِأَنفُسِهِمْ نَفْعًۭا وَلَا ضَرًّۭا ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ أَمْ هَلْ تَسْتَوِى ٱلظُّلُمَٰتُ وَٱلنُّورُ ۗ أَمْ جَعَلُوا۟ لِلَّهِ شُرَكَآءَ خَلَقُوا۟ كَخَلْقِهِۦ فَتَشَٰبَهَ ٱلْخَلْقُ عَلَيْهِمْ ۚ قُلِ ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ وَهُوَ ٱلْوَٰحِدُ ٱلْقَهَّٰرُ
- (18:83) [listed for 87:9] وَيَسْـَٔلُونَكَ عَن ذِى ٱلْقَرْنَيْنِ ۖ قُلْ سَأَتْلُوا۟ عَلَيْكُم مِّنْهُ ذِكْرًا
- (20:89) [listed for 87:9] أَفَلَا يَرَوْنَ أَلَّا يَرْجِعُ إِلَيْهِمْ قَوْلًۭا وَلَا يَمْلِكُ لَهُمْ ضَرًّۭا وَلَا نَفْعًۭا
- (20:109) [listed for 87:9] يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَرَضِىَ لَهُۥ قَوْلًۭا
- (21:66) [listed for 87:9] [cited in ¶13] قَالَ أَفَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُكُمْ شَيْـًۭٔا وَلَا يَضُرُّكُمْ
- (21:105) [listed for 87:9] [cited in ¶5] وَلَقَدْ كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ أَنَّ ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ
- (22:12) [listed for 87:9] يَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَضُرُّهُۥ وَمَا لَا يَنفَعُهُۥ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
- (22:33) [listed for 87:9] لَكُمْ فِيهَا مَنَٰفِعُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ مَحِلُّهَآ إِلَى ٱلْبَيْتِ ٱلْعَتِيقِ
- (26:73) [listed for 87:9] [cited in ¶13] أَوْ يَنفَعُونَكُمْ أَوْ يَضُرُّونَ
- (33:16) [listed for 87:9] قُل لَّن يَنفَعَكُمُ ٱلْفِرَارُ إِن فَرَرْتُم مِّنَ ٱلْمَوْتِ أَوِ ٱلْقَتْلِ وَإِذًۭا لَّا تُمَتَّعُونَ إِلَّا قَلِيلًۭا
- (36:73) [listed for 87:9] وَلَهُمْ فِيهَا مَنَٰفِعُ وَمَشَارِبُ ۖ أَفَلَا يَشْكُرُونَ
- (40:52) [listed for 87:9] يَوْمَ لَا يَنفَعُ ٱلظَّٰلِمِينَ مَعْذِرَتُهُمْ ۖ وَلَهُمُ ٱللَّعْنَةُ وَلَهُمْ سُوٓءُ ٱلدَّارِ

## named by the passage's own list as weak for this ayah (6)

- (2:239) [listed for 87:9] فَإِنْ خِفْتُمْ فَرِجَالًا أَوْ رُكْبَانًۭا ۖ فَإِذَآ أَمِنتُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَمَا عَلَّمَكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (20:99) [listed for 87:9] كَذَٰلِكَ نَقُصُّ عَلَيْكَ مِنْ أَنۢبَآءِ مَا قَدْ سَبَقَ ۚ وَقَدْ ءَاتَيْنَٰكَ مِن لَّدُنَّا ذِكْرًۭا
- (25:56) [listed for 87:9] وَمَآ أَرْسَلْنَٰكَ إِلَّا مُبَشِّرًۭا وَنَذِيرًۭا
- (35:3) [listed for 87:9] يَٰٓأَيُّهَا ٱلنَّاسُ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ ۚ هَلْ مِنْ خَٰلِقٍ غَيْرُ ٱللَّهِ يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (46:21) [listed for 87:9] ۞ وَٱذْكُرْ أَخَا عَادٍ إِذْ أَنذَرَ قَوْمَهُۥ بِٱلْأَحْقَافِ وَقَدْ خَلَتِ ٱلنُّذُرُ مِنۢ بَيْنِ يَدَيْهِ وَمِنْ خَلْفِهِۦٓ أَلَّا تَعْبُدُوٓا۟ إِلَّا ٱللَّهَ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (60:3) [listed for 87:9] لَن تَنفَعَكُمْ أَرْحَامُكُمْ وَلَآ أَوْلَٰدُكُمْ ۚ يَوْمَ ٱلْقِيَٰمَةِ يَفْصِلُ بَيْنَكُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ

## neighbours: within two ayat of a passage the commentary cites (53)

- (7:162) [next to 7:164] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَرْسَلْنَا عَلَيْهِمْ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَظْلِمُونَ
- (7:163) [next to 7:164] وَسْـَٔلْهُمْ عَنِ ٱلْقَرْيَةِ ٱلَّتِى كَانَتْ حَاضِرَةَ ٱلْبَحْرِ إِذْ يَعْدُونَ فِى ٱلسَّبْتِ إِذْ تَأْتِيهِمْ حِيتَانُهُمْ يَوْمَ سَبْتِهِمْ شُرَّعًۭا وَيَوْمَ لَا يَسْبِتُونَ ۙ لَا تَأْتِيهِمْ ۚ كَذَٰلِكَ نَبْلُوهُم بِمَا كَانُوا۟ يَفْسُقُونَ
- (7:166) [next to 7:164] فَلَمَّا عَتَوْا۟ عَن مَّا نُهُوا۟ عَنْهُ قُلْنَا لَهُمْ كُونُوا۟ قِرَدَةً خَٰسِـِٔينَ
- (7:167) [next to 7:165] وَإِذْ تَأَذَّنَ رَبُّكَ لَيَبْعَثَنَّ عَلَيْهِمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَن يَسُومُهُمْ سُوٓءَ ٱلْعَذَابِ ۗ إِنَّ رَبَّكَ لَسَرِيعُ ٱلْعِقَابِ ۖ وَإِنَّهُۥ لَغَفُورٌۭ رَّحِيمٌۭ
- (13:15) [next to 13:17] وَلِلَّهِ يَسْجُدُ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ طَوْعًۭا وَكَرْهًۭا وَظِلَٰلُهُم بِٱلْغُدُوِّ وَٱلْءَاصَالِ ۩
- (13:18) [next to 13:17] لِلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمُ ٱلْحُسْنَىٰ ۚ وَٱلَّذِينَ لَمْ يَسْتَجِيبُوا۟ لَهُۥ لَوْ أَنَّ لَهُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لَٱفْتَدَوْا۟ بِهِۦٓ ۚ أُو۟لَٰٓئِكَ لَهُمْ سُوٓءُ ٱلْحِسَابِ وَمَأْوَىٰهُمْ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمِهَادُ
- (20:0) [next to 20:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (20:1) [next to 20:2] طه
- (20:4) [next to 20:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:16) [next to 20:18] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (20:17) [next to 20:18] وَمَا تِلْكَ بِيَمِينِكَ يَٰمُوسَىٰ
- (20:19) [next to 20:18] قَالَ أَلْقِهَا يَٰمُوسَىٰ
- (20:20) [next to 20:18] فَأَلْقَىٰهَا فَإِذَا هِىَ حَيَّةٌۭ تَسْعَىٰ
- (20:22) [next to 20:21] وَٱضْمُمْ يَدَكَ إِلَىٰ جَنَاحِكَ تَخْرُجْ بَيْضَآءَ مِنْ غَيْرِ سُوٓءٍ ءَايَةً أُخْرَىٰ
- (20:23) [next to 20:21] لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى
- (21:64) [next to 21:66] فَرَجَعُوٓا۟ إِلَىٰٓ أَنفُسِهِمْ فَقَالُوٓا۟ إِنَّكُمْ أَنتُمُ ٱلظَّٰلِمُونَ
- (21:65) [next to 21:66] ثُمَّ نُكِسُوا۟ عَلَىٰ رُءُوسِهِمْ لَقَدْ عَلِمْتَ مَا هَٰٓؤُلَآءِ يَنطِقُونَ
- (21:67) [next to 21:66] أُفٍّۢ لَّكُمْ وَلِمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ ۖ أَفَلَا تَعْقِلُونَ
- (21:68) [next to 21:66] قَالُوا۟ حَرِّقُوهُ وَٱنصُرُوٓا۟ ءَالِهَتَكُمْ إِن كُنتُمْ فَٰعِلِينَ
- (21:103) [next to 21:105] لَا يَحْزُنُهُمُ ٱلْفَزَعُ ٱلْأَكْبَرُ وَتَتَلَقَّىٰهُمُ ٱلْمَلَٰٓئِكَةُ هَٰذَا يَوْمُكُمُ ٱلَّذِى كُنتُمْ تُوعَدُونَ
- (21:104) [next to 21:105] يَوْمَ نَطْوِى ٱلسَّمَآءَ كَطَىِّ ٱلسِّجِلِّ لِلْكُتُبِ ۚ كَمَا بَدَأْنَآ أَوَّلَ خَلْقٍۢ نُّعِيدُهُۥ ۚ وَعْدًا عَلَيْنَآ ۚ إِنَّا كُنَّا فَٰعِلِينَ
- (21:106) [next to 21:105] إِنَّ فِى هَٰذَا لَبَلَٰغًۭا لِّقَوْمٍ عَٰبِدِينَ
- (21:107) [next to 21:105] وَمَآ أَرْسَلْنَٰكَ إِلَّا رَحْمَةًۭ لِّلْعَٰلَمِينَ
- (26:70) [next to 26:72] إِذْ قَالَ لِأَبِيهِ وَقَوْمِهِۦ مَا تَعْبُدُونَ
- (26:71) [next to 26:72] قَالُوا۟ نَعْبُدُ أَصْنَامًۭا فَنَظَلُّ لَهَا عَٰكِفِينَ
- (26:74) [next to 26:72] قَالُوا۟ بَلْ وَجَدْنَآ ءَابَآءَنَا كَذَٰلِكَ يَفْعَلُونَ
- (26:75) [next to 26:73] قَالَ أَفَرَءَيْتُم مَّا كُنتُمْ تَعْبُدُونَ
- (26:76) [next to 26:78] أَنتُمْ وَءَابَآؤُكُمُ ٱلْأَقْدَمُونَ
- (26:77) [next to 26:78] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
- (26:79) [next to 26:78] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (26:80) [next to 26:78] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (26:86) [next to 26:88] وَٱغْفِرْ لِأَبِىٓ إِنَّهُۥ كَانَ مِنَ ٱلضَّآلِّينَ
- (26:87) [next to 26:88] وَلَا تُخْزِنِى يَوْمَ يُبْعَثُونَ
- (26:90) [next to 26:88] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ
- (26:91) [next to 26:89] وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ
- (43:41) [next to 43:43] فَإِمَّا نَذْهَبَنَّ بِكَ فَإِنَّا مِنْهُم مُّنتَقِمُونَ
- (43:42) [next to 43:43] أَوْ نُرِيَنَّكَ ٱلَّذِى وَعَدْنَٰهُمْ فَإِنَّا عَلَيْهِم مُّقْتَدِرُونَ
- (43:45) [next to 43:43] وَسْـَٔلْ مَنْ أَرْسَلْنَا مِن قَبْلِكَ مِن رُّسُلِنَآ أَجَعَلْنَا مِن دُونِ ٱلرَّحْمَٰنِ ءَالِهَةًۭ يُعْبَدُونَ
- (43:46) [next to 43:44] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَقَالَ إِنِّى رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- (51:52) [next to 51:54] كَذَٰلِكَ مَآ أَتَى ٱلَّذِينَ مِن قَبْلِهِم مِّن رَّسُولٍ إِلَّا قَالُوا۟ سَاحِرٌ أَوْ مَجْنُونٌ
- (51:53) [next to 51:54] أَتَوَاصَوْا۟ بِهِۦ ۚ بَلْ هُمْ قَوْمٌۭ طَاغُونَ
- (51:56) [next to 51:54] وَمَا خَلَقْتُ ٱلْجِنَّ وَٱلْإِنسَ إِلَّا لِيَعْبُدُونِ
- (51:57) [next to 51:55] مَآ أُرِيدُ مِنْهُم مِّن رِّزْقٍۢ وَمَآ أُرِيدُ أَن يُطْعِمُونِ
- (80:1) [next to 80:3] عَبَسَ وَتَوَلَّىٰٓ
- (80:2) [next to 80:3] أَن جَآءَهُ ٱلْأَعْمَىٰ
- (80:5) [next to 80:3] أَمَّا مَنِ ٱسْتَغْنَىٰ
- (80:8) [next to 80:7] وَأَمَّا مَن جَآءَكَ يَسْعَىٰ
- (80:9) [next to 80:7] وَهُوَ يَخْشَىٰ
- (88:19) [next to 88:21] وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- (88:20) [next to 88:21] وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- (88:23) [next to 88:21] إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- (88:24) [next to 88:22] فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ

