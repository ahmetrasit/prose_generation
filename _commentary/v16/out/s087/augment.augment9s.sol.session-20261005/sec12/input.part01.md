Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 12 of 18 ("Toplanan, tutulan, düşürülen: okuma, unutma ve sayfalar"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.

===== _commentary/v16/prompts/augment9s/augment.md =====
You are completing a finished Turkish commentary on the images of a surah,
written by another reader, with what the Quran itself says about it: the Quran
explaining the Quran. Below are one image section of that commentary, with its
prose paragraphs numbered [¶n] as in the whole commentary; the commentary's
ledger; and Quran passages from an image-based discovery list (two readers'
judgements of which ayat this image activates), each with its Arabic, its tier,
the bases given for it, and the paragraphs of the section that already cite it,
if any. A tier is that list's own judgement, not yours; the list is not
authoritative and may be incomplete.

Read the section first. Then judge every listed passage, one by one, against
every paragraph of the section: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the ayat the paragraph reads leave
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

Then go through the section paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; the other places where the image's scene,
object or act is staged, with or without a shared word; ayat that state the same thing in other
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
passage from your own knowledge that you weighed, marked "own". Paragraph
numbers are the ones shown: only this section's paragraphs may be served.
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 12 (prose paragraphs numbered) =====
[¶46] Altıncı ayet {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız da unutmayacaksın, source:87:6} der. Yedinci ayet buna bir istisna ekler: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği hariç, source:87:7}. Kelimelerin aileleri hafızayı bir kaplar dizisi olarak gösterir. قرأ toplamaktır: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:karaeu'ş-şey'e kur'ânen ceme'tuhû ve damamtu ba'dahû ilâ ba'd, gloss:bir şeyi okudum yani onu toplayıp parçalarını birbirine kattım, source:"ق ر ء,B001"}. Okuma harfleri ve kelimeleri birbirine eklemektir: {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل, tr:el-kırâe dammu'l-hurûfi ve'l-kelimâti ba'dihâ ilâ ba'din fi't-tertîl, gloss:okuma harfleri ve kelimeleri tertil içinde birbirine eklemektir, source:"ق ر ء,B001"}. Ayetteki fiil başkasına bu toplamayı vermektir: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu ğayrî ukriuhû ikrâen, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Unutmak ise emanet edilmiş bir şeyi tutamamaktır: {ar:ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد, tr:terku'l-insâni dabta mâ'stûdia immâ li-da'fi kalbihî ve immâ an ğafletin ve immâ an kasd, gloss:insanın kendisine emanet edileni tutmayı bırakmasıdır; ya kalbinin zayıflığından ya gaflettendir ya da kasıtla, source:"ن س ي,B001"}. {ar:النسيان خلاف الذكر والحفظ, tr:en-nisyân hilâfu'ẕ-ẕikri ve'l-hıfz, gloss:unutmak anmanın ve korumanın zıddıdır, source:"ن س ي,B001"}. Unutmak bırakmak da demektir: {ar:النسيان الترك، نسوا الله فنسيهم, tr:en-nisyânu't-terk nesullâhe fe-nesiyehum, gloss:unutmak bırakmaktır; Allah'ı unuttular o da onları unuttu, source:"ن س ي,B002"}. Ve göç edenlerin geride bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sekata min menâzili'l-murtehilîne min ruẕâli emtiatihim, gloss:nisy göç edenlerin konak yerlerinden düşen değersiz eşyadır, source:"ن س ي,B003"}.

[¶47] Dokuzuncu, onuncu ve on beşinci ayetlerdeki ذكر kökü bu düşüşün karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi andım unuttumun zıddıdır, source:"ذ ك ر,B003"}. {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey'i ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; o benim aklımdadır, source:"ذ ك ر,B003"}. {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür kaçanı aramaktır, source:"ذ ك ر,B003"}. Öğüt bir şeyi akla getiren araçtır: {ar:التذكرة ما تستذكر به الحاجة, tr:et-teẕkira mâ tusteẕkeru bihi'l-hâce, gloss:teẕkira bir ihtiyacın hatırlandığı şeydir, source:"ذ ك ر,B009"}. Bir peygamberin kitabının adı da aynı köktendir: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîn ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntılarını içeren kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Bu anlam dokuzuncu ayetteki öğüdü on sekizinci ve on dokuzuncu ayetlerdeki sayfalara bağlar. Sayfalar, üzerine yazı yazılan deri parçalarıdır: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıtatu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhuf sahîfenin çoğuludur; sahîfe üzerine yazılan ak deri ya da parşömen parçasıdır, source:"ص ح ف,B002"}. Mushaf bu sayfaları bir araya toplayandır: {ar:المصحف ما جعل جامعا للصحف المكتوبة, tr:el-mushaf mâ cuile câmian li's-suhufi'l-mektûbe, gloss:mushaf yazılı sayfaları toplamak için yapılmış şeydir, source:"ص ح ف,B003"}. "İlk" kelimesi bir şeyin başlangıcıdır: {ar:الأول وهو مبتدأ الشيء, tr:el-evvel ve huve mubtedeu'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"}. On altıncı ayetteki tercih fiilinin kökü de söz aktarmayı verir: {ar:أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور, tr:eŝertu'l-hadîŝe iẕâ ẕekertehû an ğayrike ve hadîŝun me'ŝûr, gloss:bir sözü başkasından naklettiğinde eŝertu denir; aktarılan söze me'ŝûr denir, source:"ء ث ر,B002"}.

[¶48] Bu aileler altıncı ayetle son ayet arasında bir yol çizer. Okutulan söz toplanır ve birbirine eklenir. Unutulmayınca tutulur. Unutulursa göç yerindeki döküntü gibi geride kalır. Anılarak geri çağrılır. Sonunda deriye yazılıp sayfa olur, sayfalar da bir arada toplanır. On sekizinci ayetteki {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâẕâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18} cümlesi, okutulan sözün yalnız Peygamber'in hafızasında değil, İbrahim'in ve Musa'nın sayfalarında da toplanmış olduğunu söyler. Düz bir anlatımda "unutmayacaksın" bir vaattir. Aile resmi ise bu vaadin işleyişini gösterir: toplayan Allah'tır, ve toplanan şey düşürülmez.

[¶49] Kur'an toplama ile okumayı aynı cümlede verir. Allah Peygamber'e vahyi acele ile tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle almak için dilini kıpırdatma, source:75:16}, {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak ve okutmak bize düşer, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe-iẕâ kara'nâhu fettebi' kur'ânah, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Başka bir yerde de {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:sana vahyi tamamlanmadan Kur'an'ı okumakta acele etme ve Rabbim ilmimi artır de, source:20:114} denir. Hemen ardından unutmanın ilk örneği gelir: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا, tr:ve lekad ahidnâ ilâ âdeme min kablu fe-nesiye ve lem necid lehû azmâ, gloss:andolsun daha önce Adem'e söz vermiştik; o unuttu ve onda bir kararlılık bulmadık, source:20:115}. Firavun Musa'ya {ar:فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:ya önceki nesillerin durumu ne olacak, source:20:51} diye sorduğunda Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Bu cevapta "ilk" kelimesi, yazılı kitap ve unutmayan Rab bir aradadır. Unutmanın karşılığı da aynı kelimeyle verilir: {ar:كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ, tr:keẕâlike etetke âyâtunâ fe-nesîtehâ ve keẕâlike'l-yevme tunsâ, gloss:ayetlerimiz sana geldi ama sen onları unuttun; bugün de sen öyle unutulursun, source:20:126}. Münafıklar için {ar:نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ, tr:nesullâhe fe-nesiyehum, gloss:Allah'ı unuttular o da onları unuttu, source:9:67} denir. Müminlere de {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ, tr:ve lâ tekûnû kelleẕîne nesullâhe fe-ensâhum enfusehum, gloss:Allah'ı unutan ve bu yüzden Allah'ın onlara kendilerini unutturduğu kimseler gibi olmayın, source:59:19} denir. Yedinci ayetteki istisnanın bir benzeri Peygamber'e verilen bir emirde de geçer: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh veẕkur rabbeke iẕâ nesît, gloss:ancak Allah dilerse; unuttuğunda Rabbini an, source:18:24}. Unutmaya karşı çare anmaktır.

[¶50] Sayfaların içeriği başka bir yerde kısmen verilir: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bi-mâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarındakiler ona haber verilmedi mi, source:53:36}, {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'lleẕî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in sayfalarındakiler, source:53:37}. Sayfalarda yazanların ilki şudur: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}. Ardından {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için kendi çabasından başkası yoktur, source:53:39} gelir, ve dizi şöyle biter: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Her kişinin kendi payını taşıması, bu surenin iki kişiye ayrılan ortasıyla aynı konudur. Delil isteyenlere de {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:ilk sayfalardakinin açık delili onlara gelmedi mi, source:20:133} denir. Başka bir yerde öğüt ve sayfa birlikte anılır: {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ teẕkira, gloss:hayır bu bir öğüttür, source:80:11}, {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe ẕekerah, gloss:dileyen onu anar, source:80:12}, {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhara, gloss:yükseltilmiş ve arınmış, source:80:14}. Sayfalar yükseltilmiş ve arınmıştır. Bu iki sıfat surenin birinci ayetindeki yüksekliği ve on dördüncü ayetindeki arınmayı sayfalara taşır. Kur'an kendisi için de {ar:وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ, tr:ve innehû le-fî zuburi'l-evvelîn, gloss:o öncekilerin kitaplarında da vardır, source:26:196} der.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (284) =====
## strong (149)

- (2:44) [luna: strong; terra: strong; basis: contrast+root+scene] ۞ أَتَأْمُرُونَ ٱلنَّاسَ بِٱلْبِرِّ وَتَنسَوْنَ أَنفُسَكُمْ وَأَنتُمْ تَتْلُونَ ٱلْكِتَٰبَ ۚ أَفَلَا تَعْقِلُونَ
  Unverified discovery rationale: luna: The section joins remembering with reciting and retaining scripture. This verse asks how people can command righteousness while forgetting themselves even as they recite the Book, bringing reading and failure to remember into one rebuke. | terra: The addressees recite the Book yet “forget yourselves”; the verse exposes a failure to retain and enact the very writing being read.
- (2:63) [terra: strong; basis: root+scene+theme] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: terra: Israel is told to hold firmly what was given and remember what is in it, directly pairing custody of an entrusted revelation with active remembrance.
- (2:97) [terra: strong; basis: scene+theme] قُلْ مَن كَانَ عَدُوًّۭا لِّجِبْرِيلَ فَإِنَّهُۥ نَزَّلَهُۥ عَلَىٰ قَلْبِكَ بِإِذْنِ ٱللَّهِ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ وَهُدًۭى وَبُشْرَىٰ لِلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: Gabriel brings the revelation onto the Prophet's heart by Allah's permission while confirming earlier revelation, joining inward retention to continuity across scriptures.
- (2:101) [terra: strong; basis: contrast+scene+theme] وَلَمَّا جَآءَهُمْ رَسُولٌۭ مِّنْ عِندِ ٱللَّهِ مُصَدِّقٌۭ لِّمَا مَعَهُمْ نَبَذَ فَرِيقٌۭ مِّنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ كِتَٰبَ ٱللَّهِ وَرَآءَ ظُهُورِهِمْ كَأَنَّهُمْ لَا يَعْلَمُونَ
  Unverified discovery rationale: terra: A party given the Book casts Allah's Book behind their backs, turning the section's figurative “dropped” word into an enacted rejection of written revelation.
- (2:106) [luna: strong; terra: contrast; basis: contrast+root+speaker+theme] ۞ مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ ۗ أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The section's 87:7 has an exception “except what Allah wills,” and its dictionary defines forgetting as no longer holding what was entrusted. This verse says Allah may cause a verse to be forgotten or replace it, making divine will govern what is retained; here the context is revelation being replaced. | terra: The divine prerogative to abrogate an ayah or cause it to be forgotten marks the explicit boundary around the promise of non-forgetting: any loss is under God's will and replacement.
- (2:121) [luna: strong; terra: medium (missing-ayat turn); basis: root+scene+theme] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَتْلُونَهُۥ حَقَّ تِلَاوَتِهِۦٓ أُو۟لَٰٓئِكَ يُؤْمِنُونَ بِهِۦ ۗ وَمَن يَكْفُرْ بِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
  Unverified discovery rationale: luna: The section's dictionary form قرأت الشيء defines reading as joining words together. This verse says the people given the Book recite it as it should be recited and believe in it, linking faithful reading with receiving scripture. | terra: Those given the Book recite it with its true recitation, presenting faithful reading as the proper handling of an entrusted scripture.
- (2:129) [luna: strong; terra: medium (missing-ayat turn); basis: root+scene+speaker+theme] رَبَّنَا وَٱبْعَثْ فِيهِمْ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِكَ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُزَكِّيهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The section connects the recited word and written scripture with purification. Abraham asks for a messenger who recites God's signs, teaches the Book and wisdom, and purifies the people, bringing those same acts together in one request. | terra: Abraham asks for a messenger who will recite God's signs and teach the Book, anticipating the movement from divinely supplied utterance to learned scripture.
- (2:151) [luna: strong (missing-ayat turn); terra: medium (missing-ayat turn); basis: root+scene+speaker+theme] كَمَآ أَرْسَلْنَا فِيكُمْ رَسُولًۭا مِّنكُمْ يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِنَا وَيُزَكِّيكُمْ وَيُعَلِّمُكُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
  Unverified discovery rationale: luna: This repeats the prophetic pattern of reciting God's signs, purifying the audience, and teaching the Book. Its own address says the Messenger also teaches what the people did not know, extending the section's meeting of recitation, purification, and scripture to its immediate audience. | terra: The sent messenger recites signs, purifies, and teaches the Book and wisdom, describing the public transmission that follows the Prophet's receipt of recitation.
- (2:282) [luna: strong; terra: medium; basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section links written pages with a تذكرة that brings a needed matter back to mind. In the debt-writing instructions, witnesses are chosen so that if one errs, “فَتُذَكِّرَ إِحْدَاهُمَا الْأُخْرَى”; writing and mutual reminding protect a detail from being lost. | terra: A second witness is to remind the first if she errs, a concrete legal use of تذكر as retrieving a detail that escaped memory.
- (2:283) [luna: strong (missing-ayat turn); basis: neighbour+scene+theme] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
