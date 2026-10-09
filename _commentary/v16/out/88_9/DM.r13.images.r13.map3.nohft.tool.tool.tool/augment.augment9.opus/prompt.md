Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:9; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_9/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_9.reading.tr.md (prose paragraphs numbered) =====
## Kendi emeğine bakan yüz

[¶1] Dokuzuncu ayet yalnızca iki kelimedir. Tek başına bir cümle de değildir; sekizinci ayetteki yüzlere bağlanan ikinci bir sıfattır. Önce {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutludur, source:88:8} denir, ardından {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnuttur, source:88:9} gelir. "Onun çabası" sözündeki zamir dişildir ve yüzlere döner. Arapça insanı yüzüyle anabilir; burada da çabalayan ve hoşnut olan, yüzün sahibidir. Yine de söz yüzde kalır, çünkü hoşnutluk her şeyden önce yüzde görünen bir şeydir.

[¶2] Kelimelerin sırası dikkat ister. Olağan sıra önce "hoşnut", sonra "çabasından" olurdu. Ayet "çabasından"ı öne alır. Öne alınan söz vurgu taşır: bu yüzü hoşnut eden şey, başka bir şeyden önce kendi çabasıdır. Bu sıralama hoşnutluk kelimesini ayetin sonuna da bırakır. Böylece dokuzuncu ayetten on ikinci ayete kadar her ayet aynı sesle biter: râdiye, âliye, lâğiye, câriye. Hoşnutluk, bahçenin anlatıldığı bu dizinin ilk sesi olur.

[¶3] Bağlayan edat da kendine özgüdür. Arapçada hoşnutluk çoğunlukla "bir şeyle" ya da "birinden" diye kurulur. Burada ise "için, -e karşı" anlamı da veren li- edatı gelir. Bu yüz çabasına dönüp bakar ve ondan hoşnuttur; hoşnutluğu da o çabadan doğmuştur. Aynı edat hem bakışın yönünü hem de sevincin nedenini gösterir.

[¶4] Bu ayetin ağırlığı, üçüncü ayetle karşılaştırılınca ortaya çıkar. Öteki yüzler de çalışmıştı: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıbe, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Araplar çaba kelimesini doğrudan iş kelimesiyle açıklarlardı: {ar:كل عمل من خير أو شر فهو السعي, tr:küllü amelin min hayrin ev şerrin fe-huve's-sa'y, gloss:iyi ya da kötü her iş sa'ydir, source:"س ع ي,B002"}. Bu yüzden iki grup yüz arasındaki fark, çalışmak ile çalışmamak arasında değildir. İki taraf da emek vermiştir. Birinin emeği üstünde yorgunluk olarak kalmıştır; ötekinin emeği ona hoşnutluk olarak geri döner. Üçüncü ayetteki ücret ve pay kelimelerinin, yedinci ayetteki "yetmez" sözünün ve yirmi altıncı ayetteki hesabın birlikte kurduğu sahne, surenin geneline aittir. Bu ayet o sahneye kendi sözünü ekler: emeğin hesabı görüldüğünde bu yüz gördüğünden memnundur.

[¶5] Kelimenin kendisi iyiyi kötüden ayırmaz. Ciddiyetle yürütülen her iş için kullanılır: {ar:يستعمل للجد في الأمر خيرا كان أو شرا, tr:yusta'melu li'l-ciddi fi'l-emri hayran kâne ev şerrâ, gloss:bir işte ciddi uğraş için kullanılır; iyi olsun kötü olsun, source:"س ع ي,B002"}. Kur'an aynı kelimeyi bozgunculuk için de kullanır. Dünya hayatına dair sözü insanı hayran bırakan, kalbindekine Allah'ı şahit tutan, ama düşmanlıkta en inatçı olan biri anlatılır {source:2:204}. Onun için şöyle denir: {ar:وَإِذَا تَوَلَّىٰ سَعَىٰ فِى ٱلْأَرْضِ لِيُفْسِدَ فِيهَا, tr:ve izâ tevellâ seâ fi'l-ardı li-yufside fîhâ, gloss:yüz çevirince yeryüzünde bozgunculuk yapmak için koşturur, source:2:205}. Oradaki "yüz çevirince" fiili, surenin yirmi üçüncü ayetindeki fiildir: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Demek ki çaba, yüz çevirenin de elinde bir güçtür. Bu ayetteki çabayı iyi yapan şey kelimenin kendisi değildir; yüzün o çabaya bakarken duyduğu hoşnutluktur.

## Bir yere doğru yürümek

[¶6] Çaba kelimesinin Arapçadaki ilk yeri ayaktır. Bu kelime şiddetli olmayan bir koşu için kullanılırdı: {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan bir koşudur, source:"س ع ي,B001"}. Kelimenin bu türden birkaç kullanımı vardı: {ar:سعى إذا مشى وسعى إذا عدا وسعى إذا قصد, tr:seâ izâ meşâ ve seâ izâ adâ ve seâ izâ kasad, gloss:yürüdüğünde de koştuğunda da bir yere yöneldiğinde de seâ denir, source:"س ع ي,B001"}. Bu ayak imgesi ayetteki "çaba" anlamının yerine geçmez. Ama onun yanında duyulur. Bu kelimeyle anılan çaba, yerinde sayan bir didinme değildir. Bir hedefe doğru adım adım, nefes kesmeden ama gevşemeden yapılan bir yürüyüştür. Ayetin hemen ardından o yürüyüşün nereye vardığı söylenir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10}. Yol yokuş yukarı gitmiştir ve sonunda bir varış vardır.

[¶7] Hac ibadetindeki bir yürüyüş de bu kelimeyle anılır: {ar:وخص المشي فيما بين الصفا والمروة بالسعي, tr:ve hussa'l-meşyu fîmâ beyne's-Safâ ve'l-Merveti bi's-sa'y, gloss:Safa ile Merve arasındaki yürüyüşe özel olarak sa'y denir, source:"س ع ي,B001"}. Türkçede sa'y kelimesi bugün çoğunlukla bu ibadetin adı olarak yaşar, bir de eski "sa'y ü gayret" deyiminde kalmıştır. Arapçada ise aynı kelime hem ayakların bir yere doğru gidişini hem de bir ömrün bütün emeğini adlandırır. Ayet, ömrü bir yere doğru yapılmış uzun bir yürüyüş olarak görmeye izin verir.

[¶8] Kur'an bu yönelişi bir çağrıya karşılık olarak da anlatır. Allah inananlara cuma günü namaz için çağrıldıklarında ne yapacaklarını söyler: {ar:فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ, tr:fes'av ilâ zikrillâhi ve zeru'l-bey', gloss:Allah'ı anmaya koşun ve alışverişi bırakın, source:62:9}. Hemen ardından, namaz bitince yeryüzüne dağılıp Allah'ın lütfundan aramaları söylenir {source:62:10}. Orada bu fiil, kazancı bir süre bırakıp anmaya yürümek anlamına gelir. Böylece aynı kelime, insanın geçimi için koşturmasını da, o koşturmayı bırakıp Allah'a yönelmesini de kapsar. Hoşnut yüzün çabası, bu iki yönelişin doğru yerde birleştiği bir yürüyüştür.

[¶9] Yürüyüşün bir yarışa dönüştüğü bir kullanım da vardır: {ar:ساعانى فلان فسعيته أسعيه إذا غلبته فيه, tr:sâ'ânî fulânun fe-sa'aytuhû es'îhi izâ ğalebtuhû fîh, gloss:biri benimle koşuda yarıştı ben de onu geçtim, source:"س ع ي,B008"}. Ayetin öteki kelimesinde de aynı kalıp görülür: {ar:راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه, tr:râdânî fulânun fe-radavtuhû erdûhu bi'd-dammi izâ ğalebtuhû fîh, gloss:biri benimle hoşnutlukta yarıştı ben de onu geçtim, source:"ر ض و,B005"}. Bu "yarıştı ve onu geçtim" kalıbı Arapçada pek çok fiilde kurulabilir. Dolayısıyla iki kelimeyi birbirine bağlayan bir kök ortaklığı yoktur. Yine de kendi başına her biri yerindedir. Çaba kelimesinin yarışı bir koşudur. Kur'an da iyilerin yüzünü anlatırken böyle bir yarıştan söz eder. Hileli tartanların kınandığı bir surede, iyiler nimet içinde ve sedirler üstünde bakarken gösterilir. Onlar için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Mühürlü içecekten söz edildikten sonra da şu çağrı gelir: {ar:وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ, tr:ve fî zâlike fe'l-yetenâfesi'l-mutenâfisûn, gloss:yarışanlar işte bunun için yarışsın, source:83:26}. Hoşnut yüz, bu koşuyu bitirmiş birinin yüzüdür.

[¶10] Surenin kendi yolu da yürüyüş kelimeleriyle kurulur. Birinci ayetteki "geldi mi" ile yirmi beşinci ayetteki "dönüş", deve sürücülerinin dilinde yürüyen bir hayvanın ayak hareketlerini de anlatır. Bu ayetteki çaba da, aradaki o kelimeler arasında, devenin şiddetli olmayan koşusunun adıdır.

## Görülen ve örtülmeyen çaba

[¶11] Kur'an çabayı kaybolmayan bir şey olarak anlatır. Musa'nın sayfalarında ve sözünü yerine getiren İbrahim'in sayfalarında bulunduğu bildirilen sözler arasında şunlar vardır {source:53:37}: {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için çabaladığından başkası yoktur, source:53:39}; {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:çabası görülecektir, source:53:40}. O ayette çaba görülecek bir şeydir. Bu ayette ise yüz onu görmüştür ve gördüğünden hoşnuttur.

[¶12] Bu ayetin kuruluşunun aynısı başka bir yerde de geçer. Allah peygamberlerin kıssalarını anlattıktan sonra insanlara "bu sizin tek bir ümmetinizdir" der. Onların işlerini parça parça böldüklerini söyler ve ekler: {ar:كُلٌّ إِلَيْنَا رَٰجِعُونَ, tr:kullun ileynâ râciûn, gloss:hepsi Bize dönecektir, source:21:93}. Ardından şöyle gelir: {ar:فَلَا كُفْرَانَ لِسَعْيِهِۦ وَإِنَّا لَهُۥ كَٰتِبُونَ, tr:fe-lâ kufrâne li-sa'yihî ve innâ lehû kâtibûn, gloss:onun çabası inkâr edilmez; Biz onu yazmaktayız, source:21:94}. Orada da çaba kelimesi aynı edatla ve aynı zamirle gelir: "onun çabasına". Bu söz, salih iş yapan ve inanan kişi için söylenir. Surenin sonundaki iki ayet de aynı sırayı izler: önce "dönüşleri Bize'dir", sonra "hesapları Bize aittir" denir. Oradaki "inkâr" kelimesi, yirmi üçüncü ayetteki "inkâr etti" fiiliyle aynı köktendir. Bu kökün temel anlamı örtmektir. Yüz çevirip inkâr eden, verileni örtmüştür. Salih iş yapanın çabası ise örtülmez, yazılır. Dokuzuncu ayetteki hoşnutluk, örtülmeden yazılmış bir çabanın sahibinin duyduğu sevinçtir.

[¶13] Kur'an, surenin iki yüzünü bir başka yerde iki ayette yan yana koyar. Önce şöyle denir: {ar:مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ, tr:men kâne yurîdu'l-âcile, gloss:kim çabuk geçeni isterse, source:17:18}. Onun sonu da şöyle anlatılır: {ar:ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا, tr:summe cealnâ lehû cehenneme yaslâhâ mezmûmen medhûrâ, gloss:sonra ona cehennemi hazırladık; kınanmış ve kovulmuş olarak oraya girer, source:17:18}. Oradaki "girer" fiili, dördüncü ayetteki ateşe girme fiilidir. Hemen ardından öteki taraf gelir: {ar:وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا, tr:ve men erâde'l-âhirete ve seâ lehâ sa'yehâ ve huve mu'minun fe-ulâike kâne sa'yuhum meşkûrâ, gloss:kim de inanarak ahireti ister ve onun için ona yakışan çabayı gösterirse işte onların çabası şükürle karşılanır, source:17:19}. Bahçe halkına da, gümüş bileziklerle süslenip Rablerinin temiz içeceğiyle sulandıktan sonra {source:76:21} aynı söz söylenir: {ar:إِنَّ هَٰذَا كَانَ لَكُمْ جَزَآءًۭ وَكَانَ سَعْيُكُم مَّشْكُورًا, tr:inne hâzâ kâne lekum cezâen ve kâne sa'yukum meşkûrâ, gloss:bu sizin için bir karşılıktır ve çabanız şükürle karşılanmıştır, source:76:22}. Böylece aynı çabaya iki taraftan bakılmış olur. Allah o çabayı teşekkürle karşılar. Yüz de ondan hoşnuttur.

[¶14] Öteki ucu da Kur'an adlandırır: {ar:ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ellezîne dalle sa'yuhum fi'l-hayâti'd-dünyâ, gloss:dünya hayatında çabaları yolunu yitirenler, source:18:104}. Ayet devamında bu insanların güzel iş yaptıklarını sandıklarını söyler. Burada "yolunu yitirmek" fiili, yürüyüş imgesini tamamlar. Bu çaba yürümüştür ama yolu kaybetmiştir. Üçüncü ayetteki bitkin yüz böyle bir yürüyüşün sonunda durur. Dokuzuncu ayetteki yüz ise yolunu bulmuş bir yürüyüşün sonundadır.

## Boynu çözen emek, başkası için taşınan yük

[¶15] Çaba kelimesinin en ağır kullanımlarından biri özgürlükle ilgilidir. Köleleştirilmiş bir kişi efendisiyle yazılı bir anlaşma yapabilirdi. Kendi bedelini belirler, o bedeli çalışıp kazanarak öderdi. Borcunu ödeyince özgür kalırdı. Araplar bu çalışmaya da çaba derlerdi: {ar:سعاية العبد إذا كوتب أن يسعى فيما يفك رقبته, tr:siâyetü'l-abdi izâ kûtibe en yes'â fîmâ yefukku rakabeteh, gloss:yazılı anlaşma yapan kölenin boynunu çözecek şey için çalışması, source:"س ع ي,B005"}. Aynı iş için {ar:سعى المكاتب في عتق رقبته سعاية, tr:seâ'l-mükâtebu fî ıtkı rakabetihî siâyeten, gloss:anlaşmalı köle boynunun azadı için çalıştı, source:"س ع ي,B005"} de denirdi. Kur'an bu anlaşmayı bilir ve inananlara buyurur: {ar:وَٱلَّذِينَ يَبْتَغُونَ ٱلْكِتَٰبَ مِمَّا مَلَكَتْ أَيْمَٰنُكُمْ فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا, tr:velleżîne yebteğûne'l-kitâbe mimmâ meleket eymânukum fe-kâtibûhum in alimtum fîhim hayrâ, gloss:elinizin altındakilerden yazılı anlaşma isteyenlerle eğer onlarda bir hayır görüyorsanız anlaşma yapın, source:24:33}. Aynı ayet, o bedelin bir kısmının da verilmesini ister: {ar:وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:ve âtûhum min mâlillâhillezî âtâkum, gloss:Allah'ın size verdiği maldan onlara verin, source:24:33}.

[¶16] Bu imge ayetin anlamının yerine geçmez, yanında durur. Ama yanında duyulduğunda hoşnutluğun türü değişir. Son taksidini ödeyip boynunu çözmüş birinin emeğine bakışı, yorgunluğun da ötesinde bir rahatlıktır. Üçüncü ayetteki yüz de emek vermişti, ama emeği hiçbir boynu çözmemişti. Kur'an boynu çözmeyi sarp bir yokuşun aşılması olarak da anlatır. İnsanın yaratılışını ve ona verilen gözü, dili, iki yolu andıktan sonra şöyle der: {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'qtehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11}. Yokuşun ne olduğu da açıklanır: {ar:فَكُّ رَقَبَةٍ, tr:fekku rakabe, gloss:bir boynu çözmek, source:90:13}. Orada çözülen boyun başkasınındır. Çabanın en yüce biçimi, kendi boynunu çözmekten başkasının boynunu çözmeye geçer. Onuncu ayetteki "yüce" bahçe de bir yokuşun ucundadır.

[¶17] Çabanın başkası için taşındığı ikinci bir kullanım da vardır. Araplar soylu ve erdemli insanların övünülecek işlerine "çabalar" derlerdi: {ar:مآثر أهل الشرف والفضل مساعي واحدتها مسعاة, tr:meâsiru ehli'ş-şerefi ve'l-fadli mesâî vâhidetuhâ mes'ât, gloss:şeref ve erdem sahiplerinin geride bıraktığı işler mesâîdir; tekili mes'âttır, source:"س ع ي,B006"}. Bu çabaların en belirgin örneği kan davasını durdurmaktı. Bir öldürme olunca iki taraf arasında kan dökülmesi sürebilirdi. O zaman biri ortaya çıkar, kan bedelini kendi üstüne alır ve yangını söndürürdü. Böyle kişilere de "çabalayanlar" adı verilirdi: {ar:أصحاب الحمالات لحقن الدماء وإطفاء النائرة سعاة, tr:ashâbu'l-hamâlâti li-hakni'd-dimâi ve itfâi'n-nâireti suât, gloss:kanı durdurmak ve fitne ateşini söndürmek için yük üstlenenlere suât denir, source:"س ع ي,B006"}. Bu kullanımda çaba, başkasının borcunu omuza almaktır.

[¶18] Kur'an bu türden bir çabayı Allah'ın yüzüne ve hoşnutluğa bağlar. Gecenin örtmesine ve gündüzün açılmasına yemin edilen bir surede Allah şöyle der: {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa'yekum le-şettâ, gloss:çabalarınız gerçekten çeşit çeşittir, source:92:4}. Sonra iki yol anlatılır. Veren ve sakınan için yol kolaylaştırılır. Cimrilik eden için ise {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:uçuruma yuvarlandığında malı ona bir yarar sağlamaz, source:92:11} denir. Buradaki "yarar sağlamaz" fiili, yedinci ayetteki "doyurmaz" fiiliyle aynıdır. Surenin sonunda veren kişi anlatılır: {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18}. Bu kişi kimseye borcunu ödemiyordur: {ar:وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ, tr:ve mâ li-ehadin indehû min ni'metin tuczâ, gloss:onun yanında karşılığı ödenecek kimsenin bir iyiliği yoktur, source:92:19}. Verişinin tek amacı da şudur: {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:illebtiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin yüzünü istemek için, source:92:20}. Sure de şu sözle kapanır: {ar:وَلَسَوْفَ يَرْضَىٰ, tr:ve le-sevfe yerdâ, gloss:ve elbette hoşnut olacaktır, source:92:21}. Bu kısa surede çabalar ayrışır, bir yüz aranır, "en yüce" sözü geçer ve iş hoşnutlukla biter. Gâşiye suresinde de çaba, yüz, "yüce" bahçe ve hoşnutluk bir arada gelir. Orada en yüce Rabbinin yüzünü isteyen kişi, burada kendi yüzü hoşnut olan kişidir.

## Öfkenin karşıtı

[¶19] Hoşnutluk kelimesi, karşıtıyla tanımlanır: {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfke ve hoşnutsuzluğun karşıtını gösteren tek bir kök, source:"ر ض و,B001"}. Türkçede "razı olmak" çoğu zaman bir şeye boyun eğmek, istemeye istemeye kabullenmek anlamına kayar; "sonunda razı oldu" deriz. Arapçadaki rıza bir kabullenme değildir. İçte kırgınlık ve öfke kalmamasıdır. Bu yüz, payına düşene katlanmış değildir; ona sevinmektedir.

[¶20] Bu hoşnutluk tek yönlü de değildir. Kulun Allah'tan hoşnutluğu ile Allah'ın kuldan hoşnutluğu aynı kelimeyle söylenir: {ar:رضا العبد عن الله ورضا الله عن العبد, tr:rıda'l-abdi anillâhi ve rıdallâhi ani'l-abd, gloss:kulun Allah'tan ve Allah'ın kuldan hoşnut olması, source:"ر ض و,B001"}. Karşılıklı hoşnutluğun da bir adı vardır: {ar:المراضاة من اثنين, tr:el-murâdâtu mine'sneyn, gloss:karşılıklı hoşnutluk iki kişi arasında olur, source:"ر ض و,B003"}. Kur'an bahçe halkını böyle anar: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıyallâhu anhum ve radû anh, gloss:Allah onlardan hoşnut olmuştur; onlar da O'ndan, source:98:8}. Bu ayette yüz kendi çabasından hoşnuttur. Çabanın teşekkürle karşılandığını söyleyen ayetlerle birlikte okunduğunda, hoşnutluk iki taraftan gelir: Allah çabayı kabul eder, yüz de kabul edilmiş çabasına sevinir.

[¶21] Uğraşarak birini hoşnut etmek için de bir söyleyiş vardı: {ar:ترضيته أرضيته بعد جهد, tr:teraddaytuhû ardaytuhû ba'de cehd, gloss:onu ancak uğraştıktan sonra hoşnut ettim, source:"ر ض و,B004"}. Bu ayette uğraş ile hoşnutluk aynı yüzde birleşir. Yüz, uğraşarak birinin gönlünü almış ve dönüp kendi uğraşına bakınca o hoşnutluğu kendi yüzünde bulmuştur.

[¶22] Bir sonraki sure aynı kelimeyi aynı biçimde kullanır. Orada yerin döküldüğü, Rabbinin ve meleklerin saf saf geldiği gün anlatılır. İnsan o gün hatırlar ve şöyle der: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önceden bir şey gönderseydim der, source:89:24}. Hemen ardından öteki ses gelir: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetuhe'n-nefsu'l-mutmainne, gloss:ey huzura kavuşmuş can, source:89:27}; {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnutluk kazanmış olarak dön, source:89:28}. İki kelime yan yana gelir: hoşnut olan ve kendisinden hoşnut olunan. Gâşiye'nin dokuzuncu ayeti bu ikiliğin ilk yarısını söyler; kabul edilmiş çaba ise ikinci yarısını taşır. Pişmanlık duyan insanın "keşke hayatım için önceden gönderseydim" sözü de, kendi çabasından hoşnut olan yüzün tam tersidir.

[¶23] Kitabı sağından verilen ve terazisi ağır gelen kişiler için de aynı kelime kullanılır, ama bu kez hoşnutluk hayatın kendisine verilir: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:artık o hoşnut bir yaşayış içindedir, source:69:21}. Bu ayette hoşnut olan yüzdür. Orada hoşnutluk yaşayışa yayılır, sanki hayatın kendisi de memnundur.

[¶24] Hoşnutluğun en yoğun biçiminin de bir adı vardı: {ar:الرضوان الرضا الكثير, tr:er-rıdvânu'r-rıda'l-kesîr, gloss:rıdvan çok büyük hoşnutluktur, source:"ر ض و,B002"}. Kur'an inananlara akan ırmakları olan bahçeleri ve güzel konutları vaat ettikten sonra şöyle der: {ar:وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ أَكْبَرُ, tr:ve rıdvânun minallâhi ekber, gloss:Allah'tan gelen hoşnutluk ise daha büyüktür, source:9:72}. Gâşiye suresi de "en büyük" kelimesini kullanır, ama yüz çevirip inkâr eden için: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah ona en büyük azabı verir, source:88:24}. Surenin bir ucunda en büyük azap vardır. Dokuzuncu ayet öteki ucun ilk sözünü söyler: emeğine dönüp bakan ve orada öfkeden hiçbir iz bulmayan bir yüz.

===== _commentary/v16/out/88_9/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: fronting li-sa'yihā gives emphasis and keeps -iya rhyme
- memory: raḍiya usually takes bi-/ʿan; lām here marks object and cause
- memory: fāʿalanī fa-faʿaltuhu contest pattern is general in Arabic
- memory: kufrān (21:94) shares root k-f-r with kafara (88:23); root sense "covering"
- memory: kitāba mechanism (agreed price paid by earnings, then freedom)
- memory: ḥamāla mechanism (shouldering blood-money to end a feud)
- memory: Turkish "razı olmak" drift to reluctant consent; "sa'y" kept mostly as hajj term
- memory: ʿīsha rāḍiya, active form with pleasing sense
- not written: س ع ي B003 tax-collector sense - no hold on this ayah's theme
- not written: س ع ي B004 informer sense - negative usage, no role here
- not written: س ع ي B007 - unrelated to the ayah
- not written: ر ض و B006 obedient/lover/guarantor - not grounded by context
- not written: ر ض و B007 Raḍwā mountain - a proper name only
- not written: echo س و ع (sāʿa beside tasʿā in 20:15) - echo root, not identity
- not written: "yasʿā li-ghārayhi" saying - meaning of ghārayn only from memory
- not written: 93:5 fa-tarḍā - addressed to the Prophet, outside the theme
- not written: 2:207 marḍāt Allāh - adds nothing beyond 92:20-21

===== passages not cited (168) =====
## strong (this ayah's own list) (19)

- (3:162) [listed for 88:9] أَفَمَنِ ٱتَّبَعَ رِضْوَٰنَ ٱللَّهِ كَمَنۢ بَآءَ بِسَخَطٍۢ مِّنَ ٱللَّهِ وَمَأْوَىٰهُ جَهَنَّمُ ۚ وَبِئْسَ ٱلْمَصِيرُ
- (5:119) [listed for 88:9] قَالَ ٱللَّهُ هَٰذَا يَوْمُ يَنفَعُ ٱلصَّٰدِقِينَ صِدْقُهُمْ ۚ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (9:21) [listed for 88:9] يُبَشِّرُهُمْ رَبُّهُم بِرَحْمَةٍۢ مِّنْهُ وَرِضْوَٰنٍۢ وَجَنَّٰتٍۢ لَّهُمْ فِيهَا نَعِيمٌۭ مُّقِيمٌ
- (9:72) [listed for 88:9] [cited in ¶24] وَعَدَ ٱللَّهُ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ أَكْبَرُ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (9:96) [listed for 88:9] يَحْلِفُونَ لَكُمْ لِتَرْضَوْا۟ عَنْهُمْ ۖ فَإِن تَرْضَوْا۟ عَنْهُمْ فَإِنَّ ٱللَّهَ لَا يَرْضَىٰ عَنِ ٱلْقَوْمِ ٱلْفَٰسِقِينَ
- (10:7) [listed for 88:9] إِنَّ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا وَرَضُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَٱطْمَأَنُّوا۟ بِهَا وَٱلَّذِينَ هُمْ عَنْ ءَايَٰتِنَا غَٰفِلُونَ
- (17:19) [listed for 88:9] [cited in ¶13] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
- (18:104) [listed for 88:9] [cited in ¶14] ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا
- (20:84) [listed for 88:9] قَالَ هُمْ أُو۟لَآءِ عَلَىٰٓ أَثَرِى وَعَجِلْتُ إِلَيْكَ رَبِّ لِتَرْضَىٰ
- (22:51) [listed for 88:9] وَٱلَّذِينَ سَعَوْا۟ فِىٓ ءَايَٰتِنَا مُعَٰجِزِينَ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَحِيمِ
- (39:7) [listed for 88:9] إِن تَكْفُرُوا۟ فَإِنَّ ٱللَّهَ غَنِىٌّ عَنكُمْ ۖ وَلَا يَرْضَىٰ لِعِبَادِهِ ٱلْكُفْرَ ۖ وَإِن تَشْكُرُوا۟ يَرْضَهُ لَكُمْ ۗ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (47:28) [listed for 88:9] ذَٰلِكَ بِأَنَّهُمُ ٱتَّبَعُوا۟ مَآ أَسْخَطَ ٱللَّهَ وَكَرِهُوا۟ رِضْوَٰنَهُۥ فَأَحْبَطَ أَعْمَٰلَهُمْ
- (53:39) [listed for 88:9] [cited in ¶11] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
- (53:40) [listed for 88:9] [cited in ¶11] وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ
- (76:22) [listed for 88:9] [cited in ¶13] إِنَّ هَٰذَا كَانَ لَكُمْ جَزَآءًۭ وَكَانَ سَعْيُكُم مَّشْكُورًا
- (79:35) [listed for 88:9] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (89:28) [listed for 88:9] [cited in ¶22] ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- (92:4) [listed for 88:9] [cited in ¶18] إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- (101:7) [listed for 88:9] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## medium (this ayah's own list) (48)

- (2:114) [listed for 88:9] وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ وَسَعَىٰ فِى خَرَابِهَآ ۚ أُو۟لَٰٓئِكَ مَا كَانَ لَهُمْ أَن يَدْخُلُوهَآ إِلَّا خَآئِفِينَ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (2:205) [listed for 88:9] [cited in ¶5] وَإِذَا تَوَلَّىٰ سَعَىٰ فِى ٱلْأَرْضِ لِيُفْسِدَ فِيهَا وَيُهْلِكَ ٱلْحَرْثَ وَٱلنَّسْلَ ۗ وَٱللَّهُ لَا يُحِبُّ ٱلْفَسَادَ
- (2:207) [listed for 88:9] وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
- (3:15) [listed for 88:9] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (4:114) [listed for 88:9] ۞ لَّا خَيْرَ فِى كَثِيرٍۢ مِّن نَّجْوَىٰهُمْ إِلَّا مَنْ أَمَرَ بِصَدَقَةٍ أَوْ مَعْرُوفٍ أَوْ إِصْلَٰحٍۭ بَيْنَ ٱلنَّاسِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ فَسَوْفَ نُؤْتِيهِ أَجْرًا عَظِيمًۭا
- (5:2) [listed for 88:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (5:3) [listed for 88:9] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (5:16) [listed for 88:9] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (5:33) [listed for 88:9] إِنَّمَا جَزَٰٓؤُا۟ ٱلَّذِينَ يُحَارِبُونَ ٱللَّهَ وَرَسُولَهُۥ وَيَسْعَوْنَ فِى ٱلْأَرْضِ فَسَادًا أَن يُقَتَّلُوٓا۟ أَوْ يُصَلَّبُوٓا۟ أَوْ تُقَطَّعَ أَيْدِيهِمْ وَأَرْجُلُهُم مِّنْ خِلَٰفٍ أَوْ يُنفَوْا۟ مِنَ ٱلْأَرْضِ ۚ ذَٰلِكَ لَهُمْ خِزْىٌۭ فِى ٱلدُّنْيَا ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌ
- (5:64) [listed for 88:9] وَقَالَتِ ٱلْيَهُودُ يَدُ ٱللَّهِ مَغْلُولَةٌ ۚ غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟ بِمَا قَالُوا۟ ۘ بَلْ يَدَاهُ مَبْسُوطَتَانِ يُنفِقُ كَيْفَ يَشَآءُ ۚ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۚ وَأَلْقَيْنَا بَيْنَهُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۚ كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ ۚ وَيَسْعَوْنَ فِى ٱلْأَرْضِ فَسَادًۭا ۚ وَٱللَّهُ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (6:113) [listed for 88:9] وَلِتَصْغَىٰٓ إِلَيْهِ أَفْـِٔدَةُ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ وَلِيَرْضَوْهُ وَلِيَقْتَرِفُوا۟ مَا هُم مُّقْتَرِفُونَ
- (9:38) [listed for 88:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ ۚ فَمَا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا قَلِيلٌ
- (9:58) [listed for 88:9] وَمِنْهُم مَّن يَلْمِزُكَ فِى ٱلصَّدَقَٰتِ فَإِنْ أُعْطُوا۟ مِنْهَا رَضُوا۟ وَإِن لَّمْ يُعْطَوْا۟ مِنْهَآ إِذَا هُمْ يَسْخَطُونَ
- (9:59) [listed for 88:9] وَلَوْ أَنَّهُمْ رَضُوا۟ مَآ ءَاتَىٰهُمُ ٱللَّهُ وَرَسُولُهُۥ وَقَالُوا۟ حَسْبُنَا ٱللَّهُ سَيُؤْتِينَا ٱللَّهُ مِن فَضْلِهِۦ وَرَسُولُهُۥٓ إِنَّآ إِلَى ٱللَّهِ رَٰغِبُونَ
- (9:62) [listed for 88:9] يَحْلِفُونَ بِٱللَّهِ لَكُمْ لِيُرْضُوكُمْ وَٱللَّهُ وَرَسُولُهُۥٓ أَحَقُّ أَن يُرْضُوهُ إِن كَانُوا۟ مُؤْمِنِينَ
- (9:83) [listed for 88:9] فَإِن رَّجَعَكَ ٱللَّهُ إِلَىٰ طَآئِفَةٍۢ مِّنْهُمْ فَٱسْتَـْٔذَنُوكَ لِلْخُرُوجِ فَقُل لَّن تَخْرُجُوا۟ مَعِىَ أَبَدًۭا وَلَن تُقَٰتِلُوا۟ مَعِىَ عَدُوًّا ۖ إِنَّكُمْ رَضِيتُم بِٱلْقُعُودِ أَوَّلَ مَرَّةٍۢ فَٱقْعُدُوا۟ مَعَ ٱلْخَٰلِفِينَ
- (9:87) [listed for 88:9] رَضُوا۟ بِأَن يَكُونُوا۟ مَعَ ٱلْخَوَالِفِ وَطُبِعَ عَلَىٰ قُلُوبِهِمْ فَهُمْ لَا يَفْقَهُونَ
- (9:93) [listed for 88:9] ۞ إِنَّمَا ٱلسَّبِيلُ عَلَى ٱلَّذِينَ يَسْتَـْٔذِنُونَكَ وَهُمْ أَغْنِيَآءُ ۚ رَضُوا۟ بِأَن يَكُونُوا۟ مَعَ ٱلْخَوَالِفِ وَطَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ فَهُمْ لَا يَعْلَمُونَ
- (9:100) [listed for 88:9] وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم بِإِحْسَٰنٍۢ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (19:6) [listed for 88:9] يَرِثُنِى وَيَرِثُ مِنْ ءَالِ يَعْقُوبَ ۖ وَٱجْعَلْهُ رَبِّ رَضِيًّۭا
- (19:55) [listed for 88:9] وَكَانَ يَأْمُرُ أَهْلَهُۥ بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ وَكَانَ عِندَ رَبِّهِۦ مَرْضِيًّۭا
- (20:15) [listed for 88:9] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (20:109) [listed for 88:9] يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَرَضِىَ لَهُۥ قَوْلًۭا
- (21:94) [listed for 88:9] [cited in ¶12] فَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا كُفْرَانَ لِسَعْيِهِۦ وَإِنَّا لَهُۥ كَٰتِبُونَ
- (22:59) [listed for 88:9] لَيُدْخِلَنَّهُم مُّدْخَلًۭا يَرْضَوْنَهُۥ ۗ وَإِنَّ ٱللَّهَ لَعَلِيمٌ حَلِيمٌۭ
- (28:20) [listed for 88:9] وَجَآءَ رَجُلٌۭ مِّنْ أَقْصَا ٱلْمَدِينَةِ يَسْعَىٰ قَالَ يَٰمُوسَىٰٓ إِنَّ ٱلْمَلَأَ يَأْتَمِرُونَ بِكَ لِيَقْتُلُوكَ فَٱخْرُجْ إِنِّى لَكَ مِنَ ٱلنَّٰصِحِينَ
- (33:51) [listed for 88:9] ۞ تُرْجِى مَن تَشَآءُ مِنْهُنَّ وَتُـْٔوِىٓ إِلَيْكَ مَن تَشَآءُ ۖ وَمَنِ ٱبْتَغَيْتَ مِمَّنْ عَزَلْتَ فَلَا جُنَاحَ عَلَيْكَ ۚ ذَٰلِكَ أَدْنَىٰٓ أَن تَقَرَّ أَعْيُنُهُنَّ وَلَا يَحْزَنَّ وَيَرْضَيْنَ بِمَآ ءَاتَيْتَهُنَّ كُلُّهُنَّ ۚ وَٱللَّهُ يَعْلَمُ مَا فِى قُلُوبِكُمْ ۚ وَكَانَ ٱللَّهُ عَلِيمًا حَلِيمًۭا
- (34:5) [listed for 88:9] وَٱلَّذِينَ سَعَوْ فِىٓ ءَايَٰتِنَا مُعَٰجِزِينَ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌۭ مِّن رِّجْزٍ أَلِيمٌۭ
- (36:20) [listed for 88:9] وَجَآءَ مِنْ أَقْصَا ٱلْمَدِينَةِ رَجُلٌۭ يَسْعَىٰ قَالَ يَٰقَوْمِ ٱتَّبِعُوا۟ ٱلْمُرْسَلِينَ
- (37:102) [listed for 88:9] فَلَمَّا بَلَغَ مَعَهُ ٱلسَّعْىَ قَالَ يَٰبُنَىَّ إِنِّىٓ أَرَىٰ فِى ٱلْمَنَامِ أَنِّىٓ أَذْبَحُكَ فَٱنظُرْ مَاذَا تَرَىٰ ۚ قَالَ يَٰٓأَبَتِ ٱفْعَلْ مَا تُؤْمَرُ ۖ سَتَجِدُنِىٓ إِن شَآءَ ٱللَّهُ مِنَ ٱلصَّٰبِرِينَ
- (48:18) [listed for 88:9] ۞ لَّقَدْ رَضِىَ ٱللَّهُ عَنِ ٱلْمُؤْمِنِينَ إِذْ يُبَايِعُونَكَ تَحْتَ ٱلشَّجَرَةِ فَعَلِمَ مَا فِى قُلُوبِهِمْ فَأَنزَلَ ٱلسَّكِينَةَ عَلَيْهِمْ وَأَثَٰبَهُمْ فَتْحًۭا قَرِيبًۭا
- (53:15) [listed for 88:9] عِندَهَا جَنَّةُ ٱلْمَأْوَىٰٓ
- (57:12) [listed for 88:9] يَوْمَ تَرَى ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ يَسْعَىٰ نُورُهُم بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِم بُشْرَىٰكُمُ ٱلْيَوْمَ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (57:20) [listed for 88:9] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (58:22) [listed for 88:9] لَّا تَجِدُ قَوْمًۭا يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ يُوَآدُّونَ مَنْ حَآدَّ ٱللَّهَ وَرَسُولَهُۥ وَلَوْ كَانُوٓا۟ ءَابَآءَهُمْ أَوْ أَبْنَآءَهُمْ أَوْ إِخْوَٰنَهُمْ أَوْ عَشِيرَتَهُمْ ۚ أُو۟لَٰٓئِكَ كَتَبَ فِى قُلُوبِهِمُ ٱلْإِيمَٰنَ وَأَيَّدَهُم بِرُوحٍۢ مِّنْهُ ۖ وَيُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ رَضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱللَّهِ ۚ أَلَآ إِنَّ حِزْبَ ٱللَّهِ هُمُ ٱلْمُفْلِحُونَ
- (59:8) [listed for 88:9] لِلْفُقَرَآءِ ٱلْمُهَٰجِرِينَ ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا وَيَنصُرُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ
- (62:9) [listed for 88:9] [cited in ¶8] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (66:1) [listed for 88:9] يَٰٓأَيُّهَا ٱلنَّبِىُّ لِمَ تُحَرِّمُ مَآ أَحَلَّ ٱللَّهُ لَكَ ۖ تَبْتَغِى مَرْضَاتَ أَزْوَٰجِكَ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (66:8) [listed for 88:9] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (69:21) [listed for 88:9] [cited in ¶23] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- (79:22) [listed for 88:9] ثُمَّ أَدْبَرَ يَسْعَىٰ
- (79:34) [listed for 88:9] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (80:8) [listed for 88:9] وَأَمَّا مَن جَآءَكَ يَسْعَىٰ
- (80:39) [listed for 88:9] ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ
- (92:20) [listed for 88:9] [cited in ¶18] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (92:21) [listed for 88:9] [cited in ¶18] وَلَسَوْفَ يَرْضَىٰ
- (93:5) [listed for 88:9] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (98:8) [listed for 88:9] [cited in ¶20] جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

## named by the passage's own list as strong for this ayah (5)

- (36:55) [listed for 88:9] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (41:32) [listed for 88:9] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (75:22) [listed for 88:9] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
- (75:24) [listed for 88:9] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ
- (77:43) [listed for 88:9] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ

## named by the passage's own list as medium for this ayah (6)

- (43:71) [listed for 88:9] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (52:19) [listed for 88:9] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (76:11) [listed for 88:9] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (83:22) [listed for 88:9] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:24) [listed for 88:9] [cited in ¶9] تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ
- (83:26) [listed for 88:9] [cited in ¶9] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ

## weak (this ayah's own list) (23)

- (2:120) [listed for 88:9] وَلَن تَرْضَىٰ عَنكَ ٱلْيَهُودُ وَلَا ٱلنَّصَٰرَىٰ حَتَّىٰ تَتَّبِعَ مِلَّتَهُمْ ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۗ وَلَئِنِ ٱتَّبَعْتَ أَهْوَآءَهُم بَعْدَ ٱلَّذِى جَآءَكَ مِنَ ٱلْعِلْمِ ۙ مَا لَكَ مِنَ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
- (2:232) [listed for 88:9] وَإِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَبَلَغْنَ أَجَلَهُنَّ فَلَا تَعْضُلُوهُنَّ أَن يَنكِحْنَ أَزْوَٰجَهُنَّ إِذَا تَرَٰضَوْا۟ بَيْنَهُم بِٱلْمَعْرُوفِ ۗ ذَٰلِكَ يُوعَظُ بِهِۦ مَن كَانَ مِنكُمْ يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۗ ذَٰلِكُمْ أَزْكَىٰ لَكُمْ وَأَطْهَرُ ۗ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (2:233) [listed for 88:9] ۞ وَٱلْوَٰلِدَٰتُ يُرْضِعْنَ أَوْلَٰدَهُنَّ حَوْلَيْنِ كَامِلَيْنِ ۖ لِمَنْ أَرَادَ أَن يُتِمَّ ٱلرَّضَاعَةَ ۚ وَعَلَى ٱلْمَوْلُودِ لَهُۥ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِٱلْمَعْرُوفِ ۚ لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا ۚ لَا تُضَآرَّ وَٰلِدَةٌۢ بِوَلَدِهَا وَلَا مَوْلُودٌۭ لَّهُۥ بِوَلَدِهِۦ ۚ وَعَلَى ٱلْوَارِثِ مِثْلُ ذَٰلِكَ ۗ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍۢ مِّنْهُمَا وَتَشَاوُرٍۢ فَلَا جُنَاحَ عَلَيْهِمَا ۗ وَإِنْ أَرَدتُّمْ أَن تَسْتَرْضِعُوٓا۟ أَوْلَٰدَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّآ ءَاتَيْتُم بِٱلْمَعْرُوفِ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (2:260) [listed for 88:9] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ أَرِنِى كَيْفَ تُحْىِ ٱلْمَوْتَىٰ ۖ قَالَ أَوَلَمْ تُؤْمِن ۖ قَالَ بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِى ۖ قَالَ فَخُذْ أَرْبَعَةًۭ مِّنَ ٱلطَّيْرِ فَصُرْهُنَّ إِلَيْكَ ثُمَّ ٱجْعَلْ عَلَىٰ كُلِّ جَبَلٍۢ مِّنْهُنَّ جُزْءًۭا ثُمَّ ٱدْعُهُنَّ يَأْتِينَكَ سَعْيًۭا ۚ وَٱعْلَمْ أَنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (3:174) [listed for 88:9] فَٱنقَلَبُوا۟ بِنِعْمَةٍۢ مِّنَ ٱللَّهِ وَفَضْلٍۢ لَّمْ يَمْسَسْهُمْ سُوٓءٌۭ وَٱتَّبَعُوا۟ رِضْوَٰنَ ٱللَّهِ ۗ وَٱللَّهُ ذُو فَضْلٍ عَظِيمٍ
- (4:24) [listed for 88:9] ۞ وَٱلْمُحْصَنَٰتُ مِنَ ٱلنِّسَآءِ إِلَّا مَا مَلَكَتْ أَيْمَٰنُكُمْ ۖ كِتَٰبَ ٱللَّهِ عَلَيْكُمْ ۚ وَأُحِلَّ لَكُم مَّا وَرَآءَ ذَٰلِكُمْ أَن تَبْتَغُوا۟ بِأَمْوَٰلِكُم مُّحْصِنِينَ غَيْرَ مُسَٰفِحِينَ ۚ فَمَا ٱسْتَمْتَعْتُم بِهِۦ مِنْهُنَّ فَـَٔاتُوهُنَّ أُجُورَهُنَّ فَرِيضَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا تَرَٰضَيْتُم بِهِۦ مِنۢ بَعْدِ ٱلْفَرِيضَةِ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
- (5:44) [listed for 88:9] إِنَّآ أَنزَلْنَا ٱلتَّوْرَىٰةَ فِيهَا هُدًۭى وَنُورٌۭ ۚ يَحْكُمُ بِهَا ٱلنَّبِيُّونَ ٱلَّذِينَ أَسْلَمُوا۟ لِلَّذِينَ هَادُوا۟ وَٱلرَّبَّٰنِيُّونَ وَٱلْأَحْبَارُ بِمَا ٱسْتُحْفِظُوا۟ مِن كِتَٰبِ ٱللَّهِ وَكَانُوا۟ عَلَيْهِ شُهَدَآءَ ۚ فَلَا تَخْشَوُا۟ ٱلنَّاسَ وَٱخْشَوْنِ وَلَا تَشْتَرُوا۟ بِـَٔايَٰتِى ثَمَنًۭا قَلِيلًۭا ۚ وَمَن لَّمْ يَحْكُم بِمَآ أَنزَلَ ٱللَّهُ فَأُو۟لَٰٓئِكَ هُمُ ٱلْكَٰفِرُونَ
- (16:99) [listed for 88:9] إِنَّهُۥ لَيْسَ لَهُۥ سُلْطَٰنٌ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (16:100) [listed for 88:9] إِنَّمَا سُلْطَٰنُهُۥ عَلَى ٱلَّذِينَ يَتَوَلَّوْنَهُۥ وَٱلَّذِينَ هُم بِهِۦ مُشْرِكُونَ
- (19:7) [listed for 88:9] يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا
- (19:57) [listed for 88:9] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- (19:65) [listed for 88:9] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:20) [listed for 88:9] فَأَلْقَىٰهَا فَإِذَا هِىَ حَيَّةٌۭ تَسْعَىٰ
- (20:66) [listed for 88:9] قَالَ بَلْ أَلْقُوا۟ ۖ فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ أَنَّهَا تَسْعَىٰ
- (21:82) [listed for 88:9] وَمِنَ ٱلشَّيَٰطِينِ مَن يَغُوصُونَ لَهُۥ وَيَعْمَلُونَ عَمَلًۭا دُونَ ذَٰلِكَ ۖ وَكُنَّا لَهُمْ حَٰفِظِينَ
- (34:38) [listed for 88:9] وَٱلَّذِينَ يَسْعَوْنَ فِىٓ ءَايَٰتِنَا مُعَٰجِزِينَ أُو۟لَٰٓئِكَ فِى ٱلْعَذَابِ مُحْضَرُونَ
- (45:19) [listed for 88:9] إِنَّهُمْ لَن يُغْنُوا۟ عَنكَ مِنَ ٱللَّهِ شَيْـًۭٔا ۚ وَإِنَّ ٱلظَّٰلِمِينَ بَعْضُهُمْ أَوْلِيَآءُ بَعْضٍۢ ۖ وَٱللَّهُ وَلِىُّ ٱلْمُتَّقِينَ
- (56:2) [listed for 88:9] لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ
- (56:3) [listed for 88:9] خَافِضَةٌۭ رَّافِعَةٌ
- (69:27) [listed for 88:9] يَٰلَيْتَهَا كَانَتِ ٱلْقَاضِيَةَ
- (77:9) [listed for 88:9] وَإِذَا ٱلسَّمَآءُ فُرِجَتْ
- (80:14) [listed for 88:9] مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ
- (92:16) [listed for 88:9] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ

## named by the passage's own list as weak for this ayah (2)

- (80:38) [listed for 88:9] وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ
- (80:41) [listed for 88:9] تَرْهَقُهَا قَتَرَةٌ

## neighbours: within two ayat of a passage the commentary cites (65)

- (2:202) [next to 2:204] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
- (2:203) [next to 2:204] ۞ وَٱذْكُرُوا۟ ٱللَّهَ فِىٓ أَيَّامٍۢ مَّعْدُودَٰتٍۢ ۚ فَمَن تَعَجَّلَ فِى يَوْمَيْنِ فَلَآ إِثْمَ عَلَيْهِ وَمَن تَأَخَّرَ فَلَآ إِثْمَ عَلَيْهِ ۚ لِمَنِ ٱتَّقَىٰ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّكُمْ إِلَيْهِ تُحْشَرُونَ
- (2:206) [next to 2:204] وَإِذَا قِيلَ لَهُ ٱتَّقِ ٱللَّهَ أَخَذَتْهُ ٱلْعِزَّةُ بِٱلْإِثْمِ ۚ فَحَسْبُهُۥ جَهَنَّمُ ۚ وَلَبِئْسَ ٱلْمِهَادُ
- (9:70) [next to 9:72] أَلَمْ يَأْتِهِمْ نَبَأُ ٱلَّذِينَ مِن قَبْلِهِمْ قَوْمِ نُوحٍۢ وَعَادٍۢ وَثَمُودَ وَقَوْمِ إِبْرَٰهِيمَ وَأَصْحَٰبِ مَدْيَنَ وَٱلْمُؤْتَفِكَٰتِ ۚ أَتَتْهُمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ ۖ فَمَا كَانَ ٱللَّهُ لِيَظْلِمَهُمْ وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (9:71) [next to 9:72] وَٱلْمُؤْمِنُونَ وَٱلْمُؤْمِنَٰتُ بَعْضُهُمْ أَوْلِيَآءُ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَيُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَيُطِيعُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ سَيَرْحَمُهُمُ ٱللَّهُ ۗ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (9:73) [next to 9:72] يَٰٓأَيُّهَا ٱلنَّبِىُّ جَٰهِدِ ٱلْكُفَّارَ وَٱلْمُنَٰفِقِينَ وَٱغْلُظْ عَلَيْهِمْ ۚ وَمَأْوَىٰهُمْ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (9:74) [next to 9:72] يَحْلِفُونَ بِٱللَّهِ مَا قَالُوا۟ وَلَقَدْ قَالُوا۟ كَلِمَةَ ٱلْكُفْرِ وَكَفَرُوا۟ بَعْدَ إِسْلَٰمِهِمْ وَهَمُّوا۟ بِمَا لَمْ يَنَالُوا۟ ۚ وَمَا نَقَمُوٓا۟ إِلَّآ أَنْ أَغْنَىٰهُمُ ٱللَّهُ وَرَسُولُهُۥ مِن فَضْلِهِۦ ۚ فَإِن يَتُوبُوا۟ يَكُ خَيْرًۭا لَّهُمْ ۖ وَإِن يَتَوَلَّوْا۟ يُعَذِّبْهُمُ ٱللَّهُ عَذَابًا أَلِيمًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَمَا لَهُمْ فِى ٱلْأَرْضِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (17:16) [next to 17:18] وَإِذَآ أَرَدْنَآ أَن نُّهْلِكَ قَرْيَةً أَمَرْنَا مُتْرَفِيهَا فَفَسَقُوا۟ فِيهَا فَحَقَّ عَلَيْهَا ٱلْقَوْلُ فَدَمَّرْنَٰهَا تَدْمِيرًۭا
- (17:17) [next to 17:18] وَكَمْ أَهْلَكْنَا مِنَ ٱلْقُرُونِ مِنۢ بَعْدِ نُوحٍۢ ۗ وَكَفَىٰ بِرَبِّكَ بِذُنُوبِ عِبَادِهِۦ خَبِيرًۢا بَصِيرًۭا
- (17:20) [next to 17:18] كُلًّۭا نُّمِدُّ هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ مِنْ عَطَآءِ رَبِّكَ ۚ وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا
- (17:21) [next to 17:19] ٱنظُرْ كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۚ وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًۭا
- (18:102) [next to 18:104] أَفَحَسِبَ ٱلَّذِينَ كَفَرُوٓا۟ أَن يَتَّخِذُوا۟ عِبَادِى مِن دُونِىٓ أَوْلِيَآءَ ۚ إِنَّآ أَعْتَدْنَا جَهَنَّمَ لِلْكَٰفِرِينَ نُزُلًۭا
- (18:103) [next to 18:104] قُلْ هَلْ نُنَبِّئُكُم بِٱلْأَخْسَرِينَ أَعْمَٰلًا
- (18:105) [next to 18:104] أُو۟لَٰٓئِكَ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ وَلِقَآئِهِۦ فَحَبِطَتْ أَعْمَٰلُهُمْ فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا
- (18:106) [next to 18:104] ذَٰلِكَ جَزَآؤُهُمْ جَهَنَّمُ بِمَا كَفَرُوا۟ وَٱتَّخَذُوٓا۟ ءَايَٰتِى وَرُسُلِى هُزُوًا
- (21:91) [next to 21:93] وَٱلَّتِىٓ أَحْصَنَتْ فَرْجَهَا فَنَفَخْنَا فِيهَا مِن رُّوحِنَا وَجَعَلْنَٰهَا وَٱبْنَهَآ ءَايَةًۭ لِّلْعَٰلَمِينَ
- (21:92) [next to 21:93] إِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةًۭ وَٰحِدَةًۭ وَأَنَا۠ رَبُّكُمْ فَٱعْبُدُونِ
- (21:95) [next to 21:93] وَحَرَٰمٌ عَلَىٰ قَرْيَةٍ أَهْلَكْنَٰهَآ أَنَّهُمْ لَا يَرْجِعُونَ
- (21:96) [next to 21:94] حَتَّىٰٓ إِذَا فُتِحَتْ يَأْجُوجُ وَمَأْجُوجُ وَهُم مِّن كُلِّ حَدَبٍۢ يَنسِلُونَ
- (24:31) [next to 24:33] وَقُل لِّلْمُؤْمِنَٰتِ يَغْضُضْنَ مِنْ أَبْصَٰرِهِنَّ وَيَحْفَظْنَ فُرُوجَهُنَّ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا مَا ظَهَرَ مِنْهَا ۖ وَلْيَضْرِبْنَ بِخُمُرِهِنَّ عَلَىٰ جُيُوبِهِنَّ ۖ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا لِبُعُولَتِهِنَّ أَوْ ءَابَآئِهِنَّ أَوْ ءَابَآءِ بُعُولَتِهِنَّ أَوْ أَبْنَآئِهِنَّ أَوْ أَبْنَآءِ بُعُولَتِهِنَّ أَوْ إِخْوَٰنِهِنَّ أَوْ بَنِىٓ إِخْوَٰنِهِنَّ أَوْ بَنِىٓ أَخَوَٰتِهِنَّ أَوْ نِسَآئِهِنَّ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُنَّ أَوِ ٱلتَّٰبِعِينَ غَيْرِ أُو۟لِى ٱلْإِرْبَةِ مِنَ ٱلرِّجَالِ أَوِ ٱلطِّفْلِ ٱلَّذِينَ لَمْ يَظْهَرُوا۟ عَلَىٰ عَوْرَٰتِ ٱلنِّسَآءِ ۖ وَلَا يَضْرِبْنَ بِأَرْجُلِهِنَّ لِيُعْلَمَ مَا يُخْفِينَ مِن زِينَتِهِنَّ ۚ وَتُوبُوٓا۟ إِلَى ٱللَّهِ جَمِيعًا أَيُّهَ ٱلْمُؤْمِنُونَ لَعَلَّكُمْ تُفْلِحُونَ
- (24:32) [next to 24:33] وَأَنكِحُوا۟ ٱلْأَيَٰمَىٰ مِنكُمْ وَٱلصَّٰلِحِينَ مِنْ عِبَادِكُمْ وَإِمَآئِكُمْ ۚ إِن يَكُونُوا۟ فُقَرَآءَ يُغْنِهِمُ ٱللَّهُ مِن فَضْلِهِۦ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (24:34) [next to 24:33] وَلَقَدْ أَنزَلْنَآ إِلَيْكُمْ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ وَمَثَلًۭا مِّنَ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُمْ وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
- (24:35) [next to 24:33] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (53:35) [next to 53:37] أَعِندَهُۥ عِلْمُ ٱلْغَيْبِ فَهُوَ يَرَىٰٓ
- (53:36) [next to 53:37] أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ
- (53:38) [next to 53:37] أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ
- (53:41) [next to 53:39] ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ
- (53:42) [next to 53:40] وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ
- (62:7) [next to 62:9] وَلَا يَتَمَنَّوْنَهُۥٓ أَبَدًۢا بِمَا قَدَّمَتْ أَيْدِيهِمْ ۚ وَٱللَّهُ عَلِيمٌۢ بِٱلظَّٰلِمِينَ
- (62:8) [next to 62:9] قُلْ إِنَّ ٱلْمَوْتَ ٱلَّذِى تَفِرُّونَ مِنْهُ فَإِنَّهُۥ مُلَٰقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (62:11) [next to 62:9] وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ
- (69:19) [next to 69:21] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (69:20) [next to 69:21] إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ
- (69:22) [next to 69:21] فِى جَنَّةٍ عَالِيَةٍۢ
- (69:23) [next to 69:21] قُطُوفُهَا دَانِيَةٌۭ
- (76:19) [next to 76:21] ۞ وَيَطُوفُ عَلَيْهِمْ وِلْدَٰنٌۭ مُّخَلَّدُونَ إِذَا رَأَيْتَهُمْ حَسِبْتَهُمْ لُؤْلُؤًۭا مَّنثُورًۭا
- (76:20) [next to 76:21] وَإِذَا رَأَيْتَ ثَمَّ رَأَيْتَ نَعِيمًۭا وَمُلْكًۭا كَبِيرًا
- (76:23) [next to 76:21] إِنَّا نَحْنُ نَزَّلْنَا عَلَيْكَ ٱلْقُرْءَانَ تَنزِيلًۭا
- (76:24) [next to 76:22] فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًۭا
- (83:23) [next to 83:24] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ
- (83:25) [next to 83:24] يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ
- (83:27) [next to 83:26] وَمِزَاجُهُۥ مِن تَسْنِيمٍ
- (83:28) [next to 83:26] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
- (89:22) [next to 89:24] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- (89:23) [next to 89:24] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (89:25) [next to 89:24] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- (89:26) [next to 89:24] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- (89:29) [next to 89:27] فَٱدْخُلِى فِى عِبَٰدِى
- (89:30) [next to 89:28] وَٱدْخُلِى جَنَّتِى
- (90:9) [next to 90:11] وَلِسَانًۭا وَشَفَتَيْنِ
- (90:10) [next to 90:11] وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- (90:12) [next to 90:11] وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- (90:14) [next to 90:13] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- (90:15) [next to 90:13] يَتِيمًۭا ذَا مَقْرَبَةٍ
- (92:2) [next to 92:4] وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- (92:3) [next to 92:4] وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- (92:5) [next to 92:4] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (92:6) [next to 92:4] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:9) [next to 92:11] وَكَذَّبَ بِٱلْحُسْنَىٰ
- (92:10) [next to 92:11] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:12) [next to 92:11] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:13) [next to 92:11] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:17) [next to 92:18] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- (98:6) [next to 98:8] إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- (98:7) [next to 98:8] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ

