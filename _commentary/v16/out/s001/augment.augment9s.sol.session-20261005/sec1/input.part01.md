Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 1 of 14 ("Çiğnenmiş yol: önden giden kılavuz, yolun ortası, nişanlar ve yolu bulamayan"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 1 (prose paragraphs numbered) =====
[¶1] Fâtiha'nın altıncı ayeti bir yol isteğidir: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-müstakîm, gloss:bizi dosdoğru yola ilet, source:1:6}. Arapçada yol, ayakların yaptığı bir şeydir. Çok kişinin yürüdüğü toprak düzlenir, sertliği kırılır ve üstünde yürüyene boyun eğer. Buna {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-mu'abbed ve hüve'l-meslûku'l-müzellel, gloss:çiğnenmiş yol, yani üzerinden geçilmiş ve uysallaştırılmış yol, source:"ع ب د,B005"} denir. Bu kelime, beşinci ayetteki {ar:نَعْبُدُ, tr:na'büdü, gloss:kulluk ederiz, source:1:5} fiiliyle aynı ailedendir. Bir kelimenin ailesinden gelen böyle görüntüler, kelimenin kendi ayetindeki anlamının yerine geçmez, o anlamın yanında duyulur. "Na'büdü" ayette "sana kulluk ederiz" demektir. Çiğnenmiş yol bu anlamın yanında, kulluğun bir zeminde bıraktığı izi gösterir: Çok yürünmüş, düzlenmiş ve artık yürüyeni zorlamayan bir yüzey.

[¶2] Yolu göstermek ve önden yürümek hidayettir. {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytühü't-tarîka ve'l-beyte hidâyeten, gloss:ona yolu ve evi gösterdim, tanıttım, source:"ه د ي,B001"}. Bu cümlede hidayet iki şeyi birden gösterir: yolu ve yolun vardığı evi. Bir yolu bilmek, nereye çıktığını bilmektir. Kılavuza da önden yürüdüğü için "hâdî" denir: {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlü yüsemmâ hâdiyen li-tekaddümihî, gloss:kılavuza önde gittiği için hâdî denir, source:"ه د ي,B003"}. Asaya da aynı ad verilir, çünkü onu tutan elin önünden gider: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemühû, gloss:asa da hâdîdir, çünkü sahibinin önünden gider, source:"ه د ي,B003"}. Üçüncü bir kullanım ise tutulan yolda sapmadan devam etmeyi anlatır: {ar:خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه, tr:huz fî hidyetike, gloss:tuttuğun yolda devam et, ondan ayrılma, source:"ه د ي,B002"}. Böylece "ihdinâ" isteği üç hareketi birlikte taşır: Bize yolu ve evi göster, önümüzden yürü, tuttuğumuz yolda bizi sapmadan götür.

[¶3] Yolun kendisi sırattır ve sıratın tarifinde surenin sıfatı zaten bulunur: {ar:الصراط: الطريق المستقيم, tr:es-sırât: et-tarîku'l-müstakîm, gloss:sırat dosdoğru yoldur, source:"ص ر ط,B001"}. Kelime {ar:الصراط والسراط والزراط: الطريق, tr:es-sırâtu ve's-sirâtu ve'z-zırât, gloss:sırat, sirat ve zırat yol demektir, source:"ص ر ط,B001"} diye üç sesle de söylenir. "Müstakîm" düz bir hat üzerinde giden yoldur: {ar:الاستقامة في الطريق الذي يكون على خط مستو, tr:el-istikâmetü fi't-tarîki'llezî yekûnü alâ hattın müstevin, gloss:istikamet, düz bir hat üzerinde uzanan yolda olur, source:"ق و م,B008"}. Bu, bükülmemiş bir mızrak sapının düzlüğüdür: {ar:رمح قويم, tr:rumhun kavîm, gloss:dümdüz mızrak, source:"ق و م,B008"}.

[¶4] Düz bir meal "doğru yol" der ve orada durur. Görüntü ise yolun ayakla yapıldığını gösterir: İstenen şey bir doğruluk bilgisi değildir. İstenen, başkalarının daha önce yürüyüp düzlediği bir yolda, önden giden birinin ardından yürümektir. Yedinci ayet bunu açıkça söyler, yol bir topluluğun yoludur: {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:sırâta'llezîne en'amte aleyhim, gloss:kendilerine nimet verdiklerinin yolu, source:1:7}.

[¶5] Sure baştan sona okunduğunda her ayet bu yola bir parça ekler. İkinci ayetteki {ar:ٱلْعَٰلَمِينَ, tr:el-âlemîn, gloss:âlemler, source:1:2} kelimesinin ailesinde yolcunun okuduğu iz ve dağ vardır: {ar:المعلم الأثر يستدل به على الطريق, tr:el-ma'lemü'l-eseru yüstedellü bihî ale't-tarîk, gloss:ma'lem, yolu bulmak için ona bakılan izdir, source:"ع ل م,B002"} ve {ar:العلم الجبل الطويل والجميع الأعلام, tr:el-alemü'l-cebelü't-tavîl, gloss:alem uzun dağdır, çoğulu a'lâmdır, source:"ع ل م,B002"}. "Âlemlerin Rabbi" ifadesi kendi anlamını korur. Yanında ise yolcunun yön bulmak için baktığı nişanların hepsinin sahibi duyulur. Dördüncü ayetteki {ar:مَٰلِكِ, tr:mâliki, gloss:sahibi, source:1:4} kelimesinin ailesinde yolun ortası vardır: {ar:الزم ملك الطريق أي وسطه, tr:elzim milke't-tarîk, gloss:yolun ortasından ayrılma, source:"م ل ك,B006"}. Aynı ayetteki {ar:ٱلدِّينِ, tr:ed-dîn, gloss:din, hesap ve karşılık, source:1:4} kelimesinde ise insanın sürdürdüğü alışkanlık duyulur: {ar:الدين بالكسر العادة والشأن, tr:ed-dînu bi'l-kesri el-âdetü ve'ş-şe'n, gloss:esreli dîn adet ve hal demektir, source:"د ي ن,B005"}. Bu ikisi, yolu yürünen bir yol yapan iki şeydir: ortada kalmak ve yürüyüşü her gün sürdürmek.

[¶6] Beşinci ayet yolun zeminini, çiğnenmiş toprağı getirir. Aynı ailede bunun tersi de vardır: {ar:العباديد الفرق من الناس الذاهبون في كل وجه, tr:el-abâbîdü'l-firaku mine'n-nâs, gloss:abâbîd, her yöne dağılıp giden insan bölükleridir, source:"ع ب د,B010"}. Altıncı ayet asıl isteği dile getirir. Ayetteki {ar:ٱلْمُسْتَقِيمَ, tr:el-müstakîm, gloss:dosdoğru, source:1:6} kelimesinin kökü, bir adamın taraftarlarına ve aşiretine de ad verir: {ar:قوم كل رجل شيعته وعشيرته, tr:kavmü kulli raculin şî'atühû ve aşîretüh, gloss:bir adamın kavmi, onun taraftarları ve aşiretidir, source:"ق و م,B001"}. Bu, yedinci ayetin "onların yolu" sözüne hazırlık yapar. Yedinci ayetteki {ar:أَنْعَمْتَ, tr:en'amte, gloss:nimet verdin, source:1:7} kelimesinin ailesinde ana yol vardır: {ar:وابن النعامة عرق الرجل ومحجة الطريق, tr:ve ibnü'n-neâme... ve mehaccetü't-tarîk, gloss:ibnü'n-neâme ayrıca yolun çiğnenmiş ana izidir, source:"ن ع م,B007"}. Topluluğun dağılması da aynı ailededir: {ar:شالت نعامتهم إذا تفرقوا, tr:şâlet neâmetühüm, gloss:dağılıp gittiler, source:"ن ع م,B008"}. Ayetin son kelimesi {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:sapanlar, yolunu yitirenler, source:1:7} bu yolun tersidir: {ar:ضل في الأرض إذا لم يهتد للسبيل, tr:dalle fi'l-ard, gloss:yeryüzünde yolu bulamadı, source:"ض ل ل,B001"}, {ar:كل جائر عن القصد ضال, tr:küllü câirin ani'l-kasdi dâll, gloss:doğru hattan yana sapan herkes dâldır, source:"ض ل ل,B001"}. Eve varamamak da bu kelimeyle söylenir: {ar:ضللت المسجد والدار إذا لم تهتد لهما, tr:dalaltü'l-mescide ve'd-dâr, gloss:mescidi ve evi bulamadım, source:"ض ل ل,B003"}. Bu ifade, hidayet tanımındaki "yolu ve evi gösterdim" cümlesini tersine çevirir. İki kelimenin birbirinin karşıtı olduğu da açıkça söylenir: {ar:الإضلال في كلام العرب ضد الهداية والإرشاد, tr:el-idlâlü fî kelâmi'l-Arab, gloss:Arap dilinde saptırmak, hidayet edip doğru yolu göstermenin zıddıdır, source:"ض ل ل,B001"}. Sure "ihdinâ" ile başlayan isteği "dâllîn" ile bitirir. Böylece istek, yolun bir ucundan öbür ucuna kadar uzanır.

[¶7] Kur'an bu yolu birçok yerde sahneler. Rab müminlere öğütlerini sıralar ve onları bir yolla birçok yolun karşısına koyar: {ar:وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ, tr:ve enne hâzâ sırâtî müstakîmen fettebi'ûh, gloss:bu benim dosdoğru yolumdur, ona uyun, source:6:153}, {ar:وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve lâ tettebi'u's-sübüle fe-teferraka biküm an sebîlih, gloss:başka yollara uymayın, sizi onun yolundan ayırıp dağıtır, source:6:153}. "Abâbîd"in ve "şâlet neâmetühüm"ün anlattığı dağılma burada yollar üzerinden olur. Peygambere şöyle demesi emredilir: {ar:قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا, tr:kul innenî hedânî rabbî ilâ sırâtın müstakîm, dînen kıyemen, gloss:de ki: Rabbim beni dosdoğru bir yola iletti, dimdik bir dine, source:6:161}. Yol, din ve aynı kökten "kıyem" tek cümlede bir araya gelir. Musa yolda olan bir adamdır ve Medyen'e yöneldiğinde şunu söyler: {ar:عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ, tr:asâ rabbî en yehdiyenî sevâe's-sebîl, gloss:umarım Rabbim beni yolun ortasına iletir, source:28:22}. "Sevâe's-sebîl", "milkü't-tarîk"in, yani yolun ortasının Kur'an'daki karşılığıdır. Allah yeryüzüne dağlar, ırmaklar ve yollar koyduğunu anlatır: {ar:وَسُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ, tr:ve sübülen lealleküm tehtedûn, gloss:yolunuzu bulasınız diye yollar, source:16:15}, {ar:وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ, tr:ve alâmât, ve bi'n-necmi hüm yehtedûn, gloss:ve nişanlar; yıldızla da yollarını bulurlar, source:16:16}. "Alâmât" kelimesi "âlemîn" ile aynı köktendir. Nişan ve yön bulmak burada bir arada durur.

[¶8] Yolunu yitiren yolcu da sahnelenir. Peygambere şunu söylemesi emredilir: {ar:كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا, tr:kellezi'stehvethü'ş-şeyâtînü fi'l-ardı hayrâne lehû ashâbün yed'ûnehû ile'l-hüde'tinâ, gloss:şeytanların yeryüzünde aklını çelip şaşkın bıraktığı, arkadaşlarının ise "bize gel" diye doğru yola çağırdığı kimse gibi, source:6:71}. Bu, "dalle fi'l-ard" sahnesinin ta kendisidir. Adam açık arazide şaşkın kalmıştır, bir topluluk ise yolun üzerinde durup onu çağırır. Allah Peygambere şöyle der: {ar:وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ, tr:ve vecedeke dâllen fe-hedâ, gloss:seni yolunu arar buldu da yola iletti, source:93:7}. İblis Allah'a karşı yemin ettiğinde bu yolun üzerinde pusu kurar: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ak'udenne lehüm sırâtake'l-müstakîm, gloss:senin dosdoğru yolunun üzerinde onlar için oturup bekleyeceğim, source:7:16}. Ardından dört yönü sayar: {ar:مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:min beyni eydîhim ve min halfihim ve an eymânihim ve an şemâilihim, gloss:önlerinden, arkalarından, sağlarından ve sollarından, source:7:17}. Yol düz bir hat olduğu için saldırı onun dört yanından gelir. Ayırma gününde suçlulara {ar:وَٱمْتَٰزُوا۟ ٱلْيَوْمَ أَيُّهَا ٱلْمُجْرِمُونَ, tr:vemtâzu'l-yevme eyyühe'l-mücrimûn, gloss:ey suçlular, bugün ayrılın, source:36:59} denir. Ardından Allah Âdemoğullarına seslenir: {ar:وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:ve eni'budûnî, hâzâ sırâtun müstakîm, gloss:bana kulluk edin; işte bu dosdoğru yoldur, source:36:61}, {ar:وَلَقَدْ أَضَلَّ مِنكُمْ جِبِلًّۭا كَثِيرًا, tr:ve le-kad edalle minküm cibillen kesîrâ, gloss:o, sizden pek çok kalabalığı yoldan çıkardı, source:36:62}. Kulluk, yol ve sapma, surenin beşinci ayetinden yedinci ayetine giden sırayla burada da yan yanadır. İsa da aynı cümleyi kurar: {ar:إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:innellâhe rabbî ve rabbüküm fa'budûh, hâzâ sırâtun müstakîm, gloss:Allah benim de Rabbim sizin de Rabbinizdir; O'na kulluk edin, işte bu dosdoğru yoldur, source:3:51}. Aynı söz iki başka yerde de tekrarlanır {source:19:36} {source:43:64}. Kulluk burada yolun ta kendisidir. Yolun tersine dönmüş hali ise mahşerde görülür: {ar:فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ, tr:fehdûhüm ilâ sırâti'l-cahîm, gloss:onları cehennemin yoluna iletin, source:37:23}. Hidayet ve sırat aynı kelimelerdir, fakat bu kez varılan yer başkadır.

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: و ل ه members of ٱللَّهِ (road, womb, herd, well, passing) - alternative derivation, root identity not established
- not developed: hadith items in womb, herd and leaning chains - outside the Quran
- not developed: ن ع م B012 walking on soles - too remote
- not developed: ع و ن B005 strength matching age - adds nothing
- not developed: ق و م B012 ayn reading of qāma - recorded as wrong
- not developed: Debt and scale chain - merged into Day of reckoning
- not developed: Well-head chain - merged into Rain as water
- memory: dīn (kasra) vs dayn (fatha) are distinct words of one root
- memory: maghḍūb is a passive participle naming no agent; anʿamta names "you" as agent
- memory: fronted iyyāka marks exclusivity ("only you")
- memory: qāma also means "stopped dead" (beast), as well as "stood up"

===== passages from the discovery list (216) =====
## strong (123)

- (2:38) [luna: strong (missing-ayat turn); terra: medium; basis: root+scene+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: luna: The verse says that those who follow God's guidance need not fear; it specifically joins following (اتبَعَ) with guidance, the section's image of staying behind a guide on the road. | terra: After the descent, whoever follows God's guidance need not fear or grieve. It adds the ongoing act of following to the section's request to be led.
- (2:108) [luna: strong; terra: contrast; basis: contrast+root+scene] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
  Unverified discovery rationale: luna: As the prompt's example indicates, ضل سواء السبيل directly makes straying a loss of the road's middle; the context warns against exchanging faith for disbelief. | terra: It says the person who exchanges faith for disbelief has gone astray from sawāʾ al-sabīl. The exact middle-of-the-road expression reverses Moses' request in 28:22.
- (2:142) [luna: strong; terra: strong; basis: root+scene+theme] ۞ سَيَقُولُ ٱلسُّفَهَآءُ مِنَ ٱلنَّاسِ مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: In the dispute over the direction of prayer, the verse says God guides whom He wills to a straight path; a changed direction makes the route's divine guidance concrete. | terra: God guides whom He wills to a straight path; its exact path-and-guidance formulation carries the Fatiha petition into the change of qibla.
- (2:198) [luna: strong (missing-ayat turn); basis: root+scene+theme] لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ ۚ فَإِذَآ أَفَضْتُم مِّنْ عَرَفَٰتٍۢ فَٱذْكُرُوا۟ ٱللَّهَ عِندَ ٱلْمَشْعَرِ ٱلْحَرَامِ ۖ وَٱذْكُرُوهُ كَمَا هَدَىٰكُمْ وَإِن كُنتُم مِّن قَبْلِهِۦ لَمِنَ ٱلضَّآلِّينَ
  Unverified discovery rationale: luna: During the Hajj route from Arafat to the sacred landmark, people are told to remember how God guided them, though before that they were among the lost; this ties finding one's way to a named destination.
- (2:213) [luna: strong; terra: strong; basis: root+scene+theme] كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ فَبَعَثَ ٱللَّهُ ٱلنَّبِيِّۦنَ مُبَشِّرِينَ وَمُنذِرِينَ وَأَنزَلَ مَعَهُمُ ٱلْكِتَٰبَ بِٱلْحَقِّ لِيَحْكُمَ بَيْنَ ٱلنَّاسِ فِيمَا ٱخْتَلَفُوا۟ فِيهِ ۚ وَمَا ٱخْتَلَفَ فِيهِ إِلَّا ٱلَّذِينَ أُوتُوهُ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ بَغْيًۢا بَيْنَهُمْ ۖ فَهَدَى ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ لِمَا ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
  Unverified discovery rationale: luna: After people differ, God guides believers to the truth by His permission and guides whom He wills to a straight path; it links the path with resolving division. | terra: After human beings become divided, God guides believers to the truth they dispute by His permission, to a straight path. It places a single guided route after communal division.
- (3:8) [luna: strong; basis: contrast+root+theme] رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ ٱلْوَهَّابُ
  Unverified discovery rationale: luna: The prayer asks God not to let hearts deviate after guidance; it parallels the section's request to stay straight on a path already shown.
- (3:51) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶8] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
  Unverified discovery rationale: luna: The section notes that worship and the walked road remain distinct senses in one word family; this verse explicitly places worship of God beside “this is a straight path.” | terra: Jesus joins worship of the one Lord to the declaration that this is a straight path, making na'budu's worship the way itself.
- (3:101) [luna: strong; terra: strong; basis: root+scene+theme] وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ ءَايَٰتُ ٱللَّهِ وَفِيكُمْ رَسُولُهُۥ ۗ وَمَن يَعْتَصِم بِٱللَّهِ فَقَدْ هُدِىَ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: The verse joins holding fast to God with being guided إلى صراط مستقيم, linking continued adherence to arrival on the straight path. | terra: Holding fast to God is followed by being guided to a straight path, joining a sustaining grip to the continued route requested in the section.
- (3:103) [luna: strong; terra: medium; basis: contrast+scene+theme] وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟ ۚ وَٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ إِذْ كُنتُمْ أَعْدَآءًۭ فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًۭا وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: luna: The community is commanded to hold together by God's rope and not disperse; this makes the section's contrast between a common road and people scattering in every direction concrete. | terra: The community is told to hold God's rope all together and not become divided. Its shared holding gives a communal counterpoint to the section's people scattering in every direction.
- (4:44) [luna: strong; basis: contrast+root+scene] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يَشْتَرُونَ ٱلضَّلَٰلَةَ وَيُرِيدُونَ أَن تَضِلُّوا۟ ٱلسَّبِيلَ
