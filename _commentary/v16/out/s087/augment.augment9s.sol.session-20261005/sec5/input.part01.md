Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 5 of 18 ("Rahimde toplanan, düzene konan beden"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 5 (prose paragraphs numbered) =====
[¶22] İkinci ve üçüncü ayetteki fiillerin bedene ait anlamları da vardır. Altıncı ayetteki "okutacağız" fiilinin kökü, rahmin yavrunun üzerine kapanmasını anlatır. Bu anlam en açık haliyle olumsuz cümlelerde görülür: {ar:لم تضم رحمها على ولد, tr:lem tedumma rahimehâ alâ veled, gloss:rahmini bir yavrunun üzerine kapamadı, source:"ق ر ء,B004"}, {ar:ما قرأت الناقة سلى قط, tr:mâ karaeti'n-nâkatu selen katt, gloss:dişi deve hiç yavru zarı toplamadı, source:"ق ر ء,B004"}. خلق, biçimi ortaya çıkmış cenindir: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallakatun ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"}. Biçimi çıkmamış olan için {ar:غير مخلقة لم تصور, tr:ğayru muhallakatin lem tusavvar, gloss:biçimlenmemiş olan, source:"خ ل ق,B003"} denir. سوّى, kusursuz kılınmış bedendir: {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyy elleẕî sevvallâhu halkahû lâ demâmete fîhi ve lâ dâ', gloss:seviyy Allah'ın yaratılışını düzgün kıldığı kişidir; onda ne çirkinlik ne hastalık vardır, source:"س و ي,B002"}. Aynı kök gençliğin doruğuna varmayı da anlatır: {ar:استوى الرجل إذا انتهى شبابه, tr:istevâ'r-raculu iẕe'ntehâ şebâbuh, gloss:adam gençliği tamamlanınca istevâ denir, source:"س و ي,B005"}. قدّر her şeyi kendi ölçüsüne koymaktır: {ar:يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة, tr:yec'aluhâ alâ mikdârin mahsûsin ve vechin mahsûsin hasebe mekteḍati'l-hikme, gloss:onu hikmetin gerektirdiği özel bir miktara ve özel bir biçime koyar, source:"ق د ر,B002"}. Rab, çocuğu evre evre büyütendir: {ar:رببت الصبي أربه, tr:rabebtu's-sabiyye erubbuh, gloss:çocuğu büyüttüm, source:"ر ب ب,B002"}. On altıncı ayetteki الدنيا'nın kökü doğumun yaklaşmasını anlatır: {ar:أدنت الناقة إذا دنا نتاجها, tr:edneti'n-nâkatu iẕâ denâ nitâcuhâ, gloss:dişi devenin doğumu yaklaştı, source:"د ن و,B004"}. On ikinci ayetteki الكبرى'nın kökü de yaşlılığı verir: {ar:الكبر في السن وقد كبر الرجل أي أسن, tr:el-kiber fi's-sinn ve kad kebira'r-racul ey esenne, gloss:kiber yaştaki büyüklüktür; adam yaşlandı, source:"ك ب ر,B004"}. Bu kelimelerin hiçbiri ayetlerinde bedeni anlatmaz. Ama aileleri, surenin yaratma ve düzene koyma fiillerini bir insan ömrünün evreleri olarak da duyurur: rahimde toplanma, biçimlenme, düzgünleşme, olgunluk ve yaşlılık.

[¶23] Kur'an ikinci ayetteki ikiliyi tam olarak cenin için kullanır. Allah insanın başıboş bırakılacağını sanmasını sorgulayan ayetlerde şöyle der: {ar:أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ, tr:e-lem yeku nutfeten min meniyyin yumnâ, gloss:o dökülen meniden bir damla değil miydi, source:75:37}, {ar:ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ, tr:ŝumme kâne alakaten fe-halaka fe-sevvâ, gloss:sonra bir alaka oldu; O da yarattı ve düzene koydu, source:75:38}. Bu kısa bölüm şu soruyla biter: {ar:أَلَيْسَ ذَٰلِكَ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ, tr:e-leyse ẕâlike bi-kâdirin alâ en yuhyiye'l-mevtâ, gloss:bunu yapan ölüleri diriltmeye kadir değil midir, source:75:40}. Üçüncü ayetteki "ölçmek" fiilinin kökü burada güç anlamıyla gelir, on üçüncü ayetteki "yaşamak" fiili de diriltme anlamıyla. Başka bir yerde insana {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:elleẕî halakake fe-sevvâke fe-adeleke, gloss:seni yaratan ve düzene koyup dengeleyen, source:82:7} denir. Yeniden dirilişten şüphe edenlere ise Allah şöyle seslenir: {ar:ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ, tr:ŝumme min mudğatin muhallakatin ve ğayri muhallaka, gloss:sonra biçimlenmiş ve biçimlenmemiş bir et parçasından, source:22:5}. Aynı ayet bazılarının ömrün en düşkün çağına geri itildiğini söyler ve sonra toprağa döner: {ar:فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:fe-iẕâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:üzerine suyu indirdiğimizde titreşip kabarır, source:22:5}. Beden ile otlak tek bir ayette yan yana gelir. İnsanın yaratılışı başka bir yerde {ar:ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ, tr:ŝumme sevvâhu ve nefaha fîhi min rûhih, gloss:sonra onu düzene koydu ve ona kendi ruhundan üfledi, source:32:9} diye anlatılır. İki bahçe benzetmesinde, bahçesine güvenen adama arkadaşı şöyle der: {ar:أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا, tr:e-kefarte billeẕî halakake min turâbin ŝumme min nutfetin ŝumme sevvâke racülâ, gloss:seni topraktan sonra bir damladan yaratan sonra seni bir adam olarak düzene koyanı mı inkâr ettin, source:18:37}. Bu sözlerden birkaç ayet sonra o bahçe yıkılır, hemen ardından da dünya hayatının kuruyan ot benzetmesi gelir. Düzene konmuş beden ile kuruyan otlak Kur'an'da aynı uyarının iki yüzüdür.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (187) =====
## strong (136)

- (2:228) [terra: strong; basis: root+scene+theme] وَٱلْمُطَلَّقَٰتُ يَتَرَبَّصْنَ بِأَنفُسِهِنَّ ثَلَٰثَةَ قُرُوٓءٍۢ ۚ وَلَا يَحِلُّ لَهُنَّ أَن يَكْتُمْنَ مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ إِن كُنَّ يُؤْمِنَّ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَبُعُولَتُهُنَّ أَحَقُّ بِرَدِّهِنَّ فِى ذَٰلِكَ إِنْ أَرَادُوٓا۟ إِصْلَٰحًۭا ۚ وَلَهُنَّ مِثْلُ ٱلَّذِى عَلَيْهِنَّ بِٱلْمَعْرُوفِ ۚ وَلِلرِّجَالِ عَلَيْهِنَّ دَرَجَةٌۭ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ
  Unverified discovery rationale: terra: The waiting period of three قُرُوءٍ uses the ق ر ء family named by the section, while the same ayah forbids women to hide what Allah has created in their wombs; reproductive time, uterine enclosure, and divine creation meet directly.
- (2:233) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene+theme] ۞ وَٱلْوَٰلِدَٰتُ يُرْضِعْنَ أَوْلَٰدَهُنَّ حَوْلَيْنِ كَامِلَيْنِ ۖ لِمَنْ أَرَادَ أَن يُتِمَّ ٱلرَّضَاعَةَ ۚ وَعَلَى ٱلْمَوْلُودِ لَهُۥ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِٱلْمَعْرُوفِ ۚ لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا ۚ لَا تُضَآرَّ وَٰلِدَةٌۢ بِوَلَدِهَا وَلَا مَوْلُودٌۭ لَّهُۥ بِوَلَدِهِۦ ۚ وَعَلَى ٱلْوَارِثِ مِثْلُ ذَٰلِكَ ۗ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍۢ مِّنْهُمَا وَتَشَاوُرٍۢ فَلَا جُنَاحَ عَلَيْهِمَا ۗ وَإِنْ أَرَدتُّمْ أَن تَسْتَرْضِعُوٓا۟ أَوْلَٰدَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّآ ءَاتَيْتُم بِٱلْمَعْرُوفِ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: luna: The source section’s ر ب ب dictionary form is “to rear a child”; this ayah gives that growth a concrete duration by naming mothers’ nursing for two complete years. | terra: Two complete years of nursing are set for one who wishes to complete suckling, while the father bears provision; early bodily growth is given a measured duration and sustained by parental care.
- (2:259) [terra: strong; basis: scene+theme] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: Bones are raised and clothed with flesh before the observer sees that Allah is powerful over all things; bodily reassembly mirrors prenatal building while proving resurrection.
- (2:266) [terra: strong; basis: root+scene+theme] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
  Unverified discovery rationale: terra: Old age reaches the owner of a fruitful garden while his children are weak, and fire destroys the garden; aged body, dependent offspring, vegetation, and perishing provision meet in one warning.
- (3:6) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The section hears creation and proportioning as bodily formation; this ayah directly says God forms people in the wombs however He wills. | terra: هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ locates divinely willed bodily form inside the womb, clarifying what the section means by the fetus acquiring its shape.
- (3:35) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِذْ قَالَتِ ٱمْرَأَتُ عِمْرَٰنَ رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا فَتَقَبَّلْ مِنِّىٓ ۖ إِنَّكَ أَنتَ ٱلسَّمِيعُ ٱلْعَلِيمُ
  Unverified discovery rationale: terra: The wife of Imran dedicates what is in her womb to her Lord, placing the still-hidden child within divine nurture before the delivery and growth narrated in 3:36-37.
- (3:36) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ وَٱللَّهُ أَعْلَمُ بِمَا وَضَعَتْ وَلَيْسَ ٱلذَّكَرُ كَٱلْأُنثَىٰ ۖ وَإِنِّى سَمَّيْتُهَا مَرْيَمَ وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ
  Unverified discovery rationale: terra: At delivery the mother identifies the child as female, names her Mary, and entrusts her offspring to Allah; the hidden womb of 3:35 becomes a born and sexed child whom 3:37 then causes to grow.
- (3:37) [terra: strong; basis: root+scene+theme] فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا ۖ كُلَّمَا دَخَلَ عَلَيْهَا زَكَرِيَّا ٱلْمِحْرَابَ وَجَدَ عِندَهَا رِزْقًۭا ۖ قَالَ يَٰمَرْيَمُ أَنَّىٰ لَكِ هَٰذَا ۖ قَالَتْ هُوَ مِنْ عِندِ ٱللَّهِ ۖ إِنَّ ٱللَّهَ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍ
  Unverified discovery rationale: terra: Mary's Lord accepts her and أَنۢبَتَهَا نَبَاتًا حَسَنًا, causing her to grow as a good growth under care; divine nurture of a child is expressed through the plant image that the section pairs with bodily growth.
- (3:40) [luna: contrast; terra: strong; basis: contrast+root+scene] قَالَ رَبِّ أَنَّىٰ يَكُونُ لِى غُلَٰمٌۭ وَقَدْ بَلَغَنِىَ ٱلْكِبَرُ وَٱمْرَأَتِى عَاقِرٌۭ ۖ قَالَ كَذَٰلِكَ ٱللَّهُ يَفْعَلُ مَا يَشَآءُ
  Unverified discovery rationale: luna: Zakariya likewise asks how he can have a boy when old age has reached him and his wife is barren, making conception at the far end of life a reversal. | terra: Zechariah asks how he can have a boy when بَلَغَنِىَ ٱلْكِبَرُ and his wife is barren; old age and new gestation meet as a divinely crossed bodily boundary.
- (7:11) [luna: strong; terra: strong; basis: root+scene+theme] وَلَقَدْ خَلَقْنَٰكُمْ ثُمَّ صَوَّرْنَٰكُمْ ثُمَّ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ لَمْ يَكُن مِّنَ ٱلسَّٰجِدِينَ
  Unverified discovery rationale: luna: The section reads creation and proportioning bodily; this ayah says God created humans and then formed them, a direct human-form parallel. | terra: Allah says He created and then shaped humankind before the command concerning Adam, presenting bodily form as a distinct completion within creation.
- (7:189) [luna: medium; terra: strong; basis: scene+theme] ۞ هُوَ ٱلَّذِى خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ وَجَعَلَ مِنْهَا زَوْجَهَا لِيَسْكُنَ إِلَيْهَا ۖ فَلَمَّا تَغَشَّىٰهَا حَمَلَتْ حَمْلًا خَفِيفًۭا فَمَرَّتْ بِهِۦ ۖ فَلَمَّآ أَثْقَلَت دَّعَوَا ٱللَّهَ رَبَّهُمَا لَئِنْ ءَاتَيْتَنَا صَٰلِحًۭا لَّنَكُونَنَّ مِنَ ٱلشَّٰكِرِينَ
  Unverified discovery rationale: luna: The section follows human formation as a life stage; this ayah describes a spouse bearing a light burden that later grows heavier, a concrete pregnancy progression. | terra: A light pregnancy becomes heavy before the parents ask for a sound child, presenting gestation as gradual bodily accumulation and completion within the single-soul creation story.
- (10:24) [luna: strong; terra: strong; basis: scene+theme] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: This ayah repeats the section’s growth-and-decay image: rain adorns the land with plants, then they are harvested and vanish, making visible what passes. | terra: The likeness of worldly life joins rain, earth's growth, human and animal food, full adornment, and sudden cutting down; it illuminates the section's move from formed body to transient pasture.
- (11:72) [terra: strong; basis: contrast+root+scene] قَالَتْ يَٰوَيْلَتَىٰٓ ءَأَلِدُ وَأَنَا۠ عَجُوزٌۭ وَهَٰذَا بَعْلِى شَيْخًا ۖ إِنَّ هَٰذَا لَشَىْءٌ عَجِيبٌۭ
  Unverified discovery rationale: terra: Sarah's amazement joins her own old age to an aged husband at the announcement of a child, placing birth at the far end of the ordinary life sequence.
- (12:22) [terra: strong (missing-ayat turn); basis: scene+theme] وَلَمَّا بَلَغَ أَشُدَّهُۥٓ ءَاتَيْنَٰهُ حُكْمًۭا وَعِلْمًۭا ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُحْسِنِينَ
  Unverified discovery rationale: terra: When Joseph reaches full strength, Allah gives him judgment and knowledge; it is a repeated formulation of mature bodily arrival, though without 28:14's additional word for full development.
- (13:8) [luna: strong; terra: strong; basis: root+scene+theme] ٱللَّهُ يَعْلَمُ مَا تَحْمِلُ كُلُّ أُنثَىٰ وَمَا تَغِيضُ ٱلْأَرْحَامُ وَمَا تَزْدَادُ ۖ وَكُلُّ شَىْءٍ عِندَهُۥ بِمِقْدَارٍ
  Unverified discovery rationale: luna: The section’s ق د ر root means setting things to a measure; this ayah joins what wombs decrease or increase to the claim that all things are with God by measure. | terra: Allah knows what every female bears, what wombs diminish or increase, and declares that everything with Him has a measure; this joins the hidden womb to the section's قدّر as exact apportioning.
- (14:3) [terra: strong (missing-ayat turn); basis: speaker+theme] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
  Unverified discovery rationale: terra: Those who prefer worldly life over the Hereafter and turn others from Allah's way enact the same preference named in 87:16, here joined to active distortion of guidance.
- (14:39) [terra: strong; basis: contrast+root+scene] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى وَهَبَ لِى عَلَى ٱلْكِبَرِ إِسْمَٰعِيلَ وَإِسْحَٰقَ ۚ إِنَّ رَبِّى لَسَمِيعُ ٱلدُّعَآءِ
  Unverified discovery rationale: terra: Abraham praises Allah for granting Ishmael and Isaac عَلَى ٱلْكِبَرِ; offspring arriving in old age makes the section's two distant bodily stages coincide.
- (15:28) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى خَٰلِقٌۢ بَشَرًۭا مِّن صَلْصَٰلٍۢ مِّنْ حَمَإٍۢ مَّسْنُونٍۢ
  Unverified discovery rationale: luna: The section’s formed-body image connects to the preceding announcement of a human being created from clay; the next ayah gives the forming and spirit-breathing detail. | terra: Allah announces that He is creating a human from clay, supplying the bodily referent that 15:29 then proportions and breathes into.
- (15:29) [luna: strong; terra: strong; basis: root+scene+theme] فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ
