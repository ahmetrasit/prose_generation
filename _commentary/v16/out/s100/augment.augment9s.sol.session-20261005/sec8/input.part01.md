Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 8 of 11 ("Sabah sulaması ve sudan dönüş"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 8 (prose paragraphs numbered) =====
[¶39] Üçüncü ayetin sabahının yanında, bir baskından çok daha sakin bir sabah işi daha duyulur: {ar:صبحت الإبل إذا سقيتها في أول النهار, tr:sabahtu'l-ibile izâ sekaytehâ fî evveli'n-nehâr, gloss:develeri günün başında suladığında "sabahtu'l-ibil" dersin, source:"ص ب ح,B003"}. Sabahleyin içilen şeyin de bir adı vardır: {ar:الصبوح ما يشرب بالغداة, tr:es-sabûhu mâ yuşrabu bi'l-ğadât, gloss:"sabûh", sabah erkenden içilendir, source:"ص ب ح,B003"}. Dördüncü ayetin kelimesinin ailesinde de durgun su vardır: {ar:نقع الماء في منقعه استقر, tr:neka'a'l-mâu fî menka'ihî isteqarra, gloss:su göletinde durdu, source:"ن ق ع,B001"}. Bu su susuzluğu giderir: {ar:ماء ناقع كأنه استقر قراره فكسر الغلة, tr:mâun nâki'un ke-ennehû isteqarra karâruhû fe-kesera'l-ğulle, gloss:"nâkı'" su, yerine oturup yanan susuzluğu kıran sudur, source:"ن ق ع,B002"}. Fiil de aynı anlamdadır: {ar:نقع الماء غلته إذا أروى عطشه, tr:neka'a'l-mâu ğulletehû izâ ervâ atașeh, gloss:su onun yanan susuzluğunu gidermiş, kandırmıştır, source:"ن ق ع,B002"}. Sekizinci ayetteki sevgi kelimesinin ailesinde ise kanana kadar içmek vardır: {ar:شربت الإبل حتى حببت, tr:şeribeti'l-ibilu hattâ habebet, gloss:develer kanıncaya dek içtiler, source:"ح ب ب,B006"}. Kanmanın da bir başlangıcı vardır: {ar:أول الري التحبب, tr:evvelu'r-riyyi't-tehabbub, gloss:kanmanın ilk aşaması "tehabbub"dur, source:"ح ب ب,B006"}. Onuncu ayetin göğüs kelimesinin ailesi bu sahneyi kapatır: {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadru'l-insırâfu ani'l-virdi ve an kulli emr, gloss:"sadr", su başından ve her işten ayrılıp dönmektir, source:"ص د ر,B003"}. Kelime en sade haliyle {ar:صدرت الإبل عن الماء, tr:saderati'l-ibilu ani'l-mâ', gloss:develer sudan döndü, source:"ص د ر,B003"} cümlesinde görülür.

[¶40] Suya iniş ile sudan dönüş, Arapçada iki ayrı fiille anlatılan bir çifttir. Sürü suya gelir, durgun suyun başında kanana kadar içer, sonra döner. Dönüş anı, kimin ne kadar içtiğinin belli olduğu andır. Onuncu ayetin "sudûr" kelimesi anlam olarak göğüslerdir. Ama kelimenin yanında bu dönüş de duyulur: su başında içilen içilmiştir ve şimdi herkes aldığıyla geri döner. Dördüncü ayetin kelimesinin bir deyimi, çok su başı görmüş bir kişiyi tarif eder ve onun bilgisini surenin son kelimesinin fiiliyle anlatır: {ar:إن فلانا لشراب بأنقع يضرب مثلا للرجل الذي قد جرب الأمور وعرفها ومارسها حتى خبرها, tr:inne fulânen le-şerrâbun bi-enku', yudrabu meselen li'r-raculi'llezî kad cerrabe'l-umûra ve arafehâ ve mârasehâ hattâ haberahâ, gloss:"falanca çok göletten içmiştir" sözü, işleri denemiş, tanımış ve onlarla uğraşıp sonunda iç yüzlerini öğrenmiş adam için atasözü olarak söylenir, source:"ن ق ع,B008"}.

[¶41] Kur'an aynı fiili gerçek bir su başında kullanır. Musa Medyen suyuna vardığında sürülerini sulayan bir kalabalık bulur, onların gerisinde de hayvanlarını geri tutan iki kadın görür. Ne istediklerini sorduğunda kadınlar şöyle der: {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌ كَبِيرٌ, tr:lâ neskî hattâ yusdira'r-ri'â', ve ebûnâ şeyhun kebîr, gloss:çobanlar sürülerini sudan çekip götürmedikçe biz sulayamayız; babamız da çok yaşlı biridir, source:28:23}. Aynı kök, yerin altüst edildiği günün anlatımında da geçer. Yer sarsılır, ağırlıklarını dışarı atar, haberlerini anlatır ve sonra {ar:يَوْمَئِذٍ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevme'izin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amelleri kendilerine gösterilsin diye bölük bölük dönüp gelirler, source:99:6}. "Yasduru" fiili, sudan dönen sürünün fiili ile göğüs kelimesiyle aynı köktendir. İnsanlar, yeryüzünün bir su başı gibi bırakıldığı o günde, içtiklerini görmeye döner.

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

===== passages from the discovery list (159) =====
## strong (50)

- (2:60) [luna: strong; terra: strong; basis: scene+theme] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: luna: Each group among Moses' people knows its “مَشْرَبَهُمْ” (drinking place); the verse makes a shared source and differentiated access concrete, as in the herd gathered at water. | terra: Twelve springs issue and قد علم كل أناس مشربهم: every group knows its own drinking place, a precise communal version of measured access to water.
- (2:93) [terra: strong; basis: scene+theme] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱسْمَعُوا۟ ۖ قَالُوا۟ سَمِعْنَا وَعَصَيْنَا وَأُشْرِبُوا۟ فِى قُلُوبِهِمُ ٱلْعِجْلَ بِكُفْرِهِمْ ۚ قُلْ بِئْسَمَا يَأْمُرُكُم بِهِۦٓ إِيمَٰنُكُمْ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: terra: وأشربوا في قلوبهم العجل turns drinking into an inward filling of the heart; it specifically brings the section's drinking scene into the hidden interior later exposed from the breasts.
- (2:249) [luna: strong; terra: strong; basis: contrast+scene+theme] فَلَمَّا فَصَلَ طَالُوتُ بِٱلْجُنُودِ قَالَ إِنَّ ٱللَّهَ مُبْتَلِيكُم بِنَهَرٍۢ فَمَن شَرِبَ مِنْهُ فَلَيْسَ مِنِّى وَمَن لَّمْ يَطْعَمْهُ فَإِنَّهُۥ مِنِّىٓ إِلَّا مَنِ ٱغْتَرَفَ غُرْفَةًۢ بِيَدِهِۦ ۚ فَشَرِبُوا۟ مِنْهُ إِلَّا قَلِيلًۭا مِّنْهُمْ ۚ فَلَمَّا جَاوَزَهُۥ هُوَ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ قَالُوا۟ لَا طَاقَةَ لَنَا ٱلْيَوْمَ بِجَالُوتَ وَجُنُودِهِۦ ۚ قَالَ ٱلَّذِينَ يَظُنُّونَ أَنَّهُم مُّلَٰقُوا۟ ٱللَّهِ كَم مِّن فِئَةٍۢ قَلِيلَةٍ غَلَبَتْ فِئَةًۭ كَثِيرَةًۢ بِإِذْنِ ٱللَّهِ ۗ وَٱللَّهُ مَعَ ٱلصَّٰبِرِينَ
  Unverified discovery rationale: luna: At Talut's river, most are barred from drinking freely and only a handful is permitted; this sharply bounds the section's camels drinking to satiety and makes intake a test. | terra: The river tests Saul's army by the amount each drinks—full drinking, no tasting, or a single handful—so drinking itself reveals who belongs and who fails.
- (3:14) [luna: medium; terra: strong; basis: root+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section names ḥ-b-b through camels drinking until satiation; here “حُبُّ الشَّهَوَاتِ” is directed to possessions including horses, livestock, and crops, making the same animals both thirsty creatures and desired property. | terra: حب الشهوات is adorned through gold, wealth, horses, and الأنعام; love, valuable goods, and herd animals meet in the same inventory, giving concrete substance to the section's love-and-camels word meeting.
- (3:29) [luna: medium; terra: strong; basis: contrast+root+theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section's word al-ṣudūr (root ṣ-d-r) names what is carried within; here what is concealed in breasts or revealed is known, a direct counterpart to contents becoming visible at return. | terra: إن تخفوا ما في صدوركم أو تبدوه يعلمه الله directly sets concealed breast-content against disclosure and divine knowledge, the same inward-to-visible movement as 100:10–11.
- (3:154) [terra: strong; basis: root+theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: ليبتلي الله ما في صدوركم وليمحص ما في قلوبكم makes what lies in breasts subject to trial and purification, a concrete antecedent for the section's image of inward contents being sorted out.
- (7:160) [luna: strong; terra: strong; basis: scene+theme] وَقَطَّعْنَٰهُمُ ٱثْنَتَىْ عَشْرَةَ أَسْبَاطًا أُمَمًۭا ۚ وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ إِذِ ٱسْتَسْقَىٰهُ قَوْمُهُۥٓ أَنِ ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنۢبَجَسَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۚ وَظَلَّلْنَا عَلَيْهِمُ ٱلْغَمَٰمَ وَأَنزَلْنَا عَلَيْهِمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۚ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
  Unverified discovery rationale: luna: This repeats the springs and the groups who know their drinking place, “مَشْرَبَهُمْ”; it supplies another direct scene of organized drinking from a common source. | terra: The twelve tribes receive twelve springs and كل أناس مشربهم, again joining a water source, distinct drinkers, and known shares.
- (11:5) [luna: medium; terra: strong; basis: contrast+root+theme] أَلَآ إِنَّهُمْ يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ ۚ أَلَا حِينَ يَسْتَغْشُونَ ثِيَابَهُمْ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section's chest word is ṣudūr (root ṣ-d-r); this verse says people fold their chests to hide, while God knows what they conceal and declare, giving the chest's hidden contents a concrete disclosure context. | terra: They fold their breasts to hide, yet God knows what they conceal and reveal and is عليم بذات الصدور; the attempted enclosure sharpens the eventual exposure of what breasts hold.
- (15:22) [terra: strong; basis: scene+theme] وَأَرْسَلْنَا ٱلرِّيَٰحَ لَوَٰقِحَ فَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَسْقَيْنَٰكُمُوهُ وَمَآ أَنتُمْ لَهُۥ بِخَٰزِنِينَ
  Unverified discovery rationale: terra: وأسقيناكموه gives the descending water to people as drink while وما أنتم له بخازنين denies that they control its stores, clarifying water as received provision rather than possession.
- (16:6) [luna: strong; terra: strong; basis: scene+theme] وَلَكُمْ فِيهَا جَمَالٌ حِينَ تُرِيحُونَ وَحِينَ تَسْرَحُونَ
  Unverified discovery rationale: luna: The livestock are admired when brought back in the evening and when sent out in the morning; this gives the section's water-bound departure and return a broader pastoral daily rhythm. | terra: Livestock are brought home in the evening and sent out in the morning, حين تريحون وحين تسرحون, supplying the daily herd movement around the section's morning watering and return.
- (16:10) [luna: strong; terra: strong; basis: scene+theme] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
  Unverified discovery rationale: luna: Rainwater is what people drink, and from it grow plants where they pasture their livestock; this joins drinking and herd nourishment in one concrete provision scene. | terra: The same heavenly water gives people drink and grows vegetation in which they pasture livestock, uniting human drinking, water provision, and the herd's feeding ground.
- (23:18) [luna: strong; terra: strong; basis: contrast+scene+theme] وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ ۖ وَإِنَّا عَلَىٰ ذَهَابٍۭ بِهِۦ لَقَٰدِرُونَ
  Unverified discovery rationale: luna: The section's dictionary sense of naqʿ is water settled in its basin; this verse says measured water was lodged in earth and could be taken away, pairing stored water with its vulnerability. | terra: Water descends بقدر and is made to lodge in the earth, فأسكناه في الأرض; measured provision becomes settled water just as the source sense of نَقْع describes water resting in its pool.
- (25:48) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
  Unverified discovery rationale: luna: This neighboring rain verse calls the water “مَاءً طَهُورًا”; it identifies the water in 25:49's land-revival and drinking scene as a provision with a cleansing quality. | terra: God sends the winds before His mercy and sends down ماء طهورا; this ayah identifies the purity and divine origin of the water that 25:49 gives to cattle and people to drink.
- (25:49) [luna: strong; terra: strong; basis: scene+theme] لِّنُحْۦِىَ بِهِۦ بَلْدَةًۭ مَّيْتًۭا وَنُسْقِيَهُۥ مِمَّا خَلَقْنَآ أَنْعَٰمًۭا وَأَنَاسِىَّ كَثِيرًۭا
  Unverified discovery rationale: luna: Rain is sent to revive dead land and “نُسْقِيَهُ ... أَنْعَامًا وَأَنَاسِيَّ كَثِيرًا”; it names livestock and people as recipients of water, like the thirsty herd. | terra: The life-giving water is expressly given as drink to many cattle and people, ونسقيه ... أنعاما وأناسي كثيرا, directly staging divine watering of herds.
- (26:155) [luna: strong; terra: strong; basis: scene+theme] قَالَ هَٰذِهِۦ نَاقَةٌۭ لَّهَا شِرْبٌۭ وَلَكُمْ شِرْبُ يَوْمٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: luna: The section's herd drinks until satiated; Salih's she-camel and the people have separate “شِرْبُ يَوْمٍ مَّعْلُومٍ” (drink on a known day), making each one's access and measure explicit. | terra: The she-camel and the people have separate drinking turns on known days, an exact scene of a herd animal's apportioned access to water.
- (26:156) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+neighbour+scene] وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابُ يَوْمٍ عَظِيمٍۢ
  Unverified discovery rationale: luna: After 26:155 assigns the camel and people their drinking days, this forbids harming her; it marks the boundary around the measured water arrangement. | terra: ولا تمسوها بسوء places a protected boundary around the she-camel and her allotted drinking day in 26:155; harming her turns the watering arrangement into grounds for punishment.
- (26:157) [luna: strong; basis: contrast+neighbour+scene] فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ
  Unverified discovery rationale: luna: After the she-camel is hamstrung, its people become regretful; this completes 26:155-156's regulated drinking scene with its consequence.
- (26:158) [luna: strong; basis: contrast+neighbour+scene] فَأَخَذَهُمُ ٱلْعَذَابُ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ ۖ وَمَا كَانَ أَكْثَرُهُم مُّؤْمِنِينَ
  Unverified discovery rationale: luna: The punishment follows the killing in 26:157; it completes the reversal of the shared, allotted watering arrangement in 26:155.
- (28:23) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶41] وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ وَوَجَدَ مِن دُونِهِمُ ٱمْرَأَتَيْنِ تَذُودَانِ ۖ قَالَ مَا خَطْبُكُمَا ۖ قَالَتَا لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌۭ كَبِيرٌۭ
  Unverified discovery rationale: luna: The section's dictionary verb ṣ-d-r means camels leave the water; here the women wait until the herdsmen “يُصْدِرَ الرِّعَاءُ” (drive their flocks away), making the return from a shared watering place literal. | terra: At the water of Midian, Moses finds a crowd watering and two women holding their animals back; their words لا نسقي حتى يصدر الرعاء directly stage both arrival at water and the ص د ر departure developed by the section.
- (28:24) [luna: strong; terra: strong; basis: neighbour+scene+theme] فَسَقَىٰ لَهُمَا ثُمَّ تَوَلَّىٰٓ إِلَى ٱلظِّلِّ فَقَالَ رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ
