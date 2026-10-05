Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 10 of 14 ("Sürü: sahip, öndeki hayvan, otlak ve başıboş kalan deve"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 10 (prose paragraphs numbered) =====
[¶51] Bir deve sürüsü bir sahibe aittir: {ar:ورب كل شيء مالكه, tr:ve rabbü kulli şey'in mâlikuh, gloss:her şeyin rabbi onun mâlikidir, source:"ر ب ب,B001"}. Sürüdeki develer "nimet" kelimesiyle aynı köktendir, çünkü insana iyilik getirirler: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamü'l-ibil, li-mâ fîhi mine'l-hayri ve'n-ni'me, gloss:neam develerdir, çünkü onlarda hayır ve nimet vardır; en'âm ise hayvanlardır, source:"ن ع م,B005"}. Sürünün kimin olduğunu damga gösterir: {ar:وبعير موسوم وسم بسمة يعرف بها, tr:ve ba'îrun mevsûmun vüsime bi-simetin yu'rafü bihâ, gloss:damgalı deve, tanınacağı bir işaretle damgalanmıştır, source:"و س م,B001"}. Uysallaştırılmış deve katranla sıvanmıştır: {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-mu'abbed, gloss:katranla sıvanmış, uysallaştırılmış deve, source:"ع ب د,B005"}. Sürüde bir öncü yürür ve diğerleri onun ardından gider. Dördüncü ayetteki "mâlik" kelimesinin ailesi bu öncüye ad verir: {ar:ملك الإبل والشاء ما يتقدم ويتبعه سائره, tr:milkü'l-ibili ve'ş-şâ', gloss:develerin ve koyunların milki, önde giden ve geri kalanların izlediği hayvandır, source:"م ل ك,B008"}. Arıların başındaki arı da böyle anılır: {ar:مليك النحل يعسوبها, tr:melîkü'n-nahli ya'sûbühâ, gloss:arıların melîki, onların beyidir, source:"م ل ك,B008"}. Altıncı ayetteki "ihdinâ" kelimesinin ailesi de aynı öncüye ad verir: {ar:هوادي الوحش متقدماتها الهادية لغيرها, tr:hevâdi'l-vahşi mütekaddimâtühe'l-hâdiyetü li-gayrihâ, gloss:yabani hayvanların hâdîleri, en önde gidip diğerlerine yol gösterenlerdir, source:"ه د ي,B003"}, {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelü ra'îl, gloss:atların hâdîleri boyunlarıdır ya da ilk bölükleridir, source:"ه د ي,B003"}. Bir cümle bu iki kökü tek bir binek hayvanında birleştirir: {ar:ملك الدابة قوائمها وهاديها, tr:milkü'd-dâbbeti kavâimühâ ve hâdîhâ, gloss:binek hayvanının milki, ayakları ve boynudur, source:"م ل ك,B008"}. Binek ayaklarıyla taşır, boynuyla yönlendirilir. Sürü bağlı olduğu yerde kalır: {ar:مرب الإبل حيث لزمته, tr:merabbü'l-ibil, gloss:develerin merabbı, ayrılmadıkları yerdir, source:"ر ب ب,B007"}. O yerin otlağı beğenilir: {ar:أحمدت الأرض إذا رضيت سكناها أو مرعاها, tr:ahmedtü'l-ard, gloss:toprağın otlağından hoşnut kaldım, source:"ح م د,B002"}.

[¶52] Sonra bir deve kopar gider: {ar:أضل بعيره إذا أفلت فذهب, tr:edalle ba'îrah, gloss:devesini yitirdi, yani deve kurtulup gitti, source:"ض ل ل,B003"}, {ar:أضللت بعيري إذا ذهب منك, tr:edlaltü ba'îrî, gloss:devemi yitirdim, elimden gitti, source:"ض ل ل,B003"}. Başıboş kalan deve şöyle tanımlanır: {ar:الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء, tr:ed-dâlletü mine'l-ibili mâ yebkâ bi-medî'atin lâ yu'rafü rabbühâ, gloss:dâlle, ıssız bir yerde kalan ve sahibi bilinmeyen devedir; erkeği de dişisi de böyledir, source:"ض ل ل,B005"}. Başka bir tanım da onu sahibiyle anar: {ar:الضالة من الإبل التي بمضيعة لا يعرف لها مالك, tr:ed-dâlletü mine'l-ibili'lletî bi-medî'atin lâ yu'rafü lehâ mâlik, gloss:dâlle, ıssız bir yerde kalan ve sahibi bilinmeyen devedir, source:"ض ل ل,B005"}. Bu iki tanım, yedinci ayetin son kelimesini ikinci ayetin "Rab" kelimesine ve dördüncü ayetin "mâlik" kelimesine bağlar. Surenin sahibe verdiği iki ad, başıboş devenin tanımında "bilinmeyen" olarak geri döner. Sahipli sürünün dışında, kimsenin olmayan yabani sürüler koşar. Yaban sığırı sürüsü {ar:الربرب: القطيع من بقر الوحش, tr:er-rabrab: el-katî'u min bakari'l-vahş, gloss:rabrab, yaban sığırı sürüsüdür, source:"ر ب ب,B014"} diye, yaban eşeği sürüsü de {ar:العانة القطيع من حمر الوحش, tr:el-ânetü'l-katî'u min humuri'l-vahş, gloss:âne, yaban eşeği sürüsüdür, source:"ع و ن,B006"} diye anılır.

[¶53] Bu görüntü, düz bir mealin "sapanlar" diye geçtiği kelimede bir sahne gösterir: Sahibinden kopmuş, ıssız bir yerde kalmış ve kime ait olduğu bilinmeyen bir hayvan. Altıncı ayetteki istek de bu sahnede bir hareket kazanır. Sürü, önde yürüyen hâdînin ve "milk"in ardından gider. Böylece "bizi ilet" isteği, ardından gidilecek bir öncüyü de ister.

[¶54] Kur'an'da bu sürü, yola dair bir ayetle birlikte anılır. Allah hayvanları yarattığını hatırlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ, tr:ve'l-en'âme halakahâ, leküm fîhâ dif'ün ve menâfi', gloss:hayvanları da yarattı; onlarda sizin için ısınma ve faydalar vardır, source:16:5}. Sürünün sabah otlağa gidişi ve akşam dönüşü güzel bir görüntüdür: {ar:وَلَكُمْ فِيهَا جَمَالٌ حِينَ تُرِيحُونَ وَحِينَ تَسْرَحُونَ, tr:ve leküm fîhâ cemâlün hîne turîhûne ve hîne tesrahûn, gloss:akşam onları getirirken ve sabah salıverirken onlarda sizin için bir güzellik vardır, source:16:6}. Hayvanlar yükü uzak bir yere taşır ve bu sahne Rabbin şefkatiyle kapanır: {ar:إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ, tr:inne rabbeküm le-raûfun rahîm, gloss:Rabbiniz çok şefkatli ve merhametlidir, source:16:7}. Hemen ardından yol konusu açılır: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve alellâhi kasdü's-sebîli ve minhâ câir, gloss:doğru yolu göstermek Allah'a aittir; yollardan bazısı ise yana sapar, source:16:9}. Buradaki "câir" kelimesi, "küllü câirin ani'l-kasdi dâll" tanımıyla aynı kelimedir. Sürüden yola geçiş Kur'an'ın kendi akışında olur. Hayvanların sahibine ait olduğu ve onlara uysallaştırıldığı da söylenir: {ar:أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ, tr:en'âmen fe-hüm lehâ mâlikûn, gloss:sahip oldukları hayvanlar, source:36:71}, {ar:وَذَلَّلْنَٰهَا لَهُمْ, tr:ve zellelnâhâ lehüm, gloss:onları kendilerine boyun eğdirdik, source:36:72}. Bu karşılaştırmanın tersi, insanın sürüden daha başıboş olmasıdır: {ar:أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ, tr:ülâike ke'l-en'âmi bel hüm edall, gloss:onlar hayvanlar gibidir, hatta daha da şaşkındırlar, source:7:179}, {ar:إِنْ هُمْ إِلَّا كَٱلْأَنْعَٰمِ ۖ بَلْ هُمْ أَضَلُّ سَبِيلًا, tr:in hüm illâ ke'l-en'âm, bel hüm edallü sebîlâ, gloss:onlar hayvanlardan başka bir şey değildir, hatta yolca daha da şaşkındırlar, source:25:44}. Hayvan başıboş kalsa da sürüsünü arar, sahibini tanır. Bu ayetlerdeki insan ise yolunu sürüden de daha çok yitirmiştir.

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

===== passages from the discovery list (210) =====
## strong (117)

- (2:21) [terra: strong; basis: root+theme] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: terra: People are commanded to worship their Rabb who created them. The source's `na'budu` and Rabb image is made explicit as a creature's service to its creator-owner.
- (2:38) [luna: strong (missing-ayat turn); terra: medium; basis: root+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: luna: This ayah says those who follow God's guidance need not fear or grieve; it makes following guidance the answer to the section's image of the lost and the led. | terra: Those who follow God's guidance have no fear or grief. The source's lead animal becomes a covenantal pattern: safety belongs to following divine direction.
- (2:71) [luna: contrast; terra: strong; basis: contrast+scene] قَالَ إِنَّهُۥ يَقُولُ إِنَّهَا بَقَرَةٌۭ لَّا ذَلُولٌۭ تُثِيرُ ٱلْأَرْضَ وَلَا تَسْقِى ٱلْحَرْثَ مُسَلَّمَةٌۭ لَّا شِيَةَ فِيهَا ۚ قَالُوا۟ ٱلْـَٰٔنَ جِئْتَ بِٱلْحَقِّ ۚ فَذَبَحُوهَا وَمَا كَادُوا۟ يَفْعَلُونَ
  Unverified discovery rationale: luna: The cow here has not been yoked to plow or water a field; it is a boundary case against the section's tamed camel used for work and carrying. | terra: The selected cow is neither subdued to plough nor to irrigate, and has no marking variation. It is a close boundary case for the source's tamed, recognizable working animal.
- (2:196) [terra: strong; basis: root+scene] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: terra: The hady may not be cleared by shaving until it reaches its appointed place. The source's H-D-Y leading form meets its animal-offering sense: a herd animal has a directed destination.
- (5:2) [luna: contrast; terra: strong; basis: contrast+root+scene] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: luna: The source's dictionary form wasm is a mark by which a camel is recognized; this ayah names garlanded sacrificial animals, whose visible marker signals sacred status rather than a human owner. | terra: The ayah protects sacrificial animals and their garlands. The source's branding sign has a close ritual counterpart in publicly marked hady.
- (5:4) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+scene+theme] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: This ayah describes trained hunting animals catching wild game for their human handlers; it puts the section's tamed animal and its unowned wild herds into one specific scene. | terra: Trained hunting animals are taught what to catch for their keeper. Their learned obedience gives a concrete counterpart to the source's tamed animal that follows a leader and serves an owner.
- (5:95) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+root+scene] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْتُلُوا۟ ٱلصَّيْدَ وَأَنتُمْ حُرُمٌۭ ۚ وَمَن قَتَلَهُۥ مِنكُم مُّتَعَمِّدًۭا فَجَزَآءٌۭ مِّثْلُ مَا قَتَلَ مِنَ ٱلنَّعَمِ يَحْكُمُ بِهِۦ ذَوَا عَدْلٍۢ مِّنكُمْ هَدْيًۢا بَٰلِغَ ٱلْكَعْبَةِ أَوْ كَفَّٰرَةٌۭ طَعَامُ مَسَٰكِينَ أَوْ عَدْلُ ذَٰلِكَ صِيَامًۭا لِّيَذُوقَ وَبَالَ أَمْرِهِۦ ۗ عَفَا ٱللَّهُ عَمَّا سَلَفَ ۚ وَمَنْ عَادَ فَيَنتَقِمُ ٱللَّهُ مِنْهُ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
  Unverified discovery rationale: luna: For killed wild game, this ayah prescribes an equivalent from domestic livestock; it explicitly sets wild animals beside managed herd animals. | terra: An expiation is an equivalent offering from livestock reaching the Ka'bah. The hady word-family ties a concrete animal to an appointed, guided destination.
- (5:97) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] ۞ جَعَلَ ٱللَّهُ ٱلْكَعْبَةَ ٱلْبَيْتَ ٱلْحَرَامَ قِيَٰمًۭا لِّلنَّاسِ وَٱلشَّهْرَ ٱلْحَرَامَ وَٱلْهَدْىَ وَٱلْقَلَٰٓئِدَ ۚ ذَٰلِكَ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَأَنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌ
  Unverified discovery rationale: luna: This ayah calls the garlands on sacrificial animals signs; like the source's mark on a camel, they identify an animal, but here the status is sacred protection. | terra: The sacred offerings and garlands are institutions through which people know God's encompassing knowledge. Marked animal offerings serve a public order rather than private possession.
- (5:103) [luna: contrast; terra: strong; basis: contrast+scene] مَا جَعَلَ ٱللَّهُ مِنۢ بَحِيرَةٍۢ وَلَا سَآئِبَةٍۢ وَلَا وَصِيلَةٍۢ وَلَا حَامٍۢ ۙ وَلَٰكِنَّ ٱلَّذِينَ كَفَرُوا۟ يَفْتَرُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ ۖ وَأَكْثَرُهُمْ لَا يَعْقِلُونَ
  Unverified discovery rationale: luna: This ayah rejects customary categories of animals deliberately released from ordinary use; it contrasts an intentionally designated free animal with the section's camel that escapes and loses its known owner. | terra: God rejects invented named statuses for livestock. The ayah challenges fabricated claims that detach animals from the true owner's command.
- (6:38) [luna: medium; terra: strong; basis: root+scene+theme] وَمَا مِن دَآبَّةٍۢ فِى ٱلْأَرْضِ وَلَا طَٰٓئِرٍۢ يَطِيرُ بِجَنَاحَيْهِ إِلَّآ أُمَمٌ أَمْثَالُكُم ۚ مَّا فَرَّطْنَا فِى ٱلْكِتَٰبِ مِن شَىْءٍۢ ۚ ثُمَّ إِلَىٰ رَبِّهِمْ يُحْشَرُونَ
  Unverified discovery rationale: luna: This ayah calls land creatures and birds communities and says they will be gathered to their Lord; it gives the section's wild herds a Qur'anic frame as animal communities. | terra: Land creatures and birds are communities, then gathered to their Rabb. The wild herd is not ownerless in the final sense: even animal communities return to their Lord.
- (6:71) [terra: strong; basis: contrast+scene+theme] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: A person is bewildered on the earth after devils entice him, while companions call him toward guidance. It gives the source's isolated stray scene and a concrete counter-call to a leading guide.
- (6:136) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+scene] وَجَعَلُوا۟ لِلَّهِ مِمَّا ذَرَأَ مِنَ ٱلْحَرْثِ وَٱلْأَنْعَٰمِ نَصِيبًۭا فَقَالُوا۟ هَٰذَا لِلَّهِ بِزَعْمِهِمْ وَهَٰذَا لِشُرَكَآئِنَا ۖ فَمَا كَانَ لِشُرَكَآئِهِمْ فَلَا يَصِلُ إِلَى ٱللَّهِ ۖ وَمَا كَانَ لِلَّهِ فَهُوَ يَصِلُ إِلَىٰ شُرَكَآئِهِمْ ۗ سَآءَ مَا يَحْكُمُونَ
  Unverified discovery rationale: luna: This ayah describes people assigning portions of crops and livestock to God and their partners; it adds a contested claim of ownership to the section's marked herd and unknown owner. | terra: People assign portions of crops and cattle that God created to God and to alleged partners. It contests human redistribution of a herd whose true source-owner is God.
- (6:138) [terra: strong; basis: contrast+scene] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
  Unverified discovery rationale: terra: Invented rules declare certain cattle and crops forbidden and some animals untouchable for riding. This is a direct boundary around who may redefine the herd's use.
- (6:142) [luna: medium; terra: strong; basis: scene+theme] وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا ۚ كُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ وَلَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
