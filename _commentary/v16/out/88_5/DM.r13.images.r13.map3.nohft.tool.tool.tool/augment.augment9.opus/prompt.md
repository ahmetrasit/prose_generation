Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:5; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_5/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_5.reading.tr.md (prose paragraphs numbered) =====
## İçmek değil, içirilmek

[¶1] Beşinci ayetin öznesi ikinci ayette başlayan yüzlerdir: o gün eğilmiş, didinip bitkin düşmüş yüzler. Dördüncü ayet bu yüzlerin kızgın bir ateşe girdiğini söylemişti: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Beşinci ayet aynı kalıpla sürer: önce bir fiil, sonra belirsiz bir isim, sonra sonu aynı sesle biten bir sıfat. Yalnız fiilin yönü değişir. Taslâ etken bir fiildir, ateşe giren yüzün kendisidir. Tuskâ ise edilgendir: {ar:تُسْقَىٰ, tr:tuskâ, gloss:içirilir, source:88:5}. Yüz kendisi içmez, ona içirilir. Arapçada bu fiil birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:birine içecek bir şey vermek, source:"س ق ي,B001"}. Araplar bu işi bir elin işi olarak söylerdi: {ar:سقيته بيدي أسقيه سقيا, tr:sekaytuhû bi-yedî eskîhi sakyâ, gloss:ona elimle içecek verdim, source:"س ق ي,B001"}. Fiilin içinde suyu uzatan biri vardır. Ayet bu kişiyi adlandırmaz, yalnızca suyun nereden geldiğini söyler. Türkçede bu kökten kalan "sâki" kelimesi şiirde kadeh sunan zarif bir figürdür. Arapça fiil ise çok daha geniştir: susamış birine su vermek de, hayvanı sulamak da, tarlaya su salmak da onunla söylenir. Ayette sâkinin yeri boş bırakılmıştır.

[¶2] Kur'an başka yerlerde içirenin adını açıkça verir. İbrahim, kavminin taptığı putları sayıp hepsinin kendisine düşman olduğunu söyledikten sonra âlemlerin Rabbini anlatır. Onu yaratan ve yol gösteren Rab için şöyle der: {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî huve yut'imunî ve yeskîn, gloss:beni yediren ve içiren O'dur, source:26:79}. İnsan suresinde adaklarını yerine getiren ve yoksulu Allah rızası için doyuranlara verilen karşılıklar sayılır. Sayımın sonunda içiren yine anılır: {ar:وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا, tr:ve sekâhum rabbuhum şerâben tahûrâ, gloss:Rableri onlara tertemiz bir içecek içirdi, source:76:21}. Bu iki ayette içirmek bir ikramdır ve ikram edenin adı söylenir. Kur'an'da beşinci ayetin kalıbını, yani edilgen fiil ve "-den" ile başlayan kaynağı, birebir taşıyan bir ayet daha vardır. İbrahim suresinde inkârcılar peygamberlerini yurtlarından çıkarmakla tehdit eder. Allah peygamberlere zalimleri helak edeceğini bildirir, her inatçı zorba da hüsrana uğrar. Ayet o zorba için şöyle der: {ar:مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ, tr:min verâihî cehennemu ve yuskâ min mâin sadîd, gloss:önünde cehennem vardır; irinli bir sudan içirilir, source:14:16}. Hemen ardından içişin kendisi anlatılır: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. Edilgen fiil, içenin seçmediği bir içişi anlatır.

[¶3] Suyun bu yüzlere ne yapması beklendiği surenin sırasından anlaşılır. Üçüncü ayetteki yüz çalışıp didinmiş, yorgun düşmüştür. Dördüncü ayetteki yüz kızgın bir ateşin içindedir. Yorgunluktan ve sıcaktan gelen birinin istediği ilk şey sudur, suyun işi de serinletmektir. Nebe' suresi cehennemi bir pusu olarak anlatıp azgınların orada çağlar boyu kalacağını söyledikten sonra suyun bu işini adıyla anar: {ar:لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا, tr:lâ yezûkûne fîhâ berden ve lâ şerâbâ, gloss:orada ne bir serinlik tadarlar ne de bir içecek, source:78:24}; {ar:إِلَّا حَمِيمًۭا وَغَسَّاقًۭا, tr:illâ hamîmen ve ğassâkâ, gloss:yalnızca kaynar su ve irin tadarlar, source:78:25}. Beşinci ayette de su gelir ama serinlik getirmez, dördüncü ayetin ateşini içeriden sürdürür. İkinci ayetteki eğik yüzün kelimesi yağmur görmemiş toprağı da adlandırdığı için, kurumuş toprağın yakan suyla sulanması surenin bütününde kurulan bir sahnedir. Bu ayetin payına o sahnenin fiili düşer: sulamak.

## Su vermek, su payı ve su istemek

[¶4] Arapça aynı kökten iki ayrı vermeyi birbirinden ayırır. Biri, buradaki gibi, ağza içecek uzatmaktır. Öteki, birine dilediği zaman yararlanacağı bir su kaynağı vermektir: {ar:أسقينا فلانا نهرا أي جعلناه له سقيا, tr:eskaynâ fülânen nehran ey cealnâhu lehû sukyâ, gloss:falana bir ırmak verdik, yani onu onun suyu kıldık, source:"س ق ي,B002"}. Bu ikinci vermenin özü serbestliktir: {ar:الإسقاء أن يجعل له ذلك حتى يتناوله كيف شاء, tr:el-iskâu en yec'ale lehû zâlike hattâ yetenâvelehû keyfe şâ', gloss:ona suyu, dilediği gibi alsın diye verme, source:"س ق ي,B002"}. Bu ve bundan sonraki yan anlamlar ayetteki "içirilir" anlamının yerine geçmez, onun yanında duyulur. Kur'an dünyadaki suyu tam da bu ikinci kalıpla anlatır. Allah gökte burçlar kurduğunu, yeri yaydığını ve orada geçim yolları yarattığını sayarken şöyle der: {ar:وَأَرْسَلْنَا ٱلرِّيَٰحَ لَوَٰقِحَ فَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَسْقَيْنَٰكُمُوهُ وَمَآ أَنتُمْ لَهُۥ بِخَٰزِنِينَ, tr:ve erselne'r-riyâha levâkiha fe-enzelnâ mine's-semâi mâen fe-eskaynâkumûhu ve mâ entum lehû bi-hâzinîn, gloss:rüzgârları aşılayıcı olarak gönderdik, gökten su indirip onu size içecek kıldık; onu depolayan siz değilsiniz, source:15:22}. Mürselât suresinde de yeryüzüne yüce dağlar yerleştirildiği söylenen ayet aynı fiille biter: {ar:وَجَعَلْنَا فِيهَا رَوَٰسِىَ شَٰمِخَٰتٍۢ وَأَسْقَيْنَٰكُم مَّآءًۭ فُرَاتًۭا, tr:ve cealnâ fîhâ revâsiye şâmihâtin ve eskaynâkum mâen furâtâ, gloss:orada yüce dağlar kurduk ve size tatlı bir su içirdik, source:77:27}. On dokuzuncu ayet de dikilmiş dağlara bakmayı ister. Dünyada su, insanın elinin altına bırakılmış bir kaynaktı: depolayan insan değildi ama dilediği gibi alıyordu. Beşinci ayette ise kaynak kimsenin eline bırakılmaz. Su ağza verilir, içenin seçimi yoktur. On ikinci ayetteki bahçede akan pınarın yanında bu fark daha da belirginleşir.

[¶5] Kökün tarımdan gelen kullanımı suya bir pay olarak bakar. Bir toprağın suyunu sorarken Araplar şöyle derlerdi: {ar:كم سقى أرضك أي حظها من الشرب, tr:kem sakyu ardike ey hazzuhâ mine'ş-şirb, gloss:toprağının su payı ne kadar, yani içme payı, source:"س ق ي,B003"}. Her tarlanın ırmaktan payına düşen bir suyu vardır. Bu açıdan bakınca ayet bir pay dağıtımını da anlatır: bu yüzlerin payına düşen su, kaynamış bir pınardan gelir.

[¶6] Su istemek de aynı kökle söylenir. Biri için su ve yağmur dilemenin sözü şuydu: {ar:سقاه الله الغيث وأسقاه, tr:sekâhullâhu'l-ğayse ve eskâh, gloss:Allah ona yağmur içirsin, ona yağmur versin, source:"س ق ي,B006"}. Kur'an bu istemeyi bir sahnede anlatır ve o sahnede ayetin iki kelimesi bir araya gelir. Allah İsrailoğullarına, onlara verdiği nimetleri hatırlatırken şöyle der: {ar:وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ, tr:ve izi'steskâ mûsâ li-kavmihî fe-kulne'drib bi-asâke'l-hacer, fenfecerat minhu'snetâ aşrate aynâ, kad alime küllü unâsin meşrebehum, gloss:Musa kavmi için su istediğinde ona "asanla taşa vur" dedik; taştan on iki pınar fışkırdı, her topluluk kendi içme yerini bildi, source:2:60}. Orada su istenir, cevap olarak pınarlar gelir, her topluluk da kendi payını bilir. Ayetin devamı bu suyu "Allah'ın rızkı" diye adlandırır. Ateş halkının su isteyişi ise başka bir sonla anlatılır. Bahçe halkına seslenirler: {ar:أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ, tr:en efîdû aleynâ mine'l-mâi ev mimmâ rezakakumullâh, gloss:üzerimize sudan ya da Allah'ın size verdiği rızıktan biraz akıtın, source:7:50}. Bahçe halkı da Allah'ın bu ikisini inkârcılara haram kıldığını söyler {source:7:50}. Allah Peygamber'e, hakkın Rabden geldiğini ve dileyenin inanıp dileyenin inkâr edeceğini söylemesini buyurduğu ayette, ateşte yardım isteyenlere verilecek cevabı da bildirir: {ar:وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ, tr:ve in yesteğîsû yuğâsû bi-mâin ke'l-mühli yeşvi'l-vucûh, gloss:yardım isterlerse erimiş maden gibi, yüzleri kavuran bir suyla yardım edilir, source:18:29}. Beşinci ayet bir istekten söz etmez. Yine de Musa'nın sahnesiyle yan yana konunca şu görülür: orada istenen su taştan pınar olarak gelmişti, burada da bir pınar vardır ama suyu kaynamıştır.

## Pınar: yerin gözü

[¶7] Pınarın Arapçadaki adı ayndır. Araplar bu kelimeyle yerden kendiliğinden kaynayıp akan suyu anlatırdı: {ar:العين الينبوع الذي ينبع من الأرض ويجري, tr:el-aynu'l-yenbû'u'llezî yenbeu mine'l-ardi ve yecrî, gloss:ayn, yerden kaynayıp akan su başıdır, source:"ع ي ن,B006"}. Pınarın işleyişi kuyudan ve ırmaktan farklıdır. Kuyudan ya da ırmaktan su almanın ayrı bir adı vardı: {ar:الاستقاء الأخذ من النهر والبئر, tr:el-istikâu'l-ahzu mine'n-nehri ve'l-bi'r, gloss:istikâ ırmaktan ve kuyudan su almaktır, source:"س ق ي,B001"}. Kuyunun suyu kova ve iple yukarı çekilir. Pınarın suyu ise yerin içinden kendiliğinden yüzeye çıkar, kimsenin emeğini beklemez. Bu yüzden pınar suyu gözle görülen sudur: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:maîn su, gözlere açık sudur, source:"ع ي ن,B006"}. Üçüncü ayetteki didinen yüz burada kova da çekmez. Su ona hazır bir kaynaktan verilir, ama bu hazırlık bir ikram değildir.

[¶8] Aynı kelime gören gözün de adıdır: {ar:العين الناظرة لكل ذي بصر, tr:el-aynu'n-nâzıratu li-külli zî basar, gloss:gören her canlının bakan gözü, source:"ع ي ن,B001"}. Ayette bu anlam pınarın yanında duyulur. Pınara neden göz dendiğini, su tulumundaki delik için söylenen bir açıklama gösterir: {ar:الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء, tr:es-sakbu fi'l-mezâdeti teşbîhen bihâ fi'l-hey'eti ve fî seyelâni'l-mâ', gloss:su tulumundaki delik; biçimiyle ve su akıtmasıyla göze benzetilerek, source:"ع ي ن,B007"}. Göz, içinden su akan yuvarlak bir açıklıktır. Gözyaşı gözden nasıl geliyorsa, yerin içindeki su da pınardan öyle çıkar. Pınar, yerin gözüdür.

[¶9] Göz kelimesi bir şeyi aracısız, kendi gözüyle görmeyi de anlatır: {ar:رأيت الشيء عيانا أي معاينة, tr:raeytu'ş-şey'e iyânen ey muâyeneten, gloss:onu gözümle, yüz yüze gördüm, source:"ع ي ن,B002"}. Türkçede "muayene" bugün hekimin hastaya bakmasıdır. Arapçadaki kaynağı ise bir şeyi başkasından duymadan, kendi gözüyle karşı karşıya görmektir. Araplar bu görmenin habere son verdiğini bir sözle söylerdi: {ar:لا أطلب أثرا بعد عين أي بعد معاينة, tr:lâ atlubu eseran ba'de aynin ey ba'de muâyene, gloss:gördükten sonra iz aramam, source:"ع ي ن,B002"}. İz, birinin geçtiğini dolaylı yoldan gösterir. Göz ise onu doğrudan görür. Sure de bir haberle açılır: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsu'l-ğâşiye, gloss:her şeyi örten o günün haberi sana geldi mi, source:88:1}. Haber kulağa gelen bir sözdür. Beşinci ayette ise o günü yaşayanlar artık haber dinlemez, bir ayndan içerler. Kur'an aynı kelimeyi ateşin görülüşü için de kullanır. Tekâsür suresinde, çokluk yarışının oyaladığı insanlara kesin bilgiyle bilselerdi neyi göreceklerini söyler: {ar:لَتَرَوُنَّ ٱلْجَحِيمَ, tr:le-terevunne'l-cahîm, gloss:alevli ateşi mutlaka göreceksiniz, source:102:6}; {ar:ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ, tr:summe le-terevunnehâ ayne'l-yakîn, gloss:sonra onu kesinliğin gözüyle göreceksiniz, source:102:7}. O ayette ateş kesinliğin gözüyle görülür. Bu ayette ise ateşten sonra gelen su bir gözden içilir. Duyulan haber, önce görülen, sonra içilen bir şeye dönüşür.

[¶10] Aynı kelime on ikinci ayette bahçede akan pınarı adlandırır: {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. İki pınarın sıfatlarıyla karşı karşıya durması surenin bütününe ait bir sahnedir.

## Âniye: vakti gelmiş sıcaklık

[¶11] Pınarın sıfatı âniyedir ve ayetteki anlamı, sıcaklığı son noktasına varmış sudur. Araplar bu sıfatı kaynar su için kullanır, pınarı da aynı kelimeyle nitelerdi: {ar:حميم آن قد انتهى حره وعين آنية, tr:hamîmun ânin kad intehâ harruhû ve aynun âniye, gloss:sıcaklığı sonuna varmış kaynar su; âniye pınar, source:"ء ن ي,B003"}; {ar:بلغ إناه من شدة الحر, tr:belağa inâhu min şiddeti'l-harr, gloss:sıcaklığın şiddetinden son noktasına vardı, source:"ء ن ي,B003"}. Kelime sıcaklığı bir dereceyle değil, bir vakitle ölçer. Kökün asıl anlamı bir şeyin vaktinin gelmesi ve olgunluğa ermesidir: {ar:أنى الشيء يأنى إنى أي حان وأنى أيضا أدرك, tr:enâ'ş-şey'u ye'nâ inen ey hâne ve enâ eyden edrake, gloss:şeyin vakti geldi; ayrıca olgunlaştı, erişti, source:"ء ن ي,B003"}. Âniye bir pınar, ısınacağı vakte ermiş, beklenen sıcaklığına ulaşmış bir pınardır. Kökün başka bir kolu da beklemeyi ve geciktirmeyi anlatır: {ar:آناه يؤنيه إيناء أي أخره وحبسه وأبطأه, tr:ânâhu yü'nîhi îna'en ey ahharahû ve habesehû ve ebtaeh, gloss:onu geciktirdi, alıkoydu, yavaşlattı, source:"ء ن ي,B001"}. Aynı harflerde hem beklemek hem de beklenen vaktin gelmesi vardır. Bekletilen şey bir gün vaktine erer. Bu suyun sıcaklığı da vaktine ermiş bir sıcaklıktır. Dördüncü ayetin kızgın ateşi ve altıncı ayetin yemeğiyle bu kelimenin birlikte konuştuğu mutfak dili, yani pişmeyi ve kıvamı anlatan dil, surenin bütününde kurulur.

[¶12] Kur'an aynı sıfatı Rahmân suresinde kullanır. Orada Allah insanlara ve cinlere seslenir. Suçluların yüzlerinden tanınıp yakalanacağı söylendikten sonra şöyle denir: {ar:هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى يُكَذِّبُ بِهَا ٱلْمُجْرِمُونَ, tr:hâzihî cehennemu'lletî yükezzibu bihe'l-mucrimûn, gloss:işte suçluların yalanladığı cehennem budur, source:55:43}; {ar:يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ, tr:yetûfûne beynehâ ve beyne hamîmin ân, gloss:onunla sıcaklığı sonuna varmış kaynar su arasında dolaşırlar, source:55:44}. Rahmân suresinin bu ayeti ile beşinci ayet aynı sıfatı taşır. Sure bunun hemen ardından Rabbinin makamından korkanlara iki bahçe verildiğini söyler {source:55:46}. Gâşiye suresinde olduğu gibi orada da kaynar suyun karşısına bahçe konur.

[¶13] Kökün vakit anlamı Kur'an'da bir soruya da dönüşür ve bu soru, beşinci ayetin kelimesini ikinci ayetin kelimesiyle buluşturur. Hadîd suresinde Allah inananlara sorar: {ar:أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ, tr:e-lem ye'ni lillezîne âmenû en tahşea kulûbuhum li-zikrillâhi ve mâ nezele mine'l-hakk, gloss:inananların kalplerinin Allah'ı anmaya ve inen hakka saygıyla eğilmesinin vakti gelmedi mi, source:57:16}. Araplar da vakit için bu soruyu sorardı: {ar:ما أنى لك ولم يأن لك أي لم يحن, tr:mâ enâ leke ve lem ye'ni leke ey lem yehın, gloss:senin için vakti gelmedi mi, source:"ء ن ي,B003"}. Hadîd'deki ayetin devamı uyarır: kendilerinden önce kitap verilenler gibi olmasınlar, onlara uzun zaman geçmiş ve kalpleri katılaşmıştır {source:57:16}. Ayette "eğilmek" diye geçen fiil, ikinci ayetteki eğik yüzün kelimesidir. "Vakti gelmek" diye geçen fiil de beşinci ayetteki âniyenin köküdür. Bu ikisinin bir araya gelişinden bir okuma doğar. Dünyada kalbe sorulan şey, eğilmenin vaktinin gelip gelmediğidir. Kalp o vakti kaçırırsa, ikinci ayette eğilme yüze gelir, beşinci ayette de vakit suya gelir. Kalp, vaktinde ermediği olgunluğun karşısında, vaktine ermiş bir sıcaklıkla karşılaşır. Hadîd'deki sorunun hemen ardından gelen ayet de toprağa döner: {ar:ٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا, tr:i'lemû ennallâhe yuhyi'l-arda ba'de mevtihâ, gloss:bilin ki Allah yeri ölümünden sonra diriltir, source:57:17}. Katılaşmış kalbin yanına, suyla dirilen toprak konur.

[¶14] Kur'an kalbin katılaşmasını başka bir yerde suyla ve taşla anlatır. Musa'nın taşından on iki pınar fışkırtılan sahneden birkaç ayet sonra, Allah İsrailoğullarına şöyle der: {ar:ثُمَّ قَسَتْ قُلُوبُكُم مِّنۢ بَعْدِ ذَٰلِكَ فَهِىَ كَٱلْحِجَارَةِ أَوْ أَشَدُّ قَسْوَةًۭ ۚ وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ ۚ وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ, tr:summe kaset kulûbukum min ba'di zâlike fe-hiye ke'l-hicârati ev eşeddu kaswah, ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, ve inne minhâ lemâ yeşşakkaku fe-yahrucu minhu'l-mâ', gloss:sonra kalpleriniz katılaştı; taş gibi, hatta daha katı oldu. Oysa taşlardan öylesi var ki içinden ırmaklar fışkırır, öylesi var ki yarılır da içinden su çıkar, source:2:74}. Hadîd'de kalbi katılaştıran fiil burada da kullanılır. Taş bile yarılıp su verir. Pınar, sert yerin içinden suyun kendiliğinden çıkmasıdır. Kur'an kalbin de böyle bir pınar olabileceğini, katı kalbin ise taştan daha az su verdiğini söyler. Beşinci ayetteki pınar bu karşıtlığın öbür ucunda durur. İçinden serinlik çıkmayan kalbin karşılaştığı pınardan da serinlik çıkmaz.

[¶15] Aynı kök, zamanı gecenin saatlerine bölerek de ölçer: {ar:آناء الليل ساعاته, tr:ânâu'l-leyli sââtuh, gloss:gecenin ânâ'sı onun saatleridir, source:"ء ن ي,B002"}. Kur'an bu saatleri dolduran insanı şöyle anar: {ar:أَمَّنْ هُوَ قَٰنِتٌ ءَانَآءَ ٱلَّيْلِ سَاجِدًۭا وَقَآئِمًۭا يَحْذَرُ ٱلْءَاخِرَةَ وَيَرْجُوا۟ رَحْمَةَ رَبِّهِۦ, tr:em-men huve kânitun âne'l-leyli sâciden ve kâimen yahzeru'l-âhirate ve yercû rahmete rabbih, gloss:yoksa gecenin saatlerinde secdeye kapanarak ve ayakta durarak gönülden itaat eden, âhiretten çekinen ve Rabbinin rahmetini uman kişi mi, source:39:9}. Bu kökte vakit, kullanılabilecek saatlerden oluşur. Saatlerini secdeyle dolduran kişinin karşısında, vakti tükenmiş ve sıcaklığı sonuna ermiş bir su durur.

## Kırba, delik ve kap

[¶16] Ayetin üç kelimesi yan anlamlarıyla birlikte duyulunca bir içme takımının parçalarını da adlandırır. Sulama kökü, suyun ve sütün taşındığı tulumun adıdır: {ar:السقاء القربة للماء واللبن, tr:es-sikâu'l-kırbetu li'l-mâi ve'l-leben, gloss:sikâ su ve süt için kırbadır, source:"س ق ي,B004"}. Göz kelimesi bu kırbanın zayıf yerini adlandırır. Araplar delinmeye yüz tutmuş tulum için {ar:عين السقاء, tr:aynu's-sikâ', gloss:kırbanın gözü, source:"ع ي ن,B007"} derdi. Bu söz, ayetin iki kökünü tek bir terkipte buluşturur. Kırba suyu sıkı derisiyle tutar. Deri eskiyip inceldikçe üzerinde küçük daireler belirir: {ar:بالجلد عين، وهي دوائر رقيقة, tr:bi'l-cildi aynun ve hiye devâiru rakîka, gloss:deride göz var, yani ince daireler, source:"ع ي ن,B007"}. Sonunda tulum tutması gereken suyu tutamaz: {ar:سقاء عين إذا رق فلم يمسك الماء, tr:sikâun ayyinun izâ rakka fe-lem yumsiki'l-mâ', gloss:incelip suyu tutamaz olan kırba, source:"ع ي ن,B007"}. Böyle bir tulumun dikiş yerleri kapansın diye içine su dökülürdü {source:"ع ي ن,B007"}. Sıfat kelimesinin harfleri de kabın çoğuludur: {ar:الإناء ما يوضع فيه الشيء وجمعه آنية, tr:el-inâu mâ yûdau fîhi'ş-şey'u ve cem'uhû âniye, gloss:kap içine bir şey konandır, çoğulu âniyedir, source:"ء ن ي,B004"}.

[¶17] Bu sesler ayetin anlamının yerine geçmez, ama ayetin kurduğu sahnede eksik olan şeyi duyurur. Ayet bir kaynak adlandırır ama bir kap adlandırmaz. Kap ayette yalnızca bir ses olarak, kaynamış suyun sıfatında yankılanır. On dördüncü ayette ise bahçenin kadehleri önceden konmuş olarak hazır durur. Kabın ve kadehin bahçede bulunup burada bulunmaması, surenin iki yarısı arasında kurulan bir sahnedir.

[¶18] Bu ayetin kendi kelimesi ise başka bir kabı, insanın bedenini akla getirir. Araplar karında biriken hastalıklı suyu da sulama fiiliyle söylerdi: {ar:وسقى بطن فلان وذلك ماء أصفر يقع فيه, tr:ve sekâ batnu fülânin ve zâlike mâun asfaru yekau fîh, gloss:falanın karnı su topladı; bu, içine düşen sarı bir sudur, source:"س ق ي,B005"}. Bu hastalığın adı, Musa'nın kavmi için su isteyişini anlatan kelimeyle aynıdır: {ar:استسقى بطنه استسقاء والاسم السقي, tr:isteskâ batnuhû isteskâen ve'l-ismu's-sakyu, gloss:karnı su topladı; hastalığın adı sakydir, source:"س ق ي,B005"}. Aynı fiil bir yerde su istemeyi, başka bir yerde suyun bedende hastalığa dönüşmesini anlatır. Kur'an kaynar suyun bedende ne yaptığını da söyler. Muhammed suresinde takva sahiplerine vaat edilen bahçe anlatılır: orada bozulmayan sudan ırmaklar, tadı değişmeyen sütten ırmaklar vardır. Ardından bunun karşısındaki sorulur: {ar:كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ, tr:ke-men huve hâlidun fi'n-nâri ve sukû mâen hamîmen fe-katta'a em'âehum, gloss:ateşte ebedî kalan ve kaynar su içirilip bağırsakları parçalanan kimse gibi mi, source:47:15}. Orada da fiil edilgendir: içirilirler. Bozulmayan su ile kaynar su, aynı ayetin iki ucunda durur. Vâkıa suresinde ise sol tarafın halkı zakkum ağacından yiyip karınlarını doldurduktan sonra üstüne kaynar su içer: {ar:فَشَٰرِبُونَ عَلَيْهِ مِنَ ٱلْحَمِيمِ, tr:fe-şâribûne aleyhi mine'l-hamîm, gloss:üstüne kaynar sudan içerler, source:56:54}; {ar:فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ, tr:fe-şâribûne şurbe'l-hîm, gloss:susuzluk hastalığına tutulmuş develer gibi içerler, source:56:55}. İçtikçe kanmayan bir içiş, karnında su toplanan hastanın durumuna benzer. Tutamayan kırba, içtikçe kanmayan beden: iki görüntüde de su, tutulması gereken yerde tutulmaz. Altıncı ve yedinci ayette yiyecek ne besler ne açlığı giderir. Beşinci ayette içecek de aynı durumdadır: bir pınardan gelir ama susuzluğu gidermez.

===== _commentary/v16/out/88_5/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: āniya as active participle of anā "reach its term"
- memory: Turkish sâki from sāqī; muayene from muʿāyana
- memory: 77:27 sits among blessings listed to deniers; context described without quoting 77:25-26
- memory: 102 context (rivalry in increase) and 56:52-53 (zaqqum) described from memory, not looked up
- not written: passive tuskā also fits asqā morphologically - unverifiable, would blur the saqā/asqā contrast
- not written: س ق ي B007 heavy rain cloud, B008 papyrus never lacking water - no theme work
- not written: س ق ي B009 dyeing by soaking - no supported link
- not written: س ق ي B010 making a heart drink enmity, with 2:93 "made to drink the calf" - analogy only, different root
- not written: س ق ي B011 backbiting - no link
- not written: siqāya as Yusuf's cup (12:70) - adds nothing to the ayah
- not written: ع ي ن B003, B004, B005, B008-B017 (protection, evil eye, spy, sun, money, notables, wide-eyed) - no theme work here
- not written: ء ن ي B005 "annā" how/whence - no link
- not written: echo roots س و ق and ء و ن - withheld, not identity
- not written: Salih's she-camel water share (26:155, 54:28) - different root, the share idea is carried by B003 alone

===== passages not cited (185) =====
## strong (this ayah's own list) (20)

- (6:70) [listed for 88:5] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (10:4) [listed for 88:5] إِلَيْهِ مَرْجِعُكُمْ جَمِيعًۭا ۖ وَعْدَ ٱللَّهِ حَقًّا ۚ إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ لِيَجْزِىَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ بِٱلْقِسْطِ ۚ وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (14:16) [listed for 88:5] [cited in ¶2] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (14:17) [listed for 88:5] [cited in ¶2] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
- (18:29) [listed for 88:5] [cited in ¶6] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
- (22:19) [listed for 88:5] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
- (22:20) [listed for 88:5] يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ
- (26:79) [listed for 88:5] [cited in ¶2] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (37:67) [listed for 88:5] ثُمَّ إِنَّ لَهُمْ عَلَيْهَا لَشَوْبًۭا مِّنْ حَمِيمٍۢ
- (38:57) [listed for 88:5] هَٰذَا فَلْيَذُوقُوهُ حَمِيمٌۭ وَغَسَّاقٌۭ
- (44:46) [listed for 88:5] كَغَلْىِ ٱلْحَمِيمِ
- (44:48) [listed for 88:5] ثُمَّ صُبُّوا۟ فَوْقَ رَأْسِهِۦ مِنْ عَذَابِ ٱلْحَمِيمِ
- (47:15) [listed for 88:5] [cited in ¶18] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (55:44) [listed for 88:5] [cited in ¶12] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- (56:42) [listed for 88:5] فِى سَمُومٍۢ وَحَمِيمٍۢ
- (56:54) [listed for 88:5] [cited in ¶18] فَشَٰرِبُونَ عَلَيْهِ مِنَ ٱلْحَمِيمِ
- (56:55) [listed for 88:5] [cited in ¶18] فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ
- (56:93) [listed for 88:5] فَنُزُلٌۭ مِّنْ حَمِيمٍۢ
- (78:24) [listed for 88:5] [cited in ¶3] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (78:25) [listed for 88:5] [cited in ¶3] إِلَّا حَمِيمًۭا وَغَسَّاقًۭا

## medium (this ayah's own list) (18)

- (23:21) [listed for 88:5] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهَا وَلَكُمْ فِيهَا مَنَٰفِعُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
- (36:34) [listed for 88:5] وَجَعَلْنَا فِيهَا جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ وَفَجَّرْنَا فِيهَا مِنَ ٱلْعُيُونِ
- (40:71) [listed for 88:5] إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ
- (40:72) [listed for 88:5] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
- (44:52) [listed for 88:5] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (51:15) [listed for 88:5] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (67:30) [listed for 88:5] قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ
- (69:36) [listed for 88:5] وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ
- (76:5) [listed for 88:5] إِنَّ ٱلْأَبْرَارَ يَشْرَبُونَ مِن كَأْسٍۢ كَانَ مِزَاجُهَا كَافُورًا
- (76:6) [listed for 88:5] عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا
- (76:17) [listed for 88:5] وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا
- (76:18) [listed for 88:5] عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا
- (76:21) [listed for 88:5] [cited in ¶2] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:27) [listed for 88:5] [cited in ¶4] وَجَعَلْنَا فِيهَا رَوَٰسِىَ شَٰمِخَٰتٍۢ وَأَسْقَيْنَٰكُم مَّآءًۭ فُرَاتًۭا
- (77:43) [listed for 88:5] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (83:25) [listed for 88:5] يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ
- (83:28) [listed for 88:5] عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ
- (91:13) [listed for 88:5] فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا

## named by the passage's own list as strong for this ayah (9)

- (8:14) [listed for 88:5] ذَٰلِكُمْ فَذُوقُوهُ وَأَنَّ لِلْكَٰفِرِينَ عَذَابَ ٱلنَّارِ
- (44:45) [listed for 88:5] كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ
- (44:49) [listed for 88:5] ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ
- (54:48) [listed for 88:5] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (55:66) [listed for 88:5] فِيهِمَا عَيْنَانِ نَضَّاخَتَانِ
- (56:56) [listed for 88:5] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
- (56:94) [listed for 88:5] وَتَصْلِيَةُ جَحِيمٍ
- (69:31) [listed for 88:5] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
- (78:30) [listed for 88:5] فَذُوقُوا۟ فَلَن نَّزِيدَكُمْ إِلَّا عَذَابًا

## named by the passage's own list as medium for this ayah (33)

- (2:60) [listed for 88:5] [cited in ¶6] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (3:88) [listed for 88:5] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (7:41) [listed for 88:5] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (7:50) [listed for 88:5] [cited in ¶6] وَنَادَىٰٓ أَصْحَٰبُ ٱلنَّارِ أَصْحَٰبَ ٱلْجَنَّةِ أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ ۚ قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ
- (11:106) [listed for 88:5] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (12:41) [listed for 88:5] يَٰصَىٰحِبَىِ ٱلسِّجْنِ أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا ۖ وَأَمَّا ٱلْءَاخَرُ فَيُصْلَبُ فَتَأْكُلُ ٱلطَّيْرُ مِن رَّأْسِهِۦ ۚ قُضِىَ ٱلْأَمْرُ ٱلَّذِى فِيهِ تَسْتَفْتِيَانِ
- (19:71) [listed for 88:5] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (20:74) [listed for 88:5] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (22:21) [listed for 88:5] وَلَهُم مَّقَٰمِعُ مِنْ حَدِيدٍۢ
- (22:22) [listed for 88:5] كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (25:13) [listed for 88:5] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
- (37:68) [listed for 88:5] ثُمَّ إِنَّ مَرْجِعَهُمْ لَإِلَى ٱلْجَحِيمِ
- (38:56) [listed for 88:5] جَهَنَّمَ يَصْلَوْنَهَا فَبِئْسَ ٱلْمِهَادُ
- (38:58) [listed for 88:5] وَءَاخَرُ مِن شَكْلِهِۦٓ أَزْوَٰجٌ
- (46:34) [listed for 88:5] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَلَيْسَ هَٰذَا بِٱلْحَقِّ ۖ قَالُوا۟ بَلَىٰ وَرَبِّنَا ۚ قَالَ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (55:50) [listed for 88:5] فِيهِمَا عَيْنَانِ تَجْرِيَانِ
- (56:18) [listed for 88:5] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:31) [listed for 88:5] وَمَآءٍۢ مَّسْكُوبٍۢ
- (56:43) [listed for 88:5] وَظِلٍّۢ مِّن يَحْمُومٍۢ
- (56:44) [listed for 88:5] لَّا بَارِدٍۢ وَلَا كَرِيمٍ
- (70:15) [listed for 88:5] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (72:16) [listed for 88:5] وَأَلَّوِ ٱسْتَقَٰمُوا۟ عَلَى ٱلطَّرِيقَةِ لَأَسْقَيْنَٰهُم مَّآءً غَدَقًۭا
- (74:30) [listed for 88:5] عَلَيْهَا تِسْعَةَ عَشَرَ
- (76:15) [listed for 88:5] وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠
- (78:23) [listed for 88:5] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (78:34) [listed for 88:5] وَكَأْسًۭا دِهَاقًۭا
- (81:12) [listed for 88:5] وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ
- (82:14) [listed for 88:5] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (83:16) [listed for 88:5] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
- (83:27) [listed for 88:5] وَمِزَاجُهُۥ مِن تَسْنِيمٍ
- (84:12) [listed for 88:5] وَيَصْلَىٰ سَعِيرًا
- (89:23) [listed for 88:5] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (111:3) [listed for 88:5] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

## weak (this ayah's own list) (34)

- (2:25) [listed for 88:5] وَبَشِّرِ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ كُلَّمَا رُزِقُوا۟ مِنْهَا مِن ثَمَرَةٍۢ رِّزْقًۭا ۙ قَالُوا۟ هَٰذَا ٱلَّذِى رُزِقْنَا مِن قَبْلُ ۖ وَأُتُوا۟ بِهِۦ مُتَشَٰبِهًۭا ۖ وَلَهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَهُمْ فِيهَا خَٰلِدُونَ
- (7:116) [listed for 88:5] قَالَ أَلْقُوا۟ ۖ فَلَمَّآ أَلْقَوْا۟ سَحَرُوٓا۟ أَعْيُنَ ٱلنَّاسِ وَٱسْتَرْهَبُوهُمْ وَجَآءُو بِسِحْرٍ عَظِيمٍۢ
- (7:160) [listed for 88:5] وَقَطَّعْنَٰهُمُ ٱثْنَتَىْ عَشْرَةَ أَسْبَاطًا أُمَمًۭا ۚ وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ إِذِ ٱسْتَسْقَىٰهُ قَوْمُهُۥٓ أَنِ ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنۢبَجَسَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۚ وَظَلَّلْنَا عَلَيْهِمُ ٱلْغَمَٰمَ وَأَنزَلْنَا عَلَيْهِمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۚ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (7:179) [listed for 88:5] وَلَقَدْ ذَرَأْنَا لِجَهَنَّمَ كَثِيرًۭا مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا وَلَهُمْ ءَاذَانٌۭ لَّا يَسْمَعُونَ بِهَآ ۚ أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْغَٰفِلُونَ
- (8:44) [listed for 88:5] وَإِذْ يُرِيكُمُوهُمْ إِذِ ٱلْتَقَيْتُمْ فِىٓ أَعْيُنِكُمْ قَلِيلًۭا وَيُقَلِّلُكُمْ فِىٓ أَعْيُنِهِمْ لِيَقْضِىَ ٱللَّهُ أَمْرًۭا كَانَ مَفْعُولًۭا ۗ وَإِلَى ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ
- (9:19) [listed for 88:5] ۞ أَجَعَلْتُمْ سِقَايَةَ ٱلْحَآجِّ وَعِمَارَةَ ٱلْمَسْجِدِ ٱلْحَرَامِ كَمَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَجَٰهَدَ فِى سَبِيلِ ٱللَّهِ ۚ لَا يَسْتَوُۥنَ عِندَ ٱللَّهِ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (12:70) [listed for 88:5] فَلَمَّا جَهَّزَهُم بِجَهَازِهِمْ جَعَلَ ٱلسِّقَايَةَ فِى رَحْلِ أَخِيهِ ثُمَّ أَذَّنَ مُؤَذِّنٌ أَيَّتُهَا ٱلْعِيرُ إِنَّكُمْ لَسَٰرِقُونَ
- (13:4) [listed for 88:5] وَفِى ٱلْأَرْضِ قِطَعٌۭ مُّتَجَٰوِرَٰتٌۭ وَجَنَّٰتٌۭ مِّنْ أَعْنَٰبٍۢ وَزَرْعٌۭ وَنَخِيلٌۭ صِنْوَانٌۭ وَغَيْرُ صِنْوَانٍۢ يُسْقَىٰ بِمَآءٍۢ وَٰحِدٍۢ وَنُفَضِّلُ بَعْضَهَا عَلَىٰ بَعْضٍۢ فِى ٱلْأُكُلِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
- (15:45) [listed for 88:5] إِنَّ ٱلْمُتَّقِينَ فِى جَنَّٰتٍۢ وَعُيُونٍ
- (15:88) [listed for 88:5] لَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ وَلَا تَحْزَنْ عَلَيْهِمْ وَٱخْفِضْ جَنَاحَكَ لِلْمُؤْمِنِينَ
- (21:61) [listed for 88:5] قَالُوا۟ فَأْتُوا۟ بِهِۦ عَلَىٰٓ أَعْيُنِ ٱلنَّاسِ لَعَلَّهُمْ يَشْهَدُونَ
- (26:57) [listed for 88:5] فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍۢ وَعُيُونٍۢ
- (26:134) [listed for 88:5] وَجَنَّٰتٍۢ وَعُيُونٍ
- (26:147) [listed for 88:5] فِى جَنَّٰتٍۢ وَعُيُونٍۢ
- (28:9) [listed for 88:5] وَقَالَتِ ٱمْرَأَتُ فِرْعَوْنَ قُرَّتُ عَيْنٍۢ لِّى وَلَكَ ۖ لَا تَقْتُلُوهُ عَسَىٰٓ أَن يَنفَعَنَآ أَوْ نَتَّخِذَهُۥ وَلَدًۭا وَهُمْ لَا يَشْعُرُونَ
- (28:23) [listed for 88:5] وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ وَوَجَدَ مِن دُونِهِمُ ٱمْرَأَتَيْنِ تَذُودَانِ ۖ قَالَ مَا خَطْبُكُمَا ۖ قَالَتَا لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌۭ كَبِيرٌۭ
- (28:24) [listed for 88:5] فَسَقَىٰ لَهُمَا ثُمَّ تَوَلَّىٰٓ إِلَى ٱلظِّلِّ فَقَالَ رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ
- (32:17) [listed for 88:5] فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (36:66) [listed for 88:5] وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ
- (37:45) [listed for 88:5] يُطَافُ عَلَيْهِم بِكَأْسٍۢ مِّن مَّعِينٍۭ
- (37:163) [listed for 88:5] إِلَّا مَنْ هُوَ صَالِ ٱلْجَحِيمِ
- (43:71) [listed for 88:5] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (44:25) [listed for 88:5] كَمْ تَرَكُوا۟ مِن جَنَّٰتٍۢ وَعُيُونٍۢ
- (44:54) [listed for 88:5] كَذَٰلِكَ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (47:18) [listed for 88:5] فَهَلْ يَنظُرُونَ إِلَّا ٱلسَّاعَةَ أَن تَأْتِيَهُم بَغْتَةًۭ ۖ فَقَدْ جَآءَ أَشْرَاطُهَا ۚ فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ
- (52:20) [listed for 88:5] مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ ۖ وَزَوَّجْنَٰهُم بِحُورٍ عِينٍۢ
- (54:12) [listed for 88:5] وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ
- (56:22) [listed for 88:5] وَحُورٌ عِينٌۭ
- (57:16) [listed for 88:5] [cited in ¶13] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (69:23) [listed for 88:5] قُطُوفُهَا دَانِيَةٌۭ
- (76:16) [listed for 88:5] قَوَارِيرَا۟ مِن فِضَّةٍۢ قَدَّرُوهَا تَقْدِيرًۭا
- (77:41) [listed for 88:5] إِنَّ ٱلْمُتَّقِينَ فِى ظِلَٰلٍۢ وَعُيُونٍۢ
- (90:8) [listed for 88:5] أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- (102:7) [listed for 88:5] [cited in ¶9] ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ

## named by the passage's own list as weak for this ayah (10)

- (25:28) [listed for 88:5] يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا
- (34:12) [listed for 88:5] وَلِسُلَيْمَٰنَ ٱلرِّيحَ غُدُوُّهَا شَهْرٌۭ وَرَوَاحُهَا شَهْرٌۭ ۖ وَأَسَلْنَا لَهُۥ عَيْنَ ٱلْقِطْرِ ۖ وَمِنَ ٱلْجِنِّ مَن يَعْمَلُ بَيْنَ يَدَيْهِ بِإِذْنِ رَبِّهِۦ ۖ وَمَن يَزِغْ مِنْهُمْ عَنْ أَمْرِنَا نُذِقْهُ مِنْ عَذَابِ ٱلسَّعِيرِ
- (54:37) [listed for 88:5] وَلَقَدْ رَٰوَدُوهُ عَن ضَيْفِهِۦ فَطَمَسْنَآ أَعْيُنَهُمْ فَذُوقُوا۟ عَذَابِى وَنُذُرِ
- (55:48) [listed for 88:5] ذَوَاتَآ أَفْنَانٍۢ
- (55:64) [listed for 88:5] مُدْهَآمَّتَانِ
- (56:19) [listed for 88:5] لَّا يُصَدَّعُونَ عَنْهَا وَلَا يُنزِفُونَ
- (56:70) [listed for 88:5] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
- (74:51) [listed for 88:5] فَرَّتْ مِن قَسْوَرَةٍۭ
- (78:32) [listed for 88:5] حَدَآئِقَ وَأَعْنَٰبًۭا
- (83:23) [listed for 88:5] عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ

## neighbours: within two ayat of a passage the commentary cites (61)

- (2:58) [next to 2:60] وَإِذْ قُلْنَا ٱدْخُلُوا۟ هَٰذِهِ ٱلْقَرْيَةَ فَكُلُوا۟ مِنْهَا حَيْثُ شِئْتُمْ رَغَدًۭا وَٱدْخُلُوا۟ ٱلْبَابَ سُجَّدًۭا وَقُولُوا۟ حِطَّةٌۭ نَّغْفِرْ لَكُمْ خَطَٰيَٰكُمْ ۚ وَسَنَزِيدُ ٱلْمُحْسِنِينَ
- (2:59) [next to 2:60] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَنزَلْنَا عَلَى ٱلَّذِينَ ظَلَمُوا۟ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَفْسُقُونَ
- (2:61) [next to 2:60] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (2:62) [next to 2:60] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَادُوا۟ وَٱلنَّصَٰرَىٰ وَٱلصَّٰبِـِٔينَ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَعَمِلَ صَٰلِحًۭا فَلَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:72) [next to 2:74] وَإِذْ قَتَلْتُمْ نَفْسًۭا فَٱدَّٰرَْٰٔتُمْ فِيهَا ۖ وَٱللَّهُ مُخْرِجٌۭ مَّا كُنتُمْ تَكْتُمُونَ
- (2:73) [next to 2:74] فَقُلْنَا ٱضْرِبُوهُ بِبَعْضِهَا ۚ كَذَٰلِكَ يُحْىِ ٱللَّهُ ٱلْمَوْتَىٰ وَيُرِيكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
- (2:75) [next to 2:74] ۞ أَفَتَطْمَعُونَ أَن يُؤْمِنُوا۟ لَكُمْ وَقَدْ كَانَ فَرِيقٌۭ مِّنْهُمْ يَسْمَعُونَ كَلَٰمَ ٱللَّهِ ثُمَّ يُحَرِّفُونَهُۥ مِنۢ بَعْدِ مَا عَقَلُوهُ وَهُمْ يَعْلَمُونَ
- (2:76) [next to 2:74] وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَا بَعْضُهُمْ إِلَىٰ بَعْضٍۢ قَالُوٓا۟ أَتُحَدِّثُونَهُم بِمَا فَتَحَ ٱللَّهُ عَلَيْكُمْ لِيُحَآجُّوكُم بِهِۦ عِندَ رَبِّكُمْ ۚ أَفَلَا تَعْقِلُونَ
- (7:48) [next to 7:50] وَنَادَىٰٓ أَصْحَٰبُ ٱلْأَعْرَافِ رِجَالًۭا يَعْرِفُونَهُم بِسِيمَىٰهُمْ قَالُوا۟ مَآ أَغْنَىٰ عَنكُمْ جَمْعُكُمْ وَمَا كُنتُمْ تَسْتَكْبِرُونَ
- (7:49) [next to 7:50] أَهَٰٓؤُلَآءِ ٱلَّذِينَ أَقْسَمْتُمْ لَا يَنَالُهُمُ ٱللَّهُ بِرَحْمَةٍ ۚ ٱدْخُلُوا۟ ٱلْجَنَّةَ لَا خَوْفٌ عَلَيْكُمْ وَلَآ أَنتُمْ تَحْزَنُونَ
- (7:51) [next to 7:50] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (7:52) [next to 7:50] وَلَقَدْ جِئْنَٰهُم بِكِتَٰبٍۢ فَصَّلْنَٰهُ عَلَىٰ عِلْمٍ هُدًۭى وَرَحْمَةًۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (14:14) [next to 14:16] وَلَنُسْكِنَنَّكُمُ ٱلْأَرْضَ مِنۢ بَعْدِهِمْ ۚ ذَٰلِكَ لِمَنْ خَافَ مَقَامِى وَخَافَ وَعِيدِ
- (14:15) [next to 14:16] وَٱسْتَفْتَحُوا۟ وَخَابَ كُلُّ جَبَّارٍ عَنِيدٍۢ
- (14:18) [next to 14:16] مَّثَلُ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ ۖ لَّا يَقْدِرُونَ مِمَّا كَسَبُوا۟ عَلَىٰ شَىْءٍۢ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
- (14:19) [next to 14:17] أَلَمْ تَرَ أَنَّ ٱللَّهَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (15:20) [next to 15:22] وَجَعَلْنَا لَكُمْ فِيهَا مَعَٰيِشَ وَمَن لَّسْتُمْ لَهُۥ بِرَٰزِقِينَ
- (15:21) [next to 15:22] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
- (15:23) [next to 15:22] وَإِنَّا لَنَحْنُ نُحْىِۦ وَنُمِيتُ وَنَحْنُ ٱلْوَٰرِثُونَ
- (15:24) [next to 15:22] وَلَقَدْ عَلِمْنَا ٱلْمُسْتَقْدِمِينَ مِنكُمْ وَلَقَدْ عَلِمْنَا ٱلْمُسْتَـْٔخِرِينَ
- (18:27) [next to 18:29] وَٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِن كِتَابِ رَبِّكَ ۖ لَا مُبَدِّلَ لِكَلِمَٰتِهِۦ وَلَن تَجِدَ مِن دُونِهِۦ مُلْتَحَدًۭا
- (18:28) [next to 18:29] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (18:30) [next to 18:29] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ إِنَّا لَا نُضِيعُ أَجْرَ مَنْ أَحْسَنَ عَمَلًا
- (18:31) [next to 18:29] أُو۟لَٰٓئِكَ لَهُمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ يُحَلَّوْنَ فِيهَا مِنْ أَسَاوِرَ مِن ذَهَبٍۢ وَيَلْبَسُونَ ثِيَابًا خُضْرًۭا مِّن سُندُسٍۢ وَإِسْتَبْرَقٍۢ مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۚ نِعْمَ ٱلثَّوَابُ وَحَسُنَتْ مُرْتَفَقًۭا
- (26:77) [next to 26:79] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
- (26:78) [next to 26:79] ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ
- (26:80) [next to 26:79] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (26:81) [next to 26:79] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (39:7) [next to 39:9] إِن تَكْفُرُوا۟ فَإِنَّ ٱللَّهَ غَنِىٌّ عَنكُمْ ۖ وَلَا يَرْضَىٰ لِعِبَادِهِ ٱلْكُفْرَ ۖ وَإِن تَشْكُرُوا۟ يَرْضَهُ لَكُمْ ۗ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (39:8) [next to 39:9] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (39:10) [next to 39:9] قُلْ يَٰعِبَادِ ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ رَبَّكُمْ ۚ لِلَّذِينَ أَحْسَنُوا۟ فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةٌۭ ۗ وَأَرْضُ ٱللَّهِ وَٰسِعَةٌ ۗ إِنَّمَا يُوَفَّى ٱلصَّٰبِرُونَ أَجْرَهُم بِغَيْرِ حِسَابٍۢ
- (39:11) [next to 39:9] قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَعْبُدَ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ
- (47:13) [next to 47:15] وَكَأَيِّن مِّن قَرْيَةٍ هِىَ أَشَدُّ قُوَّةًۭ مِّن قَرْيَتِكَ ٱلَّتِىٓ أَخْرَجَتْكَ أَهْلَكْنَٰهُمْ فَلَا نَاصِرَ لَهُمْ
- (47:14) [next to 47:15] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ كَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُم
- (47:16) [next to 47:15] وَمِنْهُم مَّن يَسْتَمِعُ إِلَيْكَ حَتَّىٰٓ إِذَا خَرَجُوا۟ مِنْ عِندِكَ قَالُوا۟ لِلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مَاذَا قَالَ ءَانِفًا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ طَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُمْ
- (47:17) [next to 47:15] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
- (55:41) [next to 55:43] يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ
- (55:42) [next to 55:43] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:45) [next to 55:43] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:47) [next to 55:46] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (56:52) [next to 56:54] لَءَاكِلُونَ مِن شَجَرٍۢ مِّن زَقُّومٍۢ
- (56:53) [next to 56:54] فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (56:57) [next to 56:55] نَحْنُ خَلَقْنَٰكُمْ فَلَوْلَا تُصَدِّقُونَ
- (57:14) [next to 57:16] يُنَادُونَهُمْ أَلَمْ نَكُن مَّعَكُمْ ۖ قَالُوا۟ بَلَىٰ وَلَٰكِنَّكُمْ فَتَنتُمْ أَنفُسَكُمْ وَتَرَبَّصْتُمْ وَٱرْتَبْتُمْ وَغَرَّتْكُمُ ٱلْأَمَانِىُّ حَتَّىٰ جَآءَ أَمْرُ ٱللَّهِ وَغَرَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (57:15) [next to 57:16] فَٱلْيَوْمَ لَا يُؤْخَذُ مِنكُمْ فِدْيَةٌۭ وَلَا مِنَ ٱلَّذِينَ كَفَرُوا۟ ۚ مَأْوَىٰكُمُ ٱلنَّارُ ۖ هِىَ مَوْلَىٰكُمْ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (57:18) [next to 57:16] إِنَّ ٱلْمُصَّدِّقِينَ وَٱلْمُصَّدِّقَٰتِ وَأَقْرَضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا يُضَٰعَفُ لَهُمْ وَلَهُمْ أَجْرٌۭ كَرِيمٌۭ
- (57:19) [next to 57:17] وَٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَرُسُلِهِۦٓ أُو۟لَٰٓئِكَ هُمُ ٱلصِّدِّيقُونَ ۖ وَٱلشُّهَدَآءُ عِندَ رَبِّهِمْ لَهُمْ أَجْرُهُمْ وَنُورُهُمْ ۖ وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَحِيمِ
- (76:19) [next to 76:21] ۞ وَيَطُوفُ عَلَيْهِمْ وِلْدَٰنٌۭ مُّخَلَّدُونَ إِذَا رَأَيْتَهُمْ حَسِبْتَهُمْ لُؤْلُؤًۭا مَّنثُورًۭا
- (76:20) [next to 76:21] وَإِذَا رَأَيْتَ ثَمَّ رَأَيْتَ نَعِيمًۭا وَمُلْكًۭا كَبِيرًا
- (76:22) [next to 76:21] إِنَّ هَٰذَا كَانَ لَكُمْ جَزَآءًۭ وَكَانَ سَعْيُكُم مَّشْكُورًا
- (76:23) [next to 76:21] إِنَّا نَحْنُ نَزَّلْنَا عَلَيْكَ ٱلْقُرْءَانَ تَنزِيلًۭا
- (77:25) [next to 77:27] أَلَمْ نَجْعَلِ ٱلْأَرْضَ كِفَاتًا
- (77:26) [next to 77:27] أَحْيَآءًۭ وَأَمْوَٰتًۭا
- (77:28) [next to 77:27] وَيْلٌۭ يَوْمَئِذٍۢ لِّلْمُكَذِّبِينَ
- (77:29) [next to 77:27] ٱنطَلِقُوٓا۟ إِلَىٰ مَا كُنتُم بِهِۦ تُكَذِّبُونَ
- (78:22) [next to 78:24] لِّلطَّٰغِينَ مَـَٔابًۭا
- (78:26) [next to 78:24] جَزَآءًۭ وِفَاقًا
- (78:27) [next to 78:25] إِنَّهُمْ كَانُوا۟ لَا يَرْجُونَ حِسَابًۭا
- (102:4) [next to 102:6] ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
- (102:5) [next to 102:6] كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
- (102:8) [next to 102:6] ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

