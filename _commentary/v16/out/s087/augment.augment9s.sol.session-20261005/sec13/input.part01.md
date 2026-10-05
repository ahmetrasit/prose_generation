Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 13 of 18 ("Açık ve gizli: ses ve örtüden çıkan"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 13 (prose paragraphs numbered) =====
[¶51] Yedinci ayetin sonu {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} der. Bu cümle iki ayrı sahnede duyulur. Birincisi sestir. جهر sesi yükseltmektir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savtah, gloss:sözü açıktan söyledi yani sesini yükseltti, source:"ج ه ر,B001"}. {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin zıddıdır, source:"ج ه ر,B001"}. Bu kök tek bir harfin söylenişine kadar iner: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve menea'n-nefese en yecriye meah, gloss:harfe mechûr denir çünkü çıkış yerine tam dayanır ve nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. خفي sesi kısmaktır: {ar:أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا, tr:ahfeytu's-savte ihfâen ve'l-hâfiyetu diddu'l-alâniye ve lekîtuhû hafiyyen ey sirran, gloss:sesi kıstım; hâfiye açıklığın zıddıdır; onunla gizlice karşılaştım, source:"خ ف ي,B001"}. On beşinci ayetteki anma iki yerde yaşar: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle ve kalbimle andım, source:"ذ ك ر,B004"}. Okuma da ezberden yapılır: {ar:قرأت القرآن عن ظهر قلب أو نظرت فيه, tr:kara'tu'l-kur'âne an zahri kalbin ev nazartu fîh, gloss:Kur'an'ı ezberden ya da bakarak okudum, source:"ق ر ء,B002"}. Bilmek de söylenenin farkında olmaktır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim yani farkına varmadım, source:"ع ل م,B001"}. Bu sahnede yedinci ayet, altıncı ayetteki okumanın iki halini, yüksek sesle ve içten okumayı birlikte kucaklar. Okutulan söz dilde de olsa kalpte de olsa bilinir.

[¶52] İkinci sahne örtüden çıkmaktır. "Gizli" kökü, Arapçada zıt anlamları birlikte taşıyan kelimelerden biridir: {ar:خفيت الشيء بغير ألف إذا أظهرته, tr:hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz hafeytu bir şeyi açığa çıkardım demektir, source:"خ ف ي,B003"}. {ar:استخفيت الشئ أي استخرجته, tr:istahfeytu'ş-şey'e ey istahrectuh, gloss:bir şeyi çıkardım, source:"خ ف ي,B003"}. Bu ikinci açıklama dördüncü ayetin "çıkarmak" kökünü kullanır, ki o kökün temel anlamı şudur: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerinden ya da halinden dışarı belirdi, source:"خ ر ج,B001"}. Örtülü olanın somut örnekleri de vardır: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine yakın dallardır, source:"خ ف ي,B002"}. {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî kanadın ön tüylerinin altında kalan tüylerdir, source:"خ ف ي,B002"}. Öbür uçta açık olan vardır: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmıştır, source:"ج ه ر,B002"}, ve temizlenip suyu görünen kuyu bu kökle anılır. Açıklığın bir tersi de vardır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâ elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Fazla ışık da bir örtü olabilir. Dördüncü ayetle birlikte okununca yedinci ayetin ikilisi sabit iki durum olmaktan çıkar ve bir harekete dönüşür: yağmurla topraktan ot çıkar, deliklerden fareler çıkar. Gizli olan, Rabbin bildiği ve dilediğinde açığa çıkardığı şeydir.

[¶53] Kur'an bu iki sahneyi açıkça kurar. Peygamber'e indirilen hitabın başında şöyle denir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi ve daha gizlisini bilir, source:20:7}. Bu, Musa'nın ateşi gördüğü sahneye geçmeden önceki ayetlerdendir. Aynı hikâyede ateşin başında {ar:إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا, tr:inne's-sâate âtiyetun ekâdu uhfîhâ, gloss:o saat gelecektir; onu neredeyse gizli tutuyorum, source:20:15} denir. Sesin ölçüsü bir emirle verilir: {ar:وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا, tr:ve lâ techer bi-salâtike ve lâ tuhâfit bihâ vebteğı beyne ẕâlike sebîlâ, gloss:namazında sesini ne yükselt ne de kıs; ikisinin arasında bir yol tut, source:17:110}. Anmanın sesi de belirlenir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden yalvararak ve korkarak ve yüksek olmayan bir sesle an, source:7:205}. Duanın sesi de: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufye, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}. Allah için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ, tr:innehû ya'lemu'l-cehra mine'l-kavli ve ya'lemu mâ tektumûn, gloss:O sözün açığını da bilir gizlediğinizi de bilir, source:21:110} ve {ar:يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ, tr:ya'lemu sirrakum ve cehrakum, gloss:gizlinizi de açığınızı da bilir, source:6:3} denir. Örtüden çıkarma sahnesini ise Süleyman'a haber getiren hüdhüd anlatır. Hüdhüd bir kavmin güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini söyler ve şöyle ekler: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran ve gizlediğinizi de açıkladığınızı da bilen Allah'a secde etmesinler diye, source:27:25}. Bu tek ayette dördüncü ayetteki "çıkarmak" ile yedinci ayetteki gizli ve açık bir arada bulunur.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (337) =====
## strong (194)

- (2:17) [terra: strong (missing-ayat turn); basis: contrast+scene] مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ
  Unverified discovery rationale: terra: A kindled fire lights the surroundings and then God removes the light, leaving the people in darkness unable to see; visibility turns into its opposite.
- (2:19) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] أَوْ كَصَيِّبٍۢ مِّنَ ٱلسَّمَآءِ فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ يَجْعَلُونَ أَصَٰبِعَهُمْ فِىٓ ءَاذَانِهِم مِّنَ ٱلصَّوَٰعِقِ حَذَرَ ٱلْمَوْتِ ۚ وَٱللَّهُ مُحِيطٌۢ بِٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: Darkness, thunder, and lightning surround people who plug their ears against the blast, supplying both obscured sight and deliberately blocked sound before 2:20.
- (2:22) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The verse describes rain sent down and fruits brought forth from the earth as provision, a direct though general instance of emergence. | terra: Rain descends and fruits are brought out as provision, an early direct parallel to pasture brought forth from earth.
- (2:33) [luna: strong; terra: strong; basis: root+theme] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
  Unverified discovery rationale: luna: God says He knows what the angels disclose and what they had concealed; the scene gives the section's hidden/manifest pair a concrete disclosure. | terra: God couples knowledge of the unseen heavens and earth with knowledge of what creatures reveal and conceal.
- (2:60) [terra: strong (missing-ayat turn); basis: root+scene] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: terra: The struck stone releases twelve springs, a direct instance of covered water brought into view.
- (2:72) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] وَإِذْ قَتَلْتُمْ نَفْسًۭا فَٱدَّٰرَْٰٔتُمْ فِيهَا ۖ وَٱللَّهُ مُخْرِجٌۭ مَّا كُنتُمْ تَكْتُمُونَ
  Unverified discovery rationale: luna: In the murder story, God brings out what the people had concealed; the verse directly combines the source section's extraction root خ ر ج with hidden matter becoming manifest. | terra: God brings out what the disputants were concealing about the killing, an exact human instance of the hidden being extracted.
- (2:74) [terra: strong; basis: root+scene] ثُمَّ قَسَتْ قُلُوبُكُم مِّنۢ بَعْدِ ذَٰلِكَ فَهِىَ كَٱلْحِجَارَةِ أَوْ أَشَدُّ قَسْوَةًۭ ۚ وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ ۚ وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
  Unverified discovery rationale: terra: Stones split and water comes out, providing a material instance of hidden water becoming visible.
- (2:77) [luna: strong; terra: strong; basis: root+theme] أَوَلَا يَعْلَمُونَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
  Unverified discovery rationale: luna: This asks whether people know that God knows what they conceal and declare, directly extending the section's account of divine knowledge beyond audible speech. | terra: The ayah asks whether they do not know that God knows both what they keep secret and what they publish.
- (2:235) [terra: strong; basis: scene+theme] وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا عَرَّضْتُم بِهِۦ مِنْ خِطْبَةِ ٱلنِّسَآءِ أَوْ أَكْنَنتُمْ فِىٓ أَنفُسِكُمْ ۚ عَلِمَ ٱللَّهُ أَنَّكُمْ سَتَذْكُرُونَهُنَّ وَلَٰكِن لَّا تُوَاعِدُوهُنَّ سِرًّا إِلَّآ أَن تَقُولُوا۟ قَوْلًۭا مَّعْرُوفًۭا ۚ وَلَا تَعْزِمُوا۟ عُقْدَةَ ٱلنِّكَاحِ حَتَّىٰ يَبْلُغَ ٱلْكِتَٰبُ أَجَلَهُۥ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِىٓ أَنفُسِكُمْ فَٱحْذَرُوهُ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
  Unverified discovery rationale: terra: God knows an inward intention that will be mentioned, while the ayah regulates secret promises and the proper spoken word.
- (2:257) [luna: strong (missing-ayat turn); basis: contrast+root+theme] ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۖ وَٱلَّذِينَ كَفَرُوٓا۟ أَوْلِيَآؤُهُمُ ٱلطَّٰغُوتُ يُخْرِجُونَهُم مِّنَ ٱلنُّورِ إِلَى ٱلظُّلُمَٰتِ ۗ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: luna: God brings believers out of darkness into light; the source section's root خ ر ج is defined as emerging from a place or state, and this verse makes the state change explicit.
- (2:271) [terra: strong; basis: root+theme] إِن تُبْدُوا۟ ٱلصَّدَقَٰتِ فَنِعِمَّا هِىَ ۖ وَإِن تُخْفُوهَا وَتُؤْتُوهَا ٱلْفُقَرَآءَ فَهُوَ خَيْرٌۭ لَّكُمْ ۚ وَيُكَفِّرُ عَنكُم مِّن سَيِّـَٔاتِكُمْ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
  Unverified discovery rationale: terra: Alms may be made visible or hidden; the latter state is explicitly named and valued, showing one act across openness and cover.
- (2:284) [luna: medium; terra: strong; basis: root+scene+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The verse concerns what people disclose or conceal within themselves; it extends the source section's hidden state from remembered words to inward accountability. | terra: What is inside the self remains known and accountable whether it is disclosed or hidden, closely matching speech on the tongue or in the heart.
- (3:5) [luna: strong; terra: strong; basis: root+theme] إِنَّ ٱللَّهَ لَا يَخْفَىٰ عَلَيْهِ شَىْءٌۭ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
  Unverified discovery rationale: luna: Nothing in earth or heaven is hidden from God; this states the section's hidden/known relation in the most direct terms. | terra: Nothing in earth or heaven is hidden from God, stating the knowledge claim behind the section without limiting it to speech.
- (3:6) [terra: strong (missing-ayat turn); basis: scene+theme] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: terra: God shapes people within wombs however He wills, locating unseen formation inside a physical covering.
- (3:29) [luna: strong; terra: strong; basis: root+scene+theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The verse applies concealment and disclosure to what lies in people's breasts; it makes explicit that the section's inward side includes intention, not only quiet speech. | terra: What breasts hide or reveal is known by God; the concealed interior and its outward disclosure are explicitly paired.
- (3:41) [terra: strong (missing-ayat turn); basis: contrast+scene+speaker] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۖ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَةَ أَيَّامٍ إِلَّا رَمْزًۭا ۗ وَٱذْكُر رَّبَّكَ كَثِيرًۭا وَسَبِّحْ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
  Unverified discovery rationale: terra: Zechariah's sign is inability to speak to people except by gesture, yet he is commanded to remember and glorify God much; inward worship persists when ordinary voice is blocked.
- (3:118) [terra: strong; basis: scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ بِطَانَةًۭ مِّن دُونِكُمْ لَا يَأْلُونَكُمْ خَبَالًۭا وَدُّوا۟ مَا عَنِتُّمْ قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ ۖ إِن كُنتُمْ تَعْقِلُونَ
  Unverified discovery rationale: terra: Hostility has appeared from mouths while breasts hide still more, making speech the audible edge of a deeper concealed state.
- (3:154) [terra: strong; basis: scene+theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: God tests what is in breasts, purifies what is in hearts, and knows the breasts' contents, turning the covered interior into something brought to proof.
- (4:42) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَئِذٍۢ يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ وَعَصَوُا۟ ٱلرَّسُولَ لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ وَلَا يَكْتُمُونَ ٱللَّهَ حَدِيثًۭا
  Unverified discovery rationale: terra: At judgment people cannot conceal any statement from God, marking the end of speech that could once be privately withheld.
- (4:81) [terra: strong (missing-ayat turn); basis: scene+theme] وَيَقُولُونَ طَاعَةٌۭ فَإِذَا بَرَزُوا۟ مِنْ عِندِكَ بَيَّتَ طَآئِفَةٌۭ مِّنْهُمْ غَيْرَ ٱلَّذِى تَقُولُ ۖ وَٱللَّهُ يَكْتُبُ مَا يُبَيِّتُونَ ۖ فَأَعْرِضْ عَنْهُمْ وَتَوَكَّلْ عَلَى ٱللَّهِ ۚ وَكَفَىٰ بِٱللَّهِ وَكِيلًا
