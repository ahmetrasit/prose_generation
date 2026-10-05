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
- (24:35) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section links nār and nūr through illumination; this lamp's oil almost gives light though no fire touches it (لم تمسسه نار). The verse makes the boundary between fire and light explicit: light may appear without the fire that the section also depicts as punishment. | terra: The light verse brings نُور, a lamp kindled from a blessed tree, oil nearly shining without fire, and يَهْدِى ٱللَّهُ لِنُورِهِ together; it fully stages the section's fire/light etymology and guiding illumination.
- (24:36) [terra: strong (missing-ayat turn); basis: neighbour+root+speaker+theme] فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ
  Unverified discovery rationale: terra: The light-and-fire parable continues in houses where Allah's name is remembered and He is glorified; this carries 24:35's guiding illumination into the remembrance named beside prayer in the section.
- (24:37) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
  Unverified discovery rationale: terra: The people illuminated by the preceding parable are not distracted from remembering Allah and establishing prayer, directly reuniting the section's remembrance and ص ل و side after 24:35's نُور and نَار.
- (25:12) [luna: strong; terra: contrast; basis: contrast+scene] إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا
  Unverified discovery rationale: luna: The section describes a person seeing a fire from afar; here Hell itself sees its targets from a far place (min makānin baʿīd). The perceiver is reversed, turning the remote sight into a threat that approaches the onlooker. | terra: From a distant place the fire sees the condemned and rages at them; agency reverses the section's traveler who sees a distant fire and intentionally approaches it.
- (25:13) [luna: strong; terra: medium (missing-ayat turn); basis: neighbour+scene] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
  Unverified discovery rationale: luna: After Hell sees its targets from afar in 25:12, this verse depicts them bound in a cramped place within it. Its own contribution carries the section's distinction from sighting a distant fire to being inside and subjected to it. | terra: After the fire sees them from afar, they are cast chained into a narrow place within it; this supplies the forced arrival that follows 25:12's reversal of distant sight.
- (25:64) [terra: strong; basis: neighbour+root+theme] وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدًۭا وَقِيَٰمًۭا
  Unverified discovery rationale: terra: The servants of the Merciful spend the night prostrating and standing before their Lord, supplying the prayer posture for the plea about Hell in the next ayah.
- (25:65) [terra: strong; basis: neighbour+scene+theme] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا
  Unverified discovery rationale: terra: Those praying servants ask their Lord to turn Hell's punishment away from them, explicitly joining worship with being spared the fire.
- (27:7) [luna: strong; terra: strong; basis: root+scene] [cited in ¶34] إِذْ قَالَ مُوسَىٰ لِأَهْلِهِۦٓ إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ
  Unverified discovery rationale: luna: This telling says Moses hopes his family may warm themselves, laʿallakum taṣṭalūn; it realizes the section's dictionary branch of ص ل ي for warming by a fire, alongside the root's punitive sense in 87:12. | terra: Moses sees a fire and promises either news or a burning brand so his family may warm themselves; تَصْطَلُونَ realizes the source section's warming sense of the ص ل ي family.
- (27:8) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶34] فَلَمَّا جَآءَهَا نُودِىَ أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: At the fire, the address blesses whoever is in it and around it and says subḥāna Allāh. This locates glorification, commanded at 87:1, within Moses' fire encounter rather than the fire's punitive entry in 87:12. | terra: At the fire Moses hears blessing upon those in it and around it followed by سُبْحَانَ ٱللَّهِ رَبِّ ٱلْعَالَمِينَ; the road fire becomes the place of the surah's glorification.
- (27:9) [luna: strong; terra: medium; basis: neighbour+scene+speaker] يَٰمُوسَىٰٓ إِنَّهُۥٓ أَنَا ٱللَّهُ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The verse after 27:8 identifies the voice addressing Moses as Allah, the Mighty, the Wise. Its own detail clarifies who speaks at the fire where the preceding verse blesses those in and around it. | terra: The next words at the fire identify the caller as Allah, the Mighty and Wise, confirming whose guidance Moses found there.
- (28:29) [luna: strong; terra: strong; basis: root+scene] [cited in ¶34] ۞ فَلَمَّا قَضَىٰ مُوسَى ٱلْأَجَلَ وَسَارَ بِأَهْلِهِۦٓ ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا قَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ
  Unverified discovery rationale: luna: Moses sees the fire from the side of Ṭūr (jānib al-ṭūr) and approaches for a brand or guidance. The prose connects this side-word's ج ن ب root with 87:11's avoiding the fire: the root's spatial side and its avoidance sense meet the image's opposed routes. | terra: Moses sees fire مِن جَانِبِ ٱلطُّورِ and seeks news or an ember for warmth, combining the section's distant fire, direction, side, and warming details.
- (28:30) [luna: strong; terra: strong; basis: neighbour+scene+speaker] فَلَمَّآ أَتَىٰهَا نُودِىَ مِن شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ فِى ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ مِنَ ٱلشَّجَرَةِ أَن يَٰمُوسَىٰٓ إِنِّىٓ أَنَا ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: After Moses sees fire from the side of Ṭūr in 28:29, this verse says that when he comes to it he is called from a blessed spot by the tree. Its contribution is the call that turns the sighting into the encounter developed in the section. | terra: On reaching the fire Moses is called from the blessed spot and tree by Allah, Lord of the worlds; it completes 28:29's journey toward the flame.
- (29:45) [terra: strong; basis: root+theme] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
  Unverified discovery rationale: terra: The ayah joins establishing ٱلصَّلَوٰةَ, remembrance of Allah, and the claim وَلَذِكْرُ ٱللَّهِ أَكْبَرُ, gathering the section's prayer, remembrance, and greatness on the positive side.
- (35:18) [terra: strong (missing-ayat turn); basis: speaker+theme] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: Those who fear their Lord unseen, establish prayer, and purify themselves are gathered in one ayah, matching the receptive fear, تَزَكَّىٰ, and prayer on the section's saved side.
- (35:36) [luna: strong; terra: medium; basis: scene+theme] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
  Unverified discovery rationale: luna: For the disbelievers there is Hellfire, where death is not decreed for them and its punishment is not lightened. This is another explicit account of the fire's non-ending condition beside 87:13. | terra: The people of Hell are neither finished so that they die nor given lighter punishment, restating the suspended state beside 87:12.
- (36:78) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَضَرَبَ لَنَا مَثَلًۭا وَنَسِىَ خَلْقَهُۥ ۖ قَالَ مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌۭ
  Unverified discovery rationale: terra: The denier asks who can revive decayed bones; this states the question for which the green-tree fire in 36:80 is presented as a visible reminder.
- (36:79) [terra: strong (missing-ayat turn); basis: neighbour+theme] قُلْ يُحْيِيهَا ٱلَّذِىٓ أَنشَأَهَآ أَوَّلَ مَرَّةٍۢ ۖ وَهُوَ بِكُلِّ خَلْقٍ عَلِيمٌ
  Unverified discovery rationale: terra: The answer says the One who first produced the bones will revive them, identifying resurrection as what the ordinary flame of 36:80 is meant to make thinkable.
- (36:80) [luna: strong; terra: strong; basis: scene+theme] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
  Unverified discovery rationale: luna: God says He made fire for people from the green tree, which they then kindle. This is another concrete form of the useful human fire in 56:71–73 and presents it as a sign of provision rather than Saqar's punishment. | terra: Allah makes fire from the green tree and people kindle from it; an ordinary flame born from its apparent opposite functions as evidence for the power being recalled.
- (36:81) [terra: strong (missing-ayat turn); basis: neighbour+theme] أَوَلَيْسَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِقَٰدِرٍ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُم ۚ بَلَىٰ وَهُوَ ٱلْخَلَّٰقُ ٱلْعَلِيمُ
  Unverified discovery rationale: terra: After the green-tree fire, creation of the heavens and earth concludes the argument that their Creator can recreate people; it completes the flame's function as a reminder.
- (37:97) [luna: strong (missing-ayat turn); basis: contrast+scene] قَالُوا۟ ٱبْنُوا۟ لَهُۥ بُنْيَٰنًۭا فَأَلْقُوهُ فِى ٱلْجَحِيمِ
  Unverified discovery rationale: luna: Abraham's people say to cast him into a blazing fire. This is a second explicit staging of someone being put into fire, but the surrounding Quranic account reverses the section's suffering-fire image when God makes that fire cool and safe (21:69).
- (52:16) [terra: strong; basis: root+theme] ٱصْلَوْهَا فَٱصْبِرُوٓا۟ أَوْ لَا تَصْبِرُوا۟ سَوَآءٌ عَلَيْكُمْ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
  Unverified discovery rationale: terra: The condemned are told ٱصْلَوْهَا and that endurance or refusal to endure is alike, directly joining entry into fire with bearing its severity.
- (56:71) [luna: strong; terra: strong; basis: root+scene] [cited in ¶34] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
  Unverified discovery rationale: luna: This asks about the fire people kindle (al-nāra allatī tūrūn), the small, human-lit fire the section contrasts with the great Fire and then calls a reminder in 56:73. | terra: The question about ٱلنَّارَ ٱلَّتِى تُورُونَ directly presents the small fire people themselves kindle, the useful fire set against the great fire.
- (56:72) [luna: strong; terra: strong; basis: neighbour+scene] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
  Unverified discovery rationale: luna: The verse after the question about kindling fire in 56:71 asks whether humans or God brought forth its tree. Its contribution is to connect the usable fire to God's provision, setting up the reminder and provision named in 56:73. | terra: The question whether people produced the fire's tree or Allah did makes the ordinary kindled flame a created sign, completing 56:71.
- (56:73) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] [cited in ¶34] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
  Unverified discovery rationale: luna: God says the human-kindled fire is a reminder (tadhkiratan) and provision for wilderness travelers (matāʿan lil-muqwīn). It gives the small fire the admonitory and sustaining purpose that the section contrasts with turning from 87:9's reminder into the great Fire. | terra: Allah says the small fire was made تَذْكِرَةً and a benefit for travelers or the needy; this directly grounds the section's claim that the useful flame is itself a reminder.
- (56:74) [luna: strong; terra: strong; basis: neighbour+scene+speaker+theme] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
  Unverified discovery rationale: luna: After the verses about kindling fire, its tree, reminder, and provision, this verse commands glorification of the great Lord. Its own contribution joins reflection on fire to the tasbīḥ at 87:1 and to the fire-side glorification in 27:8. | terra: Immediately after fire is declared a reminder, the hearer is told to glorify the name of the tremendous Lord; the small-fire sequence reaches the same glorification that opens surah 87.
- (56:94) [terra: strong (missing-ayat turn); basis: root+scene] وَتَصْلِيَةُ جَحِيمٍ
  Unverified discovery rationale: terra: تَصْلِيَةُ جَحِيمٍ names a roasting in Hell with the same ص ل ي family, making the source section's roasting sense the form of punishment.
- (62:9) [terra: strong (missing-ayat turn); basis: root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: When the call to prayer is made, believers are commanded to hasten to the remembrance of Allah; prayer and remembrance are one directed act here.
- (67:7) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene] إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ
  Unverified discovery rationale: luna: Those thrown into Hell hear its roaring as it boils. This stages the section's entry into fire and endurance of its heat as an audible, seething scene. | terra: When people are thrown into Hell they hear it inhale while it boils, giving a vivid arrival inside the punitive fire.
- (67:8) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene+speaker+theme] تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ ۖ كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ
  Unverified discovery rationale: luna: The next verse says Hell nearly bursts with rage and its keepers ask whether a warner came. Its contribution connects the fire's scene to the warning and reminder the section says the wretched person avoids. | terra: As each group is cast in, the raging fire's keepers ask whether a warner came, directly joining entry into fire to the prior opportunity for reminder.
- (67:9) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene+theme] قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا وَقُلْنَا مَا نَزَّلَ ٱللَّهُ مِن شَىْءٍ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ كَبِيرٍۢ
  Unverified discovery rationale: luna: The people in Hell answer that a warner did come but they denied him. This completes 67:8's question and makes the link between rejected reminder and entry into fire explicit, as in 87:9–12. | terra: Those cast into the fire admit that a warner came and that they denied him, supplying the same rejected-admonition sequence as 87:9–12.
- (69:31) [terra: strong (missing-ayat turn); basis: root+scene] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
  Unverified discovery rationale: terra: The command ثُمَّ ٱلْجَحِيمَ صَلُّوهُ explicitly has the condemned person put into the blaze, realizing the source section's causative sense of inserting someone into fire.
- (70:15) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] كَلَّآ ۖ إِنَّهَا لَظَىٰ
  Unverified discovery rationale: luna: This passage names the blazing fire Laẓā. It supplies another concrete fire for the section's contrast between a fire one approaches for guidance or warmth and the great Fire entered for punishment. | terra: The threatened destination is named لَظَىٰ, beginning a passage in which the blaze calls the one who turned away and praying people form the exception.
- (70:16) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene] نَزَّاعَةًۭ لِّلشَّوَىٰ
  Unverified discovery rationale: luna: Laẓā is described as stripping the scalp. This gives the section's accounts of skin cooked or scorched in fire (4:56, 74:29) a closely related bodily image. | terra: The blaze is نَزَّاعَةً لِّلشَّوَىٰ, stripping the body's outer parts; it gives another precise bodily counterpart to cooked and scorched skin.
- (70:17) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ
  Unverified discovery rationale: luna: The fire calls the one who turned away and turned his back (man adbara wa-tawallā). That directly joins the section's person who turns away from reminder to the fire he enters. | terra: The blaze itself calls the person who turned his back and withdrew; this reverses the traveler choosing a visible fire and matches the reminder-avoider whom the great fire receives.
- (70:18) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَجَمَعَ فَأَوْعَىٰٓ
  Unverified discovery rationale: luna: The same passage says the person gathered and hoarded wealth; following the fire's call to the turn-away person in 70:17, this gives a concrete worldly preference alongside 87:16's preference for the nearer life. | terra: The blaze calls the one who amassed and hoarded, completing 70:17's description of the person whom the fire summons.
- (70:19) [terra: strong (missing-ayat turn); basis: neighbour+theme] ۞ إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا
  Unverified discovery rationale: terra: Humanity is described as anxiously constituted before praying people are excepted, stating the general condition from which 70:22 separates them.
- (70:20) [terra: strong (missing-ayat turn); basis: neighbour+theme] إِذَا مَسَّهُ ٱلشَّرُّ جَزُوعًۭا
  Unverified discovery rationale: terra: The person panics when harm touches him, one half of the behavior from which the people of prayer are made the exception.
- (70:21) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا
  Unverified discovery rationale: terra: The person withholds when good touches him, completing the traits immediately answered by إِلَّا ٱلْمُصَلِّينَ.
- (70:22) [terra: strong; basis: contrast+neighbour+root+theme] إِلَّا ٱلْمُصَلِّينَ
  Unverified discovery rationale: terra: إِلَّا ٱلْمُصَلِّينَ makes people of prayer the explicit exception to the traits attached to the blaze, reproducing the section's division between fire and prayer.
- (70:23) [terra: strong; basis: neighbour+root+theme] ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ
  Unverified discovery rationale: terra: The exception is specified as those constant in their prayer, giving durable practice to the section's فَصَلَّىٰ side.
- (73:20) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ
  Unverified discovery rationale: terra: The same surah that commands remembering the Lord's name in 73:8 later commands establishing prayer, confirming the section's pairing of remembrance and ṣalāh.
- (74:26) [luna: strong; terra: strong; basis: root+scene] [cited in ¶35] سَأُصْلِيهِ سَقَرَ
  Unverified discovery rationale: luna: The threat sa-uṣlīhi Saqar names entry into a fire and uses the same ص ل ي root as 87:12's entering and enduring the great Fire. | terra: سَأُصْلِيهِ سَقَرَ uses the causative fire verb for putting the sign-rejecter into Saqar, exactly the punitive approach to fire developed by the section.
- (74:28) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶35] لَا تُبْقِى وَلَا تَذَرُ
  Unverified discovery rationale: luna: Saqar “neither spares nor leaves” (lā tubqī wa-lā tadhar); the negative baqā-rooted verb reverses 87:17's description of the Hereafter as more enduring (abqā), sharpening what cannot be preserved inside the fire. | terra: Saqar لَا تُبْقِى وَلَا تَذَرُ; its refusal to leave anything gives the negative ب ق ي counterpart to the surah's enduring good.
- (74:29) [luna: strong; terra: strong; basis: neighbour+scene] لَوَّاحَةٌۭ لِّلْبَشَرِ
  Unverified discovery rationale: luna: Saqar is described as a scorcher of human skin (lawwāḥatun lil-bashar), extending the section's account of fire's effect on skin alongside 4:56's repeated cooking and replacement. | terra: لَوَّاحَةٌ لِّلْبَشَرِ identifies Saqar as a scorcher of human skin, sharpening the section's roasting image and 4:56's cooked skins.
- (74:35) [terra: strong; basis: neighbour+root] إِنَّهَا لَإِحْدَى ٱلْكُبَرِ
  Unverified discovery rationale: terra: The Saqar passage calls it إِحْدَى ٱلْكُبَرِ, placing the fire among the great matters and directly echoing ٱلنَّارَ ٱلْكُبْرَىٰ.
- (74:42) [terra: strong; basis: neighbour+scene] مَا سَلَكَكُمْ فِى سَقَرَ
  Unverified discovery rationale: terra: The question مَا سَلَكَكُمْ فِى سَقَرَ asks what course brought them into the fire and introduces the answer about failing to pray.
- (74:43) [luna: strong; terra: strong; basis: contrast+neighbour+root+scene+theme] [cited in ¶35] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
  Unverified discovery rationale: luna: Asked why they are in Saqar, its people answer that they were not among those who prayed (lam nakun mina al-muṣallīn). This makes the fire's occupants the direct opposite of the one who remembers the Lord and prays in 87:15; the related-looking ṣ-l-y roots mark different acts. | terra: The inhabitants answer that they were not among ٱلْمُصَلِّينَ; the same passage thus joins entry into fire to the absence of the prayer that answers it in surah 87.
- (74:44) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ
  Unverified discovery rationale: terra: The people in Saqar continue their answer by saying they did not feed the poor; this distinguishes the cited row's own cause from their preceding failure to pray.
- (74:45) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ
  Unverified discovery rationale: terra: Their answer continues that they joined others in vain discourse, adding another stated action on the road that brought them into Saqar.
- (74:46) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: neighbour+theme] وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ
  Unverified discovery rationale: luna: Among the reasons given by Saqar's occupants after their confession about prayer in 74:43, this ayah says they denied the Day of Recompense. It specifies the rejection of the Hereafter that contrasts with 87:16–17's preference for the present life and the superior, enduring Hereafter. | terra: They say they denied the Day of Judgment, making denial of the final reckoning another explicit reason for their presence in Saqar.
- (74:47) [terra: strong (missing-ayat turn); basis: neighbour+theme] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
  Unverified discovery rationale: terra: Their denial continued until certainty came to them; this closes the inhabitants' own explanation of how they reached Saqar.
- (75:31) [terra: strong; basis: neighbour+root+theme] فَلَا صَدَّقَ وَلَا صَلَّىٰ
  Unverified discovery rationale: terra: فَلَا صَدَّقَ وَلَا صَلَّىٰ names failure to pray as part of the condemned person's refusal, directly illuminating the prayer/fire division.
- (75:32) [terra: strong; basis: neighbour+theme] وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: terra: وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ completes 75:31 with denial and turning away, the same stance that precedes fire in 92:14–16 and 88:21–24.
- (79:16) [terra: strong (missing-ayat turn); basis: neighbour+scene+speaker] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
  Unverified discovery rationale: terra: The Lord calls Moses in the sacred valley of Tuwa, repeating the call reached by approaching the fire in 20:11–12.
- (79:18) [terra: strong (missing-ayat turn); basis: neighbour+theme] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
  Unverified discovery rationale: terra: Moses is told to ask Pharaoh whether he will purify himself, linking the Mosaic call to the successful تَزَكَّىٰ person on the prayer side of surah 87.
- (79:19) [terra: strong (missing-ayat turn); basis: neighbour+root+speaker+theme] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
  Unverified discovery rationale: terra: Moses offers to guide Pharaoh to his Lord so that he may fear, joining guidance and the receptive fear that makes reminder effective.
- (79:38) [luna: strong (missing-ayat turn); basis: contrast+theme] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: luna: This ayah says that a person preferred the worldly life (āthara al-ḥayāta al-dunyā), closely repeating 87:16. Its neighboring verse, 79:39, names Hell as his destination, making this preference an explicit route toward the fire discussed in the section.
- (79:39) [luna: strong (missing-ayat turn); basis: neighbour+scene] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: After 79:38 describes preferring worldly life, this ayah says Hell is the refuge. Its own contribution makes the fire the outcome of the preference that 87:16 sets against the better, lasting Hereafter in 87:17.
- (79:40) [luna: strong (missing-ayat turn); basis: contrast+theme] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
  Unverified discovery rationale: luna: The alternative person fears standing before his Lord and restrains himself from desire. This gives a specific counterpart to 87:10's one who fears and to the worldly preference leading to Hell in 79:38–39.
- (79:41) [luna: strong (missing-ayat turn); basis: neighbour+scene] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: The verse after that restraint says Paradise is the refuge. Its own contribution completes the contrast between the fire for worldly preference and a lasting good destination, the choice framed in 87:16–17.
- (88:4) [luna: strong; terra: strong; basis: root+scene] [cited in ¶35] تَصْلَىٰ نَارًا حَامِيَةًۭ
  Unverified discovery rationale: luna: The miserable person taslā nāran ḥāmiyatan enters a hot fire. This repeats the section's entry-into-fire verb and its distinction between suffering the fire's heat and merely approaching one. | terra: تَصْلَىٰ نَارًا حَامِيَةً restates entry into a fiercely hot fire with the same ص ل ي sense and makes the endured heat explicit.
- (88:21) [luna: strong; terra: strong; basis: neighbour+root+speaker+theme] فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
  Unverified discovery rationale: luna: This passage commands the Prophet to remind (fa-dhakkir); the section pairs 87:9's reminder with turning away and the great Fire. Here the neighboring verses 88:23–24 make the reminder's rejection and punishment explicit. | terra: فَذَكِّرْ إِنَّمَا أَنتَ مُذَكِّرٌ repeats the command and stance of the reminder immediately before the passage's turning away and greater punishment.
- (88:23) [luna: strong; terra: strong; basis: neighbour+theme] إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
  Unverified discovery rationale: luna: The following punishment passage identifies the person who turns away and denies (man tawallā wa-kafarā); 88:24 gives him the greatest punishment. It echoes the section's wretched one turning from reminder before entering the great Fire. | terra: The one who turns away and disbelieves is singled out between the command to remind and the greater punishment, reproducing the section's causal sequence.
- (88:24) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] [cited in ¶35] فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
  Unverified discovery rationale: luna: For that turn-away person, God inflicts the greatest punishment (al-ʿadhāb al-akbar). This directly matches the section's pairing of fire with greatness in 87:12, while its preceding verse specifies the rejection that leads to it. | terra: ٱلْعَذَابَ ٱلْأَكْبَرَ supplies the direct 'greater punishment' counterpart to the section's great fire.
- (92:7) [terra: strong (missing-ayat turn); basis: neighbour+theme] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
  Unverified discovery rationale: terra: The giving, God-fearing person is eased toward ease with the same يُسْرَىٰ formulation as 87:8, and the passage later identifies him as the atqā kept from fire.
- (92:10) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
  Unverified discovery rationale: terra: The miserly denier is eased toward hardship, the pointed reversal of the ease promised in 87:8 before this passage reaches the blazing fire.
- (92:14) [terra: strong; basis: neighbour+scene+theme] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
  Unverified discovery rationale: terra: The speaker warns of نَارًا تَلَظَّىٰ, making the fire the content of an admonition just before the same ashqā language appears.
- (92:15) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶35] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
  Unverified discovery rationale: luna: The wording lā yaṣlāhā illā al-ashqā closely repeats 87:12's person who enters the great Fire, and directly connects the section's “most wretched” figure with who enters it here. | terra: لَا يَصْلَىٰهَا إِلَّا ٱلْأَشْقَى repeats both the burning verb and 'the most wretched,' making it the closest verbal counterpart to 87:11–12.
- (92:16) [luna: strong; terra: strong; basis: neighbour+theme] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: luna: The next verse defines the one called “most wretched” in 92:15 as someone who denied and turned away (kadhdhaba wa-tawallā). This gives content to the section's connection between rejecting 87:9's reminder and entering the Fire in 87:12. | terra: The ashqā is defined as the one who denied and turned away, corresponding concretely to the wretch who avoids the reminder before entering the fire.
- (92:17) [luna: strong; terra: contrast; basis: contrast+root+scene+theme] [cited in ¶35] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
  Unverified discovery rationale: luna: The section says 87:11's wretched person turns away from the reminder before entering fire; here the most God-fearing is kept away from the fire (wa-sayujannabuhā al-atqā). The same avoidance-root now names protection from the fire, reversing the section's allocation of avoidance. | terra: وَسَيُجَنَّبُهَا ٱلْأَتْقَىٰ reverses the direction of 87:11: the ashqā avoids the reminder, while the atqā is made to avoid the fire.
- (92:18) [luna: strong; terra: strong; basis: neighbour+theme] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
  Unverified discovery rationale: luna: The passage continues by describing the most God-fearing person as giving wealth to purify himself (yutī mālahu yatazakkā). This closely echoes 87:14's purification and explains the good outcome of the one kept away from fire in 92:17. | terra: The atqā kept from the fire gives his wealth يَتَزَكَّىٰ; this identifies his purification with the successful تَزَكَّىٰ person beside prayer in surah 87.
- (92:20) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
  Unverified discovery rationale: luna: The spared person's deed is for the face of his Lord, al-aʿlā. This links the fire-avoidance passage to 87:15's remembrance of the Lord and 87:1's “the Most High,” the stance opposite entering the Fire. | terra: The atqā kept from the fire gives only to seek the face of رَبِّهِ ٱلْأَعْلَىٰ, joining that spared person to the Lord Most High whose name is glorified in 87:1.
- (92:21) [luna: strong (missing-ayat turn); basis: neighbour+theme] وَلَسَوْفَ يَرْضَىٰ
  Unverified discovery rationale: luna: This closes the passage in which the God-fearing person is kept away from Fire in 92:17: he will be satisfied. Its contribution gives the saved person's outcome, alongside 87:14's success for the one who purifies himself.

## medium (57)

- (2:20) [terra: medium; basis: scene+theme] يَكَادُ ٱلْبَرْقُ يَخْطَفُ أَبْصَٰرَهُمْ ۖ كُلَّمَآ أَضَآءَ لَهُم مَّشَوْا۟ فِيهِ وَإِذَآ أَظْلَمَ عَلَيْهِمْ قَامُوا۟ ۚ وَلَوْ شَآءَ ٱللَّهُ لَذَهَبَ بِسَمْعِهِمْ وَأَبْصَٰرِهِمْ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: Lightning lights the way and people walk, then darkness makes them stand still; movement depends on visible illumination just as in the section's wayfinding fire.
- (3:191) [terra: medium; basis: neighbour+speaker+theme] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: Those who remember Allah in every posture ask to be protected from the punishment of the fire, linking remembrance directly to seeking distance from it.
- (3:192) [terra: medium; basis: neighbour+scene+theme] رَبَّنَآ إِنَّكَ مَن تُدْخِلِ ٱلنَّارَ فَقَدْ أَخْزَيْتَهُۥ ۖ وَمَا لِلظَّٰلِمِينَ مِنْ أَنصَارٍۢ
  Unverified discovery rationale: terra: Their prayer says that whoever Allah admits into the fire is disgraced, explicitly treating entry into fire as the outcome remembrance asks to avert.
- (4:10) [terra: medium; basis: root+scene] إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا
  Unverified discovery rationale: terra: Those who consume orphans' wealth unjustly consume fire into their bellies and will burn in a blaze; the fire is first taken into the body and then receives the person.
- (5:15) [terra: medium (missing-ayat turn); basis: neighbour+root+theme] يَٰٓأَهْلَ ٱلْكِتَٰبِ قَدْ جَآءَكُمْ رَسُولُنَا يُبَيِّنُ لَكُمْ كَثِيرًۭا مِّمَّا كُنتُمْ تُخْفُونَ مِنَ ٱلْكِتَٰبِ وَيَعْفُوا۟ عَن كَثِيرٍۢ ۚ قَدْ جَآءَكُم مِّنَ ٱللَّهِ نُورٌۭ وَكِتَٰبٌۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: A light and clarifying book are said to have come from Allah, supplying the guiding object by which 5:16 leads people along paths of peace.
- (5:16) [luna: medium (missing-ayat turn); terra: medium; basis: root+theme] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: The section's fire can serve as a waymark, and its prose links nār with nūr; here God guides people by revelation through paths of peace and brings them from darknesses into light. This is a specific light-as-guidance counterpart to the fire-side guidance of 20:10. | terra: Allah guides those seeking His pleasure along paths of peace and brings them from darkness into light; it states in non-fire language what the illuminated road marker makes perceptible.
- (6:122) [luna: medium; terra: medium; basis: root+theme] أَوَمَن كَانَ مَيْتًۭا فَأَحْيَيْنَٰهُ وَجَعَلْنَا لَهُۥ نُورًۭا يَمْشِى بِهِۦ فِى ٱلنَّاسِ كَمَن مَّثَلُهُۥ فِى ٱلظُّلُمَٰتِ لَيْسَ بِخَارِجٍۢ مِّنْهَا ۚ كَذَٰلِكَ زُيِّنَ لِلْكَٰفِرِينَ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: The section links fire with light and guidance; this verse gives a person who had been dead life and a light by which to walk among people. It offers a specific opposite to the one who neither dies nor lives in 87:13 and a light-as-guidance counterpart to the fire used as a waymark. | terra: The revived believer receives a light by which he walks among people, making illumination function as practical guidance along a way rather than mere brightness.
- (9:32) [terra: medium (missing-ayat turn); basis: contrast+neighbour+root+theme] يُرِيدُونَ أَن يُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَيَأْبَى ٱللَّهُ إِلَّآ أَن يُتِمَّ نُورَهُۥ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
  Unverified discovery rationale: terra: Opponents try to extinguish Allah's light with their mouths, applying a fire's vulnerability to nūr while promising that this light will be completed.
- (9:33) [terra: medium (missing-ayat turn); basis: neighbour+root+theme] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ وَلَوْ كَرِهَ ٱلْمُشْرِكُونَ
  Unverified discovery rationale: terra: The next ayah names the guidance with which the Messenger was sent, completing the link between the unextinguished light of 9:32 and hudā.
- (9:35) [luna: medium; terra: medium; basis: root+scene+theme] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
  Unverified discovery rationale: luna: The section notes the ج ن ب root's spatial “side” sense at Moses' fire on the side of Ṭūr; here heated treasure brands foreheads, sides (junūb), and backs in Hellfire. It extends that side-word into a bodily fire-scene, rather than the avoidance sense of 87:11. | terra: Wealth is heated in Hell's fire and used to brand foreheads, sides, and backs; ordinary fire's heating function becomes bodily punishment.
- (16:15) [terra: medium (missing-ayat turn); basis: neighbour+root+scene] وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَأَنْهَٰرًۭا وَسُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: Allah places paths on the earth so people may be guided, giving the road framework immediately before 16:16 names landmarks and stars.
- (17:97) [terra: medium (missing-ayat turn); basis: contrast+scene+theme] وَمَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُمْ أَوْلِيَآءَ مِن دُونِهِۦ ۖ وَنَحْشُرُهُمْ يَوْمَ ٱلْقِيَٰمَةِ عَلَىٰ وُجُوهِهِمْ عُمْيًۭا وَبُكْمًۭا وَصُمًّۭا ۖ مَّأْوَىٰهُمْ جَهَنَّمُ ۖ كُلَّمَا خَبَتْ زِدْنَٰهُمْ سَعِيرًۭا
  Unverified discovery rationale: terra: Whenever Hell's blaze subsides Allah increases it, contrasting the war fire Allah extinguishes in 5:64 with the punitive fire that cannot be put out.
- (19:52) [terra: medium; basis: root+scene+theme] وَنَٰدَيْنَٰهُ مِن جَانِبِ ٱلطُّورِ ٱلْأَيْمَنِ وَقَرَّبْنَٰهُ نَجِيًّۭا
  Unverified discovery rationale: terra: Moses is called مِن جَانِبِ ٱلطُّورِ and brought near for intimate speech; the Mount-side wording shares the section's ج ن ب detail while nearness counters avoidance.
- (19:59) [terra: medium; basis: root+theme] ۞ فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌ أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ ۖ فَسَوْفَ يَلْقَوْنَ غَيًّا
  Unverified discovery rationale: terra: Later generations neglect prayer and follow desires, then meet ruin; it supplies another explicit consequence for abandoning the positive ص ل و side of the section's echo.
- (19:70) [terra: medium; basis: neighbour+root+theme] ثُمَّ لَنَحْنُ أَعْلَمُ بِٱلَّذِينَ هُمْ أَوْلَىٰ بِهَا صِلِيًّۭا
  Unverified discovery rationale: terra: Allah knows best who is most deserving of صِلِيًّا in Hell, retaining the section's burning root while making admission an act of judgment.
- (19:71) [terra: medium; basis: neighbour+scene+theme] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
  Unverified discovery rationale: terra: Everyone is said to come to or pass by Hell, making approach to the fire universal before the separation described in the next ayah.
- (19:72) [terra: medium; basis: contrast+neighbour+scene+theme] ثُمَّ نُنَجِّى ٱلَّذِينَ ٱتَّقَوا۟ وَّنَذَرُ ٱلظَّٰلِمِينَ فِيهَا جِثِيًّۭا
  Unverified discovery rationale: terra: Allah saves the God-fearing and leaves the wrongdoers there on their knees, dividing those brought near the fire by their final relation to it.
- (20:73) [terra: medium (missing-ayat turn); basis: root+theme] إِنَّآ ءَامَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَٰيَٰنَا وَمَآ أَكْرَهْتَنَا عَلَيْهِ مِنَ ٱلسِّحْرِ ۗ وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ
  Unverified discovery rationale: terra: Within the Mosaic narrative the believing magicians say Allah is better and more lasting, repeating خَيْرٌ وَأَبْقَىٰ against Pharaoh's temporary threat.
- (21:31) [terra: medium (missing-ayat turn); basis: root+scene+theme] وَجَعَلْنَا فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِهِمْ وَجَعَلْنَا فِيهَا فِجَاجًۭا سُبُلًۭا لَّعَلَّهُمْ يَهْتَدُونَ
  Unverified discovery rationale: terra: Passes are made as roads through the earth so people may be guided, repeating the practical pathfinding relation behind the road marker.
- (21:68) [terra: medium; basis: neighbour+scene] قَالُوا۟ حَرِّقُوهُ وَٱنصُرُوٓا۟ ءَالِهَتَكُمْ إِن كُنتُمْ فَٰعِلِينَ
  Unverified discovery rationale: terra: Abraham's people command one another to burn him and support their gods, supplying the intended action that 21:69 overturns.
- (22:19) [terra: medium; basis: neighbour+scene] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
  Unverified discovery rationale: terra: Garments of fire are cut for the disbelievers and boiling water is poured over their heads, beginning another concrete scene of heat applied to bodies.
- (25:66) [terra: medium (missing-ayat turn); basis: neighbour+scene+theme] إِنَّهَا سَآءَتْ مُسْتَقَرًّۭا وَمُقَامًۭا
  Unverified discovery rationale: terra: The praying servants call Hell an evil settlement and residence, completing their plea for its punishment to be turned away.
- (28:46) [terra: medium; basis: root+scene+speaker] وَمَا كُنتَ بِجَانِبِ ٱلطُّورِ إِذْ نَادَيْنَا وَلَٰكِن رَّحْمَةًۭ مِّن رَّبِّكَ لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
  Unverified discovery rationale: terra: The addressee was not at the side of the Mount when Allah called, yet receives the account as mercy in order to warn; the fire-call scene is explicitly made into admonition.
- (29:24) [terra: medium; basis: contrast+scene] فَمَا كَانَ جَوَابَ قَوْمِهِۦٓ إِلَّآ أَن قَالُوا۟ ٱقْتُلُوهُ أَوْ حَرِّقُوهُ فَأَنجَىٰهُ ٱللَّهُ مِنَ ٱلنَّارِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: terra: Abraham's people propose killing or burning him, but Allah saves him from the fire; the scene contrasts being put into flame with being delivered from it.
- (32:21) [terra: medium; basis: contrast+root+theme] وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ
  Unverified discovery rationale: terra: A nearer punishment is tasted before the greater punishment so that people may return; it distinguishes an admonitory lesser suffering from ٱلْعَذَابَ ٱلْأَكْبَرَ.
- (39:16) [terra: medium; basis: scene+theme] لَهُم مِّن فَوْقِهِمْ ظُلَلٌۭ مِّنَ ٱلنَّارِ وَمِن تَحْتِهِمْ ظُلَلٌۭ ۚ ذَٰلِكَ يُخَوِّفُ ٱللَّهُ بِهِۦ عِبَادَهُۥ ۚ يَٰعِبَادِ فَٱتَّقُونِ
  Unverified discovery rationale: terra: Layers of fire above and below are expressly something by which Allah warns His servants, a punitive fire performing the reminder function assigned to the small flame.
- (39:22) [terra: medium (missing-ayat turn); basis: contrast+root+theme] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
  Unverified discovery rationale: terra: One opened to submission stands upon light from his Lord, while hardened hearts are far from Allah's remembrance; guiding light and failed reminder meet in one ayah.
- (39:71) [terra: medium; basis: scene+theme] وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا فُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَتْلُونَ عَلَيْكُمْ ءَايَٰتِ رَبِّكُمْ وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ بَلَىٰ وَلَٰكِنْ حَقَّتْ كَلِمَةُ ٱلْعَذَابِ عَلَى ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: The disbelievers are driven to Hell in groups until they arrive and its gates open; it is a coerced journey to fire rather than the purposeful approach to a waymark.
- (40:72) [terra: medium (missing-ayat turn); basis: root+scene] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
  Unverified discovery rationale: terra: The condemned pass through boiling water and then are set ablaze in fire, another concrete Quranic realization of heating and cooking the person.
- (43:10) [terra: medium (missing-ayat turn); basis: root+scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَجَعَلَ لَكُمْ فِيهَا سُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: Allah makes roads through the earth so people may be guided, a nonluminous formulation of the route for which the section's menār supplies a visible sign.
- (44:47) [terra: medium (missing-ayat turn); basis: neighbour+root+scene] خُذُوهُ فَٱعْتِلُوهُ إِلَىٰ سَوَآءِ ٱلْجَحِيمِ
  Unverified discovery rationale: terra: The condemned man is seized and dragged into the middle of the blaze, supplying the physical insertion into fire described by the source section's dictionary sense.
- (44:48) [terra: medium (missing-ayat turn); basis: neighbour+scene] ثُمَّ صُبُّوا۟ فَوْقَ رَأْسِهِۦ مِنْ عَذَابِ ٱلْحَمِيمِ
  Unverified discovery rationale: terra: Boiling punishment is poured over his head after he is dragged into the blaze, specifying how the fire scene acts upon the body.
- (53:18) [terra: medium (missing-ayat turn); basis: root+theme] لَقَدْ رَأَىٰ مِنْ ءَايَٰتِ رَبِّهِ ٱلْكُبْرَىٰٓ
  Unverified discovery rationale: terra: The Prophet sees some of his Lord's greatest signs, repeating the positive use of ٱلْكُبْرَىٰ for revelation rather than for the great fire.
- (54:48) [terra: medium (missing-ayat turn); basis: scene+theme] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
  Unverified discovery rationale: terra: The condemned are dragged on their faces in the fire and told to taste Saqar's touch, making approach coerced and bodily rather than a search for guidance.
- (57:12) [terra: medium; basis: neighbour+root+scene] يَوْمَ تَرَى ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ يَسْعَىٰ نُورُهُم بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِم بُشْرَىٰكُمُ ٱلْيَوْمَ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
  Unverified discovery rationale: terra: On the final day believers' light runs before them and on their right, turning nūr into a leading light on the decisive journey.
- (57:28) [terra: medium (missing-ayat turn); basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَءَامِنُوا۟ بِرَسُولِهِۦ يُؤْتِكُمْ كِفْلَيْنِ مِن رَّحْمَتِهِۦ وَيَجْعَل لَّكُمْ نُورًۭا تَمْشُونَ بِهِۦ وَيَغْفِرْ لَكُمْ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: The faithful are promised a light by which they may walk, another explicit presentation of nūr as a traveling light rather than brightness alone.
- (61:8) [terra: medium (missing-ayat turn); basis: contrast+neighbour+root+theme] يُرِيدُونَ لِيُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَٱللَّهُ مُتِمُّ نُورِهِۦ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
  Unverified discovery rationale: terra: The repeated attempt to extinguish Allah's light again treats nūr like a flame, while Allah's completion of it denies that human control.
- (61:9) [terra: medium (missing-ayat turn); basis: neighbour+root+theme] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ وَلَوْ كَرِهَ ٱلْمُشْرِكُونَ
  Unverified discovery rationale: terra: The repeated continuation says the Messenger was sent with guidance, again joining completed light to hudā.
- (66:8) [terra: medium; basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: Believers' light runs before them as they pray that it be perfected, joining guiding light, eschatological safety, and supplication.
- (67:5) [terra: medium (missing-ayat turn); basis: contrast+root+scene] وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًۭا لِّلشَّيَٰطِينِ ۖ وَأَعْتَدْنَا لَهُمْ عَذَابَ ٱلسَّعِيرِ
  Unverified discovery rationale: terra: The nearest heaven's lamps are made missiles against devils, while a blaze is prepared for them; luminous objects and punitive fire are assigned sharply different functions in one ayah.
- (73:8) [terra: medium; basis: root+speaker+theme] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
  Unverified discovery rationale: terra: وَٱذْكُرِ ٱسْمَ رَبِّكَ repeats the section's exact act of remembering the Lord's name and joins it to wholehearted devotion.
- (76:25) [terra: medium (missing-ayat turn); basis: neighbour+root+speaker+theme] وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا
  Unverified discovery rationale: terra: The command to remember the name of the Lord morning and evening repeats the action that immediately precedes prayer in 87:15.
- (76:26) [terra: medium (missing-ayat turn); basis: neighbour+root+speaker+theme] وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا
  Unverified discovery rationale: terra: The next ayah commands prostration and prolonged glorification at night, carrying 76:25's remembrance of the Lord's name into worship.
- (77:29) [terra: medium (missing-ayat turn); basis: neighbour+scene+theme] ٱنطَلِقُوٓا۟ إِلَىٰ مَا كُنتُم بِهِۦ تُكَذِّبُونَ
  Unverified discovery rationale: terra: The deniers are commanded to proceed toward what they had denied; this is the actual first imperative of the compulsory journey elaborated by 77:30–32.
- (77:30) [terra: medium; basis: neighbour+scene+theme] ٱنطَلِقُوٓا۟ إِلَىٰ ظِلٍّۢ ذِى ثَلَٰثِ شُعَبٍۢ
  Unverified discovery rationale: terra: The deniers are ordered to proceed toward what they denied, giving punitive compulsion to the section's idea of directing oneself toward fire.
- (77:31) [terra: medium; basis: contrast+neighbour+scene] لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ
  Unverified discovery rationale: terra: The apparent shade toward which they proceed neither shades nor protects from flame, so what looks like shelter fails at the fire.
- (77:32) [terra: medium; basis: neighbour+scene] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
  Unverified discovery rationale: terra: The fire throws sparks as large as a fortress, magnifying the small brand Moses hoped to carry into an overwhelming projectile.
- (77:33) [terra: medium (missing-ayat turn); basis: neighbour+scene] كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ
  Unverified discovery rationale: terra: The enormous sparks are likened to yellow camels, completing 77:32's magnification of an ember into an overwhelming fire scene.
- (79:20) [terra: medium; basis: root+speaker+theme] فَأَرَىٰهُ ٱلْءَايَةَ ٱلْكُبْرَىٰ
  Unverified discovery rationale: terra: Moses shows Pharaoh ٱلْءَايَةَ ٱلْكُبْرَىٰ, another Mosaic use of greatness for a sign rather than for the fire.
- (79:26) [terra: medium (missing-ayat turn); basis: neighbour+speaker+theme] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
  Unverified discovery rationale: terra: After Pharaoh's rejection of Moses, the episode is called a lesson for one who fears, returning the Mosaic narrative to the section's fear-responsive reminder.
- (82:15) [terra: medium (missing-ayat turn); basis: root+scene] يَصْلَوْنَهَا يَوْمَ ٱلدِّينِ
  Unverified discovery rationale: terra: The deniers enter or burn in the fire on the Day of Judgment, using the same ص ل ي sense in its final setting.
- (82:16) [terra: medium (missing-ayat turn); basis: neighbour+scene+theme] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
  Unverified discovery rationale: terra: They are never absent from that fire, adding sustained exposure to 82:15's entry and the section's endurance of its severity.
- (83:16) [terra: medium (missing-ayat turn); basis: root+scene] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
  Unverified discovery rationale: terra: The veiled deniers are then made to enter or burn in Hell, attaching the section's fire verb to exclusion from their Lord.
- (83:17) [terra: medium (missing-ayat turn); basis: neighbour+theme] ثُمَّ يُقَالُ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
  Unverified discovery rationale: terra: Inside that scene they are told this is what they used to deny, making rejected truth the explicit antecedent of 83:16's burning.
- (88:22) [terra: medium; basis: neighbour+speaker+theme] لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
  Unverified discovery rationale: terra: The reminder is told he is not a controller over the hearers; this distinguishes the messenger's admonition from Allah's punishment in 88:24.
- (104:6) [terra: medium; basis: scene+theme] نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
  Unverified discovery rationale: terra: نَارُ ٱللَّهِ ٱلْمُوقَدَةُ names Allah's kindled fire, setting the deliberately kindled punitive flame beside the small fire people kindle for use.
- (104:7) [terra: medium; basis: neighbour+scene] ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
  Unverified discovery rationale: terra: The kindled fire rises over the hearts, shifting the roasting image from outer skin to the body's inward center.

## contrast (16)

- (2:17) [luna: contrast; terra: contrast; basis: contrast+root+scene] مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ
  Unverified discovery rationale: luna: In the parable, a person kindles a fire; when it illuminates around him, God takes away their light (ذهب الله بنورهم). This directly joins the section's n-w-r link between fire and light, while showing that a fire's apparent illumination may be withdrawn, the opposite of a reliable waymark. | terra: A man kindles a fire and it lights his surroundings, but Allah takes away their light and leaves them unable to see; the hoped-for illumination of a waymark becomes lost sight and direction.
- (5:64) [terra: contrast; basis: contrast+scene+theme] وَقَالَتِ ٱلْيَهُودُ يَدُ ٱللَّهِ مَغْلُولَةٌ ۚ غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟ بِمَا قَالُوا۟ ۘ بَلْ يَدَاهُ مَبْسُوطَتَانِ يُنفِقُ كَيْفَ يَشَآءُ ۚ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۚ وَأَلْقَيْنَا بَيْنَهُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۚ كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ ۚ وَيَسْعَوْنَ فِى ٱلْأَرْضِ فَسَادًۭا ۚ وَٱللَّهُ لَا يُحِبُّ ٱلْمُفْسِدِينَ
  Unverified discovery rationale: terra: Whenever people kindle a fire for war Allah extinguishes it; a human-lit fire here has a destructive purpose and is put out rather than followed as a guide.
- (7:50) [luna: contrast; basis: contrast+scene] وَنَادَىٰٓ أَصْحَٰبُ ٱلنَّارِ أَصْحَٰبَ ٱلْجَنَّةِ أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ ۚ قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The people of the Fire ask the people of the Garden for water or some of God's provision. This reverses the small fire's function as provision for wilderness travelers in 56:73: the condemned occupants have neither the sustaining use nor relief associated with fire's earthly use.
- (21:69) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] قُلْنَا يَٰنَارُ كُونِى بَرْدًۭا وَسَلَٰمًا عَلَىٰٓ إِبْرَٰهِيمَ
  Unverified discovery rationale: luna: Abraham is commanded that the fire be coolness and peace for him. With the same object as the punitive great Fire, this is a direct reversal: burning is an effect of one fire-scene, not an invariable property of every fire in the section's Quranic image. | terra: The fire meant to burn Abraham is commanded to be cool and safe, marking the boundary between fire's heat and what Allah can make that same object do.
- (21:101) [terra: contrast; basis: contrast+scene+theme] إِنَّ ٱلَّذِينَ سَبَقَتْ لَهُم مِّنَّا ٱلْحُسْنَىٰٓ أُو۟لَٰٓئِكَ عَنْهَا مُبْعَدُونَ
  Unverified discovery rationale: terra: Those already promised the best are kept far away from Hell, a nonlexical counterpart to the atqā being made to avoid the fire.
- (24:40) [terra: contrast; basis: contrast+root+theme] أَوْ كَظُلُمَٰتٍۢ فِى بَحْرٍۢ لُّجِّىٍّۢ يَغْشَىٰهُ مَوْجٌۭ مِّن فَوْقِهِۦ مَوْجٌۭ مِّن فَوْقِهِۦ سَحَابٌۭ ۚ ظُلُمَٰتٌۢ بَعْضُهَا فَوْقَ بَعْضٍ إِذَآ أَخْرَجَ يَدَهُۥ لَمْ يَكَدْ يَرَىٰهَا ۗ وَمَن لَّمْ يَجْعَلِ ٱللَّهُ لَهُۥ نُورًۭا فَمَا لَهُۥ مِن نُّورٍ
  Unverified discovery rationale: terra: The layered-darkness image ends by denying any light to one for whom Allah makes none, setting a limit on the guiding illumination displayed in 24:35.
- (39:73) [terra: contrast; basis: contrast+scene+theme] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
  Unverified discovery rationale: terra: The God-fearing are driven to the garden in groups, giving the opposite destination and reception to those driven toward Hell in 39:71.
- (57:13) [terra: contrast; basis: contrast+neighbour+root+theme] يَوْمَ يَقُولُ ٱلْمُنَٰفِقُونَ وَٱلْمُنَٰفِقَٰتُ لِلَّذِينَ ءَامَنُوا۟ ٱنظُرُونَا نَقْتَبِسْ مِن نُّورِكُمْ قِيلَ ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًۭا فَضُرِبَ بَيْنَهُم بِسُورٍۢ لَّهُۥ بَابٌۢ بَاطِنُهُۥ فِيهِ ٱلرَّحْمَةُ وَظَٰهِرُهُۥ مِن قِبَلِهِ ٱلْعَذَابُ
  Unverified discovery rationale: terra: Hypocrites ask believers to wait so they can take some of their light, but are told to go back and seek light; visible light no longer offers a route they can join.
- (57:19) [terra: contrast; basis: contrast+root+theme] وَٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَرُسُلِهِۦٓ أُو۟لَٰٓئِكَ هُمُ ٱلصِّدِّيقُونَ ۖ وَٱلشُّهَدَآءُ عِندَ رَبِّهِمْ لَهُمْ أَجْرُهُمْ وَنُورُهُمْ ۖ وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَحِيمِ
  Unverified discovery rationale: terra: One ayah assigns believers their light and sign-deniers the blazing fire, making the section's etymologically related light and fire the two opposed outcomes.
- (66:6) [terra: contrast; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌۭ شِدَادٌۭ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ
  Unverified discovery rationale: terra: Believers are told to protect themselves and their families from a fire fueled by people and stones; this reverses Moses's search for a small fire to warm his waiting family.
- (79:24) [terra: contrast (missing-ayat turn); basis: contrast+speaker+theme] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
  Unverified discovery rationale: terra: Pharaoh answers Moses by claiming to be the people's lord most high; this is the blasphemous reversal of the true Lord who identifies Himself to Moses at the fire and is ٱلْأَعْلَىٰ in 87:1.
- (85:5) [terra: contrast; basis: contrast+neighbour+scene] ٱلنَّارِ ذَاتِ ٱلْوَقُودِ
  Unverified discovery rationale: terra: The trench is identified by its fuel-fed fire, setting up a humanly kindled flame used for persecution rather than guidance, warmth, or reminder.
- (85:6) [terra: contrast; basis: contrast+neighbour+scene] إِذْ هُمْ عَلَيْهَا قُعُودٌۭ
  Unverified discovery rationale: terra: The persecutors sit around the trench fire, a moral reversal of the blessed presence around Moses's fire in 27:8.
- (85:7) [terra: contrast; basis: contrast+neighbour+scene] وَهُمْ عَلَىٰ مَا يَفْعَلُونَ بِٱلْمُؤْمِنِينَ شُهُودٌۭ
  Unverified discovery rationale: terra: Those around the trench witness what is done to the believers in the fire; the same positions 'in' and 'around' a fire carry the opposite moral relation from 27:8.
- (107:4) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+root+theme] فَوَيْلٌۭ لِّلْمُصَلِّينَ
  Unverified discovery rationale: terra: Woe is pronounced upon people described as praying, marking a boundary around the section's positive prayer figure: the mere outward category can also be condemned.
- (107:5) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+root+theme] ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
  Unverified discovery rationale: terra: Those condemned worshipers are heedless of their prayer, clarifying why the section pairs prayer with remembering the Lord's name.

## neighbours: within two ayat of a passage the section cites (34)

- (4:54) [next to 4:56] أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۖ فَقَدْ ءَاتَيْنَآ ءَالَ إِبْرَٰهِيمَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَءَاتَيْنَٰهُم مُّلْكًا عَظِيمًۭا
- (4:55) [next to 4:56] فَمِنْهُم مَّنْ ءَامَنَ بِهِۦ وَمِنْهُم مَّن صَدَّ عَنْهُ ۚ وَكَفَىٰ بِجَهَنَّمَ سَعِيرًا
- (4:57) [next to 4:56] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (4:58) [next to 4:56] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
- (20:8) [next to 20:10] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:9) [next to 20:10] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:15) [next to 20:13] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (20:16) [next to 20:14] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (20:21) [next to 20:23] قَالَ خُذْهَا وَلَا تَخَفْ ۖ سَنُعِيدُهَا سِيرَتَهَا ٱلْأُولَىٰ
- (20:22) [next to 20:23] وَٱضْمُمْ يَدَكَ إِلَىٰ جَنَاحِكَ تَخْرُجْ بَيْضَآءَ مِنْ غَيْرِ سُوٓءٍ ءَايَةً أُخْرَىٰ
- (20:24) [next to 20:23] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (20:25) [next to 20:23] قَالَ رَبِّ ٱشْرَحْ لِى صَدْرِى
- (27:5) [next to 27:7] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَهُمْ سُوٓءُ ٱلْعَذَابِ وَهُمْ فِى ٱلْءَاخِرَةِ هُمُ ٱلْأَخْسَرُونَ
- (27:6) [next to 27:7] وَإِنَّكَ لَتُلَقَّى ٱلْقُرْءَانَ مِن لَّدُنْ حَكِيمٍ عَلِيمٍ
- (27:10) [next to 27:8] وَأَلْقِ عَصَاكَ ۚ فَلَمَّا رَءَاهَا تَهْتَزُّ كَأَنَّهَا جَآنٌّۭ وَلَّىٰ مُدْبِرًۭا وَلَمْ يُعَقِّبْ ۚ يَٰمُوسَىٰ لَا تَخَفْ إِنِّى لَا يَخَافُ لَدَىَّ ٱلْمُرْسَلُونَ
- (28:27) [next to 28:29] قَالَ إِنِّىٓ أُرِيدُ أَنْ أُنكِحَكَ إِحْدَى ٱبْنَتَىَّ هَٰتَيْنِ عَلَىٰٓ أَن تَأْجُرَنِى ثَمَٰنِىَ حِجَجٍۢ ۖ فَإِنْ أَتْمَمْتَ عَشْرًۭا فَمِنْ عِندِكَ ۖ وَمَآ أُرِيدُ أَنْ أَشُقَّ عَلَيْكَ ۚ سَتَجِدُنِىٓ إِن شَآءَ ٱللَّهُ مِنَ ٱلصَّٰلِحِينَ
- (28:28) [next to 28:29] قَالَ ذَٰلِكَ بَيْنِى وَبَيْنَكَ ۖ أَيَّمَا ٱلْأَجَلَيْنِ قَضَيْتُ فَلَا عُدْوَٰنَ عَلَىَّ ۖ وَٱللَّهُ عَلَىٰ مَا نَقُولُ وَكِيلٌۭ
- (28:31) [next to 28:29] وَأَنْ أَلْقِ عَصَاكَ ۖ فَلَمَّا رَءَاهَا تَهْتَزُّ كَأَنَّهَا جَآنٌّۭ وَلَّىٰ مُدْبِرًۭا وَلَمْ يُعَقِّبْ ۚ يَٰمُوسَىٰٓ أَقْبِلْ وَلَا تَخَفْ ۖ إِنَّكَ مِنَ ٱلْءَامِنِينَ
- (56:69) [next to 56:71] ءَأَنتُمْ أَنزَلْتُمُوهُ مِنَ ٱلْمُزْنِ أَمْ نَحْنُ ٱلْمُنزِلُونَ
- (56:70) [next to 56:71] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
- (56:75) [next to 56:73] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (74:24) [next to 74:26] فَقَالَ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ يُؤْثَرُ
- (74:25) [next to 74:26] إِنْ هَٰذَآ إِلَّا قَوْلُ ٱلْبَشَرِ
- (74:27) [next to 74:26] وَمَآ أَدْرَىٰكَ مَا سَقَرُ
- (74:30) [next to 74:28] عَلَيْهَا تِسْعَةَ عَشَرَ
- (74:41) [next to 74:43] عَنِ ٱلْمُجْرِمِينَ
- (88:2) [next to 88:4] وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- (88:3) [next to 88:4] عَامِلَةٌۭ نَّاصِبَةٌۭ
- (88:5) [next to 88:4] تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- (88:6) [next to 88:4] لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- (88:25) [next to 88:24] إِنَّ إِلَيْنَآ إِيَابَهُمْ
- (88:26) [next to 88:24] ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم
- (92:13) [next to 92:15] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (92:19) [next to 92:17] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 87, "section": 8, "run_tag": "sol-session-20261005", "source_sha256": "5e9ef0a461cc99bfb9b4c0e1b4609dd85b292c96610df2a0bb8cfe5bd670daa3", "list_sha256": "83e3f0c7cec2ea04eba6b8175e1037bd55e587c1db8a7ae84b64042c577969e6", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec8/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 14, "unique_additions": 14, "repeated_proposals": [], "turn1_sha256": "93d08e33ed91ad5255827926e04f380f158aebdf6a60b8b54a49fc84b619abb2", "followup_sha256": "3bda7be863a21c6f85c8b11288b602fc7eae6a7ebbeae7de203354d1b38cd9dc", "proposal_file": "followup.tsv", "proposal_sha256": "3bda7be863a21c6f85c8b11288b602fc7eae6a7ebbeae7de203354d1b38cd9dc", "list_sha256": "5907a1f2f59599a0f58e95177b5a9d72328dce8e4f5d21fb128a93075079b3e3", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec8/luna/list.tsv", "rows": 58, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 2, "ref": "27:7", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 3, "ref": "28:29", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 7, "ref": "74:26", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 12, "ref": "4:56", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 44, "ref": "9:35", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec8/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 61, "unique_additions": 61, "repeated_proposals": [], "turn1_sha256": "641abf97a66d1d86ca496e507107ab93a004c5342f824f7fc9fd8fcc22da6326", "followup_sha256": "55dd943c769a3fc5cd2f795af9c0754f88b1c3fb3342197d188cee223b29a324", "proposal_file": "followup.tsv", "proposal_sha256": "55dd943c769a3fc5cd2f795af9c0754f88b1c3fb3342197d188cee223b29a324", "list_sha256": "49b371b3a124ca7b8751b991c9771245af5a84b82e25794285ce8f6d72c4dfb8", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec8/terra/list.tsv", "rows": 159, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 2, "ref": "27:7", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 14, "ref": "4:56", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 15, "ref": "11:69", "arabic": "عِجْلٍ حَنِيذٍ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 18, "ref": "74:28", "arabic": "ب ق ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 20, "ref": "74:35", "arabic": "إِحْدَى ٱلْكُبَرِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 20, "ref": "74:35", "arabic": "ٱلنَّارَ ٱلْكُبْرَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["87:12"], "matching_ref_count": 1}, {"line": 26, "ref": "92:18", "arabic": "تَزَكَّىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 27, "ref": "88:4", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 39, "ref": "70:23", "arabic": "فَصَلَّىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 49, "ref": "3:185", "arabic": "قَدْ أَفْلَحَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["20:64", "23:1", "87:14", "91:9"], "matching_ref_count": 4}, {"line": 67, "ref": "19:52", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 94, "ref": "19:59", "arabic": "ص ل و", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 100, "ref": "24:37", "arabic": "ص ل و", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 100, "ref": "24:37", "arabic": "نُور", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 100, "ref": "24:37", "arabic": "نَار", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 109, "ref": "56:94", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 121, "ref": "70:21", "arabic": "إِلَّا ٱلْمُصَلِّينَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["70:22"], "matching_ref_count": 1}, {"line": 126, "ref": "92:7", "arabic": "يُسْرَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 135, "ref": "82:15", "arabic": "ص ل ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

