Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:13; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_13/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_13.reading.tr.md (prose paragraphs numbered) =====
## Son "sonra"

[¶1] On üçüncü ayet, on birinci ayette hatırlatmadan uzak duran kişinin hikâyesini sürdürür. Sure ona {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ondan kaçınır, source:87:11} demiş, onu da {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yaslâ'n-nâra'l-kubrâ, gloss:en büyük ateşe giren, source:87:12} diye tanıtmıştı. Bu ayet onun o ateşin içindeki halini söyler: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. {ar:فِيهَا, tr:fîhâ, gloss:orada, onun içinde, source:87:13} ateşe döner. İki fiil de bitmemiş, süren bir hali bildiren kiptedir. Ayet bir olayı değil, sonu görünmeyen bir durumu anlatır. Başa gelen {ar:ثُمَّ, tr:ŝumme, gloss:sonra, source:87:13} Arapçada arada bir mesafe olduğunu duyurur. Bu mesafe zamanla ilgili olabildiği gibi derece farkı da olabilir. Burada ikisi birlikte işler. Ateşe girmek bir olaydır. Ardından ondan daha ağır olan gelir: girilen yerde kalınan hal.

[¶2] Arapça bu iki kelimeyi birbirinin tam karşıtı olarak tanımlar: {ar:الحياة ضد الموت والحي ضد الميت, tr:el-hayâtu diddu'l-mevti ve'l-hayyu diddu'l-meyyit, gloss:hayat ölümün karşıtıdır, diri de ölünün, source:"ح ي ي,B001"}. Canlı bir varlık ya diridir ya ölü. Üçüncü bir yol yoktur. Ayet bu yüzden "yarı ölü" demiyor. İkisini birden olumsuzlayarak her iki çıkışın da kapandığını söylüyor.

[¶3] Kur'an insanın serüvenini başka bir yerde bu "sonra"larla sıralar. Allah, kendisini inkâr edenlere {ar:كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ, tr:keyfe tekfurûne billâhi ve kuntum emvâten fe-ahyâkum, gloss:Allah'ı nasıl inkâr edersiniz, ölüydünüz de sizi O diriltti, source:2:28} der ve sözü şöyle sürdürür: {ar:ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ, tr:ŝumme yumîtukum ŝumme yuhyîkum ŝumme ileyhi turce'ûn, gloss:sonra sizi öldürecek, sonra diriltecek, sonra O'na döndürüleceksiniz, source:2:28}. Oradaki her "sonra" insanı ölümden hayata ya da hayattan ölüme geçirir. On üçüncü ayette ise "sonra" son bir kez gelir ve arkasından ne ölüm gelir ne hayat. Adem'in, eşinin ve şeytanın cennetten indirildiği sahne de bu ayetin yapısını önceden kurar. Onlara {ar:ٱهْبِطُوا۟, tr:ihbitû, gloss:inin, source:7:24} denir, sonra yeryüzü için şöyle buyrulur: {ar:فِيهَا تَحْيَوْنَ وَفِيهَا تَمُوتُونَ وَمِنْهَا تُخْرَجُونَ, tr:fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuhracûn, gloss:orada yaşayacak, orada ölecek, oradan çıkarılacaksınız, source:7:25}. Yeryüzü ikisinin de yaşandığı "orası"dır. Ateş ise ikisinin de yaşanmadığı "orası"dır. İki ayette aynı edat aynı iki fiille kullanılır, ama ikinci ayette iki fiil de olumsuzdur.

[¶4] Ayetin yükü ikinci yarısındadır. Cennettekiler için de {ar:لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ, tr:lâ yeẕûkûne fîhe'l-mevte ille'l-mevtete'l-ûlâ, gloss:orada ilk ölümden başka ölüm tatmazlar, source:44:56} denir. Buradaki mevte, Arapçada {ar:الموتة الواحدة من الموت, tr:el-mevtetu'l-vâhidetu mine'l-mevt, gloss:bir kez ölüş, source:"م و ت,B008"} olarak bilinen kelimedir. "Ölmemek" iki yurdun ortak halidir. Ateşi ateş yapan, ölümsüzlüğün yanına hayatın konmamasıdır.

## Ölümün dinginliği

[¶5] Ayette يَمُوتُ yalnızca "ölmek", yani hayatın sona ermesi anlamındadır. Ama Araplar bu fiili tam anlamıyla ölüm olmayan durumlar için de kullanmıştır. Bu kullanımlardan doğan görüntüler kelimenin ayetteki anlamının yerini almaz, onun yanında duyulur. Duyulduklarında da "ölememek"in insandan neyi esirgediğini gösterirler. Kökün çekirdeği güç kaybıdır: {ar:أصل صحيح يدل على ذهاب القوة من الشيء, tr:aslun sahîhun yedullu alâ ẕehâbi'l-kuvveti mine'ş-şey', gloss:bir şeyden gücün çekilmesini gösteren sağlam bir kök, source:"م و ت,B001"}. Kısaca da {ar:الموت السكون, tr:el-mevtu's-sukûn, gloss:ölüm dinginliktir, source:"م و ت,B012"} denirdi. Esen rüzgâr durunca {ar:ماتت الريح إذا سكنت, tr:mâteti'r-rîhu iẕâ sekenet, gloss:rüzgâr dindiğinde "rüzgâr öldü" denir, source:"م و ت,B012"}. Uykuya dalan biri için {ar:مات الرجل وهمد وهوم إذا نام, tr:mâte'r-raculu ve hemede ve hevveme iẕâ nâm, gloss:adam uyuyunca "öldü, sindi, daldı" derler, source:"م و ت,B012"}. Nöbet geçirip yere yıkılan ve sonra kendine gelen kişinin haline de bu kökten bir ad verilmişti: {ar:الموتة الذي يصرع من الجنون أو غيره ثم يفيق, tr:el-mûtetu elleẕî yusra'u mine'l-cunûni ev ğayrihî ŝumme yufîk, gloss:mûte, delilikten ya da başka bir sebepten yere yıkılıp sonra ayılmaktır, source:"م و ت,B009"}. Bu kullanımların hepsinde ölüm hareketin, sarsıntının ve çabanın çekildiği bir duruştur. Rüzgârın dinmesi, gözün kapanması, bilincin bir süre kararması bu duruşun örnekleridir.

[¶6] Kur'an da uykuyu ölüme yakın tutar: {ar:ٱللَّهُ يَتَوَفَّى ٱلْأَنفُسَ حِينَ مَوْتِهَا وَٱلَّتِى لَمْ تَمُتْ فِى مَنَامِهَا, tr:allâhu yeteveffe'l-enfuse hîne mevtihâ velletî lem temut fî menâmihâ, gloss:Allah canları ölümleri anında alır, ölmeyenleri de uykularında, source:39:42}. Başka bir yerde uyku için {ar:وَٱلنَّوْمَ سُبَاتًۭا, tr:ve'n-nevme subâtâ, gloss:uykuyu bir dinlenme kıldı, source:25:47} denir. Dünyada insan her gece küçük bir "ölüm" yaşar ve dinlenir. "Ölmez" sözü bu ışıkta okunduğunda, son çıkışın kapanmasının yanında dinmenin, uykunun ve kendinden geçmenin de kalmadığını söyler.

[¶7] Kur'an bu hali başka yerlerde de anlatır. İnkâr edenler için cehennem ateşinde {ar:لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا, tr:lâ yukdâ aleyhim fe-yemûtû ve lâ yuhaffefu anhum min azâbihâ, gloss:haklarında ölmeleri için hüküm verilmez, azabı da onlardan hafifletilmez, source:35:36} denir. Bu ayet de bizim ayet gibi iki olumsuzlukla kurulmuştur. Suçluların cehennem azabında olduğu anlatılan bir başka yerde azabın {ar:لَا يُفَتَّرُ عَنْهُمْ وَهُمْ فِيهِ مُبْلِسُونَ, tr:lâ yufetteru anhum ve hum fîhi mublisûn, gloss:onlardan gevşetilmez, onlar da orada umutsuz kalırlar, source:43:75} olduğu söylenir. Ardından bekçiye seslenip yalnızca ölüm isterler: {ar:يَٰمَٰلِكُ لِيَقْضِ عَلَيْنَا رَبُّكَ, tr:yâ mâliku li-yakdi aleynâ rabbuk, gloss:Ey Mâlik, Rabbin işimizi bitirsin, source:43:77}. Aldıkları cevap tek kelimedir: {ar:إِنَّكُم مَّٰكِثُونَ, tr:innekum mâkiŝûn, gloss:siz kalacaksınız, source:43:77}. Her zorbanın hüsrana uğradığının anlatıldığı yerde de cehennemde irinli su içirilen kişi için {ar:وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ, tr:ve ye'tîhi'l-mevtu min kulli mekânin ve mâ huve bi-meyyit, gloss:ölüm ona her yandan gelir ama o ölmez, source:14:17} denir. Ölümün bütün sebepleri oradadır, sadece sonucu gelmez.

[¶8] Bu "ölmeyiş"in nasıl işlediğini Kur'an bir yerde açıkça gösterir. Ayetleri inkâr edenler için şöyle denir: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ, tr:kullemâ nadıcet culûduhum beddelnâhum culûden ğayrahâ li-yeẕûku'l-azâb, gloss:derileri piştikçe azabı tatsınlar diye onları başka derilerle değiştiririz, source:4:56}. Ateş, bir şeyi tüketip gücünü bitirerek dindiren şeydir. Ama orada tükenen yenilenir. Gücün çekilmesi demek olan ölüm hiçbir zaman tamamlanmaz. Yenilemenin amacı da açıkça söylenir: tatsınlar diye. Ölmeyen şey, acıyı duyma gücüdür.

## Hayatın kıpırtısı

[¶9] Ayetin ikinci fiili يَحْيَىٰ "yaşar" demektir. Arapça hayatı da tek katlı görmez. Hayat kelimesinin {ar:الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية, tr:el-hayâtu tusta'melu li'l-kuvveti'n-nâmiyeti ve'l-hassâseti ve'l-âkıleti ve'l-uhreviyye, gloss:hayat büyüyen güç, duyan güç, akleden güç ve ahiret hayatı için kullanılır, source:"ح ي ي,B001"} anlamlarında kullanıldığı söylenir. Bunun karşılığı olarak da {ar:أنواع الموت بحسب أنواع الحياة, tr:envâ'u'l-mevti bi-hasebi envâ'i'l-hayât, gloss:ölümün türleri hayatın türlerine göredir, source:"م و ت,B001"} denir. Ayeti bu katmanlarla okumak bir yorumdur, ama kelimelerin taşıdığı bir yorumdur. Duyma gücü ateştekinde kalır. Derileri yenilenen kişi tam da bu güç yüzünden "ölmez". Büyüme, akıl ve ahiret hayatı ise ondan esirgenir. Bu yüzden "yaşamaz".

[¶10] Hayatın büyüme katmanı Arapçada yağmura ve ota bağlanır. {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura "hayâ" denir, çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. Diri ot da şöyle tanımlanır: {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezz, gloss:bitkinin dirisi, taze olup kıpırdayanıdır, source:"ح ي ي,B002"}. Ölü toprağı ise iki kök aynı cümlede anlatır: {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtânu'l-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân, ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Kur'an bu iki hali aynı kelimelerle sahneler. Yeniden dirilişten kuşku duyan insanlara Allah, kendilerini topraktan, sonra damladan nasıl yarattığını anlatır ve şöyle devam eder: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tere'l-arda hâmideten fe-iẕâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri kupkuru ve kıpırtısız görürsün; üzerine suyu indirdiğimizde kıpırdar ve kabarır, source:22:5}. Buradaki hâmide kelimesinin fiili همد, Arapların uyuyan adam için "öldü" fiilinin yanına koydukları fiilin ta kendisidir. Kur'an'da ölü yer kıpırtısız yerdir, diri yer ise suyla titreyip kabaran yerdir. Başka bir ayet aynı sahneden sonuca geçer: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:inne'lleẕî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten, ölüleri de elbette diriltendir, source:41:39}.

[¶11] Ateşteki kişi bu iki halin hiçbirinde değildir. Ne kuru toprağın sessizliği ondadır ne de yağmur yemiş otun kıpırtısı. Surenin dördüncü ve beşinci ayetlerinin sözleri bir otlağın filizden kara döküntüye uzanan yolunu anlatır. On üçüncü ayetin kişisi bu yolun hiçbir durağında yer almaz. Bir de şu var: Araplar közü üfleyip harlatmaya da "diriltmek" derlerdi {source:"ح ي ي,B001"}. Ayetin anlattığı yerde ateş sürekli diri tutulur. İçindeki insan ise diri değildir. Bu bir dil yankısıdır, ayet bunu söylemez. Ama sahneyi keskinleştirir.

[¶12] Hayatın bir anlamı daha vardır ve sure içinde en çok iş gören anlam budur. Bir adam için {ar:ليس بفلان حياة أي ليس عنده نفع ولا خير, tr:leyse bi-fulânin hayâtun ey leyse indehû nef'un ve lâ hayr, gloss:falancada hayat yok, yani onda ne fayda var ne hayır, source:"ح ي ي,B013"} denirdi. Hayat burada fayda ve hayır demektir. Bu cümledeki iki kelime surede de geçer. Dokuzuncu ayet {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefe'ati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt fayda verirse, source:87:9} der. On yedinci ayet ahireti "daha hayırlı" diye niteler. "Yaşamaz" sözü bu anlamın yanında duyulduğunda başka bir şey daha söyler: ona ne bir fayda ulaşır ne de ondan bir hayır çıkar. Kendisine fayda verecek öğütten kaçan kişi sonunda faydanın hiç ulaşmadığı bir hale düşer.

## Diri olana öğüt

[¶13] Kur'an "diri" ve "ölü" kelimelerini ahiretten önce de, öğüdü kabul edenler ve etmeyenler için kullanır. Allah, Peygamber'e şiir öğretmediğini ve indirilenin {ar:إِنْ هُوَ إِلَّا ذِكْرٌۭ وَقُرْءَانٌۭ مُّبِينٌۭ, tr:in huve illâ ẕikrun ve kur'ânun mubîn, gloss:o bir öğüt ve apaçık bir Kur'an'dan başka bir şey değildir, source:36:69} olduğunu söyler. Hemen ardından bu öğüdün amacını bildirir: {ar:لِّيُنذِرَ مَن كَانَ حَيًّۭا, tr:li-yunẕira men kâne hayyâ, gloss:diri olanı uyarsın diye, source:36:70}. Görenle görmeyenin, aydınlıkla karanlığın eşit olmadığını sayan ayetlerin ardından {ar:وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ, tr:ve mâ yestevi'l-ahyâu ve le'l-emvât, gloss:diriler ile ölüler bir olmaz, source:35:22} denir ve Peygamber'e {ar:وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ, tr:ve mâ ente bi-musmi'in men fi'l-kubûr, gloss:sen kabirdekilere duyuramazsın, source:35:22} diye seslenilir. Bir başka yerde Allah şöyle sorar: {ar:أَوَمَن كَانَ مَيْتًۭا فَأَحْيَيْنَٰهُ وَجَعَلْنَا لَهُۥ نُورًۭا يَمْشِى بِهِۦ فِى ٱلنَّاسِ, tr:e-ve-men kâne meyten fe-ahyeynâhu ve ce'alnâ lehû nûran yemşî bihî fi'n-nâs, gloss:ölüyken dirilttiğimiz ve insanlar arasında yürüdüğü bir ışık verdiğimiz kimse, source:6:122}. Böyle biri karanlıklarda kalıp oradan çıkamayan biriyle bir olur mu? İnananlara da {ar:ٱسْتَجِيبُوا۟ لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا يُحْيِيكُمْ, tr:istecîbû lillâhi ve li'r-resûli iẕâ de'âkum li-mâ yuhyîkum, gloss:sizi size hayat verecek şeye çağırdığında Allah'a ve Elçi'ye karşılık verin, source:8:24} denir. Arapların gündelik dili de aynı yöndedir. Kavrayışı kıt kişiye {ar:رجل موتان الفؤاد إذا كان غير ذكي ولا فهم, tr:raculun mevtânu'l-fuâdi iẕâ kâne ğayra ẕekiyyin ve lâ fehim, gloss:zeki ve anlayışlı değilse "yüreği ölü adam" denir, source:"م و ت,B006"} derlerdi.

[¶14] Bu kullanım, surenin onuncu ve on birinci ayetlerindeki ayrımı yeni bir ışıkta gösterir. {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}. Kur'an'ın dilinde öğüdü duyan diridir. Öğütten kaçan kişi ise kendisine hayat verecek çağrıya sırtını dönmüştür. On üçüncü ayetin hali, o kişinin seçtiği bir halin kalıcı olmuş sonucu gibi okunabilir. Ayet bunu açıkça söylemez. Bu bağı Kur'an'ın diri ve ölü kelimelerini nasıl kullandığı kurar. Hayata çağrıldığında gelmeyen, sonunda hayatın hiç verilmediği bir yere düşer. Ama ölüm de verilmez, yani yok olup gitmek de ona açık değildir.

[¶15] Öğüdün geç kalınca bir işe yaramadığını Kur'an başka bir surede söyler. Cehennemin getirildiği gün için {ar:يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ, tr:yevmeiẕin yeteẕekkeru'l-insânu ve ennâ lehu'ẕ-ẕikrâ, gloss:o gün insan hatırlar, ama o hatırlamanın ona ne faydası olur, source:89:23} denir. Buradaki "öğüt" kelimesi dokuzuncu ayettekiyle aynıdır. O gün insanın söylediği ise şudur: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:"Keşke hayatım için önceden bir şey gönderseydim" der, source:89:24}. O anda "hayatım" diye andığı şey, geride bıraktığı dünya değildir, önündeki hayattır. On üçüncü ayetteki kişi, ne yazık ki, o hayat için hiçbir şey göndermemiştir.

## Tercih edilen hayat

[¶16] Sure, ayetimizden üç ayet sonra aynı kökü yeniden kullanır: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır, siz yakın hayatı öne alıyorsunuz, source:87:16}. Hemen ardından da {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17} der. On üçüncü ayetteki "yaşamaz" fiili ile on altıncı ayetteki "hayat" aynı köktendir. Bu yüzden sure kendi içinde acı bir denge kurar. Hayatı seçtiğini sanan kişi sonunda hayatsız kalır. Seçtiği, hayatın yakın ve kısa olan biçimiydi. Bıraktığı ise asıl hayattı.

[¶17] Kur'an bu asıl hayata ayrı bir kelimeyle ad verir: {ar:وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ, tr:ve mâ hâẕihi'l-hayâtu'd-dunyâ illâ lehvun ve le'ib, gloss:bu dünya hayatı bir oyalanma ve oyundan başka bir şey değildir, source:29:64}, {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve inne'd-dâre'l-âhirete le-hiye'l-hayevân, gloss:ahiret yurdu ise asıl hayatın ta kendisidir, source:29:64}. Türkçede "hayvan" kelimesi bu Arapça kelimeden gelir. Ama Türkçede yalnızca insan dışındaki canlıları anlatır, hatta hakaret olarak da kullanılır. Kelimenin aslı ise {ar:الحيوان كل ذي روح, tr:el-hayevânu kullu ẕî rûh, gloss:hayevân, ruhu olan her varlıktır, source:"ح ي ي,B003"} diye tanımlanır. Kelimenin daha derin bir anlamı da vardır: {ar:الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي, tr:el-hayevânu makarru'l-hayâti ve mâ lehu'l-hâssetu ve mâ lehu'l-bekâu'l-ebediyy, gloss:hayevân hayatın yurdudur, duyusu olan ve sonsuz kalıcılığı bulunandır, source:"ح ي ي,B003"}. Kur'an ahirete bu kelimeyle ad verdiğinde, hayatın en dolu ve en kalıcı halini kasteder. On üçüncü ayetteki kişi, ahirette tam da bu hayatı yaşamaz.

[¶18] Bu ayetin cümlesi Kur'an'da kelimesi kelimesine başka bir sahnede de geçer. Firavun'un sihirbazları Musa'nın karşısında secdeye kapanıp iman ederler. Firavun onları el ve ayaklarını çaprazlama kesmekle tehdit eder. Sihirbazlar ona {ar:إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:innemâ takdî hâẕihi'l-hayâte'd-dunyâ, gloss:sen ancak bu yakın hayatta hüküm verebilirsin, source:20:72} der, ardından da {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} diye ekler. Sonra iki ucu anlatırlar: {ar:مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:men ye'ti rabbehû mucrimen fe-inne lehû cehenneme lâ yemûtu fîhâ ve lâ yahyâ, gloss:Rabbine suçlu olarak gelene cehennem vardır; orada ne ölür ne yaşar, source:20:74}. Öbür ucu da şöyle bağlarlar: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu da arınanın karşılığıdır, source:20:76}. Ölümle tehdit edilen bu insanlar, asıl korkulacak şeyin ölüm olmadığını bilirler. Asıl korkulacak olan, ölümün bile gelmediği yerdir.

## Yahya: aynı harfler, bir ad

[¶19] Ayetin son kelimesi يَحْيَىٰ, Kur'an'da aynı harflerle bir peygamberin adı olarak da geçer. Yaşlı Zekeriya Rabbine gizlice yalvarıp bir varis ister ve şu müjdeyi alır: {ar:يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ, tr:yâ zekeriyyâ innâ nubeşşiruke bi-ğulâmin ismuhû yahyâ, gloss:Ey Zekeriya, sana adı Yahya olan bir oğul müjdeliyoruz, source:19:7}. Ayetimizde kelime bir fiildir, "yaşar" demektir. Orada ise bir addır. İkisi aynı kökten gelir ve yazılışları aynıdır, ama anlamları bir değildir. Bu adı açıklarken {ar:اسمه يحيى نبه أنه سماه بذلك من حيث إنه لم تمته الذنوب, tr:ismuhû yahyâ nebbehe ennehû semmâhu bi-ẕâlike min haysu innehû lem tumithu'ẕ-ẕunûb, gloss:"adı Yahya" sözü, ona bu adın günahlar onu öldürmediği için verildiğine işaret eder, source:"ح ي ي,B014"} denmiştir.

[¶20] Kur'an Yahya'yı anlatırken ayetimizin iki kökünü de kullanır. Ona {ar:يَٰيَحْيَىٰ خُذِ ٱلْكِتَٰبَ بِقُوَّةٍۢ, tr:yâ yahyâ huẕi'l-kitâbe bi-kuvve, gloss:Ey Yahya, Kitab'ı güçle tut, source:19:12} denir. Ölümün "gücün çekilmesi" olduğunu hatırlarsak, bu hitap Yahya'nın tam tersine güçle donatıldığını gösterir. Ona {ar:وَحَنَانًۭا مِّن لَّدُنَّا وَزَكَوٰةًۭ, tr:ve hanânen min ledunnâ ve zekâten, gloss:katımızdan bir şefkat ve arınmışlık, source:19:13} verildiği de söylenir. Buradaki arınmışlık, surenin on dördüncü ayetindeki {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kurtuluşa erdi, source:87:14} sözüyle aynı köktendir. Yahya anlatısı şu sözle kapanır: {ar:وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا, tr:ve selâmun aleyhi yevme vulide ve yevme yemûtu ve yevme yub'asu hayyâ, gloss:doğduğu gün, öleceği gün ve diri olarak kaldırılacağı gün ona selam olsun, source:19:15}. Annesi suçlandığında beşikten konuşan İsa da kendisi için aynı sözü söyler: {ar:وَٱلسَّلَٰمُ عَلَىَّ يَوْمَ وُلِدتُّ وَيَوْمَ أَمُوتُ وَيَوْمَ أُبْعَثُ حَيًّۭا, tr:ve's-selâmu aleyye yevme vulidtu ve yevme emûtu ve yevme ub'asu hayyâ, gloss:doğduğum gün, öleceğim gün ve diri olarak kaldırılacağım gün bana selam olsun, source:19:33}.

[¶21] İki sahne yan yana konunca karşıtlık açıkça görünür. Yahya için yemûtu fiili esenlikle gelen bir gündür. Hayy, yani diri olmak, onun dirilişinin niteliğidir. Ölüm de hayat da ona birer kapı olarak açılır ve ikisinin üzerinde de selam vardır. On üçüncü ayetteki kişi için aynı iki fiil olumsuzdur. Onun ne ölüm günü vardır ne diri kalkış günü. Bunun yerine sonu gelmeyen bir "orada" vardır. Adı "yaşar" olan peygamber ile hakkında "yaşamaz" denen kişi arasındaki fark, on dördüncü ayetin arınması ile on birinci ayetin kaçınması arasındaki farktır.

===== _commentary/v16/out/87_13/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: thumma marks distance in rank as well as in time
- memory: imperfect yamūtu/yaḥyā here denotes an ongoing state
- memory: hāmida (22:5) means still, lifeless earth, from root ه م د
- memory: ihtazza means to stir or quiver
- memory: Turkish "hayvan" narrowed to non-human animal, also an insult
- memory: aḥyā al-nār (to kindle a fire) given only as a Turkish sense
- not written: ح ي ي B009 ḥayya ʿalā l-ṣalāh beside 87:15 - only a sound echo, would be wordplay
- not written: ح ي ي B005 shame (Turkish hayâ) - did nothing for any theme
- not written: ح ي ي B004, B010, B011, B012 snake, tribe, womb, face - no work here
- not written: ح ي ي B006/B013 sparing a life, saving from ruin - overlaps the benefit sense
- not written: ح ي ي B007/B008 taḥiyya greeting/sovereignty - no link to the negation
- not written: م و ت B005, B007, B010, B011, B013, B014 - off theme
- not written: 67:2 death and life created as a test - crowded the first section
- not written: 74:28 fire neither spares nor leaves - overlaps 4:56, root link weak
- not written: 25:13-14 crying out for ruin - repeats 43:77
- not written: 43:77 mākithūn tied to the flood scene of 13:17 - belongs to the surah commentary's scene

===== passages not cited (247) =====
## strong (this ayah's own list) (10)

- (5:37) [listed for 87:13] يُرِيدُونَ أَن يَخْرُجُوا۟ مِنَ ٱلنَّارِ وَمَا هُم بِخَٰرِجِينَ مِنْهَا ۖ وَلَهُمْ عَذَابٌۭ مُّقِيمٌۭ
- (6:122) [listed for 87:13] [cited in ¶13] أَوَمَن كَانَ مَيْتًۭا فَأَحْيَيْنَٰهُ وَجَعَلْنَا لَهُۥ نُورًۭا يَمْشِى بِهِۦ فِى ٱلنَّاسِ كَمَن مَّثَلُهُۥ فِى ٱلظُّلُمَٰتِ لَيْسَ بِخَارِجٍۢ مِّنْهَا ۚ كَذَٰلِكَ زُيِّنَ لِلْكَٰفِرِينَ مَا كَانُوا۟ يَعْمَلُونَ
- (14:17) [listed for 87:13] [cited in ¶7] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
- (20:74) [listed for 87:13] [cited in ¶18] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (22:22) [listed for 87:13] كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (25:49) [listed for 87:13] لِّنُحْۦِىَ بِهِۦ بَلْدَةًۭ مَّيْتًۭا وَنُسْقِيَهُۥ مِمَّا خَلَقْنَآ أَنْعَٰمًۭا وَأَنَاسِىَّ كَثِيرًۭا
- (32:20) [listed for 87:13] وَأَمَّا ٱلَّذِينَ فَسَقُوا۟ فَمَأْوَىٰهُمُ ٱلنَّارُ ۖ كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَآ أُعِيدُوا۟ فِيهَا وَقِيلَ لَهُمْ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (35:36) [listed for 87:13] [cited in ¶7] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (43:77) [listed for 87:13] [cited in ¶7] وَنَادَوْا۟ يَٰمَٰلِكُ لِيَقْضِ عَلَيْنَا رَبُّكَ ۖ قَالَ إِنَّكُم مَّٰكِثُونَ
- (74:28) [listed for 87:13] لَا تُبْقِى وَلَا تَذَرُ

## medium (this ayah's own list) (90)

- (2:28) [listed for 87:13] [cited in ¶3] كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ
- (2:86) [listed for 87:13] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
- (2:154) [listed for 87:13] وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۢ ۚ بَلْ أَحْيَآءٌۭ وَلَٰكِن لَّا تَشْعُرُونَ
- (2:162) [listed for 87:13] خَٰلِدِينَ فِيهَا ۖ لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (2:167) [listed for 87:13] وَقَالَ ٱلَّذِينَ ٱتَّبَعُوا۟ لَوْ أَنَّ لَنَا كَرَّةًۭ فَنَتَبَرَّأَ مِنْهُمْ كَمَا تَبَرَّءُوا۟ مِنَّا ۗ كَذَٰلِكَ يُرِيهِمُ ٱللَّهُ أَعْمَٰلَهُمْ حَسَرَٰتٍ عَلَيْهِمْ ۖ وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ
- (3:88) [listed for 87:13] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (3:185) [listed for 87:13] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (4:56) [listed for 87:13] [cited in ¶8] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
- (4:78) [listed for 87:13] أَيْنَمَا تَكُونُوا۟ يُدْرِككُّمُ ٱلْمَوْتُ وَلَوْ كُنتُمْ فِى بُرُوجٍۢ مُّشَيَّدَةٍۢ ۗ وَإِن تُصِبْهُمْ حَسَنَةٌۭ يَقُولُوا۟ هَٰذِهِۦ مِنْ عِندِ ٱللَّهِ ۖ وَإِن تُصِبْهُمْ سَيِّئَةٌۭ يَقُولُوا۟ هَٰذِهِۦ مِنْ عِندِكَ ۚ قُلْ كُلٌّۭ مِّنْ عِندِ ٱللَّهِ ۖ فَمَالِ هَٰٓؤُلَآءِ ٱلْقَوْمِ لَا يَكَادُونَ يَفْقَهُونَ حَدِيثًۭا
- (6:29) [listed for 87:13] وَقَالُوٓا۟ إِنْ هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا وَمَا نَحْنُ بِمَبْعُوثِينَ
- (6:36) [listed for 87:13] ۞ إِنَّمَا يَسْتَجِيبُ ٱلَّذِينَ يَسْمَعُونَ ۘ وَٱلْمَوْتَىٰ يَبْعَثُهُمُ ٱللَّهُ ثُمَّ إِلَيْهِ يُرْجَعُونَ
- (6:60) [listed for 87:13] وَهُوَ ٱلَّذِى يَتَوَفَّىٰكُم بِٱلَّيْلِ وَيَعْلَمُ مَا جَرَحْتُم بِٱلنَّهَارِ ثُمَّ يَبْعَثُكُمْ فِيهِ لِيُقْضَىٰٓ أَجَلٌۭ مُّسَمًّۭى ۖ ثُمَّ إِلَيْهِ مَرْجِعُكُمْ ثُمَّ يُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (6:95) [listed for 87:13] ۞ إِنَّ ٱللَّهَ فَالِقُ ٱلْحَبِّ وَٱلنَّوَىٰ ۖ يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَمُخْرِجُ ٱلْمَيِّتِ مِنَ ٱلْحَىِّ ۚ ذَٰلِكُمُ ٱللَّهُ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (7:25) [listed for 87:13] [cited in ¶3] قَالَ فِيهَا تَحْيَوْنَ وَفِيهَا تَمُوتُونَ وَمِنْهَا تُخْرَجُونَ
- (7:36) [listed for 87:13] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا وَٱسْتَكْبَرُوا۟ عَنْهَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (7:57) [listed for 87:13] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
- (8:24) [listed for 87:13] [cited in ¶13] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَجِيبُوا۟ لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا يُحْيِيكُمْ ۖ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَحُولُ بَيْنَ ٱلْمَرْءِ وَقَلْبِهِۦ وَأَنَّهُۥٓ إِلَيْهِ تُحْشَرُونَ
- (8:42) [listed for 87:13] إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ وَٱلرَّكْبُ أَسْفَلَ مِنكُمْ ۚ وَلَوْ تَوَاعَدتُّمْ لَٱخْتَلَفْتُمْ فِى ٱلْمِيعَٰدِ ۙ وَلَٰكِن لِّيَقْضِىَ ٱللَّهُ أَمْرًۭا كَانَ مَفْعُولًۭا لِّيَهْلِكَ مَنْ هَلَكَ عَنۢ بَيِّنَةٍۢ وَيَحْيَىٰ مَنْ حَىَّ عَنۢ بَيِّنَةٍۢ ۗ وَإِنَّ ٱللَّهَ لَسَمِيعٌ عَلِيمٌ
- (9:68) [listed for 87:13] وَعَدَ ٱللَّهُ ٱلْمُنَٰفِقِينَ وَٱلْمُنَٰفِقَٰتِ وَٱلْكُفَّارَ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ ۚ وَلَعَنَهُمُ ٱللَّهُ ۖ وَلَهُمْ عَذَابٌۭ مُّقِيمٌۭ
- (9:125) [listed for 87:13] وَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ فَزَادَتْهُمْ رِجْسًا إِلَىٰ رِجْسِهِمْ وَمَاتُوا۟ وَهُمْ كَٰفِرُونَ
- (10:56) [listed for 87:13] هُوَ يُحْىِۦ وَيُمِيتُ وَإِلَيْهِ تُرْجَعُونَ
- (11:106) [listed for 87:13] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (15:23) [listed for 87:13] وَإِنَّا لَنَحْنُ نُحْىِۦ وَنُمِيتُ وَنَحْنُ ٱلْوَٰرِثُونَ
- (16:21) [listed for 87:13] أَمْوَٰتٌ غَيْرُ أَحْيَآءٍۢ ۖ وَمَا يَشْعُرُونَ أَيَّانَ يُبْعَثُونَ
- (16:29) [listed for 87:13] فَٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَلَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (16:38) [listed for 87:13] وَأَقْسَمُوا۟ بِٱللَّهِ جَهْدَ أَيْمَٰنِهِمْ ۙ لَا يَبْعَثُ ٱللَّهُ مَن يَمُوتُ ۚ بَلَىٰ وَعْدًا عَلَيْهِ حَقًّۭا وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (16:65) [listed for 87:13] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
- (16:97) [listed for 87:13] مَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَلَنُحْيِيَنَّهُۥ حَيَوٰةًۭ طَيِّبَةًۭ ۖ وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (17:75) [listed for 87:13] إِذًۭا لَّأَذَقْنَٰكَ ضِعْفَ ٱلْحَيَوٰةِ وَضِعْفَ ٱلْمَمَاتِ ثُمَّ لَا تَجِدُ لَكَ عَلَيْنَا نَصِيرًۭا
- (18:29) [listed for 87:13] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
- (19:15) [listed for 87:13] [cited in ¶20] وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا
- (19:33) [listed for 87:13] [cited in ¶20] وَٱلسَّلَٰمُ عَلَىَّ يَوْمَ وُلِدتُّ وَيَوْمَ أَمُوتُ وَيَوْمَ أُبْعَثُ حَيًّۭا
- (19:72) [listed for 87:13] ثُمَّ نُنَجِّى ٱلَّذِينَ ٱتَّقَوا۟ وَّنَذَرُ ٱلظَّٰلِمِينَ فِيهَا جِثِيًّۭا
- (21:35) [listed for 87:13] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ ۖ وَإِلَيْنَا تُرْجَعُونَ
- (22:5) [listed for 87:13] [cited in ¶10] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
- (22:7) [listed for 87:13] وَأَنَّ ٱلسَّاعَةَ ءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ
- (22:66) [listed for 87:13] وَهُوَ ٱلَّذِىٓ أَحْيَاكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ۗ إِنَّ ٱلْإِنسَٰنَ لَكَفُورٌۭ
- (23:15) [listed for 87:13] ثُمَّ إِنَّكُم بَعْدَ ذَٰلِكَ لَمَيِّتُونَ
- (23:82) [listed for 87:13] قَالُوٓا۟ أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَبْعُوثُونَ
- (23:99) [listed for 87:13] حَتَّىٰٓ إِذَا جَآءَ أَحَدَهُمُ ٱلْمَوْتُ قَالَ رَبِّ ٱرْجِعُونِ
- (23:103) [listed for 87:13] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (23:108) [listed for 87:13] قَالَ ٱخْسَـُٔوا۟ فِيهَا وَلَا تُكَلِّمُونِ
- (25:58) [listed for 87:13] وَتَوَكَّلْ عَلَى ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ وَسَبِّحْ بِحَمْدِهِۦ ۚ وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا
- (25:65) [listed for 87:13] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا
- (25:66) [listed for 87:13] إِنَّهَا سَآءَتْ مُسْتَقَرًّۭا وَمُقَامًۭا
- (26:81) [listed for 87:13] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (29:54) [listed for 87:13] يَسْتَعْجِلُونَكَ بِٱلْعَذَابِ وَإِنَّ جَهَنَّمَ لَمُحِيطَةٌۢ بِٱلْكَٰفِرِينَ
- (30:19) [listed for 87:13] يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَيُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ وَكَذَٰلِكَ تُخْرَجُونَ
- (30:50) [listed for 87:13] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (30:52) [listed for 87:13] فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (33:65) [listed for 87:13] خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّا يَجِدُونَ وَلِيًّۭا وَلَا نَصِيرًۭا
- (35:9) [listed for 87:13] وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ
- (36:12) [listed for 87:13] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
- (36:33) [listed for 87:13] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
- (36:51) [listed for 87:13] وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ
- (36:78) [listed for 87:13] وَضَرَبَ لَنَا مَثَلًۭا وَنَسِىَ خَلْقَهُۥ ۖ قَالَ مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌۭ
- (36:79) [listed for 87:13] قُلْ يُحْيِيهَا ٱلَّذِىٓ أَنشَأَهَآ أَوَّلَ مَرَّةٍۢ ۖ وَهُوَ بِكُلِّ خَلْقٍ عَلِيمٌ
- (37:58) [listed for 87:13] أَفَمَا نَحْنُ بِمَيِّتِينَ
- (39:30) [listed for 87:13] إِنَّكَ مَيِّتٌۭ وَإِنَّهُم مَّيِّتُونَ
- (39:42) [listed for 87:13] [cited in ¶6] ٱللَّهُ يَتَوَفَّى ٱلْأَنفُسَ حِينَ مَوْتِهَا وَٱلَّتِى لَمْ تَمُتْ فِى مَنَامِهَا ۖ فَيُمْسِكُ ٱلَّتِى قَضَىٰ عَلَيْهَا ٱلْمَوْتَ وَيُرْسِلُ ٱلْأُخْرَىٰٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّى ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (39:72) [listed for 87:13] قِيلَ ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (40:11) [listed for 87:13] قَالُوا۟ رَبَّنَآ أَمَتَّنَا ٱثْنَتَيْنِ وَأَحْيَيْتَنَا ٱثْنَتَيْنِ فَٱعْتَرَفْنَا بِذُنُوبِنَا فَهَلْ إِلَىٰ خُرُوجٍۢ مِّن سَبِيلٍۢ
- (40:68) [listed for 87:13] هُوَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ ۖ فَإِذَا قَضَىٰٓ أَمْرًۭا فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ
- (40:76) [listed for 87:13] ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (41:28) [listed for 87:13] ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (41:39) [listed for 87:13] [cited in ¶10] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (42:9) [listed for 87:13] أَمِ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ ۖ فَٱللَّهُ هُوَ ٱلْوَلِىُّ وَهُوَ يُحْىِ ٱلْمَوْتَىٰ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (43:74) [listed for 87:13] إِنَّ ٱلْمُجْرِمِينَ فِى عَذَابِ جَهَنَّمَ خَٰلِدُونَ
- (45:26) [listed for 87:13] قُلِ ٱللَّهُ يُحْيِيكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يَجْمَعُكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (50:3) [listed for 87:13] أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا ۖ ذَٰلِكَ رَجْعٌۢ بَعِيدٌۭ
- (50:11) [listed for 87:13] رِّزْقًۭا لِّلْعِبَادِ ۖ وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ ٱلْخُرُوجُ
- (50:43) [listed for 87:13] إِنَّا نَحْنُ نُحْىِۦ وَنُمِيتُ وَإِلَيْنَا ٱلْمَصِيرُ
- (53:44) [listed for 87:13] وَأَنَّهُۥ هُوَ أَمَاتَ وَأَحْيَا
- (56:60) [listed for 87:13] نَحْنُ قَدَّرْنَا بَيْنَكُمُ ٱلْمَوْتَ وَمَا نَحْنُ بِمَسْبُوقِينَ
- (57:17) [listed for 87:13] ٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَعْقِلُونَ
- (58:17) [listed for 87:13] لَّن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (62:6) [listed for 87:13] قُلْ يَٰٓأَيُّهَا ٱلَّذِينَ هَادُوٓا۟ إِن زَعَمْتُمْ أَنَّكُمْ أَوْلِيَآءُ لِلَّهِ مِن دُونِ ٱلنَّاسِ فَتَمَنَّوُا۟ ٱلْمَوْتَ إِن كُنتُمْ صَٰدِقِينَ
- (62:8) [listed for 87:13] قُلْ إِنَّ ٱلْمَوْتَ ٱلَّذِى تَفِرُّونَ مِنْهُ فَإِنَّهُۥ مُلَٰقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (64:7) [listed for 87:13] زَعَمَ ٱلَّذِينَ كَفَرُوٓا۟ أَن لَّن يُبْعَثُوا۟ ۚ قُلْ بَلَىٰ وَرَبِّى لَتُبْعَثُنَّ ثُمَّ لَتُنَبَّؤُنَّ بِمَا عَمِلْتُمْ ۚ وَذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (67:2) [listed for 87:13] ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
- (72:23) [listed for 87:13] إِلَّا بَلَٰغًۭا مِّنَ ٱللَّهِ وَرِسَٰلَٰتِهِۦ ۚ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَإِنَّ لَهُۥ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَآ أَبَدًا
- (75:40) [listed for 87:13] أَلَيْسَ ذَٰلِكَ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ
- (78:21) [listed for 87:13] إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا
- (78:24) [listed for 87:13] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (80:21) [listed for 87:13] ثُمَّ أَمَاتَهُۥ فَأَقْبَرَهُۥ
- (88:4) [listed for 87:13] تَصْلَىٰ نَارًا حَامِيَةًۭ
- (88:11) [listed for 87:13] لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- (89:24) [listed for 87:13] [cited in ¶15] يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- (90:19) [listed for 87:13] وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- (98:6) [listed for 87:13] إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ

## named by the passage's own list as strong for this ayah (11)

- (43:75) [listed for 87:13] [cited in ¶7] لَا يُفَتَّرُ عَنْهُمْ وَهُمْ فِيهِ مُبْلِسُونَ
- (54:48) [listed for 87:13] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (78:23) [listed for 87:13] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (79:38) [listed for 87:13] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (82:14) [listed for 87:13] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (82:16) [listed for 87:13] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
- (85:5) [listed for 87:13] ٱلنَّارِ ذَاتِ ٱلْوَقُودِ
- (90:20) [listed for 87:13] عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ
- (92:14) [listed for 87:13] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:15) [listed for 87:13] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (101:11) [listed for 87:13] نَارٌ حَامِيَةٌۢ

## named by the passage's own list as medium for this ayah (17)

- (2:56) [listed for 87:13] ثُمَّ بَعَثْنَٰكُم مِّنۢ بَعْدِ مَوْتِكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (2:175) [listed for 87:13] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ وَٱلْعَذَابَ بِٱلْمَغْفِرَةِ ۚ فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ
- (5:32) [listed for 87:13] مِنْ أَجْلِ ذَٰلِكَ كَتَبْنَا عَلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ أَنَّهُۥ مَن قَتَلَ نَفْسًۢا بِغَيْرِ نَفْسٍ أَوْ فَسَادٍۢ فِى ٱلْأَرْضِ فَكَأَنَّمَا قَتَلَ ٱلنَّاسَ جَمِيعًۭا وَمَنْ أَحْيَاهَا فَكَأَنَّمَآ أَحْيَا ٱلنَّاسَ جَمِيعًۭا ۚ وَلَقَدْ جَآءَتْهُمْ رُسُلُنَا بِٱلْبَيِّنَٰتِ ثُمَّ إِنَّ كَثِيرًۭا مِّنْهُم بَعْدَ ذَٰلِكَ فِى ٱلْأَرْضِ لَمُسْرِفُونَ
- (7:41) [listed for 87:13] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (14:23) [listed for 87:13] وَأُدْخِلَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا بِإِذْنِ رَبِّهِمْ ۖ تَحِيَّتُهُمْ فِيهَا سَلَٰمٌ
- (19:71) [listed for 87:13] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (35:22) [listed for 87:13] [cited in ¶13] وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ ۚ إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ ۖ وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ
- (44:8) [listed for 87:13] لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ
- (44:35) [listed for 87:13] إِنْ هِىَ إِلَّا مَوْتَتُنَا ٱلْأُولَىٰ وَمَا نَحْنُ بِمُنشَرِينَ
- (45:35) [listed for 87:13] ذَٰلِكُم بِأَنَّكُمُ ٱتَّخَذْتُمْ ءَايَٰتِ ٱللَّهِ هُزُوًۭا وَغَرَّتْكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ لَا يُخْرَجُونَ مِنْهَا وَلَا هُمْ يُسْتَعْتَبُونَ
- (56:94) [listed for 87:13] وَتَصْلِيَةُ جَحِيمٍ
- (77:26) [listed for 87:13] أَحْيَآءًۭ وَأَمْوَٰتًۭا
- (81:12) [listed for 87:13] وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ
- (84:11) [listed for 87:13] فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
- (84:12) [listed for 87:13] وَيَصْلَىٰ سَعِيرًا
- (104:8) [listed for 87:13] إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- (104:9) [listed for 87:13] فِى عَمَدٍۢ مُّمَدَّدَةٍۭ

## weak (this ayah's own list) (31)

- (2:73) [listed for 87:13] فَقُلْنَا ٱضْرِبُوهُ بِبَعْضِهَا ۚ كَذَٰلِكَ يُحْىِ ٱللَّهُ ٱلْمَوْتَىٰ وَيُرِيكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
- (2:164) [listed for 87:13] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (2:179) [listed for 87:13] وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تَتَّقُونَ
- (2:243) [listed for 87:13] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ خَرَجُوا۟ مِن دِيَٰرِهِمْ وَهُمْ أُلُوفٌ حَذَرَ ٱلْمَوْتِ فَقَالَ لَهُمُ ٱللَّهُ مُوتُوا۟ ثُمَّ أَحْيَٰهُمْ ۚ إِنَّ ٱللَّهَ لَذُو فَضْلٍ عَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (2:258) [listed for 87:13] أَلَمْ تَرَ إِلَى ٱلَّذِى حَآجَّ إِبْرَٰهِۦمَ فِى رَبِّهِۦٓ أَنْ ءَاتَىٰهُ ٱللَّهُ ٱلْمُلْكَ إِذْ قَالَ إِبْرَٰهِۦمُ رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ قَالَ أَنَا۠ أُحْىِۦ وَأُمِيتُ ۖ قَالَ إِبْرَٰهِۦمُ فَإِنَّ ٱللَّهَ يَأْتِى بِٱلشَّمْسِ مِنَ ٱلْمَشْرِقِ فَأْتِ بِهَا مِنَ ٱلْمَغْرِبِ فَبُهِتَ ٱلَّذِى كَفَرَ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (2:259) [listed for 87:13] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (2:260) [listed for 87:13] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ أَرِنِى كَيْفَ تُحْىِ ٱلْمَوْتَىٰ ۖ قَالَ أَوَلَمْ تُؤْمِن ۖ قَالَ بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِى ۖ قَالَ فَخُذْ أَرْبَعَةًۭ مِّنَ ٱلطَّيْرِ فَصُرْهُنَّ إِلَيْكَ ثُمَّ ٱجْعَلْ عَلَىٰ كُلِّ جَبَلٍۢ مِّنْهُنَّ جُزْءًۭا ثُمَّ ٱدْعُهُنَّ يَأْتِينَكَ سَعْيًۭا ۚ وَٱعْلَمْ أَنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (3:27) [listed for 87:13] تُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَتُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ ۖ وَتُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَتُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ ۖ وَتَرْزُقُ مَن تَشَآءُ بِغَيْرِ حِسَابٍۢ
- (3:169) [listed for 87:13] وَلَا تَحْسَبَنَّ ٱلَّذِينَ قُتِلُوا۟ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتًۢا ۚ بَلْ أَحْيَآءٌ عِندَ رَبِّهِمْ يُرْزَقُونَ
- (9:126) [listed for 87:13] أَوَلَا يَرَوْنَ أَنَّهُمْ يُفْتَنُونَ فِى كُلِّ عَامٍۢ مَّرَّةً أَوْ مَرَّتَيْنِ ثُمَّ لَا يَتُوبُونَ وَلَا هُمْ يَذَّكَّرُونَ
- (10:31) [listed for 87:13] قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ أَمَّن يَمْلِكُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَمَن يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَمَن يُدَبِّرُ ٱلْأَمْرَ ۚ فَسَيَقُولُونَ ٱللَّهُ ۚ فَقُلْ أَفَلَا تَتَّقُونَ
- (16:84) [listed for 87:13] وَيَوْمَ نَبْعَثُ مِن كُلِّ أُمَّةٍۢ شَهِيدًۭا ثُمَّ لَا يُؤْذَنُ لِلَّذِينَ كَفَرُوا۟ وَلَا هُمْ يُسْتَعْتَبُونَ
- (17:49) [listed for 87:13] وَقَالُوٓا۟ أَءِذَا كُنَّا عِظَٰمًۭا وَرُفَٰتًا أَءِنَّا لَمَبْعُوثُونَ خَلْقًۭا جَدِيدًۭا
- (17:98) [listed for 87:13] ذَٰلِكَ جَزَآؤُهُم بِأَنَّهُمْ كَفَرُوا۟ بِـَٔايَٰتِنَا وَقَالُوٓا۟ أَءِذَا كُنَّا عِظَٰمًۭا وَرُفَٰتًا أَءِنَّا لَمَبْعُوثُونَ خَلْقًۭا جَدِيدًا
- (20:107) [listed for 87:13] لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا
- (20:118) [listed for 87:13] إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ
- (20:119) [listed for 87:13] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (22:6) [listed for 87:13] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّهُۥ يُحْىِ ٱلْمَوْتَىٰ وَأَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (23:80) [listed for 87:13] وَهُوَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ وَلَهُ ٱخْتِلَٰفُ ٱلَّيْلِ وَٱلنَّهَارِ ۚ أَفَلَا تَعْقِلُونَ
- (29:57) [listed for 87:13] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۖ ثُمَّ إِلَيْنَا تُرْجَعُونَ
- (29:63) [listed for 87:13] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
- (30:27) [listed for 87:13] وَهُوَ ٱلَّذِى يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ وَهُوَ أَهْوَنُ عَلَيْهِ ۚ وَلَهُ ٱلْمَثَلُ ٱلْأَعْلَىٰ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (35:35) [listed for 87:13] ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ
- (37:47) [listed for 87:13] لَا فِيهَا غَوْلٌۭ وَلَا هُمْ عَنْهَا يُنزَفُونَ
- (52:23) [listed for 87:13] يَتَنَٰزَعُونَ فِيهَا كَأْسًۭا لَّا لَغْوٌۭ فِيهَا وَلَا تَأْثِيمٌۭ
- (56:25) [listed for 87:13] لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا
- (71:18) [listed for 87:13] ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًۭا
- (75:26) [listed for 87:13] كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ
- (76:13) [listed for 87:13] مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۖ لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا
- (78:35) [listed for 87:13] لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا
- (88:7) [listed for 87:13] لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ

## named by the passage's own list as weak for this ayah (7)

- (23:37) [listed for 87:13] إِنْ هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا نَمُوتُ وَنَحْيَا وَمَا نَحْنُ بِمَبْعُوثِينَ
- (37:16) [listed for 87:13] أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَبْعُوثُونَ
- (40:59) [listed for 87:13] إِنَّ ٱلسَّاعَةَ لَءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (55:39) [listed for 87:13] فَيَوْمَئِذٍۢ لَّا يُسْـَٔلُ عَن ذَنۢبِهِۦٓ إِنسٌۭ وَلَا جَآنٌّۭ
- (56:19) [listed for 87:13] لَّا يُصَدَّعُونَ عَنْهَا وَلَا يُنزِفُونَ
- (56:44) [listed for 87:13] لَّا بَارِدٍۢ وَلَا كَرِيمٍ
- (68:44) [listed for 87:13] فَذَرْنِى وَمَن يُكَذِّبُ بِهَٰذَا ٱلْحَدِيثِ ۖ سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ

## neighbours: within two ayat of a passage the commentary cites (81)

- (2:26) [next to 2:28] ۞ إِنَّ ٱللَّهَ لَا يَسْتَحْىِۦٓ أَن يَضْرِبَ مَثَلًۭا مَّا بَعُوضَةًۭ فَمَا فَوْقَهَا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۖ وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَيَقُولُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۘ يُضِلُّ بِهِۦ كَثِيرًۭا وَيَهْدِى بِهِۦ كَثِيرًۭا ۚ وَمَا يُضِلُّ بِهِۦٓ إِلَّا ٱلْفَٰسِقِينَ
- (2:27) [next to 2:28] ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيُفْسِدُونَ فِى ٱلْأَرْضِ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (2:29) [next to 2:28] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (2:30) [next to 2:28] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى جَاعِلٌۭ فِى ٱلْأَرْضِ خَلِيفَةًۭ ۖ قَالُوٓا۟ أَتَجْعَلُ فِيهَا مَن يُفْسِدُ فِيهَا وَيَسْفِكُ ٱلدِّمَآءَ وَنَحْنُ نُسَبِّحُ بِحَمْدِكَ وَنُقَدِّسُ لَكَ ۖ قَالَ إِنِّىٓ أَعْلَمُ مَا لَا تَعْلَمُونَ
- (4:54) [next to 4:56] أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۖ فَقَدْ ءَاتَيْنَآ ءَالَ إِبْرَٰهِيمَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَءَاتَيْنَٰهُم مُّلْكًا عَظِيمًۭا
- (4:55) [next to 4:56] فَمِنْهُم مَّنْ ءَامَنَ بِهِۦ وَمِنْهُم مَّن صَدَّ عَنْهُ ۚ وَكَفَىٰ بِجَهَنَّمَ سَعِيرًا
- (4:57) [next to 4:56] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (4:58) [next to 4:56] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
- (6:120) [next to 6:122] وَذَرُوا۟ ظَٰهِرَ ٱلْإِثْمِ وَبَاطِنَهُۥٓ ۚ إِنَّ ٱلَّذِينَ يَكْسِبُونَ ٱلْإِثْمَ سَيُجْزَوْنَ بِمَا كَانُوا۟ يَقْتَرِفُونَ
- (6:121) [next to 6:122] وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ وَإِنَّهُۥ لَفِسْقٌۭ ۗ وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ ۖ وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ
- (6:123) [next to 6:122] وَكَذَٰلِكَ جَعَلْنَا فِى كُلِّ قَرْيَةٍ أَكَٰبِرَ مُجْرِمِيهَا لِيَمْكُرُوا۟ فِيهَا ۖ وَمَا يَمْكُرُونَ إِلَّا بِأَنفُسِهِمْ وَمَا يَشْعُرُونَ
- (6:124) [next to 6:122] وَإِذَا جَآءَتْهُمْ ءَايَةٌۭ قَالُوا۟ لَن نُّؤْمِنَ حَتَّىٰ نُؤْتَىٰ مِثْلَ مَآ أُوتِىَ رُسُلُ ٱللَّهِ ۘ ٱللَّهُ أَعْلَمُ حَيْثُ يَجْعَلُ رِسَالَتَهُۥ ۗ سَيُصِيبُ ٱلَّذِينَ أَجْرَمُوا۟ صَغَارٌ عِندَ ٱللَّهِ وَعَذَابٌۭ شَدِيدٌۢ بِمَا كَانُوا۟ يَمْكُرُونَ
- (7:22) [next to 7:24] فَدَلَّىٰهُمَا بِغُرُورٍۢ ۚ فَلَمَّا ذَاقَا ٱلشَّجَرَةَ بَدَتْ لَهُمَا سَوْءَٰتُهُمَا وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِن وَرَقِ ٱلْجَنَّةِ ۖ وَنَادَىٰهُمَا رَبُّهُمَآ أَلَمْ أَنْهَكُمَا عَن تِلْكُمَا ٱلشَّجَرَةِ وَأَقُل لَّكُمَآ إِنَّ ٱلشَّيْطَٰنَ لَكُمَا عَدُوٌّۭ مُّبِينٌۭ
- (7:23) [next to 7:24] قَالَا رَبَّنَا ظَلَمْنَآ أَنفُسَنَا وَإِن لَّمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ ٱلْخَٰسِرِينَ
- (7:26) [next to 7:24] يَٰبَنِىٓ ءَادَمَ قَدْ أَنزَلْنَا عَلَيْكُمْ لِبَاسًۭا يُوَٰرِى سَوْءَٰتِكُمْ وَرِيشًۭا ۖ وَلِبَاسُ ٱلتَّقْوَىٰ ذَٰلِكَ خَيْرٌۭ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ لَعَلَّهُمْ يَذَّكَّرُونَ
- (7:27) [next to 7:25] يَٰبَنِىٓ ءَادَمَ لَا يَفْتِنَنَّكُمُ ٱلشَّيْطَٰنُ كَمَآ أَخْرَجَ أَبَوَيْكُم مِّنَ ٱلْجَنَّةِ يَنزِعُ عَنْهُمَا لِبَاسَهُمَا لِيُرِيَهُمَا سَوْءَٰتِهِمَآ ۗ إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ ۗ إِنَّا جَعَلْنَا ٱلشَّيَٰطِينَ أَوْلِيَآءَ لِلَّذِينَ لَا يُؤْمِنُونَ
- (8:22) [next to 8:24] ۞ إِنَّ شَرَّ ٱلدَّوَآبِّ عِندَ ٱللَّهِ ٱلصُّمُّ ٱلْبُكْمُ ٱلَّذِينَ لَا يَعْقِلُونَ
- (8:23) [next to 8:24] وَلَوْ عَلِمَ ٱللَّهُ فِيهِمْ خَيْرًۭا لَّأَسْمَعَهُمْ ۖ وَلَوْ أَسْمَعَهُمْ لَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ
- (8:25) [next to 8:24] وَٱتَّقُوا۟ فِتْنَةًۭ لَّا تُصِيبَنَّ ٱلَّذِينَ ظَلَمُوا۟ مِنكُمْ خَآصَّةًۭ ۖ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (8:26) [next to 8:24] وَٱذْكُرُوٓا۟ إِذْ أَنتُمْ قَلِيلٌۭ مُّسْتَضْعَفُونَ فِى ٱلْأَرْضِ تَخَافُونَ أَن يَتَخَطَّفَكُمُ ٱلنَّاسُ فَـَٔاوَىٰكُمْ وَأَيَّدَكُم بِنَصْرِهِۦ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ لَعَلَّكُمْ تَشْكُرُونَ
- (14:15) [next to 14:17] وَٱسْتَفْتَحُوا۟ وَخَابَ كُلُّ جَبَّارٍ عَنِيدٍۢ
- (14:16) [next to 14:17] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (14:18) [next to 14:17] مَّثَلُ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ ۖ لَّا يَقْدِرُونَ مِمَّا كَسَبُوا۟ عَلَىٰ شَىْءٍۢ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
- (14:19) [next to 14:17] أَلَمْ تَرَ أَنَّ ٱللَّهَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (19:5) [next to 19:7] وَإِنِّى خِفْتُ ٱلْمَوَٰلِىَ مِن وَرَآءِى وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا
- (19:6) [next to 19:7] يَرِثُنِى وَيَرِثُ مِنْ ءَالِ يَعْقُوبَ ۖ وَٱجْعَلْهُ رَبِّ رَضِيًّۭا
- (19:8) [next to 19:7] قَالَ رَبِّ أَنَّىٰ يَكُونُ لِى غُلَٰمٌۭ وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا وَقَدْ بَلَغْتُ مِنَ ٱلْكِبَرِ عِتِيًّۭا
- (19:9) [next to 19:7] قَالَ كَذَٰلِكَ قَالَ رَبُّكَ هُوَ عَلَىَّ هَيِّنٌۭ وَقَدْ خَلَقْتُكَ مِن قَبْلُ وَلَمْ تَكُ شَيْـًۭٔا
- (19:10) [next to 19:12] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۚ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَ لَيَالٍۢ سَوِيًّۭا
- (19:11) [next to 19:12] فَخَرَجَ عَلَىٰ قَوْمِهِۦ مِنَ ٱلْمِحْرَابِ فَأَوْحَىٰٓ إِلَيْهِمْ أَن سَبِّحُوا۟ بُكْرَةًۭ وَعَشِيًّۭا
- (19:14) [next to 19:12] وَبَرًّۢا بِوَٰلِدَيْهِ وَلَمْ يَكُن جَبَّارًا عَصِيًّۭا
- (19:16) [next to 19:15] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مَرْيَمَ إِذِ ٱنتَبَذَتْ مِنْ أَهْلِهَا مَكَانًۭا شَرْقِيًّۭا
- (19:17) [next to 19:15] فَٱتَّخَذَتْ مِن دُونِهِمْ حِجَابًۭا فَأَرْسَلْنَآ إِلَيْهَا رُوحَنَا فَتَمَثَّلَ لَهَا بَشَرًۭا سَوِيًّۭا
- (19:31) [next to 19:33] وَجَعَلَنِى مُبَارَكًا أَيْنَ مَا كُنتُ وَأَوْصَٰنِى بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ مَا دُمْتُ حَيًّۭا
- (19:32) [next to 19:33] وَبَرًّۢا بِوَٰلِدَتِى وَلَمْ يَجْعَلْنِى جَبَّارًۭا شَقِيًّۭا
- (19:34) [next to 19:33] ذَٰلِكَ عِيسَى ٱبْنُ مَرْيَمَ ۚ قَوْلَ ٱلْحَقِّ ٱلَّذِى فِيهِ يَمْتَرُونَ
- (19:35) [next to 19:33] مَا كَانَ لِلَّهِ أَن يَتَّخِذَ مِن وَلَدٍۢ ۖ سُبْحَٰنَهُۥٓ ۚ إِذَا قَضَىٰٓ أَمْرًۭا فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ
- (20:70) [next to 20:72] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (20:71) [next to 20:72] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (20:75) [next to 20:73] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (20:77) [next to 20:76] وَلَقَدْ أَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ أَنْ أَسْرِ بِعِبَادِى فَٱضْرِبْ لَهُمْ طَرِيقًۭا فِى ٱلْبَحْرِ يَبَسًۭا لَّا تَخَٰفُ دَرَكًۭا وَلَا تَخْشَىٰ
- (20:78) [next to 20:76] فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ
- (22:3) [next to 22:5] وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّبِعُ كُلَّ شَيْطَٰنٍۢ مَّرِيدٍۢ
- (22:4) [next to 22:5] كُتِبَ عَلَيْهِ أَنَّهُۥ مَن تَوَلَّاهُ فَأَنَّهُۥ يُضِلُّهُۥ وَيَهْدِيهِ إِلَىٰ عَذَابِ ٱلسَّعِيرِ
- (25:45) [next to 25:47] أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ وَلَوْ شَآءَ لَجَعَلَهُۥ سَاكِنًۭا ثُمَّ جَعَلْنَا ٱلشَّمْسَ عَلَيْهِ دَلِيلًۭا
- (25:46) [next to 25:47] ثُمَّ قَبَضْنَٰهُ إِلَيْنَا قَبْضًۭا يَسِيرًۭا
- (25:48) [next to 25:47] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
- (29:62) [next to 29:64] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥٓ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (29:65) [next to 29:64] فَإِذَا رَكِبُوا۟ فِى ٱلْفُلْكِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ إِذَا هُمْ يُشْرِكُونَ
- (29:66) [next to 29:64] لِيَكْفُرُوا۟ بِمَآ ءَاتَيْنَٰهُمْ وَلِيَتَمَتَّعُوا۟ ۖ فَسَوْفَ يَعْلَمُونَ
- (35:20) [next to 35:22] وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ
- (35:21) [next to 35:22] وَلَا ٱلظِّلُّ وَلَا ٱلْحَرُورُ
- (35:23) [next to 35:22] إِنْ أَنتَ إِلَّا نَذِيرٌ
- (35:24) [next to 35:22] إِنَّآ أَرْسَلْنَٰكَ بِٱلْحَقِّ بَشِيرًۭا وَنَذِيرًۭا ۚ وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌۭ
- (35:34) [next to 35:36] وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَذْهَبَ عَنَّا ٱلْحَزَنَ ۖ إِنَّ رَبَّنَا لَغَفُورٌۭ شَكُورٌ
- (35:37) [next to 35:36] وَهُمْ يَصْطَرِخُونَ فِيهَا رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ ۖ فَذُوقُوا۟ فَمَا لِلظَّٰلِمِينَ مِن نَّصِيرٍ
- (35:38) [next to 35:36] إِنَّ ٱللَّهَ عَٰلِمُ غَيْبِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (36:67) [next to 36:69] وَلَوْ نَشَآءُ لَمَسَخْنَٰهُمْ عَلَىٰ مَكَانَتِهِمْ فَمَا ٱسْتَطَٰعُوا۟ مُضِيًّۭا وَلَا يَرْجِعُونَ
- (36:68) [next to 36:69] وَمَن نُّعَمِّرْهُ نُنَكِّسْهُ فِى ٱلْخَلْقِ ۖ أَفَلَا يَعْقِلُونَ
- (36:71) [next to 36:69] أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ
- (36:72) [next to 36:70] وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ
- (39:40) [next to 39:42] مَن يَأْتِيهِ عَذَابٌۭ يُخْزِيهِ وَيَحِلُّ عَلَيْهِ عَذَابٌۭ مُّقِيمٌ
- (39:41) [next to 39:42] إِنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ لِلنَّاسِ بِٱلْحَقِّ ۖ فَمَنِ ٱهْتَدَىٰ فَلِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍ
- (39:43) [next to 39:42] أَمِ ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ شُفَعَآءَ ۚ قُلْ أَوَلَوْ كَانُوا۟ لَا يَمْلِكُونَ شَيْـًۭٔا وَلَا يَعْقِلُونَ
- (39:44) [next to 39:42] قُل لِّلَّهِ ٱلشَّفَٰعَةُ جَمِيعًۭا ۖ لَّهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ ثُمَّ إِلَيْهِ تُرْجَعُونَ
- (41:37) [next to 41:39] وَمِنْ ءَايَٰتِهِ ٱلَّيْلُ وَٱلنَّهَارُ وَٱلشَّمْسُ وَٱلْقَمَرُ ۚ لَا تَسْجُدُوا۟ لِلشَّمْسِ وَلَا لِلْقَمَرِ وَٱسْجُدُوا۟ لِلَّهِ ٱلَّذِى خَلَقَهُنَّ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (41:38) [next to 41:39] فَإِنِ ٱسْتَكْبَرُوا۟ فَٱلَّذِينَ عِندَ رَبِّكَ يُسَبِّحُونَ لَهُۥ بِٱلَّيْلِ وَٱلنَّهَارِ وَهُمْ لَا يَسْـَٔمُونَ ۩
- (41:40) [next to 41:39] إِنَّ ٱلَّذِينَ يُلْحِدُونَ فِىٓ ءَايَٰتِنَا لَا يَخْفَوْنَ عَلَيْنَآ ۗ أَفَمَن يُلْقَىٰ فِى ٱلنَّارِ خَيْرٌ أَم مَّن يَأْتِىٓ ءَامِنًۭا يَوْمَ ٱلْقِيَٰمَةِ ۚ ٱعْمَلُوا۟ مَا شِئْتُمْ ۖ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌ
- (41:41) [next to 41:39] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (43:73) [next to 43:75] لَكُمْ فِيهَا فَٰكِهَةٌۭ كَثِيرَةٌۭ مِّنْهَا تَأْكُلُونَ
- (43:76) [next to 43:75] وَمَا ظَلَمْنَٰهُمْ وَلَٰكِن كَانُوا۟ هُمُ ٱلظَّٰلِمِينَ
- (43:78) [next to 43:77] لَقَدْ جِئْنَٰكُم بِٱلْحَقِّ وَلَٰكِنَّ أَكْثَرَكُمْ لِلْحَقِّ كَٰرِهُونَ
- (43:79) [next to 43:77] أَمْ أَبْرَمُوٓا۟ أَمْرًۭا فَإِنَّا مُبْرِمُونَ
- (44:54) [next to 44:56] كَذَٰلِكَ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (44:55) [next to 44:56] يَدْعُونَ فِيهَا بِكُلِّ فَٰكِهَةٍ ءَامِنِينَ
- (44:57) [next to 44:56] فَضْلًۭا مِّن رَّبِّكَ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (44:58) [next to 44:56] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (89:21) [next to 89:23] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- (89:22) [next to 89:23] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- (89:25) [next to 89:23] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- (89:26) [next to 89:24] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ

