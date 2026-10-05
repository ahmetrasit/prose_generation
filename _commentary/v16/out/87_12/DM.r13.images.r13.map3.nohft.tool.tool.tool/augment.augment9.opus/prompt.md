Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:12; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_12/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_12.reading.tr.md (prose paragraphs numbered) =====
## O ki: ateşiyle tanıtılan kişi

[¶1] On ikinci ayet tek başına bir cümle değildir. Önceki ayetin son kelimesine bağlanan bir ilgi cümlesidir. Dokuzuncu ayette Peygamber'e öğüt vermesi emredilmişti. Onuncu ve on birinci ayetler bu öğüt karşısında insanların ikiye ayrıldığını anlatır, on birinci ayet de şöyle biter: {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ise ondan uzak durur, source:87:11}. Ardından gelen {ar:ٱلَّذِى, tr:elleẕî, gloss:o kişi ki, source:87:12} bu en bedbahtın kim olduğunu söyler: {ar:يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:yasle'n-nâra'l-kubrâ, gloss:en büyük ateşe girip yakıcılığını çekecek olan, source:87:12}. Ayet kişinin adını vermez, ne düşündüğünü ya da ne söylediğini de anlatmaz. Kişi iki hareketle tanımlanır: öğütten yana çekilir ve ateşe girer. Bir şeyden sakınan beden, başka bir şeyin içine yürür.

[¶2] Fiil, Arapçada hem şimdiyi hem geleceği taşıyan kiptedir. Henüz olmamış bir şeyi, kişiye şimdiden yapışmış bir nitelik gibi söyler. Türkçedeki "yanacaktır" bunun yalnızca gelecek yüzünü verir. Arapça ise o kişiyi şimdi de "ateşe giren" diye adlandırır. Ateş Arapçada dişil bir isimdir: {ar:النار مؤنثة وهي من الواو, tr:en-nâru muennesetun ve hiye mine'l-vâv, gloss:ateş dişildir ve kökünde vav vardır, source:"ن و ر,B002"}. Bu yüzden sıfatı da "daha büyük" demek olan ekber'in dişil biçimi, kubrâ'dır. İki üstünlük sıfatı karşı karşıya gelir: en bedbaht olan, en büyük ateşe girer.

[¶3] Bu ilgi zamiri surede ilk kez burada geçmez. Sure onu üç kez arka arkaya Rab için kullanmıştı: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}, {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran, source:87:4}. O üç cümlede Rab, eşyaya uzanan işleriyle tanınır. Bir şeyi yaratır, ölçer, toprağın içinden dışarı çıkarır, ve her işinden bir sonuç doğar. On ikinci ayette aynı kalıp bir insanı anlatır. Fiil dilbilgisi açısından etkendir, ama içeriği bir uğrayıştır. Bu kişinin yaptığı şey, başına gelen şeyin ta kendisidir. Rab'bin işleri bir düzen kurar. Bu kişinin işi ise kendi üstüne kapanır.

[¶4] Arapçada ateşin kelimesi bir tanınma işini de görür. Bundan sonra anılacak bütün aile imgeleri gibi bu da kelimenin bu ayetteki anlamının yerine değil, yanında duyulur. Bir devenin kime ait olduğunu sormak isteyen {ar:ما نار هذه الناقة أي ما سمتها, tr:mâ nâru hâẕihi'n-nâkati ey mâ simetuhâ, gloss:bu devenin ateşi, yani damgası nedir, source:"ن و ر,B002"} diye sorardı. Damga, kızdırılmış bir demirin deriye bastırılmasıyla açılan, iyileşince kalıcı kalan bir izdir. Sürüden kopan bir hayvan bu izden tanınır ve sahibine götürülür. Araplar hayvanın soyunun bile bu izde okunduğunu söylerlerdi: {ar:نجارها نارها, tr:nicâruhâ nâruhâ, gloss:onun soyu ateşindedir, source:"ن و ر,B002"}. On ikinci ayet de en bedbahtı adıyla değil ateşiyle anar. Onun ne olduğu, varacağı ateşte okunur. Birinci ayetteki "ad" ve on altıncı ayetteki "tercih etmek" kelimelerinin kurduğu iz ve işaret sahnesi, bu damgaya surenin o ayetleri üzerinden bağlanır.

## Ateşe girmek, ateşte ısınmak, ateşte pişmek

[¶5] Yaslâ fiili ateşe değmeyi değil, içine girip ateşin ağırlığını çekmeyi anlatır. Araplar {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi, yani onun sıcağına ve şiddetine katlandı, source:"ص ل ي,B003"} derlerdi. Fiilin içinde bir süreklilik de vardır: {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâri ey yelzemu'n-nâr, gloss:ateşe sokulan, yani ateşten ayrılmayan, source:"ص ل ي,B003"}. Kelime yalnız ateş için de kullanılmaz. Ağır bir işe ya da bir belaya uğrayan için de {ar:صلي بالنار وبكذا أي بلي بها واصطلى بها, tr:saliye bi'n-nâri ve bi-keẕâ ey buliye bihâ va'stalâ bihâ, gloss:ateşe ya da şuna uğradı, yani onunla sınandı ve onun sıcağını yedi, source:"ص ل ي,B003"} denir. Böylece fiil, bir şeyin içinde kalıp onun bütün sertliğini üstüne almayı adlandırır.

[¶6] Aynı fiil ateşin öbür yüzünü de taşır. Isınmak için yakılan yakıta {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-salâu mâ yustalâ bihî ve mâ yuẕkâ bihi'n-nâru ve yûkad, gloss:salâ, başında ısınılan ve ateşin onunla tutuşturulup yakıldığı şeydir, source:"ص ل ي,B004"} denir. Burada fiilin dönüşlü biçimi ısınmaktır: soğuk gecede ateşin kenarına oturup ellerini ona tutmak. Kur'an bu biçimi Musa'nın ağzından verir. Musa ailesiyle yol alırken bir ateş görür ve onlara {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ, tr:innî ânestu nâran se-âtîkum minhâ bi-haberin ev âtîkum bi-şihâbin kabesin leallekum tastalûn, gloss:bir ateş gördüm; ondan size ya bir haber ya da yanan bir kor getireceğim, belki ısınırsınız, source:27:7} der. Yolcunun soğuk gecede aradığı rahatlık ile en bedbahtın yanışı aynı fiil ailesinden adlandırılır. Fark mesafede ve iradededir. Isınan kişi ateşe ihtiyacı kadar yaklaşır, kenarda durur, istediğinde kalkar. On ikinci ayetteki kişi ise içeridedir ve ateşten ayrılmaz. Yakıtın adı da aynı köktendir, ve Kur'an büyük ateşin yakıtını da söyler. Allah, indirdiği sözden şüphe edenlere onun bir benzerini getirmelerini söyleyip meydan okur. Yapamazlarsa şunu söyler: {ar:فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe'ttekû'n-nâra'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}. Bu ateşte insan, başında ısınan kişi değildir. Ateşi besleyen yakıtın kendisidir.

[¶7] Fiil, ateşin mutfaktaki işini de adlandırır: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. Kızartılan et bir süre sonra pişer ve iş biter. Kur'an bu fiilin ettirgen biçimini, pişmenin bitmediği bir ateş için kullanır. Allah ayetlerini inkâr edenler için şöyle der: {ar:سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ, tr:sevfe nuslîhim nâran kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ li-yeẕûku'l-azâb, gloss:onları bir ateşe sokacağız; derileri piştikçe yerlerine başka deriler koyacağız ki azabı tatsınlar, source:4:56}. Deri piştikçe yenilenir ve tatma sona ermez. Bu, on üçüncü ayetteki halin nasıl işlediğini gösterir: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne de yaşar, source:87:13}. Pişme tamamlanıp ölüme varmaz, ama ateşten kurtulup hayata da dönülmez.

[¶8] Ateş bir zanaatkârın elinde düzeltir de. Araplar eğri değneği ateşte doğrultana {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"} derlerdi. Değnek alevin üstünde döndürülür ve ısınınca odunu yumuşar. Sıcakken bükülüp doğrultulur, soğuyunca da o doğrulukta kalır. İkinci ayetteki "düzene koydu" fiiliyle bu doğrultma işi, surenin yaratılışı bir zanaat gibi gösteren sahnesinde buluşur. Ama on ikinci ayetin ateşi bir şey doğrultmaz. Sonraki ayet ondan hiçbir sonuç çıkmadığını söyler: ne ölüm vardır ne hayat. Başka bir surede bir ateş, Sekar, şöyle anlatılır: {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ teẕer, gloss:ne bir şey bırakır ne de kendi haline koyar, source:74:28}. Aynı fiilin hem düzelten bir ateşi hem de içine düşenin yalnızca katlandığı bir ateşi adlandırması dilin bir yankısıdır, ayetin sözü değildir. Yine de bu yankı, büyük ateşin ne olmadığını duyurur: orada ateş bir alet olmaktan çıkmıştır.

## Işıkla aynı adı taşıyan ateş

[¶9] Nâr, nûr ile, yani ışıkla aynı köktendir: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-ẕâlike min tarîkati'l-idâe, gloss:nur da nâr da bu adı aydınlatmalarından alır, source:"ن و ر,B001"}. Bu kökte ışıkla birlikte bir kıpırtı da vardır: {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslun sahîhun yedullu alâ idâetin ve'dtırâbin ve kılleti ŝebât, gloss:aydınlanma, çalkantı ve kararsızlık bildiren sağlam bir kök, source:"ن و ر,B001"}. Ateşin adının bir sebebi de durmadan oynamasıdır: {ar:ولأن ذلك يكون مضطربا سريع الحركة, tr:ve li-enne ẕâlike yekûnu mudtariben serîa'l-hareke, gloss:çünkü o çalkantılı ve hızlı hareketlidir, source:"ن و ر,B002"}. Alev hiçbir an aynı biçimde kalmaz. Bunu on üçüncü ayetle birlikte okumak bir yorumdur, ama ayetin kelimeleri buna izin verir. Hiç durulmayan bir şeyin içindeki kişi de iki halden birine yerleşemez: ne ölümde karar kılar ne hayatta.

[¶10] Çöl insanı için ateş önce uzaktan görülen bir işaretti. Gece yol alan biri karanlıkta bir ateş seçer ve ona yönelirdi. Bunun için ayrı bir fiil vardı: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min baîdin tebassartuhâ, gloss:ateşi uzaktan seçtim, source:"ن و ر,B003"}, {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran kasadtu ileyhâ, gloss:bir ateşe doğru yöneldim, source:"ن و ر,B003"}. Yolcular yolunu bulsun diye yüksek yerlerde ateş de yakılırdı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:İslam'dan önceki dönemde yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu cümledeki "yol bulunsun" fiili, üçüncü ayetteki "yol gösterdi" fiilinin köküdür. Böyle bir ateşin yakıldığı yere menâr denirdi: {ar:المنار: علم الطريق, tr:el-menâr alemu't-tarîk, gloss:menâr yolun işaretidir, source:"ن و ر,B005"}. Kelime sonra ezanın okunduğu yapıya geçti: {ar:المنارة للمؤذن, tr:el-menâratu li'l-muezzin, gloss:menâre ezan okuyan içindir, source:"ن و ر,B005"}. Türkçedeki "minare" bu kelimedir, ama Türkçe kulak onda artık yalnızca caminin kulesini duyar. Arapça kelime ise içinde ateşi ve ışığı taşır: {ar:المنارة مفعلة من الإنارة, tr:el-menâratu mef'aletun mine'l-inâra, gloss:menâre, aydınlatmanın yeri anlamında bir kalıptır, source:"ن و ر,B005"}. Namaza çağrılan yer, yolcuya ateş yakılan yerin adını taşır. Surenin son ayetinde adı geçen Musa da uzakta bir ateş görüp onun başında yol bulmayı ummuş ve orada namaz ile anma emrini almıştı. On ikinci ayetin ateşi ile on beşinci ayetin namazı, surenin bu sahnesinde buluşur.

[¶11] Kur'an dünyadaki ateşe de bu işaret görevini verir. Allah insanlara sorar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Ateşi veren ağacı onların mı yoksa kendisinin mi yarattığını da sorar, sonra da şöyle der: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:nahnu cealnâhâ teẕkiraten ve metâan li'l-mukvîn, gloss:onu bir hatırlatma ve ıssız yerde kalanlar için bir geçimlik yaptık, source:56:73}. Teẕkire, dokuzuncu ayetteki "öğüt" kelimesiyle aynı köktendir. Küçük ateş her yakıldığında bir öğüttür. Büyük ateşin kendisi de öğüt diye sunulur. Sekar'ın başında on dokuz görevli bulunduğu söylendikten sonra şu eklenir: {ar:وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ, tr:ve mâ hiye illâ ẕikrâ li'l-beşer, gloss:o insanlar için bir öğütten başka bir şey değildir, source:74:31}. Ateş, içine girilen bir yer olmadan önce anlatılan bir öğüttür. On birinci ayetteki kişi öğütten uzak durmuştur. Öğüt olarak sunulan ateşten kaçan, ateşin kendisine girer.

[¶12] Aynı kökün bir kolu kaçınmayı da adlandırır. Kötülükten ürküp uzak duran iffetli kadına {ar:امرأة نوار وهي العفيفة النافرة عن الشر والقبيح, tr:imraetun nevârun ve hiye'l-afîfetu'n-nâfiratu ani'ş-şerri ve'l-kabîh, gloss:nevâr kadın, kötülükten ve çirkinlikten ürküp uzak duran iffetli kadındır, source:"ن و ر,B006"} denirdi. Fiil de bu anlamda kullanılırdı: {ar:نارت نفرت, tr:nâret nefarat, gloss:ürktü, kaçtı, source:"ن و ر,B006"}. Bu kaçınma, kaçılan şey kötü olduğunda övülür. On birinci ayetteki kişi de kaçar, ama öğütten kaçar. Kur'an bu kaçışa bir görüntü verir. Sekar'ı anlatan ayetlerin sonunda şöyle sorulur: {ar:فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ, tr:fe-mâ lehum ani't-teẕkirati mu'ridîn, gloss:onlara ne oluyor ki öğütten yüz çeviriyorlar, source:74:49}, {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:ke-ennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri, source:74:50}, {ar:فَرَّتْ مِن قَسْوَرَةٍۭ, tr:ferrat min kasvera, gloss:bir aslandan kaçan, source:74:51}. "Ürkmüş" kelimesi ayrı bir köktendir. Ama nevâr'ın anlamını vermek için kullanılan kelimenin ta kendisidir. On ikinci ayetteki "ateş" kelimesi bu ayette ateştir, başka bir şey değildir. Yine de aynı harfler, kişinin öğütten ürküp kaçmasını da adlandırabilir. Kaçışın vardığı yer, o kaçışın kökünü taşıyan bir addır.

## Küçük ateşin karşısındaki büyük ateş

[¶13] Kubrâ küçüğün karşıtıdır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullu alâ hilâfi's-sığar, gloss:küçüklüğün karşıtını bildiren sağlam bir kök, source:"ك ب ر,B001"}. Büyük ile küçük, birbirine bakarak söylenen adlardır: {ar:الكبير والصغير من الأسماء المتضايفة, tr:el-kebîru ve's-sağîru mine'l-esmâi'l-mutedâyife, gloss:büyük ve küçük, birbirine göre söylenen adlardandır, source:"ك ب ر,B001"}. "En büyük ateş" demek, bir de daha küçük bir ateş var demektir. Kur'an bu küçük ateşi göstermişti: insanın kendi yaktığı ve öğüt diye verilen ateş. Sure, öğüt ile ateş arasındaki bu ilişkiyi iki ayet arasında kurar. Dokuzuncu ayetteki öğüt ile on ikinci ayetteki ateş, aynı rimle biten iki kelime gibi karşı karşıya durur: ẕikrâ ve kubrâ.

[¶14] Kur'an küçükle büyüğü bir başka yerde de açıkça yan yana koyar. Mümin ile yoldan çıkanın bir olmadığını, yoldan çıkanların varacağı yerin ateş olduğunu ve her çıkmak istediklerinde oraya geri döndürüleceklerini söyledikten sonra Allah şöyle der: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuẕîkannehum mine'l-aẕâbi'l-ednâ dûne'l-aẕâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce daha yakın azaptan tattıracağız, source:32:21}. Ednâ, on altıncı ayetteki dünyâ ile aynı köktendir. Ekber de on ikinci ayetteki kubrâ'nın eril biçimidir. Yakın olan küçük acı bir dönüş fırsatı olarak verilir, büyük olan ise sonra gelir. Surenin kendi kelimeleri de aynı ikiliği kurar. On altıncı ayet {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır, siz bu yakın hayatı öne alıyorsunuz, source:87:16} der. Yakın hayat ile büyük ateş, aynı kalıptaki iki dişil sıfatla karşılıklı adlandırılır.

[¶15] Başka bir surede bu ikili aynı sırayla ve neredeyse aynı kelimelerle geçer. O surede Allah göğü ve yeri nasıl kurduğunu anlatır ve yer için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} der. Bu, dördüncü ayetteki otlaktır. Sonra o gün gelir: {ar:فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ, tr:fe-iẕâ câeti't-tâmmetu'l-kubrâ, gloss:her şeyi bastıran en büyük felaket geldiğinde, source:79:34}, {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:o gün insan neyin peşinde koştuğunu hatırlar, source:79:35}. Ardından hüküm gelir: {ar:وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:ve âŝera'l-hayâte'd-dunyâ, gloss:ve yakın hayatı öne alan, source:79:38}, {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:onun sığınağı alevli ateştir, source:79:39}. Otlak, en büyük olan, hatırlama ve yakın hayatı öne alma burada da bir aradadır. Bir fark vardır: o surede insan, en büyük olan geldiğinde hatırlar. Onuncu ayette ise {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10} denir. Öğüt şimdi alınabilir. Büyük olanın gelişinde alınan öğüt geç kalmıştır.

[¶16] Aynı kök yaşlılığı da adlandırır: {ar:الكبر في السن وقد كبر الرجل أي أسن, tr:el-kiberu fi's-sinni ve kad kebira'r-raculu ey esenne, gloss:kiber yaşta büyüklüktür; adam yaşlandı, source:"ك ب ر,B004"}. Uzun süre kullanılmış bir kılıcın ağzını bürüyen pas da bu kökle anılır: {ar:للسيف والنصل العتيق الذي قدم علته كبرة, tr:li's-seyfi ve'n-nasli'l-atîki'lleẕî kadume alethu kebra, gloss:eskimiş kılıca ve temrene, yaşlılık onu bürüdü denir, source:"ك ب ر,B004"}. Surenin ikinci ayetten beşinci ayete uzanan ve otlağın kara bir döküntüye dönmesiyle biten sahnesinde bu anlam, bir ömrün son evresine işaret eder. Ama on ikinci ayette kelime yaşı söylemez, ölçüyü söyler. Ömrün yaşlanarak vardığı son, bu büyük ateşin karşısında küçük kalır.

## Büyüklüğü kime vermek

[¶17] Kubrâ'nın kökü insanın Allah'ı yüceltirken söylediği sözü de verir: {ar:التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر, tr:et-tekbîru yukâlu li-ta'zîmillâhi teâlâ bi-kavlihimullâhu ekber, gloss:tekbir, "Allah en büyüktür" diyerek Allah'ı yüceltmektir, source:"ك ب ر,B009"}. Namaz bu sözle başlar, ezan da bu sözle açılır. Sure de yücelikle açılmıştı: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını her kusurdan arı tut, source:87:1}. Birinci ayetteki yükseklik ile on altıncı ayetteki yakın ve alçak hayat arasında kurulan eksen, surenin o iki ayeti üzerinden bu ayete uzanır. Aynı kök, insanın kendine yakıştırdığı büyüklüğü de adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametu ve keẕâlike'l-kibriyâ, gloss:kibir büyüklüktür, kibriyâ da öyle, source:"ك ب ر,B006"}. Büyüklenenler için de {ar:يتكبرون أي يرون أنهم أفضل الخلق, tr:yetekebberûne ey yerevne ennehum efdalu'l-halk, gloss:büyüklenirler, yani kendilerini yaratılmışların en üstünü görürler, source:"ك ب ر,B006"} denir. Türkçedeki "kibir" kelimesi bu kökün yalnızca bu son kolunu, kendini beğenmişliği saklar. Arapça kelime ise önce düz büyüklüktür. Sonra yaşlılık, bir işin ana yükü ve Allah'a verilen yücelik olur. Kibir, bu büyüklüğün yanlış yere konmasıdır.

[¶18] Kökün bir kolu da ağırlıktır: bir şeyin kişinin üstüne büyük gelmesi. Araplar {ar:كبر الأمر يكبر كبارة, tr:kebura'l-emru yekburu kebâra, gloss:iş ağırlaştı, büyük geldi, source:"ك ب ر,B010"} derlerdi. Bu kelime {ar:تستعمل الكبيرة فيما يشق ويصعب, tr:testa'milu'l-kebîratu fîmâ yeşukku ve yas'ub, gloss:kebîre, zor ve güç gelen şey için kullanılır, source:"ك ب ر,B010"}. Kur'an bu ağırlığı tam da öğüt ve namaz için kullanır. Allah, Nuh'a, İbrahim'e, Musa'ya ve İsa'ya buyurduğu dini Peygamber'e de buyurduğunu söyler: dini ayakta tutun ve onda ayrılığa düşmeyin. Sonra şunu ekler: {ar:كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ, tr:kebura ale'l-muşrikîne mâ ted'ûhum ileyh, gloss:onları çağırdığın şey Allah'a ortak koşanlara ağır geldi, source:42:13}. Bu ayette adı geçen İbrahim ve Musa, surenin son ayetinde sayfaları anılan iki peygamberdir. İsrailoğullarına seslenilen bir bölümde de {ar:وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ, tr:vesteînû bi's-sabri ve's-salâti ve innehâ le-kebîratun illâ ale'l-hâşiîn, gloss:sabır ve namazla yardım dileyin; namaz, gönülden boyun eğenler dışında herkese gerçekten ağır gelir, source:2:45} denir. Ardından bu boyun eğenlerin, Rablerine kavuşacaklarını düşünenler olduğu söylenir. Namazı büyük, yani ağır bulan kişi ile büyük ateşe giren kişi arasında kök birliği vardır. Bu ikisini birleştirmek bir yorumdur. Ama Kur'an'ın kendisi de aynı yolu gösterir: {ar:إِنَّ ٱلَّذِينَ يَسْتَكْبِرُونَ عَنْ عِبَادَتِى سَيَدْخُلُونَ جَهَنَّمَ دَاخِرِينَ, tr:inne'lleẕîne yestekbirûne an ibâdetî se-yedhulûne cehenneme dâhirîn, gloss:bana kulluk etmeye tenezzül etmeyip büyüklenenler aşağılanmış olarak cehenneme gireceklerdir, source:40:60}. Allah bu sözü {ar:ٱدْعُونِىٓ أَسْتَجِبْ لَكُمْ, tr:ud'ûnî estecib lekum, gloss:bana dua edin, size karşılık vereyim, source:40:60} çağrısının hemen ardından söyler.

[¶19] Kur'an'da on ikinci ayetin iki kelimesini, fiili ve büyüklüğü, tek bir insanın hikâyesinde birleştiren bir bölüm vardır. Orada Allah, bürünüp sarınmış olan Peygamber'e kalkıp uyarmasını emreder ve şunu ekler: {ar:وَرَبَّكَ فَكَبِّرْ, tr:ve rabbeke fe-kebbir, gloss:ve Rabbini büyük tut, source:74:3}. Birkaç ayet sonra bir adam anlatılır. Allah onu tek başına yaratmış, ona uzanıp giden bir mal ve yanında hazır duran oğullar vermiştir. Adam yine de daha fazlasını ister ve ayetlere karşı inat eder. Sonra şöyle denir: {ar:إِنَّهُۥ فَكَّرَ وَقَدَّرَ, tr:innehû fekkera ve kaddar, gloss:o düşündü ve ölçüp biçti, source:74:18}. Bu fiil, üçüncü ayette Rab'bin yaptığı işin fiilidir. Rab ölçer ve yol gösterir. Bu adam ise ölçer ve sözü çürütmenin yolunu arar. Ardından şu gelir: {ar:ثُمَّ أَدْبَرَ وَٱسْتَكْبَرَ, tr:ŝumme edbera vestekber, gloss:sonra sırt çevirdi ve büyüklendi, source:74:23}. Adam vahiy için {ar:إِنْ هَٰذَآ إِلَّا سِحْرٌۭ يُؤْثَرُ, tr:in hâẕâ illâ sihrun yu'ŝer, gloss:bu, dilden dile aktarılan bir büyüden başka bir şey değil, source:74:24} der, ve hüküm verilir: {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26}. Bu, on ikinci ayetteki fiilin "sokmak" anlamındaki ettirgen biçimidir. O ateş için de şöyle denir: {ar:إِنَّهَا لَإِحْدَى ٱلْكُبَرِ, tr:innehâ le-ihde'l-kuber, gloss:o, büyüklerden biridir, source:74:35}. Kuber, kubrâ'nın çoğuludur. Rabbini büyük tutması emredilen bir peygamberin karşısında kendini büyük tutan bir adam vardır, ve onun varacağı yer "büyüklerden biri" diye anılır. On ikinci ayet bu hikâyeyi anlatmaz, adamın yaptıklarını da saymaz. Ama aynı fiil ve aynı büyüklük sıfatı orada ne anlama geldiklerini açıkça gösterir.

## Yaslâ ile sallâ: iki kişiyi ayıran ses

[¶20] On beşinci ayet öbür kişiyi anlatır: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:ve Rabbinin adını anıp namaz kıldı, source:87:15}. Kulak, yaslâ ile sallâ arasındaki yakınlığı hemen duyar. İkisi de aynı iki ünsüzle kurulur ve ikisi de surenin uzun â rimiyle biter. Ama bunlar ayrı iki köktür. Ateş fiili ص ل ي köküne yazılır, namaz ise ص ل و köküne. Aralarındaki yakınlık bir ses akrabalığıdır, kök birliği değildir. Bu harflerin anlamları konuşulurken iki ayrı asıl ayırt edilir ve ateşli olan için {ar:أحدهما النار وما أشبهها من الحمى, tr:ehaduhumâ en-nâru ve mâ eşbehehâ mine'l-humma, gloss:ikisinden biri ateş ve ateşe benzeyen sıcaklıktır, source:"ص ل ي,B003"} denir. Öbürü, belli hareketleri olan ibadettir: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtu'lletî câe bihe'ş-şer'u mine'r-rukûi ve's-sucûd, gloss:dinin getirdiği, eğilme ve yere kapanmadan oluşan namaz, source:"ص ل ي,B001"}. Sure bu iki sesi iki ayrı kişiye verir. Birinin adı yoktur, yalnızca ateşi vardır. Öbürü Rabbinin adını anar. Birinci ayette emredilen ad anma, on beşinci ayetteki kişi tarafından yerine getirilmiştir.

[¶21] Kur'an bu iki sesi başka yerlerde de karşı karşıya getirir. Az önce anılan Sekar bölümünde, bahçelerdeki sağın ehli suçlulara sorar: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekekum fî sekar, gloss:sizi Sekar'a ne soktu, source:74:42}. Verdikleri ilk cevap şudur: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:namaz kılanlardan değildik dediler, source:74:43}. Aynı bölümde ateşe sokmanın fiili ile namazın adı, soru ve cevap olarak birbirine bağlanır. Bir başka surede yakıcı bir ateş anılır, {ar:كَلَّآ ۖ إِنَّهَا لَظَىٰ, tr:kellâ innehâ lezâ, gloss:hayır, o alevli bir ateştir, source:70:15}, ve birkaç ayet sonra insanın sabırsız ve tez canlı yaratıldığı söylenir. Bundan ayrılanlar da şöyle anılır: {ar:إِلَّا ٱلْمُصَلِّينَ, tr:ille'l-musallîn, gloss:namaz kılanlar müstesna, source:70:22}. Ateşin ardından namaz kılanlar gelir.

[¶22] En yakın eş ise başka bir suredir. Orada Allah veren ve sakınan ile cimrilik edip kendini yeterli gören arasındaki ayrımı anlattıktan sonra şöyle der: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enẕertukum nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}, {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:elleẕî keẕẕebe ve tevellâ, gloss:o ki yalanladı ve sırt çevirdi, source:92:16}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en sakınan ise ondan uzak tutulacak, source:92:17}. Kelimeler neredeyse aynıdır: en bedbaht, "o ki" diye başlayan tanım, ateşe giriş ve uzak tutmanın fiili. Ama uzak tutma fiili bu iki surede farklı yönlere işler. Orada ateş, en sakınandan uzak tutulur. Burada ise en bedbaht kendini öğütten uzak tutar. İki sure birlikte okunduğunda ortaya bir denge çıkar. Öğütten yana çekilen ateşten yana çekilmiş olmaz. Öğütten kaçan, ateşe girer. Öğüde yönelip Rabbinin adını anan ve namaz kılan ise ateşten uzak tutulur.

===== _commentary/v16/out/87_12/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: imperfect yaṣlā spans present and future
- memory: kubrā is the feminine of akbar (fuʿlā pattern)
- memory: adnā (32:21) and dunyā share root د ن و
- memory: kuber (74:35) is the plural of kubrā
- memory: Turkish "minare" derives from manāra
- memory: Turkish "kibir" keeps only the arrogance sense
- memory: qaswara glossed as lion; muqwīn as people in empty land
- memory: the prayer word belongs to ص ل و, as distinct from the fire verb
- memory: the -t- reflexive form iṣṭalā means warming oneself at a fire
- not written: snare sense (maṣālī) - nothing in the ayah's scene calls for a trap
- not written: tree blossom (nawr) beside the pasture of 87:4-5 - too thin to build a theme on
- not written: enmity (nāʾira), tattoo soot, depilatory nūra - no work in this ayah
- not written: ك ب ر drum, forenoon, eldest/last child, rivalry, main share of a matter - none touches the ayah
- not written: ص ل ي rump, second horse in a race (muṣallī), pounding stone, fodder plant, synagogues - no ground here
- not written: grave sin (kabīra) - folded into the "weighing heavily" sense, not developed separately
- not written: 84:12 and 88:4 (yaṣlā/taṣlā with a fire) - add nothing that 92:15 and 74:26 do not already give

===== passages not cited (253) =====
## strong (this ayah's own list) (42)

- (2:167) [listed for 87:12] وَقَالَ ٱلَّذِينَ ٱتَّبَعُوا۟ لَوْ أَنَّ لَنَا كَرَّةًۭ فَنَتَبَرَّأَ مِنْهُمْ كَمَا تَبَرَّءُوا۟ مِنَّا ۗ كَذَٰلِكَ يُرِيهِمُ ٱللَّهُ أَعْمَٰلَهُمْ حَسَرَٰتٍ عَلَيْهِمْ ۖ وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ
- (3:192) [listed for 87:12] رَبَّنَآ إِنَّكَ مَن تُدْخِلِ ٱلنَّارَ فَقَدْ أَخْزَيْتَهُۥ ۖ وَمَا لِلظَّٰلِمِينَ مِنْ أَنصَارٍۢ
- (4:10) [listed for 87:12] إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا
- (4:56) [listed for 87:12] [cited in ¶7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
- (4:115) [listed for 87:12] وَمَن يُشَاقِقِ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُ ٱلْهُدَىٰ وَيَتَّبِعْ غَيْرَ سَبِيلِ ٱلْمُؤْمِنِينَ نُوَلِّهِۦ مَا تَوَلَّىٰ وَنُصْلِهِۦ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًا
- (5:37) [listed for 87:12] يُرِيدُونَ أَن يَخْرُجُوا۟ مِنَ ٱلنَّارِ وَمَا هُم بِخَٰرِجِينَ مِنْهَا ۖ وَلَهُمْ عَذَابٌۭ مُّقِيمٌۭ
- (7:36) [listed for 87:12] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا وَٱسْتَكْبَرُوا۟ عَنْهَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (7:38) [listed for 87:12] قَالَ ٱدْخُلُوا۟ فِىٓ أُمَمٍۢ قَدْ خَلَتْ مِن قَبْلِكُم مِّنَ ٱلْجِنِّ وَٱلْإِنسِ فِى ٱلنَّارِ ۖ كُلَّمَا دَخَلَتْ أُمَّةٌۭ لَّعَنَتْ أُخْتَهَا ۖ حَتَّىٰٓ إِذَا ٱدَّارَكُوا۟ فِيهَا جَمِيعًۭا قَالَتْ أُخْرَىٰهُمْ لِأُولَىٰهُمْ رَبَّنَا هَٰٓؤُلَآءِ أَضَلُّونَا فَـَٔاتِهِمْ عَذَابًۭا ضِعْفًۭا مِّنَ ٱلنَّارِ ۖ قَالَ لِكُلٍّۢ ضِعْفٌۭ وَلَٰكِن لَّا تَعْلَمُونَ
- (14:29) [listed for 87:12] جَهَنَّمَ يَصْلَوْنَهَا ۖ وَبِئْسَ ٱلْقَرَارُ
- (15:43) [listed for 87:12] وَإِنَّ جَهَنَّمَ لَمَوْعِدُهُمْ أَجْمَعِينَ
- (16:29) [listed for 87:12] فَٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَلَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (18:29) [listed for 87:12] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
- (19:68) [listed for 87:12] فَوَرَبِّكَ لَنَحْشُرَنَّهُمْ وَٱلشَّيَٰطِينَ ثُمَّ لَنُحْضِرَنَّهُمْ حَوْلَ جَهَنَّمَ جِثِيًّۭا
- (19:70) [listed for 87:12] ثُمَّ لَنَحْنُ أَعْلَمُ بِٱلَّذِينَ هُمْ أَوْلَىٰ بِهَا صِلِيًّۭا
- (19:71) [listed for 87:12] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (20:74) [listed for 87:12] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (22:19) [listed for 87:12] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
- (22:22) [listed for 87:12] كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (25:11) [listed for 87:12] بَلْ كَذَّبُوا۟ بِٱلسَّاعَةِ ۖ وَأَعْتَدْنَا لِمَن كَذَّبَ بِٱلسَّاعَةِ سَعِيرًا
- (32:20) [listed for 87:12] وَأَمَّا ٱلَّذِينَ فَسَقُوا۟ فَمَأْوَىٰهُمُ ٱلنَّارُ ۖ كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَآ أُعِيدُوا۟ فِيهَا وَقِيلَ لَهُمْ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (35:36) [listed for 87:12] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (36:64) [listed for 87:12] ٱصْلَوْهَا ٱلْيَوْمَ بِمَا كُنتُمْ تَكْفُرُونَ
- (37:163) [listed for 87:12] إِلَّا مَنْ هُوَ صَالِ ٱلْجَحِيمِ
- (38:56) [listed for 87:12] جَهَنَّمَ يَصْلَوْنَهَا فَبِئْسَ ٱلْمِهَادُ
- (40:46) [listed for 87:12] ٱلنَّارُ يُعْرَضُونَ عَلَيْهَا غُدُوًّۭا وَعَشِيًّۭا ۖ وَيَوْمَ تَقُومُ ٱلسَّاعَةُ أَدْخِلُوٓا۟ ءَالَ فِرْعَوْنَ أَشَدَّ ٱلْعَذَابِ
- (46:20) [listed for 87:12] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَذْهَبْتُمْ طَيِّبَٰتِكُمْ فِى حَيَاتِكُمُ ٱلدُّنْيَا وَٱسْتَمْتَعْتُم بِهَا فَٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَسْتَكْبِرُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَبِمَا كُنتُمْ تَفْسُقُونَ
- (56:94) [listed for 87:12] وَتَصْلِيَةُ جَحِيمٍ
- (69:31) [listed for 87:12] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
- (69:32) [listed for 87:12] ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ
- (74:26) [listed for 87:12] [cited in ¶19] سَأُصْلِيهِ سَقَرَ
- (74:28) [listed for 87:12] [cited in ¶8] لَا تُبْقِى وَلَا تَذَرُ
- (74:43) [listed for 87:12] [cited in ¶21] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
- (78:21) [listed for 87:12] إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا
- (79:34) [listed for 87:12] [cited in ¶15] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (82:16) [listed for 87:12] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
- (83:16) [listed for 87:12] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
- (88:4) [listed for 87:12] تَصْلَىٰ نَارًا حَامِيَةًۭ
- (92:14) [listed for 87:12] [cited in ¶22] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (92:15) [listed for 87:12] [cited in ¶22] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (101:11) [listed for 87:12] نَارٌ حَامِيَةٌۢ
- (102:6) [listed for 87:12] لَتَرَوُنَّ ٱلْجَحِيمَ
- (111:3) [listed for 87:12] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

## medium (this ayah's own list) (90)

- (2:24) [listed for 87:12] [cited in ¶6] فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ ۖ أُعِدَّتْ لِلْكَٰفِرِينَ
- (2:39) [listed for 87:12] وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:81) [listed for 87:12] بَلَىٰ مَن كَسَبَ سَيِّئَةًۭ وَأَحَٰطَتْ بِهِۦ خَطِيٓـَٔتُهُۥ فَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:257) [listed for 87:12] ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۖ وَٱلَّذِينَ كَفَرُوٓا۟ أَوْلِيَآؤُهُمُ ٱلطَّٰغُوتُ يُخْرِجُونَهُم مِّنَ ٱلنُّورِ إِلَى ٱلظُّلُمَٰتِ ۗ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:275) [listed for 87:12] ٱلَّذِينَ يَأْكُلُونَ ٱلرِّبَوٰا۟ لَا يَقُومُونَ إِلَّا كَمَا يَقُومُ ٱلَّذِى يَتَخَبَّطُهُ ٱلشَّيْطَٰنُ مِنَ ٱلْمَسِّ ۚ ذَٰلِكَ بِأَنَّهُمْ قَالُوٓا۟ إِنَّمَا ٱلْبَيْعُ مِثْلُ ٱلرِّبَوٰا۟ ۗ وَأَحَلَّ ٱللَّهُ ٱلْبَيْعَ وَحَرَّمَ ٱلرِّبَوٰا۟ ۚ فَمَن جَآءَهُۥ مَوْعِظَةٌۭ مِّن رَّبِّهِۦ فَٱنتَهَىٰ فَلَهُۥ مَا سَلَفَ وَأَمْرُهُۥٓ إِلَى ٱللَّهِ ۖ وَمَنْ عَادَ فَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (3:131) [listed for 87:12] وَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِىٓ أُعِدَّتْ لِلْكَٰفِرِينَ
- (5:29) [listed for 87:12] إِنِّىٓ أُرِيدُ أَن تَبُوٓأَ بِإِثْمِى وَإِثْمِكَ فَتَكُونَ مِنْ أَصْحَٰبِ ٱلنَّارِ ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- (6:128) [listed for 87:12] وَيَوْمَ يَحْشُرُهُمْ جَمِيعًۭا يَٰمَعْشَرَ ٱلْجِنِّ قَدِ ٱسْتَكْثَرْتُم مِّنَ ٱلْإِنسِ ۖ وَقَالَ أَوْلِيَآؤُهُم مِّنَ ٱلْإِنسِ رَبَّنَا ٱسْتَمْتَعَ بَعْضُنَا بِبَعْضٍۢ وَبَلَغْنَآ أَجَلَنَا ٱلَّذِىٓ أَجَّلْتَ لَنَا ۚ قَالَ ٱلنَّارُ مَثْوَىٰكُمْ خَٰلِدِينَ فِيهَآ إِلَّا مَا شَآءَ ٱللَّهُ ۗ إِنَّ رَبَّكَ حَكِيمٌ عَلِيمٌۭ
- (7:41) [listed for 87:12] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (7:76) [listed for 87:12] قَالَ ٱلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا بِٱلَّذِىٓ ءَامَنتُم بِهِۦ كَٰفِرُونَ
- (9:35) [listed for 87:12] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
- (11:106) [listed for 87:12] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (13:18) [listed for 87:12] لِلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمُ ٱلْحُسْنَىٰ ۚ وَٱلَّذِينَ لَمْ يَسْتَجِيبُوا۟ لَهُۥ لَوْ أَنَّ لَهُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لَٱفْتَدَوْا۟ بِهِۦٓ ۚ أُو۟لَٰٓئِكَ لَهُمْ سُوٓءُ ٱلْحِسَابِ وَمَأْوَىٰهُمْ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمِهَادُ
- (14:16) [listed for 87:12] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (14:50) [listed for 87:12] سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ
- (15:44) [listed for 87:12] لَهَا سَبْعَةُ أَبْوَٰبٍۢ لِّكُلِّ بَابٍۢ مِّنْهُمْ جُزْءٌۭ مَّقْسُومٌ
- (17:18) [listed for 87:12] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
- (19:72) [listed for 87:12] ثُمَّ نُنَجِّى ٱلَّذِينَ ٱتَّقَوا۟ وَّنَذَرُ ٱلظَّٰلِمِينَ فِيهَا جِثِيًّۭا
- (20:23) [listed for 87:12] لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى
- (21:98) [listed for 87:12] إِنَّكُمْ وَمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ حَصَبُ جَهَنَّمَ أَنتُمْ لَهَا وَٰرِدُونَ
- (23:104) [listed for 87:12] تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ
- (25:12) [listed for 87:12] إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا
- (25:15) [listed for 87:12] قُلْ أَذَٰلِكَ خَيْرٌ أَمْ جَنَّةُ ٱلْخُلْدِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۚ كَانَتْ لَهُمْ جَزَآءًۭ وَمَصِيرًۭا
- (25:21) [listed for 87:12] ۞ وَقَالَ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا لَوْلَآ أُنزِلَ عَلَيْنَا ٱلْمَلَٰٓئِكَةُ أَوْ نَرَىٰ رَبَّنَا ۗ لَقَدِ ٱسْتَكْبَرُوا۟ فِىٓ أَنفُسِهِمْ وَعَتَوْ عُتُوًّۭا كَبِيرًۭا
- (28:39) [listed for 87:12] وَٱسْتَكْبَرَ هُوَ وَجُنُودُهُۥ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَظَنُّوٓا۟ أَنَّهُمْ إِلَيْنَا لَا يُرْجَعُونَ
- (28:41) [listed for 87:12] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَدْعُونَ إِلَى ٱلنَّارِ ۖ وَيَوْمَ ٱلْقِيَٰمَةِ لَا يُنصَرُونَ
- (29:39) [listed for 87:12] وَقَٰرُونَ وَفِرْعَوْنَ وَهَٰمَٰنَ ۖ وَلَقَدْ جَآءَهُم مُّوسَىٰ بِٱلْبَيِّنَٰتِ فَٱسْتَكْبَرُوا۟ فِى ٱلْأَرْضِ وَمَا كَانُوا۟ سَٰبِقِينَ
- (29:54) [listed for 87:12] يَسْتَعْجِلُونَكَ بِٱلْعَذَابِ وَإِنَّ جَهَنَّمَ لَمُحِيطَةٌۢ بِٱلْكَٰفِرِينَ
- (31:7) [listed for 87:12] وَإِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا وَلَّىٰ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًۭا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍ
- (31:21) [listed for 87:12] وَإِذَا قِيلَ لَهُمُ ٱتَّبِعُوا۟ مَآ أَنزَلَ ٱللَّهُ قَالُوا۟ بَلْ نَتَّبِعُ مَا وَجَدْنَا عَلَيْهِ ءَابَآءَنَآ ۚ أَوَلَوْ كَانَ ٱلشَّيْطَٰنُ يَدْعُوهُمْ إِلَىٰ عَذَابِ ٱلسَّعِيرِ
- (33:64) [listed for 87:12] إِنَّ ٱللَّهَ لَعَنَ ٱلْكَٰفِرِينَ وَأَعَدَّ لَهُمْ سَعِيرًا
- (36:63) [listed for 87:12] هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى كُنتُمْ تُوعَدُونَ
- (37:23) [listed for 87:12] مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ
- (37:35) [listed for 87:12] إِنَّهُمْ كَانُوٓا۟ إِذَا قِيلَ لَهُمْ لَآ إِلَٰهَ إِلَّا ٱللَّهُ يَسْتَكْبِرُونَ
- (38:59) [listed for 87:12] هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ ۖ لَا مَرْحَبًۢا بِهِمْ ۚ إِنَّهُمْ صَالُوا۟ ٱلنَّارِ
- (39:8) [listed for 87:12] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (39:16) [listed for 87:12] لَهُم مِّن فَوْقِهِمْ ظُلَلٌۭ مِّنَ ٱلنَّارِ وَمِن تَحْتِهِمْ ظُلَلٌۭ ۚ ذَٰلِكَ يُخَوِّفُ ٱللَّهُ بِهِۦ عِبَادَهُۥ ۚ يَٰعِبَادِ فَٱتَّقُونِ
- (39:71) [listed for 87:12] وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا فُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَتْلُونَ عَلَيْكُمْ ءَايَٰتِ رَبِّكُمْ وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ بَلَىٰ وَلَٰكِنْ حَقَّتْ كَلِمَةُ ٱلْعَذَابِ عَلَى ٱلْكَٰفِرِينَ
- (40:6) [listed for 87:12] وَكَذَٰلِكَ حَقَّتْ كَلِمَتُ رَبِّكَ عَلَى ٱلَّذِينَ كَفَرُوٓا۟ أَنَّهُمْ أَصْحَٰبُ ٱلنَّارِ
- (40:41) [listed for 87:12] ۞ وَيَٰقَوْمِ مَا لِىٓ أَدْعُوكُمْ إِلَى ٱلنَّجَوٰةِ وَتَدْعُونَنِىٓ إِلَى ٱلنَّارِ
- (40:47) [listed for 87:12] وَإِذْ يَتَحَآجُّونَ فِى ٱلنَّارِ فَيَقُولُ ٱلضُّعَفَٰٓؤُا۟ لِلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُنَّا لَكُمْ تَبَعًۭا فَهَلْ أَنتُم مُّغْنُونَ عَنَّا نَصِيبًۭا مِّنَ ٱلنَّارِ
- (41:28) [listed for 87:12] ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (42:7) [listed for 87:12] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ قُرْءَانًا عَرَبِيًّۭا لِّتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا وَتُنذِرَ يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ ۚ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ
- (43:74) [listed for 87:12] إِنَّ ٱلْمُجْرِمِينَ فِى عَذَابِ جَهَنَّمَ خَٰلِدُونَ
- (44:16) [listed for 87:12] يَوْمَ نَبْطِشُ ٱلْبَطْشَةَ ٱلْكُبْرَىٰٓ إِنَّا مُنتَقِمُونَ
- (45:10) [listed for 87:12] مِّن وَرَآئِهِمْ جَهَنَّمُ ۖ وَلَا يُغْنِى عَنْهُم مَّا كَسَبُوا۟ شَيْـًۭٔا وَلَا مَا ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ أَوْلِيَآءَ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌ
- (45:34) [listed for 87:12] وَقِيلَ ٱلْيَوْمَ نَنسَىٰكُمْ كَمَا نَسِيتُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا وَمَأْوَىٰكُمُ ٱلنَّارُ وَمَا لَكُم مِّن نَّٰصِرِينَ
- (48:13) [listed for 87:12] وَمَن لَّمْ يُؤْمِنۢ بِٱللَّهِ وَرَسُولِهِۦ فَإِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَعِيرًۭا
- (50:24) [listed for 87:12] أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍۢ
- (51:13) [listed for 87:12] يَوْمَ هُمْ عَلَى ٱلنَّارِ يُفْتَنُونَ
- (52:13) [listed for 87:12] يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا
- (52:14) [listed for 87:12] هَٰذِهِ ٱلنَّارُ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ
- (52:16) [listed for 87:12] ٱصْلَوْهَا فَٱصْبِرُوٓا۟ أَوْ لَا تَصْبِرُوا۟ سَوَآءٌ عَلَيْكُمْ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
- (54:48) [listed for 87:12] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (57:15) [listed for 87:12] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (58:17) [listed for 87:12] لَّن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (59:17) [listed for 87:12] فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- (64:10) [listed for 87:12] وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ خَٰلِدِينَ فِيهَا ۖ وَبِئْسَ ٱلْمَصِيرُ
- (66:6) [listed for 87:12] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌۭ شِدَادٌۭ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ
- (66:10) [listed for 87:12] ضَرَبَ ٱللَّهُ مَثَلًۭا لِّلَّذِينَ كَفَرُوا۟ ٱمْرَأَتَ نُوحٍۢ وَٱمْرَأَتَ لُوطٍۢ ۖ كَانَتَا تَحْتَ عَبْدَيْنِ مِنْ عِبَادِنَا صَٰلِحَيْنِ فَخَانَتَاهُمَا فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ
- (67:6) [listed for 87:12] وَلِلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ عَذَابُ جَهَنَّمَ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (67:7) [listed for 87:12] إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ
- (67:8) [listed for 87:12] تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ ۖ كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ
- (67:10) [listed for 87:12] وَقَالُوا۟ لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ مَا كُنَّا فِىٓ أَصْحَٰبِ ٱلسَّعِيرِ
- (67:11) [listed for 87:12] فَٱعْتَرَفُوا۟ بِذَنۢبِهِمْ فَسُحْقًۭا لِّأَصْحَٰبِ ٱلسَّعِيرِ
- (69:30) [listed for 87:12] خُذُوهُ فَغُلُّوهُ
- (70:15) [listed for 87:12] [cited in ¶21] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (71:22) [listed for 87:12] وَمَكَرُوا۟ مَكْرًۭا كُبَّارًۭا
- (72:15) [listed for 87:12] وَأَمَّا ٱلْقَٰسِطُونَ فَكَانُوا۟ لِجَهَنَّمَ حَطَبًۭا
- (74:3) [listed for 87:12] [cited in ¶19] وَرَبَّكَ فَكَبِّرْ
- (74:27) [listed for 87:12] وَمَآ أَدْرَىٰكَ مَا سَقَرُ
- (74:29) [listed for 87:12] لَوَّاحَةٌۭ لِّلْبَشَرِ
- (74:35) [listed for 87:12] [cited in ¶19] إِنَّهَا لَإِحْدَى ٱلْكُبَرِ
- (74:42) [listed for 87:12] [cited in ¶21] مَا سَلَكَكُمْ فِى سَقَرَ
- (76:4) [listed for 87:12] إِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا
- (78:23) [listed for 87:12] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (79:20) [listed for 87:12] فَأَرَىٰهُ ٱلْءَايَةَ ٱلْكُبْرَىٰ
- (79:36) [listed for 87:12] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- (81:12) [listed for 87:12] وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ
- (82:14) [listed for 87:12] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (84:12) [listed for 87:12] وَيَصْلَىٰ سَعِيرًا
- (85:5) [listed for 87:12] ٱلنَّارِ ذَاتِ ٱلْوَقُودِ
- (85:10) [listed for 87:12] إِنَّ ٱلَّذِينَ فَتَنُوا۟ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ثُمَّ لَمْ يَتُوبُوا۟ فَلَهُمْ عَذَابُ جَهَنَّمَ وَلَهُمْ عَذَابُ ٱلْحَرِيقِ
- (88:24) [listed for 87:12] فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- (90:20) [listed for 87:12] عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ
- (98:6) [listed for 87:12] إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- (102:7) [listed for 87:12] ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- (104:6) [listed for 87:12] نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- (104:7) [listed for 87:12] ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- (104:9) [listed for 87:12] فِى عَمَدٍۢ مُّمَدَّدَةٍۭ

## named by the passage's own list as strong for this ayah (3)

- (10:52) [listed for 87:12] ثُمَّ قِيلَ لِلَّذِينَ ظَلَمُوا۟ ذُوقُوا۟ عَذَابَ ٱلْخُلْدِ هَلْ تُجْزَوْنَ إِلَّا بِمَا كُنتُمْ تَكْسِبُونَ
- (18:53) [listed for 87:12] وَرَءَا ٱلْمُجْرِمُونَ ٱلنَّارَ فَظَنُّوٓا۟ أَنَّهُم مُّوَاقِعُوهَا وَلَمْ يَجِدُوا۟ عَنْهَا مَصْرِفًۭا
- (79:39) [listed for 87:12] [cited in ¶15] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ

## named by the passage's own list as medium for this ayah (14)

- (2:175) [listed for 87:12] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ وَٱلْعَذَابَ بِٱلْمَغْفِرَةِ ۚ فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ
- (4:121) [listed for 87:12] أُو۟لَٰٓئِكَ مَأْوَىٰهُمْ جَهَنَّمُ وَلَا يَجِدُونَ عَنْهَا مَحِيصًۭا
- (18:100) [listed for 87:12] وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا
- (32:22) [listed for 87:12] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ ثُمَّ أَعْرَضَ عَنْهَآ ۚ إِنَّا مِنَ ٱلْمُجْرِمِينَ مُنتَقِمُونَ
- (37:30) [listed for 87:12] وَمَا كَانَ لَنَا عَلَيْكُم مِّن سُلْطَٰنٍۭ ۖ بَلْ كُنتُمْ قَوْمًۭا طَٰغِينَ
- (39:72) [listed for 87:12] قِيلَ ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (40:56) [listed for 87:12] إِنَّ ٱلَّذِينَ يُجَٰدِلُونَ فِىٓ ءَايَٰتِ ٱللَّهِ بِغَيْرِ سُلْطَٰنٍ أَتَىٰهُمْ ۙ إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ مَّا هُم بِبَٰلِغِيهِ ۚ فَٱسْتَعِذْ بِٱللَّهِ ۖ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- (40:72) [listed for 87:12] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
- (43:75) [listed for 87:12] لَا يُفَتَّرُ عَنْهُمْ وَهُمْ فِيهِ مُبْلِسُونَ
- (56:71) [listed for 87:12] [cited in ¶11] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
- (73:12) [listed for 87:12] إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا
- (74:23) [listed for 87:12] [cited in ¶19] ثُمَّ أَدْبَرَ وَٱسْتَكْبَرَ
- (85:11) [listed for 87:12] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْكَبِيرُ
- (101:9) [listed for 87:12] فَأُمُّهُۥ هَاوِيَةٌۭ

## weak (this ayah's own list) (22)

- (2:34) [listed for 87:12] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ وَٱسْتَكْبَرَ وَكَانَ مِنَ ٱلْكَٰفِرِينَ
- (2:80) [listed for 87:12] وَقَالُوا۟ لَن تَمَسَّنَا ٱلنَّارُ إِلَّآ أَيَّامًۭا مَّعْدُودَةًۭ ۚ قُلْ أَتَّخَذْتُمْ عِندَ ٱللَّهِ عَهْدًۭا فَلَن يُخْلِفَ ٱللَّهُ عَهْدَهُۥٓ ۖ أَمْ تَقُولُونَ عَلَى ٱللَّهِ مَا لَا تَعْلَمُونَ
- (2:174) [listed for 87:12] إِنَّ ٱلَّذِينَ يَكْتُمُونَ مَآ أَنزَلَ ٱللَّهُ مِنَ ٱلْكِتَٰبِ وَيَشْتَرُونَ بِهِۦ ثَمَنًۭا قَلِيلًا ۙ أُو۟لَٰٓئِكَ مَا يَأْكُلُونَ فِى بُطُونِهِمْ إِلَّا ٱلنَّارَ وَلَا يُكَلِّمُهُمُ ٱللَّهُ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ
- (3:7) [listed for 87:12] هُوَ ٱلَّذِىٓ أَنزَلَ عَلَيْكَ ٱلْكِتَٰبَ مِنْهُ ءَايَٰتٌۭ مُّحْكَمَٰتٌ هُنَّ أُمُّ ٱلْكِتَٰبِ وَأُخَرُ مُتَشَٰبِهَٰتٌۭ ۖ فَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِمْ زَيْغٌۭ فَيَتَّبِعُونَ مَا تَشَٰبَهَ مِنْهُ ٱبْتِغَآءَ ٱلْفِتْنَةِ وَٱبْتِغَآءَ تَأْوِيلِهِۦ ۗ وَمَا يَعْلَمُ تَأْوِيلَهُۥٓ إِلَّا ٱللَّهُ ۗ وَٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ يَقُولُونَ ءَامَنَّا بِهِۦ كُلٌّۭ مِّنْ عِندِ رَبِّنَا ۗ وَمَا يَذَّكَّرُ إِلَّآ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (3:16) [listed for 87:12] ٱلَّذِينَ يَقُولُونَ رَبَّنَآ إِنَّنَآ ءَامَنَّا فَٱغْفِرْ لَنَا ذُنُوبَنَا وَقِنَا عَذَابَ ٱلنَّارِ
- (3:24) [listed for 87:12] ذَٰلِكَ بِأَنَّهُمْ قَالُوا۟ لَن تَمَسَّنَا ٱلنَّارُ إِلَّآ أَيَّامًۭا مَّعْدُودَٰتٍۢ ۖ وَغَرَّهُمْ فِى دِينِهِم مَّا كَانُوا۟ يَفْتَرُونَ
- (3:39) [listed for 87:12] فَنَادَتْهُ ٱلْمَلَٰٓئِكَةُ وَهُوَ قَآئِمٌۭ يُصَلِّى فِى ٱلْمِحْرَابِ أَنَّ ٱللَّهَ يُبَشِّرُكَ بِيَحْيَىٰ مُصَدِّقًۢا بِكَلِمَةٍۢ مِّنَ ٱللَّهِ وَسَيِّدًۭا وَحَصُورًۭا وَنَبِيًّۭا مِّنَ ٱلصَّٰلِحِينَ
- (6:35) [listed for 87:12] وَإِن كَانَ كَبُرَ عَلَيْكَ إِعْرَاضُهُمْ فَإِنِ ٱسْتَطَعْتَ أَن تَبْتَغِىَ نَفَقًۭا فِى ٱلْأَرْضِ أَوْ سُلَّمًۭا فِى ٱلسَّمَآءِ فَتَأْتِيَهُم بِـَٔايَةٍۢ ۚ وَلَوْ شَآءَ ٱللَّهُ لَجَمَعَهُمْ عَلَى ٱلْهُدَىٰ ۚ فَلَا تَكُونَنَّ مِنَ ٱلْجَٰهِلِينَ
- (6:93) [listed for 87:12] وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ قَالَ أُوحِىَ إِلَىَّ وَلَمْ يُوحَ إِلَيْهِ شَىْءٌۭ وَمَن قَالَ سَأُنزِلُ مِثْلَ مَآ أَنزَلَ ٱللَّهُ ۗ وَلَوْ تَرَىٰٓ إِذِ ٱلظَّٰلِمُونَ فِى غَمَرَٰتِ ٱلْمَوْتِ وَٱلْمَلَٰٓئِكَةُ بَاسِطُوٓا۟ أَيْدِيهِمْ أَخْرِجُوٓا۟ أَنفُسَكُمُ ۖ ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَقُولُونَ عَلَى ٱللَّهِ غَيْرَ ٱلْحَقِّ وَكُنتُمْ عَنْ ءَايَٰتِهِۦ تَسْتَكْبِرُونَ
- (8:14) [listed for 87:12] ذَٰلِكُمْ فَذُوقُوهُ وَأَنَّ لِلْكَٰفِرِينَ عَذَابَ ٱلنَّارِ
- (33:43) [listed for 87:12] هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ لِيُخْرِجَكُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَكَانَ بِٱلْمُؤْمِنِينَ رَحِيمًۭا
- (35:43) [listed for 87:12] ٱسْتِكْبَارًۭا فِى ٱلْأَرْضِ وَمَكْرَ ٱلسَّيِّئِ ۚ وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِۦ ۚ فَهَلْ يَنظُرُونَ إِلَّا سُنَّتَ ٱلْأَوَّلِينَ ۚ فَلَن تَجِدَ لِسُنَّتِ ٱللَّهِ تَبْدِيلًۭا ۖ وَلَن تَجِدَ لِسُنَّتِ ٱللَّهِ تَحْوِيلًا
- (36:80) [listed for 87:12] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
- (38:27) [listed for 87:12] وَمَا خَلَقْنَا ٱلسَّمَآءَ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا بَٰطِلًۭا ۚ ذَٰلِكَ ظَنُّ ٱلَّذِينَ كَفَرُوا۟ ۚ فَوَيْلٌۭ لِّلَّذِينَ كَفَرُوا۟ مِنَ ٱلنَّارِ
- (39:19) [listed for 87:12] أَفَمَنْ حَقَّ عَلَيْهِ كَلِمَةُ ٱلْعَذَابِ أَفَأَنتَ تُنقِذُ مَن فِى ٱلنَّارِ
- (40:43) [listed for 87:12] لَا جَرَمَ أَنَّمَا تَدْعُونَنِىٓ إِلَيْهِ لَيْسَ لَهُۥ دَعْوَةٌۭ فِى ٱلدُّنْيَا وَلَا فِى ٱلْءَاخِرَةِ وَأَنَّ مَرَدَّنَآ إِلَى ٱللَّهِ وَأَنَّ ٱلْمُسْرِفِينَ هُمْ أَصْحَٰبُ ٱلنَّارِ
- (41:19) [listed for 87:12] وَيَوْمَ يُحْشَرُ أَعْدَآءُ ٱللَّهِ إِلَى ٱلنَّارِ فَهُمْ يُوزَعُونَ
- (53:18) [listed for 87:12] لَقَدْ رَأَىٰ مِنْ ءَايَٰتِ رَبِّهِ ٱلْكُبْرَىٰٓ
- (54:53) [listed for 87:12] وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ
- (55:35) [listed for 87:12] يُرْسَلُ عَلَيْكُمَا شُوَاظٌۭ مِّن نَّارٍۢ وَنُحَاسٌۭ فَلَا تَنتَصِرَانِ
- (64:8) [listed for 87:12] فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَٱلنُّورِ ٱلَّذِىٓ أَنزَلْنَا ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (66:8) [listed for 87:12] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ

## named by the passage's own list as weak for this ayah (7)

- (4:30) [listed for 87:12] وَمَن يَفْعَلْ ذَٰلِكَ عُدْوَٰنًۭا وَظُلْمًۭا فَسَوْفَ نُصْلِيهِ نَارًۭا ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًا
- (7:13) [listed for 87:12] قَالَ فَٱهْبِطْ مِنْهَا فَمَا يَكُونُ لَكَ أَن تَتَكَبَّرَ فِيهَا فَٱخْرُجْ إِنَّكَ مِنَ ٱلصَّٰغِرِينَ
- (7:48) [listed for 87:12] وَنَادَىٰٓ أَصْحَٰبُ ٱلْأَعْرَافِ رِجَالًۭا يَعْرِفُونَهُم بِسِيمَىٰهُمْ قَالُوا۟ مَآ أَغْنَىٰ عَنكُمْ جَمْعُكُمْ وَمَا كُنتُمْ تَسْتَكْبِرُونَ
- (25:52) [listed for 87:12] فَلَا تُطِعِ ٱلْكَٰفِرِينَ وَجَٰهِدْهُم بِهِۦ جِهَادًۭا كَبِيرًۭا
- (27:7) [listed for 87:12] [cited in ¶6] إِذْ قَالَ مُوسَىٰ لِأَهْلِهِۦٓ إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ
- (55:15) [listed for 87:12] وَخَلَقَ ٱلْجَآنَّ مِن مَّارِجٍۢ مِّن نَّارٍۢ
- (82:15) [listed for 87:12] يَصْلَوْنَهَا يَوْمَ ٱلدِّينِ

## neighbours: within two ayat of a passage the commentary cites (75)

- (2:22) [next to 2:24] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
- (2:23) [next to 2:24] وَإِن كُنتُمْ فِى رَيْبٍۢ مِّمَّا نَزَّلْنَا عَلَىٰ عَبْدِنَا فَأْتُوا۟ بِسُورَةٍۢ مِّن مِّثْلِهِۦ وَٱدْعُوا۟ شُهَدَآءَكُم مِّن دُونِ ٱللَّهِ إِن كُنتُمْ صَٰدِقِينَ
- (2:25) [next to 2:24] وَبَشِّرِ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ كُلَّمَا رُزِقُوا۟ مِنْهَا مِن ثَمَرَةٍۢ رِّزْقًۭا ۙ قَالُوا۟ هَٰذَا ٱلَّذِى رُزِقْنَا مِن قَبْلُ ۖ وَأُتُوا۟ بِهِۦ مُتَشَٰبِهًۭا ۖ وَلَهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَهُمْ فِيهَا خَٰلِدُونَ
- (2:26) [next to 2:24] ۞ إِنَّ ٱللَّهَ لَا يَسْتَحْىِۦٓ أَن يَضْرِبَ مَثَلًۭا مَّا بَعُوضَةًۭ فَمَا فَوْقَهَا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۖ وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَيَقُولُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۘ يُضِلُّ بِهِۦ كَثِيرًۭا وَيَهْدِى بِهِۦ كَثِيرًۭا ۚ وَمَا يُضِلُّ بِهِۦٓ إِلَّا ٱلْفَٰسِقِينَ
- (2:43) [next to 2:45] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ
- (2:44) [next to 2:45] ۞ أَتَأْمُرُونَ ٱلنَّاسَ بِٱلْبِرِّ وَتَنسَوْنَ أَنفُسَكُمْ وَأَنتُمْ تَتْلُونَ ٱلْكِتَٰبَ ۚ أَفَلَا تَعْقِلُونَ
- (2:46) [next to 2:45] ٱلَّذِينَ يَظُنُّونَ أَنَّهُم مُّلَٰقُوا۟ رَبِّهِمْ وَأَنَّهُمْ إِلَيْهِ رَٰجِعُونَ
- (2:47) [next to 2:45] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (4:54) [next to 4:56] أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۖ فَقَدْ ءَاتَيْنَآ ءَالَ إِبْرَٰهِيمَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَءَاتَيْنَٰهُم مُّلْكًا عَظِيمًۭا
- (4:55) [next to 4:56] فَمِنْهُم مَّنْ ءَامَنَ بِهِۦ وَمِنْهُم مَّن صَدَّ عَنْهُ ۚ وَكَفَىٰ بِجَهَنَّمَ سَعِيرًا
- (4:57) [next to 4:56] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (4:58) [next to 4:56] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
- (27:5) [next to 27:7] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَهُمْ سُوٓءُ ٱلْعَذَابِ وَهُمْ فِى ٱلْءَاخِرَةِ هُمُ ٱلْأَخْسَرُونَ
- (27:6) [next to 27:7] وَإِنَّكَ لَتُلَقَّى ٱلْقُرْءَانَ مِن لَّدُنْ حَكِيمٍ عَلِيمٍ
- (27:8) [next to 27:7] فَلَمَّا جَآءَهَا نُودِىَ أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (27:9) [next to 27:7] يَٰمُوسَىٰٓ إِنَّهُۥٓ أَنَا ٱللَّهُ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (32:19) [next to 32:21] أَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ جَنَّٰتُ ٱلْمَأْوَىٰ نُزُلًۢا بِمَا كَانُوا۟ يَعْمَلُونَ
- (32:23) [next to 32:21] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَلَا تَكُن فِى مِرْيَةٍۢ مِّن لِّقَآئِهِۦ ۖ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ
- (40:58) [next to 40:60] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَلَا ٱلْمُسِىٓءُ ۚ قَلِيلًۭا مَّا تَتَذَكَّرُونَ
- (40:59) [next to 40:60] إِنَّ ٱلسَّاعَةَ لَءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (40:61) [next to 40:60] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلَّيْلَ لِتَسْكُنُوا۟ فِيهِ وَٱلنَّهَارَ مُبْصِرًا ۚ إِنَّ ٱللَّهَ لَذُو فَضْلٍ عَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (40:62) [next to 40:60] ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ خَٰلِقُ كُلِّ شَىْءٍۢ لَّآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (42:11) [next to 42:13] فَاطِرُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَمِنَ ٱلْأَنْعَٰمِ أَزْوَٰجًۭا ۖ يَذْرَؤُكُمْ فِيهِ ۚ لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- (42:12) [next to 42:13] لَهُۥ مَقَالِيدُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (42:14) [next to 42:13] وَمَا تَفَرَّقُوٓا۟ إِلَّا مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْعِلْمُ بَغْيًۢا بَيْنَهُمْ ۚ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى لَّقُضِىَ بَيْنَهُمْ ۚ وَإِنَّ ٱلَّذِينَ أُورِثُوا۟ ٱلْكِتَٰبَ مِنۢ بَعْدِهِمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- (42:15) [next to 42:13] فَلِذَٰلِكَ فَٱدْعُ ۖ وَٱسْتَقِمْ كَمَآ أُمِرْتَ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ ۖ وَقُلْ ءَامَنتُ بِمَآ أَنزَلَ ٱللَّهُ مِن كِتَٰبٍۢ ۖ وَأُمِرْتُ لِأَعْدِلَ بَيْنَكُمُ ۖ ٱللَّهُ رَبُّنَا وَرَبُّكُمْ ۖ لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ ۖ لَا حُجَّةَ بَيْنَنَا وَبَيْنَكُمُ ۖ ٱللَّهُ يَجْمَعُ بَيْنَنَا ۖ وَإِلَيْهِ ٱلْمَصِيرُ
- (56:69) [next to 56:71] ءَأَنتُمْ أَنزَلْتُمُوهُ مِنَ ٱلْمُزْنِ أَمْ نَحْنُ ٱلْمُنزِلُونَ
- (56:70) [next to 56:71] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
- (56:72) [next to 56:71] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
- (56:74) [next to 56:73] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (56:75) [next to 56:73] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (70:13) [next to 70:15] وَفَصِيلَتِهِ ٱلَّتِى تُـْٔوِيهِ
- (70:14) [next to 70:15] وَمَن فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ يُنجِيهِ
- (70:16) [next to 70:15] نَزَّاعَةًۭ لِّلشَّوَىٰ
- (70:17) [next to 70:15] تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ
- (70:20) [next to 70:22] إِذَا مَسَّهُ ٱلشَّرُّ جَزُوعًۭا
- (70:21) [next to 70:22] وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا
- (70:23) [next to 70:22] ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ
- (70:24) [next to 70:22] وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ
- (74:1) [next to 74:3] يَٰٓأَيُّهَا ٱلْمُدَّثِّرُ
- (74:2) [next to 74:3] قُمْ فَأَنذِرْ
- (74:4) [next to 74:3] وَثِيَابَكَ فَطَهِّرْ
- (74:5) [next to 74:3] وَٱلرُّجْزَ فَٱهْجُرْ
- (74:16) [next to 74:18] كَلَّآ ۖ إِنَّهُۥ كَانَ لِءَايَٰتِنَا عَنِيدًۭا
- (74:17) [next to 74:18] سَأُرْهِقُهُۥ صَعُودًا
- (74:19) [next to 74:18] فَقُتِلَ كَيْفَ قَدَّرَ
- (74:20) [next to 74:18] ثُمَّ قُتِلَ كَيْفَ قَدَّرَ
- (74:21) [next to 74:23] ثُمَّ نَظَرَ
- (74:22) [next to 74:23] ثُمَّ عَبَسَ وَبَسَرَ
- (74:25) [next to 74:23] إِنْ هَٰذَآ إِلَّا قَوْلُ ٱلْبَشَرِ
- (74:30) [next to 74:28] عَلَيْهَا تِسْعَةَ عَشَرَ
- (74:32) [next to 74:31] كَلَّا وَٱلْقَمَرِ
- (74:33) [next to 74:31] وَٱلَّيْلِ إِذْ أَدْبَرَ
- (74:34) [next to 74:35] وَٱلصُّبْحِ إِذَآ أَسْفَرَ
- (74:36) [next to 74:35] نَذِيرًۭا لِّلْبَشَرِ
- (74:37) [next to 74:35] لِمَن شَآءَ مِنكُمْ أَن يَتَقَدَّمَ أَوْ يَتَأَخَّرَ
- (74:40) [next to 74:42] فِى جَنَّٰتٍۢ يَتَسَآءَلُونَ
- (74:41) [next to 74:42] عَنِ ٱلْمُجْرِمِينَ
- (74:44) [next to 74:42] وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ
- (74:45) [next to 74:43] وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ
- (74:47) [next to 74:49] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
- (74:48) [next to 74:49] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
- (74:52) [next to 74:50] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
- (74:53) [next to 74:51] كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ
- (79:29) [next to 79:31] وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا
- (79:30) [next to 79:31] وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ
- (79:32) [next to 79:31] وَٱلْجِبَالَ أَرْسَىٰهَا
- (79:33) [next to 79:31] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (79:37) [next to 79:35] فَأَمَّا مَن طَغَىٰ
- (79:40) [next to 79:38] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
- (79:41) [next to 79:39] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- (92:12) [next to 92:14] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:13) [next to 92:14] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:18) [next to 92:16] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- (92:19) [next to 92:17] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ

