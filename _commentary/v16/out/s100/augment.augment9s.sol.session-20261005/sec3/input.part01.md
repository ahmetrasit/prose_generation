Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 3 of 11 ("Taştan ateş çakmak"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 3 (prose paragraphs numbered) =====
[¶13] İkinci ayet bir ateş yakma işlemini anlatır: {ar:فَٱلْمُورِيَٰتِ قَدْحًا, tr:fe'l-mûriyâti kadhâ, gloss:derken çakarak ateş çıkaranlara, source:100:2}. Ateş şöyle çakılır: bir demir parçası taşa sertçe vurulur, kopan kıvılcım tutuşmaya hazır bir maddeye düşer ve ateş doğar. İki kelime bu işlemin iki aletini tek bir tanımda birleştirir: {ar:المقدحة ما تقدح به النار والقداحة والقداح الحجر الذي يوري النار, tr:el-mikdahatu mâ tukdahu bihi'n-nâr, ve'l-kaddâhatu ve'l-kaddâhu'l-haceru'llezî yûri'n-nâr, gloss:"mikdaha" ateşin onunla çakıldığı alettir; "kaddâha" ve "kaddâh" ateş çıkaran taştır, source:"ق د ح,B001"}. Ayetin ilk kelimesinin kökü de ateşin dışarı çıkmasını anlatır: {ar:ورى الزند خرجت ناره, tr:verâ'z-zend, harecet nâruh, gloss:çakmak tutuştu, yani ateşi çıktı, source:"و ر ي,B002"}. Aynı kök sönmeye yüz tutmuş ateşi canlandırmayı da kapsar: {ar:أوريت النار إذا كانت خامدة فأججتها, tr:evraytu'n-nâra izâ kânet hâmideten fe-eccectehâ, gloss:sönük duran ateşi alevlendirdiğinde "evraytu" dersin, source:"و ر ي,B002"}. Surede bu aletler, koşan hayvanların taşlara çarpan ayaklarıdır. Hız taşla karşılaşınca kıvılcım çıkar.

[¶14] Birinci ayetin kelimesi, anlamının yanında bu ateşin izlerini de taşır. Çakmak taşları "dabh" ile nitelenir: {ar:حجارة القداحة مضبوحة, tr:hicâratu'l-kaddâhati madbûha, gloss:çakmak taşları "madbûh"tur, yani yanıktır, source:"ض ب ح,B003"}. Kelime ateşle dağlanmayı da anlatır: {ar:الضبح إحراق أعالي العود بالنار, tr:ed-dabhu ihrâku a'âli'l-ûdi bi'n-nâr, gloss:"dabh", çubuğun ucunu ateşle yakmaktır, source:"ض ب ح,B003"}. Yanan şeyin rengi değişir: {ar:ضبحته الشمس وضبته إذا غيرت لونه وكذلك النار, tr:dabahathu'ş-şemsu ve dabbethu izâ ğayyerat levneh, ve kezâlike'n-nâr, gloss:güneş ya da ateş bir şeyin rengini değiştirince "onu dabh etti" denir, source:"ض ب ح,B004"}. Geriye kalan şey de aynı kelimeyle adlandırılır: {ar:الضبح الرماد, tr:ed-dabhu'r-ramâd, gloss:"dabh" küldür, source:"ض ب ح,B005"}. Böylece birinci ayetin soluğu, ikinci ayetin ateşinin hem kızgınlığını hem de külünü yanında taşır.

[¶15] Sekizinci ayetin {ar:لِحُبِّ, tr:li-hubbi, gloss:sevgisine, source:100:8} kelimesinin ailesinde, atların çaktığı ateşin özel bir adı vardır: {ar:نار الحباحب ما أورت الخيل لا ينتفع به, tr:nâru'l-hubâhibi mâ evrati'l-haylu lâ yuntefe'u bih, gloss:"hubâhib ateşi", atların çıkardığı, hiçbir işe yaramayan ateştir, source:"ح ب ب,B011"}. Bu ateş havada uçuşan kıvılcımlardan ibarettir: {ar:ما اقتدحت من شرار النار في الهواء من تصادم الحجارة, tr:mâ'ktedahte min şerâri'n-nâri fi'l-hevâi min tesâdumi'l-hicâra, gloss:taşların çarpışmasıyla havaya çaktığın kıvılcımlar, source:"ح ب ب,B011"}. Buna karşılık üçüncü ayetin kelimesinin ailesinde süren ışık durur: {ar:المصباح السراج وقد استصبحت به إذا أسرجت, tr:el-misbâhu's-sirâc, ve kad istasbahtu bihî izâ esracte, gloss:"misbâh" kandildir; onu yaktığında "istasbahtu" dersin, source:"ص ب ح,B005"}. Günün ışığı da bu kökle anılır: {ar:الصباح نور النهار, tr:es-sabâhu nûru'n-nehâr, gloss:sabah, gündüzün ışığıdır, source:"ص ب ح,B001"}. İkinci ayetin kıvılcımı karanlıkta bir an parlar, üçüncü ayetin sabahı ise karanlığın yerini kalıcı olarak alan ışıktır. Sekizinci ayetteki sevginin yanında duyulan ateş ise atların çaktığı ama hiçbir şey aydınlatmayan kıvılcımdır.

[¶16] Ateş insana da döner. Altıncı ayetteki insan kelimesinin kökü uzaktan bir ateş görmeyi anlatır: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, ya'nî ebsara nâran, gloss:bir yandan "ânese", yani bir ateş gördü, source:"ء ن س,B002"}. Ateş çakmak, bir işi düşünüp tartmanın da adıdır: {ar:الإنسان يقتدح الأمر إذا نظر فيه ودبر, tr:el-insânu yaktedihu'l-emra izâ nazara fîhi ve debbera, gloss:insan bir işi inceleyip tartınca "o işi çakar", source:"ق د ح,B010"}. Çakmağın tutuşması, girişilen işin başarılmasıdır: {ar:لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب, tr:le-vâri'z-zinâd izâ râme emran encaha fîhi ve edreke mâ taleb, gloss:çakmağı tutuşan biri, bir işe girişince başarır ve istediğine ulaşır, source:"و ر ي,B003"}. Ama aynı çakmak yanlış taşa da vurulabilir: {ar:فلان يستوري زناد الضلالة, tr:fulânun yestevrî zinâde'd-dalâle, gloss:falanca sapıklığın çakmağından ateş çıkarmaya çalışıyor, source:"و ر ي,B009"}. Böylece görüntü, ikinci ayetin kıvılcımlarından insanın kendi aklını nasıl kullandığı sorusuna geçer: bu kıvılcım tutuşan bir iş mi olacak, boşa uçuşan bir ateş mi?

[¶17] Kur'an aynı fiili, dirilişi inkâr edenlere yönelttiği sorularda kullanır. Ölüp toprak olduktan sonra diriltilmeyi uzak görenlere Allah ekin, su ve ateş üzerine sorular sorar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:çakıp çıkardığınız ateşi gördünüz mü, source:56:71}, {ar:ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ, tr:e-entum enşe'tum şeceratehâ em nahnu'l-munşi'ûn, gloss:onun ağacını siz mi yarattınız, yoksa yaratan biz miyiz, source:56:72}. Cevap da ateşin ne olduğunu söyler: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةً وَمَتَٰعًا لِّلْمُقْوِينَ, tr:nahnu ce'alnâhâ tezkireten ve metâ'an li'l-mukvîn, gloss:onu bir hatırlatma ve çölde konaklayanlar için bir geçim aracı yaptık, source:56:73}. Buradaki "tûrûn", ikinci ayetin "mûriyât"ıyla aynı kökten, aynı fiildir. Başka bir yerde de çürümüş kemikleri kimin dirilteceğini soran adama {ar:مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌ, tr:men yuhyi'l-izâme ve hiye ramîm, gloss:çürümüşken kemikleri kim diriltecek, source:36:78} ateşle cevap verilir: {ar:ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ, tr:ellezî ce'ale lekum mine'ş-şeceri'l-ahdari nâran fe-izâ entum minhu tûkıdûn, gloss:size yeşil ağaçtan ateş çıkaran; siz de ondan yakıp duruyorsunuz, source:36:80}. İnsan kökünün "uzaktan ateş görmek" anlamı Musa'nın sahnesinde bütünüyle yaşanır. Ailesiyle yolculuk ederken Tur'un yanında bir ateş görür ve şöyle der: {ar:إِنِّىٓ ءَانَسْتُ نَارًا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ, tr:innî ânestu nâran le'allî âtîkum minhâ bi-haber, gloss:ben bir ateş gördüm; belki oradan size bir haber getiririm, source:28:29}. Bir başka anlatımda {ar:سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍ قَبَسٍ, tr:se-âtîkum minhâ bi-haberin ev âtîkum bi-şihâbin kabes, gloss:oradan size bir haber ya da yanan bir kor getireceğim, source:27:7} der. Bir başkasında ise {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Musa'nın sahnesinde uzaktan görülen ateş haber (haber, "h-b-r") ve yol göstericilikle sonuçlanır. Bu, surenin son kelimesi {ar:لَّخَبِيرٌ, tr:le-habîr, gloss:her şeyden haberdardır, source:100:11} ile aynı köktür.

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

===== passages from the discovery list (142) =====
## strong (53)

- (3:10) [terra: strong; basis: scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ
  Unverified discovery rationale: terra: Wealth cannot benefit its owners against God and they become fuel for the Fire, tightly joining prized possessions, failed benefit, and fire.
- (3:14) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section links the fire-name نار الحباحب to 100:8’s حُبّ الخير; this verse names “الخيل المسومة” among the worldly desires people love, placing the horse scene beside wealth and attachment. | terra: The love of desires is adorned through gold, silver, and marked horses among other possessions, directly joining the ح ب ب family, prized wealth, and horses in one ayah.
- (6:96) [luna: strong; terra: strong; basis: contrast+root+scene+theme] فَالِقُ ٱلْإِصْبَاحِ وَجَعَلَ ٱلَّيْلَ سَكَنًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ حُسْبَانًۭا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ
  Unverified discovery rationale: luna: The section’s dictionary form الصباح means daylight and its prose says morning replaces darkness; here God is “فالق الإصباح” and makes night for rest, directly placing dawn against night. | terra: God is فَالِقُ الْإِصْبَاحِ and appoints night for rest; the same ص ب ح family presents dawn as a divinely opened boundary after darkness.
- (9:35) [terra: strong; basis: neighbour+scene+theme] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
  Unverified discovery rationale: terra: Hoarded gold and silver are heated in Hell and used to brand bodies, joining love of wealth to the source's sense of fire scorching or branding what it touches.
- (13:17) [luna: medium; terra: strong; basis: contrast+scene+theme] أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا ۚ وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْحَقَّ وَٱلْبَٰطِلَ ۚ فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ ۚ كَذَٰلِكَ يَضْرِبُ ٱللَّهُ ٱلْأَمْثَالَ
  Unverified discovery rationale: luna: This describes material heated “في النار” for adornment or use, then distinguishes foam that vanishes from what benefits people and stays; it develops the section’s contrast between useless airborne sparks or ash and lasting benefit. | terra: Metal is heated in fire, useless scum rises, and what benefits people remains; the verse gives the image's fleeting spark versus useful result a precise material analogue.
- (14:18) [luna: strong; terra: strong; basis: scene+theme] مَّثَلُ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ ۖ لَّا يَقْدِرُونَ مِمَّا كَسَبُوا۟ عَلَىٰ شَىْءٍۢ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
  Unverified discovery rationale: luna: The section’s dictionary branch calls the remains of fire “الرماد”; here rejecters’ deeds are compared to ash scattered by storm wind, extending the physical residue into an image of effort with no lasting gain. | terra: The deeds of rejecters become ashes driven violently by wind, making the source dictionary's dabh-as-ash into an image of an effort from which nothing can be retained.
- (17:12) [luna: medium; terra: strong (missing-ayat turn); basis: contrast+scene+theme] وَجَعَلْنَا ٱلَّيْلَ وَٱلنَّهَارَ ءَايَتَيْنِ ۖ فَمَحَوْنَآ ءَايَةَ ٱلَّيْلِ وَجَعَلْنَآ ءَايَةَ ٱلنَّهَارِ مُبْصِرَةًۭ لِّتَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ وَلِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ ۚ وَكُلَّ شَىْءٍۢ فَصَّلْنَٰهُ تَفْصِيلًۭا
  Unverified discovery rationale: luna: The section sets a brief spark against morning light that lets people see; this verse says the night’s sign was effaced and the day’s made visible so people can see and seek provision. | terra: God erases the sign of night and makes the sign of day visible so people can seek bounty and reckon time, giving durable daylight the usefulness the section's instant sparks lack.
- (17:50) [terra: strong; basis: scene+theme] ۞ قُلْ كُونُوا۟ حِجَارَةً أَوْ حَدِيدًا
  Unverified discovery rationale: terra: “Be stones or iron” names the two materials of the section's fire-making tool inside a challenge about resurrection, joining its physical apparatus to the same proof made with fire in 36:80.
- (18:96) [luna: weak (missing-ayat turn); terra: strong; basis: scene+theme] ءَاتُونِى زُبَرَ ٱلْحَدِيدِ ۖ حَتَّىٰٓ إِذَا سَاوَىٰ بَيْنَ ٱلصَّدَفَيْنِ قَالَ ٱنفُخُوا۟ ۖ حَتَّىٰٓ إِذَا جَعَلَهُۥ نَارًۭا قَالَ ءَاتُونِىٓ أُفْرِغْ عَلَيْهِ قِطْرًۭا
  Unverified discovery rationale: luna: The section’s fire-making tool is iron struck against stone; here iron is worked until it is heated like fire and molten metal is poured over it. The link is the iron-and-fire craft, though this ayah builds a barrier rather than making a spark. | terra: Iron blocks are blown upon until they become fire-hot, then covered with molten metal; iron, force, heat, and a useful finished work recast the section's physical ignition scene.
- (20:10) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶17] إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى
  Unverified discovery rationale: luna: The section’s root ء ن س appears in “إني آنست نارا”; Moses hopes either for a firebrand or “هدى” there, making the distant fire a possible practical aid and guide. | terra: Moses's إِنِّي آنَسْتُ نَارًا leads him to seek a firebrand or guidance at the fire, realizing both the source's ء ن س sense and its question of what a spark will become.
- (20:11) [luna: strong; terra: strong; basis: neighbour+scene+speaker] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
  Unverified discovery rationale: luna: This is the next moment after Moses reaches the fire in 20:10: he is called by name, and the hoped-for sign becomes an address. | terra: When Moses reaches the fire he is called by name, the first concrete fulfilment of the guidance he hoped to find in 20:10.
- (20:12) [luna: strong; terra: medium (missing-ayat turn); basis: neighbour+scene+speaker] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
  Unverified discovery rationale: luna: The call at the fire continues with an instruction to remove his sandals because he is in the sacred valley; it locates the guidance Moses hoped to find. | terra: The voice at the fire tells Moses to remove his sandals because he is in the sacred valley Tuwa, identifying the fire-site as holy rather than merely a place to collect an ember.
- (20:13) [luna: strong; terra: medium; basis: neighbour+speaker+theme] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
  Unverified discovery rationale: luna: The same encounter tells Moses he has been chosen and must listen to revelation, giving concrete content to the “هدى” sought at the fire in 20:10. | terra: After the call at the fire, God chooses Moses and commands him to listen to revelation, specifying the guidance that 20:10 only anticipated.
- (20:14) [luna: strong; terra: medium; basis: neighbour+speaker+theme] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
  Unverified discovery rationale: luna: The call identifies Allah and commands worship and prayer for remembrance; this is the guidance that follows Moses’ search at the fire. | terra: The guidance found at the fire becomes recognition of God, worship, and remembrance, giving the distant light a durable human consequence.
- (20:15) [luna: strong (missing-ayat turn); basis: neighbour+theme] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
  Unverified discovery rationale: luna: The fire encounter’s speech continues from the guidance Moses seeks in 20:10: this ayah says the Hour is coming and each soul is recompensed for its striving, meeting the section’s dictionary sense of a kindled undertaking reaching its aim.
- (20:97) [terra: strong; basis: scene+theme] قَالَ فَٱذْهَبْ فَإِنَّ لَكَ فِى ٱلْحَيَوٰةِ أَن تَقُولَ لَا مِسَاسَ ۖ وَإِنَّ لَكَ مَوْعِدًۭا لَّن تُخْلَفَهُۥ ۖ وَٱنظُرْ إِلَىٰٓ إِلَٰهِكَ ٱلَّذِى ظَلْتَ عَلَيْهِ عَاكِفًۭا ۖ لَّنُحَرِّقَنَّهُۥ ثُمَّ لَنَنسِفَنَّهُۥ فِى ٱلْيَمِّ نَسْفًا
  Unverified discovery rationale: terra: Moses burns the calf and then scatters it into the sea, a complete Quranic movement from burning an object to dispersing what remains.
