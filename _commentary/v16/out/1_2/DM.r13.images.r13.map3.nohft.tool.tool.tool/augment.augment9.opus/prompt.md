Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:2; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_2.reading.tr.md (prose paragraphs numbered) =====
## Fiilsiz bir hüküm

[¶1] İkinci ayet bir isim cümlesidir ve içinde fiil yoktur. Kimse "övüyorum" demez, kimseye "övün" diye emredilmez. Cümle belirlilik takısı almış bir adla başlar: {ar:ٱلْحَمْدُ, tr:el-hamdü, gloss:övgü, övgünün bütünü, source:1:2}. Ardından bu övgünün kime ait olduğunu bildiren "li" harfi ve Allah adı gelir: {ar:لِلَّهِ, tr:lillâhi, gloss:Allah'a aittir, source:1:2}. Cümleyi iki kelimelik bir nitelik kapatır: {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabbi'l-âlemîn, gloss:âlemlerin Rabbi, source:1:2}. Bu cümle bir eylemi anlatmaz, bir durumu tespit eder. Övgü, biri onu söylemeden önce de yerini bulmuştur. Fâtiha her namazda okunduğu için bu cümle her gün bir insanın ağzından çıkar. Ama okuyan kendini cümlenin öznesi yapmaz. Konuşan kişi ancak beşinci ayette "biz" olarak ortaya çıkacaktır.

[¶2] Türkçede "hamd" kelimesinin anlamı daralmıştır. "Allah'a hamdolsun" çoğu zaman bir rahatlama sözüdür. Bir tehlike atlatıldığında ya da işler yolunda gittiğinde söylenir ve teşekküre yakın durur. Arapçada ise hamd her şeyden önce bir yargıdır. Araplar onu yerginin karşısına koyarlardı: {ar:الحمد نقيض الذم, tr:el-hamdü nakîdu'z-zemm, gloss:hamd yerginin karşıtıdır, source:"ح م د,B001"}. Birini övmek, onu yerilecek biri değil, övülecek biri olarak bulmaktır. Bu yüzden hamd teşekkürden daha geniştir: {ar:الحمد أعم من الشكر, tr:el-hamdü eammü mine'ş-şükr, gloss:hamd şükürden daha kapsamlıdır, source:"ح م د,B001"}. Teşekkür bize yapılmış bir iyiliğe verilen karşılıktır. Hamd bu karşılığı da içine alır ama onunla sınırlı kalmaz. Birini yaptığı övülecek bir iş için över, karşılığında bir iyilik görülmüş olsun ya da olmasın {source:"ح م د,B001"}.

[¶3] Aynı fiilin bir başka kullanımı, hamdın nasıl ortaya çıktığını gösterir. Birini sınayıp övgüye değer bulana {ar:أحمدت فلانا إذا وجدته محمودا, tr:ahmedtü fülânen izâ vecedtühû mahmûdâ, gloss:falancayı övülmeye değer buldum, source:"ح م د,B002"} denirdi. Bir işi onaylayıp onaylamadığınızı sormak isteyen de bu fiili kullanırdı: {ar:هل تحمد لي هذا الأمر أي هل ترضاه لي, tr:hel tahmedü lî hâze'l-emr, gloss:bu işi benim için uygun görür müsün, ona razı olur musun, source:"ح م د,B002"}. Demek ki hamd bir deneyimin sonunda verilen onaydır. Bir şeye bakılmış, sınanmış, içinde yaşanmış ve iyi bulunmuştur. "El-hamdü lillâh" bu anlamda bir dilek değil, bir hükümdür. Onay ile ret arasındaki bu karşıtlık surenin sonunda yeniden belirir. Yedinci ayet, kendilerine nimet verilenleri {ar:غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:gayri'l-magdûbi aleyhim, gloss:gazaba uğramış olanlar değil, source:1:7} sözüyle ayırırken, ikinci ayetin onayla açtığı alanı ikiye böler.

## Övgü, işi yapana döner

[¶4] Araplar hamdı yapılmış övülecek bir işin karşılığı sayarlardı {source:"ح م د,B001"}. Ayetteki "li" harfi övgünün tamamını tek bir yere bağlar. Böylece cümle, bütün övülecek işlerin kime ait olduğunu söylemiş olur. Aynı fiilin bir kalıbı ise övgünün yanlış yere çekilmesini anlatır. İyiliğini başa kakıp karşılığında övgü bekleyen biri için {ar:فلان يتحمد علي أي يمن, tr:fülânün yetehammedü aleyye, gloss:falanca iyiliğini başıma kakıyor, source:"ح م د,B005"} denirdi. Bir söz bu davranışın sınırını çizer: {ar:من أنفق ماله على نفسه فلا يتحمد به إلى الناس, tr:men enfeka mâlehû alâ nefsihî fe-lâ yetehammed bihî ile'n-nâs, gloss:malını kendine harcayan, bunu insanlara iyilik diye öne sürmesin, source:"ح م د,B005"}. İki örnekte de övgü kendine çekilmektedir, oysa ona yol açan iş başka yerdedir.

[¶5] Kur'an bu sapmaya bir ad verir. Kitap verilenlerden, kitabı insanlara açıklayıp gizlemeyeceklerine dair söz alındığını, onların ise bu sözü arkalarına atıp az bir bedele sattıklarını anlatır {source:3:187}. Hemen ardından şu kimselerden söz eder: {ar:ٱلَّذِينَ يَفْرَحُونَ بِمَآ أَتَوا۟ وَّيُحِبُّونَ أَن يُحْمَدُوا۟ بِمَا لَمْ يَفْعَلُوا۟, tr:ellezîne yefrahûne bimâ etev ve yuhibbûne en yuhmedû bimâ lem yef'alû, gloss:yaptıklarına sevinen ve yapmadıkları şeyle övülmeyi sevenler, source:3:188}. Ayet onların azaptan kurtulmuş sanılmamasını söyler. Bu insanlar yapılmamış bir iş için övgü istemiştir. İkinci ayetteki cümle bunun tam tersini yapar ve övgüyü işin yapıldığı yere bırakır.

[¶6] Kur'an'da bu cümle bir yerde kelimesi kelimesine, bir hikâyenin sonunda geçer. Allah, Peygamberden önceki ümmetlere elçiler gönderdiğini ve yalvarsınlar diye onları darlık ve sıkıntıyla yakaladığını anlatır {source:6:42}. Fakat kalpleri katılaşır {source:6:43}. Bunun üzerine onlara her şeyin kapıları açılır: {ar:حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ, tr:hattâ izâ ferihû bimâ ûtû ehaznâhüm bagteten, gloss:kendilerine verilenle sevindiklerinde onları ansızın yakaladık, source:6:44}. Sonraki ayet şöyledir: {ar:فَقُطِعَ دَابِرُ ٱلْقَوْمِ ٱلَّذِينَ ظَلَمُوا۟ ۚ وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:fe-kutı'a dâbiru'l-kavmi'llezîne zalemû, ve'l-hamdü lillâhi rabbi'l-âlemîn, gloss:zulmeden kavmin kökü kesildi; hamd âlemlerin Rabbi Allah'adır, source:6:45}. Burada hamd, verilmiş bir armağana teşekkür olamaz. Bir sonun doğru olduğunu söyleyen yargıdır, yani yerginin karşıtı olan hamddır. İki hikâye de aynı noktada kırılır. Birinde insanlar yaptıklarına, öbüründe kendilerine verilene sevinir. İkisinde de ellerindekini kendi övgülerinin kaynağı sayarlar. Fâtiha'nın ikinci ayeti ise övgüyü elden ele geçen bütün iyiliklerin kaynağına geri koyar.

[¶7] Övgünün bağlandığı ad da bu yönü güçlendirir. "Allah" adının kökü tapınmayı ve tapınılanı anlatır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır, çünkü kulluk edilendir, source:"ء ل ه,B001"}. Bir söz bunu açık bir şart olarak koyar: {ar:لا يكون إلاها حتى يكون معبودا, tr:lâ yekûnü ilâhen hattâ yekûne ma'bûdâ, gloss:kulluk edilmedikçe ilah olmaz, source:"ء ل ه,B001"}. Hamd böylece, anlamı "kulluk edilen" olan bir ada bağlanır. Konuşan kişi bu bağı beşinci ayette kendi sesiyle söyleyecektir: {ar:إِيَّاكَ نَعْبُدُ, tr:iyyâke na'büdü, gloss:yalnız sana kulluk ederiz, source:1:5}. Bu adın en büyük ad olduğu da söylenirdi: {ar:اسم الله الأكبر هو الله, tr:ismullâhi'l-ekberu hüvallâh, gloss:Allah'ın en büyük adı "Allah"tır, source:"ء ل ه,B002"}. Birinci ayetteki "bism" kelimesiyle kurulan ad ve işaret sahnesi de bu adın üzerinde durur.

## Rab: evin, atın ve her şeyin sahibi

[¶8] "Rab" kelimesi Arapçada bir ilişkiyi anlatır ve çoğu zaman bir şeye bağlanarak kullanılırdı: {ar:رب الدار ورب الفرس, tr:rabbü'd-dâr ve rabbü'l-feres, gloss:evin sahibi, atın sahibi, source:"ر ب ب,B001"}. Kural şöyle konurdu: {ar:ورب كل شيء مالكه, tr:ve rabbü kulli şey'in mâlikuh, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}. Ama buradaki sahiplik bir şeyi yalnızca elde tutmak değildir. Kelimeye üç ayrı anlam verilirdi: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح, tr:yekûnü'r-rabbü'l-mâlik, ve yekûnü'r-rabbü's-seyyidü'l-mutâ', ve yekûnü'r-rabbü'l-muslih, gloss:rab sahip olandır, sözü dinlenen efendidir, düzeltip iyileştirendir, source:"ر ب ب,B001"}. Bir evin rabbi o evin hem sahibi, hem sözü geçen büyüğü, hem de onu onarıp çekip çevirenidir. Cahiliye döneminde kelime hükümdar için de kullanılmıştı: {ar:وقد قالوه في الجاهلية للملك, tr:ve kad kâlûhü fi'l-câhiliyyeti li'l-melik, gloss:cahiliyede bunu hükümdar için de söylemişlerdi, source:"ر ب ب,B001"}. Yine de kelime tek başına, bir şeye bağlanmadan söylendiğinde yalnızca Allah'ı gösterirdi: {ar:لا يقال الرب مطلقا إلا لله, tr:lâ yukâlü'r-rabbü mutlakan illâ lillâh, gloss:kayıtsız "rab" yalnız Allah için söylenir, source:"ر ب ب,B001"}.

[¶9] Kur'an da kelimeyi insan efendiler için kullanır. Zindandaki Yusuf, iki arkadaşının rüyasını yorumlarken birinin {ar:فَيَسْقِى رَبَّهُۥ خَمْرًۭا, tr:fe-yeskî rabbehû hamrâ, gloss:efendisine şarap sunacak, source:12:41} olduğunu söyler. Kitap ehline yapılan çağrı ise insanların birbirini rab edinmemesini ister: {ar:وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ, tr:ve lâ yettehize ba'dunâ ba'dan erbâben min dûnillâh, gloss:Allah'ı bırakıp birbirimizi rabler edinmeyelim, source:3:64}. Bu kullanımlar göz önünde tutulunca ikinci ayetin tamlaması daha iyi duyulur. Kelime alışılmış kullanımında bir eve, bir ata ya da bir hükümdarın halkına, yani sınırlı bir şeye bağlanır. Burada ise bağlandığı şey "âlemler"dir, yani sahip olunabilecek her şeyin bütün türleri. Kelimenin gündelik ölçüsü korunmuş, nesnesi ise sonuna kadar genişletilmiştir. Surede efendi ile kulu arasındaki sahne dördüncü ayetteki "mâlik" ve beşinci ayetteki "na'büdü" kelimeleriyle kurulur. İkinci ayet bu sahnede efendinin adını verir.

[¶10] Kur'an, "âlemlerin Rabbi" sözünün bir hükümdar tarafından sorgulandığı bir sahneyi de anlatır. Musa ile Harun'a, Firavun'a gidip {ar:إِنَّا رَسُولُ رَبِّ ٱلْعَٰلَمِينَ, tr:innâ rasûlü rabbi'l-âlemîn, gloss:biz âlemlerin Rabbinin elçisiyiz, source:26:16} demeleri emredilir. Firavun sorar: {ar:وَمَا رَبُّ ٱلْعَٰلَمِينَ, tr:ve mâ rabbü'l-âlemîn, gloss:âlemlerin Rabbi de nedir, source:26:23}. Musa tamlamayı üç adımda açar. Önce {ar:رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَآ, tr:rabbü's-semâvâti ve'l-ardı ve mâ beynehümâ, gloss:göklerin, yerin ve ikisinin arasındakilerin Rabbi, source:26:24} der. Sonra {ar:رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ, tr:rabbüküm ve rabbü âbâikümü'l-evvelîn, gloss:sizin de önceki atalarınızın da Rabbi, source:26:26} der. En sonunda da {ar:رَبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَمَا بَيْنَهُمَآ, tr:rabbü'l-meşrikı ve'l-magribi ve mâ beynehümâ, gloss:doğunun, batının ve ikisinin arasındakilerin Rabbi, source:26:28} der. Firavun arada çevresindekilere dinlemiyor musunuz diye sorar {source:26:25} ve elçiye deli der {source:26:27}. Musa'nın cevabında âlemler soyut bir "evren" değildir. Onlar gök ile yer, kuşaklar boyu yaşamış insanlar, güneşin doğduğu ve battığı yerlerdir. Tartışmanın neden bu kadar sertleştiğini Kur'an başka bir yerde Firavun'un kendi sözüyle gösterir: {ar:أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:ene rabbükümü'l-a'lâ, gloss:en yüce rabbiniz benim, source:79:24}. Bir hükümdarın halkına "rabbiniz" demesi kelimenin alışılmış kullanımı içinde kalır. "Âlemlerin Rabbi" sözü ise onun ülkesini de halkını da bu tamlamanın küçük bir parçası haline getirir.

## Halden hale: yetiştiren Rab

[¶11] Sahiplik anlamının yanında kelimenin ikinci büyük kolu yetiştirmektir. Araplar çocuğunu büyüten için {ar:رب فلان ولده؛ رباه, tr:rabbe fülânün veledehû, rabbâh, gloss:falanca çocuğunu büyüttü, yetiştirdi, source:"ر ب ب,B002"} derlerdi. Bir mülkü düzene koyana da {ar:رب الضيعة أي أصلحها وأتمها, tr:rabbe'd-day'a, gloss:arazisini düzeltip tamamladı, source:"ر ب ب,B002"} derlerdi. Bu yetiştirmenin nasıl işlediği de tarif edilirdi: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve hüve inşâü'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale geçirerek tamamlanma sınırına kadar var etmektir, source:"ر ب ب,B002"}. Türkçe "terbiye" kelimesini bilir, ama onu büyük ölçüde görgüye ve kibar davranışa daraltmıştır. "Terbiyeli çocuk" sofrada nasıl oturacağını bilen çocuktur. Bu tanımdaki terbiye ise bir şeyi ilk halinden alıp aşama aşama tamamlanmasına kadar götüren uzun bir işlemdir. Bir kelimenin akrabalarından gelen böyle görüntüler, kelimenin ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Ayette "Rab" sahip ve efendidir. Yetiştirme bu anlamın yanında şunu duyurur: Âlemlerin Rabbi âlemleri bir defada yapıp bırakmaz, onları halden hale tamamlanmaya götürür.

[¶12] Kur'an bu iki aşamayı Firavun'un sarayında bir cevapta adlandırır. Firavun {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbükümâ yâ Mûsâ, gloss:ey Musa, ikinizin Rabbi kim, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbünellezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz, her şeye yaratılışını veren, sonra ona yolunu gösterendir, source:20:50}. Önce verilen bir yaratılış, sonra gösterilen bir yol vardır. Rab kelimesi bu cevapta "halden hale" yetiştirmenin iki basamağıyla tanımlanır.

[¶13] Aynı fiil bir iyiliği tamamlamak için de kullanılırdı: {ar:رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe fülânüni's-sanî'ate, gloss:falanca yaptığı iyiliği tamamlayıp düzene koydu, source:"ر ب ب,B002"}. Bir başka söyleyiş de şuydu: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-racülü'n-ni'mete yerubbühâ, gloss:adam nimeti tamamladı, source:"ر ب ب,B002"}. Nimetin kendisine de bu kökten bir ad verilirdi: {ar:الربى: النعمة والإحسان, tr:er-rubbâ: en-ni'metü ve'l-ihsân, gloss:rubbâ nimet ve iyiliktir, source:"ر ب ب,B016"}. Hamd böylece iyiliği yarıda bırakmayıp tamamlayana yönelir. Sure nimeti ancak yedinci ayette {ar:أَنْعَمْتَ عَلَيْهِمْ, tr:en'amte aleyhim, gloss:onlara nimet verdin, source:1:7} diye adıyla anar. Hamdın bu adlandırmadan önce gelmesi, surenin iyilik ile ona verilen cevap arasında kurduğu sırayı belirler.

[¶14] Kelimenin ailesi yetiştirmeyi yakın ve somut sahnelerle de anlatır. Üvey çocuk bu adla anılırdı: {ar:ربيب الرجل: ابن امرأته من غيره, tr:rabîbü'r-racül: ibnü'mraetihî min gayrih, gloss:bir adamın rabîbi, karısının başka birinden olan oğludur, source:"ر ب ب,B005"}. Çocuğu büyütmeyi üstlenen üvey ebeveyne de aynı kökten ad verilirdi: {ar:الراب والرابة بأحد الزوجين إذا تولى تربية الولد, tr:er-râbbü ve'r-râbbe, gloss:râb ve râbbe, eşlerden biri çocuğun terbiyesini üstlendiğinde ona verilen addır, source:"ر ب ب,B005"}. Bu adlar doğurmaktan değil, bakım üstlenmekten doğan bir bağı gösterir. Kur'an, evlenilmesi yasak kadınları sayarken üvey kızları şöyle anar: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rabâibükümü'llâtî fî hucûriküm, gloss:kucağınızda büyüyen üvey kızlarınız, source:4:23}. Rabîbe kucakta büyüyen çocuktur. Sütü için evde tutulan koyun da bu kökten adlandırılırdı: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtü'r-rubbâ, gloss:rubbâ, sütü için evde alıkonan koyundur, source:"ر ب ب,B009"}. Yeni doğurmuş koyun sürüyle birlikte otlağa gönderilmez, evde kalır ve sütü ev halkını besler. Yetiştirme burada yakından, el altında yapılan bir beslemedir. Surede bu yetiştirme, birinci ve üçüncü ayetlerdeki "Rahmân" ve "Rahîm" adlarının arasına yerleşir. Rahim ve büyütme sahnesi bu iki ayetin kelimeleriyle tamamlanır.

[¶15] Yetiştirme öğretmeye de uzanır. Rabbâniye şöyle bir tanım verilirdi: {ar:العالم المعلم الذي يغذو الناس بصغار العلوم, tr:el-âlimü'l-muallimü'llezî yağzu'n-nâse bi-sığâri'l-ulûm, gloss:insanları bilginin önce küçük parçalarıyla besleyen öğretici bilgin, source:"ر ب ب,B003"}. Bu tanımda ayetteki tamlamanın iki kökü tek bir kişide birleşir. Rabbânî, "âlemîn" kelimesiyle aynı kökten gelen bilgiyi, öğrenenin büyümesine göre ölçüp verir. Kur'an bu adı öğretmeye bağlar. Kendisine kitap, hüküm ve peygamberlik verilen bir insanın "Allah'ı bırakıp bana kul olun" demesinin olamayacağını söyler ve şöyle devam eder: {ar:وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ, tr:ve lâkin kûnû rabbâniyyîne bimâ küntüm tu'allimûne'l-kitâbe ve bimâ küntüm tedrusûn, gloss:kitabı öğretmeniz ve okuyup incelemeniz sebebiyle rabbâniler olun, source:3:79}.

[¶16] Kur'an'daki çocuğun duası bu yakınlığı başka bir fiille dile getirir: {ar:وَقُل رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:ve kul rabbi'rhamhümâ kemâ rabbeyânî sağîrâ, gloss:de ki: Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et, source:17:24}. "Rabbeyânî" ayrı ama sesçe çok yakın bir kökten gelir, dolayısıyla "Rab" ile aynı kelime değildir. Yine de Araplar yetiştirmeyi bu iki kökün biçimleriyle yan yana söylerlerdi: {ar:ربه ورباه ورببه, tr:rabbehû ve rabbâhû ve rabbebehû, gloss:onu yetiştirdi, source:"ر ب ب,B002"}. Duada çocuk Allah'a "Rabbim" diye seslenir ve kendisini büyütenlere, onların kendisini büyüttüğü gibi davranmasını ister.

## Bulutun altındaki yurt

[¶17] Araplar bir tür buluta "rabâb" derlerdi ve bu adın sebebini de söylerlerdi: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâbü's-sehâb, sümmiye bi-zâlike li-ennehû yerubbü'n-nebât, gloss:rabâb buluttur; bitkiyi yetiştirdiği için bu adı almıştır, source:"ر ب ب,B008"}. Bu bulut belirli bir biçimdedir: {ar:الربابة: السحابة التي قد ركب بعضها بعضا, tr:er-rabâbetü's-sehâbetü'lletî kad rekibe ba'duhâ ba'dâ, gloss:rabâbe, katmanları üst üste binmiş buluttur, source:"ر ب ب,B008"}. Asıl bulut kütlesinin altında da durur: {ar:السحاب المتعلق دون السحاب يكون أبيض ويكون أسود, tr:es-sehâbü'l-müteallaku dûne's-sehâb, gloss:asıl bulutun altında asılı duran, kimi beyaz kimi kara bulut, source:"ر ب ب,B008"}. Gözünüzün önüne şöyle bir manzara getirebilirsiniz: Yüksekteki bulut kütlesinin altında toprağa yakın sarkan, katman katman bir bulut saçağı. Yağmuru getiren budur. Bu bulut gelip geçmez, bir yerde kalır: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe, gloss:bulut kalıp sürdü, source:"ر ب ب,B007"}.

[¶18] Bulutun altında olanlar da aynı kökle adlandırılır. Yazın kurumayan körpe bitkiler bunlardan biridir: {ar:الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف, tr:er-ribbetü bakletün nâime, gloss:ribbe, yazın solmayan birçok körpe bitkinin adıdır, source:"ر ب ب,B012"}. Bir yerde toplanmış bol su da öyledir: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab, ve hüve'l-mâü'l-kesîr, sümmiye bi-zâlike li'ctimâih, gloss:rabab bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Develerin ayrılmadan kaldığı yere {ar:مرب الإبل حيث لزمته, tr:merabbü'l-ibil, gloss:develerin merabbı, ayrılmadıkları yerdir, source:"ر ب ب,B007"} denirdi. Böyle bir yere gelip orayı deneyen kişi hamdın fiilini kullanırdı: {ar:أحمدت الأرض إذا رضيت سكناها أو مرعاها, tr:ahmedtü'l-ard, gloss:o toprağı beğendim, orada oturmaktan ya da otlağından hoşnut kaldım, source:"ح م د,B002"}. Ayetin iki kelimesi bu tek manzarada buluşur. "Rab" bitkiyi büyüten bulutun, toplanan suyun ve hayvanların ayrılmadığı yerin adıdır. "Hamd" ise o toprağı deneyip kalmaya değer bulan kişinin verdiği hükümdür. Ayette bu iki kelime yan yana durur. Sürünün bu sahnesi yedinci ayetin son kelimesinde tamamlanır. Orada "dâllîn" kelimesinin ailesi, sahibinden kopmuş, sahibi bilinmeyen başıboş deveyi gösterir {source:1:7}. "Âlemîn" kelimesinin kökü de suyu bol kuyuya ad verir: {ar:العيلم الركية الكثيرة الماء, tr:el-aylemü'r-rakiyyetü'l-kesîretü'l-mâ', gloss:aylem, suyu bol kuyudur, source:"ع ل م,B005"}. Kuyu başındaki kiriş ve makara sahnesi ise altıncı ve yedinci ayetlerin kelimeleriyle kurulur.

[¶19] Kur'an katmanlı bulutu başka bir kelimeyle anlatır: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ, tr:e-lem tera ennallâhe yüzcî sehâben sümme yüellifu beynehû sümme yec'aluhû rukâmen fe-tera'l-vedka yahrucu min hılâlih, gloss:görmez misin, Allah bulutu sürer, sonra onları birleştirir, sonra üst üste yığar; yağmurun aralarından çıktığını görürsün, source:24:43}. Musa'nın Firavun'a verdiği cevap da yaratılış ve yol gösterme ile bitmez, bu manzaraya varır. Rabbini şöyle anlatmayı sürdürür: {ar:وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:ve enzele mine's-semâi mâen fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:gökten su indirdi, biz de onunla çeşit çeşit bitki çiftleri çıkardık, source:20:53}. Ardından şunu söyler: {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ, tr:külû ver'av en'âmeküm, gloss:yiyin ve hayvanlarınızı otlatın, source:20:54}. "Rabbiniz kim" sorusuna verilen cevap bir otlakta biter.

## Dağılanı bir arada tutan

[¶20] Kelimenin bir kolu toplamayı ve bir arada tutmayı anlatır. Eski Araplar işaretli oklarla kura çekerlerdi. Bu okları bir arada tutan kılıfa da bu kökten ad verirlerdi: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbetü şebîhetün bi'l-kinâneti tücme'u fîhâ sihâmü'l-meysir, gloss:ribâbe, okluğa benzeyen ve kura okları içinde toplanan kılıftır, source:"ر ب ب,B010"}. Kılıf olmasa oklar dağılırdı. Tarafları birbirine bağlayan söze de aynı ad verilirdi: {ar:الربابة: العهد والميثاق؛ الأربة أهل الميثاق, tr:er-ribâbetü'l-ahdü ve'l-mîsâk, el-erabbetü ehlü'l-mîsâk, gloss:ribâbe ahit ve sözleşmedir; erabbe, sözleşmeye bağlı olanlardır, source:"ر ب ب,B011"}. Bir başkasıyla dostluk bağı kurmak da böyle adlandırılırdı: {ar:العقد في موالاة الغير: الربابة, tr:el-akdü fî muvâlâti'l-gayr, gloss:başkasıyla dostluk bağıtı ribâbedir, source:"ر ب ب,B011"}. Kalabalıklar da bu kökle anılırdı: {ar:الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا, tr:er-ribbiyyü vâhidü'r-ribbiyyîn, ve hümü'l-ülûf mine'n-nâs; er-ribâbü hamsü kabâile tecemme'û, gloss:ribbiyyûn binlerce insandır; ribâb, bir araya gelmiş beş kabiledir, source:"ر ب ب,B004"}. Yaban sığırı sürüsüne de {ar:الربرب: القطيع من بقر الوحش, tr:er-rabrab: el-katî'u min bakari'l-vahş, gloss:rabrab, yaban sığırı sürüsüdür, source:"ر ب ب,B014"} denirdi. Bu sürünün adı toplanma anlamına bağlanır: {ar:يجوز أن يضم الربرب إلى الباب الثالث لتجمعه, tr:yecûzu en yudamme'r-rabrabu ile'l-bâbi's-sâlis li-tecemmu'ih, gloss:rabrab toplanmış olduğu için toplama anlamının altına konabilir, source:"ر ب ب,B014"}. Toplanmış suyun da aynı sebeple bu adı aldığı yukarıda geçti.

[¶21] Bu kollar ayetteki "Rab" kelimesinin anlamını değiştirmez. Ama tamlamanın ikinci kelimesinin bir çoğul olduğunu hatırlatır. Âlemler çoktur ve türlü türlüdür. Böyle bir çokluğun Rabbi, okları bir arada tutan kılıf ya da tarafları birbirine bağlayan söz gibi, dağılabilecek olanı bir arada tutandır. Bu dalların hepsi aynı köke aittir. Onları âlemlerin Rabbiyle buluşturan ise kelimenin kendisi değil, bu okumadır. Kur'an kökün kalabalık anlamına gelen kelimesini de kullanır: {ar:وَكَأَيِّن مِّن نَّبِىٍّۢ قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ, tr:ve keeyyin min nebiyyin kâtele meahû ribbiyyûne kesîr, gloss:nice peygamber vardır ki onunla birlikte pek çok ribbiyyûn savaştı, source:3:146}. Ayet bu kalabalıkların başlarına gelenler yüzünden gevşemediklerini söyler.

[¶22] Kur'an insanın Rabbiyle kurduğu ilk bağı da bir söz olarak anlatır. Rab, Âdemoğullarının sırtlarından soylarını alır ve onları kendilerine şahit tutar: {ar:أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ ۛ شَهِدْنَآ, tr:e-lestü bi-rabbiküm, kâlû belâ, şehidnâ, gloss:ben sizin Rabbiniz değil miyim? "Evet, şahit olduk" dediler, source:7:172}. Ayet bunun sebebini de söyler: İnsanlar diriliş günü bundan habersiz olduklarını öne sürmesinler. Bir sonraki ayete göre şunu da diyemesinler: Bizden önce atalarımız şirk koştu, biz de onlardan sonra gelen bir soyduk {source:7:173}. Bu söz "Rab" kelimesi üzerinde alınır. Araplar bağlayıcı söze de "ribâbe" derlerdi. Bu sözün koruma isteyenle bağı ise altıncı ayetteki "ihdinâ" kelimesinin ailesindeki, eve götürülen ve korunan kişi sahnesinde kurulur.

## Âlemler: tanınmak için dikilmiş işaretler

[¶23] Türkçede "âlem" dünya demektir. Ama kelime kalabalığı da anlatır ("âlem ne der"), gece eğlencesini de ("âlem yapmak"). Bu kullanımlarda kelimenin Arapçadaki ilk anlamı kaybolmuştur. Arapçada âlem, aslında bir şeyin kendisiyle bilindiği şeyin adıdır: {ar:العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به, tr:el-âlemü ismün li'l-feleki ve mâ yahvîh, ve hüve fi'l-asli ismün li-mâ yu'lemü bih, gloss:âlem gök küresinin ve içindekilerin adıdır; aslında bir şeyin onunla bilindiği şeyin adıdır, source:"ع ل م,B003"}. Çoğul hali de şöyle açıklanırdı: {ar:العالمون كل جنس من الخلق فهو في نفسه معلم وعلم, tr:el-âlemûne küllü cinsin mine'l-halk, fe-hüve fî nefsihî ma'lemun ve alem, gloss:âlemler yaratılmışların her bir türüdür; her biri kendi başına bir işaret ve bir nişandır, source:"ع ل م,B003"}. Kelime çoğul yapılırken genellikle akıllı varlıklar için kullanılan eki alır. Kapsamı da şöyle söylenirdi: {ar:العالمين رب الجن والإنس ورب الخلق كلهم, tr:rabbi'l-âlemîn: rabbü'l-cinni ve'l-ins ve rabbü'l-halki küllihim, gloss:âlemlerin Rabbi, cinlerin, insanların ve bütün yaratılmışların Rabbidir, source:"ع ل م,B003"}.

[¶24] Kökün temel anlamı bir şeyi başkalarından ayıran izdir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedüllü alâ eserin bi'ş-şey'i yetemeyyezü bihî an gayrih, gloss:bir şeyi başkasından ayıran bir ize işaret eden tek ve sağlam bir kök, source:"ع ل م,B002"}. Bu izin dört somut biçimi vardır ve her biri bir iş görür. Sancak, savaşta askerlerin nerede toplanacaklarını bilsinler diye yükseltilir: {ar:العلم الراية والجمع أعلام, tr:el-alemü'r-râye ve'l-cem'u a'lâm, gloss:alem sancaktır, çoğulu a'lâmdır, source:"ع ل م,B002"}. Uzaktan görünen yüksek dağ, çöldeki yolcuya yön verir: {ar:العلم الجبل الطويل والجميع الأعلام, tr:el-alemü'l-cebelü't-tavîl, gloss:alem uzun dağdır, source:"ع ل م,B002"}. Yoldaki iz, yolun nereden geçtiğini gösterir: {ar:المعلم الأثر يستدل به على الطريق, tr:el-ma'lemü'l-eseru yüstedellü bihî ale't-tarîk, gloss:ma'lem, yolu bulmak için bakılan izdir, source:"ع ل م,B002"}. Kumaşın kenarına dokunan desen de kumaşın ne olduğunu ve kime ait olduğunu söyler: {ar:علم الثوب ورقمه في أطرافه, tr:alemü's-sevbi ve rakmuhû fî etrâfih, gloss:kumaşın alemi, kenarlarındaki işareti ve desenidir, source:"ع ل م,B002"}. Dördünün de görevi, kendinden ötesini göstermektir. Bu işaretlerin amacı da bilmektir: {ar:العلم نقيض الجهل, tr:el-ilmü nakîdu'l-cehl, gloss:bilgi bilgisizliğin karşıtıdır, source:"ع ل م,B001"}, {ar:علمت الشيء عرفته, tr:alimtü'ş-şey'e araftüh, gloss:şeyi bildim, tanıdım, source:"ع ل م,B001"}.

[¶25] Ayette "âlemîn" bütün varlıklar demektir. Bu anlamın yanında şu da duyulur: Her tür, Rabbinin kendisiyle tanındığı bir işarettir. Âlemlerin Rabbi, bütün bu işaretlerin gösterdiği Rab'dir. Kur'an hamdı, işaretleri ve tanımayı bir ayette bir araya getirir. Neml suresinin sonunda Peygambere Kur'an'ı okuması emredilir ve kim doğru yolu bulursa kendisi için bulacağı söylenir {source:27:92}. Ardından şu gelir: {ar:وَقُلِ ٱلْحَمْدُ لِلَّهِ سَيُرِيكُمْ ءَايَٰتِهِۦ فَتَعْرِفُونَهَا, tr:ve kuli'l-hamdü lillâhi seyurîküm âyâtihî fe-ta'rifûnehâ, gloss:de ki: hamd Allah'adır; size işaretlerini gösterecek, siz de onları tanıyacaksınız, source:27:93}. Kur'an, denizde yüzen gemileri anlatırken bu kökün dağ anlamındaki çoğulunu kullanır: {ar:وَمِنْ ءَايَٰتِهِ ٱلْجَوَارِ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ, tr:ve min âyâtihi'l-cevâri fi'l-bahri ke'l-a'lâm, gloss:denizde dağlar gibi akıp giden gemiler de O'nun işaretlerindendir, source:42:32}. Sonraki ayet, O dilerse rüzgârı dindireceğini ve gemilerin suyun sırtında kımıldamadan kalacağını söyler. Bu da sabreden ve şükreden herkes için bir işarettir {source:42:33}. Yolcunun yön bulmak için baktığı nişanlar ise altıncı ayetteki yol isteğinin sahnesine aittir. Bu sahnede yolcu {ar:وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ, tr:ve alâmât, ve bi'n-necmi hüm yehtedûn, gloss:nişanlar da koydu; yıldızla da yollarını bulurlar, source:16:16} ayetindeki işaretlere bakar. Câsiye suresi de kendi sonunda âlemleri açar: {ar:فَلِلَّهِ ٱلْحَمْدُ رَبِّ ٱلسَّمَٰوَٰتِ وَرَبِّ ٱلْأَرْضِ رَبِّ ٱلْعَٰلَمِينَ, tr:fe-lillâhi'l-hamdü rabbi's-semâvâti ve rabbi'l-ardı rabbi'l-âlemîn, gloss:hamd göklerin Rabbi, yerin Rabbi, âlemlerin Rabbi olan Allah'adır, source:45:36}.

[¶26] Tanıma bir yönde işlemez. Firavun, Musa'nın cevabından sonra eski kuşakların durumunu sorar {source:20:51}. Musa şöyle der: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmühâ inde rabbî fî kitâb, lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Âlemler, yaratılmışların Rablerini tanıdığı işaretlerdir. Âlemlerin bilgisi ise Rablerinin katındadır ve orada kaybolmaz. Musa'nın burada kullandığı "yanılmak" fiili, surenin son kelimesi olan "dâllîn" ile aynı köktendir. Birinci ayetteki "bism" kelimesiyle kurulan ad ve damga sahnesi de aynı işi görür. Ad, adlandırılanın tanınması için yükseltilmiş bir işarettir.

## Batmayan Rab

[¶27] "Âlem" kelimesi gök küresine ve onun içindekilere de verilen addır {source:"ع ل م,B003"}. Yıldızlar, ay ve güneş bu kürenin içindedir. "Allah" adının kökü ise güneşe de bir ad vermiştir ve bu adın sebebi de söylenirdi: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetü'ş-şems, sümmiyet bi-zâlike li-enne kavmen kânû ya'büdûnehâ, gloss:ilâhe güneştir; bir kavim ona taptığı için bu adı almıştır, source:"ء ل ه,B001"}. Ad tapınmayı izlemiştir. Tapılan bir ışık, tapılan olmanın adını almıştır.

[¶28] Kur'an, gökteki bu ışıklara "Rab" kelimesinin tek tek sorulduğu bir sahne anlatır. Gece İbrahim'i örttüğünde bir yıldız görür ve "bu benim Rabbim" der. Yıldız batınca şöyle der: {ar:لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:lâ uhibbü'l-âfilîn, gloss:batıp kaybolanları sevmem, source:6:76}. Doğmakta olan ayı görür, aynı sözü söyler. Ay da batınca şöyle der: {ar:لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ, tr:le-in lem yehdinî rabbî le-ekûnenne mine'l-kavmi'd-dâllîn, gloss:Rabbim beni doğru yola iletmezse yolunu yitirmiş kavimden olurum, source:6:77}. Doğan güneşi görünce "bu daha büyük" der. Güneş de batınca kavmine onların ortak koştuklarından uzak olduğunu söyler {source:6:78}. Sonunda yüzünü çevirir: {ar:إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا, tr:innî veccehtü vechiye lillezî fatara's-semâvâti ve'l-arda hanîfâ, gloss:ben hanif olarak yüzümü gökleri ve yeri yaratana çevirdim, source:6:79}. İbrahim'in ölçütü batmaktır. Batan şey bir işarettir, bir âlemdir, ama Rab olamaz.

[¶29] "Rab" kelimesinin ailesinde bu ölçütün tam karşılığı vardır. Bir yerde kalıp oradan ayrılmayana {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fülânün bi'l-mekâni izâ ekâme bihî fe-lem yebrahhu, gloss:falanca bir yerde kaldı ve oradan ayrılmadı, source:"ر ب ب,B007"} denirdi. Yıldız, ay ve güneş için ise Kur'an "efele" der, yani batıp kayboldular. Bu ikisini karşı karşıya koyan Kur'an'ın kelimesi değil, bu okumadır. Ama İbrahim'in sahnesi tam da bu karşıtlık üzerine kuruludur. Rab sanılan her şey bir süre görünüp gitmiştir. Rab ise yerinde kalandır. Aynı İbrahim başka bir yerde kavmine ve atalarına neye taptıklarını sorar {source:26:70}. Taptıkları şeyleri sayar {source:26:76} ve şöyle der: {ar:فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ, tr:fe-innehüm adüvvün lî illâ rabbe'l-âlemîn, gloss:onlar benim düşmanımdır, yalnız âlemlerin Rabbi müstesna, source:26:77}. Âlemlerin Rabbini anlatırken de evrenden değil, kendi bedeninden söz eder: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-hüve yehdîn, gloss:beni yaratan ve bana yolu gösteren O'dur, source:26:78}. Ardından {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî hüve yut'imunî ve yeskîn, gloss:beni yediren ve içiren O'dur, source:26:79} der ve hastalandığında kendisine şifa verenin de O olduğunu ekler {source:26:80}. Bütün âlemlerin Rabbi, tek bir insanın ekmeğini ve suyunu veren Rab'dir. Bu, yetiştirmenin en yakın ölçeğidir. Gök sahnesinin öbür parçaları, yani dördüncü ayetteki günün güneşin doğuşu ile batışı arasındaki uzunluğu ve altıncı ayetteki "müstakîm" kelimesinin ailesindeki öğle dengesi, o ayetlerin kelimeleriyle kurulur.

## Sona saklanan söz, başta söylenir

[¶30] Kur'an, ikinci ayetin cümlesini birçok yerde bir şeyin sonuna koyar. Cennet ehlinin orada ettikleri dua "sübhânekellâhümme", birbirlerini selamlamaları "selâm" diye anlatılır ve şöyle devam eder: {ar:وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve âhiru da'vâhüm eni'l-hamdü lillâhi rabbi'l-âlemîn, gloss:dualarının sonu da "hamd âlemlerin Rabbi Allah'adır" sözüdür, source:10:10}. Zümer suresinin sonunda Rablerinden sakınanlar cennete götürülür. Onlar kendilerine verdiği sözü yerine getiren Allah'a hamd ederler {source:39:74}. Ardından melekler Arş'ın çevresinde Rablerini hamd ile tesbih ederken gösterilir ve hüküm verilir: {ar:وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَقِيلَ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve kudıye beynehüm bi'l-hakkı ve kîle'l-hamdü lillâhi rabbi'l-âlemîn, gloss:aralarında hakla hüküm verildi ve "hamd âlemlerin Rabbi Allah'adır" denildi, source:39:75}. Bu sözü söyleyenin adı geçmez. Fiil edilgendir, "denildi". Bu, Fâtiha'daki öznesiz cümlenin aynısıdır. Hüküm verilmiştir ve hamd, kimin ağzından çıktığı söylenmeden yerini bulur. Sâffât suresi de Rabbin nitelendirmelerden uzak olduğunu söyleyip elçilere selam verdikten {source:37:180} sonra aynı cümleyle kapanır: {ar:وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve'l-hamdü lillâhi rabbi'l-âlemîn, gloss:hamd âlemlerin Rabbi Allah'adır, source:37:182}. Zulmeden kavmin kökünün kesildiği hikâye de, yukarıda görüldüğü gibi, aynı sözle biter.

[¶31] Araplar bir kimsenin çabasıyla varabileceği en uç noktaya da bu kökten bir ad verirlerdi: {ar:حماداك أن تفعل كذا أي غايتك وفعلك المحمود, tr:hamâdâke en tef'ale kezâ, ey gâyetüke ve fi'lüke'l-mahmûd, gloss:senin varabileceğin en ileri nokta şunu yapmaktır, yani son hedefin ve övülecek işin, source:"ح م د,B004"}. Bir başka açıklama şöyleydi: {ar:حماداك في معنى قصاراك, tr:hamâdâke fî ma'nâ kusârâke, gloss:hamâdâk, elinden gelebilecek en son şey demektir, source:"ح م د,B004"}. Hamdın kökü varılabilecek son sınıra ad verir. Kur'an da hamd cümlesini işlerin bu son sınıra vardığı anlarda söyletir: bir hükmün ardından, bir hikâyenin sonunda, cennettekilerin son sözü olarak. Bir başka ayet bunu açıkça söyler: {ar:لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ, tr:lehü'l-hamdü fi'l-ûlâ ve'l-âhira, gloss:dünyada da ahirette de hamd O'nundur, source:28:70}.

[¶32] Fâtiha ise bu sonu başa koyar. Hamd normalde bir deneyimden sonra verilen onaydır. Bir toprak içinde yaşandıktan, bir kişi sınandıktan sonra söylenir. Okuyan ise onu altıncı ayette yol istemeden önce, yolun daha başındayken söyler. Bu onayın dayanağı, ikinci ayetin kendi son kelimesindedir. Âlemler, Rabbin kendileriyle tanındığı işaretlerdir. Yol henüz yürünmemiştir, ama işaretler görülmüştür. Kur'an'ın bir hükümden sonra "denildi" diye aktardığı söz, Fâtiha'yı okuyanın ağzında, Allah'ın adından hemen sonra gelen ilk sözdür.

===== _commentary/v16/out/1_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: verbless nominal sentence expresses a settled state, not an act
- memory: lām in لِلَّهِ marks belonging/entitlement
- memory: ʿālamūn/ʿālamīn takes the sound plural ending normally used for rational beings
- memory: رَبَّيَانِى belongs to the neighbouring root ر ب و, not ر ب ب
- memory: رُكَام (24:43) is from a different root than رباب
- memory: ancient Arabs cast lots with marked arrows (gloss of B010 context)
- not written: و ل ه alternative derivation of the divine name - contested origin; would compete with the identity root rather than sit beside it
- not written: ر ب ب B006 thick fruit syrup / ghee residue - no theme it could ground or join
- not written: ر ب ب B015 particle rubba - attested as having no derivation; no image
- not written: ر ب ب B017 ship captain - single attestation; joins no theme
- not written: ر ب ب B016 need, firm knot - knot could join "gathering" but too thin; only favour sense used
- not written: ر ب ب B009 first youth / freshness - weaker than the milk-ewe image already used
- not written: ح م د B003 maḥmūd/muḥammad, B006 praising "with you" - no theme needed them beyond hamd as verdict
- not written: ع ل م B004 harelip, B006 falcon, B007 male hyena - no bearing on the ayah's themes
- not written: echo root ر ب و (increase, hill) - withheld; used only to keep rabbayānī distinct
- not written: 16:75 parable ending in al-ḥamdu lillāh - belongs to the owner/servant scene of the surah commentary

===== passages not cited (267) =====
## strong (this ayah's own list) (13)

- (2:131) [listed for 1:2] إِذْ قَالَ لَهُۥ رَبُّهُۥٓ أَسْلِمْ ۖ قَالَ أَسْلَمْتُ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:45) [listed for 1:2] [cited in ¶6] فَقُطِعَ دَابِرُ ٱلْقَوْمِ ٱلَّذِينَ ظَلَمُوا۟ ۚ وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (17:111) [listed for 1:2] وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ ۖ وَكَبِّرْهُ تَكْبِيرًۢا
- (28:30) [listed for 1:2] فَلَمَّآ أَتَىٰهَا نُودِىَ مِن شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ فِى ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ مِنَ ٱلشَّجَرَةِ أَن يَٰمُوسَىٰٓ إِنِّىٓ أَنَا ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (32:2) [listed for 1:2] تَنزِيلُ ٱلْكِتَٰبِ لَا رَيْبَ فِيهِ مِن رَّبِّ ٱلْعَٰلَمِينَ
- (37:182) [listed for 1:2] [cited in ¶30] وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (45:36) [listed for 1:2] [cited in ¶25] فَلِلَّهِ ٱلْحَمْدُ رَبِّ ٱلسَّمَٰوَٰتِ وَرَبِّ ٱلْأَرْضِ رَبِّ ٱلْعَٰلَمِينَ
- (83:6) [listed for 1:2] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
- (93:3) [listed for 1:2] مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ
- (93:11) [listed for 1:2] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (100:6) [listed for 1:2] إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- (106:3) [listed for 1:2] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- (106:4) [listed for 1:2] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ

## medium (this ayah's own list) (60)

- (3:188) [listed for 1:2] [cited in ¶5] لَا تَحْسَبَنَّ ٱلَّذِينَ يَفْرَحُونَ بِمَآ أَتَوا۟ وَّيُحِبُّونَ أَن يُحْمَدُوا۟ بِمَا لَمْ يَفْعَلُوا۟ فَلَا تَحْسَبَنَّهُم بِمَفَازَةٍۢ مِّنَ ٱلْعَذَابِ ۖ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- (5:28) [listed for 1:2] لَئِنۢ بَسَطتَ إِلَىَّ يَدَكَ لِتَقْتُلَنِى مَآ أَنَا۠ بِبَاسِطٍۢ يَدِىَ إِلَيْكَ لِأَقْتُلَكَ ۖ إِنِّىٓ أَخَافُ ٱللَّهَ رَبَّ ٱلْعَٰلَمِينَ
- (6:1) [listed for 1:2] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَجَعَلَ ٱلظُّلُمَٰتِ وَٱلنُّورَ ۖ ثُمَّ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ يَعْدِلُونَ
- (6:71) [listed for 1:2] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:162) [listed for 1:2] قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (7:43) [listed for 1:2] وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ ۖ وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى هَدَىٰنَا لِهَٰذَا وَمَا كُنَّا لِنَهْتَدِىَ لَوْلَآ أَنْ هَدَىٰنَا ٱللَّهُ ۖ لَقَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ ۖ وَنُودُوٓا۟ أَن تِلْكُمُ ٱلْجَنَّةُ أُورِثْتُمُوهَا بِمَا كُنتُمْ تَعْمَلُونَ
- (7:61) [listed for 1:2] قَالَ يَٰقَوْمِ لَيْسَ بِى ضَلَٰلَةٌۭ وَلَٰكِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (7:67) [listed for 1:2] قَالَ يَٰقَوْمِ لَيْسَ بِى سَفَاهَةٌۭ وَلَٰكِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (7:104) [listed for 1:2] وَقَالَ مُوسَىٰ يَٰفِرْعَوْنُ إِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (10:10) [listed for 1:2] [cited in ¶30] دَعْوَىٰهُمْ فِيهَا سُبْحَٰنَكَ ٱللَّهُمَّ وَتَحِيَّتُهُمْ فِيهَا سَلَٰمٌۭ ۚ وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (14:39) [listed for 1:2] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى وَهَبَ لِى عَلَى ٱلْكِبَرِ إِسْمَٰعِيلَ وَإِسْحَٰقَ ۚ إِنَّ رَبِّى لَسَمِيعُ ٱلدُّعَآءِ
- (15:98) [listed for 1:2] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ ٱلسَّٰجِدِينَ
- (16:75) [listed for 1:2] ۞ ضَرَبَ ٱللَّهُ مَثَلًا عَبْدًۭا مَّمْلُوكًۭا لَّا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَمَن رَّزَقْنَٰهُ مِنَّا رِزْقًا حَسَنًۭا فَهُوَ يُنفِقُ مِنْهُ سِرًّۭا وَجَهْرًا ۖ هَلْ يَسْتَوُۥنَ ۚ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (18:1) [listed for 1:2] ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَنزَلَ عَلَىٰ عَبْدِهِ ٱلْكِتَٰبَ وَلَمْ يَجْعَل لَّهُۥ عِوَجَا ۜ
- (18:27) [listed for 1:2] وَٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِن كِتَابِ رَبِّكَ ۖ لَا مُبَدِّلَ لِكَلِمَٰتِهِۦ وَلَن تَجِدَ مِن دُونِهِۦ مُلْتَحَدًۭا
- (19:65) [listed for 1:2] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:49) [listed for 1:2] [cited in ¶12] قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ
- (23:28) [listed for 1:2] فَإِذَا ٱسْتَوَيْتَ أَنتَ وَمَن مَّعَكَ عَلَى ٱلْفُلْكِ فَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى نَجَّىٰنَا مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (23:72) [listed for 1:2] أَمْ تَسْـَٔلُهُمْ خَرْجًۭا فَخَرَاجُ رَبِّكَ خَيْرٌۭ ۖ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ
- (23:117) [listed for 1:2] وَمَن يَدْعُ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ لَا بُرْهَٰنَ لَهُۥ بِهِۦ فَإِنَّمَا حِسَابُهُۥ عِندَ رَبِّهِۦٓ ۚ إِنَّهُۥ لَا يُفْلِحُ ٱلْكَٰفِرُونَ
- (26:16) [listed for 1:2] [cited in ¶10] فَأْتِيَا فِرْعَوْنَ فَقُولَآ إِنَّا رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- (26:23) [listed for 1:2] [cited in ¶10] قَالَ فِرْعَوْنُ وَمَا رَبُّ ٱلْعَٰلَمِينَ
- (26:47) [listed for 1:2] قَالُوٓا۟ ءَامَنَّا بِرَبِّ ٱلْعَٰلَمِينَ
- (26:77) [listed for 1:2] [cited in ¶29] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
- (26:98) [listed for 1:2] إِذْ نُسَوِّيكُم بِرَبِّ ٱلْعَٰلَمِينَ
- (26:192) [listed for 1:2] وَإِنَّهُۥ لَتَنزِيلُ رَبِّ ٱلْعَٰلَمِينَ
- (27:8) [listed for 1:2] فَلَمَّا جَآءَهَا نُودِىَ أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (27:15) [listed for 1:2] وَلَقَدْ ءَاتَيْنَا دَاوُۥدَ وَسُلَيْمَٰنَ عِلْمًۭا ۖ وَقَالَا ٱلْحَمْدُ لِلَّهِ ٱلَّذِى فَضَّلَنَا عَلَىٰ كَثِيرٍۢ مِّنْ عِبَادِهِ ٱلْمُؤْمِنِينَ
- (27:44) [listed for 1:2] قِيلَ لَهَا ٱدْخُلِى ٱلصَّرْحَ ۖ فَلَمَّا رَأَتْهُ حَسِبَتْهُ لُجَّةًۭ وَكَشَفَتْ عَن سَاقَيْهَا ۚ قَالَ إِنَّهُۥ صَرْحٌۭ مُّمَرَّدٌۭ مِّن قَوَارِيرَ ۗ قَالَتْ رَبِّ إِنِّى ظَلَمْتُ نَفْسِى وَأَسْلَمْتُ مَعَ سُلَيْمَٰنَ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (27:59) [listed for 1:2] قُلِ ٱلْحَمْدُ لِلَّهِ وَسَلَٰمٌ عَلَىٰ عِبَادِهِ ٱلَّذِينَ ٱصْطَفَىٰٓ ۗ ءَآللَّهُ خَيْرٌ أَمَّا يُشْرِكُونَ
- (27:93) [listed for 1:2] [cited in ¶25] وَقُلِ ٱلْحَمْدُ لِلَّهِ سَيُرِيكُمْ ءَايَٰتِهِۦ فَتَعْرِفُونَهَا ۚ وَمَا رَبُّكَ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (29:63) [listed for 1:2] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
- (31:25) [listed for 1:2] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (32:15) [listed for 1:2] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (34:1) [listed for 1:2] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَلَهُ ٱلْحَمْدُ فِى ٱلْءَاخِرَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (35:1) [listed for 1:2] ٱلْحَمْدُ لِلَّهِ فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ جَاعِلِ ٱلْمَلَٰٓئِكَةِ رُسُلًا أُو۟لِىٓ أَجْنِحَةٍۢ مَّثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ ۚ يَزِيدُ فِى ٱلْخَلْقِ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (35:34) [listed for 1:2] وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَذْهَبَ عَنَّا ٱلْحَزَنَ ۖ إِنَّ رَبَّنَا لَغَفُورٌۭ شَكُورٌ
- (37:4) [listed for 1:2] إِنَّ إِلَٰهَكُمْ لَوَٰحِدٌۭ
- (37:5) [listed for 1:2] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا وَرَبُّ ٱلْمَشَٰرِقِ
- (39:29) [listed for 1:2] ضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلًۭا فِيهِ شُرَكَآءُ مُتَشَٰكِسُونَ وَرَجُلًۭا سَلَمًۭا لِّرَجُلٍ هَلْ يَسْتَوِيَانِ مَثَلًا ۚ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (39:74) [listed for 1:2] [cited in ¶30] وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى صَدَقَنَا وَعْدَهُۥ وَأَوْرَثَنَا ٱلْأَرْضَ نَتَبَوَّأُ مِنَ ٱلْجَنَّةِ حَيْثُ نَشَآءُ ۖ فَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (39:75) [listed for 1:2] [cited in ¶30] وَتَرَى ٱلْمَلَٰٓئِكَةَ حَآفِّينَ مِنْ حَوْلِ ٱلْعَرْشِ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ ۖ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَقِيلَ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (40:65) [listed for 1:2] هُوَ ٱلْحَىُّ لَآ إِلَٰهَ إِلَّا هُوَ فَٱدْعُوهُ مُخْلِصِينَ لَهُ ٱلدِّينَ ۗ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (41:9) [listed for 1:2] ۞ قُلْ أَئِنَّكُمْ لَتَكْفُرُونَ بِٱلَّذِى خَلَقَ ٱلْأَرْضَ فِى يَوْمَيْنِ وَتَجْعَلُونَ لَهُۥٓ أَندَادًۭا ۚ ذَٰلِكَ رَبُّ ٱلْعَٰلَمِينَ
- (43:46) [listed for 1:2] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَقَالَ إِنِّى رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- (44:20) [listed for 1:2] وَإِنِّى عُذْتُ بِرَبِّى وَرَبِّكُمْ أَن تَرْجُمُونِ
- (56:74) [listed for 1:2] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (56:80) [listed for 1:2] تَنزِيلٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (64:1) [listed for 1:2] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ لَهُ ٱلْمُلْكُ وَلَهُ ٱلْحَمْدُ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (68:2) [listed for 1:2] مَآ أَنتَ بِنِعْمَةِ رَبِّكَ بِمَجْنُونٍۢ
- (69:43) [listed for 1:2] تَنزِيلٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (69:52) [listed for 1:2] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (73:9) [listed for 1:2] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (78:36) [listed for 1:2] جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا
- (79:44) [listed for 1:2] إِلَىٰ رَبِّكَ مُنتَهَىٰهَآ
- (81:29) [listed for 1:2] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (92:20) [listed for 1:2] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (93:5) [listed for 1:2] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (94:8) [listed for 1:2] وَإِلَىٰ رَبِّكَ فَٱرْغَب
- (100:11) [listed for 1:2] إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ

## named by the passage's own list as strong for this ayah (7)

- (28:70) [listed for 1:2] [cited in ¶31] وَهُوَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ ۖ وَلَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
- (36:25) [listed for 1:2] إِنِّىٓ ءَامَنتُ بِرَبِّكُمْ فَٱسْمَعُونِ
- (53:49) [listed for 1:2] وَأَنَّهُۥ هُوَ رَبُّ ٱلشِّعْرَىٰ
- (79:19) [listed for 1:2] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- (87:1) [listed for 1:2] سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- (110:3) [listed for 1:2] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا
- (114:1) [listed for 1:2] قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ

## named by the passage's own list as medium for this ayah (40)

- (2:139) [listed for 1:2] قُلْ أَتُحَآجُّونَنَا فِى ٱللَّهِ وَهُوَ رَبُّنَا وَرَبُّكُمْ وَلَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ وَنَحْنُ لَهُۥ مُخْلِصُونَ
- (3:51) [listed for 1:2] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (3:79) [listed for 1:2] [cited in ¶15] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
- (4:131) [listed for 1:2] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَلَقَدْ وَصَّيْنَا ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ وَإِيَّاكُمْ أَنِ ٱتَّقُوا۟ ٱللَّهَ ۚ وَإِن تَكْفُرُوا۟ فَإِنَّ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ وَكَانَ ٱللَّهُ غَنِيًّا حَمِيدًۭا
- (7:122) [listed for 1:2] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (7:125) [listed for 1:2] قَالُوٓا۟ إِنَّآ إِلَىٰ رَبِّنَا مُنقَلِبُونَ
- (9:31) [listed for 1:2] ٱتَّخَذُوٓا۟ أَحْبَارَهُمْ وَرُهْبَٰنَهُمْ أَرْبَابًۭا مِّن دُونِ ٱللَّهِ وَٱلْمَسِيحَ ٱبْنَ مَرْيَمَ وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ۚ سُبْحَٰنَهُۥ عَمَّا يُشْرِكُونَ
- (14:8) [listed for 1:2] وَقَالَ مُوسَىٰٓ إِن تَكْفُرُوٓا۟ أَنتُمْ وَمَن فِى ٱلْأَرْضِ جَمِيعًۭا فَإِنَّ ٱللَّهَ لَغَنِىٌّ حَمِيدٌ
- (15:87) [listed for 1:2] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (23:98) [listed for 1:2] وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ
- (26:48) [listed for 1:2] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (30:18) [listed for 1:2] وَلَهُ ٱلْحَمْدُ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَعَشِيًّۭا وَحِينَ تُظْهِرُونَ
- (31:26) [listed for 1:2] لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّ ٱللَّهَ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ
- (37:87) [listed for 1:2] فَمَا ظَنُّكُم بِرَبِّ ٱلْعَٰلَمِينَ
- (38:66) [listed for 1:2] رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلْعَزِيزُ ٱلْغَفَّٰرُ
- (39:31) [listed for 1:2] ثُمَّ إِنَّكُمْ يَوْمَ ٱلْقِيَٰمَةِ عِندَ رَبِّكُمْ تَخْتَصِمُونَ
- (43:14) [listed for 1:2] وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ
- (52:48) [listed for 1:2] وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا ۖ وَسَبِّحْ بِحَمْدِ رَبِّكَ حِينَ تَقُومُ
- (53:42) [listed for 1:2] وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ
- (55:17) [listed for 1:2] رَبُّ ٱلْمَشْرِقَيْنِ وَرَبُّ ٱلْمَغْرِبَيْنِ
- (55:27) [listed for 1:2] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (55:32) [listed for 1:2] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:34) [listed for 1:2] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:78) [listed for 1:2] تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (74:3) [listed for 1:2] وَرَبَّكَ فَكَبِّرْ
- (74:7) [listed for 1:2] وَلِرَبِّكَ فَٱصْبِرْ
- (74:31) [listed for 1:2] وَمَا جَعَلْنَآ أَصْحَٰبَ ٱلنَّارِ إِلَّا مَلَٰٓئِكَةًۭ ۙ وَمَا جَعَلْنَا عِدَّتَهُمْ إِلَّا فِتْنَةًۭ لِّلَّذِينَ كَفَرُوا۟ لِيَسْتَيْقِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَيَزْدَادَ ٱلَّذِينَ ءَامَنُوٓا۟ إِيمَٰنًۭا ۙ وَلَا يَرْتَابَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْمُؤْمِنُونَ ۙ وَلِيَقُولَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ وَٱلْكَٰفِرُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَمَا يَعْلَمُ جُنُودَ رَبِّكَ إِلَّا هُوَ ۚ وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ
- (78:37) [listed for 1:2] رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا
- (78:39) [listed for 1:2] ذَٰلِكَ ٱلْيَوْمُ ٱلْحَقُّ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا
- (79:24) [listed for 1:2] [cited in ¶10] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
- (83:15) [listed for 1:2] كَلَّآ إِنَّهُمْ عَن رَّبِّهِمْ يَوْمَئِذٍۢ لَّمَحْجُوبُونَ
- (85:12) [listed for 1:2] إِنَّ بَطْشَ رَبِّكَ لَشَدِيدٌ
- (85:15) [listed for 1:2] ذُو ٱلْعَرْشِ ٱلْمَجِيدُ
- (89:22) [listed for 1:2] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- (95:8) [listed for 1:2] أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ
- (96:1) [listed for 1:2] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- (96:3) [listed for 1:2] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- (96:4) [listed for 1:2] ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- (99:5) [listed for 1:2] بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- (109:3) [listed for 1:2] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ

## weak (this ayah's own list) (20)

- (2:5) [listed for 1:2] أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (8:53) [listed for 1:2] ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًۭا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۙ وَأَنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (14:7) [listed for 1:2] وَإِذْ تَأَذَّنَ رَبُّكُمْ لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ ۖ وَلَئِن كَفَرْتُمْ إِنَّ عَذَابِى لَشَدِيدٌۭ
- (18:50) [listed for 1:2] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ كَانَ مِنَ ٱلْجِنِّ فَفَسَقَ عَنْ أَمْرِ رَبِّهِۦٓ ۗ أَفَتَتَّخِذُونَهُۥ وَذُرِّيَّتَهُۥٓ أَوْلِيَآءَ مِن دُونِى وَهُمْ لَكُمْ عَدُوٌّۢ ۚ بِئْسَ لِلظَّٰلِمِينَ بَدَلًۭا
- (26:109) [listed for 1:2] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:127) [listed for 1:2] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:145) [listed for 1:2] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:164) [listed for 1:2] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:180) [listed for 1:2] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (27:42) [listed for 1:2] فَلَمَّا جَآءَتْ قِيلَ أَهَٰكَذَا عَرْشُكِ ۖ قَالَتْ كَأَنَّهُۥ هُوَ ۚ وَأُوتِينَا ٱلْعِلْمَ مِن قَبْلِهَا وَكُنَّا مُسْلِمِينَ
- (34:6) [listed for 1:2] وَيَرَى ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (37:41) [listed for 1:2] أُو۟لَٰٓئِكَ لَهُمْ رِزْقٌۭ مَّعْلُومٌۭ
- (37:164) [listed for 1:2] وَمَا مِنَّآ إِلَّا لَهُۥ مَقَامٌۭ مَّعْلُومٌۭ
- (53:5) [listed for 1:2] عَلَّمَهُۥ شَدِيدُ ٱلْقُوَىٰ
- (68:52) [listed for 1:2] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (71:28) [listed for 1:2] رَّبِّ ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِمَن دَخَلَ بَيْتِىَ مُؤْمِنًۭا وَلِلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ وَلَا تَزِدِ ٱلظَّٰلِمِينَ إِلَّا تَبَارًۢا
- (78:4) [listed for 1:2] كَلَّا سَيَعْلَمُونَ
- (92:19) [listed for 1:2] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (109:2) [listed for 1:2] لَآ أَعْبُدُ مَا تَعْبُدُونَ
- (109:6) [listed for 1:2] لَكُمْ دِينُكُمْ وَلِىَ دِينِ

## named by the passage's own list as weak for this ayah (33)

- (9:112) [listed for 1:2] ٱلتَّٰٓئِبُونَ ٱلْعَٰبِدُونَ ٱلْحَٰمِدُونَ ٱلسَّٰٓئِحُونَ ٱلرَّٰكِعُونَ ٱلسَّٰجِدُونَ ٱلْءَامِرُونَ بِٱلْمَعْرُوفِ وَٱلنَّاهُونَ عَنِ ٱلْمُنكَرِ وَٱلْحَٰفِظُونَ لِحُدُودِ ٱللَّهِ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (17:79) [listed for 1:2] وَمِنَ ٱلَّيْلِ فَتَهَجَّدْ بِهِۦ نَافِلَةًۭ لَّكَ عَسَىٰٓ أَن يَبْعَثَكَ رَبُّكَ مَقَامًۭا مَّحْمُودًۭا
- (18:38) [listed for 1:2] لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى وَلَآ أُشْرِكُ بِرَبِّىٓ أَحَدًۭا
- (18:40) [listed for 1:2] فَعَسَىٰ رَبِّىٓ أَن يُؤْتِيَنِ خَيْرًۭا مِّن جَنَّتِكَ وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا
- (18:82) [listed for 1:2] وَأَمَّا ٱلْجِدَارُ فَكَانَ لِغُلَٰمَيْنِ يَتِيمَيْنِ فِى ٱلْمَدِينَةِ وَكَانَ تَحْتَهُۥ كَنزٌۭ لَّهُمَا وَكَانَ أَبُوهُمَا صَٰلِحًۭا فَأَرَادَ رَبُّكَ أَن يَبْلُغَآ أَشُدَّهُمَا وَيَسْتَخْرِجَا كَنزَهُمَا رَحْمَةًۭ مِّن رَّبِّكَ ۚ وَمَا فَعَلْتُهُۥ عَنْ أَمْرِى ۚ ذَٰلِكَ تَأْوِيلُ مَا لَمْ تَسْطِع عَّلَيْهِ صَبْرًۭا
- (18:109) [listed for 1:2] قُل لَّوْ كَانَ ٱلْبَحْرُ مِدَادًۭا لِّكَلِمَٰتِ رَبِّى لَنَفِدَ ٱلْبَحْرُ قَبْلَ أَن تَنفَدَ كَلِمَٰتُ رَبِّى وَلَوْ جِئْنَا بِمِثْلِهِۦ مَدَدًۭا
- (19:36) [listed for 1:2] وَإِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (21:56) [listed for 1:2] قَالَ بَل رَّبُّكُمْ رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ٱلَّذِى فَطَرَهُنَّ وَأَنَا۠ عَلَىٰ ذَٰلِكُم مِّنَ ٱلشَّٰهِدِينَ
- (25:77) [listed for 1:2] قُلْ مَا يَعْبَؤُا۟ بِكُمْ رَبِّى لَوْلَا دُعَآؤُكُمْ ۖ فَقَدْ كَذَّبْتُمْ فَسَوْفَ يَكُونُ لِزَامًۢا
- (26:117) [listed for 1:2] قَالَ رَبِّ إِنَّ قَوْمِى كَذَّبُونِ
- (26:165) [listed for 1:2] أَتَأْتُونَ ٱلذُّكْرَانَ مِنَ ٱلْعَٰلَمِينَ
- (26:188) [listed for 1:2] قَالَ رَبِّىٓ أَعْلَمُ بِمَا تَعْمَلُونَ
- (27:26) [listed for 1:2] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ ۩
- (37:149) [listed for 1:2] فَٱسْتَفْتِهِمْ أَلِرَبِّكَ ٱلْبَنَاتُ وَلَهُمُ ٱلْبَنُونَ
- (38:79) [listed for 1:2] قَالَ رَبِّ فَأَنظِرْنِىٓ إِلَىٰ يَوْمِ يُبْعَثُونَ
- (39:69) [listed for 1:2] وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَهُمْ لَا يُظْلَمُونَ
- (50:4) [listed for 1:2] قَدْ عَلِمْنَا مَا تَنقُصُ ٱلْأَرْضُ مِنْهُمْ ۖ وَعِندَنَا كِتَٰبٌ حَفِيظٌۢ
- (51:34) [listed for 1:2] مُّسَوَّمَةً عِندَ رَبِّكَ لِلْمُسْرِفِينَ
- (51:44) [listed for 1:2] فَعَتَوْا۟ عَنْ أَمْرِ رَبِّهِمْ فَأَخَذَتْهُمُ ٱلصَّٰعِقَةُ وَهُمْ يَنظُرُونَ
- (52:37) [listed for 1:2] أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ
- (55:46) [listed for 1:2] وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- (70:3) [listed for 1:2] مِّنَ ٱللَّهِ ذِى ٱلْمَعَارِجِ
- (75:30) [listed for 1:2] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ
- (83:11) [listed for 1:2] ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ
- (85:8) [listed for 1:2] وَمَا نَقَمُوا۟ مِنْهُمْ إِلَّآ أَن يُؤْمِنُوا۟ بِٱللَّهِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (88:8) [listed for 1:2] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- (89:14) [listed for 1:2] إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- (89:28) [listed for 1:2] ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- (97:4) [listed for 1:2] تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ
- (108:2) [listed for 1:2] فَصَلِّ لِرَبِّكَ وَٱنْحَرْ
- (109:4) [listed for 1:2] وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- (109:5) [listed for 1:2] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- (112:2) [listed for 1:2] ٱللَّهُ ٱلصَّمَدُ

## neighbours: within two ayat of a passage the commentary cites (94)

- (3:62) [next to 3:64] إِنَّ هَٰذَا لَهُوَ ٱلْقَصَصُ ٱلْحَقُّ ۚ وَمَا مِنْ إِلَٰهٍ إِلَّا ٱللَّهُ ۚ وَإِنَّ ٱللَّهَ لَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (3:63) [next to 3:64] فَإِن تَوَلَّوْا۟ فَإِنَّ ٱللَّهَ عَلِيمٌۢ بِٱلْمُفْسِدِينَ
- (3:65) [next to 3:64] يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تُحَآجُّونَ فِىٓ إِبْرَٰهِيمَ وَمَآ أُنزِلَتِ ٱلتَّوْرَىٰةُ وَٱلْإِنجِيلُ إِلَّا مِنۢ بَعْدِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (3:66) [next to 3:64] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ حَٰجَجْتُمْ فِيمَا لَكُم بِهِۦ عِلْمٌۭ فَلِمَ تُحَآجُّونَ فِيمَا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ ۚ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (3:77) [next to 3:79] إِنَّ ٱلَّذِينَ يَشْتَرُونَ بِعَهْدِ ٱللَّهِ وَأَيْمَٰنِهِمْ ثَمَنًۭا قَلِيلًا أُو۟لَٰٓئِكَ لَا خَلَٰقَ لَهُمْ فِى ٱلْءَاخِرَةِ وَلَا يُكَلِّمُهُمُ ٱللَّهُ وَلَا يَنظُرُ إِلَيْهِمْ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- (3:78) [next to 3:79] وَإِنَّ مِنْهُمْ لَفَرِيقًۭا يَلْوُۥنَ أَلْسِنَتَهُم بِٱلْكِتَٰبِ لِتَحْسَبُوهُ مِنَ ٱلْكِتَٰبِ وَمَا هُوَ مِنَ ٱلْكِتَٰبِ وَيَقُولُونَ هُوَ مِنْ عِندِ ٱللَّهِ وَمَا هُوَ مِنْ عِندِ ٱللَّهِ وَيَقُولُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ وَهُمْ يَعْلَمُونَ
- (3:80) [next to 3:79] وَلَا يَأْمُرَكُمْ أَن تَتَّخِذُوا۟ ٱلْمَلَٰٓئِكَةَ وَٱلنَّبِيِّۦنَ أَرْبَابًا ۗ أَيَأْمُرُكُم بِٱلْكُفْرِ بَعْدَ إِذْ أَنتُم مُّسْلِمُونَ
- (3:81) [next to 3:79] وَإِذْ أَخَذَ ٱللَّهُ مِيثَٰقَ ٱلنَّبِيِّۦنَ لَمَآ ءَاتَيْتُكُم مِّن كِتَٰبٍۢ وَحِكْمَةٍۢ ثُمَّ جَآءَكُمْ رَسُولٌۭ مُّصَدِّقٌۭ لِّمَا مَعَكُمْ لَتُؤْمِنُنَّ بِهِۦ وَلَتَنصُرُنَّهُۥ ۚ قَالَ ءَأَقْرَرْتُمْ وَأَخَذْتُمْ عَلَىٰ ذَٰلِكُمْ إِصْرِى ۖ قَالُوٓا۟ أَقْرَرْنَا ۚ قَالَ فَٱشْهَدُوا۟ وَأَنَا۠ مَعَكُم مِّنَ ٱلشَّٰهِدِينَ
- (3:144) [next to 3:146] وَمَا مُحَمَّدٌ إِلَّا رَسُولٌۭ قَدْ خَلَتْ مِن قَبْلِهِ ٱلرُّسُلُ ۚ أَفَإِي۟ن مَّاتَ أَوْ قُتِلَ ٱنقَلَبْتُمْ عَلَىٰٓ أَعْقَٰبِكُمْ ۚ وَمَن يَنقَلِبْ عَلَىٰ عَقِبَيْهِ فَلَن يَضُرَّ ٱللَّهَ شَيْـًۭٔا ۗ وَسَيَجْزِى ٱللَّهُ ٱلشَّٰكِرِينَ
- (3:145) [next to 3:146] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
- (3:147) [next to 3:146] وَمَا كَانَ قَوْلَهُمْ إِلَّآ أَن قَالُوا۟ رَبَّنَا ٱغْفِرْ لَنَا ذُنُوبَنَا وَإِسْرَافَنَا فِىٓ أَمْرِنَا وَثَبِّتْ أَقْدَامَنَا وَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (3:148) [next to 3:146] فَـَٔاتَىٰهُمُ ٱللَّهُ ثَوَابَ ٱلدُّنْيَا وَحُسْنَ ثَوَابِ ٱلْءَاخِرَةِ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
- (3:185) [next to 3:187] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (3:186) [next to 3:187] ۞ لَتُبْلَوُنَّ فِىٓ أَمْوَٰلِكُمْ وَأَنفُسِكُمْ وَلَتَسْمَعُنَّ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ وَمِنَ ٱلَّذِينَ أَشْرَكُوٓا۟ أَذًۭى كَثِيرًۭا ۚ وَإِن تَصْبِرُوا۟ وَتَتَّقُوا۟ فَإِنَّ ذَٰلِكَ مِنْ عَزْمِ ٱلْأُمُورِ
- (3:189) [next to 3:187] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (3:190) [next to 3:188] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
- (4:21) [next to 4:23] وَكَيْفَ تَأْخُذُونَهُۥ وَقَدْ أَفْضَىٰ بَعْضُكُمْ إِلَىٰ بَعْضٍۢ وَأَخَذْنَ مِنكُم مِّيثَٰقًا غَلِيظًۭا
- (4:22) [next to 4:23] وَلَا تَنكِحُوا۟ مَا نَكَحَ ءَابَآؤُكُم مِّنَ ٱلنِّسَآءِ إِلَّا مَا قَدْ سَلَفَ ۚ إِنَّهُۥ كَانَ فَٰحِشَةًۭ وَمَقْتًۭا وَسَآءَ سَبِيلًا
- (4:24) [next to 4:23] ۞ وَٱلْمُحْصَنَٰتُ مِنَ ٱلنِّسَآءِ إِلَّا مَا مَلَكَتْ أَيْمَٰنُكُمْ ۖ كِتَٰبَ ٱللَّهِ عَلَيْكُمْ ۚ وَأُحِلَّ لَكُم مَّا وَرَآءَ ذَٰلِكُمْ أَن تَبْتَغُوا۟ بِأَمْوَٰلِكُم مُّحْصِنِينَ غَيْرَ مُسَٰفِحِينَ ۚ فَمَا ٱسْتَمْتَعْتُم بِهِۦ مِنْهُنَّ فَـَٔاتُوهُنَّ أُجُورَهُنَّ فَرِيضَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا تَرَٰضَيْتُم بِهِۦ مِنۢ بَعْدِ ٱلْفَرِيضَةِ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
- (4:25) [next to 4:23] وَمَن لَّمْ يَسْتَطِعْ مِنكُمْ طَوْلًا أَن يَنكِحَ ٱلْمُحْصَنَٰتِ ٱلْمُؤْمِنَٰتِ فَمِن مَّا مَلَكَتْ أَيْمَٰنُكُم مِّن فَتَيَٰتِكُمُ ٱلْمُؤْمِنَٰتِ ۚ وَٱللَّهُ أَعْلَمُ بِإِيمَٰنِكُم ۚ بَعْضُكُم مِّنۢ بَعْضٍۢ ۚ فَٱنكِحُوهُنَّ بِإِذْنِ أَهْلِهِنَّ وَءَاتُوهُنَّ أُجُورَهُنَّ بِٱلْمَعْرُوفِ مُحْصَنَٰتٍ غَيْرَ مُسَٰفِحَٰتٍۢ وَلَا مُتَّخِذَٰتِ أَخْدَانٍۢ ۚ فَإِذَآ أُحْصِنَّ فَإِنْ أَتَيْنَ بِفَٰحِشَةٍۢ فَعَلَيْهِنَّ نِصْفُ مَا عَلَى ٱلْمُحْصَنَٰتِ مِنَ ٱلْعَذَابِ ۚ ذَٰلِكَ لِمَنْ خَشِىَ ٱلْعَنَتَ مِنكُمْ ۚ وَأَن تَصْبِرُوا۟ خَيْرٌۭ لَّكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (6:40) [next to 6:42] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ أَوْ أَتَتْكُمُ ٱلسَّاعَةُ أَغَيْرَ ٱللَّهِ تَدْعُونَ إِن كُنتُمْ صَٰدِقِينَ
- (6:41) [next to 6:42] بَلْ إِيَّاهُ تَدْعُونَ فَيَكْشِفُ مَا تَدْعُونَ إِلَيْهِ إِن شَآءَ وَتَنسَوْنَ مَا تُشْرِكُونَ
- (6:46) [next to 6:44] قُلْ أَرَءَيْتُمْ إِنْ أَخَذَ ٱللَّهُ سَمْعَكُمْ وَأَبْصَٰرَكُمْ وَخَتَمَ عَلَىٰ قُلُوبِكُم مَّنْ إِلَٰهٌ غَيْرُ ٱللَّهِ يَأْتِيكُم بِهِ ۗ ٱنظُرْ كَيْفَ نُصَرِّفُ ٱلْءَايَٰتِ ثُمَّ هُمْ يَصْدِفُونَ
- (6:47) [next to 6:45] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ بَغْتَةً أَوْ جَهْرَةً هَلْ يُهْلَكُ إِلَّا ٱلْقَوْمُ ٱلظَّٰلِمُونَ
- (6:74) [next to 6:76] ۞ وَإِذْ قَالَ إِبْرَٰهِيمُ لِأَبِيهِ ءَازَرَ أَتَتَّخِذُ أَصْنَامًا ءَالِهَةً ۖ إِنِّىٓ أَرَىٰكَ وَقَوْمَكَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (6:75) [next to 6:76] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (6:80) [next to 6:78] وَحَآجَّهُۥ قَوْمُهُۥ ۚ قَالَ أَتُحَٰٓجُّوٓنِّى فِى ٱللَّهِ وَقَدْ هَدَىٰنِ ۚ وَلَآ أَخَافُ مَا تُشْرِكُونَ بِهِۦٓ إِلَّآ أَن يَشَآءَ رَبِّى شَيْـًۭٔا ۗ وَسِعَ رَبِّى كُلَّ شَىْءٍ عِلْمًا ۗ أَفَلَا تَتَذَكَّرُونَ
- (6:81) [next to 6:79] وَكَيْفَ أَخَافُ مَآ أَشْرَكْتُمْ وَلَا تَخَافُونَ أَنَّكُمْ أَشْرَكْتُم بِٱللَّهِ مَا لَمْ يُنَزِّلْ بِهِۦ عَلَيْكُمْ سُلْطَٰنًۭا ۚ فَأَىُّ ٱلْفَرِيقَيْنِ أَحَقُّ بِٱلْأَمْنِ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (7:170) [next to 7:172] وَٱلَّذِينَ يُمَسِّكُونَ بِٱلْكِتَٰبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ إِنَّا لَا نُضِيعُ أَجْرَ ٱلْمُصْلِحِينَ
- (7:171) [next to 7:172] ۞ وَإِذْ نَتَقْنَا ٱلْجَبَلَ فَوْقَهُمْ كَأَنَّهُۥ ظُلَّةٌۭ وَظَنُّوٓا۟ أَنَّهُۥ وَاقِعٌۢ بِهِمْ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (7:174) [next to 7:172] وَكَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ وَلَعَلَّهُمْ يَرْجِعُونَ
- (7:175) [next to 7:173] وَٱتْلُ عَلَيْهِمْ نَبَأَ ٱلَّذِىٓ ءَاتَيْنَٰهُ ءَايَٰتِنَا فَٱنسَلَخَ مِنْهَا فَأَتْبَعَهُ ٱلشَّيْطَٰنُ فَكَانَ مِنَ ٱلْغَاوِينَ
- (10:8) [next to 10:10] أُو۟لَٰٓئِكَ مَأْوَىٰهُمُ ٱلنَّارُ بِمَا كَانُوا۟ يَكْسِبُونَ
- (10:9) [next to 10:10] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ يَهْدِيهِمْ رَبُّهُم بِإِيمَٰنِهِمْ ۖ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (10:11) [next to 10:10] ۞ وَلَوْ يُعَجِّلُ ٱللَّهُ لِلنَّاسِ ٱلشَّرَّ ٱسْتِعْجَالَهُم بِٱلْخَيْرِ لَقُضِىَ إِلَيْهِمْ أَجَلُهُمْ ۖ فَنَذَرُ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (10:12) [next to 10:10] وَإِذَا مَسَّ ٱلْإِنسَٰنَ ٱلضُّرُّ دَعَانَا لِجَنۢبِهِۦٓ أَوْ قَاعِدًا أَوْ قَآئِمًۭا فَلَمَّا كَشَفْنَا عَنْهُ ضُرَّهُۥ مَرَّ كَأَن لَّمْ يَدْعُنَآ إِلَىٰ ضُرٍّۢ مَّسَّهُۥ ۚ كَذَٰلِكَ زُيِّنَ لِلْمُسْرِفِينَ مَا كَانُوا۟ يَعْمَلُونَ
- (12:39) [next to 12:41] يَٰصَىٰحِبَىِ ٱلسِّجْنِ ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
- (12:40) [next to 12:41] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (12:42) [next to 12:41] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (12:43) [next to 12:41] وَقَالَ ٱلْمَلِكُ إِنِّىٓ أَرَىٰ سَبْعَ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعَ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ ۖ يَٰٓأَيُّهَا ٱلْمَلَأُ أَفْتُونِى فِى رُءْيَٰىَ إِن كُنتُمْ لِلرُّءْيَا تَعْبُرُونَ
- (16:14) [next to 16:16] وَهُوَ ٱلَّذِى سَخَّرَ ٱلْبَحْرَ لِتَأْكُلُوا۟ مِنْهُ لَحْمًۭا طَرِيًّۭا وَتَسْتَخْرِجُوا۟ مِنْهُ حِلْيَةًۭ تَلْبَسُونَهَا وَتَرَى ٱلْفُلْكَ مَوَاخِرَ فِيهِ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- (16:15) [next to 16:16] وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَأَنْهَٰرًۭا وَسُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
- (16:17) [next to 16:16] أَفَمَن يَخْلُقُ كَمَن لَّا يَخْلُقُ ۗ أَفَلَا تَذَكَّرُونَ
- (16:18) [next to 16:16] وَإِن تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱللَّهَ لَغَفُورٌۭ رَّحِيمٌۭ
- (17:22) [next to 17:24] لَّا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ فَتَقْعُدَ مَذْمُومًۭا مَّخْذُولًۭا
- (17:23) [next to 17:24] ۞ وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًا ۚ إِمَّا يَبْلُغَنَّ عِندَكَ ٱلْكِبَرَ أَحَدُهُمَآ أَوْ كِلَاهُمَا فَلَا تَقُل لَّهُمَآ أُفٍّۢ وَلَا تَنْهَرْهُمَا وَقُل لَّهُمَا قَوْلًۭا كَرِيمًۭا
- (17:25) [next to 17:24] رَّبُّكُمْ أَعْلَمُ بِمَا فِى نُفُوسِكُمْ ۚ إِن تَكُونُوا۟ صَٰلِحِينَ فَإِنَّهُۥ كَانَ لِلْأَوَّٰبِينَ غَفُورًۭا
- (17:26) [next to 17:24] وَءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ وَلَا تُبَذِّرْ تَبْذِيرًا
- (20:47) [next to 20:49] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
- (20:48) [next to 20:49] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:55) [next to 20:53] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
- (20:56) [next to 20:54] وَلَقَدْ أَرَيْنَٰهُ ءَايَٰتِنَا كُلَّهَا فَكَذَّبَ وَأَبَىٰ
- (24:41) [next to 24:43] أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ ۖ كُلٌّۭ قَدْ عَلِمَ صَلَاتَهُۥ وَتَسْبِيحَهُۥ ۗ وَٱللَّهُ عَلِيمٌۢ بِمَا يَفْعَلُونَ
- (24:42) [next to 24:43] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (24:44) [next to 24:43] يُقَلِّبُ ٱللَّهُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّأُو۟لِى ٱلْأَبْصَٰرِ
- (24:45) [next to 24:43] وَٱللَّهُ خَلَقَ كُلَّ دَآبَّةٍۢ مِّن مَّآءٍۢ ۖ فَمِنْهُم مَّن يَمْشِى عَلَىٰ بَطْنِهِۦ وَمِنْهُم مَّن يَمْشِى عَلَىٰ رِجْلَيْنِ وَمِنْهُم مَّن يَمْشِى عَلَىٰٓ أَرْبَعٍۢ ۚ يَخْلُقُ ٱللَّهُ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (26:14) [next to 26:16] وَلَهُمْ عَلَىَّ ذَنۢبٌۭ فَأَخَافُ أَن يَقْتُلُونِ
- (26:15) [next to 26:16] قَالَ كَلَّا ۖ فَٱذْهَبَا بِـَٔايَٰتِنَآ ۖ إِنَّا مَعَكُم مُّسْتَمِعُونَ
- (26:17) [next to 26:16] أَنْ أَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ
- (26:18) [next to 26:16] قَالَ أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا وَلَبِثْتَ فِينَا مِنْ عُمُرِكَ سِنِينَ
- (26:21) [next to 26:23] فَفَرَرْتُ مِنكُمْ لَمَّا خِفْتُكُمْ فَوَهَبَ لِى رَبِّى حُكْمًۭا وَجَعَلَنِى مِنَ ٱلْمُرْسَلِينَ
- (26:22) [next to 26:23] وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ
- (26:29) [next to 26:27] قَالَ لَئِنِ ٱتَّخَذْتَ إِلَٰهًا غَيْرِى لَأَجْعَلَنَّكَ مِنَ ٱلْمَسْجُونِينَ
- (26:30) [next to 26:28] قَالَ أَوَلَوْ جِئْتُكَ بِشَىْءٍۢ مُّبِينٍۢ
- (26:68) [next to 26:70] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:69) [next to 26:70] وَٱتْلُ عَلَيْهِمْ نَبَأَ إِبْرَٰهِيمَ
- (26:71) [next to 26:70] قَالُوا۟ نَعْبُدُ أَصْنَامًۭا فَنَظَلُّ لَهَا عَٰكِفِينَ
- (26:72) [next to 26:70] قَالَ هَلْ يَسْمَعُونَكُمْ إِذْ تَدْعُونَ
- (26:74) [next to 26:76] قَالُوا۟ بَلْ وَجَدْنَآ ءَابَآءَنَا كَذَٰلِكَ يَفْعَلُونَ
- (26:75) [next to 26:76] قَالَ أَفَرَءَيْتُم مَّا كُنتُمْ تَعْبُدُونَ
- (26:81) [next to 26:79] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (26:82) [next to 26:80] وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ
- (27:90) [next to 27:92] وَمَن جَآءَ بِٱلسَّيِّئَةِ فَكُبَّتْ وُجُوهُهُمْ فِى ٱلنَّارِ هَلْ تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (27:91) [next to 27:92] إِنَّمَآ أُمِرْتُ أَنْ أَعْبُدَ رَبَّ هَٰذِهِ ٱلْبَلْدَةِ ٱلَّذِى حَرَّمَهَا وَلَهُۥ كُلُّ شَىْءٍۢ ۖ وَأُمِرْتُ أَنْ أَكُونَ مِنَ ٱلْمُسْلِمِينَ
- (28:68) [next to 28:70] وَرَبُّكَ يَخْلُقُ مَا يَشَآءُ وَيَخْتَارُ ۗ مَا كَانَ لَهُمُ ٱلْخِيَرَةُ ۚ سُبْحَٰنَ ٱللَّهِ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (28:69) [next to 28:70] وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
- (28:71) [next to 28:70] قُلْ أَرَءَيْتُمْ إِن جَعَلَ ٱللَّهُ عَلَيْكُمُ ٱلَّيْلَ سَرْمَدًا إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَنْ إِلَٰهٌ غَيْرُ ٱللَّهِ يَأْتِيكُم بِضِيَآءٍ ۖ أَفَلَا تَسْمَعُونَ
- (28:72) [next to 28:70] قُلْ أَرَءَيْتُمْ إِن جَعَلَ ٱللَّهُ عَلَيْكُمُ ٱلنَّهَارَ سَرْمَدًا إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَنْ إِلَٰهٌ غَيْرُ ٱللَّهِ يَأْتِيكُم بِلَيْلٍۢ تَسْكُنُونَ فِيهِ ۖ أَفَلَا تُبْصِرُونَ
- (37:178) [next to 37:180] وَتَوَلَّ عَنْهُمْ حَتَّىٰ حِينٍۢ
- (37:179) [next to 37:180] وَأَبْصِرْ فَسَوْفَ يُبْصِرُونَ
- (37:181) [next to 37:180] وَسَلَٰمٌ عَلَى ٱلْمُرْسَلِينَ
- (39:72) [next to 39:74] قِيلَ ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (39:73) [next to 39:74] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
- (42:30) [next to 42:32] وَمَآ أَصَٰبَكُم مِّن مُّصِيبَةٍۢ فَبِمَا كَسَبَتْ أَيْدِيكُمْ وَيَعْفُوا۟ عَن كَثِيرٍۢ
- (42:31) [next to 42:32] وَمَآ أَنتُم بِمُعْجِزِينَ فِى ٱلْأَرْضِ ۖ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (42:34) [next to 42:32] أَوْ يُوبِقْهُنَّ بِمَا كَسَبُوا۟ وَيَعْفُ عَن كَثِيرٍۢ
- (42:35) [next to 42:33] وَيَعْلَمَ ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِنَا مَا لَهُم مِّن مَّحِيصٍۢ
- (45:34) [next to 45:36] وَقِيلَ ٱلْيَوْمَ نَنسَىٰكُمْ كَمَا نَسِيتُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا وَمَأْوَىٰكُمُ ٱلنَّارُ وَمَا لَكُم مِّن نَّٰصِرِينَ
- (45:35) [next to 45:36] ذَٰلِكُم بِأَنَّكُمُ ٱتَّخَذْتُمْ ءَايَٰتِ ٱللَّهِ هُزُوًۭا وَغَرَّتْكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ لَا يُخْرَجُونَ مِنْهَا وَلَا هُمْ يُسْتَعْتَبُونَ
- (45:37) [next to 45:36] وَلَهُ ٱلْكِبْرِيَآءُ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (79:22) [next to 79:24] ثُمَّ أَدْبَرَ يَسْعَىٰ
- (79:23) [next to 79:24] فَحَشَرَ فَنَادَىٰ
- (79:25) [next to 79:24] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- (79:26) [next to 79:24] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ

