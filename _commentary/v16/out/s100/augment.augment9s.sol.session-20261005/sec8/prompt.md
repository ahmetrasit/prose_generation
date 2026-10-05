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
  Unverified discovery rationale: luna: This completes 28:23's waiting at the watering place: Moses waters the women's flock, then “تَوَلَّىٰ إِلَى الظِّلِّ” (withdraws to the shade), joining watering to departure. | terra: Moses فسقى لهما, then turns away from the water and asks his Lord for whatever خير He sends; watering, departure, and the surah's الخير meet within the same continued scene.
- (28:25) [terra: strong; basis: neighbour+scene+theme] فَجَآءَتْهُ إِحْدَىٰهُمَا تَمْشِى عَلَى ٱسْتِحْيَآءٍۢ قَالَتْ إِنَّ أَبِى يَدْعُوكَ لِيَجْزِيَكَ أَجْرَ مَا سَقَيْتَ لَنَا ۚ فَلَمَّا جَآءَهُۥ وَقَصَّ عَلَيْهِ ٱلْقَصَصَ قَالَ لَا تَخَفْ ۖ نَجَوْتَ مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: terra: The Midian scene continues when Moses is summoned so that he may be repaid أجر ما سقيت لنا; the act performed at the watering place returns to its doer as a known recompense.
- (31:23) [terra: strong (missing-ayat turn); basis: root+theme] وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: إلينا مرجعهم فننبئهم بما عملوا is immediately joined to divine knowledge of ذات الصدور, bringing return, disclosure of deeds, and what breasts contain into the same sequence as the section's water-source analogy.
- (38:32) [terra: strong; basis: neighbour+root+scene+theme] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
  Unverified discovery rationale: terra: إني أحببت حب الخير uses the same love-of-good wording as 100:8 in the midst of a horse scene, letting animal wealth embody the “good” that absorbs love.
- (38:42) [luna: strong; basis: scene] ٱرْكُضْ بِرِجْلِكَ ۖ هَٰذَا مُغْتَسَلٌۢ بَارِدٌۭ وَشَرَابٌۭ
  Unverified discovery rationale: luna: Job is given “مُغْتَسَلٌ بَارِدٌ وَشَرَابٌ” (a cool bath and drink); the spring answers bodily need with both refreshment and drinking.
- (39:7) [terra: strong; basis: root+theme] إِن تَكْفُرُوا۟ فَإِنَّ ٱللَّهَ غَنِىٌّ عَنكُمْ ۖ وَلَا يَرْضَىٰ لِعِبَادِهِ ٱلْكُفْرَ ۖ وَإِن تَشْكُرُوا۟ يَرْضَهُ لَكُمْ ۗ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: This ayah joins return to the Lord, being told what one did, and إنه عليم بذات الصدور, closely paralleling departure from the water, disclosure of what was taken, and knowledge of breasts.
- (40:80) [terra: strong; basis: neighbour+root+scene+theme] وَلَكُمْ فِيهَا مَنَٰفِعُ وَلِتَبْلُغُوا۟ عَلَيْهَا حَاجَةًۭ فِى صُدُورِكُمْ وَعَلَيْهَا وَعَلَى ٱلْفُلْكِ تُحْمَلُونَ
  Unverified discovery rationale: terra: Livestock carry people so they may reach حاجة في صدوركم; the moving herd and what is held in breasts occur together, a striking meeting of the section's animal movement and literal صُدور.
- (54:27) [luna: strong; terra: strong; basis: neighbour+scene+theme] إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ
  Unverified discovery rationale: luna: This introduces Salih's she-camel as a test, which the neighboring 54:28 places at a divided water source; it identifies the animal whose watering turn is measured there. | terra: The she-camel is sent فتنة لهم immediately before the divided-water rule, identifying the animal and making the watering arrangement a test rather than a neutral drink.
- (54:28) [luna: strong; terra: strong; basis: scene+theme] وَنَبِّئْهُمْ أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ ۖ كُلُّ شِرْبٍۢ مُّحْتَضَرٌۭ
  Unverified discovery rationale: luna: “الْمَاءَ قِسْمَةٌ بَيْنَهُمْ” divides the water between the people and the she-camel, and each drink is attended; this gives a precise counterpart to knowing who drank and returned with what. | terra: الماء قسمة بينهم and كل شرب محتضر make water an allotted share whose drinking turn is attended, directly matching the section's concern with who drinks, how much, and its being known.
- (54:29) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+neighbour+scene] فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ
  Unverified discovery rationale: luna: After 54:28 divides the water, the people call their companion and he hamstrings the camel; this shows the violent reversal of a shared watering order. | terra: The people summon their companion and he hamstrings the she-camel, recording the concrete breach of the water-sharing test established in 54:27–28.
- (54:30) [luna: strong; basis: contrast+neighbour+scene] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
  Unverified discovery rationale: luna: This asks how the punishment and warnings were; it follows the hamstringing of the camel whose water share 54:28 had regulated.
- (54:31) [luna: strong; basis: contrast+neighbour+scene] إِنَّآ أَرْسَلْنَا عَلَيْهِمْ صَيْحَةًۭ وَٰحِدَةًۭ فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ
  Unverified discovery rationale: luna: A single blast leaves them like dry stalks; this completes the destruction following their rejection of the water-sharing order in 54:28-29.
- (56:68) [luna: strong; terra: strong; basis: scene+theme] أَفَرَءَيْتُمُ ٱلْمَآءَ ٱلَّذِى تَشْرَبُونَ
  Unverified discovery rationale: luna: “الْمَاءَ الَّذِي تَشْرَبُونَ” asks the reader to consider the water they drink; it recalls the section's focus on drinking water as a bodily need. | terra: أفرأيتم الماء الذي تشربون asks the drinker to look at the very water consumed, turning the section's ordinary act of quenching thirst into evidence about giver and receiver.
- (56:69) [luna: strong; terra: medium; basis: neighbour+scene+theme] ءَأَنتُمْ أَنزَلْتُمُوهُ مِنَ ٱلْمُزْنِ أَمْ نَحْنُ ٱلْمُنزِلُونَ
  Unverified discovery rationale: luna: This continues 56:68 by asking who brings down the drinking water from clouds; it locates the source of the water whose drinkability the prior ayah asks us to notice. | terra: أأنتم أنزلتموه من المزن أم نحن المنزلون identifies the giver of the water considered in 56:68, so the drinker's acquired share cannot be credited to the drinker.
- (56:70) [luna: strong; terra: contrast; basis: contrast+neighbour+scene+theme] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
  Unverified discovery rationale: luna: The continuation says God could make that water “أُجَاجًا” (bitter); it marks the boundary between drink that quenches and water that cannot serve the section's purpose. | terra: لو نشاء جعلناه أجاجا makes bitterness a possible reversal of the drinkable water in 56:68 and ends by asking for gratitude, fitting the surah's concern with received good and ingratitude.
- (64:4) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+root+theme] يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ ۚ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: God knows what is concealed or declared and what is in breasts; this gives the section's collected chest contents a concrete account of hidden and shown things. | terra: God knows what people conceal and declare and is عليم بذات الصدور; the explicit concealed-to-declared opposition makes this a repeated formulation of the inward disclosure developed in the section.
- (67:13) [luna: medium; terra: strong; basis: contrast+root+theme] وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: Whether speech is concealed or voiced, God knows what is in breasts; this directly meets the section's chest word and its movement from hidden contents to disclosure. | terra: Whether speech is concealed or declared, God knows بذات الصدور; hidden inward content and its complete knowability match what the section hears behind the breasts being brought out.
- (67:14) [terra: strong; basis: neighbour+root+theme] أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ
  Unverified discovery rationale: terra: ألا يعلم من خلق ... الخبير grounds the knowledge of breasts in 67:13 in the Creator's being Khabir, meeting the source proverb's خبرها—knowledge that fully reaches a matter's inside.
- (72:16) [terra: strong; basis: scene+theme] وَأَلَّوِ ٱسْتَقَٰمُوا۟ عَلَى ٱلطَّرِيقَةِ لَأَسْقَيْنَٰهُم مَّآءً غَدَقًۭا
  Unverified discovery rationale: terra: ماء غدقا promises abundant water as a divinely given drink, bringing the section's satiation image into a conditional gift.
- (72:17) [terra: strong; basis: neighbour+theme] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
  Unverified discovery rationale: terra: لنفتنهم فيه states that the abundant water of 72:16 would itself be a test, as the section makes what one receives at the water source reveal the drinker.
- (89:20) [luna: medium; terra: strong; basis: contrast+root+theme] وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
  Unverified discovery rationale: luna: The section's ḥ-b-b dictionary branch is the first stage of a camel's satiety; here the root names intense love of wealth, a specific but analogical contrast between bodily satisfaction and attachment to goods. | terra: وتحبون المال حبا جما states intense love of wealth directly, a close formulation of the surah's شديد love of الخير and the appetite heard in the section's satiation branch of ح ب ب.
- (91:13) [luna: strong; terra: strong; basis: scene+theme] فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
  Unverified discovery rationale: luna: Salih warns them about God's she-camel and “سُقْيَاهَا” (her drink); it makes the animal's access to water a specific obligation, as in the section's herd scene. | terra: ناقة الله وسقياها names the she-camel together with her right to drink, concentrating the section's camel-and-watering image in one warning.
- (91:14) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+neighbour+scene] فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
  Unverified discovery rationale: luna: The people deny the warning and hamstring the she-camel from 91:13; this is the explicit opposite of respecting the animal's drinking share. | terra: They deny the messenger and hamstring the she-camel after the warning about her watering right; the ayah contributes the rejection and leveling punishment that follow violation of the drink.
- (99:1) [luna: strong; basis: neighbour+scene] إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
  Unverified discovery rationale: luna: The section links the people's return in 99:6 to an earth left like a watering place; this neighbor supplies the quake that opens that scene: “زُلْزِلَتِ الْأَرْضُ”.
- (99:2) [luna: strong; basis: neighbour+scene] وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
  Unverified discovery rationale: luna: This continues the earth's upheaval before the return of 99:6: it casts out its “أَثْقَالَهَا” (burdens), like a source emptied before people come to see what it held.
- (99:3) [luna: strong; basis: neighbour+scene] وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
  Unverified discovery rationale: luna: The human asks “مَا لَهَا” after the earth's upheaval; this is the response between its expelling burdens and its report, which 99:6 follows with people's return to see deeds.
- (99:4) [luna: strong; basis: neighbour+scene] يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
  Unverified discovery rationale: luna: The earth “تُحَدِّثُ أَخْبَارَهَا” (relates its news); this is the report that completes the section's comparison of earth as a water place whose contents are disclosed before people see their deeds in 99:6.
- (99:5) [luna: strong; basis: neighbour+theme] بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
  Unverified discovery rationale: luna: This says the earth speaks because its Lord inspires it; it completes 99:4's report and grounds the section's image of the earth disclosing what it held.
- (99:6) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶41] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
  Unverified discovery rationale: luna: The section's ṣ-d-r root is used here in “يَصْدُرُ النَّاسُ أَشْتَاتًا”; people leave in groups to see their deeds, turning the herd's return with its intake into a scene of return with one's acts. | terra: يصدر الناس أشتاتا uses the same ص د ر departure as a herd leaving water, but now people depart in groups so that their deeds may be shown—the section's explicit judgmental transformation of the watering scene.
- (99:7) [luna: strong; terra: strong; basis: neighbour+theme] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
  Unverified discovery rationale: luna: After 99:6 says people return to see their deeds, this specifies that even an atom's weight of good is seen, giving the return a precise measure. | terra: This ayah specifies what the departing groups of 99:6 are shown: each person sees even an atom's weight of good, sharpening the section's claim that the return discloses what each one took away.
- (99:8) [luna: strong; terra: strong; basis: neighbour+theme] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
  Unverified discovery rationale: luna: This completes 99:7 with the same measure for evil; the section's image of each one returning with what was taken now has an explicit good-and-evil accounting. | terra: This completes the accounting begun in 99:6 by making even an atom's weight of evil visible; nothing carried from the lived “watering place” escapes disclosure.

## medium (63)

- (2:61) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
  Unverified discovery rationale: luna: After the springs and instruction to eat and drink in 2:60, the people say they cannot bear one food and ask for other produce; this contrasts human dissatisfaction with the section's animal reaching satiety.
- (3:121) [luna: medium; basis: scene] وَإِذْ غَدَوْتَ مِنْ أَهْلِكَ تُبَوِّئُ ٱلْمُؤْمِنِينَ مَقَٰعِدَ لِلْقِتَالِ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The verse says Muhammad went out from his household at dawn to arrange believers for battle; it gives another specific morning departure beside the section's raid and quieter watering task.
- (7:31) [luna: weak (missing-ayat turn); terra: medium; basis: contrast+scene+theme] ۞ يَٰبَنِىٓ ءَادَمَ خُذُوا۟ زِينَتَكُمْ عِندَ كُلِّ مَسْجِدٍۢ وَكُلُوا۟ وَٱشْرَبُوا۟ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
  Unverified discovery rationale: luna: The link is analogical: the section shows camels drinking to the onset of satiety, while this command sets a boundary on human eating and drinking by forbidding excess. | terra: كلوا واشربوا ولا تسرفوا places a limit on drinking; it supports the section's attention to quantity by making excess at the drink a morally meaningful boundary.
- (9:120) [terra: medium; basis: scene+theme] مَا كَانَ لِأَهْلِ ٱلْمَدِينَةِ وَمَنْ حَوْلَهُم مِّنَ ٱلْأَعْرَابِ أَن يَتَخَلَّفُوا۟ عَن رَّسُولِ ٱللَّهِ وَلَا يَرْغَبُوا۟ بِأَنفُسِهِمْ عَن نَّفْسِهِۦ ۚ ذَٰلِكَ بِأَنَّهُمْ لَا يُصِيبُهُمْ ظَمَأٌۭ وَلَا نَصَبٌۭ وَلَا مَخْمَصَةٌۭ فِى سَبِيلِ ٱللَّهِ وَلَا يَطَـُٔونَ مَوْطِئًۭا يَغِيظُ ٱلْكُفَّارَ وَلَا يَنَالُونَ مِنْ عَدُوٍّۢ نَّيْلًا إِلَّا كُتِبَ لَهُم بِهِۦ عَمَلٌۭ صَٰلِحٌ ۚ إِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
  Unverified discovery rationale: terra: No thirst afflicts the believers and no step angers the enemy إلا كتب لهم به عمل صالح; bodily thirst itself becomes part of an exactly recorded deed, joining thirst with later accounting.
- (9:121) [terra: medium; basis: neighbour+theme] وَلَا يُنفِقُونَ نَفَقَةًۭ صَغِيرَةًۭ وَلَا كَبِيرَةًۭ وَلَا يَقْطَعُونَ وَادِيًا إِلَّا كُتِبَ لَهُمْ لِيَجْزِيَهُمُ ٱللَّهُ أَحْسَنَ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: Neither a small nor large expenditure nor a crossed valley escapes being written for them, extending 9:120's recorded thirst into the exhaustive measure of what each traveler carries forward.
- (11:6) [terra: medium (missing-ayat turn); basis: theme] ۞ وَمَا مِن دَآبَّةٍۢ فِى ٱلْأَرْضِ إِلَّا عَلَى ٱللَّهِ رِزْقُهَا وَيَعْلَمُ مُسْتَقَرَّهَا وَمُسْتَوْدَعَهَا ۚ كُلٌّۭ فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: terra: Every creature's provision is God's charge and He knows مستقرها ومستودعها; provision, a settled place, and complete knowledge meet here as they do in the section's water resting in its pool and the knower of what each receives.
- (12:19) [terra: medium; basis: root+scene] وَجَآءَتْ سَيَّارَةٌۭ فَأَرْسَلُوا۟ وَارِدَهُمْ فَأَدْلَىٰ دَلْوَهُۥ ۖ قَالَ يَٰبُشْرَىٰ هَٰذَا غُلَٰمٌۭ ۚ وَأَسَرُّوهُ بِضَٰعَةًۭ ۚ وَٱللَّهُ عَلِيمٌۢ بِمَا يَعْمَلُونَ
  Unverified discovery rationale: terra: A caravan sends its وارد and he lowers his bucket at the water source; the source section's الورد side of the arrival/departure pair appears here as the practical role of a water-seeker.
- (15:21) [terra: medium; basis: neighbour+theme] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: terra: وما ننزله إلا بقدر معلوم states that every stored provision descends only in a known measure, preparing the water given to drink in 15:22 and clarifying the drink as an allotted share.
- (17:13) [luna: medium; basis: theme] وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا
  Unverified discovery rationale: luna: Each person's deed is fastened to them and a book is brought out on the Day of Resurrection; this makes the section's “everyone returns with what they got” a personal record.
- (17:14) [luna: medium; basis: neighbour+theme] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
  Unverified discovery rationale: luna: “اقْرَأْ كِتَابَكَ” completes 17:13's personal record: the person reads what was brought out, paralleling the section's return to see what one has received.
- (17:17) [terra: medium (missing-ayat turn); basis: root+theme] وَكَمْ أَهْلَكْنَا مِنَ ٱلْقُرُونِ مِنۢ بَعْدِ نُوحٍۢ ۗ وَكَفَىٰ بِرَبِّكَ بِذُنُوبِ عِبَادِهِۦ خَبِيرًۢا بَصِيرًۭا
  Unverified discovery rationale: terra: After destroyed generations are recalled, كفى بربك بذنوب عباده خبيرا بصيرا presents God as fully aware of servants' sins; this applies the source proverb's خبرها vocabulary of complete knowledge to moral accounting.
- (18:49) [luna: medium; basis: theme] وَوُضِعَ ٱلْكِتَٰبُ فَتَرَى ٱلْمُجْرِمِينَ مُشْفِقِينَ مِمَّا فِيهِ وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا ۗ وَلَا يَظْلِمُ رَبُّكَ أَحَدًۭا
  Unverified discovery rationale: luna: The laid-out book omits neither small nor great deeds; this concretely expands the section's claim that the return makes each one's amount visible.
- (20:53) [terra: medium; basis: scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
  Unverified discovery rationale: terra: He sends water from the sky and thereby brings out kinds of plants, establishing the supplied landscape in which the next ayah places livestock.
- (20:54) [terra: medium; basis: neighbour+scene+theme] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
  Unverified discovery rationale: terra: كلوا وارعوا أنعامكم directs people to eat and pasture their cattle from the growth of 20:53, continuing the water-to-herd provision scene.
- (22:46) [terra: medium; basis: root+theme] أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَتَكُونَ لَهُمْ قُلُوبٌۭ يَعْقِلُونَ بِهَآ أَوْ ءَاذَانٌۭ يَسْمَعُونَ بِهَا ۖ فَإِنَّهَا لَا تَعْمَى ٱلْأَبْصَٰرُ وَلَٰكِن تَعْمَى ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ
  Unverified discovery rationale: terra: The ayah specifies قلوب التي في الصدور and says those hearts, rather than eyes, can be blind; it identifies a morally decisive inward content housed in the breasts that 100:10 says will be brought out.
- (25:58) [terra: medium (missing-ayat turn); basis: root+theme] وَتَوَكَّلْ عَلَى ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ وَسَبِّحْ بِحَمْدِهِۦ ۚ وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا
  Unverified discovery rationale: terra: وكفى به بذنوب عباده خبيرا makes God's خبرا specifically knowledge of His servants' sins, connecting the section's experienced-knower expression to the deeds known at return.
- (27:74) [luna: medium; basis: contrast+root+theme] وَإِنَّ رَبَّكَ لَيَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
  Unverified discovery rationale: luna: This says the Lord knows what breasts conceal and declare; it connects the section's chest word and disclosure at return with knowledge that exceeds what people show.
- (28:69) [luna: medium; basis: contrast+root+theme] وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
  Unverified discovery rationale: luna: The verse says God knows what breasts conceal and declare; it gives the section's chest-and-return image a specific hidden-versus-visible boundary.
- (32:27) [terra: medium; basis: scene+theme] أَوَلَمْ يَرَوْا۟ أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ ۖ أَفَلَا يُبْصِرُونَ
  Unverified discovery rationale: terra: Water is driven to barren land to produce crops eaten by their cattle and themselves, linking divinely conducted water with the sustenance of herd and owner.
- (35:14) [terra: medium; basis: root+theme] إِن تَدْعُوهُمْ لَا يَسْمَعُوا۟ دُعَآءَكُمْ وَلَوْ سَمِعُوا۟ مَا ٱسْتَجَابُوا۟ لَكُمْ ۖ وَيَوْمَ ٱلْقِيَٰمَةِ يَكْفُرُونَ بِشِرْكِكُمْ ۚ وَلَا يُنَبِّئُكَ مِثْلُ خَبِيرٍۢ
  Unverified discovery rationale: terra: ولا ينبئك مثل خبير answers false appearances with the report of one fully informed; the source proverb similarly calls the person who has “drunk from many pools” one who has tried affairs حتى خبرها.
- (36:72) [terra: medium; basis: neighbour+scene] وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ
  Unverified discovery rationale: terra: Livestock are subjected so that some are mounts and some are food, identifying the animals that become sources of benefits and drinks in 36:73.
- (38:31) [terra: medium; basis: neighbour+scene] إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ
  Unverified discovery rationale: terra: The fine, swift horses are displayed بالعشي immediately before the declaration of حب الخير, giving 38:32's loved “good” its animal scene and an evening counterpoint to morning herd-work.
- (38:33) [terra: medium; basis: neighbour+scene] رُدُّوهَا عَلَىَّ ۖ فَطَفِقَ مَسْحًۢا بِٱلسُّوقِ وَٱلْأَعْنَاقِ
  Unverified discovery rationale: terra: ردوها علي commands the horses' return after the love-of-good declaration; the returning animals echo the section's herd movement, though no water source is present here.
- (39:21) [terra: medium; basis: scene+theme] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: God sends down water and threads it into ينابيع في الأرض, a nonlexical parallel to water finding and remaining in its earthly place before it sustains life.
- (40:19) [luna: medium; basis: contrast+root+theme] يَعْلَمُ خَآئِنَةَ ٱلْأَعْيُنِ وَمَا تُخْفِى ٱلصُّدُورُ
  Unverified discovery rationale: luna: God knows the stealthiest glance and what breasts conceal; this links the section's chest word to contents that may not be outwardly visible at the return.
- (40:79) [terra: medium; basis: neighbour+scene] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَنْعَٰمَ لِتَرْكَبُوا۟ مِنْهَا وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: terra: God makes الأنعام for riding and eating; it supplies the livestock whose movement and relation to the riders' breasts are completed in 40:80.
- (43:11) [terra: medium; basis: scene+theme] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
  Unverified discovery rationale: terra: Water descends بقدر, revives dead land, and the ayah ends كذلك تخرجون; measured water provision becomes an analogy for the later human emergence that precedes accounting.
- (50:22) [luna: medium; basis: theme] لَّقَدْ كُنتَ فِى غَفْلَةٍۢ مِّنْ هَٰذَا فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ
  Unverified discovery rationale: luna: The cover is removed and sight becomes sharp; this gives the section's return-to-see image a specific scene of disclosure.
- (52:19) [luna: medium (missing-ayat turn); basis: scene+theme] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
  Unverified discovery rationale: luna: The people are told to eat and drink in satisfaction for what they did; this ties drinking to the deeds that the section says people return to see.
- (53:39) [luna: medium (missing-ayat turn); basis: theme] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
  Unverified discovery rationale: luna: A person has only what they strive for; this gives the section's return-with-one's-intake image a specific statement of individual ownership of deeds.
- (53:40) [luna: medium (missing-ayat turn); basis: neighbour+theme] وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ
  Unverified discovery rationale: luna: The person's striving will be seen; this completes 53:39's claim about what belongs to each person with the visibility emphasized in the section.
- (53:41) [luna: medium (missing-ayat turn); basis: neighbour+theme] ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ
  Unverified discovery rationale: luna: The effort is then repaid in full; this completes 53:39-40's movement from individual work to what one receives back.
- (68:17) [luna: medium; basis: contrast+root+scene] إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ
  Unverified discovery rationale: luna: The section names ṣ-b-ḥ and makes morning watering a provision scene; here garden owners plan to harvest “مُصْبِحِينَ” at dawn, but the intended harvest is withheld from others.
- (68:21) [luna: medium (missing-ayat turn); basis: contrast+neighbour+root+scene] فَتَنَادَوْا۟ مُصْبِحِينَ
  Unverified discovery rationale: luna: The owners call one another at daybreak to harvest; this continues 68:17's planned morning task and makes its exclusionary purpose an enacted contrast to the section's water offered to waiting herds.
- (68:22) [luna: medium; basis: contrast+neighbour+root+scene] أَنِ ٱغْدُوا۟ عَلَىٰ حَرْثِكُمْ إِن كُنتُمْ صَٰرِمِينَ
  Unverified discovery rationale: luna: The owners urge one another to go to the harvest at dawn; this continues 68:17's morning work and specifies the action whose exclusionary purpose contrasts with water given to the thirsty.
- (68:23) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene] فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ
  Unverified discovery rationale: luna: They set out whispering to the crop; this continues the dawn departure in 68:22 and shows the secrecy behind the plan to keep others from its yield.
- (68:24) [luna: medium; basis: contrast+neighbour+theme] أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ
  Unverified discovery rationale: luna: They say no poor person should enter the garden; this completes the withholding motive in 68:17 and contrasts with the section's water that relieves need.
- (68:26) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene] فَلَمَّا رَأَوْهَا قَالُوٓا۟ إِنَّا لَضَآلُّونَ
  Unverified discovery rationale: luna: When the owners see the ruined garden, they think they have lost their way; this completes the morning harvest plan in 68:17 with a return that reveals the expected yield is gone.
- (69:18) [luna: medium; basis: theme] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
  Unverified discovery rationale: luna: On that day “لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌ” (nothing hidden from you stays hidden); this sharpens the section's moment when what each one carries becomes clear.
- (75:13) [luna: medium; basis: theme] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
  Unverified discovery rationale: luna: A person is told what they sent ahead and left behind; this is a direct account of what each brings to the return described in the section.
- (75:14) [luna: medium; basis: neighbour+theme] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
  Unverified discovery rationale: luna: The person is a witness against their own soul; this completes 75:13's report of prior acts with the self-recognition that the section's return image suggests.
- (75:15) [luna: medium; basis: neighbour+theme] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
  Unverified discovery rationale: luna: Even if a person offers excuses, the witness in 75:14 remains; this completes the image of an intake that cannot be changed on the way back.
- (75:20) [terra: medium (missing-ayat turn); basis: root+theme] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
  Unverified discovery rationale: terra: بل تحبون العاجلة identifies love's object as the immediate life just before the Hereafter is neglected, a specific counterpart to intense love of worldly الخير before disclosure.
- (76:6) [terra: medium (missing-ayat turn); basis: scene+theme] عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا
  Unverified discovery rationale: terra: A spring يشرب بها عباد الله gives God's servants drink and is made to flow abundantly, a fulfilled water-source scene in which the drink is secure and available.
- (76:21) [terra: medium; basis: scene+theme] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
  Unverified discovery rationale: terra: وسقاهم ربهم شرابا طهورا makes the Lord Himself give a purifying drink at the final destination, a fulfilled counterpart to receiving one's water-share.
- (76:27) [terra: medium (missing-ayat turn); basis: root+theme] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
  Unverified discovery rationale: terra: إن هؤلاء يحبون العاجلة ويذرون وراءهم يوما ثقيلا sets love of the immediate world against leaving a heavy Day behind, clarifying how present appetite obscures the return when one's taking is exposed.
- (77:27) [terra: medium; basis: scene+theme] وَجَعَلْنَا فِيهَا رَوَٰسِىَ شَٰمِخَٰتٍۢ وَأَسْقَيْنَٰكُم مَّآءًۭ فُرَاتًۭا
  Unverified discovery rationale: terra: وأسقيناكم ماء فراتا names sweet water as a direct gift for drinking, a concise Quranic counterpart to the section's water that breaks burning thirst.
- (79:31) [terra: medium; basis: scene+theme] أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا
  Unverified discovery rationale: terra: أخرج منها ماءها ومرعاها places water and pasture together as what God draws from the earth, the two necessities around the section's herd.
- (79:33) [terra: medium; basis: neighbour+scene+theme] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
  Unverified discovery rationale: terra: متاعا لكم ولأنعامكم identifies the water and pasture of 79:31 as provision for people and their livestock.
- (80:25) [terra: medium; basis: scene+theme] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
  Unverified discovery rationale: terra: أنا صببنا الماء صبا begins a close account of poured water becoming food; it supplies the water side of the provision later assigned to livestock.
- (80:32) [terra: medium; basis: neighbour+scene+theme] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
  Unverified discovery rationale: terra: متاعا لكم ولأنعامكم closes the water-grown sequence as provision for people and livestock, connecting the poured water of 80:25 to the herd.
- (81:14) [luna: medium; basis: theme] عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ
  Unverified discovery rationale: luna: “عَلِمَتْ نَفْسٌ مَّا أَحْضَرَتْ” says each soul knows what it brought; it closely matches returning with what one has taken and seeing it.
- (82:3) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene] وَإِذَا ٱلْبِحَارُ فُجِّرَتْ
  Unverified discovery rationale: luna: The seas are burst open; beside 82:5's soul learning what it sent ahead and left behind, this gives the section's settled watering place a specific eschatological reversal.
- (82:4) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ
  Unverified discovery rationale: luna: The graves are scattered immediately before 82:5 says each soul knows what it sent ahead and left behind; this continues the section's link between earth's upheaval and the disclosure of deeds.
- (82:5) [luna: medium; basis: theme] عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ
  Unverified discovery rationale: luna: Each soul learns what it sent ahead and left behind; this makes the section's return with one's intake an explicit reckoning of one's actions.
- (83:28) [terra: medium (missing-ayat turn); basis: scene+theme] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
  Unverified discovery rationale: terra: عينا يشرب بها المقربون is a repeated Quranic formulation of a spring from which the near ones drink, supplying an afterlife counterpart to receiving one's share at water.
- (84:7) [luna: medium; basis: theme] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ
  Unverified discovery rationale: luna: One person receives their book in the right hand; this begins a scene where what one receives determines the return that follows.
- (84:8) [luna: medium; basis: neighbour+theme] فَسَوْفَ يُحَاسَبُ حِسَابًۭا يَسِيرًۭا
  Unverified discovery rationale: luna: The easy account completes 84:7's received book; it links what a person carries back to the account made of it.
- (84:9) [luna: medium; basis: neighbour+scene+theme] وَيَنقَلِبُ إِلَىٰٓ أَهْلِهِۦ مَسْرُورًۭا
  Unverified discovery rationale: luna: The person “يَنقَلِبُ إِلَىٰ أَهْلِهِ مَسْرُورًا” (returns to their people happy) after the account; this directly links return with the outcome one brings.
- (84:10) [luna: medium; basis: contrast+neighbour+theme] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
  Unverified discovery rationale: luna: The opposite person receives the book behind their back; it reverses 84:7's favorable receipt and changes the outcome of return.
- (84:11) [luna: medium; basis: contrast+neighbour+theme] فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
  Unverified discovery rationale: luna: This person calls for destruction after receiving the book behind the back in 84:10; it completes the adverse return.
- (84:12) [luna: medium; basis: contrast+neighbour+theme] وَيَصْلَىٰ سَعِيرًا
  Unverified discovery rationale: luna: The person enters the Blaze, completing 84:10-11's opposite outcome to the joyful return in 84:9.
- (86:9) [luna: medium; basis: theme] يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
  Unverified discovery rationale: luna: “يَوْمَ تُبْلَى السَّرَائِرُ” describes hidden things being exposed; this parallels the section's movement from what is held inside to what is disclosed at return.

## weak (2)

- (18:68) [terra: weak; basis: root+theme] وَكَيْفَ تَصْبِرُ عَلَىٰ مَا لَمْ تُحِطْ بِهِۦ خُبْرًۭا
  Unverified discovery rationale: terra: The source proverb uses خبرها for the understanding gained by trying many watering places; ما لم تحط به خبرا names the knowledge Moses lacks. This is a specific experiential-knowledge link, though the ayah itself has no watering scene.
- (102:8) [luna: weak (missing-ayat turn); basis: theme] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ
  Unverified discovery rationale: luna: The link is indirect: this asks people about the delights they enjoyed, while the section treats drinking as something received before the return and accounting; the verse makes enjoyment itself answerable.

## contrast (42)

- (7:50) [luna: contrast; terra: contrast; basis: contrast+scene+theme] وَنَادَىٰٓ أَصْحَٰبُ ٱلنَّارِ أَصْحَٰبَ ٱلْجَنَّةِ أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ ۚ قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The people of the Fire beg for water, but it is forbidden to them; this reverses water that breaks thirst and satisfies the herd. | terra: The people of Fire beg for water, but the people of the Garden answer that God has forbidden it to the disbelievers; access to the watering gift is finally denied.
- (11:44) [terra: contrast (missing-ayat turn); basis: contrast+scene] وَقِيلَ يَٰٓأَرْضُ ٱبْلَعِى مَآءَكِ وَيَٰسَمَآءُ أَقْلِعِى وَغِيضَ ٱلْمَآءُ وَقُضِىَ ٱلْأَمْرُ وَٱسْتَوَتْ عَلَى ٱلْجُودِىِّ ۖ وَقِيلَ بُعْدًۭا لِّلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: terra: The earth swallows its water, the sky withholds, and the water subsides; this is a concrete reversal of accessible water remaining settled in its pool.
- (11:81) [luna: contrast; terra: contrast (missing-ayat turn); basis: contrast+root+scene] قَالُوا۟ يَٰلُوطُ إِنَّا رُسُلُ رَبِّكَ لَن يَصِلُوٓا۟ إِلَيْكَ ۖ فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ وَلَا يَلْتَفِتْ مِنكُمْ أَحَدٌ إِلَّا ٱمْرَأَتَكَ ۖ إِنَّهُۥ مُصِيبُهَا مَآ أَصَابَهُمْ ۚ إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍۢ
  Unverified discovery rationale: luna: Lot is told that the appointed time is morning; this places a destructive deadline at dawn, against the section's ordinary morning task. | terra: إن موعدهم الصبح makes morning the appointed time of a people's destruction, a specific reversal of the quiet morning watering task heard beside the raid in 100:3.
- (11:98) [terra: contrast; basis: contrast+root+scene] يَقْدُمُ قَوْمَهُۥ يَوْمَ ٱلْقِيَٰمَةِ فَأَوْرَدَهُمُ ٱلنَّارَ ۖ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ
  Unverified discovery rationale: terra: Pharaoh leads his people فأوردهم النار and it is بئس الورد المورود: the source section's dictionary form الورد, a watering place, is transformed into a herd-like arrival at Fire.
- (14:16) [luna: contrast; terra: contrast; basis: contrast+scene] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
  Unverified discovery rationale: luna: The one ahead of him is Hell and he is given water of pus; the section's restorative drink is inverted into an offered drink that harms. | terra: The rebel is given ماء صديد to drink, replacing the section's settled, thirst-breaking water with a corrupt drink.
- (14:17) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
  Unverified discovery rationale: luna: He gulps the pus-water but can scarcely swallow and death approaches without release; this completes 14:16's opposite of thirst being relieved. | terra: يتجرعه ولا يكاد يسيغه portrays repeated sipping that can scarcely be swallowed, the direct reverse of camels drinking through to satiation.
- (15:66) [luna: contrast; terra: contrast (missing-ayat turn); basis: contrast+root+scene] وَقَضَيْنَآ إِلَيْهِ ذَٰلِكَ ٱلْأَمْرَ أَنَّ دَابِرَ هَٰٓؤُلَآءِ مَقْطُوعٌۭ مُّصْبِحِينَ
  Unverified discovery rationale: luna: Lot's people are cut off by morning; this repeats dawn as the time of destruction, reversing the section's water-giving morning. | terra: The decree that the people's last remnant will be cut off مصبحين again turns morning into the completion of destruction rather than the beginning of a life-sustaining herd routine.
- (15:83) [luna: contrast; basis: contrast+root] فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ
  Unverified discovery rationale: luna: A cry seizes the people in the morning; this is another specific destructive ṣ-b-ḥ scene against the section's quiet watering.
- (16:66) [terra: contrast; basis: contrast+scene+theme] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ
  Unverified discovery rationale: terra: From inside livestock comes pure milk سائغا للشاربين; the animal being watered becomes the provider of drink, while hidden bodily contents are brought forth as something wholesome.
- (18:29) [luna: contrast; terra: contrast; basis: contrast+scene] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
  Unverified discovery rationale: luna: Those who call for help are given water like molten metal that burns faces; it is explicitly “بِئْسَ الشَّرَابُ”, the opposite of the section's drink that quenches. | terra: They seek water and are given ماء كالمهل that burns faces; بئس الشراب marks a drink whose effect is the opposite of breaking thirst.
- (18:41) [luna: contrast; terra: contrast; basis: contrast+scene] أَوْ يُصْبِحَ مَآؤُهَا غَوْرًۭا فَلَن تَسْتَطِيعَ لَهُۥ طَلَبًۭا
  Unverified discovery rationale: luna: The garden's water may sink beyond reach; this reverses the section's pool settled in place and available for the herd to drink. | terra: أو يصبح ماؤها غورا فلن تستطيع له طلبا imagines water sunk beyond recovery, reversing the accessible still pool at which the herd can drink.
- (19:71) [terra: contrast; basis: contrast+root] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
  Unverified discovery rationale: terra: واردها applies the arrival-root heard in the section's الورد to everyone's coming to Hell; the link is lexical but pointedly reverses arrival at a life-giving water source.
- (19:86) [terra: contrast; basis: contrast+root+scene] وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا
  Unverified discovery rationale: terra: ونسوق المجرمين إلى جهنم وردا drives the criminals like a thirsty drove toward Hell, reversing the herd's hoped-for arrival at thirst-quenching water.
- (20:119) [terra: contrast; basis: contrast+theme] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
  Unverified discovery rationale: terra: ولا تظمأ فيها promises that Adam will not thirst in the Garden, the fulfilled boundary beyond the section's cycle of thirst, drinking, and departure.
- (21:98) [terra: contrast (missing-ayat turn); basis: contrast+root+scene] إِنَّكُمْ وَمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ حَصَبُ جَهَنَّمَ أَنتُمْ لَهَا وَٰرِدُونَ
  Unverified discovery rationale: terra: أنتم لها واردون applies the water-arrival root developed through the source's الورد to the idolaters' arrival at Hell, reversing approach to a watering place into approach to fire.
- (21:99) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+root] لَوْ كَانَ هَٰٓؤُلَآءِ ءَالِهَةًۭ مَّا وَرَدُوهَا ۖ وَكُلٌّۭ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: terra: ما وردوها argues that true gods would not arrive at Hell; its own contribution is to make the ورود of 21:98 a test exposing the false objects of worship.
- (22:19) [luna: contrast; basis: contrast+scene] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
  Unverified discovery rationale: luna: Boiling water is poured over the heads of the opposing parties; this makes water a punishment rather than the section's relief.
- (22:20) [luna: contrast; basis: contrast+neighbour+scene] يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ
  Unverified discovery rationale: luna: That hot water melts what is in their bellies; it completes 22:19's punitive pouring and reverses the drink that satisfies thirst.
- (22:45) [luna: contrast; basis: contrast+scene] فَكَأَيِّن مِّن قَرْيَةٍ أَهْلَكْنَٰهَا وَهِىَ ظَالِمَةٌۭ فَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا وَبِئْرٍۢ مُّعَطَّلَةٍۢ وَقَصْرٍۢ مَّشِيدٍ
  Unverified discovery rationale: luna: Among ruined towns is “بِئْرٍ مُّعَطَّلَةٍ” (an abandoned well); it gives the section's visited watering place a concrete opposite, a source no longer serving people.
- (23:21) [terra: contrast; basis: contrast+scene+theme] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهَا وَلَكُمْ فِيهَا مَنَٰفِعُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: terra: نسقيكم مما في بطونها likewise gives people drink from what is inside livestock, reversing the direction of watering and joining drink with disclosed interior contents.
- (25:53) [luna: contrast; basis: contrast+scene] ۞ وَهُوَ ٱلَّذِى مَرَجَ ٱلْبَحْرَيْنِ هَٰذَا عَذْبٌۭ فُرَاتٌۭ وَهَٰذَا مِلْحٌ أُجَاجٌۭ وَجَعَلَ بَيْنَهُمَا بَرْزَخًۭا وَحِجْرًۭا مَّحْجُورًۭا
  Unverified discovery rationale: luna: The verse sets sweet, drinkable water against salty, bitter water; it gives a boundary between the section's thirst-quenching pool and water that does not answer thirst.
- (35:12) [luna: contrast; basis: contrast+scene] وَمَا يَسْتَوِى ٱلْبَحْرَانِ هَٰذَا عَذْبٌۭ فُرَاتٌۭ سَآئِغٌۭ شَرَابُهُۥ وَهَٰذَا مِلْحٌ أُجَاجٌۭ ۖ وَمِن كُلٍّۢ تَأْكُلُونَ لَحْمًۭا طَرِيًّۭا وَتَسْتَخْرِجُونَ حِلْيَةًۭ تَلْبَسُونَهَا ۖ وَتَرَى ٱلْفُلْكَ فِيهِ مَوَاخِرَ لِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: luna: This distinguishes fresh, pleasant water “سَائِغٌ شَرَابُهُ” from salt, bitter water; it marks which water can serve the section's drinking and quenching scene.
- (36:73) [terra: contrast; basis: contrast+neighbour+scene+theme] وَلَهُمْ فِيهَا مَنَٰفِعُ وَمَشَارِبُ ۖ أَفَلَا يَشْكُرُونَ
  Unverified discovery rationale: terra: Livestock provide منافع ومشارب to people; the herd that drinks in the section here becomes the source of drinks, and أفلا يشكرون turns that reversal into a question of gratitude.
- (37:67) [luna: contrast; terra: contrast; basis: contrast+scene] ثُمَّ إِنَّ لَهُمْ عَلَيْهَا لَشَوْبًۭا مِّنْ حَمِيمٍۢ
  Unverified discovery rationale: luna: After their food, the people of Hell have a mixture of boiling water; it reverses the section's fresh drinking at the watering place. | terra: A mixture من حميم follows their food, giving the drinkers a scalding share in place of the section's satisfying water.
- (37:68) [terra: contrast; basis: contrast+neighbour+scene] ثُمَّ إِنَّ مَرْجِعَهُمْ لَإِلَى ٱلْجَحِيمِ
  Unverified discovery rationale: terra: ثم إن مرجعهم لإلى الجحيم makes a return follow the scalding drink of 37:67; it darkly mirrors leaving a watering place with what has been consumed.
- (37:177) [luna: contrast; terra: contrast; basis: contrast+root+scene] فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ
  Unverified discovery rationale: luna: When punishment reaches the warned in their courtyard, it is a “سَاءَ صَبَاحُ” (terrible morning); the ṣ-b-ḥ morning of attack reverses the section's quiet morning watering. | terra: When punishment descends into their courtyard, فساء صباح المنذرين, morning becomes an invasion scene rather than the calm watering routine the prose hears beside 100:3.
- (40:72) [luna: contrast; basis: contrast+scene] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
  Unverified discovery rationale: luna: The condemned are dragged through boiling water and then burned; it is a direct reversal of water as bodily relief.
- (44:48) [luna: contrast; basis: contrast+scene] ثُمَّ صُبُّوا۟ فَوْقَ رَأْسِهِۦ مِنْ عَذَابِ ٱلْحَمِيمِ
  Unverified discovery rationale: luna: The verse orders boiling water to be poured over the head; it turns water from drink into torment.
- (47:15) [terra: contrast; basis: contrast+scene+theme] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
  Unverified discovery rationale: terra: The ayah opposes rivers of water غير آسن to boiling water that tears the drinkers' bowels, setting lasting, wholesome drink against a drink that destroys rather than quenches.
- (54:38) [luna: contrast; terra: contrast; basis: contrast+root+scene] وَلَقَدْ صَبَّحَهُم بُكْرَةً عَذَابٌۭ مُّسْتَقِرٌّۭ
  Unverified discovery rationale: luna: A settled punishment comes upon them early in the morning; it reverses the morning provision scene named by the section. | terra: عذاب مستقر seizes them بكرة: a morning marked by settled punishment stands against the quiet morning task and settled water developed in the section.
- (56:52) [luna: contrast; basis: contrast+scene] لَءَاكِلُونَ مِن شَجَرٍۢ مِّن زَقُّومٍۢ
  Unverified discovery rationale: luna: The condemned eat from Zaqqum before the following drink; this identifies the source of the sequence that culminates in the thirsty-camel comparison of 56:55.
- (56:53) [luna: contrast; basis: contrast+neighbour+scene] فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
  Unverified discovery rationale: luna: They fill their bellies from that tree before drinking; it completes 56:52's context for the later thirst-like drinking.
- (56:54) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] فَشَٰرِبُونَ عَلَيْهِ مِنَ ٱلْحَمِيمِ
  Unverified discovery rationale: luna: They drink boiling water after the tree; this prepares the explicit contrast in 56:55 with camels that remain thirsty. | terra: فشاربون عليه من الحميم identifies the liquid consumed before 56:55's camel simile, replacing thirst-breaking water with boiling water.
- (56:55) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ
  Unverified discovery rationale: luna: “شُرْبَ الْهِيمِ” compares their drinking to thirsty camels; unlike the section's camels drinking until satisfaction begins, this drink does not quench. | terra: فشاربون شرب الهيم compares the condemned drinkers to desperately thirsty camels; their repeated drinking reverses the section's camels reaching satisfaction.
- (56:56) [luna: contrast; basis: contrast+neighbour+theme] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
  Unverified discovery rationale: luna: The passage calls this their welcome on the Day of Judgment; it completes 56:52-55 by naming the thirsty-camel drink as an afterlife outcome.
- (67:30) [luna: contrast; terra: contrast; basis: contrast+scene+theme] قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ
  Unverified discovery rationale: luna: If the community's water sinks, who can bring flowing water? This challenges the section's settled source and its relief of thirst. | terra: If water sinks away, who can bring ماء معين? The question exposes the contingency of the section's stable, thirst-quenching water source.
- (68:27) [luna: contrast (missing-ayat turn); basis: contrast+neighbour+scene] بَلْ نَحْنُ مَحْرُومُونَ
  Unverified discovery rationale: luna: They realize, “rather, we are deprived”; this is the garden owners' explicit opposite to the section's herd returning with what it drank.
- (78:24) [luna: contrast; terra: contrast; basis: contrast+scene] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
  Unverified discovery rationale: luna: They taste neither coolness nor drink; it states the deprivation opposite to the section's water that breaks thirst. | terra: لا يذوقون فيها بردا ولا شرابا removes both coolness and drink, a direct denial of the relief promised by satiating water.
- (78:25) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] إِلَّا حَمِيمًۭا وَغَسَّاقًۭا
  Unverified discovery rationale: luna: The only drink is boiling water and pus; it completes 78:24's deprivation with a harmful substitute. | terra: إلا حميما وغساقا supplies the dreadful exception to 78:24: what looks like access to drink becomes scalding and foul rather than quenching.
- (88:5) [luna: contrast; terra: contrast; basis: contrast+scene] تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
  Unverified discovery rationale: luna: The faces are made to drink from a boiling spring; this reverses the cool, settled source in the section. | terra: تسقى من عين آنية gives the condemned drink from a boiling spring, reversing both the watering act and the refreshing pool in the section.
- (88:6) [luna: contrast; basis: contrast+neighbour+scene] لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
  Unverified discovery rationale: luna: They have no food but thorn; this continues the deprivation surrounding the boiling spring of 88:5.
- (88:7) [luna: contrast; basis: contrast+neighbour+theme] لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
  Unverified discovery rationale: luna: The thorn neither nourishes nor relieves hunger; it completes 88:6's failed provision and contrasts with the section's water that actually satisfies need.

## neighbours: within two ayat of a passage the section cites (2)

- (28:21) [next to 28:23] فَخَرَجَ مِنْهَا خَآئِفًۭا يَتَرَقَّبُ ۖ قَالَ رَبِّ نَجِّنِى مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (28:22) [next to 28:23] وَلَمَّا تَوَجَّهَ تِلْقَآءَ مَدْيَنَ قَالَ عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 100, "section": 8, "run_tag": "sol-session-20261005", "source_sha256": "3a6b25a830b4ea96189b0c2300605ec958f572fbc92f8603f0e4cbbc0271856b", "list_sha256": "f28e0aa70ea794fe740953def0bfff45cb30951d7eeed1eaa0e4e9dc48b293af", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec8/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 13, "unique_additions": 13, "repeated_proposals": [], "turn1_sha256": "986cf2df1071e5c56a39b7ec3943d3a415660b55769448cf8a11cc7282f872b7", "followup_sha256": "5779214aeb30b1217f94a49c576a5cce4b1eeef5aabf0fc14373fca400e317b0", "proposal_file": "followup.tsv", "proposal_sha256": "5779214aeb30b1217f94a49c576a5cce4b1eeef5aabf0fc14373fca400e317b0", "list_sha256": "74bda92778131cdea263dc2412bfb14740a1de12632a34ce50075c17b6a0db89", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec8/luna/list.tsv", "rows": 105, "schema_errors": [], "duplicates": {}, "arabic_findings": [], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec8/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 18, "unique_additions": 18, "repeated_proposals": [], "turn1_sha256": "f7b026c83602677431af9e5207ca3f5c14fdf2b61e717c0934024dae4e010997", "followup_sha256": "3a5de6242a347a0e06ff4da9a286feea350b55d79408a3111e362c0b61a81f14", "proposal_file": "followup.tsv", "proposal_sha256": "3a5de6242a347a0e06ff4da9a286feea350b55d79408a3111e362c0b61a81f14", "list_sha256": "14aa9033c0707540a7df1eb5a6daa809d9d4b70dcd192594baafabd0585e601e", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec8/terra/list.tsv", "rows": 98, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 1, "ref": "28:23", "arabic": "ص د ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 2, "ref": "28:24", "arabic": "الخير", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 3, "ref": "99:6", "arabic": "ص د ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 12, "ref": "23:18", "arabic": "نَقْع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 16, "ref": "15:22", "arabic": "وأسقيناكموه", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 21, "ref": "89:20", "arabic": "شديد", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 21, "ref": "89:20", "arabic": "الخير", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 21, "ref": "89:20", "arabic": "ح ب ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 25, "ref": "67:14", "arabic": "خبرها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 31, "ref": "56:68", "arabic": "أفرأيتم الماء الذي تشربون", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 32, "ref": "40:80", "arabic": "صُدور", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 36, "ref": "19:71", "arabic": "الورد", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 40, "ref": "47:15", "arabic": "غير آسن", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 41, "ref": "20:119", "arabic": "ولا تظمأ فيها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 43, "ref": "67:30", "arabic": "ماء معين", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 46, "ref": "88:5", "arabic": "تسقى من عين آنية", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 47, "ref": "18:29", "arabic": "ماء كالمهل", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 57, "ref": "12:19", "arabic": "وارد", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 57, "ref": "12:19", "arabic": "الورد", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 59, "ref": "43:11", "arabic": "كذلك تخرجون", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 63, "ref": "79:31", "arabic": "أخرج منها ماءها ومرعاها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 67, "ref": "56:69", "arabic": "أأنتم أنزلتموه من المزن أم نحن المنزلون", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 71, "ref": "38:31", "arabic": "حب الخير", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["38:32"], "matching_ref_count": 1}, {"line": 73, "ref": "35:14", "arabic": "حتى خبرها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 76, "ref": "76:21", "arabic": "وسقاهم ربهم شرابا طهورا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 79, "ref": "22:46", "arabic": "قلوب التي في الصدور", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 80, "ref": "18:68", "arabic": "خبرها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 81, "ref": "31:23", "arabic": "ذات الصدور", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 86, "ref": "21:98", "arabic": "الورد", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 87, "ref": "21:99", "arabic": "ورود", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 94, "ref": "75:20", "arabic": "الخير", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 95, "ref": "76:27", "arabic": "إن هؤلاء يحبون العاجلة ويذرون وراءهم يوما ثقيلا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 96, "ref": "17:17", "arabic": "خبرها", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 97, "ref": "25:58", "arabic": "خبرا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

