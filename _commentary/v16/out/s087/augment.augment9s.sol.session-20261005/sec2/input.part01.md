Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 2 of 18 ("Sel: köpük gider, su kalır"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 2 (prose paragraphs numbered) =====
[¶10] Beşinci ayetteki غثاء yalnızca kurumuş ot değildir, selin yüzünde yüzen şeydir de. Arapça onu iki ayrı kaba birden koyar: {ar:الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر, tr:el-ğuŝâu ğuŝâu's-seyli ve'l-kıdr mâ yatfahu ve yetefarraku mine'n-nebâti'l-yâbisi ve zebedi'l-kıdr, gloss:ğuŝâ selin de tencerenin de ğuŝâsıdır; kuru bitkiden ve tencere köpüğünden yüzeye taşıp dağılandır, source:"غ ث و,B001"}. Kelime bir atasözü değeri de taşır: {ar:يضرب به المثل فيما يضيع ويذهب غير معتد به, tr:yudrabu bihi'l-meŝelu fî mâ yadîu ve yeẕhebu ğayra mu'teddin bih, gloss:kaybolup giden ve hesaba katılmayan şey için örnek olarak anılır, source:"غ ث و,B004"}. Selin öbür yüzü sudur. Surenin kelimelerinin aileleri suyun nerede toplanıp kaldığını gösterir.

[¶11] İkinci ayetteki "yarattı" fiilinin ailesinde kayalardaki oyuklar vardır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahratin yectemiu fîhi mâu's-semâ, gloss:halîka kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}. Bu oyuklar şöyle de anlatılır: {ar:قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق, tr:kılâten tumsiku mâe's-sehâbi fî safâtin halakahallâhu fîhâ tusemmîhe'l-arabu'l-halâik, gloss:Allah'ın düz kayada yarattığı ve bulut suyunu tutan çukurlar; Araplar onlara halâik der, source:"خ ل ق,B011"}. Beşinci ayetteki أحوى'nın ailesinde selin doldurduğu kıvrımlı çukurlar vardır: {ar:الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل, tr:el-havâyâ elletî tekûnu fi'l-kîâni ve'r-riyâdi hafâiru multeviyetun yemleuhâ mâu's-seyl, gloss:havâyâ düzlüklerde ve çayırlarda selin doldurduğu kıvrımlı çukurlardır, source:"ح و ي,B008"}. "Rab" kelimesinin ailesinde bol su, toplandığı için bu adı alır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabeb ve huve'l-mâu'l-keŝîr sumiye bi-ẕâlike li-ictimâih, gloss:rabeb boldur ve toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Yedinci ayetteki "açık" kelimesinin ailesinde kuyu temizlenir: {ar:جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو, tr:cehertu'r-rakiyye iẕâ kâne mâuhâ kad ğattâhu't-tînu fe-nakkâ ẕâlike hattâ yezhera'l-mâu ve yesfû, gloss:suyunu çamur örtmüş kuyuyu su görünüp duruluncaya kadar temizledim, source:"ج ه ر,B008"}. Aynı ayetteki "bilir" fiilinin ailesinde de suyu bol kuyu vardır: {ar:العيلم البئر الكثيرة الماء, tr:el-aylem el-bi'ru'l-keŝîratu'l-mâ, gloss:aylem suyu bol kuyudur, source:"ع ل م,B005"}.

[¶12] Dokuzuncu ayet öğütten "fayda verirse" diye söz eder, on yedinci ayet ahireti "daha kalıcı" diye niteler. Fayda, {ar:ما يستعان به في الوصول إلى الخيرات, tr:mâ yusteânu bihî fi'l-vusûli ile'l-hayrât, gloss:iyiliklere ulaşmak için yardım alınan şey, source:"ن ف ع,B001"} diye tanımlanır. Bu tanım on yedinci ayetteki "hayırlı" kelimesinin kökünü de taşır. Kalıcılık ise şudur: {ar:البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء, tr:el-bekâu ŝebâtu'ş-şey'i alâ hâlihi'l-ûlâ ve huve yudâddu'l-fenâ, gloss:bekâ bir şeyin ilk halinde sabit durmasıdır ve yok olmanın zıddıdır, source:"ب ق ي,B001"}. Bu tanımda on sekizinci ayetteki "ilk" kelimesi de vardır.

[¶13] Kur'an'da bu iki yüzü bir sahnede toplayan benzetmeyi Allah verir. Gökten su iner, vadiler {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:fe-sâlet evdiyetun bi-kaderihâ, gloss:vadiler kendi ölçülerince akar, source:13:17}. Burada üçüncü ayetteki "ölçtü" fiilinin kökü geçer. Sel kabarık bir köpük taşır. İnsanların süs ya da eşya için ateşte erittikleri madenin de benzer bir köpüğü vardır. Sonra ayırım gelir: {ar:فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ, tr:fe-emme'z-zebedu fe-yeẕhebu cufâen ve emmâ mâ yenfau'n-nâse fe-yemkuŝu fi'l-ard, gloss:köpük atılıp gider; insanlara fayda veren ise yerde kalır, source:13:17}. Kelime farklıdır, orada غثاء değil زبد geçer. Ama sahne aynıdır. Surenin beşinci, dokuzuncu ve on yedinci ayetlere dağıttığı döküntü, fayda ve kalıcılık bu ayette tek bir selin içinde bir aradadır. Bu yan yana koyuş surenin kendi sözü değildir, ama bu ayet ona Kur'an'dan bir dayanak verir. Fayda verirse sunulan öğüt, kayadaki oyukta tutulan suya benzer. Çerçöp ise akıntıyla gidip hesaba katılmayan şeydir.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (177) =====
## strong (68)

- (2:60) [luna: strong; terra: strong; basis: root+scene+theme] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: luna: The section's dictionary form خَلِيقَة names a rock hollow collecting rain; here water bursts from a struck rock into twelve springs, and each group عَلِمَ its drinking place. The ayah gives both a rock-water scene and the source section's علم family beside an assigned water source. | terra: A struck stone releases twelve springs and each people عَلِمَ its drinking place; this meets both the source dictionary's water-holding rock hollow and its ʿ-l-m family image of a water-rich well.
- (2:164) [terra: strong; basis: root+scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: terra: The same ayah names ships running بِمَا يَنفَعُ ٱلنَّاسَ and water sent from heaven to revive earth, joining the section's root of benefit to beneficial rain.
- (2:264) [luna: strong; terra: contrast; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section distinguishes useful water from what a torrent carries off; this ayah's rain strikes a thinly covered rock and leaves it bare, as a picture of deeds that yield nothing. It makes the loss of apparent benefit concrete. | terra: A downpour strips soil from a smooth rock and leaves it bare, so ostentatious spending yields nothing; this reverses the source image of a rock hollow retaining beneficial rain.
- (2:265) [luna: medium (missing-ayat turn); terra: strong; basis: scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: The section's rock hollows gather rainwater for growth; this ayah pictures a garden on high ground receiving heavy rain or drizzle and yielding double. It is the fruitful counterpart to 2:264's rain-washed bare rock. | terra: A well-placed garden gives doubled produce under a downpour and still yields under drizzle, making retained rain an image of expenditure that truly benefits.
- (6:3) [terra: strong; basis: root+theme] وَهُوَ ٱللَّهُ فِى ٱلسَّمَٰوَٰتِ وَفِى ٱلْأَرْضِ ۖ يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ وَيَعْلَمُ مَا تَكْسِبُونَ
  Unverified discovery rationale: terra: God يَعْلَمُ both سِرَّكُمْ and جَهْرَكُمْ; the roots of “knows” and “manifest” meet in the same open/hidden relation from which the section derives its well image.
- (7:160) [luna: strong; terra: strong; basis: root+scene+theme] وَقَطَّعْنَٰهُمُ ٱثْنَتَىْ عَشْرَةَ أَسْبَاطًا أُمَمًۭا ۚ وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ إِذِ ٱسْتَسْقَىٰهُ قَوْمُهُۥٓ أَنِ ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنۢبَجَسَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۚ وَظَلَّلْنَا عَلَيْهِمُ ٱلْغَمَٰمَ وَأَنزَلْنَا عَلَيْهِمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۚ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
  Unverified discovery rationale: luna: The section's خَلِيقَة is a hollow in rock where water gathers; here twelve springs gush from the rock and each group عَلِمَ its drinking place. The springs emerge rather than collect, but the ayah supplies a close rock-and-water counterpart and the named علم family. | terra: The rock sends out twelve springs and every tribe عَلِمَ its drinking place, again bringing the section's rock cavity, abundant water, and the root of “knows” into one scene.
- (10:24) [luna: strong; terra: strong; basis: contrast+scene+theme] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The section's pasture turns to debris; here rain makes the earth's growth lush, then it is harvested as though it had not flourished the day before. The abrupt loss sharpens the difference between a season's display and what remains. | terra: The parable of worldly life begins with heavenly water and luxuriant growth, then leaves the land harvested as though it had not flourished, emphasizing passing appearance.
- (11:44) [luna: medium; terra: strong; basis: contrast+scene+theme] وَقِيلَ يَٰٓأَرْضُ ٱبْلَعِى مَآءَكِ وَيَٰسَمَآءُ أَقْلِعِى وَغِيضَ ٱلْمَآءُ وَقُضِىَ ٱلْأَمْرُ وَٱسْتَوَتْ عَلَى ٱلْجُودِىِّ ۖ وَقِيلَ بُعْدًۭا لِّلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: The section describes a flood and what its current carries away; after Noah's flood, the earth is told to swallow its water and the sky to stop. This is the flood's recession, a counterpart to the section's gathering and flow. | terra: Earth is commanded to swallow its water, heaven to cease, and the floodwater subsides; the verse stages where overwhelming water goes and how it is withdrawn.
- (11:86) [terra: strong; basis: root+theme] بَقِيَّتُ ٱللَّهِ خَيْرٌۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ ۚ وَمَآ أَنَا۠ عَلَيْكُم بِحَفِيظٍۢ
  Unverified discovery rationale: terra: بَقِيَّتُ ٱللَّهِ خَيْرٌ لَّكُمْ makes a God-given lawful remainder better than gain taken by fraud, a social form of beneficial residue.
- (13:17) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶13] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
  Unverified discovery rationale: luna: The section joins flood foam, measured valley flow, and useful metal scum in one image: the ayah says the valleys flow بِقَدَرِهَا, then زَبَدٌ goes while what benefits people remains. It gives the section's exact contrast between passing residue and enduring benefit. | terra: This is the section's controlling parallel: rain fills valleys بِقَدَرِهَا, the flood carries زَبَدًا, metalworking raises like foam, and what benefits people يَمْكُثُ while the foam goes away.
- (13:19) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: neighbour+root+speaker+theme] ۞ أَفَمَن يَعْلَمُ أَنَّمَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ كَمَنْ هُوَ أَعْمَىٰٓ ۚ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: After 13:17's foam-and-water parable and 13:18's response contrast, this ayah distinguishes recognizing the revealed truth from blindness and says only people of understanding remember. It continues the section's question of whether a reminder takes hold. | terra: Immediately after the flood parable and its application in 13:18, this ayah contrasts one who يَعْلَمُ that the revelation is truth with the blind and says only people of understanding remember; it joins knowledge, truth, and receptive remembrance.
- (14:24) [luna: medium; terra: strong; basis: scene+theme] أَلَمْ تَرَ كَيْفَ ضَرَبَ ٱللَّهُ مَثَلًۭا كَلِمَةًۭ طَيِّبَةًۭ كَشَجَرَةٍۢ طَيِّبَةٍ أَصْلُهَا ثَابِتٌۭ وَفَرْعُهَا فِى ٱلسَّمَآءِ
  Unverified discovery rationale: luna: The section's reminder is valuable if it benefits and its water image rests on growth; this ayah likens a good word to a good tree with a firm root and high branches. It makes the word's benefit look rooted and growing. | terra: A good word is a good tree whose root is ثابت, giving the section's beneficial remainder a stable vegetal counterpart.
- (14:25) [luna: medium; terra: strong; basis: neighbour+scene+speaker+theme] تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا ۗ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ
  Unverified discovery rationale: luna: This continues 14:24's good-tree comparison: the tree yields fruit continually by its Lord's permission, and God gives the comparison so people may remember. It joins lasting yield to a reminder that takes root. | terra: The stable tree of 14:24 continually gives fruit by its Lord's permission; this ayah contributes the lasting thing's recurring benefit.
- (14:26) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَمَثَلُ كَلِمَةٍ خَبِيثَةٍۢ كَشَجَرَةٍ خَبِيثَةٍ ٱجْتُثَّتْ مِن فَوْقِ ٱلْأَرْضِ مَا لَهَا مِن قَرَارٍۢ
  Unverified discovery rationale: luna: The section contrasts useful water with waste that leaves; this ayah likens a bad word to a tree uprooted from the earth with no stability. It supplies the opposite of the good, rooted yield. | terra: The corrupt word is a bad tree uprooted from the earth with no قرار, the vegetal opposite of both held water and what remains in the ground.
- (15:21) [luna: medium (missing-ayat turn); terra: strong; basis: root+theme] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: luna: The section links 13:17's valley flow by measure to the root of 87:3; this ayah says what is sent down is only by a known measure. It places the measured water scene within God's measured provision. | terra: All things have divine خزائن and descend only بِقَدَرٍ مَعْلُومٍ; this states the hidden provision and measured release presupposed by the section's retained water.
- (15:22) [terra: strong; basis: neighbour+scene+theme] وَأَرْسَلْنَا ٱلرِّيَٰحَ لَوَٰقِحَ فَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَسْقَيْنَٰكُمُوهُ وَمَآ أَنتُمْ لَهُۥ بِخَٰزِنِينَ
  Unverified discovery rationale: terra: After 15:21's measured storehouses, this ayah sends fertilizing winds, gives water to drink, and says humans are not its keepers; its own contribution is the water and the limit on human storage.
- (16:96) [luna: contrast; terra: strong; basis: contrast+root+theme] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: The section defines ب ق ي as remaining in one's first state and opposes it to perishing; this ayah says what you have runs out while what is with God remains. It gives the exact passing-and-remaining distinction behind the image. | terra: مَا عِندَكُمْ يَنفَدُ وَمَا عِندَ ٱللَّهِ بَاقٍ states in bare terms the section's division between what runs out and what remains.
- (17:81) [luna: medium; terra: strong; basis: contrast+theme] وَقُلْ جَآءَ ٱلْحَقُّ وَزَهَقَ ٱلْبَٰطِلُ ۚ إِنَّ ٱلْبَٰطِلَ كَانَ زَهُوقًۭا
  Unverified discovery rationale: luna: The section's cleaned-well sense is water emerging after mud is removed, and 13:17 separates foam from what benefits; this ayah says truth comes and falsehood vanishes. It gives the same clear separation in moral terms. | terra: Truth arrives and falsehood is زَهُوقًا, destined to vanish; it states directly what 13:17 makes visible through disappearing foam.
