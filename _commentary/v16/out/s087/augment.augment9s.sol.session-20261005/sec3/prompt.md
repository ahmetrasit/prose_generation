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
  Unverified discovery rationale: luna: The verse names landmarks and says “وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ”; stars guide people, a specific parallel to the section’s leaders who guide others. | terra: “By the star they are guided” directly meets the section’s secondary act of watching stars with its image of a guide leading others.
- (16:69) [luna: strong (missing-ayat turn); basis: scene+theme] ثُمَّ كُلِى مِن كُلِّ ٱلثَّمَرَٰتِ فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًۭا ۚ يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌۭ مُّخْتَلِفٌ أَلْوَٰنُهُۥ فِيهِ شِفَآءٌۭ لِّلنَّاسِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The bee is told to eat from fruits and follow paths made easy by its Lord, from which honey comes; this directly joins guided animal movement to plant provision.
- (16:80) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] وَٱللَّهُ جَعَلَ لَكُم مِّنۢ بُيُوتِكُمْ سَكَنًۭا وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا تَسْتَخِفُّونَهَا يَوْمَ ظَعْنِكُمْ وَيَوْمَ إِقَامَتِكُمْ ۙ وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا إِلَىٰ حِينٍۢ
  Unverified discovery rationale: luna: The verse describes livestock skins made into tents for travel and rest, and wool, fur, and hair as household goods for a time; it concretizes the section’s grazing-camels-around-a-camp detail. | terra: Homes and portable tents made from livestock skins serve people when they travel and camp, closely matching the section’s work animals around a people and its dwellings.
- (16:96) [luna: contrast (missing-ayat turn); terra: strong; basis: contrast+theme] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: What people have is said to end while what is with Allah remains; this directly echoes the section’s distinction between temporary pasture-like provision and what abides. | terra: “What is with you runs out, and what is with Allah remains” states in abstract form what the pasture-to-debris image makes visible.
- (18:7) [terra: strong (missing-ayat turn); basis: scene+theme] إِنَّا جَعَلْنَا مَا عَلَى ٱلْأَرْضِ زِينَةًۭ لَّهَا لِنَبْلُوَهُمْ أَيُّهُمْ أَحْسَنُ عَمَلًۭا
  Unverified discovery rationale: terra: God makes what is on earth an adornment in order to test human action, placing the flourishing surface under the purpose of its true Owner.
- (18:8) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَإِنَّا لَجَٰعِلُونَ مَا عَلَيْهَا صَعِيدًۭا جُرُزًا
  Unverified discovery rationale: terra: God will turn that adorned surface into barren ground, a direct earth-scale counterpart to pasture becoming refuse.
- (18:32) [luna: strong (missing-ayat turn); basis: scene] ۞ وَٱضْرِبْ لَهُم مَّثَلًۭا رَّجُلَيْنِ جَعَلْنَا لِأَحَدِهِمَا جَنَّتَيْنِ مِنْ أَعْنَٰبٍۢ وَحَفَفْنَٰهُمَا بِنَخْلٍۢ وَجَعَلْنَا بَيْنَهُمَا زَرْعًۭا
  Unverified discovery rationale: luna: The parable begins with an owner given two grape gardens, date palms around them, and crops between; it turns the section’s pasture into a concrete cultivated estate.
- (18:33) [luna: strong (missing-ayat turn); basis: scene+theme] كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا وَلَمْ تَظْلِم مِّنْهُ شَيْـًۭٔا ۚ وَفَجَّرْنَا خِلَٰلَهُمَا نَهَرًۭا
  Unverified discovery rationale: luna: Both gardens yield their produce without loss and a river runs through them; this verse shows the garden’s provision at its height before the owner’s confidence and its destruction.
- (18:35) [luna: contrast (missing-ayat turn); terra: strong; basis: contrast+scene+theme] وَدَخَلَ جَنَّتَهُۥ وَهُوَ ظَالِمٌۭ لِّنَفْسِهِۦ قَالَ مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا
  Unverified discovery rationale: luna: The owner enters his garden convinced it will never perish; this is a specific denial of the section’s pasture-to-debris change. | terra: The garden-holder enters his garden and claims it will never perish, articulating the false owner’s blindness to where cultivated abundance ends.
- (18:39) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+root+scene+theme] وَلَوْلَآ إِذْ دَخَلْتَ جَنَّتَكَ قُلْتَ مَا شَآءَ ٱللَّهُ لَا قُوَّةَ إِلَّا بِٱللَّهِ ۚ إِن تَرَنِ أَنَا۠ أَقَلَّ مِنكَ مَالًۭا وَوَلَدًۭا
  Unverified discovery rationale: luna: The companion says the owner should have acknowledged the garden as what God willed and denied power to himself; this directly assigns the garden’s growth to its true provider. | terra: His companion says entry into the garden should have elicited “What Allah willed; no power except through Allah,” relocating growth and possession with the true Lord.
- (18:40) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+neighbour+scene+theme] فَعَسَىٰ رَبِّىٓ أَن يُؤْتِيَنِ خَيْرًۭا مِّن جَنَّتِكَ وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا
  Unverified discovery rationale: luna: The companion warns that God may give him a better garden and send a calamity on this one until it becomes bare slippery ground; the cited verse makes the pasture’s reversal concrete in a garden. | terra: The companion says “my Lord” may replace the garden and send a calamity that leaves it bare, seeing precisely the outcome the owner refuses to see.
- (18:41) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: neighbour+scene+theme] أَوْ يُصْبِحَ مَآؤُهَا غَوْرًۭا فَلَن تَسْتَطِيعَ لَهُۥ طَلَبًۭا
  Unverified discovery rationale: luna: The companion adds that the garden’s water may sink beyond recovery; this identifies the hidden source of its growth as something its owner cannot secure. | terra: The garden’s water may sink beyond the claimant’s ability to retrieve it, showing that even the hidden source of his cultivated abundance remains outside his control.
- (18:42) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+neighbour+scene+theme] وَأُحِيطَ بِثَمَرِهِۦ فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا وَيَقُولُ يَٰلَيْتَنِى لَمْ أُشْرِكْ بِرَبِّىٓ أَحَدًۭا
  Unverified discovery rationale: luna: The garden’s fruit is destroyed and its trellises collapse while its owner wrings his hands; this is a close counterpart to pasture turning into debris and to temporary worldly provision. | terra: The garden’s fruit is encompassed and its claimant wrings his hands over what he spent, enacting the end hidden inside apparent ownership.
- (18:44) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+root+scene+theme] هُنَالِكَ ٱلْوَلَٰيَةُ لِلَّهِ ٱلْحَقِّ ۚ هُوَ خَيْرٌۭ ثَوَابًۭا وَخَيْرٌ عُقْبًۭا
  Unverified discovery rationale: luna: The passage concludes that true protection belongs to Allah and that He gives the best outcome; this connects the section’s Lord as owner and protector to the ruined garden’s final state. | terra: At the garden’s collapse, true protecting authority belongs to Allah; He is best in reward and outcome, joining ownership, protection, and the end of the affair.
- (18:45) [luna: strong; terra: strong; basis: scene+theme] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
  Unverified discovery rationale: luna: The parable of worldly life says vegetation becomes dry stubble scattered by the wind; it makes the pasture’s change into refuse in 87:5 part of a stated pattern of passing growth. | terra: The worldly-life likeness moves from rain and mingled vegetation to dry fragments scattered by wind, a close expansion of pasture becoming debris.
- (20:18) [luna: strong (missing-ayat turn); terra: strong; basis: scene] قَالَ هِىَ عَصَاىَ أَتَوَكَّؤُا۟ عَلَيْهَا وَأَهُشُّ بِهَا عَلَىٰ غَنَمِى وَلِىَ فِيهَا مَـَٔارِبُ أُخْرَىٰ
  Unverified discovery rationale: luna: Moses says he uses his staff to shake leaves down for his sheep; this is a direct shepherd tending animals with forage. | terra: Moses says he beats down leaves with his staff for his sheep, an explicit first-person glimpse of a shepherd providing forage.
- (20:49) [luna: strong; basis: neighbour+root+speaker] قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ
  Unverified discovery rationale: luna: Pharaoh asks Moses, “فَمَن رَّبُّكُمَا,” setting up the section’s cited answer in 20:50: the question makes “Lord” a claim about who gives form and guidance.
- (20:50) [luna: strong; terra: strong; basis: root+scene+speaker+theme] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
  Unverified discovery rationale: luna: Moses answers Pharaoh’s question about their Lord with “أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ”; this joins the section’s owner and guide into one act of giving each thing its form and directing it. | terra: Moses defines “our Lord” as the one who gives every creature its form and then guides it, joining the section’s owner, fitter, and leader in one sentence.
- (20:53) [luna: strong; terra: strong; basis: neighbour+scene+speaker] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
  Unverified discovery rationale: luna: Moses’ reply says God made the earth a resting place, laid paths through it, sent water, and brought forth varied plants; this is the provision landscape immediately before 20:54’s grazing command. | terra: Within Moses’ answer about the Lord, this ayah makes the earth traversable, sends water down, and brings out diverse plants; it supplies the grown terrain to which 20:54 brings the herd.
- (20:54) [luna: strong; terra: strong; basis: neighbour+root+scene+speaker+theme] [cited in ¶16] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
  Unverified discovery rationale: luna: In Moses’ reply to Pharaoh, “كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ” explicitly joins eating to grazing livestock, as the section’s pasture-and-herd scene does. | terra: “Eat and pasture your livestock” directly stages people, herd, and pasture as the provision of the Lord described in 20:50-53.
- (20:131) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
  Unverified discovery rationale: luna: The “flower of the life of this world” is set against the Lord’s better, enduring provision; this sharpens the section’s link from pasture as matāʿ to the world’s short-lived goods. | terra: The “flower of worldly life” is temporary trial, while “your Lord’s provision is better and more lasting”; plant image, personal Owner, and the lasting comparison converge.
- (21:73) [luna: medium; terra: strong; basis: root+scene+theme] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا وَأَوْحَيْنَآ إِلَيْهِمْ فِعْلَ ٱلْخَيْرَٰتِ وَإِقَامَ ٱلصَّلَوٰةِ وَإِيتَآءَ ٱلزَّكَوٰةِ ۖ وَكَانُوا۟ لَنَا عَٰبِدِينَ
  Unverified discovery rationale: luna: These leaders are made guides by God’s command and directed to good works; the verse transfers the section’s leading-and-guiding relation to human leadership. | terra: God makes leaders who guide by His command, a human counterpart to the section’s leading animals that go ahead and guide the rest.
- (21:78) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] وَدَاوُۥدَ وَسُلَيْمَٰنَ إِذْ يَحْكُمَانِ فِى ٱلْحَرْثِ إِذْ نَفَشَتْ فِيهِ غَنَمُ ٱلْقَوْمِ وَكُنَّا لِحُكْمِهِمْ شَٰهِدِينَ
  Unverified discovery rationale: luna: David and Solomon judge the case of people’s sheep grazing at night in another’s field; this joins herd, pasture, damage, and a ruler’s judgment in one scene. | terra: Sheep graze by night in a cultivated field while David and Solomon judge the damage; the ayah brings livestock, pasture, ownership, and rulers’ care into the same scene.
- (21:79) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] فَفَهَّمْنَٰهَا سُلَيْمَٰنَ ۚ وَكُلًّا ءَاتَيْنَا حُكْمًۭا وَعِلْمًۭا ۚ وَسَخَّرْنَا مَعَ دَاوُۥدَ ٱلْجِبَالَ يُسَبِّحْنَ وَٱلطَّيْرَ ۚ وَكُنَّا فَٰعِلِينَ
  Unverified discovery rationale: luna: This verse says God gave Solomon understanding of the flock-and-field case; its contribution is that the ruler’s judgment is guided, completing 21:78’s pastoral dispute. | terra: God gives Solomon understanding of the grazing dispute while granting both rulers judgment and knowledge, embodying the section’s governor-as-shepherd sense.
- (25:2) [terra: strong (missing-ayat turn); basis: root+theme] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
  Unverified discovery rationale: terra: God creates everything and determines it with exact measure, closely matching the section’s creator-fitter who measures and then guides.
- (25:48) [terra: strong; basis: scene+theme] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
  Unverified discovery rationale: terra: God sends winds and purifying water ahead of the rain that will revive land and water creatures, presenting the pasture’s provision as directed mercy.
- (25:49) [terra: strong; basis: neighbour+scene+theme] لِّنُحْۦِىَ بِهِۦ بَلْدَةًۭ مَّيْتًۭا وَنُسْقِيَهُۥ مِمَّا خَلَقْنَآ أَنْعَٰمًۭا وَأَنَاسِىَّ كَثِيرًۭا
  Unverified discovery rationale: terra: The rain revives dead land and gives drink to livestock and many people, directly naming the herd among the recipients of divine provision.
- (26:78) [terra: strong; basis: root+theme] ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ
  Unverified discovery rationale: terra: Abraham names the one who created him as the one who guides him, binding personal Lordship to the guiding act just as the section does.
- (26:79) [terra: strong; basis: neighbour+theme] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
  Unverified discovery rationale: terra: Abraham immediately names that same Lord as the one who feeds and gives drink, completing the guide-and-provision relation.
- (27:60) [terra: strong (missing-ayat turn); basis: scene+theme] أَمَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ لَكُم مِّنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا بِهِۦ حَدَآئِقَ ذَاتَ بَهْجَةٍۢ مَّا كَانَ لَكُمْ أَن تُنۢبِتُوا۟ شَجَرَهَآ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ بَلْ هُمْ قَوْمٌۭ يَعْدِلُونَ
  Unverified discovery rationale: terra: God sends rain and grows splendid gardens whose trees humans could not grow, sharply distinguishing the user of a field from its true producer.
- (28:23) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene] وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ وَوَجَدَ مِن دُونِهِمُ ٱمْرَأَتَيْنِ تَذُودَانِ ۖ قَالَ مَا خَطْبُكُمَا ۖ قَالَتَا لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌۭ كَبِيرٌۭ
  Unverified discovery rationale: luna: The two women hold back their livestock because the shepherds have not finished watering theirs; this is an explicit flock-and-water scene. | terra: At the well Moses finds shepherds (ٱلرِّعَآءُ) watering while two women restrain their animals, an exact Qur’anic occurrence of the section’s shepherd family.
- (28:24) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+speaker] فَسَقَىٰ لَهُمَا ثُمَّ تَوَلَّىٰٓ إِلَى ٱلظِّلِّ فَقَالَ رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ
  Unverified discovery rationale: luna: Moses waters the women’s livestock and then asks his Lord for good; this shows the section’s protective caretaker role as a concrete act. | terra: Moses waters the women’s animals, supplying the protective pastoral act left unresolved in 28:23.
- (28:60) [luna: contrast; terra: strong; basis: contrast+root+theme] وَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَزِينَتُهَا ۚ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ
  Unverified discovery rationale: luna: This verse likewise calls worldly gifts “مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا” and contrasts them with what is better and enduring with God, clarifying the section’s word matāʿ. | terra: What people receive is the enjoyment and adornment of worldly life, while what is with God is “better and more lasting,” the exact inference the section draws from مَتَاع.
- (28:88) [terra: strong; basis: theme] وَلَا تَدْعُ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ ۘ لَآ إِلَٰهَ إِلَّا هُوَ ۚ كُلُّ شَىْءٍ هَالِكٌ إِلَّا وَجْهَهُۥ ۚ لَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: Everything perishes except God’s face, and judgment belongs to Him; the Owner remains beyond the things He brings forth and ends.
- (29:60) [terra: strong (missing-ayat turn); basis: scene+theme] وَكَأَيِّن مِّن دَآبَّةٍۢ لَّا تَحْمِلُ رِزْقَهَا ٱللَّهُ يَرْزُقُهَا وَإِيَّاكُمْ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
  Unverified discovery rationale: terra: Many creatures cannot carry their own provision; God provides for them and for humans, directly identifying the sustaining Owner behind animal life.
- (32:24) [luna: strong; terra: strong; basis: root+scene+theme] وَجَعَلْنَا مِنْهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا لَمَّا صَبَرُوا۟ ۖ وَكَانُوا۟ بِـَٔايَٰتِنَا يُوقِنُونَ
  Unverified discovery rationale: luna: The verse calls some Israelites “أَئِمَّةً يَهْدُونَ بِأَمْرِنَا,” a human parallel to the section’s dictionary account of herd leaders who guide those behind them. | terra: God appoints leaders who guide by His command, explicitly turning precedence into guidance of a community.
- (32:27) [terra: strong; basis: scene+theme] أَوَلَمْ يَرَوْا۟ أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ ۖ أَفَلَا يُبْصِرُونَ
  Unverified discovery rationale: terra: God drives water to barren land and brings out crops from which livestock and people eat; the whole owner-water-pasture-herd relation appears in one ayah.
- (36:33) [luna: strong (missing-ayat turn); terra: medium (missing-ayat turn); basis: scene+theme] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
  Unverified discovery rationale: luna: The dead earth is revived and produces grain for people to eat; this is another explicit scene of the Creator bringing provision out of the ground. | terra: Dead earth is revived and yields grain from which people eat, presenting the field’s food as God’s sign and work.
- (36:71) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ
  Unverified discovery rationale: luna: God’s livestock are made for people, who become their owners; this directly joins the section’s Rabb-as-owner sense to the herd. | terra: God creates livestock for human beings and says “they are their owners” (مَالِكُونَ), placing derived human herd-ownership inside divine creation.
- (36:72) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ
  Unverified discovery rationale: luna: The livestock are made manageable so people ride some and eat others; this specifies the practical relation between people and the herd created in 36:71. | terra: God subjects the livestock so that some are mounts and some are food, showing who makes the human owner-herd relation possible.
- (36:73) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] وَلَهُمْ فِيهَا مَنَٰفِعُ وَمَشَارِبُ ۖ أَفَلَا يَشْكُرُونَ
  Unverified discovery rationale: luna: The livestock provide further benefits and drink, followed by a call to gratitude; this completes the provision attached to the herd in 36:71–72. | terra: The livestock yield benefits and drinks, and the closing demand for gratitude turns use of the herd toward recognition of its giver.
- (39:21) [luna: strong; terra: strong; basis: scene+theme] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: After rain and varied crops, the growth yellows and becomes “حُطَٰمًا”; this closely parallels the section’s pasture that turns to debris and adds the verse’s lesson for people of understanding. | terra: God sends water, produces varied crops, then they wither, yellow, and become حُطَامًا; the producer encompasses the pasture’s full course and its lesson.
- (39:62) [terra: strong (missing-ayat turn); basis: theme] ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ وَكِيلٌۭ
  Unverified discovery rationale: terra: Allah is creator of everything and guardian over everything, giving the section’s shepherd-like protection its universal ground.
- (40:64) [terra: strong (missing-ayat turn); basis: root+scene+theme] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ قَرَارًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ فَتَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: God makes earth a settled place, shapes people well, and provides good things before being named “Allah, your Lord,” joining fitter, provider, and personal Owner.
- (42:20) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+scene+theme] مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
  Unverified discovery rationale: luna: The verse contrasts the one who seeks the hereafter’s harvest with the one who seeks this world’s harvest; it makes the section’s temporary pasture and lasting hereafter a specific crop analogy. | terra: The seeker of the Hereafter receives increase in its “harvest,” while the seeker of worldly harvest receives only some of it; cultivation itself becomes the choice between passing and lasting yield.
- (42:36) [luna: contrast; terra: strong; basis: contrast+root+theme] فَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
  Unverified discovery rationale: luna: The verse calls what people have “مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا” and says what is with God is better and more lasting, echoing the section’s move from temporary pasture to the lasting hereafter. | terra: Whatever people receive is the enjoyment of worldly life, whereas what is with God is better and more lasting for those who trust their Lord.
- (43:32) [terra: strong (missing-ayat turn); basis: root+theme] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
  Unverified discovery rationale: terra: God distributes livelihoods in worldly life and raises people in rank so that they serve one another; provision and human governing relations remain allocations of “your Lord.”
- (55:26) [terra: strong; basis: theme] كُلُّ مَنْ عَلَيْهَا فَانٍۢ
  Unverified discovery rationale: terra: Everything upon the earth is passing, supplying the universal side of the pasture’s decay.
- (55:27) [terra: strong; basis: neighbour+root+theme] وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
  Unverified discovery rationale: terra: The face of “your Lord” remains, setting the lasting personal Owner against the passing creation of 55:26.
- (56:63) [luna: strong (missing-ayat turn); terra: strong; basis: scene+speaker+theme] أَفَرَءَيْتُم مَّا تَحْرُثُونَ
  Unverified discovery rationale: luna: The verse asks who causes the seed people sow to grow, themselves or God; this directly raises who produces the pasture in the section’s image. | terra: The question “Have you considered what you sow?” makes the human cultivator inspect the act whose true agent is identified in the next ayah.
- (56:64) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] ءَأَنتُمْ تَزْرَعُونَهُۥٓ أَمْ نَحْنُ ٱلزَّٰرِعُونَ
  Unverified discovery rationale: luna: The answer assigns the growing of the crop to God; this makes explicit the provider behind the vegetation, as in the section’s pasture scene. | terra: “Is it you who make it grow, or are We the grower?” states the section’s claim that the apparent pasture-owner is not its ultimate producer.
- (56:65) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+neighbour+scene+theme] لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا فَظَلْتُمْ تَفَكَّهُونَ
  Unverified discovery rationale: luna: God says He could make the crop broken debris; this is a direct parallel to the pasture’s transformation in 87:5. | terra: God could make the crop حُطَامًا, directly pairing divine growth with divine power over its debris-end.
- (56:74) [terra: strong; basis: neighbour+scene+speaker] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
  Unverified discovery rationale: terra: After the crop, water, and fire signs, the command to glorify the name of “your Lord, the Magnificent” returns the produced world to the personally acknowledged Owner.
- (57:20) [luna: strong; terra: strong; basis: scene+theme] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: luna: The verse likens worldly life to vegetation that grows, yellows, then becomes “حُطَٰمًا”; it connects the pasture’s decay to the surah’s contrast between near life and what lasts. | terra: The rain-grown crop that pleases its growers, yellows, and becomes debris is explicitly a likeness for worldly life and its deceptive مَتَاع.
- (68:17) [terra: strong; basis: scene+theme] إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ
  Unverified discovery rationale: terra: The owners of a garden swear to harvest it in the morning, beginning a test of people who mistake control of produce for ultimate ownership.
- (68:19) [terra: strong; basis: neighbour+scene+theme] فَطَافَ عَلَيْهَا طَآئِفٌۭ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ
  Unverified discovery rationale: terra: A visitation from “your Lord” circles the garden while its owners sleep, revealing the higher Owner who already sees the crop’s end.
- (68:20) [terra: strong; basis: neighbour+scene+theme] فَأَصْبَحَتْ كَٱلصَّرِيمِ
  Unverified discovery rationale: terra: The garden becomes like a field already reaped, a sudden produce-to-waste reversal governed by the Lord rather than its claimants.
- (68:28) [terra: strong; basis: neighbour+scene+speaker+theme] قَالَ أَوْسَطُهُمْ أَلَمْ أَقُل لَّكُمْ لَوْلَا تُسَبِّحُونَ
  Unverified discovery rationale: terra: The most balanced owner asks why they did not glorify God, explicitly connecting failed ownership of produce to neglected praise.
- (68:29) [terra: strong; basis: neighbour+root+speaker+theme] قَالُوا۟ سُبْحَٰنَ رَبِّنَآ إِنَّا كُنَّا ظَٰلِمِينَ
  Unverified discovery rationale: terra: The garden owners answer, “Glory be to our Lord,” finally naming the true Owner after their crop has vanished.
- (75:20) [terra: strong (missing-ayat turn); basis: theme] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
  Unverified discovery rationale: terra: People love the immediate life, naming the preference toward nearness that the pasture’s temporary مَتَاع helps expose.
- (75:21) [terra: strong (missing-ayat turn); basis: neighbour+theme] وَتَذَرُونَ ٱلْءَاخِرَةَ
  Unverified discovery rationale: terra: They leave the Hereafter, completing the same near-life versus lasting-life choice stated in surah 87.
- (79:31) [luna: strong; terra: strong; basis: root+scene] أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا
  Unverified discovery rationale: luna: In the passage the section names beside the mountains, “مَرْعَىٰهَا” follows the bringing forth of earth’s water; this directly echoes the section’s source word al-marʿā and pasture as provision. | terra: God brings the earth’s water and its مَرْعَىٰ out of it, an exact occurrence of the section’s pasture family and its producing act.
- (79:32) [luna: medium; terra: strong; basis: neighbour+scene] وَٱلْجِبَالَ أَرْسَىٰهَا
  Unverified discovery rationale: luna: The section notes the mountains beside the pasture: this verse’s contribution is that God fixed the mountains, between 79:31’s water and pasture and 79:33’s provision for people and livestock. | terra: The fixing of the mountains is the adjacent act explicitly joined to pasture in the section; 79:33 gathers both into one provision-scene.
- (79:33) [luna: strong; terra: strong; basis: neighbour+scene+theme] [cited in ¶16] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
  Unverified discovery rationale: luna: The section quotes this verse’s “مَتَٰعًا لَّكُمْ وَلِأَنْعَٰمِكُمْ” after the pasture and mountains, specifying that the pasture belongs to temporary provision for people and livestock. | terra: مَتَاعًا لَّكُمْ وَلِأَنْعَامِكُمْ names the landscape as temporary use for humans and livestock, the precise bridge the section makes from pasture to worldly life.
- (79:38) [luna: contrast; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: luna: “وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا” directly states preference for worldly life, matching 87:16 and its contrast with what is better and enduring. | terra: The person who “preferred the worldly life” repeats surah 87’s decisive verb and object immediately after the pasture-and-provision scene of this same surah.
- (79:39) [luna: contrast; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: The fire is the outcome named after 79:38’s preference for worldly life; it completes that cited verse’s side of the choice. | terra: The Fire is the refuge of the one who preferred worldly life, disclosing the destination hidden behind temporary enjoyment.
- (79:40) [luna: contrast; terra: strong (missing-ayat turn); basis: contrast+neighbour+root+theme] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
  Unverified discovery rationale: luna: This verse turns to the one who fears standing before the Lord and restrains desire; it supplies the opposite disposition to 79:38’s preference for worldly life. | terra: The opposite person fears standing before “his Lord” and restrains desire, recognizing the personal Owner and looking beyond near enjoyment.
- (79:41) [luna: contrast; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: The Garden is the outcome named after 79:40’s restraint; it completes the other side of the choice between near life and what endures. | terra: The Garden becomes that person’s refuge, completing the opposite destination to temporary worldly pasture.
- (80:24) [luna: medium; terra: strong; basis: neighbour+scene+speaker+theme] فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ
  Unverified discovery rationale: luna: The command “فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦ” asks the reader to consider food; 80:31–32 supplies the particular fruit, pasture, and shared provision the section draws out. | terra: The command that the human being look at his food opens the food-and-fodder scene which the section explicitly invokes.
- (80:25) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
  Unverified discovery rationale: luna: The food passage begins with rain poured down; this verse supplies the water source before 80:31 names fruit and pasture together. | terra: The abundant pouring of water is the first producing act in the sequence that ends with fruit, fodder, and provision for livestock.
- (80:26) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا
  Unverified discovery rationale: luna: The same food passage says the earth is split open; this verse gives the ground’s part in producing the provisions later named in 80:31–32. | terra: The splitting of the earth supplies the opened ground from which the listed human food and animal forage emerge.
- (80:27) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] فَأَنۢبَتْنَا فِيهَا حَبًّۭا
  Unverified discovery rationale: luna: The passage first names grain grown from that opened earth; this is a specific food yield preceding its pairing of fruit and pasture. | terra: The bringing forth of grain is one particular product of the single provision-making work that culminates in 80:31-32.
- (80:28) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] وَعِنَبًۭا وَقَضْبًۭا
  Unverified discovery rationale: luna: The next crop named is grapes; this verse specifies the fruit side of the food passage that later pairs fruit with pasture. | terra: Grapes and fresh herbage extend the same produced field whose human and animal beneficiaries are named at the close.
- (80:29) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] وَزَيْتُونًۭا وَنَخْلًۭا
  Unverified discovery rationale: luna: The passage names olives and date palms; these are further specific crops in the food sequence ending with pasture and shared provision. | terra: Olives and date palms are further products within the food scene the section asks the reader to hold beside pasture.
- (80:30) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene] وَحَدَآئِقَ غُلْبًۭا
  Unverified discovery rationale: luna: The passage adds luxuriant gardens before naming fruit and pasture in 80:31; this verse completes the cultivated setting. | terra: Dense gardens complete the cultivated landscape before 80:31 distinguishes fruit and livestock fodder.
- (80:31) [luna: strong; terra: strong; basis: neighbour+root+scene] [cited in ¶16] وَفَٰكِهَةًۭ وَأَبًّۭا
  Unverified discovery rationale: luna: The section’s word al-marʿā meets “وَأَبًّا” here: fruit and animal fodder appear together in the food passage the section invokes. | terra: فَاكِهَةً وَأَبًّا places human fruit beside animal fodder, exactly the paired detail developed in the section.
- (80:32) [luna: strong; terra: strong; basis: neighbour+scene+theme] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
  Unverified discovery rationale: luna: This passage calls the listed fruit and pasture “مَتَٰعًا لَّكُمْ وَلِأَنْعَٰمِكُمْ,” making the field’s yield a provision for people and livestock, as in the section. | terra: مَتَاعًا لَّكُمْ وَلِأَنْعَامِكُمْ repeats the section’s decisive closing: a provision for a time, shared by people and their animals.
- (89:15) [terra: strong (missing-ayat turn); basis: root+theme] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
  Unverified discovery rationale: terra: The human being calls God “my Lord” but misreads expanded provision as personal honor, exposing a false understanding of the Owner’s pasture-gift.
- (89:16) [terra: strong (missing-ayat turn); basis: contrast+root+theme] وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
  Unverified discovery rationale: terra: When provision is measured tightly, the same person says “my Lord has humiliated me”; the ayah separates Lordship from the fluctuating amount of temporary provision.
- (91:13) [terra: strong; basis: scene+theme] فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
  Unverified discovery rationale: terra: God’s messenger protects “Allah’s she-camel” and her allotted drink, marking the animal, its Owner, and its measured provision.
- (106:3) [terra: strong (missing-ayat turn); basis: root+speaker+theme] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
  Unverified discovery rationale: terra: The community is commanded to worship “the Lord of this House,” identifying a particular sustaining authority as its own Lord.
- (106:4) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ
  Unverified discovery rationale: terra: That Lord is the one who feeds against hunger and secures against fear, giving the personal Owner the shepherd’s nourishing and protective functions.

## medium (108)

- (2:104) [terra: medium; basis: root+speaker] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقُولُوا۟ رَٰعِنَا وَقُولُوا۟ ٱنظُرْنَا وَٱسْمَعُوا۟ ۗ وَلِلْكَٰفِرِينَ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: terra: رَاعِنَا uses the section’s رعي family in the interpersonal sense “attend to us”; the command to use انظُرْنَا instead exposes a distinct sense within the shepherd word’s range.
- (2:126) [terra: medium (missing-ayat turn); basis: root+scene+theme] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ ٱجْعَلْ هَٰذَا بَلَدًا ءَامِنًۭا وَٱرْزُقْ أَهْلَهُۥ مِنَ ٱلثَّمَرَٰتِ مَنْ ءَامَنَ مِنْهُم بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ قَالَ وَمَن كَفَرَ فَأُمَتِّعُهُۥ قَلِيلًۭا ثُمَّ أَضْطَرُّهُۥٓ إِلَىٰ عَذَابِ ٱلنَّارِ ۖ وَبِئْسَ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: Abraham asks his Lord to make a settlement secure and provide its people with fruits, giving the owner-ruler the paired tasks of protection and feeding.
- (2:247) [terra: medium (missing-ayat turn); basis: scene+theme] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ٱللَّهَ قَدْ بَعَثَ لَكُمْ طَالُوتَ مَلِكًۭا ۚ قَالُوٓا۟ أَنَّىٰ يَكُونُ لَهُ ٱلْمُلْكُ عَلَيْنَا وَنَحْنُ أَحَقُّ بِٱلْمُلْكِ مِنْهُ وَلَمْ يُؤْتَ سَعَةًۭ مِّنَ ٱلْمَالِ ۚ قَالَ إِنَّ ٱللَّهَ ٱصْطَفَىٰهُ عَلَيْكُمْ وَزَادَهُۥ بَسْطَةًۭ فِى ٱلْعِلْمِ وَٱلْجِسْمِ ۖ وَٱللَّهُ يُؤْتِى مُلْكَهُۥ مَن يَشَآءُ ۚ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
  Unverified discovery rationale: terra: God chooses Saul as king and enlarges him in knowledge and body, making a people’s governing leader an appointment of the higher Owner.
- (3:64) [terra: medium (missing-ayat turn); basis: contrast+root+theme] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ تَعَالَوْا۟ إِلَىٰ كَلِمَةٍۢ سَوَآءٍۭ بَيْنَنَا وَبَيْنَكُمْ أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ وَلَا نُشْرِكَ بِهِۦ شَيْـًۭٔا وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ ۚ فَإِن تَوَلَّوْا۟ فَقُولُوا۟ ٱشْهَدُوا۟ بِأَنَّا مُسْلِمُونَ
  Unverified discovery rationale: terra: The call not to take one another as lords besides God marks the boundary between human authority and the single ultimate Owner.
- (3:137) [terra: medium (missing-ayat turn); basis: speaker+theme] قَدْ خَلَتْ مِن قَبْلِكُمْ سُنَنٌۭ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
  Unverified discovery rationale: terra: People are commanded to travel and look at how deniers ended, a direct Qur’anic formulation of the section’s secondary sense “look where the affair will go.”
- (3:185) [luna: contrast; terra: medium; basis: contrast+theme] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: luna: The verse calls worldly life “مَتَٰعُ ٱلْغُرُورِ” and sets it against full recompense after death, reinforcing the section’s contrast between fleeting provision and the hereafter. | terra: Worldly life is only the enjoyment of delusion, supplying the warning latent in a pasture that flourishes and then becomes refuse.
- (4:58) [terra: medium (missing-ayat turn); basis: theme] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
  Unverified discovery rationale: terra: Trusts must be returned to their owners and rulers must judge justly, joining custodial care with the governor’s responsibility toward those under authority.
- (6:38) [terra: medium (missing-ayat turn); basis: scene+theme] وَمَا مِن دَآبَّةٍۢ فِى ٱلْأَرْضِ وَلَا طَٰٓئِرٍۢ يَطِيرُ بِجَنَاحَيْهِ إِلَّآ أُمَمٌ أَمْثَالُكُم ۚ مَّا فَرَّطْنَا فِى ٱلْكِتَٰبِ مِن شَىْءٍۢ ۚ ثُمَّ إِلَىٰ رَبِّهِمْ يُحْشَرُونَ
  Unverified discovery rationale: terra: Earth-creatures and flying birds are communities like human beings and are ultimately gathered to their Lord; animal collectivity remains within divine oversight and destination.
- (6:99) [terra: medium; basis: scene+theme] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: terra: God sends water and brings forth vegetation, grain, fruit, and gardens, then commands people to look at their fruiting and ripening—the producer and attentive observer of the crop’s course.
- (7:57) [terra: medium (missing-ayat turn); basis: scene+theme] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: terra: God drives rain-bearing winds, revives dead land, and brings forth every fruit, a full production scene under one directing agent.
- (9:31) [terra: medium (missing-ayat turn); basis: contrast+root+theme] ٱتَّخَذُوٓا۟ أَحْبَارَهُمْ وَرُهْبَٰنَهُمْ أَرْبَابًۭا مِّن دُونِ ٱللَّهِ وَٱلْمَسِيحَ ٱبْنَ مَرْيَمَ وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ۚ سُبْحَٰنَهُۥ عَمَّا يُشْرِكُونَ
  Unverified discovery rationale: terra: Taking religious authorities as lords besides God shows how human guidance can be mistaken for ownership that belongs to God.
- (9:38) [luna: contrast; terra: medium; basis: contrast+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ ۚ فَمَا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا قَلِيلٌ
  Unverified discovery rationale: luna: The rebuke “أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ” names the same preference the section states after treating worldly life as temporary provision. | terra: The enjoyment of worldly life is declared little beside the Hereafter, clarifying the temporariness carried by مَتَاع in the pasture passages.
- (10:35) [luna: medium (missing-ayat turn); terra: medium; basis: contrast+root+theme] قُلْ هَلْ مِن شُرَكَآئِكُم مَّن يَهْدِىٓ إِلَى ٱلْحَقِّ ۚ قُلِ ٱللَّهُ يَهْدِى لِلْحَقِّ ۗ أَفَمَن يَهْدِىٓ إِلَى ٱلْحَقِّ أَحَقُّ أَن يُتَّبَعَ أَمَّن لَّا يَهِدِّىٓ إِلَّآ أَن يُهْدَىٰ ۖ فَمَا لَكُمْ كَيْفَ تَحْكُمُونَ
  Unverified discovery rationale: luna: The question is whether one who guides to truth is more worthy to be followed than one who cannot guide unless guided; this makes following a true guide the issue, as in the section’s herd leaders. | terra: The question asks whether the one who guides to truth is more worthy of being followed than one who needs guidance, testing the qualification of any leader at the herd’s front.
- (10:39) [terra: medium (missing-ayat turn); basis: theme] بَلْ كَذَّبُوا۟ بِمَا لَمْ يُحِيطُوا۟ بِعِلْمِهِۦ وَلَمَّا يَأْتِهِمْ تَأْوِيلُهُۥ ۚ كَذَٰلِكَ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ ۖ فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: terra: Deniers reject what they have not yet encompassed and whose fulfillment has not reached them, then the reader is told to look at the wrongdoers’ end; impatience is corrected by outcome-seeing.
- (11:123) [terra: medium; basis: root+theme] وَلِلَّهِ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَإِلَيْهِ يُرْجَعُ ٱلْأَمْرُ كُلُّهُۥ فَٱعْبُدْهُ وَتَوَكَّلْ عَلَيْهِ ۚ وَمَا رَبُّكَ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
  Unverified discovery rationale: terra: The unseen belongs to God, the whole affair returns to Him, and “your Lord” is not unaware, directly supporting the Owner who sees where the matter goes.
- (12:11) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene] قَالُوا۟ يَٰٓأَبَانَا مَا لَكَ لَا تَأْمَ۫نَّا عَلَىٰ يُوسُفَ وَإِنَّا لَهُۥ لَنَٰصِحُونَ
  Unverified discovery rationale: luna: Joseph’s brothers first ask their father to trust them with him; 12:12 turns that request into a promise to guard him during their outing, and the later betrayal exposes the difference between a shepherd’s care and their claim.
- (12:12) [luna: medium (missing-ayat turn); basis: contrast+scene] أَرْسِلْهُ مَعَنَا غَدًۭا يَرْتَعْ وَيَلْعَبْ وَإِنَّا لَهُۥ لَحَٰفِظُونَ
  Unverified discovery rationale: luna: The brothers propose taking Joseph to graze and play, promising to watch over him; this is a concrete pasture-and-guarding scene, though its verb for roaming is not the section’s named r-ʿ-y root.
- (12:17) [luna: medium (missing-ayat turn); basis: contrast+neighbour+scene] قَالُوا۟ يَٰٓأَبَانَآ إِنَّا ذَهَبْنَا نَسْتَبِقُ وَتَرَكْنَا يُوسُفَ عِندَ مَتَٰعِنَا فَأَكَلَهُ ٱلذِّئْبُ ۖ وَمَآ أَنتَ بِمُؤْمِنٍۢ لَّنَا وَلَوْ كُنَّا صَٰدِقِينَ
  Unverified discovery rationale: luna: The brothers later claim a wolf ate Joseph while they were racing; their story names the very lapse of care Jacob feared in 12:13.
- (12:23) [terra: medium; basis: root+theme] وَرَٰوَدَتْهُ ٱلَّتِى هُوَ فِى بَيْتِهَا عَن نَّفْسِهِۦ وَغَلَّقَتِ ٱلْأَبْوَٰبَ وَقَالَتْ هَيْتَ لَكَ ۚ قَالَ مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ ۖ إِنَّهُۥ لَا يُفْلِحُ ٱلظَّٰلِمُونَ
  Unverified discovery rationale: terra: Joseph’s “he is my rabb; he made my lodging good” admits the contextual reading of a human master, preserving the section’s owner/master sense of رَبّ alongside the theological reading.
- (12:39) [terra: medium (missing-ayat turn); basis: contrast+root+theme] يَٰصَىٰحِبَىِ ٱلسِّجْنِ ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
  Unverified discovery rationale: terra: Joseph asks whether scattered lords are better than God, the One, setting competing masters against the undivided Owner.
- (12:41) [luna: medium; basis: root] يَٰصَىٰحِبَىِ ٱلسِّجْنِ أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا ۖ وَأَمَّا ٱلْءَاخَرُ فَيُصْلَبُ فَتَأْكُلُ ٱلطَّيْرُ مِن رَّأْسِهِۦ ۚ قُضِىَ ٱلْأَمْرُ ٱلَّذِى فِيهِ تَسْتَفْتِيَانِ
  Unverified discovery rationale: luna: The section’s dictionary sense of Rabb as owner or master has a human usage here: the cupbearer will return to serve “رَبَّهُۥ,” his master, in Joseph’s interpretation.
- (12:42) [luna: medium; terra: medium; basis: root+theme] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
  Unverified discovery rationale: luna: After the cupbearer’s release, Joseph asks him to mention him to “رَبِّكَ,” the king as his master; this makes the section’s owner-and-governor sense of Rabb concrete in human authority. | terra: Joseph tells the released prisoner to mention him to “your rabb,” where rabb is the royal master; it is a clear non-divine use of the section’s ownership word.
- (12:46) [luna: medium (missing-ayat turn); basis: neighbour+scene+theme] يُوسُفُ أَيُّهَا ٱلصِّدِّيقُ أَفْتِنَا فِى سَبْعِ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعِ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ لَّعَلِّىٓ أَرْجِعُ إِلَى ٱلنَّاسِ لَعَلَّهُمْ يَعْلَمُونَ
  Unverified discovery rationale: luna: Yusuf is asked to interpret the king’s cows and ears and to tell what will follow; this verse frames the animal-and-crop vision as a question about its outcome, which 12:47–49 answers.
- (12:49) [luna: medium (missing-ayat turn); terra: medium; basis: neighbour+scene+theme] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ
  Unverified discovery rationale: luna: After the hard years, Yusuf foretells a year of rain and pressing; this verse completes the cycle of shortage and renewed agricultural provision begun in 12:47. | terra: A later year brings rain and renewed pressing, completing the provision-cycle that Joseph foresaw and administered.
- (12:50) [terra: medium; basis: root+theme] وَقَالَ ٱلْمَلِكُ ٱئْتُونِى بِهِۦ ۖ فَلَمَّا جَآءَهُ ٱلرَّسُولُ قَالَ ٱرْجِعْ إِلَىٰ رَبِّكَ فَسْـَٔلْهُ مَا بَالُ ٱلنِّسْوَةِ ٱلَّٰتِى قَطَّعْنَ أَيْدِيَهُنَّ ۚ إِنَّ رَبِّى بِكَيْدِهِنَّ عَلِيمٌۭ
  Unverified discovery rationale: terra: Joseph tells the messenger to return to “your rabb,” again using rabb for the king and making the master sense concrete.
- (12:64) [terra: medium; basis: theme] قَالَ هَلْ ءَامَنُكُمْ عَلَيْهِ إِلَّا كَمَآ أَمِنتُكُمْ عَلَىٰٓ أَخِيهِ مِن قَبْلُ ۖ فَٱللَّهُ خَيْرٌ حَٰفِظًۭا ۖ وَهُوَ أَرْحَمُ ٱلرَّٰحِمِينَ
  Unverified discovery rationale: terra: Jacob calls Allah the best guardian, directly supporting the protective function that the section hears within Lordship and shepherding.
- (13:4) [terra: medium (missing-ayat turn); basis: scene+theme] وَفِى ٱلْأَرْضِ قِطَعٌۭ مُّتَجَٰوِرَٰتٌۭ وَجَنَّٰتٌۭ مِّنْ أَعْنَٰبٍۢ وَزَرْعٌۭ وَنَخِيلٌۭ صِنْوَانٌۭ وَغَيْرُ صِنْوَانٍۢ يُسْقَىٰ بِمَآءٍۢ وَٰحِدٍۢ وَنُفَضِّلُ بَعْضَهَا عَلَىٰ بَعْضٍۢ فِى ٱلْأُكُلِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: terra: Adjacent fields and gardens receive the same water yet bear differentiated produce, displaying the producer’s ordering within a single pasture-landscape.
- (13:7) [luna: medium (missing-ayat turn); basis: root+theme] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
  Unverified discovery rationale: luna: The verse says every people has a guide; this is a human counterpart to the section’s dictionary description of the animals at the head of a herd guiding those behind.
- (13:26) [luna: contrast; terra: medium; basis: contrast+theme] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ وَفَرِحُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا مَتَٰعٌۭ
  Unverified discovery rationale: luna: Provision is expanded or restricted, but the verse says worldly life is only enjoyment beside the hereafter; this makes the pasture-like provision contingent and brief. | terra: God expands and restricts provision, and worldly life is only a small enjoyment beside the Hereafter; giver, measure, and temporary use are joined.
- (14:37) [terra: medium (missing-ayat turn); basis: root+scene+theme] رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ
  Unverified discovery rationale: terra: Abraham addresses “our Lord” from a barren valley and asks that people be provided with fruits, joining personal Lordship, settlement, and produced provision.
- (15:19) [terra: medium; basis: scene+theme] وَٱلْأَرْضَ مَدَدْنَٰهَا وَأَلْقَيْنَا فِيهَا رَوَٰسِىَ وَأَنۢبَتْنَا فِيهَا مِن كُلِّ شَىْءٍۢ مَّوْزُونٍۢ
  Unverified discovery rationale: terra: God spreads the earth, sets mountains, and grows everything in due balance, pairing terrain with measured vegetation as parts of one ordering work.
- (16:8) [terra: medium (missing-ayat turn); basis: scene+theme] وَٱلْخَيْلَ وَٱلْبِغَالَ وَٱلْحَمِيرَ لِتَرْكَبُوهَا وَزِينَةًۭ ۚ وَيَخْلُقُ مَا لَا تَعْلَمُونَ
  Unverified discovery rationale: terra: Horses, mules, and donkeys are created for riding and adornment, extending the fitted work-animal scene beyond cattle.
- (16:11) [luna: medium; terra: medium; basis: neighbour+scene] يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ وَٱلنَّخِيلَ وَٱلْأَعْنَٰبَ وَمِن كُلِّ ٱلثَّمَرَٰتِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The verse continues 16:10’s rain and grazing scene by naming crops, olives, dates, grapes, and other fruits, then calls them signs for reflection. | terra: Crops, olives, palms, grapes, and every fruit are grown by the rain of 16:10, broadening the vegetation in which the livestock pasture.
- (16:12) [luna: medium; basis: scene+theme] وَسَخَّرَ لَكُمُ ٱلَّيْلَ وَٱلنَّهَارَ وَٱلشَّمْسَ وَٱلْقَمَرَ ۖ وَٱلنُّجُومُ مُسَخَّرَٰتٌۢ بِأَمْرِهِۦٓ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The sun, moon, and stars are “مُسَخَّرَٰتٌۢ بِأَمْرِهِۦ”; this places the stars the section’s dictionary entry says one watches under the governing command of the Lord.
- (16:65) [terra: medium (missing-ayat turn); basis: scene+theme] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
  Unverified discovery rationale: terra: Water from heaven revives dead earth, giving the general life-giving act behind the pasture scene.
- (16:66) [terra: medium (missing-ayat turn); basis: scene+theme] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ
  Unverified discovery rationale: terra: Livestock themselves contain a lesson and provide pure drink, making the herd an internally fitted provision from its creator.
- (16:68) [luna: medium (missing-ayat turn); basis: scene+speaker] وَأَوْحَىٰ رَبُّكَ إِلَى ٱلنَّحْلِ أَنِ ٱتَّخِذِى مِنَ ٱلْجِبَالِ بُيُوتًۭا وَمِنَ ٱلشَّجَرِ وَمِمَّا يَعْرِشُونَ
  Unverified discovery rationale: luna: God inspires the bee to make homes in mountains, trees, and structures; this extends the section’s picture of creatures placed and directed by their Lord.
- (18:34) [luna: medium (missing-ayat turn); basis: scene+theme] وَكَانَ لَهُۥ ثَمَرٌۭ فَقَالَ لِصَٰحِبِهِۦ وَهُوَ يُحَاوِرُهُۥٓ أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا
  Unverified discovery rationale: luna: The garden’s owner boasts of greater wealth and a stronger following; his claim makes human possession of a productive estate part of the section’s owner-and-provision image.
- (18:36) [luna: medium (missing-ayat turn); basis: neighbour+theme] وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّدِدتُّ إِلَىٰ رَبِّى لَأَجِدَنَّ خَيْرًۭا مِّنْهَا مُنقَلَبًۭا
  Unverified discovery rationale: luna: The same owner doubts the Hour and expects an even better return if restored to his Lord; this verse shows how confidence in the garden spills into confidence about the hereafter.
- (18:37) [luna: medium (missing-ayat turn); basis: neighbour+theme] قَالَ لَهُۥ صَاحِبُهُۥ وَهُوَ يُحَاوِرُهُۥٓ أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا
  Unverified discovery rationale: luna: The companion answers that the owner was created from dust and then made a man; this verse supplies the creature’s dependence on the one who gives life, within the garden dispute.
- (18:38) [luna: medium (missing-ayat turn); basis: neighbour+root] لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى وَلَآ أُشْرِكُ بِرَبِّىٓ أَحَدًۭا
  Unverified discovery rationale: luna: The companion names Allah as his Lord while answering the garden owner; this gives the section’s Rabb-as-owner image a contrasting confession of whose garden and life ultimately depend on whom.
- (18:43) [luna: medium (missing-ayat turn); basis: contrast+neighbour] وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا
  Unverified discovery rationale: luna: After the garden is ruined, the owner has no group to help him; this verse completes the failure of the strong company he boasted of in 18:34.
- (18:46) [luna: medium (missing-ayat turn); terra: medium; basis: contrast+theme] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
  Unverified discovery rationale: luna: Immediately after the garden parable, wealth and children are called adornment of worldly life, while enduring good deeds are better with the Lord; this extends the section’s temporary-provision contrast. | terra: Worldly adornments are set against lasting good deeds that are better with “your Lord,” keeping transient possession and enduring value under the personal Owner.
- (19:85) [terra: medium (missing-ayat turn); basis: contrast+scene+theme] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
  Unverified discovery rationale: terra: The God-conscious are gathered to the Most Merciful as an honored delegation, supplying the acknowledged-Lord counterpart to the thirsty driving of criminals in 19:86.
- (19:86) [terra: medium; basis: contrast+scene] وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا
  Unverified discovery rationale: terra: Criminals are driven to Hell thirsty, evoking a herd driven toward water while reversing the expected life-giving destination.
- (20:55) [luna: medium; basis: neighbour+theme] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
  Unverified discovery rationale: luna: After 20:54’s eating and grazing, this verse says humans were created from earth, return to it, and are brought forth again; it carries the same earth scene from temporary provision to return.
- (22:5) [terra: medium (missing-ayat turn); basis: scene+theme] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
  Unverified discovery rationale: terra: Lifeless earth stirs, swells, and grows beautiful kinds after rain; the ayah sets the field’s life-cycle beside the human life-cycle and resurrection.
- (22:36) [terra: medium; basis: scene+theme] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: terra: Sacrificial camels are among God’s signs; people arrange, slaughter, eat, and feed from them, while the animal remains explicitly under divine ordinance.
- (22:41) [terra: medium; basis: theme] ٱلَّذِينَ إِن مَّكَّنَّٰهُمْ فِى ٱلْأَرْضِ أَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ وَأَمَرُوا۟ بِٱلْمَعْرُوفِ وَنَهَوْا۟ عَنِ ٱلْمُنكَرِ ۗ وَلِلَّهِ عَٰقِبَةُ ٱلْأُمُورِ
  Unverified discovery rationale: terra: After describing people entrusted with authority, the ayah closes “to Allah belongs the outcome of affairs,” fitting the governor-shepherd sense and the watcher of where a matter ends.
- (23:8) [luna: medium; terra: medium; basis: root+theme] وَٱلَّذِينَ هُمْ لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ
  Unverified discovery rationale: luna: The section’s dictionary describes a shepherd as guarding and tending; here “لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ” uses the same root for keeping trusts and pledges. | terra: The faithful are رَاعُون over their trusts and covenants, using the pasture-root for guarding what has been placed in one’s care.
- (23:18) [terra: medium; basis: scene+theme] وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَسْكَنَّٰهُ فِى ٱلْأَرْضِ ۖ وَإِنَّا عَلَىٰ ذَهَابٍۭ بِهِۦ لَقَٰدِرُونَ
  Unverified discovery rationale: terra: Water descends in measure and is lodged in the earth, while God can remove it; pasture depends on provision that remains fully under its giver’s control.
- (23:19) [terra: medium; basis: neighbour+scene+theme] فَأَنشَأْنَا لَكُم بِهِۦ جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ لَّكُمْ فِيهَا فَوَٰكِهُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: terra: The measured water produces gardens, abundant fruit, and food, completing the provision-act begun in 23:18.
- (23:21) [luna: medium (missing-ayat turn); terra: medium; basis: scene+theme] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهَا وَلَكُمْ فِيهَا مَنَٰفِعُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: luna: The verse calls livestock a sign and names milk, other benefits, and food; it gives a specific instance of the provision in the section’s herd image. | terra: Livestock contain a lesson, drink, many benefits, and food for people; the herd itself is presented as sustained provision.
- (23:41) [luna: medium; basis: scene] فَأَخَذَتْهُمُ ٱلصَّيْحَةُ بِٱلْحَقِّ فَجَعَلْنَٰهُمْ غُثَآءًۭ ۚ فَبُعْدًۭا لِّلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: The people of Noah are made “غُثَاءً” after punishment; the same debris image that the section assigns to the transformed pasture is applied here to a destroyed people.
- (24:45) [terra: medium (missing-ayat turn); basis: scene+theme] وَٱللَّهُ خَلَقَ كُلَّ دَآبَّةٍۢ مِّن مَّآءٍۢ ۖ فَمِنْهُم مَّن يَمْشِى عَلَىٰ بَطْنِهِۦ وَمِنْهُم مَّن يَمْشِى عَلَىٰ رِجْلَيْنِ وَمِنْهُم مَّن يَمْشِى عَلَىٰٓ أَرْبَعٍۢ ۚ يَخْلُقُ ٱللَّهُ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: God creates every creature from water and gives its differing modes of movement, a broad account of the Owner fitting animal kinds.
- (25:74) [terra: medium; basis: scene+theme] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا هَبْ لَنَا مِنْ أَزْوَٰجِنَا وَذُرِّيَّٰتِنَا قُرَّةَ أَعْيُنٍۢ وَٱجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا
  Unverified discovery rationale: terra: The prayer to be made a leader for the God-conscious treats precedence as a responsibility to guide others, not mere rank.
- (26:155) [terra: medium; basis: scene+theme] قَالَ هَٰذِهِۦ نَاقَةٌۭ لَّهَا شِرْبٌۭ وَلَكُمْ شِرْبُ يَوْمٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: terra: The she-camel has an allotted drink and the people an allotted drink on a known day, a managed boundary around herd-provision.
- (26:156) [terra: medium; basis: contrast+neighbour+scene] وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابُ يَوْمٍ عَظِيمٍۢ
  Unverified discovery rationale: terra: The warning not to harm the camel defines the protective limit that the false human controllers later violate.
- (26:205) [terra: medium; basis: neighbour+theme] أَفَرَءَيْتَ إِن مَّتَّعْنَٰهُمْ سِنِينَ
  Unverified discovery rationale: terra: The question imagines God allowing people enjoyment for years, testing whether duration changes its temporary status.
- (26:207) [terra: medium; basis: neighbour+theme] مَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يُمَتَّعُونَ
  Unverified discovery rationale: terra: When the promised end arrives, their former enjoyment does not avail them, making explicit the endpoint hidden within temporary provision.
- (27:19) [terra: medium (missing-ayat turn); basis: root+scene+theme] فَتَبَسَّمَ ضَاحِكًۭا مِّن قَوْلِهَا وَقَالَ رَبِّ أَوْزِعْنِىٓ أَنْ أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ أَنْعَمْتَ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ وَأَنْ أَعْمَلَ صَٰلِحًۭا تَرْضَىٰهُ وَأَدْخِلْنِى بِرَحْمَتِكَ فِى عِبَادِكَ ٱلصَّٰلِحِينَ
  Unverified discovery rationale: terra: Solomon, ruler over people and creatures, asks “my Lord” to enable gratitude for divine favor, acknowledging an Owner above his own command.
- (27:20) [terra: medium (missing-ayat turn); basis: scene+theme] وَتَفَقَّدَ ٱلطَّيْرَ فَقَالَ مَا لِىَ لَآ أَرَى ٱلْهُدْهُدَ أَمْ كَانَ مِنَ ٱلْغَآئِبِينَ
  Unverified discovery rationale: terra: Solomon inspects the birds and notices the hoopoe’s absence, a ruler’s concrete vigilance over creatures in his charge.
- (28:25) [luna: medium (missing-ayat turn); basis: neighbour+scene] فَجَآءَتْهُ إِحْدَىٰهُمَا تَمْشِى عَلَى ٱسْتِحْيَآءٍۢ قَالَتْ إِنَّ أَبِى يَدْعُوكَ لِيَجْزِيَكَ أَجْرَ مَا سَقَيْتَ لَنَا ۚ فَلَمَّا جَآءَهُۥ وَقَصَّ عَلَيْهِ ٱلْقَصَصَ قَالَ لَا تَخَفْ ۖ نَجَوْتَ مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: The woman tells her father that Moses watered their livestock and brings him to be rewarded; this verse completes the care act in 28:24 with its recognition by the flock’s household.
- (28:26) [luna: medium (missing-ayat turn); basis: scene+theme] قَالَتْ إِحْدَىٰهُمَا يَٰٓأَبَتِ ٱسْتَـْٔجِرْهُ ۖ إِنَّ خَيْرَ مَنِ ٱسْتَـْٔجَرْتَ ٱلْقَوِىُّ ٱلْأَمِينُ
  Unverified discovery rationale: luna: The daughter recommends Moses as strong and trustworthy for hire; this is a specific judgment about fitness to serve and guard a household’s livelihood after he watered their livestock.
- (28:61) [terra: medium; basis: contrast+theme] أَفَمَن وَعَدْنَٰهُ وَعْدًا حَسَنًۭا فَهُوَ لَٰقِيهِ كَمَن مَّتَّعْنَٰهُ مَتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ثُمَّ هُوَ يَوْمَ ٱلْقِيَٰمَةِ مِنَ ٱلْمُحْضَرِينَ
  Unverified discovery rationale: terra: One who receives the good promise is contrasted with one merely given worldly enjoyment and then brought for judgment, distinguishing lasting provision from temporary use.
- (28:77) [luna: medium (missing-ayat turn); basis: contrast+theme] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
  Unverified discovery rationale: luna: The verse directs people to seek the home of the hereafter through what God has given while not forgetting their share of this world; it makes the section’s boundary between temporary provision and lasting reward explicit.
- (30:50) [terra: medium (missing-ayat turn); basis: scene+speaker+theme] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: People are told to look at the effects of God’s mercy in His revival of dead earth, turning observation of the field’s outcome into recognition of its giver.
- (31:10) [terra: medium (missing-ayat turn); basis: scene+theme] خَلَقَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا ۖ وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ
  Unverified discovery rationale: terra: God fixes mountains, disperses creatures, sends rain, and grows noble kinds, gathering terrain, herd-life, and vegetation into one ordering act.
- (31:22) [terra: medium; basis: root+theme] ۞ وَمَن يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ وَهُوَ مُحْسِنٌۭ فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ ۗ وَإِلَى ٱللَّهِ عَٰقِبَةُ ٱلْأُمُورِ
  Unverified discovery rationale: terra: One who submits to God and does good has the firm handhold, and the outcome of affairs is God’s; the personal Lord owns both guidance and destination.
- (31:24) [terra: medium (missing-ayat turn); basis: theme] نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ
  Unverified discovery rationale: terra: God grants brief enjoyment and then drives the recipients toward punishment, making the limit and destination of مَتَاع explicit.
- (34:15) [luna: medium (missing-ayat turn); basis: scene+theme] لَقَدْ كَانَ لِسَبَإٍۢ فِى مَسْكَنِهِمْ ءَايَةٌۭ ۖ جَنَّتَانِ عَن يَمِينٍۢ وَشِمَالٍۢ ۖ كُلُوا۟ مِن رِّزْقِ رَبِّكُمْ وَٱشْكُرُوا۟ لَهُۥ ۚ بَلْدَةٌۭ طَيِّبَةٌۭ وَرَبٌّ غَفُورٌۭ
  Unverified discovery rationale: luna: The people of Saba are told to eat from two gardens and be grateful for their Lord’s provision; this is a concrete cultivated-land version of the section’s pasture as a gift.
- (34:17) [luna: medium (missing-ayat turn); basis: neighbour+scene+theme] ذَٰلِكَ جَزَيْنَٰهُم بِمَا كَفَرُوا۟ ۖ وَهَلْ نُجَٰزِىٓ إِلَّا ٱلْكَفُورَ
  Unverified discovery rationale: luna: This verse identifies their ingratitude as the consequence’s setting; it adds the human response to the lost garden provision described in 34:16.
- (35:9) [terra: medium (missing-ayat turn); basis: scene+theme] وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ
  Unverified discovery rationale: terra: God drives clouds to dead land and revives earth after death, joining direction, provision, and the field’s transformation.
- (36:34) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَجَعَلْنَا فِيهَا جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ وَفَجَّرْنَا فِيهَا مِنَ ٱلْعُيُونِ
  Unverified discovery rationale: luna: The verse continues the revived-earth scene with date palms and grape gardens and flowing springs; it specifies the planted provision around 36:33.
- (36:35) [luna: medium (missing-ayat turn); basis: scene+theme] لِيَأْكُلُوا۟ مِن ثَمَرِهِۦ وَمَا عَمِلَتْهُ أَيْدِيهِمْ ۖ أَفَلَا يَشْكُرُونَ
  Unverified discovery rationale: luna: The verse says people may eat the fruit, which their hands did not make; it specifies dependence on the provider behind the crops in 36:33–34.
- (38:23) [luna: medium; terra: medium; basis: scene] إِنَّ هَٰذَآ أَخِى لَهُۥ تِسْعٌۭ وَتِسْعُونَ نَعْجَةًۭ وَلِىَ نَعْجَةٌۭ وَٰحِدَةٌۭ فَقَالَ أَكْفِلْنِيهَا وَعَزَّنِى فِى ٱلْخِطَابِ
  Unverified discovery rationale: luna: The dispute before David turns on one man’s 99 ewes and another’s single ewe; this gives the section’s herd-and-owner image a concrete case of contested possession. | terra: The claimant describes one ewe beside another man’s ninety-nine ewes, giving a dispute about flock-ownership before a ruler.
- (38:24) [luna: medium; terra: medium; basis: neighbour+scene+theme] قَالَ لَقَدْ ظَلَمَكَ بِسُؤَالِ نَعْجَتِكَ إِلَىٰ نِعَاجِهِۦ ۖ وَإِنَّ كَثِيرًۭا مِّنَ ٱلْخُلَطَآءِ لَيَبْغِى بَعْضُهُمْ عَلَىٰ بَعْضٍ إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَقَلِيلٌۭ مَّا هُمْ ۗ وَظَنَّ دَاوُۥدُ أَنَّمَا فَتَنَّٰهُ فَٱسْتَغْفَرَ رَبَّهُۥ وَخَرَّ رَاكِعًۭا وَأَنَابَ ۩
  Unverified discovery rationale: luna: David judges the ewe dispute from 38:23 as a wrong by the stronger partner; the flock scene thus links authority over a herd to just judgment. | terra: David judges that the many-ewe owner has wronged the one-ewe owner, linking care of a flock’s ownership to the ruler’s just oversight.
- (38:26) [terra: medium; basis: neighbour+theme] يَٰدَاوُۥدُ إِنَّا جَعَلْنَٰكَ خَلِيفَةًۭ فِى ٱلْأَرْضِ فَٱحْكُم بَيْنَ ٱلنَّاسِ بِٱلْحَقِّ وَلَا تَتَّبِعِ ٱلْهَوَىٰ فَيُضِلَّكَ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّ ٱلَّذِينَ يَضِلُّونَ عَن سَبِيلِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۢ بِمَا نَسُوا۟ يَوْمَ ٱلْحِسَابِ
  Unverified discovery rationale: terra: God appoints David a vicegerent and commands him to judge people in truth, making explicit the governing duty implicit in the sheep case.
- (39:71) [terra: medium; basis: contrast+scene] وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا فُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَتْلُونَ عَلَيْكُمْ ءَايَٰتِ رَبِّكُمْ وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ بَلَىٰ وَلَٰكِنْ حَقَّتْ كَلِمَةُ ٱلْعَذَابِ عَلَى ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: Those who disbelieve are driven to Hell in groups, a final herding scene whose destination exposes the cost of refusing guidance.
- (39:73) [terra: medium; basis: contrast+scene+theme] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
  Unverified discovery rationale: terra: Those mindful of their Lord are driven in groups to the Garden, supplying the opposite final destination under acknowledged Lordship.
- (40:39) [luna: contrast; terra: medium; basis: contrast+theme] يَٰقَوْمِ إِنَّمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَا مَتَٰعٌۭ وَإِنَّ ٱلْءَاخِرَةَ هِىَ دَارُ ٱلْقَرَارِ
  Unverified discovery rationale: luna: The believer in Pharaoh’s household calls worldly life “مَتَٰعٌۭ” and the hereafter the lasting abode, a direct parallel to the section’s temporary-benefit reading. | terra: The believer says worldly life is only enjoyment while the Hereafter is the lasting home, an explicit gloss on the section’s movement from مَتَاع to permanence.
- (40:79) [terra: medium; basis: scene+theme] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَنْعَٰمَ لِتَرْكَبُوا۟ مِنْهَا وَمِنْهَا تَأْكُلُونَ
  Unverified discovery rationale: terra: God makes livestock so people may ride some and eat others, another direct statement that the herd and its uses are bestowed.
- (40:80) [terra: medium; basis: neighbour+scene+theme] وَلَكُمْ فِيهَا مَنَٰفِعُ وَلِتَبْلُغُوا۟ عَلَيْهَا حَاجَةًۭ فِى صُدُورِكُمْ وَعَلَيْهَا وَعَلَى ٱلْفُلْكِ تُحْمَلُونَ
  Unverified discovery rationale: terra: Livestock carry further benefits and bear people toward needs in their hearts, extending the Owner’s fitting of animals for human use.
- (41:10) [terra: medium (missing-ayat turn); basis: scene+theme] وَجَعَلَ فِيهَا رَوَٰسِىَ مِن فَوْقِهَا وَبَٰرَكَ فِيهَا وَقَدَّرَ فِيهَآ أَقْوَٰتَهَا فِىٓ أَرْبَعَةِ أَيَّامٍۢ سَوَآءًۭ لِّلسَّآئِلِينَ
  Unverified discovery rationale: terra: God places stabilizing mountains and apportions the earth’s sustenance, bringing fixed terrain and measured provision together.
- (41:39) [terra: medium (missing-ayat turn); basis: scene+theme] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: Humbled earth quivers and grows after rain, and its reviver is identified as the giver of life, making vegetation a sign of the Owner’s larger power.
- (42:11) [terra: medium (missing-ayat turn); basis: scene+theme] فَاطِرُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَمِنَ ٱلْأَنْعَٰمِ أَزْوَٰجًۭا ۖ يَذْرَؤُكُمْ فِيهِ ۚ لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
  Unverified discovery rationale: terra: God makes mates among humans and livestock and multiplies them through those pairs, locating the herd’s increase in divine creation.
- (43:11) [terra: medium (missing-ayat turn); basis: scene+theme] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
  Unverified discovery rationale: terra: God sends water in due measure and revives a dead land, combining measured provision with the produced landscape.
- (43:12) [terra: medium; basis: scene+theme] وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا وَجَعَلَ لَكُم مِّنَ ٱلْفُلْكِ وَٱلْأَنْعَٰمِ مَا تَرْكَبُونَ
  Unverified discovery rationale: terra: God creates pairs and makes ships and livestock for riding, assigning the herd its fitted human use.
- (43:13) [terra: medium; basis: neighbour+root+scene+speaker] لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
  Unverified discovery rationale: terra: Upon mounting, people are told to remember their Lord’s blessing, turning mastery of the animal back into acknowledgment of the true Owner.
- (50:9) [terra: medium; basis: neighbour+scene] وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا فَأَنۢبَتْنَا بِهِۦ جَنَّٰتٍۢ وَحَبَّ ٱلْحَصِيدِ
  Unverified discovery rationale: terra: Blessed water descends and grows gardens and harvested grain, beginning a compact provision sequence.
- (50:10) [terra: medium; basis: neighbour+scene] وَٱلنَّخْلَ بَاسِقَٰتٍۢ لَّهَا طَلْعٌۭ نَّضِيدٌۭ
  Unverified discovery rationale: terra: Tall palms and clustered fruit add the visible produce of the rain-grown landscape.
- (50:11) [terra: medium; basis: neighbour+scene+theme] رِّزْقًۭا لِّلْعِبَادِ ۖ وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ ٱلْخُرُوجُ
  Unverified discovery rationale: terra: The growth is “provision for the servants,” and dead land is revived by it, naming the purpose and giver of the produced field.
- (50:21) [terra: medium (missing-ayat turn); basis: scene+theme] وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ
  Unverified discovery rationale: terra: Every soul arrives with a driver and a witness, making direction and watchfulness accompany the creature all the way to its outcome.
- (54:27) [terra: medium; basis: scene+theme] إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ
  Unverified discovery rationale: terra: The she-camel is sent as a trial under watch, a protected animal whose treatment reveals whether people accept the higher Owner’s command.
- (54:28) [terra: medium; basis: neighbour+scene+theme] وَنَبِّئْهُمْ أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ ۖ كُلُّ شِرْبٍۢ مُّحْتَضَرٌۭ
  Unverified discovery rationale: terra: Water is apportioned between the people and the camel, making animal provision measured and guarded.
- (54:49) [terra: medium (missing-ayat turn); basis: theme] إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ
  Unverified discovery rationale: terra: Everything is created according to measure, supplying the universal formulation behind the measured guidance and provision in the section’s opening sequence.
- (56:66) [luna: medium (missing-ayat turn); basis: neighbour+scene] إِنَّا لَمُغْرَمُونَ
  Unverified discovery rationale: luna: After the crop is ruined, people lament their loss; this gives the consequence of the possible transformation named in 56:65.
- (56:67) [luna: medium (missing-ayat turn); basis: neighbour+scene] بَلْ نَحْنُ مَحْرُومُونَ
  Unverified discovery rationale: luna: The people conclude they are deprived; this completes their response to the lost crop in 56:65–66.
- (59:18) [terra: medium; basis: speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
  Unverified discovery rationale: terra: Each soul is told to look at what it has sent ahead for tomorrow, transferring the section’s “look where the affair will end” from the shepherd’s vigilance to moral foresight.
- (70:32) [luna: medium; terra: medium; basis: root+theme] وَٱلَّذِينَ هُمْ لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ
  Unverified discovery rationale: luna: This repeated description says believers are “لِأَمَٰنَٰتِهِمْ وَعَهْدِهِمْ رَٰعُونَ”; it carries the section’s root from attending a flock to guarding human trusts. | terra: The repeated description of believers as رَاعُون over trusts and covenants confirms the shepherd-family’s ethical sense of protective custody.
- (73:8) [terra: medium; basis: root+speaker+theme] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
  Unverified discovery rationale: terra: “Remember the name of your Lord and devote yourself to Him” closely parallels the section’s person naming this Owner as his own Lord.
- (77:46) [terra: medium (missing-ayat turn); basis: theme] كُلُوا۟ وَتَمَتَّعُوا۟ قَلِيلًا إِنَّكُم مُّجْرِمُونَ
  Unverified discovery rationale: terra: “Eat and enjoy for a little” states the short duration of bodily provision while attaching an approaching moral outcome to it.
- (78:14) [terra: medium; basis: neighbour+scene] وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا
  Unverified discovery rationale: terra: Pouring water descends from rain clouds, initiating the crop-and-garden sequence.
- (78:15) [terra: medium; basis: neighbour+scene+theme] لِّنُخْرِجَ بِهِۦ حَبًّۭا وَنَبَاتًۭا
  Unverified discovery rationale: terra: God brings out grain and plants by that water, stating the productive act at the center of the pasture image.
- (78:16) [terra: medium; basis: neighbour+scene] وَجَنَّٰتٍ أَلْفَافًا
  Unverified discovery rationale: terra: Dense gardens complete the rain-grown scene and echo the gardens adjoining fruit and fodder in 80:30-31.
- (79:30) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ
  Unverified discovery rationale: luna: The earth is spread before 79:31 brings forth its water and pasture; this verse supplies the ground setting for the pasture-and-mountain sequence the section names.
- (88:17) [luna: medium; terra: medium; basis: scene+speaker] أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
  Unverified discovery rationale: luna: The section’s dictionary phrase “مَرَبُّ الإِبِل” names the place camels remain; 88:17 asks people to consider the camel’s creation, making the animal in that entry an object of reflection. | terra: The command to look at how the camel was created brings the work animal itself before the reader as an object fitted by its Maker.
- (96:1) [terra: medium; basis: root+speaker+theme] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
  Unverified discovery rationale: terra: The command to read in the name of “your Lord who created” makes the addressee identify the personal Lord precisely as creator.

## weak (2)

- (74:50) [terra: weak; basis: scene] كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ
  Unverified discovery rationale: terra: The people are likened to startled wild asses; the species differs from the dictionary’s wild-cattle herd, but the ayah still supplies a concrete wild-herd scene.
- (74:51) [terra: weak; basis: contrast+neighbour+scene] فَرَّتْ مِن قَسْوَرَةٍۭ
  Unverified discovery rationale: terra: The wild asses flee from a lion; this may illuminate a herd moving in panic rather than behind a guide, though the ayah does not mention a leader or pasture.

## contrast (28)

- (4:46) [terra: contrast; basis: contrast+root+speaker] مِّنَ ٱلَّذِينَ هَادُوا۟ يُحَرِّفُونَ ٱلْكَلِمَ عَن مَّوَاضِعِهِۦ وَيَقُولُونَ سَمِعْنَا وَعَصَيْنَا وَٱسْمَعْ غَيْرَ مُسْمَعٍۢ وَرَٰعِنَا لَيًّۢا بِأَلْسِنَتِهِمْ وَطَعْنًۭا فِى ٱلدِّينِ ۚ وَلَوْ أَنَّهُمْ قَالُوا۟ سَمِعْنَا وَأَطَعْنَا وَٱسْمَعْ وَٱنظُرْنَا لَكَانَ خَيْرًۭا لَّهُمْ وَأَقْوَمَ وَلَٰكِن لَّعَنَهُمُ ٱللَّهُ بِكُفْرِهِمْ فَلَا يُؤْمِنُونَ إِلَّا قَلِيلًۭا
  Unverified discovery rationale: terra: Hostile speakers twist رَاعِنَا with their tongues; the word-family of attentive care becomes an instrument of insult rather than true regard.
- (6:136) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] وَجَعَلُوا۟ لِلَّهِ مِمَّا ذَرَأَ مِنَ ٱلْحَرْثِ وَٱلْأَنْعَٰمِ نَصِيبًۭا فَقَالُوا۟ هَٰذَا لِلَّهِ بِزَعْمِهِمْ وَهَٰذَا لِشُرَكَآئِنَا ۖ فَمَا كَانَ لِشُرَكَآئِهِمْ فَلَا يَصِلُ إِلَى ٱللَّهِ ۖ وَمَا كَانَ لِلَّهِ فَهُوَ يَصِلُ إِلَىٰ شُرَكَآئِهِمْ ۗ سَآءَ مَا يَحْكُمُونَ
  Unverified discovery rationale: terra: People assign invented shares of crops and livestock to God and their partners, corrupting recognition of the single Owner of both pasture and herd.
- (6:138) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
  Unverified discovery rationale: terra: People falsely declare livestock and crops restricted and impose invented rules over them, acting as owners against the provision-giver’s authority.
- (7:77) [terra: contrast (missing-ayat turn); basis: contrast+scene] فَعَقَرُوا۟ ٱلنَّاقَةَ وَعَتَوْا۟ عَنْ أَمْرِ رَبِّهِمْ وَقَالُوا۟ يَٰصَٰلِحُ ٱئْتِنَا بِمَا تَعِدُنَآ إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ
  Unverified discovery rationale: terra: The people hamstring the she-camel after the command to let her graze, violating the protective boundary around the Owner’s animal.
- (7:179) [terra: contrast; basis: contrast+root+scene] وَلَقَدْ ذَرَأْنَا لِجَهَنَّمَ كَثِيرًۭا مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا وَلَهُمْ ءَاذَانٌۭ لَّا يَسْمَعُونَ بِهَآ ۚ أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْغَٰفِلُونَ
  Unverified discovery rationale: terra: Those who do not use heart, eyes, or ears are like livestock and more astray, marking the boundary between a guided herd and human heedlessness.
- (11:65) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] فَعَقَرُوهَا فَقَالَ تَمَتَّعُوا۟ فِى دَارِكُمْ ثَلَٰثَةَ أَيَّامٍۢ ۖ ذَٰلِكَ وَعْدٌ غَيْرُ مَكْذُوبٍۢ
  Unverified discovery rationale: terra: After the camel is hamstrung, Ṣāliḥ announces only three more days of enjoyment, tying abuse of the protected herd to the measured end of temporary use.
- (11:97) [terra: contrast; basis: contrast+neighbour+root+scene] إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَٱتَّبَعُوٓا۟ أَمْرَ فِرْعَوْنَ ۖ وَمَآ أَمْرُ فِرْعَوْنَ بِرَشِيدٍۢ
  Unverified discovery rationale: terra: Pharaoh’s people follow his command even though his command is not rightly guided, reversing the section’s leader who conducts those behind him well.
- (11:98) [terra: contrast; basis: contrast+neighbour+scene+theme] يَقْدُمُ قَوْمَهُۥ يَوْمَ ٱلْقِيَٰمَةِ فَأَوْرَدَهُمُ ٱلنَّارَ ۖ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ
  Unverified discovery rationale: terra: Pharaoh goes before his people and brings them to the Fire as a watering-place, a precise anti-shepherd scene: a ruler leads his herd to the worst destination.
- (12:13) [luna: contrast (missing-ayat turn); basis: contrast+neighbour+scene] قَالَ إِنِّى لَيَحْزُنُنِىٓ أَن تَذْهَبُوا۟ بِهِۦ وَأَخَافُ أَن يَأْكُلَهُ ٱلذِّئْبُ وَأَنتُمْ عَنْهُ غَٰفِلُونَ
  Unverified discovery rationale: luna: Jacob fears a wolf may eat Joseph while the brothers are heedless; this is his own stated concern about watchful care, answering their promise in 12:12.
- (12:14) [luna: contrast (missing-ayat turn); basis: contrast+neighbour+scene] قَالُوا۟ لَئِنْ أَكَلَهُ ٱلذِّئْبُ وَنَحْنُ عُصْبَةٌ إِنَّآ إِذًۭا لَّخَٰسِرُونَ
  Unverified discovery rationale: luna: The brothers argue that a wolf could not overcome them while they are many; this verse contributes their confident claim of protection, which 12:15 exposes as false.
- (12:15) [luna: contrast (missing-ayat turn); basis: contrast+neighbour+scene] فَلَمَّا ذَهَبُوا۟ بِهِۦ وَأَجْمَعُوٓا۟ أَن يَجْعَلُوهُ فِى غَيَٰبَتِ ٱلْجُبِّ ۚ وَأَوْحَيْنَآ إِلَيْهِ لَتُنَبِّئَنَّهُم بِأَمْرِهِمْ هَٰذَا وَهُمْ لَا يَشْعُرُونَ
  Unverified discovery rationale: luna: After gaining custody of Joseph, the brothers agree to cast him into a well; this is the actual reversal of the guarding they promised in 12:12.
- (14:3) [luna: contrast; basis: contrast+theme] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
  Unverified discovery rationale: luna: The verse explicitly describes people who “يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ,” matching the preference for near life that follows the section’s pasture image.
- (16:107) [luna: contrast; basis: contrast+theme] ذَٰلِكَ بِأَنَّهُمُ ٱسْتَحَبُّوا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَأَنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: This verse says people preferred “ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ,” directly echoing the section’s move from temporary worldly provision to what lasts.
- (25:44) [terra: contrast; basis: contrast+root+scene] أَمْ تَحْسَبُ أَنَّ أَكْثَرَهُمْ يَسْمَعُونَ أَوْ يَعْقِلُونَ ۚ إِنْ هُمْ إِلَّا كَٱلْأَنْعَٰمِ ۖ بَلْ هُمْ أَضَلُّ سَبِيلًا
  Unverified discovery rationale: terra: People who refuse to hear are said to be like livestock, indeed further astray from the way; the herd is present but guidance has failed.
- (26:157) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ
  Unverified discovery rationale: terra: The people hamstring the allotted she-camel and become regretful, overturning the managed water-and-herd relation of 26:155-56.
- (28:41) [luna: contrast; terra: contrast; basis: contrast+root+scene+theme] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَدْعُونَ إِلَى ٱلنَّارِ ۖ وَيَوْمَ ٱلْقِيَٰمَةِ لَا يُنصَرُونَ
  Unverified discovery rationale: luna: Pharaoh’s people are made leaders “يَدْعُونَ إِلَى ٱلنَّارِ”; this reverses the section’s guiding leader, showing that leading those behind can direct them toward ruin. | terra: Leaders call others to the Fire rather than to sustaining pasture, reversing both the guide’s destination and the ruler’s duty of care.
- (29:64) [luna: contrast; basis: contrast+theme] وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ ۚ وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: luna: The verse says this worldly life is only play and amusement while the hereafter is the real life; this makes explicit the boundary implied by pasture that grows and passes.
- (33:67) [terra: contrast; basis: contrast+root+scene] وَقَالُوا۟ رَبَّنَآ إِنَّآ أَطَعْنَا سَادَتَنَا وَكُبَرَآءَنَا فَأَضَلُّونَا ٱلسَّبِيلَا۠
  Unverified discovery rationale: terra: The condemned say they obeyed their chiefs and great ones, who led them astray from the path, exposing leadership that functions as misguidance.
- (34:16) [luna: contrast (missing-ayat turn); basis: contrast+scene] فَأَعْرَضُوا۟ فَأَرْسَلْنَا عَلَيْهِمْ سَيْلَ ٱلْعَرِمِ وَبَدَّلْنَٰهُم بِجَنَّتَيْهِمْ جَنَّتَيْنِ ذَوَاتَىْ أُكُلٍ خَمْطٍۢ وَأَثْلٍۢ وَشَىْءٍۢ مِّن سِدْرٍۢ قَلِيلٍۢ
  Unverified discovery rationale: luna: After they turn away, a flood replaces the two gardens with bitter produce and sparse trees; this is a specific reversal from fruitful land to diminished growth.
- (37:22) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] ۞ ٱحْشُرُوا۟ ٱلَّذِينَ ظَلَمُوا۟ وَأَزْوَٰجَهُمْ وَمَا كَانُوا۟ يَعْبُدُونَ
  Unverified discovery rationale: terra: Wrongdoers and their associated companions are gathered together before being directed onward, a collective mustering that prepares the anti-guidance of 37:23.
- (37:23) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+root+scene] مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ
  Unverified discovery rationale: terra: “Guide them to the path of Hell” deliberately puts guidance language onto the worst destination, an exact reversal of the leader conducting a herd toward sustaining pasture.
- (47:12) [terra: contrast; basis: contrast+scene+theme] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
  Unverified discovery rationale: terra: Disbelievers enjoy themselves and eat as livestock eat, but the Fire is their lodging; temporary pasture-like consumption is severed from right guidance and right destination.
- (54:29) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ
  Unverified discovery rationale: terra: They summon their companion and hamstring the camel, breaking the watched trial and apportioned water arrangement of 54:27-28.
- (56:55) [terra: contrast (missing-ayat turn); basis: contrast+scene] فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ
  Unverified discovery rationale: terra: The condemned drink like desperately thirsty camels, retaining the herd-and-water scene while replacing sustaining provision with torment.
- (57:27) [terra: contrast; basis: contrast+root+theme] ثُمَّ قَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِرُسُلِنَا وَقَفَّيْنَا بِعِيسَى ٱبْنِ مَرْيَمَ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ وَجَعَلْنَا فِى قُلُوبِ ٱلَّذِينَ ٱتَّبَعُوهُ رَأْفَةًۭ وَرَحْمَةًۭ وَرَهْبَانِيَّةً ٱبْتَدَعُوهَا مَا كَتَبْنَٰهَا عَلَيْهِمْ إِلَّا ٱبْتِغَآءَ رِضْوَٰنِ ٱللَّهِ فَمَا رَعَوْهَا حَقَّ رِعَايَتِهَا ۖ فَـَٔاتَيْنَا ٱلَّذِينَ ءَامَنُوا۟ مِنْهُمْ أَجْرَهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
  Unverified discovery rationale: terra: People invent monasticism but do not tend or observe it as it should be tended (فَمَا رَعَوْهَا حَقَّ رِعَايَتِهَا), a moral failure of the same guarding root used for a shepherd’s care.
- (79:37) [luna: contrast; basis: contrast+neighbour] فَأَمَّا مَن طَغَىٰ
  Unverified discovery rationale: luna: This verse identifies the transgressor; its neighbor 79:38 specifies that he preferred worldly life. Together they name the agent and choice behind the same contrast the section states.
- (81:4) [terra: contrast; basis: contrast+scene] وَإِذَا ٱلْعِشَارُ عُطِّلَتْ
  Unverified discovery rationale: terra: At the Hour, prized pregnant she-camels are left untended, a concrete reversal of the protected herd gathered around its people.
- (91:14) [terra: contrast; basis: contrast+neighbour+scene+theme] فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
  Unverified discovery rationale: terra: The people hamstring the protected camel, and their Lord levels them for it; violation of the Owner’s pasture-boundary destroys the would-be human controllers.

## neighbours: within two ayat of a passage the section cites (5)

- (20:52) [next to 20:54] قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى
- (20:56) [next to 20:54] وَلَقَدْ أَرَيْنَٰهُ ءَايَٰتِنَا كُلَّهَا فَكَذَّبَ وَأَبَىٰ
- (79:34) [next to 79:33] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (79:35) [next to 79:33] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (80:33) [next to 80:31] فَإِذَا جَآءَتِ ٱلصَّآخَّةُ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 87, "section": 3, "run_tag": "sol-session-20261005", "source_sha256": "5e9ef0a461cc99bfb9b4c0e1b4609dd85b292c96610df2a0bb8cfe5bd670daa3", "list_sha256": "41a45caf51bfc7a87bcf82b3704a07fc154e48abd7b3c7fdfc3a5cf057956cf3", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec3/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 64, "unique_additions": 64, "repeated_proposals": [], "turn1_sha256": "c0f03b0ba6e5b8931982d3fa370d2e2efee1294a8d0dd29c31992a854e65956d", "followup_sha256": "1e0709e6167fb8a95c95fd0240d9a3478bebd5372c1b0eab1a33808b8f2995d1", "proposal_file": "followup.tsv", "proposal_sha256": "1e0709e6167fb8a95c95fd0240d9a3478bebd5372c1b0eab1a33808b8f2995d1", "list_sha256": "4c42b9bc6b43eb3e01208beed790bd527407397d4c3229a472e96206444d772d", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec3/luna/list.tsv", "rows": 110, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 19, "ref": "88:17", "arabic": "مَرَبُّ الإِبِل", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec3/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 66, "unique_additions": 66, "repeated_proposals": [], "turn1_sha256": "cdaa174e4b668a9333c3d3ce560681b71d00163daa94947ea8f0e358b50bf76c", "followup_sha256": "1b7e905d4e61d473a894967fa7eff9ceeaa0963975e60f6ea26c6972926c699d", "proposal_file": "followup.tsv", "proposal_sha256": "1b7e905d4e61d473a894967fa7eff9ceeaa0963975e60f6ea26c6972926c699d", "list_sha256": "d3ecc97effa614a5860a4764e8e8530ca6b46da56252c479bce2f06a81fbd49a", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec3/terra/list.tsv", "rows": 207, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 4, "ref": "79:31", "arabic": "مَرْعَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 50, "ref": "6:97", "arabic": "رعي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 85, "ref": "2:104", "arabic": "رعي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 88, "ref": "12:23", "arabic": "رَبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 110, "ref": "7:58", "arabic": "رب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 161, "ref": "75:20", "arabic": "مَتَاع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 202, "ref": "31:24", "arabic": "مَتَاع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

