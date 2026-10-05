Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 13 of 14 ("Eve götürülen: kurbanlık, gelin, armağan ve sığınan"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 13 (prose paragraphs numbered) =====
[¶62] "İhdinâ" kelimesinin ailesinde, bir yolda götürülüp ait olacağı bir eve ulaştırılan şeyler vardır. Bunların ilki sürüden ayrılıp Harem'e götürülen kurbanlıktır: {ar:الهدي ما يهدى إلى الحرم من النعم؛ حتى يبلغ الهدى محله, tr:el-hedyü mâ yühdâ ile'l-harami mine'n-neam; hattâ yebluga'l-hedyü mahilleh, gloss:hedy, develer arasından Harem'e götürülen hayvandır; "kurbanlık yerine ulaşıncaya kadar", source:"ه د ي,B005"}. Develere de bu ad verilir: {ar:العرب تسمي الإبل هديا, tr:el-Arabü tüsemmi'l-ibile hedyen, gloss:Araplar develere hedy derler, source:"ه د ي,B005"}. Bu götürmenin amacı yakınlaşmaktır: {ar:ما أهدي من النعم إلى الحرم قربة إلى الله تعالى, tr:mâ uhdiye mine'n-neami ile'l-harami kurbeten ilallâh, gloss:Allah'a yakınlaşmak için develer arasından Harem'e götürülen hayvan, source:"ه د ي,B005"}. Hayvan, yedinci ayetteki "en'amte" kelimesiyle aynı kökten gelen sürüden ({ar:النعم الإبل, tr:en-neamü'l-ibil, gloss:neam develerdir, source:"ن ع م,B005"}) alınır. Götürülen hayvan uysallaştırılmış bir devedir: {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-mu'abbed, gloss:katranla sıvanmış, uysallaştırılmış deve, source:"ع ب د,B005"}. Hizmet ettiği şey de ibadettir: {ar:العبادة الطاعة والتعبد التنسك, tr:el-ibâdetü't-tâatü ve't-teabbüdü't-tenessük, gloss:ibadet itaattir; teabbüd ise kulluk ibadetini yerine getirmektir, source:"ع ب د,B003"}. Hayvanın üzerinde ad söylenir. Bu ad, adlandırılanın anılışını yücelten yükseltilmiş addır: {ar:به رفع ذكر المسمى, tr:bihî rufi'a zikru'l-müsemmâ, gloss:onunla adlandırılanın anılışı yükseltilir, source:"س م و,B005"}. Hac mevsiminin adı da "bism" için anılan ikinci kökten gelir: {ar:موسم الحج موسما لأنه معلم يجتمع فيه, tr:mevsimü'l-hacci mevsimen li-ennehû ma'lemun yüctema'u fîh, gloss:hac mevsimine mevsim denir, çünkü içinde toplanılan bir nişandır, source:"و س م,B004"}, {ar:وسم الناس: شهدوا الموسم, tr:vesemen-nâs, gloss:insanlar mevsimde hazır bulundular, source:"و س م,B004"}. Bu cümle damgayı ikinci ayetteki "âlemîn" kelimesinin kökü olan "ma'lem" ile birleştirir.

[¶63] İkinci götürülen gelindir: {ar:هديت العروس فأنا أهديها هداء, tr:hedeytü'l-arûse fe-ene ehdîhâ hidâen, gloss:gelini kocasının evine götürdüm, source:"ه د ي,B006"}. Gelin, kocasının yanına toplanır: {ar:أهدى الرجل امرأته جمعها إليه وضمها, tr:ehde'r-racülü'mraetehû, gloss:adam karısını yanına aldı, kendine kattı, source:"ه د ي,B006"}. Bu götürmeden önce nikâh kıyılır. Dördüncü ayetteki "mâlik" kelimesinin ailesi bunu anlatır: {ar:أملكنا فلانا فلانة إذا زوجناه إياها, tr:emleknâ fülânen fülâneten, gloss:falancayı falancayla nikâhladık, source:"م ل ك,B004"}, {ar:الإملاك التزويج, tr:el-imlâkü't-tezvîc, gloss:imlâk, evlendirmektir, source:"م ل ك,B004"}. Üçüncü götürülen, tepsi üzerinde bir dosta taşınan armağandır: {ar:الهدية ما أهديت إلى ذي مودة من بر, tr:el-hediyyetü mâ ehdeyte ilâ zî meveddetin min birr, gloss:hediye, sevgi beslediğin birine gönderdiğin iyiliktir, source:"ه د ي,B004"}, {ar:المهدى الطبق الذي يهدى عليه, tr:el-mihdâ et-tabakullezî yühdâ aleyh, gloss:mihdâ, hediyenin üzerinde götürüldüğü tepsidir, source:"ه د ي,B004"}. Dördüncüsü, bir topluluğa sığınan kişidir. O da Beyt'in kurbanlığı gibi dokunulmaz olur: {ar:الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا, tr:el-hedyü'r-racülü zü'l-hurme, gloss:hedy, dokunulmazlığı olan kişidir; bir topluluğa gelip onlardan koruma ister ya da onlardan söz alır, source:"ه د ي,B007"}, {ar:الرجل الذي له حرمة كحرمة هدي البيت, tr:er-racülüllezî lehû hurmetün ke-hurmeti hedyi'l-beyt, gloss:Beyt'e götürülen kurbanlık kadar dokunulmazlığı olan kişi, source:"ه د ي,B007"}. Onu koruyan söz, ikinci ayetteki "Rab" kelimesinin ailesindendir: {ar:الربابة: العهد والميثاق؛ الأربة أهل الميثاق, tr:er-ribâbetü'l-ahdü ve'l-mîsâk, gloss:ribâbe ahit ve sözleşmedir; erebbe, sözleşme ehlidir, source:"ر ب ب,B011"}.

[¶64] Bu dört götürmenin ortak yanı, hidayet tanımının kendisinde bulunur: {ar:هديته الطريق والبيت, tr:hedeytühü't-tarîka ve'l-beyt, gloss:ona yolu ve evi gösterdim, source:"ه د ي,B001"}. Bu ailede "ihdinâ" isteği kendi anlamının yanında yolu göstermekten öte bir şey duyurur: Bizi yolun sonundaki eve ulaştır. Kurbanlık "mahill"ine, gelin kocasının evine, armağan dostuna, sığınan ise güvenli yerine ulaşır. Her biri bir eve ait olmak için yola çıkarılmıştır. Düz bir mealde bu isteğin varılacak bir yeri yoktur. Görüntü ise yolun bir eve vardığını gösterir.

[¶65] Kur'an kurbanlığı bir ev ile, bir ad ile ve bir hidayet ile birlikte anlatır: {ar:ثُمَّ مَحِلُّهَآ إِلَى ٱلْبَيْتِ ٱلْعَتِيقِ, tr:sümme mahillühâ ile'l-beyti'l-atîk, gloss:sonra onların varacağı yer o eski evdir, source:22:33}. Bu hayvanlar adla anılır: {ar:لِّيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ, tr:li-yezkürüsmellâhi alâ mâ razakahüm min behîmeti'l-en'âm, gloss:kendilerine rızık olarak verdiği hayvanlar üzerine Allah'ın adını ansınlar diye, source:22:34}. Kesim anında da ad söylenir: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkürüsmellâhi aleyhâ savâff, gloss:onlar sıra sıra dururken üzerlerine Allah'ın adını anın, source:22:36}. Sahne hidayet ile kapanır: {ar:كَذَٰلِكَ سَخَّرَهَا لَكُمْ لِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ, tr:kezâlike sahharahâ leküm li-tükebbirullâhe alâ mâ hedâküm, gloss:sizi doğru yola ilettiği için Allah'ı yüceltesiniz diye onları size böyle boyun eğdirdi, source:22:37}. Uysallaştırılmış hayvan, adın anılması, sürü ve hidayet bu tek pasajda yan yanadır. Kurbanlığın ulaşması gereken yer başka yerlerde de anılır: {ar:حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ, tr:hattâ yebluga'l-hedyü mahilleh, gloss:kurbanlık yerine ulaşıncaya kadar, source:2:196}, {ar:هَدْيًۢا بَٰلِغَ ٱلْكَعْبَةِ, tr:hedyen bâliga'l-Ka'be, gloss:Kâbe'ye ulaşacak bir kurbanlık olarak, source:5:95}. Yolun kesildiği bir sahne de vardır: {ar:وَٱلْهَدْىَ مَعْكُوفًا أَن يَبْلُغَ مَحِلَّهُۥ, tr:ve'l-hedye ma'kûfen en yebluga mahilleh, gloss:kurbanlık da yerine ulaşmaktan alıkonmuş olarak, source:48:25}. Kurbanlık ile Eve yönelenler birlikte dokunulmaz sayılır: {ar:وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ, tr:ve le'l-hedye ve le'l-kalâide ve lâ âmmîne'l-beyte'l-harâm, gloss:kurbanlığa, gerdanlıklı hayvanlara ve Beyt-i Haram'a yönelenlere dokunmayın, source:5:2}. Sığınanın Kur'an'daki sahnesi şöyledir: {ar:وَإِنْ أَحَدٌۭ مِّنَ ٱلْمُشْرِكِينَ ٱسْتَجَارَكَ فَأَجِرْهُ حَتَّىٰ يَسْمَعَ كَلَٰمَ ٱللَّهِ ثُمَّ أَبْلِغْهُ مَأْمَنَهُۥ, tr:ve in ehadün mine'l-müşrikîne'stecârake fe-ecirhü hattâ yesmea kelâmallâhi sümme eblığhü me'meneh, gloss:müşriklerden biri senden koruma isterse, Allah'ın sözünü işitinceye kadar onu koru, sonra onu güvende olacağı yere ulaştır, source:9:6}. Sığınan kişi korunur ve güvenli yerine ulaştırılır. Armağan da Kur'an'da bir hükümdarlar sahnesinde geçer. Süleyman'ın mektubunu alan kadın şöyle der: {ar:وَإِنِّى مُرْسِلَةٌ إِلَيْهِم بِهَدِيَّةٍۢ, tr:ve innî mürsiletün ileyhim bi-hediyye, gloss:onlara bir hediye göndereceğim, source:27:35}. Süleyman ise bu armağanı geri çevirir: {ar:بَلْ أَنتُم بِهَدِيَّتِكُمْ تَفْرَحُونَ, tr:bel entüm bi-hediyyetiküm tefrahûn, gloss:hayır, siz kendi hediyenizle sevinirsiniz, source:27:36}. Burada armağan, bir dosta değil bir rakibe gönderildiği için yerine ulaşamaz. Adın anıldığı yemek de helal kılınır: {ar:فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ, tr:fe-külû mimmâ zükirasmullâhi aleyh, gloss:üzerine Allah'ın adı anılandan yiyin, source:6:118}.

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

===== passages from the discovery list (249) =====
## strong (107)

- (2:38) [terra: strong; basis: root+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: terra: After the descent, whoever follows God's guidance has neither fear nor grief, casting guidance as the protection needed after leaving an earlier dwelling.
- (2:125) [luna: strong; terra: strong; basis: root+scene+theme] وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا وَٱتَّخِذُوا۟ مِن مَّقَامِ إِبْرَٰهِۦمَ مُصَلًّۭى ۖ وَعَهِدْنَآ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ أَن طَهِّرَا بَيْتِىَ لِلطَّآئِفِينَ وَٱلْعَٰكِفِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ
  Unverified discovery rationale: luna: The House is made مَثَابَةً لِّلنَّاسِ وَأَمْنًا, a return and safety for people; the same ayah records God's covenant with Abraham and Ishmael to purify it. | terra: God makes the House a place of return and security, making explicit the section's claim that the guided route has a home and safe arrival.
- (2:126) [luna: strong; terra: strong; basis: scene+speaker+theme] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ ٱجْعَلْ هَٰذَا بَلَدًا ءَامِنًۭا وَٱرْزُقْ أَهْلَهُۥ مِنَ ٱلثَّمَرَٰتِ مَنْ ءَامَنَ مِنْهُم بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ قَالَ وَمَن كَفَرَ فَأُمَتِّعُهُۥ قَلِيلًۭا ثُمَّ أَضْطَرُّهُۥٓ إِلَىٰ عَذَابِ ٱلنَّارِ ۖ وَبِئْسَ ٱلْمَصِيرُ
  Unverified discovery rationale: luna: Abraham asks God to make the city secure and provide its people with fruits; it joins the section's safe destination with the herd and gift as provision. | terra: Abraham asks that this be a secure city and that its people receive fruits, combining safe settlement and provision near the House.
- (2:142) [terra: strong; basis: root+scene+theme] ۞ سَيَقُولُ ٱلسُّفَهَآءُ مِنَ ٱلنَّاسِ مَا وَلَّىٰهُمْ عَن قِبْلَتِهِمُ ٱلَّتِى كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: terra: In the qiblah dispute, God guides whom He wills to a straight path; orientation toward the House becomes a test of being directed.
- (2:144) [terra: strong; basis: scene+theme] قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا يَعْمَلُونَ
  Unverified discovery rationale: terra: The Prophet is commanded to turn his face toward the Sacred Mosque, a concrete bodily direction toward the section's House.
- (2:149) [terra: strong; basis: scene+theme] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۖ وَإِنَّهُۥ لَلْحَقُّ مِن رَّبِّكَ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
  Unverified discovery rationale: terra: Wherever travelers emerge from, they are to turn toward the Sacred Mosque; this makes the House a direction carried through movement.
- (2:150) [terra: strong; basis: root+theme] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: The repeated qiblah command ends with completion of God's favor and the hope that people will be guided, linking direction, نعمة, and hidayah.
- (2:158) [luna: strong; terra: medium; basis: scene+theme] ۞ إِنَّ ٱلصَّفَا وَٱلْمَرْوَةَ مِن شَعَآئِرِ ٱللَّهِ ۖ فَمَنْ حَجَّ ٱلْبَيْتَ أَوِ ٱعْتَمَرَ فَلَا جُنَاحَ عَلَيْهِ أَن يَطَّوَّفَ بِهِمَا ۚ وَمَن تَطَوَّعَ خَيْرًۭا فَإِنَّ ٱللَّهَ شَاكِرٌ عَلِيمٌ
  Unverified discovery rationale: luna: This ayah calls Safa and Marwa signs of God and places them in Hajj and Umrah, making pilgrimage's marked route visible. | terra: Safa and Marwa are God's ritual signs, and their circuit belongs to Hajj or umrah; they broaden the section's marked pilgrimage landscape.
- (2:189) [luna: strong; basis: scene+theme] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ ۗ وَلَيْسَ ٱلْبِرُّ بِأَن تَأْتُوا۟ ٱلْبُيُوتَ مِن ظُهُورِهَا وَلَٰكِنَّ ٱلْبِرَّ مَنِ ٱتَّقَىٰ ۗ وَأْتُوا۟ ٱلْبُيُوتَ مِنْ أَبْوَٰبِهَا ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: The source section's dictionary calls the Hajj season a marker where people gather; this ayah says the new moons are appointed times for people and Hajj, a calendar marker for that gathering.
- (2:196) [luna: strong; terra: strong; basis: root+scene] [cited in ¶65] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: luna: The source section quotes this very rule: complete Hajj and Umrah, and do not release the pilgrim state until الهدي reaches its محل, its appointed place. | terra: Until the hady reaches its mahill directly supplies the section's animal, journey, and appointed arrival.
- (2:197) [luna: strong; terra: medium; basis: scene+theme] ٱلْحَجُّ أَشْهُرٌۭ مَّعْلُومَٰتٌۭ ۚ فَمَن فَرَضَ فِيهِنَّ ٱلْحَجَّ فَلَا رَفَثَ وَلَا فُسُوقَ وَلَا جِدَالَ فِى ٱلْحَجِّ ۗ وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍۢ يَعْلَمْهُ ٱللَّهُ ۗ وَتَزَوَّدُوا۟ فَإِنَّ خَيْرَ ٱلزَّادِ ٱلتَّقْوَىٰ ۚ وَٱتَّقُونِ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: The source section makes the Hajj season a marked time of gathering; this ayah calls Hajj's months known, giving the season a defined calendar place. | terra: Hajj has known months, giving Qur'anic substance to the section's season as a marked time of gathering.
- (2:198) [luna: strong; terra: medium; basis: root+scene+theme] لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ ۚ فَإِذَآ أَفَضْتُم مِّنْ عَرَفَٰتٍۢ فَٱذْكُرُوا۟ ٱللَّهَ عِندَ ٱلْمَشْعَرِ ٱلْحَرَامِ ۖ وَٱذْكُرُوهُ كَمَا هَدَىٰكُمْ وَإِن كُنتُم مِّن قَبْلِهِۦ لَمِنَ ٱلضَّآلِّينَ
  Unverified discovery rationale: luna: This Hajj passage names المشعر الحرام, the sacred landmark, and tells pilgrims to remember God there after leaving Arafat; it closely matches the section's season-as-marker and gathering. | terra: At the Hajj stations people remember God as He guided them after earlier error; rite, gathered place, remembrance, and hidayah converge.
- (2:200) [luna: strong (missing-ayat turn); basis: neighbour+theme] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: luna: This ayah says that after completing the rites pilgrims should remember God; it continues the Hajj season's gathering and links its marked days to the named remembrance developed in the section.
- (2:201) [luna: strong (missing-ayat turn); basis: neighbour+speaker+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: luna: In the same Hajj passage, this ayah gives the petition for good in this life and the Hereafter and protection from the Fire, a prayer for provision and a safe final destination.
