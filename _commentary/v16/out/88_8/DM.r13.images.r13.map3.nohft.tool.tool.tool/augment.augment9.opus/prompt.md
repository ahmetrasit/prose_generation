Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:8; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_8/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_8.reading.tr.md (prose paragraphs numbered) =====
## Aynı kalıp, tek kelimelik fark

[¶1] Sekizinci ayet, ikinci ayetin kalıbını harfi harfine tekrarlar. İkinci ayet {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2} der. Sekizinci ayet de {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve rahat, source:88:8} der. İki cümlede ilk iki kelime aynıdır, değişen yalnızca sonundaki sıfattır. "O gün", surenin ilk ayetinde haberi sorulan örtücü olayın günüdür. Bu yüzden ayet yeni bir sahne açmaz. İkinci ayette başlayan aynı günün öbür yüzünü gösterir. "Yüzler" belirsiz söylenir, yani "birtakım yüzler". O gün yüzler ikiye ayrılır ve her biri kendi sıfatıyla anılır.

[¶2] Kur'an bu kalıbı başka iki surede de kurar. Kıyamet suresinde Allah önce {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} der, ardından {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} der. Abese suresinde, kişinin kardeşinden, anasından ve babasından kaçtığı günün sonunda yine önce aydınlık yüzler gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ, tr:vucûhun yevmeizin musfira, gloss:o gün birtakım yüzler ışıl ışıl, source:80:38}. Tozlu yüzler ise ikinci sıradadır: {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:birtakım yüzlerin üstünde de toz vardır, source:80:40}. Gâşiye suresi bu sırayı tersine çevirir. Okuyucu önce ateşe giren, kaynar pınardan içirilen ve doymayan yüzlerden geçer, yumuşak yüze ancak ondan sonra varır. Bir fark daha vardır. O iki surede ikinci grup "ve" ile bağlanır, burada ise sekizinci ayet bağlaçsız başlar. Yumuşak yüz, öncekine eklenen bir ek gibi gelmez. İkinci ayet nasıl başladıysa o da öyle, baştan ve kendi başına başlar.

[¶3] Bu yüzlerin yalnızca yüz olmadığını bir sonraki ayet gösterir: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdıye, gloss:çabasından hoşnut, source:88:9}. Buradaki "onun çabası" zamiri yüzlere döner. Ama yürüyen, koşan ve çabalayan şey bir yüz değil, bir insandır. Araplar da yüzü kişinin kendisi yerine koyarlardı: {ar:ربما عبر عن الذات بالوجه, tr:rubbemâ ubbira ani'z-zâti bi'l-vech, gloss:kimi zaman kişinin kendisi yüzle anlatılır, source:"و ج ه,B004"}. Kur'an da {ar:كُلُّ شَىْءٍ هَالِكٌ إِلَّا وَجْهَهُۥ, tr:küllü şey'in hâlikun illâ vecheh, gloss:O'nun yüzünden başka her şey yok olacaktır, source:28:88} derken yüzü varlığın kendisi anlamında kullanır. Yine de seçilen kelime "yüz"dür, çünkü yüz bir şeyin karşıya bakan yanıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz, her şeyin karşıya dönük yanıdır, source:"و ج ه,B001"}. O gün insanın içinde ne varsa yüzünde okunur. Mutaffifîn suresi iyilerin sedirler üzerinde bakındığı sahneyi anlatırken okura doğrudan seslenir: {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24}. Oradaki "nimet" kelimesi, nâime ile aynı köktendir. Kur'an o yüzde bakanın tanıyabileceği bir yumuşaklık ve tazelik görür.

## Yumuşaklık: kelimenin kendisi

[¶4] Nâime, ilk ve en yalın fiilin sıfatıdır. Bir şey yumuşadığında Araplar şöyle derdi: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:o şey yumuşadı, esnekleşti, source:"ن ع م,B002"}. Fiilden sıfata giden yol da şu sözle anlatılır: {ar:نعم ينعم نعمة فهو نعم ناعم, tr:neime yen'amu na'meten fe-huve neimun nâim, gloss:rahat ve yumuşak oldu; o artık rahat yaşayan biridir, source:"ن ع م,B001"}. Kökün temeli bir arada üç şey olarak tanımlanır: {ar:أصل واحد يدل على ترفه وطيب عيش وصلاح, tr:aslun vâhidun yedullü alâ terafuhin ve tîbi ayşin ve salâh, gloss:rahatlığı, hoş yaşamı ve esenliği gösteren tek bir kök, source:"ن ع م,B001"}. Yani ayet yüzün bir şey aldığını söylemez, yüzün kendisinin yumuşak ve rahat olduğunu söyler.

[¶5] Türkçede bu kökten gelen "nimet" kelimesi daralmıştır. Bugün nimet denince verilen bir lütuf, çoğu zaman da sofradaki ekmek akla gelir. Arapçada ise kök dokunarak bilinen bir yumuşaklıktan başlar ve oradan rahat bir hayata uzanır. Nâime'yi duyan biri bu yüzde önce bir dokuyu, gerilmemiş ve kurumamış bir teni duyar. Mutaffifîn suresinin yüzlerde tanınır dediği tazelik de bu yumuşaklıkla aynı sahnededir {source:83:24}.

[¶6] Kökün başka kolları bu yumuşaklığı somut nesnelerde gösterir. Bunlar ayetin anlamının yerine geçmez, onun yanında duyulan yan resimlerdir. Devekuşu bu kökten adını alır ve gerekçesi açıkça söylenir: {ar:النعامة معروفة لنعمة ريشها, tr:en-neâmetü ma'rûfetun li-nu'meti rîşihâ, gloss:devekuşu tüylerinin yumuşaklığıyla bilinir, source:"ن ع م,B006"}. Yani bu kuşun adı, tüyüne dokunan elin duyduğu şeyden gelir. Rüzgârlar arasında güney rüzgârı da bu kökten bir ad taşır: {ar:النعامي الريح اللينة, tr:en-neâmâ er-rîhu'l-leyyine, gloss:neâmâ yumuşak esen rüzgârdır, source:"ن ع م,B009"}. Neden böyle adlandırıldığı da söylenir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûbi li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:güney rüzgârıdır, çünkü rüzgârların en ıslağı ve en nemlisidir, source:"ن ع م,B009"}. Bu rüzgâr sert esmez, nem taşıyarak gelir. Bu kökte yumuşaklık ile nem birbirine yakındır.

[¶7] Bu yakınlık surenin içinde bir karşılık bulur. İkinci ayetteki yüzün sıfatı, yağmur görmeyip kurumuş ve yere çökmüş toprak için de kullanılırdı. Kurak toprak ile suyla yumuşamış toprağın karşılaşması surenin bütününe ait bir sahnedir ve ikinci ayetin kelimesiyle kurulur. Sekizinci ayet o sahnenin nemli yanını taşır. Bir de yaşamın tazeliği vardır: {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın rahatlığı, onun güzelliği ve yeşil tazeliğidir, source:"ن ع م,B002"}.

[¶8] Yemek de bu kelimeyle anılırdı: {ar:طعام ناعم وجارية ناعمة, tr:taâmun nâimun ve câriyetun nâime, gloss:yumuşak, ince yemek ve teni yumuşak genç kız, source:"ن ع م,B002"}. Bu kullanım surenin akışında yerine oturur. Sekizinci ayetten hemen önce, ateşteki yüzlerin yiyeceği anlatılır: {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besler ne de açlığı giderir, source:88:7}. Bu ayet "açlık" kelimesiyle biter. Ardından gelen ilk sıfat ise Arapların yumuşak ve ince yemeğe verdiği addır. Doymayan bedenden sonra, rahatlığı yüzünden okunan bir insan gelir.

## Duada istenen, yüzde görünen

[¶9] Aynı kök her namazda okunan Fâtiha'da da vardır. Yedinci ayette istenen yol {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:sırâta'llezîne en'amte aleyhim, gloss:kendilerine nimet verdiğin kimselerin yolu, source:1:7} diye tarif edilir. Oradaki fiil ettirgendir, yani başkasına iyilik ulaştırmayı anlatır: {ar:الإنعام إيصال الإحسان إلى الغير, tr:el-in'âmu îsâlu'l-ihsâni ile'l-ğayr, gloss:in'âm, iyiliği bir başkasına ulaştırmaktır, source:"ن ع م,B001"}. Ulaştırılan şeyin kendisine de ad verilir: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanîatü ve'l-minnetü ve mâ en'ame bihî aleyk, gloss:nimet, sana uzanan el, yapılan iyilik ve sana verilen şeydir, source:"ن ع م,B001"}. Sekizinci ayetteki kelime ise bu ettirgen fiilden gelmez. Nimet verilmiş biri anlamındaki edilgen sıfat da değildir. Yalın fiilden gelir ve iyiliğin bir insana ulaşıp onda yerleştikten sonra bıraktığı hali anlatır. Namazda Allah'a "en'amte" diye seslenen kişi, iyilik ulaştırılmış olanların yolunu ister. Sekizinci ayet o iyiliğin varılan günde bir yüzde nasıl göründüğünü gösterir. İyiliği veren Allah'tır, yumuşayan ise yüzdür.

[¶10] Bu yumuşaklık bakan göz için de bir sevinçtir. Araplar birine dua ederken şöyle derlerdi: {ar:نعم الله بك عينا, tr:neima'llâhu bike aynâ, gloss:Allah seninle bir gözü sevindirsin, source:"ن ع م,B013"}. Bu sözün açıklaması da yapılmıştır: {ar:نعمة العين قرتها, tr:nu'metü'l-ayni kurratuhâ, gloss:gözün nimeti onun serinleyip sevinmesidir, source:"ن ع م,B013"}. Kur'an aynı "göz serinliği" ifadesini, geceleri yataklarından kalkıp Rablerine korku ve umutla yalvaran kimseler için kullanır. Allah onlar hakkında şöyle der: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ, tr:fe-lâ ta'lemu nefsun mâ uhfiye lehum min kurrati a'yunin cezâen bimâ kânû ya'melûn, gloss:yaptıklarına karşılık olarak onlar için hangi göz sevinçlerinin saklandığını hiç kimse bilmez, source:32:17}. O ayet karşılığı "yaptıkları"na bağlar. Surenin iki yüzünü ayıran şey de buradadır.

## Emek ve ücreti

[¶11] İki yüz de çalışmıştır. Üçüncü ayetteki yüz {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3} diye anılır. Dokuzuncu ayetteki yüz de çabasından hoşnuttur. Ayrım çalışılıp çalışılmadığında değildir, çalışmanın neye vardığındadır.

[¶12] Nâime'nin kökü övgü sözünü de verir: {ar:نعم كلمة تستعمل في المدح بإزاء بئس, tr:ni'me kelimetun tusta'melu fi'l-medhi bi-izâi bi's, gloss:ni'me, kötülemeyi bildiren bi'se'nin karşısında övgü için kullanılan kelimedir, source:"ن ع م,B003"}. Kur'an bu övgüyü üç kez aynı sözle çalışanlara yöneltir. Âl-i İmrân suresinde, bollukta da darlıkta da harcayan, öfkesini yutan, insanları affeden, kendine zulmettiğinde Allah'ı anıp bağışlanma dileyen ve yaptığında direnmeyenler anlatılır. Onların karşılığı bağışlanma ve altından ırmaklar akan bahçelerdir. Ayet şöyle biter: {ar:وَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ, tr:ve ni'me ecru'l-âmilîn, gloss:çalışanların ücreti ne güzeldir, source:3:136}. Ankebût suresinde de iman edip iyi işler yapanlar, altından ırmaklar akan bahçe odalarına yerleştirilir. Bunlar sabredip Rablerine dayananlardır ve aynı söz tekrarlanır: {ar:نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ, tr:ni'me ecru'l-âmilîn, gloss:çalışanların ücreti ne güzeldir, source:29:58}. Zümer suresinde ise bu sözü bahçeye bölük bölük sürülen takva sahipleri kendileri söyler. Kapılar açılıp bekçiler onları selamladığında, sözünü yerine getiren Allah'a hamdederler ve bahçede istedikleri yere yerleştiklerini söyleyerek şöyle derler: {ar:فَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ, tr:fe-ni'me ecru'l-âmilîn, gloss:çalışanların ücreti ne güzelmiş, source:39:74}. Bu üç ayette "çalışanlar" kelimesi üçüncü ayetteki âmile ile, "ne güzel" kelimesi de nâime ile aynı köktendir. Surenin iki yüzü bu sözde yan yana gelir. Âmile olmak iki yüz için de ortaktır. Sekizinci ayetteki yüzün emeği ise "ne güzel" diye övülen bir ücrete varmıştır.

[¶13] Bu ücretin yönü de yüzle anlatılır. Yahudiler ve Hristiyanlar bahçeye yalnızca kendilerinin gireceğini söylediklerinde Allah şu cevabı verir: {ar:بَلَىٰ مَنْ أَسْلَمَ وَجْهَهُۥ لِلَّهِ وَهُوَ مُحْسِنٌۭ فَلَهُۥٓ أَجْرُهُۥ عِندَ رَبِّهِۦ, tr:belâ men esleme vechehû li'llâhi ve huve muhsinun fe-lehû ecruhû inde rabbih, gloss:hayır, kim iyilik yaparak yüzünü Allah'a teslim ederse onun ücreti Rabbinin katındadır, source:2:112}. Araplar da bir yöne bütünüyle dönmeyi yüz kelimesiyle söylerdi: {ar:وجهت وجهي لله سبحانه, tr:veccehtü vechî li'llâhi subhânehû, gloss:yüzümü Allah'a çevirdim, source:"و ج ه,B005"}. Dünyada Allah'a çevrilen yüz, o gün yumuşamış olarak görünür. Surenin yirmi üçüncü ayeti ise bunun tersini, yüz çeviren kimseyi anar {source:88:23}.

[¶14] Bu emeğin karşılığı başka bir yerde, surenin dokuzuncu ve onuncu ayetlerindeki kelimelerle aynı sırayla anlatılır. Hâkka suresinde kitabı sağından verilen kişi sevinçle {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentu ennî mulâkın hisâbiyeh, gloss:hesabımla karşılaşacağımı zaten biliyordum, source:69:20} der. Ardından onun hali şöyle anlatılır: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdıye, gloss:o artık hoşnut edici bir yaşayış içindedir, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:69:22}. Nâime'nin kökü de en çok bu yaşayış kelimesinin yanında kullanılır: na'metü'l-ayş, yani yaşamın rahatlığı. Gâşiye'de yüzün hoşnutluğu "çabası"na bağlanır. Hâkka'da ise hoşnutluk yaşayışın sıfatıdır ve o kişi hesabıyla karşılaşacağını bilerek yaşamıştır.

[¶15] Kökün iki dar kalıbı bu bağı yan resim olarak duyurur. Biri yürümekle ilgilidir. Birini yaya olarak arayıp ona gitmeye bu kökten bir fiille ad verilirdi ve bunun gerekçesi şöyle açıklanırdı: {ar:تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه, tr:tenaamtu Zeyden talebtuhû ke-ennehû erâde a'meltu ileyhi neâmetehû ve hiye bâtinu kademih, gloss:Zeyd'i aradım; sanki ona doğru ayağımın tabanını işlettim demek ister, tabana neâme denir, source:"ن ع م,B012"}. Hafif yürüyüş de bu kökle anılırdı: {ar:تنعم فلان إذا مشى مشيا خفيفا, tr:tenaame fulânun izâ meşâ meşyen hafîfâ, gloss:biri hafif adımlarla yürüdüğünde tenaame denir, source:"ن ع م,B012"}. Dokuzuncu ayetteki çaba kelimesi de aslında bir yürüyüş adıdır: {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y, şiddetli olmayan bir koşudur, source:"س ع ي,B001"}. Yumuşak yüzü anlatan kök, birine doğru yürüyen ayağın tabanına da ad verir. Hemen ardından gelen ayet de o yüzün yürüyüşünden hoşnut olduğunu söyler.

[¶16] Öteki kalıp bir yere varıp orada kalmakla ilgilidir: {ar:أتيت أرضا فنعمتني أي وافقتني وأقمت بها, tr:eteytu ardan fe-neametnî ey vâfekatnî ve ekamtu bihâ, gloss:bir yere vardım, bana uydu ve orada kaldım, source:"ن ع م,B011"}. Bu kullanımda toprağın kendisi gelene uyar. Dokuzuncu ayette yüz hoşnuttur, onuncu ayette ise yüksek bir bahçededir. Hoşnut olan bir yüz ile o yüze uyan bir yer, aynı kökün iki yönünden duyulur.

## Dünyanın rahatlığı, o günün rahatlığı

[¶17] Bu kök yalnızca o günün rahatlığını anlatmaz, dünyadaki rahatlığı da anlatır. Her rahatlık da iyi sonlanmaz. Duhân suresinde Allah, Firavun'un kavmini sınadığını ve onlara değerli bir elçi geldiğini anlatır. Musa'ya kullarını geceleyin yola çıkarmasını, denizi açık bırakmasını söyler, çünkü onlar boğulacak bir ordudur. Ardından geride kalanları sayar: {ar:كَمْ تَرَكُوا۟ مِن جَنَّٰتٍۢ وَعُيُونٍۢ, tr:kem terakû min cennâtin ve uyûn, gloss:ne çok bahçe ve pınar bıraktılar, source:44:25}; {ar:وَنَعْمَةٍۢ كَانُوا۟ فِيهَا فَٰكِهِينَ, tr:ve na'metin kânû fîhâ fâkihîn, gloss:içinde keyif sürdükleri nice rahatlık, source:44:27}. Orada bahçeler ve pınarlar vardır. Gâşiye'nin yumuşak yüzleri de onuncu ayette bir bahçede, on ikinci ayette akan bir pınarın yanındadır. Kelimeler aynıdır, sonları ise birbirinin tersidir. Biri geride bırakılan bir rahatlıktır, öteki varılan bir rahatlıktır. Müzzemmil suresinde Allah, Peygamber'e onların söylediklerine sabretmesini ve onlardan güzellikle uzaklaşmasını söyler. Sonra şöyle der: {ar:وَذَرْنِى وَٱلْمُكَذِّبِينَ أُو۟لِى ٱلنَّعْمَةِ وَمَهِّلْهُمْ قَلِيلًا, tr:ve zernî ve'l-mukezzibîne uli'n-na'meti ve mehhilhum kalîlâ, gloss:o yalanlayan rahatlık sahiplerini bana bırak, onlara biraz mühlet ver, source:73:11}. Dünyadaki rahatlık, yalanlayanların da sahip olduğu bir şeydir.

[¶18] Hemen arkadan gelen Fecr suresi bu rahatlığın ne olduğunu açıkça söyler: {ar:فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe-emme'l-insânu izâ me'btelâhu rabbuhû fe-ekramehû ve na''amehû fe-yekûlu rabbî ekramen, gloss:insan, Rabbi onu sınayıp ona ikram ettiğinde ve onu rahatlık içinde yaşattığında "Rabbim bana ikram etti" der, source:89:15}. Rızkı daraltıldığında da "Rabbim beni aşağıladı" der. Kur'an bu iki sözü de "hayır" diye reddeder. Dünyada rahat yaşatılmak bir sınavdır, bir hüküm değildir. Araplar da çocuklarını bolluk içinde büyüten babayı şöyle anarlardı: {ar:نعم فلان أولاده ترفهم, tr:neame fulânun evlâdehû terrafehum, gloss:falanca çocuklarını rahatlık içinde yaşattı, source:"ن ع م,B002"}. O gün ise yüz, kimsenin onu rahat yaşatmasıyla değil, kendi çabasından hoşnut olduğu için yumuşaktır. Kökün tanımı rahatlığı, hoş yaşamı ve esenliği bir arada sayıyordu. Dünyada bu üçü birbirinden ayrılabilir. Sekizinci ayette ise üçü bir arada görünür.

[¶19] Kökün en somut dünya malı devedir: {ar:النعم الإبل لما فيه من الخير والنعمة, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meh, gloss:neam devedir, içinde taşıdığı hayır ve nimetten dolayı böyle denir, source:"ن ع م,B005"}. Bir başka açıklama bu adın neyi kapsadığını söyler: {ar:النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل, tr:en-neamu vâhidu'l-en'âm ve hiye'l-mâlu'r-râiye ve ekseru mâ yekau hâze'l-ismu ale'l-ibil, gloss:neam, en'âmın tekilidir; otlayan maldır ve bu ad çoğunlukla deveye verilir, source:"ن ع م,B005"}. Bu adı taşıyan sürü, otlakta yayılıp kendi kendini besleyen, süt, yün, yük taşıma ve yemek veren canlı bir servetti. Kur'an bunu bir yaratma işi olarak sayar: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları da O yarattı; onlarda sizin için ısınma ve faydalar vardır, onlardan yersiniz, source:16:5}. Ama aynı sürüyü insana süslü gösterilen arzular arasında da sayar ve şöyle der: {ar:ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ, tr:zâlike metâu'l-hayâti'd-dünyâ, va'llâhu indehû husnu'l-meâb, gloss:bunlar dünya hayatının geçimliğidir; varılacak yerin güzeli ise Allah katındadır, source:3:14}. Sürü insanın sahip olduğu bir rahatlıktır. Nâime ise insanın kendisinin dönüştüğü bir haldir. Surenin on yedinci ayeti deveye bakmaya ve nasıl yaratıldığını görmeye çağırır. Bu bakışın surede kurduğu sahne o ayetin kelimesine aittir. Sekizinci ayetin kelimesi ise o sahneye, devenin adını taşıyan kökün rahatlığını ekler.

===== _commentary/v16/out/88_8/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: tanwin in يَوْمَئِذٍ stands for an omitted clause (the day of the Ghashiya)
- memory: indefinite وُجُوهٌ as subject justified by the division into groups
- memory: نَاعِمَة is the active participle of the base verb نَعِمَ, not causative/passive (مُنْعَم)
- memory: نَعْمَة (ease, fatha) vs نِعْمَة (favour, kasra) distinction
- memory: Turkish "nimet" narrowed to granted blessing / bread
- not written: و ج ه B002 direction senses (wind driving pebbles, treading a path) - B005 already carries turning the face
- not written: و ج ه B006 notables (وجوه القوم) - rank contrast with "faces" on that day not grounded by the text
- not written: و ج ه B007 face of the day = morning - no support linking it to يومئذ
- not written: و ج ه B003, B008-B015 (confrontation, right course, aging, breech birth, rhyme letter, cucumber, striking, sending back, two-faced) - no work in a theme
- not written: ن ع م B004 "yes" - no link to the ayah
- not written: ن ع م B007 well crossbeam / mountain shade - named by ostrich shape, not softness
- not written: ن ع م B008 scattering (شالت نعامتهم) - no work here
- not written: ن ع م B010 doing thoroughly / grinding fine - softness-through-grinding link too speculative

===== passages not cited (199) =====
## strong (this ayah's own list) (14)

- (3:107) [listed for 88:8] وَأَمَّا ٱلَّذِينَ ٱبْيَضَّتْ وُجُوهُهُمْ فَفِى رَحْمَةِ ٱللَّهِ هُمْ فِيهَا خَٰلِدُونَ
- (10:26) [listed for 88:8] ۞ لِّلَّذِينَ أَحْسَنُوا۟ ٱلْحُسْنَىٰ وَزِيَادَةٌۭ ۖ وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (56:12) [listed for 88:8] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (75:22) [listed for 88:8] [cited in ¶2] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
- (75:23) [listed for 88:8] إِلَىٰ رَبِّهَا نَاظِرَةٌۭ
- (76:11) [listed for 88:8] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (80:39) [listed for 88:8] ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ
- (83:24) [listed for 88:8] [cited in ¶3, ¶5] تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ
- (83:25) [listed for 88:8] يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ
- (89:27) [listed for 88:8] يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- (89:28) [listed for 88:8] ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- (89:30) [listed for 88:8] وَٱدْخُلِى جَنَّتِى
- (93:5) [listed for 88:8] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (98:8) [listed for 88:8] جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

## medium (this ayah's own list) (70)

- (1:7) [listed for 88:8] [cited in ¶9] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- (3:106) [listed for 88:8] يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌۭ ۚ فَأَمَّا ٱلَّذِينَ ٱسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُم بَعْدَ إِيمَٰنِكُمْ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (4:69) [listed for 88:8] وَمَن يُطِعِ ٱللَّهَ وَٱلرَّسُولَ فَأُو۟لَٰٓئِكَ مَعَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ وَٱلصِّدِّيقِينَ وَٱلشُّهَدَآءِ وَٱلصَّٰلِحِينَ ۚ وَحَسُنَ أُو۟لَٰٓئِكَ رَفِيقًۭا
- (6:127) [listed for 88:8] ۞ لَهُمْ دَارُ ٱلسَّلَٰمِ عِندَ رَبِّهِمْ ۖ وَهُوَ وَلِيُّهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- (7:42) [listed for 88:8] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (7:179) [listed for 88:8] وَلَقَدْ ذَرَأْنَا لِجَهَنَّمَ كَثِيرًۭا مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا وَلَهُمْ ءَاذَانٌۭ لَّا يَسْمَعُونَ بِهَآ ۚ أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْغَٰفِلُونَ
- (9:21) [listed for 88:8] يُبَشِّرُهُمْ رَبُّهُم بِرَحْمَةٍۢ مِّنْهُ وَرِضْوَٰنٍۢ وَجَنَّٰتٍۢ لَّهُمْ فِيهَا نَعِيمٌۭ مُّقِيمٌ
- (9:72) [listed for 88:8] وَعَدَ ٱللَّهُ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ أَكْبَرُ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (11:108) [listed for 88:8] ۞ وَأَمَّا ٱلَّذِينَ سُعِدُوا۟ فَفِى ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۖ عَطَآءً غَيْرَ مَجْذُوذٍۢ
- (13:23) [listed for 88:8] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۖ وَٱلْمَلَٰٓئِكَةُ يَدْخُلُونَ عَلَيْهِم مِّن كُلِّ بَابٍۢ
- (15:45) [listed for 88:8] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (16:5) [listed for 88:8] [cited in ¶19] وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ
- (16:31) [listed for 88:8] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ لَهُمْ فِيهَا مَا يَشَآءُونَ ۚ كَذَٰلِكَ يَجْزِى ٱللَّهُ ٱلْمُتَّقِينَ
- (18:31) [listed for 88:8] أُو۟لَٰٓئِكَ لَهُمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَيَلْبَسُونَ ثِيَابًا خُضْرًۭا مِّن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًۭا
- (18:107) [listed for 88:8] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ كَانَتْ لَهُمْ جَنَّٰتُ ٱلْفِرْدَوْسِ نُزُلًا
- (19:61) [listed for 88:8] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (20:111) [listed for 88:8] ۞ وَعَنَتِ ٱلْوُجُوهُ لِلْحَىِّ ٱلْقَيُّومِ ۖ وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا
- (23:104) [listed for 88:8] تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ
- (25:15) [listed for 88:8] قُلْ أَذَٰلِكَ خَيْرٌ أَمْ جَنَّةُ ٱلْخُلْدِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۚ كَانَتْ لَهُمْ جَزَآءًۭ وَمَصِيرًۭا
- (26:133) [listed for 88:8] أَمَدَّكُم بِأَنْعَٰمٍۢ وَبَنِينَ
- (31:8) [listed for 88:8] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ
- (32:17) [listed for 88:8] [cited in ¶10] فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (33:66) [listed for 88:8] يَوْمَ تُقَلَّبُ وُجُوهُهُمْ فِى ٱلنَّارِ يَقُولُونَ يَٰلَيْتَنَآ أَطَعْنَا ٱللَّهَ وَأَطَعْنَا ٱلرَّسُولَا۠
- (35:3) [listed for 88:8] يَٰٓأَيُّهَا ٱلنَّاسُ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ ۚ هَلْ مِنْ خَٰلِقٍ غَيْرُ ٱللَّهِ يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (36:55) [listed for 88:8] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (36:71) [listed for 88:8] أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ
- (37:40) [listed for 88:8] إِلَّا عِبَادَ ٱللَّهِ ٱلْمُخْلَصِينَ
- (37:57) [listed for 88:8] وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ
- (38:50) [listed for 88:8] جَنَّٰتِ عَدْنٍۢ مُّفَتَّحَةًۭ لَّهُمُ ٱلْأَبْوَٰبُ
- (39:60) [listed for 88:8] وَيَوْمَ ٱلْقِيَٰمَةِ تَرَى ٱلَّذِينَ كَذَبُوا۟ عَلَى ٱللَّهِ وُجُوهُهُم مُّسْوَدَّةٌ ۚ أَلَيْسَ فِى جَهَنَّمَ مَثْوًۭى لِّلْمُتَكَبِّرِينَ
- (39:73) [listed for 88:8] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
- (40:8) [listed for 88:8] رَبَّنَا وَأَدْخِلْهُمْ جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدتَّهُمْ وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (41:30) [listed for 88:8] إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟ تَتَنَزَّلُ عَلَيْهِمُ ٱلْمَلَٰٓئِكَةُ أَلَّا تَخَافُوا۟ وَلَا تَحْزَنُوا۟ وَأَبْشِرُوا۟ بِٱلْجَنَّةِ ٱلَّتِى كُنتُمْ تُوعَدُونَ
- (43:17) [listed for 88:8] وَإِذَا بُشِّرَ أَحَدُهُم بِمَا ضَرَبَ لِلرَّحْمَٰنِ مَثَلًۭا ظَلَّ وَجْهُهُۥ مُسْوَدًّۭا وَهُوَ كَظِيمٌ
- (43:68) [listed for 88:8] يَٰعِبَادِ لَا خَوْفٌ عَلَيْكُمُ ٱلْيَوْمَ وَلَآ أَنتُمْ تَحْزَنُونَ
- (43:70) [listed for 88:8] ٱدْخُلُوا۟ ٱلْجَنَّةَ أَنتُمْ وَأَزْوَٰجُكُمْ تُحْبَرُونَ
- (44:51) [listed for 88:8] إِنَّ ٱلْمُتَّقِينَ فِى مَقَامٍ أَمِينٍۢ
- (47:15) [listed for 88:8] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (48:29) [listed for 88:8] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
- (49:8) [listed for 88:8] فَضْلًۭا مِّنَ ٱللَّهِ وَنِعْمَةًۭ ۚ وَٱللَّهُ عَلِيمٌ حَكِيمٌۭ
- (52:18) [listed for 88:8] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (54:35) [listed for 88:8] نِّعْمَةًۭ مِّنْ عِندِنَا ۚ كَذَٰلِكَ نَجْزِى مَن شَكَرَ
- (55:46) [listed for 88:8] وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- (56:27) [listed for 88:8] وَأَصْحَٰبُ ٱلْيَمِينِ مَآ أَصْحَٰبُ ٱلْيَمِينِ
- (57:12) [listed for 88:8] يَوْمَ تَرَى ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ يَسْعَىٰ نُورُهُم بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِم بُشْرَىٰكُمُ ٱلْيَوْمَ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (67:27) [listed for 88:8] فَلَمَّا رَأَوْهُ زُلْفَةًۭ سِيٓـَٔتْ وُجُوهُ ٱلَّذِينَ كَفَرُوا۟ وَقِيلَ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تَدَّعُونَ
- (68:2) [listed for 88:8] مَآ أَنتَ بِنِعْمَةِ رَبِّكَ بِمَجْنُونٍۢ
- (68:43) [listed for 88:8] خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ
- (69:22) [listed for 88:8] [cited in ¶14] فِى جَنَّةٍ عَالِيَةٍۢ
- (70:35) [listed for 88:8] أُو۟لَٰٓئِكَ فِى جَنَّٰتٍۢ مُّكْرَمُونَ
- (70:44) [listed for 88:8] خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۚ ذَٰلِكَ ٱلْيَوْمُ ٱلَّذِى كَانُوا۟ يُوعَدُونَ
- (74:39) [listed for 88:8] إِلَّآ أَصْحَٰبَ ٱلْيَمِينِ
- (75:24) [listed for 88:8] [cited in ¶2] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ
- (75:25) [listed for 88:8] تَظُنُّ أَن يُفْعَلَ بِهَا فَاقِرَةٌۭ
- (77:41) [listed for 88:8] إِنَّ ٱلْمُتَّقِينَ فِى ظِلَٰلٍۢ وَعُيُونٍۢ
- (78:31) [listed for 88:8] إِنَّ لِلْمُتَّقِينَ مَفَازًا
- (79:33) [listed for 88:8] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (80:38) [listed for 88:8] [cited in ¶2] وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ
- (80:40) [listed for 88:8] [cited in ¶2] وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ
- (82:13) [listed for 88:8] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍۢ
- (83:22) [listed for 88:8] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:26) [listed for 88:8] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ
- (83:27) [listed for 88:8] وَمِزَاجُهُۥ مِن تَسْنِيمٍ
- (83:28) [listed for 88:8] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
- (89:29) [listed for 88:8] فَٱدْخُلِى فِى عِبَٰدِى
- (92:19) [listed for 88:8] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (92:20) [listed for 88:8] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (92:21) [listed for 88:8] وَلَسَوْفَ يَرْضَىٰ
- (93:11) [listed for 88:8] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (102:8) [listed for 88:8] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

## named by the passage's own list as strong for this ayah (5)

- (41:32) [listed for 88:8] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (76:10) [listed for 88:8] إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا
- (76:21) [listed for 88:8] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:43) [listed for 88:8] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (101:7) [listed for 88:8] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## named by the passage's own list as medium for this ayah (21)

- (18:108) [listed for 88:8] خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا
- (19:85) [listed for 88:8] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
- (22:72) [listed for 88:8] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ تَعْرِفُ فِى وُجُوهِ ٱلَّذِينَ كَفَرُوا۟ ٱلْمُنكَرَ ۖ يَكَادُونَ يَسْطُونَ بِٱلَّذِينَ يَتْلُونَ عَلَيْهِمْ ءَايَٰتِنَا ۗ قُلْ أَفَأُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكُمُ ۗ ٱلنَّارُ وَعَدَهَا ٱللَّهُ ٱلَّذِينَ كَفَرُوا۟ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (25:75) [listed for 88:8] أُو۟لَٰٓئِكَ يُجْزَوْنَ ٱلْغُرْفَةَ بِمَا صَبَرُوا۟ وَيُلَقَّوْنَ فِيهَا تَحِيَّةًۭ وَسَلَٰمًا
- (33:44) [listed for 88:8] تَحِيَّتُهُمْ يَوْمَ يَلْقَوْنَهُۥ سَلَٰمٌۭ ۚ وَأَعَدَّ لَهُمْ أَجْرًۭا كَرِيمًۭا
- (33:69) [listed for 88:8] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَكُونُوا۟ كَٱلَّذِينَ ءَاذَوْا۟ مُوسَىٰ فَبَرَّأَهُ ٱللَّهُ مِمَّا قَالُوا۟ ۚ وَكَانَ عِندَ ٱللَّهِ وَجِيهًۭا
- (36:59) [listed for 88:8] وَٱمْتَٰزُوا۟ ٱلْيَوْمَ أَيُّهَا ٱلْمُجْرِمُونَ
- (37:42) [listed for 88:8] فَوَٰكِهُ ۖ وَهُم مُّكْرَمُونَ
- (37:43) [listed for 88:8] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (42:7) [listed for 88:8] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ قُرْءَانًا عَرَبِيًّۭا لِّتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا وَتُنذِرَ يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ ۚ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ
- (43:71) [listed for 88:8] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (44:57) [listed for 88:8] فَضْلًۭا مِّن رَّبِّكَ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (52:19) [listed for 88:8] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (56:18) [listed for 88:8] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:89) [listed for 88:8] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (64:9) [listed for 88:8] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (69:24) [listed for 88:8] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ
- (73:11) [listed for 88:8] [cited in ¶17] وَذَرْنِى وَٱلْمُكَذِّبِينَ أُو۟لِى ٱلنَّعْمَةِ وَمَهِّلْهُمْ قَلِيلًا
- (75:12) [listed for 88:8] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ
- (79:9) [listed for 88:8] أَبْصَٰرُهَا خَٰشِعَةٌۭ
- (80:41) [listed for 88:8] تَرْهَقُهَا قَتَرَةٌ

## weak (this ayah's own list) (27)

- (1:2) [listed for 88:8] ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (2:47) [listed for 88:8] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:122) [listed for 88:8] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:150) [listed for 88:8] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
- (3:72) [listed for 88:8] وَقَالَت طَّآئِفَةٌۭ مِّنْ أَهْلِ ٱلْكِتَٰبِ ءَامِنُوا۟ بِٱلَّذِىٓ أُنزِلَ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَجْهَ ٱلنَّهَارِ وَٱكْفُرُوٓا۟ ءَاخِرَهُۥ لَعَلَّهُمْ يَرْجِعُونَ
- (5:6) [listed for 88:8] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (5:20) [listed for 88:8] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ إِذْ جَعَلَ فِيكُمْ أَنۢبِيَآءَ وَجَعَلَكُم مُّلُوكًۭا وَءَاتَىٰكُم مَّا لَمْ يُؤْتِ أَحَدًۭا مِّنَ ٱلْعَٰلَمِينَ
- (6:16) [listed for 88:8] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (8:16) [listed for 88:8] وَمَن يُوَلِّهِمْ يَوْمَئِذٍۢ دُبُرَهُۥٓ إِلَّا مُتَحَرِّفًۭا لِّقِتَالٍ أَوْ مُتَحَيِّزًا إِلَىٰ فِئَةٍۢ فَقَدْ بَآءَ بِغَضَبٍۢ مِّنَ ٱللَّهِ وَمَأْوَىٰهُ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (12:9) [listed for 88:8] ٱقْتُلُوا۟ يُوسُفَ أَوِ ٱطْرَحُوهُ أَرْضًۭا يَخْلُ لَكُمْ وَجْهُ أَبِيكُمْ وَتَكُونُوا۟ مِنۢ بَعْدِهِۦ قَوْمًۭا صَٰلِحِينَ
- (16:76) [listed for 88:8] وَضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلَيْنِ أَحَدُهُمَآ أَبْكَمُ لَا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَهُوَ كَلٌّ عَلَىٰ مَوْلَىٰهُ أَيْنَمَا يُوَجِّههُّ لَا يَأْتِ بِخَيْرٍ ۖ هَلْ يَسْتَوِى هُوَ وَمَن يَأْمُرُ بِٱلْعَدْلِ ۙ وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (22:56) [listed for 88:8] ٱلْمُلْكُ يَوْمَئِذٍۢ لِّلَّهِ يَحْكُمُ بَيْنَهُمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (25:24) [listed for 88:8] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (25:44) [listed for 88:8] أَمْ تَحْسَبُ أَنَّ أَكْثَرَهُمْ يَسْمَعُونَ أَوْ يَعْقِلُونَ ۚ إِنْ هُمْ إِلَّا كَٱلْأَنْعَٰمِ ۖ بَلْ هُمْ أَضَلُّ سَبِيلًا
- (35:28) [listed for 88:8] وَمِنَ ٱلنَّاسِ وَٱلدَّوَآبِّ وَٱلْأَنْعَٰمِ مُخْتَلِفٌ أَلْوَٰنُهُۥ كَذَٰلِكَ ۗ إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟ ۗ إِنَّ ٱللَّهَ عَزِيزٌ غَفُورٌ
- (40:79) [listed for 88:8] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَنْعَٰمَ لِتَرْكَبُوا۟ مِنْهَا وَمِنْهَا تَأْكُلُونَ
- (47:12) [listed for 88:8] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
- (52:17) [listed for 88:8] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَعِيمٍۢ
- (74:26) [listed for 88:8] سَأُصْلِيهِ سَقَرَ
- (76:9) [listed for 88:8] إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا
- (76:20) [listed for 88:8] وَإِذَا رَأَيْتَ ثَمَّ رَأَيْتَ نَعِيمًۭا وَمُلْكًۭا كَبِيرًا
- (84:25) [listed for 88:8] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۭ
- (92:12) [listed for 88:8] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:14) [listed for 88:8] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:16) [listed for 88:8] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:18) [listed for 88:8] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- (99:6) [listed for 88:8] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ

## named by the passage's own list as weak for this ayah (11)

- (6:79) [listed for 88:8] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (27:90) [listed for 88:8] وَمَن جَآءَ بِٱلسَّيِّئَةِ فَكُبَّتْ وُجُوهُهُمْ فِى ٱلنَّارِ هَلْ تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (31:31) [listed for 88:8] أَلَمْ تَرَ أَنَّ ٱلْفُلْكَ تَجْرِى فِى ٱلْبَحْرِ بِنِعْمَتِ ٱللَّهِ لِيُرِيَكُم مِّنْ ءَايَٰتِهِۦٓ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (37:49) [listed for 88:8] كَأَنَّهُنَّ بَيْضٌۭ مَّكْنُونٌۭ
- (47:27) [listed for 88:8] فَكَيْفَ إِذَا تَوَفَّتْهُمُ ٱلْمَلَٰٓئِكَةُ يَضْرِبُونَ وُجُوهَهُمْ وَأَدْبَٰرَهُمْ
- (55:27) [listed for 88:8] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (69:15) [listed for 88:8] فَيَوْمَئِذٍۢ وَقَعَتِ ٱلْوَاقِعَةُ
- (69:18) [listed for 88:8] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (69:23) [listed for 88:8] قُطُوفُهَا دَانِيَةٌۭ
- (79:8) [listed for 88:8] قُلُوبٌۭ يَوْمَئِذٍۢ وَاجِفَةٌ
- (80:32) [listed for 88:8] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ

## neighbours: within two ayat of a passage the commentary cites (51)

- (1:5) [next to 1:7] إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- (1:6) [next to 1:7] ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (2:110) [next to 2:112] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ ۗ إِنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (2:111) [next to 2:112] وَقَالُوا۟ لَن يَدْخُلَ ٱلْجَنَّةَ إِلَّا مَن كَانَ هُودًا أَوْ نَصَٰرَىٰ ۗ تِلْكَ أَمَانِيُّهُمْ ۗ قُلْ هَاتُوا۟ بُرْهَٰنَكُمْ إِن كُنتُمْ صَٰدِقِينَ
- (2:113) [next to 2:112] وَقَالَتِ ٱلْيَهُودُ لَيْسَتِ ٱلنَّصَٰرَىٰ عَلَىٰ شَىْءٍۢ وَقَالَتِ ٱلنَّصَٰرَىٰ لَيْسَتِ ٱلْيَهُودُ عَلَىٰ شَىْءٍۢ وَهُمْ يَتْلُونَ ٱلْكِتَٰبَ ۗ كَذَٰلِكَ قَالَ ٱلَّذِينَ لَا يَعْلَمُونَ مِثْلَ قَوْلِهِمْ ۚ فَٱللَّهُ يَحْكُمُ بَيْنَهُمْ يَوْمَ ٱلْقِيَٰمَةِ فِيمَا كَانُوا۟ فِيهِ يَخْتَلِفُونَ
- (2:114) [next to 2:112] وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ وَسَعَىٰ فِى خَرَابِهَآ ۚ أُو۟لَٰٓئِكَ مَا كَانَ لَهُمْ أَن يَدْخُلُوهَآ إِلَّا خَآئِفِينَ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (3:12) [next to 3:14] قُل لِّلَّذِينَ كَفَرُوا۟ سَتُغْلَبُونَ وَتُحْشَرُونَ إِلَىٰ جَهَنَّمَ ۚ وَبِئْسَ ٱلْمِهَادُ
- (3:13) [next to 3:14] قَدْ كَانَ لَكُمْ ءَايَةٌۭ فِى فِئَتَيْنِ ٱلْتَقَتَا ۖ فِئَةٌۭ تُقَٰتِلُ فِى سَبِيلِ ٱللَّهِ وَأُخْرَىٰ كَافِرَةٌۭ يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ۚ وَٱللَّهُ يُؤَيِّدُ بِنَصْرِهِۦ مَن يَشَآءُ ۗ إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّأُو۟لِى ٱلْأَبْصَٰرِ
- (3:15) [next to 3:14] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:16) [next to 3:14] ٱلَّذِينَ يَقُولُونَ رَبَّنَآ إِنَّنَآ ءَامَنَّا فَٱغْفِرْ لَنَا ذُنُوبَنَا وَقِنَا عَذَابَ ٱلنَّارِ
- (3:134) [next to 3:136] ٱلَّذِينَ يُنفِقُونَ فِى ٱلسَّرَّآءِ وَٱلضَّرَّآءِ وَٱلْكَٰظِمِينَ ٱلْغَيْظَ وَٱلْعَافِينَ عَنِ ٱلنَّاسِ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
- (3:135) [next to 3:136] وَٱلَّذِينَ إِذَا فَعَلُوا۟ فَٰحِشَةً أَوْ ظَلَمُوٓا۟ أَنفُسَهُمْ ذَكَرُوا۟ ٱللَّهَ فَٱسْتَغْفَرُوا۟ لِذُنُوبِهِمْ وَمَن يَغْفِرُ ٱلذُّنُوبَ إِلَّا ٱللَّهُ وَلَمْ يُصِرُّوا۟ عَلَىٰ مَا فَعَلُوا۟ وَهُمْ يَعْلَمُونَ
- (3:137) [next to 3:136] قَدْ خَلَتْ مِن قَبْلِكُمْ سُنَنٌۭ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (3:138) [next to 3:136] هَٰذَا بَيَانٌۭ لِّلنَّاسِ وَهُدًۭى وَمَوْعِظَةٌۭ لِّلْمُتَّقِينَ
- (16:3) [next to 16:5] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ تَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (16:4) [next to 16:5] خَلَقَ ٱلْإِنسَٰنَ مِن نُّطْفَةٍۢ فَإِذَا هُوَ خَصِيمٌۭ مُّبِينٌۭ
- (16:6) [next to 16:5] وَلَكُمْ فِيهَا جَمَالٌ حِينَ تُرِيحُونَ وَحِينَ تَسْرَحُونَ
- (16:7) [next to 16:5] وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ ۚ إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ
- (28:86) [next to 28:88] وَمَا كُنتَ تَرْجُوٓا۟ أَن يُلْقَىٰٓ إِلَيْكَ ٱلْكِتَٰبُ إِلَّا رَحْمَةًۭ مِّن رَّبِّكَ ۖ فَلَا تَكُونَنَّ ظَهِيرًۭا لِّلْكَٰفِرِينَ
- (28:87) [next to 28:88] وَلَا يَصُدُّنَّكَ عَنْ ءَايَٰتِ ٱللَّهِ بَعْدَ إِذْ أُنزِلَتْ إِلَيْكَ ۖ وَٱدْعُ إِلَىٰ رَبِّكَ ۖ وَلَا تَكُونَنَّ مِنَ ٱلْمُشْرِكِينَ
- (29:56) [next to 29:58] يَٰعِبَادِىَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ أَرْضِى وَٰسِعَةٌۭ فَإِيَّٰىَ فَٱعْبُدُونِ
- (29:57) [next to 29:58] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۖ ثُمَّ إِلَيْنَا تُرْجَعُونَ
- (29:59) [next to 29:58] ٱلَّذِينَ صَبَرُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (29:60) [next to 29:58] وَكَأَيِّن مِّن دَآبَّةٍۢ لَّا تَحْمِلُ رِزْقَهَا ٱللَّهُ يَرْزُقُهَا وَإِيَّاكُمْ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (32:15) [next to 32:17] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (32:16) [next to 32:17] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (32:18) [next to 32:17] أَفَمَن كَانَ مُؤْمِنًۭا كَمَن كَانَ فَاسِقًۭا ۚ لَّا يَسْتَوُۥنَ
- (32:19) [next to 32:17] أَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ جَنَّٰتُ ٱلْمَأْوَىٰ نُزُلًۢا بِمَا كَانُوا۟ يَعْمَلُونَ
- (39:72) [next to 39:74] قِيلَ ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (39:75) [next to 39:74] وَتَرَى ٱلْمَلَٰٓئِكَةَ حَآفِّينَ مِنْ حَوْلِ ٱلْعَرْشِ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ ۖ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَقِيلَ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (44:23) [next to 44:25] فَأَسْرِ بِعِبَادِى لَيْلًا إِنَّكُم مُّتَّبَعُونَ
- (44:24) [next to 44:25] وَٱتْرُكِ ٱلْبَحْرَ رَهْوًا ۖ إِنَّهُمْ جُندٌۭ مُّغْرَقُونَ
- (44:26) [next to 44:25] وَزُرُوعٍۢ وَمَقَامٍۢ كَرِيمٍۢ
- (44:28) [next to 44:27] كَذَٰلِكَ ۖ وَأَوْرَثْنَٰهَا قَوْمًا ءَاخَرِينَ
- (44:29) [next to 44:27] فَمَا بَكَتْ عَلَيْهِمُ ٱلسَّمَآءُ وَٱلْأَرْضُ وَمَا كَانُوا۟ مُنظَرِينَ
- (69:19) [next to 69:20] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (73:9) [next to 73:11] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (73:10) [next to 73:11] وَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَٱهْجُرْهُمْ هَجْرًۭا جَمِيلًۭا
- (73:12) [next to 73:11] إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا
- (73:13) [next to 73:11] وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا
- (75:20) [next to 75:22] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
- (75:21) [next to 75:22] وَتَذَرُونَ ٱلْءَاخِرَةَ
- (75:26) [next to 75:24] كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ
- (80:36) [next to 80:38] وَصَٰحِبَتِهِۦ وَبَنِيهِ
- (80:37) [next to 80:38] لِكُلِّ ٱمْرِئٍۢ مِّنْهُمْ يَوْمَئِذٍۢ شَأْنٌۭ يُغْنِيهِ
- (80:42) [next to 80:40] أُو۟لَٰٓئِكَ هُمُ ٱلْكَفَرَةُ ٱلْفَجَرَةُ
- (83:23) [next to 83:24] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ
- (89:13) [next to 89:15] فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- (89:14) [next to 89:15] إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- (89:16) [next to 89:15] وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- (89:17) [next to 89:15] كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ

