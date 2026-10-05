Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 14 of 14 ("Buluşmalar"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 14 (prose paragraphs numbered) =====
[¶66] Görüntülerin en sık buluştuğu yer "na'büdü" kelimesidir. Aynı sıfat, "müzellel", hem çiğnenmiş yolu hem de katranlanmış deveyi anlatır. Beşinci ayetin kulu, ayakların düzlediği yolun yüzeyiyle aynı kelimeden konuşur. Altıncı ayet hemen ardından bu yolu ister. Kulluk ile yol arasındaki bağı Kur'an da açıkça kurar: {ar:وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:ve eni'budûnî, hâzâ sırâtun müstakîm, gloss:bana kulluk edin; işte bu dosdoğru yoldur, source:36:61}. Bu cümlede ikinci görüntü ile birinci görüntü tek bir şeyin iki adıdır. Uysallaşmış kul yolun kendisidir, yürünen yol da kulluğun kendisidir.

[¶67] Sürü ile yol, başıboş devede buluşur. Başıboş deve "Rabbi bilinmeyen" ve "mâliki bilinmeyen" deve olarak tanımlanır. Böylece ikinci ve dördüncü ayetlerin sahiplik adları, yedinci ayetin son kelimesinin tanımına girer. "Hâdî" kelimesi hem yolcunun önünden giden kılavuzu hem de sürünün başındaki öncüyü adlandırır. Kur'an bu iki sahneyi tek bir akışta anlatır: Sürünün otlağa gidiş ve dönüşünün güzelliğinden hemen sonra şöyle der: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve alellâhi kasdü's-sebîli ve minhâ câir, gloss:doğru yol Allah'a varır; yollardan bazısı ise yana sapar, source:16:9}. Sürü ile eve götürülen kurbanlık da aynı yerde buluşur. Kurbanlık sürüden ("neam") ayrılır, üzerinde ad söylenir ve Eve ulaştırılır. Kur'an bu sahneyi şu sözle kapatır: {ar:لِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ, tr:li-tükebbirullâhe alâ mâ hedâküm, gloss:sizi yola ilettiği için Allah'ı yüceltesiniz diye, source:22:37}. Burada sürü, ad, uysallaştırma ve hidayet aynı pasajda bir aradadır.

[¶68] Rahim ile tamamlanan nimet "Rab" kelimesinde birleşir. Aynı fiil hem çocuğu büyütmeyi hem de nimeti tamamlamayı anlatır ve her ikisi de "tamamlanma sınırına kadar" yürür. Bu ikisini Kur'an'da bir sarayın içinde, bir tartışmanın ortasında görmek mümkündür. Firavun {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni küçükken aramızda biz büyütmedik mi, source:26:18} diye büyütmeyi bir alacak gibi öne sürer. Musa kendi geçmişinden şöyle söz eder: {ar:قَالَ فَعَلْتُهَآ إِذًۭا وَأَنَا۠ مِنَ ٱلضَّآلِّينَ, tr:kâle fealtühâ izen ve ene mine'd-dâllîn, gloss:dedi ki: onu yaptığımda ben yolunu bilmeyenlerden idim, source:26:20}. Ardından şöyle der: {ar:فَوَهَبَ لِى رَبِّى حُكْمًۭا وَجَعَلَنِى مِنَ ٱلْمُرْسَلِينَ, tr:fe-vehebe lî rabbî hukmen ve cealenî mine'l-mürselîn, gloss:Rabbim bana hikmet verdi ve beni elçilerden kıldı, source:26:21}. Son olarak da başa kakılan nimeti ve köleleştirmeyi tek cümlede adlandırır {source:26:22}. Bu kısa konuşmada büyütme, başa kakılan nimet, zorla köle edinme, "dâllîn" kelimesi ve gerçek Rabbin verdiği şey bir arada bulunur. Böylece beş görüntü birbirinden ayrılarak tek bir sahnede görünür: Sahte büyüten ile gerçek Rab, başa kakılan iyilik ile tamamlanan iyilik, zorla köle edilen halk ile kendi isteğiyle kul olan elçi.

[¶69] Rıza ve gazap ile hesap günü bir sahnede buluşur. "Allah'ın günleri", bazılarına azabın, bazılarına da bağışlamanın indiği günlerdir. Hesap gününün yüzleri bu ikiliği taşır: Biri yumuşamış ("nâime"), öbürü üstüne toz inmiş bir yüzdür. Gazap ile yol da buluşur: {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi gadabî fe-kad hevâ, gloss:kimin üzerine gazabım inerse o düşmüştür, source:20:81}. Bu düşüşün karşısında "sonra yolunu bulan" kişi durur {source:20:82}. Gazaba uğrayan, yolda tökezleyip yere kapanan kişidir. Yolu bulan ise doğrulup dimdik yürüyen kişidir. Bu dimdik yürüyüş, dayanmak ve doğrulmak görüntüsüyle de birleşir: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe men yemşî mükibben alâ vechihî ehdâ em men yemşî seviyyen alâ sırâtın müstakîm, gloss:yüzüstü kapanarak yürüyen mi yolu daha iyi bulur, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}.

[¶70] Hesap günü ile terazi, borç ile gözden kaybolmak tek bir ayette yan yana durur. Borç ayetinde borç, vade, tanığın unutması ("en tadılle") ve "akvem" sıfatı bir aradadır {source:2:282}. Burada unutkanlık bir kaybolma olarak, düzgün yazı da bir dik durma olarak görünür. Terazi ile gök de "kâme mîzânü'n-nehâr" sözünde buluşur. Öğle güneşi tepede dikildiğinde gündüzün terazisi dengeye gelir. Aynı kök hem eğilmeyen teraziye hem de hesap gününde ayağa kalkan insanlara ad verir. Ölçüde hile yapanlar sahnesi bunları bir araya getirir. Eksik tartanlar, insanların âlemlerin Rabbi için ayağa kalkacağı güne bağlanır {source:83:6}.

[¶71] Su ile yol, Musa'nın Medyen yolculuğunda buluşur. Musa önce yolun ortasına iletilmeyi diler {source:28:22}. Sonra kuyuya varır ve başkalarına su verir. Ardından gölgeye çekilip Rabbine muhtaç olduğunu söyler {source:28:24}. Kiriş ("neâme") ve ondan sarkan makara ("kâme") yedinci ve altıncı ayetin kelimelerini kuyunun ağzında birleştirir. Musa'nın sahnesi de aynı kelimeleri bir yolcunun hayatında birleştirir: Yol, su ve gölge. İbrahim'in sözü bu buluşmayı surenin sırasıyla dile getirir. Âlemlerin Rabbini anlatırken önce {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-hüve yehdîn, gloss:beni yaratan, bana yolu gösteren O'dur, source:26:78} der, sonra yedirip içireni anar {source:26:79} ve sonunda din gününde bağışlanmayı umar {source:26:82}. Yaratma, yola iletme, su verme ve din günü, bir insanın ağzında sırayla dizilir.

[¶72] Gök ile yol ve sahiplik de İbrahim'in gece sahnesinde buluşur. Ufuktan yükselen yıldız, ay ve güneş birer "semâve", yani yükselen birer şekildir. İbrahim her birine "bu benim Rabbim" der. Hiçbirinin Rab olmadığını batışlarından anlar ve yola iletilmezse yolunu yitirmiş kavimden olacağını söyler {source:6:77}. Ad ve damga görüntüsü bu sahneye bir ayrım ekler: Yükselen her şey bir işarettir, fakat işaret, işaret ettiği şeyin kendisi değildir. Güneşe tapanlar bu ayrımı kaçırır ve yoldan alıkonur {source:27:24}.

[¶73] Bütün bu buluşmalar surenin hareketini taşır. Sure tanıtan bir adla, yani yükseltilmiş bir işaretle başlar. İkinci ve üçüncü ayetler, rahimde biçimlendiren, büyüten, bulutla bitkiyi besleyen ve nimeti tamamlayan Rabbi anar. Hamd, iyiliğin adı geçmeden önce cevap olarak söylenir. Dördüncü ayet, bir hükümdarın elinde toplanan mülkü ve bir günü, yani borcun kapandığı, terazinin eğilmediği ve insanların ayağa kalktığı günü getirir. Beşinci ayette konuşan değişir. Sahip olunan, sahibine doğrudan seslenir. Kendi isteğiyle boyun eğer, ama bineği yorulmuş bir yolcu olduğu için yardım ister. Altıncı ayette bu yolcu, önden giden bir kılavuzla ve iki yanından tutularak, başkalarının düzlediği yolda yürümeyi ve sürünün öncüsünün ardından gitmeyi diler. Yolun bir kuyusu ve bir varış evi vardır. Yedinci ayet bu yolu bir topluluğa bağlar. Yolu yitirmenin iki yüzünü de gösterir: Birinde gazap iner ve yüz kızarır, öbüründe hayvan sahibinden kopar ve izi kaybolur. Böylece sure, işaretinden tanınan sahipten başlayıp, sahibini tanımayan başıboş devede biter. Arada istenen tek şey, yolun sonundaki eve götürülmektir.

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

===== passages from the discovery list (340) =====
## strong (245)

- (2:21) [terra: strong (missing-ayat turn); basis: speaker+theme] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: terra: People are commanded to worship their Rabb, who created them and those before them. It grounds worship in the Creator-nurturer rather than in an unknown master.
- (2:22) [luna: strong; terra: strong (missing-ayat turn); basis: scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The section’s recap names the Lord who feeds clouds and plants; this ayah pairs the sky as canopy with rain sent down and fruits brought forth as provision. | terra: The same Rabb makes earth a resting place, sky a canopy, and rain a source of fruit provision. Ground, water, plant, and dependence form one worship scene.
- (2:38) [terra: strong (missing-ayat turn); basis: speaker+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: terra: When guidance comes, those who follow it have no fear and do not grieve. It makes following the given road the opposite of exposed strayness.
- (2:45) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+speaker+theme] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
  Unverified discovery rationale: luna: The section’s weary servant asks his Lord for help; this ayah commands people to seek help (اسْتَعِينُوا) through patience and prayer, a direct use of the same help-root as the section’s “nastaʿīn.” | terra: “Seek help through patience and prayer” is hard except for the humble. It supplies a Qur’anic form for the section’s worshipper who asks the owner for help.
- (2:71) [luna: strong; terra: contrast; basis: contrast+root+scene] قَالَ إِنَّهُۥ يَقُولُ إِنَّهَا بَقَرَةٌۭ لَّا ذَلُولٌۭ تُثِيرُ ٱلْأَرْضَ وَلَا تَسْقِى ٱلْحَرْثَ مُسَلَّمَةٌۭ لَّا شِيَةَ فِيهَا ۚ قَالُوا۟ ٱلْـَٰٔنَ جِئْتَ بِٱلْحَقِّ ۚ فَذَبَحُوهَا وَمَا كَادُوا۟ يَفْعَلُونَ
  Unverified discovery rationale: luna: The section’s dictionary form “muzallal” (مذلل) is a tamed camel; this cow is specifically said not to plow earth or water a field, a boundary case for an animal’s being made useful or subdued. | terra: The cow is described as not ذَلُولٌ, not broken to plough earth or water crops. This negative boundary sharpens the section’s “müzellel” animal/path sense and its link to earth and water.
- (2:125) [luna: medium; terra: strong; basis: scene+theme] وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا وَٱتَّخِذُوا۟ مِن مَّقَامِ إِبْرَٰهِۦمَ مُصَلًّۭى ۖ وَعَهِدْنَآ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ أَن طَهِّرَا بَيْتِىَ لِلطَّآئِفِينَ وَٱلْعَٰكِفِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ
  Unverified discovery rationale: luna: The section’s road has an arrival House; this ayah identifies the House as a place of return and safety and commands Abraham and Ishmael to purify it for worshippers. | terra: The House is made a place of return and safety, with Abraham’s standing-place made a prayer place. It realizes the section’s return-home and upright-worship imagery.
- (2:138) [terra: strong; basis: scene+speaker+theme] صِبْغَةَ ٱللَّهِ ۖ وَمَنْ أَحْسَنُ مِنَ ٱللَّهِ صِبْغَةًۭ ۖ وَنَحْنُ لَهُۥ عَٰبِدُونَ
  Unverified discovery rationale: terra: “God’s dye/mark” (صِبْغَةَ ٱللَّهِ) is followed by “we are worshippers of Him.” It gives the section’s brand image a mark that identifies voluntary worship rather than an idol.
- (2:150) [terra: strong; basis: theme] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: God’s direction of faces is “so that I may complete My favor upon you and so that you may be guided.” Completion and way-finding are explicitly paired.
- (2:153) [terra: strong; basis: speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ إِنَّ ٱللَّهَ مَعَ ٱلصَّٰبِرِينَ
  Unverified discovery rationale: terra: Believers are told to seek help through patience and prayer, with God with the patient. It turns the requested aid of 1:5 into a sustained way of walking.
- (2:164) [luna: strong; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: This ayah gathers heaven and earth, winds, clouds, and rain that revives the earth into signs, closely matching the section’s linked cloud-and-growth image.
- (2:185) [terra: strong; basis: speaker+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: terra: Completing the counted days is followed by magnifying God for having guided you. It echoes the section’s 22:37 meeting of completion, praise, and guidance.
- (2:196) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: root+scene+theme] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: luna: The section’s herd is separated for sacrifice and brought to its destination; this ayah says the offering must reach its place (مَحِلَّهُ), within the completion of pilgrimage for God. | terra: Completing pilgrimage includes an available sacrifice, and the offering must reach its place before a head is shaved. It joins completion, animal, and destination at the House.
- (2:233) [luna: medium; terra: strong; basis: scene+theme] ۞ وَٱلْوَٰلِدَٰتُ يُرْضِعْنَ أَوْلَٰدَهُنَّ حَوْلَيْنِ كَامِلَيْنِ ۖ لِمَنْ أَرَادَ أَن يُتِمَّ ٱلرَّضَاعَةَ ۚ وَعَلَى ٱلْمَوْلُودِ لَهُۥ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِٱلْمَعْرُوفِ ۚ لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا ۚ لَا تُضَآرَّ وَٰلِدَةٌۢ بِوَلَدِهَا وَلَا مَوْلُودٌۭ لَّهُۥ بِوَلَدِهِۦ ۚ وَعَلَى ٱلْوَارِثِ مِثْلُ ذَٰلِكَ ۗ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍۢ مِّنْهُمَا وَتَشَاوُرٍۢ فَلَا جُنَاحَ عَلَيْهِمَا ۗ وَإِنْ أَرَدتُّمْ أَن تَسْتَرْضِعُوٓا۟ أَوْلَٰدَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّآ ءَاتَيْتُم بِٱلْمَعْرُوفِ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: luna: This ayah names nursing a child for two full years and the parents’ duty to provide, a specific continuation of the section’s child-rearing image. | terra: Mothers nurse for two complete years “for whoever wishes to complete nursing.” The verse supplies the section’s precise boundary at which nurture reaches completion.
- (2:258) [luna: strong; terra: strong; basis: contrast+scene+speaker+theme] أَلَمْ تَرَ إِلَى ٱلَّذِى حَآجَّ إِبْرَٰهِۦمَ فِى رَبِّهِۦٓ أَنْ ءَاتَىٰهُ ٱللَّهُ ٱلْمُلْكَ إِذْ قَالَ إِبْرَٰهِۦمُ رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ قَالَ أَنَا۠ أُحْىِۦ وَأُمِيتُ ۖ قَالَ إِبْرَٰهِۦمُ فَإِنَّ ٱللَّهَ يَأْتِى بِٱلشَّمْسِ مِنَ ٱلْمَشْرِقِ فَأْتِ بِهَا مِنَ ٱلْمَغْرِبِ فَبُهِتَ ٱلَّذِى كَفَرَ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
