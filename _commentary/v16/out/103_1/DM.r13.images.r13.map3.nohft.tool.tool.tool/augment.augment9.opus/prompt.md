Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 103:1; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/103_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/103_1.reading.tr.md (prose paragraphs numbered) =====
## Tek kelimelik bir yemin

[¶1] Sure tek bir kelimeyle açılır: {ar:وَٱلْعَصْرِ, tr:ve'l-asr, gloss:asra andolsun, source:103:1}. Baştaki "ve" burada iki şeyi birbirine bağlayan bağlaç değil, yemin edatıdır; ardındaki isim bu yüzden esre ile okunur. Yeminin neye dair olduğu bu ayette söylenmez, bir sonraki ayete bırakılır. Birinci ayet bu yüzden bir eşik gibidir: okuyan, neyin üzerine yemin edildiğini duyar, ama hangi hükmün söyleneceğini henüz bilmez. Hüküm ikinci ayette gelir: {ar:إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ, tr:inne'l-insâne le-fî husr, gloss:insan gerçekten kayıp içindedir, source:103:2}. Yeminle öne konan şey, ardından gelecek hükmün hemen yanına yerleştirilmiştir; asrın ne olduğunu iyi duymak, kaybın nasıl bir kayıp olduğunu duymanın da yoludur.

[¶2] Kur'an başka surelerde de günün vakitleri üzerine yemin eder: {ar:وَٱلْفَجْرِ, tr:ve'l-fecr, gloss:şafağa andolsun, source:89:1}, {ar:وَٱلضُّحَىٰ, tr:ve'd-duhâ, gloss:kuşluk vaktine andolsun, source:93:1}, {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:her şeyi örttüğünde geceye andolsun, source:92:1}, {ar:وَٱلصُّبْحِ إِذَآ أَسْفَرَ, tr:ve's-subhi izâ esfer, gloss:ağardığında sabaha andolsun, source:74:34}. Bunların çoğunda vakit bir hareketle birlikte anılır: gece örttüğünde, sabah ağardığında. Asr ise yalnız gelir, hiçbir niteleme almaz; bu yalnızlık kelimenin genişliğini açık bırakır. Çünkü aynı kelime hem günün bir dilimini hem de zamanın bütününü adlandırır. Uzun zamana, çağa {ar:العصر الدهر, tr:el-asru'd-dehr, gloss:asr, uzun zaman, çağdır, source:"ع ص ر,B001"} denir; günün akşama yakın kısmına da {ar:العصر العشي, tr:el-asru'l-aşiyy, gloss:asr, akşamüstüdür, source:"ع ص ر,B001"}; o vakitte kılınan namaz da adını ondan alır: {ar:صلاة العصر, tr:salâtu'l-asr, gloss:ikindi namazı, source:"ع ص ر,B001"}. Kelimedeki belirlilik takısı bilinen bir vakti gösterir, ama hangisinin, günün ikindisinin mi, insanın içinde yaşadığı çağın mı, zamanın kendisinin mi kastedildiğini ayet söylemez. Tek kelime, okuyanı bunları birlikte duymaya bırakır.

[¶3] Türkçe bu kelimeyi ikiye bölmüştür. "Asır" bugün yüz yıl demektir, "asri" de çağdaş; günün sonu ise "ikindi" diye başka bir kelimeyle söylenir. Türkçede "asır" denince ne akşamüstünün azalan ışığı duyulur ne de aşağıda görülecek sıkma, sığınak ve kasırga. Ayetteki kelime ise saati de çağı da bir arada tutar: bir günün sonu ile bir ömrün sonu aynı adı taşır.

[¶4] Araplar kelimeyi ikil olarak da kullanır, günün iki ucunu birlikte "iki asr" diye anarlardı: {ar:العصران الليل والنهار, tr:el-asrâni'l-leylu ve'n-nehâr, gloss:iki asr, gece ile gündüz, source:"ع ص ر,B001"}, {ar:العصران الغداة والعشي, tr:el-asrâni'l-gadâtu ve'l-aşiyy, gloss:iki asr, sabah erkeni ile akşamüstü, source:"ع ص ر,B001"}. Kur'an bu çifti, günün iki kenarını, kendi sözleriyle anar. Peygamber'e, yanındaki bir grup mümin hakkında şöyle denir: {ar:وَلَا تَطْرُدِ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ, tr:ve lâ tatrudi'llezîne yed'ûne rabbehum bi'l-gadâti ve'l-aşiyyi yurîdûne vechehû, gloss:sabah akşam, O'nun rızasını isteyerek Rablerine yalvaranları kovma, source:6:52}. Bir başka surede, dosdoğru durması emredilen Peygamber'e namazın vakti yine bu iki uçla verilir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ وَزُلَفًۭا مِّنَ ٱلَّيْلِ, tr:ve ekimi's-salâte tarafeyi'n-nehâri ve zulefen mine'l-leyl, gloss:namazı gündüzün iki ucunda ve gecenin ilk saatlerinde kıl, source:11:114}. Asrın günün iki ucunun adı olması, kelimenin zamanı kenarından tuttuğunu gösterir: bir dönemin girildiği ve çıkıldığı yerden. Ayetin akşamüstü anlamı da bu kenarlardan biridir, günün kapanan ucu.

## Geç gelen ve kısalan vakit

[¶5] Kelime gecikmeyi de taşır. Biri vaktinden sonra, ağır ağır gelince {ar:جاءني فلان عصرا أي بطيئا, tr:câenî fulânun asran, gloss:falanca bana geç, ağır ağır geldi, source:"ع ص ر,B001"} derlerdi. Gözüne uyku girmemiş biri için {ar:نام وما نام لعصر, tr:nâme ve mâ nâme li-asr, gloss:yattı ama bir an bile uyumadı, source:"ع ص ر,B001"} denirdi; bir zaman parçasına {ar:العصار الحين, tr:el-asâru'l-hîn, gloss:asâr, bir süredir, source:"ع ص ر,B001"} adı verilirdi. Böylece asr hem uzun bir çağdır hem de göz açıp kapayıncaya kadar geçen an; hem günün olağan bir dilimidir hem de gecikmiş gelişin vakti. Bir insan ömrünün evrelerine de aynı kelimeyle işaret edilir: genç kız için {ar:بلغت عصر شبابها وإدراكها, tr:belegat asra şebâbihâ ve idrâkihâ, gloss:gençliğinin ve erginliğinin çağına erdi, source:"ع ص ر,B009"} derler, kişinin ömrü ve yaşlılığı da bu adla anılır {source:"ع ص ر,B001"}. Akşamüstü günün kalanının en az olduğu saattir: iş bitmek üzeredir, ışık azalır, yapılmamış olan için vakit daralır. Asr bu yüzden yalnızca bir saat değil, bir saatin içinde duyulan geç kalmışlıktır.

[¶6] Kur'an zamanın sonda nasıl daraldığını, insanın kendi süresini dönüp nasıl ölçtüğünü gösterir. Peygamber'e kıyamet sorulur: {ar:يَسْـَٔلُونَكَ عَنِ ٱلسَّاعَةِ أَيَّانَ مُرْسَىٰهَا, tr:yes'elûneke ani's-sâ'ati eyyâne mursâhâ, gloss:sana o Saat'i, ne zaman demir atacağını soruyorlar, source:79:42}. Surenin son ayeti cevap yerine bir ölçü verir; o Saat görüldüğünde bütün ömür bir günün tek dilimine iner: {ar:كَأَنَّهُمْ يَوْمَ يَرَوْنَهَا لَمْ يَلْبَثُوٓا۟ إِلَّا عَشِيَّةً أَوْ ضُحَىٰهَا, tr:keennehum yevme yerevnehâ lem yelbesû illâ aşiyyeten ev duhâhâ, gloss:onu gördükleri gün, sanki bir akşamüstü ya da onun kuşluğu kadar kalmışlardır, source:79:46}. Buradaki kelime asr değildir, ama asrın kendisiyle açıklandığı akşamüstüdür: uzun çağ ile akşamüstünün aynı kelimede durması, sondan bakılınca birinin ötekine dönüşmesidir. Cehennemdekilerin feryadında ise geç kalmış iş açıkça görünür: {ar:رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ, tr:rabbenâ ahricnâ na'mel sâlihan gayra'llezî kunnâ na'mel, gloss:Rabbimiz, bizi çıkar da yaptığımızdan başka, salih bir iş yapalım, source:35:37}; aynı ayetteki cevap ömrü verilmiş bir süre olarak anar: {ar:أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ, tr:e-ve lem nu'ammirkum mâ yetezekkeru fîhi men tezekker, gloss:size, düşünecek olanın düşünebileceği kadar ömür vermedik mi, source:35:37}. İkinci ayetin kaybı da, üçüncü ayetin iman ve salih işi de bu verilmiş süre içinde yer alır.

## Sıkmak: öz, kuruluk ve yudum

[¶7] Kelimenin en somut işi sıkmaktır. Buradan sonra anılacak imgeler ayetteki "zaman" anlamının yerine geçmez, onun yanında duyulur. Sıkma bir yöntemle tarif edilir: {ar:ضغط شيء حتى يتحلب, tr:dagtu şey'in hattâ yetehalleb, gloss:bir şeyi suyu sağılır gibi akana dek bastırmak, source:"ع ص ر,B002"}. Üzüm sıkmak için yem torbasına benzeyen bir torba kullanılırdı: {ar:المعصار شيء كالمخلاة يجعل فيه العنب ويعصر, tr:el-mi'sâr şey'un ke'l-mihlât, gloss:içine üzüm konup sıkılan, yem torbasına benzer bir şey, source:"ع ص ر,B002"}; sıkmanın yapıldığı yere de {ar:المعصرة ما يعصر فيه العنب, tr:el-ma'sara, gloss:içinde üzüm sıkılan yer, source:"ع ص ر,B002"} denirdi. Torba üzümü bir arada tutar, el ya da ağırlık onu bastırır, kabuklar yarılır ve sıvı torbanın dokusundan süzülüp akar. Akana {ar:العصارة ما سال عن العصر, tr:el-usâratu mâ sâle ani'l-asr, gloss:usâre, sıkmadan akandır, source:"ع ص ر,B002"} adı verilir; suyu sıkılarak alınmış her şeye de {ar:كل شيء عصر ماؤه فهو عصير, tr:kullu şey'in usira mâuhû fe-huve asîr, gloss:suyu sıkılmış her şey asîrdir, source:"ع ص ر,B002"} denir. Torbada kalan ise posadır {source:"ع ص ر,B002"}. Sıkma böylece bir şeyi ikiye ayırır: akıp giden öz ve geride kalan kuru kütle.

[¶8] Bu işin ürünü iyiliğin adı olmuştur. Araplar sıkılıp akan özü hayrın ve bağışın misali yaparlardı {ar:العرب تجعل العصارة والمعتصر مثلا للخير والعطاء, tr:el-arabu tec'alu'l-usârate ve'l-mu'tasare mesalen li'l-hayri ve'l-atâ', gloss:Araplar usâreyi ve sıkılan yeri hayır ve bağış için misal yaparlar, source:"ع ص ر,B007"}; cömert biri için {ar:يعصر فينا كالذي تعصر, tr:ya'siru fînâ ke'llezî ta'sir, gloss:bize senin verdiğin gibi verir, source:"ع ص ر,B007"} derlerdi, topraktan alınan gelire de {ar:العصارة الغلة, tr:el-usâratu'l-galle, gloss:usâre, üründür, source:"ع ص ر,B007"} denirdi. Sıkma göğe de taşınır. Bulutun yağmurla sıkıldığı söylenir: {ar:المعصرات السحائب تعتصر بالمطر, tr:el-mu'sırâtu's-sehâibu ta'tasıru bi'l-matar, gloss:mu'sırât, yağmurla sıkılan bulutlardır, source:"ع ص ر,B003"}, {ar:السحابة المعصر التي تتحلب بالمطر, tr:es-sehâbetu'l-mu'sır, gloss:yağmuru sağılır gibi akıtan bulut, source:"ع ص ر,B003"}; yağmura kavuşan topluluk için {ar:عصر القوم أي مطروا, tr:usira'l-kavm, gloss:topluluk yağmura kavuştu, source:"ع ص ر,B003"} denir. Kur'an bu bulutları kendi adlarıyla anar. Kıyamet haberini tartışanlara yeryüzünün düzeni sayılırken şöyle denir: {ar:وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا, tr:ve enzelnâ mine'l-mu'sırâti mâen seccâcâ, gloss:sıkılan bulutlardan şarıl şarıl su indirdik, source:78:14}, {ar:لِّنُخْرِجَ بِهِۦ حَبًّۭا وَنَبَاتًۭا, tr:li-nuhrice bihî habben ve nebâtâ, gloss:onunla tane ve bitki çıkaralım diye, source:78:15}, {ar:وَجَنَّٰتٍ أَلْفَافًا, tr:ve cennâtin elfâfâ, gloss:ve iç içe geçmiş bahçeler, source:78:16}. Bulutun sıkılması burada bir bereket zinciri başlatır: sıkılan bulut, tane, bitki, bahçe.

[¶9] Sıkmanın öteki ucu kuruluktur. Susuzluktan kurumuş dile {ar:المعصور اللسان اليابس عطشا, tr:el-ma'sûru'l-lisânu'l-yâbisu atşâ, gloss:ma'sûr, susuzluktan kurumuş dildir, source:"ع ص ر,B014"} denir: sıkılmış, içinde su kalmamış dil. Aynı fiil bir kurtuluş hareketini de adlandırır. Lokma boğazına takılan kişi suyu azar azar içerek onu geçirir: {ar:الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء وهو أن يشربه قليلا قليلا ليسيغه, tr:el-i'tisâru en yagassa'l-insânu bi't-taâmi fe-ya'tasıra bi'l-mâ', gloss:i'tisâr, insanın yemekle tıkanınca suyu yudum yudum içip lokmayı geçirmesidir, source:"ع ص ر,B008"}. Bir şair bu hareketi tersinden kullanmıştır: {ar:لو بغير الماء حلقي شرق كنت كالغصان بالماء اعتصاري, tr:lev bi-gayri'l-mâi halkî şarikun kuntu ke'l-gassâni bi'l-mâi'-tisârî, gloss:boğazım sudan başka bir şeyle tıkansaydı, suyla yudumlayıp kurtulan tıkanmış biri gibi olurdum, source:"ع ص ر,B008"}; söylemediği ama duyurduğu şudur: onu tıkayan suyun kendisidir, kurtaracak yudum kalmamıştır.

[¶10] Bu imgeler ayetteki zamanın yanında duyulunca zaman bir baskı olarak görünür. Günler insanın üzerinden geçer ve ondan bir şey çıkarır: ya özü akar, bağış olur, bulut gibi yağmur bırakır, ya da kuru bir kütle, susuzluktan kurumuş bir dil kalır. İkinci ayetteki kayıp, sıkılmış olanın geride kalan yanıdır; üçüncü ayetin son kelimesi olan sabrın da bir ağaçtan sıkılan acı özün adı olması {source:"ص ب ر,B008"} bu baskıyı surenin sonuna taşır.

## Yusuf'un zindanında sıkılan üzüm ve beklenen yıl

[¶11] Kur'an sıkma fiilini bir zindanda kullanır ve onu uzun bir bekleyişin içine yerleştirir. Yusuf suçsuz olduğu belli olduktan sonra, kendisini sıkıştıranların kararıyla zindana atılır: {ar:لَيَسْجُنُنَّهُۥ حَتَّىٰ حِينٍۢ, tr:le-yescununnehû hattâ hîn, gloss:onu bir süreye kadar mutlaka zindana atacaklardı, source:12:35}. Zindan burada bir süre ile ölçülmüştür; asra da bir zaman parçası denildiğini, kelimenin alıkoymak anlamı da taşıdığını hatırlamak gerekir {source:"ع ص ر,B006"}. Bu bir bağlantıdır, kelime ortaklığı değil: Kur'an zindan için başka bir kelime kullanır. Yusuf'la birlikte zindana iki genç girer; biri rüyasını anlatır: {ar:إِنِّىٓ أَرَىٰنِىٓ أَعْصِرُ خَمْرًۭا, tr:innî erânî a'siru hamrâ, gloss:kendimi şarap sıkarken görüyorum, source:12:36}. Gencin sıktığı şey üzümdür, ama cümle onu çıkacak içkinin adıyla söyler: sıkma, ürününün adıyla anılır. Yusuf'un yorumu bu genç için kurtuluştur: {ar:أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا, tr:emmâ ehadukumâ fe-yeskî rabbehû hamrâ, gloss:biriniz efendisine şarap sunacak, source:12:41}. Ardından gelen ayet onu kurtulacak olan diye anar: {ar:وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ, tr:ve kâle li'llezî zanne ennehû nâcin minhumâ'zkurnî inde rabbik, gloss:ikisinden kurtulacağını sandığına: beni efendinin yanında an, dedi, source:12:42}. Asrın kurtuluş yeri anlamına da {ar:العصر المنجاة, tr:el-asru'l-mencât, gloss:asr, kurtuluş yeridir, source:"ع ص ر,B005"} denmesi bu sahnede yankılanır: rüyasında sıkan, zindandan kurtulan kişidir.

[¶12] Ama aynı ayet bekleyişi de uzatır: genç Yusuf'u anmayı unutur ve {ar:فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ, tr:fe-lebise fi's-sicni bid'a sinîn, gloss:Yusuf zindanda birkaç yıl kaldı, source:12:42}. Unutan genç ancak kralın rüyası anlatıldığında hatırlar: {ar:وَقَالَ ٱلَّذِى نَجَا مِنْهُمَا وَٱدَّكَرَ بَعْدَ أُمَّةٍ, tr:ve kâle'llezî necâ minhumâ veddekera ba'de ummeh, gloss:ikisinden kurtulmuş olan, uzun bir süre sonra hatırlayıp dedi, source:12:45}. Kralın rüyasında yedi yeşil başak ve yedi kuru başak vardır {ar:وَسَبْعَ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ, tr:ve seb'a sunbulâtin hudrin ve uhara yâbisât, gloss:yedi yeşil başak ve ötekiler kuru, source:12:43}. Yusuf'un yorumu bir zaman planıdır. Önce yedi yıl ekilecek ve ürün başağında bırakılacaktır: {ar:فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ, tr:fe-mâ hasadtum fe-zerûhu fî sunbulihî illâ kalîlen mimmâ te'kulûn, gloss:biçtiğinizi, yiyeceğiniz az bir kısım dışında başağında bırakın, source:12:47}. Araplar, başağın kabukları belirdiğinde ekin için {ar:إذا تبينت أكمام السنبل قيل قد عصر الزرع, tr:izâ tebeyyenet ekmâmu's-sunbuli kîle kad asara'z-zer', gloss:başağın kabukları belirince ekin "asara" oldu denir, source:"ع ص ر,B010"} derlerdi ve bunu korunak anlamına bağlarlardı: {ar:مأخوذ من العصر وهو الحرز أي تحرز في غلفه, tr:me'hûzun mine'l-asri ve huve'l-hirz, gloss:korunak anlamındaki asrdan alınmıştır, tane kabuğunun içinde korunur, source:"ع ص ر,B010"}. Bu bir kalıp içinde yaşayan anlamdır ve Kur'an'ın kelimesi başaktır, asr değil; ama Yusuf'un planı tam bu işi yapar: tane, kabuğunun içinde, darlık yıllarına saklanır. Sonra yedi sert yıl gelir ve saklananı yer: {ar:ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ سَبْعٌۭ شِدَادٌۭ يَأْكُلْنَ مَا قَدَّمْتُمْ لَهُنَّ إِلَّا قَلِيلًۭا مِّمَّا تُحْصِنُونَ, tr:summe ye'tî min ba'di zâlike seb'un şidâdun ye'kulne mâ kaddemtum lehunne illâ kalîlen mimmâ tuhsınûn, gloss:sonra yedi çetin yıl gelir, onlar için biriktirdiğinizi yer, koruyup sakladığınız az bir kısım kalır, source:12:48}. Ve en sonunda: {ar:ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ, tr:summe ye'tî min ba'di zâlike âmun fîhi yugâsu'n-nâsu ve fîhi ya'sirûn, gloss:sonra bir yıl gelir; o yıl insanlar imdada kavuşur ve o yıl sıkarlar, source:12:49}. Bu son fiil, topraktan ürün almak diye de anlaşılmıştır: {ar:يعصرون قال يستغلون بأرضيهم, tr:ya'sirûn, yestagıllûne bi-aradîhim, gloss:sıkarlar, yani topraklarından ürün alırlar, source:"ع ص ر,B007"}.

[¶13] Bu hikâyede kökün birbirinden uzak görünen anlamları tek bir takvime dizilir: zindanda geçen süre, kurtulacak olanın rüyasındaki sıkma, unutulup uzayan yıllar, kabuğunda saklanan tane ve sıkmanın yeniden başladığı bolluk yılı. Sıkmak burada darlığın sonunu işaret eder; sıkılacak üzüm, darlık yıllarını sabırla bekleyip saklayanların payıdır. Ayetin yemin ettiği zaman bu açıdan yalnızca tüketen bir süre değildir: içinde saklananın korunduğu ve sonunda sıkılıp akan bir süredir.

## Tutmak ve vermek

[¶14] Sıkmak bir kavrayıştır, ve kavrayış iki yöne işler: tutar ya da akıtır. Asr kelimesi tutmayı da adlandırır: {ar:العصر الحبس, tr:el-asru'l-habs, gloss:asr, alıkoymaktır, source:"ع ص ر,B006"}; birine seni ne alıkoydu diye sorulurken {ar:ما عصرك أي ما منعك, tr:mâ asarak, gloss:seni ne tuttu, ne engelledi, source:"ع ص ر,B006"} denirdi. Elinden bir şey bırakmayan, veremeyen kişi için {ar:فلان عاصر إذا كان ممسكا, tr:fulânun âsirun izâ kâne mumsikâ, gloss:eli sıkı olana âsir denir, source:"ع ص ر,B006"} derlerdi. Babanın, çocuğuna ait malı ondan tutması da bu fiille söylenir: {ar:يعتصر الوالد على ولده في ماله أي يمنعه إياه ويحبسه عنه, tr:ya'tasıru'l-vâlidu alâ veledihî fî mâlih, gloss:baba çocuğunun malını ondan esirger, alıkoyar, source:"ع ص ر,B006"}; verdiği bağıştan dönüp onu geri almak da: {ar:أعطيت فلانا عطية فاعتصرتها أي رجعت فيها, tr:a'taytu fulânen atıyyeten fa'tasartuhâ, gloss:birine bir bağış verdim, sonra ondan dönüp geri aldım, source:"ع ص ر,B006"}. Bir önceki bölümdeki cömert ise aynı kökle {source:"ع ص ر,B007"} verendi. Torba örneği bu ikiliği açıklar: sıkan el sıkıca kavrar; kavrayış sıvıyı dışarı akıtırsa bağış olur, kavrayış yalnızca tutarsa cimrilik olur. Aynı fiil hem el açıklığını hem el sıkılığını adlandırabilir, çünkü ikisi de bir şeyi avuçta sıkmaktır; fark, avuçtan bir şeyin çıkıp çıkmamasıdır.

[¶15] Tutmak her zaman kötü değildir. İlk aybaşı vaktinde evde tutulan genç kızın adı da buradan gelir: {ar:المعصر ساعة تطمث أي تحيض لأنها تحبس في البيت يجعل لها عصرا, tr:el-mu'sır, gloss:ilk aybaşı vaktindeki kız; evde tutulduğu, kendisine bir korunak yapıldığı için böyle denir, source:"ع ص ر,B009"}; kabuğunda saklanan tane de aynı korunağın içindedir {source:"ع ص ر,B010"}. Burada tutmak, bir eşikte olanı korumaktır.

[¶16] Kur'an ürünü tutmanın ne getirdiğini bir bahçe sahneleriyle anlatır. Peygamber'i yalanlayanlara, onları bir bahçenin sahipleri gibi sınadığını söyler: {ar:إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:innâ belevnâhum kemâ belevnâ ashâbe'l-cenneti iz aksemû le-yasrimunnehâ musbihîn, gloss:onları, sabah olunca bahçenin ürününü mutlaka devşireceklerine yemin eden bahçe sahiplerini sınadığımız gibi sınadık, source:68:17}, {ar:وَلَا يَسْتَثْنُونَ, tr:ve lâ yestesnûn, gloss:ve hiçbir istisna yapmıyorlardı, source:68:18}. Niyetleri, ürünü yoksula kapatmaktır: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya yanınıza hiçbir yoksul girmesin, source:68:24}. Onlar uyurken bahçenin üzerinden Rab'den gelen bir şey geçer {ar:فَطَافَ عَلَيْهَا طَآئِفٌۭ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uyurken Rabbinden bir dolaşan onun üzerinden dolaştı, source:68:19} ve bahçe kopkoyu bir yere döner {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kesilip kararmış gibi çıktı, source:68:20}. Gördüklerinde ilk sözleri {ar:إِنَّا لَضَآلُّونَ, tr:innâ le-dâllûn, gloss:biz yolu şaşırmışız, source:68:26}, ardından {ar:بَلْ نَحْنُ مَحْرُومُونَ, tr:bel nahnu mahrûmûn, gloss:hayır, biz yoksun bırakılmışız, source:68:27} olur. Tutulan ürün tutanın elinde kalmamıştır. Bu bahçe sahipleri istisnasız bir yemin etmişlerdi; surenin yemini ise ikinci ayetteki genel hükmün ardından üçüncü ayetin istisnasıyla tamamlanır.

## Sığınak

[¶17] Asrın sıkıştırma anlamının karşısında, şaşırtıcı biçimde, sığınak anlamı durur. Kök tutunmayı anlatır: {ar:تعلق بشيء وامتساك به, tr:teallukun bi-şey'in ve imtisâkun bih, gloss:bir şeye asılmak ve ona sıkıca tutunmak, source:"ع ص ر,B005"}. Tutunulan yerin adı da asrdır: {ar:العصر الملجأ, tr:el-asru'l-melce', gloss:asr, sığınaktır, source:"ع ص ر,B005"}; birine sığınan {ar:اعتصرت بفلان وتعصرت أي التجأت إليه, tr:i'tasartu bi-fulânin ve teassartu, gloss:falancaya sığındım, source:"ع ص ر,B005"} derdi, bir yere sığınan için de {ar:اعتصر بالمكان إذا التجأ إليه, tr:i'tasara bi'l-mekân, gloss:o yere sığındı, source:"ع ص ر,B005"} denirdi. Bir deyim bu sığınağı darda kalmış kişiye bağlar: {ar:عصرة المنجود, tr:usratu'l-mencûd, gloss:bunalmış, sıkışmış kişinin sığınağı, source:"ع ص ر,B005"}. İki insan arasındaki bağ da bu kelimeyle, olmayışıyla anılır: {ar:ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة, tr:mâ beynehumâ asrun ve lâ yasr, gloss:aralarında ne sevgi ne akrabalık var, source:"ع ص ر,B005"}. Kişinin soyu da dönüp sığındığı yerdir; köke {ar:العنصر والعنصر الأصل والحسب, tr:el-unsur, gloss:unsur, kök ve soydur, source:"ع ص ر,B011"} denir ve bu kelimenin aslının sığınak anlamındaki asr olduğu söylenir: {ar:العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ, tr:el-unsuru aslu'l-haseb, gloss:unsur soyun köküdür, ona bir nun eklenmiştir, aslı sığınak anlamındaki asrdır, source:"ع ص ر,B011"}. Savaşta insanı saran zırhlar da bu köktendir: {ar:المعاصر الدروع مأخوذ من العصر لأنه يعصر بها, tr:el-meâsiru'd-durû', gloss:meâsir zırhlardır; insan onlarla korunduğu için asrdan alınmıştır, source:"ع ص ر,B016"}.

[¶18] Aynı kelimenin hem sıkıştırmayı hem sığınağı adlandırması ilk bakışta çelişki gibi görünür, ama ikisi de bir kavrayıştır. Sıkma bir şeyi dışarıdan sarar; sığınan ise kendisi bir şeyi sıkıca kavrar, zırh da bedeni dışarıdan sarar ve korur. Sıkışmış olan, bunalmış olan sığınağa koşar: deyimdeki sığınak tam da bunalmış kişinin sığınağıdır. Bu imge zamanın yanında duyulunca yemin edilen vakit hem insanı sıkıştıran bir süre hem de sığınılacak bir yer olarak görünür.

[¶19] Kur'an bir sığınağın zamanı nasıl kapattığını bir mağara hikâyesinde gösterir. Allah Peygamber'e, kavimlerinin taptıklarından ayrılan birkaç gencin haberini anlatır; onlar birbirine şöyle der: {ar:وَإِذِ ٱعْتَزَلْتُمُوهُمْ وَمَا يَعْبُدُونَ إِلَّا ٱللَّهَ فَأْوُۥٓا۟ إِلَى ٱلْكَهْفِ يَنشُرْ لَكُمْ رَبُّكُم مِّن رَّحْمَتِهِۦ, tr:ve izi'tezeltumûhum ve mâ ya'budûne illallâhe fe'vû ile'l-kehfi yenşur lekum rabbukum min rahmetih, gloss:madem onlardan ve Allah'tan başka taptıklarından ayrıldınız, mağaraya sığının ki Rabbiniz rahmetinden size yaysın, source:18:16}. Sığındıklarında dua ederler: {ar:إِذْ أَوَى ٱلْفِتْيَةُ إِلَى ٱلْكَهْفِ فَقَالُوا۟ رَبَّنَآ ءَاتِنَا مِن لَّدُنكَ رَحْمَةًۭ, tr:iz eve'l-fityetu ile'l-kehfi fe-kâlû rabbenâ âtinâ min ledunke rahmeh, gloss:o gençler mağaraya sığınıp Rabbimiz, katından bize rahmet ver dediklerinde, source:18:10}. Sığınağın içinde zaman kapanır: {ar:فَضَرَبْنَا عَلَىٰٓ ءَاذَانِهِمْ فِى ٱلْكَهْفِ سِنِينَ عَدَدًۭا, tr:fe-darabnâ alâ âzânihim fi'l-kehfi sinîne adedâ, gloss:mağarada nice yıllar kulaklarının üstüne perde vurduk, source:18:11}. Uyandıklarında birbirlerine ne kadar kaldıklarını sorarlar ve cevapları {ar:لَبِثْنَا يَوْمًا أَوْ بَعْضَ يَوْمٍۢ, tr:lebisnâ yevmen ev ba'da yevm, gloss:bir gün ya da günün bir kısmı kaldık, source:18:19} olur; oysa {ar:وَلَبِثُوا۟ فِى كَهْفِهِمْ ثَلَٰثَ مِا۟ئَةٍۢ سِنِينَ وَٱزْدَادُوا۟ تِسْعًۭا, tr:ve lebisû fî kehfihim selâse mietin sinîne vezdâdû tis'â, gloss:mağaralarında üç yüz yıl kaldılar, dokuz da eklediler, source:18:25}. Bu hikâyede asrın üç yüzü bir arada görünür, ama kelimenin kendisi geçmez: sığınak, uzun bir çağ ve uyuyanın bir an sandığı süre. Üçüncü ayette istisna edilen iman edenler bu sığınak imgesine yaslanır; kayıptan kurtuluş, bu sahnede bir yere sığınmak olarak duyulur.

## Kasırga ve kokunun yükselişi

[¶20] Kökün bir dalı göğe yükselen bir rüzgârı adlandırır. Rüzgâr yerden eser, tozu kaldırır ve onu sütun gibi göğe diker: {ar:الإعصار ريح تهب تثير الغبار فيرتفع إلى السماء كأنه عمود, tr:el-i'sâru rîhun tehubbu tusîru'l-gubâra fe-yertefi'u ile's-semâi keennehû amûd, gloss:i'sâr, esip tozu kaldıran ve onu sütun gibi göğe yükselten rüzgârdır, source:"ع ص ر,B004"}; dönerek yükselen tozun kendisine de {ar:الإعصار الغبار الذي يسطع مستديرا والجمع الأعاصير, tr:el-i'sâru'l-gubâru'llezî yesta'u mustedîrâ, gloss:i'sâr, dönerek yükselen tozdur, çoğulu eâsîr, source:"ع ص ر,B004"} denir. Bu rüzgârın işi, yerdeki şeyi döndürerek bir araya toplamak ve onu dik bir sütun hâlinde yukarı çekmektir. Aynı dal hoş bir şeyi de böyle anlatır: güzel kokular sürünmüş bir kadın geçtiğinde {ar:مرت امرأة متطيبة لذيلها عصر, tr:merrat imraetun mutetayyibetun li-zeylihâ asr, gloss:güzel koku sürünmüş bir kadın geçti, eteğinin ardından koku yükseliyordu, source:"ع ص ر,B004"} derlerdi; {ar:تكون العصرة من فوح الطيب وهيجه, tr:tekûnu'l-usratu min fevhi't-tîbi ve heycih, gloss:usra, kokunun yayılıp kabarmasıdır, source:"ع ص ر,B004"}. Hareket eden bir şeyin ardından kabarıp yükselen ya tozdur ya kokudur.

[¶21] Kur'an bu rüzgârı, yaşlılığın içine yerleştirilmiş bir bahçe misalinde anar. Allah Allah yolunda harcamaya dair misaller verir: gösteriş için harcayanın hâli üzerinde toprak bulunan düz bir kayadır, sağanak vurunca çıplak kalır {ar:فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:fe-meseluhû ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:onun misali, üstünde toprak olan düz bir kaya gibidir; sağanak vurdu, onu çıplak bıraktı, source:2:264}; Allah'ın rızası için harcayanınki ise sağanak da çisenti de alsa iki kat ürün veren tepedeki bir bahçedir {source:2:265}. Sonra bir soru gelir: {ar:أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:e-yeveddu ehadukum en tekûne lehû cennetun min nahîlin ve a'nâbin tecrî min tahtihe'l-enhâr, gloss:biriniz, altından ırmaklar akan, hurmalık ve üzüm bağından bir bahçesi olmasını ister mi, source:2:266}; aynı ayette {ar:وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:ve esâbehu'l-kiberu ve lehû zurriyyetun duafâu fe-esâbehâ i'sârun fîhi nârun fahtarakat, gloss:kendisine yaşlılık çökmüş, zayıf çocukları varken, bahçeye içinde ateş olan bir kasırga isabet etsin de yansın, source:2:266}. Ayet kendi işini de söyler: {ar:كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ, tr:kezâlike yubeyyinullâhu lekumu'l-âyâti leallekum tetefekkerûn, gloss:Allah size ayetleri böyle açıklar ki düşünesiniz, source:2:266}.

[¶22] Bu bahçede kökün birkaç anlamı aynı yerde durur, ama kelime olarak yalnızca kasırga geçer. Bahçede üzüm vardır, yani sıkılacak meyve; ırmaklar ve bütün ürünler, yani gelir; sahibine yaşlılık gelmiştir, yani ömrün akşamüstü; ve bütün bunları, yerden kaldırdığını göğe diken, içinde ateş taşıyan bir rüzgâr yok eder. Bir ömür boyunca sıkılmayı bekleyen ürün, tam sahibinin yeniden ekecek gücü kalmadığı vakitte gider. İkinci ayetteki kaybın en somut resmi budur; kasırga, asrın yanında duyulduğunda zamanın biriktirdiğini bir anda savurabilen yüzüdür. Kokunun yükselişi ise aynı hareketin öteki ucunda durur: geçen birinin ardından toz değil, güzel bir iz kalabilir.

===== _commentary/v16/out/103_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: wa- here is the oath particle; al-ʿaṣr in genitive after it
- memory: yataḥallab evokes flowing as in milking (ḥ-l-b)
- memory: al-manjūd = one overwhelmed, in distress
- memory: the poem line implies water itself chokes him, no remedy left
- memory: yuʿṣar bihā in the armour phrase read as "protected by them"
- not written: B003 recorded rain reading of 12:49 - vowels not supplied, cannot quote safely
- not written: B011 karīm al-muʿṣir (generous when asked) - adds nothing beyond B007 giving
- not written: B012 lowly clients - rank contrast belongs to the surah scene, no theme in this ayah alone
- not written: B013 a tree - bare name, no work
- not written: B015 breaking wind - no theme
- not written: B016 turbans / black clothes - only the armour sense joins the refuge theme
- not written: 38:31-32 horses shown at ʿashī - the hidden referent is unclear in the text

===== passages not cited (212) =====
## strong (this ayah's own list) (26)

- (7:9) [listed for 103:1] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَظْلِمُونَ
- (12:49) [listed for 103:1] [cited in ¶12] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ
- (17:13) [listed for 103:1] وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا
- (17:14) [listed for 103:1] ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًۭا
- (18:49) [listed for 103:1] وَوُضِعَ ٱلْكِتَٰبُ فَتَرَى ٱلْمُجْرِمِينَ مُشْفِقِينَ مِمَّا فِيهِ وَيَقُولُونَ يَٰوَيْلَتَنَا مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا ۗ وَلَا يَظْلِمُ رَبُّكَ أَحَدًۭا
- (18:103) [listed for 103:1] قُلْ هَلْ نُنَبِّئُكُم بِٱلْأَخْسَرِينَ أَعْمَٰلًا
- (21:47) [listed for 103:1] وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ فَلَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا ۖ وَإِن كَانَ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ أَتَيْنَا بِهَا ۗ وَكَفَىٰ بِنَا حَٰسِبِينَ
- (22:11) [listed for 103:1] وَمِنَ ٱلنَّاسِ مَن يَعْبُدُ ٱللَّهَ عَلَىٰ حَرْفٍۢ ۖ فَإِنْ أَصَابَهُۥ خَيْرٌ ٱطْمَأَنَّ بِهِۦ ۖ وَإِنْ أَصَابَتْهُ فِتْنَةٌ ٱنقَلَبَ عَلَىٰ وَجْهِهِۦ خَسِرَ ٱلدُّنْيَا وَٱلْءَاخِرَةَ ۚ ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (23:102) [listed for 103:1] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (23:103) [listed for 103:1] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (36:12) [listed for 103:1] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
- (39:15) [listed for 103:1] فَٱعْبُدُوا۟ مَا شِئْتُم مِّن دُونِهِۦ ۗ قُلْ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَا ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (45:24) [listed for 103:1] وَقَالُوا۟ مَا هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا نَمُوتُ وَنَحْيَا وَمَا يُهْلِكُنَآ إِلَّا ٱلدَّهْرُ ۚ وَمَا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَظُنُّونَ
- (50:17) [listed for 103:1] إِذْ يَتَلَقَّى ٱلْمُتَلَقِّيَانِ عَنِ ٱلْيَمِينِ وَعَنِ ٱلشِّمَالِ قَعِيدٌۭ
- (50:18) [listed for 103:1] مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ
- (57:20) [listed for 103:1] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (63:9) [listed for 103:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (78:14) [listed for 103:1] [cited in ¶8] وَأَنزَلْنَا مِنَ ٱلْمُعْصِرَٰتِ مَآءًۭ ثَجَّاجًۭا
- (82:10) [listed for 103:1] وَإِنَّ عَلَيْكُمْ لَحَٰفِظِينَ
- (82:12) [listed for 103:1] يَعْلَمُونَ مَا تَفْعَلُونَ
- (99:7) [listed for 103:1] فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- (99:8) [listed for 103:1] وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
- (101:6) [listed for 103:1] فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- (101:8) [listed for 103:1] وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- (102:1) [listed for 103:1] أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
- (102:2) [listed for 103:1] حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ

## medium (this ayah's own list) (51)

- (2:164) [listed for 103:1] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (2:266) [listed for 103:1] [cited in ¶21] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (3:185) [listed for 103:1] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (3:190) [listed for 103:1] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
- (7:8) [listed for 103:1] وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (7:34) [listed for 103:1] وَلِكُلِّ أُمَّةٍ أَجَلٌۭ ۖ فَإِذَا جَآءَ أَجَلُهُمْ لَا يَسْتَأْخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
- (8:37) [listed for 103:1] لِيَمِيزَ ٱللَّهُ ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ وَيَجْعَلَ ٱلْخَبِيثَ بَعْضَهُۥ عَلَىٰ بَعْضٍۢ فَيَرْكُمَهُۥ جَمِيعًۭا فَيَجْعَلَهُۥ فِى جَهَنَّمَ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (10:24) [listed for 103:1] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
- (10:49) [listed for 103:1] قُل لَّآ أَمْلِكُ لِنَفْسِى ضَرًّۭا وَلَا نَفْعًا إِلَّا مَا شَآءَ ٱللَّهُ ۗ لِكُلِّ أُمَّةٍ أَجَلٌ ۚ إِذَا جَآءَ أَجَلُهُمْ فَلَا يَسْتَـْٔخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
- (10:103) [listed for 103:1] ثُمَّ نُنَجِّى رُسُلَنَا وَٱلَّذِينَ ءَامَنُوا۟ ۚ كَذَٰلِكَ حَقًّا عَلَيْنَا نُنجِ ٱلْمُؤْمِنِينَ
- (11:15) [listed for 103:1] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
- (11:16) [listed for 103:1] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
- (12:47) [listed for 103:1] [cited in ¶12] قَالَ تَزْرَعُونَ سَبْعَ سِنِينَ دَأَبًۭا فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ
- (14:18) [listed for 103:1] مَّثَلُ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ ۖ لَّا يَقْدِرُونَ مِمَّا كَسَبُوا۟ عَلَىٰ شَىْءٍۢ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
- (14:52) [listed for 103:1] هَٰذَا بَلَٰغٌۭ لِّلنَّاسِ وَلِيُنذَرُوا۟ بِهِۦ وَلِيَعْلَمُوٓا۟ أَنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ وَلِيَذَّكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (16:61) [listed for 103:1] وَلَوْ يُؤَاخِذُ ٱللَّهُ ٱلنَّاسَ بِظُلْمِهِم مَّا تَرَكَ عَلَيْهَا مِن دَآبَّةٍۢ وَلَٰكِن يُؤَخِّرُهُمْ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ۖ فَإِذَا جَآءَ أَجَلُهُمْ لَا يَسْتَـْٔخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
- (19:96) [listed for 103:1] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَيَجْعَلُ لَهُمُ ٱلرَّحْمَٰنُ وُدًّۭا
- (21:35) [listed for 103:1] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ ۖ وَإِلَيْنَا تُرْجَعُونَ
- (25:62) [listed for 103:1] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (33:72) [listed for 103:1] إِنَّا عَرَضْنَا ٱلْأَمَانَةَ عَلَى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلْجِبَالِ فَأَبَيْنَ أَن يَحْمِلْنَهَا وَأَشْفَقْنَ مِنْهَا وَحَمَلَهَا ٱلْإِنسَٰنُ ۖ إِنَّهُۥ كَانَ ظَلُومًۭا جَهُولًۭا
- (35:18) [listed for 103:1] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (39:5) [listed for 103:1] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ يُكَوِّرُ ٱلَّيْلَ عَلَى ٱلنَّهَارِ وَيُكَوِّرُ ٱلنَّهَارَ عَلَى ٱلَّيْلِ ۖ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّى ۗ أَلَا هُوَ ٱلْعَزِيزُ ٱلْغَفَّٰرُ
- (49:7) [listed for 103:1] وَٱعْلَمُوٓا۟ أَنَّ فِيكُمْ رَسُولَ ٱللَّهِ ۚ لَوْ يُطِيعُكُمْ فِى كَثِيرٍۢ مِّنَ ٱلْأَمْرِ لَعَنِتُّمْ وَلَٰكِنَّ ٱللَّهَ حَبَّبَ إِلَيْكُمُ ٱلْإِيمَٰنَ وَزَيَّنَهُۥ فِى قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ ٱلْكُفْرَ وَٱلْفُسُوقَ وَٱلْعِصْيَانَ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلرَّٰشِدُونَ
- (50:43) [listed for 103:1] إِنَّا نَحْنُ نُحْىِۦ وَنُمِيتُ وَإِلَيْنَا ٱلْمَصِيرُ
- (51:56) [listed for 103:1] وَمَا خَلَقْتُ ٱلْجِنَّ وَٱلْإِنسَ إِلَّا لِيَعْبُدُونِ
- (59:18) [listed for 103:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (62:8) [listed for 103:1] قُلْ إِنَّ ٱلْمَوْتَ ٱلَّذِى تَفِرُّونَ مِنْهُ فَإِنَّهُۥ مُلَٰقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (64:9) [listed for 103:1] يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (70:22) [listed for 103:1] إِلَّا ٱلْمُصَلِّينَ
- (74:38) [listed for 103:1] كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ
- (75:13) [listed for 103:1] يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ
- (75:14) [listed for 103:1] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
- (76:1) [listed for 103:1] هَلْ أَتَىٰ عَلَى ٱلْإِنسَٰنِ حِينٌۭ مِّنَ ٱلدَّهْرِ لَمْ يَكُن شَيْـًۭٔا مَّذْكُورًا
- (77:13) [listed for 103:1] لِيَوْمِ ٱلْفَصْلِ
- (78:11) [listed for 103:1] وَجَعَلْنَا ٱلنَّهَارَ مَعَاشًۭا
- (78:15) [listed for 103:1] [cited in ¶8] لِّنُخْرِجَ بِهِۦ حَبًّۭا وَنَبَاتًۭا
- (79:46) [listed for 103:1] [cited in ¶6] كَأَنَّهُمْ يَوْمَ يَرَوْنَهَا لَمْ يَلْبَثُوٓا۟ إِلَّا عَشِيَّةً أَوْ ضُحَىٰهَا
- (82:11) [listed for 103:1] كِرَامًۭا كَٰتِبِينَ
- (87:16) [listed for 103:1] بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (87:17) [listed for 103:1] وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- (89:1) [listed for 103:1] [cited in ¶2] وَٱلْفَجْرِ
- (90:4) [listed for 103:1] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- (90:17) [listed for 103:1] ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- (91:1) [listed for 103:1] وَٱلشَّمْسِ وَضُحَىٰهَا
- (92:4) [listed for 103:1] إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- (92:5) [listed for 103:1] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (92:6) [listed for 103:1] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:8) [listed for 103:1] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- (93:1) [listed for 103:1] [cited in ¶2] وَٱلضُّحَىٰ
- (94:5) [listed for 103:1] فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- (94:6) [listed for 103:1] إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا

## named by the passage's own list as medium for this ayah (6)

- (56:75) [listed for 103:1] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (56:76) [listed for 103:1] وَإِنَّهُۥ لَقَسَمٌۭ لَّوْ تَعْلَمُونَ عَظِيمٌ
- (77:2) [listed for 103:1] فَٱلْعَٰصِفَٰتِ عَصْفًۭا
- (81:15) [listed for 103:1] فَلَآ أُقْسِمُ بِٱلْخُنَّسِ
- (89:3) [listed for 103:1] وَٱلشَّفْعِ وَٱلْوَتْرِ
- (95:1) [listed for 103:1] وَٱلتِّينِ وَٱلزَّيْتُونِ

## weak (this ayah's own list) (57)

- (2:187) [listed for 103:1] أُحِلَّ لَكُمْ لَيْلَةَ ٱلصِّيَامِ ٱلرَّفَثُ إِلَىٰ نِسَآئِكُمْ ۚ هُنَّ لِبَاسٌۭ لَّكُمْ وَأَنتُمْ لِبَاسٌۭ لَّهُنَّ ۗ عَلِمَ ٱللَّهُ أَنَّكُمْ كُنتُمْ تَخْتَانُونَ أَنفُسَكُمْ فَتَابَ عَلَيْكُمْ وَعَفَا عَنكُمْ ۖ فَٱلْـَٰٔنَ بَٰشِرُوهُنَّ وَٱبْتَغُوا۟ مَا كَتَبَ ٱللَّهُ لَكُمْ ۚ وَكُلُوا۟ وَٱشْرَبُوا۟ حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ ۖ ثُمَّ أَتِمُّوا۟ ٱلصِّيَامَ إِلَى ٱلَّيْلِ ۚ وَلَا تُبَٰشِرُوهُنَّ وَأَنتُمْ عَٰكِفُونَ فِى ٱلْمَسَٰجِدِ ۗ تِلْكَ حُدُودُ ٱللَّهِ فَلَا تَقْرَبُوهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَّقُونَ
- (2:196) [listed for 103:1] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (2:246) [listed for 103:1] أَلَمْ تَرَ إِلَى ٱلْمَلَإِ مِنۢ بَنِىٓ إِسْرَٰٓءِيلَ مِنۢ بَعْدِ مُوسَىٰٓ إِذْ قَالُوا۟ لِنَبِىٍّۢ لَّهُمُ ٱبْعَثْ لَنَا مَلِكًۭا نُّقَٰتِلْ فِى سَبِيلِ ٱللَّهِ ۖ قَالَ هَلْ عَسَيْتُمْ إِن كُتِبَ عَلَيْكُمُ ٱلْقِتَالُ أَلَّا تُقَٰتِلُوا۟ ۖ قَالُوا۟ وَمَا لَنَآ أَلَّا نُقَٰتِلَ فِى سَبِيلِ ٱللَّهِ وَقَدْ أُخْرِجْنَا مِن دِيَٰرِنَا وَأَبْنَآئِنَا ۖ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ تَوَلَّوْا۟ إِلَّا قَلِيلًۭا مِّنْهُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِٱلظَّٰلِمِينَ
- (4:12) [listed for 103:1] ۞ وَلَكُمْ نِصْفُ مَا تَرَكَ أَزْوَٰجُكُمْ إِن لَّمْ يَكُن لَّهُنَّ وَلَدٌۭ ۚ فَإِن كَانَ لَهُنَّ وَلَدٌۭ فَلَكُمُ ٱلرُّبُعُ مِمَّا تَرَكْنَ ۚ مِنۢ بَعْدِ وَصِيَّةٍۢ يُوصِينَ بِهَآ أَوْ دَيْنٍۢ ۚ وَلَهُنَّ ٱلرُّبُعُ مِمَّا تَرَكْتُمْ إِن لَّمْ يَكُن لَّكُمْ وَلَدٌۭ ۚ فَإِن كَانَ لَكُمْ وَلَدٌۭ فَلَهُنَّ ٱلثُّمُنُ مِمَّا تَرَكْتُم ۚ مِّنۢ بَعْدِ وَصِيَّةٍۢ تُوصُونَ بِهَآ أَوْ دَيْنٍۢ ۗ وَإِن كَانَ رَجُلٌۭ يُورَثُ كَلَٰلَةً أَوِ ٱمْرَأَةٌۭ وَلَهُۥٓ أَخٌ أَوْ أُخْتٌۭ فَلِكُلِّ وَٰحِدٍۢ مِّنْهُمَا ٱلسُّدُسُ ۚ فَإِن كَانُوٓا۟ أَكْثَرَ مِن ذَٰلِكَ فَهُمْ شُرَكَآءُ فِى ٱلثُّلُثِ ۚ مِنۢ بَعْدِ وَصِيَّةٍۢ يُوصَىٰ بِهَآ أَوْ دَيْنٍ غَيْرَ مُضَآرٍّۢ ۚ وَصِيَّةًۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ عَلِيمٌ حَلِيمٌۭ
- (11:90) [listed for 103:1] وَٱسْتَغْفِرُوا۟ رَبَّكُمْ ثُمَّ تُوبُوٓا۟ إِلَيْهِ ۚ إِنَّ رَبِّى رَحِيمٌۭ وَدُودٌۭ
- (12:36) [listed for 103:1] [cited in ¶11] وَدَخَلَ مَعَهُ ٱلسِّجْنَ فَتَيَانِ ۖ قَالَ أَحَدُهُمَآ إِنِّىٓ أَرَىٰنِىٓ أَعْصِرُ خَمْرًۭا ۖ وَقَالَ ٱلْءَاخَرُ إِنِّىٓ أَرَىٰنِىٓ أَحْمِلُ فَوْقَ رَأْسِى خُبْزًۭا تَأْكُلُ ٱلطَّيْرُ مِنْهُ ۖ نَبِّئْنَا بِتَأْوِيلِهِۦٓ ۖ إِنَّا نَرَىٰكَ مِنَ ٱلْمُحْسِنِينَ
- (20:31) [listed for 103:1] ٱشْدُدْ بِهِۦٓ أَزْرِى
- (26:152) [listed for 103:1] ٱلَّذِينَ يُفْسِدُونَ فِى ٱلْأَرْضِ وَلَا يُصْلِحُونَ
- (35:21) [listed for 103:1] وَلَا ٱلظِّلُّ وَلَا ٱلْحَرُورُ
- (37:1) [listed for 103:1] وَٱلصَّٰٓفَّٰتِ صَفًّۭا
- (43:2) [listed for 103:1] وَٱلْكِتَٰبِ ٱلْمُبِينِ
- (44:2) [listed for 103:1] وَٱلْكِتَٰبِ ٱلْمُبِينِ
- (51:1) [listed for 103:1] وَٱلذَّٰرِيَٰتِ ذَرْوًۭا
- (52:1) [listed for 103:1] وَٱلطُّورِ
- (52:4) [listed for 103:1] وَٱلْبَيْتِ ٱلْمَعْمُورِ
- (52:5) [listed for 103:1] وَٱلسَّقْفِ ٱلْمَرْفُوعِ
- (52:6) [listed for 103:1] وَٱلْبَحْرِ ٱلْمَسْجُورِ
- (54:18) [listed for 103:1] كَذَّبَتْ عَادٌۭ فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:21) [listed for 103:1] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (54:30) [listed for 103:1] فَكَيْفَ كَانَ عَذَابِى وَنُذُرِ
- (55:12) [listed for 103:1] وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ
- (56:10) [listed for 103:1] وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ
- (56:38) [listed for 103:1] لِّأَصْحَٰبِ ٱلْيَمِينِ
- (63:1) [listed for 103:1] إِذَا جَآءَكَ ٱلْمُنَٰفِقُونَ قَالُوا۟ نَشْهَدُ إِنَّكَ لَرَسُولُ ٱللَّهِ ۗ وَٱللَّهُ يَعْلَمُ إِنَّكَ لَرَسُولُهُۥ وَٱللَّهُ يَشْهَدُ إِنَّ ٱلْمُنَٰفِقِينَ لَكَٰذِبُونَ
- (68:16) [listed for 103:1] سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ
- (69:1) [listed for 103:1] ٱلْحَآقَّةُ
- (70:9) [listed for 103:1] وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ
- (74:5) [listed for 103:1] وَٱلرُّجْزَ فَٱهْجُرْ
- (74:18) [listed for 103:1] إِنَّهُۥ فَكَّرَ وَقَدَّرَ
- (74:23) [listed for 103:1] ثُمَّ أَدْبَرَ وَٱسْتَكْبَرَ
- (74:32) [listed for 103:1] كَلَّا وَٱلْقَمَرِ
- (74:41) [listed for 103:1] عَنِ ٱلْمُجْرِمِينَ
- (75:8) [listed for 103:1] وَخَسَفَ ٱلْقَمَرُ
- (75:9) [listed for 103:1] وَجُمِعَ ٱلشَّمْسُ وَٱلْقَمَرُ
- (75:29) [listed for 103:1] وَٱلْتَفَّتِ ٱلسَّاقُ بِٱلسَّاقِ
- (78:3) [listed for 103:1] ٱلَّذِى هُمْ فِيهِ مُخْتَلِفُونَ
- (78:7) [listed for 103:1] وَٱلْجِبَالَ أَوْتَادًۭا
- (78:12) [listed for 103:1] وَبَنَيْنَا فَوْقَكُمْ سَبْعًۭا شِدَادًۭا
- (79:1) [listed for 103:1] وَٱلنَّٰزِعَٰتِ غَرْقًۭا
- (79:2) [listed for 103:1] وَٱلنَّٰشِطَٰتِ نَشْطًۭا
- (79:3) [listed for 103:1] وَٱلسَّٰبِحَٰتِ سَبْحًۭا
- (79:4) [listed for 103:1] فَٱلسَّٰبِقَٰتِ سَبْقًۭا
- (80:35) [listed for 103:1] وَأُمِّهِۦ وَأَبِيهِ
- (80:36) [listed for 103:1] وَصَٰحِبَتِهِۦ وَبَنِيهِ
- (81:16) [listed for 103:1] ٱلْجَوَارِ ٱلْكُنَّسِ
- (85:2) [listed for 103:1] وَٱلْيَوْمِ ٱلْمَوْعُودِ
- (86:1) [listed for 103:1] وَٱلسَّمَآءِ وَٱلطَّارِقِ
- (87:3) [listed for 103:1] وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- (90:13) [listed for 103:1] فَكُّ رَقَبَةٍ
- (92:17) [listed for 103:1] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- (92:21) [listed for 103:1] وَلَسَوْفَ يَرْضَىٰ
- (96:18) [listed for 103:1] سَنَدْعُ ٱلزَّبَانِيَةَ
- (99:3) [listed for 103:1] وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- (100:1) [listed for 103:1] وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- (101:1) [listed for 103:1] ٱلْقَارِعَةُ
- (101:2) [listed for 103:1] مَا ٱلْقَارِعَةُ
- (107:7) [listed for 103:1] وَيَمْنَعُونَ ٱلْمَاعُونَ

## named by the passage's own list as weak for this ayah (7)

- (10:5) [listed for 103:1] هُوَ ٱلَّذِى جَعَلَ ٱلشَّمْسَ ضِيَآءًۭ وَٱلْقَمَرَ نُورًۭا وَقَدَّرَهُۥ مَنَازِلَ لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ ۚ مَا خَلَقَ ٱللَّهُ ذَٰلِكَ إِلَّا بِٱلْحَقِّ ۚ يُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (69:38) [listed for 103:1] فَلَآ أُقْسِمُ بِمَا تُبْصِرُونَ
- (73:3) [listed for 103:1] نِّصْفَهُۥٓ أَوِ ٱنقُصْ مِنْهُ قَلِيلًا
- (79:34) [listed for 103:1] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (85:3) [listed for 103:1] وَشَاهِدٍۢ وَمَشْهُودٍۢ
- (89:2) [listed for 103:1] وَلَيَالٍ عَشْرٍۢ
- (106:2) [listed for 103:1] إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ

## neighbours: within two ayat of a passage the commentary cites (65)

- (2:262) [next to 2:264] ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى ۙ لَّهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:263) [next to 2:264] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
- (2:267) [next to 2:265] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
- (2:268) [next to 2:266] ٱلشَّيْطَٰنُ يَعِدُكُمُ ٱلْفَقْرَ وَيَأْمُرُكُم بِٱلْفَحْشَآءِ ۖ وَٱللَّهُ يَعِدُكُم مَّغْفِرَةًۭ مِّنْهُ وَفَضْلًۭا ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (6:50) [next to 6:52] قُل لَّآ أَقُولُ لَكُمْ عِندِى خَزَآئِنُ ٱللَّهِ وَلَآ أَعْلَمُ ٱلْغَيْبَ وَلَآ أَقُولُ لَكُمْ إِنِّى مَلَكٌ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ ۚ أَفَلَا تَتَفَكَّرُونَ
- (6:51) [next to 6:52] وَأَنذِرْ بِهِ ٱلَّذِينَ يَخَافُونَ أَن يُحْشَرُوٓا۟ إِلَىٰ رَبِّهِمْ ۙ لَيْسَ لَهُم مِّن دُونِهِۦ وَلِىٌّۭ وَلَا شَفِيعٌۭ لَّعَلَّهُمْ يَتَّقُونَ
- (6:53) [next to 6:52] وَكَذَٰلِكَ فَتَنَّا بَعْضَهُم بِبَعْضٍۢ لِّيَقُولُوٓا۟ أَهَٰٓؤُلَآءِ مَنَّ ٱللَّهُ عَلَيْهِم مِّنۢ بَيْنِنَآ ۗ أَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِٱلشَّٰكِرِينَ
- (6:54) [next to 6:52] وَإِذَا جَآءَكَ ٱلَّذِينَ يُؤْمِنُونَ بِـَٔايَٰتِنَا فَقُلْ سَلَٰمٌ عَلَيْكُمْ ۖ كَتَبَ رَبُّكُمْ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۖ أَنَّهُۥ مَنْ عَمِلَ مِنكُمْ سُوٓءًۢا بِجَهَٰلَةٍۢ ثُمَّ تَابَ مِنۢ بَعْدِهِۦ وَأَصْلَحَ فَأَنَّهُۥ غَفُورٌۭ رَّحِيمٌۭ
- (11:112) [next to 11:114] فَٱسْتَقِمْ كَمَآ أُمِرْتَ وَمَن تَابَ مَعَكَ وَلَا تَطْغَوْا۟ ۚ إِنَّهُۥ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (11:113) [next to 11:114] وَلَا تَرْكَنُوٓا۟ إِلَى ٱلَّذِينَ ظَلَمُوا۟ فَتَمَسَّكُمُ ٱلنَّارُ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِنْ أَوْلِيَآءَ ثُمَّ لَا تُنصَرُونَ
- (11:115) [next to 11:114] وَٱصْبِرْ فَإِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
- (11:116) [next to 11:114] فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ إِلَّا قَلِيلًۭا مِّمَّنْ أَنجَيْنَا مِنْهُمْ ۗ وَٱتَّبَعَ ٱلَّذِينَ ظَلَمُوا۟ مَآ أُتْرِفُوا۟ فِيهِ وَكَانُوا۟ مُجْرِمِينَ
- (12:33) [next to 12:35] قَالَ رَبِّ ٱلسِّجْنُ أَحَبُّ إِلَىَّ مِمَّا يَدْعُونَنِىٓ إِلَيْهِ ۖ وَإِلَّا تَصْرِفْ عَنِّى كَيْدَهُنَّ أَصْبُ إِلَيْهِنَّ وَأَكُن مِّنَ ٱلْجَٰهِلِينَ
- (12:34) [next to 12:35] فَٱسْتَجَابَ لَهُۥ رَبُّهُۥ فَصَرَفَ عَنْهُ كَيْدَهُنَّ ۚ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (12:37) [next to 12:35] قَالَ لَا يَأْتِيكُمَا طَعَامٌۭ تُرْزَقَانِهِۦٓ إِلَّا نَبَّأْتُكُمَا بِتَأْوِيلِهِۦ قَبْلَ أَن يَأْتِيَكُمَا ۚ ذَٰلِكُمَا مِمَّا عَلَّمَنِى رَبِّىٓ ۚ إِنِّى تَرَكْتُ مِلَّةَ قَوْمٍۢ لَّا يُؤْمِنُونَ بِٱللَّهِ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (12:38) [next to 12:36] وَٱتَّبَعْتُ مِلَّةَ ءَابَآءِىٓ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ ۚ مَا كَانَ لَنَآ أَن نُّشْرِكَ بِٱللَّهِ مِن شَىْءٍۢ ۚ ذَٰلِكَ مِن فَضْلِ ٱللَّهِ عَلَيْنَا وَعَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (12:39) [next to 12:41] يَٰصَىٰحِبَىِ ٱلسِّجْنِ ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
- (12:40) [next to 12:41] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (12:44) [next to 12:42] قَالُوٓا۟ أَضْغَٰثُ أَحْلَٰمٍۢ ۖ وَمَا نَحْنُ بِتَأْوِيلِ ٱلْأَحْلَٰمِ بِعَٰلِمِينَ
- (12:46) [next to 12:45] يُوسُفُ أَيُّهَا ٱلصِّدِّيقُ أَفْتِنَا فِى سَبْعِ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعِ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ لَّعَلِّىٓ أَرْجِعُ إِلَى ٱلنَّاسِ لَعَلَّهُمْ يَعْلَمُونَ
- (12:50) [next to 12:48] وَقَالَ ٱلْمَلِكُ ٱئْتُونِى بِهِۦ ۖ فَلَمَّا جَآءَهُ ٱلرَّسُولُ قَالَ ٱرْجِعْ إِلَىٰ رَبِّكَ فَسْـَٔلْهُ مَا بَالُ ٱلنِّسْوَةِ ٱلَّٰتِى قَطَّعْنَ أَيْدِيَهُنَّ ۚ إِنَّ رَبِّى بِكَيْدِهِنَّ عَلِيمٌۭ
- (12:51) [next to 12:49] قَالَ مَا خَطْبُكُنَّ إِذْ رَٰوَدتُّنَّ يُوسُفَ عَن نَّفْسِهِۦ ۚ قُلْنَ حَٰشَ لِلَّهِ مَا عَلِمْنَا عَلَيْهِ مِن سُوٓءٍۢ ۚ قَالَتِ ٱمْرَأَتُ ٱلْعَزِيزِ ٱلْـَٰٔنَ حَصْحَصَ ٱلْحَقُّ أَنَا۠ رَٰوَدتُّهُۥ عَن نَّفْسِهِۦ وَإِنَّهُۥ لَمِنَ ٱلصَّٰدِقِينَ
- (18:8) [next to 18:10] وَإِنَّا لَجَٰعِلُونَ مَا عَلَيْهَا صَعِيدًۭا جُرُزًا
- (18:9) [next to 18:10] أَمْ حَسِبْتَ أَنَّ أَصْحَٰبَ ٱلْكَهْفِ وَٱلرَّقِيمِ كَانُوا۟ مِنْ ءَايَٰتِنَا عَجَبًا
- (18:12) [next to 18:10] ثُمَّ بَعَثْنَٰهُمْ لِنَعْلَمَ أَىُّ ٱلْحِزْبَيْنِ أَحْصَىٰ لِمَا لَبِثُوٓا۟ أَمَدًۭا
- (18:13) [next to 18:11] نَّحْنُ نَقُصُّ عَلَيْكَ نَبَأَهُم بِٱلْحَقِّ ۚ إِنَّهُمْ فِتْيَةٌ ءَامَنُوا۟ بِرَبِّهِمْ وَزِدْنَٰهُمْ هُدًۭى
- (18:14) [next to 18:16] وَرَبَطْنَا عَلَىٰ قُلُوبِهِمْ إِذْ قَامُوا۟ فَقَالُوا۟ رَبُّنَا رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ لَن نَّدْعُوَا۟ مِن دُونِهِۦٓ إِلَٰهًۭا ۖ لَّقَدْ قُلْنَآ إِذًۭا شَطَطًا
- (18:15) [next to 18:16] هَٰٓؤُلَآءِ قَوْمُنَا ٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ ۖ لَّوْلَا يَأْتُونَ عَلَيْهِم بِسُلْطَٰنٍۭ بَيِّنٍۢ ۖ فَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًۭا
- (18:17) [next to 18:16] ۞ وَتَرَى ٱلشَّمْسَ إِذَا طَلَعَت تَّزَٰوَرُ عَن كَهْفِهِمْ ذَاتَ ٱلْيَمِينِ وَإِذَا غَرَبَت تَّقْرِضُهُمْ ذَاتَ ٱلشِّمَالِ وَهُمْ فِى فَجْوَةٍۢ مِّنْهُ ۚ ذَٰلِكَ مِنْ ءَايَٰتِ ٱللَّهِ ۗ مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِ ۖ وَمَن يُضْلِلْ فَلَن تَجِدَ لَهُۥ وَلِيًّۭا مُّرْشِدًۭا
- (18:18) [next to 18:16] وَتَحْسَبُهُمْ أَيْقَاظًۭا وَهُمْ رُقُودٌۭ ۚ وَنُقَلِّبُهُمْ ذَاتَ ٱلْيَمِينِ وَذَاتَ ٱلشِّمَالِ ۖ وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ ۚ لَوِ ٱطَّلَعْتَ عَلَيْهِمْ لَوَلَّيْتَ مِنْهُمْ فِرَارًۭا وَلَمُلِئْتَ مِنْهُمْ رُعْبًۭا
- (18:20) [next to 18:19] إِنَّهُمْ إِن يَظْهَرُوا۟ عَلَيْكُمْ يَرْجُمُوكُمْ أَوْ يُعِيدُوكُمْ فِى مِلَّتِهِمْ وَلَن تُفْلِحُوٓا۟ إِذًا أَبَدًۭا
- (18:21) [next to 18:19] وَكَذَٰلِكَ أَعْثَرْنَا عَلَيْهِمْ لِيَعْلَمُوٓا۟ أَنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَأَنَّ ٱلسَّاعَةَ لَا رَيْبَ فِيهَآ إِذْ يَتَنَٰزَعُونَ بَيْنَهُمْ أَمْرَهُمْ ۖ فَقَالُوا۟ ٱبْنُوا۟ عَلَيْهِم بُنْيَٰنًۭا ۖ رَّبُّهُمْ أَعْلَمُ بِهِمْ ۚ قَالَ ٱلَّذِينَ غَلَبُوا۟ عَلَىٰٓ أَمْرِهِمْ لَنَتَّخِذَنَّ عَلَيْهِم مَّسْجِدًۭا
- (18:23) [next to 18:25] وَلَا تَقُولَنَّ لِشَا۟ىْءٍ إِنِّى فَاعِلٌۭ ذَٰلِكَ غَدًا
- (18:24) [next to 18:25] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (18:26) [next to 18:25] قُلِ ٱللَّهُ أَعْلَمُ بِمَا لَبِثُوا۟ ۖ لَهُۥ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَبْصِرْ بِهِۦ وَأَسْمِعْ ۚ مَا لَهُم مِّن دُونِهِۦ مِن وَلِىٍّۢ وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا
- (18:27) [next to 18:25] وَٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِن كِتَابِ رَبِّكَ ۖ لَا مُبَدِّلَ لِكَلِمَٰتِهِۦ وَلَن تَجِدَ مِن دُونِهِۦ مُلْتَحَدًۭا
- (35:35) [next to 35:37] ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ
- (35:36) [next to 35:37] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (35:38) [next to 35:37] إِنَّ ٱللَّهَ عَٰلِمُ غَيْبِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (35:39) [next to 35:37] هُوَ ٱلَّذِى جَعَلَكُمْ خَلَٰٓئِفَ فِى ٱلْأَرْضِ ۚ فَمَن كَفَرَ فَعَلَيْهِ كُفْرُهُۥ ۖ وَلَا يَزِيدُ ٱلْكَٰفِرِينَ كُفْرُهُمْ عِندَ رَبِّهِمْ إِلَّا مَقْتًۭا ۖ وَلَا يَزِيدُ ٱلْكَٰفِرِينَ كُفْرُهُمْ إِلَّا خَسَارًۭا
- (68:15) [next to 68:17] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (68:21) [next to 68:19] فَتَنَادَوْا۟ مُصْبِحِينَ
- (68:22) [next to 68:20] أَنِ ٱغْدُوا۟ عَلَىٰ حَرْثِكُمْ إِن كُنتُمْ صَٰرِمِينَ
- (68:23) [next to 68:24] فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ
- (68:25) [next to 68:24] وَغَدَوْا۟ عَلَىٰ حَرْدٍۢ قَٰدِرِينَ
- (68:28) [next to 68:26] قَالَ أَوْسَطُهُمْ أَلَمْ أَقُل لَّكُمْ لَوْلَا تُسَبِّحُونَ
- (68:29) [next to 68:27] قَالُوا۟ سُبْحَٰنَ رَبِّنَآ إِنَّا كُنَّا ظَٰلِمِينَ
- (74:33) [next to 74:34] وَٱلَّيْلِ إِذْ أَدْبَرَ
- (74:35) [next to 74:34] إِنَّهَا لَإِحْدَى ٱلْكُبَرِ
- (74:36) [next to 74:34] نَذِيرًۭا لِّلْبَشَرِ
- (78:13) [next to 78:14] وَجَعَلْنَا سِرَاجًۭا وَهَّاجًۭا
- (78:17) [next to 78:15] إِنَّ يَوْمَ ٱلْفَصْلِ كَانَ مِيقَٰتًۭا
- (78:18) [next to 78:16] يَوْمَ يُنفَخُ فِى ٱلصُّورِ فَتَأْتُونَ أَفْوَاجًۭا
- (79:40) [next to 79:42] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
- (79:41) [next to 79:42] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- (79:43) [next to 79:42] فِيمَ أَنتَ مِن ذِكْرَىٰهَآ
- (79:44) [next to 79:42] إِلَىٰ رَبِّكَ مُنتَهَىٰهَآ
- (79:45) [next to 79:46] إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
- (89:0) [next to 89:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (92:0) [next to 92:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (92:2) [next to 92:1] وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- (92:3) [next to 92:1] وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- (93:0) [next to 93:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (93:2) [next to 93:1] وَٱلَّيْلِ إِذَا سَجَىٰ
- (93:3) [next to 93:1] مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ

