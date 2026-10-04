Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:4; its ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/augment9/augment.md =====
You are completing a finished Turkish commentary written by another reader with
what the Quran itself says about it: the Quran explaining the Quran. Below are
the commentary, with its prose paragraphs numbered [¶n]; its ledger; and Quran
passages from an earlier cross-reference list, each with its Arabic, its tier,
and the paragraphs of the commentary that already cite it, if any. A tier is
that list's own judgement, not yours; the list is not authoritative and may be
incomplete.

Read the commentary first. Then judge every listed passage, one by one, against
every paragraph: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the paragraph's ayah leaves
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

Then go through the commentary paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; ayat that state the same thing in other
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
passage from your own knowledge that you weighed, marked "own":
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/1_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_4.reading.tr.md (prose paragraphs numbered) =====
## Övgünün bir güne uzanması

[¶1] Dördüncü ayet tek başına bir cümle değildir. İkinci ayet {ar:ٱلْحَمْدُ لِلَّهِ, tr:el-hamdü lillâh, gloss:hamd Allah'adır, source:1:2} diye başlar ve Allah'ı art arda gelen adlarla anlatır: âlemlerin Rabbi, Rahman, Rahim ve şimdi {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}. "Mâliki" kelimesinin sonundaki esre onu bu zincire bağlar. Hamd hâlâ sürmektedir. Önceki adlar varlıkların bütününe ve rahmete uzanıyordu. Bu ad ise bir zamana uzanır. İnsan bir toprağa, bir sürüye ya da bir eve sahip olur, burada sahip olunan şey ise bir gündür. Bir zamanın sahibi olmak, o zamanda olacak her şeyin onun elinde olması demektir. Sure Allah'tan üçüncü şahısla en son burada söz eder. Beşinci ayette konuşan kişi O'na doğrudan seslenir: {ar:إِيَّاكَ نَعْبُدُ, tr:iyyâke na'büdü, gloss:yalnız sana kulluk ederiz, source:1:5}. Sahibin adı anıldıktan sonra konuşma yüz yüze döner.

[¶2] Kelimenin yazısında mim harfinin üstündeki küçük elif uzun "â" sesini gösterir. Harflerin gövdesi m-l-k'dir. Kur'an Allah'ı bu kökten iki ayrı kelimeyle anar. Peygambere şöyle dua etmesi söylenir: {ar:قُلِ ٱللَّهُمَّ مَٰلِكَ ٱلْمُلْكِ, tr:kulillâhümme mâlike'l-mülk, gloss:de ki: Allah'ım, ey mülkün sahibi, source:3:26}. Kur'an'ın son suresinde ise sığınılan, "insanların Rabbi"dir ve hemen ardından O, {ar:مَلِكِ ٱلنَّاسِ, tr:meliki'n-nâs, gloss:insanların hükümdarı, source:114:2} ve {ar:إِلَٰهِ ٱلنَّاسِ, tr:ilâhi'n-nâs, gloss:insanların ilahı, source:114:3} diye anılır. Rab, hükümdar ve ilah sırası Fâtiha'daki Allah, Rab ve sahip sırasıyla aynı malzemeden kurulur. "Mâlik" (sahip) ile "melik" (hükümdar) aynı kökten iki ayrı kelimedir. Araplar ikisini Allah için yan yana da söylerdi: {ar:الملك لله المالك المليك, tr:el-mülkü lillâhi'l-mâliki'l-melîk, gloss:mülk, sahip ve hükümdar olan Allah'ındır, source:"م ل ك,B003"}. Sahip elinde tuttuğunu kullanır. Hükümdar ise bir topluluğu yönetir: {ar:الملك هو المتصرف بالأمر والنهي في الجمهور, tr:el-melikü hüve'l-mütesarrifü bi'l-emri ve'n-nehyi fi'l-cumhûr, gloss:melik, topluluk üzerinde emir ve yasakla tasarruf edendir, source:"م ل ك,B003"}. Türkçede "memleket" bugün insanın doğup büyüdüğü yer ya da bir ülke demektir. Arapçada ise kelime toprağı değil, bir yetkiyi adlandırır: {ar:المملكة سلطان الملك في رعيته, tr:el-memleketü sultânü'l-meliki fî raiyyetih, gloss:memleket, hükümdarın halkı üzerindeki yetkisidir, source:"م ل ك,B003"}.

[¶3] Kur'an bu ayetin sorusunu bir yerde kendisi sorar ve cevabını bu ayetin ilk kelimesiyle verir. Gün art arda iki kez sorulur: {ar:وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:ve mâ edrâke mâ yevmü'd-dîn, gloss:din gününün ne olduğunu sana ne bildirdi, source:82:17}, {ar:ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:sümme mâ edrâke mâ yevmü'd-dîn, gloss:sonra, din gününün ne olduğunu sana ne bildirdi, source:82:18}. Cevap şudur: {ar:يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا ۖ وَٱلْأَمْرُ يَوْمَئِذٍۢ لِّلَّهِ, tr:yevme lâ temlikü nefsün li-nefsin şey'â, ve'l-emru yevmeizin lillâh, gloss:o gün hiçbir kimse bir başkası için hiçbir şeye sahip olamaz; o gün emir Allah'ındır, source:82:19}. "Temlikü" ile "mâlik" aynı köktendir. Kur'an'ın kendi tarifinde din günü, sahip olmak fiilinin herkes için olumsuz söylendiği gündür. O gün bir sahip vardır, çünkü öteki bütün sahiplikler düşmüştür. Mülk her zaman O'nundur, ama dünyada insanlara da bir sahiplik verilir. Üç yüz kırk dokuzuncu değil, yukarıdaki dua bunu açıkça söyler: {ar:تُؤْتِى ٱلْمُلْكَ مَن تَشَآءُ وَتَنزِعُ ٱلْمُلْكَ مِمَّن تَشَآءُ, tr:tü'ti'l-mülke men teşâü ve tenzi'u'l-mülke mimmen teşâ, gloss:mülkü dilediğine verirsin, dilediğinden çekip alırsın, source:3:26}. Mülk verilen ve geri alınan bir şeydir. Başka bir yerde insanların ortaya çıktığı ve hiçbir şeylerinin Allah'tan gizli kalmadığı bir gün anlatılır. O gün bir soru sorulur ve cevabını soran kendisi verir: {ar:لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ, tr:li-meni'l-mülkü'l-yevm, lillâhi'l-vâhidi'l-kahhâr, gloss:bugün mülk kimindir? Bir ve her şeye galip gelen Allah'ın, source:40:16}. Mülkün kimde olduğu sorusunun dünyada birçok cevabı vardır. Din günü bu sorunun tek bir cevabının kaldığı gündür.

## Güneşle ölçülmeyen gün

[¶4] "Gün" kelimesinin gündelik anlamı güneşe bağlıdır: {ar:اليوم مقداره من طلوع الشمس إلى غروبها, tr:el-yevmü mikdâruhû min tulû'i'ş-şemsi ilâ gurûbihâ, gloss:günün ölçüsü güneşin doğuşundan batışına kadardır, source:"ي و م,B001"}. Bir kelimenin akrabalarından gelen görüntüler, kelimenin bu ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Güneşin tepeye dikilip gölgenin kaybolduğu öğle anını altıncı ayetin {ar:ٱلْمُسْتَقِيمَ, tr:el-müstakîm, gloss:dosdoğru, source:1:6} kelimesi adlandırır. Bu ayetteki "yevm" o gökyüzü sahnesine güneşle ölçülen günü verir.

[¶5] Kur'an ise din gününü anlatırken bu ölçüyü bozar. Bir surenin başında, gelip çatacak bir azabı soran birinden söz edilir {source:70:1}. Ardından meleklerin ve ruhun Allah'a yükseldiği gün şöyle anlatılır: {ar:فِى يَوْمٍۢ كَانَ مِقْدَارُهُۥ خَمْسِينَ أَلْفَ سَنَةٍۢ, tr:fî yevmin kâne mikdâruhû hamsîne elfe sene, gloss:ölçüsü elli bin yıl olan bir günde, source:70:4}. Günün ölçüsünü güneşin yolculuğuyla veren tanımdaki "mikdâr" kelimesi burada da geçer, ama ölçü artık güneşin değildir. Aynı sure biraz sonra {ar:وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ, tr:ve'llezîne yusaddikûne bi-yevmi'd-dîn, gloss:din gününü doğrulayanlar, source:70:26} diye bu ayetin adını anar. O günde güneşin kendisi de dürülür: {ar:إِذَا ٱلشَّمْسُ كُوِّرَتْ, tr:ize'ş-şemsü kuvviret, gloss:güneş dürüldüğünde, source:81:1}.

[¶6] Güneşle ölçülmeyen bir gün, kelimenin öteki anlamlarına yaslanır. "Yevm" herhangi bir zaman dilimi için de kullanılır: {ar:مدة من الزمان أي مدة كانت, tr:müddetün mine'z-zamâni eyyü müddetin kânet, gloss:zamandan bir süre, hangi süre olursa olsun, source:"ي و م,B002"}. En güçlü anlamı ise insanların başına gelen büyük olaydır: {ar:اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت, tr:el-yevm: el-kevn, el-kâinetü mine'l-kevni izâ nezelet ev hadeset, gloss:gün, inen ya da meydana gelen olaydır, source:"ي و م,B003"}. Araplar kelimeyi büyük işler için ödünç alır, {ar:يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل, tr:yesta'îrûnehû fi'l-emri'l-azîm ve yekûlûne ni'me fülânün fi'l-yevmi izâ nezel, gloss:onu büyük iş için ödünç alırlar ve "gün indiğinde falanca ne iyi adamdır" derler, source:"ي و م,B003"} diye konuşurlardı. Burada gün, bir savaşın ya da bir felaketin gelip çattığı andır. İnsanın ne olduğu o an anlaşılır. Ağır bir güne {ar:اليوم الشديد: يوم ذو أيام, tr:el-yevmü'ş-şedîd: yevmün zû eyyâm, gloss:çetin gün, içinde birçok gün taşıyan gündür, source:"ي و م,B003"} denir. Kur'an din gününü de böyle, gelip çatan bir olay olarak anar: {ar:وَإِنَّ ٱلدِّينَ لَوَٰقِعٌۭ, tr:ve inne'd-dîne le-vâki', gloss:hesap ve karşılık mutlaka gelip çatacaktır, source:51:6}. "Vâki'", düşen ve gelip çatan demektir. Takvimde sırası gelen bir gün değildir bu, insanın üstüne inen bir gündür. "Yevm" kelimesi "iz" ile birleşip {ar:يومئذ, tr:yevmeizin, gloss:o gün, source:"ي و م,B005"} olur. Kur'an o günü anlatırken bu sözü sık kullanır. Yukarıda gördüğümüz cevaptaki "emir o gün Allah'ındır" sözü de bu kelimeyle kurulur.

## Elin sıkı tutuşu ve gevşeyen eller

[¶7] "Mâlik" kelimesinin kökü bir güce ve sağlamlığa işaret eder: {ar:أصل صحيح يدل على قوة في الشيء وصحة, tr:aslun sahîhun yedüllü alâ kuvvetin fi'ş-şey'i ve sıhha, gloss:bir şeydeki güce ve sağlamlığa işaret eden bir kök, source:"م ل ك,B001"}. Bu gücün en somut hali hamur teknesinde görülür. Hamuru sıkıca yoğurmak bu kökle söylenir: {ar:ملكت العجين إذا شددت عجنه, tr:melektü'l-acîne izâ şededtü acneh, gloss:hamuru sıkıca yoğurduğumda "melektü" derim, source:"م ل ك,B001"}. Gevşek yoğrulmuş hamur elde dağılır, sıkı yoğrulmuş hamur ise bir arada durur ve şeklini korur. Yani Arapçada sahip olmanın kökünde, bir şeyi dağılmayacak kadar sıkı kavrayan yoğurucu bir el vardır. Tutunması olmayan, bir arada duramayan duvar için {ar:حائط ليس له ملاك أي تماسك, tr:hâitun leyse lehû milâkün ey temâsük, gloss:"milâk"ı, yani bir arada tutunması olmayan duvar, source:"م ل ك,B001"} denir. Mülk de bu elden tanımlanır: {ar:الملك ما ملكت اليد من مال وخول, tr:el-milkü mâ meleketi'l-yedü min mâlin ve haval, gloss:mülk, elin sahip olduğu mal ve hizmetkârlardır, source:"م ل ك,B002"}. Hükümdarlığın adının gerekçesi de aynı eldir: {ar:لأن يده فيه قوية صحيحة, tr:li-enne yedehû fîhi kaviyyetün sahîha, gloss:çünkü onun üzerindeki eli güçlü ve sağlamdır, source:"م ل ك,B003"}. Türkçede "mülk" çoğunlukla tapulu bir ev ya da arsa demektir. Arapçadaki kelime ise elin tuttuğu her şeyi, malı da hizmetkârları da kapsar ve kökünde o elin kavrayışını taşır.

[¶8] Bir şeyi ayakta tutan dayanak da bu kökten adlandırılır. Kalp için {ar:القلب ملاك الجسد, tr:el-kalbü milâkü'l-cesed, gloss:kalp bedenin dayanağıdır, onu bir arada tutandır, source:"م ل ك,B005"} denir. Su için de aynı söz kullanılır: {ar:الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر, tr:el-mâü milâkü'l-eşyâ, yudrabu li'ş-şey'i'llezî bihî kemâlü'l-emr, gloss:su her şeyin dayanağıdır; bir işi tamamlayan şey için örnek olarak söylenir, source:"م ل ك,B007"}. Çölde yolcunun yanında taşıdığı su da bu kökten bir adla anılırdı. Gerekçesi şuydu: {ar:لأنه إذا كان معه ملك أمره, tr:li-ennehû izâ kâne meahû maleke emrah, gloss:çünkü su yanındaysa işinin sahibi olur, source:"م ل ك,B007"}. Suyu olan yolcu yürür, susuz kalan yolda kalır. Kişinin kendi işine sahip olması, yanında onu sürdürecek şeyi taşımasıdır. Yol ile suyun buluştuğu sahne altıncı ayetin yol isteğine ve yedinci ayetin {ar:أَنْعَمْتَ, tr:en'amte, gloss:nimet verdin, source:1:7} kelimesine aittir. Buradaki su, yolcunun elindeki işin adıdır.

[¶9] Din günü bu tutuşların gevşediği gündür. İbrahim kavmine taptıklarını sorar, sonra Rabbini anlatıp duaya geçer. Bu konuşmada Rabbini {ar:وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ, tr:ve'llezî atmau en yağfira lî hatîetî yevme'd-dîn, gloss:din günü hatamı bağışlamasını umduğum O'dur, source:26:82} diye anar. Duasının sonunda o günü şöyle anlatır: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlün ve lâ benûn, gloss:ne malın ne oğulların fayda verdiği gün, source:26:88}, {ar:إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ, tr:illâ men ete'llâhe bi-kalbin selîm, gloss:ancak Allah'a sağlam bir kalple gelen müstesna, source:26:89}. Buradaki "mal", mülkün tanımında geçen "elin sahip olduğu mal"dır ve o gün işe yaramaz. İşe yarayan tek şey, Arapların bedenin "milâk"ı dediği kalptir. Bunlar iki ayrı sözdür, aynı kelime değildir. Yan yana konduklarında ise aynı şeyi söylerler: O gün sayılan şey insanın elinde tuttuğu değil, onu içeriden bir arada tutandır.

[¶10] Suyun da o gün nasıl el değiştirdiği anlatılır. Ateşte olanlar cennettekilere seslenip {ar:أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ, tr:en efîdû aleynâ mine'l-mâi ev mimmâ razakakümu'llâh, gloss:üzerimize biraz su ya da Allah'ın size verdiği rızıktan dökün, source:7:50} derler. Cevap şudur: {ar:قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ, tr:kâlû inna'llâhe harramehümâ ale'l-kâfirîn, gloss:dediler ki: Allah ikisini de inkârcılara yasakladı, source:7:50}. Ardından bu insanlar anlatılır: {ar:ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا, tr:ellezîne'ttehazû dînehüm lehven ve le'iben, gloss:dinlerini eğlence ve oyun edinenler, source:7:51}. Allah onlar hakkında şöyle der: {ar:فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا, tr:fe'l-yevme nensâhüm kemâ nesû likâe yevmihim hâzâ, gloss:bugün onlar bu günlerine kavuşmayı nasıl unuttularsa biz de onları öyle unuturuz, source:7:51}. Yolcunun işini ayakta tutan su o gün istenerek elde edilemez. Bunu yaşayanlar, "dîn" kelimesini oyuna çevirip "bu günlerini" unutanlardır.

[¶11] İnsanların birbirine bağlanması da bu kökün diliyle söylenir. Evlendirmeye {ar:الإملاك التزويج, tr:el-imlâkü't-tezvîc, gloss:imlâk, evlendirmektir, source:"م ل ك,B004"} denir. Nikâh meclisine katılan da {ar:شهدنا إملاك فلان, tr:şehidnâ imlâke fülân, gloss:falancanın nikâhında bulunduk, source:"م ل ك,B004"} derdi. Gelinin kocasının evine götürülmesi altıncı ayetteki {ar:ٱهْدِنَا, tr:ihdinâ, gloss:bizi ilet, source:1:6} kelimesinin sahnesidir. Burada kökün gösterdiği şey, evlilik bağının da bir tutuş olarak adlandırılmasıdır. O gün bu bağ da çözülür: {ar:يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ, tr:yevme yeferru'l-mer'ü min ahîh, gloss:o gün kişi kardeşinden kaçar, source:80:34}, {ar:وَأُمِّهِۦ وَأَبِيهِ, tr:ve ümmihî ve ebîh, gloss:annesinden ve babasından, source:80:35}, {ar:وَصَٰحِبَتِهِۦ وَبَنِيهِ, tr:ve sâhibetihî ve benîh, gloss:eşinden ve oğullarından, source:80:36}, {ar:لِكُلِّ ٱمْرِئٍۢ مِّنْهُمْ يَوْمَئِذٍۢ شَأْنٌۭ يُغْنِيهِ, tr:li-kulli'mriin minhüm yevmeizin şe'nün yuğnîh, gloss:o gün onlardan her birinin kendine yetecek bir derdi vardır, source:80:37}. "Hiçbir kimse bir başkası için hiçbir şeye sahip olamaz" cümlesi, bu kaçışta bir insan yüzü kazanır.

## Önde yürüyen

[¶12] Kökün bir başka kullanımında sahip, elinde tutan değil, önden yürüyen kişidir. Arıların başındaki arı için {ar:مليك النحل يعسوبها, tr:melîkü'n-nahli ya'sûbühâ, gloss:arıların melîki, onların beyidir, source:"م ل ك,B008"} denir. Deve ve koyun sürüsünde de bu kökten bir ad, sürünün {ar:ما يتقدم ويتبعه سائره, tr:mâ yetekaddemü ve yetbe'uhû sâiruh, gloss:önden giden ve geri kalanların izlediği, source:"م ل ك,B008"} hayvanına verilir. Sürü bir yöne kendiliğinden gitmez. Öndeki hayvan yola çıkar, ötekiler onun izine basar. Bineğin de bu adla anılan parçaları vardır: {ar:قوائمها وهاديها, tr:kavâimühâ ve hâdîhâ, gloss:ayakları ve boynu, source:"م ل ك,B008"}. Biri yükü taşır, öteki yönü verir. Önden yürüyen kılavuzun ve sürünün başındaki öncünün sahnesi altıncı ayetin "ihdinâ" kelimesiyle kurulur. Bu ayetin kelimesi o sahneye, önde yürüyenin bir tür sahip olduğunu ekler.

[¶13] Yolun kendisinde de bu kökten bir yer vardır. Bir yolcuya {ar:الزم ملك الطريق أي وسطه, tr:elzim milke't-tarîki ey vasatah, gloss:yolun "milk"inden, yani ortasından ayrılma, source:"م ل ك,B006"} denirdi. Aynı söz bir yerleşimin ortası için de kullanılır: {ar:أراد بالمملكة وسطها وملك الطريق معظمه ووسطه, tr:erâde bi'l-memleketi vasatahâ ve milkü't-tarîki mu'zamuhû ve vasatuh, gloss:"memleket" ile ortasını kastetti; yolun "milk"i, onun ana kesimi ve ortasıdır, source:"م ل ك,B006"}. Bir yolun yükünü taşıyan, kalabalığın aktığı orta kesimi, sahiplik kelimesiyle anılır. Yolun ortasında kalmak ile yoldan sapmak arasındaki gerilim altıncı ve yedinci ayetlerin kelimeleriyle kurulur.

[¶14] Din günü kimin önde yürüdüğü sorusuna da cevap verir. Kur'an o günün başlangıcını anlatır: Dağlar savrulmuş, yer ne bir eğrilik ne bir tümsek kalmayacak şekilde düzlenmiştir {source:20:107}. Sonra şöyle der: {ar:يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:yevmeizin yettebi'ûne'd-dâ'iye lâ ıvece leh, ve haşeati'l-asvâtü li'r-rahmâni fe-lâ tesmeu illâ hemsâ, gloss:o gün, kimsenin yanından sapamayacağı çağırıcının ardından giderler; sesler Rahman için kısılır, bir fısıltıdan başkasını duymazsın, source:20:108}. Herkes tek bir öncünün ardından yürür. Dünyada önde yürüdüğünü sananların sonu da anlatılır. Musa Firavun'a ve ileri gelenlerine gönderilir. Onlar Firavun'un emrine uyarlar: {ar:فَٱتَّبَعُوٓا۟ أَمْرَ فِرْعَوْنَ ۖ وَمَآ أَمْرُ فِرْعَوْنَ بِرَشِيدٍۢ, tr:fettebe'û emra Fir'avn, ve mâ emru Fir'avne bi-reşîd, gloss:Firavun'un emrine uydular, oysa Firavun'un emri doğru değildi, source:11:97}. Firavun başka bir yerde halkına sahipliğini şöyle ilan eder: {ar:أَلَيْسَ لِى مُلْكُ مِصْرَ وَهَٰذِهِ ٱلْأَنْهَٰرُ تَجْرِى مِن تَحْتِىٓ, tr:e-leyse lî mülkü Mısra ve hâzihi'l-enhâru tecrî min tahtî, gloss:Mısır'ın mülkü benim değil mi, şu ırmaklar da altımdan akıp gitmiyor mu, source:43:51}. Toprağın ve akan suyun sahibi olduğunu söyleyen bu adamın din günündeki yeri şöyle anlatılır: {ar:يَقْدُمُ قَوْمَهُۥ يَوْمَ ٱلْقِيَٰمَةِ فَأَوْرَدَهُمُ ٱلنَّارَ ۖ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ, tr:yakdümü kavmehû yevme'l-kıyâmeti fe-evradehümü'n-nâr, ve bi'se'l-virdü'l-mevrûd, gloss:kıyamet günü kavminin önüne geçer ve onları ateşe, bir suya indirir gibi indirir; inilen o su yeri ne kötüdür, source:11:98}. Sürünün öncüsü gibi öndedir ve arkasındakileri bir suya götürür gibi götürür, ama götürdüğü yer ateştir. O gün yalnızca önde yürüyenin kim olduğu değil, nereye vardırdığı da ortaya çıkar.

## Din: vadesi gelen hesap

[¶15] Türkçede "din" yalnızca inanç ve ibadet düzeni anlamında kalmıştır. Bu ayetteki kelime ise öncelikle bir hesabın kapanmasını anlatır: {ar:يوم الدين أي يوم الحكم والحساب والجزاء, tr:yevmü'd-dîni ey yevmü'l-hukmi ve'l-hisâbi ve'l-cezâ, gloss:din günü, hüküm, hesap ve karşılık günüdür, source:"د ي ن,B002"}. Karşılığın niteliği de ayrıca söylenir: {ar:الدين الجزاء والمكافأة, tr:ed-dînü'l-cezâü ve'l-mükâfee, gloss:din, karşılık ve denk ödemedir, source:"د ي ن,B002"}. "Mükâfee", bir şeyi kendi ağırlığında karşılamak, dengini vermektir. Türkçedeki "din" kelimesi bu ödeme, denklik ve hesap anlamlarını artık taşımaz. Ayetin meali "hesap günü" derken bu yitik katmanı geri getirir.

[¶16] Aynı kökte borcun adı da vardır, ama o başka bir kelimedir. Ayetteki kelime esreyle okunan "dîn"dir. Borç ise üstünle okunan "deyn"dir. Kur'an onu böyle yazar: {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belli bir vadeye kadar borçlandığınızda onu yazın, source:2:282}. Borç alıp vermek {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn, ve dâyentü fülânen izâ âmeltühû deynen immâ ahzen ve immâ i'tâen, gloss:borç; biriyle ya alarak ya vererek borçlu alışveriş yapmak, source:"د ي ن,B003"} diye anlatılır. Borcun işleyişi şöyledir: Bir şey bugün alınır, karşılığı sonraya kalır. Arada bir vade vardır, kayıt tutulur, tanık bulunur. Vade dolunca hesap kapanır. "Dîn" ile "deyn" aynı kelime değildir, ama aynı kökün iki yüzüdür. Biri açılan hesabı, öteki onun kapanışını adlandırır.

[¶17] Kur'an, kelimeyi kullanmadan, bu iki yüzü bir yerde yan yana koyar. Borç hükümleri anlatılırken önce darda kalan borçluya süre tanınması söylenir: {ar:وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ, tr:ve in kâne zû usratin fe-nazıratün ilâ meysera, ve en tesaddakû hayrun leküm, gloss:borçlu darda ise eli genişleyinceye kadar beklemek gerekir; bağışlamanız ise sizin için daha hayırlıdır, source:2:280}. Hemen ardından vade ayetinden önce şu gelir: {ar:وَٱتَّقُوا۟ يَوْمًۭا تُرْجَعُونَ فِيهِ إِلَى ٱللَّهِ ۖ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ, tr:vettekû yevmen turce'ûne fîhi ila'llâh, sümme tuveffâ küllü nefsin mâ kesebet ve hüm lâ yuzlemûn, gloss:Allah'a döndürüleceğiniz günden sakının; sonra her kişiye kazandığı tam olarak ödenir ve onlara haksızlık edilmez, source:2:281}. Dünyadaki borcun iki hükmü arasında, her hesabın tam ödendiği gün durur. Din günü bu sıralamada bütün vadelerin dolduğu gün olarak görünür.

[¶18] O günün ödemesi, bu ayetin kelimesiyle de anlatılır. Kur'an iffetli kadınlara iftira atanlardan söz ederken onların uzuvlarının konuşacağı günü anlatır: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ, tr:yevme teşhedü aleyhim elsinetühüm ve eydîhim ve ercülühüm bimâ kânû ya'melûn, gloss:dillerinin, ellerinin ve ayaklarının yaptıklarına karşı onların aleyhine tanıklık edeceği gün, source:24:24}. Ardından şu söylenir: {ar:يَوْمَئِذٍۢ يُوَفِّيهِمُ ٱللَّهُ دِينَهُمُ ٱلْحَقَّ, tr:yevmeizin yuveffîhimu'llâhu dînehümü'l-hakk, gloss:o gün Allah onlara hak ettikleri karşılığı tastamam öder, source:24:25}. "Yuveffî" bir borcu eksiksiz ödemenin fiilidir, nesnesi de "dîn"dir. Burada tanıklık eden uzuvlar arasında el de vardır. Mülkün tanımında "elin sahip olduğu" diye geçen el, o gün sahibinin aleyhine konuşur. Hesap kaydı da tutulmuştur. Her topluluk diz çökmüş olarak kendi kitabına çağrılır: {ar:كُلُّ أُمَّةٍۢ تُدْعَىٰٓ إِلَىٰ كِتَٰبِهَا ٱلْيَوْمَ تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ, tr:küllü ümmetin tud'â ilâ kitâbihâ, el-yevme tüczevne mâ küntüm ta'melûn, gloss:her topluluk kendi kitabına çağrılır; bugün yapmakta olduğunuzun karşılığını görürsünüz, source:45:28}, {ar:هَٰذَا كِتَٰبُنَا يَنطِقُ عَلَيْكُم بِٱلْحَقِّ ۚ إِنَّا كُنَّا نَسْتَنسِخُ مَا كُنتُمْ تَعْمَلُونَ, tr:hâzâ kitâbunâ yentıku aleyküm bi'l-hakk, innâ künnâ nestensihu mâ küntüm ta'melûn, gloss:bu kitabımız size karşı gerçeği söyler; biz yapmakta olduğunuzu yazdırıyorduk, source:45:29}. Dünyada borç yazılır ki vade gelince unutulmasın. O günün hesabı da yazılmış bir kayıtla gelir. Ölçünün ve dengede duran terazinin sahnesi ise altıncı ayetin "müstakîm" kelimesinin kökü üzerinden kurulur.

[¶19] "Dîn" kelimesinin bir anlamı daha bu hesabın neyi kapsadığını gösterir. Araplar alışkanlığa da bu adı verirdi: {ar:العادة يقال لها دين, tr:el-âdetü yükâlü lehâ dîn, gloss:alışkanlığa din denir, source:"د ي ن,B005"}. Kelime, insanın öteden beri sürdürdüğü hal için de kullanılır: {ar:الحال والأمر الذي تعهده, tr:el-hâlü ve'l-emru'llezî ta'hedüh, gloss:alıştığın hal ve iş, source:"د ي ن,B005"}. Aynı kelimenin hem alışkanlığı hem karşılığı adlandırması bir köprüdür. Bu köprüyü kökün kendisi değil, Kur'an'ın cümlesi doldurur. Karşılık hemen her yerde "yapmakta olduğunuz" ile söylenir: Yukarıdaki "mâ küntüm ta'melûn" bir kez yapılanı değil, sürdürülen işi anlatır. Cehennemdekilere ne yüzden oraya girdikleri sorulduğunda verdikleri cevap da böyle bir alışkanlık dökümüdür: {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem nekü nut'imu'l-miskîn, gloss:yoksulu doyuranlardan değildik, source:74:44}, {ar:وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ, tr:ve künnâ nükezzibü bi-yevmi'd-dîn, gloss:din gününü yalanlayıp dururduk, source:74:46}. Hesap gününü yalanlamak, bu dökümde tek bir düşünce değil, sürdürülen bir alışkanlıktır. O alışkanlık da yoksulun hakkını vermemekle yan yana durur. Başka bir yerde aynı bağ bir soruyla kurulur: {ar:أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ, tr:e-raeyte'llezî yükezzibü bi'd-dîn, gloss:din'i yalanlayanı gördün mü, source:107:1}, {ar:فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ, tr:fe-zâlike'llezî yedu''u'l-yetîm, gloss:işte o, yetimi itip kakandır, source:107:2}. Hesabın kapanacağına inanmayan, kimseye borçlu olmadığını sanır. Bunu da en zayıfın hakkını iterek gösterir.

## İnsanın kendi dinine bırakılması

[¶20] Kökün başka bir kullanımı, dışarıdan bilinemeyen bir şeyi tartmayı anlatır. Bir mahkemede söz ispat edilemediğinde hâkim adamı kendine bırakabilirdi: {ar:دينت الرجل تديينا إذا وكلته إلى دينه, tr:deyyentü'r-racüle tedyînen izâ vekeltühû ilâ dînih, gloss:adamı kendi dinine, yani vicdanına bıraktım, source:"د ي ن,B007"}. Bunun anlamı da açıklanır: {ar:دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته, tr:deyyentü'r-racüle fi'l-kadâi ve fîmâ beynehû ve beyna'llâhi ey saddaktuh, gloss:yargıda ve onunla Allah arasındaki konuda sözünü doğru kabul ettim, source:"د ي ن,B007"}. Yemin eden birinin niyetine göre değerlendirilmesi de bu kelimeyle söylenir {source:"د ي ن,B007"}. Dünyadaki yargıç, bir noktadan sonra durur ve geri kalanı, adamla Allah arasında kalan alana bırakır. Din günü o alanın da açıldığı gündür. Kur'an yeminler konusunda tam bu sınırı çizer: {ar:لَّا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا كَسَبَتْ قُلُوبُكُمْ, tr:lâ yüâhizükümu'llâhu bi'l-lağvi fî eymâniküm ve lâkin yüâhizüküm bimâ kesebet kulûbüküm, gloss:Allah sizi yeminlerinizdeki boş sözden sorumlu tutmaz, ama kalplerinizin kazandığından sorumlu tutar, source:2:225}. Yargıcın durduğu yerde, kalbin kazandığı başlar. İbrahim'in "sağlam kalp" sözü de, kalbi bedenin dayanağı sayan kullanım da, bu ayetin iki kelimesini aynı noktada buluşturur: Sahip olunan gün, kalbin hesabının görüldüğü gündür.

## Sahip olunmak ve karşılık görmek aynı kelimede

[¶21] Ayetin ilk ve son kelimeleri, kökleri ayrı olduğu halde bir anlamda birbirine değer. "Dîn" kelimesinin bir kullanımı doğrudan sahip olmaktır: {ar:دانه دينا أي أذله واستعبده ودينته ملكته, tr:dânehû dînen ey ezellehû ve'sta'bedeh, ve deyyentühû melektüh, gloss:onu boyun eğdirip kul edindi; "deyyentühû" ona sahip oldum demektir, source:"د ي ن,B004"}. Köleye de bu kökten ad verilir: {ar:العبد مدين, tr:el-abdü medîn, gloss:kul "medîn"dir, source:"د ي ن,B004"}. Aynı "medîn" kelimesi Kur'an'da geçer ve iki şekilde açıklanır. Bir açıklamaya göre {ar:غير مدينين أي غير مجزيين, tr:gayra medînîne ey gayra meczîyyîn, gloss:medîn olmayanlar, yani karşılık görmeyecek olanlar, source:"د ي ن,B002"}. Diğerine göre {ar:غير مدينين غير مملوكين, tr:gayra medînîne gayra memlûkîn, gloss:medîn olmayanlar, yani sahip olunmayanlar, source:"د ي ن,B004"}. "Karşılık görmeyen" ile "kimseye ait olmayan" aynı kelimenin iki açıklamasıdır.

[¶22] Kur'an bu kelimeyi bir ölüm döşeğinde kullanır. Can boğaza dayanmıştır: {ar:فَلَوْلَآ إِذَا بَلَغَتِ ٱلْحُلْقُومَ, tr:fe-levlâ izâ belegati'l-hulkûm, gloss:can boğaza dayandığında, source:56:83}. Çevredekiler bakar durur, Allah ise ölene onlardan daha yakındır ama onlar görmezler {source:56:85}. Sonra şu meydan okuma gelir: {ar:فَلَوْلَآ إِن كُنتُمْ غَيْرَ مَدِينِينَ, tr:fe-levlâ in küntüm gayra medînîn, gloss:madem kimseye ait değilsiniz ve karşılık görmeyeceksiniz, source:56:86}, {ar:تَرْجِعُونَهَآ إِن كُنتُمْ صَٰدِقِينَ, tr:terci'ûnehâ in küntüm sâdıkîn, gloss:doğru söylüyorsanız onu geri çevirsenize, source:56:87}. Kelimenin iki açıklaması burada ayrılmaz. İnsan kendi canını geri çeviremediği anda hem birine ait olduğunu hem de bir hesaba doğru gittiğini görür. Bunu inkâr edenin sorusu da aynı kelimeyle kurulur. Cennette biri, dünyadaki bir arkadaşının ona şöyle dediğini hatırlar: {ar:أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَدِينُونَ, tr:e-izâ mitnâ ve künnâ türâben ve izâmen e-innâ le-medînûn, gloss:öldüğümüzde, toprak ve kemik olduğumuzda, gerçekten hesaba çekilip karşılık mı göreceğiz, source:37:53}.

[¶23] "Dîn" ile hükümdarın aynı olayda buluştuğu bir hikâye de vardır. Yusuf, Mısır'da kardeşlerine yük hazırlarken su kabını küçük kardeşinin yüküne koydurur {source:12:70}. Görevliler {ar:نَفْقِدُ صُوَاعَ ٱلْمَلِكِ, tr:nefkıdü suvâa'l-melik, gloss:hükümdarın ölçek kabını kaybettik, source:12:72} der. Kardeşlere hırsızın cezası sorulur, onlar da kendi geleneklerine göre cevap verirler: {ar:جَزَٰٓؤُهُۥ مَن وُجِدَ فِى رَحْلِهِۦ فَهُوَ جَزَٰٓؤُهُۥ, tr:cezâühû men vücide fî rahlihî fe-hüve cezâüh, gloss:cezası, o kimin yükünde bulunursa kendisinin cezaya karşılık alıkonmasıdır, source:12:75}. Kap kardeşin yükünden çıkar ve Kur'an şunu ekler: {ar:مَا كَانَ لِيَأْخُذَ أَخَاهُ فِى دِينِ ٱلْمَلِكِ إِلَّآ أَن يَشَآءَ ٱللَّهُ, tr:mâ kâne li-ye'huze ehâhü fî dîni'l-melik illâ en yeşâa'llâh, gloss:Allah dilemeseydi, hükümdarın dinine göre kardeşini alıkoyamazdı, source:12:76}. "Hükümdarın dini", hükümdarın ülkesinde geçerli olan yargı ve karşılık düzenidir. Buradan bakınca bu ayetin "din günü" sözü, tek bir sahibin yargı düzeninden başka hiçbir düzenin işlemediği günü anlatır. "Dîn" bu yüzden boyun eğmenin de adıdır: {ar:فالدين الطاعة, tr:fe'd-dînü't-tâ'a, gloss:din itaattir, source:"د ي ن,B001"}, {ar:الدين لله طاعته والتعبد له, tr:ed-dînü lillâhi tâ'atühû ve't-teabbüdü leh, gloss:Allah için din, O'na itaat ve kulluktur, source:"د ي ن,B001"}. Kur'an sahipliği ve dini tek bir ayette birleştirir: {ar:وَلَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَهُ ٱلدِّينُ وَاصِبًا, tr:ve lehû mâ fi's-semâvâti ve'l-ardı ve lehü'd-dînü vâsıbâ, gloss:göklerde ve yerde ne varsa O'nundur, din de daima O'nundur, source:16:52}. Din günü, her zaman var olan bu düzenin artık kimse tarafından görmezden gelinemediği gündür. Sahibin ve sahip olunanın sahnesi beşinci ayetin "na'büdü" kelimesiyle kurulur. Bu ayetteki "dîn", o sahnede sahip olunanın kendi sesiyle konuşmaya başlamasından hemen önce gelir.

## Günün sahibi Rahman'dır

[¶24] Dördüncü ayet doğrudan üçüncü ayetin {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:Rahman ve Rahim, source:1:3} sözünden sonra gelir. Bu sıra rastgele değildir, çünkü Kur'an o günün sahibini birçok yerde Rahman adıyla anar: {ar:ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ ۚ وَكَانَ يَوْمًا عَلَى ٱلْكَٰفِرِينَ عَسِيرًۭا, tr:el-mülkü yevmeizini'l-hakku li'r-rahmân, ve kâne yevmen ale'l-kâfirîne asîrâ, gloss:o gün gerçek mülk Rahman'ındır; o gün inkârcılar için zor bir gündür, source:25:26}. Başka bir sahnede o günün sessizliği anlatılır: {ar:رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا, tr:rabbi's-semâvâti ve'l-ardı ve mâ beynehüme'r-rahmân, lâ yemlikûne minhü hitâbâ, gloss:göklerin, yerin ve aralarındakilerin Rabbi, Rahman; O'nun huzurunda konuşmaya sahip olamazlar, source:78:37}, {ar:يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا ۖ لَّا يَتَكَلَّمُونَ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَقَالَ صَوَابًۭا, tr:yevme yekûmü'r-rûhu ve'l-melâiketü saffâ, lâ yetekellemûne illâ men ezine lehü'r-rahmânü ve kâle savâbâ, gloss:ruhun ve meleklerin saf saf durduğu gün, Rahman'ın izin verdiği ve doğruyu söyleyen dışında kimse konuşmaz, source:78:38}. Bu iki ayette Fâtiha'nın ikinci, üçüncü ve dördüncü ayetleri bir arada duyulur: Rab, Rahman, sahip olmak fiili ve gün. Sahip olunamayan şeyler arasında söz de vardır. Elin tuttuğu mal düştükten sonra dilin tuttuğu söz de düşer. Konuşma hakkı da Rahman'ın izniyle verilir. Şefaat için de aynı şey söylenir: {ar:يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ, tr:yevmeizin lâ tenfau'ş-şefâatü illâ men ezine lehü'r-rahmân, gloss:o gün şefaat, Rahman'ın izin verdiği kimseden başkasına fayda vermez, source:20:109}.

[¶25] Sahiplik, rahmet ve gün sırasını Kur'an bir ayette Fâtiha'daki düzeniyle kurar. Peygambere bir soru sorması ve cevabını kendisinin vermesi söylenir: {ar:قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ, tr:kul li-men mâ fi's-semâvâti ve'l-ard, kul lillâh, ketebe alâ nefsihi'r-rahmete, le-yecme'annekküm ilâ yevmi'l-kıyâmeti lâ raybe fîh, gloss:de ki: göklerde ve yerde olanlar kimindir? De ki: Allah'ındır. O, rahmeti kendi üzerine yazmıştır; sizi kuşkusuz kıyamet gününde toplayacaktır, source:6:12}. Önce mülk gelir, sonra rahmet, sonra gün. Rahmet için kullanılan fiil "yazmak"tır. Borcun vadesine kadar yazılması gibi, rahmet de bir yükümlülük olarak yazılmıştır. Ama bu yükümlülüğü sahip kendi üzerine almıştır.

[¶26] "Yevm" kelimesinin bir kullanımı bu iki yüzü bir arada taşır. Araplar Allah'a izafe edilen günleri, o günlerde olanlarla anarlardı: {ar:وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين, tr:ve zekkirhüm bi-eyyâmi'llâh: bimâ nezele bi-Âdin ve Semûde ve gayrihim mine'l-azâbi ve bi'l-afvi an âharîn, gloss:"onlara Allah'ın günlerini hatırlat", yani Âd'a, Semûd'a ve başkalarına inen azabı ve başkalarının bağışlanmasını, source:"ي و م,B004"}. Kelime yalnızca nimet anlamında da kullanılır: {ar:أيامه: نعمه, tr:eyyâmühû: niamuh, gloss:O'nun günleri, O'nun nimetleridir, source:"ي و م,B004"}. Kur'an bu sözü Musa'ya verilen bir görevde kullanır: Musa halkını karanlıklardan aydınlığa çıkarmak için gönderilir ve ona şöyle denir: {ar:وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ, tr:ve zekkirhüm bi-eyyâmillâh, gloss:onlara Allah'ın günlerini hatırlat, source:14:5}. Allah'ın günleri, azabın da bağışlamanın da indiği günlerdir. Din günü bu günlerin sonuncusu ve en büyüğüdür. Nimetin ve gazabın iki topluluğun üstüne indiği sahne yedinci ayetin {ar:أَنْعَمْتَ, tr:en'amte, gloss:nimet verdin, source:1:7} ve {ar:ٱلْمَغْضُوبِ, tr:el-magdûb, gloss:gazaba uğramış, source:1:7} kelimeleriyle kurulur. Bu ayetin "yevm" kelimesi o iki inişe bir gün verir.

[¶27] İbrahim'in din gününe bakışı da bu yüzden korku değil umutla söylenir: Bağışlanmayı umduğu gün din günüdür {source:26:82}. Borç ayetlerinin başında alacaklıya yöneltilen öğüt bu umuda bir ölçü verir. Darda kalan borçluya süre tanınır, sonra da {ar:وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ, tr:ve en tesaddakû hayrun leküm, gloss:borcu bağışlamanız sizin için daha hayırlıdır, source:2:280} denir. Hesabın tastamam ödendiği günün sahibi, alacağını bağışlayabilen bir alacaklıdır. Fâtiha bu sahibi Rahman ve Rahim diye andıktan hemen sonra onu din gününün sahibi diye anar.

===== _commentary/v16/out/1_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: some canonical readings read the word as "melik" (without long â)
- memory: the vocalization "milk" for the road's middle; the sources give several vocalizations
- memory: "el-mülk" vocalization in الملك لله المالك المليك
- memory: "awrada" means leading herds down to water, and "wird" is the watering place (11:98)
- memory: "kâna + imperfect" (kuntum ta'malûn) expresses continuous or habitual past action
- memory: "dîn" is read with kasra and "deyn" with fatha; the Quran text confirms only the fatha of deyn
- not written: malak/angel (B009) - the source derives it from alûk, so it is an echo, not this word's family
- not written: madîna/city (B006) - its place in this root is itself disputed, and it adds nothing to the day
- not written: "miyâhunâ mulûkunâ" - its vocalization and exact sense are uncertain
- not written: "yâ dîna qalbika" (B004/B005) - the source marks it as disputed
- not written: sha'n in 80:37 and the gloss العادة والشأن - a shared word only, not the same root or sense
- not written: "yumlil" in 2:282 - root m-l-l, not m-l-k
- not written: making someone king (B003 ملك القوم فلانا) - no work in this ayah's themes
- not written: the stray phrase "Üç yüz kırk dokuzuncu değil" in section one is an editing slip and should be deleted

===== passages not cited (319) =====
## strong (this ayah's own list) (39)

- (2:281) [listed for 1:4] [cited in ¶17] وَٱتَّقُوا۟ يَوْمًۭا تُرْجَعُونَ فِيهِ إِلَى ٱللَّهِ ۖ ثُمَّ تُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (3:25) [listed for 1:4] فَكَيْفَ إِذَا جَمَعْنَٰهُمْ لِيَوْمٍۢ لَّا رَيْبَ فِيهِ وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (3:26) [listed for 1:4] [cited in ¶2, ¶3] قُلِ ٱللَّهُمَّ مَٰلِكَ ٱلْمُلْكِ تُؤْتِى ٱلْمُلْكَ مَن تَشَآءُ وَتَنزِعُ ٱلْمُلْكَ مِمَّن تَشَآءُ وَتُعِزُّ مَن تَشَآءُ وَتُذِلُّ مَن تَشَآءُ ۖ بِيَدِكَ ٱلْخَيْرُ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (5:40) [listed for 1:4] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ يُعَذِّبُ مَن يَشَآءُ وَيَغْفِرُ لِمَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (6:73) [listed for 1:4] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (14:41) [listed for 1:4] رَبَّنَا ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ ٱلْحِسَابُ
- (17:13) [listed for 1:4] وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا
- (17:14) [listed for 1:4] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
- (18:49) [listed for 1:4] وَوُضِعَ ٱلْكِتَٰبُ فَتَرَى ٱلْمُجْرِمِينَ مُشْفِقِينَ مِمَّا فِيهِ وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا ۗ وَلَا يَظْلِمُ رَبُّكَ أَحَدًۭا
- (21:47) [listed for 1:4] وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ فَلَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا ۖ وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا ۗ وَكَفَىٰ بِنَا حَٰسِبِينَ
- (24:25) [listed for 1:4] [cited in ¶18] يَوْمَئِذٍۢ يُوَفِّيهِمُ ٱللَّهُ دِينَهُمُ ٱلْحَقَّ وَيَعْلَمُونَ أَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ ٱلْمُبِينُ
- (26:82) [listed for 1:4] [cited in ¶9, ¶27] وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى يَوْمَ ٱلدِّينِ
- (36:51) [listed for 1:4] وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ
- (36:54) [listed for 1:4] فَٱلْيَوْمَ لَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا وَلَا تُجْزَوْنَ إِلَّا مَا كُنتُمْ تَعْمَلُونَ
- (37:21) [listed for 1:4] هَٰذَا يَوْمُ ٱلْفَصْلِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (39:68) [listed for 1:4] وَنُفِخَ فِى ٱلصُّورِ فَصَعِقَ مَن فِى ٱلسَّمَٰوَٰتِ وَمَن فِى ٱلْأَرْضِ إِلَّا مَن شَآءَ ٱللَّهُ ۖ ثُمَّ نُفِخَ فِيهِ أُخْرَىٰ فَإِذَا هُمْ قِيَامٌۭ يَنظُرُونَ
- (39:69) [listed for 1:4] وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ وَقُضِىَ بَيْنَهُم بِٱلْحَقِّ وَهُمْ لَا يُظْلَمُونَ
- (39:70) [listed for 1:4] وَوُفِّيَتْ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُوَ أَعْلَمُ بِمَا يَفْعَلُونَ
- (40:16) [listed for 1:4] [cited in ¶3] يَوْمَ هُم بَٰرِزُونَ ۖ لَا يَخْفَىٰ عَلَى ٱللَّهِ مِنْهُمْ شَىْءٌۭ ۚ لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
- (40:17) [listed for 1:4] ٱلْيَوْمَ تُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ ۚ لَا ظُلْمَ ٱلْيَوْمَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (44:40) [listed for 1:4] إِنَّ يَوْمَ ٱلْفَصْلِ مِيقَٰتُهُمْ أَجْمَعِينَ
- (45:22) [listed for 1:4] وَخَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَلِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (45:26) [listed for 1:4] قُلِ ٱللَّهُ يُحْيِيكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يَجْمَعُكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (45:28) [listed for 1:4] [cited in ¶18] وَتَرَىٰ كُلَّ أُمَّةٍۢ جَاثِيَةًۭ ۚ كُلُّ أُمَّةٍۢ تُدْعَىٰٓ إِلَىٰ كِتَٰبِهَا ٱلْيَوْمَ تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
- (45:29) [listed for 1:4] [cited in ¶18] هَٰذَا كِتَٰبُنَا يَنطِقُ عَلَيْكُم بِٱلْحَقِّ ۚ إِنَّا كُنَّا نَسْتَنسِخُ مَا كُنتُمْ تَعْمَلُونَ
- (50:20) [listed for 1:4] وَنُفِخَ فِى ٱلصُّورِ ۚ ذَٰلِكَ يَوْمُ ٱلْوَعِيدِ
- (50:21) [listed for 1:4] وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ
- (51:6) [listed for 1:4] [cited in ¶6] وَإِنَّ ٱلدِّينَ لَوَٰقِعٌۭ
- (51:12) [listed for 1:4] يَسْـَٔلُونَ أَيَّانَ يَوْمُ ٱلدِّينِ
- (56:56) [listed for 1:4] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
- (77:13) [listed for 1:4] لِيَوْمِ ٱلْفَصْلِ
- (82:15) [listed for 1:4] يَصْلَوْنَهَا يَوْمَ ٱلدِّينِ
- (82:19) [listed for 1:4] [cited in ¶3] يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا ۖ وَٱلْأَمْرُ يَوْمَئِذٍۢ لِّلَّهِ
- (83:4) [listed for 1:4] أَلَا يَظُنُّ أُو۟لَٰٓئِكَ أَنَّهُم مَّبْعُوثُونَ
- (83:5) [listed for 1:4] لِيَوْمٍ عَظِيمٍۢ
- (83:6) [listed for 1:4] يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ
- (99:7) [listed for 1:4] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- (99:8) [listed for 1:4] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
- (114:2) [listed for 1:4] [cited in ¶2] مَلِكِ ٱلنَّاسِ

## medium (this ayah's own list) (93)

- (3:19) [listed for 1:4] إِنَّ ٱلدِّينَ عِندَ ٱللَّهِ ٱلْإِسْلَٰمُ ۗ وَمَا ٱخْتَلَفَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْعِلْمُ بَغْيًۢا بَيْنَهُمْ ۗ وَمَن يَكْفُرْ بِـَٔايَٰتِ ٱللَّهِ فَإِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (3:30) [listed for 1:4] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
- (3:185) [listed for 1:4] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (4:87) [listed for 1:4] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۗ وَمَنْ أَصْدَقُ مِنَ ٱللَّهِ حَدِيثًۭا
- (5:3) [listed for 1:4] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (6:12) [listed for 1:4] [cited in ¶25] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
- (6:31) [listed for 1:4] قَدْ خَسِرَ ٱلَّذِينَ كَذَّبُوا۟ بِلِقَآءِ ٱللَّهِ ۖ حَتَّىٰٓ إِذَا جَآءَتْهُمُ ٱلسَّاعَةُ بَغْتَةًۭ قَالُوا۟ يَٰحَسْرَتَنَا عَلَىٰ مَا فَرَّطْنَا فِيهَا وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ ۚ أَلَا سَآءَ مَا يَزِرُونَ
- (6:70) [listed for 1:4] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (6:158) [listed for 1:4] هَلْ يَنظُرُونَ إِلَّآ أَن تَأْتِيَهُمُ ٱلْمَلَٰٓئِكَةُ أَوْ يَأْتِىَ رَبُّكَ أَوْ يَأْتِىَ بَعْضُ ءَايَٰتِ رَبِّكَ ۗ يَوْمَ يَأْتِى بَعْضُ ءَايَٰتِ رَبِّكَ لَا يَنفَعُ نَفْسًا إِيمَٰنُهَا لَمْ تَكُنْ ءَامَنَتْ مِن قَبْلُ أَوْ كَسَبَتْ فِىٓ إِيمَٰنِهَا خَيْرًۭا ۗ قُلِ ٱنتَظِرُوٓا۟ إِنَّا مُنتَظِرُونَ
- (7:8) [listed for 1:4] وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (7:9) [listed for 1:4] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَظْلِمُونَ
- (7:51) [listed for 1:4] [cited in ¶10] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (7:158) [listed for 1:4] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ جَمِيعًا ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِ ٱلنَّبِىِّ ٱلْأُمِّىِّ ٱلَّذِى يُؤْمِنُ بِٱللَّهِ وَكَلِمَٰتِهِۦ وَٱتَّبِعُوهُ لَعَلَّكُمْ تَهْتَدُونَ
- (10:22) [listed for 1:4] هُوَ ٱلَّذِى يُسَيِّرُكُمْ فِى ٱلْبَرِّ وَٱلْبَحْرِ ۖ حَتَّىٰٓ إِذَا كُنتُمْ فِى ٱلْفُلْكِ وَجَرَيْنَ بِهِم بِرِيحٍۢ طَيِّبَةٍۢ وَفَرِحُوا۟ بِهَا جَآءَتْهَا رِيحٌ عَاصِفٌۭ وَجَآءَهُمُ ٱلْمَوْجُ مِن كُلِّ مَكَانٍۢ وَظَنُّوٓا۟ أَنَّهُمْ أُحِيطَ بِهِمْ ۙ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ لَئِنْ أَنجَيْتَنَا مِنْ هَٰذِهِۦ لَنَكُونَنَّ مِنَ ٱلشَّٰكِرِينَ
- (10:105) [listed for 1:4] وَأَنْ أَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا وَلَا تَكُونَنَّ مِنَ ٱلْمُشْرِكِينَ
- (11:103) [listed for 1:4] إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّمَنْ خَافَ عَذَابَ ٱلْءَاخِرَةِ ۚ ذَٰلِكَ يَوْمٌۭ مَّجْمُوعٌۭ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌۭ مَّشْهُودٌۭ
- (11:105) [listed for 1:4] يَوْمَ يَأْتِ لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِۦ ۚ فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ
- (12:40) [listed for 1:4] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (14:48) [listed for 1:4] يَوْمَ تُبَدَّلُ ٱلْأَرْضُ غَيْرَ ٱلْأَرْضِ وَٱلسَّمَٰوَٰتُ ۖ وَبَرَزُوا۟ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ
- (15:35) [listed for 1:4] وَإِنَّ عَلَيْكَ ٱللَّعْنَةَ إِلَىٰ يَوْمِ ٱلدِّينِ
- (16:52) [listed for 1:4] [cited in ¶23] وَلَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَهُ ٱلدِّينُ وَاصِبًا ۚ أَفَغَيْرَ ٱللَّهِ تَتَّقُونَ
- (18:47) [listed for 1:4] وَيَوْمَ نُسَيِّرُ ٱلْجِبَالَ وَتَرَى ٱلْأَرْضَ بَارِزَةًۭ وَحَشَرْنَٰهُمْ فَلَمْ نُغَادِرْ مِنْهُمْ أَحَدًۭا
- (20:111) [listed for 1:4] ۞ وَعَنَتِ ٱلْوُجُوهُ لِلْحَىِّ ٱلْقَيُّومِ ۖ وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا
- (20:112) [listed for 1:4] وَمَن يَعْمَلْ مِنَ ٱلصَّٰلِحَٰتِ وَهُوَ مُؤْمِنٌۭ فَلَا يَخَافُ ظُلْمًۭا وَلَا هَضْمًۭا
- (23:101) [listed for 1:4] فَإِذَا نُفِخَ فِى ٱلصُّورِ فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ
- (23:102) [listed for 1:4] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (23:103) [listed for 1:4] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (24:2) [listed for 1:4] ٱلزَّانِيَةُ وَٱلزَّانِى فَٱجْلِدُوا۟ كُلَّ وَٰحِدٍۢ مِّنْهُمَا مِا۟ئَةَ جَلْدَةٍۢ ۖ وَلَا تَأْخُذْكُم بِهِمَا رَأْفَةٌۭ فِى دِينِ ٱللَّهِ إِن كُنتُمْ تُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ وَلْيَشْهَدْ عَذَابَهُمَا طَآئِفَةٌۭ مِّنَ ٱلْمُؤْمِنِينَ
- (24:42) [listed for 1:4] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (25:2) [listed for 1:4] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
- (30:12) [listed for 1:4] وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يُبْلِسُ ٱلْمُجْرِمُونَ
- (30:43) [listed for 1:4] فَأَقِمْ وَجْهَكَ لِلدِّينِ ٱلْقَيِّمِ مِن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا مَرَدَّ لَهُۥ مِنَ ٱللَّهِ ۖ يَوْمَئِذٍۢ يَصَّدَّعُونَ
- (37:20) [listed for 1:4] وَقَالُوا۟ يَٰوَيْلَنَا هَٰذَا يَوْمُ ٱلدِّينِ
- (37:24) [listed for 1:4] وَقِفُوهُمْ ۖ إِنَّهُم مَّسْـُٔولُونَ
- (37:53) [listed for 1:4] [cited in ¶22] أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَدِينُونَ
- (39:2) [listed for 1:4] إِنَّآ أَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (39:11) [listed for 1:4] قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (39:14) [listed for 1:4] قُلِ ٱللَّهَ أَعْبُدُ مُخْلِصًۭا لَّهُۥ دِينِى
- (40:14) [listed for 1:4] فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (42:45) [listed for 1:4] وَتَرَىٰهُمْ يُعْرَضُونَ عَلَيْهَا خَٰشِعِينَ مِنَ ٱلذُّلِّ يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ ۗ وَقَالَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَآ إِنَّ ٱلظَّٰلِمِينَ فِى عَذَابٍۢ مُّقِيمٍۢ
- (45:27) [listed for 1:4] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَيَوْمَ تَقُومُ ٱلسَّاعَةُ يَوْمَئِذٍۢ يَخْسَرُ ٱلْمُبْطِلُونَ
- (50:22) [listed for 1:4] لَّقَدْ كُنتَ فِى غَفْلَةٍۢ مِّنْ هَٰذَا فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ
- (51:60) [listed for 1:4] فَوَيْلٌۭ لِّلَّذِينَ كَفَرُوا۟ مِن يَوْمِهِمُ ٱلَّذِى يُوعَدُونَ
- (52:13) [listed for 1:4] يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا
- (53:31) [listed for 1:4] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
- (56:50) [listed for 1:4] لَمَجْمُوعُونَ إِلَىٰ مِيقَٰتِ يَوْمٍۢ مَّعْلُومٍۢ
- (57:5) [listed for 1:4] لَّهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَإِلَى ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ
- (57:13) [listed for 1:4] يَوْمَ يَقُولُ ٱلْمُنَٰفِقُونَ وَٱلْمُنَٰفِقَٰتُ لِلَّذِينَ ءَامَنُوا۟ ٱنظُرُونَا نَقْتَبِسْ مِن نُّورِكُمْ قِيلَ ٱرْجِعُوا۟ وَرَآءَكُمْ فَٱلْتَمِسُوا۟ نُورًۭا فَضُرِبَ بَيْنَهُم بِسُورٍۢ لَّهُۥ بَابٌۢ بَاطِنُهُۥ فِيهِ ٱلرَّحْمَةُ وَظَٰهِرُهُۥ مِن قِبَلِهِ ٱلْعَذَابُ
- (57:15) [listed for 1:4] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (62:1) [listed for 1:4] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ٱلْمَلِكِ ٱلْقُدُّوسِ ٱلْعَزِيزِ ٱلْحَكِيمِ
- (64:9) [listed for 1:4] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (69:13) [listed for 1:4] فَإِذَا نُفِخَ فِى ٱلصُّورِ نَفْخَةٌۭ وَٰحِدَةٌۭ
- (69:18) [listed for 1:4] يَوْمَئِذٍۢ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌۭ
- (69:19) [listed for 1:4] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ فَيَقُولُ هَآؤُمُ ٱقْرَءُوا۟ كِتَٰبِيَهْ
- (69:25) [listed for 1:4] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ فَيَقُولُ يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ
- (70:26) [listed for 1:4] [cited in ¶5] وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ
- (72:21) [listed for 1:4] قُلْ إِنِّى لَآ أَمْلِكُ لَكُمْ ضَرًّۭا وَلَا رَشَدًۭا
- (74:46) [listed for 1:4] [cited in ¶19] وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ
- (75:6) [listed for 1:4] يَسْـَٔلُ أَيَّانَ يَوْمُ ٱلْقِيَٰمَةِ
- (75:10) [listed for 1:4] يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ
- (75:12) [listed for 1:4] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ
- (75:13) [listed for 1:4] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
- (75:30) [listed for 1:4] إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ
- (76:10) [listed for 1:4] إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا
- (77:14) [listed for 1:4] وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلْفَصْلِ
- (78:17) [listed for 1:4] إِنَّ يَوْمَ ٱلْفَصْلِ كَانَ مِيقَٰتًۭا
- (78:21) [listed for 1:4] إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا
- (79:6) [listed for 1:4] يَوْمَ تَرْجُفُ ٱلرَّاجِفَةُ
- (79:34) [listed for 1:4] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (79:35) [listed for 1:4] يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- (79:40) [listed for 1:4] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
- (80:33) [listed for 1:4] فَإِذَا جَآءَتِ ٱلصَّآخَّةُ
- (80:34) [listed for 1:4] [cited in ¶11] يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ
- (80:37) [listed for 1:4] [cited in ¶11] لِكُلِّ ٱمْرِئٍۢ مِّنْهُمْ يَوْمَئِذٍۢ شَأْنٌۭ يُغْنِيهِ
- (81:14) [listed for 1:4] عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ
- (82:1) [listed for 1:4] إِذَا ٱلسَّمَآءُ ٱنفَطَرَتْ
- (82:5) [listed for 1:4] عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ
- (82:9) [listed for 1:4] كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ
- (82:17) [listed for 1:4] [cited in ¶3] وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ
- (83:11) [listed for 1:4] ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ
- (84:7) [listed for 1:4] فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ
- (84:8) [listed for 1:4] فَسَوْفَ يُحَاسَبُ حِسَابًۭا يَسِيرًۭا
- (84:10) [listed for 1:4] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
- (86:9) [listed for 1:4] يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
- (89:23) [listed for 1:4] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (98:5) [listed for 1:4] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- (99:6) [listed for 1:4] يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- (101:6) [listed for 1:4] فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- (101:8) [listed for 1:4] وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- (102:8) [listed for 1:4] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ
- (106:3) [listed for 1:4] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- (109:2) [listed for 1:4] لَآ أَعْبُدُ مَا تَعْبُدُونَ
- (109:6) [listed for 1:4] لَكُمْ دِينُكُمْ وَلِىَ دِينِ

## named by the passage's own list as strong for this ayah (11)

- (7:29) [listed for 1:4] قُلْ أَمَرَ رَبِّى بِٱلْقِسْطِ ۖ وَأَقِيمُوا۟ وُجُوهَكُمْ عِندَ كُلِّ مَسْجِدٍۢ وَٱدْعُوهُ مُخْلِصِينَ لَهُ ٱلدِّينَ ۚ كَمَا بَدَأَكُمْ تَعُودُونَ
- (9:29) [listed for 1:4] قَٰتِلُوا۟ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱللَّهِ وَلَا بِٱلْيَوْمِ ٱلْءَاخِرِ وَلَا يُحَرِّمُونَ مَا حَرَّمَ ٱللَّهُ وَرَسُولُهُۥ وَلَا يَدِينُونَ دِينَ ٱلْحَقِّ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ حَتَّىٰ يُعْطُوا۟ ٱلْجِزْيَةَ عَن يَدٍۢ وَهُمْ صَٰغِرُونَ
- (15:38) [listed for 1:4] إِلَىٰ يَوْمِ ٱلْوَقْتِ ٱلْمَعْلُومِ
- (25:26) [listed for 1:4] [cited in ¶24] ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ ۚ وَكَانَ يَوْمًا عَلَى ٱلْكَٰفِرِينَ عَسِيرًۭا
- (28:70) [listed for 1:4] وَهُوَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ ۖ وَلَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
- (56:86) [listed for 1:4] [cited in ¶22] فَلَوْلَآ إِن كُنتُمْ غَيْرَ مَدِينِينَ
- (77:12) [listed for 1:4] لِأَىِّ يَوْمٍ أُجِّلَتْ
- (78:26) [listed for 1:4] جَزَآءًۭ وِفَاقًا
- (95:7) [listed for 1:4] فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ
- (95:8) [listed for 1:4] أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ
- (101:4) [listed for 1:4] يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ

## named by the passage's own list as medium for this ayah (28)

- (2:132) [listed for 1:4] وَوَصَّىٰ بِهَآ إِبْرَٰهِۦمُ بَنِيهِ وَيَعْقُوبُ يَٰبَنِىَّ إِنَّ ٱللَّهَ ٱصْطَفَىٰ لَكُمُ ٱلدِّينَ فَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسْلِمُونَ
- (4:53) [listed for 1:4] أَمْ لَهُمْ نَصِيبٌۭ مِّنَ ٱلْمُلْكِ فَإِذًۭا لَّا يُؤْتُونَ ٱلنَّاسَ نَقِيرًا
- (10:104) [listed for 1:4] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى شَكٍّۢ مِّن دِينِى فَلَآ أَعْبُدُ ٱلَّذِينَ تَعْبُدُونَ مِن دُونِ ٱللَّهِ وَلَٰكِنْ أَعْبُدُ ٱللَّهَ ٱلَّذِى يَتَوَفَّىٰكُمْ ۖ وَأُمِرْتُ أَنْ أَكُونَ مِنَ ٱلْمُؤْمِنِينَ
- (15:87) [listed for 1:4] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (18:105) [listed for 1:4] أُو۟لَٰٓئِكَ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ وَلِقَآئِهِۦ فَحَبِطَتْ أَعْمَٰلُهُمْ فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا
- (19:33) [listed for 1:4] وَٱلسَّلَٰمُ عَلَىَّ يَوْمَ وُلِدتُّ وَيَوْمَ أَمُوتُ وَيَوْمَ أُبْعَثُ حَيًّۭا
- (34:30) [listed for 1:4] قُل لَّكُم مِّيعَادُ يَوْمٍۢ لَّا تَسْتَـْٔخِرُونَ عَنْهُ سَاعَةًۭ وَلَا تَسْتَقْدِمُونَ
- (38:78) [listed for 1:4] وَإِنَّ عَلَيْكَ لَعْنَتِىٓ إِلَىٰ يَوْمِ ٱلدِّينِ
- (38:81) [listed for 1:4] إِلَىٰ يَوْمِ ٱلْوَقْتِ ٱلْمَعْلُومِ
- (39:3) [listed for 1:4] أَلَا لِلَّهِ ٱلدِّينُ ٱلْخَالِصُ ۚ وَٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَآ إِلَى ٱللَّهِ زُلْفَىٰٓ إِنَّ ٱللَّهَ يَحْكُمُ بَيْنَهُمْ فِى مَا هُمْ فِيهِ يَخْتَلِفُونَ ۗ إِنَّ ٱللَّهَ لَا يَهْدِى مَنْ هُوَ كَٰذِبٌۭ كَفَّارٌۭ
- (42:21) [listed for 1:4] أَمْ لَهُمْ شُرَكَٰٓؤُا۟ شَرَعُوا۟ لَهُم مِّنَ ٱلدِّينِ مَا لَمْ يَأْذَنۢ بِهِ ٱللَّهُ ۚ وَلَوْلَا كَلِمَةُ ٱلْفَصْلِ لَقُضِىَ بَيْنَهُمْ ۗ وَإِنَّ ٱلظَّٰلِمِينَ لَهُمْ عَذَابٌ أَلِيمٌۭ
- (44:9) [listed for 1:4] بَلْ هُمْ فِى شَكٍّۢ يَلْعَبُونَ
- (44:16) [listed for 1:4] يَوْمَ نَبْطِشُ ٱلْبَطْشَةَ ٱلْكُبْرَىٰٓ إِنَّا مُنتَقِمُونَ
- (48:28) [listed for 1:4] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ ۚ وَكَفَىٰ بِٱللَّهِ شَهِيدًۭا
- (49:16) [listed for 1:4] قُلْ أَتُعَلِّمُونَ ٱللَّهَ بِدِينِكُمْ وَٱللَّهُ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (50:41) [listed for 1:4] وَٱسْتَمِعْ يَوْمَ يُنَادِ ٱلْمُنَادِ مِن مَّكَانٍۢ قَرِيبٍۢ
- (50:42) [listed for 1:4] يَوْمَ يَسْمَعُونَ ٱلصَّيْحَةَ بِٱلْحَقِّ ۚ ذَٰلِكَ يَوْمُ ٱلْخُرُوجِ
- (51:13) [listed for 1:4] يَوْمَ هُمْ عَلَى ٱلنَّارِ يُفْتَنُونَ
- (53:30) [listed for 1:4] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (60:3) [listed for 1:4] لَن تَنفَعَكُمْ أَرْحَامُكُمْ وَلَآ أَوْلَٰدُكُمْ ۚ يَوْمَ ٱلْقِيَٰمَةِ يَفْصِلُ بَيْنَكُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (74:9) [listed for 1:4] فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ
- (77:35) [listed for 1:4] هَٰذَا يَوْمُ لَا يَنطِقُونَ
- (78:18) [listed for 1:4] يَوْمَ يُنفَخُ فِى ٱلصُّورِ فَتَأْتُونَ أَفْوَاجًۭا
- (82:18) [listed for 1:4] [cited in ¶3] ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ
- (83:22) [listed for 1:4] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (107:1) [listed for 1:4] [cited in ¶19] أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- (109:3) [listed for 1:4] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- (114:3) [listed for 1:4] [cited in ¶2] إِلَٰهِ ٱلنَّاسِ

## weak (this ayah's own list) (17)

- (2:107) [listed for 1:4] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
- (2:193) [listed for 1:4] وَقَٰتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌۭ وَيَكُونَ ٱلدِّينُ لِلَّهِ ۖ فَإِنِ ٱنتَهَوْا۟ فَلَا عُدْوَٰنَ إِلَّا عَلَى ٱلظَّٰلِمِينَ
- (2:217) [listed for 1:4] يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ ۖ وَصَدٌّ عَن سَبِيلِ ٱللَّهِ وَكُفْرٌۢ بِهِۦ وَٱلْمَسْجِدِ ٱلْحَرَامِ وَإِخْرَاجُ أَهْلِهِۦ مِنْهُ أَكْبَرُ عِندَ ٱللَّهِ ۚ وَٱلْفِتْنَةُ أَكْبَرُ مِنَ ٱلْقَتْلِ ۗ وَلَا يَزَالُونَ يُقَٰتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ ٱسْتَطَٰعُوا۟ ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِۦ فَيَمُتْ وَهُوَ كَافِرٌۭ فَأُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:256) [listed for 1:4] لَآ إِكْرَاهَ فِى ٱلدِّينِ ۖ قَد تَّبَيَّنَ ٱلرُّشْدُ مِنَ ٱلْغَىِّ ۚ فَمَن يَكْفُرْ بِٱلطَّٰغُوتِ وَيُؤْمِنۢ بِٱللَّهِ فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ لَا ٱنفِصَامَ لَهَا ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
- (3:189) [listed for 1:4] وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (4:136) [listed for 1:4] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ ءَامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِى نَزَّلَ عَلَىٰ رَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِىٓ أَنزَلَ مِن قَبْلُ ۚ وَمَن يَكْفُرْ بِٱللَّهِ وَمَلَٰٓئِكَتِهِۦ وَكُتُبِهِۦ وَرُسُلِهِۦ وَٱلْيَوْمِ ٱلْءَاخِرِ فَقَدْ ضَلَّ ضَلَٰلًۢا بَعِيدًا
- (5:120) [listed for 1:4] لِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا فِيهِنَّ ۚ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۢ
- (6:75) [listed for 1:4] وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ
- (6:159) [listed for 1:4] إِنَّ ٱلَّذِينَ فَرَّقُوا۟ دِينَهُمْ وَكَانُوا۟ شِيَعًۭا لَّسْتَ مِنْهُمْ فِى شَىْءٍ ۚ إِنَّمَآ أَمْرُهُمْ إِلَى ٱللَّهِ ثُمَّ يُنَبِّئُهُم بِمَا كَانُوا۟ يَفْعَلُونَ
- (7:14) [listed for 1:4] قَالَ أَنظِرْنِىٓ إِلَىٰ يَوْمِ يُبْعَثُونَ
- (9:36) [listed for 1:4] إِنَّ عِدَّةَ ٱلشُّهُورِ عِندَ ٱللَّهِ ٱثْنَا عَشَرَ شَهْرًۭا فِى كِتَٰبِ ٱللَّهِ يَوْمَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ مِنْهَآ أَرْبَعَةٌ حُرُمٌۭ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ ۚ فَلَا تَظْلِمُوا۟ فِيهِنَّ أَنفُسَكُمْ ۚ وَقَٰتِلُوا۟ ٱلْمُشْرِكِينَ كَآفَّةًۭ كَمَا يُقَٰتِلُونَكُمْ كَآفَّةًۭ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَعَ ٱلْمُتَّقِينَ
- (9:116) [listed for 1:4] إِنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ يُحْىِۦ وَيُمِيتُ ۚ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (26:156) [listed for 1:4] وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابُ يَوْمٍ عَظِيمٍۢ
- (46:5) [listed for 1:4] وَمَنْ أَضَلُّ مِمَّن يَدْعُوا۟ مِن دُونِ ٱللَّهِ مَن لَّا يَسْتَجِيبُ لَهُۥٓ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ وَهُمْ عَن دُعَآئِهِمْ غَٰفِلُونَ
- (53:26) [listed for 1:4] ۞ وَكَم مِّن مَّلَكٍۢ فِى ٱلسَّمَٰوَٰتِ لَا تُغْنِى شَفَٰعَتُهُمْ شَيْـًٔا إِلَّا مِنۢ بَعْدِ أَن يَأْذَنَ ٱللَّهُ لِمَن يَشَآءُ وَيَرْضَىٰٓ
- (60:6) [listed for 1:4] لَقَدْ كَانَ لَكُمْ فِيهِمْ أُسْوَةٌ حَسَنَةٌۭ لِّمَن كَانَ يَرْجُوا۟ ٱللَّهَ وَٱلْيَوْمَ ٱلْءَاخِرَ ۚ وَمَن يَتَوَلَّ فَإِنَّ ٱللَّهَ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ
- (106:4) [listed for 1:4] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ

## named by the passage's own list as weak for this ayah (21)

- (3:55) [listed for 1:4] إِذْ قَالَ ٱللَّهُ يَٰعِيسَىٰٓ إِنِّى مُتَوَفِّيكَ وَرَافِعُكَ إِلَىَّ وَمُطَهِّرُكَ مِنَ ٱلَّذِينَ كَفَرُوا۟ وَجَاعِلُ ٱلَّذِينَ ٱتَّبَعُوكَ فَوْقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۖ ثُمَّ إِلَىَّ مَرْجِعُكُمْ فَأَحْكُمُ بَيْنَكُمْ فِيمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
- (6:137) [listed for 1:4] وَكَذَٰلِكَ زَيَّنَ لِكَثِيرٍۢ مِّنَ ٱلْمُشْرِكِينَ قَتْلَ أَوْلَٰدِهِمْ شُرَكَآؤُهُمْ لِيُرْدُوهُمْ وَلِيَلْبِسُوا۟ عَلَيْهِمْ دِينَهُمْ ۖ وَلَوْ شَآءَ ٱللَّهُ مَا فَعَلُوهُ ۖ فَذَرْهُمْ وَمَا يَفْتَرُونَ
- (6:161) [listed for 1:4] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- (9:11) [listed for 1:4] فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ ۗ وَنُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (11:31) [listed for 1:4] وَلَآ أَقُولُ لَكُمْ عِندِى خَزَآئِنُ ٱللَّهِ وَلَآ أَعْلَمُ ٱلْغَيْبَ وَلَآ أَقُولُ إِنِّى مَلَكٌۭ وَلَآ أَقُولُ لِلَّذِينَ تَزْدَرِىٓ أَعْيُنُكُمْ لَن يُؤْتِيَهُمُ ٱللَّهُ خَيْرًا ۖ ٱللَّهُ أَعْلَمُ بِمَا فِىٓ أَنفُسِهِمْ ۖ إِنِّىٓ إِذًۭا لَّمِنَ ٱلظَّٰلِمِينَ
- (19:15) [listed for 1:4] وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا
- (26:38) [listed for 1:4] فَجُمِعَ ٱلسَّحَرَةُ لِمِيقَٰتِ يَوْمٍۢ مَّعْلُومٍۢ
- (29:65) [listed for 1:4] فَإِذَا رَكِبُوا۟ فِى ٱلْفُلْكِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ إِذَا هُمْ يُشْرِكُونَ
- (30:30) [listed for 1:4] فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا ۚ فِطْرَتَ ٱللَّهِ ٱلَّتِى فَطَرَ ٱلنَّاسَ عَلَيْهَا ۚ لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (31:32) [listed for 1:4] وَإِذَا غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ فَمِنْهُم مُّقْتَصِدٌۭ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا كُلُّ خَتَّارٍۢ كَفُورٍۢ
- (40:32) [listed for 1:4] وَيَٰقَوْمِ إِنِّىٓ أَخَافُ عَلَيْكُمْ يَوْمَ ٱلتَّنَادِ
- (42:13) [listed for 1:4] ۞ شَرَعَ لَكُم مِّنَ ٱلدِّينِ مَا وَصَّىٰ بِهِۦ نُوحًۭا وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَمَا وَصَّيْنَا بِهِۦٓ إِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَىٰٓ ۖ أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ ۚ ٱللَّهُ يَجْتَبِىٓ إِلَيْهِ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَن يُنِيبُ
- (50:30) [listed for 1:4] يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ
- (50:34) [listed for 1:4] ٱدْخُلُوهَا بِسَلَٰمٍۢ ۖ ذَٰلِكَ يَوْمُ ٱلْخُلُودِ
- (52:9) [listed for 1:4] يَوْمَ تَمُورُ ٱلسَّمَآءُ مَوْرًۭا
- (70:8) [listed for 1:4] يَوْمَ تَكُونُ ٱلسَّمَآءُ كَٱلْمُهْلِ
- (73:14) [listed for 1:4] يَوْمَ تَرْجُفُ ٱلْأَرْضُ وَٱلْجِبَالُ وَكَانَتِ ٱلْجِبَالُ كَثِيبًۭا مَّهِيلًا
- (79:32) [listed for 1:4] وَٱلْجِبَالَ أَرْسَىٰهَا
- (90:14) [listed for 1:4] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- (109:4) [listed for 1:4] وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- (109:5) [listed for 1:4] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ

## neighbours: within two ayat of a passage the commentary cites (110)

- (2:223) [next to 2:225] نِسَآؤُكُمْ حَرْثٌۭ لَّكُمْ فَأْتُوا۟ حَرْثَكُمْ أَنَّىٰ شِئْتُمْ ۖ وَقَدِّمُوا۟ لِأَنفُسِكُمْ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّكُم مُّلَٰقُوهُ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (2:224) [next to 2:225] وَلَا تَجْعَلُوا۟ ٱللَّهَ عُرْضَةًۭ لِّأَيْمَٰنِكُمْ أَن تَبَرُّوا۟ وَتَتَّقُوا۟ وَتُصْلِحُوا۟ بَيْنَ ٱلنَّاسِ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- (2:226) [next to 2:225] لِّلَّذِينَ يُؤْلُونَ مِن نِّسَآئِهِمْ تَرَبُّصُ أَرْبَعَةِ أَشْهُرٍۢ ۖ فَإِن فَآءُو فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:227) [next to 2:225] وَإِنْ عَزَمُوا۟ ٱلطَّلَٰقَ فَإِنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (2:278) [next to 2:280] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَذَرُوا۟ مَا بَقِىَ مِنَ ٱلرِّبَوٰٓا۟ إِن كُنتُم مُّؤْمِنِينَ
- (2:279) [next to 2:280] فَإِن لَّمْ تَفْعَلُوا۟ فَأْذَنُوا۟ بِحَرْبٍۢ مِّنَ ٱللَّهِ وَرَسُولِهِۦ ۖ وَإِن تُبْتُمْ فَلَكُمْ رُءُوسُ أَمْوَٰلِكُمْ لَا تَظْلِمُونَ وَلَا تُظْلَمُونَ
- (2:283) [next to 2:281] ۞ وَإِن كُنتُمْ عَلَىٰ سَفَرٍۢ وَلَمْ تَجِدُوا۟ كَاتِبًۭا فَرِهَٰنٌۭ مَّقْبُوضَةٌۭ ۖ فَإِنْ أَمِنَ بَعْضُكُم بَعْضًۭا فَلْيُؤَدِّ ٱلَّذِى ٱؤْتُمِنَ أَمَٰنَتَهُۥ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ ۗ وَلَا تَكْتُمُوا۟ ٱلشَّهَٰدَةَ ۚ وَمَن يَكْتُمْهَا فَإِنَّهُۥٓ ءَاثِمٌۭ قَلْبُهُۥ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (2:284) [next to 2:282] لِّلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِن تُبْدُوا۟ مَا فِىٓ أَنفُسِكُمْ أَوْ تُخْفُوهُ يُحَاسِبْكُم بِهِ ٱللَّهُ ۖ فَيَغْفِرُ لِمَن يَشَآءُ وَيُعَذِّبُ مَن يَشَآءُ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (3:24) [next to 3:26] ذَٰلِكَ بِأَنَّهُمْ قَالُوا۟ لَن تَمَسَّنَا ٱلنَّارُ إِلَّآ أَيَّامًۭا مَّعْدُودَٰتٍۢ ۖ وَغَرَّهُمْ فِى دِينِهِم مَّا كَانُوا۟ يَفْتَرُونَ
- (3:27) [next to 3:26] تُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَتُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ ۖ وَتُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَتُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ ۖ وَتَرْزُقُ مَن تَشَآءُ بِغَيْرِ حِسَابٍۢ
- (3:28) [next to 3:26] لَّا يَتَّخِذِ ٱلْمُؤْمِنُونَ ٱلْكَٰفِرِينَ أَوْلِيَآءَ مِن دُونِ ٱلْمُؤْمِنِينَ ۖ وَمَن يَفْعَلْ ذَٰلِكَ فَلَيْسَ مِنَ ٱللَّهِ فِى شَىْءٍ إِلَّآ أَن تَتَّقُوا۟ مِنْهُمْ تُقَىٰةًۭ ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (6:10) [next to 6:12] وَلَقَدِ ٱسْتُهْزِئَ بِرُسُلٍۢ مِّن قَبْلِكَ فَحَاقَ بِٱلَّذِينَ سَخِرُوا۟ مِنْهُم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (6:11) [next to 6:12] قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ ثُمَّ ٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (6:13) [next to 6:12] ۞ وَلَهُۥ مَا سَكَنَ فِى ٱلَّيْلِ وَٱلنَّهَارِ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:14) [next to 6:12] قُلْ أَغَيْرَ ٱللَّهِ أَتَّخِذُ وَلِيًّۭا فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ ۗ قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَكُونَ أَوَّلَ مَنْ أَسْلَمَ ۖ وَلَا تَكُونَنَّ مِنَ ٱلْمُشْرِكِينَ
- (7:48) [next to 7:50] وَنَادَىٰٓ أَصْحَٰبُ ٱلْأَعْرَافِ رِجَالًۭا يَعْرِفُونَهُم بِسِيمَىٰهُمْ قَالُوا۟ مَآ أَغْنَىٰ عَنكُمْ جَمْعُكُمْ وَمَا كُنتُمْ تَسْتَكْبِرُونَ
- (7:49) [next to 7:50] أَهَٰٓؤُلَآءِ ٱلَّذِينَ أَقْسَمْتُمْ لَا يَنَالُهُمُ ٱللَّهُ بِرَحْمَةٍ ۚ ٱدْخُلُوا۟ ٱلْجَنَّةَ لَا خَوْفٌ عَلَيْكُمْ وَلَآ أَنتُمْ تَحْزَنُونَ
- (7:52) [next to 7:50] وَلَقَدْ جِئْنَٰهُم بِكِتَٰبٍۢ فَصَّلْنَٰهُ عَلَىٰ عِلْمٍ هُدًۭى وَرَحْمَةًۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:53) [next to 7:51] هَلْ يَنظُرُونَ إِلَّا تَأْوِيلَهُۥ ۚ يَوْمَ يَأْتِى تَأْوِيلُهُۥ يَقُولُ ٱلَّذِينَ نَسُوهُ مِن قَبْلُ قَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ فَهَل لَّنَا مِن شُفَعَآءَ فَيَشْفَعُوا۟ لَنَآ أَوْ نُرَدُّ فَنَعْمَلَ غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ قَدْ خَسِرُوٓا۟ أَنفُسَهُمْ وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ
- (11:95) [next to 11:97] كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ ۗ أَلَا بُعْدًۭا لِّمَدْيَنَ كَمَا بَعِدَتْ ثَمُودُ
- (11:96) [next to 11:97] وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِـَٔايَٰتِنَا وَسُلْطَٰنٍۢ مُّبِينٍ
- (11:99) [next to 11:97] وَأُتْبِعُوا۟ فِى هَٰذِهِۦ لَعْنَةًۭ وَيَوْمَ ٱلْقِيَٰمَةِ ۚ بِئْسَ ٱلرِّفْدُ ٱلْمَرْفُودُ
- (11:100) [next to 11:98] ذَٰلِكَ مِنْ أَنۢبَآءِ ٱلْقُرَىٰ نَقُصُّهُۥ عَلَيْكَ ۖ مِنْهَا قَآئِمٌۭ وَحَصِيدٌۭ
- (12:68) [next to 12:70] وَلَمَّا دَخَلُوا۟ مِنْ حَيْثُ أَمَرَهُمْ أَبُوهُم مَّا كَانَ يُغْنِى عَنْهُم مِّنَ ٱللَّهِ مِن شَىْءٍ إِلَّا حَاجَةًۭ فِى نَفْسِ يَعْقُوبَ قَضَىٰهَا ۚ وَإِنَّهُۥ لَذُو عِلْمٍۢ لِّمَا عَلَّمْنَٰهُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (12:69) [next to 12:70] وَلَمَّا دَخَلُوا۟ عَلَىٰ يُوسُفَ ءَاوَىٰٓ إِلَيْهِ أَخَاهُ ۖ قَالَ إِنِّىٓ أَنَا۠ أَخُوكَ فَلَا تَبْتَئِسْ بِمَا كَانُوا۟ يَعْمَلُونَ
- (12:71) [next to 12:70] قَالُوا۟ وَأَقْبَلُوا۟ عَلَيْهِم مَّاذَا تَفْقِدُونَ
- (12:73) [next to 12:72] قَالُوا۟ تَٱللَّهِ لَقَدْ عَلِمْتُم مَّا جِئْنَا لِنُفْسِدَ فِى ٱلْأَرْضِ وَمَا كُنَّا سَٰرِقِينَ
- (12:74) [next to 12:72] قَالُوا۟ فَمَا جَزَٰٓؤُهُۥٓ إِن كُنتُمْ كَٰذِبِينَ
- (12:77) [next to 12:75] ۞ قَالُوٓا۟ إِن يَسْرِقْ فَقَدْ سَرَقَ أَخٌۭ لَّهُۥ مِن قَبْلُ ۚ فَأَسَرَّهَا يُوسُفُ فِى نَفْسِهِۦ وَلَمْ يُبْدِهَا لَهُمْ ۚ قَالَ أَنتُمْ شَرٌّۭ مَّكَانًۭا ۖ وَٱللَّهُ أَعْلَمُ بِمَا تَصِفُونَ
- (12:78) [next to 12:76] قَالُوا۟ يَٰٓأَيُّهَا ٱلْعَزِيزُ إِنَّ لَهُۥٓ أَبًۭا شَيْخًۭا كَبِيرًۭا فَخُذْ أَحَدَنَا مَكَانَهُۥٓ ۖ إِنَّا نَرَىٰكَ مِنَ ٱلْمُحْسِنِينَ
- (14:3) [next to 14:5] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (14:4) [next to 14:5] وَمَآ أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوْمِهِۦ لِيُبَيِّنَ لَهُمْ ۖ فَيُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (14:6) [next to 14:5] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِ ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ إِذْ أَنجَىٰكُم مِّنْ ءَالِ فِرْعَوْنَ يَسُومُونَكُمْ سُوٓءَ ٱلْعَذَابِ وَيُذَبِّحُونَ أَبْنَآءَكُمْ وَيَسْتَحْيُونَ نِسَآءَكُمْ ۚ وَفِى ذَٰلِكُم بَلَآءٌۭ مِّن رَّبِّكُمْ عَظِيمٌۭ
- (14:7) [next to 14:5] وَإِذْ تَأَذَّنَ رَبُّكُمْ لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ ۖ وَلَئِن كَفَرْتُمْ إِنَّ عَذَابِى لَشَدِيدٌۭ
- (16:50) [next to 16:52] يَخَافُونَ رَبَّهُم مِّن فَوْقِهِمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ ۩
- (16:51) [next to 16:52] ۞ وَقَالَ ٱللَّهُ لَا تَتَّخِذُوٓا۟ إِلَٰهَيْنِ ٱثْنَيْنِ ۖ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ ۖ فَإِيَّٰىَ فَٱرْهَبُونِ
- (16:53) [next to 16:52] وَمَا بِكُم مِّن نِّعْمَةٍۢ فَمِنَ ٱللَّهِ ۖ ثُمَّ إِذَا مَسَّكُمُ ٱلضُّرُّ فَإِلَيْهِ تَجْـَٔرُونَ
- (16:54) [next to 16:52] ثُمَّ إِذَا كَشَفَ ٱلضُّرَّ عَنكُمْ إِذَا فَرِيقٌۭ مِّنكُم بِرَبِّهِمْ يُشْرِكُونَ
- (20:105) [next to 20:107] وَيَسْـَٔلُونَكَ عَنِ ٱلْجِبَالِ فَقُلْ يَنسِفُهَا رَبِّى نَسْفًۭا
- (20:106) [next to 20:107] فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا
- (20:110) [next to 20:108] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِهِۦ عِلْمًۭا
- (24:22) [next to 24:24] وَلَا يَأْتَلِ أُو۟لُوا۟ ٱلْفَضْلِ مِنكُمْ وَٱلسَّعَةِ أَن يُؤْتُوٓا۟ أُو۟لِى ٱلْقُرْبَىٰ وَٱلْمَسَٰكِينَ وَٱلْمُهَٰجِرِينَ فِى سَبِيلِ ٱللَّهِ ۖ وَلْيَعْفُوا۟ وَلْيَصْفَحُوٓا۟ ۗ أَلَا تُحِبُّونَ أَن يَغْفِرَ ٱللَّهُ لَكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌ
- (24:23) [next to 24:24] إِنَّ ٱلَّذِينَ يَرْمُونَ ٱلْمُحْصَنَٰتِ ٱلْغَٰفِلَٰتِ ٱلْمُؤْمِنَٰتِ لُعِنُوا۟ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
- (24:26) [next to 24:24] ٱلْخَبِيثَٰتُ لِلْخَبِيثِينَ وَٱلْخَبِيثُونَ لِلْخَبِيثَٰتِ ۖ وَٱلطَّيِّبَٰتُ لِلطَّيِّبِينَ وَٱلطَّيِّبُونَ لِلطَّيِّبَٰتِ ۚ أُو۟لَٰٓئِكَ مُبَرَّءُونَ مِمَّا يَقُولُونَ ۖ لَهُم مَّغْفِرَةٌۭ وَرِزْقٌۭ كَرِيمٌۭ
- (24:27) [next to 24:25] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَدْخُلُوا۟ بُيُوتًا غَيْرَ بُيُوتِكُمْ حَتَّىٰ تَسْتَأْنِسُوا۟ وَتُسَلِّمُوا۟ عَلَىٰٓ أَهْلِهَا ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ لَعَلَّكُمْ تَذَكَّرُونَ
- (25:24) [next to 25:26] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (25:25) [next to 25:26] وَيَوْمَ تَشَقَّقُ ٱلسَّمَآءُ بِٱلْغَمَٰمِ وَنُزِّلَ ٱلْمَلَٰٓئِكَةُ تَنزِيلًا
- (25:27) [next to 25:26] وَيَوْمَ يَعَضُّ ٱلظَّالِمُ عَلَىٰ يَدَيْهِ يَقُولُ يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا
- (25:28) [next to 25:26] يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا
- (26:80) [next to 26:82] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (26:81) [next to 26:82] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (26:83) [next to 26:82] رَبِّ هَبْ لِى حُكْمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (26:84) [next to 26:82] وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ
- (26:86) [next to 26:88] وَٱغْفِرْ لِأَبِىٓ إِنَّهُۥ كَانَ مِنَ ٱلضَّآلِّينَ
- (26:87) [next to 26:88] وَلَا تُخْزِنِى يَوْمَ يُبْعَثُونَ
- (26:90) [next to 26:88] وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ
- (26:91) [next to 26:89] وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ
- (37:51) [next to 37:53] قَالَ قَآئِلٌۭ مِّنْهُمْ إِنِّى كَانَ لِى قَرِينٌۭ
- (37:52) [next to 37:53] يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ
- (37:54) [next to 37:53] قَالَ هَلْ أَنتُم مُّطَّلِعُونَ
- (37:55) [next to 37:53] فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ
- (40:15) [next to 40:16] رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ
- (40:18) [next to 40:16] وَأَنذِرْهُمْ يَوْمَ ٱلْءَازِفَةِ إِذِ ٱلْقُلُوبُ لَدَى ٱلْحَنَاجِرِ كَٰظِمِينَ ۚ مَا لِلظَّٰلِمِينَ مِنْ حَمِيمٍۢ وَلَا شَفِيعٍۢ يُطَاعُ
- (43:49) [next to 43:51] وَقَالُوا۟ يَٰٓأَيُّهَ ٱلسَّاحِرُ ٱدْعُ لَنَا رَبَّكَ بِمَا عَهِدَ عِندَكَ إِنَّنَا لَمُهْتَدُونَ
- (43:50) [next to 43:51] فَلَمَّا كَشَفْنَا عَنْهُمُ ٱلْعَذَابَ إِذَا هُمْ يَنكُثُونَ
- (43:52) [next to 43:51] أَمْ أَنَا۠ خَيْرٌۭ مِّنْ هَٰذَا ٱلَّذِى هُوَ مَهِينٌۭ وَلَا يَكَادُ يُبِينُ
- (43:53) [next to 43:51] فَلَوْلَآ أُلْقِىَ عَلَيْهِ أَسْوِرَةٌۭ مِّن ذَهَبٍ أَوْ جَآءَ مَعَهُ ٱلْمَلَٰٓئِكَةُ مُقْتَرِنِينَ
- (45:30) [next to 45:28] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَيُدْخِلُهُمْ رَبُّهُمْ فِى رَحْمَتِهِۦ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْمُبِينُ
- (45:31) [next to 45:29] وَأَمَّا ٱلَّذِينَ كَفَرُوٓا۟ أَفَلَمْ تَكُنْ ءَايَٰتِى تُتْلَىٰ عَلَيْكُمْ فَٱسْتَكْبَرْتُمْ وَكُنتُمْ قَوْمًۭا مُّجْرِمِينَ
- (51:4) [next to 51:6] فَٱلْمُقَسِّمَٰتِ أَمْرًا
- (51:5) [next to 51:6] إِنَّمَا تُوعَدُونَ لَصَادِقٌۭ
- (51:7) [next to 51:6] وَٱلسَّمَآءِ ذَاتِ ٱلْحُبُكِ
- (51:8) [next to 51:6] إِنَّكُمْ لَفِى قَوْلٍۢ مُّخْتَلِفٍۢ
- (56:81) [next to 56:83] أَفَبِهَٰذَا ٱلْحَدِيثِ أَنتُم مُّدْهِنُونَ
- (56:82) [next to 56:83] وَتَجْعَلُونَ رِزْقَكُمْ أَنَّكُمْ تُكَذِّبُونَ
- (56:84) [next to 56:83] وَأَنتُمْ حِينَئِذٍۢ تَنظُرُونَ
- (56:88) [next to 56:86] فَأَمَّآ إِن كَانَ مِنَ ٱلْمُقَرَّبِينَ
- (56:89) [next to 56:87] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (70:0) [next to 70:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (70:2) [next to 70:1] لِّلْكَٰفِرِينَ لَيْسَ لَهُۥ دَافِعٌۭ
- (70:3) [next to 70:1] مِّنَ ٱللَّهِ ذِى ٱلْمَعَارِجِ
- (70:5) [next to 70:4] فَٱصْبِرْ صَبْرًۭا جَمِيلًا
- (70:6) [next to 70:4] إِنَّهُمْ يَرَوْنَهُۥ بَعِيدًۭا
- (70:24) [next to 70:26] وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ
- (70:25) [next to 70:26] لِّلسَّآئِلِ وَٱلْمَحْرُومِ
- (70:27) [next to 70:26] وَٱلَّذِينَ هُم مِّنْ عَذَابِ رَبِّهِم مُّشْفِقُونَ
- (70:28) [next to 70:26] إِنَّ عَذَابَ رَبِّهِمْ غَيْرُ مَأْمُونٍۢ
- (74:42) [next to 74:44] مَا سَلَكَكُمْ فِى سَقَرَ
- (74:43) [next to 74:44] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
- (74:45) [next to 74:44] وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ
- (74:47) [next to 74:46] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
- (74:48) [next to 74:46] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
- (78:35) [next to 78:37] لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا
- (78:36) [next to 78:37] جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا
- (78:39) [next to 78:37] ذَٰلِكَ ٱلْيَوْمُ ٱلْحَقُّ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا
- (78:40) [next to 78:38] إِنَّآ أَنذَرْنَٰكُمْ عَذَابًۭا قَرِيبًۭا يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ وَيَقُولُ ٱلْكَافِرُ يَٰلَيْتَنِى كُنتُ تُرَٰبًۢا
- (80:32) [next to 80:34] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (80:38) [next to 80:36] وُجُوهٌۭ يَوْمَئِذٍۢ مُّسْفِرَةٌۭ
- (80:39) [next to 80:37] ضَاحِكَةٌۭ مُّسْتَبْشِرَةٌۭ
- (81:0) [next to 81:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (81:2) [next to 81:1] وَإِذَا ٱلنُّجُومُ ٱنكَدَرَتْ
- (81:3) [next to 81:1] وَإِذَا ٱلْجِبَالُ سُيِّرَتْ
- (82:16) [next to 82:17] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
- (107:0) [next to 107:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (107:3) [next to 107:1] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (107:4) [next to 107:2] فَوَيْلٌۭ لِّلْمُصَلِّينَ
- (114:0) [next to 114:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (114:1) [next to 114:2] قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- (114:4) [next to 114:2] مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- (114:5) [next to 114:3] ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ

