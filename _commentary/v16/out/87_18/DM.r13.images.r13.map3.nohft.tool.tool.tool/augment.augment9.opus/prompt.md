Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:18; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_18/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_18.reading.tr.md (prose paragraphs numbered) =====
## Söz yeni değil: vurgu ve "bu"

[¶1] On sekizinci ayet kısa bir hükümdür: {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâzâ le-fi's-suhufi'l-ûlâ, gloss:bu, elbette ilk sayfalarda vardır, source:87:18}. Cümle iki kez pekiştirilmiştir. Başta "inne" (şüphesiz) vardır, haberin önünde de "le" (elbette) durur. Arapçada bu çift vurgu, karşısında bir kuşku ya da itiraz sezilen söze uyar. Kuşkunun nereden geldiğini bir önceki iki ayet gösterir. Konuşma orada birden dinleyenlere döner: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'sirûne'l-hayâte'd-dunyâ, gloss:hayır, siz dünya hayatını öne koyuyorsunuz, source:87:16}, {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Yakın hayatı öne koyan birine "sonra gelen daha iyidir" denince ilk cevabı bellidir: Bu yeni bir laftır, bu adamın kendi sözüdür. Ayet bu cevabı daha söylenmeden karşılar. Söz yeni değildir, en eski sayfalarda yazılıdır. Ardından gelen son ayet de bu sayfaların kime verildiğini söyler: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi ibrâhîme ve mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}.

[¶2] "Hâzâ" (bu) yakındakini gösterir, az önce söylenmiş olanı işaret eder. En yakında duran söz on dördüncü ayetten on yedinci ayete kadar uzanır: {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad efleha men tezekkâ, gloss:kendini arıtan kurtuldu, source:87:14}, Rabbinin adını anıp namaz kılan kişi, dünyayı öne koyanlar ve daha hayırlı, daha kalıcı olan ahiret. İşaret bütün sureyi de kapsayabilir, dil buna da izin verir. Ama Kur'an aynı sayfaların içinden başka bir yerde de cümleler aktarır ve bu cümleler en yakın okumayı destekler. Necm suresinde Kur'an yüz çeviren birini gösterir: {ar:أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ, tr:e-fe-raeyte'llezî tevellâ, gloss:yüz çevireni gördün mü, source:53:33}, {ar:وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ, tr:ve a'tâ kalîlen ve ekdâ, gloss:azıcık verdi, sonra elini kesti, source:53:34}. Sonra sorar: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bi-mâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarında olan ona haber verilmedi mi, source:53:36}, {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'llezî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in sayfalarında olan, source:53:37}. Sayfaların söylediği de arkasından gelir: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}, {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ se'â, gloss:insana kendi çabasından başkası yoktur, source:53:39}, {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:çabası da ileride görülecektir, source:53:40}, {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}.

[¶3] Bu cümleler surenin son bölümüyle aynı şeyi söyler. On dördüncü ayetteki arınma dönüşlü bir fiille anlatılır: Kişi kendini arıtır, başkası onu arıtmaz. Necm'deki sayfalar da kimsenin başkasının yükünü taşımadığını söyler. Ahiretin daha kalıcı olması, varışın Rabbe olmasının öbür yüzüdür. İki yerde de sayfalar sırt çeviren birine karşı tanık olarak çağrılır. Necm'de bu kişi yüz çevirir. Burada da en bedbaht olan öğütten uzak durur: {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht olan ondan kaçınır, source:87:11}.

[¶4] Kur'an bu cümle kalıbını kendisi için de kullanır. Şuara suresinde Kur'an'ın Âlemlerin Rabbinin indirdiği söz olduğu söylenir. Onu güvenilir ruhun Peygamber'in kalbine apaçık bir Arapçayla indirdiği anlatılır. Ardından şu gelir: {ar:وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ, tr:ve innehû le-fî zuburi'l-evvelîn, gloss:o, elbette öncekilerin yazılarında da vardır, source:26:196}. Cümlenin iskeleti burada da aynıdır: vurgu, "le", "içinde" ve "ilkler". Sonraki ayet bunun neye yaradığını söyler: {ar:أَوَلَمْ يَكُن لَّهُمْ ءَايَةً أَن يَعْلَمَهُۥ عُلَمَٰٓؤُا۟ بَنِىٓ إِسْرَٰٓءِيلَ, tr:e-ve lem yekun lehum âyeten en ya'lemehû ulemâu benî isrâîl, gloss:İsrailoğullarının bilginlerinin onu bilmesi onlar için bir işaret değil mi, source:26:197}. Yeni sözün eski yazıların içinde bulunması onun kimlik belgesidir. Söz kendini yeni bir buluş olarak sunmaz, önceden bilinen bir şeyin dönüşü olarak sunar.

## Sayfa: serilmiş, açık yüzey

[¶5] Ayetteki "suhuf", tek bir "sahîfe"nin çoğuludur. Araplar sahîfe derken üzerine yazı yazılan bir deri parçasını anlardı: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıt'atu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhufun teki sahîfedir, üzerine yazı yazılan ak deri ya da parşömen parçası, source:"ص ح ف,B002"}. Türkçedeki "sayfa" bu kelimeden gelir, ama anlamı daralmıştır. Bugün ciltli bir kitabın numaralı bir yüzü demektir. Arapçadaki sahîfe ise başlı başına bir yazı parçasıdır. Tek başına bir mektup ya da bir belge olabilir ve ciltten önce gelir. Ayetteki "ilk sayfalar" birbirine dikilmiş bir kitabın yaprakları olarak değil, ayrı ayrı yazılmış deri parçaları olarak duyulmalıdır.

[¶6] Kelimenin ailesi bu yaprağın nasıl bir nesne olduğunu da gösterir. Bu aile resimleri ayetteki "yazılı sayfalar" anlamının yanında duyulur, onun yerine geçmez. Kökün temelinde yayılmışlık ve genişlik vardır: {ar:أصل صحيح يدل على انبساط في شيء وسعة, tr:aslun sahîhun yedullu alâ inbisâtin fî şey'in ve se'a, gloss:bir şeydeki yayılmışlığı ve genişliği gösteren sağlam bir kök, source:"ص ح ف,B001"}. Yeryüzünün görünen yüzüne {ar:الصحيف وجه الأرض, tr:es-sahîfu vechu'l-ard, gloss:sahîf yeryüzünün yüzüdür, source:"ص ح ف,B001"} denirdi. İnsan yüzünün derisi de "yüzün sahîfesi" diye anılırdı: {ar:صحيفة الوجه بشرة جلده, tr:sahîfetu'l-vechi beşeratu cildih, gloss:yüzün sahîfesi derisinin dış yüzüdür, source:"ص ح ف,B001"}. Bir başka tanım bu kullanımları birleştirir: {ar:الصحيفة المبسوط من الشيء كصحيفة الوجه, tr:es-sahîfetu'l-mebsûtu mine'ş-şey' ke-sahîfeti'l-vech, gloss:sahîfe, bir şeyin yayılıp serilmiş kısmıdır, yüzün sahîfesi gibi, source:"ص ح ف,B001"}. Yazı yaprağının işi budur. Deri gerilir, düzleştirilir ve üzerine yazılan bir bakışta görünecek biçimde açılır. Katlanmış bir şey değildir. Yüz nasıl taşıdığını gösterirse yaprak da taşıdığını gösterir.

[¶7] Bu resim ayetin iddiasına bir renk katar. Dünyanın değil ahiretin, yakının değil sonrakinin seçilmesi gerektiği gizli bir bilgi olarak saklanmamıştır. En eski zamanlardan beri gerilmiş, açık yüzeylere yazılmıştır. Kur'an başka bir yerde, eksik olanın açık bir yaprak olmadığını da söyler. Müddessir suresinde öğütten kaçan inkârcılar anlatılır: {ar:بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ, tr:bel yurîdu kullu'mriin minhum en yu'tâ suhufen muneşşera, gloss:hayır, her biri kendisine açılıp serilmiş sayfalar verilmesini istiyor, source:74:52}. Cevap hemen gelir: {ar:كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ, tr:kellâ bel lâ yehâfûne'l-âhira, gloss:hayır, onlar ahiretten korkmuyorlar, source:74:53}. Sonra: {ar:كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ, tr:kellâ innehû tezkira, gloss:hayır, bu bir öğüttür, source:74:54}, {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:74:55}. Açık yapraklar zaten vardır. Eksik olan korkudur. Bu sure de aynı şeyi söyler: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}. Yeni bir yaprak istemek, eski yaprakların açıklığından kaçmanın bir yoludur.

[¶8] Ayetteki kelime çoğuldur: İki peygamberin birçok yaprağı. Bir araya toplanmış yapraklara "mushaf" denirdi: {ar:المصحف لأنه صحف جمعت, tr:el-mushafu li-ennehû suhufun cumi'at, gloss:mushafa bu ad verilir çünkü o, toplanmış sayfalardır, source:"ص ح ف,B003"}. Ayet yaprakları bir cilt içinde toplamaz, onları dağınık ve eski haliyle anar. Bu dağınık yaprakları bir araya getiren şey, altıncı ayetteki "okutacağız" fiilinin toplamayla kurduğu sahnedir. Surenin okumayla sayfa arasında kurduğu bu bağ o ayetin kelimeleriyle taşınır.

## Sayfaya bakmadan okunan sayfalar

[¶9] Ayetin kurduğu durumda ince bir nokta vardır. Söz sayfalardadır, ama Peygamber'in eline bir sayfa verilmez. Ona verilen şey okutmadır: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Kur'an bu ayrımı başka bir yerde açıkça yapar. Ankebut suresinde Allah Peygamber'e şöyle der: {ar:وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ ۖ إِذًۭا لَّٱرْتَابَ ٱلْمُبْطِلُونَ, tr:ve mâ kunte tetlû min kablihî min kitâbin ve lâ tehuttuhû bi-yemînik izen le'rtâbe'l-mubtilûn, gloss:sen bundan önce hiçbir kitap okumuyordun, onu sağ elinle de yazmıyordun; öyle olsaydı batıla sapanlar şüpheye düşerdi, source:29:48}. Eski sayfalardaki söz Peygamber'e sayfalardan okunarak ulaşmaz, işitilerek ulaşır. "İlk sayfalarda vardır" cümlesinin tanıklık gücü de buradan gelir. Sayfaları okumamış birinin ağzından sayfalardaki söz çıkmaktadır.

[¶10] Beyyine suresi bu durumu tek bir cümleye sığdırır. Ehl-i kitaptan ve müşriklerden inkâr edenlerin açık bir delil gelinceye kadar yerlerinden ayrılmayacakları söylenir: {ar:لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ, tr:lem yekuni'llezîne keferû min ehli'l-kitâbi ve'l-muşrikîne munfekkîne hattâ te'tiyehumu'l-beyyine, gloss:ehl-i kitaptan ve müşriklerden inkâr edenler, açık delil kendilerine gelinceye kadar ayrılacak değillerdi, source:98:1}. Açık delilin ne olduğu da söylenir: {ar:رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ, tr:rasûlun mina'llâhi yetlû suhufen mutahhara, gloss:Allah'tan bir elçi, arınmış sayfalar okuyor, source:98:2}, {ar:فِيهَا كُتُبٌۭ قَيِّمَةٌۭ, tr:fîhâ kutubun kayyime, gloss:içlerinde dosdoğru yazılar var, source:98:3}. Elçi sayfaları okur, ama okunan sayfalar onun sesindedir. Sayfaların dışarıdaki bir arşivde değil, okuyuşun içinde bulunduğu bir durumdur bu. Bu surede sayfalar ayetin sonunda anılır, okutma ise altıncı ayette. Bu ikisi aynı olayın iki ucudur: Allah'ın okuttuğu söz, ilk yaprakların içeriğini sesle yeniden ortaya koyar.

## Taha'nın sonunda aynı yol

[¶11] Kur'an'da "ilk sayfalar" ifadesi bir yerde daha geçer ve orada da bu surenin yolu adım adım tekrarlanır. Taha suresinin sonunda Allah Peygamber'e inkârcıların sözlerine sabretmesini ve tesbih etmesini söyler: {ar:فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ, tr:fasbir alâ mâ yekûlûne ve sebbih bi-hamdi rabbik, gloss:söylediklerine sabret ve Rabbini överek tesbih et, source:20:130}. Bu, surenin ilk ayetindeki emirdir. Sonra dünya hayatının çiçeğine göz dikmemesi istenir ve şöyle denir: {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike hayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131}. Bu, on altıncı ve on yedinci ayetlerin karşıtlığıdır ve hatta aynı iki kelimeyle söylenir. Ardından namaz gelir: {ar:وَأْمُرْ أَهْلَكَ بِٱلصَّلَوٰةِ وَٱصْطَبِرْ عَلَيْهَا, tr:ve'mur ehleke bi's-salâti vastabir aleyhâ, gloss:ailene namazı emret ve ona sabırla devam et, source:20:132}. Bu da on beşinci ayetteki namazdır. Aynı ayet {ar:وَٱلْعَٰقِبَةُ لِلتَّقْوَىٰ, tr:ve'l-âkıbetu li't-takvâ, gloss:sonuç sakınanındır, source:20:132} diye biter. En sonda inkârcıların itirazı ve cevabı yer alır: {ar:وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:ve kâlû levlâ ye'tînâ bi-âyetin min rabbih e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:"Bize Rabbinden bir işaret getirse ya!" dediler; ilk sayfalarda olanın açık delili onlara gelmedi mi, source:20:133}.

[¶12] İki surede sıra aynıdır: tesbih, dünyanın çekiciliği, "daha hayırlı ve daha kalıcı", namaz ve ilk sayfalar. Bu, ayetin rastgele bir dipnot olmadığını gösterir. İlk sayfaları anmak, bu öğretinin kapanış mührüdür. Taha'da itirazın biçimi de açıkça görülür. İnkârcılar bir işaret ister, cevap ise işaretin zaten geldiğidir. Onlara gelen sözün kendisi, ilk sayfalarda olanın açık delilidir. Bu surenin vurgulu cümlesi de aynı işi görür. Dinleyeni sayfaları aramaya göndermez, işittiği sözün o sayfaların sözü olduğunu söyler.

## İlk olan sonu taşır

[¶13] "Ûlâ", "evvel" (ilk) kelimesinin dişil biçimidir ve burada dişil çoğul "suhuf"a uyar. Kelimenin kökü bir şeyin başlangıcını adlandırır: {ar:الأول وهو مبتدأ الشيء, tr:el-evvelu ve huve mubtedeu'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"}. Araplar sürünün önüne geçen deveye de bu kelimeyle ad verirdi: {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatun evveletun ve cemelun evvelu izâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişiye "evvele", erkeğe "evvel" denir, source:"ء و ل,B001"}. Öndeki deve yolu açar, sürü onun izinden yürür. İlk sayfalar da böyle önde yürür ve sonraki söz onların açtığı izden gelir. On altıncı ve on yedinci ayetlerin kelimeleri yakın olanla en arkada geleni bir yürüyüş dizisine yerleştirir. Surenin bu sahnesinde on sekizinci ayetin "ilk" kelimesi dizinin önünü tutar.

[¶14] Ama bu kelimenin asıl şaşırtıcı yanı Kur'an'daki eşindedir. Kur'an'da "ûlâ" çoğu zaman "âhire"nin karşısında, ilk hayatın, yani bu dünyanın adı olarak durur. Duhâ suresinde Allah kuşluk vaktine ve geceye yemin eder, Peygamber'e Rabbinin onu bırakmadığını söyler ve şunu ekler: {ar:وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ, tr:ve le'l-âhiratu hayrun leke mine'l-ûlâ, gloss:sonraki senin için öncekinden elbette daha hayırlıdır, source:93:4}. Necm suresinde {ar:فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ, tr:fe-lillâhi'l-âhiratu ve'l-ûlâ, gloss:son da ilk de Allah'ındır, source:53:25} denir. Kasas suresinde {ar:لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ, tr:lehu'l-hamdu fi'l-ûlâ ve'l-âhira, gloss:ilkte de sonda da övgü onundur, source:28:70} denir. Bu surede ise on yedinci ayet "âhire" ile başlar ve hemen sonraki ayet "ûlâ" ile biter. Kur'an'ı duyan bir kulak bu çiftin iki kelimesini art arda işitir. Ama "ûlâ" bu kez dünya hayatı anlamına gelmez, en eski yazıları niteler. Başka yerlerde ahiretin karşısına konan kelime burada ahireti savunan tanığın sıfatı olur. En eskiye ait olan, sona ait olanın daha hayırlı olduğunu söyler. Bir kelimenin anlamı değişmemiştir. Değişen, ilk olanın hangi tarafta durduğudur.

[¶15] Aynı kök harfleri, başlangıcın yanında dönüşü ve varılan sonu da taşır. Bu da ayetteki "ilk" anlamının yanında duyulan bir resimdir. {ar:آل يؤول أى رجع, tr:âle ye'ûlu ey raca', gloss:geri döndü, source:"ء و ل,B002"} denirdi. Sözün "te'vîl"i ise onun sonu ve vardığı yerdir: {ar:تأويل الكلام وهو عاقبته وما يؤول إليه, tr:te'vîlu'l-kelâmi ve huve âkıbetuhû ve mâ ye'ûlu ileyh, gloss:sözün te'vîli onun sonucu ve vardığı yerdir, source:"ء و ل,B002"}. Bir başka ifade bunu daha da kısa söyler: {ar:التأويل المرجع والمصير, tr:et-te'vîlu'l-merci'u ve'l-masîr, gloss:te'vîl dönülen yer ve varılan sondur, source:"ء و ل,B002"}. Taha'da ilk sayfalar anılmadan hemen önce "sonuç sakınanındır" denmesi bu bağı Kur'an'ın içinde de görünür kılar. İlk sayfaların içeriği tam da bir sonu haber verir: Necm'deki dizinin varış noktası, varışın Rabbe olmasıdır. İlk yazılan şey, her şeyin döneceği yeri söylemiştir.

[¶16] Bundan bir şey daha çıkar. On yedinci ayet ahiretin "daha kalıcı" olduğunu söyler. On sekizinci ayet ise bu sözün kendisinin de kalıcı olduğunu gösterir. Söz en eski yapraklardan Peygamber'in okuyuşuna kadar ayakta kalmıştır. Dünya hayatı geçer, ama kalıcı olanı anlatan söz geçmemiştir. İddia kendi süresiyle kendini doğrular.

## Musa'nın cevabı: ilkler unutulmaz

[¶17] Son ayette sayfaları anılan Musa, Kur'an'da bu surenin sözlerini neredeyse kendi ağzıyla söyler. Taha suresinde Firavun Musa'ya ve kardeşine {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:Rabbiniz kim, ey Musa, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunâ'llezî a'tâ kulle şey'in halkahû summe hedâ, gloss:Rabbimiz, her şeye yaratılışını veren, sonra yol gösterendir, source:20:50}. Bu, surenin açılışındaki {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî haleka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2} ve {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:ve'llezî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3} ayetlerinin iki adımıdır: yaratmak ve yol göstermek. Firavun'un ikinci sorusu bu ayetin kelimesiyle gelir: {ar:قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:kâle fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:o halde ilk nesillerin durumu ne olacak, source:20:51}. Musa'nın cevabı şudur: {ar:قَالَ عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:kâle ilmuhâ inde rabbî fî kitâb lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne şaşırır ne unutur, source:20:52}.

[¶18] Bu kısa konuşmada ayetin bütün unsurları bir aradadır: "ilk" olanlar, yazılı bir kitap ve unutmayan bir Rab. Firavun'un sorusu bir küçümsemedir. Geçip gitmiş eski nesillerden ne kalmıştır ki? Musa'nın cevabı, ilk olanın kaybolmadığıdır, çünkü yazıldığı yerde unutulmaz. Bu sure de aynı güvenceyi iki kez verir. Altıncı ayette Peygamber'e "unutmayacaksın" denir. On sekizinci ayette en eski sözün hâlâ yerinde durduğu söylenir. İlk nesillerin bilgisi Rabbin katındaki kitapta korunur. İlk sayfaların sözü de okutulan Kur'an'da korunur. İkisinde de "ilk" kelimesi geçmişte kalmış ve unutulmuş bir şeyi değil, korunmuş ve geri getirilmiş bir şeyi anlatır.

===== _commentary/v16/out/87_18/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: inna plus lam on predicate as double emphasis answering doubt
- memory: hādhā as near demonstrative pointing to what was just said
- memory: ūlā is feminine of awwal, agreeing with broken plural ṣuḥuf
- memory: tazakkā as reflexive form, purifying oneself
- memory: Turkish sayfa derives from ṣaḥīfa and narrowed to a book side
- not written: ص ح ف B005 taṣḥīf misreading - pages are never said to be misread here; would import a claim
- not written: ص ح ف B004 broad bowl, ṣiḥāf of paradise - spread-surface theme already carried by B001; bowl adds no work to the ayah
- not written: ء و ل B003 āl as family (āl Ibrāhīm) - different word, belongs to 87:19 rather than ūlā
- not written: ء و ل B004–B011 (governing, thickening, silhouette, tool, ibex, vessel, plant) - no tie to "first pages"
- not written: echo و ل ي - withheld, not identity
- not written: 81:10 pages spread on the last day - record pages, a different referent
- not written: 80:13–16 honoured, raised pages - surah commentary's scene, not needed

===== passages not cited (201) =====
## strong (this ayah's own list) (23)

- (2:79) [listed for 87:18] فَوَيْلٌۭ لِّلَّذِينَ يَكْتُبُونَ ٱلْكِتَٰبَ بِأَيْدِيهِمْ ثُمَّ يَقُولُونَ هَٰذَا مِنْ عِندِ ٱللَّهِ لِيَشْتَرُوا۟ بِهِۦ ثَمَنًۭا قَلِيلًۭا ۖ فَوَيْلٌۭ لَّهُم مِّمَّا كَتَبَتْ أَيْدِيهِمْ وَوَيْلٌۭ لَّهُم مِّمَّا يَكْسِبُونَ
- (3:3) [listed for 87:18] نَزَّلَ عَلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ وَأَنزَلَ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ
- (5:44) [listed for 87:18] إِنَّآ أَنزَلْنَا ٱلتَّوْرَىٰةَ فِيهَا هُدًۭى وَنُورٌۭ ۚ يَحْكُمُ بِهَا ٱلنَّبِيُّونَ ٱلَّذِينَ أَسْلَمُوا۟ لِلَّذِينَ هَادُوا۟ وَٱلرَّبَّٰنِيُّونَ وَٱلْأَحْبَارُ بِمَا ٱسْتُحْفِظُوا۟ مِن كِتَٰبِ ٱللَّهِ وَكَانُوا۟ عَلَيْهِ شُهَدَآءَ ۚ فَلَا تَخْشَوُا۟ ٱلنَّاسَ وَٱخْشَوْنِ وَلَا تَشْتَرُوا۟ بِـَٔايَٰتِى ثَمَنًۭا قَلِيلًۭا ۚ وَمَن لَّمْ يَحْكُم بِمَآ أَنزَلَ ٱللَّهُ فَأُو۟لَٰٓئِكَ هُمُ ٱلْكَٰفِرُونَ
- (5:46) [listed for 87:18] وَقَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِعِيسَى ٱبْنِ مَرْيَمَ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلتَّوْرَىٰةِ ۖ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ فِيهِ هُدًۭى وَنُورٌۭ وَمُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلتَّوْرَىٰةِ وَهُدًۭى وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
- (5:48) [listed for 87:18] وَأَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلْكِتَٰبِ وَمُهَيْمِنًا عَلَيْهِ ۖ فَٱحْكُم بَيْنَهُم بِمَآ أَنزَلَ ٱللَّهُ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ عَمَّا جَآءَكَ مِنَ ٱلْحَقِّ ۚ لِكُلٍّۢ جَعَلْنَا مِنكُمْ شِرْعَةًۭ وَمِنْهَاجًۭا ۚ وَلَوْ شَآءَ ٱللَّهُ لَجَعَلَكُمْ أُمَّةًۭ وَٰحِدَةًۭ وَلَٰكِن لِّيَبْلُوَكُمْ فِى مَآ ءَاتَىٰكُمْ ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ إِلَى ٱللَّهِ مَرْجِعُكُمْ جَمِيعًۭا فَيُنَبِّئُكُم بِمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
- (6:91) [listed for 87:18] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦٓ إِذْ قَالُوا۟ مَآ أَنزَلَ ٱللَّهُ عَلَىٰ بَشَرٍۢ مِّن شَىْءٍۢ ۗ قُلْ مَنْ أَنزَلَ ٱلْكِتَٰبَ ٱلَّذِى جَآءَ بِهِۦ مُوسَىٰ نُورًۭا وَهُدًۭى لِّلنَّاسِ ۖ تَجْعَلُونَهُۥ قَرَاطِيسَ تُبْدُونَهَا وَتُخْفُونَ كَثِيرًۭا ۖ وَعُلِّمْتُم مَّا لَمْ تَعْلَمُوٓا۟ أَنتُمْ وَلَآ ءَابَآؤُكُمْ ۖ قُلِ ٱللَّهُ ۖ ثُمَّ ذَرْهُمْ فِى خَوْضِهِمْ يَلْعَبُونَ
- (7:157) [listed for 87:18] ٱلَّذِينَ يَتَّبِعُونَ ٱلرَّسُولَ ٱلنَّبِىَّ ٱلْأُمِّىَّ ٱلَّذِى يَجِدُونَهُۥ مَكْتُوبًا عِندَهُمْ فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ يَأْمُرُهُم بِٱلْمَعْرُوفِ وَيَنْهَىٰهُمْ عَنِ ٱلْمُنكَرِ وَيُحِلُّ لَهُمُ ٱلطَّيِّبَٰتِ وَيُحَرِّمُ عَلَيْهِمُ ٱلْخَبَٰٓئِثَ وَيَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ بِهِۦ وَعَزَّرُوهُ وَنَصَرُوهُ وَٱتَّبَعُوا۟ ٱلنُّورَ ٱلَّذِىٓ أُنزِلَ مَعَهُۥٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (9:111) [listed for 87:18] ۞ إِنَّ ٱللَّهَ ٱشْتَرَىٰ مِنَ ٱلْمُؤْمِنِينَ أَنفُسَهُمْ وَأَمْوَٰلَهُم بِأَنَّ لَهُمُ ٱلْجَنَّةَ ۚ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ فَيَقْتُلُونَ وَيُقْتَلُونَ ۖ وَعْدًا عَلَيْهِ حَقًّۭا فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ وَٱلْقُرْءَانِ ۚ وَمَنْ أَوْفَىٰ بِعَهْدِهِۦ مِنَ ٱللَّهِ ۚ فَٱسْتَبْشِرُوا۟ بِبَيْعِكُمُ ٱلَّذِى بَايَعْتُم بِهِۦ ۚ وَذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (10:37) [listed for 87:18] وَمَا كَانَ هَٰذَا ٱلْقُرْءَانُ أَن يُفْتَرَىٰ مِن دُونِ ٱللَّهِ وَلَٰكِن تَصْدِيقَ ٱلَّذِى بَيْنَ يَدَيْهِ وَتَفْصِيلَ ٱلْكِتَٰبِ لَا رَيْبَ فِيهِ مِن رَّبِّ ٱلْعَٰلَمِينَ
- (10:94) [listed for 87:18] فَإِن كُنتَ فِى شَكٍّۢ مِّمَّآ أَنزَلْنَآ إِلَيْكَ فَسْـَٔلِ ٱلَّذِينَ يَقْرَءُونَ ٱلْكِتَٰبَ مِن قَبْلِكَ ۚ لَقَدْ جَآءَكَ ٱلْحَقُّ مِن رَّبِّكَ فَلَا تَكُونَنَّ مِنَ ٱلْمُمْتَرِينَ
- (20:133) [listed for 87:18] [cited in ¶11] وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ
- (21:105) [listed for 87:18] وَلَقَدْ كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ أَنَّ ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ
- (26:196) [listed for 87:18] [cited in ¶4] وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ
- (42:13) [listed for 87:18] ۞ شَرَعَ لَكُم مِّنَ ٱلدِّينِ مَا وَصَّىٰ بِهِۦ نُوحًۭا وَٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَمَا وَصَّيْنَا بِهِۦٓ إِبْرَٰهِيمَ وَمُوسَىٰ وَعِيسَىٰٓ ۖ أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ مَا تَدْعُوهُمْ إِلَيْهِ ۚ ٱللَّهُ يَجْتَبِىٓ إِلَيْهِ مَن يَشَآءُ وَيَهْدِىٓ إِلَيْهِ مَن يُنِيبُ
- (46:12) [listed for 87:18] وَمِن قَبْلِهِۦ كِتَٰبُ مُوسَىٰٓ إِمَامًۭا وَرَحْمَةًۭ ۚ وَهَٰذَا كِتَٰبٌۭ مُّصَدِّقٌۭ لِّسَانًا عَرَبِيًّۭا لِّيُنذِرَ ٱلَّذِينَ ظَلَمُوا۟ وَبُشْرَىٰ لِلْمُحْسِنِينَ
- (46:30) [listed for 87:18] قَالُوا۟ يَٰقَوْمَنَآ إِنَّا سَمِعْنَا كِتَٰبًا أُنزِلَ مِنۢ بَعْدِ مُوسَىٰ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ يَهْدِىٓ إِلَى ٱلْحَقِّ وَإِلَىٰ طَرِيقٍۢ مُّسْتَقِيمٍۢ
- (53:36) [listed for 87:18] [cited in ¶2] أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ
- (57:25) [listed for 87:18] لَقَدْ أَرْسَلْنَا رُسُلَنَا بِٱلْبَيِّنَٰتِ وَأَنزَلْنَا مَعَهُمُ ٱلْكِتَٰبَ وَٱلْمِيزَانَ لِيَقُومَ ٱلنَّاسُ بِٱلْقِسْطِ ۖ وَأَنزَلْنَا ٱلْحَدِيدَ فِيهِ بَأْسٌۭ شَدِيدٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَلِيَعْلَمَ ٱللَّهُ مَن يَنصُرُهُۥ وَرُسُلَهُۥ بِٱلْغَيْبِ ۚ إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌۭ
- (80:13) [listed for 87:18] فِى صُحُفٍۢ مُّكَرَّمَةٍۢ
- (80:14) [listed for 87:18] مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ
- (80:15) [listed for 87:18] بِأَيْدِى سَفَرَةٍۢ
- (80:16) [listed for 87:18] كِرَامٍۭ بَرَرَةٍۢ
- (81:10) [listed for 87:18] وَإِذَا ٱلصُّحُفُ نُشِرَتْ

## medium (this ayah's own list) (59)

- (2:4) [listed for 87:18] وَٱلَّذِينَ يُؤْمِنُونَ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ وَبِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (2:53) [listed for 87:18] وَإِذْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَٱلْفُرْقَانَ لَعَلَّكُمْ تَهْتَدُونَ
- (2:75) [listed for 87:18] ۞ أَفَتَطْمَعُونَ أَن يُؤْمِنُوا۟ لَكُمْ وَقَدْ كَانَ فَرِيقٌۭ مِّنْهُمْ يَسْمَعُونَ كَلَٰمَ ٱللَّهِ ثُمَّ يُحَرِّفُونَهُۥ مِنۢ بَعْدِ مَا عَقَلُوهُ وَهُمْ يَعْلَمُونَ
- (2:89) [listed for 87:18] وَلَمَّا جَآءَهُمْ كِتَٰبٌۭ مِّنْ عِندِ ٱللَّهِ مُصَدِّقٌۭ لِّمَا مَعَهُمْ وَكَانُوا۟ مِن قَبْلُ يَسْتَفْتِحُونَ عَلَى ٱلَّذِينَ كَفَرُوا۟ فَلَمَّا جَآءَهُم مَّا عَرَفُوا۟ كَفَرُوا۟ بِهِۦ ۚ فَلَعْنَةُ ٱللَّهِ عَلَى ٱلْكَٰفِرِينَ
- (2:97) [listed for 87:18] قُلْ مَن كَانَ عَدُوًّۭا لِّجِبْرِيلَ فَإِنَّهُۥ نَزَّلَهُۥ عَلَىٰ قَلْبِكَ بِإِذْنِ ٱللَّهِ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ وَهُدًۭى وَبُشْرَىٰ لِلْمُؤْمِنِينَ
- (2:101) [listed for 87:18] وَلَمَّا جَآءَهُمْ رَسُولٌۭ مِّنْ عِندِ ٱللَّهِ مُصَدِّقٌۭ لِّمَا مَعَهُمْ نَبَذَ فَرِيقٌۭ مِّنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ كِتَٰبَ ٱللَّهِ وَرَآءَ ظُهُورِهِمْ كَأَنَّهُمْ لَا يَعْلَمُونَ
- (2:121) [listed for 87:18] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَتْلُونَهُۥ حَقَّ تِلَاوَتِهِۦٓ أُو۟لَٰٓئِكَ يُؤْمِنُونَ بِهِۦ ۗ وَمَن يَكْفُرْ بِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (2:136) [listed for 87:18] قُولُوٓا۟ ءَامَنَّا بِٱللَّهِ وَمَآ أُنزِلَ إِلَيْنَا وَمَآ أُنزِلَ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَمَآ أُوتِىَ مُوسَىٰ وَعِيسَىٰ وَمَآ أُوتِىَ ٱلنَّبِيُّونَ مِن رَّبِّهِمْ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّنْهُمْ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (2:146) [listed for 87:18] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَعْرِفُونَهُۥ كَمَا يَعْرِفُونَ أَبْنَآءَهُمْ ۖ وَإِنَّ فَرِيقًۭا مِّنْهُمْ لَيَكْتُمُونَ ٱلْحَقَّ وَهُمْ يَعْلَمُونَ
- (2:174) [listed for 87:18] إِنَّ ٱلَّذِينَ يَكْتُمُونَ مَآ أَنزَلَ ٱللَّهُ مِنَ ٱلْكِتَٰبِ وَيَشْتَرُونَ بِهِۦ ثَمَنًۭا قَلِيلًا ۙ أُو۟لَٰٓئِكَ مَا يَأْكُلُونَ فِى بُطُونِهِمْ إِلَّا ٱلنَّارَ وَلَا يُكَلِّمُهُمُ ٱللَّهُ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ
- (2:176) [listed for 87:18] ذَٰلِكَ بِأَنَّ ٱللَّهَ نَزَّلَ ٱلْكِتَٰبَ بِٱلْحَقِّ ۗ وَإِنَّ ٱلَّذِينَ ٱخْتَلَفُوا۟ فِى ٱلْكِتَٰبِ لَفِى شِقَاقٍۭ بَعِيدٍۢ
- (2:213) [listed for 87:18] كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ فَبَعَثَ ٱللَّهُ ٱلنَّبِيِّۦنَ مُبَشِّرِينَ وَمُنذِرِينَ وَأَنزَلَ مَعَهُمُ ٱلْكِتَٰبَ بِٱلْحَقِّ لِيَحْكُمَ بَيْنَ ٱلنَّاسِ فِيمَا ٱخْتَلَفُوا۟ فِيهِ ۚ وَمَا ٱخْتَلَفَ فِيهِ إِلَّا ٱلَّذِينَ أُوتُوهُ مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ بَغْيًۢا بَيْنَهُمْ ۖ فَهَدَى ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ لِمَا ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
- (3:48) [listed for 87:18] وَيُعَلِّمُهُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ
- (3:50) [listed for 87:18] وَمُصَدِّقًۭا لِّمَا بَيْنَ يَدَىَّ مِنَ ٱلتَّوْرَىٰةِ وَلِأُحِلَّ لَكُم بَعْضَ ٱلَّذِى حُرِّمَ عَلَيْكُمْ ۚ وَجِئْتُكُم بِـَٔايَةٍۢ مِّن رَّبِّكُمْ فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ
- (3:65) [listed for 87:18] يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تُحَآجُّونَ فِىٓ إِبْرَٰهِيمَ وَمَآ أُنزِلَتِ ٱلتَّوْرَىٰةُ وَٱلْإِنجِيلُ إِلَّا مِنۢ بَعْدِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (3:78) [listed for 87:18] وَإِنَّ مِنْهُمْ لَفَرِيقًۭا يَلْوُۥنَ أَلْسِنَتَهُم بِٱلْكِتَٰبِ لِتَحْسَبُوهُ مِنَ ٱلْكِتَٰبِ وَمَا هُوَ مِنَ ٱلْكِتَٰبِ وَيَقُولُونَ هُوَ مِنْ عِندِ ٱللَّهِ وَمَا هُوَ مِنْ عِندِ ٱللَّهِ وَيَقُولُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ وَهُمْ يَعْلَمُونَ
- (3:79) [listed for 87:18] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
- (3:81) [listed for 87:18] وَإِذْ أَخَذَ ٱللَّهُ مِيثَٰقَ ٱلنَّبِيِّۦنَ لَمَآ ءَاتَيْتُكُم مِّن كِتَٰبٍۢ وَحِكْمَةٍۢ ثُمَّ جَآءَكُمْ رَسُولٌۭ مُّصَدِّقٌۭ لِّمَا مَعَكُمْ لَتُؤْمِنُنَّ بِهِۦ وَلَتَنصُرُنَّهُۥ ۚ قَالَ ءَأَقْرَرْتُمْ وَأَخَذْتُمْ عَلَىٰ ذَٰلِكُمْ إِصْرِى ۖ قَالُوٓا۟ أَقْرَرْنَا ۚ قَالَ فَٱشْهَدُوا۟ وَأَنَا۠ مَعَكُم مِّنَ ٱلشَّٰهِدِينَ
- (3:84) [listed for 87:18] قُلْ ءَامَنَّا بِٱللَّهِ وَمَآ أُنزِلَ عَلَيْنَا وَمَآ أُنزِلَ عَلَىٰٓ إِبْرَٰهِيمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَمَآ أُوتِىَ مُوسَىٰ وَعِيسَىٰ وَٱلنَّبِيُّونَ مِن رَّبِّهِمْ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّنْهُمْ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (3:113) [listed for 87:18] ۞ لَيْسُوا۟ سَوَآءًۭ ۗ مِّنْ أَهْلِ ٱلْكِتَٰبِ أُمَّةٌۭ قَآئِمَةٌۭ يَتْلُونَ ءَايَٰتِ ٱللَّهِ ءَانَآءَ ٱلَّيْلِ وَهُمْ يَسْجُدُونَ
- (3:187) [listed for 87:18] وَإِذْ أَخَذَ ٱللَّهُ مِيثَٰقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَتُبَيِّنُنَّهُۥ لِلنَّاسِ وَلَا تَكْتُمُونَهُۥ فَنَبَذُوهُ وَرَآءَ ظُهُورِهِمْ وَٱشْتَرَوْا۟ بِهِۦ ثَمَنًۭا قَلِيلًۭا ۖ فَبِئْسَ مَا يَشْتَرُونَ
- (4:46) [listed for 87:18] مِّنَ ٱلَّذِينَ هَادُوا۟ يُحَرِّفُونَ ٱلْكَلِمَ عَن مَّوَاضِعِهِۦ وَيَقُولُونَ سَمِعْنَا وَعَصَيْنَا وَٱسْمَعْ غَيْرَ مُسْمَعٍۢ وَرَٰعِنَا لَيًّۢا بِأَلْسِنَتِهِمْ وَطَعْنًۭا فِى ٱلدِّينِ ۚ وَلَوْ أَنَّهُمْ قَالُوا۟ سَمِعْنَا وَأَطَعْنَا وَٱسْمَعْ وَٱنظُرْنَا لَكَانَ خَيْرًۭا لَّهُمْ وَأَقْوَمَ وَلَٰكِن لَّعَنَهُمُ ٱللَّهُ بِكُفْرِهِمْ فَلَا يُؤْمِنُونَ إِلَّا قَلِيلًۭا
- (4:136) [listed for 87:18] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ ءَامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِى نَزَّلَ عَلَىٰ رَسُولِهِۦ وَٱلْكِتَٰبِ ٱلَّذِىٓ أَنزَلَ مِن قَبْلُ ۚ وَمَن يَكْفُرْ بِٱللَّهِ وَمَلَٰٓئِكَتِهِۦ وَكُتُبِهِۦ وَرُسُلِهِۦ وَٱلْيَوْمِ ٱلْءَاخِرِ فَقَدْ ضَلَّ ضَلَٰلًۢا بَعِيدًا
- (4:163) [listed for 87:18] ۞ إِنَّآ أَوْحَيْنَآ إِلَيْكَ كَمَآ أَوْحَيْنَآ إِلَىٰ نُوحٍۢ وَٱلنَّبِيِّۦنَ مِنۢ بَعْدِهِۦ ۚ وَأَوْحَيْنَآ إِلَىٰٓ إِبْرَٰهِيمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ وَيَعْقُوبَ وَٱلْأَسْبَاطِ وَعِيسَىٰ وَأَيُّوبَ وَيُونُسَ وَهَٰرُونَ وَسُلَيْمَٰنَ ۚ وَءَاتَيْنَا دَاوُۥدَ زَبُورًۭا
- (4:171) [listed for 87:18] يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ وَلَا تَقُولُوا۟ عَلَى ٱللَّهِ إِلَّا ٱلْحَقَّ ۚ إِنَّمَا ٱلْمَسِيحُ عِيسَى ٱبْنُ مَرْيَمَ رَسُولُ ٱللَّهِ وَكَلِمَتُهُۥٓ أَلْقَىٰهَآ إِلَىٰ مَرْيَمَ وَرُوحٌۭ مِّنْهُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرُسُلِهِۦ ۖ وَلَا تَقُولُوا۟ ثَلَٰثَةٌ ۚ ٱنتَهُوا۟ خَيْرًۭا لَّكُمْ ۚ إِنَّمَا ٱللَّهُ إِلَٰهٌۭ وَٰحِدٌۭ ۖ سُبْحَٰنَهُۥٓ أَن يَكُونَ لَهُۥ وَلَدٌۭ ۘ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَكَفَىٰ بِٱللَّهِ وَكِيلًۭا
- (5:13) [listed for 87:18] فَبِمَا نَقْضِهِم مِّيثَٰقَهُمْ لَعَنَّٰهُمْ وَجَعَلْنَا قُلُوبَهُمْ قَٰسِيَةًۭ ۖ يُحَرِّفُونَ ٱلْكَلِمَ عَن مَّوَاضِعِهِۦ ۙ وَنَسُوا۟ حَظًّۭا مِّمَّا ذُكِّرُوا۟ بِهِۦ ۚ وَلَا تَزَالُ تَطَّلِعُ عَلَىٰ خَآئِنَةٍۢ مِّنْهُمْ إِلَّا قَلِيلًۭا مِّنْهُمْ ۖ فَٱعْفُ عَنْهُمْ وَٱصْفَحْ ۚ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُحْسِنِينَ
- (5:41) [listed for 87:18] ۞ يَٰٓأَيُّهَا ٱلرَّسُولُ لَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ مِنَ ٱلَّذِينَ قَالُوٓا۟ ءَامَنَّا بِأَفْوَٰهِهِمْ وَلَمْ تُؤْمِن قُلُوبُهُمْ ۛ وَمِنَ ٱلَّذِينَ هَادُوا۟ ۛ سَمَّٰعُونَ لِلْكَذِبِ سَمَّٰعُونَ لِقَوْمٍ ءَاخَرِينَ لَمْ يَأْتُوكَ ۖ يُحَرِّفُونَ ٱلْكَلِمَ مِنۢ بَعْدِ مَوَاضِعِهِۦ ۖ يَقُولُونَ إِنْ أُوتِيتُمْ هَٰذَا فَخُذُوهُ وَإِن لَّمْ تُؤْتَوْهُ فَٱحْذَرُوا۟ ۚ وَمَن يُرِدِ ٱللَّهُ فِتْنَتَهُۥ فَلَن تَمْلِكَ لَهُۥ مِنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ لَمْ يُرِدِ ٱللَّهُ أَن يُطَهِّرَ قُلُوبَهُمْ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ ۖ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (5:68) [listed for 87:18] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَسْتُمْ عَلَىٰ شَىْءٍ حَتَّىٰ تُقِيمُوا۟ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ وَمَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُمْ ۗ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۖ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (6:7) [listed for 87:18] وَلَوْ نَزَّلْنَا عَلَيْكَ كِتَٰبًۭا فِى قِرْطَاسٍۢ فَلَمَسُوهُ بِأَيْدِيهِمْ لَقَالَ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ
- (6:19) [listed for 87:18] قُلْ أَىُّ شَىْءٍ أَكْبَرُ شَهَٰدَةًۭ ۖ قُلِ ٱللَّهُ ۖ شَهِيدٌۢ بَيْنِى وَبَيْنَكُمْ ۚ وَأُوحِىَ إِلَىَّ هَٰذَا ٱلْقُرْءَانُ لِأُنذِرَكُم بِهِۦ وَمَنۢ بَلَغَ ۚ أَئِنَّكُمْ لَتَشْهَدُونَ أَنَّ مَعَ ٱللَّهِ ءَالِهَةً أُخْرَىٰ ۚ قُل لَّآ أَشْهَدُ ۚ قُلْ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ وَإِنَّنِى بَرِىٓءٌۭ مِّمَّا تُشْرِكُونَ
- (6:92) [listed for 87:18] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ مُّصَدِّقُ ٱلَّذِى بَيْنَ يَدَيْهِ وَلِتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا ۚ وَٱلَّذِينَ يُؤْمِنُونَ بِٱلْءَاخِرَةِ يُؤْمِنُونَ بِهِۦ ۖ وَهُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ
- (7:169) [listed for 87:18] فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌۭ وَرِثُوا۟ ٱلْكِتَٰبَ يَأْخُذُونَ عَرَضَ هَٰذَا ٱلْأَدْنَىٰ وَيَقُولُونَ سَيُغْفَرُ لَنَا وَإِن يَأْتِهِمْ عَرَضٌۭ مِّثْلُهُۥ يَأْخُذُوهُ ۚ أَلَمْ يُؤْخَذْ عَلَيْهِم مِّيثَٰقُ ٱلْكِتَٰبِ أَن لَّا يَقُولُوا۟ عَلَى ٱللَّهِ إِلَّا ٱلْحَقَّ وَدَرَسُوا۟ مَا فِيهِ ۗ وَٱلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ
- (11:17) [listed for 87:18] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ وَيَتْلُوهُ شَاهِدٌۭ مِّنْهُ وَمِن قَبْلِهِۦ كِتَٰبُ مُوسَىٰٓ إِمَامًۭا وَرَحْمَةً ۚ أُو۟لَٰٓئِكَ يُؤْمِنُونَ بِهِۦ ۚ وَمَن يَكْفُرْ بِهِۦ مِنَ ٱلْأَحْزَابِ فَٱلنَّارُ مَوْعِدُهُۥ ۚ فَلَا تَكُ فِى مِرْيَةٍۢ مِّنْهُ ۚ إِنَّهُ ٱلْحَقُّ مِن رَّبِّكَ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يُؤْمِنُونَ
- (12:111) [listed for 87:18] لَقَدْ كَانَ فِى قَصَصِهِمْ عِبْرَةٌۭ لِّأُو۟لِى ٱلْأَلْبَٰبِ ۗ مَا كَانَ حَدِيثًۭا يُفْتَرَىٰ وَلَٰكِن تَصْدِيقَ ٱلَّذِى بَيْنَ يَدَيْهِ وَتَفْصِيلَ كُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (13:36) [listed for 87:18] وَٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يَفْرَحُونَ بِمَآ أُنزِلَ إِلَيْكَ ۖ وَمِنَ ٱلْأَحْزَابِ مَن يُنكِرُ بَعْضَهُۥ ۚ قُلْ إِنَّمَآ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ وَلَآ أُشْرِكَ بِهِۦٓ ۚ إِلَيْهِ أَدْعُوا۟ وَإِلَيْهِ مَـَٔابِ
- (16:44) [listed for 87:18] بِٱلْبَيِّنَٰتِ وَٱلزُّبُرِ ۗ وَأَنزَلْنَآ إِلَيْكَ ٱلذِّكْرَ لِتُبَيِّنَ لِلنَّاسِ مَا نُزِّلَ إِلَيْهِمْ وَلَعَلَّهُمْ يَتَفَكَّرُونَ
- (17:55) [listed for 87:18] وَرَبُّكَ أَعْلَمُ بِمَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَلَقَدْ فَضَّلْنَا بَعْضَ ٱلنَّبِيِّۦنَ عَلَىٰ بَعْضٍۢ ۖ وَءَاتَيْنَا دَاوُۥدَ زَبُورًۭا
- (23:49) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ لَعَلَّهُمْ يَهْتَدُونَ
- (28:43) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ مِنۢ بَعْدِ مَآ أَهْلَكْنَا ٱلْقُرُونَ ٱلْأُولَىٰ بَصَآئِرَ لِلنَّاسِ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُمْ يَتَذَكَّرُونَ
- (28:49) [listed for 87:18] قُلْ فَأْتُوا۟ بِكِتَٰبٍۢ مِّنْ عِندِ ٱللَّهِ هُوَ أَهْدَىٰ مِنْهُمَآ أَتَّبِعْهُ إِن كُنتُمْ صَٰدِقِينَ
- (29:27) [listed for 87:18] وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ وَجَعَلْنَا فِى ذُرِّيَّتِهِ ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ وَءَاتَيْنَٰهُ أَجْرَهُۥ فِى ٱلدُّنْيَا ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
- (29:46) [listed for 87:18] ۞ وَلَا تُجَٰدِلُوٓا۟ أَهْلَ ٱلْكِتَٰبِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ ۖ وَقُولُوٓا۟ ءَامَنَّا بِٱلَّذِىٓ أُنزِلَ إِلَيْنَا وَأُنزِلَ إِلَيْكُمْ وَإِلَٰهُنَا وَإِلَٰهُكُمْ وَٰحِدٌۭ وَنَحْنُ لَهُۥ مُسْلِمُونَ
- (32:23) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَلَا تَكُن فِى مِرْيَةٍۢ مِّن لِّقَآئِهِۦ ۖ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ
- (35:25) [listed for 87:18] وَإِن يُكَذِّبُوكَ فَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ جَآءَتْهُمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ وَبِٱلزُّبُرِ وَبِٱلْكِتَٰبِ ٱلْمُنِيرِ
- (37:168) [listed for 87:18] لَوْ أَنَّ عِندَنَا ذِكْرًۭا مِّنَ ٱلْأَوَّلِينَ
- (40:53) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْهُدَىٰ وَأَوْرَثْنَا بَنِىٓ إِسْرَٰٓءِيلَ ٱلْكِتَٰبَ
- (41:45) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ فَٱخْتُلِفَ فِيهِ ۗ وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَقُضِىَ بَيْنَهُمْ ۚ وَإِنَّهُمْ لَفِى شَكٍّۢ مِّنْهُ مُرِيبٍۢ
- (42:15) [listed for 87:18] فَلِذَٰلِكَ فَٱدْعُ ۖ وَٱسْتَقِمْ كَمَآ أُمِرْتَ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ ۖ وَقُلْ ءَامَنتُ بِمَآ أَنزَلَ ٱللَّهُ مِن كِتَٰبٍۢ ۖ وَأُمِرْتُ لِأَعْدِلَ بَيْنَكُمُ ۖ ٱللَّهُ رَبُّنَا وَرَبُّكُمْ ۖ لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ ۖ لَا حُجَّةَ بَيْنَنَا وَبَيْنَكُمُ ۖ ٱللَّهُ يَجْمَعُ بَيْنَنَا ۖ وَإِلَيْهِ ٱلْمَصِيرُ
- (43:45) [listed for 87:18] وَسْـَٔلْ مَنْ أَرْسَلْنَا مِن قَبْلِكَ مِن رُّسُلِنَآ أَجَعَلْنَا مِن دُونِ ٱلرَّحْمَٰنِ ءَالِهَةًۭ يُعْبَدُونَ
- (48:29) [listed for 87:18] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
- (53:56) [listed for 87:18] هَٰذَا نَذِيرٌۭ مِّنَ ٱلنُّذُرِ ٱلْأُولَىٰٓ
- (54:52) [listed for 87:18] وَكُلُّ شَىْءٍۢ فَعَلُوهُ فِى ٱلزُّبُرِ
- (57:26) [listed for 87:18] وَلَقَدْ أَرْسَلْنَا نُوحًۭا وَإِبْرَٰهِيمَ وَجَعَلْنَا فِى ذُرِّيَّتِهِمَا ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ ۖ فَمِنْهُم مُّهْتَدٍۢ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (61:6) [listed for 87:18] وَإِذْ قَالَ عِيسَى ٱبْنُ مَرْيَمَ يَٰبَنِىٓ إِسْرَٰٓءِيلَ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُم مُّصَدِّقًۭا لِّمَا بَيْنَ يَدَىَّ مِنَ ٱلتَّوْرَىٰةِ وَمُبَشِّرًۢا بِرَسُولٍۢ يَأْتِى مِنۢ بَعْدِى ٱسْمُهُۥٓ أَحْمَدُ ۖ فَلَمَّا جَآءَهُم بِٱلْبَيِّنَٰتِ قَالُوا۟ هَٰذَا سِحْرٌۭ مُّبِينٌۭ
- (62:5) [listed for 87:18] مَثَلُ ٱلَّذِينَ حُمِّلُوا۟ ٱلتَّوْرَىٰةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ ٱلْحِمَارِ يَحْمِلُ أَسْفَارًۢا ۚ بِئْسَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِ ٱللَّهِ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (66:12) [listed for 87:18] وَمَرْيَمَ ٱبْنَتَ عِمْرَٰنَ ٱلَّتِىٓ أَحْصَنَتْ فَرْجَهَا فَنَفَخْنَا فِيهِ مِن رُّوحِنَا وَصَدَّقَتْ بِكَلِمَٰتِ رَبِّهَا وَكُتُبِهِۦ وَكَانَتْ مِنَ ٱلْقَٰنِتِينَ
- (74:52) [listed for 87:18] [cited in ¶7] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
- (92:13) [listed for 87:18] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (98:2) [listed for 87:18] [cited in ¶10] رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ

## named by the passage's own list as strong for this ayah (4)

- (2:285) [listed for 87:18] ءَامَنَ ٱلرَّسُولُ بِمَآ أُنزِلَ إِلَيْهِ مِن رَّبِّهِۦ وَٱلْمُؤْمِنُونَ ۚ كُلٌّ ءَامَنَ بِٱللَّهِ وَمَلَٰٓئِكَتِهِۦ وَكُتُبِهِۦ وَرُسُلِهِۦ لَا نُفَرِّقُ بَيْنَ أَحَدٍۢ مِّن رُّسُلِهِۦ ۚ وَقَالُوا۟ سَمِعْنَا وَأَطَعْنَا ۖ غُفْرَانَكَ رَبَّنَا وَإِلَيْكَ ٱلْمَصِيرُ
- (6:156) [listed for 87:18] أَن تَقُولُوٓا۟ إِنَّمَآ أُنزِلَ ٱلْكِتَٰبُ عَلَىٰ طَآئِفَتَيْنِ مِن قَبْلِنَا وَإِن كُنَّا عَن دِرَاسَتِهِمْ لَغَٰفِلِينَ
- (26:137) [listed for 87:18] إِنْ هَٰذَآ إِلَّا خُلُقُ ٱلْأَوَّلِينَ
- (53:37) [listed for 87:18] [cited in ¶2] وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ

## named by the passage's own list as medium for this ayah (36)

- (2:183) [listed for 87:18] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُتِبَ عَلَيْكُمُ ٱلصِّيَامُ كَمَا كُتِبَ عَلَى ٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
- (3:4) [listed for 87:18] مِن قَبْلُ هُدًۭى لِّلنَّاسِ وَأَنزَلَ ٱلْفُرْقَانَ ۗ إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
- (4:162) [listed for 87:18] لَّٰكِنِ ٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ مِنْهُمْ وَٱلْمُؤْمِنُونَ يُؤْمِنُونَ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ ۚ وَٱلْمُقِيمِينَ ٱلصَّلَوٰةَ ۚ وَٱلْمُؤْتُونَ ٱلزَّكَوٰةَ وَٱلْمُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ أُو۟لَٰٓئِكَ سَنُؤْتِيهِمْ أَجْرًا عَظِيمًا
- (5:114) [listed for 87:18] قَالَ عِيسَى ٱبْنُ مَرْيَمَ ٱللَّهُمَّ رَبَّنَآ أَنزِلْ عَلَيْنَا مَآئِدَةًۭ مِّنَ ٱلسَّمَآءِ تَكُونُ لَنَا عِيدًۭا لِّأَوَّلِنَا وَءَاخِرِنَا وَءَايَةًۭ مِّنكَ ۖ وَٱرْزُقْنَا وَأَنتَ خَيْرُ ٱلرَّٰزِقِينَ
- (6:84) [listed for 87:18] وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ ۚ كُلًّا هَدَيْنَا ۚ وَنُوحًا هَدَيْنَا مِن قَبْلُ ۖ وَمِن ذُرِّيَّتِهِۦ دَاوُۥدَ وَسُلَيْمَٰنَ وَأَيُّوبَ وَيُوسُفَ وَمُوسَىٰ وَهَٰرُونَ ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُحْسِنِينَ
- (6:89) [listed for 87:18] أُو۟لَٰٓئِكَ ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ۚ فَإِن يَكْفُرْ بِهَا هَٰٓؤُلَآءِ فَقَدْ وَكَّلْنَا بِهَا قَوْمًۭا لَّيْسُوا۟ بِهَا بِكَٰفِرِينَ
- (6:90) [listed for 87:18] أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا ۖ إِنْ هُوَ إِلَّا ذِكْرَىٰ لِلْعَٰلَمِينَ
- (6:155) [listed for 87:18] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ فَٱتَّبِعُوهُ وَٱتَّقُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (8:31) [listed for 87:18] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا قَالُوا۟ قَدْ سَمِعْنَا لَوْ نَشَآءُ لَقُلْنَا مِثْلَ هَٰذَآ ۙ إِنْ هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (15:10) [listed for 87:18] وَلَقَدْ أَرْسَلْنَا مِن قَبْلِكَ فِى شِيَعِ ٱلْأَوَّلِينَ
- (15:13) [listed for 87:18] لَا يُؤْمِنُونَ بِهِۦ ۖ وَقَدْ خَلَتْ سُنَّةُ ٱلْأَوَّلِينَ
- (17:2) [listed for 87:18] وَءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ أَلَّا تَتَّخِذُوا۟ مِن دُونِى وَكِيلًۭا
- (23:24) [listed for 87:18] فَقَالَ ٱلْمَلَؤُا۟ ٱلَّذِينَ كَفَرُوا۟ مِن قَوْمِهِۦ مَا هَٰذَآ إِلَّا بَشَرٌۭ مِّثْلُكُمْ يُرِيدُ أَن يَتَفَضَّلَ عَلَيْكُمْ وَلَوْ شَآءَ ٱللَّهُ لَأَنزَلَ مَلَٰٓئِكَةًۭ مَّا سَمِعْنَا بِهَٰذَا فِىٓ ءَابَآئِنَا ٱلْأَوَّلِينَ
- (23:68) [listed for 87:18] أَفَلَمْ يَدَّبَّرُوا۟ ٱلْقَوْلَ أَمْ جَآءَهُم مَّا لَمْ يَأْتِ ءَابَآءَهُمُ ٱلْأَوَّلِينَ
- (23:81) [listed for 87:18] بَلْ قَالُوا۟ مِثْلَ مَا قَالَ ٱلْأَوَّلُونَ
- (23:83) [listed for 87:18] لَقَدْ وُعِدْنَا نَحْنُ وَءَابَآؤُنَا هَٰذَا مِن قَبْلُ إِنْ هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (26:69) [listed for 87:18] وَٱتْلُ عَلَيْهِمْ نَبَأَ إِبْرَٰهِيمَ
- (26:84) [listed for 87:18] وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ
- (26:197) [listed for 87:18] [cited in ¶4] أَوَلَمْ يَكُن لَّهُمْ ءَايَةً أَن يَعْلَمَهُۥ عُلَمَٰٓؤُا۟ بَنِىٓ إِسْرَٰٓءِيلَ
- (28:52) [listed for 87:18] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ مِن قَبْلِهِۦ هُم بِهِۦ يُؤْمِنُونَ
- (40:2) [listed for 87:18] تَنزِيلُ ٱلْكِتَٰبِ مِنَ ٱللَّهِ ٱلْعَزِيزِ ٱلْعَلِيمِ
- (43:6) [listed for 87:18] وَكَمْ أَرْسَلْنَا مِن نَّبِىٍّۢ فِى ٱلْأَوَّلِينَ
- (45:16) [listed for 87:18] وَلَقَدْ ءَاتَيْنَا بَنِىٓ إِسْرَٰٓءِيلَ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ وَرَزَقْنَٰهُم مِّنَ ٱلطَّيِّبَٰتِ وَفَضَّلْنَٰهُمْ عَلَى ٱلْعَٰلَمِينَ
- (46:9) [listed for 87:18] قُلْ مَا كُنتُ بِدْعًۭا مِّنَ ٱلرُّسُلِ وَمَآ أَدْرِى مَا يُفْعَلُ بِى وَلَا بِكُمْ ۖ إِنْ أَتَّبِعُ إِلَّا مَا يُوحَىٰٓ إِلَىَّ وَمَآ أَنَا۠ إِلَّا نَذِيرٌۭ مُّبِينٌۭ
- (46:17) [listed for 87:18] وَٱلَّذِى قَالَ لِوَٰلِدَيْهِ أُفٍّۢ لَّكُمَآ أَتَعِدَانِنِىٓ أَنْ أُخْرَجَ وَقَدْ خَلَتِ ٱلْقُرُونُ مِن قَبْلِى وَهُمَا يَسْتَغِيثَانِ ٱللَّهَ وَيْلَكَ ءَامِنْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ فَيَقُولُ مَا هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (52:2) [listed for 87:18] وَكِتَٰبٍۢ مَّسْطُورٍۢ
- (52:3) [listed for 87:18] فِى رَقٍّۢ مَّنشُورٍۢ
- (56:13) [listed for 87:18] ثُلَّةٌۭ مِّنَ ٱلْأَوَّلِينَ
- (56:62) [listed for 87:18] وَلَقَدْ عَلِمْتُمُ ٱلنَّشْأَةَ ٱلْأُولَىٰ فَلَوْلَا تَذَكَّرُونَ
- (68:1) [listed for 87:18] نٓ ۚ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ
- (68:37) [listed for 87:18] أَمْ لَكُمْ كِتَٰبٌۭ فِيهِ تَدْرُسُونَ
- (74:25) [listed for 87:18] إِنْ هَٰذَآ إِلَّا قَوْلُ ٱلْبَشَرِ
- (79:25) [listed for 87:18] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- (85:22) [listed for 87:18] فِى لَوْحٍۢ مَّحْفُوظٍۭ
- (93:4) [listed for 87:18] [cited in ¶14] وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ
- (98:3) [listed for 87:18] [cited in ¶10] فِيهَا كُتُبٌۭ قَيِّمَةٌۭ

## weak (this ayah's own list) (27)

- (3:33) [listed for 87:18] ۞ إِنَّ ٱللَّهَ ٱصْطَفَىٰٓ ءَادَمَ وَنُوحًۭا وَءَالَ إِبْرَٰهِيمَ وَءَالَ عِمْرَٰنَ عَلَى ٱلْعَٰلَمِينَ
- (3:96) [listed for 87:18] إِنَّ أَوَّلَ بَيْتٍۢ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ مُبَارَكًۭا وَهُدًۭى لِّلْعَٰلَمِينَ
- (4:59) [listed for 87:18] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ وَأُو۟لِى ٱلْأَمْرِ مِنكُمْ ۖ فَإِن تَنَٰزَعْتُمْ فِى شَىْءٍۢ فَرُدُّوهُ إِلَى ٱللَّهِ وَٱلرَّسُولِ إِن كُنتُمْ تُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ ذَٰلِكَ خَيْرٌۭ وَأَحْسَنُ تَأْوِيلًا
- (5:110) [listed for 87:18] إِذْ قَالَ ٱللَّهُ يَٰعِيسَى ٱبْنَ مَرْيَمَ ٱذْكُرْ نِعْمَتِى عَلَيْكَ وَعَلَىٰ وَٰلِدَتِكَ إِذْ أَيَّدتُّكَ بِرُوحِ ٱلْقُدُسِ تُكَلِّمُ ٱلنَّاسَ فِى ٱلْمَهْدِ وَكَهْلًۭا ۖ وَإِذْ عَلَّمْتُكَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ ۖ وَإِذْ تَخْلُقُ مِنَ ٱلطِّينِ كَهَيْـَٔةِ ٱلطَّيْرِ بِإِذْنِى فَتَنفُخُ فِيهَا فَتَكُونُ طَيْرًۢا بِإِذْنِى ۖ وَتُبْرِئُ ٱلْأَكْمَهَ وَٱلْأَبْرَصَ بِإِذْنِى ۖ وَإِذْ تُخْرِجُ ٱلْمَوْتَىٰ بِإِذْنِى ۖ وَإِذْ كَفَفْتُ بَنِىٓ إِسْرَٰٓءِيلَ عَنكَ إِذْ جِئْتَهُم بِٱلْبَيِّنَٰتِ فَقَالَ ٱلَّذِينَ كَفَرُوا۟ مِنْهُمْ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ
- (6:25) [listed for 87:18] وَمِنْهُم مَّن يَسْتَمِعُ إِلَيْكَ ۖ وَجَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۚ وَإِن يَرَوْا۟ كُلَّ ءَايَةٍۢ لَّا يُؤْمِنُوا۟ بِهَا ۚ حَتَّىٰٓ إِذَا جَآءُوكَ يُجَٰدِلُونَكَ يَقُولُ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (9:83) [listed for 87:18] فَإِن رَّجَعَكَ ٱللَّهُ إِلَىٰ طَآئِفَةٍۢ مِّنْهُمْ فَٱسْتَـْٔذَنُوكَ لِلْخُرُوجِ فَقُل لَّن تَخْرُجُوا۟ مَعِىَ أَبَدًۭا وَلَن تُقَٰتِلُوا۟ مَعِىَ عَدُوًّا ۖ إِنَّكُمْ رَضِيتُم بِٱلْقُعُودِ أَوَّلَ مَرَّةٍۢ فَٱقْعُدُوا۟ مَعَ ٱلْخَٰلِفِينَ
- (20:21) [listed for 87:18] قَالَ خُذْهَا وَلَا تَخَفْ ۖ سَنُعِيدُهَا سِيرَتَهَا ٱلْأُولَىٰ
- (20:65) [listed for 87:18] قَالُوا۟ يَٰمُوسَىٰٓ إِمَّآ أَن تُلْقِىَ وَإِمَّآ أَن نَّكُونَ أَوَّلَ مَنْ أَلْقَىٰ
- (24:55) [listed for 87:18] وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَيَسْتَخْلِفَنَّهُمْ فِى ٱلْأَرْضِ كَمَا ٱسْتَخْلَفَ ٱلَّذِينَ مِن قَبْلِهِمْ وَلَيُمَكِّنَنَّ لَهُمْ دِينَهُمُ ٱلَّذِى ٱرْتَضَىٰ لَهُمْ وَلَيُبَدِّلَنَّهُم مِّنۢ بَعْدِ خَوْفِهِمْ أَمْنًۭا ۚ يَعْبُدُونَنِى لَا يُشْرِكُونَ بِى شَيْـًۭٔا ۚ وَمَن كَفَرَ بَعْدَ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (26:26) [listed for 87:18] قَالَ رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ
- (26:51) [listed for 87:18] إِنَّا نَطْمَعُ أَن يَغْفِرَ لَنَا رَبُّنَا خَطَٰيَٰنَآ أَن كُنَّآ أَوَّلَ ٱلْمُؤْمِنِينَ
- (26:184) [listed for 87:18] وَٱتَّقُوا۟ ٱلَّذِى خَلَقَكُمْ وَٱلْجِبِلَّةَ ٱلْأَوَّلِينَ
- (28:36) [listed for 87:18] فَلَمَّا جَآءَهُم مُّوسَىٰ بِـَٔايَٰتِنَا بَيِّنَٰتٍۢ قَالُوا۟ مَا هَٰذَآ إِلَّا سِحْرٌۭ مُّفْتَرًۭى وَمَا سَمِعْنَا بِهَٰذَا فِىٓ ءَابَآئِنَا ٱلْأَوَّلِينَ
- (37:17) [listed for 87:18] أَوَءَابَآؤُنَا ٱلْأَوَّلُونَ
- (37:126) [listed for 87:18] ٱللَّهَ رَبَّكُمْ وَرَبَّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ
- (38:45) [listed for 87:18] وَٱذْكُرْ عِبَٰدَنَآ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ أُو۟لِى ٱلْأَيْدِى وَٱلْأَبْصَٰرِ
- (39:12) [listed for 87:18] وَأُمِرْتُ لِأَنْ أَكُونَ أَوَّلَ ٱلْمُسْلِمِينَ
- (43:81) [listed for 87:18] قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ
- (44:35) [listed for 87:18] إِنْ هِىَ إِلَّا مَوْتَتُنَا ٱلْأُولَىٰ وَمَا نَحْنُ بِمُنشَرِينَ
- (53:50) [listed for 87:18] وَأَنَّهُۥٓ أَهْلَكَ عَادًا ٱلْأُولَىٰ
- (56:39) [listed for 87:18] ثُلَّةٌۭ مِّنَ ٱلْأَوَّلِينَ
- (56:48) [listed for 87:18] أَوَءَابَآؤُنَا ٱلْأَوَّلُونَ
- (56:49) [listed for 87:18] قُلْ إِنَّ ٱلْأَوَّلِينَ وَٱلْءَاخِرِينَ
- (68:15) [listed for 87:18] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (77:16) [listed for 87:18] أَلَمْ نُهْلِكِ ٱلْأَوَّلِينَ
- (83:13) [listed for 87:18] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (93:6) [listed for 87:18] أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ

## named by the passage's own list as weak for this ayah (14)

- (5:57) [listed for 87:18] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَكُمْ هُزُوًۭا وَلَعِبًۭا مِّنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ وَٱلْكُفَّارَ أَوْلِيَآءَ ۚ وَٱتَّقُوا۟ ٱللَّهَ إِن كُنتُم مُّؤْمِنِينَ
- (6:163) [listed for 87:18] لَا شَرِيكَ لَهُۥ ۖ وَبِذَٰلِكَ أُمِرْتُ وَأَنَا۠ أَوَّلُ ٱلْمُسْلِمِينَ
- (20:51) [listed for 87:18] [cited in ¶17] قَالَ فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ
- (21:106) [listed for 87:18] إِنَّ فِى هَٰذَا لَبَلَٰغًۭا لِّقَوْمٍ عَٰبِدِينَ
- (33:33) [listed for 87:18] وَقَرْنَ فِى بُيُوتِكُنَّ وَلَا تَبَرَّجْنَ تَبَرُّجَ ٱلْجَٰهِلِيَّةِ ٱلْأُولَىٰ ۖ وَأَقِمْنَ ٱلصَّلَوٰةَ وَءَاتِينَ ٱلزَّكَوٰةَ وَأَطِعْنَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ إِنَّمَا يُرِيدُ ٱللَّهُ لِيُذْهِبَ عَنكُمُ ٱلرِّجْسَ أَهْلَ ٱلْبَيْتِ وَيُطَهِّرَكُمْ تَطْهِيرًۭا
- (40:54) [listed for 87:18] هُدًۭى وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (44:8) [listed for 87:18] لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ
- (44:56) [listed for 87:18] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
- (53:25) [listed for 87:18] [cited in ¶14] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (56:78) [listed for 87:18] فِى كِتَٰبٍۢ مَّكْنُونٍۢ
- (56:95) [listed for 87:18] إِنَّ هَٰذَا لَهُوَ حَقُّ ٱلْيَقِينِ
- (81:21) [listed for 87:18] مُّطَاعٍۢ ثَمَّ أَمِينٍۢ
- (83:7) [listed for 87:18] كَلَّآ إِنَّ كِتَٰبَ ٱلْفُجَّارِ لَفِى سِجِّينٍۢ
- (83:18) [listed for 87:18] كَلَّآ إِنَّ كِتَٰبَ ٱلْأَبْرَارِ لَفِى عِلِّيِّينَ

## neighbours: within two ayat of a passage the commentary cites (38)

- (20:47) [next to 20:49] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
- (20:48) [next to 20:49] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
- (20:53) [next to 20:51] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
- (20:54) [next to 20:52] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:128) [next to 20:130] أَفَلَمْ يَهْدِ لَهُمْ كَمْ أَهْلَكْنَا قَبْلَهُم مِّنَ ٱلْقُرُونِ يَمْشُونَ فِى مَسَٰكِنِهِمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:129) [next to 20:130] وَلَوْلَا كَلِمَةٌۭ سَبَقَتْ مِن رَّبِّكَ لَكَانَ لِزَامًۭا وَأَجَلٌۭ مُّسَمًّۭى
- (20:134) [next to 20:132] وَلَوْ أَنَّآ أَهْلَكْنَٰهُم بِعَذَابٍۢ مِّن قَبْلِهِۦ لَقَالُوا۟ رَبَّنَا لَوْلَآ أَرْسَلْتَ إِلَيْنَا رَسُولًۭا فَنَتَّبِعَ ءَايَٰتِكَ مِن قَبْلِ أَن نَّذِلَّ وَنَخْزَىٰ
- (20:135) [next to 20:133] قُلْ كُلٌّۭ مُّتَرَبِّصٌۭ فَتَرَبَّصُوا۟ ۖ فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ
- (26:194) [next to 26:196] عَلَىٰ قَلْبِكَ لِتَكُونَ مِنَ ٱلْمُنذِرِينَ
- (26:195) [next to 26:196] بِلِسَانٍ عَرَبِىٍّۢ مُّبِينٍۢ
- (26:198) [next to 26:196] وَلَوْ نَزَّلْنَٰهُ عَلَىٰ بَعْضِ ٱلْأَعْجَمِينَ
- (26:199) [next to 26:197] فَقَرَأَهُۥ عَلَيْهِم مَّا كَانُوا۟ بِهِۦ مُؤْمِنِينَ
- (28:68) [next to 28:70] وَرَبُّكَ يَخْلُقُ مَا يَشَآءُ وَيَخْتَارُ ۗ مَا كَانَ لَهُمُ ٱلْخِيَرَةُ ۚ سُبْحَٰنَ ٱللَّهِ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (28:69) [next to 28:70] وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ
- (28:71) [next to 28:70] قُلْ أَرَءَيْتُمْ إِن جَعَلَ ٱللَّهُ عَلَيْكُمُ ٱلَّيْلَ سَرْمَدًا إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَنْ إِلَٰهٌ غَيْرُ ٱللَّهِ يَأْتِيكُم بِضِيَآءٍ ۖ أَفَلَا تَسْمَعُونَ
- (28:72) [next to 28:70] قُلْ أَرَءَيْتُمْ إِن جَعَلَ ٱللَّهُ عَلَيْكُمُ ٱلنَّهَارَ سَرْمَدًا إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَنْ إِلَٰهٌ غَيْرُ ٱللَّهِ يَأْتِيكُم بِلَيْلٍۢ تَسْكُنُونَ فِيهِ ۖ أَفَلَا تُبْصِرُونَ
- (29:47) [next to 29:48] وَكَذَٰلِكَ أَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ ۚ فَٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يُؤْمِنُونَ بِهِۦ ۖ وَمِنْ هَٰٓؤُلَآءِ مَن يُؤْمِنُ بِهِۦ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلْكَٰفِرُونَ
- (29:49) [next to 29:48] بَلْ هُوَ ءَايَٰتٌۢ بَيِّنَٰتٌۭ فِى صُدُورِ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلظَّٰلِمُونَ
- (29:50) [next to 29:48] وَقَالُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَٰتٌۭ مِّن رَّبِّهِۦ ۖ قُلْ إِنَّمَا ٱلْءَايَٰتُ عِندَ ٱللَّهِ وَإِنَّمَآ أَنَا۠ نَذِيرٌۭ مُّبِينٌ
- (53:23) [next to 53:25] إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ ۚ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ وَمَا تَهْوَى ٱلْأَنفُسُ ۖ وَلَقَدْ جَآءَهُم مِّن رَّبِّهِمُ ٱلْهُدَىٰٓ
- (53:24) [next to 53:25] أَمْ لِلْإِنسَٰنِ مَا تَمَنَّىٰ
- (53:26) [next to 53:25] ۞ وَكَم مِّن مَّلَكٍۢ فِى ٱلسَّمَٰوَٰتِ لَا تُغْنِى شَفَٰعَتُهُمْ شَيْـًٔا إِلَّا مِنۢ بَعْدِ أَن يَأْذَنَ ٱللَّهُ لِمَن يَشَآءُ وَيَرْضَىٰٓ
- (53:27) [next to 53:25] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ لَيُسَمُّونَ ٱلْمَلَٰٓئِكَةَ تَسْمِيَةَ ٱلْأُنثَىٰ
- (53:31) [next to 53:33] وَلِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ لِيَجْزِىَ ٱلَّذِينَ أَسَٰٓـُٔوا۟ بِمَا عَمِلُوا۟ وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى
- (53:32) [next to 53:33] ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ إِلَّا ٱللَّمَمَ ۚ إِنَّ رَبَّكَ وَٰسِعُ ٱلْمَغْفِرَةِ ۚ هُوَ أَعْلَمُ بِكُمْ إِذْ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ ۖ فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ
- (53:35) [next to 53:33] أَعِندَهُۥ عِلْمُ ٱلْغَيْبِ فَهُوَ يَرَىٰٓ
- (53:41) [next to 53:39] ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ
- (53:43) [next to 53:42] وَأَنَّهُۥ هُوَ أَضْحَكَ وَأَبْكَىٰ
- (53:44) [next to 53:42] وَأَنَّهُۥ هُوَ أَمَاتَ وَأَحْيَا
- (74:50) [next to 74:52] كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ
- (74:51) [next to 74:52] فَرَّتْ مِن قَسْوَرَةٍۭ
- (74:56) [next to 74:54] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
- (93:2) [next to 93:4] وَٱلَّيْلِ إِذَا سَجَىٰ
- (93:3) [next to 93:4] مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ
- (93:5) [next to 93:4] وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
- (98:0) [next to 98:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (98:4) [next to 98:2] وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- (98:5) [next to 98:3] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ

