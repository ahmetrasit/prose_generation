Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 6 of 18 ("Yarılan tarla: büyüme ve hakkı verilen ürün"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 6 (prose paragraphs numbered) =====
[¶24] On dördüncü ayet {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kurtuluşa ermiştir, source:87:14} der. Ayetin iki fiilinin aileleri bir tarla sahnesi kurar. فلح toprağı yarmaktır: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda şakaktuhâ, gloss:toprağı sürdüm ve yardım, source:"ف ل ح,B001"}. Toprağı süren de bu adı alır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:sumiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye toprağı yardığı için fellâh denmiştir, source:"ف ل ح,B003"}. Kökün başarı anlamı ise kalıcılık üzerinden tanımlanır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh iyilik içinde kalmaktır, source:"ف ل ح,B005"}. {ar:الفلاح الفوز والنجاة والبقاء, tr:el-felâh el-fevzu ve'n-necâtu ve'l-bekâ, gloss:felâh kazanmak kurtulmak ve kalıcı olmaktır, source:"ف ل ح,B005"}. Bu tanım on dördüncü ayeti, on yedinci ayetteki iki kelimeye, "hayırlı" ve "kalıcı" kelimelerine bağlar. زكا ekinin büyüyüp çoğalmasıdır: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen izdâde ve nemâ, gloss:ekin artıp büyüdü, source:"ز ك و,B001"}. {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti en-nemuvvu'l-hâsılu an bereketi'llâh, gloss:zekâtın aslı Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. Aynı kök üründen verilen payı da anlatır: {ar:زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق, tr:zekkâ mâlehû tezkiyeten ey eddâ anhu zekâtehû ve tezekkâ ey tesaddaka, gloss:malının zekâtını verdi; tezekkâ sadaka verdi demektir, source:"ز ك و,B003"}. Bu pay geri kalanı temizler: {ar:الطهارة زكاة المال؛ زكاة لأنها طهارة, tr:et-tahâretu zekâtu'l-mâl zekâtun li-ennehâ tahâra, gloss:temizlik malın zekâtıdır; temizlik olduğu için zekât denmiştir, source:"ز ك و,B002"}.

[¶25] Sahnenin öbür parçaları surenin başka kelimelerindedir. Dördüncü ayetin fiili hasılatın adını verir: {ar:الخرج والخراج ما يخرج من المال في السنة بقدر معلوم, tr:el-harcu ve'l-harâcu mâ yahrucu mine'l-mâli fi's-seneti bi-kaderin ma'lûm, gloss:harâc maldan her yıl bilinen bir ölçüyle çıkandır, source:"خ ر ج,B003"}. Bu tanım üçüncü ayetin kökünü de içerir. Rab, çiftliğe bakıp onu tamamlayandır: {ar:رب فلان ضيعته إذا قام على إصلاحها, tr:rabbe fulânun day'atehû iẕâ kâme alâ islâhihâ, gloss:falanca çiftliğinin bakımını üstlendi, source:"ر ب ب,B002"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde, hasılattan geriye kalan şey vardır: {ar:الباقي حاصل الخراج ونحوه, tr:el-bâkî hâsılu'l-harâci ve nahvih, gloss:bâkî hasılattan ve benzerinden kalan miktardır, source:"ب ق ي,B002"}.

[¶26] Düz bir anlatım on dördüncü ayeti "arınan kurtuldu" diye özetler. Tarla sahnesi bu cümleye bir işleyiş ekler: toprak yarılır, ekin büyür, büyüyen üründen bir pay verilir, verilen pay geri kalanı temizler, ve bu büyüme iyilik içinde kalıcı olur. Böylece tarla, beşinci ayetteki yabani otlağın karşısına geçer. Aynı toprakta biri kuruyup selle gider, öbürü işlenir, verimi alınır ve hakkı ödenir.

[¶27] Kur'an bu tarlayı açıkça sahneler. Allah insandan yemeğine bakmasını ister: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:biz suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:ŝumme şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Yarmak fiili tarlanın sürülmesini de verir. Başka bir yerde Allah sorar: {ar:أَفَرَءَيْتُم مَّا تَحْرُثُونَ, tr:e-fe-raeytum mâ tahruŝûn, gloss:ektiğinizi gördünüz mü, source:56:63}. Ardından {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا, tr:lev neşâu le-cealnâhu hutâmâ, gloss:dileseydik onu çer çöp yapardık, source:56:65} diye ekler. Tarla da otlağın kaderine düşebilir. Ayrım ekimin hangi tarlaya yapıldığındadır: {ar:مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ, tr:men kâne yurîdu harŝe'l-âhireti nezid lehû fî harŝih ve men kâne yurîdu harŝe'd-dunyâ nu'tihî minhâ ve mâ lehû fi'l-âhireti min nasîb, gloss:ahiret tarlasını isteyenin tarlasını artırırız; dünya tarlasını isteyene ondan veririz ama onun ahirette payı yoktur, source:42:20}. Bu ayet, on altıncı ve on yedinci ayetteki karşıtlığı tarlanın diliyle söyler. Ürünün hakkı için {ar:وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ, tr:ve âtû hakkahû yevme hasâdih, gloss:hasat günü hakkını verin, source:6:141} denir. Malını veren kişi için {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:elleẕî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} denir. Can üzerine yemin edilen ayetlerde iki ayrı son yan yana konur: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad eflaha men zekkâhâ, gloss:onu arıtan kurtuluşa erdi, source:91:9}, {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp örten ise hüsrana uğradı, source:91:10}. Tarlanın dilinde arıtmanın karşıtı, tohumu toprağın altında boğmaktır. Peygamber'in arkadaşları ise bir ekine benzetilir: {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ, tr:ke-zer'in ahrace şat'ehû fe-âzerahû fe'steğleza fe'stevâ alâ sûkıh, gloss:filizini çıkaran sonra onu güçlendiren sonra kalınlaşıp sapları üzerinde doğrulan bir ekin gibi, source:48:29}. Bu ayet, surenin dördüncü ayetindeki "çıkardı" fiilini ve ikinci ayetindeki "düzene koydu" fiilinin kökünü, kurumayan bir ekinde buluşturur. Bir başka yerde kurtuluşa erenler sayılırken {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad eflaha'l-mu'minûn, gloss:müminler kurtuluşa ermiştir, source:23:1} denir ve onlar arasında {ar:وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ, tr:velleẕîne hum li'z-zekâti fâilûn, gloss:zekâtı yerine getirenler, source:23:4} anılır. Musa'nın karşısındaki sihirbazlar da sözlerini cennet bahçelerini anarak bitirir: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu arınanın karşılığıdır, source:20:76}.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (254) =====
## strong (139)

- (2:177) [luna: strong (missing-ayat turn); basis: root+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section interprets tazkiya as a wealth share given to purify; this ayah defines righteousness through giving wealth to named recipients, prayer, and zakat, specifying the ethical acts behind that purification.
- (2:200) [terra: strong (missing-ayat turn); basis: contrast+theme] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: terra: One pilgrim asks only for worldly benefit and consequently has no share in the afterlife, closely matching the worldly tilth with no afterlife portion in 42:20.
- (2:201) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: The contrasting prayer asks for good in both the world and the afterlife, refusing to make the nearer field the sole crop.
- (2:202) [terra: strong (missing-ayat turn); basis: neighbour+theme] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: terra: Those who ask for both goods receive a share of what they have earned, joining labor, portion, and lasting outcome.
- (2:205) [luna: strong (missing-ayat turn); terra: contrast; basis: contrast+scene] وَإِذَا تَوَلَّىٰ سَعَىٰ فِى ٱلْأَرْضِ لِيُفْسِدَ فِيهَا وَيُهْلِكَ ٱلْحَرْثَ وَٱلنَّسْلَ ۗ وَٱللَّهُ لَا يُحِبُّ ٱلْفَسَادَ
  Unverified discovery rationale: luna: The section contrasts tended ground and a field whose growth is lost; this ayah describes a corrupt person striving to destroy crops and offspring, making deliberate destruction the field's moral opposite. | terra: The corrupt person destroys cultivated land and progeny, reversing the Lord-like work of maintaining and repairing a farm.
- (2:261) [luna: medium; terra: strong; basis: scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section's ز ك و includes growth and an apportioned gift; this ayah compares spending in God's way to a grain producing seven ears, making giving and multiplying harvest one image. | terra: Spending wealth is pictured as one grain producing seven ears and multiplied seed, joining gift, crop, and increase.
- (2:264) [luna: strong (missing-ayat turn); terra: contrast; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section says the crop's given share cleans what remains; this ayah warns that reproach and harm can nullify charity, comparing such spending to soil washed from bare rock, a failed counterpart to fruitful giving. | terra: Charity spoiled by display and injury is like thin soil washed from rock by rain, a gift whose apparent field retains no yield.
- (2:265) [luna: strong; terra: strong; basis: scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: The section joins giving a share to blessed growth; this ayah pictures those who spend seeking God's approval as a garden on fertile ground that yields double after rain. | terra: Sincere spending is a high garden whose rain brings double yield, so giving itself becomes fruitful cultivation.
- (2:267) [luna: strong; terra: strong; basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
  Unverified discovery rationale: luna: The section names the root خ ر ج for what emerges and explains tazkiya as giving from produce; this ayah joins spending good things to what God brought forth from earth. | terra: Believers must spend from good earnings and from what God brings out of the earth, making the field's produce the substance of the gift.
- (2:271) [terra: strong; basis: root+theme] إِن تُبْدُوا۟ ٱلصَّدَقَٰتِ فَنِعِمَّا هِىَ ۖ وَإِن تُخْفُوهَا وَتُؤْتُوهَا ٱلْفُقَرَآءَ فَهُوَ خَيْرٌۭ لَّكُمْ ۚ وَيُكَفِّرُ عَنكُم مِّن سَيِّـَٔاتِكُمْ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
  Unverified discovery rationale: terra: Concealed charity to the poor is called better and is said to remove evil deeds, directly pairing a paid share with cleansing.
- (2:276) [luna: strong; terra: strong; basis: contrast+root+theme] يَمْحَقُ ٱللَّهُ ٱلرِّبَوٰا۟ وَيُرْبِى ٱلصَّدَقَٰتِ ۗ وَٱللَّهُ لَا يُحِبُّ كُلَّ كَفَّارٍ أَثِيمٍ
  Unverified discovery rationale: luna: The section's root ز ك و includes growth and charity; this ayah contrasts God erasing usury with making charities grow, clarifying the difference between increase by taking and increase through giving. | terra: God effaces usury but makes charities grow, the sharpest non-field statement of increase through giving rather than grasping.
- (2:277) [luna: strong; basis: root+theme] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ لَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: luna: The section connects giving zakat to success and what remains; this ayah pairs belief, prayer, and zakat with reward from the Lord and freedom from fear, linking the given share to enduring recompense.
- (3:14) [terra: strong (missing-ayat turn); basis: contrast+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: terra: Cultivated land is listed among the alluring provisions of worldly life, making the field itself one object of the preference named in 87:16.
- (3:15) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: terra: What is better than those worldly attractions is then identified as abiding gardens with the Lord, turning cultivation toward its lasting end.
- (3:92) [terra: strong; basis: theme] لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: terra: One does not attain enduring goodness until giving from what one loves, specifying the costly share by which good is reached.
- (3:117) [luna: strong (missing-ayat turn); terra: contrast; basis: contrast+scene+theme] مَثَلُ مَا يُنفِقُونَ فِى هَٰذِهِ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَثَلِ رِيحٍۢ فِيهَا صِرٌّ أَصَابَتْ حَرْثَ قَوْمٍۢ ظَلَمُوٓا۟ أَنفُسَهُمْ فَأَهْلَكَتْهُ ۚ وَمَا ظَلَمَهُمُ ٱللَّهُ وَلَٰكِنْ أَنفُسَهُمْ يَظْلِمُونَ
  Unverified discovery rationale: luna: The section links a crop's fate to whether its yield is rightly cultivated and shared; this ayah compares what wrongdoers spend to a freezing wind that strikes and destroys a people's harvest, showing spending that yields no good. | terra: Worldly spending by wrongdoers is like a freezing wind that destroys a crop, an anti-harvest opposite to charity that multiplies.
- (6:95) [terra: strong; basis: root+scene] ۞ إِنَّ ٱللَّهَ فَالِقُ ٱلْحَبِّ وَٱلنَّوَىٰ ۖ يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَمُخْرِجُ ٱلْمَيِّتِ مِنَ ٱلْحَىِّ ۚ ذَٰلِكُمُ ٱللَّهُ ۖ فَأَنَّىٰ تُؤْفَكُونَ
  Unverified discovery rationale: terra: God splits the grain and date-stone and brings living from dead, placing divine opening at the seed inside the section's split field.
- (6:99) [luna: strong; terra: strong; basis: scene+theme] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: luna: The section describes grain growing from split earth; this ayah stages rain producing green growth, grain, dates, grapes, olives, and pomegranates, making divine provision visible in harvest. | terra: Water produces vegetation, layered grain, and ripening fruit, and the reader is told to look at fruiting and maturity; this is the field's growth made visible.
