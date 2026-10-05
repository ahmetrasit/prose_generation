Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 7 of 18 ("Damga: deriye basılan iz"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 7 (prose paragraphs numbered) =====
[¶28] Daha önce anılan ikinci türetme, birinci ayetteki "ad" kelimesini وسم köküne, yani damgaya bağlar. Bu kök kimliği tartışmalıdır, ama yolun sonundaki sahne açıktır: {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmu eseru keyyin ve baîrun mevsûmun vusime bi-simetin yu'rafu bihâ min kat'ı uẕunin ev keyy, gloss:vesm dağlama izidir; damgalı deve kulak kesiği ya da dağlama gibi tanındığı bir işaretle işaretlenmiştir, source:"و س م,B001"}. Damgayı basan alet de bu köktendir: {ar:الميسم المكواة أو الشيء الذي يوسم به الدواب, tr:el-mîsem el-mikvâtu evi'ş-şey'u'lleẕî yûsemu bihi'd-devâbb, gloss:mîsem dağlama demiri ya da hayvanların işaretlendiği aletidir, source:"و س م,B001"}. "İz" diye çevrilen أثر, on altıncı ayetteki تُؤْثِرُونَ kelimesinin köküdür. Damganın sahibi rabdir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi sahibidir, source:"ر ب ب,B001"}. Ad, bu sahnede bir şeyin kime ait olduğunu gösteren ve onu ötekilerden ayıran işarettir. "Rabbinin adını tesbih et" emri, düz anlamının yanında, Rabbin işaretini her türlü kusurdan arınmış tutma emri olarak da duyulur.

[¶29] Surenin başka kelimeleri aynı sahneye girer. On ikinci ayetteki "ateş" kelimesi damganın kendisi için de kullanılır: {ar:ما نار هذه الناقة أي ما سمتها؛ نجارها نارها, tr:mâ nâru hâẕihi'n-nâkati ey mâ simetuhâ nicâruhâ nâruhâ, gloss:bu devenin nârı nedir yani damgası nedir; soyu damgasından bellidir, source:"ن و ر,B002"}. Bu ifade ateş ile damganın kökünü tek cümlede birleştirir. On altıncı ayetteki kökün ailesinde devenin ayağına basılan iz de vardır: {ar:المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض, tr:el-mi'ŝera hadîdetun yu'ŝeru bihâ huffu'l-baîri li-yu'rafe eseruhû fi'l-ard, gloss:mi'ŝera devenin tabanına iz basılan demirdir; böylece yerdeki izi tanınır, source:"ء ث ر,B008"}. İz, bir şeyden geriye kalandır: {ar:الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة, tr:el-eser bakıyyetu mâ yurâ min kulli şey'in ve mâ lâ yurâ ba'de en tebkâ fîhi alaka, gloss:eser her şeyden görünen ya da görünmeyip bir ilişiği kalan artıktır, source:"ء ث ر,B003"}. Bu tanım on altıncı ayetin kökünü on yedinci ayetin köküne bağlar. Yedinci ayetteki "bilir" fiilinin kökü de ayırt edici işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu alâ eserin bi'ş-şey'i yetemeyyezu bihî an ğayrih, gloss:bir şeyi ötekilerden ayıran iz anlamında tek bir köktür, source:"ع ل م,B002"}. Damga yüzde de okunur: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtu fîhi'l-hayra ve'ş-şerra ey raeytu fîhi eseren, gloss:onda iyiliği ya da kötülüğü sezdim yani onda bir iz gördüm, source:"و س م,B002"}. Bu ifade on yedinci ayetteki "hayırlı" kelimesinin kökünü de içerir.

[¶30] Düz bir okuma, on altıncı ayetteki "tercih edersiniz" fiilini yalnızca bir eğilim olarak görür. Damga sahnesi, aynı kökün iz bırakmak ve izden tanınmak demek olduğunu duyurur. Tercih edilen şey kişide bir iz bırakır ve kişi o izden tanınır. Sure bu izi iki türlü gösterir: birinde Rabbin adı anılır, ötekinde ateş vardır.

[¶31] Kur'an damgayı bir tehdit olarak kullanır. Allah Peygamber'e çok yemin eden, aşağılık, söz taşıyan kişiye uymamasını söyler. Bu kişi ayetler okunduğunda {ar:أَسَٰطِيرُ ٱلْأَوَّلِينَ, tr:esâtîru'l-evvelîn, gloss:öncekilerin masalları, source:68:15} der, ve hükmü şudur: {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimuhû ale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. "Öncekiler" kelimesi surenin on sekizinci ayetindeki "ilk sayfalar"ın köküdür. İlk sayfaları masal sayan kişi damgalanır. Lut kavmini sabahleyin çığlık yakalayıp şehirlerinin altı üstüne getirildikten sonra şöyle denir: {ar:إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْمُتَوَسِّمِينَ, tr:inne fî ẕâlike le-âyâtin li'l-mutevessimîn, gloss:bunda işaretleri okuyanlar için ibretler vardır, source:15:75}. Yıkılmış bir yerden iz okumak, damganın öbür yüzüdür. Peygamber'in arkadaşları için de {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:işaretleri yüzlerindedir; secdenin izinden, source:48:29} denir. Buradaki سيما başka bir köke yazılır, bu yüzden kök kimliği kurmaz. Ama yanındaki أثر, on altıncı ayetin köküdür, ve iz burada namazın bıraktığı izdir.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (210) =====
## strong (117)

- (2:7) [terra: strong (missing-ayat turn); basis: scene+theme] خَتَمَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَعَلَىٰ سَمْعِهِمْ ۖ وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
  Unverified discovery rationale: terra: God seals the disbelievers' hearts and hearing and places a covering on sight; rejection becomes an identifying divine impression upon the faculties that sustained it.
- (2:31) [luna: strong; terra: medium; basis: root+theme] وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَٰٓؤُلَآءِ إِن كُنتُمْ صَٰدِقِينَ
  Unverified discovery rationale: luna: The section's proposed sense of ٱسْم as a distinguishing mark meets the naming of every thing to Adam; names separate and identify what is otherwise undifferentiated. | terra: God teaches Adam the names and asks that the named things be identified, giving اسم the practical work of distinguishing one thing from another.
- (2:138) [luna: medium; terra: strong; basis: scene+theme] صِبْغَةَ ٱللَّهِ ۖ وَمَنْ أَحْسَنُ مِنَ ٱللَّهِ صِبْغَةًۭ ۖ وَنَحْنُ لَهُۥ عَٰبِدُونَ
  Unverified discovery rationale: luna: صبغة الله, God's dye, gives the believers a marked identity; it is a specific metaphor for belonging, though not the section's proposed root for ٱسْم. | terra: صِبْغَةَ ٱللَّهِ presents God's dye or coloring as an identity of worship and belonging, a close nonlexical counterpart to the Lord's mark borne by His own.
- (2:248) [terra: strong (missing-ayat turn); basis: scene+theme] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ءَايَةَ مُلْكِهِۦٓ أَن يَأْتِيَكُمُ ٱلتَّابُوتُ فِيهِ سَكِينَةٌۭ مِّن رَّبِّكُمْ وَبَقِيَّةٌۭ مِّمَّا تَرَكَ ءَالُ مُوسَىٰ وَءَالُ هَٰرُونَ تَحْمِلُهُ ٱلْمَلَٰٓئِكَةُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: terra: The ark contains a remnant left by the houses of Moses and Aaron and is itself a sign of rightful kingship; surviving objects identify a divinely appointed owner and relation.
- (2:273) [luna: medium; terra: strong; basis: contrast+scene+theme] لِلْفُقَرَآءِ ٱلَّذِينَ أُحْصِرُوا۟ فِى سَبِيلِ ٱللَّهِ لَا يَسْتَطِيعُونَ ضَرْبًۭا فِى ٱلْأَرْضِ يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ مِنَ ٱلتَّعَفُّفِ تَعْرِفُهُم بِسِيمَٰهُمْ لَا يَسْـَٔلُونَ ٱلنَّاسَ إِلْحَافًۭا ۗ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌ
  Unverified discovery rationale: luna: Restrained poor people are recognized by their marks even though they do not beg; this is a compassionate, positive counterpart to a punitive brand. | terra: تَعْرِفُهُم بِسِيمَاهُمْ directs the giver to recognize the restrained poor by their sign despite their refusal to ask, so an unspoken condition is read from a trace.
- (3:14) [luna: medium (missing-ayat turn); terra: strong; basis: root+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The list of worldly attractions includes wealth, livestock, and fields, all described as enjoyment of near life while the good return is with Allah; it gives concrete objects one may prefer over what remains. | terra: ٱلْخَيْلِ ٱلْمُسَوَّمَةِ places marked or branded horses inside the adornments of worldly life, then calls all of them temporary enjoyment; it joins the section's animal brand directly to its reading of preferring الدنيا.
- (4:119) [luna: strong; terra: strong; basis: contrast+scene+theme] وَلَأُضِلَّنَّهُمْ وَلَأُمَنِّيَنَّهُمْ وَلَءَامُرَنَّهُمْ فَلَيُبَتِّكُنَّ ءَاذَانَ ٱلْأَنْعَٰمِ وَلَءَامُرَنَّهُمْ فَلَيُغَيِّرُنَّ خَلْقَ ٱللَّهِ ۚ وَمَن يَتَّخِذِ ٱلشَّيْطَٰنَ وَلِيًّۭا مِّن دُونِ ٱللَّهِ فَقَدْ خَسِرَ خُسْرَانًۭا مُّبِينًۭا
  Unverified discovery rationale: luna: The section's brand lexicon says an animal can be recognized by an ear cut or a burn; this ayah names cutting livestock ears as a satanic practice, a reversal of an identifying mark. | terra: Satan's command that people slit the ears of livestock stages the section's exact alternative to cautery for marking an animal, while exposing a mark that falsely alters God's creation.
- (5:4) [luna: strong (missing-ayat turn); terra: medium; basis: scene+theme] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: The trained hunting animal catches prey, and Allah's name is mentioned over the catch; this is another specific case where the name marks an animal as lawfully dedicated to its Lord. | terra: Hunters are told to mention God's name over what trained animals catch, using the name to identify the lawful relation among owner, animal, and food.
- (6:59) [luna: strong (missing-ayat turn); basis: root+scene+theme] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: Allah knows every fallen leaf and every seed hidden in the earth; the root ع ل م from the section meets its concern with visible and hidden traces in a specific scene of plant remains.
- (6:118) [luna: strong; terra: strong; basis: scene+theme] فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ إِن كُنتُم بِـَٔايَٰتِهِۦ مُؤْمِنِينَ
  Unverified discovery rationale: luna: The verse says to eat what has Allah's name mentioned over it; spoken naming marks the animal as dedicated to its true owner. | terra: Eating what God's name has been mentioned over makes the name a practical sign of lawful dedication, close to the section's ownership-mark reading of اسم.
- (6:119) [luna: strong (missing-ayat turn); basis: neighbour+theme] وَمَا لَكُمْ أَلَّا تَأْكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ وَقَدْ فَصَّلَ لَكُم مَّا حَرَّمَ عَلَيْكُمْ إِلَّا مَا ٱضْطُرِرْتُمْ إِلَيْهِ ۗ وَإِنَّ كَثِيرًۭا لَّيُضِلُّونَ بِأَهْوَآئِهِم بِغَيْرِ عِلْمٍ ۗ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِٱلْمُعْتَدِينَ
  Unverified discovery rationale: luna: This ayah continues 6:118 by asking why people would not eat what has Allah's name mentioned over it and clarifying the exception; it spells out the boundary conveyed by naming the offering.
- (6:121) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ وَإِنَّهُۥ لَفِسْقٌۭ ۗ وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ ۖ وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ
  Unverified discovery rationale: luna: The inverse boundary is explicit: an animal without Allah's name mentioned over it is not to be eaten, and the verse associates that omission with disobedience and satanic prompting. | terra: The prohibition on eating what God's name was not mentioned over draws a boundary between two allegiances; an animal without the true owner's name becomes a site of satanic dispute.
- (6:136) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+scene+theme] وَجَعَلُوا۟ لِلَّهِ مِمَّا ذَرَأَ مِنَ ٱلْحَرْثِ وَٱلْأَنْعَٰمِ نَصِيبًۭا فَقَالُوا۟ هَٰذَا لِلَّهِ بِزَعْمِهِمْ وَهَٰذَا لِشُرَكَآئِنَا ۖ فَمَا كَانَ لِشُرَكَآئِهِمْ فَلَا يَصِلُ إِلَى ٱللَّهِ ۖ وَمَا كَانَ لِلَّهِ فَهُوَ يَصِلُ إِلَىٰ شُرَكَآئِهِمْ ۗ سَآءَ مَا يَحْكُمُونَ
  Unverified discovery rationale: luna: People assign portions of crops and cattle to God and partners, then misdirect them; this exposes false claims of ownership against the section's true Lord. | terra: People allocate crops and livestock between God and their alleged partners, staging rival claims of ownership that the section's true Lord-mark is meant to distinguish.
- (6:138) [terra: strong; basis: scene+theme] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
  Unverified discovery rationale: terra: The pagans invent livestock restrictions and animals عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ over which God's name is not mentioned; the absent name exposes a counterfeit claim of ownership and consecration.
- (6:162) [luna: strong; terra: medium; basis: root+scene+speaker+theme] قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: Prayer, sacrifice, life, and death are declared for Allah, Lord of the worlds; this makes the section's owner-mark concrete as a whole life identified with its Lord. | terra: Prayer, sacrifice, life, and death are declared لِلَّهِ رَبِّ ٱلْعَـٰلَمِينَ; the whole self and its animal offering are assigned to the named Lord-owner.
- (6:164) [terra: strong; basis: root+theme] قُلْ أَغَيْرَ ٱللَّهِ أَبْغِى رَبًّۭا وَهُوَ رَبُّ كُلِّ شَىْءٍۢ ۚ وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
  Unverified discovery rationale: terra: وَهُوَ رَبُّ كُلِّ شَىْءٍ states the section's lexicographic claim almost verbatim: the sought Lord is the Lord and owner of every thing.
- (7:46) [luna: strong; terra: strong; basis: neighbour+scene+theme] وَبَيْنَهُمَا حِجَابٌۭ ۚ وَعَلَى ٱلْأَعْرَافِ رِجَالٌۭ يَعْرِفُونَ كُلًّۢا بِسِيمَىٰهُمْ ۚ وَنَادَوْا۟ أَصْحَٰبَ ٱلْجَنَّةِ أَن سَلَٰمٌ عَلَيْكُمْ ۚ لَمْ يَدْخُلُوهَا وَهُمْ يَطْمَعُونَ
  Unverified discovery rationale: luna: People on the heights recognize each group by its marks; 7:48 continues their address to those recognized, a direct scene of identity read from signs. | terra: The people on the Heights يَعْرِفُونَ كُلًّۢا بِسِيمَاهُمْ, recognizing every group by its marks; the sign visibly distinguishes belonging and fate.
- (7:48) [luna: strong; terra: strong; basis: neighbour+scene+theme] وَنَادَىٰٓ أَصْحَٰبُ ٱلْأَعْرَافِ رِجَالًۭا يَعْرِفُونَهُم بِسِيمَىٰهُمْ قَالُوا۟ مَآ أَغْنَىٰ عَنكُمْ جَمْعُكُمْ وَمَا كُنتُمْ تَسْتَكْبِرُونَ
  Unverified discovery rationale: luna: The men of the heights call people they recognize by their marks; the dialogue completes 7:46's image of a sign distinguishing persons. | terra: The people on the Heights address men whom they know بِسِيمَاهُمْ; this continuation shows a mark identifying particular persons even before their final admission is announced.
- (7:71) [luna: strong (missing-ayat turn); terra: contrast (missing-ayat turn); basis: contrast+root+theme] قَالَ قَدْ وَقَعَ عَلَيْكُم مِّن رَّبِّكُمْ رِجْسٌۭ وَغَضَبٌ ۖ أَتُجَٰدِلُونَنِى فِىٓ أَسْمَآءٍۢ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّا نَزَّلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍۢ ۚ فَٱنتَظِرُوٓا۟ إِنِّى مَعَكُم مِّنَ ٱلْمُنتَظِرِينَ
  Unverified discovery rationale: luna: Hud challenges the people over names they and their fathers assigned without God's authority; the section's name-as-mark reading meets a boundary where naming cannot establish rightful ownership. | terra: Hūd calls the alleged deities mere names coined by the people and their fathers without authority, exposing labels that claim sacred identity but bear no true owner's warrant.
- (7:180) [luna: strong; terra: strong; basis: root+speaker+theme] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: Allah owns the most beautiful names and is invoked by them; the command to leave those who distort His names parallels the section's call to keep the Lord's identifying name free of flaw. | terra: God owns the beautiful names and the hearer is told to leave those who distort them; this directly supports hearing “glorify your Lord's name” as keeping His identifying name pure.
