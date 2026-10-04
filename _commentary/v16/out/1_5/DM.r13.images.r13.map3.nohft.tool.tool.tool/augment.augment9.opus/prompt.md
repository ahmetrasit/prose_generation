Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:5; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_5/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_5.reading.tr.md (prose paragraphs numbered) =====
## Dört ayetten sonra ilk söz: "Seni"

[¶1] Fâtiha'nın ilk dört ayeti Allah'tan "O" diye söz eder. Hamd O'nadır. O âlemlerin Rabbi, Rahman ve Rahim'dir, din gününün sahibidir. Beşinci ayette konuşan kişi O'na döner ve doğrudan seslenir. Allah'a doğrudan söylediği ilk söz {ar:إِيَّاكَ, tr:iyyâke, gloss:yalnız seni, source:1:5} olur. "İyyâ" sözcüğünün tek başına bir anlamı yoktur. Zamirin fiilden ayrılıp öne geçebilmesi için ona dayanak olur. Anlamı sondaki "-ke" ekindedir, yani "sen" demektir. Olağan sırada zamir fiilin sonuna eklenirdi ve "na'büdüke", yani "sana kulluk ederiz" denirdi. Ayet zamiri fiilden ayırır ve cümlenin başına koyar. Nesne fiilden önce gelince başka bütün ihtimaller dışarıda kalır: Kulluk edilen sensin, başkası değil. Türkçe meal bunu "yalnız" kelimesiyle iyi karşılar. Karşılayamadığı şey sözün sırasıdır. Dua eden kişi, Allah'a ilk kez doğrudan seslendiğinde kendi yaptığı işten önce O'nu söyler.

[¶2] Kur'an, sözün öne alınmasının ne yaptığını aynı konuşmacının iki cümlesiyle gösterir. Peygambere önce {ar:قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ, tr:kul innî ümirtü en a'büdallâhe muhlisan lehü'd-dîn, gloss:de ki: Bana, dini O'na özgü kılarak Allah'a kulluk etmem emredildi, source:39:11} demesi emredilir. Az sonra aynı söz, Allah adı fiilden önce gelecek biçimde yinelenir: {ar:قُلِ ٱللَّهَ أَعْبُدُ مُخْلِصًۭا لَّهُۥ دِينِى, tr:kulillâhe a'büdü muhlisan lehû dînî, gloss:de ki: Ben ancak Allah'a, dinimi O'na özgü kılarak kulluk ederim, source:39:14}. Hemen ardından karşı tarafa {ar:فَٱعْبُدُوا۟ مَا شِئْتُم مِّن دُونِهِۦ, tr:fa'büdû mâ şi'tüm min dûnih, gloss:siz de O'ndan başka neye dilerseniz ona kulluk edin, source:39:15} denir. Birinci cümle bir emri bildirir. İkinci cümle bir ayrılığı ilan eder, çünkü öne geçen ad öteki kulluk edilenlerin hepsini dışarıda bırakır. Fâtiha'nın beşinci ayeti bu ikinci türden bir cümledir.

[¶3] Aynı sözü Allah kendi ağzından da söyler. Kullarına yeryüzünün geniş olduğunu hatırlatır: {ar:يَٰعِبَادِىَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ أَرْضِى وَٰسِعَةٌۭ فَإِيَّٰىَ فَٱعْبُدُونِ, tr:yâ ibâdiye'llezîne âmenû inne ardî vâsi'atün fe-iyyâye fa'büdûn, gloss:ey iman eden kullarım, yerim geniştir, öyleyse yalnız bana kulluk edin, source:29:56}. Orada "yalnız bana" denir, burada kul "yalnız sana" diye karşılık verir. Zindanda iki arkadaşına konuşan Yusuf aynı sınırı "illâ" ile çizer: {ar:أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ, tr:emera ellâ ta'büdû illâ iyyâh, gloss:O'ndan başkasına kulluk etmemenizi emretti, source:12:40}. Aynı yapı kıyamet sahnesinde tersine işler. Allah herkesi topladığı gün meleklere sorar: {ar:أَهَٰٓؤُلَآءِ إِيَّاكُمْ كَانُوا۟ يَعْبُدُونَ, tr:e-hâülâi iyyâküm kânû ya'büdûn, gloss:bunlar size mi kulluk ediyorlardı, source:34:40}. Melekler bu "size"yi kabul etmez ve sözü kendilerinden geri çevirirler: {ar:سُبْحَٰنَكَ أَنتَ وَلِيُّنَا مِن دُونِهِم, tr:sübhâneke ente veliyyünâ min dûnihim, gloss:Sen yücesin, onları değil seni dost ediniriz, source:34:41}. Onlar da "sen" diyerek Allah'a dönerler.

[¶4] Ayette "iyyâke" iki kez geçer. Bir kez söylenip iki fiil ona bağlanabilirdi. Böyle olsaydı yardım istemek kulluğun bir ayrıntısı gibi kalırdı. Ayet, iki işin her birini ayrı ayrı "sen"e bağlar. Sure de bu dönüşten sonra hiç geri dönmez. Altıncı ayetteki {ar:ٱهْدِنَا, tr:ihdinâ, gloss:bizi ilet, source:1:6} ona yönelmiş bir istektir. Yedinci ayetteki {ar:أَنْعَمْتَ, tr:en'amte, gloss:nimet verdin, source:1:7} de ona söylenmiş bir sözdür. İki fiil şimdiyi ve süreni birlikte anlatan kipte gelir. Kul "kulluk ettik" ya da "edeceğiz" demez. Sürmekte olan bir hali söyler: kulluk ederiz, yardım dileriz.

## Kul: ait olmak ve boyun eğmek

[¶5] {ar:نَعْبُدُ, tr:na'büdü, gloss:kulluk ederiz, source:1:5} fiilinin kökü önce bir toplumsal durumu adlandırır: {ar:العبد المملوك وجمعه عبيد, tr:el-abdü'l-memlûk ve cem'uhû abîd, gloss:abd, sahip olunan kişidir, çoğulu abîd, source:"ع ب د,B001"}. Kısaca {ar:العبد ضد الحر, tr:el-abdü ziddü'l-hurr, gloss:abd, hürün karşıtıdır, source:"ع ب د,B001"} de denir. Türkçede "ibadet" kelimesi daralmıştır. Namaz kılan ya da oruç tutan için "ibadet ediyor" denir ve kelime belirli vakitlerde yapılan işlere çekilmiştir. Arapçada ise kelime bir duruşla başlar: Birine ait olmak ve bu aitliğin gereğini yapmak. Bu anlamda kulluk, saatleri belli bir iş olmaktan önce, insanın kime ait olduğunu söyleyen bir haldir. Fiilin bu ayetteki anlamı da itaatle açıklanmıştır: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke na'büdü: iyyâke nutî'u't-tâ'ate'lletî nahdau me'ahâ, gloss:yalnız sana kulluk ederiz, yani yalnız sana boyun eğerek itaat ederiz, source:"ع ب د,B003"}. Kelimenin ne kadar ileri gittiği de söylenmiştir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ubûdiyyetü izhâru't-tezellül ve'l-ibâdetü gâyetü't-tezellül, gloss:kulluk alçak gönüllülüğü göstermektir, ibadet ise boyun eğmenin son noktasıdır, source:"ع ب د,B003"}.

[¶6] Bu boyun eğiş insanlara da yönelebilir. Araplar bir adama boyun eğen kişi için {ar:تعبدت للرجل إذا تذللت له, tr:teabbedtü li'r-racüli izâ tezelleltü leh, gloss:adama boyun eğdiğimde teabbedtü derim, source:"ع ب د,B003"} derlerdi. Fiil başkasını boyunduruk altına almak için de kullanılırdı: {ar:عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا, tr:abedtü'r-racüle izâ zelleltühû ve abedtü'l-kavme ittehaztühüm abîdâ, gloss:adamı boyun eğdirdim; kavmi köle edindim, source:"ع ب د,B004"}. Kur'an bu kullanımı Firavun'un sarayında gösterir. Musa ile Harun apaçık delillerle Firavun'a ve ileri gelenlerine gönderilir, onlar da büyüklük taslar {source:23:46}. Sonra şunu derler: {ar:وَقَوْمُهُمَا لَنَا عَٰبِدُونَ, tr:ve kavmühümâ lenâ âbidûn, gloss:üstelik onların kavmi bize kulluk ediyor, source:23:47}. Firavun Musa'ya onu çocukken büyüttüğünü hatırlatır {source:26:18}. Musa da onun başa kaktığı iyiliğin adını koyar: {ar:أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ, tr:en abbedte benî İsrâîl, gloss:İsrailoğullarını köle edinmiş olman, source:26:22}. İnsanın elinde bu fiil köleleştirmek anlamına gelir.

[¶7] "İyyâke na'büdü" sözü bu yüzden yalnızca bir saygı sözü değildir. Kişi kime ait olduğunu söylerken başka efendilere giden yolu da kapatır. Kur'an kitap ehline aynı fiili, aynı "biz" ile önerir: {ar:أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ, tr:ellâ na'büde illallâh, gloss:Allah'tan başkasına kulluk etmeyelim, source:3:64}. Aynı cümle şöyle devam eder: {ar:وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ, tr:ve lâ yettehize ba'dunâ ba'dan erbâben min dûnillâh, gloss:Allah'ı bırakıp birbirimizi rabler edinmeyelim, source:3:64}. Zindandaki Yusuf da aynı seçimi bir soruyla önüne koyar: {ar:ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ, tr:e-erbâbün müteferrikûne hayrun emillâhü'l-vâhidü'l-kahhâr, gloss:birbirinden ayrı birçok efendi mi daha iyidir, yoksa tek ve her şeye galip olan Allah mı, source:12:39}. Tek sahibe ait olmak, birçok efendinin arasında bölünmemek demektir.

[¶8] Bu kökten gelen kelimelerin bir kısmı da kelimenin bu ayetteki anlamının yanında duyulur. Hiçbiri o anlamın yerine geçmez. İlki şaşırtıcıdır. Kulluk ibadetini yerine getirmeye {ar:التعبد التنسك, tr:et-teabbüdü't-tenessük, gloss:teabbüd, kendini ibadete vermektir, source:"ع ب د,B003"} denir. Aynı kalıptan bir sıfat ise insanlara yaklaşmayan bir deveye ad verir: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:ba'îrun müteabbidün ve müteebbidün izâ imtene'a ale'n-nâsi su'ûbeten, gloss:huysuzlaşıp insanlara yanaşmayan deveye müteabbid denir, source:"ع ب د,B011"}. "Müteabbid" kelimesi hem kendini ibadete veren kişiyi hem de insanların elinden kaçan deveyi anlatır. Bu iki anlamı yan yana koymak bir yorumdur, ama ayetin öne aldığı zamir bu yorumu destekler. Yalnız birine boyun eğen kişi, öbür bütün ellere karşı başı dik kalır. Kökün edilgen biçimi ise kulluğun yöneldiği tarafı gösterir: {ar:المعبد المكرم والمعظم كأنه يعبد, tr:el-mu'abbedü'l-mükerramü ve'l-mu'azzamü ke-ennehû yu'bed, gloss:mu'abbed, sanki kulluk ediliyormuş gibi ağırlanan ve yüceltilen kişidir, source:"ع ب د,B006"}. Kıyamet sahnesindeki melekler böyle görülmeyi reddeder. "Size mi kulluk ediyorlardı" sorusunu kendi üzerlerinde bırakmazlar.

[¶9] Bu aitlik kulun kendi kararıyla başlamaz. {ar:العبد الإنسان حرا أو رقيقا هو عبد الله, tr:el-abdü'l-insânü hurran ev rakîkan hüve abdu'llâh, gloss:insan, hür de olsa köle de olsa Allah'ın kuludur, source:"ع ب د,B002"} denir. Bu kulluğun sebebi de gösterilir: {ar:عبد بالإيجاد وذلك ليس إلا لله, tr:abdün bi'l-îcâd ve zâlike leyse illâ lillâh, gloss:var edilmiş olmakla kul olmak; bu yalnızca Allah için söz konusudur, source:"ع ب د,B002"}. Kur'an bunu bütün varlıklar için söyler: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde kim varsa Rahman'a ancak kul olarak gelecektir, source:19:93}. Beşinci ayet bu aitliği yaratmaz. Yaratılışla zaten var olan bir aitliği kulun kendi sesiyle ve kendi isteğiyle söyler. Dördüncü ayetteki sahiplik kelimelerinin kurduğu efendi ve mülk sahnesi surenin bütününe aittir. Burada konuşan, o sahnede sahip olunan taraftır.

## Çiğnenmiş yol, katranlı deve, ziftli gemi

[¶10] Aynı kök, insan elinin ya da ayağının işleyip hizmete elverişli hale getirdiği üç nesneye ad verir. İlki yoldur: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-mu'abbedü ve hüve'l-meslûku'l-müzellel, gloss:mu'abbed yol, çok yürünmüş ve düzlenmiş yoldur, source:"ع ب د,B005"}. Böyle bir yolu tek bir adım yapmaz. Çok sayıda ayağın aynı çizgiden geçmesi gerekir. Ayaklar toprağın sertliğini kırar, otu yatırır, çizgiyi belirginleştirir. Sonunda yol, üzerinde yürüyeni zorlamaz olur. Tanımdaki iki kelime bu işleyişi anlatır. "Meslûk" üzerinden geçilmiş demektir, "müzellel" ise boyun eğdirilmiş ve kolaylaşmış demektir. İkinci nesne devedir: {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-mu'abbedü'l-mehnû'ü bi'l-katrâni'l-müzellel, gloss:katranla sıvanmış, uysallaştırılmış deve, source:"ع ب د,B005"}. Bir başka tarif katranın nereye kadar sürüldüğünü söyler: {ar:المعبد من الإبل الذي عم جلده بالقطران, tr:el-mu'abbedü mine'l-ibili'llezî amme cildehû bi'l-katrân, gloss:derisinin her yeri katranla kaplanmış deve, source:"ع ب د,B005"}. Katran deriye bakım için sürülürdü ve tarif bu baştan sona sıvanmış deveyi uysal deve olarak anar. Üçüncü nesne gemidir: {ar:المعبدة السفينة المقيرة, tr:el-mu'abbedetü's-sefînetü'l-mukayyere, gloss:ziftle kaplanmış gemi, source:"ع ب د,B005"}. Teknenin tahta ekleri ziftle doldurulunca su içeri sızmaz ve gemi denize dayanabilir hale gelir.

[¶11] Bu üç nesnede ortak olan şey şudur: Her biri üzerinde emek harcanarak işe yarar hale gelmiştir. Yol yürüyene, deve binene, gemi denizciye hizmet eder. Kulluk kelimesinin yanında bu görüntü, boyun eğmenin bir ezilme olmadığını, yürünebilir, binilebilir, suya dayanır olmak olduğunu duyurur. Kökün başka bir kolu bu duyuşa sağlamlık katar: {ar:ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة, tr:nâkatün zâtü abedetin ey zâtü kuvvetin ve simen, ve mâ li-sevbike abedetün ey kuvve, gloss:abedeli deve güçlü ve semiz devedir; "elbisenin abedesi yok" ise dayanıklılığı yok demektir, source:"ع ب د,B007"}. Bu kol, ayrıca {ar:العبدة البقاء وقيل الشدة, tr:el-abedetü'l-bekâ' ve kîle'ş-şidde, gloss:abede kalıcılıktır, sertlik olduğu da söylenir, source:"ع ب د,B007"} diye de anılır. Aynı harfler hem uysallaşmayı hem dayanıklılığı adlandırır. Katranlı deve ile ziftli gemi bu iki anlamı tek bir işlemde birleştirir: Sürülen madde hem onları hizmete hazırlar hem de korur.

[¶12] Kur'an bu uysallaştırmayı Allah'ın işi olarak anlatır. Yeryüzü hakkında şöyle der: {ar:جَعَلَ لَكُمُ ٱلْأَرْضَ ذَلُولًۭا فَٱمْشُوا۟ فِى مَنَاكِبِهَا, tr:ceale lekümü'l-arda zelûlen femşû fî menâkibihâ, gloss:yeri size boyun eğen, uysal bir binek gibi yaptı; öyleyse onun sırtlarında yürüyün, source:67:15}. Arıya verdiği vahiyde de önce dağlarda ve ağaçlarda yuva edinmesini söyler {source:16:68}, sonra şöyle buyurur: {ar:فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًۭا, tr:fesülükî sübüle rabbiki zülülâ, gloss:Rabbinin sana kolaylaştırılmış yollarında boyun eğerek yürü, source:16:69}. Bu kısa emirde yol tanımının iki kelimesi yeniden görünür: "meslûk" fiilde, "müzellel" ise "zülül" kelimesinde. "Zülül" dil bakımından hem yollara hem arıya bağlanabilir. Yol da yürüyen de uysaldır. Bu yürüyüşün sonucu aynı ayette söylenir: {ar:يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌۭ مُّخْتَلِفٌ أَلْوَٰنُهُۥ فِيهِ شِفَآءٌۭ لِّلنَّاسِ, tr:yahrucü min butûnihâ şerâbün muhtelifün elvânühû fîhi şifâün li'n-nâs, gloss:karınlarından renkleri türlü türlü bir içecek çıkar, onda insanlar için şifa vardır, source:16:69}.

[¶13] Kulluğu bir yol olarak adlandıran da yine Kur'an'dır. Suçluların ayrıldığı gün Allah Âdemoğullarına verdiği sözü hatırlatır: {ar:أَن لَّا تَعْبُدُوا۟ ٱلشَّيْطَٰنَ, tr:en lâ ta'büdü'ş-şeytân, gloss:şeytana kulluk etmeyin diye, source:36:60}. Ardından şöyle der: {ar:وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:ve eni'büdûnî, hâzâ sırâtun müstakîm, gloss:ve bana kulluk edin; işte dosdoğru yol budur, source:36:61}. Bu yüzden altıncı ayetin "sırat" kelimesiyle istenen yol, beşinci ayetin fiilinde zaten duyulur. Çok yürünmüş yolun yüzeyi kulluğun kendisidir. O yolun önden giden kılavuzu ve varış evi, surenin bütününe ait bir sahne olarak altıncı ve yedinci ayetlerin kelimelerinde kurulur. Aynı kökte bu tek yolun karşıtı da vardır: {ar:العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد, tr:el-abâdîdü'l-firaku mine'n-nâsi'z-zâhibûne fî külli vech, gloss:abâdîd, her yöne dağılıp giden insan bölükleridir, source:"ع ب د,B010"}. Kur'an yolların insanları dağıttığını aynı görüntüyle söyler: {ar:وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve lâ tettebi'u's-sübüle fe-teferraka biküm an sebîlih, gloss:başka yollara uymayın, sizi O'nun yolundan ayırıp dağıtır, source:6:153}. Çok kişinin tek bir çizgiden yürümesi yolu düzler. Herkesin kendi yönüne gitmesi ise topluluğu bölüklere ayırır.

## Dayanılan şey: yardım istemek

[¶14] {ar:نَسْتَعِينُ, tr:nesteînü, gloss:yardım dileriz, source:1:5} fiilinin kalıbı istemek anlamı taşır: {ar:الاستعانة طلب العون, tr:el-isti'ânetü talebü'l-avn, gloss:istiâne, yardım istemektir, source:"ع و ن,B001"}. İstenen "avn" ise geniş bir kelimedir: {ar:كل شيء استعنت به أو أعانك فهو عونك, tr:küllü şey'in este'ante bihî ev eâneke fe-hüve avnük, gloss:yardımını istediğin ya da sana yardım eden her şey senin avnindir, source:"ع و ن,B001"}. Avn bir kişi olabileceği gibi bir alet, bir güç ya da bir huy da olabilir. Yardımın neye benzediği de söylenir: {ar:العون الظهيرة على الأمر, tr:el-avnü'z-zahîretü ale'l-emr, gloss:avn, bir işte arka çıkan destektir, source:"ع و ن,B001"}. Bir başka tarif de şöyledir: {ar:العون المعاونة والمظاهرة, tr:el-avnü'l-muâvenetü ve'l-muzâhara, gloss:avn, yardımlaşma ve arka çıkmadır, source:"ع و ن,B001"}. "Zahîr" kelimesi sırttan gelir. Yardım eden, insanın arkasında duran ve yükünü sırtıyla paylaşan kişidir. Türkçede bu kökten "iane" kalmıştır, ama bir iş için toplanan bağış anlamına daralmıştır. "Muavin" ise bir makamdaki yardımcıdır. Ayetteki kelime ise insanın dayandığı her şeyi kapsar.

[¶15] Ayet, yardımın neye karşı ya da ne için istendiğini söylemez. Kur'an'da yardım çoğu zaman bir derdin karşısında istenir. Yusuf'un kardeşleri onu kurdun yediğini söyler {source:12:17} ve gömleğini sahte kanla getirir. Babaları Yakup şöyle der: {ar:وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:vallâhü'l-müsteânü alâ mâ tesıfûn, gloss:anlattıklarınıza karşı yardımı istenecek olan Allah'tır, source:12:18}. Peygamber de sözü kabul etmeyen bir topluluğa duyurusunu yaptıktan sonra {source:21:109} aynı sözle bitirir: {ar:وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:ve rabbüne'r-rahmânü'l-müsteânü alâ mâ tesıfûn, gloss:Rabbimiz, anlattıklarınıza karşı yardımı istenecek olan Rahman'dır, source:21:112}. Bu iki sahnede dert bellidir. Fâtiha'da ise dert adlandırılmaz. Böylece istek bütün işlere açık kalır. İlk açıkça istenen şey de hemen ardından gelir: Altıncı ayet yolu ister. Kulluk kelimesinin kökü burada sessiz bir hazırlık yapar. Bineği yolda tükenen yolcu için {ar:أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت, tr:u'bide bi-fülânin bi-ma'nâ übdia bihî izâ kellet râhiletühû ev atıbet, gloss:falanca yolda kaldı, yani bineği yoruldu ya da sakatlandı, source:"ع ب د,B011"} denirdi. "Na'büdü" kelimesinin kökünde yolda kalmış bir adam vardır ve hemen sonraki kelime yardım ister. İki yanından tutularak yürüyen güçsüz yolcu ise altıncı ayetin "ihdinâ" kelimesinin taşıdığı ve surenin bütününe ait bir sahnedir.

[¶16] Sıra da anlamlıdır: önce kulluk, sonra yardım. Kur'an bu ikisini başka yerlerde de aynı sırayla bir araya getirir. Peygambere {ar:فَٱعْبُدْهُ وَتَوَكَّلْ عَلَيْهِ, tr:fa'büdhü ve tevekkel aleyh, gloss:O'na kulluk et ve O'na dayan, source:11:123} denir. Rablerinin emriyle indiklerini söyleyen melekler {source:19:64} kulluğun bir güç gerektirdiğini de anlatır: {ar:فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ, tr:fa'büdhü vastabir li-ibâdetih, gloss:O'na kulluk et ve O'na kulluk etmekte direnerek sabret, source:19:65}. Kulluk bir yükse, yardım istemek o yükün altında dik durabilmektir. İstek de kulluğun dışından değil, içinden yapılır.

[¶17] Burada beklenmedik bir şey ortaya çıkar. Kur'an, yardım istenecek şeyler arasında namazı da sayar. Önce İsrailoğullarına {ar:وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ, tr:vesteînû bi's-sabri ve's-salâh, ve innehâ le-kebîratün ille ale'l-hâşi'în, gloss:sabırla ve namazla yardım isteyin; o, gönülden boyun eğenlerden başkasına ağır gelir, source:2:45} denir. Sonra müminlere {ar:يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ, tr:yâ eyyühe'llezîne âmenü'steînû bi's-sabri ve's-salâh, gloss:ey iman edenler, sabırla ve namazla yardım isteyin, source:2:153} denir. Fâtiha her namazda okunur. Kişi "yardımı yalnız senden dileriz" sözünü, kendisi bir dayanak olan namazın içinde söyler. Yardım isteği, istenen yardımın içinde yapılmış olur. Görünürdeki çelişki de "avn" kelimesinin genişliğiyle çözülür. Sabır ve namaz insanın dayandığı araçlardır, yardımı istenen ise yalnız O'dur. Musa, Firavun'un oğulları öldürme tehdidi karşısında {source:7:127} halkına bu iki şeyi ayrı ayrı söyler: {ar:ٱسْتَعِينُوا۟ بِٱللَّهِ وَٱصْبِرُوٓا۟, tr:isteînû billâhi vasbirû, gloss:Allah'tan yardım isteyin ve sabredin, source:7:128}. Yardım Allah'tan istenir, sabretmek ise onların işidir.

[¶18] Yardım insanlar arasında da istenir. Zülkarneyn'den bir set yapması istenir ve bunun için ona ücret önerilir {source:18:94}. O ücreti almaz, onun yerine güç ister: {ar:فَأَعِينُونِى بِقُوَّةٍ أَجْعَلْ بَيْنَكُمْ وَبَيْنَهُمْ رَدْمًا, tr:fe-eînûnî bi-kuvvetin ec'al beyneküm ve beynehüm radmâ, gloss:bana güç vererek yardım edin de sizinle onlar arasına sağlam bir set yapayım, source:18:95}. Müminlere de yardımın yönü gösterilir: {ar:وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ, tr:ve teâvenû ale'l-birri ve't-takvâ, ve lâ teâvenû ale'l-ismi ve'l-udvân, gloss:iyilikte ve sakınmada yardımlaşın, günahta ve düşmanlıkta yardımlaşmayın, source:5:2}. Arka çıkmak yanlış tarafa da yönelebilir. Musa, şehirde kendi tarafından birinin yardım çağrısına koşmuş ve karşı taraftaki adamı tek darbeyle öldürmüştür {source:28:15}. Bağışlanma diledikten sonra {source:28:16} şu sözü verir: {ar:رَبِّ بِمَآ أَنْعَمْتَ عَلَىَّ فَلَنْ أَكُونَ ظَهِيرًۭا لِّلْمُجْرِمِينَ, tr:rabbi bimâ en'amte aleyye fe-len ekûne zahîran li'l-mücrimîn, gloss:Rabbim, bana verdiğin nimet hakkı için suçlulara asla arka çıkmayacağım, source:28:17}. Bu sözde yedinci ayetteki "en'amte" ile yardımın "zahîr" kelimesi aynı cümlede yer alır. Nimeti tanıyan kişi kime arka çıkacağını da seçer.

[¶19] Yardım yalnızca tek yönde akar. Allah'tan başka çağrılanlar için şöyle denir: {ar:وَمَا لَهُۥ مِنْهُم مِّن ظَهِيرٍۢ, tr:ve mâ lehû minhüm min zahîr, gloss:O'nun onlardan bir destekçisi de yoktur, source:34:22}. Hamd sözü de bunu tamamlar: {ar:وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ, tr:ve lem yekün lehû veliyyün mine'z-züll, gloss:güçsüzlükten ötürü bir yardımcıya da ihtiyacı olmadı, source:17:111}. Kulluğun tanımında geçen "tezellül", yani boyun eğiş, kula aittir. Allah hakkında aynı kökten gelen "züll", yani düşkünlük, açıkça reddedilir. Kul kulluğunu ve yardım isteğini O'na yöneltir. O ise ne birinin kulu olur ne de birinin yardımına muhtaç olur.

## "Biz"

[¶20] İki fiil de çoğuldur: kulluk ederiz, yardım dileriz. Fâtiha her namazda okunduğu için kişi yalnız namaz kıldığında da "ben" değil "biz" der. Allah'ın kulları kelimesi bir topluluğu da anlatır. Kur'an'daki bir davet bu yüzden {ar:فادخلي في عبادي أي في حزبي, tr:fe'dhulî fî ibâdî ey fî hizbî, gloss:kullarımın arasına gir, yani benim topluluğuma katıl, source:"ع ب د,B002"} diye açıklanır. Bu davet, yeryüzünün dövülüp düzlendiği ve Rabbin meleklerle saf saf geldiği günün anlatıldığı yerde geçer {source:89:22}. Allah orada huzura ermiş cana seslenir: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetühe'n-nefsü'l-mutmainne, gloss:ey huzura ermiş can, source:89:27}. Ona Rabbine dönmesini söyler {source:89:28}, sonra şöyle der: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Bahçeye girmek {ar:وَٱدْخُلِى جَنَّتِى, tr:vedhulî cennetî, gloss:cennetime gir, source:89:30} ancak bundan sonra gelir. Varılan yerin ilk adı bir topluluktur. Beşinci ayetin "biz"i o topluluğun dünyada söylediği sözdür.

[¶21] Bu "biz" dışarıya kapalı değildir. Daha önce kitap ehline yöneltilen çağrı "kulluk etmeyelim" diye birinci çoğul şahısla kurulmuştu. Yani aynı fiilin "biz"i, ayrı yollardan gelenleri ortak bir söze çağırır. Topluluğun kendi içindeki yardımlaşması da aynı kökten gelir: "teâvenû", yani iyilikte birbirinize yardım edin. Aynı harfler yaban eşeği sürüsüne de ad verir: {ar:العانة القطيع من حمر الوحش, tr:el-ânetü'l-katî'u min humuri'l-vahş, gloss:âne, yaban eşeği sürüsüdür, source:"ع و ن,B006"}. Bu kelime, birlikte koşan bir sürüden öte bir şey taşımaz. Ayetteki "biz" ise sahibini bilen ve O'na "sen" diye seslenen bir topluluktur.

[¶22] Bu topluluğa ait olmak bir korumadır. İblis insanları yoldan çıkaracağına yemin ettiğinde kendisi bir istisna yapar: {ar:إِلَّا عِبَادَكَ مِنْهُمُ ٱلْمُخْلَصِينَ, tr:illâ ibâdeke minhümü'l-muhlasîn, gloss:onlardan ancak arınmış kulların hariç, source:15:40}. Allah da ona cevap verir: {ar:إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌ, tr:inne ibâdî leyse leke aleyhim sultân, gloss:kullarım üzerinde senin hiçbir gücün yoktur, source:15:42}. Tek sahibe ait olduğunu kendi ağzıyla söyleyen kişi, başka bir efendinin eline düşmez. Firavun'un saray adamlarının "bize kulluk ediyorlar" dediği halk, Fâtiha'nın her okunuşunda bu sözün tersini söyler: Biz yalnız sana kulluk ederiz.

===== _commentary/v16/out/1_5/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: iyyâ is a rootless support for a detached pronoun
- memory: fronting the object pronoun restricts (yalnız sen)
- memory: unfronted form would be na'buduka
- memory: imperfect na'budu/nasta'în covers present and continuing
- memory: zahîr derives from zahr, the back
- memory: tar was smeared on camels' skin as care
- memory: pitch caulks ship seams against water
- memory: dhululan in 16:69 can qualify paths or the bee
- memory: Turkish iane narrowed to donation; muavin to assistant
- not written: ع ب د B008 indignation/pride - no ayah-supported tie to this address
- not written: ع ب د B009 not delaying - fixed phrase, no thematic work
- not written: ع ب د B012 perfume-grinding stone - no bridge to the ayah
- not written: ع و ن B002–B005 middle age, recurring war, old palm, bodily balance - no textual bridge to seeking help
- not written: ع و ن B007 pubic hair, B008 place name 'Âna - irrelevant to the ayah
- not written: echo root ع ي ن (eye, spring) - sound only, not identity
- not written: 10:28 partners disowning worship - 34:40-41 already does this work
- not written: 25:55 disbeliever as backer against his Lord - 28:17 carried the point

===== passages not cited (283) =====
## strong (this ayah's own list) (51)

- (2:186) [listed for 1:5] وَإِذَا سَأَلَكَ عِبَادِى عَنِّى فَإِنِّى قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ ۖ فَلْيَسْتَجِيبُوا۟ لِى وَلْيُؤْمِنُوا۟ بِى لَعَلَّهُمْ يَرْشُدُونَ
- (2:286) [listed for 1:5] لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا ٱكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَآ إِن نَّسِينَآ أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَآ إِصْرًۭا كَمَا حَمَلْتَهُۥ عَلَى ٱلَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِۦ ۖ وَٱعْفُ عَنَّا وَٱغْفِرْ لَنَا وَٱرْحَمْنَآ ۚ أَنتَ مَوْلَىٰنَا فَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (3:51) [listed for 1:5] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (3:64) [listed for 1:5] [cited in ¶7] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ تَعَالَوْا۟ إِلَىٰ كَلِمَةٍۢ سَوَآءٍۭ بَيْنَنَا وَبَيْنَكُمْ أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ وَلَا نُشْرِكَ بِهِۦ شَيْـًۭٔا وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ ۚ فَإِن تَوَلَّوْا۟ فَقُولُوا۟ ٱشْهَدُوا۟ بِأَنَّا مُسْلِمُونَ
- (3:150) [listed for 1:5] بَلِ ٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ خَيْرُ ٱلنَّٰصِرِينَ
- (4:36) [listed for 1:5] ۞ وَٱعْبُدُوا۟ ٱللَّهَ وَلَا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا وَبِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱلْجَارِ ذِى ٱلْقُرْبَىٰ وَٱلْجَارِ ٱلْجُنُبِ وَٱلصَّاحِبِ بِٱلْجَنۢبِ وَٱبْنِ ٱلسَّبِيلِ وَمَا مَلَكَتْ أَيْمَٰنُكُمْ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ مَن كَانَ مُخْتَالًۭا فَخُورًا
- (4:45) [listed for 1:5] وَٱللَّهُ أَعْلَمُ بِأَعْدَآئِكُمْ ۚ وَكَفَىٰ بِٱللَّهِ وَلِيًّۭا وَكَفَىٰ بِٱللَّهِ نَصِيرًۭا
- (4:172) [listed for 1:5] لَّن يَسْتَنكِفَ ٱلْمَسِيحُ أَن يَكُونَ عَبْدًۭا لِّلَّهِ وَلَا ٱلْمَلَٰٓئِكَةُ ٱلْمُقَرَّبُونَ ۚ وَمَن يَسْتَنكِفْ عَنْ عِبَادَتِهِۦ وَيَسْتَكْبِرْ فَسَيَحْشُرُهُمْ إِلَيْهِ جَمِيعًۭا
- (5:23) [listed for 1:5] قَالَ رَجُلَانِ مِنَ ٱلَّذِينَ يَخَافُونَ أَنْعَمَ ٱللَّهُ عَلَيْهِمَا ٱدْخُلُوا۟ عَلَيْهِمُ ٱلْبَابَ فَإِذَا دَخَلْتُمُوهُ فَإِنَّكُمْ غَٰلِبُونَ ۚ وَعَلَى ٱللَّهِ فَتَوَكَّلُوٓا۟ إِن كُنتُم مُّؤْمِنِينَ
- (6:102) [listed for 1:5] ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ خَٰلِقُ كُلِّ شَىْءٍۢ فَٱعْبُدُوهُ ۚ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ وَكِيلٌۭ
- (6:162) [listed for 1:5] قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (7:128) [listed for 1:5] [cited in ¶17] قَالَ مُوسَىٰ لِقَوْمِهِ ٱسْتَعِينُوا۟ بِٱللَّهِ وَٱصْبِرُوٓا۟ ۖ إِنَّ ٱلْأَرْضَ لِلَّهِ يُورِثُهَا مَن يَشَآءُ مِنْ عِبَادِهِۦ ۖ وَٱلْعَٰقِبَةُ لِلْمُتَّقِينَ
- (8:40) [listed for 1:5] وَإِن تَوَلَّوْا۟ فَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَوْلَىٰكُمْ ۚ نِعْمَ ٱلْمَوْلَىٰ وَنِعْمَ ٱلنَّصِيرُ
- (9:51) [listed for 1:5] قُل لَّن يُصِيبَنَآ إِلَّا مَا كَتَبَ ٱللَّهُ لَنَا هُوَ مَوْلَىٰنَا ۚ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ
- (10:106) [listed for 1:5] وَلَا تَدْعُ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُكَ وَلَا يَضُرُّكَ ۖ فَإِن فَعَلْتَ فَإِنَّكَ إِذًۭا مِّنَ ٱلظَّٰلِمِينَ
- (11:123) [listed for 1:5] [cited in ¶16] وَلِلَّهِ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَإِلَيْهِ يُرْجَعُ ٱلْأَمْرُ كُلُّهُۥ فَٱعْبُدْهُ وَتَوَكَّلْ عَلَيْهِ ۚ وَمَا رَبُّكَ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (12:40) [listed for 1:5] [cited in ¶3] مَا تَعْبُدُونَ مِن دُونِهِۦٓ إِلَّآ أَسْمَآءًۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۚ أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (14:35) [listed for 1:5] وَإِذْ قَالَ إِبْرَٰهِيمُ رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ
- (17:2) [listed for 1:5] وَءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ أَلَّا تَتَّخِذُوا۟ مِن دُونِى وَكِيلًۭا
- (18:16) [listed for 1:5] وَإِذِ ٱعْتَزَلْتُمُوهُمْ وَمَا يَعْبُدُونَ إِلَّا ٱللَّهَ فَأْوُۥٓا۟ إِلَى ٱلْكَهْفِ يَنشُرْ لَكُمْ رَبُّكُم مِّن رَّحْمَتِهِۦ وَيُهَيِّئْ لَكُم مِّنْ أَمْرِكُم مِّرْفَقًۭا
- (19:36) [listed for 1:5] وَإِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (19:65) [listed for 1:5] [cited in ¶16] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:14) [listed for 1:5] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (21:25) [listed for 1:5] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ مِن رَّسُولٍ إِلَّا نُوحِىٓ إِلَيْهِ أَنَّهُۥ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدُونِ
- (21:112) [listed for 1:5] [cited in ¶15] قَٰلَ رَبِّ ٱحْكُم بِٱلْحَقِّ ۗ وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (22:77) [listed for 1:5] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱرْكَعُوا۟ وَٱسْجُدُوا۟ وَٱعْبُدُوا۟ رَبَّكُمْ وَٱفْعَلُوا۟ ٱلْخَيْرَ لَعَلَّكُمْ تُفْلِحُونَ ۩
- (26:71) [listed for 1:5] قَالُوا۟ نَعْبُدُ أَصْنَامًۭا فَنَظَلُّ لَهَا عَٰكِفِينَ
- (29:17) [listed for 1:5] إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًۭا وَتَخْلُقُونَ إِفْكًا ۚ إِنَّ ٱلَّذِينَ تَعْبُدُونَ مِن دُونِ ٱللَّهِ لَا يَمْلِكُونَ لَكُمْ رِزْقًۭا فَٱبْتَغُوا۟ عِندَ ٱللَّهِ ٱلرِّزْقَ وَٱعْبُدُوهُ وَٱشْكُرُوا۟ لَهُۥٓ ۖ إِلَيْهِ تُرْجَعُونَ
- (33:3) [listed for 1:5] وَتَوَكَّلْ عَلَى ٱللَّهِ ۚ وَكَفَىٰ بِٱللَّهِ وَكِيلًۭا
- (36:22) [listed for 1:5] وَمَا لِىَ لَآ أَعْبُدُ ٱلَّذِى فَطَرَنِى وَإِلَيْهِ تُرْجَعُونَ
- (36:23) [listed for 1:5] ءَأَتَّخِذُ مِن دُونِهِۦٓ ءَالِهَةً إِن يُرِدْنِ ٱلرَّحْمَٰنُ بِضُرٍّۢ لَّا تُغْنِ عَنِّى شَفَٰعَتُهُمْ شَيْـًۭٔا وَلَا يُنقِذُونِ
- (36:61) [listed for 1:5] [cited in ¶13] وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (37:118) [listed for 1:5] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (39:2) [listed for 1:5] إِنَّآ أَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (39:11) [listed for 1:5] [cited in ¶2] قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (39:64) [listed for 1:5] قُلْ أَفَغَيْرَ ٱللَّهِ تَأْمُرُوٓنِّىٓ أَعْبُدُ أَيُّهَا ٱلْجَٰهِلُونَ
- (39:66) [listed for 1:5] بَلِ ٱللَّهَ فَٱعْبُدْ وَكُن مِّنَ ٱلشَّٰكِرِينَ
- (40:14) [listed for 1:5] فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (40:60) [listed for 1:5] وَقَالَ رَبُّكُمُ ٱدْعُونِىٓ أَسْتَجِبْ لَكُمْ ۚ إِنَّ ٱلَّذِينَ يَسْتَكْبِرُونَ عَنْ عِبَادَتِى سَيَدْخُلُونَ جَهَنَّمَ دَاخِرِينَ
- (41:6) [listed for 1:5] قُلْ إِنَّمَآ أَنَا۠ بَشَرٌۭ مِّثْلُكُمْ يُوحَىٰٓ إِلَىَّ أَنَّمَآ إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَٱسْتَقِيمُوٓا۟ إِلَيْهِ وَٱسْتَغْفِرُوهُ ۗ وَوَيْلٌۭ لِّلْمُشْرِكِينَ
- (42:10) [listed for 1:5] وَمَا ٱخْتَلَفْتُمْ فِيهِ مِن شَىْءٍۢ فَحُكْمُهُۥٓ إِلَى ٱللَّهِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبِّى عَلَيْهِ تَوَكَّلْتُ وَإِلَيْهِ أُنِيبُ
- (43:64) [listed for 1:5] إِنَّ ٱللَّهَ هُوَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (44:18) [listed for 1:5] أَنْ أَدُّوٓا۟ إِلَىَّ عِبَادَ ٱللَّهِ ۖ إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ
- (46:28) [listed for 1:5] فَلَوْلَا نَصَرَهُمُ ٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ قُرْبَانًا ءَالِهَةًۢ ۖ بَلْ ضَلُّوا۟ عَنْهُمْ ۚ وَذَٰلِكَ إِفْكُهُمْ وَمَا كَانُوا۟ يَفْتَرُونَ
- (53:62) [listed for 1:5] فَٱسْجُدُوا۟ لِلَّهِ وَٱعْبُدُوا۟ ۩
- (72:18) [listed for 1:5] وَأَنَّ ٱلْمَسَٰجِدَ لِلَّهِ فَلَا تَدْعُوا۟ مَعَ ٱللَّهِ أَحَدًۭا
- (72:20) [listed for 1:5] قُلْ إِنَّمَآ أَدْعُوا۟ رَبِّى وَلَآ أُشْرِكُ بِهِۦٓ أَحَدًۭا
- (72:21) [listed for 1:5] قُلْ إِنِّى لَآ أَمْلِكُ لَكُمْ ضَرًّۭا وَلَا رَشَدًۭا
- (73:9) [listed for 1:5] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (96:10) [listed for 1:5] عَبْدًا إِذَا صَلَّىٰٓ
- (109:2) [listed for 1:5] لَآ أَعْبُدُ مَا تَعْبُدُونَ

## medium (this ayah's own list) (89)

- (2:21) [listed for 1:5] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
- (2:45) [listed for 1:5] [cited in ¶17] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
- (2:83) [listed for 1:5] وَإِذْ أَخَذْنَا مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ لَا تَعْبُدُونَ إِلَّا ٱللَّهَ وَبِٱلْوَٰلِدَيْنِ إِحْسَانًۭا وَذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ثُمَّ تَوَلَّيْتُمْ إِلَّا قَلِيلًۭا مِّنكُمْ وَأَنتُم مُّعْرِضُونَ
- (2:112) [listed for 1:5] بَلَىٰ مَنْ أَسْلَمَ وَجْهَهُۥ لِلَّهِ وَهُوَ مُحْسِنٌۭ فَلَهُۥٓ أَجْرُهُۥ عِندَ رَبِّهِۦ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:133) [listed for 1:5] أَمْ كُنتُمْ شُهَدَآءَ إِذْ حَضَرَ يَعْقُوبَ ٱلْمَوْتُ إِذْ قَالَ لِبَنِيهِ مَا تَعْبُدُونَ مِنۢ بَعْدِى قَالُوا۟ نَعْبُدُ إِلَٰهَكَ وَإِلَٰهَ ءَابَآئِكَ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ إِلَٰهًۭا وَٰحِدًۭا وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (2:153) [listed for 1:5] [cited in ¶17] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ إِنَّ ٱللَّهَ مَعَ ٱلصَّٰبِرِينَ
- (2:172) [listed for 1:5] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَٱشْكُرُوا۟ لِلَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (3:20) [listed for 1:5] فَإِنْ حَآجُّوكَ فَقُلْ أَسْلَمْتُ وَجْهِىَ لِلَّهِ وَمَنِ ٱتَّبَعَنِ ۗ وَقُل لِّلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْأُمِّيِّۦنَ ءَأَسْلَمْتُمْ ۚ فَإِنْ أَسْلَمُوا۟ فَقَدِ ٱهْتَدَوا۟ ۖ وَّإِن تَوَلَّوْا۟ فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:79) [listed for 1:5] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
- (4:75) [listed for 1:5] وَمَا لَكُمْ لَا تُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ وَٱلْمُسْتَضْعَفِينَ مِنَ ٱلرِّجَالِ وَٱلنِّسَآءِ وَٱلْوِلْدَٰنِ ٱلَّذِينَ يَقُولُونَ رَبَّنَآ أَخْرِجْنَا مِنْ هَٰذِهِ ٱلْقَرْيَةِ ٱلظَّالِمِ أَهْلُهَا وَٱجْعَل لَّنَا مِن لَّدُنكَ وَلِيًّۭا وَٱجْعَل لَّنَا مِن لَّدُنكَ نَصِيرًا
- (4:118) [listed for 1:5] لَّعَنَهُ ٱللَّهُ ۘ وَقَالَ لَأَتَّخِذَنَّ مِنْ عِبَادِكَ نَصِيبًۭا مَّفْرُوضًۭا
- (4:132) [listed for 1:5] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ وَكَفَىٰ بِٱللَّهِ وَكِيلًا
- (5:2) [listed for 1:5] [cited in ¶18] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (5:76) [listed for 1:5] قُلْ أَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَمْلِكُ لَكُمْ ضَرًّۭا وَلَا نَفْعًۭا ۚ وَٱللَّهُ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (5:117) [listed for 1:5] مَا قُلْتُ لَهُمْ إِلَّا مَآ أَمَرْتَنِى بِهِۦٓ أَنِ ٱعْبُدُوا۟ ٱللَّهَ رَبِّى وَرَبَّكُمْ ۚ وَكُنتُ عَلَيْهِمْ شَهِيدًۭا مَّا دُمْتُ فِيهِمْ ۖ فَلَمَّا تَوَفَّيْتَنِى كُنتَ أَنتَ ٱلرَّقِيبَ عَلَيْهِمْ ۚ وَأَنتَ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
- (6:17) [listed for 1:5] وَإِن يَمْسَسْكَ ٱللَّهُ بِضُرٍّۢ فَلَا كَاشِفَ لَهُۥٓ إِلَّا هُوَ ۖ وَإِن يَمْسَسْكَ بِخَيْرٍۢ فَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (6:56) [listed for 1:5] قُلْ إِنِّى نُهِيتُ أَنْ أَعْبُدَ ٱلَّذِينَ تَدْعُونَ مِن دُونِ ٱللَّهِ ۚ قُل لَّآ أَتَّبِعُ أَهْوَآءَكُمْ ۙ قَدْ ضَلَلْتُ إِذًۭا وَمَآ أَنَا۠ مِنَ ٱلْمُهْتَدِينَ
- (6:71) [listed for 1:5] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
- (6:88) [listed for 1:5] ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۚ وَلَوْ أَشْرَكُوا۟ لَحَبِطَ عَنْهُم مَّا كَانُوا۟ يَعْمَلُونَ
- (6:163) [listed for 1:5] لَا شَرِيكَ لَهُۥ ۖ وَبِذَٰلِكَ أُمِرْتُ وَأَنَا۠ أَوَّلُ ٱلْمُسْلِمِينَ
- (7:59) [listed for 1:5] لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (7:65) [listed for 1:5] ۞ وَإِلَىٰ عَادٍ أَخَاهُمْ هُودًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۚ أَفَلَا تَتَّقُونَ
- (7:73) [listed for 1:5] وَإِلَىٰ ثَمُودَ أَخَاهُمْ صَٰلِحًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ فَيَأْخُذَكُمْ عَذَابٌ أَلِيمٌۭ
- (7:85) [listed for 1:5] وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا ۗ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ قَدْ جَآءَتْكُم بَيِّنَةٌۭ مِّن رَّبِّكُمْ ۖ فَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ وَلَا تَبْخَسُوا۟ ٱلنَّاسَ أَشْيَآءَهُمْ وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
- (7:197) [listed for 1:5] وَٱلَّذِينَ تَدْعُونَ مِن دُونِهِۦ لَا يَسْتَطِيعُونَ نَصْرَكُمْ وَلَآ أَنفُسَهُمْ يَنصُرُونَ
- (9:31) [listed for 1:5] ٱتَّخَذُوٓا۟ أَحْبَارَهُمْ وَرُهْبَٰنَهُمْ أَرْبَابًۭا مِّن دُونِ ٱللَّهِ وَٱلْمَسِيحَ ٱبْنَ مَرْيَمَ وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ۚ سُبْحَٰنَهُۥ عَمَّا يُشْرِكُونَ
- (9:129) [listed for 1:5] فَإِن تَوَلَّوْا۟ فَقُلْ حَسْبِىَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَلَيْهِ تَوَكَّلْتُ ۖ وَهُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ
- (10:18) [listed for 1:5] وَيَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَضُرُّهُمْ وَلَا يَنفَعُهُمْ وَيَقُولُونَ هَٰٓؤُلَآءِ شُفَعَٰٓؤُنَا عِندَ ٱللَّهِ ۚ قُلْ أَتُنَبِّـُٔونَ ٱللَّهَ بِمَا لَا يَعْلَمُ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (10:29) [listed for 1:5] فَكَفَىٰ بِٱللَّهِ شَهِيدًۢا بَيْنَنَا وَبَيْنَكُمْ إِن كُنَّا عَنْ عِبَادَتِكُمْ لَغَٰفِلِينَ
- (11:2) [listed for 1:5] أَلَّا تَعْبُدُوٓا۟ إِلَّا ٱللَّهَ ۚ إِنَّنِى لَكُم مِّنْهُ نَذِيرٌۭ وَبَشِيرٌۭ
- (11:26) [listed for 1:5] أَن لَّا تَعْبُدُوٓا۟ إِلَّا ٱللَّهَ ۖ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ أَلِيمٍۢ
- (11:50) [listed for 1:5] وَإِلَىٰ عَادٍ أَخَاهُمْ هُودًۭا ۚ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۖ إِنْ أَنتُمْ إِلَّا مُفْتَرُونَ
- (11:62) [listed for 1:5] قَالُوا۟ يَٰصَٰلِحُ قَدْ كُنتَ فِينَا مَرْجُوًّۭا قَبْلَ هَٰذَآ ۖ أَتَنْهَىٰنَآ أَن نَّعْبُدَ مَا يَعْبُدُ ءَابَآؤُنَا وَإِنَّنَا لَفِى شَكٍّۢ مِّمَّا تَدْعُونَآ إِلَيْهِ مُرِيبٍۢ
- (11:84) [listed for 1:5] ۞ وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا ۚ قَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ ۖ وَلَا تَنقُصُوا۟ ٱلْمِكْيَالَ وَٱلْمِيزَانَ ۚ إِنِّىٓ أَرَىٰكُم بِخَيْرٍۢ وَإِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍۢ مُّحِيطٍۢ
- (12:18) [listed for 1:5] [cited in ¶15] وَجَآءُو عَلَىٰ قَمِيصِهِۦ بِدَمٍۢ كَذِبٍۢ ۚ قَالَ بَلْ سَوَّلَتْ لَكُمْ أَنفُسُكُمْ أَمْرًۭا ۖ فَصَبْرٌۭ جَمِيلٌۭ ۖ وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (12:67) [listed for 1:5] وَقَالَ يَٰبَنِىَّ لَا تَدْخُلُوا۟ مِنۢ بَابٍۢ وَٰحِدٍۢ وَٱدْخُلُوا۟ مِنْ أَبْوَٰبٍۢ مُّتَفَرِّقَةٍۢ ۖ وَمَآ أُغْنِى عَنكُم مِّنَ ٱللَّهِ مِن شَىْءٍ ۖ إِنِ ٱلْحُكْمُ إِلَّا لِلَّهِ ۖ عَلَيْهِ تَوَكَّلْتُ ۖ وَعَلَيْهِ فَلْيَتَوَكَّلِ ٱلْمُتَوَكِّلُونَ
- (13:14) [listed for 1:5] لَهُۥ دَعْوَةُ ٱلْحَقِّ ۖ وَٱلَّذِينَ يَدْعُونَ مِن دُونِهِۦ لَا يَسْتَجِيبُونَ لَهُم بِشَىْءٍ إِلَّا كَبَٰسِطِ كَفَّيْهِ إِلَى ٱلْمَآءِ لِيَبْلُغَ فَاهُ وَمَا هُوَ بِبَٰلِغِهِۦ ۚ وَمَا دُعَآءُ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍۢ
- (13:16) [listed for 1:5] قُلْ مَن رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ قُلِ ٱللَّهُ ۚ قُلْ أَفَٱتَّخَذْتُم مِّن دُونِهِۦٓ أَوْلِيَآءَ لَا يَمْلِكُونَ لِأَنفُسِهِمْ نَفْعًۭا وَلَا ضَرًّۭا ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ أَمْ هَلْ تَسْتَوِى ٱلظُّلُمَٰتُ وَٱلنُّورُ ۗ أَمْ جَعَلُوا۟ لِلَّهِ شُرَكَآءَ خَلَقُوا۟ كَخَلْقِهِۦ فَتَشَٰبَهَ ٱلْخَلْقُ عَلَيْهِمْ ۚ قُلِ ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ وَهُوَ ٱلْوَٰحِدُ ٱلْقَهَّٰرُ
- (15:49) [listed for 1:5] ۞ نَبِّئْ عِبَادِىٓ أَنِّىٓ أَنَا ٱلْغَفُورُ ٱلرَّحِيمُ
- (16:36) [listed for 1:5] وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ ۖ فَمِنْهُم مَّنْ هَدَى ٱللَّهُ وَمِنْهُم مَّنْ حَقَّتْ عَلَيْهِ ٱلضَّلَٰلَةُ ۚ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (16:51) [listed for 1:5] ۞ وَقَالَ ٱللَّهُ لَا تَتَّخِذُوٓا۟ إِلَٰهَيْنِ ٱثْنَيْنِ ۖ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ ۖ فَإِيَّٰىَ فَٱرْهَبُونِ
- (16:73) [listed for 1:5] وَيَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَمْلِكُ لَهُمْ رِزْقًۭا مِّنَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ شَيْـًۭٔا وَلَا يَسْتَطِيعُونَ
- (17:56) [listed for 1:5] قُلِ ٱدْعُوا۟ ٱلَّذِينَ زَعَمْتُم مِّن دُونِهِۦ فَلَا يَمْلِكُونَ كَشْفَ ٱلضُّرِّ عَنكُمْ وَلَا تَحْوِيلًا
- (17:65) [listed for 1:5] إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌۭ ۚ وَكَفَىٰ بِرَبِّكَ وَكِيلًۭا
- (18:14) [listed for 1:5] وَرَبَطْنَا عَلَىٰ قُلُوبِهِمْ إِذْ قَامُوا۟ فَقَالُوا۟ رَبُّنَا رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ لَن نَّدْعُوَا۟ مِن دُونِهِۦٓ إِلَٰهًۭا ۖ لَّقَدْ قُلْنَآ إِذًۭا شَطَطًا
- (18:26) [listed for 1:5] قُلِ ٱللَّهُ أَعْلَمُ بِمَا لَبِثُوا۟ ۖ لَهُۥ غَيْبُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَبْصِرْ بِهِۦ وَأَسْمِعْ ۚ مَا لَهُم مِّن دُونِهِۦ مِن وَلِىٍّۢ وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا
- (18:65) [listed for 1:5] فَوَجَدَا عَبْدًۭا مِّنْ عِبَادِنَآ ءَاتَيْنَٰهُ رَحْمَةًۭ مِّنْ عِندِنَا وَعَلَّمْنَٰهُ مِن لَّدُنَّا عِلْمًۭا
- (18:102) [listed for 1:5] أَفَحَسِبَ ٱلَّذِينَ كَفَرُوٓا۟ أَن يَتَّخِذُوا۟ عِبَادِى مِن دُونِىٓ أَوْلِيَآءَ ۚ إِنَّآ أَعْتَدْنَا جَهَنَّمَ لِلْكَٰفِرِينَ نُزُلًۭا
- (19:2) [listed for 1:5] ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ
- (22:62) [listed for 1:5] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّ مَا يَدْعُونَ مِن دُونِهِۦ هُوَ ٱلْبَٰطِلُ وَأَنَّ ٱللَّهَ هُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ
- (23:23) [listed for 1:5] وَلَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۖ أَفَلَا تَتَّقُونَ
- (23:32) [listed for 1:5] فَأَرْسَلْنَا فِيهِمْ رَسُولًۭا مِّنْهُمْ أَنِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ ۖ أَفَلَا تَتَّقُونَ
- (25:43) [listed for 1:5] أَرَءَيْتَ مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ أَفَأَنتَ تَكُونُ عَلَيْهِ وَكِيلًا
- (25:55) [listed for 1:5] وَيَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُهُمْ وَلَا يَضُرُّهُمْ ۗ وَكَانَ ٱلْكَافِرُ عَلَىٰ رَبِّهِۦ ظَهِيرًۭا
- (26:22) [listed for 1:5] [cited in ¶6] وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ
- (26:70) [listed for 1:5] إِذْ قَالَ لِأَبِيهِ وَقَوْمِهِۦ مَا تَعْبُدُونَ
- (27:91) [listed for 1:5] إِنَّمَآ أُمِرْتُ أَنْ أَعْبُدَ رَبَّ هَٰذِهِ ٱلْبَلْدَةِ ٱلَّذِى حَرَّمَهَا وَلَهُۥ كُلُّ شَىْءٍۢ ۖ وَأُمِرْتُ أَنْ أَكُونَ مِنَ ٱلْمُسْلِمِينَ
- (29:16) [listed for 1:5] وَإِبْرَٰهِيمَ إِذْ قَالَ لِقَوْمِهِ ٱعْبُدُوا۟ ٱللَّهَ وَٱتَّقُوهُ ۖ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (29:36) [listed for 1:5] وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ وَٱرْجُوا۟ ٱلْيَوْمَ ٱلْءَاخِرَ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (29:56) [listed for 1:5] [cited in ¶3] يَٰعِبَادِىَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ أَرْضِى وَٰسِعَةٌۭ فَإِيَّٰىَ فَٱعْبُدُونِ
- (29:59) [listed for 1:5] ٱلَّذِينَ صَبَرُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (30:30) [listed for 1:5] فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا ۚ فِطْرَتَ ٱللَّهِ ٱلَّتِى فَطَرَ ٱلنَّاسَ عَلَيْهَا ۚ لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (30:33) [listed for 1:5] وَإِذَا مَسَّ ٱلنَّاسَ ضُرٌّۭ دَعَوْا۟ رَبَّهُم مُّنِيبِينَ إِلَيْهِ ثُمَّ إِذَآ أَذَاقَهُم مِّنْهُ رَحْمَةً إِذَا فَرِيقٌۭ مِّنْهُم بِرَبِّهِمْ يُشْرِكُونَ
- (31:13) [listed for 1:5] وَإِذْ قَالَ لُقْمَٰنُ لِٱبْنِهِۦ وَهُوَ يَعِظُهُۥ يَٰبُنَىَّ لَا تُشْرِكْ بِٱللَّهِ ۖ إِنَّ ٱلشِّرْكَ لَظُلْمٌ عَظِيمٌۭ
- (32:16) [listed for 1:5] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (34:22) [listed for 1:5] [cited in ¶19] قُلِ ٱدْعُوا۟ ٱلَّذِينَ زَعَمْتُم مِّن دُونِ ٱللَّهِ ۖ لَا يَمْلِكُونَ مِثْقَالَ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ وَمَا لَهُمْ فِيهِمَا مِن شِرْكٍۢ وَمَا لَهُۥ مِنْهُم مِّن ظَهِيرٍۢ
- (34:41) [listed for 1:5] [cited in ¶3] قَالُوا۟ سُبْحَٰنَكَ أَنتَ وَلِيُّنَا مِن دُونِهِم ۖ بَلْ كَانُوا۟ يَعْبُدُونَ ٱلْجِنَّ ۖ أَكْثَرُهُم بِهِم مُّؤْمِنُونَ
- (35:3) [listed for 1:5] يَٰٓأَيُّهَا ٱلنَّاسُ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ ۚ هَلْ مِنْ خَٰلِقٍ غَيْرُ ٱللَّهِ يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (36:30) [listed for 1:5] يَٰحَسْرَةً عَلَى ٱلْعِبَادِ ۚ مَا يَأْتِيهِم مِّن رَّسُولٍ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (36:74) [listed for 1:5] وَٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ ءَالِهَةًۭ لَّعَلَّهُمْ يُنصَرُونَ
- (37:40) [listed for 1:5] إِلَّا عِبَادَ ٱللَّهِ ٱلْمُخْلَصِينَ
- (37:161) [listed for 1:5] فَإِنَّكُمْ وَمَا تَعْبُدُونَ
- (38:30) [listed for 1:5] وَوَهَبْنَا لِدَاوُۥدَ سُلَيْمَٰنَ ۚ نِعْمَ ٱلْعَبْدُ ۖ إِنَّهُۥٓ أَوَّابٌ
- (39:3) [listed for 1:5] أَلَا لِلَّهِ ٱلدِّينُ ٱلْخَالِصُ ۚ وَٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَآ إِلَى ٱللَّهِ زُلْفَىٰٓ إِنَّ ٱللَّهَ يَحْكُمُ بَيْنَهُمْ فِى مَا هُمْ فِيهِ يَخْتَلِفُونَ ۗ إِنَّ ٱللَّهَ لَا يَهْدِى مَنْ هُوَ كَٰذِبٌۭ كَفَّارٌۭ
- (39:8) [listed for 1:5] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (39:14) [listed for 1:5] [cited in ¶2] قُلِ ٱللَّهَ أَعْبُدُ مُخْلِصًۭا لَّهُۥ دِينِى
- (39:17) [listed for 1:5] وَٱلَّذِينَ ٱجْتَنَبُوا۟ ٱلطَّٰغُوتَ أَن يَعْبُدُوهَا وَأَنَابُوٓا۟ إِلَى ٱللَّهِ لَهُمُ ٱلْبُشْرَىٰ ۚ فَبَشِّرْ عِبَادِ
- (39:38) [listed for 1:5] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلْ أَفَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ إِنْ أَرَادَنِىَ ٱللَّهُ بِضُرٍّ هَلْ هُنَّ كَٰشِفَٰتُ ضُرِّهِۦٓ أَوْ أَرَادَنِى بِرَحْمَةٍ هَلْ هُنَّ مُمْسِكَٰتُ رَحْمَتِهِۦ ۚ قُلْ حَسْبِىَ ٱللَّهُ ۖ عَلَيْهِ يَتَوَكَّلُ ٱلْمُتَوَكِّلُونَ
- (43:15) [listed for 1:5] وَجَعَلُوا۟ لَهُۥ مِنْ عِبَادِهِۦ جُزْءًا ۚ إِنَّ ٱلْإِنسَٰنَ لَكَفُورٌۭ مُّبِينٌ
- (46:4) [listed for 1:5] قُلْ أَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ أَرُونِى مَاذَا خَلَقُوا۟ مِنَ ٱلْأَرْضِ أَمْ لَهُمْ شِرْكٌۭ فِى ٱلسَّمَٰوَٰتِ ۖ ٱئْتُونِى بِكِتَٰبٍۢ مِّن قَبْلِ هَٰذَآ أَوْ أَثَٰرَةٍۢ مِّنْ عِلْمٍ إِن كُنتُمْ صَٰدِقِينَ
- (51:50) [listed for 1:5] فَفِرُّوٓا۟ إِلَى ٱللَّهِ ۖ إِنِّى لَكُم مِّنْهُ نَذِيرٌۭ مُّبِينٌۭ
- (51:56) [listed for 1:5] وَمَا خَلَقْتُ ٱلْجِنَّ وَٱلْإِنسَ إِلَّا لِيَعْبُدُونِ
- (76:6) [listed for 1:5] عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا
- (92:12) [listed for 1:5] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (94:8) [listed for 1:5] وَإِلَىٰ رَبِّكَ فَٱرْغَب
- (106:3) [listed for 1:5] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- (109:3) [listed for 1:5] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- (109:4) [listed for 1:5] وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- (109:6) [listed for 1:5] لَكُمْ دِينُكُمْ وَلِىَ دِينِ

## named by the passage's own list as strong for this ayah (5)

- (2:138) [listed for 1:5] صِبْغَةَ ٱللَّهِ ۖ وَمَنْ أَحْسَنُ مِنَ ٱللَّهِ صِبْغَةًۭ ۖ وَنَحْنُ لَهُۥ عَٰبِدُونَ
- (28:70) [listed for 1:5] وَهُوَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ ۖ وَلَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ
- (71:3) [listed for 1:5] أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱتَّقُوهُ وَأَطِيعُونِ
- (72:2) [listed for 1:5] يَهْدِىٓ إِلَى ٱلرُّشْدِ فَـَٔامَنَّا بِهِۦ ۖ وَلَن نُّشْرِكَ بِرَبِّنَآ أَحَدًۭا
- (98:5) [listed for 1:5] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ

## named by the passage's own list as medium for this ayah (5)

- (15:87) [listed for 1:5] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (15:98) [listed for 1:5] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ ٱلسَّٰجِدِينَ
- (16:53) [listed for 1:5] وَمَا بِكُم مِّن نِّعْمَةٍۢ فَمِنَ ٱللَّهِ ۖ ثُمَّ إِذَا مَسَّكُمُ ٱلضُّرُّ فَإِلَيْهِ تَجْـَٔرُونَ
- (17:42) [listed for 1:5] قُل لَّوْ كَانَ مَعَهُۥٓ ءَالِهَةٌۭ كَمَا يَقُولُونَ إِذًۭا لَّٱبْتَغَوْا۟ إِلَىٰ ذِى ٱلْعَرْشِ سَبِيلًۭا
- (109:5) [listed for 1:5] وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ

## weak (this ayah's own list) (26)

- (2:23) [listed for 1:5] وَإِن كُنتُمْ فِى رَيْبٍۢ مِّمَّا نَزَّلْنَا عَلَىٰ عَبْدِنَا فَأْتُوا۟ بِسُورَةٍۢ مِّن مِّثْلِهِۦ وَٱدْعُوا۟ شُهَدَآءَكُم مِّن دُونِ ٱللَّهِ إِن كُنتُمْ صَٰدِقِينَ
- (2:207) [listed for 1:5] وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
- (3:15) [listed for 1:5] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
- (3:30) [listed for 1:5] يَوْمَ تَجِدُ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ مِنْ خَيْرٍۢ مُّحْضَرًۭا وَمَا عَمِلَتْ مِن سُوٓءٍۢ تَوَدُّ لَوْ أَنَّ بَيْنَهَا وَبَيْنَهُۥٓ أَمَدًۢا بَعِيدًۭا ۗ وَيُحَذِّرُكُمُ ٱللَّهُ نَفْسَهُۥ ۗ وَٱللَّهُ رَءُوفٌۢ بِٱلْعِبَادِ
- (6:18) [listed for 1:5] وَهُوَ ٱلْقَاهِرُ فَوْقَ عِبَادِهِۦ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (8:53) [listed for 1:5] ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًۭا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۙ وَأَنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (16:114) [listed for 1:5] فَكُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ حَلَٰلًۭا طَيِّبًۭا وَٱشْكُرُوا۟ نِعْمَتَ ٱللَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (17:31) [listed for 1:5] وَلَا تَقْتُلُوٓا۟ أَوْلَٰدَكُمْ خَشْيَةَ إِمْلَٰقٍۢ ۖ نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ ۚ إِنَّ قَتْلَهُمْ كَانَ خِطْـًۭٔا كَبِيرًۭا
- (18:95) [listed for 1:5] [cited in ¶18] قَالَ مَا مَكَّنِّى فِيهِ رَبِّى خَيْرٌۭ فَأَعِينُونِى بِقُوَّةٍ أَجْعَلْ بَيْنَكُمْ وَبَيْنَهُمْ رَدْمًا
- (19:91) [listed for 1:5] أَن دَعَوْا۟ لِلرَّحْمَٰنِ وَلَدًۭا
- (20:33) [listed for 1:5] كَىْ نُسَبِّحَكَ كَثِيرًۭا
- (20:34) [listed for 1:5] وَنَذْكُرَكَ كَثِيرًا
- (22:10) [listed for 1:5] ذَٰلِكَ بِمَا قَدَّمَتْ يَدَاكَ وَأَنَّ ٱللَّهَ لَيْسَ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
- (25:1) [listed for 1:5] تَبَارَكَ ٱلَّذِى نَزَّلَ ٱلْفُرْقَانَ عَلَىٰ عَبْدِهِۦ لِيَكُونَ لِلْعَٰلَمِينَ نَذِيرًا
- (29:60) [listed for 1:5] وَكَأَيِّن مِّن دَآبَّةٍۢ لَّا تَحْمِلُ رِزْقَهَا ٱللَّهُ يَرْزُقُهَا وَإِيَّاكُمْ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (29:62) [listed for 1:5] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥٓ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (33:56) [listed for 1:5] إِنَّ ٱللَّهَ وَمَلَٰٓئِكَتَهُۥ يُصَلُّونَ عَلَى ٱلنَّبِىِّ ۚ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ صَلُّوا۟ عَلَيْهِ وَسَلِّمُوا۟ تَسْلِيمًا
- (37:81) [listed for 1:5] إِنَّهُۥ مِنْ عِبَادِنَا ٱلْمُؤْمِنِينَ
- (37:111) [listed for 1:5] إِنَّهُۥ مِنْ عِبَادِنَا ٱلْمُؤْمِنِينَ
- (37:122) [listed for 1:5] إِنَّهُمَا مِنْ عِبَادِنَا ٱلْمُؤْمِنِينَ
- (37:132) [listed for 1:5] إِنَّهُۥ مِنْ عِبَادِنَا ٱلْمُؤْمِنِينَ
- (47:19) [listed for 1:5] فَٱعْلَمْ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا ٱللَّهُ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَلِلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ۗ وَٱللَّهُ يَعْلَمُ مُتَقَلَّبَكُمْ وَمَثْوَىٰكُمْ
- (50:29) [listed for 1:5] مَا يُبَدَّلُ ٱلْقَوْلُ لَدَىَّ وَمَآ أَنَا۠ بِظَلَّٰمٍۢ لِّلْعَبِيدِ
- (75:17) [listed for 1:5] إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ
- (106:4) [listed for 1:5] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ
- (109:1) [listed for 1:5] قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ

## named by the passage's own list as weak for this ayah (1)

- (25:4) [listed for 1:5] وَقَالَ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ هَٰذَآ إِلَّآ إِفْكٌ ٱفْتَرَىٰهُ وَأَعَانَهُۥ عَلَيْهِ قَوْمٌ ءَاخَرُونَ ۖ فَقَدْ جَآءُو ظُلْمًۭا وَزُورًۭا

## neighbours: within two ayat of a passage the commentary cites (106)

- (2:43) [next to 2:45] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ
- (2:44) [next to 2:45] ۞ أَتَأْمُرُونَ ٱلنَّاسَ بِٱلْبِرِّ وَتَنسَوْنَ أَنفُسَكُمْ وَأَنتُمْ تَتْلُونَ ٱلْكِتَٰبَ ۚ أَفَلَا تَعْقِلُونَ
- (2:46) [next to 2:45] ٱلَّذِينَ يَظُنُّونَ أَنَّهُم مُّلَٰقُوا۟ رَبِّهِمْ وَأَنَّهُمْ إِلَيْهِ رَٰجِعُونَ
- (2:47) [next to 2:45] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:151) [next to 2:153] كَمَآ أَرْسَلْنَا فِيكُمْ رَسُولًۭا مِّنكُمْ يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِنَا وَيُزَكِّيكُمْ وَيُعَلِّمُكُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (2:152) [next to 2:153] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
- (2:154) [next to 2:153] وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۢ ۚ بَلْ أَحْيَآءٌۭ وَلَٰكِن لَّا تَشْعُرُونَ
- (2:155) [next to 2:153] وَلَنَبْلُوَنَّكُم بِشَىْءٍۢ مِّنَ ٱلْخَوْفِ وَٱلْجُوعِ وَنَقْصٍۢ مِّنَ ٱلْأَمْوَٰلِ وَٱلْأَنفُسِ وَٱلثَّمَرَٰتِ ۗ وَبَشِّرِ ٱلصَّٰبِرِينَ
- (3:62) [next to 3:64] إِنَّ هَٰذَا لَهُوَ ٱلْقَصَصُ ٱلْحَقُّ ۚ وَمَا مِنْ إِلَٰهٍ إِلَّا ٱللَّهُ ۚ وَإِنَّ ٱللَّهَ لَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (3:63) [next to 3:64] فَإِن تَوَلَّوْا۟ فَإِنَّ ٱللَّهَ عَلِيمٌۢ بِٱلْمُفْسِدِينَ
- (3:65) [next to 3:64] يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تُحَآجُّونَ فِىٓ إِبْرَٰهِيمَ وَمَآ أُنزِلَتِ ٱلتَّوْرَىٰةُ وَٱلْإِنجِيلُ إِلَّا مِنۢ بَعْدِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (3:66) [next to 3:64] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ حَٰجَجْتُمْ فِيمَا لَكُم بِهِۦ عِلْمٌۭ فَلِمَ تُحَآجُّونَ فِيمَا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ ۚ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (5:0) [next to 5:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (5:1) [next to 5:2] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَوْفُوا۟ بِٱلْعُقُودِ ۚ أُحِلَّتْ لَكُم بَهِيمَةُ ٱلْأَنْعَٰمِ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ غَيْرَ مُحِلِّى ٱلصَّيْدِ وَأَنتُمْ حُرُمٌ ۗ إِنَّ ٱللَّهَ يَحْكُمُ مَا يُرِيدُ
- (5:3) [next to 5:2] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (5:4) [next to 5:2] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (6:151) [next to 6:153] ۞ قُلْ تَعَالَوْا۟ أَتْلُ مَا حَرَّمَ رَبُّكُمْ عَلَيْكُمْ ۖ أَلَّا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا ۖ وَلَا تَقْتُلُوٓا۟ أَوْلَٰدَكُم مِّنْ إِمْلَٰقٍۢ ۖ نَّحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ ۖ وَلَا تَقْرَبُوا۟ ٱلْفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ ۖ وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
- (6:152) [next to 6:153] وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۖ وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَا ۖ وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ ۖ وَبِعَهْدِ ٱللَّهِ أَوْفُوا۟ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَذَكَّرُونَ
- (6:154) [next to 6:153] ثُمَّ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ تَمَامًا عَلَى ٱلَّذِىٓ أَحْسَنَ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُم بِلِقَآءِ رَبِّهِمْ يُؤْمِنُونَ
- (6:155) [next to 6:153] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ فَٱتَّبِعُوهُ وَٱتَّقُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (7:125) [next to 7:127] قَالُوٓا۟ إِنَّآ إِلَىٰ رَبِّنَا مُنقَلِبُونَ
- (7:126) [next to 7:127] وَمَا تَنقِمُ مِنَّآ إِلَّآ أَنْ ءَامَنَّا بِـَٔايَٰتِ رَبِّنَا لَمَّا جَآءَتْنَا ۚ رَبَّنَآ أَفْرِغْ عَلَيْنَا صَبْرًۭا وَتَوَفَّنَا مُسْلِمِينَ
- (7:129) [next to 7:127] قَالُوٓا۟ أُوذِينَا مِن قَبْلِ أَن تَأْتِيَنَا وَمِنۢ بَعْدِ مَا جِئْتَنَا ۚ قَالَ عَسَىٰ رَبُّكُمْ أَن يُهْلِكَ عَدُوَّكُمْ وَيَسْتَخْلِفَكُمْ فِى ٱلْأَرْضِ فَيَنظُرَ كَيْفَ تَعْمَلُونَ
- (7:130) [next to 7:128] وَلَقَدْ أَخَذْنَآ ءَالَ فِرْعَوْنَ بِٱلسِّنِينَ وَنَقْصٍۢ مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَذَّكَّرُونَ
- (11:121) [next to 11:123] وَقُل لِّلَّذِينَ لَا يُؤْمِنُونَ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنَّا عَٰمِلُونَ
- (11:122) [next to 11:123] وَٱنتَظِرُوٓا۟ إِنَّا مُنتَظِرُونَ
- (12:15) [next to 12:17] فَلَمَّا ذَهَبُوا۟ بِهِۦ وَأَجْمَعُوٓا۟ أَن يَجْعَلُوهُ فِى غَيَٰبَتِ ٱلْجُبِّ ۚ وَأَوْحَيْنَآ إِلَيْهِ لَتُنَبِّئَنَّهُم بِأَمْرِهِمْ هَٰذَا وَهُمْ لَا يَشْعُرُونَ
- (12:16) [next to 12:17] وَجَآءُوٓ أَبَاهُمْ عِشَآءًۭ يَبْكُونَ
- (12:19) [next to 12:17] وَجَآءَتْ سَيَّارَةٌۭ فَأَرْسَلُوا۟ وَارِدَهُمْ فَأَدْلَىٰ دَلْوَهُۥ ۖ قَالَ يَٰبُشْرَىٰ هَٰذَا غُلَٰمٌۭ ۚ وَأَسَرُّوهُ بِضَٰعَةًۭ ۚ وَٱللَّهُ عَلِيمٌۢ بِمَا يَعْمَلُونَ
- (12:20) [next to 12:18] وَشَرَوْهُ بِثَمَنٍۭ بَخْسٍۢ دَرَٰهِمَ مَعْدُودَةٍۢ وَكَانُوا۟ فِيهِ مِنَ ٱلزَّٰهِدِينَ
- (12:37) [next to 12:39] قَالَ لَا يَأْتِيكُمَا طَعَامٌۭ تُرْزَقَانِهِۦٓ إِلَّا نَبَّأْتُكُمَا بِتَأْوِيلِهِۦ قَبْلَ أَن يَأْتِيَكُمَا ۚ ذَٰلِكُمَا مِمَّا عَلَّمَنِى رَبِّىٓ ۚ إِنِّى تَرَكْتُ مِلَّةَ قَوْمٍۢ لَّا يُؤْمِنُونَ بِٱللَّهِ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (12:38) [next to 12:39] وَٱتَّبَعْتُ مِلَّةَ ءَابَآءِىٓ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ ۚ مَا كَانَ لَنَآ أَن نُّشْرِكَ بِٱللَّهِ مِن شَىْءٍۢ ۚ ذَٰلِكَ مِن فَضْلِ ٱللَّهِ عَلَيْنَا وَعَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (12:41) [next to 12:39] يَٰصَىٰحِبَىِ ٱلسِّجْنِ أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا ۖ وَأَمَّا ٱلْءَاخَرُ فَيُصْلَبُ فَتَأْكُلُ ٱلطَّيْرُ مِن رَّأْسِهِۦ ۚ قُضِىَ ٱلْأَمْرُ ٱلَّذِى فِيهِ تَسْتَفْتِيَانِ
- (12:42) [next to 12:40] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (15:38) [next to 15:40] إِلَىٰ يَوْمِ ٱلْوَقْتِ ٱلْمَعْلُومِ
- (15:39) [next to 15:40] قَالَ رَبِّ بِمَآ أَغْوَيْتَنِى لَأُزَيِّنَنَّ لَهُمْ فِى ٱلْأَرْضِ وَلَأُغْوِيَنَّهُمْ أَجْمَعِينَ
- (15:41) [next to 15:40] قَالَ هَٰذَا صِرَٰطٌ عَلَىَّ مُسْتَقِيمٌ
- (15:43) [next to 15:42] وَإِنَّ جَهَنَّمَ لَمَوْعِدُهُمْ أَجْمَعِينَ
- (15:44) [next to 15:42] لَهَا سَبْعَةُ أَبْوَٰبٍۢ لِّكُلِّ بَابٍۢ مِّنْهُمْ جُزْءٌۭ مَّقْسُومٌ
- (16:66) [next to 16:68] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ
- (16:67) [next to 16:68] وَمِن ثَمَرَٰتِ ٱلنَّخِيلِ وَٱلْأَعْنَٰبِ تَتَّخِذُونَ مِنْهُ سَكَرًۭا وَرِزْقًا حَسَنًا ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَعْقِلُونَ
- (16:70) [next to 16:68] وَٱللَّهُ خَلَقَكُمْ ثُمَّ يَتَوَفَّىٰكُمْ ۚ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَىْ لَا يَعْلَمَ بَعْدَ عِلْمٍۢ شَيْـًٔا ۚ إِنَّ ٱللَّهَ عَلِيمٌۭ قَدِيرٌۭ
- (16:71) [next to 16:69] وَٱللَّهُ فَضَّلَ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ فِى ٱلرِّزْقِ ۚ فَمَا ٱلَّذِينَ فُضِّلُوا۟ بِرَآدِّى رِزْقِهِمْ عَلَىٰ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَهُمْ فِيهِ سَوَآءٌ ۚ أَفَبِنِعْمَةِ ٱللَّهِ يَجْحَدُونَ
- (17:109) [next to 17:111] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
- (17:110) [next to 17:111] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (18:92) [next to 18:94] ثُمَّ أَتْبَعَ سَبَبًا
- (18:93) [next to 18:94] حَتَّىٰٓ إِذَا بَلَغَ بَيْنَ ٱلسَّدَّيْنِ وَجَدَ مِن دُونِهِمَا قَوْمًۭا لَّا يَكَادُونَ يَفْقَهُونَ قَوْلًۭا
- (18:96) [next to 18:94] ءَاتُونِى زُبَرَ ٱلْحَدِيدِ ۖ حَتَّىٰٓ إِذَا سَاوَىٰ بَيْنَ ٱلصَّدَفَيْنِ قَالَ ٱنفُخُوا۟ ۖ حَتَّىٰٓ إِذَا جَعَلَهُۥ نَارًۭا قَالَ ءَاتُونِىٓ أُفْرِغْ عَلَيْهِ قِطْرًۭا
- (18:97) [next to 18:95] فَمَا ٱسْطَٰعُوٓا۟ أَن يَظْهَرُوهُ وَمَا ٱسْتَطَٰعُوا۟ لَهُۥ نَقْبًۭا
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (19:67) [next to 19:65] أَوَلَا يَذْكُرُ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن قَبْلُ وَلَمْ يَكُ شَيْـًۭٔا
- (19:92) [next to 19:93] وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا
- (19:94) [next to 19:93] لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا
- (19:95) [next to 19:93] وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا
- (21:107) [next to 21:109] وَمَآ أَرْسَلْنَٰكَ إِلَّا رَحْمَةًۭ لِّلْعَٰلَمِينَ
- (21:108) [next to 21:109] قُلْ إِنَّمَا يُوحَىٰٓ إِلَىَّ أَنَّمَآ إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۖ فَهَلْ أَنتُم مُّسْلِمُونَ
- (21:110) [next to 21:109] إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ
- (21:111) [next to 21:109] وَإِنْ أَدْرِى لَعَلَّهُۥ فِتْنَةٌۭ لَّكُمْ وَمَتَٰعٌ إِلَىٰ حِينٍۢ
- (23:44) [next to 23:46] ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا ۖ كُلَّ مَا جَآءَ أُمَّةًۭ رَّسُولُهَا كَذَّبُوهُ ۚ فَأَتْبَعْنَا بَعْضَهُم بَعْضًۭا وَجَعَلْنَٰهُمْ أَحَادِيثَ ۚ فَبُعْدًۭا لِّقَوْمٍۢ لَّا يُؤْمِنُونَ
- (23:45) [next to 23:46] ثُمَّ أَرْسَلْنَا مُوسَىٰ وَأَخَاهُ هَٰرُونَ بِـَٔايَٰتِنَا وَسُلْطَٰنٍۢ مُّبِينٍ
- (23:48) [next to 23:46] فَكَذَّبُوهُمَا فَكَانُوا۟ مِنَ ٱلْمُهْلَكِينَ
- (23:49) [next to 23:47] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ لَعَلَّهُمْ يَهْتَدُونَ
- (26:16) [next to 26:18] فَأْتِيَا فِرْعَوْنَ فَقُولَآ إِنَّا رَسُولُ رَبِّ ٱلْعَٰلَمِينَ
- (26:17) [next to 26:18] أَنْ أَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ
- (26:19) [next to 26:18] وَفَعَلْتَ فَعْلَتَكَ ٱلَّتِى فَعَلْتَ وَأَنتَ مِنَ ٱلْكَٰفِرِينَ
- (26:20) [next to 26:18] قَالَ فَعَلْتُهَآ إِذًۭا وَأَنَا۠ مِنَ ٱلضَّآلِّينَ
- (26:21) [next to 26:22] فَفَرَرْتُ مِنكُمْ لَمَّا خِفْتُكُمْ فَوَهَبَ لِى رَبِّى حُكْمًۭا وَجَعَلَنِى مِنَ ٱلْمُرْسَلِينَ
- (26:23) [next to 26:22] قَالَ فِرْعَوْنُ وَمَا رَبُّ ٱلْعَٰلَمِينَ
- (26:24) [next to 26:22] قَالَ رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَآ ۖ إِن كُنتُم مُّوقِنِينَ
- (28:13) [next to 28:15] فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا وَلَا تَحْزَنَ وَلِتَعْلَمَ أَنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَلَٰكِنَّ أَكْثَرَهُمْ لَا يَعْلَمُونَ
- (28:14) [next to 28:15] وَلَمَّا بَلَغَ أَشُدَّهُۥ وَٱسْتَوَىٰٓ ءَاتَيْنَٰهُ حُكْمًۭا وَعِلْمًۭا ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُحْسِنِينَ
- (28:18) [next to 28:16] فَأَصْبَحَ فِى ٱلْمَدِينَةِ خَآئِفًۭا يَتَرَقَّبُ فَإِذَا ٱلَّذِى ٱسْتَنصَرَهُۥ بِٱلْأَمْسِ يَسْتَصْرِخُهُۥ ۚ قَالَ لَهُۥ مُوسَىٰٓ إِنَّكَ لَغَوِىٌّۭ مُّبِينٌۭ
- (28:19) [next to 28:17] فَلَمَّآ أَنْ أَرَادَ أَن يَبْطِشَ بِٱلَّذِى هُوَ عَدُوٌّۭ لَّهُمَا قَالَ يَٰمُوسَىٰٓ أَتُرِيدُ أَن تَقْتُلَنِى كَمَا قَتَلْتَ نَفْسًۢا بِٱلْأَمْسِ ۖ إِن تُرِيدُ إِلَّآ أَن تَكُونَ جَبَّارًۭا فِى ٱلْأَرْضِ وَمَا تُرِيدُ أَن تَكُونَ مِنَ ٱلْمُصْلِحِينَ
- (29:54) [next to 29:56] يَسْتَعْجِلُونَكَ بِٱلْعَذَابِ وَإِنَّ جَهَنَّمَ لَمُحِيطَةٌۢ بِٱلْكَٰفِرِينَ
- (29:55) [next to 29:56] يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ وَيَقُولُ ذُوقُوا۟ مَا كُنتُمْ تَعْمَلُونَ
- (29:57) [next to 29:56] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۖ ثُمَّ إِلَيْنَا تُرْجَعُونَ
- (29:58) [next to 29:56] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (34:20) [next to 34:22] وَلَقَدْ صَدَّقَ عَلَيْهِمْ إِبْلِيسُ ظَنَّهُۥ فَٱتَّبَعُوهُ إِلَّا فَرِيقًۭا مِّنَ ٱلْمُؤْمِنِينَ
- (34:21) [next to 34:22] وَمَا كَانَ لَهُۥ عَلَيْهِم مِّن سُلْطَٰنٍ إِلَّا لِنَعْلَمَ مَن يُؤْمِنُ بِٱلْءَاخِرَةِ مِمَّنْ هُوَ مِنْهَا فِى شَكٍّۢ ۗ وَرَبُّكَ عَلَىٰ كُلِّ شَىْءٍ حَفِيظٌۭ
- (34:23) [next to 34:22] وَلَا تَنفَعُ ٱلشَّفَٰعَةُ عِندَهُۥٓ إِلَّا لِمَنْ أَذِنَ لَهُۥ ۚ حَتَّىٰٓ إِذَا فُزِّعَ عَن قُلُوبِهِمْ قَالُوا۟ مَاذَا قَالَ رَبُّكُمْ ۖ قَالُوا۟ ٱلْحَقَّ ۖ وَهُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ
- (34:24) [next to 34:22] ۞ قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُلِ ٱللَّهُ ۖ وَإِنَّآ أَوْ إِيَّاكُمْ لَعَلَىٰ هُدًى أَوْ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (34:38) [next to 34:40] وَٱلَّذِينَ يَسْعَوْنَ فِىٓ ءَايَٰتِنَا مُعَٰجِزِينَ أُو۟لَٰٓئِكَ فِى ٱلْعَذَابِ مُحْضَرُونَ
- (34:39) [next to 34:40] قُلْ إِنَّ رَبِّى يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥ ۚ وَمَآ أَنفَقْتُم مِّن شَىْءٍۢ فَهُوَ يُخْلِفُهُۥ ۖ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ
- (34:42) [next to 34:40] فَٱلْيَوْمَ لَا يَمْلِكُ بَعْضُكُمْ لِبَعْضٍۢ نَّفْعًۭا وَلَا ضَرًّۭا وَنَقُولُ لِلَّذِينَ ظَلَمُوا۟ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ
- (34:43) [next to 34:41] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ قَالُوا۟ مَا هَٰذَآ إِلَّا رَجُلٌۭ يُرِيدُ أَن يَصُدَّكُمْ عَمَّا كَانَ يَعْبُدُ ءَابَآؤُكُمْ وَقَالُوا۟ مَا هَٰذَآ إِلَّآ إِفْكٌۭ مُّفْتَرًۭى ۚ وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لِلْحَقِّ لَمَّا جَآءَهُمْ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ
- (36:58) [next to 36:60] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (36:59) [next to 36:60] وَٱمْتَٰزُوا۟ ٱلْيَوْمَ أَيُّهَا ٱلْمُجْرِمُونَ
- (36:62) [next to 36:60] وَلَقَدْ أَضَلَّ مِنكُمْ جِبِلًّۭا كَثِيرًا ۖ أَفَلَمْ تَكُونُوا۟ تَعْقِلُونَ
- (36:63) [next to 36:61] هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى كُنتُمْ تُوعَدُونَ
- (39:9) [next to 39:11] أَمَّنْ هُوَ قَٰنِتٌ ءَانَآءَ ٱلَّيْلِ سَاجِدًۭا وَقَآئِمًۭا يَحْذَرُ ٱلْءَاخِرَةَ وَيَرْجُوا۟ رَحْمَةَ رَبِّهِۦ ۗ قُلْ هَلْ يَسْتَوِى ٱلَّذِينَ يَعْلَمُونَ وَٱلَّذِينَ لَا يَعْلَمُونَ ۗ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:10) [next to 39:11] قُلْ يَٰعِبَادِ ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ رَبَّكُمْ ۚ لِلَّذِينَ أَحْسَنُوا۟ فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةٌۭ ۗ وَأَرْضُ ٱللَّهِ وَٰسِعَةٌ ۗ إِنَّمَا يُوَفَّى ٱلصَّٰبِرُونَ أَجْرَهُم بِغَيْرِ حِسَابٍۢ
- (39:12) [next to 39:11] وَأُمِرْتُ لِأَنْ أَكُونَ أَوَّلَ ٱلْمُسْلِمِينَ
- (39:13) [next to 39:11] قُلْ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (39:16) [next to 39:14] لَهُم مِّن فَوْقِهِمْ ظُلَلٌۭ مِّنَ ٱلنَّارِ وَمِن تَحْتِهِمْ ظُلَلٌۭ ۚ ذَٰلِكَ يُخَوِّفُ ٱللَّهُ بِهِۦ عِبَادَهُۥ ۚ يَٰعِبَادِ فَٱتَّقُونِ
- (67:13) [next to 67:15] وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (67:14) [next to 67:15] أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ
- (67:16) [next to 67:15] ءَأَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يَخْسِفَ بِكُمُ ٱلْأَرْضَ فَإِذَا هِىَ تَمُورُ
- (67:17) [next to 67:15] أَمْ أَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا ۖ فَسَتَعْلَمُونَ كَيْفَ نَذِيرِ
- (89:20) [next to 89:22] وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- (89:21) [next to 89:22] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- (89:23) [next to 89:22] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (89:24) [next to 89:22] يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- (89:25) [next to 89:27] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- (89:26) [next to 89:27] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ

