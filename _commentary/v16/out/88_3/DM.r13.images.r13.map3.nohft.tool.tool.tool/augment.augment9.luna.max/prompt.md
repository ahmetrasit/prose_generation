Work only from this message and the lookup command it describes: read no file and run no other command.

Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:3; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_3.reading.tr.md (prose paragraphs numbered) =====
## Zamanı söylenmemiş bir emek

[¶1] İkinci ayet bazı yüzleri "o gün" eğik ve ezik olarak anmıştı. Üçüncü ayet aynı yüzlere iki sıfat daha ekler. İkisini de fiilsiz ve bağlaçsız, yan yana dizer: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışan, didinen ve bitkin düşen, source:88:3}. Sıfatlar "yüzler" kelimesine uyar. Ama altıncı ayet {ar:لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ, tr:leyse lehum taâmun illâ min darî', gloss:onlar için darîden başka yiyecek yoktur, source:88:6} derken "yüzler"den "onlar"a geçer. Böylece surenin kendisi, yüzün insanın bütünü yerine konduğunu gösterir. Çalışan da yorulan da yalnızca bir yüz değil, o yüzün sahibidir. Sure ise onu yüzüyle gösterir, çünkü emek ve yorgunluk en önce yüzde okunur.

[¶2] İki kelime de bir işi yapanın halini anlatan sıfat kalıbındadır, ama yanlarında zaman bildiren bir fiil yoktur. Zaman yalnızca ikinci ayetten gelen "o gün" sözündedir. Bu yüzden cümle iki biçimde okunabilir. Birinde yüzler o gün çalışmakta ve yorulmaktadır, yani emek azabın kendisidir. Ötekinde yüzler çalışmış, o gün ise bitkin düşmüştür, yani emek dünyada harcanmış, yorgunluğu o güne kalmıştır. Surenin kendi kuruluşu ikinci okumaya bir dayanak verir. Karşı taraftaki yüz için dokuzuncu ayet {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnut, source:88:9} der. O yüz geride kalmış bir çabaya bakıp sevinir. Bu tarafın emeği de geride kalmış bir emek gibi okunur, ama ona bakınca sevinç değil yorgunluk görülür. Kur'an'da azabın kendisinin bir zahmet olduğu da söylenir. Allah, kendisine uzayıp giden mal ve gözü önünde oğullar verdiği, sonra daha fazlasını umup ayetlere karşı direnen bir adamdan söz ederken şöyle der: {ar:سَأُرْهِقُهُۥ صَعُودًا, tr:se-urhikuhû saûdâ, gloss:onu sarp bir yokuşa sardıracağım, source:74:17}. Orada ceza bir tırmanıştır. Üçüncü ayetin sıfatları bu iki okumadan birini kapatmaz. Dünyada başlayıp o güne uzanan, aynı yüzde süren tek bir emek de anlatıyor olabilirler.

[¶3] İlk kelimenin kökü, rastgele bir hareketi değil, amaçla yapılan işi anlatır. Canlıdan kasıtla çıkan her iş böyle adlandırılır: {ar:كل فعل يكون من الحيوان بقصد, tr:küllü fi'lin yekûnu mine'l-hayevâni bi-kasd, gloss:canlıdan kasıtla çıkan her iş, source:"ع م ل,B001"}. Bu işin iyisi de kötüsü de aynı kelimeyle anılır: {ar:الأعمال الصالحة والسيئة, tr:el-a'mâlu's-sâlihatu ve's-seyyie, gloss:iyi ve kötü işler, source:"ع م ل,B001"}. Türkçede bu kökten iki kelime yaşar, ama ikisi de daralmıştır. "Amel" çoğunlukla "amel defteri" gibi dinî bir terime çekilmiştir. "Amele" ise yalnızca gündelikçi işçi demektir. Arapçada ikisi tek bir aileye aittir. Elleriyle kazı yapan, kuyu ören topluluğa da bu adın bir biçimi verilir: {ar:العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه, tr:el-amaletu'l-kavmu ya'melûne bi-eydîhim durûben mine'l-ameli hafran ev tayyen ev nahveh, gloss:elleriyle kazmak, kuyu örmek gibi türlü işler gören topluluk, source:"ع م ل,B006"}. Âmile kelimesinde bu yüzden iki şey birden duyulur. Biri, hesaba yazılacak olan bilerek yapılmış iştir. Öteki, kazma kürekle çalışan işçinin bedenine çöken yorgunluktur. Ayetin ikinci kelimesi bu ikinci yüzü öne çıkarır.

## Ayakta durmanın yorgunluğu

[¶4] Nâsıba kelimesinin ayetteki anlamı bitkinliktir. Bu kökün temelinde ise bir şeyi dikmek, dik tutmak vardır: {ar:أصل صحيح يدل على إقامة شيء وإهداف في استواء, tr:aslun sahîhun yedullü alâ ikâmeti şey'in ve ihdâfin fi'stivâ', gloss:bir şeyi dikip dimdik yükseltmeyi gösteren sağlam bir kök, source:"ن ص ب,B001"}; {ar:النصب رفعك شيئا تنصبه قائما منتصبا, tr:en-nasbu ref'uke şey'en tensıbuhû kâimen muntasıbâ, gloss:nasb, bir şeyi kaldırıp dimdik ayakta dikmendir, source:"ن ص ب,B001"}. Kökün aile içinde taşıdığı bu resim ayetin anlamının yerine geçmez, onun yanında duyulur. Bu ayetteki ve bundan sonraki bütün aile resimleri için de durum böyledir. Bu resim yorgunluğu da kendisi açıklar. Araplar yorgunluğa nasab derken bunun nedenini de söylerlerdi: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasıben hattâ yu'yî, gloss:nasab zahmettir; insanın tükenene dek ayakta dikilip durmasıdır, source:"ن ص ب,B004"}. Burada yorgunluk, bir direk gibi dik tutulan bedenin sonunda çözülmesidir. Ağır bir yük kaldırmanın ani yorgunluğu değildir. Durmadan, oturmadan, ara vermeden ayakta kalmanın yavaş yavaş biriken tükenişidir.

[¶5] Bu kelime yalnızca işin yorgunluğunu anlatmaz. Hastalık için {ar:نصب الداء, tr:nasabu'd-dâ', gloss:hastalığın verdiği bitkinlik, source:"ن ص ب,B004"} denir. Yüze iz bırakan keder de bu adla anılır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bıraktığında keder, source:"ن ص ب,B004"}. Yorgunluğa huzursuzluk da karışır: {ar:أنصبني كذا أي أتعبني وأزعجني, tr:ensabenî kezâ ey et'abenî ve ez'acenî, gloss:şu beni yordu ve tedirgin etti, source:"ن ص ب,B004"}. Böylece nâsıba, işin bittiği yerde bitmeyen, yüzde kalan bir tükenmişliktir. Kelime iki yöne de okunabilir. Hem yorgunluk içinde olanı hem de yorgunluk vereni anlatır {source:"ن ص ب,B004"}. Araplar insanı yoran bir tasaya da {ar:هَمٌّ ناصِبٌ, tr:hemmun nâsıb, gloss:yorup bitiren tasa, source:"memory"} derlerdi. Ayetteki yüz yorgundur, ama sıfatın bu ikinci yönü emeğin kendisinin de yorucu olduğunu duyurur. Yüz, onu tüketen işle bir olmuştur.

[¶6] Kök surede bir kez daha geçer. Bu sefer insan için değil dağlar için kullanılır: {ar:وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ, tr:ve ile'l-cibâli keyfe nusibet, gloss:dağlara da bakmazlar mı, nasıl dikilmiş, source:88:19}. Bu iki kelime arasında bir benzetme değil, kök birliği vardır. On dokuzuncu ayette fiil edilgendir. Dağı biri dikmiştir ve dağ dikildiği yerde yorulmadan durur. Üçüncü ayetteki yüz ise kendi başına ayakta dikilmiş ve dikildiği yerde tükenmiştir. Yorgunluğun tanımındaki "tükenene dek dik durmak" sözü, iki kullanımın arasındaki farkı da gösterir. Dik durmak dağın doğasıdır, insanın ise yorgunluğudur. Bu karşılaştırma surenin kelimelerinden çıkan bir yorumdur, sure onu açıkça kurmaz. Ama on yedinci ayetten itibaren bakış devye, göğe, dağlara ve yere çevrildiğinde, dağların "nasıl dikildiği" sorusu, ayakta durmanın ne pahalıya geldiğini görmüş bir okura sorulmuş olur. Dört nesneye bakışın bütün sahnesi on yedinci ve yirminci ayetler arasındadır. Bu ayetin payı, dağın dikiliş fiilini kendi yorgunluk kelimesinde taşımasıdır.

[¶7] Kökün dikili taşlara verdiği adlar da bu resmi tamamlar. Araplar dikilip tapınılan, üstüne kurban kanı dökülen taşa nusub derlerdi: {ar:النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام, tr:en-nusubu hacerun kâne yunsabu fe-yu'bedu ve tusabbu aleyhi dimâu'z-zebâihi li'l-esnâm, gloss:dikilip tapınılan ve üstüne putlar için kesilen hayvanların kanı dökülen taş, source:"ن ص ب,B002"}. Kutsal bölgenin sınırını gösteren taşlar da kuyunun ağzına dizilen taşlar da aynı fiille adlandırılırdı: {ar:أنصاب الحرم حجارة تنصب لتعرف حدوده بها, tr:ensâbu'l-harem hicâratun tunsabu li-tu'rafe hudûduhû bihâ, gloss:harem sınırları bilinsin diye dikilen taşlar, source:"ن ص ب,B003"}; {ar:النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد, tr:en-nesâibu hicâratun tunsabu havâlay şefîri'l-bi'ri fe-tuc'alu adâid, gloss:kuyu ağzının çevresine dikilip destek yapılan taşlar, source:"ن ص ب,B003"}. Kur'an da Allah'ın haram kıldığı yiyecekleri sayarken bu taşı anar: {ar:وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ, tr:ve mâ zubiha ale'n-nusub, gloss:dikili taşlar üzerinde kesilen, source:5:3}. Aynı taş, Meâric suresinde o günün sahnesine girer. Allah Peygamber'e, kendilerine vaat edilen güne kavuşuncaya kadar inkârcıları dalıp oynamaya bırakmasını söyler {source:70:42}, sonra o günü anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâan ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları gün, sanki dikili bir işarete koşuyormuş gibidirler, source:70:43}; {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik, kendilerini aşağılanma bürümüş, source:70:44}. O sahnede de ikinci ayetin eğiklik kelimesi ile üçüncü ayetin kökü yan yanadır. Orada kök dikili taşı, burada yorgunluğu anlatır. Anlamlar farklıdır, kök aynıdır. Bir sahnede insanlar dikili bir taşa doğru koşar. Gâşiye'de ise dikilip duran ve tükenen şey, insanın kendisidir.

## İşi taşıyan uzuvlar

[¶8] Araplar âmile kelimesini bir bütünün işi yüklenen parçası için de kullanırlardı. Bu kullanımda ayetin kelimesi tıpatıp geçer: {ar:عوامل الدابة قوائمه واحدها عاملة, tr:avâmilu'd-dâbbeti kavâimuhû vâhiduhâ âmile, gloss:hayvanın ayaklarına avâmil denir, tekili âmiledir, source:"ع م ل,B010"}. Binek hayvanının bacakları onun "çalışanları"dır. Yükü taşıyan, yolu tüketen, yorgunluğu ilk duyan onlardır. Uzağa bakan göze de aynı ad verilirdi: {ar:وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر, tr:ve terkubuhû bi-âmiletin kazûf ey terkubuhû bi-aynin baîdeti'n-nazar, gloss:onu uzağı gören bir gözle gözetler, source:"ع م ل,B010"}. Mızrakta da işi gören parçanın adı aynıdır: {ar:عامل الرمح ما يلي السنان, tr:âmilu'r-rumhi mâ yeli's-sinân, gloss:mızrağın âmili, demir ucun hemen arkasındaki kısımdır, source:"ع م ل,B009"}. Bu kısım mızrağın göğsü sayılırdı {source:"ع م ل,B009"}. Saplanan demir uçtur, ama vuruşun ağırlığını uca ileten, darbeyi taşıyan, ucun arkasındaki bu gövdedir. Bu adlandırmaların hepsinde âmile, bütünün emeği yüklenen organıdır. Üçüncü ayette bu sıfatı alan da yüzdür. Bu da yüzün bütün bir hayatın emeğini taşıyan organ haline geldiğini düşündürür. Bu bir yorumdur. Ama ikinci ayette eğilen, üçüncü ayette çalışıp yorulan hep aynı yüzdür.

[¶9] Kök, işe yaratılmış canlıyı da adlandırır. Soylu, güçlü ve işe yatkın dişi deveye ya'mele denirdi: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletu'n-nâkatu'n-necîbetu'l-matbûatu ale'l-amel, gloss:yaratılıştan işe yatkın soylu dişi deve, source:"ع م ل,B008"}. İşe yatkın insan için de aynı söz söylenir: {ar:رجل عمل بكسر الميم أي مطبوع على العمل, tr:raculun amil bi-kesri'l-mîm ey matbûun ale'l-amel, gloss:amil, işe yaratılmış adamdır, source:"ع م ل,B008"}. İşe koşulan sığırlar da bu kökle anılır {source:"ع م ل,B001"}. Kelime koşum hayvanının dünyasından gelir. Âmile, sürekli koşulan, yük altında tutulan bir canlının sıfatı gibi duyulur. Kökün kalıplaşmış bir sözünde iş doğrudan zahmet anlamına da gelir: {ar:سوف أتعمل في حاجتك أي أتعنى, tr:sevfe eteammelu fî hâcetike ey eteannâ, gloss:ihtiyacın için zahmete gireceğim, source:"ع م ل,B007"}; {ar:لا تتعمل في أمرك ذا كقولك لا تتعن, tr:lâ teteammel fî emrike zâ ke-kavlike lâ teteanna, gloss:bu işte kendini yorma, source:"ع م ل,B007"}. Böylece ayetin iki kelimesi birbirine zaten yaslanır. Biri işi anlatır ama zahmete kayar. Öteki zahmeti anlatır ve onu ayakta çalışmaya bağlar.

[¶10] İki kökün aile resimleri bir yolculuk gününde de buluşur. Çok yürünmüş, iz bırakmış yol için {ar:طريق معمل أي لحب مسلوك, tr:tarîkun mu'mel ey lahbun meslûk, gloss:çok yürünmekten belirginleşmiş yol, source:"ع م ل,B011"} denirdi. Yol da ayaklar tarafından "işlenmiş"tir. Yürüyerek yolculuk edenlere de bu kökten bir ad verilirdi: {ar:المسافرون إذا مشوا على أرجلهم يسمون بني العمل, tr:el-musâfirûne izâ meşev alâ erculihim yusemmevne benî'l-amel, gloss:yolcular yaya yürüdüklerinde benü'l-amel diye anılır, source:"ع م ل,B012"}. Nasab kökü ise bütün gün süren yumuşak yürüyüşe ad verir: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yol aldı, source:"ن ص ب,B010"}. Yolda söylenen bir türküye de bu ad verilirdi: {ar:غناء لهم يشبه الحداء إلا أنه أرق منه, tr:ğınâun lehum yuşbihu'l-hudâe illâ ennehû erakku minh, gloss:deve sürücülerinin türküsüne benzeyen ama ondan daha yumuşak bir ezgi, source:"ن ص ب,B009"}. Kelimelerin dünyasında bir günlük yürüyüşün bütün parçaları vardır: çalışan bacaklar, işlenmiş yol, gün boyu süren yumuşak adım ve yolu kısaltan ezgi. Ayette bunlardan yalnızca yolun sonundaki bitkinlik kalmıştır. Kur'an nasab kelimesini yolculuğun yorgunluğu için de kullanır. Musa, genç yol arkadaşına iki denizin birleştiği yere varıncaya kadar durmayacağını söylemişti {source:18:60}. Oraya vardıklarında balıklarını unuttular ve balık denizde yolunu tuttu {source:18:61}. Orayı geçince Musa şöyle dedi: {ar:ءَاتِنَا غَدَآءَنَا لَقَدْ لَقِينَا مِن سَفَرِنَا هَٰذَا نَصَبًۭا, tr:âtinâ ğadâenâ lekad lakînâ min seferinâ hâzâ nasabâ, gloss:kuşluk yemeğimizi getir, bu yolculuğumuzdan gerçekten yorgunluk gördük, source:18:62}. Orada yorgunluğun hemen yanında onu giderecek yemek vardır. Gâşiye'de ise yorgunluğun ardından gelen yemek, yedinci ayetin dediği gibi {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besler ne açlığı giderir, source:88:7} bir yiyecektir. Bu yürüyüş resmini sure, on yedinci ayetteki devede bir bütün olarak kurar. İlk ayetin "geldi mi" fiilinden yirmi beşinci ayetin "dönüş" kelimesine uzanan yol oradadır.

## Ücreti yorgunluk olan iş

[¶11] Arapçada işin karşılığı da aynı köktendir. Araplar işçinin ücretine umâle derlerdi: {ar:العمالة أجر ما عمل, tr:el-umâletu ecru mâ amel, gloss:umâle yapılan işin ücretidir, source:"ع م ل,B004"}; {ar:العمالة بالضم رزق العامل, tr:el-umâletu bi'd-damm rızku'l-âmil, gloss:umâle işçinin rızkıdır, source:"ع م ل,B004"}. Âmile kelimesi bu yüzden, karşılığını bekleyen biri olarak duyulur. Nasab kökü de pay anlamını taşır, ve payı dikme fiiliyle açıklar: {ar:النصيب الحظ المنصوب أي المعين, tr:en-nasîbu'l-hazzu'l-mansûbu eyi'l-muayyen, gloss:nasip, dikilmiş yani belirlenmiş paydır, source:"ن ص ب,B005"}. Pay, sınır taşı gibi dikilip işaretlenmiş bir bölümdür. Türkçede "nasip" kelimesi kadere ve şansa kaymıştır. Arapçada ise önceden bölünüp işaretlenmiş, kime düştüğü belli olan bir hissedir. Ayetteki anlam yorgunluktur, ama yanında pay da duyulur. Bu yüz çalışmış, karşılığında eline geçen pay ise yorgunluğun kendisi olmuştur. İşçinin rızkı demek olan ücret burada, altıncı ve yedinci ayetlerde doyurmayan bir yiyecek olarak gelir. Bu ücret ve pay resmini sure dokuzuncu ayetteki çaba ve son ayetteki hesap ile bütünler.

[¶12] Kur'an aynı kelimeyle, hiçbir işçinin emeğinin kaybolmayacağını da söyler. Âl-i İmrân suresinde, göklerin ve yerin yaratılışını düşünen, Allah'ı ayakta, otururken ve yanları üstünde anan kişiler {source:3:191} Rablerine dua eder. Ayet, Rablerinin onlara cevabını şöyle verir: {ar:أَنِّى لَآ أُضِيعُ عَمَلَ عَٰمِلٍۢ مِّنكُم مِّن ذَكَرٍ أَوْ أُنثَىٰ, tr:ennî lâ udîu amele âmilin minkum min zekerin ev unsâ, gloss:ben sizden erkek olsun kadın olsun hiçbir çalışanın işini boşa çıkarmam, source:3:195}. O ayette âmil kelimesi ile üçüncü ayetteki âmile aynı kalıptan gelir. Orada çalışanın işi korunur. Burada ise işçi de vardır, iş de vardır, ama geriye yalnızca yorgunluk kalmıştır.

[¶13] Kur'an, kaybolan emeği somut resimlerle anlatır. Bunların biri beşinci ayetteki içirme ile son ayetteki hesabı aynı sahnede toplar: {ar:وَٱلَّذِينَ كَفَرُوٓا۟ أَعْمَٰلُهُمْ كَسَرَابٍۭ بِقِيعَةٍۢ يَحْسَبُهُ ٱلظَّمْـَٔانُ مَآءً حَتَّىٰٓ إِذَا جَآءَهُۥ لَمْ يَجِدْهُ شَيْـًۭٔا وَوَجَدَ ٱللَّهَ عِندَهُۥ فَوَفَّىٰهُ حِسَابَهُۥ, tr:vellezîne keferû a'mâluhum ke-serâbin bi-kîatin yahsebuhu'z-zam'ânu mâen hattâ izâ câehû lem yecidhu şey'en ve vecedallâhe indehû fe-veffâhu hısâbeh, gloss:inkâr edenlerin işleri düz bir arazideki serap gibidir; susamış kişi onu su sanır, yanına varınca hiçbir şey bulamaz, yanında Allah'ı bulur, O da hesabını tam öder, source:24:39}. İşler bir susuzun önündeki serap gibidir. Uzaktan su gibi görünür, yaklaşıldıkça yok olur. Yolun sonunda su yerine hesap bulunur. Gâşiye'nin yorgun yüzüne de beşinci ayette içecek verilir, ama bu içecek kaynamış bir pınardandır. Furkân suresinde de kendileriyle karşılaşmayı ummayanların melekleri görecekleri gün için {ar:لَا بُشْرَىٰ يَوْمَئِذٍۢ لِّلْمُجْرِمِينَ, tr:lâ buşrâ yevmeizin li'l-mucrimîn, gloss:o gün suçlulara hiçbir müjde yoktur, source:25:22} denir. Hemen ardından işin ne olduğu söylenir: {ar:وَقَدِمْنَآ إِلَىٰ مَا عَمِلُوا۟ مِنْ عَمَلٍۢ فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا, tr:ve kadimnâ ilâ mâ amilû min amelin fe-cealnâhu hebâen mensûrâ, gloss:yaptıkları her işe yöneldik ve onu savrulmuş toz zerrelerine çevirdik, source:25:23}. Buradaki "o gün" ikinci ayetteki "o gün" ile aynı kelimedir. Emek dağılıp gider, yorgunluk ise çalışanın üstünde kalır. Kur'an aynı şeyi bir hesap cümlesiyle de söyler: {ar:قُلْ هَلْ نُنَبِّئُكُم بِٱلْأَخْسَرِينَ أَعْمَٰلًا, tr:kul hel nunebbiukum bi'l-ahserîne a'mâlâ, gloss:de ki: işleri bakımından en çok kaybedenleri size haber vereyim mi, source:18:103}. İşi en çok kaybettiren şey, işin azlığı değildir. Ardından gelen ayete göre bu insanlar çabalarının boşa gittiğini bilmeden güzel iş yaptıklarını sanır {source:18:104}.

[¶14] Ateşe girişin kendisi de işle bağlanır. Cehenneme itilenlere, inkâr ettikleri ateş gösterilir {source:52:14} ve şöyle denir: {ar:ٱصْلَوْهَا فَٱصْبِرُوٓا۟ أَوْ لَا تَصْبِرُوا۟ سَوَآءٌ عَلَيْكُمْ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ, tr:islevhâ fasbirû ev lâ tasbirû sevâun aleykum innemâ tuczevne mâ kuntum ta'melûn, gloss:girin oraya; ister katlanın ister katlanmayın, sizin için birdir; yalnızca yaptıklarınızın karşılığını görüyorsunuz, source:52:16}. Bu ayetteki "girin" emri, dördüncü ayetteki {ar:تَصْلَىٰ, tr:taslâ, gloss:girer, source:88:4} fiiliyle aynı köktendir. "Yaptıklarınız" ise âmile ile aynı köktendir. Gâşiye'de bu iki kelime komşu ayetlerde art arda gelir: önce çalışan ve yorulan yüz, sonra kızgın ateşe giren yüz. Bu sıra, ateşin işe verilmiş bir ücret gibi geldiğini gösterir.

## İki yorgunluk

[¶15] Yorgunluğun kendisi bir kayıp işareti değildir. Kur'an aynı kelimeyi, karşılığı yazılan bir zahmet için de kullanır. Tevbe suresinde, çevredeki bedevilerin ve şehir halkının Allah'ın elçisinden geri kalmaması gerektiği söylenir ve gerekçesi şöyle verilir: {ar:ذَٰلِكَ بِأَنَّهُمْ لَا يُصِيبُهُمْ ظَمَأٌۭ وَلَا نَصَبٌۭ وَلَا مَخْمَصَةٌۭ فِى سَبِيلِ ٱللَّهِ, tr:zâlike bi-ennehum lâ yusîbuhum zameun ve lâ nasabun ve lâ mahmasatun fî sebîlillâh, gloss:çünkü Allah yolunda onlara dokunan hiçbir susuzluk, yorgunluk ve açlık yoktur ki, source:9:120}. Cümle şöyle tamamlanır: {ar:إِلَّا كُتِبَ لَهُم بِهِۦ عَمَلٌۭ صَٰلِحٌ ۚ إِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ, tr:illâ kutibe lehum bihî amelun sâlih innallâhe lâ yudîu ecra'l-muhsinîn, gloss:onun karşılığında kendilerine iyi bir iş yazılmış olmasın; Allah iyilik yapanların ücretini boşa çıkarmaz, source:9:120}. Bu ayette üç zahmet sayılır: susuzluk, yorgunluk ve açlık. Gâşiye'nin üçüncü ile yedinci ayetleri arasında da aynı üçlü vardır. Üçüncü ayette yorgunluk, beşinci ayette kaynamış pınardan içirilen bir susuzluk, yedinci ayette giderilmeyen bir açlık geçer. Tevbe'de bu üç zahmetin her biri iyi bir iş olarak yazılır ve ücreti korunur. Orada yorgunluk, âmile kökünden bir "iş" olur. Burada ise işin kendisi yorgunluğa dönmüştür. İki sahnede de çalışan bir insan ve onun yorgunluğu vardır. Ayıran şey yorgunluğun neyin hesabına yazıldığıdır.

[¶16] Kur'an aynı kökten bir emri doğrudan Peygamber'e de verir. İnşirâh suresinde, güçlükle birlikte bir kolaylık olduğu iki kez söylendikten sonra {source:94:6} şöyle denir: {ar:فَإِذَا فَرَغْتَ فَٱنصَبْ, tr:fe-izâ ferağte fensab, gloss:bir işten boşaldığında hemen kalk ve yorul, source:94:7}; {ar:وَإِلَىٰ رَبِّكَ فَٱرْغَب, tr:ve ilâ rabbike farğab, gloss:ve yalnız Rabbine yönel, source:94:8}. Orada yorgunluk istenen bir şeydir, ama yönü bellidir: Rabbe doğru. Bu kelimelerin ibadetin duruşlarını da taşıdığı ve ikinci, üçüncü ve dördüncü ayetleri rükû, kıyam ve namazla buluşturduğu sahne, surenin bütününde bu ayetin yorgunluk kelimesi üzerinden kurulur.

[¶17] Bahçe ise yorgunluğun bittiği yerdir. Kitaba mirasçı kılınanlar Adn bahçelerine girer {source:35:33}. Önce Allah'a hamdederek kederi kendilerinden giderdiğini söylerler: {ar:ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَذْهَبَ عَنَّا ٱلْحَزَنَ, tr:el-hamdu lillâhi'llezî ezhebe anne'l-hazen, gloss:kederi bizden gideren Allah'a hamd olsun, source:35:34}. Ardından şöyle derler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne de bitkinlik, source:35:35}. Aynı konuşmada önce keder sonra nasab anılır. Nasab kökü yüze iz bırakan kederi de adlandırıyordu. Bahçe halkının diliyle bu iki şeyin birlikte kalkması, üçüncü ayetteki kelimenin iki yüzünün birlikte kalkmasıdır. Gâşiye'nin kendi dengesi de böyledir. Bir yüz emeğine bakar ve ondan razı olur. Öteki yüz de emeğine bakar, ama orada yalnızca kendi yorgunluğunu bulur. İkisi de çalışmıştır. Fark, emeğin bir pay olarak dikilip yazılması ile yüzün kendisinin, dikildiği yerde tükenen bir direk gibi kalmasıdır.

===== _commentary/v16/out/88_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: hamm nāṣib (a wearying care) as attested Arabic usage
- memory: active participle without a verb carries no fixed tense
- memory: Turkish "amele" derives from Arabic ʿamala (labourers)
- not written: ن ص ب B001 snare-setting (nasabtu lil-qaṭāt) - hunting scene belongs to the surah commentary's fire section, no fresh theme here
- not written: ن ص ب B001 trivet for the pot - cooking scene is the surah commentary's; would only repeat it
- not written: ن ص ب B006 niṣāb (base, knife hilt, zakat threshold) - no tie to fatigue or work here
- not written: ن ص ب B007 grammatical naṣb - technical, no theme
- not written: ن ص ب B008 nāṣaba al-ḥarb (hostility) - different verb form; link to 88:23 too thin
- not written: ع م ل B002/B003 employing, officials, alms collectors - no support in the ayah's scene
- not written: ع م ل B005 muʿāmala (transaction) - wage theme already carried by B004
- not written: 14:18 works like ashes in the wind - repeats 25:23's image
- not written: 39:39 "innī ʿāmil" - adds nothing beyond 3:195

===== passages not cited (212) =====
## strong (this ayah's own list) (51)

- (3:195) [listed for 88:3] [cited in ¶12] فَٱسْتَجَابَ لَهُمْ رَبُّهُمْ أَنِّى لَآ أُضِيعُ عَمَلَ عَٰمِلٍۢ مِّنكُم مِّن ذَكَرٍ أَوْ أُنثَىٰ ۖ بَعْضُكُم مِّنۢ بَعْضٍۢ ۖ فَٱلَّذِينَ هَاجَرُوا۟ وَأُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأُوذُوا۟ فِى سَبِيلِى وَقَٰتَلُوا۟ وَقُتِلُوا۟ لَأُكَفِّرَنَّ عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأُدْخِلَنَّهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ثَوَابًۭا مِّنْ عِندِ ٱللَّهِ ۗ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلثَّوَابِ
- (9:105) [listed for 88:3] وَقُلِ ٱعْمَلُوا۟ فَسَيَرَى ٱللَّهُ عَمَلَكُمْ وَرَسُولُهُۥ وَٱلْمُؤْمِنُونَ ۖ وَسَتُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (9:120) [listed for 88:3] [cited in ¶15] مَا كَانَ لِأَهْلِ ٱلْمَدِينَةِ وَمَنْ حَوْلَهُم مِّنَ ٱلْأَعْرَابِ أَن يَتَخَلَّفُوا۟ عَن رَّسُولِ ٱللَّهِ وَلَا يَرْغَبُوا۟ بِأَنفُسِهِمْ عَن نَّفْسِهِۦ ۚ ذَٰلِكَ بِأَنَّهُمْ لَا يُصِيبُهُمْ ظَمَأٌۭ وَلَا نَصَبٌۭ وَلَا مَخْمَصَةٌۭ فِى سَبِيلِ ٱللَّهِ وَلَا يَطَـُٔونَ مَوْطِئًۭا يَغِيظُ ٱلْكُفَّارَ وَلَا يَنَالُونَ مِنْ عَدُوٍّۢ نَّيْلًا إِلَّا كُتِبَ لَهُم بِهِۦ عَمَلٌۭ صَٰلِحٌ ۚ إِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
- (11:15) [listed for 88:3] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
- (11:16) [listed for 88:3] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
- (14:18) [listed for 88:3] مَّثَلُ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ ۖ لَّا يَقْدِرُونَ مِمَّا كَسَبُوا۟ عَلَىٰ شَىْءٍۢ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
- (15:48) [listed for 88:3] لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ وَمَا هُم مِّنْهَا بِمُخْرَجِينَ
- (17:18) [listed for 88:3] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
- (17:19) [listed for 88:3] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
- (18:103) [listed for 88:3] [cited in ¶13] قُلْ هَلْ نُنَبِّئُكُم بِٱلْأَخْسَرِينَ أَعْمَٰلًا
- (18:104) [listed for 88:3] [cited in ¶13] ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا
- (18:105) [listed for 88:3] أُو۟لَٰٓئِكَ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ وَلِقَآئِهِۦ فَحَبِطَتْ أَعْمَٰلُهُمْ فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا
- (20:15) [listed for 88:3] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (23:102) [listed for 88:3] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (23:103) [listed for 88:3] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (24:39) [listed for 88:3] [cited in ¶13] وَٱلَّذِينَ كَفَرُوٓا۟ أَعْمَٰلُهُمْ كَسَرَابٍۭ بِقِيعَةٍۢ يَحْسَبُهُ ٱلظَّمْـَٔانُ مَآءً حَتَّىٰٓ إِذَا جَآءَهُۥ لَمْ يَجِدْهُ شَيْـًۭٔا وَوَجَدَ ٱللَّهَ عِندَهُۥ فَوَفَّىٰهُ حِسَابَهُۥ ۗ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
- (25:23) [listed for 88:3] [cited in ¶13] وَقَدِمْنَآ إِلَىٰ مَا عَمِلُوا۟ مِنْ عَمَلٍۢ فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا
- (28:84) [listed for 88:3] مَن جَآءَ بِٱلْحَسَنَةِ فَلَهُۥ خَيْرٌۭ مِّنْهَا ۖ وَمَن جَآءَ بِٱلسَّيِّئَةِ فَلَا يُجْزَى ٱلَّذِينَ عَمِلُوا۟ ٱلسَّيِّـَٔاتِ إِلَّا مَا كَانُوا۟ يَعْمَلُونَ
- (29:7) [listed for 88:3] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُكَفِّرَنَّ عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَنَجْزِيَنَّهُمْ أَحْسَنَ ٱلَّذِى كَانُوا۟ يَعْمَلُونَ
- (29:69) [listed for 88:3] وَٱلَّذِينَ جَٰهَدُوا۟ فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا ۚ وَإِنَّ ٱللَّهَ لَمَعَ ٱلْمُحْسِنِينَ
- (32:17) [listed for 88:3] فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (35:10) [listed for 88:3] مَن كَانَ يُرِيدُ ٱلْعِزَّةَ فَلِلَّهِ ٱلْعِزَّةُ جَمِيعًا ۚ إِلَيْهِ يَصْعَدُ ٱلْكَلِمُ ٱلطَّيِّبُ وَٱلْعَمَلُ ٱلصَّٰلِحُ يَرْفَعُهُۥ ۚ وَٱلَّذِينَ يَمْكُرُونَ ٱلسَّيِّـَٔاتِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۖ وَمَكْرُ أُو۟لَٰٓئِكَ هُوَ يَبُورُ
- (35:35) [listed for 88:3] [cited in ¶17] ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ
- (36:54) [listed for 88:3] فَٱلْيَوْمَ لَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا وَلَا تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (39:65) [listed for 88:3] وَلَقَدْ أُوحِىَ إِلَيْكَ وَإِلَى ٱلَّذِينَ مِن قَبْلِكَ لَئِنْ أَشْرَكْتَ لَيَحْبَطَنَّ عَمَلُكَ وَلَتَكُونَنَّ مِنَ ٱلْخَٰسِرِينَ
- (39:70) [listed for 88:3] وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُوَ أَعْلَمُ بِمَا يَفْعَلُونَ
- (40:17) [listed for 88:3] ٱلْيَوْمَ تُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ ۚ لَا ظُلْمَ ٱلْيَوْمَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (45:22) [listed for 88:3] وَخَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَلِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (46:19) [listed for 88:3] وَلِكُلٍّۢ دَرَجَٰتٌۭ مِّمَّا عَمِلُوا۟ ۖ وَلِيُوَفِّيَهُمْ أَعْمَٰلَهُمْ وَهُمْ لَا يُظْلَمُونَ
- (47:28) [listed for 88:3] ذَٰلِكَ بِأَنَّهُمُ ٱتَّبَعُوا۟ مَآ أَسْخَطَ ٱللَّهَ وَكَرِهُوا۟ رِضْوَٰنَهُۥ فَأَحْبَطَ أَعْمَٰلَهُمْ
- (53:39) [listed for 88:3] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
- (53:40) [listed for 88:3] وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ
- (53:41) [listed for 88:3] ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ
- (67:2) [listed for 88:3] ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
- (76:22) [listed for 88:3] إِنَّ هَٰذَا كَانَ لَكُمْ جَزَآءًۭ وَكَانَ سَعْيُكُم مَّشْكُورًا
- (79:35) [listed for 88:3] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (84:6) [listed for 88:3] يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ
- (90:4) [listed for 88:3] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- (92:4) [listed for 88:3] إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- (92:5) [listed for 88:3] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (92:6) [listed for 88:3] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:7) [listed for 88:3] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (92:8) [listed for 88:3] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- (92:9) [listed for 88:3] وَكَذَّبَ بِٱلْحُسْنَىٰ
- (92:10) [listed for 88:3] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (94:4) [listed for 88:3] وَرَفَعْنَا لَكَ ذِكْرَكَ
- (94:7) [listed for 88:3] [cited in ¶16] فَإِذَا فَرَغْتَ فَٱنصَبْ
- (94:8) [listed for 88:3] [cited in ¶16] وَإِلَىٰ رَبِّكَ فَٱرْغَب
- (99:7) [listed for 88:3] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- (99:8) [listed for 88:3] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
- (103:3) [listed for 88:3] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ

## medium (this ayah's own list) (80)

- (2:217) [listed for 88:3] يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ ۖ وَصَدٌّ عَن سَبِيلِ ٱللَّهِ وَكُفْرٌۢ بِهِۦ وَٱلْمَسْجِدِ ٱلْحَرَامِ وَإِخْرَاجُ أَهْلِهِۦ مِنْهُ أَكْبَرُ عِندَ ٱللَّهِ ۚ وَٱلْفِتْنَةُ أَكْبَرُ مِنَ ٱلْقَتْلِ ۗ وَلَا يَزَالُونَ يُقَٰتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ ٱسْتَطَٰعُوا۟ ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِۦ فَيَمُتْ وَهُوَ كَافِرٌۭ فَأُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:264) [listed for 88:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (2:286) [listed for 88:3] لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا ٱكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَآ إِصْرًۭا كَمَا حَمَلْتَهُۥ عَلَى ٱلَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِۦ ۖ وَٱعْفُ عَنَّا وَٱغْفِرْ لَنَا وَٱرْحَمْنَآ ۚ أَنتَ مَوْلَىٰنَا فَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (3:22) [listed for 88:3] أُو۟لَٰٓئِكَ ٱلَّذِينَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (3:136) [listed for 88:3] أُو۟لَٰٓئِكَ جَزَآؤُهُم مَّغْفِرَةٌۭ مِّن رَّبِّهِمْ وَجَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (4:32) [listed for 88:3] وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ ۚ لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبُوا۟ ۖ وَلِلنِّسَآءِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبْنَ ۚ وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (4:124) [listed for 88:3] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ مِن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ نَقِيرًۭا
- (5:9) [listed for 88:3] وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ ۙ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌ عَظِيمٌۭ
- (7:147) [listed for 88:3] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا وَلِقَآءِ ٱلْءَاخِرَةِ حَبِطَتْ أَعْمَٰلُهُمْ ۚ هَلْ يُجْزَوْنَ إِلَّا مَا كَانُوا۟ يَعْمَلُونَ
- (9:16) [listed for 88:3] أَمْ حَسِبْتُمْ أَن تُتْرَكُوا۟ وَلَمَّا يَعْلَمِ ٱللَّهُ ٱلَّذِينَ جَٰهَدُوا۟ مِنكُمْ وَلَمْ يَتَّخِذُوا۟ مِن دُونِ ٱللَّهِ وَلَا رَسُولِهِۦ وَلَا ٱلْمُؤْمِنِينَ وَلِيجَةًۭ ۚ وَٱللَّهُ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (9:17) [listed for 88:3] مَا كَانَ لِلْمُشْرِكِينَ أَن يَعْمُرُوا۟ مَسَٰجِدَ ٱللَّهِ شَٰهِدِينَ عَلَىٰٓ أَنفُسِهِم بِٱلْكُفْرِ ۚ أُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ وَفِى ٱلنَّارِ هُمْ خَٰلِدُونَ
- (9:69) [listed for 88:3] كَٱلَّذِينَ مِن قَبْلِكُمْ كَانُوٓا۟ أَشَدَّ مِنكُمْ قُوَّةًۭ وَأَكْثَرَ أَمْوَٰلًۭا وَأَوْلَٰدًۭا فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ فَٱسْتَمْتَعْتُم بِخَلَٰقِكُمْ كَمَا ٱسْتَمْتَعَ ٱلَّذِينَ مِن قَبْلِكُم بِخَلَٰقِهِمْ وَخُضْتُمْ كَٱلَّذِى خَاضُوٓا۟ ۚ أُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (10:14) [listed for 88:3] ثُمَّ جَعَلْنَٰكُمْ خَلَٰٓئِفَ فِى ٱلْأَرْضِ مِنۢ بَعْدِهِمْ لِنَنظُرَ كَيْفَ تَعْمَلُونَ
- (12:107) [listed for 88:3] أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ
- (14:51) [listed for 88:3] لِيَجْزِىَ ٱللَّهُ كُلَّ نَفْسٍۢ مَّا كَسَبَتْ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (15:93) [listed for 88:3] عَمَّا كَانُوا۟ يَعْمَلُونَ
- (16:25) [listed for 88:3] لِيَحْمِلُوٓا۟ أَوْزَارَهُمْ كَامِلَةًۭ يَوْمَ ٱلْقِيَٰمَةِ ۙ وَمِنْ أَوْزَارِ ٱلَّذِينَ يُضِلُّونَهُم بِغَيْرِ عِلْمٍ ۗ أَلَا سَآءَ مَا يَزِرُونَ
- (16:56) [listed for 88:3] وَيَجْعَلُونَ لِمَا لَا يَعْلَمُونَ نَصِيبًۭا مِّمَّا رَزَقْنَٰهُمْ ۗ تَٱللَّهِ لَتُسْـَٔلُنَّ عَمَّا كُنتُمْ تَفْتَرُونَ
- (16:96) [listed for 88:3] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (16:97) [listed for 88:3] مَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَلَنُحْيِيَنَّهُۥ حَيَوٰةًۭ طَيِّبَةًۭ ۖ وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (18:30) [listed for 88:3] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ إِنَّا لَا نُضِيعُ أَجْرَ مَنْ أَحْسَنَ عَمَلًا
- (18:62) [listed for 88:3] [cited in ¶10] فَلَمَّا جَاوَزَا قَالَ لِفَتَىٰهُ ءَاتِنَا غَدَآءَنَا لَقَدْ لَقِينَا مِن سَفَرِنَا هَٰذَا نَصَبًۭا
- (19:76) [listed for 88:3] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
- (20:112) [listed for 88:3] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا يَخَافُ ظُلْمًۭا وَلَا هَضْمًۭا
- (21:47) [listed for 88:3] وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ فَلَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا ۖ وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا ۗ وَكَفَىٰ بِنَا حَٰسِبِينَ
- (21:94) [listed for 88:3] فَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا كُفْرَانَ لِسَعْيِهِۦ وَإِنَّا لَهُۥ كَٰتِبُونَ
- (23:51) [listed for 88:3] يَٰٓأَيُّهَا ٱلرُّسُلُ كُلُوا۟ مِنَ ٱلطَّيِّبَٰتِ وَٱعْمَلُوا۟ صَٰلِحًا ۖ إِنِّى بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (28:77) [listed for 88:3] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (32:19) [listed for 88:3] أَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ جَنَّٰتُ ٱلْمَأْوَىٰ نُزُلًۢا بِمَا كَانُوا۟ يَعْمَلُونَ
- (32:20) [listed for 88:3] وَأَمَّا ٱلَّذِينَ فَسَقُوا۟ فَمَأْوَىٰهُمُ ٱلنَّارُ ۖ كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَآ أُعِيدُوا۟ فِيهَا وَقِيلَ لَهُمْ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (33:2) [listed for 88:3] وَٱتَّبِعْ مَا يُوحَىٰٓ إِلَيْكَ مِن رَّبِّكَ ۚ إِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
- (33:19) [listed for 88:3] أَشِحَّةً عَلَيْكُمْ ۖ فَإِذَا جَآءَ ٱلْخَوْفُ رَأَيْتَهُمْ يَنظُرُونَ إِلَيْكَ تَدُورُ أَعْيُنُهُمْ كَٱلَّذِى يُغْشَىٰ عَلَيْهِ مِنَ ٱلْمَوْتِ ۖ فَإِذَا ذَهَبَ ٱلْخَوْفُ سَلَقُوكُم بِأَلْسِنَةٍ حِدَادٍ أَشِحَّةً عَلَى ٱلْخَيْرِ ۚ أُو۟لَٰٓئِكَ لَمْ يُؤْمِنُوا۟ فَأَحْبَطَ ٱللَّهُ أَعْمَٰلَهُمْ ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًۭا
- (35:7) [listed for 88:3] ٱلَّذِينَ كَفَرُوا۟ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۖ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌ
- (37:61) [listed for 88:3] لِمِثْلِ هَٰذَا فَلْيَعْمَلِ ٱلْعَٰمِلُونَ
- (37:96) [listed for 88:3] وَٱللَّهُ خَلَقَكُمْ وَمَا تَعْمَلُونَ
- (38:41) [listed for 88:3] وَٱذْكُرْ عَبْدَنَآ أَيُّوبَ إِذْ نَادَىٰ رَبَّهُۥٓ أَنِّى مَسَّنِىَ ٱلشَّيْطَٰنُ بِنُصْبٍۢ وَعَذَابٍ
- (39:10) [listed for 88:3] قُلْ يَٰعِبَادِ ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ رَبَّكُمْ ۚ لِلَّذِينَ أَحْسَنُوا۟ فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةٌۭ ۗ وَأَرْضُ ٱللَّهِ وَٰسِعَةٌ ۗ إِنَّمَا يُوَفَّى ٱلصَّٰبِرُونَ أَجْرَهُم بِغَيْرِ حِسَابٍۢ
- (40:40) [listed for 88:3] مَنْ عَمِلَ سَيِّئَةًۭ فَلَا يُجْزَىٰٓ إِلَّا مِثْلَهَا ۖ وَمَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ يُرْزَقُونَ فِيهَا بِغَيْرِ حِسَابٍۢ
- (40:58) [listed for 88:3] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَلَا ٱلْمُسِىٓءُ ۚ قَلِيلًۭا مَّا تَتَذَكَّرُونَ
- (41:20) [listed for 88:3] حَتَّىٰٓ إِذَا مَا جَآءُوهَا شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- (41:46) [listed for 88:3] مَّنْ عَمِلَ صَٰلِحًۭا فَلِنَفْسِهِۦ ۖ وَمَنْ أَسَآءَ فَعَلَيْهَا ۗ وَمَا رَبُّكَ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
- (41:50) [listed for 88:3] وَلَئِنْ أَذَقْنَٰهُ رَحْمَةًۭ مِّنَّا مِنۢ بَعْدِ ضَرَّآءَ مَسَّتْهُ لَيَقُولَنَّ هَٰذَا لِى وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّجِعْتُ إِلَىٰ رَبِّىٓ إِنَّ لِى عِندَهُۥ لَلْحُسْنَىٰ ۚ فَلَنُنَبِّئَنَّ ٱلَّذِينَ كَفَرُوا۟ بِمَا عَمِلُوا۟ وَلَنُذِيقَنَّهُم مِّنْ عَذَابٍ غَلِيظٍۢ
- (42:20) [listed for 88:3] مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
- (42:30) [listed for 88:3] وَمَآ أَصَٰبَكُم مِّن مُّصِيبَةٍۢ فَبِمَا كَسَبَتْ أَيْدِيكُمْ وَيَعْفُوا۟ عَن كَثِيرٍۢ
- (43:72) [listed for 88:3] وَتِلْكَ ٱلْجَنَّةُ ٱلَّتِىٓ أُورِثْتُمُوهَا بِمَا كُنتُمْ تَعْمَلُونَ
- (44:11) [listed for 88:3] يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ
- (45:15) [listed for 88:3] مَنْ عَمِلَ صَٰلِحًۭا فَلِنَفْسِهِۦ ۖ وَمَنْ أَسَآءَ فَعَلَيْهَا ۖ ثُمَّ إِلَىٰ رَبِّكُمْ تُرْجَعُونَ
- (46:14) [listed for 88:3] أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (46:15) [listed for 88:3] وَوَصَّيْنَا ٱلْإِنسَٰنَ بِوَٰلِدَيْهِ إِحْسَٰنًا ۖ حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا ۖ وَحَمْلُهُۥ وَفِصَٰلُهُۥ ثَلَٰثُونَ شَهْرًا ۚ حَتَّىٰٓ إِذَا بَلَغَ أَشُدَّهُۥ وَبَلَغَ أَرْبَعِينَ سَنَةًۭ قَالَ رَبِّ أَوْزِعْنِىٓ أَنْ أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ أَنْعَمْتَ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ وَأَنْ أَعْمَلَ صَٰلِحًۭا تَرْضَىٰهُ وَأَصْلِحْ لِى فِى ذُرِّيَّتِىٓ ۖ إِنِّى تُبْتُ إِلَيْكَ وَإِنِّى مِنَ ٱلْمُسْلِمِينَ
- (52:16) [listed for 88:3] [cited in ¶14] ٱصْلَوْهَا فَٱصْبِرُوٓا۟ أَوْ لَا تَصْبِرُوا۟ سَوَآءٌ عَلَيْكُمْ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
- (52:21) [listed for 88:3] وَٱلَّذِينَ ءَامَنُوا۟ وَٱتَّبَعَتْهُمْ ذُرِّيَّتُهُم بِإِيمَٰنٍ أَلْحَقْنَا بِهِمْ ذُرِّيَّتَهُمْ وَمَآ أَلَتْنَٰهُم مِّنْ عَمَلِهِم مِّن شَىْءٍۢ ۚ كُلُّ ٱمْرِئٍۭ بِمَا كَسَبَ رَهِينٌۭ
- (53:31) [listed for 88:3] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
- (54:52) [listed for 88:3] وَكُلُّ شَىْءٍۢ فَعَلُوهُ فِى ٱلزُّبُرِ
- (54:53) [listed for 88:3] وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ
- (56:24) [listed for 88:3] جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (57:4) [listed for 88:3] هُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۖ وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (57:10) [listed for 88:3] وَمَا لَكُمْ أَلَّا تُنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ وَلِلَّهِ مِيرَٰثُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ لَا يَسْتَوِى مِنكُم مَّنْ أَنفَقَ مِن قَبْلِ ٱلْفَتْحِ وَقَٰتَلَ ۚ أُو۟لَٰٓئِكَ أَعْظَمُ دَرَجَةًۭ مِّنَ ٱلَّذِينَ أَنفَقُوا۟ مِنۢ بَعْدُ وَقَٰتَلُوا۟ ۚ وَكُلًّۭا وَعَدَ ٱللَّهُ ٱلْحُسْنَىٰ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (58:6) [listed for 88:3] يَوْمَ يَبْعَثُهُمُ ٱللَّهُ جَمِيعًۭا فَيُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
- (64:7) [listed for 88:3] زَعَمَ ٱلَّذِينَ كَفَرُوٓا۟ أَن لَّن يُبْعَثُوا۟ ۚ قُلْ بَلَىٰ وَرَبِّى لَتُبْعَثُنَّ ثُمَّ لَتُنَبَّؤُنَّ بِمَا عَمِلْتُمْ ۚ وَذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (64:9) [listed for 88:3] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (69:19) [listed for 88:3] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (69:25) [listed for 88:3] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ فَيَقُولُ يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ
- (70:16) [listed for 88:3] نَزَّاعَةًۭ لِّلشَّوَىٰ
- (72:23) [listed for 88:3] إِلَّا بَلَٰغًۭا مِّنَ ٱللَّهِ وَرِسَٰلَٰتِهِۦ ۚ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَإِنَّ لَهُۥ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَآ أَبَدًا
- (74:38) [listed for 88:3] كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ
- (80:39) [listed for 88:3] ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ
- (81:14) [listed for 88:3] عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ
- (82:5) [listed for 88:3] عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ
- (82:16) [listed for 88:3] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
- (84:25) [listed for 88:3] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۭ
- (87:14) [listed for 88:3] قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- (89:23) [listed for 88:3] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (91:9) [listed for 88:3] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- (92:15) [listed for 88:3] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (92:16) [listed for 88:3] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- (92:20) [listed for 88:3] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (95:6) [listed for 88:3] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ
- (98:7) [listed for 88:3] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- (99:6) [listed for 88:3] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- (101:11) [listed for 88:3] نَارٌ حَامِيَةٌۢ

## named by the passage's own list as strong for this ayah (2)

- (55:44) [listed for 88:3] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- (75:24) [listed for 88:3] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ

## named by the passage's own list as medium for this ayah (6)

- (3:106) [listed for 88:3] يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌۭ ۚ فَأَمَّا ٱلَّذِينَ ٱسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُم بَعْدَ إِيمَٰنِكُمْ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (70:15) [listed for 88:3] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (74:10) [listed for 88:3] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (80:41) [listed for 88:3] تَرْهَقُهَا قَتَرَةٌ
- (84:12) [listed for 88:3] وَيَصْلَىٰ سَعِيرًا
- (94:3) [listed for 88:3] ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ

## weak (this ayah's own list) (22)

- (2:202) [listed for 88:3] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
- (3:23) [listed for 88:3] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يُدْعَوْنَ إِلَىٰ كِتَٰبِ ٱللَّهِ لِيَحْكُمَ بَيْنَهُمْ ثُمَّ يَتَوَلَّىٰ فَرِيقٌۭ مِّنْهُمْ وَهُم مُّعْرِضُونَ
- (4:7) [listed for 88:3] لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا تَرَكَ ٱلْوَٰلِدَانِ وَٱلْأَقْرَبُونَ وَلِلنِّسَآءِ نَصِيبٌۭ مِّمَّا تَرَكَ ٱلْوَٰلِدَانِ وَٱلْأَقْرَبُونَ مِمَّا قَلَّ مِنْهُ أَوْ كَثُرَ ۚ نَصِيبًۭا مَّفْرُوضًۭا
- (6:136) [listed for 88:3] وَجَعَلُوا۟ لِلَّهِ مِمَّا ذَرَأَ مِنَ ٱلْحَرْثِ وَٱلْأَنْعَٰمِ نَصِيبًۭا فَقَالُوا۟ هَٰذَا لِلَّهِ بِزَعْمِهِمْ وَهَٰذَا لِشُرَكَآئِنَا ۖ فَمَا كَانَ لِشُرَكَآئِهِمْ فَلَا يَصِلُ إِلَى ٱللَّهِ ۖ وَمَا كَانَ لِلَّهِ فَهُوَ يَصِلُ إِلَىٰ شُرَكَآئِهِمْ ۗ سَآءَ مَا يَحْكُمُونَ
- (7:37) [listed for 88:3] فَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ كَذَّبَ بِـَٔايَٰتِهِۦٓ ۚ أُو۟لَٰٓئِكَ يَنَالُهُمْ نَصِيبُهُم مِّنَ ٱلْكِتَٰبِ ۖ حَتَّىٰٓ إِذَا جَآءَتْهُمْ رُسُلُنَا يَتَوَفَّوْنَهُمْ قَالُوٓا۟ أَيْنَ مَا كُنتُمْ تَدْعُونَ مِن دُونِ ٱللَّهِ ۖ قَالُوا۟ ضَلُّوا۟ عَنَّا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
- (15:96) [listed for 88:3] ٱلَّذِينَ يَجْعَلُونَ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ ۚ فَسَوْفَ يَعْلَمُونَ
- (22:11) [listed for 88:3] وَمِنَ ٱلنَّاسِ مَن يَعْبُدُ ٱللَّهَ عَلَىٰ حَرْفٍۢ ۖ فَإِنْ أَصَابَهُۥ خَيْرٌ ٱطْمَأَنَّ بِهِۦ ۖ وَإِنْ أَصَابَتْهُ فِتْنَةٌ ٱنقَلَبَ عَلَىٰ وَجْهِهِۦ خَسِرَ ٱلدُّنْيَا وَٱلْءَاخِرَةَ ۚ ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (26:112) [listed for 88:3] قَالَ وَمَا عِلْمِى بِمَا كَانُوا۟ يَعْمَلُونَ
- (26:169) [listed for 88:3] رَبِّ نَجِّنِى وَأَهْلِى مِمَّا يَعْمَلُونَ
- (29:58) [listed for 88:3] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (33:31) [listed for 88:3] ۞ وَمَن يَقْنُتْ مِنكُنَّ لِلَّهِ وَرَسُولِهِۦ وَتَعْمَلْ صَٰلِحًۭا نُّؤْتِهَآ أَجْرَهَا مَرَّتَيْنِ وَأَعْتَدْنَا لَهَا رِزْقًۭا كَرِيمًۭا
- (48:11) [listed for 88:3] سَيَقُولُ لَكَ ٱلْمُخَلَّفُونَ مِنَ ٱلْأَعْرَابِ شَغَلَتْنَآ أَمْوَٰلُنَا وَأَهْلُونَا فَٱسْتَغْفِرْ لَنَا ۚ يَقُولُونَ بِأَلْسِنَتِهِم مَّا لَيْسَ فِى قُلُوبِهِمْ ۚ قُلْ فَمَن يَمْلِكُ لَكُم مِّنَ ٱللَّهِ شَيْـًٔا إِنْ أَرَادَ بِكُمْ ضَرًّا أَوْ أَرَادَ بِكُمْ نَفْعًۢا ۚ بَلْ كَانَ ٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرًۢا
- (58:13) [listed for 88:3] ءَأَشْفَقْتُمْ أَن تُقَدِّمُوا۟ بَيْنَ يَدَىْ نَجْوَىٰكُمْ صَدَقَٰتٍۢ ۚ فَإِذْ لَمْ تَفْعَلُوا۟ وَتَابَ ٱللَّهُ عَلَيْكُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَطِيعُوا۟ ٱللَّهَ وَرَسُولَهُۥ ۚ وَٱللَّهُ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (65:7) [listed for 88:3] لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ ۖ وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ ۚ لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا ۚ سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا
- (70:4) [listed for 88:3] تَعْرُجُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ إِلَيْهِ فِى يَوْمٍۢ كَانَ مِقْدَارُهُۥ خَمْسِينَ أَلْفَ سَنَةٍۢ
- (73:20) [listed for 88:3] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ
- (83:4) [listed for 88:3] أَلَا يَظُنُّ أُو۟لَٰٓئِكَ أَنَّهُم مَّبْعُوثُونَ
- (92:12) [listed for 88:3] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:13) [listed for 88:3] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (100:6) [listed for 88:3] إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- (100:11) [listed for 88:3] إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ
- (102:8) [listed for 88:3] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

## named by the passage's own list as weak for this ayah (5)

- (4:85) [listed for 88:3] مَّن يَشْفَعْ شَفَٰعَةً حَسَنَةًۭ يَكُن لَّهُۥ نَصِيبٌۭ مِّنْهَا ۖ وَمَن يَشْفَعْ شَفَٰعَةًۭ سَيِّئَةًۭ يَكُن لَّهُۥ كِفْلٌۭ مِّنْهَا ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقِيتًۭا
- (70:43) [listed for 88:3] [cited in ¶7] يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ
- (79:2) [listed for 88:3] وَٱلنَّٰشِطَٰتِ نَشْطًۭا
- (80:38) [listed for 88:3] وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ
- (90:13) [listed for 88:3] فَكُّ رَقَبَةٍ

## neighbours: within two ayat of a passage the commentary cites (46)

- (3:189) [next to 3:191] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (3:190) [next to 3:191] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
- (3:192) [next to 3:191] رَبَّنَآ إِنَّكَ مَن تُدْخِلِ ٱلنَّارَ فَقَدْ أَخْزَيْتَهُۥ ۖ وَمَا لِلظَّٰلِمِينَ مِنْ أَنصَارٍۢ
- (3:193) [next to 3:191] رَّبَّنَآ إِنَّنَا سَمِعْنَا مُنَادِيًۭا يُنَادِى لِلْإِيمَٰنِ أَنْ ءَامِنُوا۟ بِرَبِّكُمْ فَـَٔامَنَّا ۚ رَبَّنَا فَٱغْفِرْ لَنَا ذُنُوبَنَا وَكَفِّرْ عَنَّا سَيِّـَٔاتِنَا وَتَوَفَّنَا مَعَ ٱلْأَبْرَارِ
- (3:194) [next to 3:195] رَبَّنَا وَءَاتِنَا مَا وَعَدتَّنَا عَلَىٰ رُسُلِكَ وَلَا تُخْزِنَا يَوْمَ ٱلْقِيَٰمَةِ ۗ إِنَّكَ لَا تُخْلِفُ ٱلْمِيعَادَ
- (3:196) [next to 3:195] لَا يَغُرَّنَّكَ تَقَلُّبُ ٱلَّذِينَ كَفَرُوا۟ فِى ٱلْبِلَٰدِ
- (3:197) [next to 3:195] مَتَٰعٌۭ قَلِيلٌۭ ثُمَّ مَأْوَىٰهُمْ جَهَنَّمُ ۚ وَبِئْسَ ٱلْمِهَادُ
- (5:1) [next to 5:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَوْفُوا۟ بِٱلْعُقُودِ ۚ أُحِلَّتْ لَكُم بَهِيمَةُ ٱلْأَنْعَٰمِ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ غَيْرَ مُحِلِّى ٱلصَّيْدِ وَأَنتُمْ حُرُمٌ ۗ إِنَّ ٱللَّهَ يَحْكُمُ مَا يُرِيدُ
- (5:2) [next to 5:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (5:4) [next to 5:3] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (5:5) [next to 5:3] ٱلْيَوْمَ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۖ وَطَعَامُ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ حِلٌّۭ لَّكُمْ وَطَعَامُكُمْ حِلٌّۭ لَّهُمْ ۖ وَٱلْمُحْصَنَٰتُ مِنَ ٱلْمُؤْمِنَٰتِ وَٱلْمُحْصَنَٰتُ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ إِذَآ ءَاتَيْتُمُوهُنَّ أُجُورَهُنَّ مُحْصِنِينَ غَيْرَ مُسَٰفِحِينَ وَلَا مُتَّخِذِىٓ أَخْدَانٍۢ ۗ وَمَن يَكْفُرْ بِٱلْإِيمَٰنِ فَقَدْ حَبِطَ عَمَلُهُۥ وَهُوَ فِى ٱلْءَاخِرَةِ مِنَ ٱلْخَٰسِرِينَ
- (9:118) [next to 9:120] وَعَلَى ٱلثَّلَٰثَةِ ٱلَّذِينَ خُلِّفُوا۟ حَتَّىٰٓ إِذَا ضَاقَتْ عَلَيْهِمُ ٱلْأَرْضُ بِمَا رَحُبَتْ وَضَاقَتْ عَلَيْهِمْ أَنفُسُهُمْ وَظَنُّوٓا۟ أَن لَّا مَلْجَأَ مِنَ ٱللَّهِ إِلَّآ إِلَيْهِ ثُمَّ تَابَ عَلَيْهِمْ لِيَتُوبُوٓا۟ ۚ إِنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (9:119) [next to 9:120] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَكُونُوا۟ مَعَ ٱلصَّٰدِقِينَ
- (9:121) [next to 9:120] وَلَا يُنفِقُونَ نَفَقَةًۭ صَغِيرَةًۭ وَلَا كَبِيرَةًۭ وَلَا يَقْطَعُونَ وَادِيًا إِلَّا كُتِبَ لَهُمْ لِيَجْزِيَهُمُ ٱللَّهُ أَحْسَنَ مَا كَانُوا۟ يَعْمَلُونَ
- (9:122) [next to 9:120] ۞ وَمَا كَانَ ٱلْمُؤْمِنُونَ لِيَنفِرُوا۟ كَآفَّةًۭ ۚ فَلَوْلَا نَفَرَ مِن كُلِّ فِرْقَةٍۢ مِّنْهُمْ طَآئِفَةٌۭ لِّيَتَفَقَّهُوا۟ فِى ٱلدِّينِ وَلِيُنذِرُوا۟ قَوْمَهُمْ إِذَا رَجَعُوٓا۟ إِلَيْهِمْ لَعَلَّهُمْ يَحْذَرُونَ
- (18:58) [next to 18:60] وَرَبُّكَ ٱلْغَفُورُ ذُو ٱلرَّحْمَةِ ۖ لَوْ يُؤَاخِذُهُم بِمَا كَسَبُوا۟ لَعَجَّلَ لَهُمُ ٱلْعَذَابَ ۚ بَل لَّهُم مَّوْعِدٌۭ لَّن يَجِدُوا۟ مِن دُونِهِۦ مَوْئِلًۭا
- (18:59) [next to 18:60] وَتِلْكَ ٱلْقُرَىٰٓ أَهْلَكْنَٰهُمْ لَمَّا ظَلَمُوا۟ وَجَعَلْنَا لِمَهْلِكِهِم مَّوْعِدًۭا
- (18:63) [next to 18:61] قَالَ أَرَءَيْتَ إِذْ أَوَيْنَآ إِلَى ٱلصَّخْرَةِ فَإِنِّى نَسِيتُ ٱلْحُوتَ وَمَآ أَنسَىٰنِيهُ إِلَّا ٱلشَّيْطَٰنُ أَنْ أَذْكُرَهُۥ ۚ وَٱتَّخَذَ سَبِيلَهُۥ فِى ٱلْبَحْرِ عَجَبًۭا
- (18:64) [next to 18:62] قَالَ ذَٰلِكَ مَا كُنَّا نَبْغِ ۚ فَٱرْتَدَّا عَلَىٰٓ ءَاثَارِهِمَا قَصَصًۭا
- (18:101) [next to 18:103] ٱلَّذِينَ كَانَتْ أَعْيُنُهُمْ فِى غِطَآءٍ عَن ذِكْرِى وَكَانُوا۟ لَا يَسْتَطِيعُونَ سَمْعًا
- (18:102) [next to 18:103] أَفَحَسِبَ ٱلَّذِينَ كَفَرُوٓا۟ أَن يَتَّخِذُوا۟ عِبَادِى مِن دُونِىٓ أَوْلِيَآءَ ۚ إِنَّآ أَعْتَدْنَا جَهَنَّمَ لِلْكَٰفِرِينَ نُزُلًۭا
- (18:106) [next to 18:104] ذَٰلِكَ جَزَآؤُهُمْ جَهَنَّمُ بِمَا كَفَرُوا۟ وَٱتَّخَذُوٓا۟ ءَايَٰتِى وَرُسُلِى هُزُوًا
- (24:37) [next to 24:39] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
- (24:38) [next to 24:39] لِيَجْزِيَهُمُ ٱللَّهُ أَحْسَنَ مَا عَمِلُوا۟ وَيَزِيدَهُم مِّن فَضْلِهِۦ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
- (24:40) [next to 24:39] أَوْ كَظُلُمَٰتٍۢ فِى بَحْرٍۢ لُّجِّىٍّۢ يَغْشَىٰهُ مَوْجٌۭ مِّن فَوْقِهِۦ مَوْجٌۭ مِّن فَوْقِهِۦ سَحَابٌۭ ۚ ظُلُمَٰتٌۢ بَعْضُهَا فَوْقَ بَعْضٍ إِذَآ أَخْرَجَ يَدَهُۥ لَمْ يَكَدْ يَرَىٰهَا ۗ وَمَن لَّمْ يَجْعَلِ ٱللَّهُ لَهُۥ نُورًۭا فَمَا لَهُۥ مِن نُّورٍ
- (24:41) [next to 24:39] أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ ۖ كُلٌّۭ قَدْ عَلِمَ صَلَاتَهُۥ وَتَسْبِيحَهُۥ ۗ وَٱللَّهُ عَلِيمٌۢ بِمَا يَفْعَلُونَ
- (25:20) [next to 25:22] وَمَآ أَرْسَلْنَا قَبْلَكَ مِنَ ٱلْمُرْسَلِينَ إِلَّآ إِنَّهُمْ لَيَأْكُلُونَ ٱلطَّعَامَ وَيَمْشُونَ فِى ٱلْأَسْوَاقِ ۗ وَجَعَلْنَا بَعْضَكُمْ لِبَعْضٍۢ فِتْنَةً أَتَصْبِرُونَ ۗ وَكَانَ رَبُّكَ بَصِيرًۭا
- (25:21) [next to 25:22] ۞ وَقَالَ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا لَوْلَآ أُنزِلَ عَلَيْنَا ٱلْمَلَٰٓئِكَةُ أَوْ نَرَىٰ رَبَّنَا ۗ لَقَدِ ٱسْتَكْبَرُوا۟ فِىٓ أَنفُسِهِمْ وَعَتَوْ عُتُوًّۭا كَبِيرًۭا
- (25:24) [next to 25:22] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (25:25) [next to 25:23] وَيَوْمَ تَشَقَّقُ ٱلسَّمَآءُ بِٱلْغَمَٰمِ وَنُزِّلَ ٱلْمَلَٰٓئِكَةُ تَنزِيلًا
- (35:31) [next to 35:33] وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ مِنَ ٱلْكِتَٰبِ هُوَ ٱلْحَقُّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ ۗ إِنَّ ٱللَّهَ بِعِبَادِهِۦ لَخَبِيرٌۢ بَصِيرٌۭ
- (35:32) [next to 35:33] ثُمَّ أَوْرَثْنَا ٱلْكِتَٰبَ ٱلَّذِينَ ٱصْطَفَيْنَا مِنْ عِبَادِنَا ۖ فَمِنْهُمْ ظَالِمٌۭ لِّنَفْسِهِۦ وَمِنْهُم مُّقْتَصِدٌۭ وَمِنْهُمْ سَابِقٌۢ بِٱلْخَيْرَٰتِ بِإِذْنِ ٱللَّهِ ۚ ذَٰلِكَ هُوَ ٱلْفَضْلُ ٱلْكَبِيرُ
- (35:36) [next to 35:34] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (35:37) [next to 35:35] وَهُمْ يَصْطَرِخُونَ فِيهَا رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ ۖ فَذُوقُوا۟ فَمَا لِلظَّٰلِمِينَ مِن نَّصِيرٍ
- (52:12) [next to 52:14] ٱلَّذِينَ هُمْ فِى خَوْضٍۢ يَلْعَبُونَ
- (52:13) [next to 52:14] يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا
- (52:15) [next to 52:14] أَفَسِحْرٌ هَٰذَآ أَمْ أَنتُمْ لَا تُبْصِرُونَ
- (52:17) [next to 52:16] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَعِيمٍۢ
- (52:18) [next to 52:16] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (70:40) [next to 70:42] فَلَآ أُقْسِمُ بِرَبِّ ٱلْمَشَٰرِقِ وَٱلْمَغَٰرِبِ إِنَّا لَقَٰدِرُونَ
- (70:41) [next to 70:42] عَلَىٰٓ أَن نُّبَدِّلَ خَيْرًۭا مِّنْهُمْ وَمَا نَحْنُ بِمَسْبُوقِينَ
- (74:15) [next to 74:17] ثُمَّ يَطْمَعُ أَنْ أَزِيدَ
- (74:16) [next to 74:17] كَلَّآ ۖ إِنَّهُۥ كَانَ لِءَايَٰتِنَا عَنِيدًۭا
- (74:18) [next to 74:17] إِنَّهُۥ فَكَّرَ وَقَدَّرَ
- (74:19) [next to 74:17] فَقُتِلَ كَيْفَ قَدَّرَ
- (94:5) [next to 94:6] فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا

