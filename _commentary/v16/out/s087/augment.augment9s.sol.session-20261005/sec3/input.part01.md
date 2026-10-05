Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 3 of 18 ("Sürü ve otlak: sahip, öncü, çoban"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 3 (prose paragraphs numbered) =====
[¶14] Birinci ayetle dördüncü ayet arasında üç kelime sırayla gelir: Rab, "yol gösterdi" ve otlak. Arapçada bu üç kelime bir sürü sahnesi kurar. Rab sahiptir, yönetendir, düzeltendir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuhû, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}, {ar:رببت القوم: سستهم, tr:rabebtu'l-kavme sustuhum, gloss:topluluğu yönettim, source:"ر ب ب,B001"}, {ar:ويكون الرب: المصلح, tr:ve yekûnu'r-rabbu el-muslih, gloss:rab düzeltici anlamına da gelir, source:"ر ب ب,B001"}. Develerin bağlı kaldığı yer {ar:مرب الإبل حيث لزمته, tr:merabbu'l-ibil haysu lezimethu, gloss:develerin ayrılmadığı yer, source:"ر ب ب,B007"} diye anılır. Yaban sığırı sürüsü de bu köktendir: {ar:الربرب: القطيع من بقر الوحش, tr:er-rabrab el-katîu min bakari'l-vahş, gloss:rabrab yaban sığırı sürüsüdür, source:"ر ب ب,B014"}. Üçüncü ayetin هدى fiilinin ailesinde sürünün önündekiler bulunur: {ar:هوادي الوحش متقدماتها الهادية لغيرها, tr:hevâdi'l-vahşi mutekaddimâtuhe'l-hâdiyetu li-ğayrihâ, gloss:yaban hayvanlarının hevâdîsi ötekilere yol gösteren öndekileridir, source:"ه د ي,B003"}. Dördüncü ayetin otlağının ailesinde çoban vardır: {ar:الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته, tr:er-râî yer'a'l-mâşiye ey yehûtuhâ ve yahfazuhâ ve'l-vâlî yer'â raiyyetehû, gloss:çoban hayvanları kuşatıp korur; yönetici de halkını böyle gözetir, source:"ر ع ي,B002"}. Aynı ailede uzağa bakan bir gözetleme de vardır: {ar:راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها, tr:râaytu'l-emra nazartu ilâme yasîr raaytu'n-nucûme rakabtuhâ, gloss:işin nereye varacağına baktım; yıldızları gözledim, source:"ر ع ي,B003"}. Obanın çevresinde otlayan iş develeri de bu köktendir: {ar:الإبل التي ترعى حوالي القوم وديارهم, tr:el-ibilu'lletî ter'â havâleyi'l-kavmi ve diyârihim, gloss:topluluğun ve yurtlarının çevresinde otlayan develer, source:"ر ع ي,B007"}.

[¶15] Sahnede sahip, önde giden hayvanlar ve korunan bir otlak vardır. Düz bir okuma, ilk dört ayette yalnızca birbirinin ardına dizilmiş eylemler görür. Bu sahne ise o eylemleri tek bir işin parçaları olarak gösterir: sahip olan, sürüyü otlağa götüren ve otlağı yetiştirendir. Sonra beşinci ayet otlağı döküntüye çevirir. Çobanın kelimesinin ailesindeki "işin nereye varacağına bakmak" anlamı burada işe yarar. Otlağı çıkaran, onun neye dönüşeceğini de gören konumdadır. On beşinci ayetteki رَبِّهِۦ ise kişinin bu sahibi kendi Rabbi olarak anmasıdır.

[¶16] Musa'nın Firavun'a cevabında bu sahne açıkça kurulur. Bitkiler çıkarıldıktan sonra {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ, tr:kulû ver'av en'âmekum inne fî ẕâlike le-âyâtin li-uli'n-nuhâ, gloss:yiyin ve hayvanlarınızı otlatın; bunda akıl sahipleri için işaretler vardır, source:20:54} denir. Otlak kelimesi bir başka yerde de dağların yerleştirilişi yanında geçer ve bunların hepsi {ar:مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:sizin ve hayvanlarınız için bir geçimlik, source:79:33} diye bağlanır. Aynı kapanış, Allah'ın insana yemeğine bakmasını söylediği yerde de gelir. Orada meyvenin yanında hayvan otu da sayılır: {ar:وَفَٰكِهَةًۭ وَأَبًّۭا, tr:ve fâkiheten ve ebbâ, gloss:meyve ve hayvan otu, source:80:31}. "Geçimlik" diye çevrilen متاع, bir süre yararlanılan şeydir. Kelime otlağın kendisinden on altıncı ayetteki dünya hayatına giden yolu sezdirir.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (250) =====
## strong (107)

- (3:14) [terra: strong; basis: scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: terra: Livestock and cultivated land appear among the adorned desires called the مَتَاع of worldly life, directly carrying pasture’s temporary use into the nearer life.
- (4:77) [terra: strong; basis: theme] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
  Unverified discovery rationale: terra: “The enjoyment of the world is little, and the Hereafter is better” closely restates the section’s semantic path from temporary مَتَاع to the preference challenged in surah 87.
- (6:97) [luna: strong; terra: strong; basis: root+scene+theme] وَهُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلنُّجُومَ لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
  Unverified discovery rationale: luna: God makes the stars signs by which people find their way through land and sea darkness; like the section’s herd leaders, they guide travelers along a route. | terra: God makes the stars means by which people are guided through land and sea, bringing the section’s star-watching sense of رعي into contact with guidance.
- (6:102) [terra: strong (missing-ayat turn); basis: root+theme] ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ خَٰلِقُ كُلِّ شَىْءٍۢ فَٱعْبُدُوهُ ۚ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ وَكِيلٌۭ
  Unverified discovery rationale: terra: “Your Lord” is the creator of everything and guardian over everything, an explicit union of ownership, production, and protective oversight.
- (6:141) [terra: strong; basis: scene+theme] ۞ وَهُوَ ٱلَّذِىٓ أَنشَأَ جَنَّٰتٍۢ مَّعْرُوشَٰتٍۢ وَغَيْرَ مَعْرُوشَٰتٍۢ وَٱلنَّخْلَ وَٱلزَّرْعَ مُخْتَلِفًا أُكُلُهُۥ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُتَشَٰبِهًۭا وَغَيْرَ مُتَشَٰبِهٍۢ ۚ كُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
  Unverified discovery rationale: terra: God produces varied gardens, palms, crops, olives, and pomegranates and regulates their harvest, locating produce and its due under the true cultivator’s command.
- (6:142) [terra: strong; basis: neighbour+scene+theme] وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا ۚ كُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ وَلَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: Livestock provide loads and bedding, and people are told to eat what God has provided; the herd follows the cultivated provision of 6:141.
- (6:164) [terra: strong; basis: root+theme] قُلْ أَغَيْرَ ٱللَّهِ أَبْغِى رَبًّۭا وَهُوَ رَبُّ كُلِّ شَىْءٍۢ ۚ وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
  Unverified discovery rationale: terra: “Shall I seek a lord other than Allah when He is the Lord of everything?” is the Qur’anic counterpart to the section’s dictionary formula “the lord of every thing is its owner.”
- (7:58) [luna: strong (missing-ayat turn); terra: medium; basis: root+scene+theme] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
  Unverified discovery rationale: luna: The good land brings forth its plants by its Lord’s permission, while poor ground yields little; this makes the Lord’s role in a pasture’s growth explicit. | terra: Good land brings vegetation forth by its Lord’s permission while bad land yields only scant growth, joining رب with the differing fate of pasture-ground.
- (7:73) [terra: strong; basis: scene+theme] وَإِلَىٰ ثَمُودَ أَخَاهُمْ صَٰلِحًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: terra: Ṣāliḥ calls the she-camel “Allah’s camel” and commands that she be left to eat in Allah’s earth, joining ownership, protected grazing, and provision.
- (10:24) [luna: strong; terra: strong; basis: contrast+scene+theme] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The crop-filled earth is suddenly made “حَصِيدًا” as though it had not flourished; this gives the section’s green pasture and its later end a sharp harvest-like reversal. | terra: Worldly life is rain-fed vegetation eaten by people and livestock; just when its people think they control it, God makes it a cut-down field, exposing the true Owner and the pasture’s end.
- (11:6) [terra: strong; basis: scene+theme] ۞ وَمَا مِن دَآبَّةٍۢ فِى ٱلْأَرْضِ إِلَّا عَلَى ٱللَّهِ رِزْقُهَا وَيَعْلَمُ مُسْتَقَرَّهَا وَمُسْتَوْدَعَهَا ۚ كُلٌّۭ فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: terra: Every earth-creature’s provision rests with God, who knows its dwelling and repository; this joins feeding, the animal’s abiding-place, and the far-seeing Owner.
- (11:56) [terra: strong; basis: root+scene+theme] إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: terra: Every creature is held by its forelock, while “my Lord is on a straight path”; control of the creature and right direction meet in one declaration of personal Lordship.
- (11:57) [terra: strong; basis: root+theme] فَإِن تَوَلَّوْا۟ فَقَدْ أَبْلَغْتُكُم مَّآ أُرْسِلْتُ بِهِۦٓ إِلَيْكُمْ ۚ وَيَسْتَخْلِفُ رَبِّى قَوْمًا غَيْرَكُمْ وَلَا تَضُرُّونَهُۥ شَيْـًٔا ۚ إِنَّ رَبِّى عَلَىٰ كُلِّ شَىْءٍ حَفِيظٌۭ
  Unverified discovery rationale: terra: “My Lord is guardian over all things” gives the section’s owner the shepherd’s developed function of encompassing and preserving what is under his care.
- (11:64) [terra: strong; basis: scene+theme] وَيَٰقَوْمِ هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابٌۭ قَرِيبٌۭ
  Unverified discovery rationale: terra: The she-camel is again identified as God’s sign and left to graze in God’s earth, while harming her is fenced off by warning.
- (12:43) [luna: strong (missing-ayat turn); basis: scene+theme] وَقَالَ ٱلْمَلِكُ إِنِّىٓ أَرَىٰ سَبْعَ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعَ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ ۖ يَٰٓأَيُّهَا ٱلْمَلَأُ أَفْتُونِى فِى رُءْيَٰىَ إِن كُنتُمْ لِلرُّءْيَا تَعْبُرُونَ
  Unverified discovery rationale: luna: The king dreams of seven fat cows swallowed by seven lean cows alongside green and dry ears of grain; the joined herd and crop image makes abundance’s future consumption visible.
- (12:47) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] قَالَ تَزْرَعُونَ سَبْعَ سِنِينَ دَأَبًۭا فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ
  Unverified discovery rationale: luna: Yusuf advises sowing for seven years and leaving most of the harvest in its ears; the section’s pasture as provision is here managed for a known future. | terra: Joseph orders years of sowing and protected storage, a governor’s far-seeing care of provision before its future scarcity.
- (12:48) [luna: strong (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ سَبْعٌۭ شِدَادٌۭ يَأْكُلْنَ مَا قَدَّمْتُمْ لَهُنَّ إِلَّا قَلِيلًۭا مِّمَّا تُحْصِنُونَ
  Unverified discovery rationale: luna: The seven hard years will consume what was stored, except a little kept back; this makes plant provision’s later fate explicit, as the section’s image does for pasture. | terra: The hard years consume what was stored, showing the ruler-shepherd’s attention to what the productive years will become.
- (12:55) [luna: strong (missing-ayat turn); terra: medium; basis: scene+theme] قَالَ ٱجْعَلْنِى عَلَىٰ خَزَآئِنِ ٱلْأَرْضِ ۖ إِنِّى حَفِيظٌ عَلِيمٌۭ
  Unverified discovery rationale: luna: As Egypt’s ruler, Yusuf asks to oversee the land’s storehouses, calling himself a knowledgeable guardian; this is the section’s caretaker image applied to food reserves and governance. | terra: Joseph asks to be placed over the land’s storehouses because he is a knowing guardian, a close instance of the section’s governor who protects those in his charge.
- (13:17) [terra: strong (missing-ayat turn); basis: contrast+theme] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
  Unverified discovery rationale: terra: Flood-foam and smelting foam vanish while what benefits people remains, a specific reverse-angle on the pasture image’s question of what passes and what abides.
- (15:20) [terra: strong (missing-ayat turn); basis: scene+theme] وَجَعَلْنَا لَكُمْ فِيهَا مَعَٰيِشَ وَمَن لَّسْتُمْ لَهُۥ بِرَٰزِقِينَ
  Unverified discovery rationale: terra: God places livelihoods on earth both for people and for creatures whose provision people do not control, widening the pasture scene beyond the human keeper.
- (15:21) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: terra: The treasuries of all things belong to God, who sends each down only in known measure; provision and its apportionment are one Owner’s work.
- (16:5) [terra: strong; basis: scene+theme] وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: terra: God’s creation of livestock with warmth, benefits, and food identifies the herd and all its uses as the Owner’s provision.
- (16:6) [terra: strong; basis: scene] وَلَكُمْ فِيهَا جَمَالٌ حِينَ تُرِيحُونَ وَحِينَ تَسْرَحُونَ
  Unverified discovery rationale: terra: The beauty of livestock when they are brought home and when they are sent out to pasture gives the daily movement of a tended herd.
- (16:7) [terra: strong (missing-ayat turn); basis: scene+theme] وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ ۚ إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: Livestock carry people’s heavy loads to lands they could not otherwise reach, giving the section’s work animals around a travelling community a concrete Qur’anic scene.
- (16:10) [luna: strong; terra: strong; basis: scene+theme] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
  Unverified discovery rationale: luna: The verse says rainwater yields trees “فِيهِ تُسِيمُونَ,” where livestock graze; it gives the pasture scene the preceding provision of water and growth. | terra: Rain produces the vegetation “in which you pasture” livestock, directly joining the giver of water, the grown pasture, and the herder’s act.
- (16:16) [luna: medium; terra: strong; basis: root+scene+theme] وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ
