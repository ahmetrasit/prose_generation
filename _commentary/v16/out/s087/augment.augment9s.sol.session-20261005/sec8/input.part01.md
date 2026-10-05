Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 8 of 18 ("Uzaktan görülen ateş"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 8 (prose paragraphs numbered) =====
[¶32] On ikinci ayet bedbahtı {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yasle'n-nâra'l-kubrâ, gloss:o en büyük ateşe girecek olan, source:87:12} diye tanıtır. "Ateş" kelimesi ışıkla aynı köktendir: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-ẕâlike min tarîkati'l-idâe, gloss:nur da nâr da aydınlatma yönünden bu adı almıştır, source:"ن و ر,B001"}. Arapça bir ateşe varmanın birkaç yolunu ayrı ayrı adlandırır. Uzakta görülen ateşe yönelinir: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran kasadtu ileyhâ, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}, {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min baîd tebassartuhâ, gloss:ateşi uzaktan seçtim, source:"ن و ر,B003"}. Ateş yol işareti olarak yakılır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu ifade üçüncü ayetteki "yol gösterdi" fiilinin kökünü içerir. Yol işaretinin adı da {ar:المنار: علم الطريق, tr:el-menâr alemu't-tarîk, gloss:menâr yolun işaretidir, source:"ن و ر,B005"} diye verilir ve yedinci ayetteki "bilir" fiilinin köküne bağlanır. Ateşte ısınılır: {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-salâu mâ yustalâ bihî ve mâ yuẕkâ bihi'n-nâru ve yûkad, gloss:salâ ısınılan ve ateşin tutuşturulduğu şeydir, source:"ص ل ي,B004"}. Ya da kişi ateşe sokulur ve yakıcılığına katlanır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Et de ateşte kızartılır: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. الكبرى ise {ar:كبر كل شيء عظمه, tr:kibru kulli şey'in izamuh, gloss:her şeyin kibri onun büyüklüğüdür, source:"ك ب ر,B001"}.

[¶33] يصلى fiili ص ل ي kökündendir. On beşinci ayetteki فَصَلَّىٰ ise ص ل و kökündendir. Harfleri aynı kalıba oturur ama iki ayrı köktür, ve aralarındaki yakınlık bir yankıdır, kimlik değildir. Yine de sure bu yankıyı iki karşıt kişiye bölüştürür. Biri ateşe girer, öbürü Rabbinin adını anıp namaz kılar. Ateşe varmanın yolları arasındaki fark burada önem kazanır. Uzaktan görülüp yol bulmak için yönelinen ateş ile içine sokulup katlanılan ateş aynı nesnedir, ama ona giden kişinin işi farklıdır.

[¶34] Kur'an bu farkı surenin son ayetinde anılan Musa'nın hikâyesinde sahneler. Musa bir ateş görür ve ailesine şöyle der: {ar:ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:imkuŝû innî ânestu nâran leallî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:burada kalın; ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Başka bir anlatımda amacı ısınmaktır: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Bir başka anlatımda ateşi {ar:مِن جَانِبِ ٱلطُّورِ, tr:min cânibi't-tûr, gloss:Tur'un yanından, source:28:29} görür. Bu ifadede on birinci ayetteki kökün "yan" anlamı geçer. Ateşe vardığında kendisine seslenilir: {ar:أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:en bûrike men fi'n-nâri ve men havlehâ ve subhânallâhi rabbi'l-âlemîn, gloss:ateşin içindeki ve çevresindeki kutlu kılındı; Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu seslenişte birinci ayetteki tesbih ateşin başında söylenir. Hikâyenin bir başka anlatımında ses ona şöyle der: {ar:وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ, tr:ve ene'htertuke fe'stemi' li-mâ yûhâ, gloss:seni ben seçtim; vahyolunanı dinle, source:20:13}, ve sonra {ar:فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:fa'budnî ve ekımi's-salâte li-ẕikrî, gloss:bana kulluk et ve beni anmak için namazı kıl, source:20:14}. Musa'nın ateşe yolculuğu namaz ve anma ile biter. Bu, surenin on beşinci ayetindeki kişinin yaptığı iştir. Kur'an insanların yaktığı küçük ateşi de anar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Hükmü de verir: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:nahnu cealnâhâ teẕkiraten ve metâan li'l-mukvîn, gloss:onu bir hatırlatma ve çölde kalanlara bir geçimlik yaptık, source:56:73}. Küçük ateş bir öğüttür. Surenin dokuzuncu ayetindeki öğütten yüz çeviren ise on ikinci ayetteki büyük ateşe girer.

[¶35] Ateşe sokulmanın işleyişini Kur'an kızartma diliyle anlatır: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ, gloss:derileri piştikçe onları başka derilerle değiştiririz, source:4:56}. Allah ayetlere sırt çeviren biri için {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26} der, ve o ateşin niteliği şudur: {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ teẕer, gloss:ne bir şey bırakır ne de bir şeyi kendi haline koyar, source:74:28}. Bu ifadede on yedinci ayetteki "kalıcı" kelimesinin kökü olumsuz bir fiilde geçer. Sekar'dakilere oraya neden girdikleri sorulduğunda cevapları şudur: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:namaz kılanlardan değildik dediler, source:74:43}. Bir başka surede ateş için surenin kendi kelimeleri kullanılır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en sakınan ondan uzak tutulacaktır, source:92:17}. Bu surede en bedbaht öğütten uzak durur. Orada ise en sakınan ateşten uzak tutulur. Aynı fiil yön değiştirir. Ateşin büyüklüğü başka yerlerde de anılır: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Bir başka yerde öğütten yüz çeviren için {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah onu en büyük azapla cezalandırır, source:88:24} denir. Musa'ya ateşin başında gösterilen ise başka bir büyüklüktür: {ar:لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى, tr:li-nuriyeke min âyâtine'l-kubrâ, gloss:sana en büyük ayetlerimizden göstermek için, source:20:23}.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (202) =====
## strong (95)

- (2:257) [luna: strong (missing-ayat turn); basis: contrast+root+theme] ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۖ وَٱلَّذِينَ كَفَرُوٓا۟ أَوْلِيَآؤُهُمُ ٱلطَّٰغُوتُ يُخْرِجُونَهُم مِّنَ ٱلنُّورِ إِلَى ٱلظُّلُمَٰتِ ۗ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: luna: The ayah joins God bringing believers from darkness into light with disbelievers becoming companions of the Fire. That directly links the section's n-w-r relation between fire and light to its contrast between a fire that guides and the Fire one enters.
- (3:185) [terra: strong; basis: scene+theme] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: terra: Success is defined as being pulled away from the fire and admitted to the garden, joining directional removal from fire to the surah's declaration قَدْ أَفْلَحَ.
- (4:56) [luna: strong; terra: strong; basis: root+scene] [cited in ¶35] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
  Unverified discovery rationale: luna: The section's roasting sense of ص ل ي becomes a bodily description: skins are cooked (naḍijat julūduhum) and replaced, so the person entering the great Fire bears its heat repeatedly. | terra: The repeated replacement of skins whenever they are cooked makes bodily roasting concrete and directly develops the source section's ص ل ي dictionary image.
- (4:115) [terra: strong; basis: root+theme] وَمَن يُشَاقِقِ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُ ٱلْهُدَىٰ وَيَتَّبِعْ غَيْرَ سَبِيلِ ٱلْمُؤْمِنِينَ نُوَلِّهِۦ مَا تَوَلَّىٰ وَنُصْلِهِۦ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًا
  Unverified discovery rationale: terra: After guidance has become clear, one who follows another way is turned toward what he chose and made to burn in Hell; path choice, rejected guidance, and entry into fire form one judgment.
- (6:97) [terra: strong; basis: root+scene+theme] وَهُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلنُّجُومَ لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
  Unverified discovery rationale: terra: The stars are appointed so people may find guidance through the darkness of land and sea, matching the practical wayfinding purpose of a distant flame.
- (11:69) [terra: strong; basis: root+scene] وَلَقَدْ جَآءَتْ رُسُلُنَآ إِبْرَٰهِيمَ بِٱلْبُشْرَىٰ قَالُوا۟ سَلَٰمًۭا ۖ قَالَ سَلَٰمٌۭ ۖ فَمَا لَبِثَ أَن جَآءَ بِعِجْلٍ حَنِيذٍۢ
  Unverified discovery rationale: terra: Abraham brings a roasted calf, عِجْلٍ حَنِيذٍ; it is the Quranic scene that most directly realizes the source section's secondary dictionary sense 'I roasted the meat.'
- (11:98) [luna: strong (missing-ayat turn); basis: contrast+scene] يَقْدُمُ قَوْمَهُۥ يَوْمَ ٱلْقِيَٰمَةِ فَأَوْرَدَهُمُ ٱلنَّارَ ۖ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ
  Unverified discovery rationale: luna: On the Day of Resurrection Pharaoh leads his people and brings them to the Fire. This reverses the section's fire lit as a waymark toward guidance: here a leader's route ends at the Fire.
- (14:5) [terra: strong; basis: root+speaker+theme] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَآ أَنْ أَخْرِجْ قَوْمَكَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ
  Unverified discovery rationale: terra: Moses is commanded to bring his people from darkness into light and to remind them of Allah's days; it unites the fire story's prophet, guiding light, and reminder.
- (14:17) [luna: strong; terra: medium; basis: scene+theme] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
  Unverified discovery rationale: luna: In the Hell context named in 14:16, death comes from every direction yet the person does not die (wa-mā huwa bi-mayyit). This concretizes the fire's suspended state between death and life in 87:13. | terra: The inhabitant of punishment has death coming from every side yet does not die, a close expansion of the one in the great fire who neither dies nor lives.
- (16:16) [terra: strong; basis: root+scene+theme] وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ
  Unverified discovery rationale: terra: وَعَلَامَاتٍۢ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ gives visible landmarks and a distant light by which travelers find their way, the Quranic counterpart to a menār as road sign.
- (17:18) [terra: strong; basis: root+theme] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
  Unverified discovery rationale: terra: The person who desires the immediate life is assigned Hell and يَصْلَىٰهَا, directly connecting preference for the nearer world in 87:16 with the burning fate in 87:12.
- (18:29) [terra: strong (missing-ayat turn); basis: scene+theme] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
  Unverified discovery rationale: terra: Hell's enclosing fire and a drink like molten metal that scalds faces develop both forced enclosure by fire and its bodily cooking heat.
- (20:3) [terra: strong (missing-ayat turn); basis: speaker+theme] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
  Unverified discovery rationale: terra: Surah 20 frames its revelation, before Moses's fire scene, as a reminder for the one who fears; this exactly matches the reminder's intended hearer in 87:9–10.
- (20:10) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶34] إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى
  Unverified discovery rationale: luna: Section's remote fire is the object Moses has seen: innî ānastu nāran, then he hopes for a brand or guidance by it. This stages the fire as a destination and waymark before 87:12's entry into it. | terra: Moses sees a fire at a distance, goes toward it for a brand, and hopes to find hudā at the fire; this is the section's fire as warmth, visible waymark, and guidance in one scene.
- (20:11) [terra: strong; basis: neighbour+scene] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
  Unverified discovery rationale: terra: When Moses reaches the fire he is called by name; this supplies the decisive arrival in the journey begun at 20:10.
- (20:12) [luna: strong; terra: strong; basis: neighbour+scene+speaker] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
  Unverified discovery rationale: luna: Following the fire Moses saw in 20:10 and the call in 20:11, this verse tells him to remove his sandals because he is in the sacred valley. Its detail makes the approach a holy encounter, not simply a search for fuel or warmth. | terra: The caller at the fire identifies Himself as Moses's Lord and names the valley sacred, showing what the hoped-for guidance at the fire actually becomes.
- (20:13) [luna: strong; terra: strong; basis: neighbour+scene+speaker+theme] [cited in ¶34] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
  Unverified discovery rationale: luna: After the fire and approach in 20:10–12, God says He has chosen Moses and tells him to listen to revelation. This verse's own contribution is to make the fire journey an encounter with a divine speaker and revelation, before 20:14 turns to prayer and remembrance. | terra: The voice at the fire says Moses has been chosen and must listen to revelation, turning his search for practical direction into revealed guidance.
- (20:14) [luna: strong; terra: strong; basis: neighbour+root+scene+speaker+theme] [cited in ¶34] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
  Unverified discovery rationale: luna: In the other account of Moses' fire encounter, the command faʿbudnī wa-aqimi al-ṣalāta li-dhikrī ends in worship and prayer for God's remembrance. That is the remembered Lord and prayer set against entering the fire in 87:12 and stated in 87:15. | terra: The voice reached through the fire commands worship and أَقِمِ ٱلصَّلَوٰةَ لِذِكْرِى; Moses's approach to fire ends in the remembrance and prayer paired in the section.
- (20:23) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶35] لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى
  Unverified discovery rationale: luna: In Moses' encounter, the purpose is for God to show him some of His greatest signs (al-kubrā). The section explicitly places this k-b-r greatness beside 87:12's great fire and 88:24's greatest punishment, while this verse gives greatness a revelatory sense. | terra: At the fire Allah says He will show Moses مِنْ ءَايَاتِنَا ٱلْكُبْرَى; the same greatness that qualifies the fire is redirected to divine signs.
- (20:50) [terra: strong; basis: root+speaker+theme] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
  Unverified discovery rationale: terra: Moses describes his Lord as the one who gave everything its created form ثُمَّ هَدَىٰ, an especially close Mosaic parallel to the Creator who measured and guided in 87:2–3.
- (20:74) [luna: strong; terra: strong; basis: scene+theme] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
  Unverified discovery rationale: luna: The account says the guilty person has Hell and will neither die nor live in it (lā yamūtu fīhā wa-lā yaḥyā); this directly extends the state inside the fire given in 87:12–13. | terra: In the same surah as Moses's fire, the criminal who comes to his Lord has Hell where he neither dies nor lives, exactly repeating the state adjacent to the great fire in 87:13.
- (22:20) [luna: strong; terra: medium; basis: neighbour+scene] يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ
  Unverified discovery rationale: luna: In this punishment, boiling liquid melts what is inside the bellies and the skins. This gives the section's fire-entry and suffering-its-heat distinction a concrete inward and bodily counterpart. | terra: The boiling punishment melts what is inside them and their skins, paralleling the section's roasting sense and the cooked skins of 4:56.
