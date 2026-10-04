Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:6; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_6.reading.tr.md (prose paragraphs numbered) =====
## Anlatılan Rab konuşmaya başlıyor

[¶1] Altıncı ayet yalnızca iki fiilden oluşur: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Surenin ilk beş ayeti Rabbi dışarıdan anlatır. Yaratan, düzene koyan, ölçen, yol gösteren, otlağı çıkarıp sonra kararmış çerçöpe çeviren "O"dur. Altıncı ayette anlatılan bu Rab birden kendisi konuşmaya başlar. "Biz" der ve muhatabına "sen" diye döner. Tanıtım hitaba dönüşür. Fiilin başındaki se- eki yakın bir geleceği bildirir. Bu yüzden söz bir bilgi olarak değil, bir vaat olarak verilir. Yedinci ayet yeniden "Allah" adını anar. Sekizinci ayette ise "biz" aynı kalıpla geri gelir: {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana yatkın kılacağız, source:87:8}. İki fiilin kuruluşu aynıdır. Özne "biz"dir, nesne "sen". Eylem de muhatabın kendi başına yapacağı bir şeyi onun için mümkün kılmaktır. Okuyan sen olacaksın ama okutan biziz. Kolaylığa yürüyen sen olacaksın ama yolu kolaylaştıran biziz.

[¶2] Fiil "okumak" değil, "okutmak"tır. Araplar başkasına okuma yaptırmayı tam bu biçimle söylerdi: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu ğayrî ukriuhû ikrâen, gloss:başkasına okuttum, ona okuma yaptırıyorum, source:"ق ر ء,B002"}. Birlikte okuyup çalışmak da aynı köktendi: {ar:قارأته دارسته, tr:kâra'tuhû dârastuh, gloss:onunla karşılıklı okudum, onunla ders çalıştım, source:"ق ر ء,B002"}. Okutmada okutan önce okur, öteki onun okuyuşunu izler. Kur'an bu düzeni başka bir surede açıkça anlatır. Allah, Peygamber'e vahiy gelirken onu kaçırmamak için acele ettiğini söyler ve şöyle der: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle yakalamak için dilini kıpırdatma, source:75:16}. Ardından yükü kendi üzerine alır: {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak da okutmak da bize düşer, source:75:17}. Muhataba düşen pay ise izlemektir: {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe-iẕâ kara'nâhu fettebi' kur'ânah, gloss:onu okuduğumuzda sen onun okunuşunu izle, source:75:18}. Anlamı açmayı da yine kendi üzerine alır: {ar:ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ, tr:ŝumme inne aleynâ beyânah, gloss:sonra onu açıklamak da bize düşer, source:75:19}. Altıncı ayetin "biz okutacağız" sözü bu dört ayetin kısaltılmış bir vaadi gibidir.

[¶3] Bu noktadan sonra anılacak kelime imgeleri ayetteki "okutmak" ve "unutmak" anlamlarının yerine geçmez. Bu anlamların yanında duyulurlar. İlki izlemekle ilgilidir. Araplar bir şiirin başka bir şiirin vezninde ve tarzında söylendiğini aynı kökle anlatırdı: {ar:هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله, tr:hâẕe'ş-şi'ru alâ kar'i hâẕe'ş-şi'r ey alâ tarîkatihî ve misâlih, gloss:bu şiir şu şiirin kar'ı üzerinedir, yani onun yolunda ve örneğindedir, source:"ق ر ء,B011"}. Burada bir şey başka bir şeyin izinden giderek kurulur. Okutulan da okutanın okuyuşunu izleyerek okur. Yetmiş beşinci suredeki "izle" emri bu kullanımla aynı yönde durur. İkinci kullanım bir sözü taşımakla ilgilidir. Birinin selamını getiren için {ar:فلان قرأ عليك السلام وأقراك السلام بمعنى, tr:fulânun karae aleyke's-selâme ve akrâke's-selâme bi-ma'nâ, gloss:falanca sana selam okudu da selamını iletti de aynı anlamdadır, source:"ق ر ء,B007"} denirdi. Kimileri bu ikinci biçimi yanlış bulur, yalnızca "ona selam oku" demeyi doğru sayardı {source:"ق ر ء,B007"}. Kalıp tartışmalıdır ama gösterdiği hareket açıktır: başkasının sözü alınır ve muhatabın kulağına ulaştırılır. Ayetteki fiil de sözü kaynağından alıp muhatabın diline yerleştirir.

[¶4] Bu vaadin karşısında Kur'an'ın bir başka hitabı durur. Orada Peygamber'e emir verilir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bismi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Aynı surede bu Rab {ar:عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ, tr:alleme'l-insâne mâ lem ya'lem, gloss:insana bilmediğini öğretti, source:96:5} diye anılır. Bu surenin açılışı da aynı sözlerle kuruludur: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1} ve ardından {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}. İki surede de "Rabbinin adı" ve "yaratan" sözleri bir arada geçer. Biri "oku" diye emreder, öbürü "sana okutacağız" diye söz verir. Emri yerine getirmeyi mümkün kılan da bu vaattir.

## Toplamak, rahimde tutmak, sonra bırakmak

[¶5] Okumak fiilinin kökü, parçaları bir araya getirmeyi anlatır. Araplar {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:kara'tu'ş-şey'e kur'ânen ceme'tuhû ve damamtu ba'dahû ilâ ba'd, gloss:o şeyi topladım, parçalarını birbirine kattım, source:"ق ر ء,B001"} derdi. Okuma da bu toplamanın sesteki biçimiydi: {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل, tr:el-kırâe dammu'l-hurûfi ve'l-kelimâti ba'dihâ ilâ ba'din fi't-tertîl, gloss:okuma, harfleri ve kelimeleri tertil içinde birbirine eklemektir, source:"ق ر ء,B001"}. Bu kullanımda okumak, sesleri tek tek çıkarmak değildir. Okumak onları birbirine bağlayıp bir bütün halinde tutmaktır. Yetmiş beşinci surenin "toplamak ve okutmak" ikilisi, bu iki işi Kur'an'ın kendi cümlesinde yan yana koyar. Tertil kelimesi de Kur'an'da geçer. Gece namazı emredilen Peygamber'e {ar:وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا, tr:ve rattili'l-kur'âne tertîlâ, gloss:Kur'an'ı dizerek, tane tane oku, source:73:4} denir. Kur'an'ın neden tek seferde indirilmediğini soran inkârcılara verilen cevap da bu dizmeyi tutmaya bağlar: {ar:كَذَٰلِكَ لِنُثَبِّتَ بِهِۦ فُؤَادَكَ ۖ وَرَتَّلْنَٰهُ تَرْتِيلًۭا, tr:keẕâlike li-nuŝebbite bihî fuâdek ve rattelnâhu tertîlâ, gloss:onunla kalbini sağlamlaştırmak için böyle yaptık ve onu dizip sıraladık, source:25:32}. Söz parça parça gelir. Kalpte sağlam durması da parçaların birbirine eklenmesiyle olur.

[¶6] Kökün bu toplama anlamı en somut biçimini develerde bulur. Hiç gebe kalmamış bir dişi deve için {ar:ما قرأت هذه الناقة سلى قط وما قرأت جنينا, tr:mâ karaet hâẕihi'n-nâkatu selen katt ve mâ karaet cenînâ, gloss:bu deve hiç yavru zarı toplamadı, hiç cenin taşımadı, source:"ق ر ء,B004"} denirdi. Bu da {ar:لم تضم رحمها على ولد, tr:lem tedumma rahimehâ alâ veled, gloss:rahmini bir yavrunun üzerine kapamadı, source:"ق ر ء,B004"} diye açıklanırdı. Selâ, yavruyu rahimde saran ve doğumdan sonra dışarı atılan zardır. Gebe kalan rahim yavrunun ve bu zarın üzerine kapanır, onları dağılmadan bir arada tutar ve vakti gelince dışarı bırakır. Aynı cümle bir başka açıdan da anlaşılırdı: {ar:ما قرأت الناقة سلى قط أي ما طرحت وتأويله ما حملت, tr:mâ karaeti'n-nâkatu selen katt ey mâ tarahat ve te'vîluhû mâ hamelet, gloss:deve hiç yavru zarı düşürmedi, yani hiç gebe kalmadı, source:"ق ر ء,B003"}. Fiil böylece iki ucu birlikte taşır: içine alıp tutmak ve vakti gelince dışarı vermek. İkisi tek bir sürecin başı ve sonudur. Tutmayan rahim veremez, veren rahim önce tutmuştur.

[¶7] Bu imge ayete okumanın bir mekanizmasını ekler. Okutulan söz önce muhatabın içinde toplanır, dağılmadan durur, sonra dışarı çıkıp başkalarına okunur. Kur'an bu süreyi kendi diliyle anlatır: {ar:وَقُرْءَانًۭا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍۢ وَنَزَّلْنَٰهُ تَنزِيلًۭا, tr:ve kur'ânen farakhâhu li-takraehû ale'n-nâsi alâ mukŝin ve nezzelnâhu tenzîlâ, gloss:onu insanlara ağır ağır okuyasın diye bölüm bölüm ayırdığımız bir Kur'an olarak indirdik ve onu aşama aşama indirdik, source:17:106}. Mukŝ bir yerde durup kalmaktır. Söz önce durur, sonra insanlara okunur. Rahim ile okuma arasındaki bu bağ bir benzerliktir, ayetin söylediği bir şey değildir. Ama altıncı ayetin vaadi bu imgeyle yan yana konunca şunu duyurur: okutulan söz muhatabın içinde, rahmin yavrunun üzerine kapanması gibi kapanıp tutulacaktır. Bu imge, ikinci ayetin yaratma ve düzene koyma fiilleriyle birlikte rahimde biçimlenen bedenin sahnesine de katılır.

[¶8] Kur'an'da bir kadın hem taşımayı hem de düşürülmeyi aynı hikâyede yaşar. Meryem için {ar:فَحَمَلَتْهُ فَٱنتَبَذَتْ بِهِۦ مَكَانًۭا قَصِيًّۭا, tr:fe-hamelethu fentebeẕet bihî mekânen kasıyyâ, gloss:ona gebe kaldı ve onunla uzak bir yere çekildi, source:19:22} denir. Doğum sancısı onu bir hurma kütüğüne götürdüğünde şöyle der: {ar:يَٰلَيْتَنِى مِتُّ قَبْلَ هَٰذَا وَكُنتُ نَسْيًۭا مَّنسِيًّۭا, tr:yâ leytenî mittu kable hâẕâ ve kuntu nesyen mensiyyâ, gloss:keşke bundan önce ölseydim de unutulup gitmiş bir hiç olsaydım, source:19:23}. Hemen altından ona seslenilir: {ar:أَلَّا تَحْزَنِى قَدْ جَعَلَ رَبُّكِ تَحْتَكِ سَرِيًّۭا, tr:ellâ tahzenî kad ceale rabbuki tahteki seriyyâ, gloss:üzülme, Rabbin senin altında bir dere akıttı, source:19:24}. Rahminde taşıyan kadın düşürülüp unutulmuş bir şey olmayı diler. Rabbi ise onu unutmaz. "Unutmak" fiilinin bu yüzünü bir sonraki bölüm açacak.

## Düşürülmeyen söz

[¶9] Ayetin ikinci yarısının dil bilgisi kesin bir şey söyler. Fe- bağlacı sonucu bildirir: okutacağız, bu yüzden unutmayacaksın. Lâ olumsuzlamasıyla gelen fiil sonundaki uzun â'yı korur. Yasak bildirilseydi fiil kısalırdı ve "unutma!" anlamına gelirdi. Ayette ise uzun ünlü yerindedir. Bu yüzden cümle bir emir değil, bir haberdir: "unutmayacaksın." Unutmamak muhataba yüklenmiş ve onun çabasına bırakılmış bir ödev olarak verilmez. Okutmanın kendiliğinden doğan sonucu olarak verilir. Hafızayı koruyan kişinin dikkati değil, okutanın okutmasıdır.

[¶10] Unutmak, bir şeyi akılda tutmayı bırakmaktır. Araplar {ar:النسيان خلاف الذكر والحفظ, tr:en-nisyânu hilâfu'ẕ-ẕikri ve'l-hıfz, gloss:unutmak, anmanın ve korumanın karşıtıdır, source:"ن س ي,B001"} derdi. Fiilin işleyişi daha ayrıntılı da tarif edilirdi: {ar:ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد, tr:terku'l-insâni dabta mâ'stûdia immâ li-da'fi kalbihî ve immâ an ğafletin ve immâ an kasd, gloss:insanın kendisine emanet edileni sıkıca tutmayı bırakmasıdır; ya kalbinin zayıflığından ya gaflettendir ya da bilerek, source:"ن س ي,B001"}. Bu tarifte hafıza bir emanettir, unutmak da emaneti tutan elin gevşemesidir. Okutmanın rahim imgesi tam bunun karşısında durur: içindekinin üzerine kapanan ve onu bırakmayan bir tutuş. Türkçede "nisyan" kelimesi yalnızca unutkanlık anlamında yaşar. Arapçada ise aynı fiil bilerek bırakmayı ve terk etmeyi de anlatır: {ar:النسيان الترك، نسوا الله فنسيهم, tr:en-nisyânu't-terk, nesullâhe fe-nesiyehum, gloss:unutmak bırakmaktır; Allah'ı bıraktılar, O da onları bıraktı, source:"ن س ي,B002"}. Kur'an bu anlamı bir yüzleşme sahnesinde verir. Allah, kendi zikrinden yüz çevirenin dar bir geçimi olacağını ve kıyamet günü kör olarak diriltileceğini söyler. O kişi neden kör diriltildiğini sorar, çünkü dünyada görüyordu {source:20:125}. Cevap şudur: {ar:كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ, tr:keẕâlike etetke âyâtunâ fe-nesîtehâ ve keẕâlike'l-yevme tunsâ, gloss:ayetlerimiz sana böyle gelmişti de sen onları bırakıp unutmuştun; bugün sen de böyle bırakılıp unutulursun, source:20:126}. "Unutmayacaksın" vaadi bu ağırlıkla birlikte duyulur. Okutulan söz yalnızca akılda kalmakla kalmayacak, bırakılıp bir kenara da atılmayacaktır.

[¶11] Unutulan şeyin kendisine de bir ad verilirdi. Araplar göç edip giden bir obanın konak yerinde kalan döküntüye {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisyu mâ sekata min menâzili'l-murtehilîne min ruẕâli emtiatihim, gloss:nisy, göçenlerin konak yerlerinden düşen değersiz eşyadır, source:"ن س ي,B003"} derlerdi. Bir başka tarif bunu genelleştirirdi: {ar:النسي ما يقل الاعتداد به وما من شأنه أن ينسى, tr:en-nisyu mâ yekıllu'l-i'tidâdu bihî ve mâ min şe'nihî en yunsâ, gloss:nisy, pek hesaba katılmayan ve unutulmaya mahkûm olan şeydir, source:"ن س ي,B003"}. Göçmen obanın kalktığını düşünelim: değerli olan her şey toplanıp hayvanlara yüklenir. Kırık kap, yırtık ip, kimsenin dönüp almadığı ufak tefek yerde kalır. Unutmak bu açıdan, yük toplanırken bir şeyin geride düşmesidir. Meryem'in dileğindeki "nesyen mensiyyâ" bu düşmüş şeydir. Okumanın ilk anlamı ise toplamak ve birbirine katmaktı. İki fiil bu imgelerle aynı hareketin iki zıt yönünü gösterir: biri toplar ve tutar, öbürü düşürür ve geride bırakır. Ayet ikisini fe- ile bağlar: toplayan Rab okutunca, okutulan söz konak yerinde kalan döküntüden olmayacaktır. Dördüncü ve beşinci ayetlerde otlağın kararmış çerçöpe dönmesi de bu düşürülen şeyle aynı kefededir. Altıncı ayetin vaadi tam o çerçöpün yanında verilir.

[¶12] Kur'an unutmanın tehlikesini okutmanın hemen bitişiğinde de gösterir. Allah Kur'an'ı Arapça bir Kur'an olarak indirdiğini ve içinde uyarıları çeşitlendirdiğini söyledikten sonra Peygamber'e şöyle der: {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:sana vahyi tamamlanmadan Kur'an'ı okumakta acele etme ve "Rabbim, bilgimi artır" de, source:20:114}. Hemen ardından gelen ayet insanlığın ilk unutuşunu anlatır: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا, tr:ve lekad ahidnâ ilâ âdeme min kablu fe-nesiye ve lem necid lehû azmâ, gloss:andolsun, daha önce Âdem'e bir söz emanet etmiştik; o unuttu ve onda bir kararlılık bulmadık, source:20:115}. Kendisine söz emanet edilen ilk insan emaneti tutamamıştır. Altıncı ayetin vaadi, okutulan sözün bu kez düşmeyeceğini söyler. Vaadin güvencesi de okutanın kendisidir. Firavun Musa'ya geçmiş nesillerin akıbetini sorduğunda Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb, lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne şaşırır ne unutur, source:20:52}. Başka bir surede, Rablerinden sakınanlara miras verilecek bahçe anlatıldıktan sonra, inenler kendi ağızlarından konuşur: {ar:وَمَا نَتَنَزَّلُ إِلَّا بِأَمْرِ رَبِّكَ ۖ لَهُۥ مَا بَيْنَ أَيْدِينَا وَمَا خَلْفَنَا وَمَا بَيْنَ ذَٰلِكَ ۚ وَمَا كَانَ رَبُّكَ نَسِيًّۭا, tr:ve mâ netenezzelu illâ bi-emri rabbik, lehû mâ beyne eydînâ ve mâ halfenâ ve mâ beyne ẕâlik, ve mâ kâne rabbuke nesiyyâ, gloss:biz ancak Rabbinin emriyle ineriz; önümüzdeki, ardımızdaki ve bunların arasındaki O'nundur; Rabbin unutkan değildir, source:19:64}. Söz unutmayan bir Rabden iner ve O okutur. Bu yüzden okutulan da unutmaz.

## İstisna, anma ve kolaylık

[¶13] Vaat istisnasız kalmaz. Yedinci ayet hemen ekler: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği hariç, source:87:7}. Bu ek vaadi zayıflatmaz. Vaadin kime ait olduğunu gösterir. Hafızayı veren onu elinde tutmaya devam eder, verilen hafıza muhatabın bağımsız bir mülkü haline gelmez. Kur'an aynı fiilin "unutturmak" biçimini de Allah'a verir. Kitap ehlinden ve müşriklerden inkâr edenlerin Rabden müminlere hiçbir hayır inmesini istemedikleri söylendikten hemen sonra şöyle denir: {ar:مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ, tr:mâ nensah min âyetin ev nunsihâ ne'ti bi-hayrin minhâ ev mislihâ, gloss:herhangi bir ayeti yürürlükten kaldırır ya da unutturursak, ondan daha iyisini ya da bir benzerini getiririz, source:2:106}. Nunsi ile nukri aynı kalıptadır: "biz unuttururuz" ve "biz okuturuz." Okutmak da unutturmak da aynı "biz"in elindedir. Unutturulan bir ayetin yerine ise ya daha iyisi ya da bir benzeri gelir. Böylece emanet hiçbir zaman eksik kalmaz. Yedinci ayetin geri kalanı bu hükmün dayanağını verir: {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa çıkanı da gizli kalanı da bilir, source:87:7}. Dilde yüksek sesle okunan da kalpte saklı duran da O'nun bilgisi içindedir.

[¶14] Aynı istisna kalıbı Peygamber'e bir başka yerde de öğretilir. Allah ona şöyle der: {ar:وَلَا تَقُولَنَّ لِشَا۟ىْءٍ إِنِّى فَاعِلٌۭ ذَٰلِكَ غَدًا, tr:ve lâ tekûlenne li-şey'in innî fâilun ẕâlike ğadâ, gloss:hiçbir şey için "bunu yarın yapacağım" deme, source:18:23}. Ardından devam eder: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh, veẕkur rabbeke iẕâ nesît, gloss:ancak "Allah dilerse" de; unuttuğun zaman da Rabbini an, source:18:24}. İstisna, unutma ve anma bu ayette üst üste gelir. Unutmanın çaresi anmaktır. Kur'an unutmayı müminlerin duasına da koyar: {ar:رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا, tr:rabbenâ lâ tuâhıẕnâ in nesînâ ev ahta'nâ, gloss:Rabbimiz, unutur ya da yanılırsak bizi sorumlu tutma, source:2:286}. Altıncı ayetin vaadi, insanın bu duayla korunmaya çalıştığı zaafı Peygamber'in okutulan sözle ilişkisinde ondan alır.

[¶15] Bu vaadin bir görevi vardır. Altıncı ayetin fe-'si dokuzuncu ayette yeniden gelir: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öyleyse hatırlat, eğer hatırlatma fayda verirse, source:87:9}. Unutmanın karşıtı anmaktı. Unutmayacağına söz verilen kişi, başkalarına hatırlatmakla görevlendirilir. İçinde toplanan söz dışarı verilir. Rahim imgesinin iki ucu, yani tutmak ve vakti gelince bırakmak, burada surenin kendi sırasıyla yerine oturur: önce okutma ve unutmama, sonra hatırlatma. Kur'an unutturmayı hatırlatmanın karşısına başka bir yerde de koyar. Allah, ayetleri hakkında boş konuşanlardan uzak durmasını Peygamber'e emrederken şöyle der: {ar:وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ, tr:ve immâ yunsiyenneke'ş-şeytânu fe-lâ tak'ud ba'de'ẕ-ẕikrâ mea'l-kavmi'z-zâlimîn, gloss:eğer şeytan sana unutturursa, hatırladıktan sonra o zalim toplulukla oturma, source:6:68}. Dokuzuncu ayetin "zikrâ"sı orada unutmanın hemen ardından gelir. Onuncu ayet hatırlatmanın karşılığını yine se- ekiyle verir: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10}. Altıncı ayetteki "se-nukriuke" ile onuncu ayetteki "se-yeẕẕekkeru" birbirine karşılık verir. Peygamber'e unutmamak vaat edilir, içi titreyen kişiye de hatırlamak.

[¶16] Bu üç ayetin kelimeleri Kur'an'da tek bir cümlede de buluşur. Nuh'un kavminin elçilerini yalanlaması, göğün kapılarının boşalan suyla açılması ve Nuh'un tahtalarla çivilerden yapılmış bir gemide taşınması anlatılır. Ardından şu nakarat gelir: {ar:وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ, tr:ve lekad yessernâ'l-kur'âne li'ẕ-ẕikri fe-hel min muddekir, gloss:andolsun, Kur'an'ı öğüt almak için kolaylaştırdık; öğüt alan yok mu, source:54:17}. Okumanın kökü, sekizinci ayetin kolaylaştırma fiili ve dokuzuncu ile onuncu ayetlerin anma kökü bu ayette bir aradadır. Sekizinci ayette kolaylaştırılan Peygamber'dir, bu nakaratta Kur'an. İkisi aynı amaca bağlanır: sözün akılda kalması ve hatırlatılabilmesi. Bir başka surede aynı bağ şöyle kurulur: {ar:فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ, tr:fe-innemâ yessernâhu bi-lisânike le'allehum yeteẕekkerûn, gloss:onu senin dilinde kolaylaştırdık ki düşünüp öğüt alsınlar, source:44:58}. Gece namazını anlatan uzun bir ayette de okuma ile kolaylık yan yana gelir. Allah, insanların gecenin ne kadarını namazla geçirdiklerini sayamayacaklarını bildiğini söyler ve iki kez şunu emreder: {ar:فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ, tr:fakraû mâ teyessera mine'l-kur'ân, gloss:Kur'an'dan kolayınıza geleni okuyun, source:73:20}. Okutmak ve kolaylaştırmak, sekizinci ayette olduğu gibi orada da aynı yöne akar.

[¶17] Okumanın bir hayat biçimine dönüştüğü de söylenirdi. Kendini ibadete veren kişiye {ar:رجل قارئ عابد ناسك, tr:raculun kâriun âbidun nâsik, gloss:okur, yani ibadete ve kulluğa bağlı bir adam, source:"ق ر ء,B006"} denirdi. "Tekarra'tu" sözü ise anlayışı anlatırdı: {ar:تقرأت تفقهت, tr:tekarra'tu tefakkahtu, gloss:okur oldum, yani derinden kavradım, source:"ق ر ء,B006"}. Bu kullanımda okumak, sözü yalnızca dilde tekrarlamak değildir. Okumak, onunla yaşanan bir kulluk ve bir kavrayıştır. On beşinci ayette Rabbinin adını anıp namaz kılan kişi bu okurun surede çizilen yüzüdür. On sekizinci ve on dokuzuncu ayetler okutulan sözün ilk sayfalarda, İbrahim'in ve Musa'nın sayfalarında da bulunduğunu söyler. Peygamber'in içinde toplanacak söz böylece daha önce deriye yazılıp toplanmış bir sözün devamı olur.

===== _commentary/v16/out/87_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: لا + indicative retaining final alif marks statement; prohibition would be تَنسَ
- memory: سَـ prefix marks near future
- memory: سَلًى as fetal membrane expelled after birth
- not written: ق ر ء B003 qur' as menstrual/purity period and its time sense - fit only through womb image, delicate and adds nothing beyond B004
- not written: ق ر ء B005 time, wind's season, need drawing near - no grounding in the ayah beyond the bare "sa-" future
- not written: ق ر ء B012 witnesses who gather knowledge - unhamzated form, speculative analogy, uncertain identity
- not written: ق ر ء B008, B009, B010, B013 (plague, mating season, detaining slave girl, livestock) - no bearing on reading or memory
- not written: ن س ي B004 sciatic vein - stray sense, no thematic work
- not written: ن س ي B005-B007 deferral, staff, watered milk - hamzated نسأ, a different root in practice
- not written: نسي as menstrual rag (B003) - adds no meaning beyond discarded thing
- not written: 18:63 servant forgetting the fish - overlaps with 6:68 in showing Satan-caused forgetting

===== passages not cited (210) =====
## strong (this ayah's own list) (11)

- (9:67) [listed for 87:6] ٱلْمُنَٰفِقُونَ وَٱلْمُنَٰفِقَٰتُ بَعْضُهُم مِّنۢ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمُنكَرِ وَيَنْهَوْنَ عَنِ ٱلْمَعْرُوفِ وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ
- (15:9) [listed for 87:6] إِنَّا نَحْنُ نَزَّلْنَا ٱلذِّكْرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ
- (17:86) [listed for 87:6] وَلَئِن شِئْنَا لَنَذْهَبَنَّ بِٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ ثُمَّ لَا تَجِدُ لَكَ بِهِۦ عَلَيْنَا وَكِيلًا
- (20:114) [listed for 87:6] [cited in ¶12] فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۗ وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا
- (20:126) [listed for 87:6] [cited in ¶10] قَالَ كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ
- (25:32) [listed for 87:6] [cited in ¶5] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَوْلَا نُزِّلَ عَلَيْهِ ٱلْقُرْءَانُ جُمْلَةًۭ وَٰحِدَةًۭ ۚ كَذَٰلِكَ لِنُثَبِّتَ بِهِۦ فُؤَادَكَ ۖ وَرَتَّلْنَٰهُ تَرْتِيلًۭا
- (29:49) [listed for 87:6] بَلْ هُوَ ءَايَٰتٌۢ بَيِّنَٰتٌۭ فِى صُدُورِ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلظَّٰلِمُونَ
- (56:78) [listed for 87:6] فِى كِتَٰبٍۢ مَّكْنُونٍۢ
- (75:16) [listed for 87:6] [cited in ¶2] لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ
- (75:17) [listed for 87:6] [cited in ¶2] إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ
- (85:22) [listed for 87:6] فِى لَوْحٍۢ مَّحْفُوظٍۭ

## medium (this ayah's own list) (39)

- (2:286) [listed for 87:6] [cited in ¶14] لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا ٱكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَآ إِصْرًۭا كَمَا حَمَلْتَهُۥ عَلَى ٱلَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِۦ ۖ وَٱعْفُ عَنَّا وَٱغْفِرْ لَنَا وَٱرْحَمْنَآ ۚ أَنتَ مَوْلَىٰنَا فَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (5:13) [listed for 87:6] فَبِمَا نَقْضِهِم مِّيثَٰقَهُمْ لَعَنَّٰهُمْ وَجَعَلْنَا قُلُوبَهُمْ قَٰسِيَةًۭ ۖ يُحَرِّفُونَ ٱلْكَلِمَ عَن مَّوَاضِعِهِۦ ۙ وَنَسُوا۟ حَظًّۭا مِّمَّا ذُكِّرُوا۟ بِهِۦ ۚ وَلَا تَزَالُ تَطَّلِعُ عَلَىٰ خَآئِنَةٍۢ مِّنْهُمْ إِلَّا قَلِيلًۭا مِّنْهُمْ ۖ فَٱعْفُ عَنْهُمْ وَٱصْفَحْ ۚ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُحْسِنِينَ
- (6:44) [listed for 87:6] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦ فَتَحْنَا عَلَيْهِمْ أَبْوَٰبَ كُلِّ شَىْءٍ حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ فَإِذَا هُم مُّبْلِسُونَ
- (6:68) [listed for 87:6] [cited in ¶15] وَإِذَا رَأَيْتَ ٱلَّذِينَ يَخُوضُونَ فِىٓ ءَايَٰتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦ ۚ وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (7:165) [listed for 87:6] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦٓ أَنجَيْنَا ٱلَّذِينَ يَنْهَوْنَ عَنِ ٱلسُّوٓءِ وَأَخَذْنَا ٱلَّذِينَ ظَلَمُوا۟ بِعَذَابٍۭ بَـِٔيسٍۭ بِمَا كَانُوا۟ يَفْسُقُونَ
- (10:37) [listed for 87:6] وَمَا كَانَ هَٰذَا ٱلْقُرْءَانُ أَن يُفْتَرَىٰ مِن دُونِ ٱللَّهِ وَلَٰكِن تَصْدِيقَ ٱلَّذِى بَيْنَ يَدَيْهِ وَتَفْصِيلَ ٱلْكِتَٰبِ لَا رَيْبَ فِيهِ مِن رَّبِّ ٱلْعَٰلَمِينَ
- (10:61) [listed for 87:6] وَمَا تَكُونُ فِى شَأْنٍۢ وَمَا تَتْلُوا۟ مِنْهُ مِن قُرْءَانٍۢ وَلَا تَعْمَلُونَ مِنْ عَمَلٍ إِلَّا كُنَّا عَلَيْكُمْ شُهُودًا إِذْ تُفِيضُونَ فِيهِ ۚ وَمَا يَعْزُبُ عَن رَّبِّكَ مِن مِّثْقَالِ ذَرَّةٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ وَلَآ أَصْغَرَ مِن ذَٰلِكَ وَلَآ أَكْبَرَ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍ
- (10:94) [listed for 87:6] فَإِن كُنتَ فِى شَكٍّۢ مِّمَّآ أَنزَلْنَآ إِلَيْكَ فَسْـَٔلِ ٱلَّذِينَ يَقْرَءُونَ ٱلْكِتَٰبَ مِن قَبْلِكَ ۚ لَقَدْ جَآءَكَ ٱلْحَقُّ مِن رَّبِّكَ فَلَا تَكُونَنَّ مِنَ ٱلْمُمْتَرِينَ
- (12:42) [listed for 87:6] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (17:14) [listed for 87:6] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
- (18:24) [listed for 87:6] [cited in ¶14] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (19:64) [listed for 87:6] [cited in ¶12] وَمَا نَتَنَزَّلُ إِلَّا بِأَمْرِ رَبِّكَ ۖ لَهُۥ مَا بَيْنَ أَيْدِينَا وَمَا خَلْفَنَا وَمَا بَيْنَ ذَٰلِكَ ۚ وَمَا كَانَ رَبُّكَ نَسِيًّۭا
- (20:52) [listed for 87:6] [cited in ¶12] قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى
- (20:115) [listed for 87:6] [cited in ¶12] وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا
- (23:110) [listed for 87:6] فَٱتَّخَذْتُمُوهُمْ سِخْرِيًّا حَتَّىٰٓ أَنسَوْكُمْ ذِكْرِى وَكُنتُم مِّنْهُمْ تَضْحَكُونَ
- (26:199) [listed for 87:6] فَقَرَأَهُۥ عَلَيْهِم مَّا كَانُوا۟ بِهِۦ مُؤْمِنِينَ
- (32:14) [listed for 87:6] فَذُوقُوا۟ بِمَا نَسِيتُمْ لِقَآءَ يَوْمِكُمْ هَٰذَآ إِنَّا نَسِينَٰكُمْ ۖ وَذُوقُوا۟ عَذَابَ ٱلْخُلْدِ بِمَا كُنتُمْ تَعْمَلُونَ
- (36:78) [listed for 87:6] وَضَرَبَ لَنَا مَثَلًۭا وَنَسِىَ خَلْقَهُۥ ۖ قَالَ مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌۭ
- (38:1) [listed for 87:6] صٓ ۚ وَٱلْقُرْءَانِ ذِى ٱلذِّكْرِ
- (39:23) [listed for 87:6] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (41:41) [listed for 87:6] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (41:42) [listed for 87:6] لَّا يَأْتِيهِ ٱلْبَٰطِلُ مِنۢ بَيْنِ يَدَيْهِ وَلَا مِنْ خَلْفِهِۦ ۖ تَنزِيلٌۭ مِّنْ حَكِيمٍ حَمِيدٍۢ
- (44:58) [listed for 87:6] [cited in ¶16] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (45:34) [listed for 87:6] وَقِيلَ ٱلْيَوْمَ نَنسَىٰكُمْ كَمَا نَسِيتُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا وَمَأْوَىٰكُمُ ٱلنَّارُ وَمَا لَكُم مِّن نَّٰصِرِينَ
- (54:22) [listed for 87:6] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (55:2) [listed for 87:6] عَلَّمَ ٱلْقُرْءَانَ
- (58:6) [listed for 87:6] يَوْمَ يَبْعَثُهُمُ ٱللَّهُ جَمِيعًۭا فَيُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
- (58:19) [listed for 87:6] ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ ۚ أَلَآ إِنَّ حِزْبَ ٱلشَّيْطَٰنِ هُمُ ٱلْخَٰسِرُونَ
- (59:19) [listed for 87:6] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (69:19) [listed for 87:6] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (73:4) [listed for 87:6] [cited in ¶5] أَوْ زِدْ عَلَيْهِ وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا
- (75:18) [listed for 87:6] [cited in ¶2] فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ
- (75:19) [listed for 87:6] [cited in ¶2] ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ
- (76:23) [listed for 87:6] إِنَّا نَحْنُ نَزَّلْنَا عَلَيْكَ ٱلْقُرْءَانَ تَنزِيلًۭا
- (80:13) [listed for 87:6] فِى صُحُفٍۢ مُّكَرَّمَةٍۢ
- (84:21) [listed for 87:6] وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ ۩
- (85:21) [listed for 87:6] بَلْ هُوَ قُرْءَانٌۭ مَّجِيدٌۭ
- (96:3) [listed for 87:6] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- (98:2) [listed for 87:6] رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ

## named by the passage's own list as strong for this ayah (15)

- (3:58) [listed for 87:6] ذَٰلِكَ نَتْلُوهُ عَلَيْكَ مِنَ ٱلْءَايَٰتِ وَٱلذِّكْرِ ٱلْحَكِيمِ
- (10:16) [listed for 87:6] قُل لَّوْ شَآءَ ٱللَّهُ مَا تَلَوْتُهُۥ عَلَيْكُمْ وَلَآ أَدْرَىٰكُم بِهِۦ ۖ فَقَدْ لَبِثْتُ فِيكُمْ عُمُرًۭا مِّن قَبْلِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (18:65) [listed for 87:6] فَوَجَدَا عَبْدًۭا مِّنْ عِبَادِنَآ ءَاتَيْنَٰهُ رَحْمَةًۭ مِّنْ عِندِنَا وَعَلَّمْنَٰهُ مِن لَّدُنَّا عِلْمًۭا
- (20:2) [listed for 87:6] مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ
- (22:52) [listed for 87:6] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ مِن رَّسُولٍۢ وَلَا نَبِىٍّ إِلَّآ إِذَا تَمَنَّىٰٓ أَلْقَى ٱلشَّيْطَٰنُ فِىٓ أُمْنِيَّتِهِۦ فَيَنسَخُ ٱللَّهُ مَا يُلْقِى ٱلشَّيْطَٰنُ ثُمَّ يُحْكِمُ ٱللَّهُ ءَايَٰتِهِۦ ۗ وَٱللَّهُ عَلِيمٌ حَكِيمٌۭ
- (27:6) [listed for 87:6] وَإِنَّكَ لَتُلَقَّى ٱلْقُرْءَانَ مِن لَّدُنْ حَكِيمٍ عَلِيمٍ
- (27:92) [listed for 87:6] وَأَنْ أَتْلُوَا۟ ٱلْقُرْءَانَ ۖ فَمَنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَقُلْ إِنَّمَآ أَنَا۠ مِنَ ٱلْمُنذِرِينَ
- (28:51) [listed for 87:6] ۞ وَلَقَدْ وَصَّلْنَا لَهُمُ ٱلْقَوْلَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (37:3) [listed for 87:6] فَٱلتَّٰلِيَٰتِ ذِكْرًا
- (54:17) [listed for 87:6] [cited in ¶16] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (62:2) [listed for 87:6] هُوَ ٱلَّذِى بَعَثَ فِى ٱلْأُمِّيِّۦنَ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍۢ
- (72:27) [listed for 87:6] إِلَّا مَنِ ٱرْتَضَىٰ مِن رَّسُولٍۢ فَإِنَّهُۥ يَسْلُكُ مِنۢ بَيْنِ يَدَيْهِ وَمِنْ خَلْفِهِۦ رَصَدًۭا
- (72:28) [listed for 87:6] لِّيَعْلَمَ أَن قَدْ أَبْلَغُوا۟ رِسَٰلَٰتِ رَبِّهِمْ وَأَحَاطَ بِمَا لَدَيْهِمْ وَأَحْصَىٰ كُلَّ شَىْءٍ عَدَدًۢا
- (73:5) [listed for 87:6] إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًۭا ثَقِيلًا
- (96:1) [listed for 87:6] [cited in ¶4] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ

## named by the passage's own list as medium for this ayah (54)

- (2:44) [listed for 87:6] ۞ أَتَأْمُرُونَ ٱلنَّاسَ بِٱلْبِرِّ وَتَنسَوْنَ أَنفُسَكُمْ وَأَنتُمْ تَتْلُونَ ٱلْكِتَٰبَ ۚ أَفَلَا تَعْقِلُونَ
- (2:106) [listed for 87:6] [cited in ¶13] ۞ مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ ۗ أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (2:151) [listed for 87:6] كَمَآ أَرْسَلْنَا فِيكُمْ رَسُولًۭا مِّنكُمْ يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِنَا وَيُزَكِّيكُمْ وَيُعَلِّمُكُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (2:185) [listed for 87:6] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
- (2:252) [listed for 87:6] تِلْكَ ءَايَٰتُ ٱللَّهِ نَتْلُوهَا عَلَيْكَ بِٱلْحَقِّ ۚ وَإِنَّكَ لَمِنَ ٱلْمُرْسَلِينَ
- (3:79) [listed for 87:6] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
- (3:108) [listed for 87:6] تِلْكَ ءَايَٰتُ ٱللَّهِ نَتْلُوهَا عَلَيْكَ بِٱلْحَقِّ ۗ وَمَا ٱللَّهُ يُرِيدُ ظُلْمًۭا لِّلْعَٰلَمِينَ
- (3:164) [listed for 87:6] لَقَدْ مَنَّ ٱللَّهُ عَلَى ٱلْمُؤْمِنِينَ إِذْ بَعَثَ فِيهِمْ رَسُولًۭا مِّنْ أَنفُسِهِمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍ
- (5:67) [listed for 87:6] ۞ يَٰٓأَيُّهَا ٱلرَّسُولُ بَلِّغْ مَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ۖ وَإِن لَّمْ تَفْعَلْ فَمَا بَلَّغْتَ رِسَالَتَهُۥ ۚ وَٱللَّهُ يَعْصِمُكَ مِنَ ٱلنَّاسِ ۗ إِنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (6:50) [listed for 87:6] قُل لَّآ أَقُولُ لَكُمْ عِندِى خَزَآئِنُ ٱللَّهِ وَلَآ أَعْلَمُ ٱلْغَيْبَ وَلَآ أَقُولُ لَكُمْ إِنِّى مَلَكٌ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ ۚ أَفَلَا تَتَفَكَّرُونَ
- (6:91) [listed for 87:6] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦٓ إِذْ قَالُوا۟ مَآ أَنزَلَ ٱللَّهُ عَلَىٰ بَشَرٍۢ مِّن شَىْءٍۢ ۗ قُلْ مَنْ أَنزَلَ ٱلْكِتَٰبَ ٱلَّذِى جَآءَ بِهِۦ مُوسَىٰ نُورًۭا وَهُدًۭى لِّلنَّاسِ ۖ تَجْعَلُونَهُۥ قَرَاطِيسَ تُبْدُونَهَا وَتُخْفُونَ كَثِيرًۭا ۖ وَعُلِّمْتُم مَّا لَمْ تَعْلَمُوٓا۟ أَنتُمْ وَلَآ ءَابَآؤُكُمْ ۖ قُلِ ٱللَّهُ ۖ ثُمَّ ذَرْهُمْ فِى خَوْضِهِمْ يَلْعَبُونَ
- (6:93) [listed for 87:6] وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ قَالَ أُوحِىَ إِلَىَّ وَلَمْ يُوحَ إِلَيْهِ شَىْءٌۭ وَمَن قَالَ سَأُنزِلُ مِثْلَ مَآ أَنزَلَ ٱللَّهُ ۗ وَلَوْ تَرَىٰٓ إِذِ ٱلظَّٰلِمُونَ فِى غَمَرَٰتِ ٱلْمَوْتِ وَٱلْمَلَٰٓئِكَةُ بَاسِطُوٓا۟ أَيْدِيهِمْ أَخْرِجُوٓا۟ أَنفُسَكُمُ ۖ ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَقُولُونَ عَلَى ٱللَّهِ غَيْرَ ٱلْحَقِّ وَكُنتُمْ عَنْ ءَايَٰتِهِۦ تَسْتَكْبِرُونَ
- (7:203) [listed for 87:6] وَإِذَا لَمْ تَأْتِهِم بِـَٔايَةٍۢ قَالُوا۟ لَوْلَا ٱجْتَبَيْتَهَا ۚ قُلْ إِنَّمَآ أَتَّبِعُ مَا يُوحَىٰٓ إِلَىَّ مِن رَّبِّى ۚ هَٰذَا بَصَآئِرُ مِن رَّبِّكُمْ وَهُدًۭى وَرَحْمَةٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:204) [listed for 87:6] وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (10:15) [listed for 87:6] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَاتُنَا بَيِّنَٰتٍۢ ۙ قَالَ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا ٱئْتِ بِقُرْءَانٍ غَيْرِ هَٰذَآ أَوْ بَدِّلْهُ ۚ قُلْ مَا يَكُونُ لِىٓ أَنْ أُبَدِّلَهُۥ مِن تِلْقَآئِ نَفْسِىٓ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ ۖ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (12:3) [listed for 87:6] نَحْنُ نَقُصُّ عَلَيْكَ أَحْسَنَ ٱلْقَصَصِ بِمَآ أَوْحَيْنَآ إِلَيْكَ هَٰذَا ٱلْقُرْءَانَ وَإِن كُنتَ مِن قَبْلِهِۦ لَمِنَ ٱلْغَٰفِلِينَ
- (13:30) [listed for 87:6] كَذَٰلِكَ أَرْسَلْنَٰكَ فِىٓ أُمَّةٍۢ قَدْ خَلَتْ مِن قَبْلِهَآ أُمَمٌۭ لِّتَتْلُوَا۟ عَلَيْهِمُ ٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَهُمْ يَكْفُرُونَ بِٱلرَّحْمَٰنِ ۚ قُلْ هُوَ رَبِّى لَآ إِلَٰهَ إِلَّا هُوَ عَلَيْهِ تَوَكَّلْتُ وَإِلَيْهِ مَتَابِ
- (13:39) [listed for 87:6] يَمْحُوا۟ ٱللَّهُ مَا يَشَآءُ وَيُثْبِتُ ۖ وَعِندَهُۥٓ أُمُّ ٱلْكِتَٰبِ
- (15:87) [listed for 87:6] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (15:91) [listed for 87:6] ٱلَّذِينَ جَعَلُوا۟ ٱلْقُرْءَانَ عِضِينَ
- (16:43) [listed for 87:6] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ إِلَّا رِجَالًۭا نُّوحِىٓ إِلَيْهِمْ ۚ فَسْـَٔلُوٓا۟ أَهْلَ ٱلذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ
- (16:44) [listed for 87:6] بِٱلْبَيِّنَٰتِ وَٱلزُّبُرِ ۗ وَأَنزَلْنَآ إِلَيْكَ ٱلذِّكْرَ لِتُبَيِّنَ لِلنَّاسِ مَا نُزِّلَ إِلَيْهِمْ وَلَعَلَّهُمْ يَتَفَكَّرُونَ
- (16:98) [listed for 87:6] فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ فَٱسْتَعِذْ بِٱللَّهِ مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ
- (16:101) [listed for 87:6] وَإِذَا بَدَّلْنَآ ءَايَةًۭ مَّكَانَ ءَايَةٍۢ ۙ وَٱللَّهُ أَعْلَمُ بِمَا يُنَزِّلُ قَالُوٓا۟ إِنَّمَآ أَنتَ مُفْتَرٍۭ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (16:103) [listed for 87:6] وَلَقَدْ نَعْلَمُ أَنَّهُمْ يَقُولُونَ إِنَّمَا يُعَلِّمُهُۥ بَشَرٌۭ ۗ لِّسَانُ ٱلَّذِى يُلْحِدُونَ إِلَيْهِ أَعْجَمِىٌّۭ وَهَٰذَا لِسَانٌ عَرَبِىٌّۭ مُّبِينٌ
- (17:88) [listed for 87:6] قُل لَّئِنِ ٱجْتَمَعَتِ ٱلْإِنسُ وَٱلْجِنُّ عَلَىٰٓ أَن يَأْتُوا۟ بِمِثْلِ هَٰذَا ٱلْقُرْءَانِ لَا يَأْتُونَ بِمِثْلِهِۦ وَلَوْ كَانَ بَعْضُهُمْ لِبَعْضٍۢ ظَهِيرًۭا
- (17:106) [listed for 87:6] [cited in ¶7] وَقُرْءَانًۭا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍۢ وَنَزَّلْنَٰهُ تَنزِيلًۭا
- (18:1) [listed for 87:6] ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَنزَلَ عَلَىٰ عَبْدِهِ ٱلْكِتَٰبَ وَلَمْ يَجْعَل لَّهُۥ عِوَجَا ۜ
- (18:27) [listed for 87:6] وَٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِن كِتَابِ رَبِّكَ ۖ لَا مُبَدِّلَ لِكَلِمَٰتِهِۦ وَلَن تَجِدَ مِن دُونِهِۦ مُلْتَحَدًۭا
- (20:4) [listed for 87:6] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:13) [listed for 87:6] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
- (26:194) [listed for 87:6] عَلَىٰ قَلْبِكَ لِتَكُونَ مِنَ ٱلْمُنذِرِينَ
- (28:45) [listed for 87:6] وَلَٰكِنَّآ أَنشَأْنَا قُرُونًۭا فَتَطَاوَلَ عَلَيْهِمُ ٱلْعُمُرُ ۚ وَمَا كُنتَ ثَاوِيًۭا فِىٓ أَهْلِ مَدْيَنَ تَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِنَا وَلَٰكِنَّا كُنَّا مُرْسِلِينَ
- (33:2) [listed for 87:6] وَٱتَّبِعْ مَا يُوحَىٰٓ إِلَيْكَ مِن رَّبِّكَ ۚ إِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
- (37:155) [listed for 87:6] أَفَلَا تَذَكَّرُونَ
- (41:3) [listed for 87:6] كِتَٰبٌۭ فُصِّلَتْ ءَايَٰتُهُۥ قُرْءَانًا عَرَبِيًّۭا لِّقَوْمٍۢ يَعْلَمُونَ
- (42:51) [listed for 87:6] ۞ وَمَا كَانَ لِبَشَرٍ أَن يُكَلِّمَهُ ٱللَّهُ إِلَّا وَحْيًا أَوْ مِن وَرَآئِ حِجَابٍ أَوْ يُرْسِلَ رَسُولًۭا فَيُوحِىَ بِإِذْنِهِۦ مَا يَشَآءُ ۚ إِنَّهُۥ عَلِىٌّ حَكِيمٌۭ
- (43:3) [listed for 87:6] إِنَّا جَعَلْنَٰهُ قُرْءَٰنًا عَرَبِيًّۭا لَّعَلَّكُمْ تَعْقِلُونَ
- (44:3) [listed for 87:6] إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةٍۢ مُّبَٰرَكَةٍ ۚ إِنَّا كُنَّا مُنذِرِينَ
- (45:6) [listed for 87:6] تِلْكَ ءَايَٰتُ ٱللَّهِ نَتْلُوهَا عَلَيْكَ بِٱلْحَقِّ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَ ٱللَّهِ وَءَايَٰتِهِۦ يُؤْمِنُونَ
- (53:4) [listed for 87:6] إِنْ هُوَ إِلَّا وَحْىٌۭ يُوحَىٰ
- (53:10) [listed for 87:6] فَأَوْحَىٰٓ إِلَىٰ عَبْدِهِۦ مَآ أَوْحَىٰ
- (55:4) [listed for 87:6] عَلَّمَهُ ٱلْبَيَانَ
- (56:77) [listed for 87:6] إِنَّهُۥ لَقُرْءَانٌۭ كَرِيمٌۭ
- (68:52) [listed for 87:6] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (69:38) [listed for 87:6] فَلَآ أُقْسِمُ بِمَا تُبْصِرُونَ
- (69:41) [listed for 87:6] وَمَا هُوَ بِقَوْلِ شَاعِرٍۢ ۚ قَلِيلًۭا مَّا تُؤْمِنُونَ
- (69:43) [listed for 87:6] تَنزِيلٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (75:31) [listed for 87:6] فَلَا صَدَّقَ وَلَا صَلَّىٰ
- (81:24) [listed for 87:6] وَمَا هُوَ عَلَى ٱلْغَيْبِ بِضَنِينٍۢ
- (92:7) [listed for 87:6] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (96:4) [listed for 87:6] ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- (96:5) [listed for 87:6] [cited in ¶4] عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- (97:1) [listed for 87:6] إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ

## weak (this ayah's own list) (21)

- (2:121) [listed for 87:6] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَتْلُونَهُۥ حَقَّ تِلَاوَتِهِۦٓ أُو۟لَٰٓئِكَ يُؤْمِنُونَ بِهِۦ ۗ وَمَن يَكْفُرْ بِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (2:203) [listed for 87:6] ۞ وَٱذْكُرُوا۟ ٱللَّهَ فِىٓ أَيَّامٍۢ مَّعْدُودَٰتٍۢ ۚ فَمَن تَعَجَّلَ فِى يَوْمَيْنِ فَلَآ إِثْمَ عَلَيْهِ وَمَن تَأَخَّرَ فَلَآ إِثْمَ عَلَيْهِ ۚ لِمَنِ ٱتَّقَىٰ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّكُمْ إِلَيْهِ تُحْشَرُونَ
- (2:228) [listed for 87:6] وَٱلْمُطَلَّقَٰتُ يَتَرَبَّصْنَ بِأَنفُسِهِنَّ ثَلَٰثَةَ قُرُوٓءٍۢ ۚ وَلَا يَحِلُّ لَهُنَّ أَن يَكْتُمْنَ مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ إِن كُنَّ يُؤْمِنَّ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَبُعُولَتُهُنَّ أَحَقُّ بِرَدِّهِنَّ فِى ذَٰلِكَ إِنْ أَرَادُوٓا۟ إِصْلَٰحًۭا ۚ وَلَهُنَّ مِثْلُ ٱلَّذِى عَلَيْهِنَّ بِٱلْمَعْرُوفِ ۚ وَلِلرِّجَالِ عَلَيْهِنَّ دَرَجَةٌۭ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ
- (2:237) [listed for 87:6] وَإِن طَلَّقْتُمُوهُنَّ مِن قَبْلِ أَن تَمَسُّوهُنَّ وَقَدْ فَرَضْتُمْ لَهُنَّ فَرِيضَةًۭ فَنِصْفُ مَا فَرَضْتُمْ إِلَّآ أَن يَعْفُونَ أَوْ يَعْفُوَا۟ ٱلَّذِى بِيَدِهِۦ عُقْدَةُ ٱلنِّكَاحِ ۚ وَأَن تَعْفُوٓا۟ أَقْرَبُ لِلتَّقْوَىٰ ۚ وَلَا تَنسَوُا۟ ٱلْفَضْلَ بَيْنَكُمْ ۚ إِنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌ
- (5:14) [listed for 87:6] وَمِنَ ٱلَّذِينَ قَالُوٓا۟ إِنَّا نَصَٰرَىٰٓ أَخَذْنَا مِيثَٰقَهُمْ فَنَسُوا۟ حَظًّۭا مِّمَّا ذُكِّرُوا۟ بِهِۦ فَأَغْرَيْنَا بَيْنَهُمُ ٱلْعَدَاوَةَ وَٱلْبَغْضَآءَ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۚ وَسَوْفَ يُنَبِّئُهُمُ ٱللَّهُ بِمَا كَانُوا۟ يَصْنَعُونَ
- (6:41) [listed for 87:6] بَلْ إِيَّاهُ تَدْعُونَ فَيَكْشِفُ مَا تَدْعُونَ إِلَيْهِ إِن شَآءَ وَتَنسَوْنَ مَا تُشْرِكُونَ
- (7:2) [listed for 87:6] كِتَٰبٌ أُنزِلَ إِلَيْكَ فَلَا يَكُن فِى صَدْرِكَ حَرَجٌۭ مِّنْهُ لِتُنذِرَ بِهِۦ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
- (7:51) [listed for 87:6] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (18:73) [listed for 87:6] قَالَ لَا تُؤَاخِذْنِى بِمَا نَسِيتُ وَلَا تُرْهِقْنِى مِنْ أَمْرِى عُسْرًۭا
- (20:88) [listed for 87:6] فَأَخْرَجَ لَهُمْ عِجْلًۭا جَسَدًۭا لَّهُۥ خُوَارٌۭ فَقَالُوا۟ هَٰذَآ إِلَٰهُكُمْ وَإِلَٰهُ مُوسَىٰ فَنَسِىَ
- (25:18) [listed for 87:6] قَالُوا۟ سُبْحَٰنَكَ مَا كَانَ يَنۢبَغِى لَنَآ أَن نَّتَّخِذَ مِن دُونِكَ مِنْ أَوْلِيَآءَ وَلَٰكِن مَّتَّعْتَهُمْ وَءَابَآءَهُمْ حَتَّىٰ نَسُوا۟ ٱلذِّكْرَ وَكَانُوا۟ قَوْمًۢا بُورًۭا
- (25:52) [listed for 87:6] فَلَا تُطِعِ ٱلْكَٰفِرِينَ وَجَٰهِدْهُم بِهِۦ جِهَادًۭا كَبِيرًۭا
- (30:58) [listed for 87:6] وَلَقَدْ ضَرَبْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍۢ ۚ وَلَئِن جِئْتَهُم بِـَٔايَةٍۢ لَّيَقُولَنَّ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ أَنتُمْ إِلَّا مُبْطِلُونَ
- (34:31) [listed for 87:6] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَن نُّؤْمِنَ بِهَٰذَا ٱلْقُرْءَانِ وَلَا بِٱلَّذِى بَيْنَ يَدَيْهِ ۗ وَلَوْ تَرَىٰٓ إِذِ ٱلظَّٰلِمُونَ مَوْقُوفُونَ عِندَ رَبِّهِمْ يَرْجِعُ بَعْضُهُمْ إِلَىٰ بَعْضٍ ٱلْقَوْلَ يَقُولُ ٱلَّذِينَ ٱسْتُضْعِفُوا۟ لِلَّذِينَ ٱسْتَكْبَرُوا۟ لَوْلَآ أَنتُمْ لَكُنَّا مُؤْمِنِينَ
- (36:2) [listed for 87:6] وَٱلْقُرْءَانِ ٱلْحَكِيمِ
- (38:26) [listed for 87:6] يَٰدَاوُۥدُ إِنَّا جَعَلْنَٰكَ خَلِيفَةًۭ فِى ٱلْأَرْضِ فَٱحْكُم بَيْنَ ٱلنَّاسِ بِٱلْحَقِّ وَلَا تَتَّبِعِ ٱلْهَوَىٰ فَيُضِلَّكَ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّ ٱلَّذِينَ يَضِلُّونَ عَن سَبِيلِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۢ بِمَا نَسُوا۟ يَوْمَ ٱلْحِسَابِ
- (39:8) [listed for 87:6] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (50:1) [listed for 87:6] قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ
- (72:1) [listed for 87:6] قُلْ أُوحِىَ إِلَىَّ أَنَّهُ ٱسْتَمَعَ نَفَرٌۭ مِّنَ ٱلْجِنِّ فَقَالُوٓا۟ إِنَّا سَمِعْنَا قُرْءَانًا عَجَبًۭا
- (82:10) [listed for 87:6] وَإِنَّ عَلَيْكُمْ لَحَٰفِظِينَ
- (93:10) [listed for 87:6] وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ

## named by the passage's own list as weak for this ayah (8)

- (4:82) [listed for 87:6] أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ ۚ وَلَوْ كَانَ مِنْ عِندِ غَيْرِ ٱللَّهِ لَوَجَدُوا۟ فِيهِ ٱخْتِلَٰفًۭا كَثِيرًۭا
- (6:155) [listed for 87:6] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ فَٱتَّبِعُوهُ وَٱتَّقُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (12:2) [listed for 87:6] إِنَّآ أَنزَلْنَٰهُ قُرْءَٰنًا عَرَبِيًّۭا لَّعَلَّكُمْ تَعْقِلُونَ
- (17:45) [listed for 87:6] وَإِذَا قَرَأْتَ ٱلْقُرْءَانَ جَعَلْنَا بَيْنَكَ وَبَيْنَ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ حِجَابًۭا مَّسْتُورًۭا
- (20:16) [listed for 87:6] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (53:60) [listed for 87:6] وَتَضْحَكُونَ وَلَا تَبْكُونَ
- (76:12) [listed for 87:6] وَجَزَىٰهُم بِمَا صَبَرُوا۟ جَنَّةًۭ وَحَرِيرًۭا
- (93:9) [listed for 87:6] فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ

## neighbours: within two ayat of a passage the commentary cites (62)

- (2:104) [next to 2:106] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقُولُوا۟ رَٰعِنَا وَقُولُوا۟ ٱنظُرْنَا وَٱسْمَعُوا۟ ۗ وَلِلْكَٰفِرِينَ عَذَابٌ أَلِيمٌۭ
- (2:105) [next to 2:106] مَّا يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَلَا ٱلْمُشْرِكِينَ أَن يُنَزَّلَ عَلَيْكُم مِّنْ خَيْرٍۢ مِّن رَّبِّكُمْ ۗ وَٱللَّهُ يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (2:107) [next to 2:106] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
- (2:108) [next to 2:106] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (2:284) [next to 2:286] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (2:285) [next to 2:286] ءَامَنَ ٱلرَّسُولُ بِمَآ أُنزِلَ إِلَيْهِ مِن رَّبِّهِۦ وَٱلْمُؤْمِنُونَ ۚ كُلٌّ ءَامَنَ بِٱللَّهِ وَمَلَٰٓئِكَتِهِۦ وَكُتُبِهِۦ وَرُسُلِهِۦ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّن رُّسُلِهِۦ ۚ وَقَالُوا۟ سَمِعْنَا وَأَطَعْنَا ۖ غُفْرَانَكَ رَبَّنَا وَإِلَيْكَ ٱلْمَصِيرُ
- (6:66) [next to 6:68] وَكَذَّبَ بِهِۦ قَوْمُكَ وَهُوَ ٱلْحَقُّ ۚ قُل لَّسْتُ عَلَيْكُم بِوَكِيلٍۢ
- (6:67) [next to 6:68] لِّكُلِّ نَبَإٍۢ مُّسْتَقَرٌّۭ ۚ وَسَوْفَ تَعْلَمُونَ
- (6:69) [next to 6:68] وَمَا عَلَى ٱلَّذِينَ يَتَّقُونَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَلَٰكِن ذِكْرَىٰ لَعَلَّهُمْ يَتَّقُونَ
- (6:70) [next to 6:68] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (17:104) [next to 17:106] وَقُلْنَا مِنۢ بَعْدِهِۦ لِبَنِىٓ إِسْرَٰٓءِيلَ ٱسْكُنُوا۟ ٱلْأَرْضَ فَإِذَا جَآءَ وَعْدُ ٱلْءَاخِرَةِ جِئْنَا بِكُمْ لَفِيفًۭا
- (17:105) [next to 17:106] وَبِٱلْحَقِّ أَنزَلْنَٰهُ وَبِٱلْحَقِّ نَزَلَ ۗ وَمَآ أَرْسَلْنَٰكَ إِلَّا مُبَشِّرًۭا وَنَذِيرًۭا
- (17:107) [next to 17:106] قُلْ ءَامِنُوا۟ بِهِۦٓ أَوْ لَا تُؤْمِنُوٓا۟ ۚ إِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مِن قَبْلِهِۦٓ إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًۭا
- (17:108) [next to 17:106] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
- (18:21) [next to 18:23] وَكَذَٰلِكَ أَعْثَرْنَا عَلَيْهِمْ لِيَعْلَمُوٓا۟ أَنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَأَنَّ ٱلسَّاعَةَ لَا رَيْبَ فِيهَآ إِذْ يَتَنَٰزَعُونَ بَيْنَهُمْ أَمْرَهُمْ ۖ فَقَالُوا۟ ٱبْنُوا۟ عَلَيْهِم بُنْيَٰنًۭا ۖ رَّبُّهُمْ أَعْلَمُ بِهِمْ ۚ قَالَ ٱلَّذِينَ غَلَبُوا۟ عَلَىٰٓ أَمْرِهِمْ لَنَتَّخِذَنَّ عَلَيْهِم مَّسْجِدًۭا
- (18:22) [next to 18:23] سَيَقُولُونَ ثَلَٰثَةٌۭ رَّابِعُهُمْ كَلْبُهُمْ وَيَقُولُونَ خَمْسَةٌۭ سَادِسُهُمْ كَلْبُهُمْ رَجْمًۢا بِٱلْغَيْبِ ۖ وَيَقُولُونَ سَبْعَةٌۭ وَثَامِنُهُمْ كَلْبُهُمْ ۚ قُل رَّبِّىٓ أَعْلَمُ بِعِدَّتِهِم مَّا يَعْلَمُهُمْ إِلَّا قَلِيلٌۭ ۗ فَلَا تُمَارِ فِيهِمْ إِلَّا مِرَآءًۭ ظَٰهِرًۭا وَلَا تَسْتَفْتِ فِيهِم مِّنْهُمْ أَحَدًۭا
- (18:25) [next to 18:23] وَلَبِثُوا۟ فِى كَهْفِهِمْ ثَلَٰثَ مِا۟ئَةٍۢ سِنِينَ وَٱزْدَادُوا۟ تِسْعًۭا
- (18:26) [next to 18:24] قُلِ ٱللَّهُ أَعْلَمُ بِمَا لَبِثُوا۟ ۖ لَهُۥ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَبْصِرْ بِهِۦ وَأَسْمِعْ ۚ مَا لَهُم مِّن دُونِهِۦ مِن وَلِىٍّۢ وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا
- (19:20) [next to 19:22] قَالَتْ أَنَّىٰ يَكُونُ لِى غُلَٰمٌۭ وَلَمْ يَمْسَسْنِى بَشَرٌۭ وَلَمْ أَكُ بَغِيًّۭا
- (19:21) [next to 19:22] قَالَ كَذَٰلِكِ قَالَ رَبُّكِ هُوَ عَلَىَّ هَيِّنٌۭ ۖ وَلِنَجْعَلَهُۥٓ ءَايَةًۭ لِّلنَّاسِ وَرَحْمَةًۭ مِّنَّا ۚ وَكَانَ أَمْرًۭا مَّقْضِيًّۭا
- (19:25) [next to 19:23] وَهُزِّىٓ إِلَيْكِ بِجِذْعِ ٱلنَّخْلَةِ تُسَٰقِطْ عَلَيْكِ رُطَبًۭا جَنِيًّۭا
- (19:26) [next to 19:24] فَكُلِى وَٱشْرَبِى وَقَرِّى عَيْنًۭا ۖ فَإِمَّا تَرَيِنَّ مِنَ ٱلْبَشَرِ أَحَدًۭا فَقُولِىٓ إِنِّى نَذَرْتُ لِلرَّحْمَٰنِ صَوْمًۭا فَلَنْ أُكَلِّمَ ٱلْيَوْمَ إِنسِيًّۭا
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:65) [next to 19:64] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (20:50) [next to 20:52] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (20:51) [next to 20:52] قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ
- (20:53) [next to 20:52] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
- (20:54) [next to 20:52] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:112) [next to 20:114] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا يَخَافُ ظُلْمًۭا وَلَا هَضْمًۭا
- (20:113) [next to 20:114] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
- (20:116) [next to 20:114] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ
- (20:117) [next to 20:115] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (20:123) [next to 20:125] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (20:124) [next to 20:125] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
- (20:127) [next to 20:125] وَكَذَٰلِكَ نَجْزِى مَنْ أَسْرَفَ وَلَمْ يُؤْمِنۢ بِـَٔايَٰتِ رَبِّهِۦ ۚ وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ
- (20:128) [next to 20:126] أَفَلَمْ يَهْدِ لَهُمْ كَمْ أَهْلَكْنَا قَبْلَهُم مِّنَ ٱلْقُرُونِ يَمْشُونَ فِى مَسَٰكِنِهِمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (25:30) [next to 25:32] وَقَالَ ٱلرَّسُولُ يَٰرَبِّ إِنَّ قَوْمِى ٱتَّخَذُوا۟ هَٰذَا ٱلْقُرْءَانَ مَهْجُورًۭا
- (25:31) [next to 25:32] وَكَذَٰلِكَ جَعَلْنَا لِكُلِّ نَبِىٍّ عَدُوًّۭا مِّنَ ٱلْمُجْرِمِينَ ۗ وَكَفَىٰ بِرَبِّكَ هَادِيًۭا وَنَصِيرًۭا
- (25:33) [next to 25:32] وَلَا يَأْتُونَكَ بِمَثَلٍ إِلَّا جِئْنَٰكَ بِٱلْحَقِّ وَأَحْسَنَ تَفْسِيرًا
- (25:34) [next to 25:32] ٱلَّذِينَ يُحْشَرُونَ عَلَىٰ وُجُوهِهِمْ إِلَىٰ جَهَنَّمَ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ سَبِيلًۭا
- (44:56) [next to 44:58] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
- (44:57) [next to 44:58] فَضْلًۭا مِّن رَّبِّكَ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (44:59) [next to 44:58] فَٱرْتَقِبْ إِنَّهُم مُّرْتَقِبُونَ
- (54:15) [next to 54:17] وَلَقَد تَّرَكْنَٰهَآ ءَايَةًۭ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:16) [next to 54:17] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:18) [next to 54:17] كَذَّبَتْ عَادٌۭ فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:19) [next to 54:17] إِنَّآ أَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا فِى يَوْمِ نَحْسٍۢ مُّسْتَمِرٍّۢ
- (73:2) [next to 73:4] قُمِ ٱلَّيْلَ إِلَّا قَلِيلًۭا
- (73:3) [next to 73:4] نِّصْفَهُۥٓ أَوِ ٱنقُصْ مِنْهُ قَلِيلًا
- (73:6) [next to 73:4] إِنَّ نَاشِئَةَ ٱلَّيْلِ هِىَ أَشَدُّ وَطْـًۭٔا وَأَقْوَمُ قِيلًا
- (73:18) [next to 73:20] ٱلسَّمَآءُ مُنفَطِرٌۢ بِهِۦ ۚ كَانَ وَعْدُهُۥ مَفْعُولًا
- (73:19) [next to 73:20] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (75:14) [next to 75:16] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
- (75:15) [next to 75:16] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
- (75:20) [next to 75:18] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
- (75:21) [next to 75:19] وَتَذَرُونَ ٱلْءَاخِرَةَ
- (96:0) [next to 96:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (96:2) [next to 96:1] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- (96:6) [next to 96:5] كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- (96:7) [next to 96:5] أَن رَّءَاهُ ٱسْتَغْنَىٰٓ

