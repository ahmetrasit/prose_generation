Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:12; its ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Lookups: once you have read the whole prompt, gather every passage whose Arabic you want to read (listed or from your own knowledge) and read them together, in one message (several `text` calls side by side when there are more than 40 refs), instead of one lookup at a time while you judge; a later lookup is fine when something new comes up.

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

===== _commentary/v16/out/88_12/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_12.reading.tr.md (prose paragraphs numbered) =====
## Bahçenin içinde bir pınar

[¶1] On ikinci ayet yalnızca üç kelimedir: {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Cümle "orada" sözüyle açılır, yani neyin bulunduğunu söylemeden önce nerede bulunduğunu söyler. Bu sözdeki zamir onuncu ayetteki bahçeye döner: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:88:10}. Sure bahçeyi içinde bulunanları sayarak anlatır ve "orada" sözü ayetten ayete tekrarlanır. On birinci ayet orada neyin olmadığını söyler: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmau fîhâ lâğiye, gloss:orada boş bir söz işitmezsin, source:88:11}. On ikinci ayet orada bulunan ilk şeyi söyler. On üçüncü ayet de aynı sözle devam eder: {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada yükseltilmiş sedirler vardır, source:88:13}. Böylece bahçede sayılan nesnelerin başına su gelir. Sedirler, kadehler, yastıklar ve halılar ondan sonra sayılır.

[¶2] Pınar belirsiz bir isimle ve tekil olarak anılır, ona bir ad da verilmez. Beşinci ayetteki pınar da aynı biçimdedir: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:son kertesine varmış sıcak bir pınardan içirilir, source:88:5}. Sure aynı ismi iki kez kullanır ve iki pınarı yalnızca sıfatlarıyla ayırır. Bu karşılaşma, beşinci ayetin kelimeleriyle birlikte surenin bütününe ait bir sahnedir. Cümle yapısındaki bir fark ise bu ayete aittir. Beşinci ayette yüz edilgen bir fiilin öznesidir, yani ona içirilir. On ikinci ayette içme fiili hiç geçmez. Pınar orada bulunur ve akar. Ayet ondan başka bir şey söylemez.

## Göz ve göze

[¶3] Ayette pınar anlamına gelen عين kelimesi, Arapçada gözün de adıdır: {ar:العين الناظرة لكل ذي بصر, tr:el-aynu'n-nâzıratu li-kulli zî basar, gloss:gören her canlının bakan gözü, source:"ع ي ن,B001"}. Ayetteki anlam pınardır. Göz bu anlamın yanında duyulur, onun yerine geçmez. Aşağıda gelen bütün imgeler için de durum böyledir. Pınar için şöyle denirdi: {ar:العين الينبوع الذي ينبع من الأرض ويجري, tr:el-aynu'l-yenbûu'llezî yenbau mine'l-ardi ve yecrî, gloss:yerden kaynayıp akan kaynak, source:"ع ي ن,B006"}. Bu tanımın son kelimesi ayetin ikinci kelimesiyle aynı fiildir. Pınar, adı gereği akan sudur. Türkçe de aynı yolu izler ve suyun yerden çıktığı yere "göze" der. Türk okur bu imgeyi kendi dilinden tanır.

[¶4] Pınar, yer altında biriken suyun toprağın yüzüne çıktığı dar bir ağızdır. Bu ağız yuvarlaktır, ıslak ve parlaktır, içinden de su taşar. Araplar aynı benzerliği başka bir nesnede de görmüşlerdir. Deriden yapılmış su tulumu eskiyince bazı yerleri incelir ve delinip su sızdırır. Bu yerlere de göz denirdi ve adın nereden geldiği açıkça söylenirdi: {ar:الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء, tr:es-sekbu fi'l-mezâdeti teşbîhen bihâ fi'l-hey'eti ve fî seylâni'l-mâ', gloss:su tulumundaki delik; biçimde ve suyun akışında göze benzetilerek, source:"ع ي ن,B007"}. Delik göze iki yönden benzer: biçimi yuvarlaktır ve içinden su akar. Gözün su akıtması Kur'an'da da anlatılır. Peygamber'e indirileni işitip onda hakkı tanıyan ve "Rabbimiz, inandık, bizi şahitlerle birlikte yaz" diyen bir topluluk için şöyle denir: {ar:تَرَىٰٓ أَعْيُنَهُمْ تَفِيضُ مِنَ ٱلدَّمْعِ, tr:terâ a'yunehum tefîdu mine'd-dem', gloss:gözlerinin yaştan taştığını görürsün, source:5:83}. Göz, içinden su taşan bir ağızdır. Pınar da yerin böyle bir gözüdür.

[¶5] Araplar kuyunun suyunun geldiği çukurlara da göz derlerdi: {ar:عين الركية, tr:aynu'r-rakiyye, gloss:kuyunun su gözü, source:"ع ي ن,B009"}. Ancak kuyunun gözü dipte kalır. Su ancak iple ve kovayla yukarı çekilir. Kur'an bunu Yusuf kıssasında gösterir. Kardeşleri Yusuf'u kuyunun dibine bıraktıktan sonra oradan bir kervan geçer: {ar:فَأَرْسَلُوا۟ وَارِدَهُمْ فَأَدْلَىٰ دَلْوَهُۥ, tr:fe-erselû vâridehum fe-edlâ delveh, gloss:sucularını gönderdiler, o da kovasını sarkıttı, source:12:19}. Kuyunun suyu gizlidir ve emekle çekilir. Pınarın suyu ise kendiliğinden yüzeye çıkar. Araplar bu açıklıktan ötürü yüzeyde akan suya da şöyle derlerdi: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Burada iki göz birbirine bakar: yerin gözünden çıkan su insanın gözüne görünür. Kur'an bu suyu Peygamber'e sordurulan bir soruda anar: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki: suyunuz yerin dibine çekilse size göz önünde akan suyu kim getirir, source:67:30}. Dünyadaki su yerin derinliğine çekilip kaybolabilir. Bahçedeki pınar ise bahçenin "içinde" bulunur ve akmaya devam eder.

[¶6] Kur'an göz önünde akan suyu bir yerde yükseklikle birlikte anar. Meryem'in oğlu ile annesinin bir ayet kılındığı anlatılırken şöyle denir: {ar:وَءَاوَيْنَٰهُمَآ إِلَىٰ رَبْوَةٍۢ ذَاتِ قَرَارٍۢ وَمَعِينٍۢ, tr:ve âveynâhumâ ilâ rabvetin zâti karârin ve maîn, gloss:onları yerleşmeye elverişli ve akar sulu bir tepeye yerleştirdik, source:23:50}. Sure de bahçeyi onuncu ayette "yüksek" diye nitelemişti. On ikinci ayet bu yüksek yerde, kova ile çekilmeyen ve göz önünde akan bir su gösterir.

## Akan su bozulmaz

[¶7] Ayetin ikinci kelimesi suyun akışını anlatır. Bu kelimenin temeli şöyle tarif edilir: {ar:أصل واحد وهو انسياح الشيء, tr:aslun vâhidun ve huve'nsiyâhu'ş-şey', gloss:tek bir kök: bir şeyin yayılıp akması, source:"ج ر ي,B001"}. Su için de şöyle denirdi: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî ciryeten ve cerye'n ve cereyânâ, gloss:su aktı, akar, source:"ج ر ي,B001"}. Türkçedeki "cereyan" bu son kelimeden gelir ve hâlâ akan havayı, elektrik akımını anlatır. "Mecra" da suyun aktığı yatağın adıdır. Buna karşılık "câriye" kelimesi Türkçede yalnızca hizmetçi kız anlamında kalmıştır. Arapça bu biçimle genç kızı da adlandırır, ama ayetteki kelime pınarın sıfatıdır. Türkçedeki "cariye" bu ayette aranmamalıdır. Kelime burada akan suyu anlatır.

[¶8] Akan suyu durgun sudan ayıran şey yenilenmesidir. Bir çukurda duran su yerinde kalır, ısınır, kokusu ve tadı değişir. Pınardan akan suyun ise her an yerine yenisi gelir. Kur'an takvalılara vaat edilen bahçeyi anlatırken bu farkı açıkça söyler: {ar:فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ, tr:fîhâ enhârun min mâin ğayri âsinin ve enhârun min lebenin lem yeteğayyer ta'muh, gloss:orada bozulmayan sudan ırmaklar ve tadı değişmeyen sütten ırmaklar vardır, source:47:15}. Aynı ayet sonunda öteki tarafı da gösterir ve bahçedekini, ateşte kalanla karşılaştırır: {ar:وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ, tr:ve sukû mâen hamîmen fe-katta'a em'âehum, gloss:kaynar su içirilmiş ve bu su bağırsaklarını parçalamıştır, source:47:15}. Beşinci ayetteki içirilme fiili burada da kullanılır. Bu ayet Gâşiye'nin iki pınarını tek bir cümlede yan yana getirir. Bir yanda tadı değişmeyen su, öbür yanda kaynar su vardır.

[¶9] Kur'an bahçeleri en çok bu akışla anar. İnanıp iyi işler yapanlara verilen müjde şöyledir: {ar:جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:cennâtin tecrî min tahtihe'l-enhâr, gloss:altlarından ırmaklar akan bahçeler, source:2:25}. Burada geçen fiil, on ikinci ayetteki sıfatla aynıdır. Rabbinin makamından korkanlara verilen iki bahçede de iki pınar akar {source:55:50}. On ikinci ayet, bahçenin bu bilinen niteliğini tek bir pınarda toplar.

## Kesilmeyen akış

[¶10] Arapça "akmak" fiilini, bir şeyin sürüp gitmesi için de kullanır. Düzenli verilen geçimlik için şöyle denirdi: {ar:الأرزاق جارية والأعطيات دارة, tr:el-erzâku câriyetun ve'l-a'tıyâtu dârra, gloss:rızıklar akar, bağışlar sağılır gibi bol gelir, source:"ج ر ي,B006"}. Bu kullanımın ne demek olduğu da açıkça söylenirdi: {ar:جرى عليه ذلك الشيء ودر له بمعنى دام له, tr:cerâ aleyhi zâlike'ş-şey'u ve derra leh, bi-ma'nâ dâme leh, gloss:o şey ona aktı ve bol geldi, yani onun için sürdü, source:"ج ر ي,B006"}; {ar:أجريت له كذا أي أدمت له, tr:ecraytu lehû kezâ ey edemtu leh, gloss:ona şunu akıttım, yani onun için sürdürdüm, source:"ج ر ي,B006"}. Yararı kesilmeyen bağışa da {ar:صدقة جارية, tr:sadakatun câriye, gloss:akan, yani süren sadaka, source:"ج ر ي,B006"} denirdi. Bu, ayetteki kelimenin ta kendisidir. Türkçedeki "cari" kelimesi bu anlamı korumuştur. "Cari hesap" kapanmamış, işlemeye devam eden hesaptır. Ayetteki pınarın sıfatında akışın yanında süreklilik de duyulur. Pınar bir kez akıp duran değil, akmaya devam eden bir sudur.

[¶11] Kur'an iki anlamı tek bir ayette yan yana getirir. Takvalılara vaat edilen bahçenin misali şöyledir: {ar:تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ أُكُلُهَا دَآئِمٌۭ وَظِلُّهَا, tr:tecrî min tahtihe'l-enhâru ukuluhâ dâimun ve zılluhâ, gloss:altından ırmaklar akar; yemişi de gölgesi de süreklidir, source:13:35}. Ayet, inkâr edenlerin varacağı yerin ateş olduğunu söyleyerek biter. Akmak ile sürmek, Araplar'ın açıklamasında olduğu gibi, burada da yan yana durur. Sâd suresinde Allah, takvalılar için hazırlanmış kapıları açık Adn bahçelerini, orada yaslanıp meyve ve içecek isteyenleri anlatır. Bunların hesap günü için vaat edildiğini söyledikten sonra şöyle der: {ar:إِنَّ هَٰذَا لَرِزْقُنَا مَا لَهُۥ مِن نَّفَادٍ, tr:inne hâzâ le-rizkunâ mâ lehû min nefâd, gloss:işte bu bizim rızkımızdır, onun tükenmesi yoktur, source:38:54}.

[¶12] Surenin ilk yarısında yemek de içecek de yetersizdir. Yedinci ayet yiyecek için {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besler ne açlıktan kurtarır, source:88:7} der. Beşinci ayetteki pınarın sıfatı, kaynayan suyun sıcaklığının son kertesine vardığını söyler. Kur'an aynı kökten bir fiille bir şeyin vaktinin gelip çattığını da anlatır: {ar:أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ, tr:e-lem ye'ni lillezîne âmenû en tahşea kulûbuhum, gloss:inananların kalplerinin saygıyla yumuşamasının vakti gelmedi mi, source:57:16}. Ateşin pınarı ucuna varmış olmasıyla adlandırılır. Bahçenin pınarı ise akışı süren bir sudur.

## Gökteki göz, bahçedeki göz

[¶13] Ayetin iki kelimesi Arapçada ayrı ayrı güneşin de adıdır. Güneş için şöyle denirdi: {ar:طلعت العين وغابت العين، أي الشمس, tr:tala'ati'l-aynu ve ğâbeti'l-ayn, eyi'ş-şems, gloss:göz doğdu, göz battı; yani güneş, source:"ع ي ن,B008"}. Bu adın nereden geldiği de söylenirdi: {ar:عين الشمس مشبه بعين الإنسان, tr:aynu'ş-şemsi muşebbehun bi-ayni'l-insân, gloss:güneşin gözü insanın gözüne benzetilmiştir, source:"ع ي ن,B008"}. Akmak kelimesinden de güneşe ad verilmiştir: {ar:الجارية السفينة والجارية الشمس, tr:el-câriyetu's-sefînetu ve'l-câriyetu'ş-şems, gloss:akan, gemidir; akan, güneştir, source:"ج ر ي,B001"}. Ayet güneşten söz etmez, ama kelimeleri tek tek güneşi de adlandırır. Bu yüzden "akan göz" ifadesi, kelimeleri bakımından güneş için de söylenebilir.

[¶14] Kur'an güneşin akışını anlatırken her seferinde bir sınır koyar. Gece ve gündüzün ayetler olarak sayıldığı yerde şöyle denir: {ar:وَٱلشَّمْسُ تَجْرِى لِمُسْتَقَرٍّۢ لَّهَا, tr:ve'ş-şemsu tecrî li-mustekarrin lehâ, gloss:güneş kendisi için belirlenmiş bir duraklama yerine doğru akar, source:36:38}. Gökleri direksiz yükselten Allah'ın güneşi ve ayı buyruğu altına aldığı anlatılırken de şöyle denir: {ar:كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّۭى, tr:kullun yecrî li-ecelin musemmâ, gloss:her biri adı konmuş bir süreye kadar akar, source:13:2}. Dünyada gökte akan göz bir sona doğru akar.

[¶15] Bahçede ise güneş yoktur. Allah'ın o günün kötülüğünden koruduğu ve sabırlarına karşılık bahçe ve ipek verdiği kişiler için şöyle denir: {ar:لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا, tr:lâ yerevne fîhâ şemsen ve lâ zemherîrâ, gloss:orada ne güneş görürler ne dondurucu soğuk, source:76:13}. Surenin ilk yarısındaki yüz ise sıcağın içindedir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Bu iki kelimenin birleşmesi bir yorum bağıdır ve ayetin anlamı değildir. Ancak kelimeler bu bağı destekler. Güneşin görülmediği bahçede akan göz sudur. Gökteki akan göz bir süreye kadar akar, bahçedeki ise akmaya devam eder.

## Tufanda göz ve akış

[¶16] Ayetin iki kökü Kur'an'da bir başka sahnede birlikte geçer, ama orada görevleri birbirinden ayrılır. Kamer suresi Nuh'un kavmini anlatır. Kavim Nuh'u yalanlamış, ona "deli" demiş ve onu azarlamıştır. Nuh Rabbine "yenildim, yardım et" diye seslenir. Allah da göğün kapılarını boşanan bir suyla açar ve şöyle der: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا, tr:ve feccerne'l-arda uyûnâ, gloss:yeri pınarlar halinde fışkırttık, source:54:12}. Gökten inen su ile yerden kaynayan su takdir edilmiş bir iş için buluşur. Nuh da {ar:ذَاتِ أَلْوَٰحٍۢ وَدُسُرٍۢ, tr:zâti elvâhin ve dusur, gloss:tahtalardan ve çivilerden yapılmış bir şey, source:54:13} üzerinde taşınır. Bu taşıtın nasıl ilerlediği şöyle anlatılır: {ar:تَجْرِى بِأَعْيُنِنَا, tr:tecrî bi-a'yuninâ, gloss:gözlerimizin önünde akıp gider, source:54:14}.

[¶17] Burada göz, gözetmek ve korumak anlamındadır. Araplar koruyup kolladıkları biri için şöyle derlerdi: {ar:فلان بعيني أي أحفظه وأراعيه, tr:fulânun bi-aynî ey ehfazuhû ve urâîh, gloss:o benim gözümdedir, yani onu korur ve gözetirim, source:"ع ي ن,B003"}. Aynı ifade şöyle de açıklanırdı: {ar:بحيث نرى ونحفظ, tr:bi-haysu nerâ ve nahfaz, gloss:gördüğümüz ve koruduğumuz yerde, source:"ع ي ن,B003"}. Tufan sahnesinde "pınarlar" yerin suyudur ve yalanlayan kavmi boğar. Akış ise gemiye aittir ve gemi gözetim altında yol alır. Hâkka suresi aynı gemiye doğrudan bu sıfatın adını verir. Orada Firavun'un ve yerle bir edilen şehirlerin elçiye isyan edip yakalandığı anlatıldıktan sonra Allah şöyle der: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağe'l-mâu hamelnâkum fi'l-câriye, gloss:su taşınca sizi akan gemide taşıdık, source:69:11}.

[¶18] Gâşiye'nin on ikinci ayetinde bu iki kelime yeniden birleşir. Pınar akandır ve akan da pınardır. Tufanda suyun bir yüzü azap, bir yüzü kurtuluştu. Bu ikilik surede beşinci ayetin pınarıyla on ikinci ayetin pınarı arasında bölünür. Bahçedeki pınar boğan bir su değildir. O, tufanda gemiye ait olan korunmuş akışın kendisidir.

## İzden sonra kendisi

[¶19] Göz kelimesi bir şeyi doğrudan, yüz yüze görmeyi de anlatır. Bir kimse artık dolaylı bir işarete ihtiyaç duymadığını söylemek istediğinde şöyle derdi: {ar:لا أطلب أثرا بعد عين أي بعد معاينة, tr:lâ atlubu eseran ba'de aynin ey ba'de muâyene, gloss:gözle gördükten sonra iz aramam, source:"ع ي ن,B002"}. Aynı kelime bir şeyin kendisini de anlatır: {ar:عين الشيء نفسه, tr:aynu'ş-şey'i nefsuh, gloss:bir şeyin aynı, onun kendisidir, source:"ع ي ن,B013"}. Türkçedeki "aynı" ve "muayene" kelimeleri bu kullanımlardan gelir. Ancak Türkçe "aynı" derken artık ne göz ne de pınar duyulur.

[¶20] Kur'an bugünkü suyu bir iz olarak gösterir. Rüzgârların bulutları kaldırdığı, yağmurun indiği ve insanların sevindiği anlatıldıktan sonra şöyle denir: {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak; ölümünden sonra yeri nasıl diriltir, source:30:50}. Ayet, bunu yapanın ölüleri de dirilteceğini söyleyerek devam eder. Surenin on yedinci ayetinden yirminci ayetine kadar yöneltilen bakış da bu izlere yöneliktir: deveye, göğe, dağlara ve yere. Bugün su yağmur olarak iner ve toprağı canlandırır, insan da onun izine bakar. Bahçedeki su ise "göz" adını taşır. Burada iz ile kendisi arasındaki fark, ayetteki kelimenin içinde duyulur. Bu, ayetin anlamı değil, kelimenin yanında duyulan bir bağdır.

[¶21] Kur'an aynı kelimeyi ahirette görmenin kesinliği için de kullanır, ama bu kez ateşin tarafında. Çokluk yarışının oyaladığı ve mezarlara varıncaya dek bu yarışı sürdürenlere şöyle denir: {ar:لَتَرَوُنَّ ٱلْجَحِيمَ, tr:le-terevunne'l-cahîm, gloss:alevli ateşi mutlaka göreceksiniz, source:102:6}; {ar:ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ, tr:summe le-terevunnehâ ayne'l-yakîn, gloss:sonra onu kesin bir gözle göreceksiniz, source:102:7}. Gâşiye'de de iki tarafın suyu aynı adla anılır. İlk ayetteki "haber", o gün iki tarafta da gözle görülen bir pınara dönüşür.

===== _commentary/v16/out/88_12/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: آنية (88:5) and يأن (57:16) and آن (55:44) share the root of "reaching its time/term"
- memory: آسن means water whose taste or smell has changed
- memory: غور means water sunk into the ground
- memory: Turkish cereyan, mecra, cari, cariye, aynı, muayene derive from these Arabic words
- not written: ج ر ي B004 young girl - only as Turkish loanword note; no support in the ayah
- not written: ج ر ي B002 habit, B003 agent/messenger, B005 crop, B007 keeping pace, B008 for your sake - no tie to a theme
- not written: ع ي ن B004 evil eye, B005 spy, B011 cash, B012 credit sale, B015 notables, B017 people present - no tie
- not written: ع ي ن B010 cloud or lasting rain from one direction - direction-specific, would add rain without the ayah
- not written: ع ي ن B014 choicest part - weak tie, would replace "spring" with praise
- not written: ع ي ن B016 wide-eyed (حور عين elsewhere) - different form, would replace the spring
- not written: 76:6 spring made to gush by the servants - belongs to the surah commentary's cup and spring scene
- not written: 18:86 sun setting in a muddy spring - would overstrain the sun resonance

===== passages not cited (218) =====
## strong (this ayah's own list) (8)

- (16:31) [listed for 88:12] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ لَهُمْ فِيهَا مَا يَشَآءُونَ ۚ كَذَٰلِكَ يَجْزِى ٱللَّهُ ٱلْمُتَّقِينَ
- (36:34) [listed for 88:12] وَجَعَلْنَا فِيهَا جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ وَفَجَّرْنَا فِيهَا مِنَ ٱلْعُيُونِ
- (37:45) [listed for 88:12] يُطَافُ عَلَيْهِم بِكَأْسٍۢ مِّن مَّعِينٍۭ
- (47:15) [listed for 88:12] [cited in ¶8] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (55:50) [listed for 88:12] [cited in ¶9] فِيهِمَا عَيْنَانِ تَجْرِيَانِ
- (76:6) [listed for 88:12] عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا
- (90:8) [listed for 88:12] أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- (102:7) [listed for 88:12] [cited in ¶21] ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ

## medium (this ayah's own list) (37)

- (2:60) [listed for 88:12] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (7:160) [listed for 88:12] وَقَطَّعْنَٰهُمُ ٱثْنَتَىْ عَشْرَةَ أَسْبَاطًا أُمَمًۭا ۚ وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ إِذِ ٱسْتَسْقَىٰهُ قَوْمُهُۥٓ أَنِ ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنۢبَجَسَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۚ وَظَلَّلْنَا عَلَيْهِمُ ٱلْغَمَٰمَ وَأَنزَلْنَا عَلَيْهِمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۚ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (13:35) [listed for 88:12] [cited in ¶11] ۞ مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ أُكُلُهَا دَآئِمٌۭ وَظِلُّهَا ۚ تِلْكَ عُقْبَى ٱلَّذِينَ ٱتَّقَوا۟ ۖ وَّعُقْبَى ٱلْكَٰفِرِينَ ٱلنَّارُ
- (15:45) [listed for 88:12] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (17:90) [listed for 88:12] وَقَالُوا۟ لَن نُّؤْمِنَ لَكَ حَتَّىٰ تَفْجُرَ لَنَا مِنَ ٱلْأَرْضِ يَنۢبُوعًا
- (17:91) [listed for 88:12] أَوْ تَكُونَ لَكَ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَعِنَبٍۢ فَتُفَجِّرَ ٱلْأَنْهَٰرَ خِلَٰلَهَا تَفْجِيرًا
- (19:26) [listed for 88:12] فَكُلِى وَٱشْرَبِى وَقَرِّى عَيْنًۭا ۖ فَإِمَّا تَرَيِنَّ مِنَ ٱلْبَشَرِ أَحَدًۭا فَقُولِىٓ إِنِّى نَذَرْتُ لِلرَّحْمَٰنِ صَوْمًۭا فَلَنْ أُكَلِّمَ ٱلْيَوْمَ إِنسِيًّۭا
- (20:76) [listed for 88:12] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
- (21:61) [listed for 88:12] قَالُوا۟ فَأْتُوا۟ بِهِۦ عَلَىٰٓ أَعْيُنِ ٱلنَّاسِ لَعَلَّهُمْ يَشْهَدُونَ
- (23:50) [listed for 88:12] [cited in ¶6] وَجَعَلْنَا ٱبْنَ مَرْيَمَ وَأُمَّهُۥٓ ءَايَةًۭ وَءَاوَيْنَٰهُمَآ إِلَىٰ رَبْوَةٍۢ ذَاتِ قَرَارٍۢ وَمَعِينٍۢ
- (26:57) [listed for 88:12] فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍۢ وَعُيُونٍۢ
- (29:58) [listed for 88:12] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (36:35) [listed for 88:12] لِيَأْكُلُوا۟ مِن ثَمَرِهِۦ وَمَا عَمِلَتْهُ أَيْدِيهِمْ ۖ أَفَلَا يَشْكُرُونَ
- (37:46) [listed for 88:12] بَيْضَآءَ لَذَّةٍۢ لِّلشَّٰرِبِينَ
- (39:5) [listed for 88:12] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ يُكَوِّرُ ٱلَّيْلَ عَلَى ٱلنَّهَارِ وَيُكَوِّرُ ٱلنَّهَارَ عَلَى ٱلَّيْلِ ۖ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّى ۗ أَلَا هُوَ ٱلْعَزِيزُ ٱلْغَفَّٰرُ
- (44:25) [listed for 88:12] كَمْ تَرَكُوا۟ مِن جَنَّٰتٍۢ وَعُيُونٍۢ
- (44:52) [listed for 88:12] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (51:15) [listed for 88:12] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (54:12) [listed for 88:12] [cited in ¶16] وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ
- (54:14) [listed for 88:12] [cited in ¶16] تَجْرِى بِأَعْيُنِنَا جَزَآءًۭ لِّمَن كَانَ كُفِرَ
- (54:37) [listed for 88:12] وَلَقَدْ رَٰوَدُوهُ عَن ضَيْفِهِۦ فَطَمَسْنَآ أَعْيُنَهُمْ فَذُوقُوا۟ عَذَابِى وَنُذُرِ
- (55:46) [listed for 88:12] وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- (55:54) [listed for 88:12] مُتَّكِـِٔينَ عَلَىٰ فُرُشٍۭ بَطَآئِنُهَا مِنْ إِسْتَبْرَقٍۢ ۚ وَجَنَى ٱلْجَنَّتَيْنِ دَانٍۢ
- (55:62) [listed for 88:12] وَمِن دُونِهِمَا جَنَّتَانِ
- (55:66) [listed for 88:12] فِيهِمَا عَيْنَانِ نَضَّاخَتَانِ
- (56:18) [listed for 88:12] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:22) [listed for 88:12] وَحُورٌ عِينٌۭ
- (67:30) [listed for 88:12] [cited in ¶5] قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ
- (69:11) [listed for 88:12] [cited in ¶17] إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ
- (76:5) [listed for 88:12] إِنَّ ٱلْأَبْرَارَ يَشْرَبُونَ مِن كَأْسٍۢ كَانَ مِزَاجُهَا كَافُورًا
- (76:12) [listed for 88:12] وَجَزَىٰهُم بِمَا صَبَرُوا۟ جَنَّةًۭ وَحَرِيرًۭا
- (76:18) [listed for 88:12] عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا
- (77:41) [listed for 88:12] إِنَّ ٱلْمُتَّقِينَ فِى ظِلَٰلٍۢ وَعُيُونٍۢ
- (83:25) [listed for 88:12] يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ
- (83:27) [listed for 88:12] وَمِزَاجُهُۥ مِن تَسْنِيمٍ
- (83:28) [listed for 88:12] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
- (85:11) [listed for 88:12] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْكَبِيرُ

## named by the passage's own list as strong for this ayah (11)

- (19:62) [listed for 88:12] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (36:55) [listed for 88:12] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (41:32) [listed for 88:12] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (51:3) [listed for 88:12] فَٱلْجَٰرِيَٰتِ يُسْرًۭا
- (54:54) [listed for 88:12] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَهَرٍۢ
- (56:12) [listed for 88:12] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (56:31) [listed for 88:12] وَمَآءٍۢ مَّسْكُوبٍۢ
- (76:21) [listed for 88:12] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:43) [listed for 88:12] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (78:34) [listed for 88:12] وَكَأْسًۭا دِهَاقًۭا
- (83:26) [listed for 88:12] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ

## named by the passage's own list as medium for this ayah (29)

- (3:15) [listed for 88:12] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (4:57) [listed for 88:12] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (9:72) [listed for 88:12] وَعَدَ ٱللَّهُ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ أَكْبَرُ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (14:32) [listed for 88:12] ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ وَسَخَّرَ لَكُمُ ٱلْفُلْكَ لِتَجْرِىَ فِى ٱلْبَحْرِ بِأَمْرِهِۦ ۖ وَسَخَّرَ لَكُمُ ٱلْأَنْهَٰرَ
- (15:48) [listed for 88:12] لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ وَمَا هُم مِّنْهَا بِمُخْرَجِينَ
- (18:33) [listed for 88:12] كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا وَلَمْ تَظْلِم مِّنْهُ شَيْـًۭٔا ۚ وَفَجَّرْنَا خِلَٰلَهُمَا نَهَرًۭا
- (18:108) [listed for 88:12] خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا
- (19:24) [listed for 88:12] فَنَادَىٰهَا مِن تَحْتِهَآ أَلَّا تَحْزَنِى قَدْ جَعَلَ رَبُّكِ تَحْتَكِ سَرِيًّۭا
- (20:119) [listed for 88:12] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (26:147) [listed for 88:12] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (37:47) [listed for 88:12] لَا فِيهَا غَوْلٌۭ وَلَا هُمْ عَنْهَا يُنزَفُونَ
- (37:62) [listed for 88:12] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (38:51) [listed for 88:12] مُتَّكِـِٔينَ فِيهَا يَدْعُونَ فِيهَا بِفَٰكِهَةٍۢ كَثِيرَةٍۢ وَشَرَابٍۢ
- (43:71) [listed for 88:12] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (44:55) [listed for 88:12] يَدْعُونَ فِيهَا بِكُلِّ فَٰكِهَةٍ ءَامِنِينَ
- (44:56) [listed for 88:12] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
- (52:18) [listed for 88:12] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (55:48) [listed for 88:12] ذَوَاتَآ أَفْنَانٍۢ
- (55:68) [listed for 88:12] فِيهِمَا فَٰكِهَةٌۭ وَنَخْلٌۭ وَرُمَّانٌۭ
- (56:15) [listed for 88:12] عَلَىٰ سُرُرٍۢ مَّوْضُونَةٍۢ
- (56:33) [listed for 88:12] لَّا مَقْطُوعَةٍۢ وَلَا مَمْنُوعَةٍۢ
- (56:34) [listed for 88:12] وَفُرُشٍۢ مَّرْفُوعَةٍ
- (56:89) [listed for 88:12] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (69:24) [listed for 88:12] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ
- (76:11) [listed for 88:12] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (76:13) [listed for 88:12] [cited in ¶15] مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۖ لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا
- (78:24) [listed for 88:12] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (83:22) [listed for 88:12] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (101:7) [listed for 88:12] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## weak (this ayah's own list) (64)

- (2:25) [listed for 88:12] [cited in ¶9] وَبَشِّرِ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ كُلَّمَا رُزِقُوا۟ مِنْهَا مِن ثَمَرَةٍۢ رِّزْقًۭا ۙ قَالُوا۟ هَٰذَا ٱلَّذِى رُزِقْنَا مِن قَبْلُ ۖ وَأُتُوا۟ بِهِۦ مُتَشَٰبِهًۭا ۖ وَلَهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَهُمْ فِيهَا خَٰلِدُونَ
- (2:266) [listed for 88:12] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (3:72) [listed for 88:12] وَقَالَت طَّآئِفَةٌۭ مِّنْ أَهْلِ ٱلْكِتَٰبِ ءَامِنُوا۟ بِٱلَّذِىٓ أُنزِلَ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَجْهَ ٱلنَّهَارِ وَٱكْفُرُوٓا۟ ءَاخِرَهُۥ لَعَلَّهُمْ يَرْجِعُونَ
- (3:136) [listed for 88:12] أُو۟لَٰٓئِكَ جَزَآؤُهُم مَّغْفِرَةٌۭ مِّن رَّبِّهِمْ وَجَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (3:195) [listed for 88:12] فَٱسْتَجَابَ لَهُمْ رَبُّهُمْ أَنِّى لَآ أُضِيعُ عَمَلَ عَٰمِلٍۢ مِّنكُم مِّن ذَكَرٍ أَوْ أُنثَىٰ ۖ بَعْضُكُم مِّنۢ بَعْضٍۢ ۖ فَٱلَّذِينَ هَاجَرُوا۟ وَأُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأُوذُوا۟ فِى سَبِيلِى وَقَٰتَلُوا۟ وَقُتِلُوا۟ لَأُكَفِّرَنَّ عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأُدْخِلَنَّهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ثَوَابًۭا مِّنْ عِندِ ٱللَّهِ ۗ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلثَّوَابِ
- (4:13) [listed for 88:12] تِلْكَ حُدُودُ ٱللَّهِ ۚ وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (4:122) [listed for 88:12] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ وَعْدَ ٱللَّهِ حَقًّۭا ۚ وَمَنْ أَصْدَقُ مِنَ ٱللَّهِ قِيلًۭا
- (5:12) [listed for 88:12] ۞ وَلَقَدْ أَخَذَ ٱللَّهُ مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ وَبَعَثْنَا مِنْهُمُ ٱثْنَىْ عَشَرَ نَقِيبًۭا ۖ وَقَالَ ٱللَّهُ إِنِّى مَعَكُمْ ۖ لَئِنْ أَقَمْتُمُ ٱلصَّلَوٰةَ وَءَاتَيْتُمُ ٱلزَّكَوٰةَ وَءَامَنتُم بِرُسُلِى وَعَزَّرْتُمُوهُمْ وَأَقْرَضْتُمُ ٱللَّهَ قَرْضًا حَسَنًۭا لَّأُكَفِّرَنَّ عَنكُمْ سَيِّـَٔاتِكُمْ وَلَأُدْخِلَنَّكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ فَمَن كَفَرَ بَعْدَ ذَٰلِكَ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (5:65) [listed for 88:12] وَلَوْ أَنَّ أَهْلَ ٱلْكِتَٰبِ ءَامَنُوا۟ وَٱتَّقَوْا۟ لَكَفَّرْنَا عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأَدْخَلْنَٰهُمْ جَنَّٰتِ ٱلنَّعِيمِ
- (5:85) [listed for 88:12] فَأَثَٰبَهُمُ ٱللَّهُ بِمَا قَالُوا۟ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ ٱلْمُحْسِنِينَ
- (5:119) [listed for 88:12] قَالَ ٱللَّهُ هَٰذَا يَوْمُ يَنفَعُ ٱلصَّٰدِقِينَ صِدْقُهُمْ ۚ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (7:116) [listed for 88:12] قَالَ أَلْقُوا۟ ۖ فَلَمَّآ أَلْقَوْا۟ سَحَرُوٓا۟ أَعْيُنَ ٱلنَّاسِ وَٱسْتَرْهَبُوهُمْ وَجَآءُو بِسِحْرٍ عَظِيمٍۢ
- (9:21) [listed for 88:12] يُبَشِّرُهُمْ رَبُّهُم بِرَحْمَةٍۢ مِّنْهُ وَرِضْوَٰنٍۢ وَجَنَّٰتٍۢ لَّهُمْ فِيهَا نَعِيمٌۭ مُّقِيمٌ
- (9:89) [listed for 88:12] أَعَدَّ ٱللَّهُ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (9:100) [listed for 88:12] وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم بِإِحْسَٰنٍۢ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (10:9) [listed for 88:12] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ يَهْدِيهِمْ رَبُّهُم بِإِيمَٰنِهِمْ ۖ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (11:41) [listed for 88:12] ۞ وَقَالَ ٱرْكَبُوا۟ فِيهَا بِسْمِ ٱللَّهِ مَجْر۪ىٰهَا وَمُرْسَىٰهَآ ۚ إِنَّ رَبِّى لَغَفُورٌۭ رَّحِيمٌۭ
- (12:84) [listed for 88:12] وَتَوَلَّىٰ عَنْهُمْ وَقَالَ يَٰٓأَسَفَىٰ عَلَىٰ يُوسُفَ وَٱبْيَضَّتْ عَيْنَاهُ مِنَ ٱلْحُزْنِ فَهُوَ كَظِيمٌۭ
- (14:23) [listed for 88:12] وَأُدْخِلَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا بِإِذْنِ رَبِّهِمْ ۖ تَحِيَّتُهُمْ فِيهَا سَلَٰمٌ
- (15:88) [listed for 88:12] لَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ وَلَا تَحْزَنْ عَلَيْهِمْ وَٱخْفِضْ جَنَاحَكَ لِلْمُؤْمِنِينَ
- (18:31) [listed for 88:12] أُو۟لَٰٓئِكَ لَهُمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَيَلْبَسُونَ ثِيَابًا خُضْرًۭا مِّن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًۭا
- (18:86) [listed for 88:12] حَتَّىٰٓ إِذَا بَلَغَ مَغْرِبَ ٱلشَّمْسِ وَجَدَهَا تَغْرُبُ فِى عَيْنٍ حَمِئَةٍۢ وَوَجَدَ عِندَهَا قَوْمًۭا ۗ قُلْنَا يَٰذَا ٱلْقَرْنَيْنِ إِمَّآ أَن تُعَذِّبَ وَإِمَّآ أَن تَتَّخِذَ فِيهِمْ حُسْنًۭا
- (19:61) [listed for 88:12] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (20:131) [listed for 88:12] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
- (21:81) [listed for 88:12] وَلِسُلَيْمَٰنَ ٱلرِّيحَ عَاصِفَةًۭ تَجْرِى بِأَمْرِهِۦٓ إِلَى ٱلْأَرْضِ ٱلَّتِى بَٰرَكْنَا فِيهَا ۚ وَكُنَّا بِكُلِّ شَىْءٍ عَٰلِمِينَ
- (22:14) [listed for 88:12] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ إِنَّ ٱللَّهَ يَفْعَلُ مَا يُرِيدُ
- (22:23) [listed for 88:12] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَلُؤْلُؤًۭا ۖ وَلِبَاسُهُمْ فِيهَا حَرِيرٌۭ
- (25:10) [listed for 88:12] تَبَارَكَ ٱلَّذِىٓ إِن شَآءَ جَعَلَ لَكَ خَيْرًۭا مِّن ذَٰلِكَ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَيَجْعَل لَّكَ قُصُورًۢا
- (26:134) [listed for 88:12] وَجَنَّٰتٍۢ وَعُيُونٍ
- (28:9) [listed for 88:12] وَقَالَتِ ٱمْرَأَتُ فِرْعَوْنَ قُرَّتُ عَيْنٍۢ لِّى وَلَكَ ۖ لَا تَقْتُلُوهُ عَسَىٰٓ أَن يَنفَعَنَآ أَوْ نَتَّخِذَهُۥ وَلَدًۭا وَهُمْ لَا يَشْعُرُونَ
- (30:46) [listed for 88:12] وَمِنْ ءَايَٰتِهِۦٓ أَن يُرْسِلَ ٱلرِّيَاحَ مُبَشِّرَٰتٍۢ وَلِيُذِيقَكُم مِّن رَّحْمَتِهِۦ وَلِتَجْرِىَ ٱلْفُلْكُ بِأَمْرِهِۦ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- (31:29) [listed for 88:12] أَلَمْ تَرَ أَنَّ ٱللَّهَ يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ كُلٌّۭ يَجْرِىٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى وَأَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (31:31) [listed for 88:12] أَلَمْ تَرَ أَنَّ ٱلْفُلْكَ تَجْرِى فِى ٱلْبَحْرِ بِنِعْمَتِ ٱللَّهِ لِيُرِيَكُم مِّنْ ءَايَٰتِهِۦٓ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (34:12) [listed for 88:12] وَلِسُلَيْمَٰنَ ٱلرِّيحَ غُدُوُّهَا شَهْرٌۭ وَرَوَاحُهَا شَهْرٌۭ ۖ وَأَسَلْنَا لَهُۥ عَيْنَ ٱلْقِطْرِ ۖ وَمِنَ ٱلْجِنِّ مَن يَعْمَلُ بَيْنَ يَدَيْهِ بِإِذْنِ رَبِّهِۦ ۖ وَمَن يَزِغْ مِنْهُمْ عَنْ أَمْرِنَا نُذِقْهُ مِنْ عَذَابِ ٱلسَّعِيرِ
- (36:66) [listed for 88:12] وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ
- (37:48) [listed for 88:12] وَعِندَهُمْ قَٰصِرَٰتُ ٱلطَّرْفِ عِينٌۭ
- (39:20) [listed for 88:12] لَٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ غُرَفٌۭ مِّن فَوْقِهَا غُرَفٌۭ مَّبْنِيَّةٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ ٱلْمِيعَادَ
- (44:54) [listed for 88:12] كَذَٰلِكَ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (45:12) [listed for 88:12] ۞ ٱللَّهُ ٱلَّذِى سَخَّرَ لَكُمُ ٱلْبَحْرَ لِتَجْرِىَ ٱلْفُلْكُ فِيهِ بِأَمْرِهِۦ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- (47:12) [listed for 88:12] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
- (48:5) [listed for 88:12] لِّيُدْخِلَ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَيُكَفِّرَ عَنْهُمْ سَيِّـَٔاتِهِمْ ۚ وَكَانَ ذَٰلِكَ عِندَ ٱللَّهِ فَوْزًا عَظِيمًۭا
- (48:17) [listed for 88:12] لَّيْسَ عَلَى ٱلْأَعْمَىٰ حَرَجٌۭ وَلَا عَلَى ٱلْأَعْرَجِ حَرَجٌۭ وَلَا عَلَى ٱلْمَرِيضِ حَرَجٌۭ ۗ وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَمَن يَتَوَلَّ يُعَذِّبْهُ عَذَابًا أَلِيمًۭا
- (52:20) [listed for 88:12] مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ ۖ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (52:37) [listed for 88:12] أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ
- (54:39) [listed for 88:12] فَذُوقُوا۟ عَذَابِى وَنُذُرِ
- (55:24) [listed for 88:12] وَلَهُ ٱلْجَوَارِ ٱلْمُنشَـَٔاتُ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ
- (55:64) [listed for 88:12] مُدْهَآمَّتَانِ
- (55:70) [listed for 88:12] فِيهِنَّ خَيْرَٰتٌ حِسَانٌۭ
- (56:17) [listed for 88:12] يَطُوفُ عَلَيْهِمْ وِلْدَٰنٌۭ مُّخَلَّدُونَ
- (56:19) [listed for 88:12] لَّا يُصَدَّعُونَ عَنْهَا وَلَا يُنزِفُونَ
- (57:12) [listed for 88:12] يَوْمَ تَرَى ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ يَسْعَىٰ نُورُهُم بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِم بُشْرَىٰكُمُ ٱلْيَوْمَ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (58:22) [listed for 88:12] لَّا تَجِدُ قَوْمًۭا يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ يُوَآدُّونَ مَنْ حَآدَّ ٱللَّهَ وَرَسُولَهُۥ وَلَوْ كَانُوٓا۟ ءَابَآءَهُمْ أَوْ أَبْنَآءَهُمْ أَوْ إِخْوَٰنَهُمْ أَوْ عَشِيرَتَهُمْ ۚ أُو۟لَٰٓئِكَ كَتَبَ فِى قُلُوبِهِمُ ٱلْإِيمَٰنَ وَأَيَّدَهُم بِرُوحٍۢ مِّنْهُ ۖ وَيُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ رَضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱللَّهِ ۚ أَلَآ إِنَّ حِزْبَ ٱللَّهِ هُمُ ٱلْمُفْلِحُونَ
- (61:12) [listed for 88:12] يَغْفِرْ لَكُمْ ذُنُوبَكُمْ وَيُدْخِلْكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (64:9) [listed for 88:12] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (65:11) [listed for 88:12] رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
- (66:8) [listed for 88:12] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (76:15) [listed for 88:12] وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠
- (77:27) [listed for 88:12] وَجَعَلْنَا فِيهَا رَوَٰسِىَ شَٰمِخَٰتٍۢ وَأَسْقَيْنَٰكُم مَّآءًۭ فُرَاتًۭا
- (81:16) [listed for 88:12] ٱلْجَوَارِ ٱلْكُنَّسِ
- (83:23) [listed for 88:12] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ
- (90:7) [listed for 88:12] أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- (92:1) [listed for 88:12] وَٱلَّيْلِ إِذَا يَغْشَىٰ
- (92:20) [listed for 88:12] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (98:8) [listed for 88:12] جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

## named by the passage's own list as weak for this ayah (9)

- (10:26) [listed for 88:12] ۞ لِّلَّذِينَ أَحْسَنُوا۟ ٱلْحُسْنَىٰ وَزِيَادَةٌۭ ۖ وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (26:7) [listed for 88:12] أَوَلَمْ يَرَوْا۟ إِلَى ٱلْأَرْضِ كَمْ أَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ
- (37:42) [listed for 88:12] فَوَٰكِهُ ۖ وَهُم مُّكْرَمُونَ
- (37:49) [listed for 88:12] كَأَنَّهُنَّ بَيْضٌۭ مَّكْنُونٌۭ
- (38:42) [listed for 88:12] ٱرْكُضْ بِرِجْلِكَ ۖ هَٰذَا مُغْتَسَلٌۢ بَارِدٌۭ وَشَرَابٌۭ
- (42:32) [listed for 88:12] وَمِنْ ءَايَٰتِهِ ٱلْجَوَارِ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ
- (50:35) [listed for 88:12] لَهُم مَّا يَشَآءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌۭ
- (78:23) [listed for 88:12] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (79:31) [listed for 88:12] أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا

## neighbours: within two ayat of a passage the commentary cites (60)

- (2:23) [next to 2:25] وَإِن كُنتُمْ فِى رَيْبٍۢ مِّمَّا نَزَّلْنَا عَلَىٰ عَبْدِنَا فَأْتُوا۟ بِسُورَةٍۢ مِّن مِّثْلِهِۦ وَٱدْعُوا۟ شُهَدَآءَكُم مِّن دُونِ ٱللَّهِ إِن كُنتُمْ صَٰدِقِينَ
- (2:24) [next to 2:25] فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ ۖ أُعِدَّتْ لِلْكَٰفِرِينَ
- (2:26) [next to 2:25] ۞ إِنَّ ٱللَّهَ لَا يَسْتَحْىِۦٓ أَن يَضْرِبَ مَثَلًۭا مَّا بَعُوضَةًۭ فَمَا فَوْقَهَا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۖ وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَيَقُولُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۘ يُضِلُّ بِهِۦ كَثِيرًۭا وَيَهْدِى بِهِۦ كَثِيرًۭا ۚ وَمَا يُضِلُّ بِهِۦٓ إِلَّا ٱلْفَٰسِقِينَ
- (2:27) [next to 2:25] ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيُفْسِدُونَ فِى ٱلْأَرْضِ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (5:81) [next to 5:83] وَلَوْ كَانُوا۟ يُؤْمِنُونَ بِٱللَّهِ وَٱلنَّبِىِّ وَمَآ أُنزِلَ إِلَيْهِ مَا ٱتَّخَذُوهُمْ أَوْلِيَآءَ وَلَٰكِنَّ كَثِيرًۭا مِّنْهُمْ فَٰسِقُونَ
- (5:82) [next to 5:83] ۞ لَتَجِدَنَّ أَشَدَّ ٱلنَّاسِ عَدَٰوَةًۭ لِّلَّذِينَ ءَامَنُوا۟ ٱلْيَهُودَ وَٱلَّذِينَ أَشْرَكُوا۟ ۖ وَلَتَجِدَنَّ أَقْرَبَهُم مَّوَدَّةًۭ لِّلَّذِينَ ءَامَنُوا۟ ٱلَّذِينَ قَالُوٓا۟ إِنَّا نَصَٰرَىٰ ۚ ذَٰلِكَ بِأَنَّ مِنْهُمْ قِسِّيسِينَ وَرُهْبَانًۭا وَأَنَّهُمْ لَا يَسْتَكْبِرُونَ
- (5:84) [next to 5:83] وَمَا لَنَا لَا نُؤْمِنُ بِٱللَّهِ وَمَا جَآءَنَا مِنَ ٱلْحَقِّ وَنَطْمَعُ أَن يُدْخِلَنَا رَبُّنَا مَعَ ٱلْقَوْمِ ٱلصَّٰلِحِينَ
- (12:17) [next to 12:19] قَالُوا۟ يَٰٓأَبَانَآ إِنَّا ذَهَبْنَا نَسْتَبِقُ وَتَرَكْنَا يُوسُفَ عِندَ مَتَٰعِنَا فَأَكَلَهُ ٱلذِّئْبُ ۖ وَمَآ أَنتَ بِمُؤْمِنٍۢ لَّنَا وَلَوْ كُنَّا صَٰدِقِينَ
- (12:18) [next to 12:19] وَجَآءُو عَلَىٰ قَمِيصِهِۦ بِدَمٍۢ كَذِبٍۢ ۚ قَالَ بَلْ سَوَّلَتْ لَكُمْ أَنفُسُكُمْ أَمْرًۭا ۖ فَصَبْرٌۭ جَمِيلٌۭ ۖ وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (12:20) [next to 12:19] وَشَرَوْهُ بِثَمَنٍۭ بَخْسٍۢ دَرَٰهِمَ مَعْدُودَةٍۢ وَكَانُوا۟ فِيهِ مِنَ ٱلزَّٰهِدِينَ
- (12:21) [next to 12:19] وَقَالَ ٱلَّذِى ٱشْتَرَىٰهُ مِن مِّصْرَ لِٱمْرَأَتِهِۦٓ أَكْرِمِى مَثْوَىٰهُ عَسَىٰٓ أَن يَنفَعَنَآ أَوْ نَتَّخِذَهُۥ وَلَدًۭا ۚ وَكَذَٰلِكَ مَكَّنَّا لِيُوسُفَ فِى ٱلْأَرْضِ وَلِنُعَلِّمَهُۥ مِن تَأْوِيلِ ٱلْأَحَادِيثِ ۚ وَٱللَّهُ غَالِبٌ عَلَىٰٓ أَمْرِهِۦ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (13:0) [next to 13:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (13:1) [next to 13:2] الٓمٓر ۚ تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ۗ وَٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (13:3) [next to 13:2] وَهُوَ ٱلَّذِى مَدَّ ٱلْأَرْضَ وَجَعَلَ فِيهَا رَوَٰسِىَ وَأَنْهَٰرًۭا ۖ وَمِن كُلِّ ٱلثَّمَرَٰتِ جَعَلَ فِيهَا زَوْجَيْنِ ٱثْنَيْنِ ۖ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (13:4) [next to 13:2] وَفِى ٱلْأَرْضِ قِطَعٌۭ مُّتَجَٰوِرَٰتٌۭ وَجَنَّٰتٌۭ مِّنْ أَعْنَٰبٍۢ وَزَرْعٌۭ وَنَخِيلٌۭ صِنْوَانٌۭ وَغَيْرُ صِنْوَانٍۢ يُسْقَىٰ بِمَآءٍۢ وَٰحِدٍۢ وَنُفَضِّلُ بَعْضَهَا عَلَىٰ بَعْضٍۢ فِى ٱلْأُكُلِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (13:33) [next to 13:35] أَفَمَنْ هُوَ قَآئِمٌ عَلَىٰ كُلِّ نَفْسٍۭ بِمَا كَسَبَتْ ۗ وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ قُلْ سَمُّوهُمْ ۚ أَمْ تُنَبِّـُٔونَهُۥ بِمَا لَا يَعْلَمُ فِى ٱلْأَرْضِ أَم بِظَٰهِرٍۢ مِّنَ ٱلْقَوْلِ ۗ بَلْ زُيِّنَ لِلَّذِينَ كَفَرُوا۟ مَكْرُهُمْ وَصُدُّوا۟ عَنِ ٱلسَّبِيلِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (13:34) [next to 13:35] لَّهُمْ عَذَابٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَقُّ ۖ وَمَا لَهُم مِّنَ ٱللَّهِ مِن وَاقٍۢ
- (13:36) [next to 13:35] وَٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَفْرَحُونَ بِمَآ أُنزِلَ إِلَيْكَ ۖ وَمِنَ ٱلْأَحْزَابِ مَن يُنكِرُ بَعْضَهُۥ ۚ قُلْ إِنَّمَآ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ وَلَآ أُشْرِكَ بِهِۦٓ ۚ إِلَيْهِ أَدْعُوا۟ وَإِلَيْهِ مَـَٔابِ
- (13:37) [next to 13:35] وَكَذَٰلِكَ أَنزَلْنَٰهُ حُكْمًا عَرَبِيًّۭا ۚ وَلَئِنِ ٱتَّبَعْتَ أَهْوَآءَهُم بَعْدَمَا جَآءَكَ مِنَ ٱلْعِلْمِ مَا لَكَ مِنَ ٱللَّهِ مِن وَلِىٍّۢ وَلَا وَاقٍۢ
- (23:48) [next to 23:50] فَكَذَّبُوهُمَا فَكَانُوا۟ مِنَ ٱلْمُهْلَكِينَ
- (23:49) [next to 23:50] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ لَعَلَّهُمْ يَهْتَدُونَ
- (23:51) [next to 23:50] يَٰٓأَيُّهَا ٱلرُّسُلُ كُلُوا۟ مِنَ ٱلطَّيِّبَٰتِ وَٱعْمَلُوا۟ صَٰلِحًا ۖ إِنِّى بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (23:52) [next to 23:50] وَإِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةًۭ وَٰحِدَةًۭ وَأَنَا۠ رَبُّكُمْ فَٱتَّقُونِ
- (30:48) [next to 30:50] ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَيَبْسُطُهُۥ فِى ٱلسَّمَآءِ كَيْفَ يَشَآءُ وَيَجْعَلُهُۥ كِسَفًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ ۖ فَإِذَآ أَصَابَ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
- (30:49) [next to 30:50] وَإِن كَانُوا۟ مِن قَبْلِ أَن يُنَزَّلَ عَلَيْهِم مِّن قَبْلِهِۦ لَمُبْلِسِينَ
- (30:51) [next to 30:50] وَلَئِنْ أَرْسَلْنَا رِيحًۭا فَرَأَوْهُ مُصْفَرًّۭا لَّظَلُّوا۟ مِنۢ بَعْدِهِۦ يَكْفُرُونَ
- (30:52) [next to 30:50] فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (36:36) [next to 36:38] سُبْحَٰنَ ٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ وَمِنْ أَنفُسِهِمْ وَمِمَّا لَا يَعْلَمُونَ
- (36:37) [next to 36:38] وَءَايَةٌۭ لَّهُمُ ٱلَّيْلُ نَسْلَخُ مِنْهُ ٱلنَّهَارَ فَإِذَا هُم مُّظْلِمُونَ
- (36:39) [next to 36:38] وَٱلْقَمَرَ قَدَّرْنَٰهُ مَنَازِلَ حَتَّىٰ عَادَ كَٱلْعُرْجُونِ ٱلْقَدِيمِ
- (36:40) [next to 36:38] لَا ٱلشَّمْسُ يَنۢبَغِى لَهَآ أَن تُدْرِكَ ٱلْقَمَرَ وَلَا ٱلَّيْلُ سَابِقُ ٱلنَّهَارِ ۚ وَكُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ
- (38:52) [next to 38:54] ۞ وَعِندَهُمْ قَٰصِرَٰتُ ٱلطَّرْفِ أَتْرَابٌ
- (38:53) [next to 38:54] هَٰذَا مَا تُوعَدُونَ لِيَوْمِ ٱلْحِسَابِ
- (38:55) [next to 38:54] هَٰذَا ۚ وَإِنَّ لِلطَّٰغِينَ لَشَرَّ مَـَٔابٍۢ
- (38:56) [next to 38:54] جَهَنَّمَ يَصْلَوْنَهَا فَبِئْسَ ٱلْمِهَادُ
- (47:13) [next to 47:15] وَكَأَيِّن مِّن قَرْيَةٍ هِىَ أَشَدُّ قُوَّةًۭ مِّن قَرْيَتِكَ ٱلَّتِىٓ أَخْرَجَتْكَ أَهْلَكْنَٰهُمْ فَلَا نَاصِرَ لَهُمْ
- (47:14) [next to 47:15] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ كَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُم
- (47:16) [next to 47:15] وَمِنْهُم مَّن يَسْتَمِعُ إِلَيْكَ حَتَّىٰٓ إِذَا خَرَجُوا۟ مِنْ عِندِكَ قَالُوا۟ لِلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مَاذَا قَالَ ءَانِفًا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ طَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُمْ
- (47:17) [next to 47:15] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
- (54:10) [next to 54:12] فَدَعَا رَبَّهُۥٓ أَنِّى مَغْلُوبٌۭ فَٱنتَصِرْ
- (54:11) [next to 54:12] فَفَتَحْنَآ أَبْوَٰبَ ٱلسَّمَآءِ بِمَآءٍۢ مُّنْهَمِرٍۢ
- (54:15) [next to 54:13] وَلَقَد تَّرَكْنَٰهَآ ءَايَةًۭ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:16) [next to 54:14] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (55:49) [next to 55:50] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:51) [next to 55:50] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:52) [next to 55:50] فِيهِمَا مِن كُلِّ فَٰكِهَةٍۢ زَوْجَانِ
- (57:14) [next to 57:16] يُنَادُونَهُمْ أَلَمْ نَكُن مَّعَكُمْ ۖ قَالُوا۟ بَلَىٰ وَلَٰكِنَّكُمْ فَتَنتُمْ أَنفُسَكُمْ وَتَرَبَّصْتُمْ وَٱرْتَبْتُمْ وَغَرَّتْكُمُ ٱلْأَمَانِىُّ حَتَّىٰ جَآءَ أَمْرُ ٱللَّهِ وَغَرَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (57:15) [next to 57:16] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (57:17) [next to 57:16] ٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَعْقِلُونَ
- (57:18) [next to 57:16] إِنَّ ٱلْمُصَّدِّقِينَ وَٱلْمُصَّدِّقَٰتِ وَأَقْرَضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا يُضَٰعَفُ لَهُمْ وَلَهُمْ أَجْرٌۭ كَرِيمٌۭ
- (67:28) [next to 67:30] قُلْ أَرَءَيْتُمْ إِنْ أَهْلَكَنِىَ ٱللَّهُ وَمَن مَّعِىَ أَوْ رَحِمَنَا فَمَن يُجِيرُ ٱلْكَٰفِرِينَ مِنْ عَذَابٍ أَلِيمٍۢ
- (67:29) [next to 67:30] قُلْ هُوَ ٱلرَّحْمَٰنُ ءَامَنَّا بِهِۦ وَعَلَيْهِ تَوَكَّلْنَا ۖ فَسَتَعْلَمُونَ مَنْ هُوَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (69:9) [next to 69:11] وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ
- (69:10) [next to 69:11] فَعَصَوْا۟ رَسُولَ رَبِّهِمْ فَأَخَذَهُمْ أَخْذَةًۭ رَّابِيَةً
- (69:12) [next to 69:11] لِنَجْعَلَهَا لَكُمْ تَذْكِرَةًۭ وَتَعِيَهَآ أُذُنٌۭ وَٰعِيَةٌۭ
- (69:13) [next to 69:11] فَإِذَا نُفِخَ فِى ٱلصُّورِ نَفْخَةٌۭ وَٰحِدَةٌۭ
- (76:14) [next to 76:13] وَدَانِيَةً عَلَيْهِمْ ظِلَٰلُهَا وَذُلِّلَتْ قُطُوفُهَا تَذْلِيلًۭا
- (102:4) [next to 102:6] ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
- (102:5) [next to 102:6] كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
- (102:8) [next to 102:6] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

