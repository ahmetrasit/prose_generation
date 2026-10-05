Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 6 of 11 ("Yetiştiren Rab, kesilen şükür, bitirmeyen toprak"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 6 (prose paragraphs numbered) =====
[¶27] Altıncı ayet yeminin cevabıdır: {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li-rabbihî le-kenûd, gloss:şüphesiz insan Rabbine karşı pek nankördür, source:100:6}. Cümlede "Rabbine" kelimesi nitelikten önce gelir. Böylece nankörlüğün kime karşı olduğu, nankörlüğün kendisinden önce duyulur. "Rab" kelimesi önce sahibi adlandırır: {ar:ورب كل شيء مالكه, tr:ve rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}. Aynı kelime sözü dinlenen efendiyi ve bir şeyi düzeltip iyileştireni de anlatır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح, tr:yekûnu'r-rabbu'l-mâlik, ve yekûnu'r-rabbu's-seyyide'l-mutâ', ve yekûnu'r-rabbu'l-muslih, gloss:rab sahip olur, itaat edilen efendi olur, ıslah eden olur, source:"ر ب ب,B001"}. Kökün işleyişi bir yetiştirmedir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}. Verilen bir iyilik de bu kökle tamamlanır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-raculu'n-ni'mete yerubbuhâ rabben ve rabâbeten izâ temmemehâ, gloss:adam bir nimeti tamamladığında "rabbe" denir, source:"ر ب ب,B002"}. Kökün ailesinde bir bulut da vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâbu's-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:"rabâb" buluttur; bitkiyi yetiştirdiği için bu adı almıştır, source:"ر ب ب,B008"}. Bir yerde toplanan bol su da aynı köktendir: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab, ve huve'l-mâu'l-kesîr, summiye bi-zâlike li-ictimâ'ih, gloss:"rabab" bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}.

[¶28] "Kenûd" kelimesi bu bakıma verilen karşılığı bir ip görüntüsüyle anlatır: {ar:كند الحبل يكنده كندا, tr:kenede'l-hable yeknuduhû kenden, gloss:ipi kesti, source:"ك ن د,B001"}. Şükrün kesilmesi de bu kelimeyle söylenir: {ar:يكند الشكر أي يقطعه, tr:yeknudu'ş-şukra, ey yakta'uh, gloss:şükrü "kened" eder, yani keser, source:"ك ن د,B001"}. Veren ile alan arasında bir ip uzanır. İyilik o ipten bir yöne akar, şükür öbür yöne döner. Kenûd olan kişi ipi kendi ucundan keser. Kelime bu kesişin nasıl işlediğini de anlatır: {ar:الكنود الكفور للنعمة, tr:el-kenûdu'l-kefûru li'n-ni'me, gloss:kenûd, nimete nankörlük edendir, source:"ك ن د,B002"}. Kenûd olan kişi {ar:يعد المصائب وينسى النعم, tr:ye'uddu'l-mesâibe ve yense'n-ni'am, gloss:musibetleri sayar, nimetleri unutur, source:"ك ن د,B002"}. Kelime bağı sürdürmemeyi de adlandırır: {ar:امرأة كند وكنود أي كفور للمواصلة, tr:imraetun kundun ve kenûd, ey kefûrun li'l-muvâsala, gloss:"kund" ya da "kenûd" kadın, yakınlığa nankörlük eden, bağı sürdürmeyendir, source:"ك ن د,B002"}. Kelimenin topraktaki karşılığı ise şudur: {ar:أرض كنود لا تنبت شيئا, tr:ardun kenûdun lâ tunbitu şey'â, gloss:kenûd toprak, hiçbir şey bitirmeyen topraktır, source:"ك ن د,B003"}.

[¶29] Toprak görüntüsünü surenin başka kelimeleri tamamlar. Dördüncü ayetin fiili bulutu kaldıran rüzgârda da toprağı süren elde de kullanılır: {ar:فتثير سحابا... وأثاروا الأرض, tr:fe-tusîru sehâben... ve esârû'l-ard, gloss:bulutu kaldırır... toprağı sürdüler, source:"ث و ر,B002"}. "Nak'", sel suyunun durup toplandığı yerdir: {ar:نقع الماء في منقعة السيل اجتمع فيها وطال مكثه, tr:neka'a'l-mâu fî menka'ati's-seyl, ictema'a fîhâ ve tâle muksuh, gloss:su, selin göllendiği yerde toplandı ve uzun süre kaldı, source:"ن ق ع,B001"}. "Nak'" aynı zamanda iyi topraktır: {ar:النقاع واحدها نقع وهي الأرض الحرة الطين الطيبة التي لا حزونة فيها ولا ارتفاع ولا انهباط, tr:en-nikâ'u vâhiduhâ nak', ve hiye'l-ardu'l-hurratu't-tîni't-tayyibetu'lletî lâ huzûnete fîhâ ve lâ irtifâ'a ve lâ inhibât, gloss:"nikâ'" (tekili "nak'"), sertliği, tümseği, çukuru olmayan, saf ve iyi balçıklı topraktır, source:"ن ق ع,B007"}. Surenin son kelimesinin ailesinde de yağmur suyunu toplayan alçak toprak vardır: {ar:الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء, tr:el-habrâu'l-ardu's-sehletu'l-munhafidatu yectemi'u fîhâ mâu's-semâ', gloss:"habrâ", gökten inen suyun toplandığı yumuşak, alçak topraktır, source:"خ ب ر,B002"}. Aynı ailede toprağı işleyen de vardır: {ar:الخبير الأكار, tr:el-habîru'l-ekkâr, gloss:"habîr", çiftçidir, source:"خ ب ر,B003"}. Sekizinci ayetteki sevgi kelimesinin yanında, toprağın vermesi beklenen tane durur: {ar:الحب والحبة في الحنطة والشعير, tr:el-habbu ve'l-habbetu fi'l-hıntati ve'ş-şa'îr, gloss:buğday ve arpada tane, source:"ح ب ب,B001"}. Yemin cümlesi böylece bir tarla sahnesi kurar. Bulut bitkiyi yetiştirir, rüzgâr bulutu kaldırır, su alçak toprakta toplanır, iyi balçık suyu tutar ve çiftçi toprağı işler. Bütün bu bakıma karşın kenûd toprak hiçbir şey bitirmez. Düz bir anlatım "insan nankördür" demekle yetinirdi. Görüntü ise nankörlüğün neye karşı olduğunu gösterir: adım adım yetiştirmeye, tamamlanmış bir iyiliğe, yağmura.

[¶30] Sekizinci ayetteki "hayr" kelimesinin bir yüzü de bu bakımın ta kendisidir: {ar:الخير الهبة, tr:el-hayru'l-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Kelime cömertlik de demektir: {ar:والخير الكرم, tr:ve'l-hayru'l-kerem, gloss:hayır, cömertliktir, source:"خ ي ر,B005"}. İnsan bağışa şiddetle düşkündür ama bağışı vereni unutur. Yedinci ayet bu nankörlüğün tanığını getirir: {ar:وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ, tr:ve innehû alâ zâlike le-şehîd, gloss:ve şüphesiz o buna tanıktır, source:100:7}. Tanıklık bilgiye dayanan sözdür: {ar:الشهادة قول صادر عن علم, tr:eş-şehâdetu kavlun sâdirun an ilm, gloss:şahitlik, bilgiden kaynaklanan sözdür, source:"ش ه د,B002"}. Ayetteki zamir bir önceki cümlede anılan insana da Rabbine de dönebilecek konumdadır. Hangisine dönerse dönsün, tanıklık aynı şeyin, kesilen ipin üzerindedir. On birinci ayet aynı Rabbi bir kez daha anar, ama bu kez çoğul bir zamirle: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevme'izin le-habîr, gloss:şüphesiz Rableri o gün onlardan tamamen haberdardır, source:100:11}. İpi kesenler O'nun bilgisinin dışına çıkmış olmazlar.

[¶31] Kur'an bu toprak sahnesini açıkça kurar. Allah rüzgârları rahmetinin önünde müjdeci olarak gönderir, ağır bulutları ölü bir toprağa sürer, oraya su indirir ve her türlü ürünü çıkarır. Sonra şöyle der: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍ يَشْكُرُونَ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, ve'llezî habuse lâ yahrucu illâ nekidâ, kezâlike nusarrifu'l-âyâti li-kavmin yeşkurûn, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar; kötü olanınki ise ancak kıt ve cılız çıkar; şükreden bir kavim için ayetleri böyle çeşitli biçimlerde açıklarız, source:7:58}. Toprak, onun Rabbi, kıt ürün ve şükür tek bir ayette bir aradadır. Rüzgârın bulutu kaldırması da bizim dördüncü ayetin fiiliyle anlatılır: {ar:ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًا, tr:Allâhu'llezî yursilu'r-riyâha fe-tusîru sehâben, gloss:Allah, rüzgârları gönderen ve onların bulutu kaldırdığı kimsedir, source:30:48}. İnsanın nankörlüğü Kur'an'da sayma üzerinden de anlatılır: {ar:وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱلْإِنسَٰنَ لَظَلُومٌ كَفَّارٌ, tr:ve in teuddû ni'meta'llâhi lâ tuhsûhâ, inne'l-insâne le-zalûmun keffâr, gloss:Allah'ın nimetini saymaya kalksanız sayamazsınız; şüphesiz insan çok zalim, çok nankördür, source:14:34}. Kenûd musibetleri sayıp nimetleri unutur. Bu ayet ise sayılmaya kalkılsa tükenmeyecek olanın nimet olduğunu söyler. Denizde sıkışan insanlar yalnız O'na yalvarır, sonra: {ar:فَلَمَّا نَجَّىٰكُمْ إِلَى ٱلْبَرِّ أَعْرَضْتُمْ ۚ وَكَانَ ٱلْإِنسَٰنُ كَفُورًا, tr:fe-lemmâ neccâkum ile'l-berri a'radtum, ve kâne'l-insânu kefûrâ, gloss:sizi karaya çıkarıp kurtarınca yüz çevirdiniz; insan pek nankördür, source:17:67}. Başka bir yerde de {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6} ve {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en reâhu'steğnâ, gloss:kendini kimseye muhtaç görmediğinde, source:96:7} denir. İnsana Rabbinin adıyla yöneltilen soru da aynı iki kelimeyi yan yana koyar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyuhe'l-insânu mâ ğarrake bi-rabbike'l-kerîm, gloss:ey insan, seni o cömert Rabbine karşı ne aldattı, source:82:6}. Yol gösterildikten sonra iki seçenek bırakılır: {ar:إِمَّا شَاكِرًا وَإِمَّا كَفُورًا, tr:immâ şâkiran ve immâ kefûrâ, gloss:ya şükreden ya da nankör olarak, source:76:3}. Tanıklık ile Rab sözü de en baştaki bir sahnede bir araya gelir. Rabbin Âdem oğullarının sırtlarından soylarını aldığı anlatılır ve şöyle denir: {ar:وَأَشْهَدَهُمْ عَلَىٰٓ أَنفُسِهِمْ أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ ۛ شَهِدْنَآ, tr:ve eşhedehum alâ enfusihim e-lestu bi-rabbikum, kâlû belâ şehidnâ, gloss:onları kendilerine karşı tanık tuttu: "Ben sizin Rabbiniz değil miyim?" "Evet, tanık olduk" dediler, source:7:172}.

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

===== passages from the discovery list (439) =====
## strong (274)

- (2:22) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The section depicts land receiving rain and producing provision, then the human forgetting its giver. This ayah says God made the earth a resting place, sent down water, and brought forth fruits as provision, before warning against setting up rivals to Him. | terra: The Lord creates people, makes earth and sky serviceable, and sends rain that produces fruits as provision; recipients are told not to give His place to rivals.
- (2:152) [terra: strong; basis: speaker+theme] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
  Unverified discovery rationale: terra: “Remember Me, I will remember you” makes the relation reciprocal, then commands gratitude and forbids ingratitude; it is the uncut version of the section's two-way cord.
- (2:164) [luna: strong; terra: medium; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The section assembles wind, cloud, water, and earth into a chain of care. This ayah places the winds, clouds, rain, and revived earth together among God’s signs, with a concluding call to reason; it lets the reader see the whole field relation at once. | terra: Rain revives earth, creatures spread, winds turn, and cloud is held between heaven and earth; this lays out the field's whole administered ecology.
- (2:172) [luna: strong; terra: strong (missing-ayat turn); basis: speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَٱشْكُرُوا۟ لِلَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
  Unverified discovery rationale: luna: The section says the receiver cuts the return of thanks to the giver. This ayah tells believers to eat the good provisions God gave them and be grateful to Him, directly naming the reciprocal response. | terra: Believers are told to eat the good things God provided and thank Him if they worship Him, directly binding consumed provision to gratitude.
- (2:177) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+root+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section links love of خير with gratitude and maintaining a bond. This ayah describes righteousness as giving beloved wealth to relatives, orphans, and the needy, while keeping promises; it joins generosity to sustained obligations. | terra: True righteousness includes giving wealth despite one's love for it, turning حُبّ of possession into an onward gift rather than kenud withholding.
- (2:205) [luna: strong (missing-ayat turn); terra: contrast (missing-ayat turn); basis: contrast+scene+theme] وَإِذَا تَوَلَّىٰ سَعَىٰ فِى ٱلْأَرْضِ لِيُفْسِدَ فِيهَا وَيُهْلِكَ ٱلْحَرْثَ وَٱلنَّسْلَ ۗ وَٱللَّهُ لَا يُحِبُّ ٱلْفَسَادَ
  Unverified discovery rationale: luna: The section’s Rab gloss includes the one who improves, while kenūd land bears no growth. This ayah depicts a person who spreads corruption and destroys crops and offspring, a human reversal of the Rabb’s nurturing work. | terra: When the corrupt person turns away he destroys crops and livestock, actively undoing the nurturing field system rather than merely failing to yield.
- (2:215) [terra: strong (missing-ayat turn); basis: root+theme] يَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ ۖ قُلْ مَآ أَنفَقْتُم مِّنْ خَيْرٍۢ فَلِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ ۗ وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: terra: The answer to what should be spent calls it خَيْر and directs it to relatives and vulnerable recipients, using the named word in an explicitly generous sense.
- (2:261) [luna: strong; terra: strong; basis: root+scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section names grain (حبة) and says a good yield is the expected return of care. This ayah compares a charitable gift to a seed grain producing seven ears, joining crop and generosity as multiplied return. | terra: Spending in God's way is a grain that grows seven ears and manifold seed, turning a passed-on gift into cultivated abundance.
- (2:264) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ وَلَا يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۖ فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا ۖ لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: The section’s kenūd soil yields nothing despite rain. This ayah compares showy or injurious giving to a smooth rock with a thin covering of soil that rain leaves bare, making failed generosity resemble a field unable to retain its yield. | terra: A gift spoiled by reproach is like soil on smooth rock stripped bare by rain; giving whose relation is cut produces nothing.
- (2:265) [luna: strong; terra: strong; basis: contrast+scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: The section’s good-soil image is paired here with spending for God’s approval: a garden on a height receives rain and yields twice over. It shows a generous response taking root in receptive ground. | terra: Sincere spending is a garden whose rain doubles its yield and whose drizzle still suffices, the fruitful opposite of both 2:264 and kenud soil.
