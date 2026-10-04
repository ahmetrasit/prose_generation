Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:7; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_7.reading.tr.md (prose paragraphs numbered) =====
## Yol, üzerinde yürüyenlerle tanınır

[¶1] Altıncı ayet bir yol ister: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-müstakîm, gloss:bizi dosdoğru yola ilet, source:1:6}. Yedinci ayet aynı kelimeyi aynı hâl ekiyle yeniden söyleyerek başlar: {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:sırâta'llezîne en'amte aleyhim, gloss:kendilerine nimet verdiğin kimselerin yolunu, source:1:7}. İkinci "sırat" birincinin yerine konur ve onu açıklar. Dua böylece aynı yolu iki kez adlandırır: önce bir niteliğiyle, "dosdoğru" diye; sonra yolcularıyla, "onların yolu" diye. İstenen şey yalnızca doğru bir yön değildir, o yönde daha önce yürümüş insanların bıraktığı izdir. Yolu tanımanın yolu, üzerinde kimlerin yürüdüğünü bilmektir.

[¶2] Türkçede "sırat" kelimesi neredeyse yalnızca bir köprüyü çağırır: kıldan ince, kılıçtan keskin, üzerinden zor geçilen bir geçit. Arapçada kelimede böyle bir darlık yoktur. Düpedüz yol demektir ve üç ayrı sesle söylenir: {ar:الصراط والسراط والزراط: الطريق, tr:es-sırât ve's-sirât ve'z-zırât: et-tarîk, gloss:sırat, sirat ve zırat yol demektir, source:"ص ر ط,B001"}. Kelimenin tanımında düzlük de vardır: {ar:الصراط: الطريق المستقيم, tr:es-sırât: et-tarîku'l-müstakîm, gloss:sırat düz yoldur, source:"ص ر ط,B001"}. Kur'an kelimeyi bu genişliğiyle kullanır. Zulmedenlerin, eşlerinin ve taptıkları şeylerin toplanması emredilen bir sahnede, onların da bir sırata götürülmesi istenir: {ar:فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ, tr:fehdûhüm ilâ sırâti'l-cahîm, gloss:onları cehennemin yoluna götürün, source:37:23}. Demek ki sırat kendi başına iyi ya da kötü değildir. Onu iyi kılan, nereye çıktığı ve kimin yolu olduğudur. Ayetteki sırat bir sınav köprüsü değildir. İnsanın gündelik adımlarıyla yürüdüğü yoldur.

[¶3] Kur'an bu iki adımlı tanımı başka bir yerde de kurar. Kendilerine verilen öğüdü tutmayan bir topluluk için, tutsalardı bunun onlara daha hayırlı olacağı ve ayaklarını daha sağlam basacakları söylenir {source:4:66}. Ardından onlara büyük bir ödül verileceği ve şu söz gelir: {ar:وَلَهَدَيْنَٰهُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve le-hedeynâhüm sırâtan müstakîmâ, gloss:onları dosdoğru bir yola da iletirdik, source:4:68}. Hemen sonraki ayet, Fâtiha'nın altıncı ayetten yedinci ayete attığı adımı atar ve yolu insanlarla tanımlar: {ar:فَأُو۟لَٰٓئِكَ مَعَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ وَٱلصِّدِّيقِينَ وَٱلشُّهَدَآءِ وَٱلصَّٰلِحِينَ, tr:fe-ülâike meallezîne en'amallâhu aleyhim mine'n-nebiyyîne ve's-sıddîkîne ve'ş-şühedâi ve's-sâlihîn, gloss:onlar Allah'ın nimet verdiği peygamberlerle, sıddıklarla, şehitlerle ve salihlerle beraberdir, source:4:69}. Ayet bir arkadaşlık sözüyle biter: {ar:وَحَسُنَ أُو۟لَٰٓئِكَ رَفِيقًۭا, tr:ve hasüne ülâike refîkâ, gloss:onlar ne güzel yol arkadaşlarıdır, source:4:69}. Fâtiha'daki "onlar" böylece adı konmuş bir yol arkadaşlığına dönüşür.

[¶4] Kur'an bu arkadaşlığın kendiliğinden miras kalmadığını da gösterir. Zekeriya'dan İdris'e kadar peygamberlerin anıldığı bir dizinin sonunda aynı söz tekrarlanır: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم, tr:ülâikellezîne en'amallâhu aleyhim, gloss:Allah'ın nimet verdiği kimseler işte bunlardır, source:19:58}. Hemen ardından şu gelir: {ar:فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌ أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ, tr:fe-halefe min ba'dihim halfün edâ'u's-salâte vettebe'u'ş-şehevât, gloss:onlardan sonra namazı yitiren ve arzularının ardına düşen bir kuşak geldi, source:19:59}. Yol, nimet verilenlerin soyundan gelenlere değil, onların yürüdüğü gibi yürüyenlere aittir.

[¶5] Bu yolun bir de ayak tarafı vardır. Buradan sonra ayetin kelimelerinin akrabalarından gelecek görüntüler, kelimenin bu ayetteki anlamının yerine geçmez. O anlamın yanında, bir yankı gibi duyulur. "En'amte" ayette "nimet verdin" demektir. Aynı kökten bir ad ise ayağa ve yürüyüşe bağlanır. Bir kimseye binek olmadan, yaya gidildiğinde şöyle denirdi: {ar:تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه, tr:tena''amtü Zeyden talebtühû, gloss:Zeyd'e yürüyerek gittim, sanki ona doğru neâmemi, yani ayağımın tabanını çalıştırdım, source:"ن ع م,B012"}. Ayaklarını yürüye yürüye aşındıran için de {ar:تنعم فلان قدميه أي ابتذلهما, tr:tena''ame fülânün kademeyhi, gloss:ayaklarını yürümekle eskitti, source:"ن ع م,B012"} derlerdi. "İbnü'n-neâme" adı da hem ayaktaki bir damara hem de yolun çok çiğnenmiş ana izine verilir: {ar:وابن النعامة عرق الرجل ومحجة الطريق, tr:ve ibnü'n-neâmeti irku'r-ricli ve mehaccetü't-tarîk, gloss:ibnü'n-neâme ayaktaki bir damardır ve yolun çiğnenmiş ana izidir, source:"ن ع م,B007"}. Ayağın tabanı, yaya gidiş ve yaya gidişin toprakta açtığı ana iz aynı kökten konuşur. Bu, nimet anlamının ayaktan türediği anlamına gelmez. İki anlam aynı kökte yan yana durur ve ayetin cümlesi ikisini aynı yere, yolun üzerine getirir. "Nimet verdiklerinin yolu" sözünün yanında, çok ayakla yürünmüş, izi belirginleşmiş bir yol duyulur. Beşinci ayetteki "na'büdü" kelimesinin akrabaları da çok yürünüp düzlenmiş yola ad verir. Surenin yol sahnesi bu iki izi orada buluşturur.

## Üç topluluk, üç ayrı cümle kuruluşu

[¶6] Ayetteki üç topluluk üç ayrı dil bilgisi yapısıyla anılır ve aradaki fark anlamın kendisini taşır. Birinci topluluk bir fiille gelir: {ar:أَنْعَمْتَ, tr:en'amte, gloss:nimet verdin, source:1:7}. Fiilin öznesi "sen"dir. Sure ilk dört ayette Allah'tan üçüncü şahısla söz eder, beşinci ayette ise doğrudan O'na döner: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke na'büdü ve iyyâke neste'în, gloss:yalnız sana kulluk eder, yalnız senden yardım isteriz, source:1:5}. Altıncı ayetin isteği bu hitabın içinden söylenir. Yedinci ayetteki nimet de aynı "sen"e bağlanır. Konuşan, nimet verilenlerden söz ederken bile gözünü nimeti verenden ayırmaz.

[¶7] İkinci topluluk bir fiille değil, edilgen bir sıfatla anılır: {ar:ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:el-magdûbi aleyhim, gloss:üzerlerine gazap edilmiş olanlar, source:1:7}. Gazap onların üzerindedir, ama kimin gazabı olduğu söylenmez. Kur'an başka yerlerde bunu açıkça söyler. Müminlere şöyle seslenilir: {ar:لَا تَتَوَلَّوْا۟ قَوْمًا غَضِبَ ٱللَّهُ عَلَيْهِمْ, tr:lâ tetevellev kavmen gadiba'llâhu aleyhim, gloss:Allah'ın gazap ettiği bir topluluğu dost edinmeyin, source:60:13}. Fâtiha'nın duası aynı "aleyhim"i kurar, ama failin yerini boş bırakır. Nimet "sen verdin" diye söylenir, gazap ise faili anılmadan. Duanın dili, iyiliği verene "sen" diye seslenir. Gazabı aynı yakınlıkta bir "sen"e bağlamaz.

[¶8] Üçüncü topluluk etken bir sıfatla anılır: {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:yolunu yitirenler, source:1:7}. Burada "aleyhim" yoktur, üzerlerine hiçbir şey inmez. Yoldan çıkmak onların kendi yürüyüşünün adıdır. Cümle böylece üç durumu birbirinden ayırır: üzerlerine senden iyilik inenler, üzerlerine gazap inenler ve kendi ayaklarıyla yoldan çıkanlar.

[¶9] İki olumsuz topluluğu ayıran kelime de kendi işini görür. {ar:غَيْرِ, tr:gayri, gloss:-den başka olan, -den olmayan, source:1:7} "başka" demektir: {ar:هذا الشيء غير ذاك أي هو سواه وخلافه, tr:hâze'ş-şey'ü gayru zâke, gloss:bu şey ondan başkadır, yani onun dışındadır ve ona aykırıdır, source:"غ ي ر,B005"}. Kelimenin olumsuzluk da taşıdığı söylenir: {ar:معنى غير معنى لا, tr:ma'nâ gayr ma'nâ lâ, gloss:gayrın anlamı lâ'nın, yani "değil"in anlamıdır, source:"غ ي ر,B005"}. Ayet önce "gayr" ile bir "değil" der, sonra {ar:وَلَا, tr:ve lâ, gloss:ve ... de değil, source:1:7} ile ikinci bir "değil" ekler. Bu ikinci "lâ" olmasaydı, sapanlar gazaba uğrayanların ikinci bir adı gibi okunabilirdi. Olumsuzluk yenilenince iki ayrı topluluk ve iki ayrı tehlike ortaya çıkar. "Gayri" kelimesi esrelidir ve "ellezîne"ye bağlanır. Nimet verilenler böylece ne olduklarıyla olduğu kadar ne olmadıklarıyla da tarif edilir.

## Uzatılan el ve sonuna kadar götürülen iyilik

[¶10] Türkçede "nimet" çoğu zaman sofradaki ekmeğe, yiyeceğe daralmıştır. Arapçada ise bir elin uzanmasıdır: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanî'atü ve'l-minnetü ve mâ en'ame bihî aleyk, gloss:nimet eldir, yapılan iyiliktir, lütuftur, sana verilen şeydir, source:"ن ع م,B001"}. Nimet vermek, iyiliği yerine ulaştırmaktır: {ar:الإنعام إيصال الإحسان إلى الغير, tr:el-in'âmü îsâlü'l-ihsâni ile'l-gayr, gloss:in'âm, iyiliği başkasına ulaştırmaktır, source:"ن ع م,B001"}. Aynı fiil bir işi artırmayı, ileri götürmeyi de anlatır: {ar:فعل كذا وأنعم أي زاد, tr:feale kezâ ve en'ame, gloss:şunu yaptı ve daha da artırdı, source:"ن ع م,B010"}. Bunun gündelik bir örneği de vardır: {ar:ودققت دواء فأنعمت دقه أي بالغت وزدت, tr:ve dekaktü devâen fe-en'amtü dakkahû, gloss:bir ilaç dövdüm ve onu iyice, inceden inceye dövdüm, source:"ن ع م,B010"}. İlacı döven el, iş bitti sanılan yerde durmaz, toz incelinceye kadar devam eder. Ayetteki "en'amte" "nimet verdin" demektir. Yanında, iyiliği yarım bırakmayan bu el duyulur.

[¶11] Kur'an nimetin tamamlanmasını yola iletmekle birlikte anar. Peygambere apaçık bir fetih verildiği bildirildikten {source:48:1} sonra şu söylenir: {ar:وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve yütimme ni'metehû aleyke ve yehdiyeke sırâtan müstakîmâ, gloss:sana nimetini tamamlasın ve seni dosdoğru bir yola iletsin, source:48:2}. Fâtiha'nın altıncı ve yedinci ayetlerindeki iki istek burada tek cümlededir. Nimetin bir yol boyunca, bir insan dizisi üzerinden aktığını da Yakup söyler. Oğlu Yusuf ona gördüğü rüyayı anlatınca şöyle der: {ar:وَيُتِمُّ نِعْمَتَهُۥ عَلَيْكَ وَعَلَىٰٓ ءَالِ يَعْقُوبَ كَمَآ أَتَمَّهَا عَلَىٰٓ أَبَوَيْكَ مِن قَبْلُ إِبْرَٰهِيمَ وَإِسْحَٰقَ, tr:ve yütimmü ni'metehû aleyke ve alâ âli Ya'kûbe kemâ etemmehâ alâ ebeveyke min kablü İbrâhîme ve İshâk, gloss:daha önce ataların İbrahim'e ve İshak'a tamamladığı gibi, nimetini sana ve Yakup ailesine de tamamlayacak, source:12:6}. Fâtiha'daki "kendilerine nimet verdiklerin" sözü de böyle bir öncekiler dizisine bakar. İbrahim'in kendisi ise nimete verilen cevapla anılır: {ar:شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:şâkiran li-en'umih, ictebâhü ve hedâhü ilâ sırâtın müstakîm, gloss:O'nun nimetlerine şükrederdi; Allah onu seçti ve dosdoğru bir yola iletti, source:16:121}.

[¶12] Kökün en somut kullanımları bir yumuşaklığa çıkar: {ar:نعم الشيء صار ناعما لينا, tr:neume'ş-şey'ü, gloss:şey yumuşadı, narinleşti, source:"ن ع م,B002"}. Hayat için de aynı söz kullanılır: {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi hüsnühû ve gadâratüh, gloss:hayatın nimeti onun güzelliği ve tazeliğidir, source:"ن ع م,B002"}. Çocuklarını bolluk içinde büyüten babaya {ar:نعم فلان أولاده ترفهم, tr:na''ame fülânün evlâdehû, gloss:falanca çocuklarını rahat içinde büyüttü, source:"ن ع م,B002"} denir. Devekuşunun adı bile bu yumuşaklıktan gelir: {ar:النعامة معروفة لنعمة ريشها, tr:en-neâmetü ma'rûfetün li-nu'meti rîşihâ, gloss:devekuşu tüylerinin yumuşaklığıyla bilinir, source:"ن ع م,B006"}. Güney rüzgârı da en ıslak ve en yumuşak rüzgâr olduğu için bu kökten bir ad alır: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-nu'âmâ rîhu'l-cenûb, li-ennehâ eballü'r-riyâhi ve ertabühâ, gloss:nu'âmâ güney rüzgârıdır, çünkü rüzgârların en ıslak ve nemli olanıdır, source:"ن ع م,B009"}. Göze gelen dinginliğe de {ar:نعمة العين قرتها, tr:nu'metü'l-ayni kurratühâ, gloss:gözün nimeti, onun serinleyip dinginleşmesidir, source:"ن ع م,B013"} derlerdi. Bu kullanımların ortak işleyişi, sertliğin yumuşamasıdır: İnsanı sürtüp yormayan bir hayat, teni okşayan bir rüzgâr, yanmayı bırakan bir göz. Bu yumuşaklığın Kur'an'da bir yüze yerleştiği sıfat, "en'amte" ile aynı köktendir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhün yevmeizin nâime, gloss:o gün bazı yüzler yumuşamış, nimet içindedir, source:88:8}. Surenin rıza ve gazap sahnesi bu yüzü öbür yüzün karşısına koyar.

[¶13] Yolcunun yolda bulduğu dinlenme de bu kökle anılır. Bir yere varıp orayı kendine uygun bulan ve orada kalan biri şöyle der: {ar:أتيت أرضا فنعمتني أي وافقتني وأقمت بها, tr:eteytü arden fe-neametnî, gloss:bir yere geldim, orası bana uydu ve orada kaldım, source:"ن ع م,B011"}. Devekuşunun dik duruşuna benzetilen şeylerin hepsi de yolcunun işine yarar: {ar:النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة, tr:en-neâmetü'l-mizalletü fi'l-cebeli ve alâ re'si'l-bi'r, gloss:neâme, dağda ve kuyu başında kurulan gölgeliktir; biçimi devekuşuna benzediği için bu adı almıştır, source:"ن ع م,B007"}. Kuyunun ağzındaki iki direğin üstüne enlemesine yatırılan kirişin adı da aynıdır: {ar:النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر, tr:en-neâmetü'l-haşebetü'l-mu'terıdatü ale'z-zürnûkayn ve'n-neâim menzilün min menâzili'l-kamer, gloss:neâme, iki direğin üstüne enlemesine konan kiriştir; neâim de Ay'ın konaklarından biridir, source:"ن ع م,B007"}. Bu kiriş su çekmenin taşıyıcısıdır, çünkü kova ona asılan makarayla iner ve çıkar. Makaranın adı altıncı ayetteki "müstakîm" ile aynı köktendir. Surenin su sahnesi kirişle makarayı kuyunun ağzında buluşturur. Gölgelik, kuyu kirişi, gece gökte bir konak: "Nimet verdin" sözünün yanında, yol boyunca başı gölgeleyen, suyu çeken ve geceyi bölen şeyler duyulur.

[¶14] Aynı kök övgü sözünü de verir: {ar:نعم كلمة تستعمل في المدح بإزاء بئس, tr:ni'me kelimetün tüsta'melü fi'l-medhi bi-izâi bi'se, gloss:ni'me, bi'se'nin karşısında övgü için kullanılan kelimedir, source:"ن ع م,B003"}. Nimet ailesinde iyiliğin yanında beğeni de vardır. Ayetin ikinci topluluğunu anan kelime ise tam bunun karşısındadır.

## Aynı "aleyhim": nimetin değiştiği yer

[¶15] Ayette iyilik de gazap da aynı edatla iner: "aleyhim", yani "onların üzerine". İki topluluğu ayıran "gayr" kelimesi ise "başka olmak" ile "değişmek"in birlikte yaşadığı bir köktendir: {ar:الاسم من قولك غيرت الشيء فتغير, tr:ğayyertü'ş-şey'e fe-teğayyer, gloss:şeyi değiştirdim, o da değişti, source:"غ ي ر,B003"}. Durum değiştirmek için de {ar:تغير فلان عن حاله, tr:teğayyere fülânün an hâlih, gloss:falanca eski hâlinden çıkıp başka oldu, source:"غ ي ر,B003"} denir. Bu bir kelime oyunu değildir, kök birliğidir. "Başka" kelimesiyle "başkalaşmak" fiili aynı kök harflerinden kurulur. Bu ayette yalnızca "başka" anlamı işler. Yine de iki topluluğu ayıran çizgi, kendi kökünde bir şeyin başka bir şeye dönüşebileceğini de taşır.

[¶16] Kur'an bu dönüşümü, ayetin kelimelerini tek bir cümlede bir araya getirerek anlatır. Firavun ailesinin ve onlardan öncekilerin Allah'ın ayetlerini inkâr ettikleri ve günahları yüzünden yakalandıkları anlatıldıktan {source:8:52} sonra sebep söylenir: {ar:ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًۭا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ, tr:zâlike bi-ennallâhe lem yekü mugayyiran ni'meten en'amehâ alâ kavmin hattâ yugayyirû mâ bi-enfüsihim, gloss:bu, Allah'ın bir topluluğa verdiği nimeti, onlar kendi içlerindekini değiştirmedikçe değiştirmemesindendir, source:8:53}. "Nimet", "en'ame", "alâ" ve "gayr" kökü burada aynı cümlededir. Nimet bir kez inince kalıcı bir soy niteliği olmaz. Onu alanların içi değiştiğinde nimet de değişir. Aynı ilke başka bir yerde daha genel söylenir: {ar:إِنَّ ٱللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ, tr:innallâhe lâ yugayyiru mâ bi-kavmin hattâ yugayyirû mâ bi-enfüsihim, gloss:bir topluluk kendi içindekini değiştirmedikçe Allah onların durumunu değiştirmez, source:13:11}. Bu değişimin sebebi bazen nimetin kendisidir: {ar:وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ, tr:ve izâ en'amnâ ale'l-insâni a'rada ve neâ bi-cânibih, gloss:insana nimet verdiğimizde yüz çevirir ve kendi yanına doğru uzaklaşır, source:17:83}. Nimet verilen insan, nimetin içinden yoldan sapar.

[¶17] Kur'an bu geçişi bir halkın hikâyesinde adım adım gösterir. İsrailoğullarına Fâtiha'daki fiilin birinci şahıs hâliyle seslenilir: {ar:ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ, tr:üzkürû ni'metiye'lletî en'amtü aleyküm, gloss:size verdiğim nimetimi hatırlayın, source:2:40}. Birkaç ayet sonra aynı halk çölde tek tip yiyeceğe dayanamaz ve topraktan sebze ister. Musa onlara şöyle sorar: {ar:أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ, tr:e-testebdilûne'llezî hüve ednâ bi'llezî hüve hayr, gloss:daha iyi olanı daha düşük olanla mı değiştirmek istiyorsunuz, source:2:61}. Ayetin sonunda şu söylenir: {ar:وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ, tr:ve bâû bi-gadabin minallâh, gloss:Allah'tan bir gazapla döndüler, source:2:61}. Aynı insanlar önce "en'amtü aleyküm" cümlesinin, sonra gazap cümlesinin konusu olur. Başka bir anlatımda geçiş daha da sıkışıktır. Allah onlara düşmandan kurtarıldıklarını ve kendilerine {ar:وَنَزَّلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ, tr:ve nezzelnâ aleykümü'l-menne ve's-selvâ, gloss:üzerinize kudret helvasıyla bıldırcın indirdik, source:20:80} diye hatırlatır, ardından uyarır: {ar:كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَلَا تَطْغَوْا۟ فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِى, tr:külû min tayyibâti mâ razaknâküm ve lâ tatgav fîhi fe-yehılle aleyküm gadabî, gloss:size verdiğimiz rızkın temizlerinden yiyin, onda azgınlık etmeyin, yoksa gazabım üzerinize iner, source:20:81}. Hemen ardından kapı yeniden açılır: {ar:وَإِنِّى لَغَفَّارٌۭ لِّمَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا ثُمَّ ٱهْتَدَىٰ, tr:ve innî le-gaffârun li-men tâbe ve âmene ve amile sâlihan sümme'htedâ, gloss:tövbe eden, iman eden, iyi iş yapan ve sonra yolunu bulan için ben çok bağışlayıcıyım, source:20:82}. Aynı hikâye devam ederken Musa, halkını geride bırakıp Rabbine acele ettiğini ve onların {ar:قَالَ هُمْ أُو۟لَآءِ عَلَىٰٓ أَثَرِى وَعَجِلْتُ إِلَيْكَ رَبِّ لِتَرْضَىٰ, tr:kâle hüm ülâi alâ eserî ve aciltü ileyke rabbi li-terdâ, gloss:onlar işte arkamdan, benim izimdeler; Rabbim, hoşnut olasın diye sana acele ettim, source:20:84} olduğunu söyler. Ona şu cevap verilir: {ar:وَأَضَلَّهُمُ ٱلسَّامِرِىُّ, tr:ve edallehümü's-Sâmiriyy, gloss:Sâmirî onları yoldan çıkardı, source:20:85}. Musa halkına öfkeli döner ve sorar: {ar:أَمْ أَرَدتُّمْ أَن يَحِلَّ عَلَيْكُمْ غَضَبٌۭ مِّن رَّبِّكُمْ, tr:em eradtüm en yehılle aleyküm gadabün min rabbiküm, gloss:yoksa Rabbinizden bir gazabın üzerinize inmesini mi istediniz, source:20:86}. Birkaç ayetlik bu anlatıda yedinci ayetin üç durumu sırayla görülür: üzerlerine inen nimet, önden gidenin izinde yürüyen bir topluluk, yoldan çıkarılış ve inmesinden korkulan gazap. Kur'an'ın kendi anlatısı, ayetin bir soyu değil bir durumu adlandırdığını gösterir. Aynı topluluk nimetin de gazabın da cümlesine girebilir. Tövbe edip yolunu bulan da yeniden geri dönebilir.

[¶18] "Gayr" kökünde değişim her zaman kötüye doğru değildir. Esreli "gıyre", aileye getirilen erzaktır: {ar:الغِيرة بالكسر: الميرة, tr:el-gıyratü bi'l-kesr: el-mîre, gloss:esreli gıyre erzaktır, source:"غ ي ر,B001"}. Kuraklık çeken bir halk için {ar:غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم, tr:gârahümullâhü teâlâ bi'l-gays, gloss:Allah onlara yağmur verdi, yani durumlarını düzeltti ve onlara yarar dokundurdu, source:"غ ي ر,B001"} denir. Yorgun bir yolcuya yardım eden için de aynı fiil kullanılır: {ar:حط عنه رحله وأصلح من شأنه, tr:hatta anhü rahlehû ve asleha min şe'nih, gloss:devesinin yükünü indirdi ve hâlini düzeltti, source:"غ ي ر,B001"}. Durumu değiştirmek burada yükü yolcunun sırtından indirmektir. Kökte bir şeyin yerine başka bir şey koymak da vardır. Kısas gereken bir yerde {ar:قود فغير إلى الدية, tr:kavedün fe-güyyira ile'd-diye, gloss:kısas vardı, kan bedeline çevrildi, source:"غ ي ر,B003"} denir ve kan bedelinin kendisine de bu kökten ad verilir: {ar:غارني الرجل إذا وداك من الدية, tr:gâranî'r-racülü, gloss:adam bana kan bedelini ödedi, source:"غ ي ر,B002"}. Dördüncü ayetteki "dîn" kelimesi hesap ve karşılık demektir. Surenin hesap sahnesi bu bedeli o kelimenin yanına koyar. Üstünlü "gayre" ise sınır çizmenin duygusudur: {ar:الغَيرة بالفتح مصدر قولك غار الرجل على أهله, tr:el-gayretü bi'l-feth, gâra'r-racülü alâ ehlih, gloss:gayre, adamın ailesini kıskanıp başkalarından sakınmasıdır, source:"غ ي ر,B004"}. Ayette "başkası" diye bir sınır çizen kelime, kendi kökünde kendine ait olanı başkasından koruyan adamı da anar.

## Gazabın dokusu: yığılan kaya, kızaran deri, katlanan kalkan

[¶19] Gazap, hoşnutsuzluğun sertleşmesidir: {ar:الغضب ضد الرضا, tr:el-gadabu ziddü'r-ridâ, gloss:gazap rızanın zıddıdır, source:"غ ض ب,B001"}. Bedendeki işleyişi de şöyle anlatılır: {ar:الغضب ثوران دم القلب إرادة الانتقام, tr:el-gadabu sevrânü demi'l-kalbi irâdete'l-intikâm, gloss:gazap, öç alma isteğiyle kalbin kanının kaynamasıdır, source:"غ ض ب,B001"}. Kelime Allah için söylendiğinde bu bedensel kaynama kastedilmez: {ar:وإذا وصف الله تعالى به فالمراد به الانتقام, tr:ve izâ vusıfallâhu teâlâ bihî fe'l-murâdü bihi'l-intikâm, gloss:Allah bununla nitelendiğinde kastedilen, karşılık verip cezalandırmaktır, source:"غ ض ب,B001"}. Ayetteki "el-magdûbi aleyhim" ifadesi bu karşılığın indiği kimseleri anlatır.

[¶20] Kelimenin somut akrabaları bir sertleşme ve kalınlaşma dünyası kurar. Dağda üst üste yığılmış sert kayaya bu kökten ad verilir: {ar:الغضبة الصخرة الصلبة المتراكمة في الجبل, tr:el-gadbetü's-sahratü's-sulbetü'l-mütarâkimetü fi'l-cebel, gloss:gadbe, dağda üst üste yığılmış sert kayadır, source:"غ ض ب,B004"}. Derisi kalın ve rengi koyu kızıl olan adam için {ar:رجل غضب إذا كان أحمر غليظا, tr:racülün gadb, gloss:kızıl ve kalın yapılı adam, source:"غ ض ب,B005"} derlerdi. Göz çevresinin şişmesi de aynı fiille söylenir: {ar:غضبت عين الرجل إذا ورم ما حولها, tr:gadibet aynü'r-racül, gloss:adamın gözünün çevresi şişti, source:"غ ض ب,B006"}. Kalkan yapımında da kelimenin bir karşılığı vardır: {ar:الغضبة قطعة من جلد البعير يطوى بعضها على بعض ويجعل شبيها بالدرقة, tr:el-gadbetü kıt'atün min cildi'l-ba'îr, gloss:gadbe, deve derisinden kesilip kat kat katlanan ve kalkana benzetilen parçadır, source:"غ ض ب,B008"}. Kaplumbağanın kabuğuna da {ar:يسمى جلد السلحفاة الغضب, tr:yüsemmâ cildü's-sülahfâti'l-gadab, gloss:kaplumbağanın derisine gadab denir, source:"غ ض ب,B008"} denir. Bu nesnelerin hepsi aynı biçimde işler: Bir yüzey kat kat kalınlaşır, sertleşir ve içine bir şey geçmez hâle gelir. Yığılan kaya, kalınlaşan deri, şişen göz kapağı, katlanan kalkan ve kabuk hep böyledir. Nimet ailesinin yumuşayan teni, okşayan rüzgârı ve serinleyen gözü ise öbür uçtadır. Ayetin iki topluluğu kendi anlamlarında nimet ve gazap alır. Kelimelerin akrabalarında ise biri yumuşamanın, öbürü katılaşmanın dilinden konuşur.

[¶21] Kur'an gazabı bir insanın bedeninde de gösterir. Musa Tur'dan döndüğünde halkını buzağıya tapar bulur. Öfkeli ve kederlidir: {ar:وَأَلْقَى ٱلْأَلْوَاحَ وَأَخَذَ بِرَأْسِ أَخِيهِ يَجُرُّهُۥٓ إِلَيْهِ, tr:ve elka'l-elvâha ve ehaze bi-re'si ahîhi yecurruhû ileyh, gloss:levhaları bıraktı ve kardeşinin başından tutup onu kendine çekti, source:7:150}. Kardeşi açıklama yapınca kendisi ve kardeşi için bağışlanma diler. Ardından gazap bir konuşan gibi susar: {ar:وَلَمَّا سَكَتَ عَن مُّوسَى ٱلْغَضَبُ أَخَذَ ٱلْأَلْوَاحَ ۖ وَفِى نُسْخَتِهَا هُدًۭى وَرَحْمَةٌۭ, tr:ve lemmâ sekete an Mûse'l-gadabü ehaze'l-elvâh, ve fî nüshatihâ hüden ve rahme, gloss:Musa'nın öfkesi susunca levhaları aldı; onların yazısında yol gösterme ve rahmet vardı, source:7:154}. Öfke yere bıraktırdığı şeyi, susunca yeniden aldırır. Alınan şey de hidayet ve rahmettir. Aynı sahnede buzağıyı edinenler için Allah'ın hükmü de söylenir: {ar:سَيَنَالُهُمْ غَضَبٌۭ مِّن رَّبِّهِمْ, tr:se-yenâlühüm gadabün min rabbihim, gloss:onlara Rablerinden bir gazap erişecek, source:7:152}. Hemen ardından şu gelir: {ar:إِنَّ رَبَّكَ مِنۢ بَعْدِهَا لَغَفُورٌۭ رَّحِيمٌۭ, tr:inne rabbeke min ba'dihâ le-gafûrun rahîm, gloss:kötülük yapıp sonra tövbe eden ve iman edenler için, bunun ardından Rabbin çok bağışlayıcı ve merhametlidir, source:7:153}. Gazap bir kapı değil, bir eşiktir.

[¶22] Yedinci ayetin iki olumsuz topluluğu Kur'an'da bir cümlede de buluşur. Peygambere, müminleri iman ettikleri için ayıplayanlara Allah katında daha kötü bir karşılığı bildirmesi emredilir: {ar:مَن لَّعَنَهُ ٱللَّهُ وَغَضِبَ عَلَيْهِ, tr:men leanehullâhü ve gadibe aleyh, gloss:Allah'ın lanetlediği ve gazap ettiği kimse, source:5:60}. Söz şöyle biter: {ar:أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ, tr:ülâike şerrun mekânen ve edallü an sevâi's-sebîl, gloss:onların yeri daha kötüdür ve yolun ortasından daha da uzağa sapmışlardır, source:5:60}. Gazap ve yolunu yitirmek burada aynı kimselerin üzerindedir. Fâtiha ikisini "ve lâ" ile ayırır, ama birinin öbürüne açılabileceği bu ayette görülür.

## Yolunu bulamayan, suya karışan süt

[¶23] "Dâll" önce yolunu bulamayandır: {ar:ضل في الأرض إذا لم يهتد للسبيل, tr:dalle fi'l-ard, gloss:açık arazide yolu bulamadı, source:"ض ل ل,B001"}. Doğru hattan yana sapan herkese de bu ad verilir: {ar:كل جائر عن القصد ضال, tr:küllü câirin ani'l-kasdi dâll, gloss:doğru hattan yana sapan herkes dâldır, source:"ض ل ل,B001"}. Kelime, surenin istek kelimesinin tam karşısındadır: {ar:الضلال ضد الهدى, tr:ed-dalâlü ziddü'l-hüdâ, gloss:dalâl hidayetin zıddıdır, source:"ض ل ل,B001"}. Altıncı ayetin "ihdinâ"sıyla açılan istek, karşıtının adıyla kapanır. Kur'an "câir" kelimesini yolun kendisi için de kullanır: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve alellâhi kasdü's-sebîli ve minhâ câir, gloss:doğru hattaki yol Allah'a varır; yollardan bazısı ise yana sapar, source:16:9}.

[¶24] Yitmek bir yeri bulamamak da olabilir: {ar:ضللت المسجد والدار إذا لم تهتد لهما, tr:dalaltü'l-mescide ve'd-dâr, gloss:mescidi ve evi bulamadım, source:"ض ل ل,B003"}. Yolu kaybeden kişi, sonunda varacağı kapıyı da kaybeder. Kaybolan bazen insanın kendisidir: {ar:ذهب فلان ضلة إذا لم يدر أين ذهب, tr:zehebe fülânün dılleten, gloss:falanca gitti, nereye gittiği bilinmedi, source:"ض ل ل,B003"}. Bazen hakkı aranmayan bir candır: {ar:ذهب دمه ضلة إذا لم يثأر به, tr:zehebe demühû dılleten, gloss:kanı boşa gitti, öcü alınmadı, source:"ض ل ل,B003"}. Bazen de hafızadan çıkan bir şeydir: {ar:ضللت الشيء أنسيته, tr:dalaltü'ş-şey'e, gloss:şeyi unuttum, source:"ض ل ل,B004"}. Kur'an bu son anlamı borç ayetinde kullanır. İki kadın tanık istenir, gerekçe de şudur: {ar:أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ, tr:en tadılle ihdâhümâ fe-tüzekkira ihdâhüme'l-uhrâ, gloss:biri unutursa öbürü ona hatırlatsın diye, source:2:282}. Burada dalâlin çaresi bir yanındaki kişidir. Unutanın yanında hatırlatan biri durur.

[¶25] Kur'an yolunu yitirmiş olanı da yanındakilerle birlikte gösterir. Peygambere, Allah yola ilettikten sonra fayda da zarar da vermeyen şeylere yönelip geri dönmenin kime benzeyeceğini söylemesi emredilir: {ar:كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا, tr:kellezi'stehvethü'ş-şeyâtînü fi'l-ardı hayrâne lehû ashâbün yed'ûnehû ile'l-hüde'tinâ, gloss:şeytanların yeryüzünde aklını çelip şaşkın bıraktığı, arkadaşlarının ise "bize gel" diye doğru yola çağırdığı kimse gibi, source:6:71}. Açık arazide şaşkın kalan biri vardır, yolun üzerinde de onu çağıran arkadaşlar. Fâtiha'nın "onların yolu" dediği yol, böyle çağıran arkadaşları olan bir yoldur.

[¶26] Kelimenin bir de ayette kendisi bulunmayan, yalnızca yanında duyulan bir anlamı vardır: Bir şeyin içine karışıp gözden yitmesi. {ar:ضل اللبن في الماء ثم استهلك, tr:dalle'l-lebenü fi'l-mâi sümme'stühlik, gloss:süt suya karıştı, sonra içinde yitip gitti, source:"ض ل ل,B002"}. Süt yok olmamıştır. Su onu içine almış, süt de artık ayırt edilemeyecek kadar dağılmıştır. Ölünün gömülmesi de bu fiille söylenir: {ar:أضل الميت إذا دفن, tr:udılle'l-meyyit, gloss:ölü gömüldü, gözden kaldırıldı, source:"ض ل ل,B002"}. Kökün aslının da bu olduğu söylenir: {ar:أصل الضلال الغيبوبة, tr:aslü'd-dalâli'l-gaybûbe, gloss:dalâlin aslı gözden kaybolmaktır, source:"ض ل ل,B002"}. Dirilişi inkâr edenler bu anlamı kendi sorularında kullanır: {ar:أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ أَءِنَّا لَفِى خَلْقٍۢ جَدِيدٍۭ, tr:e-izâ dalelnâ fi'l-ardı e-innâ le-fî halkın cedîd, gloss:toprağa karışıp kaybolduğumuzda mı yeniden yaratılacağız, source:32:10}. "Yolunu yitirenler" sözünün yanında, kendi biçimini kaybedip çevresine karışan bir şey duyulur: suya karışmış süt, toprağa karışmış beden. Yoldan çıkmak bu görüntüde bir yönü kaybetmekle kalmaz, ayırt edilebilir bir yolcu olmaktan çıkmaktır.

[¶27] Kur'an'da en çarpıcı olan, "dâll" kelimesini peygamberlerin kendileri için kullanmasıdır. Allah Peygambere yetimken barındırıldığını hatırlatır {source:93:6} ve şöyle der: {ar:وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ, tr:ve vecedeke dâllen fe-hedâ, gloss:seni yolunu arar buldu da yola iletti, source:93:7}. Musa'ya Firavun {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nürabbike fînâ velîdâ, gloss:seni küçükken aramızda büyütmedik mi, source:26:18} diye sorar ve yaptığı işi yüzüne vurur. Musa cevap verir: {ar:قَالَ فَعَلْتُهَآ إِذًۭا وَأَنَا۠ مِنَ ٱلضَّآلِّينَ, tr:kâle fealtühâ izen ve ene mine'd-dâllîn, gloss:dedi ki: onu yaptığımda ben yolunu bilmeyenlerdendim, source:26:20}. Ardından {ar:فَوَهَبَ لِى رَبِّى حُكْمًۭا وَجَعَلَنِى مِنَ ٱلْمُرْسَلِينَ, tr:fe-vehebe lî rabbî hukmen ve cealenî mine'l-mürselîn, gloss:Rabbim bana hikmet verdi ve beni elçilerden kıldı, source:26:21} der. İbrahim de geceleyin yükselip batan aya bakıp şunu söyler: {ar:لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ, tr:le-in lem yehdinî rabbî le-ekûnenne mine'l-kavmi'd-dâllîn, gloss:Rabbim beni yola iletmezse yolunu yitirmiş topluluktan olurum, source:6:77}. Fâtiha'nın son kelimesi, uzak ve yabancı bir topluluğun adı değildir. Peygamberlerin "ben de onlardandım" ya da "onlardan olurum" dediği bir hâldir. Bu yüzden dua bu kelimeyle biter: Hidayet istenmezse, istenen yolun karşısındaki ad herkesin adı olabilir.

## İki türlü gözden kaybolmak

[¶28] "Sırat" kelimesinin kökü de bir gözden kayboluşu anlatır, ama dalâlinkinden başka türlüsünü. Yemeği yutmak bu kökle söylenir: {ar:سرطت الطعام إذا بلعته لأنه إذا سرط غاب, tr:seratu't-taâme izâ bele'tüh, gloss:yemeği yuttum, çünkü yutulan yemek gözden kaybolur, source:"ص ر ط,B002"}. Kolayca kayıp giden yumuşak bir tatlıya da bu yüzden bu kökten ad verilir: {ar:السرطراط على فعلال الفالوذ لأنه يسترط, tr:es-sirtirât, gloss:sirtirât, boğazdan kayıp giden pelte kıvamlı tatlıdır, source:"ص ر ط,B002"}. Yutulan lokma boğazdan geçer ve gözden çıkar, ama yok olmaz. Bedenin içinde gitmesi gereken yere gider. Yolun da bu adı aynı sebeple aldığı söylenir: {ar:السراط مشتق من ذلك لأن الذاهب فيه يغيب, tr:es-sirâtu müştakkun min zâlike li-enne'z-zâhibe fîhi yegîb, gloss:sirat bundan türemiştir, çünkü yolda giden gözden kaybolur, source:"ص ر ط,B001"}. Yolcu ilerler, bakanın gözünden çıkar, ama bir yönü ve bir varış yeri vardır. Aynı kökten bir ad da duraksamadan kesip geçen kılıca verilir: {ar:والسراط السيف القاطع الماضي في الضريبة, tr:ve's-sirâtu's-seyfü'l-kâtı'u'l-mâdî fi'd-darîbe, gloss:sirat, vuruşta kesip içinden geçen keskin kılıçtır, source:"ص ر ط,B003"}. Bu kılıç yüzeyde takılıp kalmaz, vurduğu yerin içinden geçip gider.

[¶29] Böylece yedinci ayetin ilk ve son kelimeleri gözden kaybolmanın iki türünü taşır. Sırat, yolcuyu yutup götüren ve bir yere ulaştıran bir geçiştir. Dalâl ise suya karışan süt gibi, gidilen yerin bilinmediği bir dağılmadır. İkisi de "gâbe" fiiliyle anlatılır. Aralarındaki fark, kaybolanın bir yere varıp varmamasıdır. Ayet bu yüzden yalnızca "doğru"yu "yanlış"ın karşısına koymaz. Bir gidişin karşısına başka bir gidişi koyar. Birinin sonu vardır, öbürünün yoktur.

## Sürüden kopan deve

[¶30] Ayetin üç topluluğunu anan kelimelerin her birinin ailesinde bir deve vardır. Bu, kelimelerin anlamında değil, yanlarında duyulan bir dizidir. "En'amte" kelimesinin kökü develere ad verir, çünkü onlarda iyilik vardır: {ar:النعم الإبل لما فيه من الخير والنعمة, tr:en-neamü'l-ibilü li-mâ fîhi mine'l-hayri ve'n-ni'me, gloss:neam develerdir, çünkü onlarda hayır ve nimet vardır, source:"ن ع م,B005"}. "El-magdûb" kelimesinin ailesinde asık suratlı, huysuz bir dişi deve vardır: {ar:ناقة غضوب عبوس, tr:nâkatün gadûbün abûs, gloss:gadûb dişi deve, asık suratlı devedir, source:"غ ض ب,B007"}. Aynı ad, iri bir yılana da verilir: {ar:الغضوب الحية العظيمة, tr:el-gadûbü'l-hayyetü'l-azîme, gloss:gadûb, iri yılandır, source:"غ ض ب,B007"}. "Ed-dâllîn" kelimesinin ailesinde ise sahibinden kopmuş deve vardır: {ar:أضللت بعيري إذا ذهب منك, tr:edlaltü ba'îrî, gloss:devemi yitirdim, elimden çıkıp gitti, source:"ض ل ل,B003"}. Böyle bir deve şöyle tanımlanır: {ar:الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء, tr:ed-dâlletü mine'l-ibili mâ yebkâ bi-medî'atin lâ yu'rafü rabbühâ, gloss:dâlle, ıssız bir yerde kalan ve sahibi bilinmeyen devedir; erkeği de dişisi de böyledir, source:"ض ل ل,B005"}. Sürüdeki hayırlı deve, huysuz ve suratsız deve, sahibinden kopup ıssızda kalan deve: Ayet, bu kelimelerin yanında bir sürünün üç hâlini de taşır. Başıboş devenin tanımındaki "rab" kelimesi ikinci ayetteki "Rab" ile aynı kelimedir. Surenin sürü sahnesi bu başıboş deveyi, ikinci ve dördüncü ayetlerin sahiplik adlarına bu tanım üzerinden bağlar. Develer arasından Harem'e götürülen kurbanlığın sahnesi ise altıncı ayetteki "ihdinâ" kelimesinin akrabalarıyla kurulur.

[¶31] Kur'an da sürüyle yolunu yitirmeyi yan yana koyar. Kalpleri olup kavramayan, gözleri olup görmeyen kimseler için şöyle der: {ar:أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ, tr:ülâike ke'l-en'âmi bel hüm edall, gloss:onlar hayvanlar gibidir, hatta daha da şaşkındırlar, source:7:179}. Başka bir yerde aynı söz yola bağlanır: {ar:إِنْ هُمْ إِلَّا كَٱلْأَنْعَٰمِ ۖ بَلْ هُمْ أَضَلُّ سَبِيلًا, tr:in hüm illâ ke'l-en'âm, bel hüm edallü sebîlâ, gloss:onlar hayvanlardan başka bir şey değildir, hatta yolca daha da şaşkındırlar, source:25:44}. "En'âm" ile "edall", ayetin ilk nimet kelimesinin kökü ile son kelimesinin kökü, burada aynı cümlededir. Sürüden kopan hayvanın en azından bir sahibi ve bir sürüsü vardır. Bu ayetlerdeki insan ise yolunu ondan da çok yitirmiştir.

[¶32] Kökün bir deyimi de topluluğun dağılmasını anlatır. Bir kavim göçüp gittiğinde ya da birliği bozulduğunda {ar:شالت نعامتهم إذا تفرقوا, tr:şâlet neâmetühüm, gloss:devekuşları kalktı, yani dağılıp gittiler, source:"ن ع م,B008"} derlerdi. Aynı deyimin iki yüzü vardır: {ar:خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم, tr:haffet neâmetühüm... ve şâlet neâmetühüm, gloss:yürüyüş onları alıp götürdü dendiğinde yolculuk sürüp gitmiştir; devekuşları kalktı dendiğinde ise sözleri bölünmüş, güçleri gitmiştir, source:"ن ع م,B008"}. Bir yerde yürüyüş topluluğu birlikte taşır, öbür yerde topluluk dağılır. Kur'an aynı ikiliği yollar üzerinden anlatır. Rab bir dizi öğüdün sonunda şöyle der: {ar:وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ, tr:ve enne hâzâ sırâtî müstakîmen fettebi'ûh, gloss:bu benim dosdoğru yolumdur, ona uyun, source:6:153}. Ardından ekler: {ar:وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve lâ tettebi'u's-sübüle fe-teferraka biküm an sebîlih, gloss:başka yollara uymayın, yoksa sizi O'nun yolundan ayırıp dağıtırlar, source:6:153}. Fâtiha'nın istediği yol birlikte yürünen bir yoldur: "nimet verdiklerinin yolu", "onlar ne güzel yol arkadaşlarıdır". Bu yolun karşıtı, sürüden kopup ıssızda tek başına kalan devedir.

===== _commentary/v16/out/1_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: ṣirāṭa in 1:7 as badal of al-ṣirāṭ in 1:6
- memory: ghayri genitive, attached to alladhīna (descriptive)
- memory: lā after ghayr renews negation, separates the two groups
- memory: rafīq connoting travel companion ("yol arkadaşı")
- memory: vocalization nuʿāmā for النعامى
- memory: vocalizations ghaḍba / ghaḍb for rock, hide, red man
- memory: vocalization tanaʿʿamtu, naʿʿama (children)
- memory: literal sense of شالت as "rose/lifted"
- memory: sirṭirāṭ vowels inferred from stated fiʿlāl pattern
- memory: pulley (qāma) hanging from the beam, recalled from 1:6's root
- not written: naʿam "yes" as opposite of lā (B004) - wordplay with the ayah's lā, no theme it could ground
- not written: ghaḍiba li / ghaḍiba bi for living/dead (B002) - no bearing on the ayah
- not written: mughāḍib / Dhū'l-Nūn going off angry (B003, 21:87) - the anger is his own; swallowing link to ṣ-r-ṭ only an analogy
- not written: sirṭim, the wide-throated (B002) - vocalization uncertain, adds nothing to the swallowing image
- not written: hearts hardened like stones (2:74) - different root; only an analogy for the rock image
- not written: ostrich as a species (B006 beyond feather softness) - no work in any theme
- not written: Iblis lying in wait on the path (7:16) - belongs to the 1:6 road scene, not this ayah's words

===== passages not cited (347) =====
## strong (this ayah's own list) (56)

- (2:16) [listed for 1:7] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ فَمَا رَبِحَت تِّجَٰرَتُهُمْ وَمَا كَانُوا۟ مُهْتَدِينَ
- (3:51) [listed for 1:7] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (3:69) [listed for 1:7] وَدَّت طَّآئِفَةٌۭ مِّنْ أَهْلِ ٱلْكِتَٰبِ لَوْ يُضِلُّونَكُمْ وَمَا يُضِلُّونَ إِلَّآ أَنفُسَهُمْ وَمَا يَشْعُرُونَ
- (3:100) [listed for 1:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِن تُطِيعُوا۟ فَرِيقًۭا مِّنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ يَرُدُّوكُم بَعْدَ إِيمَٰنِكُمْ كَٰفِرِينَ
- (4:60) [listed for 1:7] أَلَمْ تَرَ إِلَى ٱلَّذِينَ يَزْعُمُونَ أَنَّهُمْ ءَامَنُوا۟ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ يُرِيدُونَ أَن يَتَحَاكَمُوٓا۟ إِلَى ٱلطَّٰغُوتِ وَقَدْ أُمِرُوٓا۟ أَن يَكْفُرُوا۟ بِهِۦ وَيُرِيدُ ٱلشَّيْطَٰنُ أَن يُضِلَّهُمْ ضَلَٰلًۢا بَعِيدًۭا
- (4:68) [listed for 1:7] [cited in ¶3] وَلَهَدَيْنَٰهُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (4:69) [listed for 1:7] [cited in ¶3] وَمَن يُطِعِ ٱللَّهَ وَٱلرَّسُولَ فَأُو۟لَٰٓئِكَ مَعَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ وَٱلصِّدِّيقِينَ وَٱلشُّهَدَآءِ وَٱلصَّٰلِحِينَ ۚ وَحَسُنَ أُو۟لَٰٓئِكَ رَفِيقًۭا
- (4:116) [listed for 1:7] إِنَّ ٱللَّهَ لَا يَغْفِرُ أَن يُشْرَكَ بِهِۦ وَيَغْفِرُ مَا دُونَ ذَٰلِكَ لِمَن يَشَآءُ ۚ وَمَن يُشْرِكْ بِٱللَّهِ فَقَدْ ضَلَّ ضَلَٰلًۢا بَعِيدًا
- (4:136) [listed for 1:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ ءَامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِى نَزَّلَ عَلَىٰ رَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِىٓ أَنزَلَ مِن قَبْلُ ۚ وَمَن يَكْفُرْ بِٱللَّهِ وَمَلَٰٓئِكَتِهِۦ وَكُتُبِهِۦ وَرُسُلِهِۦ وَٱلْيَوْمِ ٱلْءَاخِرِ فَقَدْ ضَلَّ ضَلَٰلًۢا بَعِيدًا
- (4:167) [listed for 1:7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ قَدْ ضَلُّوا۟ ضَلَٰلًۢا بَعِيدًا
- (4:175) [listed for 1:7] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَٱعْتَصَمُوا۟ بِهِۦ فَسَيُدْخِلُهُمْ فِى رَحْمَةٍۢ مِّنْهُ وَفَضْلٍۢ وَيَهْدِيهِمْ إِلَيْهِ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (5:16) [listed for 1:7] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (6:71) [listed for 1:7] [cited in ¶25] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:77) [listed for 1:7] [cited in ¶27] فَلَمَّا رَءَا ٱلْقَمَرَ بَازِغًۭا قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ
- (6:126) [listed for 1:7] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
- (6:153) [listed for 1:7] [cited in ¶32] وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَتَّقُونَ
- (6:161) [listed for 1:7] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (7:16) [listed for 1:7] قَالَ فَبِمَآ أَغْوَيْتَنِى لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ
- (7:86) [listed for 1:7] وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ وَتَصُدُّونَ عَن سَبِيلِ ٱللَّهِ مَنْ ءَامَنَ بِهِۦ وَتَبْغُونَهَا عِوَجًۭا ۚ وَٱذْكُرُوٓا۟ إِذْ كُنتُمْ قَلِيلًۭا فَكَثَّرَكُمْ ۖ وَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُفْسِدِينَ
- (8:53) [listed for 1:7] [cited in ¶16] ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًۭا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۙ وَأَنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (10:25) [listed for 1:7] وَٱللَّهُ يَدْعُوٓا۟ إِلَىٰ دَارِ ٱلسَّلَٰمِ وَيَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (10:32) [listed for 1:7] فَذَٰلِكُمُ ٱللَّهُ رَبُّكُمُ ٱلْحَقُّ ۖ فَمَاذَا بَعْدَ ٱلْحَقِّ إِلَّا ٱلضَّلَٰلُ ۖ فَأَنَّىٰ تُصْرَفُونَ
- (11:56) [listed for 1:7] إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (12:6) [listed for 1:7] [cited in ¶11] وَكَذَٰلِكَ يَجْتَبِيكَ رَبُّكَ وَيُعَلِّمُكَ مِن تَأْوِيلِ ٱلْأَحَادِيثِ وَيُتِمُّ نِعْمَتَهُۥ عَلَيْكَ وَعَلَىٰٓ ءَالِ يَعْقُوبَ كَمَآ أَتَمَّهَا عَلَىٰٓ أَبَوَيْكَ مِن قَبْلُ إِبْرَٰهِيمَ وَإِسْحَٰقَ ۚ إِنَّ رَبَّكَ عَلِيمٌ حَكِيمٌۭ
- (14:1) [listed for 1:7] الٓر ۚ كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِ رَبِّهِمْ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (14:3) [listed for 1:7] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (14:28) [listed for 1:7] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ بَدَّلُوا۟ نِعْمَتَ ٱللَّهِ كُفْرًۭا وَأَحَلُّوا۟ قَوْمَهُمْ دَارَ ٱلْبَوَارِ
- (15:41) [listed for 1:7] قَالَ هَٰذَا صِرَٰطٌ عَلَىَّ مُسْتَقِيمٌ
- (15:42) [listed for 1:7] إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌ إِلَّا مَنِ ٱتَّبَعَكَ مِنَ ٱلْغَاوِينَ
- (16:9) [listed for 1:7] [cited in ¶23] وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ ۚ وَلَوْ شَآءَ لَهَدَىٰكُمْ أَجْمَعِينَ
- (16:76) [listed for 1:7] وَضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلَيْنِ أَحَدُهُمَآ أَبْكَمُ لَا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَهُوَ كَلٌّ عَلَىٰ مَوْلَىٰهُ أَيْنَمَا يُوَجِّههُّ لَا يَأْتِ بِخَيْرٍ ۖ هَلْ يَسْتَوِى هُوَ وَمَن يَأْمُرُ بِٱلْعَدْلِ ۙ وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (17:9) [listed for 1:7] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
- (19:36) [listed for 1:7] وَإِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (19:43) [listed for 1:7] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (20:81) [listed for 1:7] [cited in ¶17] كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَلَا تَطْغَوْا۟ فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِى ۖ وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ
- (20:123) [listed for 1:7] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (22:54) [listed for 1:7] وَلِيَعْلَمَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّكَ فَيُؤْمِنُوا۟ بِهِۦ فَتُخْبِتَ لَهُۥ قُلُوبُهُمْ ۗ وَإِنَّ ٱللَّهَ لَهَادِ ٱلَّذِينَ ءَامَنُوٓا۟ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (23:73) [listed for 1:7] وَإِنَّكَ لَتَدْعُوهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (23:74) [listed for 1:7] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- (24:46) [listed for 1:7] لَّقَدْ أَنزَلْنَآ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ ۚ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (26:20) [listed for 1:7] [cited in ¶27] قَالَ فَعَلْتُهَآ إِذًۭا وَأَنَا۠ مِنَ ٱلضَّآلِّينَ
- (28:17) [listed for 1:7] قَالَ رَبِّ بِمَآ أَنْعَمْتَ عَلَىَّ فَلَنْ أَكُونَ ظَهِيرًۭا لِّلْمُجْرِمِينَ
- (30:29) [listed for 1:7] بَلِ ٱتَّبَعَ ٱلَّذِينَ ظَلَمُوٓا۟ أَهْوَآءَهُم بِغَيْرِ عِلْمٍۢ ۖ فَمَن يَهْدِى مَنْ أَضَلَّ ٱللَّهُ ۖ وَمَا لَهُم مِّن نَّٰصِرِينَ
- (36:61) [listed for 1:7] وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (37:23) [listed for 1:7] [cited in ¶2] مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ
- (37:118) [listed for 1:7] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (38:26) [listed for 1:7] يَٰدَاوُۥدُ إِنَّا جَعَلْنَٰكَ خَلِيفَةًۭ فِى ٱلْأَرْضِ فَٱحْكُم بَيْنَ ٱلنَّاسِ بِٱلْحَقِّ وَلَا تَتَّبِعِ ٱلْهَوَىٰ فَيُضِلَّكَ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّ ٱلَّذِينَ يَضِلُّونَ عَن سَبِيلِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۢ بِمَا نَسُوا۟ يَوْمَ ٱلْحِسَابِ
- (42:53) [listed for 1:7] صِرَٰطِ ٱللَّهِ ٱلَّذِى لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ أَلَآ إِلَى ٱللَّهِ تَصِيرُ ٱلْأُمُورُ
- (43:43) [listed for 1:7] فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ ۖ إِنَّكَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (43:64) [listed for 1:7] إِنَّ ٱللَّهَ هُوَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (56:92) [listed for 1:7] وَأَمَّآ إِن كَانَ مِنَ ٱلْمُكَذِّبِينَ ٱلضَّآلِّينَ
- (58:14) [listed for 1:7] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ تَوَلَّوْا۟ قَوْمًا غَضِبَ ٱللَّهُ عَلَيْهِم مَّا هُم مِّنكُمْ وَلَا مِنْهُمْ وَيَحْلِفُونَ عَلَى ٱلْكَذِبِ وَهُمْ يَعْلَمُونَ
- (93:7) [listed for 1:7] [cited in ¶27] وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ
- (93:11) [listed for 1:7] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (102:8) [listed for 1:7] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ
- (105:2) [listed for 1:7] أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ

## medium (this ayah's own list) (110)

- (2:61) [listed for 1:7] [cited in ¶17] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (2:90) [listed for 1:7] بِئْسَمَا ٱشْتَرَوْا۟ بِهِۦٓ أَنفُسَهُمْ أَن يَكْفُرُوا۟ بِمَآ أَنزَلَ ٱللَّهُ بَغْيًا أَن يُنَزِّلَ ٱللَّهُ مِن فَضْلِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۖ فَبَآءُو بِغَضَبٍ عَلَىٰ غَضَبٍۢ ۚ وَلِلْكَٰفِرِينَ عَذَابٌۭ مُّهِينٌۭ
- (2:108) [listed for 1:7] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (2:122) [listed for 1:7] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:152) [listed for 1:7] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
- (2:213) [listed for 1:7] كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ فَبَعَثَ ٱللَّهُ ٱلنَّبِيِّۦنَ مُبَشِّرِينَ وَمُنذِرِينَ وَأَنزَلَ مَعَهُمُ ٱلْكِتَٰبَ بِٱلْحَقِّ لِيَحْكُمَ بَيْنَ ٱلنَّاسِ فِيمَا ٱخْتَلَفُوا۟ فِيهِ ۚ وَمَا ٱخْتَلَفَ فِيهِ إِلَّا ٱلَّذِينَ أُوتُوهُ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ بَغْيًۢا بَيْنَهُمْ ۖ فَهَدَى ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ لِمَا ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
- (4:88) [listed for 1:7] ۞ فَمَا لَكُمْ فِى ٱلْمُنَٰفِقِينَ فِئَتَيْنِ وَٱللَّهُ أَرْكَسَهُم بِمَا كَسَبُوٓا۟ ۚ أَتُرِيدُونَ أَن تَهْدُوا۟ مَنْ أَضَلَّ ٱللَّهُ ۖ وَمَن يُضْلِلِ ٱللَّهُ فَلَن تَجِدَ لَهُۥ سَبِيلًۭا
- (4:93) [listed for 1:7] وَمَن يَقْتُلْ مُؤْمِنًۭا مُّتَعَمِّدًۭا فَجَزَآؤُهُۥ جَهَنَّمُ خَٰلِدًۭا فِيهَا وَغَضِبَ ٱللَّهُ عَلَيْهِ وَلَعَنَهُۥ وَأَعَدَّ لَهُۥ عَذَابًا عَظِيمًۭا
- (4:119) [listed for 1:7] وَلَأُضِلَّنَّهُمْ وَلَأُمَنِّيَنَّهُمْ وَلَءَامُرَنَّهُمْ فَلَيُبَتِّكُنَّ ءَاذَانَ ٱلْأَنْعَٰمِ وَلَءَامُرَنَّهُمْ فَلَيُغَيِّرُنَّ خَلْقَ ٱللَّهِ ۚ وَمَن يَتَّخِذِ ٱلشَّيْطَٰنَ وَلِيًّۭا مِّن دُونِ ٱللَّهِ فَقَدْ خَسِرَ خُسْرَانًۭا مُّبِينًۭا
- (5:6) [listed for 1:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (5:11) [listed for 1:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ إِذْ هَمَّ قَوْمٌ أَن يَبْسُطُوٓا۟ إِلَيْكُمْ أَيْدِيَهُمْ فَكَفَّ أَيْدِيَهُمْ عَنكُمْ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ
- (5:60) [listed for 1:7] [cited in ¶22] قُلْ هَلْ أُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكَ مَثُوبَةً عِندَ ٱللَّهِ ۚ مَن لَّعَنَهُ ٱللَّهُ وَغَضِبَ عَلَيْهِ وَجَعَلَ مِنْهُمُ ٱلْقِرَدَةَ وَٱلْخَنَازِيرَ وَعَبَدَ ٱلطَّٰغُوتَ ۚ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ
- (5:77) [listed for 1:7] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ غَيْرَ ٱلْحَقِّ وَلَا تَتَّبِعُوٓا۟ أَهْوَآءَ قَوْمٍۢ قَدْ ضَلُّوا۟ مِن قَبْلُ وَأَضَلُّوا۟ كَثِيرًۭا وَضَلُّوا۟ عَن سَوَآءِ ٱلسَّبِيلِ
- (5:105) [listed for 1:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ عَلَيْكُمْ أَنفُسَكُمْ ۖ لَا يَضُرُّكُم مَّن ضَلَّ إِذَا ٱهْتَدَيْتُمْ ۚ إِلَى ٱللَّهِ مَرْجِعُكُمْ جَمِيعًۭا فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (6:140) [listed for 1:7] قَدْ خَسِرَ ٱلَّذِينَ قَتَلُوٓا۟ أَوْلَٰدَهُمْ سَفَهًۢا بِغَيْرِ عِلْمٍۢ وَحَرَّمُوا۟ مَا رَزَقَهُمُ ٱللَّهُ ٱفْتِرَآءً عَلَى ٱللَّهِ ۚ قَدْ ضَلُّوا۟ وَمَا كَانُوا۟ مُهْتَدِينَ
- (7:30) [listed for 1:7] فَرِيقًا هَدَىٰ وَفَرِيقًا حَقَّ عَلَيْهِمُ ٱلضَّلَٰلَةُ ۗ إِنَّهُمُ ٱتَّخَذُوا۟ ٱلشَّيَٰطِينَ أَوْلِيَآءَ مِن دُونِ ٱللَّهِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
- (7:140) [listed for 1:7] قَالَ أَغَيْرَ ٱللَّهِ أَبْغِيكُمْ إِلَٰهًۭا وَهُوَ فَضَّلَكُمْ عَلَى ٱلْعَٰلَمِينَ
- (7:152) [listed for 1:7] [cited in ¶21] إِنَّ ٱلَّذِينَ ٱتَّخَذُوا۟ ٱلْعِجْلَ سَيَنَالُهُمْ غَضَبٌۭ مِّن رَّبِّهِمْ وَذِلَّةٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُفْتَرِينَ
- (7:162) [listed for 1:7] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَرْسَلْنَا عَلَيْهِمْ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَظْلِمُونَ
- (7:178) [listed for 1:7] مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِى ۖ وَمَن يُضْلِلْ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (7:186) [listed for 1:7] مَن يُضْلِلِ ٱللَّهُ فَلَا هَادِىَ لَهُۥ ۚ وَيَذَرُهُمْ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (9:93) [listed for 1:7] ۞ إِنَّمَا ٱلسَّبِيلُ عَلَى ٱلَّذِينَ يَسْتَـْٔذِنُونَكَ وَهُمْ أَغْنِيَآءُ ۚ رَضُوا۟ بِأَن يَكُونُوا۟ مَعَ ٱلْخَوَالِفِ وَطَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ فَهُمْ لَا يَعْلَمُونَ
- (9:115) [listed for 1:7] وَمَا كَانَ ٱللَّهُ لِيُضِلَّ قَوْمًۢا بَعْدَ إِذْ هَدَىٰهُمْ حَتَّىٰ يُبَيِّنَ لَهُم مَّا يَتَّقُونَ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌ
- (10:15) [listed for 1:7] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَاتُنَا بَيِّنَٰتٍۢ ۙ قَالَ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا ٱئْتِ بِقُرْءَانٍ غَيْرِ هَٰذَآ أَوْ بَدِّلْهُ ۚ قُلْ مَا يَكُونُ لِىٓ أَنْ أُبَدِّلَهُۥ مِن تِلْقَآئِ نَفْسِىٓ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ ۖ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (10:108) [listed for 1:7] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ قَدْ جَآءَكُمُ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا ۖ وَمَآ أَنَا۠ عَلَيْكُم بِوَكِيلٍۢ
- (14:4) [listed for 1:7] وَمَآ أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوْمِهِۦ لِيُبَيِّنَ لَهُمْ ۖ فَيُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (14:7) [listed for 1:7] وَإِذْ تَأَذَّنَ رَبُّكُمْ لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ ۖ وَلَئِن كَفَرْتُمْ إِنَّ عَذَابِى لَشَدِيدٌۭ
- (14:27) [listed for 1:7] يُثَبِّتُ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ بِٱلْقَوْلِ ٱلثَّابِتِ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَفِى ٱلْءَاخِرَةِ ۖ وَيُضِلُّ ٱللَّهُ ٱلظَّٰلِمِينَ ۚ وَيَفْعَلُ ٱللَّهُ مَا يَشَآءُ
- (14:36) [listed for 1:7] رَبِّ إِنَّهُنَّ أَضْلَلْنَ كَثِيرًۭا مِّنَ ٱلنَّاسِ ۖ فَمَن تَبِعَنِى فَإِنَّهُۥ مِنِّى ۖ وَمَنْ عَصَانِى فَإِنَّكَ غَفُورٌۭ رَّحِيمٌۭ
- (15:39) [listed for 1:7] قَالَ رَبِّ بِمَآ أَغْوَيْتَنِى لَأُزَيِّنَنَّ لَهُمْ فِى ٱلْأَرْضِ وَلَأُغْوِيَنَّهُمْ أَجْمَعِينَ
- (16:18) [listed for 1:7] وَإِن تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱللَّهَ لَغَفُورٌۭ رَّحِيمٌۭ
- (16:53) [listed for 1:7] وَمَا بِكُم مِّن نِّعْمَةٍۢ فَمِنَ ٱللَّهِ ۖ ثُمَّ إِذَا مَسَّكُمُ ٱلضُّرُّ فَإِلَيْهِ تَجْـَٔرُونَ
- (16:72) [listed for 1:7] وَٱللَّهُ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَجَعَلَ لَكُم مِّنْ أَزْوَٰجِكُم بَنِينَ وَحَفَدَةًۭ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ ۚ أَفَبِٱلْبَٰطِلِ يُؤْمِنُونَ وَبِنِعْمَتِ ٱللَّهِ هُمْ يَكْفُرُونَ
- (16:81) [listed for 1:7] وَٱللَّهُ جَعَلَ لَكُم مِّمَّا خَلَقَ ظِلَٰلًۭا وَجَعَلَ لَكُم مِّنَ ٱلْجِبَالِ أَكْنَٰنًۭا وَجَعَلَ لَكُمْ سَرَٰبِيلَ تَقِيكُمُ ٱلْحَرَّ وَسَرَٰبِيلَ تَقِيكُم بَأْسَكُمْ ۚ كَذَٰلِكَ يُتِمُّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تُسْلِمُونَ
- (16:106) [listed for 1:7] مَن كَفَرَ بِٱللَّهِ مِنۢ بَعْدِ إِيمَٰنِهِۦٓ إِلَّا مَنْ أُكْرِهَ وَقَلْبُهُۥ مُطْمَئِنٌّۢ بِٱلْإِيمَٰنِ وَلَٰكِن مَّن شَرَحَ بِٱلْكُفْرِ صَدْرًۭا فَعَلَيْهِمْ غَضَبٌۭ مِّنَ ٱللَّهِ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
- (16:121) [listed for 1:7] [cited in ¶11] شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (17:15) [listed for 1:7] مَّنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ وَمَا كُنَّا مُعَذِّبِينَ حَتَّىٰ نَبْعَثَ رَسُولًۭا
- (17:67) [listed for 1:7] وَإِذَا مَسَّكُمُ ٱلضُّرُّ فِى ٱلْبَحْرِ ضَلَّ مَن تَدْعُونَ إِلَّآ إِيَّاهُ ۖ فَلَمَّا نَجَّىٰكُمْ إِلَى ٱلْبَرِّ أَعْرَضْتُمْ ۚ وَكَانَ ٱلْإِنسَٰنُ كَفُورًا
- (17:73) [listed for 1:7] وَإِن كَادُوا۟ لَيَفْتِنُونَكَ عَنِ ٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ لِتَفْتَرِىَ عَلَيْنَا غَيْرَهُۥ ۖ وَإِذًۭا لَّٱتَّخَذُوكَ خَلِيلًۭا
- (17:83) [listed for 1:7] [cited in ¶16] وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ ۖ وَإِذَا مَسَّهُ ٱلشَّرُّ كَانَ يَـُٔوسًۭا
- (17:97) [listed for 1:7] وَمَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُمْ أَوْلِيَآءَ مِن دُونِهِۦ ۖ وَنَحْشُرُهُمْ يَوْمَ ٱلْقِيَٰمَةِ عَلَىٰ وُجُوهِهِمْ عُمْيًۭا وَبُكْمًۭا وَصُمًّۭا ۖ مَّأْوَىٰهُمْ جَهَنَّمُ ۖ كُلَّمَا خَبَتْ زِدْنَٰهُمْ سَعِيرًۭا
- (18:17) [listed for 1:7] ۞ وَتَرَى ٱلشَّمْسَ إِذَا طَلَعَت تَّزَٰوَرُ عَن كَهْفِهِمْ ذَاتَ ٱلْيَمِينِ وَإِذَا غَرَبَت تَّقْرِضُهُمْ ذَاتَ ٱلشِّمَالِ وَهُمْ فِى فَجْوَةٍۢ مِّنْهُ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ ۗ مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُۥ وَلِيًّۭا مُّرْشِدًۭا
- (18:104) [listed for 1:7] ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا
- (20:86) [listed for 1:7] [cited in ¶17] فَرَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا ۚ قَالَ يَٰقَوْمِ أَلَمْ يَعِدْكُمْ رَبُّكُمْ وَعْدًا حَسَنًا ۚ أَفَطَالَ عَلَيْكُمُ ٱلْعَهْدُ أَمْ أَرَدتُّمْ أَن يَحِلَّ عَلَيْكُمْ غَضَبٌۭ مِّن رَّبِّكُمْ فَأَخْلَفْتُم مَّوْعِدِى
- (21:54) [listed for 1:7] قَالَ لَقَدْ كُنتُمْ أَنتُمْ وَءَابَآؤُكُمْ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (21:112) [listed for 1:7] قَٰلَ رَبِّ ٱحْكُم بِٱلْحَقِّ ۗ وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (22:3) [listed for 1:7] وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّبِعُ كُلَّ شَيْطَٰنٍۢ مَّرِيدٍۢ
- (22:4) [listed for 1:7] كُتِبَ عَلَيْهِ أَنَّهُۥ مَن تَوَلَّاهُ فَأَنَّهُۥ يُضِلُّهُۥ وَيَهْدِيهِ إِلَىٰ عَذَابِ ٱلسَّعِيرِ
- (22:9) [listed for 1:7] ثَانِىَ عِطْفِهِۦ لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ ۖ لَهُۥ فِى ٱلدُّنْيَا خِزْىٌۭ ۖ وَنُذِيقُهُۥ يَوْمَ ٱلْقِيَٰمَةِ عَذَابَ ٱلْحَرِيقِ
- (24:9) [listed for 1:7] وَٱلْخَٰمِسَةَ أَنَّ غَضَبَ ٱللَّهِ عَلَيْهَآ إِن كَانَ مِنَ ٱلصَّٰدِقِينَ
- (24:21) [listed for 1:7] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ وَمَن يَتَّبِعْ خُطُوَٰتِ ٱلشَّيْطَٰنِ فَإِنَّهُۥ يَأْمُرُ بِٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۚ وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ مَا زَكَىٰ مِنكُم مِّنْ أَحَدٍ أَبَدًۭا وَلَٰكِنَّ ٱللَّهَ يُزَكِّى مَن يَشَآءُ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- (25:42) [listed for 1:7] إِن كَادَ لَيُضِلُّنَا عَنْ ءَالِهَتِنَا لَوْلَآ أَن صَبَرْنَا عَلَيْهَا ۚ وَسَوْفَ يَعْلَمُونَ حِينَ يَرَوْنَ ٱلْعَذَابَ مَنْ أَضَلُّ سَبِيلًا
- (26:86) [listed for 1:7] وَٱغْفِرْ لِأَبِىٓ إِنَّهُۥ كَانَ مِنَ ٱلضَّآلِّينَ
- (27:19) [listed for 1:7] فَتَبَسَّمَ ضَاحِكًۭا مِّن قَوْلِهَا وَقَالَ رَبِّ أَوْزِعْنِىٓ أَنْ أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ أَنْعَمْتَ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ وَأَنْ أَعْمَلَ صَٰلِحًۭا تَرْضَىٰهُ وَأَدْخِلْنِى بِرَحْمَتِكَ فِى عِبَادِكَ ٱلصَّٰلِحِينَ
- (27:92) [listed for 1:7] وَأَنْ أَتْلُوَا۟ ٱلْقُرْءَانَ ۖ فَمَنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَقُلْ إِنَّمَآ أَنَا۠ مِنَ ٱلْمُنذِرِينَ
- (28:15) [listed for 1:7] وَدَخَلَ ٱلْمَدِينَةَ عَلَىٰ حِينِ غَفْلَةٍۢ مِّنْ أَهْلِهَا فَوَجَدَ فِيهَا رَجُلَيْنِ يَقْتَتِلَانِ هَٰذَا مِن شِيعَتِهِۦ وَهَٰذَا مِنْ عَدُوِّهِۦ ۖ فَٱسْتَغَٰثَهُ ٱلَّذِى مِن شِيعَتِهِۦ عَلَى ٱلَّذِى مِنْ عَدُوِّهِۦ فَوَكَزَهُۥ مُوسَىٰ فَقَضَىٰ عَلَيْهِ ۖ قَالَ هَٰذَا مِنْ عَمَلِ ٱلشَّيْطَٰنِ ۖ إِنَّهُۥ عَدُوٌّۭ مُّضِلٌّۭ مُّبِينٌۭ
- (28:50) [listed for 1:7] فَإِن لَّمْ يَسْتَجِيبُوا۟ لَكَ فَٱعْلَمْ أَنَّمَا يَتَّبِعُونَ أَهْوَآءَهُمْ ۚ وَمَنْ أَضَلُّ مِمَّنِ ٱتَّبَعَ هَوَىٰهُ بِغَيْرِ هُدًۭى مِّنَ ٱللَّهِ ۚ إِنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (30:55) [listed for 1:7] وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يُقْسِمُ ٱلْمُجْرِمُونَ مَا لَبِثُوا۟ غَيْرَ سَاعَةٍۢ ۚ كَذَٰلِكَ كَانُوا۟ يُؤْفَكُونَ
- (31:6) [listed for 1:7] وَمِنَ ٱلنَّاسِ مَن يَشْتَرِى لَهْوَ ٱلْحَدِيثِ لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّخِذَهَا هُزُوًا ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌۭ مُّهِينٌۭ
- (31:20) [listed for 1:7] أَلَمْ تَرَوْا۟ أَنَّ ٱللَّهَ سَخَّرَ لَكُم مَّا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَأَسْبَغَ عَلَيْكُمْ نِعَمَهُۥ ظَٰهِرَةًۭ وَبَاطِنَةًۭ ۗ وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَلَا هُدًۭى وَلَا كِتَٰبٍۢ مُّنِيرٍۢ
- (32:10) [listed for 1:7] [cited in ¶26] وَقَالُوٓا۟ أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ أَءِنَّا لَفِى خَلْقٍۢ جَدِيدٍۭ ۚ بَلْ هُم بِلِقَآءِ رَبِّهِمْ كَٰفِرُونَ
- (33:36) [listed for 1:7] وَمَا كَانَ لِمُؤْمِنٍۢ وَلَا مُؤْمِنَةٍ إِذَا قَضَى ٱللَّهُ وَرَسُولُهُۥٓ أَمْرًا أَن يَكُونَ لَهُمُ ٱلْخِيَرَةُ مِنْ أَمْرِهِمْ ۗ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَقَدْ ضَلَّ ضَلَٰلًۭا مُّبِينًۭا
- (33:67) [listed for 1:7] وَقَالُوا۟ رَبَّنَآ إِنَّآ أَطَعْنَا سَادَتَنَا وَكُبَرَآءَنَا فَأَضَلُّونَا ٱلسَّبِيلَا۠
- (34:13) [listed for 1:7] يَعْمَلُونَ لَهُۥ مَا يَشَآءُ مِن مَّحَٰرِيبَ وَتَمَٰثِيلَ وَجِفَانٍۢ كَٱلْجَوَابِ وَقُدُورٍۢ رَّاسِيَٰتٍ ۚ ٱعْمَلُوٓا۟ ءَالَ دَاوُۥدَ شُكْرًۭا ۚ وَقَلِيلٌۭ مِّنْ عِبَادِىَ ٱلشَّكُورُ
- (34:50) [listed for 1:7] قُلْ إِن ضَلَلْتُ فَإِنَّمَآ أَضِلُّ عَلَىٰ نَفْسِى ۖ وَإِنِ ٱهْتَدَيْتُ فَبِمَا يُوحِىٓ إِلَىَّ رَبِّىٓ ۚ إِنَّهُۥ سَمِيعٌۭ قَرِيبٌۭ
- (35:3) [listed for 1:7] يَٰٓأَيُّهَا ٱلنَّاسُ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ ۚ هَلْ مِنْ خَٰلِقٍ غَيْرُ ٱللَّهِ يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (35:8) [listed for 1:7] أَفَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ فَرَءَاهُ حَسَنًۭا ۖ فَإِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۖ فَلَا تَذْهَبْ نَفْسُكَ عَلَيْهِمْ حَسَرَٰتٍ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِمَا يَصْنَعُونَ
- (36:4) [listed for 1:7] عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (36:62) [listed for 1:7] وَلَقَدْ أَضَلَّ مِنكُمْ جِبِلًّۭا كَثِيرًا ۖ أَفَلَمْ تَكُونُوا۟ تَعْقِلُونَ
- (37:43) [listed for 1:7] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (39:8) [listed for 1:7] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (39:36) [listed for 1:7] أَلَيْسَ ٱللَّهُ بِكَافٍ عَبْدَهُۥ ۖ وَيُخَوِّفُونَكَ بِٱلَّذِينَ مِن دُونِهِۦ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (39:41) [listed for 1:7] إِنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ لِلنَّاسِ بِٱلْحَقِّ ۖ فَمَنِ ٱهْتَدَىٰ فَلِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍ
- (39:49) [listed for 1:7] فَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَانَا ثُمَّ إِذَا خَوَّلْنَٰهُ نِعْمَةًۭ مِّنَّا قَالَ إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍۭ ۚ بَلْ هِىَ فِتْنَةٌۭ وَلَٰكِنَّ أَكْثَرَهُمْ لَا يَعْلَمُونَ
- (39:64) [listed for 1:7] قُلْ أَفَغَيْرَ ٱللَّهِ تَأْمُرُوٓنِّىٓ أَعْبُدُ أَيُّهَا ٱلْجَٰهِلُونَ
- (40:34) [listed for 1:7] وَلَقَدْ جَآءَكُمْ يُوسُفُ مِن قَبْلُ بِٱلْبَيِّنَٰتِ فَمَا زِلْتُمْ فِى شَكٍّۢ مِّمَّا جَآءَكُم بِهِۦ ۖ حَتَّىٰٓ إِذَا هَلَكَ قُلْتُمْ لَن يَبْعَثَ ٱللَّهُ مِنۢ بَعْدِهِۦ رَسُولًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَنْ هُوَ مُسْرِفٌۭ مُّرْتَابٌ
- (41:17) [listed for 1:7] وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ فَأَخَذَتْهُمْ صَٰعِقَةُ ٱلْعَذَابِ ٱلْهُونِ بِمَا كَانُوا۟ يَكْسِبُونَ
- (42:37) [listed for 1:7] وَٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ وَإِذَا مَا غَضِبُوا۟ هُمْ يَغْفِرُونَ
- (42:46) [listed for 1:7] وَمَا كَانَ لَهُم مِّنْ أَوْلِيَآءَ يَنصُرُونَهُم مِّن دُونِ ٱللَّهِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِن سَبِيلٍ
- (43:32) [listed for 1:7] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (43:36) [listed for 1:7] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (43:37) [listed for 1:7] وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
- (45:23) [listed for 1:7] أَفَرَءَيْتَ مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ وَأَضَلَّهُ ٱللَّهُ عَلَىٰ عِلْمٍۢ وَخَتَمَ عَلَىٰ سَمْعِهِۦ وَقَلْبِهِۦ وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ ۚ أَفَلَا تَذَكَّرُونَ
- (46:28) [listed for 1:7] فَلَوْلَا نَصَرَهُمُ ٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ قُرْبَانًا ءَالِهَةًۢ ۖ بَلْ ضَلُّوا۟ عَنْهُمْ ۚ وَذَٰلِكَ إِفْكُهُمْ وَمَا كَانُوا۟ يَفْتَرُونَ
- (47:1) [listed for 1:7] ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ أَضَلَّ أَعْمَٰلَهُمْ
- (47:8) [listed for 1:7] وَٱلَّذِينَ كَفَرُوا۟ فَتَعْسًۭا لَّهُمْ وَأَضَلَّ أَعْمَٰلَهُمْ
- (48:6) [listed for 1:7] وَيُعَذِّبَ ٱلْمُنَٰفِقِينَ وَٱلْمُنَٰفِقَٰتِ وَٱلْمُشْرِكِينَ وَٱلْمُشْرِكَٰتِ ٱلظَّآنِّينَ بِٱللَّهِ ظَنَّ ٱلسَّوْءِ ۚ عَلَيْهِمْ دَآئِرَةُ ٱلسَّوْءِ ۖ وَغَضِبَ ٱللَّهُ عَلَيْهِمْ وَلَعَنَهُمْ وَأَعَدَّ لَهُمْ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًۭا
- (53:23) [listed for 1:7] إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ وَمَا تَهْوَى ٱلْأَنفُسُ ۖ وَلَقَدْ جَآءَهُم مِّن رَّبِّهِمُ ٱلْهُدَىٰٓ
- (53:29) [listed for 1:7] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (53:30) [listed for 1:7] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (56:51) [listed for 1:7] ثُمَّ إِنَّكُمْ أَيُّهَا ٱلضَّآلُّونَ ٱلْمُكَذِّبُونَ
- (60:13) [listed for 1:7] [cited in ¶7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَوَلَّوْا۟ قَوْمًا غَضِبَ ٱللَّهُ عَلَيْهِمْ قَدْ يَئِسُوا۟ مِنَ ٱلْءَاخِرَةِ كَمَا يَئِسَ ٱلْكُفَّارُ مِنْ أَصْحَٰبِ ٱلْقُبُورِ
- (61:5) [listed for 1:7] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ لِمَ تُؤْذُونَنِى وَقَد تَّعْلَمُونَ أَنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ ۖ فَلَمَّا زَاغُوٓا۟ أَزَاغَ ٱللَّهُ قُلُوبَهُمْ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْفَٰسِقِينَ
- (67:9) [listed for 1:7] قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا وَقُلْنَا مَا نَزَّلَ ٱللَّهُ مِن شَىْءٍ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ كَبِيرٍۢ
- (67:10) [listed for 1:7] وَقَالُوا۟ لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ مَا كُنَّا فِىٓ أَصْحَٰبِ ٱلسَّعِيرِ
- (68:7) [listed for 1:7] إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (68:26) [listed for 1:7] فَلَمَّا رَأَوْهَا قَالُوٓا۟ إِنَّا لَضَآلُّونَ
- (68:49) [listed for 1:7] لَّوْلَآ أَن تَدَٰرَكَهُۥ نِعْمَةٌۭ مِّن رَّبِّهِۦ لَنُبِذَ بِٱلْعَرَآءِ وَهُوَ مَذْمُومٌۭ
- (74:31) [listed for 1:7] وَمَا جَعَلْنَآ أَصْحَٰبَ ٱلنَّارِ إِلَّا مَلَٰٓئِكَةًۭ ۙ وَمَا جَعَلْنَا عِدَّتَهُمْ إِلَّا فِتْنَةًۭ لِّلَّذِينَ كَفَرُوا۟ لِيَسْتَيْقِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَيَزْدَادَ ٱلَّذِينَ ءَامَنُوٓا۟ إِيمَٰنًۭا ۙ وَلَا يَرْتَابَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْمُؤْمِنُونَ ۙ وَلِيَقُولَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ وَٱلْكَٰفِرُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَمَا يَعْلَمُ جُنُودَ رَبِّكَ إِلَّا هُوَ ۚ وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ
- (83:22) [listed for 1:7] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:32) [listed for 1:7] وَإِذَا رَأَوْهُمْ قَالُوٓا۟ إِنَّ هَٰٓؤُلَآءِ لَضَآلُّونَ
- (88:8) [listed for 1:7] [cited in ¶12] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- (89:15) [listed for 1:7] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- (92:19) [listed for 1:7] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (109:1) [listed for 1:7] قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ
- (109:2) [listed for 1:7] لَآ أَعْبُدُ مَا تَعْبُدُونَ
- (109:3) [listed for 1:7] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- (109:4) [listed for 1:7] وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- (109:5) [listed for 1:7] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- (109:6) [listed for 1:7] لَكُمْ دِينُكُمْ وَلِىَ دِينِ

## named by the passage's own list as strong for this ayah (6)

- (11:112) [listed for 1:7] فَٱسْتَقِمْ كَمَآ أُمِرْتَ وَمَن تَابَ مَعَكَ وَلَا تَطْغَوْا۟ ۚ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (15:87) [listed for 1:7] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (19:58) [listed for 1:7] [cited in ¶4] أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ مِن ذُرِّيَّةِ ءَادَمَ وَمِمَّنْ حَمَلْنَا مَعَ نُوحٍۢ وَمِن ذُرِّيَّةِ إِبْرَٰهِيمَ وَإِسْرَٰٓءِيلَ وَمِمَّنْ هَدَيْنَا وَٱجْتَبَيْنَآ ۚ إِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُ ٱلرَّحْمَٰنِ خَرُّوا۟ سُجَّدًۭا وَبُكِيًّۭا ۩
- (36:66) [listed for 1:7] وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ
- (38:22) [listed for 1:7] إِذْ دَخَلُوا۟ عَلَىٰ دَاوُۥدَ فَفَزِعَ مِنْهُمْ ۖ قَالُوا۟ لَا تَخَفْ ۖ خَصْمَانِ بَغَىٰ بَعْضُنَا عَلَىٰ بَعْضٍۢ فَٱحْكُم بَيْنَنَا بِٱلْحَقِّ وَلَا تُشْطِطْ وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ
- (81:26) [listed for 1:7] فَأَيْنَ تَذْهَبُونَ

## named by the passage's own list as medium for this ayah (22)

- (4:115) [listed for 1:7] وَمَن يُشَاقِقِ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُ ٱلْهُدَىٰ وَيَتَّبِعْ غَيْرَ سَبِيلِ ٱلْمُؤْمِنِينَ نُوَلِّهِۦ مَا تَوَلَّىٰ وَنُصْلِهِۦ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًا
- (5:20) [listed for 1:7] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ إِذْ جَعَلَ فِيكُمْ أَنۢبِيَآءَ وَجَعَلَكُم مُّلُوكًۭا وَءَاتَىٰكُم مَّا لَمْ يُؤْتِ أَحَدًۭا مِّنَ ٱلْعَٰلَمِينَ
- (5:65) [listed for 1:7] وَلَوْ أَنَّ أَهْلَ ٱلْكِتَٰبِ ءَامَنُوا۟ وَٱتَّقَوْا۟ لَكَفَّرْنَا عَنْهُمْ سَيِّـَٔاتِهِمْ وَلَأَدْخَلْنَٰهُمْ جَنَّٰتِ ٱلنَّعِيمِ
- (7:202) [listed for 1:7] وَإِخْوَٰنُهُمْ يَمُدُّونَهُمْ فِى ٱلْغَىِّ ثُمَّ لَا يُقْصِرُونَ
- (11:19) [listed for 1:7] ٱلَّذِينَ يَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًۭا وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (14:6) [listed for 1:7] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِ ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ إِذْ أَنجَىٰكُم مِّنْ ءَالِ فِرْعَوْنَ يَسُومُونَكُمْ سُوٓءَ ٱلْعَذَابِ وَيُذَبِّحُونَ أَبْنَآءَكُمْ وَيَسْتَحْيُونَ نِسَآءَكُمْ ۚ وَفِى ذَٰلِكُم بَلَآءٌۭ مِّن رَّبِّكُمْ عَظِيمٌۭ
- (14:48) [listed for 1:7] يَوْمَ تُبَدَّلُ ٱلْأَرْضُ غَيْرَ ٱلْأَرْضِ وَٱلسَّمَٰوَٰتُ ۖ وَبَرَزُوا۟ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
- (20:135) [listed for 1:7] قُلْ كُلٌّۭ مُّتَرَبِّصٌۭ فَتَرَبَّصُوا۟ ۖ فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ
- (23:23) [listed for 1:7] وَلَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۖ أَفَلَا تَتَّقُونَ
- (26:22) [listed for 1:7] وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ
- (30:31) [listed for 1:7] ۞ مُنِيبِينَ إِلَيْهِ وَٱتَّقُوهُ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَلَا تَكُونُوا۟ مِنَ ٱلْمُشْرِكِينَ
- (35:20) [listed for 1:7] وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ
- (37:57) [listed for 1:7] وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ
- (43:40) [listed for 1:7] أَفَأَنتَ تُسْمِعُ ٱلصُّمَّ أَوْ تَهْدِى ٱلْعُمْىَ وَمَن كَانَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (43:59) [listed for 1:7] إِنْ هُوَ إِلَّا عَبْدٌ أَنْعَمْنَا عَلَيْهِ وَجَعَلْنَٰهُ مَثَلًۭا لِّبَنِىٓ إِسْرَٰٓءِيلَ
- (43:61) [listed for 1:7] وَإِنَّهُۥ لَعِلْمٌۭ لِّلسَّاعَةِ فَلَا تَمْتَرُنَّ بِهَا وَٱتَّبِعُونِ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (48:2) [listed for 1:7] [cited in ¶11] لِّيَغْفِرَ لَكَ ٱللَّهُ مَا تَقَدَّمَ مِن ذَنۢبِكَ وَمَا تَأَخَّرَ وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (50:31) [listed for 1:7] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ غَيْرَ بَعِيدٍ
- (53:2) [listed for 1:7] مَا ضَلَّ صَاحِبُكُمْ وَمَا غَوَىٰ
- (77:23) [listed for 1:7] فَقَدَرْنَا فَنِعْمَ ٱلْقَٰدِرُونَ
- (82:13) [listed for 1:7] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍۢ
- (100:3) [listed for 1:7] فَٱلْمُغِيرَٰتِ صُبْحًۭا

## weak (this ayah's own list) (27)

- (2:40) [listed for 1:7] [cited in ¶17] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَوْفُوا۟ بِعَهْدِىٓ أُوفِ بِعَهْدِكُمْ وَإِيَّٰىَ فَٱرْهَبُونِ
- (2:47) [listed for 1:7] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:119) [listed for 1:7] إِنَّآ أَرْسَلْنَٰكَ بِٱلْحَقِّ بَشِيرًۭا وَنَذِيرًۭا ۖ وَلَا تُسْـَٔلُ عَنْ أَصْحَٰبِ ٱلْجَحِيمِ
- (2:198) [listed for 1:7] لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ ۚ فَإِذَآ أَفَضْتُم مِّنْ عَرَفَٰتٍۢ فَٱذْكُرُوا۟ ٱللَّهَ عِندَ ٱلْمَشْعَرِ ٱلْحَرَامِ ۖ وَٱذْكُرُوهُ كَمَا هَدَىٰكُمْ وَإِن كُنتُم مِّن قَبْلِهِۦ لَمِنَ ٱلضَّآلِّينَ
- (2:282) [listed for 1:7] [cited in ¶24] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (3:112) [listed for 1:7] ضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ أَيْنَ مَا ثُقِفُوٓا۟ إِلَّا بِحَبْلٍۢ مِّنَ ٱللَّهِ وَحَبْلٍۢ مِّنَ ٱلنَّاسِ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ وَضُرِبَتْ عَلَيْهِمُ ٱلْمَسْكَنَةُ ۚ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلْأَنۢبِيَآءَ بِغَيْرِ حَقٍّۢ ۚ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (3:154) [listed for 1:7] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (4:56) [listed for 1:7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
- (6:93) [listed for 1:7] وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَوْ قَالَ أُوحِىَ إِلَىَّ وَلَمْ يُوحَ إِلَيْهِ شَىْءٌۭ وَمَن قَالَ سَأُنزِلُ مِثْلَ مَآ أَنزَلَ ٱللَّهُ ۗ وَلَوْ تَرَىٰٓ إِذِ ٱلظَّٰلِمُونَ فِى غَمَرَٰتِ ٱلْمَوْتِ وَٱلْمَلَٰٓئِكَةُ بَاسِطُوٓا۟ أَيْدِيهِمْ أَخْرِجُوٓا۟ أَنفُسَكُمُ ۖ ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَقُولُونَ عَلَى ٱللَّهِ غَيْرَ ٱلْحَقِّ وَكُنتُمْ عَنْ ءَايَٰتِهِۦ تَسْتَكْبِرُونَ
- (10:23) [listed for 1:7] فَلَمَّآ أَنجَىٰهُمْ إِذَا هُمْ يَبْغُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ ۗ يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّمَا بَغْيُكُمْ عَلَىٰٓ أَنفُسِكُم ۖ مَّتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ ثُمَّ إِلَيْنَا مَرْجِعُكُمْ فَنُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (10:62) [listed for 1:7] أَلَآ إِنَّ أَوْلِيَآءَ ٱللَّهِ لَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (12:8) [listed for 1:7] إِذْ قَالُوا۟ لَيُوسُفُ وَأَخُوهُ أَحَبُّ إِلَىٰٓ أَبِينَا مِنَّا وَنَحْنُ عُصْبَةٌ إِنَّ أَبَانَا لَفِى ضَلَٰلٍۢ مُّبِينٍ
- (16:5) [listed for 1:7] وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ
- (23:6) [listed for 1:7] إِلَّا عَلَىٰٓ أَزْوَٰجِهِمْ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَإِنَّهُمْ غَيْرُ مَلُومِينَ
- (33:37) [listed for 1:7] وَإِذْ تَقُولُ لِلَّذِىٓ أَنْعَمَ ٱللَّهُ عَلَيْهِ وَأَنْعَمْتَ عَلَيْهِ أَمْسِكْ عَلَيْكَ زَوْجَكَ وَٱتَّقِ ٱللَّهَ وَتُخْفِى فِى نَفْسِكَ مَا ٱللَّهُ مُبْدِيهِ وَتَخْشَى ٱلنَّاسَ وَٱللَّهُ أَحَقُّ أَن تَخْشَىٰهُ ۖ فَلَمَّا قَضَىٰ زَيْدٌۭ مِّنْهَا وَطَرًۭا زَوَّجْنَٰكَهَا لِكَىْ لَا يَكُونَ عَلَى ٱلْمُؤْمِنِينَ حَرَجٌۭ فِىٓ أَزْوَٰجِ أَدْعِيَآئِهِمْ إِذَا قَضَوْا۟ مِنْهُنَّ وَطَرًۭا ۚ وَكَانَ أَمْرُ ٱللَّهِ مَفْعُولًۭا
- (36:27) [listed for 1:7] بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ
- (39:61) [listed for 1:7] وَيُنَجِّى ٱللَّهُ ٱلَّذِينَ ٱتَّقَوْا۟ بِمَفَازَتِهِمْ لَا يَمَسُّهُمُ ٱلسُّوٓءُ وَلَا هُمْ يَحْزَنُونَ
- (42:18) [listed for 1:7] يَسْتَعْجِلُ بِهَا ٱلَّذِينَ لَا يُؤْمِنُونَ بِهَا ۖ وَٱلَّذِينَ ءَامَنُوا۟ مُشْفِقُونَ مِنْهَا وَيَعْلَمُونَ أَنَّهَا ٱلْحَقُّ ۗ أَلَآ إِنَّ ٱلَّذِينَ يُمَارُونَ فِى ٱلسَّاعَةِ لَفِى ضَلَٰلٍۭ بَعِيدٍ
- (42:52) [listed for 1:7] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ رُوحًۭا مِّنْ أَمْرِنَا ۚ مَا كُنتَ تَدْرِى مَا ٱلْكِتَٰبُ وَلَا ٱلْإِيمَٰنُ وَلَٰكِن جَعَلْنَٰهُ نُورًۭا نَّهْدِى بِهِۦ مَن نَّشَآءُ مِنْ عِبَادِنَا ۚ وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (47:12) [listed for 1:7] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
- (52:17) [listed for 1:7] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَعِيمٍۢ
- (68:9) [listed for 1:7] وَدُّوا۟ لَوْ تُدْهِنُ فَيُدْهِنُونَ
- (73:11) [listed for 1:7] وَذَرْنِى وَٱلْمُكَذِّبِينَ أُو۟لِى ٱلنَّعْمَةِ وَمَهِّلْهُمْ قَلِيلًا
- (83:6) [listed for 1:7] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
- (83:11) [listed for 1:7] ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ
- (89:13) [listed for 1:7] فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- (106:3) [listed for 1:7] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ

## named by the passage's own list as weak for this ayah (25)

- (2:142) [listed for 1:7] ۞ سَيَقُولُ ٱلسُّفَهَآءُ مِنَ ٱلنَّاسِ مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (3:88) [listed for 1:7] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (7:61) [listed for 1:7] قَالَ يَٰقَوْمِ لَيْسَ بِى ضَلَٰلَةٌۭ وَلَٰكِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (7:150) [listed for 1:7] [cited in ¶21] وَلَمَّا رَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا قَالَ بِئْسَمَا خَلَفْتُمُونِى مِنۢ بَعْدِىٓ ۖ أَعَجِلْتُمْ أَمْرَ رَبِّكُمْ ۖ وَأَلْقَى ٱلْأَلْوَاحَ وَأَخَذَ بِرَأْسِ أَخِيهِ يَجُرُّهُۥٓ إِلَيْهِ ۚ قَالَ ٱبْنَ أُمَّ إِنَّ ٱلْقَوْمَ ٱسْتَضْعَفُونِى وَكَادُوا۟ يَقْتُلُونَنِى فَلَا تُشْمِتْ بِىَ ٱلْأَعْدَآءَ وَلَا تَجْعَلْنِى مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (12:57) [listed for 1:7] وَلَأَجْرُ ٱلْءَاخِرَةِ خَيْرٌۭ لِّلَّذِينَ ءَامَنُوا۟ وَكَانُوا۟ يَتَّقُونَ
- (12:95) [listed for 1:7] قَالُوا۟ تَٱللَّهِ إِنَّكَ لَفِى ضَلَٰلِكَ ٱلْقَدِيمِ
- (21:87) [listed for 1:7] وَذَا ٱلنُّونِ إِذ ذَّهَبَ مُغَٰضِبًۭا فَظَنَّ أَن لَّن نَّقْدِرَ عَلَيْهِ فَنَادَىٰ فِى ٱلظُّلُمَٰتِ أَن لَّآ إِلَٰهَ إِلَّآ أَنتَ سُبْحَٰنَكَ إِنِّى كُنتُ مِنَ ٱلظَّٰلِمِينَ
- (23:32) [listed for 1:7] فَأَرْسَلْنَا فِيهِمْ رَسُولًۭا مِّنْهُمْ أَنِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۖ أَفَلَا تَتَّقُونَ
- (26:99) [listed for 1:7] وَمَآ أَضَلَّنَآ إِلَّا ٱلْمُجْرِمُونَ
- (26:101) [listed for 1:7] وَلَا صَدِيقٍ حَمِيمٍۢ
- (26:133) [listed for 1:7] أَمَدَّكُم بِأَنْعَٰمٍۢ وَبَنِينَ
- (26:173) [listed for 1:7] وَأَمْطَرْنَا عَلَيْهِم مَّطَرًۭا ۖ فَسَآءَ مَطَرُ ٱلْمُنذَرِينَ
- (31:31) [listed for 1:7] أَلَمْ تَرَ أَنَّ ٱلْفُلْكَ تَجْرِى فِى ٱلْبَحْرِ بِنِعْمَتِ ٱللَّهِ لِيُرِيَكُم مِّنْ ءَايَٰتِهِۦٓ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (35:37) [listed for 1:7] وَهُمْ يَصْطَرِخُونَ فِيهَا رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ ۖ فَذُوقُوا۟ فَمَا لِلظَّٰلِمِينَ مِن نَّصِيرٍ
- (37:69) [listed for 1:7] إِنَّهُمْ أَلْفَوْا۟ ءَابَآءَهُمْ ضَآلِّينَ
- (42:42) [listed for 1:7] إِنَّمَا ٱلسَّبِيلُ عَلَى ٱلَّذِينَ يَظْلِمُونَ ٱلنَّاسَ وَيَبْغُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌ أَلِيمٌۭ
- (47:38) [listed for 1:7] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ تُدْعَوْنَ لِتُنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ فَمِنكُم مَّن يَبْخَلُ ۖ وَمَن يَبْخَلْ فَإِنَّمَا يَبْخَلُ عَن نَّفْسِهِۦ ۚ وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ ۚ وَإِن تَتَوَلَّوْا۟ يَسْتَبْدِلْ قَوْمًا غَيْرَكُمْ ثُمَّ لَا يَكُونُوٓا۟ أَمْثَٰلَكُم
- (51:36) [listed for 1:7] فَمَا وَجَدْنَا فِيهَا غَيْرَ بَيْتٍۢ مِّنَ ٱلْمُسْلِمِينَ
- (70:30) [listed for 1:7] إِلَّا عَلَىٰٓ أَزْوَٰجِهِمْ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَإِنَّهُمْ غَيْرُ مَلُومِينَ
- (71:24) [listed for 1:7] وَقَدْ أَضَلُّوا۟ كَثِيرًۭا ۖ وَلَا تَزِدِ ٱلظَّٰلِمِينَ إِلَّا ضَلَٰلًۭا
- (74:10) [listed for 1:7] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (76:14) [listed for 1:7] وَدَانِيَةً عَلَيْهِمْ ظِلَٰلُهَا وَذُلِّلَتْ قُطُوفُهَا تَذْلِيلًۭا
- (79:33) [listed for 1:7] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (84:25) [listed for 1:7] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۭ
- (95:6) [listed for 1:7] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ

## neighbours: within two ayat of a passage the commentary cites (101)

- (2:38) [next to 2:40] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:39) [next to 2:40] وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:41) [next to 2:40] وَءَامِنُوا۟ بِمَآ أَنزَلْتُ مُصَدِّقًۭا لِّمَا مَعَكُمْ وَلَا تَكُونُوٓا۟ أَوَّلَ كَافِرٍۭ بِهِۦ ۖ وَلَا تَشْتَرُوا۟ بِـَٔايَٰتِى ثَمَنًۭا قَلِيلًۭا وَإِيَّٰىَ فَٱتَّقُونِ
- (2:42) [next to 2:40] وَلَا تَلْبِسُوا۟ ٱلْحَقَّ بِٱلْبَٰطِلِ وَتَكْتُمُوا۟ ٱلْحَقَّ وَأَنتُمْ تَعْلَمُونَ
- (2:59) [next to 2:61] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَنزَلْنَا عَلَى ٱلَّذِينَ ظَلَمُوا۟ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَفْسُقُونَ
- (2:60) [next to 2:61] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (2:62) [next to 2:61] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَادُوا۟ وَٱلنَّصَٰرَىٰ وَٱلصَّٰبِـِٔينَ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَعَمِلَ صَٰلِحًۭا فَلَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:63) [next to 2:61] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (2:280) [next to 2:282] وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (2:281) [next to 2:282] وَٱتَّقُوا۟ يَوْمًۭا تُرْجَعُونَ فِيهِ إِلَى ٱللَّهِ ۖ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (2:283) [next to 2:282] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (2:284) [next to 2:282] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (4:64) [next to 4:66] وَمَآ أَرْسَلْنَا مِن رَّسُولٍ إِلَّا لِيُطَاعَ بِإِذْنِ ٱللَّهِ ۚ وَلَوْ أَنَّهُمْ إِذ ظَّلَمُوٓا۟ أَنفُسَهُمْ جَآءُوكَ فَٱسْتَغْفَرُوا۟ ٱللَّهَ وَٱسْتَغْفَرَ لَهُمُ ٱلرَّسُولُ لَوَجَدُوا۟ ٱللَّهَ تَوَّابًۭا رَّحِيمًۭا
- (4:65) [next to 4:66] فَلَا وَرَبِّكَ لَا يُؤْمِنُونَ حَتَّىٰ يُحَكِّمُوكَ فِيمَا شَجَرَ بَيْنَهُمْ ثُمَّ لَا يَجِدُوا۟ فِىٓ أَنفُسِهِمْ حَرَجًۭا مِّمَّا قَضَيْتَ وَيُسَلِّمُوا۟ تَسْلِيمًۭا
- (4:67) [next to 4:66] وَإِذًۭا لَّءَاتَيْنَٰهُم مِّن لَّدُنَّآ أَجْرًا عَظِيمًۭا
- (4:70) [next to 4:68] ذَٰلِكَ ٱلْفَضْلُ مِنَ ٱللَّهِ ۚ وَكَفَىٰ بِٱللَّهِ عَلِيمًۭا
- (4:71) [next to 4:69] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ خُذُوا۟ حِذْرَكُمْ فَٱنفِرُوا۟ ثُبَاتٍ أَوِ ٱنفِرُوا۟ جَمِيعًۭا
- (5:58) [next to 5:60] وَإِذَا نَادَيْتُمْ إِلَى ٱلصَّلَوٰةِ ٱتَّخَذُوهَا هُزُوًۭا وَلَعِبًۭا ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ
- (5:59) [next to 5:60] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ هَلْ تَنقِمُونَ مِنَّآ إِلَّآ أَنْ ءَامَنَّا بِٱللَّهِ وَمَآ أُنزِلَ إِلَيْنَا وَمَآ أُنزِلَ مِن قَبْلُ وَأَنَّ أَكْثَرَكُمْ فَٰسِقُونَ
- (5:61) [next to 5:60] وَإِذَا جَآءُوكُمْ قَالُوٓا۟ ءَامَنَّا وَقَد دَّخَلُوا۟ بِٱلْكُفْرِ وَهُمْ قَدْ خَرَجُوا۟ بِهِۦ ۚ وَٱللَّهُ أَعْلَمُ بِمَا كَانُوا۟ يَكْتُمُونَ
- (5:62) [next to 5:60] وَتَرَىٰ كَثِيرًۭا مِّنْهُمْ يُسَٰرِعُونَ فِى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ وَأَكْلِهِمُ ٱلسُّحْتَ ۚ لَبِئْسَ مَا كَانُوا۟ يَعْمَلُونَ
- (6:69) [next to 6:71] وَمَا عَلَى ٱلَّذِينَ يَتَّقُونَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَلَٰكِن ذِكْرَىٰ لَعَلَّهُمْ يَتَّقُونَ
- (6:70) [next to 6:71] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (6:72) [next to 6:71] وَأَنْ أَقِيمُوا۟ ٱلصَّلَوٰةَ وَٱتَّقُوهُ ۚ وَهُوَ ٱلَّذِىٓ إِلَيْهِ تُحْشَرُونَ
- (6:73) [next to 6:71] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (6:75) [next to 6:77] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (6:76) [next to 6:77] فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ
- (6:78) [next to 6:77] فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ ۖ فَلَمَّآ أَفَلَتْ قَالَ يَٰقَوْمِ إِنِّى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:79) [next to 6:77] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (6:151) [next to 6:153] ۞ قُلْ تَعَالَوْا۟ أَتْلُ مَا حَرَّمَ رَبُّكُمْ عَلَيْكُمْ ۖ أَلَّا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا ۖ وَلَا تَقْتُلُوٓا۟ أَوْلَٰدَكُم مِّنْ إِمْلَٰقٍۢ ۖ نَّحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ ۖ وَلَا تَقْرَبُوا۟ ٱلْفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ ۖ وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
- (6:152) [next to 6:153] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۖ وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَا ۖ وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ ۖ وَبِعَهْدِ ٱللَّهِ أَوْفُوا۟ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَذَكَّرُونَ
- (6:154) [next to 6:153] ثُمَّ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ تَمَامًا عَلَى ٱلَّذِىٓ أَحْسَنَ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُم بِلِقَآءِ رَبِّهِمْ يُؤْمِنُونَ
- (6:155) [next to 6:153] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ فَٱتَّبِعُوهُ وَٱتَّقُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (7:148) [next to 7:150] وَٱتَّخَذَ قَوْمُ مُوسَىٰ مِنۢ بَعْدِهِۦ مِنْ حُلِيِّهِمْ عِجْلًۭا جَسَدًۭا لَّهُۥ خُوَارٌ ۚ أَلَمْ يَرَوْا۟ أَنَّهُۥ لَا يُكَلِّمُهُمْ وَلَا يَهْدِيهِمْ سَبِيلًا ۘ ٱتَّخَذُوهُ وَكَانُوا۟ ظَٰلِمِينَ
- (7:149) [next to 7:150] وَلَمَّا سُقِطَ فِىٓ أَيْدِيهِمْ وَرَأَوْا۟ أَنَّهُمْ قَدْ ضَلُّوا۟ قَالُوا۟ لَئِن لَّمْ يَرْحَمْنَا رَبُّنَا وَيَغْفِرْ لَنَا لَنَكُونَنَّ مِنَ ٱلْخَٰسِرِينَ
- (7:151) [next to 7:150] قَالَ رَبِّ ٱغْفِرْ لِى وَلِأَخِى وَأَدْخِلْنَا فِى رَحْمَتِكَ ۖ وَأَنتَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (7:155) [next to 7:153] وَٱخْتَارَ مُوسَىٰ قَوْمَهُۥ سَبْعِينَ رَجُلًۭا لِّمِيقَٰتِنَا ۖ فَلَمَّآ أَخَذَتْهُمُ ٱلرَّجْفَةُ قَالَ رَبِّ لَوْ شِئْتَ أَهْلَكْتَهُم مِّن قَبْلُ وَإِيَّٰىَ ۖ أَتُهْلِكُنَا بِمَا فَعَلَ ٱلسُّفَهَآءُ مِنَّآ ۖ إِنْ هِىَ إِلَّا فِتْنَتُكَ تُضِلُّ بِهَا مَن تَشَآءُ وَتَهْدِى مَن تَشَآءُ ۖ أَنتَ وَلِيُّنَا فَٱغْفِرْ لَنَا وَٱرْحَمْنَا ۖ وَأَنتَ خَيْرُ ٱلْغَٰفِرِينَ
- (7:156) [next to 7:154] ۞ وَٱكْتُبْ لَنَا فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ إِنَّا هُدْنَآ إِلَيْكَ ۚ قَالَ عَذَابِىٓ أُصِيبُ بِهِۦ مَنْ أَشَآءُ ۖ وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ ۚ فَسَأَكْتُبُهَا لِلَّذِينَ يَتَّقُونَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَٱلَّذِينَ هُم بِـَٔايَٰتِنَا يُؤْمِنُونَ
- (7:177) [next to 7:179] سَآءَ مَثَلًا ٱلْقَوْمُ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا وَأَنفُسَهُمْ كَانُوا۟ يَظْلِمُونَ
- (7:180) [next to 7:179] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
- (7:181) [next to 7:179] وَمِمَّنْ خَلَقْنَآ أُمَّةٌۭ يَهْدُونَ بِٱلْحَقِّ وَبِهِۦ يَعْدِلُونَ
- (8:50) [next to 8:52] وَلَوْ تَرَىٰٓ إِذْ يَتَوَفَّى ٱلَّذِينَ كَفَرُوا۟ ۙ ٱلْمَلَٰٓئِكَةُ يَضْرِبُونَ وُجُوهَهُمْ وَأَدْبَٰرَهُمْ وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (8:51) [next to 8:52] ذَٰلِكَ بِمَا قَدَّمَتْ أَيْدِيكُمْ وَأَنَّ ٱللَّهَ لَيْسَ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
- (8:54) [next to 8:52] كَدَأْبِ ءَالِ فِرْعَوْنَ ۙ وَٱلَّذِينَ مِن قَبْلِهِمْ ۚ كَذَّبُوا۟ بِـَٔايَٰتِ رَبِّهِمْ فَأَهْلَكْنَٰهُم بِذُنُوبِهِمْ وَأَغْرَقْنَآ ءَالَ فِرْعَوْنَ ۚ وَكُلٌّۭ كَانُوا۟ ظَٰلِمِينَ
- (8:55) [next to 8:53] إِنَّ شَرَّ ٱلدَّوَآبِّ عِندَ ٱللَّهِ ٱلَّذِينَ كَفَرُوا۟ فَهُمْ لَا يُؤْمِنُونَ
- (12:4) [next to 12:6] إِذْ قَالَ يُوسُفُ لِأَبِيهِ يَٰٓأَبَتِ إِنِّى رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ رَأَيْتُهُمْ لِى سَٰجِدِينَ
- (12:5) [next to 12:6] قَالَ يَٰبُنَىَّ لَا تَقْصُصْ رُءْيَاكَ عَلَىٰٓ إِخْوَتِكَ فَيَكِيدُوا۟ لَكَ كَيْدًا ۖ إِنَّ ٱلشَّيْطَٰنَ لِلْإِنسَٰنِ عَدُوٌّۭ مُّبِينٌۭ
- (12:7) [next to 12:6] ۞ لَّقَدْ كَانَ فِى يُوسُفَ وَإِخْوَتِهِۦٓ ءَايَٰتٌۭ لِّلسَّآئِلِينَ
- (13:9) [next to 13:11] عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْكَبِيرُ ٱلْمُتَعَالِ
- (13:10) [next to 13:11] سَوَآءٌۭ مِّنكُم مَّنْ أَسَرَّ ٱلْقَوْلَ وَمَن جَهَرَ بِهِۦ وَمَنْ هُوَ مُسْتَخْفٍۭ بِٱلَّيْلِ وَسَارِبٌۢ بِٱلنَّهَارِ
- (13:12) [next to 13:11] هُوَ ٱلَّذِى يُرِيكُمُ ٱلْبَرْقَ خَوْفًۭا وَطَمَعًۭا وَيُنشِئُ ٱلسَّحَابَ ٱلثِّقَالَ
- (13:13) [next to 13:11] وَيُسَبِّحُ ٱلرَّعْدُ بِحَمْدِهِۦ وَٱلْمَلَٰٓئِكَةُ مِنْ خِيفَتِهِۦ وَيُرْسِلُ ٱلصَّوَٰعِقَ فَيُصِيبُ بِهَا مَن يَشَآءُ وَهُمْ يُجَٰدِلُونَ فِى ٱللَّهِ وَهُوَ شَدِيدُ ٱلْمِحَالِ
- (16:7) [next to 16:9] وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ ۚ إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ
- (16:8) [next to 16:9] وَٱلْخَيْلَ وَٱلْبِغَالَ وَٱلْحَمِيرَ لِتَرْكَبُوهَا وَزِينَةًۭ ۚ وَيَخْلُقُ مَا لَا تَعْلَمُونَ
- (16:10) [next to 16:9] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
- (16:11) [next to 16:9] يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ وَٱلنَّخِيلَ وَٱلْأَعْنَٰبَ وَمِن كُلِّ ٱلثَّمَرَٰتِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (16:119) [next to 16:121] ثُمَّ إِنَّ رَبَّكَ لِلَّذِينَ عَمِلُوا۟ ٱلسُّوٓءَ بِجَهَٰلَةٍۢ ثُمَّ تَابُوا۟ مِنۢ بَعْدِ ذَٰلِكَ وَأَصْلَحُوٓا۟ إِنَّ رَبَّكَ مِنۢ بَعْدِهَا لَغَفُورٌۭ رَّحِيمٌ
- (16:120) [next to 16:121] إِنَّ إِبْرَٰهِيمَ كَانَ أُمَّةًۭ قَانِتًۭا لِّلَّهِ حَنِيفًۭا وَلَمْ يَكُ مِنَ ٱلْمُشْرِكِينَ
- (16:122) [next to 16:121] وَءَاتَيْنَٰهُ فِى ٱلدُّنْيَا حَسَنَةًۭ ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
- (16:123) [next to 16:121] ثُمَّ أَوْحَيْنَآ إِلَيْكَ أَنِ ٱتَّبِعْ مِلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۖ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (17:81) [next to 17:83] وَقُلْ جَآءَ ٱلْحَقُّ وَزَهَقَ ٱلْبَٰطِلُ ۚ إِنَّ ٱلْبَٰطِلَ كَانَ زَهُوقًۭا
- (17:82) [next to 17:83] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
- (17:84) [next to 17:83] قُلْ كُلٌّۭ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًۭا
- (17:85) [next to 17:83] وَيَسْـَٔلُونَكَ عَنِ ٱلرُّوحِ ۖ قُلِ ٱلرُّوحُ مِنْ أَمْرِ رَبِّى وَمَآ أُوتِيتُم مِّنَ ٱلْعِلْمِ إِلَّا قَلِيلًۭا
- (19:56) [next to 19:58] وَٱذْكُرْ فِى ٱلْكِتَٰبِ إِدْرِيسَ ۚ إِنَّهُۥ كَانَ صِدِّيقًۭا نَّبِيًّۭا
- (19:57) [next to 19:58] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- (19:60) [next to 19:58] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ شَيْـًۭٔا
- (19:61) [next to 19:59] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (20:78) [next to 20:80] فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ
- (20:79) [next to 20:80] وَأَضَلَّ فِرْعَوْنُ قَوْمَهُۥ وَمَا هَدَىٰ
- (20:83) [next to 20:81] ۞ وَمَآ أَعْجَلَكَ عَن قَوْمِكَ يَٰمُوسَىٰ
- (20:87) [next to 20:85] قَالُوا۟ مَآ أَخْلَفْنَا مَوْعِدَكَ بِمَلْكِنَا وَلَٰكِنَّا حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ فَقَذَفْنَٰهَا فَكَذَٰلِكَ أَلْقَى ٱلسَّامِرِىُّ
- (20:88) [next to 20:86] فَأَخْرَجَ لَهُمْ عِجْلًۭا جَسَدًۭا لَّهُۥ خُوَارٌۭ فَقَالُوا۟ هَٰذَآ إِلَٰهُكُمْ وَإِلَٰهُ مُوسَىٰ فَنَسِىَ
- (25:43) [next to 25:44] أَرَءَيْتَ مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ أَفَأَنتَ تَكُونُ عَلَيْهِ وَكِيلًا
- (25:45) [next to 25:44] أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ وَلَوْ شَآءَ لَجَعَلَهُۥ سَاكِنًۭا ثُمَّ جَعَلْنَا ٱلشَّمْسَ عَلَيْهِ دَلِيلًۭا
- (25:46) [next to 25:44] ثُمَّ قَبَضْنَٰهُ إِلَيْنَا قَبْضًۭا يَسِيرًۭا
- (26:16) [next to 26:18] فَأْتِيَا فِرْعَوْنَ فَقُولَآ إِنَّا رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- (26:17) [next to 26:18] أَنْ أَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ
- (26:19) [next to 26:18] وَفَعَلْتَ فَعْلَتَكَ ٱلَّتِى فَعَلْتَ وَأَنتَ مِنَ ٱلْكَٰفِرِينَ
- (26:23) [next to 26:21] قَالَ فِرْعَوْنُ وَمَا رَبُّ ٱلْعَٰلَمِينَ
- (32:8) [next to 32:10] ثُمَّ جَعَلَ نَسْلَهُۥ مِن سُلَٰلَةٍۢ مِّن مَّآءٍۢ مَّهِينٍۢ
- (32:9) [next to 32:10] ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ ۖ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۚ قَلِيلًۭا مَّا تَشْكُرُونَ
- (32:11) [next to 32:10] ۞ قُلْ يَتَوَفَّىٰكُم مَّلَكُ ٱلْمَوْتِ ٱلَّذِى وُكِّلَ بِكُمْ ثُمَّ إِلَىٰ رَبِّكُمْ تُرْجَعُونَ
- (32:12) [next to 32:10] وَلَوْ تَرَىٰٓ إِذِ ٱلْمُجْرِمُونَ نَاكِسُوا۟ رُءُوسِهِمْ عِندَ رَبِّهِمْ رَبَّنَآ أَبْصَرْنَا وَسَمِعْنَا فَٱرْجِعْنَا نَعْمَلْ صَٰلِحًا إِنَّا مُوقِنُونَ
- (37:21) [next to 37:23] هَٰذَا يَوْمُ ٱلْفَصْلِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (37:22) [next to 37:23] ۞ ٱحْشُرُوا۟ ٱلَّذِينَ ظَلَمُوا۟ وَأَزْوَٰجَهُمْ وَمَا كَانُوا۟ يَعْبُدُونَ
- (37:24) [next to 37:23] وَقِفُوهُمْ ۖ إِنَّهُم مَّسْـُٔولُونَ
- (37:25) [next to 37:23] مَا لَكُمْ لَا تَنَاصَرُونَ
- (48:0) [next to 48:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (48:3) [next to 48:1] وَيَنصُرَكَ ٱللَّهُ نَصْرًا عَزِيزًا
- (48:4) [next to 48:2] هُوَ ٱلَّذِىٓ أَنزَلَ ٱلسَّكِينَةَ فِى قُلُوبِ ٱلْمُؤْمِنِينَ لِيَزْدَادُوٓا۟ إِيمَٰنًۭا مَّعَ إِيمَٰنِهِمْ ۗ وَلِلَّهِ جُنُودُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَكَانَ ٱللَّهُ عَلِيمًا حَكِيمًۭا
- (60:11) [next to 60:13] وَإِن فَاتَكُمْ شَىْءٌۭ مِّنْ أَزْوَٰجِكُمْ إِلَى ٱلْكُفَّارِ فَعَاقَبْتُمْ فَـَٔاتُوا۟ ٱلَّذِينَ ذَهَبَتْ أَزْوَٰجُهُم مِّثْلَ مَآ أَنفَقُوا۟ ۚ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِىٓ أَنتُم بِهِۦ مُؤْمِنُونَ
- (60:12) [next to 60:13] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا جَآءَكَ ٱلْمُؤْمِنَٰتُ يُبَايِعْنَكَ عَلَىٰٓ أَن لَّا يُشْرِكْنَ بِٱللَّهِ شَيْـًۭٔا وَلَا يَسْرِقْنَ وَلَا يَزْنِينَ وَلَا يَقْتُلْنَ أَوْلَٰدَهُنَّ وَلَا يَأْتِينَ بِبُهْتَٰنٍۢ يَفْتَرِينَهُۥ بَيْنَ أَيْدِيهِنَّ وَأَرْجُلِهِنَّ وَلَا يَعْصِينَكَ فِى مَعْرُوفٍۢ ۙ فَبَايِعْهُنَّ وَٱسْتَغْفِرْ لَهُنَّ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (88:6) [next to 88:8] لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- (88:7) [next to 88:8] لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- (88:9) [next to 88:8] لِّسَعْيِهَا رَاضِيَةٌۭ
- (88:10) [next to 88:8] فِى جَنَّةٍ عَالِيَةٍۢ
- (93:4) [next to 93:6] وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ
- (93:5) [next to 93:6] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (93:8) [next to 93:6] وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ
- (93:9) [next to 93:7] فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ

