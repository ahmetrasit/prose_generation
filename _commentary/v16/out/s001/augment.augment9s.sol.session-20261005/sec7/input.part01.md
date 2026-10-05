Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 7 of 14 ("Ad, damga ve nişan: bir şeyin tanınması için yükseltilen ya da yakılan iz"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 7 (prose paragraphs numbered) =====
[¶37] Sure bir adla açılır: {ar:بِسْمِ ٱللَّهِ, tr:bismillâh, gloss:Allah'ın adıyla, source:1:1}. Arapçada ad, adlandırılan şeyin tanınması için yükseltilmiş bir şeydir: {ar:الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى, tr:el-ismü müştakkun mine's-sümüvvi ve hüve'r-rif'a, gloss:isim, yükseklik anlamındaki sümüvvden türer; anlama işaret etsin diye yükseltilmiştir, source:"س م و,B005"}. Başka bir tanım bunu daha açık söyler: {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismü mâ yu'rafü bihî zâtü'ş-şey', gloss:isim, bir şeyin kendisinin onunla tanındığı şeydir; aslı sumüvdür ve onunla adlandırılanın anılışı yükseltilir, source:"س م و,B005"}. Kökün temel anlamı yüksekliktir: {ar:السمو الارتفاع والعلو, tr:es-sümüvvü'l-irtifâu ve'l-ulüvv, gloss:sümüvv, yükselmek ve yüce olmaktır, source:"س م و,B001"}. İşleyişi şöyle tarif edilir: {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hattâ'stesbettüh, gloss:bir karaltı önümde yükseldi, sonunda onu iyice seçip tanıdım, source:"س م و,B002"}. Ad, ufukta yükselen bir şekil gibidir. Yükseldikçe tanınır hale gelir. İyi bir ad insanlar arasında dolaşır: {ar:ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر, tr:zehebe sîtühû fi'n-nâsi ve semâh, gloss:ünü ve adı insanlar arasında yayıldı, yani iyilikle anılması, kötülükle değil, source:"س م و,B008"}. Kelimenin kökü için anılan ikinci bir açıklama, onu yükseklikten değil, dağlama izinden türetir: {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmü eseru keyy, ve ba'îrun mevsûm, gloss:vesm, dağlama izidir; mevsûm deve, kulak kesiği ya da dağlama gibi tanınacağı bir işaretle damgalanmış devedir, source:"و س م,B001"}. İki açıklama da aynı işlemi anlatır: Ad, bir şeyin tanınması için onun üstüne konan izdir. Bu iz ya yukarıya yükseltilir ya da derinin içine yakılır. İzi okumak da aynı ailedendir: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtü fîhi'l-hayra ve'ş-şerr, gloss:onda hayrı ya da şerri sezdim, yani onda bir iz gördüm, source:"و س م,B002"}.

[¶38] İkinci ayetteki "âlemîn" aynı işlemi bütün yaratılışa yayar. Kökün aslı, bir şeyi başkalarından ayıran izdir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedüllü alâ eserin bi'ş-şey'i yetemeyyezü bihî an gayrih, gloss:bir şeyi başkasından ayıran bir ize işaret eden tek ve sağlam bir köktür, source:"ع ل م,B002"}. Sancak da bu köktendir: {ar:العلم الراية والجمع أعلام, tr:el-alemü'r-râye, gloss:alem sancaktır, çoğulu a'lâmdır, source:"ع ل م,B002"}. Savaşta süvarinin taşıdığı nişan da öyledir: {ar:أعلم الفارس إذا كانت له علامة في الحرب, tr:a'leme'l-fâris, gloss:süvari, savaşta kendine bir nişan taktı, source:"ع ل م,B002"}. Âlem de aslında bir nişandır: {ar:العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به, tr:el-âlemü ismün li'l-feleki ve mâ yahvîh, ve hüve fi'l-asli ismün li-mâ yu'lemü bih, gloss:âlem, gök küresine ve içindekilere verilen addır; aslında bir şeyin onunla bilindiği şeyin adıdır, source:"ع ل م,B003"}. Her canlı türü de kendi başına bir nişandır: {ar:العالمون كل جنس من الخلق فهو في نفسه معلم وعلم, tr:el-âlemûne küllü cinsin mine'l-halk, gloss:âlemler, yaratılmışların her bir türüdür; her biri kendi başına bir işaret ve bir nişandır, source:"ع ل م,B003"}. Nişanın varlık sebebi bilmektir: {ar:علمت الشيء عرفته, tr:alimtü'ş-şey'e araftüh, gloss:şeyi bildim, tanıdım, source:"ع ل م,B001"}.

[¶39] Bu iki ayet yan yana okunduğunda görüntü belirginleşir. Birinci ayet, tanımanın yükseltilmiş işaretiyle, yani bir adla başlar. İkinci ayet bütün yaratılışı Rabbin işaretleri olarak sayar. Sure, bir şeyin kendisiyle değil, onu tanıtan izle başlar. İz yükseltilmiş bir ad da olabilir, bir sancak da, bütün bir canlı türü de. Birinci ayette anılan ad, en büyük ad olarak gösterilir: {ar:اسم الله الأكبر هو الله, tr:ismullâhi'l-ekberu hüvallâh, gloss:Allah'ın en büyük adı "Allah"tır, source:"ء ل ه,B002"}. Bu ad çağrıda söylenir: {ar:يا ألله اغفر لي, tr:yâ allâhü'ğfir lî, gloss:ey Allah, beni bağışla, source:"ء ل ه,B002"}. Düz bir meal "Allah'ın adıyla" der. Görüntü ise adın neden bir başlangıç olduğunu gösterir: Ad, adlandırılanı bilinir kılan yükseltilmiş işarettir. Bir işe onunla başlamak, o işi bu tanınmış işaretin altına koymaktır.

[¶40] Kur'an'da ad ile yükseklik, ad ile kulluk ve ad ile bilgi bir arada anılır. Biri şöyle der: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihisme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Ad, Rab ve yükseklik bu cümlede bir aradadır. Bir başka yerde ad yüceltilir: {ar:تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ, tr:tebârakesmü rabbike zi'l-celâli ve'l-ikrâm, gloss:celal ve ikram sahibi Rabbinin adı ne yücedir, source:55:78}. Okumak da adla başlar: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bismi rabbikellezî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. "Biz ancak Rabbinin emriyle ineriz" diyenlerin sözü {source:19:64}, kulluk ile adaşı aynı cümleye koyan ayete varır: {ar:فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:fa'büdhü vastabir li-ibâdetih, hel ta'lemü lehû semiyyâ, gloss:O'na kulluk et ve kulluğunda sabırlı ol; O'nun adını taşıyabilecek bir dengini biliyor musun, source:19:65}. "Semiyy" kelimesi şöyle açıklanır: {ar:سميا أي نظيرا له يستحق اسمه, tr:semiyyen, ey nazîran lehû yestehıkku ismeh, gloss:semiyy, onun adını hak edecek bir dengidir, source:"س م و,B005"}. Kulluk, bilmek ve ad bu tek ayette bir araya gelir. Allah'ın adları ile çağrı da birlikte anılır: {ar:قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ, tr:kuli'd'ullâhe evi'd'u'r-rahmân, eyyen mâ ted'û fe-lehü'l-esmâü'l-hüsnâ, gloss:de ki: Allah diye çağırın ya da Rahman diye çağırın; hangisiyle çağırırsanız çağırın, en güzel adlar O'nundur, source:17:110}. Surenin birinci ayetindeki iki ad burada yan yanadır. Rahman adını reddedenler de bir ad üzerinden konuşur: {ar:قَالُوا۟ وَمَا ٱلرَّحْمَٰنُ, tr:kâlû ve me'r-rahmân, gloss:Rahman da nedir, dediler, source:25:60}. Yusuf zindandaki arkadaşlarına sahibi olmayan adları gösterir: {ar:مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم, tr:mâ ta'büdûne min dûnihî illâ esmâen semmeytümûhâ entüm ve âbâüküm, gloss:O'nu bırakıp kulluk ettikleriniz, sizin ve atalarınızın taktığı adlardan başka bir şey değildir, source:12:40}. Bu adlar yükseltilmiş, ama altında tanıtacakları bir şey olmayan işaretlerdir.

[¶41] Surenin birinci ayeti Kur'an'da bir mektubun başında da görülür. Kadın hükümdar, kendisine "değerli bir mektup" bırakıldığını söyler {source:27:29} ve mektubu tanıtır: {ar:إِنَّهُۥ مِن سُلَيْمَٰنَ وَإِنَّهُۥ بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:innehû min Süleymâne ve innehû bismillâhi'r-rahmâni'r-rahîm, gloss:o, Süleyman'dandır ve Rahman ve Rahim olan Allah'ın adıyladır, source:27:30}. Ad burada yazının başına konmuş, mektubun kimden geldiğini ve kimin adına konuştuğunu bildiren bir işarettir. Nuh, gemiye binenlere adı geminin yürüyüşünün ve duruşunun üstüne koyarak seslenir: {ar:ٱرْكَبُوا۟ فِيهَا بِسْمِ ٱللَّهِ مَجْر۪ىٰهَا وَمُرْسَىٰهَآ, tr:irkebû fîhâ bismillâhi mecrâhâ ve mürsâhâ, gloss:binin ona; onun yürümesi de durması da Allah'ın adıyladır, source:11:41}. Adlar Âdem'e öğretilmiştir: {ar:وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا, tr:ve alleme Âdeme'l-esmâe küllehâ, gloss:Âdem'e adların hepsini öğretti, source:2:31}. Ad ile bilgi kökü burada aynı cümlededir. Damganın izi de Kur'an'da okunur. Lut'un şehri altüst edildikten sonra {source:15:74} şöyle denir: {ar:إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْمُتَوَسِّمِينَ, tr:inne fî zâlike le-âyâtin li'l-mütevessimîn, gloss:bunda izleri okuyabilenler için ayetler vardır, source:15:75}. Damganın kendisi de anılır: {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimuhû ale'l-hurtûm, gloss:onun burnuna damga vuracağız, source:68:16}.

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: و ل ه members of ٱللَّهِ (road, womb, herd, well, passing) - alternative derivation, root identity not established
- not developed: hadith items in womb, herd and leaning chains - outside the Quran
- not developed: ن ع م B012 walking on soles - too remote
- not developed: ع و ن B005 strength matching age - adds nothing
- not developed: ق و م B012 ayn reading of qāma - recorded as wrong
- not developed: Debt and scale chain - merged into Day of reckoning
- not developed: Well-head chain - merged into Rain as water
- memory: dīn (kasra) vs dayn (fatha) are distinct words of one root
- memory: maghḍūb is a passive participle naming no agent; anʿamta names "you" as agent
- memory: fronted iyyāka marks exclusivity ("only you")
- memory: qāma also means "stopped dead" (beast), as well as "stood up"

===== passages from the discovery list (239) =====
## strong (120)

- (2:31) [luna: strong; terra: strong; basis: root+theme] [cited in ¶41] وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَٰٓؤُلَآءِ إِن كُنتُمْ صَٰدِقِينَ
  Unverified discovery rationale: luna: The source-section says a name is what makes a thing known; Allah teaches Adam الْأَسْمَاءَ كُلَّهَا. | terra: God teaches Adam all the names, joining الاسم to عَلَّم: naming is knowledge, exactly as the section says a name is what makes a thing knowable.
- (2:33) [luna: strong; terra: strong; basis: neighbour+root+theme] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
  Unverified discovery rationale: luna: This neighbor completes the naming scene: Adam is told to inform the angels of the names, making the taught names usable for recognition. | terra: Adam informs the angels of the names, completing 2:31: the taught names are publicly articulated so the things can be identified, and God contrasts this with the angels' limited knowledge.
- (2:158) [luna: strong; terra: medium; basis: root+scene+theme] ۞ إِنَّ ٱلصَّفَا وَٱلْمَرْوَةَ مِن شَعَآئِرِ ٱللَّهِ ۖ فَمَنْ حَجَّ ٱلْبَيْتَ أَوِ ٱعْتَمَرَ فَلَا جُنَاحَ عَلَيْهِ أَن يَطَّوَّفَ بِهِمَا ۚ وَمَن تَطَوَّعَ خَيْرًۭا فَإِنَّ ٱللَّهَ شَاكِرٌ عَلِيمٌ
  Unverified discovery rationale: luna: The source-section dictionary form ع ل م is a distinguishing sign; Safa and Marwa are named as مِن شَعَائِرِ اللَّهِ, visible ritual markers traversed in pilgrimage. | terra: Safa and Marwah are among God's شعائر, public sacred symbols. Their named, visible locations show how a place can function as a sign within worship.
- (2:164) [luna: strong; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The section calls creation a field of signs that can be known; this verse names the heavens, earth, rain, winds, ships, and clouds as آيَات for people who reason.
- (2:189) [luna: strong; basis: root+theme] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ ۗ وَلَيْسَ ٱلْبِرُّ بِأَن تَأْتُوا۟ ٱلْبُيُوتَ مِن ظُهُورِهَا وَلَٰكِنَّ ٱلْبِرَّ مَنِ ٱتَّقَىٰ ۗ وَأْتُوا۟ ٱلْبُيُوتَ مِنْ أَبْوَٰبِهَا ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: The section says a sign enables recognition; the new moons are appointed marks of time for people and pilgrimage.
- (2:248) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ءَايَةَ مُلْكِهِۦٓ أَن يَأْتِيَكُمُ ٱلتَّابُوتُ فِيهِ سَكِينَةٌۭ مِّن رَّبِّكُمْ وَبَقِيَّةٌۭ مِّمَّا تَرَكَ ءَالُ مُوسَىٰ وَءَالُ هَٰرُونَ تَحْمِلُهُ ٱلْمَلَٰٓئِكَةُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: luna: The source-section defines a sign as a mark by which something is known; the chest bearing relics is called آيَةَ مُلْكِهِ, the identifying sign of Saul's kingship. | terra: The return of the Ark is specified as the sign of Saul's kingship. A concrete object functions as the public mark by which an otherwise disputed claim is recognized.
- (2:273) [luna: strong; terra: strong; basis: root+scene+theme] لِلْفُقَرَآءِ ٱلَّذِينَ أُحْصِرُوا۟ فِى سَبِيلِ ٱللَّهِ لَا يَسْتَطِيعُونَ ضَرْبًۭا فِى ٱلْأَرْضِ يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ مِنَ ٱلتَّعَفُّفِ تَعْرِفُهُم بِسِيمَٰهُمْ لَا يَسْـَٔلُونَ ٱلنَّاسَ إِلْحَافًۭا ۗ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌ
  Unverified discovery rationale: luna: The source-section image is a mark by which a person is known; this verse says the needy are recognized by their سِيمَاهُم. | terra: The needy are known by their سِيمَا although they do not beg insistently; this gives the section's readable mark a quiet social form rather than a literal burn.
- (3:36) [luna: strong; basis: root+theme] فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ وَٱللَّهُ أَعْلَمُ بِمَا وَضَعَتْ وَلَيْسَ ٱلذَّكَرُ كَٱلْأُنثَىٰ ۖ وَإِنِّى سَمَّيْتُهَا مَرْيَمَ وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ
  Unverified discovery rationale: luna: The source-section defines a name as what identifies a person; Mary's mother says سَمَّيْتُهَا مَرْيَمَ, I have named her Mary.
- (3:45) [luna: strong; terra: medium; basis: root+scene+theme] إِذْ قَالَتِ ٱلْمَلَٰٓئِكَةُ يَٰمَرْيَمُ إِنَّ ٱللَّهَ يُبَشِّرُكِ بِكَلِمَةٍۢ مِّنْهُ ٱسْمُهُ ٱلْمَسِيحُ عِيسَى ٱبْنُ مَرْيَمَ وَجِيهًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَمِنَ ٱلْمُقَرَّبِينَ
  Unverified discovery rationale: luna: The source-section says the name raises and identifies the named; this verse names the Messiah, Jesus son of Mary, then calls him وَجِيهًا in this life and the next. | terra: The angels announce a word from God whose name is the Messiah, Jesus son of Mary. The stated name and title distinguish the announced person before his appearance.
- (3:125) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] بَلَىٰٓ ۚ إِن تَصْبِرُوا۟ وَتَتَّقُوا۟ وَيَأْتُوكُم مِّن فَوْرِهِمْ هَٰذَا يُمْدِدْكُمْ رَبُّكُم بِخَمْسَةِ ءَالَٰفٍۢ مِّنَ ٱلْمَلَٰٓئِكَةِ مُسَوِّمِينَ
  Unverified discovery rationale: luna: The source-section dictionary describes a rider with a mark in battle; here the angelic reinforcements are marked, مُسَوِّمِينَ, in a battle scene. | terra: The promised angels are مُسَوِّمِينَ, marked or bearing distinguishing marks in battle; it realizes the section's dictionary image of a rider's battle badge.
- (3:190) [luna: strong; terra: strong; basis: contrast+scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: The section treats creation as marks that disclose their maker; this verse calls the creation of heavens and earth and the night-day alternation signs for people of understanding. | terra: The creation of the heavens and earth and the alternation of night and day are signs for people of understanding; the world is explicitly presented as discernible indication.
- (3:191) [luna: strong; terra: medium; basis: neighbour+theme] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: luna: The section links signs with knowing and invoking the named Lord; these readers remember Allah and call him رَبَّنَا after reflecting on creation. | terra: Those who remember God read heaven and earth's creation as not purposeless. It gives the responsive act of understanding that completes the signs named in 3:190.
- (5:4) [luna: strong; terra: medium; basis: root+speaker+theme] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: The source-section says a name marks the beginning of an act; trained hunting animals are sent with Allah's name mentioned over the catch. | terra: The hunter is told to mention God's name over what trained animals catch. An ordinary act is made answerable to the name, extending the beginning-under-the-name pattern.
