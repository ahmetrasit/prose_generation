Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:11; its ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Lookups: once you have read the whole prompt, gather every passage whose Arabic you want to read (listed or from your own knowledge) and read them together, in one message (several `text` calls side by side when there are more than 40 refs), instead of one lookup at a time while you judge; a later lookup is fine when something new comes up.

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

===== _commentary/v16/out/88_11/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_11.reading.tr.md (prose paragraphs numbered) =====
## Bahçede kulağın payı

[¶1] Bir önceki ayet yeri göstermiştir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüksek bir bahçede, source:88:10}. Akan pınar, yüksek sedirler, konmuş kadehler, dizili yastıklar ve serilmiş halılar sonra gelecektir ve hepsi gözle görülen şeylerdir. Bahçenin içinden verilen ilk bilgi ise görülen bir şey değildir. Kulağın orada karşılaşmayacağı şeyi söyler: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmeu fîhâ lâğiyeten, gloss:orada boş bir söz işitmezsin, source:88:11}. Bahçe önce bir sesin yokluğuyla tarif edilir, nesneleri ancak ondan sonra sayılır.

[¶2] Fiilin öznesi iki türlü anlaşılabilir. Arapçada tesmeu biçimi hem "sen işitirsin" hem de dişil tekil "o işitir" demektir. İlk anlayışta muhatap, surenin başında kendisine soru sorulan kişidir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:o örten günün haberi sana geldi mi, source:88:1}. Haberi kulağıyla almış olan kişiye, şimdi aynı kulağın orada neyle karşılaşmayacağı söylenir. İkinci anlayışta özne, sekizinci ayetteki yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün nimet içinde parlayan yüzler, source:88:8}. Çoğul olan bu kelime Arapçada dişil tekil bir fiille anılabilir. O zaman ayet şunu söylemiş olur: çabasından hoşnut olan o yüzler orada boş söz işitmez. İki anlayış birbirini dışlamaz. Biri haberi dinleyen kişiye bahçeyi vaat eder, öteki bahçedeki yüzlerin kulağını tarif eder.

[¶3] İşitmek, bir şeyi kulakla sezip fark etmektir: {ar:إيناس الشيء بالأذن, tr:înâsu'ş-şey'i bi'l-üzün, gloss:bir şeyi kulakla sezmek, source:"س م ع,B001"}. Kelime yalnızca sesin kulağa çarpmasını anlatmaz, sözü anlamayı ve ona uymayı da kapsar: {ar:تارة عن الفهم وتارة عن الطاعة, tr:târaten ani'l-fehmi ve târaten ani't-tâa, gloss:kimi zaman anlamayı, kimi zaman itaati anlatır, source:"س م ع,B003"}. Bu dilde işitmenin iki yüzü vardı. Birine çirkin söz söyleyip sövdüklerinde Araplar "ona işittirdim" derlerdi: {ar:أسمعته القبيح وشتمته, tr:esma'tühu'l-kabîha ve şetemtüh, gloss:ona çirkini işittirdim, ona sövdüm, source:"س م ع,B006"}. Kulağın hoşlandığı güzel sese de yine işitmeden türeyen bir ad verirlerdi: {ar:السماع اسم ما استلذت الأذن من صوت حسن, tr:es-semâu'smü mâ isteleźźeti'l-üzünü min savtin hasen, gloss:semâ, kulağın tadını aldığı güzel sesin adıdır, source:"س م ع,B007"}. Bu anlamlar ayetteki düz anlamın, yani işitmenin yerine geçmez, onun yanında duyulur. Türkçede semâ deyince dönen dervişler akla gelir. Kelime ise önce kulağın kendisine iyi gelen sesi bulmasının adıydı. Dilde işitmek hem yaralanmanın hem tat almanın kapısıydı. Ayet bu kapıyı kapatmaz, yalnızca bir yanını kapatır. Bahçede kulak açıktır ama ona çirkin söz gelmez.

[¶4] Aynı söz kalıbı Kur'an'da bir başka sessizliği de anlatır. Sur'a üfürüleceği, suçluların toplanacağı ve dağların savrulacağı gün anlatılırken o günün insanları şöyle tarif edilir: {ar:يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:yevmeizin yettebiûne'd-dâiye lâ ivece leh, ve haşaati'l-asvâtu li'r-Rahmâni fe-lâ tesmeu illâ hemsâ, gloss:o gün çağırıcının ardından eğrilmeden giderler; sesler Rahman'ın önünde kısılır, bir fısıltıdan başkasını işitmezsin, source:20:108}. Oradaki "işitmezsin" ile buradaki harfi harfine aynıdır, ama iki sessizlik birbirine benzemez. O günün sessizliği korkudan doğar ve bütün sesleri kısar. Geriye yalnızca bir fısıltı kalır. Bahçenin sessizliği ise seçicidir. Bütün sesleri değil, yalnızca boş sözü kaldırır. Surenin ikinci ayetindeki eğik yüzler o birinci sessizliğin yüzleridir. İki sessizliğin surede karşı karşıya gelişi surenin bütününe ait bir sahnedir.

## Tek bir söz bile

[¶5] Bahçede işitilmeyen şey için seçilen kelime dikkat çeker. Bu tür sözler başka yerlerde boşluk anlamındaki mastarla, lağv ile söylenir. Burada ise lâğiye denir. Bu, tek bir sözü gösteren biçimdir ve tek tek söylenen sözü adlandırır: {ar:لاغية كلمة قبيحة أو فاحشة, tr:lâğiyetun kelimetun kabîhatun ev fâhişe, gloss:lâğiye, çirkin ya da hayasız bir sözdür, source:"ل غ و,B002"}. Kelime boş bir söz olarak da anlaşılabilir, boş konuşan biri olarak da. İkisinde de olumsuzluğun ardından belirsiz ve tekil gelir. Bu yüzden bir türün tamamını kaldırır: orada böyle bir söz bir kere bile işitilmez.

[¶6] Kur'an bu biçimi, bir şeyin hiçbir izinin kalmadığını söylemek için de kullanır. Ad kavminin yedi gece sekiz gün süren bir rüzgârla yok edilişi anlatıldıktan sonra şu soru sorulur: {ar:فَهَلْ تَرَىٰ لَهُم مِّنۢ بَاقِيَةٍۢ, tr:fe-hel terâ lehum min bâkiye, gloss:onlardan geriye kalan bir şey görüyor musun, source:69:8}. Kıyametin gelişini anlatan bir başka surenin açılışında da aynı biçim vardır: {ar:لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ, tr:leyse li-vak'atihâ kâzibe, gloss:onun gelişini yalanlayacak hiçbir şey yoktur, source:56:2}. Orada gözün arayıp bulamadığı bir kalıntı vardır. Burada da kulağın arasa bile bulamayacağı bir söz vardır.

[¶7] Kur'an bahçeyi başka yerlerde de aynı fiille anlatır: {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا, tr:lâ yesmeûne fîhâ lağven ve lâ kizzâbâ, gloss:orada ne boş söz işitirler ne yalan, source:78:35}. Bu ayetlerde fiil çoğuldur, "işitmezler" denir. Kaldırılan şey de lağv, yani bir yığın olarak boş konuşmadır. Ardından çoğu zaman bir ek gelir: ya yanında başka bir kötü söz anılır ya da yerine gelen söz söylenir. Bu surede ise hem dinleyen hem söz tekildir. Ayet hiçbir ek almadan biter ve bir sonraki ayet doğrudan akan pınara geçer. Kalabalık bir sohbetin genel havası değil, tek bir kulak ile tek bir söz arasındaki ilişki anlatılır.

## Hesaba girmeyen söz

[¶8] Kelimenin kökü sözden önce sayıyla ilgili bir şeyi anlatır. Kan bedeli develerle ödendiğinde, sürünün içinde yürüyen yavrular o sayıya katılmazdı. Araplar bunlara lağv derlerdi: {ar:اللغو ما لا يعتد به من أولاد الإبل في الدية, tr:el-lağvu mâ lâ yu'teddü bihî min evlâdi'l-ibili fi'd-diye, gloss:lağv, kan bedelinde sayılmayan deve yavrularıdır, source:"ل غ و,B001"}. Yavrular oradadır, görülür, yürür. Ama borç ödenirken hiçbiri bir deve yerine geçmez. Aynı işlem söze de uygulanırdı. Bir sözü fazlalık sayıp atan kişi şöyle konuşurdu: {ar:ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب, tr:elğaytü hâzihi'l-kelimete ey raeytühâ bâtılen ve fadlen ve haşven ve mâ yulğâ mine'l-hısâb, gloss:bu sözü boş, fazlalık ve dolgu saydım; hesaptan düşülen şey, source:"ل غ و,B001"}. Lağv bu yüzden yalnızca kaba söz değildir. Söylenmiş ama hiçbir ağırlık taşımayan, bir cümleyi dolduran ama hiçbir şey taşımayan sözdür. Türkçede lağvetmek bir kurumu ya da makamı kaldırmak demektir ve bu sözü yalnızca resmî dilde duyarız. Arapçada ise bu kaldırma her gün konuşulan söze olur: söz söylenmiştir ama hiç söylenmemiş gibi hesaptan düşer.

[¶9] Kur'an bu anlamı yeminler hakkında kullanır. Allah müminlere yeminlerinden söz ederken şöyle der: {ar:لَّا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا كَسَبَتْ قُلُوبُكُمْ, tr:lâ yuâhızukumu'llâhu bi'l-lağvi fî eymânikum ve lâkin yuâhızukum bimâ kesebet kulûbukum, gloss:Allah sizi yeminlerinizdeki boş sözden sorumlu tutmaz, kalplerinizin kazandığından sorumlu tutar, source:2:225}. Başka bir yerde karşıtı daha somut söylenir: {ar:وَلَٰكِن يُؤَاخِذُكُم بِمَا عَقَّدتُّمُ ٱلْأَيْمَٰنَ, tr:ve lâkin yuâhızukum bimâ akkadtumu'l-eymân, gloss:sizi bağlayıp düğümlediğiniz yeminlerden sorumlu tutar, source:5:89}. Yeminin boşu, kalbin düğümlemediği yemindir: {ar:لغو الأيمان ما لم تعقدوه بقلوبكم وما لا عقد عليه, tr:lağvu'l-eymâni mâ lem ta'kidûhu bi-kulûbikum ve mâ lâ akde aleyh, gloss:yeminin boşu kalplerinizle bağlamadığınız, düğümü olmayan yemindir, source:"ل غ و,B001"}. Ağızdan çıkar ama hiçbir yere bağlanmaz. Dünyada böyle bir söz bağışlanır, çünkü hesaba girmez. Bahçe ise boş sözün bağışlandığı bir yer olarak değil, hiç doğmadığı bir yer olarak anlatılır.

[¶10] Kökün bir kolu, boş sözün söyleyeni eli boş bırakmasını da anlatır. Birini umduğundan yoksun bırakana {ar:ألغيته أي خيبته, tr:elğaytühû ey hayyebtüh, gloss:onu eli boş çevirdim, source:"ل غ و,B006"} denirdi. Boş söz kimseye bir şey kazandırmaz, söyleyenine bile. Dokuzuncu ayetteki yüz ise çabasından hoşnuttur: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnut, source:88:9}. Bu yüzün emeği karşılıksız kalmamıştır. Bulunduğu yerde de hesaba girmeyen tek bir söz işitilmez. Sayılmayan söz ile surenin son ayetindeki sayım arasındaki bağ surenin bütününe ait bir sahnedir: {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra onların hesabı da Bize aittir, source:88:26}.

## Kulağı dolduran gürültü

[¶11] Kökün bir başka kolunda söz bile yoktur, yalnızca ses vardır: {ar:اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا, tr:el-leğâ es-savtu misle'l-vağâ ve nubâhu'l-kelbi lağvun eydan, gloss:leğâ, savaş uğultusu gibi sestir; köpeğin havlaması da lağvdır, source:"ل غ و,B003"}. Kuşların cıvıltısına da bu ad verilirdi: {ar:اللغا صوت العصافير ونحوها من الطيور, tr:el-leğâ savtu'l-asâfîri ve nahvihâ mine't-tuyûr, gloss:leğâ, serçelerin ve benzeri kuşların sesidir, source:"ل غ و,B003"}. Bunlar insanı rahatsız eden ama hiçbir şey söylemeyen seslerdir. Havlama bir şeyi bildirmez, uğultu bir sözü taşımaz. Bu anlamın yanında ayet şunu da duyurur: bahçede kulağı anlamsız bir uğultu doldurmaz.

[¶12] Bir başka kol, dilin kendi içinden bir takıntıyı anlatır. Bir şeye takılıp onu dilinden düşürmeyene {ar:لغى بالأمر إذا لهج به, tr:leğiye bi'l-emri izâ lehice bih, gloss:bir işi dilinden düşürmedi, ona takıldı, source:"ل غ و,B004"} denirdi. Topluluk topluluk dilden düşürülmeyen konuşmaya da aynı yerden ad verilmiştir: {ar:لغي بكذا أي لهج به ومنه قيل للكلام الذي يلهج به فرقة فرقة لغة, tr:leğiye bi-kezâ ey lehice bih, ve minhu kîle li'l-kelâmi'llezî yelhecu bihî firkatun firkatun luğa, gloss:bir şeyi dilinden düşürmedi; her topluluğun dilinden düşürmediği konuşmaya bu yüzden luga, yani dil denmiştir, source:"ل غ و,B004"}. Böylece aynı kök, insanların dilini de o dilin artığını da adlandırır. Dil kalır, onu dolduran boş tekrar, dolgu ve gürültü düşer.

[¶13] Kur'an bu gürültüyü bir sahnede gösterir ve sahnede bu ayetin iki kelimesi birlikte geçer. İnkârcılara yakın arkadaşlar verilmiş, bunlar onlara önlerindekini ve arkalarındakini süslü göstermiştir. Ardından inkârcıların kendi aralarındaki emri aktarılır: {ar:وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَسْمَعُوا۟ لِهَٰذَا ٱلْقُرْءَانِ وَٱلْغَوْا۟ فِيهِ لَعَلَّكُمْ تَغْلِبُونَ, tr:ve kâle'llezîne keferû lâ tesmeû li-hâza'l-Kur'âni ve'lğav fîhi lealleküm tağlibûn, gloss:inkâr edenler dedi ki: bu Kur'an'ı dinlemeyin, okunurken gürültü yapın, belki üstün gelirsiniz, source:41:26}. Bu gürültüde amaç, sesi yükseltip okunanı duyulmaz hale getirmektir: {ar:والغوا فيه يعني رفع الصوت بالكلام ليغلطوا المسلمين, tr:ve'lğav fîhi ya'nî ref'a's-savti bi'l-kelâmi li-yuğallitu'l-müslimîn, gloss:gürültü yapın, yani müslümanları şaşırtmak için konuşarak sesi yükseltin, source:"ل غ و,B003"}. Hemen ardından Allah onlara çetin bir azap tattıracağını söyler {source:41:27}. O sahnede işitmek yasaklanmış ve gürültü emredilmiştir. Bahçede ise tam tersi olur: işitmek kalır, gürültü kalkar. Dünyada sözün üstünü örtmek için çıkarılan ses, bahçeye hiç girmez. Surenin yirmi birinci ayetinde Peygamber'e "hatırlat" denir. Bu hatırlatma da kulağa ulaşmak zorunda olan bir sözdür ve onun bu ayetle buluşması surenin bütününe aittir.

## Dünyada geçip gidilen, bahçede hiç gelmeyen söz

[¶14] Dünyada boş söz kulağa gelir ve kulak onu geri çeviremez. Kur'an müminleri bu yüzden işitmemekle değil, yüz çevirmekle över. Kurtuluşa eren müminler sayılırken ilk iki nitelik art arda gelir: {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşiûn, gloss:onlar namazlarında içten eğilirler, source:23:2}; {ar:وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ, tr:vellezîne hum ani'l-lağvi mu'ridûn, gloss:onlar boş sözden yüz çevirirler, source:23:3}. Orada aynı insanlarda bulunan iki nitelik, bu surede iki ayrı yüz grubuna dağılmış gibidir. İkinci ayetteki eğiklik zorla gelen bir eğikliktir. Boş sözden kurtulmak ise sekizinci ayetteki yüzlerin bahçesine aittir.

[¶15] Rahman'ın kulları anlatılırken de aynı tavır görülür: {ar:وَإِذَا مَرُّوا۟ بِٱللَّغْوِ مَرُّوا۟ كِرَامًۭا, tr:ve izâ merrû bi'l-lağvi merrû kirâmâ, gloss:boş sözün yanından geçtiklerinde onurlu bir şekilde geçip giderler, source:25:72}. Bu kullar, cahiller kendilerine laf attığında da {ar:قَالُوا۟ سَلَٰمًۭا, tr:kâlû selâmâ, gloss:selam derler, source:25:63}. Daha önce kendilerine kitap verilmiş olup Kur'an okunduğunda ona inananlar için de bu sahne daha ayrıntılı anlatılır. Bunlara sabırları yüzünden ecirleri iki kat verilir {source:28:54}. Boş söz karşısındaki tavırları da şöyledir: {ar:وَإِذَا سَمِعُوا۟ ٱللَّغْوَ أَعْرَضُوا۟ عَنْهُ وَقَالُوا۟ لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ سَلَٰمٌ عَلَيْكُمْ لَا نَبْتَغِى ٱلْجَٰهِلِينَ, tr:ve izâ semiu'l-lağve a'radû anhu ve kâlû lenâ a'mâlunâ ve leküm a'mâlüküm selâmün aleyküm lâ nebteği'l-câhilîn, gloss:boş söz işittiklerinde ondan yüz çevirirler ve derler ki: bizim işlerimiz bize, sizin işleriniz size; selam size, biz cahilleri istemeyiz, source:28:55}. Burada fiil olumludur: işittiler. Dünyada boş söz kulağa ulaşır. Mümin onu duymazdan gelemez. Ondan yüz çevirir ve karşılığında selam der.

[¶16] Bahçe bu dünyadaki sahnenin tamamlanmış halidir. Rahman'ın kullarına gaipte vaat ettiği Adn bahçeleri anlatılırken şöyle denir: {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا, tr:lâ yesmeûne fîhâ lağven illâ selâmâ, gloss:orada boş söz değil, yalnızca selam işitirler, source:19:62}. Rabbe yaklaştırılmışlar anlatılırken de aynı şey söylenir: {ar:لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا, tr:lâ yesmeûne fîhâ lağven ve lâ te'sîmâ, gloss:orada ne boş söz işitirler ne günaha sokan söz, source:56:25}; {ar:إِلَّا قِيلًۭا سَلَٰمًۭا سَلَٰمًۭا, tr:illâ kîlen selâmen selâmâ, gloss:yalnızca selam, selam diye bir söz, source:56:26}. Dünyada müminin boş söze verdiği cevap selamdı. Bahçede boş söz ortadan kalkar ve ona verilen cevap, işitilen sözün tamamı olur. Dünyada selam boş sözü uzaklaştırmak için söylenirdi. Bahçede ise uzaklaştırılacak bir şey kalmamıştır ve selam yalnızca kendisi için söylenir. Bu surenin ayeti selamı anmaz. Yalnızca boş sözün yokluğunu söyler. Ama bu yokluk, öteki ayetlerin selamla doldurduğu yeri boşaltır.

[¶17] Kur'an bu sessizliği birkaç yerde kadehin hemen yanında anar. Takva sahiplerinin bahçesinde {ar:يَتَنَٰزَعُونَ فِيهَا كَأْسًۭا لَّا لَغْوٌۭ فِيهَا وَلَا تَأْثِيمٌۭ, tr:yetenâzeûne fîhâ ke'sen lâ lağvun fîhâ ve lâ te'sîm, gloss:orada birbirlerine bir kadeh uzatırlar; o kadehte ne boş söz vardır ne günaha sokma, source:52:23}. Yaklaştırılmışlara sunulan kadehler ve testiler anlatılırken başlarının ağrımayacağı ve akıllarının gitmeyeceği söylenir: {ar:لَّا يُصَدَّعُونَ عَنْهَا وَلَا يُنزِفُونَ, tr:lâ yusadda'ûne anhâ ve lâ yünzifûn, gloss:ondan başları ağrımaz, akılları da gitmez, source:56:19}. Boş sözün yokluğu da bu tarifin hemen ardından gelir. Takva sahiplerine ağzına kadar dolu bir kadeh verileceği söylendikten sonra da aynı şey söylenir {source:78:34}. Dünyada içki ile boş söz birbirini çağırır. Araplar içkiye düşüp çok içene bu kökten bir fiille {ar:لغي بالشراب أكثر منه, tr:leğiye bi'ş-şarâbi ekesera minh, gloss:içkiye düştü, ondan çok içti, source:"ل غ و,B004"} derlerdi. Bahçenin kadehi ise dili çözüp boş konuşturmaz. Bu surenin on dördüncü ayetindeki konmuş kadehlerin bu ayetteki sessizlikle oluşturduğu sahne surenin bütününe aittir: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}.

===== _commentary/v16/out/88_11/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: tasmaʿu read as 2nd masc. sg. or 3rd fem. sg. with broken plural wujūh as subject
- memory: lāghiya as fāʿila-form noun (like kāḏiba, bāqiya) or adjective of an implied word/speaker
- memory: indefinite singular after lā negates the whole kind
- memory: Turkish lağvetmek = abolish an office; Turkish semâ = dervish ceremony
- not written: passive reading lā tusmaʿu/yusmaʿu fīhā lāghiyatun - reading report outside the supplied texts
- not written: ل غ و B006 Friday-sermon usage - hadith-based, outside the Quran
- not written: ل غ و B002 Qatada/Mujahid glosses - exegetes' views
- not written: ل غ و B005 swerving from the right - adds nothing beyond B002
- not written: س م ع B008 bucket "ear" handle - link to flowing spring only analogy
- not written: س م ع B005 reputation/showing off - no support in the ayah
- not written: س م ع B011 "heard but not reaching me" - no theme to join
- not written: س م ع B014 between earth's hearing and sight - no theme to join
- not written: س م ع B009, B010, B012, B013, B015, B016 - unrelated to the ayah
- not written: rhyme ghāshiya/lāghiya - sound echo only, not root

===== passages not cited (170) =====
## strong (this ayah's own list) (3)

- (41:26) [listed for 88:11] [cited in ¶13] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَسْمَعُوا۟ لِهَٰذَا ٱلْقُرْءَانِ وَٱلْغَوْا۟ فِيهِ لَعَلَّكُمْ تَغْلِبُونَ
- (56:25) [listed for 88:11] [cited in ¶16] لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا
- (78:35) [listed for 88:11] [cited in ¶7] لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا

## medium (this ayah's own list) (42)

- (5:83) [listed for 88:11] وَإِذَا سَمِعُوا۟ مَآ أُنزِلَ إِلَى ٱلرَّسُولِ تَرَىٰٓ أَعْيُنَهُمْ تَفِيضُ مِنَ ٱلدَّمْعِ مِمَّا عَرَفُوا۟ مِنَ ٱلْحَقِّ ۖ يَقُولُونَ رَبَّنَآ ءَامَنَّا فَٱكْتُبْنَا مَعَ ٱلشَّٰهِدِينَ
- (7:43) [listed for 88:11] وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّۢ تَجْرِى مِن تَحْتِهِمُ ٱلْأَنْهَٰرُ ۖ وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى هَدَىٰنَا لِهَٰذَا وَمَا كُنَّا لِنَهْتَدِىَ لَوْلَآ أَنْ هَدَىٰنَا ٱللَّهُ ۖ لَقَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ ۖ وَنُودُوٓا۟ أَن تِلْكُمُ ٱلْجَنَّةُ أُورِثْتُمُوهَا بِمَا كُنتُمْ تَعْمَلُونَ
- (7:204) [listed for 88:11] وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (9:6) [listed for 88:11] وَإِنْ أَحَدٌۭ مِّنَ ٱلْمُشْرِكِينَ ٱسْتَجَارَكَ فَأَجِرْهُ حَتَّىٰ يَسْمَعَ كَلَٰمَ ٱللَّهِ ثُمَّ أَبْلِغْهُ مَأْمَنَهُۥ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْلَمُونَ
- (10:10) [listed for 88:11] دَعْوَىٰهُمْ فِيهَا سُبْحَٰنَكَ ٱللَّهُمَّ وَتَحِيَّتُهُمْ فِيهَا سَلَٰمٌۭ ۚ وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (10:42) [listed for 88:11] وَمِنْهُم مَّن يَسْتَمِعُونَ إِلَيْكَ ۚ أَفَأَنتَ تُسْمِعُ ٱلصُّمَّ وَلَوْ كَانُوا۟ لَا يَعْقِلُونَ
- (13:24) [listed for 88:11] سَلَٰمٌ عَلَيْكُم بِمَا صَبَرْتُمْ ۚ فَنِعْمَ عُقْبَى ٱلدَّارِ
- (14:23) [listed for 88:11] وَأُدْخِلَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا بِإِذْنِ رَبِّهِمْ ۖ تَحِيَّتُهُمْ فِيهَا سَلَٰمٌ
- (15:47) [listed for 88:11] وَنَزَعْنَا مَا فِى صُدُورِهِم مِّنْ غِلٍّ إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ
- (16:32) [listed for 88:11] ٱلَّذِينَ تَتَوَفَّىٰهُمُ ٱلْمَلَٰٓئِكَةُ طَيِّبِينَ ۙ يَقُولُونَ سَلَٰمٌ عَلَيْكُمُ ٱدْخُلُوا۟ ٱلْجَنَّةَ بِمَا كُنتُمْ تَعْمَلُونَ
- (19:62) [listed for 88:11] [cited in ¶16] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (20:13) [listed for 88:11] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
- (20:108) [listed for 88:11] [cited in ¶4] يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا
- (21:100) [listed for 88:11] لَهُمْ فِيهَا زَفِيرٌۭ وَهُمْ فِيهَا لَا يَسْمَعُونَ
- (21:102) [listed for 88:11] لَا يَسْمَعُونَ حَسِيسَهَا ۖ وَهُمْ فِى مَا ٱشْتَهَتْ أَنفُسُهُمْ خَٰلِدُونَ
- (23:3) [listed for 88:11] [cited in ¶14] وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ
- (24:12) [listed for 88:11] لَّوْلَآ إِذْ سَمِعْتُمُوهُ ظَنَّ ٱلْمُؤْمِنُونَ وَٱلْمُؤْمِنَٰتُ بِأَنفُسِهِمْ خَيْرًۭا وَقَالُوا۟ هَٰذَآ إِفْكٌۭ مُّبِينٌۭ
- (25:72) [listed for 88:11] [cited in ¶15] وَٱلَّذِينَ لَا يَشْهَدُونَ ٱلزُّورَ وَإِذَا مَرُّوا۟ بِٱللَّغْوِ مَرُّوا۟ كِرَامًۭا
- (25:75) [listed for 88:11] أُو۟لَٰٓئِكَ يُجْزَوْنَ ٱلْغُرْفَةَ بِمَا صَبَرُوا۟ وَيُلَقَّوْنَ فِيهَا تَحِيَّةًۭ وَسَلَٰمًا
- (27:80) [listed for 88:11] إِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (28:55) [listed for 88:11] [cited in ¶15] وَإِذَا سَمِعُوا۟ ٱللَّغْوَ أَعْرَضُوا۟ عَنْهُ وَقَالُوا۟ لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ سَلَٰمٌ عَلَيْكُمْ لَا نَبْتَغِى ٱلْجَٰهِلِينَ
- (30:52) [listed for 88:11] فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (35:22) [listed for 88:11] وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ ۚ إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ ۖ وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ
- (35:34) [listed for 88:11] وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَذْهَبَ عَنَّا ٱلْحَزَنَ ۖ إِنَّ رَبَّنَا لَغَفُورٌۭ شَكُورٌ
- (35:35) [listed for 88:11] ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ
- (36:58) [listed for 88:11] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (37:8) [listed for 88:11] لَّا يَسَّمَّعُونَ إِلَى ٱلْمَلَإِ ٱلْأَعْلَىٰ وَيُقْذَفُونَ مِن كُلِّ جَانِبٍۢ
- (37:50) [listed for 88:11] فَأَقْبَلَ بَعْضُهُمْ عَلَىٰ بَعْضٍۢ يَتَسَآءَلُونَ
- (39:73) [listed for 88:11] وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا وَفُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَا سَلَٰمٌ عَلَيْكُمْ طِبْتُمْ فَٱدْخُلُوهَا خَٰلِدِينَ
- (39:74) [listed for 88:11] وَقَالُوا۟ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى صَدَقَنَا وَعْدَهُۥ وَأَوْرَثَنَا ٱلْأَرْضَ نَتَبَوَّأُ مِنَ ٱلْجَنَّةِ حَيْثُ نَشَآءُ ۖ فَنِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- (41:4) [listed for 88:11] بَشِيرًۭا وَنَذِيرًۭا فَأَعْرَضَ أَكْثَرُهُمْ فَهُمْ لَا يَسْمَعُونَ
- (46:26) [listed for 88:11] وَلَقَدْ مَكَّنَّٰهُمْ فِيمَآ إِن مَّكَّنَّٰكُمْ فِيهِ وَجَعَلْنَا لَهُمْ سَمْعًۭا وَأَبْصَٰرًۭا وَأَفْـِٔدَةًۭ فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ وَلَآ أَفْـِٔدَتُهُم مِّن شَىْءٍ إِذْ كَانُوا۟ يَجْحَدُونَ بِـَٔايَٰتِ ٱللَّهِ وَحَاقَ بِهِم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (46:30) [listed for 88:11] قَالُوا۟ يَٰقَوْمَنَآ إِنَّا سَمِعْنَا كِتَٰبًا أُنزِلَ مِنۢ بَعْدِ مُوسَىٰ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ يَهْدِىٓ إِلَى ٱلْحَقِّ وَإِلَىٰ طَرِيقٍۢ مُّسْتَقِيمٍۢ
- (50:42) [listed for 88:11] يَوْمَ يَسْمَعُونَ ٱلصَّيْحَةَ بِٱلْحَقِّ ۚ ذَٰلِكَ يَوْمُ ٱلْخُرُوجِ
- (52:23) [listed for 88:11] [cited in ¶17] يَتَنَٰزَعُونَ فِيهَا كَأْسًۭا لَّا لَغْوٌۭ فِيهَا وَلَا تَأْثِيمٌۭ
- (52:25) [listed for 88:11] وَأَقْبَلَ بَعْضُهُمْ عَلَىٰ بَعْضٍۢ يَتَسَآءَلُونَ
- (56:26) [listed for 88:11] [cited in ¶16] إِلَّا قِيلًۭا سَلَٰمًۭا سَلَٰمًۭا
- (63:4) [listed for 88:11] ۞ وَإِذَا رَأَيْتَهُمْ تُعْجِبُكَ أَجْسَامُهُمْ ۖ وَإِن يَقُولُوا۟ تَسْمَعْ لِقَوْلِهِمْ ۖ كَأَنَّهُمْ خُشُبٌۭ مُّسَنَّدَةٌۭ ۖ يَحْسَبُونَ كُلَّ صَيْحَةٍ عَلَيْهِمْ ۚ هُمُ ٱلْعَدُوُّ فَٱحْذَرْهُمْ ۚ قَٰتَلَهُمُ ٱللَّهُ ۖ أَنَّىٰ يُؤْفَكُونَ
- (67:7) [listed for 88:11] إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ
- (67:10) [listed for 88:11] وَقَالُوا۟ لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ مَا كُنَّا فِىٓ أَصْحَٰبِ ٱلسَّعِيرِ
- (72:1) [listed for 88:11] قُلْ أُوحِىَ إِلَىَّ أَنَّهُ ٱسْتَمَعَ نَفَرٌۭ مِّنَ ٱلْجِنِّ فَقَالُوٓا۟ إِنَّا سَمِعْنَا قُرْءَانًا عَجَبًۭا
- (72:13) [listed for 88:11] وَأَنَّا لَمَّا سَمِعْنَا ٱلْهُدَىٰٓ ءَامَنَّا بِهِۦ ۖ فَمَن يُؤْمِنۢ بِرَبِّهِۦ فَلَا يَخَافُ بَخْسًۭا وَلَا رَهَقًۭا

## named by the passage's own list as strong for this ayah (6)

- (36:55) [listed for 88:11] إِنَّ أَصْحَٰبَ ٱلْجَنَّةِ ٱلْيَوْمَ فِى شُغُلٍۢ فَٰكِهُونَ
- (37:42) [listed for 88:11] فَوَٰكِهُ ۖ وَهُم مُّكْرَمُونَ
- (41:32) [listed for 88:11] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ
- (56:12) [listed for 88:11] فِى جَنَّٰتِ ٱلنَّعِيمِ
- (77:43) [listed for 88:11] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ
- (78:24) [listed for 88:11] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا

## named by the passage's own list as medium for this ayah (19)

- (2:225) [listed for 88:11] [cited in ¶9] لَّا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا كَسَبَتْ قُلُوبُكُمْ ۗ وَٱللَّهُ غَفُورٌ حَلِيمٌۭ
- (43:71) [listed for 88:11] يُطَافُ عَلَيْهِم بِصِحَافٍۢ مِّن ذَهَبٍۢ وَأَكْوَابٍۢ ۖ وَفِيهَا مَا تَشْتَهِيهِ ٱلْأَنفُسُ وَتَلَذُّ ٱلْأَعْيُنُ ۖ وَأَنتُمْ فِيهَا خَٰلِدُونَ
- (44:55) [listed for 88:11] يَدْعُونَ فِيهَا بِكُلِّ فَٰكِهَةٍ ءَامِنِينَ
- (44:56) [listed for 88:11] لَا يَذُوقُونَ فِيهَا ٱلْمَوْتَ إِلَّا ٱلْمَوْتَةَ ٱلْأُولَىٰ ۖ وَوَقَىٰهُمْ عَذَابَ ٱلْجَحِيمِ
- (52:18) [listed for 88:11] فَٰكِهِينَ بِمَآ ءَاتَىٰهُمْ رَبُّهُمْ وَوَقَىٰهُمْ رَبُّهُمْ عَذَابَ ٱلْجَحِيمِ
- (55:66) [listed for 88:11] فِيهِمَا عَيْنَانِ نَضَّاخَتَانِ
- (56:15) [listed for 88:11] عَلَىٰ سُرُرٍۢ مَّوْضُونَةٍۢ
- (56:34) [listed for 88:11] وَفُرُشٍۢ مَّرْفُوعَةٍ
- (56:89) [listed for 88:11] فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ
- (69:24) [listed for 88:11] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ
- (76:13) [listed for 88:11] مُّتَّكِـِٔينَ فِيهَا عَلَى ٱلْأَرَآئِكِ ۖ لَا يَرَوْنَ فِيهَا شَمْسًۭا وَلَا زَمْهَرِيرًۭا
- (76:21) [listed for 88:11] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (77:35) [listed for 88:11] هَٰذَا يَوْمُ لَا يَنطِقُونَ
- (77:42) [listed for 88:11] وَفَوَٰكِهَ مِمَّا يَشْتَهُونَ
- (78:34) [listed for 88:11] [cited in ¶17] وَكَأْسًۭا دِهَاقًۭا
- (83:22) [listed for 88:11] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (83:26) [listed for 88:11] خِتَٰمُهُۥ مِسْكٌۭ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ
- (87:13) [listed for 88:11] ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (101:7) [listed for 88:11] فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

## weak (this ayah's own list) (32)

- (2:181) [listed for 88:11] فَمَنۢ بَدَّلَهُۥ بَعْدَمَا سَمِعَهُۥ فَإِنَّمَآ إِثْمُهُۥ عَلَى ٱلَّذِينَ يُبَدِّلُونَهُۥٓ ۚ إِنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (4:5) [listed for 88:11] وَلَا تُؤْتُوا۟ ٱلسُّفَهَآءَ أَمْوَٰلَكُمُ ٱلَّتِى جَعَلَ ٱللَّهُ لَكُمْ قِيَٰمًۭا وَٱرْزُقُوهُمْ فِيهَا وَٱكْسُوهُمْ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا
- (5:89) [listed for 88:11] [cited in ¶9] لَا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا عَقَّدتُّمُ ٱلْأَيْمَٰنَ ۖ فَكَفَّٰرَتُهُۥٓ إِطْعَامُ عَشَرَةِ مَسَٰكِينَ مِنْ أَوْسَطِ مَا تُطْعِمُونَ أَهْلِيكُمْ أَوْ كِسْوَتُهُمْ أَوْ تَحْرِيرُ رَقَبَةٍۢ ۖ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ ۚ ذَٰلِكَ كَفَّٰرَةُ أَيْمَٰنِكُمْ إِذَا حَلَفْتُمْ ۚ وَٱحْفَظُوٓا۟ أَيْمَٰنَكُمْ ۚ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَشْكُرُونَ
- (6:115) [listed for 88:11] وَتَمَّتْ كَلِمَتُ رَبِّكَ صِدْقًۭا وَعَدْلًۭا ۚ لَّا مُبَدِّلَ لِكَلِمَٰتِهِۦ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (7:200) [listed for 88:11] وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ ۚ إِنَّهُۥ سَمِيعٌ عَلِيمٌ
- (11:106) [listed for 88:11] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (12:31) [listed for 88:11] فَلَمَّا سَمِعَتْ بِمَكْرِهِنَّ أَرْسَلَتْ إِلَيْهِنَّ وَأَعْتَدَتْ لَهُنَّ مُتَّكَـًۭٔا وَءَاتَتْ كُلَّ وَٰحِدَةٍۢ مِّنْهُنَّ سِكِّينًۭا وَقَالَتِ ٱخْرُجْ عَلَيْهِنَّ ۖ فَلَمَّا رَأَيْنَهُۥٓ أَكْبَرْنَهُۥ وَقَطَّعْنَ أَيْدِيَهُنَّ وَقُلْنَ حَٰشَ لِلَّهِ مَا هَٰذَا بَشَرًا إِنْ هَٰذَآ إِلَّا مَلَكٌۭ كَرِيمٌۭ
- (15:48) [listed for 88:11] لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ وَمَا هُم مِّنْهَا بِمُخْرَجِينَ
- (16:65) [listed for 88:11] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
- (18:108) [listed for 88:11] خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا
- (19:38) [listed for 88:11] أَسْمِعْ بِهِمْ وَأَبْصِرْ يَوْمَ يَأْتُونَنَا ۖ لَٰكِنِ ٱلظَّٰلِمُونَ ٱلْيَوْمَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (20:46) [listed for 88:11] قَالَ لَا تَخَافَآ ۖ إِنَّنِى مَعَكُمَآ أَسْمَعُ وَأَرَىٰ
- (20:107) [listed for 88:11] لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا
- (20:118) [listed for 88:11] إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ
- (20:119) [listed for 88:11] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (21:60) [listed for 88:11] قَالُوا۟ سَمِعْنَا فَتًۭى يَذْكُرُهُمْ يُقَالُ لَهُۥٓ إِبْرَٰهِيمُ
- (25:12) [listed for 88:11] إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا
- (26:15) [listed for 88:11] قَالَ كَلَّا ۖ فَٱذْهَبَا بِـَٔايَٰتِنَآ ۖ إِنَّا مَعَكُم مُّسْتَمِعُونَ
- (26:72) [listed for 88:11] قَالَ هَلْ يَسْمَعُونَكُمْ إِذْ تَدْعُونَ
- (26:210) [listed for 88:11] وَمَا تَنَزَّلَتْ بِهِ ٱلشَّيَٰطِينُ
- (26:212) [listed for 88:11] إِنَّهُمْ عَنِ ٱلسَّمْعِ لَمَعْزُولُونَ
- (36:25) [listed for 88:11] إِنِّىٓ ءَامَنتُ بِرَبِّكُمْ فَٱسْمَعُونِ
- (37:47) [listed for 88:11] لَا فِيهَا غَوْلٌۭ وَلَا هُمْ عَنْهَا يُنزَفُونَ
- (37:92) [listed for 88:11] مَا لَكُمْ لَا تَنطِقُونَ
- (38:7) [listed for 88:11] مَا سَمِعْنَا بِهَٰذَا فِى ٱلْمِلَّةِ ٱلْءَاخِرَةِ إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ
- (41:20) [listed for 88:11] حَتَّىٰٓ إِذَا مَا جَآءُوهَا شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم بِمَا كَانُوا۟ يَعْمَلُونَ
- (41:36) [listed for 88:11] وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ ۖ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (43:40) [listed for 88:11] أَفَأَنتَ تُسْمِعُ ٱلصُّمَّ أَوْ تَهْدِى ٱلْعُمْىَ وَمَن كَانَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (52:38) [listed for 88:11] أَمْ لَهُمْ سُلَّمٌۭ يَسْتَمِعُونَ فِيهِ ۖ فَلْيَأْتِ مُسْتَمِعُهُم بِسُلْطَٰنٍۢ مُّبِينٍ
- (58:1) [listed for 88:11] قَدْ سَمِعَ ٱللَّهُ قَوْلَ ٱلَّتِى تُجَٰدِلُكَ فِى زَوْجِهَا وَتَشْتَكِىٓ إِلَى ٱللَّهِ وَٱللَّهُ يَسْمَعُ تَحَاوُرَكُمَآ ۚ إِنَّ ٱللَّهَ سَمِيعٌۢ بَصِيرٌ
- (67:23) [listed for 88:11] قُلْ هُوَ ٱلَّذِىٓ أَنشَأَكُمْ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۖ قَلِيلًۭا مَّا تَشْكُرُونَ
- (69:22) [listed for 88:11] فِى جَنَّةٍ عَالِيَةٍۢ

## named by the passage's own list as weak for this ayah (10)

- (4:140) [listed for 88:11] وَقَدْ نَزَّلَ عَلَيْكُمْ فِى ٱلْكِتَٰبِ أَنْ إِذَا سَمِعْتُمْ ءَايَٰتِ ٱللَّهِ يُكْفَرُ بِهَا وَيُسْتَهْزَأُ بِهَا فَلَا تَقْعُدُوا۟ مَعَهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦٓ ۚ إِنَّكُمْ إِذًۭا مِّثْلُهُمْ ۗ إِنَّ ٱللَّهَ جَامِعُ ٱلْمُنَٰفِقِينَ وَٱلْكَٰفِرِينَ فِى جَهَنَّمَ جَمِيعًا
- (18:3) [listed for 88:11] مَّٰكِثِينَ فِيهِ أَبَدًۭا
- (19:98) [listed for 88:11] وَكَمْ أَهْلَكْنَا قَبْلَهُم مِّن قَرْنٍ هَلْ تُحِسُّ مِنْهُم مِّنْ أَحَدٍ أَوْ تَسْمَعُ لَهُمْ رِكْزًۢا
- (26:25) [listed for 88:11] قَالَ لِمَنْ حَوْلَهُۥٓ أَلَا تَسْتَمِعُونَ
- (37:46) [listed for 88:11] بَيْضَآءَ لَذَّةٍۢ لِّلشَّٰرِبِينَ
- (50:35) [listed for 88:11] لَهُم مَّا يَشَآءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌۭ
- (50:41) [listed for 88:11] وَٱسْتَمِعْ يَوْمَ يُنَادِ ٱلْمُنَادِ مِن مَّكَانٍۢ قَرِيبٍۢ
- (75:16) [listed for 88:11] لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ
- (76:11) [listed for 88:11] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (77:31) [listed for 88:11] لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ

## neighbours: within two ayat of a passage the commentary cites (58)

- (2:223) [next to 2:225] نِسَآؤُكُمْ حَرْثٌۭ لَّكُمْ فَأْتُوا۟ حَرْثَكُمْ أَنَّىٰ شِئْتُمْ ۖ وَقَدِّمُوا۟ لِأَنفُسِكُمْ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّكُم مُّلَٰقُوهُ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (2:224) [next to 2:225] وَلَا تَجْعَلُوا۟ ٱللَّهَ عُرْضَةًۭ لِّأَيْمَٰنِكُمْ أَن تَبَرُّوا۟ وَتَتَّقُوا۟ وَتُصْلِحُوا۟ بَيْنَ ٱلنَّاسِ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- (2:226) [next to 2:225] لِّلَّذِينَ يُؤْلُونَ مِن نِّسَآئِهِمْ تَرَبُّصُ أَرْبَعَةِ أَشْهُرٍۢ ۖ فَإِن فَآءُو فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:227) [next to 2:225] وَإِنْ عَزَمُوا۟ ٱلطَّلَٰقَ فَإِنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌۭ
- (5:87) [next to 5:89] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحَرِّمُوا۟ طَيِّبَٰتِ مَآ أَحَلَّ ٱللَّهُ لَكُمْ وَلَا تَعْتَدُوٓا۟ ۚ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (5:88) [next to 5:89] وَكُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ حَلَٰلًۭا طَيِّبًۭا ۚ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِىٓ أَنتُم بِهِۦ مُؤْمِنُونَ
- (5:90) [next to 5:89] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
- (5:91) [next to 5:89] إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
- (19:60) [next to 19:62] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ شَيْـًۭٔا
- (19:61) [next to 19:62] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (19:63) [next to 19:62] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:64) [next to 19:62] وَمَا نَتَنَزَّلُ إِلَّا بِأَمْرِ رَبِّكَ ۖ لَهُۥ مَا بَيْنَ أَيْدِينَا وَمَا خَلْفَنَا وَمَا بَيْنَ ذَٰلِكَ ۚ وَمَا كَانَ رَبُّكَ نَسِيًّۭا
- (20:106) [next to 20:108] فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا
- (20:109) [next to 20:108] يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَرَضِىَ لَهُۥ قَوْلًۭا
- (20:110) [next to 20:108] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِهِۦ عِلْمًۭا
- (23:0) [next to 23:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (23:1) [next to 23:2] قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ
- (23:4) [next to 23:2] وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ
- (23:5) [next to 23:3] وَٱلَّذِينَ هُمْ لِفُرُوجِهِمْ حَٰفِظُونَ
- (25:61) [next to 25:63] تَبَارَكَ ٱلَّذِى جَعَلَ فِى ٱلسَّمَآءِ بُرُوجًۭا وَجَعَلَ فِيهَا سِرَٰجًۭا وَقَمَرًۭا مُّنِيرًۭا
- (25:62) [next to 25:63] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (25:64) [next to 25:63] وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدًۭا وَقِيَٰمًۭا
- (25:65) [next to 25:63] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا
- (25:70) [next to 25:72] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ عَمَلًۭا صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يُبَدِّلُ ٱللَّهُ سَيِّـَٔاتِهِمْ حَسَنَٰتٍۢ ۗ وَكَانَ ٱللَّهُ غَفُورًۭا رَّحِيمًۭا
- (25:71) [next to 25:72] وَمَن تَابَ وَعَمِلَ صَٰلِحًۭا فَإِنَّهُۥ يَتُوبُ إِلَى ٱللَّهِ مَتَابًۭا
- (25:73) [next to 25:72] وَٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانًۭا
- (25:74) [next to 25:72] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا هَبْ لَنَا مِنْ أَزْوَٰجِنَا وَذُرِّيَّٰتِنَا قُرَّةَ أَعْيُنٍۢ وَٱجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا
- (28:52) [next to 28:54] ٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ مِن قَبْلِهِۦ هُم بِهِۦ يُؤْمِنُونَ
- (28:53) [next to 28:54] وَإِذَا يُتْلَىٰ عَلَيْهِمْ قَالُوٓا۟ ءَامَنَّا بِهِۦٓ إِنَّهُ ٱلْحَقُّ مِن رَّبِّنَآ إِنَّا كُنَّا مِن قَبْلِهِۦ مُسْلِمِينَ
- (28:56) [next to 28:54] إِنَّكَ لَا تَهْدِى مَنْ أَحْبَبْتَ وَلَٰكِنَّ ٱللَّهَ يَهْدِى مَن يَشَآءُ ۚ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (28:57) [next to 28:55] وَقَالُوٓا۟ إِن نَّتَّبِعِ ٱلْهُدَىٰ مَعَكَ نُتَخَطَّفْ مِنْ أَرْضِنَآ ۚ أَوَلَمْ نُمَكِّن لَّهُمْ حَرَمًا ءَامِنًۭا يُجْبَىٰٓ إِلَيْهِ ثَمَرَٰتُ كُلِّ شَىْءٍۢ رِّزْقًۭا مِّن لَّدُنَّا وَلَٰكِنَّ أَكْثَرَهُمْ لَا يَعْلَمُونَ
- (41:24) [next to 41:26] فَإِن يَصْبِرُوا۟ فَٱلنَّارُ مَثْوًۭى لَّهُمْ ۖ وَإِن يَسْتَعْتِبُوا۟ فَمَا هُم مِّنَ ٱلْمُعْتَبِينَ
- (41:25) [next to 41:26] ۞ وَقَيَّضْنَا لَهُمْ قُرَنَآءَ فَزَيَّنُوا۟ لَهُم مَّا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَحَقَّ عَلَيْهِمُ ٱلْقَوْلُ فِىٓ أُمَمٍۢ قَدْ خَلَتْ مِن قَبْلِهِم مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ إِنَّهُمْ كَانُوا۟ خَٰسِرِينَ
- (41:28) [next to 41:26] ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (41:29) [next to 41:27] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ نَجْعَلْهُمَا تَحْتَ أَقْدَامِنَا لِيَكُونَا مِنَ ٱلْأَسْفَلِينَ
- (52:21) [next to 52:23] وَٱلَّذِينَ ءَامَنُوا۟ وَٱتَّبَعَتْهُمْ ذُرِّيَّتُهُم بِإِيمَٰنٍ أَلْحَقْنَا بِهِمْ ذُرِّيَّتَهُمْ وَمَآ أَلَتْنَٰهُم مِّنْ عَمَلِهِم مِّن شَىْءٍۢ ۚ كُلُّ ٱمْرِئٍۭ بِمَا كَسَبَ رَهِينٌۭ
- (52:22) [next to 52:23] وَأَمْدَدْنَٰهُم بِفَٰكِهَةٍۢ وَلَحْمٍۢ مِّمَّا يَشْتَهُونَ
- (52:24) [next to 52:23] ۞ وَيَطُوفُ عَلَيْهِمْ غِلْمَانٌۭ لَّهُمْ كَأَنَّهُمْ لُؤْلُؤٌۭ مَّكْنُونٌۭ
- (56:0) [next to 56:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (56:1) [next to 56:2] إِذَا وَقَعَتِ ٱلْوَاقِعَةُ
- (56:3) [next to 56:2] خَافِضَةٌۭ رَّافِعَةٌ
- (56:4) [next to 56:2] إِذَا رُجَّتِ ٱلْأَرْضُ رَجًّۭا
- (56:17) [next to 56:19] يَطُوفُ عَلَيْهِمْ وِلْدَٰنٌۭ مُّخَلَّدُونَ
- (56:18) [next to 56:19] بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ
- (56:20) [next to 56:19] وَفَٰكِهَةٍۢ مِّمَّا يَتَخَيَّرُونَ
- (56:21) [next to 56:19] وَلَحْمِ طَيْرٍۢ مِّمَّا يَشْتَهُونَ
- (56:23) [next to 56:25] كَأَمْثَٰلِ ٱللُّؤْلُؤِ ٱلْمَكْنُونِ
- (56:24) [next to 56:25] جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (56:27) [next to 56:25] وَأَصْحَٰبُ ٱلْيَمِينِ مَآ أَصْحَٰبُ ٱلْيَمِينِ
- (56:28) [next to 56:26] فِى سِدْرٍۢ مَّخْضُودٍۢ
- (69:6) [next to 69:8] وَأَمَّا عَادٌۭ فَأُهْلِكُوا۟ بِرِيحٍۢ صَرْصَرٍ عَاتِيَةٍۢ
- (69:7) [next to 69:8] سَخَّرَهَا عَلَيْهِمْ سَبْعَ لَيَالٍۢ وَثَمَٰنِيَةَ أَيَّامٍ حُسُومًۭا فَتَرَى ٱلْقَوْمَ فِيهَا صَرْعَىٰ كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍۢ
- (69:9) [next to 69:8] وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ
- (69:10) [next to 69:8] فَعَصَوْا۟ رَسُولَ رَبِّهِمْ فَأَخَذَهُمْ أَخْذَةًۭ رَّابِيَةً
- (78:32) [next to 78:34] حَدَآئِقَ وَأَعْنَٰبًۭا
- (78:33) [next to 78:34] وَكَوَاعِبَ أَتْرَابًۭا
- (78:36) [next to 78:34] جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا
- (78:37) [next to 78:35] رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا

