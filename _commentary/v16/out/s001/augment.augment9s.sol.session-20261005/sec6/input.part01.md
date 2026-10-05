Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 6 of 14 ("Rıza ve gazap: inen şey ve yüzde bıraktığı iz"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 6 (prose paragraphs numbered) =====
[¶32] Sure iki toplulukla biter. Her iki grubun ardından aynı söz gelir: {ar:أَنْعَمْتَ عَلَيْهِمْ, tr:en'amte aleyhim, gloss:onlara nimet verdin, source:1:7} ve {ar:ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:el-magdûbi aleyhim, gloss:üzerlerine gazap inenler, source:1:7}. "Aleyhim" bir şeyin üstlerine indiğini söyler. Birincisinde inen nimettir, ikincisinde gazap. Nimet cümlesinde fiili yapan açıkça "sen"dir. Gazap kelimesi ise edilgen bir sıfattır ve gazabı yapanı anmaz. Bu dilbilgisi farkının yanında kelimelerin aileleri de birer karşıtlık taşır. Hamd yerginin karşıtıdır: {ar:الحمد نقيض الذم, tr:el-hamdü nakîdu'z-zemm, gloss:hamd, yerginin karşıtıdır, source:"ح م د,B001"}. Hamd bir şeyi beğenip onaylamaktır: {ar:هل تحمد لي هذا الأمر أي هل ترضاه لي, tr:hel tahmedü lî hâze'l-emr, gloss:bu işi benim için uygun görür müsün, yani benim için ona razı olur musun, source:"ح م د,B002"}. "Nimet" kelimesinin ailesinde övgü sözü yergi sözünün karşısında durur: {ar:نعم ضد بئس, tr:ni'me ziddü bi'se, gloss:ni'me, bi'senin zıddıdır, source:"ن ع م,B003"}, {ar:نعم كلمة تستعمل في المدح بإزاء بئس, tr:ni'me kelimetün tüsta'melü fi'l-medhi bi-izâi bi'se, gloss:ni'me, bi'senin karşısında övgü için kullanılan kelimedir, source:"ن ع م,B003"}. Gazap da rızanın karşıtıdır: {ar:الغضب ضد الرضا, tr:el-gadabu ziddü'r-ridâ, gloss:gazap rızanın zıddıdır, source:"غ ض ب,B001"}.

[¶33] Bu sahne bedende de görülür. Gazap kalpte kanın kaynamasıdır: {ar:الغضب ثوران دم القلب إرادة الانتقام, tr:el-gadabu sevrânü demi'l-kalbi irâdete'l-intikâm, gloss:gazap, öç almak isteğiyle kalbin kanının kaynamasıdır, source:"غ ض ب,B001"}. Kelime koyu kırmızıya da ad verir: {ar:الغضب الأحمر الشديد الحمرة, tr:el-gadbü'l-ahmerü'ş-şedîdü'l-humre, gloss:gadb, koyu kırmızıdır, source:"غ ض ب,B005"}. Asık yüze de bu kökten ad verilir: {ar:امرأة غضوب أي عبوس, tr:imraetün gadûb, gloss:gadûb kadın, yüzü asık kadındır, source:"غ ض ب,B007"}. Göz çevresinin şişmesi de aynı fiille anlatılır: {ar:غضبت عين الرجل إذا ورم ما حولها, tr:gadibet aynü'r-racül, gloss:adamın gözünün çevresi şişti, source:"غ ض ب,B006"}. Nimetin yüzü bunun tersidir. Yüz yumuşaktır: {ar:نعم الشيء صار ناعما لينا, tr:neume'ş-şey'ü, gloss:şey yumuşak ve narin oldu, source:"ن ع م,B002"}. Göz de serinleyip dinginleşir: {ar:نعمة العين قرتها, tr:nu'metü'l-ayni kurratühâ, gloss:gözün nimeti onun serinleyip dinginleşmesidir, source:"ن ع م,B013"}.

[¶34] Bu görüntü düz bir mealin gösteremediğini gösterir: Yedinci ayetin iki grubu yalnızca iki ayrı hükmü almaz, iki ayrı yüz de taşır. Biri kızarmış, asık ve gözleri şişmiş bir yüzdür. Öbürü yumuşamış ve gözü serinlemiş bir yüzdür. İkinci ayet bu sahneyi rızayla açar. Yedinci ayet ise onu ikiye böler. Dördüncü ayetteki "yevm" kelimesi bu iki inişi taşıyan günleri adlandırır: {ar:وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين, tr:ve zekkirhüm bi-eyyâmi'llâh, gloss:"onlara Allah'ın günlerini hatırlat", yani Âd'a, Semûd'a ve başkalarına inen azabı ve başkalarının bağışlanmasını, source:"ي و م,B004"}. Aynı kelime nimet anlamında da kullanılır: {ar:أيامه: نعمه, tr:eyyâmühû: niamuh, gloss:onun günleri, nimetleridir, source:"ي و م,B004"}. Musa'ya verilen emir bu sözle gelir: {ar:وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ, tr:ve zekkirhüm bi-eyyâmillâh, gloss:onlara Allah'ın günlerini hatırlat, source:14:5}.

[¶35] Kur'an'da gazabın inişi bir sahne olarak anlatılır. Allah, düşmandan kurtardığı İsrailoğullarına kudret helvası ile bıldırcını hatırlatır ve şöyle der: {ar:كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَلَا تَطْغَوْا۟ فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِى, tr:külû min tayyibâti mâ razaknâküm ve lâ tatgav fîhi fe-yehılle aleyküm gadabî, gloss:size verdiğimiz rızkın temizlerinden yiyin, bunda azmayın, yoksa gazabım üzerinize iner, source:20:81}. Ardından iki son yan yana gelir: {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi gadabî fe-kad hevâ, gloss:kimin üzerine gazabım inerse o düşmüştür, source:20:81} ve {ar:وَإِنِّى لَغَفَّارٌۭ لِّمَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا ثُمَّ ٱهْتَدَىٰ, tr:ve innî le-gaffârun li-men tâbe ve âmene ve amile sâlihan sümme'htedâ, gloss:tövbe eden, iman edip iyi iş yapan, sonra da doğru yolda yürüyen için ben çok bağışlayıcıyım, source:20:82}. Gazap bir düşüştür, bağışlanmanın sonu ise yolu bulmaktır. Buzağı olayından sonra Musa halkına gazaplı döner: {ar:فَرَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا, tr:fe-raca'a Mûsâ ilâ kavmihî gadbâne esifâ, gloss:Musa halkına öfkeli ve üzgün döndü, source:20:86}. Halkına da şöyle sorar: {ar:أَمْ أَرَدتُّمْ أَن يَحِلَّ عَلَيْكُمْ غَضَبٌۭ مِّن رَّبِّكُمْ, tr:em eradtüm en yehılle aleyküm gadabün min rabbiküm, gloss:yoksa Rabbinizden üzerinize gazap inmesini mi istediniz, source:20:86}. Buzağıyı edinenler için hüküm şudur: {ar:سَيَنَالُهُمْ غَضَبٌۭ مِّن رَّبِّهِمْ وَذِلَّةٌۭ, tr:se-yenâlühüm gadabün min rabbihim ve zilleh, gloss:onlara Rablerinden bir gazap ve bir alçalış erişecek, source:7:152}. Burada alçalış, kulun kendi isteğiyle seçtiği alçalışın tersidir. Gazap ile yolu yitirmek bir ayette birlikte de geçer: {ar:مَن لَّعَنَهُ ٱللَّهُ وَغَضِبَ عَلَيْهِ, tr:men leanehu'llâhu ve gadibe aleyh, gloss:Allah'ın lanet ettiği ve gazap ettiği kimse, source:5:60}, {ar:أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ, tr:ülâike şerrun mekânen ve edallü an sevâi's-sebîl, gloss:onların yeri daha kötüdür ve yolun ortasından daha çok sapmışlardır, source:5:60}. Rıza ile öfke bir yürüyüş olarak karşılaştırılır: {ar:أَفَمَنِ ٱتَّبَعَ رِضْوَٰنَ ٱللَّهِ كَمَنۢ بَآءَ بِسَخَطٍۢ مِّنَ ٱللَّهِ, tr:e-fe meni'ttebe'a rıdvâna'llâhi ke-men bâe bi-sehatin mina'llâh, gloss:Allah'ın rızasının ardından giden, Allah'ın öfkesiyle dönen gibi midir, source:3:162}.

[¶36] Nimet verilenler topluluğu açıkça sayılır: {ar:فَأُو۟لَٰٓئِكَ مَعَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ وَٱلصِّدِّيقِينَ وَٱلشُّهَدَآءِ وَٱلصَّٰلِحِينَ, tr:fe-ülâike meallezîne en'amallâhu aleyhim mine'n-nebiyyîne ve's-sıddîkîne ve'ş-şühedâi ve's-sâlihîn, gloss:onlar Allah'ın nimet verdiği peygamberler, sıddıklar, şehitler ve salihlerle beraberdir, source:4:69}. Ayet {ar:وَحَسُنَ أُو۟لَٰٓئِكَ رَفِيقًۭا, tr:ve hasüne ülâike refîkâ, gloss:onlar ne güzel yol arkadaşlarıdır, source:4:69} sözüyle biter. Yedinci ayetteki "onların yolu", birlikte yürünen bir yoldur. Başka bir yerde nimet ile hidayet birlikte anılır ve yüzleri secdeye kapanmış olarak gösterilir: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم, tr:ülâikellezîne en'amallâhu aleyhim, gloss:Allah'ın nimet verdikleri işte bunlardır, source:19:58}, {ar:وَمِمَّنْ هَدَيْنَا وَٱجْتَبَيْنَآ, tr:ve mimmen hedeynâ vectebeynâ, gloss:ve yola iletip seçtiklerimizden, source:19:58}, {ar:خَرُّوا۟ سُجَّدًۭا وَبُكِيًّۭا, tr:harrû succeden ve bukiyyâ, gloss:secde ederek ve ağlayarak yere kapandılar, source:19:58}. O gündeki yüzler de bu iki tarafı taşır: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün bazı yüzler zelil ve düşkündür, source:88:2} ve {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün bazı yüzler nimetle yumuşamıştır, source:88:8}. "Nâime", "en'amte" ile aynı köktendir. Ardından gelen ayet bu yüzleri rızaya bağlar: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdıye, gloss:çabasından hoşnuttur, source:88:9}. Başka bir yerde de aynı kök yüzde okunur: {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-na'îm, gloss:yüzlerinde nimetin parlaklığını tanırsın, source:83:24}. Bir başka sahnede yüzlerin bir kısmı ışıldar: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ, tr:vucûhun yevmeizin müsfira, gloss:o gün bazı yüzler ışıl ışıldır, source:80:38}, {ar:ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ, tr:dâhiketün müstebşira, gloss:güler ve sevinir, source:80:39}. Öbür yüzlerin üstüne ise bir şey iner: {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ gabera, gloss:o gün bazı yüzlerin üstünde toz vardır, source:80:40}, {ar:تَرْهَقُهَا قَتَرَةٌ, tr:terhakuhâ katera, gloss:onları bir karartı kaplar, source:80:41}. Burada "aleyhâ", surenin "aleyhim" sözünün yüzdeki karşılığıdır.

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

===== passages from the discovery list (299) =====
## strong (182)

- (2:57) [luna: strong; terra: strong; basis: scene+theme] وَظَلَّلْنَا عَلَيْكُمُ ٱلْغَمَامَ وَأَنزَلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۖ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
  Unverified discovery rationale: luna: In the wilderness, God shades Israel with cloud and sends manna and quail, then tells them to eat from the good provision; this is another direct provision scene behind 20:81's gift-and-warning pattern. | terra: Cloud shade, manna, quail, and the command to eat good provision repeat the provision scene quoted by the section before 20:81's warning.
- (2:58) [terra: strong; basis: scene+theme] وَإِذْ قُلْنَا ٱدْخُلُوا۟ هَٰذِهِ ٱلْقَرْيَةَ فَكُلُوا۟ مِنْهَا حَيْثُ شِئْتُمْ رَغَدًۭا وَٱدْخُلُوا۟ ٱلْبَابَ سُجَّدًۭا وَقُولُوا۟ حِطَّةٌۭ نَّغْفِرْ لَكُمْ خَطَٰيَٰكُمْ ۚ وَسَنَزِيدُ ٱلْمُحْسِنِينَ
  Unverified discovery rationale: terra: Israel is told to enter, eat abundantly, enter the gate prostrating, and ask for remission; forgiveness and increase await the doers of good. It binds plentiful favor, a bowed face, and pardon.
- (2:59) [luna: contrast; terra: strong; basis: contrast+neighbour+scene+theme] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَنزَلْنَا عَلَى ٱلَّذِينَ ظَلَمُوا۟ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَفْسُقُونَ
  Unverified discovery rationale: luna: After the command to enter and ask forgiveness in 2:58, the wrongdoers are struck by punishment from heaven; the verse gives the descent that follows refusal of a given way. | terra: The wrongdoers alter the commanded word, so a punishment is sent down upon them from heaven. It reverses 2:58's gift and remission with a descending consequence.
- (2:61) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
  Unverified discovery rationale: luna: Israel asks for other food after the manna, and the verse says humiliation was laid upon them and they incurred anger from God (بَاءُوا بِغَضَبٍ مِنَ اللَّهِ); it closely joins rejected provision, abasement, and anger. | terra: After rejecting the given food for lesser substitutes, Israel receives abasement and returns with غضب upon غضب. It makes misuse of provision lead to the section's falling wrath and lowliness.
- (2:90) [luna: contrast (missing-ayat turn); terra: strong; basis: root+theme] بِئْسَمَا ٱشْتَرَوْا۟ بِهِۦٓ أَنفُسَهُمْ أَن يَكْفُرُوا۟ بِمَآ أَنزَلَ ٱللَّهُ بَغْيًا أَن يُنَزِّلَ ٱللَّهُ مِن فَضْلِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۖ فَبَآءُو بِغَضَبٍ عَلَىٰ غَضَبٍۢ ۚ وَلِلْكَٰفِرِينَ عَذَابٌۭ مُّهِينٌۭ
  Unverified discovery rationale: luna: The verse says they incurred anger upon anger (بَاءُوا بِغَضَبٍ عَلَىٰ غَضَبٍ) for rejecting what God revealed; it is a repeated formulation of anger settling on a group. | terra: Those who reject Allah's revelation out of envy return with غضب upon غضب. The repeated burdened return sharpens the section's language of wrath as an acquired descent.
- (2:144) [terra: strong (missing-ayat turn); basis: root+scene+theme] قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا يَعْمَلُونَ
  Unverified discovery rationale: terra: Allah sees the Prophet turn his face toward heaven and gives him a qibla that will please him. It directly joins face-direction and rıza before 2:150 completes favor and guidance.
- (2:150) [terra: strong; basis: root+scene+theme] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: The command repeatedly turns faces toward the Sacred Mosque so that Allah may complete His favor and guide the community. It joins face, نعمة, and guidance in one direction.
- (2:207) [luna: strong (missing-ayat turn); terra: medium; basis: root+theme] وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: luna: A person gives himself seeking God's pleasure (ابْتِغَاءَ مَرْضَاتِ اللَّهِ); this is a specific path of seeking the acceptance that the section contrasts with anger. | terra: A person gives himself seeking Allah's pleasure (مَرْضَات). It makes rıza a concrete motive for self-offering rather than a detached reward.
- (3:106) [luna: contrast; terra: strong; basis: contrast+scene+theme] يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌۭ ۚ فَأَمَّا ٱلَّذِينَ ٱسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُم بَعْدَ إِيمَٰنِكُمْ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
  Unverified discovery rationale: luna: At judgment some faces whiten and others blacken (تَبْيَضُّ وُجُوهٌ وَتَسْوَدُّ وُجُوهٌ); this is a direct alternative account of judgment appearing in two faces. | terra: On the Day, faces are whitened and blackened, and the blackened faces are confronted with their disbelief. It makes the final division visible on the face.
- (3:107) [luna: strong; terra: strong; basis: contrast+neighbour+scene+theme] وَأَمَّا ٱلَّذِينَ ٱبْيَضَّتْ وُجُوهُهُمْ فَفِى رَحْمَةِ ٱللَّهِ هُمْ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: luna: The whitened faces are in God's mercy; the verse identifies the favorable meaning of the facial sign introduced in 3:106. | terra: The whitened faces are in Allah's mercy forever. It supplies the mercy-side outcome of the facial division in 3:106.
- (3:112) [luna: contrast (missing-ayat turn); terra: strong; basis: root+scene+theme] ضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ أَيْنَ مَا ثُقِفُوٓا۟ إِلَّا بِحَبْلٍۢ مِّنَ ٱللَّهِ وَحَبْلٍۢ مِّنَ ٱلنَّاسِ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ وَضُرِبَتْ عَلَيْهِمُ ٱلْمَسْكَنَةُ ۚ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلْأَنۢبِيَآءَ بِغَيْرِ حَقٍّۢ ۚ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
  Unverified discovery rationale: luna: Humiliation is laid upon a people and they incur anger from God for disbelief and rebellion; this repeats the section's combination of an imposed mark and divine anger. | terra: Humiliation is struck upon them and they return with غضب from Allah. The verse visually couples wrath with the lowly condition that the section finds in the adverse face.
- (3:134) [luna: medium; terra: strong; basis: contrast+scene+theme] ٱلَّذِينَ يُنفِقُونَ فِى ٱلسَّرَّآءِ وَٱلضَّرَّآءِ وَٱلْكَٰظِمِينَ ٱلْغَيْظَ وَٱلْعَافِينَ عَنِ ٱلنَّاسِ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
  Unverified discovery rationale: luna: The righteous restrain rage and pardon people; the verse gives an ethical opposite to the bodily eruption in the section's B001 gloss for anger, using the related but different word الغيظ. | terra: The God-fearing restrain anger and pardon people, and Allah loves the doers of good. It gives a human reversal of anger's urge toward retaliation.
