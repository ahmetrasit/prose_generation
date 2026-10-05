Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 16 of 18 ("Seçmek: seçkin ve döküntü"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 16 (prose paragraphs numbered) =====
[¶61] On altıncı ayet {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır; siz dünya hayatını tercih ediyorsunuz, source:87:16} der. On yedinci ayet buna şöyle karşılık verir: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Tercih fiili, bir şeyi kayırıp kendine ayırmaktır. Kayırılan kişi {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-eŝîr el-kerîmu aleyke'lleẕî tu'ŝiruhû bi-fadlike ve sıletik, gloss:esîr senin için değerli olandır; ona iyiliğinle ve bağışınla öncelik verirsin, source:"ء ث ر,B005"}. Başkasını kendine tercih etmek de bu köktendir: {ar:آثرت فلانا على نفسي من الإيثار, tr:âŝertu fulânen alâ nefsî mine'l-îŝâr, gloss:falancayı kendime tercih ettim, source:"ء ث ر,B005"}. Kendine ayırmak da: {ar:استأثر الله بالبقاء أي انفرد بالبقاء, tr:ista'ŝerallâhu bi'l-bekâi ey infarada bi'l-bekâ, gloss:Allah kalıcılığı kendine ayırdı yani kalıcılıkta tek kaldı, source:"ء ث ر,B006"}. Bu ifade on altıncı ayetin fiilini on yedinci ayetin kalıcılığına bağlar. Seçmek daha iyiyi aramaktır: {ar:الاختيار طلب ما هو خير وفعله, tr:el-ihtiyâru talebu mâ huve hayrun ve fi'luh, gloss:seçmek daha hayırlı olanı arayıp yapmaktır, source:"خ ي ر,B003"}. Seçilmiş olan döküntü içermez: {ar:فيهن مختارات لا رذل فيهن, tr:fîhinne muhtârâtun lâ reẕle fîhinn, gloss:onların arasında seçkinler var; aralarında döküntü yok, source:"خ ي ر,B002"}. Mal ancak bol ve temiz kaynaklı olunca hayır diye anılmayı hak eder: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne keŝîran ve min mekânin tayyib, gloss:mal bol olmadıkça ve temiz bir yerden gelmedikçe ona hayır denmez, source:"خ ي ر,B004"}.

[¶62] Öbür kefede dünya kelimesinin kökünden gelen aşağılık vardır: {ar:خص الدنيء بالحقير القدر, tr:hussa'd-denîu bi'l-hakîri'l-kadr, gloss:denî değeri düşük olana özgü kılınmıştır, source:"د ن و,B003"}. {ar:الأدنى عن الأرذل, tr:el-ednâ ani'l-erẕel, gloss:ednâ en aşağılık olanı anlatır, source:"د ن و,B003"}. "Değer" diye çevrilen kelime üçüncü ayetteki ölçmek fiilinin köküdür. Beşinci ayetin döküntüsü insanlar için de kullanılır: {ar:يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه, tr:yukâlu li-sefeleti'n-nâsi'l-ğuŝâ teşbîhen bi'lleẕî ẕekernâh, gloss:insanların aşağısına da ona benzetilerek ğuŝâ denir, source:"غ ث و,B004"}. Göç yerinde düşürülen değersiz eşya da bu kefededir. Kalan şey ise hâlâ iyilik taşır: {ar:أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير, tr:ulû bakıyyetin min dînin kavmun lehum bakıyyetun iẕâ kânet bihim misketun ve fîhim hayr, gloss:dinden bir bakıyye sahipleri; tutunacak bir şeyleri ve içlerinde iyilik bulunan topluluk, source:"ب ق ي,B002"}.

[¶63] Bu ayrım surenin önceki imgelerini bir seçim olarak toplar. Beşinci ayetteki çerçöp, altıncı ayetteki unutulan döküntü ve on altıncı ayetteki aşağı olan bir kefededir. On yedinci ayetteki hayırlı ve kalıcı olan, seçilmiş ve döküntüsüz olan öbür kefededir. Düz bir anlatım "dünya" ile "ahiret" arasında bir tercih görür. Kök aileleri bu tercihin bir ayıklama olduğunu duyurur: seçkin olan alınır, döküntü bırakılır. Kınanan şey ise döküntüyü seçmektir.

[¶64] Kur'an bu seçimi açıkça sahneler. Firavun'un en yüce rab olma iddiasının anlatıldığı surede hüküm şudur: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:artık barınağı cehennemdir, source:79:39}. Karşı tarafta {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve nehe'n-nefse ani'l-hevâ, gloss:Rabbinin huzuruna çıkmaktan korkan ve nefsini hevesten alıkoyana gelince, source:79:40} vardır. Musa'nın karşısındaki sihirbazlar bu seçimi tehdit altında yapar: {ar:لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:len nu'ŝirake alâ mâ câenâ mine'l-beyyinâti velleẕî fataranâ fakdı mâ ente kâd innemâ takdî hâẕihi'l-hayâte'd-dunyâ, gloss:bize gelen açık delillere ve bizi yaratana seni asla tercih etmeyiz; vereceğin hükmü ver; sen ancak bu dünya hayatında hüküm verebilirsin, source:20:72}. Sözlerini şöyle bitirirler: {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73}. Bu iki ayette surenin on altıncı ve on yedinci ayetlerinin dört kelimesi bulunur. Peygamber'e de {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temuddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhum zehrate'l-hayâti'd-dunyâ, gloss:onlardan bazılarına verdiğimiz dünya hayatının çiçeğine gözünü dikme, source:20:131} denir. Ayet {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike hayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131} diye biter. Dünya hayatı burada bir çiçektir. Otlağın imgesi seçimin tam içindedir. Aynı karşıtlık başka yerlerde de geçer: {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ, tr:ve mâ indallâhi hayrun ve ebkâ e-fe-lâ ta'kılûn, gloss:Allah katında olan daha hayırlı ve daha kalıcıdır; akıl etmez misiniz, source:28:60}, {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟, tr:ve mâ indallâhi hayrun ve ebkâ li'lleẕîne âmenû, gloss:Allah katında olan iman edenler için daha hayırlı ve daha kalıcıdır, source:42:36}, {ar:مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ, tr:mâ indekum yenfedu ve mâ indallâhi bâk, gloss:sizin yanınızdaki tükenir; Allah'ın katındaki ise kalır, source:16:96}. Kalıcılık kötü yönde de geçer: {ar:وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ, tr:ve le-azâbu'l-âhirati eşeddu ve ebkâ, gloss:ahiret azabı ise elbette daha çetin ve daha kalıcıdır, source:20:127}. Tercih fiili Kur'an'da iyi yönde de kullanılır. Yusuf'un kardeşleri onu tanıdıklarında {ar:تَٱللَّهِ لَقَدْ ءَاثَرَكَ ٱللَّهُ عَلَيْنَا, tr:tallâhi lekad âŝerakallâhu aleynâ, gloss:Allah'a andolsun ki Allah seni bize üstün kıldı, source:12:91} derler. Hicret edenleri barındıranlar için de {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ, tr:ve yu'ŝirûne alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri ihtiyaç içinde olsalar bile onları kendilerine tercih ederler, source:59:9} denir. Bu ayet {ar:فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:fe-ulâike humu'l-muflihûn, gloss:işte kurtuluşa erenler onlardır, source:59:9} diye biter. Burada tercih ile kurtuluş, yani surenin on altıncı ve on dördüncü ayetlerinin fiilleri, doğru yönde birleşir. Kalanlar da şöyle anılır: {ar:فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ, tr:fe-lev lâ kâne mine'l-kurûni min kablikum ulû bakıyyetin yenhevne ani'l-fesâdi fi'l-ard, gloss:sizden önceki nesiller arasında yeryüzünde bozgunculuğu önleyecek bir kalıntı sahibi olsaydı ya, source:11:116}.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (294) =====
## strong (193)

- (2:61) [terra: strong; basis: root+scene+theme] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
  Unverified discovery rationale: terra: Israel's exchange asks, أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ, staging the section's condemned choice of the lower for the better.
- (2:86) [luna: strong; terra: strong; basis: contrast+scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: luna: The ayah condemns those who bought the life of this world at the price of the Hereafter, a concrete exchange of the better enduring outcome for the nearer one. | terra: Those who bought worldly life at the price of the hereafter turn preference into an exchange whose consequence cannot be reduced or relieved.
- (2:96) [terra: strong (missing-ayat turn); basis: theme] وَلَتَجِدَنَّهُمْ أَحْرَصَ ٱلنَّاسِ عَلَىٰ حَيَوٰةٍۢ وَمِنَ ٱلَّذِينَ أَشْرَكُوا۟ ۚ يَوَدُّ أَحَدُهُمْ لَوْ يُعَمَّرُ أَلْفَ سَنَةٍۢ وَمَا هُوَ بِمُزَحْزِحِهِۦ مِنَ ٱلْعَذَابِ أَن يُعَمَّرَ ۗ وَٱللَّهُ بَصِيرٌۢ بِمَا يَعْمَلُونَ
  Unverified discovery rationale: terra: A life of a thousand years would still not remove the covetous person from punishment, exposing mere longevity as counterfeit permanence.
- (2:110) [terra: strong (missing-ayat turn); basis: root+theme] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ ۗ إِنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: terra: Whatever good people send ahead for themselves will be found with God, so present goods are retained by being transferred toward Him.
- (2:177) [luna: strong (missing-ayat turn); terra: medium (missing-ayat turn); basis: contrast+scene+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The ayah defines righteousness partly as giving wealth, despite love of it, to relatives, orphans, the needy, and others; this is a specific choice to direct possessions away from self. | terra: Giving cherished wealth to relatives, orphans, needy people, travelers, petitioners, and captives concretely enacts preferring needy others over possession.
- (2:200) [luna: strong; terra: strong; basis: contrast+scene+theme] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: luna: Some ask only for good in worldly life and have no share in the Hereafter; this is the section’s condemned narrowing of what counts as a desirable outcome. | terra: The person whose prayer asks only for this world is said to have no share in the hereafter, one side of a paired choice.
- (2:201) [luna: strong; terra: strong; basis: contrast+neighbour+scene+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: luna: The neighboring supplication asks for good in both worlds and protection from the Fire, giving a balanced alternative to seeking only worldly good. | terra: The answering prayer seeks good in both world and hereafter, setting a right ordering that does not call every worldly good refuse.
- (2:202) [luna: strong; terra: strong; basis: neighbour+scene+theme] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: The next ayah says these people have a share from what they earned, completing the consequence of the balanced supplication. | terra: أُولَٰٓئِكَ لَهُمْ نَصِيبٌ مِّمَّا كَسَبُوا assigns the correctly ordered seekers a lasting earned portion and completes the pair.
- (2:207) [luna: strong (missing-ayat turn); basis: contrast+theme] وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: luna: A person gives up the self in seeking God’s approval, a specific reversal of keeping worldly benefit for oneself.
- (2:212) [terra: strong; basis: scene+theme] زُيِّنَ لِلَّذِينَ كَفَرُوا۟ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَيَسْخَرُونَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ ۘ وَٱلَّذِينَ ٱتَّقَوْا۟ فَوْقَهُمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
  Unverified discovery rationale: terra: Worldly life is adorned for unbelievers who mock believers, but the God-fearing will be above them on resurrection day, reversing apparent rank.
- (2:216) [terra: strong (missing-ayat turn); basis: theme] كُتِبَ عَلَيْكُمُ ٱلْقِتَالُ وَهُوَ كُرْهٌۭ لَّكُمْ ۖ وَعَسَىٰٓ أَن تَكْرَهُوا۟ شَيْـًۭٔا وَهُوَ خَيْرٌۭ لَّكُمْ ۖ وَعَسَىٰٓ أَن تُحِبُّوا۟ شَيْـًۭٔا وَهُوَ شَرٌّۭ لَّكُمْ ۗ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
  Unverified discovery rationale: terra: People may dislike what is good for them and love what is bad for them; divine knowledge therefore corrects desire as a sufficient rule of selection.
- (2:221) [terra: strong (missing-ayat turn); basis: contrast+root+theme] وَلَا تَنكِحُوا۟ ٱلْمُشْرِكَٰتِ حَتَّىٰ يُؤْمِنَّ ۚ وَلَأَمَةٌۭ مُّؤْمِنَةٌ خَيْرٌۭ مِّن مُّشْرِكَةٍۢ وَلَوْ أَعْجَبَتْكُمْ ۗ وَلَا تُنكِحُوا۟ ٱلْمُشْرِكِينَ حَتَّىٰ يُؤْمِنُوا۟ ۚ وَلَعَبْدٌۭ مُّؤْمِنٌ خَيْرٌۭ مِّن مُّشْرِكٍۢ وَلَوْ أَعْجَبَكُمْ ۗ أُو۟لَٰٓئِكَ يَدْعُونَ إِلَى ٱلنَّارِ ۖ وَٱللَّهُ يَدْعُوٓا۟ إِلَى ٱلْجَنَّةِ وَٱلْمَغْفِرَةِ بِإِذْنِهِۦ ۖ وَيُبَيِّنُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ
  Unverified discovery rationale: terra: A believing slave is better than an admired polytheist, correcting a chooser who confuses social station or attraction with worth.
- (2:247) [terra: strong; basis: scene+theme] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ٱللَّهَ قَدْ بَعَثَ لَكُمْ طَالُوتَ مَلِكًۭا ۚ قَالُوٓا۟ أَنَّىٰ يَكُونُ لَهُ ٱلْمُلْكُ عَلَيْنَا وَنَحْنُ أَحَقُّ بِٱلْمُلْكِ مِنْهُ وَلَمْ يُؤْتَ سَعَةًۭ مِّنَ ٱلْمَالِ ۚ قَالَ إِنَّ ٱللَّهَ ٱصْطَفَىٰهُ عَلَيْكُمْ وَزَادَهُۥ بَسْطَةًۭ فِى ٱلْعِلْمِ وَٱلْجِسْمِ ۖ وَٱللَّهُ يُؤْتِى مُلْكَهُۥ مَن يَشَآءُ ۚ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
  Unverified discovery rationale: terra: Israel rejects Saul for lacking abundant wealth, but their prophet says God selected him and increased him in knowledge and stature, overturning their worldly criterion of worth.
- (2:248) [terra: strong; basis: root+scene] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ءَايَةَ مُلْكِهِۦٓ أَن يَأْتِيَكُمُ ٱلتَّابُوتُ فِيهِ سَكِينَةٌۭ مِّن رَّبِّكُمْ وَبَقِيَّةٌۭ مِّمَّا تَرَكَ ءَالُ مُوسَىٰ وَءَالُ هَٰرُونَ تَحْمِلُهُ ٱلْمَلَٰٓئِكَةُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: terra: The Ark bears بَقِيَّةٌ of what the houses of Moses and Aaron left; this sacred remainder carries tranquility and serves as the sign of the chosen king.
- (2:264) [terra: strong (missing-ayat turn); basis: scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: Charity ruined by reproach and display becomes dust on a smooth rock swept bare by rain, a deed chosen for appearance turning into residue with no yield.
