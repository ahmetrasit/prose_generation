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
- (2:255) [luna: strong; terra: strong; basis: root+theme] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
  Unverified discovery rationale: luna: The section names al-Qayyūm and glosses it from source root q-w-m as the one who sustains and oversees everything. This ayah uses the exact title “الْحَيُّ الْقَيُّومُ,” anchoring that secondary dictionary sense in Quranic wording. | terra: Allah is al-Ḥayy al-Qayyūm (ٱلْقَيُّومُ), the one standing over and sustaining all things in the q-w-m sense developed by the section.
- (2:278) [terra: strong (missing-ayat turn); basis: neighbour+scene] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَذَرُوا۟ مَا بَقِىَ مِنَ ٱلرِّبَوٰٓا۟ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: terra: Believers are told to leave what remains of usury, beginning the debt passage whose final settlement appears in 2:280-281.
- (2:279) [terra: strong (missing-ayat turn); basis: neighbour+root+scene+theme] فَإِن لَّمْ تَفْعَلُوا۟ فَأْذَنُوا۟ بِحَرْبٍۢ مِّنَ ٱللَّهِ وَرَسُولِهِۦ ۖ وَإِن تُبْتُمْ فَلَكُمْ رُءُوسُ أَمْوَٰلِكُمْ لَا تَظْلِمُونَ وَلَا تُظْلَمُونَ
  Unverified discovery rationale: terra: Taking only the principal means neither wronging nor being wronged, a monetary form of equal measure beside 2:280-281.
- (2:280) [terra: strong; basis: root+scene] وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: A debtor in hardship is granted deferment, making the section's due date and debt settlement a lived ethical scene.
- (2:281) [terra: strong; basis: scene+theme] وَٱتَّقُوا۟ يَوْمًۭا تُرْجَعُونَ فِيهِ إِلَى ٱللَّهِ ۖ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: terra: Return to Allah on a day when every soul is paid in full what it earned, and none is wronged.
- (2:282) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶22] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: luna: This ayah gathers the section's worldly debt scene: “بِدَيْنٍ إِلَىٰ أَجَلٍ مُّسَمًّى” is a loan due at a term, “تَضِلَّ إِحْدَاهُمَا” is a witness's lapse, and “أَقْوَمُ لِلشَّهَادَةِ” uses the section's source root q-w-m for sound testimony. | terra: It joins a fixed-term debt, writing, a witness who may forget (تَضِلَّ), and the description أَقْوَمُ for sounder testimony; the section's debt, memory, and q-w-m balance occur together.
- (2:283) [terra: strong; basis: root+scene+theme] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
  Unverified discovery rationale: terra: Its pledge, entrusted party, and warning not to conceal testimony extend 2:282's debt contract and accountable witness.
- (2:284) [terra: strong (missing-ayat turn); basis: neighbour+theme] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: After the written-debt instruction, Allah brings people to account for what they reveal or conceal, then forgives or punishes.
- (3:2) [luna: strong; terra: strong; basis: root+theme] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ
  Unverified discovery rationale: luna: This ayah repeats the title “الْحَيُّ الْقَيُّومُ” that the section explains from source root q-w-m as the one standing over all things; it is a second direct occurrence of that named attribute. | terra: It repeats al-Ḥayy al-Qayyūm, reinforcing that the one before whom creatures stand is Himself the sustainer.
- (3:18) [luna: medium; terra: strong; basis: root+theme] شَهِدَ ٱللَّهُ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا هُوَ وَٱلْمَلَٰٓئِكَةُ وَأُو۟لُوا۟ ٱلْعِلْمِ قَآئِمًۢا بِٱلْقِسْطِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The section links source root q-w-m in mustaqīm to uprightness and a just scale. This ayah calls God “قَائِمًا بِالْقِسْطِ,” bringing standing and justice together in one formulation. | terra: Allah stands maintaining justice (قَائِمًا بِٱلْقِسْطِ), a divine q-w-m expression that unites standing with the section's just balance.
- (3:25) [terra: strong; basis: scene+theme] فَكَيْفَ إِذَا جَمَعْنَٰهُمْ لِيَوْمٍۢ لَّا رَيْبَ فِيهِ وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: terra: On a day without doubt every soul is paid in full for what it earned and is not wronged, a compact statement of final debt settlement.
- (3:26) [terra: strong; basis: root+theme] قُلِ ٱللَّهُمَّ مَٰلِكَ ٱلْمُلْكِ تُؤْتِى ٱلْمُلْكَ مَن تَشَآءُ وَتَنزِعُ ٱلْمُلْكَ مِمَّن تَشَآءُ وَتُعِزُّ مَن تَشَآءُ وَتُذِلُّ مَن تَشَآءُ ۖ بِيَدِكَ ٱلْخَيْرُ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: Allah is Owner of sovereignty, giving and taking dominion; it displays the powerful disposal meant by Mālik before the Day's exclusive ownership.
- (3:30) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: terra: On the day each soul finds every good and evil deed present, it wishes its evil far away; the account becomes personally visible.
- (3:77) [terra: strong; basis: contrast+scene+theme] إِنَّ ٱلَّذِينَ يَشْتَرُونَ بِعَهْدِ ٱللَّهِ وَأَيْمَٰنِهِمْ ثَمَنًۭا قَلِيلًا أُو۟لَٰٓئِكَ لَا خَلَٰقَ لَهُمْ فِى ٱلْءَاخِرَةِ وَلَا يُكَلِّمُهُمُ ٱللَّهُ وَلَا يَنظُرُ إِلَيْهِمْ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: terra: Those who sell Allah's covenant and their oaths for a small price have no share in the Hereafter and face punishment, joining corrupt exchange to the Day.
- (3:91) [luna: contrast; terra: strong; basis: contrast+scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَمَاتُوا۟ وَهُمْ كُفَّارٌۭ فَلَن يُقْبَلَ مِنْ أَحَدِهِم مِّلْءُ ٱلْأَرْضِ ذَهَبًۭا وَلَوِ ٱفْتَدَىٰ بِهِۦٓ ۗ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌ أَلِيمٌۭ وَمَا لَهُم مِّن نَّٰصِرِينَ
  Unverified discovery rationale: luna: Even earthful of gold offered as ransom “لَن يُقْبَلَ مِنْ أَحَدِهِم” for those dying in disbelief. This is a specific limit on the section's image of paying a debt or setting one thing in another's place. | terra: Even earthfuls of gold offered as ransom are not accepted from one who dies rejecting faith, showing wealth cannot settle the final due.
- (3:161) [terra: strong (missing-ayat turn); basis: scene+theme] وَمَا كَانَ لِنَبِىٍّ أَن يَغُلَّ ۚ وَمَن يَغْلُلْ يَأْتِ بِمَا غَلَّ يَوْمَ ٱلْقِيَٰمَةِ ۚ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: terra: One who misappropriates comes with what was taken on the Day of Resurrection, then every soul is paid in full without wrong.
- (3:162) [terra: strong; basis: root+theme] أَفَمَنِ ٱتَّبَعَ رِضْوَٰنَ ٱللَّهِ كَمَنۢ بَآءَ بِسَخَطٍۢ مِّنَ ٱللَّهِ وَمَأْوَىٰهُ جَهَنَّمُ ۚ وَبِئْسَ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: One who follows Allah's pleasure is contrasted with one who incurs His wrath and whose refuge is Hell, locating wrath in final consequence.
- (3:177) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] إِنَّ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْكُفْرَ بِٱلْإِيمَٰنِ لَن يَضُرُّوا۟ ٱللَّهَ شَيْـًۭٔا وَلَهُمْ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: luna: This ayah says those who “اشْتَرَوُا الْكُفْرَ بِالْإِيمَانِ” acquire no harm for God and face punishment. It repeats the section's exchange image with faith and disbelief reversed. | terra: They purchase disbelief for faith, an explicit reversal of the profitable exchange that ends in painful punishment.
- (3:187) [terra: strong (missing-ayat turn); basis: root+scene+theme] وَإِذْ أَخَذَ ٱللَّهُ مِيثَٰقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَتُبَيِّنُنَّهُۥ لِلنَّاسِ وَلَا تَكْتُمُونَهُۥ فَنَبَذُوهُ وَرَآءَ ظُهُورِهِمْ وَٱشْتَرَوْا۟ بِهِۦ ثَمَنًۭا قَلِيلًۭا ۖ فَبِئْسَ مَا يَشْتَرُونَ
  Unverified discovery rationale: terra: Those entrusted with the Book cast it behind them and sell it for a small price, a corrupt exchange of a binding due.
- (4:40) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] إِنَّ ٱللَّهَ لَا يَظْلِمُ مِثْقَالَ ذَرَّةٍۢ ۖ وَإِن تَكُ حَسَنَةًۭ يُضَٰعِفْهَا وَيُؤْتِ مِن لَّدُنْهُ أَجْرًا عَظِيمًۭا
  Unverified discovery rationale: luna: God does not wrong even “مِثْقَالَ ذَرَّةٍ” and multiplies a good deed. The exact tiny weight and denial of injustice connect the section's precise scales to God's equitable recompense. | terra: Allah does not wrong even an atom's weight and multiplies good; exact tiny weight becomes exact recompense.
- (4:44) [terra: strong (missing-ayat turn); basis: root+theme] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يَشْتَرُونَ ٱلضَّلَٰلَةَ وَيُرِيدُونَ أَن تَضِلُّوا۟ ٱلسَّبِيلَ
  Unverified discovery rationale: terra: They purchase error and want others to lose the way, directly joining bad trade to the surah contrast of guidance and dalalah.
- (4:56) [terra: strong; basis: root+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
  Unverified discovery rationale: terra: When skins are burned they are exchanged for other skins (غَيْرَهَا) so punishment continues; the section's 'other/replacement' sense meets divine punitive recompense.
- (4:92) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶22] وَمَا كَانَ لِمُؤْمِنٍ أَن يَقْتُلَ مُؤْمِنًا إِلَّا خَطَـًۭٔا ۚ وَمَن قَتَلَ مُؤْمِنًا خَطَـًۭٔا فَتَحْرِيرُ رَقَبَةٍۢ مُّؤْمِنَةٍۢ وَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦٓ إِلَّآ أَن يَصَّدَّقُوا۟ ۚ فَإِن كَانَ مِن قَوْمٍ عَدُوٍّۢ لَّكُمْ وَهُوَ مُؤْمِنٌۭ فَتَحْرِيرُ رَقَبَةٍۢ مُّؤْمِنَةٍۢ ۖ وَإِن كَانَ مِن قَوْمٍۭ بَيْنَكُمْ وَبَيْنَهُم مِّيثَٰقٌۭ فَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦ وَتَحْرِيرُ رَقَبَةٍۢ مُّؤْمِنَةٍۢ ۖ فَمَن لَّمْ يَجِدْ فَصِيَامُ شَهْرَيْنِ مُتَتَابِعَيْنِ تَوْبَةًۭ مِّنَ ٱللَّهِ ۗ وَكَانَ ٱللَّهُ عَلِيمًا حَكِيمًۭا
  Unverified discovery rationale: luna: For accidental killing, this ayah requires “دِيَةٌ مُّسَلَّمَةٌ إِلَىٰ أَهْلِهِ.” It supplies the section's exact worldly case of blood money paid to the victim's family. | terra: Accidental killing requires a diya delivered to the family, the concrete blood payment named by the section.
- (4:93) [luna: medium; terra: strong; basis: neighbour+root+theme] وَمَن يَقْتُلْ مُؤْمِنًۭا مُّتَعَمِّدًۭا فَجَزَآؤُهُۥ جَهَنَّمُ خَٰلِدًۭا فِيهَا وَغَضِبَ ٱللَّهُ عَلَيْهِ وَلَعَنَهُۥ وَأَعَدَّ لَهُۥ عَذَابًا عَظِيمًۭا
  Unverified discovery rationale: luna: The section labels its source root gh-ḍ-b and says divine anger means punishment. This ayah uses “غَضِبَ اللَّهُ عَلَيْهِ” for the intentional killer and places it alongside severe penalty, clarifying that anger here is judicial consequence. | terra: Deliberate murder brings Allah's wrath, curse, and great punishment, tying the diya passage to the section's explanation of divine غضب as punishment.
- (4:135) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+speaker+theme] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ بِٱلْقِسْطِ شُهَدَآءَ لِلَّهِ وَلَوْ عَلَىٰٓ أَنفُسِكُمْ أَوِ ٱلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ ۚ إِن يَكُنْ غَنِيًّا أَوْ فَقِيرًۭا فَٱللَّهُ أَوْلَىٰ بِهِمَا ۖ فَلَا تَتَّبِعُوا۟ ٱلْهَوَىٰٓ أَن تَعْدِلُوا۟ ۚ وَإِن تَلْوُۥٓا۟ أَوْ تُعْرِضُوا۟ فَإِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
  Unverified discovery rationale: luna: The command “كُونُوا قَوَّامِينَ بِالْقِسْطِ شُهَدَاءَ لِلَّهِ” joins standing, justice, and witness. It echoes the section's source root q-w-m, its upright measure, and the witnesses of its debt scene. | terra: Believers are told to be steadfastly standing for justice (قَوَّامِينَ بِٱلْقِسْطِ), turning the root's uprightness into impartial testimony.
- (5:8) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ لِلَّهِ شُهَدَآءَ بِٱلْقِسْطِ ۖ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ عَلَىٰٓ أَلَّا تَعْدِلُوا۟ ۚ ٱعْدِلُوا۟ هُوَ أَقْرَبُ لِلتَّقْوَىٰ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
  Unverified discovery rationale: luna: “كُونُوا قَوَّامِينَ لِلَّهِ شُهَدَاءَ بِالْقِسْطِ” commands standing as witnesses for justice, and warns not to let hatred make one unjust. This makes the section's straight path and unleaning scale an ethical stance. | terra: Be standing firm for Allah as witnesses in justice, and let hostility not make you unjust; the upright stance resists a tilted verdict.
- (5:36) [terra: strong; basis: contrast+scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَوْ أَنَّ لَهُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لِيَفْتَدُوا۟ بِهِۦ مِنْ عَذَابِ يَوْمِ ٱلْقِيَٰمَةِ مَا تُقُبِّلَ مِنْهُمْ ۖ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: terra: All the earth and its like offered to escape the Day's punishment would not be accepted; no value can substitute for the person then.
- (5:45) [luna: medium (missing-ayat turn); terra: strong; basis: scene+theme] وَكَتَبْنَا عَلَيْهِمْ فِيهَآ أَنَّ ٱلنَّفْسَ بِٱلنَّفْسِ وَٱلْعَيْنَ بِٱلْعَيْنِ وَٱلْأَنفَ بِٱلْأَنفِ وَٱلْأُذُنَ بِٱلْأُذُنِ وَٱلسِّنَّ بِٱلسِّنِّ وَٱلْجُرُوحَ قِصَاصٌۭ ۚ فَمَن تَصَدَّقَ بِهِۦ فَهُوَ كَفَّارَةٌۭ لَّهُۥ ۚ وَمَن لَّمْ يَحْكُم بِمَآ أَنزَلَ ٱللَّهُ فَأُو۟لَٰٓئِكَ هُمُ ٱلظَّٰلِمُونَ
  Unverified discovery rationale: luna: This ayah allows the injured party to remit retaliation as charity, which becomes expiation for the one who does so. It adds a distinct way the section's qisas and compensation scene can be settled. | terra: Its life-for-life equivalence and its valuation of forgiveness as charity show retaliation and remission as measured responses.
- (5:60) [terra: strong (missing-ayat turn); basis: root+theme] قُلْ هَلْ أُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكَ مَثُوبَةً عِندَ ٱللَّهِ ۚ مَن لَّعَنَهُ ٱللَّهُ وَغَضِبَ عَلَيْهِ وَجَعَلَ مِنْهُمُ ٱلْقِرَدَةَ وَٱلْخَنَازِيرَ وَعَبَدَ ٱلطَّٰغُوتَ ۚ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ
  Unverified discovery rationale: terra: Allah curse and wrath are joined to degrading punitive transformations, making divine غضب a concrete punishment.
- (6:51) [terra: strong (missing-ayat turn); basis: contrast+scene+theme] وَأَنذِرْ بِهِ ٱلَّذِينَ يَخَافُونَ أَن يُحْشَرُوٓا۟ إِلَىٰ رَبِّهِمْ ۙ لَيْسَ لَهُم مِّن دُونِهِۦ وَلِىٌّۭ وَلَا شَفِيعٌۭ لَّعَلَّهُمْ يَتَّقُونَ
  Unverified discovery rationale: terra: Those who fear being gathered before their Lord are warned that no protector or intercessor besides Him can answer for them.
- (6:57) [terra: strong (missing-ayat turn); basis: root+theme] قُلْ إِنِّى عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّى وَكَذَّبْتُم بِهِۦ ۚ مَا عِندِى مَا تَسْتَعْجِلُونَ بِهِۦٓ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۖ يَقُصُّ ٱلْحَقَّ ۖ وَهُوَ خَيْرُ ٱلْفَٰصِلِينَ
  Unverified discovery rationale: terra: Judgment belongs only to Allah, who tells the truth and is best at deciding; it realizes the ruling authority in Mālik.
- (6:62) [terra: strong (missing-ayat turn); basis: root+theme] ثُمَّ رُدُّوٓا۟ إِلَى ٱللَّهِ مَوْلَىٰهُمُ ٱلْحَقِّ ۚ أَلَا لَهُ ٱلْحُكْمُ وَهُوَ أَسْرَعُ ٱلْحَٰسِبِينَ
  Unverified discovery rationale: terra: People return to Allah, their true master; judgment is His and He is swiftest in account.
- (6:70) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] [cited in ¶22] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
  Unverified discovery rationale: luna: The section says a substitute payment cannot settle the account on that day: “وَإِن تَعْدِلْ كُلَّ عَدْلٍ لَّا يُؤْخَذْ مِنْهَا.” The same ayah uses dīn in “دِينَهُمْ” for religion, a distinct sense from the section's dīn of recompense, while showing the limit of substitution. | terra: A soul may be held for what it earned, and no ransom or equivalent payment is accepted from it: substitution fails at the final settlement.
- (6:73) [terra: strong; basis: root+scene] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
  Unverified discovery rationale: terra: His is the dominion on the day the trumpet is blown, another direct declaration of sovereignty at the event of judgment.
- (6:152) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+speaker+theme] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۖ وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَا ۖ وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ ۖ وَبِعَهْدِ ٱللَّهِ أَوْفُوا۟ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: luna: The command to give full measure and weight with justice makes the section's upright scale a rule for ordinary dealings; it adds that even weighing is part of God's covenantal guidance. | terra: Give full measure and weight with justice, a direct command for the full and even weighing pictured in the section.
- (6:160) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: scene+theme] مَن جَآءَ بِٱلْحَسَنَةِ فَلَهُۥ عَشْرُ أَمْثَالِهَا ۖ وَمَن جَآءَ بِٱلسَّيِّئَةِ فَلَا يُجْزَىٰٓ إِلَّا مِثْلَهَا وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: luna: A good deed receives tenfold, while an evil deed receives only its equivalent and no one is wronged. This states the proportionate recompense that the section's balance image makes visible. | terra: A good deed receives tenfold and an evil deed only its like, with no wrong done: recompense is explicitly proportioned.
- (7:6) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] فَلَنَسْـَٔلَنَّ ٱلَّذِينَ أُرْسِلَ إِلَيْهِمْ وَلَنَسْـَٔلَنَّ ٱلْمُرْسَلِينَ
  Unverified discovery rationale: terra: Allah will question both those sent and the communities sent to, beginning the inquiry before the weighing in 7:8-9.
- (7:7) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] فَلَنَقُصَّنَّ عَلَيْهِم بِعِلْمٍۢ ۖ وَمَا كُنَّا غَآئِبِينَ
  Unverified discovery rationale: terra: He will recount their deeds with knowledge, supplying the informed account for the scales that follow.
- (7:8) [luna: strong; terra: strong; basis: root+scene+theme] وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
  Unverified discovery rationale: luna: “وَالْوَزْنُ يَوْمَئِذٍ الْحَقُّ” explicitly says weighing on that day is true; it supplies another direct formulation of the section's judgment day as an exact, just measure. | terra: The weighing on that day is truth itself; heavy scales lead to success, directly complementing the full-weight coin.
- (7:9) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَظْلِمُونَ
  Unverified discovery rationale: luna: This next weighing-scene ayah says those whose scales are light have lost themselves through wronging God's signs, giving a distinct consequence of the imbalance named in 7:8. | terra: Those whose scales are light lose themselves, giving the adverse end of deficient weight and misvaluation.
- (7:85) [luna: strong; terra: strong; basis: root+scene+speaker+theme] وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ فَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
  Unverified discovery rationale: luna: Shuʿayb tells Midian to give full measure and weight. This is another concrete worldly standard against which the section's just final scales can be understood. | terra: Shu'ayb commands full measure and balance with justice and forbids depriving people of their goods, joining commerce to moral account.
- (9:9) [terra: strong (missing-ayat turn); basis: root+scene+theme] ٱشْتَرَوْا۟ بِـَٔايَٰتِ ٱللَّهِ ثَمَنًۭا قَلِيلًۭا فَصَدُّوا۟ عَن سَبِيلِهِۦٓ ۚ إِنَّهُمْ سَآءَ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: They sell Allah signs for a small price and turn from His way, another explicit trade that produces dalalah.
- (10:54) [terra: strong; basis: contrast+scene+theme] وَلَوْ أَنَّ لِكُلِّ نَفْسٍۢ ظَلَمَتْ مَا فِى ٱلْأَرْضِ لَٱفْتَدَتْ بِهِۦ ۗ وَأَسَرُّوا۟ ٱلنَّدَامَةَ لَمَّا رَأَوُا۟ ٱلْعَذَابَ ۖ وَقُضِىَ بَيْنَهُم بِٱلْقِسْطِ ۚ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: terra: Every wrongdoer would ransom with all the earth, but judgment is made with justice; it directly opposes a purchasable escape from account.
- (10:61) [luna: strong (missing-ayat turn); basis: scene+theme] وَمَا تَكُونُ فِى شَأْنٍۢ وَمَا تَتْلُوا۟ مِنْهُ مِن قُرْءَانٍۢ وَلَا تَعْمَلُونَ مِنْ عَمَلٍ إِلَّا كُنَّا عَلَيْكُمْ شُهُودًا إِذْ تُفِيضُونَ فِيهِ ۚ وَمَا يَعْزُبُ عَن رَّبِّكَ مِن مِّثْقَالِ ذَرَّةٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ وَلَآ أَصْغَرَ مِن ذَٰلِكَ وَلَآ أَكْبَرَ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍ
  Unverified discovery rationale: luna: The ayah says no “مِثْقَالِ ذَرَّةٍ” is absent from the Lord in earth or heaven. It joins the section's claim that no one is absent from the day to its insistence that no measure is too small to be known.
- (11:84) [terra: strong; basis: neighbour+root+scene] ۞ وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا ۚ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ وَلَا تَنقُصُوا۟ ٱلْمِكْيَالَ وَٱلْمِيزَانَ ۚ إِنِّىٓ أَرَىٰكُم بِخَيْرٍۢ وَإِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍۢ مُّحِيطٍۢ
  Unverified discovery rationale: terra: Shu'ayb's warning to Madyan to worship Allah begins the passage whose concrete test is complete measure and balance.
- (11:85) [luna: strong; terra: strong; basis: root+scene+speaker+theme] وَيَٰقَوْمِ أَوْفُوا۟ ٱلْمِكْيَالَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: luna: Shuʿayb commands, “أَوْفُوا الْمِكْيَالَ وَالْمِيزَانَ بِالْقِسْطِ.” The ayah joins measure, balance, and justice in ordinary dealings, the same fairness the section pictures at judgment. | terra: Give full measure and balance with justice and do not diminish people's things, another direct earthly instance of the section's unbent scale.
- (12:40) [terra: strong (missing-ayat turn); basis: root+speaker] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
  Unverified discovery rationale: terra: Judgment belongs only to Allah, and He commands worship of none but Him; sovereign judgment issues the command described in the section.
- (13:18) [luna: contrast; terra: strong; basis: contrast+scene+theme] لِلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمُ ٱلْحُسْنَىٰ ۚ وَٱلَّذِينَ لَمْ يَسْتَجِيبُوا۟ لَهُۥ لَوْ أَنَّ لَهُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لَٱفْتَدَوْا۟ بِهِۦٓ ۚ أُو۟لَٰٓئِكَ لَهُمْ سُوٓءُ ٱلْحِسَابِ وَمَأْوَىٰهُمْ جَهَنَّمُ ۖ وَبِئْسَ ٱلْمِهَادُ
  Unverified discovery rationale: luna: Those who do not answer their Lord would offer all the earth and its like as ransom, but face an evil account. It extends the section's denied-substitution boundary to an imagined unlimited payment. | terra: Wrongdoers would offer the earth and its like as ransom, yet receive the worst account and Hell: value cannot purchase a different verdict.
- (13:33) [luna: strong; basis: root+scene+theme] أَفَمَنْ هُوَ قَآئِمٌ عَلَىٰ كُلِّ نَفْسٍۭ بِمَا كَسَبَتْ ۗ وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ قُلْ سَمُّوهُمْ ۚ أَمْ تُنَبِّـُٔونَهُۥ بِمَا لَا يَعْلَمُ فِى ٱلْأَرْضِ أَم بِظَٰهِرٍۢ مِّنَ ٱلْقَوْلِ ۗ بَلْ زُيِّنَ لِلَّذِينَ كَفَرُوا۟ مَكْرُهُمْ وَصُدُّوا۟ عَنِ ٱلسَّبِيلِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
  Unverified discovery rationale: luna: The section's source gloss for al-Qayyūm is one who stands over and watches each thing. This ayah says “قَائِمٌ عَلَىٰ كُلِّ نَفْسٍ بِمَا كَسَبَتْ,” directly joining that root sense to each soul's earned account.
- (13:41) [terra: strong (missing-ayat turn); basis: root+theme] أَوَلَمْ يَرَوْا۟ أَنَّا نَأْتِى ٱلْأَرْضَ نَنقُصُهَا مِنْ أَطْرَافِهَا ۚ وَٱللَّهُ يَحْكُمُ لَا مُعَقِّبَ لِحُكْمِهِۦ ۚ وَهُوَ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: terra: Allah judges and none reverses His judgment, while He is swift in account; rule and حساب meet in one assertion.
- (14:31) [terra: strong; basis: contrast+scene+theme] قُل لِّعِبَادِىَ ٱلَّذِينَ ءَامَنُوا۟ يُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُنفِقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا بَيْعٌۭ فِيهِ وَلَا خِلَٰلٌ
  Unverified discovery rationale: terra: Believers are told to spend before a day in which there is no buying or friendship, a boundary on the market logic of debt and exchange.
- (14:41) [terra: strong (missing-ayat turn); basis: root+theme] رَبَّنَا ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ ٱلْحِسَابُ
  Unverified discovery rationale: terra: Abraham asks forgiveness for the day the account is established, a personal plea parallel to his hope in 26:82.
- (14:48) [luna: medium; terra: strong; basis: contrast+root+scene+theme] يَوْمَ تُبَدَّلُ ٱلْأَرْضُ غَيْرَ ٱلْأَرْضِ وَٱلسَّمَٰوَٰتُ ۖ وَبَرَزُوا۟ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
  Unverified discovery rationale: luna: On the day the earth is changed, all appear before God, “الْوَاحِدِ الْقَهَّارِ.” This supplies another public appearance before the sovereign whom the section places at the center of the day. | terra: On the day the earth is changed to another earth and people emerge before the One, Compelling Allah, غَيْر becomes a final transformation before judgment.
- (15:35) [terra: strong (missing-ayat turn); basis: root+theme] وَإِنَّ عَلَيْكَ ٱللَّعْنَةَ إِلَىٰ يَوْمِ ٱلدِّينِ
  Unverified discovery rationale: terra: The curse on Iblis lasts until the Day of Recompense, using the exact dīn formulation for an irrevocable final due.
- (16:106) [terra: strong; basis: root+theme] مَن كَفَرَ بِٱللَّهِ مِنۢ بَعْدِ إِيمَٰنِهِۦٓ إِلَّا مَنْ أُكْرِهَ وَقَلْبُهُۥ مُطْمَئِنٌّۢ بِٱلْإِيمَٰنِ وَلَٰكِن مَّن شَرَحَ بِٱلْكُفْرِ صَدْرًۭا فَعَلَيْهِمْ غَضَبٌۭ مِّنَ ٱللَّهِ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
  Unverified discovery rationale: terra: Whoever opens the breast to disbelief receives Allah's wrath and a great punishment, making غضب explicitly punitive.
- (16:111) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] ۞ يَوْمَ تَأْتِى كُلُّ نَفْسٍۢ تُجَٰدِلُ عَن نَّفْسِهَا وَتُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: luna: On the day each soul comes pleading for itself, it is fully repaid for what it did and is not wronged. This adds the individual appearance and accounting that the section's day scene entails. | terra: Every soul comes pleading for itself and is paid in full for what it did; personal standing and exact recompense coincide.
- (17:13) [terra: strong; basis: scene+theme] وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا
  Unverified discovery rationale: terra: Each person's deed is fastened to the neck and a book is brought out on the Day of Resurrection, making personal liability visible.
- (17:14) [terra: strong; basis: neighbour+scene+theme] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
  Unverified discovery rationale: terra: 'Read your book' makes the person sufficient as accountant against himself, completing 17:13's record.
- (17:33) [luna: medium; terra: strong; basis: contrast+scene+theme] وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۗ وَمَن قُتِلَ مَظْلُومًۭا فَقَدْ جَعَلْنَا لِوَلِيِّهِۦ سُلْطَٰنًۭا فَلَا يُسْرِف فِّى ٱلْقَتْلِ ۖ إِنَّهُۥ كَانَ مَنصُورًۭا
  Unverified discovery rationale: luna: The section's dictionary gloss says blood is wasted when no retaliation is sought. This ayah gives the slain person's heir authority to seek justice but bars excess, setting a limit on the blood-for-blood scene. | terra: The slain person's heir receives authority, but must not exceed the limit in killing; it guards against blood being both unavenged and over-avenged.
- (17:35) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶22] وَأَوْفُوا۟ ٱلْكَيْلَ إِذَا كِلْتُمْ وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ ۚ ذَٰلِكَ خَيْرٌۭ وَأَحْسَنُ تَأْوِيلًۭا
  Unverified discovery rationale: luna: The section says its source root q-w-m links mustaqīm to a balance that does not lean. The command “وَزِنُوا بِالْقِسْطَاسِ الْمُسْتَقِيمِ” makes that link literal in honest weighing. | terra: It commands full measure and weighing with the upright balance (ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ), explicitly giving the section's straight path a market scale.
- (17:71) [terra: strong (missing-ayat turn); basis: scene+theme] يَوْمَ نَدْعُوا۟ كُلَّ أُنَاسٍۭ بِإِمَٰمِهِمْ ۖ فَمَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَأُو۟لَٰٓئِكَ يَقْرَءُونَ كِتَٰبَهُمْ وَلَا يُظْلَمُونَ فَتِيلًۭا
  Unverified discovery rationale: terra: On the day every people is called with its record, those given their book read it and are not wronged even a thread.
- (18:47) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَيَوْمَ نُسَيِّرُ ٱلْجِبَالَ وَتَرَى ٱلْأَرْضَ بَارِزَةًۭ وَحَشَرْنَٰهُمْ فَلَمْ نُغَادِرْ مِنْهُمْ أَحَدًۭا
  Unverified discovery rationale: terra: The earth is laid bare and all are gathered with none left behind, staging the presentation before the Lord in 18:48.
- (18:49) [luna: strong; terra: strong; basis: scene+theme] وَوُضِعَ ٱلْكِتَٰبُ فَتَرَى ٱلْمُجْرِمِينَ مُشْفِقِينَ مِمَّا فِيهِ وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا ۗ وَلَا يَظْلِمُ رَبُّكَ أَحَدًۭا
  Unverified discovery rationale: luna: The placed record leaves nothing small or great uncounted, and wrongdoers fear what it contains. This gives the section's accounting day a written counterpart to its scale that omits no weight. | terra: The record leaves neither small nor great deed uncounted, and Allah wrongs no one: it is the written counterpart to an exact scale.
- (19:93) [terra: strong (missing-ayat turn); basis: scene+theme] إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا
  Unverified discovery rationale: terra: Every being in the heavens and earth comes to the Merciful only as a servant, giving final arrival a relation of total possession.
- (19:94) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا
  Unverified discovery rationale: terra: Allah has counted and numbered them all, the comprehensive enumeration behind their individual coming in 19:95.
- (19:95) [luna: strong (missing-ayat turn); terra: medium; basis: root+scene+theme] وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا
  Unverified discovery rationale: luna: Everyone comes to God on Resurrection Day “فَرْدًا,” one by one. This makes the section's qiyāmah image of creatures standing before God an individual appearance rather than an evadable collective account. | terra: Every one comes to Allah individually on the Day of Resurrection, sharpening the section's personal, non-substitutable reckoning.
- (20:15) [terra: strong (missing-ayat turn); basis: scene+theme] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
  Unverified discovery rationale: terra: The Hour is coming so every soul may be repaid for what it strives for, directly binding a hidden day to measured recompense.
- (20:81) [terra: strong; basis: root+theme] كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَلَا تَطْغَوْا۟ فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِى ۖ وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ
  Unverified discovery rationale: terra: Whoever incurs Allah's wrath falls, directly explaining wrath as an effective punishment rather than mere emotion.
- (20:111) [luna: strong; terra: strong; basis: root+scene+theme] ۞ وَعَنَتِ ٱلْوُجُوهُ لِلْحَىِّ ٱلْقَيُّومِ ۖ وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا
  Unverified discovery rationale: luna: The section describes creatures standing before al-Ḥayy al-Qayyūm. Here faces are humbled before “الْحَيِّ الْقَيُّومِ,” joining that divine title to the judgment scene and its reckoning of wrongdoing. | terra: Faces are humbled before the Living, Self-Subsisting One, and one bearing injustice fails; it joins Qayyūm, standing before Him, and final loss.
- (21:47) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ فَلَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا ۖ وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا ۗ وَكَفَىٰ بِنَا حَٰسِبِينَ
  Unverified discovery rationale: luna: The section's account is pictured through an even scale and full weight. This ayah sets “الْمَوَازِينَ الْقِسْطَ” for Resurrection and says even a mustard seed's weight will be brought, making no imbalance or omission escape the reckoning. | terra: Allah sets the scales of justice for the Day of Resurrection and brings even a mustard-seed weight: the section's exact, non-leaning balance at final account.
- (22:56) [luna: strong; terra: strong; basis: root+scene+theme] ٱلْمُلْكُ يَوْمَئِذٍۢ لِّلَّهِ يَحْكُمُ بَيْنَهُمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِى جَنَّٰتِ ٱلنَّعِيمِ
  Unverified discovery rationale: luna: The section's mālik image is echoed by “الْمُلْكُ يَوْمَئِذٍ لِلَّهِ”; this ayah adds that God judges between people, joining sovereignty to the day's accounting. | terra: Dominion belongs to Allah that day and He judges between people, directly combining ملك, day, and judgment.
- (23:88) [terra: strong (missing-ayat turn); basis: root+theme] قُلْ مَنۢ بِيَدِهِۦ مَلَكُوتُ كُلِّ شَىْءٍۢ وَهُوَ يُجِيرُ وَلَا يُجَارُ عَلَيْهِ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: The kingdom of every thing is in whose hand, and He protects while none protects against Him: the powerful hand of final sovereignty.
- (23:101) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] فَإِذَا نُفِخَ فِى ٱلصُّورِ فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ
  Unverified discovery rationale: terra: At the trumpet, kinship and mutual questions cease, immediately before the weighing of scales in 23:102-103.
- (23:102) [luna: strong; terra: strong; basis: root+scene+theme] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
  Unverified discovery rationale: luna: “ثَقُلَتْ مَوَازِينُهُ” describes heavy scales as the condition for success, directly matching the section's account of weight being assessed on the day. | terra: Whoever's scales are heavy succeeds, repeating the final balance with a personal outcome.
- (23:103) [luna: strong; terra: strong; basis: contrast+neighbour+root+scene+theme] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
  Unverified discovery rationale: luna: This next ayah gives the opposite outcome: light scales mean loss. It completes 23:102's two-sided weighing scene and makes the section's unbending measure consequential. | terra: Light scales make their possessors lose themselves in Hell, the reversal that makes the upright measure morally consequential.
- (23:115) [terra: strong (missing-ayat turn); basis: root+theme] أَفَحَسِبْتُمْ أَنَّمَا خَلَقْنَٰكُمْ عَبَثًۭا وَأَنَّكُمْ إِلَيْنَا لَا تُرْجَعُونَ
  Unverified discovery rationale: terra: Creation is not purposeless and people are returned to Allah, giving the account its answer to the denial of meaningful return.
- (23:116) [terra: strong; basis: root+theme] فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۖ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْكَرِيمِ
  Unverified discovery rationale: terra: Allah is the True King, and people are not created without return to Him; true kingship entails the account denied by purposelessness.
- (24:37) [terra: strong (missing-ayat turn); basis: scene+theme] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
  Unverified discovery rationale: terra: Trade and sale do not distract these people from worship and almsgiving because they fear a day when hearts and eyes turn.
- (24:39) [terra: strong (missing-ayat turn); basis: scene+theme] وَٱلَّذِينَ كَفَرُوٓا۟ أَعْمَٰلُهُمْ كَسَرَابٍۭ بِقِيعَةٍۢ يَحْسَبُهُ ٱلظَّمْـَٔانُ مَآءً حَتَّىٰٓ إِذَا جَآءَهُۥ لَمْ يَجِدْهُ شَيْـًۭٔا وَوَجَدَ ٱللَّهَ عِندَهُۥ فَوَفَّىٰهُ حِسَابَهُۥ ۗ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: terra: The deeds of disbelievers are a mirage; finding Allah, they receive their account in full, and He is swift in account.
- (25:24) [terra: strong; basis: neighbour+scene] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
  Unverified discovery rationale: terra: It gives the prosperous destination of the people of Paradise on the same day whose true dominion 25:26 assigns to the Merciful.
- (25:25) [terra: strong; basis: neighbour+scene] وَيَوْمَ تَشَقَّقُ ٱلسَّمَآءُ بِٱلْغَمَٰمِ وَنُزِّلَ ٱلْمَلَٰٓئِكَةُ تَنزِيلًا
  Unverified discovery rationale: terra: The sky's splitting and the angels' descent stage the Day immediately before 25:26's declaration of true kingship.
- (25:26) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶21] ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ ۚ وَكَانَ يَوْمًا عَلَى ٱلْكَٰفِرِينَ عَسِيرًۭا
  Unverified discovery rationale: luna: The section connects 1:3's al-Raḥmān with 1:4's owner of the day. “الْمُلْكُ يَوْمَئِذٍ الْحَقُّ لِلرَّحْمَٰنِ” joins the true dominion on that day to the same name. | terra: The true kingdom on that day belongs to the Merciful, bringing the surah's Rahmān and its Mālik of the Day together.
- (26:80) [terra: strong; basis: neighbour+speaker] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
  Unverified discovery rationale: terra: Abraham names Allah as the one who heals him, part of his personal chain of dependence leading to the Day of Recompense in 26:82.
- (26:81) [terra: strong; basis: neighbour+speaker] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
  Unverified discovery rationale: terra: Abraham says Allah will cause his death and then give life, supplying resurrection for his hope about the Day in 26:82.
- (26:82) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶22] وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ
  Unverified discovery rationale: luna: Ibrahim speaks of hoping for forgiveness “يَوْمَ الدِّينِ.” His hope places mercy and accountability together in the very day named by the section. | terra: Abraham hopes that Allah will forgive his sin on the Day of Recompense, giving the day an individual plea for mercy as well as judgment.
- (26:181) [luna: strong; terra: strong; basis: contrast+neighbour+scene+speaker+theme] ۞ أَوْفُوا۟ ٱلْكَيْلَ وَلَا تَكُونُوا۟ مِنَ ٱلْمُخْسِرِينَ
  Unverified discovery rationale: luna: Shuʿayb first commands, “أَوْفُوا الْكَيْلَ,” and forbids causing loss. The next ayah's straight balance completes this scene of fair trade that the section links to the final scale. | terra: Give full measure and do not cause loss: the command begins the same fair-weighing scene completed by 26:182.
- (26:182) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶22] وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ
  Unverified discovery rationale: luna: Shuʿayb's command “بِالْقِسْطَاسِ الْمُسْتَقِيمِ” directly joins the section's source word mustaqīm to an upright trading balance, so straightness applies to both the path and measure. | terra: Weigh with the upright balance (ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ), the exact verbal meeting of the section's straightness and scale.
- (26:183) [terra: strong; basis: contrast+neighbour+scene] وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: terra: Do not deprive people of their things or spread corruption; it gives the social wrong that an unequal scale commits.
- (28:70) [terra: strong (missing-ayat turn); basis: root+theme] وَهُوَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ ۖ وَلَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: Judgment belongs to Allah and to Him people return, compactly joining sovereign rule to final return.
- (31:16) [luna: strong; basis: scene+theme] يَٰبُنَىَّ إِنَّهَآ إِن تَكُ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ فَتَكُن فِى صَخْرَةٍ أَوْ فِى ٱلسَّمَٰوَٰتِ أَوْ فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ ۚ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌۭ
  Unverified discovery rationale: luna: The section's scale scene says even a mustard seed's weight will be brought. Luqman's example likewise says that a mustard seed hidden in rock, heaven, or earth will be brought forth, emphasizing the reach of exact reckoning.
- (31:33) [terra: strong (missing-ayat turn); basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمْ وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا ۚ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ
  Unverified discovery rationale: terra: On the day no parent can avail a child and no child a parent, family cannot substitute for personal liability.
- (34:3) [luna: strong (missing-ayat turn); basis: scene+theme] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَأْتِينَا ٱلسَّاعَةُ ۖ قُلْ بَلَىٰ وَرَبِّى لَتَأْتِيَنَّكُمْ عَٰلِمِ ٱلْغَيْبِ ۖ لَا يَعْزُبُ عَنْهُ مِثْقَالُ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ وَلَآ أَصْغَرُ مِن ذَٰلِكَ وَلَآ أَكْبَرُ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: Nothing the size of an atom, smaller, or larger is hidden from God, and it is recorded in a clear book. This connects the section's smallest weights and complete accounting to what cannot escape notice.
- (36:12) [terra: strong; basis: scene+theme] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
  Unverified discovery rationale: terra: Allah records what people sent ahead and their traces and enumerates everything, the comprehensive ledger behind recompense.
- (36:51) [terra: strong (missing-ayat turn); basis: scene+theme] وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ
  Unverified discovery rationale: terra: The trumpet is blown and people rush from graves toward their Lord, a resurrection arrival for account.
- (36:52) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] قَالُوا۟ يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا ۜ ۗ هَٰذَا مَا وَعَدَ ٱلرَّحْمَٰنُ وَصَدَقَ ٱلْمُرْسَلُونَ
  Unverified discovery rationale: terra: The raised people recognize the promise of the Merciful and the truth of the messengers, answering their question about awakening.
- (36:53) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِن كَانَتْ إِلَّا صَيْحَةًۭ وَٰحِدَةًۭ فَإِذَا هُمْ جَمِيعٌۭ لَّدَيْنَا مُحْضَرُونَ
  Unverified discovery rationale: terra: One blast brings all before Allah, completing the passage in which 36:54 gives exact recompense.
- (36:54) [luna: strong (missing-ayat turn); basis: scene+theme] فَٱلْيَوْمَ لَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا وَلَا تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
  Unverified discovery rationale: luna: On that day no soul is wronged and each is repaid only for what it did. It directly joins the section's day of recompense to a just, individual account.
- (36:78) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَضَرَبَ لَنَا مَثَلًۭا وَنَسِىَ خَلْقَهُۥ ۖ قَالَ مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌۭ
  Unverified discovery rationale: terra: The decayed-bone question begins the resurrection argument that ends with dominion in Allah hand at 36:83.
- (36:79) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] قُلْ يُحْيِيهَا ٱلَّذِىٓ أَنشَأَهَآ أَوَّلَ مَرَّةٍۢ ۖ وَهُوَ بِكُلِّ خَلْقٍ عَلِيمٌ
  Unverified discovery rationale: terra: The One who first originated bones gives them life and knows every creation, grounding resurrection before the final return.
- (36:83) [terra: strong; basis: root+theme] فَسُبْحَٰنَ ٱلَّذِى بِيَدِهِۦ مَلَكُوتُ كُلِّ شَىْءٍۢ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: In His hand is the dominion of every thing and to Him people return, bringing sovereign possession and final return together.
- (37:19) [terra: strong (missing-ayat turn); basis: neighbour+scene] فَإِنَّمَا هِىَ زَجْرَةٌۭ وَٰحِدَةٌۭ فَإِذَا هُمْ يَنظُرُونَ
  Unverified discovery rationale: terra: One cry leaves them looking on, setting the immediate resurrection scene for the Day of Recompense in 37:20.
- (37:20) [terra: strong (missing-ayat turn); basis: root+theme] وَقَالُوا۟ يَٰوَيْلَنَا هَٰذَا يَوْمُ ٱلدِّينِ
  Unverified discovery rationale: terra: They recognize the event as the Day of Recompense, matching 1:4 with the exact final-day term.
- (38:16) [terra: strong (missing-ayat turn); basis: root+theme] وَقَالُوا۟ رَبَّنَا عَجِّل لَّنَا قِطَّنَا قَبْلَ يَوْمِ ٱلْحِسَابِ
  Unverified discovery rationale: terra: They demand their allotted record before the Day of Account, naming the final reckoning with حساب.
- (38:78) [terra: strong (missing-ayat turn); basis: root+theme] وَإِنَّ عَلَيْكَ لَعْنَتِىٓ إِلَىٰ يَوْمِ ٱلدِّينِ
  Unverified discovery rationale: terra: Iblis is cursed until the Day of Recompense, another exact dīn designation for the day when punishment reaches its term.
- (39:47) [luna: contrast; terra: strong; basis: contrast+scene+theme] وَلَوْ أَنَّ لِلَّذِينَ ظَلَمُوا۟ مَا فِى ٱلْأَرْضِ جَمِيعًۭا وَمِثْلَهُۥ مَعَهُۥ لَٱفْتَدَوْا۟ بِهِۦ مِن سُوٓءِ ٱلْعَذَابِ يَوْمَ ٱلْقِيَٰمَةِ ۚ وَبَدَا لَهُم مِّنَ ٱللَّهِ مَا لَمْ يَكُونُوا۟ يَحْتَسِبُونَ
  Unverified discovery rationale: luna: On Resurrection Day, wrongdoers would offer all the earth and its like as ransom from punishment. The ayah makes explicit the section's point that no equivalent payment can replace the account due that day. | terra: Possessing the earth twice over would lead wrongdoers to offer it as ransom from the evil of the Day, but the judgment exceeds such exchange.
- (39:68) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَنُفِخَ فِى ٱلصُّورِ فَصَعِقَ مَن فِى ٱلسَّمَٰوَٰتِ وَمَن فِى ٱلْأَرْضِ إِلَّا مَن شَآءَ ٱللَّهُ ۖ ثُمَّ نُفِخَ فِيهِ أُخْرَىٰ فَإِذَا هُمْ قِيَامٌۭ يَنظُرُونَ
  Unverified discovery rationale: terra: The trumpet brings death and then rising to wait, immediately before 39:69 sets the record and judges in truth.
- (39:69) [luna: strong; terra: strong; basis: scene+theme] وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: luna: On the judgment scene's earth, the record is placed and judgment is made in truth without wrong. This joins the section's account and just measure to the public scene of final judgment. | terra: The earth shines, the record is set down, prophets and witnesses are brought, and judgment is made in truth without wrong.
- (39:70) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُوَ أَعْلَمُ بِمَا يَفْعَلُونَ
  Unverified discovery rationale: luna: Every soul is paid in full for what it did, and God knows best what they did. This is another explicit formulation of the section's accounting and equivalent recompense. | terra: Every soul is paid in full for what it did, completing the judicial scene in 39:69.
- (40:15) [terra: strong (missing-ayat turn); basis: neighbour+scene] رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ
  Unverified discovery rationale: terra: Allah warns of the Day of Meeting, introducing the day when all come forth and ownership is declared His in 40:16.
- (40:16) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ ۚ لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
  Unverified discovery rationale: luna: The section's source root m-l-k connects the owner of the day to the question “لِمَنِ الْمُلْكُ الْيَوْمَ”; the answer makes that day's sovereignty God's alone. | terra: On the day all come forth, ownership is asked and answered: the kingdom belongs to the One, Overpowering Allah.
- (40:17) [luna: strong; terra: strong; basis: neighbour+scene+theme] ٱلْيَوْمَ تُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ ۚ لَا ظُلْمَ ٱلْيَوْمَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: After 40:16 asks who owns the day, this ayah says every soul is repaid for what it earned and no one is wronged. It makes the section's judgment and recompense concrete. | terra: Each soul is repaid for what it earned, without injustice, and Allah is swift in account; it states the reckoning under 40:16's sole kingship.
- (40:18) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَأَنذِرْهُمْ يَوْمَ ٱلْءَازِفَةِ إِذِ ٱلْقُلُوبُ لَدَى ٱلْحَنَاجِرِ كَٰظِمِينَ ۚ مَا لِلظَّٰلِمِينَ مِنْ حَمِيمٍۢ وَلَا شَفِيعٍۢ يُطَاعُ
  Unverified discovery rationale: terra: On the impending day no intimate friend or obeyed intercessor remains for wrongdoers, extending 40:16-17 beyond property to failed advocacy.
- (45:22) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] وَخَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَلِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
  Unverified discovery rationale: luna: God created the heavens and earth in truth so every soul may be recompensed for what it earned without being wronged. It connects the section's just scale to the stated purpose of creation and judgment. | terra: Heavens and earth are created in truth so every soul may be repaid for what it earned without injustice.
- (45:26) [luna: strong; terra: strong (missing-ayat turn); basis: neighbour+scene+theme] قُلِ ٱللَّهُ يُحْيِيكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يَجْمَعُكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
  Unverified discovery rationale: luna: This ayah says God gives life, causes death, and gathers people for the Resurrection Day, supplying the event of gathering that the section's day-of-recompense scene presupposes. | terra: Allah gives life and death, then gathers people on the unquestionable Day of Resurrection before the dominion and record scenes in 45:27-28.
- (45:27) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يَوْمَئِذٍۢ يَخْسَرُ ٱلْمُبْطِلُونَ
  Unverified discovery rationale: luna: Following 45:26's gathering for the Hour, this ayah assigns the dominion of the heavens and earth to God and says the Hour's day is when loss becomes clear; it joins the section's day and sovereignty. | terra: To Allah belongs the dominion of heavens and earth; when the Hour comes, the falsifiers lose, making earthly ownership answer to final loss.
- (45:28) [terra: strong; basis: scene+theme] وَتَرَىٰ كُلَّ أُمَّةٍۢ جَاثِيَةًۭ ۚ كُلُّ أُمَّةٍۢ تُدْعَىٰٓ إِلَىٰ كِتَٰبِهَا ٱلْيَوْمَ تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
  Unverified discovery rationale: terra: Every community is seen kneeling and called to its record; 'Today you are recompensed' fuses bodily stance, book, and account.
- (47:28) [terra: strong (missing-ayat turn); basis: root+theme] ذَٰلِكَ بِأَنَّهُمُ ٱتَّبَعُوا۟ مَآ أَسْخَطَ ٱللَّهَ وَكَرِهُوا۟ رِضْوَٰنَهُۥ فَأَحْبَطَ أَعْمَٰلَهُمْ
  Unverified discovery rationale: terra: Following what angers Allah and hating His pleasure makes deeds void, linking divine anger to the loss of accounted work.
- (47:38) [terra: strong; basis: contrast+root] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ تُدْعَوْنَ لِتُنفِقُوا۟ فِى سَبِيلِ ٱللَّهِ فَمِنكُم مَّن يَبْخَلُ ۖ وَمَن يَبْخَلْ فَإِنَّمَا يَبْخَلُ عَن نَّفْسِهِۦ ۚ وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ ۚ وَإِن تَتَوَلَّوْا۟ يَسْتَبْدِلْ قَوْمًا غَيْرَكُمْ ثُمَّ لَا يَكُونُوٓا۟ أَمْثَٰلَكُم
  Unverified discovery rationale: terra: If people turn away, Allah replaces them with another people; the verse gives غَيْر a communal substitution that warns against refusing the required response.
- (48:6) [terra: strong; basis: root+theme] وَيُعَذِّبَ ٱلْمُنَٰفِقِينَ وَٱلْمُنَٰفِقَٰتِ وَٱلْمُشْرِكِينَ وَٱلْمُشْرِكَٰتِ ٱلظَّآنِّينَ بِٱللَّهِ ظَنَّ ٱلسَّوْءِ ۚ عَلَيْهِمْ دَآئِرَةُ ٱلسَّوْءِ ۖ وَغَضِبَ ٱللَّهُ عَلَيْهِمْ وَلَعَنَهُمْ وَأَعَدَّ لَهُمْ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًۭا
  Unverified discovery rationale: terra: Allah's wrath and curse are joined to Hell for hypocrites and idolaters, giving the punished sense of ٱلْمَغْضُوبِ a direct outcome.
- (50:17) [terra: strong; basis: scene+theme] إِذْ يَتَلَقَّى ٱلْمُتَلَقِّيَانِ عَنِ ٱلْيَمِينِ وَعَنِ ٱلشِّمَالِ قَعِيدٌۭ
  Unverified discovery rationale: terra: Two receivers sit at right and left taking down deeds, an evidentiary counterpart to written debt testimony.
- (50:18) [terra: strong; basis: scene+theme] مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ
  Unverified discovery rationale: terra: No word is uttered without a ready watcher, sharpening the section's concern that account and memory not be lost.
- (50:20) [terra: strong (missing-ayat turn); basis: scene+theme] وَنُفِخَ فِى ٱلصُّورِ ۚ ذَٰلِكَ يَوْمُ ٱلْوَعِيدِ
  Unverified discovery rationale: terra: The trumpet comes with the truth: this is the day of threat, introducing the soul with driver and witness in 50:21.
- (50:21) [terra: strong; basis: scene+theme] وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ
  Unverified discovery rationale: terra: Every soul comes with a driver and a witness, staging individual arrival for account.
- (50:22) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] لَّقَدْ كُنتَ فِى غَفْلَةٍۢ مِّنْ هَٰذَا فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ
  Unverified discovery rationale: terra: The veil is lifted and sight becomes sharp, making the final presentation unmistakable.
- (50:23) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَقَالَ قَرِينُهُۥ هَٰذَا مَا لَدَىَّ عَتِيدٌ
  Unverified discovery rationale: terra: The companion presents a ready record, an explicit ledger beside the witnessing scene of 50:17-21.
- (50:29) [terra: strong; basis: speaker+theme] مَا يُبَدَّلُ ٱلْقَوْلُ لَدَىَّ وَمَآ أَنَا۠ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
  Unverified discovery rationale: terra: Allah says His word is not changed and He is not unjust to servants, grounding the final verdict in fixed, even justice.
- (51:5) [terra: strong; basis: neighbour+scene] إِنَّمَا تُوعَدُونَ لَصَادِقٌۭ
  Unverified discovery rationale: terra: The command is surely occurring; it prepares 51:6's assertion that recompense is certain rather than speculative.
- (51:6) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶22] وَإِنَّ ٱلدِّينَ لَوَٰقِعٌۭ
  Unverified discovery rationale: luna: The section's source word dīn means recompense, and its dictionary gloss calls the day an event that comes to pass. “وَإِنَّ الدِّينَ لَوَاقِعٌ” states that this recompense is certain to occur. | terra: Recompense (ٱلدِّينَ) is surely to occur, directly confirming the inevitable Day of Recompense in 1:4.
- (53:31) [terra: strong (missing-ayat turn); basis: scene+theme] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
  Unverified discovery rationale: terra: Allah owns heavens and earth in order to repay evildoers for what they did and reward those who do good.
- (55:7) [luna: medium; terra: strong; basis: root+scene+theme] وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
  Unverified discovery rationale: luna: The section develops the balance as an image of measured justice. This ayah says God set “الْمِيزَانَ,” giving the balance a created order beyond the marketplace and judgment scene. | terra: Allah raised the sky and set the balance (ٱلْمِيزَانَ), enlarging the section's measure from coin to created order.
- (55:9) [luna: medium; terra: strong; basis: contrast+neighbour+root+scene+theme] وَأَقِيمُوا۟ ٱلْوَزْنَ بِٱلْقِسْطِ وَلَا تُخْسِرُوا۟ ٱلْمِيزَانَ
  Unverified discovery rationale: luna: This ayah commands “أَقِيمُوا الْوَزْنَ بِالْقِسْطِ,” just weighing. It completes 55:7–8 by making the balance an obligation of equitable measure. | terra: Establish weight with justice and do not make the balance deficient, the direct opposite of the deficient weighing in 83:3.
- (56:1) [terra: strong (missing-ayat turn); basis: scene+theme] إِذَا وَقَعَتِ ٱلْوَاقِعَةُ
  Unverified discovery rationale: terra: When the Inevitable Event occurs, the Day is portrayed as an arriving occurrence rather than an ordinary interval.
- (56:2) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ
  Unverified discovery rationale: terra: No one can deny its occurrence, echoing the certainty of recompense in 51:6.
- (56:3) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] خَافِضَةٌۭ رَّافِعَةٌ
  Unverified discovery rationale: terra: It lowers some and raises others, giving final recompense a reversal of rank and value.
- (56:60) [terra: strong (missing-ayat turn); basis: root+theme] نَحْنُ قَدَّرْنَا بَيْنَكُمُ ٱلْمَوْتَ وَمَا نَحْنُ بِمَسْبُوقِينَ
  Unverified discovery rationale: terra: Allah decreed death and cannot be outstripped, opening a resurrection argument in terms of replacement.
- (56:61) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] عَلَىٰٓ أَن نُّبَدِّلَ أَمْثَٰلَكُمْ وَنُنشِئَكُمْ فِى مَا لَا تَعْلَمُونَ
  Unverified discovery rationale: terra: He can replace people with their likeness and bring them forth in an unknown form, a final counterpart to the section secondary replacement sense.
- (57:15) [terra: strong; basis: contrast+scene+theme] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: No ransom is taken that day from hypocrites or disbelievers; the fire is their due destination.
- (57:25) [luna: medium; terra: strong; basis: root+scene+theme] لَقَدْ أَرْسَلْنَا رُسُلَنَا بِٱلْبَيِّنَٰتِ وَأَنزَلْنَا مَعَهُمُ ٱلْكِتَٰبَ وَٱلْمِيزَانَ لِيَقُومَ ٱلنَّاسُ بِٱلْقِسْطِ ۖ وَأَنزَلْنَا ٱلْحَدِيدَ فِيهِ بَأْسٌۭ شَدِيدٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَلِيَعْلَمَ ٱللَّهُ مَن يَنصُرُهُۥ وَرُسُلَهُۥ بِٱلْغَيْبِ ۚ إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌۭ
  Unverified discovery rationale: luna: The section sets the straight path beside the upright scale through source root q-w-m. Here scripture and “الْمِيزَانَ” are sent so people may establish justice, explicitly joining guidance with measured fairness. | terra: The Book and the balance are sent down so people may uphold justice; it states the public purpose of the straight measure.
- (58:6) [terra: strong; basis: scene+theme] يَوْمَ يَبْعَثُهُمُ ٱللَّهُ جَمِيعًۭا فَيُنَبِّئُهُم بِمَا عَمِلُوٓا۟ ۚ أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
  Unverified discovery rationale: terra: Allah informs them of what they did; they forgot it but Allah counted it, directly reversing the witness's possible forgetting in 2:282.
- (67:1) [terra: strong; basis: root+theme] تَبَٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: Blessed is He in whose hand is all dominion and who has power over everything, illuminating the section's gloss of the king's strong hand.
- (69:13) [terra: strong (missing-ayat turn); basis: neighbour+scene] فَإِذَا نُفِخَ فِى ٱلصُّورِ نَفْخَةٌۭ وَٰحِدَةٌۭ
  Unverified discovery rationale: terra: The trumpet is blown once, beginning the final presentation scene completed at 69:18.
- (69:14) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَحُمِلَتِ ٱلْأَرْضُ وَٱلْجِبَالُ فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ
  Unverified discovery rationale: terra: Earth and mountains are lifted and crushed in one blow, making the day an overwhelming event.
- (69:15) [terra: strong (missing-ayat turn); basis: neighbour+scene] فَيَوْمَئِذٍۢ وَقَعَتِ ٱلْوَاقِعَةُ
  Unverified discovery rationale: terra: On that day the Occurrence occurs, directly treating the day as the arriving event named by the section.
- (69:16) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَٱنشَقَّتِ ٱلسَّمَآءُ فَهِىَ يَوْمَئِذٍۢ وَاهِيَةٌۭ
  Unverified discovery rationale: terra: The sky splits and becomes frail, extending the final-day scene before the presentation of all secrets.
- (69:17) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا ۚ وَيَحْمِلُ عَرْشَ رَبِّكَ فَوْقَهُمْ يَوْمَئِذٍۢ ثَمَٰنِيَةٌۭ
  Unverified discovery rationale: terra: Angels stand at its edges while bearers carry the Throne, adding a sovereign court to 69:18 presentation.
- (69:18) [terra: strong; basis: scene+theme] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
  Unverified discovery rationale: terra: On the day of presentation no secret is hidden, matching the section's claim that no one vanishes from the accounting scene.
- (69:19) [terra: strong; basis: scene+theme] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
  Unverified discovery rationale: terra: The one given his record in the right hand announces his account, a concrete favorable settlement.
- (69:25) [terra: strong; basis: scene+theme] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ فَيَقُولُ يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ
  Unverified discovery rationale: terra: The one given his record in the left hand voices the contrary failed account.
- (70:11) [luna: contrast; terra: strong; basis: contrast+scene+theme] يُبَصَّرُونَهُمْ ۚ يَوَدُّ ٱلْمُجْرِمُ لَوْ يَفْتَدِى مِنْ عَذَابِ يَوْمِئِذٍۭ بِبَنِيهِ
  Unverified discovery rationale: luna: The criminal wishes to ransom himself “مِنْ عَذَابِ يَوْمِئِذٍ بِبَنِيهِ,” giving the section's failed-substitution image a vivid day-of-recompense scene. | terra: The guilty person would like to ransom himself from that day's punishment with his children, exposing the impossible substitution of another for oneself.
- (70:12) [luna: contrast; terra: strong; basis: contrast+neighbour+scene+theme] وَصَٰحِبَتِهِۦ وَأَخِيهِ
  Unverified discovery rationale: luna: Continuing 70:11's ransom wish, this ayah adds his wife and brother as substitutes. It shows the reach of the attempted payment while 70:11 supplies the day and punishment. | terra: He would offer his spouse and brother as ransom, extending the failed exchange to closest relations.
- (70:13) [luna: contrast; terra: strong; basis: contrast+neighbour+scene+theme] وَفَصِيلَتِهِ ٱلَّتِى تُـْٔوِيهِ
  Unverified discovery rationale: luna: This continuation adds the family that shelters him to the imagined ransom, showing that even one's closest social refuge cannot replace the account. | terra: He would offer his clan that sheltered him, but kinship cannot discharge the personal due.
- (70:14) [luna: contrast; terra: strong; basis: contrast+neighbour+scene+theme] وَمَن فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ يُنجِيهِ
  Unverified discovery rationale: luna: The final continuation expands the wished-for ransom to everyone on earth. It completes the sequence by making clear that no imaginable equivalent could avert that day's punishment. | terra: He would offer everyone on earth to save himself; the verse sets the outer limit of ransom as an answer to the section's replacement imagery.
- (73:17) [terra: strong (missing-ayat turn); basis: scene+theme] فَكَيْفَ تَتَّقُونَ إِن كَفَرْتُمْ يَوْمًۭا يَجْعَلُ ٱلْوِلْدَٰنَ شِيبًا
  Unverified discovery rationale: terra: It asks how disbelievers can guard against a day that makes children gray, an exact severe-day image.
- (73:18) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] ٱلسَّمَآءُ مُنفَطِرٌۢ بِهِۦ ۚ كَانَ وَعْدُهُۥ مَفْعُولًا
  Unverified discovery rationale: terra: The sky splits because of it, completing the overwhelming event described in 73:17.
- (75:1) [terra: strong (missing-ayat turn); basis: root+scene] لَآ أُقْسِمُ بِيَوْمِ ٱلْقِيَٰمَةِ
  Unverified discovery rationale: terra: The oath by the Day of Resurrection names the qiyamah whose standing the section derives from q-w-m.
- (75:6) [terra: strong (missing-ayat turn); basis: scene+theme] يَسْـَٔلُ أَيَّانَ يَوْمُ ٱلْقِيَٰمَةِ
  Unverified discovery rationale: terra: The human question asks when the Day of Resurrection will be, treating it as a decisive impending event.
- (75:10) [terra: strong (missing-ayat turn); basis: neighbour+scene] يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ
  Unverified discovery rationale: terra: On that day a person asks where to flee, bringing the final event into the language of inescapability.
- (75:11) [terra: strong (missing-ayat turn); basis: neighbour+scene] كَلَّا لَا وَزَرَ
  Unverified discovery rationale: terra: There is no refuge, a direct boundary on escape or substitute payment.
- (75:12) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ
  Unverified discovery rationale: terra: To the Lord is the destination that day, returning every person to the owner of the affair.
- (75:13) [terra: strong; basis: scene+theme] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
  Unverified discovery rationale: terra: A person is informed that day of what he sent forward and left behind, the temporal ledger of his due.
- (75:22) [terra: strong (missing-ayat turn); basis: scene+theme] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
  Unverified discovery rationale: terra: Some faces are radiant that day, supplying the favorable side of the final separation.
- (75:23) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِلَىٰ رَبِّهَا نَاظِرَةٌۭ
  Unverified discovery rationale: terra: They look toward their Lord, placing the blessed outcome in direct relation to the sovereign judge.
- (75:24) [terra: strong (missing-ayat turn); basis: scene+theme] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ
  Unverified discovery rationale: terra: Other faces are gloomy that day, giving the contrasting punished side of the account.
- (75:25) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] تَظُنُّ أَن يُفْعَلَ بِهَا فَاقِرَةٌۭ
  Unverified discovery rationale: terra: They expect a backbreaking calamity, completing the adverse-day scene.
- (77:13) [terra: strong (missing-ayat turn); basis: root+theme] لِيَوْمِ ٱلْفَصْلِ
  Unverified discovery rationale: terra: The question answers that the appointed time is the Day of Decision, another formulation of final judgment.
- (77:38) [terra: strong (missing-ayat turn); basis: root+theme] هَٰذَا يَوْمُ ٱلْفَصْلِ ۖ جَمَعْنَٰكُمْ وَٱلْأَوَّلِينَ
  Unverified discovery rationale: terra: The Day of Decision gathers later and earlier peoples together, making the judicial separation a universal assembly.
- (78:38) [luna: medium; terra: strong; basis: root+scene+theme] يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا ۖ لَّا يَتَكَلَّمُونَ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَقَالَ صَوَابًۭا
  Unverified discovery rationale: luna: On the day when the Spirit and angels stand in rows, no one speaks except by permission of the Merciful. It extends the section's standing-before-God scene to the heavenly assembly and the same day. | terra: The Spirit and angels stand in rows on the day, a celestial counterpart to people standing before the Lord in 83:6.
- (79:34) [terra: strong (missing-ayat turn); basis: scene+theme] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
  Unverified discovery rationale: terra: When the overwhelming event comes, the final account reaches its decisive moment.
- (79:35) [terra: strong; basis: scene+theme] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
  Unverified discovery rationale: terra: The person remembers what he strove for when the overwhelming event comes, answering forgetfulness with recalled labor.
- (79:36) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
  Unverified discovery rationale: terra: Hell is displayed for the one who sees, supplying the punitive result surrounding remembered effort in 79:35.
- (81:13) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَإِذَا ٱلْجَنَّةُ أُزْلِفَتْ
  Unverified discovery rationale: terra: Hell is kindled immediately before every soul knows what it has brought in 81:14.
- (81:14) [terra: strong; basis: scene+theme] عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ
  Unverified discovery rationale: terra: Every soul knows what it has brought, reducing final account to the person's own presented deeds.
- (82:10) [terra: strong; basis: neighbour+theme] وَإِنَّ عَلَيْكُمْ لَحَٰفِظِينَ
  Unverified discovery rationale: terra: The guarding scribes begin the immediate context of the Day of Recompense: no deed can disappear from its account.
- (82:11) [terra: strong; basis: neighbour+theme] كِرَامًۭا كَٰتِبِينَ
  Unverified discovery rationale: terra: Its noble recorders make concrete the section's reckoning, alongside 82:17-19's Day of Recompense.
- (82:12) [terra: strong; basis: neighbour+theme] يَعْلَمُونَ مَا تَفْعَلُونَ
  Unverified discovery rationale: terra: They know what people do, supplying the recorded evidence for the recompense named later in the passage.
- (82:13) [terra: strong; basis: neighbour+scene+theme] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍۢ
  Unverified discovery rationale: terra: The righteous are in bliss, one of the two outcomes surrounding the Day of Recompense in 82:17-19.
- (82:14) [terra: strong; basis: neighbour+scene+theme] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
  Unverified discovery rationale: terra: The wicked are in Hell, the punitive counterpart to the section's account and divine wrath.
- (82:15) [terra: strong; basis: neighbour+scene+theme] يَصْلَوْنَهَا يَوْمَ ٱلدِّينِ
  Unverified discovery rationale: terra: They enter it on the Day of Recompense, joining the day directly to its due outcome.
- (82:16) [terra: strong; basis: neighbour+scene+theme] [cited in ¶21] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
  Unverified discovery rationale: terra: They are not absent from the Fire; the section likewise stresses that no one slips away from that day's settlement.
- (82:17) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ
  Unverified discovery rationale: luna: The section reads 1:4 as the day of judgment, accounting, and recompense; 82:17 asks what “يَوْمُ الدِّينِ” is, making that named day itself the question. | terra: It asks exactly what the Day of Recompense (يَوْمُ ٱلدِّينِ) is, opening the same event named in 1:4.
- (82:18) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ
  Unverified discovery rationale: luna: The section says this day is asked about twice. This next ayah repeats the question “يَوْمُ الدِّينِ,” so its contribution is the insistence that the recompense day exceeds ordinary description. | terra: The repeated question about يَوْمُ ٱلدِّينِ makes the day an overwhelming occurrence rather than an ordinary date.
- (82:19) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا ۖ وَٱلْأَمْرُ يَوْمَئِذٍۢ لِّلَّهِ
  Unverified discovery rationale: luna: The section's source word mālik means sovereign with command. “لَا تَمْلِكُ نَفْسٌ لِّنَفْسٍ شَيْئًا” and “الْأَمْرُ يَوْمَئِذٍ لِلَّهِ” show ownership and authority stripped from everyone else on that day. | terra: On that day no soul can possess or do anything for another, and the command belongs to Allah; this unfolds the exclusive Mālik of 1:4.
- (83:1) [luna: strong; terra: contrast; basis: contrast+neighbour+scene+theme] وَيْلٌۭ لِّلْمُطَفِّفِينَ
  Unverified discovery rationale: luna: This opening woe names those who give short measure as mutaffifūn; it introduces the market fraud that 83:3 specifies and that the section sets against an uninclining just scale. | terra: Its woe to defrauders introduces the crooked commercial scale that reverses the section's full, non-tilting coin.
- (83:2) [luna: strong; terra: contrast; basis: contrast+neighbour+scene] ٱلَّذِينَ إِذَا ٱكْتَالُوا۟ عَلَى ٱلنَّاسِ يَسْتَوْفُونَ
  Unverified discovery rationale: luna: The first half of the fraud is that they take their full due when measuring for themselves. With 83:3's short measure to others, this ayah exposes the imbalance the section's upright scale corrects. | terra: They demand full measure when receiving, a one-sided counterpart to equal valuation and payment.
- (83:4) [luna: strong; terra: strong; basis: neighbour+scene+theme] أَلَا يَظُنُّ أُو۟لَٰٓئِكَ أَنَّهُم مَّبْعُوثُونَ
  Unverified discovery rationale: luna: After describing short measure in 83:1–3, this ayah asks whether the defrauders expect to be raised. It connects their marketplace imbalance to the accounting day in the section. | terra: The cheaters are asked whether they expect resurrection, explicitly carrying their market fraud into the final account.
- (83:5) [luna: strong; terra: strong; basis: neighbour+scene+theme] لِيَوْمٍ عَظِيمٍۢ
  Unverified discovery rationale: luna: This neighbor names the “عَظِيمٍ” day for which the defrauders are raised, completing 83:4's link from dishonest measures to the section's weighty day of judgment. | terra: It calls that resurrection a عظیم day, the grave event which gives the deficient weighing its final consequence.
- (83:6) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶21] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: “يَوْمَ يَقُومُ النَّاسُ لِرَبِّ الْعَالَمِينَ” directly joins the section's source root q-w-m in mustaqīm and qiyāmah to people standing before their Lord for reckoning. | terra: People stand (يَقُومُ ٱلنَّاسُ) before the Lord, directly joining the q-w-m family of standing to the Day and the balance scene.
- (84:1) [terra: strong (missing-ayat turn); basis: neighbour+scene] إِذَا ٱلسَّمَآءُ ٱنشَقَّتْ
  Unverified discovery rationale: terra: The sky splits in the sequence that leads to every person meeting the Lord and receiving a record.
- (84:2) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ
  Unverified discovery rationale: terra: It obeys its Lord as due, giving the final scene a sovereign command relationship.
- (84:3) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَإِذَا ٱلْأَرْضُ مُدَّتْ
  Unverified discovery rationale: terra: The earth is extended as the cosmological setting for the account that follows.
- (84:4) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ
  Unverified discovery rationale: terra: It casts out what is in it and becomes empty, a resurrection image before the record is given.
- (84:5) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ
  Unverified discovery rationale: terra: The earth obeys its Lord as due, continuing the final court imagery.
- (84:6) [terra: strong (missing-ayat turn); basis: scene+theme] يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ
  Unverified discovery rationale: terra: A human labors toward the Lord and meets Him, the personal encounter underlying the easy or ruinous account in 84:7-11.
- (84:7) [luna: medium (missing-ayat turn); terra: strong; basis: scene+theme] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ
  Unverified discovery rationale: luna: The person given his record in his right hand faces an account, extending the section's debt-and-reckoning image into the final presentation of each person's account. | terra: The one given his book in the right hand receives an easy account, a formal image of merciful reckoning.
- (84:8) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene+theme] فَسَوْفَ يُحَاسَبُ حِسَابًۭا يَسِيرًۭا
  Unverified discovery rationale: luna: The next ayah promises an easy account to the one given the record in the right hand, a concrete outcome of the section's final accounting. | terra: His easy accounting spells out the favorable reckoning introduced by the record in 84:7.
- (84:10) [luna: contrast (missing-ayat turn); terra: strong; basis: contrast+scene+theme] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
  Unverified discovery rationale: luna: The other person receives his record from behind his back, a specific reversal of the right-hand presentation in 84:7 and a contrasting result within the section's day of judgment. | terra: The one given his book behind his back receives the contrary record.
- (84:11) [luna: contrast (missing-ayat turn); terra: strong; basis: contrast+neighbour+scene+theme] فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
  Unverified discovery rationale: luna: Continuing the reversed record scene, this ayah says he calls for destruction. It supplies the response to the account whose contrary outcome is developed in the following ayah. | terra: He calls for destruction, the punitive answer to the failed account of 84:10.
- (88:25) [luna: strong; basis: scene+theme] إِنَّ إِلَيْنَآ إِيَابَهُمْ
  Unverified discovery rationale: luna: “Their return is to Us” locates the final return with God, matching the section's day as the appointed close of the account.
- (88:26) [luna: strong; basis: neighbour+scene+theme] ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم
  Unverified discovery rationale: luna: This next ayah says “ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم,” putting the reckoning upon God and making explicit the accounting that 88:25's return introduces.
- (89:21) [terra: strong (missing-ayat turn); basis: neighbour+scene] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
  Unverified discovery rationale: terra: The earth is crushed repeatedly, beginning the final arrival scene in 89:22-26.
- (89:22) [terra: strong (missing-ayat turn); basis: neighbour+root+scene] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
  Unverified discovery rationale: terra: The Lord comes and angels stand rank upon rank, an explicit royal court and standing scene.
- (89:23) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
  Unverified discovery rationale: terra: Hell is brought that day and the human remembers, but remembrance is then of no use.
- (89:24) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
  Unverified discovery rationale: terra: The person wishes he had sent something ahead for his life, giving the account a debt-like forward-payment image.
- (89:25) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
  Unverified discovery rationale: terra: No one punishes as Allah punishes that day, a direct scene of divine wrath as penalty.
- (89:26) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
  Unverified discovery rationale: terra: No one binds as Allah binds, completing the sovereign punitive power of the passage.
- (99:1) [terra: strong (missing-ayat turn); basis: neighbour+scene] إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
  Unverified discovery rationale: terra: The earth is shaken with its quake, beginning the event whose deeds are measured in 99:7-8.
- (99:2) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
  Unverified discovery rationale: terra: It brings out its burdens, staging final disclosure before people see what they did.
- (99:3) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
  Unverified discovery rationale: terra: The human asks what has happened to it, registering the day as an extraordinary occurrence.
- (99:4) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
  Unverified discovery rationale: terra: The earth reports its news, making created ground a witness in the account.
- (99:5) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
  Unverified discovery rationale: terra: Its report comes by its Lord inspiration, grounding that witness in divine command.
- (99:6) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
  Unverified discovery rationale: terra: People issue separately to be shown their deeds, directly introducing the atom-weight recompense in 99:7-8.
- (99:7) [luna: strong; terra: strong; basis: scene+theme] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
  Unverified discovery rationale: luna: “مِثْقَالَ ذَرَّةٍ خَيْرًا” says even an atom's weight of good will be seen. It parallels the section's claim that no amount is too small for the day's accounting. | terra: Whoever does an atom's weight of good sees it, translating final account into the smallest measurable deed.
- (99:8) [luna: strong; terra: strong; basis: contrast+scene+theme] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
  Unverified discovery rationale: luna: This next ayah applies the same atom-weight measure to evil, completing 99:7's two-sided account and showing that the section's exact weighing reaches both kinds of deeds. | terra: Whoever does an atom's weight of evil sees it, the matching adverse measure.
- (100:9) [terra: strong (missing-ayat turn); basis: scene+theme] ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
  Unverified discovery rationale: terra: What is in graves is scattered, making resurrection a disclosure before account.
- (100:10) [terra: strong (missing-ayat turn); basis: scene+theme] وَحُصِّلَ مَا فِى ٱلصُّدُورِ
  Unverified discovery rationale: terra: What is in breasts is brought out, so inward hidden matter enters the reckoning.
- (100:11) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ
  Unverified discovery rationale: terra: Their Lord is fully aware of them that day, completing the disclosure and account scene.
- (101:6) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
  Unverified discovery rationale: luna: The section itself cites “ثَقُلَتْ مَوَازِينُهُ”; this ayah makes heavy scales the first side of the final weighing whose balance the image describes. | terra: It explicitly shows the heavy side of the scales (ثَقُلَتْ مَوَٰزِينُهُ), the section's full weight on the favorable side.
- (101:7) [luna: strong; terra: strong; basis: neighbour+scene+theme] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
  Unverified discovery rationale: luna: After 101:6's heavy scales, this ayah gives their result, “عِيشَةٍ رَّاضِيَةٍ.” It adds the favorable outcome that the section's measured recompense entails. | terra: The one with heavy scales receives a pleasing life, completing 101:6's recompense.
- (101:8) [luna: strong; terra: strong; basis: contrast+root+scene] [cited in ¶21] وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
  Unverified discovery rationale: luna: The section itself cites “خَفَّتْ مَوَازِينُهُ”; this ayah supplies the opposite side of the final weighing and marks the boundary between heavy and light accounts. | terra: It explicitly shows the light side of the scales (خَفَّتْ مَوَٰزِينُهُ), the contrary outcome of insufficient weight.
- (101:9) [luna: strong; terra: strong; basis: neighbour+scene+theme] فَأُمُّهُۥ هَاوِيَةٌۭ
  Unverified discovery rationale: luna: After 101:8's light scales, this ayah names the destination “هَاوِيَةٌ”; its contribution is the consequence of coming out light in the section's balance scene. | terra: The abyss is assigned to the one with light scales, completing the negative side of the same weighing.
- (101:10) [terra: strong; basis: neighbour+scene] وَمَآ أَدْرَىٰكَ مَا هِيَهْ
  Unverified discovery rationale: terra: Its question about the abyss intensifies the account's consequence begun by the light scales in 101:8.
- (101:11) [terra: strong; basis: neighbour+scene] نَارٌ حَامِيَةٌۢ
  Unverified discovery rationale: terra: The abyss is a blazing fire, the punitive destination tied to the failed balance.
- (102:8) [terra: strong; basis: scene+theme] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ
  Unverified discovery rationale: terra: On that day people will be questioned about blessing, showing that even received benefit enters the account.

## medium (47)

- (2:106) [terra: medium; basis: contrast+root] ۞ مَا نَنسَخْ مِنْ ءَايَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍۢ مِّنْهَآ أَوْ مِثْلِهَآ ۗ أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: A sign is replaced or caused to be forgotten and a better or similar one brought; it gives a concrete Qur'anic instance of one thing put in another's place.
- (2:245) [luna: medium; basis: root+scene+theme] مَّن ذَا ٱلَّذِى يُقْرِضُ ٱللَّهَ قَرْضًا حَسَنًۭا فَيُضَٰعِفَهُۥ لَهُۥٓ أَضْعَافًۭا كَثِيرَةًۭ ۚ وَٱللَّهُ يَقْبِضُ وَيَبْصُۜطُ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: luna: The section distinguishes the source word dīn (recompense) from the related but different word dayn (debt). This ayah's “قَرْضًا حَسَنًا” is a loan that God multiplies in return, a concrete loan-and-recompense parallel.
- (3:75) [luna: medium; basis: scene+theme] ۞ وَمِنْ أَهْلِ ٱلْكِتَٰبِ مَنْ إِن تَأْمَنْهُ بِقِنطَارٍۢ يُؤَدِّهِۦٓ إِلَيْكَ وَمِنْهُم مَّنْ إِن تَأْمَنْهُ بِدِينَارٍۢ لَّا يُؤَدِّهِۦٓ إِلَيْكَ إِلَّا مَا دُمْتَ عَلَيْهِ قَآئِمًۭا ۗ ذَٰلِكَ بِأَنَّهُمْ قَالُوا۟ لَيْسَ عَلَيْنَا فِى ٱلْأُمِّيِّۦنَ سَبِيلٌۭ وَيَقُولُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ وَهُمْ يَعْلَمُونَ
  Unverified discovery rationale: luna: The section's dictionary gloss calls a fully weighted coin a standing dinar. This ayah's “بِدِينَارٍ” places that specific coin in an entrusted-money transaction, adding a concrete monetary object to the section's debt and measure scene.
- (4:11) [terra: medium; basis: root+theme] يُوصِيكُمُ ٱللَّهُ فِىٓ أَوْلَٰدِكُمْ ۖ لِلذَّكَرِ مِثْلُ حَظِّ ٱلْأُنثَيَيْنِ ۚ فَإِن كُنَّ نِسَآءًۭ فَوْقَ ٱثْنَتَيْنِ فَلَهُنَّ ثُلُثَا مَا تَرَكَ ۖ وَإِن كَانَتْ وَٰحِدَةًۭ فَلَهَا ٱلنِّصْفُ ۚ وَلِأَبَوَيْهِ لِكُلِّ وَٰحِدٍۢ مِّنْهُمَا ٱلسُّدُسُ مِمَّا تَرَكَ إِن كَانَ لَهُۥ وَلَدٌۭ ۚ فَإِن لَّمْ يَكُن لَّهُۥ وَلَدٌۭ وَوَرِثَهُۥٓ أَبَوَاهُ فَلِأُمِّهِ ٱلثُّلُثُ ۚ فَإِن كَانَ لَهُۥٓ إِخْوَةٌۭ فَلِأُمِّهِ ٱلسُّدُسُ ۚ مِنۢ بَعْدِ وَصِيَّةٍۢ يُوصِى بِهَآ أَوْ دَيْنٍ ۗ ءَابَآؤُكُمْ وَأَبْنَآؤُكُمْ لَا تَدْرُونَ أَيُّهُمْ أَقْرَبُ لَكُمْ نَفْعًۭا ۚ فَرِيضَةًۭ مِّنَ ٱللَّهِ ۗ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
  Unverified discovery rationale: terra: Inheritance is distributed only after a bequest or debt, showing that a due claim is settled before property changes hands.
- (4:12) [terra: medium; basis: root+theme] ۞ وَلَكُمْ نِصْفُ مَا تَرَكَ أَزْوَٰجُكُمْ إِن لَّمْ يَكُن لَّهُنَّ وَلَدٌۭ ۚ فَإِن كَانَ لَهُنَّ وَلَدٌۭ فَلَكُمُ ٱلرُّبُعُ مِمَّا تَرَكْنَ ۚ مِنۢ بَعْدِ وَصِيَّةٍۢ يُوصِينَ بِهَآ أَوْ دَيْنٍۢ ۚ وَلَهُنَّ ٱلرُّبُعُ مِمَّا تَرَكْتُمْ إِن لَّمْ يَكُن لَّكُمْ وَلَدٌۭ ۚ فَإِن كَانَ لَكُمْ وَلَدٌۭ فَلَهُنَّ ٱلثُّمُنُ مِمَّا تَرَكْتُم ۚ مِّنۢ بَعْدِ وَصِيَّةٍۢ تُوصُونَ بِهَآ أَوْ دَيْنٍۢ ۗ وَإِن كَانَ رَجُلٌۭ يُورَثُ كَلَٰلَةً أَوِ ٱمْرَأَةٌۭ وَلَهُۥٓ أَخٌ أَوْ أُخْتٌۭ فَلِكُلِّ وَٰحِدٍۢ مِّنْهُمَا ٱلسُّدُسُ ۚ فَإِن كَانُوٓا۟ أَكْثَرَ مِن ذَٰلِكَ فَهُمْ شُرَكَآءُ فِى ٱلثُّلُثِ ۚ مِنۢ بَعْدِ وَصِيَّةٍۢ يُوصَىٰ بِهَآ أَوْ دَيْنٍ غَيْرَ مُضَآرٍّۢ ۚ وَصِيَّةًۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ عَلِيمٌ حَلِيمٌۭ
  Unverified discovery rationale: terra: Its repeated 'after bequest or debt' makes debt a prior, recorded obligation even at death.
- (4:58) [terra: medium; basis: theme] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
  Unverified discovery rationale: terra: Trusts are returned to their owners and judgment between people is made with justice, joining owed property to upright adjudication.
- (5:1) [terra: medium; basis: theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَوْفُوا۟ بِٱلْعُقُودِ ۚ أُحِلَّتْ لَكُم بَهِيمَةُ ٱلْأَنْعَٰمِ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ غَيْرَ مُحِلِّى ٱلصَّيْدِ وَأَنتُمْ حُرُمٌ ۗ إِنَّ ٱللَّهَ يَحْكُمُ مَا يُرِيدُ
  Unverified discovery rationale: terra: The command to fulfill contracts supplies the broader obligation that makes debt terms and written agreements morally binding.
- (5:44) [terra: medium (missing-ayat turn); basis: scene+theme] إِنَّآ أَنزَلْنَا ٱلتَّوْرَىٰةَ فِيهَا هُدًۭى وَنُورٌۭ ۚ يَحْكُمُ بِهَا ٱلنَّبِيُّونَ ٱلَّذِينَ أَسْلَمُوا۟ لِلَّذِينَ هَادُوا۟ وَٱلرَّبَّٰنِيُّونَ وَٱلْأَحْبَارُ بِمَا ٱسْتُحْفِظُوا۟ مِن كِتَٰبِ ٱللَّهِ وَكَانُوا۟ عَلَيْهِ شُهَدَآءَ ۚ فَلَا تَخْشَوُا۟ ٱلنَّاسَ وَٱخْشَوْنِ وَلَا تَشْتَرُوا۟ بِـَٔايَٰتِى ثَمَنًۭا قَلِيلًۭا ۚ وَمَن لَّمْ يَحْكُم بِمَآ أَنزَلَ ٱللَّهُ فَأُو۟لَٰٓئِكَ هُمُ ٱلْكَٰفِرُونَ
  Unverified discovery rationale: terra: The people of the Book are told not to sell Allah signs for a small price while judging by revelation, joining price to just judgment.
- (9:60) [terra: medium; basis: root+theme] ۞ إِنَّمَا ٱلصَّدَقَٰتُ لِلْفُقَرَآءِ وَٱلْمَسَٰكِينِ وَٱلْعَٰمِلِينَ عَلَيْهَا وَٱلْمُؤَلَّفَةِ قُلُوبُهُمْ وَفِى ٱلرِّقَابِ وَٱلْغَٰرِمِينَ وَفِى سَبِيلِ ٱللَّهِ وَٱبْنِ ٱلسَّبِيلِ ۖ فَرِيضَةًۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ عَلِيمٌ حَكِيمٌۭ
  Unverified discovery rationale: terra: Those burdened by debt are named among the recipients of alms, showing communal recognition of the debtor's due.
- (9:111) [luna: medium; terra: contrast; basis: contrast+scene+theme] ۞ إِنَّ ٱللَّهَ ٱشْتَرَىٰ مِنَ ٱلْمُؤْمِنِينَ أَنفُسَهُمْ وَأَمْوَٰلَهُم بِأَنَّ لَهُمُ ٱلْجَنَّةَ ۚ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ فَيَقْتُلُونَ وَيُقْتَلُونَ ۖ وَعْدًا عَلَيْهِ حَقًّۭا فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ وَٱلْقُرْءَانِ ۚ وَمَنْ أَوْفَىٰ بِعَهْدِهِۦ مِنَ ٱللَّهِ ۚ فَٱسْتَبْشِرُوا۟ بِبَيْعِكُمُ ٱلَّذِى بَايَعْتُم بِهِۦ ۚ وَذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
  Unverified discovery rationale: luna: The section makes guidance and misguidance sides of a trade. Here God “اشْتَرَىٰ” believers' lives and wealth for Paradise, a promised return that contrasts with the failed purchase in 2:16. | terra: Allah purchases believers' lives and wealth for Paradise; this is the successful divine transaction opposite buying error for guidance.
- (15:92) [terra: medium; basis: scene+theme] فَوَرَبِّكَ لَنَسْـَٔلَنَّهُمْ أَجْمَعِينَ
  Unverified discovery rationale: terra: Allah will question all of them, adding direct interrogation to the reckoning image.
- (15:93) [terra: medium; basis: neighbour+scene+theme] عَمَّا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: They will be questioned about what they used to do, completing 15:92's universal accounting.
- (16:101) [terra: medium; basis: contrast+root] وَإِذَا بَدَّلْنَآ ءَايَةًۭ مَّكَانَ ءَايَةٍۢ ۙ وَٱللَّهُ أَعْلَمُ بِمَا يُنَزِّلُ قَالُوٓا۟ إِنَّمَآ أَنتَ مُفْتَرٍۭ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
  Unverified discovery rationale: terra: When Allah substitutes one sign for another, the verse supplies another explicit scene of replacement relevant to the section's secondary غَيْر sense.
- (16:126) [terra: medium; basis: scene+theme] وَإِنْ عَاقَبْتُمْ فَعَاقِبُوا۟ بِمِثْلِ مَا عُوقِبْتُم بِهِۦ ۖ وَلَئِن صَبَرْتُمْ لَهُوَ خَيْرٌۭ لِّلصَّٰبِرِينَ
  Unverified discovery rationale: terra: Retaliation must be only equivalent to what was inflicted, giving another earthly limit to measured repayment.
- (18:48) [terra: medium; basis: scene+theme] وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا لَّقَدْ جِئْتُمُونَا كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۭ ۚ بَلْ زَعَمْتُمْ أَلَّن نَّجْعَلَ لَكُم مَّوْعِدًۭا
  Unverified discovery rationale: terra: People are presented in rows before their Lord and told they have returned as first created, a standing-and-return scene for the account.
- (22:60) [terra: medium; basis: scene+theme] ۞ ذَٰلِكَ وَمَنْ عَاقَبَ بِمِثْلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِىَ عَلَيْهِ لَيَنصُرَنَّهُ ٱللَّهُ ۗ إِنَّ ٱللَّهَ لَعَفُوٌّ غَفُورٌۭ
  Unverified discovery rationale: terra: One who responds with the like of what he suffered is promised Allah's help if wronged again; equivalence governs retaliation here too.
- (34:26) [terra: medium; basis: scene+theme] قُلْ يَجْمَعُ بَيْنَنَا رَبُّنَا ثُمَّ يَفْتَحُ بَيْنَنَا بِٱلْحَقِّ وَهُوَ ٱلْفَتَّاحُ ٱلْعَلِيمُ
  Unverified discovery rationale: terra: The Lord gathers people and opens judgment between them in truth, a compact judicial scene under His role as decisive judge.
- (35:18) [terra: medium; basis: contrast+theme] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: No bearer bears another's burden, even if a heavily burdened person calls a relative; this parallels the final day when another cannot settle one's due.
- (37:21) [terra: medium; basis: root+scene] هَٰذَا يَوْمُ ٱلْفَصْلِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
  Unverified discovery rationale: terra: 'This is the Day of Decision' identifies the denied event as a day of separating verdicts, close to the section's yawm al-ḥukm.
- (37:24) [terra: medium; basis: scene+theme] وَقِفُوهُمْ ۖ إِنَّهُم مَّسْـُٔولُونَ
  Unverified discovery rationale: terra: The gathered are stopped to be questioned, making the Day's judgment an interrogation as well as a weighing.
- (38:26) [terra: medium; basis: scene+theme] يَٰدَاوُۥدُ إِنَّا جَعَلْنَٰكَ خَلِيفَةًۭ فِى ٱلْأَرْضِ فَٱحْكُم بَيْنَ ٱلنَّاسِ بِٱلْحَقِّ وَلَا تَتَّبِعِ ٱلْهَوَىٰ فَيُضِلَّكَ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّ ٱلَّذِينَ يَضِلُّونَ عَن سَبِيلِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۢ بِمَا نَسُوا۟ يَوْمَ ٱلْحِسَابِ
  Unverified discovery rationale: terra: Forgetting the Day of Account leads to severe punishment; it turns failure to remember the reckoning into a judicial fault.
- (40:27) [terra: medium; basis: scene+theme] وَقَالَ مُوسَىٰٓ إِنِّى عُذْتُ بِرَبِّى وَرَبِّكُم مِّن كُلِّ مُتَكَبِّرٍۢ لَّا يُؤْمِنُ بِيَوْمِ ٱلْحِسَابِ
  Unverified discovery rationale: terra: Moses seeks refuge from every arrogant person who does not believe in the Day of Account, naming the day with the section's حساب.
- (42:40) [terra: medium; basis: scene+theme] وَجَزَٰٓؤُا۟ سَيِّئَةٍۢ سَيِّئَةٌۭ مِّثْلُهَا ۖ فَمَنْ عَفَا وَأَصْلَحَ فَأَجْرُهُۥ عَلَى ٱللَّهِ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: terra: The recompense of an injury is an equal injury, while pardon and reform have reward with Allah; it develops equal payment and its merciful alternative.
- (44:40) [terra: medium; basis: scene+theme] إِنَّ يَوْمَ ٱلْفَصْلِ مِيقَٰتُهُمْ أَجْمَعِينَ
  Unverified discovery rationale: terra: The Day of Decision is the appointed meeting of all, another formulation of the inevitable judgment day.
- (52:21) [terra: medium; basis: scene+theme] وَٱلَّذِينَ ءَامَنُوا۟ وَٱتَّبَعَتْهُمْ ذُرِّيَّتُهُم بِإِيمَٰنٍ أَلْحَقْنَا بِهِمْ ذُرِّيَّتَهُمْ وَمَآ أَلَتْنَٰهُم مِّنْ عَمَلِهِم مِّن شَىْءٍۢ ۚ كُلُّ ٱمْرِئٍۭ بِمَا كَسَبَ رَهِينٌۭ
  Unverified discovery rationale: terra: Every person is held in pledge for what he earned, another debt-like image of nontransferable recompense.
- (53:38) [terra: medium; basis: contrast+theme] أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ
  Unverified discovery rationale: terra: No burdened soul bears another's burden, a concise boundary on transferring the moral debt of the account.
- (55:8) [luna: medium; terra: contrast; basis: contrast+neighbour+root+scene+theme] أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ
  Unverified discovery rationale: luna: This next ayah forbids transgressing the balance. It states the boundary that the section's straight, non-leaning scale makes visible. | terra: Do not transgress the balance: its boundary explains why a scale that tips or is manipulated violates the order Allah set.
- (56:56) [terra: medium; basis: root+scene] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
  Unverified discovery rationale: terra: It names the described punishment their hospitality on the Day of Recompense, another exact دِين designation for final due.
- (58:18) [terra: medium; basis: scene+theme] يَوْمَ يَبْعَثُهُمُ ٱللَّهُ جَمِيعًۭا فَيَحْلِفُونَ لَهُۥ كَمَا يَحْلِفُونَ لَكُمْ ۖ وَيَحْسَبُونَ أَنَّهُمْ عَلَىٰ شَىْءٍ ۚ أَلَآ إِنَّهُمْ هُمُ ٱلْكَٰذِبُونَ
  Unverified discovery rationale: terra: On the day Allah resurrects them all, their false oaths fail before the One who knows their account; testimony cannot be manipulated then.
- (65:8) [terra: medium; basis: scene+theme] وَكَأَيِّن مِّن قَرْيَةٍ عَتَتْ عَنْ أَمْرِ رَبِّهَا وَرُسُلِهِۦ فَحَاسَبْنَٰهَا حِسَابًۭا شَدِيدًۭا وَعَذَّبْنَٰهَا عَذَابًۭا نُّكْرًۭا
  Unverified discovery rationale: terra: A people were called to a severe account and tasted the evil consequence of their affair, joining حساب to enacted recompense.
- (68:46) [terra: medium (missing-ayat turn); basis: root] أَمْ تَسْـَٔلُهُمْ أَجْرًۭا فَهُم مِّن مَّغْرَمٍۢ مُّثْقَلُونَ
  Unverified discovery rationale: terra: It repeats the question whether a messenger asks payment so hearers are burdened by debt, the same debt word-play as 52:40.
- (70:4) [terra: medium; basis: scene+theme] تَعْرُجُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ إِلَيْهِ فِى يَوْمٍۢ كَانَ مِقْدَارُهُۥ خَمْسِينَ أَلْفَ سَنَةٍۢ
  Unverified discovery rationale: terra: The angels ascend in a day measured as fifty thousand years, giving the section's 'heavy day' its Qur'anic sense of overwhelming scale.
- (70:26) [terra: medium; basis: root+theme] وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ
  Unverified discovery rationale: terra: The faithful affirm the Day of Recompense, treating the section's dīn as a reality with present ethical force.
- (70:40) [terra: medium (missing-ayat turn); basis: contrast+root] فَلَآ أُقْسِمُ بِرَبِّ ٱلْمَشَٰرِقِ وَٱلْمَغَٰرِبِ إِنَّا لَقَٰدِرُونَ
  Unverified discovery rationale: terra: The Lord of east and west swears He can replace people with better than them, a direct replacement formulation.
- (70:41) [terra: medium (missing-ayat turn); basis: contrast+neighbour+root] عَلَىٰٓ أَن نُّبَدِّلَ خَيْرًۭا مِّنْهُمْ وَمَا نَحْنُ بِمَسْبُوقِينَ
  Unverified discovery rationale: terra: He cannot be outstripped in replacing them, completing the alternative-to-them scene of 70:40.
- (74:8) [terra: medium; basis: scene+theme] فَإِذَا نُقِرَ فِى ٱلنَّاقُورِ
  Unverified discovery rationale: terra: When the trumpet is blown, the final event begins in the passage that calls it a difficult day.
- (74:9) [luna: medium; terra: medium; basis: neighbour+scene+theme] فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ
  Unverified discovery rationale: luna: “فَذَٰلِكَ يَوْمَئِذٍ يَوْمٌ عَسِيرٌ” calls that day difficult, paralleling the section's dictionary image of a severe day as an event that bears heavily on people. | terra: It is a difficult day, directly embodying the section's severe day rather than an ordinary unit of time.
- (74:10) [luna: medium; terra: medium; basis: neighbour+scene+theme] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
  Unverified discovery rationale: luna: This next ayah says the difficult day is not easy for disbelievers, specifying who bears its severity and completing 74:9's hard-day scene. | terra: It is not easy for the disbelievers, completing the passage's severe-day contrast.
- (74:38) [terra: medium; basis: scene+theme] كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ
  Unverified discovery rationale: terra: Every soul is held in pledge for what it earned, using a financial holding image for personal liability before punishment.
- (74:46) [terra: medium; basis: root+theme] وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ
  Unverified discovery rationale: terra: The people of the left admit that they denied the Day of Recompense, making its denial part of the path to punishment.
- (75:30) [terra: medium; basis: scene+theme] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ
  Unverified discovery rationale: terra: To the Lord is the driving on that day, concentrating all movement and return under the owner of the final affair.
- (76:7) [terra: medium; basis: scene+theme] يُوفُونَ بِٱلنَّذْرِ وَيَخَافُونَ يَوْمًۭا كَانَ شَرُّهُۥ مُسْتَطِيرًۭا
  Unverified discovery rationale: terra: The righteous fear a day whose evil is widespread, giving moral urgency to the coming recompense.
- (76:10) [terra: medium; basis: scene+theme] إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا
  Unverified discovery rationale: terra: They fear from their Lord a grim, severe day, a second explicit image of the day as crushing event.
- (78:17) [terra: medium; basis: scene+theme] إِنَّ يَوْمَ ٱلْفَصْلِ كَانَ مِيقَٰتًۭا
  Unverified discovery rationale: terra: The Day of Decision has an appointed time, matching the section's day as a scheduled event more than a mere duration.
- (83:11) [terra: medium; basis: root+theme] ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ
  Unverified discovery rationale: terra: The sinful deny the Day of Recompense; this extends the same sūrah's fraudulent scales into the refusal of final settlement.
- (84:9) [luna: medium (missing-ayat turn); basis: neighbour+scene+theme] وَيَنقَلِبُ إِلَىٰٓ أَهْلِهِۦ مَسْرُورًۭا
  Unverified discovery rationale: luna: This continuation says that person returns to his family joyful, showing the outcome of the easy account introduced in 84:8.
- (107:1) [terra: medium; basis: root+theme] أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
  Unverified discovery rationale: terra: Denying the dīn immediately appears in conduct toward the orphan and poor, showing that denial of recompense distorts present obligations.

## contrast (14)

- (2:275) [terra: contrast (missing-ayat turn); basis: contrast+root+scene] ٱلَّذِينَ يَأْكُلُونَ ٱلرِّبَوٰا۟ لَا يَقُومُونَ إِلَّا كَمَا يَقُومُ ٱلَّذِى يَتَخَبَّطُهُ ٱلشَّيْطَٰنُ مِنَ ٱلْمَسِّ ۚ ذَٰلِكَ بِأَنَّهُمْ قَالُوٓا۟ إِنَّمَا ٱلْبَيْعُ مِثْلُ ٱلرِّبَوٰا۟ ۗ وَأَحَلَّ ٱللَّهُ ٱلْبَيْعَ وَحَرَّمَ ٱلرِّبَوٰا۟ ۚ فَمَن جَآءَهُۥ مَوْعِظَةٌۭ مِّن رَّبِّهِۦ فَٱنتَهَىٰ فَلَهُۥ مَا سَلَفَ وَأَمْرُهُۥٓ إِلَى ٱللَّهِ ۖ وَمَنْ عَادَ فَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: terra: It distinguishes permitted trade from forbidden usury, setting a moral boundary inside the debt and commerce scene.
- (4:74) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] ۞ فَلْيُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ ٱلَّذِينَ يَشْرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۚ وَمَن يُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ فَيُقْتَلْ أَوْ يَغْلِبْ فَسَوْفَ نُؤْتِيهِ أَجْرًا عَظِيمًۭا
  Unverified discovery rationale: terra: Those who sell the nearer life for the Hereafter enact the saving reverse of purchasing error or worldly value at final loss.
- (9:39) [terra: contrast (missing-ayat turn); basis: contrast+root] إِلَّا تَنفِرُوا۟ يُعَذِّبْكُمْ عَذَابًا أَلِيمًۭا وَيَسْتَبْدِلْ قَوْمًا غَيْرَكُمْ وَلَا تَضُرُّوهُ شَيْـًۭٔا ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
  Unverified discovery rationale: terra: Refusing to go forth brings punishment and replacement by another people, making غَيْر a warning of communal substitution.
- (21:23) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] لَا يُسْـَٔلُ عَمَّا يَفْعَلُ وَهُمْ يُسْـَٔلُونَ
  Unverified discovery rationale: terra: Allah is not questioned about what He does while people are questioned, distinguishing the sovereign judge from accountable servants.
- (61:10) [terra: contrast; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ هَلْ أَدُلُّكُمْ عَلَىٰ تِجَٰرَةٍۢ تُنجِيكُم مِّنْ عَذَابٍ أَلِيمٍۢ
  Unverified discovery rationale: terra: It offers a trade that saves from painful punishment, deliberately answering the section's unprofitable commerce with a saving exchange.
- (61:11) [terra: contrast; basis: contrast+scene+theme] تُؤْمِنُونَ بِٱللَّهِ وَرَسُولِهِۦ وَتُجَٰهِدُونَ فِى سَبِيلِ ٱللَّهِ بِأَمْوَٰلِكُمْ وَأَنفُسِكُمْ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: Faith and striving are the contents of that saving trade, instead of the error and near life bought in the bad transactions.
- (61:12) [terra: contrast; basis: contrast+scene+theme] يَغْفِرْ لَكُمْ ذُنُوبَكُمْ وَيُدْخِلْكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
  Unverified discovery rationale: terra: Forgiveness and Paradise are its promised return, showing what a true recompense can be.
- (74:48) [terra: contrast (missing-ayat turn); basis: contrast+theme] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
  Unverified discovery rationale: terra: No intercession benefits them, setting a clear limit on advocacy at the punitive outcome of denying the Day of Recompense.
- (79:37) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] فَأَمَّا مَن طَغَىٰ
  Unverified discovery rationale: terra: The one who transgressed and preferred the nearer life receives the negative side of final valuation.
- (79:38) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: terra: Hell is the shelter for that preference, giving the near-life transaction its settled result.
- (79:40) [terra: contrast (missing-ayat turn); basis: contrast+scene+theme] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
  Unverified discovery rationale: terra: One who feared standing before the Lord and restrained desire takes the opposite orientation to preferring the nearer life.
- (79:41) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene+theme] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: terra: Paradise is the shelter for that restraint, completing the favorable side of the same final contrast.
- (83:3) [luna: contrast; terra: contrast; basis: contrast+root+scene] [cited in ¶21] وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ
  Unverified discovery rationale: luna: The section's image is a scale that does not lean. Here sellers “يُخْسِرُونَ” when they measure or weigh for others, a direct reversal: they make the worldly measure lean before standing for judgment. | terra: When measuring or weighing for others they give less (يُخْسِرُونَ), the inverse of the upright scale tied to مُسْتَقِيم.
- (84:12) [luna: contrast (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَيَصْلَىٰ سَعِيرًا
  Unverified discovery rationale: luna: This next ayah says he will enter a blaze, completing the consequence of the rejected account in 84:10–11 and contrasting with the easy account's joyful return in 84:8–9.

## neighbours: within two ayat of a passage the section cites (35)

- (2:14) [next to 2:16] وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ إِلَىٰ شَيَٰطِينِهِمْ قَالُوٓا۟ إِنَّا مَعَكُمْ إِنَّمَا نَحْنُ مُسْتَهْزِءُونَ
- (2:15) [next to 2:16] ٱللَّهُ يَسْتَهْزِئُ بِهِمْ وَيَمُدُّهُمْ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (2:17) [next to 2:16] مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ
- (2:18) [next to 2:16] صُمٌّۢ بُكْمٌ عُمْىٌۭ فَهُمْ لَا يَرْجِعُونَ
- (2:176) [next to 2:178] ذَٰلِكَ بِأَنَّ ٱللَّهَ نَزَّلَ ٱلْكِتَٰبَ بِٱلْحَقِّ ۗ وَإِنَّ ٱلَّذِينَ ٱخْتَلَفُوا۟ فِى ٱلْكِتَٰبِ لَفِى شِقَاقٍۭ بَعِيدٍۢ
- (2:177) [next to 2:178] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
- (2:180) [next to 2:178] كُتِبَ عَلَيْكُمْ إِذَا حَضَرَ أَحَدَكُمُ ٱلْمَوْتُ إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ لِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ بِٱلْمَعْرُوفِ ۖ حَقًّا عَلَى ٱلْمُتَّقِينَ
- (4:90) [next to 4:92] إِلَّا ٱلَّذِينَ يَصِلُونَ إِلَىٰ قَوْمٍۭ بَيْنَكُمْ وَبَيْنَهُم مِّيثَٰقٌ أَوْ جَآءُوكُمْ حَصِرَتْ صُدُورُهُمْ أَن يُقَٰتِلُوكُمْ أَوْ يُقَٰتِلُوا۟ قَوْمَهُمْ ۚ وَلَوْ شَآءَ ٱللَّهُ لَسَلَّطَهُمْ عَلَيْكُمْ فَلَقَٰتَلُوكُمْ ۚ فَإِنِ ٱعْتَزَلُوكُمْ فَلَمْ يُقَٰتِلُوكُمْ وَأَلْقَوْا۟ إِلَيْكُمُ ٱلسَّلَمَ فَمَا جَعَلَ ٱللَّهُ لَكُمْ عَلَيْهِمْ سَبِيلًۭا
- (4:91) [next to 4:92] سَتَجِدُونَ ءَاخَرِينَ يُرِيدُونَ أَن يَأْمَنُوكُمْ وَيَأْمَنُوا۟ قَوْمَهُمْ كُلَّ مَا رُدُّوٓا۟ إِلَى ٱلْفِتْنَةِ أُرْكِسُوا۟ فِيهَا ۚ فَإِن لَّمْ يَعْتَزِلُوكُمْ وَيُلْقُوٓا۟ إِلَيْكُمُ ٱلسَّلَمَ وَيَكُفُّوٓا۟ أَيْدِيَهُمْ فَخُذُوهُمْ وَٱقْتُلُوهُمْ حَيْثُ ثَقِفْتُمُوهُمْ ۚ وَأُو۟لَٰٓئِكُمْ جَعَلْنَا لَكُمْ عَلَيْهِمْ سُلْطَٰنًۭا مُّبِينًۭا
- (4:94) [next to 4:92] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا ضَرَبْتُمْ فِى سَبِيلِ ٱللَّهِ فَتَبَيَّنُوا۟ وَلَا تَقُولُوا۟ لِمَنْ أَلْقَىٰٓ إِلَيْكُمُ ٱلسَّلَٰمَ لَسْتَ مُؤْمِنًۭا تَبْتَغُونَ عَرَضَ ٱلْحَيَوٰةِ ٱلدُّنْيَا فَعِندَ ٱللَّهِ مَغَانِمُ كَثِيرَةٌۭ ۚ كَذَٰلِكَ كُنتُم مِّن قَبْلُ فَمَنَّ ٱللَّهُ عَلَيْكُمْ فَتَبَيَّنُوٓا۟ ۚ إِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
- (6:68) [next to 6:70] وَإِذَا رَأَيْتَ ٱلَّذِينَ يَخُوضُونَ فِىٓ ءَايَٰتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦ ۚ وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (6:69) [next to 6:70] وَمَا عَلَى ٱلَّذِينَ يَتَّقُونَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَلَٰكِن ذِكْرَىٰ لَعَلَّهُمْ يَتَّقُونَ
- (6:71) [next to 6:70] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:72) [next to 6:70] وَأَنْ أَقِيمُوا۟ ٱلصَّلَوٰةَ وَٱتَّقُوهُ ۚ وَهُوَ ٱلَّذِىٓ إِلَيْهِ تُحْشَرُونَ
- (17:34) [next to 17:35] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۚ وَأَوْفُوا۟ بِٱلْعَهْدِ ۖ إِنَّ ٱلْعَهْدَ كَانَ مَسْـُٔولًۭا
- (17:36) [next to 17:35] وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ ۚ إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًۭا
- (17:37) [next to 17:35] وَلَا تَمْشِ فِى ٱلْأَرْضِ مَرَحًا ۖ إِنَّكَ لَن تَخْرِقَ ٱلْأَرْضَ وَلَن تَبْلُغَ ٱلْجِبَالَ طُولًۭا
- (21:45) [next to 21:47] قُلْ إِنَّمَآ أُنذِرُكُم بِٱلْوَحْىِ ۚ وَلَا يَسْمَعُ ٱلصُّمُّ ٱلدُّعَآءَ إِذَا مَا يُنذَرُونَ
- (21:46) [next to 21:47] وَلَئِن مَّسَّتْهُمْ نَفْحَةٌۭ مِّنْ عَذَابِ رَبِّكَ لَيَقُولُنَّ يَٰوَيْلَنَآ إِنَّا كُنَّا ظَٰلِمِينَ
- (21:48) [next to 21:47] وَلَقَدْ ءَاتَيْنَا مُوسَىٰ وَهَٰرُونَ ٱلْفُرْقَانَ وَضِيَآءًۭ وَذِكْرًۭا لِّلْمُتَّقِينَ
- (21:49) [next to 21:47] ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَهُم مِّنَ ٱلسَّاعَةِ مُشْفِقُونَ
- (25:27) [next to 25:26] وَيَوْمَ يَعَضُّ ٱلظَّالِمُ عَلَىٰ يَدَيْهِ يَقُولُ يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا
- (25:28) [next to 25:26] يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا
- (26:83) [next to 26:82] رَبِّ هَبْ لِى حُكْمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (26:84) [next to 26:82] وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ
- (26:180) [next to 26:182] وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ ۖ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ
- (26:184) [next to 26:182] وَٱتَّقُوا۟ ٱلَّذِى خَلَقَكُمْ وَٱلْجِبِلَّةَ ٱلْأَوَّلِينَ
- (40:14) [next to 40:16] فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (51:4) [next to 51:6] فَٱلْمُقَسِّمَٰتِ أَمْرًا
- (51:7) [next to 51:6] وَٱلسَّمَآءِ ذَاتِ ٱلْحُبُكِ
- (51:8) [next to 51:6] إِنَّكُمْ لَفِى قَوْلٍۢ مُّخْتَلِفٍۢ
- (83:7) [next to 83:6] كَلَّآ إِنَّ كِتَٰبَ ٱلْفُجَّارِ لَفِى سِجِّينٍۢ
- (83:8) [next to 83:6] وَمَآ أَدْرَىٰكَ مَا سِجِّينٌۭ
- (101:4) [next to 101:6] يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- (101:5) [next to 101:6] وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 1, "section": 3, "run_tag": "revision3", "source_sha256": "782be8c16d10f4684dc7f79db8acefd312f3ca466c57cffa1c3ce02d6429dea7", "list_sha256": "acd2d016621c6daace7ac81e3ddab6a85e50a349e34ac400a84b5075e57186fc", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision3/sec3/luna/run.log.json", "validation_review": {"reviewed_findings": [{"line": 3, "ref": "82:19", "arabic": "لَا تَمْلِكُ نَفْسٌ لِّنَفْسٍ شَيْئًا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Ordinary/Uthmani orthographic difference; wording and reference agree."}, {"line": 34, "ref": "2:282", "arabic": "تَضِلَّ إِحْدَاهُمَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Ordinary/Uthmani orthographic difference; wording and reference agree."}, {"line": 64, "ref": "20:111", "arabic": "الْحَيِّ الْقَيُّومِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["2:255", "3:2"], "matching_ref_count": 2, "assessment": "Title quoted without attached preposition: canonical للحي القيوم; no wrong-ayah or substantive lexical mismatch."}], "confirmed_quotation_errors": 0, "scope": "All three automated Arabic flags adjudicated against canonical text; no exhaustive semantic audit."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision3/sec3/luna/list.tsv", "rows": 91, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 3, "ref": "82:19", "arabic": "لَا تَمْلِكُ نَفْسٌ لِّنَفْسٍ شَيْئًا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 34, "ref": "2:282", "arabic": "تَضِلَّ إِحْدَاهُمَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 64, "ref": "20:111", "arabic": "الْحَيِّ الْقَيُّومِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["2:255", "3:2"], "matching_ref_count": 2}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision3/sec3/terra/run.log.json", "validation_review": {"reviewed_findings": [{"line": 13, "ref": "83:3", "arabic": "مُسْتَقِيم", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 15, "ref": "83:5", "arabic": "عظیم", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 36, "ref": "17:35", "arabic": "ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 38, "ref": "26:182", "arabic": "ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 51, "ref": "2:178", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 123, "ref": "22:56", "arabic": "ملك", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 129, "ref": "47:38", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 133, "ref": "48:6", "arabic": "ٱلْمَغْضُوبِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 155, "ref": "65:8", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 156, "ref": "40:27", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 160, "ref": "56:56", "arabic": "دِين", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 169, "ref": "16:101", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 192, "ref": "9:39", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 194, "ref": "13:41", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}, {"line": 217, "ref": "38:16", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0, "assessment": "Source-section term or lemma, attached-preposition difference, or ordinary/Uthmani/Persian-letter spelling; no substantive wrong-ayah Arabic quotation in this flagged span."}], "confirmed_wording_issues": 0, "additional_semantic_findings": [{"ref": "65:8", "finding": "English note adds tasting the consequence from 65:9; 65:8 supplies severe account and punishment."}, {"ref": "79:37", "finding": "English note adds preferring the nearer life from 79:38; 79:37 only names transgression."}, {"ref": "17:71", "finding": "Calling with a record is an interpretive rendering of imam, not an unambiguous literal gloss; retain as unverified."}], "sampling": {"method": "Every twelfth appended row, beginning with first appended row; all automatic Arabic flags.", "scope_observation": "Many additions have concrete accounting, debt, court or substitution links. Generic resurrection questions and long continuations still warrant grading review. Root basis sometimes denotes semantic family, not shared letters."}, "limits": "No exhaustive English/relevance validation. Raw TSV preserved."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision3/sec3/terra/list.tsv", "rows": 282, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 13, "ref": "83:3", "arabic": "مُسْتَقِيم", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 15, "ref": "83:5", "arabic": "عظیم", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 36, "ref": "17:35", "arabic": "ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 38, "ref": "26:182", "arabic": "ٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 51, "ref": "2:178", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 123, "ref": "22:56", "arabic": "ملك", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 129, "ref": "47:38", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 133, "ref": "48:6", "arabic": "ٱلْمَغْضُوبِ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 155, "ref": "65:8", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 156, "ref": "40:27", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 160, "ref": "56:56", "arabic": "دِين", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 169, "ref": "16:101", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 192, "ref": "9:39", "arabic": "غَيْر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 194, "ref": "13:41", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 217, "ref": "38:16", "arabic": "حساب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

