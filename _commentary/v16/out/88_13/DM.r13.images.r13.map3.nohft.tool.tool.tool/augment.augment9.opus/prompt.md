Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:13; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_13/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_13.reading.tr.md (prose paragraphs numbered) =====
## Yüksek bahçenin içinde kaldırılmış bir yer

[¶1] Ayet üç kelimeden oluşur ve içinde fiil yoktur. Bir olay anlatmaz, bir durumu bildirir: orada sedirler vardır ve kaldırılmış hâlde dururlar. İlk kelime {ar:فِيهَا, tr:fîhâ, gloss:orada, onun içinde, source:88:13} onuncu ayetteki bahçeye döner: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:88:10}. Bu kelime arka arkaya üçüncü kez gelir. On birinci ayet bahçede işitilmeyeni, on ikinci ayet orada akanı söyler. Bu ayet de orada kaldırılmış duranı söyler. Sedirden sonra kadehler, yastıklar ve halılar gelir. Bu dört eşyanın birlikte döşediği oda surenin bütününe aittir. Burada konuşan, o odanın ilk eşyası olan sedirdir.

[¶2] İkinci kelime serîr'in çoğuludur. Bu kelimenin iki çoğulu bilinir: {ar:السرير وجمعه سرر وأسرة, tr:es-serîru ve cem'uhû sururun ve esirra, gloss:serîr; çoğulu surur ve esirra, source:"س ر ر,B011"}. Üçüncü kelime {ar:مَّرْفُوعَةٌ, tr:merfûa, gloss:kaldırılmış, yükseltilmiş, source:88:13} edilgen bir sıfattır. Bir kaldırma işinin yapıldığını ve sonucunun sürdüğünü söyler, ama kaldıranın adını anmaz.

[¶3] Serîr, üzerinde oturulan, yaslanılan ya da yatılan yerdir {source:"س ر ر,B011"}. Araplar onu herkesin tanıdığı bir eşya olarak anarlardı: {ar:السرير معروف, tr:es-serîru ma'rûf, gloss:serir bilinen bir eşyadır, source:"س ر ر,B011"}. Kelime yalnızca bir mobilyayı adlandırmaz. Başın durup yerleştiği yer için de aynı ad kullanılırdı: {ar:سرير الرأس مستقره, tr:serîru'r-ra'si müstekarruh, gloss:başın seriri, onun yerleşip durduğu yerdir, source:"س ر ر,B011"}. Aynı kullanım, yaşamın yerine oturmuş rahatlığını ve dinginliğini de bu kelimeyle anlatır {source:"س ر ر,B011"}. Serir, yürüyen ve çalışan bir bedenin sonunda vardığı ve durduğu yerdir. Türkçede serir kelimesi çoğunlukla taht anlamıyla, saltanat ve törenle birlikte akla gelir. Ayetteki kelime ise önce bir oturma ve dinlenme yeridir. Ayetteki yükseklik ve şeref, sedirin adından değil, ona eklenen kaldırılmış sıfatından gelir.

## Sevinçten adını alan sedir

[¶4] Kelime ailesinden gelen resimler, kelimenin bu ayetteki anlamının yanında duyulur, onun yerine geçmez. Ayette sedir yine bir sedirdir. Ama Arap kulağı onun adında başka bir şey de duyar. Üstüne oturulan sedirin adını sevinçten aldığı söylenirdi: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan serir adını sürurdan, yani sevinçten alır, source:"س ر ر,B011"}. Türk okur sır, sürur ve serir kelimelerini birbirinden ayrı üç kelime olarak bilir. Arapçada bu üçü aynı köktendir. Kök birliği kesindir. Sedirin adını sevinçten aldığı ise Arapların kendi açıklamasıdır. Sevincin kendisi de bir yokluk üzerinden tanımlanır: {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sürur, kederden boş bir hâldir, source:"س ر ر,B010"}. Aynı kökten gelen bir başka kelime de bolluğu darlığın karşısına koyar: {ar:السراء الرخاء نقيض الضراء, tr:es-serrâu'r-rahâu nakîdu'd-darrâ', gloss:serrâ, darlığın zıddı olan bolluk ve rahatlıktır, source:"س ر ر,B010"}. Böylece sedirin adında oturmanın yanında kederin bitişi de duyulur.

[¶5] Kur'an bahçe halkının ilk şükrünü de tam bu yoklukla anlatır. Fâtır suresinde Adn bahçelerine girenler altın bilezikler ve inci takınmış, ipekler giymiş olarak anılır {source:35:33}. Ardından kendi sözleri gelir: {ar:وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَذْهَبَ عَنَّا ٱلْحَزَنَ, tr:ve kâlu'l-hamdu lillâhi'llezî ezhebe anne'l-hazen, gloss:dediler ki: bizden kederi gideren Allah'a hamd olsun, source:35:34}. Bir sonraki ayette, orada kendilerine yorgunluk dokunmadığını söylerler {source:35:35}. Sevincin tanımındaki keder kelimesi ile bahçe halkının gitti dediği keder aynı kelimedir. İnsan suresinde de iyiler korkularını söyler: {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfu min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık yüzlü, çetin bir günden korkarız, source:76:10}. Karşılık da şöyle gelir: {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevmi ve lekkâhum nadraten ve surûrâ, gloss:Allah onları o günün kötülüğünden korudu, onlara tazelik ve sevinç kavuşturdu, source:76:11}. İki ayet sonra bu insanlar yaslanmış hâlde anılır {source:76:13}. Asık yüzlü bir günden korkanlara verilen şey sevinçtir. Sevinçten adını alan eşya da onların oturduğu yerdir.

[¶6] Ama sevinç kendi başına bir müjde değildir. İnşikâk suresi aynı kelimeyi iki insan için kullanır. Kitabı sağından verilen, kolay bir hesapla hesaba çekilir {source:84:8} ve {ar:وَيَنقَلِبُ إِلَىٰٓ أَهْلِهِۦ مَسْرُورًۭا, tr:ve yenkalibu ilâ ehlihî mesrûrâ, gloss:ailesine sevinçli olarak döner, source:84:9}. Kitabı arkasından verilen için ise şöyle denir: {ar:إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:innehû kâne fî ehlihî mesrûrâ, gloss:o, ailesi içinde sevinçliydi, source:84:13}. Birinin sevinci hesaptan sonra gelir. Ötekininki hesaptan önce yaşanmış ve bitmiştir. Sedirin kendisi de böyledir. Zuhruf suresinde Allah, insanlar inkârda tek bir topluluk olacak olmasa, Rahman'ı inkâr edenlere neler vereceğini sayar: evlerine gümüşten tavanlar ve üstüne çıkacakları merdivenler {source:43:33}, sonra {ar:وَلِبُيُوتِهِمْ أَبْوَٰبًۭا وَسُرُرًا عَلَيْهَا يَتَّكِـُٔونَ, tr:ve li-buyûtihim ebvâben ve sururan aleyhâ yettekiûn, gloss:evlerine kapılar ve üzerine yaslanacakları sedirler, source:43:34}. Hüküm hemen arkasından gelir: {ar:وَإِن كُلُّ ذَٰلِكَ لَمَّا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَٱلْءَاخِرَةُ عِندَ رَبِّكَ لِلْمُتَّقِينَ, tr:ve in küllü zâlike lemmâ metâu'l-hayâti'd-dunyâ, ve'l-âhiratu inde rabbike li'l-muttekîn, gloss:bütün bunlar dünya hayatının geçici yararlanmasından başka bir şey değildir; ahiret ise Rabbinin katında takva sahipleri içindir, source:43:35}. Burada da aynı kelime vardır, sedirler yüksek tavanların altındadır, ama değerleri yoktur. Bu ayetteki sedirleri ayıran, ilk kelimedir: onlar yüksek bahçenin içindedir. Dokuzuncu ayetteki, emeğinden hoşnut yüzün vardığı yerdir. Üçüncü ayette emeği yorgunluğa dönen yüzle bu sedirin karşı karşıya gelişi surenin kurduğu sahnedir.

## Saklı olan ve yükseltilen

[¶7] Kökün en geniş kolu saklamaktır: {ar:السر خلاف الإعلان, tr:es-sirru hılâfu'l-i'lân, gloss:sır, açığa vurmanın karşıtıdır, source:"س ر ر,B001"}. Gizli yapılan işin adı da bu kökten gelir: {ar:السر ما أسررت والسريرة عمل السر, tr:es-sirru mâ eserart ve's-serîratu amelu's-sirr, gloss:sır gizlediğin şeydir; serîra da gizlice yapılan iştir, source:"س ر ر,B001"}. Sevincin bir tanımı da onu bu saklılığa bağlar: {ar:السرور ما ينكتم من الفرح, tr:es-surûru mâ yenketimu mine'l-ferah, gloss:sürur, sevincin içte saklı kalan kısmıdır, source:"س ر ر,B010"}. Bu tanıma göre sürur dışa taşan bir coşku değildir. İnsanın içinde tuttuğu bir sevinçtir. Gizli işin adı olan serîra ile sedirin adı olan serîr arasında yalnızca bir son harf fark vardır. Aynı kökten gelen iki ayrı kelimedir.

[¶8] Bu surenin iki sure öncesinde, Târık suresinde, birincisinin çoğulu geçer. İnsana neden yaratıldığına bakması söylenir. Sonra Allah'ın onu geri döndürmeye gücünün yettiği bildirilir: {ar:إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌۭ, tr:innehû alâ rac'ihî le-kâdir, gloss:O, onu geri döndürmeye elbette güç yetirendir, source:86:8}. Hemen ardından o dönüşün günü anlatılır: {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tuble's-serâir, gloss:saklı olanların sınandığı gün, source:86:9}. Sonraki ayet o gün insanın ne gücünün ne yardımcısının olduğunu söyler {source:86:10}. Serâir, serîra'nın çoğuludur. Bu ayetteki surur da serîr'in çoğuludur. İkisinin yan yana getirilmesi kelimelerin değil, bu yorumun işidir. Ama kök aynı olduğu için bağ boş değildir. Saklı olanların sınandığı bir günün öbür yanında, aynı kökten adlanmış yerler kaldırılmış durur.

[¶9] Ayetin ikinci kelimesinin kökünde de bir açığa çıkarma vardır: {ar:الرفع إذاعة الشيء وإظهاره, tr:er-ref'u izâatu'ş-şey'i ve izhâruh, gloss:ref', bir şeyi duyurmak ve ortaya çıkarmaktır, source:"ر ف ع,B005"}. Böylece ayetin iki kelimesi, biri saklama kökünden, öteki açığa çıkarma anlamı da taşıyan bir kökten gelir. Bu, ayetin anlamının yanında duyulan bir şeydir. Ayet, kaldırılmış sedirleri anlatır. Yanında ise içte saklı tutulan sevincin yüksek ve görünen bir yer bulduğu duyulur.

[¶10] Kur'an sedirleri bir yerde tam da içte saklı olanın çıkarılmasıyla birlikte anar. Hicr suresinde Allah takva sahiplerinin bahçeler ve pınarlar arasında olduğunu söyler {source:15:45}. Onlara esenlikle ve güven içinde girmeleri söylenir {source:15:46}. Sonra şöyle denir: {ar:وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:ve neza'nâ mâ fî sudûrihim min ğillin ihvânen alâ sururin mutekâbilîn, gloss:göğüslerinde kinden ne varsa çekip çıkardık; sedirler üstünde karşı karşıya oturan kardeşler olarak, source:15:47}. Göğüste gizlenen kin söküldükten sonra insanlar sedirlerde yüz yüze otururlar. Yüz yüze oturan iki kişi birbirinden bir şey saklamaz. Bir sonraki ayet de orada onlara yorgunluk dokunmadığını söyler {source:15:48}. Araf suresinde göğüslerden kinin çekilip alınması, altlarından ırmakların akmasıyla birlikte anlatılır {source:7:43}. On ikinci ayetteki akan pınar ile bu sedirin aynı bahçede oluşu da bu resme uyar. Saffât suresinde Allah'ın ihlaslı kulları da ikramla ağırlanan kimseler olarak anılır {source:37:42}. Nimet bahçelerinde {source:37:43} şu hâlde bulunurlar: {ar:عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:alâ sururin mutekâbilîn, gloss:karşılıklı sedirler üstünde, source:37:44}. Aynı kök, insanın en yakın dostunu da adlandırırdı: {ar:سرسوري وسرسورتي أي حبيبي وخاصتي, tr:sursûrî ve sursûratî ey habîbî ve hâssatî, gloss:sursûrum, yani sevdiğim ve en yakınım, source:"س ر ر,B014"}. Sırrın paylaşıldığı yakınlık, karşılıklı sedirlerde herkese açık bir kardeşliğe dönüşür.

[¶11] Yûsuf suresinin sonunda aynı hareket kelimeleri paylaşmadan sahnelenir. Yakub, oğlu için yıllarca ağlamıştır: {ar:وَٱبْيَضَّتْ عَيْنَاهُ مِنَ ٱلْحُزْنِ فَهُوَ كَظِيمٌۭ, tr:vebyaddat aynâhu mine'l-huzni fe-huve kezîm, gloss:kederden gözleri ağardı; acısını içine gömüyordu, source:12:84}. Aile Mısır'a geldiğinde Yûsuf anne babasını yanına alır ve onlara güven içinde girmelerini söyler {source:12:99}. Sonra: {ar:وَرَفَعَ أَبَوَيْهِ عَلَى ٱلْعَرْشِ, tr:ve rafea ebeveyhi ale'l-arş, gloss:anne babasını tahtın üstüne yükseltti, source:12:100}. Aynı ayette Yûsuf, Rabbinin ona iyilik ettiğini, şeytan kendisiyle kardeşlerinin arasını bozduktan sonra ailesini çölden getirdiğini söyler: {ar:مِنۢ بَعْدِ أَن نَّزَغَ ٱلشَّيْطَٰنُ بَيْنِى وَبَيْنَ إِخْوَتِىٓ, tr:min ba'di en nezeğa'ş-şeytânu beynî ve beyne ihvetî, gloss:şeytan benimle kardeşlerimin arasını bozduktan sonra, source:12:100}. Oradaki oturak kelimesi başkadır, ama fiil bu ayetteki sıfatın fiilidir. Keder biter, kardeşler arasındaki bozgunluk kapanır ve sevilen kişiler yükseltilmiş bir yere oturtulur. Hicr suresindeki bahçede de kin çıkarılır, kardeşler sedirlere oturur. İki sahne arasındaki bu benzerlik bir kelime birliği değil, bir hareket birliğidir.

## Kaldırmak: yukarı, yakın ve şerefli

[¶12] Kaldırmanın ilk anlamı bedenseldir ve alçaltmanın karşıtıdır: {ar:رفعت الشيء رفعا وهو خلاف الخفض, tr:rafa'tu'ş-şey'e raf'an ve huve hılâfu'l-hafd, gloss:bir şeyi kaldırdım; bu alçaltmanın karşıtıdır, source:"ر ف ع,B001"}. Bu kaldırma bir yerde duran şeyden başlar: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlü fi'l-ecsâmi'l-mevdûati izâ a'leytehâ an makarrihâ, gloss:yere konmuş cisimleri durdukları yerden yukarı aldığında ref' denir, source:"ر ف ع,B001"}. Bu tanımda konmuş anlamındaki kelime, bir sonraki ayette kadehlerin sıfatı olarak gelir. Sedirler kaldırılmış, kadehler konmuştur. Araplar bu iki kelimeyi devenin yürüyüşü için de birbirinin karşıtı olarak kullanırlardı: {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:dişi devenin yürüyüşünde merfû, mevdûun karşıtıdır, source:"ر ف ع,B003"}. Bu hızlı yürüyüş, ağır adımla dörtnal arasında bir hızdır {source:"ر ف ع,B003"}. Bu resim, on yedinci ayette bakılması istenen deveyle birlikte surenin sahnesine aittir.

[¶13] Kaldırmak, şerefi de anlatır: {ar:رجل رفيع أي شريف, tr:racülün rafî' ey şerîf, gloss:refi' adam, yani şerefli adam, source:"ر ف ع,B002"}. Bu yüksekliğin karşıtı aşağılanmadır: {ar:الرفعة نقيض الذلة, tr:er-rif'atu nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. Kaldırılmış bir sedir, üstüne oturanın da ağırlandığını gösterir. İkinci ayetteki yere eğilmiş yüz ile bu sedirin yüksekliği aynı surede karşı karşıya durur. Vâkıa suresi o günü bu iki hareketle adlandırır: {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}.

[¶14] Kökün bir başka kolu yüksekliği yakınlığa bağlar: {ar:الرفع تقريب الشيء, tr:er-ref'u takrîbu'ş-şey', gloss:ref', bir şeyi yaklaştırmaktır, source:"ر ف ع,B004"}. Aynı kol, döşeklerin kullanacak olanlara yaklaştırılmasını da anlatır {source:"ر ف ع,B004"}. Bu anlam, ayetteki kaldırmanın yanında bir uzaklık değil, bir yakınlık da duyurur. Kur'an da yükseklik ile yakınlığı aynı bahçede birleştirir. Hâkka suresinde kitabı sağından verilen kişi sevinçle {ar:هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ, tr:hâumu'kraû kitâbiyeh, gloss:alın, kitabımı okuyun, source:69:19} der. Sonra onun hâli bu surenin kelimeleriyle anlatılır: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o, hoşnut olunan bir hayattadır, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:69:22}; {ar:قُطُوفُهَا دَانِيَةٌۭ, tr:kutûfuhâ dâniye, gloss:salkımları yakındır, source:69:23}. Bahçe yüksektir, ama meyvesi uzanacak kadar yakındır. Ardından {ar:كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ, tr:kulû veşrabû henîen bimâ esleftum fi'l-eyyâmi'l-hâliye, gloss:geçmiş günlerde önden gönderdiklerinize karşılık afiyetle yiyin için, source:69:24} denir. Yüksek bahçenin içindeki kaldırılmış sedir de böyle yakındır. Vâkıa suresinde öne geçenler {ar:أُو۟لَٰٓئِكَ ٱلْمُقَرَّبُونَ, tr:ülâike'l-mukarrabûn, gloss:işte onlar yaklaştırılmış olanlardır, source:56:11} diye anılır. Nimet bahçelerinde {source:56:12} sedirlere yaslanmış, karşı karşıya otururlar: {ar:مُّتَّكِـِٔينَ عَلَيْهَا مُتَقَٰبِلِينَ, tr:muttekiîne aleyhâ mutekâbilîn, gloss:onların üzerine karşılıklı yaslanmış olarak, source:56:16}. Sağın adamları için de bu ayetin sıfatı kullanılır: {ar:وَفُرُشٍۢ مَّرْفُوعَةٍ, tr:ve furuşin merfûa, gloss:ve kaldırılmış döşekler, source:56:34}. Yaklaştırılmış kelimesi başka bir köktendir. Ama ref' kelimesi yaklaştırmak diye açıklandığında, sedirlerdeki yaklaştırılmışlar ile kaldırılmış döşekler aynı düşünceyi paylaşır.

[¶15] Sedirleri kimin kaldırdığı söylenmez. Surede bu fiilin aynı edilgen biçimi yalnız bir kez daha, on sekizinci ayette gök için geçer: {ar:وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ, tr:ve ile's-semâi keyfe rufiat, gloss:göğe de bakmazlar mı, nasıl kaldırılmış, source:88:18}. Bahçedeki sedir ile dünyanın tavanını aynı fiile bağlayan sahne surenin bütününe aittir. Bu ayette ise fiil bir eşyanın üzerinde durur. Yüksek bahçede dinlenen bir beden için yerden kaldırılmış bir yer vardır. O yerin adı sevinçten gelir. Kaldırılması hem yüksekliği hem şerefi hem de yakınlığı taşır.

===== _commentary/v16/out/88_13/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: عرش in 12:100 denotes a raised royal seat, distinct from سرير
- not written: س ر ر B002 (أسررته = "disclosed") - contested sense; the disclosure idea was carried by ر ف ع B005 instead
- not written: س ر ر B003 (sirr = marriage/intercourse) - no ground in this ayah's theme
- not written: س ر ر B004 (moon's hidden last nights) - no link beyond hiding, already carried by B001
- not written: س ر ر B005 (pure core, best soil of a valley) - tempting with the garden but no usage ties it to seats
- not written: س ر ر B006/B007/B008 (navel, camel chest disease, hollow stick) - no work in any theme
- not written: س ر ر B009 (lines of palm and forehead) - link to faces of 88:8 would need usage not supplied
- not written: س ر ر B012/B013/B015 (plant tips, truffle crust, sand on a hillock) - fixed-expression senses, no theme
- not written: ر ف ع B004 presenting before a ruler, link to 88:25-26 reckoning - too thin
- not written: ر ف ع B006/B007/B008/B009/B010/B011/B012 (harvest carrying, milk retention, hip pad, fetter rope, loud voice, travelling inland, nominative case) - no theme here
- not written: 35:10 good deed raised - pronoun ambiguity, link to 88:9 striving unsure
- not written: 56:15 سرر موضونة and 52:20 سرر مصفوفة - belong to the room scene of the surah commentary

===== passages not cited (160) =====
## strong (this ayah's own list) (9)

- (12:100) [listed for 88:13] [cited in ¶11] وَرَفَعَ أَبَوَيْهِ عَلَى ٱلْعَرْشِ وَخَرُّوا۟ لَهُۥ سُجَّدًۭا ۖ وَقَالَ يَٰٓأَبَتِ هَٰذَا تَأْوِيلُ رُءْيَٰىَ مِن قَبْلُ قَدْ جَعَلَهَا رَبِّى حَقًّۭا ۖ وَقَدْ أَحْسَنَ بِىٓ إِذْ أَخْرَجَنِى مِنَ ٱلسِّجْنِ وَجَآءَ بِكُم مِّنَ ٱلْبَدْوِ مِنۢ بَعْدِ أَن نَّزَغَ ٱلشَّيْطَٰنُ بَيْنِى وَبَيْنَ إِخْوَتِىٓ ۚ إِنَّ رَبِّى لَطِيفٌۭ لِّمَا يَشَآءُ ۚ إِنَّهُۥ هُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ
- (15:47) [listed for 88:13] [cited in ¶10] وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ
- (52:20) [listed for 88:13] مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ ۖ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (56:15) [listed for 88:13] عَلَىٰ سُرُرٍۢ مَّوْضُونَةٍۢ
- (56:16) [listed for 88:13] [cited in ¶14] مُّتَّكِـِٔينَ عَلَيْهَا مُتَقَٰبِلِينَ
- (56:34) [listed for 88:13] [cited in ¶14] وَفُرُشٍۢ مَّرْفُوعَةٍ
- (76:13) [listed for 88:13] [cited in ¶5] مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۖ لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا
- (80:14) [listed for 88:13] مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ
- (83:23) [listed for 88:13] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ

## medium (this ayah's own list) (22)

- (2:127) [listed for 88:13] وَإِذْ يَرْفَعُ إِبْرَٰهِۦمُ ٱلْقَوَاعِدَ مِنَ ٱلْبَيْتِ وَإِسْمَٰعِيلُ رَبَّنَا تَقَبَّلْ مِنَّآ ۖ إِنَّكَ أَنتَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (4:158) [listed for 88:13] بَل رَّفَعَهُ ٱللَّهُ إِلَيْهِ ۚ وَكَانَ ٱللَّهُ عَزِيزًا حَكِيمًۭا
- (6:165) [listed for 88:13] وَهُوَ ٱلَّذِى جَعَلَكُمْ خَلَٰٓئِفَ ٱلْأَرْضِ وَرَفَعَ بَعْضَكُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَبْلُوَكُمْ فِى مَآ ءَاتَىٰكُمْ ۗ إِنَّ رَبَّكَ سَرِيعُ ٱلْعِقَابِ وَإِنَّهُۥ لَغَفُورٌۭ رَّحِيمٌۢ
- (7:176) [listed for 88:13] وَلَوْ شِئْنَا لَرَفَعْنَٰهُ بِهَا وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ ۚ فَمَثَلُهُۥ كَمَثَلِ ٱلْكَلْبِ إِن تَحْمِلْ عَلَيْهِ يَلْهَثْ أَوْ تَتْرُكْهُ يَلْهَث ۚ ذَّٰلِكَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا ۚ فَٱقْصُصِ ٱلْقَصَصَ لَعَلَّهُمْ يَتَفَكَّرُونَ
- (13:2) [listed for 88:13] ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا ۖ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۖ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّۭى ۚ يُدَبِّرُ ٱلْأَمْرَ يُفَصِّلُ ٱلْءَايَٰتِ لَعَلَّكُم بِلِقَآءِ رَبِّكُمْ تُوقِنُونَ
- (18:31) [listed for 88:13] أُو۟لَٰٓئِكَ لَهُمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَيَلْبَسُونَ ثِيَابًا خُضْرًۭا مِّن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًۭا
- (19:57) [listed for 88:13] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- (24:36) [listed for 88:13] فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ
- (36:56) [listed for 88:13] هُمْ وَأَزْوَٰجُهُمْ فِى ظِلَٰلٍ عَلَى ٱلْأَرَآئِكِ مُتَّكِـُٔونَ
- (37:44) [listed for 88:13] [cited in ¶10] عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ
- (39:20) [listed for 88:13] لَٰكِنِ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ لَهُمْ غُرَفٌۭ مِّن فَوْقِهَا غُرَفٌۭ مَّبْنِيَّةٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَعْدَ ٱللَّهِ ۖ لَا يُخْلِفُ ٱللَّهُ ٱلْمِيعَادَ
- (40:15) [listed for 88:13] رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ
- (43:34) [listed for 88:13] [cited in ¶6] وَلِبُيُوتِهِمْ أَبْوَٰبًۭا وَسُرُرًا عَلَيْهَا يَتَّكِـُٔونَ
- (52:5) [listed for 88:13] وَٱلسَّقْفِ ٱلْمَرْفُوعِ
- (55:7) [listed for 88:13] وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
- (55:54) [listed for 88:13] مُتَّكِـِٔينَ عَلَىٰ فُرُشٍۭ بَطَآئِنُهَا مِنْ إِسْتَبْرَقٍۢ ۚ وَجَنَى ٱلْجَنَّتَيْنِ دَانٍۢ
- (55:76) [listed for 88:13] مُتَّكِـِٔينَ عَلَىٰ رَفْرَفٍ خُضْرٍۢ وَعَبْقَرِىٍّ حِسَانٍۢ
- (56:3) [listed for 88:13] [cited in ¶13] خَافِضَةٌۭ رَّافِعَةٌ
- (79:28) [listed for 88:13] رَفَعَ سَمْكَهَا فَسَوَّىٰهَا
- (83:35) [listed for 88:13] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ
- (84:9) [listed for 88:13] [cited in ¶6] وَيَنقَلِبُ إِلَىٰٓ أَهْلِهِۦ مَسْرُورًۭا
- (94:4) [listed for 88:13] وَرَفَعْنَا لَكَ ذِكْرَكَ

## named by the passage's own list as strong for this ayah (10)

- (25:24) [listed for 88:13] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (36:55) [listed for 88:13] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (37:42) [listed for 88:13] [cited in ¶10] فَوَٰكِهُ ۖ وَهُم مُّكْرَمُونَ
- (38:51) [listed for 88:13] مُتَّكِـِٔينَ فِيهَا يَدْعُونَ فِيهَا بِفَٰكِهَةٍۢ كَثِيرَةٍۢ وَشَرَابٍۢ
- (41:32) [listed for 88:13] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (43:71) [listed for 88:13] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (56:12) [listed for 88:13] [cited in ¶14] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (76:11) [listed for 88:13] [cited in ¶5] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (76:21) [listed for 88:13] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:43) [listed for 88:13] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ

## named by the passage's own list as medium for this ayah (13)

- (37:46) [listed for 88:13] بَيْضَآءَ لَذَّةٍۢ لِّلشَّٰرِبِينَ
- (37:62) [listed for 88:13] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (44:52) [listed for 88:13] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (44:55) [listed for 88:13] يَدْعُونَ فِيهَا بِكُلِّ فَٰكِهَةٍ ءَامِنِينَ
- (52:18) [listed for 88:13] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (52:19) [listed for 88:13] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (54:55) [listed for 88:13] فِى مَقْعَدِ صِدْقٍ عِندَ مَلِيكٍۢ مُّقْتَدِرٍۭ
- (56:89) [listed for 88:13] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (77:41) [listed for 88:13] إِنَّ ٱلْمُتَّقِينَ فِى ظِلَٰلٍۢ وَعُيُونٍۢ
- (83:22) [listed for 88:13] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:26) [listed for 88:13] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ
- (84:13) [listed for 88:13] [cited in ¶6] إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا
- (101:7) [listed for 88:13] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## weak (this ayah's own list) (34)

- (2:63) [listed for 88:13] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (2:69) [listed for 88:13] قَالُوا۟ ٱدْعُ لَنَا رَبَّكَ يُبَيِّن لَّنَا مَا لَوْنُهَا ۚ قَالَ إِنَّهُۥ يَقُولُ إِنَّهَا بَقَرَةٌۭ صَفْرَآءُ فَاقِعٌۭ لَّوْنُهَا تَسُرُّ ٱلنَّٰظِرِينَ
- (2:77) [listed for 88:13] أَوَلَا يَعْلَمُونَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
- (2:235) [listed for 88:13] وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا عَرَّضْتُم بِهِۦ مِنْ خِطْبَةِ ٱلنِّسَآءِ أَوْ أَكْنَنتُمْ فِىٓ أَنفُسِكُمْ ۚ عَلِمَ ٱللَّهُ أَنَّكُمْ سَتَذْكُرُونَهُنَّ وَلَٰكِن لَّا تُوَاعِدُوهُنَّ سِرًّا إِلَّآ أَن تَقُولُوا۟ قَوْلًۭا مَّعْرُوفًۭا ۚ وَلَا تَعْزِمُوا۟ عُقْدَةَ ٱلنِّكَاحِ حَتَّىٰ يَبْلُغَ ٱلْكِتَٰبُ أَجَلَهُۥ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِىٓ أَنفُسِكُمْ فَٱحْذَرُوهُ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
- (2:253) [listed for 88:13] ۞ تِلْكَ ٱلرُّسُلُ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۘ مِّنْهُم مَّن كَلَّمَ ٱللَّهُ ۖ وَرَفَعَ بَعْضَهُمْ دَرَجَٰتٍۢ ۚ وَءَاتَيْنَا عِيسَى ٱبْنَ مَرْيَمَ ٱلْبَيِّنَٰتِ وَأَيَّدْنَٰهُ بِرُوحِ ٱلْقُدُسِ ۗ وَلَوْ شَآءَ ٱللَّهُ مَا ٱقْتَتَلَ ٱلَّذِينَ مِنۢ بَعْدِهِم مِّنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ وَلَٰكِنِ ٱخْتَلَفُوا۟ فَمِنْهُم مَّنْ ءَامَنَ وَمِنْهُم مَّن كَفَرَ ۚ وَلَوْ شَآءَ ٱللَّهُ مَا ٱقْتَتَلُوا۟ وَلَٰكِنَّ ٱللَّهَ يَفْعَلُ مَا يُرِيدُ
- (2:274) [listed for 88:13] ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُم بِٱلَّيْلِ وَٱلنَّهَارِ سِرًّۭا وَعَلَانِيَةًۭ فَلَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (3:55) [listed for 88:13] إِذْ قَالَ ٱللَّهُ يَٰعِيسَىٰٓ إِنِّى مُتَوَفِّيكَ وَرَافِعُكَ إِلَىَّ وَمُطَهِّرُكَ مِنَ ٱلَّذِينَ كَفَرُوا۟ وَجَاعِلُ ٱلَّذِينَ ٱتَّبَعُوكَ فَوْقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۖ ثُمَّ إِلَىَّ مَرْجِعُكُمْ فَأَحْكُمُ بَيْنَكُمْ فِيمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
- (4:154) [listed for 88:13] وَرَفَعْنَا فَوْقَهُمُ ٱلطُّورَ بِمِيثَٰقِهِمْ وَقُلْنَا لَهُمُ ٱدْخُلُوا۟ ٱلْبَابَ سُجَّدًۭا وَقُلْنَا لَهُمْ لَا تَعْدُوا۟ فِى ٱلسَّبْتِ وَأَخَذْنَا مِنْهُم مِّيثَٰقًا غَلِيظًۭا
- (5:52) [listed for 88:13] فَتَرَى ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ يُسَٰرِعُونَ فِيهِمْ يَقُولُونَ نَخْشَىٰٓ أَن تُصِيبَنَا دَآئِرَةٌۭ ۚ فَعَسَى ٱللَّهُ أَن يَأْتِىَ بِٱلْفَتْحِ أَوْ أَمْرٍۢ مِّنْ عِندِهِۦ فَيُصْبِحُوا۟ عَلَىٰ مَآ أَسَرُّوا۟ فِىٓ أَنفُسِهِمْ نَٰدِمِينَ
- (10:54) [listed for 88:13] وَلَوْ أَنَّ لِكُلِّ نَفْسٍۢ ظَلَمَتْ مَا فِى ٱلْأَرْضِ لَٱفْتَدَتْ بِهِۦ ۗ وَأَسَرُّوا۟ ٱلنَّدَامَةَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ ۖ وَقُضِىَ بَيْنَهُم بِٱلْقِسْطِ ۚ وَهُمْ لَا يُظْلَمُونَ
- (13:10) [listed for 88:13] سَوَآءٌۭ مِّنكُم مَّنْ أَسَرَّ ٱلْقَوْلَ وَمَن جَهَرَ بِهِۦ وَمَنْ هُوَ مُسْتَخْفٍۭ بِٱلَّيْلِ وَسَارِبٌۢ بِٱلنَّهَارِ
- (16:19) [listed for 88:13] وَٱللَّهُ يَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ
- (20:62) [listed for 88:13] فَتَنَٰزَعُوٓا۟ أَمْرَهُم بَيْنَهُمْ وَأَسَرُّوا۟ ٱلنَّجْوَىٰ
- (21:3) [listed for 88:13] لَاهِيَةًۭ قُلُوبُهُمْ ۗ وَأَسَرُّوا۟ ٱلنَّجْوَى ٱلَّذِينَ ظَلَمُوا۟ هَلْ هَٰذَآ إِلَّا بَشَرٌۭ مِّثْلُكُمْ ۖ أَفَتَأْتُونَ ٱلسِّحْرَ وَأَنتُمْ تُبْصِرُونَ
- (25:6) [listed for 88:13] قُلْ أَنزَلَهُ ٱلَّذِى يَعْلَمُ ٱلسِّرَّ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ كَانَ غَفُورًۭا رَّحِيمًۭا
- (25:75) [listed for 88:13] أُو۟لَٰٓئِكَ يُجْزَوْنَ ٱلْغُرْفَةَ بِمَا صَبَرُوا۟ وَيُلَقَّوْنَ فِيهَا تَحِيَّةًۭ وَسَلَٰمًا
- (29:58) [listed for 88:13] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (34:33) [listed for 88:13] وَقَالَ ٱلَّذِينَ ٱسْتُضْعِفُوا۟ لِلَّذِينَ ٱسْتَكْبَرُوا۟ بَلْ مَكْرُ ٱلَّيْلِ وَٱلنَّهَارِ إِذْ تَأْمُرُونَنَآ أَن نَّكْفُرَ بِٱللَّهِ وَنَجْعَلَ لَهُۥٓ أَندَادًۭا ۚ وَأَسَرُّوا۟ ٱلنَّدَامَةَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ وَجَعَلْنَا ٱلْأَغْلَٰلَ فِىٓ أَعْنَاقِ ٱلَّذِينَ كَفَرُوا۟ ۚ هَلْ يُجْزَوْنَ إِلَّا مَا كَانُوا۟ يَعْمَلُونَ
- (34:37) [listed for 88:13] وَمَآ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُم بِٱلَّتِى تُقَرِّبُكُمْ عِندَنَا زُلْفَىٰٓ إِلَّا مَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ لَهُمْ جَزَآءُ ٱلضِّعْفِ بِمَا عَمِلُوا۟ وَهُمْ فِى ٱلْغُرُفَٰتِ ءَامِنُونَ
- (35:10) [listed for 88:13] مَن كَانَ يُرِيدُ ٱلْعِزَّةَ فَلِلَّهِ ٱلْعِزَّةُ جَمِيعًا ۚ إِلَيْهِ يَصْعَدُ ٱلْكَلِمُ ٱلطَّيِّبُ وَٱلْعَمَلُ ٱلصَّٰلِحُ يَرْفَعُهُۥ ۚ وَٱلَّذِينَ يَمْكُرُونَ ٱلسَّيِّـَٔاتِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۖ وَمَكْرُ أُو۟لَٰٓئِكَ هُوَ يَبُورُ
- (36:76) [listed for 88:13] فَلَا يَحْزُنكَ قَوْلُهُمْ ۘ إِنَّا نَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
- (43:32) [listed for 88:13] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (43:80) [listed for 88:13] أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ
- (47:26) [listed for 88:13] ذَٰلِكَ بِأَنَّهُمْ قَالُوا۟ لِلَّذِينَ كَرِهُوا۟ مَا نَزَّلَ ٱللَّهُ سَنُطِيعُكُمْ فِى بَعْضِ ٱلْأَمْرِ ۖ وَٱللَّهُ يَعْلَمُ إِسْرَارَهُمْ
- (49:2) [listed for 88:13] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَرْفَعُوٓا۟ أَصْوَٰتَكُمْ فَوْقَ صَوْتِ ٱلنَّبِىِّ وَلَا تَجْهَرُوا۟ لَهُۥ بِٱلْقَوْلِ كَجَهْرِ بَعْضِكُمْ لِبَعْضٍ أَن تَحْبَطَ أَعْمَٰلُكُمْ وَأَنتُمْ لَا تَشْعُرُونَ
- (58:11) [listed for 88:13] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قِيلَ لَكُمْ تَفَسَّحُوا۟ فِى ٱلْمَجَٰلِسِ فَٱفْسَحُوا۟ يَفْسَحِ ٱللَّهُ لَكُمْ ۖ وَإِذَا قِيلَ ٱنشُزُوا۟ فَٱنشُزُوا۟ يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ وَٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ دَرَجَٰتٍۢ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (60:1) [listed for 88:13] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ عَدُوِّى وَعَدُوَّكُمْ أَوْلِيَآءَ تُلْقُونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَقَدْ كَفَرُوا۟ بِمَا جَآءَكُم مِّنَ ٱلْحَقِّ يُخْرِجُونَ ٱلرَّسُولَ وَإِيَّاكُمْ ۙ أَن تُؤْمِنُوا۟ بِٱللَّهِ رَبِّكُمْ إِن كُنتُمْ خَرَجْتُمْ جِهَٰدًۭا فِى سَبِيلِى وَٱبْتِغَآءَ مَرْضَاتِى ۚ تُسِرُّونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَأَنَا۠ أَعْلَمُ بِمَآ أَخْفَيْتُمْ وَمَآ أَعْلَنتُمْ ۚ وَمَن يَفْعَلْهُ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (71:9) [listed for 88:13] ثُمَّ إِنِّىٓ أَعْلَنتُ لَهُمْ وَأَسْرَرْتُ لَهُمْ إِسْرَارًۭا
- (86:9) [listed for 88:13] [cited in ¶8] يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
- (94:2) [listed for 88:13] وَوَضَعْنَا عَنكَ وِزْرَكَ
- (94:3) [listed for 88:13] ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- (94:5) [listed for 88:13] فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- (94:6) [listed for 88:13] إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- (94:7) [listed for 88:13] فَإِذَا فَرَغْتَ فَٱنصَبْ

## named by the passage's own list as weak for this ayah (13)

- (7:73) [listed for 88:13] وَإِلَىٰ ثَمُودَ أَخَاهُمْ صَٰلِحًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابٌ أَلِيمٌۭ
- (18:3) [listed for 88:13] مَّٰكِثِينَ فِيهِ أَبَدًۭا
- (20:119) [listed for 88:13] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (37:49) [listed for 88:13] كَأَنَّهُنَّ بَيْضٌۭ مَّكْنُونٌۭ
- (44:53) [listed for 88:13] يَلْبَسُونَ مِن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَقَٰبِلِينَ
- (50:35) [listed for 88:13] لَهُم مَّا يَشَآءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌۭ
- (55:68) [listed for 88:13] فِيهِمَا فَٰكِهَةٌۭ وَنَخْلٌۭ وَرُمَّانٌۭ
- (56:18) [listed for 88:13] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:28) [listed for 88:13] فِى سِدْرٍۢ مَّخْضُودٍۢ
- (56:30) [listed for 88:13] وَظِلٍّۢ مَّمْدُودٍۢ
- (76:14) [listed for 88:13] وَدَانِيَةً عَلَيْهِمْ ظِلَٰلُهَا وَذُلِّلَتْ قُطُوفُهَا تَذْلِيلًۭا
- (76:18) [listed for 88:13] عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا
- (78:23) [listed for 88:13] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا

## neighbours: within two ayat of a passage the commentary cites (59)

- (7:41) [next to 7:43] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (7:42) [next to 7:43] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (7:44) [next to 7:43] وَنَادَىٰٓ أَصْحَٰبُ ٱلْجَنَّةِ أَصْحَٰبَ ٱلنَّارِ أَن قَدْ وَجَدْنَا مَا وَعَدَنَا رَبُّنَا حَقًّۭا فَهَلْ وَجَدتُّم مَّا وَعَدَ رَبُّكُمْ حَقًّۭا ۖ قَالُوا۟ نَعَمْ ۚ فَأَذَّنَ مُؤَذِّنٌۢ بَيْنَهُمْ أَن لَّعْنَةُ ٱللَّهِ عَلَى ٱلظَّٰلِمِينَ
- (7:45) [next to 7:43] ٱلَّذِينَ يَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًۭا وَهُم بِٱلْءَاخِرَةِ كَٰفِرُونَ
- (12:82) [next to 12:84] وَسْـَٔلِ ٱلْقَرْيَةَ ٱلَّتِى كُنَّا فِيهَا وَٱلْعِيرَ ٱلَّتِىٓ أَقْبَلْنَا فِيهَا ۖ وَإِنَّا لَصَٰدِقُونَ
- (12:83) [next to 12:84] قَالَ بَلْ سَوَّلَتْ لَكُمْ أَنفُسُكُمْ أَمْرًۭا ۖ فَصَبْرٌۭ جَمِيلٌ ۖ عَسَى ٱللَّهُ أَن يَأْتِيَنِى بِهِمْ جَمِيعًا ۚ إِنَّهُۥ هُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ
- (12:85) [next to 12:84] قَالُوا۟ تَٱللَّهِ تَفْتَؤُا۟ تَذْكُرُ يُوسُفَ حَتَّىٰ تَكُونَ حَرَضًا أَوْ تَكُونَ مِنَ ٱلْهَٰلِكِينَ
- (12:86) [next to 12:84] قَالَ إِنَّمَآ أَشْكُوا۟ بَثِّى وَحُزْنِىٓ إِلَى ٱللَّهِ وَأَعْلَمُ مِنَ ٱللَّهِ مَا لَا تَعْلَمُونَ
- (12:97) [next to 12:99] قَالُوا۟ يَٰٓأَبَانَا ٱسْتَغْفِرْ لَنَا ذُنُوبَنَآ إِنَّا كُنَّا خَٰطِـِٔينَ
- (12:98) [next to 12:99] قَالَ سَوْفَ أَسْتَغْفِرُ لَكُمْ رَبِّىٓ ۖ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (12:101) [next to 12:99] ۞ رَبِّ قَدْ ءَاتَيْتَنِى مِنَ ٱلْمُلْكِ وَعَلَّمْتَنِى مِن تَأْوِيلِ ٱلْأَحَادِيثِ ۚ فَاطِرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ أَنتَ وَلِىِّۦ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ تَوَفَّنِى مُسْلِمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (12:102) [next to 12:100] ذَٰلِكَ مِنْ أَنۢبَآءِ ٱلْغَيْبِ نُوحِيهِ إِلَيْكَ ۖ وَمَا كُنتَ لَدَيْهِمْ إِذْ أَجْمَعُوٓا۟ أَمْرَهُمْ وَهُمْ يَمْكُرُونَ
- (15:43) [next to 15:45] وَإِنَّ جَهَنَّمَ لَمَوْعِدُهُمْ أَجْمَعِينَ
- (15:44) [next to 15:45] لَهَا سَبْعَةُ أَبْوَٰبٍۢ لِّكُلِّ بَابٍۢ مِّنْهُمْ جُزْءٌۭ مَّقْسُومٌ
- (15:49) [next to 15:47] ۞ نَبِّئْ عِبَادِىٓ أَنِّىٓ أَنَا ٱلْغَفُورُ ٱلرَّحِيمُ
- (15:50) [next to 15:48] وَأَنَّ عَذَابِى هُوَ ٱلْعَذَابُ ٱلْأَلِيمُ
- (35:31) [next to 35:33] وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ مِنَ ٱلْكِتَٰبِ هُوَ ٱلْحَقُّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ ۗ إِنَّ ٱللَّهَ بِعِبَادِهِۦ لَخَبِيرٌۢ بَصِيرٌۭ
- (35:32) [next to 35:33] ثُمَّ أَوْرَثْنَا ٱلْكِتَٰبَ ٱلَّذِينَ ٱصْطَفَيْنَا مِنْ عِبَادِنَا ۖ فَمِنْهُمْ ظَالِمٌۭ لِّنَفْسِهِۦ وَمِنْهُم مُّقْتَصِدٌۭ وَمِنْهُمْ سَابِقٌۢ بِٱلْخَيْرَٰتِ بِإِذْنِ ٱللَّهِ ۚ ذَٰلِكَ هُوَ ٱلْفَضْلُ ٱلْكَبِيرُ
- (35:36) [next to 35:34] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (35:37) [next to 35:35] وَهُمْ يَصْطَرِخُونَ فِيهَا رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ ۖ فَذُوقُوا۟ فَمَا لِلظَّٰلِمِينَ مِن نَّصِيرٍ
- (37:40) [next to 37:42] إِلَّا عِبَادَ ٱللَّهِ ٱلْمُخْلَصِينَ
- (37:41) [next to 37:42] أُو۟لَٰٓئِكَ لَهُمْ رِزْقٌۭ مَّعْلُومٌۭ
- (37:45) [next to 37:43] يُطَافُ عَلَيْهِم بِكَأْسٍۢ مِّن مَّعِينٍۭ
- (43:31) [next to 43:33] وَقَالُوا۟ لَوْلَا نُزِّلَ هَٰذَا ٱلْقُرْءَانُ عَلَىٰ رَجُلٍۢ مِّنَ ٱلْقَرْيَتَيْنِ عَظِيمٍ
- (43:36) [next to 43:34] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (43:37) [next to 43:35] وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
- (56:1) [next to 56:3] إِذَا وَقَعَتِ ٱلْوَاقِعَةُ
- (56:2) [next to 56:3] لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ
- (56:4) [next to 56:3] إِذَا رُجَّتِ ٱلْأَرْضُ رَجًّۭا
- (56:5) [next to 56:3] وَبُسَّتِ ٱلْجِبَالُ بَسًّۭا
- (56:9) [next to 56:11] وَأَصْحَٰبُ ٱلْمَشْـَٔمَةِ مَآ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- (56:10) [next to 56:11] وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ
- (56:13) [next to 56:11] ثُلَّةٌۭ مِّنَ ٱلْأَوَّلِينَ
- (56:14) [next to 56:12] وَقَلِيلٌۭ مِّنَ ٱلْءَاخِرِينَ
- (56:17) [next to 56:16] يَطُوفُ عَلَيْهِمْ وِلْدَٰنٌۭ مُّخَلَّدُونَ
- (56:32) [next to 56:34] وَفَٰكِهَةٍۢ كَثِيرَةٍۢ
- (56:33) [next to 56:34] لَّا مَقْطُوعَةٍۢ وَلَا مَمْنُوعَةٍۢ
- (56:35) [next to 56:34] إِنَّآ أَنشَأْنَٰهُنَّ إِنشَآءًۭ
- (56:36) [next to 56:34] فَجَعَلْنَٰهُنَّ أَبْكَارًا
- (69:17) [next to 69:19] وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا ۚ وَيَحْمِلُ عَرْشَ رَبِّكَ فَوْقَهُمْ يَوْمَئِذٍۢ ثَمَٰنِيَةٌۭ
- (69:18) [next to 69:19] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (69:20) [next to 69:19] إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ
- (69:25) [next to 69:23] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ فَيَقُولُ يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ
- (69:26) [next to 69:24] وَلَمْ أَدْرِ مَا حِسَابِيَهْ
- (76:8) [next to 76:10] وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا
- (76:9) [next to 76:10] إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا
- (76:12) [next to 76:10] وَجَزَىٰهُم بِمَا صَبَرُوا۟ جَنَّةًۭ وَحَرِيرًۭا
- (76:15) [next to 76:13] وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠
- (84:6) [next to 84:8] يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ
- (84:7) [next to 84:8] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ
- (84:10) [next to 84:8] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
- (84:11) [next to 84:9] فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
- (84:12) [next to 84:13] وَيَصْلَىٰ سَعِيرًا
- (84:14) [next to 84:13] إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ
- (84:15) [next to 84:13] بَلَىٰٓ إِنَّ رَبَّهُۥ كَانَ بِهِۦ بَصِيرًۭا
- (86:6) [next to 86:8] خُلِقَ مِن مَّآءٍۢ دَافِقٍۢ
- (86:7) [next to 86:8] يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ
- (86:11) [next to 86:9] وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ
- (86:12) [next to 86:10] وَٱلْأَرْضِ ذَاتِ ٱلصَّدْعِ

