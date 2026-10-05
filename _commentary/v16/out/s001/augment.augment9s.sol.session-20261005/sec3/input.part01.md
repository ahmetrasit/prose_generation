Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 3 of 14 ("Hesap günü: hükümdar, ayağa kalkanlar, borç ve eğilmeyen terazi"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 3 (prose paragraphs numbered) =====
[¶15] Dördüncü ayet bütün bir sahneyi üç kelimede taşır: {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}. Bu ayet bizzat açıklanmıştır: {ar:الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء, tr:ed-dînü'l-hisâb, ve minhü mâliki yevmi'd-dîn, gloss:din hesaptır; "din gününün sahibi", yani karşılık gününün sahibi de buradandır, source:"د ي ن,B002"}. Üç unsur sırayla açıklanabilir: {ar:يوم الدين أي يوم الحكم والحساب والجزاء, tr:yevmü'd-dîn: yevmü'l-hukmi ve'l-hisâbi ve'l-cezâ, gloss:din günü, hüküm, hesap ve karşılık günüdür, source:"د ي ن,B002"}.

[¶16] Gün bu sahnede bir zaman aralığı olmanın ötesinde, insanların başına gelen bir olaydır: {ar:اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت, tr:el-yevm: el-kevn, el-kâinetü izâ nezelet ev hadeset, gloss:gün, inip gelen ya da meydana gelen olaydır, source:"ي و م,B003"}. Böyle bir gün ağırdır: {ar:اليوم الشديد: يوم ذو أيام, tr:el-yevmü'ş-şedîd: yevmün zû eyyâm, gloss:şiddetli gün, içinde birçok gün taşıyan gündür, source:"ي و م,B003"}. Kur'an'ın bu sahne için en çok kullandığı söz de bu kelimeden kurulur: {ar:يركب يوم مع إذ، فيقال: يومئذ, tr:yürakkebü yevmün mea iz, fe-yükâlü yevmeizin, gloss:"yevm" kelimesi "iz" ile birleşir ve "yevmeizin", yani o gün denir, source:"ي و م,B005"}. Hükümdar ise emir verip yasaklayan ve eli güçlü olan kişidir: {ar:الملك هو المتصرف بالأمر والنهي في الجمهور, tr:el-melikü hüve'l-mütesarrifü bi'l-emri ve'n-nehy, gloss:melik, topluluk üzerinde emir ve yasakla tasarruf edendir, source:"م ل ك,B003"}. Kelimenin kökündeki anlam elin sağlamlığıdır: {ar:لأن يده فيه قوية صحيحة, tr:li-enne yedehû fîhi kaviyyetün sahîha, gloss:çünkü onun üzerindeki eli güçlü ve sağlamdır, source:"م ل ك,B003"}.

[¶17] Altıncı ayetteki "müstakîm" kelimesinin kökü bu sahneye ayağa kalkışı ekler: {ar:القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم, tr:el-kıyâmetü yevmü'l-ba's, yevmün yekûmü fîhi'l-halku beyne yedeyi'l-hayyi'l-kayyûm, gloss:kıyamet diriliş günüdür; yaratılmışlar o gün diri ve her şeyi ayakta tutanın önünde ayağa kalkar, source:"ق و م,B013"}. Her şeyi ayakta tutan da aynı köktendir: {ar:القيوم القائم على كل شيء, tr:el-kayyûmü'l-kâimü alâ kulli şey', gloss:kayyûm, her şeyin başında duran ve onu gözetendir, source:"ق و م,B004"}. Yedinci ayetteki {ar:ٱلْمَغْضُوبِ عَلَيْهِمْ, tr:el-magdûbi aleyhim, gloss:gazaba uğramışlar, source:1:7} ifadesindeki gazap, Allah için kullanıldığında cezalandırmadır: {ar:وإذا وصف الله تعالى به فالمراد به الانتقام, tr:ve izâ vusıfallâhu teâlâ bihî fe'l-murâdü bihi'l-intikâm, gloss:Allah bununla nitelendiğinde kastedilen cezalandırmadır, source:"غ ض ب,B001"}.

[¶18] Aynı kökte bir alışveriş sahnesi de vardır. Ayetteki kelime esreli "dîn"dir. Borç anlamındaki kelime ise üstünle okunan "deyn"dir. İkisi aynı kök harflerini paylaşır, fakat aynı kelime değildir. Borç alınıp verilir ve belli bir vadeye kadar ertelenir: {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn, ve dâyentü fülânen izâ âmeltühû deynen, gloss:borç; biriyle ya alarak ya vererek borçlu alışveriş yapmak, source:"د ي ن,B003"}, {ar:الدين واحد الديون وتداينوا تبايعوا بالدين, tr:ed-deynü vâhidü'd-düyûn, ve tedâyenû: tebâye'û bi'd-deyn, gloss:deyn borçların tekilidir; tedâyenû, veresiye alışveriş ettiler demektir, source:"د ي ن,B003"}. Ayetteki "dîn" ise bu borcun kapanışını hatırlatır: {ar:الدين الجزاء والمكافأة, tr:ed-dînü'l-cezâü ve'l-mükâfee, gloss:din, karşılık ve denk ödemedir, source:"د ي ن,B002"}. "Müstakîm" kelimesinin ailesi bu sahneye fiyatı ve teraziyi getirir: {ar:القيمة ثمن الشيء بالتقويم, tr:el-kıymetü semenü'ş-şey'i bi't-takvîm, gloss:kıymet, bir şeyin biçilerek belirlenen fiyatıdır, source:"ق و م,B010"}. Fiyatın mantığı da aynı köktedir: {ar:أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك, tr:aslü'l-kıymeti'l-vâv, ve asluhû enneke tukîmü hâzâ mekâne zâk, gloss:kıymetin aslı, birini öbürünün yerine koymandır, source:"ق و م,B007"}. Ağırlığı tam olan sikke de bu kökle anılır: {ar:دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح, tr:dînârun kâimün izâ kâne miskâlen sevâen lâ yerceh, gloss:"kâim" dinar, ağırlığı tam olan ve teraziyi bir yana eğmeyen dinardır, source:"ق و م,B015"}.

[¶19] Yedinci ayetteki {ar:غَيْرِ, tr:gayri, gloss:-den başka, değil, source:1:7} kelimesinin kökü, ayetteki "başka" anlamının yanında kan bedelini taşır: {ar:غارني الرجل إذا وداك من الدية والاسم الغِيرة, tr:gâranî'r-racülü izâ vedâke mine'd-diye, gloss:adam bana kan bedeli ödedi; adı gıyredir, source:"غ ي ر,B002"}. Bu kökte kısasın bedele çevrilmesi de anlatılır: {ar:قود فغير إلى الدية, tr:kavedün fe-güyyira ile'd-diye, gloss:kısas gerekiyordu, fakat kan bedeline çevrildi, source:"غ ي ر,B003"}. Bir şeyi başkasıyla takas etmek de bu köktendir: {ar:غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال, tr:gâyertü'r-racüle, gloss:adamla mal karşılığında mal değiştirdim, source:"غ ي ر,B003"}. Ayetin son kelimesi bu sahnenin kötü sonunu taşır: {ar:ذهب دمه ضلة إذا لم يثأر به, tr:zehebe demühû dılleten, gloss:kanı boşa gitti, öcü alınmadı, source:"ض ل ل,B003"}. Borcun tanığının unutması da aynı kelimeyle söylenir: {ar:أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها, tr:en tadılle ihdâhümâ, gloss:birinin "dalâl"i, yani olayın hafızasından kaybolması ya da hafızasının kendisinden kaybolması, source:"ض ل ل,B004"}.

[¶20] Düz bir meal "hesap gününün sahibi" der. Görüntü ise bu hesabın nasıl işlediğini gösterir: vadesi gelen borç, hiçbir yana eğilmeyen terazi, ağırlığı tam sikke ve bir şeyin yerine konan bedel. Altıncı ayetteki "dosdoğru" sözü, "tam tartan" sözüyle aynı kökten duyulur. Bu yüzden sure hem doğru yolu hem eğilmeyen teraziyi aynı kök üzerinden anar.

[¶21] Kur'an'daki sahneler bu kelimeleri ayetlerinde taşır. Bir yerde gün iki kez sorulur: {ar:وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:ve mâ edrâke mâ yevmü'd-dîn, gloss:din gününün ne olduğunu sana ne bildirdi, source:82:17}. Hemen ardından mülkiyet bütünüyle el değiştirir: {ar:يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا ۖ وَٱلْأَمْرُ يَوْمَئِذٍۢ لِّلَّهِ, tr:yevme lâ temlikü nefsün li-nefsin şey'â, ve'l-emru yevmeizin lillâh, gloss:o gün hiçbir kimse bir başkası için hiçbir şeye sahip olamaz; o gün emir Allah'ındır, source:82:19}. "Mâlik" kelimesinin kökü burada sahipliğin herkesten alınmasını söyler. O gün kimse gözden kaybolamaz: {ar:وَمَا هُمْ عَنْهَا بِغَآئِبِينَ, tr:ve mâ hüm anhâ bi-gâibîn, gloss:oradan da uzak kalamazlar, source:82:16}. Ölçüde hile yapanlar sahnesinde terazi ve gün tek bir yerde birleşir. Önce {ar:وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ, tr:ve izâ kâlûhüm ev vezenûhüm yuhsirûn, gloss:onlara ölçüp tarttıklarında ise eksik verirler, source:83:3} denir. Ardından şu söylenir: {ar:يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ, tr:yevme yekûmü'n-nâsü li-rabbi'l-âlemîn, gloss:insanların âlemlerin Rabbi için ayağa kalkacağı gün, source:83:6}. Eğri tartıyla "ayağa kalkış" aynı kökten konuşur. İkinci ayetin "âlemlerin Rabbi"si de bu sahnenin içindedir. Kur'an hükümranlığı o güne bağlayıp sorar: {ar:لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ, tr:li-meni'l-mülkü'l-yevm, lillâhi'l-vâhidi'l-kahhâr, gloss:bugün mülk kimindir? Bir ve kahredici Allah'ın, source:40:16}. Başka bir yerde aynı mülk surenin üçüncü ayetindeki adla anılır: {ar:ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ, tr:el-mülkü yevmeizini'l-hakku li'r-rahmân, gloss:o gün gerçek mülk Rahman'ındır, source:25:26}. Böylece üçüncü ve dördüncü ayetler tek cümlede birleşir. Terazi de o güne konur: {ar:وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ, tr:ve neda'u'l-mevâzîne'l-kıste li-yevmi'l-kıyâme, gloss:kıyamet günü için adalet terazileri kurarız, source:21:47}, {ar:وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا, tr:ve in kâne miskâle habbetin min hardelin eteynâ bihâ, gloss:bir hardal tanesi ağırlığında da olsa onu getiririz, source:21:47}. Terazinin iki ucu ayrı ayrı gösterilir: {ar:فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:fe-emmâ men sekulet mevâzînüh, gloss:tartıları ağır gelen, source:101:6} ve {ar:وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve emmâ men haffet mevâzînüh, gloss:tartıları hafif gelen, source:101:8}.

[¶22] Dünyadaki borç ayeti bu görüntünün bütün parçalarını içerir: {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belli bir vadeye kadar borçlandığınızda onu yazın, source:2:282}. Aynı ayette unutan tanık da vardır: {ar:أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ, tr:en tadılle ihdâhümâ fe-tüzekkira ihdâhümel-uhrâ, gloss:biri unutursa öbürü ona hatırlatsın diye, source:2:282}. Yazmanın gerekçesi aynı kökten bir sıfatla söylenir: {ar:ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ, tr:zâliküm aksatu indallâhi ve akvemü li'ş-şehâde, gloss:bu, Allah katında daha adil ve şahitlik için daha sağlamdır, source:2:282}. Böylece borç, unutkanlık ve "akvem" sıfatı tek bir ayette bir araya gelir. Terazi, surenin sıfatıyla iki kez nitelenir. Bunlardan biri, Medyen halkına Şuayb'ın dilinden söylenen sözdür: {ar:وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:ve zinû bi'l-kıstâsi'l-müstakîm, gloss:dosdoğru terazi ile tartın, source:26:182}. Aynı söz bir başka yerde de tekrarlanır {source:17:35}. Kan bedeli konusunda öldürülenin yakını bağışlarsa {ar:فَٱتِّبَاعٌۢ بِٱلْمَعْرُوفِ وَأَدَآءٌ إِلَيْهِ بِإِحْسَٰنٍۢ, tr:fe-ttibâun bi'l-ma'rûfi ve edâün ileyhi bi-ihsân, gloss:iyilikle takip, güzellikle ödeme gerekir, source:2:178} denir. Hataen öldürmede ise {ar:وَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦٓ, tr:ve diyetün müselletün ilâ ehlih, gloss:ailesine teslim edilecek bir kan bedeli, source:4:92} gerekir. O günde ise bedelin kabul edilmediği söylenir: {ar:وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ, tr:ve in ta'dil külle adlin lâ yü'haz minhâ, gloss:her türlü fidyeyi verse de ondan alınmaz, source:6:70}. "Bir şeyi başkasının yerine koymak" o gün işlemez. Kötü takasın Kur'an'daki sahnesi şudur: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ فَمَا رَبِحَت تِّجَٰرَتُهُمْ, tr:ülâike'llezîne'şteravu'd-dalâlete bi'l-hudâ fe-mâ rabihat ticâratühüm, gloss:onlar hidayete karşılık sapıklığı satın alanlardır, ticaretleri kazanç getirmedi, source:2:16}. Burada surenin iki ucu, hidayet ve dalâlet, bir alışverişin iki tarafı olur. Bu günün kaçınılmaz olduğu da söylenir: {ar:وَإِنَّ ٱلدِّينَ لَوَٰقِعٌۭ, tr:ve inne'd-dîne le-vâki', gloss:karşılık mutlaka gerçekleşecektir, source:51:6}. "Vâki'", inip gelen gün tanımına uyar. İbrahim de bu güne bakarak konuşur: {ar:وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ, tr:ve'llezî atmau en yağfira lî hatîetî yevme'd-dîn, gloss:din günü hatamı bağışlamasını umduğum O'dur, source:26:82}.

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

===== passages from the discovery list (328) =====
## strong (232)

- (2:16) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶22] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ فَمَا رَبِحَت تِّجَٰرَتُهُمْ وَمَا كَانُوا۟ مُهْتَدِينَ
  Unverified discovery rationale: luna: The section says guidance and misguidance become the two sides of a failed trade. “اشْتَرَوُا الضَّلَالَةَ بِالْهُدَىٰ” names that exact exchange and says the trade brought no profit. | terra: They buy error (ٱلضَّلَٰلَةَ) for guidance, and their trade does not profit: the surah's huda and dalālah become the two sides of a bad exchange.
- (2:48) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَٱتَّقُوا۟ يَوْمًۭا لَّا تَجْزِى نَفْسٌ عَن نَّفْسٍۢ شَيْـًۭٔا وَلَا يُقْبَلُ مِنْهَا شَفَٰعَةٌۭ وَلَا يُؤْخَذُ مِنْهَا عَدْلٌۭ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: luna: This ayah says no soul can pay for another and no ransom or intercession is accepted. It sets the final boundary on the section's worldly debt and substitution images: one cannot settle another's account on that day. | terra: Fear the day when no soul can compensate for another and no ransom or intercession is accepted; it is a direct boundary on paying another's debt.
- (2:86) [terra: strong; basis: contrast+scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: terra: They purchase the nearer life with the Hereafter; the transaction loses the final life for immediate value.
- (2:90) [terra: strong (missing-ayat turn); basis: root+theme] بِئْسَمَا ٱشْتَرَوْا۟ بِهِۦٓ أَنفُسَهُمْ أَن يَكْفُرُوا۟ بِمَآ أَنزَلَ ٱللَّهُ بَغْيًا أَن يُنَزِّلَ ٱللَّهُ مِن فَضْلِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۖ فَبَآءُو بِغَضَبٍ عَلَىٰ غَضَبٍۢ ۚ وَلِلْكَٰفِرِينَ عَذَابٌۭ مُّهِينٌۭ
  Unverified discovery rationale: terra: Its bad purchase of themselves brings wrath upon wrath for rejecting revelation, fusing corrupt exchange with divine غضب.
- (2:123) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَٱتَّقُوا۟ يَوْمًۭا لَّا تَجْزِى نَفْسٌ عَن نَّفْسٍۢ شَيْـًۭٔا وَلَا يُقْبَلُ مِنْهَا عَدْلٌۭ وَلَا تَنفَعُهَا شَفَٰعَةٌۭ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: luna: This ayah repeats the boundary that no soul is compensated for another and no ransom is taken. Its separate warning reinforces that the section's final account cannot be transferred or paid off by someone else. | terra: Its second warning that no soul avails another and no compensation is accepted reinforces the nontransferable final account.
- (2:175) [terra: strong; basis: root+scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ وَٱلْعَذَابَ بِٱلْمَغْفِرَةِ ۚ فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ
  Unverified discovery rationale: terra: They exchange guidance for error and forgiveness for punishment, a second explicit market scene of disastrous moral valuation.
- (2:178) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶22] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُتِبَ عَلَيْكُمُ ٱلْقِصَاصُ فِى ٱلْقَتْلَى ۖ ٱلْحُرُّ بِٱلْحُرِّ وَٱلْعَبْدُ بِٱلْعَبْدِ وَٱلْأُنثَىٰ بِٱلْأُنثَىٰ ۚ فَمَنْ عُفِىَ لَهُۥ مِنْ أَخِيهِ شَىْءٌۭ فَٱتِّبَاعٌۢ بِٱلْمَعْرُوفِ وَأَدَآءٌ إِلَيْهِ بِإِحْسَٰنٍۢ ۗ ذَٰلِكَ تَخْفِيفٌۭ مِّن رَّبِّكُمْ وَرَحْمَةٌۭ ۗ فَمَنِ ٱعْتَدَىٰ بَعْدَ ذَٰلِكَ فَلَهُۥ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: luna: The section's source dictionary branch says retaliation can be changed into blood compensation. This ayah describes pardon in a killing followed by fair pursuit and payment, “فَاتِّبَاعٌ بِالْمَعْرُوفِ وَأَدَاءٌ إِلَيْهِ بِإِحْسَانٍ,” making that conversion concrete. | terra: After intentional killing, pardon requires fair following and gracious payment; it is the qisas-to-payment turn developed under غَيْر.
- (2:179) [luna: medium (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: luna: After 2:178's retaliation and blood-payment rules, this ayah says there is life in qisas. It completes the legal scene by explaining the boundary's protective purpose. | terra: Retaliation contains life, explaining why the legal equivalence beside 2:178 is neither arbitrary vengeance nor a lost blood claim.
- (2:254) [terra: strong; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِمَّا رَزَقْنَٰكُم مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا بَيْعٌۭ فِيهِ وَلَا خُلَّةٌۭ وَلَا شَفَٰعَةٌۭ ۗ وَٱلْكَٰفِرُونَ هُمُ ٱلظَّٰلِمُونَ
  Unverified discovery rationale: terra: Spend before a day with no trade or intercession; ordinary exchange closes before the Day's reckoning.
