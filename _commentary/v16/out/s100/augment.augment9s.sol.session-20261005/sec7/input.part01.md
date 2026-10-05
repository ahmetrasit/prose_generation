Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 7 of 11 ("Sıkılmış el ve ortak kazan"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 7 (prose paragraphs numbered) =====
[¶32] Sekizinci ayet insanın neye bağlandığını söyler: {ar:وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ, tr:ve innehû li-hubbi'l-hayri le-şedîd, gloss:ve şüphesiz o, hayrı sevmekte pek şiddetlidir, source:100:8}. Bu ayetteki "hayr" mal olarak açıklanır: {ar:وإنه لحب الخير لشديد أي المال الكثير, tr:ve innehû li-hubbi'l-hayri le-şedîd, ey el-mâlu'l-kesîr, gloss:"hayrı sevmekte şiddetlidir", yani çok malı, source:"خ ي ر,B004"}. Ama her mala bu ad verilmez: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne kesîran ve min mekânin tayyib, gloss:mal çok olmadıkça ve temiz bir yerden gelmedikçe ona "hayır" denmez, source:"خ ي ر,B004"}. Bu ad {ar:ما كان مجموعا من المال من وجه محمود, tr:mâ kâne mecmû'an mine'l-mâli min vechin mahmûd, gloss:övülen bir yoldan toplanmış mal, source:"خ ي ر,B004"} için kullanılır. Kur'an kelimeyi bu anlamda vasiyet hükmünde de kullanır: {ar:إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ لِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ, tr:in teraka hayran el-vasiyyetu li'l-vâlideyni ve'l-akrabîn, gloss:geride mal bırakacaksa anne babaya ve yakınlara vasiyet, source:2:180}. Kelime iyi bir şeyi adlandırır, ama sevgi bu iyi şeye takıldığında onu tutsak eder.

[¶33] Sevgi kelimesinin kendisi de bu takılmayı gösterir. Önce bir tanımı vardır: {ar:المحبة إرادة ما تراه أو تظنه خيرا, tr:el-mahabbetu irâdetu mâ terâhu ev tezunnuhû hayran, gloss:sevgi, hayır olarak gördüğün ya da sandığın şeyi istemektir, source:"ح ب ب,B002"}. Bu tanım "sevgi" ile "hayr"ı tek bir cümlede birleştirir. Ardından bir yapışma anlamı gelir: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbetu iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi, bir şeye yapışıp ondan ayrılmamak anlamındaki "ehabbe"den türer, source:"ح ب ب,B002"}. Bu yapışmanın bir hayvan görüntüsü de vardır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-ba'îru izâ harune ve lezime mekânehû, gloss:deve inat edip yerinden kıpırdamadığında "ehabbe" denir, source:"ح ب ب,B005"}. Birinci ayette at bütün gücüyle ileri atılır. Sekizinci ayetin sevgisinin yanında ise yerine çakılıp kalan deve duyulur.

[¶34] "Şedîd" kelimesi de bu ayette cimri olarak açıklanır: {ar:لشديد أي لبخيل, tr:le-şedîd, ey le-bahîl, gloss:"şedîd" yani cimri, source:"ش د د,B006"}. Kelimenin bir başka kullanımı da aynı yöndedir: {ar:الشديد والمتشدد البخيل, tr:eş-şedîdu ve'l-muteşeddidu'l-bahîl, gloss:"şedîd" ve "muteşeddid" cimridir, source:"ش د د,B006"}. Kökün aslı bağlamaktır: {ar:شده أي أوثقه, tr:şeddehû, ey evsekah, gloss:onu sıkıca bağladı, source:"ش د د,B001"}; {ar:الشد العقد القوي, tr:eş-şeddu'l-akdu'l-kaviyy, gloss:"şedd" sağlam düğümdür, source:"ش د د,B001"}. Kese sıkıca bağlanır, düğüm çözülmez. Beşinci ayetin kelimesinin ailesi aynı eli gösterir: {ar:جمع الكف وهو حين تقبضها, tr:cum'u'l-keff, ve huve hîne takbiduhâ, gloss:"cum'", avucun yumulmuş halidir, source:"ج م ع,B005"}. Aynı ailede yumruğun en ağır biçimi de vardır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'atu'l-ğull, li-ennehâ tecma'u'l-yedeyni ile'l-unuk, gloss:"câmi'a" bukağıdır, çünkü elleri boyuna toplar, source:"ج م ع,B008"}. Kökün genel anlamı bir araya çekmektir: {ar:الجمع ضم الشيء بتقريب بعضه من بعض, tr:el-cem'u dammu'ş-şey'i bi-takrîbi ba'dıhî min ba'd, gloss:toplamak, bir şeyin parçalarını birbirine yaklaştırarak bir araya getirmektir, source:"ج م ع,B001"}. Kenûd olan kişi de bu el ile tarif edilir: {ar:يأكل وحده ويضرب عبده ويمنع رفده, tr:ye'kulu vahdehû ve yadribu abdehû ve yemne'u rifdeh, gloss:yalnız yer, kölesini döver, yardımını esirger, source:"ك ن د,B002"}.

[¶35] Bu yumulmuş elin karşısında aynı köklerden kurulan bir sofra durur. Beşinci ayetin kelimesinin ailesinde büyük bir kazan vardır: {ar:قدر جماع وجامعة وهي العظيمة, tr:kıdrun cimâ'un ve câmi'atun, ve hiye'l-azîme, gloss:"cimâ'" ve "câmi'a" kazan, büyük kazandır, source:"ج م ع,B012"}. İkinci ayetin kelimesinin ailesinde bu kazandan yemek kepçeyle alınır: {ar:قدحت القدر غرفت ما فيها, tr:kadahtu'l-kıdr, ğaraftu mâ fîhâ, gloss:kazanı "kadh" ettim, yani içindekini kepçeledim, source:"ق د ح,B005"}. Kepçe kazanın dibine kadar iner: {ar:القديح ما يبقى في أسفل القدر فيغرف بجهد, tr:el-kadîhu mâ yebkâ fî esfeli'l-kıdri fe-yuğrafu bi-cehd, gloss:"kadîh", kazanın dibinde kalıp güçlükle kepçelenen yemektir, source:"ق د ح,B005"}. Aynı ailede içki kabı da vardır: {ar:القدح واحد الأقداح التي للشرب, tr:el-kadahu vâhidu'l-akdâhi'lletî li'ş-şurb, gloss:"kadah", içmek için kullanılan kaplardan biridir, source:"ق د ح,B006"}. Paylar ise kura oklarıyla dağıtılır: {ar:القدح الواحد من قداح الميسر, tr:el-kıdhu'l-vâhidu min kıdâhi'l-meysir, gloss:"kıdh", meysir oklarından biridir, source:"ق د ح,B007"}. Bu okların durduğu kabın adı, altıncı ve on birinci ayetteki Rab kelimesinin ailesindendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rıbâbetu şebîhetun bi'l-kinâneti tucma'u fîhâ sihâmu'l-meysir, gloss:"rıbâbe", meysir oklarının toplandığı, ok kılıfına benzer bir kaptır, source:"ر ب ب,B010"}. Dördüncü ayetin kelimesinin ailesinde de kesilen hayvan ve yolcuya sunulan yemek vardır: {ar:النقيعة الجزور تنقع عن عدة إبل, tr:en-nakî'atu'l-cezûru tunka'u an iddeti ibil, gloss:"nakî'a", birkaç deve arasından ayrılıp kesilen devedir, source:"ن ق ع,B003"}; {ar:النقيعة الطعام يتخذ للقادم من السفر, tr:en-nakî'atu't-ta'âmu yuttehazu li'l-kâdimi mine's-sefer, gloss:"nakî'a", yolculuktan dönen için hazırlanan yemektir, source:"ن ق ع,B003"}. Son ayetin kelimesinin ailesinde ise ortaklaşa alınıp bölüşülen et vardır: {ar:تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها, tr:tehabbera'l-kavmu beynehum hubreten izâ işterev şâten fe-zebehûhâ ve'ktesemû lahmehâ, gloss:bir koyunu birlikte satın alıp kesen ve etini bölüşen topluluk için "tehabbera" denir, source:"خ ب ر,B006"}. Bütün bu sofranın adı da hayırdır: {ar:والخير الكرم, tr:ve'l-hayru'l-kerem, gloss:hayır, cömertliktir, source:"خ ي ر,B005"}. Böylece kelimeler, kenûdun "yalnız yer" tanımının tam karşısına büyük kazanı, kepçeyi, kabı, payları, kesilen hayvanı ve bölüşülen eti koyar.

[¶36] Onuncu ayetin fiili bu biriktirmeyi biriktirenin üzerine çevirir: {ar:أصل واحد منقاس وهو جمع الشيء, tr:aslun vâhidun munkâs, ve huve cem'u'ş-şey', gloss:tek ve kuralı işleyen bir köktür; bir şeyi toplamaktır, source:"ح ص ل,B001"}. Yumruğunu sıkıp malını toplayan kişi, sonunda göğsündekilerin toplanıp ortaya konduğu kişi olur. Düz bir anlatım "insan mala düşkündür" demekle kalırdı. Görüntü ise bu düşkünlüğün bedenini gösterir: yumulmuş avuç, boyna bağlanmış eller, yerinden kıpırdamayan deve ve tek başına yenen yemek.

[¶37] Kur'an biriktireni hem sözle hem de bu el görüntüsüyle anar. Ayıplayıp çekiştirenler için {ar:ٱلَّذِى جَمَعَ مَالًا وَعَدَّدَهُۥ, tr:ellezî ceme'a mâlen ve addedeh, gloss:mal toplayıp onu tekrar tekrar sayan, source:104:2} ve {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kıldığını sanır, source:104:3} denir. Cehennem ateşi yüz çevireni çağırır: {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve ceme'a fe-ev'â, gloss:toplayıp kaba doldurup saklayanı, source:70:18}. Aynı yerde insanın yaratılışı anlatılır: {ar:إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا, tr:inne'l-insâne hulika helû'â, gloss:insan pek sabırsız yaratıldı, source:70:19}; {ar:وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا, tr:ve izâ messehu'l-hayru menû'â, gloss:kendisine hayır dokununca da pek esirgeyici olur, source:70:21}. Bu ayette "insan" ve "hayr", bizim suredeki gibi yan yana ve aynı esirgeme anlamında geçer. Rabbinin kendisini aşağıladığını söyleyen insana şu cevap verilir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ bel lâ tukrimûne'l-yetîm, gloss:hayır, siz yetime ikram etmiyorsunuz, source:89:17}; {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ ta'âmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}; {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّا جَمًّا, tr:ve tuhibbûne'l-mâle hubben cemmâ, gloss:malı yığın yığın bir sevgiyle seviyorsunuz, source:89:20}. Boyna bağlı el görüntüsü bir buyrukta açıkça yer alır: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Buyruğun hemen ardından gelen ayet, bizim surenin son kelimesiyle biter: {ar:إِنَّ رَبَّكَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ كَانَ بِعِبَادِهِۦ خَبِيرًا بَصِيرًا, tr:inne rabbeke yebsutu'r-rızka li-men yeşâu ve yakdir, innehû kâne bi-ibâdihî habîran basîrâ, gloss:Rabbin rızkı dilediğine bol verir, dilediğine daraltır; O kullarından haberdar olandır, onları görendir, source:17:30}. Aynı surede insanın tutumu şöyle özetlenir: {ar:قُل لَّوْ أَنتُمْ تَمْلِكُونَ خَزَآئِنَ رَحْمَةِ رَبِّىٓ إِذًا لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ ۚ وَكَانَ ٱلْإِنسَٰنُ قَتُورًا, tr:kul lev entum temlikûne hazâine rahmeti rabbî izen le-emsektum haşyete'l-infâk, ve kâne'l-insânu katûrâ, gloss:de ki: Rabbimin rahmet hazinelerine siz sahip olsaydınız, harcamaktan korkup elinizde tutardınız; insan pek eli sıkıdır, source:17:100}. Cimrilerin tuttukları şey sonunda boyunlarına dolanır: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahılû bihî yevme'l-kıyâme, gloss:cimrilik ettikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}. Bu ayet de {ar:وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌ, tr:va'llâhu bimâ ta'melûne habîr, gloss:Allah yaptıklarınızdan haberdardır, source:3:180} sözüyle biter.

[¶38] Ortak kazan görüntüsü de Kur'an'da karşılığını bulur. Davud'un ailesi için yapılanlar arasında {ar:وَجِفَانٍ كَٱلْجَوَابِ وَقُدُورٍ رَّاسِيَٰتٍ, tr:ve cifânin ke'l-cevâbi ve kudûrin râsiyât, gloss:havuz gibi çanaklar ve yerinden kalkmayan kazanlar, source:34:13} sayılır. Hemen ardından {ar:ٱعْمَلُوٓا۟ ءَالَ دَاوُۥدَ شُكْرًا ۚ وَقَلِيلٌ مِّنْ عِبَادِىَ ٱلشَّكُورُ, tr:i'melû âle dâvûde şukrâ, ve kalîlun min ibâdiye'ş-şekûr, gloss:ey Davud ailesi, şükür olarak çalışın; kullarımdan şükredenler azdır, source:34:13} denir. Büyük kazan ile şükür aynı ayette durur. Sevdiği şeyi verenler de anılır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا, tr:ve yut'imûne't-ta'âme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:ona olan sevgilerine rağmen yemeği yoksula, yetime ve esire yedirirler, source:76:8}. İyiliğin tarifinde de aynı kalıp kullanılır: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı, sevgisine rağmen verdi, source:2:177}. Hüküm de açıktır: {ar:لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ, tr:len tenâlû'l-birra hattâ tunfikû mimmâ tuhibbûn, gloss:sevdiğiniz şeylerden harcamadıkça iyiliğe erişemezsiniz, source:3:92}. Sevgi bu ayetlerde de vardır, ama tutan elde değil veren eldedir. Yalnız yiyenin tarifi de Kur'an'da geçer: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ ta'âmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmezdi, source:69:34}; {ar:وَيَمْنَعُونَ ٱلْمَاعُونَ, tr:ve yemne'ûne'l-mâ'ûn, gloss:en küçük yardımı bile esirgerler, source:107:7}. Göğüs bu sahnede de belirir. Göç edenleri yurtlarında karşılayanlar için {ar:وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةً مِّمَّآ أُوتُوا۟ وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ, tr:ve lâ yecidûne fî sudûrihim hâceten mimmâ ûtû ve yu'sirûne alâ enfusihim, gloss:onlara verilenden ötürü göğüslerinde bir istek duymazlar ve onları kendilerine tercih ederler, source:59:9} denir. Ayet şöyle sürer: {ar:وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve men yûka şuhha nefsihî fe-ulâike humu'l-muflihûn, gloss:kim nefsinin hırsından korunursa, işte onlar kurtuluşa erenlerdir, source:59:9}.

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: chain 7 (rain on the land) as its own section - merged into chain 6 as one image of kenûd
- not developed: chain 9 (shared pot) as its own section - merged into chain 8 as the counter-scene of the closed hand
- not developed: غ ي ر B001 "God's rain/provision" member in chains 6 and 7 - wrong root for al-mughīrāt, dropped
- not developed: ضبح as owl and echo calls (chain 4) - relies on pre-Islamic lore outside the Quran, dropped
- not developed: ربيون "great crowds" (chain 11) - too loose a link to rabb, dropped
- not developed: the map's meysir lore (chain 9) and its commentators remark (chain 6) - reports from outside the Quran, dropped
- memory: al-mughīrāt is the form IV participle of أغار "to raid", root غ و ر
- memory: غار يغير "to provide rain" is a separate verb and not the root of al-mughīrāt
- memory: the preposition عن in 38:32 can mean both "because of" and "away from"

===== passages from the discovery list (261) =====
## strong (122)

- (2:177) [luna: strong; terra: contrast; basis: contrast+root+theme] [cited in ¶38] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section's root حبّ depicts attachment to wealth; this ayah makes giving wealth “عَلَىٰ حُبِّهِ” part of righteousness, so love need not end in hoarding. The phrase can retain the sense of giving while the wealth is loved. | terra: Righteousness includes giving wealth عَلَىٰ حُبِّهِ to relatives and vulnerable people, the same love-of-property tension resolved by release.
- (2:180) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶32] كُتِبَ عَلَيْكُمْ إِذَا حَضَرَ أَحَدَكُمُ ٱلْمَوْتُ إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ لِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ بِٱلْمَعْرُوفِ ۖ حَقًّا عَلَى ٱلْمُتَّقِينَ
  Unverified discovery rationale: luna: The section explicitly identifies its dictionary sense of الخير as wealth; this testamentary ayah uses “خَيْرًا” for what a person leaves and directs a bequest to parents and relatives. | terra: إِن تَرَكَ خَيْرًا uses khayr for property left behind and orders a bequest to parents and relatives, confirming the section's wealth sense while directing it into shares.
- (2:188) [luna: strong; terra: strong; basis: contrast+scene+theme] وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَكُم بَيْنَكُم بِٱلْبَٰطِلِ وَتُدْلُوا۟ بِهَآ إِلَى ٱلْحُكَّامِ لِتَأْكُلُوا۟ فَرِيقًۭا مِّنْ أَمْوَٰلِ ٱلنَّاسِ بِٱلْإِثْمِ وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The section calls good wealth that acquired from a praiseworthy way; this boundary forbids consuming one another's wealth unjustly (“بِالْبَاطِلِ”), distinguishing legitimate provision from wrongful gain. | terra: The ban on consuming one another's property falsely sets the negative boundary around the section's “good” wealth gathered from a praiseworthy source.
- (2:215) [luna: strong; terra: strong; basis: root+theme] يَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ ۖ قُلْ مَآ أَنفَقْتُم مِّنْ خَيْرٍۢ فَلِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ ۗ وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section identifies “خَيْر” as wealth; in this answer about what to spend, “مِنْ خَيْرٍ” is directed to parents, relatives, orphans, the poor, and travelers. | terra: The answer about what khayr is spent names parents, relatives, orphans, the poor, and the traveler, converting “good” property into a widening table of beneficiaries.
- (2:219) [terra: strong; basis: scene+theme] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ ۖ قُلْ فِيهِمَآ إِثْمٌۭ كَبِيرٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا ۗ وَيَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ قُلِ ٱلْعَفْوَ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
  Unverified discovery rationale: terra: One ayah joins wine, gambling, and the answer قُلِ ٱلْعَفْوَ about what to spend; it brings together the section's drinking cup, gambling lots, and the surplus that should leave the hand.
- (2:267) [luna: strong; terra: strong; basis: contrast+root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
  Unverified discovery rationale: luna: The section says its dictionary sense of الخير is substantial wealth from a good source; this command to spend from good earnings (“مِن طَيِّبَاتِ مَا كَسَبْتُمْ”) forbids selecting the bad for others. | terra: The command to spend from the good things one has earned, not deliberately offer the defective, grounds the section's claim that wealth called khayr comes by a praised and wholesome route.
