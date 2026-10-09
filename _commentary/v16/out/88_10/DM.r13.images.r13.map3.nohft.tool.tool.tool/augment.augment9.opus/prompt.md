Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:10; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_10/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_10.reading.tr.md (prose paragraphs numbered) =====
## Fiilsiz bir cümle: bahçenin içinde

[¶1] Onuncu ayet tek başına duran bir cümle değildir. Sekizinci ayette başlayan cümlenin üçüncü halkasıdır. Önce yüzler gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşacık ve parlaktır, source:88:8}. Sonra yüzlerin içi: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabalarından hoşnuttur, source:88:9}. En sonunda yerleri: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçededir, source:88:10}. Böylece üç şey söylenmiş olur: bu yüzler nasıl görünür, ne hisseder ve nerededir. Üçünde de fiil yoktur. Surenin ilk yarısındaki yüzler içinse cümleler fiillerle kurulur: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:tasla nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}; {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir kaynaktan içirilir, source:88:5}. Bunlar o yüzlerin başına gelen işlerdir ve ikincisi edilgendir: Suyu onlar içmez, onlara içirilir. Bahçedeki yüzlerin başına gelen bir iş anlatılmaz. Onlar için yalnızca bir "içinde" vardır. Ayet bir olay anlatmaz, bir yerleşmeyi anlatır.

[¶2] Yapı iki yarıyı birbirine ayna yapar. Dördüncü ayette belirsiz bir ad ve onun sıfatı vardır: kızgın bir ateş. Onuncu ayette de belirsiz bir ad ve sıfatı vardır: yüksek bir bahçe. İki sıfat aynı kalıptadır ve aynı sesle biter. Biri ısıyı söyler, öteki yüksekliği. "Bir bahçe" denmesi, yeri tanıtılmış bir yer olarak değil, henüz görülmemiş bir yer olarak getirir.

[¶3] Bu bahçe arkasından gelen ayetlerin hepsinin çerçevesidir. On birinci ayetten itibaren üç kez söylenen "orada" kelimesi bu bahçeye döner: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmau fîhâ lâğiye, gloss:orada boş bir söz işitmezsin, source:88:11}; {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir kaynak vardır, source:88:12}; {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada yükseltilmiş sedirler vardır, source:88:13}. Kaynak, sedirler, kadehler, yastıklar ve halılar bu ayetin açtığı yerin içine yerleştirilir. Onuncu ayet odanın eşyasını saymaz. Odanın duvarlarını çizer.

## Ağaçların örttüğü yer

[¶4] Arapçada cennet önce gözle görülen bir şeydir: ağaçları toprağı örten bir bahçe. Bu ad için şöyle denirdi: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü büstânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bostan, source:"ج ن ن,B003"}. Araplar hurmalığa da aynı adı verirdi: {ar:العرب تسمي النخيل جنة, tr:el-arabu tusemmi'n-nahîle cenneh, gloss:Araplar hurma ağaçlarına cennet der, source:"ج ن ن,B003"}. Kelimenin dayandığı temel iş örtmek ve örtünmektir: {ar:الجيم والنون أصل واحد وهو الستر والتستر, tr:el-cîmu ve'n-nûnu aslun vâhidun ve huve's-setru ve't-teserrur, gloss:cim ve nun tek bir köktür, o da örtmek ve örtünmektir, source:"ج ن ن,B001"}. Bu yazı boyunca kelime ailelerinden gelen resimler ayetteki anlamın yerine geçmez, onun yanında duyulur. Burada cennet o yüzlerin içinde bulunduğu ödül yurdudur. Örtü resmi yalnızca bu yurdun adının neyi taşıdığını gösterir.

[¶5] Örten bir bahçe şöyle işler: Ağaçların tepeleri birbirine değer, güneş toprağa ancak yaprakların arasından süzülerek iner. Altta gölge, nem ve serinlik kalır. İçeride yürüyen dışarıdan görünmez. Bu örtü dışarıdan getirilip atılmaz, bahçenin kendi büyümesiyle oluşur. Aynı harfler bitkinin bu büyüyüşünü de adlandırır. Ot boy atıp sarmaş dolaş olunca ve çiçeğe durunca şöyle derlerdi: {ar:جن النبت جنونا أي طال والتف وخرج زهره, tr:cenne'n-nebtu cunûnen ey tâle ve'lteffe ve harace zehruhû, gloss:bitki boy attı, sarmaş dolaş oldu ve çiçeğini çıkardı, source:"ج ن ن,B011"}. Kur'an bahçeleri tam bu sıklıkla anar. Nebe suresinde Allah yarattıklarını sayar ve yüklü bulutlardan bol su indirip onunla tane ve bitki çıkardığını söyler {source:78:15}. Arkasından şu gelir: {ar:وَجَنَّٰتٍ أَلْفَافًا, tr:ve cennâtin elfâfâ, gloss:ve birbirine sarılmış bahçeler, source:78:16}. Bahçenin örtüsü canlıdır, sarılmış dallardan örülür.

[¶6] Surenin ilk ayetindeki Gâşiye, üstüne gelip örten gün, yukarıdan inen bir örtüdür. Onuncu ayetteki bahçe ise aşağıdan, kendi ağaçlarından yükselen bir örtüdür. Sure bu iki örtüyü karşı karşıya koyar.

[¶7] Örtünün bir yüzü de bugüne bakar. Ödül yurdunun adı için şöyle denirdi: {ar:الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم, tr:el-cennetü mâ yasîru ileyhi'l-müslimûne fi'l-âhirati ve huve sevâbun mestûrun anhumu'l-yevm, gloss:cennet, Müslümanların ahirette varacağı ve bugün onlardan örtülü olan ödüldür, source:"ج ن ن,B004"}. Kur'an bu gizliliği açıkça söyler. Secde suresinde geceleri yataklarından kalkıp korku ve umutla Rablerine yalvaranlar ve verilen rızıktan harcayanlar anlatılır. Onlar için şöyle denir: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ, tr:fe-lâ ta'lemu nefsun mâ uhfiye lehum min kurrati a'yun, gloss:onlar için gizlenmiş göz aydınlığını hiçbir kimse bilmez, source:32:17}. Sure on üçüncü ayetten on altıncı ayete kadar bahçenin eşyasını sayar: sedir, kadeh, yastık, halı. Bunlar bilinen şeylerin adlarıdır. Yerin kendi adı ise içindekinin bir kısmını hâlâ örtülü tutar.

[¶8] Türkçede cennet yalnızca öteki dünyanın adı olmuştur. Kelimede artık bir meyve bahçesi, bir hurmalık duyulmaz. Kur'an'da ise aynı kelime bu dünyanın kaybedilebilen bahçelerini de anlatır. Kalem suresinde bir bahçenin sahipleri, ürünü sabah erkenden toplamaya yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabahleyin mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken bahçenin üstünden Rabbin katından bir dolaşan geçer {source:68:19} ve bahçe sabaha {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:biçilip kesilmiş gibi oldu, source:68:20} halinde çıkar. Kehf suresindeki iki bahçe sahibi de bahçesine girerken şöyle der: {ar:مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا, tr:mâ ezunnu en tebîde hâzihî ebedâ, gloss:bunun hiç yok olacağını sanmıyorum, source:18:35}. Sonunda bahçe {ar:وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا, tr:ve hiye hâviyetun alâ urûşihâ, gloss:çardakları üstüne çökmüş halde, source:18:42} kalır. Arap kulağı cennet kelimesini duyunca önce bir gecede yanıp çökebilen bir bahçe duyar. Onuncu ayetteki bahçeyi o bahçelerden ayıran, kelimenin kendisi değil, yanındaki sıfat ve durduğu yerdir.

## Yüksek yerdeki bahçe

[¶9] Sıfatın kökü yükselmeyi ve yukarıda olmayı anlatır: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yüceliği ve yükselmeyi gösteren tek kök, source:"ع ل و,B001"}. Bu kökten yer adları da çıkmıştır. Her dağın ya da yüksek yerin başına el-alyâ denirdi: {ar:العلياء رأس كل جبل أو شرف, tr:el-alyâu ra'su külli cebelin ev şeref, gloss:alyâ her dağın ya da yüksek yerin başıdır, source:"ع ل و,B007"}. Hicaz'ın yukarı bölgesi de aynı adla anılırdı: {ar:العالية من محال العرب من الحجاز, tr:el-âliyetu min mahâlli'l-arabi mine'l-Hicâz, gloss:Âliye Hicaz'da Arapların yurtlarından biridir, source:"ع ل و,B007"}. Evin üst katındaki odaya da bu köktan bir ad verilirdi: {ar:العلية غرفة, tr:el-ulliyyetu ğurfe, gloss:ulliyye üst kattaki odadır, source:"ع ل و,B007"}. Böylece âliye kelimesi önce bir konum olarak duyulur: yukarıda, yaylada, tepede duran bir bahçe.

[¶10] Yüksekteki bahçenin nasıl işlediğini Kur'an bir benzetmede anlatır. Bakara suresinde mallarını Allah'ın hoşnutluğunu arayarak harcayanlar şöyle anılır: {ar:ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ, tr:ibtiğâe merdâtillâh, gloss:Allah'ın hoşnutluğunu arayarak, source:2:265}. Onların durumu tepedeki bir bahçeye benzer: {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilun fe-âtet ukulehâ dı'feyn, fe-in lem yusıbhâ vâbilun fe-tall, gloss:tepedeki bir bahçe gibi; ona sağanak yağmur düşer, ürününü iki kat verir; sağanak düşmese çisenti de yeter, source:2:265}. Tepe için kullanılan kelime başka bir köktendir. Buradaki bağ kökte değil, resimdedir. Yine de işleyiş açıkça söylenir: Yukarıdaki bahçe her havadan payını alır. Bol yağmur onu boğmaz, ürününü katlar. Yağmur gelmezse ince bir nem bile ona yeter. Benzetmenin başlangıcındaki hoşnutluk kelimesi, dokuzuncu ayetteki hoşnut yüzlerle aynı köktendir. Orada hoşnutluğu arayan bir harcama vardır, burada çabasından hoşnut bir yüz.

[¶11] Bu benzetmenin iki yanında iki ayrı yüzey daha durur. Hemen önceki ayette malını gösteriş için harcayan kişi, üstünde biraz toprak bulunan pürüzsüz bir kayaya benzetilir: {ar:كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:üstünde toprak olan bir kaya gibi; sağanak düşer ve onu çıplak bırakır, source:2:264}. Aynı yağmur tepedeki bahçeye iki kat ürün verir, kayayı ise çıplak bırakır. Hemen sonraki ayette, altından ırmaklar akan bir hurma ve üzüm bahçesinin sahibi yaşlanmıştır ve çocukları güçsüzdür. Sonra şu olur: {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fahtarakat, gloss:içinde ateş bulunan bir kasırga ona çarptı ve bahçe yandı, source:2:266}. Üç ayette gökyüzünün altında üç yüzey sıralanır: çıplak kaya, katlanan tepe bahçesi ve ateşle yanan bahçe. Gâşiye suresi de ateşi ve yüksek bahçeyi iki yarıya yerleştirir. Dördüncü ayetteki ateş ile onuncu ayetteki bahçe, o üç ayetteki ateş ile tepe bahçesinin sonsuzlukta kalıcı olmuş halleridir.

[¶12] Kur'an bahçenin yüksekliğini katlarla da anlatır. Zümer suresinde Rablerinden sakınanlar için şöyle denir: {ar:لَهُمْ غُرَفٌۭ مِّن فَوْقِهَا غُرَفٌۭ مَّبْنِيَّةٌۭ, tr:lehum ğurafun min fevkıhâ ğurafun mebniyye, gloss:onlar için üstlerinde başka odalar yapılmış odalar vardır, source:39:20}. Aynı ayette bu odaların altından ırmaklar akar. Üst kattaki odanın Arapçada yükseklik kökünden bir adı olduğunu yukarıda gördük. Yüksek bahçe ile katlı odalar aynı resmi iki ayrı malzemeyle kurar. Bu ayette de akan su vardır, tıpkı on ikinci ayetteki akan kaynak gibi. Ateşin yeri ise aşağıdır. Kur'an münafıklar için şöyle der: {ar:إِنَّ ٱلْمُنَٰفِقِينَ فِى ٱلدَّرْكِ ٱلْأَسْفَلِ مِنَ ٱلنَّارِ, tr:inne'l-münâfıkîne fi'd-derki'l-esfeli mine'n-nâr, gloss:münafıklar ateşin en alt katındadır, source:4:145}. İkinci ayetteki eğik yüz ile on üçüncü ayetteki yükseltilmiş sedirler arasında kurulan alçaklık ve yükseklik karşıtlığı surenin tamamına yayılır. Onuncu ayet bu karşıtlığın yukarı ucunu bir yere, bir bahçeye bağlar.

## Yüksek, ama dalı eğik

[¶13] Aynı iki kelime Kur'an'da bir kez daha, harfi harfine geçer. Hâkka suresinde hesap günü anlatılırken kitabı sağ eline verilen kişi sevinçle seslenir: {ar:هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ, tr:hâumu'kraû kitâbiyeh, gloss:alın, kitabımı okuyun, source:69:19}. Sevincinin sebebini de söyler: {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentu ennî mulâkın hisâbiyeh, gloss:ben hesabımla karşılaşacağımı zaten düşünüyordum, source:69:20}. Arkasından onun yeri anlatılır: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:artık o hoşnut bir yaşayış içindedir, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:69:22}. İki sure aynı iskeleti paylaşır. Orada da hoşnutluk vardır ve aynı kelimeyle söylenir. Orada da hesap vardır: Gâşiye suresi {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hisâbehum, gloss:sonra onların hesabı da bize aittir, source:88:26} diye biter. Orada da karşı tarafın yemeği bir tek şeye indirilir: {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irin dışında bir yemek de yoktur, source:69:36}. Bu, altıncı ayetteki darî'in yerini tutar. Hâkka suresi yüksek bahçeyi, hesapla karşılaşacağını bilerek yaşamış birine verir. Gâşiye suresinde ise aynı bahçe çabasından hoşnut olan yüzlerin yeridir. İki ayrı söyleyiş aynı kişiyi anlatır: Hesabı bekleyerek çalışan kişi, hesap açıldığında çabasından utanmaz.

[¶14] Hâkka suresi bir adım daha atar: {ar:قُطُوفُهَا دَانِيَةٌۭ, tr:kutûfuhâ dâniye, gloss:salkımları yakındır, source:69:23}. Yükseklik çoğu zaman uzaklık demektir. Kökün kendisi de yükselip uzaklaşmayı anlatır {source:"ع ل و,B001"}. Yüksek bir bahçenin meyvesinin de ele ulaşmaması beklenirdi. Ayet bu beklentiyi bozar: Bahçe yüksektir, salkımları ise eğilmiştir. İnsan suresinde sabırlarına karşılık bahçe ve ipekle ödüllendirilenler orada koltuklara yaslanır, ne güneş ne de dondurucu soğuk görürler {source:76:13}. Sonra şöyle denir: {ar:وَدَانِيَةً عَلَيْهِمْ ظِلَٰلُهَا وَذُلِّلَتْ قُطُوفُهَا تَذْلِيلًۭا, tr:ve dâniyeten aleyhim zılâluhâ ve zullilet kutûfuhâ tezlîlâ, gloss:gölgeleri üzerlerine yakındır ve salkımları iyice boyun eğdirilmiştir, source:76:14}. Burada eğilen fiil, aşağılanmayı da anlatan bir köktendir. Ateşe sunulanlar için {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} denir. Bahçede ise boyun eğen insan değil, daldır. On dördüncü ayetteki kadehler de böyledir: Orada aşağıya konan şey, oturanlara hizmet eden kaplardır. Yüksek bahçenin yüksekliği oradakileri meyveden uzaklaştırmaz. Uzaklaştırdığı şey, ilk yarıdaki yüzleri eğen ağırlıktır.

[¶15] Yükseklik ile kayıt bir başka surede de bir araya gelir. Mutaffifîn suresinde kötülerin kitabının siccîn içinde olduğu söylendikten sonra {source:83:7} iyilerin kitabı için şöyle denir: {ar:كَلَّآ إِنَّ كِتَٰبَ ٱلْأَبْرَارِ لَفِى عِلِّيِّينَ, tr:kellâ inne kitâbe'l-ebrâri le-fî illiyyîn, gloss:hayır, iyilerin kitabı illiyyîn içindedir, source:83:18}. İlliyyîn de yükseklik kökündendir ve o çok yüksek yerin ya da kaydın adı olarak anılırdı {source:"ع ل و,B007"}. Kısa bir süre sonra o iyiler için {ar:إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ, tr:inne'l-ebrâra le-fî naîm, gloss:iyiler nimet içindedir, source:83:22} denir. Bu nimet kelimesi, sekizinci ayetteki yumuşak yüzlerin sıfatıyla aynı köktendir. Hâkka suresinde sağ eldeki kitap, Mutaffifîn suresinde yüksekte duran kitap ve Gâşiye suresinde son ayetteki hesap, hepsi aynı yere çıkar: Kayıt yüksekte durur, sahibi de yüksekte oturur.

## Verilen yükseklik, istenen yükseklik

[¶16] Yükseklik kökü yalnızca yeri değil, insanın mertebesini de anlatır. Şerefli bir adam için {ar:رجل عالي الكعب أي شريف, tr:racülün âli'l-ka'bi ey şerîf, gloss:topuğu yüksek adam, yani şerefli kişi, source:"ع ل و,B002"} derlerdi. Aynı fiil kınanan bir büyüklenmeyi de anlatır. Bir hükümdar azıp büyüklendiğinde şöyle söylenirdi: {ar:علا ملك في الأرض أي طغى وتعظم, tr:alâ melikun fi'l-ardı ey tağâ ve teazzame, gloss:bir hükümdar yeryüzünde yükseldi, yani azdı ve büyüklendi, source:"ع ل و,B003"}. Kelimenin iki yönlü olduğu açıkça söylenir: {ar:علا يقال في المحمود والمذموم, tr:alâ yukâlü fi'l-mahmûdi ve'l-mezmûm, gloss:alâ hem övülen hem kınanan için söylenir, source:"ع ل و,B003"}. Onuncu ayetteki âliye bu iki yükseklikten hangisidir? Kur'an'ın cevabı açıktır ve şaşırtıcıdır: Yüksek bahçe, yeryüzünde yükseklik istemeyenlere verilir.

[¶17] Kasas suresi Firavun'u şöyle tanıtır: {ar:إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ, tr:inne fir'avne alâ fi'l-ard, gloss:Firavun yeryüzünde büyüklendi, source:28:4}. Aynı ayet onun ne yaptığını da söyler: Halkı bölüklere ayırmış, bir kesimini ezmiş, oğullarını boğazlamıştır. Surenin sonunda Musa'nın kavminden Karun anlatılır. Karun hazinelerinin anahtarlarını güçlü bir topluluk zorla taşıyacak kadar zengindir ve kavminin üstüne süslü giysileriyle çıkar {source:28:79}. Sonu şudur: {ar:فَخَسَفْنَا بِهِۦ وَبِدَارِهِ ٱلْأَرْضَ, tr:fe-hasefnâ bihî ve bi-dârihi'l-ard, gloss:onu da evini de yere geçirdik, source:28:81}. Hemen ardından gelen ayette yükseklik kökü kendisi geçer: {ar:تِلْكَ ٱلدَّارُ ٱلْءَاخِرَةُ نَجْعَلُهَا لِلَّذِينَ لَا يُرِيدُونَ عُلُوًّۭا فِى ٱلْأَرْضِ وَلَا فَسَادًۭا, tr:tilke'd-dâru'l-âhiratu nec'aluhâ lillezîne lâ yurîdûne uluvven fi'l-ardı ve lâ fesâdâ, gloss:işte o ahiret yurdunu, yeryüzünde yükseklik ve bozgunculuk istemeyenlere veririz, source:28:83}. Karun'un evi yerin dibine batar. Öteki yurt ise yükseklik istemeyenlere verilir. Onuncu ayetteki yüksek bahçe, yeryüzündeki yükseklikten vazgeçenlerin vardığı yerdir. Bahçenin sıfatı da onların istemediği yükseklikle aynı köktendir.

[¶18] Taha suresi aynı dönüşümü tek bir sahnede gösterir. Firavun'un tarafı Musa'nın karşısına çıkacak büyücülere şöyle der: {ar:وَقَدْ أَفْلَحَ ٱلْيَوْمَ مَنِ ٱسْتَعْلَىٰ, tr:ve kad eflaha'l-yevme meni's-ta'lâ, gloss:bugün üstün gelen kurtuluşa erer, source:20:64}. Musa içinde korku duyduğunda Allah ona şöyle der: {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma, en üstün olan sensin dedik, source:20:68}. Büyücüler gerçeği görünce secdeye kapanırlar {source:20:70} ve Firavun'un tehditlerine rağmen geri dönmezler. Konuşma şöyle devam eder: {ar:فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:fe-ulâike lehumu'd-derecâtu'l-ulâ, gloss:işte onlar için en yüksek dereceler vardır, source:20:75}. Bir günlük üstünlük için gelenler secdeye eğilmiş ve en yüksek derecelere kavuşmuştur. Yükseklik kökü bu sahnede üç kez geçer: Önce istenen ve kapılmak istenen üstünlük, sonra Allah'ın verdiği üstünlük, en sonunda eğilenlere verilen yükseklik.

[¶19] Onuncu ayet bu yüksekliği dokuzuncu ayetin hemen ardına koyar: Yüzler çabalarından hoşnuttur ve yüksek bir bahçededir. Üçüncü ayetteki yüzler de çalışmış ve yorulmuştur: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsibe, gloss:çalışmış, yorgun düşmüş, source:88:3}. Ama o çaba onları yükseltmez, yere eğer. Bahçedeki yükseklik ise kapılmış bir üstünlük değildir. Hoşnutluk getiren bir çabanın vardığı yerdir. Kelime aynıdır, ama bu yükseklik bir taht gibi ele geçirilmez. Ona eğilerek varılır.

===== _commentary/v16/out/88_10/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: مرضات (2:265) and راضية (88:9) share root ر ض ي
- memory: ذُلِّلَت (76:14) and الذل (42:45) share root ذ ل ل
- memory: ألفافا (78:16) and التف share root ل ف ف (stated only as resemblance, not cited as identity)
- memory: ربوة = elevated ground/hill, root ر ب و (not ع ل و)
- memory: نعيم (83:22) and ناعمة (88:8) share root ن ع م
- memory: عالية and حامية share the fāʿila pattern
- memory: 32:16 content (rising from beds, calling Lord in fear and hope, spending) described, not quoted
- memory: 20:75 continues the magicians' speech; written neutrally ("konuşma devam eder")
- not written: ج ن ن B005–B007, B009, B012–B017 (jinn, madness, embryo, grave, snake, crowd, etc.) - would be a catalogue; no theme work here
- not written: ج ن ن B008 shield / 52:27 protection - belongs to the surah's two-covers scene; only recalled
- not written: ع ل و B006 تعال "come up" - no grounding in this ayah's themes
- not written: ع ل و B004, B005, B008–B012 (overpowering, upper side, extra load, anvil, tall camel, recovery, preposition) - no work here
- not written: Turkish âlâ/âli as loanwords - cennet chosen as the narrowed loanword

===== passages not cited (267) =====
## strong (this ayah's own list) (12)

- (15:45) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (15:46) [listed for 88:10] ٱدْخُلُوهَا بِسَلَٰمٍ ءَامِنِينَ
- (18:31) [listed for 88:10] أُو۟لَٰٓئِكَ لَهُمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَيَلْبَسُونَ ثِيَابًا خُضْرًۭا مِّن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًۭا
- (28:83) [listed for 88:10] [cited in ¶17] تِلْكَ ٱلدَّارُ ٱلْءَاخِرَةُ نَجْعَلُهَا لِلَّذِينَ لَا يُرِيدُونَ عُلُوًّۭا فِى ٱلْأَرْضِ وَلَا فَسَادًۭا ۚ وَٱلْعَٰقِبَةُ لِلْمُتَّقِينَ
- (29:58) [listed for 88:10] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (39:20) [listed for 88:10] [cited in ¶12] لَٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ غُرَفٌۭ مِّن فَوْقِهَا غُرَفٌۭ مَّبْنِيَّةٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ ٱلْمِيعَادَ
- (42:4) [listed for 88:10] لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (47:15) [listed for 88:10] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (53:15) [listed for 88:10] عِندَهَا جَنَّةُ ٱلْمَأْوَىٰٓ
- (56:15) [listed for 88:10] عَلَىٰ سُرُرٍۢ مَّوْضُونَةٍۢ
- (69:22) [listed for 88:10] [cited in ¶13] فِى جَنَّةٍ عَالِيَةٍۢ
- (78:32) [listed for 88:10] حَدَآئِقَ وَأَعْنَٰبًۭا

## medium (this ayah's own list) (86)

- (2:265) [listed for 88:10] [cited in ¶10] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
- (2:266) [listed for 88:10] [cited in ¶11] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (3:15) [listed for 88:10] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:133) [listed for 88:10] ۞ وَسَارِعُوٓا۟ إِلَىٰ مَغْفِرَةٍۢ مِّن رَّبِّكُمْ وَجَنَّةٍ عَرْضُهَا ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ أُعِدَّتْ لِلْمُتَّقِينَ
- (3:136) [listed for 88:10] أُو۟لَٰٓئِكَ جَزَآؤُهُم مَّغْفِرَةٌۭ مِّن رَّبِّهِمْ وَجَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (3:139) [listed for 88:10] وَلَا تَهِنُوا۟ وَلَا تَحْزَنُوا۟ وَأَنتُمُ ٱلْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
- (3:195) [listed for 88:10] فَٱسْتَجَابَ لَهُمْ رَبُّهُمْ أَنِّى لَآ أُضِيعُ عَمَلَ عَٰمِلٍۢ مِّنكُم مِّن ذَكَرٍ أَوْ أُنثَىٰ ۖ بَعْضُكُم مِّنۢ بَعْضٍۢ ۖ فَٱلَّذِينَ هَاجَرُوا۟ وَأُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأُوذُوا۟ فِى سَبِيلِى وَقَٰتَلُوا۟ وَقُتِلُوا۟ لَأُكَفِّرَنَّ عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأُدْخِلَنَّهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ثَوَابًۭا مِّنْ عِندِ ٱللَّهِ ۗ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلثَّوَابِ
- (3:198) [listed for 88:10] لَٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا نُزُلًۭا مِّنْ عِندِ ٱللَّهِ ۗ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ لِّلْأَبْرَارِ
- (4:13) [listed for 88:10] تِلْكَ حُدُودُ ٱللَّهِ ۚ وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (4:34) [listed for 88:10] ٱلرِّجَالُ قَوَّٰمُونَ عَلَى ٱلنِّسَآءِ بِمَا فَضَّلَ ٱللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍۢ وَبِمَآ أَنفَقُوا۟ مِنْ أَمْوَٰلِهِمْ ۚ فَٱلصَّٰلِحَٰتُ قَٰنِتَٰتٌ حَٰفِظَٰتٌۭ لِّلْغَيْبِ بِمَا حَفِظَ ٱللَّهُ ۚ وَٱلَّٰتِى تَخَافُونَ نُشُوزَهُنَّ فَعِظُوهُنَّ وَٱهْجُرُوهُنَّ فِى ٱلْمَضَاجِعِ وَٱضْرِبُوهُنَّ ۖ فَإِنْ أَطَعْنَكُمْ فَلَا تَبْغُوا۟ عَلَيْهِنَّ سَبِيلًا ۗ إِنَّ ٱللَّهَ كَانَ عَلِيًّۭا كَبِيرًۭا
- (4:57) [listed for 88:10] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (5:65) [listed for 88:10] وَلَوْ أَنَّ أَهْلَ ٱلْكِتَٰبِ ءَامَنُوا۟ وَٱتَّقَوْا۟ لَكَفَّرْنَا عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأَدْخَلْنَٰهُمْ جَنَّٰتِ ٱلنَّعِيمِ
- (5:85) [listed for 88:10] فَأَثَٰبَهُمُ ٱللَّهُ بِمَا قَالُوا۟ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ ٱلْمُحْسِنِينَ
- (9:21) [listed for 88:10] يُبَشِّرُهُمْ رَبُّهُم بِرَحْمَةٍۢ مِّنْهُ وَرِضْوَٰنٍۢ وَجَنَّٰتٍۢ لَّهُمْ فِيهَا نَعِيمٌۭ مُّقِيمٌ
- (9:40) [listed for 88:10] إِلَّا تَنصُرُوهُ فَقَدْ نَصَرَهُ ٱللَّهُ إِذْ أَخْرَجَهُ ٱلَّذِينَ كَفَرُوا۟ ثَانِىَ ٱثْنَيْنِ إِذْ هُمَا فِى ٱلْغَارِ إِذْ يَقُولُ لِصَٰحِبِهِۦ لَا تَحْزَنْ إِنَّ ٱللَّهَ مَعَنَا ۖ فَأَنزَلَ ٱللَّهُ سَكِينَتَهُۥ عَلَيْهِ وَأَيَّدَهُۥ بِجُنُودٍۢ لَّمْ تَرَوْهَا وَجَعَلَ كَلِمَةَ ٱلَّذِينَ كَفَرُوا۟ ٱلسُّفْلَىٰ ۗ وَكَلِمَةُ ٱللَّهِ هِىَ ٱلْعُلْيَا ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ
- (9:72) [listed for 88:10] وَعَدَ ٱللَّهُ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ أَكْبَرُ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (10:83) [listed for 88:10] فَمَآ ءَامَنَ لِمُوسَىٰٓ إِلَّا ذُرِّيَّةٌۭ مِّن قَوْمِهِۦ عَلَىٰ خَوْفٍۢ مِّن فِرْعَوْنَ وَمَلَإِي۟هِمْ أَن يَفْتِنَهُمْ ۚ وَإِنَّ فِرْعَوْنَ لَعَالٍۢ فِى ٱلْأَرْضِ وَإِنَّهُۥ لَمِنَ ٱلْمُسْرِفِينَ
- (13:9) [listed for 88:10] عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْكَبِيرُ ٱلْمُتَعَالِ
- (13:35) [listed for 88:10] ۞ مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ أُكُلُهَا دَآئِمٌۭ وَظِلُّهَا ۚ تِلْكَ عُقْبَى ٱلَّذِينَ ٱتَّقَوا۟ ۖ وَّعُقْبَى ٱلْكَٰفِرِينَ ٱلنَّارُ
- (16:31) [listed for 88:10] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ لَهُمْ فِيهَا مَا يَشَآءُونَ ۚ كَذَٰلِكَ يَجْزِى ٱللَّهُ ٱلْمُتَّقِينَ
- (16:60) [listed for 88:10] لِلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ مَثَلُ ٱلسَّوْءِ ۖ وَلِلَّهِ ٱلْمَثَلُ ٱلْأَعْلَىٰ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (17:4) [listed for 88:10] وَقَضَيْنَآ إِلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ فِى ٱلْكِتَٰبِ لَتُفْسِدُنَّ فِى ٱلْأَرْضِ مَرَّتَيْنِ وَلَتَعْلُنَّ عُلُوًّۭا كَبِيرًۭا
- (17:43) [listed for 88:10] سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يَقُولُونَ عُلُوًّۭا كَبِيرًۭا
- (19:61) [listed for 88:10] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (20:68) [listed for 88:10] [cited in ¶18] قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ
- (20:117) [listed for 88:10] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (23:25) [listed for 88:10] إِنْ هُوَ إِلَّا رَجُلٌۢ بِهِۦ جِنَّةٌۭ فَتَرَبَّصُوا۟ بِهِۦ حَتَّىٰ حِينٍۢ
- (23:46) [listed for 88:10] إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَٱسْتَكْبَرُوا۟ وَكَانُوا۟ قَوْمًا عَالِينَ
- (23:70) [listed for 88:10] أَمْ يَقُولُونَ بِهِۦ جِنَّةٌۢ ۚ بَلْ جَآءَهُم بِٱلْحَقِّ وَأَكْثَرُهُمْ لِلْحَقِّ كَٰرِهُونَ
- (25:15) [listed for 88:10] قُلْ أَذَٰلِكَ خَيْرٌ أَمْ جَنَّةُ ٱلْخُلْدِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۚ كَانَتْ لَهُمْ جَزَآءًۭ وَمَصِيرًۭا
- (25:24) [listed for 88:10] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (26:85) [listed for 88:10] وَٱجْعَلْنِى مِن وَرَثَةِ جَنَّةِ ٱلنَّعِيمِ
- (26:134) [listed for 88:10] وَجَنَّٰتٍۢ وَعُيُونٍ
- (26:147) [listed for 88:10] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (28:4) [listed for 88:10] [cited in ¶17] إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ وَجَعَلَ أَهْلَهَا شِيَعًۭا يَسْتَضْعِفُ طَآئِفَةًۭ مِّنْهُمْ يُذَبِّحُ أَبْنَآءَهُمْ وَيَسْتَحْىِۦ نِسَآءَهُمْ ۚ إِنَّهُۥ كَانَ مِنَ ٱلْمُفْسِدِينَ
- (31:8) [listed for 88:10] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ
- (31:30) [listed for 88:10] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّ مَا يَدْعُونَ مِن دُونِهِ ٱلْبَٰطِلُ وَأَنَّ ٱللَّهَ هُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ
- (32:19) [listed for 88:10] أَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ جَنَّٰتُ ٱلْمَأْوَىٰ نُزُلًۢا بِمَا كَانُوا۟ يَعْمَلُونَ
- (37:8) [listed for 88:10] لَّا يَسَّمَّعُونَ إِلَى ٱلْمَلَإِ ٱلْأَعْلَىٰ وَيُقْذَفُونَ مِن كُلِّ جَانِبٍۢ
- (37:43) [listed for 88:10] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (37:44) [listed for 88:10] عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ
- (38:69) [listed for 88:10] مَا كَانَ لِىَ مِنْ عِلْمٍۭ بِٱلْمَلَإِ ٱلْأَعْلَىٰٓ إِذْ يَخْتَصِمُونَ
- (40:8) [listed for 88:10] رَبَّنَا وَأَدْخِلْهُمْ جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدتَّهُمْ وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (43:4) [listed for 88:10] وَإِنَّهُۥ فِىٓ أُمِّ ٱلْكِتَٰبِ لَدَيْنَا لَعَلِىٌّ حَكِيمٌ
- (43:70) [listed for 88:10] ٱدْخُلُوا۟ ٱلْجَنَّةَ أَنتُمْ وَأَزْوَٰجُكُمْ تُحْبَرُونَ
- (44:14) [listed for 88:10] ثُمَّ تَوَلَّوْا۟ عَنْهُ وَقَالُوا۟ مُعَلَّمٌۭ مَّجْنُونٌ
- (44:19) [listed for 88:10] وَأَن لَّا تَعْلُوا۟ عَلَى ٱللَّهِ ۖ إِنِّىٓ ءَاتِيكُم بِسُلْطَٰنٍۢ مُّبِينٍۢ
- (44:25) [listed for 88:10] كَمْ تَرَكُوا۟ مِن جَنَّٰتٍۢ وَعُيُونٍۢ
- (44:52) [listed for 88:10] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (48:5) [listed for 88:10] لِّيُدْخِلَ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَيُكَفِّرَ عَنْهُمْ سَيِّـَٔاتِهِمْ ۚ وَكَانَ ذَٰلِكَ عِندَ ٱللَّهِ فَوْزًا عَظِيمًۭا
- (50:9) [listed for 88:10] وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا فَأَنۢبَتْنَا بِهِۦ جَنَّٰتٍۢ وَحَبَّ ٱلْحَصِيدِ
- (51:15) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (52:17) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَعِيمٍۢ
- (52:20) [listed for 88:10] مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ ۖ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (53:7) [listed for 88:10] وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ
- (54:54) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَهَرٍۢ
- (55:46) [listed for 88:10] وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- (55:62) [listed for 88:10] وَمِن دُونِهِمَا جَنَّتَانِ
- (56:12) [listed for 88:10] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (56:16) [listed for 88:10] مُّتَّكِـِٔينَ عَلَيْهَا مُتَقَٰبِلِينَ
- (56:34) [listed for 88:10] وَفُرُشٍۢ مَّرْفُوعَةٍ
- (56:89) [listed for 88:10] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (57:12) [listed for 88:10] يَوْمَ تَرَى ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ يَسْعَىٰ نُورُهُم بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِم بُشْرَىٰكُمُ ٱلْيَوْمَ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (57:21) [listed for 88:10] سَابِقُوٓا۟ إِلَىٰ مَغْفِرَةٍۢ مِّن رَّبِّكُمْ وَجَنَّةٍ عَرْضُهَا كَعَرْضِ ٱلسَّمَآءِ وَٱلْأَرْضِ أُعِدَّتْ لِلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَرُسُلِهِۦ ۚ ذَٰلِكَ فَضْلُ ٱللَّهِ يُؤْتِيهِ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (58:16) [listed for 88:10] ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ فَلَهُمْ عَذَابٌۭ مُّهِينٌۭ
- (58:22) [listed for 88:10] لَّا تَجِدُ قَوْمًۭا يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ يُوَآدُّونَ مَنْ حَآدَّ ٱللَّهَ وَرَسُولَهُۥ وَلَوْ كَانُوٓا۟ ءَابَآءَهُمْ أَوْ أَبْنَآءَهُمْ أَوْ إِخْوَٰنَهُمْ أَوْ عَشِيرَتَهُمْ ۚ أُو۟لَٰٓئِكَ كَتَبَ فِى قُلُوبِهِمُ ٱلْإِيمَٰنَ وَأَيَّدَهُم بِرُوحٍۢ مِّنْهُ ۖ وَيُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ رَضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱللَّهِ ۚ أَلَآ إِنَّ حِزْبَ ٱللَّهِ هُمُ ٱلْمُفْلِحُونَ
- (61:12) [listed for 88:10] يَغْفِرْ لَكُمْ ذُنُوبَكُمْ وَيُدْخِلْكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (63:2) [listed for 88:10] ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّهُمْ سَآءَ مَا كَانُوا۟ يَعْمَلُونَ
- (64:9) [listed for 88:10] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (66:8) [listed for 88:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (70:35) [listed for 88:10] أُو۟لَٰٓئِكَ فِى جَنَّٰتٍۢ مُّكْرَمُونَ
- (70:38) [listed for 88:10] أَيَطْمَعُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُدْخَلَ جَنَّةَ نَعِيمٍۢ
- (71:12) [listed for 88:10] وَيُمْدِدْكُم بِأَمْوَٰلٍۢ وَبَنِينَ وَيَجْعَل لَّكُمْ جَنَّٰتٍۢ وَيَجْعَل لَّكُمْ أَنْهَٰرًۭا
- (72:3) [listed for 88:10] وَأَنَّهُۥ تَعَٰلَىٰ جَدُّ رَبِّنَا مَا ٱتَّخَذَ صَٰحِبَةًۭ وَلَا وَلَدًۭا
- (76:12) [listed for 88:10] وَجَزَىٰهُم بِمَا صَبَرُوا۟ جَنَّةًۭ وَحَرِيرًۭا
- (76:13) [listed for 88:10] [cited in ¶14] مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۖ لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا
- (78:16) [listed for 88:10] [cited in ¶5] وَجَنَّٰتٍ أَلْفَافًا
- (78:31) [listed for 88:10] إِنَّ لِلْمُتَّقِينَ مَفَازًا
- (79:41) [listed for 88:10] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- (81:13) [listed for 88:10] وَإِذَا ٱلْجَنَّةُ أُزْلِفَتْ
- (83:19) [listed for 88:10] وَمَآ أَدْرَىٰكَ مَا عِلِّيُّونَ
- (83:23) [listed for 88:10] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ
- (85:11) [listed for 88:10] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْكَبِيرُ
- (92:1) [listed for 88:10] وَٱلَّيْلِ إِذَا يَغْشَىٰ
- (98:8) [listed for 88:10] جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ
- (114:6) [listed for 88:10] مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ

## named by the passage's own list as strong for this ayah (12)

- (12:57) [listed for 88:10] وَلَأَجْرُ ٱلْءَاخِرَةِ خَيْرٌۭ لِّلَّذِينَ ءَامَنُوا۟ وَكَانُوا۟ يَتَّقُونَ
- (18:108) [listed for 88:10] خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا
- (19:62) [listed for 88:10] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (25:76) [listed for 88:10] خَٰلِدِينَ فِيهَا ۚ حَسُنَتْ مُسْتَقَرًّۭا وَمُقَامًۭا
- (36:26) [listed for 88:10] قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ
- (38:49) [listed for 88:10] هَٰذَا ذِكْرٌۭ ۚ وَإِنَّ لِلْمُتَّقِينَ لَحُسْنَ مَـَٔابٍۢ
- (41:32) [listed for 88:10] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (43:71) [listed for 88:10] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (69:23) [listed for 88:10] [cited in ¶14] قُطُوفُهَا دَانِيَةٌۭ
- (74:40) [listed for 88:10] فِى جَنَّٰتٍۢ يَتَسَآءَلُونَ
- (77:41) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى ظِلَٰلٍۢ وَعُيُونٍۢ
- (77:43) [listed for 88:10] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ

## named by the passage's own list as medium for this ayah (42)

- (2:25) [listed for 88:10] وَبَشِّرِ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ كُلَّمَا رُزِقُوا۟ مِنْهَا مِن ثَمَرَةٍۢ رِّزْقًۭا ۙ قَالُوا۟ هَٰذَا ٱلَّذِى رُزِقْنَا مِن قَبْلُ ۖ وَأُتُوا۟ بِهِۦ مُتَشَٰبِهًۭا ۖ وَلَهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَهُمْ فِيهَا خَٰلِدُونَ
- (6:16) [listed for 88:10] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (10:26) [listed for 88:10] ۞ لِّلَّذِينَ أَحْسَنُوا۟ ٱلْحُسْنَىٰ وَزِيَادَةٌۭ ۖ وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (13:23) [listed for 88:10] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۖ وَٱلْمَلَٰٓئِكَةُ يَدْخُلُونَ عَلَيْهِم مِّن كُلِّ بَابٍۢ
- (13:24) [listed for 88:10] سَلَٰمٌ عَلَيْكُم بِمَا صَبَرْتُمْ ۚ فَنِعْمَ عُقْبَى ٱلدَّارِ
- (15:74) [listed for 88:10] فَجَعَلْنَا عَٰلِيَهَا سَافِلَهَا وَأَمْطَرْنَا عَلَيْهِمْ حِجَارَةًۭ مِّن سِجِّيلٍ
- (18:107) [listed for 88:10] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ كَانَتْ لَهُمْ جَنَّٰتُ ٱلْفِرْدَوْسِ نُزُلًا
- (19:85) [listed for 88:10] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
- (20:119) [listed for 88:10] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (21:102) [listed for 88:10] لَا يَسْمَعُونَ حَسِيسَهَا ۖ وَهُمْ فِى مَا ٱشْتَهَتْ أَنفُسُهُمْ خَٰلِدُونَ
- (32:17) [listed for 88:10] [cited in ¶7] فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (35:33) [listed for 88:10] جَنَّٰتُ عَدْنٍۢ يَدْخُلُونَهَا يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَلُؤْلُؤًۭا ۖ وَلِبَاسُهُمْ فِيهَا حَرِيرٌۭ
- (36:55) [listed for 88:10] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (36:58) [listed for 88:10] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (37:42) [listed for 88:10] فَوَٰكِهُ ۖ وَهُم مُّكْرَمُونَ
- (37:46) [listed for 88:10] بَيْضَآءَ لَذَّةٍۢ لِّلشَّٰرِبِينَ
- (37:47) [listed for 88:10] لَا فِيهَا غَوْلٌۭ وَلَا هُمْ عَنْهَا يُنزَفُونَ
- (37:58) [listed for 88:10] أَفَمَا نَحْنُ بِمَيِّتِينَ
- (37:62) [listed for 88:10] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (38:51) [listed for 88:10] مُتَّكِـِٔينَ فِيهَا يَدْعُونَ فِيهَا بِفَٰكِهَةٍۢ كَثِيرَةٍۢ وَشَرَابٍۢ
- (38:54) [listed for 88:10] إِنَّ هَٰذَا لَرِزْقُنَا مَا لَهُۥ مِن نَّفَادٍ
- (39:73) [listed for 88:10] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
- (44:51) [listed for 88:10] إِنَّ ٱلْمُتَّقِينَ فِى مَقَامٍ أَمِينٍۢ
- (44:55) [listed for 88:10] يَدْعُونَ فِيهَا بِكُلِّ فَٰكِهَةٍ ءَامِنِينَ
- (44:57) [listed for 88:10] فَضْلًۭا مِّن رَّبِّكَ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (50:34) [listed for 88:10] ٱدْخُلُوهَا بِسَلَٰمٍۢ ۖ ذَٰلِكَ يَوْمُ ٱلْخُلُودِ
- (52:18) [listed for 88:10] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (52:19) [listed for 88:10] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (52:22) [listed for 88:10] وَأَمْدَدْنَٰهُم بِفَٰكِهَةٍۢ وَلَحْمٍۢ مِّمَّا يَشْتَهُونَ
- (55:68) [listed for 88:10] فِيهِمَا فَٰكِهَةٌۭ وَنَخْلٌۭ وَرُمَّانٌۭ
- (56:18) [listed for 88:10] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:33) [listed for 88:10] لَّا مَقْطُوعَةٍۢ وَلَا مَمْنُوعَةٍۢ
- (69:21) [listed for 88:10] [cited in ¶13] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- (69:24) [listed for 88:10] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ
- (76:11) [listed for 88:10] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (76:21) [listed for 88:10] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:42) [listed for 88:10] وَفَوَٰكِهَ مِمَّا يَشْتَهُونَ
- (83:18) [listed for 88:10] [cited in ¶15] كَلَّآ إِنَّ كِتَٰبَ ٱلْأَبْرَارِ لَفِى عِلِّيِّينَ
- (83:22) [listed for 88:10] [cited in ¶15] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:26) [listed for 88:10] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ
- (87:1) [listed for 88:10] سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- (101:7) [listed for 88:10] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## weak (this ayah's own list) (20)

- (2:177) [listed for 88:10] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
- (6:100) [listed for 88:10] وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ ٱلْجِنَّ وَخَلَقَهُمْ ۖ وَخَرَقُوا۟ لَهُۥ بَنِينَ وَبَنَٰتٍۭ بِغَيْرِ عِلْمٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يَصِفُونَ
- (7:184) [listed for 88:10] أَوَلَمْ يَتَفَكَّرُوا۟ ۗ مَا بِصَاحِبِهِم مِّن جِنَّةٍ ۚ إِنْ هُوَ إِلَّا نَذِيرٌۭ مُّبِينٌ
- (9:78) [listed for 88:10] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ سِرَّهُمْ وَنَجْوَىٰهُمْ وَأَنَّ ٱللَّهَ عَلَّٰمُ ٱلْغُيُوبِ
- (12:86) [listed for 88:10] قَالَ إِنَّمَآ أَشْكُوا۟ بَثِّى وَحُزْنِىٓ إِلَى ٱللَّهِ وَأَعْلَمُ مِنَ ٱللَّهِ مَا لَا تَعْلَمُونَ
- (16:1) [listed for 88:10] أَتَىٰٓ أَمْرُ ٱللَّهِ فَلَا تَسْتَعْجِلُوهُ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (17:91) [listed for 88:10] أَوْ تَكُونَ لَكَ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَعِنَبٍۢ فَتُفَجِّرَ ٱلْأَنْهَٰرَ خِلَٰلَهَا تَفْجِيرًا
- (19:50) [listed for 88:10] وَوَهَبْنَا لَهُم مِّن رَّحْمَتِنَا وَجَعَلْنَا لَهُمْ لِسَانَ صِدْقٍ عَلِيًّۭا
- (22:14) [listed for 88:10] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ إِنَّ ٱللَّهَ يَفْعَلُ مَا يُرِيدُ
- (25:8) [listed for 88:10] أَوْ يُلْقَىٰٓ إِلَيْهِ كَنزٌ أَوْ تَكُونُ لَهُۥ جَنَّةٌۭ يَأْكُلُ مِنْهَا ۚ وَقَالَ ٱلظَّٰلِمُونَ إِن تَتَّبِعُونَ إِلَّا رَجُلًۭا مَّسْحُورًا
- (25:10) [listed for 88:10] تَبَارَكَ ٱلَّذِىٓ إِن شَآءَ جَعَلَ لَكَ خَيْرًۭا مِّن ذَٰلِكَ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَيَجْعَل لَّكَ قُصُورًۢا
- (27:13) [listed for 88:10] فَلَمَّا جَآءَتْهُمْ ءَايَٰتُنَا مُبْصِرَةًۭ قَالُوا۟ هَٰذَا سِحْرٌۭ مُّبِينٌۭ
- (34:8) [listed for 88:10] أَفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَم بِهِۦ جِنَّةٌۢ ۗ بَلِ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ فِى ٱلْعَذَابِ وَٱلضَّلَٰلِ ٱلْبَعِيدِ
- (34:46) [listed for 88:10] ۞ قُلْ إِنَّمَآ أَعِظُكُم بِوَٰحِدَةٍ ۖ أَن تَقُومُوا۟ لِلَّهِ مَثْنَىٰ وَفُرَٰدَىٰ ثُمَّ تَتَفَكَّرُوا۟ ۚ مَا بِصَاحِبِكُم مِّن جِنَّةٍ ۚ إِنْ هُوَ إِلَّا نَذِيرٌۭ لَّكُم بَيْنَ يَدَىْ عَذَابٍۢ شَدِيدٍۢ
- (37:36) [listed for 88:10] وَيَقُولُونَ أَئِنَّا لَتَارِكُوٓا۟ ءَالِهَتِنَا لِشَاعِرٍۢ مَّجْنُونٍۭ
- (38:74) [listed for 88:10] إِلَّآ إِبْلِيسَ ٱسْتَكْبَرَ وَكَانَ مِنَ ٱلْكَٰفِرِينَ
- (38:75) [listed for 88:10] قَالَ يَٰٓإِبْلِيسُ مَا مَنَعَكَ أَن تَسْجُدَ لِمَا خَلَقْتُ بِيَدَىَّ ۖ أَسْتَكْبَرْتَ أَمْ كُنتَ مِنَ ٱلْعَالِينَ
- (38:76) [listed for 88:10] قَالَ أَنَا۠ خَيْرٌۭ مِّنْهُ ۖ خَلَقْتَنِى مِن نَّارٍۢ وَخَلَقْتَهُۥ مِن طِينٍۢ
- (47:35) [listed for 88:10] فَلَا تَهِنُوا۟ وَتَدْعُوٓا۟ إِلَى ٱلسَّلْمِ وَأَنتُمُ ٱلْأَعْلَوْنَ وَٱللَّهُ مَعَكُمْ وَلَن يَتِرَكُمْ أَعْمَٰلَكُمْ
- (101:11) [listed for 88:10] نَارٌ حَامِيَةٌۢ

## named by the passage's own list as weak for this ayah (20)

- (2:82) [listed for 88:10] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (9:89) [listed for 88:10] أَعَدَّ ٱللَّهُ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (18:3) [listed for 88:10] مَّٰكِثِينَ فِيهِ أَبَدًۭا
- (19:57) [listed for 88:10] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- (20:64) [listed for 88:10] [cited in ¶18] فَأَجْمِعُوا۟ كَيْدَكُمْ ثُمَّ ٱئْتُوا۟ صَفًّۭا ۚ وَقَدْ أَفْلَحَ ٱلْيَوْمَ مَنِ ٱسْتَعْلَىٰ
- (20:76) [listed for 88:10] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
- (22:56) [listed for 88:10] ٱلْمُلْكُ يَوْمَئِذٍۢ لِّلَّهِ يَحْكُمُ بَيْنَهُمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (23:11) [listed for 88:10] ٱلَّذِينَ يَرِثُونَ ٱلْفِرْدَوْسَ هُمْ فِيهَا خَٰلِدُونَ
- (26:57) [listed for 88:10] فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍۢ وَعُيُونٍۢ
- (26:90) [listed for 88:10] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ
- (36:27) [listed for 88:10] بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ
- (38:50) [listed for 88:10] جَنَّٰتِ عَدْنٍۢ مُّفَتَّحَةًۭ لَّهُمُ ٱلْأَبْوَٰبُ
- (44:31) [listed for 88:10] مِن فِرْعَوْنَ ۚ إِنَّهُۥ كَانَ عَالِيًۭا مِّنَ ٱلْمُسْرِفِينَ
- (47:12) [listed for 88:10] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
- (50:35) [listed for 88:10] لَهُم مَّا يَشَآءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌۭ
- (56:3) [listed for 88:10] خَافِضَةٌۭ رَّافِعَةٌ
- (68:2) [listed for 88:10] مَآ أَنتَ بِنِعْمَةِ رَبِّكَ بِمَجْنُونٍۢ
- (68:34) [listed for 88:10] إِنَّ لِلْمُتَّقِينَ عِندَ رَبِّهِمْ جَنَّٰتِ ٱلنَّعِيمِ
- (79:24) [listed for 88:10] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
- (89:30) [listed for 88:10] وَٱدْخُلِى جَنَّتِى

## neighbours: within two ayat of a passage the commentary cites (75)

- (2:262) [next to 2:264] ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى ۙ لَّهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:263) [next to 2:264] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
- (2:267) [next to 2:265] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
- (2:268) [next to 2:266] ٱلشَّيْطَٰنُ يَعِدُكُمُ ٱلْفَقْرَ وَيَأْمُرُكُم بِٱلْفَحْشَآءِ ۖ وَٱللَّهُ يَعِدُكُم مَّغْفِرَةًۭ مِّنْهُ وَفَضْلًۭا ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (4:143) [next to 4:145] مُّذَبْذَبِينَ بَيْنَ ذَٰلِكَ لَآ إِلَىٰ هَٰٓؤُلَآءِ وَلَآ إِلَىٰ هَٰٓؤُلَآءِ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَلَن تَجِدَ لَهُۥ سَبِيلًۭا
- (4:144) [next to 4:145] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ ٱلْكَٰفِرِينَ أَوْلِيَآءَ مِن دُونِ ٱلْمُؤْمِنِينَ ۚ أَتُرِيدُونَ أَن تَجْعَلُوا۟ لِلَّهِ عَلَيْكُمْ سُلْطَٰنًۭا مُّبِينًا
- (4:146) [next to 4:145] إِلَّا ٱلَّذِينَ تَابُوا۟ وَأَصْلَحُوا۟ وَٱعْتَصَمُوا۟ بِٱللَّهِ وَأَخْلَصُوا۟ دِينَهُمْ لِلَّهِ فَأُو۟لَٰٓئِكَ مَعَ ٱلْمُؤْمِنِينَ ۖ وَسَوْفَ يُؤْتِ ٱللَّهُ ٱلْمُؤْمِنِينَ أَجْرًا عَظِيمًۭا
- (4:147) [next to 4:145] مَّا يَفْعَلُ ٱللَّهُ بِعَذَابِكُمْ إِن شَكَرْتُمْ وَءَامَنتُمْ ۚ وَكَانَ ٱللَّهُ شَاكِرًا عَلِيمًۭا
- (18:33) [next to 18:35] كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا وَلَمْ تَظْلِم مِّنْهُ شَيْـًۭٔا ۚ وَفَجَّرْنَا خِلَٰلَهُمَا نَهَرًۭا
- (18:34) [next to 18:35] وَكَانَ لَهُۥ ثَمَرٌۭ فَقَالَ لِصَٰحِبِهِۦ وَهُوَ يُحَاوِرُهُۥٓ أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا
- (18:36) [next to 18:35] وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّدِدتُّ إِلَىٰ رَبِّى لَأَجِدَنَّ خَيْرًۭا مِّنْهَا مُنقَلَبًۭا
- (18:37) [next to 18:35] قَالَ لَهُۥ صَاحِبُهُۥ وَهُوَ يُحَاوِرُهُۥٓ أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا
- (18:40) [next to 18:42] فَعَسَىٰ رَبِّىٓ أَن يُؤْتِيَنِ خَيْرًۭا مِّن جَنَّتِكَ وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا
- (18:41) [next to 18:42] أَوْ يُصْبِحَ مَآؤُهَا غَوْرًۭا فَلَن تَسْتَطِيعَ لَهُۥ طَلَبًۭا
- (18:43) [next to 18:42] وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا
- (18:44) [next to 18:42] هُنَالِكَ ٱلْوَلَٰيَةُ لِلَّهِ ٱلْحَقِّ ۚ هُوَ خَيْرٌۭ ثَوَابًۭا وَخَيْرٌ عُقْبًۭا
- (20:62) [next to 20:64] فَتَنَٰزَعُوٓا۟ أَمْرَهُم بَيْنَهُمْ وَأَسَرُّوا۟ ٱلنَّجْوَىٰ
- (20:63) [next to 20:64] قَالُوٓا۟ إِنْ هَٰذَٰنِ لَسَٰحِرَٰنِ يُرِيدَانِ أَن يُخْرِجَاكُم مِّنْ أَرْضِكُم بِسِحْرِهِمَا وَيَذْهَبَا بِطَرِيقَتِكُمُ ٱلْمُثْلَىٰ
- (20:65) [next to 20:64] قَالُوا۟ يَٰمُوسَىٰٓ إِمَّآ أَن تُلْقِىَ وَإِمَّآ أَن نَّكُونَ أَوَّلَ مَنْ أَلْقَىٰ
- (20:66) [next to 20:64] قَالَ بَلْ أَلْقُوا۟ ۖ فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ أَنَّهَا تَسْعَىٰ
- (20:67) [next to 20:68] فَأَوْجَسَ فِى نَفْسِهِۦ خِيفَةًۭ مُّوسَىٰ
- (20:69) [next to 20:68] وَأَلْقِ مَا فِى يَمِينِكَ تَلْقَفْ مَا صَنَعُوٓا۟ ۖ إِنَّمَا صَنَعُوا۟ كَيْدُ سَٰحِرٍۢ ۖ وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ
- (20:71) [next to 20:70] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (20:72) [next to 20:70] قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ
- (20:73) [next to 20:75] إِنَّآ ءَامَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَٰيَٰنَا وَمَآ أَكْرَهْتَنَا عَلَيْهِ مِنَ ٱلسِّحْرِ ۗ وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ
- (20:74) [next to 20:75] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:77) [next to 20:75] وَلَقَدْ أَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ أَنْ أَسْرِ بِعِبَادِى فَٱضْرِبْ لَهُمْ طَرِيقًۭا فِى ٱلْبَحْرِ يَبَسًۭا لَّا تَخَٰفُ دَرَكًۭا وَلَا تَخْشَىٰ
- (28:2) [next to 28:4] تِلْكَ ءَايَٰتُ ٱلْكِتَٰبِ ٱلْمُبِينِ
- (28:3) [next to 28:4] نَتْلُوا۟ عَلَيْكَ مِن نَّبَإِ مُوسَىٰ وَفِرْعَوْنَ بِٱلْحَقِّ لِقَوْمٍۢ يُؤْمِنُونَ
- (28:5) [next to 28:4] وَنُرِيدُ أَن نَّمُنَّ عَلَى ٱلَّذِينَ ٱسْتُضْعِفُوا۟ فِى ٱلْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةًۭ وَنَجْعَلَهُمُ ٱلْوَٰرِثِينَ
- (28:6) [next to 28:4] وَنُمَكِّنَ لَهُمْ فِى ٱلْأَرْضِ وَنُرِىَ فِرْعَوْنَ وَهَٰمَٰنَ وَجُنُودَهُمَا مِنْهُم مَّا كَانُوا۟ يَحْذَرُونَ
- (28:77) [next to 28:79] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (28:78) [next to 28:79] قَالَ إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍ عِندِىٓ ۚ أَوَلَمْ يَعْلَمْ أَنَّ ٱللَّهَ قَدْ أَهْلَكَ مِن قَبْلِهِۦ مِنَ ٱلْقُرُونِ مَنْ هُوَ أَشَدُّ مِنْهُ قُوَّةًۭ وَأَكْثَرُ جَمْعًۭا ۚ وَلَا يُسْـَٔلُ عَن ذُنُوبِهِمُ ٱلْمُجْرِمُونَ
- (28:80) [next to 28:79] وَقَالَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ وَيْلَكُمْ ثَوَابُ ٱللَّهِ خَيْرٌۭ لِّمَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا وَلَا يُلَقَّىٰهَآ إِلَّا ٱلصَّٰبِرُونَ
- (28:82) [next to 28:81] وَأَصْبَحَ ٱلَّذِينَ تَمَنَّوْا۟ مَكَانَهُۥ بِٱلْأَمْسِ يَقُولُونَ وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ ۖ لَوْلَآ أَن مَّنَّ ٱللَّهُ عَلَيْنَا لَخَسَفَ بِنَا ۖ وَيْكَأَنَّهُۥ لَا يُفْلِحُ ٱلْكَٰفِرُونَ
- (28:84) [next to 28:83] مَن جَآءَ بِٱلْحَسَنَةِ فَلَهُۥ خَيْرٌۭ مِّنْهَا ۖ وَمَن جَآءَ بِٱلسَّيِّئَةِ فَلَا يُجْزَى ٱلَّذِينَ عَمِلُوا۟ ٱلسَّيِّـَٔاتِ إِلَّا مَا كَانُوا۟ يَعْمَلُونَ
- (28:85) [next to 28:83] إِنَّ ٱلَّذِى فَرَضَ عَلَيْكَ ٱلْقُرْءَانَ لَرَآدُّكَ إِلَىٰ مَعَادٍۢ ۚ قُل رَّبِّىٓ أَعْلَمُ مَن جَآءَ بِٱلْهُدَىٰ وَمَنْ هُوَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (32:15) [next to 32:17] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (32:16) [next to 32:17] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (32:18) [next to 32:17] أَفَمَن كَانَ مُؤْمِنًۭا كَمَن كَانَ فَاسِقًۭا ۚ لَّا يَسْتَوُۥنَ
- (39:18) [next to 39:20] ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَىٰهُمُ ٱللَّهُ ۖ وَأُو۟لَٰٓئِكَ هُمْ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:19) [next to 39:20] أَفَمَنْ حَقَّ عَلَيْهِ كَلِمَةُ ٱلْعَذَابِ أَفَأَنتَ تُنقِذُ مَن فِى ٱلنَّارِ
- (39:21) [next to 39:20] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (39:22) [next to 39:20] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (42:43) [next to 42:45] وَلَمَن صَبَرَ وَغَفَرَ إِنَّ ذَٰلِكَ لَمِنْ عَزْمِ ٱلْأُمُورِ
- (42:44) [next to 42:45] وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن وَلِىٍّۢ مِّنۢ بَعْدِهِۦ ۗ وَتَرَى ٱلظَّٰلِمِينَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ يَقُولُونَ هَلْ إِلَىٰ مَرَدٍّۢ مِّن سَبِيلٍۢ
- (42:46) [next to 42:45] وَمَا كَانَ لَهُم مِّنْ أَوْلِيَآءَ يَنصُرُونَهُم مِّن دُونِ ٱللَّهِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن سَبِيلٍ
- (42:47) [next to 42:45] ٱسْتَجِيبُوا۟ لِرَبِّكُم مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۚ مَا لَكُم مِّن مَّلْجَإٍۢ يَوْمَئِذٍۢ وَمَا لَكُم مِّن نَّكِيرٍۢ
- (68:15) [next to 68:17] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (68:16) [next to 68:17] سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ
- (68:18) [next to 68:17] وَلَا يَسْتَثْنُونَ
- (68:21) [next to 68:19] فَتَنَادَوْا۟ مُصْبِحِينَ
- (68:22) [next to 68:20] أَنِ ٱغْدُوا۟ عَلَىٰ حَرْثِكُمْ إِن كُنتُمْ صَٰرِمِينَ
- (69:17) [next to 69:19] وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا ۚ وَيَحْمِلُ عَرْشَ رَبِّكَ فَوْقَهُمْ يَوْمَئِذٍۢ ثَمَٰنِيَةٌۭ
- (69:18) [next to 69:19] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (69:25) [next to 69:23] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ فَيَقُولُ يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ
- (69:34) [next to 69:36] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (69:35) [next to 69:36] فَلَيْسَ لَهُ ٱلْيَوْمَ هَٰهُنَا حَمِيمٌۭ
- (69:37) [next to 69:36] لَّا يَأْكُلُهُۥٓ إِلَّا ٱلْخَٰطِـُٔونَ
- (69:38) [next to 69:36] فَلَآ أُقْسِمُ بِمَا تُبْصِرُونَ
- (76:15) [next to 76:13] وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠
- (76:16) [next to 76:14] قَوَارِيرَا۟ مِن فِضَّةٍۢ قَدَّرُوهَا تَقْدِيرًۭا
- (78:13) [next to 78:15] وَجَعَلْنَا سِرَاجًۭا وَهَّاجًۭا
- (78:14) [next to 78:15] وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا
- (78:17) [next to 78:15] إِنَّ يَوْمَ ٱلْفَصْلِ كَانَ مِيقَٰتًۭا
- (78:18) [next to 78:16] يَوْمَ يُنفَخُ فِى ٱلصُّورِ فَتَأْتُونَ أَفْوَاجًۭا
- (83:5) [next to 83:7] لِيَوْمٍ عَظِيمٍۢ
- (83:6) [next to 83:7] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
- (83:8) [next to 83:7] وَمَآ أَدْرَىٰكَ مَا سِجِّينٌۭ
- (83:9) [next to 83:7] كِتَٰبٌۭ مَّرْقُومٌۭ
- (83:16) [next to 83:18] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
- (83:17) [next to 83:18] ثُمَّ يُقَالُ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (83:20) [next to 83:18] كِتَٰبٌۭ مَّرْقُومٌۭ
- (83:21) [next to 83:22] يَشْهَدُهُ ٱلْمُقَرَّبُونَ
- (83:24) [next to 83:22] تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ

