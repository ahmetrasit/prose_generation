Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:10; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_10/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_10.reading.tr.md (prose paragraphs numbered) =====
## Söylenen öğüdü almak

[¶1] Onuncu ayet, dokuzuncu ayetin cevapsız bıraktığı bir soruyu cevaplar. Peygamber'e {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:hatırlat, eğer hatırlatma fayda verirse, source:87:9} denmişti. Cümle bir şartla bitiyordu ve bu şartın kimde gerçekleşeceği söylenmemişti. Onuncu ayet bunu söyler: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içinde saygıyla karışık bir korku taşıyan hatırlayacaktır, source:87:10}. Ayet üç kelimeden oluşur: bir fiil, öznesini belirsiz bırakan bir "kim ki" ve o kişiyi tanımlayan ikinci bir fiil. Burada bir sınıftan, bir kavimden ya da bir isimden söz edilmez. Ölçü yalnızca kişinin içindeki bir hâldir.

[¶2] İlk fiil, dokuzuncu ayetteki emirle aynı kökten gelir. Fark, kalıbındadır. Emirdeki "ẕekkir" başkasına hatırlatmaktır. Onuncu ayetteki fiil ise aynı hatırlatmayı alan kişinin kendi üzerine aldığı ve kendi içinde yürüttüğü bir iştir. Fiilin aslı "yetezekkeru"dur. Baştaki "te" sesi yanındaki ẕâl sesine karışır ve kelime "yeẕẕekkeru" diye okunur. Hatırlatma, ağızdan çıkıp başkasına geçen bir iş olarak tanımlanır: {ar:الذكرى اسم للتذكير والتذكير مجاوز, tr:eẕ-ẕikrâ ismun li't-teẕkîri ve't-teẕkîru mucâviz, gloss:zikrâ hatırlatmanın adıdır; hatırlatma ise karşıya geçen bir iştir, source:"ذ ك ر,B009"}. Peygamber'in yapabileceği iş buraya kadardır, yani sözü karşıya geçirmektir. Hatırlamak ise dinleyenin işidir. Bu yüzden ayet "korkan kişiye öğüt işleyecek" demez, "korkan kişi hatırlayacak" der. Fiilin öznesi dinleyendir. Dokuzuncu ayetteki "eğer" sözünün kapısı da onun elindedir.

[¶3] Fiilin başındaki "se-" eki, sözü yakın ve kesin bir geleceğe yerleştirir. Aynı ek altıncı ayette Allah'ın kendi işi için kullanılmıştı: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız ve unutmayacaksın, source:87:6}. Orada okutan ve unutturmayan Allah'tır. Burada aynı gelecek eki bir insanın hatırlamasına konur. Sure böylece iki vaadi yan yana dizer. Biri sözü getiren elçinin hafızası, öbürü sözü alan dinleyenin hafızası hakkındadır. İlki tamamen Allah'ın işidir. İkincisi, dinleyenin içinde bir korku bulunmasına bağlıdır.

## Kaçanı geri aramak

[¶4] Hatırlamayı anlatan kelimeler, burada bir hafıza resmi çizer. Bu resimler kelimenin bu ayetteki anlamının yerine geçmez, onun yanında duyulur. Arap dilinde bu kök önce unutmanın karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi hatırladım demek, onu unuttum demenin karşıtıdır, source:"ذ ك ر,B003"}. Kök ayrıca bir şeyi elde tutmayı da anlatır: {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey'i ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; "o benim zikrimin üzerindedir" denir, yani aklımda tuttuğum bir yerde durur, source:"ذ ك ر,B003"}. Bu ayetin kalıbı ise bir adım öteye gider: {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür, elden kaçmış olanı aramaktır, source:"ذ ك ر,B003"}. Tezekkür, bir şeyin kendiliğinden akla düşmesi değildir. Geçip gitmiş bir şeyin peşine düşmektir. Aranan şey bir zamanlar elde olan şeydir, çünkü kişinin hiç sahip olmadığı bir şey "kaçmış" sayılmaz. Hatırlatma bu yüzden dinleyene yabancı bir şey getirmez. Elinden kayanı ona yeniden gösterir. Asıl arayışı ise dinleyenin kendisi yapar.

[¶5] Bu kelime, surenin altıncı ayetle başlayan zincirine katılır. O ayette okutulan sözün toplanıp tutulması ve unutulanın, göç edenlerin konak yerinde bıraktığı döküntü gibi geride kalması anlatılır. Onuncu ayetin fiili, o zincirde geride kalana geri dönüp onu arayan hareketin adıdır. Arada bir fark vardır. Peygamber'in hafızası Allah'ın "okutacağız" vaadiyle korunur, kaçan bir şeyi araması gerekmez. Dinleyenin hafızası ise kaçmış olanın peşine kendisi düşmek zorundadır.

[¶6] Kur'an bu arayışın nasıl sonuçlandığını başka bir yerde tek bir anla gösterir. Peygamber'e cahillerden yüz çevirmesi ve şeytandan bir kışkırtma gelirse Allah'a sığınması söylendikten hemen sonra şöyle denir: {ar:إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ, tr:inne'lleẕîne't-tekav iẕâ messehum tâifun mine'ş-şeytâni teẕekkerû fe-iẕâ hum mubsirûn, gloss:sakınanlara şeytandan dolaşan bir şey dokunduğunda hatırlarlar ve bir de bakarsın görmektedirler, source:7:201}. Fiil onuncu ayetteki fiilin aynısıdır ve sonucu görmektir. Kaçanı arayan, bulduğunda gözünü yeniden açar. Bu ayetteki "sakınanlar" ile onuncu ayetteki "korkan" aynı kökten değildir, ama aynı tutumda buluşurlar. İkisinde de hatırlamayı tetikleyen şey, kişinin önceden içinde taşıdığı bir dikkattir.

[¶7] Türkçeye geçen iki kelime bu anlamın bir kısmını yolda bırakmıştır. "Zikir" bugün çoğunlukla Allah'ın adlarını belli bir düzende tekrar etmek anlamına gelir. "Tezekkür" ise bir konuyu görüşüp konuşmak demektir. Ayetteki kelime ikisinden de genişse ve daha canlıdır. Kişinin, kaybettiği bir şeyi bulmak için kendi içine dönmesini anlatır.

## Bilerek korkmak

[¶8] Ayetin ikinci fiili korkuyu anlatır, ama sıradan bir korkuyu değil. Bu korkunun içine yücelik duygusu karışır ve çoğunlukla bilgiden doğar: {ar:الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم, tr:el-haşyetu havfun yeşûbuhû ta'zîmun ve ekŝeru mâ yekûnu ẕâlike an ilm, gloss:haşyet içine yüceltme karışmış bir korkudur ve çoğu zaman bilgiden gelir, source:"خ ش ي,B001"}. Kelimenin içinde ürkme de vardır ({source:"خ ش ي,B001"}). Bir yerin insana verdiği duyguyu anlatırken de kullanılır: {ar:هذا المكان أخشى من ذاك أي أفزعه, tr:hâẕe'l-mekânu ahşâ min ẕâke ey efzauh, gloss:bu yer ötekinden daha ürkütücüdür, source:"خ ش ي,B001"}. Yani bu korku, kişinin kendi kuruntusundan çıkmaz. Gerçekten orada olan ve insanı aşan bir şeyin karşısında duyulur. Araplar mecaz olarak "korktum" deyip "bildim" demeyi de kastederlerdi: {ar:المجاز قولهم خشيت بمعنى علمت, tr:el-mecâzu kavluhum haşîtu bi-ma'nâ alimtu, gloss:mecaz olarak "haşîtu" (korktum) sözünü "bildim" anlamında söylerlerdi, source:"خ ش ي,B002"}. Bu mecaz, iki fiil arasındaki bağın dilde de hissedildiğini gösterir. Bilmek, bu korkuya giden yoldur. Bazen de bu korku, bilmenin kendisi gibi yaşanır.

[¶9] Kur'an bu bağı açıkça söyler. Bir ayet, gökten inen suyla çıkan farklı renklerdeki meyveleri, dağlardaki ak, kırmızı ve kara yolları, insanların ve hayvanların farklı renklerini sayar. Sonra şöyle der: {ar:إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟, tr:innemâ yahşallâhe min ibâdihi'l-ulemâ, gloss:kulları arasında Allah'tan ancak bilenler haşyetle korkar, source:35:28}. Buradaki bilgi, yaratılışa bakarak kazanılan bilgidir. Bizim sure de aynı yerden başlar: yaratıp düzene koyan, ölçüp yol gösteren, otlağı çıkarıp sonra onu kararmış bir döküntüye çeviren Rabbin işleriyle açılır. Onuncu ayetteki korkunun kaynağı bu açılışta zaten gösterilmiştir. Yaratılışın bu işleyişini gören kişi, hatırlatma geldiğinde neyin söz konusu olduğunu bilir.

[¶10] Ayet korkunun nesnesini söylemez. "Kim korkarsa" der ve orada durur. Kur'an başka yerlerde bu nesneyi verir. Kendisine sözü geçmeyenlerin anlatıldığı bir yerde Peygamber'e şöyle denir: {ar:إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ, tr:innemâ tunẕiru meni'ttebea'ẕ-ẕikra ve haşiye'r-rahmâne bi'l-ğayb, gloss:sen ancak hatırlatmaya uyanı ve Rahman'dan görmeden korkanı uyarırsın, source:36:11}. Bu ayette onuncu ayetin iki kökü yan yana durur. Korkunun nesnesi Rahman'dır ve bu korku görmeden duyulur. Bizim ayetteki sessizlik ise korkuyu bir nesneye bağlamaktan çok, bir hâl olarak bırakır. İçinde ciddiyet duygusu olan herkes bu cümlenin öznesi olabilir. Yedinci ayet Allah'ın {ar:يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:ya'lemu'l-cehra ve mâ yahfâ, gloss:açığa çıkanı da gizli kalanı da bilir, source:87:7} olduğunu söylemişti. "Yahfâ" ile "yahşâ" ayrı köklerden gelir. Aralarındaki benzerlik yalnızca sestedir. Yine de kulak, iki ayet arasında bir eşleşme duyar. Allah gizli olanı bilir, korkan da görmediğinin karşısında korkar.

[¶11] Bu korkunun karşıtı cesaret değildir. Kur'an bunu bir sahnede gösterir. Peygamber'in yanına gözleri görmeyen bir adam gelir. Peygamber yüzünü ekşitir ve döner, çünkü o sırada başkasıyla ilgilenmektedir. Allah ona adam hakkında şöyle der: {ar:أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ, tr:ev yeẕẕekkeru fe-tenfeahu'ẕ-ẕikrâ, gloss:ya da hatırlar da hatırlatma ona fayda verir, source:80:4}. Bu cümlede bizim surenin dokuzuncu ve onuncu ayetlerindeki kelimelerin aynısı geçer. Sonra iki kişi karşılaştırılır. Biri {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'steğnâ, gloss:kendini yeterli gören kişi, source:80:5}, öbürü ise {ar:وَأَمَّا مَن جَآءَكَ يَسْعَىٰ, tr:ve emmâ men câeke yes'â, gloss:sana koşarak gelen, source:80:8} ve {ar:وَهُوَ يَخْشَىٰ, tr:ve huve yahşâ, gloss:içinde korku taşıyarak gelen, source:80:9}. Korkanın karşısında korkusuz biri durmaz, kendini yeterli gören biri durur. Bir şeyi kaybetmiş olabileceğini hiç düşünmeyen kişi, kaçanı aramaya da çıkmaz. Kendinden yana eksik bir şey görmeyen için hatırlatmanın geri getirebileceği bir şey yoktur.

## Korkudan hatırlamaya, hatırlamadan korkuya

[¶12] Onuncu ayette sıra bellidir: önce korku vardır, sonra hatırlama gelir. Korkuyu anlatan fiil süren bir hâli gösterir. Hatırlamayı anlatan fiil ise ileriye bakar. Kur'an başka bir yerde bu sırayı açık bırakır. Allah, Musa ile Harun'u azgınlaşmış Firavun'a gönderirken onlara şöyle der: {ar:فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ, tr:fe-kûlâ lehû kavlen leyyinen leallehû yeteẕekkeru ev yahşâ, gloss:ona yumuşak bir söz söyleyin; belki hatırlar ya da korkar, source:20:44}. Aynı iki fiil, aynı kişi hakkında, "ya da" ile bağlanmıştır. Bu ayete göre ikisi de birer kapıdır. Bazen önce hatırlamak gelir ve korkuyu uyandırır. Bazen önce korku gelir ve hatırlamaya yol açar. Bizim ayet bu kapılardan birini söyler: hatırlatma, içinde zaten bir korku taşıyan kişide tutunur.

[¶13] Aynı kelimeler, Peygamber'e yapılan bir başka hitabın başında da bir araya gelir. Allah ona şöyle der: {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana sıkıntıya düşesin diye indirmedik, source:20:2}, {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkiraten li-men yahşâ, gloss:ancak içinde korku taşıyan için bir hatırlatma olarak indirdik, source:20:3}. Bir şeyi hatırlatmaya yarayan araca "teẕkira" denir: {ar:التذكرة ما تستذكر به الحاجة, tr:et-teẕkiratu mâ tusteẕkeru bihi'l-hâce, gloss:teẕkira, bir ihtiyacın onunla hatırlandığı şeydir, source:"ذ ك ر,B009"}. Kur'an kendini böyle bir araç olarak tanıtır, yani unutulanı bulduran bir işaret olarak. Bu ayetteki "sıkıntıya düşmek" fiili, on birinci ayette hatırlatmadan uzak duran {ar:ٱلْأَشْقَى, tr:el-eşkâ, gloss:en bedbaht, source:87:11} kelimesiyle aynı köktendir. On birinci ayet, sunulan hatırlatmanın yanından geçip gideni gösterir. Böylece sure, hatırlatmayı alan ile yanından geçen arasındaki ayrımı kurar. Bu ayrımın sahnesi surenin bütününe aittir. Diğer ayette ise önemli olan şudur: Kur'an, kimin hatırlayacağının yükünü elçinin omzuna koymaz. Hatırlatma içinde korku taşıyana verilmiştir. Onu almamanın sıkıntısını elçi değil, almayan çeker. Dokuzuncu ayetteki "eğer fayda verirse" kaydı ile onuncu ayetin cevabı bu yükü yerine koyar.

## Hatırlamanın vakti

[¶14] Fiilin başındaki yakın gelecek eki, bu hatırlamanın ne zaman olduğunu da söyler: şimdi ile çok yakın bir sonra arasında. Kur'an aynı fiili çok daha geç bir an için de kullanır. Yeryüzü dümdüz edildiğinde, Rab geldiğinde ve melekler saf saf dizildiğinde, şöyle denir: {ar:وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ, tr:ve cîe yevmeiẕin bi-cehennem yevmeiẕin yeteẕekkeru'l-insânu ve ennâ lehu'ẕ-ẕikrâ, gloss:o gün cehennem getirilir; o gün insan hatırlar, ama o hatırlamanın ona ne yararı olur, source:89:23}. Ardından insan {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önceden bir şey gönderseydim der, source:89:24}. Burada hatırlamak yine vardır ve dokuzuncu ayetteki "ẕikrâ" kelimesi de oradadır. Eksik olan, onun faydasıdır. Kaçanı aramak, onu hâlâ yakalayabilecek kişiye yarar. Her şey görünür hâle geldikten sonra hatırlamak artık bir arayış değildir, yalnızca bir pişmanlıktır.

[¶15] Kur'an bu zamanı bir ömür olarak da ölçer. Ateşte ne ölmelerine hükmedilen ne de azapları hafifletilen inkârcılar, "Rabbimiz, bizi çıkar, yaptığımızdan başka iyi işler yapalım" diye bağırırlar. Onlara şu cevap verilir: {ar:أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ, tr:e-ve lem nuammirkum mâ yeteẕekkeru fîhi men teẕekkera ve câekumu'n-neẕîr, gloss:size, hatırlayacak olanın içinde hatırlayabileceği kadar bir ömür vermedik mi, size uyarıcı da gelmişti, source:35:37}. Ömür, hatırlamak için verilmiş bir süre olarak tanımlanır. Bu sahnede ateşin içinde ne ölüp ne kurtulan bu insanlar, bizim surenin on üçüncü ayetinde ateşe girip {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:87:13} denilen kişiyle aynı durumdadır. Başka bir yerde de büyük felaketin geldiği gün için {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yeteẕekkeru'l-insânu mâ seâ, gloss:insanın bütün çabasını hatırlayacağı gün, source:79:35} denir.

[¶16] Onuncu ayetteki korkunun değeri burada ortaya çıkar. Korkan kişi, cehennem getirilmeden önce, görmeden korkar. Onu hatırlamaya iten şey, henüz görmediği şeyin ciddiyetidir. Ötekiler ise ancak gördükten sonra hatırlar. İkisinde de fiil aynıdır, değişen yalnızca vakittir. "Se-" ekinin yakınlığı, bu hatırlamanın ömür sürerken olacağını söyler. Vakti geçmiş bir hatırlamadan farkı da budur.

## Hatırlamaktan anmaya

[¶17] Bu kök surede üç kez geçer ve her seferinde farklı bir kalıpla gelir. Dokuzuncu ayette elçiye yöneltilen emirdir: hatırlat. Onuncu ayette dinleyenin kendi işidir: hatırlayacak. On beşinci ayette ise başarıya ulaşan kişinin yaptığı iştir: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını andı ve namaz kıldı, source:87:15}. Kökün bir anlamı, bir şeyin dilden akmasıdır: {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikruceryu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinin üzerinden akmasıdır, source:"ذ ك ر,B004"}. Bir anlamı da Allah'a kulluk olarak yapılan anmadır: {ar:الذكر الصلاة والدعاء والثناء, tr:eẕ-ẕikru's-salâtu ve'd-duâu ve's-senâ, gloss:zikir namaz, dua ve övgüdür, source:"ذ ك ر,B005"}. Üç ayet bu anlamları bir yol gibi dizer. Söz önce elçinin ağzından karşıya geçer. Sonra dinleyenin içinde kaybettiğini arayan bir hareket olur. En sonunda yeniden dile çıkar, ama bu kez Rabbin adını anan bir söz olarak ve namazla birlikte. On beşinci ayetteki kişi, surenin birinci ayetindeki {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1} emrini yerine getirmiş olur. Onuncu ayet bu yolun ortasındaki adımdır. Hatırlatma içeride tutunmadıkça dile dönüp anmaya dönüşemez.

[¶18] Bu yolun bir de ses tarafı vardır. On dördüncü ayetteki {ar:تَزَكَّىٰ, tr:tezekkâ, gloss:arındı, source:87:14} fiili, onuncu ayetteki fiille aynı kalıptadır ve kulağa neredeyse aynı gelir. İki kelime farklı köklerden gelir. Biri arınmayı, öbürü hatırlamayı anlatır. Aralarındaki bağ, kök birliği değil ses yakınlığıdır. Kur'an bu iki fiili gözleri görmeyen adamın sahnesinde de yan yana koyar: {ar:وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ, tr:ve mâ yudrîke leallehû yezzekkâ, gloss:ne bilirsin, belki o arınacak, source:80:3}. Bunun hemen ardından "ya da hatırlayacak" denir. Orada iki fiil de bizim ayetteki gibi ses kaynaşmasıyla söylenir: yezzekkâ, yeẕẕekkeru. Bizim surede ise onuncu ve on dördüncü ayet arasına hatırlatmadan uzak duranın ateşi girer. Yan yana duyulan bu iki ses, içinde korku taşıyan kişinin önündeki iki adımı gösterir. O kişi önce kaçanı arar, sonra kendini arıtır. Bu ikisinin ardından da Rabbinin adını anar.

===== _commentary/v16/out/87_10/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: Form V tafa''ala as reflexive/receptive counterpart of Form II ḏakkara
- memory: yaḏḏakkaru = yatadhakkaru with ta' assimilated into ḏāl
- memory: sa- prefix marks near, certain future
- memory: Turkish "zikir" narrowed to ritual repetition; "tezekkür" now means deliberation/discussion
- not written: ذ ك ر B001 male, male offspring - no bearing on remembering here
- not written: ذ ك ر B002 hard steel, sharp sword, strong man - would replace, not accompany, the sense
- not written: ذ ك ر B006 scripture named dhikr - belongs to 87:18-19 pages chain, surah commentary
- not written: ذ ك ر B007 honour, renown - no grounding in this ayah's situation
- not written: ذ ك ر B008 deed of right (dhikr haqq) - no link to theme
- not written: خ ش ي B003 khashya as dislike, said of God - concerns another passage, irrelevant to the human fearer
- not written: خ ش ي B004 shrivelled dates, dry meat - marked as outside the root's core; tying it to 87:5's chaff would be speculative
- not written: 87:11 avoidance and janb imagery, 79:19 Pharaoh scene - belong to the surah commentary's shared scene; only recalled

===== passages not cited (198) =====
## strong (this ayah's own list) (26)

- (6:51) [listed for 87:10] وَأَنذِرْ بِهِ ٱلَّذِينَ يَخَافُونَ أَن يُحْشَرُوٓا۟ إِلَىٰ رَبِّهِمْ ۙ لَيْسَ لَهُم مِّن دُونِهِۦ وَلِىٌّۭ وَلَا شَفِيعٌۭ لَّعَلَّهُمْ يَتَّقُونَ
- (7:63) [listed for 87:10] أَوَعَجِبْتُمْ أَن جَآءَكُمْ ذِكْرٌۭ مِّن رَّبِّكُمْ عَلَىٰ رَجُلٍۢ مِّنكُمْ لِيُنذِرَكُمْ وَلِتَتَّقُوا۟ وَلَعَلَّكُمْ تُرْحَمُونَ
- (20:3) [listed for 87:10] [cited in ¶13] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
- (20:14) [listed for 87:10] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:34) [listed for 87:10] وَنَذْكُرَكَ كَثِيرًا
- (20:44) [listed for 87:10] [cited in ¶12] فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ
- (20:113) [listed for 87:10] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
- (20:124) [listed for 87:10] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
- (26:5) [listed for 87:10] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
- (29:45) [listed for 87:10] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
- (32:15) [listed for 87:10] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (35:18) [listed for 87:10] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (35:28) [listed for 87:10] [cited in ¶9] وَمِنَ ٱلنَّاسِ وَٱلدَّوَآبِّ وَٱلْأَنْعَٰمِ مُخْتَلِفٌ أَلْوَٰنُهُۥ كَذَٰلِكَ ۗ إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟ ۗ إِنَّ ٱللَّهَ عَزِيزٌ غَفُورٌ
- (36:11) [listed for 87:10] [cited in ¶10] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
- (39:23) [listed for 87:10] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (50:37) [listed for 87:10] إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِمَن كَانَ لَهُۥ قَلْبٌ أَوْ أَلْقَى ٱلسَّمْعَ وَهُوَ شَهِيدٌۭ
- (50:45) [listed for 87:10] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
- (54:40) [listed for 87:10] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (79:19) [listed for 87:10] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- (79:26) [listed for 87:10] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (79:45) [listed for 87:10] إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
- (80:3) [listed for 87:10] [cited in ¶18] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
- (80:4) [listed for 87:10] [cited in ¶11] أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ
- (80:9) [listed for 87:10] [cited in ¶11] وَهُوَ يَخْشَىٰ
- (80:10) [listed for 87:10] فَأَنتَ عَنْهُ تَلَهَّىٰ
- (80:11) [listed for 87:10] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ

## medium (this ayah's own list) (68)

- (2:150) [listed for 87:10] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
- (2:269) [listed for 87:10] يُؤْتِى ٱلْحِكْمَةَ مَن يَشَآءُ ۚ وَمَن يُؤْتَ ٱلْحِكْمَةَ فَقَدْ أُوتِىَ خَيْرًۭا كَثِيرًۭا ۗ وَمَا يَذَّكَّرُ إِلَّآ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (7:171) [listed for 87:10] ۞ وَإِذْ نَتَقْنَا ٱلْجَبَلَ فَوْقَهُمْ كَأَنَّهُۥ ظُلَّةٌۭ وَظَنُّوٓا۟ أَنَّهُۥ وَاقِعٌۢ بِهِمْ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (7:205) [listed for 87:10] وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ بِٱلْغُدُوِّ وَٱلْءَاصَالِ وَلَا تَكُن مِّنَ ٱلْغَٰفِلِينَ
- (9:13) [listed for 87:10] أَلَا تُقَٰتِلُونَ قَوْمًۭا نَّكَثُوٓا۟ أَيْمَٰنَهُمْ وَهَمُّوا۟ بِإِخْرَاجِ ٱلرَّسُولِ وَهُم بَدَءُوكُمْ أَوَّلَ مَرَّةٍ ۚ أَتَخْشَوْنَهُمْ ۚ فَٱللَّهُ أَحَقُّ أَن تَخْشَوْهُ إِن كُنتُم مُّؤْمِنِينَ
- (9:18) [listed for 87:10] إِنَّمَا يَعْمُرُ مَسَٰجِدَ ٱللَّهِ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَلَمْ يَخْشَ إِلَّا ٱللَّهَ ۖ فَعَسَىٰٓ أُو۟لَٰٓئِكَ أَن يَكُونُوا۟ مِنَ ٱلْمُهْتَدِينَ
- (13:19) [listed for 87:10] ۞ أَفَمَن يَعْلَمُ أَنَّمَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ كَمَنْ هُوَ أَعْمَىٰٓ ۚ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (13:21) [listed for 87:10] وَٱلَّذِينَ يَصِلُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيَخْشَوْنَ رَبَّهُمْ وَيَخَافُونَ سُوٓءَ ٱلْحِسَابِ
- (13:28) [listed for 87:10] ٱلَّذِينَ ءَامَنُوا۟ وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ ٱللَّهِ ۗ أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ
- (16:17) [listed for 87:10] أَفَمَن يَخْلُقُ كَمَن لَّا يَخْلُقُ ۗ أَفَلَا تَذَكَّرُونَ
- (18:24) [listed for 87:10] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (18:28) [listed for 87:10] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (18:57) [listed for 87:10] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ فَأَعْرَضَ عَنْهَا وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ ۚ إِنَّا جَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۖ وَإِن تَدْعُهُمْ إِلَى ٱلْهُدَىٰ فَلَن يَهْتَدُوٓا۟ إِذًا أَبَدًۭا
- (19:58) [listed for 87:10] أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ مِن ذُرِّيَّةِ ءَادَمَ وَمِمَّنْ حَمَلْنَا مَعَ نُوحٍۢ وَمِن ذُرِّيَّةِ إِبْرَٰهِيمَ وَإِسْرَٰٓءِيلَ وَمِمَّنْ هَدَيْنَا وَٱجْتَبَيْنَآ ۚ إِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُ ٱلرَّحْمَٰنِ خَرُّوا۟ سُجَّدًۭا وَبُكِيًّۭا ۩
- (20:77) [listed for 87:10] وَلَقَدْ أَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ أَنْ أَسْرِ بِعِبَادِى فَٱضْرِبْ لَهُمْ طَرِيقًۭا فِى ٱلْبَحْرِ يَبَسًۭا لَّا تَخَٰفُ دَرَكًۭا وَلَا تَخْشَىٰ
- (20:99) [listed for 87:10] كَذَٰلِكَ نَقُصُّ عَلَيْكَ مِنْ أَنۢبَآءِ مَا قَدْ سَبَقَ ۚ وَقَدْ ءَاتَيْنَٰكَ مِن لَّدُنَّا ذِكْرًۭا
- (21:28) [listed for 87:10] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يَشْفَعُونَ إِلَّا لِمَنِ ٱرْتَضَىٰ وَهُم مِّنْ خَشْيَتِهِۦ مُشْفِقُونَ
- (21:48) [listed for 87:10] وَلَقَدْ ءَاتَيْنَا مُوسَىٰ وَهَٰرُونَ ٱلْفُرْقَانَ وَضِيَآءًۭ وَذِكْرًۭا لِّلْمُتَّقِينَ
- (21:49) [listed for 87:10] ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَهُم مِّنَ ٱلسَّاعَةِ مُشْفِقُونَ
- (21:50) [listed for 87:10] وَهَٰذَا ذِكْرٌۭ مُّبَارَكٌ أَنزَلْنَٰهُ ۚ أَفَأَنتُمْ لَهُۥ مُنكِرُونَ
- (22:34) [listed for 87:10] وَلِكُلِّ أُمَّةٍۢ جَعَلْنَا مَنسَكًۭا لِّيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۗ فَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَلَهُۥٓ أَسْلِمُوا۟ ۗ وَبَشِّرِ ٱلْمُخْبِتِينَ
- (22:35) [listed for 87:10] ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَٱلصَّٰبِرِينَ عَلَىٰ مَآ أَصَابَهُمْ وَٱلْمُقِيمِى ٱلصَّلَوٰةِ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (22:40) [listed for 87:10] ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِم بِغَيْرِ حَقٍّ إِلَّآ أَن يَقُولُوا۟ رَبُّنَا ٱللَّهُ ۗ وَلَوْلَا دَفْعُ ٱللَّهِ ٱلنَّاسَ بَعْضَهُم بِبَعْضٍۢ لَّهُدِّمَتْ صَوَٰمِعُ وَبِيَعٌۭ وَصَلَوَٰتٌۭ وَمَسَٰجِدُ يُذْكَرُ فِيهَا ٱسْمُ ٱللَّهِ كَثِيرًۭا ۗ وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ
- (23:57) [listed for 87:10] إِنَّ ٱلَّذِينَ هُم مِّنْ خَشْيَةِ رَبِّهِم مُّشْفِقُونَ
- (24:1) [listed for 87:10] سُورَةٌ أَنزَلْنَٰهَا وَفَرَضْنَٰهَا وَأَنزَلْنَا فِيهَآ ءَايَٰتٍۭ بَيِّنَٰتٍۢ لَّعَلَّكُمْ تَذَكَّرُونَ
- (24:52) [listed for 87:10] وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ وَيَخْشَ ٱللَّهَ وَيَتَّقْهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْفَآئِزُونَ
- (25:18) [listed for 87:10] قَالُوا۟ سُبْحَٰنَكَ مَا كَانَ يَنۢبَغِى لَنَآ أَن نَّتَّخِذَ مِن دُونِكَ مِنْ أَوْلِيَآءَ وَلَٰكِن مَّتَّعْتَهُمْ وَءَابَآءَهُمْ حَتَّىٰ نَسُوا۟ ٱلذِّكْرَ وَكَانُوا۟ قَوْمًۢا بُورًۭا
- (25:73) [listed for 87:10] وَٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانًۭا
- (29:51) [listed for 87:10] أَوَلَمْ يَكْفِهِمْ أَنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ يُتْلَىٰ عَلَيْهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَرَحْمَةًۭ وَذِكْرَىٰ لِقَوْمٍۢ يُؤْمِنُونَ
- (33:39) [listed for 87:10] ٱلَّذِينَ يُبَلِّغُونَ رِسَٰلَٰتِ ٱللَّهِ وَيَخْشَوْنَهُۥ وَلَا يَخْشَوْنَ أَحَدًا إِلَّا ٱللَّهَ ۗ وَكَفَىٰ بِٱللَّهِ حَسِيبًۭا
- (36:69) [listed for 87:10] وَمَا عَلَّمْنَٰهُ ٱلشِّعْرَ وَمَا يَنۢبَغِى لَهُۥٓ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ وَقُرْءَانٌۭ مُّبِينٌۭ
- (36:70) [listed for 87:10] لِّيُنذِرَ مَن كَانَ حَيًّۭا وَيَحِقَّ ٱلْقَوْلُ عَلَى ٱلْكَٰفِرِينَ
- (37:13) [listed for 87:10] وَإِذَا ذُكِّرُوا۟ لَا يَذْكُرُونَ
- (38:1) [listed for 87:10] صٓ ۚ وَٱلْقُرْءَانِ ذِى ٱلذِّكْرِ
- (38:87) [listed for 87:10] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (39:21) [listed for 87:10] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (39:22) [listed for 87:10] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (43:13) [listed for 87:10] لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
- (50:33) [listed for 87:10] مَّنْ خَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ وَجَآءَ بِقَلْبٍۢ مُّنِيبٍ
- (51:37) [listed for 87:10] وَتَرَكْنَا فِيهَآ ءَايَةًۭ لِّلَّذِينَ يَخَافُونَ ٱلْعَذَابَ ٱلْأَلِيمَ
- (51:55) [listed for 87:10] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
- (52:25) [listed for 87:10] وَأَقْبَلَ بَعْضُهُمْ عَلَىٰ بَعْضٍۢ يَتَسَآءَلُونَ
- (54:17) [listed for 87:10] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:22) [listed for 87:10] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (54:32) [listed for 87:10] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (56:73) [listed for 87:10] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
- (57:16) [listed for 87:10] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (58:19) [listed for 87:10] ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ ۚ أَلَآ إِنَّ حِزْبَ ٱلشَّيْطَٰنِ هُمُ ٱلْخَٰسِرُونَ
- (59:19) [listed for 87:10] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (59:21) [listed for 87:10] لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
- (62:9) [listed for 87:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (63:9) [listed for 87:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (65:10) [listed for 87:10] أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا ۖ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟ ۚ قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا
- (67:12) [listed for 87:10] إِنَّ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌۭ
- (69:42) [listed for 87:10] وَلَا بِقَوْلِ كَاهِنٍۢ ۚ قَلِيلًۭا مَّا تَذَكَّرُونَ
- (69:48) [listed for 87:10] وَإِنَّهُۥ لَتَذْكِرَةٌۭ لِّلْمُتَّقِينَ
- (72:17) [listed for 87:10] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
- (73:19) [listed for 87:10] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (74:31) [listed for 87:10] وَمَا جَعَلْنَآ أَصْحَٰبَ ٱلنَّارِ إِلَّا مَلَٰٓئِكَةًۭ ۙ وَمَا جَعَلْنَا عِدَّتَهُمْ إِلَّا فِتْنَةًۭ لِّلَّذِينَ كَفَرُوا۟ لِيَسْتَيْقِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَيَزْدَادَ ٱلَّذِينَ ءَامَنُوٓا۟ إِيمَٰنًۭا ۙ وَلَا يَرْتَابَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ وَٱلْمُؤْمِنُونَ ۙ وَلِيَقُولَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ وَٱلْكَٰفِرُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۚ كَذَٰلِكَ يُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَمَا يَعْلَمُ جُنُودَ رَبِّكَ إِلَّا هُوَ ۚ وَمَا هِىَ إِلَّا ذِكْرَىٰ لِلْبَشَرِ
- (74:49) [listed for 87:10] فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ
- (74:54) [listed for 87:10] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
- (74:55) [listed for 87:10] فَمَن شَآءَ ذَكَرَهُۥ
- (74:56) [listed for 87:10] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
- (79:43) [listed for 87:10] فِيمَ أَنتَ مِن ذِكْرَىٰهَآ
- (80:12) [listed for 87:10] فَمَن شَآءَ ذَكَرَهُۥ
- (81:27) [listed for 87:10] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (88:21) [listed for 87:10] فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- (98:8) [listed for 87:10] جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

## named by the passage's own list as strong for this ayah (12)

- (8:21) [listed for 87:10] وَلَا تَكُونُوا۟ كَٱلَّذِينَ قَالُوا۟ سَمِعْنَا وَهُمْ لَا يَسْمَعُونَ
- (13:7) [listed for 87:10] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَةٌۭ مِّن رَّبِّهِۦٓ ۗ إِنَّمَآ أَنتَ مُنذِرٌۭ ۖ وَلِكُلِّ قَوْمٍ هَادٍ
- (17:41) [listed for 87:10] وَلَقَدْ صَرَّفْنَا فِى هَٰذَا ٱلْقُرْءَانِ لِيَذَّكَّرُوا۟ وَمَا يَزِيدُهُمْ إِلَّا نُفُورًۭا
- (17:82) [listed for 87:10] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
- (27:81) [listed for 87:10] وَمَآ أَنتَ بِهَٰدِى ٱلْعُمْىِ عَن ضَلَٰلَتِهِمْ ۖ إِن تُسْمِعُ إِلَّا مَن يُؤْمِنُ بِـَٔايَٰتِنَا فَهُم مُّسْلِمُونَ
- (37:3) [listed for 87:10] فَٱلتَّٰلِيَٰتِ ذِكْرًا
- (38:32) [listed for 87:10] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
- (40:44) [listed for 87:10] فَسَتَذْكُرُونَ مَآ أَقُولُ لَكُمْ ۚ وَأُفَوِّضُ أَمْرِىٓ إِلَى ٱللَّهِ ۚ إِنَّ ٱللَّهَ بَصِيرٌۢ بِٱلْعِبَادِ
- (71:6) [listed for 87:10] فَلَمْ يَزِدْهُمْ دُعَآءِىٓ إِلَّا فِرَارًۭا
- (80:6) [listed for 87:10] فَأَنتَ لَهُۥ تَصَدَّىٰ
- (80:7) [listed for 87:10] وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ
- (92:14) [listed for 87:10] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ

## named by the passage's own list as medium for this ayah (24)

- (2:40) [listed for 87:10] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَوْفُوا۟ بِعَهْدِىٓ أُوفِ بِعَهْدِكُمْ وَإِيَّٰىَ فَٱرْهَبُونِ
- (2:63) [listed for 87:10] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (2:122) [listed for 87:10] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (3:173) [listed for 87:10] ٱلَّذِينَ قَالَ لَهُمُ ٱلنَّاسُ إِنَّ ٱلنَّاسَ قَدْ جَمَعُوا۟ لَكُمْ فَٱخْشَوْهُمْ فَزَادَهُمْ إِيمَٰنًۭا وَقَالُوا۟ حَسْبُنَا ٱللَّهُ وَنِعْمَ ٱلْوَكِيلُ
- (7:201) [listed for 87:10] [cited in ¶6] إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ
- (12:104) [listed for 87:10] وَمَا تَسْـَٔلُهُمْ عَلَيْهِ مِنْ أَجْرٍ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (16:50) [listed for 87:10] يَخَافُونَ رَبَّهُم مِّن فَوْقِهِمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ ۩
- (17:9) [listed for 87:10] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
- (17:31) [listed for 87:10] وَلَا تَقْتُلُوٓا۟ أَوْلَٰدَكُمْ خَشْيَةَ إِمْلَٰقٍۢ ۖ نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ ۚ إِنَّ قَتْلَهُمْ كَانَ خِطْـًۭٔا كَبِيرًۭا
- (18:80) [listed for 87:10] وَأَمَّا ٱلْغُلَٰمُ فَكَانَ أَبَوَاهُ مُؤْمِنَيْنِ فَخَشِينَآ أَن يُرْهِقَهُمَا طُغْيَٰنًۭا وَكُفْرًۭا
- (20:42) [listed for 87:10] ٱذْهَبْ أَنتَ وَأَخُوكَ بِـَٔايَٰتِى وَلَا تَنِيَا فِى ذِكْرِى
- (20:100) [listed for 87:10] مَّنْ أَعْرَضَ عَنْهُ فَإِنَّهُۥ يَحْمِلُ يَوْمَ ٱلْقِيَٰمَةِ وِزْرًا
- (23:85) [listed for 87:10] سَيَقُولُونَ لِلَّهِ ۚ قُلْ أَفَلَا تَذَكَّرُونَ
- (23:110) [listed for 87:10] فَٱتَّخَذْتُمُوهُمْ سِخْرِيًّا حَتَّىٰٓ أَنسَوْكُمْ ذِكْرِى وَكُنتُم مِّنْهُمْ تَضْحَكُونَ
- (26:209) [listed for 87:10] ذِكْرَىٰ وَمَا كُنَّا ظَٰلِمِينَ
- (37:155) [listed for 87:10] أَفَلَا تَذَكَّرُونَ
- (38:46) [listed for 87:10] إِنَّآ أَخْلَصْنَٰهُم بِخَالِصَةٍۢ ذِكْرَى ٱلدَّارِ
- (43:5) [listed for 87:10] أَفَنَضْرِبُ عَنكُمُ ٱلذِّكْرَ صَفْحًا أَن كُنتُمْ قَوْمًۭا مُّسْرِفِينَ
- (50:8) [listed for 87:10] تَبْصِرَةًۭ وَذِكْرَىٰ لِكُلِّ عَبْدٍۢ مُّنِيبٍۢ
- (68:52) [listed for 87:10] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (74:1) [listed for 87:10] يَٰٓأَيُّهَا ٱلْمُدَّثِّرُ
- (82:14) [listed for 87:10] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (92:7) [listed for 87:10] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (92:10) [listed for 87:10] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ

## weak (this ayah's own list) (16)

- (2:47) [listed for 87:10] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
- (2:74) [listed for 87:10] ثُمَّ قَسَتْ قُلُوبُكُم مِّنۢ بَعْدِ ذَٰلِكَ فَهِىَ كَٱلْحِجَارَةِ أَوْ أَشَدُّ قَسْوَةًۭ ۚ وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ ۚ وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
- (2:152) [listed for 87:10] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
- (2:282) [listed for 87:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (4:9) [listed for 87:10] وَلْيَخْشَ ٱلَّذِينَ لَوْ تَرَكُوا۟ مِنْ خَلْفِهِمْ ذُرِّيَّةًۭ ضِعَٰفًا خَافُوا۟ عَلَيْهِمْ فَلْيَتَّقُوا۟ ٱللَّهَ وَلْيَقُولُوا۟ قَوْلًۭا سَدِيدًا
- (4:77) [listed for 87:10] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
- (5:52) [listed for 87:10] فَتَرَى ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ يُسَٰرِعُونَ فِيهِمْ يَقُولُونَ نَخْشَىٰٓ أَن تُصِيبَنَا دَآئِرَةٌۭ ۚ فَعَسَى ٱللَّهُ أَن يَأْتِىَ بِٱلْفَتْحِ أَوْ أَمْرٍۢ مِّنْ عِندِهِۦ فَيُصْبِحُوا۟ عَلَىٰ مَآ أَسَرُّوا۟ فِىٓ أَنفُسِهِمْ نَٰدِمِينَ
- (7:3) [listed for 87:10] ٱتَّبِعُوا۟ مَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُمْ وَلَا تَتَّبِعُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ ۗ قَلِيلًۭا مَّا تَذَكَّرُونَ
- (7:130) [listed for 87:10] وَلَقَدْ أَخَذْنَآ ءَالَ فِرْعَوْنَ بِٱلسِّنِينَ وَنَقْصٍۢ مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَذَّكَّرُونَ
- (17:100) [listed for 87:10] قُل لَّوْ أَنتُمْ تَمْلِكُونَ خَزَآئِنَ رَحْمَةِ رَبِّىٓ إِذًۭا لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ ۚ وَكَانَ ٱلْإِنسَٰنُ قَتُورًۭا
- (20:94) [listed for 87:10] قَالَ يَبْنَؤُمَّ لَا تَأْخُذْ بِلِحْيَتِى وَلَا بِرَأْسِىٓ ۖ إِنِّى خَشِيتُ أَن تَقُولَ فَرَّقْتَ بَيْنَ بَنِىٓ إِسْرَٰٓءِيلَ وَلَمْ تَرْقُبْ قَوْلِى
- (33:21) [listed for 87:10] لَّقَدْ كَانَ لَكُمْ فِى رَسُولِ ٱللَّهِ أُسْوَةٌ حَسَنَةٌۭ لِّمَن كَانَ يَرْجُوا۟ ٱللَّهَ وَٱلْيَوْمَ ٱلْءَاخِرَ وَذَكَرَ ٱللَّهَ كَثِيرًۭا
- (33:41) [listed for 87:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (38:48) [listed for 87:10] وَٱذْكُرْ إِسْمَٰعِيلَ وَٱلْيَسَعَ وَذَا ٱلْكِفْلِ ۖ وَكُلٌّۭ مِّنَ ٱلْأَخْيَارِ
- (46:21) [listed for 87:10] ۞ وَٱذْكُرْ أَخَا عَادٍ إِذْ أَنذَرَ قَوْمَهُۥ بِٱلْأَحْقَافِ وَقَدْ خَلَتِ ٱلنُّذُرُ مِنۢ بَيْنِ يَدَيْهِ وَمِنْ خَلْفِهِۦٓ أَلَّا تَعْبُدُوٓا۟ إِلَّا ٱللَّهَ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (94:4) [listed for 87:10] وَرَفَعْنَا لَكَ ذِكْرَكَ

## named by the passage's own list as weak for this ayah (19)

- (2:201) [listed for 87:10] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
- (2:221) [listed for 87:10] وَلَا تَنكِحُوا۟ ٱلْمُشْرِكَٰتِ حَتَّىٰ يُؤْمِنَّ ۚ وَلَأَمَةٌۭ مُّؤْمِنَةٌ خَيْرٌۭ مِّن مُّشْرِكَةٍۢ وَلَوْ أَعْجَبَتْكُمْ ۗ وَلَا تُنكِحُوا۟ ٱلْمُشْرِكِينَ حَتَّىٰ يُؤْمِنُوا۟ ۚ وَلَعَبْدٌۭ مُّؤْمِنٌ خَيْرٌۭ مِّن مُّشْرِكٍۢ وَلَوْ أَعْجَبَكُمْ ۗ أُو۟لَٰٓئِكَ يَدْعُونَ إِلَى ٱلنَّارِ ۖ وَٱللَّهُ يَدْعُوٓا۟ إِلَى ٱلْجَنَّةِ وَٱلْمَغْفِرَةِ بِإِذْنِهِۦ ۖ وَيُبَيِّنُ ءَايَٰتِهِۦ لِلنَّاسِ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (2:239) [listed for 87:10] فَإِنْ خِفْتُمْ فَرِجَالًا أَوْ رُكْبَانًۭا ۖ فَإِذَآ أَمِنتُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَمَا عَلَّمَكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (3:58) [listed for 87:10] ذَٰلِكَ نَتْلُوهُ عَلَيْكَ مِنَ ٱلْءَايَٰتِ وَٱلذِّكْرِ ٱلْحَكِيمِ
- (20:86) [listed for 87:10] فَرَجَعَ مُوسَىٰٓ إِلَىٰ قَوْمِهِۦ غَضْبَٰنَ أَسِفًۭا ۚ قَالَ يَٰقَوْمِ أَلَمْ يَعِدْكُمْ رَبُّكُمْ وَعْدًا حَسَنًا ۚ أَفَطَالَ عَلَيْكُمُ ٱلْعَهْدُ أَمْ أَرَدتُّمْ أَن يَحِلَّ عَلَيْكُمْ غَضَبٌۭ مِّن رَّبِّكُمْ فَأَخْلَفْتُم مَّوْعِدِى
- (21:2) [listed for 87:10] مَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّن رَّبِّهِم مُّحْدَثٍ إِلَّا ٱسْتَمَعُوهُ وَهُمْ يَلْعَبُونَ
- (21:6) [listed for 87:10] مَآ ءَامَنَتْ قَبْلَهُم مِّن قَرْيَةٍ أَهْلَكْنَٰهَآ ۖ أَفَهُمْ يُؤْمِنُونَ
- (21:105) [listed for 87:10] وَلَقَدْ كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ أَنَّ ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ
- (23:97) [listed for 87:10] وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَٰتِ ٱلشَّيَٰطِينِ
- (25:62) [listed for 87:10] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (28:47) [listed for 87:10] وَلَوْلَآ أَن تُصِيبَهُم مُّصِيبَةٌۢ بِمَا قَدَّمَتْ أَيْدِيهِمْ فَيَقُولُوا۟ رَبَّنَا لَوْلَآ أَرْسَلْتَ إِلَيْنَا رَسُولًۭا فَنَتَّبِعَ ءَايَٰتِكَ وَنَكُونَ مِنَ ٱلْمُؤْمِنِينَ
- (33:9) [listed for 87:10] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ إِذْ جَآءَتْكُمْ جُنُودٌۭ فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا ۚ وَكَانَ ٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرًا
- (37:108) [listed for 87:10] وَتَرَكْنَا عَلَيْهِ فِى ٱلْءَاخِرِينَ
- (38:29) [listed for 87:10] كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ مُبَٰرَكٌۭ لِّيَدَّبَّرُوٓا۟ ءَايَٰتِهِۦ وَلِيَتَذَكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (41:2) [listed for 87:10] تَنزِيلٌۭ مِّنَ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (51:49) [listed for 87:10] وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ
- (54:51) [listed for 87:10] وَلَقَدْ أَهْلَكْنَآ أَشْيَاعَكُمْ فَهَلْ مِن مُّدَّكِرٍۢ
- (92:5) [listed for 87:10] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- (114:4) [listed for 87:10] مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ

## neighbours: within two ayat of a passage the commentary cites (33)

- (7:199) [next to 7:201] خُذِ ٱلْعَفْوَ وَأْمُرْ بِٱلْعُرْفِ وَأَعْرِضْ عَنِ ٱلْجَٰهِلِينَ
- (7:200) [next to 7:201] وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ ۚ إِنَّهُۥ سَمِيعٌ عَلِيمٌ
- (7:202) [next to 7:201] وَإِخْوَٰنُهُمْ يَمُدُّونَهُمْ فِى ٱلْغَىِّ ثُمَّ لَا يُقْصِرُونَ
- (7:203) [next to 7:201] وَإِذَا لَمْ تَأْتِهِم بِـَٔايَةٍۢ قَالُوا۟ لَوْلَا ٱجْتَبَيْتَهَا ۚ قُلْ إِنَّمَآ أَتَّبِعُ مَا يُوحَىٰٓ إِلَىَّ مِن رَّبِّى ۚ هَٰذَا بَصَآئِرُ مِن رَّبِّكُمْ وَهُدًۭى وَرَحْمَةٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (20:0) [next to 20:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (20:1) [next to 20:2] طه
- (20:4) [next to 20:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:43) [next to 20:44] ٱذْهَبَآ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (20:45) [next to 20:44] قَالَا رَبَّنَآ إِنَّنَا نَخَافُ أَن يَفْرُطَ عَلَيْنَآ أَوْ أَن يَطْغَىٰ
- (20:46) [next to 20:44] قَالَ لَا تَخَافَآ ۖ إِنَّنِى مَعَكُمَآ أَسْمَعُ وَأَرَىٰ
- (35:26) [next to 35:28] ثُمَّ أَخَذْتُ ٱلَّذِينَ كَفَرُوا۟ ۖ فَكَيْفَ كَانَ نَكِيرِ
- (35:27) [next to 35:28] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍۢ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌۭ وَحُمْرٌۭ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌۭ
- (35:29) [next to 35:28] إِنَّ ٱلَّذِينَ يَتْلُونَ كِتَٰبَ ٱللَّهِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ يَرْجُونَ تِجَٰرَةًۭ لَّن تَبُورَ
- (35:30) [next to 35:28] لِيُوَفِّيَهُمْ أُجُورَهُمْ وَيَزِيدَهُم مِّن فَضْلِهِۦٓ ۚ إِنَّهُۥ غَفُورٌۭ شَكُورٌۭ
- (35:35) [next to 35:37] ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ
- (35:36) [next to 35:37] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (35:38) [next to 35:37] إِنَّ ٱللَّهَ عَٰلِمُ غَيْبِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (35:39) [next to 35:37] هُوَ ٱلَّذِى جَعَلَكُمْ خَلَٰٓئِفَ فِى ٱلْأَرْضِ ۚ فَمَن كَفَرَ فَعَلَيْهِ كُفْرُهُۥ ۖ وَلَا يَزِيدُ ٱلْكَٰفِرِينَ كُفْرُهُمْ عِندَ رَبِّهِمْ إِلَّا مَقْتًۭا ۖ وَلَا يَزِيدُ ٱلْكَٰفِرِينَ كُفْرُهُمْ إِلَّا خَسَارًۭا
- (36:9) [next to 36:11] وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّۭا وَمِنْ خَلْفِهِمْ سَدًّۭا فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ
- (36:10) [next to 36:11] وَسَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
- (36:12) [next to 36:11] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
- (36:13) [next to 36:11] وَٱضْرِبْ لَهُم مَّثَلًا أَصْحَٰبَ ٱلْقَرْيَةِ إِذْ جَآءَهَا ٱلْمُرْسَلُونَ
- (79:33) [next to 79:35] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (79:34) [next to 79:35] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (79:36) [next to 79:35] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- (79:37) [next to 79:35] فَأَمَّا مَن طَغَىٰ
- (80:1) [next to 80:3] عَبَسَ وَتَوَلَّىٰٓ
- (80:2) [next to 80:3] أَن جَآءَهُ ٱلْأَعْمَىٰ
- (89:21) [next to 89:23] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- (89:22) [next to 89:23] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- (89:25) [next to 89:23] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- (89:26) [next to 89:24] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ

