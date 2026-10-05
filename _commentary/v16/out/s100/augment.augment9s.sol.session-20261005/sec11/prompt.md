Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 11 of 11 ("Buluşmalar"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 11 (prose paragraphs numbered) =====
[¶48] İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

[¶49] Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

[¶50] Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

[¶51] Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

[¶52] Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

[¶53] Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

[¶54] Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

[¶55] Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

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

===== passages from the discovery list (313) =====
## strong (199)

- (2:143) [luna: medium (missing-ayat turn); terra: strong; basis: root+speaker+theme] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: luna: The section’s verse 5 uses waṣaṭna for entering the middle of a gathering and verse 7 speaks of a witness; this verse calls the community ummatan wasaṭan, a just community made witnesses over people, joining those roots in a different “middle” sense. | terra: أُمَّةً وَسَطًا is made so that it may be شُهَدَاءَ عَلَى النَّاسِ; “middle” and “witnesses” meet within one ayah as they do across the section's crowd and testimony.
- (2:165) [luna: strong; terra: contrast; basis: contrast+root+theme] وَمِنَ ٱلنَّاسِ مَن يَتَّخِذُ مِن دُونِ ٱللَّهِ أَندَادًۭا يُحِبُّونَهُمْ كَحُبِّ ٱللَّهِ ۖ وَٱلَّذِينَ ءَامَنُوٓا۟ أَشَدُّ حُبًّۭا لِّلَّهِ ۗ وَلَوْ يَرَى ٱلَّذِينَ ظَلَمُوٓا۟ إِذْ يَرَوْنَ ٱلْعَذَابَ أَنَّ ٱلْقُوَّةَ لِلَّهِ جَمِيعًۭا وَأَنَّ ٱللَّهَ شَدِيدُ ٱلْعَذَابِ
  Unverified discovery rationale: luna: The section describes intense love directed toward wealth; this verse contrasts that attachment with believers’ stronger love for God (أَشَدُّ حُبًّا لِّلَّهِ). | terra: Believers are أَشَدُّ حُبًّا لِلَّهِ, redirecting the section's intensity of love away from khayr-as-wealth toward God.
- (2:177) [luna: strong; basis: root+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section’s loved wealth is put into a giving scene: virtue includes giving one’s wealth, despite loving it, to relatives, orphans, the needy, and travelers.
- (2:261) [luna: strong; terra: contrast (missing-ayat turn); basis: contrast+root+scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section’s dictionary gloss gives حبّ the secondary sense “grain”; this verse makes a grain that yields seven ears the likeness for wealth spent in God’s way, turning attachment to wealth toward giving. | terra: Spending wealth is a grain that grows seven ears and multiplies, turning property and the inner “grain” into productive yield rather than hoarded barrenness.
- (2:264) [luna: strong; terra: medium; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section joins charity and soil; this verse warns that ostentatious charity is like a dusty smooth rock left bare by heavy rain, a crop-like image of giving emptied of fruit. | terra: A rock bearing dust is stripped bare by downpour as the image of ruined giving, joining dust, rain, and the failure of wealth to yield.
- (2:265) [luna: strong; terra: contrast; basis: contrast+scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: This verse pictures sincere spending as a garden on a height that yields abundantly after rain, linking charitable wealth to fertile ground. | terra: Those who spend for God's pleasure resemble a high garden whose rain doubles its yield, opposing both withheld wealth and foul soil's meagre growth.
- (2:266) [luna: strong; basis: contrast+scene] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
  Unverified discovery rationale: luna: A garden with palms and crops is destroyed by a fiery whirlwind just as its owner grows old and has young children, a concrete reversal of expected provision.
- (2:284) [luna: strong; terra: medium; basis: contrast+speaker+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The section says what lies within chests will be brought forth; this verse says God calls people to account for what they reveal or conceal within themselves. | terra: Whether people disclose or hide what is within themselves, God calls them to account for it, matching the final extraction and divine knowledge of breasts.
- (3:14) [luna: strong; terra: strong; basis: root+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section joins horses with a severe love of wealth; this verse lists gold and silver and fine horses among the things people love, bringing its horse and wealth images together. | terra: One catalogue of human desire contains hoarded gold and silver and branded horses, bringing the section's opening horses and later wealth-love into a single ayah.
- (3:29) [luna: medium; terra: strong; basis: scene+speaker+theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section ends with God’s knowledge of hidden chest contents; this verse says God knows what people conceal or disclose within themselves. | terra: Whether people hide what is in their breasts or reveal it, God knows it, directly answering the section's question about knowledge after breasts are opened.
- (3:92) [luna: strong; terra: contrast; basis: contrast+root+theme] لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section describes intense love of wealth; this verse says righteousness is not attained until one spends from what one loves (مِمَّا تُحِبُّونَ), making generosity the countermeasure. | terra: Righteousness requires spending مِمَّا تُحِبُّونَ, reversing the clenched attachment to beloved property by making that very love the measure of giving.
- (3:154) [luna: medium; terra: strong; basis: contrast+scene+theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section pictures inner contents being extracted; this verse says the trial at Uhud exposed what was in breasts and purified what was in hearts. | terra: Within a battle aftermath God tests مَا فِي صُدُورِكُمْ and assays مَا فِي قُلُوبِكُمْ, directly meeting the outer raid with inward refinement.
- (3:180) [luna: strong; terra: medium; basis: contrast+scene+theme] وَلَا يَحْسَبَنَّ ٱلَّذِينَ يَبْخَلُونَ بِمَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ هُوَ خَيْرًۭا لَّهُم ۖ بَلْ هُوَ شَرٌّۭ لَّهُمْ ۖ سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ ۗ وَلِلَّهِ مِيرَٰثُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
  Unverified discovery rationale: luna: The section depicts someone clutching accumulated wealth; this verse warns that what the miserly hoard will be made a collar around their necks on the Resurrection Day. | terra: What people withhold from God's bounty will be collared around them on resurrection day, converting retained property into exposed judgment.
- (4:41) [terra: strong (missing-ayat turn); basis: scene+theme] فَكَيْفَ إِذَا جِئْنَا مِن كُلِّ أُمَّةٍۭ بِشَهِيدٍۢ وَجِئْنَا بِكَ عَلَىٰ هَٰٓؤُلَآءِ شَهِيدًۭا
  Unverified discovery rationale: terra: A witness is brought from every community and the Messenger is brought as witness against his people, staging testimony in the assembled judgment.
- (4:135) [luna: strong; basis: contrast+speaker] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ بِٱلْقِسْطِ شُهَدَآءَ لِلَّهِ وَلَوْ عَلَىٰٓ أَنفُسِكُمْ أَوِ ٱلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ ۚ إِن يَكُنْ غَنِيًّا أَوْ فَقِيرًۭا فَٱللَّهُ أَوْلَىٰ بِهِمَا ۖ فَلَا تَتَّبِعُوا۟ ٱلْهَوَىٰٓ أَن تَعْدِلُوا۟ ۚ وَإِن تَلْوُۥٓا۟ أَوْ تُعْرِضُوا۟ فَإِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
  Unverified discovery rationale: luna: The section says the human bears witness against himself; this command requires standing as just witnesses even against oneself, making the adverse testimony explicit.
- (5:31) [luna: strong; terra: strong; basis: contrast+root+scene] فَبَعَثَ ٱللَّهُ غُرَابًۭا يَبْحَثُ فِى ٱلْأَرْضِ لِيُرِيَهُۥ كَيْفَ يُوَٰرِى سَوْءَةَ أَخِيهِ ۚ قَالَ يَٰوَيْلَتَىٰٓ أَعَجَزْتُ أَنْ أَكُونَ مِثْلَ هَٰذَا ٱلْغُرَابِ فَأُوَٰرِىَ سَوْءَةَ أَخِى ۖ فَأَصْبَحَ مِنَ ٱلنَّٰدِمِينَ
  Unverified discovery rationale: luna: The section’s dictionary explanation links making fire with covering the buried; this verse uses the covering verb (يُوَارِي) as a raven shows how to conceal a dead body in the earth. | terra: The raven shows Cain how يُوَارِي his brother's corpse in earth; the w-r-y wording hides a body where the section's cognate fire-making discloses flame, before graves disclose bodies again.
- (5:109) [terra: strong; basis: scene+speaker+theme] ۞ يَوْمَ يَجْمَعُ ٱللَّهُ ٱلرُّسُلَ فَيَقُولُ مَاذَآ أُجِبْتُمْ ۖ قَالُوا۟ لَا عِلْمَ لَنَآ ۖ إِنَّكَ أَنتَ عَلَّٰمُ ٱلْغُيُوبِ
  Unverified discovery rationale: terra: God gathers the messengers, asks what answer they received, and they defer knowledge to the Knower of unseen things; gathering, question, and ultimate knowledge converge.
- (6:22) [terra: strong (missing-ayat turn); basis: scene+speaker] وَيَوْمَ نَحْشُرُهُمْ جَمِيعًۭا ثُمَّ نَقُولُ لِلَّذِينَ أَشْرَكُوٓا۟ أَيْنَ شُرَكَآؤُكُمُ ٱلَّذِينَ كُنتُمْ تَزْعُمُونَ
  Unverified discovery rationale: terra: God gathers all of them and then questions the associators, joining assembly with the interrogative disclosure of what they had served.
- (6:95) [luna: strong; terra: strong; basis: root+scene+theme] ۞ إِنَّ ٱللَّهَ فَالِقُ ٱلْحَبِّ وَٱلنَّوَىٰ ۖ يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَمُخْرِجُ ٱلْمَيِّتِ مِنَ ٱلْحَىِّ ۚ ذَٰلِكُمُ ٱللَّهُ ۖ فَأَنَّىٰ تُؤْفَكُونَ
  Unverified discovery rationale: luna: The section’s dictionary gloss connects حبّ, “love,” with حبّ, “grain”; this verse names grain and date-stones, then says God brings the living out of the dead, joining the wordplay to emergence. | terra: فَالِقُ الْحَبِّ وَالنَّوَىٰ brings grain from its enclosure and the living from the dead; ḥabb, the section's lexical heart of ḥubb, is opened into a resurrection image.
- (6:99) [luna: strong; terra: medium (missing-ayat turn); basis: root+scene+theme] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: luna: This verse connects rain to growing plants, grain, and ripening fruit, supplying the crop-and-provision side of the section’s soil imagery. | terra: Rain brings forth vegetation, clustered grain, and fruit, supplying the productive field and extracted grain against which barren kenūd earth is read.
- (6:130) [luna: strong; basis: speaker+theme] يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَقُصُّونَ عَلَيْكُمْ ءَايَٰتِى وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ شَهِدْنَا عَلَىٰٓ أَنفُسِنَا ۖ وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
  Unverified discovery rationale: luna: At judgment, humans and jinn are asked whether they bore witness against themselves; this matches the section’s testimony about one’s own conduct before God.
- (7:57) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶50] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: luna: The section links rain-revived soil to the dead brought out of graves; after sending winds and rain, God says, “Thus We bring forth the dead” (نُخْرِجُ الْمَوْتَىٰ). | terra: Rain is driven to dead land and brings fruit before كَذَٰلِكَ نُخْرِجُ الْمَوْتَىٰ; it states the section's rain-to-grave analogy outright.
- (7:58) [luna: strong; terra: strong; basis: contrast+scene] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
  Unverified discovery rationale: luna: The section calls the unproductive kenud land to mind; this neighboring verse contrasts good land that yields by its Lord’s permission with poor land yielding little. | terra: Good soil yields by its Lord's leave whereas foul soil yields only نَكِدًا; this is the productive-earth boundary behind the section's kenūd soil before the same earth opens its graves.
- (7:172) [luna: strong; terra: strong; basis: scene+speaker+theme] وَإِذْ أَخَذَ رَبُّكَ مِنۢ بَنِىٓ ءَادَمَ مِن ظُهُورِهِمْ ذُرِّيَّتَهُمْ وَأَشْهَدَهُمْ عَلَىٰٓ أَنفُسِهِمْ أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ ۛ شَهِدْنَآ ۛ أَن تَقُولُوا۟ يَوْمَ ٱلْقِيَٰمَةِ إِنَّا كُنَّا عَنْ هَٰذَا غَٰفِلِينَ
  Unverified discovery rationale: luna: The section says a person is witness against himself before his Lord; here humanity answers “Yes, we bear witness” (بَلَىٰ شَهِدْنَا) to the question “Am I not your Lord?” | terra: Humanity answers أَلَسْتُ بِرَبِّكُمْ with بَلَىٰ شَهِدْنَا, the covenant scene behind a human being witness upon himself concerning his Lord.
- (8:37) [terra: strong; basis: scene+theme] لِيَمِيزَ ٱللَّهُ ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ وَيَجْعَلَ ٱلْخَبِيثَ بَعْضَهُۥ عَلَىٰ بَعْضٍۢ فَيَرْكُمَهُۥ جَمِيعًۭا فَيَجْعَلَهُۥ فِى جَهَنَّمَ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
  Unverified discovery rationale: terra: God separates the foul from the good, heaps the foul جَمِيعًا, and puts it in Hell; sorting, gathering, and fire converge exactly as in the section's ore image.
- (8:43) [terra: strong (missing-ayat turn); basis: scene+theme] إِذْ يُرِيكَهُمُ ٱللَّهُ فِى مَنَامِكَ قَلِيلًۭا ۖ وَلَوْ أَرَىٰكَهُمْ كَثِيرًۭا لَّفَشِلْتُمْ وَلَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَلَٰكِنَّ ٱللَّهَ سَلَّمَ ۗ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: In an actual battle setting God controls the army's perceived size and is declared knowing of what breasts contain, joining outward conflict to inward knowledge.
- (8:60) [luna: strong; terra: medium; basis: scene+theme] وَأَعِدُّوا۟ لَهُم مَّا ٱسْتَطَعْتُم مِّن قُوَّةٍۢ وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ وَعَدُوَّكُمْ وَءَاخَرِينَ مِن دُونِهِمْ لَا تَعْلَمُونَهُمُ ٱللَّهُ يَعْلَمُهُمْ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فِى سَبِيلِ ٱللَّهِ يُوَفَّ إِلَيْكُمْ وَأَنتُمْ لَا تُظْلَمُونَ
  Unverified discovery rationale: luna: The section opens with horses charging in a dawn raid; 8:60 explicitly prepares steeds (رِبَاطِ الْخَيْلِ) to frighten enemies, giving the charge its military setting. | terra: رِبَاطِ الْخَيْلِ is prepared to terrify an enemy, confirming the opening animals as horses readied for hostile action rather than mere travel.
- (9:34) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶51] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ كَثِيرًۭا مِّنَ ٱلْأَحْبَارِ وَٱلرُّهْبَانِ لَيَأْكُلُونَ أَمْوَٰلَ ٱلنَّاسِ بِٱلْبَٰطِلِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ ۗ وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ فَبَشِّرْهُم بِعَذَابٍ أَلِيمٍۢ
  Unverified discovery rationale: luna: The section joins hoarded wealth to what is drawn out of the chest; this verse names those who hoard gold and silver (يَكْنِزُونَ الذَّهَبَ وَالْفِضَّةَ). | terra: Those who hoard gold and silver and do not spend name the accumulated treasure that the section places beside the assaying of what lies in breasts.
- (9:35) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶51] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
  Unverified discovery rationale: luna: The section says stored gold and silver meet fire; here the hoarded metals are heated in Hellfire and used to brand their owners. | terra: Hoarded metal is heated in Hell and used to brand foreheads, sides, and backs, fusing treasure, fire, and the exposure of its owner.
- (9:103) [luna: strong; basis: scene+theme] خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section links collected wealth with inner purification; this verse commands taking charity from their wealth to cleanse and purify them (تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا).
- (10:24) [luna: strong; terra: medium; basis: contrast+scene+theme] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: The section moves from rain-fed soil toward final disclosure; this verse says luxuriant growth is suddenly cut down as though it had not flourished, exposing how temporary a harvest can be. | terra: Rain-grown earth reaches full adornment just as its people think they control it, then God's command leaves it harvested; it parallels the garden owners' confident seizure and sudden loss.
- (11:5) [terra: strong; basis: scene+theme] أَلَآ إِنَّهُمْ يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ ۚ أَلَا حِينَ يَسْتَغْشُونَ ثِيَابَهُمْ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: People fold their breasts to hide, yet God knows what they conceal and disclose and is عَلِيمٌ بِذَاتِ الصُّدُورِ; it states the section's outward-to-inward penetration.
- (11:103) [terra: strong; basis: root+scene+theme] إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّمَنْ خَافَ عَذَابَ ٱلْءَاخِرَةِ ۚ ذَٰلِكَ يَوْمٌۭ مَّجْمُوعٌۭ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌۭ مَّشْهُودٌۭ
  Unverified discovery rationale: terra: The Last Day is يَوْمٌ مَجْمُوعٌ لَهُ النَّاسُ and يَوْمٌ مَشْهُودٌ, fusing universal gathering with witnessed presence.
- (13:17) [terra: strong; basis: scene+theme] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
  Unverified discovery rationale: terra: Floodwater bears foam while heated ore casts up dross, and what benefits people remains; this is the Quranic assay scene behind separating precious metal from earth and sorting the inward residue.
- (14:21) [terra: strong (missing-ayat turn); basis: scene+theme] وَبَرَزُوا۟ لِلَّهِ جَمِيعًۭا فَقَالَ ٱلضُّعَفَٰٓؤُا۟ لِلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُنَّا لَكُمْ تَبَعًۭا فَهَلْ أَنتُم مُّغْنُونَ عَنَّا مِنْ عَذَابِ ٱللَّهِ مِن شَىْءٍۢ ۚ قَالُوا۟ لَوْ هَدَىٰنَا ٱللَّهُ لَهَدَيْنَٰكُمْ ۖ سَوَآءٌ عَلَيْنَآ أَجَزِعْنَآ أَمْ صَبَرْنَا مَا لَنَا مِن مَّحِيصٍۢ
  Unverified discovery rationale: terra: وَبَرَزُوا لِلَّهِ جَمِيعًا presents everyone emerging together before God, an exact outer manifestation of the hidden dead into a gathered crowd.
- (14:48) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ تُبَدَّلُ ٱلْأَرْضُ غَيْرَ ٱلْأَرْضِ وَٱلسَّمَٰوَٰتُ ۖ وَبَرَزُوا۟ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
  Unverified discovery rationale: luna: The section moves from overturned graves toward the universal gathering; this verse says the earth will be changed to another earth and people will come out before God. | terra: When earth and heavens are changed, all people emerge before the One, the Overwhelming, combining transformed ground, exposure, and universal presence.
- (16:84) [terra: strong (missing-ayat turn); basis: scene+theme] وَيَوْمَ نَبْعَثُ مِن كُلِّ أُمَّةٍۢ شَهِيدًۭا ثُمَّ لَا يُؤْذَنُ لِلَّذِينَ كَفَرُوا۟ وَلَا هُمْ يُسْتَعْتَبُونَ
  Unverified discovery rationale: terra: On the day a witness is raised from every community, deniers receive no leave to answer, making adverse testimony decisive.
- (17:13) [luna: strong; terra: strong (missing-ayat turn); basis: scene+theme] وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا
  Unverified discovery rationale: luna: The section ends in the Lord’s knowledge of people’s inner contents; this verse fastens each person’s record to them and brings it out on the Day of Resurrection. | terra: Each person's deeds are fastened to his neck and God brings out an open record at resurrection, externalizing what had accompanied him unseen.
- (17:14) [luna: strong; terra: medium; basis: scene+speaker+theme] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
  Unverified discovery rationale: luna: The record tells each person to read, since their own self suffices as an accountant (كَفَىٰ بِنَفْسِكَ الْيَوْمَ عَلَيْكَ حَسِيبًا), matching the section’s self-witness. | terra: The resurrected person reads his own record and is sufficient as accountant against himself, another form of self-testimony at judgment.
- (17:29) [luna: strong; terra: medium; basis: scene+theme] وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ فَتَقْعُدَ مَلُومًۭا مَّحْسُورًا
  Unverified discovery rationale: luna: The section portrays the hand closed around wealth; this verse says not to keep one’s hand chained to the neck, an explicit image of miserliness. | terra: The hand must not be chained to the neck nor wholly outspread; its bodily image sets the boundary around the section's clenched hand of withholding.
- (17:49) [luna: strong; basis: scene] وَقَالُوٓا۟ أَءِذَا كُنَّا عِظَٰمًۭا وَرُفَٰتًا أَءِنَّا لَمَبْعُوثُونَ خَلْقًۭا جَدِيدًۭا
  Unverified discovery rationale: luna: The section asks whether people know when the graves are overturned; these disbelievers ask whether they will be raised as bones and dust.
- (17:50) [luna: strong; basis: neighbour+scene] ۞ قُلْ كُونُوا۟ حِجَارَةً أَوْ حَدِيدًا
  Unverified discovery rationale: luna: This reply to 17:49 commands the doubters to become stone or iron, keeping the question of bodily return in view.
- (17:51) [luna: strong; basis: neighbour+scene] أَوْ خَلْقًۭا مِّمَّا يَكْبُرُ فِى صُدُورِكُمْ ۚ فَسَيَقُولُونَ مَن يُعِيدُنَا ۖ قُلِ ٱلَّذِى فَطَرَكُمْ أَوَّلَ مَرَّةٍۢ ۚ فَسَيُنْغِضُونَ إِلَيْكَ رُءُوسَهُمْ وَيَقُولُونَ مَتَىٰ هُوَ ۖ قُلْ عَسَىٰٓ أَن يَكُونَ قَرِيبًۭا
  Unverified discovery rationale: luna: The reply continues that God will restore them even if they become something they regard as still harder to raise.
- (17:52) [luna: strong; terra: medium; basis: scene+speaker+theme] يَوْمَ يَدْعُوكُمْ فَتَسْتَجِيبُونَ بِحَمْدِهِۦ وَتَظُنُّونَ إِن لَّبِثْتُمْ إِلَّا قَلِيلًۭا
  Unverified discovery rationale: luna: This verse completes the response to 17:49–51: on the day God calls, people answer with praise and think they remained only briefly. | terra: On the day God calls, people answer and think they stayed only a little, a collective movement initiated by the Lord's summons.
- (17:64) [luna: weak; terra: strong; basis: scene+theme] وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ وَشَارِكْهُمْ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ وَعِدْهُمْ ۚ وَمَا يَعِدُهُمُ ٱلشَّيْطَٰنُ إِلَّا غُرُورًا
  Unverified discovery rationale: luna: The section’s charging horses are a literal raid; the devil’s “cavalry and infantry” (بِخَيْلِكَ وَرَجِلِكَ) is a specific but metaphorical mounted assault, so the scene correspondence is indirect. | terra: The command to charge with cavalry and infantry then share in الأموال joins an attacking mounted force to corrupted attachment to property.
- (17:100) [luna: strong (missing-ayat turn); basis: contrast+theme] قُل لَّوْ أَنتُمْ تَمْلِكُونَ خَزَآئِنَ رَحْمَةِ رَبِّىٓ إِذًۭا لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ ۚ وَكَانَ ٱلْإِنسَٰنُ قَتُورًۭا
  Unverified discovery rationale: luna: The section exposes attachment to stored wealth; this verse says that even if people possessed their Lord’s treasuries of mercy they would withhold for fear of spending, and calls the human miserly (قَتُورًا).
- (18:32) [luna: strong; basis: scene+theme] ۞ وَٱضْرِبْ لَهُم مَّثَلًۭا رَّجُلَيْنِ جَعَلْنَا لِأَحَدِهِمَا جَنَّتَيْنِ مِنْ أَعْنَٰبٍۢ وَحَفَفْنَٰهُمَا بِنَخْلٍۢ وَجَعَلْنَا بَيْنَهُمَا زَرْعًۭا
  Unverified discovery rationale: luna: The section connects a garden to a wealthy owner; this parable centers on two men, one given two gardens and abundant produce.
- (18:34) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+scene+theme] وَكَانَ لَهُۥ ثَمَرٌۭ فَقَالَ لِصَٰحِبِهِۦ وَهُوَ يُحَاوِرُهُۥٓ أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا
  Unverified discovery rationale: luna: The garden owner boasts of greater wealth and more supporters, illustrating the section’s attachment to stored goods before its reversal. | terra: The garden owner boasts that he has more wealth and a stronger following, making property the basis of his false security.
- (18:35) [luna: strong; terra: medium (missing-ayat turn); basis: scene+theme] وَدَخَلَ جَنَّتَهُۥ وَهُوَ ظَالِمٌۭ لِّنَفْسِهِۦ قَالَ مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا
  Unverified discovery rationale: luna: Like the section’s garden owners, this wealthy man enters his garden confident in it, while his own soul remains in view. | terra: He enters his garden while wronging himself and claims it will never perish, the possessive confidence later answered by destruction.
- (18:36) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+neighbour+theme] وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّدِدتُّ إِلَىٰ رَبِّى لَأَجِدَنَّ خَيْرًۭا مِّنْهَا مُنقَلَبًۭا
  Unverified discovery rationale: luna: The garden owner denies that the Hour will come and doubts return to his Lord, a direct contrast to the section’s coming resurrection and disclosure. | terra: He doubts the Hour and assumes an even better return, linking attachment to his garden with denial of final reckoning.
- (18:40) [luna: strong (missing-ayat turn); terra: medium (missing-ayat turn); basis: contrast+neighbour+scene] فَعَسَىٰ رَبِّىٓ أَن يُؤْتِيَنِ خَيْرًۭا مِّن جَنَّتِكَ وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا
  Unverified discovery rationale: luna: The companion warns in 18:39’s garden dialogue that God may give him a better garden and send a calamity on the other one, leaving it bare ground; this is a direct parallel to the section’s planned harvest reversed by a garden’s ruin. | terra: His companion warns that God may send a calamity from heaven so the garden becomes barren ground, anticipating the owner's reversal.
- (18:42) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+scene+theme] وَأُحِيطَ بِثَمَرِهِۦ فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا وَيَقُولُ يَٰلَيْتَنِى لَمْ أُشْرِكْ بِرَبِّىٓ أَحَدًۭا
  Unverified discovery rationale: luna: The man’s garden and wealth are destroyed; he wrings his hands over what he spent on it, reversing the confidence of 18:35–36. | terra: The wealthy garden owner's produce is encompassed, and he wrings his hands over what he spent as the garden collapses, a second garden scene where confident possession is overturned.
- (18:43) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا
  Unverified discovery rationale: luna: After the garden is destroyed, no group can help its owner; this meets the section’s image of a gathering where wealth cannot protect its holder. | terra: No group can help the garden owner against God after the loss, stripping amassed property of protective power.
- (18:45) [luna: strong; terra: medium; basis: contrast+scene+theme] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
  Unverified discovery rationale: luna: This verse compares worldly life to rain-grown plants that dry and scatter, then contrasts passing wealth and children with lasting good deeds. | terra: Rain-mingled vegetation becomes dry fragments scattered by wind, a field image in which apparent abundance ends as dispersed matter.
- (18:46) [luna: strong; terra: medium; basis: contrast+neighbour+theme] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
  Unverified discovery rationale: luna: The section follows wealth into the gathering and sorting of the heart; this verse calls wealth and children the adornment of worldly life but says lasting good deeds are better. | terra: Wealth is the adornment of near life while lasting good deeds are better, interpreting the transient field of 18:45 against attachment to property.
- (18:47) [terra: strong; basis: scene+theme] وَيَوْمَ نُسَيِّرُ ٱلْجِبَالَ وَتَرَى ٱلْأَرْضَ بَارِزَةًۭ وَحَشَرْنَٰهُمْ فَلَمْ نُغَادِرْ مِنْهُمْ أَحَدًۭا
  Unverified discovery rationale: terra: The earth is laid bare and all people are gathered without one being left, supplying the universal crowd into whose midst the section's movement ends.
- (18:49) [terra: strong (missing-ayat turn); basis: scene+theme] وَوُضِعَ ٱلْكِتَٰبُ فَتَرَى ٱلْمُجْرِمِينَ مُشْفِقِينَ مِمَّا فِيهِ وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا ۗ وَلَا يَظْلِمُ رَبُّكَ أَحَدًۭا
  Unverified discovery rationale: terra: The record is laid open and people find every deed present; nothing inwardly accumulated is omitted from the final disclosure.
- (18:99) [terra: strong (missing-ayat turn); basis: scene+theme] ۞ وَتَرَكْنَا بَعْضَهُمْ يَوْمَئِذٍۢ يَمُوجُ فِى بَعْضٍۢ ۖ وَنُفِخَ فِى ٱلصُّورِ فَجَمَعْنَٰهُمْ جَمْعًۭا
  Unverified discovery rationale: terra: People surge into one another, the trumpet is blown, and God gathers them with a total gathering; moving multitude and assembly converge.
- (19:85) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
  Unverified discovery rationale: terra: The Godfearing are gathered to the Merciful as a delegation, giving the final crowd a differentiated destination and manner of arrival.
- (19:86) [terra: strong (missing-ayat turn); basis: contrast+scene] وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا
  Unverified discovery rationale: terra: The guilty are driven to Hell وِرْدًا, like a thirsty herd driven to water; the watering-place image becomes a grim final destination.
- (20:55) [terra: strong (missing-ayat turn); basis: scene+theme] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
  Unverified discovery rationale: terra: Humans are created from earth, returned into it, and brought out from it once more; burial and emergence are stated as one complete earth-cycle.
- (22:5) [luna: strong; terra: strong; basis: scene+theme] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
  Unverified discovery rationale: luna: The section moves from soil and rain to graves; this verse joins rain making the earth stir and grow to human creation, death, and emergence from the ground. | terra: Human formation, barren earth, descending water, and stirred growth are staged together as a detailed demonstration addressed to doubters of resurrection.
- (22:6) [luna: strong; terra: medium; basis: neighbour+scene+theme] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّهُۥ يُحْىِ ٱلْمَوْتَىٰ وَأَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The verse states that God gives life to dead earth and can revive the dead, making the section’s rain-and-resurrection meeting explicit. | terra: Between the barren-earth demonstration and the raised graves, the ayah states that God is the truth and gives life to the dead.
- (22:7) [luna: strong; terra: strong; basis: scene+theme] وَأَنَّ ٱلسَّاعَةَ ءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ
  Unverified discovery rationale: luna: The section’s overturning of graves is stated directly: the Hour comes and God raises those in the graves (فِي الْقُبُورِ). | terra: God will raise مَنْ فِي الْقُبُورِ, making explicit what the revived-earth demonstration in 22:5 proves.
- (23:79) [terra: strong (missing-ayat turn); basis: scene+theme] وَهُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
  Unverified discovery rationale: terra: God dispersed humanity through earth and to Him they will be gathered, moving from earthly distribution to final collection.
- (24:24) [luna: strong; terra: strong; basis: scene+speaker+theme] يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: The section’s human is witness against himself; here tongues, hands, and feet testify against people for what they did. | terra: Tongues, hands, and feet testify عَلَيْهِمْ about what people did, a direct instance of witness working against its human subject.
- (28:23) [terra: strong; basis: root+scene] وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ وَوَجَدَ مِن دُونِهِمُ ٱمْرَأَتَيْنِ تَذُودَانِ ۖ قَالَ مَا خَطْبُكُمَا ۖ قَالَتَا لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌۭ كَبِيرٌۭ
  Unverified discovery rationale: terra: At Midian's water the women wait حَتَّىٰ يُصْدِرَ الرِّعَاءُ; this actual flock-leaving-water scene supplies the concrete dictionary image carried by يَصْدُرُ in 99:6 and ṣudūr in the section.
- (28:76) [luna: strong; terra: medium; basis: scene+theme] ۞ إِنَّ قَٰرُونَ كَانَ مِن قَوْمِ مُوسَىٰ فَبَغَىٰ عَلَيْهِمْ ۖ وَءَاتَيْنَٰهُ مِنَ ٱلْكُنُوزِ مَآ إِنَّ مَفَاتِحَهُۥ لَتَنُوٓأُ بِٱلْعُصْبَةِ أُو۟لِى ٱلْقُوَّةِ إِذْ قَالَ لَهُۥ قَوْمُهُۥ لَا تَفْرَحْ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْفَرِحِينَ
  Unverified discovery rationale: luna: The section examines attachment to wealth; Qarun is introduced as possessing great treasure and boasting over it. | terra: Qarun's treasure keys burden a strong company, giving amassed wealth the concrete weight that precedes his return into earth.
- (28:77) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+theme] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
  Unverified discovery rationale: luna: This verse tells Qarun to seek the Hereafter with what God has given him and do good, a specific alternative to making wealth the heart’s object. | terra: Qarun is told to seek the afterlife with what God gave him and to do good, setting use of wealth against possessive accumulation.
- (28:78) [luna: strong; terra: medium; basis: contrast+speaker+theme] قَالَ إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍ عِندِىٓ ۚ أَوَلَمْ يَعْلَمْ أَنَّ ٱللَّهَ قَدْ أَهْلَكَ مِن قَبْلِهِۦ مِنَ ٱلْقُرُونِ مَنْ هُوَ أَشَدُّ مِنْهُ قُوَّةًۭ وَأَكْثَرُ جَمْعًۭا ۚ وَلَا يُسْـَٔلُ عَن ذُنُوبِهِمُ ٱلْمُجْرِمُونَ
  Unverified discovery rationale: luna: Qarun credits his own knowledge for his wealth, while this verse reminds him that God destroyed stronger and wealthier generations. | terra: Qarun claims his treasure came through knowledge he possesses, while the ayah answers with God's prior destruction of stronger accumulators; claimed knowledge meets divine knowledge and judgment.
- (28:79) [terra: strong (missing-ayat turn); basis: scene+theme] فَخَرَجَ عَلَىٰ قَوْمِهِۦ فِى زِينَتِهِۦ ۖ قَالَ ٱلَّذِينَ يُرِيدُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا يَٰلَيْتَ لَنَا مِثْلَ مَآ أُوتِىَ قَٰرُونُ إِنَّهُۥ لَذُو حَظٍّ عَظِيمٍۢ
  Unverified discovery rationale: terra: Qarun comes out in his adornment and people who desire near life wish for his wealth, exposing the attractive force of treasure before earth takes it.
- (28:81) [luna: strong; terra: contrast; basis: contrast+scene+theme] فَخَسَفْنَا بِهِۦ وَبِدَارِهِ ٱلْأَرْضَ فَمَا كَانَ لَهُۥ مِن فِئَةٍۢ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مِنَ ٱلْمُنتَصِرِينَ
  Unverified discovery rationale: luna: The earth swallows Qarun and his house, making the section’s movement from earthly treasure to what lies under the ground a concrete reversal. | terra: The earth swallows Qarun and his house, so amassed treasure ends with its owner hidden below the same earth that will later cast the buried out.
- (28:82) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَأَصْبَحَ ٱلَّذِينَ تَمَنَّوْا۟ مَكَانَهُۥ بِٱلْأَمْسِ يَقُولُونَ وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ ۖ لَوْلَآ أَن مَّنَّ ٱللَّهُ عَلَيْنَا لَخَسَفَ بِنَا ۖ وَيْكَأَنَّهُۥ لَا يُفْلِحُ ٱلْكَٰفِرُونَ
  Unverified discovery rationale: luna: After the earth swallows Qarun in 28:81, those who had envied him recognize that God expands and restricts provision, completing the section’s reversal of hoarded wealth. | terra: After Qarun is swallowed, his former admirers recognize God's control of provision and the unbeliever's failure, converting desire into belated knowledge.
- (30:25) [terra: strong; basis: scene+speaker] وَمِنْ ءَايَٰتِهِۦٓ أَن تَقُومَ ٱلسَّمَآءُ وَٱلْأَرْضُ بِأَمْرِهِۦ ۚ ثُمَّ إِذَا دَعَاكُمْ دَعْوَةًۭ مِّنَ ٱلْأَرْضِ إِذَآ أَنتُمْ تَخْرُجُونَ
  Unverified discovery rationale: terra: At one divine call from earth إِذَا أَنْتُمْ تَخْرُجُونَ, joining the Lord's summons to sudden bodily emergence.
- (30:50) [luna: strong; terra: medium; basis: scene+theme] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The verse tells the reader to look at God’s mercy in reviving earth after its death and says He will likewise revive the dead, matching the section’s rain-to-grave movement. | terra: The hearer is told to look at revived earth and infer that its reviver gives life to the dead.
- (31:16) [luna: strong; basis: root+scene+theme] يَٰبُنَىَّ إِنَّهَآ إِن تَكُ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ فَتَكُن فِى صَخْرَةٍ أَوْ فِى ٱلسَّمَٰوَٰتِ أَوْ فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ ۚ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌۭ
  Unverified discovery rationale: luna: The section’s source gloss links حبّ to grain and its ending to hidden contents known by God; this verse says even a mustard seed inside a rock or earth will be brought forth by God.
- (34:2) [terra: strong (missing-ayat turn); basis: scene+theme] يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۚ وَهُوَ ٱلرَّحِيمُ ٱلْغَفُورُ
  Unverified discovery rationale: terra: God knows what enters the earth and what emerges from it, placing the grave's concealed occupant and final coming-out under one knowledge.
- (34:40) [terra: strong (missing-ayat turn); basis: scene+speaker] وَيَوْمَ يَحْشُرُهُمْ جَمِيعًۭا ثُمَّ يَقُولُ لِلْمَلَٰٓئِكَةِ أَهَٰٓؤُلَآءِ إِيَّاكُمْ كَانُوا۟ يَعْبُدُونَ
  Unverified discovery rationale: terra: God gathers everyone and questions the angels about the people's worship, another final crowd brought under divine questioning and superior knowledge.
- (35:9) [luna: strong; terra: strong; basis: scene+theme] وَٱللَّهُ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَسُقْنَٰهُ إِلَىٰ بَلَدٍۢ مَّيِّتٍۢ فَأَحْيَيْنَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ كَذَٰلِكَ ٱلنُّشُورُ
  Unverified discovery rationale: luna: God drives clouds, revives dead land with rain, and the verse says resurrection will be like that; this directly bridges the section’s weathered ground and raised dead. | terra: Winds drive cloud to dead land and revive earth after death, followed by كَذَٰلِكَ النُّشُورُ; rain and emergence are identified.
- (36:33) [terra: strong; basis: root+scene+theme] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
  Unverified discovery rationale: terra: A dead earth is revived and حَبًّا is brought out for people to eat; hidden grain, extraction, and life from death meet in one sign.
- (36:51) [luna: strong; terra: strong; basis: scene+theme] وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ
  Unverified discovery rationale: luna: The section’s dead emerge and run to the gathering; here the trumpet is blown and people rush from graves toward their Lord. | terra: At the trumpet they move from the graves إِلَىٰ رَبِّهِمْ يَنْسِلُونَ, a rapid human counterpart to the opening charge.
- (36:52) [luna: strong; basis: neighbour+scene] قَالُوا۟ يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا ۜ ۗ هَٰذَا مَا وَعَدَ ٱلرَّحْمَٰنُ وَصَدَقَ ٱلْمُرْسَلُونَ
  Unverified discovery rationale: luna: The newly raised ask who woke them from their resting place, giving voice to the section’s overturned-grave scene.
- (36:53) [luna: strong; basis: neighbour+scene] إِن كَانَتْ إِلَّا صَيْحَةًۭ وَٰحِدَةًۭ فَإِذَا هُمْ جَمِيعٌۭ لَّدَيْنَا مُحْضَرُونَ
  Unverified discovery rationale: luna: The answer to 36:52 is a single blast, after which all are brought before God; this completes the section’s movement to a universal gathering.
- (36:65) [luna: strong; terra: strong; basis: scene+speaker+theme] ٱلْيَوْمَ نَخْتِمُ عَلَىٰٓ أَفْوَٰهِهِمْ وَتُكَلِّمُنَآ أَيْدِيهِمْ وَتَشْهَدُ أَرْجُلُهُم بِمَا كَانُوا۟ يَكْسِبُونَ
  Unverified discovery rationale: luna: This verse seals mouths while hands speak and testify to what people earned, a bodily counterpart to the section’s witness and revealed contents. | terra: Mouths are sealed while hands speak and feet testify to earnings, turning bodily action into testimony against the person who performed it.
- (36:77) [terra: strong (missing-ayat turn); basis: neighbour+theme] أَوَلَمْ يَرَ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن نُّطْفَةٍۢ فَإِذَا هُوَ خَصِيمٌۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: The resurrection objector is reminded that God created him from a drop before he became an open adversary; his denial itself displays human ingratitude to his Originator.
- (36:78) [luna: strong; terra: strong; basis: scene+speaker+theme] وَضَرَبَ لَنَا مَثَلًۭا وَنَسِىَ خَلْقَهُۥ ۖ قَالَ مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌۭ
  Unverified discovery rationale: luna: The section uses fire as evidence for resurrection; this verse poses the challenge of reviving bones after they have decayed. | terra: The challenger asks who will revive bones when they are decayed, supplying the denial to which the section's green-tree fire answers.
- (36:79) [luna: strong; terra: strong; basis: scene+theme] قُلْ يُحْيِيهَا ٱلَّذِىٓ أَنشَأَهَآ أَوَّلَ مَرَّةٍۢ ۖ وَهُوَ بِكُلِّ خَلْقٍ عَلِيمٌ
  Unverified discovery rationale: luna: The answer to 36:78 says the one who made the bones the first time will give them life again (أَنشَأَهَا أَوَّلَ مَرَّةٍ). | terra: The answer that their first Originator will revive them fixes the resurrection claim that the following tree-fire image demonstrates.
- (36:80) [luna: strong; terra: strong; basis: root+scene+theme] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
  Unverified discovery rationale: luna: The section links hidden fire brought out by striking to hidden people brought from earth; this verse points to fire produced from green trees (مِنَ الشَّجَرِ الْأَخْضَرِ نَارًا) as a sign of the Creator’s power. | terra: God makes fire from the green tree and people kindle from it; latent fire brought out of wood parallels bodies brought out of earth.
- (36:81) [terra: strong; basis: speaker+theme] أَوَلَيْسَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِقَٰدِرٍ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُم ۚ بَلَىٰ وَهُوَ ٱلْخَلَّٰقُ ٱلْعَلِيمُ
  Unverified discovery rationale: terra: The Creator of heavens and earth is declared able to create their like, drawing the tree-fire proof back to bodily resurrection.
- (38:31) [terra: strong; basis: neighbour+scene] إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ
  Unverified discovery rationale: terra: The displayed الصَّافِنَاتُ الْجِيَادُ identifies the excellent horses that the next ayah calls حُبَّ الْخَيْرِ.
- (38:32) [terra: strong; basis: root+scene+theme] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
  Unverified discovery rationale: terra: Solomon's إِنِّي أَحْبَبْتُ حُبَّ الْخَيْرِ speaks of the displayed horses with the same love-of-khayr wording that follows the horses in surah 100.
- (39:68) [terra: strong (missing-ayat turn); basis: scene+theme] وَنُفِخَ فِى ٱلصُّورِ فَصَعِقَ مَن فِى ٱلسَّمَٰوَٰتِ وَمَن فِى ٱلْأَرْضِ إِلَّا مَن شَآءَ ٱللَّهُ ۖ ثُمَّ نُفِخَ فِيهِ أُخْرَىٰ فَإِذَا هُمْ قِيَامٌۭ يَنظُرُونَ
  Unverified discovery rationale: terra: After the second trumpet blast, all are standing and looking, a sudden collective emergence into visible awareness.
- (39:69) [terra: strong (missing-ayat turn); basis: scene+theme] وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: terra: The earth shines by its Lord, the record is set down, and prophets and witnesses are brought; opened earth, disclosure, and testimony meet.
- (40:16) [terra: strong; basis: scene+theme] يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ ۚ لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
  Unverified discovery rationale: terra: On the day people are بَارِزُونَ, nothing about them is hidden from God; bodily emergence and total disclosure occur together.
- (41:20) [luna: strong; terra: strong; basis: scene+speaker+theme] حَتَّىٰٓ إِذَا مَا جَآءُوهَا شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم بِمَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: luna: The section makes the person a witness on himself; here hearing, sight, and skin testify to what people did (شَهِدَ عَلَيْهِمْ سَمْعُهُمْ). | terra: At the Fire, hearing, sight, and skins testify against their owners about their deeds, joining embodied witness, exposure, and punishment.
- (41:21) [luna: strong; terra: medium; basis: neighbour+scene+speaker] وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا ۖ قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍۢ وَهُوَ خَلَقَكُمْ أَوَّلَ مَرَّةٍۢ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: luna: When the people ask their skins why they testified in 41:20, the skins answer that God made everything speak, completing the testimony scene. | terra: The skins answer that God who gives speech to everything made them speak, explaining the adverse testimony staged in 41:20.
- (41:22) [luna: strong; terra: strong; basis: neighbour+scene+theme] وَمَا كُنتُمْ تَسْتَتِرُونَ أَن يَشْهَدَ عَلَيْكُمْ سَمْعُكُمْ وَلَآ أَبْصَٰرُكُمْ وَلَا جُلُودُكُمْ وَلَٰكِن ظَنَنتُمْ أَنَّ ٱللَّهَ لَا يَعْلَمُ كَثِيرًۭا مِّمَّا تَعْمَلُونَ
  Unverified discovery rationale: luna: This neighboring verse says they had not concealed themselves from their own hearing, sight, or skin, joining testimony to the section’s exposed inward contents. | terra: They failed to hide because they assumed God did not know much of what they did; the ayah explicitly connects adverse bodily witness to underestimated divine knowledge.
- (41:39) [luna: strong; terra: strong; basis: scene+theme] وَمِنْ ءَايَٰتِهِۦٓ أَنَّكَ تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ ۚ إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ ۚ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The ground appears lifeless, then stirs and grows when rain reaches it; the verse applies that sign to the One who gives life to the dead. | terra: Humbled earth stirs and swells with rain, and its reviver is declared the reviver of the dead.
- (43:11) [luna: strong; terra: strong; basis: scene+theme] وَٱلَّذِى نَزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۢ بِقَدَرٍۢ فَأَنشَرْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ تُخْرَجُونَ
  Unverified discovery rationale: luna: The section joins rain and emergence from the earth; this verse says God sends water in measure, revives dead land, and “thus you will be brought forth” (كَذَٰلِكَ تُخْرَجُونَ). | terra: Measured water revives a dead land and كَذَٰلِكَ تُخْرَجُونَ directly applies that emergence to the hearers.
- (45:26) [terra: strong (missing-ayat turn); basis: scene+speaker] قُلِ ٱللَّهُ يُحْيِيكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يَجْمَعُكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
  Unverified discovery rationale: terra: God gives life, causes death, and then gathers people on resurrection day, stating the whole movement from life through burial to assembly.
- (47:37) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶51] إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ
  Unverified discovery rationale: luna: The section explicitly joins withheld wealth to what is extracted from within: if wealth were demanded, people would withhold it and God would bring out their grudges (وَيُخْرِجْ أَضْغَانَكُمْ). | terra: If their wealth were pressed from them they would become miserly and God would bring out أَضْغَانَكُمْ; property and concealed contents are extracted in one statement.
- (50:9) [luna: strong; terra: medium; basis: neighbour+scene] وَنَزَّلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ مُّبَٰرَكًۭا فَأَنۢبَتْنَا بِهِۦ جَنَّٰتٍۢ وَحَبَّ ٱلْحَصِيدِ
  Unverified discovery rationale: luna: The section’s rain scene has a close counterpart in blessed water sent down to produce gardens and grain for harvest (حَبَّ الْحَصِيدِ). | terra: Blessed rain produces gardens and grain, beginning the land-revival sequence that 50:11 explicitly calls human emergence.
- (50:10) [luna: strong; terra: medium; basis: neighbour+scene] وَٱلنَّخْلَ بَاسِقَٰتٍۢ لَّهَا طَلْعٌۭ نَّضِيدٌۭ
  Unverified discovery rationale: luna: This neighboring verse completes the rain-and-crop scene of 50:9 with tall date palms bearing clustered fruit, a visible product of the revived land. | terra: Tall palms with layered fruit continue the visible yield from rain before the sequence turns to resurrection.
- (50:11) [luna: strong; terra: strong; basis: scene+theme] رِّزْقًۭا لِّلْعِبَادِ ۖ وَأَحْيَيْنَا بِهِۦ بَلْدَةًۭ مَّيْتًۭا ۚ كَذَٰلِكَ ٱلْخُرُوجُ
  Unverified discovery rationale: luna: The section links rain-revived land to emergence from graves; this verse says God revives dead land and adds, “such is the emergence” (كَذَٰلِكَ الْخُرُوجُ). | terra: Rain provision revives dead land and كَذَٰلِكَ الْخُرُوجُ names human coming-out by the same pattern.
- (50:16) [luna: strong; terra: medium; basis: scene+speaker+theme] وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ
  Unverified discovery rationale: luna: The section ends with the Lord fully knowing people; this verse says God knows the soul’s whisper and is nearer than its jugular vein. | terra: God knows what the self whispers and is nearer than the jugular vein, intensifying the section's final movement into the unseen interior.
- (50:21) [terra: strong (missing-ayat turn); basis: scene+theme] وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ
  Unverified discovery rationale: terra: Every soul comes with a driver and a witness, turning movement to judgment into escorted, adverse testimony.
- (50:44) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶49] يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًۭا ۚ ذَٰلِكَ حَشْرٌ عَلَيْنَا يَسِيرٌۭ
  Unverified discovery rationale: luna: The section says the buried will emerge and hurry to the gathering; this verse has earth split open as people rush out, “that is an easy gathering” (حَشْرٌ عَلَيْنَا يَسِيرٌ). | terra: The earth splits from them as they emerge سِرَاعًا, directly joining cracked grave-earth, speed, and the final gathering.
- (54:7) [luna: strong; terra: strong; basis: scene+theme] خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ
  Unverified discovery rationale: luna: The section depicts dead people emerging and running; here humbled eyes watch people come from graves like scattered locusts (كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ). | terra: They emerge from graves like scattered locusts, turning hidden bodies into a visible moving multitude.
- (54:8) [luna: strong; terra: strong; basis: neighbour+scene] مُّهْطِعِينَ إِلَى ٱلدَّاعِ ۖ يَقُولُ ٱلْكَٰفِرُونَ هَٰذَا يَوْمٌ عَسِرٌۭ
  Unverified discovery rationale: luna: This verse completes the grave-emergence in 54:7: the people hurry toward the caller and say this is a difficult day. | terra: مُهْطِعِينَ إِلَى الدَّاعِ gives the grave-emergers of 54:7 their urgent directed movement toward the caller.
- (55:12) [luna: strong; basis: root+scene] وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ
  Unverified discovery rationale: luna: The section’s dictionary gloss connects حبّ as love with حبّ as grain; this verse names grain with husks, making that secondary sense concrete in a provision scene.
- (56:49) [terra: strong; basis: neighbour+scene] قُلْ إِنَّ ٱلْأَوَّلِينَ وَٱلْءَاخِرِينَ
  Unverified discovery rationale: terra: Both the former and latter peoples are named before the next ayah gathers them to a fixed time.
- (56:50) [terra: strong; basis: scene+theme] لَمَجْمُوعُونَ إِلَىٰ مِيقَٰتِ يَوْمٍۢ مَّعْلُومٍۢ
  Unverified discovery rationale: terra: لَمَجْمُوعُونَ إِلَىٰ مِيقَاتِ يَوْمٍ مَعْلُومٍ states the final universal gathering toward which the image runs.
- (56:63) [luna: strong; basis: scene+theme] أَفَرَءَيْتُم مَّا تَحْرُثُونَ
  Unverified discovery rationale: luna: The section’s love word has a source-section dictionary double sense, حبّ as love and حبّ as grain; this verse begins a crop sequence by asking about what people sow.
- (56:64) [luna: strong; basis: scene+theme] ءَأَنتُمْ تَزْرَعُونَهُۥٓ أَمْ نَحْنُ ٱلزَّٰرِعُونَ
  Unverified discovery rationale: luna: The crop sequence asks whether people or God make the sown grain grow, connecting the source section’s “grain in the heart” gloss to what is grown and gathered.
- (56:65) [luna: strong; basis: contrast+scene] لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا فَظَلْتُمْ تَفَكَّهُونَ
  Unverified discovery rationale: luna: This verse warns that God could make the crop dry debris, reversing the expected harvest just as the section’s garden owners lose their crop.
- (56:66) [luna: strong; basis: neighbour+scene] إِنَّا لَمُغْرَمُونَ
  Unverified discovery rationale: luna: After 56:65’s possible crop failure, people would lament that they had become debt-burdened; this completes the harvest reversal.
- (56:67) [luna: strong; basis: neighbour+scene] بَلْ نَحْنُ مَحْرُومُونَ
  Unverified discovery rationale: luna: This verse completes the crop-loss sequence of 56:65–66 by saying they would be left deprived.
- (56:71) [luna: strong; terra: strong; basis: root+scene+speaker] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
  Unverified discovery rationale: luna: The section describes fire struck out by the horses; this verse asks about the fire people kindle (النَّارَ الَّتِي تُورُونَ), using the source section’s fire-making root in the same sense. | terra: أَفَرَأَيْتُمُ النَّارَ الَّتِي تُورُونَ asks resurrection deniers about the very act of striking forth latent fire developed in the section.
- (56:72) [luna: strong; terra: strong; basis: neighbour+scene+theme] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
  Unverified discovery rationale: luna: This neighboring question completes 56:71 by asking who made the tree from which the kindled fire comes, extending the section’s hidden-source image. | terra: The question whether humans produced the fire's tree or God did makes the hidden flame in wood evidence of divine re-creation.
- (56:73) [luna: strong; terra: strong (missing-ayat turn); basis: scene+theme] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
  Unverified discovery rationale: luna: The section treats fire as a sign; this verse calls the fire a reminder and a provision for travelers (تَذْكِرَةً وَمَتَاعًا لِّلْمُقْوِينَ). | terra: God says He made the kindled fire a reminder, confirming the section's reading of brought-forth fire as an admonitory sign rather than a stray detail.
- (57:4) [terra: strong (missing-ayat turn); basis: scene+theme] هُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۖ وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: terra: God knows what enters earth and what comes out of it, as well as all descending and ascending, directly framing hidden burial and emergence within divine sight.
- (57:17) [luna: strong; terra: medium; basis: scene+speaker+theme] ٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَعْقِلُونَ
  Unverified discovery rationale: luna: This verse directly says God gives life to earth after its death, the land-side counterpart to the section’s people brought out of graves. | terra: اعْلَمُوا أَنَّ اللَّهَ يُحْيِي الْأَرْضَ بَعْدَ مَوْتِهَا makes revived ground an explicit admonition to know and understand.
- (57:20) [luna: strong; terra: medium; basis: contrast+scene+theme] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: luna: The section follows rain, crops, and attachment to wealth; this verse joins rain-grown vegetation that withers to rivalry in wealth and children and the fading of worldly life. | terra: Worldly rivalry in wealth is compared to rain-grown vegetation that yellows and becomes debris, joining property, soil, and passing yield.
- (58:6) [terra: strong; basis: scene+theme] يَوْمَ يَبْعَثُهُمُ ٱللَّهُ جَمِيعًۭا فَيُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
  Unverified discovery rationale: terra: God raises them all, tells them their forgotten deeds, and is witness over everything; resurrection, inwardly complete reckoning, and witness form one sequence.
- (59:9) [luna: strong; terra: contrast; basis: contrast+scene+theme] وَٱلَّذِينَ تَبَوَّءُو ٱلدَّارَ وَٱلْإِيمَٰنَ مِن قَبْلِهِمْ يُحِبُّونَ مَنْ هَاجَرَ إِلَيْهِمْ وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةًۭ مِّمَّآ أُوتُوا۟ وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
  Unverified discovery rationale: luna: The section’s miser clings to wealth and leaves the needy outside; these helpers prefer others over themselves despite poverty and feel no want in their breasts over what others receive. | terra: They prefer others despite their own need and are guarded from the soul's stinginess, the direct ethical opposite of the garden owners' closed hand.
- (59:10) [luna: strong; basis: neighbour+theme] وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ
  Unverified discovery rationale: luna: This neighboring prayer asks God to remove rancor from believers’ hearts (غِلًّا فِي قُلُوبِنَا), completing 59:9’s image of generosity without resentment.
- (64:4) [luna: strong; terra: medium; basis: speaker+theme] يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ ۚ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section ends with the Lord knowing people; this verse explicitly says God knows what is in the breasts as well as what is concealed and declared. | terra: God knows what people conceal and reveal and is عَلِيمٌ بِذَاتِ الصُّدُورِ, specifying the invisible endpoint of the section's movement inward.
- (64:15) [luna: strong; basis: theme] إِنَّمَآ أَمْوَٰلُكُمْ وَأَوْلَٰدُكُمْ فِتْنَةٌۭ ۚ وَٱللَّهُ عِندَهُۥٓ أَجْرٌ عَظِيمٌۭ
  Unverified discovery rationale: luna: This verse calls wealth and children a trial, matching the section’s claim that attachment to wealth exposes what lies within.
- (64:16) [luna: strong; terra: contrast (missing-ayat turn); basis: contrast+theme] فَٱتَّقُوا۟ ٱللَّهَ مَا ٱسْتَطَعْتُمْ وَٱسْمَعُوا۟ وَأَطِيعُوا۟ وَأَنفِقُوا۟ خَيْرًۭا لِّأَنفُسِكُمْ ۗ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
  Unverified discovery rationale: luna: The section shows wealth held tightly; this verse says those saved from the stinginess of their own souls are successful (شُحَّ نَفْسِهِ), describing the opposite inward disposition. | terra: The command to spend is followed by success for whoever is protected from the soul's stinginess, the direct opposite of the closed hand.
- (67:13) [luna: strong; terra: medium; basis: speaker+theme] وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section moves from audible signs to what is hidden in chests; this verse says God knows what people conceal in their breasts and what they speak aloud. | terra: Secret or public speech is alike known by the One who knows what breasts contain, setting a boundary around attempted concealment.
- (67:24) [terra: strong (missing-ayat turn); basis: scene+theme] قُلْ هُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
  Unverified discovery rationale: terra: The One who spread humanity through earth is the One to whom they will be gathered, pairing present terrestrial scattering with future assembly.
- (68:17) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶52] إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ
  Unverified discovery rationale: luna: The section links a morning raid to the garden owners’ harvest plan; they swear to cut its crop in the morning (مُصْبِحِينَ). | terra: The garden owners swear to cut its crop مُصْبِحِينَ, beginning the exact dawn expedition in which withholding resembles a raid.
- (68:19) [luna: strong; terra: strong; basis: contrast+scene] [cited in ¶52] فَطَافَ عَلَيْهَا طَآئِفٌۭ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ
  Unverified discovery rationale: luna: The section says the garden owners become the raided; while they sleep, a calamity from their Lord circles the garden (فَطَافَ عَلَيْهَا طَآئِفٌ). | terra: A visitation from their Lord circles the garden while they sleep, turning the intended dawn takers into people overtaken before dawn.
- (68:20) [luna: strong; terra: strong; basis: contrast+scene] [cited in ¶52] فَأَصْبَحَتْ كَٱلصَّرِيمِ
  Unverified discovery rationale: luna: Their expected harvest is reversed when the garden enters morning blackened like a cut-down field (كَالصَّرِيمِ), making the section’s barren-land image concrete. | terra: By morning the garden is كَالصَّرِيمِ, so the scene's expected harvest has already been cut off by the Lord's answering stroke.
- (68:21) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶52] فَتَنَادَوْا۟ مُصْبِحِينَ
  Unverified discovery rationale: luna: As in the section’s dawn scene, the owners call one another in the morning (مُصْبِحِينَ), unaware of what happened overnight. | terra: They call one another مُصْبِحِينَ, preserving the section's tightly linked sequence of morning, collective movement, and intended seizure.
- (68:22) [luna: strong; terra: medium; basis: neighbour+scene] أَنِ ٱغْدُوا۟ عَلَىٰ حَرْثِكُمْ إِن كُنتُمْ صَٰرِمِينَ
  Unverified discovery rationale: luna: This neighboring verse completes 68:21’s morning call: they urge one another to go early to the crop if they mean to harvest it. | terra: Their command to go early to the crop continues the purposeful dawn advance begun in 68:17.
- (68:24) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶52] أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ
  Unverified discovery rationale: luna: The section’s withheld wealth and the garden’s refusal of the needy meet in their plan that no poor person enter that day (مِسْكِينٌ). | terra: Their whispered order that no poor person enter the garden gives the dawn party its clenched-hand purpose.
- (68:25) [luna: strong; terra: medium; basis: scene+theme] وَغَدَوْا۟ عَلَىٰ حَرْدٍۢ قَٰدِرِينَ
  Unverified discovery rationale: luna: The owners proceed with a settled intention to keep the needy out; this gives the section’s closed hand a specific human scene. | terra: They go early عَلَىٰ حَرْدٍ while thinking themselves able, giving the withholding dawn party the hard intent and confidence of an assault.
- (68:26) [luna: strong; terra: medium; basis: contrast+scene] فَلَمَّا رَأَوْهَا قَالُوٓا۟ إِنَّا لَضَآلُّونَ
  Unverified discovery rationale: luna: The harvesters who expected to collect a crop instead find the garden ruined and recognize they have lost their way; the planned morning raid turns against them. | terra: On seeing the struck garden they think they have lost the way, the first recognition that the intended raiders have themselves been pre-empted.
- (68:27) [luna: strong; terra: medium; basis: contrast+scene] بَلْ نَحْنُ مَحْرُومُونَ
  Unverified discovery rationale: luna: Their recognition is confirmed: “rather, we have been deprived” (بَلْ نَحْنُ مَحْرُومُونَ), the reversal of planned gain. | terra: They recognize that they are deprived, making their planned deprivation of the poor rebound upon them.
- (68:28) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+root+scene+speaker] قَالَ أَوْسَطُهُمْ أَلَمْ أَقُل لَّكُمْ لَوْلَا تُسَبِّحُونَ
  Unverified discovery rationale: luna: The section’s verse 5 uses the source form waṣaṭna for entering the middle of a gathering; here awsaṭuhum means the most balanced one among the garden owners, who warns them from within their group. | terra: أَوْسَطُهُمْ, the soundest or most balanced among the garden owners, asks why they did not glorify God; the w-s-ṭ wording places a moral witness in the middle of the dawn party.
- (69:18) [luna: strong; terra: strong; basis: scene+theme] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
  Unverified discovery rationale: luna: The section’s hidden chest contents are exposed on the final day; this verse says that day people will be displayed and no secret will remain hidden (خَافِيَةٌ). | terra: At the presentation لَا تَخْفَىٰ مِنْكُمْ خَافِيَةٌ; inward concealment ends when humanity is brought before its Lord.
- (70:15) [terra: strong; basis: neighbour+scene] كَلَّآ ۖ إِنَّهَا لَظَىٰ
  Unverified discovery rationale: terra: The blaze لَظَى begins the punishment whose own next clauses call the one who turns away and gathers wealth.
- (70:17) [terra: strong; basis: neighbour+scene] تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ
  Unverified discovery rationale: terra: The fire calls whoever أَدْبَرَ وَتَوَلَّى, identifying the human stance that culminates in hoarding in 70:18.
- (70:18) [terra: strong; basis: scene+theme] وَجَمَعَ فَأَوْعَىٰٓ
  Unverified discovery rationale: terra: وَجَمَعَ فَأَوْعَىٰ compresses collecting and closing away wealth, exactly the section's gathered treasure and clenched hand.
- (70:21) [luna: strong (missing-ayat turn); basis: theme] وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا
  Unverified discovery rationale: luna: The section describes the human who clings to wealth; this verse says that when good reaches a person, he withholds (مَنُوعًا), a direct formulation of that response to provision.
- (70:43) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶49] يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ
  Unverified discovery rationale: luna: The section quotes this direct parallel: people come swiftly out of graves, hurrying as if toward a standing target (يُوفِضُونَ). | terra: People come out of the graves سِرَاعًا and hurry toward a نصب; this is the section's explicit meeting of the running horses with running resurrected humans.
- (71:17) [terra: strong (missing-ayat turn); basis: scene+theme] وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا
  Unverified discovery rationale: terra: God caused humanity to grow from the earth like vegetation, tightening the section's analogy between a field's yield and human bodies.
- (71:18) [terra: strong (missing-ayat turn); basis: scene+theme] ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًۭا
  Unverified discovery rationale: terra: God returns people into earth and will bring them out with a true bringing-out, directly joining burial to final emergence.
- (75:3) [terra: strong (missing-ayat turn); basis: root+scene] أَيَحْسَبُ ٱلْإِنسَٰنُ أَلَّن نَّجْمَعَ عِظَامَهُۥ
  Unverified discovery rationale: terra: The human asks whether God will gather his bones; جَمْع simultaneously names bodily reassembly and the final gathering developed in the section.
- (75:14) [luna: strong; terra: strong; basis: scene+speaker+theme] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
  Unverified discovery rationale: luna: The section says a person is witness against himself; this verse states that the human being is evidence against himself (عَلَىٰ نَفْسِهِ بَصِيرَةٌ). | terra: بَلِ الْإِنْسَانُ عَلَىٰ نَفْسِهِ بَصِيرَةٌ makes the human being evidence against himself, matching the adverse self-witness reading of 100:7.
- (75:15) [luna: strong; terra: medium (missing-ayat turn); basis: neighbour+speaker+theme] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
  Unverified discovery rationale: luna: This verse completes 75:14 by saying excuses will not remove that self-evidence, reinforcing the section’s unanswerable witness. | terra: Even when a person presents excuses, the self-insight of 75:14 remains, clarifying why self-witness cannot be evaded.
- (77:32) [luna: strong; basis: contrast+scene] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
  Unverified discovery rationale: luna: The section’s sparks are small flashes from hooves striking stone; this verse reverses their scale with Hellfire sparks like huge structures.
- (77:33) [luna: strong; basis: neighbour+scene] كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ
  Unverified discovery rationale: luna: This verse completes the sparks in 77:32 by likening them to yellow camels, extending the contrast between sparks of a charge and punishment’s fire.
- (77:38) [terra: strong; basis: scene+speaker] هَٰذَا يَوْمُ ٱلْفَصْلِ ۖ جَمَعْنَٰكُمْ وَٱلْأَوَّلِينَ
  Unverified discovery rationale: terra: هَٰذَا يَوْمُ الْفَصْلِ جَمَعْنَاكُمْ وَالْأَوَّلِينَ names the assembled crowd as the gathering for decisive separation.
- (79:10) [luna: strong; basis: scene] يَقُولُونَ أَءِنَّا لَمَرْدُودُونَ فِى ٱلْحَافِرَةِ
  Unverified discovery rationale: luna: The section makes grave emergence a real event; here the deniers ask whether they will be returned to their former state.
- (79:11) [luna: strong; basis: neighbour+scene] أَءِذَا كُنَّا عِظَٰمًۭا نَّخِرَةًۭ
  Unverified discovery rationale: luna: They sharpen the objection in 79:10 by asking whether they will return after becoming decayed bones.
- (79:12) [luna: strong; basis: neighbour+scene] قَالُوا۟ تِلْكَ إِذًۭا كَرَّةٌ خَاسِرَةٌۭ
  Unverified discovery rationale: luna: This neighboring verse records their dismissive response that such a return would be a ruinous return.
- (79:13) [luna: strong; terra: medium; basis: neighbour+scene+theme] فَإِنَّمَا هِىَ زَجْرَةٌۭ وَٰحِدَةٌۭ
  Unverified discovery rationale: luna: The section’s hidden dead are brought out by a decisive upheaval; here resurrection follows one overwhelming blast (زَجْرَةٌ وَاحِدَةٌ). | terra: A single rebuking blast precedes humanity's sudden appearance on the surface in 79:14, compressing the opening of the final scene into one sound.
- (79:14) [luna: strong; terra: strong; basis: neighbour+scene] فَإِذَا هُم بِٱلسَّاهِرَةِ
  Unverified discovery rationale: luna: This verse completes the blast in 79:13: suddenly they are on the surface of the earth. | terra: After a single blast, everyone is suddenly بِالسَّاهِرَةِ on the exposed surface, the endpoint of emergence from below ground.
- (81:18) [terra: strong (missing-ayat turn); basis: scene+theme] وَٱلصُّبْحِ إِذَا تَنَفَّسَ
  Unverified discovery rationale: terra: وَالصُّبْحِ إِذَا تَنَفَّسَ makes dawn itself breathe, joining the opening horse's breath to the morning light in a single Quranic image.
- (82:4) [luna: strong; terra: strong; basis: root+scene] وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ
  Unverified discovery rationale: luna: The section’s graves being overturned is repeated in the same verb: “when the graves are scattered/opened” (بُعْثِرَتْ). | terra: وَإِذَا الْقُبُورُ بُعْثِرَتْ repeats the section's exact grave-overturning verb, making the raised dust of the opening a rehearsal for opened graves.
- (82:5) [luna: strong; terra: medium; basis: neighbour+scene+theme] عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ
  Unverified discovery rationale: luna: After 82:4’s graves are overturned, this verse says every soul will know what it sent ahead and left behind, completing the section’s emergence-and-accounting sequence. | terra: After the graves are overturned, each soul knows what it advanced and delayed; exposed earth is followed by exposed moral record.
- (83:4) [terra: strong (missing-ayat turn); basis: speaker+theme] أَلَا يَظُنُّ أُو۟لَٰٓئِكَ أَنَّهُم مَّبْعُوثُونَ
  Unverified discovery rationale: terra: أَلَا يَظُنُّ أُولَٰئِكَ أَنَّهُمْ مَبْعُوثُونَ confronts exploiters with a rhetorical question about being raised, closely matching the section's unanswered appeal to knowledge.
- (83:6) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: People stand before the Lord of all worlds on that tremendous day, identifying the destination of the grave-emerging crowd.
- (84:4) [luna: strong; terra: medium; basis: scene+theme] وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ
  Unverified discovery rationale: luna: The section pictures what lies in graves being brought out; this verse says the earth throws out what is inside it and empties itself (أَلْقَتْ مَا فِيهَا). | terra: The earth casts out what is within it and empties, a direct parallel to ground yielding all its buried contents.
- (84:5) [luna: strong; basis: neighbour+scene] وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ
  Unverified discovery rationale: luna: After the earth empties its contents in 84:4, it listens and responds to its Lord, extending the section’s image of earth opened by divine command.
- (86:9) [luna: strong; terra: strong; basis: scene+theme] يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
  Unverified discovery rationale: luna: The section says what lies in the chest is gathered and exposed; this verse names the Day when hidden secrets are examined and disclosed (تُبْلَى السَّرَائِرُ). | terra: يَوْمَ تُبْلَى السَّرَائِرُ makes the judgment day an assay of concealed things, the direct thematic counterpart of sorting what breasts contain.
- (89:17) [luna: strong; basis: contrast+theme] كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
  Unverified discovery rationale: luna: The section depicts hoarded wealth and a needy person excluded; this verse rebukes people for failing to honor the orphan.
- (89:18) [luna: strong; basis: contrast+theme] وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
  Unverified discovery rationale: luna: The section’s garden owners bar a poor person; this verse rebukes them for not urging one another to feed the poor (الْمِسْكِينِ).
- (89:19) [luna: strong; terra: strong; basis: scene+theme] وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
  Unverified discovery rationale: luna: The section’s fixation on collected goods meets this verse’s greedy consumption of inheritance (أَكْلًا لَّمًّا). | terra: وَتَأْكُلُونَ التُّرَاثَ أَكْلًا لَمًّا portrays all-consuming acquisition, a direct form of the kenūd person's solitary, withholding appetite.
- (89:20) [luna: strong; terra: strong; basis: root+theme] وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
  Unverified discovery rationale: luna: The section’s attachment to wealth is stated with the same love-root: people “love wealth with immense love” (تُحِبُّونَ الْمَالَ حُبًّا جَمًّا). | terra: وَتُحِبُّونَ الْمَالَ حُبًّا جَمًّا is the Quran's closest explicit restatement of intense love of wealth.
- (89:21) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
  Unverified discovery rationale: luna: After 89:20’s immense love of wealth, this verse turns to the earth pounded flat, a specific final-day counterpart to the section’s soil lifted and graves overturned. | terra: Immediately after the love of wealth, the earth is pounded دَكًّا دَكًّا, joining attachment to property with the final upheaval of ground.
- (92:8) [luna: strong; terra: medium; basis: contrast+theme] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
  Unverified discovery rationale: luna: The section’s tightly held wealth meets this passage’s miser who considers himself self-sufficient (اسْتَغْنَىٰ). | terra: The one who بَخِلَ وَاسْتَغْنَىٰ embodies the self-sufficient miserliness developed through the kenūd and garden-owner images.
- (92:9) [luna: strong; basis: contrast+theme] وَكَذَّبَ بِٱلْحُسْنَىٰ
  Unverified discovery rationale: luna: This verse says the miser denies the best, specifying the inward refusal behind the section’s closed hand.
- (92:10) [luna: strong; basis: contrast+scene] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
  Unverified discovery rationale: luna: The miser is eased toward hardship here, the contrary outcome to the section’s hoped-for gain from hoarding.
- (92:11) [luna: strong; terra: medium; basis: contrast+neighbour+theme] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
  Unverified discovery rationale: luna: This verse says wealth will not avail its owner when he falls, directly opposing the section’s wealth-attachment before the grave and gathering. | terra: وَمَا يُغْنِي عَنْهُ مَالُهُ إِذَا تَرَدَّىٰ carries the miser of 92:8 to the point where amassed wealth cannot save him.
- (99:1) [luna: strong; terra: strong; basis: neighbour+scene] إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
  Unverified discovery rationale: luna: The section’s ground and graves are overturned on the final day; this surah opens with the earth violently shaken. | terra: The earth's final shaking begins the sequence whose burdens emerge and whose people issue in groups in 99:2 and 99:6.
- (99:2) [luna: strong; terra: strong; basis: scene+theme] وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
  Unverified discovery rationale: luna: This neighboring verse specifies the shaking’s result: the earth throws out its burdens (أَثْقَالَهَا), matching the section’s buried contents brought out. | terra: وَأَخْرَجَتِ الْأَرْضُ أَثْقَالَهَا depicts earth casting out what it carried, the clearest parallel to overturned graves yielding their hidden occupants.
- (99:4) [luna: strong; terra: strong; basis: scene+theme] يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
  Unverified discovery rationale: luna: The section moves from soil to what it conceals; here the earth reports its news on that day, making the ground an active witness. | terra: The earth tells its reports, making the previously trodden ground itself a witness when it opens.
- (99:5) [luna: strong; terra: strong; basis: neighbour+scene+speaker+theme] بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
  Unverified discovery rationale: luna: This verse completes the earth’s report in 99:4 by saying its Lord inspires it to do so. | terra: The earth reports بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا, locating the opened ground's testimony under the command of the same knowing Lord.
- (99:6) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶53] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
  Unverified discovery rationale: luna: The section cites this verse: people emerge in groups to see their deeds. Its verb يَصْدُرُ is also the source section’s dictionary link to “returning from water” and shares the root of its word for chests (الصُّدُور). | terra: يَصْدُرُ النَّاسُ أَشْتَاتًا depicts people issuing in groups as flocks leave water; it joins the watering-place sense of ṣ-d-r to breasts, emergence, and the sight of deeds.
- (99:7) [luna: strong; terra: strong; basis: root+theme] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
  Unverified discovery rationale: luna: The section ends with inner contents known by God; here each person sees even an atom’s weight of good that they did. | terra: After issuing from the earth, a person sees an atom's weight of خَيْرًا; khayr has become a witnessed deed rather than the property intensely loved in 100:8.
- (99:8) [luna: strong; terra: strong; basis: contrast+scene+theme] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
  Unverified discovery rationale: luna: The paired verse sets the boundary for the section’s accounting: even an atom’s weight of evil is seen, alongside 99:7’s good. | terra: The smallest evil is likewise seen, completing the move from opened earth to exact disclosure of what each person had done.
- (102:1) [luna: strong; terra: strong; basis: root+scene+theme] أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
  Unverified discovery rationale: luna: The section links gathering with attachment to wealth; this verse says rivalry in increase distracts people (أَلْهَاكُمُ التَّكَاثُرُ), setting up the graves that follow. | terra: أَلْهَاكُمُ التَّكَاثُرُ names acquisitive accumulation as the force carrying people toward the grave scene.
- (102:2) [luna: strong; terra: strong; basis: neighbour+scene+theme] حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ
  Unverified discovery rationale: luna: This verse completes 102:1’s rivalry in accumulation: it lasts until people visit the graves, joining wealth competition to the section’s burial scene. | terra: حَتَّىٰ زُرْتُمُ الْمَقَابِرَ places competitive accumulation and graves in the same movement, matching the section's wealth-to-grave turn.
- (102:3) [terra: strong; basis: speaker+theme] كَلَّا سَوْفَ تَعْلَمُونَ
  Unverified discovery rationale: terra: كَلَّا سَوْفَ تَعْلَمُونَ answers heedless accumulation with coming knowledge, as the section asks whether the wealth-lover knows what grave-opening entails.
- (102:5) [terra: strong; basis: speaker+theme] كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
  Unverified discovery rationale: terra: لَوْ تَعْلَمُونَ عِلْمَ الْيَقِينِ intensifies the section's movement from unanswered human knowledge to certainty at judgment.
- (102:6) [terra: strong; basis: neighbour+scene] لَتَرَوُنَّ ٱلْجَحِيمَ
  Unverified discovery rationale: terra: لَتَرَوُنَّ الْجَحِيمَ brings the accumulating grave-visitor of 102:1-2 to visible fire.
- (102:8) [luna: strong; terra: strong; basis: neighbour+speaker+theme] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ
  Unverified discovery rationale: luna: After 102:1–2’s wealth rivalry and graves, this closing verse says people will be questioned about their blessings, completing the section’s reckoning of what was loved and held. | terra: The grave-visitors are questioned that day about نعيم, turning enjoyed goods into disclosed accountability.
- (104:2) [luna: strong; terra: strong; basis: root+scene+theme] ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
  Unverified discovery rationale: luna: The section links gathering to wealth and the final gathering; this verse uses the same gather-root for one who collects wealth (جَمَعَ مَالًا) and counts it. | terra: الَّذِي جَمَعَ مَالًا وَعَدَّدَهُ names the wealth-gatherer whose collection the section sets against the final gathering and sorting.
- (104:3) [luna: strong; basis: contrast+theme] يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
  Unverified discovery rationale: luna: The section’s hoarder trusts his stored wealth; this verse exposes the false belief that wealth makes its owner immortal.
- (104:4) [luna: strong; terra: strong; basis: neighbour+scene+theme] كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
  Unverified discovery rationale: luna: The section brings hoarded riches to fire; this verse says the wealth-counter will be thrown into the Crusher (الْحُطَمَةِ). | terra: The wealth-counter of 104:2 is thrown into the Crusher, carrying accumulated property directly into the fire sequence completed in 104:6-7.
- (104:6) [terra: strong; basis: neighbour+scene] نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
  Unverified discovery rationale: terra: نَارُ اللَّهِ الْمُوقَدَةُ supplies the divine fire that answers the wealth-gatherer named in 104:2.
- (104:7) [terra: strong; basis: scene+theme] ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
  Unverified discovery rationale: terra: The fire rises over الْأَفْئِدَةِ, joining punishment for amassed wealth to the inward heart exposed in the section.
- (107:1) [luna: strong; basis: contrast+theme] أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
  Unverified discovery rationale: luna: The section pairs ingratitude with neglect of the needy; this verse identifies denial of judgment through the treatment of the orphan.
- (107:2) [luna: strong; terra: medium (missing-ayat turn); basis: contrast+theme] فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
  Unverified discovery rationale: luna: The denier’s response to the orphan here gives a specific human counterpart to the section’s account of miserliness. | terra: Repulsing the orphan gives concrete social action to the kenūd person's refusal to share what he holds.
- (107:3) [luna: strong; terra: medium (missing-ayat turn); basis: theme] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
  Unverified discovery rationale: luna: This verse condemns failure to urge feeding the poor, the same social cost enacted when the section’s garden owners bar the needy. | terra: Failure to urge feeding the poor directly parallels the garden owners' plan to exclude a needy person.
- (107:7) [luna: strong; terra: medium (missing-ayat turn); basis: theme] وَيَمْنَعُونَ ٱلْمَاعُونَ
  Unverified discovery rationale: luna: The passage ends with withholding even small assistance (الْمَاعُونَ), a specific form of the closed hand in the section. | terra: Withholding ordinary aid distills the closed-hand image into a small, observable refusal.

## medium (89)

- (2:77) [terra: medium; basis: speaker+theme] أَوَلَا يَعْلَمُونَ أَنَّ ٱللَّهَ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ
  Unverified discovery rationale: terra: أَوَلَا يَعْلَمُونَ asks whether people know that God knows what they conceal and announce, closely matching the section's rhetorical question and hidden interior.
- (2:164) [luna: medium; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The section moves from rain and land to life emerging; this verse lists rain reviving the earth after its death among signs for people who reason.
- (2:180) [luna: medium; basis: root+theme] كُتِبَ عَلَيْكُمْ إِذَا حَضَرَ أَحَدَكُمُ ٱلْمَوْتُ إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ لِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ بِٱلْمَعْرُوفِ ۖ حَقًّا عَلَى ٱلْمُتَّقِينَ
  Unverified discovery rationale: luna: The section’s word khayr carries its source-section dictionary sense of wealth; this verse uses “good” for wealth in its bequest command, linking property to what is left behind.
- (2:259) [terra: medium (missing-ayat turn); basis: scene+theme] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: A doubter is shown bones being raised and clothed with flesh, an explicit bodily demonstration of how the dead are brought out again.
- (2:262) [luna: medium (missing-ayat turn); basis: neighbour+theme] ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى ۙ لَّهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: luna: After 2:261’s grain-and-spending parable, this verse describes spenders who do not follow their gifts with reminders or injury; it specifies the inward and social quality of giving that opposes the section’s closed hand.
- (2:263) [luna: medium (missing-ayat turn); basis: neighbour+theme] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
  Unverified discovery rationale: luna: This neighboring verse says a good word and forgiveness are better than charity followed by injury, adding the treatment of the needy to the section’s account of withheld wealth.
- (3:9) [terra: medium; basis: scene+speaker] رَبَّنَآ إِنَّكَ جَامِعُ ٱلنَّاسِ لِيَوْمٍۢ لَّا رَيْبَ فِيهِ ۚ إِنَّ ٱللَّهَ لَا يُخْلِفُ ٱلْمِيعَادَ
  Unverified discovery rationale: terra: The prayer addresses God as the One who gathers all people for a day without doubt, the universal destination implicit in the section's central crowd.
- (3:10) [terra: medium; basis: scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ
  Unverified discovery rationale: terra: Wealth and children do not avail against God and their owners become fuel for the Fire, another precise wealth-to-fire conjunction.
- (3:141) [terra: medium (missing-ayat turn); basis: theme] وَلِيُمَحِّصَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَيَمْحَقَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: God assays the believers and effaces the disbelievers, preserving the refining sense behind the section's image of separating precious substance from residue.
- (3:179) [terra: medium; basis: theme] مَّا كَانَ ٱللَّهُ لِيَذَرَ ٱلْمُؤْمِنِينَ عَلَىٰ مَآ أَنتُمْ عَلَيْهِ حَتَّىٰ يَمِيزَ ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ ۗ وَمَا كَانَ ٱللَّهُ لِيُطْلِعَكُمْ عَلَى ٱلْغَيْبِ وَلَٰكِنَّ ٱللَّهَ يَجْتَبِى مِن رُّسُلِهِۦ مَن يَشَآءُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرُسُلِهِۦ ۚ وَإِن تُؤْمِنُوا۟ وَتَتَّقُوا۟ فَلَكُمْ أَجْرٌ عَظِيمٌۭ
  Unverified discovery rationale: terra: God does not leave the mixed community as it is until He distinguishes the foul from the good, a social counterpart to the section's assay and separation.
- (4:10) [terra: medium; basis: scene+theme] إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا
  Unverified discovery rationale: terra: Those who consume orphans' wealth unjustly consume fire into their bellies, making wrongful acquisition already an inward fire.
- (4:37) [terra: medium (missing-ayat turn); basis: theme] ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ وَيَكْتُمُونَ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۗ وَأَعْتَدْنَا لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
  Unverified discovery rationale: terra: The miserly both command miserliness and conceal what God gave from His bounty, joining withheld property with concealment.
- (4:87) [terra: medium; basis: scene+speaker] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۗ وَمَنْ أَصْدَقُ مِنَ ٱللَّهِ حَدِيثًۭا
  Unverified discovery rationale: terra: God promises لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ الْقِيَامَةِ, turning gathering into the Lord's direct, certain act.
- (5:7) [terra: medium (missing-ayat turn); basis: speaker+theme] وَٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ وَمِيثَٰقَهُ ٱلَّذِى وَاثَقَكُم بِهِۦٓ إِذْ قُلْتُمْ سَمِعْنَا وَأَطَعْنَا ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: The remembered covenant includes “we hear and obey,” followed by the assertion that God knows what breasts contain; pledged witness and inward knowledge meet.
- (6:59) [luna: medium; terra: medium; basis: scene+theme] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: The section’s ending entrusts hidden contents to the Lord’s knowledge; this verse says no leaf falls, and no grain lies in earth’s darkness, without God knowing it. | terra: God knows a grain in the darknesses of earth as well as every falling leaf, joining the hidden inner “grain,” buried earth, and exhaustive knowledge.
- (6:141) [luna: medium; basis: scene+theme] ۞ وَهُوَ ٱلَّذِىٓ أَنشَأَ جَنَّٰتٍۢ مَّعْرُوشَٰتٍۢ وَغَيْرَ مَعْرُوشَٰتٍۢ وَٱلنَّخْلَ وَٱلزَّرْعَ مُخْتَلِفًا أُكُلُهُۥ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُتَشَٰبِهًۭا وَغَيْرَ مُتَشَٰبِهٍۢ ۚ كُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
  Unverified discovery rationale: luna: The section’s grain and harvest associations meet this command to eat from crops when they yield and give their due on harvest day (يَوْمَ حَصَادِهِ).
- (7:26) [terra: medium (missing-ayat turn); basis: contrast+root] يَٰبَنِىٓ ءَادَمَ قَدْ أَنزَلْنَا عَلَيْكُمْ لِبَاسًۭا يُوَٰرِى سَوْءَٰتِكُمْ وَرِيشًۭا ۖ وَلِبَاسُ ٱلتَّقْوَىٰ ذَٰلِكَ خَيْرٌۭ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ لَعَلَّهُمْ يَذَّكَّرُونَ
  Unverified discovery rationale: terra: Garments يُوَارِي nakedness, preserving the covering sense of w-r-y; it illuminates the reversal from covered body to disclosed body, though its immediate subject is clothing rather than burial.
- (7:97) [terra: medium; basis: contrast+scene] أَفَأَمِنَ أَهْلُ ٱلْقُرَىٰٓ أَن يَأْتِيَهُم بَأْسُنَا بَيَٰتًۭا وَهُمْ نَآئِمُونَ
  Unverified discovery rationale: terra: The townspeople are asked whether they feel safe from punishment coming بَيَاتًا while asleep, matching the garden owners' nocturnal reversal.
- (9:67) [terra: medium; basis: scene+theme] ٱلْمُنَٰفِقُونَ وَٱلْمُنَٰفِقَٰتُ بَعْضُهُم مِّنۢ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمُنكَرِ وَيَنْهَوْنَ عَنِ ٱلْمَعْرُوفِ وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ ۗ إِنَّ ٱلْمُنَٰفِقِينَ هُمُ ٱلْفَٰسِقُونَ
  Unverified discovery rationale: terra: The hypocrites يَقْبِضُونَ أَيْدِيَهُمْ and forget God, giving the closed hand a Quranic moral relation to ingratitude toward the Lord.
- (9:78) [terra: medium; basis: speaker+theme] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَعْلَمُ سِرَّهُمْ وَنَجْوَىٰهُمْ وَأَنَّ ٱللَّهَ عَلَّٰمُ ٱلْغُيُوبِ
  Unverified discovery rationale: terra: أَلَمْ يَعْلَمُوا asks whether they know that God knows their secret and private counsel, another exact rhetorical movement from human ignorance to divine knowledge.
- (11:9) [luna: medium (missing-ayat turn); basis: contrast+theme] وَلَئِنْ أَذَقْنَا ٱلْإِنسَٰنَ مِنَّا رَحْمَةًۭ ثُمَّ نَزَعْنَٰهَا مِنْهُ إِنَّهُۥ لَيَـُٔوسٌۭ كَفُورٌۭ
  Unverified discovery rationale: luna: The section calls the human ungrateful to his Lord; this verse gives a specific form of that ingratitude, despairing when mercy is withdrawn after being tasted.
- (11:81) [terra: medium; basis: scene+speaker] قَالُوا۟ يَٰلُوطُ إِنَّا رُسُلُ رَبِّكَ لَن يَصِلُوٓا۟ إِلَيْكَ ۖ فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ وَلَا يَلْتَفِتْ مِنكُمْ أَحَدٌ إِلَّا ٱمْرَأَتَكَ ۖ إِنَّهُۥ مُصِيبُهَا مَآ أَصَابَهُمْ ۚ إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍۢ
  Unverified discovery rationale: terra: Lot is told that his people's appointment is الصُّبْح and asked whether morning is near, tying dawn to an unavoidable divine strike.
- (12:47) [luna: medium (missing-ayat turn); basis: scene+theme] قَالَ تَزْرَعُونَ سَبْعَ سِنِينَ دَأَبًۭا فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ
  Unverified discovery rationale: luna: The section’s dictionary double sense of ḥubb as love and grain meets Joseph’s instruction to sow for seven years and keep most of the harvest in its ears; this is a concrete image of gathered grain kept within its husk.
- (15:66) [terra: medium; basis: scene+theme] وَقَضَيْنَآ إِلَيْهِ ذَٰلِكَ ٱلْأَمْرَ أَنَّ دَابِرَ هَٰٓؤُلَآءِ مَقْطُوعٌۭ مُّصْبِحِينَ
  Unverified discovery rationale: terra: The decree that the last of the people will be cut off مُصْبِحِينَ gives morning the same decisive movement from warning to destruction.
- (16:65) [terra: medium; basis: scene+theme] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
  Unverified discovery rationale: terra: Rain gives dead earth life and is a sign for those who listen, a nonlexical parallel to the grave-soil becoming productive again.
- (18:37) [luna: medium (missing-ayat turn); basis: scene+theme] قَالَ لَهُۥ صَاحِبُهُۥ وَهُوَ يُحَاوِرُهُۥٓ أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا
  Unverified discovery rationale: luna: In the garden-owner dialogue, the companion recalls that the owner was created from dust, then a drop, then made a man; that grounds the section’s garden-and-wealth scene in human origin and the return to God being debated nearby.
- (18:39) [luna: medium (missing-ayat turn); basis: scene+speaker] وَلَوْلَآ إِذْ دَخَلْتَ جَنَّتَكَ قُلْتَ مَا شَآءَ ٱللَّهُ لَا قُوَّةَ إِلَّا بِٱللَّهِ ۚ إِن تَرَنِ أَنَا۠ أَقَلَّ مِنكَ مَالًۭا وَوَلَدًۭا
  Unverified discovery rationale: luna: The companion tells the garden owner that, on entering his garden, he should acknowledge God’s will and power; this makes the garden’s yield provision from the Lord, not the owner’s own possession alone.
- (18:41) [luna: medium (missing-ayat turn); terra: medium (missing-ayat turn); basis: neighbour+scene+theme] أَوْ يُصْبِحَ مَآؤُهَا غَوْرًۭا فَلَن تَسْتَطِيعَ لَهُۥ طَلَبًۭا
  Unverified discovery rationale: luna: Continuing the garden warning in 18:40, the companion says its water could sink into the earth so deeply that the owner cannot recover it, joining crop failure to what is hidden below ground. | terra: The warning that its water may sink beyond recovery makes hidden water the boundary of the garden's apparent productivity.
- (18:44) [luna: medium; basis: neighbour+theme] هُنَالِكَ ٱلْوَلَٰيَةُ لِلَّهِ ٱلْحَقِّ ۚ هُوَ خَيْرٌۭ ثَوَابًۭا وَخَيْرٌ عُقْبًۭا
  Unverified discovery rationale: luna: After the garden owner loses his wealth and helpers in 18:42–43, this verse says true authority and support belong to God, completing the reversal.
- (18:96) [terra: medium (missing-ayat turn); basis: scene] ءَاتُونِى زُبَرَ ٱلْحَدِيدِ ۖ حَتَّىٰٓ إِذَا سَاوَىٰ بَيْنَ ٱلصَّدَفَيْنِ قَالَ ٱنفُخُوا۟ ۖ حَتَّىٰٓ إِذَا جَعَلَهُۥ نَارًۭا قَالَ ءَاتُونِىٓ أُفْرِغْ عَلَيْهِ قِطْرًۭا
  Unverified discovery rationale: terra: Iron is blown upon until it becomes fire before molten copper is poured, a concrete Quranic meeting of metal, heating, and transformation.
- (20:102) [terra: medium (missing-ayat turn); basis: scene+theme] يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ وَنَحْشُرُ ٱلْمُجْرِمِينَ يَوْمَئِذٍۢ زُرْقًۭا
  Unverified discovery rationale: terra: At the trumpet God gathers the guilty on that day, a direct formulation of the final assembly initiated by a single sound.
- (20:108) [terra: medium (missing-ayat turn); basis: neighbour+scene] يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا
  Unverified discovery rationale: terra: On that day people follow the caller without deviation and voices fall silent before the Merciful, giving the gathered crowd its directed movement and hush.
- (22:1) [terra: medium (missing-ayat turn); basis: scene+speaker] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمْ ۚ إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌۭ
  Unverified discovery rationale: terra: The command to fear the Lord is justified by the tremendous quake of the Hour, pairing divine address with earth's final disturbance.
- (22:2) [terra: medium (missing-ayat turn); basis: neighbour+scene] يَوْمَ تَرَوْنَهَا تَذْهَلُ كُلُّ مُرْضِعَةٍ عَمَّآ أَرْضَعَتْ وَتَضَعُ كُلُّ ذَاتِ حَمْلٍ حَمْلَهَا وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ وَلَٰكِنَّ عَذَابَ ٱللَّهِ شَدِيدٌۭ
  Unverified discovery rationale: terra: The quake makes people appear intoxicated and breaks ordinary human bonds, supplying the human crowd's condition within the upheaval of 22:1.
- (25:67) [luna: medium; basis: contrast+theme] وَٱلَّذِينَ إِذَآ أَنفَقُوا۟ لَمْ يُسْرِفُوا۟ وَلَمْ يَقْتُرُوا۟ وَكَانَ بَيْنَ ذَٰلِكَ قَوَامًۭا
  Unverified discovery rationale: luna: The section portrays a hand clenched around wealth; this verse defines the faithful as neither extravagant nor miserly but balanced in spending.
- (26:88) [terra: medium; basis: scene+theme] يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ
  Unverified discovery rationale: terra: On the final day neither wealth nor children benefit, stripping the loved property of the value assigned to it before judgment.
- (26:89) [terra: medium; basis: scene+theme] إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ
  Unverified discovery rationale: terra: Only one who comes with a sound heart benefits, setting inward condition against the wealth dismissed in 26:88.
- (28:80) [terra: medium (missing-ayat turn); basis: contrast+theme] وَقَالَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ وَيْلَكُمْ ثَوَابُ ٱللَّهِ خَيْرٌۭ لِّمَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا وَلَا يُلَقَّىٰهَآ إِلَّا ٱلصَّٰبِرُونَ
  Unverified discovery rationale: terra: Those given knowledge say God's reward is better for faith and good action, opposing informed valuation to the crowd's desire for Qarun's display.
- (29:63) [terra: medium (missing-ayat turn); basis: scene+speaker] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
  Unverified discovery rationale: terra: When asked who sends rain and revives dead earth, people must answer “God”; a question makes land-revival an acknowledged divine act.
- (30:19) [luna: medium; terra: medium; basis: scene+theme] يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَيُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا ۚ وَكَذَٰلِكَ تُخْرَجُونَ
  Unverified discovery rationale: luna: The section joins what is dead to what is brought out alive; this verse pairs God’s bringing the living from the dead with bringing life to earth after its death. | terra: God brings the living from the dead, the dead from the living, and revives earth, followed by وَكَذَٰلِكَ تُخْرَجُونَ.
- (30:24) [terra: medium; basis: scene+theme] وَمِنْ ءَايَٰتِهِۦ يُرِيكُمُ ٱلْبَرْقَ خَوْفًۭا وَطَمَعًۭا وَيُنَزِّلُ مِنَ ٱلسَّمَآءِ مَآءًۭ فَيُحْىِۦ بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: terra: Lightning, hope and fear, rain, and revived earth form another staged sign of life after death.
- (31:23) [terra: medium; basis: speaker+theme] وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: Their return is to God, who will tell them what they did and knows what breasts contain; return, disclosed deeds, and inward knowledge are one sequence.
- (34:3) [luna: medium; basis: theme] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَأْتِينَا ٱلسَّاعَةُ ۖ قُلْ بَلَىٰ وَرَبِّى لَتَأْتِيَنَّكُمْ عَٰلِمِ ٱلْغَيْبِ ۖ لَا يَعْزُبُ عَنْهُ مِثْقَالُ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ وَلَآ أَصْغَرُ مِن ذَٰلِكَ وَلَآ أَكْبَرُ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: The section culminates in the Lord’s knowledge; this verse says nothing hidden in heaven or earth escapes God, down to smaller or larger than an atom.
- (36:82) [terra: medium (missing-ayat turn); basis: neighbour+theme] إِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ شَيْـًٔا أَن يَقُولَ لَهُۥ كُن فَيَكُونُ
  Unverified discovery rationale: terra: God's creative command is simply “Be,” completing the green-tree fire argument with the ease of re-creation.
- (36:83) [terra: medium (missing-ayat turn); basis: neighbour+theme] فَسُبْحَٰنَ ٱلَّذِى بِيَدِهِۦ مَلَكُوتُ كُلِّ شَىْءٍۢ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: All dominion belongs to God and all are returned to Him, closing the resurrection answer with its destination.
- (39:21) [terra: medium (missing-ayat turn); basis: scene+theme] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: Water produces varied crops that yellow and become debris, and the sequence is a reminder for people of inner understanding; field change reaches the inward faculty.
- (39:70) [terra: medium (missing-ayat turn); basis: neighbour+theme] وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُوَ أَعْلَمُ بِمَا يَفْعَلُونَ
  Unverified discovery rationale: terra: Every soul is paid fully for what it did, and God knows best their deeds, completing the record-and-witness scene of 39:69.
- (41:23) [terra: medium (missing-ayat turn); basis: neighbour+theme] وَذَٰلِكُمْ ظَنُّكُمُ ٱلَّذِى ظَنَنتُم بِرَبِّكُمْ أَرْدَىٰكُمْ فَأَصْبَحْتُم مِّنَ ٱلْخَٰسِرِينَ
  Unverified discovery rationale: terra: The assumption that God did not know ruined them, stating the consequence of the mistaken concealment described in 41:22.
- (42:7) [terra: medium; basis: scene+speaker] وَكَذَٰلِكَ أَوْحَيْنَآ إِلَيْكَ قُرْءَانًا عَرَبِيًّۭا لِّتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا وَتُنذِرَ يَوْمَ ٱلْجَمْعِ لَا رَيْبَ فِيهِ ۚ فَرِيقٌۭ فِى ٱلْجَنَّةِ وَفَرِيقٌۭ فِى ٱلسَّعِيرِ
  Unverified discovery rationale: terra: The messenger warns of يَوْمَ الْجَمْعِ, naming the eschatological assembly toward which the section's final runners move.
- (45:5) [luna: medium; terra: medium; basis: scene+theme] وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن رِّزْقٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَتَصْرِيفِ ٱلرِّيَٰحِ ءَايَٰتٌۭ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: This verse also names rain by which God revives earth after its death, a specific rain-and-resurrection parallel to the section. | terra: Provision descending from heaven revives earth after death, repeating the section's field-to-resurrection bridge.
- (47:38) [luna: medium; basis: neighbour+theme] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ تُدْعَوْنَ لِتُنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ فَمِنكُم مَّن يَبْخَلُ ۖ وَمَن يَبْخَلْ فَإِنَّمَا يَبْخَلُ عَن نَّفْسِهِۦ ۚ وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ ۚ وَإِن تَتَوَلَّوْا۟ يَسْتَبْدِلْ قَوْمًا غَيْرَكُمْ ثُمَّ لَا يَكُونُوٓا۟ أَمْثَٰلَكُم
  Unverified discovery rationale: luna: This neighboring verse completes 47:37’s warning that wealth would expose grudges: it calls people to spend and says whoever withholds only withholds from himself.
- (50:22) [terra: medium (missing-ayat turn); basis: neighbour+theme] لَّقَدْ كُنتَ فِى غَفْلَةٍۢ مِّنْ هَٰذَا فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ
  Unverified discovery rationale: terra: The veil is removed from the formerly heedless person and sight becomes sharp, making inwardly resisted judgment suddenly perceptible after arrival with witness.
- (53:32) [terra: medium (missing-ayat turn); basis: scene+theme] ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ إِلَّا ٱللَّمَمَ ۚ إِنَّ رَبَّكَ وَٰسِعُ ٱلْمَغْفِرَةِ ۚ هُوَ أَعْلَمُ بِكُمْ إِذْ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ ۖ فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ
  Unverified discovery rationale: terra: God knows people best when He produced them from earth and while they were hidden embryos, extending divine knowledge through successive forms of concealment.
- (54:38) [terra: medium; basis: contrast+scene] وَلَقَدْ صَبَّحَهُم بُكْرَةً عَذَابٌۭ مُّسْتَقِرٌّۭ
  Unverified discovery rationale: terra: A settled punishment seizes the warned people at morning, another concrete Quranic morning in which the threatened party is overtaken.
- (56:4) [terra: medium; basis: neighbour+scene] إِذَا رُجَّتِ ٱلْأَرْضُ رَجًّۭا
  Unverified discovery rationale: terra: The earth is convulsed violently at the event, beginning a dust-producing final upheaval continued in 56:5-6.
- (56:5) [terra: medium; basis: neighbour+scene] وَبُسَّتِ ٱلْجِبَالُ بَسًّۭا
  Unverified discovery rationale: terra: Mountains are crushed completely, moving the opening scene's raised ground-dust onto a cosmic scale.
- (56:6) [terra: medium; basis: scene+theme] فَكَانَتْ هَبَآءًۭ مُّنۢبَثًّۭا
  Unverified discovery rationale: terra: The crushed mountains become هَبَاءً مُنْبَثًّا, a final-day cloud of dispersed dust answering the dust raised by hooves.
- (56:7) [luna: medium (missing-ayat turn); basis: scene+theme] وَكُنتُمْ أَزْوَٰجًۭا ثَلَٰثَةًۭ
  Unverified discovery rationale: luna: The section says the resurrected rush into a gathering; this verse says people will be sorted into three groups (أَزْوَاجًا ثَلَاثَةً), adding a particular division within the gathered multitude.
- (57:6) [terra: medium (missing-ayat turn); basis: theme] يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ ۚ وَهُوَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: God turns night into day and day into night and knows what breasts contain, extending the section's visible-to-hidden movement under one knowledge.
- (57:24) [terra: medium (missing-ayat turn); basis: theme] ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ ۗ وَمَن يَتَوَلَّ فَإِنَّ ٱللَّهَ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ
  Unverified discovery rationale: terra: Those who are miserly and command others to be miserly are warned that God is self-sufficient, exposing the hoarder's false stance of independence.
- (63:9) [terra: medium; basis: theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
  Unverified discovery rationale: terra: Wealth must not distract from God's remembrance; those it distracts are the losers, a direct diagnosis of intense attachment to property.
- (63:10) [terra: medium; basis: scene+theme] وَأَنفِقُوا۟ مِن مَّا رَزَقْنَٰكُم مِّن قَبْلِ أَن يَأْتِىَ أَحَدَكُمُ ٱلْمَوْتُ فَيَقُولَ رَبِّ لَوْلَآ أَخَّرْتَنِىٓ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ فَأَصَّدَّقَ وَأَكُن مِّنَ ٱلصَّٰلِحِينَ
  Unverified discovery rationale: terra: The command to spend before death arrives makes the closed hand's missed opportunity visible at the boundary of burial and return.
- (64:9) [luna: medium (missing-ayat turn); terra: medium; basis: scene+theme] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
  Unverified discovery rationale: luna: This verse explicitly names the Day God gathers people for the Day of Gathering and calls it the day of mutual loss, matching the section’s graves-to-assembly movement and reversal of worldly confidence. | terra: The day God gathers humanity is also the day of mutual loss, adding judgment's separating consequence to the collected crowd.
- (68:23) [terra: medium; basis: neighbour+scene] فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ
  Unverified discovery rationale: terra: They set out whispering, making the morning harvesting party a coordinated secret expedition before 68:24 reveals its aim.
- (68:29) [terra: medium (missing-ayat turn); basis: neighbour+speaker] قَالُوا۟ سُبْحَٰنَ رَبِّنَآ إِنَّا كُنَّا ظَٰلِمِينَ
  Unverified discovery rationale: terra: The garden owners finally glorify their Lord and confess wrongdoing, supplying the answer to the central person's rebuke in 68:28.
- (68:31) [terra: medium (missing-ayat turn); basis: neighbour+theme] قَالُوا۟ يَٰوَيْلَنَآ إِنَّا كُنَّا طَٰغِينَ
  Unverified discovery rationale: terra: They acknowledge that they were transgressors, naming the moral nature of the dawn expedition after its reversal.
- (68:32) [terra: medium (missing-ayat turn); basis: neighbour+theme] عَسَىٰ رَبُّنَآ أَن يُبْدِلَنَا خَيْرًۭا مِّنْهَآ إِنَّآ إِلَىٰ رَبِّنَا رَٰغِبُونَ
  Unverified discovery rationale: terra: They hope their Lord will replace the garden with something better, turning failed possession into dependence on the Provider.
- (68:33) [terra: medium; basis: neighbour+theme] كَذَٰلِكَ ٱلْعَذَابُ ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: terra: كَذَٰلِكَ الْعَذَابُ identifies the ruined garden as divine punishment and points beyond it to the greater afterlife reckoning.
- (69:28) [terra: medium (missing-ayat turn); basis: scene+theme] مَآ أَغْنَىٰ عَنِّى مَالِيَهْ ۜ
  Unverified discovery rationale: terra: The judged person admits that his wealth did not benefit him, reversing the value attached to property before exposure.
- (69:29) [terra: medium (missing-ayat turn); basis: neighbour+theme] هَلَكَ عَنِّى سُلْطَٰنِيَهْ
  Unverified discovery rationale: terra: His authority has vanished after his wealth fails, completing the stripping away of outward power at judgment.
- (69:34) [terra: medium (missing-ayat turn); basis: theme] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
  Unverified discovery rationale: terra: Failure to urge feeding the poor is named within the causes of punishment, carrying withholding into judgment.
- (70:24) [luna: medium; basis: theme] وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ
  Unverified discovery rationale: luna: The section links gathered goods and the needy; this verse describes a recognized share in wealth for those who ask and those deprived.
- (70:25) [luna: medium; basis: neighbour+theme] لِّلسَّآئِلِ وَٱلْمَحْرُومِ
  Unverified discovery rationale: luna: This verse specifies the recipients of the wealth-share in 70:24 as the asker and the deprived, completing its social counterpart to the closed hand.
- (74:12) [terra: medium (missing-ayat turn); basis: theme] وَجَعَلْتُ لَهُۥ مَالًۭا مَّمْدُودًۭا
  Unverified discovery rationale: terra: God gave the denier extended wealth, establishing property as a divine provision toward which his later greed is ungrateful.
- (74:15) [terra: medium (missing-ayat turn); basis: theme] ثُمَّ يَطْمَعُ أَنْ أَزِيدَ
  Unverified discovery rationale: terra: He still covets an increase after abundant provision, a concise parallel to acquisitive intensity.
- (74:26) [terra: medium (missing-ayat turn); basis: neighbour+scene] سَأُصْلِيهِ سَقَرَ
  Unverified discovery rationale: terra: God promises to cast that covetous recipient of wealth into Saqar, taking provision and ingratitude into fire.
- (74:44) [terra: medium (missing-ayat turn); basis: theme] وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ
  Unverified discovery rationale: terra: The condemned confess that they did not feed the poor, a final disclosure of the same refusal staged by the garden owners.
- (78:18) [luna: medium; basis: scene] يَوْمَ يُنفَخُ فِى ٱلصُّورِ فَتَأْتُونَ أَفْوَاجًۭا
  Unverified discovery rationale: luna: The section’s horses enter a gathering and the resurrected arrive in groups; this verse says the day the trumpet is blown, people come in multitudes (أَفْوَاجًا).
- (81:14) [terra: medium; basis: scene+theme] عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ
  Unverified discovery rationale: terra: At the cosmic unveiling every soul knows what it has brought, matching the section's progression from spectacle to inward account.
- (84:3) [terra: medium (missing-ayat turn); basis: neighbour+scene] وَإِذَا ٱلْأَرْضُ مُدَّتْ
  Unverified discovery rationale: terra: The earth is stretched flat immediately before it casts out and empties what is inside, preparing the exposed ground of 84:4.
- (89:22) [luna: medium (missing-ayat turn); basis: neighbour+scene] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
  Unverified discovery rationale: luna: This verse completes 89:21’s earth-pounding scene: the Lord comes and angels arrive in ranks, adding the ordered assembly before which the section’s wealthy human stands.
- (92:14) [terra: medium; basis: neighbour+scene] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
  Unverified discovery rationale: terra: The blazing fire warned in this ayah supplies the judgment horizon for the miser and the purifying giver contrasted in the surrounding passage.
- (92:18) [terra: medium; basis: contrast+theme] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
  Unverified discovery rationale: terra: The Godfearing person gives his wealth يَتَزَكَّىٰ, reversing hoarding and turning property into a means of inward purification.
- (96:14) [terra: medium; basis: speaker+theme] أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
  Unverified discovery rationale: terra: أَلَمْ يَعْلَمْ بِأَنَّ اللَّهَ يَرَىٰ uses the same admonishing question to confront a person acting as though divine awareness were absent.
- (99:3) [terra: medium; basis: scene+speaker] وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
  Unverified discovery rationale: terra: The human asks what is happening to the earth, supplying the bewildered human question between its upheaval and its disclosure.
- (102:4) [terra: medium; basis: neighbour+speaker] ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
  Unverified discovery rationale: terra: The repeated ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ makes the threatened transition from present heedlessness to final knowledge emphatic.
- (102:7) [terra: medium; basis: neighbour+scene] ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
  Unverified discovery rationale: terra: The Fire is seen عَيْنَ الْيَقِينِ, completing the visible certainty promised to the accumulators and grave-visitors.
- (111:2) [terra: medium; basis: scene+theme] مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
  Unverified discovery rationale: terra: مَا أَغْنَىٰ عَنْهُ مَالُهُ وَمَا كَسَبَ denies saving power to accumulated property immediately before fire.
- (111:3) [terra: medium; basis: neighbour+scene] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
  Unverified discovery rationale: terra: The owner whose wealth does not avail in 111:2 enters a blazing fire, completing the property-to-flame movement.

## weak (4)

- (24:35) [terra: weak; basis: scene+theme] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: terra: Oil from the blessed tree nearly shines even before fire touches it, a possible Quranic analogue for flame latent in plant matter, though this ayah's governing image is divine light rather than resurrection.
- (68:18) [terra: weak; basis: neighbour+theme] وَلَا يَسْتَثْنُونَ
  Unverified discovery rationale: terra: وَلَا يَسْتَثْنُونَ may mean that the garden owners made no exception for the poor, directly sharpening their withholding; it may instead refer to failing to say “if God wills.”
- (79:4) [terra: weak; basis: scene+theme] فَٱلسَّٰبِقَٰتِ سَبْقًۭا
  Unverified discovery rationale: terra: فَالسَّابِقَاتِ سَبْقًا presents racers whose motion proves precedence, like the opening animal's run witnessing that it has gone ahead; the racers' identity is disputed.
- (84:23) [terra: weak; basis: root+theme] وَٱللَّهُ أَعْلَمُ بِمَا يُوعُونَ
  Unverified discovery rationale: terra: وَاللَّهُ أَعْلَمُ بِمَا يُوعُونَ can evoke what people inwardly harbor or gather away, but the precise force of يُوعُونَ is broader than the section's chest-assay image.

## contrast (4)

- (37:177) [terra: contrast; basis: contrast+scene] فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ
  Unverified discovery rationale: terra: When the threatened force descends into their courtyard, فَسَاءَ صَبَاحُ الْمُنْذَرِينَ; the morning assaulters' image is reversed into a terrible morning for those assaulted.
- (59:6) [terra: contrast; basis: contrast+root+scene] وَمَآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْهُمْ فَمَآ أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍۢ وَلَا رِكَابٍۢ وَلَٰكِنَّ ٱللَّهَ يُسَلِّطُ رُسُلَهُۥ عَلَىٰ مَن يَشَآءُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: فَمَا أَوْجَفْتُمْ عَلَيْهِ مِنْ خَيْلٍ denies that believers spurred horses in this campaign, marking a Quranic boundary to the mounted-raid scene.
- (76:8) [terra: contrast (missing-ayat turn); basis: contrast+theme] وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا
  Unverified discovery rationale: terra: They feed the needy despite their love of the food, reversing the section's intense attachment by allowing love to remain while giving the loved thing away.
- (101:4) [terra: contrast; basis: contrast+scene] يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
  Unverified discovery rationale: terra: People become كَالْفَرَاشِ الْمَبْثُوثِ, a dispersed human swarm that illuminates by reversal the image of entering the middle of a gathered mass.

## neighbours: within two ayat of a passage the section cites (17)

- (7:55) [next to 7:57] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (7:56) [next to 7:57] وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا وَٱدْعُوهُ خَوْفًۭا وَطَمَعًا ۚ إِنَّ رَحْمَتَ ٱللَّهِ قَرِيبٌۭ مِّنَ ٱلْمُحْسِنِينَ
- (7:59) [next to 7:57] لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (9:32) [next to 9:34] يُرِيدُونَ أَن يُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَيَأْبَى ٱللَّهُ إِلَّآ أَن يُتِمَّ نُورَهُۥ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (9:33) [next to 9:34] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ وَلَوْ كَرِهَ ٱلْمُشْرِكُونَ
- (9:36) [next to 9:34] إِنَّ عِدَّةَ ٱلشُّهُورِ عِندَ ٱللَّهِ ٱثْنَا عَشَرَ شَهْرًۭا فِى كِتَٰبِ ٱللَّهِ يَوْمَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ مِنْهَآ أَرْبَعَةٌ حُرُمٌۭ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ ۚ فَلَا تَظْلِمُوا۟ فِيهِنَّ أَنفُسَكُمْ ۚ وَقَٰتِلُوا۟ ٱلْمُشْرِكِينَ كَآفَّةًۭ كَمَا يُقَٰتِلُونَكُمْ كَآفَّةًۭ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَعَ ٱلْمُتَّقِينَ
- (9:37) [next to 9:35] إِنَّمَا ٱلنَّسِىٓءُ زِيَادَةٌۭ فِى ٱلْكُفْرِ ۖ يُضَلُّ بِهِ ٱلَّذِينَ كَفَرُوا۟ يُحِلُّونَهُۥ عَامًۭا وَيُحَرِّمُونَهُۥ عَامًۭا لِّيُوَاطِـُٔوا۟ عِدَّةَ مَا حَرَّمَ ٱللَّهُ فَيُحِلُّوا۟ مَا حَرَّمَ ٱللَّهُ ۚ زُيِّنَ لَهُمْ سُوٓءُ أَعْمَٰلِهِمْ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (47:35) [next to 47:37] فَلَا تَهِنُوا۟ وَتَدْعُوٓا۟ إِلَى ٱلسَّلْمِ وَأَنتُمُ ٱلْأَعْلَوْنَ وَٱللَّهُ مَعَكُمْ وَلَن يَتِرَكُمْ أَعْمَٰلَكُمْ
- (47:36) [next to 47:37] إِنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ ۚ وَإِن تُؤْمِنُوا۟ وَتَتَّقُوا۟ يُؤْتِكُمْ أُجُورَكُمْ وَلَا يَسْـَٔلْكُمْ أَمْوَٰلَكُمْ
- (50:42) [next to 50:44] يَوْمَ يَسْمَعُونَ ٱلصَّيْحَةَ بِٱلْحَقِّ ۚ ذَٰلِكَ يَوْمُ ٱلْخُرُوجِ
- (50:43) [next to 50:44] إِنَّا نَحْنُ نُحْىِۦ وَنُمِيتُ وَإِلَيْنَا ٱلْمَصِيرُ
- (50:45) [next to 50:44] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
- (68:15) [next to 68:17] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (68:16) [next to 68:17] سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ
- (70:41) [next to 70:43] عَلَىٰٓ أَن نُّبَدِّلَ خَيْرًۭا مِّنْهُمْ وَمَا نَحْنُ بِمَسْبُوقِينَ
- (70:42) [next to 70:43] فَذَرْهُمْ يَخُوضُوا۟ وَيَلْعَبُوا۟ حَتَّىٰ يُلَٰقُوا۟ يَوْمَهُمُ ٱلَّذِى يُوعَدُونَ
- (70:44) [next to 70:43] خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۚ ذَٰلِكَ ٱلْيَوْمُ ٱلَّذِى كَانُوا۟ يُوعَدُونَ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 100, "section": 11, "run_tag": "sol-session-20261005", "source_sha256": "3a6b25a830b4ea96189b0c2300605ec958f572fbc92f8603f0e4cbbc0271856b", "list_sha256": "106574e047f27eea5febcc81e13ebc56a8ffd87d063a5c06e01b359ae3445608", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec11/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 16, "unique_additions": 16, "repeated_proposals": [], "turn1_sha256": "bcda5fa26696fe3b031d270c8b57ebaaf1b5624221a8784b8e2273f29a3be76c", "followup_sha256": "69834bc444f22cf3d1ba37fbb5dfc945698cca0da1edd127ccd0181b91735bd1", "proposal_file": "followup.tsv", "proposal_sha256": "69834bc444f22cf3d1ba37fbb5dfc945698cca0da1edd127ccd0181b91735bd1", "list_sha256": "1c55cb3a9d99a806b0ed878b6e35c8e20a7b253b5c06c1b28e43dfe0b884dc4a", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec11/luna/list.tsv", "rows": 170, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 30, "ref": "99:6", "arabic": "الصُّدُور", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 56, "ref": "56:63", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 56, "ref": "56:63", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 61, "ref": "6:95", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 61, "ref": "6:95", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 62, "ref": "2:261", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 63, "ref": "55:12", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 63, "ref": "55:12", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 77, "ref": "102:1", "arabic": "أَلْهَاكُمُ التَّكَاثُرُ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 97, "ref": "59:10", "arabic": "غِلًّا فِي قُلُوبِنَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 116, "ref": "31:16", "arabic": "حبّ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec11/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 80, "unique_additions": 80, "repeated_proposals": [], "turn1_sha256": "68f54a83446e9134077de2f0b3054f277082a4a5f693853a7aae450d91daf9fc", "followup_sha256": "025e5818bdd7c6dc378abd6fe5d0a33c9cacb5c55fe52175c2caff4a8455dc42", "proposal_file": "followup.tsv", "proposal_sha256": "025e5818bdd7c6dc378abd6fe5d0a33c9cacb5c55fe52175c2caff4a8455dc42", "list_sha256": "246a6594e802dc0af75591341e35f628951045674773ffa2d98aeeda3e1ecd2c", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/discovery/sol-session-20261005/sec11/terra/list.tsv", "rows": 244, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 16, "ref": "56:71", "arabic": "أَفَرَأَيْتُمُ النَّارَ الَّتِي تُورُونَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 26, "ref": "104:7", "arabic": "الْأَفْئِدَةِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 33, "ref": "102:1", "arabic": "أَلْهَاكُمُ التَّكَاثُرُ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 38, "ref": "102:8", "arabic": "نعيم", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 39, "ref": "38:31", "arabic": "حُبَّ الْخَيْرِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["38:32"], "matching_ref_count": 1}, {"line": 145, "ref": "57:17", "arabic": "اعْلَمُوا أَنَّ اللَّهَ يُحْيِي الْأَرْضَ بَعْدَ مَوْتِهَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 170, "ref": "75:3", "arabic": "جَمْع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

