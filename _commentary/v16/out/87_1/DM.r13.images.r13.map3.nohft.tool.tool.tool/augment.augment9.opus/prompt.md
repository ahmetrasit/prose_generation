Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:1; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_1.reading.tr.md (prose paragraphs numbered) =====
## Emir kime, neye verilir

[¶1] Sure bir emirle açılır ve emir tek bir kişiye söylenir. {ar:سَبِّحِ, tr:sebbih, gloss:tesbih et; arıt ve yücelt, source:87:1} fiili tekil "sen"e yöneliktir. {ar:رَبِّكَ, tr:rabbike, gloss:senin Rabbin, source:87:1} sözünün sonundaki ek de aynı "sen"i gösterir. Bu "sen" surede kaybolmaz. Altıncı ayette {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız ve unutmayacaksın, source:87:6} denir, sekizinci ayette {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana hazırlayacağız, source:87:8}, dokuzuncu ayette ise {ar:فَذَكِّرْ, tr:fe-ẕekkir, gloss:öyleyse öğüt ver, source:87:9}. Kendisine okutulacak, yolu kolaylaştırılacak ve sonra başkalarına öğüt verecek olan kişinin ilk işi böylece kendi Rabbine yönelmek olur. Her namazda okunan Fatiha'da Rab {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabbi'l-âlemîn, gloss:âlemlerin Rabbi, source:1:2} diye anılır. Burada aynı kelime tek bir insana bağlanır: senin Rabbin.

[¶2] Emrin nesnesi addır ve araya hiçbir edat girmez. Bu küçük ayrıntı emrin ne istediğini değiştirir. Fatiha her okumayı {ar:بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:bismillâhi'r-rahmâni'r-rahîm, gloss:Rahman ve Rahim olan Allah'ın adıyla, source:1:1} diye açar. Okuyan söze adla, adın içinden girer. Kur'an buna benzeyen başka emirlerde de bu "ile" edatını kullanır. İnsana ektiğini, içtiği suyu ve yaktığı ateşi soran ayetlerin sonunda Peygamber'e {ar:فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ, tr:fe-sebbih bi'smi rabbike'l-azîm, gloss:büyük Rabbinin adıyla tesbih et, source:56:74} denir. Başka bir emir {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1} der. O cümlelerde ad bir araçtır ve eylem onunla yapılır. Bu ayette ise eylem doğrudan adın üzerine düşer. Arıtılıp yüksekte tutulması istenen şey adın kendisidir. Yani ayet yalnızca "Rabbini an" demiyor, insanın Rabbi için kullandığı adı korumasını istiyor.

[¶3] Son kelime {ar:ٱلْأَعْلَى, tr:el-a'lâ, gloss:en yüce, source:87:1} bir sıfattır, ama neyi nitelediği biçiminden anlaşılmaz. Arapçada sıfat, nitelediği kelimenin durum ekini alır. "Ad" burada nesne ekini, "Rab" ise tamlayan ekini taşır. الأعلى ise elifle biten bir kalıptadır ve bu kalıpta durum ekleri seslenmez. Bu yüzden sıfat hem Rab'be hem ada bağlanabilir. "En yüce Rabbinin adı" da "Rabbinin en yüce adı" da aynı sözde durur. Kur'an başka bir surede bu bağlantıyı seste açıkça gösterir ve iki yolu da kullanır. Yeryüzündeki herkesin yok olacağı söylendikten hemen sonra {ar:وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ, tr:ve yebkâ vechu rabbike ẕu'l-celâli ve'l-ikrâm, gloss:celal ve ikram sahibi olarak Rabbinin yüzü kalır, source:55:27} denir. ذو kelimesinin u sesi onu "yüz"e bağlar. Aynı surenin son ayeti ise {ar:تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ, tr:tebâreke'smu rabbike ẕi'l-celâli ve'l-ikrâm, gloss:celal ve ikram sahibi Rabbinin adı ne yücedir, source:55:78} der. Oradaki i sesi sıfatı addan ayırıp Rab'be verir. Bu ayette ise ses seçim yapmaz ve iki okuma birlikte duyulur. Rab en yücedir, onun adı da bu yüceliği taşır. Bir çeviri bunlardan birini seçmek zorunda kalır.

## Tesbih: arıtmak, uzak tutmak

[¶4] Türkçede "tespih" denince önce parmaklar arasında çekilen boncuk dizisi akla gelir. Arapçada bu dizinin ayrı bir adı vardır ve sonradan ortaya çıkmış bir kelime sayılır: {ar:الخرزات التي يعد بها المسبح تسبيحه السبحة وهي كلمة مولدة, tr:el-harazâtu'lletî ye'uddu bihe'l-musebbihu tesbîhahû es-subha ve hiye kelimetun muvellede, gloss:tesbih edenin tesbihini saydığı boncuklara subha denir; bu sonradan türemiş bir kelimedir, source:"س ب ح,B006"}. Ayetteki tesbih bir nesne değil, bir iştir. Bu işin özünü Araplar şöyle anlatırdı: {ar:التسبيح وهو تنزيه الله من كل سوء, tr:et-tesbîh ve huve tenzîhullâhi min kulli sû', gloss:tesbih Allah'ı her kötülükten uzak tutmaktır, source:"س ب ح,B002"}. {ar:سبحان تنزيه وتبرئة, tr:subhâne tenzîhun ve tebria, gloss:subhân uzak tutma ve aklamadır, source:"س ب ح,B002"}. Yani tesbih bir hüküm verir: Rab her eksikten, her yakışmayan nitelikten uzaktır. Aynı kelime aynı zamanda bir uygulamanın da adıdır: {ar:التسبيح عاما في العبادات قولا كان أو فعلا أو نية, tr:et-tesbîhu âmmen fi'l-ibâdâti kavlen kâne ev fi'len ev niyye, gloss:tesbih söz, iş ya da niyet olsun bütün ibadetlere verilen genel addır, source:"س ب ح,B001"}. Gönüllü kılınan namaz ve anma da bu adla anılır: {ar:السبحة التطوع من الذكر والصلاة, tr:es-subha et-tetavvuu mine'ẕ-ẕikri ve's-salât, gloss:subha gönüllü anma ve namazdır, source:"س ب ح,B001"}. Emir böylece iki şey ister: Rab hakkında doğru bir hüküm ve bu hükmü dile, bedene ve niyete taşıyan bir iş.

[¶5] Bu harflerin bir başka kullanımı suya ve koşuya aittir. Bundan sonra anılacak bu tür görüntüler kelimenin bu ayetteki anlamının yerine geçmez. Onun yanında, Arapça duyan kulağa ayrıca ulaşır. Suda yüzmek bu harflerle söylenir: {ar:السَّبح والسباحة العوم في الماء, tr:es-sebhu ve's-sibâha el-avmu fi'l-mâ, gloss:sebh ve sibâha suda yüzmektir, source:"س ب ح,B004"}. Daha genel olarak suda ya da havada hızla akıp gitmek de böyle anılır: {ar:السبح المر السريع في الماء وفي الهواء, tr:es-sebhu el-merru's-serî'u fi'l-mâi ve fi'l-hevâ, gloss:sebh suda ve havada hızla geçip gitmektir, source:"س ب ح,B004"}. Koşan ata da {ar:السابح من الخيل يمد يديه في الجري, tr:es-sâbihu mine'l-hayli yemuddu yedeyhi fi'l-cerî, gloss:sâbih koşarken ön ayaklarını ileri uzatan attır, source:"س ب ح,B004"} denirdi. Yıldızlar için de {ar:النجوم تسبح في الفلك, tr:en-nucûmu tesbehu fi'l-felek, gloss:yıldızlar yörüngede yüzer, source:"س ب ح,B004"} denirdi. Üç görüntüde de aynı işleyiş vardır. Yüzücü batmamak için kollarını durmadan ileri uzatır. At ön ayaklarını uzatarak yeri geçer. Yıldız düşmeden yörüngesinde akar. Hepsi bir ortamın içinde, durmayan bir hareketle taşınır. Yalnız bu görüntüyü ibadet anlamına bağlayan ortak bir kökeni varsaymamak gerekir, çünkü bu harflere iki ayrı asıl tanınır: {ar:أصلان أحدهما جنس من العبادة والآخر جنس من السعي, tr:aslâni ehaduhumâ cinsun mine'l-ibâdeti ve'l-âharu cinsun mine's-sa'y, gloss:iki asıl vardır: biri bir tür ibadet, öbürü bir tür koşup çabalama, source:"س ب ح,B005"}. İkisi arasındaki bağ köken değildir. Bağı aynı harfleri duyan kulak kurar.

[¶6] Kur'an'ın kendi dizilişi de bu kulağa yer açar. Allah inkâr edenlere göklerle yerin bir zamanlar bitişik olduğunu, kendisinin onları ayırdığını ve her canlıyı sudan yarattığını hatırlatır. Ardından göğü {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا, tr:ve cealne's-semâe sakfen mahfûzâ, gloss:göğü korunmuş bir tavan yaptık, source:21:32} diye anar, sonra gece ile gündüz, güneş ile ay için {ar:كُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ, tr:kullun fî felekin yesbehûn, gloss:hepsi bir yörüngede yüzüyor, source:21:33} der. Başka bir yerde de {ar:تُسَبِّحُ لَهُ ٱلسَّمَٰوَٰتُ ٱلسَّبْعُ وَٱلْأَرْضُ وَمَن فِيهِنَّ, tr:tusebbihu lehu's-semâvâtu's-seb'u ve'l-ardu ve men fîhinn, gloss:yedi gök, yer ve içlerindekiler onu tesbih eder, source:17:44} buyurur ve ekler: {ar:وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:ve lâkin lâ tefkahûne tesbîhahum, gloss:ama siz onların tesbihini kavramazsınız, source:17:44}. Yazıda fark görünür. Yörüngedeki yüzüş yalın fiille gelir (يَسْبَحُونَ), göklerin tesbihi ise orta harfi şeddeli, pekiştirilmiş fiille (يُسَبِّحُ). Bizim ayetteki emir bu ikinci kalıptadır. Ama ikisinde de aynı harfler yer alır, ve Kur'an göklerin tesbihinin nasıl olduğunu söylemez. Yalnızca insanın onu kavramadığını söyler.

[¶7] Aynı harfler bir peygamberin gününü ve gecesini de ikiye böler. Allah örtüsüne bürünmüş olana {ar:قُمِ ٱلَّيْلَ إِلَّا قَلِيلًۭا, tr:kumi'l-leyle illâ kalîlâ, gloss:birazı dışında geceyi ayakta geçir, source:73:2} der. Geceleyin kalkmanın daha sağlam ve sözü daha doğru kıldığını söyledikten sonra da ekler: {ar:إِنَّ لَكَ فِى ٱلنَّهَارِ سَبْحًۭا طَوِيلًۭا, tr:inne leke fi'n-nehâri sebhan tavîlâ, gloss:gündüz senin için uzun bir koşuşturma vardır, source:73:7}. Bu sebh, gündüzün gidip gelmesi ve geçim telaşıdır: {ar:السبح الفراغ والتصرف في المعاش والمنقلب والجيئة والذهاب, tr:es-sebhu'l-ferâğu ve't-tasarrufu fi'l-meâşi ve'l-munkalebi ve'l-cîeti ve'ẕ-ẕehâb, gloss:sebh boş zaman, geçim için iş görme, dönüp dolaşma, gidip gelmedir, source:"س ب ح,B005"}. Başka bir surede Allah Peygamber'e Kur'an'ı kendisinin indirdiğini söyler, sabretmesini ve {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا, tr:veẕkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25} demesini ister. Ardından gelen ayet {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا, tr:ve mine'l-leyli fescud lehû ve sebbihhu leylen tavîlâ, gloss:gecenin bir kısmında ona secde et ve onu uzun bir gece boyunca tesbih et, source:76:26} der. Gündüzün "uzun sebh"i ile gecenin "uzun tesbih"i aynı harflerle ve aynı "uzun" kelimesiyle söylenir. Gündüz insan işlerinin içinde yüzer. Gece aynı harflerin öbür anlamına, Rabbi arıtma işine döner. Bu ayetin emri de kendisine "gündüz uzun bir koşuşturma vardır" denen kişiye verilir.

[¶8] Kur'an tesbihi bir kez gerçekten suyun içinde gösterir. Yunus, Allah'ın gönderdiği elçilerdendir. Kaçarak {ar:إِذْ أَبَقَ إِلَى ٱلْفُلْكِ ٱلْمَشْحُونِ, tr:iẕ ebeka ile'l-fulki'l-meşhûn, gloss:hani dolu gemiye kaçmıştı, source:37:140}. Gemide kura çekilir ve kaybeden o olur: {ar:فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ, tr:fe-sâheme fe-kâne mine'l-mudhadîn, gloss:kura çekti ve kaybedenlerden oldu, source:37:141}. Sonra {ar:فَٱلْتَقَمَهُ ٱلْحُوتُ وَهُوَ مُلِيمٌۭ, tr:felteķamehu'l-hûtu ve huve mulîm, gloss:kınanacak durumdayken balık onu yuttu, source:37:142}. Hüküm şudur: {ar:فَلَوْلَآ أَنَّهُۥ كَانَ مِنَ ٱلْمُسَبِّحِينَ, tr:fe-levlâ ennehû kâne mine'l-musebbihîn, gloss:eğer tesbih edenlerden olmasaydı, source:37:143} {ar:لَلَبِثَ فِى بَطْنِهِۦٓ إِلَىٰ يَوْمِ يُبْعَثُونَ, tr:le-lebiŝe fî batnihî ilâ yevmi yub'aŝûn, gloss:dirilecekleri güne kadar onun karnında kalırdı, source:37:144}. Başka bir anlatımda karanlıklar içinden yaptığı çağrı da verilir: {ar:لَّآ إِلَٰهَ إِلَّآ أَنتَ سُبْحَٰنَكَ إِنِّى كُنتُ مِنَ ٱلظَّٰلِمِينَ, tr:lâ ilâhe illâ ente subhâneke innî kuntu mine'z-zâlimîn, gloss:senden başka ilah yok; sen her eksikten arısın; ben zalimlerden oldum, source:21:87}. Yunus yüzmez, yutulur. Onu dipte kalmaktan kurtaran söz ise aklamanın yönünü gösterir. Kusursuzluğu Rabbine verir, kusuru kendine alır. Tesbih burada kişinin kendini temize çıkarması değildir, eksiği nerede aradığını düzeltmesidir.

[¶9] Aynı harfler hem en yükseği hem en alçağı adlandırır. Yüzün görkemi için {ar:سبحات وجه ربنا يعني جلاله وعظمته ونوره, tr:subuhâtu vechi rabbinâ ya'nî celâlehû ve azametehû ve nûrah, gloss:Rabbimizin yüzünün subuhâtı onun celali, azameti ve nurudur, source:"س ب ح,B003"} denirdi. Secde edilen yerler için de {ar:السبحات مواضع السجود, tr:es-subuhât mevâdiu's-sucûd, gloss:subuhât secde yerleridir, source:"س ب ح,B003"} denirdi. Görkemin adı, alnın yere değdiği noktanın adıyla aynıdır. Bu emrin bir insanın bedeninde nasıl yerine getirildiğini on beşinci ayet gösterir: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını andı ve namaz kıldı, source:87:15}. Tesbihin, anmanın ve namazın birleştiği sahne o ayetin kelimeleriyle kurulur. Koşan atın görüntüsü de surenin başka bir sahnesine girer: on beşinci ayetteki namaz kelimesinin ailesinde öndekini izleyen ikinci at vardır, on altıncı ve on yedinci ayetlerin kelimelerinde ise öne geçenle sona kalan.

## Ad: yükselip seçilen

[¶10] Türkçede "isim" bir etikettir. Bir şeyin üstüne yapıştırılmış, onu ötekilerden ayırmaya yarayan bir sözcüktür. Arapçada ism kelimesi bir yükselişin içinden konuşur, çünkü kökü yükselmek anlamına gelir: {ar:السمو الارتفاع والعلو, tr:es-sumuvvu el-irtifâu ve'l-uluvv, gloss:sümüv yükselme ve yüceliktir, source:"س م و,B001"}. Soylu ve şerefli kişi için de {ar:ويقال للحسيب والشريف قد سما, tr:ve yukâlu li'l-hasîbi ve'ş-şerîfi kad semâ, gloss:soylu ve şerefli kişiye "yükseldi" denir, source:"س م و,B001"} denirdi. Adın bu kökten nasıl geldiği de açıklanır: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-uluvvi li-ennehû tenvîhun ve delâletun ale'l-ma'nâ, gloss:ismin aslı sümüvdür ve yüceliktendir, çünkü bir şeyi anıp yükseltir ve anlamı gösterir, source:"س م و,B005"}. {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismu mâ yu'rafu bihî ẕâtu'ş-şey'i ve asluhû sumuvv bihî rufia ẕikru'l-musemmâ, gloss:isim bir şeyin kendisinin tanındığı şeydir; aslı sümüvdür; adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Ad bir etiket olmaktan önce bir yükseltmedir. Adlandırılanı söze çıkarır ve orada görünür kılar.

[¶11] Bu yükselişin çölde bir görüntüsü vardır: {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hatte'steŝbettuh, gloss:bana bir karaltı yükseldi, öyle ki onu iyice seçebildim, source:"س م و,B002"}. Ayın ilk hilali için de {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetu'l-hilâli şahsuhû iẕe'rtefea ani'l-ufuki şey'en, gloss:hilalin semâvesi ufuktan biraz yükseldiğinde görünen biçimidir, source:"س م و,B002"} denirdi. Bu işleyiş tanıdıktır. Ufuk çizgisine yapışık duran şey seçilmez, toprağa ve ışığa karışır. Biraz yükselince göz onu tutabilir ve ne olduğunu kestirebilir. Ad da adlandırılanı böyle yığından ayırır. Uzaktaki şeyi seçilebilir bir biçim haline getirir. Bu görüntünün yanında adı tesbih etmek, ufuktan yükselmiş o biçimi temiz tutmak, onu başka karaltılarla karıştırmamak olarak duyulur. Kur'an'da vahyi getiren için de bir ufuk anılır: {ar:عَلَّمَهُۥ شَدِيدُ ٱلْقُوَىٰ, tr:allemehû şedîdu'l-kuvâ, gloss:ona gücü çetin olan öğretti, source:53:5}, {ar:وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ, tr:ve huve bi'l-ufuki'l-a'lâ, gloss:o en yüksek ufuktaydı, source:53:7}. Bu ayetteki "en yüce" kelimesi orada ufku niteler.

[¶12] Aynı kök göğü de verir, çünkü gök de üstte olandır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp seni gölgeleyen her şeydir, source:"س م و,B004"}. Bu tanıma göre evin tavanı da gök sayılır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyti ve kullu âlin mutillin semâ, gloss:semâ evin tavanıdır; yukarıdan sarkan her yüksek şey semâdır, source:"س م و,B004"}. Bulut da yağmur da aynı adla anılır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}. Göğün altında yükselen bitki de öyle: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt yön değil, yükselmektir. Bir şey insanın üstüne çıkar, onu örter ya da topraktan başını kaldırırsa bu adı alır. Ad kelimesi bu bakımdan göğün kardeşidir. Buluttan yağmura, yağmurdan otlağa uzanan sahne dördüncü ve beşinci ayetin kelimeleriyle tamamlanır, ayetin adı ise o sahnenin üst ucunda durur.

[¶13] ism kelimesi için Arapçada kayıtlı ikinci bir türetme de vardır. Bu türetme kelimeyi وسم köküne, yani damgaya bağlar. Bu kök kimliği değil, belgelenmiş bir alternatiftir, ama bu yoldan da görüntü açıktır. Develere basılan iz için {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmu eseru keyyin ve baîrun mevsûmun vusime bi-simetin yu'rafu bihâ min kat'ı uẕunin ev keyy, gloss:vesm dağlama izidir; damgalı deve, kulak kesiği ya da dağlama gibi tanındığı bir işaretle işaretlenmiştir, source:"و س م,B001"} denirdi. İzi basan alet de {ar:الميسم المكواة أو الشيء الذي يوسم به الدواب, tr:el-mîsem el-mikvâtu evi'ş-şey'u'lleẕî yûsemu bihi'd-devâbb, gloss:mîsem dağlama demiri ya da hayvanların işaretlendiği alettir, source:"و س م,B001"} diye anılırdı. Kızgın demir deriye bastırılır, iz kalıcı olur ve sürüye karışan hayvanın kime ait olduğu uzaktan bilinir. Aynı kök izden kişiyi okumayı da anlatır: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtu fîhi'l-hayra ve'ş-şerra ey raeytu fîhi eseren, gloss:onda iyiliği ve kötülüğü sezdim, yani onda bir iz gördüm, source:"و س م,B002"}. Yılın ilk yağmuru da bu köktendir, çünkü toprağa yeşil bir iz basar: {ar:الوسمي أول المطر لأنه يسم الأرض بالنبات, tr:el-vesmiyyu evvelu'l-matari li-ennehû yesimu'l-arda bi'n-nebât, gloss:vesmî ilk yağmurdur, çünkü toprağı bitkiyle damgalar, source:"و س م,B003"}. Bu yoldan bakıldığında ad, sahibini gösteren ve onu ötekilerden ayıran bir izdir. Damganın ateşle ve tercih edilen hayatın bıraktığı izle kurduğu sahne ise on ikinci ayetteki ateşin ve on altıncı ayetteki "tercih edersiniz" fiilinin kelimelerine aittir.

## Rab: sahip olan, kalan, tamamlayan

[¶14] Türkçede "Rab" yalnızca Allah için kullanılır. Arapçada da kelime tek başına söylendiğinde yalnızca Allah'ı gösterir: {ar:لا يقال الرب مطلقا إلا لله, tr:lâ yukâlu'r-rabbu mutlakan illâ lillâh, gloss:rab kayıtsız olarak yalnızca Allah için söylenir, source:"ر ب ب,B001"}. Ama bir tamlamanın içinde gündelik hayatta da dolaşır: {ar:رب الدار ورب الفرس, tr:rabbu'd-dâri ve rabbu'l-feres, gloss:evin sahibi ve atın sahibi, source:"ر ب ب,B001"}. Annenin kocasına da bu kökten bir ad verilirdi: {ar:الراب: زوج الأم, tr:er-râbb zevcu'l-umm, gloss:râbb annenin kocasıdır, source:"ر ب ب,B005"}, çünkü {ar:الراب والرابة بأحد الزوجين إذا تولى تربية الولد, tr:er-râbbu ve'r-râbbe bi-ehadi'z-zevceyni iẕâ tevellâ terbiyete'l-veled, gloss:râbb ve râbbe, çocuğun yetiştirilmesini üstlenen eşe denir, source:"ر ب ب,B005"}. Yani Arapça kulak "Rabbin" sözünde sahipliği, buyruğun yürümesini ve kan bağı olmadan üstlenilmiş bir bakımı birlikte duyar. Sahip için {ar:ويكون الرب: السيد المطاع, tr:ve yekûnu'r-rabbu es-seyyide'l-mutâ', gloss:rab sözü dinlenen efendi anlamına da gelir, source:"ر ب ب,B001"} denir, düzeltici için de {ar:ويكون الرب: المصلح, tr:ve yekûnu'r-rabbu el-muslih, gloss:rab düzelten anlamına da gelir, source:"ر ب ب,B001"}.

[¶15] Kelimenin işleyen yanı terbiyedir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}. Çiftliğine bakan için {ar:رب الضيعة أي أصلحها وأتمها, tr:rabbe'd-day'ate ey aslahahâ ve etemmehâ, gloss:çiftliği düzeltti ve tamamladı, source:"ر ب ب,B002"} denir. Yapılan bir iyiliği eksiksiz kılmak da böyle anılır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-raculu'n-ni'mete yerubbuhâ rabben ve ribâbeten iẕâ temmemehâ, gloss:adam iyiliği tamamladığında "onu rabbetti" denir, source:"ر ب ب,B002"}. Ayetin ardından gelen dört ayet bu tanımı adım adım sahneye koyar. İkinci ayette yaratır ve düzene koyar, üçüncü ayette ölçer ve yol gösterir, dördüncü ayette otlağı çıkarır, beşinci ayette onu kararmış bir döküntüye çevirir. "Rabbin" kelimesinden sonra gelen bu sıra, halden hale geçirmenin ta kendisidir, ve bu sıranın sonunda solmak da vardır. Bilgi de bu yolla verilir. Bu köke nispet edilen bilgin için {ar:العالم المعلم الذي يغذو الناس بصغار العلوم, tr:el-âlimu'l-muallimu'lleẕî yağẕu'n-nâse bi-sığâri'l-ulûm, gloss:insanları küçük bilgilerle besleyen öğretici bilgin, source:"ر ب ب,B003"} denir. Altıncı ayetteki "sana okutacağız" vaadi de aynı Rab'den gelir.

[¶16] Kökün somut kullanımları bir yerde kalmayı, toplamayı ve sağlamlaştırmayı gösterir. Bir yerden ayrılmayan kişi için {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fulânun bi'l-mekâni iẕâ ekâme bihî fe-lem yebrahh, gloss:falanca bir yerde kalıp oradan ayrılmadığında erabbe denir, source:"ر ب ب,B007"} denir. Develerin bağlı kaldığı yere {ar:مرب الإبل أي حيث لزمته, tr:merabbu'l-ibil ey haysu lezimethu, gloss:develerin ayrılmadığı yer, source:"ر ب ب,B007"} denir. Bulut da bir yerde durup sürebilir: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Belli bir bulutun adı da bu köktendir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi yetiştirdiği için bu adı almıştır, source:"ر ب ب,B008"}. Bu bulut ötekilerin altında asılı durur: {ar:السحاب المتعلق دون السحاب يكون أبيض ويكون أسود, tr:es-sehâbu'l-muteallaku dûne's-sehâbi yekûnu ebyada ve yekûnu esved, gloss:bulutların altında asılı duran bulut; beyaz da olur kara da, source:"ر ب ب,B008"}. Bol su için de {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabeb ve huve'l-mâu'l-keŝîr sumiye bi-ẕâlike li-ictimâih, gloss:rabeb bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"} denir. Yaban sığırı sürüsüne {ar:الربرب: القطيع من بقر الوحش, tr:er-rabrab el-katîu min bakari'l-vahş, gloss:rabrab yaban sığırı sürüsüdür, source:"ر ب ب,B014"} denir. Kumar oklarını bir arada tutan kese de bu adla anılır: {ar:الربابة: قطعة من أدم تجمع فيها القداح, tr:er-ribâbe kıt'atun min edemin tucmeu fîhe'l-kıdâh, gloss:ribâbe okların toplandığı bir deri parçasıdır, source:"ر ب ب,B010"}. Tarafları birbirine bağlayan söz de öyle: {ar:الربابة: العهد والميثاق, tr:er-ribâbe el-ahdu ve'l-mîŝâk, gloss:ribâbe ahit ve bağlayıcı sözdür, source:"ر ب ب,B011"}. Bir mutfak ve zanaat sözü de buraya girer: {ar:رب السمن والزيت: ثفله الأسود, tr:rubbu's-semni ve'z-zeyt sufluhu'l-esved, gloss:yağın rubbu dibinde kalan kara tortudur, source:"ر ب ب,B006"}. Kaynatılıp koyulaştırılan meyve özü de bu adla anılır ve deri kaba sürülür: {ar:سقاء مربوب إذا أصلح بالرب, tr:sikâun merbûbun iẕâ usliha bi'r-rubb, gloss:rubla iyileştirilmiş tuluma merbûb denir, source:"ر ب ب,B006"}. Koyu öz derinin içine işler ve onu sağlamlaştırır: {ar:رب فلان نحيه إذا جعل فيه الرب ومتنه به, tr:rabbe fulânun nihyehû iẕâ cealehû fîhi'r-rubbe ve metenehû bih, gloss:yağ tulumuna rub koyup onu sağlamlaştırdı, source:"ر ب ب,B006"}. Bir de yazın sararmayan otlar vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}.

[¶17] Bu nesnelerin hepsi aynı hareketi gösterir: dağılabilecek olanı bir arada tutmak, gidebilecek olanı yerinde tutmak, sızabilecek olanı sağlamlaştırmak. Sürü toplanır, su birikir, oklar bir kesede durur, ahit tarafları bağlar, alçak bulut yerinden ayrılmaz ve bitkiyi yetiştirir. Bu ortaklık dilin bir kanıtı değil, bir okumadır. Ama ayetin Rab'bine bu ışıkta bakıldığında sahiplik soğuk bir mülkiyet olmaktan çıkar. Sahip olan, sahip olduğu şeyle kalır, onu toplar ve tamamlanana kadar bırakmaz. Bu görüntüler surede başka ayetlerin kelimeleriyle sahnelere dönüşür. Bulut ile sararmayan ot dördüncü ve beşinci ayetin otlağıyla buluşur. Sürü üçüncü ayetteki "yol gösterdi" ve dördüncü ayetteki "otlak" ile bir çoban sahnesi kurar. Ok kesesi ile tulum ikinci ve üçüncü ayetin ölçüp biçmesine, sekizinci ayetin kolaylığına ve dokuzuncu ayetin faydasına bağlanır. Çiftliğin bakımı on dördüncü ayetin yarılan tarlasına, çocuğun büyütülmesi de ikinci ayetin düzene konan bedenine uzanır.

## En yüce: karşılaştırmasız bir doruk

[¶18] {ar:ٱلْأَعْلَى, tr:el-a'lâ, gloss:en yüce, source:87:1} bir üstünlük kalıbıdır, ama yanında karşılaştırılan bir şey yoktur. "Şundan daha yüce" demez, yalnızca en yüceliği söyler. Türkçede bu kelimenin bir akrabası "âlâ" olarak yaşar ve "birinci kalite, pek iyi" anlamına gelir. Arapçada kelimenin merkezinde ise beğeni değil yükseklik vardır, aşağının karşıtı olan yukarısı: {ar:العلو ضد السفل والعلو الارتفاع, tr:el-uluvvu diddu's-sufli ve'l-uluvvu el-irtifâ', gloss:ulüv aşağılığın karşıtıdır; ulüv yükselmektir, source:"ع ل و,B001"}. Kökün tanımı dikkat çekici bir sözle yapılır: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullu ale's-sumuvvi ve'l-irtifâ', gloss:sümüv ve yükseklik bildiren tek bir asıldır, source:"ع ل و,B001"}. Sümüv, ayetin ikinci kelimesi olan ism'in köküdür. İki kök ayrıdır ve biri öbüründen türemez, ama biri öbürüyle tanımlanır. Ayet bu yüzden iki ayrı yükseklik kelimesini bir araya getirir: yükseltmekten gelen bir ad ve en yüksek olanı bildiren bir sıfat. Birinci bölümde görüldüğü gibi sıfatın ada da Rab'be de bağlanabilmesi bu buluşmayı daha da sıkılaştırır.

[¶19] Yükseklik kelimesinin somut kullanımları bu doruğun neye benzediğini gösterir. Dağ başı için {ar:العلياء رأس كل جبل أو شرف, tr:el-alyâu ra'su kulli cebelin ev şeref, gloss:alyâ her dağın ya da yüksek yerin başıdır, source:"ع ل و,B007"} denir. Mektubun en üstünde duran başlık da bu köktendir: {ar:علوان الكتاب من العلو لأنه أول الكتاب وأعلاه, tr:ulvânu'l-kitâbi mine'l-uluvvi li-ennehû evvelu'l-kitâbi ve a'lâh, gloss:mektubun ulvânı yücelikten gelir, çünkü mektubun başı ve en üstüdür, source:"ع ل و,B008"}. Başlık mektubun kimden ve kime olduğunu, ne hakkında olduğunu söyleyen addır ve en üste yazılır. Adın yükseltmek anlamıyla bu görüntü kendiliğinden buluşur. Kumar oklarının dizisinde de bir "en yüce" vardır: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Bu, dizinin en değerli okudur {source:"ع ل و,B009"}. Okların ve payların sahnesi ise ikinci ve üçüncü ayetin ölçüp biçme fiilleriyle, sekizinci ayetteki kolaylık kelimesinin kökünde saklı oyunla kurulur.

[¶20] Yükseklik her zaman övülmez: {ar:علا يقال في المحمود والمذموم, tr:alâ yukâlu fi'l-mahmûdi ve'l-mezmûm, gloss:alâ hem övülen hem kınanan için söylenir, source:"ع ل و,B003"}. Kınanan yanı şöyle anlatılır: {ar:علا ملك في الأرض أي طغى وتعظم, tr:alâ melikun fi'l-ardi ey tağâ ve teazzam, gloss:bir hükümdar yeryüzünde yükseldi, yani azdı ve büyüklük tasladı, source:"ع ل و,B003"}. Övülen yanı ise yerinde verilmiş üstünlüktür. Musa, Firavun'un sihirbazlarının attığı iplerin ve değneklerin karşısında içinde bir korku duyduğunda Allah ona {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma dedik, üstün gelen sensin, source:20:68} der. Ardından gelen ayet {ar:وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ, tr:ve lâ yuflihu's-sâhiru haysu etâ, gloss:büyücü nereye varsa kurtuluşa eremez, source:20:69} der. Bu üstünlük Musa'nın kendinden değil, ona söylenen sözden gelir. Malını arınmak için veren kişi için de {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin yüzünü istemek için, source:92:20} denir. Bu ayetteki "Rab" ve "en yüce" orada da yan yana durur, ve bu kişinin kimseye bir iyilik borcunu ödemek için vermediği söylenir. Yükseklik ekseninin öbür ucu, yani on altıncı ayetteki "dünya", yakın ve alçak olan anlamıyla surenin ikinci yarısında yer alır.

[¶21] Yükseklik kelimesinin bir de çağrı biçimi vardır: {ar:تعال أصله أن يدعى الإنسان إلى مكان مرتفع, tr:teâle asluhû en yud'a'l-insânu ilâ mekânin murtefi', gloss:teâlin aslı insanın yüksek bir yere çağrılmasıdır, source:"ع ل و,B006"}. "Gel" demek, aslında "yukarı çık" demektir. Kur'an bu çağrıyı tam da Rab kelimesinin çoğuluyla birlikte kullanır. Peygamber'e Kitap ehline şöyle seslenmesi söylenir: {ar:قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ تَعَالَوْا۟ إِلَىٰ كَلِمَةٍۢ سَوَآءٍۭ بَيْنَنَا وَبَيْنَكُمْ, tr:kul yâ ehle'l-kitâbi teâlev ilâ kelimetin sevâin beynenâ ve beynekum, gloss:de ki: ey Kitap ehli, bizimle sizin aranızda ortak bir söze gelin, source:3:64}. O söz de şudur: {ar:وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ, tr:ve lâ yettehıze ba'dunâ ba'dan erbâben min dûnillâh, gloss:Allah'ı bırakıp birbirimizi rabler edinmeyelim, source:3:64}. Yukarı çağıran söz, rablik adının kimseye dağıtılmamasıdır.

## Adaşı olmayan ad

[¶22] Bir adı arıtmanın ne demek olduğunu Arapçanın ad etrafındaki öbür kelimeleri gösterir. Ad bir kişiye verilir: {ar:سميت فلانا زيدا, tr:semmeytu fulânen zeyden, gloss:falancaya Zeyd adını verdim, source:"س م و,B005"}. Aynı adı taşıyana da bir ad verilir: {ar:هذا سمي فلان, tr:hâẕâ semiyyu fulân, gloss:bu, falancanın adaşıdır, source:"س م و,B005"}. Adaşlık yalnızca bir ses benzerliği değildir. Aynı adı taşımayı hak eden bir dengi de anlatır: {ar:سميا أي نظيرا له يستحق اسمه, tr:semiyyen ey nazîran lehû yestehıkku'smeh, gloss:semiyy onun adını hak eden bir benzeridir, source:"س م و,B005"}. Yarışmak da bu köktendir: {ar:تساموا أي تباروا, tr:tesâmev ey tebârev, gloss:birbiriyle boy ölçüştüler, source:"س م و,B007"}. Kimsenin yarışamadığı kişi için de {ar:فلان لا يسامى, tr:fulânun lâ yusâmâ, gloss:falancayla kimse boy ölçüşemez, source:"س م و,B007"} denirdi. Aynı ad bir yarışma alanı açar. Birinin adını almak, onun yerine aday olmaktır.

[¶23] Kur'an bu kelimeyi iki kez kullanır ve ikisi de bu ağırlığı taşır. Zekeriya bir oğul için Rabbine yalvardığında ona {ar:يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا, tr:yâ zekeriyyâ innâ nubeşşiruke bi-ğulâminismuhû yahyâ lem nec'al lehû min kablu semiyyâ, gloss:ey Zekeriya, sana adı Yahya olan bir oğul müjdeliyoruz; daha önce ona hiç adaş yapmadık, source:19:7} denir. Aynı surede, vahyi indirenler Peygamber'e {ar:وَمَا نَتَنَزَّلُ إِلَّا بِأَمْرِ رَبِّكَ, tr:ve mâ netenezzelu illâ bi-emri rabbik, gloss:biz ancak Rabbinin buyruğuyla ineriz, source:19:64} dedikten sonra şöyle sürdürür: {ar:رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:rabbu's-semâvâti ve'l-ardi ve mâ beynehumâ fa'budhu vastabir li-ibâdetih hel ta'lemu lehû semiyyâ, gloss:göklerin, yerin ve aralarındakilerin Rabbidir; ona kulluk et ve kulluğunda sabırlı ol; onun bir adaşını biliyor musun, source:19:65}. Bu soru, "Rabbinin adını tesbih et" emrinin bir yüzünü açar. O adın adaşı yoktur. Onu taşımayı hak eden bir denk, onunla boy ölçüşen bir rakip yoktur. Adı tesbih etmek, onu böyle tutmak, başka hiçbir şeye vermemek ve onunla yarışan hiçbir iddiayı kabul etmemektir.

[¶24] Kur'an adın başka şeylere dağıtıldığı durumu da adıyla anar. Lât'ı, Uzzâ'yı ve üçüncüleri Menât'ı sayan ayetlerin ardından {ar:إِنْ هِىَ إِلَّآ أَسْمَآءٌۭ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّآ أَنزَلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍ, tr:in hiye illâ esmâun semmeytumûhâ entum ve âbâukum mâ enzelallâhu bihâ min sultân, gloss:bunlar sizin ve atalarınızın taktığı adlardan başka bir şey değildir; Allah onlar için hiçbir delil indirmemiştir, source:53:23} denir. Bu ayet, en yüksek ufuktaki görülen varlığı anlatan ayetlerle aynı suredendir. Bir yanda ufukta gerçekten yükselip seçilen bir şey, öbür yanda arkasında hiçbir şey olmayan, yalnızca söylenmiş adlar vardır. Başka bir yerde {ar:وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ, tr:ve lillâhi'l-esmâu'l-husnâ fed'ûhu bihâ ve ẕeru'lleẕîne yulhidûne fî esmâih, gloss:en güzel adlar Allah'ındır; onunla bu adlarla dua edin ve onun adlarında yoldan sapanları bırakın, source:7:180} denir. Adı arıtmak, bu sapmanın karşıtıdır. Ad yerinde tutulur, başkasına giydirilmez, kendisine yakışmayan bir anlamla doldurulmaz.

[¶25] Kur'an adlar ile tesbihi bir başka sahnede de buluşturur. Allah meleklere yeryüzünde bir halife yaratacağını söyler. Melekler, orada bozgunculuk yapacak ve kan dökecek birinin mi yaratılacağını sorar ve kendilerinden {ar:وَنَحْنُ نُسَبِّحُ بِحَمْدِكَ وَنُقَدِّسُ لَكَ, tr:ve nahnu nusebbihu bi-hamdike ve nukaddisu lek, gloss:oysa biz seni överek tesbih ediyor ve seni kutsuyoruz, source:2:30} diye söz ederler. Sonra {ar:وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا, tr:ve alleme âdeme'l-esmâe kullehâ, gloss:Adem'e bütün adları öğretti, source:2:31} denir. Meleklerden bunların adlarını söylemeleri istenir, ama söyleyemezler. Cevapları tesbihle başlar: {ar:قَالُوا۟ سُبْحَٰنَكَ لَا عِلْمَ لَنَآ إِلَّا مَا عَلَّمْتَنَآ, tr:kâlû subhâneke lâ ilme lenâ illâ mâ allemtenâ, gloss:dediler ki: sen her eksikten arısın; senin bize öğrettiğinden başka bilgimiz yoktur, source:2:32}. İlk tesbih bir iddiaya eşlik ediyordu. Adlar karşısındaki tesbih ise bir sınırı kabul eder. Tıpkı Yunus'un karanlıktaki sözünde olduğu gibi, kusursuzluk Rabbe verilir, eksik kişinin kendisinde aranır. Adları bilen ve öğreten O olduğu için adını arıtmak, onu bilenin bilgisine bırakmak demektir. Allah'ı yaratan, var eden ve biçim veren diye anan bir ayet de {ar:لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:lehu'l-esmâu'l-husnâ yusebbihu lehû mâ fi's-semâvâti ve'l-ard, gloss:en güzel adlar onundur; göklerde ve yerde olanlar onu tesbih eder, source:59:24} der. Adlar ile tesbih orada aynı cümlede birbirine bağlanır.

[¶26] Bu ayetin üç kelimesinin bir yaratık tarafından sahiplenildiği bir an da Kur'an'da vardır. Allah Musa'ya {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:iẕheb ilâ fir'avne innehû tağâ, gloss:Firavun'a git, o azdı, source:79:17} der. Musa ona büyük mucizeyi gösterir, Firavun ise yalanlar ve karşı gelir. Sonra {ar:فَحَشَرَ فَنَادَىٰ, tr:fe-haşera fe-nâdâ, gloss:halkı topladı ve seslendi, source:79:23} ve {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Bu cümlede durum eki görünür: "rabbukum" yalın haldedir ve "en yüce" kesinlikle Rab'bi niteler. Firavun ad koymaz, adı alır. Rab'bin adını ve onun en yüceliğini kendi üstüne geçirir. Az önce anılan, yeryüzünde yükselmek ile azmanın aynı söz olduğunu söyleyen kullanım, bu sahnede bir hükümdarın ağzından gerçekleşir. Bizim ayetteki emir, bu sözün tam karşısında durur. Aynı "Rab" ve aynı "en yüce" bu kez "senin" diye başlayan bir tamlamada gelir, ve yapılması istenen iş o adı herkesten ve her iddiadan uzak tutmaktır. Firavun'un bir halkı toplayıp söylediğini, bu ayet tek bir kişiye sessizce yaptırır. Ad yükseltilir, ama yükselten onu kendine almaz.

===== _commentary/v16/out/87_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: alif-maqsura adjectives (الأعلى) show no case ending, so attachment to اسم or رب is ambiguous
- memory: ذو/ذي case vowels mark attachment in 55:27 vs 55:78
- memory: أفعل elative used without مِن gives an absolute superlative
- memory: يَسْبَحُ (form I) vs يُسَبِّحُ (form II, doubled middle) as distinct verb patterns
- memory: Turkish "âlâ" and "tespih" current meanings (Turkish usage)
- not written: echo root ر ب و (rabwa, swelling, growth) - echo only, cannot establish identity with رب
- not written: ر ب ب B015 particle rubba, B016 knot/need, B017 ship captain, B009 fresh ewe - no work in this ayah's theme
- not written: س ب ح B007 children's leather shirt, B008 valley name - no bearing on the command
- not written: س م و B003 stallion among she-camels, B006 hunters, B008 good fame - did not ground or join a theme
- not written: ع ل و B010 tall build, B011 recovery after childbirth, B012 preposition على - no work here
- not written: و س م B004 mawsim gathering, B005 beauty, B006 dye plant - alternative derivation; only the mark/brand line served the name theme

===== passages not cited (256) =====
## strong (this ayah's own list) (39)

- (1:2) [listed for 87:1] [cited in ¶1] ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (3:191) [listed for 87:1] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
- (7:180) [listed for 87:1] [cited in ¶24] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
- (10:10) [listed for 87:1] دَعْوَىٰهُمْ فِيهَا سُبْحَٰنَكَ ٱللَّهُمَّ وَتَحِيَّتُهُمْ فِيهَا سَلَٰمٌۭ ۚ وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (15:98) [listed for 87:1] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ ٱلسَّٰجِدِينَ
- (17:43) [listed for 87:1] سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يَقُولُونَ عُلُوًّۭا كَبِيرًۭا
- (17:110) [listed for 87:1] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (17:111) [listed for 87:1] وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ ۖ وَكَبِّرْهُ تَكْبِيرًۢا
- (19:65) [listed for 87:1] [cited in ¶23] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:8) [listed for 87:1] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:50) [listed for 87:1] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (20:130) [listed for 87:1] فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا ۖ وَمِنْ ءَانَآئِ ٱلَّيْلِ فَسَبِّحْ وَأَطْرَافَ ٱلنَّهَارِ لَعَلَّكَ تَرْضَىٰ
- (21:87) [listed for 87:1] [cited in ¶8] وَذَا ٱلنُّونِ إِذ ذَّهَبَ مُغَٰضِبًۭا فَظَنَّ أَن لَّن نَّقْدِرَ عَلَيْهِ فَنَادَىٰ فِى ٱلظُّلُمَٰتِ أَن لَّآ إِلَٰهَ إِلَّآ أَنتَ سُبْحَٰنَكَ إِنِّى كُنتُ مِنَ ٱلظَّٰلِمِينَ
- (23:91) [listed for 87:1] مَا ٱتَّخَذَ ٱللَّهُ مِن وَلَدٍۢ وَمَا كَانَ مَعَهُۥ مِنْ إِلَٰهٍ ۚ إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ وَلَعَلَا بَعْضُهُمْ عَلَىٰ بَعْضٍۢ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يَصِفُونَ
- (25:2) [listed for 87:1] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
- (25:58) [listed for 87:1] وَتَوَكَّلْ عَلَى ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ وَسَبِّحْ بِحَمْدِهِۦ ۚ وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا
- (30:17) [listed for 87:1] فَسُبْحَٰنَ ٱللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ
- (32:15) [listed for 87:1] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (33:41) [listed for 87:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (36:36) [listed for 87:1] سُبْحَٰنَ ٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ وَمِنْ أَنفُسِهِمْ وَمِمَّا لَا يَعْلَمُونَ
- (37:143) [listed for 87:1] [cited in ¶8] فَلَوْلَآ أَنَّهُۥ كَانَ مِنَ ٱلْمُسَبِّحِينَ
- (37:180) [listed for 87:1] سُبْحَٰنَ رَبِّكَ رَبِّ ٱلْعِزَّةِ عَمَّا يَصِفُونَ
- (40:55) [listed for 87:1] فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَسَبِّحْ بِحَمْدِ رَبِّكَ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
- (43:82) [listed for 87:1] سُبْحَٰنَ رَبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبِّ ٱلْعَرْشِ عَمَّا يَصِفُونَ
- (50:39) [listed for 87:1] فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ ٱلْغُرُوبِ
- (52:48) [listed for 87:1] وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا ۖ وَسَبِّحْ بِحَمْدِ رَبِّكَ حِينَ تَقُومُ
- (54:49) [listed for 87:1] إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ
- (55:78) [listed for 87:1] [cited in ¶3] تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (56:74) [listed for 87:1] [cited in ¶2] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (59:23) [listed for 87:1] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ٱلْمَلِكُ ٱلْقُدُّوسُ ٱلسَّلَٰمُ ٱلْمُؤْمِنُ ٱلْمُهَيْمِنُ ٱلْعَزِيزُ ٱلْجَبَّارُ ٱلْمُتَكَبِّرُ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- (59:24) [listed for 87:1] [cited in ¶25] هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (68:29) [listed for 87:1] قَالُوا۟ سُبْحَٰنَ رَبِّنَآ إِنَّا كُنَّا ظَٰلِمِينَ
- (68:48) [listed for 87:1] فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تَكُن كَصَاحِبِ ٱلْحُوتِ إِذْ نَادَىٰ وَهُوَ مَكْظُومٌۭ
- (69:52) [listed for 87:1] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (76:25) [listed for 87:1] [cited in ¶7] وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا
- (79:24) [listed for 87:1] [cited in ¶26] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
- (92:20) [listed for 87:1] [cited in ¶20] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (96:1) [listed for 87:1] [cited in ¶2] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- (110:3) [listed for 87:1] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا

## medium (this ayah's own list) (59)

- (5:4) [listed for 87:1] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (6:100) [listed for 87:1] وَجَعَلُوا۟ لِلَّهِ شُرَكَآءَ ٱلْجِنَّ وَخَلَقَهُمْ ۖ وَخَرَقُوا۟ لَهُۥ بَنِينَ وَبَنَٰتٍۭ بِغَيْرِ عِلْمٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يَصِفُونَ
- (6:118) [listed for 87:1] فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ إِن كُنتُم بِـَٔايَٰتِهِۦ مُؤْمِنِينَ
- (6:121) [listed for 87:1] وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ وَإِنَّهُۥ لَفِسْقٌۭ ۗ وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ ۖ وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ
- (6:138) [listed for 87:1] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
- (7:54) [listed for 87:1] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ وَٱلنُّجُومَ مُسَخَّرَٰتٍۭ بِأَمْرِهِۦٓ ۗ أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ ۗ تَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (9:40) [listed for 87:1] إِلَّا تَنصُرُوهُ فَقَدْ نَصَرَهُ ٱللَّهُ إِذْ أَخْرَجَهُ ٱلَّذِينَ كَفَرُوا۟ ثَانِىَ ٱثْنَيْنِ إِذْ هُمَا فِى ٱلْغَارِ إِذْ يَقُولُ لِصَٰحِبِهِۦ لَا تَحْزَنْ إِنَّ ٱللَّهَ مَعَنَا ۖ فَأَنزَلَ ٱللَّهُ سَكِينَتَهُۥ عَلَيْهِ وَأَيَّدَهُۥ بِجُنُودٍۢ لَّمْ تَرَوْهَا وَجَعَلَ كَلِمَةَ ٱلَّذِينَ كَفَرُوا۟ ٱلسُّفْلَىٰ ۗ وَكَلِمَةُ ٱللَّهِ هِىَ ٱلْعُلْيَا ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ
- (10:3) [listed for 87:1] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۖ يُدَبِّرُ ٱلْأَمْرَ ۖ مَا مِن شَفِيعٍ إِلَّا مِنۢ بَعْدِ إِذْنِهِۦ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ فَٱعْبُدُوهُ ۚ أَفَلَا تَذَكَّرُونَ
- (10:68) [listed for 87:1] قَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ ۖ هُوَ ٱلْغَنِىُّ ۖ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۚ إِنْ عِندَكُم مِّن سُلْطَٰنٍۭ بِهَٰذَآ ۚ أَتَقُولُونَ عَلَى ٱللَّهِ مَا لَا تَعْلَمُونَ
- (10:83) [listed for 87:1] فَمَآ ءَامَنَ لِمُوسَىٰٓ إِلَّا ذُرِّيَّةٌۭ مِّن قَوْمِهِۦ عَلَىٰ خَوْفٍۢ مِّن فِرْعَوْنَ وَمَلَإِي۟هِمْ أَن يَفْتِنَهُمْ ۚ وَإِنَّ فِرْعَوْنَ لَعَالٍۢ فِى ٱلْأَرْضِ وَإِنَّهُۥ لَمِنَ ٱلْمُسْرِفِينَ
- (12:108) [listed for 87:1] قُلْ هَٰذِهِۦ سَبِيلِىٓ أَدْعُوٓا۟ إِلَى ٱللَّهِ ۚ عَلَىٰ بَصِيرَةٍ أَنَا۠ وَمَنِ ٱتَّبَعَنِى ۖ وَسُبْحَٰنَ ٱللَّهِ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (14:40) [listed for 87:1] رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ
- (16:3) [listed for 87:1] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ تَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (16:57) [listed for 87:1] وَيَجْعَلُونَ لِلَّهِ ٱلْبَنَٰتِ سُبْحَٰنَهُۥ ۙ وَلَهُم مَّا يَشْتَهُونَ
- (16:60) [listed for 87:1] لِلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ مَثَلُ ٱلسَّوْءِ ۖ وَلِلَّهِ ٱلْمَثَلُ ٱلْأَعْلَىٰ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (17:44) [listed for 87:1] [cited in ¶6] تُسَبِّحُ لَهُ ٱلسَّمَٰوَٰتُ ٱلسَّبْعُ وَٱلْأَرْضُ وَمَن فِيهِنَّ ۚ وَإِن مِّن شَىْءٍ إِلَّا يُسَبِّحُ بِحَمْدِهِۦ وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ ۗ إِنَّهُۥ كَانَ حَلِيمًا غَفُورًۭا
- (18:27) [listed for 87:1] وَٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِن كِتَابِ رَبِّكَ ۖ لَا مُبَدِّلَ لِكَلِمَٰتِهِۦ وَلَن تَجِدَ مِن دُونِهِۦ مُلْتَحَدًۭا
- (20:4) [listed for 87:1] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:14) [listed for 87:1] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:68) [listed for 87:1] [cited in ¶20] قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ
- (21:22) [listed for 87:1] لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا ۚ فَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَرْشِ عَمَّا يَصِفُونَ
- (22:1) [listed for 87:1] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمْ ۚ إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌۭ
- (22:34) [listed for 87:1] وَلِكُلِّ أُمَّةٍۢ جَعَلْنَا مَنسَكًۭا لِّيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۗ فَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَلَهُۥٓ أَسْلِمُوا۟ ۗ وَبَشِّرِ ٱلْمُخْبِتِينَ
- (22:62) [listed for 87:1] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّ مَا يَدْعُونَ مِن دُونِهِۦ هُوَ ٱلْبَٰطِلُ وَأَنَّ ٱللَّهَ هُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ
- (23:14) [listed for 87:1] ثُمَّ خَلَقْنَا ٱلنُّطْفَةَ عَلَقَةًۭ فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةًۭ فَخَلَقْنَا ٱلْمُضْغَةَ عِظَٰمًۭا فَكَسَوْنَا ٱلْعِظَٰمَ لَحْمًۭا ثُمَّ أَنشَأْنَٰهُ خَلْقًا ءَاخَرَ ۚ فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ
- (23:116) [listed for 87:1] فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۖ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْكَرِيمِ
- (24:36) [listed for 87:1] فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ
- (27:31) [listed for 87:1] أَلَّا تَعْلُوا۟ عَلَىَّ وَأْتُونِى مُسْلِمِينَ
- (28:68) [listed for 87:1] وَرَبُّكَ يَخْلُقُ مَا يَشَآءُ وَيَخْتَارُ ۗ مَا كَانَ لَهُمُ ٱلْخِيَرَةُ ۚ سُبْحَٰنَ ٱللَّهِ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (30:27) [listed for 87:1] وَهُوَ ٱلَّذِى يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ وَهُوَ أَهْوَنُ عَلَيْهِ ۚ وَلَهُ ٱلْمَثَلُ ٱلْأَعْلَىٰ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (37:5) [listed for 87:1] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا وَرَبُّ ٱلْمَشَٰرِقِ
- (37:159) [listed for 87:1] سُبْحَٰنَ ٱللَّهِ عَمَّا يَصِفُونَ
- (37:166) [listed for 87:1] وَإِنَّا لَنَحْنُ ٱلْمُسَبِّحُونَ
- (38:75) [listed for 87:1] قَالَ يَٰٓإِبْلِيسُ مَا مَنَعَكَ أَن تَسْجُدَ لِمَا خَلَقْتُ بِيَدَىَّ ۖ أَسْتَكْبَرْتَ أَمْ كُنتَ مِنَ ٱلْعَالِينَ
- (39:67) [listed for 87:1] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦ وَٱلْأَرْضُ جَمِيعًۭا قَبْضَتُهُۥ يَوْمَ ٱلْقِيَٰمَةِ وَٱلسَّمَٰوَٰتُ مَطْوِيَّٰتٌۢ بِيَمِينِهِۦ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (42:4) [listed for 87:1] لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (43:13) [listed for 87:1] لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقْرِنِينَ
- (44:6) [listed for 87:1] رَحْمَةًۭ مِّن رَّبِّكَ ۚ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (44:12) [listed for 87:1] رَّبَّنَا ٱكْشِفْ عَنَّا ٱلْعَذَابَ إِنَّا مُؤْمِنُونَ
- (45:36) [listed for 87:1] فَلِلَّهِ ٱلْحَمْدُ رَبِّ ٱلسَّمَٰوَٰتِ وَرَبِّ ٱلْأَرْضِ رَبِّ ٱلْعَٰلَمِينَ
- (53:7) [listed for 87:1] [cited in ¶11] وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ
- (53:49) [listed for 87:1] وَأَنَّهُۥ هُوَ رَبُّ ٱلشِّعْرَىٰ
- (56:96) [listed for 87:1] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (57:1) [listed for 87:1] سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (59:1) [listed for 87:1] سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (61:1) [listed for 87:1] سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (62:1) [listed for 87:1] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ٱلْمَلِكِ ٱلْقُدُّوسِ ٱلْعَزِيزِ ٱلْحَكِيمِ
- (64:1) [listed for 87:1] يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ لَهُ ٱلْمُلْكُ وَلَهُ ٱلْحَمْدُ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (68:7) [listed for 87:1] إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- (72:3) [listed for 87:1] وَأَنَّهُۥ تَعَٰلَىٰ جَدُّ رَبِّنَا مَا ٱتَّخَذَ صَٰحِبَةًۭ وَلَا وَلَدًۭا
- (73:8) [listed for 87:1] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
- (73:9) [listed for 87:1] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (76:26) [listed for 87:1] [cited in ¶7] وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا
- (88:10) [listed for 87:1] فِى جَنَّةٍ عَالِيَةٍۢ
- (89:14) [listed for 87:1] إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- (100:6) [listed for 87:1] إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- (100:11) [listed for 87:1] إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ
- (105:1) [listed for 87:1] أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ
- (106:3) [listed for 87:1] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ

## named by the passage's own list as strong for this ayah (4)

- (7:185) [listed for 87:1] أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا خَلَقَ ٱللَّهُ مِن شَىْءٍۢ وَأَنْ عَسَىٰٓ أَن يَكُونَ قَدِ ٱقْتَرَبَ أَجَلُهُمْ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ
- (74:3) [listed for 87:1] وَرَبَّكَ فَكَبِّرْ
- (79:3) [listed for 87:1] وَٱلسَّٰبِحَٰتِ سَبْحًۭا
- (85:1) [listed for 87:1] وَٱلسَّمَآءِ ذَاتِ ٱلْبُرُوجِ

## named by the passage's own list as medium for this ayah (26)

- (2:32) [listed for 87:1] [cited in ¶25] قَالُوا۟ سُبْحَٰنَكَ لَا عِلْمَ لَنَآ إِلَّا مَا عَلَّمْتَنَآ ۖ إِنَّكَ أَنتَ ٱلْعَلِيمُ ٱلْحَكِيمُ
- (3:41) [listed for 87:1] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۖ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَةَ أَيَّامٍ إِلَّا رَمْزًۭا ۗ وَٱذْكُر رَّبَّكَ كَثِيرًۭا وَسَبِّحْ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
- (7:206) [listed for 87:1] إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ وَيُسَبِّحُونَهُۥ وَلَهُۥ يَسْجُدُونَ ۩
- (16:1) [listed for 87:1] أَتَىٰٓ أَمْرُ ٱللَّهِ فَلَا تَسْتَعْجِلُوهُ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (17:108) [listed for 87:1] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
- (19:11) [listed for 87:1] فَخَرَجَ عَلَىٰ قَوْمِهِۦ مِنَ ٱلْمِحْرَابِ فَأَوْحَىٰٓ إِلَيْهِمْ أَن سَبِّحُوا۟ بُكْرَةًۭ وَعَشِيًّۭا
- (20:33) [listed for 87:1] كَىْ نُسَبِّحَكَ كَثِيرًۭا
- (21:20) [listed for 87:1] يُسَبِّحُونَ ٱلَّيْلَ وَٱلنَّهَارَ لَا يَفْتُرُونَ
- (21:33) [listed for 87:1] [cited in ¶6] وَهُوَ ٱلَّذِى خَلَقَ ٱلَّيْلَ وَٱلنَّهَارَ وَٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ
- (27:8) [listed for 87:1] فَلَمَّا جَآءَهَا نُودِىَ أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (31:30) [listed for 87:1] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّ مَا يَدْعُونَ مِن دُونِهِ ٱلْبَٰطِلُ وَأَنَّ ٱللَّهَ هُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ
- (33:42) [listed for 87:1] وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا
- (36:83) [listed for 87:1] فَسُبْحَٰنَ ٱلَّذِى بِيَدِهِۦ مَلَكُوتُ كُلِّ شَىْءٍۢ وَإِلَيْهِ تُرْجَعُونَ
- (41:38) [listed for 87:1] فَإِنِ ٱسْتَكْبَرُوا۟ فَٱلَّذِينَ عِندَ رَبِّكَ يُسَبِّحُونَ لَهُۥ بِٱلَّيْلِ وَٱلنَّهَارِ وَهُمْ لَا يَسْـَٔمُونَ ۩
- (45:4) [listed for 87:1] وَفِى خَلْقِكُمْ وَمَا يَبُثُّ مِن دَآبَّةٍ ءَايَٰتٌۭ لِّقَوْمٍۢ يُوقِنُونَ
- (45:13) [listed for 87:1] وَسَخَّرَ لَكُم مَّا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ جَمِيعًۭا مِّنْهُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (52:43) [listed for 87:1] أَمْ لَهُمْ إِلَٰهٌ غَيْرُ ٱللَّهِ ۚ سُبْحَٰنَ ٱللَّهِ عَمَّا يُشْرِكُونَ
- (52:49) [listed for 87:1] وَمِنَ ٱلَّيْلِ فَسَبِّحْهُ وَإِدْبَٰرَ ٱلنُّجُومِ
- (55:17) [listed for 87:1] رَبُّ ٱلْمَشْرِقَيْنِ وَرَبُّ ٱلْمَغْرِبَيْنِ
- (55:51) [listed for 87:1] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (68:2) [listed for 87:1] مَآ أَنتَ بِنِعْمَةِ رَبِّكَ بِمَجْنُونٍۢ
- (68:28) [listed for 87:1] قَالَ أَوْسَطُهُمْ أَلَمْ أَقُل لَّكُمْ لَوْلَا تُسَبِّحُونَ
- (74:34) [listed for 87:1] وَٱلصُّبْحِ إِذَآ أَسْفَرَ
- (79:16) [listed for 87:1] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- (83:19) [listed for 87:1] وَمَآ أَدْرَىٰكَ مَا عِلِّيُّونَ
- (96:3) [listed for 87:1] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ

## weak (this ayah's own list) (17)

- (2:30) [listed for 87:1] [cited in ¶25] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى جَاعِلٌۭ فِى ٱلْأَرْضِ خَلِيفَةًۭ ۖ قَالُوٓا۟ أَتَجْعَلُ فِيهَا مَن يُفْسِدُ فِيهَا وَيَسْفِكُ ٱلدِّمَآءَ وَنَحْنُ نُسَبِّحُ بِحَمْدِكَ وَنُقَدِّسُ لَكَ ۖ قَالَ إِنِّىٓ أَعْلَمُ مَا لَا تَعْلَمُونَ
- (6:119) [listed for 87:1] وَمَا لَكُمْ أَلَّا تَأْكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ وَقَدْ فَصَّلَ لَكُم مَّا حَرَّمَ عَلَيْكُمْ إِلَّا مَا ٱضْطُرِرْتُمْ إِلَيْهِ ۗ وَإِنَّ كَثِيرًۭا لَّيُضِلُّونَ بِأَهْوَآئِهِم بِغَيْرِ عِلْمٍ ۗ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِٱلْمُعْتَدِينَ
- (7:122) [listed for 87:1] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (10:85) [listed for 87:1] فَقَالُوا۟ عَلَى ٱللَّهِ تَوَكَّلْنَا رَبَّنَا لَا تَجْعَلْنَا فِتْنَةًۭ لِّلْقَوْمِ ٱلظَّٰلِمِينَ
- (20:49) [listed for 87:1] قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ
- (22:28) [listed for 87:1] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:36) [listed for 87:1] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (22:40) [listed for 87:1] ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِم بِغَيْرِ حَقٍّ إِلَّآ أَن يَقُولُوا۟ رَبُّنَا ٱللَّهُ ۗ وَلَوْلَا دَفْعُ ٱللَّهِ ٱلنَّاسَ بَعْضَهُم بِبَعْضٍۢ لَّهُدِّمَتْ صَوَٰمِعُ وَبِيَعٌۭ وَصَلَوَٰتٌۭ وَمَسَٰجِدُ يُذْكَرُ فِيهَا ٱسْمُ ٱللَّهِ كَثِيرًۭا ۗ وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ
- (26:48) [listed for 87:1] رَبِّ مُوسَىٰ وَهَٰرُونَ
- (36:27) [listed for 87:1] بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ
- (37:8) [listed for 87:1] لَّا يَسَّمَّعُونَ إِلَى ٱلْمَلَإِ ٱلْأَعْلَىٰ وَيُقْذَفُونَ مِن كُلِّ جَانِبٍۢ
- (38:69) [listed for 87:1] مَا كَانَ لِىَ مِنْ عِلْمٍۭ بِٱلْمَلَإِ ٱلْأَعْلَىٰٓ إِذْ يَخْتَصِمُونَ
- (46:13) [listed for 87:1] إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (49:11) [listed for 87:1] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا يَسْخَرْ قَوْمٌۭ مِّن قَوْمٍ عَسَىٰٓ أَن يَكُونُوا۟ خَيْرًۭا مِّنْهُمْ وَلَا نِسَآءٌۭ مِّن نِّسَآءٍ عَسَىٰٓ أَن يَكُنَّ خَيْرًۭا مِّنْهُنَّ ۖ وَلَا تَلْمِزُوٓا۟ أَنفُسَكُمْ وَلَا تَنَابَزُوا۟ بِٱلْأَلْقَٰبِ ۖ بِئْسَ ٱلِٱسْمُ ٱلْفُسُوقُ بَعْدَ ٱلْإِيمَٰنِ ۚ وَمَن لَّمْ يَتُبْ فَأُو۟لَٰٓئِكَ هُمُ ٱلظَّٰلِمُونَ
- (55:69) [listed for 87:1] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (82:1) [listed for 87:1] إِذَا ٱلسَّمَآءُ ٱنفَطَرَتْ
- (110:1) [listed for 87:1] إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ

## named by the passage's own list as weak for this ayah (29)

- (2:33) [listed for 87:1] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
- (2:116) [listed for 87:1] وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ ۖ بَل لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ كُلٌّۭ لَّهُۥ قَٰنِتُونَ
- (2:255) [listed for 87:1] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (4:171) [listed for 87:1] يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ وَلَا تَقُولُوا۟ عَلَى ٱللَّهِ إِلَّا ٱلْحَقَّ ۚ إِنَّمَا ٱلْمَسِيحُ عِيسَى ٱبْنُ مَرْيَمَ رَسُولُ ٱللَّهِ وَكَلِمَتُهُۥٓ أَلْقَىٰهَآ إِلَىٰ مَرْيَمَ وَرُوحٌۭ مِّنْهُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرُسُلِهِۦ ۖ وَلَا تَقُولُوا۟ ثَلَٰثَةٌ ۚ ٱنتَهُوا۟ خَيْرًۭا لَّكُمْ ۚ إِنَّمَا ٱللَّهُ إِلَٰهٌۭ وَٰحِدٌۭ ۖ سُبْحَٰنَهُۥٓ أَن يَكُونَ لَهُۥ وَلَدٌۭ ۘ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَكَفَىٰ بِٱللَّهِ وَكِيلًۭا
- (7:190) [listed for 87:1] فَلَمَّآ ءَاتَىٰهُمَا صَٰلِحًۭا جَعَلَا لَهُۥ شُرَكَآءَ فِيمَآ ءَاتَىٰهُمَا ۚ فَتَعَٰلَى ٱللَّهُ عَمَّا يُشْرِكُونَ
- (9:31) [listed for 87:1] ٱتَّخَذُوٓا۟ أَحْبَارَهُمْ وَرُهْبَٰنَهُمْ أَرْبَابًۭا مِّن دُونِ ٱللَّهِ وَٱلْمَسِيحَ ٱبْنَ مَرْيَمَ وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ۚ سُبْحَٰنَهُۥ عَمَّا يُشْرِكُونَ
- (10:18) [listed for 87:1] وَيَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَضُرُّهُمْ وَلَا يَنفَعُهُمْ وَيَقُولُونَ هَٰٓؤُلَآءِ شُفَعَٰٓؤُنَا عِندَ ٱللَّهِ ۚ قُلْ أَتُنَبِّـُٔونَ ٱللَّهَ بِمَا لَا يَعْلَمُ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (19:57) [listed for 87:1] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- (23:46) [listed for 87:1] إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَٱسْتَكْبَرُوا۟ وَكَانُوا۟ قَوْمًا عَالِينَ
- (23:58) [listed for 87:1] وَٱلَّذِينَ هُم بِـَٔايَٰتِ رَبِّهِمْ يُؤْمِنُونَ
- (23:72) [listed for 87:1] أَمْ تَسْـَٔلُهُمْ خَرْجًۭا فَخَرَاجُ رَبِّكَ خَيْرٌۭ ۖ وَهُوَ خَيْرُ ٱلرَّٰزِقِينَ
- (23:92) [listed for 87:1] عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (24:16) [listed for 87:1] وَلَوْلَآ إِذْ سَمِعْتُمُوهُ قُلْتُم مَّا يَكُونُ لَنَآ أَن نَّتَكَلَّمَ بِهَٰذَا سُبْحَٰنَكَ هَٰذَا بُهْتَٰنٌ عَظِيمٌۭ
- (30:18) [listed for 87:1] وَلَهُ ٱلْحَمْدُ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَعَشِيًّۭا وَحِينَ تُظْهِرُونَ
- (30:40) [listed for 87:1] ٱللَّهُ ٱلَّذِى خَلَقَكُمْ ثُمَّ رَزَقَكُمْ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ۖ هَلْ مِن شُرَكَآئِكُم مَّن يَفْعَلُ مِن ذَٰلِكُم مِّن شَىْءٍۢ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (34:41) [listed for 87:1] قَالُوا۟ سُبْحَٰنَكَ أَنتَ وَلِيُّنَا مِن دُونِهِم ۖ بَلْ كَانُوا۟ يَعْبُدُونَ ٱلْجِنَّ ۖ أَكْثَرُهُم بِهِم مُّؤْمِنُونَ
- (37:1) [listed for 87:1] وَٱلصَّٰٓفَّٰتِ صَفًّۭا
- (39:4) [listed for 87:1] لَّوْ أَرَادَ ٱللَّهُ أَن يَتَّخِذَ وَلَدًۭا لَّٱصْطَفَىٰ مِمَّا يَخْلُقُ مَا يَشَآءُ ۚ سُبْحَٰنَهُۥ ۖ هُوَ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
- (44:19) [listed for 87:1] وَأَن لَّا تَعْلُوا۟ عَلَى ٱللَّهِ ۖ إِنِّىٓ ءَاتِيكُم بِسُلْطَٰنٍۢ مُّبِينٍۢ
- (44:31) [listed for 87:1] مِن فِرْعَوْنَ ۚ إِنَّهُۥ كَانَ عَالِيًۭا مِّنَ ٱلْمُسْرِفِينَ
- (50:40) [listed for 87:1] وَمِنَ ٱلَّيْلِ فَسَبِّحْهُ وَأَدْبَٰرَ ٱلسُّجُودِ
- (69:22) [listed for 87:1] فِى جَنَّةٍ عَالِيَةٍۢ
- (71:5) [listed for 87:1] قَالَ رَبِّ إِنِّى دَعَوْتُ قَوْمِى لَيْلًۭا وَنَهَارًۭا
- (73:7) [listed for 87:1] [cited in ¶7] إِنَّ لَكَ فِى ٱلنَّهَارِ سَبْحًۭا طَوِيلًۭا
- (76:21) [listed for 87:1] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (83:18) [listed for 87:1] كَلَّآ إِنَّ كِتَٰبَ ٱلْأَبْرَارِ لَفِى عِلِّيِّينَ
- (85:15) [listed for 87:1] ذُو ٱلْعَرْشِ ٱلْمَجِيدُ
- (91:5) [listed for 87:1] وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- (99:5) [listed for 87:1] بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا

## neighbours: within two ayat of a passage the commentary cites (82)

- (1:3) [next to 1:1] ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (1:4) [next to 1:2] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (2:28) [next to 2:30] كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ
- (2:29) [next to 2:30] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (2:34) [next to 2:32] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ وَٱسْتَكْبَرَ وَكَانَ مِنَ ٱلْكَٰفِرِينَ
- (3:62) [next to 3:64] إِنَّ هَٰذَا لَهُوَ ٱلْقَصَصُ ٱلْحَقُّ ۚ وَمَا مِنْ إِلَٰهٍ إِلَّا ٱللَّهُ ۚ وَإِنَّ ٱللَّهَ لَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (3:63) [next to 3:64] فَإِن تَوَلَّوْا۟ فَإِنَّ ٱللَّهَ عَلِيمٌۢ بِٱلْمُفْسِدِينَ
- (3:65) [next to 3:64] يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تُحَآجُّونَ فِىٓ إِبْرَٰهِيمَ وَمَآ أُنزِلَتِ ٱلتَّوْرَىٰةُ وَٱلْإِنجِيلُ إِلَّا مِنۢ بَعْدِهِۦٓ ۚ أَفَلَا تَعْقِلُونَ
- (3:66) [next to 3:64] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ حَٰجَجْتُمْ فِيمَا لَكُم بِهِۦ عِلْمٌۭ فَلِمَ تُحَآجُّونَ فِيمَا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ ۚ وَٱللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ
- (7:178) [next to 7:180] مَن يَهْدِ ٱللَّهُ فَهُوَ ٱلْمُهْتَدِى ۖ وَمَن يُضْلِلْ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (7:179) [next to 7:180] وَلَقَدْ ذَرَأْنَا لِجَهَنَّمَ كَثِيرًۭا مِّنَ ٱلْجِنِّ وَٱلْإِنسِ ۖ لَهُمْ قُلُوبٌۭ لَّا يَفْقَهُونَ بِهَا وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا وَلَهُمْ ءَاذَانٌۭ لَّا يَسْمَعُونَ بِهَآ ۚ أُو۟لَٰٓئِكَ كَٱلْأَنْعَٰمِ بَلْ هُمْ أَضَلُّ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْغَٰفِلُونَ
- (7:181) [next to 7:180] وَمِمَّنْ خَلَقْنَآ أُمَّةٌۭ يَهْدُونَ بِٱلْحَقِّ وَبِهِۦ يَعْدِلُونَ
- (7:182) [next to 7:180] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ
- (17:42) [next to 17:44] قُل لَّوْ كَانَ مَعَهُۥٓ ءَالِهَةٌۭ كَمَا يَقُولُونَ إِذًۭا لَّٱبْتَغَوْا۟ إِلَىٰ ذِى ٱلْعَرْشِ سَبِيلًۭا
- (17:45) [next to 17:44] وَإِذَا قَرَأْتَ ٱلْقُرْءَانَ جَعَلْنَا بَيْنَكَ وَبَيْنَ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ حِجَابًۭا مَّسْتُورًۭا
- (17:46) [next to 17:44] وَجَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۚ وَإِذَا ذَكَرْتَ رَبَّكَ فِى ٱلْقُرْءَانِ وَحْدَهُۥ وَلَّوْا۟ عَلَىٰٓ أَدْبَٰرِهِمْ نُفُورًۭا
- (19:5) [next to 19:7] وَإِنِّى خِفْتُ ٱلْمَوَٰلِىَ مِن وَرَآءِى وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا
- (19:6) [next to 19:7] يَرِثُنِى وَيَرِثُ مِنْ ءَالِ يَعْقُوبَ ۖ وَٱجْعَلْهُ رَبِّ رَضِيًّۭا
- (19:8) [next to 19:7] قَالَ رَبِّ أَنَّىٰ يَكُونُ لِى غُلَٰمٌۭ وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا وَقَدْ بَلَغْتُ مِنَ ٱلْكِبَرِ عِتِيًّۭا
- (19:9) [next to 19:7] قَالَ كَذَٰلِكَ قَالَ رَبُّكَ هُوَ عَلَىَّ هَيِّنٌۭ وَقَدْ خَلَقْتُكَ مِن قَبْلُ وَلَمْ تَكُ شَيْـًۭٔا
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (19:67) [next to 19:65] أَوَلَا يَذْكُرُ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن قَبْلُ وَلَمْ يَكُ شَيْـًۭٔا
- (20:66) [next to 20:68] قَالَ بَلْ أَلْقُوا۟ ۖ فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ أَنَّهَا تَسْعَىٰ
- (20:67) [next to 20:68] فَأَوْجَسَ فِى نَفْسِهِۦ خِيفَةًۭ مُّوسَىٰ
- (20:70) [next to 20:68] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (20:71) [next to 20:69] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (21:30) [next to 21:32] أَوَلَمْ يَرَ ٱلَّذِينَ كَفَرُوٓا۟ أَنَّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ كَانَتَا رَتْقًۭا فَفَتَقْنَٰهُمَا ۖ وَجَعَلْنَا مِنَ ٱلْمَآءِ كُلَّ شَىْءٍ حَىٍّ ۖ أَفَلَا يُؤْمِنُونَ
- (21:31) [next to 21:32] وَجَعَلْنَا فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِهِمْ وَجَعَلْنَا فِيهَا فِجَاجًۭا سُبُلًۭا لَّعَلَّهُمْ يَهْتَدُونَ
- (21:34) [next to 21:32] وَمَا جَعَلْنَا لِبَشَرٍۢ مِّن قَبْلِكَ ٱلْخُلْدَ ۖ أَفَإِي۟ن مِّتَّ فَهُمُ ٱلْخَٰلِدُونَ
- (21:35) [next to 21:33] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ ۖ وَإِلَيْنَا تُرْجَعُونَ
- (21:85) [next to 21:87] وَإِسْمَٰعِيلَ وَإِدْرِيسَ وَذَا ٱلْكِفْلِ ۖ كُلٌّۭ مِّنَ ٱلصَّٰبِرِينَ
- (21:86) [next to 21:87] وَأَدْخَلْنَٰهُمْ فِى رَحْمَتِنَآ ۖ إِنَّهُم مِّنَ ٱلصَّٰلِحِينَ
- (21:88) [next to 21:87] فَٱسْتَجَبْنَا لَهُۥ وَنَجَّيْنَٰهُ مِنَ ٱلْغَمِّ ۚ وَكَذَٰلِكَ نُۨجِى ٱلْمُؤْمِنِينَ
- (21:89) [next to 21:87] وَزَكَرِيَّآ إِذْ نَادَىٰ رَبَّهُۥ رَبِّ لَا تَذَرْنِى فَرْدًۭا وَأَنتَ خَيْرُ ٱلْوَٰرِثِينَ
- (37:138) [next to 37:140] وَبِٱلَّيْلِ ۗ أَفَلَا تَعْقِلُونَ
- (37:139) [next to 37:140] وَإِنَّ يُونُسَ لَمِنَ ٱلْمُرْسَلِينَ
- (37:145) [next to 37:143] ۞ فَنَبَذْنَٰهُ بِٱلْعَرَآءِ وَهُوَ سَقِيمٌۭ
- (37:146) [next to 37:144] وَأَنۢبَتْنَا عَلَيْهِ شَجَرَةًۭ مِّن يَقْطِينٍۢ
- (53:3) [next to 53:5] وَمَا يَنطِقُ عَنِ ٱلْهَوَىٰٓ
- (53:4) [next to 53:5] إِنْ هُوَ إِلَّا وَحْىٌۭ يُوحَىٰ
- (53:6) [next to 53:5] ذُو مِرَّةٍۢ فَٱسْتَوَىٰ
- (53:8) [next to 53:7] ثُمَّ دَنَا فَتَدَلَّىٰ
- (53:9) [next to 53:7] فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ
- (53:21) [next to 53:23] أَلَكُمُ ٱلذَّكَرُ وَلَهُ ٱلْأُنثَىٰ
- (53:22) [next to 53:23] تِلْكَ إِذًۭا قِسْمَةٌۭ ضِيزَىٰٓ
- (53:24) [next to 53:23] أَمْ لِلْإِنسَٰنِ مَا تَمَنَّىٰ
- (53:25) [next to 53:23] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (55:25) [next to 55:27] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:26) [next to 55:27] كُلُّ مَنْ عَلَيْهَا فَانٍۢ
- (55:28) [next to 55:27] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:29) [next to 55:27] يَسْـَٔلُهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ كُلَّ يَوْمٍ هُوَ فِى شَأْنٍۢ
- (55:76) [next to 55:78] مُتَّكِـِٔينَ عَلَىٰ رَفْرَفٍ خُضْرٍۢ وَعَبْقَرِىٍّ حِسَانٍۢ
- (55:77) [next to 55:78] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (56:72) [next to 56:74] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
- (56:73) [next to 56:74] نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ
- (56:75) [next to 56:74] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (56:76) [next to 56:74] وَإِنَّهُۥ لَقَسَمٌۭ لَّوْ تَعْلَمُونَ عَظِيمٌ
- (59:22) [next to 59:24] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (73:0) [next to 73:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (73:1) [next to 73:2] يَٰٓأَيُّهَا ٱلْمُزَّمِّلُ
- (73:3) [next to 73:2] نِّصْفَهُۥٓ أَوِ ٱنقُصْ مِنْهُ قَلِيلًا
- (73:4) [next to 73:2] أَوْ زِدْ عَلَيْهِ وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا
- (73:5) [next to 73:7] إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًۭا ثَقِيلًا
- (73:6) [next to 73:7] إِنَّ نَاشِئَةَ ٱلَّيْلِ هِىَ أَشَدُّ وَطْـًۭٔا وَأَقْوَمُ قِيلًا
- (76:23) [next to 76:25] إِنَّا نَحْنُ نَزَّلْنَا عَلَيْكَ ٱلْقُرْءَانَ تَنزِيلًۭا
- (76:24) [next to 76:25] فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًۭا
- (76:27) [next to 76:25] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
- (76:28) [next to 76:26] نَّحْنُ خَلَقْنَٰهُمْ وَشَدَدْنَآ أَسْرَهُمْ ۖ وَإِذَا شِئْنَا بَدَّلْنَآ أَمْثَٰلَهُمْ تَبْدِيلًا
- (79:15) [next to 79:17] هَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (79:18) [next to 79:17] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
- (79:19) [next to 79:17] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- (79:21) [next to 79:23] فَكَذَّبَ وَعَصَىٰ
- (79:22) [next to 79:23] ثُمَّ أَدْبَرَ يَسْعَىٰ
- (79:25) [next to 79:23] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- (79:26) [next to 79:24] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (92:18) [next to 92:20] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- (92:19) [next to 92:20] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- (92:21) [next to 92:20] وَلَسَوْفَ يَرْضَىٰ
- (96:0) [next to 96:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (96:2) [next to 96:1] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ

