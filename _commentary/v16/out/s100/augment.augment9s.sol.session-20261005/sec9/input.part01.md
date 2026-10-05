Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 9 of 11 ("Toplanmış kalabalık ve toplanma günü"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 9 (prose paragraphs numbered) =====
[¶42] Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesi baskına uğrayan kalabalıktır: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'", insan topluluğunun adıdır, source:"ج م ع,B002"}. Aynı kök insanların toplandığı yeri ve günü de adlandırır: {ar:المجمع حيث يجمع الناس, tr:el-mecma'u haysu yucma'u'n-nâs, gloss:"mecma'", insanların toplandığı yerdir, source:"ج م ع,B004"}. Bu yerin ve günün en büyüğü de bu kökle anılır: {ar:يوم الجمع ويوم يجمعكم ليوم الجمع, tr:yevmu'l-cem'i ve yevme yecme'ukum li-yevmi'l-cem', gloss:"toplanma günü" ve "sizi toplanma günü için toplayacağı gün", source:"ج م ع,B004"}. Beşinci ayetin fiili, bir şeyin iki kenarı arasında kalan yeri adlandıran bir köke dayanır: {ar:اسما لما بين طرفي كل شيء, tr:isman li-mâ beyne tarafey kulli şey', gloss:her şeyin iki ucu arasındakinin adı, source:"و س ط,B002"}. Atlar kalabalığın iki kenarı arasında, tam ortasında durur. Yedinci ayetin tanık kelimesinin kökü de bir toplanma yerinin adıdır: {ar:المشهد مجمع الناس, tr:el-meşhedu mecma'u'n-nâs, gloss:"meşhed", insanların toplandığı yerdir, source:"ش ه د,B001"}. Fiil hazır bulunmayı anlatır: {ar:شهده شهودا أي حضره, tr:şehidehû şuhûden, ey hadarah, gloss:"şehidehû", yani orada hazır bulundu, source:"ش ه د,B001"}. Onuncu ayetin fiili de bir toplamadır: {ar:أصل واحد منقاس وهو جمع الشيء, tr:aslun vâhidun munkâs, ve huve cem'u'ş-şey', gloss:tek ve kuralı işleyen bir köktür; bir şeyi toplamaktır, source:"ح ص ل,B001"}. On birinci ayetteki {ar:يَوْمَئِذٍ, tr:yevme'izin, gloss:o gün, source:100:11} ise bütün bunları bir güne bağlar.

[¶43] Bu görüntünün sureye kattığı şey bir ölçek değişimidir. Beşinci ayette atlar bir obanın, belki birkaç çadırlık bir halkın ortasına dalar. Surenin sonundaki gün ise bütün insanların toplandığı gündür. Önce bir kalabalık şaşkınlıkla yakalanır, sonra herkes bir araya getirilir. Düz bir anlatım baskının yalnızca bir savaş sahnesi olduğunu söylerdi. Kökler ise aynı kelimeyi o büyük toplanmaya doğru açık tutar.

[¶44] Kur'an bu toplanmayı beşinci ayetin kelimesiyle, aynı biçimde anlatır. Bir seddin yerle bir edileceği vaadinin ardından şöyle denir: {ar:وَنُفِخَ فِى ٱلصُّورِ فَجَمَعْنَٰهُمْ جَمْعًا, tr:ve nufiha fi's-sûri fe-cema'nâhum cem'â, gloss:sura üfürüldü ve onları hep birlikte topladık, source:18:99}. Yok edilen kavimlerin hikâyeleri anlatıldıktan sonra da o gün iki kökle birden anılır: {ar:ذَٰلِكَ يَوْمٌ مَّجْمُوعٌ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌ مَّشْهُودٌ, tr:zâlike yevmun mecmû'un lehu'n-nâsu ve zâlike yevmun meşhûd, gloss:o, insanların kendisi için toplandığı bir gündür; o, herkesin hazır bulunduğu bir gündür, source:11:103}. Bu ayette beşinci ayetin kökü ile yedinci ayetin kökü yan yana durur. O günün adı da verilir: {ar:يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ, tr:yevme yecme'ukum li-yevmi'l-cem', zâlike yevmu't-teğâbun, gloss:sizi toplanma günü için toplayacağı gün; o, kazancın ve kaybın ortaya çıktığı gündür, source:64:9}. Toplanmanın nasıl olacağı da anlatılır: {ar:وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ, tr:ve nufiha fi's-sûri fe-izâ hum mine'l-ecdâsi ilâ rabbihim yensilûn, gloss:sura üfürülür ve onlar kabirlerinden Rablerine doğru akın akın koşarlar, source:36:51}. Bu ayette de "Rableri" kelimesi geçer, tıpkı on birinci ayette olduğu gibi. Toplanış tek bir sesle tamamlanır: {ar:إِن كَانَتْ إِلَّا صَيْحَةً وَٰحِدَةً فَإِذَا هُمْ جَمِيعٌ لَّدَيْنَا مُحْضَرُونَ, tr:in kânet illâ sayhaten vâhideten fe-izâ hum cemî'un ledeynâ muhdarûn, gloss:yalnızca tek bir çığlık olur ve hepsi birden huzurumuza getirilir, source:36:53}.

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: chain 7 (rain on the land) as its own section - merged into chain 6 as one image of kenûd
- not developed: chain 9 (shared pot) as its own section - merged into chain 8 as the counter-scene of the closed hand
- not developed: غ ي ر B001 "God's rain/provision" member in chains 6 and 7 - wrong root for al-mughīrāt, dropped
- not developed: ضبح as owl and echo calls (chain 4) - relies on pre-Islamic lore outside the Quran, dropped
- not developed: ربيون "great crowds" (chain 11) - too loose a link to rabb, dropped
- not developed: the map's meysir lore (chain 9) and its commentators remark (chain 6) - reports from outside the Quran, dropped
- memory: al-mughīrāt is the form IV participle of أغار "to raid", root غ و ر
- memory: غار يغير "to provide rain" is a separate verb and not the root of al-mughīrāt
- memory: the preposition عن in 38:32 can mean both "because of" and "away from"

===== passages from the discovery list (246) =====
## strong (122)

- (2:143) [luna: medium; terra: strong; basis: root+theme] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: luna: The source section reads the root و-س-ط spatially as the place between two sides; this ayah calls the community an أمة وسطا and immediately makes it a witness-community over humanity. Its distinct ethical sense links centrality to the section's other root ش-ه-د, while remaining different from the horses' position in a crowd. | terra: أُمَّةً وَسَطًا ... شُهَدَاءَ عَلَى النَّاسِ unites both roots developed by the section: being in the middle and bearing witness over humanity.
- (2:148) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] وَلِكُلٍّۢ وِجْهَةٌ هُوَ مُوَلِّيهَا ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ أَيْنَ مَا تَكُونُوا۟ يَأْتِ بِكُمُ ٱللَّهُ جَمِيعًا ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The source section's root ج-م-ع opens a local human crowd toward the final gathering; this ayah says that wherever people are, God will bring them all together (جميعا). It makes the assembly universal across places. | terra: Wherever people may be, يَأْتِ بِكُمُ اللَّهُ جَمِيعًا promises their convergence from every location into a single divine summons.
- (2:284) [terra: strong (missing-ayat turn); basis: speaker+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: Whether people disclose or conceal what is within themselves, God calls them to account for it, closely matching the collected contents of breasts.
- (3:9) [luna: strong; terra: strong; basis: root+scene+speaker] رَبَّنَآ إِنَّكَ جَامِعُ ٱلنَّاسِ لِيَوْمٍۢ لَّا رَيْبَ فِيهِ ۚ إِنَّ ٱللَّهَ لَا يُخْلِفُ ٱلْمِيعَادَ
  Unverified discovery rationale: luna: The source section says the root ج-م-ع names the final gathering; the prayer here calls God جامع الناس for a day about which there is no doubt. It gives the crowd's gathering a universal and certain horizon. | terra: The prayer addresses رَبَّنَا as جَامِعُ النَّاسِ for an unquestionable day, matching the section's movement from their Lord to all humanity gathered.
- (3:13) [luna: strong; basis: root+scene] قَدْ كَانَ لَكُمْ ءَايَةٌۭ فِى فِئَتَيْنِ ٱلْتَقَتَا ۖ فِئَةٌۭ تُقَٰتِلُ فِى سَبِيلِ ٱللَّهِ وَأُخْرَىٰ كَافِرَةٌۭ يَرَوْنَهُم مِّثْلَيْهِمْ رَأْىَ ٱلْعَيْنِ ۚ وَٱللَّهُ يُؤَيِّدُ بِنَصْرِهِۦ مَن يَشَآءُ ۗ إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّأُو۟لِى ٱلْأَبْصَٰرِ
  Unverified discovery rationale: luna: The source section describes horses penetrating the middle of a human crowd; this ayah names the two hosts who met at Badr (التقى الجمعان), one fighting for God and one disbelieving. It gives the battle-crowd image a direct Qur'anic counterpart.
- (3:25) [luna: strong; terra: strong; basis: root+scene+theme] فَكَيْفَ إِذَا جَمَعْنَٰهُمْ لِيَوْمٍۢ لَّا رَيْبَ فِيهِ وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: luna: The source section opens جَمْعًا from a battle crowd toward the final day; this ayah asks what it will be like when people are gathered for a doubtless day and each soul is repaid in full. The verse makes the assembly a setting for reckoning. | terra: فَكَيْفَ إِذَا جَمَعْنَاهُمْ describes an unquestionable day when every soul is paid fully, giving purpose to the section's universal collection.
- (3:30) [luna: medium (missing-ayat turn); terra: strong; basis: root+theme] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: luna: The source section says what is in the breasts is collected on the day; this ayah says each soul will find the good and evil it did present before it. It gives a concrete disclosure of each person's record. | terra: On the day each soul finds its good and evil مُحْضَرًا, inward moral contents become present objects from which it cannot distance itself.
- (3:155) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+root+scene] إِنَّ ٱلَّذِينَ تَوَلَّوْا۟ مِنكُمْ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ إِنَّمَا ٱسْتَزَلَّهُمُ ٱلشَّيْطَٰنُ بِبَعْضِ مَا كَسَبُوا۟ ۖ وَلَقَدْ عَفَا ٱللَّهُ عَنْهُمْ ۗ إِنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
  Unverified discovery rationale: luna: The source section pictures a crowd caught by a raid; this ayah recalls the day the two groups met (التقى الجمعان) and says some turned away. It supplies the reversal of a crowd's cohesion under pressure. | terra: The people who turned back on the day the two hosts met locate moral failure inside the same battlefield meeting of gathered crowds.
- (3:166) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene] وَمَآ أَصَٰبَكُمْ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ فَبِإِذْنِ ٱللَّهِ وَلِيَعْلَمَ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: The source section's crowd is a human group caught in battle; this ayah refers to the day the two groups met and says what befell them was by God's permission. It frames a battle crowd's fate as more than its visible force. | terra: What struck the believers on the day the two hosts met occurred by God's permission, another exact battlefield use of the gathered-crowd formula.
- (4:41) [luna: strong; terra: strong; basis: root+scene+theme] فَكَيْفَ إِذَا جِئْنَا مِن كُلِّ أُمَّةٍۭ بِشَهِيدٍۢ وَجِئْنَا بِكَ عَلَىٰ هَٰٓؤُلَآءِ شَهِيدًۭا
  Unverified discovery rationale: luna: The source section's witness-root ش-ه-د describes being present; this ayah asks what it will be like when a witness is brought from every community and the Messenger is a witness over his people. It turns the gathered communities into witnesses and the witnessed. | terra: A witness is brought مِنْ كُلِّ أُمَّةٍ and the Messenger is brought as witness over these people, populating the universal assembly with its witnesses.
- (4:87) [luna: strong; terra: strong; basis: root+scene+speaker] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۗ وَمَنْ أَصْدَقُ مِنَ ٱللَّهِ حَدِيثًۭا
  Unverified discovery rationale: luna: The source section connects the human جمع to the Day of Gathering; this ayah says God will surely gather people for the Day of Resurrection. Its direct root wording confirms that the crowd-word reaches the final assembly. | terra: God promises لَيَجْمَعَنَّكُمْ إِلَى يَوْمِ الْقِيَامَةِ and grounds it in His uniquely truthful speech, a direct formulation of the great gathering.
- (4:140) [luna: strong (missing-ayat turn); basis: contrast+root+scene] وَقَدْ نَزَّلَ عَلَيْكُمْ فِى ٱلْكِتَٰبِ أَنْ إِذَا سَمِعْتُمْ ءَايَٰتِ ٱللَّهِ يُكْفَرُ بِهَا وَيُسْتَهْزَأُ بِهَا فَلَا تَقْعُدُوا۟ مَعَهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦٓ ۚ إِنَّكُمْ إِذًۭا مِّثْلُهُمْ ۗ إِنَّ ٱللَّهَ جَامِعُ ٱلْمُنَٰفِقِينَ وَٱلْكَٰفِرِينَ فِى جَهَنَّمَ جَمِيعًا
  Unverified discovery rationale: luna: The source section moves from a crowded human group to the day of gathering; this ayah says God will gather the hypocrites and disbelievers together in Hell (جامع المنافقين والكافرين). It gives the assembly a specifically punitive destination.
- (5:109) [terra: strong; basis: root+scene+theme] ۞ يَوْمَ يَجْمَعُ ٱللَّهُ ٱلرُّسُلَ فَيَقُولُ مَاذَآ أُجِبْتُمْ ۖ قَالُوا۟ لَا عِلْمَ لَنَآ ۖ إِنَّكَ أَنتَ عَلَّٰمُ ٱلْغُيُوبِ
  Unverified discovery rationale: terra: يَوْمَ يَجْمَعُ اللَّهُ الرُّسُلَ depicts a particular assembly within the universal day and immediately questions its witnesses about their reception.
- (5:117) [terra: strong; basis: contrast+root+scene] مَا قُلْتُ لَهُمْ إِلَّا مَآ أَمَرْتَنِى بِهِۦٓ أَنِ ٱعْبُدُوا۟ ٱللَّهَ رَبِّى وَرَبَّكُمْ ۚ وَكُنتُ عَلَيْهِمْ شَهِيدًۭا مَّا دُمْتُ فِيهِمْ ۖ فَلَمَّا تَوَفَّيْتَنِى كُنتَ أَنتَ ٱلرَّقِيبَ عَلَيْهِمْ ۚ وَأَنتَ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
  Unverified discovery rationale: terra: Jesus says he was شَهِيدًا only مَا دُمْتُ فِيهِمْ; his witness depended on presence among the people, while God's witness continues after his departure.
- (6:12) [luna: strong; terra: strong; basis: root+scene+theme] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
  Unverified discovery rationale: luna: The source section contrasts a small attacked people with the gathering of all humanity; this ayah says God will surely assemble people for the Resurrection Day, with no doubt in it. It makes the final assembly the scale beyond any tribe. | terra: لَيَجْمَعَنَّكُمْ إِلَى يَوْمِ الْقِيَامَةِ follows the statement that mercy is written upon God, placing universal gathering under that lordly relation.
- (6:22) [luna: strong; terra: strong; basis: scene+theme] وَيَوْمَ نَحْشُرُهُمْ جَمِيعًۭا ثُمَّ نَقُولُ لِلَّذِينَ أَشْرَكُوٓا۟ أَيْنَ شُرَكَآؤُكُمُ ٱلَّذِينَ كُنتُمْ تَزْعُمُونَ
  Unverified discovery rationale: luna: The source section turns an attacked crowd into humanity gathered before God; here God gathers everyone and asks the idolaters where their claimed partners are. The assembled crowd faces the collapse of its former affiliations. | terra: وَيَوْمَ نَحْشُرُهُمْ جَمِيعًا stages everyone together before God, who then addresses the associators inside that assembled scene.
- (6:73) [terra: strong (missing-ayat turn); basis: contrast+root+scene] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
  Unverified discovery rationale: terra: The trumpet-day belongs to the knower of the unseen and the witnessed, joining resurrection's summons to the boundary between hidden and manifest.
- (6:128) [luna: strong; terra: strong; basis: contrast+scene+theme] وَيَوْمَ يَحْشُرُهُمْ جَمِيعًۭا يَٰمَعْشَرَ ٱلْجِنِّ قَدِ ٱسْتَكْثَرْتُم مِّنَ ٱلْإِنسِ ۖ وَقَالَ أَوْلِيَآؤُهُم مِّنَ ٱلْإِنسِ رَبَّنَا ٱسْتَمْتَعَ بَعْضُنَا بِبَعْضٍۢ وَبَلَغْنَآ أَجَلَنَا ٱلَّذِىٓ أَجَّلْتَ لَنَا ۚ قَالَ ٱلنَّارُ مَثْوَىٰكُمْ خَٰلِدِينَ فِيهَآ إِلَّا مَا شَآءَ ٱللَّهُ ۗ إِنَّ رَبَّكَ حَكِيمٌ عَلِيمٌۭ
  Unverified discovery rationale: luna: The source section scales a human crowd up to a universal gathering; this ayah gathers jinn and humans together and has the jinn acknowledge the people who followed them. It broadens the assembly and exposes the relation between its two groups. | terra: وَيَوْمَ يَحْشُرُهُمْ جَمِيعًا gathers jinn and humans together, making the section's all-human scale still wider and exposing their relations.
- (6:130) [terra: strong; basis: root+scene+theme] يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَقُصُّونَ عَلَيْكُمْ ءَايَٰتِى وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ شَهِدْنَا عَلَىٰٓ أَنفُسِنَا ۖ وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
  Unverified discovery rationale: terra: In the assembled address to jinn and humans, شَهِدْنَا عَلَى أَنْفُسِنَا makes the gathered beings testify against themselves about meeting this day.
