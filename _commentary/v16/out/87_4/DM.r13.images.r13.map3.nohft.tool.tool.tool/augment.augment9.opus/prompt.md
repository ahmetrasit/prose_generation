Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:4; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_4.reading.tr.md (prose paragraphs numbered) =====
## Üçüncü "O ki": cümlenin yeri

[¶1] Dördüncü ayet kendi başına bir cümle değildir. Birinci ayette adının tesbih edilmesi istenen Rabbi anlatan üçüncü tanımdır. Önce {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî haleka fe-sevvâ, gloss:yaratan ve düzene koyan, source:87:2} gelir, sonra {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp biçen ve yol gösteren, source:87:3}, en sonunda da {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran, source:87:4}. Üç "O ki" de aynı Rabbe döner. Dinleyen kişi, adını yücelteceği Rabbi bu tanımlardan tanır. Tanımların sırası geniş olandan elle tutulana doğru iner. Yaratmak her şeyi kapsar, ölçmek ve yol göstermek bir düzeni anlatır. Otlak ise insanın çadırının önünde gördüğü yeşildir.

[¶2] İlk iki tanım kendi ayeti içinde kapanan birer çifttir. Önce bir iş gelir, sonra "fe" bağlacıyla ona bağlanan sonucu: yarattı ve düzene koydu, ölçtü ve yol gösterdi. Dördüncü ayette çiftin yalnız ilk yarısı vardır. İkinci yarısı bir sonraki ayete taşar: {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5}. Bu yapıdan iki sonuç çıkar. Birincisi, beşinci ayetteki "onu" zamiri bu ayetin son kelimesine döner. Kuruyup döküntüye dönen şey ot olduğuna göre, buradaki merâ her şeyden önce otun kendisidir. İkincisi, bu çiftin sonucu ilk ikisindeki gibi bir tamamlanma değil, bir sona eriştir. Dördüncü ayet yeşili verir, beşinci ayet onu karartır. İkisi ayrı ayetlerde dursa da tek bir hareket olarak okunur.

[¶3] Ayette ne yağmurun ne de toprağın adı geçer. Kur'an aynı işi başka bir yerde kaynağıyla birlikte anlatır. Orada dirilişten kuşku duyanlara {ar:ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا, tr:e-entum eşeddu halkan emi's-semâu benâhâ, gloss:sizi yaratmak mı daha zor, yoksa göğü mü? Onu O kurdu, source:79:27} diye sorulur. Göğün {ar:فَسَوَّىٰهَا, tr:fe-sevvâhâ, gloss:ve onu düzene koydu, source:79:28} diye düzene konduğu söylenir, ardından yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir. Surenin ikinci ve dördüncü ayetlerindeki iki fiil, düzene koymak ve otlağı çıkarmak, orada da yan yana durur. Ancak orada toprak da su da anılır. Burada ise yalnız işi yapan ile ortaya çıkan ot kalır. Bu kısaltma dinleyenin dikkatini işin nasıl olduğundan onu yapanın kim olduğuna çevirir. Bir yüceltmenin içinde olunduğu için önemli olan da budur.

[¶4] Aynı kuruluş Kur'an'ın başka bir yerinde de vardır. Göklerle yeri kimin yarattığı sorulunca insanların "Güçlü ve Bilen" diyecekleri söylenir {source:43:9}. Ardından bu ad, bu suredeki gibi "O ki" cümleleriyle açılır. Önce {ar:ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَجَعَلَ لَكُمْ فِيهَا سُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ, tr:elleẕî ce'ale lekumu'l-arda mehden ve ce'ale lekum fîhâ subulen leallekum tehtedûn, gloss:yeri size bir beşik yapan, yolunuzu bulasınız diye orada size yollar açan, source:43:10} gelir, sonra {ar:وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ, tr:velleẕî nezzele mine's-semâi mâen bi-kaderin fe-enşernâ bihî beldeten meytâ keẕâlike tuhracûn, gloss:gökten ölçüyle su indiren, böylece ölü bir beldeyi dirilttik; siz de böyle çıkarılacaksınız, source:43:11}. Surenin üçüncü ayetindeki ölçü ve yol gösterme kökleri ile dördüncü ayetindeki çıkarma kökü, orada aynı tür bir cümle zincirinde bir arada geçer. O zincirin söylediği, dördüncü ayetin açıkça söylemediği şeydir: çıkarma işi sonunda insana da uzanır.

## Çıkarmak: yerinden ve halinden

[¶5] أَخْرَجَ, "çıkmak" anlamındaki fiilin ettirgen biçimidir, yani bir şeyi çıkmaya götürmektir. Çıkmanın kendisi girmenin tam tersidir: {ar:الخروج نقيض الدخول, tr:el-hurûcu nakîdu'd-duhûl, gloss:çıkmak girmenin zıddıdır, source:"خ ر ج,B001"}. Bu çıkışın iki yönü vardır: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerleştiği yerden ya da içinde bulunduğu halden dışarı belirdi, source:"خ ر ج,B001"}. Ot da iki türlü çıkar. Yerinden çıkar, çünkü tohumun ve kökün yattığı karanlık toprağı bırakıp ışığa yükselir. Halinden de çıkar, çünkü kuru taneyken yeşil bir yaprağa dönüşür. Fiil çoğunlukla elle tutulan şeyler için kullanılır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut varlıklar için söylenir, source:"خ ر ج,B002"}. Burada da somut bir iş anlatılır. Ot toprağı gerçekten yarar ve dışarı çıkar. Fiil ayrıca otun daha önce içeride olduğunu da söyler: görünmeyen bir yerde saklı duruyordu.

[¶6] Kur'an bu çıkarmanın birbirini izleyen basamaklarını başka bir yerde gösterir. Allah kendini gökten su indiren olarak anlatır ve şöyle der: {ar:فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا, tr:fe-ahracnâ bihî nebâte kulli şey'in fe-ahracnâ minhu hadiran nuhricu minhu habben muterâkibâ, gloss:onunla her şeyin bitkisini çıkardık, ondan bir yeşillik çıkardık, ondan da üst üste dizilmiş taneler çıkarırız, source:6:99}. Her çıkarma bir öncekinin içinden yapılır. Sudan bitki, bitkiden yeşil, yeşilden tane çıkar. Dördüncü ayetteki otlak da böyle bir zincirin halkasıdır. Arkasında tohum ve kök gibi görünmeyen bir geçmiş, önünde de beşinci ayetin tamamlayacağı görünür bir gelecek vardır.

[¶7] Türkçede ihraç kelimesi ya malı sınırın ötesine göndermek ya da birini okuldan veya partiden atmak demektir. İki durumda da çıkan şey ait olduğu yerden uzaklaşır. Arapça fiil bu ayette bir doğuşu anlatır: içeride saklı olanı görünür ve diri kılar.

[¶8] Kelimenin kök ailesinden gelen görüntüler, kelimenin bu ayetteki anlamının yanında duyulur, o anlamın yerini hiçbir zaman almaz. Bunlardan biri göğe aittir. Bulut boş gökte belirmeye başladığında da bu fiil kullanılırdı: {ar:أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن, tr:evvelu mâ yenşeu's-sehâbu fe-huve neş'un ve kad harace lehû hurûcun hasen, gloss:bulut ilk oluştuğunda ona neş' denir; onun için güzel bir çıkış çıktı denir, source:"خ ر ج,B005"}. Arapçada bulutun ilk belirişine "çıkış" denirdi. Otun topraktan çıkışından önce bulutun gökten çıkışı gelir. Ayetin anmadığı yağmuru surenin başka kelimeleri adlandırır: birinci ayetteki "ad" ve "Rab" kelimelerinin aileleri bulutu ve yağmuru içinde taşır. Ayetin kendi fiili ise yağmurun iki ucuna da aynı adı verir: yukarıda bulutun belirişine, aşağıda otun bitişine.

[¶9] Öbür görüntü yere aittir. Arapçada {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:bitkisi bir yerde çıkıp başka yerde çıkmayan toprak, source:"خ ر ج,B007"} denir. Aynı kalıp, hayvanın otlağın bir bölümünü yiyip bir bölümünü bırakmasını da anlatır {source:"خ ر ج,B007"}. Yeni çıkmış otlak bir halı gibi düzgün serilmez, alaca bulaca bir görünüm verir: bir yanda yeşil, öbür yanda çıplak toprak. Sürü yeşilin çıktığı yere doğru yürür ve geçtiği yerde yine böyle bir alacalık bırakır. Ayetin anlattığı otlak, böyle kuru bir toprakta yer yer beliren yeşildir. Bu yüzden her çıkışı ayrı bir lütuf olarak görülür.

## Merâ: ot, yer ve otlama

[¶10] Ayetin otlak için seçtiği kelime üç şeyi birden taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ri'yu ve'l-mevdiu ve'l-masdar, gloss:merâ hem ottur hem otlanan yerdir hem de otlamanın kendisidir, source:"ر ع ي,B001"}. Fiilin anlamı ise şöyle açıklanır: {ar:الرعي مصدر رعى يرعى رعيا الكلأ ونحوه, tr:er-ra'yu masdaru ra'â yer'â ra'yen el-kelee ve nahvehû, gloss:ra'y, otu ve benzerini otlamaktır, source:"ر ع ي,B001"}. Türkçede bu kökten kalan "mera" yalnız yeri, devletin ayırdığı otlak arazisini anlatır. "Riayet" kurala uymaya, "reaya" da yönetilen halka daralmıştır. Arapça kelimede ise ot, toprak ve hayvanın ağzı tek bir sözcükte birleşir. Bu ayette öne çıkan anlam ottur. Ancak bu ot, onu yiyecek ağzın gözünden görülmüş bir ottur. Kur'an başka yerlerde bitkinin kendisini anlatmak için نَبَات kelimesini kullanır. Merâ ise otu bir canlının rızkı olarak adlandırır.

[¶11] Kelime bu yüzden adını anmadan hayvanları ve onlarla geçinen insanları da ayetin içine alır. Kur'an otlağı andığı yerlerde bu bağı açıkça kurar. Yeryüzünden suyun ve otlağın çıkarıldığı ayetten iki ayet sonra {ar:مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:sizin ve hayvanlarınız için bir yararlanma payı, source:79:33} denir. Başka bir yerde Allah, inkâr edenlere kurak toprağa suyu nasıl sürdüğünü görüp görmediklerini sorar: {ar:فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ, tr:fe-nuhricu bihî zer'an te'kulu minhu en'âmuhum ve enfusuhum, gloss:onunla bir ekin çıkarırız; ondan hayvanları da kendileri de yer, source:32:27}. Bu cümlede hayvanlar insanlardan önce anılır. Otlak önce sürüyü besler, sürü de insanı süt, yün ve yük taşıma gücüyle besler. Arapçada obanın çevresinde otlayan develere özel bir ad verilmesi de bu düzenden gelir: {ar:الإبل التي ترعى حوالي القوم وديارهم لأنها الإبل التي يعتمل عليها, tr:el-ibilu'lletî ter'â havâleyi'l-kavmi ve diyârihim li-ennehe'l-ibilu'lletî yu'temelu aleyhâ, gloss:topluluğun ve yurtlarının çevresinde otlayan develer, çünkü üzerlerinde iş görülen develer bunlardır, source:"ر ع ي,B007"}. Evin yakınındaki otlak, işi yapan hayvanların otlağıdır. Böyle bir hayatta merâ kelimesi geçimin temelini anlatır.

[¶12] Aynı fiil, Musa'nın ağzından bir emir olarak da gelir. Firavun Musa ile kardeşine {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kim, ey Musa, source:20:49} diye sorar. Musa Rabbini, her şeye yaratılışını verip sonra yol gösteren olarak tanıtır {source:20:50}. Sonra konuşma yeryüzüne ve gökten inen suya geçer. Söz bu noktada birinci çoğul şahsa döner: {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Ardından {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ, tr:kulû ver'av en'âmekum, gloss:yiyin ve hayvanlarınızı otlatın, source:20:54} denir. Fiil burada geçişlidir: hayvan otlar, insan hayvanı otlatır. Merâ kelimesinin içindeki "otlama", Kur'an'da insana verilmiş bir iştir.

## Otlatan ve gözeten

[¶13] Arapçada otlamak ile korumak aynı fiille söylenir. Çobanın sürüyü otlatması, onu kuşatıp korumasıdır. Konuşanlar bu işi yöneticinin işine de taşırdı: {ar:الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته, tr:er-râî yer'a'l-mâşiye ey yehûtuhâ ve yahfazuhâ ve'l-vâlî yer'â raiyyetehû, gloss:çoban hayvanları otlatır, yani onları çevreler ve korur; yönetici de halkını böyle gözetir, source:"ر ع ي,B002"}. Bu bir benzetme değil, kök kimliğidir. Ayetteki "otlak" ile "çoban" aynı köktendir. Kur'an Allah'a çoban demez. Burada kurulan bağ okumanın işidir: ayetin otu adlandırmak için seçtiği kelime, çobanın mesleğinin kelimesidir. Çoban otlağı ancak arayıp bulur. Rabbi tanımlayan cümle ise otlağı çıkaranı anlatır. Birinci ayetteki "Rab" ile üçüncü ayetteki "yol gösterdi" kelimelerinin aileleri de bu çobanı sürüyle birlikte bir sahneye yerleştirir.

[¶14] Kur'an'da bu kökün çoğul hali, bir kuyunun başında, Musa'nın hikâyesinde geçer. Musa Medyen'e yönelir ve Rabbinin kendisine doğru yolu göstereceğini umar {source:28:22}. Medyen suyuna vardığında hayvanlarını sulayan bir kalabalık görür. Kenarda hayvanlarını geri tutan iki kadın vardır. Kadınlar {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌۭ كَبِيرٌۭ, tr:lâ neskî hattâ yusdira'r-riâu ve ebûnâ şeyhun kebîr, gloss:çobanlar sürülerini çekip gidinceye kadar sulamayız; babamız da çok yaşlıdır, source:28:23} der. Musa onların hayvanlarını sular. Kadınların babası daha sonra ona, kızlarından birini vermeyi ve karşılığında sekiz yıl kendisi için ücretle çalışmasını önerir {source:28:27}. Musa'nın elindeki değnek de bu hayattan kalmıştır. Ateşin başında ona elindekinin ne olduğu sorulur. Cevabı şudur: {ar:هِىَ عَصَاىَ أَتَوَكَّؤُا۟ عَلَيْهَا وَأَهُشُّ بِهَا عَلَىٰ غَنَمِى, tr:hiye asâye etevekkeu aleyhâ ve ehuşşu bihâ alâ ğanemî, gloss:bu benim değneğimdir; ona dayanırım, onunla koyunlarıma yaprak silkerim, source:20:18}. Firavun'un karşısında Rabbini bitkiyi çıkaran ve hayvanları otlatma emrini veren olarak tanıtan kişi, değneğiyle koyunlarına yaprak silkmiş biridir. Sure de kapanırken Musa'nın sayfalarını anar {source:87:19}.

[¶15] Çobanın bakışı yalnız bugünkü otta kalmaz. Aynı fiil, bir işin nereye varacağını gözetmeyi de anlatır: {ar:راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها, tr:râaytu'l-emra nazartu ilâme yasîr, raaytu'n-nucûme rakabtuhâ, gloss:işi gözettim, yani nereye varacağına baktım; yıldızları gözledim, source:"ر ع ي,B003"}. Bu, gece sürünün yanında uyanık kalıp yıldızlara bakan ve havanın, mevsimin, yağmurun gidişini kestiren kişinin bakışıdır. Dördüncü ayetin otlağı beşinci ayette sona erer. Otlağı çıkaran, onun varacağı yeri de baştan görür. Yedinci ayette Rab için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açıkta olanı da gizli kalanı da bilir, source:87:7} denir. Otlak kelimesinin kökündeki "sonuna bakma" anlamı bu bilgiye yaklaşır.

[¶16] Kökün bir kolu daha bu ayette ince bir gerilim yaratır. Konuşanlar {ar:أرعيت عليه إذا أبقيت عليه وترحمته, tr:er'aytu aleyhi iẕâ ebkaytu aleyhi ve terahhamtuh, gloss:onu esirgedim, yani onu bıraktım ve ona acıdım, source:"ر ع ي,B006"} derlerdi. Kısaca da {ar:الإرعاء الإبقاء, tr:el-ir'âu el-ibkâ, gloss:ir'â esirgeyip bırakmaktır, source:"ر ع ي,B006"} denirdi. Bu açıklamada kullanılan "bırakmak, sürdürmek" kelimesi, on yedinci ayetteki "daha kalıcı" kelimesiyle aynı köktendir. Ancak otlakla kalıcılığın kökleri ayrıdır. Aralarındaki bağ bir açıklamadan doğar, kök birliğinden doğmaz. Yine de surede anlamlı bir yer tutar: otlağın kendisi esirgenmez, döküntüye döner. Çobanın gözetimiyle yaşamaya devam eden ot değil sürüdür. Sure de neyin kalacağını sonunda söyler: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:ahiret ise daha hayırlı ve daha kalıcıdır, source:87:17}. Kur'an bu gözetme fiilini insana da yükler. Kurtuluşa eren müminler sayılırken onlar için {ar:وَٱلَّذِينَ هُمْ لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ, tr:velleẕîne hum li-emânâtihim ve ahdihim râûn, gloss:emanetlerini ve verdikleri sözü gözetenler, source:23:8} denir. Bu ayetlerin açıldığı söz, surenin on dördüncü ayetindeki "kurtuluşa erdi" fiiliyle başlar {source:23:1}.

## İkinci çıkış

[¶17] Kur'an otun topraktan çıkışını anlattığı yerlerde çoğu zaman bir adım daha atar. Allah rüzgârları rahmetinin önünde müjdeci olarak gönderir, ağırlaşan bulutu ölü bir beldeye sürer, suyu indirir ve şöyle der: {ar:فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız, belki düşünüp hatırlarsınız, source:7:57}. Başka bir surede inkârcılar {ar:أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا ۖ ذَٰلِكَ رَجْعٌۢ بَعِيدٌۭ, tr:e-iẕâ mitnâ ve kunnâ turâben ẕâlike rec'un ba'îd, gloss:öldüğümüzde ve toprak olduğumuzda mı? Bu, akla uzak bir dönüş, source:50:3} diye itiraz eder. Kur'an onlara bereketli suyu, bahçeleri, hurmaları ve diriltilen ölü beldeyi gösterir, sonra {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Nuh da kavmine şunu söylemişti: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا, tr:vallâhu enbetekum mine'l-ardi nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}, ve {ar:ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًۭا, tr:ŝumme yu'îdukum fîhâ ve yuhricukum ihrâcâ, gloss:sonra sizi oraya geri döndürecek ve sizi bir çıkarışla çıkaracak, source:71:18}. Musa'nın Firavun'a verdiği cevap da hayvanları otlatma emrinden hemen sonra aynı yere varır: {ar:مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ, tr:minhâ halaknâkum ve fîhâ nu'îdukum ve minhâ nuhricukum târaten uhrâ, gloss:sizi ondan yarattık, oraya döndüreceğiz ve bir kez daha oradan çıkaracağız, source:20:55}.

[¶18] Kur'an'ın kendi kullanımında otlağı çıkaran fiil, ölüleri çıkaran fiilin aynısıdır. Dördüncü ayet bu ikinci çıkışı açıkça söylemez, ama fiili onu çağırır. Sure de bu çağrıyı yanıtsız bırakmaz. On üçüncü ayet ateşe giren kişi için {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13} der. Otlak bunun tam tersini yaşar. Önce diri olarak çıkar, sonra ölü bir döküntüye döner. İki hali de bütünüyle yaşar. Ateşteki kişinin ise ikisinden de payı yoktur. On altıncı ve on yedinci ayetler de bu karşıtlığı tamamlar. Otlağın çıkışı bir kezdir ve döküntüyle biter. İnsanın "bir kez daha" çıkarılışı ise daha hayırlı ve daha kalıcı olana doğrudur.

[¶19] Otlak böylece iki şey öğretir. İlki, çıkarmanın mümkün olduğudur. Ölü toprağın her yıl yeşerdiğini gören kişi, ölülerin çıkarılmasını akla uzak sayamaz. Yedinci surenin "belki hatırlarsınız" sözü bu yüzden surenin dokuzuncu ve onuncu ayetlerindeki öğüde ve hatırlamaya bağlanır. İkincisi, bu dünyada çıkarılan her şeyin geçtiğidir. Kur'an'ın başka bir yerinde yeryüzünden suyun ve otlağın çıkarılmasının hemen ardından {ar:فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ, tr:fe-iẕâ câeti't-tâmmetu'l-kubrâ, gloss:o en büyük, her şeyi örten felaket geldiğinde, source:79:34} denmesi de bu yüzden şaşırtıcı değildir. Bu surede de otlağın yeşilinden birkaç ayet sonra "en büyük ateş" anılır {source:87:12}.

## Topraktan okumaya: yetiştirmek

[¶20] Çıkarma fiilinin bir kolu insanın yetişmesini anlatır. Bir hocanın elinde yetişen kişiye onun "çıkardığı" denirdi. Bunun açıklaması da şöyle yapılırdı: {ar:خريج فلان كأنه أخرجه من حد الجهل, tr:hirrîcu fulânin ke-ennehû ahracehû min haddi'l-cehl, gloss:falancanın yetiştirmesi; sanki onu bilgisizliğin sınırından dışarı çıkarmıştır, source:"خ ر ج,B002"}. Aynı kolda saklı olanı ortaya çıkarmanın bir adı daha vardır: {ar:الاستخراج كالاستنباط, tr:el-istihrâcu ke'l-istinbât, gloss:istihrâc, derindeki suyu çıkarıp ortaya koymak gibidir, source:"خ ر ج,B002"}. Bu görüntü de ayetteki anlamın yanında duyulur. Toprağın içinden yeşil nasıl çıkarsa, bilgisizliğin içinden de bilen bir insan öyle çıkar.

[¶21] Kur'an bu iki çıkışı yan yana koyar. {ar:وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًۭٔا وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ, tr:vallâhu ahracekum min butûni ummehâtikum lâ ta'lemûne şey'en ve ce'ale lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide, gloss:Allah sizi annelerinizin karnından hiçbir şey bilmez halde çıkardı ve size işitme, görme ve gönül verdi, source:16:78}. İnsan ilk çıkışında, toprağı yeni yarmış bir filiz kadar bilgisizdir. Kitabın işi de aynı fiille anlatılır. Peygamber'e {ar:كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:kitâbun enzelnâhu ileyke li-tuhrice'n-nâse mine'z-zulumâti ile'n-nûr, gloss:insanları karanlıklardan aydınlığa çıkarasın diye sana indirdiğimiz bir kitap, source:14:1} denir. Tohum toprağın karanlığından ışığa nasıl çıkıyorsa, insan da karanlıklardan öyle çıkarılır.

[¶22] Surenin akışı bu yolu izler. Otlak beşinci ayette döküntüye döner. Altıncı ayet hiçbir geçiş yapmadan Peygamber'e döner: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız ve sen unutmayacaksın, source:87:6}. Arka arkaya gelen bu iki ayette iki ayrı yetiştirme vardır. Topraktan çıkarılan ot kurur ve götürülür. Peygamber'e okutulan söz ise Allah'ın dilediği dışında unutulmaz, yani yerinde kalır. Dördüncü ayetin fiili, kökünün bu kolu sayesinde toprakla öğretimi birbirine bağlar. Altıncı ayet de ikisinin farkını gösterir: biri mevsimle gelip gider, öbürü kalır.

## Hasılat: yılın çıkardığı ve istenmeyen ücret

[¶23] Çıkarma kökü topraktan her yıl alınan ürüne de ad verir: {ar:الخرج والخراج ما يخرج من المال في السنة بقدر معلوم, tr:el-harcu ve'l-harâcu mâ yahrucu mine'l-mâli fi's-seneti bi-kaderin ma'lûm, gloss:harc ve harâc, maldan her yıl bilinen bir ölçüyle çıkandır, source:"خ ر ج,B003"}. Kısaca {ar:الخراج الغلة, tr:el-harâcu el-ğalle, gloss:harâc üründür, hasılattır, source:"خ ر ج,B003"} de denir. Aynı kelime birinin ödediği vergiyi de anlatır: {ar:الخراج والخرج الإتاوة لأنه مال يخرجه المعطي, tr:el-harâcu ve'l-harcu el-itâve li-ennehû mâlun yuhricuhu'l-mu'tî, gloss:harâc ve harc vergidir, çünkü onu veren kişi elinden çıkarır, source:"خ ر ج,B003"}. Türkçedeki "haraç" zorla alınan paraya dönüşmüştür. Arapçada ise kelimenin özünde yalnızca yılın çıkardığı şey vardır. Bu açıdan bakınca otlak toprağın yıllık hasılatıdır, ama bu hasılat için kimse bir şey ödemez. Sürü onu ücretsiz otlar ve otlağı çıkaran ondan hiçbir karşılık istemez. "Bilinen ölçü" ifadesi üçüncü ayetteki ölçmeyi, yıllık ürün de on dördüncü ayetteki tarlayı akla getirir. Bu ikisinin kurduğu sahne surenin bütününe aittir.

[¶24] Kur'an bu kelimeyi Allah'ın verdiği karşılık için de kullanır. Peygamber'i dinlemeyenlerden söz edilirken önce {ar:بَلْ أَتَيْنَٰهُم بِذِكْرِهِمْ فَهُمْ عَن ذِكْرِهِم مُّعْرِضُونَ, tr:bel eteynâhum bi-ẕikrihim fe-hum an ẕikrihim mu'ridûn, gloss:hayır, onlara kendi öğütlerini getirdik, ama onlar öğütlerinden yüz çeviriyorlar, source:23:71} denir. Sonra Peygamber'e şöyle sorulur: {ar:أَمْ تَسْـَٔلُهُمْ خَرْجًۭا فَخَرَاجُ رَبِّكَ خَيْرٌۭ ۖ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ, tr:em tes'eluhum harcen fe-harâcu rabbike hayrun ve huve hayru'r-râzikîn, gloss:yoksa onlardan bir ücret mi istiyorsun? Rabbinin vereceği karşılık daha hayırlıdır; O, rızık verenlerin en hayırlısıdır, source:23:72}. Ardından {ar:وَإِنَّكَ لَتَدْعُوهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:ve inneke le-ted'ûhum ilâ sırâtın mustekîm, gloss:sen onları dosdoğru bir yola çağırıyorsun, source:23:73} gelir. Bu üç ayette öğüt, istenmeyen ücret, Rabbin karşılığı ve yol bir arada geçer. Bu surede de otlağı karşılıksız çıkaran Rab, dokuzuncu ayette Peygamber'e {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt fayda verirse, source:87:9} der. Öğüt de otlak gibi ücretsiz sunulur. Rızkı veren karşılık istemez, öğüdü getiren de istemez. İkisinin de karşılığı Rabbin katındadır.

===== _commentary/v16/out/87_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: herbage noun vocalized ri'y (kasra), distinct from verbal noun ra'y
- memory: the Quran never calls God rā'ī (shepherd)
- memory: ahushshu in 20:18 means beating down leaves for sheep
- memory: khirrīj vocalization of the "trained student" word
- not written: خ ر ج B004 abscess emerging from body - no hold in this ayah's theme
- not written: خ ر ج B006 self-made noble / excelling horse / rebels - no tie to pasture or surah
- not written: خ ر ج B007 colour akhraj (more black than white) - belongs to 87:5's colour, would only duplicate
- not written: خ ر ج B008, B009, B010, B012, B013 - camel shape, saddlebag, game, partners' settlement, horse neck; no thematic work
- not written: خ ر ج B011 rhyme alif called khurūj - surah's rhyme is not of that kind; would mislead
- not written: ر ع ي B004 lending ear, rā'inā (2:104) - no anchor in this ayah; better at 87:9-10
- not written: ر ع ي B005 irʿawā, desisting - marked as a separate origin; would blur root identity

===== passages not cited (214) =====
## strong (this ayah's own list) (42)

- (2:22) [listed for 87:4] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
- (2:164) [listed for 87:4] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (6:95) [listed for 87:4] ۞ إِنَّ ٱللَّهَ فَالِقُ ٱلْحَبِّ وَٱلنَّوَىٰ ۖ يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَمُخْرِجُ ٱلْمَيِّتِ مِنَ ٱلْحَىِّ ۚ ذَٰلِكُمُ ٱللَّهُ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (6:99) [listed for 87:4] [cited in ¶6] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:57) [listed for 87:4] [cited in ¶17] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
- (7:58) [listed for 87:4] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
- (9:64) [listed for 87:4] يَحْذَرُ ٱلْمُنَٰفِقُونَ أَن تُنَزَّلَ عَلَيْهِمْ سُورَةٌۭ تُنَبِّئُهُم بِمَا فِى قُلُوبِهِمْ ۚ قُلِ ٱسْتَهْزِءُوٓا۟ إِنَّ ٱللَّهَ مُخْرِجٌۭ مَّا تَحْذَرُونَ
- (10:24) [listed for 87:4] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
- (16:10) [listed for 87:4] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
- (16:11) [listed for 87:4] يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ وَٱلنَّخِيلَ وَٱلْأَعْنَٰبَ وَمِن كُلِّ ٱلثَّمَرَٰتِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (16:65) [listed for 87:4] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
- (18:45) [listed for 87:4] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
- (22:5) [listed for 87:4] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
- (22:63) [listed for 87:4] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَتُصْبِحُ ٱلْأَرْضُ مُخْضَرَّةً ۗ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌۭ
- (23:8) [listed for 87:4] [cited in ¶16] وَٱلَّذِينَ هُمْ لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ
- (25:48) [listed for 87:4] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
- (26:7) [listed for 87:4] أَوَلَمْ يَرَوْا۟ إِلَى ٱلْأَرْضِ كَمْ أَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ
- (27:60) [listed for 87:4] أَمَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ لَكُم مِّنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا بِهِۦ حَدَآئِقَ ذَاتَ بَهْجَةٍۢ مَّا كَانَ لَكُمْ أَن تُنۢبِتُوا۟ شَجَرَهَآ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ بَلْ هُمْ قَوْمٌۭ يَعْدِلُونَ
- (29:63) [listed for 87:4] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
- (30:19) [listed for 87:4] يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَيُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ وَكَذَٰلِكَ تُخْرَجُونَ
- (30:24) [listed for 87:4] وَمِنْ ءَايَٰتِهِۦ يُرِيكُمُ ٱلْبَرْقَ خَوْفًۭا وَطَمَعًۭا وَيُنَزِّلُ مِنَ ٱلسَّمَآءِ مَآءًۭ فَيُحْىِۦ بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (32:27) [listed for 87:4] [cited in ¶11] أَوَلَمْ يَرَوْا۟ أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ ۖ أَفَلَا يُبْصِرُونَ
- (35:9) [listed for 87:4] وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ
- (36:33) [listed for 87:4] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
- (39:21) [listed for 87:4] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (41:39) [listed for 87:4] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (47:29) [listed for 87:4] أَمْ حَسِبَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌ أَن لَّن يُخْرِجَ ٱللَّهُ أَضْغَٰنَهُمْ
- (50:9) [listed for 87:4] وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا فَأَنۢبَتْنَا بِهِۦ جَنَّٰتٍۢ وَحَبَّ ٱلْحَصِيدِ
- (50:10) [listed for 87:4] وَٱلنَّخْلَ بَاسِقَٰتٍۢ لَّهَا طَلْعٌۭ نَّضِيدٌۭ
- (50:11) [listed for 87:4] [cited in ¶17] رِّزْقًۭا لِّلْعِبَادِ ۖ وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ ٱلْخُرُوجُ
- (57:20) [listed for 87:4] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (71:18) [listed for 87:4] [cited in ¶17] ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًۭا
- (78:14) [listed for 87:4] وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا
- (78:15) [listed for 87:4] لِّنُخْرِجَ بِهِۦ حَبًّۭا وَنَبَاتًۭا
- (78:16) [listed for 87:4] وَجَنَّٰتٍ أَلْفَافًا
- (79:31) [listed for 87:4] [cited in ¶3] أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا
- (80:24) [listed for 87:4] فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ
- (80:25) [listed for 87:4] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
- (80:26) [listed for 87:4] ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا
- (80:27) [listed for 87:4] فَأَنۢبَتْنَا فِيهَا حَبًّۭا
- (80:31) [listed for 87:4] وَفَٰكِهَةًۭ وَأَبًّۭا
- (80:32) [listed for 87:4] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ

## medium (this ayah's own list) (49)

- (2:265) [listed for 87:4] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
- (2:267) [listed for 87:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
- (6:141) [listed for 87:4] ۞ وَهُوَ ٱلَّذِىٓ أَنشَأَ جَنَّٰتٍۢ مَّعْرُوشَٰتٍۢ وَغَيْرَ مَعْرُوشَٰتٍۢ وَٱلنَّخْلَ وَٱلزَّرْعَ مُخْتَلِفًا أُكُلُهُۥ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُتَشَٰبِهًۭا وَغَيْرَ مُتَشَٰبِهٍۢ ۚ كُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
- (7:27) [listed for 87:4] يَٰبَنِىٓ ءَادَمَ لَا يَفْتِنَنَّكُمُ ٱلشَّيْطَٰنُ كَمَآ أَخْرَجَ أَبَوَيْكُم مِّنَ ٱلْجَنَّةِ يَنزِعُ عَنْهُمَا لِبَاسَهُمَا لِيُرِيَهُمَا سَوْءَٰتِهِمَآ ۗ إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ ۗ إِنَّا جَعَلْنَا ٱلشَّيَٰطِينَ أَوْلِيَآءَ لِلَّذِينَ لَا يُؤْمِنُونَ
- (7:32) [listed for 87:4] قُلْ مَنْ حَرَّمَ زِينَةَ ٱللَّهِ ٱلَّتِىٓ أَخْرَجَ لِعِبَادِهِۦ وَٱلطَّيِّبَٰتِ مِنَ ٱلرِّزْقِ ۚ قُلْ هِىَ لِلَّذِينَ ءَامَنُوا۟ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا خَالِصَةًۭ يَوْمَ ٱلْقِيَٰمَةِ ۗ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (8:5) [listed for 87:4] كَمَآ أَخْرَجَكَ رَبُّكَ مِنۢ بَيْتِكَ بِٱلْحَقِّ وَإِنَّ فَرِيقًۭا مِّنَ ٱلْمُؤْمِنِينَ لَكَٰرِهُونَ
- (10:31) [listed for 87:4] قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ أَمَّن يَمْلِكُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَمَن يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَمَن يُدَبِّرُ ٱلْأَمْرَ ۚ فَسَيَقُولُونَ ٱللَّهُ ۚ فَقُلْ أَفَلَا تَتَّقُونَ
- (11:52) [listed for 87:4] وَيَٰقَوْمِ ٱسْتَغْفِرُوا۟ رَبَّكُمْ ثُمَّ تُوبُوٓا۟ إِلَيْهِ يُرْسِلِ ٱلسَّمَآءَ عَلَيْكُم مِّدْرَارًۭا وَيَزِدْكُمْ قُوَّةً إِلَىٰ قُوَّتِكُمْ وَلَا تَتَوَلَّوْا۟ مُجْرِمِينَ
- (12:47) [listed for 87:4] قَالَ تَزْرَعُونَ سَبْعَ سِنِينَ دَأَبًۭا فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ
- (13:4) [listed for 87:4] وَفِى ٱلْأَرْضِ قِطَعٌۭ مُّتَجَٰوِرَٰتٌۭ وَجَنَّٰتٌۭ مِّنْ أَعْنَٰبٍۢ وَزَرْعٌۭ وَنَخِيلٌۭ صِنْوَانٌۭ وَغَيْرُ صِنْوَانٍۢ يُسْقَىٰ بِمَآءٍۢ وَٰحِدٍۢ وَنُفَضِّلُ بَعْضَهَا عَلَىٰ بَعْضٍۢ فِى ٱلْأُكُلِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (14:1) [listed for 87:4] [cited in ¶21] الٓر ۚ كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِ رَبِّهِمْ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- (14:5) [listed for 87:4] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ أَنْ أَخْرِجْ قَوْمَكَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
- (14:32) [listed for 87:4] ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ وَسَخَّرَ لَكُمُ ٱلْفُلْكَ لِتَجْرِىَ فِى ٱلْبَحْرِ بِأَمْرِهِۦ ۖ وَسَخَّرَ لَكُمُ ٱلْأَنْهَٰرَ
- (15:19) [listed for 87:4] وَٱلْأَرْضَ مَدَدْنَٰهَا وَأَلْقَيْنَا فِيهَا رَوَٰسِىَ وَأَنۢبَتْنَا فِيهَا مِن كُلِّ شَىْءٍۢ مَّوْزُونٍۢ
- (16:78) [listed for 87:4] [cited in ¶21] وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًۭٔا وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۙ لَعَلَّكُمْ تَشْكُرُونَ
- (19:66) [listed for 87:4] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (20:53) [listed for 87:4] [cited in ¶12] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
- (20:54) [listed for 87:4] [cited in ¶12] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:57) [listed for 87:4] قَالَ أَجِئْتَنَا لِتُخْرِجَنَا مِنْ أَرْضِنَا بِسِحْرِكَ يَٰمُوسَىٰ
- (20:117) [listed for 87:4] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (21:30) [listed for 87:4] أَوَلَمْ يَرَ ٱلَّذِينَ كَفَرُوٓا۟ أَنَّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ كَانَتَا رَتْقًۭا فَفَتَقْنَٰهُمَا ۖ وَجَعَلْنَا مِنَ ٱلْمَآءِ كُلَّ شَىْءٍ حَىٍّ ۖ أَفَلَا يُؤْمِنُونَ
- (23:18) [listed for 87:4] وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ ۖ وَإِنَّا عَلَىٰ ذَهَابٍۭ بِهِۦ لَقَٰدِرُونَ
- (23:19) [listed for 87:4] فَأَنشَأْنَا لَكُم بِهِۦ جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ لَّكُمْ فِيهَا فَوَٰكِهُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
- (24:40) [listed for 87:4] أَوْ كَظُلُمَٰتٍۢ فِى بَحْرٍۢ لُّجِّىٍّۢ يَغْشَىٰهُ مَوْجٌۭ مِّن فَوْقِهِۦ مَوْجٌۭ مِّن فَوْقِهِۦ سَحَابٌۭ ۚ ظُلُمَٰتٌۢ بَعْضُهَا فَوْقَ بَعْضٍ إِذَآ أَخْرَجَ يَدَهُۥ لَمْ يَكَدْ يَرَىٰهَا ۗ وَمَن لَّمْ يَجْعَلِ ٱللَّهُ لَهُۥ نُورًۭا فَمَا لَهُۥ مِن نُّورٍ
- (26:57) [listed for 87:4] فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍۢ وَعُيُونٍۢ
- (27:67) [listed for 87:4] وَقَالَ ٱلَّذِينَ كَفَرُوٓا۟ أَءِذَا كُنَّا تُرَٰبًۭا وَءَابَآؤُنَآ أَئِنَّا لَمُخْرَجُونَ
- (31:10) [listed for 87:4] خَلَقَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا ۖ وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ
- (34:15) [listed for 87:4] لَقَدْ كَانَ لِسَبَإٍۢ فِى مَسْكَنِهِمْ ءَايَةٌۭ ۖ جَنَّتَانِ عَن يَمِينٍۢ وَشِمَالٍۢ ۖ كُلُوا۟ مِن رِّزْقِ رَبِّكُمْ وَٱشْكُرُوا۟ لَهُۥ ۚ بَلْدَةٌۭ طَيِّبَةٌۭ وَرَبٌّ غَفُورٌۭ
- (42:28) [listed for 87:4] وَهُوَ ٱلَّذِى يُنَزِّلُ ٱلْغَيْثَ مِنۢ بَعْدِ مَا قَنَطُوا۟ وَيَنشُرُ رَحْمَتَهُۥ ۚ وَهُوَ ٱلْوَلِىُّ ٱلْحَمِيدُ
- (43:11) [listed for 87:4] [cited in ¶4] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
- (45:5) [listed for 87:4] وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن رِّزْقٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَتَصْرِيفِ ٱلرِّيَٰحِ ءَايَٰتٌۭ لِّقَوْمٍۢ يَعْقِلُونَ
- (46:17) [listed for 87:4] وَٱلَّذِى قَالَ لِوَٰلِدَيْهِ أُفٍّۢ لَّكُمَآ أَتَعِدَانِنِىٓ أَنْ أُخْرَجَ وَقَدْ خَلَتِ ٱلْقُرُونُ مِن قَبْلِى وَهُمَا يَسْتَغِيثَانِ ٱللَّهَ وَيْلَكَ ءَامِنْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ فَيَقُولُ مَا هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (48:29) [listed for 87:4] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
- (49:5) [listed for 87:4] وَلَوْ أَنَّهُمْ صَبَرُوا۟ حَتَّىٰ تَخْرُجَ إِلَيْهِمْ لَكَانَ خَيْرًۭا لَّهُمْ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (51:35) [listed for 87:4] فَأَخْرَجْنَا مَن كَانَ فِيهَا مِنَ ٱلْمُؤْمِنِينَ
- (55:10) [listed for 87:4] وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ
- (55:12) [listed for 87:4] وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ
- (56:63) [listed for 87:4] أَفَرَءَيْتُم مَّا تَحْرُثُونَ
- (56:64) [listed for 87:4] ءَأَنتُمْ تَزْرَعُونَهُۥٓ أَمْ نَحْنُ ٱلزَّٰرِعُونَ
- (57:27) [listed for 87:4] ثُمَّ قَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِرُسُلِنَا وَقَفَّيْنَا بِعِيسَى ٱبْنِ مَرْيَمَ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ وَجَعَلْنَا فِى قُلُوبِ ٱلَّذِينَ ٱتَّبَعُوهُ رَأْفَةًۭ وَرَحْمَةًۭ وَرَهْبَانِيَّةً ٱبْتَدَعُوهَا مَا كَتَبْنَٰهَا عَلَيْهِمْ إِلَّا ٱبْتِغَآءَ رِضْوَٰنِ ٱللَّهِ فَمَا رَعَوْهَا حَقَّ رِعَايَتِهَا ۖ فَـَٔاتَيْنَا ٱلَّذِينَ ءَامَنُوا۟ مِنْهُمْ أَجْرَهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (60:1) [listed for 87:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ عَدُوِّى وَعَدُوَّكُمْ أَوْلِيَآءَ تُلْقُونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَقَدْ كَفَرُوا۟ بِمَا جَآءَكُم مِّنَ ٱلْحَقِّ يُخْرِجُونَ ٱلرَّسُولَ وَإِيَّاكُمْ ۙ أَن تُؤْمِنُوا۟ بِٱللَّهِ رَبِّكُمْ إِن كُنتُمْ خَرَجْتُمْ جِهَٰدًۭا فِى سَبِيلِى وَٱبْتِغَآءَ مَرْضَاتِى ۚ تُسِرُّونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَأَنَا۠ أَعْلَمُ بِمَآ أَخْفَيْتُمْ وَمَآ أَعْلَنتُمْ ۚ وَمَن يَفْعَلْهُ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (60:9) [listed for 87:4] إِنَّمَا يَنْهَىٰكُمُ ٱللَّهُ عَنِ ٱلَّذِينَ قَٰتَلُوكُمْ فِى ٱلدِّينِ وَأَخْرَجُوكُم مِّن دِيَٰرِكُمْ وَظَٰهَرُوا۟ عَلَىٰٓ إِخْرَاجِكُمْ أَن تَوَلَّوْهُمْ ۚ وَمَن يَتَوَلَّهُمْ فَأُو۟لَٰٓئِكَ هُمُ ٱلظَّٰلِمُونَ
- (65:1) [listed for 87:4] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَطَلِّقُوهُنَّ لِعِدَّتِهِنَّ وَأَحْصُوا۟ ٱلْعِدَّةَ ۖ وَٱتَّقُوا۟ ٱللَّهَ رَبَّكُمْ ۖ لَا تُخْرِجُوهُنَّ مِنۢ بُيُوتِهِنَّ وَلَا يَخْرُجْنَ إِلَّآ أَن يَأْتِينَ بِفَٰحِشَةٍۢ مُّبَيِّنَةٍۢ ۚ وَتِلْكَ حُدُودُ ٱللَّهِ ۚ وَمَن يَتَعَدَّ حُدُودَ ٱللَّهِ فَقَدْ ظَلَمَ نَفْسَهُۥ ۚ لَا تَدْرِى لَعَلَّ ٱللَّهَ يُحْدِثُ بَعْدَ ذَٰلِكَ أَمْرًۭا
- (65:11) [listed for 87:4] رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
- (70:32) [listed for 87:4] وَٱلَّذِينَ هُمْ لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ
- (71:10) [listed for 87:4] فَقُلْتُ ٱسْتَغْفِرُوا۟ رَبَّكُمْ إِنَّهُۥ كَانَ غَفَّارًۭا
- (71:11) [listed for 87:4] يُرْسِلِ ٱلسَّمَآءَ عَلَيْكُم مِّدْرَارًۭا
- (71:12) [listed for 87:4] وَيُمْدِدْكُم بِأَمْوَٰلٍۢ وَبَنِينَ وَيَجْعَل لَّكُمْ جَنَّٰتٍۢ وَيَجْعَل لَّكُمْ أَنْهَٰرًۭا
- (99:2) [listed for 87:4] وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا

## named by the passage's own list as strong for this ayah (1)

- (16:13) [listed for 87:4] وَمَا ذَرَأَ لَكُمْ فِى ٱلْأَرْضِ مُخْتَلِفًا أَلْوَٰنُهُۥٓ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَذَّكَّرُونَ

## named by the passage's own list as medium for this ayah (21)

- (2:266) [listed for 87:4] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (7:10) [listed for 87:4] وَلَقَدْ مَكَّنَّٰكُمْ فِى ٱلْأَرْضِ وَجَعَلْنَا لَكُمْ فِيهَا مَعَٰيِشَ ۗ قَلِيلًۭا مَّا تَشْكُرُونَ
- (13:17) [listed for 87:4] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
- (15:20) [listed for 87:4] وَجَعَلْنَا لَكُمْ فِيهَا مَعَٰيِشَ وَمَن لَّسْتُمْ لَهُۥ بِرَٰزِقِينَ
- (16:6) [listed for 87:4] وَلَكُمْ فِيهَا جَمَالٌ حِينَ تُرِيحُونَ وَحِينَ تَسْرَحُونَ
- (16:69) [listed for 87:4] ثُمَّ كُلِى مِن كُلِّ ٱلثَّمَرَٰتِ فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًۭا ۚ يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌۭ مُّخْتَلِفٌ أَلْوَٰنُهُۥ فِيهِ شِفَآءٌۭ لِّلنَّاسِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (27:25) [listed for 87:4] أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ
- (30:50) [listed for 87:4] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (35:27) [listed for 87:4] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍۢ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌۭ وَحُمْرٌۭ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌۭ
- (36:71) [listed for 87:4] أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ
- (41:10) [listed for 87:4] وَجَعَلَ فِيهَا رَوَٰسِىَ مِن فَوْقِهَا وَبَٰرَكَ فِيهَا وَقَدَّرَ فِيهَآ أَقْوَٰتَهَا فِىٓ أَرْبَعَةِ أَيَّامٍۢ سَوَآءًۭ لِّلسَّآئِلِينَ
- (45:13) [listed for 87:4] وَسَخَّرَ لَكُم مَّا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ جَمِيعًۭا مِّنْهُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (50:7) [listed for 87:4] وَٱلْأَرْضَ مَدَدْنَٰهَا وَأَلْقَيْنَا فِيهَا رَوَٰسِىَ وَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
- (67:15) [listed for 87:4] هُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ ذَلُولًۭا فَٱمْشُوا۟ فِى مَنَاكِبِهَا وَكُلُوا۟ مِن رِّزْقِهِۦ ۖ وَإِلَيْهِ ٱلنُّشُورُ
- (71:17) [listed for 87:4] [cited in ¶17] وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا
- (74:34) [listed for 87:4] وَٱلصُّبْحِ إِذَآ أَسْفَرَ
- (78:6) [listed for 87:4] أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا
- (79:29) [listed for 87:4] وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا
- (80:28) [listed for 87:4] وَعِنَبًۭا وَقَضْبًۭا
- (91:6) [listed for 87:4] وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- (105:5) [listed for 87:4] فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ

## weak (this ayah's own list) (26)

- (2:84) [listed for 87:4] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ لَا تَسْفِكُونَ دِمَآءَكُمْ وَلَا تُخْرِجُونَ أَنفُسَكُم مِّن دِيَٰرِكُمْ ثُمَّ أَقْرَرْتُمْ وَأَنتُمْ تَشْهَدُونَ
- (2:104) [listed for 87:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقُولُوا۟ رَٰعِنَا وَقُولُوا۟ ٱنظُرْنَا وَٱسْمَعُوا۟ ۗ وَلِلْكَٰفِرِينَ عَذَابٌ أَلِيمٌۭ
- (2:240) [listed for 87:4] وَٱلَّذِينَ يُتَوَفَّوْنَ مِنكُمْ وَيَذَرُونَ أَزْوَٰجًۭا وَصِيَّةًۭ لِّأَزْوَٰجِهِم مَّتَٰعًا إِلَى ٱلْحَوْلِ غَيْرَ إِخْرَاجٍۢ ۚ فَإِنْ خَرَجْنَ فَلَا جُنَاحَ عَلَيْكُمْ فِى مَا فَعَلْنَ فِىٓ أَنفُسِهِنَّ مِن مَّعْرُوفٍۢ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌۭ
- (2:259) [listed for 87:4] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (2:261) [listed for 87:4] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
- (3:110) [listed for 87:4] كُنتُمْ خَيْرَ أُمَّةٍ أُخْرِجَتْ لِلنَّاسِ تَأْمُرُونَ بِٱلْمَعْرُوفِ وَتَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَتُؤْمِنُونَ بِٱللَّهِ ۗ وَلَوْ ءَامَنَ أَهْلُ ٱلْكِتَٰبِ لَكَانَ خَيْرًۭا لَّهُم ۚ مِّنْهُمُ ٱلْمُؤْمِنُونَ وَأَكْثَرُهُمُ ٱلْفَٰسِقُونَ
- (7:18) [listed for 87:4] قَالَ ٱخْرُجْ مِنْهَا مَذْءُومًۭا مَّدْحُورًۭا ۖ لَّمَن تَبِعَكَ مِنْهُمْ لَأَمْلَأَنَّ جَهَنَّمَ مِنكُمْ أَجْمَعِينَ
- (7:82) [listed for 87:4] وَمَا كَانَ جَوَابَ قَوْمِهِۦٓ إِلَّآ أَن قَالُوٓا۟ أَخْرِجُوهُم مِّن قَرْيَتِكُمْ ۖ إِنَّهُمْ أُنَاسٌۭ يَتَطَهَّرُونَ
- (7:123) [listed for 87:4] قَالَ فِرْعَوْنُ ءَامَنتُم بِهِۦ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّ هَٰذَا لَمَكْرٌۭ مَّكَرْتُمُوهُ فِى ٱلْمَدِينَةِ لِتُخْرِجُوا۟ مِنْهَآ أَهْلَهَا ۖ فَسَوْفَ تَعْلَمُونَ
- (8:30) [listed for 87:4] وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ ۚ وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ ۖ وَٱللَّهُ خَيْرُ ٱلْمَٰكِرِينَ
- (12:48) [listed for 87:4] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ سَبْعٌۭ شِدَادٌۭ يَأْكُلْنَ مَا قَدَّمْتُمْ لَهُنَّ إِلَّا قَلِيلًۭا مِّمَّا تُحْصِنُونَ
- (14:13) [listed for 87:4] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لِرُسُلِهِمْ لَنُخْرِجَنَّكُم مِّنْ أَرْضِنَآ أَوْ لَتَعُودُنَّ فِى مِلَّتِنَا ۖ فَأَوْحَىٰٓ إِلَيْهِمْ رَبُّهُمْ لَنُهْلِكَنَّ ٱلظَّٰلِمِينَ
- (18:94) [listed for 87:4] قَالُوا۟ يَٰذَا ٱلْقَرْنَيْنِ إِنَّ يَأْجُوجَ وَمَأْجُوجَ مُفْسِدُونَ فِى ٱلْأَرْضِ فَهَلْ نَجْعَلُ لَكَ خَرْجًا عَلَىٰٓ أَن تَجْعَلَ بَيْنَنَا وَبَيْنَهُمْ سَدًّۭا
- (20:63) [listed for 87:4] قَالُوٓا۟ إِنْ هَٰذَٰنِ لَسَٰحِرَٰنِ يُرِيدَانِ أَن يُخْرِجَاكُم مِّنْ أَرْضِكُم بِسِحْرِهِمَا وَيَذْهَبَا بِطَرِيقَتِكُمُ ٱلْمُثْلَىٰ
- (20:88) [listed for 87:4] فَأَخْرَجَ لَهُمْ عِجْلًۭا جَسَدًۭا لَّهُۥ خُوَارٌۭ فَقَالُوا۟ هَٰذَآ إِلَٰهُكُمْ وَإِلَٰهُ مُوسَىٰ فَنَسِىَ
- (23:20) [listed for 87:4] وَشَجَرَةًۭ تَخْرُجُ مِن طُورِ سَيْنَآءَ تَنۢبُتُ بِٱلدُّهْنِ وَصِبْغٍۢ لِّلْءَاكِلِينَ
- (24:43) [listed for 87:4] أَلَمْ تَرَ أَنَّ ٱللَّهَ يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ وَيُنَزِّلُ مِنَ ٱلسَّمَآءِ مِن جِبَالٍۢ فِيهَا مِنۢ بَرَدٍۢ فَيُصِيبُ بِهِۦ مَن يَشَآءُ وَيَصْرِفُهُۥ عَن مَّن يَشَآءُ ۖ يَكَادُ سَنَا بَرْقِهِۦ يَذْهَبُ بِٱلْأَبْصَٰرِ
- (26:35) [listed for 87:4] يُرِيدُ أَن يُخْرِجَكُم مِّنْ أَرْضِكُم بِسِحْرِهِۦ فَمَاذَا تَأْمُرُونَ
- (26:79) [listed for 87:4] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (26:167) [listed for 87:4] قَالُوا۟ لَئِن لَّمْ تَنتَهِ يَٰلُوطُ لَتَكُونَنَّ مِنَ ٱلْمُخْرَجِينَ
- (27:56) [listed for 87:4] ۞ فَمَا كَانَ جَوَابَ قَوْمِهِۦٓ إِلَّآ أَن قَالُوٓا۟ أَخْرِجُوٓا۟ ءَالَ لُوطٍۢ مِّن قَرْيَتِكُمْ ۖ إِنَّهُمْ أُنَاسٌۭ يَتَطَهَّرُونَ
- (36:80) [listed for 87:4] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
- (47:13) [listed for 87:4] وَكَأَيِّن مِّن قَرْيَةٍ هِىَ أَشَدُّ قُوَّةًۭ مِّن قَرْيَتِكَ ٱلَّتِىٓ أَخْرَجَتْكَ أَهْلَكْنَٰهُمْ فَلَا نَاصِرَ لَهُمْ
- (50:42) [listed for 87:4] يَوْمَ يَسْمَعُونَ ٱلصَّيْحَةَ بِٱلْحَقِّ ۚ ذَٰلِكَ يَوْمُ ٱلْخُرُوجِ
- (59:2) [listed for 87:4] هُوَ ٱلَّذِىٓ أَخْرَجَ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ مِن دِيَٰرِهِمْ لِأَوَّلِ ٱلْحَشْرِ ۚ مَا ظَنَنتُمْ أَن يَخْرُجُوا۟ ۖ وَظَنُّوٓا۟ أَنَّهُم مَّانِعَتُهُمْ حُصُونُهُم مِّنَ ٱللَّهِ فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟ ۖ وَقَذَفَ فِى قُلُوبِهِمُ ٱلرُّعْبَ ۚ يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ وَأَيْدِى ٱلْمُؤْمِنِينَ فَٱعْتَبِرُوا۟ يَٰٓأُو۟لِى ٱلْأَبْصَٰرِ
- (63:8) [listed for 87:4] يَقُولُونَ لَئِن رَّجَعْنَآ إِلَى ٱلْمَدِينَةِ لَيُخْرِجَنَّ ٱلْأَعَزُّ مِنْهَا ٱلْأَذَلَّ ۚ وَلِلَّهِ ٱلْعِزَّةُ وَلِرَسُولِهِۦ وَلِلْمُؤْمِنِينَ وَلَٰكِنَّ ٱلْمُنَٰفِقِينَ لَا يَعْلَمُونَ

## named by the passage's own list as weak for this ayah (10)

- (2:172) [listed for 87:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَٱشْكُرُوا۟ لِلَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (26:81) [listed for 87:4] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (36:34) [listed for 87:4] وَجَعَلْنَا فِيهَا جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ وَفَجَّرْنَا فِيهَا مِنَ ٱلْعُيُونِ
- (47:37) [listed for 87:4] إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ
- (54:7) [listed for 87:4] خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ
- (55:22) [listed for 87:4] يَخْرُجُ مِنْهُمَا ٱللُّؤْلُؤُ وَٱلْمَرْجَانُ
- (81:15) [listed for 87:4] فَلَآ أُقْسِمُ بِٱلْخُنَّسِ
- (84:16) [listed for 87:4] فَلَآ أُقْسِمُ بِٱلشَّفَقِ
- (86:7) [listed for 87:4] يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ
- (90:14) [listed for 87:4] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ

## neighbours: within two ayat of a passage the commentary cites (65)

- (6:97) [next to 6:99] وَهُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلنُّجُومَ لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (6:98) [next to 6:99] وَهُوَ ٱلَّذِىٓ أَنشَأَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ فَمُسْتَقَرٌّۭ وَمُسْتَوْدَعٌۭ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَفْقَهُونَ
- (6:100) [next to 6:99] وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ ٱلْجِنَّ وَخَلَقَهُمْ ۖ وَخَرَقُوا۟ لَهُۥ بَنِينَ وَبَنَٰتٍۭ بِغَيْرِ عِلْمٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يَصِفُونَ
- (6:101) [next to 6:99] بَدِيعُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ ۖ وَخَلَقَ كُلَّ شَىْءٍۢ ۖ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (7:55) [next to 7:57] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (7:56) [next to 7:57] وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا وَٱدْعُوهُ خَوْفًۭا وَطَمَعًا ۚ إِنَّ رَحْمَتَ ٱللَّهِ قَرِيبٌۭ مِّنَ ٱلْمُحْسِنِينَ
- (7:59) [next to 7:57] لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (14:0) [next to 14:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (14:2) [next to 14:1] ٱللَّهِ ٱلَّذِى لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَوَيْلٌۭ لِّلْكَٰفِرِينَ مِنْ عَذَابٍۢ شَدِيدٍ
- (14:3) [next to 14:1] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (16:76) [next to 16:78] وَضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلَيْنِ أَحَدُهُمَآ أَبْكَمُ لَا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَهُوَ كَلٌّ عَلَىٰ مَوْلَىٰهُ أَيْنَمَا يُوَجِّههُّ لَا يَأْتِ بِخَيْرٍ ۖ هَلْ يَسْتَوِى هُوَ وَمَن يَأْمُرُ بِٱلْعَدْلِ ۙ وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (16:77) [next to 16:78] وَلِلَّهِ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَمَآ أَمْرُ ٱلسَّاعَةِ إِلَّا كَلَمْحِ ٱلْبَصَرِ أَوْ هُوَ أَقْرَبُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (16:79) [next to 16:78] أَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ مُسَخَّرَٰتٍۢ فِى جَوِّ ٱلسَّمَآءِ مَا يُمْسِكُهُنَّ إِلَّا ٱللَّهُ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (16:80) [next to 16:78] وَٱللَّهُ جَعَلَ لَكُم مِّنۢ بُيُوتِكُمْ سَكَنًۭا وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا تَسْتَخِفُّونَهَا يَوْمَ ظَعْنِكُمْ وَيَوْمَ إِقَامَتِكُمْ ۙ وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا إِلَىٰ حِينٍۢ
- (20:16) [next to 20:18] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (20:17) [next to 20:18] وَمَا تِلْكَ بِيَمِينِكَ يَٰمُوسَىٰ
- (20:19) [next to 20:18] قَالَ أَلْقِهَا يَٰمُوسَىٰ
- (20:20) [next to 20:18] فَأَلْقَىٰهَا فَإِذَا هِىَ حَيَّةٌۭ تَسْعَىٰ
- (20:47) [next to 20:49] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
- (20:48) [next to 20:49] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:51) [next to 20:49] قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ
- (20:52) [next to 20:50] قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى
- (20:56) [next to 20:54] وَلَقَدْ أَرَيْنَٰهُ ءَايَٰتِنَا كُلَّهَا فَكَذَّبَ وَأَبَىٰ
- (23:0) [next to 23:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (23:2) [next to 23:1] ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ
- (23:3) [next to 23:1] وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ
- (23:6) [next to 23:8] إِلَّا عَلَىٰٓ أَزْوَٰجِهِمْ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَإِنَّهُمْ غَيْرُ مَلُومِينَ
- (23:7) [next to 23:8] فَمَنِ ٱبْتَغَىٰ وَرَآءَ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْعَادُونَ
- (23:9) [next to 23:8] وَٱلَّذِينَ هُمْ عَلَىٰ صَلَوَٰتِهِمْ يُحَافِظُونَ
- (23:10) [next to 23:8] أُو۟لَٰٓئِكَ هُمُ ٱلْوَٰرِثُونَ
- (23:69) [next to 23:71] أَمْ لَمْ يَعْرِفُوا۟ رَسُولَهُمْ فَهُمْ لَهُۥ مُنكِرُونَ
- (23:70) [next to 23:71] أَمْ يَقُولُونَ بِهِۦ جِنَّةٌۢ ۚ بَلْ جَآءَهُم بِٱلْحَقِّ وَأَكْثَرُهُمْ لِلْحَقِّ كَٰرِهُونَ
- (23:74) [next to 23:72] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- (23:75) [next to 23:73] ۞ وَلَوْ رَحِمْنَٰهُمْ وَكَشَفْنَا مَا بِهِم مِّن ضُرٍّۢ لَّلَجُّوا۟ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (28:20) [next to 28:22] وَجَآءَ رَجُلٌۭ مِّنْ أَقْصَا ٱلْمَدِينَةِ يَسْعَىٰ قَالَ يَٰمُوسَىٰٓ إِنَّ ٱلْمَلَأَ يَأْتَمِرُونَ بِكَ لِيَقْتُلُوكَ فَٱخْرُجْ إِنِّى لَكَ مِنَ ٱلنَّٰصِحِينَ
- (28:21) [next to 28:22] فَخَرَجَ مِنْهَا خَآئِفًۭا يَتَرَقَّبُ ۖ قَالَ رَبِّ نَجِّنِى مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (28:24) [next to 28:22] فَسَقَىٰ لَهُمَا ثُمَّ تَوَلَّىٰٓ إِلَى ٱلظِّلِّ فَقَالَ رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ
- (28:25) [next to 28:23] فَجَآءَتْهُ إِحْدَىٰهُمَا تَمْشِى عَلَى ٱسْتِحْيَآءٍۢ قَالَتْ إِنَّ أَبِى يَدْعُوكَ لِيَجْزِيَكَ أَجْرَ مَا سَقَيْتَ لَنَا ۚ فَلَمَّا جَآءَهُۥ وَقَصَّ عَلَيْهِ ٱلْقَصَصَ قَالَ لَا تَخَفْ ۖ نَجَوْتَ مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (28:26) [next to 28:27] قَالَتْ إِحْدَىٰهُمَا يَٰٓأَبَتِ ٱسْتَـْٔجِرْهُ ۖ إِنَّ خَيْرَ مَنِ ٱسْتَـْٔجَرْتَ ٱلْقَوِىُّ ٱلْأَمِينُ
- (28:28) [next to 28:27] قَالَ ذَٰلِكَ بَيْنِى وَبَيْنَكَ ۖ أَيَّمَا ٱلْأَجَلَيْنِ قَضَيْتُ فَلَا عُدْوَٰنَ عَلَىَّ ۖ وَٱللَّهُ عَلَىٰ مَا نَقُولُ وَكِيلٌۭ
- (28:29) [next to 28:27] ۞ فَلَمَّا قَضَىٰ مُوسَى ٱلْأَجَلَ وَسَارَ بِأَهْلِهِۦٓ ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا قَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ
- (32:25) [next to 32:27] إِنَّ رَبَّكَ هُوَ يَفْصِلُ بَيْنَهُمْ يَوْمَ ٱلْقِيَٰمَةِ فِيمَا كَانُوا۟ فِيهِ يَخْتَلِفُونَ
- (32:26) [next to 32:27] أَوَلَمْ يَهْدِ لَهُمْ كَمْ أَهْلَكْنَا مِن قَبْلِهِم مِّنَ ٱلْقُرُونِ يَمْشُونَ فِى مَسَٰكِنِهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍ ۖ أَفَلَا يَسْمَعُونَ
- (32:28) [next to 32:27] وَيَقُولُونَ مَتَىٰ هَٰذَا ٱلْفَتْحُ إِن كُنتُمْ صَٰدِقِينَ
- (32:29) [next to 32:27] قُلْ يَوْمَ ٱلْفَتْحِ لَا يَنفَعُ ٱلَّذِينَ كَفَرُوٓا۟ إِيمَٰنُهُمْ وَلَا هُمْ يُنظَرُونَ
- (43:7) [next to 43:9] وَمَا يَأْتِيهِم مِّن نَّبِىٍّ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (43:8) [next to 43:9] فَأَهْلَكْنَآ أَشَدَّ مِنْهُم بَطْشًۭا وَمَضَىٰ مَثَلُ ٱلْأَوَّلِينَ
- (43:12) [next to 43:10] وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا وَجَعَلَ لَكُم مِّنَ ٱلْفُلْكِ وَٱلْأَنْعَٰمِ مَا تَرْكَبُونَ
- (43:13) [next to 43:11] لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
- (50:1) [next to 50:3] قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ
- (50:2) [next to 50:3] بَلْ عَجِبُوٓا۟ أَن جَآءَهُم مُّنذِرٌۭ مِّنْهُمْ فَقَالَ ٱلْكَٰفِرُونَ هَٰذَا شَىْءٌ عَجِيبٌ
- (50:4) [next to 50:3] قَدْ عَلِمْنَا مَا تَنقُصُ ٱلْأَرْضُ مِنْهُمْ ۖ وَعِندَنَا كِتَٰبٌ حَفِيظٌۢ
- (50:5) [next to 50:3] بَلْ كَذَّبُوا۟ بِٱلْحَقِّ لَمَّا جَآءَهُمْ فَهُمْ فِىٓ أَمْرٍۢ مَّرِيجٍ
- (50:12) [next to 50:11] كَذَّبَتْ قَبْلَهُمْ قَوْمُ نُوحٍۢ وَأَصْحَٰبُ ٱلرَّسِّ وَثَمُودُ
- (50:13) [next to 50:11] وَعَادٌۭ وَفِرْعَوْنُ وَإِخْوَٰنُ لُوطٍۢ
- (71:15) [next to 71:17] أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا
- (71:16) [next to 71:17] وَجَعَلَ ٱلْقَمَرَ فِيهِنَّ نُورًۭا وَجَعَلَ ٱلشَّمْسَ سِرَاجًۭا
- (71:19) [next to 71:17] وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا
- (71:20) [next to 71:18] لِّتَسْلُكُوا۟ مِنْهَا سُبُلًۭا فِجَاجًۭا
- (79:25) [next to 79:27] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- (79:26) [next to 79:27] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (79:30) [next to 79:28] وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ
- (79:32) [next to 79:31] وَٱلْجِبَالَ أَرْسَىٰهَا
- (79:35) [next to 79:33] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (79:36) [next to 79:34] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ

