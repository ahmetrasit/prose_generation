Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:15; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_15/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_15.reading.tr.md (prose paragraphs numbered) =====
## Birinci ayetin emri, bir insanın işi olarak

[¶1] Bu ayet tek başına bir cümle değildir. On dördüncü ayetin devamıdır ve onunla birlikte okunur: {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kişi kurtuluşa ermiştir, source:87:14}, ve o kişi {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını andı, ardından namaz kıldı, source:87:15}. Üç fiilin öznesi aynı kişidir ve üçü de geçmiş kiptedir: arındı, andı, kıldı. Kurtuluş da "kad" ile pekiştirilmiş geçmiş kipte söylenir, sonucu kesinleşmiş bir şey gibi. Ayet emir vermez. Bir insanı yaptıklarıyla tanıtır. Bağlaçlar da işi bölüştürür. "Ve" anmayı arınmanın yanına ekler. "Fe" ise namazı anmanın hemen ardına koyar, hem sonraki adım hem de onun sonucu olarak. Ağızda anılan ad, araya zaman girmeden bedenin işine dönüşür.

[¶2] Bu kişinin yaptığı iş surenin ilk cümlesinden tanıdıktır. Sure {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1} emriyle açılmıştı. "Ad" ve "Rab" kelimeleri on beşinci ayette aynı sırayla geri gelir. Ama emir kipi geçmiş kipe, "sen" hitabı "o"ya dönmüştür. "Rabbin" artık "Rabbi" olmuştur. Birinci ayette elçiye söylenen söz, burada bir insanın yapıp bitirdiği iştir. Emir hedefini bulmuş, bir hayatta yerine gelmiştir. Fiil de değişir: emir "tesbih et" der, gerçekleşen iş "andı ve namaz kıldı" olur. Bu ikisinin arasında dokuzuncu ve onuncu ayetlerin öğüdü durur. Emir bir hatırlatma olarak dolaşmış ve bir insanda anmaya dönüşmüştür.

[¶3] Ayetin yeri de anlamına katılır. Hemen öncesinde öğütten kaçınan en bedbaht kişi {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yasle'n-nâra'l-kubrâ, gloss:en büyük ateşe girecek olan, source:87:12} diye tanıtılmış, orada ne öldüğü ne yaşadığı söylenmiştir. Hemen sonrasında hitap "siz"e döner: {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır, siz dünya hayatını öne alıyorsunuz, source:87:16}. Namaz kılan kişi iki uyarının arasında duran tek olumlu portredir. Surenin bütün ayetleri uzun bir "â" sesiyle biter. "Sallâ" da bu sesle kapanır ve kulak onu üç ayet önceki "yaslâ" ile birlikte duyar.

## Anmak: unutmanın karşısında

[¶4] Türkçede "zikir" denince çoğu zaman bir adın belli bir sayıyla, toplu hâlde ve sesle tekrarlanması akla gelir. Arapçada ẕikr çok daha geniş bir alanı kaplar ve en sade hâliyle unutmanın karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hılâfu nesîtuh, gloss:bir şeyi andım, yani unutmadım, source:"ذ ك ر,B003"}. Bir şeyi aklında tutup korumak da aynı kelimeyle söylenir: {ar:الذكر الحفظ للشيء, tr:eẕ-ẕikru'l-hıfzu li'ş-şey', gloss:zikir bir şeyi korumak, aklında saklamaktır, source:"ذ ك ر,B003"}. Bu yüzden ayetin fiili önce şunu söyler: bu kişi Rabbinin adını unutmadı, onu sakladı ve diri tuttu.

[¶5] Unutma ile anma surede bir zincir kurar. Altıncı ayette elçiye bir söz verilir: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukri'uke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}. Unutmayan elçiye dokuzuncu ayette {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver, eğer öğüt yarar sağlarsa, source:87:9} denir. "Ẕekkir" aynı fiilin ettirgen biçimidir, yani "hatırlat, andır" demektir. Ẕikrâ da {ar:الذكرى اسم للتذكير, tr:eẕ-ẕikrâ ismun li't-teẕkîr, gloss:zikrâ hatırlatmanın adıdır, source:"ذ ك ر,B009"}. Onuncu ayette hatırlatılanı alan kişi gelir: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}. Buradaki biçim bir çaba bildirir, kişinin hatırlayışı kendi içinde araması gibi: {ar:التذكر طلب ما فات, tr:et-teẕekkur talebu mâ fât, gloss:tezekkür elden kaçanı aramaktır, source:"ذ ك ر,B003"}. Zincir on beşinci ayette fiilin en yalın biçimiyle tamamlanır: ẕekera, yani andı. Elçiye verilen unutmazlık onun hatırlatmasıyla dinleyenin anışına geçmiştir. On birinci ayette öğütten kaçınan kişide ise aynı zincir kopar.

[¶6] Burada anılan şey bir addır ve ad dilde söylenir. Anmayı {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikru cerayu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinde akıp gitmesidir, source:"ذ ك ر,B004"} diye tarif ederlerdi. Ama aynı fiil kalbe de uzanır: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle de kalbimle de andım, source:"ذ ك ر,B004"}. Yedinci ayetin {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} sözü, dilde sesi yükselen anmayı da kalpte saklı kalan anmayı da kapsar. Anma ibadetin kendisi de sayılır: {ar:الذكر الصلاة والدعاء والثناء, tr:eẕ-ẕikru's-salâtu ve'd-duâu ve's-senâ, gloss:zikir namaz, dua ve övgüdür, source:"ذ ك ر,B005"}. Bu kullanım ayetin iki fiilini birbirine yaklaştırır. "Andı" ile "kıldı" iki ayrı iş olduğu kadar tek bir yönelişin iki adımıdır.

[¶7] Bu ayetteki fiil, Kur'an'da elçiye emir olarak da söylenir. Müzzemmil suresinde elçiye gecenin azı dışında kalkması söylenir {source:73:2}, Kur'an'ı ağır ağır okuması istenir ve şu eklenir: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا, tr:veẕkuri'sme rabbike ve tebettel ileyhi tebtîlâ, gloss:Rabbinin adını an ve her şeyden sıyrılıp bütünüyle O'na yönel, source:73:8}. İnsan suresinde Allah, Kur'an'ı ona parça parça indirdiğini söyler {source:76:23}, sabretmesini ve günaha dalanla nankörün sözüne uymamasını ister. Sonra şöyle buyurur: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا, tr:veẕkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا, tr:ve mine'l-leyli fescud lehû ve sebbihhu leylen tavîlâ, gloss:gecenin bir kısmında O'na secde et ve uzun gece boyunca O'nu tesbih et, source:76:26}. Orada da sıra aynıdır: önce ad anılır, ardından beden secdeye iner ve tesbih gelir. Elçiye emir olarak verilen iş, bu surede bir insanın geçmişte yaptığı iş olarak anlatılır.

[¶8] Ẕikr, peygamberlere indirilen kitabın da adıdır: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîni ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntısını taşıyan kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Kur'an kendini de böyle anar. Elçiyle alay edenler ona {ar:يَٰٓأَيُّهَا ٱلَّذِى نُزِّلَ عَلَيْهِ ٱلذِّكْرُ إِنَّكَ لَمَجْنُونٌۭ, tr:yâ eyyuhe'lleẕî nuzzile aleyhi'ẕ-ẕikru inneke le-mecnûn, gloss:ey kendisine zikir indirilen, sen kesinlikle delisin, source:15:6} derler. Birkaç ayet sonra Allah şöyle der: {ar:إِنَّا نَحْنُ نَزَّلْنَا ٱلذِّكْرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ, tr:innâ nahnu nezzelne'ẕ-ẕikra ve innâ lehû le-hâfizûn, gloss:zikri biz indirdik, onu koruyan da biziz, source:15:9}. Zikri yukarıda Allah korur, aşağıda onu anan insan saklar. Surenin sonunda söylenenlerin {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi ibrâhîme ve mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19} içinde de bulunduğu bildirilir. Son ayetin adını verdiği Musa'ya ateşin başında söylenen söz bu ayetin iki kelimesini ters sırayla taşır: {ar:فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:fa'budnî ve ekımi's-salâte li-ẕikrî, gloss:bana kulluk et ve beni anmak için namazı kıl, source:20:14}. Bu surede anma namaza götürür, Musa'ya verilen emirde ise namaz anmaya. İki sıra birlikte bir çember çizer.

## Ad: yükselen ve tanıtan

[¶9] Türkçede "isim" bir etiket ya da dilbilgisinde bir sözcük türüdür. Arapçada ism kelimesi yükseklik bildiren bir kökten gelir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-uluvvi li-ennehû tenvîhun ve delâletun ale'l-ma'nâ, gloss:ismin aslı sümüvdür, yücelikten gelir, çünkü bir şeyi anıp yükseltir ve anlamı gösterir, source:"س م و,B005"}. Bu ve bundan sonraki aile imgeleri kelimenin bu ayetteki anlamının yanında duyulur, onun yerine geçmez. Burada ism yalnızca "ad" demektir. Ama kökün bir kullanımı adın nasıl iş gördüğünü gözle görülür kılar. Çölde uzaktan seçilen bir karaltı için {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hatte'steŝbettuh, gloss:bir karaltı gözüme yükseldi, ben de onu iyice seçtim, source:"س م و,B002"} derlerdi. Ad da adlandırılanı belirsizliğin üstüne çıkarır. Onu seçilebilir ve çağrılabilir kılar. Aynı köke ilişkin bir başka tarif bu ayetin iki kelimesini tek cümlede buluşturur: {ar:به رفع ذكر المسمى, tr:bihî rufia ẕikru'l-musemmâ, gloss:adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Ad, anılışın yükseldiği yerdir. "Adını andı" demek, bir şeyi yükselten kelimeyi dilde yükseltmektir. Birinci ayet bu yönü "en yüce" sıfatıyla zaten başlatmıştı.

[¶10] Ẕikr kelimesi de bu yükselişe katılır. Bu kelime ün ve şeref anlamında da kullanılır: {ar:الذكر الشرف والصوت, tr:eẕ-ẕikru'ş-şerefu ve's-savt, gloss:zikir şeref ve yayılan ündür, source:"ذ ك ر,B007"}. Kur'an bu anlamı elçiye seslendiği kısa bir surede kullanır. Göğsünü açtığını ve sırtını büken yükü kaldırdığını hatırlattıktan sonra Allah şöyle der: {ar:وَرَفَعْنَا لَكَ ذِكْرَكَ, tr:ve rafa'nâ leke ẕikrak, gloss:senin anılışını yükselttik, source:94:4}. Ad ile anma, yükseltme fiiliyle birlikte Nûr suresinde de geçer. Allah'ın göklerin ve yerin nuru olduğunu anlatan benzetmenin ardından ışığın yandığı yerler gösterilir: {ar:فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ, tr:fî buyûtin eẕinallâhu en turfea ve yuẕkera fîhe'smuhû yusebbihu lehû fîhâ bi'l-ğuduvvi ve'l-âsâl, gloss:Allah'ın yükseltilmesine ve içlerinde adının anılmasına izin verdiği evlerde sabah akşam O'nu tesbih ederler, source:24:36}. Sonraki ayet o evlerdeki insanları anlatır: {ar:رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ, tr:ricâlun lâ tulhîhim ticâratun ve lâ bey'un an ẕikrillâhi ve ikâmi's-salâti ve îtâi'z-zekât, gloss:ne ticaretin ne alışverişin Allah'ı anmaktan, namazı kılmaktan ve zekâtı vermekten alıkoyduğu adamlar, source:24:37}. Bu surenin on dördüncü ve on beşinci ayetlerinde tek bir kişide toplanan anma, namaz ve arınma, orada bir topluluğun gündelik hayatıdır. Birinci ayetin tesbihi de o evlerde söylenir.

[¶11] Ad kelimesinin ailesinde bir de "adaş" vardır: {ar:سميا أي نظيرا له يستحق اسمه, tr:semiyyen ey nazîran lehû yestehıkku'smeh, gloss:semiy, onun adını hak eden bir dengi demektir, source:"س م و,B005"}. Kur'an bu kelimeyi Meryem suresinde, unutmayı ve adı yan yana getiren iki ayette kullanır. Önce, Rabbinin emri olmadan inmeyenlerin sözü olarak, şu söylenir: {ar:وَمَا كَانَ رَبُّكَ نَسِيًّۭا, tr:ve mâ kâne rabbuke nesiyyâ, gloss:Rabbin unutkan değildir, source:19:64}. Hemen ardından şu gelir: {ar:رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:rabbu's-semâvâti ve'l-ardi ve mâ beynehumâ fa'budhu vastabir li-ibâdetih, hel ta'lemu lehû semiyyâ, gloss:göklerin, yerin ve aralarındakilerin Rabbi; O'na kulluk et, kulluğunda sabırlı ol; O'nun adını taşımaya layık birini biliyor musun, source:19:65}. Orada da sıra bu ayettekine benzer: Rab unutmaz, adı başka kimseye yakışmaz ve bu adı bilen kulluğa yönelir. On beşinci ayetteki kişinin andığı ad, ortağı olmayan bir addır. Birinci ayetin tesbihi de bu adı ona yakışmayan her şeyden ayırmaktır.

[¶12] Kelimenin kökünü yükseklikle değil, damga ve işaret bildiren başka bir kökle açıklayan bir çözümleme de vardır. O kökte, kızgın demirle ya da kulağı kesilerek işaretlenen deve için {ar:بعير موسوم وسم بسمة يعرف بها, tr:baîrun mevsûmun vusime bi-simetin yu'rafu bihâ, gloss:damgalı deve, tanınacağı bir işaretle damgalanmıştır, source:"و س م,B001"} denir. Ayetteki kelimenin kökü bu değildir. Bu yalnızca bir başka okuyuştur. Ama adın ne işe yaradığını o da gösterir: ad, bir şeyin tanındığı işarettir. Namaz kılan kişi ise ilk sözünü bu işaretle söyler. Her namazda okunan Fatiha {ar:بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:bismillâhi'r-rahmâni'r-rahîm, gloss:Rahmân ve Rahîm olan Allah'ın adıyla, source:1:1} diye başlar ve hemen ardından Allah'ı {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabbi'l-âlemîn, gloss:âlemlerin Rabbi, source:1:2} diye anar. Yani namazın kendisi de bu ayetin sırasıyla başlar: önce ad ve Rab anılır, sonra beden eğilir. Kur'an'ın ilk emirlerinden biri de aynı iki kelimeyi yaratmayla birleştirir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}.

## Rab: sahibi ve yetiştireni

[¶13] Arapçada rabb önce sahip demektir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}. Gündelik dilde bir evin ya da bir atın sahibi için de söylenirdi: {ar:رب الدار ورب الفرس, tr:rabbu'd-dâri ve rabbu'l-feres, gloss:evin sahibi, atın sahibi, source:"ر ب ب,B001"}. Kelimenin bir başka kullanımı ise sahipliği bir emeğe çevirir. Bir şeyi adım adım yetiştirip tamama erdirmek de bu köktendir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi hâlden hâle geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}. Yapılan bir iyiliği eksiksiz hâle getiren için de {ar:رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe fulânun es-sanîate iẕâ etemmehâ ve aslahahâ, gloss:falanca iyiliğini tamamladı ve düzeltti, source:"ر ب ب,B002"} denirdi.

[¶14] Surenin açılışı Rabbi tam da bu adım adım işle tanıtır. O, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzgün biçime koyan, source:87:2} ve {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp biçen ve yol gösteren, source:87:3} olandır. Her adımdan sonra gelen "fe", bir sonraki aşamaya geçişi gösterir. Yağmur yüklü bir bulut türüne verilen ad da bu emeği gökyüzüne taşır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, summiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur, bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Dördüncü ayetteki otlağı çıkaran Rab, bu aile imgesinde bitkinin üstünde asılı duran ve onu besleyen bulutun yakınında duyulur.

[¶15] Ayetteki kelime "Rabbi"dir, yani onun Rabbi. Kişi, kendisine sahip olan ve onu hâlden hâle geçirerek yetiştirenin adını anar. On dördüncü ayetteki arınma da bir büyümedir, çünkü Araplar ekinin gelişmesini {ar:زكا الزرع, tr:zekâ'z-zer', gloss:ekin gelişti, source:"memory"} diye anlatırdı. Tezekkâ, insanın bu temizlenerek büyümeyi kendi üstüne almasıdır. Kur'an aynı iki fiili Şems suresinde, bir dizi yeminin sonunda yan yana koyar. Önce {ar:وَنَفْسٍۢ وَمَا سَوَّىٰهَا, tr:ve nefsin ve mâ sevvâhâ, gloss:nefse ve onu düzgün biçime koyana andolsun, source:91:7} denir. Sonra nefse kötülüğünün ve sakınmasının bildirildiği söylenir {source:91:8}. Ardından hüküm gelir: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad eflaha men zekkâhâ, gloss:onu arındırıp geliştiren kurtuluşa ermiştir, source:91:9}. Bu surede de çizgi aynıdır. İkinci ayette Rab "düzgün biçime koydu", on dördüncü ayette insan "arındı". Yetiştiren işini yapmış, yetiştirilen o işi sürdürmüştür. On beşinci ayette ise yetiştirilen kişi yetiştirenin adını anar.

## Namaz: dua, eğilen beden ve arkadan gelen

[¶16] "Namaz" Türkçeye Farsçadan geçmiştir. Arapça salât kelimesi Türkçede en çok "salavat" sözünde yaşar, ve orada asıl anlamlarından birini, başkası için iyilik dilemeyi korur. Fiilin ilk anlamı budur: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duâ, gloss:salât duadır, source:"ص ل و,B002"}. Kuralları belli olan ibadet de bu anlamdan çıkmış sayılırdı: {ar:الصلاة التي هي العبادة المخصوصة أصلها الدعاء, tr:es-salâtu'lletî hiye'l-ibâdetu'l-mahsûsa asluhe'd-duâ, gloss:o özel ibadet olan namazın aslı duadır, source:"ص ل و,B003"}. O ibadetin parçaları da tek tek sayılır: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rukûu ve's-sucûdu ve'd-duâu ve't-tesbîh, gloss:yaratılmışların namazı ayakta durmak, eğilmek, secdeye kapanmak, dua ve tesbihtir, source:"ص ل و,B003"}. Bu sayımın sonunda tesbih vardır. Demek ki birinci ayetin "tesbih et" emri, on beşinci ayetin "namaz kıldı" fiilinin içinde de yerine gelir.

[¶17] Namaz bedenle kılınır ve bu kelimenin ailesi de bedenin bir yerini adlandırır: {ar:الصلا وسط الظهر لكل ذي أربع وللناس, tr:es-salâ vasatu'z-zahri li-kulli ẕî erbain ve li'n-nâs, gloss:salâ dört ayaklıların ve insanların sırtının ortasıdır, source:"ص ل و,B005"}. Rükûda bükülen yer sırtın bu bölümüdür. Bu bir aile imgesidir, ayetteki kelimenin kökeni hakkında bir iddia değildir. Ama "kıldı" fiilinin yanında, eğilen bir sırtı göze getirir.

[¶18] Aynı harflerle kurulan aynı fiil biçimi, at yarışında da kullanılırdı. Öndeki atın hemen ardından gelen at için {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen li-enne ra'sehû yetlu's-salâ'lleẕî beyne yedeyh, gloss:sallâ etti, musallî olarak geldi, çünkü başı önündekinin sağrısını izler, source:"ص ل و,B006"} denirdi. Kısaca {ar:المصلى تالي السابق, tr:el-musallî tâli's-sâbık, gloss:musallî öne geçenin ardından gelendir, source:"ص ل و,B006"}. Bu ayetin "fe-sallâ"sı, bu kullanımın yanında bir izleme hareketi olarak duyulur. Namaz anmanın hemen arkasından gelir, ikinci atın başının birincinin sırtında durması gibi, arada boşluk bırakmadan. Kişinin bütün işi de surenin başında verilmiş bir emrin ardından gitmektir. On altıncı ayetin "öne almak" fiili, on yedinci ayetin "son" kelimesiyle birlikte, surede bir öndekiler ve arkadakiler dizisi kurar. Namaz kılan kişi o dizide doğru olanın izinden gelendir. Kelimenin bu ayetteki anlamı yine de namazdır.

[¶19] Salât kelimesi iki yönde de kullanılır. İnsandan Allah'a doğru dua ve namazdır. Allah'tan insana doğru ise başka bir anlam taşır: {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtullâhi li'l-muslimîne tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı onları arındırmasıdır, source:"ص ل و,B002"}. Meleklerden gelen salât ise {ar:صلاة الملائكة الاستغفار, tr:salâtu'l-melâiketi'l-istiğfâr, gloss:meleklerin salâtı bağışlanma dilemektir, source:"ص ل و,B002"}. Böylece on dördüncü ayetin "arındı"sı ile on beşinci ayetin "kıldı"sı, yukarıdan bakıldığında Allah'ın tek bir işinin iki adı olur. Kur'an bu karşılıklılığı Ahzâb suresinde, müminlere seslenirken açıkça kurar: {ar:يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا, tr:yâ eyyuhe'lleẕîne âmenuẕkurullâhe ẕikran keŝîrâ, gloss:ey iman edenler, Allah'ı çokça anın, source:33:41}, {ar:وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا, tr:ve sebbihûhu bukraten ve asîlâ, gloss:sabah akşam O'nu tesbih edin, source:33:42}, {ar:هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ لِيُخْرِجَكُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:huve'lleẕî yusallî aleykum ve melâiketuhû li-yuhricekum mine'z-zulumâti ile'n-nûr, gloss:sizi karanlıklardan aydınlığa çıkarmak için size salât eden O'dur, melekleri de, source:33:43}. Bu üç ayette surenin üç fiili, anmak, tesbih etmek ve salât, bir arada geçer. Ama salâtın öznesi değişmiştir. Anan ve tesbih eden insana, Allah ve melekleri salât eder.

[¶20] Arınma ile salât, Tevbe suresinde elçinin elinde de yan yana durur. Söz, günahlarını itiraf eden ve iyi işi kötüsüyle karıştıran insanlar hakkındadır {source:9:102}. Allah elçiye şöyle der: {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ, tr:huẕ min emvâlihim sadakaten tutahhiruhum ve tuzekkîhim bihâ ve salli aleyhim, inne salâteke sekenun lehum, gloss:mallarından bir sadaka al, onunla onları temizleyip arındırırsın; onlar için dua et, senin duan onlara huzur verir, source:9:103}. Mü'minûn suresi ise bu surenin on dördüncü ayetindeki sözle açılır: {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad eflaha'l-mu'minûn, gloss:müminler kurtuluşa ermiştir, source:23:1}. Hemen ardından bu müminlerin ilk niteliği sayılır: {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:elleẕîne hum fî salâtihim hâşiûn, gloss:onlar namazlarında huşu içindedirler, source:23:2}. Biraz sonra da {ar:وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ, tr:velleẕîne hum li'z-zekâti fâilûn, gloss:onlar zekâtı yerine getirirler, source:23:4} denir. Zekât, "arındı" fiiliyle aynı kökten gelir. Orada da kurtuluş, namaz ve arınma birlikte anılır.

[¶21] Kelimenin ailesi bir mekânı da adlandırır: {ar:يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات, tr:yusemmâ mevdiu'l-ibâdeti's-salâh, ve li-ẕâlike summiyeti'l-kenâisu salavât, gloss:ibadet yerine salât denir, bu yüzden mabetlere salavât adı verilmiştir, source:"ص ل و,B007"}. Kur'an bu kelimeyi Hac suresinde, haksız yere yurtlarından çıkarılanlara savaş izni verildiği yerde kullanır. Bu insanların tek suçu {ar:رَبُّنَا ٱللَّهُ, tr:rabbunallâh, gloss:Rabbimiz Allah'tır, source:22:40} demeleridir. Ayet şöyle sürer: Allah insanların bir kısmını ötekilerle savmasaydı {ar:لَّهُدِّمَتْ صَوَٰمِعُ وَبِيَعٌۭ وَصَلَوَٰتٌۭ وَمَسَٰجِدُ يُذْكَرُ فِيهَا ٱسْمُ ٱللَّهِ كَثِيرًۭا, tr:le-huddimet savâmiu ve biyaun ve salavâtun ve mesâcidu yuẕkeru fîhe'smullâhi keŝîrâ, gloss:manastırlar, kiliseler, havralar ve içlerinde Allah'ın adı çokça anılan mescitler yıkılıp giderdi, source:22:40}. Bu ayetin dört kelimesi de, yani Rab, salât, anmak ve ad, o tek ayette bulunur. On beşinci ayette tek bir kişinin yaptığı iş, Hac suresinde birçok topluluğun mabetlerinde yaşar.

[¶22] Surenin son ayeti bu işin eskiliğini de söyler. Sayfaları anılan İbrahim'in duası, Kur'an'da onun kendi ağzından aktarılır. İbrahim soyunun bir kısmını ekin bitmeyen bir vadiye, Allah'ın kutsal evinin yanına yerleştirmiştir ve amacını şöyle söyler: {ar:رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ, tr:rabbenâ li-yukîmu's-salâh, gloss:Rabbimiz, namazı kılsınlar diye, source:14:37}. Biraz sonra kendisi için de ister: {ar:رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ, tr:rabbi'c'alnî mukîme's-salâti ve min ẕurriyyetî, rabbenâ ve tekabbel duâ, gloss:Rabbim, beni ve soyumdan gelenleri namazı kılanlardan eyle; Rabbimiz, duamı kabul et, source:14:40}. İbrahim'in ağzında namaz ve dua yan yana söylenir, tıpkı bu fiilin iki anlamı gibi. On beşinci ayetteki kişi, İbrahim'in olmak istediği kişidir.

## İki ateş: yaslâ ile sallâ

[¶23] On ikinci ayetteki "yaslâ", yani ateşe girer, ile on beşinci ayetteki "sallâ", yani namaz kıldı, aynı iki ünsüzü taşır ve aynı sesle biter. Ama son harfleri farklıdır. Birinin kökü ص ل ي, ötekinin ص ل و'dur. Aralarındaki yakınlık bir ses yankısıdır, kök birliği değildir. Ateş için kullanılan fiil yakıcılığa katlanmayı anlatır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi, yani onun sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Sure bu yankıyı iki karşıt insana bölüştürür. Öğütten kaçınan ateşe girer. Rabbinin adını anan namaz kılar.

[¶24] Aynı harflerle kurulan aynı fiil biçimi ateşin bir başka işini de adlandırır. Eğri bir değneği düzeltmek için onu ateşin üstünde çeviren kişi için {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:sallâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateş üstünde çevirdi, onu düzeltip doğrultmak için, source:"ص ل ي,B004"} derlerdi. Ayetin fiilinin kendi ailesinde de bu kullanım vardır: {ar:صليت العود بالنار, tr:salleytu'l-ûde bi'n-nâr, gloss:değneği ateşle yumuşatıp düzelttim, source:"ص ل و,B001"}. Yani Arapça bu harflerle iki ateş tanır. Birine insan atılır ve onun yakıcılığına katlanır. Ötekinin üstünde eğri bir değnek tutulur, yanmadan ısınır ve doğrulur. Sure ilkini on ikinci ayette en bedbaht kişiye açıkça verir. İkincisini söylemez. O yalnızca bir ses yakınlığı olarak, "sallâ" kelimesinin yanında duyulur. Namaz kılan kişi, ateşin içine atılan değil, ateşin üstünde tutulup doğrultulan değnek gibidir. İkinci ayetteki "düzgün biçime koydu" fiili de bu doğrultmanın yakınında durur. Ama bu bağ dilin bir yankısıdır, ayetin söylediği bir şey değildir. Ayetin "sallâ"sı namaz kıldı demektir.

[¶25] Kur'an bu ayetin tam tersini Kıyâmet suresinde, ölüm anını anlatırken kurar. Can köprücük kemiklerine dayanmıştır {source:75:26}, ve o gün sevk edilecek yer Rabbin huzurudur {source:75:30}. Sonra o kişinin hayatı tek cümleyle özetlenir: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe-lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne de namaz kıldı, source:75:31}, {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin keẕẕebe ve tevellâ, gloss:tersine yalanladı ve sırt çevirdi, source:75:32}, {ar:ثُمَّ ذَهَبَ إِلَىٰٓ أَهْلِهِۦ يَتَمَطَّىٰٓ, tr:ŝumme ẕehebe ilâ ehlihî yetemettâ, gloss:sonra çalım satarak ailesinin yanına gitti, source:75:33}. Bu ayetin "fe-sallâ"sı orada "lâ sallâ" olur. Sırt çevirmek de on birinci ayette öğütten kaçınmanın karşılığıdır. Aynı ses, aynı kalıp ve aynı uyak iki hayatı birbirinden ayırır. On ikinci ayetin ateşindekiler de Müddessir suresinde neden oraya girdikleri sorulunca {ar:لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:lem neku mine'l-musallîn, gloss:namaz kılanlardan değildik, source:74:43} diye cevap verirler. Bu cevapta, bu surenin iki fiili arasındaki ayrım bir itiraf olarak duyulur.

===== _commentary/v16/out/87_15/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: ṣallaytu/ṣallā al-ʿaṣā (form II) is used for turning a staff over fire to straighten it
- memory: zakā al-zarʿ, meaning "the crop grew"
- memory: tazakkā and zakāt share the root z-k-w
- memory: "namaz" came into Turkish from Persian; Turkish "salavat" keeps the sense of blessing
- memory: fa- marks a step that follows with no delay, plus consequence
- not written: dhikr as male and as hard steel or a sharp sword (B001, B002) - no part in remembering a name
- not written: dhikr al-ḥaqq as a written deed (B008) - no theme in this ayah
- not written: s-m-w sky, rain, roof (B004) - pulls toward the surah's height scene, adds nothing here
- not written: s-m-w hunting, stallion, rivalry, good repute (B003, B006-B008) - no work in this ayah
- not written: brand mark linked to rabb as owner - rests on the alternative root plus outside custom
- not written: w-s-m first rain, festival season, beauty, dye plant - not identity; no theme
- not written: rabb multitude, stepchild, syrup, staying, covenant, captain, etc. (B004-B007, B009-B017) - no support for a theme
- not written: ṣ-l-w trap, pounding stone, ṣilliyān camel fodder (B004, B008, B009) - fodder-to-pasture link too thin
- not written: 29:45, 62:9-10, 107:4-5 - repeat connections already made
- not written: 24:37 said to follow the 14-15 order - the order differs, so the claim was dropped

===== passages not cited (280) =====
## strong (this ayah's own list) (53)

- (2:152) [listed for 87:15] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
- (3:191) [listed for 87:15] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
- (4:102) [listed for 87:15] وَإِذَا كُنتَ فِيهِمْ فَأَقَمْتَ لَهُمُ ٱلصَّلَوٰةَ فَلْتَقُمْ طَآئِفَةٌۭ مِّنْهُم مَّعَكَ وَلْيَأْخُذُوٓا۟ أَسْلِحَتَهُمْ فَإِذَا سَجَدُوا۟ فَلْيَكُونُوا۟ مِن وَرَآئِكُمْ وَلْتَأْتِ طَآئِفَةٌ أُخْرَىٰ لَمْ يُصَلُّوا۟ فَلْيُصَلُّوا۟ مَعَكَ وَلْيَأْخُذُوا۟ حِذْرَهُمْ وَأَسْلِحَتَهُمْ ۗ وَدَّ ٱلَّذِينَ كَفَرُوا۟ لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةًۭ وَٰحِدَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ إِن كَانَ بِكُمْ أَذًۭى مِّن مَّطَرٍ أَوْ كُنتُم مَّرْضَىٰٓ أَن تَضَعُوٓا۟ أَسْلِحَتَكُمْ ۖ وَخُذُوا۟ حِذْرَكُمْ ۗ إِنَّ ٱللَّهَ أَعَدَّ لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
- (4:103) [listed for 87:15] فَإِذَا قَضَيْتُمُ ٱلصَّلَوٰةَ فَٱذْكُرُوا۟ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِكُمْ ۚ فَإِذَا ٱطْمَأْنَنتُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ ۚ إِنَّ ٱلصَّلَوٰةَ كَانَتْ عَلَى ٱلْمُؤْمِنِينَ كِتَٰبًۭا مَّوْقُوتًۭا
- (5:91) [listed for 87:15] إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
- (6:162) [listed for 87:15] قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (7:205) [listed for 87:15] وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ بِٱلْغُدُوِّ وَٱلْءَاصَالِ وَلَا تَكُن مِّنَ ٱلْغَٰفِلِينَ
- (11:87) [listed for 87:15] قَالُوا۟ يَٰشُعَيْبُ أَصَلَوٰتُكَ تَأْمُرُكَ أَن نَّتْرُكَ مَا يَعْبُدُ ءَابَآؤُنَآ أَوْ أَن نَّفْعَلَ فِىٓ أَمْوَٰلِنَا مَا نَشَٰٓؤُا۟ ۖ إِنَّكَ لَأَنتَ ٱلْحَلِيمُ ٱلرَّشِيدُ
- (11:114) [listed for 87:15] وَأَقِمِ ٱلصَّلَوٰةَ طَرَفَىِ ٱلنَّهَارِ وَزُلَفًۭا مِّنَ ٱلَّيْلِ ۚ إِنَّ ٱلْحَسَنَٰتِ يُذْهِبْنَ ٱلسَّيِّـَٔاتِ ۚ ذَٰلِكَ ذِكْرَىٰ لِلذَّٰكِرِينَ
- (13:28) [listed for 87:15] ٱلَّذِينَ ءَامَنُوا۟ وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ ٱللَّهِ ۗ أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ
- (14:40) [listed for 87:15] [cited in ¶22] رَبِّ ٱجْعَلْنِى مُقِيمَ ٱلصَّلَوٰةِ وَمِن ذُرِّيَّتِى ۚ رَبَّنَا وَتَقَبَّلْ دُعَآءِ
- (15:98) [listed for 87:15] فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ ٱلسَّٰجِدِينَ
- (17:78) [listed for 87:15] أَقِمِ ٱلصَّلَوٰةَ لِدُلُوكِ ٱلشَّمْسِ إِلَىٰ غَسَقِ ٱلَّيْلِ وَقُرْءَانَ ٱلْفَجْرِ ۖ إِنَّ قُرْءَانَ ٱلْفَجْرِ كَانَ مَشْهُودًۭا
- (17:110) [listed for 87:15] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (18:28) [listed for 87:15] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (19:55) [listed for 87:15] وَكَانَ يَأْمُرُ أَهْلَهُۥ بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ وَكَانَ عِندَ رَبِّهِۦ مَرْضِيًّۭا
- (19:59) [listed for 87:15] ۞ فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌ أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ ۖ فَسَوْفَ يَلْقَوْنَ غَيًّا
- (20:14) [listed for 87:15] [cited in ¶8] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
- (20:33) [listed for 87:15] كَىْ نُسَبِّحَكَ كَثِيرًۭا
- (20:34) [listed for 87:15] وَنَذْكُرَكَ كَثِيرًا
- (20:130) [listed for 87:15] فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا ۖ وَمِنْ ءَانَآئِ ٱلَّيْلِ فَسَبِّحْ وَأَطْرَافَ ٱلنَّهَارِ لَعَلَّكَ تَرْضَىٰ
- (20:132) [listed for 87:15] وَأْمُرْ أَهْلَكَ بِٱلصَّلَوٰةِ وَٱصْطَبِرْ عَلَيْهَا ۖ لَا نَسْـَٔلُكَ رِزْقًۭا ۖ نَّحْنُ نَرْزُقُكَ ۗ وَٱلْعَٰقِبَةُ لِلتَّقْوَىٰ
- (21:73) [listed for 87:15] وَجَعَلْنَٰهُمْ أَئِمَّةًۭ يَهْدُونَ بِأَمْرِنَا وَأَوْحَيْنَآ إِلَيْهِمْ فِعْلَ ٱلْخَيْرَٰتِ وَإِقَامَ ٱلصَّلَوٰةِ وَإِيتَآءَ ٱلزَّكَوٰةِ ۖ وَكَانُوا۟ لَنَا عَٰبِدِينَ
- (22:35) [listed for 87:15] ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَٱلصَّٰبِرِينَ عَلَىٰ مَآ أَصَابَهُمْ وَٱلْمُقِيمِى ٱلصَّلَوٰةِ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (22:41) [listed for 87:15] ٱلَّذِينَ إِن مَّكَّنَّٰهُمْ فِى ٱلْأَرْضِ أَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ وَأَمَرُوا۟ بِٱلْمَعْرُوفِ وَنَهَوْا۟ عَنِ ٱلْمُنكَرِ ۗ وَلِلَّهِ عَٰقِبَةُ ٱلْأُمُورِ
- (24:37) [listed for 87:15] [cited in ¶10] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
- (24:56) [listed for 87:15] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَطِيعُوا۟ ٱلرَّسُولَ لَعَلَّكُمْ تُرْحَمُونَ
- (29:45) [listed for 87:15] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
- (30:31) [listed for 87:15] ۞ مُنِيبِينَ إِلَيْهِ وَٱتَّقُوهُ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَلَا تَكُونُوا۟ مِنَ ٱلْمُشْرِكِينَ
- (33:35) [listed for 87:15] إِنَّ ٱلْمُسْلِمِينَ وَٱلْمُسْلِمَٰتِ وَٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ وَٱلْقَٰنِتِينَ وَٱلْقَٰنِتَٰتِ وَٱلصَّٰدِقِينَ وَٱلصَّٰدِقَٰتِ وَٱلصَّٰبِرِينَ وَٱلصَّٰبِرَٰتِ وَٱلْخَٰشِعِينَ وَٱلْخَٰشِعَٰتِ وَٱلْمُتَصَدِّقِينَ وَٱلْمُتَصَدِّقَٰتِ وَٱلصَّٰٓئِمِينَ وَٱلصَّٰٓئِمَٰتِ وَٱلْحَٰفِظِينَ فُرُوجَهُمْ وَٱلْحَٰفِظَٰتِ وَٱلذَّٰكِرِينَ ٱللَّهَ كَثِيرًۭا وَٱلذَّٰكِرَٰتِ أَعَدَّ ٱللَّهُ لَهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۭا
- (33:41) [listed for 87:15] [cited in ¶19] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (33:42) [listed for 87:15] [cited in ¶19] وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا
- (43:36) [listed for 87:15] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
- (50:39) [listed for 87:15] فَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ ٱلْغُرُوبِ
- (50:40) [listed for 87:15] وَمِنَ ٱلَّيْلِ فَسَبِّحْهُ وَأَدْبَٰرَ ٱلسُّجُودِ
- (52:48) [listed for 87:15] وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا ۖ وَسَبِّحْ بِحَمْدِ رَبِّكَ حِينَ تَقُومُ
- (53:29) [listed for 87:15] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (53:62) [listed for 87:15] فَٱسْجُدُوا۟ لِلَّهِ وَٱعْبُدُوا۟ ۩
- (57:16) [listed for 87:15] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (62:9) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (62:10) [listed for 87:15] فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
- (63:9) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (70:22) [listed for 87:15] إِلَّا ٱلْمُصَلِّينَ
- (70:23) [listed for 87:15] ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ
- (73:8) [listed for 87:15] [cited in ¶7] وَٱذْكُرِ ٱسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًۭا
- (73:20) [listed for 87:15] ۞ إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌۭ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا وَأَعْظَمَ أَجْرًۭا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۢ
- (74:43) [listed for 87:15] [cited in ¶25] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
- (76:25) [listed for 87:15] [cited in ¶7] وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةًۭ وَأَصِيلًۭا
- (76:26) [listed for 87:15] [cited in ¶7] وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ وَسَبِّحْهُ لَيْلًۭا طَوِيلًا
- (96:1) [listed for 87:15] [cited in ¶12] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- (96:19) [listed for 87:15] كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩
- (107:4) [listed for 87:15] فَوَيْلٌۭ لِّلْمُصَلِّينَ
- (108:2) [listed for 87:15] فَصَلِّ لِرَبِّكَ وَٱنْحَرْ

## medium (this ayah's own list) (98)

- (2:43) [listed for 87:15] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ
- (2:45) [listed for 87:15] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
- (2:110) [listed for 87:15] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ ۗ إِنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (2:125) [listed for 87:15] وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا وَٱتَّخِذُوا۟ مِن مَّقَامِ إِبْرَٰهِۦمَ مُصَلًّۭى ۖ وَعَهِدْنَآ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ أَن طَهِّرَا بَيْتِىَ لِلطَّآئِفِينَ وَٱلْعَٰكِفِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ
- (2:153) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ إِنَّ ٱللَّهَ مَعَ ٱلصَّٰبِرِينَ
- (2:157) [listed for 87:15] أُو۟لَٰٓئِكَ عَلَيْهِمْ صَلَوَٰتٌۭ مِّن رَّبِّهِمْ وَرَحْمَةٌۭ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُهْتَدُونَ
- (2:186) [listed for 87:15] وَإِذَا سَأَلَكَ عِبَادِى عَنِّى فَإِنِّى قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ ۖ فَلْيَسْتَجِيبُوا۟ لِى وَلْيُؤْمِنُوا۟ بِى لَعَلَّهُمْ يَرْشُدُونَ
- (2:238) [listed for 87:15] حَٰفِظُوا۟ عَلَى ٱلصَّلَوَٰتِ وَٱلصَّلَوٰةِ ٱلْوُسْطَىٰ وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ
- (2:239) [listed for 87:15] فَإِنْ خِفْتُمْ فَرِجَالًا أَوْ رُكْبَانًۭا ۖ فَإِذَآ أَمِنتُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَمَا عَلَّمَكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
- (2:277) [listed for 87:15] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ لَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (3:39) [listed for 87:15] فَنَادَتْهُ ٱلْمَلَٰٓئِكَةُ وَهُوَ قَآئِمٌۭ يُصَلِّى فِى ٱلْمِحْرَابِ أَنَّ ٱللَّهَ يُبَشِّرُكَ بِيَحْيَىٰ مُصَدِّقًۢا بِكَلِمَةٍۢ مِّنَ ٱللَّهِ وَسَيِّدًۭا وَحَصُورًۭا وَنَبِيًّۭا مِّنَ ٱلصَّٰلِحِينَ
- (3:41) [listed for 87:15] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۖ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَةَ أَيَّامٍ إِلَّا رَمْزًۭا ۗ وَٱذْكُر رَّبَّكَ كَثِيرًۭا وَسَبِّحْ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
- (3:113) [listed for 87:15] ۞ لَيْسُوا۟ سَوَآءًۭ ۗ مِّنْ أَهْلِ ٱلْكِتَٰبِ أُمَّةٌۭ قَآئِمَةٌۭ يَتْلُونَ ءَايَٰتِ ٱللَّهِ ءَانَآءَ ٱلَّيْلِ وَهُمْ يَسْجُدُونَ
- (4:43) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْرَبُوا۟ ٱلصَّلَوٰةَ وَأَنتُمْ سُكَٰرَىٰ حَتَّىٰ تَعْلَمُوا۟ مَا تَقُولُونَ وَلَا جُنُبًا إِلَّا عَابِرِى سَبِيلٍ حَتَّىٰ تَغْتَسِلُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُمْ ۗ إِنَّ ٱللَّهَ كَانَ عَفُوًّا غَفُورًا
- (4:77) [listed for 87:15] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
- (4:142) [listed for 87:15] إِنَّ ٱلْمُنَٰفِقِينَ يُخَٰدِعُونَ ٱللَّهَ وَهُوَ خَٰدِعُهُمْ وَإِذَا قَامُوٓا۟ إِلَى ٱلصَّلَوٰةِ قَامُوا۟ كُسَالَىٰ يُرَآءُونَ ٱلنَّاسَ وَلَا يَذْكُرُونَ ٱللَّهَ إِلَّا قَلِيلًۭا
- (4:162) [listed for 87:15] لَّٰكِنِ ٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ مِنْهُمْ وَٱلْمُؤْمِنُونَ يُؤْمِنُونَ بِمَآ أُنزِلَ إِلَيْكَ وَمَآ أُنزِلَ مِن قَبْلِكَ ۚ وَٱلْمُقِيمِينَ ٱلصَّلَوٰةَ ۚ وَٱلْمُؤْتُونَ ٱلزَّكَوٰةَ وَٱلْمُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ أُو۟لَٰٓئِكَ سَنُؤْتِيهِمْ أَجْرًا عَظِيمًا
- (5:4) [listed for 87:15] يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
- (5:6) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (5:12) [listed for 87:15] ۞ وَلَقَدْ أَخَذَ ٱللَّهُ مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ وَبَعَثْنَا مِنْهُمُ ٱثْنَىْ عَشَرَ نَقِيبًۭا ۖ وَقَالَ ٱللَّهُ إِنِّى مَعَكُمْ ۖ لَئِنْ أَقَمْتُمُ ٱلصَّلَوٰةَ وَءَاتَيْتُمُ ٱلزَّكَوٰةَ وَءَامَنتُم بِرُسُلِى وَعَزَّرْتُمُوهُمْ وَأَقْرَضْتُمُ ٱللَّهَ قَرْضًا حَسَنًۭا لَّأُكَفِّرَنَّ عَنكُمْ سَيِّـَٔاتِكُمْ وَلَأُدْخِلَنَّكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ فَمَن كَفَرَ بَعْدَ ذَٰلِكَ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (5:58) [listed for 87:15] وَإِذَا نَادَيْتُمْ إِلَى ٱلصَّلَوٰةِ ٱتَّخَذُوهَا هُزُوًۭا وَلَعِبًۭا ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْقِلُونَ
- (6:52) [listed for 87:15] وَلَا تَطْرُدِ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ مَا عَلَيْكَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَمَا مِنْ حِسَابِكَ عَلَيْهِم مِّن شَىْءٍۢ فَتَطْرُدَهُمْ فَتَكُونَ مِنَ ٱلظَّٰلِمِينَ
- (6:72) [listed for 87:15] وَأَنْ أَقِيمُوا۟ ٱلصَّلَوٰةَ وَٱتَّقُوهُ ۚ وَهُوَ ٱلَّذِىٓ إِلَيْهِ تُحْشَرُونَ
- (6:118) [listed for 87:15] فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ إِن كُنتُم بِـَٔايَٰتِهِۦ مُؤْمِنِينَ
- (6:121) [listed for 87:15] وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ وَإِنَّهُۥ لَفِسْقٌۭ ۗ وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ ۖ وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ
- (6:138) [listed for 87:15] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
- (7:170) [listed for 87:15] وَٱلَّذِينَ يُمَسِّكُونَ بِٱلْكِتَٰبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ إِنَّا لَا نُضِيعُ أَجْرَ ٱلْمُصْلِحِينَ
- (7:180) [listed for 87:15] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
- (8:2) [listed for 87:15] إِنَّمَا ٱلْمُؤْمِنُونَ ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَإِذَا تُلِيَتْ عَلَيْهِمْ ءَايَٰتُهُۥ زَادَتْهُمْ إِيمَٰنًۭا وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (8:3) [listed for 87:15] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (8:35) [listed for 87:15] وَمَا كَانَ صَلَاتُهُمْ عِندَ ٱلْبَيْتِ إِلَّا مُكَآءًۭ وَتَصْدِيَةًۭ ۚ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (9:5) [listed for 87:15] فَإِذَا ٱنسَلَخَ ٱلْأَشْهُرُ ٱلْحُرُمُ فَٱقْتُلُوا۟ ٱلْمُشْرِكِينَ حَيْثُ وَجَدتُّمُوهُمْ وَخُذُوهُمْ وَٱحْصُرُوهُمْ وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ ۚ فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَخَلُّوا۟ سَبِيلَهُمْ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (9:11) [listed for 87:15] فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ ۗ وَنُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (9:18) [listed for 87:15] إِنَّمَا يَعْمُرُ مَسَٰجِدَ ٱللَّهِ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَلَمْ يَخْشَ إِلَّا ٱللَّهَ ۖ فَعَسَىٰٓ أُو۟لَٰٓئِكَ أَن يَكُونُوا۟ مِنَ ٱلْمُهْتَدِينَ
- (9:54) [listed for 87:15] وَمَا مَنَعَهُمْ أَن تُقْبَلَ مِنْهُمْ نَفَقَٰتُهُمْ إِلَّآ أَنَّهُمْ كَفَرُوا۟ بِٱللَّهِ وَبِرَسُولِهِۦ وَلَا يَأْتُونَ ٱلصَّلَوٰةَ إِلَّا وَهُمْ كُسَالَىٰ وَلَا يُنفِقُونَ إِلَّا وَهُمْ كَٰرِهُونَ
- (9:71) [listed for 87:15] وَٱلْمُؤْمِنُونَ وَٱلْمُؤْمِنَٰتُ بَعْضُهُمْ أَوْلِيَآءُ بَعْضٍۢ ۚ يَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَيُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَيُطِيعُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ سَيَرْحَمُهُمُ ٱللَّهُ ۗ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
- (9:112) [listed for 87:15] ٱلتَّٰٓئِبُونَ ٱلْعَٰبِدُونَ ٱلْحَٰمِدُونَ ٱلسَّٰٓئِحُونَ ٱلرَّٰكِعُونَ ٱلسَّٰجِدُونَ ٱلْءَامِرُونَ بِٱلْمَعْرُوفِ وَٱلنَّاهُونَ عَنِ ٱلْمُنكَرِ وَٱلْحَٰفِظُونَ لِحُدُودِ ٱللَّهِ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (10:87) [listed for 87:15] وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰ وَأَخِيهِ أَن تَبَوَّءَا لِقَوْمِكُمَا بِمِصْرَ بُيُوتًۭا وَٱجْعَلُوا۟ بُيُوتَكُمْ قِبْلَةًۭ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- (13:22) [listed for 87:15] وَٱلَّذِينَ صَبَرُوا۟ ٱبْتِغَآءَ وَجْهِ رَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ وَيَدْرَءُونَ بِٱلْحَسَنَةِ ٱلسَّيِّئَةَ أُو۟لَٰٓئِكَ لَهُمْ عُقْبَى ٱلدَّارِ
- (14:31) [listed for 87:15] قُل لِّعِبَادِىَ ٱلَّذِينَ ءَامَنُوا۟ يُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُنفِقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا بَيْعٌۭ فِيهِ وَلَا خِلَٰلٌ
- (14:37) [listed for 87:15] [cited in ¶22] رَّبَّنَآ إِنِّىٓ أَسْكَنتُ مِن ذُرِّيَّتِى بِوَادٍ غَيْرِ ذِى زَرْعٍ عِندَ بَيْتِكَ ٱلْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا۟ ٱلصَّلَوٰةَ فَٱجْعَلْ أَفْـِٔدَةًۭ مِّنَ ٱلنَّاسِ تَهْوِىٓ إِلَيْهِمْ وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ
- (17:79) [listed for 87:15] وَمِنَ ٱلَّيْلِ فَتَهَجَّدْ بِهِۦ نَافِلَةًۭ لَّكَ عَسَىٰٓ أَن يَبْعَثَكَ رَبُّكَ مَقَامًۭا مَّحْمُودًۭا
- (19:31) [listed for 87:15] وَجَعَلَنِى مُبَارَكًا أَيْنَ مَا كُنتُ وَأَوْصَٰنِى بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ مَا دُمْتُ حَيًّۭا
- (19:65) [listed for 87:15] [cited in ¶11] رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ ۚ هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا
- (20:42) [listed for 87:15] ٱذْهَبْ أَنتَ وَأَخُوكَ بِـَٔايَٰتِى وَلَا تَنِيَا فِى ذِكْرِى
- (22:28) [listed for 87:15] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:34) [listed for 87:15] وَلِكُلِّ أُمَّةٍۢ جَعَلْنَا مَنسَكًۭا لِّيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۗ فَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ فَلَهُۥٓ أَسْلِمُوا۟ ۗ وَبَشِّرِ ٱلْمُخْبِتِينَ
- (22:36) [listed for 87:15] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (22:40) [listed for 87:15] [cited in ¶21] ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِم بِغَيْرِ حَقٍّ إِلَّآ أَن يَقُولُوا۟ رَبُّنَا ٱللَّهُ ۗ وَلَوْلَا دَفْعُ ٱللَّهِ ٱلنَّاسَ بَعْضَهُم بِبَعْضٍۢ لَّهُدِّمَتْ صَوَٰمِعُ وَبِيَعٌۭ وَصَلَوَٰتٌۭ وَمَسَٰجِدُ يُذْكَرُ فِيهَا ٱسْمُ ٱللَّهِ كَثِيرًۭا ۗ وَلَيَنصُرَنَّ ٱللَّهُ مَن يَنصُرُهُۥٓ ۗ إِنَّ ٱللَّهَ لَقَوِىٌّ عَزِيزٌ
- (22:77) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱرْكَعُوا۟ وَٱسْجُدُوا۟ وَٱعْبُدُوا۟ رَبَّكُمْ وَٱفْعَلُوا۟ ٱلْخَيْرَ لَعَلَّكُمْ تُفْلِحُونَ ۩
- (23:1) [listed for 87:15] [cited in ¶20] قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ
- (23:2) [listed for 87:15] [cited in ¶20] ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ
- (23:9) [listed for 87:15] وَٱلَّذِينَ هُمْ عَلَىٰ صَلَوَٰتِهِمْ يُحَافِظُونَ
- (24:36) [listed for 87:15] [cited in ¶10] فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا بِٱلْغُدُوِّ وَٱلْءَاصَالِ
- (24:41) [listed for 87:15] أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ ۖ كُلٌّۭ قَدْ عَلِمَ صَلَاتَهُۥ وَتَسْبِيحَهُۥ ۗ وَٱللَّهُ عَلِيمٌۢ بِمَا يَفْعَلُونَ
- (25:64) [listed for 87:15] وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدًۭا وَقِيَٰمًۭا
- (25:77) [listed for 87:15] قُلْ مَا يَعْبَؤُا۟ بِكُمْ رَبِّى لَوْلَا دُعَآؤُكُمْ ۖ فَقَدْ كَذَّبْتُمْ فَسَوْفَ يَكُونُ لِزَامًۢا
- (27:3) [listed for 87:15] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (31:4) [listed for 87:15] ٱلَّذِينَ يُقِيمُونَ ٱلصَّلَوٰةَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ
- (32:15) [listed for 87:15] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
- (32:16) [listed for 87:15] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (33:21) [listed for 87:15] لَّقَدْ كَانَ لَكُمْ فِى رَسُولِ ٱللَّهِ أُسْوَةٌ حَسَنَةٌۭ لِّمَن كَانَ يَرْجُوا۟ ٱللَّهَ وَٱلْيَوْمَ ٱلْءَاخِرَ وَذَكَرَ ٱللَّهَ كَثِيرًۭا
- (33:33) [listed for 87:15] وَقَرْنَ فِى بُيُوتِكُنَّ وَلَا تَبَرَّجْنَ تَبَرُّجَ ٱلْجَٰهِلِيَّةِ ٱلْأُولَىٰ ۖ وَأَقِمْنَ ٱلصَّلَوٰةَ وَءَاتِينَ ٱلزَّكَوٰةَ وَأَطِعْنَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ إِنَّمَا يُرِيدُ ٱللَّهُ لِيُذْهِبَ عَنكُمُ ٱلرِّجْسَ أَهْلَ ٱلْبَيْتِ وَيُطَهِّرَكُمْ تَطْهِيرًۭا
- (33:43) [listed for 87:15] [cited in ¶19] هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ لِيُخْرِجَكُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَكَانَ بِٱلْمُؤْمِنِينَ رَحِيمًۭا
- (33:56) [listed for 87:15] إِنَّ ٱللَّهَ وَمَلَٰٓئِكَتَهُۥ يُصَلُّونَ عَلَى ٱلنَّبِىِّ ۚ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ صَلُّوا۟ عَلَيْهِ وَسَلِّمُوا۟ تَسْلِيمًا
- (35:18) [listed for 87:15] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
- (35:29) [listed for 87:15] إِنَّ ٱلَّذِينَ يَتْلُونَ كِتَٰبَ ٱللَّهِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ يَرْجُونَ تِجَٰرَةًۭ لَّن تَبُورَ
- (37:13) [listed for 87:15] وَإِذَا ذُكِّرُوا۟ لَا يَذْكُرُونَ
- (37:155) [listed for 87:15] أَفَلَا تَذَكَّرُونَ
- (38:18) [listed for 87:15] إِنَّا سَخَّرْنَا ٱلْجِبَالَ مَعَهُۥ يُسَبِّحْنَ بِٱلْعَشِىِّ وَٱلْإِشْرَاقِ
- (38:32) [listed for 87:15] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
- (39:9) [listed for 87:15] أَمَّنْ هُوَ قَٰنِتٌ ءَانَآءَ ٱلَّيْلِ سَاجِدًۭا وَقَآئِمًۭا يَحْذَرُ ٱلْءَاخِرَةَ وَيَرْجُوا۟ رَحْمَةَ رَبِّهِۦ ۗ قُلْ هَلْ يَسْتَوِى ٱلَّذِينَ يَعْلَمُونَ وَٱلَّذِينَ لَا يَعْلَمُونَ ۗ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (39:22) [listed for 87:15] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (39:45) [listed for 87:15] وَإِذَا ذُكِرَ ٱللَّهُ وَحْدَهُ ٱشْمَأَزَّتْ قُلُوبُ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ ۖ وَإِذَا ذُكِرَ ٱلَّذِينَ مِن دُونِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
- (40:14) [listed for 87:15] فَٱدْعُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (40:55) [listed for 87:15] فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَسَبِّحْ بِحَمْدِ رَبِّكَ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
- (41:38) [listed for 87:15] فَإِنِ ٱسْتَكْبَرُوا۟ فَٱلَّذِينَ عِندَ رَبِّكَ يُسَبِّحُونَ لَهُۥ بِٱلَّيْلِ وَٱلنَّهَارِ وَهُمْ لَا يَسْـَٔمُونَ ۩
- (51:55) [listed for 87:15] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
- (52:49) [listed for 87:15] وَمِنَ ٱلَّيْلِ فَسَبِّحْهُ وَإِدْبَٰرَ ٱلنُّجُومِ
- (54:22) [listed for 87:15] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
- (55:78) [listed for 87:15] تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- (56:74) [listed for 87:15] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (56:96) [listed for 87:15] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (58:13) [listed for 87:15] ءَأَشْفَقْتُمْ أَن تُقَدِّمُوا۟ بَيْنَ يَدَىْ نَجْوَىٰكُمْ صَدَقَٰتٍۢ ۚ فَإِذْ لَمْ تَفْعَلُوا۟ وَتَابَ ٱللَّهُ عَلَيْكُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَطِيعُوا۟ ٱللَّهَ وَرَسُولَهُۥ ۚ وَٱللَّهُ خَبِيرٌۢ بِمَا تَعْمَلُونَ
- (58:19) [listed for 87:15] ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ حِزْبُ ٱلشَّيْطَٰنِ ۚ أَلَآ إِنَّ حِزْبَ ٱلشَّيْطَٰنِ هُمُ ٱلْخَٰسِرُونَ
- (69:52) [listed for 87:15] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (70:34) [listed for 87:15] وَٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ
- (72:17) [listed for 87:15] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
- (72:18) [listed for 87:15] وَأَنَّ ٱلْمَسَٰجِدَ لِلَّهِ فَلَا تَدْعُوا۟ مَعَ ٱللَّهِ أَحَدًۭا
- (74:42) [listed for 87:15] مَا سَلَكَكُمْ فِى سَقَرَ
- (74:54) [listed for 87:15] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
- (74:55) [listed for 87:15] فَمَن شَآءَ ذَكَرَهُۥ
- (75:31) [listed for 87:15] [cited in ¶25] فَلَا صَدَّقَ وَلَا صَلَّىٰ
- (80:11) [listed for 87:15] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
- (80:12) [listed for 87:15] فَمَن شَآءَ ذَكَرَهُۥ
- (96:9) [listed for 87:15] أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- (96:10) [listed for 87:15] عَبْدًا إِذَا صَلَّىٰٓ
- (98:5) [listed for 87:15] وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ

## named by the passage's own list as strong for this ayah (4)

- (2:200) [listed for 87:15] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
- (18:24) [listed for 87:15] إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ وَقُلْ عَسَىٰٓ أَن يَهْدِيَنِ رَبِّى لِأَقْرَبَ مِنْ هَٰذَا رَشَدًۭا
- (59:19) [listed for 87:15] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
- (107:5) [listed for 87:15] ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ

## named by the passage's own list as medium for this ayah (13)

- (2:3) [listed for 87:15] ٱلَّذِينَ يُؤْمِنُونَ بِٱلْغَيْبِ وَيُقِيمُونَ ٱلصَّلَوٰةَ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (2:114) [listed for 87:15] وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ وَسَعَىٰ فِى خَرَابِهَآ ۚ أُو۟لَٰٓئِكَ مَا كَانَ لَهُمْ أَن يَدْخُلُوهَآ إِلَّا خَآئِفِينَ ۚ لَهُمْ فِى ٱلدُّنْيَا خِزْىٌۭ وَلَهُمْ فِى ٱلْءَاخِرَةِ عَذَابٌ عَظِيمٌۭ
- (7:206) [listed for 87:15] إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ وَيُسَبِّحُونَهُۥ وَلَهُۥ يَسْجُدُونَ ۩
- (19:11) [listed for 87:15] فَخَرَجَ عَلَىٰ قَوْمِهِۦ مِنَ ٱلْمِحْرَابِ فَأَوْحَىٰٓ إِلَيْهِمْ أَن سَبِّحُوا۟ بُكْرَةًۭ وَعَشِيًّۭا
- (19:60) [listed for 87:15] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ شَيْـًۭٔا
- (25:62) [listed for 87:15] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (33:34) [listed for 87:15] وَٱذْكُرْنَ مَا يُتْلَىٰ فِى بُيُوتِكُنَّ مِنْ ءَايَٰتِ ٱللَّهِ وَٱلْحِكْمَةِ ۚ إِنَّ ٱللَّهَ كَانَ لَطِيفًا خَبِيرًا
- (38:46) [listed for 87:15] إِنَّآ أَخْلَصْنَٰهُم بِخَالِصَةٍۢ ذِكْرَى ٱلدَّارِ
- (43:44) [listed for 87:15] وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ
- (53:25) [listed for 87:15] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (73:19) [listed for 87:15] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
- (92:20) [listed for 87:15] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (94:4) [listed for 87:15] [cited in ¶10] وَرَفَعْنَا لَكَ ذِكْرَكَ

## weak (this ayah's own list) (24)

- (2:37) [listed for 87:15] فَتَلَقَّىٰٓ ءَادَمُ مِن رَّبِّهِۦ كَلِمَٰتٍۢ فَتَابَ عَلَيْهِ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:124) [listed for 87:15] ۞ وَإِذِ ٱبْتَلَىٰٓ إِبْرَٰهِۦمَ رَبُّهُۥ بِكَلِمَٰتٍۢ فَأَتَمَّهُنَّ ۖ قَالَ إِنِّى جَاعِلُكَ لِلنَّاسِ إِمَامًۭا ۖ قَالَ وَمِن ذُرِّيَّتِى ۖ قَالَ لَا يَنَالُ عَهْدِى ٱلظَّٰلِمِينَ
- (2:131) [listed for 87:15] إِذْ قَالَ لَهُۥ رَبُّهُۥٓ أَسْلِمْ ۖ قَالَ أَسْلَمْتُ لِرَبِّ ٱلْعَٰلَمِينَ
- (2:282) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (6:70) [listed for 87:15] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (6:119) [listed for 87:15] وَمَا لَكُمْ أَلَّا تَأْكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ وَقَدْ فَصَّلَ لَكُم مَّا حَرَّمَ عَلَيْكُمْ إِلَّا مَا ٱضْطُرِرْتُمْ إِلَيْهِ ۗ وَإِنَّ كَثِيرًۭا لَّيُضِلُّونَ بِأَهْوَآئِهِم بِغَيْرِ عِلْمٍ ۗ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِٱلْمُعْتَدِينَ
- (9:99) [listed for 87:15] وَمِنَ ٱلْأَعْرَابِ مَن يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَيَتَّخِذُ مَا يُنفِقُ قُرُبَٰتٍ عِندَ ٱللَّهِ وَصَلَوَٰتِ ٱلرَّسُولِ ۚ أَلَآ إِنَّهَا قُرْبَةٌۭ لَّهُمْ ۚ سَيُدْخِلُهُمُ ٱللَّهُ فِى رَحْمَتِهِۦٓ ۗ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (10:10) [listed for 87:15] دَعْوَىٰهُمْ فِيهَا سُبْحَٰنَكَ ٱللَّهُمَّ وَتَحِيَّتُهُمْ فِيهَا سَلَٰمٌۭ ۚ وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (21:10) [listed for 87:15] لَقَدْ أَنزَلْنَآ إِلَيْكُمْ كِتَٰبًۭا فِيهِ ذِكْرُكُمْ ۖ أَفَلَا تَعْقِلُونَ
- (21:24) [listed for 87:15] أَمِ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ ۖ قُلْ هَاتُوا۟ بُرْهَٰنَكُمْ ۖ هَٰذَا ذِكْرُ مَن مَّعِىَ وَذِكْرُ مَن قَبْلِى ۗ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ ٱلْحَقَّ ۖ فَهُم مُّعْرِضُونَ
- (36:58) [listed for 87:15] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (38:1) [listed for 87:15] صٓ ۚ وَٱلْقُرْءَانِ ذِى ٱلذِّكْرِ
- (47:20) [listed for 87:15] وَيَقُولُ ٱلَّذِينَ ءَامَنُوا۟ لَوْلَا نُزِّلَتْ سُورَةٌۭ ۖ فَإِذَآ أُنزِلَتْ سُورَةٌۭ مُّحْكَمَةٌۭ وَذُكِرَ فِيهَا ٱلْقِتَالُ ۙ رَأَيْتَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ يَنظُرُونَ إِلَيْكَ نَظَرَ ٱلْمَغْشِىِّ عَلَيْهِ مِنَ ٱلْمَوْتِ ۖ فَأَوْلَىٰ لَهُمْ
- (49:11) [listed for 87:15] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا يَسْخَرْ قَوْمٌۭ مِّن قَوْمٍ عَسَىٰٓ أَن يَكُونُوا۟ خَيْرًۭا مِّنْهُمْ وَلَا نِسَآءٌۭ مِّن نِّسَآءٍ عَسَىٰٓ أَن يَكُنَّ خَيْرًۭا مِّنْهُنَّ ۖ وَلَا تَلْمِزُوٓا۟ أَنفُسَكُمْ وَلَا تَنَابَزُوا۟ بِٱلْأَلْقَٰبِ ۖ بِئْسَ ٱلِٱسْمُ ٱلْفُسُوقُ بَعْدَ ٱلْإِيمَٰنِ ۚ وَمَن لَّمْ يَتُبْ فَأُو۟لَٰٓئِكَ هُمُ ٱلظَّٰلِمُونَ
- (53:49) [listed for 87:15] وَأَنَّهُۥ هُوَ رَبُّ ٱلشِّعْرَىٰ
- (55:17) [listed for 87:15] رَبُّ ٱلْمَشْرِقَيْنِ وَرَبُّ ٱلْمَغْرِبَيْنِ
- (55:21) [listed for 87:15] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (55:53) [listed for 87:15] فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- (61:6) [listed for 87:15] وَإِذْ قَالَ عِيسَى ٱبْنُ مَرْيَمَ يَٰبَنِىٓ إِسْرَٰٓءِيلَ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُم مُّصَدِّقًۭا لِّمَا بَيْنَ يَدَىَّ مِنَ ٱلتَّوْرَىٰةِ وَمُبَشِّرًۢا بِرَسُولٍۢ يَأْتِى مِنۢ بَعْدِى ٱسْمُهُۥٓ أَحْمَدُ ۖ فَلَمَّا جَآءَهُم بِٱلْبَيِّنَٰتِ قَالُوا۟ هَٰذَا سِحْرٌۭ مُّبِينٌۭ
- (68:50) [listed for 87:15] فَٱجْتَبَٰهُ رَبُّهُۥ فَجَعَلَهُۥ مِنَ ٱلصَّٰلِحِينَ
- (68:51) [listed for 87:15] وَإِن يَكَادُ ٱلَّذِينَ كَفَرُوا۟ لَيُزْلِقُونَكَ بِأَبْصَٰرِهِمْ لَمَّا سَمِعُوا۟ ٱلذِّكْرَ وَيَقُولُونَ إِنَّهُۥ لَمَجْنُونٌۭ
- (84:15) [listed for 87:15] بَلَىٰٓ إِنَّ رَبَّهُۥ كَانَ بِهِۦ بَصِيرًۭا
- (89:28) [listed for 87:15] ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- (100:11) [listed for 87:15] إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ

## named by the passage's own list as weak for this ayah (13)

- (2:63) [listed for 87:15] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (4:101) [listed for 87:15] وَإِذَا ضَرَبْتُمْ فِى ٱلْأَرْضِ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَقْصُرُوا۟ مِنَ ٱلصَّلَوٰةِ إِنْ خِفْتُمْ أَن يَفْتِنَكُمُ ٱلَّذِينَ كَفَرُوٓا۟ ۚ إِنَّ ٱلْكَٰفِرِينَ كَانُوا۟ لَكُمْ عَدُوًّۭا مُّبِينًۭا
- (6:92) [listed for 87:15] وَهَٰذَا كِتَٰبٌ أَنزَلْنَٰهُ مُبَارَكٌۭ مُّصَدِّقُ ٱلَّذِى بَيْنَ يَدَيْهِ وَلِتُنذِرَ أُمَّ ٱلْقُرَىٰ وَمَنْ حَوْلَهَا ۚ وَٱلَّذِينَ يُؤْمِنُونَ بِٱلْءَاخِرَةِ يُؤْمِنُونَ بِهِۦ ۖ وَهُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ
- (9:103) [listed for 87:15] [cited in ¶20] خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
- (19:3) [listed for 87:15] إِذْ نَادَىٰ رَبَّهُۥ نِدَآءً خَفِيًّۭا
- (19:7) [listed for 87:15] يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا
- (20:25) [listed for 87:15] قَالَ رَبِّ ٱشْرَحْ لِى صَدْرِى
- (20:122) [listed for 87:15] ثُمَّ ٱجْتَبَٰهُ رَبُّهُۥ فَتَابَ عَلَيْهِ وَهَدَىٰ
- (42:38) [listed for 87:15] وَٱلَّذِينَ ٱسْتَجَابُوا۟ لِرَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَمْرُهُمْ شُورَىٰ بَيْنَهُمْ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
- (55:46) [listed for 87:15] وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- (69:12) [listed for 87:15] لِنَجْعَلَهَا لَكُمْ تَذْكِرَةًۭ وَتَعِيَهَآ أُذُنٌۭ وَٰعِيَةٌۭ
- (88:18) [listed for 87:15] وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- (89:15) [listed for 87:15] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ

## neighbours: within two ayat of a passage the commentary cites (75)

- (1:3) [next to 1:1] ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (1:4) [next to 1:2] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (9:100) [next to 9:102] وَٱلسَّٰبِقُونَ ٱلْأَوَّلُونَ مِنَ ٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ وَٱلَّذِينَ ٱتَّبَعُوهُم بِإِحْسَٰنٍۢ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (9:101) [next to 9:102] وَمِمَّنْ حَوْلَكُم مِّنَ ٱلْأَعْرَابِ مُنَٰفِقُونَ ۖ وَمِنْ أَهْلِ ٱلْمَدِينَةِ ۖ مَرَدُوا۟ عَلَى ٱلنِّفَاقِ لَا تَعْلَمُهُمْ ۖ نَحْنُ نَعْلَمُهُمْ ۚ سَنُعَذِّبُهُم مَّرَّتَيْنِ ثُمَّ يُرَدُّونَ إِلَىٰ عَذَابٍ عَظِيمٍۢ
- (9:104) [next to 9:102] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ هُوَ يَقْبَلُ ٱلتَّوْبَةَ عَنْ عِبَادِهِۦ وَيَأْخُذُ ٱلصَّدَقَٰتِ وَأَنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (9:105) [next to 9:103] وَقُلِ ٱعْمَلُوا۟ فَسَيَرَى ٱللَّهُ عَمَلَكُمْ وَرَسُولُهُۥ وَٱلْمُؤْمِنُونَ ۖ وَسَتُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (14:35) [next to 14:37] وَإِذْ قَالَ إِبْرَٰهِيمُ رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ
- (14:36) [next to 14:37] رَبِّ إِنَّهُنَّ أَضْلَلْنَ كَثِيرًۭا مِّنَ ٱلنَّاسِ ۖ فَمَن تَبِعَنِى فَإِنَّهُۥ مِنِّى ۖ وَمَنْ عَصَانِى فَإِنَّكَ غَفُورٌۭ رَّحِيمٌۭ
- (14:38) [next to 14:37] رَبَّنَآ إِنَّكَ تَعْلَمُ مَا نُخْفِى وَمَا نُعْلِنُ ۗ وَمَا يَخْفَىٰ عَلَى ٱللَّهِ مِن شَىْءٍۢ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (14:39) [next to 14:37] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى وَهَبَ لِى عَلَى ٱلْكِبَرِ إِسْمَٰعِيلَ وَإِسْحَٰقَ ۚ إِنَّ رَبِّى لَسَمِيعُ ٱلدُّعَآءِ
- (14:41) [next to 14:40] رَبَّنَا ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ ٱلْحِسَابُ
- (14:42) [next to 14:40] وَلَا تَحْسَبَنَّ ٱللَّهَ غَٰفِلًا عَمَّا يَعْمَلُ ٱلظَّٰلِمُونَ ۚ إِنَّمَا يُؤَخِّرُهُمْ لِيَوْمٍۢ تَشْخَصُ فِيهِ ٱلْأَبْصَٰرُ
- (15:4) [next to 15:6] وَمَآ أَهْلَكْنَا مِن قَرْيَةٍ إِلَّا وَلَهَا كِتَابٌۭ مَّعْلُومٌۭ
- (15:5) [next to 15:6] مَّا تَسْبِقُ مِنْ أُمَّةٍ أَجَلَهَا وَمَا يَسْتَـْٔخِرُونَ
- (15:7) [next to 15:6] لَّوْ مَا تَأْتِينَا بِٱلْمَلَٰٓئِكَةِ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ
- (15:8) [next to 15:6] مَا نُنَزِّلُ ٱلْمَلَٰٓئِكَةَ إِلَّا بِٱلْحَقِّ وَمَا كَانُوٓا۟ إِذًۭا مُّنظَرِينَ
- (15:10) [next to 15:9] وَلَقَدْ أَرْسَلْنَا مِن قَبْلِكَ فِى شِيَعِ ٱلْأَوَّلِينَ
- (15:11) [next to 15:9] وَمَا يَأْتِيهِم مِّن رَّسُولٍ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (19:62) [next to 19:64] لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا ۖ وَلَهُمْ رِزْقُهُمْ فِيهَا بُكْرَةًۭ وَعَشِيًّۭا
- (19:63) [next to 19:64] تِلْكَ ٱلْجَنَّةُ ٱلَّتِى نُورِثُ مِنْ عِبَادِنَا مَن كَانَ تَقِيًّۭا
- (19:66) [next to 19:64] وَيَقُولُ ٱلْإِنسَٰنُ أَءِذَا مَا مِتُّ لَسَوْفَ أُخْرَجُ حَيًّا
- (19:67) [next to 19:65] أَوَلَا يَذْكُرُ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن قَبْلُ وَلَمْ يَكُ شَيْـًۭٔا
- (20:12) [next to 20:14] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
- (20:13) [next to 20:14] وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ
- (20:15) [next to 20:14] إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا لِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا تَسْعَىٰ
- (20:16) [next to 20:14] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- (22:38) [next to 22:40] ۞ إِنَّ ٱللَّهَ يُدَٰفِعُ عَنِ ٱلَّذِينَ ءَامَنُوٓا۟ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ كُلَّ خَوَّانٍۢ كَفُورٍ
- (22:39) [next to 22:40] أُذِنَ لِلَّذِينَ يُقَٰتَلُونَ بِأَنَّهُمْ ظُلِمُوا۟ ۚ وَإِنَّ ٱللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ
- (22:42) [next to 22:40] وَإِن يُكَذِّبُوكَ فَقَدْ كَذَّبَتْ قَبْلَهُمْ قَوْمُ نُوحٍۢ وَعَادٌۭ وَثَمُودُ
- (23:0) [next to 23:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (23:3) [next to 23:1] وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ
- (23:5) [next to 23:4] وَٱلَّذِينَ هُمْ لِفُرُوجِهِمْ حَٰفِظُونَ
- (23:6) [next to 23:4] إِلَّا عَلَىٰٓ أَزْوَٰجِهِمْ أَوْ مَا مَلَكَتْ أَيْمَٰنُهُمْ فَإِنَّهُمْ غَيْرُ مَلُومِينَ
- (24:34) [next to 24:36] وَلَقَدْ أَنزَلْنَآ إِلَيْكُمْ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ وَمَثَلًۭا مِّنَ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُمْ وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
- (24:35) [next to 24:36] ۞ ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ مَثَلُ نُورِهِۦ كَمِشْكَوٰةٍۢ فِيهَا مِصْبَاحٌ ۖ ٱلْمِصْبَاحُ فِى زُجَاجَةٍ ۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوْكَبٌۭ دُرِّىٌّۭ يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ لَّا شَرْقِيَّةٍۢ وَلَا غَرْبِيَّةٍۢ يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ ۚ نُّورٌ عَلَىٰ نُورٍۢ ۗ يَهْدِى ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ ۚ وَيَضْرِبُ ٱللَّهُ ٱلْأَمْثَٰلَ لِلنَّاسِ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (24:38) [next to 24:36] لِيَجْزِيَهُمُ ٱللَّهُ أَحْسَنَ مَا عَمِلُوا۟ وَيَزِيدَهُم مِّن فَضْلِهِۦ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
- (24:39) [next to 24:37] وَٱلَّذِينَ كَفَرُوٓا۟ أَعْمَٰلُهُمْ كَسَرَابٍۭ بِقِيعَةٍۢ يَحْسَبُهُ ٱلظَّمْـَٔانُ مَآءً حَتَّىٰٓ إِذَا جَآءَهُۥ لَمْ يَجِدْهُ شَيْـًۭٔا وَوَجَدَ ٱللَّهَ عِندَهُۥ فَوَفَّىٰهُ حِسَابَهُۥ ۗ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
- (33:39) [next to 33:41] ٱلَّذِينَ يُبَلِّغُونَ رِسَٰلَٰتِ ٱللَّهِ وَيَخْشَوْنَهُۥ وَلَا يَخْشَوْنَ أَحَدًا إِلَّا ٱللَّهَ ۗ وَكَفَىٰ بِٱللَّهِ حَسِيبًۭا
- (33:40) [next to 33:41] مَّا كَانَ مُحَمَّدٌ أَبَآ أَحَدٍۢ مِّن رِّجَالِكُمْ وَلَٰكِن رَّسُولَ ٱللَّهِ وَخَاتَمَ ٱلنَّبِيِّۦنَ ۗ وَكَانَ ٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (33:44) [next to 33:42] تَحِيَّتُهُمْ يَوْمَ يَلْقَوْنَهُۥ سَلَٰمٌۭ ۚ وَأَعَدَّ لَهُمْ أَجْرًۭا كَرِيمًۭا
- (33:45) [next to 33:43] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِنَّآ أَرْسَلْنَٰكَ شَٰهِدًۭا وَمُبَشِّرًۭا وَنَذِيرًۭا
- (73:0) [next to 73:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (73:1) [next to 73:2] يَٰٓأَيُّهَا ٱلْمُزَّمِّلُ
- (73:3) [next to 73:2] نِّصْفَهُۥٓ أَوِ ٱنقُصْ مِنْهُ قَلِيلًا
- (73:4) [next to 73:2] أَوْ زِدْ عَلَيْهِ وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا
- (73:6) [next to 73:8] إِنَّ نَاشِئَةَ ٱلَّيْلِ هِىَ أَشَدُّ وَطْـًۭٔا وَأَقْوَمُ قِيلًا
- (73:7) [next to 73:8] إِنَّ لَكَ فِى ٱلنَّهَارِ سَبْحًۭا طَوِيلًۭا
- (73:9) [next to 73:8] رَّبُّ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ لَآ إِلَٰهَ إِلَّا هُوَ فَٱتَّخِذْهُ وَكِيلًۭا
- (73:10) [next to 73:8] وَٱصْبِرْ عَلَىٰ مَا يَقُولُونَ وَٱهْجُرْهُمْ هَجْرًۭا جَمِيلًۭا
- (74:41) [next to 74:43] عَنِ ٱلْمُجْرِمِينَ
- (74:44) [next to 74:43] وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ
- (74:45) [next to 74:43] وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ
- (75:24) [next to 75:26] وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ
- (75:25) [next to 75:26] تَظُنُّ أَن يُفْعَلَ بِهَا فَاقِرَةٌۭ
- (75:27) [next to 75:26] وَقِيلَ مَنْ ۜ رَاقٍۢ
- (75:28) [next to 75:26] وَظَنَّ أَنَّهُ ٱلْفِرَاقُ
- (75:29) [next to 75:30] وَٱلْتَفَّتِ ٱلسَّاقُ بِٱلسَّاقِ
- (75:34) [next to 75:32] أَوْلَىٰ لَكَ فَأَوْلَىٰ
- (75:35) [next to 75:33] ثُمَّ أَوْلَىٰ لَكَ فَأَوْلَىٰٓ
- (76:21) [next to 76:23] عَٰلِيَهُمْ ثِيَابُ سُندُسٍ خُضْرٌۭ وَإِسْتَبْرَقٌۭ ۖ وَحُلُّوٓا۟ أَسَاوِرَ مِن فِضَّةٍۢ وَسَقَىٰهُمْ رَبُّهُمْ شَرَابًۭا طَهُورًا
- (76:22) [next to 76:23] إِنَّ هَٰذَا كَانَ لَكُمْ جَزَآءًۭ وَكَانَ سَعْيُكُم مَّشْكُورًا
- (76:24) [next to 76:23] فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًۭا
- (76:27) [next to 76:25] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
- (76:28) [next to 76:26] نَّحْنُ خَلَقْنَٰهُمْ وَشَدَدْنَآ أَسْرَهُمْ ۖ وَإِذَا شِئْنَا بَدَّلْنَآ أَمْثَٰلَهُمْ تَبْدِيلًا
- (91:5) [next to 91:7] وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- (91:6) [next to 91:7] وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- (91:10) [next to 91:8] وَقَدْ خَابَ مَن دَسَّىٰهَا
- (91:11) [next to 91:9] كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- (94:2) [next to 94:4] وَوَضَعْنَا عَنكَ وِزْرَكَ
- (94:3) [next to 94:4] ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- (94:5) [next to 94:4] فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- (94:6) [next to 94:4] إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- (96:0) [next to 96:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (96:2) [next to 96:1] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- (96:3) [next to 96:1] ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ

