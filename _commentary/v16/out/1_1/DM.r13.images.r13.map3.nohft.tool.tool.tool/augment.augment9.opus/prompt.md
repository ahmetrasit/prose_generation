Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:1; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_1.reading.tr.md (prose paragraphs numbered) =====
## Fiili söylenmemiş bir başlangıç

[¶1] Ayet tam bir cümle değildir. Bir edat, bir isim ve bu isme bağlanan üç ad vardır: {ar:بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:bismillâhi'r-rahmâni'r-rahîm, gloss:Rahman ve Rahim olan Allah'ın adıyla, source:1:1}. Baştaki "bi" edatı bir işi bir şeyle birlikte yapmayı da, bir şey aracılığıyla yapmayı da anlatır. Türkçedeki "-ile" eki de bu iki yönü taşır. Bu yüzden "adıyla" karşılığı yerindedir. Fakat bu adla neyin yapıldığı söylenmez. Fiil boş bırakılmıştır. O boşluğu, sözü ağzına alanın o anda yaptığı iş doldurur. Her namazda okunan Fâtiha'da bu iş, ardından gelen altı ayettir: hamd etmek, kulluğu dile getirmek ve yol istemek. Ayet aynı biçimiyle başka herhangi bir işin başına da konabilir.

[¶2] Kur'an başka yerlerde fiili açıkça söyler. Allah'ın Peygamberine verdiği bir emirde fiil okumaktır: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bismi rabbikellezî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Ekilen tohum, buluttan inen su ve yakılan ateş tek tek sorulduktan sonra fiil tesbih olur: {ar:فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ, tr:fe-sebbih bismi rabbike'l-azîm, gloss:o halde büyük Rabbinin adıyla tesbih et, source:56:74}. Bu ayetlerde ad, fiilin yanında aracı ya da eşlikçi olarak durur. Birinci ayette ise fiil düştüğü için ad tek başına ve önde kalır. Söze başlayan kişi ne yaptığını söylemeden önce kimin adıyla yaptığını söyler.

[¶3] Bu boşluğun ne kadar geniş olduğunu Nuh'un sahnesi gösterir. Allah'ın emri gelip tandır kaynayınca Nuh'a her türden birer çifti, ailesini ve inananları gemiye alması söylenir {source:11:40}. Nuh binenlere şöyle seslenir: {ar:ٱرْكَبُوا۟ فِيهَا بِسْمِ ٱللَّهِ مَجْر۪ىٰهَا وَمُرْسَىٰهَآ ۚ إِنَّ رَبِّى لَغَفُورٌۭ رَّحِيمٌۭ, tr:irkebû fîhâ bismillâhi mecrâhâ ve mürsâhâ, inne rabbî le-gafûrun rahîm, gloss:binin ona; yürümesi de durması da Allah'ın adıyladır; Rabbim çok bağışlayan, çok merhamet edendir, source:11:41}. Burada ad tek bir hareketin değil, bütün yolculuğun üstüne konur. Geminin yürüyüşü de demir atıp durması da bu adın altındadır. Cümle de "rahîm" sıfatıyla biter. Gemi dağ gibi dalgaların arasında ilerlerken Nuh uzakta duran oğlunu çağırır. Oğlu bir dağa sığınacağını söyler. Nuh ona şöyle cevap verir: {ar:لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ إِلَّا مَن رَّحِمَ, tr:lâ âsıme'l-yevme min emrillâhi illâ men rahim, gloss:bugün Allah'ın emrinden, O'nun merhamet ettiği dışında kimse korunamaz, source:11:43}. Adın altına girilen gemi, merhametin kapsadığı yerle aynı yerdir. Fâtiha'nın birinci ayeti de fiilini söylemediği için ardından gelen her şeyi baştan sona aynı adın altına alır, tıpkı geminin yürüyüşü ile duruşu gibi.

[¶4] Bir işin üstünde söylenen ad o işin niteliğini de değiştirir. Kur'an etin yenip yenmemesini adın anılıp anılmamasına bağlar: {ar:فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ, tr:fe-külû mimmâ zükirasmullâhi aleyh, gloss:üzerine Allah'ın adı anılandan yiyin, source:6:118}, {ar:وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ, tr:ve lâ te'külû mimmâ lem yüzkerismullâhi aleyh, gloss:üzerine Allah'ın adı anılmayandan yemeyin, source:6:121}. Eğitilmiş av hayvanlarının sahipleri için tuttuğu av için de aynı şey söylenir: {ar:فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ, tr:fe-külû mimmâ emsekne aleyküm vezkürüsmellâhi aleyh, gloss:sizin için tuttuklarından yiyin ve üzerine Allah'ın adını anın, source:5:4}. Her ümmete bir ibadet yolu verilmiştir. Amaç, kendilerine rızık olarak verilen hayvanların üzerinde adın anılmasıdır {source:22:34}. Kurbanlık develer sıra sıra dururken üzerlerine ad anılır {source:22:36}. Et aynı et, av aynı av, kesim aynı kesimdir. Fakat üzerinde ad söylendiğinde başka bir şeye dönüşür. Kurbanlığın sürüden ayrılıp Eve götürülmesi, altıncı ayetteki "ihdinâ" kelimesinin taşıdığı bir sahnedir. Bu ayetin o sahnedeki payı, yolculuğun başında hayvanın üstünde söylenen addır.

## Ad: ufukta yükselip seçilen şekil

[¶5] Arapçada "ism" kelimesi yükseklik bildiren bir kökten gelir: {ar:السمو الارتفاع والعلو, tr:es-sümüvvü'l-irtifâu ve'l-ulüvv, gloss:sümüvv yükselmek ve yüce olmaktır, source:"س م و,B001"}. Bu kökün aile görüntüleri burada ve aşağıda hep kelimenin bu ayetteki anlamının, yani "ad"ın yanında duyulur, onun yerine geçmez. Kökün en açık görüntüsü çölde uzaktan beliren bir karaltıdır. Önce belirsizdir, sonra yükseldikçe göz onu seçer. Araplar bunun için {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hattâ'stesbettüh, gloss:bir karaltı önümde yükseldi, sonunda onu iyice seçtim, source:"س م و,B002"} derlerdi. Yeni ayın ilk görünüşü de böyle adlandırılır: {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetü'l-hilâli şahsuhû izâ irtefea ani'l-ufuki şey'â, gloss:hilalin semâvesi, ufuktan biraz yükseldiğinde görünen şeklidir, source:"س م و,B002"}. Hilal ufka yapışık durdukça görülmez. Biraz yükselince ince bir yay olarak seçilir ve ay görülmüş olur.

[¶6] Ad da böyle işler. Kelime şöyle açıklanır: {ar:الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى, tr:el-ismü müştakkun mine's-sümüvvi ve hüve'r-rif'a, tenvîhen ale'd-delâleti ale'l-ma'nâ, gloss:isim yükseklik anlamındaki sümüvvden türer; anlamı göstersin diye öne çıkarılmıştır, source:"س م و,B005"}. Bir başka açıklama da şöyledir: {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismü mâ yu'rafü bihî zâtü'ş-şey' ve aslühû sümüvv, bihî rufi'a zikru'l-müsemmâ, gloss:isim, bir şeyin kendisinin onunla tanındığı şeydir; aslı sümüvvdür, adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Ad, bir şeyi belirsizlikten çıkarıp tanınacak kadar yukarı kaldırır. İyi bir adın insanlar arasında dolaşması da aynı kelimeyle anlatılır: {ar:ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر, tr:zehebe sîtühû fi'n-nâsi ve semâh, ey savtühû fi'l-hayri lâ fi'ş-şer, gloss:ünü ve adı insanlar arasında yayıldı, yani iyilikle anılması, kötülükle değil, source:"س م و,B008"}. Türkçede "isim" çoğunlukla bir etiket ya da dilbilgisindeki ad soylu kelime olarak kalmıştır. Arapçada ise kelime, adlandırılanın anılışını yükseltmeyi de içinde taşır.

[¶7] Kur'an da adın kendisini yüceltir. Peygambere şöyle denir: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihisme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Burada tesbih edilen addır. "En yüce" anlamındaki "a'lâ" başka bir köktendir. Ancak bu kök, adın kökünü açıklarken kullanılan "ulüvv" kelimesiyle aynıdır. Bu bir kök birliği değil, bir anlam yakınlığıdır. Bir başka surenin son ayeti de adı yüceltir: {ar:تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ, tr:tebârakesmü rabbike zi'l-celâli ve'l-ikrâm, gloss:celal ve ikram sahibi Rabbinin adı ne yücedir, source:55:78}. "Bismillâh" diyen kişi, işine başlamadan önce bir adı kaldırır ve işini, ufukta seçilen o adın altına koyar.

[¶8] Bu kök yalnız adı değil, insanın başının üstündeki her şeyi de adlandırır: {ar:السماء كل ما علاك فأظلك, tr:es-semâü küllü mâ alâke fe-ezalleke, gloss:sema, üstünde durup sana gölge eden her şeydir, source:"س م و,B004"}. Bir evin tavanı da böyle anılır: {ar:سماوة البيت سقفه, tr:semâvetü'l-beyti sakfuh, gloss:evin semâvesi onun tavanıdır, source:"س م و,B004"}. İçindekileri örten ve onlara gölge eden şey, bir evin en yüksek yeridir. Fiili söylenmemiş bir işin başında duran ad da o işin üstünde durur. Araplar buluta da yağmura da "semâ" derlerdi: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-Arabü tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da sema derler, source:"س م و,B004"}. Bitkiye de aynı adı verirlerdi {source:"س م و,B004"}. Bu kullanım, ikinci ayetteki "Rab" kelimesinin bitkiyi büyüten bulutuyla birlikte kurulan bir su sahnesine katılır. O sahne surenin bütününe aittir. Ufukta yükselen yıldızı, ayı ve güneşi Rab sanan, batışlarını görünce yolunu yitirme korkusunu dile getiren İbrahim'in gece sahnesi de beşinci ayetin kulluğu ve yedinci ayetin "dâllîn" kelimesiyle kurulur {source:6:77}. Bu ayet o sahneye yükselen şeklin adını verir.

## Adaşı olmayan ad ve altı boş adlar

[¶9] Adın bir yükselme olduğu, Kur'an'daki bir soruda belirgin bir yere varır. Bu soruyu, "Biz ancak Rabbinin emriyle ineriz" diyenlerin sözü hazırlar {source:19:64}. Ardından şu gelir: {ar:رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:rabbü's-semâvâti ve'l-ardı ve mâ beynehümâ fa'büdhü vastabir li-ibâdetih, hel ta'lemü lehû semiyyâ, gloss:göklerin, yerin ve ikisinin arasındakilerin Rabbidir; O'na kulluk et ve kulluğunda sabırlı ol; O'nun adını taşıyabilecek bir dengini biliyor musun, source:19:65}. Ayetin başındaki "semâvât" ile sonundaki "semiyy", "ism" kelimesiyle aynı köktendir. Bu bir kök birliğidir. "Semiyy" kelimesi şöyle açıklanır: {ar:سميا أي نظيرا له يستحق اسمه, tr:semiyyen, ey nazîran lehû yestehıkku ismeh, gloss:semiyy, onun adını hak eden bir dengidir, source:"س م و,B005"}. Günlük dilde adaş için de bu kelime kullanılır: {ar:هذا سمي فلان, tr:hâzâ semiyyü fülân, gloss:bu, falancanın adaşıdır, source:"س م و,B005"}. Aynı kök, yükseklikte boy ölçüşmeyi de anlatır. Araplar kimsenin boy ölçüşemediği kişi için {ar:فلان لا يسامى, tr:fülânün lâ yüsâmâ, gloss:falancayla yükseklikte yarışılmaz, source:"س م و,B007"} derlerdi. Aynı kullanımda şu söz de geçer: {ar:قد علا من ساماه, tr:kad alâ men sâmâh, gloss:kendisiyle yükseklik yarışına gireni geçti, source:"س م و,B007"}. Göklerin Rabbinin adı da böyledir: Kimse onu taşıyamaz, kimse onunla yükseklik yarışına giremez. Birinci ayette yükseltilen ad, adaşı olmayan bir addır.

[¶10] Kur'an bu adı çağrıyla birlikte anar. Ayetteki ilk iki ad yan yana bir çağrı olarak geçer: {ar:قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ, tr:kuli'd'ullâhe evi'd'u'r-rahmân, eyyen mâ ted'û fe-lehü'l-esmâü'l-hüsnâ, gloss:de ki: Allah diye çağırın ya da Rahman diye çağırın; hangisiyle çağırırsanız çağırın, en güzel adlar O'nundur, source:17:110}. Adlar çağırmak içindir: {ar:وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا, tr:ve lillâhi'l-esmâü'l-hüsnâ fed'ûhü bihâ, gloss:en güzel adlar Allah'ındır; O'nu onlarla çağırın, source:7:180}. "Esmâ" kelimesi "ism"in çoğuludur ve biçimi yükseklik bildiren köke uyar. Âdem'e öğretilen de adlardır {source:2:31}. Ad, bilmenin kapısıdır.

[¶11] Kur'an'da bunun karşısında altı boş adlar vardır. Zindandaki Yusuf, yanındaki iki tutsağa şöyle der: {ar:مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ, tr:mâ ta'büdûne min dûnihî illâ esmâen semmeytümûhâ entüm ve âbâüküm mâ enzelallâhü bihâ min sultân, gloss:O'nu bırakıp kulluk ettikleriniz, sizin ve atalarınızın taktığı adlardan başka bir şey değildir; Allah onlar için hiçbir delil indirmemiştir, source:12:40}. Lât, Uzzâ ve Menât için de aynı söz söylenir {source:53:19}: {ar:إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم, tr:in hiye illâ esmâün semmeytümûhâ entüm ve âbâüküm, gloss:bunlar sizin ve atalarınızın taktığı adlardan başka bir şey değildir, source:53:23}. Ad, bir şeyin seçilsin diye yükselmesiyse, bu adlar ufukta yükselen ama ardında hiçbir gövde bulunmayan şekillerdir. Birinci ayetteki ad ise ardında gövdesi olan, seçildikçe daha çok seçilen bir addır.

## Damga: sahibini gösteren iz

[¶12] Arap dilcilerinin bir kısmı "ism" kelimesini yükseklik kökünden değil, damgalamak anlamındaki başka bir kökten türetmeyi önermiştir. Kur'an'daki "esmâ" çoğulu yükseklik köküne uyduğu için bu öneri kelimenin kökünü belirlemez. Ama yanında bir görüntü olarak duyulabilir. Damgalama şöyle anlatılır: {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmü eseru keyy, ve ba'îrun mevsûmun vüsime bi-simetin yu'rafü bihâ min kat'ı üzünin ev keyy, gloss:vesm dağlama izidir; mevsûm deve, kulak kesiği ya da dağlama gibi tanınacağı bir işaretle damgalanmış devedir, source:"و س م,B001"}. Bunun aracı da adlandırılmıştır: {ar:الميسم المكواة أو الشيء الذي يوسم به الدواب, tr:el-mîsemü'l-mikvâtü evi'ş-şey'ü'llezî yûsemu bihi'd-devâbb, gloss:mîsem, hayvanların damgalandığı kızgın demirdir, source:"و س م,B001"}. Demir ateşte kızdırılır ve devenin derisine bastırılır. Yara iyileşir ama iz kalır. Sular başında birçok sürü birbirine karıştığında hangi devenin kime ait olduğu bu izden anlaşılır. Damga deveye bir şey eklemez, yalnızca onun kime ait olduğunu söyler.

[¶13] Bu görüntüde ad, bir şeyin üstüne konmuş ve sahibini gösteren bir izdir. Bir işe "bismillâh" diye başlamak, o işin üstüne kime ait olduğunu söyleyen bir iz koymak gibidir. Kur'an bu ayeti bir kez daha, bir mektubun başında aynen gösterir. Süleyman mektubunu bir kuşla Sebe' halkına gönderir {source:27:28}. Kraliçe kavminin ileri gelenlerine kendisine değerli bir mektup bırakıldığını söyler {source:27:29} ve mektubu şöyle tanıtır: {ar:إِنَّهُۥ مِن سُلَيْمَٰنَ وَإِنَّهُۥ بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:innehû min Süleymâne ve innehû bismillâhi'r-rahmâni'r-rahîm, gloss:o, Süleyman'dandır ve Rahman ve Rahim olan Allah'ın adıyladır, source:27:30}. Kraliçe mektubu okumadan önce onun iki izini okur: kimden geldiğini ve kimin adıyla yazıldığını. Mektubun asıl sözü hemen ardından gelir: {ar:أَلَّا تَعْلُوا۟ عَلَىَّ وَأْتُونِى مُسْلِمِينَ, tr:ellâ ta'lû aleyye ve'tûnî müslimîn, gloss:bana karşı büyüklük taslamayın, teslim olarak bana gelin, source:27:31}. "Ta'lû" kelimesi yükselmek demektir. Kök farklıdır ama anlam yakındır. Mektubun başında yükseltilen tek şey addır. Muhataplardan istenen ise kendilerini yükseltmemeleridir.

[¶14] İzi okumak da bu ailedendir: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtü fîhi'l-hayra ve'ş-şerr, ey raeytü fîhi eserâ, gloss:onda hayrı ya da şerri sezdim, yani onda bir iz gördüm, source:"و س م,B002"}. Lut'un şehri altüst edilip üzerine taş yağdırıldıktan sonra {source:15:74} Kur'an şunu söyler: {ar:إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْمُتَوَسِّمِينَ, tr:inne fî zâlike le-âyâtin li'l-mütevessimîn, gloss:bunda izleri okuyabilenler için ayetler vardır, source:15:75}. Ayetleri dinlediğinde "öncekilerin masalları" diyen, çok yemin eden ve laf taşıyan biri için de şöyle denir: {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimuhû ale'l-hurtûm, gloss:onun burnuna damga vuracağız, source:68:16}. Bu damga onun kim olduğunu herkese gösterecektir. Aynı kökte toprağa vurulan bir damga da vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyü evvelü matari's-sene, yesimü'l-arda bi'n-nebât, gloss:vesmî yılın ilk yağmurudur; toprağı bitkiyle damgalar, source:"و س م,B003"}. İlk yağmurdan sonra çıkan yeşillik, yağmurun nereye düştüğünü gösteren izdir. Türkçedeki "mevsim" kelimesi de bu köktendir. Bugün yılın dört bölümünden birini anlatır. Oysa kelime önce hacıların ve pazarların toplandığı, işaretlenmiş buluşma zamanıydı: {ar:موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه, tr:mevsimü'l-hâcci mecmeuhüm, sümmiye bi-zâlike li-ennehû ma'lemun yüctemeu ileyh, gloss:hacıların mevsimi toplandıkları yerdir; insanların toplandığı işaretli bir yer olduğu için bu adı almıştır, source:"و س م,B004"}. Damgalı deve, yedinci ayetin son kelimesinin anlattığı sahibi bilinmeyen başıboş devenin karşısında durur. O sahne yedinci ayete aittir.

## Allah: kulluk edilenin ve çağrılanın adı

[¶15] Ayetteki ikinci kelime, adı anılanın kendi adıdır. Bu adın kökü tapınmayı ve kulluk etmeyi anlatır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah yüce Allah'tır, çünkü kulluk edilendir, source:"ء ل ه,B001"}. Bir başka söz bunun ölçüsünü verir: {ar:لا يكون إلاها حتى يكون معبودا, tr:lâ yekûnü ilâhen hattâ yekûne ma'bûdâ, gloss:kulluk edilmedikçe ilah olmaz, source:"ء ل ه,B001"}. "Allah" adının bu kelimeden nasıl oluştuğu da anlatılır: {ar:الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى, tr:Allâh, kîle aslühû ilâh, fe-huzifet hemzetühû ve üdhile aleyhe'l-elifü ve'l-lâm, fe-hussa bi'l-Bârî teâlâ, gloss:Allah adının aslının "ilâh" olduğu, hemzesi düşüp başına harf-i tarif gelerek yalnız Yaratıcıya özgü kılındığı söylenmiştir, source:"ء ل ه,B002"}. Böylece birinci ayette anılan ad, daha beşinci ayete gelinmeden kulluğu içinde taşır. Beşinci ayet bu adın sahibine doğrudan döner: {ar:إِيَّاكَ نَعْبُدُ, tr:iyyâke na'büdü, gloss:yalnız sana kulluk ederiz, source:1:5}. Sahip ile ona boyun eğen kulun sahnesi beşinci ayetin "na'büdü" kelimesiyle, dördüncü ayetin "mâlik" kelimesiyle kurulur. Bu ayet o sahneye kulluk edilenin adını verir.

[¶16] Bu ad yalnızca anılmaz, seslenmek için de kullanılır. Araplar bu adın en büyük ad olduğunu söylerlerdi: {ar:اسم الله الأكبر هو الله, tr:ismullâhi'l-ekberu hüvallâh, gloss:Allah'ın en büyük adı "Allah"tır, source:"ء ل ه,B002"}. Bu adla yakarırlar ({ar:يا ألله اغفر لي, tr:yâ allâhü'ğfir lî, gloss:ey Allah, beni bağışla, source:"ء ل ه,B002"}) ve yemin ederlerdi: {ar:الله ما فعلت ذاك تريد والله ما فعلته, tr:Allâhi mâ fealtü zâke, türîdü vallâhi mâ fealtüh, gloss:Allah'a andolsun bunu yapmadım, yani "vallahi yapmadım" demek istersin, source:"ء ل ه,B002"}. Kısaltılmış bir çağrı biçimi de vardı: {ar:اللهم بمعنى يا ألله, tr:Allâhümme bi-ma'nâ yâ Allâh, gloss:"Allâhümme", "ey Allah" anlamındadır, source:"ء ل ه,B002"}. Ad, onu ağzına alanı adın sahibine bağlar. Yakarana göre bir sığınaktır, yemin edene göre bir tanıktır. Kur'an bu bağı insanların birbirinden bir şey isterken başvurduğu bir ad olarak da gösterir. Bunu bir sonraki bölüm ele alır.

[¶17] Kur'an bu ayetin üç adını iki yerde aynı sırayla anar. Birincisinde tek ilah olmak, Rahman ve Rahim olmakla birleşir: {ar:وَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ, tr:ve ilâhüküm ilâhün vâhid, lâ ilâhe illâ hüve'r-rahmânü'r-rahîm, gloss:ilahınız tek bir ilahtır; O'ndan başka ilah yoktur; O Rahman'dır, Rahim'dir, source:2:163}. İkincisinde aynı adlar arasına görüneni ve görünmeyeni bilmek girer: {ar:هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ, tr:hüvallâhüllezî lâ ilâhe illâ hüv, âlimü'l-gaybi ve'ş-şehâdeh, hüve'r-rahmânü'r-rahîm, gloss:O, kendisinden başka ilah olmayan Allah'tır; görünmeyeni de görüneni de bilir; O Rahman'dır, Rahim'dir, source:59:22}. Kulluk edilenin kim olduğu sorulduğunda Kur'an'ın cevabı birinci ayetin iki sıfatıdır. Kulluk edilen, merhameti dolu ve merhametini yönelten olandır. Adlar ve kulluk bir ayette daha birlikte anılır: {ar:ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ, tr:Allâhü lâ ilâhe illâ hü, lehü'l-esmâü'l-hüsnâ, gloss:Allah, O'ndan başka ilah yoktur; en güzel adlar O'nundur, source:20:8}.

[¶18] Aynı ailede, bir kavim taptığı için güneşe verilmiş bir ad da vardır: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetü'ş-şems, sümmiyet bi-zâlike li-enne kavmen kânû ya'büdûnehâ, gloss:ilâhe güneştir; bir kavim ona taptığı için bu adı almıştır, source:"ء ل ه,B001"}. Bu ad, kendisine tapanların bakışından doğmuştur. Güneşe tapanların yoldan alıkonduğu sahne surenin bütününe aittir. Bu ayet o sahneye, tapınmanın adı bir şeye nasıl verilebiliyorsa ondan geri de alınabileceğini ekler. "Allah" adı da tapınma kelimesinden yalnız Yaratıcıya özgü kılınarak ayrılmıştır.

[¶19] Bazı dilciler bu adı, yoğun duygudan aklı karışmak anlamındaki başka bir köke bağlamayı da önermiştir. O kökte yavrusuna özlemi ağırlaşmış bir dişi deve vardır: {ar:ناقة واله إذا اشتد وجدها على ولدها, tr:nâkatün vâlihun izeştedde vecdühâ alâ veledihâ, gloss:yavrusuna duyduğu özlem ağırlaşan dişi deveye vâlih denir, source:"و ل ه,B001"}. Anneyi yavrusundan ayırmamak için şu söz söylenirdi: {ar:لا توله والدة عن ولدها, tr:lâ tüvellehu vâlidetün an veledihâ, gloss:hiçbir anne yavrusundan ayrılıp özleme düşürülmesin, source:"و ل ه,B002"}. Bu türetme bir öneri olarak kalır. Kur'an adı hep "ilâh" kelimesinin yanında anar. Ama bu görüntünün anlattığı anne ile yavru arasındaki bağ, ayetin son iki kelimesinde başka bir kökle, gerçekten kendi kökleriyle karşımıza çıkar.

## Rahmân ve Rahîm: taşan ve yönelen merhamet

[¶20] Ayetin son iki kelimesi aynı kökten gelir: {ar:والرحمن الرحيم مشتقان من الرحمة, tr:ve'r-rahmânü'r-rahîmü müştakkâni mine'r-rahme, gloss:Rahman ve Rahim, rahmetten türemiş iki addır, source:"ر ح م,B001"}. Kök aynıdır ama kalıplar farklıdır, iş bu farkta yatar. "Rahmân" kelimesinin kalıbı, Arapçada içi bir şeyle dolup taşan bir hali anlatır. Kur'an'da aynı kalıp Musa için kullanılır. Musa, kendisi yokken buzağıya tapan kavmine döner: {ar:وَلَمَّا رَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا, tr:ve lemmâ racea Mûsâ ilâ kavmihî gadbâne esifâ, gloss:Musa öfkeyle dolu ve üzgün olarak kavmine dönünce, source:7:150}. "Gadbân" öfkeyle dolu olan demektir. Levhaları yere bırakır ve kardeşinin başından tutup onu kendine çeker. "Rahmân" da merhametle dolu olandır. Bu yalnızca bir kalıp benzerliğidir, ama sure aynı kökü tersine çevrilmiş haliyle tanır: Yedinci ayetteki {ar:ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:el-mağdûbi aleyhim, gloss:gazaba uğramışlar, source:1:7} sözü, öfkenin yöneldiği kişileri anlatır. Sure merhametle dolu olanın adıyla başlar ve öfkenin yöneldiklerini anarak biter. Musa'nın sahnesinde de öfke merhamete dönüşür. Öfkesi dindiğinde Musa şöyle der: {ar:رَبِّ ٱغْفِرْ لِى وَلِأَخِى وَأَدْخِلْنَا فِى رَحْمَتِكَ ۖ وَأَنتَ أَرْحَمُ ٱلرَّٰحِمِينَ, tr:rabbi'ğfir lî ve li-ahî ve edhilnâ fî rahmetik, ve ente erhamü'r-râhimîn, gloss:Rabbim, beni ve kardeşimi bağışla, bizi rahmetinin içine al; sen merhamet edenlerin en merhametlisisin, source:7:151}.

[¶21] "Rahîm" kelimesinin kalıbı ise bir niteliğin sürekli olarak birine yöneldiğini anlatır. Kur'an bu kelimeyi bir insan için de kullanır. İnananlara içlerinden çıkmış bir elçinin geldiği söylenir. Onların sıkıntıya düşmesi ona ağır gelir ve şöyle nitelenir: {ar:بِٱلْمُؤْمِنِينَ رَءُوفٌۭ رَّحِيمٌۭ, tr:bi'l-mü'minîne raûfun rahîm, gloss:inananlara karşı çok şefkatli, çok merhametlidir, source:9:128}. Allah için de aynı yönelme söylenir: {ar:وَكَانَ بِٱلْمُؤْمِنِينَ رَحِيمًۭا, tr:ve kâne bi'l-mü'minîne rahîmâ, gloss:O inananlara karşı merhametlidir, source:33:43}. "Rahîm" bir yöne bakar ve ulaştığı birini gösterir. "Rahmân" ise Kur'an'da başka kimse için kullanılmaz ve çoğu zaman tek başına bir ad olarak durur. Bir sure yalnızca bu kelimeyle açılır: {ar:ٱلرَّحْمَٰنُ, tr:er-rahmân, gloss:Rahman, source:55:1}. Ardından gelen ilk iş bir öğretmedir: {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:alleme'l-kur'ân, gloss:Kur'an'ı öğretti, source:55:2}. Arşın üstünde bulunan da bu addır: {ar:ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ, tr:er-rahmânü ale'l-arşi'stevâ, gloss:Rahman arşa kurulmuştur, source:20:5}. Göklerde ve yerde olan herkes ona kul olarak gelecektir {source:19:93}. Bu ad, onu ilk duyanların takıldığı ad da olmuştur: {ar:وَإِذَا قِيلَ لَهُمُ ٱسْجُدُوا۟ لِلرَّحْمَٰنِ قَالُوا۟ وَمَا ٱلرَّحْمَٰنُ, tr:ve izâ kîle lehümü'scüdû li'r-rahmâni kâlû ve me'r-rahmân, gloss:onlara "Rahman'a secde edin" denince "Rahman da nedir" dediler, source:25:60}. Başka bir yerde Peygamberin, Rahman'ı inkâr eden bir topluluğa gönderildiği söylenir {source:13:30}.

[¶22] İki ad birlikte merhametin hem kaynağını hem de ulaştığı yeri gösterir: dolup taşan bir merhamet ve o merhametin tek tek insanlara yönelmesi. Merhametin genişliği de Kur'an'da söylenir. Musa kavmi için dünyada ve ahirette iyilik yazılmasını ister. Allah ona şöyle cevap verir: {ar:عَذَابِىٓ أُصِيبُ بِهِۦ مَنْ أَشَآءُ ۖ وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ, tr:azâbî usîbü bihî men eşâ', ve rahmetî vesiat külle şey', gloss:azabımı dilediğime ulaştırırım; rahmetim ise her şeyi kuşatmıştır, source:7:156}. Göklerde ve yerde olanların kime ait olduğu sorulur ve cevabın hemen ardından şu söylenir: {ar:كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ, tr:ketebe alâ nefsihi'r-rahme, gloss:rahmeti kendi üzerine yazdı, source:6:12}. Bu doluluk hesabı ortadan kaldırmaz. İbrahim putlara tapan babasına şöyle der: {ar:يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ, tr:yâ ebeti innî ehâfü en yemesseke azâbün mine'r-rahmân, gloss:babacığım, sana Rahman'dan bir azabın dokunmasından korkuyorum, source:19:45}. Azap bile Rahman adıyla anılır. Sure de bu iki adı ikinci ayetten sonra yeniden söyler ({ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:merhameti dolu, merhametini yönelten, source:1:3}) ve dördüncü ayette hesap gününe geçer. Hesap günü de bu iki adın gölgesinde anılır.

[¶23] Beşinci ayetin yardım isteyişi de bu adla buluşur. Peygamber, kendisini yalanlayanlar karşısında şöyle der: {ar:وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:ve rabbüne'r-rahmânü'l-müste'ânü alâ mâ tesifûn, gloss:Rabbimiz, anlattıklarınıza karşı yardımı istenen Rahman'dır, source:21:112}. "Müste'ân", surenin {ar:وَإِيَّاكَ نَسْتَعِينُ, tr:ve iyyâke neste'în, gloss:ve yalnız senden yardım isteriz, source:1:5} sözündeki fiille aynı köktendir. Yardım istenen, merhameti dolu olandır.

## Rahim: çocuğun evi ve içine girilen merhamet

[¶24] Kök kelime, bedenin içindeki bir yeri adlandırır: {ar:الرحم بيت منبت الولد ووعاؤه في البطن, tr:er-rahimu beytü menbiti'l-veledi ve vi'âühû fi'l-batn, gloss:rahim, karındaki çocuğun bittiği yer olan ev ve onun kabıdır, source:"ر ح م,B003"}. Bu ev, içindekinin isteyemediği her şeyi kendiliğinden verir. Çocuk kendini besleyemez, koruyamaz, bir şey isteyemez ve karşılığında bir şey ödeyemez. Rahim onu sarar, besler ve dışarıya hazır olana kadar içinde tutar. Kökün temel anlamı da bu sarışa uyar: {ar:أصل واحد يدل على الرقة والعطف والرأفة, tr:aslun vâhidun yedüllü ale'r-rikkati ve'l-atfi ve'r-ra'fe, gloss:incelik, şefkatle eğilme ve acıma bildiren tek bir köktür, source:"ر ح م,B001"}. Ama bu incelik bir duyguda kalmaz: {ar:الرحمة رقة تقتضي الإحسان إلى المرحوم, tr:er-rahmetü rikkatün tektedi'l-ihsâne ile'l-merhûm, gloss:rahmet, merhamet edilene iyilik etmeyi gerektiren bir inceliktir, source:"ر ح م,B001"}. Bu iyilik özellikle güçsüze yönelir: {ar:رحمة الضعيف والتعطف عليه, tr:rahmetü'd-da'îfi ve't-teattufu aleyh, gloss:güçsüze acımak ve ona şefkatle eğilmek, source:"ر ح م,B001"}. Bu evin bir bedeli de vardır. Araplar doğurduktan sonra rahminin ağrısını çeken dişi deveye bir ad verirlerdi: {ar:الرحوم الناقة التي تشتكي رحمها بعد النتاج, tr:er-rahûmu'n-nâkatü'lletî teştekî rahimehâ ba'de'n-nitâc, gloss:rahûm, doğurduktan sonra rahminden acı çeken dişi devedir, source:"ر ح م,B004"}. Taşıyan ev, taşıdığının ağrısını kendi bedeninde çeker.

[¶25] Türkçede "rahim" kelimesi hâlâ döl yatağı anlamındadır. Ama bu ayeti okuyan kulak "Rahîm" adında onu pek duymaz. "Rahmet" ise Türkçede daralmıştır. Daha çok yağmur için ("rahmet yağdı") ve ölüler için ("rahmetli") söylenir. Arapçada ise kelime çocuğun evini, iyiliğe dönüşen inceliği ve güçsüze eğilmeyi birlikte taşır. Yağmur anlamı bile Kur'an'dan uzak değildir. Rüzgârlar, ağır bulutları ölü bir toprağa sürmeden önce "rahmetinin önünden" müjdeci olarak gönderilir {source:7:57}. Toprağın ölümünden sonra dirilmesine bakılması istenir: {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak: toprağı ölümünden sonra nasıl diriltiyor, source:30:50}. Türkçe yağmuru korumuş, rahimi unutmuştur.

[¶26] Aynı kelime akrabalığı da anlatır. Bu anlamın kaynağı açıkça söylenir: {ar:استعير الرحم للقرابة لكونهم خارجين من رحم واحدة, tr:üstüîre'r-rahimu li'l-karâbeti li-kevnihim hâricîne min rahimin vâhide, gloss:rahim kelimesi akrabalık için ödünç alındı, çünkü akrabalar tek bir rahimden çıkmıştır, source:"ر ح م,B002"}. Kur'an Allah'ın adını ve rahimleri tek bir emirde yan yana getirir. İnsanlara tek bir candan yaratıldıkları, eşlerinin de o candan yaratıldığı ve bu ikisinden birçok erkek ve kadının yayıldığı hatırlatılır. Ardından şöyle denir: {ar:وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ, tr:vettekullâhellezî tesâelûne bihî ve'l-erhâm, gloss:adını anarak birbirinizden bir şey istediğiniz Allah'tan ve rahimlerden sakının, source:4:1}. İnsanlar birbirinden bir şey isterken bu adı ortaya koyarlar. Ayet, aynı saygıyı onları birbirine bağlayan rahimlere de ister. Birinci ayet de bu iki şeyi bir arada söyler: Allah'ın adını ve rahim kökünden gelen iki sıfatı. Rahimlerin bu bağını kesmek bozgunculukla birlikte anılır {source:47:22}. Rahimde biçim veren de O'dur: {ar:هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ, tr:hüvellezî yusavvirukum fi'l-erhâmi keyfe yeşâ', lâ ilâhe illâ hüv, gloss:sizi rahimlerde dilediği gibi biçimlendiren O'dur; O'ndan başka ilah yoktur, source:3:6}.

[¶27] Kur'an merhameti, rahim gibi içine girilen bir yer olarak da anlatır. Musa'nın yakarışı {ar:وَأَدْخِلْنَا فِى رَحْمَتِكَ, tr:ve edhilnâ fî rahmetik, gloss:bizi rahmetinin içine al, source:7:151} sözüyle bunu söyler. Nuh'un tufanında korunan da yalnızca merhamet edilen kişidir {source:11:43}. Rahim görüntüsü burada kendi kökünün içinden konuşur. Merhamet, güçsüzü içine alan, onu besleyip koruyan ve bunun bedelini kendisi taşıyan bir evdir. "Rahmân" bu evin taşan doluluğudur, "Rahîm" ise bu evin tek tek içindekilere eğilmesidir. Rahimden çıkanı halden hale büyütmek, ikinci ayetteki "Rab" kelimesinin taşıdığı bir sahnedir. Merhametin dönüştüğü iyiliğin adı da yedinci ayetteki "en'amte" kelimesinde geçer. Birinci ayet bu iki sahneye kaynaklarını, yani evi ve inceliği verir.

===== _commentary/v16/out/1_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: "bi" carries both accompaniment and instrument senses
- memory: fa'lân pattern (rahmân, ghadbân) denotes a full, overflowing state; fa'îl a lasting quality directed at someone
- memory: plural asmâ' fits the s-m-w root rather than w-s-m
- memory: rahmân is used in the Quran for God alone
- memory: the w-s-m derivation of ism was proposed by some grammarians (per dictionary note, unnamed in prose)
- not written: س م و B003 stallion leaping into the she-camels - no bearing on the name or the opening act
- not written: س م و B006 going out to hunt / hunters - only a pun beside 5:4's naming over the catch, no supported theme
- not written: و س م B005 beauty, B006 dye plant - add nothing to the mark or the name
- not written: و ل ه B003 water lost in the desert - irrelevant even to the proposed derivation
- not written: Musa's mother separated from her child (28:7-13) as a tawlîh scene - it hangs on a minority derivation; the terbiye scene belongs to the second ayah
- not written: ر ح م B004 other forms (sheep with a swollen womb) - the rahûm she-camel already covers the image

===== passages not cited (246) =====
## strong (this ayah's own list) (7)

- (2:163) [listed for 1:1] [cited in ¶17] وَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (7:156) [listed for 1:1] [cited in ¶22] ۞ وَٱكْتُبْ لَنَا فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ إِنَّا هُدْنَآ إِلَيْكَ ۚ قَالَ عَذَابِىٓ أُصِيبُ بِهِۦ مَنْ أَشَآءُ ۖ وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ ۚ فَسَأَكْتُبُهَا لِلَّذِينَ يَتَّقُونَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَٱلَّذِينَ هُم بِـَٔايَٰتِنَا يُؤْمِنُونَ
- (12:40) [listed for 1:1] [cited in ¶11] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (20:90) [listed for 1:1] وَلَقَدْ قَالَ لَهُمْ هَٰرُونُ مِن قَبْلُ يَٰقَوْمِ إِنَّمَا فُتِنتُم بِهِۦ ۖ وَإِنَّ رَبَّكُمُ ٱلرَّحْمَٰنُ فَٱتَّبِعُونِى وَأَطِيعُوٓا۟ أَمْرِى
- (21:112) [listed for 1:1] [cited in ¶23] قَٰلَ رَبِّ ٱحْكُم بِٱلْحَقِّ ۗ وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (27:30) [listed for 1:1] [cited in ¶13] إِنَّهُۥ مِن سُلَيْمَٰنَ وَإِنَّهُۥ بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (43:45) [listed for 1:1] وَسْـَٔلْ مَنْ أَرْسَلْنَا مِن قَبْلِكَ مِن رُّسُلِنَآ أَجَعَلْنَا مِن دُونِ ٱلرَّحْمَٰنِ ءَالِهَةًۭ يُعْبَدُونَ

## medium (this ayah's own list) (27)

- (6:12) [listed for 1:1] [cited in ¶22] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
- (6:54) [listed for 1:1] وَإِذَا جَآءَكَ ٱلَّذِينَ يُؤْمِنُونَ بِـَٔايَٰتِنَا فَقُلْ سَلَٰمٌ عَلَيْكُمْ ۖ كَتَبَ رَبُّكُمْ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۖ أَنَّهُۥ مَنْ عَمِلَ مِنكُمْ سُوٓءًۢا بِجَهَٰلَةٍۢ ثُمَّ تَابَ مِنۢ بَعْدِهِۦ وَأَصْلَحَ فَأَنَّهُۥ غَفُورٌۭ رَّحِيمٌۭ
- (6:118) [listed for 1:1] [cited in ¶4] فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ إِن كُنتُم بِـَٔايَٰتِهِۦ مُؤْمِنِينَ
- (7:56) [listed for 1:1] وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا وَٱدْعُوهُ خَوْفًۭا وَطَمَعًا ۚ إِنَّ رَحْمَتَ ٱللَّهِ قَرِيبٌۭ مِّنَ ٱلْمُحْسِنِينَ
- (7:180) [listed for 1:1] [cited in ¶10] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
- (11:41) [listed for 1:1] [cited in ¶3] ۞ وَقَالَ ٱرْكَبُوا۟ فِيهَا بِسْمِ ٱللَّهِ مَجْر۪ىٰهَا وَمُرْسَىٰهَآ ۚ إِنَّ رَبِّى لَغَفُورٌۭ رَّحِيمٌۭ
- (17:110) [listed for 1:1] [cited in ¶10] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (19:18) [listed for 1:1] قَالَتْ إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ إِن كُنتَ تَقِيًّۭا
- (19:44) [listed for 1:1] يَٰٓأَبَتِ لَا تَعْبُدِ ٱلشَّيْطَٰنَ ۖ إِنَّ ٱلشَّيْطَٰنَ كَانَ لِلرَّحْمَٰنِ عَصِيًّۭا
- (19:45) [listed for 1:1] [cited in ¶22] يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ فَتَكُونَ لِلشَّيْطَٰنِ وَلِيًّۭا
- (19:65) [listed for 1:1] [cited in ¶9] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:5) [listed for 1:1] [cited in ¶21] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:8) [listed for 1:1] [cited in ¶17] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (24:22) [listed for 1:1] وَلَا يَأْتَلِ أُو۟لُوا۟ ٱلْفَضْلِ مِنكُمْ وَٱلسَّعَةِ أَن يُؤْتُوٓا۟ أُو۟لِى ٱلْقُرْبَىٰ وَٱلْمَسَٰكِينَ وَٱلْمُهَٰجِرِينَ فِى سَبِيلِ ٱللَّهِ ۖ وَلْيَعْفُوا۟ وَلْيَصْفَحُوٓا۟ ۗ أَلَا تُحِبُّونَ أَن يَغْفِرَ ٱللَّهُ لَكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌ
- (25:63) [listed for 1:1] وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا وَإِذَا خَاطَبَهُمُ ٱلْجَٰهِلُونَ قَالُوا۟ سَلَٰمًۭا
- (36:11) [listed for 1:1] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
- (36:23) [listed for 1:1] ءَأَتَّخِذُ مِن دُونِهِۦٓ ءَالِهَةً إِن يُرِدْنِ ٱلرَّحْمَٰنُ بِضُرٍّۢ لَّا تُغْنِ عَنِّى شَفَٰعَتُهُمْ شَيْـًۭٔا وَلَا يُنقِذُونِ
- (37:118) [listed for 1:1] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (37:182) [listed for 1:1] وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (39:11) [listed for 1:1] قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (39:64) [listed for 1:1] قُلْ أَفَغَيْرَ ٱللَّهِ تَأْمُرُوٓنِّىٓ أَعْبُدُ أَيُّهَا ٱلْجَٰهِلُونَ
- (41:2) [listed for 1:1] تَنزِيلٌۭ مِّنَ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (43:36) [listed for 1:1] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (59:22) [listed for 1:1] [cited in ¶17] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (67:29) [listed for 1:1] قُلْ هُوَ ٱلرَّحْمَٰنُ ءَامَنَّا بِهِۦ وَعَلَيْهِ تَوَكَّلْنَا ۖ فَسَتَعْلَمُونَ مَنْ هُوَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (73:8) [listed for 1:1] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
- (109:6) [listed for 1:1] لَكُمْ دِينُكُمْ وَلِىَ دِينِ

## named by the passage's own list as strong for this ayah (1)

- (15:87) [listed for 1:1] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ

## named by the passage's own list as medium for this ayah (3)

- (26:9) [listed for 1:1] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (55:1) [listed for 1:1] [cited in ¶21] ٱلرَّحْمَٰنُ
- (95:8) [listed for 1:1] أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ

## weak (this ayah's own list) (63)

- (2:37) [listed for 1:1] فَتَلَقَّىٰٓ ءَادَمُ مِن رَّبِّهِۦ كَلِمَٰتٍۢ فَتَابَ عَلَيْهِ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:54) [listed for 1:1] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ إِنَّكُمْ ظَلَمْتُمْ أَنفُسَكُم بِٱتِّخَاذِكُمُ ٱلْعِجْلَ فَتُوبُوٓا۟ إِلَىٰ بَارِئِكُمْ فَٱقْتُلُوٓا۟ أَنفُسَكُمْ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ عِندَ بَارِئِكُمْ فَتَابَ عَلَيْكُمْ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:64) [listed for 1:1] ثُمَّ تَوَلَّيْتُم مِّنۢ بَعْدِ ذَٰلِكَ ۖ فَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ لَكُنتُم مِّنَ ٱلْخَٰسِرِينَ
- (2:105) [listed for 1:1] مَّا يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَلَا ٱلْمُشْرِكِينَ أَن يُنَزَّلَ عَلَيْكُم مِّنْ خَيْرٍۢ مِّن رَّبِّكُمْ ۗ وَٱللَّهُ يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (2:128) [listed for 1:1] رَبَّنَا وَٱجْعَلْنَا مُسْلِمَيْنِ لَكَ وَمِن ذُرِّيَّتِنَآ أُمَّةًۭ مُّسْلِمَةًۭ لَّكَ وَأَرِنَا مَنَاسِكَنَا وَتُبْ عَلَيْنَآ ۖ إِنَّكَ أَنتَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:143) [listed for 1:1] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
- (2:160) [listed for 1:1] إِلَّا ٱلَّذِينَ تَابُوا۟ وَأَصْلَحُوا۟ وَبَيَّنُوا۟ فَأُو۟لَٰٓئِكَ أَتُوبُ عَلَيْهِمْ ۚ وَأَنَا ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:173) [listed for 1:1] إِنَّمَا حَرَّمَ عَلَيْكُمُ ٱلْمَيْتَةَ وَٱلدَّمَ وَلَحْمَ ٱلْخِنزِيرِ وَمَآ أُهِلَّ بِهِۦ لِغَيْرِ ٱللَّهِ ۖ فَمَنِ ٱضْطُرَّ غَيْرَ بَاغٍۢ وَلَا عَادٍۢ فَلَآ إِثْمَ عَلَيْهِ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ
- (2:182) [listed for 1:1] فَمَنْ خَافَ مِن مُّوصٍۢ جَنَفًا أَوْ إِثْمًۭا فَأَصْلَحَ بَيْنَهُمْ فَلَآ إِثْمَ عَلَيْهِ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:192) [listed for 1:1] فَإِنِ ٱنتَهَوْا۟ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:199) [listed for 1:1] ثُمَّ أَفِيضُوا۟ مِنْ حَيْثُ أَفَاضَ ٱلنَّاسُ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:207) [listed for 1:1] وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
- (3:129) [listed for 1:1] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ يَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (5:54) [listed for 1:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَن يَرْتَدَّ مِنكُمْ عَن دِينِهِۦ فَسَوْفَ يَأْتِى ٱللَّهُ بِقَوْمٍۢ يُحِبُّهُمْ وَيُحِبُّونَهُۥٓ أَذِلَّةٍ عَلَى ٱلْمُؤْمِنِينَ أَعِزَّةٍ عَلَى ٱلْكَٰفِرِينَ يُجَٰهِدُونَ فِى سَبِيلِ ٱللَّهِ وَلَا يَخَافُونَ لَوْمَةَ لَآئِمٍۢ ۚ ذَٰلِكَ فَضْلُ ٱللَّهِ يُؤْتِيهِ مَن يَشَآءُ ۚ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
- (9:104) [listed for 1:1] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ هُوَ يَقْبَلُ ٱلتَّوْبَةَ عَنْ عِبَادِهِۦ وَيَأْخُذُ ٱلصَّدَقَٰتِ وَأَنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (9:118) [listed for 1:1] وَعَلَى ٱلثَّلَٰثَةِ ٱلَّذِينَ خُلِّفُوا۟ حَتَّىٰٓ إِذَا ضَاقَتْ عَلَيْهِمُ ٱلْأَرْضُ بِمَا رَحُبَتْ وَضَاقَتْ عَلَيْهِمْ أَنفُسُهُمْ وَظَنُّوٓا۟ أَن لَّا مَلْجَأَ مِنَ ٱللَّهِ إِلَّآ إِلَيْهِ ثُمَّ تَابَ عَلَيْهِمْ لِيَتُوبُوٓا۟ ۚ إِنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (10:107) [listed for 1:1] وَإِن يَمْسَسْكَ ٱللَّهُ بِضُرٍّۢ فَلَا كَاشِفَ لَهُۥٓ إِلَّا هُوَ ۖ وَإِن يُرِدْكَ بِخَيْرٍۢ فَلَا رَآدَّ لِفَضْلِهِۦ ۚ يُصِيبُ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۚ وَهُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (12:98) [listed for 1:1] قَالَ سَوْفَ أَسْتَغْفِرُ لَكُمْ رَبِّىٓ ۖ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (15:49) [listed for 1:1] ۞ نَبِّئْ عِبَادِىٓ أَنِّىٓ أَنَا ٱلْغَفُورُ ٱلرَّحِيمُ
- (19:7) [listed for 1:1] يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا
- (19:58) [listed for 1:1] أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ مِن ذُرِّيَّةِ ءَادَمَ وَمِمَّنْ حَمَلْنَا مَعَ نُوحٍۢ وَمِن ذُرِّيَّةِ إِبْرَٰهِيمَ وَإِسْرَٰٓءِيلَ وَمِمَّنْ هَدَيْنَا وَٱجْتَبَيْنَآ ۚ إِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُ ٱلرَّحْمَٰنِ خَرُّوا۟ سُجَّدًۭا وَبُكِيًّۭا ۩
- (19:85) [listed for 1:1] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
- (19:88) [listed for 1:1] وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا
- (19:93) [listed for 1:1] [cited in ¶21] إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا
- (21:42) [listed for 1:1] قُلْ مَن يَكْلَؤُكُم بِٱلَّيْلِ وَٱلنَّهَارِ مِنَ ٱلرَّحْمَٰنِ ۗ بَلْ هُمْ عَن ذِكْرِ رَبِّهِم مُّعْرِضُونَ
- (22:65) [listed for 1:1] أَلَمْ تَرَ أَنَّ ٱللَّهَ سَخَّرَ لَكُم مَّا فِى ٱلْأَرْضِ وَٱلْفُلْكَ تَجْرِى فِى ٱلْبَحْرِ بِأَمْرِهِۦ وَيُمْسِكُ ٱلسَّمَآءَ أَن تَقَعَ عَلَى ٱلْأَرْضِ إِلَّا بِإِذْنِهِۦٓ ۗ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
- (23:75) [listed for 1:1] ۞ وَلَوْ رَحِمْنَٰهُمْ وَكَشَفْنَا مَا بِهِم مِّن ضُرٍّۢ لَّلَجُّوا۟ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (24:7) [listed for 1:1] وَٱلْخَٰمِسَةُ أَنَّ لَعْنَتَ ٱللَّهِ عَلَيْهِ إِن كَانَ مِنَ ٱلْكَٰذِبِينَ
- (24:9) [listed for 1:1] وَٱلْخَٰمِسَةَ أَنَّ غَضَبَ ٱللَّهِ عَلَيْهَآ إِن كَانَ مِنَ ٱلصَّٰدِقِينَ
- (25:6) [listed for 1:1] قُلْ أَنزَلَهُ ٱلَّذِى يَعْلَمُ ٱلسِّرَّ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ كَانَ غَفُورًۭا رَّحِيمًۭا
- (25:48) [listed for 1:1] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
- (25:59) [listed for 1:1] ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ ٱلرَّحْمَٰنُ فَسْـَٔلْ بِهِۦ خَبِيرًۭا
- (25:60) [listed for 1:1] [cited in ¶21] وَإِذَا قِيلَ لَهُمُ ٱسْجُدُوا۟ لِلرَّحْمَٰنِ قَالُوا۟ وَمَا ٱلرَّحْمَٰنُ أَنَسْجُدُ لِمَا تَأْمُرُنَا وَزَادَهُمْ نُفُورًۭا ۩
- (26:5) [listed for 1:1] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
- (26:104) [listed for 1:1] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:217) [listed for 1:1] وَتَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ
- (29:21) [listed for 1:1] يُعَذِّبُ مَن يَشَآءُ وَيَرْحَمُ مَن يَشَآءُ ۖ وَإِلَيْهِ تُقْلَبُونَ
- (30:5) [listed for 1:1] بِنَصْرِ ٱللَّهِ ۚ يَنصُرُ مَن يَشَآءُ ۖ وَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (32:6) [listed for 1:1] ذَٰلِكَ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (34:2) [listed for 1:1] يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۚ وَهُوَ ٱلرَّحِيمُ ٱلْغَفُورُ
- (36:5) [listed for 1:1] تَنزِيلَ ٱلْعَزِيزِ ٱلرَّحِيمِ
- (36:58) [listed for 1:1] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (39:38) [listed for 1:1] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلْ أَفَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ إِنْ أَرَادَنِىَ ٱللَّهُ بِضُرٍّ هَلْ هُنَّ كَٰشِفَٰتُ ضُرِّهِۦٓ أَوْ أَرَادَنِى بِرَحْمَةٍ هَلْ هُنَّ مُمْسِكَٰتُ رَحْمَتِهِۦ ۚ قُلْ حَسْبِىَ ٱللَّهُ ۖ عَلَيْهِ يَتَوَكَّلُ ٱلْمُتَوَكِّلُونَ
- (39:53) [listed for 1:1] ۞ قُلْ يَٰعِبَادِىَ ٱلَّذِينَ أَسْرَفُوا۟ عَلَىٰٓ أَنفُسِهِمْ لَا تَقْنَطُوا۟ مِن رَّحْمَةِ ٱللَّهِ ۚ إِنَّ ٱللَّهَ يَغْفِرُ ٱلذُّنُوبَ جَمِيعًا ۚ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (42:5) [listed for 1:1] تَكَادُ ٱلسَّمَٰوَٰتُ يَتَفَطَّرْنَ مِن فَوْقِهِنَّ ۚ وَٱلْمَلَٰٓئِكَةُ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ وَيَسْتَغْفِرُونَ لِمَن فِى ٱلْأَرْضِ ۗ أَلَآ إِنَّ ٱللَّهَ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (43:20) [listed for 1:1] وَقَالُوا۟ لَوْ شَآءَ ٱلرَّحْمَٰنُ مَا عَبَدْنَٰهُم ۗ مَّا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَخْرُصُونَ
- (43:81) [listed for 1:1] قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ
- (44:42) [listed for 1:1] إِلَّا مَن رَّحِمَ ٱللَّهُ ۚ إِنَّهُۥ هُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (46:8) [listed for 1:1] أَمْ يَقُولُونَ ٱفْتَرَىٰهُ ۖ قُلْ إِنِ ٱفْتَرَيْتُهُۥ فَلَا تَمْلِكُونَ لِى مِنَ ٱللَّهِ شَيْـًٔا ۖ هُوَ أَعْلَمُ بِمَا تُفِيضُونَ فِيهِ ۖ كَفَىٰ بِهِۦ شَهِيدًۢا بَيْنِى وَبَيْنَكُمْ ۖ وَهُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (48:14) [listed for 1:1] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ يَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۚ وَكَانَ ٱللَّهُ غَفُورًۭا رَّحِيمًۭا
- (49:8) [listed for 1:1] فَضْلًۭا مِّنَ ٱللَّهِ وَنِعْمَةًۭ ۚ وَٱللَّهُ عَلِيمٌ حَكِيمٌۭ
- (50:33) [listed for 1:1] مَّنْ خَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ وَجَآءَ بِقَلْبٍۢ مُّنِيبٍ
- (55:78) [listed for 1:1] [cited in ¶7] تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (61:14) [listed for 1:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوٓا۟ أَنصَارَ ٱللَّهِ كَمَا قَالَ عِيسَى ٱبْنُ مَرْيَمَ لِلْحَوَارِيِّۦنَ مَنْ أَنصَارِىٓ إِلَى ٱللَّهِ ۖ قَالَ ٱلْحَوَارِيُّونَ نَحْنُ أَنصَارُ ٱللَّهِ ۖ فَـَٔامَنَت طَّآئِفَةٌۭ مِّنۢ بَنِىٓ إِسْرَٰٓءِيلَ وَكَفَرَت طَّآئِفَةٌۭ ۖ فَأَيَّدْنَا ٱلَّذِينَ ءَامَنُوا۟ عَلَىٰ عَدُوِّهِمْ فَأَصْبَحُوا۟ ظَٰهِرِينَ
- (67:3) [listed for 1:1] ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ ۖ فَٱرْجِعِ ٱلْبَصَرَ هَلْ تَرَىٰ مِن فُطُورٍۢ
- (67:20) [listed for 1:1] أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- (67:28) [listed for 1:1] قُلْ أَرَءَيْتُمْ إِنْ أَهْلَكَنِىَ ٱللَّهُ وَمَن مَّعِىَ أَوْ رَحِمَنَا فَمَن يُجِيرُ ٱلْكَٰفِرِينَ مِنْ عَذَابٍ أَلِيمٍۢ
- (70:3) [listed for 1:1] مِّنَ ٱللَّهِ ذِى ٱلْمَعَارِجِ
- (73:9) [listed for 1:1] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (78:37) [listed for 1:1] رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا
- (78:38) [listed for 1:1] يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا ۖ لَّا يَتَكَلَّمُونَ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَقَالَ صَوَابًۭا
- (93:11) [listed for 1:1] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (112:2) [listed for 1:1] ٱللَّهُ ٱلصَّمَدُ

## named by the passage's own list as weak for this ayah (1)

- (3:74) [listed for 1:1] يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۗ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ

## neighbours: within two ayat of a passage the commentary cites (144)

- (2:29) [next to 2:31] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (2:30) [next to 2:31] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى جَاعِلٌۭ فِى ٱلْأَرْضِ خَلِيفَةًۭ ۖ قَالُوٓا۟ أَتَجْعَلُ فِيهَا مَن يُفْسِدُ فِيهَا وَيَسْفِكُ ٱلدِّمَآءَ وَنَحْنُ نُسَبِّحُ بِحَمْدِكَ وَنُقَدِّسُ لَكَ ۖ قَالَ إِنِّىٓ أَعْلَمُ مَا لَا تَعْلَمُونَ
- (2:32) [next to 2:31] قَالُوا۟ سُبْحَٰنَكَ لَا عِلْمَ لَنَآ إِلَّا مَا عَلَّمْتَنَآ ۖ إِنَّكَ أَنتَ ٱلْعَلِيمُ ٱلْحَكِيمُ
- (2:33) [next to 2:31] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
- (2:161) [next to 2:163] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَمَاتُوا۟ وَهُمْ كُفَّارٌ أُو۟لَٰٓئِكَ عَلَيْهِمْ لَعْنَةُ ٱللَّهِ وَٱلْمَلَٰٓئِكَةِ وَٱلنَّاسِ أَجْمَعِينَ
- (2:162) [next to 2:163] خَٰلِدِينَ فِيهَا ۖ لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (2:164) [next to 2:163] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (2:165) [next to 2:163] وَمِنَ ٱلنَّاسِ مَن يَتَّخِذُ مِن دُونِ ٱللَّهِ أَندَادًۭا يُحِبُّونَهُمْ كَحُبِّ ٱللَّهِ ۖ وَٱلَّذِينَ ءَامَنُوٓا۟ أَشَدُّ حُبًّۭا لِّلَّهِ ۗ وَلَوْ يَرَى ٱلَّذِينَ ظَلَمُوٓا۟ إِذْ يَرَوْنَ ٱلْعَذَابَ أَنَّ ٱلْقُوَّةَ لِلَّهِ جَمِيعًۭا وَأَنَّ ٱللَّهَ شَدِيدُ ٱلْعَذَابِ
- (3:4) [next to 3:6] مِن قَبْلُ هُدًۭى لِّلنَّاسِ وَأَنزَلَ ٱلْفُرْقَانَ ۗ إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
- (3:5) [next to 3:6] إِنَّ ٱللَّهَ لَا يَخْفَىٰ عَلَيْهِ شَىْءٌۭ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (3:7) [next to 3:6] هُوَ ٱلَّذِىٓ أَنزَلَ عَلَيْكَ ٱلْكِتَٰبَ مِنْهُ ءَايَٰتٌۭ مُّحْكَمَٰتٌ هُنَّ أُمُّ ٱلْكِتَٰبِ وَأُخَرُ مُتَشَٰبِهَٰتٌۭ ۖ فَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِمْ زَيْغٌۭ فَيَتَّبِعُونَ مَا تَشَٰبَهَ مِنْهُ ٱبْتِغَآءَ ٱلْفِتْنَةِ وَٱبْتِغَآءَ تَأْوِيلِهِۦ ۗ وَمَا يَعْلَمُ تَأْوِيلَهُۥٓ إِلَّا ٱللَّهُ ۗ وَٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ يَقُولُونَ ءَامَنَّا بِهِۦ كُلٌّۭ مِّنْ عِندِ رَبِّنَا ۗ وَمَا يَذَّكَّرُ إِلَّآ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (3:8) [next to 3:6] رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ ٱلْوَهَّابُ
- (4:0) [next to 4:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (4:2) [next to 4:1] وَءَاتُوا۟ ٱلْيَتَٰمَىٰٓ أَمْوَٰلَهُمْ ۖ وَلَا تَتَبَدَّلُوا۟ ٱلْخَبِيثَ بِٱلطَّيِّبِ ۖ وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ ۚ إِنَّهُۥ كَانَ حُوبًۭا كَبِيرًۭا
- (4:3) [next to 4:1] وَإِنْ خِفْتُمْ أَلَّا تُقْسِطُوا۟ فِى ٱلْيَتَٰمَىٰ فَٱنكِحُوا۟ مَا طَابَ لَكُم مِّنَ ٱلنِّسَآءِ مَثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ ۖ فَإِنْ خِفْتُمْ أَلَّا تَعْدِلُوا۟ فَوَٰحِدَةً أَوْ مَا مَلَكَتْ أَيْمَٰنُكُمْ ۚ ذَٰلِكَ أَدْنَىٰٓ أَلَّا تَعُولُوا۟
- (5:2) [next to 5:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (5:3) [next to 5:4] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (5:5) [next to 5:4] ٱلْيَوْمَ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۖ وَطَعَامُ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ حِلٌّۭ لَّكُمْ وَطَعَامُكُمْ حِلٌّۭ لَّهُمْ ۖ وَٱلْمُحْصَنَٰتُ مِنَ ٱلْمُؤْمِنَٰتِ وَٱلْمُحْصَنَٰتُ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ إِذَآ ءَاتَيْتُمُوهُنَّ أُجُورَهُنَّ مُحْصِنِينَ غَيْرَ مُسَٰفِحِينَ وَلَا مُتَّخِذِىٓ أَخْدَانٍۢ ۗ وَمَن يَكْفُرْ بِٱلْإِيمَٰنِ فَقَدْ حَبِطَ عَمَلُهُۥ وَهُوَ فِى ٱلْءَاخِرَةِ مِنَ ٱلْخَٰسِرِينَ
- (5:6) [next to 5:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (6:10) [next to 6:12] وَلَقَدِ ٱسْتُهْزِئَ بِرُسُلٍۢ مِّن قَبْلِكَ فَحَاقَ بِٱلَّذِينَ سَخِرُوا۟ مِنْهُم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (6:11) [next to 6:12] قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ ثُمَّ ٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (6:13) [next to 6:12] ۞ وَلَهُۥ مَا سَكَنَ فِى ٱلَّيْلِ وَٱلنَّهَارِ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:14) [next to 6:12] قُلْ أَغَيْرَ ٱللَّهِ أَتَّخِذُ وَلِيًّۭا فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ ۗ قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَكُونَ أَوَّلَ مَنْ أَسْلَمَ ۖ وَلَا تَكُونَنَّ مِنَ ٱلْمُشْرِكِينَ
- (6:75) [next to 6:77] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (6:76) [next to 6:77] فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ
- (6:78) [next to 6:77] فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ ۖ فَلَمَّآ أَفَلَتْ قَالَ يَٰقَوْمِ إِنِّى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:79) [next to 6:77] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (6:116) [next to 6:118] وَإِن تُطِعْ أَكْثَرَ مَن فِى ٱلْأَرْضِ يُضِلُّوكَ عَن سَبِيلِ ٱللَّهِ ۚ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ وَإِنْ هُمْ إِلَّا يَخْرُصُونَ
- (6:117) [next to 6:118] إِنَّ رَبَّكَ هُوَ أَعْلَمُ مَن يَضِلُّ عَن سَبِيلِهِۦ ۖ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (6:119) [next to 6:118] وَمَا لَكُمْ أَلَّا تَأْكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ وَقَدْ فَصَّلَ لَكُم مَّا حَرَّمَ عَلَيْكُمْ إِلَّا مَا ٱضْطُرِرْتُمْ إِلَيْهِ ۗ وَإِنَّ كَثِيرًۭا لَّيُضِلُّونَ بِأَهْوَآئِهِم بِغَيْرِ عِلْمٍ ۗ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِٱلْمُعْتَدِينَ
- (6:120) [next to 6:118] وَذَرُوا۟ ظَٰهِرَ ٱلْإِثْمِ وَبَاطِنَهُۥٓ ۚ إِنَّ ٱلَّذِينَ يَكْسِبُونَ ٱلْإِثْمَ سَيُجْزَوْنَ بِمَا كَانُوا۟ يَقْتَرِفُونَ
- (6:122) [next to 6:121] أَوَمَن كَانَ مَيْتًۭا فَأَحْيَيْنَٰهُ وَجَعَلْنَا لَهُۥ نُورًۭا يَمْشِى بِهِۦ فِى ٱلنَّاسِ كَمَن مَّثَلُهُۥ فِى ٱلظُّلُمَٰتِ لَيْسَ بِخَارِجٍۢ مِّنْهَا ۚ كَذَٰلِكَ زُيِّنَ لِلْكَٰفِرِينَ مَا كَانُوا۟ يَعْمَلُونَ
- (6:123) [next to 6:121] وَكَذَٰلِكَ جَعَلْنَا فِى كُلِّ قَرْيَةٍ أَكَٰبِرَ مُجْرِمِيهَا لِيَمْكُرُوا۟ فِيهَا ۖ وَمَا يَمْكُرُونَ إِلَّا بِأَنفُسِهِمْ وَمَا يَشْعُرُونَ
- (7:55) [next to 7:57] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (7:58) [next to 7:57] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
- (7:59) [next to 7:57] لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (7:148) [next to 7:150] وَٱتَّخَذَ قَوْمُ مُوسَىٰ مِنۢ بَعْدِهِۦ مِنْ حُلِيِّهِمْ عِجْلًۭا جَسَدًۭا لَّهُۥ خُوَارٌ ۚ أَلَمْ يَرَوْا۟ أَنَّهُۥ لَا يُكَلِّمُهُمْ وَلَا يَهْدِيهِمْ سَبِيلًا ۘ ٱتَّخَذُوهُ وَكَانُوا۟ ظَٰلِمِينَ
- (7:149) [next to 7:150] وَلَمَّا سُقِطَ فِىٓ أَيْدِيهِمْ وَرَأَوْا۟ أَنَّهُمْ قَدْ ضَلُّوا۟ قَالُوا۟ لَئِن لَّمْ يَرْحَمْنَا رَبُّنَا وَيَغْفِرْ لَنَا لَنَكُونَنَّ مِنَ ٱلْخَٰسِرِينَ
- (7:152) [next to 7:150] إِنَّ ٱلَّذِينَ ٱتَّخَذُوا۟ ٱلْعِجْلَ سَيَنَالُهُمْ غَضَبٌۭ مِّن رَّبِّهِمْ وَذِلَّةٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُفْتَرِينَ
- (7:153) [next to 7:151] وَٱلَّذِينَ عَمِلُوا۟ ٱلسَّيِّـَٔاتِ ثُمَّ تَابُوا۟ مِنۢ بَعْدِهَا وَءَامَنُوٓا۟ إِنَّ رَبَّكَ مِنۢ بَعْدِهَا لَغَفُورٌۭ رَّحِيمٌۭ
- (7:154) [next to 7:156] وَلَمَّا سَكَتَ عَن مُّوسَى ٱلْغَضَبُ أَخَذَ ٱلْأَلْوَاحَ ۖ وَفِى نُسْخَتِهَا هُدًۭى وَرَحْمَةٌۭ لِّلَّذِينَ هُمْ لِرَبِّهِمْ يَرْهَبُونَ
- (7:155) [next to 7:156] وَٱخْتَارَ مُوسَىٰ قَوْمَهُۥ سَبْعِينَ رَجُلًۭا لِّمِيقَٰتِنَا ۖ فَلَمَّآ أَخَذَتْهُمُ ٱلرَّجْفَةُ قَالَ رَبِّ لَوْ شِئْتَ أَهْلَكْتَهُم مِّن قَبْلُ وَإِيَّٰىَ ۖ أَتُهْلِكُنَا بِمَا فَعَلَ ٱلسُّفَهَآءُ مِنَّآ ۖ إِنْ هِىَ إِلَّا فِتْنَتُكَ تُضِلُّ بِهَا مَن تَشَآءُ وَتَهْدِى مَن تَشَآءُ ۖ أَنتَ وَلِيُّنَا فَٱغْفِرْ لَنَا وَٱرْحَمْنَا ۖ وَأَنتَ خَيْرُ ٱلْغَٰفِرِينَ
- (7:157) [next to 7:156] ٱلَّذِينَ يَتَّبِعُونَ ٱلرَّسُولَ ٱلنَّبِىَّ ٱلْأُمِّىَّ ٱلَّذِى يَجِدُونَهُۥ مَكْتُوبًا عِندَهُمْ فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ يَأْمُرُهُم بِٱلْمَعْرُوفِ وَيَنْهَىٰهُمْ عَنِ ٱلْمُنكَرِ وَيُحِلُّ لَهُمُ ٱلطَّيِّبَٰتِ وَيُحَرِّمُ عَلَيْهِمُ ٱلْخَبَٰٓئِثَ وَيَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ بِهِۦ وَعَزَّرُوهُ وَنَصَرُوهُ وَٱتَّبَعُوا۟ ٱلنُّورَ ٱلَّذِىٓ أُنزِلَ مَعَهُۥٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (7:158) [next to 7:156] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ جَمِيعًا ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِ ٱلنَّبِىِّ ٱلْأُمِّىِّ ٱلَّذِى يُؤْمِنُ بِٱللَّهِ وَكَلِمَٰتِهِۦ وَٱتَّبِعُوهُ لَعَلَّكُمْ تَهْتَدُونَ
- (7:178) [next to 7:180] مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِى ۖ وَمَن يُضْلِلْ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (7:179) [next to 7:180] وَلَقَدْ ذَرَأْنَا لِجَهَنَّمَ كَثِيرًۭا مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا وَلَهُمْ ءَاذَانٌۭ لَّا يَسْمَعُونَ بِهَآ ۚ أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْغَٰفِلُونَ
- (7:181) [next to 7:180] وَمِمَّنْ خَلَقْنَآ أُمَّةٌۭ يَهْدُونَ بِٱلْحَقِّ وَبِهِۦ يَعْدِلُونَ
- (7:182) [next to 7:180] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ
- (9:126) [next to 9:128] أَوَلَا يَرَوْنَ أَنَّهُمْ يُفْتَنُونَ فِى كُلِّ عَامٍۢ مَّرَّةً أَوْ مَرَّتَيْنِ ثُمَّ لَا يَتُوبُونَ وَلَا هُمْ يَذَّكَّرُونَ
- (9:127) [next to 9:128] وَإِذَا مَآ أُنزِلَتْ سُورَةٌۭ نَّظَرَ بَعْضُهُمْ إِلَىٰ بَعْضٍ هَلْ يَرَىٰكُم مِّنْ أَحَدٍۢ ثُمَّ ٱنصَرَفُوا۟ ۚ صَرَفَ ٱللَّهُ قُلُوبَهُم بِأَنَّهُمْ قَوْمٌۭ لَّا يَفْقَهُونَ
- (9:129) [next to 9:128] فَإِن تَوَلَّوْا۟ فَقُلْ حَسْبِىَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَلَيْهِ تَوَكَّلْتُ ۖ وَهُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ
- (11:38) [next to 11:40] وَيَصْنَعُ ٱلْفُلْكَ وَكُلَّمَا مَرَّ عَلَيْهِ مَلَأٌۭ مِّن قَوْمِهِۦ سَخِرُوا۟ مِنْهُ ۚ قَالَ إِن تَسْخَرُوا۟ مِنَّا فَإِنَّا نَسْخَرُ مِنكُمْ كَمَا تَسْخَرُونَ
- (11:39) [next to 11:40] فَسَوْفَ تَعْلَمُونَ مَن يَأْتِيهِ عَذَابٌۭ يُخْزِيهِ وَيَحِلُّ عَلَيْهِ عَذَابٌۭ مُّقِيمٌ
- (11:42) [next to 11:40] وَهِىَ تَجْرِى بِهِمْ فِى مَوْجٍۢ كَٱلْجِبَالِ وَنَادَىٰ نُوحٌ ٱبْنَهُۥ وَكَانَ فِى مَعْزِلٍۢ يَٰبُنَىَّ ٱرْكَب مَّعَنَا وَلَا تَكُن مَّعَ ٱلْكَٰفِرِينَ
- (11:44) [next to 11:43] وَقِيلَ يَٰٓأَرْضُ ٱبْلَعِى مَآءَكِ وَيَٰسَمَآءُ أَقْلِعِى وَغِيضَ ٱلْمَآءُ وَقُضِىَ ٱلْأَمْرُ وَٱسْتَوَتْ عَلَى ٱلْجُودِىِّ ۖ وَقِيلَ بُعْدًۭا لِّلْقَوْمِ ٱلظَّٰلِمِينَ
- (11:45) [next to 11:43] وَنَادَىٰ نُوحٌۭ رَّبَّهُۥ فَقَالَ رَبِّ إِنَّ ٱبْنِى مِنْ أَهْلِى وَإِنَّ وَعْدَكَ ٱلْحَقُّ وَأَنتَ أَحْكَمُ ٱلْحَٰكِمِينَ
- (12:38) [next to 12:40] وَٱتَّبَعْتُ مِلَّةَ ءَابَآءِىٓ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ ۚ مَا كَانَ لَنَآ أَن نُّشْرِكَ بِٱللَّهِ مِن شَىْءٍۢ ۚ ذَٰلِكَ مِن فَضْلِ ٱللَّهِ عَلَيْنَا وَعَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (12:39) [next to 12:40] يَٰصَىٰحِبَىِ ٱلسِّجْنِ ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
- (12:41) [next to 12:40] يَٰصَىٰحِبَىِ ٱلسِّجْنِ أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا ۖ وَأَمَّا ٱلْءَاخَرُ فَيُصْلَبُ فَتَأْكُلُ ٱلطَّيْرُ مِن رَّأْسِهِۦ ۚ قُضِىَ ٱلْأَمْرُ ٱلَّذِى فِيهِ تَسْتَفْتِيَانِ
- (12:42) [next to 12:40] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (13:28) [next to 13:30] ٱلَّذِينَ ءَامَنُوا۟ وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ ٱللَّهِ ۗ أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ
- (13:29) [next to 13:30] ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ طُوبَىٰ لَهُمْ وَحُسْنُ مَـَٔابٍۢ
- (13:31) [next to 13:30] وَلَوْ أَنَّ قُرْءَانًۭا سُيِّرَتْ بِهِ ٱلْجِبَالُ أَوْ قُطِّعَتْ بِهِ ٱلْأَرْضُ أَوْ كُلِّمَ بِهِ ٱلْمَوْتَىٰ ۗ بَل لِّلَّهِ ٱلْأَمْرُ جَمِيعًا ۗ أَفَلَمْ يَا۟يْـَٔسِ ٱلَّذِينَ ءَامَنُوٓا۟ أَن لَّوْ يَشَآءُ ٱللَّهُ لَهَدَى ٱلنَّاسَ جَمِيعًۭا ۗ وَلَا يَزَالُ ٱلَّذِينَ كَفَرُوا۟ تُصِيبُهُم بِمَا صَنَعُوا۟ قَارِعَةٌ أَوْ تَحُلُّ قَرِيبًۭا مِّن دَارِهِمْ حَتَّىٰ يَأْتِىَ وَعْدُ ٱللَّهِ ۚ إِنَّ ٱللَّهَ لَا يُخْلِفُ ٱلْمِيعَادَ
- (13:32) [next to 13:30] وَلَقَدِ ٱسْتُهْزِئَ بِرُسُلٍۢ مِّن قَبْلِكَ فَأَمْلَيْتُ لِلَّذِينَ كَفَرُوا۟ ثُمَّ أَخَذْتُهُمْ ۖ فَكَيْفَ كَانَ عِقَابِ
- (15:72) [next to 15:74] لَعَمْرُكَ إِنَّهُمْ لَفِى سَكْرَتِهِمْ يَعْمَهُونَ
- (15:73) [next to 15:74] فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُشْرِقِينَ
- (15:76) [next to 15:74] وَإِنَّهَا لَبِسَبِيلٍۢ مُّقِيمٍ
- (15:77) [next to 15:75] إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّلْمُؤْمِنِينَ
- (17:108) [next to 17:110] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
- (17:109) [next to 17:110] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
- (17:111) [next to 17:110] وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ ۖ وَكَبِّرْهُ تَكْبِيرًۢا
- (19:43) [next to 19:45] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (19:46) [next to 19:45] قَالَ أَرَاغِبٌ أَنتَ عَنْ ءَالِهَتِى يَٰٓإِبْرَٰهِيمُ ۖ لَئِن لَّمْ تَنتَهِ لَأَرْجُمَنَّكَ ۖ وَٱهْجُرْنِى مَلِيًّۭا
- (19:47) [next to 19:45] قَالَ سَلَٰمٌ عَلَيْكَ ۖ سَأَسْتَغْفِرُ لَكَ رَبِّىٓ ۖ إِنَّهُۥ كَانَ بِى حَفِيًّۭا
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (19:67) [next to 19:65] أَوَلَا يَذْكُرُ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن قَبْلُ وَلَمْ يَكُ شَيْـًۭٔا
- (19:91) [next to 19:93] أَن دَعَوْا۟ لِلرَّحْمَٰنِ وَلَدًۭا
- (19:92) [next to 19:93] وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا
- (19:94) [next to 19:93] لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا
- (19:95) [next to 19:93] وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا
- (20:3) [next to 20:5] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
- (20:4) [next to 20:5] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:6) [next to 20:5] لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَمَا بَيْنَهُمَا وَمَا تَحْتَ ٱلثَّرَىٰ
- (20:7) [next to 20:5] وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى
- (20:9) [next to 20:8] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:10) [next to 20:8] إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى
- (21:110) [next to 21:112] إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ
- (21:111) [next to 21:112] وَإِنْ أَدْرِى لَعَلَّهُۥ فِتْنَةٌۭ لَّكُمْ وَمَتَٰعٌ إِلَىٰ حِينٍۢ
- (22:32) [next to 22:34] ذَٰلِكَ وَمَن يُعَظِّمْ شَعَٰٓئِرَ ٱللَّهِ فَإِنَّهَا مِن تَقْوَى ٱلْقُلُوبِ
- (22:33) [next to 22:34] لَكُمْ فِيهَا مَنَٰفِعُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ مَحِلُّهَآ إِلَى ٱلْبَيْتِ ٱلْعَتِيقِ
- (22:35) [next to 22:34] ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَٱلصَّٰبِرِينَ عَلَىٰ مَآ أَصَابَهُمْ وَٱلْمُقِيمِى ٱلصَّلَوٰةِ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (22:37) [next to 22:36] لَن يَنَالَ ٱللَّهَ لُحُومُهَا وَلَا دِمَآؤُهَا وَلَٰكِن يَنَالُهُ ٱلتَّقْوَىٰ مِنكُمْ ۚ كَذَٰلِكَ سَخَّرَهَا لَكُمْ لِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ ۗ وَبَشِّرِ ٱلْمُحْسِنِينَ
- (22:38) [next to 22:36] ۞ إِنَّ ٱللَّهَ يُدَٰفِعُ عَنِ ٱلَّذِينَ ءَامَنُوٓا۟ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ كُلَّ خَوَّانٍۢ كَفُورٍ
- (25:58) [next to 25:60] وَتَوَكَّلْ عَلَى ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ وَسَبِّحْ بِحَمْدِهِۦ ۚ وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا
- (25:61) [next to 25:60] تَبَارَكَ ٱلَّذِى جَعَلَ فِى ٱلسَّمَآءِ بُرُوجًۭا وَجَعَلَ فِيهَا سِرَٰجًۭا وَقَمَرًۭا مُّنِيرًۭا
- (25:62) [next to 25:60] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (27:26) [next to 27:28] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ ۩
- (27:27) [next to 27:28] ۞ قَالَ سَنَنظُرُ أَصَدَقْتَ أَمْ كُنتَ مِنَ ٱلْكَٰذِبِينَ
- (27:32) [next to 27:30] قَالَتْ يَٰٓأَيُّهَا ٱلْمَلَؤُا۟ أَفْتُونِى فِىٓ أَمْرِى مَا كُنتُ قَاطِعَةً أَمْرًا حَتَّىٰ تَشْهَدُونِ
- (27:33) [next to 27:31] قَالُوا۟ نَحْنُ أُو۟لُوا۟ قُوَّةٍۢ وَأُو۟لُوا۟ بَأْسٍۢ شَدِيدٍۢ وَٱلْأَمْرُ إِلَيْكِ فَٱنظُرِى مَاذَا تَأْمُرِينَ
- (30:48) [next to 30:50] ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَيَبْسُطُهُۥ فِى ٱلسَّمَآءِ كَيْفَ يَشَآءُ وَيَجْعَلُهُۥ كِسَفًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ ۖ فَإِذَآ أَصَابَ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
- (30:49) [next to 30:50] وَإِن كَانُوا۟ مِن قَبْلِ أَن يُنَزَّلَ عَلَيْهِم مِّن قَبْلِهِۦ لَمُبْلِسِينَ
- (30:51) [next to 30:50] وَلَئِنْ أَرْسَلْنَا رِيحًۭا فَرَأَوْهُ مُصْفَرًّۭا لَّظَلُّوا۟ مِنۢ بَعْدِهِۦ يَكْفُرُونَ
- (30:52) [next to 30:50] فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (33:41) [next to 33:43] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (33:42) [next to 33:43] وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا
- (33:44) [next to 33:43] تَحِيَّتُهُمْ يَوْمَ يَلْقَوْنَهُۥ سَلَٰمٌۭ ۚ وَأَعَدَّ لَهُمْ أَجْرًۭا كَرِيمًۭا
- (33:45) [next to 33:43] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِنَّآ أَرْسَلْنَٰكَ شَٰهِدًۭا وَمُبَشِّرًۭا وَنَذِيرًۭا
- (47:20) [next to 47:22] وَيَقُولُ ٱلَّذِينَ ءَامَنُوا۟ لَوْلَا نُزِّلَتْ سُورَةٌۭ ۖ فَإِذَآ أُنزِلَتْ سُورَةٌۭ مُّحْكَمَةٌۭ وَذُكِرَ فِيهَا ٱلْقِتَالُ ۙ رَأَيْتَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ يَنظُرُونَ إِلَيْكَ نَظَرَ ٱلْمَغْشِىِّ عَلَيْهِ مِنَ ٱلْمَوْتِ ۖ فَأَوْلَىٰ لَهُمْ
- (47:21) [next to 47:22] طَاعَةٌۭ وَقَوْلٌۭ مَّعْرُوفٌۭ ۚ فَإِذَا عَزَمَ ٱلْأَمْرُ فَلَوْ صَدَقُوا۟ ٱللَّهَ لَكَانَ خَيْرًۭا لَّهُمْ
- (47:23) [next to 47:22] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَعَنَهُمُ ٱللَّهُ فَأَصَمَّهُمْ وَأَعْمَىٰٓ أَبْصَٰرَهُمْ
- (47:24) [next to 47:22] أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَآ
- (53:17) [next to 53:19] مَا زَاغَ ٱلْبَصَرُ وَمَا طَغَىٰ
- (53:18) [next to 53:19] لَقَدْ رَأَىٰ مِنْ ءَايَٰتِ رَبِّهِ ٱلْكُبْرَىٰٓ
- (53:20) [next to 53:19] وَمَنَوٰةَ ٱلثَّالِثَةَ ٱلْأُخْرَىٰٓ
- (53:21) [next to 53:19] أَلَكُمُ ٱلذَّكَرُ وَلَهُ ٱلْأُنثَىٰ
- (53:22) [next to 53:23] تِلْكَ إِذًۭا قِسْمَةٌۭ ضِيزَىٰٓ
- (53:24) [next to 53:23] أَمْ لِلْإِنسَٰنِ مَا تَمَنَّىٰ
- (53:25) [next to 53:23] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (55:0) [next to 55:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (55:3) [next to 55:1] خَلَقَ ٱلْإِنسَٰنَ
- (55:4) [next to 55:2] عَلَّمَهُ ٱلْبَيَانَ
- (55:76) [next to 55:78] مُتَّكِـِٔينَ عَلَىٰ رَفْرَفٍ خُضْرٍۢ وَعَبْقَرِىٍّ حِسَانٍۢ
- (55:77) [next to 55:78] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (56:72) [next to 56:74] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
- (56:73) [next to 56:74] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
- (56:75) [next to 56:74] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (56:76) [next to 56:74] وَإِنَّهُۥ لَقَسَمٌۭ لَّوْ تَعْلَمُونَ عَظِيمٌ
- (59:20) [next to 59:22] لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- (59:21) [next to 59:22] لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- (59:23) [next to 59:22] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- (59:24) [next to 59:22] هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (68:14) [next to 68:16] أَن كَانَ ذَا مَالٍۢ وَبَنِينَ
- (68:15) [next to 68:16] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (68:17) [next to 68:16] إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ
- (68:18) [next to 68:16] وَلَا يَسْتَثْنُونَ
- (87:0) [next to 87:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (87:2) [next to 87:1] ٱلَّذِى خَلَقَ فَسَوَّىٰ
- (87:3) [next to 87:1] وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- (96:0) [next to 96:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (96:2) [next to 96:1] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- (96:3) [next to 96:1] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ

