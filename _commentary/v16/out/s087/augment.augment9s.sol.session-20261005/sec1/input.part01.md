Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 1 of 18 ("Gökten otlağa: bulut, ilk yağmur ve kararan ot"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.

===== _commentary/v16/prompts/augment9s/augment.md =====
You are completing a finished Turkish commentary on the images of a surah,
written by another reader, with what the Quran itself says about it: the Quran
explaining the Quran. Below are one image section of that commentary, with its
prose paragraphs numbered [¶n] as in the whole commentary; the commentary's
ledger; and Quran passages from an image-based discovery list (two readers'
judgements of which ayat this image activates), each with its Arabic, its tier,
the bases given for it, and the paragraphs of the section that already cite it,
if any. A tier is that list's own judgement, not yours; the list is not
authoritative and may be incomplete.

Read the section first. Then judge every listed passage, one by one, against
every paragraph of the section: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the ayat the paragraph reads leave
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

Then go through the section paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; the other places where the image's scene,
object or act is staged, with or without a shared word; ayat that state the same thing in other
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
passage from your own knowledge that you weighed, marked "own". Paragraph
numbers are the ones shown: only this section's paragraphs may be served.
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 1 (prose paragraphs numbered) =====
[¶1] Surenin ilk beş ayeti bir bitkinin bütün ömrünü kısa tutarak anlatır. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran O'dur, source:87:4} der, beşinci ayet ise {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5} diye biter. İki ayet arasında otu topraktan çıkaran şeyin, yani yağmurun adı geçmez. Bu eksik halkayı surenin başka kelimelerinin aileleri tamamlar. Burada ve sonraki bölümlerde, bir kelimenin kök ailesinden gelen görüntü kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Birinci ayetteki "ad" yine addır, "Rab" yine Rab'dir. Aile görüntüsü, bu anlamın arkasında Arapçayı bilen kulağa ayrıca ulaşan sahnedir.

[¶2] Birinci ayet {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:yüce Rabbinin adını tesbih et, source:87:1} der. "Ad" anlamındaki اسم kelimesi س م و kökündendir ve bu kök gökyüzünü de verir. Araplar için {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}, ve aynı ad yağmurun bitirdiği ota da verilir: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt basittir: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp sana gölge salan her şeydir, source:"س م و,B004"}. Tek bir kök böylece başın üstündeki örtüden buluta, buluttan yağmura, yağmurdan topraktan çıkan ota kadar uzanan bütün dikey sütunu kapsar. "Rab" kelimesinin ailesi bu sütunun içinde belirli bir bulutu gösterir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bu, ötekilerin altında sarkan alçak buluttur: {ar:السحاب المتعلق دون السحاب, tr:es-sehâbu'l-muteallaku dûne's-sehâb, gloss:bulutların altında asılı duran bulut, source:"ر ب ب,B008"}. Aynı kök bulutun bir yerde durup gitmemesini de söyler: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Aynı kalıp güney rüzgârı için de kullanılır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbu ve's-sehâbe ey dâmet, gloss:güney rüzgârı da bulut da sürdü, source:"ر ب ب,B007"}. Bulutu süren bu rüzgârın adı olan cenûb, on birinci ayetteki يَتَجَنَّبُهَا kelimesiyle aynı köktendir: {ar:الجنوب ريح تجيء عن يمين القبلة, tr:el-cenûbu rîhun tecîu an yemîni'l-kıble, gloss:cenûb kıblenin sağ yanından gelen rüzgârdır, source:"ج ن ب,B006"}.

[¶3] Bulut ilk belirdiğinde Arapça ona dördüncü ayetin fiilinden bir ad verir: {ar:الخروج السحاب أول ما يبدأ, tr:el-hurûc es-sehâbu evvele mâ yebdeu, gloss:hurûc bulutun ilk belirişidir, source:"خ ر ج,B005"}. Bulutun kenarlarında zayıf bir şimşek çakar. Bunu anlatan fiil, yedinci ayetteki يَخْفَىٰ ile aynı köktendir: {ar:خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم, tr:hafe'l-berku yahfû hufuvven ve yahfî hafyen iẕâ leme'a lem'an daîfen mu'teridan fî nevâhi'l-ğaym, gloss:şimşek bulutun kenarlarında yan yan zayıfça parladığında hafâ denir, source:"خ ف ي,B004"}. Bu ışığı bütün gece gözleyen kişiyi ise on yedinci ayetteki أَبْقَىٰٓ kelimesinin kökü anlatır: {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca şimşeğin nereden çakacağına bakarak geceyi geçirdi, source:"ب ق ي,B005"}. Sonunda yağmur gelir ve adını verdiği hayattan alır: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. On üçüncü ayetteki يَحْيَىٰ fiili ve on altıncı ayetteki ٱلْحَيَوٰةَ kelimesi bu köktendir. Yağmur yuvalarındaki fareleri de dışarı sürer. Bu sürüş yine "gizli" kökünden bir fiille söylenir, açıklaması da dördüncü ayetin fiiliyle yapılır: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}.

[¶4] اسم kelimesi için Arapçada kayıtlı ikinci bir türetme vardır. Bu türetme kelimeyi "damga" anlamındaki وسم köküne bağlar. Bu, kök kimliği değil, kayıtlı bir alternatiftir. Ama bu yoldan da aynı sahneye varılır, çünkü yılın ilk yağmurunun adı bu köktendir: {ar:سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة, tr:sumiye'l-vesmiyyu mine'l-matari vesmiyyen li-ennehû yesimu'l-arda bi'n-nebâti fe-yasîru fîhâ eseran fî evveli's-sene, gloss:ilk yağmura vesmî denir çünkü yeri bitkiyle damgalar ve yılın başında yerde bir iz olur, source:"و س م,B003"}. Yağmur toprağa yeşil bir iz basar.

[¶5] Dördüncü ayetin fiili أخرج, somut bir şeyin bulunduğu yerden dışarı alınmasıdır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut şeyler için söylenir, source:"خ ر ج,B002"}. Ot gerçekten topraktan çekilip çıkarılan bir şeydir. Aynı kökün ailesi ilk çıkışın görünüşünü de verir: {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:otu bir yerde bitip başka yerde bitmeyen toprak, source:"خ ر ج,B007"}. İlk yeşil, toprağa yama yama düşer. Aynı ailede bir renk adı da vardır: {ar:الأخرج لون سواده أكثر من بياضه, tr:el-ahrecu levnun sevâduhû ekŝeru min beyâdih, gloss:karası akından çok olan renk, source:"خ ر ج,B007"}. المرعى ise tek kelimede otu, otlağın yerini ve otlamanın kendisini birlikte taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ra'yu ve'l-mevdiu ve'l-masdar, gloss:mer'â hem ot hem yer hem otlamadır, source:"ر ع ي,B001"}.

[¶6] Beşinci ayetteki جعل, bir şeyi bir halden başka bir hale çevirmektir: {ar:جعل صير, tr:ce'ale sayyera, gloss:ce'ale bir şeyi başka bir hale soktu demektir, source:"ج ع ل,B002"}. Otun çevrildiği şey olan غثاء, otun sonunu üç adımda anlatır: ot kurur, tadını yitirir, sel onu yığıp götürür. {ar:غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته, tr:ğaŝe's-seylu'l-merte'a iẕâ ceme'a ba'dahû ilâ ba'din ve eẕhebe halâvetehû, gloss:sel otlağı üst üste yığıp tadını giderdiğinde ğaŝâ denir, source:"غ ث و,B002"}. Ot bu noktada {ar:يابسا بعد خضرته, tr:yâbisen ba'de hudratihî, gloss:yeşilliğinden sonra kurumuş olarak, source:"غ ث و,B002"} kalır. غثاء de {ar:الغثاء ما جاء به السيل من نبات قد يبس, tr:el-ğuŝâu mâ câe bihi's-seylu min nebâtin kad yebise, gloss:ğuŝâ selin getirdiği kurumuş bitkidir, source:"غ ث و,B001"}. Ardından gelen أحوى bir renktir: {ar:الأحوى الأسود من الخضرة, tr:el-ahvâ el-esvedu mine'l-hudra, gloss:ahvâ yeşilden kararmış olandır, source:"ح و ي,B006"}. Bir deve için de {ar:بعير أحوى إذا خالط خضرته سواد وصفرة, tr:baîrun ahvâ iẕâ hâlata hudratehû sevâdun ve sufra, gloss:yeşiline kara ve sarı karışmış deveye ahvâ denir, source:"ح و ي,B006"}. Rengin adı {ar:حُوَّة, tr:huvve, gloss:yeşile çalan koyu renk, source:"memory"} kelimesidir. Ayette kelime غثاء'nın sıfatı olarak durur. Ama tanımı hem gür yeşilin koyuluğunu hem de çürüyen otun kararmasını kapsar. Bu yüzden tek kelime otun iki ucunu, taze koyuluğu ve kapkara döküntüyü yan yana tutar. Kur'an gür yeşilin koyuluğunu başka bir yerde tek kelimeyle, cennet bahçeleri için verir: {ar:مُدْهَآمَّتَانِ, tr:müdhâmmetân, gloss:yeşillikten koyu kara görünen iki bahçe, source:55:64}.

[¶7] Bu sahne surenin geri kalanında karşılık bulur. On üçüncü ayetteki "yaşamak" fiilinin ailesi diri otu {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezzu, gloss:bitkinin dirisi taze olup titreşenidir, source:"ح ي ي,B002"} diye tanımlar. "Ölmek" fiilinin ailesi de {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtân el-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Otun yolculuğu böylece ölü topraktan titreşen yeşile, oradan kuru döküntüye uzanır. On üçüncü ayetin ateşteki adam için söylediği şey ise bu uçlardan hiçbirinde olmamaktır. "Rab" kelimesinin ailesinde bu yolculuğun karşısında duran bir bitki adı da vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}. Kur'an dünya hayatı benzetmesinde tam da bu "sararıp kurumak" fiilini kullanır. Rab adının ailesindeki sararmayan ot bu sayede otlağın kaderinin karşısına konabilir. Bu bağı dil değil, okuma kurar.

[¶8] Kur'an bu yolculuğu kendi sözleriyle sahneler. Allah kendini, rüzgârları rahmetinin önünde müjdeci olarak gönderen ve ağır bulutları ölü bir beldeye süren olarak anlatır, sonra şöyle der: {ar:فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-enzelnâ bihi'l-mâe fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:oraya suyu indirdik ve onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Çıkarmak fiili burada hem bitkiye hem ölülere, sonunda da hatırlamaya bağlanır. Sure de dördüncü ayetteki çıkarmadan dokuzuncu ayetteki hatırlatmaya aynı yolla uzanır. Hemen sonraki ayet, iyi toprağın bitkisini {ar:بِإِذْنِ رَبِّهِۦ, tr:bi-izni rabbih, gloss:Rabbinin izniyle, source:7:58} çıkardığını söyler. Başka bir yerde Allah gökten bereketli su indirip onunla ölü bir beldeyi dirilttiğini anlatır ve {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Firavun Musa'ya {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kimdir ey Musa, source:20:49} diye sorduğunda Musa'nın cevabı bu surenin ilk ayetlerindeki sırayı izler: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunelleẕî a'tâ kulle şey'in halkahû ŝumme hedâ, gloss:Rabbimiz her şeye yaratılışını veren sonra yol gösterendir, source:20:50}. Birkaç ayet sonra gökten su indirilir ve {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Surenin son ayetinde sayfaları anılan Musa, Rabbini tanıtırken aynı yaratma, yol gösterme ve çıkarma sırasını kullanır. Bir başka yerde yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir.

[¶9] Kur'an otun ikinci yarısını, yani kuruyup savrulmasını, dünya hayatının benzetmesi yapar. İki bahçe sahibinin hikâyesinden sonra Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ, tr:vadrib lehum meŝele'l-hayâti'd-dunyâ ke-mâin enzelnâhu mine's-semâ, gloss:onlara dünya hayatının örneğini ver; gökten indirdiğimiz bir su gibidir, source:18:45}. Yerin bitkisi o suyla karışır, sonra {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen sonraki ayet karşı kefeyi koyar: {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bu iki ayet, beşinci ayetteki döküntüyü on altıncı ve on yedinci ayetteki "dünya hayatı" ile "daha hayırlı ve daha kalıcı" ayrımına bağlayan köprüyü Kur'an'ın kendi ağzından kurar. Aynı benzetme başka bir yerde şu sözlerle gelir: {ar:ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ŝumme yehîcu fe-terâhu musferran ŝumme yekûnu hutâmâ, gloss:sonra kurur da onu sapsarı görürsün sonra çer çöp olur, source:57:20}. Bir başka yerde aynı süreç {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ, tr:ŝumme yec'aluhû hutâmâ inne fî ẕâlike le-ẕikrâ, gloss:sonra onu çer çöpe çevirir; bunda elbette bir öğüt vardır, source:39:21} sözleriyle anlatılır. Bu cümle beşinci ayetteki "çevirdi" fiilini ve dokuzuncu ayetteki "öğüt" kelimesini bir arada tutar. Başka bir yerde yeryüzü süslenir, sahipleri ona güç yetirdiklerini sanır, sonra buyruk gelir: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-ce'alnâhâ hasîden ke-en lem teğne bi'l-ems, gloss:onu dün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Kelimenin kendisi de Kur'an'da bir topluluk için kullanılır. Bir önceki kavimden sonra yaratılan bir neslin hikâyesinde, onları yakalayan çığlığın ardından şöyle denir: {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-ce'alnâhum ğuŝâen, gloss:onları sel döküntüsüne çevirdik, source:23:41}. Fiil de kelime de aynıdır, ama burada ot yerine insanlar vardır.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (235) =====
## strong (115)

- (2:19) [luna: medium; terra: strong; basis: scene] أَوْ كَصَيِّبٍۢ مِّنَ ٱلسَّمَآءِ فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ يَجْعَلُونَ أَصَٰبِعَهُمْ فِىٓ ءَاذَانِهِم مِّنَ ٱلصَّوَٰعِقِ حَذَرَ ٱلْمَوْتِ ۚ وَٱللَّهُ مُحِيطٌۢ بِٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section develops weak lightning at cloud edges; this rainstorm parable explicitly stages rain from the sky, darkness, thunder, and lightning, though its primary point is people in doubt. | terra: A rain cloud contains darkness, thunder, and lightning, supplying a direct Quranic storm setting for the section's first cloud and its marginal flash.
- (2:20) [luna: medium; terra: strong; basis: contrast+neighbour+scene] يَكَادُ ٱلْبَرْقُ يَخْطَفُ أَبْصَٰرَهُمْ ۖ كُلَّمَآ أَضَآءَ لَهُم مَّشَوْا۟ فِيهِ وَإِذَآ أَظْلَمَ عَلَيْهِمْ قَامُوا۟ ۚ وَلَوْ شَآءَ ٱللَّهُ لَذَهَبَ بِسَمْعِهِمْ وَأَبْصَٰرِهِمْ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The verse's برق nearly snatches sight: it gives the section's faint cloud-edge flash a brighter storm counterpart and makes visibility itself unstable. | terra: The lightning nearly snatches sight, yet people walk when it lights and stop when darkness returns; this turns watching intermittent nocturnal light into movement and contrasts with the lexicon's weak lightning watched through the night.
- (2:22) [luna: strong; terra: strong; basis: root+scene+speaker+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The section's lexical image of the sky as what covers above extends downward through cloud and rain to pasture; this verse joins the sky as a canopy, water sent down, and fruit brought out from earth. | terra: Earth is made a resting place, sky a canopy, water descends, and fruits are brought out as provision; it renders the section's sky-to-earth vertical column in one ayah.
- (2:164) [luna: strong; terra: strong; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: This sign sequence places winds, clouds held between sky and earth, rain, and revived land together, matching the section's vertical passage from cloud to living growth. | terra: Water from the sky revives earth after death, creatures spread, winds turn, and clouds are controlled between sky and earth; the ayah lays out the section's complete vertical and moving weather system.
- (2:265) [luna: medium (missing-ayat turn); terra: strong; basis: scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: The verse pictures a fertile garden on a height receiving heavy rain or drizzle and yielding fruit, a specific soil-and-rain counterpart to the section's pasture emerging under rain. | terra: A garden on high ground bears doubled produce under heavy rain and still yields under light rain, showing how differing rain intensities nourish rather than merely accompany the green mark.
- (6:59) [terra: strong; basis: root+theme] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: terra: God knows the falling leaf, the grain hidden in earth's darkness, and every moist and dry thing; hiddenness, plant location, and the wet-to-dry poles of the image meet under divine knowledge.
