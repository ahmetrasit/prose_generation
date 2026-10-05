Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:14; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_14/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_14.reading.tr.md (prose paragraphs numbered) =====
## Dört kelimelik bir hüküm

[¶1] On dördüncü ayet dört kelimeden oluşur: {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kişi kurtuluşa ermiştir, source:87:14}. İlk kelime kad, geçmiş zamanlı bir fiilin önüne gelince o işi olmuş ve kesinleşmiş olarak sunar. Bu yüzden ayet bir umut ya da vaat cümlesi gibi durmaz, verilmiş bir hüküm gibi durur. Kurtuluş ileride beklenen bir şey olarak anlatılmaz, gerçekleşmiş olarak ilan edilir. Hemen önceki ayetler ateşin içinde ne ölen ne yaşayan bir kişiyi anlatırken geleceği konuşuyordu. On dördüncü ayet aynı gelecekteki sonucu geçmiş zamanla söyler ve onu kapanmış bir hesap gibi gösterir.

[¶2] İkinci kelime men, "kim ki" demektir. Ayet bir isim, bir soy ya da bir zümre saymaz, kurtuluşu bir eyleme bağlar. Arınan kim olursa olsun bu cümlenin öznesidir.

[¶3] Üçüncüsü fiilin kalıbıdır. tezekkâ, "arıttı" anlamındaki zekkâ fiilinin, kişinin işi kendi üzerinde ve kendisi için yaptığını anlatan biçimidir: "arındı, kendini arıttı, arınmayı üstlendi". Bu kalıp çoğu zaman bir anda olan bir şeyi değil, emekle ve adım adım kazanılan bir hali anlatır. Aynı kalıp surenin onuncu ayetinde de vardır: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:seyeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10}. İki ayet aynı biçimde kurulmuştur: önce men gelir, ardından kişinin kendi içinde yaptığı bir iş. Onuncu ayet öğüdün kime ulaşacağını söyler, on dördüncü ayet de o öğüdü alanın nereye vardığını. Aradaki ayetler öğütten kaçanın yolunu anlatır: {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ondan uzak durur, source:87:11}. On dördüncü ayet ise "ve" bağlacı olmadan, ani bir dönüşle gelir ve iki yolun ikincisini tek cümlede bitirir.

[¶4] Cümle on beşinci ayetle tamamlanır: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını andı ve namaz kıldı, source:87:15}. "Rabbinin adı" sözü surenin ilk emrini geri getirir: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Surenin başında verilen emri yerine getiren kişi, on dördüncü ve on beşinci ayetlerde tarif edilen kişidir. Arınma da bu anmanın ve namazın önünde durur.

## Toprağı yaran kelime

[¶5] eflaha fiilinin kökü ف ل ح'nin en somut anlamı yarmaktır. Araplar toprağı sürmeyi bu fiille söylerdi: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda şakaktuhâ, gloss:toprağı sürdüm, yani yardım, source:"ف ل ح,B001"}. Toprağı yaran kişi de adını bu işten alır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye toprağı yardığı için fellâh denmiştir, source:"ف ل ح,B003"}. Bu imge ve sonra gelecek imgeler, kelimenin bu ayetteki anlamının yerine geçmez. eflaha burada "kurtuluşa erdi" demektir. Tarla bu anlamın arkasında, onunla birlikte duyulan bir sestir.

[¶6] Sabanın işi şudur. Güneşte kabuk bağlamış toprağa serpilen tohum kök salamaz, yağan su da yüzeyden akıp gider. Saban toprağı keserek bir iz açar. Açılan yerden su ve hava içeri girer, tohum toprağın içine kapanır ve tutunur. Ürün bu yarıktan çıkar. Sert olanın ancak sert olanla açılabileceğini söyleyen bir deyim de aynı fiili kullanır: {ar:الحديد بالحديد يفلح أي يشق أو يقطع, tr:el-hadîdu bi'l-hadîdi yuflah, ey yuşakku ev yuktau, gloss:demir demirle yarılır, yani kesilir, source:"ف ل ح,B001"}. Kurtuluş kelimesinin bu toprak ve demir anlamıyla aynı kökte durması, kurtuluşu direnen bir yüzeyi açmaya yakın bir iş olarak düşündürür. Bu bir yorumdur: Arapça iki anlamı aynı kökte taşır, ama birinin öbüründen doğduğunu söylemez.

[¶7] Türkçede bu kelimenin iki ucu birbirinden kopmuştur. "Fellah" yalnızca köylü, rençper demektir. "İflah" ise neredeyse sadece "iflah olmaz" deyiminde, olumsuz yanıyla ve düzelmesi umulmayan kişi için yaşar. Arapçada aynı kelime hem sabanı süren eli hem de bir ömrün varacağı kurtuluşu adlandırır.

[¶8] Kur'an da toprağın yarılmasını yiyeceğin başlangıcı olarak anlatır. Abese suresinde Allah insanı kendi yemeğine bakmaya çağırır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}. Ardından suyun dökülüşünü anlatır, sonra {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:ŝumme şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26} der, sonra da {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Toprağı sürmeyi tanımlayan yarma fiili burada Allah'ın işi olarak geçer.

[¶9] Ayetin ikinci fiili de aynı tarlada durur. zekâ, ekinin büyüyüp gelişmesini anlatır: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen, izdâde ve nemâ, gloss:ekin büyüdü, arttı ve gelişti, source:"ز ك و,B001"}. Böylece dört kelimelik cümlenin iki fiilinden biri toprağı açmayı, öbürü ekinin büyümesini adlandırır. Surenin dördüncü ve beşinci ayetlerinde çıkarılıp kara bir çer çöpe dönen otlak, bu işlenmiş tarlanın karşısında durur.

## İyilik içinde kalmak

[¶10] ف ل ح kökünün ikinci büyük anlamı kalıcılıktır. Kelime şöyle tanımlanırdı: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh iyilik içinde kalıcı olmaktır, source:"ف ل ح,B005"}. Bir başka tanıma göre {ar:الفلاح الفوز والنجاة والبقاء, tr:el-felâhu el-fevzu ve'n-necâtu ve'l-bekâ, gloss:felâh kazanmak, kurtulmak ve kalıcı olmaktır, source:"ف ل ح,B005"}. Aradığını bulan kişi için de {ar:أفلح وأنجح إذا أدرك مطلوبه, tr:eflaha ve encaha iẕâ edreke matlûbeh, gloss:aradığına erişince eflaha ve encaha denir, source:"ف ل ح,B005"} derlerdi. Türkçedeki "kurtuluş" kelimesi bir tehlikeden kaçmayı öne çıkarır. Arapçadaki felâh ise kaçmaktan çok bir yere varmayı ve varılan iyilikte kalmayı söyler.

[¶11] Bu tanım on dördüncü ayeti bir önceki ayetin tam karşısına koyar. Ateşe giren kişi için şöyle denmişti: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. Bu da bir tür kalmaktır: bitmeyen ama hayat da olmayan bir sürüp gitme. On dördüncü ayetin fiili ise iyiliğin içinde kalmayı adlandırır. İki son da bir devamı anlatır. Aralarındaki fark, devam edenin iyilik olup olmamasıdır.

[¶12] Aynı kök sahur yemeğine de ad olmuştur: {ar:الفلاح السحور, tr:el-felâhu es-sehûr, gloss:felâh sahur yemeğidir, source:"ف ل ح,B006"}. Gerekçesi açıktır: {ar:لأن به بقاء الصوم, tr:li-enne bihî bekâe's-savm, gloss:çünkü orucun sürmesi onunla olur, source:"ف ل ح,B006"}. Oruç tutan kişi şafaktan önce yer. O yemek gün boyu onunla kalır ve akşama kadar ayakta durmasını sağlar. Bu küçük kullanım felâhın ne tür bir şey olduğunu gösterir: günün sonuna kadar taşıyan, tükenmeyen bir azık.

[¶13] Sure bu tanımın iki kelimesini birkaç ayet sonra yan yana getirir: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Felâhın tanımı "iyilik içinde kalıcılık", on yedinci ayetin ölçüsü ise "daha hayırlı ve daha kalıcı"dır. ebkâ başka bir kökten gelir. İki ayeti bağlayan şey kök birliği değil, felâhın kendi tanımında taşıdığı anlamdır. Bu bağ duyulunca on dördüncü ve on yedinci ayetler aynı iddiayı iki taraftan söyler: kurtuluşa eren kişi, on yedinci ayetin kalıcı dediği şeyi seçmiştir. Aradaki on altıncı ayet ise insanların bu seçimi çoğu zaman tersine yaptığını söyler: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:ama siz yakın hayatı öne alıyorsunuz, source:87:16}.

## Büyüyen, arınan, veren

[¶14] tezekkâ fiilinin kökü ز ك و'nün temelinde büyüme vardır: {ar:أصل يدل على نماء وزيادة, tr:aslun yedullu alâ nemâin ve ziyâde, gloss:büyüme ve artış bildiren bir köktür, source:"ز ك و,B001"}. Aynı kök ahlaki temizliği ve düzgünlüğü de anlatır: {ar:والزكاة الصلاح, tr:ve'z-zekâtu es-salâh, gloss:zekât düzgünlük ve iyiliktir, source:"ز ك و,B002"}. Temiz ve kötülükten sakınan kişi için {ar:رجل زكي تقي, tr:raculun zekiyyun takiyy, gloss:arı ve sakınan adam, source:"ز ك و,B002"} denir. Kök ayrıca malın yoksula verilen payını adlandırır, aynı fiil de vermek anlamına gelir: {ar:وتزكى أي تصدق, tr:ve tezekkâ ey tesaddaka, gloss:tezekkâ, sadaka verdi demektir, source:"ز ك و,B003"}.

[¶15] Türkçede "zekât" yalnızca dinen belirlenmiş mal payının adıdır. Arapçada ise kelime büyümeyi ve temizliği de içinde taşır. Verilen paya neden bu adın verildiği de açıkça söylenir: {ar:زكاة لأنها طهارة, tr:zekâtun li-ennehâ tahâra, gloss:temizlik olduğu için zekât denmiştir, source:"ز ك و,B002"}. Malın bir kısmını vermek sayıyı azaltır, ama kelime bu azalmayı büyüme diye adlandırır: {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti en-nemuvvu'l-hâsılu an bereketi'llâhi teâlâ, gloss:zekâtın aslı, Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}.

[¶16] Kur'an bu ters hesabı açıkça yapar. Rûm suresinde Allah iki türlü vermeyi karşılaştırır: insanların mallarında artsın diye verilen faiz ile Allah'ın rızası istenerek verilen zekât. {ar:وَمَآ ءَاتَيْتُم مِّن رِّبًۭا لِّيَرْبُوَا۟ فِىٓ أَمْوَٰلِ ٱلنَّاسِ فَلَا يَرْبُوا۟ عِندَ ٱللَّهِ ۖ وَمَآ ءَاتَيْتُم مِّن زَكَوٰةٍۢ تُرِيدُونَ وَجْهَ ٱللَّهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُضْعِفُونَ, tr:ve mâ âteytum min ribâen li-yerbuve fî emvâli'n-nâsi fe-lâ yerbû inda'llâh, ve mâ âteytum min zekâtin turîdûne vechallâhi fe-ulâike humu'l-mud'ifûn, gloss:insanların mallarında artsın diye faizle verdiğiniz Allah katında artmaz; Allah'ın rızasını isteyerek verdiğiniz zekâta gelince, işte katlayanlar onlardır, source:30:39}. Faiz de "artmak" fiiliyle anılır, zekât da büyüme adını taşır. Ama ayet gerçek artışı, görünürde eksilten vermeye bağlar.

[¶17] Bu yüzden on dördüncü ayetteki tezekkâ hem "arındı" hem "verdi" hem de "büyüdü" diye duyulabilir. Fiilin nesnesi yoktur ve ayet anlamı daraltmaz. Kur'an aynı fiili açıkça mal vermek için de kullanır. Leyl suresinde ateşten uzak tutulacak kişi şöyle tarif edilir: {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:elleẕî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18}. On beşinci ayetteki namazla birlikte okununca, surede Kur'an'ın sık sık yan yana getirdiği bir çift belirir. Mü'minûn suresi {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad eflaha'l-mu'minûn, gloss:müminler kurtuluşa ermiştir, source:23:1} diye açılır. Kurtuluşa erenleri sayarken önce {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:elleẕîne hum fî salâtihim hâşi'ûn, gloss:namazlarında saygıyla eğilenler, source:23:2} der, sonra {ar:وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ, tr:velleẕîne hum li'z-zekâti fâ'ilûn, gloss:zekâtı yerine getirenler, source:23:4}. Orada namaz önce gelir. On dördüncü ve on beşinci ayetlerde ise arınma namazın önüne geçmiştir.

[¶18] Arınma ile büyümenin aynı kelimede durması bir şey daha söyler. Arınma burada yalnızca bir şeyi çıkarıp atmak değildir, ekinin büyümesine benzeyen bir gelişmedir. Kişinin kendini arıtması, kendinden bir şey eksiltmek kadar kendini düzgün ve verimli kılmaktır.

## Kendini arı saymak ile arınmak

[¶19] Türkçede "tezkiye" daha çok birinin iyi hal sahibi olduğuna tanıklık etmek, onu sözle temize çıkarmak anlamında kullanılır. Arapçada da bu kökün, birini ya da kendini sözle temiz sayma anlamında bir kullanımı vardır {source:"ز ك و,B002"}. Kur'an bunu insanın kendisi için yasaklar. Necm suresinde Allah büyük günahlardan kaçınanları anlatır. Ardından insanları topraktan var ettiği zamandan ve anne karnında cenin oldukları zamandan beri onları en iyi bildiğini söyler ve şöyle der: {ar:فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ, tr:fe-lâ tuzekkû enfusekum, huve a'lemu bi-meni't-tekâ, gloss:kendinizi temize çıkarmayın; kimin sakındığını O daha iyi bilir, source:53:32}. Nisâ suresinde de şöyle denir: {ar:أَلَمْ تَرَ إِلَى ٱلَّذِينَ يُزَكُّونَ أَنفُسَهُم ۚ بَلِ ٱللَّهُ يُزَكِّى مَن يَشَآءُ, tr:elem tera ile'lleẕîne yuzekkûne enfusehum, beli'llâhu yuzekkî men yeşâ', gloss:kendilerini temize çıkaranları görmedin mi? Hayır, Allah dilediğini arıtır, source:4:49}.

[¶20] Demek ki aynı kök hem övülen hem yerilen bir işi adlandırır. Fark fiilin biçiminde ve yönündedir. tuzekkû enfusekum, kendini temiz diye ilan etmektir. tezekkâ ise temizliği bir iş olarak üstlenmektir. Biri sözle verilen bir hükümdür, öbürü emekle kazanılan bir hal. On dördüncü ayet de kişinin kendisi hakkındaki hükmünü değil, Allah'ın onun hakkındaki hükmünü bildirir. kad eflaha diyen, arınan kişinin kendisi değildir.

[¶21] Kur'an arınmayı yalnızca insana da bırakmaz. Nûr suresinde müminlere şeytanın adımlarına uymamaları söylendikten sonra şöyle denir: {ar:وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ مَا زَكَىٰ مِنكُم مِّنْ أَحَدٍ أَبَدًۭا, tr:ve lev lâ fadlu'llâhi aleykum ve rahmetuhû mâ zekâ minkum min ehadin ebedâ, gloss:Allah'ın size lütfu ve rahmeti olmasaydı içinizden hiç kimse asla arınamazdı, source:24:21}. Cuma suresinde Allah, ümmîler arasından gönderdiği elçiyi onlara ayetlerini okuyan ve {ar:وَيُزَكِّيهِمْ, tr:ve yuzekkîhim, gloss:onları arıtan, source:62:2} biri olarak tanıtır. Arınma insanın fiili, elçinin işi ve Allah'ın lütfu olarak üç yerden birden anlatılır. Bu surede de insanın fiillerinden önce Rabbin fiilleri gelir: ikinci ve üçüncü ayetlerde O yaratır, düzene koyar, ölçer ve yol gösterir {source:87:2} {source:87:3}. Elçiye de {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana kolayca eriştireceğiz, source:87:8} denir. Kişinin kendini arıtması, bu hazırlanmış zeminin üzerinde yapılan bir iştir.

## Öğüdü alan

[¶22] tezekkâ Kur'an'da pek tek başına durmaz. Çoğu zaman öğüt almak ve içi titremekle birlikte gelir. Abese suresi şöyle açılır: {ar:عَبَسَ وَتَوَلَّىٰٓ, tr:abese ve tevellâ, gloss:yüzünü ekşitti ve döndü, source:80:1}, {ar:أَن جَآءَهُ ٱلْأَعْمَىٰ, tr:en câehu'l-a'mâ, gloss:kendisine kör adam geldi diye, source:80:2}. Sonra söz yüzünü çevirene döner: {ar:وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ, tr:ve mâ yudrîke le'allehû yezzekkâ, gloss:ne bilirsin, belki o arınacaktı, source:80:3}, {ar:أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ, tr:ev yeẕẕekkeru fe-tenfeahu'ẕ-ẕikrâ, gloss:ya da öğüt alacaktı da öğüt ona yarayacaktı, source:80:4}. Kendini yeterli görene yönelindiği söylenir ve {ar:وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ, tr:ve mâ aleyke ellâ yezzekkâ, gloss:onun arınmamasından sen sorumlu değilsin, source:80:7} denir. Koşarak gelen için ise {ar:وَهُوَ يَخْشَىٰ, tr:ve huve yahşâ, gloss:o içi titreyerek gelmişti, source:80:9} denir. Bu birkaç ayette surenin dokuzuncu ve onuncu ayetlerindeki kelimeler neredeyse aynen yer alır: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt yarar sağlıyorsa, source:87:9}, ardından da öğüt alan ve içi titreyen kişi. Abese'de arınma, öğüdün yaradığı kişinin varacağı yer olarak anılır. Öğüt verenin elinde olan bir şey değildir.

[¶23] Fâtır suresinde aynı kelimeler bir araya gelir. Hiç kimsenin başkasının yükünü taşımayacağı söylendikten sonra elçiye şöyle denir: {ar:إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ, tr:innemâ tunẕiru'lleẕîne yahşevne rabbehum bi'l-ğaybi ve ekâmu's-salâh, ve men tezekkâ fe-innemâ yetezekkâ li-nefsih, gloss:sen ancak Rablerinden görmeden içleri titreyenleri ve namazı dosdoğru kılanları uyarabilirsin; kim arınırsa ancak kendisi için arınır, source:35:18}. Bu ayette içi titremek, namaz ve arınma birlikte geçer. Bu üçü, surenin onuncu, on dördüncü ve on beşinci ayetlerinin taşıdığı işlerdir. Arınmanın kazancı da arınana aittir, tıpkı yükün başkasına geçmemesi gibi.

[¶24] Musa'ya verilen görevde de aynı sıra vardır. Nâziât suresinde Allah Musa'ya, azgınlaşan Firavun'a gitmesini ve ona şöyle demesini söyler: {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:de ki: arınmaya bir yönelişin var mı, source:79:18}, {ar:وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ, tr:ve ehdiyeke ilâ rabbike fe-tahşâ, gloss:seni Rabbine yönelteyim de içini saygı kaplasın, source:79:19}. Firavun'a sunulan şey bir davettir, arınma ise onun kendi fiili olarak kalır. Firavun yalanlar ve sonunda {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}.

[¶25] Surede ẕekkir, eẕ-ẕikrâ, yeẕẕekkeru, tezekkâ ve ẕekera kelimeleri arka arkaya gelir. Anmayı ve öğüdü anlatan ذ ك ر ile arınmayı ve büyümeyi anlatan ز ك و ayrı köklerdir, aralarında kök birliği yoktur. Ama kulağa yakın gelirler ve sure onları aynı yola dizer: öğüt verilir, öğüt alınır, kişi arınır ve Rabbinin adını anar. Bu ses yakınlığı bir benzerliktir, anlam için kanıt değildir. Yine de surenin akışında öğüt ile arınmanın bu kadar yakın durduğu duyulur.

## Kurtuluşun iki tanımı

[¶26] kad eflaha kalıbı Kur'an'da tekrar eden bir hüküm biçimidir ve bazen karşıtıyla birlikte söylenir. Şems suresinde Allah güneşe, aya, gündüze, geceye, göğe ve yere yemin ettikten sonra cana yemin eder: {ar:وَنَفْسٍۢ وَمَا سَوَّىٰهَا, tr:ve nefsin ve mâ sevvâhâ, gloss:cana ve onu düzene koyana, source:91:7}, {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona yoldan çıkışını da sakınışını da bildirene, source:91:8}. Sonra hüküm gelir: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad eflaha men zekkâhâ, gloss:onu arıtan kurtuluşa ermiştir, source:91:9}, {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp örten ise eli boş kalmıştır, source:91:10}. Buradaki düzene koyma fiili, surenin ikinci ayetindeki fiilin aynısıdır: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}. Canı biçimlendiren Rabdir, onu arıtmak ise insana kalır. Şems'te fiil canı nesne alır: "onu arıttı". On dördüncü ayette ise dönüşlü biçimdedir: "arındı". Aynı iş iki yerde iki açıdan söylenir. Birinde kişi canı üzerinde çalışır, öbüründe kişinin kendisi bu işin içinde değişir. Arıtmanın karşıtı olarak gömüp örtmenin seçilmesi de tarlayı yeniden hatırlatır: büyüyen ekinin karşısında, toprağın altına bastırılıp boğulan bir şey durur.

[¶27] Leyl suresi, on birinci ve on ikinci ayetlerin kelimeleriyle aynı sahneyi ters yönden kurar. Allah alevlenen bir ateşle uyardığını söyler ve şöyle der: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve seyucennebuhe'l-etkâ, gloss:en çok sakınan ondan uzak tutulacaktır, source:92:17}. Uzak tutulan kişi, malını verip arınandır. Bu surede en bedbaht öğütten uzak durur {source:87:11} ve ateşe girer. Leyl'de ise arınan ateşten uzak tutulur. Uzak durma fiili iki surede iki ayrı şeye yönelir: biri öğütten kaçar, öbürü ateşten korunur.

[¶28] Kalıbın en şaşırtıcı kullanımı Musa'nın hikâyesindedir. Orada kurtuluşun tanımı aynı kalıp içinde değişir. Firavun hilesini toplayıp gelir. Musa karşısındakileri uyarır ve {ar:وَقَدْ خَابَ مَنِ ٱفْتَرَىٰ, tr:ve kad hâbe meni'fterâ, gloss:yalan uyduran eli boş kalmıştır, source:20:61} der. Onlar kendi aralarında tartışıp fısıldaşır ve şu sonuca varır: {ar:وَقَدْ أَفْلَحَ ٱلْيَوْمَ مَنِ ٱسْتَعْلَىٰ, tr:ve kad eflaha'l-yevme meni'ste'lâ, gloss:bugün üstün gelen kurtuluşa ermiştir, source:20:64}. Şems'te bir arada söylenen iki hüküm burada iki ağza bölünmüştür: eli boş kalanı Musa tarif eder, kurtuluşa ereni karşı taraf. Onların tarifinde felâh, bugün başkalarının üstüne çıkmaktır. Allah ise Musa'ya {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma dedik, üstün olan sensin, source:20:68} der. Sihirbazlar secdeye kapanır. Firavun'un tehditlerine verdikleri cevapla başlayan konuşma, cennet bahçeleri anılarak şu cümleyle kapanır: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu, arınanın karşılığıdır, source:20:76}. Hikâyenin başında kurtuluşa eren "üstün gelen" diye tanımlanmıştı. Sonunda kurtuluşa eren "arınan" olur.

[¶29] On dördüncü ayet bu ikinci tanımı kullanır. Surenin açılışında yücelik Rabbe verilmiştir {source:87:1}. Kurtuluşun ölçüsü üstün gelmek değil, arınmaktır. "Bugün" de ölçü değildir, çünkü on yedinci ayet daha kalıcı olanı öne koyar. On üçüncü ve on yedinci ayetlerin kelimelerinin bu hikâyede birlikte söylenmesi, son ayetin Musa'nın sayfalarını anmasıyla birleşerek surenin ortak sahnesini kurar {source:87:19}.

===== _commentary/v16/out/87_14/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: qad + perfect verb marks a realized, certain fact
- memory: tafa''ul form tazakkâ is the reflexive/effortful counterpart of zakkâ
- memory: yazzakkâ and yadhdhakkaru are assimilated forms of yatazakkâ and yatadhakkaru
- memory: dassâhâ means buried/concealed it
- memory: Turkish usage of "fellah", "iflah olmaz", "zekât", "tezkiye"
- not written: ف ل ح B002 split lip - no work in any theme
- not written: ف ل ح B004 hired carrier likened to farmer - no theme
- not written: ف ل ح B007 dressing up a sale, deceit - a link to the near life in ayah sixteen has no ground
- not written: ز ك و B004 "does not befit" - fixed expression, no theme
- not written: ز ك و B005 even/pair, odd-even game - too weak against the surah's twofold division
- not written: field scene with خرج, ربب, بقي - belongs to the surah commentary, only recalled
- not written: 48:29, 56:63-65, 42:20, 6:141 - support the shared field scene, not this ayah's own words
- not written: who speaks in 20:74-76 - left open, the Quran text does not say outright

===== passages not cited (179) =====
## strong (this ayah's own list) (5)

- (23:1) [listed for 87:14] [cited in ¶17] قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ
- (30:39) [listed for 87:14] [cited in ¶16] وَمَآ ءَاتَيْتُم مِّن رِّبًۭا لِّيَرْبُوَا۟ فِىٓ أَمْوَٰلِ ٱلنَّاسِ فَلَا يَرْبُوا۟ عِندَ ٱللَّهِ ۖ وَمَآ ءَاتَيْتُم مِّن زَكَوٰةٍۢ تُرِيدُونَ وَجْهَ ٱللَّهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُضْعِفُونَ
- (79:18) [listed for 87:14] [cited in ¶24] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
- (91:9) [listed for 87:14] [cited in ¶26] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- (91:10) [listed for 87:14] [cited in ¶26] وَقَدْ خَابَ مَن دَسَّىٰهَا

## medium (this ayah's own list) (27)

- (2:129) [listed for 87:14] رَبَّنَا وَٱبْعَثْ فِيهِمْ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِكَ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُزَكِّيهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (2:151) [listed for 87:14] كَمَآ أَرْسَلْنَا فِيكُمْ رَسُولًۭا مِّنكُمْ يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِنَا وَيُزَكِّيكُمْ وَيُعَلِّمُكُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (2:222) [listed for 87:14] وَيَسْـَٔلُونَكَ عَنِ ٱلْمَحِيضِ ۖ قُلْ هُوَ أَذًۭى فَٱعْتَزِلُوا۟ ٱلنِّسَآءَ فِى ٱلْمَحِيضِ ۖ وَلَا تَقْرَبُوهُنَّ حَتَّىٰ يَطْهُرْنَ ۖ فَإِذَا تَطَهَّرْنَ فَأْتُوهُنَّ مِنْ حَيْثُ أَمَرَكُمُ ٱللَّهُ ۚ إِنَّ ٱللَّهَ يُحِبُّ ٱلتَّوَّٰبِينَ وَيُحِبُّ ٱلْمُتَطَهِّرِينَ
- (3:77) [listed for 87:14] إِنَّ ٱلَّذِينَ يَشْتَرُونَ بِعَهْدِ ٱللَّهِ وَأَيْمَٰنِهِمْ ثَمَنًۭا قَلِيلًا أُو۟لَٰٓئِكَ لَا خَلَٰقَ لَهُمْ فِى ٱلْءَاخِرَةِ وَلَا يُكَلِّمُهُمُ ٱللَّهُ وَلَا يَنظُرُ إِلَيْهِمْ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- (4:49) [listed for 87:14] [cited in ¶19] أَلَمْ تَرَ إِلَى ٱلَّذِينَ يُزَكُّونَ أَنفُسَهُم ۚ بَلِ ٱللَّهُ يُزَكِّى مَن يَشَآءُ وَلَا يُظْلَمُونَ فَتِيلًا
- (5:90) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
- (5:100) [listed for 87:14] قُل لَّا يَسْتَوِى ٱلْخَبِيثُ وَٱلطَّيِّبُ وَلَوْ أَعْجَبَكَ كَثْرَةُ ٱلْخَبِيثِ ۚ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تُفْلِحُونَ
- (6:21) [listed for 87:14] وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ كَذَّبَ بِـَٔايَٰتِهِۦٓ ۗ إِنَّهُۥ لَا يُفْلِحُ ٱلظَّٰلِمُونَ
- (7:8) [listed for 87:14] وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (9:103) [listed for 87:14] خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
- (12:23) [listed for 87:14] وَرَٰوَدَتْهُ ٱلَّتِى هُوَ فِى بَيْتِهَا عَن نَّفْسِهِۦ وَغَلَّقَتِ ٱلْأَبْوَٰبَ وَقَالَتْ هَيْتَ لَكَ ۚ قَالَ مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ ۖ إِنَّهُۥ لَا يُفْلِحُ ٱلظَّٰلِمُونَ
- (16:116) [listed for 87:14] وَلَا تَقُولُوا۟ لِمَا تَصِفُ أَلْسِنَتُكُمُ ٱلْكَذِبَ هَٰذَا حَلَٰلٌۭ وَهَٰذَا حَرَامٌۭ لِّتَفْتَرُوا۟ عَلَى ٱللَّهِ ٱلْكَذِبَ ۚ إِنَّ ٱلَّذِينَ يَفْتَرُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ لَا يُفْلِحُونَ
- (19:19) [listed for 87:14] قَالَ إِنَّمَآ أَنَا۠ رَسُولُ رَبِّكِ لِأَهَبَ لَكِ غُلَٰمًۭا زَكِيًّۭا
- (20:76) [listed for 87:14] [cited in ¶28] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
- (23:4) [listed for 87:14] [cited in ¶17] وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ
- (23:102) [listed for 87:14] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (24:21) [listed for 87:14] [cited in ¶21] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ وَمَن يَتَّبِعْ خُطُوَٰتِ ٱلشَّيْطَٰنِ فَإِنَّهُۥ يَأْمُرُ بِٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۚ وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ مَا زَكَىٰ مِنكُم مِّنْ أَحَدٍ أَبَدًۭا وَلَٰكِنَّ ٱللَّهَ يُزَكِّى مَن يَشَآءُ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- (24:28) [listed for 87:14] فَإِن لَّمْ تَجِدُوا۟ فِيهَآ أَحَدًۭا فَلَا تَدْخُلُوهَا حَتَّىٰ يُؤْذَنَ لَكُمْ ۖ وَإِن قِيلَ لَكُمُ ٱرْجِعُوا۟ فَٱرْجِعُوا۟ ۖ هُوَ أَزْكَىٰ لَكُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (30:38) [listed for 87:14] فَـَٔاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ ۚ ذَٰلِكَ خَيْرٌۭ لِّلَّذِينَ يُرِيدُونَ وَجْهَ ٱللَّهِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (31:5) [listed for 87:14] أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (35:18) [listed for 87:14] [cited in ¶23] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (53:32) [listed for 87:14] [cited in ¶19] ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ إِلَّا ٱللَّمَمَ ۚ إِنَّ رَبَّكَ وَٰسِعُ ٱلْمَغْفِرَةِ ۚ هُوَ أَعْلَمُ بِكُمْ إِذْ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ ۖ فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ
- (62:10) [listed for 87:14] فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
- (80:3) [listed for 87:14] [cited in ¶22] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
- (80:7) [listed for 87:14] [cited in ¶22] وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ
- (92:18) [listed for 87:14] [cited in ¶17] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- (98:5) [listed for 87:14] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ

## named by the passage's own list as strong for this ayah (11)

- (7:156) [listed for 87:14] ۞ وَٱكْتُبْ لَنَا فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ إِنَّا هُدْنَآ إِلَيْكَ ۚ قَالَ عَذَابِىٓ أُصِيبُ بِهِۦ مَنْ أَشَآءُ ۖ وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ ۚ فَسَأَكْتُبُهَا لِلَّذِينَ يَتَّقُونَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَٱلَّذِينَ هُم بِـَٔايَٰتِنَا يُؤْمِنُونَ
- (9:112) [listed for 87:14] ٱلتَّٰٓئِبُونَ ٱلْعَٰبِدُونَ ٱلْحَٰمِدُونَ ٱلسَّٰٓئِحُونَ ٱلرَّٰكِعُونَ ٱلسَّٰجِدُونَ ٱلْءَامِرُونَ بِٱلْمَعْرُوفِ وَٱلنَّاهُونَ عَنِ ٱلْمُنكَرِ وَٱلْحَٰفِظُونَ لِحُدُودِ ٱللَّهِ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (12:53) [listed for 87:14] ۞ وَمَآ أُبَرِّئُ نَفْسِىٓ ۚ إِنَّ ٱلنَّفْسَ لَأَمَّارَةٌۢ بِٱلسُّوٓءِ إِلَّا مَا رَحِمَ رَبِّىٓ ۚ إِنَّ رَبِّى غَفُورٌۭ رَّحِيمٌۭ
- (19:13) [listed for 87:14] وَحَنَانًۭا مِّن لَّدُنَّا وَزَكَوٰةًۭ ۖ وَكَانَ تَقِيًّۭا
- (22:77) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱرْكَعُوا۟ وَٱسْجُدُوا۟ وَٱعْبُدُوا۟ رَبَّكُمْ وَٱفْعَلُوا۟ ٱلْخَيْرَ لَعَلَّكُمْ تُفْلِحُونَ ۩
- (23:60) [listed for 87:14] وَٱلَّذِينَ يُؤْتُونَ مَآ ءَاتَوا۟ وَّقُلُوبُهُمْ وَجِلَةٌ أَنَّهُمْ إِلَىٰ رَبِّهِمْ رَٰجِعُونَ
- (23:111) [listed for 87:14] إِنِّى جَزَيْتُهُمُ ٱلْيَوْمَ بِمَا صَبَرُوٓا۟ أَنَّهُمْ هُمُ ٱلْفَآئِزُونَ
- (24:37) [listed for 87:14] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
- (33:33) [listed for 87:14] وَقَرْنَ فِى بُيُوتِكُنَّ وَلَا تَبَرَّجْنَ تَبَرُّجَ ٱلْجَٰهِلِيَّةِ ٱلْأُولَىٰ ۖ وَأَقِمْنَ ٱلصَّلَوٰةَ وَءَاتِينَ ٱلزَّكَوٰةَ وَأَطِعْنَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ إِنَّمَا يُرِيدُ ٱللَّهُ لِيُذْهِبَ عَنكُمُ ٱلرِّجْسَ أَهْلَ ٱلْبَيْتِ وَيُطَهِّرَكُمْ تَطْهِيرًۭا
- (63:9) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (92:20) [listed for 87:14] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ

## named by the passage's own list as medium for this ayah (29)

- (2:43) [listed for 87:14] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ
- (2:174) [listed for 87:14] إِنَّ ٱلَّذِينَ يَكْتُمُونَ مَآ أَنزَلَ ٱللَّهُ مِنَ ٱلْكِتَٰبِ وَيَشْتَرُونَ بِهِۦ ثَمَنًۭا قَلِيلًا ۙ أُو۟لَٰٓئِكَ مَا يَأْكُلُونَ فِى بُطُونِهِمْ إِلَّا ٱلنَّارَ وَلَا يُكَلِّمُهُمُ ٱللَّهُ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ
- (2:200) [listed for 87:14] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
- (3:42) [listed for 87:14] وَإِذْ قَالَتِ ٱلْمَلَٰٓئِكَةُ يَٰمَرْيَمُ إِنَّ ٱللَّهَ ٱصْطَفَىٰكِ وَطَهَّرَكِ وَٱصْطَفَىٰكِ عَلَىٰ نِسَآءِ ٱلْعَٰلَمِينَ
- (5:35) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَٱبْتَغُوٓا۟ إِلَيْهِ ٱلْوَسِيلَةَ وَجَٰهِدُوا۟ فِى سَبِيلِهِۦ لَعَلَّكُمْ تُفْلِحُونَ
- (9:18) [listed for 87:14] إِنَّمَا يَعْمُرُ مَسَٰجِدَ ٱللَّهِ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَلَمْ يَخْشَ إِلَّا ٱللَّهَ ۖ فَعَسَىٰٓ أُو۟لَٰٓئِكَ أَن يَكُونُوا۟ مِنَ ٱلْمُهْتَدِينَ
- (9:88) [listed for 87:14] لَٰكِنِ ٱلرَّسُولُ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ جَٰهَدُوا۟ بِأَمْوَٰلِهِمْ وَأَنفُسِهِمْ ۚ وَأُو۟لَٰٓئِكَ لَهُمُ ٱلْخَيْرَٰتُ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (9:108) [listed for 87:14] لَا تَقُمْ فِيهِ أَبَدًۭا ۚ لَّمَسْجِدٌ أُسِّسَ عَلَى ٱلتَّقْوَىٰ مِنْ أَوَّلِ يَوْمٍ أَحَقُّ أَن تَقُومَ فِيهِ ۚ فِيهِ رِجَالٌۭ يُحِبُّونَ أَن يَتَطَهَّرُوا۟ ۚ وَٱللَّهُ يُحِبُّ ٱلْمُطَّهِّرِينَ
- (19:55) [listed for 87:14] وَكَانَ يَأْمُرُ أَهْلَهُۥ بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ وَكَانَ عِندَ رَبِّهِۦ مَرْضِيًّۭا
- (19:60) [listed for 87:14] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ شَيْـًۭٔا
- (19:76) [listed for 87:14] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
- (20:64) [listed for 87:14] [cited in ¶28] فَأَجْمِعُوا۟ كَيْدَكُمْ ثُمَّ ٱئْتُوا۟ صَفًّۭا ۚ وَقَدْ أَفْلَحَ ٱلْيَوْمَ مَنِ ٱسْتَعْلَىٰ
- (21:73) [listed for 87:14] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا وَأَوْحَيْنَآ إِلَيْهِمْ فِعْلَ ٱلْخَيْرَٰتِ وَإِقَامَ ٱلصَّلَوٰةِ وَإِيتَآءَ ٱلزَّكَوٰةِ ۖ وَكَانُوا۟ لَنَا عَٰبِدِينَ
- (24:52) [listed for 87:14] وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ وَيَخْشَ ٱللَّهَ وَيَتَّقْهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْفَآئِزُونَ
- (25:64) [listed for 87:14] وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدًۭا وَقِيَٰمًۭا
- (27:3) [listed for 87:14] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (28:67) [listed for 87:14] فَأَمَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَعَسَىٰٓ أَن يَكُونَ مِنَ ٱلْمُفْلِحِينَ
- (31:4) [listed for 87:14] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (37:60) [listed for 87:14] إِنَّ هَٰذَا لَهُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (38:49) [listed for 87:14] هَٰذَا ذِكْرٌۭ ۚ وَإِنَّ لِلْمُتَّقِينَ لَحُسْنَ مَـَٔابٍۢ
- (58:13) [listed for 87:14] ءَأَشْفَقْتُمْ أَن تُقَدِّمُوا۟ بَيْنَ يَدَىْ نَجْوَىٰكُمْ صَدَقَٰتٍۢ ۚ فَإِذْ لَمْ تَفْعَلُوا۟ وَتَابَ ٱللَّهُ عَلَيْكُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَطِيعُوا۟ ٱللَّهَ وَرَسُولَهُۥ ۚ وَٱللَّهُ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (64:9) [listed for 87:14] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (65:5) [listed for 87:14] ذَٰلِكَ أَمْرُ ٱللَّهِ أَنزَلَهُۥٓ إِلَيْكُمْ ۚ وَمَن يَتَّقِ ٱللَّهَ يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُعْظِمْ لَهُۥٓ أَجْرًا
- (79:37) [listed for 87:14] فَأَمَّا مَن طَغَىٰ
- (88:3) [listed for 87:14] عَامِلَةٌۭ نَّاصِبَةٌۭ
- (91:8) [listed for 87:14] [cited in ¶26] فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- (92:17) [listed for 87:14] [cited in ¶27] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- (92:21) [listed for 87:14] وَلَسَوْفَ يَرْضَىٰ
- (96:10) [listed for 87:14] عَبْدًا إِذَا صَلَّىٰٓ

## weak (this ayah's own list) (36)

- (2:5) [listed for 87:14] أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (2:189) [listed for 87:14] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ ۗ وَلَيْسَ ٱلْبِرُّ بِأَن تَأْتُوا۟ ٱلْبُيُوتَ مِن ظُهُورِهَا وَلَٰكِنَّ ٱلْبِرَّ مَنِ ٱتَّقَىٰ ۗ وَأْتُوا۟ ٱلْبُيُوتَ مِنْ أَبْوَٰبِهَا ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
- (2:232) [listed for 87:14] وَإِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَبَلَغْنَ أَجَلَهُنَّ فَلَا تَعْضُلُوهُنَّ أَن يَنكِحْنَ أَزْوَٰجَهُنَّ إِذَا تَرَٰضَوْا۟ بَيْنَهُم بِٱلْمَعْرُوفِ ۗ ذَٰلِكَ يُوعَظُ بِهِۦ مَن كَانَ مِنكُمْ يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۗ ذَٰلِكُمْ أَزْكَىٰ لَكُمْ وَأَطْهَرُ ۗ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (2:277) [listed for 87:14] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ لَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (3:104) [listed for 87:14] وَلْتَكُن مِّنكُمْ أُمَّةٌۭ يَدْعُونَ إِلَى ٱلْخَيْرِ وَيَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ ۚ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (3:130) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَأْكُلُوا۟ ٱلرِّبَوٰٓا۟ أَضْعَٰفًۭا مُّضَٰعَفَةًۭ ۖ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
- (3:164) [listed for 87:14] لَقَدْ مَنَّ ٱللَّهُ عَلَى ٱلْمُؤْمِنِينَ إِذْ بَعَثَ فِيهِمْ رَسُولًۭا مِّنْ أَنفُسِهِمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍ
- (3:200) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱصْبِرُوا۟ وَصَابِرُوا۟ وَرَابِطُوا۟ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
- (4:162) [listed for 87:14] لَّٰكِنِ ٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ مِنْهُمْ وَٱلْمُؤْمِنُونَ يُؤْمِنُونَ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ ۚ وَٱلْمُقِيمِينَ ٱلصَّلَوٰةَ ۚ وَٱلْمُؤْتُونَ ٱلزَّكَوٰةَ وَٱلْمُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ أُو۟لَٰٓئِكَ سَنُؤْتِيهِمْ أَجْرًا عَظِيمًا
- (5:12) [listed for 87:14] ۞ وَلَقَدْ أَخَذَ ٱللَّهُ مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ وَبَعَثْنَا مِنْهُمُ ٱثْنَىْ عَشَرَ نَقِيبًۭا ۖ وَقَالَ ٱللَّهُ إِنِّى مَعَكُمْ ۖ لَئِنْ أَقَمْتُمُ ٱلصَّلَوٰةَ وَءَاتَيْتُمُ ٱلزَّكَوٰةَ وَءَامَنتُم بِرُسُلِى وَعَزَّرْتُمُوهُمْ وَأَقْرَضْتُمُ ٱللَّهَ قَرْضًا حَسَنًۭا لَّأُكَفِّرَنَّ عَنكُمْ سَيِّـَٔاتِكُمْ وَلَأُدْخِلَنَّكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ فَمَن كَفَرَ بَعْدَ ذَٰلِكَ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (5:55) [listed for 87:14] إِنَّمَا وَلِيُّكُمُ ٱللَّهُ وَرَسُولُهُۥ وَٱلَّذِينَ ءَامَنُوا۟ ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُمْ رَٰكِعُونَ
- (6:135) [listed for 87:14] قُلْ يَٰقَوْمِ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنِّى عَامِلٌۭ ۖ فَسَوْفَ تَعْلَمُونَ مَن تَكُونُ لَهُۥ عَٰقِبَةُ ٱلدَّارِ ۗ إِنَّهُۥ لَا يُفْلِحُ ٱلظَّٰلِمُونَ
- (7:69) [listed for 87:14] أَوَعَجِبْتُمْ أَن جَآءَكُمْ ذِكْرٌۭ مِّن رَّبِّكُمْ عَلَىٰ رَجُلٍۢ مِّنكُمْ لِيُنذِرَكُمْ ۚ وَٱذْكُرُوٓا۟ إِذْ جَعَلَكُمْ خُلَفَآءَ مِنۢ بَعْدِ قَوْمِ نُوحٍۢ وَزَادَكُمْ فِى ٱلْخَلْقِ بَصْۜطَةًۭ ۖ فَٱذْكُرُوٓا۟ ءَالَآءَ ٱللَّهِ لَعَلَّكُمْ تُفْلِحُونَ
- (7:157) [listed for 87:14] ٱلَّذِينَ يَتَّبِعُونَ ٱلرَّسُولَ ٱلنَّبِىَّ ٱلْأُمِّىَّ ٱلَّذِى يَجِدُونَهُۥ مَكْتُوبًا عِندَهُمْ فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ يَأْمُرُهُم بِٱلْمَعْرُوفِ وَيَنْهَىٰهُمْ عَنِ ٱلْمُنكَرِ وَيُحِلُّ لَهُمُ ٱلطَّيِّبَٰتِ وَيُحَرِّمُ عَلَيْهِمُ ٱلْخَبَٰٓئِثَ وَيَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ بِهِۦ وَعَزَّرُوهُ وَنَصَرُوهُ وَٱتَّبَعُوا۟ ٱلنُّورَ ٱلَّذِىٓ أُنزِلَ مَعَهُۥٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (8:45) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا لَقِيتُمْ فِئَةًۭ فَٱثْبُتُوا۟ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
- (9:5) [listed for 87:14] فَإِذَا ٱنسَلَخَ ٱلْأَشْهُرُ ٱلْحُرُمُ فَٱقْتُلُوا۟ ٱلْمُشْرِكِينَ حَيْثُ وَجَدتُّمُوهُمْ وَخُذُوهُمْ وَٱحْصُرُوهُمْ وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ ۚ فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَخَلُّوا۟ سَبِيلَهُمْ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (9:11) [listed for 87:14] فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ ۗ وَنُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (9:71) [listed for 87:14] وَٱلْمُؤْمِنُونَ وَٱلْمُؤْمِنَٰتُ بَعْضُهُمْ أَوْلِيَآءُ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَيُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَيُطِيعُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ سَيَرْحَمُهُمُ ٱللَّهُ ۗ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (10:17) [listed for 87:14] فَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ كَذَّبَ بِـَٔايَٰتِهِۦٓ ۚ إِنَّهُۥ لَا يُفْلِحُ ٱلْمُجْرِمُونَ
- (10:69) [listed for 87:14] قُلْ إِنَّ ٱلَّذِينَ يَفْتَرُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ لَا يُفْلِحُونَ
- (10:77) [listed for 87:14] قَالَ مُوسَىٰٓ أَتَقُولُونَ لِلْحَقِّ لَمَّا جَآءَكُمْ ۖ أَسِحْرٌ هَٰذَا وَلَا يُفْلِحُ ٱلسَّٰحِرُونَ
- (18:20) [listed for 87:14] إِنَّهُمْ إِن يَظْهَرُوا۟ عَلَيْكُمْ يَرْجُمُوكُمْ أَوْ يُعِيدُوكُمْ فِى مِلَّتِهِمْ وَلَن تُفْلِحُوٓا۟ إِذًا أَبَدًۭا
- (19:31) [listed for 87:14] وَجَعَلَنِى مُبَارَكًا أَيْنَ مَا كُنتُ وَأَوْصَٰنِى بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ مَا دُمْتُ حَيًّۭا
- (20:48) [listed for 87:14] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:69) [listed for 87:14] وَأَلْقِ مَا فِى يَمِينِكَ تَلْقَفْ مَا صَنَعُوٓا۟ ۖ إِنَّمَا صَنَعُوا۟ كَيْدُ سَٰحِرٍۢ ۖ وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ
- (22:41) [listed for 87:14] ٱلَّذِينَ إِن مَّكَّنَّٰهُمْ فِى ٱلْأَرْضِ أَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ وَأَمَرُوا۟ بِٱلْمَعْرُوفِ وَنَهَوْا۟ عَنِ ٱلْمُنكَرِ ۗ وَلِلَّهِ عَٰقِبَةُ ٱلْأُمُورِ
- (22:78) [listed for 87:14] وَجَٰهِدُوا۟ فِى ٱللَّهِ حَقَّ جِهَادِهِۦ ۚ هُوَ ٱجْتَبَىٰكُمْ وَمَا جَعَلَ عَلَيْكُمْ فِى ٱلدِّينِ مِنْ حَرَجٍۢ ۚ مِّلَّةَ أَبِيكُمْ إِبْرَٰهِيمَ ۚ هُوَ سَمَّىٰكُمُ ٱلْمُسْلِمِينَ مِن قَبْلُ وَفِى هَٰذَا لِيَكُونَ ٱلرَّسُولُ شَهِيدًا عَلَيْكُمْ وَتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ ۚ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱعْتَصِمُوا۟ بِٱللَّهِ هُوَ مَوْلَىٰكُمْ ۖ فَنِعْمَ ٱلْمَوْلَىٰ وَنِعْمَ ٱلنَّصِيرُ
- (23:117) [listed for 87:14] وَمَن يَدْعُ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ لَا بُرْهَٰنَ لَهُۥ بِهِۦ فَإِنَّمَا حِسَابُهُۥ عِندَ رَبِّهِۦٓ ۚ إِنَّهُۥ لَا يُفْلِحُ ٱلْكَٰفِرُونَ
- (24:51) [listed for 87:14] إِنَّمَا كَانَ قَوْلَ ٱلْمُؤْمِنِينَ إِذَا دُعُوٓا۟ إِلَى ٱللَّهِ وَرَسُولِهِۦ لِيَحْكُمَ بَيْنَهُمْ أَن يَقُولُوا۟ سَمِعْنَا وَأَطَعْنَا ۚ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (28:37) [listed for 87:14] وَقَالَ مُوسَىٰ رَبِّىٓ أَعْلَمُ بِمَن جَآءَ بِٱلْهُدَىٰ مِنْ عِندِهِۦ وَمَن تَكُونُ لَهُۥ عَٰقِبَةُ ٱلدَّارِ ۖ إِنَّهُۥ لَا يُفْلِحُ ٱلظَّٰلِمُونَ
- (41:7) [listed for 87:14] ٱلَّذِينَ لَا يُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (56:29) [listed for 87:14] وَطَلْحٍۢ مَّنضُودٍۢ
- (59:9) [listed for 87:14] وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ يُحِبُّونَ مَنْ هَاجَرَ إِلَيْهِمْ وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةًۭ مِّمَّآ أُوتُوا۟ وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (62:2) [listed for 87:14] [cited in ¶21] هُوَ ٱلَّذِى بَعَثَ فِى ٱلْأُمِّيِّۦنَ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍۢ
- (64:16) [listed for 87:14] فَٱتَّقُوا۟ ٱللَّهَ مَا ٱسْتَطَعْتُمْ وَٱسْمَعُوا۟ وَأَطِيعُوا۟ وَأَنفِقُوا۟ خَيْرًۭا لِّأَنفُسِكُمْ ۗ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (73:20) [listed for 87:14] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ

## named by the passage's own list as weak for this ayah (6)

- (5:6) [listed for 87:14] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (20:75) [listed for 87:14] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (26:136) [listed for 87:14] قَالُوا۟ سَوَآءٌ عَلَيْنَآ أَوَعَظْتَ أَمْ لَمْ تَكُن مِّنَ ٱلْوَٰعِظِينَ
- (39:54) [listed for 87:14] وَأَنِيبُوٓا۟ إِلَىٰ رَبِّكُمْ وَأَسْلِمُوا۟ لَهُۥ مِن قَبْلِ أَن يَأْتِيَكُمُ ٱلْعَذَابُ ثُمَّ لَا تُنصَرُونَ
- (53:39) [listed for 87:14] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
- (74:51) [listed for 87:14] فَرَّتْ مِن قَسْوَرَةٍۭ

## neighbours: within two ayat of a passage the commentary cites (65)

- (4:47) [next to 4:49] يَٰٓأَيُّهَا ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ ءَامِنُوا۟ بِمَا نَزَّلْنَا مُصَدِّقًۭا لِّمَا مَعَكُم مِّن قَبْلِ أَن نَّطْمِسَ وُجُوهًۭا فَنَرُدَّهَا عَلَىٰٓ أَدْبَارِهَآ أَوْ نَلْعَنَهُمْ كَمَا لَعَنَّآ أَصْحَٰبَ ٱلسَّبْتِ ۚ وَكَانَ أَمْرُ ٱللَّهِ مَفْعُولًا
- (4:48) [next to 4:49] إِنَّ ٱللَّهَ لَا يَغْفِرُ أَن يُشْرَكَ بِهِۦ وَيَغْفِرُ مَا دُونَ ذَٰلِكَ لِمَن يَشَآءُ ۚ وَمَن يُشْرِكْ بِٱللَّهِ فَقَدِ ٱفْتَرَىٰٓ إِثْمًا عَظِيمًا
- (4:50) [next to 4:49] ٱنظُرْ كَيْفَ يَفْتَرُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ ۖ وَكَفَىٰ بِهِۦٓ إِثْمًۭا مُّبِينًا
- (4:51) [next to 4:49] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يُؤْمِنُونَ بِٱلْجِبْتِ وَٱلطَّٰغُوتِ وَيَقُولُونَ لِلَّذِينَ كَفَرُوا۟ هَٰٓؤُلَآءِ أَهْدَىٰ مِنَ ٱلَّذِينَ ءَامَنُوا۟ سَبِيلًا
- (20:59) [next to 20:61] قَالَ مَوْعِدُكُمْ يَوْمُ ٱلزِّينَةِ وَأَن يُحْشَرَ ٱلنَّاسُ ضُحًۭى
- (20:60) [next to 20:61] فَتَوَلَّىٰ فِرْعَوْنُ فَجَمَعَ كَيْدَهُۥ ثُمَّ أَتَىٰ
- (20:62) [next to 20:61] فَتَنَٰزَعُوٓا۟ أَمْرَهُم بَيْنَهُمْ وَأَسَرُّوا۟ ٱلنَّجْوَىٰ
- (20:63) [next to 20:61] قَالُوٓا۟ إِنْ هَٰذَٰنِ لَسَٰحِرَٰنِ يُرِيدَانِ أَن يُخْرِجَاكُم مِّنْ أَرْضِكُم بِسِحْرِهِمَا وَيَذْهَبَا بِطَرِيقَتِكُمُ ٱلْمُثْلَىٰ
- (20:65) [next to 20:64] قَالُوا۟ يَٰمُوسَىٰٓ إِمَّآ أَن تُلْقِىَ وَإِمَّآ أَن نَّكُونَ أَوَّلَ مَنْ أَلْقَىٰ
- (20:66) [next to 20:64] قَالَ بَلْ أَلْقُوا۟ ۖ فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ أَنَّهَا تَسْعَىٰ
- (20:67) [next to 20:68] فَأَوْجَسَ فِى نَفْسِهِۦ خِيفَةًۭ مُّوسَىٰ
- (20:70) [next to 20:68] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (20:74) [next to 20:76] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:77) [next to 20:76] وَلَقَدْ أَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ أَنْ أَسْرِ بِعِبَادِى فَٱضْرِبْ لَهُمْ طَرِيقًۭا فِى ٱلْبَحْرِ يَبَسًۭا لَّا تَخَٰفُ دَرَكًۭا وَلَا تَخْشَىٰ
- (20:78) [next to 20:76] فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ
- (23:0) [next to 23:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (23:3) [next to 23:1] وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ
- (23:5) [next to 23:4] وَٱلَّذِينَ هُمْ لِفُرُوجِهِمْ حَٰفِظُونَ
- (23:6) [next to 23:4] إِلَّا عَلَىٰٓ أَزْوَٰجِهِمْ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَإِنَّهُمْ غَيْرُ مَلُومِينَ
- (24:19) [next to 24:21] إِنَّ ٱلَّذِينَ يُحِبُّونَ أَن تَشِيعَ ٱلْفَٰحِشَةُ فِى ٱلَّذِينَ ءَامَنُوا۟ لَهُمْ عَذَابٌ أَلِيمٌۭ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (24:20) [next to 24:21] وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ وَأَنَّ ٱللَّهَ رَءُوفٌۭ رَّحِيمٌۭ
- (24:22) [next to 24:21] وَلَا يَأْتَلِ أُو۟لُوا۟ ٱلْفَضْلِ مِنكُمْ وَٱلسَّعَةِ أَن يُؤْتُوٓا۟ أُو۟لِى ٱلْقُرْبَىٰ وَٱلْمَسَٰكِينَ وَٱلْمُهَٰجِرِينَ فِى سَبِيلِ ٱللَّهِ ۖ وَلْيَعْفُوا۟ وَلْيَصْفَحُوٓا۟ ۗ أَلَا تُحِبُّونَ أَن يَغْفِرَ ٱللَّهُ لَكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌ
- (24:23) [next to 24:21] إِنَّ ٱلَّذِينَ يَرْمُونَ ٱلْمُحْصَنَٰتِ ٱلْغَٰفِلَٰتِ ٱلْمُؤْمِنَٰتِ لُعِنُوا۟ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
- (30:37) [next to 30:39] أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (30:40) [next to 30:39] ٱللَّهُ ٱلَّذِى خَلَقَكُمْ ثُمَّ رَزَقَكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ۖ هَلْ مِن شُرَكَآئِكُم مَّن يَفْعَلُ مِن ذَٰلِكُم مِّن شَىْءٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (30:41) [next to 30:39] ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ بِمَا كَسَبَتْ أَيْدِى ٱلنَّاسِ لِيُذِيقَهُم بَعْضَ ٱلَّذِى عَمِلُوا۟ لَعَلَّهُمْ يَرْجِعُونَ
- (35:16) [next to 35:18] إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (35:17) [next to 35:18] وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ
- (35:19) [next to 35:18] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ
- (35:20) [next to 35:18] وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ
- (53:30) [next to 53:32] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (53:31) [next to 53:32] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
- (53:33) [next to 53:32] أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ
- (53:34) [next to 53:32] وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ
- (62:0) [next to 62:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (62:1) [next to 62:2] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ٱلْمَلِكِ ٱلْقُدُّوسِ ٱلْعَزِيزِ ٱلْحَكِيمِ
- (62:3) [next to 62:2] وَءَاخَرِينَ مِنْهُمْ لَمَّا يَلْحَقُوا۟ بِهِمْ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (62:4) [next to 62:2] ذَٰلِكَ فَضْلُ ٱللَّهِ يُؤْتِيهِ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (79:16) [next to 79:18] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- (79:17) [next to 79:18] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (79:20) [next to 79:18] فَأَرَىٰهُ ٱلْءَايَةَ ٱلْكُبْرَىٰ
- (79:21) [next to 79:19] فَكَذَّبَ وَعَصَىٰ
- (79:22) [next to 79:24] ثُمَّ أَدْبَرَ يَسْعَىٰ
- (79:23) [next to 79:24] فَحَشَرَ فَنَادَىٰ
- (79:25) [next to 79:24] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- (79:26) [next to 79:24] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (80:0) [next to 80:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (80:5) [next to 80:3] أَمَّا مَنِ ٱسْتَغْنَىٰ
- (80:6) [next to 80:4] فَأَنتَ لَهُۥ تَصَدَّىٰ
- (80:8) [next to 80:7] وَأَمَّا مَن جَآءَكَ يَسْعَىٰ
- (80:10) [next to 80:9] فَأَنتَ عَنْهُ تَلَهَّىٰ
- (80:11) [next to 80:9] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
- (80:22) [next to 80:24] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
- (80:23) [next to 80:24] كَلَّا لَمَّا يَقْضِ مَآ أَمَرَهُۥ
- (80:25) [next to 80:24] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
- (80:28) [next to 80:26] وَعِنَبًۭا وَقَضْبًۭا
- (80:29) [next to 80:27] وَزَيْتُونًۭا وَنَخْلًۭا
- (91:5) [next to 91:7] وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- (91:6) [next to 91:7] وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- (91:11) [next to 91:9] كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- (91:12) [next to 91:10] إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- (92:13) [next to 92:15] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:14) [next to 92:15] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:16) [next to 92:15] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:19) [next to 92:17] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ

