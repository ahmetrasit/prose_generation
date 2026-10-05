Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 5 of 11 ("Özü kabuğundan ayırmak"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 5 (prose paragraphs numbered) =====
[¶23] Onuncu ayetin fiili bir ayıklama işidir: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fi's-sudûr, gloss:ve göğüslerde olan ayıklanıp ortaya konduğunda, source:100:10}. Fiilin aslı üç ayrı ayıklamayı tek bir tanıma toplar: {ar:التحصيل إخراج اللب من القشور كإخراج الذهب من حجر المعدن والبر من التبن, tr:et-tahsîlu ihrâcu'l-lubbi mine'l-kuşûr, ke-ihrâci'z-zehebi min haceri'l-ma'deni ve'l-burri mine't-tibn, gloss:"tahsîl", özü kabuklardan çıkarmaktır; altını maden taşından, buğdayı samandan çıkarmak gibi, source:"ح ص ل,B002"}. İşin kendisi bir ayırt etmedir: {ar:التحصيل تمييز ما يحصل, tr:et-tahsîlu temyîzu mâ yahsul, gloss:"tahsîl", elde kalanı ayırt etmektir, source:"ح ص ل,B002"}. Geriye kalan şey ise ötekiler gidince sabit kalandır: {ar:حصل يحصل حصولا أي بقي وثبت وذهب ما سواه من حساب أو عمل, tr:hasale yahsulu husûlen, ey bekıye ve sebete ve zehebe mâ sivâhu min hısâbin ev amel, gloss:"hasale", yani hesapta ya da işte geri kalanlar gidip kendisi kaldı ve sabitlendi, source:"ح ص ل,B001"}. Bu bir hesabın son satırıdır: {ar:أظهر ما فيها وجمع أو إظهار الحاصل من الحساب, tr:azhara mâ fîhâ ve ceme'a ev izhâru'l-hâsıli mine'l-hısâb, gloss:içindekini açığa çıkardı ve topladı; ya da hesaptan kalan toplamı ortaya koymak, source:"ح ص ل,B001"}. Ayetteki fiil edilgen ve şeddelidir. Bu kalıp işin emekle, adım adım yapıldığını duyurur. Ayıklayanın adı anılmaz, yalnızca ayıklanan şey öne çıkar. Aynı kökün kuş dünyasında da bir karşılığı vardır: {ar:حوصلة الطائر لأنه يجمع فيها, tr:havsaletu't-tâiri li-ennehû yecma'u fîhâ, gloss:kuşun kursağı; çünkü yediklerini orada toplar, source:"ح ص ل,B004"}. Göğüs de böyle bir kursaktır, yıllar boyunca içine alınanların biriktiği bir kap. Kur'an'da göğüs insanın içini taşıyan kaptır: {ar:الصدر للإنسان والجمع صدور, tr:es-sadru li'l-insâni ve'l-cem'u sudûr, gloss:insanın göğsü; çoğulu "sudûr", source:"ص د ر,B001"}.

[¶24] Sekizinci ayetteki sevgi kelimesinin ailesi bu ayıklama sahnesinde yerini alır. Kelimenin yanında tane duyulur: {ar:الحب والحبة في الحنطة والشعير وبزور الرياحين, tr:el-habbu ve'l-habbetu fi'l-hıntati ve'ş-şa'îri ve buzûri'r-reyâhîn, gloss:buğdayda, arpada ve kokulu bitki tohumlarında tane, source:"ح ب ب,B001"}. Kalbin içinde de bir tane vardır: {ar:حبة القلب سويداؤه ويقال ثمرته, tr:habbetu'l-kalbi suveydâuhû ve yukâlu semeratuh, gloss:kalbin tanesi onun kara noktasıdır, meyvesi de denir, source:"ح ب ب,B004"}. Bu tane kalbin en içindedir: {ar:حبة القلب هي العلقة السوداء التي تكون داخل القلب, tr:habbetu'l-kalbi hiye'l-alakatu's-sevdâu'lletî tekûnu dâhile'l-kalb, gloss:kalbin tanesi, kalbin içindeki kara pıhtıdır, source:"ح ب ب,B004"}. İki kök harman yerinde buluşur: {ar:الحصالة ما يبقى في الأندر من الحب بعد ما يرفع الحب وهو الكناسة, tr:el-husâletu mâ yebkâ fi'l-enderi mine'l-habbi ba'de mâ yurfe'u'l-habbu ve huve'l-kunâse, gloss:"husâle", tane kaldırıldıktan sonra harmanda kalan süprüntüdür, source:"ح ص ل,B003"}. Bu yan yana gelişler şunu duyurur: insanın şiddetle bağlandığı sevgi, göğsün içindeki tanedir ve ayıklanacak olan da odur. Harman savrulunca tane bir yana, saman öbür yana gider.

[¶25] Surenin son kelimesi bu ayıklamanın hangi bilgiye dayandığını söyler: {ar:الخبرة المعرفة ببواطن الأمر, tr:el-hibratu'l-ma'rifetu bi-bevâtıni'l-emr, gloss:"hibre", işin iç yüzünü bilmektir, source:"خ ب ر,B001"}. Aynı kökte içi dışından ayıran bir karşıtlık da vardır: {ar:المخبر خلاف المنظر, tr:el-mahbaru hılâfu'l-manzar, gloss:"mahber" (iç yüz), "manzar"ın (görünüşün) karşıtıdır, source:"خ ب ر,B001"}. Dokuzuncu ile onuncu ayet aynı kalıpla kurulmuştur: "kabirlerde olan" ve "göğüslerde olan". Kabir kelimesinin bir açıklaması iki ayeti doğrudan birbirine bağlar: {ar:أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة, tr:ahvâlu'l-insâni mâ dâme fi'd-dunyâ mesturatun ke-ennehâ makbûra, gloss:insan dünyada oldukça halleri örtülüdür, sanki gömülüdürler, source:"ق ب ر,B005"}. Önce bedenler topraktan çıkar, sonra göğüslerde gömülü olan ayıklanır. Düz bir anlatım "kalpteki her şey açığa çıkacak" demekle yetinirdi. Bu görüntü ise o açığa çıkışı bir işçilik olarak gösterir: kabuk soyulur, tane ayrılır, hesap son satırına kadar indirilir.

[¶26] Kur'an göğüslerdekinin sınanmasını Uhud'dan sonra, inananlara indirilen ayette anlatır. Bir kısmı huzurlu bir uykuya dalmışken bir kısmı kendi derdine düşmüştü ve {ar:يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ, tr:yuhfûne fî enfusihim mâ lâ yubdûne lek, gloss:sana açmadıklarını içlerinde gizliyorlardı, source:3:154}. Ayet şöyle sürer: {ar:وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ, tr:ve li-yebteliya'llâhu mâ fî sudûrikum ve li-yumahhısa mâ fî kulûbikum, gloss:Allah göğüslerinizdekini sınasın ve kalplerinizdekini arıtsın diye, source:3:154}. "Mâ fî sudûrikum" ifadesi bizim ayetin ifadesiyle aynıdır. Yanında yer alan "arıtma" fiili de bir ayıklama işidir. Allah'ın elçisine şunu söylemesi de buyrulur: {ar:قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ, tr:kul in tuhfû mâ fî sudûrikum ev tubdûhu ya'lemhu'llâh, gloss:de ki: göğüslerinizdekini gizleseniz de açığa vursanız da Allah onu bilir, source:3:29}. Kalplerinde hastalık olanlara {ar:أَمْ حَسِبَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌ أَن لَّن يُخْرِجَ ٱللَّهُ أَضْغَٰنَهُمْ, tr:em hasibe'llezîne fî kulûbihim maradun en len yuhrica'llâhu adğânehum, gloss:kalplerinde hastalık olanlar, Allah'ın kinlerini dışarı çıkarmayacağını mı sandılar, source:47:29} diye sorulur. Gecenin yıldızı üzerine yeminle başlayan surede ise o gün kısaca {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tublâ's-serâir, gloss:gizlilerin sınandığı gün, source:86:9} diye anılır. Ayıklamanın inceliği de zerre ölçüsüyle verilir: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığınca hayır işlerse onu görür, source:99:7}.

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

===== passages from the discovery list (267) =====
## strong (140)

- (2:177) [terra: strong (missing-ayat turn); basis: root+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: terra: True righteousness includes giving wealth despite loving it, so inner attachment is disclosed and transformed through relinquishment.
- (2:204) [luna: strong (missing-ayat turn); terra: contrast; basis: contrast+scene+theme] وَمِنَ ٱلنَّاسِ مَن يُعْجِبُكَ قَوْلُهُۥ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَيُشْهِدُ ٱللَّهَ عَلَىٰ مَا فِى قَلْبِهِۦ وَهُوَ أَلَدُّ ٱلْخِصَامِ
  Unverified discovery rationale: luna: This ayah joins attractive public speech to what is in the heart, which is hostile; it directly meets the section's contrast between the chest's hidden contents and outward appearance. | terra: A person's worldly speech pleases and he invokes God over what is in his heart, yet he is the fiercest opponent; polished exterior and inner reality diverge.
- (2:205) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] وَإِذَا تَوَلَّىٰ سَعَىٰ فِى ٱلْأَرْضِ لِيُفْسِدَ فِيهَا وَيُهْلِكَ ٱلْحَرْثَ وَٱلنَّسْلَ ۗ وَٱللَّهُ لَا يُحِبُّ ٱلْفَسَادَ
  Unverified discovery rationale: luna: Following the person whose words and heart diverge in 2:204, this ayah shows him corrupting the land and destroying crops and offspring, joining the hidden heart to a concrete agricultural consequence. | terra: When that person turns away, he destroys crops and offspring; the action supplies the exposed fruit of the hidden antagonism in 2:204.
- (2:261) [luna: strong; terra: medium; basis: root+scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section's dictionary form حَبّة is grain as the kernel of the heart; this ayah makes one grain grow seven ears, each with a hundred grains, turning that kernel into a concrete image of multiplied provision. | terra: A single حبة grows seven ears with a hundred grains each as a figure for expenditure, making a deed's hidden seed disclose its multiplied yield.
- (2:265) [terra: strong; basis: neighbour+scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: terra: Giving from desire for God's pleasure and inner firmness is likened to a garden yielding abundantly, supplying the inwardly sound counterpart to 2:264's stripped surface.
- (2:267) [luna: strong; terra: strong; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
  Unverified discovery rationale: luna: The section's grain is extracted from husk; this ayah speaks of what God brings from the earth and forbids choosing its bad portion to give away, making quality-selection in produce a concrete moral boundary. | terra: Believers must spend from the good things they earn and from earth's produce rather than deliberately selecting the bad, combining harvest, wealth, and moral sorting.
- (2:283) [terra: strong; basis: scene+theme] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
  Unverified discovery rationale: terra: Concealing testimony is called a sin of the heart, and God knows what people do; a suppressed outward truth becomes an inner moral deposit.
- (2:284) [luna: strong; terra: strong; basis: scene+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: luna: The section's “what is in the breasts” becomes an account; this ayah says whatever people disclose or conceal within themselves is reckoned by God, explicitly linking inward contents to judgment. | terra: Whether people disclose or conceal what is within themselves, God calls them to account for it; hidden interior and final reckoning are directly joined.
- (3:29) [luna: strong; terra: strong; basis: root+speaker+theme] [cited in ¶26] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section foregrounds the wording “ما في الصدور”; this ayah says whether people hide or disclose what is in their breasts, God knows it, grounding the image in knowledge of concealed contents. | terra: The commanded warning uses the same ما في صدوركم and says that concealing or disclosing it makes no difference to God's knowledge.
- (3:30) [luna: strong (missing-ayat turn); basis: contrast+scene+theme] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: luna: The section describes the final account exposing what was inside; this ayah says each soul will find its good and evil deeds present and wish the evil far away, a concrete disclosure of both sides of the account.
- (3:92) [luna: medium; terra: strong; basis: contrast+root+theme] لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ ۚ وَمَا تُنفِقُوا۟ مِن شَىْءٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section depicts strong love of wealth as a kernel in the chest; this ayah says righteousness is not reached until one spends what one loves, turning that attachment toward relinquishment. | terra: People cannot reach righteousness until they spend from what they love, making relinquishment of the beloved thing the test that discloses love's quality.
- (3:118) [luna: strong; terra: strong; basis: contrast+root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ بِطَانَةًۭ مِّن دُونِكُمْ لَا يَأْلُونَكُمْ خَبَالًۭا وَدُّوا۟ مَا عَنِتُّمْ قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ ۚ قَدْ بَيَّنَّا لَكُمُ ٱلْءَايَٰتِ ۖ إِن كُنتُمْ تَعْقِلُونَ
  Unverified discovery rationale: luna: The section's inside/outside distinction is explicit here: hostility has appeared from mouths, while what breasts conceal is greater, so the inner contents exceed their visible trace. | terra: Hatred has appeared from mouths, but what breasts hide is greater, making the unseen interior exceed the visible disclosure.
- (3:119) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+neighbour+root+scene+theme] هَٰٓأَنتُمْ أُو۟لَآءِ تُحِبُّونَهُمْ وَلَا يُحِبُّونَكُمْ وَتُؤْمِنُونَ بِٱلْكِتَٰبِ كُلِّهِۦ وَإِذَا لَقُوكُمْ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ عَضُّوا۟ عَلَيْكُمُ ٱلْأَنَامِلَ مِنَ ٱلْغَيْظِ ۚ قُلْ مُوتُوا۟ بِغَيْظِكُمْ ۗ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The section contrasts inward truth with outward appearance; this ayah contrasts people who greet believers warmly with the rage they show in private and says God knows what breasts contain. | terra: The same people profess belief when they meet believers and bite their fingers in rage when alone; the ayah closes with God's knowledge of breast contents, completing 3:118's hidden hatred.
- (3:141) [luna: strong; terra: strong (missing-ayat turn); basis: root+scene+theme] وَلِيُمَحِّصَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَيَمْحَقَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section's 3:154 uses the purification verb “لِيُمَحِّصَ” for hearts; this earlier Uhud passage says God purifies the believers, using the same verb for the larger testing process. | terra: God's purpose is to purify the believers and efface the disbelievers; the same refining family developed beside 3:154 is stated as the purpose of trial.
- (3:152) [luna: strong (missing-ayat turn); basis: contrast+theme] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: In the Uhud passage that leads to the section's 3:154 example, this ayah distinguishes those who wanted this world from those who wanted the Hereafter, making battle behavior expose the attachment within.
