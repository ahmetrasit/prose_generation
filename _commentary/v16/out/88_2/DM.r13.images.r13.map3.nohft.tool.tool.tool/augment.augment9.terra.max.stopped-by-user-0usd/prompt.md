Work only from this message and the lookup command it describes: read no file and run no other command.

Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:2; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_2.reading.tr.md (prose paragraphs numbered) =====
## O gün ve yüzler

[¶1] Ayet üç kelimeden ibarettir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğilmiş ve çökmüştür, source:88:2}. Ortadaki kelime "o gün" demektir ve kendi başına bir gün adı vermez, geriye işaret eder. Hangi günün kastedildiğini ilk ayet söylemiştir: haberi sorulan Gâşiye'nin, yani her şeyi üstünden örten olayın günü {source:88:1}. Örtünün ilk olarak yüzlere inmesi surenin kendi sahnesidir ve ilk ayetin kelimesiyle kurulur; burada yüzün kendisine bakılacak.

[¶2] Yüzler belirlilik takısı olmadan söylenir: bütün yüzler değil, birtakım yüzler. Sekizinci ayet aynı iki kelimeyle ikinci bir takımı açar: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşacık ve mutludur, source:88:8}. Yalnızca bir sıfatta ayrılan bu iki yüzün karşılaşmasını sekizinci ayetin kelimesi taşır. İkinci ayetin yüzleri ise şimdilik yalnızdır ve ardından gelen her sıfat, her fiil onlara uyar: çalışıp didinen, bitkin düşen, kızgın ateşe giren, kaynar bir pınardan içirilen hep bu yüzlerdir. Altıncı ayette dil birden değişir: {ar:لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ, tr:leyse lehum taâmun illâ min darî', gloss:onların darîden başka bir yiyeceği yoktur, source:88:6}. Buradaki "onlar" insanlar için kullanılan çoğul zamirdir. Metnin kendisi, yüzün insanın yerine geçtiğini böylece gösterir. Araplar da kişinin kendisini yüzüyle anarlardı: {ar:ربما عبر عن الذات بالوجه, tr:rubbemâ ubbira ani'z-zâti bi'l-vech, gloss:kimi zaman kişinin kendisi yüz diye anılır, source:"و ج ه,B004"}.

[¶3] Arapça insanı burada eliyle, ayağıyla ya da kalbiyle değil yüzüyle anar. Yüz, bir şeyin karşıya dönük yanıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. İnsan bir başkasıyla yüzü aracılığıyla karşılaşır ve yüzleşmenin adı da buradan gelir: {ar:واجهت فلانا جعلت وجهي تلقاء وجهه, tr:vâcehtü fülânen cealtü vechî tilkâe vechih, gloss:falanla yüzleştim yani yüzümü onun yüzünün karşısına koydum, source:"و ج ه,B003"}. Bu yüzlerin kimin karşısına çıktığını sure sonunda söyler: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bizedir, source:88:25}. Yüz öne dönük olduğu için gelen her şeyi ilk karşılayan yerdir. Kur'an bunun en çıplak hâlini bir soruyla gösterir. Allah sözün en güzelini birbirine benzeyen, tekrar tekrar okunan bir kitap olarak indirdiğini ve onunla dilediğini doğru yola ilettiğini söyledikten {source:39:23} sonra sorar: {ar:أَفَمَن يَتَّقِى بِوَجْهِهِۦ سُوٓءَ ٱلْعَذَابِ يَوْمَ ٱلْقِيَٰمَةِ, tr:e-fe-men yettekî bi-vechihî sûe'l-azâbi yevme'l-kıyâme, gloss:kıyamet günü azabın kötüsünden yüzüyle korunmaya çalışan kimse mi, source:39:24}. İnsan bir darbe gelince yüzünü korur; bu ayette yüz, korunan yer olmaktan çıkıp kalkan olmuştur. İkinci ayetteki yüzlerin dördüncü ayette ateşe girmesi, bu karşılaşmanın surede aldığı biçimdir.

## Eğilen baş, yere düşen bakış, kısılan ses

[¶4] Ayetteki sıfatın temel hareketi alçalıp çökmektir: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Bu hareketin bedendeki ilk görüntüsü başın inmesidir: {ar:تطامن وطأطا رأسه, tr:tatâmene ve ta'ta'e ra'sehû, gloss:çöktü ve başını eğdi, source:"خ ش ع,B001"}. Kelimenin göründüğü yerler de tek tek sayılır: {ar:الخشوع في البدن والصوت والبصر, tr:el-huşûu fi'l-bedeni ve's-savti ve'l-basar, gloss:huşu bedende ve seste ve bakıştadır, source:"خ ش ع,B001"}. Bakıştaki biçimi için {ar:الخشوع رميك ببصرك إلى الأرض, tr:el-huşûu remyüke bi-basarike ile'l-ard, gloss:huşu bakışını yere atmandır, source:"خ ش ع,B001"} denir; sesteki biçimi için de {ar:خشعت الأصوات أي سكنت, tr:haşaati'l-asvâtu ey sekenet, gloss:sesler haşaat yani dindi, source:"خ ش ع,B001"}. Ayet bu sıfatı ne göze verir ne sese; yüze verir. Yüz ise bunların hepsinin yeridir: göz oradadır, ses oradan çıkar, eğilen başın önü odur. Tek sıfat, yüzde buluşan üç eğilmeyi birden söyler.

[¶5] Türkçede huşu bugün çoğunlukla namazdaki iç saygıyı, gönlün toplanmasını anlatır ve bedenden pek söz etmez. Arapçada ise kelime gözle görülen bir şeydir: baş iner, bakış toprağa düşer, ses kısılır. Aşağıda görüleceği gibi aynı kelime yağmursuz toprak, tutulan güneş ve yağı erimiş hörgüç için de söylenir. Türkçedeki kelime bu bedeni de bu dünyayı da geride bırakmıştır.

[¶6] Kur'an sesi, bakışı ve yüzü tek bir sahnede bir araya getirir. Peygamber'e dağların ne olacağı sorulur; Allah, Rabbinin onları savurup yerlerini eğriliği ve tümseği olmayan dümdüz bir düzlük bırakacağını söyler {source:20:107}. Ardından o günün halkı gelir: {ar:يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:yevmeizin yettebiûne'd-dâiye lâ ivece lehû ve haşaati'l-asvâtu li'r-Rahmâni fe-lâ tesmeu illâ hemsâ, gloss:o gün sapmadan çağırıcının ardından giderler; sesler Rahman'ın önünde kısılmıştır; bir fısıltıdan başkasını işitmezsin, source:20:108}. Buradaki "o gün" ikinci ayettekiyle aynı kelimedir, "kısıldı" da ikinci ayetteki sıfatın fiilidir. Üç ayet sonra yüzler de sahneye girer: {ar:وَعَنَتِ ٱلْوُجُوهُ لِلْحَىِّ ٱلْقَيُّومِ, tr:ve aneti'l-vucûhu li'l-Hayyi'l-Kayyûm, gloss:yüzler Diri olana ve her şeyi ayakta tutana boyun eğmiştir, source:20:111}. Yüzler için kullanılan fiil başka bir köktendir; bağ kelimede değil sahnededir. Seslerin kısıldığı ve yüzlerin eğildiği aynı an, ikinci ayetteki tek sıfatın içinde toplanır. O sahne, yüzlerin kimin önünde eğildiğini de söyler: Diri olanın, her şeyi ayakta tutanın önünde. Eğilen yüzün karşısında, eğilmeyen ve düşmeyen biri vardır.

[¶7] Kalıbın kendisi başka bir surede tekrarlanır. Yerin sarsıldığı ve ardından ikinci bir sarsıntının geldiği gün anlatılırken şöyle denir: {ar:قُلُوبٌۭ يَوْمَئِذٍۢ وَاجِفَةٌ, tr:kulûbun yevmeizin vâcife, gloss:o gün birtakım kalpler çarpıntı içindedir, source:79:8}; {ar:أَبْصَٰرُهَا خَٰشِعَةٌۭ, tr:ebsâruhâ hâşia, gloss:onların gözleri yere eğilmiştir, source:79:9}. Kuruluş ikinci ayettekiyle aynıdır: bir isim, "o gün" ve bir sıfat. Ama orada önce kalp gelir ve eğilen göz o kalbin gözüdür. Araplar içerisi ile dışarısı arasındaki bu sırayı açıkça söylerdi: {ar:إذا ضرع القلب خشعت الجوارح, tr:izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. İkinci ayet kalbi anmaz, yalnız yüzü gösterir; içeride olanı aynı kalıptaki bu öteki ayet söyler.

[¶8] Eğik yüzün nasıl baktığını da Kur'an gösterir. Zalimlerin ateşe sunulduğu sahnede şöyle denir: {ar:وَتَرَىٰهُمْ يُعْرَضُونَ عَلَيْهَا خَٰشِعِينَ مِنَ ٱلذُّلِّ يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ, tr:ve terâhum yu'radûne aleyhâ hâşiîne mine'z-zulli yenzurûne min tarfin hafiyy, gloss:onları aşağılanmadan eğilmiş halde ateşe sunulurken ve gizli bir göz ucuyla bakarken görürsün, source:42:45}. Yüz, başka bir yüzün karşısına konmak için vardı; şimdi karşısına ancak göz ucuyla, kaçamak bakabilir.

[¶9] Dünyada bu eğilme taklit de edilebilir: {ar:التخشع تكلف الخشوع, tr:et-tehaşşuu tekellufu'l-huşû', gloss:tehaşşu huşuyu zorla takınmaktır, source:"خ ش ع,B001"}. İçi dışına uymayan kimseye de yüz kelimesiyle ad verilmiştir: {ar:رجل ذو وجهين إذا لقي بخلاف ما في قلبه, tr:racülün zû vechayni izâ lakiye bi-hılâfi mâ fî kalbih, gloss:karşısındakini kalbindekinin tersiyle karşılayan adama iki yüzlü denir, source:"و ج ه,B015"}. O gün ne takınılmış bir huşu kalır ne ikinci bir yüz. Bir başka surede, insanın atılan bir sudan yaratıldığı ve Allah'ın onu geri döndürmeye gücünün yettiği söylendikten {source:86:8} sonra o gün şöyle anılır: {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tuble's-serâir, gloss:gizlilerin sınanıp ortaya çıktığı gün, source:86:9}. İkinci ayetteki yüz, kalbin hâlini dışarıya olduğu gibi taşıyan tek bir yüzdür.

## Yağmur görmemiş toprak

[¶10] Bundan sonra kelimenin başka kullanımlarından gelen resimler anılacak. Bunlar ayetteki "eğilmiş, çökmüş" anlamının yerine geçmez, o anlamın yanında duyulur.

[¶11] Araplar bu sıfatı bir yer parçası için de kullanırdı: {ar:الخشعة قطعة من الأرض قف قد غلبت عليه السهولة, tr:el-huş'atu kıt'atun mine'l-ardi kuffun kad ğalebet aleyhi's-suhûle, gloss:huş'a düzlüğün üstün geldiği sert bir yer parçasıdır, source:"خ ش ع,B002"}. Kuff, düz arazinin ortasında kabaran sert, taşlık bir sırttır; huş'a ise yükselmesi gerekirken düzlüğe yenilip yere yatmış böyle bir sırttır. Aynı yer {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"} diye de anılır; küçük bir tepe için de {ar:الخشعة أكمة متواضعة, tr:el-huş'atu ekemetun mütevâdia, gloss:huş'a mütevazı bir tepeciktir, source:"خ ش ع,B002"} denir. Türkçedeki "mütevazı" burada bir tepeye verilmiştir: kendini yerden yukarı kaldırmayan tepe. Yıkılmış bir duvar için de aynı sıfat söylenir: {ar:جدار خاشع, tr:cidârun hâşi', gloss:çöküp yere inmiş duvar, source:"خ ش ع,B002"}. Ayakta durması gereken şey yere doğru inmiştir.

[¶12] Resmin en canlı yüzü kuraklıktır: {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}. Böyle bir yer için {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:yağmursuz kalmış tozlu yöre, source:"خ ش ع,B002"} ve {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:kurumuş ve cansız toprak, source:"خ ش ع,B002"} derlerdi. Yağmur almayan toprakta bitki çekilir, yüzey kurur, tozu kalkar ve toprağın kabarıklığı iner. Kur'an bu toprağı tam da ikinci ayetteki kelimeyle anar. Allah kendi işaretlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirdiğimizde kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen bunu ölülerin dirilişine bağlar: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten elbette ölüleri de diriltendir, source:41:39}. Dirilişten şüphe eden insanlara seslenilen bir başka ayette, onların topraktan ve damladan nasıl yaratıldıkları anlatıldıktan sonra aynı sahne toprağın öteki sıfatıyla kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri kupkuru ve cansız görürsün; üstüne su indirdiğimizde kıpırdar ve kabarır, source:22:5}. İki ayetin iki sıfatı, Arapların kurak toprak için söylediği "hâşia hâmide" ikilisinde yan yana durur.

[¶13] İkinci ayetteki yüzün yanında böyle bir toprak duyulur: kurumuş, tozlanmış, yere yapışmış. Kur'an o günün yüzlerini başka bir yerde de toprağın diliyle anlatır. Kulakları sağır eden çığlığın geldiği gün {source:80:33} bazı yüzler ışıl ışıldır, güler ve sevinir; ötekiler için şöyle denir: {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}; {ar:تَرْهَقُهَا قَتَرَةٌ, tr:terhakuhâ katera, gloss:onları kapkara bir duman bürür, source:80:41}. Yüzün üstündeki "toz" ile kurak yöreye verilen "tozlu" sıfatı aynı harflerden, aynı köktendir. Kurak toprağa nasıl bir su verildiğini ise beşinci ayet söyler {source:88:5}; yağmurun yerine kaynar suyun geldiği o sahne surenin kendi sahnesidir ve beşinci ayetin kelimeleriyle kurulur.

[¶14] Dünyada aynı toprak yağmur bekleyebilir. Allah inananlara bir soru sorar: {ar:أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ, tr:e-lem ye'ni lillezîne âmenû en tahşea kulûbuhum li-zikrillâhi ve mâ nezele mine'l-hak, gloss:inananların kalplerinin Allah'ı anmaya ve inen hakka huşu ile eğilme vakti gelmedi mi, source:57:16}. Aynı ayet, kendilerinden önce kitap verilenlerin üzerinden uzun zaman geçince kalplerinin katılaştığını söyler. Bir sonraki ayet ise sözü birden toprağa çevirir: {ar:ٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا, tr:i'lemû ennallâhe yuhyi'l-arda ba'de mevtihâ, gloss:bilin ki Allah yeri ölümünden sonra diriltir, source:57:17}. Kalbin huşuu burada kurumuş toprağın yağmura açılmasına benzer. Kalpler için "inen hak" denir, toprak için "üstüne su indirdik"; iki fiil aynı köktendir. Katılaşan kalp ise suyu almayan taşlık sırta benzer. Bir başka ayette Allah, bu Kur'an'ı bir dağa indirseydi ne olacağını söyler: {ar:لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ, tr:lev enzelnâ hâze'l-Kur'âne alâ cebelin le-raeytehû hâşian mutesaddian min haşyetillâh, gloss:bu Kur'an'ı bir dağa indirseydik onu Allah korkusundan eğilmiş ve yarılmış görürdün, source:59:21}. Yeryüzünün en yüksek yeri, inen sözün altında huş'a gibi yere yatar. Dünyada huşu, yukarıdan inen bir şeyin karşılanmasıdır: su ya da söz. İkinci ayetteki yüzün huşuunda ise beklenen yağmur yoktur; yalnız kuruluk kalmıştır.

## Sönen ışık, çöken hörgüç

[¶15] Ayetin ilk kelimesi, Arapların toplumdaki itibara verdiği adın da ta kendisidir: {ar:وجوه القوم سادتهم ورجل وجيه عند السلطان, tr:vucûhu'l-kavmi sâdetuhum ve racülün vecîhun inde's-sultân, gloss:topluluğun yüzleri onların ulularıdır; hükümdar katında itibarlı adama vecîh denir, source:"و ج ه,B006"}. Türkçeye geçmiş "câh" da bu kelimenin harfleri yer değiştirmiş biçimi olarak anılır: {ar:وجيه بين الجاه والجاه مقلوب, tr:vecîhun beyyinu'l-câhi ve'l-câhu maklûb, gloss:câhı belli bir vecîh; câh yüz kelimesinin harfleri yer değiştirerek oluşmuştur, source:"و ج ه,B006"}. Yüz, kişinin başkalarının gözündeki yüksekliğidir; ikinci ayetin sıfatı ise tam bu yüksekliği alçaltır. "Yüzler" kelimesinin yanında toplumun ulularının adı duyulur. Ayetin anlamı onlarla sınırlı değildir, ama eğilen şeyin ne olduğunu bu ad gösterir: insanın en yukarıda taşıdığı yer.

[¶16] Kelime hayvanın bedeninde de aynı hareketi anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yolda bitkin düşen devenin hörgücü yağı gidip tepesi eğilince haşaa denir, source:"خ ش ع,B004"}. Hörgüç, devenin sırtında yağın toplandığı tümsektir ve bedeninin en yüksek noktasıdır. Uzun ve ağır yolda deve bu yağı harcar; yol onu tükettiğinde yağ erir ve hörgücün tepesi çöker. Bu tepeye verilen ad, Türkçede "şeref" diye bilinen kelimedir; Arapçada hem yüksek yer hem onur demektir. Yüzün câhı ile hörgücün şerefi aynı yoldan iner: tükenen emekle. Üçüncü ayetteki çalışıp didinme ve yedinci ayetteki semirtmeyen yiyecek bu resmin yanında durur; o buluşma surenin kendi sahnesidir ve o ayetlerin kelimeleriyle kurulur.

[¶17] Gökte de aynı kelime söylenir: {ar:خشعت الشمس وكسفت وخسفت بمعنى واحد, tr:haşaati'ş-şemsu ve kesefet ve hasefet bi-ma'nen vâhid, gloss:güneş için haşaat ve kesefet ve hasefet aynı anlamdadır yani tutuldu, source:"خ ش ع,B003"}; {ar:خشعت الكواكب إذا دنت من المغيب, tr:haşaati'l-kevâkibu izâ denet mine'l-mağîb, gloss:yıldızlar batmaya yaklaşınca haşaat denir, source:"خ ش ع,B003"}. Güneş tutulunca gündüzün ortasında ışığı kararır; batmaya yaklaşan yıldız ufka iner ve sönükleşir. İkisinde de yukarıda parlayan bir şey alçalır ya da kararır, ve ikinci ayetteki yüzün yanında böyle bir ışık sönmesi de duyulur. Kur'an o günün göğünü yüzlerle aynı surede anlatır. İnsanın kıyamet gününün ne zaman olacağını sorduğu söylendikten sonra cevap gelir: {ar:فَإِذَا بَرِقَ ٱلْبَصَرُ, tr:fe-izâ beraka'l-basar, gloss:göz kamaşıp donduğunda, source:75:7}; {ar:وَخَسَفَ ٱلْقَمَرُ, tr:ve hasefe'l-kamer, gloss:ay tutulduğunda, source:75:8}; {ar:وَجُمِعَ ٱلشَّمْسُ وَٱلْقَمَرُ, tr:ve cumia'ş-şemsu ve'l-kamer, gloss:güneş ile ay bir araya getirildiğinde, source:75:9}; ve o gün {ar:يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ, tr:yekûlu'l-insânu yevmeizin eyne'l-meferr, gloss:insan o gün kaçacak yer nerede der, source:75:10}. Ayın tutulmasını anlatan fiil başka bir köktendir; ama Araplar güneş için o fiille ikinci ayetteki sıfatın fiilini aynı anlamda kullanırdı. Aynı sure birkaç ayet sonra yüzleri ikiye ayırır: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptazedir, source:75:22}; {ar:إِلَىٰ رَبِّهَا نَاظِرَةٌۭ, tr:ilâ rabbihâ nâzıra, gloss:Rablerine bakmaktadır, source:75:23}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de o gün asıktır, source:75:24}; {ar:تَظُنُّ أَن يُفْعَلَ بِهَا فَاقِرَةٌۭ, tr:tezunnu en yuf'ale bihâ fâkıra, gloss:kendilerine bel kıran bir felaketin geleceğini sanırlar, source:75:25}. Ayın karardığı gün yüzlerin bir kısmı da kararır. Gökteki tutulmayı ve yüzdeki çöküşü ikinci ayetin tek sıfatı birlikte taşır. Sekizinci ayetin yumuşak yüzleri ile onuncu ve on üçüncü ayetlerin yüce bahçesi ve kaldırılmış sedirleri bu alçalmanın karşısında durur; o karşılaşmayı da o ayetlerin kelimeleri kurar.

## Yüzün yönü

[¶18] Yüz yalnızca bir organ değil, bir yöndür: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıin istakbeltehû, gloss:vichet yüzünü döndüğün her yerdir, source:"و ج ه,B002"}; {ar:الجهة النحو, tr:el-cihetü'n-nahv, gloss:cihet yöndür, source:"و ج ه,B002"}. Türkçedeki "cihet" ve "tevcih" de bu köktendir. İnsanın amacını yitirmesi bile yüzün yönüyle söylenir: {ar:ضل وجهة أمره إذا ضل قصده, tr:dalle vichete emrihî izâ dalle kasdeh, gloss:amacını yitirince işinin yönünü yitirdi denir, source:"و ج ه,B002"}. Bağlılık da bir yüz yönüdür: {ar:وجهت وجهي لله سبحانه, tr:veccehtü vechî lillâhi subhânehû, gloss:yüzümü Allah'a yönelttim, source:"و ج ه,B005"}.

[¶19] Kur'an bu yönelişi İbrahim'in ağzından anlatır. Allah İbrahim'e göklerin ve yerin hükümranlığını gösterir. Gece onu örtünce bir yıldız görür ve "bu Rabbim" der; yıldız batınca {ar:لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:lâ uhibbu'l-âfilîn, gloss:batanları sevmem, source:6:76} der. Doğarken gördüğü ay ve güneş için de aynısı olur. Sonunda şöyle der: {ar:إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا, tr:innî veccehtü vechiye lillezî fatara's-semâvâti ve'l-arda hanîfâ, gloss:ben yüzümü gökleri ve yeri yaratana dosdoğru yönelttim, source:6:79}. İbrahim'in "batmak" için kullandığı kelime başka bir köktendir. Ama ufka inip sönen yıldıza Araplar ikinci ayetteki sıfatın fiilini de söylerdi. İbrahim yüzünü alçalıp sönen ışıklardan çevirip onları yaratana döndürür. İkinci ayetteki yüz ise kendisi o sönen ışıklara benzemiştir.

[¶20] Yön ile yüz çevirmek Kur'an'da bir başka yerde yan yana gelir. Allah Peygamber'e, yüzünün göğe dönüp durduğunu gördüğünü söyler ve ona razı olacağı bir kıble vereceğini bildirir: {ar:فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ, tr:fe-velli vecheke şatra'l-Mescidi'l-Harâm, gloss:yüzünü Mescid-i Haram'a doğru çevir, source:2:144}. Birkaç ayet sonra şöyle denir: {ar:وَلِكُلٍّۢ وِجْهَةٌ هُوَ مُوَلِّيهَا ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ أَيْنَ مَا تَكُونُوا۟ يَأْتِ بِكُمُ ٱللَّهُ جَمِيعًا, tr:ve li-küllin vichetun huve muvellîhâ festebiku'l-hayrât eyne mâ tekûnû ye'ti bikumullâhu cemîâ, gloss:herkesin yüzünü döndüğü bir yönü vardır; öyleyse iyiliklerde yarışın; nerede olursanız olun Allah hepinizi bir araya getirir, source:2:148}. Buradaki "yön" ikinci ayetteki "yüz" ile aynı köktendir; "döndüğü" ise yirmi üçüncü ayette yüz çevireni anlatan fiille aynı köktendir: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz bir yöne döner ya da bir yönden çevrilir; ama o ayetin sonu, nereye dönülürse dönülsün herkesin bir araya getirileceğini söyler, tıpkı surede yüz çevirenin dönüşünün de "Bize" olması gibi. İkinci ayetteki yüz, yön seçme vaktinin bittiği yüzdür: artık hiçbir yere dönük değildir, bakışı toprağa düşmüştür.

[¶21] Her namazda okunan Fatiha da bir yüz yönüdür. Konuşan, yüzünü doğrudan Allah'a çevirir: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke na'budu ve iyyâke nesteîn, gloss:yalnız Sana kulluk eder ve yalnız Senden yardım dileriz, source:1:5}; ardından yolu ister: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-mustakîm, gloss:bizi dosdoğru yola ilet, source:1:6}. Kur'an dosdoğru yolu yüzle birlikte bir kez daha anar. Allah, rızkını kesse insanlara kimin rızık vereceğini sorar ve onların azgınlıkta, kaçışta direttiklerini söyler {source:67:21}; sonra sorar: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe-men yemşî mukibben alâ vechihî ehdâ em-men yemşî seviyyen alâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Yüzüstü kapanan önündeki yolu göremez; dimdik yürüyen görür. Yere dönük, eğik duruşuyla ikinci ayetteki yüz bu ilk yürüyüşün yüzüne benzer.

## İki eğilme

[¶22] Ayetteki sıfat ibadetin bir duruşuna da ad verir: {ar:الخاشع الراكع, tr:el-hâşiu'r-râki', gloss:hâşi rükû edendir, source:"خ ش ع,B001"}. Rükû, namazda belin bükülüp başın öne eğildiği duruştur. Kur'an kurtuluşa erenleri sayarken ilk olarak bu eğilmeyi anar: {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad efleha'l-mu'minûn, gloss:inananlar kurtuluşa ermiştir, source:23:1}; {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşiûn, gloss:onlar ki namazlarında huşu ile eğilirler, source:23:2}. Bir başka ayette Peygamber'e, inkârcılara "ister inanın ister inanmayın" demesi söylenir ve daha önce kendilerine bilgi verilenlerin Kur'an'ı nasıl karşıladığı anlatılır: {ar:إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًۭا, tr:izâ yutlâ aleyhim yahırrûne li'l-ezkâni succedâ, gloss:onlara okunduğunda çeneleri üstüne secdeye kapanırlar, source:17:107}; {ar:وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا, tr:ve yahırrûne li'l-ezkâni yebkûne ve yezîduhum huşûâ, gloss:ağlayarak çeneleri üstüne kapanırlar ve bu onların huşuunu artırır, source:17:109}. Çene yüzün en alt ucudur. Bu insanlar yüzlerini kendi istekleriyle toprağa indirirler ve her iniş eğilmelerini derinleştirir.

[¶23] Aynı eğilme bir de zorla gelir. O günün bir sahnesinde şöyle denir: {ar:يَوْمَ يُكْشَفُ عَن سَاقٍۢ وَيُدْعَوْنَ إِلَى ٱلسُّجُودِ فَلَا يَسْتَطِيعُونَ, tr:yevme yukşefu an sâkın ve yud'avne ile's-sucûdi fe-lâ yestatîûn, gloss:baldırın açıldığı gün secdeye çağrılırlar ama güç yetiremezler, source:68:42}; {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ, tr:hâşiaten ebsâruhum terhakuhum zilletun ve kad kânû yud'avne ile's-sucûdi ve hum sâlimûn, gloss:gözleri eğik ve kendilerini aşağılanma bürümüştür; oysa sapasağlamken secdeye çağrılıyorlardı, source:68:43}. Dünyada secdeye çağrıldıklarında sağlamdılar ve eğilmek kendi ellerindeydi. O gün yine çağrılırlar ve eğilemezler; ama gözleri eğiktir. İstenen eğilme gelmemiş, istenmeyen eğilme gelmiştir. İkinci ayetteki sıfat bu iki eğilmeyi aynı kelimeyle duyurur: kurtuluşa erenlerin namazdaki huşuu ile o günün çökmüş yüzleri tek bir adla anılır. Aralarındaki fark kelimede değil vakittedir: biri kalpten gelip yüzü kendiliğinden toprağa indirir, öteki vakti geçince dışarıdan gelir ve yüzü toprağa yapıştırır.

===== _commentary/v16/out/88_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: يَوْمَئِذٍ is built from يوم "day" and إذ "then", pointing back to a stated time
- memory: indefinite وُجُوهٌ reads as "some faces", not all faces
- memory: feminine singular agreement of 88:3–5 with the broken plural وجوه
- memory: قفّ is hard, stony raised ground amid flat land
- memory: the hump stores fat that a camel spends on long journeys
- memory: شَرَف means both a high point and honour
- memory: Turkish cihet, tevcih and câh come from the و ج ه root; mütevazı from متواضع
- memory: rükû is the bowing posture of the prayer
- memory: غبرة (80:40) and مغبرة share the root غ ب ر
- not written: خ ش ع B005 (spitting phlegm) - no bearing on the face or the day
- not written: و ج ه B007 (beginning of the day) - no support in the ayah or surah
- not written: و ج ه B009–B012 (ageing, birth, rhyme letter, melon) - unrelated to the ayah's scene
- not written: و ج ه B013 striking the face, with 47:27 faces and backs struck - too thin a tie to lowering
- not written: و ج ه B014 turning back a visitor - no textual support
- not written: و ج ه B008 right course of a matter - adds nothing beyond the direction theme
- not written: 3:106 faces whitened and blackened - repeats the veil and darkness scene owned by the surah commentary
- not written: 70:44 eyes lowered, humiliation covering - duplicates 68:43

===== passages not cited (200) =====
## strong (this ayah's own list) (24)

- (3:106) [listed for 88:2] يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌۭ ۚ فَأَمَّا ٱلَّذِينَ ٱسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُم بَعْدَ إِيمَٰنِكُمْ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (3:107) [listed for 88:2] وَأَمَّا ٱلَّذِينَ ٱبْيَضَّتْ وُجُوهُهُمْ فَفِى رَحْمَةِ ٱللَّهِ هُمْ فِيهَا خَٰلِدُونَ
- (10:26) [listed for 88:2] ۞ لِّلَّذِينَ أَحْسَنُوا۟ ٱلْحُسْنَىٰ وَزِيَادَةٌۭ ۖ وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (10:27) [listed for 88:2] وَٱلَّذِينَ كَسَبُوا۟ ٱلسَّيِّـَٔاتِ جَزَآءُ سَيِّئَةٍۭ بِمِثْلِهَا وَتَرْهَقُهُمْ ذِلَّةٌۭ ۖ مَّا لَهُم مِّنَ ٱللَّهِ مِنْ عَاصِمٍۢ ۖ كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (17:109) [listed for 88:2] [cited in ¶22] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
- (20:108) [listed for 88:2] [cited in ¶6] يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا
- (20:111) [listed for 88:2] [cited in ¶6] ۞ وَعَنَتِ ٱلْوُجُوهُ لِلْحَىِّ ٱلْقَيُّومِ ۖ وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا
- (32:12) [listed for 88:2] وَلَوْ تَرَىٰٓ إِذِ ٱلْمُجْرِمُونَ نَاكِسُوا۟ رُءُوسِهِمْ عِندَ رَبِّهِمْ رَبَّنَآ أَبْصَرْنَا وَسَمِعْنَا فَٱرْجِعْنَا نَعْمَلْ صَٰلِحًا إِنَّا مُوقِنُونَ
- (33:66) [listed for 88:2] يَوْمَ تُقَلَّبُ وُجُوهُهُمْ فِى ٱلنَّارِ يَقُولُونَ يَٰلَيْتَنَآ أَطَعْنَا ٱللَّهَ وَأَطَعْنَا ٱلرَّسُولَا۠
- (39:24) [listed for 88:2] [cited in ¶3] أَفَمَن يَتَّقِى بِوَجْهِهِۦ سُوٓءَ ٱلْعَذَابِ يَوْمَ ٱلْقِيَٰمَةِ ۚ وَقِيلَ لِلظَّٰلِمِينَ ذُوقُوا۟ مَا كُنتُمْ تَكْسِبُونَ
- (39:60) [listed for 88:2] وَيَوْمَ ٱلْقِيَٰمَةِ تَرَى ٱلَّذِينَ كَذَبُوا۟ عَلَى ٱللَّهِ وُجُوهُهُم مُّسْوَدَّةٌ ۚ أَلَيْسَ فِى جَهَنَّمَ مَثْوًۭى لِّلْمُتَكَبِّرِينَ
- (42:45) [listed for 88:2] [cited in ¶8] وَتَرَىٰهُمْ يُعْرَضُونَ عَلَيْهَا خَٰشِعِينَ مِنَ ٱلذُّلِّ يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ ۗ وَقَالَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَآ إِنَّ ٱلظَّٰلِمِينَ فِى عَذَابٍۢ مُّقِيمٍۢ
- (54:7) [listed for 88:2] خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ
- (57:16) [listed for 88:2] [cited in ¶14] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (68:42) [listed for 88:2] [cited in ¶23] يَوْمَ يُكْشَفُ عَن سَاقٍۢ وَيُدْعَوْنَ إِلَى ٱلسُّجُودِ فَلَا يَسْتَطِيعُونَ
- (75:22) [listed for 88:2] [cited in ¶17] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
- (75:23) [listed for 88:2] [cited in ¶17] إِلَىٰ رَبِّهَا نَاظِرَةٌۭ
- (75:24) [listed for 88:2] [cited in ¶17] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ
- (76:11) [listed for 88:2] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (79:9) [listed for 88:2] [cited in ¶7] أَبْصَٰرُهَا خَٰشِعَةٌۭ
- (80:38) [listed for 88:2] وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ
- (80:39) [listed for 88:2] ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ
- (80:40) [listed for 88:2] [cited in ¶13] وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ
- (80:41) [listed for 88:2] [cited in ¶13] تَرْهَقُهَا قَتَرَةٌ

## medium (this ayah's own list) (49)

- (2:45) [listed for 88:2] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
- (2:112) [listed for 88:2] بَلَىٰ مَنْ أَسْلَمَ وَجْهَهُۥ لِلَّهِ وَهُوَ مُحْسِنٌۭ فَلَهُۥٓ أَجْرُهُۥ عِندَ رَبِّهِۦ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:150) [listed for 88:2] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
- (2:177) [listed for 88:2] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
- (3:20) [listed for 88:2] فَإِنْ حَآجُّوكَ فَقُلْ أَسْلَمْتُ وَجْهِىَ لِلَّهِ وَمَنِ ٱتَّبَعَنِ ۗ وَقُل لِّلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْأُمِّيِّۦنَ ءَأَسْلَمْتُمْ ۚ فَإِنْ أَسْلَمُوا۟ فَقَدِ ٱهْتَدَوا۟ ۖ وَّإِن تَوَلَّوْا۟ فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:199) [listed for 88:2] وَإِنَّ مِنْ أَهْلِ ٱلْكِتَٰبِ لَمَن يُؤْمِنُ بِٱللَّهِ وَمَآ أُنزِلَ إِلَيْكُمْ وَمَآ أُنزِلَ إِلَيْهِمْ خَٰشِعِينَ لِلَّهِ لَا يَشْتَرُونَ بِـَٔايَٰتِ ٱللَّهِ ثَمَنًۭا قَلِيلًا ۗ أُو۟لَٰٓئِكَ لَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ ۗ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (4:125) [listed for 88:2] وَمَنْ أَحْسَنُ دِينًۭا مِّمَّنْ أَسْلَمَ وَجْهَهُۥ لِلَّهِ وَهُوَ مُحْسِنٌۭ وَٱتَّبَعَ مِلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۗ وَٱتَّخَذَ ٱللَّهُ إِبْرَٰهِيمَ خَلِيلًۭا
- (6:79) [listed for 88:2] [cited in ¶19] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (7:8) [listed for 88:2] وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (7:29) [listed for 88:2] قُلْ أَمَرَ رَبِّى بِٱلْقِسْطِ ۖ وَأَقِيمُوا۟ وُجُوهَكُمْ عِندَ كُلِّ مَسْجِدٍۢ وَٱدْعُوهُ مُخْلِصِينَ لَهُ ٱلدِّينَ ۚ كَمَا بَدَأَكُمْ تَعُودُونَ
- (8:16) [listed for 88:2] وَمَن يُوَلِّهِمْ يَوْمَئِذٍۢ دُبُرَهُۥٓ إِلَّا مُتَحَرِّفًۭا لِّقِتَالٍ أَوْ مُتَحَيِّزًا إِلَىٰ فِئَةٍۢ فَقَدْ بَآءَ بِغَضَبٍۢ مِّنَ ٱللَّهِ وَمَأْوَىٰهُ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (8:50) [listed for 88:2] وَلَوْ تَرَىٰٓ إِذْ يَتَوَفَّى ٱلَّذِينَ كَفَرُوا۟ ۙ ٱلْمَلَٰٓئِكَةُ يَضْرِبُونَ وُجُوهَهُمْ وَأَدْبَٰرَهُمْ وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (14:49) [listed for 88:2] وَتَرَى ٱلْمُجْرِمِينَ يَوْمَئِذٍۢ مُّقَرَّنِينَ فِى ٱلْأَصْفَادِ
- (14:50) [listed for 88:2] سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ
- (16:87) [listed for 88:2] وَأَلْقَوْا۟ إِلَى ٱللَّهِ يَوْمَئِذٍ ٱلسَّلَمَ ۖ وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ
- (17:97) [listed for 88:2] وَمَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُمْ أَوْلِيَآءَ مِن دُونِهِۦ ۖ وَنَحْشُرُهُمْ يَوْمَ ٱلْقِيَٰمَةِ عَلَىٰ وُجُوهِهِمْ عُمْيًۭا وَبُكْمًۭا وَصُمًّۭا ۖ مَّأْوَىٰهُمْ جَهَنَّمُ ۖ كُلَّمَا خَبَتْ زِدْنَٰهُمْ سَعِيرًۭا
- (18:99) [listed for 88:2] ۞ وَتَرَكْنَا بَعْضَهُمْ يَوْمَئِذٍۢ يَمُوجُ فِى بَعْضٍۢ ۖ وَنُفِخَ فِى ٱلصُّورِ فَجَمَعْنَٰهُمْ جَمْعًۭا
- (18:100) [listed for 88:2] وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا
- (20:102) [listed for 88:2] يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ وَنَحْشُرُ ٱلْمُجْرِمِينَ يَوْمَئِذٍۢ زُرْقًۭا
- (20:109) [listed for 88:2] يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَرَضِىَ لَهُۥ قَوْلًۭا
- (21:39) [listed for 88:2] لَوْ يَعْلَمُ ٱلَّذِينَ كَفَرُوا۟ حِينَ لَا يَكُفُّونَ عَن وُجُوهِهِمُ ٱلنَّارَ وَلَا عَن ظُهُورِهِمْ وَلَا هُمْ يُنصَرُونَ
- (21:90) [listed for 88:2] فَٱسْتَجَبْنَا لَهُۥ وَوَهَبْنَا لَهُۥ يَحْيَىٰ وَأَصْلَحْنَا لَهُۥ زَوْجَهُۥٓ ۚ إِنَّهُمْ كَانُوا۟ يُسَٰرِعُونَ فِى ٱلْخَيْرَٰتِ وَيَدْعُونَنَا رَغَبًۭا وَرَهَبًۭا ۖ وَكَانُوا۟ لَنَا خَٰشِعِينَ
- (22:56) [listed for 88:2] ٱلْمُلْكُ يَوْمَئِذٍۢ لِّلَّهِ يَحْكُمُ بَيْنَهُمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (22:72) [listed for 88:2] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ تَعْرِفُ فِى وُجُوهِ ٱلَّذِينَ كَفَرُوا۟ ٱلْمُنكَرَ ۖ يَكَادُونَ يَسْطُونَ بِٱلَّذِينَ يَتْلُونَ عَلَيْهِمْ ءَايَٰتِنَا ۗ قُلْ أَفَأُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكُمُ ۗ ٱلنَّارُ وَعَدَهَا ٱللَّهُ ٱلَّذِينَ كَفَرُوا۟ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (23:2) [listed for 88:2] [cited in ¶22] ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ
- (23:101) [listed for 88:2] فَإِذَا نُفِخَ فِى ٱلصُّورِ فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ
- (23:104) [listed for 88:2] تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ
- (24:37) [listed for 88:2] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
- (27:90) [listed for 88:2] وَمَن جَآءَ بِٱلسَّيِّئَةِ فَكُبَّتْ وُجُوهُهُمْ فِى ٱلنَّارِ هَلْ تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (33:35) [listed for 88:2] إِنَّ ٱلْمُسْلِمِينَ وَٱلْمُسْلِمَٰتِ وَٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ وَٱلْقَٰنِتِينَ وَٱلْقَٰنِتَٰتِ وَٱلصَّٰدِقِينَ وَٱلصَّٰدِقَٰتِ وَٱلصَّٰبِرِينَ وَٱلصَّٰبِرَٰتِ وَٱلْخَٰشِعِينَ وَٱلْخَٰشِعَٰتِ وَٱلْمُتَصَدِّقِينَ وَٱلْمُتَصَدِّقَٰتِ وَٱلصَّٰٓئِمِينَ وَٱلصَّٰٓئِمَٰتِ وَٱلْحَٰفِظِينَ فُرُوجَهُمْ وَٱلْحَٰفِظَٰتِ وَٱلذَّٰكِرِينَ ٱللَّهَ كَثِيرًۭا وَٱلذَّٰكِرَٰتِ أَعَدَّ ٱللَّهُ لَهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۭا
- (40:9) [listed for 88:2] وَقِهِمُ ٱلسَّيِّـَٔاتِ ۚ وَمَن تَقِ ٱلسَّيِّـَٔاتِ يَوْمَئِذٍۢ فَقَدْ رَحِمْتَهُۥ ۚ وَذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (42:47) [listed for 88:2] ٱسْتَجِيبُوا۟ لِرَبِّكُم مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۚ مَا لَكُم مِّن مَّلْجَإٍۢ يَوْمَئِذٍۢ وَمَا لَكُم مِّن نَّكِيرٍۢ
- (43:17) [listed for 88:2] وَإِذَا بُشِّرَ أَحَدُهُم بِمَا ضَرَبَ لِلرَّحْمَٰنِ مَثَلًۭا ظَلَّ وَجْهُهُۥ مُسْوَدًّۭا وَهُوَ كَظِيمٌ
- (54:6) [listed for 88:2] فَتَوَلَّ عَنْهُمْ ۘ يَوْمَ يَدْعُ ٱلدَّاعِ إِلَىٰ شَىْءٍۢ نُّكُرٍ
- (55:41) [listed for 88:2] يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ
- (59:21) [listed for 88:2] [cited in ¶14] لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- (67:22) [listed for 88:2] [cited in ¶21] أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (67:27) [listed for 88:2] فَلَمَّا رَأَوْهُ زُلْفَةًۭ سِيٓـَٔتْ وُجُوهُ ٱلَّذِينَ كَفَرُوا۟ وَقِيلَ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تَدَّعُونَ
- (68:43) [listed for 88:2] [cited in ¶23] خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ
- (70:43) [listed for 88:2] يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ
- (70:44) [listed for 88:2] خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۚ ذَٰلِكَ ٱلْيَوْمُ ٱلَّذِى كَانُوا۟ يُوعَدُونَ
- (75:25) [listed for 88:2] [cited in ¶17] تَظُنُّ أَن يُفْعَلَ بِهَا فَاقِرَةٌۭ
- (76:10) [listed for 88:2] إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا
- (79:8) [listed for 88:2] [cited in ¶7] قُلُوبٌۭ يَوْمَئِذٍۢ وَاجِفَةٌ
- (83:15) [listed for 88:2] كَلَّآ إِنَّهُمْ عَن رَّبِّهِمْ يَوْمَئِذٍۢ لَّمَحْجُوبُونَ
- (83:24) [listed for 88:2] تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ
- (92:14) [listed for 88:2] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:16) [listed for 88:2] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:20) [listed for 88:2] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ

## named by the passage's own list as strong for this ayah (2)

- (7:41) [listed for 88:2] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (55:44) [listed for 88:2] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ

## named by the passage's own list as medium for this ayah (14)

- (12:9) [listed for 88:2] ٱقْتُلُوا۟ يُوسُفَ أَوِ ٱطْرَحُوهُ أَرْضًۭا يَخْلُ لَكُمْ وَجْهُ أَبِيكُمْ وَتَكُونُوا۟ مِنۢ بَعْدِهِۦ قَوْمًۭا صَٰلِحِينَ
- (26:87) [listed for 88:2] وَلَا تُخْزِنِى يَوْمَ يُبْعَثُونَ
- (36:59) [listed for 88:2] وَٱمْتَٰزُوا۟ ٱلْيَوْمَ أَيُّهَا ٱلْمُجْرِمُونَ
- (40:52) [listed for 88:2] يَوْمَ لَا يَنفَعُ ٱلظَّٰلِمِينَ مَعْذِرَتُهُمْ ۖ وَلَهُمُ ٱللَّعْنَةُ وَلَهُمْ سُوٓءُ ٱلدَّارِ
- (42:7) [listed for 88:2] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ قُرْءَانًا عَرَبِيًّۭا لِّتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا وَتُنذِرَ يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ ۚ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ
- (56:3) [listed for 88:2] خَافِضَةٌۭ رَّافِعَةٌ
- (68:16) [listed for 88:2] سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ
- (69:18) [listed for 88:2] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (70:15) [listed for 88:2] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (74:10) [listed for 88:2] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (75:13) [listed for 88:2] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
- (83:5) [listed for 88:2] لِيَوْمٍ عَظِيمٍۢ
- (84:12) [listed for 88:2] وَيَصْلَىٰ سَعِيرًا
- (89:23) [listed for 88:2] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ

## weak (this ayah's own list) (25)

- (2:115) [listed for 88:2] وَلِلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ فَأَيْنَمَا تُوَلُّوا۟ فَثَمَّ وَجْهُ ٱللَّهِ ۚ إِنَّ ٱللَّهَ وَٰسِعٌ عَلِيمٌۭ
- (2:144) [listed for 88:2] [cited in ¶20] قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا يَعْمَلُونَ
- (2:272) [listed for 88:2] ۞ لَّيْسَ عَلَيْكَ هُدَىٰهُمْ وَلَٰكِنَّ ٱللَّهَ يَهْدِى مَن يَشَآءُ ۗ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ فَلِأَنفُسِكُمْ ۚ وَمَا تُنفِقُونَ إِلَّا ٱبْتِغَآءَ وَجْهِ ٱللَّهِ ۚ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ يُوَفَّ إِلَيْكُمْ وَأَنتُمْ لَا تُظْلَمُونَ
- (3:72) [listed for 88:2] وَقَالَت طَّآئِفَةٌۭ مِّنْ أَهْلِ ٱلْكِتَٰبِ ءَامِنُوا۟ بِٱلَّذِىٓ أُنزِلَ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَجْهَ ٱلنَّهَارِ وَٱكْفُرُوٓا۟ ءَاخِرَهُۥ لَعَلَّهُمْ يَرْجِعُونَ
- (3:167) [listed for 88:2] وَلِيَعْلَمَ ٱلَّذِينَ نَافَقُوا۟ ۚ وَقِيلَ لَهُمْ تَعَالَوْا۟ قَٰتِلُوا۟ فِى سَبِيلِ ٱللَّهِ أَوِ ٱدْفَعُوا۟ ۖ قَالُوا۟ لَوْ نَعْلَمُ قِتَالًۭا لَّٱتَّبَعْنَٰكُمْ ۗ هُمْ لِلْكُفْرِ يَوْمَئِذٍ أَقْرَبُ مِنْهُمْ لِلْإِيمَٰنِ ۚ يَقُولُونَ بِأَفْوَٰهِهِم مَّا لَيْسَ فِى قُلُوبِهِمْ ۗ وَٱللَّهُ أَعْلَمُ بِمَا يَكْتُمُونَ
- (4:42) [listed for 88:2] يَوْمَئِذٍۢ يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ وَعَصَوُا۟ ٱلرَّسُولَ لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ وَلَا يَكْتُمُونَ ٱللَّهَ حَدِيثًۭا
- (5:6) [listed for 88:2] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (6:16) [listed for 88:2] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (6:52) [listed for 88:2] وَلَا تَطْرُدِ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ مَا عَلَيْكَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَمَا مِنْ حِسَابِكَ عَلَيْهِم مِّن شَىْءٍۢ فَتَطْرُدَهُمْ فَتَكُونَ مِنَ ٱلظَّٰلِمِينَ
- (11:66) [listed for 88:2] فَلَمَّا جَآءَ أَمْرُنَا نَجَّيْنَا صَٰلِحًۭا وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ بِرَحْمَةٍۢ مِّنَّا وَمِنْ خِزْىِ يَوْمِئِذٍ ۗ إِنَّ رَبَّكَ هُوَ ٱلْقَوِىُّ ٱلْعَزِيزُ
- (12:93) [listed for 88:2] ٱذْهَبُوا۟ بِقَمِيصِى هَٰذَا فَأَلْقُوهُ عَلَىٰ وَجْهِ أَبِى يَأْتِ بَصِيرًۭا وَأْتُونِى بِأَهْلِكُمْ أَجْمَعِينَ
- (13:22) [listed for 88:2] وَٱلَّذِينَ صَبَرُوا۟ ٱبْتِغَآءَ وَجْهِ رَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ وَيَدْرَءُونَ بِٱلْحَسَنَةِ ٱلسَّيِّئَةَ أُو۟لَٰٓئِكَ لَهُمْ عُقْبَى ٱلدَّارِ
- (18:28) [listed for 88:2] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (25:24) [listed for 88:2] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (28:88) [listed for 88:2] وَلَا تَدْعُ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ ۘ لَآ إِلَٰهَ إِلَّا هُوَ ۚ كُلُّ شَىْءٍ هَالِكٌ إِلَّا وَجْهَهُۥ ۚ لَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
- (30:38) [listed for 88:2] فَـَٔاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ ۚ ذَٰلِكَ خَيْرٌۭ لِّلَّذِينَ يُرِيدُونَ وَجْهَ ٱللَّهِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (34:43) [listed for 88:2] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ قَالُوا۟ مَا هَٰذَآ إِلَّا رَجُلٌۭ يُرِيدُ أَن يَصُدَّكُمْ عَمَّا كَانَ يَعْبُدُ ءَابَآؤُكُمْ وَقَالُوا۟ مَا هَٰذَآ إِلَّآ إِفْكٌۭ مُّفْتَرًۭى ۚ وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لِلْحَقِّ لَمَّا جَآءَهُمْ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ
- (41:39) [listed for 88:2] [cited in ¶12] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (47:27) [listed for 88:2] فَكَيْفَ إِذَا تَوَفَّتْهُمُ ٱلْمَلَٰٓئِكَةُ يَضْرِبُونَ وُجُوهَهُمْ وَأَدْبَٰرَهُمْ
- (48:29) [listed for 88:2] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
- (51:29) [listed for 88:2] فَأَقْبَلَتِ ٱمْرَأَتُهُۥ فِى صَرَّةٍۢ فَصَكَّتْ وَجْهَهَا وَقَالَتْ عَجُوزٌ عَقِيمٌۭ
- (54:48) [listed for 88:2] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (55:27) [listed for 88:2] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (76:9) [listed for 88:2] إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا
- (77:15) [listed for 88:2] وَيْلٌۭ يَوْمَئِذٍۢ لِّلْمُكَذِّبِينَ

## named by the passage's own list as weak for this ayah (6)

- (6:44) [listed for 88:2] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦ فَتَحْنَا عَلَيْهِمْ أَبْوَٰبَ كُلِّ شَىْءٍ حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ فَإِذَا هُم مُّبْلِسُونَ
- (69:15) [listed for 88:2] فَيَوْمَئِذٍۢ وَقَعَتِ ٱلْوَاقِعَةُ
- (74:9) [listed for 88:2] فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ
- (90:8) [listed for 88:2] أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- (92:12) [listed for 88:2] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (99:6) [listed for 88:2] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ

## neighbours: within two ayat of a passage the commentary cites (80)

- (1:3) [next to 1:5] ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (1:4) [next to 1:5] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (1:7) [next to 1:5] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- (2:142) [next to 2:144] ۞ سَيَقُولُ ٱلسُّفَهَآءُ مِنَ ٱلنَّاسِ مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (2:143) [next to 2:144] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
- (2:145) [next to 2:144] وَلَئِنْ أَتَيْتَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ بِكُلِّ ءَايَةٍۢ مَّا تَبِعُوا۟ قِبْلَتَكَ ۚ وَمَآ أَنتَ بِتَابِعٍۢ قِبْلَتَهُمْ ۚ وَمَا بَعْضُهُم بِتَابِعٍۢ قِبْلَةَ بَعْضٍۢ ۚ وَلَئِنِ ٱتَّبَعْتَ أَهْوَآءَهُم مِّنۢ بَعْدِ مَا جَآءَكَ مِنَ ٱلْعِلْمِ ۙ إِنَّكَ إِذًۭا لَّمِنَ ٱلظَّٰلِمِينَ
- (2:146) [next to 2:144] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَعْرِفُونَهُۥ كَمَا يَعْرِفُونَ أَبْنَآءَهُمْ ۖ وَإِنَّ فَرِيقًۭا مِّنْهُمْ لَيَكْتُمُونَ ٱلْحَقَّ وَهُمْ يَعْلَمُونَ
- (2:147) [next to 2:148] ٱلْحَقُّ مِن رَّبِّكَ ۖ فَلَا تَكُونَنَّ مِنَ ٱلْمُمْتَرِينَ
- (2:149) [next to 2:148] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۖ وَإِنَّهُۥ لَلْحَقُّ مِن رَّبِّكَ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (6:74) [next to 6:76] ۞ وَإِذْ قَالَ إِبْرَٰهِيمُ لِأَبِيهِ ءَازَرَ أَتَتَّخِذُ أَصْنَامًا ءَالِهَةً ۖ إِنِّىٓ أَرَىٰكَ وَقَوْمَكَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (6:75) [next to 6:76] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (6:77) [next to 6:76] فَلَمَّا رَءَا ٱلْقَمَرَ بَازِغًۭا قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ
- (6:78) [next to 6:76] فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ ۖ فَلَمَّآ أَفَلَتْ قَالَ يَٰقَوْمِ إِنِّى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:80) [next to 6:79] وَحَآجَّهُۥ قَوْمُهُۥ ۚ قَالَ أَتُحَٰٓجُّوٓنِّى فِى ٱللَّهِ وَقَدْ هَدَىٰنِ ۚ وَلَآ أَخَافُ مَا تُشْرِكُونَ بِهِۦٓ إِلَّآ أَن يَشَآءَ رَبِّى شَيْـًۭٔا ۗ وَسِعَ رَبِّى كُلَّ شَىْءٍ عِلْمًا ۗ أَفَلَا تَتَذَكَّرُونَ
- (6:81) [next to 6:79] وَكَيْفَ أَخَافُ مَآ أَشْرَكْتُمْ وَلَا تَخَافُونَ أَنَّكُمْ أَشْرَكْتُم بِٱللَّهِ مَا لَمْ يُنَزِّلْ بِهِۦ عَلَيْكُمْ سُلْطَٰنًۭا ۚ فَأَىُّ ٱلْفَرِيقَيْنِ أَحَقُّ بِٱلْأَمْنِ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (17:105) [next to 17:107] وَبِٱلْحَقِّ أَنزَلْنَٰهُ وَبِٱلْحَقِّ نَزَلَ ۗ وَمَآ أَرْسَلْنَٰكَ إِلَّا مُبَشِّرًۭا وَنَذِيرًۭا
- (17:106) [next to 17:107] وَقُرْءَانًۭا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍۢ وَنَزَّلْنَٰهُ تَنزِيلًۭا
- (17:108) [next to 17:107] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
- (17:110) [next to 17:109] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (17:111) [next to 17:109] وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ ۖ وَكَبِّرْهُ تَكْبِيرًۢا
- (20:105) [next to 20:107] وَيَسْـَٔلُونَكَ عَنِ ٱلْجِبَالِ فَقُلْ يَنسِفُهَا رَبِّى نَسْفًۭا
- (20:106) [next to 20:107] فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا
- (20:110) [next to 20:108] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِهِۦ عِلْمًۭا
- (20:112) [next to 20:111] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا يَخَافُ ظُلْمًۭا وَلَا هَضْمًۭا
- (20:113) [next to 20:111] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
- (22:3) [next to 22:5] وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّبِعُ كُلَّ شَيْطَٰنٍۢ مَّرِيدٍۢ
- (22:4) [next to 22:5] كُتِبَ عَلَيْهِ أَنَّهُۥ مَن تَوَلَّاهُ فَأَنَّهُۥ يُضِلُّهُۥ وَيَهْدِيهِ إِلَىٰ عَذَابِ ٱلسَّعِيرِ
- (22:6) [next to 22:5] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّهُۥ يُحْىِ ٱلْمَوْتَىٰ وَأَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (22:7) [next to 22:5] وَأَنَّ ٱلسَّاعَةَ ءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ
- (23:0) [next to 23:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (23:3) [next to 23:1] وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ
- (23:4) [next to 23:2] وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ
- (39:21) [next to 39:23] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (39:22) [next to 39:23] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (39:25) [next to 39:23] كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ فَأَتَىٰهُمُ ٱلْعَذَابُ مِنْ حَيْثُ لَا يَشْعُرُونَ
- (39:26) [next to 39:24] فَأَذَاقَهُمُ ٱللَّهُ ٱلْخِزْىَ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- (41:37) [next to 41:39] وَمِنْ ءَايَٰتِهِ ٱلَّيْلُ وَٱلنَّهَارُ وَٱلشَّمْسُ وَٱلْقَمَرُ ۚ لَا تَسْجُدُوا۟ لِلشَّمْسِ وَلَا لِلْقَمَرِ وَٱسْجُدُوا۟ لِلَّهِ ٱلَّذِى خَلَقَهُنَّ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (41:38) [next to 41:39] فَإِنِ ٱسْتَكْبَرُوا۟ فَٱلَّذِينَ عِندَ رَبِّكَ يُسَبِّحُونَ لَهُۥ بِٱلَّيْلِ وَٱلنَّهَارِ وَهُمْ لَا يَسْـَٔمُونَ ۩
- (41:40) [next to 41:39] إِنَّ ٱلَّذِينَ يُلْحِدُونَ فِىٓ ءَايَٰتِنَا لَا يَخْفَوْنَ عَلَيْنَآ ۗ أَفَمَن يُلْقَىٰ فِى ٱلنَّارِ خَيْرٌ أَم مَّن يَأْتِىٓ ءَامِنًۭا يَوْمَ ٱلْقِيَٰمَةِ ۚ ٱعْمَلُوا۟ مَا شِئْتُمْ ۖ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌ
- (41:41) [next to 41:39] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِٱلذِّكْرِ لَمَّا جَآءَهُمْ ۖ وَإِنَّهُۥ لَكِتَٰبٌ عَزِيزٌۭ
- (42:43) [next to 42:45] وَلَمَن صَبَرَ وَغَفَرَ إِنَّ ذَٰلِكَ لَمِنْ عَزْمِ ٱلْأُمُورِ
- (42:44) [next to 42:45] وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن وَلِىٍّۢ مِّنۢ بَعْدِهِۦ ۗ وَتَرَى ٱلظَّٰلِمِينَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ يَقُولُونَ هَلْ إِلَىٰ مَرَدٍّۢ مِّن سَبِيلٍۢ
- (42:46) [next to 42:45] وَمَا كَانَ لَهُم مِّنْ أَوْلِيَآءَ يَنصُرُونَهُم مِّن دُونِ ٱللَّهِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن سَبِيلٍ
- (57:14) [next to 57:16] يُنَادُونَهُمْ أَلَمْ نَكُن مَّعَكُمْ ۖ قَالُوا۟ بَلَىٰ وَلَٰكِنَّكُمْ فَتَنتُمْ أَنفُسَكُمْ وَتَرَبَّصْتُمْ وَٱرْتَبْتُمْ وَغَرَّتْكُمُ ٱلْأَمَانِىُّ حَتَّىٰ جَآءَ أَمْرُ ٱللَّهِ وَغَرَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (57:15) [next to 57:16] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (57:18) [next to 57:16] إِنَّ ٱلْمُصَّدِّقِينَ وَٱلْمُصَّدِّقَٰتِ وَأَقْرَضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا يُضَٰعَفُ لَهُمْ وَلَهُمْ أَجْرٌۭ كَرِيمٌۭ
- (57:19) [next to 57:17] وَٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَرُسُلِهِۦٓ أُو۟لَٰٓئِكَ هُمُ ٱلصِّدِّيقُونَ ۖ وَٱلشُّهَدَآءُ عِندَ رَبِّهِمْ لَهُمْ أَجْرُهُمْ وَنُورُهُمْ ۖ وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَحِيمِ
- (59:19) [next to 59:21] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (59:20) [next to 59:21] لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- (59:22) [next to 59:21] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (59:23) [next to 59:21] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- (67:19) [next to 67:21] أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ ۚ مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍۭ بَصِيرٌ
- (67:20) [next to 67:21] أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- (67:23) [next to 67:21] قُلْ هُوَ ٱلَّذِىٓ أَنشَأَكُمْ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۖ قَلِيلًۭا مَّا تَشْكُرُونَ
- (67:24) [next to 67:22] قُلْ هُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
- (68:40) [next to 68:42] سَلْهُمْ أَيُّهُم بِذَٰلِكَ زَعِيمٌ
- (68:41) [next to 68:42] أَمْ لَهُمْ شُرَكَآءُ فَلْيَأْتُوا۟ بِشُرَكَآئِهِمْ إِن كَانُوا۟ صَٰدِقِينَ
- (68:44) [next to 68:42] فَذَرْنِى وَمَن يُكَذِّبُ بِهَٰذَا ٱلْحَدِيثِ ۖ سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ
- (68:45) [next to 68:43] وَأُمْلِى لَهُمْ ۚ إِنَّ كَيْدِى مَتِينٌ
- (75:5) [next to 75:7] بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ
- (75:6) [next to 75:7] يَسْـَٔلُ أَيَّانَ يَوْمُ ٱلْقِيَٰمَةِ
- (75:11) [next to 75:9] كَلَّا لَا وَزَرَ
- (75:12) [next to 75:10] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ
- (75:20) [next to 75:22] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
- (75:21) [next to 75:22] وَتَذَرُونَ ٱلْءَاخِرَةَ
- (75:26) [next to 75:24] كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ
- (75:27) [next to 75:25] وَقِيلَ مَنْ ۜ رَاقٍۢ
- (79:6) [next to 79:8] يَوْمَ تَرْجُفُ ٱلرَّاجِفَةُ
- (79:7) [next to 79:8] تَتْبَعُهَا ٱلرَّادِفَةُ
- (79:10) [next to 79:8] يَقُولُونَ أَءِنَّا لَمَرْدُودُونَ فِى ٱلْحَافِرَةِ
- (79:11) [next to 79:9] أَءِذَا كُنَّا عِظَٰمًۭا نَّخِرَةًۭ
- (80:31) [next to 80:33] وَفَٰكِهَةًۭ وَأَبًّۭا
- (80:32) [next to 80:33] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (80:34) [next to 80:33] يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ
- (80:35) [next to 80:33] وَأُمِّهِۦ وَأَبِيهِ
- (80:42) [next to 80:40] أُو۟لَٰٓئِكَ هُمُ ٱلْكَفَرَةُ ٱلْفَجَرَةُ
- (86:6) [next to 86:8] خُلِقَ مِن مَّآءٍۢ دَافِقٍۢ
- (86:7) [next to 86:8] يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ
- (86:10) [next to 86:8] فَمَا لَهُۥ مِن قُوَّةٍۢ وَلَا نَاصِرٍۢ
- (86:11) [next to 86:9] وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ

