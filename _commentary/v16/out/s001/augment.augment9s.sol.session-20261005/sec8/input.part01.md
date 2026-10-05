Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 8 of 14 ("Gök: gündüz, öğle güneşi, hilal ve tapılan güneş"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 8 (prose paragraphs numbered) =====
[¶42] Bu görüntü gün boyunca dönen göğü gösterir. Dördüncü ayetteki "yevm" kelimesi, güneşin doğuşundan batışına kadar geçen süredir: {ar:اليوم مقداره من طلوع الشمس إلى غروبها, tr:el-yevmü mikdâruhû min tulû'i'ş-şemsi ilâ gurûbihâ, gloss:günün uzunluğu güneşin doğuşundan batışına kadardır, source:"ي و م,B001"}. Altıncı ayetteki "müstakîm" kelimesinin ailesinde bu günün ortası vardır: {ar:قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل, tr:kâme kâimü'z-zahîre izâ kâmeti'ş-şemsü ve kâde'z-zıllü ya'kılu, gloss:öğle vakti dikildi, yani güneş tepede durdu ve gölge neredeyse yok oldu, source:"ق و م,B017"}. Aynı an bir terazinin dengeye gelmesi olarak da anlatılır: {ar:قام ميزان النهار فاعتدل, tr:kâme mîzânü'n-nehâri fa'tedel, gloss:gündüzün terazisi dikilip dengeye geldi, source:"ق و م,B017"}. Birinci ayetteki "bism" kelimesinin ailesinde ufuktan biraz yükselmiş bir hilal vardır: {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetü'l-hilâli şahsuh, gloss:hilalin semâvesi, ufuktan biraz yükseldiğinde görünen şeklidir, source:"س م و,B002"}. Gök de bu ailedendir: {ar:السماء كل ما علاك فأظلك, tr:es-semâü küllü mâ alâke fe-ezalleke, gloss:sema, üstünde durup sana gölge eden her şeydir, source:"س م و,B004"}. Yedinci ayetteki "en'amte" kelimesinin ailesinde Ay'ın konaklarından biri vardır: {ar:والنعائم منزل من منازل القمر, tr:ve'n-neâimü menzilün min menâzili'l-kamer, gloss:neâim, Ay'ın konaklarından biridir, source:"ن ع م,B007"}. İkinci ayetteki "âlem" kelimesi bütün bunları içine alan gök küresidir: {ar:العالم اسم للفلك وما يحويه, tr:el-âlemü ismün li'l-feleki ve mâ yahvîh, gloss:âlem, gök küresinin ve içindekilerin adıdır, source:"ع ل م,B003"}.

[¶43] Bu görüntüde "müstakîm" kelimesi kendi anlamının yanında bir an da hissettirir. Güneş tepede dikildiğinde gölge ne sağa ne sola düşer ve gündüzün terazisi dengeye gelir. Yolun dosdoğru olması ile öğlenin dengesi kelimenin ailesinde yan yana durur. Aynı kök hem eğilmeyen yolu hem de gölgesi düşmeyen anı adlandırır. Bu, kökün kendi içinde kurduğu bir bağdır ve yorumu buradan öteye taşımak gerekmez. Görüntünün asıl ağırlığı ise başka bir yerdedir. Birinci ayetteki "Allah" adının ailesinde güneşin de bir adı vardır: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetü'ş-şems, sümmiyet bi-zâlike li-enne kavmen kânû ya'büdûnehâ, gloss:ilâhe güneştir; bir kavim ona taptığı için bu adı almıştır, source:"ء ل ه,B001"}. Beşinci ayetin {ar:إِيَّاكَ نَعْبُدُ, tr:iyyâke na'büdü, gloss:yalnız sana kulluk ederiz, source:1:5} sözü, kulluğu gökte yükselip batan bu ışıklardan ayırır.

[¶44] Kur'an bu ayrımı açıkça yapar: {ar:لَا تَسْجُدُوا۟ لِلشَّمْسِ وَلَا لِلْقَمَرِ وَٱسْجُدُوا۟ لِلَّهِ ٱلَّذِى خَلَقَهُنَّ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ, tr:lâ tescüdû li'ş-şemsi ve lâ li'l-kameri vescüdû lillâhillezî halakahünne in küntüm iyyâhü ta'büdûn, gloss:güneşe de aya da secde etmeyin; eğer yalnız O'na kulluk ediyorsanız, onları yaratan Allah'a secde edin, source:41:37}. Bu ayetteki "iyyâhü ta'büdûn" sözü, surenin "iyyâke na'büdü" sözünün üçüncü şahısla söylenmiş halidir. İbrahim'in sahnesinde gök, yol ve sapma birlikte görülür. Gece onu örtünce bir yıldız görür ve "bu benim Rabbim" der. Yıldız batınca {ar:لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:lâ uhibbü'l-âfilîn, gloss:batanları sevmem, source:6:76} der. Doğmakta olan ayı görünce aynı şeyi söyler. Ay batınca şöyle der: {ar:لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ, tr:le-in lem yehdinî rabbî le-ekûnenne mine'l-kavmi'd-dâllîn, gloss:Rabbim beni yola iletmezse, ben de mutlaka yolunu yitirmiş kavimden olurum, source:6:77}. Bu cümlede Fâtiha'nın "Rab", "hidayet", "kavm" ve "dâllîn" kelimeleri bir arada geçer. İbrahim ufuktan yükselen bir şekli, yani "semâvetü'l-hilâl"i görür, onu Rab sanar ve batışını görünce yönünü yitirme tehlikesini fark eder. Güneşte de aynı şey olur. Sonunda yüzünü göklerin ve yerin yaratıcısına çevirir: {ar:إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا, tr:innî veccehtü vechiye lillezî fatara's-semâvâti ve'l-arda hanîfâ, gloss:ben yüzümü, hanif olarak, gökleri ve yeri yaratana çevirdim, source:6:79}. Hüdhüd, Süleyman'a güneşe tapan bir halkı haber verir: {ar:يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ, tr:yescüdûne li'ş-şemsi min dûnillâh, gloss:Allah'ı bırakıp güneşe secde ediyorlar, source:27:24}. Ardından sonucu söyler: {ar:فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ فَهُمْ لَا يَهْتَدُونَ, tr:fe-saddehüm ani's-sebîli fe-hüm lâ yehtedûn, gloss:onları yoldan alıkoydu, onlar da yolu bulamıyorlar, source:27:24}. Güneşe tapmak burada yoldan alıkonmak olarak anlatılır. Aynı haberde bu halkı bir kadının yönettiği söylenir: {ar:إِنِّى وَجَدتُّ ٱمْرَأَةًۭ تَمْلِكُهُمْ, tr:innî vecedtü'mraeten temlikühüm, gloss:onlara hükmeden bir kadın buldum, source:27:23}. Ay'ın konakları ise bir hesap için yaratılmıştır: {ar:وَٱلْقَمَرَ نُورًۭا وَقَدَّرَهُۥ مَنَازِلَ لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:ve'l-kamera nûran ve kaddarahû menâzile li-ta'lemû adede's-sinîne ve'l-hisâb, gloss:ayı bir ışık yaptı ve yılların sayısını ve hesabı bilesiniz diye ona konaklar biçti, source:10:5}. Hilaller de birer vakit işaretidir: {ar:يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ, tr:yes'elûneke ani'l-ehille, kul hiye mevâkîtü li'n-nâsi ve'l-hacc, gloss:sana hilalleri soruyorlar; de ki: onlar insanlar ve hac için vakit ölçüleridir, source:2:189}. Mağara sahnesinde güneş gençlerin üzerinden sağa ve sola kayar ve ayet şöyle biter: {ar:مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ, tr:men yehdillâhü fe-hüve'l-mühted, gloss:Allah kimi yola iletirse yolu bulan odur, source:18:17}.

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

===== passages from the discovery list (158) =====
## strong (71)

- (2:189) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶44] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ ۗ وَلَيْسَ ٱلْبِرُّ بِأَن تَأْتُوا۟ ٱلْبُيُوتَ مِن ظُهُورِهَا وَلَٰكِنَّ ٱلْبِرَّ مَنِ ٱتَّقَىٰ ۗ وَأْتُوا۟ ٱلْبُيُوتَ مِنْ أَبْوَٰبِهَا ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: The section develops the rising crescent and lunar stations; 2:189 calls the الأهلة time markers (مواقيت) for people and pilgrimage, making the crescent a calendar sign. | terra: The new crescents are appointed measures of time for people and pilgrimage. It directly gives the hilal its practical timekeeping role rather than a divine status.
- (2:258) [luna: strong; terra: strong; basis: contrast+scene+theme] أَلَمْ تَرَ إِلَى ٱلَّذِى حَآجَّ إِبْرَٰهِۦمَ فِى رَبِّهِۦٓ أَنْ ءَاتَىٰهُ ٱللَّهُ ٱلْمُلْكَ إِذْ قَالَ إِبْرَٰهِۦمُ رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ قَالَ أَنَا۠ أُحْىِۦ وَأُمِيتُ ۖ قَالَ إِبْرَٰهِۦمُ فَإِنَّ ٱللَّهَ يَأْتِى بِٱلشَّمْسِ مِنَ ٱلْمَشْرِقِ فَأْتِ بِهَا مِنَ ٱلْمَغْرِبِ فَبُهِتَ ٱلَّذِى كَفَرَ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: In Abraham’s argument about lordship, the challenge فأت بها من المغرب turns the sun’s rising from the east into evidence against the ruler who disputes God; the luminary’s course belongs to the Creator. | terra: Abraham answers the claimant of lordship by saying Allah brings the sun from the east and challenging him to bring it from the west. The solar horizon becomes evidence against a false lord.
- (3:190) [luna: strong; terra: strong; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: The verse pairs creation of the heavens and earth with the succession of night and day (اختلاف الليل والنهار); it presents the section’s turning sky as a sign for reflection. | terra: The creation of the heavens and earth and the alternation of night and day are signs for people of understanding. It states the reflective frame for the section's whole sky image.
- (6:75) [luna: medium; terra: strong; basis: neighbour+scene] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
  Unverified discovery rationale: luna: Immediately before the star test, God shows Abraham the kingdom of the heavens and earth (ملكوت السماوات والأرض); this supplies the celestial setting for 6:76 and locates it within God’s display. | terra: Before Abraham's observations of the setting lights, this ayah says he was shown the dominion of the heavens and earth; it supplies the cosmic frame in which the following star, moon, and sun are judged as creatures.
- (6:76) [luna: strong; terra: strong; basis: contrast+scene+theme] [cited in ¶44] فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ
  Unverified discovery rationale: luna: In Abraham’s test of celestial lights, the star sets (أفل), and he says لا أحب الآفلين; a visible light’s disappearance defeats treating it as Lord. | terra: Abraham sees a star and calls it his lord only within the test of its setting; “those that set” cannot be loved as lord. It begins the section's contrast between a visible heavenly light and the true Lord.
- (6:77) [luna: strong; terra: strong; basis: contrast+root+scene+speaker+theme] [cited in ¶44] فَلَمَّا رَءَا ٱلْقَمَرَ بَازِغًۭا قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ
  Unverified discovery rationale: luna: Abraham watches the moon set, then says لئن لم يهدني ربي لأكونن من القوم الضالين; this passage itself gathers Rab, guidance, and the lost people named in the section’s Fatiha reading. | terra: The moon rises and then sets; Abraham says that without his Lord's guidance he would belong to the astray people. This directly joins the lunar scene to the source's Rab, hidayah, and dallin language.
- (6:78) [luna: strong; terra: strong; basis: contrast+scene+speaker+theme] فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ ۖ فَلَمَّآ أَفَلَتْ قَالَ يَٰقَوْمِ إِنِّى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
  Unverified discovery rationale: luna: Abraham calls the rising sun “greater,” but when it sets (أفلت) he disavows the objects they associate with God; the same test now uses the sun. | terra: The sun rises, is called the larger heavenly body, then sets; Abraham disavows association. It is the source's fullest solar reversal of treating a rising light as divine.
- (6:79) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶44] إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا ۖ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
  Unverified discovery rationale: luna: After the sun sets, Abraham turns his face to the One who created the heavens and earth (فطر السماوات والأرض); this gives the section’s worship distinction its creator, rather than a heavenly light, as its object. | terra: Abraham turns his face toward the Originator of the heavens and earth as a hanif. It supplies the positive direction after the star, moon, and sun have proved unfit as objects of devotion.
- (6:80) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+scene+speaker+theme] وَحَآجَّهُۥ قَوْمُهُۥ ۚ قَالَ أَتُحَٰٓجُّوٓنِّى فِى ٱللَّهِ وَقَدْ هَدَىٰنِ ۚ وَلَآ أَخَافُ مَا تُشْرِكُونَ بِهِۦٓ إِلَّآ أَن يَشَآءَ رَبِّى شَيْـًۭٔا ۗ وَسِعَ رَبِّى كُلَّ شَىْءٍ عِلْمًا ۗ أَفَلَا تَتَذَكَّرُونَ
  Unverified discovery rationale: luna: After Abraham turns to the Creator in 6:79, this verse says his people dispute with him and he answers that Allah has guided him; its own contribution continues the section’s Abraham-and-guidance scene into the people’s challenge. | terra: After the celestial argument, Abraham says that Allah has guided him and that he does not fear the things his people associate with Him. Its own contribution is the passage's explicit contrast between guidance and feared false associates.
- (6:81) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+scene+speaker+theme] وَكَيْفَ أَخَافُ مَآ أَشْرَكْتُمْ وَلَا تَخَافُونَ أَنَّكُمْ أَشْرَكْتُم بِٱللَّهِ مَا لَمْ يُنَزِّلْ بِهِۦ عَلَيْكُمْ سُلْطَٰنًۭا ۚ فَأَىُّ ٱلْفَرِيقَيْنِ أَحَقُّ بِٱلْأَمْنِ ۖ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: Abraham asks how he should fear the partners his people associate with God when they do not fear associating without authority; it continues the same argument after the celestial test and sharpens the rejection of worshiping created things. | terra: Abraham asks why he should fear their associates when they do not fear associating with Allah without authority. It carries the preceding sun-and-moon rejection into a direct argument against association.
- (6:82) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: neighbour+theme] ٱلَّذِينَ ءَامَنُوا۟ وَلَمْ يَلْبِسُوٓا۟ إِيمَٰنَهُم بِظُلْمٍ أُو۟لَٰٓئِكَ لَهُمُ ٱلْأَمْنُ وَهُم مُّهْتَدُونَ
  Unverified discovery rationale: luna: The next verse says those who believe without mixing faith with injustice have security and are guided (وهم مهتدون); in Abraham’s argument this answers the section’s fear of becoming among the astray with a stated condition for guidance. | terra: The conclusion of Abraham's exchange gives security and guidance to those whose faith is not mixed with wrongdoing. It supplies the passage's answer to the source's danger of becoming among the astray.
- (6:96) [luna: strong; terra: strong; basis: scene+theme] فَالِقُ ٱلْإِصْبَاحِ وَجَعَلَ ٱلَّيْلَ سَكَنًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ حُسْبَانًۭا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ
  Unverified discovery rationale: luna: This verse joins dawn splitting, night as rest, and sun and moon by calculation (حسبانا); it makes the section’s day and luminaries part of an ordered time system. | terra: The splitter of dawn makes night for rest and the sun and moon for calculation. It gathers daybreak, the daily rhythm, and celestial measurement into one created order.
- (6:97) [luna: strong (missing-ayat turn); terra: medium; basis: contrast+scene+theme] وَهُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلنُّجُومَ لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
  Unverified discovery rationale: luna: The verse says God made stars so people can find their way through land and sea darkness; it gives the star from Abraham’s scene a created navigational role, distinct from treating a heavenly light as Lord or from the section’s spiritual guidance. | terra: Allah makes stars so people can find their way through the darkness of land and sea. It distinguishes their created navigational guidance from the Lord's guidance sought by Abraham.
- (6:161) [terra: strong; basis: root+theme] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
  Unverified discovery rationale: terra: Abraham's Lord has guided him to a straight, upright religion. It connects the source's Ibrahim scene to the mustaqim/Q-W-M family without making the noon sense into a further doctrine.
- (7:54) [luna: strong; terra: strong; basis: contrast+scene+speaker+theme] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ وَٱلنُّجُومَ مُسَخَّرَٰتٍۭ بِأَمْرِهِۦٓ ۗ أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ ۗ تَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: After describing creation of heaven and earth and night covering day, the verse says sun, moon, and stars are subjected to God’s command; their celestial motion is created service, not a reason to worship them. | terra: Allah creates the heavens and earth, covers day with night in rapid pursuit, and makes sun, moon, and stars subject to His command. It supplies the daily sky as an ordered act of lordship.
- (10:3) [luna: strong (missing-ayat turn); basis: contrast+scene+theme] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۖ يُدَبِّرُ ٱلْأَمْرَ ۖ مَا مِن شَفِيعٍ إِلَّا مِنۢ بَعْدِ إِذْنِهِۦ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ فَٱعْبُدُوهُ ۚ أَفَلَا تَذَكَّرُونَ
