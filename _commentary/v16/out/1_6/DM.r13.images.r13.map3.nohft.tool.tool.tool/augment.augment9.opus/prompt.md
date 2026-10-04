Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:6; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_6.reading.tr.md (prose paragraphs numbered) =====
## İsteğin adı konuyor

[¶1] Beşinci ayet iki şey söyler: kulluk yalnız Allah'adır, yardım da yalnız O'ndan istenir. Yardım isteği ayette nesnesiz kalır: {ar:وَإِيَّاكَ نَسْتَعِينُ, tr:ve iyyâke nesteîn, gloss:ve yalnız senden yardım dileriz, source:1:5}. Ne tür bir yardım istendiğini altıncı ayet hemen söyler: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-müstakîm, gloss:bizi dosdoğru yola ilet, source:1:6}. Konuşan "biz" değişmez. "Na'büdü" ve "nesteînü" fiillerinde konuşan topluluk, "ihdinâ" kelimesinin sonundaki "-nâ"da da "bizi" diye yine kendini anar. Fiil emir kipindedir, fakat aşağıdan yukarıya söylenen bir emir yalvarıştır. İkinci ayetten dördüncü ayete kadar Allah'tan "O" diye söz edilmişti. Beşinci ayette O'na "sen" diye dönülmüştü. Bu ayette de O'ndan doğrudan bir şey istenir.

[¶2] Fiilin yapısında küçük ama önemli bir ayrıntı var. "İhdi" iki nesne alır, "bizi" ve "yolu", ve araya "-e doğru" anlamında bir edat girmez. Araplar da yol gösterdiklerini aynı biçimde söylerlerdi: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytühü't-tarîka ve'l-beyte hidâyeten, ey arraftühû, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}. Kur'an aynı fiili başka yerlerde "-e doğru" anlamındaki edatla da kullanır: {ar:قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:kul innenî hedânî rabbî ilâ sırâtın müstakîm, gloss:de ki: Rabbim beni dosdoğru bir yola iletti, source:6:161}. Fâtiha'da ise yol fiilin doğrudan nesnesidir. Böylece yol uzaktan gösterilen bir hedef olmaktan çok, tanıtılan ve üzerinde yürütülen bir yer olarak durur.

[¶3] İsteyenlerin kim olduğu da ayeti anlamaya yardım eder. Bunu "yalnız sana kulluk ederiz" diyenler söyler, yani yolda olduklarını zaten beyan etmiş olanlar. Kur'an'da bu çelişki gibi görünmez. Allah Peygamber'e {ar:فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ, tr:festemsik billezî ûhiye ileyk, gloss:sana vahyedilene sımsıkı tutun, source:43:43} der ve ardından ekler: {ar:إِنَّكَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:inneke alâ sırâtın müstakîm, gloss:sen dosdoğru bir yol üzerindesin, source:43:43}. Fetih suresinin açılışında ise "sana apaçık bir açılış verdik" dedikten sonra, yolda olduğunu söylediği aynı kişi için yine bu yolu vaat eder: {ar:وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve yütimme ni'metehû aleyke ve yehdiyeke sırâtan müstakîmâ, gloss:sana olan nimetini tamamlasın ve seni dosdoğru bir yola iletsin diye, source:48:2}. Saffât suresinde Musa ile Harun'a yapılan iyilikler sayılır. Onlara açıklayıcı kitabın verildiği söylenir, sonra Fâtiha'nın kelimeleri aynı yapıyla, edatsız olarak gelir: {ar:وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ve hedeynâhüme's-sırâta'l-müstakîm, gloss:ve ikisini dosdoğru yola ilettik, source:37:118}. Meryem suresinde de Allah yolu bulanlar için şöyle der: {ar:وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى, tr:ve yezîdullâhü'llezîne'hteday hüdâ, gloss:Allah yolu bulmuş olanların hidayetini artırır, source:19:76}. Demek ki hidayet bir kez ulaşılıp geride bırakılan bir eşik değildir. Her adımda yeniden istenir.

[¶4] Türkçede "hidayet" kelimesi daralmıştır. "Hidayete ermek" denince insanın bir gün imana ya da dindarlığa geçmesi, yani bir kez yaşanan bir dönüş anlaşılır. Arapçada ise kelime yolda kalır. Bir yabancıya yolu ve evi tarif etmek de hidayettir, onu adım adım götürmek de. Fâtiha'yı her gün okuyan kişi bu yüzden bir kez dönmeyi değil, her gün yeniden yola konmayı ister.

## Önden giden

[¶5] "İhdinâ" kelimesinin ailesinde birkaç somut görüntü var. Bunlar kelimenin bu ayetteki anlamının, yani "yolu göster, ilet" anlamının yerine geçmez, onun yanında duyulur. Birincisi önde olandır. Araplar atların boynuna ve öndeki ilk bölüğe "hevâdî" derlerdi: {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelü ra'îl, gloss:atların hâdîleri boyunlarıdır ya da ilk süvari bölüğüdür, source:"ه د ي,B003"}. At koşarken boyun gövdenin önünden gider ve baş nereye dönerse beden de oraya gider. Yaban hayvanı sürülerinde de başa geçip ötekilere yolu açanlar bu adla anılırdı: {ar:هوادي الوحش متقدماتها الهادية لغيرها, tr:hevâdi'l-vahşi mütekaddimâtühe'l-hâdiyetü li-gayrihâ, gloss:yaban hayvanlarının hâdîleri, önden gidip ötekilere yol gösterenlerdir, source:"ه د ي,B003"}. Okun demir ucuna da {ar:هادي السهم نصله, tr:hâdi's-sehmi naslüh, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"} denirdi. Asa da bu adı alırdı: {ar:الهادية العصا لأنها تتقدم ممسكها, tr:el-hâdiyetü'l-asâ li-ennehâ tetekaddemü mümsikehâ, gloss:asaya hâdiye denir, çünkü onu tutanın önünden gider, source:"ه د ي,B003"}. Asa yürüyenin bir adım önünde yere değer, zemini ondan önce yoklar. Yol bilen kılavuz da aynı sebeple bu adı taşırdı: {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlü yüsemmâ hâdiyen li-tekaddümih, gloss:kılavuza önde gittiği için hâdî denir, source:"ه د ي,B003"}. Bu görüntü "bizi ilet" isteğinin yanında şunu da duyurur: Önümüzden git. Burada istenen eline verilip yalnız yürünecek bir harita değildir. Bir öncünün ardından yürümektir.

[¶6] İkinci görüntü yönelmedir. Aynı kökten "hidye" kelimesi bir işin ya da bir kimsenin yönünü ve gidişatını anlatır. Yönü belirsiz bir iş için şöyle denirdi: {ar:ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة, tr:leyse li-hâze'l-emri hidyetün ve lâ kıbletün ve lâ dibretün ve lâ vichetün, gloss:bu işin ne yönü var ne kıblesi, ne arkası ne yüzü, source:"ه د ي,B002"}. Bu sözde "hidye" kelimesi kıble ile yan yana sayılır. Kur'an da bu iki şeyi aynı yerde buluşturur. Bakara suresinde müminlerin namazda yöneldikleri yön değişince bazı kimselerin itiraz edeceği haber verilir: {ar:مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا, tr:mâ vellâhüm an kıbletihimü'lletî kânû aleyhâ, gloss:onları yöneldikleri kıbleden ne çevirdi, source:2:142}. Verilmesi istenen cevap şudur: {ar:قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:kul lillâhi'l-maşriku ve'l-mağrib, yehdî men yeşâü ilâ sırâtın müstakîm, gloss:de ki: doğu da batı da Allah'ındır; O dilediğini dosdoğru bir yola iletir, source:2:142}. Hemen sonraki ayet yön değişikliğinin zor olduğunu söyler: {ar:وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ, tr:ve in kânet le-kebîraten illâ ale'llezîne hedallâh, gloss:bu, Allah'ın yola ilettiklerinden başkasına gerçekten ağır geldi, source:2:143}. Dosdoğru yol burada bir yüzün nereye döndüğü meselesi olarak sahnelenir. Musa da Firavun "Rabbiniz kim?" diye sorduğunda O'nu böyle tanıtır: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını veren, sonra da onu yönlendirendir, source:20:50}. Önce yaratılış verilir, sonra bir yön.

[¶7] Aynı kelime bir kimsenin tuttuğu gidişi de adlandırır. Birinin yolundan gidene {ar:هدى هدي فلان أي سار سيرته, tr:hedâ hedye fülânin, ey sâra sîratehû, gloss:falancanın gidişini tuttu, yani onun yolundan yürüdü, source:"ه د ي,B002"} denirdi. Tuttuğu işten sapmasın diye birine de {ar:خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه, tr:huz fî hidyetik, gloss:tuttuğun yolda devam et, ondan ayrılma, source:"ه د ي,B002"} denirdi. Kur'an bu gidişin önden yürüyenlerini adlarıyla sayar. En'âm suresinde İbrahim'den başlayarak bir peygamberler zinciri anılır ve onlar için {ar:وَهَدَيْنَٰهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:ve hedeynâhüm ilâ sırâtın müstakîm, gloss:onları dosdoğru bir yola ilettik, source:6:87} denir. Sonra Peygamber'e şöyle seslenilir: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ, tr:ülâike'llezîne hedallâh, fe-bi-hüdâhümü'ktedih, gloss:Allah'ın yola ilettikleri işte onlardır; sen de onların gidişine uy, source:6:90}. Yedinci ayet aynı şeyi yolun sahiplerini anarak söyler: {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:sırâta'llezîne en'amte aleyhim, gloss:kendilerine nimet verdiklerinin yolu, source:1:7}.

[¶8] Aynı ailede önde gidenin karşısında duran bir görüntü daha vardır. Araplar güçsüzlükten tek başına yürüyemeyen birini şöyle anlatırlardı: {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yühâdâ beyne's-neyn, gloss:güçsüzlüğünden ve sendelemesinden ötürü iki kişinin arasında onlara dayanarak yürür, source:"ه د ي,B008"}. Bu sendeleme de ayrıca tarif edilirdi: {ar:التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال, tr:et-tehâdî meşyün fî temâyülin yemînen ve şimâlâ, gloss:sağa sola salınarak yürümek, kadınların ve yüklü develerin yürüyüşü gibi, source:"ه د ي,B008"}. Demek ki bu kök hem önden giden kılavuzu hem de iki yanından tutulması gereken yolcuyu adlandırır. "İhdinâ" diyen, bir an önce "yardım dileriz" demiş kişidir. Kendini ikinci yerde, sağa sola yalpalayan ve dayanacak omuz arayan yolcunun yerinde görür. Önüne bir öncü, yanına bir dayanak ister. Bu yürüyüşün varacağı hal de aynı kökle anlatılırdı: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yüsri' isrâ'a'l-münhezim, velâkin alâ sükûnin ve hedyin hasen, gloss:bozguna uğramış biri gibi koşmadı, sakin ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. "Hedy" kelimesi burada yürüyüşün kendisini adlandırır. Yola iletilen kişi önce dayanarak, sonunda telaşsız adımlarla yürür.

## Yolcuyu içine alan yol

[¶9] Türkçede "sırat" denince çoğu insanın aklına ahirette geçilecek ince bir köprü gelir. Kelime Türkçede neredeyse yalnız bu köprünün adı olarak yaşar. Kur'an'ın kelimesi ise bir yoldur ve çoğunlukla bu dünyada yürünen bir yoldur. Araplar yolun kendisine bu adı verirlerdi: {ar:الصراط والسراط والزراط: الطريق, tr:es-sırâtu ve's-sirâtu ve'z-zırât: et-tarîk, gloss:sırat, sirat ve zırat yol demektir, source:"ص ر ط,B001"}. Kelimenin bir tanımı Fâtiha'nın sıfatını zaten içinde taşır: {ar:الصراط: الطريق المستقيم, tr:es-sırât: et-tarîku'l-müstakîm, gloss:sırat dosdoğru yoldur, source:"ص ر ط,B001"}. Buna göre "es-sırâtu'l-müstakîm" doğruluğu iki kez söyler. İsim düzlüğü zaten içinde taşır, sıfat onu bir de açıkça söyler.

[¶10] Kelimenin "s" ile söylenişi başka bir fiille aynı harfleri paylaşır. Yemeği yutmak için {ar:سرطت الطعام إذا بلعته لأنه إذا سرط غاب, tr:seratü't-taâme izâ bele'tüh, li-ennehû izâ süreta gâb, gloss:yemeği yuttum; yutulan lokma gözden kaybolur, source:"ص ر ط,B002"} denirdi. Bu harflerin taşıdığı anlam şöyle özetlenirdi: {ar:أصل صحيح واحد يدل على غيبة في مر وذهاب, tr:aslun sahîhun vâhidün yedüllü alâ gaybetin fî merrin ve zehâb, gloss:geçip giderken gözden kaybolmayı anlatan tek bir kök, source:"ص ر ط,B002"}. Kimileri yolun adını da buna bağlardı: {ar:بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب, tr:ba'du ehli'l-ilmi yekûlü's-sirâtu müştakkun min zâlik, li-enne'z-zâhibe fîhi yegîb, gloss:bazı bilginler, yolda giden gözden kaybolduğu için siratın buradan türediğini söyler, source:"ص ر ط,B001"}. Lokma boğazdan geçer ve görünmez olur, ama yok olmaz. Bedeni besleyeceği yere varır. Yol da içine gireni yutar. Yolcu uğurlayanın gözünden çıkar, ama yol onu taşımaya devam eder. Aynı harflerle keskin kılıca da ad verilirdi: {ar:والسراط السيف القاطع الماضي في الضريبة, tr:ve's-sirâtu's-seyfü'l-kâti'u'l-mâdî fi'd-darîbe, gloss:sirat, vuruşta kesip içinden geçen kılıçtır, source:"ص ر ط,B003"}. Lokmada da kılıçta da yolda da ortak olan, bir yerden geçip öteye varmaktır. Bu görüntülerin yanında okununca istenen sırat, üzerinde durulacak bir yer olmaktan çok, insanı içine alıp bir yere geçiren bir geçittir. Yedinci ayetin son kelimesi de bir gözden kayboluşu adlandırır: {ar:وَلَا ٱلضَّآلِّينَ, tr:ve le'd-dâllîn, gloss:yolunu yitirenlerin de değil, source:1:7}. Ama o, varılacak yeri olmayan bir kayboluştur.

[¶11] Bu yol tektir. En'âm suresinde Allah'ın öğütleri sıralanır ve sonunda şu söylenir: {ar:وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ, tr:ve enne hâzâ sırâtî müstakîmen fettebi'ûh, gloss:işte bu benim dosdoğru yolumdur, ona uyun, source:6:153}. Ardından bir uyarı gelir: {ar:وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve lâ tettebi'u's-sübüle fe-teferraka biküm an sebîlih, gloss:başka yollara uymayın, sizi O'nun yolundan ayırıp dağıtır, source:6:153}. Tek bir sırat birçok yolun karşısına konur. Fâtiha'daki belirlilik takısı da "bir yol" değil, "o yol" der.

[¶12] Yine de ne fiil ne isim kendi başına iyiliği garanti eder. Saffât suresinde ahiret sahnesi anlatılırken şöyle bir emir verilir: {ar:ٱحْشُرُوا۟ ٱلَّذِينَ ظَلَمُوا۟ وَأَزْوَٰجَهُمْ, tr:uhşüru'llezîne zalemû ve ezvâcehüm, gloss:zulmedenleri ve eşlerini toplayın, source:37:22}. Sonra da {ar:فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ, tr:fehdûhüm ilâ sırâti'l-cahîm, gloss:onları cehennemin yoluna götürün, source:37:23} denir. Fiil de isim de Fâtiha'dakinin aynısıdır. Yalnız yolun sonu başkadır. Yolu iyi kılan şey "dosdoğru" sıfatıdır ve yedinci ayetin söylediği gibi kimlerin yolu olduğudur.

## Dikilmek ve yürümeyi sürdürmek

[¶13] "Müstakîm" kelimesi "kâme" fiilinden gelir. Bu fiil ayağa kalkmak, dikilmek demektir: {ar:قام الرجل قياما, tr:kâme'r-racülü kıyâmen, gloss:adam ayağa kalktı, source:"ق و م,B002"}. "İstekâme" ise bu dikilmenin bir hale gelmesi ve öyle sürmesidir. Bu doğruluğun somut örneği mızraktır: {ar:رمح قويم, tr:rumhun kavîm, gloss:dümdüz mızrak, source:"ق و م,B008"}. Sapı eğri bir mızrak, ucunu hedefe değil yana götürür. Yolda da istikamet şöyle tarif edilirdi: {ar:الاستقامة في الطريق الذي يكون على خط مستو, tr:el-istikâmetü fi't-tarîki'llezî yekûnü alâ hattın müstevin, gloss:istikamet, düz bir hat üzerinde uzanan yolda olur, source:"ق و م,B008"}. İnsanda ise {ar:استقامة الإنسان لزومه المنهج المستقيم, tr:istikâmetü'l-insâni lüzûmühü'l-menhece'l-müstakîm, gloss:insanın istikameti dosdoğru yoldan ayrılmamasıdır, source:"ق و م,B008"} denirdi.

[¶14] Bu kökte bir ayrım çok önemlidir. "Kâme" fiili durup kalmayı da anlatır. Yorulup yürüyemeyen hayvan için {ar:قامت لفلان دابته إذا كلت أو عيت فلم تسر, tr:kâmet li-fülânin dâbbetüh, gloss:falancanın bineği yorulup tükendi ve yürümez oldu, source:"ق و م,B016"} denirdi. Donan su için de aynı fiil kullanılırdı: {ar:قام الماء جمد, tr:kâme'l-mâü cemed, gloss:su dondu, source:"ق و م,B016"}. Dimdik durmanın bir de böyle ölü bir hali vardır: hareket etmeyen hayvan, akmayan su. İstikamet ise bunun tersidir. Onun tarifi bir sürüşü anlatır: {ar:إذا انقاد واستمرت طريقته فقد استقام, tr:izen'kâde vestemerrat tarîkatühû fe-kad istekâm, gloss:boyun eğip gidişi sürüp gittiğinde doğrulmuş olur, source:"ق و م,B008"}. Burada istenen dik duruş yürüyerek sürdürülen bir dik duruştur. Türkçede "istikamet" çoğu zaman yalnız "yön" demektir, "müstakim" de "dürüst" demektir. Arapça kelime ise hâlâ bedenin dikilmesini ve yolun eğilmeden sürmesini içinde taşır.

[¶15] Aynı kök bir aletin dik duran ve yükü taşıyan parçasına da ad verirdi. Kılıcın tutulan yeri {ar:قائم السيف مقبضه, tr:kâimü's-seyfi mikbazuh, gloss:kılıcın kâimi kabzasıdır, source:"ق و م,B012"} diye anılırdı. Kuyudan su çeken makaraya da bu kökten bir ad verilirdi: {ar:القامة البكرة بأداتها, tr:el-kâmetü'l-bekretü bi-edâtihâ, gloss:kâme, donanımıyla birlikte makaradır, source:"ق و م,B012"}. Genel ilke de şöyle söylenirdi: {ar:قوام كل شيء ما استقام به, tr:kıvâmü kulli şey'in mâ'stekâme bih, gloss:her şeyin kıvâmı, onunla doğrulup ayakta durduğu şeydir, source:"ق و م,B009"}. Kur'an istikamet ile suyu bir arada anar. Cin suresinde Peygamber'e kendisine vahyedildiğini söylemesi emredilen şeyler arasında şu da vardır: {ar:وَأَلَّوِ ٱسْتَقَٰمُوا۟ عَلَى ٱلطَّرِيقَةِ لَأَسْقَيْنَٰهُم مَّآءً غَدَقًۭا, tr:ve ellevi'stekâmû ale't-tarîkati le-eskaynâhüm mâen gadakâ, gloss:yol üzerinde dosdoğru dursalardı onlara bol su içirirdik, source:72:16}. Yolda dik durana su verilir. Makaranın kuyudan su çektiği gibi, dik duruş da hayatı ayakta tutan şeyi taşır.

[¶16] Kur'an istikameti bir sözden sonra gelen bir hal olarak anlatır: {ar:إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟, tr:innellezîne kâlû rabbünallâhü sümme'stekâmû, gloss:"Rabbimiz Allah'tır" deyip sonra dosdoğru duranlar, source:41:30}. Bu ayetin devamında böylelerine meleklerin inip korkmamalarını söylediği anlatılır. Fâtiha'da da sıra aynıdır. Önce "yalnız sana kulluk ederiz" denir, sonra o sözde dik durabilmek için yol istenir. Peygamber'e de aynı emir verilir: {ar:فَٱسْتَقِمْ كَمَآ أُمِرْتَ وَمَن تَابَ مَعَكَ وَلَا تَطْغَوْا۟, tr:festekım kemâ ümirte ve men tâbe meake ve lâ tatgav, gloss:emrolunduğun gibi dosdoğru ol, seninle birlikte tövbe edenler de; taşkınlık etmeyin, source:11:112}. Taşmak, istikametin tersi olarak hemen yanında anılır.

[¶17] Dik beden ile düz yol Mülk suresinde tek bir soruda buluşur. Allah sorar: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe men yemşî mükibben alâ vechihî ehdâ em men yemşî seviyyen alâ sırâtın müstakîm, gloss:yüzüstü kapanarak yürüyen mi yolu daha iyi bulur, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Fâtiha'nın üç kelimesinin üçü de bu ayette vardır: "ehdâ", "sırât" ve "müstakîm". Yola iletilen kişi yüzükoyun değil, dik yürür. Bu yolun pusu kurulan bir yol olduğunu da Kur'an söyler. İblis secdeden kaçınıp kovulduktan sonra mühlet ister ve şöyle yemin eder: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ak'udenne lehüm sırâtake'l-müstakîm, gloss:senin dosdoğru yolunun üzerinde onları gözetleyip oturacağım, source:7:16}. Pusu kurulacak yer, Fâtiha'da istenen yolun ta kendisidir. Bu yüzden yolu bir kez bulmak yetmez. O yol her gün yeniden istenir.

## Terazinin dengesi

[¶18] "Kâme" kökü teraziye de girer. Ağırlığı tam olan altın para için {ar:دينار قائم إذا كان مثقالا سواء لا يرجح, tr:dînârun kâimün izâ kâne miskâlen sevâen lâ yerceh, gloss:kâim dinar, ağırlığı tam bir miskal olan ve ağır basmayan dinardır, source:"ق و م,B015"} derlerdi. Sikke bir kefeye, ölçü ağırlığı öbür kefeye konur. Sikke "kâim" ise kefeler aynı hizada kalır ve terazinin dili ne sağa ne sola eğilir. Gündüzün ortası da aynı dille anlatılırdı: {ar:قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل, tr:kâme kâimü'z-zahîre izâ kâmeti'ş-şemsü ve kâde'z-zıllü ya'kıl, gloss:öğle dikildi, yani güneş tepede durdu ve gölge neredeyse yerinden kıpırdamaz oldu, source:"ق و م,B017"}. Öğle vakti için {ar:قام ميزان النهار فاعتدل, tr:kâme mîzânü'n-nehâri fa'tedel, gloss:gündüzün terazisi dikilip dengeye geldi, source:"ق و م,B017"} de denirdi. Güneş tepedeyken gölge hiçbir yana düşmez. Bu kökte dik durmak, iki yandan hiçbirine eğilmemek demektir. Kökün en genel tanımlarından biri de budur: {ar:الاستقامة الاعتدال, tr:el-istikâmetü'l-i'tidâl, gloss:istikamet dengedir, source:"ق و م,B008"}.

[¶19] Kur'an aynı sıfatı teraziye verir. İsrâ suresinde Rabbin buyruklarının sıralandığı bölümde şöyle denir: {ar:وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:ve zinû bi'l-kıstâsi'l-müstakîm, gloss:dosdoğru teraziyle tartın, source:17:35}. Şuayb da Eyke halkına aynı sözü söyler {source:26:182}. Kur'an'da "müstakîm" yalnız düz bir çizgiyi değil, eğilmeyen bir teraziyi de niteler. Yedinci ayet istenen yolun iki yanını da adlandırır: {ar:غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:gayri'l-magdûbi aleyhim, gloss:gazaba uğrayanların değil, source:1:7} ve yolunu yitirenler. Bu ayetin yanında okununca yolun dosdoğru oluşu, terazinin dilini bu iki yandan hiçbirine eğdirmemek gibi de duyulur.

[¶20] Kök, yolun ardından gelen dine de ad verir. Peygamber'e dosdoğru yola iletildiğini söylemesi emredilen ayette yolun hemen arkasından bir sıfat gelir: {ar:دِينًۭا قِيَمًۭا, tr:dînen kıyemen, gloss:dimdik duran bir din, source:6:161}. Araplar da {ar:القيمة الملة المستقيمة, tr:el-kayyimetü'l-milletü'l-müstakîme, gloss:kayyime, dosdoğru olan dindir, source:"ق و م,B008"} derlerdi. İsrâ suresi de hidayeti ve bu kökü tek cümlede birleştirir: {ar:إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ, tr:inne hâze'l-kur'âne yehdî li'lletî hiye akvem, gloss:bu Kur'an en dik duran, en doğru olana iletir, source:17:9}. Fâtiha'da istenen şey, Kur'an'ın kendisinin de götürdüğünü söylediği yerdir.

## Yolun ucundaki ev

[¶21] Hidayetin tarifinde iki şey birden geçer: {ar:هديته الطريق والبيت, tr:hedeytühü't-tarîka ve'l-beyt, gloss:ona yolu ve evi gösterdim, source:"ه د ي,B001"}. Yol bir eve çıkar. Bu kökün başka kullanımları hep bir şeyi ait olduğu ve kabul göreceği yere götürmeyi anlatır. Kutsal bölgeye sürülen hayvan için {ar:الهدي ما يهدى إلى الحرم من النعم, tr:el-hedyü mâ yühdâ ile'l-harami mine'n-neam, gloss:hedy, Harem'e götürülen hayvandır, source:"ه د ي,B005"} denirdi. Kur'an hac hükümlerinde bu hayvanın yolculuğunu varışıyla birlikte anar: {ar:حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ, tr:hattâ yebluga'l-hedyü mahilleh, gloss:kurbanlık yerine varıncaya kadar, source:2:196}. Başka bir yerde de {ar:هَدْيًۢا بَٰلِغَ ٱلْكَعْبَةِ, tr:hedyen bâliga'l-Ka'be, gloss:Kâbe'ye ulaşacak bir kurbanlık olarak, source:5:95} der. Gelin için {ar:هديت العروس إلى زوجها, tr:hedeytü'l-arûse ilâ zevcihâ, gloss:gelini kocasının evine götürdüm, source:"ه د ي,B006"} denirdi. Bir topluluğa sığınıp onların korumasına giren kişiye de aynı kökten ad verilirdi: {ar:الرجل الذي له حرمة كحرمة هدي البيت, tr:er-racülüllezî lehû hurmetün ke-hurmeti hedyi'l-beyt, gloss:Beyt'e götürülen kurbanlık kadar dokunulmaz olan kişi, source:"ه د ي,B007"}. Kurbanlık mahalline, gelin kocasının evine, sığınan da korunduğu yere varır. Bu görüntüler "bizi ilet" isteğinin yanında şunu duyurur: Bizi yolun sonunda bizi kabul edecek bir yere ulaştır. Kur'an bu varış yerinin adını da verir. Allah'a inanıp O'na sarılanlar için şöyle der: {ar:وَيَهْدِيهِمْ إِلَيْهِ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve yehdîhim ileyhi sırâtan müstakîmâ, gloss:ve onları kendisine dosdoğru bir yolla iletir, source:4:175}. Yol, istenene çıkar.

[¶22] Aynı kökte bir de armağan vardır: {ar:الهدية ما أهديت إلى ذي مودة من بر, tr:el-hediyyetü mâ ehdeyte ilâ zî meveddetin min birr, gloss:hediye, sevdiğin birine gönderdiğin iyiliktir, source:"ه د ي,B004"}. Armağanın inceliği ayrıca vurgulanırdı: {ar:الهدية مختصة باللطف, tr:el-hediyyetü muhtassatün bi'l-lutf, gloss:hediye inceliğe özgüdür, source:"ه د ي,B004"}. Yol gösterme de aynı incelikle tarif edilirdi: {ar:الهداية دلالة بلطف, tr:el-hidâyetü delâletün bi-lutf, gloss:hidayet incelikle yol göstermektir, source:"ه د ي,B001"}. Hediye borç ödenir gibi verilmez, sevgiyle gönderilir. Fâtiha'yı okuyan da yolu bir ücret olarak değil, bir armağan olarak ister. Bunu "Rahman, Rahîm" diye andığı birinden ister. Yedinci ayet de yolun sahiplerini nimet verilmiş olanlar diye tanıtır. Fetih suresindeki vaatte nimetin tamamlanması ile dosdoğru yola iletilmenin yan yana durması bu yüzden tesadüf değildir.

===== _commentary/v16/out/1_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: ṣirāṭ never occurs in plural in the Quran
- memory: Turkish "sırat" mostly known as the afterlife bridge
- memory: Turkish "hidayet" narrowed to conversion/becoming pious
- memory: Turkish "istikamet" = direction, "müstakim" = honest
- memory: istafʿala of qāma read as uprightness becoming a lasting state
- not written: ق و م B013 qiyāma day - root link only; fourth ayah's scene belongs to surah commentary
- not written: ق و م B004 qayyim/qayyūm, household keeper - root echo, no work in this ayah's request
- not written: ق و م B001 qawm (kin group) - does not shape the road theme beyond 1:7's "those"
- not written: ق و م B007, B010 substitution/price - the trade scene is the surah commentary's, weak here
- not written: ق و م B011, B014, B018-B021 - no bearing on straightness or road
- not written: ه د ي B009 dull weak man - adds nothing beyond B008
- not written: ه د ي B011 presenting praise/satire poems - no work in the theme
- not written: ه د د echo root - echo, not identity
- not written: well beam/pulley scene with نعامة - belongs to 1:7 and the surah commentary; pulley only used here
- not written: images.md womb/upbringing via قوام أهل بيته - too thin for this ayah
- not written: 2:143 "middle community" - shares no word with the balance theme; would have diluted it

===== passages not cited (234) =====
## strong (this ayah's own list) (46)

- (2:38) [listed for 1:6] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:213) [listed for 1:6] كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ فَبَعَثَ ٱللَّهُ ٱلنَّبِيِّۦنَ مُبَشِّرِينَ وَمُنذِرِينَ وَأَنزَلَ مَعَهُمُ ٱلْكِتَٰبَ بِٱلْحَقِّ لِيَحْكُمَ بَيْنَ ٱلنَّاسِ فِيمَا ٱخْتَلَفُوا۟ فِيهِ ۚ وَمَا ٱخْتَلَفَ فِيهِ إِلَّا ٱلَّذِينَ أُوتُوهُ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ بَغْيًۢا بَيْنَهُمْ ۖ فَهَدَى ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ لِمَا ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
- (3:101) [listed for 1:6] وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ ءَايَٰتُ ٱللَّهِ وَفِيكُمْ رَسُولُهُۥ ۗ وَمَن يَعْتَصِم بِٱللَّهِ فَقَدْ هُدِىَ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (4:68) [listed for 1:6] وَلَهَدَيْنَٰهُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (4:175) [listed for 1:6] [cited in ¶21] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَٱعْتَصَمُوا۟ بِهِۦ فَسَيُدْخِلُهُمْ فِى رَحْمَةٍۢ مِّنْهُ وَفَضْلٍۢ وَيَهْدِيهِمْ إِلَيْهِ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (5:16) [listed for 1:6] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (6:87) [listed for 1:6] [cited in ¶7] وَمِنْ ءَابَآئِهِمْ وَذُرِّيَّٰتِهِمْ وَإِخْوَٰنِهِمْ ۖ وَٱجْتَبَيْنَٰهُمْ وَهَدَيْنَٰهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (6:126) [listed for 1:6] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
- (6:153) [listed for 1:6] [cited in ¶11] وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَتَّقُونَ
- (6:161) [listed for 1:6] [cited in ¶2, ¶20] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (7:16) [listed for 1:6] [cited in ¶17] قَالَ فَبِمَآ أَغْوَيْتَنِى لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ
- (10:25) [listed for 1:6] وَٱللَّهُ يَدْعُوٓا۟ إِلَىٰ دَارِ ٱلسَّلَٰمِ وَيَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (10:35) [listed for 1:6] قُلْ هَلْ مِن شُرَكَآئِكُم مَّن يَهْدِىٓ إِلَى ٱلْحَقِّ ۚ قُلِ ٱللَّهُ يَهْدِى لِلْحَقِّ ۗ أَفَمَن يَهْدِىٓ إِلَى ٱلْحَقِّ أَحَقُّ أَن يُتَّبَعَ أَمَّن لَّا يَهِدِّىٓ إِلَّآ أَن يُهْدَىٰ ۖ فَمَا لَكُمْ كَيْفَ تَحْكُمُونَ
- (11:56) [listed for 1:6] إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (12:108) [listed for 1:6] قُلْ هَٰذِهِۦ سَبِيلِىٓ أَدْعُوٓا۟ إِلَى ٱللَّهِ ۚ عَلَىٰ بَصِيرَةٍ أَنَا۠ وَمَنِ ٱتَّبَعَنِى ۖ وَسُبْحَٰنَ ٱللَّهِ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (13:7) [listed for 1:6] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
- (14:1) [listed for 1:6] الٓر ۚ كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِ رَبِّهِمْ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (14:5) [listed for 1:6] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ أَنْ أَخْرِجْ قَوْمَكَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (15:41) [listed for 1:6] قَالَ هَٰذَا صِرَٰطٌ عَلَىَّ مُسْتَقِيمٌ
- (16:9) [listed for 1:6] وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ ۚ وَلَوْ شَآءَ لَهَدَىٰكُمْ أَجْمَعِينَ
- (16:121) [listed for 1:6] شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (17:9) [listed for 1:6] [cited in ¶20] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
- (19:36) [listed for 1:6] وَإِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (19:43) [listed for 1:6] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (20:123) [listed for 1:6] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
- (21:73) [listed for 1:6] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا وَأَوْحَيْنَآ إِلَيْهِمْ فِعْلَ ٱلْخَيْرَٰتِ وَإِقَامَ ٱلصَّلَوٰةِ وَإِيتَآءَ ٱلزَّكَوٰةِ ۖ وَكَانُوا۟ لَنَا عَٰبِدِينَ
- (22:16) [listed for 1:6] وَكَذَٰلِكَ أَنزَلْنَٰهُ ءَايَٰتٍۭ بَيِّنَٰتٍۢ وَأَنَّ ٱللَّهَ يَهْدِى مَن يُرِيدُ
- (22:24) [listed for 1:6] وَهُدُوٓا۟ إِلَى ٱلطَّيِّبِ مِنَ ٱلْقَوْلِ وَهُدُوٓا۟ إِلَىٰ صِرَٰطِ ٱلْحَمِيدِ
- (23:73) [listed for 1:6] وَإِنَّكَ لَتَدْعُوهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (24:46) [listed for 1:6] لَّقَدْ أَنزَلْنَآ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ ۚ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (27:63) [listed for 1:6] أَمَّن يَهْدِيكُمْ فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ وَمَن يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦٓ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ تَعَٰلَى ٱللَّهُ عَمَّا يُشْرِكُونَ
- (28:22) [listed for 1:6] وَلَمَّا تَوَجَّهَ تِلْقَآءَ مَدْيَنَ قَالَ عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ
- (28:56) [listed for 1:6] إِنَّكَ لَا تَهْدِى مَنْ أَحْبَبْتَ وَلَٰكِنَّ ٱللَّهَ يَهْدِى مَن يَشَآءُ ۚ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (32:24) [listed for 1:6] وَجَعَلْنَا مِنْهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا لَمَّا صَبَرُوا۟ ۖ وَكَانُوا۟ بِـَٔايَٰتِنَا يُوقِنُونَ
- (34:6) [listed for 1:6] وَيَرَى ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (36:61) [listed for 1:6] وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (37:118) [listed for 1:6] [cited in ¶3] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (40:38) [listed for 1:6] وَقَالَ ٱلَّذِىٓ ءَامَنَ يَٰقَوْمِ ٱتَّبِعُونِ أَهْدِكُمْ سَبِيلَ ٱلرَّشَادِ
- (42:52) [listed for 1:6] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ رُوحًۭا مِّنْ أَمْرِنَا ۚ مَا كُنتَ تَدْرِى مَا ٱلْكِتَٰبُ وَلَا ٱلْإِيمَٰنُ وَلَٰكِن جَعَلْنَٰهُ نُورًۭا نَّهْدِى بِهِۦ مَن نَّشَآءُ مِنْ عِبَادِنَا ۚ وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (43:43) [listed for 1:6] [cited in ¶3] فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ ۖ إِنَّكَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (43:64) [listed for 1:6] إِنَّ ٱللَّهَ هُوَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (46:30) [listed for 1:6] قَالُوا۟ يَٰقَوْمَنَآ إِنَّا سَمِعْنَا كِتَٰبًا أُنزِلَ مِنۢ بَعْدِ مُوسَىٰ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ يَهْدِىٓ إِلَى ٱلْحَقِّ وَإِلَىٰ طَرِيقٍۢ مُّسْتَقِيمٍۢ
- (48:2) [listed for 1:6] [cited in ¶3] لِّيَغْفِرَ لَكَ ٱللَّهُ مَا تَقَدَّمَ مِن ذَنۢبِكَ وَمَا تَأَخَّرَ وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (67:22) [listed for 1:6] [cited in ¶17] أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (92:12) [listed for 1:6] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (93:7) [listed for 1:6] وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ

## medium (this ayah's own list) (61)

- (2:120) [listed for 1:6] وَلَن تَرْضَىٰ عَنكَ ٱلْيَهُودُ وَلَا ٱلنَّصَٰرَىٰ حَتَّىٰ تَتَّبِعَ مِلَّتَهُمْ ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۗ وَلَئِنِ ٱتَّبَعْتَ أَهْوَآءَهُم بَعْدَ ٱلَّذِى جَآءَكَ مِنَ ٱلْعِلْمِ ۙ مَا لَكَ مِنَ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
- (2:142) [listed for 1:6] [cited in ¶6] ۞ سَيَقُولُ ٱلسُّفَهَآءُ مِنَ ٱلنَّاسِ مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (2:177) [listed for 1:6] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
- (3:2) [listed for 1:6] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ
- (3:51) [listed for 1:6] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (3:73) [listed for 1:6] وَلَا تُؤْمِنُوٓا۟ إِلَّا لِمَن تَبِعَ دِينَكُمْ قُلْ إِنَّ ٱلْهُدَىٰ هُدَى ٱللَّهِ أَن يُؤْتَىٰٓ أَحَدٌۭ مِّثْلَ مَآ أُوتِيتُمْ أَوْ يُحَآجُّوكُمْ عِندَ رَبِّكُمْ ۗ قُلْ إِنَّ ٱلْفَضْلَ بِيَدِ ٱللَّهِ يُؤْتِيهِ مَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (4:5) [listed for 1:6] وَلَا تُؤْتُوا۟ ٱلسُّفَهَآءَ أَمْوَٰلَكُمُ ٱلَّتِى جَعَلَ ٱللَّهُ لَكُمْ قِيَٰمًۭا وَٱرْزُقُوهُمْ فِيهَا وَٱكْسُوهُمْ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا
- (4:34) [listed for 1:6] ٱلرِّجَالُ قَوَّٰمُونَ عَلَى ٱلنِّسَآءِ بِمَا فَضَّلَ ٱللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍۢ وَبِمَآ أَنفَقُوا۟ مِنْ أَمْوَٰلِهِمْ ۚ فَٱلصَّٰلِحَٰتُ قَٰنِتَٰتٌ حَٰفِظَٰتٌۭ لِّلْغَيْبِ بِمَا حَفِظَ ٱللَّهُ ۚ وَٱلَّٰتِى تَخَافُونَ نُشُوزَهُنَّ فَعِظُوهُنَّ وَٱهْجُرُوهُنَّ فِى ٱلْمَضَاجِعِ وَٱضْرِبُوهُنَّ ۖ فَإِنْ أَطَعْنَكُمْ فَلَا تَبْغُوا۟ عَلَيْهِنَّ سَبِيلًا ۗ إِنَّ ٱللَّهَ كَانَ عَلِيًّۭا كَبِيرًۭا
- (5:8) [listed for 1:6] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ لِلَّهِ شُهَدَآءَ بِٱلْقِسْطِ ۖ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ عَلَىٰٓ أَلَّا تَعْدِلُوا۟ ۚ ٱعْدِلُوا۟ هُوَ أَقْرَبُ لِلتَّقْوَىٰ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (5:77) [listed for 1:6] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ غَيْرَ ٱلْحَقِّ وَلَا تَتَّبِعُوٓا۟ أَهْوَآءَ قَوْمٍۢ قَدْ ضَلُّوا۟ مِن قَبْلُ وَأَضَلُّوا۟ كَثِيرًۭا وَضَلُّوا۟ عَن سَوَآءِ ٱلسَّبِيلِ
- (6:39) [listed for 1:6] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا صُمٌّۭ وَبُكْمٌۭ فِى ٱلظُّلُمَٰتِ ۗ مَن يَشَإِ ٱللَّهُ يُضْلِلْهُ وَمَن يَشَأْ يَجْعَلْهُ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (6:71) [listed for 1:6] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:88) [listed for 1:6] ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۚ وَلَوْ أَشْرَكُوا۟ لَحَبِطَ عَنْهُم مَّا كَانُوا۟ يَعْمَلُونَ
- (6:90) [listed for 1:6] [cited in ¶7] أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا ۖ إِنْ هُوَ إِلَّا ذِكْرَىٰ لِلْعَٰلَمِينَ
- (7:146) [listed for 1:6] سَأَصْرِفُ عَنْ ءَايَٰتِىَ ٱلَّذِينَ يَتَكَبَّرُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَإِن يَرَوْا۟ كُلَّ ءَايَةٍۢ لَّا يُؤْمِنُوا۟ بِهَا وَإِن يَرَوْا۟ سَبِيلَ ٱلرُّشْدِ لَا يَتَّخِذُوهُ سَبِيلًۭا وَإِن يَرَوْا۟ سَبِيلَ ٱلْغَىِّ يَتَّخِذُوهُ سَبِيلًۭا ۚ ذَٰلِكَ بِأَنَّهُمْ كَذَّبُوا۟ بِـَٔايَٰتِنَا وَكَانُوا۟ عَنْهَا غَٰفِلِينَ
- (7:178) [listed for 1:6] مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِى ۖ وَمَن يُضْلِلْ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (8:3) [listed for 1:6] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (10:9) [listed for 1:6] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ يَهْدِيهِمْ رَبُّهُم بِإِيمَٰنِهِمْ ۖ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ فِى جَنَّٰتِ ٱلنَّعِيمِ
- (14:12) [listed for 1:6] وَمَا لَنَآ أَلَّا نَتَوَكَّلَ عَلَى ٱللَّهِ وَقَدْ هَدَىٰنَا سُبُلَنَا ۚ وَلَنَصْبِرَنَّ عَلَىٰ مَآ ءَاذَيْتُمُونَا ۚ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُتَوَكِّلُونَ
- (14:40) [listed for 1:6] رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ
- (16:36) [listed for 1:6] وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ ۖ فَمِنْهُم مَّنْ هَدَى ٱللَّهُ وَمِنْهُم مَّنْ حَقَّتْ عَلَيْهِ ٱلضَّلَٰلَةُ ۚ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (17:35) [listed for 1:6] [cited in ¶19] وَأَوْفُوا۟ ٱلْكَيْلَ إِذَا كِلْتُمْ وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ ۚ ذَٰلِكَ خَيْرٌۭ وَأَحْسَنُ تَأْوِيلًۭا
- (17:97) [listed for 1:6] وَمَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُمْ أَوْلِيَآءَ مِن دُونِهِۦ ۖ وَنَحْشُرُهُمْ يَوْمَ ٱلْقِيَٰمَةِ عَلَىٰ وُجُوهِهِمْ عُمْيًۭا وَبُكْمًۭا وَصُمًّۭا ۖ مَّأْوَىٰهُمْ جَهَنَّمُ ۖ كُلَّمَا خَبَتْ زِدْنَٰهُمْ سَعِيرًۭا
- (18:17) [listed for 1:6] ۞ وَتَرَى ٱلشَّمْسَ إِذَا طَلَعَت تَّزَٰوَرُ عَن كَهْفِهِمْ ذَاتَ ٱلْيَمِينِ وَإِذَا غَرَبَت تَّقْرِضُهُمْ ذَاتَ ٱلشِّمَالِ وَهُمْ فِى فَجْوَةٍۢ مِّنْهُ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ ۗ مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُۥ وَلِيًّۭا مُّرْشِدًۭا
- (18:24) [listed for 1:6] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (19:76) [listed for 1:6] [cited in ¶3] وَيَزِيدُ ٱللَّهُ ٱلَّذِينَ ٱهْتَدَوْا۟ هُدًۭى ۗ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌۭ مَّرَدًّا
- (20:50) [listed for 1:6] [cited in ¶6] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (20:82) [listed for 1:6] وَإِنِّى لَغَفَّارٌۭ لِّمَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا ثُمَّ ٱهْتَدَىٰ
- (20:135) [listed for 1:6] قُلْ كُلٌّۭ مُّتَرَبِّصٌۭ فَتَرَبَّصُوا۟ ۖ فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ
- (21:112) [listed for 1:6] قَٰلَ رَبِّ ٱحْكُم بِٱلْحَقِّ ۗ وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (22:54) [listed for 1:6] وَلِيَعْلَمَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّكَ فَيُؤْمِنُوا۟ بِهِۦ فَتُخْبِتَ لَهُۥ قُلُوبُهُمْ ۗ وَإِنَّ ٱللَّهَ لَهَادِ ٱلَّذِينَ ءَامَنُوٓا۟ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (23:74) [listed for 1:6] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- (24:35) [listed for 1:6] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (25:57) [listed for 1:6] قُلْ مَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ إِلَّا مَن شَآءَ أَن يَتَّخِذَ إِلَىٰ رَبِّهِۦ سَبِيلًۭا
- (26:182) [listed for 1:6] [cited in ¶19] وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ
- (27:3) [listed for 1:6] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (27:35) [listed for 1:6] وَإِنِّى مُرْسِلَةٌ إِلَيْهِم بِهَدِيَّةٍۢ فَنَاظِرَةٌۢ بِمَ يَرْجِعُ ٱلْمُرْسَلُونَ
- (29:69) [listed for 1:6] وَٱلَّذِينَ جَٰهَدُوا۟ فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا ۚ وَإِنَّ ٱللَّهَ لَمَعَ ٱلْمُحْسِنِينَ
- (30:43) [listed for 1:6] فَأَقِمْ وَجْهَكَ لِلدِّينِ ٱلْقَيِّمِ مِن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۖ يَوْمَئِذٍۢ يَصَّدَّعُونَ
- (31:3) [listed for 1:6] هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ
- (35:8) [listed for 1:6] أَفَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ فَرَءَاهُ حَسَنًۭا ۖ فَإِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۖ فَلَا تَذْهَبْ نَفْسُكَ عَلَيْهِمْ حَسَرَٰتٍ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِمَا يَصْنَعُونَ
- (36:4) [listed for 1:6] عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (36:66) [listed for 1:6] وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ
- (37:23) [listed for 1:6] [cited in ¶12] مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ
- (38:22) [listed for 1:6] إِذْ دَخَلُوا۟ عَلَىٰ دَاوُۥدَ فَفَزِعَ مِنْهُمْ ۖ قَالُوا۟ لَا تَخَفْ ۖ خَصْمَانِ بَغَىٰ بَعْضُنَا عَلَىٰ بَعْضٍۢ فَٱحْكُم بَيْنَنَا بِٱلْحَقِّ وَلَا تُشْطِطْ وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ
- (39:18) [listed for 1:6] ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَىٰهُمُ ٱللَّهُ ۖ وَأُو۟لَٰٓئِكَ هُمْ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:23) [listed for 1:6] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (39:36) [listed for 1:6] أَلَيْسَ ٱللَّهُ بِكَافٍ عَبْدَهُۥ ۖ وَيُخَوِّفُونَكَ بِٱلَّذِينَ مِن دُونِهِۦ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (39:37) [listed for 1:6] وَمَن يَهْدِ ٱللَّهُ فَمَا لَهُۥ مِن مُّضِلٍّ ۗ أَلَيْسَ ٱللَّهُ بِعَزِيزٍۢ ذِى ٱنتِقَامٍۢ
- (41:6) [listed for 1:6] قُلْ إِنَّمَآ أَنَا۠ بَشَرٌۭ مِّثْلُكُمْ يُوحَىٰٓ إِلَىَّ أَنَّمَآ إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَٱسْتَقِيمُوٓا۟ إِلَيْهِ وَٱسْتَغْفِرُوهُ ۗ وَوَيْلٌۭ لِّلْمُشْرِكِينَ
- (41:17) [listed for 1:6] وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ فَأَخَذَتْهُمْ صَٰعِقَةُ ٱلْعَذَابِ ٱلْهُونِ بِمَا كَانُوا۟ يَكْسِبُونَ
- (47:17) [listed for 1:6] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
- (48:20) [listed for 1:6] وَعَدَكُمُ ٱللَّهُ مَغَانِمَ كَثِيرَةًۭ تَأْخُذُونَهَا فَعَجَّلَ لَكُمْ هَٰذِهِۦ وَكَفَّ أَيْدِىَ ٱلنَّاسِ عَنكُمْ وَلِتَكُونَ ءَايَةًۭ لِّلْمُؤْمِنِينَ وَيَهْدِيَكُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (49:17) [listed for 1:6] يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا۟ ۖ قُل لَّا تَمُنُّوا۟ عَلَىَّ إِسْلَٰمَكُم ۖ بَلِ ٱللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَىٰكُمْ لِلْإِيمَٰنِ إِن كُنتُمْ صَٰدِقِينَ
- (53:30) [listed for 1:6] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (64:6) [listed for 1:6] ذَٰلِكَ بِأَنَّهُۥ كَانَت تَّأْتِيهِمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَقَالُوٓا۟ أَبَشَرٌۭ يَهْدُونَنَا فَكَفَرُوا۟ وَتَوَلَّوا۟ ۚ وَّٱسْتَغْنَى ٱللَّهُ ۚ وَٱللَّهُ غَنِىٌّ حَمِيدٌۭ
- (65:2) [listed for 1:6] فَإِذَا بَلَغْنَ أَجَلَهُنَّ فَأَمْسِكُوهُنَّ بِمَعْرُوفٍ أَوْ فَارِقُوهُنَّ بِمَعْرُوفٍۢ وَأَشْهِدُوا۟ ذَوَىْ عَدْلٍۢ مِّنكُمْ وَأَقِيمُوا۟ ٱلشَّهَٰدَةَ لِلَّهِ ۚ ذَٰلِكُمْ يُوعَظُ بِهِۦ مَن كَانَ يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مَخْرَجًۭا
- (72:16) [listed for 1:6] [cited in ¶15] وَأَلَّوِ ٱسْتَقَٰمُوا۟ عَلَى ٱلطَّرِيقَةِ لَأَسْقَيْنَٰهُم مَّآءً غَدَقًۭا
- (87:3) [listed for 1:6] وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- (90:10) [listed for 1:6] وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- (98:3) [listed for 1:6] فِيهَا كُتُبٌۭ قَيِّمَةٌۭ

## named by the passage's own list as strong for this ayah (9)

- (6:127) [listed for 1:6] ۞ لَهُمْ دَارُ ٱلسَّلَٰمِ عِندَ رَبِّهِمْ ۖ وَهُوَ وَلِيُّهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- (11:112) [listed for 1:6] [cited in ¶16] فَٱسْتَقِمْ كَمَآ أُمِرْتَ وَمَن تَابَ مَعَكَ وَلَا تَطْغَوْا۟ ۚ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (14:27) [listed for 1:6] يُثَبِّتُ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ بِٱلْقَوْلِ ٱلثَّابِتِ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَفِى ٱلْءَاخِرَةِ ۖ وَيُضِلُّ ٱللَّهُ ٱلظَّٰلِمِينَ ۚ وَيَفْعَلُ ٱللَّهُ مَا يَشَآءُ
- (16:76) [listed for 1:6] وَضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلَيْنِ أَحَدُهُمَآ أَبْكَمُ لَا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَهُوَ كَلٌّ عَلَىٰ مَوْلَىٰهُ أَيْنَمَا يُوَجِّههُّ لَا يَأْتِ بِخَيْرٍ ۖ هَلْ يَسْتَوِى هُوَ وَمَن يَأْمُرُ بِٱلْعَدْلِ ۙ وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (31:19) [listed for 1:6] وَٱقْصِدْ فِى مَشْيِكَ وَٱغْضُضْ مِن صَوْتِكَ ۚ إِنَّ أَنكَرَ ٱلْأَصْوَٰتِ لَصَوْتُ ٱلْحَمِيرِ
- (43:10) [listed for 1:6] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَجَعَلَ لَكُمْ فِيهَا سُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
- (68:7) [listed for 1:6] إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (81:26) [listed for 1:6] فَأَيْنَ تَذْهَبُونَ
- (81:28) [listed for 1:6] لِمَن شَآءَ مِنكُمْ أَن يَسْتَقِيمَ

## named by the passage's own list as medium for this ayah (11)

- (2:186) [listed for 1:6] وَإِذَا سَأَلَكَ عِبَادِى عَنِّى فَإِنِّى قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ ۖ فَلْيَسْتَجِيبُوا۟ لِى وَلْيُؤْمِنُوا۟ بِى لَعَلَّهُمْ يَرْشُدُونَ
- (2:286) [listed for 1:6] لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا ٱكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَآ إِصْرًۭا كَمَا حَمَلْتَهُۥ عَلَى ٱلَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِۦ ۖ وَٱعْفُ عَنَّا وَٱغْفِرْ لَنَا وَٱرْحَمْنَآ ۚ أَنتَ مَوْلَىٰنَا فَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (7:43) [listed for 1:6] وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ ۖ وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى هَدَىٰنَا لِهَٰذَا وَمَا كُنَّا لِنَهْتَدِىَ لَوْلَآ أَنْ هَدَىٰنَا ٱللَّهُ ۖ لَقَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ ۖ وَنُودُوٓا۟ أَن تِلْكُمُ ٱلْجَنَّةُ أُورِثْتُمُوهَا بِمَا كُنتُمْ تَعْمَلُونَ
- (11:19) [listed for 1:6] ٱلَّذِينَ يَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًۭا وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (15:87) [listed for 1:6] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (43:57) [listed for 1:6] ۞ وَلَمَّا ضُرِبَ ٱبْنُ مَرْيَمَ مَثَلًا إِذَا قَوْمُكَ مِنْهُ يَصِدُّونَ
- (73:6) [listed for 1:6] إِنَّ نَاشِئَةَ ٱلَّيْلِ هِىَ أَشَدُّ وَطْـًۭٔا وَأَقْوَمُ قِيلًا
- (73:20) [listed for 1:6] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ
- (78:39) [listed for 1:6] ذَٰلِكَ ٱلْيَوْمُ ٱلْحَقُّ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا
- (93:11) [listed for 1:6] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (98:5) [listed for 1:6] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ

## weak (this ayah's own list) (8)

- (2:196) [listed for 1:6] [cited in ¶21] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (5:68) [listed for 1:6] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَسْتُمْ عَلَىٰ شَىْءٍ حَتَّىٰ تُقِيمُوا۟ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ وَمَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُمْ ۗ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۖ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (6:154) [listed for 1:6] ثُمَّ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ تَمَامًا عَلَى ٱلَّذِىٓ أَحْسَنَ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُم بِلِقَآءِ رَبِّهِمْ يُؤْمِنُونَ
- (14:28) [listed for 1:6] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ بَدَّلُوا۟ نِعْمَتَ ٱللَّهِ كُفْرًۭا وَأَحَلُّوا۟ قَوْمَهُمْ دَارَ ٱلْبَوَارِ
- (27:2) [listed for 1:6] هُدًۭى وَبُشْرَىٰ لِلْمُؤْمِنِينَ
- (53:23) [listed for 1:6] إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ وَمَا تَهْوَى ٱلْأَنفُسُ ۖ وَلَقَدْ جَآءَهُم مِّن رَّبِّهِمُ ٱلْهُدَىٰٓ
- (57:10) [listed for 1:6] وَمَا لَكُمْ أَلَّا تُنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ وَلِلَّهِ مِيرَٰثُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ لَا يَسْتَوِى مِنكُم مَّنْ أَنفَقَ مِن قَبْلِ ٱلْفَتْحِ وَقَٰتَلَ ۚ أُو۟لَٰٓئِكَ أَعْظَمُ دَرَجَةًۭ مِّنَ ٱلَّذِينَ أَنفَقُوا۟ مِنۢ بَعْدُ وَقَٰتَلُوا۟ ۚ وَكُلًّۭا وَعَدَ ٱللَّهُ ٱلْحُسْنَىٰ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- (62:5) [listed for 1:6] مَثَلُ ٱلَّذِينَ حُمِّلُوا۟ ٱلتَّوْرَىٰةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ ٱلْحِمَارِ يَحْمِلُ أَسْفَارًۢا ۚ بِئْسَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِ ٱللَّهِ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ

## named by the passage's own list as weak for this ayah (16)

- (2:255) [listed for 1:6] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (4:36) [listed for 1:6] ۞ وَٱعْبُدُوا۟ ٱللَّهَ وَلَا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا وَبِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱلْجَارِ ذِى ٱلْقُرْبَىٰ وَٱلْجَارِ ٱلْجُنُبِ وَٱلصَّاحِبِ بِٱلْجَنۢبِ وَٱبْنِ ٱلسَّبِيلِ وَمَا مَلَكَتْ أَيْمَٰنُكُمْ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ مَن كَانَ مُخْتَالًۭا فَخُورًا
- (15:24) [listed for 1:6] وَلَقَدْ عَلِمْنَا ٱلْمُسْتَقْدِمِينَ مِنكُمْ وَلَقَدْ عَلِمْنَا ٱلْمُسْتَـْٔخِرِينَ
- (44:26) [listed for 1:6] وَزُرُوعٍۢ وَمَقَامٍۢ كَرِيمٍۢ
- (46:13) [listed for 1:6] إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (50:1) [listed for 1:6] قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ
- (55:9) [listed for 1:6] وَأَقِيمُوا۟ ٱلْوَزْنَ بِٱلْقِسْطِ وَلَا تُخْسِرُوا۟ ٱلْمِيزَانَ
- (62:11) [listed for 1:6] وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ
- (70:33) [listed for 1:6] وَٱلَّذِينَ هُم بِشَهَٰدَٰتِهِمْ قَآئِمُونَ
- (74:5) [listed for 1:6] وَٱلرُّجْزَ فَٱهْجُرْ
- (78:36) [listed for 1:6] جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا
- (86:3) [listed for 1:6] ٱلنَّجْمُ ٱلثَّاقِبُ
- (89:27) [listed for 1:6] يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- (109:2) [listed for 1:6] لَآ أَعْبُدُ مَا تَعْبُدُونَ
- (109:4) [listed for 1:6] وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- (109:5) [listed for 1:6] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ

## neighbours: within two ayat of a passage the commentary cites (83)

- (2:140) [next to 2:142] أَمْ تَقُولُونَ إِنَّ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطَ كَانُوا۟ هُودًا أَوْ نَصَٰرَىٰ ۗ قُلْ ءَأَنتُمْ أَعْلَمُ أَمِ ٱللَّهُ ۗ وَمَنْ أَظْلَمُ مِمَّن كَتَمَ شَهَٰدَةً عِندَهُۥ مِنَ ٱللَّهِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (2:141) [next to 2:142] تِلْكَ أُمَّةٌۭ قَدْ خَلَتْ ۖ لَهَا مَا كَسَبَتْ وَلَكُم مَّا كَسَبْتُمْ ۖ وَلَا تُسْـَٔلُونَ عَمَّا كَانُوا۟ يَعْمَلُونَ
- (2:144) [next to 2:142] قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا يَعْمَلُونَ
- (2:145) [next to 2:143] وَلَئِنْ أَتَيْتَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ بِكُلِّ ءَايَةٍۢ مَّا تَبِعُوا۟ قِبْلَتَكَ ۚ وَمَآ أَنتَ بِتَابِعٍۢ قِبْلَتَهُمْ ۚ وَمَا بَعْضُهُم بِتَابِعٍۢ قِبْلَةَ بَعْضٍۢ ۚ وَلَئِنِ ٱتَّبَعْتَ أَهْوَآءَهُم مِّنۢ بَعْدِ مَا جَآءَكَ مِنَ ٱلْعِلْمِ ۙ إِنَّكَ إِذًۭا لَّمِنَ ٱلظَّٰلِمِينَ
- (2:194) [next to 2:196] ٱلشَّهْرُ ٱلْحَرَامُ بِٱلشَّهْرِ ٱلْحَرَامِ وَٱلْحُرُمَٰتُ قِصَاصٌۭ ۚ فَمَنِ ٱعْتَدَىٰ عَلَيْكُمْ فَٱعْتَدُوا۟ عَلَيْهِ بِمِثْلِ مَا ٱعْتَدَىٰ عَلَيْكُمْ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَعَ ٱلْمُتَّقِينَ
- (2:195) [next to 2:196] وَأَنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ وَلَا تُلْقُوا۟ بِأَيْدِيكُمْ إِلَى ٱلتَّهْلُكَةِ ۛ وَأَحْسِنُوٓا۟ ۛ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُحْسِنِينَ
- (2:197) [next to 2:196] ٱلْحَجُّ أَشْهُرٌۭ مَّعْلُومَٰتٌۭ ۚ فَمَن فَرَضَ فِيهِنَّ ٱلْحَجَّ فَلَا رَفَثَ وَلَا فُسُوقَ وَلَا جِدَالَ فِى ٱلْحَجِّ ۗ وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍۢ يَعْلَمْهُ ٱللَّهُ ۗ وَتَزَوَّدُوا۟ فَإِنَّ خَيْرَ ٱلزَّادِ ٱلتَّقْوَىٰ ۚ وَٱتَّقُونِ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ
- (2:198) [next to 2:196] لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ ۚ فَإِذَآ أَفَضْتُم مِّنْ عَرَفَٰتٍۢ فَٱذْكُرُوا۟ ٱللَّهَ عِندَ ٱلْمَشْعَرِ ٱلْحَرَامِ ۖ وَٱذْكُرُوهُ كَمَا هَدَىٰكُمْ وَإِن كُنتُم مِّن قَبْلِهِۦ لَمِنَ ٱلضَّآلِّينَ
- (4:173) [next to 4:175] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَيُوَفِّيهِمْ أُجُورَهُمْ وَيَزِيدُهُم مِّن فَضْلِهِۦ ۖ وَأَمَّا ٱلَّذِينَ ٱسْتَنكَفُوا۟ وَٱسْتَكْبَرُوا۟ فَيُعَذِّبُهُمْ عَذَابًا أَلِيمًۭا وَلَا يَجِدُونَ لَهُم مِّن دُونِ ٱللَّهِ وَلِيًّۭا وَلَا نَصِيرًۭا
- (4:174) [next to 4:175] يَٰٓأَيُّهَا ٱلنَّاسُ قَدْ جَآءَكُم بُرْهَٰنٌۭ مِّن رَّبِّكُمْ وَأَنزَلْنَآ إِلَيْكُمْ نُورًۭا مُّبِينًۭا
- (4:176) [next to 4:175] يَسْتَفْتُونَكَ قُلِ ٱللَّهُ يُفْتِيكُمْ فِى ٱلْكَلَٰلَةِ ۚ إِنِ ٱمْرُؤٌا۟ هَلَكَ لَيْسَ لَهُۥ وَلَدٌۭ وَلَهُۥٓ أُخْتٌۭ فَلَهَا نِصْفُ مَا تَرَكَ ۚ وَهُوَ يَرِثُهَآ إِن لَّمْ يَكُن لَّهَا وَلَدٌۭ ۚ فَإِن كَانَتَا ٱثْنَتَيْنِ فَلَهُمَا ٱلثُّلُثَانِ مِمَّا تَرَكَ ۚ وَإِن كَانُوٓا۟ إِخْوَةًۭ رِّجَالًۭا وَنِسَآءًۭ فَلِلذَّكَرِ مِثْلُ حَظِّ ٱلْأُنثَيَيْنِ ۗ يُبَيِّنُ ٱللَّهُ لَكُمْ أَن تَضِلُّوا۟ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۢ
- (5:93) [next to 5:95] لَيْسَ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جُنَاحٌۭ فِيمَا طَعِمُوٓا۟ إِذَا مَا ٱتَّقَوا۟ وَّءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ ثُمَّ ٱتَّقَوا۟ وَّءَامَنُوا۟ ثُمَّ ٱتَّقَوا۟ وَّأَحْسَنُوا۟ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
- (5:94) [next to 5:95] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَيَبْلُوَنَّكُمُ ٱللَّهُ بِشَىْءٍۢ مِّنَ ٱلصَّيْدِ تَنَالُهُۥٓ أَيْدِيكُمْ وَرِمَاحُكُمْ لِيَعْلَمَ ٱللَّهُ مَن يَخَافُهُۥ بِٱلْغَيْبِ ۚ فَمَنِ ٱعْتَدَىٰ بَعْدَ ذَٰلِكَ فَلَهُۥ عَذَابٌ أَلِيمٌۭ
- (5:96) [next to 5:95] أُحِلَّ لَكُمْ صَيْدُ ٱلْبَحْرِ وَطَعَامُهُۥ مَتَٰعًۭا لَّكُمْ وَلِلسَّيَّارَةِ ۖ وَحُرِّمَ عَلَيْكُمْ صَيْدُ ٱلْبَرِّ مَا دُمْتُمْ حُرُمًۭا ۗ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِىٓ إِلَيْهِ تُحْشَرُونَ
- (5:97) [next to 5:95] ۞ جَعَلَ ٱللَّهُ ٱلْكَعْبَةَ ٱلْبَيْتَ ٱلْحَرَامَ قِيَٰمًۭا لِّلنَّاسِ وَٱلشَّهْرَ ٱلْحَرَامَ وَٱلْهَدْىَ وَٱلْقَلَٰٓئِدَ ۚ ذَٰلِكَ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَأَنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌ
- (6:85) [next to 6:87] وَزَكَرِيَّا وَيَحْيَىٰ وَعِيسَىٰ وَإِلْيَاسَ ۖ كُلٌّۭ مِّنَ ٱلصَّٰلِحِينَ
- (6:86) [next to 6:87] وَإِسْمَٰعِيلَ وَٱلْيَسَعَ وَيُونُسَ وَلُوطًۭا ۚ وَكُلًّۭا فَضَّلْنَا عَلَى ٱلْعَٰلَمِينَ
- (6:89) [next to 6:87] أُو۟لَٰٓئِكَ ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ۚ فَإِن يَكْفُرْ بِهَا هَٰٓؤُلَآءِ فَقَدْ وَكَّلْنَا بِهَا قَوْمًۭا لَّيْسُوا۟ بِهَا بِكَٰفِرِينَ
- (6:91) [next to 6:90] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦٓ إِذْ قَالُوا۟ مَآ أَنزَلَ ٱللَّهُ عَلَىٰ بَشَرٍۢ مِّن شَىْءٍۢ ۗ قُلْ مَنْ أَنزَلَ ٱلْكِتَٰبَ ٱلَّذِى جَآءَ بِهِۦ مُوسَىٰ نُورًۭا وَهُدًۭى لِّلنَّاسِ ۖ تَجْعَلُونَهُۥ قَرَاطِيسَ تُبْدُونَهَا وَتُخْفُونَ كَثِيرًۭا ۖ وَعُلِّمْتُم مَّا لَمْ تَعْلَمُوٓا۟ أَنتُمْ وَلَآ ءَابَآؤُكُمْ ۖ قُلِ ٱللَّهُ ۖ ثُمَّ ذَرْهُمْ فِى خَوْضِهِمْ يَلْعَبُونَ
- (6:92) [next to 6:90] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ مُّصَدِّقُ ٱلَّذِى بَيْنَ يَدَيْهِ وَلِتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا ۚ وَٱلَّذِينَ يُؤْمِنُونَ بِٱلْءَاخِرَةِ يُؤْمِنُونَ بِهِۦ ۖ وَهُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ
- (6:151) [next to 6:153] ۞ قُلْ تَعَالَوْا۟ أَتْلُ مَا حَرَّمَ رَبُّكُمْ عَلَيْكُمْ ۖ أَلَّا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا ۖ وَلَا تَقْتُلُوٓا۟ أَوْلَٰدَكُم مِّنْ إِمْلَٰقٍۢ ۖ نَّحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ ۖ وَلَا تَقْرَبُوا۟ ٱلْفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ ۖ وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
- (6:152) [next to 6:153] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۖ وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَا ۖ وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ ۖ وَبِعَهْدِ ٱللَّهِ أَوْفُوا۟ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَذَكَّرُونَ
- (6:155) [next to 6:153] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ فَٱتَّبِعُوهُ وَٱتَّقُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (6:159) [next to 6:161] إِنَّ ٱلَّذِينَ فَرَّقُوا۟ دِينَهُمْ وَكَانُوا۟ شِيَعًۭا لَّسْتَ مِنْهُمْ فِى شَىْءٍ ۚ إِنَّمَآ أَمْرُهُمْ إِلَى ٱللَّهِ ثُمَّ يُنَبِّئُهُم بِمَا كَانُوا۟ يَفْعَلُونَ
- (6:160) [next to 6:161] مَن جَآءَ بِٱلْحَسَنَةِ فَلَهُۥ عَشْرُ أَمْثَالِهَا ۖ وَمَن جَآءَ بِٱلسَّيِّئَةِ فَلَا يُجْزَىٰٓ إِلَّا مِثْلَهَا وَهُمْ لَا يُظْلَمُونَ
- (6:162) [next to 6:161] قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (6:163) [next to 6:161] لَا شَرِيكَ لَهُۥ ۖ وَبِذَٰلِكَ أُمِرْتُ وَأَنَا۠ أَوَّلُ ٱلْمُسْلِمِينَ
- (7:14) [next to 7:16] قَالَ أَنظِرْنِىٓ إِلَىٰ يَوْمِ يُبْعَثُونَ
- (7:15) [next to 7:16] قَالَ إِنَّكَ مِنَ ٱلْمُنظَرِينَ
- (7:17) [next to 7:16] ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ ۖ وَلَا تَجِدُ أَكْثَرَهُمْ شَٰكِرِينَ
- (7:18) [next to 7:16] قَالَ ٱخْرُجْ مِنْهَا مَذْءُومًۭا مَّدْحُورًۭا ۖ لَّمَن تَبِعَكَ مِنْهُمْ لَأَمْلَأَنَّ جَهَنَّمَ مِنكُمْ أَجْمَعِينَ
- (11:110) [next to 11:112] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَٱخْتُلِفَ فِيهِ ۚ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَقُضِىَ بَيْنَهُمْ ۚ وَإِنَّهُمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- (11:111) [next to 11:112] وَإِنَّ كُلًّۭا لَّمَّا لَيُوَفِّيَنَّهُمْ رَبُّكَ أَعْمَٰلَهُمْ ۚ إِنَّهُۥ بِمَا يَعْمَلُونَ خَبِيرٌۭ
- (11:113) [next to 11:112] وَلَا تَرْكَنُوٓا۟ إِلَى ٱلَّذِينَ ظَلَمُوا۟ فَتَمَسَّكُمُ ٱلنَّارُ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِنْ أَوْلِيَآءَ ثُمَّ لَا تُنصَرُونَ
- (11:114) [next to 11:112] وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ وَزُلَفًۭا مِّنَ ٱلَّيْلِ ۚ إِنَّ ٱلْحَسَنَٰتِ يُذْهِبْنَ ٱلسَّيِّـَٔاتِ ۚ ذَٰلِكَ ذِكْرَىٰ لِلذَّٰكِرِينَ
- (17:7) [next to 17:9] إِنْ أَحْسَنتُمْ أَحْسَنتُمْ لِأَنفُسِكُمْ ۖ وَإِنْ أَسَأْتُمْ فَلَهَا ۚ فَإِذَا جَآءَ وَعْدُ ٱلْءَاخِرَةِ لِيَسُۥٓـُٔوا۟ وُجُوهَكُمْ وَلِيَدْخُلُوا۟ ٱلْمَسْجِدَ كَمَا دَخَلُوهُ أَوَّلَ مَرَّةٍۢ وَلِيُتَبِّرُوا۟ مَا عَلَوْا۟ تَتْبِيرًا
- (17:8) [next to 17:9] عَسَىٰ رَبُّكُمْ أَن يَرْحَمَكُمْ ۚ وَإِنْ عُدتُّمْ عُدْنَا ۘ وَجَعَلْنَا جَهَنَّمَ لِلْكَٰفِرِينَ حَصِيرًا
- (17:10) [next to 17:9] وَأَنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًۭا
- (17:11) [next to 17:9] وَيَدْعُ ٱلْإِنسَٰنُ بِٱلشَّرِّ دُعَآءَهُۥ بِٱلْخَيْرِ ۖ وَكَانَ ٱلْإِنسَٰنُ عَجُولًۭا
- (17:33) [next to 17:35] وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۗ وَمَن قُتِلَ مَظْلُومًۭا فَقَدْ جَعَلْنَا لِوَلِيِّهِۦ سُلْطَٰنًۭا فَلَا يُسْرِف فِّى ٱلْقَتْلِ ۖ إِنَّهُۥ كَانَ مَنصُورًۭا
- (17:34) [next to 17:35] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۚ وَأَوْفُوا۟ بِٱلْعَهْدِ ۖ إِنَّ ٱلْعَهْدَ كَانَ مَسْـُٔولًۭا
- (17:36) [next to 17:35] وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ ۚ إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًۭا
- (17:37) [next to 17:35] وَلَا تَمْشِ فِى ٱلْأَرْضِ مَرَحًا ۖ إِنَّكَ لَن تَخْرِقَ ٱلْأَرْضَ وَلَن تَبْلُغَ ٱلْجِبَالَ طُولًۭا
- (19:74) [next to 19:76] وَكَمْ أَهْلَكْنَا قَبْلَهُم مِّن قَرْنٍ هُمْ أَحْسَنُ أَثَٰثًۭا وَرِءْيًۭا
- (19:75) [next to 19:76] قُلْ مَن كَانَ فِى ٱلضَّلَٰلَةِ فَلْيَمْدُدْ لَهُ ٱلرَّحْمَٰنُ مَدًّا ۚ حَتَّىٰٓ إِذَا رَأَوْا۟ مَا يُوعَدُونَ إِمَّا ٱلْعَذَابَ وَإِمَّا ٱلسَّاعَةَ فَسَيَعْلَمُونَ مَنْ هُوَ شَرٌّۭ مَّكَانًۭا وَأَضْعَفُ جُندًۭا
- (19:77) [next to 19:76] أَفَرَءَيْتَ ٱلَّذِى كَفَرَ بِـَٔايَٰتِنَا وَقَالَ لَأُوتَيَنَّ مَالًۭا وَوَلَدًا
- (19:78) [next to 19:76] أَطَّلَعَ ٱلْغَيْبَ أَمِ ٱتَّخَذَ عِندَ ٱلرَّحْمَٰنِ عَهْدًۭا
- (20:48) [next to 20:50] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:49) [next to 20:50] قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ
- (20:51) [next to 20:50] قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ
- (20:52) [next to 20:50] قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى
- (26:180) [next to 26:182] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:181) [next to 26:182] ۞ أَوْفُوا۟ ٱلْكَيْلَ وَلَا تَكُونُوا۟ مِنَ ٱلْمُخْسِرِينَ
- (26:183) [next to 26:182] وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (26:184) [next to 26:182] وَٱتَّقُوا۟ ٱلَّذِى خَلَقَكُمْ وَٱلْجِبِلَّةَ ٱلْأَوَّلِينَ
- (37:20) [next to 37:22] وَقَالُوا۟ يَٰوَيْلَنَا هَٰذَا يَوْمُ ٱلدِّينِ
- (37:21) [next to 37:22] هَٰذَا يَوْمُ ٱلْفَصْلِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (37:24) [next to 37:22] وَقِفُوهُمْ ۖ إِنَّهُم مَّسْـُٔولُونَ
- (37:25) [next to 37:23] مَا لَكُمْ لَا تَنَاصَرُونَ
- (37:116) [next to 37:118] وَنَصَرْنَٰهُمْ فَكَانُوا۟ هُمُ ٱلْغَٰلِبِينَ
- (37:117) [next to 37:118] وَءَاتَيْنَٰهُمَا ٱلْكِتَٰبَ ٱلْمُسْتَبِينَ
- (37:119) [next to 37:118] وَتَرَكْنَا عَلَيْهِمَا فِى ٱلْءَاخِرِينَ
- (37:120) [next to 37:118] سَلَٰمٌ عَلَىٰ مُوسَىٰ وَهَٰرُونَ
- (41:28) [next to 41:30] ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (41:29) [next to 41:30] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ نَجْعَلْهُمَا تَحْتَ أَقْدَامِنَا لِيَكُونَا مِنَ ٱلْأَسْفَلِينَ
- (41:31) [next to 41:30] نَحْنُ أَوْلِيَآؤُكُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَفِى ٱلْءَاخِرَةِ ۖ وَلَكُمْ فِيهَا مَا تَشْتَهِىٓ أَنفُسُكُمْ وَلَكُمْ فِيهَا مَا تَدَّعُونَ
- (41:32) [next to 41:30] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (43:41) [next to 43:43] فَإِمَّا نَذْهَبَنَّ بِكَ فَإِنَّا مِنْهُم مُّنتَقِمُونَ
- (43:42) [next to 43:43] أَوْ نُرِيَنَّكَ ٱلَّذِى وَعَدْنَٰهُمْ فَإِنَّا عَلَيْهِم مُّقْتَدِرُونَ
- (43:44) [next to 43:43] وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ
- (43:45) [next to 43:43] وَسْـَٔلْ مَنْ أَرْسَلْنَا مِن قَبْلِكَ مِن رُّسُلِنَآ أَجَعَلْنَا مِن دُونِ ٱلرَّحْمَٰنِ ءَالِهَةًۭ يُعْبَدُونَ
- (48:0) [next to 48:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (48:1) [next to 48:2] إِنَّا فَتَحْنَا لَكَ فَتْحًۭا مُّبِينًۭا
- (48:3) [next to 48:2] وَيَنصُرَكَ ٱللَّهُ نَصْرًا عَزِيزًا
- (48:4) [next to 48:2] هُوَ ٱلَّذِىٓ أَنزَلَ ٱلسَّكِينَةَ فِى قُلُوبِ ٱلْمُؤْمِنِينَ لِيَزْدَادُوٓا۟ إِيمَٰنًۭا مَّعَ إِيمَٰنِهِمْ ۗ وَلِلَّهِ جُنُودُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَكَانَ ٱللَّهُ عَلِيمًا حَكِيمًۭا
- (67:20) [next to 67:22] أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- (67:21) [next to 67:22] أَمَّنْ هَٰذَا ٱلَّذِى يَرْزُقُكُمْ إِنْ أَمْسَكَ رِزْقَهُۥ ۚ بَل لَّجُّوا۟ فِى عُتُوٍّۢ وَنُفُورٍ
- (67:23) [next to 67:22] قُلْ هُوَ ٱلَّذِىٓ أَنشَأَكُمْ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۖ قَلِيلًۭا مَّا تَشْكُرُونَ
- (67:24) [next to 67:22] قُلْ هُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
- (72:14) [next to 72:16] وَأَنَّا مِنَّا ٱلْمُسْلِمُونَ وَمِنَّا ٱلْقَٰسِطُونَ ۖ فَمَنْ أَسْلَمَ فَأُو۟لَٰٓئِكَ تَحَرَّوْا۟ رَشَدًۭا
- (72:15) [next to 72:16] وَأَمَّا ٱلْقَٰسِطُونَ فَكَانُوا۟ لِجَهَنَّمَ حَطَبًۭا
- (72:17) [next to 72:16] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
- (72:18) [next to 72:16] وَأَنَّ ٱلْمَسَٰجِدَ لِلَّهِ فَلَا تَدْعُوا۟ مَعَ ٱللَّهِ أَحَدًۭا

