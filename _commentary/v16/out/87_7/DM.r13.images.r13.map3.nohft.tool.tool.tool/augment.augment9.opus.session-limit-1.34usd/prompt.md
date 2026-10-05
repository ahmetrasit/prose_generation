Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:7; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_7.reading.tr.md (prose paragraphs numbered) =====
## Vaadin içindeki istisna

[¶1] Altıncı ayet Peygamber'e bir söz verir: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Yedinci ayet ayrı bir cümle olarak başlamaz. Bu sözün içinden konuşur: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği başka, source:87:7}. Cümlenin bütünü şöyle kurulur: sana okutulanı unutmayacaksın, Allah'ın dilediği şey dışında. Buradaki "mâ" kelimesi "o şey ki" demektir. Dışarıda bırakılan şey, unutulacak olandır. Altıncı ayetteki "lâ" bir yasak bildirmez, bir haber verir. Fiilin sonundaki uzun ünlü yerinde durur, yasak olsaydı düşerdi. Yani Peygamber'e "unutma" diye bir görev yüklenmez. Unutmamak ona verilmiş bir vaattir. Yedinci ayetin ilk yarısı bu vaadin kime ait olduğunu hatırlatır. Hafıza Peygamber'e devredilip artık onun malı olmuş bir güç değildir. Onu veren dileyenin elinde durur.

[¶2] Bu yarım cümlede küçük ama göze çarpan bir şey olur. Altıncı ayette konuşan ses "biz"dir ve "okutacağız" der. Sekizinci ayette de yine "biz" konuşur: {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana kolaylaştıracağız, source:87:8}. Birinci ayet {ar:رَبِّكَ, tr:rabbike, gloss:Rabbin, source:87:1} der, on beşinci ayet de "Rabbi" der. Allah adı ise bütün surede yalnızca burada, iki "biz" fiilinin arasında, istisnanın tam yerinde geçer. Dileyen kişisiz bir talih ya da adsız bir kader değildir, özel adıyla anılır. Bu ad, kulluk etmeyi anlatan kökle aynıdır: {ar:أصل واحد وهو التعبد, tr:aslun vâhidun ve huve't-teabbud, gloss:tek bir aslı vardır, o da kulluk etmektir, source:"ء ل ه,B001"}. Her namazda okunan Fâtiha övgüyü bu ada verir: {ar:ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:el-hamdu lillâhi rabbi'l-âlemîn, gloss:hamd âlemlerin Rabbi Allah'adır, source:1:2}. Ayet, unutmanın ve hatırlamanın sınırını kulluk edilen bu ada bağlar.

[¶3] Kur'an aynı düğümü başka bir yerde Peygamber'e doğrudan bir öğüt olarak açar. Mağara arkadaşlarının hikâyesinde insanlar onların kaç kişi olduğu üzerine tahmin yürütür. Peygamber'e "Rabbim onların sayısını daha iyi bilir" demesi söylenir {source:18:22}. Hemen ardından şu gelir: {ar:وَلَا تَقُولَنَّ لِشَا۟ىْءٍ إِنِّى فَاعِلٌۭ ذَٰلِكَ غَدًا, tr:ve lâ tekûlenne li-şey'in innî fâilun ẕâlike ğadâ, gloss:hiçbir şey için "bunu yarın yapacağım" deme, source:18:23}. Sonra şu gelir: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh veẕkur rabbeke iẕâ nesîte, gloss:ancak "Allah dilerse" diyerek söyle; unuttuğunda da Rabbini an, source:18:24}. Bilmek, dilemek, unutmak ve anmak bu iki ayette art arda dizilir. Ayet de Rabbin daha doğru olana yöneltmesini umarak biter. Bu surede de bunların hepsi vardır: üçüncü ayette yol göstermek, altıncı ayette unutmamak, yedinci ayette dilemek ve bilmek, dokuzuncu ayette hatırlatmak. Mağara hikâyesindeki öğüt, insanın kendi yarını için verdiği sözü Allah'ın dilemesine bağlar. Bu surede ise Allah'ın kendi verdiği söz bu dilemeyi içinde taşır.

[¶4] Kur'an bu istisnanın neye dayandığını da gösterir. Ruh hakkında soranlara "size bilgiden ancak az bir şey verildi" denir. Ardından Peygamber'e şöyle seslenilir: {ar:وَلَئِن شِئْنَا لَنَذْهَبَنَّ بِٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ, tr:ve le-in şi'nâ le-neẕhebenne billeẕî evhaynâ ileyk, gloss:dileseydik sana vahyettiğimizi elbette alıp götürürdük, source:17:86}. Bunu önleyen tek şey {ar:إِلَّا رَحْمَةًۭ مِّن رَّبِّكَ, tr:illâ rahmeten min rabbik, gloss:ancak Rabbinden bir rahmet, source:17:87} olur. Vahyin yerinde kalması bir hak değil, bir rahmettir. Başka bir yerde, Kitap ehlinden ve müşriklerden inkâr edenlerin müminlere Rablerinden bir hayır inmesini istemedikleri anlatılır. Sonra şu söylenir: {ar:مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ, tr:mâ nensah min âyetin ev nunsihâ ne'ti bi-hayrin minhâ ev mislihâ, gloss:bir ayeti kaldırır ya da unutturursak ondan daha hayırlısını ya da benzerini getiririz, source:2:106}. Unutturmak, Kur'an'ın kendi ağzından Allah'ın yaptığı bir iş olarak geçer. Ama yanında bir kayıp yoktur, daha iyisi ya da benzeri vardır. Yedinci ayetin istisnası da bu yüzden kaygıyla bitmez. Hemen arkasından kolaylık vaadi gelir.

[¶5] Aynı kalıp Kur'an'ın en kesin sözlerinin içine de konur. Allah cinleri ve onların insanlardan dostlarını bir araya topladığı günü anlatır, ateş için şöyle der: {ar:خَٰلِدِينَ فِيهَآ إِلَّا مَا شَآءَ ٱللَّهُ ۗ إِنَّ رَبَّكَ حَكِيمٌ عَلِيمٌۭ, tr:hâlidîne fîhâ illâ mâ şâallâh inne rabbeke hakîmun alîm, gloss:orada sürekli kalırsınız, Allah'ın dilediği başka; Rabbin hikmet sahibidir, bilendir, source:6:128}. Mutlu olanlar için de {ar:إِلَّا مَا شَآءَ رَبُّكَ ۖ عَطَآءً غَيْرَ مَجْذُوذٍۢ, tr:illâ mâ şâe rabbuk atâen ğayra mecẕûẕ, gloss:Rabbinin dilediği başka; kesintisiz bir bağış olarak, source:11:108} denir. İstisna bağışı kesmez, bağışın kimden geldiğini söyler. Ateş ayetinin yapısı yedinci ayetin yapısıyla aynıdır: önce "Allah'ın dilediği başka" denir, hemen ardından "O bilendir" gelir. Dilemek hiçbir yerde gelişigüzel bırakılmaz, bilmeyle birlikte söylenir. Yedinci ayetin ikinci yarısı bu işi görür.

## Dilenen şey, bilinen şey

[¶6] "Diledi" anlamındaki şâe ile "şey" anlamındaki şey' aynı köktendir. İsteme şöyle tanımlanır: {ar:المشيئة الإرادة وقد شئت الشئ أشاؤه, tr:el-meşîetu'l-irâdetu ve kad şi'tu'ş-şey'e eşâuh, gloss:meşîet istemektir; bir şeyi istedim, istiyorum, source:"ش ي ء,B002"}. Türkçede "şey" adını koyamadığımız her şeyin yerini tutan, neredeyse boş bir kelimeye dönüşmüştür. Konuşurken duraksadığımızda bile "şey" deriz. Arapçada ise bu kelime dilemekle aynı soydandır, bu yüzden hiç boş değildir. Şeyin tanımı da yedinci ayetin öbür yarısına uzanır: {ar:الذي يصح أن يعلم ويخبر عنه, tr:elleẕî yasıhhu en yu'leme ve yuhbere anh, gloss:bilinmesi ve hakkında haber verilmesi mümkün olan, source:"ش ي ء,B001"}. Bu tanımda ayetteki "bilir" fiilinin kökü geçer. Dilemenin aslı ise şöyle anlatılır: {ar:في الأصل إيجاد الشيء وإصابته, tr:fi'l-asl îcâdu'ş-şey'i ve isâbetuh, gloss:aslında bir şeyi var etmek ve onu tam yerinden tutturmak, source:"ش ي ء,B002"}. Fiil ile ismin aynı kökten geldiği kesindir. İkisi arasındaki bağı kurmak ise okumanın işidir. Allah'ın dilediği her şey bir "şey"dir, her şey de bilinebilir olandır. Ayetin iki yarısı, dilemek ve bilmek, aynı nesneye iki yandan bakar. Unutulması dilenen şey de bir şeydir, şey olduğu için de bilinir.

[¶7] Kur'an "şey" kelimesini yedinci ayetin son fiiliyle tekrar tekrar yan yana getirir: {ar:إِنَّ ٱللَّهَ لَا يَخْفَىٰ عَلَيْهِ شَىْءٌۭ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ, tr:innallâhe lâ yahfâ aleyhi şey'un fi'l-ardi ve lâ fi's-semâ, gloss:yerde de gökte de hiçbir şey Allah'a gizli kalmaz, source:3:5}. Bu cümlenin en canlı geçtiği yer İbrahim'in duasıdır. İbrahim Rabbinden bu şehri güvenli kılmasını, kendisini ve oğullarını putlara tapmaktan uzak tutmasını ister. Soyunun bir kısmını kutsal Ev'in yanında, ekin bitmeyen bir vadiye, namazı kılsınlar diye yerleştirdiğini söyler. Sonra şöyle der: {ar:رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ, tr:rabbenâ inneke ta'lemu mâ nuhfî ve mâ nu'lin ve mâ yahfâ alallâhi min şey'in fi'l-ardi ve lâ fi's-semâ, gloss:Rabbimiz, sen gizlediğimizi de açığa vurduğumuzu da bilirsin; yerde de gökte de hiçbir şey Allah'a gizli kalmaz, source:14:38}. Buradaki fiil yedinci ayetteki "yahfâ"nın aynısıdır ve yanında "şey" durur. Sure son ayetinde, bu sözün İbrahim'in sayfalarında da bulunduğunu söyler. Kur'an'ın aktardığı İbrahim duası da aynı bilgiye yaslanır. Hesap gününün sahnesinde insanlar ortaya çıktıklarında da aynı söz söylenir: {ar:يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ, tr:yevme hum bârizûn lâ yahfâ alallâhi minhum şey', gloss:ortaya çıktıkları gün onlardan hiçbir şey Allah'a gizli kalmaz, source:40:16}.

## Unutulan nereye gider

[¶8] Ayetin ikinci yarısı bir gerekçeyle başlar: {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:çünkü O açıkta olanı da gizli kalanı da bilir, source:87:7}. "İnne" kelimesi burada "çünkü" işini görür. İstisna güvenlidir, çünkü dileyen aynı zamanda bilendir. Son fiilin biçimi önemlidir. "Yahfâ" geçişsiz bir fiildir, "gizlediğiniz şey" demez, "gizli kalan şey" der: {ar:خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته, tr:hafiye'ş-şey'u yahfâ ve ahfeytuhû ve huve fî hufyetin ve hafâin iẕâ setertah, gloss:şey gizli kaldı; ben onu gizledim; örttüğünde o gizlilik içindedir, source:"خ ف ي,B001"}. Bir şeyi kimin gizlediği, hatta biri onu gizlemiş mi gizlememiş mi, söylenmez. Unutulan da tam olarak böyle bir şeydir. Kimse onu saklamamıştır ama insanın kendisinden bile gizli kalmıştır. Altıncı ayetin "unutmayacaksın"ından sonra gelen bu "gizli kalan", unutmanın varabileceği yeri gösterir. Bir şey insanın hafızasından kaybolabilir, ama onu bilen birinin bilgisinden kaybolmaz.

[¶9] Kur'an insanın unutması ile Rabbin unutmaması arasındaki farkı açıkça söyler. Firavun Musa'ya önce Rabbinin kim olduğunu sorar, sonra {ar:فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:peki ilk nesillerin durumu ne olacak, source:20:51} der. Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb lâ yadıllu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Buradaki "ilk" kelimesi, on sekizinci ayette "ilk sayfalar" denirken geçen kelimenin aynısıdır. Son ayette sayfaları anılan Musa, Rabbini unutmayan olarak tanıtır. Başka bir yerde yalnızca Rabbinin emriyle indiklerini söyleyenler de aynı şeyi söyler: {ar:وَمَا كَانَ رَبُّكَ نَسِيًّۭا, tr:ve mâ kâne rabbuke nesiyyâ, gloss:Rabbin unutkan değildir, source:19:64}. Allah'a ve elçisine karşı gelenlerin diriliş günü ise tek bir cümlede özetlenir: {ar:أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ, tr:ahsâhullâhu ve nesûh, gloss:Allah onu tek tek saydı, onlar ise unuttular, source:58:6}. İnsanın unuttuğu şey Allah'ın saydığı şeydir.

[¶10] Kur'an'da okuma emri ile unutma hikâyesi aynı yerde art arda gelir. Peygamber'e {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:vahyi sana tamamlanmadan Kur'an'ı okumakta acele etme; "Rabbim, bilgimi artır" de, source:20:114} denir. Hemen sonraki ayet şudur: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ, tr:ve le-kad ahidnâ ilâ âdeme min kablu fe-nesiye, gloss:daha önce Âdem'e de söz vermiştik, o unuttu, source:20:115}. İnsanın soyu unutmayla başlar. Altıncı ayetteki vaat bu yüzden insanın kendinde olmayan bir şeyi verir. Yedinci ayet de bu armağanın sınırını bilgiyle çizer.

[¶11] Gizlinin isim hali "hâfiye"dir: {ar:الخافية ضد العلانية, tr:el-hâfiyetu diddu'l-alâniye, gloss:hâfiye, açıkta olanın karşıtıdır, source:"خ ف ي,B001"}. Türkçede bu kelime gizlice haber toplayan bir ajanın adına dönüşmüştür. Arapçada ise gizli kalan şeyin kendisidir. Kur'an onu insanların Rablerinin önüne çıkarıldığı gün için kullanır: {ar:يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ, tr:yevme'iẕin tu'radûne lâ tahfâ minkum hâfiye, gloss:o gün önüne çıkarılırsınız, sizden hiçbir gizli şey gizli kalmaz, source:69:18}.

## Sesin iki derecesi

[¶12] Altıncı ayet okumayla ilgili olduğu için yedinci ayetteki "cehr" önce bir sestir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savteh, gloss:sözü açıktan söyledi, yani sesini yükseltti, source:"ج ه ر,B001"}. Araplar bu kelimeyi okumak ve namaz kılmak için de kullanırdı: {ar:جهر بكلامه وصلاته وقراءته, tr:cehera bi-kelâmihî ve salâtihî ve kırâetih, gloss:sözünü, namazını ve okumasını sesli yaptı, source:"ج ه ر,B001"}. Karşıtı da açıkça söylenirdi: {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin karşıtıdır, source:"ج ه ر,B001"}. "Gizli" fiilinin kökü de sese uygulanır: {ar:أخفيت الصوت إخفاء, tr:ahfeytu's-savte ihfâen, gloss:sesimi kıstım, source:"خ ف ي,B001"}. Yedinci ayetin ikilisi, açık ile gizli, bu yüzden okuma bağlamında yüksek ses ile kısık ses olarak da duyulur. Açıkta olan, Peygamber'in yüksek sesle okuduğu ve başkalarının işittiği ayettir. Gizli kalan ise göğüste toplanan, içten okunan ve henüz dile gelmeyen sözdür. Bu ses ayrımı ayetin "açık ve gizli" anlamının yerini almaz, onu okumanın içine yerleştirir.

[¶13] Buradan sonra anılan kullanımlar, kelimenin bu ayetteki anlamının yerine geçmez, yanında duyulur. İlki dilin en küçük birimine kadar iner. Arap dil bilginleri harfleri ikiye ayırırdı ve bir kısmına bu kökten "mechûr" adını verirdi: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه حتى ينقضي الاعتماد بجرى الصوت, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve mena'a'n-nefese en yecriye meahû hattâ yenkadiye'l-i'timâdu bi-cerye's-savt, gloss:harfe mechûr denir, çünkü çıktığı yere tam dayanır ve dayanma sesin akışıyla bitene kadar nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. Bu harf, ağızda çıktığı yere sıkıca basılarak söylenir. O sırada nefes serbestçe dışarı kaçmaz, dışarı çıkan şey sestir. Öbür grupta ise nefes harfle birlikte akar. Yani "cehr" yalnızca yüksek sesle konuşmak değildir. Nefesi tutup sese dönüştürmek, sözü tam ağırlığıyla yerine oturtmaktır. Okutulan bir Kitap hakkındaki surede, Rabbin bildiği "açık", harfin bu tam basılışına kadar iner. "Gizli" ise nefesin sessizce geçişine kadar.

[¶14] Kur'an aynı ikiliyi bir başka surenin açılışında, bu sureyle şaşırtıcı ölçüde örtüşen bir dizide kurar. Peygamber'e şöyle denir: {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana sıkıntıya düşesin diye indirmedik, source:20:2}. Sonra şu gelir: {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkireten li-men yahşâ, gloss:ancak içi titreyen için bir hatırlatma olarak indirdik, source:20:3}. Bu surenin onuncu ve on birinci ayetlerindeki "içi titreyen" ve "en bedbaht" kelimeleri burada da yan yanadır. Birkaç ayet sonra, yerin ıslak toprağının altındakinin bile Ona ait olduğu söylendikten sonra şu cümle gelir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi de daha gizlisini de bilir, source:20:7}. Sır, insanın başkalarından sakladığı şeydir. Ondan "daha gizli" olan ise insanın kendinden bile gizli kalan olabilir. Bu karşılaştırma, yedinci ayetteki geçişsiz "gizli kalan" ile aynı yere varır.

[¶15] Okumanın kendisi de Kur'an'da bu iki yüzüyle anlatılır. Peygamber'e {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu çabucak almak için dilini kıpırdatma, source:75:16} denir. Sonra güvence gelir: {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'âneh, gloss:onu toplamak ve okutmak bize düşer, source:75:17}. Dışarıdan görünen, dilin kıpırdamasıdır. İçeride olan ise sözün göğüste toplanmasıdır. İkisi de "bize düşer" sözüyle Allah'ın üzerine alınır. Altıncı ayetteki "okutacağız" vaadi de aynı güvencedir. Kur'an dinleyene de iki sesi birden öğretir. Kur'an okunduğunda susup dinlenmesi emredilir {source:7:204}. Hemen ardından şu gelir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden, yalvararak ve korkarak, yüksek olmayan bir sesle an, source:7:205}. Surenin dördüncü ayette anılan namaz sahnesi de bu kökün sesli namaz ve okuma anlamıyla birinci ayetteki tesbih emrine ve on beşinci ayetteki namaza bağlanır.

## Örtünün altı, örtüden çıkan

[¶16] Gizli kalanın neye benzediğini Araplar somut nesnelerle söylerdi. Örtü bu köktendir: {ar:وكل شيء غطيت به شيئا فهو خفاء, tr:ve kullu şey'in ğattayte bihî şey'en fe-huve hafâ, gloss:bir şeyi örttüğün her şeye hafâ denir, source:"خ ف ي,B002"}. Kuşun kanadında öndeki uzun tüylerin gerisinde kalanlar da bu adı taşır: {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî, hâfiyenin çoğuludur; kanadın ön tüylerinin gerisinde kalan tüylerdir, source:"خ ف ي,B002"}. Hurma ağacında da aynı ad, gövdenin göbeğine en yakın dallara verilir: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine bitişik dallardır, source:"خ ف ي,B002"}. Bu örneklerde gizli olan karanlık ya da kötü değildir. Bir şeyin iç katıdır, göze ilk çarpanın arkasında, özüne en yakın yerde durur. "Gizli kalan" böyle duyulunca yalnızca saklanan sırları değil, insanın içinde en derinde duran şeyi de anlatır. Okutulan sözün göğüsteki yeri de böyle bir iç kattır.

[¶17] Bu kök bir de şaşırtıcı bir şey yapar. Aynı harfler gizlemenin tam tersini de söyler: {ar:وخفيت الشيء بغير ألف إذا أظهرته, tr:ve hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz söylenen hafeytu "şeyi açığa çıkardım" demektir, source:"خ ف ي,B003"}. Kökün bu anlamı karşıt anlamları birlikte taşıyan kelimeler arasında sayılır: {ar:وهو من الأضداد, tr:ve huve mine'l-addâd, gloss:bu, karşıt anlamlı kelimelerdendir, source:"خ ف ي,B003"}. Açığa çıkarmak da toprağın altından bir şey çekip almaktır: {ar:وخفيت الخرزة من تحت التراب أخفيها خفيا, tr:ve hafeytu'l-haraze min tahti't-turâbi ahfîhâ hafyen, gloss:boncuğu toprağın altından çıkardım, source:"خ ف ي,B003"}. Bunun özü örtüyü kaldırmaktır: {ar:وخفيته أزلت خفاه وذلك إذا أظهرته, tr:ve hafeytuhû ezeltu hafâhu ve ẕâlike iẕâ azhartah, gloss:onun örtüsünü kaldırdım, yani onu açığa çıkardım, source:"خ ف ي,B003"}. Ayetteki biçim bu değildir. "Yahfâ" gizli kalmaktır, açığa çıkarmanın şimdiki zamanı başka türlü çekilir. Ama aynı kökün öbür yüzü kulağa ulaşır. Bu dilde gizli kalan şey, onu açığa çıkarmaktan yalnızca bir hareket uzaktadır. Unutulan şey de böyledir, bilen dilediğinde onu yeniden toprağın üstüne çıkarır. Surenin otlak sahnesinde bu öbür yüz yağmurla görünür: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}. Bu cümlede açıklama dördüncü ayetteki "çıkardı" fiiliyle yapılır.

[¶18] Kur'an çıkarmak ile gizliyi bilmeyi tek bir ağızda birleştirir. Süleyman kuşları yoklar, hüdhüdü göremez. Hüdhüd uzak durmadan gelir, Sebe'den kesin bir haber getirdiğini söyler. Orada bir kadının hükmettiğini, kavminin Allah'ı bırakıp güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini anlatır. Sonra şöyle der: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran, gizlediğinizi ve açığa vurduğunuzu bilen Allah'a secde etmesinler diye, source:27:25}. Buradaki "saklı olan" (hab') başka bir köktendir. Ama sahne aynıdır: gizliyi bilen, onu çıkaran da olur.

## Gün ışığında, kamaşan gözde ve bulutun kenarında

[¶19] "Cehr" sesten sonra göze geçer: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmış olur, source:"ج ه ر,B002"}. Biri herkesin gözü önünde durduğunda bu kökle konuşulurdu: {ar:اجتهر القوم فلانا أي نظروا إليه عيانا جهارا, tr:ictehera'l-kavmu fulânen ey nazarû ileyhi iyânen cihâran, gloss:topluluk falancaya açıkça, gözleriyle baktı, source:"ج ه ر,B002"}. Topluluğun kendisine de bu ad verilirdi: {ar:كيف جهراؤكم أي عند جماعتكم, tr:keyfe cehrâukum ey inde cemâatikum, gloss:cehrânız nasıl, yani topluluğunuzun yanında durum nasıl, source:"ج ه ر,B006"}. Açık olan, kalabalığın önünde olandır. Sabah da bu köktendir: {ar:أتيناهم صباحا والصباح جهر, tr:eteynâhum sabâhan ve's-sabâhu cehr, gloss:onlara sabahleyin vardık; sabah açıklıktır, source:"ج ه ر,B005"}. Aynı fiil bir kabileye şafakta baskın yapmayı da anlatır: {ar:جهرنا بني فلان أي صبحناهم على غرة, tr:cehernâ benî fulân ey sabbahnâhum alâ ğırre, gloss:falan oğullarına sabahleyin, onlar habersizken vardık, source:"ج ه ر,B005"}. Gün ağarınca gece saklanabilen her şey ortaya çıkar.

[¶20] Ama bu açıklığın insan gözü için bir sınırı vardır. Güneşte göremeyen göz de bu kökle anılır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâu elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz, güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Güneş insanın gözünü de böyle alır: {ar:جهرته الشمس إذا أسدرت بصره, tr:cehrethu'ş-şemsu iẕâ esderet basarah, gloss:güneş gözünü kamaştırıp başını döndürdü, source:"ج ه ر,B004"}. Açıklık, göze büyük görünenle de yanıltabilir: {ar:جهرت الجيش واجتهرتهم إذا كثروا في عينك, tr:cehertu'l-ceyşe ve'ctehertuhum iẕâ keŝurû fî aynik, gloss:ordu gözüne kalabalık göründüğünde cehertu denir, source:"ج ه ر,B003"}. Gizlinin ucunda ise neredeyse görünmeyen bir ışık vardır: {ar:خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا, tr:hafe'l-berku yahfû hufven ve hufuvven iẕâ leme'a lemeânen hafiyyen, gloss:şimşek belli belirsiz parladığında hafâ denir, source:"خ ف ي,B004"}. Bulutun kenarında bir an çakıp sönen bu ışık, gizli kalanın tamamen karanlık olmadığını, ama gözün onu ancak yakalayabildiğini gösterir. İnsanın görüşü iki uç arasında kalır: bir yanda gözü kamaştıran güneş, öbür yanda bulutun kenarında zayıfça çakan şimşek vardır. Yedinci ayet bu iki ucu bir arada ve eşit biçimde bilen birinden söz eder. Surenin yağmur sahnesinde bu zayıf şimşek, dördüncü ayetteki "çıkardı" fiilinin kökünün bulutun ilk belirişine verdiği adla ve on yedinci ayetteki "daha kalıcı" kelimesinin kökünün şimşeği gece boyu gözleyen adama verdiği adla yan yana durur.

[¶21] Kur'an insanın "açıkça" görme isteğinin nereye vardığını anlatır. Musa'nın kavmi ona şöyle der: {ar:لَن نُّؤْمِنَ لَكَ حَتَّىٰ نَرَى ٱللَّهَ جَهْرَةًۭ فَأَخَذَتْكُمُ ٱلصَّٰعِقَةُ وَأَنتُمْ تَنظُرُونَ, tr:len nu'mine leke hattâ nerallâhe cehraten fe-ehaẕetkumu's-sâikatu ve entum tenzurûn, gloss:Allah'ı açıkça görmedikçe sana inanmayacağız, dediniz; siz bakıp dururken yıldırım sizi yakaladı, source:2:55}. Görmek istedikleri açıklık onlara bir yıldırım olarak geldi. Güneşte göremeyen gözü anlatan kelime bu sahneyi anlamanın bir yolunu verir. Bu, dilin değil okumanın kurduğu bir bağdır. Kur'an açık ile gizliyi gece ile gündüze de bağlar. Allah'ın her dişinin karnında taşıdığını ve rahimlerin neyi eksiltip neyi artırdığını bildiği, katında her şeyin bir ölçüyle durduğu söylenir. Ardından O {ar:عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْكَبِيرُ ٱلْمُتَعَالِ, tr:âlimu'l-ğaybi ve'ş-şehâdeti'l-kebîru'l-muteâl, gloss:görünmeyeni ve görüneni bilen, büyük, yüceler yücesi, source:13:9} diye anılır. Sonra şu gelir: {ar:سَوَآءٌۭ مِّنكُم مَّنْ أَسَرَّ ٱلْقَوْلَ وَمَن جَهَرَ بِهِۦ وَمَنْ هُوَ مُسْتَخْفٍۭ بِٱلَّيْلِ وَسَارِبٌۢ بِٱلنَّهَارِ, tr:sevâun minkum men eserra'l-kavle ve men cehera bihî ve men huve mustahfin bi'l-leyli ve sâribun bi'n-nehâr, gloss:sizden sözü gizleyenle açıktan söyleyen, gece saklananla gündüz ortada dolaşan Onun için birdir, source:13:10}. Sabahın açıklık sayıldığı dilde gizlenmek geceye, açıkta yürümek gündüze düşer. Ama bilen için ikisi birdir. Bu dizide birinci ayetteki "en yüce"nin kökü ve üçüncü ayetteki "ölçtü"nün kökü de geçer.

## Bir kuyu: hem gizli hem açılan

[¶22] Ayetin üç kelimesinin kökü de bir kuyunun adını verir. "Gizli" kökünden kuyuya {ar:والخفية الركية, tr:ve'l-hafiyyetu'r-rakiyye, gloss:hafiyye kuyudur, source:"خ ف ي,B002"} derlerdi. Aynı kuyu "açık" kökünün fiiliyle temizlenirdi: {ar:جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو, tr:cehertu'r-rakiyye iẕâ kâne mâuhâ kad ğattâhu't-tînu fe-nakkâ ẕâlike hattâ yezhera'l-mâu ve yasfû, gloss:suyunu çamur örtmüş kuyuyu, su görünüp duruluncaya kadar temizlediğimde cehertu derim, source:"ج ه ر,B008"}. İşin nasıl yapıldığı da anlatılır: {ar:جهرت البئر واجتهرتها أي نقيتها وأخرجت ما فيها من الحمأة, tr:cehertu'l-bi're ve'ctehertuhâ ey nakkaytuhâ ve ahractu mâ fîhâ mine'l-hame', gloss:kuyuyu temizledim, içindeki kara balçığı çıkardım, source:"ج ه ر,B008"}. Kuyunun dibinde su vardır ama üstüne çamur çökmüştür. Kuyuyu temizleyen kişi bu balçığı dışarı çeker, ta ki su yeniden görünüp berraklaşana kadar. Burada da açıklama dördüncü ayetin "çıkarmak" fiiliyle yapılır. "Bilir" fiilinin kökü ise bitmeyen suyu adlandırır: {ar:العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء, tr:el-aylemu yukâlu innehu'l-bahr ve yukâlu innehu'l-bi'ru'l-keŝîratu'l-mâ, gloss:aylem için deniz de denir, suyu bol kuyu da, source:"ع ل م,B005"}.

[¶23] Bunlar üç kökün ayrı kullanımlarıdır. Bir araya getirildiklerinde ortaya çıkan sahne ise okumanın kendi bulduğu bir şeydir. Okutulan söz göğüste bir kuyunun suyu gibi durur. Çamur çöktüğünde su görünmez olur, ama yok olmaz. Temizlenince yeniden yüzeye çıkar. Açık olan, balçığı alınmış ve yüzü görünen sudur. Gizli kalan, kuyunun kendisi ve çamurun altındaki sudur. Bu iki halin ikisini de bilen ise suyu tükenmeyen denizin adını taşıyan köktendir. Unutmak çamurun suyu örtmesine benzer. Hatırlamak da balçığın alınmasına. Aynı kök süt tulumu için de kullanılır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuh, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Çalkalanan tulumdan çıkan süte de bu ad verilir: {ar:الجهير اللبن الذي أخرج زبده, tr:el-cehîru'l-lebenu'lleẕî uhrice zubduh, gloss:cehîr, yağı çıkarılmış süttür, source:"ج ه ر,B010"}. Sütün içinde dağınık duran yağ, çalkalanınca toplanıp ortaya çıkar. Kuyu sahnesi surenin sel ve su sahnesine, ikinci ayetteki "yarattı" fiilinin kökünün kayadaki su oyuklarına verdiği adla ve beşinci ayetteki kelimenin kökünün selin doldurduğu çukurlara verdiği adla katılır. Tulum da surenin deri sahnesine, ikinci ayetteki fiilin deriyi kesmeden önce ölçmeye verdiği adla girer.

## Bilmek: iz, dağ ve âlem

[¶24] Ayetin "bilir" fiili ilk anlamıyla bilmemenin karşıtıdır: {ar:العلم نقيض الجهل, tr:el-ilmu nakîdu'l-cehl, gloss:bilgi, bilgisizliğin karşıtıdır, source:"ع ل م,B001"}. Bilmek bir şeyi gerçeğiyle kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi-hakîkatih, gloss:bir şeyi gerçeğiyle kavramak, source:"ع ل م,B001"}. Bu tanımda da "şey" kelimesi vardır. Türkçede "ilim" okullarda ve kitaplarda biriktirilen bilgiye dönüşmüştür. Arapçadaki fiil ise bir şeyin farkına varmayı da kapsar: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim, yani farkına varmadım, source:"ع ل م,B001"}. Yedinci ayette Rabbin bilgisi işte bu farkındalıktır. Yüksek sesle söylenen de, kimsenin farkına varmadan göğüste kalan da Onun gözünden kaçmaz.

[¶25] Bu kökün bir kolu işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu alâ eserin bi'ş-şey'i yetemeyyezu bihî an ğayrih, gloss:bir şeyi ötekilerden ayıran bir izi anlatan tek bir asıl, source:"ع ل م,B002"}. Yolcu yolunu böyle işaretlerle bulurdu: {ar:المعلم الأثر يستدل به على الطريق, tr:el-ma'lemu'l-eseru yustedellu bihî ale't-tarîk, gloss:ma'lem, yolu bulmak için izlenen izdir, source:"ع ل م,B002"}. Uzaktan görünen yüksek dağ da bu adı taşırdı: {ar:العلم الجبل الطويل والجميع الأعلام, tr:el-alemu'l-cebelu't-tavîlu ve'l-cemîu'l-a'lâm, gloss:alem yüksek dağdır, çoğulu a'lâmdır, source:"ع ل م,B002"}. Kumaşın kenarına işlenen desen de öyle: {ar:علم الثوب ورقمه في أطرافه, tr:alemu'ŝ-ŝevbi ve rakmuhû fî etrâfih, gloss:kumaşın alemi, kenarlarına işlenen desenidir, source:"ع ل م,B002"}. İnsan bir şeyi, onu ötekilerden ayıran bir izle tanır: dağla, yol işaretiyle, kumaş kenarındaki desenle. Açık olanın böyle işaretleri vardır. Gizli kalanın ise yoktur, görünmediği için gizlidir. Yedinci ayet, bilgisi işarete muhtaç olmayan birinden söz eder. Bir izle tanınan ile hiçbir iz bırakmayan, Onun bilgisinde aynı yerde durur. Bu bağı kelime değil okuma kurar. Aynı iz anlamı surenin damga sahnesinde, birinci ayetteki "ad" kelimesinin bağlandığı damga köküyle ve on altıncı ayetteki "tercih edersiniz" fiilinin iz anlamıyla buluşur.

[¶26] Bütün yaratılmışlara verilen ad da bu köktendir. Fâtiha'daki "âlemler" kelimesi bu ailedendir: {ar:العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به, tr:el-âlemu ismun li'l-feleki ve mâ yahvîh ve huve fi'l-asli ismun li-mâ yu'lemu bih, gloss:âlem, gök kubbe ile onun kapsadığı her şeyin adıdır; aslında bir şeyin onunla bilindiği şeyin adıdır, source:"ع ل م,B003"}. Namaz kılan kişi her gün "âlemlerin Rabbi" derken, bilgi kökünden bir kelimeyle bütün varlığı anar.

[¶27] Bilmek ile okumak Kur'an'ın başka bir surede ilk emri olarak da yan yana gelir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Birkaç ayet sonra Rab şöyle anılır: {ar:ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ, tr:elleẕî alleme bi'l-kalem, gloss:kalemle öğreten, source:96:4}. Ardından şu gelir: {ar:عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ, tr:alleme'l-insâne mâ lem ya'lem, gloss:insana bilmediğini öğretti, source:96:5}. "Rabbinin adı", "yarattı" ve "okumak" bu surenin birinci, ikinci ve altıncı ayetlerinde de vardır. Orada okuma öğretmeye bağlanır, burada bilmeye. İnsana bilmediğini öğreten, öğrettiğinin hangisinin kalıp hangisinin unutulacağını da bilir. Altıncı ayetteki "okutacağız" vaadi, yedinci ayetteki "bilir" fiiline bu yüzden yaslanır. Hemen ardından gelen söz de bir kolaylık vaadidir.

===== _commentary/v16/out/87_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: final long vowel in tansā marks a statement, not a prohibition
- memory: the grammarians' counterpart to majhūr letters lets the breath flow with the letter
- not written: ش ي ء B003 driving someone to a matter - no bearing on will or forgetting here
- not written: ش ي ء B006 "listened attentively" - tempting link to recitation but too thin to carry a theme
- not written: ش ي ء B004/B005/B007/B008/B009 ugliness, longing, far-sighted horse, palm shoots, interjection - none joins a theme
- not written: و ل ه alternative for Allah - only a documented alternative; bewilderment adds nothing grounded here
- not written: ع ل م B004 split lip, B006 falcon, B007 hyena - no work in the ayah's themes
- not written: ج ه ر B007 broad hill, B009 crossing unknown land - no theme support
- not written: 17:110 tukhāfit - different root (خ ف ت), would blur root identity
- not written: 14:35 wa-jnubnī echoes 87:11 - belongs to another ayah's word

===== passages not cited (221) =====
## strong (this ayah's own list) (27)

- (2:33) [listed for 87:7] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
- (3:29) [listed for 87:7] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (5:99) [listed for 87:7] مَّا عَلَى ٱلرَّسُولِ إِلَّا ٱلْبَلَٰغُ ۗ وَٱللَّهُ يَعْلَمُ مَا تُبْدُونَ وَمَا تَكْتُمُونَ
- (5:116) [listed for 87:7] وَإِذْ قَالَ ٱللَّهُ يَٰعِيسَى ٱبْنَ مَرْيَمَ ءَأَنتَ قُلْتَ لِلنَّاسِ ٱتَّخِذُونِى وَأُمِّىَ إِلَٰهَيْنِ مِن دُونِ ٱللَّهِ ۖ قَالَ سُبْحَٰنَكَ مَا يَكُونُ لِىٓ أَنْ أَقُولَ مَا لَيْسَ لِى بِحَقٍّ ۚ إِن كُنتُ قُلْتُهُۥ فَقَدْ عَلِمْتَهُۥ ۚ تَعْلَمُ مَا فِى نَفْسِى وَلَآ أَعْلَمُ مَا فِى نَفْسِكَ ۚ إِنَّكَ أَنتَ عَلَّٰمُ ٱلْغُيُوبِ
- (6:3) [listed for 87:7] وَهُوَ ٱللَّهُ فِى ٱلسَّمَٰوَٰتِ وَفِى ٱلْأَرْضِ ۖ يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ وَيَعْلَمُ مَا تَكْسِبُونَ
- (6:73) [listed for 87:7] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (9:78) [listed for 87:7] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ سِرَّهُمْ وَنَجْوَىٰهُمْ وَأَنَّ ٱللَّهَ عَلَّٰمُ ٱلْغُيُوبِ
- (11:5) [listed for 87:7] أَلَآ إِنَّهُمْ يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ ۚ أَلَا حِينَ يَسْتَغْشُونَ ثِيَابَهُمْ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (13:10) [listed for 87:7] [cited in ¶21] سَوَآءٌۭ مِّنكُم مَّنْ أَسَرَّ ٱلْقَوْلَ وَمَن جَهَرَ بِهِۦ وَمَنْ هُوَ مُسْتَخْفٍۭ بِٱلَّيْلِ وَسَارِبٌۢ بِٱلنَّهَارِ
- (14:38) [listed for 87:7] [cited in ¶7] رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (16:19) [listed for 87:7] وَٱللَّهُ يَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ
- (16:23) [listed for 87:7] لَا جَرَمَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْتَكْبِرِينَ
- (20:7) [listed for 87:7] [cited in ¶14] وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى
- (21:4) [listed for 87:7] قَالَ رَبِّى يَعْلَمُ ٱلْقَوْلَ فِى ٱلسَّمَآءِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (21:110) [listed for 87:7] إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ
- (23:92) [listed for 87:7] عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (24:29) [listed for 87:7] لَّيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَدْخُلُوا۟ بُيُوتًا غَيْرَ مَسْكُونَةٍۢ فِيهَا مَتَٰعٌۭ لَّكُمْ ۚ وَٱللَّهُ يَعْلَمُ مَا تُبْدُونَ وَمَا تَكْتُمُونَ
- (27:74) [listed for 87:7] وَإِنَّ رَبَّكَ لَيَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
- (28:69) [listed for 87:7] وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
- (32:6) [listed for 87:7] ذَٰلِكَ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (33:54) [listed for 87:7] إِن تُبْدُوا۟ شَيْـًٔا أَوْ تُخْفُوهُ فَإِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (40:19) [listed for 87:7] يَعْلَمُ خَآئِنَةَ ٱلْأَعْيُنِ وَمَا تُخْفِى ٱلصُّدُورُ
- (50:16) [listed for 87:7] وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ
- (59:22) [listed for 87:7] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (60:1) [listed for 87:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ عَدُوِّى وَعَدُوَّكُمْ أَوْلِيَآءَ تُلْقُونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَقَدْ كَفَرُوا۟ بِمَا جَآءَكُم مِّنَ ٱلْحَقِّ يُخْرِجُونَ ٱلرَّسُولَ وَإِيَّاكُمْ ۙ أَن تُؤْمِنُوا۟ بِٱللَّهِ رَبِّكُمْ إِن كُنتُمْ خَرَجْتُمْ جِهَٰدًۭا فِى سَبِيلِى وَٱبْتِغَآءَ مَرْضَاتِى ۚ تُسِرُّونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَأَنَا۠ أَعْلَمُ بِمَآ أَخْفَيْتُمْ وَمَآ أَعْلَنتُمْ ۚ وَمَن يَفْعَلْهُ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (62:8) [listed for 87:7] قُلْ إِنَّ ٱلْمَوْتَ ٱلَّذِى تَفِرُّونَ مِنْهُ فَإِنَّهُۥ مُلَٰقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (67:13) [listed for 87:7] وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ

## medium (this ayah's own list) (54)

- (2:77) [listed for 87:7] أَوَلَا يَعْلَمُونَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
- (2:235) [listed for 87:7] وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا عَرَّضْتُم بِهِۦ مِنْ خِطْبَةِ ٱلنِّسَآءِ أَوْ أَكْنَنتُمْ فِىٓ أَنفُسِكُمْ ۚ عَلِمَ ٱللَّهُ أَنَّكُمْ سَتَذْكُرُونَهُنَّ وَلَٰكِن لَّا تُوَاعِدُوهُنَّ سِرًّا إِلَّآ أَن تَقُولُوا۟ قَوْلًۭا مَّعْرُوفًۭا ۚ وَلَا تَعْزِمُوا۟ عُقْدَةَ ٱلنِّكَاحِ حَتَّىٰ يَبْلُغَ ٱلْكِتَٰبُ أَجَلَهُۥ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِىٓ أَنفُسِكُمْ فَٱحْذَرُوهُ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
- (2:255) [listed for 87:7] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (2:284) [listed for 87:7] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (3:5) [listed for 87:7] [cited in ¶7] إِنَّ ٱللَّهَ لَا يَخْفَىٰ عَلَيْهِ شَىْءٌۭ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (4:108) [listed for 87:7] يَسْتَخْفُونَ مِنَ ٱلنَّاسِ وَلَا يَسْتَخْفُونَ مِنَ ٱللَّهِ وَهُوَ مَعَهُمْ إِذْ يُبَيِّتُونَ مَا لَا يَرْضَىٰ مِنَ ٱلْقَوْلِ ۚ وَكَانَ ٱللَّهُ بِمَا يَعْمَلُونَ مُحِيطًا
- (4:148) [listed for 87:7] ۞ لَّا يُحِبُّ ٱللَّهُ ٱلْجَهْرَ بِٱلسُّوٓءِ مِنَ ٱلْقَوْلِ إِلَّا مَن ظُلِمَ ۚ وَكَانَ ٱللَّهُ سَمِيعًا عَلِيمًا
- (4:149) [listed for 87:7] إِن تُبْدُوا۟ خَيْرًا أَوْ تُخْفُوهُ أَوْ تَعْفُوا۟ عَن سُوٓءٍۢ فَإِنَّ ٱللَّهَ كَانَ عَفُوًّۭا قَدِيرًا
- (5:48) [listed for 87:7] وَأَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلْكِتَٰبِ وَمُهَيْمِنًا عَلَيْهِ ۖ فَٱحْكُم بَيْنَهُم بِمَآ أَنزَلَ ٱللَّهُ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ عَمَّا جَآءَكَ مِنَ ٱلْحَقِّ ۚ لِكُلٍّۢ جَعَلْنَا مِنكُمْ شِرْعَةًۭ وَمِنْهَاجًۭا ۚ وَلَوْ شَآءَ ٱللَّهُ لَجَعَلَكُمْ أُمَّةًۭ وَٰحِدَةًۭ وَلَٰكِن لِّيَبْلُوَكُمْ فِى مَآ ءَاتَىٰكُمْ ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ إِلَى ٱللَّهِ مَرْجِعُكُمْ جَمِيعًۭا فَيُنَبِّئُكُم بِمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
- (6:28) [listed for 87:7] بَلْ بَدَا لَهُم مَّا كَانُوا۟ يُخْفُونَ مِن قَبْلُ ۖ وَلَوْ رُدُّوا۟ لَعَادُوا۟ لِمَا نُهُوا۟ عَنْهُ وَإِنَّهُمْ لَكَٰذِبُونَ
- (6:107) [listed for 87:7] وَلَوْ شَآءَ ٱللَّهُ مَآ أَشْرَكُوا۟ ۗ وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ
- (6:128) [listed for 87:7] [cited in ¶5] وَيَوْمَ يَحْشُرُهُمْ جَمِيعًۭا يَٰمَعْشَرَ ٱلْجِنِّ قَدِ ٱسْتَكْثَرْتُم مِّنَ ٱلْإِنسِ ۖ وَقَالَ أَوْلِيَآؤُهُم مِّنَ ٱلْإِنسِ رَبَّنَا ٱسْتَمْتَعَ بَعْضُنَا بِبَعْضٍۢ وَبَلَغْنَآ أَجَلَنَا ٱلَّذِىٓ أَجَّلْتَ لَنَا ۚ قَالَ ٱلنَّارُ مَثْوَىٰكُمْ خَٰلِدِينَ فِيهَآ إِلَّا مَا شَآءَ ٱللَّهُ ۗ إِنَّ رَبَّكَ حَكِيمٌ عَلِيمٌۭ
- (7:188) [listed for 87:7] قُل لَّآ أَمْلِكُ لِنَفْسِى نَفْعًۭا وَلَا ضَرًّا إِلَّا مَا شَآءَ ٱللَّهُ ۚ وَلَوْ كُنتُ أَعْلَمُ ٱلْغَيْبَ لَٱسْتَكْثَرْتُ مِنَ ٱلْخَيْرِ وَمَا مَسَّنِىَ ٱلسُّوٓءُ ۚ إِنْ أَنَا۠ إِلَّا نَذِيرٌۭ وَبَشِيرٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:205) [listed for 87:7] [cited in ¶15] وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ بِٱلْغُدُوِّ وَٱلْءَاصَالِ وَلَا تَكُن مِّنَ ٱلْغَٰفِلِينَ
- (10:49) [listed for 87:7] قُل لَّآ أَمْلِكُ لِنَفْسِى ضَرًّۭا وَلَا نَفْعًا إِلَّا مَا شَآءَ ٱللَّهُ ۗ لِكُلِّ أُمَّةٍ أَجَلٌ ۚ إِذَا جَآءَ أَجَلُهُمْ فَلَا يَسْتَـْٔخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
- (10:61) [listed for 87:7] وَمَا تَكُونُ فِى شَأْنٍۢ وَمَا تَتْلُوا۟ مِنْهُ مِن قُرْءَانٍۢ وَلَا تَعْمَلُونَ مِنْ عَمَلٍ إِلَّا كُنَّا عَلَيْكُمْ شُهُودًا إِذْ تُفِيضُونَ فِيهِ ۚ وَمَا يَعْزُبُ عَن رَّبِّكَ مِن مِّثْقَالِ ذَرَّةٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ وَلَآ أَصْغَرَ مِن ذَٰلِكَ وَلَآ أَكْبَرَ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍ
- (11:107) [listed for 87:7] خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۚ إِنَّ رَبَّكَ فَعَّالٌۭ لِّمَا يُرِيدُ
- (13:8) [listed for 87:7] ٱللَّهُ يَعْلَمُ مَا تَحْمِلُ كُلُّ أُنثَىٰ وَمَا تَغِيضُ ٱلْأَرْحَامُ وَمَا تَزْدَادُ ۖ وَكُلُّ شَىْءٍ عِندَهُۥ بِمِقْدَارٍ
- (13:9) [listed for 87:7] [cited in ¶21] عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْكَبِيرُ ٱلْمُتَعَالِ
- (17:25) [listed for 87:7] رَّبُّكُمْ أَعْلَمُ بِمَا فِى نُفُوسِكُمْ ۚ إِن تَكُونُوا۟ صَٰلِحِينَ فَإِنَّهُۥ كَانَ لِلْأَوَّٰبِينَ غَفُورًۭا
- (18:39) [listed for 87:7] وَلَوْلَآ إِذْ دَخَلْتَ جَنَّتَكَ قُلْتَ مَا شَآءَ ٱللَّهُ لَا قُوَّةَ إِلَّا بِٱللَّهِ ۚ إِن تَرَنِ أَنَا۠ أَقَلَّ مِنكَ مَالًۭا وَوَلَدًۭا
- (19:3) [listed for 87:7] إِذْ نَادَىٰ رَبَّهُۥ نِدَآءً خَفِيًّۭا
- (20:110) [listed for 87:7] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِهِۦ عِلْمًۭا
- (25:6) [listed for 87:7] قُلْ أَنزَلَهُ ٱلَّذِى يَعْلَمُ ٱلسِّرَّ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ كَانَ غَفُورًۭا رَّحِيمًۭا
- (27:25) [listed for 87:7] [cited in ¶18] أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ
- (27:65) [listed for 87:7] قُل لَّا يَعْلَمُ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ٱلْغَيْبَ إِلَّا ٱللَّهُ ۚ وَمَا يَشْعُرُونَ أَيَّانَ يُبْعَثُونَ
- (29:10) [listed for 87:7] وَمِنَ ٱلنَّاسِ مَن يَقُولُ ءَامَنَّا بِٱللَّهِ فَإِذَآ أُوذِىَ فِى ٱللَّهِ جَعَلَ فِتْنَةَ ٱلنَّاسِ كَعَذَابِ ٱللَّهِ وَلَئِن جَآءَ نَصْرٌۭ مِّن رَّبِّكَ لَيَقُولُنَّ إِنَّا كُنَّا مَعَكُمْ ۚ أَوَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِمَا فِى صُدُورِ ٱلْعَٰلَمِينَ
- (31:23) [listed for 87:7] وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (32:17) [listed for 87:7] فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (34:3) [listed for 87:7] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَأْتِينَا ٱلسَّاعَةُ ۖ قُلْ بَلَىٰ وَرَبِّى لَتَأْتِيَنَّكُمْ عَٰلِمِ ٱلْغَيْبِ ۖ لَا يَعْزُبُ عَنْهُ مِثْقَالُ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ وَلَآ أَصْغَرُ مِن ذَٰلِكَ وَلَآ أَكْبَرُ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
- (35:38) [listed for 87:7] إِنَّ ٱللَّهَ عَٰلِمُ غَيْبِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (36:76) [listed for 87:7] فَلَا يَحْزُنكَ قَوْلُهُمْ ۘ إِنَّا نَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
- (39:46) [listed for 87:7] قُلِ ٱللَّهُمَّ فَاطِرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ عَٰلِمَ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ أَنتَ تَحْكُمُ بَيْنَ عِبَادِكَ فِى مَا كَانُوا۟ فِيهِ يَخْتَلِفُونَ
- (40:16) [listed for 87:7] [cited in ¶7] يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ ۚ لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
- (41:40) [listed for 87:7] إِنَّ ٱلَّذِينَ يُلْحِدُونَ فِىٓ ءَايَٰتِنَا لَا يَخْفَوْنَ عَلَيْنَآ ۗ أَفَمَن يُلْقَىٰ فِى ٱلنَّارِ خَيْرٌ أَم مَّن يَأْتِىٓ ءَامِنًۭا يَوْمَ ٱلْقِيَٰمَةِ ۚ ٱعْمَلُوا۟ مَا شِئْتُمْ ۖ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌ
- (42:24) [listed for 87:7] أَمْ يَقُولُونَ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًۭا ۖ فَإِن يَشَإِ ٱللَّهُ يَخْتِمْ عَلَىٰ قَلْبِكَ ۗ وَيَمْحُ ٱللَّهُ ٱلْبَٰطِلَ وَيُحِقُّ ٱلْحَقَّ بِكَلِمَٰتِهِۦٓ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (42:51) [listed for 87:7] ۞ وَمَا كَانَ لِبَشَرٍ أَن يُكَلِّمَهُ ٱللَّهُ إِلَّا وَحْيًا أَوْ مِن وَرَآئِ حِجَابٍ أَوْ يُرْسِلَ رَسُولًۭا فَيُوحِىَ بِإِذْنِهِۦ مَا يَشَآءُ ۚ إِنَّهُۥ عَلِىٌّ حَكِيمٌۭ
- (43:80) [listed for 87:7] أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ
- (47:30) [listed for 87:7] وَلَوْ نَشَآءُ لَأَرَيْنَٰكَهُمْ فَلَعَرَفْتَهُم بِسِيمَٰهُمْ ۚ وَلَتَعْرِفَنَّهُمْ فِى لَحْنِ ٱلْقَوْلِ ۚ وَٱللَّهُ يَعْلَمُ أَعْمَٰلَكُمْ
- (48:18) [listed for 87:7] ۞ لَّقَدْ رَضِىَ ٱللَّهُ عَنِ ٱلْمُؤْمِنِينَ إِذْ يُبَايِعُونَكَ تَحْتَ ٱلشَّجَرَةِ فَعَلِمَ مَا فِى قُلُوبِهِمْ فَأَنزَلَ ٱلسَّكِينَةَ عَلَيْهِمْ وَأَثَٰبَهُمْ فَتْحًۭا قَرِيبًۭا
- (49:18) [listed for 87:7] إِنَّ ٱللَّهَ يَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَٱللَّهُ بَصِيرٌۢ بِمَا تَعْمَلُونَ
- (55:2) [listed for 87:7] عَلَّمَ ٱلْقُرْءَانَ
- (57:3) [listed for 87:7] هُوَ ٱلْأَوَّلُ وَٱلْءَاخِرُ وَٱلظَّٰهِرُ وَٱلْبَاطِنُ ۖ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌ
- (57:4) [listed for 87:7] هُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۖ وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (64:4) [listed for 87:7] يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ ۚ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (65:12) [listed for 87:7] ٱللَّهُ ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ وَمِنَ ٱلْأَرْضِ مِثْلَهُنَّ يَتَنَزَّلُ ٱلْأَمْرُ بَيْنَهُنَّ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ وَأَنَّ ٱللَّهَ قَدْ أَحَاطَ بِكُلِّ شَىْءٍ عِلْمًۢا
- (67:14) [listed for 87:7] أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ
- (69:18) [listed for 87:7] [cited in ¶11] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (71:8) [listed for 87:7] ثُمَّ إِنِّى دَعَوْتُهُمْ جِهَارًۭا
- (72:26) [listed for 87:7] عَٰلِمُ ٱلْغَيْبِ فَلَا يُظْهِرُ عَلَىٰ غَيْبِهِۦٓ أَحَدًا
- (72:28) [listed for 87:7] لِّيَعْلَمَ أَن قَدْ أَبْلَغُوا۟ رِسَٰلَٰتِ رَبِّهِمْ وَأَحَاطَ بِمَا لَدَيْهِمْ وَأَحْصَىٰ كُلَّ شَىْءٍ عَدَدًۢا
- (76:30) [listed for 87:7] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
- (86:9) [listed for 87:7] يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
- (96:5) [listed for 87:7] [cited in ¶27] عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ

## named by the passage's own list as strong for this ayah (10)

- (2:106) [listed for 87:7] [cited in ¶4] ۞ مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ ۗ أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (3:179) [listed for 87:7] مَّا كَانَ ٱللَّهُ لِيَذَرَ ٱلْمُؤْمِنِينَ عَلَىٰ مَآ أَنتُمْ عَلَيْهِ حَتَّىٰ يَمِيزَ ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ ۗ وَمَا كَانَ ٱللَّهُ لِيُطْلِعَكُمْ عَلَى ٱلْغَيْبِ وَلَٰكِنَّ ٱللَّهَ يَجْتَبِى مِن رُّسُلِهِۦ مَن يَشَآءُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرُسُلِهِۦ ۚ وَإِن تُؤْمِنُوا۟ وَتَتَّقُوا۟ فَلَكُمْ أَجْرٌ عَظِيمٌۭ
- (17:86) [listed for 87:7] [cited in ¶4] وَلَئِن شِئْنَا لَنَذْهَبَنَّ بِٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ ثُمَّ لَا تَجِدُ لَكَ بِهِۦ عَلَيْنَا وَكِيلًا
- (18:26) [listed for 87:7] قُلِ ٱللَّهُ أَعْلَمُ بِمَا لَبِثُوا۟ ۖ لَهُۥ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَبْصِرْ بِهِۦ وَأَسْمِعْ ۚ مَا لَهُم مِّن دُونِهِۦ مِن وَلِىٍّۢ وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا
- (18:91) [listed for 87:7] كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا
- (20:15) [listed for 87:7] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (28:51) [listed for 87:7] ۞ وَلَقَدْ وَصَّلْنَا لَهُمُ ٱلْقَوْلَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (41:42) [listed for 87:7] لَّا يَأْتِيهِ ٱلْبَٰطِلُ مِنۢ بَيْنِ يَدَيْهِ وَلَا مِنْ خَلْفِهِۦ ۖ تَنزِيلٌۭ مِّنْ حَكِيمٍ حَمِيدٍۢ
- (64:18) [listed for 87:7] عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (84:23) [listed for 87:7] وَٱللَّهُ أَعْلَمُ بِمَا يُوعُونَ

## named by the passage's own list as medium for this ayah (14)

- (2:220) [listed for 87:7] فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۗ وَيَسْـَٔلُونَكَ عَنِ ٱلْيَتَٰمَىٰ ۖ قُلْ إِصْلَاحٌۭ لَّهُمْ خَيْرٌۭ ۖ وَإِن تُخَالِطُوهُمْ فَإِخْوَٰنُكُمْ ۚ وَٱللَّهُ يَعْلَمُ ٱلْمُفْسِدَ مِنَ ٱلْمُصْلِحِ ۚ وَلَوْ شَآءَ ٱللَّهُ لَأَعْنَتَكُمْ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (2:271) [listed for 87:7] إِن تُبْدُوا۟ ٱلصَّدَقَٰتِ فَنِعِمَّا هِىَ ۖ وَإِن تُخْفُوهَا وَتُؤْتُوهَا ٱلْفُقَرَآءَ فَهُوَ خَيْرٌۭ لَّكُمْ ۚ وَيُكَفِّرُ عَنكُم مِّن سَيِّـَٔاتِكُمْ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (6:47) [listed for 87:7] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ بَغْتَةً أَوْ جَهْرَةً هَلْ يُهْلَكُ إِلَّا ٱلْقَوْمُ ٱلظَّٰلِمُونَ
- (6:59) [listed for 87:7] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
- (7:55) [listed for 87:7] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (10:15) [listed for 87:7] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَاتُنَا بَيِّنَٰتٍۢ ۙ قَالَ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا ٱئْتِ بِقُرْءَانٍ غَيْرِ هَٰذَآ أَوْ بَدِّلْهُ ۚ قُلْ مَا يَكُونُ لِىٓ أَنْ أُبَدِّلَهُۥ مِن تِلْقَآئِ نَفْسِىٓ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ ۖ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (11:108) [listed for 87:7] [cited in ¶5] ۞ وَأَمَّا ٱلَّذِينَ سُعِدُوا۟ فَفِى ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۖ عَطَآءً غَيْرَ مَجْذُوذٍۢ
- (13:39) [listed for 87:7] يَمْحُوا۟ ٱللَّهُ مَا يَشَآءُ وَيُثْبِتُ ۖ وَعِندَهُۥٓ أُمُّ ٱلْكِتَٰبِ
- (22:76) [listed for 87:7] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۗ وَإِلَى ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ
- (24:31) [listed for 87:7] وَقُل لِّلْمُؤْمِنَٰتِ يَغْضُضْنَ مِنْ أَبْصَٰرِهِنَّ وَيَحْفَظْنَ فُرُوجَهُنَّ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا مَا ظَهَرَ مِنْهَا ۖ وَلْيَضْرِبْنَ بِخُمُرِهِنَّ عَلَىٰ جُيُوبِهِنَّ ۖ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا لِبُعُولَتِهِنَّ أَوْ ءَابَآئِهِنَّ أَوْ ءَابَآءِ بُعُولَتِهِنَّ أَوْ أَبْنَآئِهِنَّ أَوْ أَبْنَآءِ بُعُولَتِهِنَّ أَوْ إِخْوَٰنِهِنَّ أَوْ بَنِىٓ إِخْوَٰنِهِنَّ أَوْ بَنِىٓ أَخَوَٰتِهِنَّ أَوْ نِسَآئِهِنَّ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُنَّ أَوِ ٱلتَّٰبِعِينَ غَيْرِ أُو۟لِى ٱلْإِرْبَةِ مِنَ ٱلرِّجَالِ أَوِ ٱلطِّفْلِ ٱلَّذِينَ لَمْ يَظْهَرُوا۟ عَلَىٰ عَوْرَٰتِ ٱلنِّسَآءِ ۖ وَلَا يَضْرِبْنَ بِأَرْجُلِهِنَّ لِيُعْلَمَ مَا يُخْفِينَ مِن زِينَتِهِنَّ ۚ وَتُوبُوٓا۟ إِلَى ٱللَّهِ جَمِيعًا أَيُّهَ ٱلْمُؤْمِنُونَ لَعَلَّكُمْ تُفْلِحُونَ
- (41:41) [listed for 87:7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (53:4) [listed for 87:7] إِنْ هُوَ إِلَّا وَحْىٌۭ يُوحَىٰ
- (72:27) [listed for 87:7] إِلَّا مَنِ ٱرْتَضَىٰ مِن رَّسُولٍۢ فَإِنَّهُۥ يَسْلُكُ مِنۢ بَيْنِ يَدَيْهِ وَمِنْ خَلْفِهِۦ رَصَدًۭا
- (96:14) [listed for 87:7] أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ

## weak (this ayah's own list) (28)

- (2:55) [listed for 87:7] [cited in ¶21] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نُّؤْمِنَ لَكَ حَتَّىٰ نَرَى ٱللَّهَ جَهْرَةًۭ فَأَخَذَتْكُمُ ٱلصَّٰعِقَةُ وَأَنتُمْ تَنظُرُونَ
- (4:70) [listed for 87:7] ذَٰلِكَ ٱلْفَضْلُ مِنَ ٱللَّهِ ۚ وَكَفَىٰ بِٱللَّهِ عَلِيمًۭا
- (4:157) [listed for 87:7] وَقَوْلِهِمْ إِنَّا قَتَلْنَا ٱلْمَسِيحَ عِيسَى ٱبْنَ مَرْيَمَ رَسُولَ ٱللَّهِ وَمَا قَتَلُوهُ وَمَا صَلَبُوهُ وَلَٰكِن شُبِّهَ لَهُمْ ۚ وَإِنَّ ٱلَّذِينَ ٱخْتَلَفُوا۟ فِيهِ لَفِى شَكٍّۢ مِّنْهُ ۚ مَا لَهُم بِهِۦ مِنْ عِلْمٍ إِلَّا ٱتِّبَاعَ ٱلظَّنِّ ۚ وَمَا قَتَلُوهُ يَقِينًۢا
- (4:166) [listed for 87:7] لَّٰكِنِ ٱللَّهُ يَشْهَدُ بِمَآ أَنزَلَ إِلَيْكَ ۖ أَنزَلَهُۥ بِعِلْمِهِۦ ۖ وَٱلْمَلَٰٓئِكَةُ يَشْهَدُونَ ۚ وَكَفَىٰ بِٱللَّهِ شَهِيدًا
- (5:97) [listed for 87:7] ۞ جَعَلَ ٱللَّهُ ٱلْكَعْبَةَ ٱلْبَيْتَ ٱلْحَرَامَ قِيَٰمًۭا لِّلنَّاسِ وَٱلشَّهْرَ ٱلْحَرَامَ وَٱلْهَدْىَ وَٱلْقَلَٰٓئِدَ ۚ ذَٰلِكَ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَأَنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌ
- (10:65) [listed for 87:7] وَلَا يَحْزُنكَ قَوْلُهُمْ ۘ إِنَّ ٱلْعِزَّةَ لِلَّهِ جَمِيعًا ۚ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (12:81) [listed for 87:7] ٱرْجِعُوٓا۟ إِلَىٰٓ أَبِيكُمْ فَقُولُوا۟ يَٰٓأَبَانَآ إِنَّ ٱبْنَكَ سَرَقَ وَمَا شَهِدْنَآ إِلَّا بِمَا عَلِمْنَا وَمَا كُنَّا لِلْغَيْبِ حَٰفِظِينَ
- (21:28) [listed for 87:7] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يَشْفَعُونَ إِلَّا لِمَنِ ٱرْتَضَىٰ وَهُم مِّنْ خَشْيَتِهِۦ مُشْفِقُونَ
- (27:6) [listed for 87:7] وَإِنَّكَ لَتُلَقَّى ٱلْقُرْءَانَ مِن لَّدُنْ حَكِيمٍ عَلِيمٍ
- (34:6) [listed for 87:7] وَيَرَى ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (36:17) [listed for 87:7] وَمَا عَلَيْنَآ إِلَّا ٱلْبَلَٰغُ ٱلْمُبِينُ
- (37:41) [listed for 87:7] أُو۟لَٰٓئِكَ لَهُمْ رِزْقٌۭ مَّعْلُومٌۭ
- (37:164) [listed for 87:7] وَمَا مِنَّآ إِلَّا لَهُۥ مَقَامٌۭ مَّعْلُومٌۭ
- (44:32) [listed for 87:7] وَلَقَدِ ٱخْتَرْنَٰهُمْ عَلَىٰ عِلْمٍ عَلَى ٱلْعَٰلَمِينَ
- (47:19) [listed for 87:7] فَٱعْلَمْ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا ٱللَّهُ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَلِلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ۗ وَٱللَّهُ يَعْلَمُ مُتَقَلَّبَكُمْ وَمَثْوَىٰكُمْ
- (49:16) [listed for 87:7] قُلْ أَتُعَلِّمُونَ ٱللَّهَ بِدِينِكُمْ وَٱللَّهُ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (53:5) [listed for 87:7] عَلَّمَهُۥ شَدِيدُ ٱلْقُوَىٰ
- (53:28) [listed for 87:7] وَمَا لَهُم بِهِۦ مِنْ عِلْمٍ ۖ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ ۖ وَإِنَّ ٱلظَّنَّ لَا يُغْنِى مِنَ ٱلْحَقِّ شَيْـًۭٔا
- (53:30) [listed for 87:7] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (54:26) [listed for 87:7] سَيَعْلَمُونَ غَدًۭا مَّنِ ٱلْكَذَّابُ ٱلْأَشِرُ
- (58:7) [listed for 87:7] أَلَمْ تَرَ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ مَا يَكُونُ مِن نَّجْوَىٰ ثَلَٰثَةٍ إِلَّا هُوَ رَابِعُهُمْ وَلَا خَمْسَةٍ إِلَّا هُوَ سَادِسُهُمْ وَلَآ أَدْنَىٰ مِن ذَٰلِكَ وَلَآ أَكْثَرَ إِلَّا هُوَ مَعَهُمْ أَيْنَ مَا كَانُوا۟ ۖ ثُمَّ يُنَبِّئُهُم بِمَا عَمِلُوا۟ يَوْمَ ٱلْقِيَٰمَةِ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌ
- (68:52) [listed for 87:7] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (69:49) [listed for 87:7] وَإِنَّا لَنَعْلَمُ أَنَّ مِنكُم مُّكَذِّبِينَ
- (70:39) [listed for 87:7] كَلَّآ ۖ إِنَّا خَلَقْنَٰهُم مِّمَّا يَعْلَمُونَ
- (78:4) [listed for 87:7] كَلَّا سَيَعْلَمُونَ
- (78:5) [listed for 87:7] ثُمَّ كَلَّا سَيَعْلَمُونَ
- (80:22) [listed for 87:7] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
- (82:8) [listed for 87:7] فِىٓ أَىِّ صُورَةٍۢ مَّا شَآءَ رَكَّبَكَ

## named by the passage's own list as weak for this ayah (6)

- (4:153) [listed for 87:7] يَسْـَٔلُكَ أَهْلُ ٱلْكِتَٰبِ أَن تُنَزِّلَ عَلَيْهِمْ كِتَٰبًۭا مِّنَ ٱلسَّمَآءِ ۚ فَقَدْ سَأَلُوا۟ مُوسَىٰٓ أَكْبَرَ مِن ذَٰلِكَ فَقَالُوٓا۟ أَرِنَا ٱللَّهَ جَهْرَةًۭ فَأَخَذَتْهُمُ ٱلصَّٰعِقَةُ بِظُلْمِهِمْ ۚ ثُمَّ ٱتَّخَذُوا۟ ٱلْعِجْلَ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ فَعَفَوْنَا عَن ذَٰلِكَ ۚ وَءَاتَيْنَا مُوسَىٰ سُلْطَٰنًۭا مُّبِينًۭا
- (6:18) [listed for 87:7] وَهُوَ ٱلْقَاهِرُ فَوْقَ عِبَادِهِۦ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (22:70) [listed for 87:7] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَآءِ وَٱلْأَرْضِ ۗ إِنَّ ذَٰلِكَ فِى كِتَٰبٍ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (37:39) [listed for 87:7] وَمَا تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (39:68) [listed for 87:7] وَنُفِخَ فِى ٱلصُّورِ فَصَعِقَ مَن فِى ٱلسَّمَٰوَٰتِ وَمَن فِى ٱلْأَرْضِ إِلَّا مَن شَآءَ ٱللَّهُ ۖ ثُمَّ نُفِخَ فِيهِ أُخْرَىٰ فَإِذَا هُمْ قِيَامٌۭ يَنظُرُونَ
- (81:29) [listed for 87:7] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ

## neighbours: within two ayat of a passage the commentary cites (82)

- (1:1) [next to 1:2] بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (1:3) [next to 1:2] ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (1:4) [next to 1:2] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (2:53) [next to 2:55] وَإِذْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَٱلْفُرْقَانَ لَعَلَّكُمْ تَهْتَدُونَ
- (2:54) [next to 2:55] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ إِنَّكُمْ ظَلَمْتُمْ أَنفُسَكُم بِٱتِّخَاذِكُمُ ٱلْعِجْلَ فَتُوبُوٓا۟ إِلَىٰ بَارِئِكُمْ فَٱقْتُلُوٓا۟ أَنفُسَكُمْ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ عِندَ بَارِئِكُمْ فَتَابَ عَلَيْكُمْ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:56) [next to 2:55] ثُمَّ بَعَثْنَٰكُم مِّنۢ بَعْدِ مَوْتِكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (2:57) [next to 2:55] وَظَلَّلْنَا عَلَيْكُمُ ٱلْغَمَامَ وَأَنزَلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۖ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (2:104) [next to 2:106] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقُولُوا۟ رَٰعِنَا وَقُولُوا۟ ٱنظُرْنَا وَٱسْمَعُوا۟ ۗ وَلِلْكَٰفِرِينَ عَذَابٌ أَلِيمٌۭ
- (2:105) [next to 2:106] مَّا يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَلَا ٱلْمُشْرِكِينَ أَن يُنَزَّلَ عَلَيْكُم مِّنْ خَيْرٍۢ مِّن رَّبِّكُمْ ۗ وَٱللَّهُ يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (2:107) [next to 2:106] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
- (2:108) [next to 2:106] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (3:3) [next to 3:5] نَزَّلَ عَلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ وَأَنزَلَ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ
- (3:4) [next to 3:5] مِن قَبْلُ هُدًۭى لِّلنَّاسِ وَأَنزَلَ ٱلْفُرْقَانَ ۗ إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
- (3:6) [next to 3:5] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (3:7) [next to 3:5] هُوَ ٱلَّذِىٓ أَنزَلَ عَلَيْكَ ٱلْكِتَٰبَ مِنْهُ ءَايَٰتٌۭ مُّحْكَمَٰتٌ هُنَّ أُمُّ ٱلْكِتَٰبِ وَأُخَرُ مُتَشَٰبِهَٰتٌۭ ۖ فَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِمْ زَيْغٌۭ فَيَتَّبِعُونَ مَا تَشَٰبَهَ مِنْهُ ٱبْتِغَآءَ ٱلْفِتْنَةِ وَٱبْتِغَآءَ تَأْوِيلِهِۦ ۗ وَمَا يَعْلَمُ تَأْوِيلَهُۥٓ إِلَّا ٱللَّهُ ۗ وَٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ يَقُولُونَ ءَامَنَّا بِهِۦ كُلٌّۭ مِّنْ عِندِ رَبِّنَا ۗ وَمَا يَذَّكَّرُ إِلَّآ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (6:126) [next to 6:128] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
- (6:127) [next to 6:128] ۞ لَهُمْ دَارُ ٱلسَّلَٰمِ عِندَ رَبِّهِمْ ۖ وَهُوَ وَلِيُّهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- (6:129) [next to 6:128] وَكَذَٰلِكَ نُوَلِّى بَعْضَ ٱلظَّٰلِمِينَ بَعْضًۢا بِمَا كَانُوا۟ يَكْسِبُونَ
- (6:130) [next to 6:128] يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَقُصُّونَ عَلَيْكُمْ ءَايَٰتِى وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ شَهِدْنَا عَلَىٰٓ أَنفُسِنَا ۖ وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
- (7:202) [next to 7:204] وَإِخْوَٰنُهُمْ يَمُدُّونَهُمْ فِى ٱلْغَىِّ ثُمَّ لَا يُقْصِرُونَ
- (7:203) [next to 7:204] وَإِذَا لَمْ تَأْتِهِم بِـَٔايَةٍۢ قَالُوا۟ لَوْلَا ٱجْتَبَيْتَهَا ۚ قُلْ إِنَّمَآ أَتَّبِعُ مَا يُوحَىٰٓ إِلَىَّ مِن رَّبِّى ۚ هَٰذَا بَصَآئِرُ مِن رَّبِّكُمْ وَهُدًۭى وَرَحْمَةٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:206) [next to 7:204] إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ وَيُسَبِّحُونَهُۥ وَلَهُۥ يَسْجُدُونَ ۩
- (11:106) [next to 11:108] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (11:109) [next to 11:108] فَلَا تَكُ فِى مِرْيَةٍۢ مِّمَّا يَعْبُدُ هَٰٓؤُلَآءِ ۚ مَا يَعْبُدُونَ إِلَّا كَمَا يَعْبُدُ ءَابَآؤُهُم مِّن قَبْلُ ۚ وَإِنَّا لَمُوَفُّوهُمْ نَصِيبَهُمْ غَيْرَ مَنقُوصٍۢ
- (11:110) [next to 11:108] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَٱخْتُلِفَ فِيهِ ۚ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَقُضِىَ بَيْنَهُمْ ۚ وَإِنَّهُمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- (13:7) [next to 13:9] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
- (13:11) [next to 13:9] لَهُۥ مُعَقِّبَٰتٌۭ مِّنۢ بَيْنِ يَدَيْهِ وَمِنْ خَلْفِهِۦ يَحْفَظُونَهُۥ مِنْ أَمْرِ ٱللَّهِ ۗ إِنَّ ٱللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۗ وَإِذَآ أَرَادَ ٱللَّهُ بِقَوْمٍۢ سُوٓءًۭا فَلَا مَرَدَّ لَهُۥ ۚ وَمَا لَهُم مِّن دُونِهِۦ مِن وَالٍ
- (13:12) [next to 13:10] هُوَ ٱلَّذِى يُرِيكُمُ ٱلْبَرْقَ خَوْفًۭا وَطَمَعًۭا وَيُنشِئُ ٱلسَّحَابَ ٱلثِّقَالَ
- (14:36) [next to 14:38] رَبِّ إِنَّهُنَّ أَضْلَلْنَ كَثِيرًۭا مِّنَ ٱلنَّاسِ ۖ فَمَن تَبِعَنِى فَإِنَّهُۥ مِنِّى ۖ وَمَنْ عَصَانِى فَإِنَّكَ غَفُورٌۭ رَّحِيمٌۭ
- (14:37) [next to 14:38] رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ
- (14:39) [next to 14:38] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى وَهَبَ لِى عَلَى ٱلْكِبَرِ إِسْمَٰعِيلَ وَإِسْحَٰقَ ۚ إِنَّ رَبِّى لَسَمِيعُ ٱلدُّعَآءِ
- (14:40) [next to 14:38] رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ
- (17:84) [next to 17:86] قُلْ كُلٌّۭ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًۭا
- (17:85) [next to 17:86] وَيَسْـَٔلُونَكَ عَنِ ٱلرُّوحِ ۖ قُلِ ٱلرُّوحُ مِنْ أَمْرِ رَبِّى وَمَآ أُوتِيتُم مِّنَ ٱلْعِلْمِ إِلَّا قَلِيلًۭا
- (17:88) [next to 17:86] قُل لَّئِنِ ٱجْتَمَعَتِ ٱلْإِنسُ وَٱلْجِنُّ عَلَىٰٓ أَن يَأْتُوا۟ بِمِثْلِ هَٰذَا ٱلْقُرْءَانِ لَا يَأْتُونَ بِمِثْلِهِۦ وَلَوْ كَانَ بَعْضُهُمْ لِبَعْضٍۢ ظَهِيرًۭا
- (17:89) [next to 17:87] وَلَقَدْ صَرَّفْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍۢ فَأَبَىٰٓ أَكْثَرُ ٱلنَّاسِ إِلَّا كُفُورًۭا
- (18:20) [next to 18:22] إِنَّهُمْ إِن يَظْهَرُوا۟ عَلَيْكُمْ يَرْجُمُوكُمْ أَوْ يُعِيدُوكُمْ فِى مِلَّتِهِمْ وَلَن تُفْلِحُوٓا۟ إِذًا أَبَدًۭا
- (18:21) [next to 18:22] وَكَذَٰلِكَ أَعْثَرْنَا عَلَيْهِمْ لِيَعْلَمُوٓا۟ أَنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَأَنَّ ٱلسَّاعَةَ لَا رَيْبَ فِيهَآ إِذْ يَتَنَٰزَعُونَ بَيْنَهُمْ أَمْرَهُمْ ۖ فَقَالُوا۟ ٱبْنُوا۟ عَلَيْهِم بُنْيَٰنًۭا ۖ رَّبُّهُمْ أَعْلَمُ بِهِمْ ۚ قَالَ ٱلَّذِينَ غَلَبُوا۟ عَلَىٰٓ أَمْرِهِمْ لَنَتَّخِذَنَّ عَلَيْهِم مَّسْجِدًۭا
- (18:25) [next to 18:23] وَلَبِثُوا۟ فِى كَهْفِهِمْ ثَلَٰثَ مِا۟ئَةٍۢ سِنِينَ وَٱزْدَادُوا۟ تِسْعًۭا
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:65) [next to 19:64] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (20:0) [next to 20:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (20:1) [next to 20:2] طه
- (20:4) [next to 20:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:6) [next to 20:7] لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَمَا بَيْنَهُمَا وَمَا تَحْتَ ٱلثَّرَىٰ
- (20:8) [next to 20:7] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:9) [next to 20:7] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:49) [next to 20:51] قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ
- (20:50) [next to 20:51] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (20:53) [next to 20:51] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
- (20:54) [next to 20:52] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:112) [next to 20:114] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا يَخَافُ ظُلْمًۭا وَلَا هَضْمًۭا
- (20:113) [next to 20:114] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
- (20:116) [next to 20:114] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ
- (20:117) [next to 20:115] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (27:23) [next to 27:25] إِنِّى وَجَدتُّ ٱمْرَأَةًۭ تَمْلِكُهُمْ وَأُوتِيَتْ مِن كُلِّ شَىْءٍۢ وَلَهَا عَرْشٌ عَظِيمٌۭ
- (27:24) [next to 27:25] وَجَدتُّهَا وَقَوْمَهَا يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ فَهُمْ لَا يَهْتَدُونَ
- (27:26) [next to 27:25] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ ۩
- (27:27) [next to 27:25] ۞ قَالَ سَنَنظُرُ أَصَدَقْتَ أَمْ كُنتَ مِنَ ٱلْكَٰذِبِينَ
- (40:14) [next to 40:16] فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (40:15) [next to 40:16] رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ
- (40:17) [next to 40:16] ٱلْيَوْمَ تُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ ۚ لَا ظُلْمَ ٱلْيَوْمَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (40:18) [next to 40:16] وَأَنذِرْهُمْ يَوْمَ ٱلْءَازِفَةِ إِذِ ٱلْقُلُوبُ لَدَى ٱلْحَنَاجِرِ كَٰظِمِينَ ۚ مَا لِلظَّٰلِمِينَ مِنْ حَمِيمٍۢ وَلَا شَفِيعٍۢ يُطَاعُ
- (58:4) [next to 58:6] فَمَن لَّمْ يَجِدْ فَصِيَامُ شَهْرَيْنِ مُتَتَابِعَيْنِ مِن قَبْلِ أَن يَتَمَآسَّا ۖ فَمَن لَّمْ يَسْتَطِعْ فَإِطْعَامُ سِتِّينَ مِسْكِينًۭا ۚ ذَٰلِكَ لِتُؤْمِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ ۚ وَتِلْكَ حُدُودُ ٱللَّهِ ۗ وَلِلْكَٰفِرِينَ عَذَابٌ أَلِيمٌ
- (58:5) [next to 58:6] إِنَّ ٱلَّذِينَ يُحَآدُّونَ ٱللَّهَ وَرَسُولَهُۥ كُبِتُوا۟ كَمَا كُبِتَ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ وَقَدْ أَنزَلْنَآ ءَايَٰتٍۭ بَيِّنَٰتٍۢ ۚ وَلِلْكَٰفِرِينَ عَذَابٌۭ مُّهِينٌۭ
- (58:8) [next to 58:6] أَلَمْ تَرَ إِلَى ٱلَّذِينَ نُهُوا۟ عَنِ ٱلنَّجْوَىٰ ثُمَّ يَعُودُونَ لِمَا نُهُوا۟ عَنْهُ وَيَتَنَٰجَوْنَ بِٱلْإِثْمِ وَٱلْعُدْوَٰنِ وَمَعْصِيَتِ ٱلرَّسُولِ وَإِذَا جَآءُوكَ حَيَّوْكَ بِمَا لَمْ يُحَيِّكَ بِهِ ٱللَّهُ وَيَقُولُونَ فِىٓ أَنفُسِهِمْ لَوْلَا يُعَذِّبُنَا ٱللَّهُ بِمَا نَقُولُ ۚ حَسْبُهُمْ جَهَنَّمُ يَصْلَوْنَهَا ۖ فَبِئْسَ ٱلْمَصِيرُ
- (69:16) [next to 69:18] وَٱنشَقَّتِ ٱلسَّمَآءُ فَهِىَ يَوْمَئِذٍۢ وَاهِيَةٌۭ
- (69:17) [next to 69:18] وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا ۚ وَيَحْمِلُ عَرْشَ رَبِّكَ فَوْقَهُمْ يَوْمَئِذٍۢ ثَمَٰنِيَةٌۭ
- (69:19) [next to 69:18] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (69:20) [next to 69:18] إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ
- (75:14) [next to 75:16] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
- (75:15) [next to 75:16] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
- (75:18) [next to 75:16] فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ
- (75:19) [next to 75:17] ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ
- (96:0) [next to 96:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (96:2) [next to 96:1] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- (96:3) [next to 96:1] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- (96:6) [next to 96:4] كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- (96:7) [next to 96:5] أَن رَّءَاهُ ٱسْتَغْنَىٰٓ

