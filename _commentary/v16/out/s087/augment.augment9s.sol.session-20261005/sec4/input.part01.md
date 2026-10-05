Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 4 of 18 ("Ölçüp biçmek: ok, tulum ve kura"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 4 (prose paragraphs numbered) =====
[¶17] İkinci ve üçüncü ayet dört fiili sıralar: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Arapçada bu fiiller bir zanaatkârın işinin adımlarıdır. خلق, kökünde ölçüp biçmektir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Bu tanım ikinci ayetin fiilini üçüncü ayetin fiiline bağlar. Ölçülüp yontulmuş ok da bu köktendir: {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş düzgün ve doğru ok, source:"خ ل ق,B008"}. Bu tanımda ikinci ayetin öbür fiili olan سوّى'nin kökü de vardır. سوّى eğri olanı doğrultmaktır: {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"}. قدّر, bir şeyi nasıl düzleyip hazır edeceğini düşünmektir: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmek, source:"ق د ر,B005"}. Aynı kök bir şeyin vardığı ölçüyü de bildirir: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sonu, source:"ق د ر,B001"}. Sonra هدى gelir. Bu kelime okun önde giden ucudur: {ar:هادي السهم نصله, tr:hâdi's-sehmi naslu, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"}. Değnek de taşıyanın önünden gittiği için bu adı alır: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemuh, gloss:değnek önünden gittiği için hâdî adını alır, source:"ه د ي,B003"}. Rab ise bir şeyi düzeltip adım adım tamamlayandır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}.

[¶18] Değneği doğrultmanın bir yolu da ateştir. Bu işin fiili, on ikinci ayetteki "ateşe girer" fiilinin kendisidir: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"}. Ölçmek, doğrultmak ve uç takmak, ikinci ve üçüncü ayetin düz anlamının yanında bir yapım sahnesi kurar. Yapılan şey yalnızca var edilmez, bir yöne de çevrilir. "Yol gösterdi" fiili okun ucunun bir hedefe dönmesi gibi duyulur.

[¶19] Aynı ölçüp biçme bir deri üzerinde de yapılır. خلق'in ilk örneği, su tulumu için deriyi kesmeden önce ölçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde halaktu derim, source:"خ ل ق,B001"}. İkinci ayetin fiili ile üçüncü ayetin fiili burada tek bir hareketin iki adı olur. Bitmiş kabın yapısını dokuzuncu ayetteki نفع kökü anlatır: {ar:النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة, tr:en-nif'u fi'l-mezâdeti fî cânibeyhâ yuşakku'l-edîmu fe-yuc'alu fî cânibeyhâ fî kulli cânibin nif'a, gloss:su kırbasının iki yanına deri yarılıp her yana nif'a denen bir parça konur, source:"ن ف ع,B002"}. Bu yanlar on birinci ayetteki kelimenin köküyle anılır: {ar:الجنبتان ناحيتا كل شيء, tr:el-canbetân nâhiyetâ kulli şey', gloss:her şeyin iki yanı, source:"ج ن ب,B001"}. Deri yağla terbiye edilir. Bu da "Rab" kelimesinin ailesindendir: {ar:رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب, tr:rabebtu'l-edîme bi's-semni ve'd-devâe bi'l-asel ve sikâun merbûb, gloss:deriyi yağla ilacı balla terbiye ettim; terbiye edilmiş tulum, source:"ر ب ب,B006"}. Tulum çalkalanır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuhû, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Kullanıldıkça da aşınıp düzleşir: {ar:أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره, tr:ahleka'ş-şey'u ve haleka iẕâ beliye iẕâ ahleka imlâsse ve ẕehebe zi'biruh, gloss:bir şey eskiyince ahleka denir; eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Beş kök tek bir nesnede, ölçülen, yanları eklenen, terbiye edilen ve eskiyen bir tulumda buluşur. Kur'an bu nesneyi bir sahnede kullanmaz. Ama aynı kelime ailesi yaratılışı bir zanaat olarak duyurur, ve bu zanaatta ölçü kesmeden önce gelir.

[¶20] Üçüncü bir nesne, kura okudur. "Rab" kelimesinin ailesinde okların saklandığı torba vardır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbe şebîhetun bi'l-kinâneti tucmeu fîhâ sihâmu'l-meysir, gloss:ribâbe meysir oklarının toplandığı sadağa benzer torbadır, source:"ر ب ب,B010"}. Bu tanım sekizinci ayetteki "kolaylaştırırız" fiilinin kökünü, meysiri, de içerir. Meysir bir oyundur ve adı paylaştırmadan gelir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yasera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını paylaştı, source:"ي س ر,B007"}. Okların en büyük payı alanı birinci ayetteki "en yüce" kelimesinin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Okun gövdesi yontulup yumuşatılır: {ar:المخلق القدح إذا لين, tr:el-muhallak el-kıdhu iẕâ luyyine, gloss:muhallak yumuşatılmış ok gövdesidir, source:"خ ل ق,B008"}. Pay da aynı köktendir: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâk en-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"}. Her şeyin bir ölçüsü ve bir vadesi vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve süresi vardır, source:"ق د ر,B001"}. İkinci ve üçüncü ayetteki ölçüp biçme bu sahnede paylaştırmaya döner. On altıncı ve on yedinci ayetteki seçim de bir pay seçimidir.

[¶21] Kur'an bu ölçmeyi yaratılışın kendisine uygular. Allah inkâr eden insan için {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddera, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Bu iki ayet surenin ikinci, üçüncü ve sekizinci ayetlerinin fiillerini aynı sırayla verir. Başka bir yerde Allah {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve ona tam ölçüsünü verdi, source:25:2} ve {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49} der. Surenin son ayetinde adı geçen İbrahim, putları reddedip kavmine Âlemlerin Rabbini anlatırken bu ikiliyi kendi ağzından söyler: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Pay kelimesi Kur'an'da tam bu surenin vardığı karşıtlıkla geçer. Hac ibadetleri anlatılırken yalnız bu dünyada verilmesini isteyen kişi için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} denir. Önceki kavimler için {ar:فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ, tr:fe'stemteû bi-halâkıhim, gloss:paylarından yararlandılar, source:9:69} denir, ayetin sonunda da yaptıkları dünyada ve ahirette boşa gider. Kura okları ve meysir müminlere yasaklanırken kullanılan kelimeler ise surenin iki kelimesini yan yana getirir: {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90}. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" burada aynı cümlededir. Başka bir yerde meysir için {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:günahları faydalarından büyüktür, source:2:219} denir. Oklarla kısmet aramak da sayılan yasaklar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla pay aramanız, source:5:3}. Kura okuyla alınan pay yasaklanır. Ölçüyü koyanın verdiği pay ise ahirette de geçerlidir.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (288) =====
## strong (200)

- (2:29) [terra: strong (missing-ayat turn); basis: root+scene+theme] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: terra: God creates everything on earth, turns to heaven, and proportions it as seven heavens; creation proceeds into the ordered finishing of a constructed whole.
- (2:60) [terra: strong (missing-ayat turn); basis: scene+theme] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: terra: Twelve springs emerge and every people knows its drinking place; water is divided into recognized shares for a whole community.
- (2:86) [terra: strong (missing-ayat turn); basis: contrast+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: terra: Those who buy worldly life with the Hereafter enact the section’s choice as an exchange, and their punishment is neither lightened nor relieved.
- (2:102) [terra: strong; basis: contrast+root+theme] وَٱتَّبَعُوا۟ مَا تَتْلُوا۟ ٱلشَّيَٰطِينُ عَلَىٰ مُلْكِ سُلَيْمَٰنَ ۖ وَمَا كَفَرَ سُلَيْمَٰنُ وَلَٰكِنَّ ٱلشَّيَٰطِينَ كَفَرُوا۟ يُعَلِّمُونَ ٱلنَّاسَ ٱلسِّحْرَ وَمَآ أُنزِلَ عَلَى ٱلْمَلَكَيْنِ بِبَابِلَ هَٰرُوتَ وَمَٰرُوتَ ۚ وَمَا يُعَلِّمَانِ مِنْ أَحَدٍ حَتَّىٰ يَقُولَآ إِنَّمَا نَحْنُ فِتْنَةٌۭ فَلَا تَكْفُرْ ۖ فَيَتَعَلَّمُونَ مِنْهُمَا مَا يُفَرِّقُونَ بِهِۦ بَيْنَ ٱلْمَرْءِ وَزَوْجِهِۦ ۚ وَمَا هُم بِضَآرِّينَ بِهِۦ مِنْ أَحَدٍ إِلَّا بِإِذْنِ ٱللَّهِ ۚ وَيَتَعَلَّمُونَ مَا يَضُرُّهُمْ وَلَا يَنفَعُهُمْ ۚ وَلَقَدْ عَلِمُوا۟ لَمَنِ ٱشْتَرَىٰهُ مَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ ۚ وَلَبِئْسَ مَا شَرَوْا۟ بِهِۦٓ أَنفُسَهُمْ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: terra: Those who purchase magic know that its buyer has no khalaq in the Hereafter; the bargain turns a chosen worldly acquisition into loss of the enduring share.
- (2:185) [terra: strong (missing-ayat turn); basis: root+speaker+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: terra: God desires ease rather than hardship, commands completion of the numbered period, and calls for magnifying Him because He guided; ease, measure, guidance, and glorification converge.
- (2:200) [luna: strong; terra: strong; basis: contrast+root+speaker+theme] [cited in ¶21] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: luna: 2:200 says the person who asks only for worldly good has no “خَلَاقٍ” in the Hereafter. The source-section identifies خَلَاق as a measured share, so this is a direct instance of a worldly choice leaving no afterlife share. | terra: The worshipper who asks the Lord only for this world has “no khalaq in the Hereafter”; the Quran uses the section’s measured-share noun for precisely Surah 87’s worldly choice.
- (2:201) [terra: strong; basis: neighbour+speaker+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: Beside 2:200’s person with no afterlife share, this speaker asks the Lord for good in both worlds, showing a choice of portion that does not discard the lasting life.
- (2:202) [luna: strong; terra: strong; basis: neighbour+root+theme] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
  Unverified discovery rationale: luna: 2:202 says those people have “نَصِيبٌ مِّمَّا كَسَبُوا۟,” a share from what they earned. It clarifies the source-section’s contrast between a lot-won share and a share assigned in relation to what one has done. | terra: Those who ask for both worlds “have a share” (نَصِيبٌ) of what they earned, completing 2:200–201’s contrast between a passing request and a valid final allotment.
- (2:219) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶21] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ ۖ قُلْ فِيهِمَآ إِثْمٌۭ كَبِيرٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا ۗ وَيَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ قُلِ ٱلْعَفْوَ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
  Unverified discovery rationale: luna: 2:219 asks about intoxicants and gambling and says their sin is greater than their benefit, “نَفْعِهِمَا.” It joins the source-section’s meysir game to its named root ن ف ع and distinguishes a game’s benefit from its greater harm. | terra: Wine and gambling have benefits but their sin is greater than their benefit; the judgment directly tests the section’s water-skin term nifʿ against the apparent gain of maysir.
- (2:280) [luna: strong (missing-ayat turn); basis: contrast+root+theme] وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: 2:280 says an insolvent debtor should be given time until ease, using the source-section root ي س ر in a financial setting. It contrasts ease granted to someone in need with meysir as a game for dividing gains.
- (3:6) [luna: strong; terra: strong; basis: scene+theme] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: 3:6 says God forms people in their mothers’ wombs as He wills. This is a bodily instance of the source-section’s making and fitting a form to its intended measure. | terra: God forms people in the womb however He wills; hidden bodily formation supplies the concrete workshop implied by measuring before shaping.
- (3:44) [luna: strong; terra: strong; basis: contrast+scene+theme] ذَٰلِكَ مِنْ أَنۢبَآءِ ٱلْغَيْبِ نُوحِيهِ إِلَيْكَ ۚ وَمَا كُنتَ لَدَيْهِمْ إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ وَمَا كُنتَ لَدَيْهِمْ إِذْ يَخْتَصِمُونَ
  Unverified discovery rationale: luna: 3:44 recalls people casting their pens to decide who would care for Mary. It stages a lot that assigns a responsibility rather than a game’s prize, clarifying the boundary around the source-section’s arrow-drawn shares. | terra: The contenders cast their pens to determine who would care for Mary; this narrative allocation by cast objects provides a boundary alongside the forbidden fortune arrows.
- (3:77) [terra: strong; basis: contrast+root+theme] إِنَّ ٱلَّذِينَ يَشْتَرُونَ بِعَهْدِ ٱللَّهِ وَأَيْمَٰنِهِمْ ثَمَنًۭا قَلِيلًا أُو۟لَٰٓئِكَ لَا خَلَٰقَ لَهُمْ فِى ٱلْءَاخِرَةِ وَلَا يُكَلِّمُهُمُ ٱللَّهُ وَلَا يَنظُرُ إِلَيْهِمْ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
  Unverified discovery rationale: terra: People who sell God’s covenant and their oaths for a small price have no khalaq in the Hereafter; the ayah opposes a cheap chosen return to God’s lasting portion.
- (3:145) [terra: strong (missing-ayat turn); basis: contrast+root+theme] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
  Unverified discovery rationale: terra: Every soul’s death has a written appointed term, and the ayah then gives worldly reward to its seeker and afterlife reward to its seeker; limit, selection, and allotted return occur together.
